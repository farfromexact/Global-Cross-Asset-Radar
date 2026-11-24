"""Publish three Markdown reports from the manual GPT inbox. Standard library only.

The same file is deployed to the report repository. No model, scheduler, data
collector, or research-quality certification is involved.
"""
import argparse
import base64
from datetime import datetime, timezone, timedelta
import hashlib
from io import BytesIO
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile

REPOSITORY = 'farfromexact/Global-Cross-Asset-Radar'
REMOTE = 'https://github.com/' + REPOSITORY + '.git'
DOMAINS = ('global', 'commodities', 'free')
EXAMPLE_BODIES = {'global': '全球报告全文', 'commodities': '商品报告全文', 'free': 'Free Report 全文'}
FORMAT = 'radar_text_archive_v1'
BJT = timezone(timedelta(hours=8))
MARKER = re.compile(r'^<!-- radar:(global|commodities|free) -->\r?\n', re.M)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def utc(value):
    stamp = datetime.fromisoformat(value.replace('Z', '+00:00'))
    require(stamp.tzinfo is not None, 'Timestamp needs a timezone')
    return stamp.astimezone(timezone.utc)


def iso(value):
    return value.astimezone(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def parse_submission(raw):
    require(len(raw) <= 4_000_000, 'Submission exceeds 4 MB')
    text = raw.decode('utf-8-sig')
    require('\x00' not in text, 'NUL byte in report')
    markers = list(MARKER.finditer(text))
    require([m.group(1) for m in markers] == list(DOMAINS),
            'Expected exactly global, commodities, free report markers in that order')
    require(not text[:markers[0].start()].strip(), 'Unexpected content before first report')
    reports = {}
    for i, match in enumerate(markers):
        end = markers[i + 1].start() if i + 1 < len(markers) else len(text)
        body = text[match.end():end]
        domain = match.group(1)
        stripped = body.strip()
        require(stripped, 'Empty report: ' + domain)
        require(stripped not in EXAMPLE_BODIES.values(), 'Unfilled delivery example: ' + domain)
        reports[domain] = body
    return reports


def receipt_path(path):
    require(re.fullmatch(r'inbox/gpt/[A-Za-z0-9][A-Za-z0-9._-]*\.md', path), 'Invalid inbox filename')
    return 'receipts/gpt/' + PurePosixPath(path).stem + '.json'


class GitError(ValueError):
    def __init__(self, message, *, retryable=True):
        super().__init__(message)
        self.retryable = retryable


def git_failure(operation, result):
    # Only fixed labels leave the process. Credential helpers can write secrets to stderr.
    stderr = result.stderr.lower()
    categories = (
        ('protected branch', False, (b'protected branch', b'gh006', b'gh013')),
        ('authentication or permission denied', False, (b'authentication failed', b'could not read username',
                                                       b'error: 401', b'error: 403', b'permission denied')),
        ('remote branch changed', True, (b'non-fast-forward', b'fetch first', b'cannot lock ref')),
        ('network failure', True, (b'could not resolve host', b'failed to connect', b'connection reset',
                                   b'connection timed out')),
    )
    for label, retryable, markers in categories:
        if any(marker in stderr for marker in markers):
            return GitError(f'git {operation} failed (exit {result.returncode}, {label})', retryable=retryable)
    return GitError(f'git {operation} failed (exit {result.returncode})')


class GitStore:
    def __init__(self, directory, remote=REMOTE, branch='main'):
        self.root = Path(directory)
        self.root.mkdir(parents=True, exist_ok=True)
        self.branch = branch
        self.git('clone', '--quiet', '--no-local', '--single-branch', '--no-tags', '--branch', branch,
                 '--config', 'core.autocrlf=false', '--config', 'user.name=Radar archive tool',
                 '--config', 'user.email=radar-archive@users.noreply.github.com', '--', remote, '.')

    def git(self, *args, stdin=None):
        env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
        token = env.get('RADAR_ARCHIVE_TOKEN')
        if token:
            count = int(env.get('GIT_CONFIG_COUNT', '0'))
            env.update({'GIT_CONFIG_COUNT': str(count + 1),
                        'GIT_CONFIG_KEY_' + str(count): 'http.https://github.com/.extraheader',
                        'GIT_CONFIG_VALUE_' + str(count): 'AUTHORIZATION: basic ' +
                            base64.b64encode(('x-access-token:' + token).encode()).decode()})
        try:
            result = subprocess.run(['git', '-C', str(self.root), *args], input=stdin,
                                    capture_output=True, timeout=120, env=env)
        except subprocess.TimeoutExpired:
            raise GitError(f'git {args[0]} timed out after 120s') from None
        if result.returncode:
            raise git_failure(args[0], result)
        return result.stdout

    def checked_path(self, path):
        target = (self.root / path).resolve()
        require(target.is_relative_to(self.root.resolve()), 'Path outside archive')
        require(not (self.root / path).is_symlink(), 'Archive file must not be a symlink')
        return target

    def read(self, path):
        target = self.checked_path(path)
        return target.read_bytes() if target.is_file() else None

    def source(self, path):
        detail = self.git('log', '-1', '--format=%H%x09%cI', '--', path).decode().strip()
        commit, _, stamp = detail.partition('\t')
        require(re.fullmatch(r'[a-f0-9]{40}', commit), 'Missing submission commit')
        return {'path': path, 'commit': commit, 'submitted_at_utc': iso(utc(stamp))}

    def historical_receipt(self, path):
        # Older failed receipts did not retain their original archived identity.
        commits = self.git('log', '--no-renames', '--diff-filter=AM', '--format=%H', '--', path).splitlines()
        for commit in commits:
            previous = json.loads(self.git('show', commit.decode('ascii') + ':' + path))
            if previous.get('status') == 'archived':
                return previous
        return None

    def commit(self, changes, message):
        for path, raw in changes.items():
            target = self.checked_path(path)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        self.git('add', '--', *changes)
        if self.git('diff', '--cached', '--name-only').strip():
            self.git('commit', '-q', '-m', message)
            self.git('push', 'origin', 'HEAD:refs/heads/' + self.branch)
        commit = self.git('rev-parse', 'HEAD').decode().strip()
        self.git('fetch', 'origin', self.branch)
        self.git('merge-base', '--is-ancestor', commit, 'FETCH_HEAD')
        requests = ''.join(f'{commit}:{path}\n' for path in changes).encode('utf-8')
        blobs = BytesIO(self.git('cat-file', '--batch', stdin=requests))
        for path, expected in changes.items():
            # Each response has an object header, the exact blob bytes, and one delimiter.
            header = blobs.readline().split()
            if (len(header) != 3 or header[1] != b'blob' or header[2] != str(len(expected)).encode()
                    or blobs.read(len(expected)) != expected or blobs.read(1) != b'\n'):
                # The push may already have succeeded. Reload the checkout and its index together.
                raise GitError('Remote readback mismatch: ' + path)
        if blobs.read(1):
            raise GitError('Unexpected trailing Git readback data')
        return commit


def read_json(store, path, default=None):
    raw = store.read(path)
    return json.loads(raw) if raw is not None else default


class RunIndex:
    """Index for a single checkout. Advance it only after the final commit succeeds."""

    def __init__(self, store):
        self.document = read_json(store, 'manifests/runs.json',
                                  {'schema_version': 'radar_runs_v2', 'archive_mode': 'production', 'runs': []})
        require(isinstance(self.document, dict) and
                self.document.get('schema_version') in ('radar_runs_v1', 'radar_runs_v2') and
                self.document.get('archive_mode') == 'production' and isinstance(self.document.get('runs'), list),
                'Invalid run index')
        self.by_id = {}
        self.by_hash = {}
        for row in self.document['runs']:
            require(row['run_id'] not in self.by_id, 'Duplicate run_id in existing index')
            self.remember(row)

    def remember(self, row):
        self.by_id[row['run_id']] = row
        if row.get('submission_sha256'):
            self.by_hash.setdefault(row['submission_sha256'], row)


def receipt_history(store, name):
    current = read_json(store, name)
    if current is None:
        return None, None
    require(isinstance(current, dict), 'Invalid submission receipt')
    if current.get('status') == 'archived':
        return current, current
    require(current.get('status') == 'failed', 'Unexpected submission receipt status')
    archived = current['archived_receipt'] if 'archived_receipt' in current else store.historical_receipt(name)
    require(archived is None or (isinstance(archived, dict) and archived.get('status') == 'archived'),
            'Invalid prior archive receipt')
    return current, archived


def check_archived(store, manifest_ref):
    raw = store.read(manifest_ref['path'])
    require(raw is not None and digest(raw) == manifest_ref['sha256'], 'Archived manifest mismatch')
    manifest = json.loads(raw)
    require(manifest['archive_format'] == FORMAT and manifest['archive_status'] == 'verified',
            'Archive is not complete')
    for domain in DOMAINS:
        for kind in ('markdown', 'json'):
            ref = manifest['reports'][domain][kind]
            data = store.read(ref['path'])
            require(data is not None and digest(data) == ref['sha256'], 'Archived report mismatch: ' + ref['path'])
    return manifest


def order(record):
    # New entries are ordered by submission, not an invented research cutoff.
    stamp = record.get('submitted_at_utc') or record.get('started_at_utc')
    return utc(stamp), record['run_id']


def make_receipt(manifest, manifest_ref, source_hash):
    return {'status': 'archived', 'archive_format': FORMAT, 'run_id': manifest['run_id'],
            'submission_sha256': source_hash, 'manifest': manifest_ref,
            'verification': 'six_report_files_read_back',
            'research_quality': 'not_certified_by_archive_tool',
            'reports': {d: 'https://github.com/' + REPOSITORY + '/blob/main/' +
                        manifest['reports'][d]['markdown']['path'] for d in DOMAINS}}


def publish(store, path, *, index=None, source=None):
    receipt_name = receipt_path(path)
    raw = store.read(path)
    require(raw is not None, 'Submission not found')
    content_hash = digest(raw)
    index = index if index is not None else RunIndex(store)
    current, archived = receipt_history(store, receipt_name)
    if archived is not None:
        require(archived['submission_sha256'] == content_hash, 'Published inbox file changed; use a new filename')
        check_archived(store, archived['manifest'])
        row = index.by_id.get(archived['run_id'])
        require(row is not None and row['manifest'] == archived['manifest'],
                'Published receipt missing from run index')
        if current != archived:
            store.commit({receipt_name: encode(archived)}, 'Restore GPT receipt after successful archive recheck')
        return archived

    bodies = parse_submission(raw)
    row = index.by_hash.get(content_hash)
    if row is not None:
        manifest = check_archived(store, row['manifest'])
        receipt = make_receipt(manifest, row['manifest'], content_hash)
        store.commit({receipt_name: encode(receipt)}, 'Record identical GPT submission receipt')
        return receipt

    if source is None:
        source = store.source(path)
    submitted = utc(source['submitted_at_utc'])
    require(submitted <= datetime.now(timezone.utc) + timedelta(minutes=5), 'Submission timestamp is in the future')
    run_id = submitted.astimezone(BJT).strftime('%Y%m%dT%H%M%S+0800_') + content_hash[:32]
    base = 'reports/' + submitted.astimezone(BJT).strftime('%Y/%m/%d/') + run_id
    manifest = {'archive_format': FORMAT, 'run_id': run_id, 'archive_mode': 'production',
                'submitted_at_utc': source['submitted_at_utc'], 'source': source,
                'submission_sha256': content_hash, 'archive_status': 'prepared',
                'research_provenance': {'information_cutoff_utc': None, 'registry_commit': None,
                    'data_versions': None, 'note': 'Research dates and citations remain in the original Markdown; not inferred from upload time.'},
                'research_quality': 'not_certified_by_archive_tool', 'reports': {}}
    files = {}
    for domain, markdown in bodies.items():
        content = {'schema_version': 'radar_text_report_v1', 'domain': domain, 'run_id': run_id,
                   'submitted_at_utc': source['submitted_at_utc'], 'markdown': markdown,
                   'research_provenance': manifest['research_provenance']}
        files[domain + '.md'] = markdown.encode('utf-8')
        files[domain + '.json'] = encode(content)
        manifest['reports'][domain] = {kind: {'path': base + '/' + domain + '.' + ext,
            'sha256': digest(files[domain + '.' + ext])} for kind, ext in (('markdown', 'md'), ('json', 'json'))}
    stage = {base + '/' + name: data for name, data in files.items()}
    manifest_path = base + '/run_manifest.json'
    stage[manifest_path] = encode(manifest)
    for name, data in stage.items():
        existing = store.read(name)
        require(existing is None or existing == data, 'Immutable archive conflict: ' + name)
    store.commit(stage, 'Store GPT report bytes for archive readback')
    manifest.update(archive_status='verified', archived_at_utc=iso(datetime.now(timezone.utc)))
    manifest_raw = encode(manifest)
    manifest_ref = {'path': manifest_path, 'sha256': digest(manifest_raw)}
    entry = {key: manifest[key] for key in ('run_id', 'submitted_at_utc', 'archived_at_utc', 'submission_sha256')}
    entry.update(manifest=manifest_ref, batch_status='complete', archive_format=FORMAT)
    require(run_id not in index.by_id, 'Conflicting run_id')
    rows = index.document['runs']
    next_index = {**index.document, 'schema_version': 'radar_runs_v2', 'runs': [*rows, entry]}
    latest = read_json(store, 'latest/run.json')
    if latest:
        latest_row = index.by_id.get(latest['run_id'])
        require(latest_row is not None and latest_row['manifest'] == latest['manifest'],
                'Latest and index disagree; preserve them for repair')
    promote = all(order(entry) >= order(row) for row in rows)
    if latest:
        promote = promote and order(entry) >= order(latest)
    receipt = make_receipt(manifest, manifest_ref, content_hash)
    receipt['latest_promoted'] = promote
    changes = {manifest_path: manifest_raw, 'manifests/runs.json': encode(next_index), receipt_name: encode(receipt)}
    if promote:
        pointer = {'schema_version': 'radar_latest_v2', 'archive_mode': 'production',
                   'run_id': run_id, 'submitted_at_utc': source['submitted_at_utc'], 'manifest': manifest_ref,
                   'reports': {d: {kind: {**ref, 'path': 'latest/' + PurePosixPath(ref['path']).name}
                                  for kind, ref in refs.items()} for d, refs in manifest['reports'].items()}}
        changes.update({'latest/' + name: data for name, data in files.items()})
        changes['latest/run.json'] = encode(pointer)
    store.commit(changes, 'Publish verified GPT batch and preserve archive history')
    index.document = next_index
    index.remember(entry)
    return receipt


def record_failure(store, path, error):
    failure = {'status': 'failed', 'submission': path, 'error': str(error)}
    try:
        name = receipt_path(path)
        previous, archived = receipt_history(store, name)
    except GitError:
        raise
    except (ValueError, KeyError):
        # No valid receipt path or readable prior state. Keep the original bytes for repair.
        return failure
    record = {**failure, 'archived_receipt': archived}
    if previous != record:
        store.commit({name: encode(record)}, 'Record GPT submission failure and retain its archive reference')
    return failure


def process_inbox(store):
    names = store.git('ls-files', '-z', '--', 'inbox/gpt/*.md').decode('utf-8', errors='backslashreplace')
    errors, receipts, sources = [], [], []
    # Scan all pending files so a superseded queued workflow cannot lose a submission.
    for path in names.split('\0')[:-1]:
        try:
            receipt_path(path)
            sources.append(store.source(path))
        except GitError:
            raise
        except (ValueError, KeyError) as exc:
            errors.append(record_failure(store, path, exc))
    if sources:
        index = RunIndex(store)
        for source in sorted(sources, key=lambda s: (s['submitted_at_utc'], s['path'])):
            path = source['path']
            try:
                receipts.append(publish(store, path, index=index, source=source))
            except GitError:
                raise
            except (ValueError, KeyError) as exc:
                errors.append(record_failure(store, path, exc))
    return {'receipts': receipts, 'errors': errors}


def smoke_test():
    """Exercise actual Git writes/readback against a disposable local bare remote."""
    with tempfile.TemporaryDirectory(prefix='radar-archive-test-') as directory:
        root = Path(directory).resolve()
        require(root.is_relative_to(Path(tempfile.gettempdir()).resolve()), 'Unexpected temporary test path')
        remote, seed = root / 'remote.git', root / 'seed'
        def git(*args):
            subprocess.run(['git', *map(str, args)], check=True, capture_output=True)
        git('init', '--bare', remote)
        git('init', '-b', 'main', seed)
        git('-C', seed, 'config', 'user.name', 'Archive synthetic test')
        git('-C', seed, 'config', 'user.email', 'test@example.invalid')
        source = seed / 'inbox/gpt/synthetic.md'
        source.parent.mkdir(parents=True)
        source.write_bytes(''.join('<!-- radar:' + d + ' -->\n# Synthetic ' + d + '\nOffline test only.\n'
                                  for d in DOMAINS).encode())
        git('-C', seed, 'add', '--', 'inbox/gpt/synthetic.md')
        git('-C', seed, 'commit', '-m', 'Synthetic inbox only')
        git('-C', seed, 'remote', 'add', 'origin', remote)
        git('-C', seed, 'push', 'origin', 'main')
        store = GitStore(root / 'publisher', str(remote))
        first = process_inbox(store)
        require(not first['errors'], 'Synthetic publication failed')
        again = GitStore(root / 'retry', str(remote))
        second = process_inbox(again)
        require(first == second, 'Retry changed the receipt')
        require(len(read_json(again, 'manifests/runs.json')['runs']) == 1, 'Retry duplicated batch')
        pointer = read_json(again, 'latest/run.json')
        require(set(pointer['reports']) == set(DOMAINS), 'Missing latest report')
        for refs in pointer['reports'].values():
            for ref in refs.values():
                require(digest(again.read(ref['path'])) == ref['sha256'], 'Latest readback mismatch')
    return {'test': 'passed', 'scope': 'disposable_local_git_remote', 'production_reports_written': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', type=Path, help='Parse a submission locally, without publishing')
    parser.add_argument('--publish-inbox', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps(smoke_test()))
        return 0
    if args.check:
        reports = parse_submission(args.check.read_bytes())
        print(json.dumps({'valid': True, 'characters': {d: len(t) for d, t in reports.items()}}, ensure_ascii=False))
        return 0
    require(args.publish_inbox, 'Choose --check FILE or --publish-inbox')
    for attempt in range(3):
        try:
            with tempfile.TemporaryDirectory(prefix='radar-publish-') as directory:
                require(Path(directory).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve()),
                        'Unexpected temporary publisher path')
                result = process_inbox(GitStore(directory))
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 1 if result['errors'] else 0
        except GitError as exc:
            message = f'Attempt {attempt + 1}/3: {exc}'
            if not exc.retryable or attempt == 2:
                raise GitError(message, retryable=exc.retryable) from None
            print(message + '. Retrying from a fresh checkout.', file=sys.stderr)


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as exc:
        raise SystemExit('Archive failed: ' + str(exc))

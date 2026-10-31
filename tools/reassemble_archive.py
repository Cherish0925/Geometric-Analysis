#!/usr/bin/env python3
"""Restore an original archive from checksummed transport parts."""
import hashlib
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
manifest = json.loads((root / sys.argv[1]).read_text())
def local(path):
    result = (root / path).resolve()
    result.relative_to(root)
    return result
data = bytearray()
for part in manifest['parts']:
    content = local(part['path']).read_bytes()
    assert len(content) == part['size'], part['path']
    assert hashlib.sha256(content).hexdigest() == part['sha256'], part['path']
    data.extend(content)
assert len(data) == manifest['size']
assert hashlib.sha256(data).hexdigest() == manifest['sha256']
destination = local(manifest['destination'])
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_bytes(data)
receipt = {
    'path': manifest['destination'], 'size': len(data),
    'sha256': hashlib.sha256(data).hexdigest(),
    'git_blob_sha': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(),
}
(root / 'catalog/large_archive_restoration.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt))

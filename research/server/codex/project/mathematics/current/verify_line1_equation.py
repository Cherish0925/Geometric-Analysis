"""Run this turn's finite checks and preserve exact local evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--output', required=True, type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parent
out = args.output.resolve()
out.mkdir(parents=True, exist_ok=False)
names = [
    'two_chirality_topology',
    'signed_harmonic_weyl',
    'half_weyl_regularity',
    'einstein_spectral_application',
]
results = []
for name in names:
    script = root / f'check_line1_{name}.py'
    result = subprocess.run([sys.executable, str(script)], cwd=root,
                            text=True, capture_output=True, timeout=120)
    log = result.stdout + result.stderr
    (out / f'{name}.log').write_text(log)
    results.append({'check': script.name, 'returncode': result.returncode,
                    'sha256': hashlib.sha256(script.read_bytes()).hexdigest()})
    print(f'{script.name}: exit {result.returncode}')
manifest = {}
for name in names:
    for ext in ('md', 'tex', 'pdf'):
        path = root / f'line1_{name}.{ext}'
        if path.exists():
            manifest[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
report = {'scope': 'Finite algebra and artifact identity; not PDE or priority certification.',
          'checks': results, 'artifacts': manifest}
(out / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
raise SystemExit(any(r['returncode'] for r in results))

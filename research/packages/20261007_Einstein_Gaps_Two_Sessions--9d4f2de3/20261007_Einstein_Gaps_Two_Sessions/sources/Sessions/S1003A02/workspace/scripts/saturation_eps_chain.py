"""Continuation in the collapse parameter for the exact-CH-terminal saturation problem.

The exact-CH terminal of saturation_optimal_control.py is a legitimate cell
competitor: after the terminal orbit the metric is continued by the exact
(homothetic) complex-hyperbolic collar, and since the action only charges the
trace-free Ricci tensor, the whole cell can be rescaled so that the collar has
Ric=-6.  By Theorem T the exact-collar infimum equals the standard-CR stable-set
infimum, so no nonlinear stable manifold is needed for this formulation.

Usage: python saturation_eps_chain.py N TAG eps1 eps2 ...
 (environment SAT_A0, SAT_T0CH, SAT_TAU0 set the cold-start guess of the first eps)
Writes data/saturation_control/chain_N<N><TAG>.json with (eps, cost, A, t_ch, T, status).
"""
import json, os, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import saturation_optimal_control as soc  # noqa: E402

N = int(sys.argv[1]); TAG = sys.argv[2]; epss = [float(e) for e in sys.argv[3:]]
os.environ['SAT_TAG'] = TAG
rows = []; warm = None
for eps in epss:
    rc = soc.solve(eps, N, warm, 'ch')
    tag = (f"eps{eps:.6g}_N{N}_ch").replace('.', 'p') + TAG
    path = soc.OUT / f'{tag}.json'
    rec = json.loads(path.read_text())
    rows.append({k: rec[k] for k in ('eps', 'N', 'success', 'return_status', 'cost', 'A', 't_ch', 'T',
                                     'max_collocation_residual', 'bplus_initial', 'max_bplus')})
    if rec['success']:
        warm = str(path)
    (soc.OUT / f'chain_N{N}{TAG}.json').write_text(json.dumps(rows, indent=1))
print(json.dumps(rows, indent=1))

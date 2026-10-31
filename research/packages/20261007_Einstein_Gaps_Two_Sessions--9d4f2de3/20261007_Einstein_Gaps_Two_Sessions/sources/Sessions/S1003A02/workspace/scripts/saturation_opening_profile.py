"""Opening-radius profile of the exact-CH saturation problem.

For fixed collapse parameter eps, minimize the full-control action with the CH
opening radius constrained to a window [tau0, tau0+0.25], warm-starting each window
from the previous one.  This maps the cost of *late* opening, the configuration not
priced by the chiral charge bound 4-9 sinh^4 tau.
Usage: python saturation_opening_profile.py EPS N warm.json tau0_1 tau0_2 ...
Writes data/saturation_control/opening_profile_eps<EPS>_N<N>.json
"""
import json, os, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import saturation_optimal_control as soc  # noqa: E402

eps = float(sys.argv[1]); N = int(sys.argv[2]); warm = sys.argv[3]
taus = [float(v) for v in sys.argv[4:]]
rows = []
for t0 in taus:
    os.environ['SAT_TCH_LO'] = str(t0); os.environ['SAT_TCH_HI'] = str(t0+0.25)
    TAG = f'_open{t0:g}'.replace('.', 'p'); os.environ['SAT_TAG'] = TAG
    soc.solve(eps, N, warm, 'ch')
    path = soc.OUT / ((f"eps{eps:.6g}_N{N}_ch").replace('.', 'p')+TAG+'.json')
    rec = json.loads(path.read_text())
    rows.append({k: rec[k] for k in ('eps', 'N', 'success', 'return_status', 'cost', 'A', 't_ch', 'T',
                                     'max_collocation_residual', 'bplus_initial', 'max_bplus', 'bplus_terminal')})
    rows[-1]['tau_window'] = [t0, t0+0.25]
    if rec['success']:
        warm = str(path)
    out = soc.OUT / (f'opening_profile_eps{eps:g}_N{N}.json').replace('0.', '0p')
    out.write_text(json.dumps(rows, indent=1))
print(json.dumps(rows, indent=1))

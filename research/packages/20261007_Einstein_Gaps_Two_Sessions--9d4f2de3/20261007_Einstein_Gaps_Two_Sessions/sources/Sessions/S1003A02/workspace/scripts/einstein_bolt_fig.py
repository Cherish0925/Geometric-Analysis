"""Figure: SU(2)-invariant Einstein metrics (Ric=-6g) on the O(-1) bolt (blown-up ball).
Reads data/einstein_bolt_runs/{bis_*,bisR_*}_n1.json, biax_n1.json; recomputes two trajectories.
Writes figures/einstein_bolt_ach_family.png and data/einstein_bolt_runs/ach_family_summary.csv.
"""
import json, glob, math
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import einstein_bolt_shoot as E

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent / 'data' / 'einstein_bolt_runs'
FIG = HERE.parent / 'figures'

recs = []
for f in glob.glob(str(RUNS / 'bis*_n1.json')):
    recs += [r for r in json.loads(Path(f).read_text()) if r.get('found') and r.get('min_dev', 1) < 0.03]
recs.sort(key=lambda r: r['b'])
with open(RUNS / 'ach_family_summary.csv', 'w') as fh:
    fh.write('b,d_star,rho_at_min,rho_plateau_lo,rho_plateau_hi,kappa1_at_min,min_dev,plateau_len\n')
    for r in recs:
        lo, hi = r.get('rossi_plateau_range', [r['rossi_a2_over_a3_at_min']]*2)
        fh.write(f"{r['b']},{r['d_lo']},{r['rossi_a2_over_a3_at_min']},{lo},{hi},{r['kappa1_at_min']},{r['min_dev']},{r['plateau_len']}\n")
b = np.array([r['b'] for r in recs]); rho = np.array([r['rossi_a2_over_a3_at_min'] for r in recs])
lo = np.array([r.get('rossi_plateau_range', [np.nan, np.nan])[0] for r in recs])
hi = np.array([r.get('rossi_plateau_range', [np.nan, np.nan])[1] for r in recs])
dst = np.array([r['d_lo'] for r in recs])
bx = json.loads((RUNS / 'biax_n1.json').read_text())

fig, ax = plt.subplots(2, 2, figsize=(11, 8.5))
a = ax[0, 0]
a.fill_between(b, lo, hi, color='C0', alpha=.25, label='plateau range')
a.plot(b, rho, 'o-', color='C0', label=r'$\rho=a_2/a_3$ at closest ACH approach')
a.axhline(1, color='k', ls='--', lw=1, label=r'standard CR sphere $\rho=1$ (exact CH end)')
a.set_xscale('log'); a.set_xlabel(r'bolt radius $b=a_1(0)=a_2(0)$'); a.set_ylabel(r'Rossi ratio $\rho$ of CR infinity')
a.set_title('Perpendicular ACH Einstein fillings of the blown-up ball'); a.legend(fontsize=8); a.set_ylim(0, 12)
a = ax[0, 1]
a.loglog(b, dst, 's-', color='C1'); a.set_xlabel('b'); a.set_ylabel(r'separatrix anisotropy $d^*(b)$, $a_1-a_2=d\,t^4+\dots$')
a.set_title('AH / singular separatrix in the bolt family')
a = ax[1, 0]
bolt = E.Bolt(1)
for bb, col in [(0.8, 'C0'), (4.0, 'C3')]:
    r = [x for x in recs if abs(x['b']-bb) < 1e-12][0]
    o = E.shoot(bolt, bb, r['d_lo'], T=10, dense=True); s = o['_sol']
    tt = np.linspace(s.t[0], s.t[-1], 2000); Z = s.sol(tt)
    for i, ls in zip(range(3), ['-', '--', ':']):
        a.plot(tt, Z[3+i], ls, color=col, label=f'b={bb}: $y_{i+1}$')
a.axhline(2, color='gray', lw=.5); a.axhline(1, color='gray', lw=.5); a.axhline(math.sqrt(2), color='gray', lw=.5, ls='-.')
a.set_ylim(0, 3); a.set_xlabel('t'); a.set_ylabel(r"$y_i=a_i'/a_i$"); a.legend(fontsize=7, ncol=2)
a.set_title(r'near-separatrix: plateau at ACH $(2,1,1)$, exit to AH $\sqrt{2}$')
a = ax[1, 1]
a.semilogx([r['b'] for r in bx], [r['squash_end'] for r in bx], 'o-', color='C2', label=r'U(2) bolts: AH squashing $c_3/c_1$')
a.axhline(1, color='k', ls='--', lw=1, label='round $S^3$')
a.set_xlabel('b'); a.set_ylabel('Berger squashing at infinity'); a.legend(fontsize=8)
a.set_title('Aligned (biaxial) O(-1) bolts: all AH, never ACH')
fig.tight_layout(); FIG.mkdir(exist_ok=True)
fig.savefig(FIG / 'einstein_bolt_ach_family.png', dpi=160)
print('rho min', rho.min(), 'at b', b[np.argmin(rho)], 'n', len(recs))

"""Boundary jet of the Einstein defect E = Ric + 6g of the frozen perpendicular cell
at its outer collar x = X (S1003A01, Step 13).

The frozen profile has second-jet contact with CH at x = X, so E vanishes there and
E_aa(u) = -E_aa'(1) (1-u) + O((1-u)^2) inside.  In geodesic distance r (dt = dx/(2 sqrt G))
we write E_aa ~ (rho - r) e_a, e_a = -dE_aa/dr at r = rho^-.
Frame slots: 0 = radial, 1 = bolt slot (contact plane), 2 = contact plane, 3 = CH fibre J nu.

Near-tangent pair interaction (see notes/step13_pair_overlap_interaction.md):
    sign I(w) = sign <e, R_theta e>,  <e,R_theta e> = e0^2+e3^2+2 m^2+2 d^2 cos(2 theta'),
with m=(e1+e2)/2, d=(e1-e2)/2; minimum e0^2+e3^2+2 e1 e2.

Usage: python pair_boundary_jet.py RECORD.json [--out OUT.json]
"""
import argparse, json, sys
from pathlib import Path
from flint import arb, acb, ctx

sys.path.insert(0, str(Path(__file__).resolve().parent))
from perp_rigorous_enclosure import FrozenCell


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--out')
    ap.add_argument('--prec', type=int, default=256)
    a = ap.parse_args(); ctx.prec = a.prec
    rec = json.loads(Path(a.record).read_text())
    cell = FrozenCell(rec)
    X = cell.X; ell = cell.ell
    G_CH = X + X*X
    drdu = ell*X/(2*G_CH.sqrt())          # dr/du at the collar for the CH value of G
    vals = {}
    for eps in ['0', '1e-8', '2e-8', '1e-4', '1e-3', '1e-2', '5e-2']:
        R, vol, prof = cell.ricci(acb(1 - arb(eps)), want_profile=True)
        vals[eps] = [(r + 6).real for r in R]
    # one-sided derivative by Richardson on 1e-8, 2e-8 (E(1)=0 exactly up to Arb radius)
    e = []
    for k in range(4):
        d1 = vals['1e-8'][k]/arb('1e-8'); d2 = vals['2e-8'][k]/arb('2e-8')
        slope = 2*d1 - d2                 # = E/(1-u) extrapolated to u -> 1
        e.append(slope/drdu)              # e_a = dE/d(rho-r)
    e = [float(v.mid()) for v in e]
    e0, e1, e2, e3 = e
    m, d = (e1+e2)/2, (e1-e2)/2
    out = dict(record=a.record, X=float(X.mid()), rho_geodesic=float((X.sqrt()).asinh().mid()),
               E_at_collar=[float(v.mid()) for v in vals['0']],
               E_samples={k: [float(v.mid()) for v in vv] for k, vv in vals.items()},
               e_jet=e, aligned_pairing=e0**2+e1**2+e2**2+e3**2,
               min_pairing=e0**2+e3**2+2*e1*e2,
               invariant_part=e0**2+e3**2+2*m*m, weight_two=2*d*d,
               trace_e=sum(e), negative_possible=bool(e0**2+e3**2+2*e1*e2 < 0))
    text = json.dumps(out, indent=1); print(text)
    if a.out: Path(a.out).write_text(text+'\n')


if __name__ == '__main__':
    main()

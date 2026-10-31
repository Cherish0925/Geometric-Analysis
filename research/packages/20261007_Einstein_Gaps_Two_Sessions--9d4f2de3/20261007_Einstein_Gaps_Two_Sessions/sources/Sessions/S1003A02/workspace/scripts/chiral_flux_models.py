"""Model checks of the chiral fluxes bX = bE -/+ (S-6) (X=A: W+ of the CH Kaehler orientation).

Uses the exact S from data/chiral_flux.json (produced by chiral_flux_identity.py).
Burns (scalar-flat Kaehler ALE on O(-1)):  a1=a2=r, a3=r sqrt(f), f=1-m/r^2, dt=dr/sqrt(f).
Taub-bolt (Ricci-flat ALF on O(-1)/CP^2-pt): a1=a2=2 sqrt(r^2-n^2), a3=4n sqrt(V),
   V=(r^2-5nr/2+n^2)/(r^2-n^2), dt=dr/sqrt(V), bolt r=2n.
For each model: block norms B_A, B_B, scalar s; charges bA,bB at the bolt and at infinity;
and direct quadratures of int W B_X dt compared with the flux differences.
Output: data/chiral_flux_models.json
"""
import json, sys
from pathlib import Path
import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / 'S1003A01' / 'workspace' / 'scripts'))
import perp_cartan_verify as pc  # noqa: E402
from chiral_flux_identity import BA, BB, bE, S_sol  # noqa: E402  (re-derives; slow but exact)

a, b, c, a1, b1, c1, a2, b2, c2 = pc.a, pc.b, pc.c, pc.a1, pc.b1, pc.c1, pc.a2, pc.b2, pc.c2
Sn = S_sol - 6
bA = bE - Sn; bB = bE + Sn
r = sp.Symbol('r', positive=True)

def radial(metric, lapse):
    """metric: list of a_i(r); lapse N(r) with dt = N dr. Return substitution for jets in t."""
    sub = {}
    for X, X1, X2, f in zip([a, b, c], [a1, b1, c1], [a2, b2, c2], metric):
        d1 = sp.diff(f, r)/lapse
        d2 = sp.diff(d1, r)/lapse
        sub[X] = f; sub[X1] = d1; sub[X2] = d2
    return sub

out = {}
m, n = sp.Integer(1), sp.Integer(1)
fB = 1 - m/r**2
models = {
    'Burns': ([r, r, r*sp.sqrt(fB)], 1/sp.sqrt(fB), sp.sqrt(m), mp.inf),
}
V = (r**2 - sp.Rational(5, 2)*n*r + n**2)/(r**2 - n**2)
models['TaubBolt'] = ([2*sp.sqrt(r**2 - n**2), 2*sp.sqrt(r**2 - n**2), 4*n*sp.sqrt(V)], 1/sp.sqrt(V), 2*n, mp.inf)
for name, (met, N, r0, r1) in models.items():
    sub = radial(met, N)
    ex = {k: sp.simplify(v.subs(sub)) for k, v in
          dict(BA=BA, BB=BB, s=pc.s, ric0=pc.ric0sq, bA=bA, bB=bB, bE=bE).items()}
    Wr = sp.simplify((met[0]*met[1]*met[2]*N))   # W dt = W N dr
    rec = {k: str(ex[k]) for k in ('BA', 'BB', 's', 'ric0')}
    for k in ('bA', 'bB', 'bE'):
        rec[k+'_bolt'] = str(sp.limit(ex[k], r, r0, '+'))
        rec[k+'_inf'] = str(sp.limit(ex[k], r, sp.oo))
    fA = sp.lambdify(r, Wr*ex['BA'], 'mpmath'); fBB = sp.lambdify(r, Wr*ex['BB'], 'mpmath')
    mp.mp.dps = 30
    r0f = mp.mpf(sp.N(r0, 40))
    rec['int_W_BA'] = str(mp.quad(fA, [r0f, r0f+1, r0f+10, mp.inf]))
    rec['int_W_BB'] = str(mp.quad(fBB, [r0f, r0f+1, r0f+10, mp.inf]))
    out[name] = rec
    print(name, json.dumps(rec, indent=1))
(HERE.parent / 'data' / 'chiral_flux_models.json').write_text(json.dumps(out, indent=1))

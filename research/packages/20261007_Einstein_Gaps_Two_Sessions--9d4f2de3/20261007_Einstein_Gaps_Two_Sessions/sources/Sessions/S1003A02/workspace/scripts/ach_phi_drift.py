"""Arb bound for the drift of the corrected neutral variable Phi~ = q + a/4 - zeta sinh q inside the
verified cusp block B(K, zeta0, Q).  Phi~' is exactly quadratic: Phi~' = zeta^2 G(ub,s1b,s2b,ab,E=e^q,zeta),
G polynomial.  With zeta' <= -c zeta (c = verified ygh lower bound) a solution staying in B after time T
has |q_inf - Phi~(T)| <= sup|G| zeta(T)^2/(2c), since Phi~ -> q_inf on the equilibrium curve.
CLI: python ach_phi_drift.py K zeta0 qlo qhi [nsub]  -> data/ach_block/phidrift_*.json
"""
import json, sys, itertools
from pathlib import Path
import sympy as sp
from flint import arb

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ach_block_verify import toE, lamb, box  # noqa: E402

OUT = HERE.parent / 'data' / 'ach_block'


def build_G():
    ub, s1b, s2b, ab, q, z = sp.symbols('ub s1b s2b ab q z')
    u, s1, s2, ah = z*ub, z*s1b, z*s2b, z*ab
    ch, sh = sp.cosh(q), sp.sinh(q)
    rhs = sp.Matrix([u + 2*ch*z, s1 - 2*ch*z, s2 + 4*ch*z])
    A = sp.Matrix([[1, -1, 6], [1, -1, -2], [2, 3, 2]])
    dyf, ds, dk = [sp.expand(x) for x in A.LUsolve(rhs)]
    a = ah - 4*sh*z
    yf, yg, yh, k = 2 + dyf, 1 + (ds + a)/2, 1 + (ds - a)/2, 1 + dk
    S = yf + yg + yh
    Pg = -2*k**2 + 4*z*sp.exp(-q) + 4*z**2*sp.sinh(2*q)/k**2
    Ph = -2*k**2 + 4*z*sp.exp(q) - 4*z**2*sp.sinh(2*q)/k**2
    da_t = -(yg - yh)*S + Pg - Ph
    dq_t = yg - yh
    dz_t = -z*(yg + yh)
    dphi = dq_t + da_t/4 - dz_t*sh - z*ch*dq_t
    G = toE(sp.expand(dphi), q)
    E = sp.Symbol('E', positive=True)
    # divide by z^2: G is a sum of monomials; check every term has z-degree >= 2 after cancellation
    num, den = sp.fraction(sp.together(G))
    num = sp.expand(num)
    P = sp.Poly(num, z)
    low = [P.coeff_monomial(z**j) for j in range(2)]
    low = [sp.simplify(c) for c in low]
    assert all(c == 0 for c in low), low
    G2 = sp.expand(sp.cancel(num/z**2))/den
    return G2, (ub, s1b, s2b, ab, E, z)


if __name__ == '__main__':
    Kv, z0, qlo, qhi = [float(v) for v in sys.argv[1:5]]
    nsub = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    G, syms = build_G()
    f = lamb(G, syms + (sp.Symbol('K'),))
    grid = [(-Kv + 2*Kv*i/nsub, -Kv + 2*Kv*(i+1)/nsub) for i in range(nsub)]
    nq, nz = 8, 4
    qg = [(qlo + (qhi-qlo)*i/nq, qlo + (qhi-qlo)*(i+1)/nq) for i in range(nq)]
    zg = [(z0*i/nz, z0*(i+1)/nz) for i in range(nz)]
    worst = 0.0
    for cells in itertools.product(grid, grid, grid, grid, qg, zg):
        v = f(*[box(*c) for c in cells[:4]], box(*cells[4]).exp(), box(*cells[5]), arb(Kv))
        worst = max(worst, float(abs(arb(v)).upper()))
    res = dict(K=Kv, zeta0=z0, q=[qlo, qhi], nsub=nsub, sup_abs_G=worst*(1 + 1e-12), G=str(G))
    print(json.dumps({k: v for k, v in res.items() if k != 'G'}, indent=1))
    (OUT / f'phidrift_K{Kv:g}_z{z0:g}_q{qlo:g}_{qhi:g}.json').write_text(json.dumps(res, indent=1))

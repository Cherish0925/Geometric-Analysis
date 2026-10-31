"""Rigorous (Arb) verification of a cusp-shaped isolating block around the ACH equilibrium curve
of the diagonal Bianchi-IX Einstein flow (Ric = -6g), fibre slot f, in compact variables
    W = (y_f, y_g, y_h, kappa, q, zeta)     (see ach_projected.py).

Eigen-coordinates (spectrum 2, -6, -8 on (dy_f, ds, dkappa), -4 on a = y_g - y_h, 0 on q, -2 on zeta),
with the linear zeta-forcing removed:
    u   = dy_f - ds + 6 dk - 2 cosh(q) zeta          (unstable, rate +2)
    s1  = dy_f - ds - 2 dk + 2 cosh(q) zeta          (rate -6)
    s2  = 2dy_f + 3ds + 2dk - 4 cosh(q) zeta         (rate -8, = linearized constraint)
    ah  = a + 4 sinh(q) zeta                         (rate -4)
with dy_f = y_f - 2, ds = y_g + y_h - 2, dk = kappa - 1.
Block  B(K, zeta0, Q) = { |u|,|s1|,|s2|,|ah| <= K zeta,  0 < zeta <= zeta0,  q in Q }.
Rescale u = zeta*ub etc.  For each face we verify, over the whole face, with Arb boxes:
    egress  on ub = +-K :  +-(u' - (+-K) zeta')/zeta > 0
    ingress on s1,s2,ah = +-K :  +-(x' - (+-K) zeta')/zeta < 0
    zeta' < 0 (zeta = zeta0 face is ingress, zeta never reaches 0 in finite time).
The q-faces are not isolating; a staying solution has |q'| = |a| <= (K + 4 sinh q) zeta, zeta' <= -(2-c)zeta,
so the total q-drift after entry at zeta0 is <= (K + 4 sinh q_max) zeta0/(2-c) (checked and reported).

CLI: python ach_block_verify.py K zeta0 qlo qhi [nsub]  -> data/ach_projected/block_K*_z*_q*.json
"""
import json, sys, itertools, math, time
from pathlib import Path
import sympy as sp
from flint import arb

OUT = Path(__file__).resolve().parents[1] / 'data' / 'ach_block'
OUT.mkdir(parents=True, exist_ok=True)


def build():
    ub, s1b, s2b, ab, q, z = sp.symbols('ub s1b s2b ab q z')
    u, s1, s2, ah = z*ub, z*s1b, z*s2b, z*ab
    ch, sh = sp.cosh(q), sp.sinh(q)
    rhs = sp.Matrix([u + 2*ch*z, s1 - 2*ch*z, s2 + 4*ch*z])
    A = sp.Matrix([[1, -1, 6], [1, -1, -2], [2, 3, 2]])
    v = A.LUsolve(rhs)
    dyf, ds, dk = [sp.expand(x) for x in v]
    a = ah - 4*sh*z
    yf, yg, yh, k = 2 + dyf, 1 + (ds + a)/2, 1 + (ds - a)/2, 1 + dk
    S = yf + yg + yh
    Pf = 2*k**2 - 8*z**2*sh**2/k**2
    Pg = -2*k**2 + 4*z*sp.exp(-q) + 4*z**2*sp.sinh(2*q)/k**2
    Ph = -2*k**2 + 4*z*sp.exp(q) - 4*z**2*sp.sinh(2*q)/k**2
    dyf_t = 6 - yf*S + Pf
    dyg_t = 6 - yg*S + Pg
    dyh_t = 6 - yh*S + Ph
    dk_t = k*(yf - yg - yh)
    dq_t = yg - yh
    dz_t = -z*(yg + yh)
    ds_t = dyg_t + dyh_t
    da_t = dyg_t - dyh_t
    du_t = dyf_t - ds_t + 6*dk_t - 2*sh*dq_t*z - 2*ch*dz_t
    ds1_t = dyf_t - ds_t - 2*dk_t + 2*sh*dq_t*z + 2*ch*dz_t
    ds2_t = 2*dyf_t + 3*ds_t + 2*dk_t - 4*sh*dq_t*z - 4*ch*dz_t
    dah_t = da_t + 4*ch*dq_t*z + 4*sh*dz_t
    K = sp.Symbol('K')
    faces = {}
    ygh = yg + yh
    # g = x - c K z, g' = x' - c K z' ; divide by z (exact cancellation checked below)
    for name, xt, lam in [('u', du_t, 2), ('s1', ds1_t, -6), ('s2', ds2_t, -8), ('ah', dah_t, -4)]:
        for c in (+1, -1):
            if name == 'u':
                # ub' = u'/z + ub*ygh ; verified  c*ub' > 0  on the whole slab c*ub in [K/2, K]
                G = sp.expand(c*(sp.expand(xt)/z + ub*ygh))
                G = toE(G, q)
                faces[(name, c)] = G
                continue
            sub = {'u': {ub: c*K}, 's1': {s1b: c*K}, 's2': {s2b: c*K}, 'ah': {ab: c*K}}[name]
            g = (xt - c*K*dz_t).subs(sub)
            G = sp.expand(sp.expand(c*g)/z)
            G = toE(G, q)
            assert not any(sp.Pow(z, -1) in t.atoms(sp.Pow) for t in sp.Add.make_args(G)), name
            faces[(name, c)] = G
    zfac = toE(ygh, q)   # zeta' = -zeta*ygh, need ygh > 0
    syms = (ub, s1b, s2b, ab, sp.Symbol('E', positive=True), z, K)
    return faces, zfac, syms, sp.expand(dq_t)


def toE(G, q):
    """Rewrite hyperbolic functions of q through E = e^q so exact cancellations happen symbolically
    (interval arithmetic cannot cancel e.g. 12 e^q - 12 e^q)."""
    E = sp.Symbol('E', positive=True)
    G = G.rewrite(sp.exp)
    G = G.subs(sp.exp(q), E)
    G = sp.expand(sp.powsimp(G))
    G = sp.expand(sp.together(G)) if False else G
    assert q not in G.free_symbols, G.free_symbols
    return G


def lamb(expr, syms):
    mod = {'mpf': lambda v: arb(v), 'cosh': lambda x: x.cosh(), 'sinh': lambda x: x.sinh(),
           'exp': lambda x: x.exp()}
    return sp.lambdify(syms, expr, modules=[mod, 'mpmath'])


def iv(lo, hi):
    lo, hi = arb(lo), arb(hi)
    return (lo + hi)/2 + arb(0, 1)*((hi - lo)/2) if False else arb.union(lo, hi) if hasattr(arb, 'union') else None


def box(lo, hi):
    m = 0.5*(lo + hi)
    r = max(hi - m, m - lo)*(1 + 1e-12) + 1e-300
    return arb(m, r)


def verify(Kv, z0, qlo, qhi, nsub=4, nq=8, nz=4):
    faces, zfac, syms, dq = build()
    F = {key: lamb(G, syms) for key, G in faces.items()}
    Z = lamb(zfac, syms)
    rescaled = ['u', 's1', 's2', 'ah']
    grid = [(-Kv + 2*Kv*i/nsub, -Kv + 2*Kv*(i+1)/nsub) for i in range(nsub)]
    qg = [(qlo + (qhi-qlo)*i/nq, qlo + (qhi-qlo)*(i+1)/nq) for i in range(nq)]
    zg = [(z0*i/nz, z0*(i+1)/nz) for i in range(nz)]
    res = {}
    t0 = time.time()
    for (name, c), f in F.items():
        free = [r for r in rescaled if r != name]
        worst = None
        slab = [(c*Kv/2 + (c*Kv/2)*i/nsub, c*Kv/2 + (c*Kv/2)*(i+1)/nsub) for i in range(nsub)]
        slab = [(min(p), max(p)) for p in slab]
        for cells in itertools.product(grid, grid, grid, qg, zg, slab if name == 'u' else [None]):
            vals = dict(zip(free, [box(*cells[0]), box(*cells[1]), box(*cells[2])]))
            vals[name] = box(*cells[5]) if name == 'u' else arb(c*Kv)
            args = [vals['u'], vals['s1'], vals['s2'], vals['ah'], box(*cells[3]).exp(), box(*cells[4]), arb(Kv)]
            G = f(*args)
            # egress (u): need G > 0 ; ingress: need G < 0
            m = G.lower() if name == 'u' else -G.upper()
            m = float(m.lower()) if hasattr(m, 'lower') else float(m)
            if worst is None or m < worst:
                worst = m
        res[f'{name}{"+" if c > 0 else "-"}'] = dict(margin_lower_bound=worst, ok=bool(worst > 1e-12))
        print(name, c, 'worst margin', worst, flush=True)
    # zeta factor positivity over the full block
    worstz = None
    for cells in itertools.product(grid, grid, grid, grid, qg, zg):
        G = Z(*[box(*cl) for cl in cells[:4]], box(*cells[4]).exp(), box(*cells[5]), arb(Kv))
        gl = float(G.lower())
        worstz = gl if worstz is None or gl < worstz else worstz
    res['zeta_decay_factor_ygh_min'] = worstz
    res['zeta_ok'] = bool(worstz > 1e-12)
    drift = (Kv + 4*math.sinh(max(abs(qlo), abs(qhi))))*z0/(worstz if worstz > 0 else 1)
    res['q_drift_bound'] = drift
    res['all_ok'] = all(v['ok'] for k, v in res.items() if isinstance(v, dict)) and res['zeta_ok']
    res.update(K=Kv, zeta0=z0, q=[qlo, qhi], nsub=nsub, nq=nq, nz=nz, sec=time.time()-t0)
    return res


if __name__ == '__main__':
    Kv, z0, qlo, qhi = [float(v) for v in sys.argv[1:5]]
    nsub = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    r = verify(Kv, z0, qlo, qhi, nsub)
    print(json.dumps(r, indent=1))
    (OUT / f'block_K{Kv:g}_z{z0:g}_q{qlo:g}_{qhi:g}.json').write_text(json.dumps(r, indent=1))

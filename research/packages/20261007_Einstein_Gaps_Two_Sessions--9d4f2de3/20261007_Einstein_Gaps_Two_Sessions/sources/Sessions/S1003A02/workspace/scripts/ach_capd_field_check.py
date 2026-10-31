"""Check that the CAPD vector field in ach_bolt_capd.cpp equals rhs_md of ach_projected.py.

(1) The vector-field string is parsed directly from the C++ source (no retyping), converted to
    sympy, and compared with rhs_md at random regular states (relative error), and symbolically
    with the exact potentials of einstein_bolt_shoot.pots.
(2) A point initial box (b=0.8, d=d*, t0) is transported by CAPD in short chained segments and
    compared with a DOP853 (rtol 1e-13) integration of rhs_md.
Output: workspace/data/ach_capd/field_check.json
"""
import json, math, re, subprocess, sys
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ach_projected import rhs_md, init_md  # noqa: E402

OUT = HERE.parent / 'data' / 'ach_capd'
OUT.mkdir(parents=True, exist_ok=True)


def parse_field():
    src = (HERE / 'ach_bolt_capd.cpp').read_text()
    block = src.split('const std::string vf =')[1].split(';\n  capd::IMap')[0]
    lits = re.findall(r'^\s*"([^"]*)"', block, flags=re.M)
    s = ''.join(lits)
    var = s.split('var:')[1].split(';')[0].split(',')
    fun = s.split('fun:')[1].rstrip(';').split(',')
    syms = sp.symbols(var)
    loc = dict(zip(var, syms)); loc['exp'] = sp.exp
    F = [sp.sympify(f.replace('^', '**'), locals=loc) for f in fun]
    return syms, F


def symbolic_check(syms, F):
    m, de, L3, ym, eta, y3, d = syms
    L = [m + de/2, m - de/2, L3]
    P = []
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        P.append(2*sp.exp(2*L[i]-2*L[j]-2*L[k]) - 8*sp.exp(-2*L[i])*sp.sinh(L[j]-L[k])**2)
    y = [ym + eta/2, ym - eta/2, y3]
    S = sum(y)
    exact = [ym, eta, y3, 6 - ym*S + (P[0]+P[1])/2, -eta*S + P[0]-P[1], 6 - y3*S + P[2], 0]
    return [sp.simplify((sp.expand((F[i] - exact[i]).rewrite(sp.exp)))) for i in range(7)]


def capd_chain(X0, d, t0, T, dt=0.05, order=30):
    box = [[float(x), float(x)] for x in X0] + [[float(d), float(d)]]
    t = t0; out = []
    while t < T - 1e-12:
        h = min(dt, T - t)
        args = ['qiushi-yau26', 'env', 'ode', str(HERE / 'ach_bolt_capd'), repr(h), str(order)]
        for lo, hi in box: args += [repr(lo), repr(hi)]
        rec = json.loads(subprocess.run(args, check=True, text=True, capture_output=True).stdout)
        box = [[float.fromhex(a), float.fromhex(b)] for a, b in rec['endpoint_hex']]
        t += h; out.append((t, box))
    return out


if __name__ == '__main__':
    syms, F = parse_field()
    res = {'field': [str(f) for f in F]}
    diffs = symbolic_check(syms, F)
    res['symbolic_difference'] = [str(x) for x in diffs]
    fn = sp.lambdify(syms, F, 'numpy')
    rng = np.random.default_rng(7)
    err = 0.0
    for _ in range(2000):
        X = np.concatenate([rng.normal(scale=1.5, size=3), rng.normal(scale=3, size=3)])
        a = np.array(fn(*X, 0.3)[:6], dtype=float); b = rhs_md(0, X)
        err = max(err, float(np.max(np.abs(a - b))/(1 + np.max(np.abs(b)))))
    res['random_state_max_rel_err'] = err
    b, d, t0, T = 0.8, 0.28699961889, 0.01, float(sys.argv[1]) if len(sys.argv) > 1 else 2.0
    X0 = init_md(b, d, t0)
    sol = solve_ivp(rhs_md, (t0, T), X0, method='DOP853', rtol=1e-13, atol=1e-30, dense_output=True)
    ch = capd_chain(list(X0), d, t0, T)
    cmp = []
    for t, box in ch[::max(1, len(ch)//10)] + [ch[-1]]:
        xf = sol.sol(t)
        lo = np.array([p[0] for p in box[:6]]); hi = np.array([p[1] for p in box[:6]])
        inside = bool(np.all(xf >= lo - 1e-9*(1+abs(xf))) and np.all(xf <= hi + 1e-9*(1+abs(xf))))
        cmp.append(dict(t=t, max_abs_diff=float(np.max(np.abs(xf - (lo+hi)/2))),
                        max_width=float(np.max(hi-lo)), float_in_box=inside))
    res['flow_compare'] = cmp
    print(json.dumps(res, indent=1))
    (OUT / 'field_check.json').write_text(json.dumps(res, indent=1))

"""Bolt-regular Einstein series for diagonal Bianchi IX, Ric = -6 g.

Metric g = dt^2 + a1^2 s1^2 + a2^2 s2^2 + a3^2 s3^2, d s_i = 2 s_j ^ s_k.
Orthonormal Ricci (checked against Cartan in S1003A01 check_bianchi_ricci_closed_form.py):
  R00 = -(a1''/a1 + a2''/a2 + a3''/a3)
  Rii = -ai''/ai - (ai'/ai)(aj'/aj + ak'/ak) + 2(ai^4 - (aj^2-ak^2)^2)/(a1 a2 a3)^2.
Bolt in slot 3 at t = 0: a3 = n t + ..., a1(0) = a2(0) = b.  n = 1 is the O(-1) bolt
(S^3 end, the blown-up ball D # CPbar^2); n = 3 gives O(-3) (lens end), used for validation
against the Kahler-Einstein Calabi-ansatz metric with bolt area pi/3.

Output: free parameters of the regular series and the coefficients as functions of them,
saved to workspace/data/einstein_bolt/series_n{n}.json (sympy srepr strings).
"""
import json, sys
from pathlib import Path
import sympy as sp

t = sp.symbols('t')
OUT = Path(__file__).resolve().parents[1] / 'data' / 'einstein_bolt'
OUT.mkdir(parents=True, exist_ok=True)


def check_models():
    s, c = sp.sinh(t), sp.cosh(t)
    def ric(A):
        d1 = [sp.diff(a, t) for a in A]; d2 = [sp.diff(a, t, 2) for a in A]
        R = [-(d2[0]/A[0] + d2[1]/A[1] + d2[2]/A[2])]
        for i in range(3):
            j, k = (i+1) % 3, (i+2) % 3
            R.append(-d2[i]/A[i] - d1[i]/A[i]*(d1[j]/A[j] + d1[k]/A[k])
                     + 2*(A[i]**4 - (A[j]**2 - A[k]**2)**2)/(A[0]*A[1]*A[2])**2)
        return [sp.simplify(sp.expand(r.rewrite(sp.exp))) for r in R]
    x0 = sp.symbols('x0', positive=True)
    print('CH (fibre slot 2):', ric([s, s*c, s]))
    RB = ric([sp.sqrt(t**2 + x0), sp.sqrt(t**2 + x0), t])
    print('Burns: scalar =', sp.simplify(sum(RB)))


def series(n, N=6):
    b = sp.symbols('b', positive=True)
    p = sp.symbols('p1:%d' % (N+1)); q = sp.symbols('q1:%d' % (N+1)); r = sp.symbols('r2:%d' % (N+2))
    a1 = b + sum(p[k-1]*t**k for k in range(1, N+1))
    a2 = b + sum(q[k-1]*t**k for k in range(1, N+1))
    a3 = n*t + sum(r[k-2]*t**k for k in range(2, N+2))
    A = [a1, a2, a3]
    d1 = [sp.diff(a, t) for a in A]; d2 = [sp.diff(a, t, 2) for a in A]
    V2 = (a1*a2*a3)**2
    eqs = []
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        # V2*(ai'' + ai'(aj'/aj + ak'/ak) - 6 ai) - 2 ai (ai^4 - (aj^2-ak^2)^2)
        e = (d2[i]*V2 + d1[i]*(d1[j]*A[j]*A[i]**2*A[k]**2 + d1[k]*A[k]*A[i]**2*A[j]**2)
             - 6*A[i]*V2 - 2*A[i]*(A[i]**4 - (A[j]**2 - A[k]**2)**2))
        eqs.append(sp.expand(e))
    # constraint: R00 = -6  <=>  sum ai'' ai aj^2 ak^2 - 6 V2 = 0
    con = sp.expand(sum(d2[i]*A[i]*A[(i+1) % 3]**2*A[(i+2) % 3]**2 for i in range(3)) - 6*V2)
    sol = {}
    unknown = list(p) + list(q) + list(r)
    free = []
    for order in range(0, N+1):
        cur = []
        for e in eqs + [con]:
            co = sp.expand(sp.expand(e).coeff(t, order).subs(sol))
            co = sp.factor(co) if co != 0 else co
            if co != 0:
                cur.append(co)
        if not cur:
            continue
        syms = sorted(set().union(*[c.free_symbols for c in cur]) & set(unknown) - set(sol), key=str)
        if not syms:
            bad = [c for c in cur if sp.simplify(c) != 0]
            if bad:
                print('order', order, 'inconsistent:', bad[:3]); return None
            continue
        ss = sp.solve(cur, syms, dict=True)
        if not ss:
            print('order', order, 'no solution in', syms, cur[:4]); return None
        if len(ss) > 1:
            print('order', order, 'multiple branches', ss)
        s0 = ss[0]
        for kk, v in s0.items():
            sol[kk] = sp.factor(v)
        sol = {kk: sp.factor(v.subs(sol)) for kk, v in sol.items()}
        print('order', order, 'solved', list(s0), flush=True)
        undet = [x for x in syms if x not in s0]
        if undet:
            free += undet
            print('order', order, 'undetermined:', undet)
    print('free parameters (besides b):', free)
    res = {str(k): sp.srepr(v) for k, v in sol.items()}
    res['_free'] = [str(f) for f in free]
    res['_N'] = N
    (OUT / f'series_n{n}.json').write_text(json.dumps(res, indent=1))
    for k in sorted(sol, key=lambda s: (str(s)[0], int(str(s)[1:]))):
        if int(str(k)[1:]) <= 5:
            print(k, '=', sp.factor(sol[k]))
    return sol, free


if __name__ == '__main__':
    check_models()
    for n in [int(a) for a in sys.argv[1:]] or [1]:
        print('==== n =', n)
        series(n)

"""Rigorous Fuchsian remainder for the regular Einstein bolt (n=1, Ric=-6g, diagonal Bianchi IX).

Metric g = dt^2 + a1^2 s1^2 + a2^2 s2^2 + a3^2 s3^2 (ds_i = 2 s_j^s_k), bolt in slot 3.
Regular variables  s = t^2,  a1 = A(s),  a2 = B(s),  a3 = t C(s),  D = s d/ds.
With A(0)=B(0)=b, C(0)=1 the Einstein equations a_i'' = 6a_i - a_i' sum_{j!=i} a_j'/a_j + a_i Pot_i
are equivalent (checked exactly below) to the Fuchsian system
  E_A := 4D^2A + 4DA(DB/B+DC/C) - 6sA - 2(A^4-B^4)/(AB^2C^2) - 4s/A + 2s^2C^2/(AB^2) = 0,
  E_B := (A<->B),
  E_C := (4D^2+2D)C + 2(C+2DC)(DA/A+DB/B) - 6sC - [2s^2C^4-2(A^2-B^2)^2]/(CA^2B^2) = 0,
  with  s*(a1''-rhs1) = E_A,  s*(a2''-rhs2) = E_B,  t*(a3''-rhs3) = E_C.
Unknowns sigma=(A+B)/2-b, delta=A-B, gamma=C-1; linear part L=(4D^2, 4D^2-16, 4D^2+2D);
delta has the resonant free coefficient delta_2 = d  (d = p4-q4 in the t-series).

Fixed-point formulation on (0,s0]: Y = Y_N + R, R = O(s^m), m = N+1,
   R = L^{-1}[ Phi(Y_N+R) - Phi(Y_N) + rho_N ],  rho_N = Phi(Y_N) - L Y_N = -(E-combinations)(Y_N),
with weighted seminorms |R_j| <= v_j s^m, |D R_j| <= w_j s^m and the explicit inverses
   (4D^2)^{-1}:        v <= F/(4m^2),          Dv <= F/(4m)
   (4D^2-16)^{-1}:     v <= F/(4(m-2)(m+2)),  Dv <= F m/(4(m-2)(m+2))
   (4D^2+2D)^{-1}:     v <= F/(2m(2m+1)),      Dv <= F/(2(2m+1)).
Interval Jacobians of Phi over the box {s in [0,s0], Y in Y_N([0,s0]) + ball} give a nonnegative
matrix M with  new_bounds <= M bounds + c;  if M r + c <= r strictly, T maps the ball to itself and is a
contraction in the r-weighted max norm, so the actual bolt solution with data (b,d) satisfies the bounds.
The script then encloses X=(m,delta_L,L3,ym,eta,y3) at t0=sqrt(s0) for given d-subintervals.

CLI: python ach_bolt_fuchs.py check
     python ach_bolt_fuchs.py boxes  N s0 dlo dhi nsub out.json [extra_lo extra_hi ...]
"""
import json, math, sys, itertools
from pathlib import Path
import sympy as sp
from flint import arb, ctx

ctx.prec = 256
HERE = Path(__file__).resolve().parent
OUT = HERE.parent / 'data' / 'ach_capd'

s, d = sp.symbols('s d')
b = sp.Rational(4, 5)
# state symbols: sig, de, ga, Dsig, Dde, Dga
SY = sp.symbols('sig de ga Dsig Dde Dga')


def ABC_from(sig, de, ga, Dsig, Dde, Dga, bb=b):
    A = bb + sig + de/2; B = bb + sig - de/2; C = 1 + ga
    DA = Dsig + Dde/2; DB = Dsig - Dde/2; DC = Dga
    return A, B, C, DA, DB, DC


def R_parts(s_, A, B, C, DA, DB, DC):
    RA = -4*DA*(DB/B + DC/C) + 6*s_*A + 2*(A**4-B**4)/(A*B**2*C**2) + 4*s_/A - 2*s_**2*C**2/(A*B**2)
    RB = -4*DB*(DA/A + DC/C) + 6*s_*B + 2*(B**4-A**4)/(B*A**2*C**2) + 4*s_/B - 2*s_**2*C**2/(B*A**2)
    RC = -2*(C + 2*DC)*(DA/A + DB/B) + 6*s_*C + (2*s_**2*C**4 - 2*(A**2-B**2)**2)/(C*A**2*B**2)
    return RA, RB, RC


def Phi(s_, st, bb=b):
    sig, de, ga, Dsig, Dde, Dga = st
    A, B, C, DA, DB, DC = ABC_from(sig, de, ga, Dsig, Dde, Dga, bb)
    RA, RB, RC = R_parts(s_, A, B, C, DA, DB, DC)
    return [(RA + RB)/2, RA - RB - 16*de, RC]


def Dop(expr):
    return sp.expand(s*sp.diff(expr, s))


def check_equivalence():
    """Exact check s*(a1''-rhs1)=E_A etc. on random rational polynomial A,B,C."""
    t = sp.Symbol('t', positive=True)
    import random
    random.seed(3)
    rp = lambda c0: c0 + sum(sp.Rational(random.randint(-9, 9), random.randint(1, 9))*s**k for k in range(1, 4))
    A, B, C = rp(b), rp(b), rp(sp.Integer(1))
    DA, DB, DC = Dop(A), Dop(B), Dop(C)
    EA = 4*Dop(DA) + 4*DA*(DB/B + DC/C) - 6*s*A - 2*(A**4-B**4)/(A*B**2*C**2) - 4*s/A + 2*s**2*C**2/(A*B**2)
    EB = 4*Dop(DB) + 4*DB*(DA/A + DC/C) - 6*s*B - 2*(B**4-A**4)/(B*A**2*C**2) - 4*s/B + 2*s**2*C**2/(B*A**2)
    EC = 4*Dop(DC) + 2*DC + 2*(C + 2*DC)*(DA/A + DB/B) - 6*s*C - (2*s**2*C**4 - 2*(A**2-B**2)**2)/(C*A**2*B**2)
    a = [A.subs(s, t**2), B.subs(s, t**2), t*C.subs(s, t**2)]
    res = []
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        Pot = 2*a[i]**2/(a[j]**2*a[k]**2) - 2*(a[j]/a[k] - a[k]/a[j])**2/a[i]**2
        rhs = 6*a[i] - sp.diff(a[i], t)*(sp.diff(a[j], t)/a[j] + sp.diff(a[k], t)/a[k]) + a[i]*Pot
        res.append(sp.diff(a[i], t, 2) - rhs)
    diffs = [sp.simplify(t**2*res[0] - EA.subs(s, t**2)), sp.simplify(t**2*res[1] - EB.subs(s, t**2)),
             sp.simplify(t*res[2] - EC.subs(s, t**2))]
    return [str(x) for x in diffs]


def series(N):
    """Exact series sigma,delta,gamma to order s^N with b=4/5 and free d=delta_2."""
    sg = [sp.Integer(0)] + list(sp.symbols(f'sg1:{N+1}'))
    dl = [sp.Integer(0)] + list(sp.symbols(f'dl1:{N+1}'))
    gm = [sp.Integer(0)] + list(sp.symbols(f'gm1:{N+1}'))
    sol = {}
    if N >= 2:
        sol[dl[2]] = d
    for k in range(1, N+1):
        sig = sum(sg[j]*s**j for j in range(1, k+1)); de = sum(dl[j]*s**j for j in range(1, k+1))
        ga = sum(gm[j]*s**j for j in range(1, k+1))
        sig, de, ga = [sp.expand(x.subs(sol)) for x in (sig, de, ga)]
        st = [sig, de, ga, Dop(sig), Dop(de), Dop(ga)]
        A, B, C, DA, DB, DC = ABC_from(*st)
        RA, RB, RC = R_parts(s, A, B, C, DA, DB, DC)
        EA = 4*Dop(DA) - RA; EB = 4*Dop(DB) - RB; EC = 4*Dop(DC) + 2*DC - RC
        eqs = []
        for E, den in ((EA, A*B**2*C**2), (EB, B*A**2*C**2), (EC, C*A**2*B**2)):
            P = sp.expand(sp.cancel(sp.together(E*den)))
            eqs.append(sp.expand(P.coeff(s, k)))
        unk = [x for x in (sg[k], dl[k], gm[k]) if x not in sol]
        if k == 2:
            # resonance: the delta_2 equation must be automatically satisfied
            sk = sp.solve(eqs, unk, dict=True)
            assert len(sk) == 1, (k, eqs)
            sol.update(sk[0])
        else:
            sk = sp.solve(eqs, unk, dict=True)
            assert len(sk) == 1, (k, eqs)
            sol.update(sk[0])
        sol = {kk: sp.factor(v.subs(sol)) for kk, v in sol.items()}
    sig = sum(sp.sympify(sg[j]).subs(sol)*s**j for j in range(1, N+1))
    de = sum(sp.sympify(dl[j]).subs(sol)*s**j for j in range(1, N+1))
    ga = sum(sp.sympify(gm[j]).subs(sol)*s**j for j in range(1, N+1))
    return sp.expand(sig), sp.expand(de), sp.expand(ga)


def to_arb(e, env):
    e = sp.sympify(e)
    if e.is_Integer: return arb(int(e))
    if e.is_Rational: return arb(int(e.p))/int(e.q)
    if e.is_Symbol: return env[e]
    if e.is_Add:
        z = arb(0)
        for a in e.args: z += to_arb(a, env)
        return z
    if e.is_Mul:
        z = arb(1)
        for a in e.args: z *= to_arb(a, env)
        return z
    if e.is_Pow and e.args[1].is_Integer:
        base = to_arb(e.args[0], env); n = int(e.args[1])
        return base**n if n >= 0 else 1/(base**(-n))
    raise ValueError(e)


def poly_eval(p, s_box, d_box):
    """Horner evaluation in s of a polynomial with d-polynomial coefficients (reduces wrapping)."""
    P = sp.Poly(p, s)
    cs = P.all_coeffs()
    z = arb(0)
    for c in cs:
        z = z*s_box + to_arb(sp.expand(c), {d: d_box})
    return z


def ball(lo, hi):
    lo, hi = arb(lo), arb(hi)
    return arb.union(lo, hi)


def s_cells(s0, nsplit, cplx):
    """Real subintervals of [0,s0], or (cplx) acb squares covering the closed disc |s|<=s0.
    With cplx=True every estimate holds on the complex disc, so the fixed point (built from radial
    integrals (D-c)^{-1}f(s)=int_0^1 lam^{-c-1} f(lam s) dlam) is holomorphic in s: A,B,C are
    real-analytic functions of s=t^2 and the metric is real-analytic across the bolt."""
    if not cplx:
        return [ball(s0*j/nsplit, s0*(j+1)/nsplit) for j in range(nsplit)]
    from flint import acb
    edges = [-s0 + 2*s0*j/nsplit for j in range(nsplit+1)]
    cells = []
    for i in range(nsplit):
        for j in range(nsplit):
            x0, x1, y0, y1 = edges[i], edges[i+1], edges[j], edges[j+1]
            if min(abs(x0), abs(x1), 0 if x0 < 0 < x1 else 9)**2 * 0 + \
               (0 if x0 <= 0 <= x1 else min(x0*x0, x1*x1)) + (0 if y0 <= 0 <= y1 else min(y0*y0, y1*y1)) > s0*s0:
                continue   # square disjoint from the disc
            cells.append(acb(ball(x0, x1), ball(y0, y1)))
    return cells


def up(x):
    """Outward (upward) binary64 bound of an arb upper endpoint: float() rounds to nearest, so
    step one ulp up and inflate by 1e-12 relative; the result is >= the true supremum."""
    v = float(arb(x).upper())
    return math.nextafter(v, math.inf)*(1 + 1e-12) + 1e-300


def remainder_bound(N, s0, dlo, dhi, nsplit=16, cplx=False):
    m = N + 1
    cells = s_cells(s0, nsplit, cplx)
    sig, de, ga = series(N)
    Ys = [sig, de, ga, Dop(sig), Dop(de), Dop(ga)]
    # residual rho_N = Phi(Y_N) - L Y_N, as exact rational functions; divide numerators by s^m
    Ph = Phi(s, Ys)
    LY = [4*Dop(Dop(sig)), 4*Dop(Dop(de)) - 16*de, 4*Dop(Dop(ga)) + 2*Dop(ga)]
    rho_q = []
    for i in range(3):
        r = sp.together(Ph[i] - LY[i])
        num, den = sp.fraction(r)
        num = sp.expand(num); den = sp.expand(den)
        qn, rem = sp.div(sp.Poly(num, s), sp.Poly(s**m, s))
        assert rem.is_zero, ('residual not O(s^m)', i)
        rho_q.append((qn.as_expr(), den))
    dB = ball(dlo, dhi)
    # sup |rho_i|/s^m over [0,s0] by subdivision
    c = [arb(0)]*3
    for sb in cells:
        for i in range(3):
            num, den = rho_q[i]
            v = poly_eval(num, sb, dB)/poly_eval(den, sb, dB)
            c[i] = arb(max(float(c[i].upper()), up(abs(v))))
    # Jacobian of Phi w.r.t. the six state variables
    Phs = Phi(s, list(SY))
    J = [[sp.diff(Phs[i], SY[j]) for j in range(6)] for i in range(3)]
    Jf = [[sp.lambdify((s, d) + SY, J[i][j], modules=[{'exp': lambda x: x.exp()}]) for j in range(6)]
          for i in range(3)]
    # inverse factors: (value, D) for each component
    inv = [(1/(4*m*m), 1/(4*m)), (1/(4*(m-2)*(m+2)), m/(4*(m-2)*(m+2))), (1/(2*m*(2*m+1)), 1/(2*(2*m+1)))]
    cf = [up(x) for x in c]
    r = [inv[i // 2][i % 2]*cf[i // 2]*2 for i in range(6)]   # initial guess
    r = [max(x, 1e-300) for x in r]
    for it in range(8):
        # box of states: Y_N([0,s0]) + ball radius r_j s0^m
        Mrow = [[0.0]*6 for _ in range(3)]
        for sb in cells:
            st = []
            for q in range(6):
                base = poly_eval(Ys[q], sb, dB)
                st.append(base + arb(0, r[q]*s0**m*1.0000001 + 1e-300))
            for i in range(3):
                for q in range(6):
                    v = Jf[i][q](sb, dB, *st)
                    v = arb(v) if isinstance(v, (int, float)) else v
                    Mrow[i][q] = max(Mrow[i][q], up(abs(v)))
        new = []
        for i in range(6):
            comp = i // 2
            F = cf[comp] + sum(Mrow[comp][q]*r[q] for q in range(6))
            new.append(inv[comp][i % 2]*F)
        ok = all(new[i] < r[i] for i in range(6))
        if ok:
            # re-verify the self-map and contraction inequalities in Arb (directed), with exact
            # rational inverse factors, so no binary64 rounding enters the certificate
            invA = [(arb(1)/(4*m*m), arb(1)/(4*m)), (arb(1)/(4*(m-2)*(m+2)), arb(m)/(4*(m-2)*(m+2))),
                    (arb(1)/(2*m*(2*m+1)), arb(1)/(2*(2*m+1)))]
            newA, lipA = [], []
            for i in range(6):
                comp = i // 2
                MS = sum((arb(Mrow[comp][q])*arb(r[q]) for q in range(6)), arb(0))
                newA.append(invA[comp][i % 2]*(arb(cf[comp]) + MS))
                lipA.append(invA[comp][i % 2]*MS/arb(r[i]))
            if not all(newA[i] < arb(r[i]) for i in range(6)):
                r = [1.5*max(new[i], r[i]) for i in range(6)]
                continue
            lip = max(up(x) for x in lipA)
            new = [up(x) for x in newA]
            return dict(N=N, m=m, s0=s0, d=[dlo, dhi], complex_disc=cplx, ncells=len(cells), rho_sup=cf, M=Mrow, r=r, new=new, lip=lip,
                        ok=bool(lip < 1), series=[str(sig), str(de), str(ga)]), (sig, de, ga)
        r = [1.5*max(new[i], r[i]) for i in range(6)]
    raise RuntimeError('no self-mapping ball found')


def enclose_X(series_, rec, dlo, dhi):
    """Arb enclosure of X=(m,delta_L,L3,ym,eta,y3) at t0=sqrt(s0) for all d in [dlo,dhi]."""
    sig, de, ga = series_
    s0 = rec['s0']; m = rec['m']; r = rec['r']
    sB = arb(str(s0)) if False else arb(s0)   # s0 is a binary64 number; use it exactly
    t0 = sB.sqrt()
    dB = ball(dlo, dhi)
    vals = []
    for q, p in enumerate([sig, de, ga, Dop(sig), Dop(de), Dop(ga)]):
        vals.append(poly_eval(p, sB, dB) + arb(0, r[q]*s0**m*1.0000001))
    sg, dl, gm, Dsg, Ddl, Dgm = vals
    bb = arb(4)/5
    A = bb + sg + dl/2; B = bb + sg - dl/2; C = 1 + gm
    DA = Dsg + Ddl/2; DB = Dsg - Ddl/2
    mm = (A.log() + B.log())/2
    deL = (1 + dl/B).log()                      # log(A/B), relative precision kept
    L3 = (t0*C).log()
    ym = (DA/A + DB/B)/t0
    eta = 2*(Ddl*(bb + sg) - dl*Dsg)/(A*B*t0)   # (2/t)(DA/A-DB/B), cancellation-free
    y3 = (1 + 2*Dgm/C)/t0
    X = [mm, deL, L3, ym, eta, y3, dB]
    out = []
    for x in X:
        lo = float(x.lower()); hi = float(x.upper())
        out.append([math.nextafter(lo, -math.inf), math.nextafter(hi, math.inf)])
    return out, [str(x) for x in X], float(t0.mid())


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'check':
        print('equivalence residuals:', check_equivalence())
        sig, de, ga = series(4)
        print('sigma =', sig); print('delta =', de); print('gamma =', ga)
        ser = json.loads((HERE.parent/'data'/'einstein_bolt'/'series_n1.json').read_text())
        loc = {'Integer': sp.Integer, 'Rational': sp.Rational, 'Symbol': sp.Symbol, 'Mul': sp.Mul,
               'Add': sp.Add, 'Pow': sp.Pow}
        bs = sp.Symbol('b', positive=True)
        p2 = sp.sympify(ser['p2'], locals=loc).subs(bs, b); r3 = sp.sympify(ser['r3'], locals=loc).subs(bs, b)
        r5 = sp.sympify(ser['r5'], locals=loc).subs(bs, b)
        print('compare p2:', sp.simplify(sig.coeff(s, 1) - p2), ' r3:', sp.simplify(ga.coeff(s, 1) - r3),
              ' r5:', sp.simplify(ga.coeff(s, 2) - r5))
    elif mode == 'boxes':
        N = int(sys.argv[2]); s0 = float(sys.argv[3]); dlo = float(sys.argv[4]); dhi = float(sys.argv[5])
        nsub = int(sys.argv[6]); out = sys.argv[7]
        extra = [float(x) for x in sys.argv[8:]]
        import os
        cplx = os.environ.get('FUCHS_COMPLEX', '0') == '1'
        rec, ser = remainder_bound(N, s0, dlo, dhi, nsplit=8 if cplx else 16, cplx=cplx)
        print(json.dumps({k: v for k, v in rec.items() if k != 'series'}, indent=1), flush=True)
        boxes = []
        grid = [(dlo + (dhi-dlo)*i/nsub, dlo + (dhi-dlo)*(i+1)/nsub) for i in range(nsub)]
        grid += [(extra[2*i], extra[2*i+1]) for i in range(len(extra)//2)]
        for lo, hi in grid:
            assert dlo <= lo <= hi <= dhi
            bx, arbs, t0 = enclose_X(ser, rec, lo, hi)
            boxes.append(dict(d=[lo, hi], t0=t0, binary64_box=bx, arb=arbs))
        rec['boxes'] = boxes
        Path(out).write_text(json.dumps(rec, indent=1))
        print('wrote', out, len(boxes), 'boxes; t0 =', boxes[0]['t0'])

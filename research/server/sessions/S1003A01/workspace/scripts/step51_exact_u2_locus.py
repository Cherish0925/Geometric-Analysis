"""Step 51b: EXACT (sympy, rational) log coefficient F on the U(2)_zeta-invariant curvature locus.

If W+_p has zeta as an eigenvector and is scalar on zeta^perp (T = 0, no mixed block), W-_p = 0, Ric0_p = 0,
then the background 2-jet h2 is U(2)_zeta-invariant. The CGB corner functional F(k0) is convex quadratic in the
degree-0 corrector k0 and U(2)_zeta-invariant, so its infimum over any U(2)_zeta-stable corrector class is attained
on invariant correctors (average a minimizing sequence over the compact group). Degree-0 invariant symmetric
tensors on C^2\\0: Pr = xx^T/u, P3 = v2v2^T/u (Burns fibre, v2 = J_zeta x), K = (v0v0^T+v1v1^T)/u, and
X = sym(x v2^T)/u. U(2)_zeta acts transitively on S^3 and every ingredient is invariant, so the a^2 eps^2
density is CONSTANT on S^3: F = (2 pi^2 / 8 pi^2) * density(x0) = density(x0)/4 at one point x0.

Background: s and lam = W+(zeta,zeta) free symbols; W+ = diag(-lam/2, -lam/2, lam) in (J1,J2,J3), zeta = J3.
  h2 = sum_m (-s/36 - lam_m/6) v_m v_m^T   (h2 = -(1/3) R_ikjl x^k x^l)
Metric: g = delta + a h2 + eps (kB + a k0),  kB = (v0v0^T+v1v1^T)/u^2.
Output: exact F_opt(s, lam), the optimal invariant corrector, and the [a eps] coefficient (must be 0).
Saved to workspace/data/step51/exact_u2_locus.json
"""
import os, json, itertools
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step51"); os.makedirs(OUT, exist_ok=True)

x = sp.symbols('x0:4', real=True)
a, e = sp.symbols('a e')
s, lam = sp.symbols('s lam', real=True)
c = sp.symbols('c0:4', real=True)
X = sp.Matrix(x)

def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return [a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2]
E4 = sp.eye(4)
Jm = [sp.zeros(4, 4) for _ in range(3)]
for cc in range(4):
    for b in range(4):
        pc = [E4[cc, i] for i in range(4)]; pc = [pc[0], -pc[1], -pc[2], -pc[3]]
        prod = qmul(pc, [E4[b, i] for i in range(4)])
        for m in range(3):
            Jm[m][b, cc] = prod[m+1]
v = [Jm[m]*X for m in range(3)]
u = sum(xi**2 for xi in x)
lams = [-lam/2, -lam/2, lam]
h2 = sp.zeros(4, 4)
for m in range(3):
    h2 += (-s/36 - lams[m]/6) * v[m]*v[m].T
kB = (v[0]*v[0].T + v[1]*v[1].T)/u**2
Pr = X*X.T/u; P3 = v[2]*v[2].T/u; Kh = (v[0]*v[0].T + v[1]*v[1].T)/u
Xm = (X*v[2].T + v[2]*X.T)/(2*u)
k0 = c[0]*Pr + c[1]*P3 + c[2]*Kh + c[3]*Xm
G = sp.eye(4) + a*h2 + e*(kB + a*k0)

x0 = {x[0]: 1, x[1]: 0, x[2]: 0, x[3]: 0}
def at0(M): return M.subs(x0)
g0 = at0(G)
dg = [[[sp.expand(at0(sp.diff(G[i, j], x[k]))) for k in range(4)] for j in range(4)] for i in range(4)]
ddg = [[[[sp.expand(at0(sp.diff(G[i, j], x[k], x[l]))) for l in range(4)] for k in range(4)] for j in range(4)] for i in range(4)]
print("jets done", flush=True)

def trunc(expr):
    p = sp.Poly(sp.expand(expr), a, e)
    out = 0
    for (da, de), cf in p.terms():
        if da <= 2 and de <= 2:
            out += cf*a**da*e**de
    return out
def tmat(M): return M.applyfunc(trunc)

H = g0 - sp.eye(4)
gi = sp.eye(4); Hp = sp.eye(4)
for n in range(1, 5):
    Hp = tmat(Hp*H); gi = gi + (-1)**n*Hp
gi = tmat(gi)
BIN = [1, sp.Rational(-1, 2), sp.Rational(3, 8), sp.Rational(-5, 16), sp.Rational(35, 128)]
ef = sp.eye(4); Hp = sp.eye(4)
for n in range(1, 5):
    Hp = tmat(Hp*H); ef = ef + BIN[n]*Hp
ef = tmat(ef)
print("inverse/frame done", flush=True)

R4 = range(4)
Gl = [[[sp.Rational(1, 2)*(dg[d][c_][b] + dg[d][b][c_] - dg[b][c_][d]) for c_ in R4] for b in R4] for d in R4]
Gam = [[[trunc(sum(gi[A, d]*Gl[d][b][c_] for d in R4)) for c_ in R4] for b in R4] for A in R4]
dgi = [[[trunc(-sum(gi[A, m]*dg[m][n][k]*gi[n, d] for m in R4 for n in R4)) for k in R4] for d in R4] for A in R4]
dGl = [[[[sp.Rational(1, 2)*(ddg[d][c_][b][E] + ddg[d][b][c_][E] - ddg[b][c_][d][E]) for E in R4] for c_ in R4] for b in R4] for d in R4]
dGam = [[[[trunc(sum(dgi[A][d][E]*Gl[d][b][c_] + gi[A, d]*dGl[d][b][c_][E] for d in R4)) for E in R4] for c_ in R4] for b in R4] for A in R4]
print("christoffel done", flush=True)
# R^A_{bcd} = d_c Gam^A_db - d_d Gam^A_cb + Gam^A_ce Gam^e_db - Gam^A_de Gam^e_cb
Rup = {}
for A in R4:
    for b in R4:
        for c_ in R4:
            for d in R4:
                if c_ < d:
                    val = dGam[A][d][b][c_] - dGam[A][c_][b][d] + sum(Gam[A][c_][E]*Gam[E][d][b] - Gam[A][d][E]*Gam[E][c_][b] for E in R4)
                    Rup[(A, b, c_, d)] = trunc(val)
def Rlow(A, b, c_, d):
    if c_ == d: return 0
    sg = 1
    if c_ > d: c_, d, sg = d, c_, -1
    return sg*trunc(sum(g0[A, m]*Rup[(m, b, c_, d)] for m in R4))
Rl = {}
for A in R4:
    for b in R4:
        for c_ in R4:
            for d in R4:
                Rl[(A, b, c_, d)] = Rlow(A, b, c_, d)
print("riemann done", flush=True)
# frame components
# first contract one index at a time
def contract(T, M, pos):
    out = {}
    for key in T:
        pass
    keys = list(itertools.product(R4, repeat=4))
    for kk in keys:
        acc = 0
        for i in R4:
            kk2 = list(kk); kk2[pos] = i
            acc += M[i, kk[pos]]*T[tuple(kk2)]
        out[kk] = trunc(acc)
    return out
Rf = Rl
for pos in range(4):
    Rf = contract(Rf, ef, pos)
print("frame done", flush=True)
Ric = sp.Matrix(4, 4, lambda b, d: trunc(sum(Rf[(A, b, A, d)] for A in R4)))
sc = trunc(Ric.trace())
I = sp.eye(4)
def Wf(A, b, c_, d):
    return (Rf[(A, b, c_, d)] - sp.Rational(1, 2)*(I[A, c_]*Ric[b, d] - I[A, d]*Ric[b, c_] - I[b, c_]*Ric[A, d] + I[b, d]*Ric[A, c_])
            + sc/6*(I[A, c_]*I[b, d] - I[A, d]*I[b, c_]))
PAIRS = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
M = sp.Matrix(6, 6, lambda i, j: Wf(*PAIRS[i], *PAIRS[j]))
Jv = sp.Matrix(3, 6, lambda m, i: Jm[m][PAIRS[i][0], PAIRS[i][1]])
Jv = sp.Matrix([Jv.row(m)/sp.sqrt(sum(Jv[m, i]**2 for i in range(6))) for m in range(3)])
Wp = tmat(Jv*M*Jv.T)
det = trunc(g0.det())
D = det - 1
sq = 1; Dp = 1
for n, bc in enumerate([sp.Rational(1, 2), sp.Rational(-1, 8), sp.Rational(1, 16), sp.Rational(-5, 128)], start=1):
    Dp = trunc(Dp*D); sq += bc*Dp
f = trunc((4*sum(Wp[i, j]**2 for i in range(3) for j in range(3)) + sc**2/12)*sq)
P = sp.Poly(f, a, e)
c22 = sp.simplify(P.coeff_monomial(a**2*e**2))
c11 = sp.simplify(P.coeff_monomial(a*e))
c02 = sp.simplify(P.coeff_monomial(e**2))
F = sp.expand(c22/4)
print("F(c) =", F, flush=True)
grad = [sp.diff(F, ci) for ci in c]
sol = sp.solve(grad, c, dict=True)
print("solutions", sol, flush=True)
Fopt = sp.factor(sp.simplify(F.subs(sol[0]))) if sol else None
Hess = sp.hessian(F, c)
res = {"F_of_c": str(F), "Fopt": str(Fopt), "opt_corrector": str(sol), "hessian": str(Hess),
       "hessian_eigs": str(Hess.eigenvals()), "a_eps_coef_density": str(c11), "eps2_coef_density(pure Burns)": str(c02),
       "A02_Phi": str(sp.factor(-(lam + s/12)*((lam + s/12) - s/8)))}
F_A02 = -(lam + s/12)*((lam + s/12) - s/8)
res["Fopt_minus_A02"] = str(sp.simplify(Fopt - F_A02)) if Fopt is not None else None
res["kernel_point_value (lam=-s/12)"] = str(sp.simplify(Fopt.subs(lam, -s/12))) if Fopt is not None else None
print(json.dumps(res, indent=1))
json.dump(res, open(os.path.join(OUT, "exact_u2_locus.json"), "w"), indent=1)

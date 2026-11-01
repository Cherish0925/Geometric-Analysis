"""Step 52a: EXACT (sympy) perpendicular-Burns log coefficient F for an ARBITRARY Einstein curvature 2-jet with
W^- = 0, over the FULL SU(2)_- -invariant degree-0 corrector space, plus the explicit kernel-direction family.

Key symmetry: if W^-_p = 0 and Ric0_p = 0, every ingredient (h2, kB, correctors built from x and v_m = J_m x,
J_m the self-dual complex structures) is SU(2)_- -equivariant; SU(2)_- commutes with the J_m and acts
transitively on S^3. Hence for SU(2)_- -invariant correctors the a^2 eps^2 CGB density is CONSTANT on S^3 and
  F = (1/8pi^2) * 2pi^2 * density(x0) = density(x0)/4     (exact, no quadrature).
By convexity of F in the corrector and compactness of SU(2)_-, inf over ANY SU(2)_- -stable class of degree-0
correctors equals the inf over the invariant ones, which are spanned by the 10 tensors sym(v_i v_j^T)/u,
0<=i<=j<=3, v_0 = x.  (W^- and Ric0 jets decouple from this sector by SU(2)_- irreducibility; Step 50.)

Background jet: s, and W+ = w (3x3 symmetric trace-free, basis J1,J2,J3; zeta = J3), with w23 = 0 by a U(1)_+
rotation (no loss of generality):
  h2 = -(s/36) sum_m v_m v_m^T - (1/6) sum_{m,n} w_mn v_m v_n^T          ( = -(1/3) R_ikjl x^k x^l )
Metric g = delta + a h2 + eps (kB + a k0).
Outputs (workspace/data/step52/exact_su2minus_general.json):
  * check that the [a] coefficient of W+ at x0 equals w and [a] of s equals s (jet normalization);
  * F(c) on the 10-dim space, its exact minimum F_opt(s,w) (compared with A02's Phi when w13 = 0);
  * F of the explicit kernel-direction family (Spirit #61)
        k0 = (7A/4)(P1+P2) + (A/2)P3 + (1/3) sum_{i,j<=2} T_ij v_i v_j^T/u,   A = -s/12,
    on the kernel locus w33 = -s/12, T = trace-free part of R+ = w + s/12 on zeta^perp;
  * [a eps] diagonal coefficient (must vanish).
"""
import os, json, itertools, time
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step52"); os.makedirs(OUT, exist_ok=True)
t00 = time.time()
x = sp.symbols('x0:4', real=True)
a, e = sp.symbols('a e')
s, w11, w22, w12, w13 = sp.symbols('s w11 w22 w12 w13', real=True)
C = sp.symbols('c0:10', real=True)
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
V = [X] + v                                   # v_0 = x
u = sum(xi**2 for xi in x)
w33 = -w11 - w22
W = sp.Matrix([[w11, w12, w13], [w12, w22, 0], [w13, 0, w33]])
h2 = sp.zeros(4, 4)
for m in range(3):
    h2 += (-s/36)*v[m]*v[m].T
    for n in range(3):
        h2 += (-sp.Rational(1, 6)*W[m, n])*v[m]*v[n].T
kB = (v[0]*v[0].T + v[1]*v[1].T)/u**2
basis = []
names = []
for i in range(4):
    for j in range(i, 4):
        basis.append((V[i]*V[j].T + V[j]*V[i].T)/(2*u)); names.append(f"sym(v{i}v{j})/u")
k0 = sp.zeros(4, 4)
for ci, B in zip(C, basis):
    k0 += ci*B
G = sp.eye(4) + a*h2 + e*(kB + a*k0)

x0 = {x[0]: 1, x[1]: 0, x[2]: 0, x[3]: 0}
def at0(M): return M.subs(x0)
g0 = at0(G)
dg = [[[sp.expand(at0(sp.diff(G[i, j], x[k]))) for k in range(4)] for j in range(4)] for i in range(4)]
ddg = [[[[sp.expand(at0(sp.diff(G[i, j], x[k], x[l]))) for l in range(4)] for k in range(4)] for j in range(4)] for i in range(4)]
print("jets done", time.time()-t00, flush=True)

def trunc(expr):
    expr = sp.expand(expr)
    if expr == 0:
        return 0
    p = sp.Poly(expr, a, e)
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
print("inverse/frame done", time.time()-t00, flush=True)

R4 = range(4)
Gl = [[[sp.Rational(1, 2)*(dg[d][c_][b] + dg[d][b][c_] - dg[b][c_][d]) for c_ in R4] for b in R4] for d in R4]
Gam = [[[trunc(sum(gi[A, d]*Gl[d][b][c_] for d in R4)) for c_ in R4] for b in R4] for A in R4]
dgi = [[[trunc(-sum(gi[A, m]*dg[m][n][k]*gi[n, d] for m in R4 for n in R4)) for k in R4] for d in R4] for A in R4]
dGl = [[[[sp.Rational(1, 2)*(ddg[d][c_][b][E] + ddg[d][b][c_][E] - ddg[b][c_][d][E]) for E in R4] for c_ in R4] for b in R4] for d in R4]
dGam = [[[[trunc(sum(dgi[A][d][E]*Gl[d][b][c_] + gi[A, d]*dGl[d][b][c_][E] for d in R4)) for E in R4] for c_ in R4] for b in R4] for A in R4]
print("christoffel done", time.time()-t00, flush=True)
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
Rl = {(A, b, c_, d): Rlow(A, b, c_, d) for A in R4 for b in R4 for c_ in R4 for d in R4}
print("riemann done", time.time()-t00, flush=True)
def contract(T, M, pos):
    out = {}
    for kk in itertools.product(R4, repeat=4):
        acc = 0
        for i in R4:
            kk2 = list(kk); kk2[pos] = i
            acc += M[i, kk[pos]]*T[tuple(kk2)]
        out[kk] = trunc(acc)
    return out
Rf = Rl
for pos in range(4):
    Rf = contract(Rf, ef, pos)
print("frame done", time.time()-t00, flush=True)
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
# jet normalization check: [a] coefficients
Wa = Wp.applyfunc(lambda z: sp.Poly(sp.expand(z), a, e).coeff_monomial(a) if z != 0 else 0)
sa = sp.Poly(sp.expand(sc), a, e).coeff_monomial(a)
norm_check = {"W+_[a]_minus_w": str(sp.simplify(Wa - W)), "s_[a]_minus_s": str(sp.simplify(sa - s))}
print(norm_check, flush=True)
det = trunc(g0.det())
D = det - 1
sq = 1; Dp = 1
for n, bc in enumerate([sp.Rational(1, 2), sp.Rational(-1, 8), sp.Rational(1, 16), sp.Rational(-5, 128)], start=1):
    Dp = trunc(Dp*D); sq += bc*Dp
f = trunc((4*sum(Wp[i, j]**2 for i in range(3) for j in range(3)) + sc**2/12)*sq)
P = sp.Poly(f, a, e)
c22 = sp.expand(P.coeff_monomial(a**2*e**2))
c11 = sp.expand(P.coeff_monomial(a*e))
c02 = sp.expand(P.coeff_monomial(e**2))
F = sp.expand(c22/4)
print("F assembled", time.time()-t00, flush=True)

# --- explicit kernel-direction family (Spirit #61) on the kernel locus w33 = -s/12 ---
Acoef = -s/12
ker = {w22: -w11 + s/12}          # w11 + w22 = -w33 = s/12  <=>  w33 = -s/12
T11 = (w11 - w22)/2; T12 = w12
# basis index map
idx = {nm: k for k, nm in enumerate(names)}
fam = {ci: 0 for ci in C}
# P_i = v_i v_i^T/u  (i = 1,2,3 in V indexing; J1,J2 = V[1],V[2]; zeta = J3 = V[3])
fam[C[idx["sym(v1v1)/u"]]] = sp.Rational(7, 4)*Acoef + T11/3
fam[C[idx["sym(v2v2)/u"]]] = sp.Rational(7, 4)*Acoef - T11/3
fam[C[idx["sym(v3v3)/u"]]] = Acoef/2
fam[C[idx["sym(v1v2)/u"]]] = 2*T12/3
Ffam = sp.factor(sp.expand(F.subs(fam).subs(w13, 0).subs(ker)))
Tnorm2 = sp.expand((2*T11**2 + 2*T12**2).subs(ker))
res = {"norm_check": norm_check, "a_eps_coef_density": str(sp.simplify(c11)),
       "eps2_pure_burns_density": str(sp.simplify(c02)),
       "F_family_kernel": str(Ffam), "F_family_plus_T2": str(sp.simplify(Ffam + Tnorm2)),
       "T2_on_kernel": str(sp.factor(Tnorm2))}
print(json.dumps(res, indent=1), flush=True)
# sign variant of the T-term (diagnostic)
fam2 = dict(fam)
fam2[C[idx["sym(v1v1)/u"]]] = sp.Rational(7, 4)*Acoef - T11/3
fam2[C[idx["sym(v2v2)/u"]]] = sp.Rational(7, 4)*Acoef + T11/3
fam2[C[idx["sym(v1v2)/u"]]] = -2*T12/3
res["F_family_opposite_T_sign"] = str(sp.factor(sp.expand(F.subs(fam2).subs(w13, 0).subs(ker))))

# --- exact minimum over the 10-dim invariant space ---
grad = [sp.diff(F, ci) for ci in C]
Hs = sp.hessian(F, C)
res["hessian"] = str(Hs)
res["hessian_eigs"] = str(Hs.eigenvals())
lin = sp.linear_eq_to_matrix(grad, C)
Amat, bvec = lin
sol = sp.linsolve((Amat, bvec), C)
sol = list(sol)
res["opt_solution_set"] = str(sol)
if sol:
    subs_opt = dict(zip(C, sol[0]))
    Fopt = sp.factor(sp.simplify(F.subs(subs_opt)))
    # free parameters (null directions) should drop out
    res["Fopt"] = str(Fopt)
    mu1 = w11 + s/12; mu2 = w22 + s/12; mu3 = w33 + s/12
    Phi = -mu3*(mu3 - mu1 - mu2)/2 - (mu1 - mu2)**2/2
    res["Fopt_minus_A02Phi_at_w13=0"] = str(sp.simplify(Fopt.subs(w13, 0) - Phi))
    res["Fopt_w13_part"] = str(sp.factor(sp.simplify(Fopt - Fopt.subs(w13, 0))))
    res["Fopt_kernel"] = str(sp.factor(sp.simplify(Fopt.subs(w13, 0).subs(ker))))
    res["family_minus_opt_on_kernel"] = str(sp.simplify(Ffam - Fopt.subs(w13, 0).subs(ker)))
res["F_of_c"] = str(F)
res["time_s"] = time.time()-t00
print(json.dumps({k: v for k, v in res.items() if k not in ("F_of_c", "hessian")}, indent=1))
json.dump(res, open(os.path.join(OUT, "exact_su2minus_general.json"), "w"), indent=1)

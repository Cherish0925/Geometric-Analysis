"""Step 52a analysis: exact consequences of the rational quadratic form Q (step52_exact_su2minus_fast.py).
Input : workspace/data/step52a/exact_su2minus_Q.json
Output: workspace/data/step52a/exact_su2minus_analysis.json
"""
import os, json
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "data", "step52a")
d = json.load(open(os.path.join(D, "exact_su2minus_Q.json")))
Q = sp.Matrix([[sp.Rational(z) for z in row] for row in d["Q"]])
s, w11, w22, w12, w13 = sp.symbols('s w11 w22 w12 w13', real=True)
C = sp.symbols('c0:10', real=True)
vv = sp.Matrix([s, w11, w22, w12, w13, *C])
F = sp.expand((vv.T*Q*vv)[0, 0])
res = {"F_polynomial": str(F)}
w33 = -w11 - w22
mu1, mu2, mu3 = w11 + s/12, w22 + s/12, w33 + s/12
Phi = -mu3*(mu3 - mu1 - mu2)/2 - (mu1 - mu2)**2/2
# corrector block
Hc = Q[5:, 5:]*2
res["corrector_hessian_eigs"] = {str(k): v for k, v in Hc.eigenvals().items()}
res["corrector_hessian_rank"] = Hc.rank()
Fmix = F
res["mixed_block_terms(F - F|w13=0)"] = str(sp.factor(sp.expand(F - F.subs(w13, 0))))
F = sp.expand(F.subs(w13, 0))     # zeta an eigenvector of W+ (automatic on the kernel when R+ <= 0)
grad = [sp.diff(F, c) for c in C]
A, b = sp.linear_eq_to_matrix(grad, C)
sol = list(sp.linsolve((A, b), C))
copt = dict(zip(C, sol[0]))
Fopt = sp.factor(sp.expand(F.subs(copt)))
free = sorted(str(z) for z in sp.Matrix(sol[0]).free_symbols if z in C)
res["free_null_directions"] = free
res["Fopt"] = str(Fopt)
res["Fopt_minus_Phi_w13=0"] = str(sp.simplify(Fopt.subs(w13, 0) - Phi))
res["Fopt_w13_part"] = str(sp.factor(sp.expand(Fopt - Fopt.subs(w13, 0))))
res["Fopt_in_mu"] = str(sp.factor(sp.expand(Fopt - Phi)))
# U(2) locus (step51): w11 = w22 = -lam/2, w33 = lam
lam = sp.symbols('lam')
res["U2_locus_check(step51 (s-24lam)(s+12lam)/288)"] = str(sp.simplify(Fopt.subs({w12: 0, w13: 0, w11: -lam/2, w22: -lam/2}) - (s - 24*lam)*(s + 12*lam)/288))
# kernel locus w33 = -s/12  <=> w22 = s/12 - w11 ; T = trace-free part of R+ on zeta^perp
ker = {w22: s/12 - w11, w13: 0}
T11 = (w11 - w22)/2; T12 = w12
T2 = sp.expand((2*T11**2 + 2*T12**2).subs(ker))
Acoef = -s/12
fam = {c: 0 for c in C}
fam[C[4]] = sp.Rational(7, 4)*Acoef + T11/3      # P1 = v1v1/u  (J1 x)
fam[C[7]] = sp.Rational(7, 4)*Acoef - T11/3      # P2 = v2v2/u  (J2 x)
fam[C[9]] = Acoef/2                              # P3 = v3v3/u  (J3 x = zeta)
fam[C[5]] = 2*T12/3                              # (1/3)(T12 v1v2^T + T21 v2v1^T)/u
Ffam = sp.expand(F.subs(fam).subs(ker))
res["T2_kernel"] = str(sp.factor(T2))
res["F_family_kernel"] = str(sp.factor(Ffam))
res["F_family_plus_T2"] = str(sp.simplify(Ffam + T2))
res["Fopt_kernel"] = str(sp.factor(sp.expand(Fopt.subs(ker))))
res["Fopt_kernel_plus_T2"] = str(sp.simplify(Fopt.subs(ker) + T2))
# family is optimal on kernel? gradient there
gfam = [sp.simplify(g.subs(fam).subs(ker)) for g in grad]
res["family_gradient_on_kernel"] = [str(z) for z in gfam]
# CH calibration: s=-24, w=(2,-4,2): family coefficients
chs = {s: -24, w11: 2, w12: 0}
res["CH_family_coeffs(P1,P2,P3)"] = [str(fam[C[4]].subs(chs).subs(ker)), str(fam[C[7]].subs(chs).subs({w22: s/12 - w11}).subs(chs)), str(fam[C[9]].subs(chs))]
# mixed block + general: express Fopt via R+ entries
res["Fopt_at_W+=0"] = str(sp.factor(Fopt.subs({w11: 0, w22: 0, w12: 0, w13: 0})))
json.dump(res, open(os.path.join(D, "exact_su2minus_analysis.json"), "w"), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != "F_polynomial"}, indent=1))

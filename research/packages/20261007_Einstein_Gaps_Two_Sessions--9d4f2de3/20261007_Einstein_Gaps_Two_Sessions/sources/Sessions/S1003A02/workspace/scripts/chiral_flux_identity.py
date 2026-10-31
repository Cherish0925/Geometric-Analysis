"""Chiral Euler (Hitchin-Thorpe) transgressions for diagonal Bianchi-IX metrics.

g = dt^2 + a^2 s1^2 + b^2 s2^2 + c^2 s3^2,  d s_i = 2 s_j^s_k,  int s123 = 2 pi^2,  W = abc.
Curvature is taken from the independent Cartan module S1003A01/.../perp_cartan_verify.py.
Block norms B_A = tr(W_A^2), B_B = tr(W_B^2) in the convention of verify_euler_flux_identity.py,
for which   W|Ric0|^2/4 = bE' + W(B_A+B_B)/2 + W s^2/48   (Step 26, exact).

We solve for a signature transgression S with  S' = W (B_A - B_B)/2  by a general ansatz
S = sum_{|alpha|<=3} p^alpha * (polynomial in gamma_i of degree <= 3-|alpha|),
p_i = a_i',  gamma_i = (a_j^2+a_k^2-a_i^2)/(a_j a_k), and then define
   bA = bE - S,  bB = bE + S,   so that   W|Ric0|^2/4 = bX' + W B_X + W s^2/48   (X = A, B).
Outputs (data/chiral_flux.json): S, checks on CH (which block is W+), H^4, Euclidean origin,
bolt limits (fibre a -> 0), and collapsed Berger limits.
"""
import itertools, json, sys
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / 'S1003A01' / 'workspace' / 'scripts'))
import perp_cartan_verify as pc  # noqa: E402

a, b, c, a1, b1, c1, a2, b2, c2 = pc.a, pc.b, pc.c, pc.a1, pc.b1, pc.c1, pc.a2, pc.b2, pc.c2
A = [a, b, c]; P = [a1, b1, c1]; W = a*b*c

pairs = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
Rop = sp.Matrix([[pc.R(i, j, k, l) for k, l in pairs] for i, j in pairs])
sq = sp.sqrt(2)/2
LA = sp.zeros(3, 6); LB = sp.zeros(3, 6)
for k in range(3):
    LA[k, k] = sq; LA[k, 3+k] = sq; LB[k, k] = sq; LB[k, 3+k] = -sq
WA = sp.simplify(LA*Rop*LA.T - pc.s*sp.eye(3)/12)
WB = sp.simplify(LB*Rop*LB.T - pc.s*sp.eye(3)/12)
BA = sp.factor(sum(WA[i, j]**2 for i in range(3) for j in range(3)))
BB = sp.factor(sum(WB[i, j]**2 for i in range(3) for j in range(3)))
target = sp.factor(W*(BA - BB)/2)

gam = [sp.factor((A[(i+1) % 3]**2 + A[(i+2) % 3]**2 - A[i]**2)/(A[(i+1) % 3]*A[(i+2) % 3])) for i in range(3)]
G = sp.symbols('g0:3'); Psym = sp.symbols('p0:3')
coeffs = []; terms = []
for deg_p in range(4):
    for alpha in itertools.combinations_with_replacement(range(3), deg_p):
        mp = sp.Mul(*[Psym[i] for i in alpha])
        for dg in range(4 - deg_p):
            for beta in itertools.combinations_with_replacement(range(3), dg):
                mg = sp.Mul(*[G[i] for i in beta])
                z = sp.Symbol(f'z{len(coeffs)}'); coeffs.append(z); terms.append(z*mp*mg)
S_sym = sum(terms)
S = S_sym.subs({**{Psym[i]: P[i] for i in range(3)}, **{G[i]: gam[i] for i in range(3)}})
num = sp.numer(sp.together(pc.Dt(S) - target))
poly = sp.Poly(sp.expand(num), a, b, c, a1, b1, c1, a2, b2, c2)
eqs = poly.coeffs()
sol = sp.solve(eqs, coeffs, dict=True)
if not sol:
    raise SystemExit('no signature transgression in ansatz')
sol = sol[0]
S_sol = sp.factor(sp.expand(S.subs(sol).subs({z: 0 for z in coeffs})))
res = sp.simplify(pc.Dt(S_sol) - target)
print('S =', S_sol); print('residual =', res)

# Euler flux from Step 26
def K3(i, j, k):
    return ((A[j]**2 - A[k]**2)**2 + 2*A[i]**2*(A[j]**2 + A[k]**2) - 3*A[i]**4)/(A[i]**2*A[j]**2*A[k]**2)
y = [P[i]/A[i] for i in range(3)]
bE = sp.factor(W*(y[0]*K3(0, 1, 2) + y[1]*K3(1, 2, 0) + y[2]*K3(2, 0, 1) - y[0]*y[1]*y[2]))
bA = sp.factor(bE - S_sol); bB = sp.factor(bE + S_sol)
chkA = sp.simplify(W*pc.ric0sq/4 - (pc.Dt(bA) + W*BA + W*pc.s**2/48))
chkB = sp.simplify(W*pc.ric0sq/4 - (pc.Dt(bB) + W*BB + W*pc.s**2/48))
print('chiral identity residuals', chkA, chkB)

t = sp.Symbol('t', positive=True)
def on(metric, expr):
    sub = {}
    for X, X1, X2, f in zip(A, P, [a2, b2, c2], metric):
        sub[X] = f; sub[X1] = sp.diff(f, t); sub[X2] = sp.diff(f, t, 2)
    return sp.simplify(expr.subs(sub))

out = {'S': str(S_sol), 'residual': str(res), 'chiral_residuals': [str(chkA), str(chkB)]}
CH = [sp.sinh(t)*sp.cosh(t), sp.sinh(t), sp.sinh(t)]      # fibre slot a
H4 = [sp.sinh(t)]*3                                         # Ric=-3 normalization (used only for shape)
E4 = [t, t, t]
for name, met in [('CH', CH), ('H4', H4), ('Euclid', E4)]:
    out[name] = {k: str(sp.simplify(sp.expand_trig(on(met, v)))) for k, v in
                 [('BA', BA), ('BB', BB), ('S', S_sol), ('bE', bE), ('bA', bA), ('bB', bB)]}
# bolt: fibre a = t - ..., b = c = beta (leading); S at t->0 for a general regular bolt jet
beta, e1, e2 = sp.symbols('beta e1 e2')
bolt = [t + e1*t**3, beta + e2*t**2, beta + e2*t**2]
out['bolt_limit'] = {k: str(sp.limit(on(bolt, v), t, 0)) for k, v in [('S', S_sol), ('bE', bE)]}
# triaxial bolt jet: b,c = beta +/- d t^2 (regular bolts force b=c at t=0)
dd = sp.Symbol('dd')
bolt3 = [t + e1*t**3, beta + (e2 + dd)*t**2, beta + (e2 - dd)*t**2]
out['bolt3_limit'] = {k: str(sp.limit(on(bolt3, v), t, 0)) for k, v in [('S', S_sol), ('bE', bE)]}
# collapsed Berger orbit: a = eps*Bt (fibre), b = c = R, with jets (R' = U, a'/a = V/R)
eps, R, U, V = sp.symbols('eps R U V', positive=True)
sub = {a: eps, b: R, c: R, a1: eps*V/R, b1: U, c1: U}
out['berger'] = {k: str(sp.factor(sp.simplify(v.subs(sub)))) for k, v in [('S', S_sol), ('bE', bE)]}
out['berger_eps0'] = {k: str(sp.limit(sp.simplify(v.subs(sub)), eps, 0)) for k, v in [('S', S_sol), ('bE', bE)]}
print(json.dumps(out, indent=1))
(HERE.parent / 'data' / 'chiral_flux.json').write_text(json.dumps(out, indent=1))

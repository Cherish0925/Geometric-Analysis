"""Step 28: exact almost-Kahler structure of the canonical conformal metric of a diagonal cell.

Claim checked here.  If g = dt^2 + sum a_i^2 s_i^2 (d s_i = 2 s_j^s_k, slots (f,g,h)) and
omega_f = d(phi s_f) is the canonical closed self-dual form, then ghat = u^2 g with
u^2 = phi/(a_g a_h) is again diagonal Bianchi IX, ghat = dT^2 + sum A_i^2 s_i^2 with
dT = u dt, A_i = u a_i, and |omega_f|_ghat is constant iff
        A_f = (A_g A_h)_T / 2         (AK constraint, phi = A_g A_h / 2).
For such metrics we compute, symbolically, in terms of the two free slots A_g, A_h:
  * the self-dual connection coefficients v_i = A_i' - gamma_i and the curvature
    R+_ii = -v_i'/(2A_i) + (-v_i - v_j v_k/2)/(A_j A_k)  (normalization fixed by S^4 and CH);
  * the AK conformal scalar curvature kappa = 6 W+_ff and the Nijenhuis density
    kappa - s = 6|a|^2 (Apostolov-Armstrong-Draghici (10)), as a function of v_g, v_h;
  * the W3 eigenvalue lambda = (W+_gg - W+_hh)/2 and its first-order (Riccati) relation to
    the Nijenhuis variables (AAD (13)).
Output: workspace/data/step28/ak_hatted_structure.json
"""
import json
from pathlib import Path
import sympy as sp

T = sp.symbols('T', real=True)
Ag, Ah = sp.Function('A_g')(T), sp.Function('A_h')(T)
Af = sp.diff(Ag*Ah, T)/2
A = [Af, Ag, Ah]
d = lambda e: sp.diff(e, T)

def gam(i):
    j, k = (i+1) % 3, (i+2) % 3
    return (A[j]**2 + A[k]**2 - A[i]**2)/(A[j]*A[k])

v = [sp.simplify(d(A[i]) - gam(i)) for i in range(3)]
Rp = []
for i in range(3):
    j, k = (i+1) % 3, (i+2) % 3
    Rp.append(-d(v[i])/(2*A[i]) + (-v[i] - v[j]*v[k]/2)/(A[j]*A[k]))
# scalar curvature from the diagonal Ricci formulas
y = [d(a)/a for a in A]; S = sum(y); W = A[0]*A[1]*A[2]
def Porb(i):
    j, k = (i+1) % 3, (i+2) % 3
    return 2*(A[i]**4 - (A[j]**2 - A[k]**2)**2)/W**2
R00 = -sum(d(yi) + yi**2 for yi in y)
Rii = [-d(y[i]) - S*y[i] + Porb(i) for i in range(3)]
s = R00 + sum(Rii)
trace_res = sp.simplify(sum(Rp) - s/4)
Wff = Rp[0] - s/12; Wgg = Rp[1] - s/12; Whh = Rp[2] - s/12
kappa = 6*Wff
nij = sp.simplify(kappa - s)
# candidate closed forms in the Nijenhuis variables
vg, vh = sp.symbols('v_g v_h')
lam = sp.simplify((Wgg - Whh)/2)
out = dict(
    v_f=str(sp.factor(v[0])), v_g=str(sp.factor(v[1])), v_h=str(sp.factor(v[2])),
    v_g_plus_v_h=str(sp.factor(sp.simplify(v[1] + v[2]))),
    v_g_times_Ag_plus_v_h_times_Ah=str(sp.factor(sp.simplify(v[1]*Ag + v[2]*Ah))),
    trace_residual=str(trace_res),
    kappa_minus_s=str(sp.factor(nij)),
)
# test kappa - s against quadratic forms in v_g, v_h
cands = {
    '(3/2)(v_g^2/A_g^2 + v_h^2/A_h^2)... generic fit': None,
}
c1, c2, c3 = sp.symbols('c1 c2 c3')
ansatz = (c1*v[1]**2/(Af*Ag)**0 + 0)  # placeholder
# direct fit: kappa-s = alpha*(v_g^2 + v_h^2)/(A_g A_h) ?  test numerically on random jets
import random
def num(expr, vals):
    return complex(expr.subs(vals)).real
jet_syms = {}
fG = sp.Function('A_g'); fH = sp.Function('A_h')
def random_jet():
    vals = {}
    for F in (fG, fH):
        cs = [random.uniform(0.5, 2.0)] + [random.uniform(-1, 1) for _ in range(4)]
        for n, c in enumerate(cs):
            vals[sp.Derivative(F(T), (T, n)) if n else F(T)] = c
    return vals
def subsjet(expr, vals):
    e = expr
    for n in (4, 3, 2, 1):
        for F in (fG, fH):
            e = e.subs(sp.Derivative(F(T), (T, n)), vals[sp.Derivative(F(T), (T, n))])
    for F in (fG, fH):
        e = e.subs(F(T), vals[F(T)])
    return float(sp.N(e))
rows = []
basis = {
    'vg2/(Af Ah)': v[1]**2/(Af*Ah), 'vh2/(Af Ag)': v[2]**2/(Af*Ag),
    'vg2/Ah2': v[1]**2/Ah**2, 'vh2/Ag2': v[2]**2/Ag**2,
    'vg vh/(Ag Ah)': v[1]*v[2]/(Ag*Ah),
    'vg2/Af2': v[1]**2/Af**2, 'vh2/Af2': v[2]**2/Af**2,
    'vg2/Ag2': v[1]**2/Ag**2, 'vh2/Ah2': v[2]**2/Ah**2,
}
random.seed(1)
import numpy as np
M = []; rhs = []
for _ in range(14):
    vals = random_jet()
    M.append([subsjet(bexpr, vals) for bexpr in basis.values()])
    rhs.append(subsjet(nij, vals))
M = np.array(M); rhs = np.array(rhs)
coef, res, rk, sv = np.linalg.lstsq(M, rhs, rcond=None)
out['kappa_minus_s_fit'] = dict(zip(basis.keys(), [float(c) for c in coef]))
out['kappa_minus_s_fit_residual'] = float(np.max(np.abs(M @ coef - rhs)))
out['fit_rank'] = int(rk)
Path(__file__).resolve().parents[1].joinpath('data', 'step28').mkdir(parents=True, exist_ok=True)
out['lambda'] = str(sp.simplify(lam))[:2000]
p = Path(__file__).resolve().parents[1]/'data'/'step28'/'ak_hatted_structure.json'
p.write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1)[:6000])

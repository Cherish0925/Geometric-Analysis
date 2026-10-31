"""Step 27: exact flux laws for diagonal Bianchi-IX cells, anchored at a smooth bolt.

Metric g = dt^2 + a_f^2 s_f^2 + a_g^2 s_g^2 + a_h^2 s_h^2, d s_i = 2 s_j ^ s_k,
int s_fgh = 2 pi^2, W = a_f a_g a_h.  The h circle collapses at the bolt; f is
the complex-hyperbolic fibre at infinity.  Orthonormal Ricci:
    Ric_00 = -sum (y_i' + y_i^2),   Ric_ii = -y_i' - S y_i + P_i,
    P_i = 2 [a_i^4 - (a_j^2-a_k^2)^2] / W^2,   y_i = a_i'/a_i,  S = sum y_i.
Trace-free channels (no scalar normalization assumed):
    C = Ric0_00,  E = Ric_ff - (Ric_gg+Ric_hh)/2,  D = Ric_gg - Ric_hh,
    beta = log(a_f/sqrt(a_g a_h)),  q = log(a_g/a_h).
Checks (all symbolic, zero residual required):
  1. |Ric0|^2 = 4C^2/3 + 2E^2/3 + D^2/2, so P/(8 pi^2) = int W (C^2/3+E^2/6+D^2/8) dt.
  2. (W q')' = W (Pi_q - D),        Pi_q = P_g - P_h.
  3. (W beta')' = W (Pi_b - E),     Pi_b = P_f - (P_g+P_h)/2.
  4. Coupled radial Bianchi: (W^{4/3} C)' = W^{4/3} [ (2/3) beta' E + (1/2) q' D + s'/4 ].
  5. Smooth bolt (a_f=b+f2 t^2+f4 t^4, a_g=b+g2 t^2+g4 t^4, a_h=t+h3 t^3+h5 t^5):
     limits of W q', W beta', W^{4/3} C, W Pi_q, W Pi_b.
  6. Exact CH (a_f=sinh r cosh r, a_g=a_h=sinh r): W beta' = sinh^4 r, W q' = 0.
Output: Sessions/S1003A01/workspace/data/step27/flux_laws_symbolic.json
"""
import json
from pathlib import Path
import sympy as sp

t = sp.symbols('t', positive=True)
af, ag, ah = [sp.Function(n)(t) for n in ('af', 'ag', 'ah')]
A = [af, ag, ah]
W = af*ag*ah
y = [sp.diff(a, t)/a for a in A]
S = sum(y)
def Porb(i):
    j, k = [(1, 2), (2, 0), (0, 1)][i]
    return 2*(A[i]**4 - (A[j]**2 - A[k]**2)**2)/W**2
P = [Porb(i) for i in range(3)]
R00 = -sum(sp.diff(yi, t) + yi**2 for yi in y)
Rii = [-sp.diff(y[i], t) - S*y[i] + P[i] for i in range(3)]
s = R00 + sum(Rii)
C = R00 - s/4
E = Rii[0] - (Rii[1] + Rii[2])/2
D = Rii[1] - Rii[2]
beta = sp.log(af) - (sp.log(ag) + sp.log(ah))/2
q = sp.log(ag) - sp.log(ah)
Piq = P[1] - P[2]
Pib = P[0] - (P[1] + P[2])/2

res = {}
ric0sq = (R00 - s/4)**2 + sum((r - s/4)**2 for r in Rii)
res['decomposition'] = sp.simplify(sp.expand(ric0sq - (sp.Rational(4, 3)*C**2 + sp.Rational(2, 3)*E**2 + D**2/2)))
res['q_equation'] = sp.simplify(sp.diff(W*sp.diff(q, t), t) - W*(Piq - D))
res['beta_equation'] = sp.simplify(sp.diff(W*sp.diff(beta, t), t) - W*(Pib - E))
lhs = sp.diff(W**sp.Rational(4, 3)*C, t)
rhs = W**sp.Rational(4, 3)*(sp.Rational(2, 3)*sp.diff(beta, t)*E + sp.diff(q, t)*D/2 + sp.diff(s, t)/4)
res['coupled_bianchi'] = sp.simplify(sp.expand((lhs - rhs)/W**sp.Rational(1, 3)))
out = {k: str(v) for k, v in res.items()}

# Smooth-bolt asymptotics.
b, f2, f4, g2, g4, h3, h5 = sp.symbols('b f2 f4 g2 g4 h3 h5', real=True)
ser = {af: b + f2*t**2 + f4*t**4, ag: b + g2*t**2 + g4*t**4, ah: t + h3*t**3 + h5*t**5}
def bolt(expr, n=3):
    e = expr.subs({k: v for k, v in ser.items()}).doit()
    return sp.simplify(sp.series(sp.simplify(e), t, 0, n).removeO())
bol = {}
bol['W_qprime'] = bolt(W*sp.diff(q, t))
bol['W_betaprime'] = bolt(W*sp.diff(beta, t))
bol['W_Piq'] = bolt(W*Piq, 2)
bol['W_Pib'] = bolt(W*Pib, 2)
bol['C_at_bolt'] = bolt(C, 1)
bol['D_at_bolt'] = bolt(D, 1)
bol['E_at_bolt'] = bolt(E, 1)
out['bolt_general'] = {k: str(v) for k, v in bol.items()}
# weight-four regularity f2=g2 removes the singular parts of C,D,E
bol2 = {k: str(sp.simplify(sp.sympify(v).subs(g2, f2))) for k, v in bol.items()}
out['bolt_weight4_f2_eq_g2'] = bol2

# Exact CH end.
r = sp.symbols('r', positive=True)
ch = {af: sp.sinh(r)*sp.cosh(r), ag: sp.sinh(r), ah: sp.sinh(r)}
def chv(expr):
    e = expr.subs(t, r)
    e = e.subs({af.subs(t, r): ch[af], ag.subs(t, r): ch[ag], ah.subs(t, r): ch[ah]}).doit()
    return sp.simplify(sp.expand_trig(e))
out['CH'] = {'W_betaprime': str(chv(W*sp.diff(beta, t))), 'W_qprime': str(chv(W*sp.diff(q, t))),
             'Ricci_trace': str(chv(s)), 'C': str(chv(C)), 'E': str(chv(E)), 'D': str(chv(D)),
             'W_Pib': str(chv(W*Pib)), 'volume_density_W': str(chv(W))}
print(json.dumps(out, indent=1))
od = Path(__file__).resolve().parents[1]/'data'/'step27'
od.mkdir(parents=True, exist_ok=True)
(od/'flux_laws_symbolic.json').write_text(json.dumps(out, indent=1) + '\n')

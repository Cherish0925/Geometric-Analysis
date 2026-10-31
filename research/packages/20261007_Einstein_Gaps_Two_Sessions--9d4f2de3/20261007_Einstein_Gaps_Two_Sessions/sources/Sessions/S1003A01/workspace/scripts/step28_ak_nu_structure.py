"""Step 28b: express W3 (lambda) and the J-anti-invariant Ricci of the canonical AK metric
through the Nijenhuis scalar nu.

Hatted diagonal AK metric: ghat = dT^2 + A_f^2 s_f^2 + A_g^2 s_g^2 + A_h^2 s_h^2,
A_g = sqrt(Pm) e^{q/2}, A_h = sqrt(Pm) e^{-q/2}, A_f = Pm'/2   (Pm = A_g A_h = 2 phi).
Step 28a found  kappa - s = 6 nu^2  with
        nu = -(1/2) (q' + 4 sinh(q)/A_f).
Here we substitute q' = -2 nu - 4 sinh(q)/A_f and simplify:
  lambda = (W+_gg - W+_hh)/2,   Dhat = Ric_gg - Ric_hh,   Ehat = Ric_ff - (Ric_gg+Ric_hh)/2,
  Chat = Ric_00 - s/4, and Ric_00 - Ric_ff (the other J-anti-invariant combination).
"""
import json
from pathlib import Path
import sympy as sp

T = sp.symbols('T', real=True)
Pm = sp.Function('P')(T); q = sp.Function('q')(T)
d = lambda e: sp.diff(e, T)
Ag = sp.sqrt(Pm)*sp.exp(q/2); Ah = sp.sqrt(Pm)*sp.exp(-q/2); Af = d(Pm)/2
A = [Af, Ag, Ah]
def gam(i):
    j, k = (i+1) % 3, (i+2) % 3
    return (A[j]**2 + A[k]**2 - A[i]**2)/(A[j]*A[k])
v = [d(A[i]) - gam(i) for i in range(3)]
Rp = []
for i in range(3):
    j, k = (i+1) % 3, (i+2) % 3
    Rp.append(-d(v[i])/(2*A[i]) + (-v[i] - v[j]*v[k]/2)/(A[j]*A[k]))
y = [d(a)/a for a in A]; S = sum(y); W = A[0]*A[1]*A[2]
def Porb(i):
    j, k = (i+1) % 3, (i+2) % 3
    return 2*(A[i]**4 - (A[j]**2 - A[k]**2)**2)/W**2
R00 = -sum(d(yi) + yi**2 for yi in y)
Rii = [-d(y[i]) - S*y[i] + Porb(i) for i in range(3)]
s = R00 + sum(Rii)
lam = (Rp[1] - Rp[2])/2
Dh = Rii[1] - Rii[2]; Eh = Rii[0] - (Rii[1] + Rii[2])/2; Ch = R00 - s/4; Xh = R00 - Rii[0]
kap = 6*(Rp[0] - s/12)

nu, nup, nupp = sp.symbols('nu nu_p nu_pp')
Q0, Q1, Q2, Q3 = sp.symbols('q0 q1 q2 q3')
p0, p1, p2, p3, p4 = sp.symbols('p0 p1 p2 p3 p4')
def to_jets(e):
    e = e.subs({sp.Derivative(q, (T, 3)): Q3, sp.Derivative(q, (T, 2)): Q2, sp.Derivative(q, T): Q1})
    e = e.subs({sp.Derivative(Pm, (T, 4)): p4, sp.Derivative(Pm, (T, 3)): p3, sp.Derivative(Pm, (T, 2)): p2,
                sp.Derivative(Pm, T): p1})
    return e.subs({q: Q0, Pm: p0})
# nu as function of jets and its derivatives
nu_expr = -(sp.Symbol('dummy')*0 + d(q) + 4*sp.sinh(q)/Af)/2
nu_j = to_jets(nu_expr); nup_j = to_jets(d(nu_expr)); nupp_j = to_jets(d(d(nu_expr)))
# solve for q1,q2,q3 in terms of nu, nu', nu''
sol1 = sp.solve(sp.Eq(nu_j, nu), Q1)[0]
sol2 = sp.solve(sp.Eq(nup_j.subs(Q1, sol1), nup), Q2)[0]
sol3 = sp.solve(sp.Eq(nupp_j.subs({Q1: sol1, Q2: sol2}), nupp), Q3)[0]
def in_nu(e):
    e = to_jets(e)
    e = e.subs(Q3, sol3).subs(Q2, sol2).subs(Q1, sol1)
    return sp.simplify(sp.expand(sp.simplify(e.rewrite(sp.exp))))
out = {}
for name, e in [('kappa_minus_s', kap - s), ('lambda', lam), ('Dhat', Dh), ('Ric00_minus_Ricff', Xh),
                ('Ehat', Eh), ('Chat', Ch), ('shat', s)]:
    r = in_nu(e)
    out[name] = str(sp.collect(sp.expand(r), [nupp, nup, nu]))
    print(name, ':', out[name][:1500], flush=True)
p = Path(__file__).resolve().parents[1]/'data'/'step28'/'ak_nu_structure.json'
p.write_text(json.dumps(out, indent=1) + '\n')

"""Step 8: exact algebra for ASD Yamabe competitors and the Q-regions.
Units: sigma=S/(8 pi^2 A), w=W_+/(8 pi^2 A), h=Q/A, T_+=A(1-h).
Chern-Weil (conventions ledger): P = 4W_+ + S/12 - 8pi^2 T_+.
"""
import sympy as sp
s, w, h, iota = sp.symbols('sigma w h iota', real=True)
P = 4*w + s/12 + (h-1)
R = P + s/4
J = sp.simplify(4*P/R)
E_asd = sp.simplify(J.subs(w, 0))
print('J =', sp.factor(J))
print('E_ASD (const s) =', sp.factor(E_asd))
print('4 - E_ASD =', sp.factor(4-E_asd))
print('E_ASD - 1 =', sp.factor(E_asd-1))
print('dE/dsigma =', sp.factor(sp.diff(E_asd, s)))
print('dJ/dw =', sp.factor(sp.diff(J, w)), ' dJ/dsigma =', sp.factor(sp.diff(J, s)))
E9 = sp.factor(E_asd.subs(s, 9))
print('E_ASD at sigma=9:', E9)
print('recovery - E9 =', sp.factor(4*h/(1+h) - E9))
# general metric in an ASD class: E = 4 - 3*iota/(sigma+3h-3), iota=(int s)^2/(8pi^2 A V) <= sigma_Y <= sigma
Eg = 4 - 3*iota/(s + 3*h - 3)
print('E (ASD class, general) =', Eg, '; at iota=sigma:', sp.factor(Eg.subs(iota, s) - E_asd))

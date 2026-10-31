"""Symbolic check of the neutral-mode identity (W q')' = W (V - E) (S1003A01 Step 15).

Uses the Cartan-derived Ricci tensor of perp_cartan_verify.py (slots a, b, c = a1, a2, a3;
d sigma_i = 2 sigma_j ^ sigma_k), with q = log(b/a), W = abc,
V = 4 (b^2 - a^2)(a^2 + b^2 - c^2)/W^2, E = Ric_22 - Ric_11 (orthonormal).
"""
import contextlib, io, sympy as sp
with contextlib.redirect_stdout(io.StringIO()):
    import perp_cartan_verify as pc
a, b, c = pc.a, pc.b, pc.c
W = a*b*c
q = sp.log(b) - sp.log(a)
V = 4*(b**2 - a**2)*(a**2 + b**2 - c**2)/W**2
E = pc.Ric[2] - pc.Ric[1]
res = sp.simplify(sp.factor(pc.Dt(W*pc.Dt(q)) - W*(V - E)))
print('neutral identity residual:', res)
# the companion neutral mode log(c/b) (not neutral at CH, recorded for completeness)
q2 = sp.log(c) - sp.log(b); V2 = 4*(c**2 - b**2)*(b**2 + c**2 - a**2)/W**2
res2 = sp.simplify(sp.factor(pc.Dt(W*pc.Dt(q2)) - W*(V2 - (pc.Ric[3] - pc.Ric[2]))))
print('second-pair residual:', res2)
if res != 0 or res2 != 0: raise SystemExit('identity failed')

"""Is the flux Y of a U(2) Kaehler slice the Ricci-form flux?
K = dr^2/F + r^2(s1^2+s2^2) + r^2 F s3^2 (Kaehler, Ric eigenvalues l1 on {e0,e3}, l2 on {e1,e2}).
Ricci form rho = l1 e0^e3 + l2 e1^e2 = d(A s3) with A = l2 r^2/2 (since d s3 = 2 s1^s2).
Compare Y = c' - 2 + z^2 = 2F + rF'/2 - 2 with A.
"""
import sympy as sp
import cell_ricci as cr

ex = cr.ricci_exprs()
sub = {cr.ws: 0, cr.w1: 0, cr.w2: 0, cr.ps: 0, cr.p1: 0, cr.p2: 0}
l = [sp.simplify(e.subs(sub)) for e in ex]
print('Ric_00, Ric_11, Ric_22, Ric_33 =', l)
r, F, F1 = cr.r, cr.Fs, cr.F1
A = sp.simplify(l[1] * r**2 / 2)
Y = 2 * F + r * F1 / 2 - 2
print('A =', A, '  Y =', Y, '  A/Y =', sp.simplify(A / Y))

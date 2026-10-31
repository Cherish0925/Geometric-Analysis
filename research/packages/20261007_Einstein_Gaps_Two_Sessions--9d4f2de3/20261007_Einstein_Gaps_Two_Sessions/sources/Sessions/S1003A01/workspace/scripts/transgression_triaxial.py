"""Triaxial structure of the slice transgression.
Slice data (scale normalized ell=1):  a = e^w, b = e^-w, c = z,
  a' = e^w (m + n), b' = e^-w (m - n), c' = gamma,
where m = ell'/ell * ell (common expansion), n = ell w' (anisotropy rate).
The almost-Kaehler closure d(ab s1^s2 + c dt^s3)=0 reads m = z; delta := m - z.
Prints Q = T/(8 pi^2) completed in gamma, and the gamma-minimized remainder.
"""
import sympy as sp
import transgression_values as tv

w, n, z, d, ga = sp.symbols('w n z delta gamma', real=True)
G = tv.load()[1]
x, y, zz, a1, b1, c1 = [tv.loc[k] for k in ('x', 'y', 'z', 'a1', 'b1', 'c1')]
m = z + d
Q = sp.expand(sp.simplify((G.subs({x: sp.exp(w), y: sp.exp(-w), zz: z,
                                    a1: sp.exp(w) * (m + n), b1: sp.exp(-w) * (m - n), c1: ga}) + 32) / 4))
Q = sp.simplify(Q.rewrite(sp.cosh))
coef2 = sp.simplify(sp.diff(Q, ga, 2) / 2)
gstar = sp.simplify(sp.solve(sp.diff(Q, ga), ga)[0])
Qs = sp.simplify(Q.subs(ga, gstar))
print('coefficient of gamma^2:', coef2)
print('gamma* =', sp.simplify(gstar.rewrite(sp.cosh)))
Qs_c = sp.simplify(sp.expand(Qs.rewrite(sp.exp)))
print('Q* (min over gamma) =', sp.factor(Qs_c))
# check biaxial reduction
print('biaxial w=n=0:', sp.factor(sp.simplify(Qs.subs({w: 0, n: 0}))))
# almost-Kaehler slices delta=0
print('delta=0:', sp.factor(sp.simplify(Qs_c.subs(d, 0))))
with open('../data/transgression/triaxial_Qstar.txt', 'w') as fh:
    fh.write('gamma* = ' + str(gstar) + '\nQ* = ' + str(sp.factor(Qs_c)) + '\n')

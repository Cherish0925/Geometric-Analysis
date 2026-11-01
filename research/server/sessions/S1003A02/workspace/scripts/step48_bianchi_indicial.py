#!/usr/bin/env python3
"""Step 48: indicial roots of diagonal Bianchi-IX Einstein perturbations of CH^2 (Ric=-6g).

g = dr^2 + A^2 s1^2 + B^2 s2^2 + C^2 s3^2 (unit round S^3 = sum s_i^2).  Orthonormal Ricci:
 R00 = -(A''/A+B''/B+C''/C)
 R11 = -A''/A - (A'/A)(B'/B+C'/C) + 2[A^4-(B^2-C^2)^2]/(A^2B^2C^2)   (cyclic)
(checked: flat A=B=C=r gives 0; CH^2 A=B=sinh r, C=sinh r cosh r gives -6.)
Perturb A=sinh r e^{eps a}, B=sinh r e^{eps b}, C=sinh r cosh r e^{eps c}; linearize E=Ric+6;
asymptotic exponents (a,b,c) ~ v e^{-nu r}.  |h|_g = O(e^{-nu r}); volume density ~ e^{4r}/16.
Output: workspace/data/step48_bianchi_indicial.json
"""
import json, os
import sympy as sp

r, eps, nu = sp.symbols('r epsilon nu')
fa, fb, fc = [sp.Function(n)(r) for n in 'abc']
A = sp.sinh(r)*sp.exp(eps*fa); B = sp.sinh(r)*sp.exp(eps*fb); C = sp.sinh(r)*sp.cosh(r)*sp.exp(eps*fc)
d = lambda F: sp.diff(F, r)

def Rii(X, Y, Z):
    return -d(d(X))/X - d(X)/X*(d(Y)/Y + d(Z)/Z) + 2*(X**4 - (Y**2 - Z**2)**2)/(X**2*Y**2*Z**2)

E = {'00': -(d(d(A))/A + d(d(B))/B + d(d(C))/C) + 6,
     '11': Rii(A, B, C) + 6, '22': Rii(B, C, A) + 6, '33': Rii(C, A, B) + 6}
zero = {k: sp.simplify(v.subs(eps, 0)) for k, v in E.items()}
lin = {k: sp.expand(sp.diff(v, eps).subs(eps, 0)) for k, v in E.items()}
va, vb, vc = sp.symbols('va vb vc')
rep = {}
for f, v in [(fa, va), (fb, vb), (fc, vc)]:
    rep[sp.Derivative(f, (r, 2))] = v*nu**2*sp.exp(-nu*r)
    rep[sp.Derivative(f, r)] = -v*nu*sp.exp(-nu*r)
    rep[f] = v*sp.exp(-nu*r)
rows = []
for k in ['00', '11', '22', '33']:
    e = lin[k].subs(rep)
    e = sp.expand(e*sp.exp(nu*r))
    e = e.rewrite(sp.exp)
    lim = sp.limit(sp.simplify(e), r, sp.oo)
    rows.append([sp.simplify(sp.diff(lim, v)) for v in (va, vb, vc)])
M = sp.Matrix(rows)
Md = M[1:, :]
detd = sp.factor(Md.det())
tri = sp.factor((Md*sp.Matrix([1, -1, 0]))[0])
# U(2)-invariant squashing a=b: restrict to (a,c) with a=b
Mu = sp.Matrix([[Md[0, 0] + Md[0, 1], Md[0, 2]], [Md[2, 0] + Md[2, 1], Md[2, 2]]])
detu = sp.factor(Mu.det())
out = {'background_E': {k: str(v) for k, v in zero.items()},
       'indicial_rows_00_11_22_33': [[str(x) for x in row] for row in rows],
       'det_dynamical': str(detd), 'roots_dynamical': [str(x) for x in sp.solve(detd, nu)],
       'triaxial_a_eq_minus_b': str(tri), 'triaxial_roots': [str(x) for x in sp.solve(tri, nu)],
       'u2_squash_det': str(detu), 'u2_squash_roots': [str(x) for x in sp.solve(detu, nu)],
       'volume_growth_exponent': 4}
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step48_bianchi_indicial.json')
with open(p, 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))

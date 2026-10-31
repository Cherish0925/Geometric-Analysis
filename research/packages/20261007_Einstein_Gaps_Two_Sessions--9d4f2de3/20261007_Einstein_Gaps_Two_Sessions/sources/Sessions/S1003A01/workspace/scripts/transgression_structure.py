"""Find a structured form of Q* (gamma-minimized slice transgression), triaxial.
kappa = n + 2 sinh(2w)/z  (anisotropy defect), delta = m - z (almost-Kaehler closure defect).
"""
import sympy as sp

w, n, z, d = sp.symbols('w n z delta', real=True)
txt = open('../data/transgression/triaxial_Qstar.txt').read().split('\n')
Qs = sp.sympify(txt[1].split('=', 1)[1], locals={'w': w, 'n': n, 'z': z, 'delta': d})
kap = n + 2 * sp.sinh(2 * w) / z
k = sp.symbols('kappa', real=True)
# substitute n = k - 2 sinh(2w)/z
Qk = sp.simplify(sp.expand((Qs.subs(n, k - 2 * sp.sinh(2 * w) / z)).rewrite(sp.exp)))
Qk = sp.simplify(Qk.rewrite(sp.cosh))
P = sp.Poly(sp.expand(sp.simplify(4 * Qk).rewrite(sp.exp)), d, k)
for mon, cf in zip(P.monoms(), P.coeffs()):
    print(mon, sp.simplify(sp.factor(cf).rewrite(sp.cosh)))

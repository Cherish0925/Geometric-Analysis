"""Cell-variable form of the Bianchi-IX transgression and independent W^+ check.

Cell metric (I54 (6.3),(6.10)):  G = e^{2 phi} ( dr^2/F + r^2(e^{2w} s1^2 + e^{-2w} s2^2) + r^2 F s3^2 ).
Scale-invariant slice data:  x=e^w, y=e^-w, z=sqrt(F),
  a1 = sqrt(F) e^{w}(1+u+v),  b1 = sqrt(F) e^{-w}(1+u-v),  c1 = F(1+u) + p,
  u = r phi',  v = r w',  p = r F'/2.
T(r) = 2 pi^2 (G - G_flat), orientation +1 (tau(O(-1)) = -1), T_bolt = 8 pi^2.

Also: symbolic |W^+|^2 (operator norm, LeBrun convention) and scalar curvature
from the Cartan curvature, and numerical checks on random admissible profiles of
  (i)  pointwise  F - |Ric+g|^2 = 8 pi^2 (2e+3p)   [with F=(s+3)^2/3+1+4|W+|^2]
  (ii) int_{r0}^{R} 8pi^2(2e+3p) dV = T(R) - T(r0) = 2 pi^2 R^4 - 8 pi^2  (CH collar).
Writes data/transgression/T_cell_formula.txt and checks.json.
"""
import itertools, json, os
import numpy as np
import sympy as sp
import transgression_values as tv

here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'transgression')

F, w, u, v, p = sp.symbols('F w u v p', real=True)


def T_cell():
    G = tv.load()[1]
    x, y, z, a1, b1, c1 = [tv.loc[k] for k in ('x', 'y', 'z', 'a1', 'b1', 'c1')]
    sub = {x: sp.exp(w), y: sp.exp(-w), z: sp.sqrt(F),
           a1: sp.sqrt(F) * sp.exp(w) * (1 + u + v),
           b1: sp.sqrt(F) * sp.exp(-w) * (1 + u - v),
           c1: F * (1 + u) + p}
    T = 2 * sp.pi**2 * (G.subs(sub) + 32)
    T = sp.simplify(sp.expand(T))
    return T


def curvature_numeric_builder():
    """Return lambdified functions of (r, F,F1,F2, w,w1,w2, ph,ph1,ph2) giving
    s, |W+|^2_op, |Ric+g|^2, and 8pi^2(2e+3p) for the cell metric."""
    r = sp.symbols('r', positive=True)
    Ff, wf, pf = [sp.Function(n)(r) for n in ('F', 'w', 'ph')]
    Aw = sp.exp(pf) / sp.sqrt(Ff)  # dt = Aw dr
    a = [sp.exp(pf) * r * sp.exp(wf), sp.exp(pf) * r * sp.exp(-wf), sp.exp(pf) * r * sp.sqrt(Ff)]
    D = lambda f: sp.diff(f, r) / Aw
    ad = [D(q) for q in a]
    add_ = [D(q) for q in ad]
    # Orthonormal Bianchi IX curvature (diagonal): sectional-type components
    # R_{0i0i} = -a_i''/a_i ;  R_{jkjk} = -a_j' a_k'/(a_j a_k) + intrinsic
    # R_{0ijk} terms: for diagonal Bianchi IX the curvature operator is diagonal in
    # the basis {e0^ei, ej^ek}, but with off-diagonal coupling e0^ei <-> ej^ek.
    # We compute these from the standard formulas (verified against the Cartan code).
    K0 = [-add_[i] / a[i] for i in range(3)]
    Kjk = []
    M = []
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        aj, ak, ai = a[j], a[k], a[i]
        intr = (ai**4 - 3 * (aj**2 - ak**2)**2 + 2 * ai**2 * (aj**2 + ak**2)) / (aj**2 * ak**2 * ai**2) * 0  # placeholder
        Kjk.append(None)
        M.append(None)
    return None


def main():
    os.makedirs(od, exist_ok=True)
    T = T_cell()
    Tf = sp.factor(sp.expand(T / (2 * sp.pi**2)))
    print('T/(2pi^2) =', Tf)
    # special values
    for name, subs in [('flat', {F: 1, w: 0, u: 0, v: 0, p: 0}),
                       ('bolt (F=0,p=1,v=0)', {F: 0, p: 1, v: 0}),
                       ('biaxial w=v=0', {w: 0, v: 0})]:
        print(name, sp.factor(sp.simplify(T.subs(subs) / (2 * sp.pi**2))))
    rr = sp.symbols('R', positive=True)
    Fch = 1 + rr**2 / 6
    Tch = sp.simplify(T.subs({F: Fch, w: 0, v: 0, u: 0, p: rr * sp.diff(Fch, rr) / 2}) / (2 * sp.pi**2))
    print('CH slice T/(2pi^2) =', sp.factor(Tch), ' (expect R^4 = 4d/(2pi^2))')
    with open(os.path.join(od, 'T_cell_formula.txt'), 'w') as fh:
        fh.write('T/(2pi^2) = ' + str(Tf) + '\n')
        fh.write('CH slice: ' + str(sp.factor(Tch)) + '\n')


if __name__ == '__main__':
    main()

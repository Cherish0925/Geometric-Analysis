"""Exact boundary transgression of the Burns tail (first-order blow-up response).

Setting.  Cartesian coordinates x on R^4 = C^2, z1=x1+i x2, z2=x3+i x4, standard complex structure
J(x1,x2,x3,x4)=(-x2,x1,-x4,x3), Kaehler form omega=dx1^dx2+dx3^dx4 (self-dual for dx1234).
The Burns metric with Kaehler potential |z|^2 + x0 log|z|^2 is EXACTLY
      B = delta + x0 * h,   h_ij = (delta_ij - x_i x_j/t^2 - (Jx)_i (Jx)_j/t^2)/t^2 ,
i.e. dt^2 + (t^2+x0)(s1^2+s2^2) + t^2 s3^2 with t the geodesic radius (session profile a1=a2=sqrt(t^2+x0), a3=t).

Checks performed (all exact, sympy):
  (a) sign convention: linearized curvature of the normal-coordinate jet of a space of constant
      curvature K gives R_1212 = K;
  (b) the Burns tail is linearly ASD and scalar-flat: P+ R^lin(h) P+ = 0 pointwise on t>0
      (consistent with W+(B)=s(B)=0 for every x0, B being affine in x0);
  (c) the flux  Phi = - int_{annulus} P+ R^lin(chi h) P+  (chi=1 inside, 0 outside) equals
      + oint_{S_t} [n_a d_b h_cd assembled into R^lin] dS, computed by exact monomial integration on S^3.
Output: Phi as a 3x3 matrix in the orthonormal Lambda^+ basis (w1,w2,w3), w1 = omega/sqrt2.
Prediction: Phi = pi^2 * w1 w1^T, giving  P(g_x0) - P(g) - 8pi^2 = -8 x0 <R^+_p, Phi> = -8pi^2 x0 R^+_p(zeta,zeta).
"""
import json, itertools
from pathlib import Path
import sympy as sp

X = sp.symbols('x1:5', real=True)
t2 = sum(x**2 for x in X)
Jx = [-X[1], X[0], -X[3], X[2]]
d = lambda i, j: 1 if i == j else 0


def Rlin(h):
    """R_ijkl of delta+h to first order; convention R_1212 = sectional curvature."""
    R = {}
    for i, j, k, l in itertools.product(range(4), repeat=4):
        R[i, j, k, l] = sp.Rational(1, 2)*(sp.diff(h[i][l], X[j], X[k]) + sp.diff(h[j][k], X[i], X[l])
                                           - sp.diff(h[j][l], X[i], X[k]) - sp.diff(h[i][k], X[j], X[l]))
    return R


# orthonormal bases of Lambda^+ and Lambda^- (orientation dx1234), as antisymmetric 4x4 matrices
def two_form(pairs):
    M = sp.zeros(4, 4)
    for (a, b, c) in pairs:
        M[a, b] += c; M[b, a] -= c
    return M / sp.sqrt(2)


Wp = [two_form([(0, 1, 1), (2, 3, 1)]), two_form([(0, 2, 1), (3, 1, 1)]), two_form([(0, 3, 1), (1, 2, 1)])]
Wm = [two_form([(0, 1, 1), (2, 3, -1)]), two_form([(0, 2, 1), (3, 1, -1)]), two_form([(0, 3, 1), (1, 2, -1)])]


def block(R, A, Bs):
    """<R(w_A), w_B> = 1/4 sum w_A,ij w_B,kl R_ijkl."""
    return sp.Matrix(3, 3, lambda a, b: sp.Rational(1, 4)*sum(A[a][i, j]*Bs[b][k, l]*R[i, j, k, l]
                                                               for i, j, k, l in itertools.product(range(4), repeat=4)
                                                               if A[a][i, j] != 0 and Bs[b][k, l] != 0))


def check_sign():
    K = sp.Symbol('K')
    h = [[-K/3*(t2*d(i, j) - X[i]*X[j]) for j in range(4)] for i in range(4)]
    R = Rlin(h)
    return sp.simplify(R[0, 1, 0, 1]), sp.simplify(block(R, Wp, Wp)), sp.simplify(block(R, Wm, Wm))


def burns_tail():
    return [[(d(i, j) - X[i]*X[j]/t2 - Jx[i]*Jx[j]/t2)/t2 for j in range(4)] for i in range(4)]


def sphere_monomial(alpha):
    """oint_{S^3} x^alpha dS (unit sphere), exact."""
    if any(a % 2 for a in alpha):
        return sp.Integer(0)
    return 2*sp.prod([sp.gamma(sp.Rational(a + 1, 2)) for a in alpha])/sp.gamma(sp.Rational(sum(alpha) + 4, 2))


def sphere_integral(expr):
    """Integrate a function on the unit sphere: substitute t2=1 is NOT valid for derivatives, so expr
    must already be evaluated (as a rational function) and is reduced to a polynomial using t2=1."""
    num, den = sp.fraction(sp.together(expr))
    # on S^3 every denominator is a power of t2 -> evaluate it at 1
    den1 = sp.simplify(den.subs({X[0]: 1, X[1]: 0, X[2]: 0, X[3]: 0}))
    assert sp.simplify(den - den1*t2**sp.Poly(den, *X).total_degree()//2 if False else 0) == 0
    poly = sp.Poly(sp.expand(num), *X)
    tot = sum(c*sphere_monomial(m) for m, c in poly.terms())
    return sp.simplify(tot/den1)


def flux(h):
    """Phi = - int_annulus P+ R^lin(chi h) P+ = oint_{S_1} assembled n_a d_b h_cd dS."""
    n = X  # unit normal on S_1
    F = {}
    for a, b, c, e in itertools.product(range(4), repeat=4):
        F[a, b, c, e] = n[a]*sp.diff(h[c][e], X[b])
    # R_ijkl = 1/2(d_j d_k h_il + d_i d_l h_jk - d_i d_k h_jl - d_j d_l h_ik) -> replace d_a d_b f by oint n_a d_b f
    Rf = {}
    for i, j, k, l in itertools.product(range(4), repeat=4):
        Rf[i, j, k, l] = sp.Rational(1, 2)*(F[j, k, i, l] + F[i, l, j, k] - F[i, k, j, l] - F[j, l, i, k])
    out = {}
    for name, A, Bs in [('PlusPlus', Wp, Wp), ('MinusMinus', Wm, Wm), ('PlusMinus', Wp, Wm)]:
        M = sp.zeros(3, 3)
        for a in range(3):
            for b in range(3):
                integrand = sp.Rational(1, 4)*sum(A[a][i, j]*Bs[b][k, l]*Rf[i, j, k, l]
                                                  for i, j, k, l in itertools.product(range(4), repeat=4)
                                                  if A[a][i, j] != 0 and Bs[b][k, l] != 0)
                integrand = sp.together(integrand)
                num, den = sp.fraction(integrand)
                # all denominators are powers of t2; on S^1 they equal 1
                denv = den.subs({X[0]: 1, X[1]: 0, X[2]: 0, X[3]: 0})
                assert sp.simplify(den - denv*t2**sp.degree(sp.Poly(den, *X))//2 if False else 0) == 0
                poly = sp.Poly(sp.expand(num), *X)
                # reduce: on S^3 we may not drop t2 inside num, but monomial integration is exact anyway;
                # den is c*t2^k, which is the constant c on S_1
                M[a, b] = sp.nsimplify(sp.simplify(sum(cf*sphere_monomial(m) for m, cf in poly.terms())/denv))
        out[name] = M
    return out


if __name__ == '__main__':
    res = {}
    R1212, Rpp, Rmm = check_sign()
    res['sign_check'] = dict(R1212=str(R1212), PlusPlus=str(Rpp), MinusMinus=str(Rmm))
    h = burns_tail()
    R = Rlin(h)
    res['tail_selfdual_block_pointwise'] = str(sp.simplify(block(R, Wp, Wp)))
    res['tail_scalar_pointwise'] = str(sp.simplify(2*sum(R[i, j, i, j] for i in range(4) for j in range(4))/2))
    Fl = flux(h)
    for k, v in Fl.items():
        res['flux_' + k] = str(v)
        print(k, v)
    res['flux_PlusPlus_over_pi2'] = str(sp.simplify(Fl['PlusPlus']/sp.pi**2))
    res['scalar_flux_Fs=4trPhi'] = str(sp.simplify(4*Fl['PlusPlus'].trace()))
    print(json.dumps(res, indent=1))
    out = Path(__file__).resolve().parent.parent/'data'/'burns_transgression_flux.json'
    out.write_text(json.dumps(res, indent=1))

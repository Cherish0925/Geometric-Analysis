"""Exact local checks for the global harmonic-separator inequality.

Run: qiushi-yau26 env numeric python round7_spectral_check.py
No numerical spectrum is substituted for the complete-manifold theorem.
"""

import sympy as s


def zero(expr):
    return s.simplify(s.expand(expr)) == 0


def main():
    hn, hz, a, b, c, d, p, q, h = s.symbols(
        "hn hz a b c d p q h", real=True
    )
    # The first row is grad |du|, with zero vertical entries by invariance.
    # The tangent 3x3 block has trace -hn because u is harmonic.
    H = s.Matrix(
        [[hn, hz, 0, 0], [hz, a, p, q],
         [0, p, b, d], [0, q, d, -hn-a-b]]
    )
    tangent = H[1:4, 1:4]
    tangent_tf = tangent + hn * s.eye(3) / 3
    defect = s.trace(H * H) - s.Rational(4, 3) * (hn**2 + hz**2)
    assert zero(defect - s.trace(tangent_tf * tangent_tf)
                - s.Rational(2, 3) * hz**2)
    # The mixed tangent entries contribute 2(p^2+q^2), not p^2+q^2.
    remainder = s.trace(tangent_tf * tangent_tf) - 2 * (p**2 + q**2)
    assert zero(remainder - ((3*a+hn)**2/s.Integer(6)
                            + (a+2*b+hn)**2/s.Integer(2) + 2*d**2))
    assert not zero(defect - s.trace(tangent_tf * tangent_tf)
                    - s.Rational(1, 3) * hz**2)
    print("PASS harmonic Hessian/Kato decomposition and wrong coefficient rejection")

    x, alpha = s.symbols("x alpha", positive=True)
    grad2, D, Enn = s.symbols("grad2 D Enn", real=True)
    lap_h = (grad2/s.Integer(3) + D)/x - 3*x + Enn*x
    lap_power = alpha*x**(alpha-1)*lap_h + alpha*(alpha-1)*x**(alpha-2)*grad2
    expected = -2*x**s.Rational(2, 3) + s.Rational(2, 3)*Enn*x**s.Rational(2, 3)
    expected += s.Rational(2, 3)*D*x**s.Rational(-4, 3)
    assert s.simplify(lap_power.subs(alpha, s.Rational(2, 3)) - expected) == 0
    print("PASS exponent cancellation and signed Ricci residual")

    # Coordinate-Christoffel check on a genuine twisted Gaussian metric:
    # dt^2 + f(t)^2[dtheta^2 + (dx+A(t)dtheta)^2 + dy^2].
    t = s.symbols("t", real=True)
    f, A = s.Function("f")(t), s.Function("A")(t)
    g = s.diag(1, f**2, f**2, f**2)
    g[1, 1] += f**2*A**2
    g[1, 2] = g[2, 1] = f**2*A
    inv = s.simplify(g.inv())

    def derivative(expr, i):
        return s.diff(expr, t) if i == 0 else s.S.Zero

    Gamma = [[[s.simplify(sum(inv[k, ell] * (
        derivative(g[ell, j], i) + derivative(g[ell, i], j)
        - derivative(g[i, j], ell)) for ell in range(4))/2)
               for j in range(4)] for i in range(4)] for k in range(4)]
    Ric00 = s.simplify(sum(
        derivative(Gamma[k][0][0], k) - derivative(Gamma[k][0][k], 0)
        + sum(Gamma[k][0][0]*Gamma[ell][k][ell]
              - Gamma[ell][0][k]*Gamma[k][0][ell] for ell in range(4))
        for k in range(4)))
    Q = s.diff(A, t)**2/2
    assert zero(Ric00 + 3*s.diff(f, t, 2)/f + Q)
    # u'=f^-3 is harmonic since det(g)=f^6.
    du = f**-3
    Hess = s.Matrix(4, 4, lambda i, j:
                    (s.diff(du, t) if i == j == 0 else 0) - Gamma[0][i][j]*du)
    assert zero(s.trace(inv*Hess))
    norm_hess = s.simplify(s.trace(inv*Hess*inv*Hess))
    kato = s.simplify(norm_hess - s.Rational(4, 3)*s.diff(du, t)**2)
    assert zero(kato - Q*du**2)
    v = f**-2
    lap_v = s.diff(v, t, 2) + 3*s.diff(f, t)/f*s.diff(v, t)
    assert zero(lap_v - (-2*v+s.Rational(2, 3)*(Ric00+3+Q)*v))
    assert not zero(kato - Q*du**2/2)
    print("PASS coordinate Ricci, harmonicity, twist norm, full power identity")

    # Complete AH example f=cosh(t), A=k*tanh(t).
    # Its normal Ricci error is -Q, not zero. This exactly cancels the
    # positive twist defect; forgetting E(n,n) would give a false bound.
    k = s.symbols("k", real=True)
    substitutions = {f: s.cosh(t), A: k*s.tanh(t)}
    def actual(expr):
        return s.simplify(expr.subs(substitutions).doit())
    assert actual(Ric00 + 3 + Q) == 0
    assert s.simplify(actual(lap_v + 2*v)) == 0
    assert actual(Q).subs(t, 0) == k**2/2
    # Exact integrals: int sech(t)=pi, int sech(t)*tanh(t)^2=pi/2.
    # v^2 dV = sech(t)dt per unit coordinate torus volume.
    denominator = s.integrate(2/(1+x**2), (x, 0, s.oo))
    numerator = s.integrate(8*(x**2-1)**2/(x**2+1)**3, (x, 0, s.oo))
    assert s.simplify(numerator/denominator) == 2
    print("PASS complete twisted AH test: positive L2 eigenfunction at eigenvalue 2")
    print("All exact checks passed. Global analysis is in round7_spectral.md.")


if __name__ == "__main__":
    main()

"""Independent coordinate-jet checks of the signature-change Ricci formula.

Uses exact rational arithmetic and the coordinate metric, not the reduced
Einstein equations. Run with qiushi-yau26 env numeric python.
"""

import sympy as s


def ricci_at(metric, coords, point):
    n = len(coords)
    g = metric.subs(point)
    inv = g.inv()
    dg = [metric.diff(x).subs(point) for x in coords]
    ddg = [[metric.diff(x, y).subs(point) for y in coords] for x in coords]
    dinv = [-inv * d * inv for d in dg]
    Gamma = [[[sum(inv[k, l] * (dg[i][l, j] + dg[j][l, i] - dg[l][i, j])
                       for l in range(n)) / 2
               for j in range(n)] for i in range(n)] for k in range(n)]

    def dGamma(a, k, i, j):
        return sum(
            dinv[a][k, l] * (dg[i][l, j] + dg[j][l, i] - dg[l][i, j])
            + inv[k, l] * (ddg[a][i][l, j] + ddg[a][j][l, i] - ddg[a][l][i, j])
            for l in range(n)) / 2

    Ric = s.Matrix(n, n, lambda i, j: s.simplify(sum(
        dGamma(k, k, i, j) - dGamma(j, k, i, k)
        + sum(Gamma[k][k][l] * Gamma[l][i][j]
              - Gamma[k][j][l] * Gamma[l][i][k] for l in range(n))
        for k in range(n))))
    return Ric, Gamma


t, x, y, z = s.symbols("t x y z", real=True)
coords = (t, x, y, z)
base = (x, y, z)
h = s.diag(1 + y*y, 1 + x*x, 1 + z*z)
V = 2 + x + y*y
alpha = s.Matrix([y*z, x + z*z, y + x*x])
F = s.Matrix(3, 3, lambda i, j: s.diff(alpha[j], base[i]) - s.diff(alpha[i], base[j]))
theta = s.Matrix([1, *alpha])
horizontal_metric = s.zeros(4)
horizontal_metric[1:, 1:] = h

checks = 0
static_checks = 0
for point in ({t: 0, x: 0, y: 0, z: 0},
              {t: 0, x: s.Rational(1, 3), y: s.Rational(-1, 2), z: s.Rational(2, 5)}):
    hp, vp, ap, fp = h.subs(point), V.subs(point), alpha.subs(point), F.subs(point)
    rh, gh = ricci_at(h, base, point)
    dV = [s.diff(V, a).subs(point) for a in base]
    Hess = s.Matrix(3, 3, lambda i, j: s.diff(V, base[i], base[j]).subs(point)
                    - sum(gh[k][i][j]*dV[k] for k in range(3)))
    Lap = s.trace(hp.inv()*Hess)
    B = fp*hp.inv()*fp.T
    f2 = s.trace(hp.inv()*B)
    frame_R = s.eye(4)
    frame_R[0, 0] = 1/vp
    for j in range(3):
        frame_R[0, j+1] = -ap[j]
    rr, _ = ricci_at(horizontal_metric + V*V*(theta*theta.T), coords, point)
    rr = s.simplify(frame_R.T*rr*frame_R)
    assert s.simplify(rr[0, 0] + Lap/vp - vp*vp*f2/4) == 0
    assert s.simplify(rr[1:, 1:] - rh + Hess/vp + vp*vp*B/2) == s.zeros(3)
    checks += 2
    static_metric = horizontal_metric.copy()
    static_metric[0, 0] = -V*V
    rs, _ = ricci_at(static_metric, coords, point)
    static_frame = s.diag(1/vp, 1, 1, 1)
    rs = s.simplify(static_frame.T*rs*static_frame)
    assert s.simplify(rs[0, 0] + rr[0, 0] - vp*vp*f2/4) == 0
    assert s.simplify(rs[1:, 1:] - rr[1:, 1:] - vp*vp*B/2) == s.zeros(3)
    assert rs[0, 1:] == s.zeros(1, 3)
    static_checks += 3
    for lam in (s.Rational(1, 3), s.Rational(2, 1)):
        rl, _ = ricci_at(horizontal_metric - lam*lam*V*V*(theta*theta.T), coords, point)
        frame_L = frame_R.copy()
        frame_L[0, 0] /= lam
        rl = s.simplify(frame_L.T*rl*frame_L)
        assert s.simplify(rl[0, 0] - Lap/vp - lam*lam*vp*vp*f2/4) == 0
        assert s.simplify(rl[1:, 1:] - rh + Hess/vp - lam*lam*vp*vp*B/2) == s.zeros(3)
        # Vanishing Riemannian mixed Ricci is preserved, not merely assumed.
        assert s.simplify(rl[0, 1:] + lam*rr[0, 1:]) == s.zeros(1, 3)
        assert s.simplify(rl[1:, 1:] - (rh - Hess/vp - lam*lam*vp*vp*B/2)) != s.zeros(3)
        assert s.simplify(rl[0, 0] - (Lap/vp + lam*lam*vp*vp*f2/8)) != 0
        checks += 3

print(f"PASS: {checks} exact coordinate-jet block checks at two points, two Lorentz scales.")
print(f"PASS: {static_checks} static-auxiliary block comparisons retaining original nonzero twist.")
print("PASS: wrong Lorentz twist sign and factor-of-two form-norm variants rejected.")

# Independent symbolic contraction at a minimal quotient separator.
Einstein_constant, hess_nn, ii2, fn2, f2, lapse, Enn, Euu = s.symbols(
    "Einstein_constant hess_nn ii2 fn2 f2 lapse Enn Euu", real=True)
ric_nn = Einstein_constant + Enn + hess_nn/lapse + lapse**2*fn2/2
lap_over_lapse = -Einstein_constant - Euu + lapse**2*f2/4
J_over_lapse = -(lap_over_lapse - hess_nn/lapse) - ric_nn - ii2
assert s.expand(J_over_lapse + ii2 + lapse**2*f2/4
                + lapse**2*fn2/2 + Enn - Euu) == 0
print("PASS: exact and near-Einstein quotient Jacobi identity, arbitrary Einstein constant.")
print("These checks support the Ricci identities, not the global causal theorem.")

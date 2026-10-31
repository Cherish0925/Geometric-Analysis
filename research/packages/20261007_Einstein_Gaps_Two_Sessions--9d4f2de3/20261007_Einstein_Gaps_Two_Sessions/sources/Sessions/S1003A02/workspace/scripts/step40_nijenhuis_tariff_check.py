"""Step 40: algebra behind the Nijenhuis form of the simultaneous signed-cost identity.

Input : none (pure algebra in flat R^4 at one point, plus symbolic polynomial identities).
Output: workspace/data/step40_nijenhuis_tariff_check.json

Checks
 (1) Clifford contraction c: T^*(x)u^perp -> S^-, v |-> sum_i e_i.(v_i u^perp), for a unit u in S^+.
     (a) c c^T = 2 Id on S^-  (so |c(v)|^2 = 2|v_4|^2 on (ker c)^perp);
     (b) ker c = {first jets of u with d omega(0)=0}, omega = Bloch 2-form of u
         (i.e. ker c is the almost-Kaehler / Gray-Hervella W_2 = Nijenhuis component, the
         complement is the Lee-form component W_4);
     (c) for real covectors a,b: |(a+ib).u|^2 = |a+J'b|^2 for an orthogonal complex structure J'.
     (d) |nabla n|^2 = 4|v|^2 for the unit self-dual Bloch vector n of u.
 (2) Pointwise consequence of D_A Phi=0, Phi=sqrt(rho) u, a=d sqrt(rho), b=sqrt(rho) beta:
        rho|v_4|^2 = |a+J'b|^2/2.
 (3) Polynomial and quadratic-form inequalities used with the weight psi(rho)=2 rho:
        m(rho) - rho^2(2-rho) = -(2-rho)^2 (2+2rho-rho^2)/6,
        coefficient form  -rho(|a|^2+5|b|^2-2<a,J'b>)  is negative definite.
 (4) Self-dual Weitzenboeck polynomial: (rho^2/6)(4-rho^2) - (2-rho)^2(2+2rho-rho^2)/6
        = (2-rho)(rho-1)(3rho+2)/3.
"""
import json, pathlib
import numpy as np
import sympy as sp

rng = np.random.default_rng(40)
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
E = [I2, 1j * sx, 1j * sy, 1j * sz]          # e_i : S^+ -> S^-
pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]


def omega_of(u):
    """Bloch 2-form omega_ij = Im u^dag (e_i e_j) u on S^+, e_i e_j|_{S+} = -E_i^dag E_j."""
    w = np.zeros((4, 4))
    for i, j in pairs:
        val = np.imag(u.conj() @ (-E[i].conj().T @ E[j]) @ u)
        w[i, j], w[j, i] = val, -val
    return w


def real_basis_jets():
    """Real basis of v in C^4 (v_i = coefficient of u_perp in d_i u)."""
    B = []
    for i in range(4):
        for ph in (1.0, 1j):
            v = np.zeros(4, dtype=complex); v[i] = ph; B.append(v)
    return B


def check_at(u0):
    u0 = u0 / np.linalg.norm(u0)
    up = np.array([-u0[1].conj(), u0[0].conj()])    # unit, orthogonal to u0
    B = real_basis_jets()
    Cmat, Dmat, gradn = [], [], []
    h = 1e-6
    w0 = omega_of(u0)
    for v in B:
        Du = sum(E[i] @ (v[i] * up) for i in range(4))
        Cmat.append(np.concatenate([Du.real, Du.imag]))
        # d omega(0) and nabla omega(0) by central differences along each direction
        dw = np.zeros((4, 4, 4))
        for k in range(4):
            ep = u0 + h * v[k] * up; em = u0 - h * v[k] * up
            dw[k] = (omega_of(ep / np.linalg.norm(ep)) - omega_of(em / np.linalg.norm(em))) / (2 * h)
        trip = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        Dmat.append([dw[i, j, k] + dw[j, k, i] + dw[k, i, j] for (i, j, k) in trip])
        gradn.append(dw)
    C = np.array(Cmat).T          # 4 x 8
    Dm = np.array(Dmat).T         # 4 x 8
    CCt = C @ C.T
    # kernels
    kC = np.linalg.svd(C)[2][4:]
    kD = np.linalg.svd(Dm)[2][4:]
    # principal angles between kernels
    s = np.linalg.svd(kC @ kD.T, compute_uv=False)
    # |nabla n|^2 vs 4|v|^2 for random v; |omega|=sqrt2 for unit u (form norm sum_{i<j})
    vr = rng.normal(size=8)
    dw = sum(vr[m] * gradn[m] for m in range(8))
    norm_omega2 = sum(w0[i, j] ** 2 for i, j in pairs)
    grad_omega2 = sum(dw[k, i, j] ** 2 for k in range(4) for i, j in pairs)
    gradn2 = grad_omega2 / norm_omega2
    # (c) |(a+ib).u|^2 versus |a+J'b|^2 with J' read off from i(b.u)=(J'b).u
    Emat = np.array([np.concatenate([(E[i] @ u0).real, (E[i] @ u0).imag]) for i in range(4)]).T
    Jp = np.linalg.solve(Emat, np.array([np.concatenate([(1j * E[i] @ u0).real, (1j * E[i] @ u0).imag])
                                         for i in range(4)]).T)
    a, b = rng.normal(size=4), rng.normal(size=4)
    gam = sum((a[i] + 1j * b[i]) * (E[i] @ u0) for i in range(4))
    lhs = np.vdot(gam, gam).real
    rhs = np.sum((a + Jp @ b) ** 2)
    return dict(CCt_minus_2I=float(np.abs(CCt - 2 * np.eye(4)).max()),
                kernel_cosines=s.tolist(),
                gradn2_over_4v2=float(gradn2 / (4 * np.sum(vr ** 2))),
                Jprime_orthogonal=float(np.abs(Jp.T @ Jp - np.eye(4)).max()),
                Jprime_squared_plus_I=float(np.abs(Jp @ Jp + np.eye(4)).max()),
                complex_clifford_norm_residual=float(abs(lhs - rhs)),
                omega_norm2=float(norm_omega2),
                rank_C=int(np.linalg.matrix_rank(C)), rank_dOmega=int(np.linalg.matrix_rank(Dm, tol=1e-6)))


clifford = [check_at(rng.normal(size=2) + 1j * rng.normal(size=2)) for _ in range(5)]

r = sp.symbols('rho', nonnegative=True)
m = (2 - r) * (-r**3 + 10 * r**2 - 2 * r - 4) / 6
poly1 = sp.factor(sp.expand(m - r**2 * (2 - r)))
target1 = -(2 - r)**2 * (2 + 2 * r - r**2) / 6
poly2 = sp.factor(sp.expand(r**2 * (4 - r**2) / 6 - (2 - r)**2 * (2 + 2 * r - r**2) / 6))
target2 = (2 - r) * (r - 1) * (3 * r + 2) / 3
# quadratic form from psi=2rho: |a|^2 coeff 3r+4r-8r, |b|^2 coeff 3r-8r, cross 2r<a,J'b>
psi = 2 * r
coef_a = sp.Rational(3, 2) * psi + 2 * r * sp.diff(psi, r) - 8 * r
coef_b = sp.Rational(3, 2) * psi - 8 * r
cross = psi
form = sp.Matrix([[coef_a, cross / 2], [cross / 2, coef_b]])
out = dict(
    clifford_checks=clifford,
    m_minus_rho2_2minusrho=str(poly1),
    m_identity_residual=str(sp.simplify(poly1 - target1)),
    weitzenboeck_polynomial=str(poly2),
    weitzenboeck_identity_residual=str(sp.simplify(poly2 - target2)),
    quadratic_form=str(form),
    quadratic_form_det_over_rho2=str(sp.simplify(form.det() / r**2)),
    quadratic_form_trace=str(sp.simplify(form.trace())),
    leftover_positive_on_0_2=str(sp.factor(2 + 2 * r - r**2)),
    nijenhuis_coefficient='psi*rho*|v_2|^2 = 2 rho^2 |v_2|^2 = rho^2 |grad n|^2_{W2} / 2',
)


def dpsi_form(u0, rho0=1.3):
    """(5) |d psi|^2 / rho as a quadratic form in (a,b) in R^8, psi=rho*n, under D_A Phi=0.

    The Dirac equation determines the W_4 part v_4 = -c^+((a+ib).u)/sqrt(rho); the W_2 part
    lies in ker d and does not enter d psi.  Also returns the full combined form
        G = Q_d - 2|a|^2 - |a+J'b|^2 - (|a|^2+5|b|^2-2<a,J'b>)
    appearing in the Weitzenboeck form of the saving bound (all divided by rho)."""
    u0 = u0 / np.linalg.norm(u0)
    up = np.array([-u0[1].conj(), u0[0].conj()])
    B = real_basis_jets()
    C = np.array([np.concatenate([sum(E[i] @ (v[i] * up) for i in range(4)).real,
                                  sum(E[i] @ (v[i] * up) for i in range(4)).imag]) for v in B]).T
    Cp = np.linalg.pinv(C)
    Emat = np.array([np.concatenate([(E[i] @ u0).real, (E[i] @ u0).imag]) for i in range(4)]).T
    Jp = np.linalg.solve(Emat, np.array([np.concatenate([(1j * E[i] @ u0).real, (1j * E[i] @ u0).imag])
                                         for i in range(4)]).T)
    n0 = omega_of(u0) / np.sqrt(2)
    h = 1e-6
    trip = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

    def dpsi(ab):
        a, b = ab[:4], ab[4:]
        gam = sum((a[i] + 1j * b[i]) * (E[i] @ u0) for i in range(4))
        vr = -Cp @ np.concatenate([gam.real, gam.imag]) / np.sqrt(rho0)
        v = np.array([vr[2 * i] + 1j * vr[2 * i + 1] for i in range(4)])
        dn = np.zeros((4, 4, 4))
        for k in range(4):
            ep = u0 + h * v[k] * up; em = u0 - h * v[k] * up
            dn[k] = (omega_of(ep / np.linalg.norm(ep)) - omega_of(em / np.linalg.norm(em))) / (2 * h * np.sqrt(2))
        drho = 2 * np.sqrt(rho0) * a
        grad = np.array([drho[k] * n0 + rho0 * dn[k] for k in range(4)])
        return np.array([grad[i, j, k] + grad[j, k, i] + grad[k, i, j] for (i, j, k) in trip])

    Q = np.zeros((8, 8))
    basis = np.eye(8)
    vals = [dpsi(basis[m]) for m in range(8)]
    for p in range(8):
        for q in range(8):
            Q[p, q] = vals[p] @ vals[q] / rho0
    Ia = np.zeros((8, 8)); Ia[:4, :4] = np.eye(4)
    Ib = np.zeros((8, 8)); Ib[4:, 4:] = np.eye(4)
    X = np.zeros((8, 8)); X[:4, 4:] = Jp; X[4:, :4] = Jp.T          # <a,J'b> polarized x2
    aJb2 = Ia + Ib + X                                               # |a+J'b|^2
    G = Q - 2 * Ia - aJb2 - (Ia + 5 * Ib - X)
    return dict(Qd_eigs=np.round(np.linalg.eigvalsh(Q), 10).tolist(),
                Qd_minus_combo=None,
                G_eigs=np.round(np.linalg.eigvalsh(G), 10).tolist())


out['dpsi_checks'] = [dpsi_form(rng.normal(size=2) + 1j * rng.normal(size=2), rho0=r0)
                      for r0 in (0.4, 1.3, 1.9)]

# (6) Pointwise envelope ("exhaustion") of the two exact forms.
#   amplitude form   : saving <= int m(rho) - 4|M|^2 - ...
#   Weitzenboeck form: saving <= int [rho^2 x - 4|M|^2 + p2(rho)] - ...,  x=M(n,n), |M|^2>=3x^2/2
#   closed identity  : P = 4W_+ + 4V/3 - 8pi^2(A-k),  |W^+|^2 = rho^4/24 - rho^2 x/2 + |M|^2.
#   For t,lam: P >= 8pi^2[k-(1-t)A] + int g,  g = (1-t)(rho^4/6+4/3) - t[lam p2+(1-lam)m]
#                                              - (t lam + 2 - 2t)^2 rho^4/24 .
t, lam = sp.symbols('t lam')
p2 = (2 - r) * (r - 1) * (3 * r + 2) / 3
g = (1 - t) * (r**4 / 6 + sp.Rational(4, 3)) - t * (lam * p2 + (1 - lam) * m) \
    - (t * lam + 2 - 2 * t)**2 * r**4 / 24
g_lebrun = sp.factor(sp.expand(g.subs({t: sp.Rational(2, 3), lam: sp.Rational(2, 3)})))
g_at_32 = sp.expand(g.subs(r, sp.Rational(3, 2)))
lam_opt = sp.solve(sp.diff(g_at_32, lam), lam)[0]
g_at_32_opt = sp.factor(sp.simplify(g_at_32.subs(lam, lam_opt)))
out['exhaustion'] = dict(
    g_at_t_lam_two_thirds=str(g_lebrun),
    g_at_rho_three_halves_maximized_over_lam=str(g_at_32_opt),
    lam_opt=str(sp.simplify(lam_opt)),
    meaning='g(2/3,2/3;rho)>=0 on [0,2] gives C_+>=2A/3 (LeBrun); max_lam g(t,lam;3/2)<0 for t>2/3, '
            'so no pointwise combination of the two exact forms beats LeBrun; binding at rho=3/2.')
path = pathlib.Path(__file__).resolve().parents[1] / 'data' / 'step40_nijenhuis_tariff_check.json'
path.write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1))

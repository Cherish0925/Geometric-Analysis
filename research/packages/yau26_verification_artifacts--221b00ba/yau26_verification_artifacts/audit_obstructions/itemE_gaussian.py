"""ITEM E: verify the Gaussian-coordinate Ricci formulas (eq:fullRic, eq:gaussian-evolution,
eq:gaussian-constraint, eq:diagonal-five) for g = dr^2 + q(r), and the identities used in
Proposition prop:center-contraction.
"""
import sympy as sp
import functools
print = functools.partial(print, flush=True)
from ricci_tools import ricci, cov_div_sym2

r, z, x, y = sp.symbols('r z x y', real=True)


def check_gaussian(q, X3, label, numeric_point=None):
    """q: 3x3 sympy matrix depending on r and the slice coordinates X3."""
    X4 = [r] + list(X3)
    g = sp.zeros(4, 4)
    g[0, 0] = 1
    for i in range(3):
        for j in range(3):
            g[i + 1, j + 1] = q[i, j]
    Ric4 = ricci(g, X4)
    K = q.diff(r) / 2
    Kr = K.diff(r)
    qinv = q.inv()
    S = qinv * K
    H = S.trace()
    Ricq = ricci(q, list(X3))
    # paper formulas
    Rrr = -(qinv * Kr).trace() + (S * S).trace()
    divK = cov_div_sym2(q, list(X3), K)
    Rri = [divK[i] - sp.diff(H, X3[i]) for i in range(3)]
    Rij = Ricq - Kr - H * K + 2 * K * qinv * K
    # residual E = Ric + 3g in the paper
    E_rr = Ric4[0, 0] + 3
    E_T = Ric4[1:, 1:] + 3 * q
    # evolution/constraint forms
    Sr = S.diff(r)
    evoS = qinv * Ricq + 3 * sp.eye(3) - H * S - qinv * E_T - Sr
    evoH = 3 - (S * S).trace() - E_rr - sp.diff(H, r)
    Rq = (qinv * Ricq).trace()
    constraint = -6 + H**2 - (S * S).trace() + (qinv * E_T).trace() - E_rr - Rq
    diffs = {
        'Ric_rr': Ric4[0, 0] - Rrr,
        'Ric_ri': sp.Matrix([Ric4[0, i + 1] - Rri[i] for i in range(3)]),
        'Ric_ij': Ric4[1:, 1:] - Rij,
        'S_r evolution': evoS,
        'H_r evolution': evoH,
        'Hamiltonian constraint': constraint,
        'S_r = q^{-1}K_r - 2S^2': Sr - (qinv * Kr - 2 * S * S),
    }
    print(f"--- {label}")
    for name, dd in diffs.items():
        if numeric_point is None:
            val = sp.simplify(dd)
            ok = (val == 0) if not isinstance(val, sp.MatrixBase) else (val == sp.zeros(*val.shape))
            print(f"   {name:28s}: identically zero? {ok}")
        else:
            val = sp.Matrix([dd]).subs(numeric_point).evalf(30)
            print(f"   {name:28s}: max |diff| at test point = {max(abs(v) for v in val):.3e}")
    return Ric4


# ---------------- Test 1: diagonal metric, fully symbolic functions of (r,z)
a = sp.Function('a')(r, z)
b = sp.Function('b')(r, z)
c = sp.Function('c')(r, z)
q1 = sp.diag(sp.exp(2 * a), sp.exp(2 * b), sp.exp(2 * c))
Ric4 = check_gaussian(q1, (z, x, y), "Test 1: q = diag(e^{2a},e^{2b},e^{2c}), a,b,c arbitrary functions of (r,z)")

# eq:diagonal-five (orthonormal components of E = Ric+3g)
Hh = a.diff(r) + b.diff(r) + c.diff(r)
rz = -sp.exp(-2 * a) * (b.diff(z, 2) + c.diff(z, 2) + b.diff(z)**2 + c.diff(z)**2 - a.diff(z) * (b.diff(z) + c.diff(z)))
rx = -sp.exp(-2 * a) * (b.diff(z, 2) + b.diff(z)**2 + b.diff(z) * c.diff(z) - a.diff(z) * b.diff(z))
ry = -sp.exp(-2 * a) * (c.diff(z, 2) + c.diff(z)**2 + b.diff(z) * c.diff(z) - a.diff(z) * c.diff(z))
paper = {
    'E_rr': 3 - a.diff(r, 2) - b.diff(r, 2) - c.diff(r, 2) - a.diff(r)**2 - b.diff(r)**2 - c.diff(r)**2,
    'E_rz': sp.exp(-a) * (a.diff(r) * (b.diff(z) + c.diff(z)) - b.diff(r) * b.diff(z) - c.diff(r) * c.diff(z)
                          - b.diff(r, z) - c.diff(r, z)),
    'E_zz': 3 + rz - a.diff(r, 2) - Hh * a.diff(r),
    'E_x': 3 + rx - b.diff(r, 2) - Hh * b.diff(r),
    'E_y': 3 + ry - c.diff(r, 2) - Hh * c.diff(r),
}
direct = {
    'E_rr': Ric4[0, 0] + 3,
    'E_rz': Ric4[0, 1] * sp.exp(-a),
    'E_zz': Ric4[1, 1] * sp.exp(-2 * a) + 3,
    'E_x': Ric4[2, 2] * sp.exp(-2 * b) + 3,
    'E_y': Ric4[3, 3] * sp.exp(-2 * c) + 3,
}
print("   eq:diagonal-five:")
for k in paper:
    print(f"      {k}: paper - direct = {sp.simplify(paper[k] - direct[k])}")
print("      other off-diagonal Ricci entries:",
      [sp.simplify(Ric4[i, j]) for (i, j) in [(0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]])

# ---------------- Proposition prop:center-contraction ingredients
print("--- Proposition (centre contraction): 3D metric q0 = ds^2 + G(s), G a general 2x2 matrix")
s = sp.symbols('s', real=True)
G11, G12, G22 = [sp.Function(n)(s) for n in ('G11', 'G12', 'G22')]
G = sp.Matrix([[G11, G12], [G12, G22]])
q0 = sp.zeros(3, 3)
q0[0, 0] = 1
q0[1:, 1:] = G
Ric3 = ricci(q0, [s, x, y])
A = G.inv() * G.diff(s) / 2
h = A.trace()
R3 = sp.simplify((q0.inv() * Ric3).trace())
print("   R_{q0} - (-2h_s - trA^2 - h^2) =", sp.simplify(R3 - (-2 * h.diff(s) - (A * A).trace() - h**2)))
print("   h - (log sqrt det G)_s =", sp.simplify(h - sp.diff(sp.log(sp.sqrt(G.det())), s)))
# sectional curvature of the orbit plane = R/2 - Ric(v,v)
Korb = sp.simplify(R3 / 2 - Ric3[0, 0])
print("   K_orb - (-det A) =", sp.simplify(Korb + A.det()))
print("   Ric(v,v) - (-h_s - trA^2) =", sp.simplify(Ric3[0, 0] - (-h.diff(s) - (A * A).trace())))
# trace-free A: -det A = tr A^2 / 2
a11, a12, a21 = sp.symbols('a11 a12 a21')
A0 = sp.Matrix([[a11, a12], [a21, -a11]])
print("   trace-free 2x2: -det A - trA^2/2 =", sp.simplify(-A0.det() - (A0 * A0).trace() / 2))

# Yamabe seed: h0 = dtheta^2 + e^{2f} dx^2 + e^{-2f} dy^2 and conformal change psi^4 h0
th = sp.symbols('theta', real=True)
f = sp.Function('f')(th)
psi = sp.Function('psi')(th)
h0 = sp.diag(1, sp.exp(2 * f), sp.exp(-2 * f))
R0 = sp.simplify((h0.inv() * ricci(h0, [th, x, y])).trace())
print("   R(h0) =", R0)
hconf = psi**4 * h0
Rconf = sp.simplify((hconf.inv() * ricci(hconf, [th, x, y])).trace())
print("   R(psi^4 h0)*psi^5 - (-8 psi'' - 2 f'^2 psi) =",
      sp.simplify(Rconf * psi**5 - (-8 * psi.diff(th, 2) - 2 * f.diff(th)**2 * psi)))

"""ITEM G: exact check (random rational 3-jets) of the weighted Bochner IDENTITY used in thm:OT,
for U=(X,Y): (B^2, gamma=e^{2phi}(dt^2+dz^2), e^sigma dmu) -> H^2 (curvature -1):

  (1/2) L e = |Nabla dU|^2 + div_sigma V - |F|^2 + tr_gamma( A o (Ric_B - Hess sigma) ) + 2 det(gamma^-1 A),

with L = Delta + <grad sigma, grad .>, e=|dU|^2, A=U^*h, F=tau_sigma(U), V = <dU(.),F>.
"""
import random
import sympy as sp

random.seed(11)
t, z = sp.symbols('t z')
co = [t, z]


def rpoly(deg, positive_const=False):
    p = 0
    for i in range(deg + 1):
        for j in range(deg + 1 - i):
            c = sp.Rational(random.randint(-9, 9), random.randint(3, 9))
            if i == j == 0 and positive_const:
                c = sp.Rational(random.randint(5, 9), 4)
            p += c * t**i * z**j
    return p


for trial in range(5):
    phi, sig = rpoly(3), rpoly(3)
    X, Y = rpoly(4), rpoly(4, positive_const=True)
    U = [X, Y]
    gam = sp.exp(2 * phi)                      # gamma_ij = gam * delta_ij
    sq = gam                                   # sqrt(det gamma)
    # base Christoffel for conformally flat metric
    dphi = [sp.diff(phi, c) for c in co]

    def Gam(k, i, j):
        return (dphi[j] if k == i else 0) + (dphi[i] if k == j else 0) - (dphi[k] if i == j else 0)
    # target Christoffel (upper half plane)
    def GT(a, b, c):
        if a == 0 and {b, c} == {0, 1}:
            return -1 / Y
        if a == 1 and b == c == 0:
            return 1 / Y
        if a == 1 and b == c == 1:
            return -1 / Y
        return 0
    hT = 1 / Y**2                              # h_ab = hT * delta_ab
    dU = [[sp.diff(U[a], c) for c in co] for a in range(2)]
    # Hessian of the map
    Hs = [[[sp.diff(U[a], co[i], co[j]) - sum(Gam(k, i, j) * dU[a][k] for k in range(2))
            + sum(GT(a, b, c) * dU[b][i] * dU[c][j] for b in range(2) for c in range(2))
            for j in range(2)] for i in range(2)] for a in range(2)]
    dsig = [sp.diff(sig, c) for c in co]
    F = [sum(Hs[a][i][i] for i in range(2)) / gam + sum(dsig[i] * dU[a][i] for i in range(2)) / gam for a in range(2)]
    e = sum(hT * dU[a][i] * dU[a][i] for a in range(2) for i in range(2)) / gam
    Le = sum(sp.diff(e, c, 2) for c in co) / gam + sum(dsig[i] * sp.diff(e, co[i]) for i in range(2)) / gam
    V = [sum(hT * dU[a][i] * F[a] for a in range(2)) / gam for i in range(2)]      # V^i
    divV = sum(sp.diff(sq * sp.exp(sig) * V[i], co[i]) for i in range(2)) / (sq * sp.exp(sig))
    normH = sum(hT * Hs[a][i][j]**2 for a in range(2) for i in range(2) for j in range(2)) / gam**2
    F2 = sum(hT * F[a]**2 for a in range(2))
    A = sp.Matrix(2, 2, lambda i, j: sum(hT * dU[a][i] * dU[a][j] for a in range(2)))
    RicB = -sum(sp.diff(phi, c, 2) for c in co) * sp.eye(2)                           # Ric of e^{2phi} delta
    HessSig = sp.Matrix(2, 2, lambda i, j: sp.diff(sig, co[i], co[j]) - sum(Gam(k, i, j) * dsig[k] for k in range(2)))
    trARic = sum(A[i, j] * (RicB - HessSig)[i, j] for i in range(2) for j in range(2)) / gam**2
    detA = (A / gam).det()
    lhs = Le / 2
    rhs = normH + divV - F2 + trARic + 2 * detA
    val = sp.simplify((lhs - rhs).subs({t: 0, z: 0}))
    print(f"trial {trial}: (1/2)L e - RHS at the origin =", val)

"""Local Ricci and normalization checks for the signature/collar diagnostic.

This does not certify global topology or existence of nonzero-signature bundles.
Run: python round20_construction_check.py (requires SymPy).
"""

import sympy as s


def simp(v):
    return s.factor(s.cancel(s.expand(v)))


def connection(metric, coords):
    n = len(coords)
    inv = metric.inv().applyfunc(simp)
    gamma = [[[s.S.Zero for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(i, n):
                value = simp(sum(inv[k, l] * (
                    s.diff(metric[l, j], coords[i])
                    + s.diff(metric[l, i], coords[j])
                    - s.diff(metric[i, j], coords[l])) for l in range(n)) / 2)
                gamma[k][i][j] = gamma[k][j][i] = value
    return inv, gamma


def ricci(metric, coords):
    n = len(coords)
    inv, gamma = connection(metric, coords)
    result = s.zeros(n)
    for i in range(n):
        for j in range(i, n):
            value = sum(
                s.diff(gamma[k][i][j], coords[k])
                - s.diff(gamma[k][i][k], coords[j])
                + sum(gamma[k][i][j] * gamma[l][k][l]
                      - gamma[l][i][k] * gamma[k][j][l] for l in range(n))
                for k in range(n))
            result[i, j] = result[j, i] = simp(value)
    return result


def zero_matrix(matrix, label):
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            assert simp(matrix[i, j]) == 0, (label, i, j, simp(matrix[i, j]))
    print("PASS:", label)


# Both base and fibre have curvature -1. Pull back the fibre by
# (u,v) -> (u, v + z*u), with z = t*r. The fibre area e^u du dv is fixed.
# This is a local diffeomorphism variation, used only for tensor checks.
t, r, u, v = s.symbols("t r u v", real=True)
coords = [t, r, u, v]
z = t*r
b = s.diag(1, s.exp(2*t))
h = s.Matrix([[1 + s.exp(2*u)*z*z, s.exp(2*u)*z],
              [s.exp(2*u)*z, s.exp(2*u)]])
metric = s.diag(b, h)
ib, gb = connection(b, [t, r])
ih, gh = connection(h, [u, v])
shapes = [(ih*h.diff(y)/2).applyfunc(simp) for y in [t, r]]
assert all(simp(S.trace()) == 0 for S in shapes)
zero_matrix(ricci(b, [t, r])+b, "base curvature -1")
zero_matrix(ricci(h, [u, v])+h, "fibre curvature -1")
assert simp(h.det()-s.exp(2*u)) == 0

expected = s.zeros(4)
for a in range(2):
    for c in range(2):
        expected[a, c] = -s.trace(shapes[a]*shapes[c])
    for i in range(2):
        # div S as a covector, using T_ji = h_jk S^k_i.
        cov = h*shapes[a]
        value = sum(ih[j, k] * (
            s.diff(cov[j, i], coords[k+2])
            - sum(gh[l][k][j]*cov[l, i] + gh[l][k][i]*cov[j, l]
                  for l in range(2))) for j in range(2) for k in range(2))
        expected[a, i+2] = expected[i+2, a] = simp(value)

div_s = s.zeros(2)
for a in range(2):
    for c in range(2):
        ds = shapes[c].diff(coords[a]) + shapes[a]*shapes[c] - shapes[c]*shapes[a]
        ds -= sum((gb[d][a][c]*shapes[d] for d in range(2)), s.zeros(2))
        div_s += ib[a, c]*ds
expected[2:4, 2:4] = -h*div_s
actual = ricci(metric, coords)+metric
zero_matrix(actual-expected, "all 16 entries of the two-direction Ricci defect")
Q = sum(ib[a, c]*s.trace(shapes[a]*shapes[c]) for a in range(2) for c in range(2))
assert simp(s.trace(ib*actual[:2, :2])+Q) == 0
assert simp(s.trace(ih*actual[2:4, 2:4])) == 0
assert simp(s.trace(metric.inv()*actual)+Q) == 0
assert simp(actual[0, 0]) != 0
assert any(simp(actual[a, i]) != 0 for a in range(2) for i in range(2, 4))
print("PASS: horizontal/vertical traces; omitted quadratic or mixed blocks rejected")

# The vertical-connection characteristic normalization for TT directions.
a, c = s.symbols("a c", real=True)
J = s.Matrix([[0, -1], [1, 0]])
A = s.diag(a, -a)
B = s.Matrix([[0, c], [c, 0]])
R_st = -(A*B-B*A)/4
R_uv = J
omega = s.trace(J*A*B)
pontryagin_numerator = 2*s.trace(R_st*R_uv)
assert simp(pontryagin_numerator+omega) == 0
assert simp(omega-2*a*c) == 0
print("PASS: tr(R wedge R) = -Omega_T in the stated tensor L2 convention")

kappa, chi, tau, delta = s.symbols("kappa chi tau delta", positive=True)
V0 = 4*s.pi**2*chi/kappa**2
gap = 6*s.pi**2*tau/(kappa*V0)
assert simp(gap/kappa-3*tau/(2*chi)) == 0
required_volume = (4*s.pi**2*chi+6*s.pi**2*tau)/(kappa*(kappa+delta))
assert simp((1+delta/kappa)*required_volume/V0-1-3*tau/(2*chi)) == 0
print("PASS: signature-gap and variable-base-volume constants")

# Finite incidence and Betti arithmetic only, not the external group embeddings.
pairs = [{i, (i+1) % 5} for i in range(5)]
disjoint_edges = {frozenset((i, j)) for i in range(5) for j in range(i+1, 5)
                  if pairs[i].isdisjoint(pairs[j])}
cycle = [0, 2, 4, 1, 3]
assert disjoint_edges == {frozenset((cycle[i], cycle[(i+1) % 5])) for i in range(5)}
fiber_chi = (2-6) + 6*(-1)
assert fiber_chi == 2-2*6
total_chi = fiber_chi*(2-2*2)
first_betti = 2*6 + 2*2
second_betti = total_chi-2+2*first_betti
assert (total_chi, first_betti, second_betti, second_betti//2) == (20, 16, 50, 25)
print("PASS: separating-curve incidence C5 and faithful-Torelli target invariants")
print("All finite checks passed; global proof and scope are in round20_construction.md.")

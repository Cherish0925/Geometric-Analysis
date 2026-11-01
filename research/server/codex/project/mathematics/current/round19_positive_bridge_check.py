"""Exact finite algebra supporting round19_positive_bridge.md; no PDE claim."""

from fractions import Fraction as F
from itertools import product


def qmul(a, b):
    w, x, y, z = a
    v, p, q, r = b
    return (w*v-x*p-y*q-z*r, w*p+x*v+y*r-z*q,
            w*q-x*r+y*v+z*p, w*r+x*q-y*p+z*v)


def matrix_for(action):
    basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    columns = [action(v) for v in basis]
    return tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))


def rank(columns):
    rows = [list(map(F, row)) for row in zip(*columns)]
    pivot = 0
    for col in range(len(columns)):
        found = next((i for i in range(pivot, len(rows)) if rows[i][col]), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        factor = rows[pivot][col]
        rows[pivot] = [x/factor for x in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot:
                factor = rows[i][col]
                rows[i] = [x-factor*y for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
    return pivot


def conjugate(q):
    return (q[0], -q[1], -q[2], -q[3])


c = matrix_for(conjugate)
assert tuple(c[i][i] for i in range(4)) == (1, -1, -1, -1)
generators = [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
left = [matrix_for(lambda v, q=q: qmul(q, v)) for q in generators]
right = [matrix_for(lambda v, q=q: qmul(v, q)) for q in generators]
for l, r in zip(left, right):
    assert matmul(matmul(c, l), c) == tuple(tuple(-x for x in row) for row in r)
flat = [tuple(x for row in m for x in row) for m in left + right]
assert rank(flat) == 6  # The imaginary left and right spans intersect trivially.
print("PASS quaternionic factor exchange and scalar intersection")

# Inverse of the negative A2 intersection matrix and its discriminant group.
q = ((-2, 1), (1, -2))
qinv = ((F(-2, 3), F(-1, 3)), (F(-1, 3), F(-2, 3)))
assert all(sum(q[i][k]*qinv[k][j] for k in range(2)) == int(i == j)
           for i in range(2) for j in range(2))
assert all(k*k % 3 != 2 for k in (1, 2))
print("PASS A2 discriminant linking form has no orientation-reversing isometry")

ade = [(f"A{r}", r, r+1) for r in range(1, 21)]
ade += [(f"D{r}", r, 4*(r-2)) for r in range(4, 21)]
ade += [("E6", 6, 24), ("E7", 7, 48), ("E8", 8, 120)]
for name, r, order in ade:
    core_chi = F(r+1) - F(1, order)
    core_tau = -F(2, 3)*core_chi
    eta_lv = F(2-r, 3) - F(2, 3*order)
    assert -r - eta_lv == core_tau
    assert (eta_lv == 0) == (name == "A1")
    chi = F(2, order) + 2*core_chi
    assert chi == 2+2*r
    assert F(4, order) + 4*core_chi == 2*chi
    assert 2*(2+2*r) - 3*(2*r) == 4-2*r
print(f"PASS modified curvature budget for {len(ade)} ADE examples")

# F is separately strictly concave in each eigenvalue, so its minimum on
# the Ricci box occurs at a vertex. Verify all equality vertices exactly.
zeros = []
for eigenvalues in product((F(1, 2), F(3, 2)), repeat=4):
    total = sum(eigenvalues)
    squares = sum(x*x for x in eigenvalues)
    density = (total*total - 3*squares)/6
    assert density >= 0
    if density == 0:
        zeros.append(eigenvalues)
assert len(zeros) == 4
assert all(sorted(e) == [F(1, 2)]*3 + [F(3, 2)] for e in zeros)
for k in range(4, 21):
    assert 2*(k+2) - 3*k == 4-k <= 0
print("PASS all Ricci-box vertices and the four simple-eigenline equality patterns")
print("All finite checks passed; no analytic gluing or Einstein existence claim.")

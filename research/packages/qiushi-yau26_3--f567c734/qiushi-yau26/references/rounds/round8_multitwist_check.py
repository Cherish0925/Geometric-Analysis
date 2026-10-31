"""Exact full-Ricci and presentation checks for round8_multitwist.md.

Run: qiushi-yau26 env numeric python round8_multitwist_check.py
This checks algebraic inputs, not an all-metrics Einstein obstruction.
"""

import sympy as s
from sympy.combinatorics.free_groups import free_group


def check(value, label):
    assert value, label
    print(f"PASS {label}")


# Independent Koszul-frame curvature calculation. The orthonormal coframe
# satisfies dω1=k ω0∧ω1 and dω3=j ω2∧ω3+v ω0∧ω2.
t, u = s.symbols("t u", real=True)
j, k = s.Function("j")(u), s.Function("k")(t)
v = s.Function("v")(t, u)
c = s.MutableDenseNDimArray.zeros(4, 4, 4)
for i, l, h, value in [(0, 1, 1, -k), (2, 3, 3, -j), (0, 2, 3, -v)]:
    c[i, l, h], c[l, i, h] = value, -value
Gamma = s.MutableDenseNDimArray.zeros(4, 4, 4)
for i in range(4):
    for l in range(4):
        for h in range(4):
            Gamma[i, l, h] = (c[i, l, h]-c[l, h, i]+c[h, i, l])/2


def deriv(i, f):
    return s.diff(f, t) if i == 0 else s.diff(f, u) if i == 2 else 0


def curvature(i, l, h, z):
    return (deriv(i, Gamma[l, h, z])-deriv(l, Gamma[i, h, z])
            + sum(Gamma[l, h, m]*Gamma[i, m, z]
                  - Gamma[i, h, m]*Gamma[l, m, z]
                  - c[i, l, m]*Gamma[m, h, z] for m in range(4)))


ric = s.Matrix(4, 4, lambda l, h: sum(curvature(i, l, h, i) for i in range(4)))
relations = {s.diff(j, u): 1-j*j, s.diff(k, t): 1-k*k}
defect = (ric+s.eye(4)).applyfunc(lambda x: s.simplify(x.subs(relations)))
mixed_f = (s.diff(v, u)+2*j*v)/2
mixed_t = -(s.diff(v, t)+k*v)/2
expected = s.Matrix([
    [-v*v/2, 0, 0, mixed_f],
    [0, 0, 0, 0],
    [0, 0, -v*v/2, mixed_t],
    [mixed_f, 0, mixed_t, v*v/2],
])
for i in range(4):
    for l in range(4):
        check(s.simplify(defect[i, l]-expected[i, l]) == 0,
              f"full Ricci block ({i},{l})")
check(s.simplify(s.trace(ric).subs(relations)+4+v*v/2) == 0,
      "scalar curvature -4-v²/2")
check(s.simplify(curvature(0, 3, 3, 0)-v*v/4) == 0,
      "positive mixed sectional curvature v²/4")

# The off-diagonal error is a symmetric rank-two star: its exact
# operator norm is sqrt(x²+y²), not a coordinate component estimate.
x, y, lam = s.symbols("x y lam", real=True)
star = s.Matrix([[0, 0, 0, x], [0, 0, 0, 0],
                 [0, 0, 0, y], [x, 0, y, 0]])
check(s.expand((lam*s.eye(4)-star).det()-lam**2*(lam**2-x*x-y*y)) == 0,
      "off-diagonal operator-norm polynomial")

# Coefficient derivatives see k=b'/b, never the collapsing factor 1/b.
ell = s.symbols("ell", positive=True)
b = ell*s.cosh(t)
check(s.simplify(s.diff(b, t)/b-s.tanh(t)) == 0,
      "shrinking circle has bounded connection coefficient")
check(s.simplify(s.diff(b, t, 2)/b-1) == 0,
      "base collar curvature independent of ell")
Q, dz = s.symbols("Q dz", real=True)
coframe = s.Matrix([[1, 0, 0, 0], [0, b, 0, 0],
                    [0, 0, 1, 0], [0, 0, Q*dz, s.cosh(u)]])
check(s.simplify(coframe.det()-b*s.cosh(u)) == 0,
      "shear preserves product volume density")

# Each based Dehn twist preserves the entire surface relator.
for p in range(2, 6):
    names = " ".join(f"a{i} b{i}" for i in range(p))
    group_and_gens = free_group(names)
    F, gens = group_and_gens[0], group_and_gens[1:]
    comm = lambda a, bb: a*bb*a**-1*bb**-1
    relator = F.identity
    for i in range(p):
        relator *= comm(gens[2*i], gens[2*i+1])
    for twist in range(p):
        image = F.identity
        for i in range(p):
            a, bb = gens[2*i:2*i+2]
            image *= comm(a, bb*a if i == twist else bb)
        check(image == relator, f"independent twist preserves relator p={p}, i={twist+1}")
        dual_image = F.identity
        for i in range(p):
            a, bb = gens[2*i:2*i+2]
            dual_image *= comm(a*bb**-1 if i == twist else a, bb)
        check(dual_image == relator, f"dual twist preserves relator p={p}, i={twist+1}")
    I = s.eye(2*p)
    a_twists, b_twists = [], []
    for i in range(p):
        ta, tb = I.copy(), I.copy()
        ta[2*i, 2*i+1] = 1
        tb[2*i+1, 2*i] = -1
        a_twists.append(ta)
        b_twists.append(tb)
    for r in range(1, p+1):
        coinvariant_relations = s.Matrix.hstack(*(ta-I for ta in a_twists[:r]))
        check(coinvariant_relations.rank() == r,
              f"rank-r fibre homology loss p={p}, r={r}")
    full_relations = s.Matrix.hstack(*(tt-I for tt in a_twists+b_twists))
    check(full_relations.rank() == 2*p, f"full-generator fibre homology loss p={p}")
    check(a_twists[0]*b_twists[0] != b_twists[0]*a_twists[0],
          f"full-generator monodromies really noncommute p={p}")

# Full rank dependence, including residual torus and free-group cases.
for p in range(2, 8):
    for q in range(2, 8):
        for r in range(1, min(p, q)+1):
            h = p-r
            fiber_cap = max(2*h-2, 0)
            base_cap = 2*q-2
            cap = fiber_cap*base_cap
            check(cap == 4*max(p-r-1, 0)*(q-1),
                  f"Euler-product cap p={p}, q={q}, r={r}")
            if r >= p-1:
                check(cap == 0, f"all representation volumes vanish p={p}, q={q}, r={r}")

print("All exact checks passed. Global gluing and group proofs are in the note.")

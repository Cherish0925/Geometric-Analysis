"""
Step 50: does the classical Z_2^3 Campedelli component contain a 6-nodal
canonical model?

Background used (source-level, not proved here):
  Alexeev-Pardini, "Explicit compactifications ...", Definition 3.1 and
  Lemma 3.4:  a Campedelli surface is the Z_2^3-cover X -> P^2 with building
  data seven lines D_g, g in Z_2^3 \ {0}.  The cover has canonical (Du Val)
  singularities iff either the seven lines are in general position (X smooth)
  or, at every point where exactly three of the lines D_{g1},D_{g2},D_{g3}
  meet, the labels g1,g2,g3 generate Z_2^3.  In that concurrent case the cover
  acquires one A_1 point.  If instead g1+g2+g3=0 the cover acquires two
  1/4(1,1) points, which are NOT canonical.  Also K_X = pi^*(h/2) so K_X^2 = 2,
  p_g = q = 0, and 2K_X is the pullback of a line: K_X is ample.

So the finite question decided here is purely projective/combinatorial:

  (Q) Is there an arrangement of 7 distinct lines in P^2 over Q, with exactly
      6 triple points, no point of multiplicity >= 4, no two lines equal, and
      a labelling of the lines by the seven nonzero elements of Z_2^3 such
      that the three labels at each of the six triple points form a basis?

A positive answer produces a canonical Campedelli model with exactly six A_1
points inside the classical component M_Cam, whose general member is a smooth
Campedelli surface with ample canonical class.

Everything is exact integer arithmetic in homogeneous coordinates.
"""
from itertools import combinations, permutations
from math import gcd

# ---------------------------------------------------------------- projective
def norm(v):
    a, b, c = v
    g = gcd(gcd(abs(a), abs(b)), abs(c))
    if g == 0:
        raise ValueError("zero vector")
    a, b, c = a // g, b // g, c // g
    for t in (a, b, c):
        if t != 0:
            if t < 0:
                a, b, c = -a, -b, -c
            break
    return (a, b, c)

def cross(u, v):
    return norm((u[1]*v[2] - u[2]*v[1],
                 u[2]*v[0] - u[0]*v[2],
                 u[0]*v[1] - u[1]*v[0]))

def on(line, pt):
    return line[0]*pt[0] + line[1]*pt[1] + line[2]*pt[2] == 0

# ------------------------------------------------------- candidate arrangement
# Six lines of the A_3 (S_4) reflection arrangement, plus one line through two
# of its double points, chosen so that two double points become triple points.
LINES = {
    "x":     (1, 0, 0),
    "y":     (0, 1, 0),
    "z":     (0, 0, 1),
    "x-y":   (1, -1, 0),
    "y-z":   (0, 1, -1),
    "x-z":   (1, 0, -1),
    "x-y+z": (1, -1, 1),
}
names = list(LINES)
vals = [LINES[n] for n in names]
assert len(set(map(norm, vals))) == 7, "lines must be distinct"

# all intersection points with their incident line index sets
pts = {}
for i, j in combinations(range(7), 2):
    p = cross(vals[i], vals[j])
    pts.setdefault(p, set()).update({i, j})
for p, inc in pts.items():
    for k in range(7):
        if on(vals[k], p):
            inc.add(k)

mult = {p: len(inc) for p, inc in pts.items()}
triples = sorted(p for p in pts if mult[p] == 3)
higher = [p for p in pts if mult[p] >= 4]

print("arrangement lines:", names)
print("number of intersection points:", len(pts))
print("multiplicity census:", {m: sum(1 for q in mult.values() if q == m)
                              for m in sorted(set(mult.values()))})
print("triple points:", triples)
print("points of multiplicity >= 4:", higher)

assert not higher, "no point of multiplicity >= 4 is allowed"
assert len(triples) == 6, f"expected 6 triple points, found {len(triples)}"

# Combinatorial check: sum of C(m,2) over points must equal C(7,2) = 21.
assert sum(m*(m-1)//2 for m in mult.values()) == 21

triple_index_sets = [tuple(sorted(pts[p])) for p in triples]
print("triple point line-index sets:", triple_index_sets)

# -------------------------------------------------------------- Z_2^3 labels
NONZERO = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)
           if (a, b, c) != (0, 0, 0)]
assert len(NONZERO) == 7

def independent(g1, g2, g3):
    # over F_2, three nonzero distinct vectors are a basis iff g1+g2+g3 != 0
    s = tuple((g1[k] + g2[k] + g3[k]) % 2 for k in range(3))
    return s != (0, 0, 0)

good = []
for perm in permutations(NONZERO):
    if all(independent(perm[i], perm[j], perm[k])
           for (i, j, k) in triple_index_sets):
        good.append(perm)

print("number of valid labellings (all six triples a basis):", len(good))
if good:
    lab = good[0]
    print("one valid labelling:")
    for n, g in zip(names, lab):
        print(f"   line {n:6s} -> label {g}")
    for (i, j, k), p in zip(triple_index_sets, triples):
        s = tuple((lab[i][t] + lab[j][t] + lab[k][t]) % 2 for t in range(3))
        print(f"   triple {p} labels {lab[i]},{lab[j]},{lab[k]} sum {s}")

assert good, "no admissible labelling: the six-nodal canonical model would fail"
print("RESULT: a six-nodal canonical Campedelli model exists in the classical "
      "Z_2^3 component (all six concurrences give A_1 points).")

"""Finite combinatorial checks for Step 45 coefficient weights.

This checks derivative partitions and scalar coefficient identities only.  It
cannot verify tensor contractions, PDE existence, signed integration by parts,
or any geometric theorem.
"""
from itertools import product

checks = 0

def ok(cond, label):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(label)

# Coefficient identities for representative chi, epsilon.
for chi in [0.0, 0.1, 0.6, 1.0]:
    for eps in [0.01, 0.2, 1.0]:
        b = chi * chi + eps * eps
        ok(0 <= chi * chi / b <= 1 + 1e-14, "chi^2/b")
        ok(4 * chi * chi / b <= 4 + 1e-14, "|db|^2/b coefficient")

# U3 partitions B_{r+1} B_{s+1} T_t at each m.
for m in range(0, 13):
    parts = [(r, s, t) for r in range(m + 1) for s in range(m + 1)
             for t in range(m + 1) if r + s + t == m]
    # Current T_m only r=s=0.
    current_t = [(r, s, t) for r, s, t in parts if t == m]
    ok(current_t == [(0, 0, m)], f"U3 current T at m={m}")
    # A C_{m+1} can only come from B_{m+1}, hence exactly the two allocations.
    top_b = [(r, s, t) for r, s, t in parts if r == m or s == m]
    expected = [(0, m, 0)] if m == 0 else [(0, m, 0), (m, 0, 0)]
    # Remove duplicate at m=0.
    top_b = list(dict.fromkeys(top_b))
    expected = list(dict.fromkeys(expected))
    ok(sorted(top_b) == sorted(expected), f"U3 current cutoff at m={m}")

# Time commutator partitions: r+s=m-1 gives max U derivative m, never m+1.
for m in range(1, 15):
    parts = [(r, s) for r in range(m) for s in range(m) if r + s == m - 1]
    ok(max(r + 1 for r, _ in parts) == m, f"time commutator U max m={m}")
    ok(all(s <= m - 1 for _, s in parts), f"time commutator companion prior m={m}")

# Cutoff Leibniz: for k>=2 all proper positive partitions have orders <=k-1.
for k in range(2, 20):
    proper = [(i, k-i) for i in range(1, k)]
    ok(all(max(i, j) <= k - 1 for i, j in proper), f"B_k proper jets k={k}")

# Current U_m from U spatial commutator b Rm_r U_s: if r=m,s=0,
# b T_m is converted by Leibniz; if r=0,s=m, b Rm is bounded by U-bG.
for m in range(1, 15):
    parts = [(r, s) for r in range(m + 1) for s in range(m + 1) if r+s == m]
    extremes = [(r, s) for r, s in parts if r == m or s == m]
    ok(sorted(extremes) == sorted([(0, m), (m, 0)]), f"U5 extremes m={m}")

print(f"{checks}/{checks} scalar and partition checks passed")
print("NOT CHECKED: tensor provenance, numerical coefficients, signed contractions, PDE existence, compactness, or Yau 26.")

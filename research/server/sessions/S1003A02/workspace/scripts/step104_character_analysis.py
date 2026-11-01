"""Step 104: boundary character analysis for Wahl spin^c extensions.

For a Wahl ball B_{n,1} embedded in M = X#kCP̄² via a four-coordinate block
with realization vector v = (v1,...,v4), |v|² = n², the restriction of a
basic class c = K_X + ε₁E₁ + ... + εkEk to ∂B = L(n²,n-1) has boundary
character j(c) = Σ_{i∈block} εᵢvᵢ mod n².

The class extends to an orbifold spin^c structure on V iff j(c) ≡ 0 mod n.
We enumerate:
  (a) all four-square representations of n² for 2 ≤ n ≤ 16,
  (b) all 16 sign choices ε ∈ {±1}⁴,
  (c) the coset j mod n for each,
and verify that j ≡ 0 mod n is always achievable.

Output: workspace/data/step104/character_analysis.json
"""
import json, os
from itertools import product

def four_squares(N):
    """Return all (v1,v2,v3,v4) with vi ≥ 0 and v1²+...+v4² = N, up to ordering."""
    reps = []
    for a in range(int(N**0.5)+1):
        for b in range(a, int(N**0.5)+1):
            for c in range(b, int(N**0.5)+1):
                d2 = N - a*a - b*b - c*c
                if d2 < 0: continue
                d = int(round(d2**0.5))
                if d*d == d2 and d >= c:
                    reps.append((a,b,c,d))
    return reps

results = {}
for n in range(2, 17):
    N = n*n
    reps = four_squares(N)
    row = {"n": n, "N": N, "representations": []}
    for v in reps:
        # all 16 sign choices
        cosets = set()
        extending = []  # sign choices with j ≡ 0 mod n
        for signs in product([-1,1], repeat=4):
            j = sum(s*vi for s,vi in zip(signs, v))
            coset = j % n
            cosets.add(coset)
            if coset == 0:
                extending.append({"signs": list(signs), "j_mod_n2": j % N})
        # Also record the "all positive" class
        j_all_pos = sum(v) % N
        j_all_pos_mod_n = sum(v) % n
        
        entry = {
            "v": list(v),
            "norm_sq": sum(x*x for x in v),
            "cosets_achieved": sorted(cosets),
            "num_extending": len(extending),
            "all_positive_j_mod_n": j_all_pos_mod_n,
            "all_positive_j_mod_n2": j_all_pos,
            "has_extending_class": len(extending) > 0,
        }
        row["representations"].append(entry)
    
    # Summary: does every representation have an extending class?
    all_have_extending = all(e["has_extending_class"] for e in row["representations"])
    row["all_representations_have_extending_class"] = all_have_extending
    row["num_representations"] = len(reps)
    results[str(n)] = row

# Also check: for n=3 with v=(2,2,1,0), which is a typical realization,
# the "all positive" class has j = 5 mod 9, j mod 3 = 2 (NOT extending).
# But j = 2+2-1+0 = 3 ≡ 0 mod 3 (extending).
# This shows the sign freedom suffices.

od = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step104')
os.makedirs(od, exist_ok=True)
outpath = os.path.join(od, 'character_analysis.json')
with open(outpath, 'w') as f:
    json.dump(results, f, indent=1)

# Print summary
fail_count = 0
for n_str, row in sorted(results.items(), key=lambda x: int(x[0])):
    n = int(n_str)
    ok = row["all_representations_have_extending_class"]
    if not ok:
        fail_count += 1
    # Find a non-extending all-positive example
    non_ext = [e for e in row["representations"] if e["all_positive_j_mod_n"] != 0]
    ext_count = sum(1 for e in row["representations"] if e["has_extending_class"])
    print(f"n={n:2d}: {row['num_representations']:3d} reps, all have extending: {ok}, "
          f"all-positive non-extending: {len(non_ext)}/{row['num_representations']}")

print(f"\nFailed (no extending class exists for some rep): {fail_count}")
print(f"Wrote {outpath}")

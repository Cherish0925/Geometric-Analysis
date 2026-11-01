"""
Step 50: character calculation for the BCGP K^2=2, G=Z_4^2 product-quotient row.

Purpose
-------
Use the actual two spherical generating triples displayed in BCGP §6.7, not only
that both signatures are (4,4,4), to compute the equivariant Hodge pieces that
enter the sufficient obstruction-vanishing test

    H^2(T_S)=0  <=>  H^0(Omega^1_S \otimes K_S)=0

for the minimal resolution S of X=(C1 x C2)/G with only A1 singularities.
For rational double points the quotient/resolution comparison is a separate
geometric input; this script only performs finite character arithmetic.

Conventions
-----------
G = Z_4^2 written additively. Characters are also pairs (a,b) mod 4 with
chi_{a,b}(x,y)=exp(2 pi i (a x + b y)/4).

BCGP §6.7 gives the branch monodromy triples:
    S1 = [(1,3), (1,0), (2,1)]
    S2 = [(3,2), (0,1), (1,1)]
Each element has order 4 and each triple sums to zero.

For an abelian G-cover C -> P^1 with branch monodromies e_i and quotient genus
0, the Chevalley-Weil dimension for a nontrivial character chi in H^0(K_C) is
    dim H^0(K_C)_chi = -1 + sum_i frac(<chi,e_i>/4),
where <chi,e_i> is represented by 0,1,2,3.  In this example all dimensions are
0 or 1 and sum to genus 3.

The curves are non-hyperelliptic: every order-two element fixes at most 4
points, so no involution has the 8 fixed points required for a genus-3
hyperelliptic involution. Hence multiplication Sym^2 H^0(K_C) -> H^0(2K_C) is
an isomorphism, and the 2K character decomposition is computed as Sym^2.
"""
from collections import Counter
from itertools import product

MOD = 4
G = [(a, b) for a in range(MOD) for b in range(MOD)]
zero = (0, 0)
S1 = [(1, 3), (1, 0), (2, 1)]
S2 = [(3, 2), (0, 1), (1, 1)]

def add(x, y):
    return ((x[0] + y[0]) % MOD, (x[1] + y[1]) % MOD)

def neg(x):
    return ((-x[0]) % MOD, (-x[1]) % MOD)

def pair(ch, g):
    return (ch[0] * g[0] + ch[1] * g[1]) % MOD

def order(g):
    if g == zero:
        return 1
    cur = zero
    for k in range(1, 9):
        cur = add(cur, g)
        if cur == zero:
            return k
    raise AssertionError("order not found")

def canonical_chars(branch):
    assert add(add(branch[0], branch[1]), branch[2]) == zero
    assert all(order(e) == 4 for e in branch)
    out = Counter()
    for ch in G:
        if ch == zero:
            continue
        residues = [pair(ch, e) for e in branch]
        # The sum is divisible by 4 because sum branch monodromies is zero.
        dim_num = sum(residues) - 4
        assert dim_num % 4 == 0, (ch, residues, dim_num)
        dim = dim_num // 4
        if dim:
            assert dim > 0
            out[ch] = dim
    return out

def sym2_chars(V):
    # V is a character multiplicity Counter.  Compute Sym^2(V).
    chars = []
    for ch, m in V.items():
        chars.extend([ch] * m)
    out = Counter()
    for i, chi in enumerate(chars):
        for j in range(i, len(chars)):
            psi = chars[j]
            out[add(chi, psi)] += 1
    return out

def invariant_dim(A, B):
    return sum(m * B.get(neg(ch), 0) for ch, m in A.items())

def involution_fixed_counts(branch):
    invs = [g for g in G if order(g) == 2]
    counts = {}
    for h in invs:
        count_branch = 0
        for e in branch:
            # h lies in <e> iff h = 2e for order-4 e in this setup.
            if h == add(e, e):
                count_branch += 1
        # Each branch point has |G|/4 = 4 points above it.
        counts[h] = 4 * count_branch
    return counts

VK1 = canonical_chars(S1)
VK2 = canonical_chars(S2)
V2K1 = sym2_chars(VK1)
V2K2 = sym2_chars(VK2)

assert sum(VK1.values()) == 3
assert sum(VK2.values()) == 3
assert sum(V2K1.values()) == 6
assert sum(V2K2.values()) == 6
assert max(involution_fixed_counts(S1).values()) == 4
assert max(involution_fixed_counts(S2).values()) == 4

term_21 = invariant_dim(V2K1, VK2)
term_12 = invariant_dim(VK1, V2K2)
total = term_21 + term_12

print("BCGP Z4^2 K^2=2 row actual branch triples")
print("S1 =", S1)
print("S2 =", S2)
print("H^0(K_C1) characters:", sorted(VK1.items()))
print("H^0(K_C2) characters:", sorted(VK2.items()))
print("H^0(2K_C1)=Sym^2 H^0(K_C1):", sorted(V2K1.items()))
print("H^0(2K_C2)=Sym^2 H^0(K_C2):", sorted(V2K2.items()))
print("invariant dim H0(2K_C1)⊗H0(K_C2):", term_21)
print("invariant dim H0(K_C1)⊗H0(2K_C2):", term_12)
print("total invariant dim for H0(Omega^1_{C1xC2}⊗K) before RDP comparison:", total)
print("order-two fixed point counts C1:", involution_fixed_counts(S1))
print("order-two fixed point counts C2:", involution_fixed_counts(S2))

# The following conclusions are finite character consequences only.
assert total == 0, "The sufficient H^2=0 character test would fail if total were nonzero."
print("character-level sufficient obstruction vanishing test passes: total = 0")

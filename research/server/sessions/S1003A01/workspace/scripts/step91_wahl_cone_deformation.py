"""Step 91: Cone deformation modes for the Wahl singularity 1/n^2(1,n-1).

Question: does the Ricci-flat Kahler cone C^2/Z_{n^2}(1,n-1) admit
anti-Hermitian (non-Kahler) TT Einstein deformation modes at the
indicial root nu=2 (the critical order for a negative Einstein bulk)?

Method: enumerate Z_{n^2}-invariant harmonic polynomial tensor fields on C^2,
restrict to anti-Hermitian TT (traceless, divergence-free), and count
those with homogeneity degree nu=2 on the cone.

A homogeneous polynomial of degree d in (z1,zb1,z2,zb2) times a tensor
component dz_i dz_j (of homogeneity degree 2) has total cone degree d+2.
For nu=2 we need d=0 (constant times tensor component). For nu=0 we need
d=-2, impossible. So the relevant modes have polynomial degree d=0 (constants).

Actually wait: the total homogeneity of a tensor r^nu h_L means we need to
count polynomial * tensor of total degree nu. A constant tensor dz_i dz_j has
homogeneity 0 (not 2) because the *metric* components absorb the tensor weight
when restricting to the unit sphere. Let me be more careful.

On the flat cone metric g=dr^2+r^2 g_L, a TT tensor of the form
  h = r^nu * (tensor on L)
has the RADIAL part r^nu. The angular part is a TT tensor on the link L.
A polynomial tensor p(z)*dz_i dz_j on R^4 = C^2 has homogeneity
  deg(p) + 2  (since dz_i has length scaling like r^1)
when restricted to the cone. Wait no - in the cone metric, dz_i already
has norm ~r because g_cone = dr^2 + r^2 g_L. So on the unit sphere r=1,
dz_i dz_j is a fixed tensor on L.

The correct interpretation: a monomial z1^a zb1^b z2^c zb2^d dz_i dz_j
restricted to the sphere r=1 gives a tensor on L. Its radial behavior on
the cone is r^{a+b+c+d} times a fixed angular function. The tensor
component dz_i dz_j is already a tensor on the sphere at each r.

So the cone indicial exponent is nu = a+b+c+d = polynomial degree.

For nu=2: degree-2 polynomial times anti-Hermitian tensor, Z_{n^2}-invariant.
For nu=0: constant anti-Hermitian tensor, Z_{n^2}-invariant.

The Lichnerowicz equation on the cone reduces to: the polynomial tensor
must be harmonic (Delta_{R^4} h = 0 in the distributional sense away from 0),
and then the restriction to the link is automatically an eigentensor.

For a constant tensor h0 = a dz_i dz_j + cc, Delta h0 = 0 trivially.
Its TT condition is: trace(h0) = 0 and div(h0) = 0. Both hold for
constant (2,0)-tensors.

So we just need to count Z_{n^2}-invariant constant anti-Hermitian TT tensors.

Anti-Hermitian means h(JX,JY) = -h(X,Y). In complex coordinates with
J(dz_k) = i dz_k, this means h_{ij} dz^i dz^j type tensors (the (2,0)+(0,2) part).

A constant anti-Hermitian TT tensor on C^2 is:
  h = A_{ij} dz^i dz^j + conj
where A is a symmetric 2x2 complex matrix. Trace-free: A_{11}+A_{22}=0 in
the Hermitian metric (but trace of (2,0)-form in the Riemannian metric IS 0
automatically). Divergence-free: trivially for constant. So dim = 3 complex
= 6 real (A_{11}, A_{12}, A_{22} with A symmetric).

Z_{n^2} with weights (1,n-1) acts on these as:
  dz_1^2 -> zeta^2 dz_1^2
  dz_1 dz_2 -> zeta^n dz_1 dz_2
  dz_2^2 -> zeta^{2(n-1)} dz_2^2

Invariance requires the weight to be 0 mod n^2.

For dz_1^2: weight 2. 2 ≡ 0 mod n^2 iff n^2 | 2. Only n=1.
For dz_1 dz_2: weight n. n ≡ 0 mod n^2 iff n | n, which is n=1.
    Wait: n ≡ 0 mod n^2 means n^2 | n, so n | 1, n=1.
For dz_2^2: weight 2(n-1). 2(n-1) ≡ 0 mod n^2 iff n^2 | 2(n-1).
    Since gcd(n, n-1)=1, gcd(n^2, n-1)=1. So n^2 | 2. Only n=1.

CONCLUSION: For n >= 2, there are NO Z_{n^2}-invariant constant (2,0)-tensors.
The Wahl cone has NO anti-Hermitian deformation at nu=0.

Now check nu=2 (degree-2 polynomials). The candidate tensors are
  p(z,zbar) * dz_i dz_j + cc
where p has degree 2 and the whole thing is Z_{n^2}-invariant.

Total Z_{n^2} weight = (monomial weight) + (tensor weight).
Monomial z1^a zb1^b z2^c zb2^d has weight a - b + (n-1)(c - d).
Tensor weight: dz1^2 -> 2, dz1 dz2 -> n, dz2^2 -> 2(n-1).

Need total weight ≡ 0 mod n^2.

Additionally need: a+b+c+d = 2, all nonneg integers.
And: harmonic polynomial (Delta p = 0 on C^2 for the (2,0) part).
And: TT after projection.

Let me enumerate for each n.
"""

import numpy as np
from itertools import product
import json, os

def enumerate_invariant_tensors(n, deg):
    """Count Z_{n^2}-invariant degree-deg anti-Hermitian tensor monomials on C^2.
    
    Returns list of (a,b,c,d, tensor_type, total_weight_mod_n2)
    where tensor_type is '11','12','22' for dz1^2, dz1 dz2, dz2^2.
    """
    p = n * n
    tensor_weights = {'11': 2, '12': n, '22': 2*(n-1)}
    results = []
    for a, b, c, d in product(range(deg+1), repeat=4):
        if a + b + c + d != deg:
            continue
        mono_weight = (a - b + (n-1)*(c - d)) % p
        for ttype, tw in tensor_weights.items():
            total = (mono_weight + tw) % p
            if total == 0:
                results.append((a, b, c, d, ttype, 0))
    return results

def is_harmonic(a, b, c, d):
    """Check if z1^a zb1^b z2^c zb2^d is harmonic on C^2.
    
    Delta = 4(d/dz1 d/dzb1 + d/dz2 d/dzb2).
    So Delta(z1^a zb1^b z2^c zb2^d) = 4(a*b * z1^{a-1} zb1^{b-1} z2^c zb2^d
                                        + c*d * z1^a zb1^b z2^{c-1} zb2^{d-1})
    This vanishes iff a*b = 0 and c*d = 0 (for a single monomial).
    """
    return (a * b == 0) and (c * d == 0)

def check_divergence_free(a, b, c, d, ttype):
    """Check if the tensor monomial is divergence-free.
    
    For h = p(z) dz_i dz_j, divergence is d/dzbar_k (h_{ij}).
    Since h is a (2,0)-form, the Riemannian divergence involves d/dzbar.
    
    div(p dz_1^2) = (d p/dzbar_1) dz_1 + (d p/dzbar_2) dz_1 (from the second index)
    Actually: div_k h_{ij} = g^{km} nabla_m h_{ij}, and for flat C^2:
    div_1(p dz_1 dz_1) = dp/dzbar_1 (from contracting the 1-index with dzbar_1)
    div_2(p dz_1 dz_1) = 0
    
    More precisely, in flat C^2 with g = |dz_1|^2 + |dz_2|^2:
    (delta h)_j = -sum_i nabla_i h_{ij}
    For h = p dz_1 dz_1:
    (delta h)_1 = -d/dz_1(p) - d/dzbar_1(p) (??? no, need to be careful with real/complex)
    
    Actually the simplest check: for a polynomial symmetric (2,0)-tensor
    h = p_{ij}(z,zbar) dz_i dz_j on flat C^2, the divergence is
    (delta h)_j = -4 sum_i d p_{ij}/d zbar_i
    (the factor 4 from the metric conversion between real and complex coords).
    
    So for h = p dz_1^2: (delta h)_1 = -4 dp/dzbar_1, (delta h)_2 = -4 dp/dzbar_2
    Wait no: h_{11} = p, h_{12} = h_{21} = 0, h_{22} = 0.
    (delta h)_1 = -4 d h_{11}/dzbar_1 = -4 dp/dzbar_1
    (delta h)_2 = -4 d h_{12}/dzbar_1 + ... = 0
    Hmm, I need to sum over both holomorphic and anti-holomorphic indices properly.
    
    For the REAL divergence of a REAL tensor on R^4:
    In complex coords, div_j h = sum_k (dh_{jk}/dx_k) where x are real coords.
    For a (2,0)-tensor h_ij dz^i dz^j + cc:
    In real terms, this contributes to both symmetric and antisymmetric parts.
    
    For a (2,0)-form specifically: h = A dz1^2 means h(d/dz1, d/dz1) = A, and
    this is a COMPLEX tensor. The real part is Re(A dz1^2) = Re(A)(dx1^2-dy1^2) - Im(A)(2 dx1 dy1).
    
    The real divergence of the real tensor Re(A dz1^2 + ...) is computed in real coordinates.
    For a CONSTANT A: the divergence of a constant tensor is 0. Always.
    
    For a non-constant p(z,zbar) dz1^2: the divergence involves derivatives of p.
    Specifically, the real divergence of Re(p dz1^2) as a real symmetric tensor
    has components proportional to dp/dx_k for various k.
    
    For our purposes, what matters is: at degree 2, the TT projection kills some modes.
    Let me just count the raw invariants first, then we'll worry about TT.
    """
    # For constant tensors (deg=0), divergence is always 0.
    if a + b + c + d == 0:
        return True
    # For deg=2, need to check
    # The divergence of p(z,zbar) dz_i dz_j involves dp/dzbar_k
    # d/dzbar_1 of z1^a zb1^b z2^c zb2^d = b * z1^a zb1^{b-1} z2^c zb2^d
    # d/dzbar_2 of z1^a zb1^b z2^c zb2^d = d * z1^a zb1^b z2^c zb2^{d-1}
    
    # For ttype '11' (dz1 dz1):
    #   divergence_1 = d p / dzbar_1 (from h_{11})
    #   divergence_2 = 0
    # For ttype '12' (dz1 dz2):
    #   divergence_1 = d p / dzbar_2
    #   divergence_2 = d p / dzbar_1
    # For ttype '22' (dz2 dz2):
    #   divergence_1 = 0
    #   divergence_2 = d p / dzbar_2
    
    if ttype == '11':
        return b == 0  # dp/dzbar_1 = 0
    elif ttype == '12':
        return b == 0 and d == 0  # dp/dzbar_1 = dp/dzbar_2 = 0
    elif ttype == '22':
        return d == 0  # dp/dzbar_2 = 0
    return False

results = {}

for n in range(2, 11):
    p = n * n
    res_n = {'n': n, 'p': p, 'link': f'L({p},{n-1})'}
    
    # nu=0: constant (deg=0) anti-Hermitian tensors
    inv0 = enumerate_invariant_tensors(n, 0)
    res_n['nu0_raw_count'] = len(inv0)
    res_n['nu0_modes'] = inv0
    
    # nu=2: degree-2 anti-Hermitian tensors
    inv2_all = enumerate_invariant_tensors(n, 2)
    # Filter: harmonic
    inv2_harm = [(a,b,c,d,t,w) for a,b,c,d,t,w in inv2_all if is_harmonic(a,b,c,d)]
    # Filter: divergence-free (individual monomial check; for combinations need linear algebra)
    inv2_divfree = [(a,b,c,d,t,w) for a,b,c,d,t,w in inv2_harm if check_divergence_free(a,b,c,d,t)]
    
    res_n['nu2_raw_count'] = len(inv2_all)
    res_n['nu2_harmonic_count'] = len(inv2_harm)
    res_n['nu2_harmonic_divfree_count'] = len(inv2_divfree)
    
    # Group by tensor type
    for ttype in ['11', '12', '22']:
        modes = [(a,b,c,d) for a,b,c,d,t,w in inv2_divfree if t == ttype]
        res_n[f'nu2_TT_{ttype}'] = modes
    
    # Also check nu=1 and nu=3
    for nu in [1, 3, 4]:
        inv = enumerate_invariant_tensors(n, nu)
        inv_h = [x for x in inv if is_harmonic(*x[:4])]
        inv_hd = [x for x in inv_h if check_divergence_free(*x[:5])]
        res_n[f'nu{nu}_harmonic_divfree'] = len(inv_hd)
    
    results[n] = res_n
    
    print(f"\nn={n}, cone 1/{p}(1,{n-1}), link L({p},{n-1}):")
    print(f"  nu=0 (constant): {res_n['nu0_raw_count']} invariant anti-Hermitian tensors")
    print(f"  nu=1: {res_n['nu1_harmonic_divfree']} harmonic div-free")
    print(f"  nu=2: {res_n['nu2_raw_count']} raw -> {res_n['nu2_harmonic_count']} harmonic -> {res_n['nu2_harmonic_divfree_count']} div-free")
    for ttype in ['11', '12', '22']:
        modes = res_n[f'nu2_TT_{ttype}']
        if modes:
            print(f"    dz{ttype}: {modes}")
    print(f"  nu=3: {res_n['nu3_harmonic_divfree']} harmonic div-free")
    print(f"  nu=4: {res_n['nu4_harmonic_divfree']} harmonic div-free")

# Summary
print("\n\nSUMMARY: anti-Hermitian TT modes at critical indicial roots")
print(f"{'n':>3} {'nu=0':>6} {'nu=1':>6} {'nu=2':>6} {'nu=3':>6} {'nu=4':>6}")
for n in range(2, 11):
    r = results[n]
    print(f"{n:3d} {r['nu0_raw_count']:6d} {r['nu1_harmonic_divfree']:6d} "
          f"{r['nu2_harmonic_divfree_count']:6d} {r['nu3_harmonic_divfree']:6d} "
          f"{r['nu4_harmonic_divfree']:6d}")

here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step91')
os.makedirs(od, exist_ok=True)
# Convert tuples to lists for JSON
json_results = {}
for n, r in results.items():
    jr = {}
    for k, v in r.items():
        if isinstance(v, list) and v and isinstance(v[0], tuple):
            jr[k] = [list(x) for x in v]
        else:
            jr[k] = v
    json_results[n] = jr
with open(os.path.join(od, 'wahl_cone_deformation.json'), 'w') as f:
    json.dump(json_results, f, indent=1)

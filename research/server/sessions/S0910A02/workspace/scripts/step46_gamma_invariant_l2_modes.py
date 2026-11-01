"""
Step 46: Γ-invariant l=2 TT tensor harmonics on S³/Γ

For each finite Γ ⊂ SU(2) (ADE classification), compute the dimension of
the Γ-invariant subspace of the l=2 TT tensor eigenspace on S³.

The l=2 TT tensor eigenspace on S³ decomposes under SO(4) = (SU(2)_L × SU(2)_R)/Z₂
into (self-dual) and (anti-self-dual) sectors, each carrying spin-2 of the
respective SU(2) factor.

For Γ ⊂ SU(2)_L:
  - On Λ²₊ (self-dual): Γ acts by Ad, factoring through Γ/{±1} ⊂ SO(3).
    The Γ-invariant subspace of the spin-2 representation is determined by
    the character of the 5D irrep of SO(3) restricted to Γ/{±1}.
  - On Λ²₋ (anti-self-dual): Γ acts trivially. Full 5D space is invariant.

The character of the spin-j representation at rotation angle θ is:
  χ_j(θ) = sin((2j+1)θ/2) / sin(θ/2)

For j=2: χ_2(θ) = sin(5θ/2) / sin(θ/2)
"""

import numpy as np
import json

def chi_spin2(theta):
    """Character of spin-2 representation at rotation angle theta."""
    if abs(theta) < 1e-12:
        return 5.0
    return np.sin(2.5 * theta) / np.sin(0.5 * theta)

def inner_product(chi_vals, irrep_vals, class_sizes, group_order):
    """Compute inner product <chi, irrep> = (1/|G|) sum |C_k| chi(k) irrep(k)*"""
    return sum(s * c * np.conj(i) for s, c, i in zip(class_sizes, chi_vals, irrep_vals)) / group_order

def analyze_cyclic(p):
    """Z_p ⊂ SU(2), image Z_{p'} in SO(3) where p' = p/gcd(2,p)."""
    # In the spin-2 representation of SU(2), generator ζ = e^{2πi/p}
    # acts with eigenvalues ζ^{-4}, ζ^{-2}, 1, ζ^{2}, ζ^{4} (m = -2,...,2)
    # Γ-invariant: those m with e^{2πim/p} = 1 for all generators, i.e. p | 2m
    count_sd = sum(1 for m in range(-2, 3) if (2*m) % p == 0)
    return {"group": f"Z_{p}", "ADE": f"A_{p-1}", "order": 2*p,
            "sd_inv_dim": count_sd, "asd_inv_dim": 5, "total_l2_inv": count_sd + 5}

def analyze_binary_dihedral(k):
    """Binary dihedral D*_k of order 4k, image D_k in SO(3)."""
    # D_k has conjugacy classes:
    # - identity (1 element, θ=0)
    # - k-1 rotation classes of size 2 (θ = 2πj/k, j=1,...,k-1) if k≥3
    #   or 1 rotation class of size 1 (θ=π) if k=2
    # - 1 or 2 reflection classes of size k/2 or k
    # For the adjoint action on R³, reflections act as rotations by π about
    # their reflection axis
    
    group_order = 2 * k  # |D_k| in SO(3)
    
    # Build classes: D_k = <r, s | r^k=s^2=1, srs=r^{-1}>
    # Conjugacy classes: {e}, {r^j, r^{-j}} for j=1..⌊k/2⌋ (or {r^{k/2}} alone if k even),
    # plus reflection classes
    
    # For the 3D representation (rotations in R³), the character at a rotation
    # by angle θ about the z-axis is χ₁(θ) = 1 + 2cos(θ), and at a reflection
    # (rotation by π about an axis in the xy-plane) is χ₁(π) = -1.
    
    # For spin-2, we use χ₂(θ) directly on the rotation angles.
    # D_k conjugacy classes (as subgroup of SO(3)):
    classes = []
    sizes = []
    
    # Identity
    classes.append(0)
    sizes.append(1)
    
    # Rotations by 2πj/k, j=1,...,⌊(k-1)/2⌋ (each class has 2 elements {r^j, r^{-j}})
    for j in range(1, k):
        theta = 2 * np.pi * j / k
        if j < k - j:
            classes.append(theta)
            sizes.append(2)
        elif j == k - j:  # k even, j = k/2
            classes.append(theta)
            sizes.append(1)
    
    # Reflections: in SO(3), each reflection of D_k is a rotation by π about
    # some axis in the equatorial plane.
    if k % 2 == 0:
        # Two reflection classes, each of size k/2
        classes.append(np.pi)
        sizes.append(k // 2)
        classes.append(np.pi)
        sizes.append(k // 2)
    else:
        # One reflection class of size k
        classes.append(np.pi)
        sizes.append(k)
    
    chi_vals = [chi_spin2(t) for t in classes]
    
    # Trivial character: all 1s
    trivial_vals = [1.0] * len(classes)
    
    mult_trivial = inner_product(chi_vals, trivial_vals, sizes, group_order)
    
    return {"group": f"D*_{k}", "ADE": f"D_{k+2}", "binary_order": 4*k,
            "sd_inv_dim": int(round(mult_trivial.real)),
            "asd_inv_dim": 5, "total_l2_inv": int(round(mult_trivial.real)) + 5}

def analyze_exceptional(name, so3_group, class_angles, class_sizes, group_order):
    """Analyze exceptional binary group via its SO(3) image."""
    chi_vals = [chi_spin2(t) for t in class_angles]
    trivial_vals = [1.0] * len(class_angles)
    mult = inner_product(chi_vals, trivial_vals, class_sizes, group_order)
    
    return {"group": name, "binary_order": 2 * group_order,
            "sd_inv_dim": int(round(mult.real)),
            "asd_inv_dim": 5, "total_l2_inv": int(round(mult.real)) + 5,
            "chi2_restricted": [round(c, 6) for c in chi_vals],
            "class_sizes": class_sizes,
            "trivial_multiplicity_exact": round(mult.real, 8)}

results = {"purpose": "Γ-invariant l=2 TT tensor harmonics for ADE singularities",
           "mechanism": "In SU(2)_L embedding, compatible ALE bubbles test R_+ on Γ-inv l=2 "
                        "self-dual subspace; reversed bubbles test R_- on full 5D anti-self-dual space.",
           "cyclic": [], "dihedral": [], "exceptional": []}

# Cyclic groups Z_p (A_{p-1} singularities)
for p in [2, 3, 4, 5, 6, 7, 8, 10, 12]:
    results["cyclic"].append(analyze_cyclic(p))

# Binary dihedral D*_k (D_{k+2} singularities)
for k in [2, 3, 4, 5, 6]:
    results["dihedral"].append(analyze_binary_dihedral(k))

# Binary tetrahedral T* (E6): SO(3) image is T ≅ A₄, order 12
# Conjugacy classes of A₄ in SO(3): {e}(1), {3 rotations by π}(3), 
# {4 rotations by 2π/3}(4), {4 rotations by 4π/3}(4)
results["exceptional"].append(analyze_exceptional(
    "T* (E6)", "T ≅ A₄",
    [0, np.pi, 2*np.pi/3, 4*np.pi/3],
    [1, 3, 4, 4], 12
))

# Binary octahedral O* (E7): SO(3) image is O ≅ S₄, order 24
# Conjugacy classes: {e}(1), {6 rotations π/2}(6), {3 rotations π (face)}(3),
# {8 rotations 2π/3}(8), {6 rotations π (edge)}(6)
results["exceptional"].append(analyze_exceptional(
    "O* (E7)", "O ≅ S₄",
    [0, np.pi/2, np.pi, 2*np.pi/3, np.pi],
    [1, 6, 3, 8, 6], 24
))

# Binary icosahedral I* (E8): SO(3) image is I ≅ A₅, order 60
# Conjugacy classes: {e}(1), {15 rotations π}(15), {20 rotations 2π/3}(20),
# {12 rotations 2π/5}(12), {12 rotations 4π/5}(12)
results["exceptional"].append(analyze_exceptional(
    "I* (E8)", "I ≅ A₅",
    [0, np.pi, 2*np.pi/3, 2*np.pi/5, 4*np.pi/5],
    [1, 15, 20, 12, 12], 60
))

# Summary table
print("=" * 80)
print("Γ-INVARIANT l=2 TT TENSOR HARMONICS ON S³/Γ")
print("=" * 80)
print(f"{'Type':<20} {'Γ':<15} {'|Γ_bin|':<10} {'dim(SD inv)':<14} {'dim(ASD inv)':<14} {'First obs'}")
print("-" * 80)

for c in results["cyclic"]:
    eff = "EFFECTIVE" if c["sd_inv_dim"] > 0 else "VACUOUS"
    print(f"{c['ADE']:<20} {c['group']:<15} {c['order']:<10} {c['sd_inv_dim']:<14} {c['asd_inv_dim']:<14} {eff}")

for d in results["dihedral"]:
    eff = "EFFECTIVE" if d["sd_inv_dim"] > 0 else "VACUOUS"
    print(f"{d['ADE']:<20} {d['group']:<15} {d['binary_order']:<10} {d['sd_inv_dim']:<14} {d['asd_inv_dim']:<14} {eff}")

for e in results["exceptional"]:
    eff = "EFFECTIVE" if e["sd_inv_dim"] > 0 else "VACUOUS"
    print(f"{e['group']:<20} {'—':<15} {e['binary_order']:<10} {e['sd_inv_dim']:<14} {e['asd_inv_dim']:<14} {eff}")

print("\n" + "=" * 80)
print("KEY FINDING: For E6, E7, E8 singularities in compatible orientation,")
print("the Γ-invariant l=2 self-dual TT space is EMPTY.")
print("The first-order vector obstruction is VACUOUS for these types.")
print("=" * 80)

print("\nFor reversed bubbles: ALL types test R_- on the FULL 5D anti-self-dual space.")
print("The condition det R_- = 0 applies to all reversed bubbles regardless of Γ.")

# Verify the exceptional cases by direct character computation
print("\n--- Verification: character of spin-2 restricted to exceptional groups ---")
for e in results["exceptional"]:
    print(f"\n{e['group']}:")
    print(f"  χ₂ on classes: {e['chi2_restricted']}")
    print(f"  class sizes:   {e['class_sizes']}")
    print(f"  ⟨χ₂, 1⟩ = {e['trivial_multiplicity_exact']}")

# Save
output = "Sessions/S0910A02/workspace/data/step46_gamma_invariant_l2_modes.json"
with open(output, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {output}")

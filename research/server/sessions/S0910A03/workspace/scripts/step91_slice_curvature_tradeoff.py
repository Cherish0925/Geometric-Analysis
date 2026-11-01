"""
Step 91 intrinsic slice-curvature calculation (corrected in Step 92).

The symbolic formula is valid. The original interpretation below reversed the
contracted-Gauss sign. At a minimal slice, negative scalar curvature is required,
and orbit energy helps supply it. See the Step 92 note; do not use the old
positive-curvature commentary as mathematics.

For a T²-invariant T³ slice: q = φ(z)²dz² + e^{σ+α}(z)(dξ₁+Pdz)² + e^{σ-α}(z)dξ₂²
we compute R(q) and compare with e_s.
"""
import sympy as sp
import json
from pathlib import Path

z = sp.Symbol('z')
phi, sig, alp, P = sp.symbols('phi sigma alpha P', cls=sp.Function)
# Evaluate at z=0 with φ(0)=1 (unit normalization)
phi_0, sig_0, alp_0 = sp.symbols('phi0 sigma0 alpha0')
phi_1, sig_1, alp_1, P_1 = sp.symbols("phi' sigma' alpha' P'")
phi_2, sig_2, alp_2, P_2 = sp.symbols("phi'' sigma'' alpha'' P''")

# The slice metric on T³ = S¹_z × T²_{ξ₁,ξ₂}:
# After gauge-fixing A_z = 0 on the universal cover (possible since T² is abelian),
# we have q = φ²dz² + G_ab(z)dξ^a dξ^b
# = φ²dz² + e^{σ+α}dξ₁² + e^{σ-α}dξ₂²

# For a left-invariant-in-fiber metric (coefficients depend on z only):
# The scalar curvature can be computed from the second fundamental form of
# the z-circles in the T³.

# Approach: q = φ²dz² + g₁₁(z)dξ₁² + g₂₂(z)dξ₂²
# In Gaussian normal coordinate t with dt = φdz:
# q = dt² + g₁₁(t)dξ₁² + g₂₂(t)dξ₂²

# Scalar curvature:
# R_q = -2(g₁₁''/(g₁₁) + g₂₂''/(g₂₂))   [in dt coordinates]
# where primes are d/dt

# Wait, for q = dt² + a(t)²dξ₁² + b(t)²dξ₂² on R × T²:
# R = -2(a''/a + b''/b) 
# (This is the scalar curvature of a warped product with 1D base and 2D flat fiber)

# Actually for a product metric dt² + a²dx² + b²dy² where a,b depend on t:
# The nonzero Christoffel symbols are Γ^t_xx = -aa', Γ^t_yy = -bb',
# Γ^x_tx = a'/a, Γ^y_ty = b'/b
# Ricci tensor:
# Ric_tt = -(a''/a + b''/b)
# Ric_xx = -a(a'' + a'b'/b)  -> Ric(e_x,e_x) = -(a''/a + a'b'/(ab))
# Ric_yy = -b(b'' + a'b'/a)  -> Ric(e_y,e_y) = -(b''/b + a'b'/(ab))
# R = -(2a''/a + 2b''/b + 2a'b'/(ab))

# With a = exp((σ+α)/2), b = exp((σ-α)/2):
# a'/a = (σ'+α')/2, a''/a = (σ''+α'')/2 + (σ'+α')²/4
# b'/b = (σ'-α')/2, b''/b = (σ''-α'')/2 + (σ'-α')²/4
# a'b'/(ab) = (σ'²-α'²)/4

s1, s2, a1, a2 = sp.symbols("s1 s2 a1 a2")  # σ', σ'', α', α''

a_p_a = (s1 + a1)/2  # a'/a
b_p_b = (s1 - a1)/2  # b'/b
a_pp_a = (s2 + a2)/2 + (s1 + a1)**2/4  # a''/a
b_pp_b = (s2 - a2)/2 + (s1 - a1)**2/4  # b''/b
ab_ratio = (s1**2 - a1**2)/4  # a'b'/(ab)

R_q = sp.expand(-2*a_pp_a - 2*b_pp_b - 2*ab_ratio)
print(f"R(q) = {R_q}")
R_q_collected = sp.collect(R_q, [s1, s2, a1, a2])
print(f"R(q) collected = {R_q_collected}")

# Orbit energy: e_s = (1/2)tr((M^{-1}M')²)
# For diagonal M = diag(e^α, e^{-α}): M^{-1}M' = diag(α', -α')
# tr((M^{-1}M')²) = 2α'² → e_s = α'² = a1²
# In dt coordinates: dt = φdz, so α'_t = α'_z/φ

# Also: h² = σ'_t² = s1²
# And the T³ "expansion rate" in the r-direction has H_slice = a'/a + b'/b = σ'

# So: R(q) = -2(a''/a + b''/b) - 2a'b'/(ab)
# = -2σ'' - σ'² - σ'² - α'²/2 - 2(σ'²-α'²)/4
# Let me just evaluate:

print(f"\nIn terms of σ'={s1}, σ''={s2}, α'={a1}, α''={a2}:")
print(f"R(q) = {R_q}")

# Simplify: the terms involving s2:
coeff_s2 = R_q.coeff(s2)
coeff_a2 = R_q.coeff(a2)
remainder = sp.expand(R_q - coeff_s2*s2 - coeff_a2*a2)
print(f"\nR(q) = ({coeff_s2})·σ'' + ({coeff_a2})·α'' + {remainder}")

# The remainder (no second derivatives):
remainder_collected = sp.collect(remainder, [s1, a1])
print(f"Remainder = {remainder_collected}")

# Key identity: R(q) = -2σ'' - (3/2)σ'² - (1/2)α'² - 2α''·(something?)
# Let me check by plugging in specific values

# Test: α = 0 (round T² fiber)
R_round = R_q.subs([(a1, 0), (a2, 0)])
print(f"\nR(q)|_alpha=0 = {sp.expand(R_round)}")
# Should be R = -2σ'' - (3/2)σ'²
# From Step 88: R_q = -2h_s - (3/2)h² - (1/2)e_s
# With h = σ' and e_s = α'² = 0: R = -2σ'' - (3/2)σ'² ✓

# Full formula:
print(f"\nFull: R(q) = -2σ'' - (3/2)σ'² - (1/2)α'² = -2h' - (3/2)h² - (1/2)e_s")
# Check:
check = sp.expand(R_q - (-2*s2 - sp.Rational(3,2)*s1**2 - sp.Rational(1,2)*a1**2))
print(f"Check residual: {check}")

if check != 0:
    print("NONZERO! The formula has additional terms.")
    # The additional terms involve α'' and cross terms
    # R(q) = -2σ'' - (3/2)σ'² - (1/2)α'² + (other)
    print(f"Other terms: {sp.collect(check, [a2, s1, a1])}")
else:
    print("Formula confirmed: R(q) = -2σ'' - (3/2)σ'² - (1/2)α'²")
    print("This is exactly the Step 88 identity: R_q = -2h' - (3/2)h² - (1/2)e_s")

# Key observation: R(q) for the T³ slice depends on σ'' and α'² = e_s.
# The orbit energy e_s appears with coefficient -(1/2).
# Integrating over z with weight ρ = e^σ:
# ∫ R(q) ρ dz = ∫(-2σ'' - (3/2)σ'² - (1/2)α'²)ρ dz
# Integration by parts: ∫σ''ρ dz = -∫σ'(ρ') dz = -∫σ'²ρ dz
# So: ∫ R(q) ρ dz = (1/2)∫σ'²ρ dz - (1/2)∫α'²ρ dz
# = (1/2)⟨h²⟩ - (1/2)⟨e_s⟩ = ⟨R_q⟩ [which is the Step 88 identity!]

print("\n=== Slice curvature vs orbit energy relationship ===")
print("R(q_r) = -2σ'' - (3/2)σ'² - (1/2)e_s  (in Gaussian t-coordinate)")
print("Pointwise: making R(q_r) ≤ -c requires either")  
print("  (a) σ'' ≥ c/2 (area acceleration), or")
print("  (b) e_s ≥ 2c (orbit energy)")
print("  (c) σ'² ≥ 2c/3 (area gradient)")
print("")
print("To overcome flat-slice barrier (need R ≈ -3 to allow H=0 at small δ):")
print("  Need R(q_r) ≤ -3, which requires σ'' + (3/4)σ'² + (1/4)e_s ≥ 3/2")
print("")
print("But at the SEPARATOR (minimal, ρ²γ-geodesic):")
print("  h_T = σ_T = 0 (since ∫ρσ_T ds = 0 on closed curve -> not exactly 0)")
print("  Actually h_T need not vanish pointwise; ⟨h_T²⟩ contributes to floor")

# Correct contracted Gauss interpretation (Step 92):
# R(q) = -6 + D + H² - |II|².
# At a minimal slice H=0, R(q) = -6 + D - |II|² <= -6 + 4δ.
# Thus the negative terms -(3/2)h_T² and -(1/2)e_s HELP furnish the required
# intrinsic curvature. H=0 must also not be confused with ∂_r H=0.
# The remaining useful question concerns the full weighted Jacobi stability
# form and concentration, not a positive-curvature conflict.

results = {
    'R_q_formula': 'R(q) = -2*sigma_tt - (3/2)*sigma_t^2 - (1/2)*e_s',
    'identity_with_step88': 'Exact: this is -2h_T - (3/2)h_T^2 - (1/2)e_s',
    'integrated_identity': '<R(q)>_rho = (1/2)<h_T^2> - (1/2)<e_s>',
      'at_H_equals_zero': 'R(q) = -6 + D - |II|^2 <= -6 + 4*delta',
      'obstruction_status': 'No pointwise conflict: tangential orbit energy helps supply the required negative curvature',
      'structural_tension': 'Superseded; investigate the full weighted Jacobi form and concentration instead'
}

out = Path('workspace/data/step91_slice_curvature_tradeoff.json')
out.parent.mkdir(parents=True, exist_ok=True)
with open(out, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nwrote {out}")

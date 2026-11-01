# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/scripts/step94_corrected_aabb_principal_response.py",
    "Sessions/S0910A01/workspace/data/step94_corrected_aabb_principal_response.json",
    "Sessions/S0910A01/workspace/scripts/step93_aabb_tensor_sector_analysis.py",
    "Sessions/S0910A01/workspace/notes/step93_aabb_sector_divergence.md",
    "Sessions/S0910A01/trace/ttcs/results/step93_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Verify the Step 94 correction to the Step 93 AA/BB tensor-sector calculation for the product-orbifold chirality-odd Green response. Check specifically: (1) if electric TF tensor E=(Hess f)^TF has pole amplitude 2b and norm mu(mu-2)/2, then magnetic tensor M=L_{(*df)^#}g has pole amplitude 4b and norm four times the electric norm; equivalently using (1/2)M restores amplitude 2b and the electric norm. (2) With this corrected normalization, separated-pole tensor electric and magnetic contributions cancel exactly under the Step-93 transported pole signs, so the claimed BB_NS/AA_SN coincident divergence is not intrinsic. (3) Same-pole tensor electric and magnetic contributions reinforce equally, leaving a finite AA_NS/BB_SN principal response. (4) The heat-kernel representation K_AA_NS = -1/1024 int_0^infty e^s A0(s) B2(s) ds with B2=32*pi d_x^2 p_{s/2}^{S2}(-1) is consistent with the script and gives a negative finite value in the stated Step89/91 principal normalization. Identify any remaining source/gauge/Ozuch normalizations not settled by this correction.

## Output

# Verification memo — Step 94 correction to the AA/BB trace-free tensor sector

## Overall assessment

All four assertions of Step 94 hold. The tensor-norm ratio, the antipodal cancellation, the same-pole reinforcement, and the heat-kernel representation with its sign are internally consistent, agree with the direct spectral ladder to about nine digits, and rest on mathematics I can reproduce independently. One point strengthens the result beyond what the script states (the relative sign is forced by orientation, not chosen); several source normalizations remain genuinely unsettled and are the deciding quantities for the physical desingularization coefficient.

## 1. Tensor norm ratio ‖M‖² = 4‖E‖² — confirmed by explicit pointwise computation

Work in an orthonormal frame at a pole and let H = Hess f with off-diagonal H₀₁ and traceless-diagonal part a = (H₀₀−H₁₁)/2, c = H₀₁.

Electric tensor:
$$E=(\mathrm{Hess}\,f)^{\rm TF}=\begin{pmatrix}a&c\\ c&-a\end{pmatrix},\qquad |E|^2=2a^2+2c^2.$$

Magnetic tensor M = L_{(*df)^#}g with X₀ = −∂₁f, X₁ = ∂₀f (using J = [[0,−1],[1,0]]). At the pole in normal coordinates,
$$M_{00}=2\partial_0X_0=-2H_{01},\quad M_{11}=2H_{01},\quad M_{01}=H_{00}-H_{11},$$
so
$$M=2\begin{pmatrix}-c&a\\ a&c\end{pmatrix},\qquad |M|^2=8a^2+8c^2=4|E|^2.$$

This is exact **pointwise**, hence in L². It also confirms the amplitudes: for the sine m=2 mode (a=0, c=2b) E₀₁ = 2b; for the cosine m=2 mode (a=2b, c=0) M₀₁ = 4b. The identity M = 2·(E rotated by J) shows electric and magnetic are the two natural TF polarizations of equal L² weight only after dividing each by **its own** norm.

The L² norm value is also right. Bochner on the unit S² (Ric = g) gives ∫|Hess f|² = μ(μ−1)‖f‖², and removing the trace part (‖trace part‖² = (Δf)²/2 in dimension 2) yields
$$\|E\|^2=\tfrac12\mu(\mu-2)\|f\|^2,$$
matching `tf_norm(electric)=μ(μ−2)/2`, and therefore ‖M‖² = 2μ(μ−2), matching `tf_norm(magnetic_full_lie)=4·electric`. The `b2(l)=(2l+1)μ(μ−2)/(128π)` normalization reproduces the tabulated `same_pole_electric_normalized` values exactly: (2ℓ+1)/(16π) gives 0.09947 (ℓ=2), 0.13926 (ℓ=3), … as listed.

The Step 93 defect is thus a real relative-normalization error: an amplitude-4b tensor was divided by the norm appropriate to amplitude 2b. The earlier Step 93 memo correctly stated that no single overall constant removes the divergence; Step 94 does not use an overall constant but a magnetic-versus-electric reweighting, so the two statements are compatible.

## 2. Antipodal tensor cancellation — confirmed, and the relative sign is forced

Using the transported pole signs (electric sine at S: −(−1)^ℓ·2b; magnetic cosine at S: +(−1)^ℓ·4b):
$$\frac{E_NE_S}{\|E\|^2}=\frac{-(-1)^\ell 4b^2}{\mu(\mu-2)/2}=-(-1)^\ell\frac{8b^2}{\mu(\mu-2)},\qquad
\frac{M_NM_S}{\|M\|^2}=\frac{(-1)^\ell 16b^2}{2\mu(\mu-2)}=(-1)^\ell\frac{8b^2}{\mu(\mu-2)}.$$
The sum is identically zero for every ℓ, matching `separated_sum = 0` throughout the table. With the erroneous common norm one gets instead (−1)^ℓ·12b²/[μ(μ−2)/2] ≠ 0, reproducing the Step 93 residual that, multiplied by the coincident scalar sum, grew as τ⁻². So the divergence was produced precisely by the norm error breaking this cancellation.

**Strengthening beyond the script.** The cancellation is not an artifact of a chosen sine/cosine phase. The magnetic tensor is built through the Hodge star, and the antipodal map on S² is orientation-reversing (−I on ℝ³ restricted to S² has determinant −1). The star therefore transports with one extra sign relative to the electric tensor. Hence, whatever the absolute phase conventions, the electric and magnetic antipodal transports differ by a factor −1, which is exactly what is needed for the exact cancellation. The earlier Step 93 memo flagged the sine/cosine phase as convention-dependent; the present observation upgrades that: the **relative** sign between the two polarizations is fixed by geometry, so the vanishing of the separated-tensor sum is robust. Because R_rec·R_src ∝ (amplitude)² and the norm ∝ (amplitude)², the normalized contribution is amplitude-independent, so the equivalent (1/2)M convention gives identical results — the resolution does not depend on how M is scaled.

## 3. Same-pole reinforcement — confirmed

At the coincident pole,
$$\frac{E_NE_N}{\|E\|^2}=\frac{4b^2}{\mu(\mu-2)/2}=\frac{8b^2}{\mu(\mu-2)}=\frac{M_NM_N}{\|M\|^2},$$
so electric and magnetic reinforce with equal weight, giving `same_pole_sum = 16b²/[μ(μ−2)] = (2ℓ+1)/(8π)`, consistent with the tabulated sums. K_AA_NS (tensor on A same-pole, scalar on B separated) is therefore finite; K_BB_NS and K_AA_SN vanish because their separated factor is the tensor, which cancels term by term before the coincident scalar sum can grow. The data confirm K_BB(NS)=0, K_AA(SN)=0, K(SS)=0, and the A↔B-symmetric total −0.004 for both NS and SN.

## 4. Heat-kernel representation and sign — confirmed to nine digits

Reducing the AA_NS double sum with the correct norms, each (l_t,l_s) term becomes
$$\frac1{1024}\,\frac{e^{-\tau P}}{P}\big[-(-1)^{l_s}(2l_s+1)\mu_s(\mu_s-2)\big](2l_t+1),$$
where the tensor factor contributes (2l_t+1)/(128π) with **no** extra μ (since b2(l_t)/[μ_t(μ_t−2)] = (2l_t+1)/128π) and the scalar factor contributes the μ(μ−2) weight. Applying 1/P = ∫₀^∞ e^{−sP}ds with P = ½(μ_t+μ_s)−1 gives exactly
$$K_{\rm AA,NS}=-\frac1{1024}\int_0^\infty e^s A_0(s)B_2(s)\,ds,\quad A_0=\sum_{\ell\ge2}(2\ell+1)e^{-s\mu/2},\ B_2=\sum_{\ell\ge2}(-1)^\ell(2\ell+1)\mu(\mu-2)e^{-s\mu/2}.$$
This matches the script. The integral is well-defined: near s→0, A₀ ~ 2/s while B₂ = 32π ∂ₓ²p_{s/2}^{S²}(−1) is exponentially small (antipodal kernel), so the integrand vanishes; at large s the ℓ=2 terms give ~600 e^{−5s}. The direct quadrature is stable at 4.0986 over four different intervals, so K_AA_NS = −4.0986/1024 = −0.0040025, and the τ-ladder converges to −0.00400249866, agreeing with the integral to ~9 digits. The sign is minus because A₀>0 and B₂>0; positivity of B₂ follows from ∂ₓ²p_t^{S²}(−1) = 4π²e^{−6t}p_t^{S⁶}(−1) with p_t^{S⁶}(−1)>0. Note the sign here is established directly by the stable positive quadrature and does not depend on the dimension-raising interpretation, which merely explains it. The 1/1024 prefactor (versus 1/512 for the fully-separated AB sector) is the expected consequence of one coincident and one separated factor rather than two separated factors.

## Reconciliation with the Step 93 divergence

The two accounts are consistent. Step 93 attributed the BB_NS growth to the coincident scalar sum on A. Step 94 shows that in the correctly-normalized computation the separated tensor factor on B cancels at each tensor degree, so the coincident scalar sum is multiplied by zero and never contributes. The Step 93 growth was the coincident scalar sum multiplied by the *uncancelled* residual left by the magnetic norm error. The earlier verifier's alternative reading — that a fully localized BB pairing would carry off-diagonal e^{−c/t} tensor suppression — is compatible: the exact antipodal cancellation is the spectral image of that suppression at the level of the principal product background.

## Remaining unsettled normalizations

This computation determines the structure of one ingredient in the Step 89/91 principal product-background normalization; it is not the physical Ozuch/Biquard desingularization coefficient. The quantities that still control the actual coefficient and its sign, none of which is supplied or fixed by this correction, are:

- the Eguchi–Hanson H⁴ ALE source tensor and its mode contractions ⟨S_ALE, e_{ℓm}⟩;
- the Bianchi/gauge projection, which may prescribe a finite-part extraction combining sectors that are not individually meaningful;
- the quotient/isotropy and symmetric-product conventions, which can rescale relative weights of AA/BB against AB;
- ordered-adjacent frame transport between distinct resolution nodes;
- the nonlinear radial matching of the gluing.

Consequently the verified statement is: in the principal normalization, the properly-normalized AA/BB sector is finite (the coincident divergence was a relative-norm error), with K_AA_NS = K_BB_SN ≈ −0.0040025 and the antipodal pieces vanishing exactly. Whether the physical adjacent coefficient inherits this sign depends on the ALE source contraction and gauge projection, which are the unresolved objects. Determining those is what would connect this ingredient to the desingularization existence question underlying the research goal, and ultimately to whether the Ricci-pinching hypothesis forces an Einstein metric.

One item worth an explicit independent check in the source material: the transported-pole sign table for the electric-sine and magnetic-cosine modes is used verbatim from Step 93. I have given a geometric reason (orientation-reversal of the antipodal map) that the *relative* sign must be −1, which is all the cancellation needs; a short direct verification of the two absolute signs against the explicit spherical-harmonic jets would close the last dependence.
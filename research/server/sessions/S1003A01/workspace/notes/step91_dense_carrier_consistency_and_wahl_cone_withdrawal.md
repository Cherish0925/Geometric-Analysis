# Step 91: the dense Taub–NUT carrier satisfies every inherited averaged density-free endpoint identity; withdrawal of the Wahl cone-mode count

Session S1003A01, Agent2, Execute. Inputs:
- the O10 finite-density proof, §§2–5 (`.../research/C/O10_Finite_Density_Complete_Proof.tex`, lines 74–463);
- the direct resolvent (`O10_Direct_Resolvent_Prerequisite.md`, (2.1)–(2.4));
- the Step-47 exact TN data (`workspace/notes/step47_o10_tn_core_free_at_energy_scale.md`);
- the Step-90 dipole (`workspace/notes/step90_review_and_tn_projected_charge5.md`);
- A02 #887 (Prop. 104.C, 104.F, 104.M).

## 0. Withdrawal: Wahl cone indicial counting is not an Einstein constraint

I started a count of Γ-invariant anti-Hermitian "TT cone modes" at the Wahl point 1/n²(1,n−1). The scripts are `workspace/scripts/step91_wahl_cone_deformation.py`, with output `data/step91/wahl_cone_deformation.json`, and `step91_wahl_cone_TT_proper.py`, which was never run. Before interpreting the count I withdrew it, for two reasons.

**(i) The count says nothing about existence.** A Wahl point of an orbifold metric is a *flat-cone orbifold point*. On the uniformizing chart, an orbifold Einstein metric is just a Γ-invariant smooth Einstein germ on a ball in C². Indicial roots of a flat cone C²/Γ therefore impose no constraint: every Γ-invariant Taylor coefficient compatible with the Einstein equation is allowed. Moreover, a non-Kähler Einstein metric has no distinguished J₀ at p, so the label "anti-Hermitian with respect to J₀" means nothing. Indicial analysis matters only for genuinely singular (non-orbifold) cones, or for ALE fillers in gluing.

**(ii) The calculation itself was ad hoc.** The divergence formula used only ∂/∂z̄ on the complex (2,0) part. It did not compute the real TT condition of h+h̄.

This agrees with A02's Prop. 104.C, which shows that the optimal supply on V has boundary character j=0, so Φ(p)≠0 and no zero is forced. The Wahl question therefore remains a pure global existence problem: does V carry a non-Kähler negative Einstein orbifold metric? It needs a global construction or obstruction, not local isotropy or cone data. Neither withdrawn script should be cited.

## 1. A density-free mean identity for the bounded resolvent

Let u be the direct resolvent, (4+L)u = 6T(t). From (2.2) and (2.4) of the prerequisite, without any Euler-density bound:
\[
|u|\le 6,\qquad |Lu|\le 48,\qquad (L-2)u\to0\ \text{in }L^2_{\rm av},\qquad |u|^2\to m_*\ \text{in }L^2_{\rm av}.
\]
Here L = ∇*∇ on E = S⁻⊗L with determinant connection 3A, and Δ = −d*d.

**Proposition 91.1.** Along every O10 endpoint sequence:

(a) the pointwise identity
\[
|\nabla u|^2=\operatorname{Re}\langle Lu,u\rangle+\tfrac12\Delta|u|^2
\]
holds, so q := |∇u|² ≤ 288 + ½Δ|u|²;

(b)
\[
\fint|\nabla u|^2\;\longrightarrow\;2m_* .
\]

*Proof.* (a) is the Bochner identity together with the two pointwise bounds. For (b), integrate (a) over the closed manifold:
∫q = Re∫⟨Lu,u⟩ = 2∫|u|² + ∫⟨(L−2)u,u⟩.
The last term is at most ‖(L−2)u‖₂‖u‖₂ = o(V), and ∫|u|²/V → m*. ∎

(b) is the integrated form of the identity Δ|v|² = 4|v|² − 2q + o(1) used in the covariance test (15). The finite-density proof upgrades it to q → 2m* *in measure* only through ‖∇v‖₄ ≤ C_B, i.e. through uniform integrability, which needs the W⁻ budget. Without that budget, the mean is fixed but q may concentrate. By (a), a concentration of q at scale ℓ must be matched pointwise by a dip of |u|² with Δ|u|² ≍ ℓ⁻², since Lu is bounded.

**Exact check on the TN model.** Script: `workspace/scripts/step91_tn_mean_identity.py`, output `workspace/data/step91/tn_mean_identity.json`. All residuals are exactly 0, and the script also returns the cell volume 4π²ℓ². Use the GH form with V = 1+ℓ/r, f̄ = x₁−ix₂, and τ_TN = √2 ρ* a df̄. Then |τ|² = m*/V = m* r/(r+ℓ), and Δ_g acting on base functions is V⁻¹Δ_{R³}. One computes Δ_{R³}(r/(r+ℓ)) = 2ℓ²/(r(r+ℓ)³), so
\[
\tfrac12\Delta_g|\tau|^2=\frac{m_*\ell^2}{(r+\ell)^4}=|\nabla\tau|^2 ,
\]
using |∇τ|² = 2ρ*²a²|Hess f̄|² and |Hess f̄|² = 2ℓ²/(r+ℓ)⁴ from Step 47. The two sides agree, as (a) requires when L τ_TN = 0 on the Ricci-flat model; on the physical block, the s=−4 curvature and F_A⁻ supply the 2τ (Step 47 (1.1)). Integrating against the GH volume V r² sinθ dr dθ dφ dψ, with ψ-period 4πℓ, gives
16π²ℓ · m*ℓ² ∫₀^∞ r(r+ℓ)⁻³ dr = 8π² m* ℓ²,
which matches the Step-47 table.

## 2. Wigner–Seitz consistency of mixed phases

**Proposition 91.2.** Suppose a fraction θ ∈ [0,1] of the normalized volume is occupied by TN-type cores of scale ℓ, at density N/V = θ/(4π²ℓ²), and the remaining fraction 1−θ is in the uniform |c|=1 phase, where q = 2m*. Then for every θ, the configuration satisfies all of the following:
- the mean identity 91.1(b);
- the Step-47 cell balance 2E₁ + 3E₂ + 4m²|c|² = 4m²;
- |u|² → m* in measure;
- the pointwise bounds |u| ≤ 6 and |Lu| ≤ 48, realized through sharp amplitude dips of the form m* r/(r+ℓ);
- normalized ∫|W⁻|²/V = 2θ/ℓ² → ∞, i.e. χ/A → ∞.

*Proof.* Each core carries ∫q = 8π²m*ℓ², so the cores contribute θ·2m* to ∫q/V. The uniform phase contributes (1−θ)2m*. For the cell geometry: a cell has 4-volume 4π²ℓ² and fibre length 4πℓ, so it is a base region of 3-volume πℓ, with linear size d ≍ ℓ^{1/3}. This is the Step-47 flux radius. The core volume fraction is O((ℓ/d)³) = O(ℓ²). ∎

**Consequence.** Every averaged or integrated density-free identity in the inherited endpoint system is blind to the parameter θ. These identities cover amplitude, mean derivative energy, Wigner–Seitz energy, and the Chern–Weil square of L, which is carried by the bounded bulk F_A ≈ i(⅔ω + ⅓β⁻) in both phases. Hence density-free O10 cannot follow from any combination of them. A proof needs a non-averaged identity: a derivative-level estimate such as the Step-47 ‖∇N_τ‖ → 0, or a transport or matching statement. Alternatively, a counterexample needs a closed realization of θ = 1, or of some θ > 0, together with its compensators.

This sharpens Step 90. That the resolvent section σ is depleted in measure is not an anomaly of the single-nut model. It is forced: along any endpoint sequence with θ > 0, the uniform phase, where σ is nearly constant, has normalized measure only 1−θ.

## 3. What the line square requires of the depleted set, quantitatively

Apply the finite-density transgression (11)–(12) to the truncated resolvent section s = T(σ) of L⁵. Let Z = {|s| ≤ 3ℓ_σ/4} be the depleted set, where ℓ_σ = 2√ρ* m*^{3/2} is the endpoint modulus. Stokes gives
\[
\frac{25}{6\pi^2}+o(1)=\frac{c_1(L^5)^2}{V}\le\frac{C}{V}\Bigl(\int_Z|F|^2+\int_Z|F|\,|\nabla s|^2\Bigr).
\]
With |F| bounded by a model plus an L²-small error, and μ(Z) → 0, this becomes:

**Corollary 91.3.** If μ(Z) → 0, then the derivative energy of s on the depleted set satisfies
\[
\liminf\ V^{-1}\!\int_Z|F_{0}|\,|\nabla s|^2\ \ge\ c_0=\frac{25}{6\pi^2C}>0,
\]
up to the term ∫_Z|e||∇s|², which is not small without the logarithmic resolvent selection. In words: **the topology of L⁵ must be paid for by σ-derivative energy concentrated on a vanishing-measure set.**

On the TN carrier this cost is overpaid. The amplitude part alone is E_amp = 67108864π²/33480783 per core, and this is a Kato lower bound valid for every unitary connection (Step 90, (90.5)). The normalized total is θ E_amp/(4π²ℓ²) → ∞. So Corollary 91.3 is a necessary condition that dense carriers satisfy, not an obstruction. It does exclude a different putative escape: depletion on a vanishing-measure set carrying vanishing normalized derivative energy, i.e. dilute or slow vortices. The only admissible escapes are *derivative-dense* ones.

## 4. Flux quantization on nut-chain spheres (conditional)

On a multi-TN block, let the curve from nut x_i to nut x_j in the base, times the fibre, close up to a 2-sphere S_ij. Assume F_A is pointwise bounded on the block, |F_A| ≤ C. The inherited fit only gives F⁻ = F₀ + e with e small in L², so pointwise control is an extra hypothesis. Then
\[
\Bigl|\int_{S_{ij}}F_A\Bigr|\le C\cdot 4\pi\ell\cdot|x_i-x_j|_{\rm base}\cdot(1+o(1)).
\]
Integrality, ∫ ∈ 2πℤ, then forces c₁(L)·[S_ij] = 0 as soon as 2Cℓ|x_i − x_j| < 1. For neighbouring nuts at spacing ≍ ℓ^{1/3}, this holds as ℓ → 0.

So, under the pointwise hypothesis, c₁(L) is orthogonal to the negative-definite chain lattice spanned by the nut spheres, whose self-intersections are −2 (an A_{N−1}-type lattice). The b⁻-growth implied by χ/A → ∞ then sits in a sublattice orthogonal to the monopole class. This is consistent with adjunction for (−2)-spheres, so it is not a contradiction. It does fix where a global matching argument must look: the transition between the nut lattice and the classes that carry c₁(L)², with c₁(L)² ≈ V/(6π²).

## 5. Status and implications

- **Proved here, density-free:** Proposition 91.1, the mean identity and pointwise dip relation; the exact TN check of 91.1(a); Corollary 91.3, which as stated keeps the uncontrolled ∫_Z|e||∇s|² term.
- **Model-consistency statement:** Proposition 91.2. It rests on the TN model and the inherited endpoint relations. It does not construct closed fields.
- **Conditional:** §4, on a pointwise bound for F_A on blocks.
- **Withdrawn:** the §0 Wahl cone count.

Density-free O10 is now known to be undecidable by averaged identities, since every θ ∈ [0,1] is averaged-consistent. Two kinds of further input remain:
(a) a non-averaged derivative estimate, for instance on the J₊-(1,0) current ∇N_τ, the Step-47 candidate;
(b) a closed realization of a derivative-dense carrier with its compensators. The carrier is circle-collapsed at fibre length ≍ ℓ, with cells of base size ℓ^{1/3}.

As Spirit #118 noted, neither affects Q1 for k/A < 1/3, where finite-density O10 already applies. The Q1 centre, sharpened by A02 #887 (Props. 104.F and 104.M), is the trichotomy: positive gap, versus a non-Kähler Einstein orbifold of Wahl or D_{≥6} type, versus a smooth Einstein metric on X#kCP̄². That is a global existence problem. Local isotropy and cone data are exhausted for it.

# Step 83 — The normalized Einstein action on moduli, the Weyl deficit, and degenerations of almost-Kähler Einstein metrics

Agent2, Execute. Inputs: Step-82 handoff (82.K derived in reasoning only), Spirit #98, Step 77 (AAD balance (c)),
LeBrun 2001 \cite{lebrun2001ricci} (Prop. 2.1 (8), Cor. 2.5, proof of Thm 3.3),
Ozuch \cite{ozuch2020higher} (Thm 0.2, remark on subanalytic completion, lines 79–130 of the Knowledge object),
Ozuch \cite{ozuch2021integrability} (Thm 0.4/0.9; real-analyticity of the obstruction projection unknown in degenerate trees, line 812).
Exact algebra: `workspace/scripts/step83_weyl_deficit_algebra.py` → `workspace/data/step83/weyl_deficit_algebra.json` (all residuals 0). TTCS verification: `trace/ttcs/results/step83_ttcs01_verifier1_integration.md` (corrections below are incorporated; an earlier ball-quotient check used the wrong s* convention and has been repaired).
Pending source retrieval (background task s83_t9_tool1): Koiso premoduli analyticity / Besse 12.49, Bando energy identity, Cheeger–Tian, Anderson's subanalytic-completion expectation. Nothing below depends on the energy identity.

## 0. Objects and normalizations

M closed oriented four-manifold. For an Einstein metric g (Ric°=0, s constant):

- normalized Einstein–Hilbert action Ŝ(g)=Vol^{-1/2}∫s dV, so Ŝ² = s²Vol;
- T₊(M)=2χ+3τ, and for Einstein metrics 4π²T₊ = ∫(2|W⁺|²+s²/24);
- **Weyl deficit** D(g) := ∫(s²/24−|W⁺|²) dV.

Then (exact; residual r1)
  (0.1) D(g) = Ŝ²(g)/16 − 2π²T₊(M).
For Kähler metrics of constant scalar curvature |W⁺|²=s²/24, so D=0. For an almost-Kähler Einstein (AKE) metric with self-dual ω, |ω|²=2, Step 77 (c) gives (residual r2)
  (0.2) D(g) = T_AK(g) = ∫(|W₃⁺|²+3q²/32) ≥ 0, with equality iff q≡0 iff g is Kähler.
Hence s²V=32π²c₁²+16T_AK (Step 77) is the statement D=T_AK, and **closed negative Goldberg is the statement that no AKE metric has D>0.**

The moduli space 𝔈(M) is the set of Einstein metrics on M modulo diffeomorphisms and scaling, with the C^∞ topology. D, Ŝ² are diffeomorphism- and scale-invariant (D is scale-invariant in dimension four).

## 1. Ŝ is locally constant on Einstein metrics

**Theorem 83.1.** Ŝ is locally constant on the space of Einstein metrics on M (C^{k,α} topology, k≥2, hence also C^∞). Consequently Ŝ² and D are constant on every connected subset of 𝔈(M), and take only finitely many values on every compact subset of 𝔈(M).

*Proof.* (i) Ŝ is a C¹ (indeed smooth) function on the Banach manifold of C^{k,α} metrics, invariant under diffeomorphisms and scaling, and its critical points are exactly the Einstein metrics (Hilbert): DŜ_g(h)=Vol^{-1/2}∫⟨−Ric+(s/2)g−(s̄/4)g, h⟩dV with s̄ the mean scalar curvature; tracing the critical equation gives s=s̄, and then Ric=(s/4)g. So DŜ_x=0 for every Einstein x.
(ii) Koiso's slice theorem: for Einstein g there is an Isom(g)-invariant slice S_g of volume-normalized metrics and a finite-dimensional real-analytic submanifold Z⊂S_g, T_gZ = infinitesimal Einstein deformations, such that the premoduli P_g=𝓔∩S_g near g is a real-analytic subset of Z, and every Einstein metric C^{k,α}-near g is, after scaling and a diffeomorphism, an element of P_g. (Koiso 1980/83; Besse 12.49; used in the same form for ALE spaces in \cite{ozuch2021integrability} App. B.2.)
(iii) A sufficiently small representative of the analytic germ (P_g,g) is locally conical (Łojasiewicz), so every point x of it is joined to g inside P_g by a finite piecewise-C¹ (subanalytic) path γ. On each C¹ piece d/dt Ŝ(γ(t))=DŜ_{γ(t)}(γ̇)=0 by (i); continuity handles junctions. So Ŝ≡Ŝ(g) on a neighbourhood of g in P_g, hence on a neighbourhood of g among all Einstein metrics.
(iv) The local moduli is P_g/Isom(g) (Isom(g) a compact Lie group; finite when Ric<0 by Bochner); an invariant locally constant function descends. A locally constant function is constant on connected sets and has finite image on compact subsets of the smooth moduli (not of a completion containing orbifolds). For orientation-dependent statements use oriented moduli (orientation-preserving diffeomorphisms, positive scalings). ∎

The argument uses no integrability of Einstein deformations, no Seiberg–Witten theory, and no Kähler structure. It is the standard principle "critical values of an analytic functional are locally constant on its critical set", applied with Koiso's analyticity.

## 2. Kähler–Einstein components contain no strict AKE metric

**Theorem 83.2 (= 82.K).** Let g₀ be a Kähler–Einstein metric on M with s<0, complex orientation equal to the orientation of M, and let g be an Einstein metric in the same connected component of 𝔈(M).
(a) If g is almost-Kähler with self-dual ω (same orientation), then g is Kähler, hence Kähler–Einstein for J_ω.
(b) If g is almost-Kähler for the opposite orientation, then its torsion energy is forced: T_AK(g)=12π²τ(M). Thus no such g exists if τ<0; if τ=0 it is Kähler for the reversed orientation; if τ>0 its torsion energy is the topological number 12π²τ.

*Proof.* (a) D(g)=D(g₀)=0 by Theorem 83.1 and (0.1); by (0.2) T_AK(g)=0. (b) The reversed-orientation deficit D̄=∫(s²/24−|W⁻|²)=Ŝ²/16−2π²(2χ−3τ) is also constant on the component; D̄(g)=Ŝ²(g₀)/16−2π²(2χ−3τ)=2π²(2χ+3τ)−2π²(2χ−3τ)=12π²τ (residual r3), and D̄=T̄_AK for reversed AKE metrics. ∎

*Checks.* For Σ_g×Σ_h (τ=0) the product KE metric is Kähler for both orientations, consistent with (b). For a ball quotient (χ=3τ) the CH metric has W⁺'=0 in the reversed orientation; a reversed AK structure would have s*=s/3=s+q, q=−2s/3, W₃⁺'=0, so T̄_AK=3q²V/32=s²V/24=12π²τ, exactly the forced value (r4=0): the identities are consistent and give no contradiction by themselves. A reversed AK structure on the CH metric is excluded instead by Armstrong's theorem (a compact strictly AK Einstein four-manifold cannot have ω everywhere a W⁺-eigenform; here W⁺'=0), while a reversed Kähler structure would need |W⁺'|²=s²/24>0.

*Relation to known results and novelty.* Theorem 83.1 is a standard consequence of Koiso's analytic premoduli. On a manifold with a negative KE metric and a monopole class, LeBrun's scalar estimate ∫s²≥32π²(c₁⁺)² and its equality rigidity (Prop. 4.1 of \cite{lebrun2001ricci}, citing earlier work; Cor. 2.5 concerns the mixed Weyl estimates) already give the stronger statement that the whole Einstein component consists of KE metrics. Theorem 83.2(a) is the SW-free version for the almost-Kähler structure actually present; 83.2(b) is an opposite-orientation reformulation of established identities. These are short consequences, recorded because they place the Goldberg problem on the moduli space: a strict AKE metric satisfies Ŝ²>32π²(2χ+3τ) and lives in a component of 𝔈(M) containing no KE metric. The substantive new content of this note is the no-concentration Theorem 83.5 and its use in §§3–5.

## 3. Transfer of the Weyl deficit through noncollapsed degeneration

Setting (N): g_n Einstein on M, s≡s₀<0 (so Vol=Ŝ²/s₀²), uniformly noncollapsed, diameters bounded. By Anderson / Bando–Kasue–Nakajima / Tian orbifold compactness (cf. \cite{anderson2003orbifold}), a subsequence converges in Gromov–Hausdorff sense to a compact Einstein orbifold (V,g_V) with finitely many singular points S, smoothly (after diffeomorphisms) on compact subsets of V∖S. Bishop–Gromov gives Vol(B_δ(S_n))≤Cδ⁴, so Vol(g_n)→Vol(V) and Ŝ²(g_n)→Ŝ²(V). Since ∫|Rm|²=8π²χ for Einstein metrics (curvature-operator norm), the measures |W⁺|²dV_n and the other quadratic curvature densities (uniformly bounded total mass) have weakly convergent subsequences; boundary radii are chosen away from atoms.

**Lemma 83.3 (deficit transfer).** In setting (N), with m:=lim_δ lim_n ∫_{B_δ(S_n)}|W⁺|² ≥ 0 (the W⁺ energy concentrated at S, including all bubbles and necks),
  D(V) = lim D(g_n) + m ≥ limsup D(g_n),  T₊(M) = T₊^{curv}(V) + m/(2π²),
where T₊^{curv}(V)=(1/4π²)∫_V(2|W⁺|²+s²/24) (an orbifold curvature number, not the underlying-space 2χ+3τ). These are measure-defect formulas; no bubble energy identity is used. In the inherited charge notation C₊ := −m/(2π²) ≤ 0.

*Proof.* Split ∫_M|W⁺|² over M∖B_δ(S_n) (smooth convergence) and B_δ(S_n); use volume convergence and constancy of s. ∎

**Corollary 83.4 (Spirit #98, KE-orbifold endpoints).** Let 𝒞⊂𝔈(M) be connected (e.g. a component or a branch) and suppose some sequence in 𝒞 satisfies (N) with a limit V that is Kähler–Einstein for the induced orientation (more generally any limit with D(V)≤0). Then the constant value of D on 𝒞 is D(V)−m. Every AKE metric in 𝒞 (same orientation) is Kähler; if 𝒞 contains an AKE metric then moreover m=0 (C₊=0) and D(V)=0. If D(V)<0, or if m>0, no AKE metric lies in 𝒞.
*Proof.* D is constant on 𝒞 (83.1) and equals lim D(g_n)=D(V)−m by Lemma 83.3. For g∈𝒞 AKE, 0≤T_AK(g)=D(g)=D(V)−m≤0. ∎ (Without an AKE member, a component with KE endpoint can have D=−m<0.)

This needs no smooth KE metric on M and no Kuranishi computation, and it closes every strict-AKE desingularization branch ending at a KE orbifold, with any Ricci-flat ALE trees in any orientation.

## 4. Almost-Kähler Einstein degenerations do not concentrate

**Theorem 83.5.** Let (g_n,ω_n) be AKE on M (s=s₀<0, self-dual ω_n) in setting (N). After a subsequence:
(a) ω_n→ω_V smoothly on V∖S, and ω_V extends across S as an orbifold almost-Kähler form; (V,g_V,ω_V) is an AKE orbifold;
(b) T_AK(g_n)→T_AK(V) and there is **no concentration** at S, neither of |W⁺|² (m=0) nor of the torsion density |W₃⁺|²+3q²/32;
(c) every curvature-scale bubble obtained by smooth convergence of rescalings at a point of S is Ricci-flat with W⁺=0 (orientation of M), and the rescaled forms (|ω|=√2 kept) converge to a parallel form: all bubbles are orientation-matched Ricci-flat Kähler (Λ⁺-flat) ALE orbifolds;
(d) Ŝ²(g_n)→Ŝ²(V)=32π²T₊(M)+16T_AK(V), T_AK(g_n)→T_AK(V), and T₊^{curv}(V)=T₊(M).

*Proof.* (a) Δω_n=0 and |ω_n|=√2 give uniform C^k bounds by elliptic estimates on compact subsets of V∖S; the limit is closed, self-dual, of length √2. Lift to a punctured chart B⁴∖0; testing (d+d*)ω_V=0 against cutoffs χ_ε gives an error ≤C‖dχ_ε‖_{L¹}=O(ε³)→0, so the equation holds distributionally across 0 and elliptic regularity gives a smooth Γ-invariant extension with the same algebraic properties. (b) Let m_T≥0 be the concentrated torsion density. Splitting gives lim T_AK(g_n)=T_AK(V)+m_T. On each closed g_n, T_AK=D (0.2). On V, (0.2) holds by the same local identity and orbifold Stokes applied to the smoothly extended data. With Lemma 83.3: T_AK(V)+m_T=lim D(g_n)=D(V)−m=T_AK(V)−m, so m_T+m=0 and both vanish. (Two nonnegative defects enter one global identity with opposite signs.) (c) Rescale g'_n=r_n^{-2}g_n, ω'_n=r_n^{-2}ω_n (keeps |ω'|=√2, closed, self-dual). Every fixed compact bubble region lies eventually in B_δ(S_n) for each δ, so scale invariance of ∫|W⁺|² gives ∫_N|W⁺|²≤m=0, and Ric=0 (s₀ scales away). All tree levels and neck regions are inside m; W⁻ concentration is not excluded. The rescaled harmonic forms converge as in (a). Calling the pointed limits ALE uses the usual bubble-tree theorem; the local conclusions do not. For a harmonic self-dual form of constant length on a Ricci-flat metric, the Weitzenböck formula gives |∇ω|²=2W⁺(ω,ω)=0. (d) Lemma 83.3 with m=0 and s²V=32π²T₊+16T_AK. ∎

So torsion and self-dual Weyl energy never escape into bubbles; a degenerating family of AKE metrics produces an AKE orbifold with the same T_AK and Kähler bubbles. Torsion zeros (c₂(E)=5χ+6τ) can however disappear into the bubble regions, where the limiting structure is Kähler.

**Corollary 83.6 (small-torsion alternative).** Let (g_n,ω_n) be strict AKE on M with s=s₀ and T_AK(g_n)→0. Then:
(a) [g_n] leaves every compact subset of 𝔈(M) (finitely many values of D=T_AK>0 on a compact set, Theorem 83.1);
(b) if (N) holds, the limit V is a Kähler–Einstein orbifold (T_AK(V)=0, Theorem 83.5) with at least one singular point (else smooth convergence contradicts (a)), all bubbles orientation-matched Ricci-flat Kähler, and Ŝ²(g_n)=Ŝ²(V)+16T_AK(g_n)>Ŝ²(V), Ŝ²(g_n)→Ŝ²(V): strict AKE metrics approach V from the side of larger normalized volume;
(c) since s₀²V_n=32π²T₊+16T_AK(g_n), a small-torsion sequence requires T₊(M)=2χ+3τ≥0; if T₊=0 the volume tends to zero (collapse); if T₊>0 the volume is bounded below, so bounded diameter gives noncollapse and (N), and the only alternative is diameter divergence. Diameter divergence is not by itself cusp formation. Products of hyperbolic surfaces with a pinching geodesic show that exact negative KE metrics (T_AK=0) diverge in diameter at fixed volume and curvature energy, so (N) is not automatic.

**Proposition 83.7 (finitely many Einstein components near an orbifold ⇒ local torsion gap).** Let V be a KE orbifold in the GH closure of 𝔈(M). Suppose there are arbitrarily small GH-neighbourhoods U of V such that 𝔈(M)∩U has finitely many connected components. (Normalization s=s_V fixed; components in the smooth quotient topology; volume continuity along normalized noncollapsed convergence.) Then all Einstein metrics on M in some GH-neighbourhood of V have Ŝ=Ŝ(V), hence D=D(V)−m=−m≤0 there by Lemma 83.3 along an approximating sequence; in particular that neighbourhood contains no strict AKE metric.
*Proof.* Let U_j↓V with finitely many components; the value sets F_j=Ŝ(𝔈∩U_j) are finite (83.1) and nested, hence stabilize at F_J. Any v∈F_J is attained in every U_j, by metrics converging to V, so v=Ŝ(V) by volume convergence. ∎
The hypothesis holds if the GH-completion 𝔈(M)∪∂_o𝔈(M) is subanalytic near V (Anderson's expectation quoted in \cite{ozuch2020higher}); Ozuch \cite{ozuch2021integrability} notes that real-analyticity of the obstruction projection is unknown for degenerate trees. **Combined with Corollary 83.6, finiteness of Einstein components near KE orbifolds (with Kähler bubble trees) is a sufficient condition for a uniform positive lower bound of T_AK over strict AKE metrics with bounded diameter** (not shown to be necessary). In the A₁ case, Ozuch's Theorem 0.2 \cite{ozuch2020higher} independently forces KE-type curvature at singular points of stable or rigid one-point limits, consistent with Corollary 83.6(b); its exact hypotheses must be checked before combining.

## 5. Consequence for Problem 1: blowups cannot degenerate to Kähler-type orbifolds

**Corollary 83.8.** Let X be a minimal surface of general type, A=c₁²(X), and M=X#k\overline{CP}², k≥1. LeBrun's Prop. 4.2/Thm 4.3 \cite{lebrun2001ricci} give, for every metric on M and every b⁺ (blow-up basic class a=c₁(X)±E₁±…±E_k selected per polarization), ∫|Ric|²≥8π²(A+k). For an Einstein metric |Ric|²=s²/4, so Ŝ²≥32π²(A+k), hence (T₊(M)=A−k)
  D(g) ≥ 4π²k.
If Einstein metrics g_n on M satisfy (N) with limit V, then
  Ŝ²(V)≥32π²(A+k),  T₊^{curv}(V)=A−k−m/(2π²),  D(V) ≥ 4π²k+m.
In particular V is never Kähler in the orientation inherited from M (|W⁺|²=s²/24 gives D(V)=0), an inherited-orientation AKE orbifold endpoint has T_AK(V)≥4π²k, and every concentrated W⁺ energy raises the required deficit of the bulk. Hence no noncollapsed bounded-diameter sequence of Einstein metrics on a nonminimal general-type surface converges to an orbifold Kähler in the inherited orientation, whatever Ricci-flat ALE trees (any type and orientation; Kronheimer, Şuvaina quotients, Wahl-type) occur. A KE bulk with the opposite complex orientation is not excluded by this argument. (Residual r5.)
*Proof.* (0.1) and Lemma 83.3. ∎
This is an immediate consequence of LeBrun's estimates and the measure transfer, not a new estimate. For k≥A/3 LeBrun's Theorem 3.3 already excludes Einstein metrics, so the content is for 1≤k<A/3. LeBrun's approximate metrics on blowups do approach KE orbifold bulks, but they are not Einstein; the identity Ric°=0 is essential.

This is a dependent consequence of LeBrun's scalar estimate plus the transfer lemma; it is not an Einstein nonexistence theorem in the small-blowup range, but it removes the entire Kähler-orbifold desingularization route from Problem 1 and quantifies how far from Kähler any degenerating bulk must be.

## 6. What remains

- Goldberg (Q4): a counterexample lies in a component of 𝔈(M) with constant D=T_AK>0 that contains no KE metric; any connected family containing it has no noncollapsed KE-orbifold endpoint with m>0 or D(V)≤0; its noncollapsed degenerations are AKE orbifolds with the same T_AK and Kähler bubbles. A uniform gap inf T_AK>0 over strict AKE metrics on M follows from (i) finiteness of Einstein components near KE orbifolds (Prop. 83.7) and (ii) exclusion of small-torsion diameter-divergent sequences (T₊>0) or collapse (T₊=0). Neither the existence question nor (i)–(ii) is settled here.
- Theorem 83.5 suggests an orbifold Goldberg problem as the natural closure of the smooth one, and a torsion-zero bookkeeping: zeros of the torsion section counted by c₂(E) can migrate into Kähler bubbles; the orbifold c₂(E) of V and the bubble contributions should be compared.
- Q1: Corollary 83.8 should be combined with the inherited mixed scalar–Weyl transfer (Step 74) and the D_k-root restriction (Step 75) to determine which orbifold bulks can still occur for k<A/3.

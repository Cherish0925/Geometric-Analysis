# Step 85 — Coupled AKE centers at negative KE metrics and orbifolds: the exact length obstruction, holomorphic transport of the mixed term, the neck-trace theorem, and the reduction of A1-endpoint rigidity to one normal coefficient

Agent2, Execute. Inputs: Step 83 (D=T_AK, no-concentration), Step 84 (coupled linearization, formal centers), Spirit #100/#101/#103.
Sources read this Step: Nagy, *Einstein deformations of Kähler–Einstein metrics* (arXiv 2603.09028, `nagy2026einsteina`), Thm 1.6 and §4.4 (lines 95–110, 684–703 of the Knowledge object); Ozuch, *Higher order obstructions* (`ozuch2020higher`), lines 83–147 (first obstruction, kernel of R⁺), 420–430 (GH-close Einstein ⇒ weighted-close to a naive desingularization), Def. A.1; Ozuch, *Integrability…* (`ozuch2021integrability`), Thm 0.4, Rem. 0.5–0.7.
Exact algebra: `workspace/scripts/step85_center_algebra.py` → `workspace/data/step85/center_algebra.json` (all checks pass; listed where used).

Conventions. (M,g,J,ω) Kähler–Einstein, Ric=Eg, E<0, complex orientation, |ω|²=2 (form norm ½ω_{ab}ω^{ab}). H⁺_g = closed self-dual (equivalently harmonic SD) 2-forms; dim H⁺_g=b⁺. On a Kähler surface Λ⁺=Rω⊕Re Λ^{2,0} pointwise orthogonally, and H⁺_g = Rω ⊕ Re H^{2,0}. A metric curve is written g^{-1}g_t = 1+tH₁+(t²/2)H₂+O(t³) (Nagy's convention). Everything below holds verbatim on compact Kähler–Einstein *orbifolds* (orbifold Hodge theory, ∂∂̄-lemma and orbifold canonical bundle); where a step uses a cited manifold theorem this is said.

---------------------------------------------------------------------------------------------------

## 1. The exact nonlinear form of the problem: AKE = Einstein metric + constant-length element of a finite-dimensional space

**Lemma 85.0.** An Einstein metric g on a closed oriented four-manifold carries a compatible almost-Kähler structure with self-dual fundamental form iff the finite-dimensional space H⁺_g contains a form of constant length √2.

*Proof.* A closed SD form is coclosed, hence harmonic; a SD form of constant length √2 is nondegenerate and equals g(J·,·) for a unique g-orthogonal J inducing the orientation. Conversely an AK form with SD ω is closed SD of length √2. ∎

So, for each Einstein metric, the Goldberg question is the vanishing of the **length defect**
λ(g) := min{ ‖|ω|²_g − 2‖_{L²} : ω∈H⁺_g, ⨍|ω|² = 2 },
a continuous function of g with values attained on a compact sphere of a b⁺-dimensional space. The analysis of the coupled pair (g,ω) reduces to (Einstein metric) × (zeros of a length map on a finite-dimensional sphere). This organizes all of §§2–5.

**Proposition 85.1 (exact rigidity of the length map at a negative KE metric or orbifold).** Let (V,g,ω) be a compact KE surface or orbifold with E<0, H := Re H^{2,0}(V). For ω' = aω+β ∈ H⁺_g (a∈R, β∈H):
 |ω'|² = 2a² + |β|² pointwise. (exact)
Hence ω' has constant length iff β = 0. Moreover, with Q₀(β):=|β|²−⨍|β|²,
 ‖Q₀(β)‖_{L²} ≥ c_V ‖β‖²_{L²}  for all β∈H,  c_V>0. (85.1)

*Proof.* ω and Re Λ^{2,0} are pointwise orthogonal, giving the identity. Write β=Re θ, θ∈H^{2,0}; |β|²=½|θ|². If |θ| is a nonzero constant, θ is a nowhere-vanishing holomorphic (orbifold) section of K_V, so K_V is (orbifold-)holomorphically trivial and c₁(V)=0, contradicting Ric=Eg with E<0 (c₁ is represented by (E/2π)ω≠0). Thus Q₀(β)=0 forces β=0. Q₀ is continuous, homogeneous of degree two on the finite-dimensional H; its minimum of ‖Q₀‖ on the L²-unit sphere is positive. ∎

Remark. At an orbifold A1 point p the lifted form θ is Z₂-invariant; dz₁∧dz₂ is invariant under −1, so θ(p)≠0 is allowed. The proof does not use H^{2,0}=0.

---------------------------------------------------------------------------------------------------

## 2. Theorem 85.A — the coupled second-order center equation, including all mixed directions

Let F(g,ω) = (Ric_g − Eg + δ*_gB(g), dω, P⁻_gω, |ω|²_g−2) (Step 84). A *formal second-order AKE jet* through (g,ω) is (g_t,ω_t), g^{-1}g_t=1+tH₁+(t²/2)H₂, ω_t=ω+tβ₁+(t²/2)β₂, with F(g_t,ω_t)=O(t³), modulo simultaneous diffeomorphisms.

**Pointwise algebra (script checks).** For any symmetric H, any b∈Re Λ^{2,0}:
- (A1) d/dt|_{0} |ω|²_{g+tH} = −tr H.
- (A2) ∂_s∂_t|_{0} |ω+tb|²_{g+sH} = 0 (the metric cross term vanishes: ω_{ab}b_c{}^b is antisymmetric because the two endomorphisms anticommute).
- (A3) the first variation of P⁻_g ω vanishes for J-anti-invariant H and for H=g, and is nonzero for J-invariant trace-free H.
- (A4) the first variation of P⁻_g b along J-anti-invariant H is in general nonzero (so a genuine mixed source exists).
- (A5) if H₁ is J-anti-invariant and H₂⁺ = H₁² (any H₂⁻), then P⁻_{g_t}ω = O(t³) and |ω|²_{g_t}=2+O(t³); a J-invariant change of H₂ destroys the first property.

**Theorem 85.A.** Let (V,g,J,ω) be a compact KE surface (or orbifold) with E<0. Every formal second-order AKE jet has, after simultaneous gauge, first-order data (H₁,β₁) with H₁ ∈ 𝓔(V,g) = {h ∈ Sym^{2,−}: ∂̄h=0, δh=0} (Kodaira–Spencer directions) and β₁ ∈ Re H^{2,0}, and the second-order equations are solvable **iff β₁ = 0** (together with Nagy's Einstein equation, which is unobstructed at this order). Precisely: after taking the quotient by every admissible second-order metric and form correction and by simultaneous gauge, the only second-order obstruction is
 Ob₂(H₁,β₁) = Q₀(β₁) ∈ L²₀(V) (functions modulo constants), (85.2)
independent of H₁; the mixed (H₁,β₁) contribution is identically removable, and the pure metric (H₁,H₁) contribution vanishes. With (85.1), ‖Ob₂‖ ≥ c_V‖β₁‖².

*Proof.* Order one. The gauged Einstein linearization forces H₁ ∈ ker Δ_E ∩ TT, which for E<0 equals 𝓔(V,g) (Koiso; Nagy line 97). By (A3) P⁻-variation of ω vanishes, so β₁ is closed and SD, hence harmonic: β₁=cω+Re θ. The length equation 2⟨ω,β₁⟩−tr H₁=0 with tr H₁=0 gives c=0.

Order two, metric. Every formal Einstein 2-jet tangent to H₁ is gauge-equivalent to Nagy's normal form (Thm 1.6; its derivation uses the equations through order two only): H₂⁺=H₁², H₂−H₁² ∈ Sym^{2,−}, plus additions from ker Δ_E (anti-J, trace-free). Simultaneous gauge acts on (H₂,β₂) by (L_Xg, L_Xω); the SD and length residuals are diffeomorphism-covariant, and the pair (L_Xg,L_Xω) solves the linearized SD and length equations (L_X|ω|²=0), so the gauge choice costs nothing.

Order two, self-duality. The t² coefficient of P⁻_{g_t}ω_t is ½β₂⁻ + (DP⁻[H₁]β₁) + [ω-terms]. The ω-terms vanish by (A5) and (A3). The remaining equation is
 dβ₂ = 0,  β₂⁻ = −2 DP⁻[H₁]β₁. (2.1)
*Holomorphic transport.* Put J' := JH₁, J_s=J+sJ', g_s = g+sH₁ = ω(·,J_s·). Since H₁ is anti-invariant, J'J+JJ'=0; since ∂̄H₁=0, J_s is integrable to first order, and g_s is J_s-Hermitian with fundamental form ω. Let θ_s = θ+sθ' be (2,0) for J_s to first order: θ'^{1,1}=ι_φθ is prescribed algebraically (φ the Beltrami form of J'), ∂̄(ι_φθ)=0 because ∂̄φ=0 and θ is holomorphic. Closedness of θ_s requires ∂(ι_φθ)+∂̄θ'^{2,0}=0. The (2,1)-form ∂(ι_φθ) is ∂-exact and ∂̄-closed (∂̄∂=−∂∂̄), so by the ∂∂̄-lemma (compact Kähler manifold or orbifold) ∂(ι_φθ)=∂∂̄ξ=−∂̄(∂ξ); take θ'^{2,0}=∂ξ. Then β_s := Re θ_s is closed, g_s-SD (real part of a (2,0)-form for a Hermitian structure of the given orientation) and pointwise g_s-orthogonal to the J_s-(1,1) form ω, all to first order. Differentiating: β' := ∂_sβ_s solves β'⁻ = −DP⁻[H₁]β₁, dβ'=0, and
 0 = ∂_s⟨ω,β_s⟩_{g_s} = ⟨ω,β'⟩ + (A2-term=0), i.e. ⟨ω,β'⟩ ≡ 0 pointwise. (2.2)
Any solution of (2.1) is β₂ = 2β' + γ with γ ∈ H⁺_g = Rω⊕Re H^{2,0}, so ⟨ω,β₂⟩ = 2c_γ is a constant.

Order two, length. Expanding N(g,ω)=|ω|²_g, bilinear in ω:
 N(g_t,ω_t) = N(g_t,ω) + 2tB_{g_t}(ω,β₁) + t²(|β₁|²+⟨ω,β₂⟩)+O(t³).
N(g_t,ω)=2+O(t³) by (A5); B_{g}(ω,β₁)=0 pointwise and its H₁-derivative vanishes by (A2). So the condition is |β₁|² + ⟨ω,β₂⟩ = 0, i.e. |β₁|² = −2c_γ is constant. Since the set of all length corrections compatible with the other second-order equations is exactly the constants, the obstruction class is Q₀(β₁) ∈ L²₀, and by Proposition 85.1 it vanishes only for β₁=0. ∎

**What this settles.** Spirit #100/#101 asked whether the mixed h–β term is the first variation of harmonic-form transport and whether it preserves the nonconstant ω-component. Answer: yes and yes. The mixed term is the Griffiths-transversal transport of the holomorphic 2-form along the Kodaira–Spencer direction, it exists for every ∂̄-closed direction (no integrability of the complex deformation, no H^{2,0}=0), and it keeps the transported form *pointwise* orthogonal to ω. The obstruction is the single function Q₀(β₁), with the quadratic estimate (85.1). The pure form rotation and every mixed direction are therefore quadratically obstructed; the pure metric directions are not obstructed at this order (Nagy), so a non-Kähler entrance must come from the metric sector (Einstein deformations that are not Kähler for ω), not from rotating ω inside H⁺. Regimes β₁≪t (e.g. β ~ t^{3/2}) are not tangent directions: there the first competing term is the cubic length defect of the transported Kähler form along a non-Kähler Einstein jet, again a metric-sector quantity.

---------------------------------------------------------------------------------------------------

## 3. Theorem 85.B — harmonic self-dual forms across Ricci-flat Kähler ALE degenerations (neck-trace theorem)

**Indicial computation (script B1).** On flat R⁴∖0, closed SD forms have harmonic coefficients in a parallel frame; homogeneous solutions exist exactly in degrees d ≥ 0 and d ≤ −4:
 d = 0,1,2,3: dim 3, 8, 15, 24;  d = −2, −3: dim 0;  d = −4, −5: dim 3, 8.
(Harmonic functions are homogeneous of degree k≥0 or −2−k; the degree-(−2) candidates aω_i r^{−2} are not closed since θ↦θ∧ω_a is injective.) No logarithmic solutions occur (the only possible double root of the Laplacian in R⁴ is at −1, which is not a spherical degree). For a nontrivial Γ ⊂ SU(2) acting trivially on Λ⁺, Γ-invariance kills degree 1 (no invariant linear functions); for Γ ∋ −1 all odd degrees die. On the A1 cone the closed-SD indicial set is {…,−6,−4} ∪ {0} ∪ {2,4,…}: the constant mode is isolated in the gap (−4,2).

**Hypotheses (H).** (M,g_n) converge to a compact orbifold (V,g_V) with isolated singular points p_j, C^∞ on compact subsets of V∖{p_j}; near each p_j the rescaled metrics converge to an orientation-matched Ricci-flat Kähler ALE space N_j asymptotic to C²/Γ_j (one bubble level, W⁺(N_j)=0 so Λ⁺N_j is flat, spanned by the hyperkähler triple); on the neck annuli the metric is, up to a fixed linear map, flat plus an error e_n with r^k|∇^k e_n| ≤ δ_n w(r), ∫_{neck} w(r) dr/r ≤ C, δ_n→0. For Einstein metrics GH-close to an Einstein orbifold this is supplied by Ozuch's theorem (GH-close ⇒ C^{2,α}_{β,*}-close to a naive desingularization, line 420ff, weight r_D^{β}, β>0; the model naive metric itself deviates by O(r²) on the orbifold side and O(|ζ|² r^{−4}) on the ALE side). The ALE orientation matching is exactly what Step 83 proves for AKE degenerations.

**Theorem 85.B.** Under (H):
(i) (uniform L^∞) every ω ∈ H⁺_{g_n} satisfies sup|ω| ≤ C‖ω‖_{L²}, C independent of n;
(ii) (no new SD directions) b⁺(M) = b⁺_orb(V), and H⁺_{g_n} → H⁺_{g_V} (L²-normalized elements subconverge, C^∞ on compacts of V∖{p_j}, to orbifold harmonic SD forms, and every orbifold harmonic SD form is such a limit);
(iii) (common trace, no slow rotation) if ω_n ∈ H⁺_{g_n} converges to ω_V, then on each neck ω_n = c_n + o(1) uniformly for a single constant c_n ∈ Λ⁺ (in the parallel trivialization), c_n → ω_V(p_j), and on the bubble ω_n converges to the parallel form of N_j whose asymptotic value is ω_V(p_j).

*Proof.* (iii) On the flat cone a closed SD form on an annulus A(ρ₁,ρ₂) is a sum of homogeneous solutions of the degrees listed; with |ω| ≤ 1 the growing part is O((r/ρ₂)²) and the decaying part O((ρ₁/r)⁴), and the degree-0 part is a single constant. With metric error e_n, ω satisfies the flat equation with a source bounded by δ_n w(r) r^{−1}; the constant mode is driven only by this source (all nonconstant modes have sphere average zero), so its total variation across the neck is ≤ Cδ_n∫w dr/r → 0. A slowly rotating direction would make dω of size |∂_τ c|/r, which the equation forbids; the vanishing of unnormalized torsion energy (Step 83) is not used. On the bubble, a bounded harmonic SD form has components that are bounded harmonic functions in the parallel frame, hence constant (Yau's Liouville theorem on complete Ric≥0 manifolds); so the bubble limit is parallel and its asymptotic value is c_∞ = lim c_n = ω_V(p_j).
(i) If sup|ω_n|=1 and ‖ω_n‖_{L²}→0, rescale at a maximum point. Exterior: smooth convergence to a bounded harmonic SD orbifold form with zero L² norm but value 1 somewhere — impossible. Bubble or neck: the rescaled limit is a constant of length 1 (Liouville on N_j, resp. bounded closed SD on the whole cone, which by the indicial set is constant); by (iii) this constant propagates through the neck to a region of fixed size in V, giving ‖ω_n‖_{L²} ≥ c > 0 — contradiction.
(ii) Bounded harmonic SD forms on V∖{p} extend over p (removable singularity for bounded harmonic forms in the lifted chart). The L² cohomology of an orientation-matched hyperkähler ALE space is anti-self-dual, so b⁺(M)=b⁺(V)+Σb⁺(N_j)=b⁺(V); with (i) and local convergence the normalized spaces converge. ∎

The theorem uses only closedness, self-duality, W⁺=0 on the bubble, and the indicial gap; it holds for any finite number of sites and for every orientation-matched Kähler ALE filling of C²/Γ, Γ ⊂ SU(2). It does not need the constant-length condition. Multilevel trees are covered by iterating (iii) along each neck provided (H) holds on every neck.

**Corollary 85.B′ (uniform center constant).** For metrics satisfying (H) and admitting Kähler forms (e.g. KE smoothings of V), let c(g_n) be the best constant in ‖Q₀(β)‖ ≥ c‖β‖² on Re H^{2,0}(g_n). Then liminf c(g_n) ≥ c_V > 0. (Minimizers subconverge by (i)–(ii); L² norms of β and of |β|² converge because of the uniform sup bound and the vanishing volume of the cores; the limit is a nonzero element of Re H^{2,0}_orb(V).) Thus the quadratic center estimate of Proposition 85.1 is *uniform as the core scale tends to zero*.

---------------------------------------------------------------------------------------------------

## 4. Consequences for strict AKE metrics approaching a KE A1 orbifold

Let (g_n,ω_n) be AKE on M, noncollapsed with bounded diameter, converging to a negative KE orbifold (V,ω_V) with one A1 point p (EH bubble). By Step 83 the bubble is orientation-matched Eguchi–Hanson, ω_n → ω_V on V∖p (the limit AK form of a KE orbifold with U(2) holonomy is ±ω_V), T_AK(g_n)→0.

**85.C (direction matching).** By 85.B(iii) the parallel limit form on EH has asymptotic value ω_V(p). This removes the Step-84 uncertainty "vanishing L⁴ torsion does not fix the normalized direction across the neck": the closed SD equation fixes the trace, independently of energy.

**85.D (asymptotically Lagrangian vanishing cycle).** At a KE point R⁺(p) = (s/4) I⊗I, I=ω_V(p)/√2, so ker R⁺(p) = I^⊥. By the first desingularization obstruction (Biquard; Ozuch, *Higher order*, lines 83–147: the EH period direction ζ̂ must satisfy ⟨R⁺(p)ζ̂, ω_k⟩ → 0), ζ̂_n → I^⊥. Combined with 85.C, the limiting bubble form ω_b satisfies ⟨ω_b(∞),ζ̂⟩=0: ω_b is a holomorphic-symplectic form of the resolution complex structure, i.e. EH is seen by ω_n as the *smoothing* {xy=z²+c} (sphere Lagrangian), never as the resolution. The vanishing cycle S has ∫_Sω_n = o(t_n) relative to its area scale. In particular the Einstein-normal tilt ζ_I := ⟨ζ,I⟩ is the only parameter by which the core can differ from a Kähler smoothing at leading order.

EH tail (script B2): with Kähler potential φ(u)=√(u²+a⁴)+a²log(u/(a²+√(u²+a⁴))) = u − a⁴/(2u) + O(u^{−3}), the resolution form is ω₁ = ω₁⁰ − (a⁴/2) i∂∂̄(r^{−2}) + O(r^{−8}), whose r^{−4} tail is flat-ASD, while ω₂+iω₃ = dz₁∧dz₂ has no tail. Hence the core form in direction n ⊥ ζ is tail-free; a tilt of n toward ζ produces an ASD r^{−4} tail of size ⟨n,ζ̂⟩a⁴ and a nonzero period, exactly mirroring the metric tilt ζ_I.

**85.E (slaving of the form sector).** By Lemma 85.0, write ω_n = a_n ω̂_n + β_n with ω̂_n ∈ H⁺_{g_n} the continuation of ω_V and β_n in the continuation of Re H^{2,0}_orb(V) (85.B(ii)). Taking nonconstant parts of |ω_n|²=2 and using the uniform estimate,
 c_V(1−o(1))‖β_n‖² ≤ ‖Q₀|ω̂_n|²‖ + 2‖Q₀⟨ω̂_n,·⟩‖_{op}‖β_n‖.
Both right-hand quantities are *metric-sector* defects of the Einstein metric g_n (the failure of the continued Kähler class to be pointwise compatible). At the second-order level they vanish (Theorem 85.A), so form rotation is of strictly higher order than the metric deviation. A strict AKE metric near V can only arise if g_n is a non-Kähler Einstein metric; rotating ω inside H⁺, in the exterior or in the core, cannot create it.

---------------------------------------------------------------------------------------------------

## 5. The metric sector: action excess and the single normal coefficient

**Topology.** For an orientation-matched EH (W⁺=0, s=0) the relative charge of 2χ+3τ is (1/4π²)∫(2|W⁺|²+s²/24)=0, so T₊(M)=T₊(V). Hence for every Einstein g on M,
 D(g) = (Ŝ²(g) − Ŝ²(V))/16 (5.1)
(D(V)=0 because V is KE). For AKE g, D=T_AK, so **a strict AKE metric near V is the same thing as an AKE Einstein metric with positive normalized-action excess over the orbifold**, and Kähler smoothings have zero excess. The same identity holds for any orientation-matched hyperkähler ALE filling (all have W⁺=0, s=0).

**Reduced problem.** By Ozuch, Einstein metrics GH-close to V are perturbations of naive desingularizations; Lyapunov–Schmidt reduction gives a finite-dimensional parameter space P = {(ζ,y)}: EH period ζ ∈ R³ (|ζ| ~ scale², three L² modes o_k), and y in the Einstein-deformation centers of V (anti-J Kodaira–Spencer tensors). Einstein metrics are the zeros of the obstruction map, equivalently the critical points of the reduced normalized action f(ζ,y). Write ζ = ζ_I I + ζ_⊥. The leading obstruction is
 λ_k ∝ ⟨R⁺(p)ζ̂, ω_k⟩ = (s/4)⟨ζ̂,I⟩⟨I,ω_k⟩,
nonzero only in the normal component, with coefficient s/4 ≠ 0; the transverse plane is unobstructed through order o(t²) (Ozuch line 147, dim ker R⁺ = 2).

**Conditional Theorem 85.M (Morse–Bott closure).** Suppose (a) the A1 point of V is globally Q-Gorenstein smoothable and the complex deformations of V are unobstructed, so that KE smoothings exist for all (ζ_⊥,y) near 0 and form, in reduced coordinates, a C¹ graph 𝒦={ζ_I = κ(ζ_⊥,y)} of critical points of f; and (b) the reduced normal derivative satisfies the scale-uniform estimate
 |∂_{ζ_I} λ_I(ζ,y) − c₀ s/(4|ζ|)| ≤ o(1)/|ζ| on a neighbourhood of 𝒦 (c₀≠0 the universal EH constant).
Then every Einstein metric GH-close to V is Kähler–Einstein; in particular no strict AKE metric approaches V.

*Proof.* On 𝒦 the normal obstruction vanishes; by (b) and the mean-value theorem λ_I(ζ,y) = (ζ_I−κ)(c₀s/(4|ζ|)+o(1/|ζ|)), so zeros lie on 𝒦; points of 𝒦 are KE. ∎

The theorem is stated conditionally because (b) — the *C¹* (not merely C⁰) control of the reduced obstruction in the normal variable, uniformly as |ζ|→0 — is exactly the missing uniform inverse; Ozuch's estimates control values of λ_k with errors |ζ|^{1+δ}, not their ζ-derivatives. What has been achieved is that every other sector has been removed: the form centers (Theorem 85.A, Cor. 85.B′, 85.E), the core form rotations and trace (85.B, 85.C), and the transverse EH parameters (Kähler smoothing data, 85.D). The whole endpoint problem at a smoothable unobstructed A1 point is reduced to the derivative of one real function in one real variable, whose leading coefficient is the scalar curvature.

**Where a strict branch could live (construction target).** If (a) fails — the A1 point is not globally smoothable, or the Kodaira–Spencer directions of V are obstructed at third order — then the Kähler locus has codimension >1 in P, while the transverse Einstein obstruction still vanishes through order t² (Ozuch line 147) and Nagy's Einstein jets are unobstructed through second order. These are precisely the configurations in which a non-Kähler Einstein metric near V is not ruled out by any established argument, and (5.1) says such a metric would be strict AKE iff it carries a constant-length SD harmonic form and has positive action excess. Non-smoothable negative KE A1 orbifolds (local-to-global obstruction in H²(T_V)) are therefore the natural search space for a closed strict AKE metric, and the place where Theorem 85.M cannot be closed by Kähler geometry.

---------------------------------------------------------------------------------------------------

## 6. Relation to the full Einstein-gap programme

- Q4 (closed negative Goldberg): proved here — exact nonlinear rigidity of the length map at KE metrics and orbifolds (85.1); the complete second-order coupled center theorem with mixed terms (85.A); the uniform-in-scale harmonic SD theory across Kähler ALE degenerations (85.B), giving direction matching and the asymptotically Lagrangian vanishing cycle. Not proved: closed Goldberg; exclusion of strict components at positive D; the normal-derivative estimate (b); collapse, cusp and diameter-divergent limits.
- Q1: the identity 8π²k − P = 4D_W − (S−32π²A)/4 (Spirit #103; equivalent to D_W = S/16 − P/4 − 2π²(2χ+3τ) with 2χ+3τ=A−k) puts the Einstein candidate (P=0 ⇒ D_W ≥ 4π²k by LeBrun), the strict-saving constructions (P<8π²k with S>32π²A) and Goldberg (D_W=T_AK) into one same-metric quantity. Theorem 85.B does not use almost-Kähler structure: in any noncollapsed Einstein degeneration with orientation-matched Kähler ALE bubbles, harmonic SD forms keep their traces through the necks. Combined with Cor. 83.8 (no inherited-orientation Kähler orbifold endpoints on X#k CP̄²) it constrains Q1 endpoints but does not decide existence.
- Q2/Q3 untouched this Step.

---------------------------------------------------------------------------------------------------

## 7. Complementary test (Spirit #103): two actual monopoles on the same Einstein metric — the route reduces to old balances

TTCS generator branch `trace/ttcs/results/step85_ttcs01_sub1_generator.md` (second branch unfinished; I checked the algebra below). Setting: b⁺>1, M=X#kCP̄², basic classes a and b=a+2e, e=Σ_{j∈J}E_j, r=|J|, so simultaneous supply holds for every metric (blow-up formula; no b⁺=1 chamber used).

- Correct twisting: V_b^± = V_a^± ⊗ E with c₁(E)=e (not E²); relative connection B with A_b = A_a⊗B², f_B=(f_b−f_a)/2. Mixed fields Φ=v⊗u* ∈ E⊗End V_a⁺, σ=⟨u,v⟩ ∈ Γ(E) (a genuine section with zero locus PD(e)).
- Exact identities: |f_B⁺|² = (U+V)²/32 − |σ|²/8; ∫|f_B⁻|² = 4π²r + ∫[(U+V)²/32 − |σ|²/8] ≥ 4π²r; 4π²r = ∫[|σ|²/8 − U(U+V)/16 − ⟨f_B⁻,f_a⁻⟩]. These are the polarization of the two individual Chern–Weil identities (∫f_b²−∫f_a² = 16π²(a·e+e²) = 0), hence contain no new curvature information.
- Mixed Bochner: ∇*∇Φ + (s/2+(U+V)/4)Φ = −2C with C = Σ∇_i^{A_b}v⊗(∇_i^{A_a}u)*; the Weyl version contains only the directional term ⟨W⁺φ,φ⟩, an unsigned relative-curvature term and the derivative correlation C₀. δW⁺=0 does not remove them.
- Equality case: both scalar estimates cannot saturate simultaneously (σ≢0 parallel ⇒ e=0; σ≡0 ⇒ b=−a ⇒ a=−e, contradicting a²>0>e²). This is the known one-field equality rigidity.
- **Corrected after Step 85 (Spirit review):** at the nominal Einstein endpoint D_W=4π²k one has ∫|W⁺|² = (4π²/3)(A−2k)>0, but the slack 4π²(A/3−k) belongs only to the weaker curvature combination S/24+2∫|W⁺|²≥(8π²/3)A. The full mixed inequality already excludes this endpoint for 0<k<A/3: it would require 2√(A+k)+√(A−2k)≥3√A, contrary to strict concavity. In fact the inherited mixed screen gives D_W≥4π²k+(8π²A/9)[1−√(1−3k/A)]². This is an old one-field necessary bound, not a new two-field obstruction; see `spirit_step85_full_mixed_endpoint_correction.md` for the derivation.

Scoped verdict: the examined relative-curvature identities are polarizations of the individual balances, while the mixed Bochner calculation retains uncontrolled relative-curvature and derivative-correlation terms. This calculation has not produced a new Q1 obstruction. Control of f_B⁻ or C₀, or a justified holomorphic/vortex-like equation for σ, could change that judgment; none was obtained here. This delimits the tested bilinear argument, not all consequences of the coupled Einstein–Seiberg–Witten system. The nominal endpoint must be evaluated with the full mixed inequality, as corrected above.

---------------------------------------------------------------------------------------------------

## 8. Operative corrections from the independent verification (`trace/ttcs/results/step85_ttcs02_verifier1_integration.md`; branches `step85_ttcs02_sub1_verifier.md`, `sub2_verifier.md`)

These supersede the corresponding statements above.

1. **85.A statement.** Read it as: a first-order pair (H₁∈𝓔, β₁∈Re H^{2,0}) extends to a second-order Einstein, closed, SD, constant-length jet iff β₁=0. Volume normalization is automatic: for fixed-E Einstein jets 𝒜_E(g)=∫(s−2E)dμ is stationary, so Vol(g_t)=Vol(g)+O(t³), and formal Moser fixes the volume form through order two. Nagy's Thm 1.6 normal form applies to formal 2-jets (its proof uses only order ≤2 equations, normalization Thms 3.9/4.21); H₂⁻ = 𝐡₂ − ½L_{J grad f}J is determined modulo 𝓔, not arbitrary. Orbifold version = adaptation of Nagy's proof, not a cited theorem. Obstruction normalization: Ob₂=Q₀(β₁) for the t²-coefficient (twice that for second derivatives).
2. **A5.** Universal form: with K=H₂⁺−H₁², [P⁻_{g_t}ω]_{t²} = ½DP⁻[K]ω and [|ω|²]_{t²} = −½tr K. A scalar J-invariant change keeps self-duality but breaks the length; a primitive J-invariant change breaks self-duality. Universal variation: DP⁻[H]F = −½∗(½tr H·F − H♯F).
3. **Indicial set, all degrees.** Inversion composed with a reflection maps closed SD forms of coefficient degree d to −d−4; degree −3 ↔ −1 (absent), degree −2 empty by dr∧F=0; Re(z₁^d dz₁∧dz₂) and its inversion realize all d≥0 and d≤−4. A1 set: {…,−6,−4}∪{0,2,4,…}.
4. **85.B(iii) must use moving necks** A(a_nR_n, ρ_n), R_n→∞, ρ_n→0: on a fixed-end neck the orbifold form differs from ω_V(p) by its quadratic Taylor term (counterexample to the literal statement). Rigorous drift control is the **flux law**: with ϑ_i = r^{−4}ι_Xω_i (dϑ_i flat-ASD), F_i(r)=∫_{S_r/Γ}α∧ϑ_i is the sphere average of the i-th coefficient and |c_i(r₂)−c_i(r₁)| ≤ C‖α‖_∞(∫_{r₁}^{r₂} sup|e| dr/r + sup_{S_{r₁}∪S_{r₂}}|e|). Model error r²+a_n⁴r^{−4} gives ρ_n²+R_n^{−4}→0. The uniform L^∞ bound (i) is proved by blow-up plus flux propagation. Deriving (H) from Ozuch's C^{2,α}_{β,*} norm needs an error bound ≲ε_n r_D^{β}, β>0 (Def. A.1 has weight r_o^{−β} in the norm, i.e. decay r^{β}; the "*" part must be checked).
5. **EH tail normalization.** With ω₁⁰=(i/2)∂∂̄u = dx₁∧dx₂+dx₃∧dx₄: ω₁ = (i/2)∂∂̄φ = ω₁⁰ − (a⁴/4) i∂∂̄(r^{−2}) + O(r^{−8}); the tail is flat-ASD (r^{−2} harmonic ⇒ primitive (1,1)). The coefficient −a⁴/2 above mixed conventions.
6. **85.D** holds for the limiting selected complex structure: ∫_{S_n}ω_n = o(|ζ_n|), Area(S_n)≍|ζ_n|; the bubble sphere is special-Lagrangian for the limit form. The first desingularization obstruction is a quoted input (Biquard/Ozuch).
7. **85.M rescaled.** Use the raw obstruction Λ_I(ζ,y) = Aζ_I + O(|ζ|^{1+δ}), A=c₀s/4≠0. The needed estimate is ∂_{ζ_I}Λ_I = A + o(1) on the relevant tube; the angular λ_I=Λ_I/|ζ| has ∂_{ζ_I}(Aζ_I/|ζ|) = A|ζ_⊥|²/|ζ|³, so the earlier hypothesis (b) was mis-scaled. The mean-value formula integrates the derivative along the normal segment; the angular first obstruction places GH-close Einstein metrics in the tube. Smoothing coordinates: on a marked period cover q~ζ₂+iζ₃ and the algebraic parameter c~q² (Weyl ±). Global ℚ-Gorenstein smoothability and unobstructedness do not by themselves give the graph 𝒦 for all (ζ_⊥,y); a local-to-global smoothing map in period coordinates is needed. Failure of smoothability leaves possibilities open; it does not construct a strict branch.
8. **85.E** retains factors a_n², 2|a_n| (a_n→±1). Its higher-order comparison across degeneration needs uniform differentiability; it does not follow from 85.A alone.
9. **Lemma 85.0** needs b⁺>0. At E=0 (flat tori, hyperkähler K3) Prop. 85.1 fails, so E≠0 is essential.

Status after verification. Proved: Lemma 85.0; Prop. 85.1 (manifolds and orbifolds); 85.A for formal jets on manifolds; the all-degree flat indicial classification; the orbifold charge/action identity (5.1). Proved under the explicit neck hypothesis (H): 85.B with moving necks and the flux law, Cor. 85.B′ (on any subspaces converging to Re H^{2,0}_orb(V)), 85.C, and the limiting geometry of 85.D. Conditional: 85.M (scale-uniform raw normal C¹ estimate and the Kähler-smoothing graph). Not established: closed negative Goldberg; exclusion of strict AKE components at positive D; collapse, cusp and diameter-divergent limits.

# Step 62 — The first nonlinear compatibility at a torsion zero: the zero cone and positivity of nondegenerate indices

Agent2, Execute. Inputs: Step-61 review handoff; A02 #849 (exact soldered/half-twistor equation, zero-index determinant, Darboux prolongation in progress); Spirit #72/#73; AAD Weitzenböck formulas; the jet engine of Step 53.
Scripts: `workspace/scripts/step62_zero_prolong.py` (jet engine at a zero, linear analysis, Gibbons–Hawking control, homotopy continuation), `step62_batch.sh`, `step62_batch2.sh`, `step62_phi_identity.py`, `step62_cone_index.py`, `step62_det_formula.py`.
Data: `workspace/data/step62/` (linear analysis `linear.json/.npz`, GH control `gh_D4.json`, `gh_D5.json`, D4 sector continuations `cont_D4_*`, logs), `workspace/data/step62_cone4/` (D4 cone tests), `workspace/data/step62_cone5/` (D5, running at the time of writing), `workspace/data/step62b/` (`phi_prediction.json`, `cone_index.json`).

Labels: [P] proved, [N] exact or high-precision numerical, [O] open.

## 0. Setting and normalizations

(M^4,g,Ω) almost-Kähler, oriented by Ω, |Ω|²=2 (so Ω is a self-dual harmonic form), Einstein Ric=λg, s=4λ; λ of either sign or zero. u=Ω/√2. W⁺ acts on Λ⁺ as an endomorphism with the convention that a Kähler metric has spectrum (s/6,−s/12,−s/12). In the orthonormal splitting Ru⊕u^⊥ write
\[
W^+=\begin{pmatrix} r & \eta^T\\ \eta & -\tfrac{r}{2}I+V\end{pmatrix},\qquad r=\langle W^+u,u\rangle,\quad \operatorname{tr}V=0 ,
\]
with |η|²=Ση_i² and trV² the Frobenius square of V (so trV²=2v² if the u^⊥-block has eigenvalues −r/2±v). q=|∇Ω|². A torsion zero is a point p with ∇Ω(p)=0. Near p, ∇Ω=a⊗φ−Ja⊗Jφ (AAD gauge), and the first jet of the torsion is the real 4×4 matrix ∇a(p); in complex terms f(z)=cz+(S+A)z̄ (A02 #849), with c∈C, S complex symmetric, A antisymmetric, A=[[0,a],[−a,0]].

## 1. Theorem 62.A (zero identity) [P]

**Theorem.** At every torsion zero p of an Einstein almost-Kähler four-manifold (any λ),
\[
|\nabla^2\Omega|^2(p)\;=\;4\,\operatorname{tr}V^2-12\,|\eta|^2 ,\qquad |\nabla^2\Omega|^2=\sum_{k,l}|\nabla_k\nabla_l\Omega|^2 .
\]

*Proof.* (i) Harmonic self-dual Ω: ∇*∇Ω=2W⁺Ω−(s/3)Ω. With |Ω| constant, pairing with Ω gives q=4⟨W⁺u,u⟩−2s/3 everywhere; at p, r=s/6.
(ii) Einstein ⇒ δW⁺=0 ⇒ (Derdziński) ∇*∇W⁺=−(s/2)W⁺+6(W⁺)²−2tr((W⁺)²)Id. At p: (W⁺²)_{uu}=s²/36+|η|², tr(W⁺²)=s²/24+2|η|²+trV², so ⟨(∇*∇W⁺)u,u⟩=2|η|²−2trV².
(iii) At p, since ∇u=0, ∇*∇⟨W⁺u,u⟩=⟨(∇*∇W⁺)u,u⟩+2⟨W⁺(∇*∇u),u⟩, and 2⟨W⁺(2W⁺u−(s/3)u),u⟩=4(s²/36+|η|²)−(2s/3)(s/6)=4|η|². Hence ∇*∇⟨W⁺u,u⟩=6|η|²−2trV².
(iv) q=Σ_i|∇_iΩ|² gives ∇*∇q(p)=−2|∇²Ω|²(p). Combining with (i): −2|∇²Ω|²=4(6|η|²−2trV²). □

All λ-dependent terms cancel; the identity is the pointwise evaluation at Z of the Laplacian of the Weitzenböck identity q=4⟨W⁺u,u⟩−2s/3. (Its integral over M is a torsion balance of AAD type; the term-by-term identification with the Step-55/59 balance has not been written out. Note the Step-59 form norm has |η|²_{59}=2|η|²_{62}, and |W₃⁺|²_{HS}=trV².) The trace-free part of Hess q=2⟨∇T,∇T⟩ produces no comparable restriction, because it is matched by the free trace-free part of ∇²W⁺; only the trace is fixed algebraically by harmonicity of W⁺.

## 2. The admissible first-jet space and the zero cone [P,N]

**Linear space L.** In first-order normal coordinates with Ω(p)=e01+e23, the order-0 system (E1 to degree 2, E2 to degree 1, Ric(p)=λδ) is affine in the 2-jets; the first torsion jets it allows form a linear space L with dim L=10 (`linear.json`). It splits as 2 (C-linear, scalar: c) + 8 (antilinear: B) = 2 (c) + 2 (A) + 6 (S), and (η,W₃⁺)(p) are linear functions of the jet: η is carried exactly by c and V exactly by A; S is invisible to W⁺(p). This independently reproduces A02's soldered-equation structure in a different representation.

**Normalized coefficients.** With m_c,m_A,m_S the components of the (32-component) jet vector, ½|m|²=|∇²Ω|², |η|²=|m_c|²/8, trV²=|m_A|²/4, and |m_c|²:|m_A|²:|m_S|²=4|c|²:2‖A‖²:2‖S‖² (Frobenius norms; checked exactly in `step62_det_formula.py`).

**Exact coframe derivation (TTCS verifier, Step 62; removes the numerical input).** At the zero, with Ω=e01+e23, φ=e02−e13, ψ=e03+e12 and ∇Ω=a⊗φ−Ja⊗ψ, the AAD Ricci identities reduce to da=−R(ψ), d(Ja)=−R(φ). Einstein makes both right sides self-dual; this forces the C-linear part of Df to be scalar and leaves the antilinear part free (2+8=10). Because r=s/6 the scalar part of R on Ω^⊥ cancels, R(φ)=η₁Ω+V₁₁φ+V₁₂ψ, R(ψ)=η₂Ω+V₁₂φ+V₂₂ψ, and comparing with the exterior derivatives of the linear model gives η=(−2c_R,−2c_I), V=[[−2a_I,2a_R],[2a_R,2a_I]] (signs gauge-dependent): |η|²=4|c|², trV²=8|a|²=4‖A‖², while S contributes nothing. With |∇²Ω|²=4‖Df‖²_R=4(4|c|²+2‖A‖²+2‖S‖²), Theorem 62.A becomes exactly (2.1). This also proves that the SVD-defined S/A split of the script coincides with the transpose split used in the determinant. (In the script the array named `Mmat` is N^φ=2∇a, not ∇a; signs and the stated m-norms are unaffected.) Theorem 62.A becomes
\[
\Phi:=2|m_c|^2-\tfrac12|m_A|^2+\tfrac12|m_S|^2=0
\quad\Longleftrightarrow\quad
\boxed{\ \|A\|^2=8|c|^2+\|S\|^2\ } \tag{2.1}
\]
(`phi_prediction.json`: eigenvalues of Φ are exactly 2 on c, −½ on A, ½ on S).

**Corollary 62.B (first-jet structure at zeros) [P].** At a torsion zero:
1. pure c (η-only), pure S (curvature-invisible) and pure A first jets are all excluded unless they vanish; a nonzero first jet always has A≠0, hence W₃⁺(p)≠0, and trV²=‖∇²Ω‖²/4+3|η|²;
2. if W₃⁺(p)=0 then ∇²Ω(p)=0 and η(p)=0: the zero is of order ≥2;
3. |W⁺|²−s²/24=2|η|²+trV²>0 at every zero with nonzero first jet.

**Corollary 62.C (positivity of nondegenerate indices) [P].** A02's determinant (verified exactly here)
\[
\det{}_{\mathbb R}Df=|c|^4-|c|^2(\|S\|^2-\|A\|^2)+|\det B|^2,\qquad B=S+A,
\]
restricted to (2.1) is det=9|c|⁴+|det B|². Since |det S|≤‖S‖²/2 and |a|²=‖A‖²/2=4|c|²+‖S‖²/2, one has |det B|≥|a|²−|det S|≥4|c|², hence
\[
\det{}_{\mathbb R}Df\;\ge\;25|c|^4\ \ (\ge 0).
\]
Therefore **every nondegenerate torsion zero of an Einstein almost-Kähler four-manifold has local index +1**. Degenerate zeros with nonzero first jet occur exactly when c=0, S has equal singular values (|det S|=‖S‖²/2) and det S=−a²; the Ricci-flat Gibbons–Hawking zero is of this type. Negative-index first jets, which exist in the linear algebra off the cone (about 10.5% of random off-cone jets, `cone_index.json`), are excluded by (2.1); 200 000 on-cone samples gave no negative determinant and min det/|m|⁴>0.

This answers, at the first nonlinear order, the question raised by Spirit #70/#73 and A02 #849. The symmetric mode S is not free: it is tied to A by (2.1), and the A mode must dominate both S and c. The mixed c+S negative-index sector is the one that is killed.

## 3. Numerical confirmation that (2.1) is the complete first nonlinear compatibility [N]

Engine: unknown Taylor jets of (g,Ω) with g=δ+O(|x|²), Ω=Ω₀+O(|x|²) (this gauge is exactly a torsion zero, since Γ(p)=0); equations ω^Tg⁻¹ω=g to degree D, dω=0 to degree D−1, Ric=λg to degree D−2, plus a prescribed first torsion jet. Homotopy continuation t·m from the Kähler germ (t=0) to t=1 with Levenberg–Marquardt and warm starts.

Controls:
- the exact Kähler germ converges to residual² ~1e−30;
- the exact Ricci-flat Gibbons–Hawking jets (w+iv=1+ε(x+iy)², coordinates (x,y,τ,z), Ω=w dx∧dy+dτ∧dz) give residual 0 (floating evaluation of exact symbolic coefficients) at D=4,5. Their first jet lies in L with c=0 and |m_A|=|m_S|=2√2, so Φ=0 exactly. GH has η=0, so it tests the trV² coefficient and the A/S balance; the −12|η|² coefficient is tested by the c+A cone runs below and proved by the exact coframe calculation of §2.

D=4 results (`data/step62/cont_D4_*`, `data/step62_cone4/`), final residual² at t=1:

| target first jet | λ=−1 | λ=0 |
|---|---|---|
| pure c | 1.6e−3, 8.9e−4 (2 seeds) | 2.1e−3 |
| pure A | 1.4e−4 | 3.2e−4 |
| pure S | 1.2e−4, 1.3e−4 | 2.0e−4 |
| mixed c+S, det<0 | 3.2e−4 | 9.8e−4 |
| generic in L | 1.1e−5 | — |
| GH jet (Φ=0, degenerate) | 2.2e−30 | 8.3e−31 |
| cone, A+S (c=0) | 1.9e−30 | — |
| cone, c+A (S=0) | 1.3e−30 | — |
| cone, generic c+A+S (2 seeds) | 1.1e−30, 1.3e−30 | 5.6e−31 |

The failing residuals scale like t⁴ at small t, as a quadratic obstruction should (pure c, λ=−1: 8.2e−6, 1.2e−4 at t=0.2, 0.4). All on-cone jets, including nondegenerate ones with det>0 and both values of λ, are compatible through D=4. So within this order the admissible first jets are exactly the quadric cone (2.1) in the 10-dimensional L.

D=5 (`data/step62_cone5/`), λ=−1, all on the cone: A+S 8.9e−28, c+A 1.5e−29, generic cone (det 0.0038>0) 7.0e−30, GH jet 1.4e−28; the target first jets and determinants are reproduced exactly. Off-cone jets are excluded at every D≥4 because the D=4 equations are a subset. D=6 results (`data/step62_cone6/`) sharpen the numerical picture. Two generic nondegenerate cone seeds at lambda=-1 reached residual-squared 1.08e-28 and 9.05e-29 at t=1, with target determinants 0.0037963753 and 0.0147112100. The same first seed at lambda=0 reached 1.43e-28. The eta=0 A+S cone target at lambda=-1 initially stalled at t=0.2 (1.04e-7) but recovered from t=0.4 onward and ended at 7.27e-28 with determinant 0.0076849151. The degenerate GH target at lambda=-1 was poorly conditioned at several homotopy points but ended at 3.93e-15 with first-jet mismatch 3.6e-9; this is compatible with, but far weaker than, the exact lambda=0 GH control. Thus every tested cone sector has a D=6 numerical continuation at negative lambda, while the exact GH solution remains only a Ricci-flat control. These are floating finite-order solutions, not formal or analytic germs.

These are floating-point LM continuations: sampled compatibility, not an exact proof that the cone is the complete obstruction at these orders, and not a formal or analytic germ. The index theorem uses only the necessary relation (2.1) and does not depend on this completeness.

## 4. What this changes

- The total charge 5χ+6τ>0 on a closed negative AKE manifold is now consistent with a strong local sign law: nondegenerate zeros all contribute +1. A closed counterexample whose zeros are all nondegenerate would have exactly 5χ+6τ isolated zeros, each with W₃⁺≠0, |W⁺|²>s²/24, and ‖A‖²=8|c|²+‖S‖². The local index restriction does not by itself contradict the global charge; it removes the negative-index mechanism and the pure-S curvature-invisible zeros.
- The source that Spirit asked about is absorbed exactly by the trace-free part of ∇²W⁺; the only first-order nonlinear restriction is the trace identity. The next genuine information must come from higher order (D≥5: Bianchi relations between ∇²W⁺ and ∇³Ω), from degenerate zeros (c=0, equal singular values of S), or from a global argument using that every nondegenerate zero carries W₃⁺≠0.
- λ does not enter Theorem 62.A. Any sign-of-λ obstruction must appear at higher order or globally; the Ricci-flat Gibbons–Hawking/Tod zeros show that order-one degenerate zeros genuinely occur when λ=0.
- Comparison with A02's Darboux computation should be made through the invariant cone (2.1) and the index law, not raw ranks.

## 5. Further mechanisms (TTCS generator, Step 62; unverified unless marked)

1. **Second-order zeros.** If T(p)=0 and ∇T(p)=0, then W⁺(p) is Kähler-type and the same Laplacian argument at the next order is claimed to give |∇³Ω|²(p)=4Σ_i trV_i²−24Σ_i|η_i|², with ∇_iW⁺=[[0,η_i^T],[η_i,V_i]]; again λ-independent. To be verified and combined with the degree-two half-twistor equation.
2. **Poincaré–Hopf for q.** Every torsion zero is a minimum of q (gradient index +1). If all zeros are nondegenerate (hence N=5χ+6τ zeros) and the other critical points of q are isolated, then the critical points of q in the strict region carry total gradient index χ−N=−2(2χ+3τ)<0. Any closed counterexample therefore needs at least 2(2χ+3τ) odd-Morse-index strict critical points (or negative-Euler-characteristic critical surfaces, as the complete example's genus-g bolt maximum shows). An even-index theorem for Hess q at strict critical points of AKE metrics would contradict this.
3. **SU(2) nut test (construction).** At an SU(2)-fixed nut the invariant first jets are f=cz+Az̄ (S=0); the cone gives ‖A‖²=8|c|² and det=25|c|⁴>0. A triaxial cohomogeneity-one Einstein metric dt²+Σa_i²σ_i² with Ω=Σx_iω_i, closure (x_ia_ja_k)'=2x_ia_i, regular nut and nonzero cone amplitude would be a local negative-scalar strict AKE germ with an isolated index-+1 torsion zero, ruling out any universal local exclusion of zeros. At T² or U(2) fixed points every invariant first jet vanishes. The Step-57 metric-only class-A machinery (n=(1,1,1), three directions) is the natural exact tool.
4. **Weighted charge.** Σ_p h(p)ind_p(T)=∫h e(E)−∫dh∧T̂*Ψ (angular form) turns localization into an exact identity; it needs a signed estimate of the second term.

## 6. Open [O]

1. D=5/6 compatibility on the cone for λ<0 versus λ=0 (running), and the structure of the next restriction if one appears.
2. Existence of an actual negative AKE germ (formal or analytic) with an isolated nondegenerate zero. Finite-order compatibility is not a germ.
3. Degenerate zeros: classify the stratum c=0, |det S|=‖S‖²/2, det S=−a² and its higher-order index contribution; zeros with vanishing first jet need the analogous identity at the next order.
4. A global use of W₃⁺≠0 at zeros, for example combined with the localization {λ_min≤s/6} or with the AAD balance.

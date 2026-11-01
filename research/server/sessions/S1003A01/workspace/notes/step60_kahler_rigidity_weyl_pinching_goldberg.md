# Step 60 — Weyl localization of the torsion charge, Kähler rigidity, and the closed negative Goldberg problem on locally symmetric manifolds

Agent2, Execute. Inputs: Step 59 charged-zero formulation (`step59_chiral_completion_and_zero_charge.md`), the updated collection section `sec:fino-complete` (the complete Bianchi-VIII pair transferred to the additive group R^4, answering Fino's existence question), AAD local-models paper (Knowledge object `Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a`), Spirit #70.

Conventions. (M^4,g) closed, oriented by the almost-Kähler (AK) form Ω, |Ω|^2=2, so Ω is a self-dual harmonic form. W^± act on Λ^± as curvature-operator endomorphisms; a Kähler surface has W^+ = diag(s/6, -s/12, -s/12) with the Kähler form as s/6-eigenform. q=|∇Ω|^2, T=∇Ω. Einstein: Ric=λg, s=4λ.

## 1. The torsion charge lives where W^+ is at least Kähler-sized

The Weitzenböck formula for the harmonic self-dual form Ω,
\[
0=\nabla^*\nabla\Omega-2W^+(\Omega)+\tfrac s3\Omega ,
\]
paired with Ω and using |Ω|^2 = const gives the pointwise identity
\[
q = 2\langle W^+\Omega,\Omega\rangle-\tfrac{2s}{3}. \tag{1.1}
\]
Since ⟨W^+Ω,Ω⟩ ≥ 2λ_min(W^+),
\[
q\;\ge\;4\bigl(\lambda_{\min}(W^+)-\tfrac s6\bigr). \tag{1.2}
\]

**Theorem 60.1 (Weyl localization of Nijenhuis zeros).** Let (M,g,Ω) be a closed almost-Kähler Einstein four-manifold with s<0. Then the zero set Z of ∇Ω (equivalently of the Nijenhuis tensor) is nonempty and
\[
Z\subset\Sigma_-:=\{x:\lambda_{\min}(W^+_x)\le s/6\},\qquad
\langle W^+\Omega,\Omega\rangle\big|_Z=\tfrac s3 .
\]
At each zero the Rayleigh quotient of W^+ on Ω/√2 equals the Kähler value s/6; in particular |W^+|^2 ≥ s^2/24 on Z. The relative Euler class of T is supported in Σ_-: T is a nowhere-zero section of E=Λ^{0,1}⊗Λ^{0,2} over M∖Σ_-, and ⟨c_2(E),[M]⟩ = 5χ+6τ>0 is carried by Σ_-.

*Proof.* Nonemptiness: Armstrong/Kim (nowhere-zero N forces 5χ+6τ=0) together with 5χ+6τ = χ+2(2χ+3τ)>0 for closed Einstein metrics with s≠0 (Step 58/59). The inclusion and the value on Z are (1.1)–(1.2) at q=0. A trace-free symmetric 3×3 matrix with an eigenvalue ≤ s/6<0 has squared norm ≥ s²/36+2(s/12)² = s²/24. □

**Full pointwise identity (Step 61 review, verified).** Write W^+ in the splitting R(Ω/√2)⊕Ω^⊥ with diagonal entry r=⟨W^+u,u⟩=s/6+q/4 (u=Ω/√2), transverse block η, and trace-free part W_3^+ of the Ω^⊥ block. Then
\[
|W^+|^2-\frac{s^2}{24}=|\eta|^2+|W_3^+|^2+\frac{sq}{8}+\frac{3q^2}{32}. \tag{1.3}
\]
At a zero (q=0) this is |W^+|^2-s^2/24=|η|^2+|W_3^+|^2. Three different threshold relations must be kept apart at a zero: (i) the Rayleigh identity r=s/6 holds at every zero; (ii) λ_min(W^+)=s/6 requires η=0 and that the two eigenvalues -s/12±|W_3^+| of the Ω^⊥ block stay ≥ s/6 (i.e. |W_3^+|≤|s|/4); nonzero η forces λ_min<s/6 strictly; (iii) norm equality |W^+|^2=s^2/24 forces η=W_3^+=0, i.e. the full Kähler-type operator diag(s/6,-s/12,-s/12). Theorem 60.1 localizes the charge in {λ_min≤s/6} but by itself gives no quantitative Weyl-energy payment, no restriction of local indices, and no placement of charged zeros on either equality stratum. (Step 62 computes what the first nonlinear compatibility adds.)

**Corollary 60.2 (pinching exclusion).** A closed Einstein four-manifold with s<0 and λ_min(W^+)>s/6 everywhere (in particular |W^+|^2<s^2/24 everywhere) carries no almost-Kähler structure compatible with g and inducing that orientation, Kähler or not. Special cases: W^+≡0 with s<0 (q ≡ -2s/3 is a nonzero constant), hence every compact real-hyperbolic 4-manifold (W≡0) in either orientation, and every compact complex-hyperbolic surface with the orientation opposite to its complex one (there W^-_I≡0).

*Sharpness and the complete control.* Kähler–Einstein metrics lie exactly on the boundary: λ_min(W^+)=s/6 and |W^+|^2=s^2/24 identically. For the complete Bianchi-VIII/Fino pair (s=-12, s/6=-2), exact computation (`workspace/scripts/step60_pinching_control.py`, output `workspace/data/step60/pinching_control.json`) gives
\[
w_1+2=\frac{6(p+1)^3(3p^3+3p^2-3p+1)}{(3p^2+1)^3},\quad
w_2+2=\frac{6(1-p)^3(1+3p+3p^2-3p^3)}{(3p^2+1)^3},\quad
w_3+2=\frac{6(21p^6-3p^4+15p^2-1)}{(3p^2+1)^3},
\]
all positive on 1/3<p<1 (the cubic factors have no root in the open interval; `Poly.count_roots(1/3,1)` in the script counts the closed interval and so includes the endpoint root p=1; the labels were corrected in Step 62), and
\[
|W^+|^2-\frac{s^2}{24}=-\frac{18(1-p^2)^3(189p^6-207p^4+87p^2-5)}{(3p^2+1)^6}<0,
\]
since f(u)=189u^3-207u^2+87u-5 is increasing in u=p² (discriminant of f' negative) with f(1/9)>0. The script also confirms (1.1) exactly: 2(X_1w_1+X_2w_2)-(-4+q/2)=0. Thus the complete pair lies strictly inside the pinched region at every finite point and reaches λ_min=s/6, |W^+|^2=s^2/24 only at the infinite end, exactly where q→0. Corollary 60.2 is therefore a genuinely global statement: the open pinched region supports complete strict AKE geometry, and only the positive charge on a closed manifold excludes it.

Interpretation. Section 1 converts Armstrong's existence of a zero into curvature information: a closed strict AKE metric must somewhere have self-dual Weyl curvature at least as large, along the direction Ω, as a Kähler–Einstein metric. The noncompact example escapes by placing its Kähler-type curvature at infinity.

## 2. Compatible AK structures of a compact Kähler surface (same orientation)

**Lemma 60.3 (Apostolov–Drăghici; see the survey \cite{apostolovcurvature}).** Let (M,g,I,ω_I) be a compact Kähler surface and Ω an almost-Kähler structure compatible with g inducing the complex orientation. Then Ω is parallel; hence (g,Ω) is Kähler. If g is not Ricci-flat, Ω=±ω_I.

*Proof.* Λ^+=Rω_I⊕[[Λ^{2,0}]] is a parallel splitting and on a compact Kähler manifold harmonic forms decompose by type. Hence Ω=fω_I+Re θ with fω_I a harmonic (1,1)-form and θ a harmonic, hence holomorphic, 2-form. d(fω_I)=df∧ω_I=0 forces f constant (wedging with ω_I is injective on 1-forms). Pointwise orthogonality gives |Ω|^2=2f^2+c|θ|^2, so |θ| is constant. For a holomorphic section of a Hermitian holomorphic line bundle with Chern connection, ∇θ=∂log|θ|^2⊗θ on {θ≠0}; constant norm forces ∇θ=0. Either θ≡0, or θ is a parallel trivialization of K_I, which makes the Ricci form zero. In both cases Ω is parallel. □

Remark (deformation picture, derived, consistent with the lemma). At a compact KE surface with λ<0 the linearized AKE space is (symmetric harmonic Beltrami differentials = Koiso's Einstein deformations) ⊕ Re H^{2,0}; the second summand rotates Ω inside H^+ with the metric fixed to first order. The second-order closure/norm condition on these directions reduces to i∂∂̄(|σ|^2ω_I)=0 modulo ∂∂̄-closed cross terms Re(c ι_μσ), i.e. Δ|σ|^2=0, which fails unless σ=0. This is the infinitesimal shadow of Lemma 60.3; it is not used below.

## 3. Opposite orientation on a Kähler metric: the commuting pair

Let (g,I) be Kähler and J an AK structure compatible with g inducing the opposite orientation. Self-dual and anti-self-dual complex structures commute, so P=-IJ is a symmetric involution and TM=D_+⊕D_- orthogonally, both I-invariant, with J=I on D_+ and J=-I on D_-. Writing ω_±=ω_I|_{D_±},
\[
\omega_I=\omega_++\omega_-,\qquad \Omega_J=\omega_+-\omega_- ,
\]
so ω_± are closed rank-two forms. Hence D_∓=ker ω_± are smooth I-invariant involutive plane fields whose leaves are I-complex curves, automatically minimal. **Correction (Step 61 review).** These are not, in general, holomorphic foliations: the line subbundles D_±^{1,0}⊂T^{1,0}M need not be holomorphic. If the orthogonal projector Π onto D_+ satisfied ∂̄_IΠ=0, then self-adjointness of Π and compatibility of the Chern (= Levi-Civita) connection would give ∇Π=0, i.e. the parallel splitting — which is the desired product conclusion, not a free input. The Tod/AAD local models have closed complementary rank-one forms with a nonparallel splitting. Baum–Bott or Brunella theory therefore cannot be invoked until transverse holomorphicity is derived from further equations. Conversely an orthogonal pair of I-invariant integrable distributions with minimal leaves gives a closed Ω_J (Rummler-type). ∇J is equivalent to the pair of second fundamental forms of the two leaf families, so

**Proposition 60.4.** Opposite-orientation AK structures compatible with a Kähler metric ↔ ordered orthogonal pairs of complementary smooth I-invariant involutive plane fields with minimal leaves. J is Kähler iff both are totally geodesic, iff g is locally a Riemannian product of two surfaces.

**Established representation (Apostolov–Drăghici–Moroianu \cite{apostolov2001splittinga}; survey \cite{apostolovcurvature} §5.3).** For a KE metric h with Ric=λh and such a splitting, h_{a,b}=a h|_{D_+}+b h|_{D_-} is Kähler for I, almost-Kähler for the opposite structure, has unchanged Ricci form (ω_{a,b}^2=ab ω_I^2), and constant Ricci eigenvalues λ/a, λ/b. Conversely a Kähler surface with two distinct constant Ricci eigenvalues gives a KE metric with a commuting opposite AK structure. The splitting theorem covers nonnegative eigenvalues; the compact nonproduct alternative with negative eigenvalues remains open, and is known to require a minimal surface of general type with ample canonical bundle and even positive signature. The rescaling therefore re-expresses, rather than solves, the opposite-orientation KE Goldberg question.

**Topological limitation (Spirit #73).** With x=c_1(D_+^{1,0}), y=c_1(D_-^{1,0}) the two canonical classes are -(x+y) and -(x-y) up to sign; their squares are controlled by χ and τ (xy=χ, x^2+y^2=3τ in the relevant normalization), but the mixed pairing x^2-y^2 is not. Opposite-orientation actual supply alone thus does not reproduce the inherited Kodaira cross-pairing argument; a global route here needs control of x^2-y^2, i.e. of the nonparallel splitting itself.

For an Einstein Kähler metric, (1.1) in J's orientation reads q=2⟨W^-_IΩ_J,Ω_J⟩-2s/3. Cohomologically [ω_I]=[ω_+]+[ω_-] with [ω_±]^2=0 and [ω_+]·[ω_-]=Vol, so for KE with λ<0 the canonical class is a positive sum of two isotropic classes represented by closed semipositive rank-one (1,1)-forms. The unresolved case of Goldberg on Kähler–Einstein metrics is precisely: does a compact negative KE surface that is not locally a product admit such a non-totally-geodesic orthogonal pair? Corollary 60.2 excludes it whenever λ_min(W^-_I)>s/6 everywhere.

## 4. Consequences for locally symmetric metrics and for whole manifolds

**Theorem 60.5.** Let (M,g) be closed and locally symmetric with s<0.
1. g real hyperbolic: no compatible AK structure in either orientation.
2. g complex hyperbolic: the compatible AK structures are exactly ±ω_I.
3. g locally H^2×H^2: every compatible AK structure is Kähler (± the product Kähler forms ω_1±ω_2 on a finite cover preserving the factors).

*Proof.* (1),(2 opposite orientation): Corollary 60.2. (2 same orientation) and (3): Lemma 60.3 applied in each orientation that carries a Kähler structure for g, after passing to the finite cover on which the factor structures are defined; Kählerness is local. □

**Corollary 60.6 (closed negative Goldberg on hyperbolic and complex-hyperbolic manifolds).** Inputs (C. LeBrun, *Einstein metrics and Mostow rigidity*, Math. Res. Lett. 2 (1995) 1–8, \cite{lebruneinsteinb}; theorem statements read from the registered record in Step 61): Theorem 1 (Besson–Courtois–Gallot): on a smooth compact quotient M of H^4 every Einstein metric is λφ^*g_0; Theorem 2 (LeBrun): on a smooth compact quotient of CH_2 every Einstein metric is λφ^*g_0, φ a diffeomorphism. No b_+ restriction appears in the displayed statement. Then:
- a closed manifold diffeomorphic to a compact real-hyperbolic 4-manifold admits no almost-Kähler Einstein structure for any metric;
- on a closed manifold diffeomorphic to a compact complex-hyperbolic surface every almost-Kähler Einstein structure is Kähler, and is the standard one up to diffeomorphism, scale and sign.

This settles Problem 4 over all metrics and all AK structures on these manifolds. On locally H^2×H^2 manifolds it settles Goldberg for the symmetric metric; the general statement reduces to uniqueness of Einstein metrics there. On a minimal general-type surface X the same-orientation case reduces to the question whether every Einstein metric on X is Kähler, and the opposite-orientation case to Proposition 60.4.

Literature status: Lemma 60.3 is likely classical; Corollary 60.2 is an immediate but apparently unrecorded consequence of Armstrong's theorem; whether Corollary 60.6 is recorded is being checked (knowledge task s60_t6_tool1). Olszak's local theorem already excludes AK structures on constant-curvature metrics, so item (1) is classical locally; the global charge argument is what removes the W^+=0 case on reversed ball quotients.

## 5. What this changes in the programme

- Problem 4 now has a complete answer on two infinite families of closed negative Einstein manifolds and a sharp curvature localization of every hypothetical closed counterexample: its torsion zeros, which carry total charge 5χ+6τ>0, sit inside {λ_min(W^+) ≤ s/6}, where W^+ is at least Kähler-sized. Any counterexample is non-Kähler as a Riemannian metric in the Ω-orientation (Lemma 60.3), and in the opposite orientation of a KE metric it must be a non-product orthogonal pair of holomorphic-curve foliations.
- The complete Bianchi-VIII/Fino pair is exactly sharp for this localization: strictly pinched at every finite point, with λ_min(W^+)→s/6 and q→0 only at infinity.
- Next mathematics: (a) combine the localization with the zero-germ analysis: at a zero, ⟨W^+Ω,Ω⟩=s/3 and Σ_- must carry the charge; the first nonlinear compatibility at a zero is computed in Step 62 (`step62_torsion_zero_prolongation.md`); (b) Proposition 60.4 for KE metrics: decide whether a non-totally-geodesic orthogonal pair of minimal I-complex plane fields can exist on a compact negative KE surface; this requires new control of ∂̄_IΠ (equivalently the negative constant-Ricci-eigenvalue alternative), not foliation theory applied to an assumed holomorphic splitting; (c) for Problem 1, any Einstein metric on a nonminimal general-type surface that is almost-Kähler for a symplectic form must be strictly almost-Kähler (KE is impossible there), so Q1 and Q4 meet in strict AKE metrics on blowups.

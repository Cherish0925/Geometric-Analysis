# Independent review of weak-source Weyl compactness

Date: 2026-09-19. Reviewed `round2_weak_curvature.md` and executed `round2_weak_curvature_check.py`; all symbolic identities pass. This review independently checks the negative-norm and regularity arguments, which the script does not prove.

## Verdict and corrections

The conditional theorem is supportable under its stated fixed-domain uniform ellipticity, uniform `C^{1,alpha}` bounds, and `C¹` metric convergence. A common harmonic gauge for the sequence is not needed. Harmonic coordinates can be constructed for the limit only, after the weak curvature limit is identified.

The script has a real normalization-label issue: `normA=trace(A*A)` is the Hilbert--Schmidt norm squared, whereas its print strings call it `|A|op` and its high-frequency example says `||A0||op=1`. If `op` means the spectral operator norm, that example's numerical factor is false: `diag(1,-1,0)` has spectral norm one but Hilbert--Schmidt norm squared two. Replace those labels by `HS`, and normalize the Fourier example by `||A0||HS=1`. The actual polynomial identities are correct.

The localized estimate must retain a fixed interior support, or an explicit cutoff/buffer, as the note does. It is not a boundary-free estimate for arbitrary functions on the whole coordinate ball.

There is also a strengthening: the separate uniform `L²` bound on `W+` can be recovered locally from the other hypotheses. A detailed argument appears below. This strengthening is not needed for the original conditional theorem, but removes an unnecessary input.

## 1. Exact symbol

The declared self-dual basis has two-form norms squared two and full component contractions

\[
 \sum_{ij}(\omega_a)_{ij}(\omega_b)_{ij}=4\delta_{ab}.
\]

For `W(A)=(1/2)sum A_ab omega_a tensor omega_b`, it follows that `|W(A)|full²=4|A|HS²`. At `xi=dx0`, the first contraction of the three omega forms produces an orthonormal set in the remaining index, so

\[
 |\sigma_D(dx^0)A|^2=|A|_{\rm HS}^2.
\]

Orthogonal covariance proves the arbitrary-covector formula. The checker independently confirms its polynomial expansion in every trace-free symmetric matrix direction. The homogeneous negative Sobolev Fourier identity is therefore correct, with the constant mode removed. This is injectivity of the first-order symbol, not a claim that the divergence detects every unrestricted first jet pointwise.

## 2. The weak Cotton estimate

The Cotton tensor involves one covariant derivative of `E=Ric+g` and its trace, with first derivatives of the metric in the connection coefficients. In the specified chart, integration by parts expresses its action on an `H¹_0` test tensor as the `L²` pairing of `E` with a linear combination of the test tensor and its first derivatives. Uniform ellipticity and bounded first metric derivatives control the coefficient functions, frame conversion and volume density.

Consequently

\[
 \|D_jA_j\|_{H^{-1}(U)}\le C\|E_j\|_{L^2(U)}
\]

uses no derivatives of `E_j`. Self-dual projection is algebraic in the metric, and its differentiated coefficients are controlled by the same `C¹` hypothesis. The manuscript's Cotton factor and sign convention have no effect on compactness, but the claimed factor `1/2` is consistent with the stated four-dimensional convention.

## 3. Why the localized negative-order estimate is valid

Write `D=P^a(x)partial_a+Q(x)` with `P` of class `C¹`, `Q` continuous, and injective principal symbol. For a function supported in a sufficiently small interior ball, freezing the principal coefficients gives the constant-coefficient estimate

\[
 \|u\|_2\le C(\|P^a(x_0)\partial_a u\|_{H^{-1}}+\|u\|_{H^{-1}}).
\]

Rewrite the coefficient error as

\[
 (P^a(x)-P^a(x_0))\partial_a u
 =\partial_a[(P^a(x)-P^a(x_0))u]-(\partial_aP^a)u.
\]

The first term has `H^{-1}` norm at most the coefficient oscillation times `||u||2`; shrink the ball to absorb it. Multiplication by the fixed continuous functions `partial P` and `Q`, followed by the compact inclusion `L²→H^{-1}`, is a compact operator `K:L²→H^{-1}`.

The needed compact-perturbation step can be made explicit: for every `eta>0`,

\[
 \|Ku\|_{H^{-1}}\le\eta\|u\|_2+C_\eta\|u\|_{H^{-1}}.
\tag{R1}
\]

Otherwise one can normalize a violating sequence to `||u_j||2=1` and obtain `u_j→0` in `H^{-1}`. A weakly convergent `L²` subsequence has weak limit zero, while compactness gives `Ku_j→0`, a contradiction. Thus no unsupported assertion that continuous coefficients multiply arbitrary `H^{-1}` distributions is needed for these lower-order terms.

Absorb the first term in (R1) and cover a fixed interior support by finitely many such balls. Cutoff commutators are lower order. This proves precisely

\[
 \|u\|_2\le C(\|Du\|_{H^{-1}}+\|u\|_{H^{-1}})
\tag{R2}
\]

on that interior support. The constant depends on the fixed coefficient geometry and buffer, as it must.

The operator difference estimate in the note is also correct: principal coefficient differences converge in `C¹`, and zeroth-order differences converge uniformly. Integrating the principal difference by parts gives

\[
 \|(D_j-D_\infty)u\|_{H^{-1}}\le o(1)\|u\|_2.
\tag{R3}
\]

No second metric derivatives enter the coefficient convergence.

## 4. The curvature bound is locally recoverable

Here is a stronger form of the conditional convergence argument.

Because `g_j→g_infinity` in `C¹`, the Christoffel symbols converge uniformly. The curvature formula

\[
 R_j=\partial\Gamma_j+\Gamma_j\Gamma_j
\]

therefore converges strongly in `H^{-1}` on the fixed coordinate domain. Lowering indices, taking Ricci traces, subtracting trace terms, and making the algebraic self-dual frame identification multiply these distributions by coefficient fields converging in `C¹`. Such multiplication is continuous on `H^{-1}`. Hence the matrix fields representing the Weyl half satisfy

\[
 A_j\longrightarrow A_\infty\quad\text{strongly in }H^{-1}_{\rm loc}.
\tag{R4}
\]

This conclusion requires no a priori curvature `L²` bound. Initially `A_infinity` is a distribution.

Choose a smooth cutoff `chi` supported strictly inside a larger chart. Apply (R2) to `chi A_j`, and use the exact decomposition

\[
 D_\infty(\chi A_j)
 =(D_\infty-D_j)(\chi A_j)
 +\chi D_jA_j+[D_j,\chi]A_j.
\tag{R5}
\]

The first term is `o(1)||chi A_j||2` by (R3) and is absorbed. The second term tends to zero in `H^{-1}` by the Ricci residual assumption. The commutator is multiplication by `P_j^a partial_a chi`, which is uniformly `C¹`, so its `H^{-1}` norm is bounded by (R4). The last norm `||chi A_j||H^{-1}` in (R2) is bounded for the same reason. It follows that

\[
 \sup_j\|\chi A_j\|_2<\infty.
\tag{R6}
\]

Now subtract (R5) for indices `j,k`. The operator-difference terms tend to zero using (R6), the Ricci-source terms tend to zero, and the commutator terms tend to zero by `C¹` coefficient convergence and (R4). Equation (R2) shows that `chi A_j` is Cauchy in `L²`. Thus the full sequence converges strongly locally, not just a chosen subsequence.

The initially stated uniform `L²(W+)` assumption can therefore be omitted if the fixed-chart `C¹` convergence and the small `L²` Ricci residual are retained. The same proof applies separately to the other Weyl half. It does not produce the controlled charts in an arbitrary collapsed sequence; that geometrical hypothesis remains substantial.

## 5. Weak Einstein regularity does not require a common harmonic gauge

First identify the limit in the original chart. The uniform `C^{1,alpha}` bound passes to the `C¹` limit, so `g_infinity` is `C^{1,alpha}` and uniformly positive definite. Strong `H^{-1}` curvature convergence and `Ric(g_j)+g_j→0` in `L²` give

\[
 \operatorname{Ric}(g_\infty)=-g_\infty
\]

as a distributional tensor. All distributional products involved are legitimate because their coefficient multipliers are `C¹`.

Next, on a smaller ball construct harmonic coordinate functions for this single limit metric, using the uniformly elliptic scalar divergence-form Laplace operator. Its coefficients are `C^{1,alpha}`. Local elliptic regularity gives coordinate functions of class `C^{2,alpha}`; choosing a sufficiently small ball makes their Jacobian nondegenerate. The transformed metric remains `C^{1,alpha}`.

In these coordinates the distributional Einstein equation is the harmonic-coordinate system

\[
 -\tfrac12g^{ab}\partial_a\partial_b g_{ij}
 +Q_{ij}(g^{-1},\partial g)=-g_{ij}.
\tag{R7}
\]

To justify the bootstrap without presupposing second derivatives, rewrite the principal term in divergence form. The new lower-order term `(partial_a g^{ab})(partial_b g_ij)` and the right side are `C^{0,alpha}`; the principal coefficients are Lipschitz. Interior weak elliptic regularity first gives `W^{2,p}` locally for finite `p`, after which the ordinary nondivergence Schauder estimate applied to (R7) gives `C^{2,alpha}`. Iteration makes the metric smooth in this harmonic atlas.

No coordinate change for every `g_j` is needed. The strong curvature convergence and spectral condition were established in the original fixed chart; the single limit coordinate change preserves these tensorial conclusions. If one replaced the stated uniform `C^{1,alpha}` hypothesis by unquantified low-regularity convergence, this bootstrap would need a separate regularity justification. Under the current hypotheses it is valid.

## 6. The final local contradiction

Strong `L²` convergence transfers the squared ordered spectral-distance condition. Eigenvalues of real symmetric matrices depend Lipschitz-continuously on the matrix in Hilbert--Schmidt norm. After smoothing the limit in its harmonic atlas, the target spectrum holds everywhere on the inner ball by continuity.

The checker's added orbit first-jet calculation supplies a direct route to parallelness: its Gram eigenvalues are `1` and `3`, each with multiplicity four, while the squared jet norm is `2sum z_i²`. Hence divergence vanishing forces every orbit-tangent first-jet component to vanish. This applies because the eigenvalues are fixed and the eigenvalue multiplicities are fixed locally. It is a stronger statement on this eight-dimensional restricted jet space than the general principal-symbol calculation.

For `A0=diag(-1/6,1/12,1/12)` and scalar curvature `-4`, the algebraic reaction is

\[
 (s/2)A_0-6A_0^2+2|A_0|^2I=-\tfrac32 A_0\ne0.
\]

A parallel Weyl operator cannot satisfy that Einstein Weitzenbock equation. This is a local contradiction and uses no closed-manifold integration. It remains conditional on actually obtaining the controlled patch and the transferred calibration spectrum from the original research problem.

## 7. Supplement: bounded full curvature supplies the patch despite collapse

I independently reviewed the new section 9 of `round2_rigidity.md`,
including its stronger averaged-defect proposition and localized
degeneration consequence. Both arguments are valid as stated. Here
`F=dist_HS(W+,O0)^2`, and all constants are existential.

**Local geometry and boundary buffer.** Choose a fixed exponential radius
`rho=rho(K)` below the conjugate radius supplied by `|sec|<=K`. On the
tangent ball, `h=exp_p^*g` is a smooth metric and the exponential map is a
local isometry, even when it is highly noninjective on the base. Gauss's
lemma gives `d_h(0,v)=|v|`, and the source exponential map at 0 is the
radial identity. Rauch bounds give uniform metric equivalence to the
Euclidean ball and uniform interior volume lower bounds. All balls used
for the local volume-to-injectivity and harmonic-radius estimates must
have a larger compactly contained buffer; the note explicitly provides
it. Thus incompleteness at the outer boundary is harmless. The resulting
interior harmonic coordinates have a fixed radius and uniform
ellipticity and `C^{1,alpha}` bounds, without a base injectivity bound.

**Multiplicity transfer, without a global cover.** Choose `3s<rho` with
the closed source `3s`-ball compactly contained in the development. For
`q,y` in the base `s`-ball, lift a fixed path `q -> p -> y` of length
less than `2s` from every source preimage of q in the source `s`-ball.
Every lift stays inside the source `3s`-ball. Compact containment and the
local inverse property ensure continuation; uniqueness of the reversed
lift ensures distinct terminal points. Consequently

    m_s(q) <= m_(3s)(y),
    m_s(q) Vol B_s(p) <= Vol_h B_(3s)(0).

The area formula then proves (30). No global covering, deck group, or
uniform bound on the individual multiplicities is required. Compactness
of the buffer makes each relevant fiber finite. The source volume ratio
is uniformly bounded by Rauch comparison. The displayed `3^4 Q0^8`
constant is conservative but valid.

**Averaged Ricci residual is sufficient.** Let
`H=|Ric+g|^2+F`. Under the global full-curvature bound, Bishop--Gromov
comparison and Fubini give

    integral_M average_(B_s(p)) H <= D_K(s) integral_M H.

Indeed `q in B_s(p)` implies
`Vol B_s(q) <= Vol B_(2s)(p) <= D_K(s) Vol B_s(p)`.
Therefore a sequence with `average_M H -> 0` admits centers whose ball
averages tend to zero. The preceding transfer gives vanishing integrals
on a fixed-size harmonic chart. The Ricci residual tends to zero in L2,
which is precisely sufficient for the weak-curvature convergence proved
above; uniform pointwise Ricci pinching is not needed here. Strong L2
Weyl convergence and the vanishing F integral produce the excluded
Einstein germ. This proves

    average_M [|Ric+g|^2+F] >= c0(K) > 0.

The claimed consequence for `delta^2+average F` follows from
`|Ric+g|^2<=4delta^2`. The monopole corollary additionally uses the stated
manuscript density budget; its coefficient comparison with 675 is
consistent.

**Localized degeneration.** If `delta_j -> 0` and `average F_j -> 0`,
suppose the set of centers with `sup_(B_R(p))|Rm|<=K` had volume fraction
at least `alpha>0`. The global Ricci lower bound from delta gives the
same Fubini estimate. Restricting its center integral to this set selects
a center with ball average at most
`(D_1(s)/alpha) average_M F_j`. Choose the exponential radius additionally
below `R/4`, and retain the compact source `3s` buffer. Every source point
then maps into the base curvature-controlled region. Uniform smallness
of the Ricci residual and the same local argument give a contradiction.
Thus (32) follows. It states that the fixed-R neighborhood of the
high-curvature set occupies asymptotically full volume; it does not give
a positive volume lower bound for the high-curvature set itself.

These conclusions do not establish the unrestricted Yau26 assertion.
Neither an integrated curvature budget nor small Ricci defect supplies
the fixed-scale pointwise full-curvature bound used to obtain this local
geometry.

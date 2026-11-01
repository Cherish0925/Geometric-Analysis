# Spirit follow-up to Step 57: an exact real point, rational coordinates, and the global distinction

These are focused algebraic consequences of the Step-57 files, intended to simplify Core's geometric verification. They do not replace an independent check of the Einstein/closure conventions, a proof of the smooth bolt extension, or a literature identification. The full closed Goldberg problem is unchanged.

## 1. An exact point for local ODE existence

In the Step-57 variables take

\[
(W_1,W_2,W_3)=(-1/15,1,192/245),\qquad
(h_1,h_2,h_3)=(176/147,656/735,76/147).
\]

Direct exact substitution into **every** generator of `data/step57/two_lift_P1.txt` gives zero. The original polynomial definitions give

\[
Q=256/105>0,\qquad
(\mu_1,\mu_2,\mu_3)=(-54/35,2/7,-128/245),
\]
\[
(X_1,X_2,X_3)=(5/32,27/32,0),\qquad
q=27648/12005>0.
\]

Thus real nonemptiness and strict positivity do not depend on a scan or on inferring that a polynomial not in an ideal is nonzero somewhere real. With the checked vector field, the reported exact tangency `D(P) subset P`, and the closure lemma, ordinary analytic ODE existence is enough to obtain a local genuine pair. Neither completeness, exhaustive characteristic-zero decomposition, primality of the lift, nor a classification of all invariant solutions is needed for this existence argument. Reconstruct positive radii by `a_i=1/sqrt(|W_j W_k|)` with `n=(-1,1,1)` and choose positive square roots of the two nonzero X_i on a small interval. The pair has |Omega|^2=2, whereas its coefficient vector has Euclidean norm 1.

## 2. Rationalize the curve instead of integrating near its endpoints

Set
\[
p=-\frac{\tan(\phi/2)}{\sqrt3},\qquad 1/3<p<1.
\]
Then
\[
\cos\phi=\frac{1-3p^2}{1+3p^2},\qquad
\sin\phi=-\frac{2\sqrt3p}{1+3p^2}.
\]
The existing angular parametrization simplifies to
\[
u=W_1/W_2=\frac{(p-1)(3p-1)}{(p+1)(3p+1)},\qquad
v=W_3/W_2=-\frac{48p^2(p-1)}{(3p+1)(3p^2+1)^2},
\]
\[
\widehat Q=\frac{192p^2(3p-1)}{(p+1)^2(3p+1)(3p^2+1)}.
\]
Here `u` is a projective W-coordinate, not the torsion notation used in other notes. With the Ric=-3g normalization, the candidate metric becomes
\[
g=G(p)dp^2+A_1(p)\sigma_1^2+A_2(p)\sigma_2^2+A_3(p)\sigma_3^2,
\]
where
\[
G=\frac{4(3p^2+1)}{(1-p)^2(1+p)^2(3p-1)(3p+1)},
\]
\[
A_1=\frac{4(3p-1)(3p^2+1)}{3(1-p)(1+p)^2},\quad
A_2=\frac{4(3p+1)(3p^2+1)}{3(1-p)^2(1+p)},\quad
A_3=\frac{64p^2}{(1-p)(1+p)(3p^2+1)}.
\]
The weights are
\[
X_1=\frac{(1-p)^3(3p+1)}{16p^3},\qquad
X_2=\frac{(1+p)^3(3p-1)}{16p^3}.
\]
They are positive and sum to one on the whole interval. These formulas were obtained by exact symbolic simplification of the saved h(W), Q, and angular parametrization, not from fitting numerical data. They give a particularly small direct verification target.

## 3. Bolt representation matters

Writing `delta=p-1/3`, the formulas give
\[
G\sim\frac{9}{8\delta},\quad A_1\sim\frac92\delta,\quad
A_2,A_3\longrightarrow6.
\]
For outward geodesic distance t from this endpoint,
\[
\delta=\frac29t^2+O(t^4),\qquad A_1=t^2+O(t^4).
\]
More specifically,
\[
A_2-A_3=
\frac{4(3p-1)^2(3p^3+3p^2+9p+1)}{3(p-1)^2(p+1)(3p^2+1)}
=\frac{10}{3}t^4+O(t^6),
\]
\[
X_2=\frac83t^2+O(t^4).
\]
This order-four anisotropy is relevant, not cosmetic. For the structure constants `(-1,1,1)` and a collapsing generator with period 2pi, the adjoint circle rotates the horizontal plane with weight two; its trace-free symmetric metric component has weight four. Evenness and equality of the two limiting radii alone do not ensure smoothness. The displayed factorization is consistent with the required stronger vanishing. Check the actual group/cover convention and the mixed form in a nonsingular polar frame: `x2=O(t)` and `Omega -> w1` alone are not a proof of the form's smooth extension.

## 4. A precise possible global discriminator

The Step-57 torsion expression simplifies exactly to
\[
q(p)=|\nabla\Omega|^2
=\frac{36(1-p^2)^3}{(1+3p^2)^3},\qquad
q'(p)=-\frac{864p(p-1)^2(p+1)^2}{(3p^2+1)^4}.
\]
It is strictly positive in the interior, tends to 32/3 at the bolt, and tends to zero only at the infinite end. If the pair extends smoothly and completely as proposed, any quotient preserving the pair retains this positive invariant and its unattained zero infimum; it cannot be compact. This is a statement about this pair, not a general nonexistence theorem for closed AKE metrics.

In the fixed invariant orbit measure the volume density is
\[
\frac{dV}{dp}=\frac{64p(3p^2+1)}{3(1-p)^3(1+p)^3}.
\]
Thus q~(9/2)(1-p)^3 and dV/dp~(32/3)(1-p)^(-3) near p=1. On a compact lattice quotient of each orbit, both integral q and integral q^2 converge despite infinite total volume. Consequently one should not assume that familiar integrated torsion identities fail merely because the end is noncompact.

For example, **conditional on the presently numerical claim W^-=0 in the stated chirality**, the Einstein radial sectional curvatures determine the W^+ eigenvalues and give
\[
|\eta|^2=-\frac{18(p-1)^3(p+1)^3(3p-1)(3p+1)}{(3p^2+1)^4},
\]
\[
|W_3^+|^2=\frac{81(p-1)^4(p+1)^4(3p-1)^2(3p+1)^2}{2(3p^2+1)^6},
\]
with eta in the form-norm convention of Step 55. Exact integration of the resulting rational expression gives
\[
\int_{1/3}^{1}\left(|\eta|^2+2|W_3^+|^2+\frac{3q^2}{16}-\frac32q\right)\frac{dV}{dp}\,dp=0.
\]
This is a lead for Core to confirm after checking chirality; it is not an independent proof of W^-=0. It suggests that the known AK balance may genuinely survive on this noncompact example rather than produce a contradiction.

The stronger connection to the closed problem is the zero set. The inherited characteristic-class argument forces a Nijenhuis zero on any closed negative-Einstein AKE four-manifold. A validated local strict branch rules out a universal local no-go on q>0; it does not rule out a local rigidity theorem at q=0, a global obstruction to adjoining the required zeros, or an actual-field comparison. The old randomly fitted q(0)=0 jets did not decide any of those questions. No quantitative lower cost for isolated zeros follows from topology alone.

## 5. Literature status

The focused follow-up Knowledge request returned no source that identifies or excludes this specific example; its sole returned article concerned smooth structures and Einstein metrics rather than the requested AKE ansatz. Armstrong's actual full text was not obtained. Novelty remains unresolved and should be separated from geometric validity and from relevance to the closed problem.

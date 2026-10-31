# Step 8: cover-mean transport, Naber–Zhang interface, and corrected model scope

## 1. Research position

Fix a critical Ishida–LeBrun four-manifold and suppose, for contradiction, that

\[
\delta_i=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_{L^\infty}\to0.
\]

The established near-saturation identities provide a nonnegative calibrated deficit density

\[
F_i=|\operatorname{Ric}_{g_i}+g_i|^2
 +(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i,
\]

where, with

\[
\alpha=\sqrt{2/3},\quad u_i=|W_i^+|,\quad w_i=\lambda_{\min}(W_i^+),
\]

\[
f_i=\frac23s_i-2\alpha u_i,\qquad
b_i=\frac23s_i+2w_i,
\]

\[
\mathcal G_i=f_i^2-(\min\{b_i,0\})^2\ge0.
\]

For fixed topology,

\[
\int_M F_i\,d\mu_i\to0.
\]

A noncollapsed unit ball would yield a smooth local Einstein limit carrying

\[
\operatorname{Spec}(W^+)=(-1/6,1/12,1/12),
\]

which is impossible by the constant-spectrum projector identity and the Einstein–Weyl formula. Thus any hypothetical fixed-topology sequence is everywhere collapsed at unit scale. The remaining task is not to classify it by exact symmetric models. It is to show that a positive-volume set of collapsed points unwraps at a fixed scale to harmonic charts while preserving small *normalized* deficit.

## 2. Correction to the old total-integral argument

The argument in `step7_orbit_volume_negative_einstein_collapse.tex`, lines 167–181, is invalid. If a covering region has degree or effective multiplicity \(D_i\), then

\[
\int_{\widehat U_i}\pi_i^*F_i=D_i\int_{U_i}F_i
\]

for a complete degree-\(D_i\) lift. One cannot delete \(D_i\) and bound the cover integral by the total downstairs integral. A collapsed product \(U\times S^1(\ell_i)\) makes the issue explicit: a fixed nonzero density has integral \(O(\ell_i)\) downstairs but \(O(1)\) on a fixed unwrapped patch.

The correct invariant is a local mean. On a full finite-sheeted lift of a domain, numerator and volume both multiply by the degree, so the mean is preserved. On a cover ball, the multiplicity is nonconstant and needs comparison.

## 3. Normal-cover mean-transfer lemma

Let \((M^n,g)\) satisfy

\[
\operatorname{Ric}_g\ge -(n-1)K g.
\]

Let \(U\supset\overline{B_{4r}(p)}\) be open and let

\[
\pi:(\widehat U,\hat g)\to(U,g)
\]

be a connected normal Riemannian cover, endowed with its intrinsic length metric, such that \(B_{3r}(\hat p)\) is relatively compact in \(\widehat U\). (Global completeness of \(\widehat U\) is unnecessary; this interior condition is what the local Bishop–Gromov argument uses.) For \(\hat p\in\pi^{-1}(p)\) and every nonnegative measurable \(\phi\),

\[
\boxed{
\fint_{B_r(\hat p)}\pi^*\phi\,d\hat\mu
\le
\frac{V_{-K}^{(n)}(3r)}{V_{-K}^{(n)}(r)}
\fint_{B_r(p)}\phi\,d\mu.}
\tag{T}
\]

Here the balls upstairs use the intrinsic metric of the cover.

### Proof

Every \(x\in B_r(p)\) has a lift in \(B_r(\hat p)\), obtained by lifting a minimizing geodesic from \(p\). Choose a Borel section

\[
s:B_r(p)\to B_r(\hat p),\qquad \pi\circ s=\mathrm{id},
\]

and set \(S=s(B_r(p))\). By the area formula,

\[
\hat\mu(S)=\mu(B_r(p)).
\]

Let

\[
N(2r)=\#\{\gamma\in\Gamma:d(\hat p,\gamma\hat p)<2r\}.
\]

If two lifts of the same point both lie in \(B_r(\hat p)\), the corresponding deck element displaces \(\hat p\) by less than \(2r\). Hence the multiplicity of
\(B_r(\hat p)\to B_r(p)\) is at most \(N(2r)\). The sets \(\gamma S\), for these deck elements, are pairwise disjoint and lie in \(B_{3r}(\hat p)\). Therefore

\[
N(2r)\mu(B_r(p))\le \hat\mu(B_{3r}(\hat p)).
\]

The multiplicity formula then gives

\[
\begin{aligned}
\fint_{B_r(\hat p)}\pi^*\phi
&\le
\frac{N(2r)}{\hat\mu(B_r(\hat p))}
\int_{B_r(p)}\phi\\
&\le
\frac{\hat\mu(B_{3r}(\hat p))}{\hat\mu(B_r(\hat p))}
\fint_{B_r(p)}\phi.
\end{aligned}
\]

Bishop–Gromov upstairs proves (T). No bound on the sheet number is needed: multiplicity is cancelled by the volume of disjoint deck translates.

The cover must be a genuine normal cover of a buffered base domain, and the radius-
\(3r\) cover ball must remain in its interior. An arbitrary truncated cover patch need not be preserved by deck transformations, so the argument does not apply there. A measurable selection theorem is enough; the earlier assertion that closest-lift tie sets are smooth hypersurfaces is unnecessary.

## 4. Selecting small local means

Under a Ricci lower bound, fixed-radius balls satisfy uniform relative volume comparison. For \(F\ge0\), Fubini and Bishop–Gromov give, for fixed \(a>0\),

\[
\frac1{\operatorname{Vol}M}
\int_M\left(\fint_{B_a(p)}F\right)d\mu(p)
\le C(n,K,a)\frac1{\operatorname{Vol}M}\int_MF\,d\mu.
\tag{A}
\]

Consequently, on any set \(S_i\) with

\[
\operatorname{Vol}(S_i)\ge\eta\operatorname{Vol}(M,g_i),
\]

there is \(p_i\in S_i\) with

\[
\fint_{B_a(p_i)}F_i\to0.
\]

A local Hardy–Littlewood maximal estimate can strengthen this to points whose centered balls are simultaneously good across a prescribed finite range of radii, but a single fixed radius suffices for the Naber–Zhang interface below.

## 5. Precise Naber–Zhang interface

Naber–Zhang Proposition 6.4 applies to bounded-Ricci balls which, at a fixed scale, are GH-close to

\[
\mathbb R^{k-\ell}\times Z^\ell,\qquad \ell\le3,
\]

and whose fibered fundamental group has maximal rank \(4-k\). It yields, on the local universal cover of \(B_1(p)\), a lower \(C^1\)-harmonic radius at every lift of a point in \(B_1(p)\). For a sequence, the lower bound is uniform only when the model noncollapsing radius \(r_c(Z,z)\) has a uniform positive lower bound.

Fix \(a<1/3\). If \(p_i\) satisfies these uniform GH/model/rank hypotheses, apply (T) to the universal cover of \(B_1(p_i)\):

\[
\fint_{B_a(\tilde p_i)}\pi_i^*F_i
\le C\fint_{B_a(p_i)}F_i\to0.
\]

The harmonic radius lower bound at \(\tilde p_i\) gives a fixed chart contained in this cover ball. In harmonic coordinates,

\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=-2(\operatorname{Ric}_{g_i})_{jk}+Q_{jk}(g_i^{-1},\partial g_i).
\]

Finite \(W^{2,p}\) compactness and the equation \(\operatorname{Ric}_{g_i}=-g_i+o_{L^\infty}(1)\) give, on a smaller chart, strong finite \(W^{2,p}\) convergence to a smooth metric \(g_\infty\) with

\[
\operatorname{Ric}_{g_\infty}=-g_\infty.
\]

The small cover mean of the full nonnegative density forces

\[
s_\infty=-4,
\qquad |W^+_\infty|=1/(2\sqrt6),
\qquad \mathcal G_\infty=0.
\]

At these calibrated values, \(\mathcal G=0\) forces the least eigenvalue \(-1/6\); trace-free and norm identities give the other two eigenvalues \(1/12,1/12\). This produces the already-excluded local Einstein germ.

### Supported conditional theorem

For a fixed critical Ishida–LeBrun sequence, let \(S_i(r_*)\) be the points satisfying, at unit scale:

1. a Naber–Zhang GH model with residual dimension \(\ell\le3\);
2. model noncollapsing radius at least \(r_*>0\);
3. maximal fibered nilpotency rank.

Then

\[
\frac{\operatorname{Vol}(S_i(r_*))}{\operatorname{Vol}(M,g_i)}\to0.
\tag{NZ-exclusion}
\]

The proof is (A), (T), Proposition 6.4, and the forbidden-germ argument. It uses neither Cheeger–Tian curvature decomposition nor an exact torus/nil orbit model.

The remaining geometric question is now precise: can almost all unit-scale collapsed points fail every fixed \(r_*>0\) version of these hypotheses? Such failure can arise through rank drop, degenerating lower-dimensional model scale, residual four-dimensional cores, or unwrapping only at radii tending to zero. At a shrinking radius the Einstein constant scales to zero, so the calibrated negative-Einstein contradiction does not persist automatically.

## 6. Corrected scope of the orbit-volume model results

The orbit-volume identities remain useful model theorems, but they do not establish that an arbitrary pinched sequence reduces to these models.

### 6.1 Exact abelian adapted models

For an exact free isometric \(\mathbb R^N\)-adapted metric with global orbit-volume function \(v=\sqrt{\det G}\),

\[
\Delta_Bv=\left(\frac14|F|^2-\lambda N\right)v.
\]

For \(\lambda<0\), this excludes such a model if the base is connected and parabolic and \(v\) is bounded above. A circle base is excluded by periodic integration without an extra boundedness assumption. Finite total volume gives only \(v\in L^1\), not \(v\in L^\infty\); completion by finitely many points does not by itself prove the ends are polar. The near-Einstein inequality with coefficient \(N(1-\delta)\) requires an exact isometric adapted action for the actual metric, not merely an approximate CFG structure.

### 6.2 Exact \(\mathrm{nil}^3\) cohomogeneity-one models

With

\[
[E_1,E_2]=\sqrt\rho E_3,
\]

the fiber scalar curvature is \(-\rho/2\), hence

\[
\boxed{v''=(3-\rho/2)v.}
\]

Equivalently, with \(\mu=\rho/2\), \(v''=(3-\mu)v\). The sign correction is definitive; the \(\mathbb{CH}^2\) cusp verifies it.

The trace subsystem gives, at an interior extremum of \(\rho\),

\[
\rho''=\rho(3\rho-2).
\]

On a circle, the global maximum satisfies \(\rho\le2/3\), and therefore

\[
v''\ge(8/3)v>0,
\]

contradicting periodicity. Thus exact \(\mathrm{nil}^3\) Einstein models over a circle do not exist.

On a finite interval, the same conclusion requires endpoint control. If

\[
\limsup_{s\to\partial I}\rho(s)<6,
\]

then \(v''\ge cv\) for some \(c>0\); if additionally \(v\to0\) at both finite-distance endpoints, positivity and convexity exclude the model. Without endpoint control, \(\rho\) may diverge and \(3-\rho/2\) may be negative. Merely assuming \(v\to0\) at both ends does not imply the needed bound on \(\rho\).

The standard \(\mathbb{CH}^2\) nil cusp has

\[
v(s)=C e^{4s/\sqrt6},\qquad s\in(-\infty,0],
\]

and finite volume but infinite base length. Its truncated segments \([-L,0]\) have uniformly bounded volume as \(L\to\infty\). Therefore finite total volume supplies no cusp-length bound.

## 7. Statements withdrawn from the working route

The following are not established and must not be used:

- total downstairs deficit directly implies small lifted deficit on a noncollapsed cover ball;
- the false inequality \(c\int\eta^2\le\int|\nabla\eta|^2\) controls regular-region volume or boundary cost;
- all regular bounded-curvature collapse is exhausted by the listed abelian and \(\mathrm{nil}^3\) exact models;
- interval \(\mathrm{nil}^3\) collapse is excluded without endpoint control of \(\rho\);
- finite volume bounds cusp length;
- Cheeger–Tian’s Einstein curvature decomposition applies from only \(\|\operatorname{Ric}+g\|_\infty\to0\);
- a fixed-topology negative pinching gap has already been proved.

## 8. Relation to the positive branch

S0910A02 identified a valid complementary result: in dimension four, a uniform lower total-volume bound plus tight positive two-sided Ricci pinching gives Myers diameter control, a uniform lower bound for every unit-ball volume by Bishop–Gromov, and hence finitely many diffeomorphism types by Cheeger–Naber Theorem 1.12. Therefore a sequence among pairwise distinct \(\#_k(S^2\times S^2)\) with positive pinching defect tending to zero must collapse in total volume. This reinforces the common structure of both signs: two-sided Ricci bounds control noncollapsed geometry strongly, while collapse and its fixed-scale local covers remain central.

It does not by itself prove the positive branch, and the asserted blow-up energy quantization/counting in the peer note requires separate support before use.

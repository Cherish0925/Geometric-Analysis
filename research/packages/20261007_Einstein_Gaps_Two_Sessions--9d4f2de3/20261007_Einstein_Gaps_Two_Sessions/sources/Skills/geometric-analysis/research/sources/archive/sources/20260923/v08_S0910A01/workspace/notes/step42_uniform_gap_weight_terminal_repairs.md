# Step 42: family-uniform gap, cutoff-weight comparison, and terminal regularity repair

Session: S0910A01. Agent3 / Actuator. Phase: Execute.

This note is a targeted repair to `step41_corrected_restricted_defect_gap_theorem.md`.  It does not replace the proof by a new broad theorem.  It corrects four load-bearing interfaces:

1. the intended result is a family-uniform negative pinching gap for the permitted Ishida--LeBrun geography, not a topology-dependent number \(\varepsilon_4(A,k)\);
2. the averaged Chern--Weil deficit uses \(I-J=2A/3-q\), hence \(D=J-q-(2/3)\sum(E_j^+)^2\), with no hidden extra \(A\)-term;
3. the weighted \(U_m\) continuation must match A03's actual weight \(\chi C_{m+2}U\), not the weaker term \(C_{m+2}U\); the extra \(\chi\) is supplied only if the exact weighted equation leaves the source as \(a\nabla^{m+2}a*T\);
4. the terminal compactness passage needs strong finite-\(W^{2,p}\) curvature convergence, not an unsupported \(W^{4,p}\) estimate from a \(C^0\)-small Einstein defect.

The main scientific status after this repair is: the zero-order unweighted \(T\) energy seed is valuable and should be retained; A03's Step 40/44 staggered derivative mechanism is plausible only after the exact weight-sensitive \(U") equation has been derived with the surviving top cutoff terms; transported DeTurck start/restart remains a separate analytic input.

---

## 1. Intended family-uniform theorem

Use the standard Ishida--LeBrun geography in the form needed by the argument:

\[
M=(\#_{j=1}^m X_j)\#N,\qquad m\in\{2,3\},
\]
where each \(X_j\) is a minimal complex surface of general type, \(N\) is closed oriented with \(b_+(N)=0\), and the connected sum carries the Ishida--LeBrun monopole family used in the mixed Seiberg--Witten inequality.  Set
\[
A=\sum_{j=1}^m c_1^2(X_j)>0,
\qquad
D=4m-(2\chi+3\tau)(N),
\qquad
q=D-{A\over3}.
\]
The above-critical no-Einstein range is \(q\ge0\), with the relevant monopole classes
\[
\kappa_\varepsilon=\sum_{j=1}^m c_1(X_j)+\sum_\ell \varepsilon_\ell E_\ell,
\qquad \varepsilon_\ell=\pm1,
\]
or the corresponding Ishida--LeBrun sign family for the chosen presentation.  The point is not the notation for the exceptional summands; it is that every class used in the sign average is a monopole class for every smooth metric on the same underlying smooth four-manifold.

The intended result of the negative-flow route is:

**Family-uniform negative gap, conditional on the analytic flow package.**  There is \(\varepsilon_{\rm IL}>0\), independent of \(A,D,q,N\) and of the chosen smooth metric, such that no manifold in the above Ishida--LeBrun no-Einstein range \(q\ge0\) carries a smooth metric with
\[
\|g^{-1}(\operatorname{Ric}_g+g)\|_{\infty,\mathrm{op}}<\varepsilon_{\rm IL}.
\]

The constant is uniform inside this four-dimensional geography.  It is not a dimension-only constant for all four-manifolds, and it does not address the positive branch or dimensions \(n\ge5\).

The topology-dependent statement in Step 41 is too weak for the purpose of the long analytic work: for a fixed topology with \(q>0\), the mixed Seiberg--Witten estimate already gives a positive number below which negative pinching is impossible.  The analytic route is valuable because it aims to stop sequences where \(q/A\to0\), including collapsing and unbounded-topology regimes.

---

## 2. Correct deficit algebra

For the geography above,
\[
(2\chi+3\tau)(M)=A-D={2A\over3}-q.
\]
With
\[
I={1\over4\pi^2}\int\left({s^2\over24}+2|W^+|^2\right)d\mu,
\qquad
J={1\over4\pi^2}\int{|\operatorname{Ric}^{\circ}|^2\over2}d\mu,
\]
Chern--Weil gives
\[
I-J=(2\chi+3\tau)(M)={2A\over3}-q. \tag{2.1}
\]
After sign-averaging the monopole inequalities,
\[
I\ge {2\over3}\left(A+\sum_\ell(E_\ell^+)^2\right).
\]
Define the averaged deficit
\[
D_{\rm av}:=I-{2A\over3}-{2\over3}\sum_\ell(E_\ell^+)^2\ge0. \tag{2.2}
\]
Using (2.1),
\[
\boxed{
D_{\rm av}=J-q-{2\over3}\sum_\ell(E_\ell^+)^2.
} \tag{2.3}
\]
There is no extra \(+2A/3\) or \(-2A/3\) term in (2.3).  In particular, when \(q\ge0\),
\[
0\le D_{\rm av}\le J,
\qquad
q+{2\over3}\sum_\ell(E_\ell^+)^2\le J. \tag{2.4}
\]
If \(\delta=\|g^{-1}(\operatorname{Ric}+g)\|_\infty\), then \(J\le C\delta^2\operatorname{Vol}\), and the calibrated volume identity gives \(\operatorname{Vol}/A\to32\pi^2/9\) along any \(\delta\to0\) sequence.  Hence
\[
{q\over A}\to0,
\qquad
{1\over A}\sum_\ell(E_\ell^+)^2\to0,
\qquad
{D_{\rm av}\over A}\to0. \tag{2.5}
\]

The earlier Step 41 line \(I-J=A-k=-q\) was only correct if the term \(2A/3\) had already been subtracted.  In the actual topology it is wrong; the final averaged deficit formula (2.3) is the one used below and at terminal time.

---

## 3. Bounded-\(A\) subsequences in the contradiction argument

To prove a family-uniform gap by contradiction, suppose \(\delta_i\to0\) on a sequence in the permitted geography.

1. The mixed inequality gives the pointwise lower bound previously derived in the session:
   \[
   {\delta_i\over1-\delta_i}\ge \sqrt{\frac{q_i/A_i}{2}}
   \]
   whenever \(q_i>0\).  Therefore \(q_i/A_i\to0\).

2. If \(A_i\to\infty\), the existing near-critical smoothing and terminal contradiction route applies after the analytic interfaces are closed.

3. If \(A_i\) is bounded, pass to a subsequence with \(A_i=A_0\).  Since \(A_i\) and \(D_i\) are integral and \(q_i=D_i-A_i/3\ge0\) lies in a discrete subset of \((1/3)\mathbb Z\), \(q_i/A_i\to0\) forces \(q_i=0\) eventually.  The same analytic contradiction does not require \(A_i\to\infty\): the terminal density is \(o(A_0)\), while the selected inner plateaux have volume \(\ge\alpha A_0>0\).  Thus the Liouville--Rauch averaging still produces a pullback ball with vanishing mean density.

Consequently the proof by contradiction should not assume \(A_i\to\infty\) as part of the theorem.  It may split into the two cases above after \(q_i/A_i\to0\) has been forced.

---

## 4. Weight-sensitive comparison with A03's staggered energy argument

Let
\[
a=\chi^2,
\qquad
T=\operatorname{Rm}+G,
\qquad
U=aT,
\qquad
E=\operatorname{Ric}(T),
\qquad
\partial_tg=-2\operatorname{Ric}(U).
\]
The unweighted shifted curvature equation has the schematic high-cutoff part
\[
(\partial_t-a\Delta)T=\cdots +(\nabla^2a)*T+\text{terms with at most one derivative of }a. \tag{4.1}
\]
This is the source of the Hessian-cutoff terms treated by signed integration by parts in the lower-order energy estimates.

Since \(a\) is a fixed scalar along the geometric flow,
\[
\partial_tU=a\partial_tT.
\]
Multiplying (4.1) by \(a\) gives the top Hessian source in the weighted equation:
\[
a(\nabla^2a)*T=(\nabla^2a)*U. \tag{4.2}
\]
After taking \(m\) spatial covariant derivatives, the highest cutoff derivative arising from (4.2) is
\[
\nabla^{m+2}a*U_0
=\left(2\chi C_{m+2}+\sum_{1\le r\le m+1} C_r*C_{m+2-r}\right)*U_0. \tag{4.3}
\]
Thus the top current-jet term in the \(U_m\) energy is
\[
\boxed{\chi C_{m+2}*U_0*P(U_m),}\tag{4.4}
\]
up to harmless universal constants.  In the original \(T\)-language this is
\[
2\chi C_{m+2}U=2\chi^3C_{m+2}T.
\]

This differs from Step 41 §4.12, which wrote \(\chi^2C_{m+2}T=C_{m+2}U\).  The missing factor \(\chi\) is not a cosmetic loss.  A03's energy estimate for \(V=U_m\) uses exactly
\[
\int \chi C_{m+2}*U*P(V). \tag{4.5}
\]
Integrating once off \(C_{m+2}=\nabla C_{m+1}\) produces
\[
-\int \chi C_{m+1}*U*\nabla P(V)+\cdots . \tag{4.6}
\]
The factor \(\chi\) in (4.6) pairs with the weighted dissipation
\[
D^U_{m,p}=\int\chi^2|\nabla V|^2|V|^{p-2}
\]
by Cauchy--Schwarz:
\[
\left|\int \chi C_{m+1}U|V|^{p-2}\nabla V\right|
\le \varepsilon D^U_{m,p}
+C_{\varepsilon,p}K^2\int |C_{m+1}|^2|V|^{p-2}. \tag{4.7}
\]
Without this \(\chi\), one would have to control \(\int |\nabla V|^2|V|^{p-2}\) without the \(\chi^2\) weight, or divide by \(\chi\) near the transition region.  Neither is available.

The product-rule comparison therefore supports A03's starting term if and only if the full weighted \(U") equation really leaves every top \(C_{m+2}\) contribution in the form (4.2), or in an even better form with an additional \(\chi\).  Derivative order alone is insufficient.  The unresolved source-level task is to derive the complete normalized weighted \(U_m\) equation from the all-lower Riemann variation and verify that no commutator, normalization, or \(G\)-variation term produces a bare \(C_{m+2}U\) term.

What is retained now:

- the zero-order unweighted \(T\) seed from Step 41/A03 Step 44;
- the unweighted \(T_m\) estimate, where the true top source is \(\chi C_{m+2}T\) and the signed integration by parts is different from the weighted \(U_m\) absorption;
- A03's extra integration by parts for the residual \(\chi C_{m+1}U_1P(U_m)\), provided the preceding top term is indeed (4.4).

What is not yet established as a self-contained theorem:

- the exact all-order weighted \(U_m\) tensor equation with the weight placement in (4.4) verified for every surviving top cutoff term;
- the transported DeTurck start/restart theorem at the source level.

---

## 5. Terminal compactness with only strong finite-\(W^{2,p}\) convergence

The terminal pullback does not need \(W^{4,p}\) bounds.  The previous Step 41 sentence deriving \(W^{4,p}\) from the harmonic-coordinate Ricci equation and a \(C^0\)-small Einstein defect was unsupported, because differentiating Ricci would require derivative control on the defect.

Use the following weaker passage.

On the selected exponential pullback balls, the terminal Moser endpoint gives a uniform bound for \(|\operatorname{Rm}|\) on the plateau, and Rauch comparison gives a uniform lower volume ratio on the tangent-domain balls.  Harmonic-radius theory then gives coordinates on a smaller ball in which
\[
\|g_i\|_{C^{1,\alpha}}+\|g_i\|_{W^{2,p}}\le C(p)
\]
for every finite \(p\), after passing to a subsequence.  In harmonic coordinates,
\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=-2(\operatorname{Ric}_{g_i})_{jk}+Q_{jk}(g_i^{-1},\partial g_i). \tag{5.1}
\]
On the plateau,
\[
\operatorname{Ric}_{g_i}=-g_i+E_i,
\qquad
\|E_i\|_{L^p}\to0
\]
for every finite \(p\), using the terminal defect endpoint (or the selected vanishing density together with the available uniform bound).  The coefficients and the quadratic first-derivative term converge strongly after the harmonic-coordinate subsequence.  Elliptic stability in (5.1) gives
\[
g_i\to g_\infty\quad\text{strongly in }W^{2,p}_{\rm loc}\quad(p<\infty). \tag{5.2}
\]
Hence the curvature tensors converge strongly in \(L^p_{\rm loc}\).  The nonnegative terminal density has vanishing pulled-back mean, so the limit satisfies almost everywhere
\[
E_\infty=0,
\qquad
s_\infty=-4,
\qquad
s_\infty+8\sqrt6|W^+_\infty|=0,
\qquad
G_\infty=0.
\]
Because \(g_\infty\in W^{2,p}\) solves \(\operatorname{Ric}_{g_\infty}=-g_\infty\) weakly in harmonic coordinates, elliptic bootstrapping makes \(g_\infty\) smooth.  The curvature equalities then hold everywhere, and Derdziński's local theorem applies.

This route avoids using per-datum continuation derivative bounds as sequence-uniform estimates.  A stronger alternative would be to prove sequence-uniform positive-time plateau derivative estimates by converting the \(\chi=1\) region to ordinary Ricci flow and applying local Shi estimates; that must be a separate positive-time estimate, not an inference from per-datum continuation.

---

## 6. Current unresolved analytic inputs after this repair

The restricted negative-flow program should now carry two precise analytic inputs rather than saying only H-DT remains:

\[
\text{H-WU: exact weighted }U_m\text{ all-order equation with the }\chi C_{m+2}U\text{ top weight.}
\]

\[
\text{H-DT: transported-coefficient DeTurck start/restart with tame estimates and uniqueness.}
\]

A03 Step 44 gives stronger evidence for H-DT by writing the normalized Yang linearization and the coupled energy estimate.  This is promising, but it should still be independently read against Yang's source because the source states the tame estimates tersely.  H-WU is independent of H-DT and must be completed by direct tensor derivation.

Once H-WU and H-DT are established, the family-uniform contradiction described in §§1--3, with the terminal passage in §5, would give a real uniform negative pinching gap for the above Ishida--LeBrun no-Einstein geography.  That would remain a restricted four-dimensional result, not a resolution of the full Yau 26 proposition.

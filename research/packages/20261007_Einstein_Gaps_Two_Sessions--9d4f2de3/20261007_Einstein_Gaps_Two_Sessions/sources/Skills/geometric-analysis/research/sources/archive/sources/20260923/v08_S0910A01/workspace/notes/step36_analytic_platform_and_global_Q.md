> **Step 38 correction:** Step 37 did **not** close the continuation theorem or
> first-exit platform.  The DeTurck formulation (§1) and global Q persistence
> (§3) remain useful conditional inputs, while continuation must follow the
> repaired weighted-\(U\)/unweighted-\(T\) route in
> `step38_continuation_repair_and_support_normalization.md` and A03 Step 40.


Session: S0910A01. Agent3 / Actuator. Phase: Execute.

## 0. Purpose and current mathematical role

The fixed-exponent estimates from Steps 34--35 are useful only if they sit on a
real smooth local-flow platform.  Step 35 proved the Hessian-cutoff contraction
bounds needed for the first smoothing estimates, so those estimates do not need
pointwise control of the evolving Hessian of the cutoff.  This separates the
first smoothing layer from the higher-derivative continuation problem.

The target flow on a closed smooth four-manifold is
\[
  \partial_t g=-2aE,
  \qquad a=\chi^2,
  \qquad E=\operatorname{Ric}_g+g .
\tag{0.1}
\]
Here \(\chi\) is fixed as a smooth function on the manifold.  The analytic
platform has three logically different parts.

1. **Per-datum short-time existence.**  For each smooth input \((g_0,\chi)\)
   one needs a smooth solution on some interval \([0,T_0(g_0,\chi))\).  The time
   may depend on all geometry of the single input, including the exterior where
   the selected support does not control curvature.

2. **Extension to the selected time \(T=\theta r^2\).**  Once the sequence-uniform
   zero-order estimates are available, finite maximal time below \(T\) must be
   excluded.  The higher-derivative bounds used for extension may depend on the
   individual input and on a positive starting time; they only need to stay finite
   as \(t\uparrow T_{\max}\).

3. **Sequence-uniform quantities used downstream.**  Metric drift, terminal
   plateau curvature, retained plateau volume, moving Sobolev comparison, and
   the global unweighted defect
   \[
     Q(t)=\int_M |E(t)|^2\,d\mu_t
   \]
   must be controlled uniformly along a near-critical sequence.  The weighted
   seed \(J_6\) and \(\|aE\|_\infty\) do not replace \(Q\).

This note records the corrected equations and proves the separate \(Q\) energy
propagation under the same support hypotheses used by the fixed-exponent module.
It also isolates exactly what remains to be written for the transported DeTurck
existence and shifted-\(U\) extension arguments.

---

## 1. Correct transported-coefficient DeTurck formulation

Yang's local Ricci-flow source (Knowledge object
`Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md`,
lines 787--823) proves short-time existence for
\(\partial_t g=-2\chi^2\operatorname{Ric}_g\) by solving for a hatted metric and
moving diffeomorphism.  The important point is that the coefficient is transported:
\[
  \widehat a(t)=a\circ\varphi_t^{-1}.
\tag{1.1}
\]
For the normalized equation (0.1), the corresponding hatted system should be
\[
  \partial_t\widehat g
  =-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
    +\mathcal L_{\widehat a W(\widehat g,S)}\widehat g,
\tag{1.2}
\]
with
\[
  \partial_t\varphi_t\circ\varphi_t^{-1}=-\widehat a W(\widehat g,S),
  \qquad \varphi_0=\operatorname{Id}.
\tag{1.3}
\]
Here \(S\) is Yang's fixed background symmetric tensor and \(W\) is the DeTurck
vector field encoded in lines 795--807 of the source.  The gauge term must be
\(\mathcal L_{\widehat aW}\widehat g\), not merely
\(\widehat a\mathcal L_W\widehat g\), because
\[
  \mathcal L_{\widehat aW}\widehat g
  =\widehat a\mathcal L_W\widehat g
   +d\widehat a\otimes W^\flat+W^\flat\otimes d\widehat a .
\tag{1.4}
\]
Those first-derivative coefficient terms are exactly part of the DeTurck
cancellation.

Pulling back by \(g=\varphi_t^*\widehat g\) gives
\[
\begin{aligned}
  {d\over dt}\varphi_t^*\widehat g
  &=\varphi_t^*(\partial_t\widehat g
      +\mathcal L_{\partial_t\varphi_t\circ\varphi_t^{-1}}\widehat g)  \\
  &=\varphi_t^*(-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g))
    =-2a(\operatorname{Ric}_g+g).
\end{aligned}
\tag{1.5}
\]
This verifies that (1.2)--(1.3) is the correct fixed-cutoff normalized DeTurck
system.

### 1.1 Linearized structure

Yang records the schematic linearized pair (source lines 811--813)
\[
\begin{aligned}
  \partial_t h &=2\chi^2\Delta h+
    \chi(B\nabla h+C\nabla\psi)+Dh+E_0\psi, \\
  \partial_t\psi&=-\chi^2(P\nabla\psi+Q\nabla h+Rh).
\end{aligned}
\tag{1.6}
\]
Relative to Yang's unnormalized transported Ricci term, the genuinely new
normalization contribution is only the variation of \(-2\widehat a\widehat g\):
\[
  \delta(-2\widehat a\widehat g)
  =-2\widehat a\,h-2(\delta\widehat a)\widehat g .
\tag{1.7}
\]
The term \(-2(\delta\widehat a)\operatorname{Ric}_{\widehat g}\) belongs to the
coefficient variation already present in Yang's unnormalized Ricci part; it is
not a new normalization term.  The variation \(\delta\widehat a\) is obtained
from the diffeomorphism variation, so it is a lower-order coefficient times the
variation of the map (schematically \(-d\widehat a(\psi)\)); it does not add
second derivatives of \(h\).  Thus the principal and first-order triangular
structure in Yang's linearized system is unchanged.  To turn this into a fully
self-contained proof one must reproduce Yang's tame energy estimates for the
transported system with the extra lower-order terms (1.7).  The present note does
not replace those estimates with ordinary strictly parabolic Schauder theory.

### 1.2 What regularization may and may not do

For fixed smooth data, replacing \(a\) by \(a+\varepsilon^2\) is not forbidden
just because the exterior temporarily evolves.  The needed statement is instead:
there is \(T_0(g_0,\chi)>0\), independent of \(\varepsilon\), and enough
\(\varepsilon\)-uniform estimates to pass to a smooth limit solving (0.1).
Yang's source line 816 regularizes the *linearized* equation by adding
\(\varepsilon^2\Delta h\), and lines 821--823 mention coefficient regularization
for the unnormalized equation, with convergence supplied by energy estimates.
Ordinary Schauder constants for a strictly parabolic problem depend on the lower
ellipticity bound and therefore do not by themselves give the required
\(\varepsilon\)-uniform smooth limit.  A valid proof must use Yang-type degenerate
energy/tame estimates or another argument with equivalent uniform content.

The quantifier distinction is important: this per-datum existence time does not
need to be uniform over the collapsing near-critical family.  Sequence-uniform
estimates enter only after a smooth solution is available.

---

## 2. Maximal-time extension interface

Let \([0,T_{\max})\) be the maximal smooth solution interval for (0.1) starting
from one fixed smooth input.  Suppose the first-exit estimates hold up to every
\(T<T_{\max}\) and give, for \(t>0\),
\[
  \|aF(t)\|_\infty\le {C\gamma\over t},
  \qquad
  \sup_{T<T_{\max}}\int_0^T\|aE(s)\|_\infty\,ds<\infty.
\tag{2.1}
\]
The uniform-in-terminal-time integral is the quantity needed for bilipschitz
comparison as \(t\uparrow T_{\max}\); mere finiteness on each proper subinterval
would be automatic for a smooth solution and would not exclude terminal loss of
metric comparison.
Set
\[
  G={g\owedge g\over 2(n-1)},
  \qquad T=\operatorname{Rm}+G,
  \qquad U=aT.
\tag{2.2}
\]
Then \(\operatorname{Ric}(T)=E\), \(\operatorname{Ric}(U)=aE\), and
\[
  \partial_t g=-2\operatorname{Ric}(U).
\tag{2.3}
\]
This identity is the reason continuation should be written in terms of \(U\):
\[
  \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
\tag{2.4}
\]
which packages the problematic split terms \(da*E+a\nabla E\) into the derivative
of the contracted shifted curvature.

If \(T_{\max}<\theta r^2\), choose \(\tau=T_{\max}/2\).  The estimate (2.1)
provides a finite bound on \(|U|\) on \([\tau,T_{\max})\); the metric drift in
(2.1) gives finite bilipschitz comparison on the same interval.  The higher
spatial derivative constants used for extension may depend on \(g(\tau)\),
\(\chi\), \(\tau\), and \(T_{\max}\).  They do not need to be uniform in the
near-critical sequence.

A Wang-type extension theorem for the normalized shifted variable should have the
following form.

**Shifted extension statement to prove.**  If a smooth solution of (0.1) on
\([0,T_{\max})\), \(T_{\max}<\infty\), satisfies finite bilipschitz metric
comparison and
\[
  \sup_{M\times[\tau,T_{\max})}|U|<\infty
\tag{2.5}
\]
for every \(\tau>0\), then all spatial derivatives needed to pass
\(g(t)\) smoothly to \(T_{\max}\) remain finite on \([\tau,T_{\max})\), and the
solution extends beyond \(T_{\max}\) by the per-datum short-time existence theorem.

The remaining proof is not a pointwise cutoff-Hessian estimate.  It should follow
Wang's induction pattern (source `Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`, lines 396--412 and 426--461),
but with \(U=a(\operatorname{Rm}+G)\).  At the lowest level one must estimate the
pair
\[
  (\nabla U,\nabla^2\chi).
\tag{2.6}
\]
The cutoff equation follows from (2.4):
\[
  \partial_t\nabla^2\chi
  =-(\partial_t\Gamma)*\nabla\chi
  =g^{-1}*\nabla\operatorname{Ric}(U)*\nabla\chi.
\tag{2.7}
\]
The differentiated \(U\)-equation contains terms of the schematic form
\[
  \chi\nabla^3\chi*U,
  \quad \nabla\chi*\nabla^2\chi*U,
  \quad \chi\nabla^2\chi*\nabla U,
  \quad \chi\nabla\chi*\nabla^2U,
\tag{2.8}
\]
plus lower-order terms involving \(U\), \(G\), and previously controlled
unweighted \(L^p\) norms of \(T\).  The first term in (2.8) must be handled as a
signed group with the fourth term: integrate by parts to move the derivative off
\(\nabla^3\chi\), and use the remaining factor \(\chi\) to absorb the
\(\nabla^2U\) contribution in the weighted dissipation.  This is the concrete
base-pair problem still to be written.  Declaring \(\|T\|_\infty\) or
\(\|a\nabla\operatorname{Rm}\|_\infty\) finite because the solution is smooth on
proper subintervals does not exclude blow-up at \(T_{\max}\).

---

## 3. Separate global Q propagation

The terminal calibration and exponential-pullback selection use the unweighted
defect energy
\[
  Q(t)=\int_M |E(t)|^2\,d\mu_t.
\tag{3.1}
\]
This is not implied by the weighted seed
\(J_6=\int \eta^2a^4|E|^6\) or by \(\|aE\|_\infty\).  The global \(Q\) estimate is
therefore carried as its own part of the first-exit argument.

On one support with a buffer cutoff, set
\[
  Q_U(t)=\int_U |E|^2\,d\mu_t,
  \qquad
  X_U(t)=\int_U a|\nabla E|^2\,d\mu_t.
\tag{3.2}
\]
The homogeneous defect variation, using the Step 35 Hessian-cutoff tensor
\(B_{\rm def}=|E|^2g+(\operatorname{tr}E)E-2E^2\), gives
\[
  Q_U' + cX_U
  \le C\int_U\left({|da|^2\over a}+a\right)|E|^2
       +C\int_U aF|E|^2 .
\tag{3.3}
\]
Here \(|da|^2/a=4|d\chi|^2\le Cr^{-2}\), and all Hessian-\(a\) terms are paid by
signed integration by parts as in Step 35, not by a pointwise evolving-Hessian
bound.  Therefore
\[
  Q_U'+cX_U
  \le C(1+r^{-2})Q_U+C\int_U F(\chi E)^2.
\tag{3.4}
\]
Using the support Sobolev inequality and the same buffered localized curvature
energy
\[
  K_2^\eta=\int_U\eta^2F^2,
  \qquad \eta\equiv1\text{ on }\operatorname{supp}\chi,
\]
so that \(K_2^\eta\) controls \(\|F\|_{L^2(\operatorname{supp}\chi)}^2\),
\[
\begin{aligned}
  \int_U F(\chi E)^2
  &=\int_{\operatorname{supp}\chi}F(\chi E)^2 \\
  &\le \|F\|_{L^2(\operatorname{supp}\chi)}\,\|\chi E\|_{L^4(U)}^2     \\
  &\le C\mathcal S K_2^\eta{}^{1/2}
        \left(\int_U |\nabla(\chi E)|^2+r^{-2}\int_U\chi^2|E|^2\right) \\
  &\le C\gamma\left(X_U+r^{-2}Q_U\right),
\end{aligned}
\tag{3.5}
\]
where \(\gamma=\mathcal S(K_2^\eta)^{1/2}\).  If \(C\gamma\le c/2\), the gradient
term is absorbed and
\[
  Q_U'(t)\le C(1+r^{-2})Q_U(t).
\tag{3.6}
\]
The shorter \(Cr^{-2}\) form is available only after fixing a scale
normalization such as \(r\le1\).  This distinction is harmless for the intended
fixed-radius application but should not be hidden.

For macro-disjoint active supports the same calculation is summed over supports.
On the frozen complement \(a=0\), the metric and \(E=\operatorname{Ric}+g\) are
stationary.  Thus the global quantity satisfies
\[
  Q(t)\le e^{C(1+r^{-2})t}Q(0)
  \le e^{C\theta(1+r^2)}Q(0),
  \qquad 0\le t\le \theta r^2.
\tag{3.7}
\]
Consequently, in the near-critical sequence where \(Q(0)/A\to0\), the terminal
input needed for Step 28 recalibration remains
\[
  {Q(\theta r^2)\over A}\to0.
\tag{3.8}
\]
This is the missing bridge between the local smoothing estimates and the
terminal Chern--Weil/monopole calibration; it is independent of \(J_6\), whose
role is to seed the positive-time defect Moser bound.

---

## 4. First-exit assembly with separated roles

On a selected macro-support, the first-exit interval should carry these
sequence-uniform quantities:
\[
\begin{array}{ll}
  \text{curvature energy:} & K_2^\eta(t)\le 2K_2^\eta(0),\\[2mm]
  \text{Sobolev:} & \mathcal S(t)\le2\mathcal S(0),\\[2mm]
  \text{metric drift:} & \displaystyle\int_0^t\|aE(s)\|_\infty ds\le \alpha_0,\\[3mm]
  \text{defect seed:} & J_6(t)\le C\delta^6V,\\[2mm]
  \text{global defect:} & Q(t)
       \le e^{C(1+r^{-2})t}Q(0),\\[2mm]
  \text{flow platform:} & \text{smooth existence and extension on the interval.}
\end{array}
\tag{4.1}
\]
The dependency structure is now non-circular:
\[
  K_2^\eta\Rightarrow
  \begin{cases}
    \int_0^tY\le C\gamma K_2^\eta(0),\quad
    Y(t)\le C\gamma K_2^\eta(0)/t,\\
    J_6(t)\le C\delta^6V,\\
      Q(t)\le e^{C(1+r^{-2})t}Q(0),
  \end{cases}
\tag{4.2}
\]
then the nested Moser estimates give
\[
  \|aF(t)\|_\infty\le C\gamma/t,
  \qquad
  \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}.
\tag{4.3}
\]
The latter yields
\[
  \int_0^{\theta r^2}\|aE(t)\|_\infty dt
  \le {3\over2}C\delta r^2\theta^{2/3},
\tag{4.4}
\]
which controls metric comparison and moving Sobolev/support geometry for
\(\delta\) sufficiently small.

The first-exit argument still has two analytic interfaces that are not proved by
(4.1)--(4.4): per-datum short-time existence and shifted-\(U\) extension at a
finite maximal time.  Establishing both would let the sequence-uniform bootstrap
run up to \(T=\theta r^2\).  Without extension, self-improvement of the energy
bounds alone does not prevent the smooth solution from terminating.

---

## 5. Downstream implication if the platform is completed

If the transported DeTurck existence theorem and shifted-\(U\) extension theorem
are proved, then the restricted negative-route chain becomes:

1. Start with a near-critical Ishida--LeBrun sequence with
   \(\delta_i\to0\), \(Q_i(0)/A_i\to0\), and selected supports with
   \(\gamma\le\gamma_0\).
2. Run (0.1) to \(T=\theta r^2\) on macro-disjoint supports.
3. Preserve \(Q_i(T)/A_i\to0\) by (3.7), and retain small metric drift by (4.4).
4. Use \(\|aF(T)\|_\infty\le C/ T\) to obtain bounded curvature on the terminal
   plateaux.
5. Reapply Step 28 terminal calibration to get terminal combined defect integral
   \(o(A_i)\).
6. Use exponential-pullback averaging on the \(A_i\)-proportional plateau center
   set to select a noncollapsed tangent ball with vanishing calibrated defects.
7. Pass to a smooth Einstein germ with the calibrated self-dual Weyl spectrum and
   contradict the Derdzinski local conformally-Kahler modulus mechanism.

This would prove only a restricted theorem for the near-critical four-dimensional
negative Ishida--LeBrun laboratory.  It would not decide the full Yau Problem 26,
which still requires the positive branch or a broader negative branch, arbitrary
four-manifold topology, dimensions \(n\ge5\), dimension-only constants, and Lean
formalization.

---

## 6. Evidence and companion files

- Tensor identities: `workspace/notes/step35_tensor_variation_and_hessian_a.md`.
- Fixed-exponent module: `workspace/notes/step34_integrated_potential_q3_and_defect.md`.
- A03 interface review: `Sessions/S0910A03/workspace/notes/step36_preceptor_interface_review.md`.
- Yang source lines 787--823 and 835--878 in
  `Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md`.
- Wang/Yang extension source lines 396--412 and 426--461 in
  `Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`.
- Algebra/dependency verifier for this step:
  `workspace/scripts/step36_platform_Q_verify.py`.

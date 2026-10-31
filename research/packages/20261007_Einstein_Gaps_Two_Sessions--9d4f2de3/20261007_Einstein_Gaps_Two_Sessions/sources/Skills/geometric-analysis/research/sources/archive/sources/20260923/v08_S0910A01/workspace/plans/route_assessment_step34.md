# Route assessment after Step 34

**Step 35 superseding notice.**  The tensor-level obligations (items 1–2 from §7)
are resolved by `workspace/notes/step35_tensor_variation_and_hessian_a.md`.
Use `workspace/plans/route_assessment_step35.md` for the current status.

## Main advance

Step 34 repaired the fixed-exponent analytic layer for the selected-support
normalized cutoff flow
\[
\partial_tg=-2a(\operatorname{Ric}+g),\qquad a=\chi^2,
\]
in the restricted four-dimensional negative Ishida--LeBrun route.  The key
scientific change is that fixed-exponent propagation can be separated cleanly from
the later high-p Moser and continuation problems.

## Corrected fixed-exponent curvature seed

Use the squared Sobolev convention
\[
\|u\|_4^2\le \mathcal S(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2),
\qquad \mathcal S\simeq r^2/\sqrt V.
\]
The p=2 quantity must be localized:
\[
K_2^\eta=\int \eta^2F^2,
\qquad D_2^\eta=\int \eta^2a|\nabla\operatorname{Rm}|^2,
\]
not the formal p=2 version of \(K_p=\int a^{p-2}F^p\).  The absorption parameter is
\[
\gamma=\mathcal S(0)(K_2^\eta(0))^{1/2}\le Cr^2\sqrt{K_0}
\]
at a good selected support, so collapse-volume dependence cancels.

From the q=2 energy inequality and the p=2 interpolation,
\[
Y=\int\eta^2aF^3\le C\gamma(D_2^\eta+r^{-2}K_2^\eta),
\]
one obtains
\[
\int_0^tY(s)ds\le C\gamma K_2^\eta(0),
\qquad
B(t):=\int_0^t\mathcal S(s)^2Y(s)ds\le C\gamma^3
\]
in the provisional first-exit interval.  This integrated-potential bound is
independent of the pointwise q=3 estimate.  If the fixed-p curvature inequality
at p=3 gives
\[
Y'\le C(r^{-2}+1+\mathcal S^2Y)Y,
\]
a good slice \(\tau\in[t/4,t/2]\) followed by Gronwall from \(\tau\) to \(t\) gives
\[
Y(t)\le C\gamma K_2^\eta(0)/t,
\qquad \mathcal S(t)^2Y(t)\le C\gamma^3/t.
\]
The appearance of \(Y\) in its own coefficient is not circular because
\(\int\mathcal S^2Y\) is already controlled by q=2.

## Corrected tensor starting point

The all-lower curvature convention was fixed by the pure scaling test: under
\(\partial_tg=-2g\), \(\partial_t|\operatorname{Rm}|^2=4|\operatorname{Rm}|^2\), and
in dimension four \(\int|\operatorname{Rm}|^2d\mu\) is invariant.  Hence the
normalization/conformal part is not pointwise damping.

The moving-volume term is controlled by
\[
|s+4|=|\operatorname{tr}E|\le CF,
\]
so it enters the curvature reaction
\(\int a^{p-1}F^{p+1}\), not a premature \(C\delta K_p\) estimate.

The pre-absorption diffusion/tensor dissipation is
\[
-pD_p^{\rm Rm}-p(p-2)D_p^F,
\]
not the Step 33 intermediate \(-pD_p^{\rm Rm}-p(p-3)D_p^F\).  The Step 33 note now
has a superseding correction notice.

For the Hessian-a terms, the useful first smoothing route is signed tensor IBP:
\[
p\int a^{p-2}F^{p-2}(\nabla_i\nabla_ja)B^{ij}.
\]
This requires the derivative structure
\(|\nabla B|\lesssim F|\nabla\operatorname{Rm}|\), not just \(|B|\lesssim F^2\).
Pointwise evolving cutoff-Hessian control is retained only as a later continuation
input, not as an initial smoothing premise.

## Defect persistence simplified by A03 Step 35

A03 Step 35 was read and its script was rerun from A03; all 28 checks passed.  The
stronger defect estimate uses
\[
s=|E|^2,
\qquad J_6=\int\eta^2a^4s^3,
\qquad X_6=\int\eta^2a^5s^2|\nabla E|^2,
\qquad w_6=\eta\chi^5|E|^3.
\]
Because \(s^3=|E|^6\) and \(w_6\) are smooth enough at \(E=0\), no norm
regularization is needed.  The defect reaction is linear in \(F\):
\[
P_6=\int\eta^2a^5Fs^3=\int Fw_6^2.
\]
Two-factor Hölder and Sobolev give
\[
P_6\le \|F\|_2\|w_6\|_4^2
\le C\gamma(X_6+r^{-2}J_6),
\]
using only \(K_2^\eta\), not \(Y\).  Absorbing for small \(\gamma\) yields
\[
J_6'+cX_6\le C(1+r^{-2})J_6,
\qquad
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
\]
For \(T=\theta r^2\), this gives \(J_6(T)\le C\delta^6V\) from initial pinching.
This supersedes A01 Step 33's regularized three-factor route for J6 persistence.
The integrated-potential mechanism remains needed for q=3 curvature propagation
and the high-p curvature Moser coefficient.

## Evidence produced and checked

- New note: `workspace/notes/step34_integrated_potential_q3_and_defect.md`.
- New verifier: `workspace/scripts/step34_integrated_potential_q3_verify.py`.
  It was run successfully and reports 48 algebra/scaling checks passed.
- TTCS verification of the first version:
  `trace/ttcs/results/step34_ttcs01_verifier1_integration.md`.  Its corrections
  (localized \(K_2^\eta\), Hessian derivative-structure assumptions) are incorporated.
- A03 source read:
  `Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md`.
- A03 verifier rerun from A03:
  `Sessions/S0910A03/workspace/scripts/verify_step35_defect_algebra.py`, reporting
  all 28 checks passed.
- Step 33 power note patched with a superseding notice.

## What remains hard

This step does not prove the smoothing theorem.  The next mathematical work should
attack the index-level tensor premises and first-exit closure:

1. derive the all-lower curvature variation with every normalization coefficient
   consistent with the pure scaling test;
2. prove the signed Hessian-a derivative-structure bound
   \(|\nabla B|\lesssim F|\nabla\operatorname{Rm}|\) for the actual curvature
   contractions;
3. derive the defect evolution from Ricci variation and contracted Bianchi,
   including the quadratic Hessian-a contraction in A03 Step 35;
4. close the simultaneous first-exit interval carrying
   \(\mathcal S(t), K_2^\eta(t), J_6(t)\), metric/support comparability, and the
   weighted high-p Moser recurrence;
5. build degenerate-flow existence/continuation with coupled cutoff jets and then
   terminal plateau selection.

Even if these are completed, the result would still cover only the near-critical
Ishida--LeBrun negative four-dimensional laboratory.  The full Yau Problem 26
still requires the positive branch, arbitrary four-manifold topology, dimensions
\(n\ge5\), dimension-only constants, and Lean formalization.

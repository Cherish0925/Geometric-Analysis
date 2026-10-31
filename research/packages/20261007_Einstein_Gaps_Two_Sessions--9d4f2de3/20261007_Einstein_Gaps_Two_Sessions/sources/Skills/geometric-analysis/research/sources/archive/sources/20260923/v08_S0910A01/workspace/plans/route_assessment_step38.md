> **Superseded by `route_assessment_step39.md`**: Step 39 assembled the complete
> conditional defect gap theorem in one document.  This file retains the Step 38
> repair details and support normalization.

# Route assessment after Step 38

## Main correction

Step 37's claim that the shifted continuation theorem and first-exit platform were
closed is withdrawn.  The failure is structural, not editorial.  For
\[
U=aT=a(\operatorname{Rm}+G),\qquad a=\chi^2,
\]
\(|U|\le K\) implies \(|aE|=|\operatorname{Ric}(U)|\le CK\), not an additional
\(\chi^2K\) bound.  Hence the Step 37 split
\(\{\chi\ge\delta\}\cup\{\chi<\delta\}\) cannot control unweighted curvature
derivatives in the degenerate transition region.  Small \(C^0\) metric drift would
not imply curvature-derivative control, and fixed coordinate derivatives of the
scalar cutoff do not control evolving covariant cutoff jets.

Patched records:

- `workspace/notes/step37_continuation_theorem_and_first_exit.md` now starts with a
  superseding correction.
- `workspace/plans/route_assessment_step37.md` now starts with a superseding
  correction.
- `workspace/scripts/step37_continuation_verify.py` has been overwritten to exit
  nonzero and point to the Step 38 verifier.
- A peer correction was sent as session-group message #349.

## Repaired continuation direction

The current repair note is
`workspace/notes/step38_continuation_repair_and_support_normalization.md`, with
verifier `workspace/scripts/step38_continuation_support_verify.py` (94/94
algebra/exponent/normalization checks pass after incorporating A03 Step 40 and the unnormalized-energy caveat).  The
verifier is intentionally not a PDE proof.

The corrected continuation architecture follows Wang's real order:

1. Evolve the weighted shifted tensor
   \[
   U=a(\operatorname{Rm}+G),\qquad \operatorname{Ric}(U)=aE,
   \]
   so top cutoff terms follow Wang Lemma 4.5 and contain derivatives of \(U\), not
   unweighted derivatives of \(\operatorname{Rm}\).
2. Evolve cutoff jets using
   \[
   \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
   \]
   giving a coupled system for \(\nabla^mU\) and \(\nabla^{m+1}\chi\).
3. Prove a separate Wang Proposition 4.13-style unweighted curvature module for
   \(T=\operatorname{Rm}+G\), without dividing by \(a\).
4. Recover the smooth terminal metric using
   \[
   \partial_tg=-2\operatorname{Ric}(U),\qquad
   \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
   \]
   not by recovering \(\operatorname{Rm}\) from \(U/a\) in the transition region.

TTCS verification of the Step 38 repair (`trace/ttcs/results/step38_ttcs01_verifier1_integration.md`) accepted the correction and support normalization, but emphasized that the continuation theorem is still open.  Its specific objections were: derive the full shifted \(U\) equation including \(G\) and normalization terms; prove the shifted Lemma 4.10 and Proposition 4.13 estimates rather than calling them plausible; fix the \(m=2\) \(\Gamma_3\) product; ensure time-uniform bounds on \([\tau,T)\), not pointwise finiteness; and formulate terminal recovery in a fixed background connection.

## A03 Step 40 input incorporated

A03 Step 40 supplied a genuine advance for the first nontrivial continuation
level.  It withdrew A03's own Step 39 all-order continuation claim and proved the
\(m=2\) coupled residual mechanism for
\[
V=\nabla^2U,
\quad Z=\nabla^3\chi,
\quad W=\nabla U,
\quad \Theta=\nabla^2\chi.
\]
The invalid direct estimate
\[
\left|\int \chi ZW|V|^{p-2}V\right|
\le \|Z\|_{2p}\|W\|_{2p}\|V\|_p^{p-1}
\]
requires the current unknown \(Z\) at exponent \(2p\).  The repaired estimate
writes \(Z=\nabla\Theta\) and integrates once more.  The descendants are:

- \(d\chi*\Theta*W*P(V)\), controlled by finite base-pair norms;
- \(\chi\Theta*V*P(V)\), controlled by the signed Hessian lemma;
- \(\chi\Theta*W*\nabla P(V)\), controlled by weighted dissipation plus
  \(\int \Theta^2W^2|V|^{p-2}\), with Hölder using \(W,\Theta\in L^{4p}\) and a
  finite-volume slot.

This avoids both current \(Z\in L^{2p}\) and \(W\in L^\infty\).  A03 also gave the
order-one unweighted \(\nabla T\) lemma: expand
\[
\nabla^2a=2\chi\nabla^2\chi+2d\chi\otimes d\chi,
\qquad
\nabla^3a=2\chi\nabla^3\chi+C d\chi*\nabla^2\chi,
\]
and integrate only the \(\chi\nabla^3\chi\) term.  This yields
\[
{d\over dt}\|\nabla T\|_p^p+cD_p^T\le C_p(1+\|\nabla T\|_p^p)
\]
from \(|U|\), \(T\), \(\nabla U\), and \(\nabla^2\chi\) finite at the needed
exponents.  A01 ran A03's `verify_step40_m2_exponents.py` successfully (44/44).

The arbitrary-order continuation theorem is still not proved.  The next analytic
work should generalize the A03 Step 40 extra integration to every high-cutoff /
lower-derivative product and prove the higher unweighted \(\nabla^mT\) modules
with explicit finite Hölder schedules.

## Correct support-selection normalization

The support front is separate and remains productive.  The corrected construction
uses the volume-average maximal function
\[
\mathcal M_Rf(x)=\sup_{0<s\le R}\fint_{B_s(x)}f,
\qquad K_0=\fint_M|\operatorname{Rm}|^2.
\]
Choose a large threshold \(\Lambda K_0\) to retain a fixed fraction of volume, then
a fixed small radius \(r\) so that on every retained center
\[
r^4\fint_{B_r(x)}|\operatorname{Rm}|^2\le r^4\Lambda\overline K_0
\le\varepsilon_{\rm Li}.
\]
If the smoothing input uses the unnormalized four-dimensional critical quantity \(\int_{B_r}|\operatorname{Rm}|^2\), Bishop--Gromov upper volume gives \(\int_{B_r}|\operatorname{Rm}|^2\le C_{BG}r^4\Lambda\overline K_0\), so a possibly smaller fixed \(r\) supplies that too; no local noncollapse is being assumed.
The Sobolev-volume product cancels:
\[
\mathcal S(K_2^\eta)^{1/2}
\le C{r^2\over \operatorname{Vol}(B_{R_0r})^{1/2}}
((1+\Lambda\overline K_0)\operatorname{Vol}(B_{R_0r}))^{1/2}
=Cr^2(1+\Lambda\overline K_0)^{1/2}.
\]
This does not require local noncollapse.  The global conversion from retained
volume to retained \(A_i\)-scale comes from calibration, not Euler upper bounds:
\[
{3\over4}\operatorname{Vol}(M_i)+o(A_i)=4\pi^2I_i,
\qquad I_i/A_i\to {2\over3},
\]
so
\[
\operatorname{Vol}(M_i)/A_i\to {32\pi^2\over9}.
\]
Remaining support work: prove the sequence-uniform mean full-curvature bound
\(\overline K_0\), state the exact local Sobolev theorem used, and write the
Vitali/Bishop-Gromov/coloring argument with real constants and fixed buffer ratios.

## Positive-branch context from A02 Step 40

A02's diagonal-sector work is independent of the negative cutoff-flow route.  It
identifies the diagonal twist-free toric sector with alternating labels only;
Page, CLW, and toric KE del Pezzo examples are outside that sector.  For the
stress family \(\#_k(S^2\times S^2)\), the current positive-branch question is
whether any diagonal \(T^2\)-Einstein metric exists for \(m\ge6\).  A02 found a
large rod/polygon gap and linearized rigidity at the product metric, suggesting
nonexistence within that symmetry sector, but this does not settle Yau-26 because
the output Einstein metric need not be toric and the antecedent has no symmetry.
The open speculative topological direction is whether simply connected positive
Einstein 4-manifolds with \(T^2\) symmetry must have \(b_+\le1\).

## Current best next work

The next agent should continue in Execute or switch to Constructor-style Execute
for the all-order analytic repair.  The most valuable concrete target is not
support construction alone and not final writing: derive the full shifted \(U\)
equation and higher unweighted \(T\) modules at arbitrary order, using the A03
m=2 double-IBP pattern as the base case, then integrate with the conditional
K2--Y--J6--Q estimates.  In parallel, a separate Actuator/Constructor step can
finish the support-selection theorem with the corrected maximal-function
normalization and calibration volume ratio.

# Endpoint covariance and actual shrinking-surgery stability

27 September 2026. Base commit
e75105d918ab6cc4d98e1b1b35b5064817cb00f7;
local branch local/yau26-coupled-endpoint-20260927.

[Continuous proof](../continuation/20260927_endpoint_covariance_and_surgery_limits.md),
[editable TeX](../continuation/20260927_endpoint_covariance_and_surgery_limits.tex),
[rendered PDF](../continuation/20260927_endpoint_covariance_and_surgery_limits.pdf).

## What changed mathematically

I52 is one result family, not a separate discovery count for each lemma.
Its final statement concerns actual, further-selected complex-hyperbolic
shrinking-surgery recovery metrics on the established balanced family.
Theorem 9 allows every globally vanishing C0 amplitude in either an
exact TT slice followed by negative Yamabe normalization, or an exact
Bianchi slice with scalar-minus-four endpoints. It assumes no derivative
bound, amplitude rate in h, or competitive endpoint energy.

The proof gives a quantitative inequality, not just a contradiction:

\[
P_{\rm final}\ge P_0+DP_0[k]+c\|\mathcal A_0(k)\|_2^2-Ca^2Q,
\qquad a=\|k\|_\infty,\quad Q=Ah.
\]

The identified derivative includes the metric and volume changes.
The opposite-chirality budget then gives
\(\mathcal E/h\ge4-C'a^2-o(1)\).
In the stated vanishing-amplitude slices, coefficient four is equivalent
to the identified derivative square being o(Q). The raw second-order
graph norm is then o(sqrt Q). Exact conformal identities give low-order
control of the actual final Yamabe factor without an assumed supremum
bound. A nonzero diffuse TT family attains this first-order equality
without being isometric to the bases.

Corollary 11 replaces exact Bianchi gauge on constant-scalar endpoints by
the verifiable condition
\[
a\,\|\delta^*\beta k\|_2=o(\sqrt Q).
\]
It keeps the complete quantitative gauge error. Pure diffeomorphism
oscillations verify that this is weaker than an unweighted small gauge
error, and that neither scalar curvature nor competitive energy alone
automatically supplies a gauge estimate.
For nonconstant-scalar inputs followed by Yamabe normalization,
equation (4.44) instead retains the additional actual scalar-linear
error \(\|Ds_0[k]\|_2^2\). The corresponding small-error condition
is stated, not inferred from an arbitrary nearby input.
The final trace calculation (4.45) shows that only the trace-free
part of the gauge forcing is needed. This is recorded as a refinement
of the same criterion, not as another independent result.

The central analytical connection is the Q-scale graph estimate. The
classical full-tensor CH gap controls the exterior, while annular cutoff
errors and the entire donor cores are paid at the surgery scale. The
nonlinear remainder uses the full product
\(\||\mathrm{Rm}_0|\,|k|\|_2\), not a curvature contraction which
could have a kernel. This removes the background loss \(a^2\sqrt A\).
The preceding \(o(h^{1/4})\) version is retained as a weaker theorem
whose proof does not use the exterior gap.

The qualitative exclusion without a competitive-energy premise alone
would also follow by taking a violating subsequence. The added content
of the square-completion step is the uniform finite-amplitude quadratic
bound and its equality criterion, not deletion of that premise as a
separate discovery.

Sections 3–4 also prove precise arbitrary-background shrinking limits,
including Yamabe normalization after surgery, and their first-order
background/variance penalties. The unmodified-collar exclusion and the
Burns/Schwarzschild construction are classical or inherited I44 inputs,
not newly claimed gluing theories.

## Endpoint continuation and unresolved scope

Sections 1–2 use the same actual constant-weight solution as I51.
They derive weighted determinant/length second derivatives, a weighted
Bochner estimate with its explicit remaining covariance, and the actual
phase-current equation. A simple-zero shell retains nonzero phase
curvature and signed flux despite weak length control. This is an
actual local test, not a closed escape sequence.

O10 remains open. O11 remains open over all metrics: no uniform
gauge-fixing theorem or reduction of arbitrary near-minimizers to the
chosen recovery bases is proved. The CH exterior and the additional
choice of recovery diagonal are genuine hypotheses; numerical core
budgets alone do not imply them. General negative KE backgrounds may
have infinitesimal Einstein deformations, so the CH spectral estimate
cannot be transplanted unchanged.

## Parallel derivation and independent checks

Three existing Astra contexts were continued in successive proof tasks.
A fourth Astra/max agent was started with a clean context for an
independent TT/Weitzenbock audit. These were successive waves within the
available concurrency limit, not four simultaneous subagents. Agents
were read-only; the root integrated all edits.

- direct_zero_flux_20260927g: same-solution endpoint equations,
  weighted Bochner and phase continuation; shrinking/Yamabe comparison.
- endpoint_normalization_review_20260927: independent conformal
  energy/tensor comparison, cutoff estimates, nonlinear square completion,
  equality and actual normalization interface.
- high_index_global_20260927g: actual local shell test, CH all-tensor
  gap, core/exterior localization, approximate gauge and actual pullbacks.
- tt_absorption_independent_20260927: fresh-context rederivation of
  the tensor Hessian estimate, exact identifications, patched graph
  estimate, competitive and noncompetitive nonlinear closure, equality,
  and amplitude-weighted gauge error.

Material corrections retained:

- The cutoff tensor need not retain TT/Bianchi gauge. Apply the explicit
  all-tensor elliptic extension after using the original gauge equation.
- Put all transition annuli in the enlarged core and compare the entire
  cutoff tensor operator on the restored CH cover.
- The actual normalized recovery metrics, not just the raw gluing metrics,
  must converge smoothly on the cutoffs; fixed-j Yamabe continuity,
  removability and uniqueness justify the diagonal.
- Competitive volume asymptotics are not used for arbitrary endpoints.
  The monotone chiral conversion handles arbitrarily large output energy.
- Approximate gauge gives weighted derivative control; it need not give
  an unweighted small Hessian.
- Weak length convergence does not control the endpoint phase curvature.

These are proof checks within this research process, not a journal
referee certification or a worldwide novelty determination.

## Classical sources used

- [LeBrun, Ricci Curvature, Minimal Volumes, and Seiberg-Witten Theory](https://arxiv.org/html/math/0003068):
  actual scalar budgets and the shrinking surgery in Theorem 4.3.
- [Wu, Stability of complex hyperbolic space under curvature-normalized Ricci flow](https://arxiv.org/abs/1106.0511):
  Section 3, Koiso identity and the full symmetric-tensor gap on closed
  CH quotients. Ric=-g in complex dimension two gives the gap 1/3.
- [Gursky–Viaclovsky, Rigidity and stability of Einstein metrics for quadratic curvature functionals](https://arxiv.org/abs/1105.4648):
  classical Bach covariance/identities and TT symbols.
- [Oh–Kim, Appendix 23](https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/07/OhKim.pdf):
  the bundle-valued Weitzenbock identity used without differentiating curvature.
- [Armstrong thesis](https://johnarmstrongmaths.com/publications/resources/thesis.pdf),
  Section 3.3: the exact endpoint compatibility mechanism, not a proof of
  the new weak-error target.

The project Skill preserved supplier quantifiers and the distinction
between V-scale and Ah-scale estimates. It did not prescribe the CH
localization, phase analysis, variational or construction methods.
The full current proofs and project catalogue, not the Skill alone,
were the mathematical sources.

## Reproducible checks and preservation

Run from the project root:

    python3 tools/check_endpoint_covariance_and_surgery_limits.py
    python3 tools/check_constant_weight_and_global_fit.py
    python3 tools/library.py verify
    git diff --check

The new finite suite checks polynomial identities, conformal weights,
CH curvature-action signs, square-completion/chiral algebra, and local
scales. It does not certify the PDE estimates, smooth gluing, actual
gauge supply, or the classical spectral theorem.

The pre-edit full-history backup is
/data/qiushi/research/Yau26_Research_backups/20260927_e75105d_line1.bundle,
SHA256 042fcfe5e3553f81458740636ceae0c8e89dbadb6958856130dee0f86871d143.
Its restoration was checked before editing. The inherited 884-file
baseline and the 10,191 preserved source files remain unchanged.
No live service or installed Skill was modified. No research files
were uploaded, published or packed for the web-GPT handoff.

Recorded execution results:

- New finite suite: 22 tests passed.
- Inherited I51 finite suite: 19 tests passed.
- Library preservation/link check: 884 baseline files, 10,191 source
  records and 763 navigation links; zero failures.
- TeX rendering: 22 pages; no compiler warnings. The nonlinear/equality
  page was also visually inspected.
- Whitespace/conflict check: git diff --check passed.

The continuous-proof SHA256 is
d6d56c3c918a60b6a59a9886dc7c7f9c5f00b68a7b2a087ab0ca8d1e8cf2b89d.
Its generated TeX SHA256 is
da2fe9150d3c347ad9dd4ff825d9b790384fe8606d8fcfb6ac658ccd2821d08a.
The PDF SHA256 is
69231ab49320277e34bbfb331809e2017d14a3e545cd5bc6b327db1a002c9336.

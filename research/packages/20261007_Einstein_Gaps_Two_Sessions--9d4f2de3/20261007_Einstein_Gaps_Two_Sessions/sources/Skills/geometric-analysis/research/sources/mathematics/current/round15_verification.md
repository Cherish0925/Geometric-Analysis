# Round 15 verification

The four research notes were developed in parallel on the Round-14 local
Git baseline afb5f538d5b23a601c3197b8b84391665735800b. No inherited
proof file, installed Skill, live Session, or service was changed.

## Reproduction

Dependencies: Python, SymPy, and mpmath. From this directory run:

~~~bash
python round15_rigidity_check.py
python round15_boundary_response_check.py
python round15_global_check.py
python round15_shear_balance_check.py
~~~

All four commands were rerun successfully on 2026-09-21 using
/data/qiushi/qiushi_engine_v09/.venv/bin/python.
The interpreter was Python 3.12.13, with SymPy 1.14.0 and mpmath 1.3.0.

| Program | Actual checks | Result |
| --- | --- | --- |
| round15_rigidity_check.py | 15 exact groups: scalar decomposition, Weyl model and remainder, constants, twelve first-jet variables, retained Bianchi source, curvature normalization, and the two canonical-form energies | Pass |
| round15_boundary_response_check.py | 7 groups: fundamental solutions, gauge current, ground-state transform, boundary matrices, source traction, full-width amplification, and a scalar exterior-response model | Pass |
| round15_global_check.py | 17 exact identities for boundary action, constraints, momentum, conormals, and a representative assembled capacitance system; one incompatible-source rejection | Pass |
| round15_shear_balance_check.py | 14 exact local identities and three nonbalanced inputs rejected | Pass |

The boundary-response program combines exact symbolic identities with
high-precision finite-parameter checks of asymptotics. Its numerical
limits are not interval-certified suprema. The limits used as results
are derived analytically in the note. The capacitance matrix checks
test the algebra of a representative network; existence and positivity
of the actual exterior harmonic-measure matrix are proved by the
Dirichlet problem and Green's identity, not inferred from that example.

## Proof review

The lead investigator independently recomputed the scalar and Weyl
identities, both-orientation curvature constants, the small-ball
Cheeger–Tian argument, the throat response and its source constants,
and the link between conormal and physical momentum.

The global-line investigator independently reviewed the rigidity
identities and the curvature/compactness consequences, including the
classical regularity statements. The construction-line investigator
also checked the principal rigidity constants and regularity argument.
The following refinements were adopted:

- The no-bubbling consequence requires exact metrics with volume
  approaching the sharp scalar-volume bound, or absolute excess
  \(D\leq D_0\). It does not cover every sequence minimizing Einstein
  volume at an unknown higher infimum.
- Compact-limit arguments transport the globally defined quadratic
  spinor two-forms. They do not assume an unstated identification of
  spin-c structures under compactness diffeomorphisms.
- The existence of a noncollapsed pointed limit uses the separate
  Cheeger–Tian thick-basepoint estimate.

The construction and global investigators cross-checked the matching
and integral-balancing arguments. In particular the physical Robin
term was retained until cancellation across a matched interface;
the branched-cover example was checked at its branch points and with
integral periods; and the closed functional includes every exterior
product contribution.
The final synthesis was independently checked against the proofs.
Its waist amplification is explicitly a projected Bianchi-gauged
boundary response, not an ungauged all-mode Einstein repair.

Static checks passed for all four Python programs, balanced math
delimiters in the six Markdown files, and all 24 local Markdown links.
The staged Git diff passed the whitespace check.

These reviews support the stated proofs. The finite programs do not
verify gauge-theoretic existence, compactness theorems, the global
branched covering, or a nonlinear Einstein solution.

## Classical inputs checked

- [LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*](https://arxiv.org/pdf/math/0003068):
  actual monopole and spinor identities. The specified square and
  both-orientation hypotheses remain explicit.
- [Ge–Jiang, Theorem 1.1](https://arxiv.org/pdf/1707.05511):
  the Cheeger–Tian four-dimensional Einstein regularity theorem uses
  small absolute \(L^2\) curvature energy, without a volume lower bound.
- [Cheeger's lecture, slides 2–3 and 8–9](https://sites.duke.edu/scshgap/files/2016/08/dim4dukebeamer.pdf):
  absolute-energy regularity and a noncollapsed basepoint under a
  total-energy bound. Curvature-operator and full-tensor conventions
  differ by a factor of four in squared norm.
- [Anderson, Section 3 and Proposition 3.1](https://arxiv.org/pdf/math/0612647):
  the ordinary Einstein Dirichlet problem is not elliptic; no unrestricted
  nonlinear filling map is assumed.
- [Rupflin–Topping–Zhu, equations (1.1)–(1.2)](https://arxiv.org/pdf/1209.3783):
  harmonic-map energy variation and the Hopf differential. The shear
  potential identities in this round are derived directly.

## Unresolved mathematical steps

The averaged TT compatibility condition is not the full boundary
equation. Its nonlinear exterior term and the remaining boundary modes
are present in the notes, not proved to vanish. The waist Dirichlet
amplification does not exclude all possible exterior responses.
The sharp-volume compactness result does not identify the limit's ends
with the original shear graph or exclude Einstein metrics at larger
volume. No new full Yau26 sign branch is claimed.

The work adds proofs and explicit models to the three scientific lines;
it does not reclassify the inherited hypotheses or establish literature
priority.

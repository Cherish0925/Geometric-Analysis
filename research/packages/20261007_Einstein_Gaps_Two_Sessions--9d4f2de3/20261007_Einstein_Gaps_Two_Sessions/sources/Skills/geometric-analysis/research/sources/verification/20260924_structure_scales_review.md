# Proof integration: global structure and realization scales

24 September 2026. Local research continuation from `8594adf`.
No live Session, installed Skill, service, external repository, or research
source archive was changed. This record identifies bounded checks; it is
not independent peer review or a literature-priority certificate.

## Mathematical work and review

Three independent worktrees supplied full English proofs:

- Thin-monodromy alternative: source commits `c67055b`, `4b4c46f`;
  integrated as `ec4a364`, `9e40a76`. Root read the full argument:
  simultaneous length-gap preservation, thick finite-isotropy lemma,
  actual transport bound, minimal-submersion Ricci identity, marked smooth
  bundle realization, and residual monodromy after cutting. The signature-zero
  comparison was checked against retained Round 20, rather than counted
  as a new construction. Three missing spacing commands were corrected.
- Nonlinear slow moduli: source commit `9d6a24e`; integrated as `a336efd`.
  Root checked all Ricci blocks and the completed square, the retained
  normal acceleration, deck averaging and fiber-preserving distance proof.
  The companion was developed by root and independently checked by the
  slow-mode author; the variable-base harmonic projection and energy
  identity were also checked by the monodromy author.
- Harmonic zero scale: source commit `1811625`; integrated as `a616d71`.
  Root checked the rescaling, local L2-bound dichotomy, first-order elliptic
  bootstrap, removal of the auxiliary field, whole-core condition and
  distinction between the period-preserving counterexample and the full
  pointwise Ricci input. The supply constants 49 and 720 were checked in
  `line1_composed_application.md`. The inherited filling classification
  and global QG smoothing remain explicitly cited inputs, not re-proved here.

The new actual-gauge companion proves exact canonical class supply and the
functional/slow-energy identity; its variable-base version retains the
negative harmonic projection. Classical Taubes nonvanishing and LeBrun's
Propositions 4.1–4.2 are cited as inputs, not claimed as new results.

## Reproduction and boundaries

Run `python3 tools/check_structure_scales.py` for this continuation only.
Its report is [the check record](20260924_structure_scales_checks.json).
It renders five sources and runs three finite scripts:

- short-length configurations, the explicit thin-fiber coefficient, and
  concrete rational monodromy tests;
- an independent full coordinate Ricci computation and 14 exact checks,
  including negative controls for dropping normal acceleration or replacing
  the scalar Laplacian by a full Hessian;
- 25 exact checks for actual gauge energies, opposite projections,
  harmonic-form derivatives, scalar spectral constants and deck averages.

These tests support the displayed algebra, not the global geometric proofs.
Run `python3 tools/library.py verify` for archive/baseline byte preservation,
catalogue consistency and new navigation links. That check has no PDE meaning.

No claim is made that an invariant multicurve solves Einstein gluing, that
fixed-amplitude separation covers every Einstein output, or that raw small
defect automatically controls the fourth power of the whole-core scale.
The three result families are I35–I37; the companion is part of I36 rather
than a fourth independent breakthrough.

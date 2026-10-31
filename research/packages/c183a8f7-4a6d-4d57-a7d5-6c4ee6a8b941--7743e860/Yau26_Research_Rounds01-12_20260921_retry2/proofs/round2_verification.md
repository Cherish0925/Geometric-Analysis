# Round-two reproduction and proof checks

Executed on 19 September 2026 in the isolated research repository containing
this file. The existing numeric environment resolves to Python 3.12.13 and
SymPy 1.14.0. No packages were installed or upgraded.

## Reproduction

From this directory, execute each command:

```bash
qiushi-yau26 env numeric python round2_rigidity_check.py
qiushi-yau26 env numeric python round2_weak_curvature_check.py
qiushi-yau26 env numeric python round2_construction_check.py
qiushi-yau26 env numeric python round2_construction_cross_check.py
qiushi-yau26 env numeric python round2_global_checks.py
```

The final versions of all five programs were rerun by the root agent and
exited successfully. They use exact SymPy identities; printed decimals
are illustrations of exact expressions, not interval certificates.

| Program | Checked mathematical content |
| --- | --- |
| `round2_rigidity_check.py` | Good-set gap, projection/amplitude constants, distance to the Weyl orbit, derivative of the quadratic spinor map, all twelve first-jet components of the weighted-energy identity, curvature-potential identity, and endpoint scaling. |
| `round2_weak_curvature_check.py` | All five Weyl components and arbitrary four-dimensional covector in the divergence symbol; full eight-dimensional orbit-tangent first-jet Gram matrix; exact Fourier scaling. |
| `round2_construction_check.py` | All ten invariant Jacobi sectors for an arbitrary jointly radial coefficient; complete one-factor quadratic source including mixed block; Bianchi identity; projection integrals; exact factorization and scalar L2 lower bound. |
| `round2_construction_cross_check.py` | Direct coordinate-Christoffel/Ricci expansion of all sixteen simultaneous cross entries; Bianchi identity; both length contractions and their combined source. |
| `round2_global_checks.py` | All sixteen Ricci components before and after the torus shear, conserved charge and its asymptotics, twist energy, threshold inversion, recovery of the OT expression, and weighted transport integral. |

Selected exact outputs are

\[
 \frac{241}{1024}-\frac{\sqrt{134}}{512}>\frac18,
 \qquad \frac{74}{81}<1,
 \qquad \frac{1680145}{2592}<649,
\]

\[
 \operatorname{Spec}(G_{\rm orbit})=\{1\ (4),3\ (4)\},
 \qquad I_1+I_2=-\frac{\pi^2}{2}(b_1^2+B_1^2),
 \qquad q_*(0)=9\sqrt2-12.
\]

## Analytic arguments checked separately

The scripts do not prove elliptic regularity, the complete bounded-kernel
classification, a global gluing theorem, or a general Ricci-pinching gap.
Those claims are considered at their actual scope in the derivations.

- [Weak-source review](round2_weak_review.md): independently reconstructs
  the negative-order elliptic estimate, absorption of coefficient errors,
  recovery of the local L2 curvature bound, and regularity of the weak
  Einstein limit. Its norm-label correction is incorporated in the checker.
  The final supplement checks the bounded-full-curvature averaged gap,
  including center selection, buffered path lifting, multiplicities, local
  harmonic-coordinate applicability, and the localized degeneration result.
- [Spinor approximation review](round2_rigidity_review.md): checks every
  rounded constant and the intrinsic negative norm. Root follow-up reads
  the actual spinor spectral-defect input and independently derives the
  weighted Hodge integration signs and necessary derivative-energy limits.
- [Construction review](round2_construction_review.md): checks the
  nonseparable kernel argument, operator-domain justification of the
  Bianchi gauge, actual all-block second-order repair, and boundary flux.
  The initially omitted arbitrary-gauge boundary contribution is now
  included in the proof.
- Root review of the connector note checks the separator/charged Bochner
  combination and reproduces the complete weighted Fisher-information
  calculation for the stated resolvent constant. The standard toral AdS
  background is identified with Anderson's published metric, not presented
  as a new Einstein construction.

Root also found and corrected a false inference from a uniform scalar L2
spectral gap to matching of a pointed thin-core limit. The explicit
\(J(u)\chi(u/R)\) counterexample and the stronger normalized residual
condition replace that inference in construction Section 8.

The final local Git change passes `git diff --cached --check`. There is
no remote configured for this research repository. The live Skill and
Qiushi services, Session configurations, and research workspaces were not
modified.

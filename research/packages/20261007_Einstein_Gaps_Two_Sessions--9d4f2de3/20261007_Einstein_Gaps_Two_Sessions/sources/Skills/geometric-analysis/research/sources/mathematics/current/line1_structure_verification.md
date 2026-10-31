# Proof review and reproducibility

23 September 2026. Baseline: local commit `ef6a282`.

## Mathematical review

The Yamabe paper was derived by the analytic worker and independently read
by a second worker and the lead. The reviews checked the full statement,
not only its symbolic program:

- Maximum-principle amplitude bounds; the positive-mass resolvent and its
  gradient estimate under a Ricci lower bound only; all integral constants.
- The logarithmic bump's bounded Laplacian, its prescribed trace-free
  Hessian, and convergence in the precise Holder spaces used by the proof.
- Cancellation of all Laplacian-of-bump terms under the nonlinear change
  of unknown; invertibility of `6 Delta + 8` on the fixed surface.
- The conformal Ricci formula, output normalization, and the original
  family's curvature, diameter, injectivity-radius and scalar-gap bounds.

The canonical shear paper was checked against the original closed-gluing,
virtual-Kahler, and harmonic-form proofs. The added calculation uses an
**auxiliary** oriented-plane connection, not the projected Levi-Civita
connection. The lead checked its sign, endpoint gluing, the compactly
supported primitive, and every coefficient in the two energy polynomials.
The fixed-form conclusion uses Moser on each compact positive-parameter
interval; no limiting diffeomorphism is assumed.

The inherited virtual-Kahler proof uses tree factorization. Its stated
hypotheses were checked against [Nicolas, Theorem 25 and Lemma 24](https://arxiv.org/pdf/2102.01128):
minimal action, no fixed end, tree neither a line nor a point; the kernel
of the induced orbifold quotient is finitely generated and acts trivially.
The exact almost-Kahler comparison was checked against
[Apostolov--Armstrong--Draghici, Theorem 2](https://arxiv.org/pdf/math/0109098),
not inferred from a summary of that theorem.

The inherited bundle Hessian lemma was independently rederived. For
`v_i = nabla_i u`, `H_ij = nabla_i v_j`, and connection curvature `F`,
the slot swap `H_ij - H_ji = F_ij u`, followed by commutation on the
bundle-valued one-form `v`, gives exactly the original identity without
any derivative of `F`. Integrating the divergence of
`|v|^2 <u,v_i>` gives the required fourth-power estimate. This review
checks that interface; it is not a new certification of every inherited
proof.

## Executable checks

Run from this directory with a Python interpreter containing SymPy:

```bash
python verify_line1_structure.py
```

This runs the two new exact check programs and three relevant inherited
programs, validates local document links and original uploaded-source
hashes, and checks compiled paper logs. Results, individual program output,
and document hashes are saved in
[the generated evidence record](line1_structure_evidence/results.json).

The two new checks verify finite exterior algebra, Euler correction,
curvature-energy coefficients, the bump differential identity, the
nonlinear scalar substitution, and normalization constants. They do not
replace the implicit-function theorem, global Euler patching, Moser, SW
theory, or the group-theoretic proof. Those are addressed in the manuscripts
and the proof review above.

## Files and changes

The increment adds two English mathematical manuscripts, their standalone
LaTeX/PDF versions, two check programs, this record and one short reading
entry. Prior proofs and uploaded sources are unchanged. All work is local;
the installed Skill, live v08/v09 services and Sessions are untouched.

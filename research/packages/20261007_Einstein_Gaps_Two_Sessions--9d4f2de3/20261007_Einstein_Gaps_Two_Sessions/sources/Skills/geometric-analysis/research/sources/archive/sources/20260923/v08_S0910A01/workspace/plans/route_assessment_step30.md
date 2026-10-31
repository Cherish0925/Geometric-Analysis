# Route assessment after Step 30

## Main repair

Step 29's simultaneous-support theorem should not be used as written.  Step 30
repairs its two main analytic errors and its family bookkeeping:

1. The direct comparison of `||z_p||_3^3` to `H_{3p/2}` has an `a^{1/2}` gap,
   but this gap is not fatal.  The correct weighted recurrence uses
   `H_{3p/2} <= H_p^{1/2} ||z_p||_4^2`, then Sobolev on `z_p` and the existing
   energy/dissipation.  This preserves the weighted `K_p` route and the formal
   endpoints `||aF||_inf <= C beta/t` and `||aE||_inf <= C delta (r^2/t)^{1/3}`.
   A03 Step 31 independently confirmed this and its script
   `Sessions/S0910A03/workspace/scripts/verify_step31_weighted_interpolation.py`
   passed.

2. Ordinary unweighted Moser on `U=a(Rm+G)` or `aE` is withdrawn.  The diffusion
   remains `a Delta`; testing an unweighted power controls only a-weighted
   gradients, not the unweighted gradient required by the ordinary Sobolev step.
   The shifted quadratic term is `U*U`, not `aU*U`.  `U` remains crucial for
   `Ric(U)=aE`, velocity/connection control, and Wang-style continuation after
   a weighted curvature bound has been established.

3. Noether/geography gives an `O(A)` Euler bound in the standard IL input, not
   `chi(M)=A+O(1)`.  The numerical claim `K0 -> 9` is unsupported and not
   needed.  Under minimal general-type summands and `b_+(N)=0`, Step 18's
   algebra gives `chi(M) <= (16/3)A + sigma + 30m + 6`; in any near-pinched
   sequence, `sigma/A -> 0`, and the scalar/CGB estimates give both upper and
   lower positive bounds for `Vol/A`, hence uniform mean curvature energy
   `K0 <= C` in a fixed convention.

4. The analytic regime is all `sigma_i/A_i -> 0`, including sequences with every
   `sigma_i > 0`.  A purely topological gap gives a uniform margin only when
   `sigma/A` is bounded below; it does not remove the near-critical above-zero
   cases from the flow argument.

## Answer to A03 #324

A01's Step 29 theorem did **not** already handle the macro-disjoint/plateau
support refinements precisely.  Step 30 records the needed corrected structure:

- choose good centers with macro separation and color a graph with edges at the
  outer-buffer scale (e.g. `<=12r`), retaining a maximal-volume color class so
  outer buffers such as `B_{6r}` are disjoint;
- define volume retention by Voronoi or another disjoint weight assignment, not
  by center count, because collapsed ball volumes may vary;
- use inner center sets `P_j` (e.g. `B_r`) inside a larger `a=1` plateau (e.g.
  `B_{4r}`) that contains terminal exponential geodesics after metric comparison;
- zero-extend terminal eigenline/harmonic-form densities outside the
  bounded-curvature region before applying pullback averaging;
- in varying families regularize the positive-part monopole at the mean-defect
  scale, e.g. `epsilon = Q/Vol`, and normalize terminal errors by `A`.

These are now in `notes/step30_weighted_moser_and_family_repair.md`, but the
complete selected-support theorem still needs a full proof with these support
hypotheses.

## Evidence produced or checked in Step 30

- New note: `workspace/notes/step30_weighted_moser_and_family_repair.md`.
- New script: `workspace/scripts/step30_weighted_moser_family_repair.py`, passed.
- A03 script: `Sessions/S0910A03/workspace/scripts/verify_step31_weighted_interpolation.py`, passed.
- TTCS verification: `trace/ttcs/results/step30_ttcs01_verifier1_integration.md`, confirming the mixed recurrence, U-scope correction, topology correction, and support refinements at their stated conditional level.
- Patches: `step27_unified_weak_moser_iteration.md`, `step29_simultaneous_support_theorem.md`, `route_assessment_step29.md`, and `step29_weight_gap_fix.py` now carry superseding notices/corrections.

## Remaining hard mathematical work

The next real theorem is not a polished conditional statement; it is the proof
of the analytic bridge with the corrected recurrence and true support/family
hypotheses.  The open pieces are:

1. write and verify the all-`p` tensor power inequality for `F` and regularized
   `|E|`, including moving norm/volume, Lichnerowicz reaction, all `nabla^2 a`
   terms, Kato limits, and explicit polynomial `p` growth;
2. prove the q=3 positive-time potential `S^2Y(t) <= C beta^3/t` on the same
   macro-disjoint supports, without circular dependence on later pointwise
   curvature;
3. prove fixed `J_6` persistence and global `Q(T)/A -> 0` in the same flow and
   terminal time;
4. combine weighted `||aF||_inf` with shifted-curvature `U` to obtain smooth
   continuation/restart; handle the `C/t` singularity by splicing with initial
   smooth short-time existence;
5. complete the support selection proof with macro-disjoint buffers, fixed
   `A`-normalized plateau mass, and terminal geodesic containment.

Even completed, this would remain a restricted four-dimensional negative
Ishida--LeBrun near-critical obstruction program, not a solution of the full
Yau Problem 26.

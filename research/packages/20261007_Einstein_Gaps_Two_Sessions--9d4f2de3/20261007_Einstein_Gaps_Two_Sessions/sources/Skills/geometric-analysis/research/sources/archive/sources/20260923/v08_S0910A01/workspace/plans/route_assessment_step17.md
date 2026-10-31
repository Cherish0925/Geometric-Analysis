# Route assessment after Step 17, corrected in Step 18

## What remains valid

### Support-scale geometry

The support-scale construction fixes the geometric scale mismatch from Step 16.
A Vitali selection at radius `r_*`, followed by thinning, gives separated
supports `B_{5r_*}(p_j)` with plateaux `B_{4r_*}(p_j)` and bootstrap domains
`B_{r_*}(p_j)` occupying a fixed positive fraction of the selected good-set
volume.  For centers close enough to `p_j`, the maximal-function bound gives

```text
r_*^4 average_{B_{r_*}(y)} |Rm(g_0)|^2 <= C K_0 r_*^4,
```

which is below Li's small-energy threshold after choosing a sufficiently small
fixed physical scale `r_*`.

### Plateau containment

With plateau radius `4r_*`, the balls that appear in Li's covering argument
for `x in B_{r_*}(p_j)` are contained in the plateau.  This is a useful
geometric input only.  It does not prove a localized Li bootstrap, because the
supremum controlled by the local energy argument cannot be restricted to the
inner centers without reopening the inner/outer closure problem.  The previous
wording that the plateau bootstrap was established has been replaced in
`workspace/notes/step17_support_scale_li_bootstrap.md`.

### Four-dimensional Sobolev-energy cancellation

For a support `U` at scale `r`, with initial control

```text
average_U |Rm|^2 <= K_0,
```

the relative Sobolev coefficient and curvature norm satisfy

```text
A_U ||Rm||_{L^2(U)} <= C sqrt(K_0) r^2.
```

The volume factor cancels, so the absorption mechanism is compatible with
collapse.  This is an algebraic scaling fact, not a completed flow theorem.
It is the right engine for the defect-energy reaction term when the test
function is `chi E`.

## The corrected analytical target

The remaining object is a full-support continuation theorem for the degenerate
cutoff flow

```text
partial_t g = -2 chi^2 (Ric + g),       a = chi^2.
```

The theorem must handle the entire support and transition region, retaining the
cutoff derivatives and the coupling between curvature and Einstein defect.  It
must jointly produce:

1. metric comparability on the active support;
2. persistence of the relative Sobolev inequality and finite-overlap cover;
3. weighted curvature control, naturally for `a Rm` or `chi^2 Rm`, not an
   unweighted transition bound;
4. a weighted pointwise defect estimate for `a E` sufficient to control metric
   speed;
5. an unweighted support-summed growth bound for `Q(t)=int |E(t)|^2`, because
   topological recalibration uses unweighted defect energy.

The scalar weighted curvature calculation starts from a schematic inequality

```text
partial_t K <= a Delta K + c a K^2 + T,
```

where `K=|Rm|` and `T` contains cutoff and coupled-defect terms.  For
`f=aK`,

```text
partial_t f <= a Delta f - 2 <nabla a, nabla f>
              + (2|nabla a|^2/a - Delta a) f
              + c f^2 + aT.
```

Thus the quadratic reaction becomes `c f^2`; there is no artificial
`1/a` reaction.  The principal operator remains degenerate, and the real work
is to control the derivative couplings in `T` and the unweighted defect energy.

## Cutoffs

A pointwise bound `|Hess chi| <= C/r_*^2` is not automatic from bounded Ricci.
Whenever possible, the estimates should integrate Hessian terms by parts so
only gradient-cutoff quantities enter.  If a pointwise Hessian bound is still
needed, constructing such cutoffs under the actual sequence hypotheses is part
of the theorem's application.

## Downstream layer after a successful continuation theorem

If the full-support theorem supplies bounded-curvature buffers on a positive
volume proportion and `Q(t_0)/A_i -> 0`, the post-smoothing contradiction can
use existing work:

- exponential-pullback averaging from A03 Step 16;
- the positive-part monopole weight repair and joint amplitude/eigenline
  density from A03 Step 16;
- the Step 8 tensor-defect/Derdzinski forbidden-germ mechanism;
- topological recalibration by the mixed Seiberg-Witten and Chern-Weil
  identities on the same smooth four-manifolds.

This would exclude the critical LeBrun/Ishida-LeBrun negative laboratory, not
the full four-dimensional sign branch, the positive branch, higher dimensions,
or the Lean formalization target.

## Files

- Corrected support-scale note: `workspace/notes/step17_support_scale_li_bootstrap.md`
- Step 18 weighted-system note: `workspace/notes/step18_weighted_cutoff_system.md`
- Step 18 algebra scripts: `workspace/scripts/step18_weighted_cutoff_algebra.py`,
  `workspace/scripts/step18_sobolev_scaling.py`
- A03 coupled system: `Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md`

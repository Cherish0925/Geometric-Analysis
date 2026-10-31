# Independent review of the invariant construction, sections 1–7

Date: 2026-09-19. Scope: `round2_construction.md`, sections 1–7, and its two
symbolic checkers. Section 8 is excluded from this review. The source note
was not edited by the reviewer.

**Conclusion.** The bounded-kernel classification, invariant L2 inverse,
all-block second-order repair, and corrected flux statement are sound in
the stated complete double-cylinder model. One boundary/gauge omission was
identified during review and has been corrected by the author. I found no
remaining mathematical error in sections 1–7.

## 1. Bounded kernel: the nonseparable step is justified

The ten scalar sector formulas were checked against the actual covariant
Einstein operator with an unrestricted joint coefficient. The half-plane
comparison for a horizontal TT coefficient is valid: on sufficiently far
half-planes the potential is uniformly positive, the coefficient is
bounded, and the barrier `C sech(t)^2` solves the same homogeneous
equation. The bounded maximum principle consequently gives
`|z| <= C sech(t)^2`, not merely decay with an unspecified rate.

After writing `z=sech(t)^2 a`, the transformed equation has uniformly
elliptic principal part and uniformly bounded smooth drift on R2. A bounded
solution therefore has uniformly bounded derivatives on Euclidean balls.
This justifies differentiation under the finite `sech(t)^3 dt` integral
and the boundary integrations in the weighted-average argument. The
factorizations `D*D` and `DD*=2+E*E` give the required mean-zero gap. Thus
the bounded nonnegative variance obeys `P_u w >= 4w` and vanishes by the
bounded maximum principle. No separation assumption is hidden here.

The eight surviving fields are all TT. None of their nonzero linear
combinations is globally L2: a transfer coefficient `c0+c1 J` cannot vanish
at both ends unless both constants vanish. “Four radial ends” refers to
the four coordinate escape directions, not four topological ends.

## 2. L2 repair: this solves the actual linearized equation

The scalar conjugation identity gives `-P >= 1/4` in the weighted
Friedrichs form domain. The TT ground-state identity is nonnegative;
together these imply `Delta_E >= 1/4`, hence `L >= 1/8`, on the full
invariant tensor space. The mixed blocks have a still larger lower bound.
The eight bounded non-L2 modes do not contradict this gap.

The displayed full quadratic source and its fixed derivatives are bounded
by `C sech(t) sech(u)`, so they belong to the weighted L2 space. The
Friedrichs inverse gives `K` in the operator domain. Because the curvature
potential is bounded, its form-domain membership implies `nabla K` is L2;
thus `beta K` is indeed L2, as needed for the gauge argument. The exact
identity `beta L = (Delta_H+2) beta/2` and `beta D=0` then force
`beta K=0` on this complete manifold. In particular, the inverse does not
only solve a gauge-fixed surrogate: it solves `D Phi K=-D`.

Uniform smooth bounds can also be obtained directly from the reduced
two-variable scalar operators: their coefficients have uniform smooth
bounds, their principal parts are Euclidean, and
`cosh(t) cosh(u) >= 1`. Global weighted L2 control therefore supplies
uniform local unweighted L2 control, followed by interior elliptic
estimates. This avoids any unstated injectivity-radius hypothesis. The
claimed uniformly small, positive metric and `O_Ck(s^3)` residual follow.
It remains a model second-order repair, not an exact Einstein solution or
a closed-manifold inverse estimate.

## 3. Source, normalization, and boundary qualification

Both checkers passed independently in this review:

- `python round2_construction_check.py`: all ten unrestricted joint
  sectors, single-fibre source, mixed component, Bianchi identity,
  projections, and factorizations;
- `python round2_construction_cross_check.py`: all sixteen entries of
  the simultaneous cross-Ricci source and its Bianchi identity.

The TT tensors `T_i,S_i` have squared tensor norm 2. The displayed
contractions, including the factor 2 in an off-diagonal pairing, are
consistent with this convention. The two length-source integrals and
their sum `-pi^2(b1^2+B1^2)/2` are correct. The cross terms integrate to
zero by an actual odd radial factor, and these integrals converge
absolutely. Angular periods are set to 1: changing the periods preserves
the reduced operator and its gap but multiplies the integrated pairings
by the product of those periods. No collapse-uniform normalized flux is
being inferred merely from angular invariance.

The original unconditional phrasing of the end-flux obstruction omitted
a gauge boundary contribution. The present section 6 correctly states

    lim [Flux(K,Q) - GaugeFlux(K,Q)] = - integral <D,Q>,
    GaugeFlux(K,Q) = integral_boundary Q(nu,beta K).

For the constructed Bianchi-gauge L2 repair the gauge term vanishes, so
the asserted nonzero Green flux follows. For an arbitrary actual repair,
zero Green flux alone is insufficient. Compact support, or the stated
`exp(-(1+eta)(|t|+|u|))` bound on K and its first derivatives, makes both
boundary terms vanish and does yield the conditional contradiction.
These corrected distinctions are necessary, not optional presentation.

No additional end condition is obtained from L2 membership, and the note
now correctly leaves reception and matching of this flux to the global
problem. The epsilon-scale discussion retains its necessary invariant
leading-limit and marking qualifications.

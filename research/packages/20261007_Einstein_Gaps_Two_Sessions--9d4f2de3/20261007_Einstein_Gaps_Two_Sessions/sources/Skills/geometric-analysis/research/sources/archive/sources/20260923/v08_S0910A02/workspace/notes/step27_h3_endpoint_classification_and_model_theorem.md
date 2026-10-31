# Step 27 addendum: endpoint classification for the diagonal H3 model

Session `S0910A02`. Agent4/Preceptor. Phase Explore.

This addendum upgrades the Step-27 review from a cautious closure statement to a
precise theorem under explicit cohomogeneity-one/tubular-end hypotheses.  It remains a
model theorem, not a proof or refutation of Yau-26.

## 1. Geometric setting

Let \(N\) be a compact quotient of the real Heisenberg group with fundamental group
\[
\Gamma=\langle x,y,z\mid [x,y]=z,\ [x,z]=[y,z]=1\rangle.
\]
The center is \(Z(\Gamma)=\langle z\rangle\), and
\(\Gamma/Z(\Gamma)\cong\mathbb Z^2\).  Think of \(z\) as the central circle in the
standard circle bundle
\[
S^1_z\longrightarrow N\longrightarrow T^2.
\]

Consider a compact smooth 4-manifold whose regular part is an interval or circle times
\(N\), with diagonal metrics
\[
g=dt^2+a(t)^2(\theta_1^2+\theta_2^2)+c(t)^2\theta_3^2,
\qquad b(t)=c(t)/a(t)^2,
\]
where \(\theta_3\) is the central direction.  Assume an interval endpoint is an ordinary
smooth tubular end: a small boundary hypersurface around the singular stratum is the
unit normal-sphere bundle of that stratum and is diffeomorphic to \(N\).

This is the natural smooth compactification hypothesis for a cohomogeneity-one or
singular-foliation model.  It excludes orbifold/edge ends; those must be named
separately if someone wants to include them.

## 2. Topological endpoint classification

Let an endpoint have singular stratum \(S\) of dimension \(s\), so the normal disk has
rank \(4-s\) and the boundary hypersurface \(N\) is an \(S^{3-s}\)-bundle over \(S\).

### Case \(s=0\)

Then \(N\) is an \(S^3\)-type normal sphere (or spherical space form in the presence of
a finite normal isotropy).  Its fundamental group is finite in the spherical-space-form
case and trivial in the ordinary sphere case.  This cannot be the Heisenberg group
\(\Gamma\), which is infinite nonabelian nilpotent.

### Case \(s=1\)

Then \(N\) is an \(S^2\)-bundle over a circle.  Since \(S^2\) is simply connected,
\(\pi_1(N)\cong\mathbb Z\).  Again this cannot equal \(\Gamma\).

### Case \(s=2\)

Then \(N\) is a circle bundle over a closed surface \(S\).  The long exact homotopy
sequence gives an extension
\[
1\to\mathbb Z_{\rm fiber}\to\Gamma\to\pi_1(S)\to1.
\]
For an oriented tubular neighborhood, the circle fiber subgroup is central in
\(\Gamma\).  Since the center of \(\Gamma\) is exactly \(\langle z\rangle\), the
collapsing circle is the central circle.  The quotient by it is \(\mathbb Z^2\), so
\(\pi_1(S)\cong\mathbb Z^2\), hence \(S\) is a torus among closed surfaces.  Thus every
ordinary smooth endpoint is the standard central-circle filling: a disk bundle over
\(T^2\) whose boundary is the Heisenberg nilmanifold.

This proves the endpoint classification needed for the diagonal model: finite smooth
ends force
\[
c(t)\to0,
\qquad a(t)\to a_0>0,
\qquad b(t)=c(t)/a(t)^2\to0.
\]
The metric smoothness part is the usual polar-coordinate condition for the normal disk
fiber: the circle radius vanishes linearly while the metric along the bolt stays
positive definite.  The topological argument identifies which circle can vanish.

## 3. Positive Ricci monotonicity theorem for closed diagonal H3 models

The Step-27 algebra gives, in the exact \(\operatorname{Ric}=\Lambda g\) model,
\[
C_\Lambda=b^2+4k_1^2+8k_1k_3+4\Lambda=0
\]
and
\[
\big((\log b)'\big)^2\ge\frac54(b^2+4\Lambda).
\]
For \(\delta\)-pinched diagonal components around \(\Lambda\), the formalized pinched
version is
\[
\big((\log b)'\big)^2\ge\frac54(b^2+4\Lambda-8\delta).
\]
In particular, if \(\Lambda>0\) and \(\delta<\Lambda/2\), then
\[
|((\log b)')|\ge\sqrt{5(\Lambda-2\delta)}>0.
\]

### Circle regular part

If the regular orbit space is a circle, then \(b\) is positive and periodic.  A positive
periodic \(C^1\) function has a critical point, contradicting the positive lower bound
on \(|(\log b)'|\).

### Interval regular part

If the regular orbit space is a compact interval with ordinary smooth tubular ends,
the endpoint classification above shows \(b\to0\) at both ends.  Then \(b\) has a
positive interior maximum, again contradicting \((\log b)'\ne0\).

Thus:

> **Model theorem.** Under the ordinary smooth tubular-end hypotheses above, no compact
> closed 4-manifold carries a diagonal cohomogeneity-one Heisenberg-nilmanifold metric
> whose diagonal Ricci components are \(\delta\)-pinched around a positive constant
> \(\Lambda\) with \(\delta<\Lambda/2\).  In particular, no exact positive Einstein
> metric occurs in this diagonal \(H_3\) cohomogeneity-one class.

This is stronger and cleaner than the prior cautious statement.  It is still a model
class theorem: it uses the diagonal \(H_3\) ansatz, one-dimensional base, no twist, and
ordinary smooth endpoints.

## 4. Negative witness and sign asymmetry

Restoring \(\Lambda\) also shows why the same theorem is false in the negative sign.
The complex-hyperbolic horosphere data
\[
\Lambda=-3/2,
\quad b=1,
\quad k_1=-1/2,
\quad k_3=-1
\]
satisfy
\[
C_\Lambda=0,
\quad (\log b)'=0,
\quad k_1'=k_3'=0.
\]
Here \(b^2+4\Lambda=-5<0\), so the positive lower bound becomes vacuous.  The sectional
curvatures in the Step-27 audit are
\[
K_{01}=K_{13}=K_{23}=-1/4,
\qquad K_{03}=K_{12}=-1,
\]
matching the expected complex-hyperbolic range.  Stable nonabelian nilpotent
horosphere geometry is therefore a negative-Einstein phenomenon; positive Einstein
constant forbids it in this diagonal model through the term \(4\Lambda\).

## 5. Lean-checked algebraic kernel and unformalized parts

The real-algebra inequalities used here are formalized in
`workspace/proofs/Step27H3Algebra.lean` and checked by
`qiushi-yau26 lean` for the declarations
`Yau26Step27.both_lower_pinched_from_rho_bounds` and
`Yau26Step27.rate_ne_zero_pinched_from_rho_bounds`.  The certificates are
`workspace/proofs/step27_h3_algebra_both_check_v2.json` and
`workspace/proofs/step27_h3_algebra_rate_ne_zero_pinched_check.json`.

The following pieces are **not** Lean-formalized:

1. the moving-frame derivation from the geometric metric to the Ricci-component
   equations, though it is symbolically checked in Python and independently verified by
   TTCS in Step 26;
2. the topological endpoint classification via tubular neighborhoods and fundamental
   groups;
3. the smooth polar-coordinate assertion \(c\to0, a\to a_0>0\) at a central bolt.

These are ordinary mathematical arguments but should remain visible as unformalized
if this model theorem is later included in a proof package.

## 6. What this contributes to Yau-26

This closes a concrete nonabelian positive-collapse adversary: ungraded Heisenberg
collapse cannot persist in the simplest closed diagonal cohomogeneity-one setting.
Together with Step 6 and Step 24, the positive-collapse picture now separates three
mechanisms:

- four-dimensional constant-length free-circle collapse over a 3-base is obstructed;
- higher-dimensional constant-length circle collapse exists but is Einstein-compatible;
- four-dimensional diagonal \(H_3\) nonabelian collapse is obstructed in the positive
  branch but has a negative complex-hyperbolic local witness.

The all-dimensional Yau-26 proposition remains open.  The next uncontrolled case is
not this diagonal \(H_3\) model but twist-active regular infranil submersions and
singular/fixed strata, especially the already-developed toric fixed-strata \(T^2\)
family.  A future all-dimensional theorem must carry twist, mean-curvature, and
stratum flux terms rather than extrapolating this codimension-one result.

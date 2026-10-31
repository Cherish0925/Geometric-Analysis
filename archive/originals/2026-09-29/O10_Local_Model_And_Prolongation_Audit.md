# O10: the proposed local bulk does not exist; what the local obstruction actually uses

2026-09-30 (Asia/Shanghai). A targeted check of the unrestricted-endpoint construction and of a possible shorter positive-chirality proof.

## 1. The necessary correction to a gluing ansatz

There is no smooth four-dimensional local model which is simultaneously
\[
\operatorname{Ric}=-g,\qquad W^+=0,\qquad
d\omega=0,\quad |\omega|^2=2,
\]
with the orientation defined by \(\omega\). Thus a construction cannot start from a non-Kähler negative ASD Einstein almost-Kähler bulk and repair only its boundary.

This is the local result in John Armstrong's thesis, *Almost-Kähler Geometry*, Section 3.3.3, especially Theorem 3.3.5 (printed pp.70–72; PDF pp.82–84):

https://johnarmstrongmaths.com/publications/resources/thesis.pdf

The theorem forces the almost-Kähler structure to be Kähler in the ASD Einstein case. A Kähler surface satisfies \(|W^+|^2=s^2/24\), so ASD forces scalar curvature zero, contradicting \(s=-4\). No compactness hypothesis is needed for that local argument.

The original manuscript already cites this local obstruction in its controlled-geometry endpoint proofs. The present check corrects a possible proposed construction; it is not a new endpoint theorem.

## 2. The actual local hyperbolic cores are different objects

The manuscript constructs actual weight-two Seiberg–Witten fields on shrinking balls in real hyperbolic four-space. They solve the local gauge equation with \(\operatorname{Ric}=-g\), \(W^\pm=0\), and have nontrivial torsion index. They do **not** give a constant-length closed compatible two-form on an open set. In particular, they are not exact zero-end bulk solutions.

Their small local integrated defects are obtained by shrinking the entire domain. Extending many such cores to a closed zero-end requires a nonparallel exterior carrying
\[
\frac1V\int|\nabla_A\Phi|^2\to\frac49,
\qquad
\frac{\|H_A^+\|_2^2}{V}\to\frac89,
\qquad
\frac{\|H_A^-\|_2^2}{V}\to\frac29.
\]
These conditions are already recorded in the manuscript's `actual-core-fit`, subsection 4.1. The cores' freely chosen local boundary traces do not solve the exterior matching problem. Attaching Ricci-flat ALE pieces can add opposite-chirality curvature, but supplies none of this missing volume-scale actual field.

Therefore the proposed exact-bulk gluing route has no valid starting block. A genuine counterexample would have to retain degeneration or oscillation on essentially every region where one might otherwise pass to a regular positive-volume limit. This does not prove such a construction impossible, but it is materially different from ordinary desingularization of a known endpoint bulk.

## 3. The classical finite prolongation has a genuine higher-derivative step

For comparison with our variables, the classical proof first fixes the original torsion magnitude by the scalar and ASD assumptions. It then reduces its first derivative to a single complex coefficient. A second Ricci identity constrains this coefficient and the opposite curvature; an opposite-orientation Bianchi argument supplies the next compatibility, followed by a line-weight curvature contradiction. These are not first-jet algebra alone.

Indeed Armstrong explicitly exhibits algebraic two-jet solutions to the compatible almost-Kähler equations on hyperbolic space before making the higher prolongation. That rules out replacing the proof by a pointwise inequality involving only the original controlled curvature and its first spinor derivative. The original manuscript's formal first-jet freedom has the same warning: satisfying a low-order jet relation does not ensure prolongation to an actual solution on an open set.

The project's fifth-line positive-potential method is a useful weak reformulation of later compatibility. Its remaining unrestricted problem is passing those compatibility equations through concentration, not finding an exact forbidden local bulk that the classical theorem overlooked.

## 4. A seemingly promising first-order shortcut and its cancellation

The small projection \(N_v=(\nabla v)^{1,0}_{J_+}\) is elliptic as a real principal symbol. A Weitzenböck formula for \(N_v^*N_v\) contracts curvature with the positive form \(\omega_+\), hence uses the \(F_E^+\) block and does not directly contain \(W^-\). This looks like a possible replacement for the full negative-spinor Hessian estimate.

However, its determinant-curvature contraction on the calibrated endpoint is precisely the zero-order term corresponding to
\[
\nabla^*\nabla v=2v.
\]
It is not an additional positive-potential equation. Testing the projected identity with \(f(|v|^2)v\) reproduces the radial terms in the existing amplitude equation; those terms do not become a second independent coercive quantity. In the ideal reduction, comparison recovers the already known relation
\[
\frac{3\rho}{2}=1+\frac{3m}{2\rho^3},
\]
which gives \(m=128/81\) at \(\rho=4/3\), rather than a new bound for \(dm\). The manuscript's `phase-curvature`, subsection 2, already contains this cancellation.

Consequently, neither the ellipticity of \(N\) nor its controlled curvature contraction alone supplies the missing global Hessian or mass-gradient estimate. A useful new argument must retain further nonintegrability information in a test that does not reintroduce the uncontrolled negative curvature, or handle the concentration by another mechanism. No such complete argument is claimed here.

## Status

This note rules out an invalid proposed gluing seed and checks why a first-order projected Weitzenböck shortcut does not close the endpoint. It does not supply an actual closed counterexample, a density-free gap, or a new sharp constant. These failed routes should not be restarted under different names.

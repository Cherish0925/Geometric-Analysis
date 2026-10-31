# Round 19: testing constructions on obstructed smooth topologies

22 September 2026. Baseline: Round 18, local commit c10d3eb.

The question tested was whether an existing pointwise near-Einstein
construction could be placed on a smooth four-manifold with a proof
excluding every Einstein metric. The rigidity line independently tested
whether actual-monopole classes could supply that connection.
No Yau26 branch is completed in this round.

We use \(\delta_\sigma(g)=\|\operatorname{Ric}^{\sharp}_g-\sigma I\|_\infty\).
The relative defect at normalization \(\operatorname{Ric}=-3g\) is
\(\|\operatorname{Ric}^{\sharp}+3I\|_\infty/3=\delta_-(3g)\).
The Einstein output may have any sign and need not resemble the input.

## 1. Growing and rotating a specified spherical throat does not repair it

The manifolds \(M_j=N_j\#(S^1\times S^3)\), for finite hyperbolic covers
\(N_j\), have the all-sign obstruction proved in
[Round 18](round18_integral_limits.md). Its fixed-piece metrics have
vanishing average defect but a fixed nonzero maximum defect.

The new result tests an actual proposed replacement:
\[
 g=dt^2+G_{ij}(t)\sigma_i\sigma_j,\qquad
 G(0)=\operatorname{diag}(A^2(4+A^2),A^2,A^2),\qquad G'(0)=0,
\]
with standard left-invariant \(SU(2)\) forms and an arbitrary positive
symmetric matrix \(G(t)\), including rotating axes. For every \(A>0\),
\[
 \delta_-(g)\le\tfrac12\quad\Longrightarrow\quad L<69/8
\]
for a positive-definite continuation on \([0,L)\). The long radius
increases and the short radii decrease: no round interface is reached.
For \(A\le1\), the larger error allowance \(\delta_-\le1\) gives
\(L<11A/5\).

The mixed Ricci equation bounds harmful rotations uniformly even as
\(A\to\infty\). The tangential equation preserves a contracting
short-plane cone; the normal equation yields finite lifetime.
The proof retains the indefinite rotation term and permits short-axis
eigenvalue crossings. Increasing the waist size does not evade it.

[Full proof](round19_surgery.md). This treats the stated homogeneous
initial family, not arbitrary initial shape operators or inhomogeneous
surgery. The old fixed-radius obstruction and necessary cover-size
growth were rediscovered during exploration and are not new results.

## 2. Additional monopole classes cannot bridge the critical ratios here

Put \(H_j=\chi(N_j)\), \(T_j=2\chi(M_j)+3\tau(M_j)=2H_j-4\).
A positive uniform projection budget \(A_j\) requires that every metric
admit an actual monopole class \(c_g\) with \((c_g^+)^2\ge A_j\).
The class may depend on the metric. A simultaneous test on the
fixed-piece metric gives
\[
 A_j\le A_{\rm met}(M_j)\le\tfrac83H_j+c_q,\qquad
 \liminf_{j\to\infty}\frac{T_j}{A_j}\ge\tfrac34,
 \qquad A_{\rm met}(M)=\inf_g\max_{c\ {\rm actual}}(c_g^+)^2.
\]
The constant \(c_q\) is the fixed replacement's contribution to
\(\int(-s+\sqrt6|W^+|)^2/(72\pi^2)\).
This includes unknown classes without assuming surjectivity of the
metric period map or a bound on their negative squares.

Thus discovering more ordinary monopole classes cannot place these
families asymptotically at the integral theorem's critical \(2/3\) ratio.
This does not prohibit a different obstruction or a stronger theorem.

[Proof and global comparisons](round19_global_gap.md). The note keeps
relative volume excess and normalized Weyl energy in the Ricci-box
inequality; an absolute energy quantum does not give an extensive cost
as \(H_j\to\infty\).

Section 4 also checks a tempting literature shortcut: the literal
uniform-in-degree wording of BBCG Theorem 1.6 conflicts with
Farrell--Jones examples. In dimension eight their sectional pinching
and the Euler polynomial force normalized volume to one on exotic
smooth covers. The full argument is recorded, and that shortcut is
not used. This does not construct a four-dimensional counterexample
or exclude Einstein metrics on the eight-dimensional examples.

## 3. Positive fillings must respect the marked cone

Replacing the two independently marked \(A_1\) cores by same-chirality
higher ADE cores does not give a legal marked construction.
Orientation reversal exchanges the two quaternionic factors of
\(SO(4)\); a nontrivial subgroup of one factor has such an orthogonal
normalizer only for \(\Gamma=\{\pm I\}\).
For \(A_2\), its boundary linking form forbids even the proposed
oriented smooth gluing.

More generally, compatible Ricci-flat ALE fillings of a positive
Einstein orbifold normalized by \(\operatorname{Ric}=g\) obey
\[
 2\chi(M)\pm3\tau(M)\ge
 \operatorname{Vol}(\mathcal O)/(6\pi^2)>0.
\]
The boundary corrections are included. ADE rank cannot create a
Hitchin--Thorpe obstruction under these hypotheses.

A second test uses published self-dual gluing on the actual
no-Einstein topology \(4\mathbb{CP}^2\). Every metric there satisfies
\[
 \delta_+(g)>\tfrac12,\qquad \delta_-(g)>\tfrac12.
\]
The endpoint would create a line field, contradicting its Euler
characteristic. This applies the existing Hitchin--Thorpe mechanism.
Scalar-flat cores cannot substitute for Ricci-flat cores: their
nonzero Ricci endomorphism diverges under the shrinking-core scaling.

[Proofs and exact published construction](round19_positive_bridge.md).
No all-sign nonexistence theorem is obtained for compatible ADE
doubles or \(\mathbb{CP}^2\#\mathbb{CP}^2\).

## Consequence and verification

There is a new continuation theorem for an enlarged homogeneous class
and an actual-monopole budget comparison. The positive-side arguments
settle two explicit attempted connections to known obstructions;
several ingredients are classical applications, not new discoveries.
No field-first novelty claim is made.

The known no-Einstein hyperbolic surgery types still lack pointwise
approximations. Compatible positive fillings still lack all-sign
Einstein nonexistence. The notes establish why these particular
connections fail, not that every possible connection fails.
Another rotation or radius adjustment within the excluded initial
family is not a route to the missing input.

The three checkers passed 12 exact finite check groups.
[Verification record](round19_verification.md). Continuation,
topology, and cited geometric results have their separate proofs;
finite calculations are not their certification.

Only new Round 19 files were added in an isolated local worktree.
Installed Skills, inherited notes, live services, Sessions, and
model settings were not changed.

# Positive spherical fillings: two concrete obstruction bridges that fail

## 1. Result and scope

The existing marked A1 construction does not acquire an all-sign Einstein
obstruction by replacing its two independently oriented Eguchi--Hanson
cores with higher ADE cores. The missing freedom is a genuine end-marking
obstruction: a nontrivial ADE flat cone admits an orientation-reversing
isometry precisely in type A1. Thus the proposed same-chirality A2 double,
whose formal characteristic numbers reach the Hitchin--Thorpe boundary,
is not an allowed filling of the spherical suspension. In the A2 case
even an orientation-reversing boundary diffeomorphism is impossible.

There is also a published, actual all-sign non-Einstein object nearby in
the literature: self-dual orbifold gluing produces metrics on
\(4\mathbb {CP}^2\). It cannot be an input for the present problem:
every smooth metric on this manifold has
\[
 \delta_+(g)>\tfrac12,\qquad \delta_-(g)>\tfrac12.             \tag{1}
\]
This excludes the specific proposal to substitute its self-dual or
scalar-flat ALE construction for the Ricci-flat log-Weyl construction.
It is a positive defect bound on an actual smooth object, not a
failure to find a correction.

The compatible positive ADE doubles retain no proved all-sign Einstein
obstruction here. Neither this note nor the unchanged
[Round 18](round18_positive.md) proves Einstein nonexistence on
\(\mathbb {CP}^2\#\mathbb {CP}^2\). The negative Davis resolutions of
[Round 7](round7_topology.md) have different input metrics and topology;
their restrictions cannot be transferred to these positive objects.

## 2. The exact construction hypothesis that prevents a chirality flip

Let \(\Gamma\subset\operatorname{Sp}(1)_L\subset SO(4)\) be a
nontrivial finite subgroup acting on \(\mathbb H\) by left multiplication.
The left/right convention may be interchanged. The relevant fact is that
the subgroup lies in one of the two quaternionic factors.

**Lemma 1.** There exists \(A\in O(4)\) with \(\det A=-1\) and
\(A\Gamma A^{-1}=\Gamma\) if and only if \(\Gamma=\{\pm I\}\).

**Proof.** Let \(C(q)=\bar q\). It has determinant \(-1\), and
\[
 C L_a C=R_{\bar a},\qquad
 SO(4)=\{L_aR_b:a,b\in\operatorname{Sp}(1)\}.
\]
Consequently every orientation-reversing orthogonal map exchanges the
left and right factors under conjugation. If it normalizes \(\Gamma\),
then
\[
 \Gamma\subset\operatorname{Sp}(1)_L
             \cap\operatorname{Sp}(1)_R=\{\pm I\}.
\]
For the intersection identity, \(L_a=R_b\) first gives \(a=b\) by
evaluation at 1, and then \(a\) commutes with every quaternion, so
\(a=\pm1\). Conversely the central group \(\{\pm I\}\) is
normalized by \(C\). This proves the lemma.

The quaternionic representation and the exchange of factors under
orientation reversal are also recorded in
[Lock--Viaclovsky, Section 2.1, equations (2.1)--(2.3)](https://arxiv.org/pdf/1501.03234).
The argument above proves the specific normalizer assertion directly.

An isometry of the round link \(S^3/\Gamma\) lifts to an isometry of
\(S^3\), hence to an orthogonal normalizer. Lemma 1 therefore concerns
the metric asymptotic marking, not just the abstract name of a finite
group. The conjugate group in the other quaternionic factor gives the
oppositely oriented cone; it does not restore an independent filling
choice at a fixed oriented node.

The inherited ADE analysis in
[the cumulative construction manuscript, Chapter 2](skill/research/20260912.tex)
requires an actual smooth Kronheimer core with fixed collinear periods
away from root hyperplanes, the complete kernel compatibility, the
quadratic Ricci-source extension, controlled remainder, and a matching
oriented representation at infinity. Its displayed estimate is
\(\delta_\sigma\le C(|\log a|^{-1}+a^{1/4})\) for fixed data.
It explicitly does not grant arbitrary A1-style chirality choices to
general ADE links. The topological obstruction below does not depend
on independently validating that analytic extension.

## 3. The A2 attempted counterexample, including the boundary obstruction

Suspend \(\Gamma=\mathbb Z_3\subset SU(2)\), acting as
\((z_1,z_2)\mapsto(\zeta z_1,\zeta^{-1}z_2)\), to obtain
\(S^4/\Gamma\). Its regular part is
\((S^3/\Gamma)\times(-1,1)\). Let \(W\) be the negative A2 plumbing,
with intersection matrix
\[
 Q=\begin{pmatrix}-2&1\\1&-2\end{pmatrix},\qquad
 \chi(W)=3,\quad\tau(W)=-2.                              \tag{2}
\]
Reflection-compatible markings yield the genuine oriented double
\[
 D(W)=W\cup_{\mathrm{id}}(-W).
\]
This is the standard smooth \(\#_2(S^2\times S^2)\) from the inherited
torus-action identification. It has \((\chi,\tau)=(6,0)\).

If one formally replaces \(-W\) by another negatively oriented copy
of \(W\), the requested characteristic numbers become \((6,-4)\),
which satisfy \(2\chi=3|\tau|\). For a general rank-\(r\) ADE core
the same formal calculation gives
\[
 \chi=2+2r,\quad |\tau|=2r,\quad
 2\chi-3|\tau|=4-2r.                                    \tag{3}
\]
Thus A2 is already the equality case, and ranks \(r\ge3\) would
violate Hitchin--Thorpe. These numbers do not define an actual marked
smooth filling. Lemma 1 prevents its asymptotic cone identification.

For A2 there is a stronger, purely topological obstruction. The boundary
has \(H_1\cong\mathbb Z_3\), with nonsingular linking form
\(\lambda(u,u)=\pm1/3\) modulo \(\mathbb Z\), as follows by inverting
\(Q\). An orientation-reversing diffeomorphism would induce
\(u\mapsto ku\), \(k\in\{1,2\}\), and require
\[
                  k^2\equiv-1\pmod3.                   \tag{4}
\]
Both possible squares are 1, so no such diffeomorphism exists. An
oriented gluing of two equally oriented copies of \(W\) requires
precisely such a map between their equally oriented boundaries.
Therefore the A2 same-chirality double cannot even be assembled as
the proposed oriented smooth manifold.

For D and E groups, the reflection-compatible construction still gives
the actual double of the corresponding negative plumbing, with
\(\pi_1=1\), \(\chi=2+2r\), \(\tau=0\), and a spin structure.
These statements follow from van Kampen, signature additivity and
\(D(W)=\partial(W\times I)\). No diffeomorphism classification of
those doubles is needed or asserted here. Independent orientation
flips are excluded by Lemma 1. This statement does not classify
all arbitrary boundary diffeomorphisms or other non-Kronheimer fillings.

## 4. Every genuinely compatible Ricci-flat ALE filling preserves strict HT

Here is a general check beyond the A1 formula of Round 17. Let
\((\mathcal O,g_0)\) be a closed oriented Einstein four-orbifold with
isolated singularities and \(\operatorname{Ric}=g_0\). Resolve it by
smooth Ricci-flat ALE spaces \(X_i\) with actual compatible oriented
cone markings. Define the modified characteristic numbers by their
curvature integrals. On each ALE space,
\[
 \widetilde\chi(X_i)=\frac1{8\pi^2}
      \int_{X_i}(|W^+|^2+|W^-|^2),\qquad
 \widetilde\tau(X_i)=\frac1{12\pi^2}
      \int_{X_i}(|W^+|^2-|W^-|^2).                       \tag{5}
\]
The corresponding orbifold definition includes \(s^2/24\) in
\(8\pi^2\widetilde\chi\). The boundary corrections give
\[
 \chi(M)=\widetilde\chi(\mathcal O)+\sum_i\widetilde\chi(X_i),
 \quad
 \tau(M)=\widetilde\tau(\mathcal O)+\sum_i\widetilde\tau(X_i).
                                                                    \tag{6}
\]
This is the modified-invariant additivity in
[Ozuch, Section 7.1, equations (118)--(119) and the following gluing identities](https://arxiv.org/pdf/1909.12960).
It is a topological curvature identity; no exact Einstein metric on
\(M\) is assumed. Smooth compatibility of the links is essential.

Combining (5)--(6), for either sign,
\[
\begin{split}
 2\chi(M)\pm3\tau(M)
 &=\frac1{4\pi^2}\int_{\mathcal O}
            \left(\frac23+2|W^\pm|^2\right)
   +\sum_i\frac1{2\pi^2}\int_{X_i}|W^\pm|^2\\
 &\ge\frac{\operatorname{Vol}(\mathcal O,g_0)}{6\pi^2}>0.
                                                               \tag{7}
\end{split}
\]
Thus replacing A1 cores by any available compatible Ricci-flat ALE
cores cannot produce an HT obstruction. This is not specific to
hyperkähler cores and does not assert that arbitrary ALE cores admit
the required Ricci-source correction.

For the rank-\(r\) ADE double, write \(d=|\Gamma|\). Each core has
\(\widetilde\chi=r+1-1/d\), one Weyl energy
\(8\pi^2(r+1-1/d)\), and zero energy in the other half. The spherical
bulk has \(\widetilde\chi=2/d\), \(\widetilde\tau=0\), and normalized
volume \(24\pi^2/d\). Opposite core chiralities give exactly
\[
 2\chi\pm3\tau=\frac4d+4(r+1-1/d)=4(r+1),                \tag{8}
\]
in agreement with its actual topology. For reference, in the eta
convention of Lock--Viaclovsky equation (3.5),
\(\widetilde\tau=\tau-\eta\) and the negative ADE core has
\(\eta=(2-r-2/d)/3\). It is zero only for A1. Reversing the eta
convention reverses this displayed eta sign, with no change to (5)--(8).

For varying groups or orbifolds, the positive lower bound in (7) may
tend to zero. Nevertheless each individual resolved topology still
satisfies strict HT. No uniform volume bound, topological finiteness,
or all-sign Einstein existence follows from this statement.

## 5. A published all-sign non-Einstein topology cannot provide the input

Lock--Viaclovsky construct degenerating self-dual metrics on
\(\ell\mathbb {CP}^2\); their first family with \((m,n)=(1,2)\) has
\(\ell=4\). See
[Corollary 1.10 and Remark 1.11](https://arxiv.org/pdf/1501.03234).
This is an actual smooth topology and an actual gluing theorem. The
following two short arguments settle its relevance to this task.

**Proposition 2.** For every \(k\ge4\), the standard smooth manifold
\(M_k=\#_k\mathbb {CP}^2\) has no Einstein metric of any sign. Every
smooth metric on it satisfies (1).

**All-sign nonexistence.** Its characteristic numbers are
\(\chi=k+2\), \(\tau=k\), hence \(2\chi-3\tau=4-k\).
For an Einstein metric Chern--Weil gives
\[
 4\pi^2(4-k)=\int_{M_k}\left(2|W^-|^2+\frac{s^2}{24}\right).
                                                               \tag{9}
\]
For \(k>4\) this is impossible. If \(k=4\), it forces
\(s=0\) and \(W^-=0\). The induced Levi-Civita connection on
\(\Lambda^-\) is then flat: both \(W^-+sI/12\) and the off-diagonal
trace-free Ricci block vanish. Simple connectivity gives three global
parallel anti-self-dual two-forms, contradicting \(b_-(M_4)=0\).
No assumption about the sign, symmetry or conformal class was imposed.

**Exclusion of the near-Einstein input, including the endpoint.**
Suppose \(\delta_\sigma(g)\le1/2\), \(\sigma\in\{+1,-1\}\).
The eigenvalues \(r_i\) of \(\sigma\operatorname{Ric}^{\sharp}\)
are in \([1/2,3/2]\). Set \(a=\min r_i\), \(S=\sum r_i\),
\(Q=\sum r_i^2\). Since \(a\le r_i\le3a\),
\[
 Q\le4aS-12a^2,
 \quad
 F:=\frac{s^2}{24}-\frac{|\operatorname{Ric}^{\circ}|^2}{2}
   =\frac{S^2-3Q}{6}\ge\frac{(S-6a)^2}{6}\ge0.           \tag{10}
\]
Thus \(4\pi^2(4-k)=\int(2|W^-|^2+F)\ge0\), excluding \(k>4\).
For \(k=4\), equality holds everywhere. Equality in (10) forces
the four eigenvalues to be \((3a,a,a,a)\), up to permutation.
Their simple eigenvalue defines a smooth real line subbundle of
\(TM_4\). As \(M_4\) is simply connected this line bundle is
trivial, giving a nowhere-zero vector field. This contradicts
\(\chi(M_4)=6\), proving (1).

This is a specialization of the inherited strict HT endpoint, with
a shorter equality proof on this simply connected object. The metricwise
strict inequality implies \(e_\sigma(M_k)\ge1/2\); it does not imply
that the infimum is strictly greater than \(1/2\).

The published self-dual examples therefore supply genuine all-sign
non-Einstein manifolds but quantitatively fail the input requirement.
Their scalar-flat condition controls only the Ricci trace.
If a fixed core \(k\) has \(\operatorname{Ric}_k\ne0\), rescaling it
gives
\[
 (a^2k)^{-1}\operatorname{Ric}_{a^2k}
             =a^{-2}k^{-1}\operatorname{Ric}_k,             \tag{11}
\]
which diverges at every point with nonzero Ricci endomorphism.
An \(O(a^2)\) relative correction with bounded core derivatives
cannot cancel that leading term. This is why replacing a Ricci-flat
core by a scalar-flat one does not preserve the construction theorem.

There is a further source-level exclusion of that substitution:
[Lock--Viaclovsky, Theorem 1.5](https://arxiv.org/pdf/1501.03234)
proves that a minimal resolution of a \(U(2)\) quotient singularity,
or an iterated blow-up of it, carries a Ricci-flat ALE metric only
when the group is contained in \(SU(2)\); the metric is then
hyperkähler. For example the \(\mathcal O(-p)\) resolution of
\(1/p(1,1)\), \(p>2\), cannot be the desired Ricci-flat core.
This theorem does not cover different fillings such as Wahl rational
balls. Actual compatible Ricci-flat fillings of that kind remain
subject to the budget (7).

## 6. What is settled and what remains

Two concrete connections to known all-sign obstructions are closed:
same-chirality higher-ADE suspension filling fails its marked end
condition (for A2, even its boundary gluing), and the published
\(4\mathbb {CP}^2\) self-dual construction has the uniform positive
defect bound (1). Increasing the ADE rank does not evade either issue.
The Ricci-flat ALE budget explains the same phenomenon for all
compatible fillings, without claiming that HT is the only possible
Einstein obstruction.

A positive near-Einstein sequence also has positive Ricci and scalar
curvature once its defect is below 1. Myers then requires finite
fundamental group, and on a spin four-manifold the Lichnerowicz
identity forces \(\widehat A=-\tau/8=0\). A nonzero spin index
would disprove that input, not distinguish it from a hypothetical
Einstein output. The compatible ADE doubles above have \(\tau=0\).

No topology carrying both the required positive near-Einstein input
and a proved all-sign Einstein obstruction is obtained in this note.
The independent normalizer proof and the A2 linking calculation
identify a specific blocked construction; they are not an exhaustive
classification of possible positive-branch counterexamples. The
inherited fixed-type constructions and varying-rank constructions
retain their previously stated analytic hypotheses and status.

`python3 round19_positive_bridge_check.py` verifies the quaternionic
factor calculations, the A2 linking arithmetic, the ADE energy and
characteristic-number budgets, and the endpoint eigenvalue patterns.
It checks finite algebra, not the analytic gluing theorem or the
external topological and curvature identities.

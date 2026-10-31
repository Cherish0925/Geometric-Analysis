# Local complex geometry and Weyl spectral defects on the definite filling

## 1. The all-output statement

Let
\[
 M=\mathbb {CP}^{2}\#\mathbb {CP}^{2},\qquad
 (\chi,\tau,b_+,b_-)=(4,2,2,0),                         \tag{1}
\]
with the standard smooth structure and the indicated orientation.
The actual marked A1 construction gives positive near-Einstein inputs
on this manifold. The previous round bounded the volume of every
normalized positive Einstein output. Here the target is different:
local geometry of **every** hypothetical Einstein output, with no
prescribed sign, symmetry or relation to the input.

Write \(\operatorname {Ric}_h=\lambda h\), and regard \(W^\pm\) as
trace-free self-adjoint endomorphisms of \(\Lambda^\pm\). Define
\[
 \mathscr D_\pm
 =\frac12\bigl(\operatorname {tr}((W^\pm)^2)\bigr)^3
       -27(\det W^\pm)^2,\qquad Z_\pm=\{\mathscr D_\pm=0\}.
                                                                  \tag{2}
\]
The norm here is the endomorphism Hilbert–Schmidt norm, not the
four-index tensor norm. If the three eigenvalues are \(a,b,c\),
then \(\mathscr D=(a-b)^2(b-c)^2(c-a)^2\). In particular
\(\mathscr D\ge0\), and its zero set is precisely the repeated-spectrum
locus, including the zeros of the Weyl block.

**Theorem 1.** Every Einstein metric on (1) has the following properties.

1. \(W^+\) has three distinct eigenvalues on an open dense set.
   No nonempty open subset admits an integrable, positive-oriented,
   \(h\)-orthogonal complex structure.
2. If \(W^-\not\equiv0\), the same statements hold for \(W^-\)
   and the opposite orientation. If \(\lambda\ge0\), this hypothesis
   is automatic.
3. The remaining alternative is
   \(\lambda<0\) and \(W^-\equiv0\): a globally self-dual negative
   Einstein metric. This theorem does not exclude that alternative.
4. There is no locally reducible nonempty open subset, for any sign
   of \(\lambda\).
5. No nonempty open subset is conformal to a Kähler metric, in
   either orientation, for any sign of \(\lambda\). In particular
   this assertion has no negative self-dual exception.

For either nontrivial discriminant in this theorem, \(Z_\pm\) is a
proper real-analytic subset with empty interior. Nevertheless it
cannot be absent, isolated, or merely a union of curves:

**Theorem 2.** Each \(Z_\pm\) intersects every smoothly embedded sphere
whose self-intersection is odd. In the proper real-analytic cases,
\[
                         2\le\dim_{\mathbb R}Z_\pm\le3.           \tag{3}
\]
The dimension is the maximum stratum dimension, not a claim that
\(Z_\pm\) is a smooth surface or has a canonical homology class.

These statements combine established Einstein structure theorems
with the topology of this concrete filling. They are not a new
general classification, and do not decide whether an Einstein
metric exists. They do exclude an entire class of exact local
ansatzes, rather than only a chosen gluing family.

## 2. The topology forbids a global eigenline, in either orientation

The manifold is simply connected. An almost complex structure on
an oriented closed four-manifold satisfies
\[
 c_1^2=2\chi+3\tau,\qquad c_2=\chi,\qquad
 \frac{c_1^2+c_2}{12}=\frac{\chi+\tau}{4}\in\mathbb Z.              \tag{4}
\]
The last integer is the index of its canonical Spin\(^c\) Dirac
operator; integrability is not needed. The right side is \(3/2\)
in the orientation of (1), and \(1/2\) in the reverse orientation.
Thus neither orientation admits an almost complex structure.

A smooth real line subbundle of \(\Lambda^+\), or of \(\Lambda^-\),
would be trivial because \(H^1(M;\mathbb Z_2)=0\). A nowhere-zero
section, normalized to length \(\sqrt2\), is the fundamental form
of an orthogonal almost complex structure in the corresponding
orientation. Therefore neither Weyl bundle admits a line subbundle.
This argument does not assume that an eigenform is closed.

## 3. Propagating a local Hermitian condition without losing Weyl zeros

Two classical inputs close the globalization step.

* An Einstein metric is real analytic in harmonic coordinates:
  [DeTurck–Kazdan, Theorem 5.2](https://www.numdam.org/article/ASENS_1981_4_14_3_249_0.pdf).
  Consequently (2) is analytic. Vanishing on a nonempty open set
  propagates throughout a connected manifold.
* For an oriented Einstein four-manifold with a Weyl half everywhere
  of at most two distinct eigenvalues, that half either vanishes
  identically or is nowhere zero and has exactly two distinct
  eigenvalues at every point. The latter has one simple eigenline.
  This is [Derdziński, Proposition 5(iv), pp. 420–422](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf).
  The equivalence with local orthogonal integrable complex structures
  is stated in [Apostolov–Gauduchon, Proposition 1, pp. 209–210](https://www.numdam.org/item/ASNSP_2002_5_1_1_203_0.pdf).

Here is the resulting general lemma. Suppose \(H^1(N;\mathbb Z_2)=0\)
and the chosen orientation of \(N\) admits no almost complex
structure. For an Einstein metric on connected \(N\), either the
chosen Weyl half vanishes identically, or its discriminant is not
identically zero and no open set is Hermitian in that orientation.
Indeed, identically zero discriminant and a nonzero Weyl half would
give a globally smooth simple eigenline by the second input, and
hence the forbidden almost complex structure. A local Hermitian
structure forces zero discriminant on that open set and therefore
everywhere, giving the same contradiction.

The nowhere-zero assertion in Derdziński's proposition is essential.
Analytic continuation of the discriminant alone would not justify
extending an eigenline across points where the entire Weyl half
vanishes. We use the proposition to remove those points, not a
purported extension theorem for a singular eigenbundle.

Apply the lemma to both orientations of (1). The signature formula
gives
\[
 \int_M\bigl(|W^+|^2-|W^-|^2\bigr)=24\pi^2>0,                    \tag{5}
\]
so \(W^+\not\equiv0\). This proves the first assertion and the
conditional second assertion of Theorem 1.

If \(\lambda>0\), \(W^-\equiv0\) is excluded by the compact positive
self-dual Einstein classification: the simply connected possibilities
are the round sphere and the Fubini–Study projective plane, not (1).
The classification is due to
[Hitchin, Kählerian Twistor Spaces](https://doi.org/10.1112/plms/s3-43.1.133);
its exact use on this object is already part of
[Round 17](round17_positive.md), via Gursky–LeBrun's proof of Theorem A.

If \(\lambda=0\) and \(W^-\equiv0\), the induced Levi-Civita
connection on \(\Lambda^-\) is flat. Its curvature is determined
by \(W^-+sI/12\) and the trace-free Ricci block, both zero here.
On the simply connected manifold this connection has three
independent global parallel sections. They are harmonic anti-self-dual
two-forms, contradicting \(b_-=0\). This uses half-flatness;
it does not assume that an arbitrary Ricci-flat four-metric has
special holonomy.

Finally, a locally reducible Einstein four-metric has either a
two-by-two product splitting or a one-dimensional factor. The first
is locally Kähler for either orientation, by choosing the complex
orientations of its surface factors, contradicting assertion 1.
The second forces \(\lambda=0\); the remaining Ricci-flat factors
have dimension at most three and are flat. That too is locally
Kähler. This proves assertion 4.

For assertion 5, assertions 1–2 already handle every case except
\(\lambda<0\), \(W^-\equiv0\), with the proposed Kähler structure
having negative orientation. Suppose on a connected open subset
\(h=\varphi^{-2}k\), where \(k\) is Kähler and \(\varphi>0\).
With \(\Delta_k=\operatorname{tr}_k\nabla_k^2\),
\[
 \operatorname{Ric}_h=\operatorname{Ric}_k
   +2\varphi^{-1}\nabla_k^2\varphi
   +\bigl(\varphi^{-1}\Delta_k\varphi
           -3\varphi^{-2}|d\varphi|_k^2\bigr)k.                  \tag{7}
\]
Since the two Ricci tensors and the metric terms in (7) are
\(J\)-invariant, \(\nabla_k^2\varphi\) is \(J\)-invariant.
Therefore \(K=J\nabla_k\varphi\) is Killing for \(k\). Moreover
\(K\varphi=0\), so it is Killing for \(h\) as well.

Any such local Killing field extends to the simply connected
analytic manifold by
[Nomizu's extension theorem](https://doi.org/10.2307/1970148);
its hypotheses and use on Einstein manifolds are also detailed in
[Round 12](round12_symmetry.md). On the closed manifold,
integration of the Killing equation and the Ricci commutator gives
the [Bochner identity](https://doi.org/10.1090/S0002-9904-1946-08647-4)
\[
 \int_M|\nabla K|^2=\lambda\int_M|K|^2.
\]
Because \(\lambda<0\), the extension is zero. Hence \(\varphi\)
is constant on the original open subset and \(h\) is Kähler there.
But a Kähler four-metric has eigenvalues
\((s/6,-s/12,-s/12)\) in its complex-orientation Weyl block.
Here \(s=4\lambda\ne0\), contradicting \(W^-\equiv0\).
This completes Theorem 1. Notice the distinction: a local Hermitian
structure in the exceptional branch is not thereby locally
conformally Kähler.

## 4. Why the degeneracy set must meet the odd spheres

This step needs no Einstein equation. Let \(S\subset M\) be an
embedded oriented sphere of odd self-intersection. Along \(S\),
split \(TM=TS\oplus\nu\) into its oriented tangent and normal
two-plane bundles. In an adapted oriented orthonormal frame,
\(\Lambda^\pm|_S\) has a trivial line generated by the sum or
difference of the two area forms. The complementary real two-plane
bundle transforms with angle equal to the sum or difference of the
tangent and normal rotation angles. Thus
\[
 \big\langle w_2(\Lambda^\pm|_S),[S]\big\rangle
  =\big\langle e(TS)\pm e(\nu),[S]\big\rangle\pmod2
  =2\pm S\cdot S=1\pmod2.                                      \tag{6}
\]
The sign assignment between the two complements is irrelevant modulo
two; (6) is also the restriction of \(w_2(\Lambda^\pm)=w_2(TM)\).

If \(S\cap Z_\pm=\varnothing\), the three ordered eigenvalues
are distinct everywhere on \(S\). Their smooth real eigenline
bundles split \(\Lambda^\pm|_S\). Every real line bundle on a
sphere is trivial, contradicting (6). This proves the intersection
claim, in particular for the standard projective-line spheres
representing either generator of \(H_2(M;\mathbb Z)\).

For an Einstein metric, a proper \(Z_\pm\) is real analytic and has
a locally finite smooth stratification; on the compact manifold it
can be taken finite. One may use the standard real-analytic
stratification theorem, or the restricted-analytic case of
[Nguyen–Trivedi–Trotman, Theorem 2.2](https://arxiv.org/pdf/1404.1218).
If its dimension were at most one, smooth transversality would
perturb a standard odd sphere to be transverse to all strata.
Since \(2+\dim S_\alpha<4\), every such intersection would be
empty. A sufficiently small perturbation preserves embeddedness
and the homology class, contradicting the first part. The upper
bound three follows because the analytic discriminant is not
identically zero. This proves (3).

In particular, the generic three-eigenvalue region and the forced
spectral defect set coexist. There is no contradiction between
Theorems 1 and 2. A repeated eigenvalue at an individual point does
not supply a Hermitian neighborhood.

## 5. Consequences for the positive A1 research object

The conclusions concern any exact output on the inherited marked
smooth manifold, not its chosen torus action. For positive or
Ricci-flat output, neither orientation permits even one Hermitian
open patch. For negative output, a positive-oriented patch is still
impossible; an oppositely oriented patch forces the metric to be
globally self-dual. Any exact product patch is excluded in all cases.

Consequently an exact construction based on Kähler, conformally
Kähler or product pieces cannot finish while retaining such a piece
unchanged on an open set, in either orientation and for any Einstein
sign. For a merely Hermitian piece, the stated negative self-dual
exception remains. This is stronger
than saying that the final metric cannot be globally Kähler.
It does not exclude a construction that perturbs every piece and
breaks the local complex structure. Such a perturbation may be
arbitrarily small; this note gives no lower bound on its size.
Likewise a smooth local limit of metrics with nonzero discriminant
may have identically zero discriminant. No compactness obstruction
follows just from the generic-spectrum conclusion.

The unchanged Yau26 endpoint is all-sign Einstein existence on (1).
For the inherited positive inputs, all-sign nonexistence on this
same smooth type would refute the positive branch. Theorem 1
restricts all possible outputs but does not supply that nonexistence.
Its remaining alternatives are generic-spectrum Einstein metrics
and the specified negative self-dual branch, not only Hermitian
metrics awaiting a classification.

## 6. Relation to prior project work and verification

The no-almost-complex observation was already recorded in Round 17.
The older cumulative manuscript, in its adapted-fibration discussion
around the label SUB:gram-zero-set, already uses analytic continuation
and the local Goldberg–Sachs condition on negative bundle candidates.
This note does not claim those mechanisms as discoveries. It supplies
the complete two-orientation, all-sign argument for the definite A1
filling, including the Weyl-zero alternative, and the explicit
odd-sphere restriction on its spectral defect loci.

The accompanying finite checker verifies the discriminant polynomial,
the two Weyl-bundle rotation representations, the odd-sphere parity,
the Todd-index obstruction, the signature normalization, and the
Hamiltonian Killing algebra in (7). These
are algebraic checks; real analyticity, the Einstein two-eigenvalue
theorem, Hitchin classification and transversality are used as the
mathematical inputs stated above.

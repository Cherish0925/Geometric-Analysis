---
retention_scope: session
part: 1
total_parts: 1
---

# Math 249B. Root systems for split classical groups

> Source: http://virtualmath1.stanford.edu/~conrad/249BW16Page/handouts/classicalgps.pdf
> Fetched: 2026-10-09 10:31
> Method: FULLTEXT_HTML_FIRECRAWL|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA

---

## Verified object metadata

```json
{
  "object_type": "web",
  "identifier": "",
  "identifiers": {},
  "identifier_aliases": {},
  "version": "",
  "published_at": "",
  "updated_at": "",
  "license": "",
  "language": "",
  "source": "serper",
  "source_url": "http://virtualmath1.stanford.edu/~conrad/249BW16Page/handouts/classicalgps.pdf",
  "metadata": {
    "provenance_urls": [
      "http://virtualmath1.stanford.edu/~conrad/249BW16Page/handouts/classicalgps.pdf"
    ],
    "search_origins": [
      {
        "source": "serper",
        "query": "root subsystems of D_n classification A D components signed graph roots plus minus e_i e_j"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

We know that the root groups are given by the copies of Ga corresponding to off-diagonal matrix entries, so Φ consists of the n2 −n characters ei −ej (i 6= j) ...

## Retrieved source content

Math 249B. Root systems for split classical groups

1. Introduction
The exceptional Lie groups were discovered by searching for groups which would realize the 5 exceptional reduced irreducible root systems. But the 4 infinite families of “classical” reduced irreducible root systems A<sub>n</sub> (*n ≥* 1), B<sub>n</sub> (*n ≥* 2), C<sub>n</sub> (*n ≥* 3), and D<sub>n</sub> (*n ≥* 4) arise from explicit split connected semisimple groups. In this handout, we work out the root systems for the split connected semisimple groups SL<sub>n+1</sub> (*n ≥* 1), SO<sub>2n+1</sub> (*n ≥* 2), Sp<sub>2n</sub> (*n ≥* 2), and SO<sub>2n</sub> (*n ≥* 3) over an arbitrary field *k*. This will yield the root system of type A<sub>n</sub>, B<sub>n</sub>, C<sub>n</sub>, and D<sub>n</sub> respectively. In the course of doing these calculations, we will determine:

(i) an explicit borus (*T,B*), (ii) the associated system of positive roots Φ(*B,T*) and its root basis ∆, (ii) the coroot associated to each (positive) root,
(iv) an explicit Weyl-invariant positive-definite symmetric bilinear form on X(*T*)<sub>Q</sub>. Our work will also *prove* that the special orthogonal and symplectic groups really are semisimple (granting that they are smooth and connected, as was proved in the previous course). Exercises 1.6.16 and 1.6.15 in the Luminy SGA3 notes provide an alternative (and in some respects more efficient/conceptual) approach to proving the reductivity and deter- mining the root systems for special orthogonal and symplectic groups.

2. Type A
Consider *G* = SL<sub>n+1</sub> with *n ≥* 1, and let *T* be the diagonal split maximal *k*-torus. We have seen Example 2.2 of the “Root datum” handout that *X* := X(*T*) is naturally identified with Z<sup>n+1</sup>*/*Z (quotient by the diagonally embedded Z), so *V* := *X<sub>Q</sub>* = Q<sup>n+1</sup>*/*Q *’* (Q<sup>n+1</sup>) Σ=0. We equip this final hyperplane inside Q<sup>n+1</sup> with the restriction of the standard inner product on Q<sup>n+1</sup>. Let *e₁,...,e<sub>n+1</sub>* denote the images in *X* of the standard basis of Z<sup>n+1</sup>. We know that the root groups are given by the copies of G<sub>a</sub> corresponding to off-diagonal matrix entries, so Φ consists of the *n² − n* characters *e<sub>i</sub> − e<sub>j</sub>* (*i 6*= *j*), sending a diagonal *t ∈ T* to *t<sub>i</sub>/t<sub>j</sub>*; these do not span *X* over Z (indeed, their span has index *n* + 1, corresponding to the fact that *ZG* = *µ<sub>n+1</sub>* has order *n* + 1). For *i < j*, the pair of opposite roots *±*(*e<sub>i</sub> − e<sub>j</sub>*) have associated root groups generating the SL₂ *⊂ G* supported in the matrix entries indexed by *i* and/or *j* (using 1’s elsewhere on the diagonal and 0’s everywhere else). For *i < j*, this latter description gives the coroot formula

(*e<sub>i</sub> − e<sub>j</sub>*) *∨* = *e<sup>∗</sup><sub>i</sub> − e<sup>∗</sup><sub>j</sub>*: G<sub>m</sub> *→ T*

carrying *y* to diag(1*,...,*1*,y,...,*1*/y,*1*,...,*1) where the only diagonal entries distinct from
1 are *y* in the *ii*-position and 1*/y* in the *jj*-position. These coroots span the lattice (Z<sup>n+1</sup>) Σ=0

naturally dual to *X*, affirming that *G* is simply connected. Using the coroot formula, the reflection *r<sub>e</sub>* *i* *−ej*on *V* = *X<sub>Q</sub>* (*defined* in terms of coroots) is easily verified to be the usual orthogonal reflection through *e<sub>i</sub> − e<sub>j</sub>* with respect to the chosen inner product on *V* (induced by the standard one on Q<sup>n+1</sup>). Hence, the inner product we are considering on *V* is invariant under all of these reflections, so invariant under the entire

Weyl group. Once we verify that Φ is irreducible we will therefore know that we have found the Weyl-invariant inner product that is unique up to a positive scaling factor. For *i < j* we have *e<sub>i</sub> − e<sub>j</sub>* = (*e<sub>i</sub> − e<sub>i+1</sub>*) + *···* + (*e<sub>j−1</sub> − e<sub>j</sub>*)*,*

so the set ∆ = *{a<sub>i</sub>* = *e<sub>i</sub> − e<sub>i+1</sub>}₁≤i≤n*of *n* positive roots generate the rest under repeated additions. We know that *G* is connected reductive with finite center, so it is semisimple, and its rank is *n*, so ∆ of size *n* must be a root basis. Under the chosen Weyl-invariant dot product we have *a<sub>i</sub> · a<sub>j</sub> 6*= 0 for *i < j* precisely when *j* = *i*+ 1, and all squared root lengths *a<sub>i</sub> · a<sub>i</sub>* have the same value (namely, 2). Thus, Dyn(Φ) is the connected A<sub>n</sub>-diagram (establishing that Φ is irreducible):

- *◦ ◦ ◦ ··· ◦* *a* 1*a*2*a*3*a*4*an*
Note in particular that

2 cos(∠(*a<sub>i</sub>,a<sub>i+1</sub>*)) = *〈a<sub>i</sub>,a* *∨* <sub>i+1</sub>*〉* = *−*1*,*

so the angle between *a<sub>i</sub>* and *a<sub>i+1</sub>* is 2*π/*3. For *n* = 2 this recovers the hexagonal picture for the root system A₂ equipped with its Weyl-invariant Euclidean structure that is unique up to scaling.

3. Type B
Fix *n ≥* 2. Let *V* = *k<sup>2n+1</sup>* with the non-degenerate quadratic form

*q* = *x₀x<sub>2n</sub>* + *···* + *x<sub>n−1</sub>x<sub>n+1</sub>* + *x²<sub>n</sub>* = (*x₀,...,x<sub>n−1</sub>*)*J*(*x<sub>n+1</sub>,...,x<sub>2n</sub>*)<sup>t</sup> + *x²<sub>n</sub>*

where *J* is the anti-diagonal *n × n* matrix with 1’s along the anti-diagonal. Denote by *{*e₀*,...,*e<sub>2n</sub>*}* the standard basis of *V*. The defect space *V* *⊥* vanishes if char(*k*) *6*= 2 and is the line *k*e<sub>n</sub> if char(*k*) = 2. A subspace *V <sup>′</sup> ⊂ V* is called *isotropic* if *q|<sub>V</sub> ′* = 0. Define *G* to be the affine *k*-group scheme SO<sub>2n+1</sub>:= SO(*q*) = O(*q*) *∩* SL(*V*). From the first course we know that this is smooth and connected with dimension *n*(2*n* + 1). We will prove below that it is semisimple with trivial center and has root system B<sub>n</sub>. This will entail some hard work, but with this experience under our belts the cases of types C and D will be smooth sailing. The split diagonal torus

## T = {diag(t₁,...,t<sub>n</sub>,1,t<sup>−1</sup><sub>n</sub>,...,t<sup>−</sup>1 1)}⊂ G

is easily verified (using weight space considerations for the standard representation on *k<sup>2n+1</sup>*) to satisfy *ZG*(*T*) = *T*, so *T* is a maximal torus. The choice of indexing of the variables appearing in *q* will ensure that an appropriate “upper triangular” subgroup will be a Borel subgroup containing *T*. To discover a Borel subgroup containing *T*, we briefly digress to discuss some related “flag varieties”. The isotropic subspace

## W<sub>std</sub>:= span(e₀,...,e<sub>n−1</sub>)

of dimension *n* is certainly maximal as such since *q* is non-degenerate and *q|<sub>ke</sub>n6*= 0 in characteristic 2. By similar reasons, every isotropic subspace of *V* has vanishing intersection with the defect space (a non-tautology only in characteristic 2). Let *Y* be the scheme (built from Grassmannians) representing the functor of pairs (*W,F*) consisting of a rank-*n* isotropic subbundle *W* of *V* and a full flag *F* of *W*. The scheme *Y* inherits properness from Grassmannians and *G* naturally acts on *Y*. We claim that *G* acts transitively on *Y*. For this purpose, it suffices to show that *G*(*k*) acts transitively on the set of *n*-dimensional isotropic subspaces of *V<sub>k</sub>* because the *G*-stabilizer of *W<sub>std</sub>* acts transitively on the variety of its full flags (since the isotropicity of *W<sub>std</sub>* provides points of *G* = SO(*q*) preserving *W<sub>std</sub>* through whatever linear automorphism we wish: 0 1 *g ~*0 0<sub>n</sub> *M* (*g*) := @ 0 1 0 A 0<sub>n</sub> *~*0 *J*(*g<sup>t</sup>*)<sup>−1</sup>*J*

for *g ∈* GL(*W<sub>std</sub>*) = GL<sub>n</sub>). To verify the transitivity of the *G*(*k*)-action on the set of *n*-dimensional isotropic subspaces of *V<sub>k</sub>* we now recall an important fact:

Theorem 3.1 (Witt Extension Theorem). *Let* (*W,Q*) *be any* (*possibly degenerate!*) *finite-dimensional quadratic space over a field K. If W <sup>′</sup>,W <sup>′′</sup> ⊂ W are subspaces and W <sup>′</sup> ∩ W* *⊥* = 0 = *W <sup>′′</sup> ∩ W* *⊥* *then any isometry W <sup>′</sup> ’ W <sup>′′</sup> extends to an element of* O(*W,Q*)(*K*)*.*

*Proof.* For a proof which (unlike most references) permits characteristic 2 and imposes no non-degeneracy conditions on *Q* or parity conditions on dim*W*, see Theorem 8.3 in the book “The Algebraic and Geometric Theory of Quadratic Forms”. The proof proceeds by induction on dim*W*, and such induction generally cannot preserve non-degeneracy hypotheses, so for the purposes of the proof it is a virtue that we impose no non-degeneracy (nor dimension parity) conditions on (*W,Q*).

All isotropic subspaces *W* of *V* with a given common dimension are isometric since *q|<sub>W</sub>* = 0 for all such *W*, so if *W,W <sup>′</sup> ⊂ V* are isotropic with dim*W ≤* dim*W <sup>′</sup>* then O(*q*)(*k*) carries *W* into *W <sup>′</sup>* (and onto *W <sup>′</sup>* when dim*W* = dim*W <sup>′</sup>*). Hence, all maximal isotropic subspaces of *V* have the same dimension, so that dimension must be *n* (as *W<sub>std</sub>* is maximal isotropic), and O(*q*)(*k*) acts transitively on the set of these. But oddness of dim*V* implies that O(*q*) = *µ₂ ×* SO(*q*) as group schemes, where *µ₂* acts on *V* through scaling, so the transitivity of O(*q*)(*k*) on the set of maximal isotropic subspaces implies the same for SO(*q*)(*k*) = *G*(*k*). Applying this over *k* then gives the desired transitivity of the *G*-action on *Y*. It follows that for the standard full flag *F<sub>std</sub>* = *{k*e₀ *⊂···⊂ W<sub>std</sub>}* in *W<sub>std</sub>*, the *G*-stabilizer *B* of (*W<sub>std</sub>,F<sub>std</sub>*) satisfies *G/B ’ Y*, so *G/B* is proper. Explicitly, if we define 0 1 0 1 *u ~*0 0<sub>n</sub> 1<sub>n</sub> *−*2*Jv L* *M* (*u*) = @*~*0<sup>t</sup> 1 *~*0<sup>t</sup> A*, h*(*v,L*) := @*~*0<sup>t</sup> 1 *v<sup>t</sup>*A 0<sub>n</sub> *~*0 *J*(*u<sup>t</sup>*)<sup>−1</sup>*J* 0<sub>n</sub> 0 1<sub>n</sub>

for upper triangular unipotent *u ∈* GL<sub>n</sub>, *v ∈ k<sup>n</sup>*, and *L ∈* Mat<sub>n</sub> then

*B* = *T* n *{M*(*u*) n *h*(*v,L*)*| v<sup>′</sup><sup>t</sup>*(*L<sup>t</sup>J* + *vv<sup>t</sup>*)*v<sup>′</sup>* = 0 for all *v<sup>′</sup> ∈ k<sup>n</sup>}*

with *L<sup>t</sup>J* generally not symmetric. For instance, with *v* = 0 the condition on *L* = (*‘<sub>ij</sub>*) *∈* Mat<sub>n</sub> is that it is “alternating with respect to the anti-diagonal”: its anti-diagonal vanishes and it is skew-symmetric relative to flipping across the anti-diagonal (i.e., *‘<sub>ij</sub>* = 0 when *i* + *j* = *n* + 1 and *‘<sub>i,n+1−j</sub>* = *−‘<sub>j,n+1−i</sub>* when *i* + *j 6*= *n* + 1). The defining condition on pairs (*v,L*) is *linear* in *L* for a given *v*, so the scheme-theoretic description of *B* is smooth and connected (of dimension *n²* + *n* due to the description in terms of *T*, *u ∈ U<sub>n</sub>*, *v ∈ k<sup>n</sup>*, and *L*), so properness of *G/B* implies that *B* is parabolic. Explicitly, *B* has a composition series with solvable successive quotients given by: the space of *L ∈* Mat<sub>n</sub> that are alternating with respect to the anti-diagonal, *k<sup>n</sup>* (corresponding to *v*), *U<sub>n</sub>* (corresponding to *u*), and *T*, so *B* is solvable and hence is a Borel subgroup of *G*! The definition of *B* has an evident analogue *B<sup>−</sup>* by reflecting conditions across the main diagonal, and *B∩B<sup>−</sup>* = *T* is a torus, proving that *G* is connected reductive. It also follows from dimension considerations that the size of a positive system of roots Φ<sup>+</sup> = Φ(*B,T*) is *n²*, so there are *n²* roots supported in the Lie algebra of the unipotent radical of *B*; we seek to find these roots. There are (*n² − n*)*/*2 such roots given by *t<sub>i</sub>/t<sub>j</sub>* for *i < j*, namely from the standard root groups contained in *U<sub>n</sub>* (setting *v* and *L* to vanish), and *n* more given by *t<sub>i</sub>* (1 *≤ i ≤ n*) through the *T*-action on the coordinate *v<sub>n+1−i</sub>* of *v ∈ k<sup>n</sup>* using the evident *T*-equivariant subquotient Lie(*k<sup>n</sup>*) of Lie(*B*) (parameterized by *v ∈ k<sup>n</sup>*). Finally, we get (*n² − n*)*/*2 more roots *t<sub>i</sub>t<sub>j</sub>* for *unordered pairs* of distinct *i,j ∈{*1*,...,n}* with *i* +*j 6*= *n*+ 1, using as the root line the coordinate *‘<sub>i,n+1−j</sub>* = *−‘<sub>j,n+1−i</sub>* in the Lie algebra of the space of *L ∈* Mat<sub>n</sub> that are alternating with respect to anti-diagonal flip. The collection of *n* such positive roots

∆ := *{a<sub>i</sub>* = *t<sub>i</sub>/t<sub>i+1</sub>}₁≤i≤n−*1*∪{a<sub>n</sub>* = *t<sub>n</sub>}*

is easily checked to generate the rest of Φ(*B,T*) under repeated additions, and the connected semisimple group *G* has rank dim*T* = *n*, so these *n* roots constitute a root basis. By inspection, ∆ spans X(*T*)=Z<sup>n</sup> with standard basis *{e₁,...,e<sub>n</sub>}* relative to which *a<sub>i</sub>* = *e<sub>i</sub> − e<sub>i+1</sub>* for 1 *≤ i ≤ n −* 1 and *a<sub>n</sub>* = *e<sub>n</sub>*. In particular, *ZG* = 1. To compute the coroot *a* *∨* <sub>i</sub> we need to determine *G<sub>a</sub>* *i* = *〈U<sub>a</sub><sub>i</sub>,U<sub>−a</sub><sub>i</sub>〉* (e.g., is this SL₂ or PGL₂?). For 1 *≤ i < n* we have *G<sub>a</sub>* *i* = SL₂ inside SL(*W<sub>std</sub>*) = SL<sub>n</sub> using the *i*th and (*i*+ 1)th rows and columns, so *a* *∨* <sub>i</sub> = *e<sup>∗</sup><sub>i</sub> − e<sup>∗</sup><sub>i+1</sub>* inside X<sub>∗</sub>(*T*). The case *i* = *n* requires some more work involving how the coroots for a split reductive pair are *defined*. We have

*G<sub>a</sub>n*:= *〈U<sub>a</sub><sub>n</sub>,U<sub>−a</sub><sub>n</sub>〉* = SO(*x<sub>n−1</sub>x<sub>n+1</sub>* + *x²<sub>n</sub>*) = Aut(sl₂*,*det)

where sl₂ consists of matrices of the form () *x<sub>n</sub> x<sub>n−1</sub>* *.* *x<sub>n+1</sub> −x<sub>n</sub>*

The natural isomorphism PGL₂ *’ G<sub>a</sub>n*= SO₃ induced by the det-invariant GL₂-conjugation on Mat₂ *⊃* sl₂ satisfies 0 1 () () 1 *x² x − x²* *t* 0 1 *x* @ A *7→* diag(*t,*1*,*1*/t*) *∈ T ∩ G<sub>a</sub><sub>n</sub>, 7→* 0 1 *x ∈ U<sub>a</sub><sub>n</sub>,*

so this isomorphism carries the diagonal of PGL₂ over to *a* *∨* <sub>n</sub>(GL₁) and carries the upper triangular unipotent subgroup over to the root group for *a<sub>n</sub>* (recall the unique characterization of root groups). Hence, the standard coroot formula *t 7→* diag(*t²,*1) for PGL₂ implies that *a* *∨* <sub>n</sub> = 2*e<sup>∗</sup><sub>n</sub>*. With the coroots determined for each root in ∆, we see that Z∆ *∨* has index 2 inside X<sub>∗</sub>(*T*) (so *G* ˜ is a central double cover of

*G*). Likewise, the orthogonal reflection on Q<sup>n</sup> in each *a<sub>i</sub>*
relative to the standard dot product on Q<sup>n</sup> = X(*T*)<sub>Q</sub> is directly verified to calculate the effect of *r<sub>a</sub>* *i* on ∆ (the *r<sub>a</sub>*’s*defined* via coroots, not via Euclidean geometry!), so the standard dot product is Weyl-invariant. But *a<sub>i</sub> · a<sub>j</sub> 6*= 0 for 1 *≤ i < j ≤ n* if (and only if) *j* = *i*+ 1, so the Dynkin diagram is connected. The root system is therefore *irreducible*, so the standard dot product is the canonical (up to positive scaling) Euclidean structure. By inspection of our list of all positive roots, it follows that there are *n* short positive roots and *n² − n* long positive roots, with ratio of square root lengths equal to 2 (long divided by short). Hence, Dyn(Φ(*G,T*)) is the B<sub>n</sub>-diagram:

- *◦ ◦ ◦ ··· ◦***+3***◦* *a* 1*a*2*a*3*a*4*an−*1*an*
4. Type C
Fix *n ≥* 2, and define *G* = Sp(*ψ*) where *ψ* is the alternating form on *V* = *k<sup>2n</sup>* given by the matrix () 0 1<sub>n</sub> *J* =*.* *−*1<sub>n</sub> 0 In other words, *G* is the functor of points *g ∈* GL<sub>2n</sub> such that *g<sup>t</sup>Jg* = *J*. By the first course, we know *G* is smooth and connected. We say that a subspace *W ⊂ V* is *isotropic* if *ψ|W ×W*= 0. It is easy to check that the group of diagonal matrices *T ⊂* GL<sub>2n</sub> having the form () *t<sup>−1</sup>* 0 0 *t*

for diagonal *t ∈* GL<sub>n</sub> is contained in *G*, and by studying weights for the standard representation of *T* on *k<sup>2n</sup>* it is not difficult to verify that *ZG*(*T*) = *T*. Thus, *T* is a maximal torus of *G*. Once again, we will *prove G* is semisimple. To compute a Borel subgroup *B* of *G* containing *T* we will introduce an appropriate “flag variety” involving maximal isotropic subspaces, as we did for odd orthogonal groups above. This requires the following analogue of the transitivity result that we deduced for orthogonal groups from the Witt Extension Theorem:

Theorem 4.1. *All maximal isotropic subspaces W ⊂ V have dimension n, the G*(*k*)*-action* *on the set of such subspaces is transitive, and if W is such a subspace then* Stab<sub>G(k)</sub>(*W*) *acts* *transitively on the set of full flags in W.*

This is *much* easier to prove than the analogue for orthogonal groups, as the structure of symplectic spaces is much simpler than that of (possibly degenerate!) quadratic spaces. More specifically, the proof of this Theorem requires nothing more than a review of the proof

of the structure theorem for symplectic spaces (over fields), so we leave this as an exercise for the reader. As in the odd orthogonal case, we use Grassmannians to build a proper scheme *Y* representing the functor of pairs (*W,F*) consisting of a rank-*n* isotropic subbundle of *V* and a full flag *F* of *W*. Letting *{*e₁*,...,*e<sub>2n</sub>*}* denote the standard basis of *V* = *k<sup>2n</sup>*, define the maximal isotropic subspace *W<sub>std</sub>* = span(e₁*,...,*e<sub>n</sub>), and let *F<sub>std</sub>* be its standard full flag (beginning with the line *k*e₁). One verifies by computation that {()} (*u<sup>t</sup>*)<sup>−1</sup> *mu* *B* := Stab<sub>G</sub>(*W<sub>std</sub>,F<sub>std</sub>*) = *T* n *| m ∈* Sym<sub>n</sub>*,u ∈ U<sub>n</sub>* 0 *u*

(where Sym<sub>n</sub> *⊂* Mat<sub>n</sub> is the subspace of symmetric matrices). This *B* has a composition series with successive quotients Sym<sub>n</sub>, *U<sub>n</sub>*, and *T*, so it is smooth and connected of dimension *n²* + *n* and solvable. By properness of *G/B* = *Y* it follows that *B* is a Borel subgroup (containing *T*). The analogous subgroup *B<sup>−</sup>* using the “lower triangular constructions” (i.e., the “opposite” maximal isotropic subspace and its standard flag beginning at *k*e<sub>2n</sub>; in effect, transporting the construction of *B* for *V <sup>∗</sup>* via the duality *ψ*) is also a Borel subgroup, and *B∩B<sup>−</sup>* = *T* is a torus, so this proves that *G* is reductive. The *n²* positive root groups and associated roots for (*B,T*) can be worked out much more easily than for the odd orthogonal case: we get *n*(*n −* 1)*/*2 roots *t<sub>i</sub>/t<sub>j</sub>* for 1 *≤ i < j ≤ n* from the *ij*-entry of *U<sub>n</sub>*, and *n*(*n* + 1)*/*2 roots (*t<sub>i</sub>t<sub>j</sub>*)<sup>−1</sup> for 1 *≤ i ≤ j ≤ n* from the common *ij* and *ji* matrix entries in the symmetric *m ∈* Sym<sub>n</sub>. In particular, Φ clearly spans X(*T*)<sub>Q</sub>, so the connected reductive *G* is semisimple. Under the evident identification of X(*T*) with Z<sup>n</sup> with standard basis denoted *e₁,...,e<sub>n</sub>* (projection onto matrix entries for *t ∈ T*), the positive roots are *e<sub>i</sub> − e<sub>j</sub>* for *i < j* and *−*(*e<sub>i</sub>* + *e<sub>j</sub>*) for *i ≤ j*. The set of *n* positive roots

∆ = *{a<sub>n−i</sub>* = *t<sub>i</sub>/t<sub>i+1</sub>}i<n∪{a<sub>n</sub>* = *t<sup>−</sup>*1 2*}*

generates the rest under repeated additions, so since *G* is semisimple with rank dim*T* = *n* it follows that ∆ is the root basis for Φ(*B,T*). It is easy to verify that *G<sub>a</sub>*:= *〈U<sub>a</sub>,U<sub>−a</sub>〉* = SL₂ (identification using standard matrix coordinates on *G ⊂* GL<sub>n</sub>) for all *a ∈* Φ<sup>+</sup>, with this identification carrying *T ∩ G<sub>a</sub>* over to the diagonal of SL₂ and carrying *U<sub>a</sub>* over to the upper triangular unipotent subgroup of SL₂, so we see that (*e<sub>i</sub> ± e<sub>j</sub>*) *∨* = *e<sup>∗</sup><sub>i</sub> ± e<sup>∗</sup><sub>j</sub>* for *i < j* (and likewise for the negative; recall that (*−a*) *∨* = *−a* *∨* for any element *a* in a root system), and that (2*e<sub>i</sub>*) *∨* = *e<sup>∗</sup><sub>i</sub>*. In particular, ∆ *∨*

spans X<sub>∗</sub>(*T*), so *G* is *simply connected*. Now that the coroots have been determined, as in the odd orthogonal case we easily check that the standard dot product on X(*T*)<sub>Q</sub> = Q<sup>n</sup> computes the reflection *r<sub>a</sub>* (defined via coroots) via Euclidean reflection in *a*. In particular, the standard dot product is Weyl-invariant. By direct calculation we find once again that for 1 *≤ i < j ≤ n*, *a<sub>i</sub> · a<sub>j</sub> 6*= 0 if and only if *j* = *i* + 1, so the Dynkin diagram is connected and hence Φ(*G,T*) is irreducible. It follows that the Weyl-invariant standard dot product provides the canonical (up to scaling) Euclidean structure, so we can use it to compute root lengths. This yields the C<sub>n</sub>-diagram:

- *◦ ◦ ◦ ··· ◦***ks***◦* *a* 1*a*2*a*3*a*4*an−*1*an*
Note that there are *n* long positive roots *t* *±* <sub>i</sub> 2 and *n² − n* short positive roots, and the long ones lie in 2X(*T*). By inspection of the classification of reduced irreducible root systems, simply connected type C<sub>n</sub> for *n ≥* 1 (where C₁ := A₁ is treated separately) are the only semisimple root data (*X,*Φ*,X* *∨* *,* Φ *∨* ) for which there is a root that is divisible (in fact, by 2) in *X*.

5. Type D
Fix *n ≥* 3, and let *G* = SO(*q*) for the quadratic form

*q* = *x₁x<sub>2n</sub>* + *···* + *x<sub>n</sub>x<sub>n+1</sub>*

on *V* = *k<sup>2n</sup>*. By the previous course, this is smooth and connected. This also makes sense for *n* = 2, but SO₄ = SL₂ *×<sup>µ</sup>* 2 SL₂ (so the Dynkin diagram is the reducible A₁ *×* A₁). Our treatment of this case will be a simplified version of the work already done in the odd orthogonal case; in effect, everything goes similarly except that various matrices no longer have a “middle column/row” (and the effect on the Dynkin diagram will be to split the long vertex into two arms associated to roots with the same length as the rest). The split torus *T ⊂* GL<sub>2n</sub> consisting of points

diag(*t₁,...,t<sub>n</sub>,t<sup>−1</sup><sub>n</sub>,...,t<sup>−</sup>*1 1)

is obviously contained in *G*, and as in the odd orthogonal case we see that *ZG*(*T*) = *T*, so *T* is maximal in *G*. In fact, since there is no “middle 1” in the description of points of *T*, one can verify that even *Z<sub>O(q)</sub>*(*T*) is equal to *T*. We will again use the Witt Extension Theorem to find a Borel *k*-subgroup of *G* containing

*T*. Let *Y* be the proper flag scheme defined as in the odd orthogonal case, so for the natural action of O(*q*) on *Y* we see that O(*q*)(*k<sup>′</sup>*) acts transitively on *Y* (*k<sup>′</sup>*) for every field *k<sup>′</sup>/k*. (Beware that *G* does *not* act transitively on *Y*. This is due to the disconnectedness of O(*q*) being inherited by *Y*, as we will see below, and so is a fundamental distinction from the odd orthogonal case.) Define the standard maximal isotropic subspace
*W<sub>std</sub>* = span(e₁*,...,*e<sub>n</sub>) *⊂ k<sup>2n</sup>* = *V*

and its standard full flag *F<sub>std</sub>* beginning with *k*e₁. Define *B* similarly to the odd orthogonal case but with no “middle row/column” contribution (so no intervention of *v ∈ k<sup>n</sup>*!). One verifies by similar (but easier) calculations to the odd orthogonal case that

## Stab<sub>O(q)</sub>(W<sub>std</sub>,F<sub>std</sub>) = B

as schemes, and that *B* is smooth, connected, and solvable. In particular, by quotient considerations for transitive actions by smooth groups we conclude that (O(*q*)*/B*)<sub>k</sub> has underlying reduced scheme *Y<sub>k</sub>* (in fact, O(*q*) is smooth in all characteristics, being an extension of Z*/*2Z by SO(*q*), but we do not need this). Thus, O(*q*)*/B* is proper, so *G/B* is proper. Hence, *B* is parabolic and therefore is a Borel subgroup of *G*.

The positive system of roots Φ<sup>+</sup> = Φ(*B,T*) comes out exactly as in the odd orthogonal case except that we do not get *t<sub>i</sub>*’s as roots (due to the absence of the middle column/row in the present calculations). We again build another Borel subgroup *B<sup>−</sup>* satisfying *B ∩ B<sup>−</sup>* = *T*, so *G* is reductive. The positive roots span X(*T*)<sub>Q</sub>, so *G* is semisimple. Hence, Φ<sup>+</sup> has a root basis of size *n*. We verify without difficulty that now the root basis is given by

∆ = *{a<sub>i</sub>* = *t<sub>i</sub>/t<sub>i+1</sub>}₁≤i<n∪{a<sub>n</sub>* = *t<sub>n−1</sub>t<sub>n</sub>}.*

Using the usual identification X(*T*) = Z<sup>n</sup> with standard basis *{e₁,...,e<sub>n</sub>}*, we have *a<sub>i</sub>* = *e<sub>i</sub> − e<sub>i+1</sub>* for 1 *≤ i < n* and *a<sub>n</sub>* = *e<sub>n−1</sub>* + *e<sub>n</sub>*. We need to compute the associated coroots *a* *∨* <sub>i</sub>. As in the odd orthogonal case we have the same identification *G<sub>a</sub>* *i* = SL₂ for *i < n*, yielding again that *a* *∨* <sub>i</sub> = *e<sup>∗</sup><sub>i</sub> − e<sup>∗</sup><sub>i+1</sub>* for *i < n*. The computation of *G<sub>a</sub>n*turns out differently: it is not PGL₂ as in the odd orthogonal case, but rather is SL₂ in a specific manner. Namely, we use the standard isomorphism

SO(*x<sub>n−1</sub>x<sub>n+2</sub>* + *x<sub>n</sub>x<sub>n+1</sub>*) = SO₄ = Aut(gl₂*,*det) *’* SL₂ *×<sup>µ</sup>* 2 SL₂

to identify *G<sub>a</sub>n*with one of these SL₂-factors, and by keeping track of where *T ∩ G<sub>a</sub>n*and *U<sub>a</sub>n*go under this identification we obtain

*a* *∨* <sub>n</sub> = *e<sup>∗</sup><sub>n−1</sub>* + *e<sup>∗</sup><sub>n</sub>.*

As in the odd orthogonal case, the standard dot product on X(*T*)<sub>Q</sub> = Q<sup>n</sup> computes the reflections *r<sub>a</sub>* *i* as the Euclidean reflection through *a<sub>i</sub>*, so this dot product is Weyl-invariant. Moreover, now *a<sub>i</sub> · a<sub>i+1</sub>* = *−*1 for *i < n −* 1 whereas *a<sub>n−1</sub> · a<sub>n</sub>* = 0 but *a<sub>n−2</sub> · a<sub>n</sub>* = *−*1 (note that *a<sub>n−2</sub>* makes sense because *n ≥* 3), so the Dynkin diagram is connected. Hence, Φ(*G,T*) is irreducible, so the standard dot product is the unique Weyl-invariant Euclidean structure up to scaling. By inspection the root lengths for all *a<sub>i</sub>*’s coincide, and we arrive at the D<sub>n</sub>-diagram:

*◦* *a* *n−*1

- *◦ ◦ ◦ ··· ◦ ◦* *a* 1*a*2*a*3*a*4*an−*3*an−*2
*◦* *a* *n* The determination of ∆ and ∆ *∨* yields that the root lattice Z∆ has index 2 inside X(*T*) and that the coroot lattice Z∆ *∨* has index 2 inside X<sub>∗</sub>(*T*). Hence, *ZG* has order 2 (so the evident central *µ₂ ⊂ G* coincides with *ZG*) and the simply connected central cover *G* ˜ is a degree-2 cover of *G* = SO<sub>2n</sub>.

*Remark* 5.1*.* A rather special situation, called *triality*, arises for the case *n* = 4: the diagram for D₄ has automorphism group *S₃*. This is the only reduced irreducible root system whose diagram has nontrivial automorphisms beyond a single involution. The corresponding group SO₈ then has “more symmetry” than typical special orthogonal groups. This was seen classical via constructions involving octonion algebras. (Beware however, that the automorphism group of an octonion algebra much smaller than SO₈: in fact, it is connected semisimple of type G₂, as explained in 2.3.5 and 2.4.5 of the book “Octonions, Jordan algebras, and exceptional groups”.)

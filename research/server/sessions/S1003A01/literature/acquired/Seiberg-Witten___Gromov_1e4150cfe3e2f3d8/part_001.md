---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Seiberg-Witten ⇒ Gromov]

# Seiberg-Witten ⇒ Gromov

> Source: https://jeffhicks.net/files/SymplecticProjectMain.pdf
> Fetched: 2026-10-09 12:30
> Method: FULLTEXT_HTML_JINA|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA|ORIGINAL_FILES=1

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
  "source": "tavily",
  "source_url": "https://jeffhicks.net/files/SymplecticProjectMain.pdf",
  "metadata": {
    "provenance_urls": [
      "https://jeffhicks.net/files/SymplecticProjectMain.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "Taubes SW=Gr J-holomorphic subvariety canonical class exceptional classes b+ greater than one chamber"
      },
      {
        "source": "tavily",
        "query": "SW Gr every tame almost complex exceptional classes canonical minimal class J-holomorphic current b plus one chamber"
      },
      {
        "source": "tavily",
        "query": "Seiberg-Witten exceptional class every tame almost complex structure J-holomorphic subvariety current canonical class minimal symplectic 4-manifold"
      }
    ]
  },
  "declared_files": [
    {
      "url": "https://jeffhicks.net/files/α",
      "name": "α",
      "label": "e",
      "role": "neighbor_file_reference",
      "parent_url": "https://jeffhicks.net/files/SymplecticProjectMain.pdf",
      "identity_bound": false,
      "primary_label": false,
      "download_eligible": false
    },
    {
      "url": "https://jeffhicks.net/files/SymplecticProjectMain.pdf",
      "name": "SymplecticProjectMain.pdf",
      "label": "",
      "role": "primary_object_file",
      "parent_url": "https://jeffhicks.net/files/SymplecticProjectMain.pdf",
      "identity_bound": true,
      "primary_label": false,
      "download_eligible": true
    }
  ]
}
```

## Source description

Nathan Seiberg and Edward Witten. “Electric-magnetic duality, monopole condensation, and con-ﬁnement in N = 2 supersymmetric Yang-Mills theory”. In: Nuclear Physics B 426.1 (1994), pp. 19– 52.
 Clifford H Taubes. “SW⇒Gr: From the Seiberg-Witten Equations to Pseudo-Holomorphic Curves”.
In: Journal of the American Mathematical Society (1996), pp. 845–918.
 Clifford Henry Taubes et al. “Counting pseudo-holomorphic submanifolds in dimension 4”. In: J.
Differential Geom 44.4 (1996), pp. 818–893.
 Clifford Henry Taubes et al. “Gr=SW: counting curves and connections”. In: Journal of Differential Geometry 52.3 (1999), pp. 453–609.
 Clifford Henry Taubes et al. “Gr⇒SW: from pseudo-holomorphic curves to Seiberg-Witten solutions”.
In: Journal of Differential Geometry 51.2 (1999), pp. 203–334. [...] Theorem 2.2.3 Structure of H(A, Ωk) For generic ω-tame almost complex structure J on M, and A ∈H2(M,Z), we have the following characterizations of H(A,Ωk).
1. Suppose that (φ,Σ) ∈H(A,Ωk) is good. Then : (a) Every (φ′,Σ′) ∈H(A,Ωk) is good.
V.2014/11/17.09:25:57 2.2 Taubes’s Gromov invariant, with Caveats 21 (b) The image of the connected components are disjoint, that is φ(Σi) ∩φ(Σj) = ∅ (c) The multiplicity of φ∣Σi is one, unless g(Σi) = 1 and φ(Σi) has no self intersections.
(d) H(A) is zero dimensional.
2. If (φ,Σ) ∈H(A,Ωk), then the image φ(Σi) of every Σi such that φ(Σi) ⋅φ(Σi) < 0 is an embedded exceptional sphere, with multiplicity possibly greater than 1. [...] 9 1.4.1 The Invariant . .

## Retrieved source content

Title: SymplecticProjectMain.pdf

URL Source: https://jeffhicks.net/files/SymplecticProjectMain.pdf

Published Time: Mon, 17 Nov 2014 17:26:00 GMT

Number of Pages: 36

Markdown Content:
# Seiberg-Witten ⇒ Gromov 

## Jeff Hicks, DongGyu Lim Spring 2014 i

## Introduction 

This report was put together for Math 242 at UC Berkeley during the spring of 2014. It contains a rough outline of the techniques to produce the Seiberg-Witten equations, Gromov-Taubes invariant, and the method used by Taubes to show that the Seiberg-Witten equations can produce the Gromov invariant. A general outline of the history related to this exposition: In 1983, Donaldson [1] used techniques of gauge theory to explore the diffeomorphism type of 4-manifolds. By looking for instantons on four manifolds, Donaldson proved that the intersection form on a 4-dimensional manifold is diagonalizable. Corollaries of this theorem showed that there existed different differential structures for the same topological manifolds. While the Donaldson invariants were very useful, they were difficult to compute. In particular, the moduli space of connections with self dual curvatures was not compact. In 1994, Seiberg and Witten used techniques they developed in [12] to develop the Seiberg-Witten invariants attached to Spin c on 4-manifolds. The solutions to the Seiberg-Witten equations formed a smooth compact moduli space which captured the same data as the Donaldson invariants, but were easier to compute. The Seiberg-Witten invariant is an assignment to every Spin c structure on a manifold a number that “counts” the number of solutions to the Seiberg-Witten equations. Separately from Donaldson’s work on instantons, Gromov in 1985 developed the theory of pseudoholomor-phic curves for symplectic manifolds. In his paper [3], Gromov gave the basic ideas for “Gromov invariants”. Given a symplectic manifold M with compatible J-holomorphic structure, Gromov studied the moduli space of pseudoholomorphic curves that represented a class in the 2nd homology of M . By requiring the pseudoholomorphic curves to pass through a certain number of points, one could make the moduli space a finite number of points and count pseudoholomorphic curves. This brings us to the result that we are going to explore in this exposition. In a series of papers ([14], [13], [15], [16]) Taubes showed an equivalence between a Gromov-type invariant and the Seiberg-Witten invariants. Taubes used these results to compute the Gromov invariants for manifolds where the Seiberg-Witten invari-ants were understood. Interestingly, his paper shows that the Gromov-Taubes invariant, though apparently an invariant of symplectomorphism type, actually is only dependent on the diffeomorphism type of the manifold. Here, we will look how solutions to the Seiberg-Witten equations can be used to produce pseudoholomorphic curves. The first two sections are the general background knowledge needed to state the problem, and short outlines of the proofs used in the construction of the Seiberg-Witten and Gromov-Taubes invariant. The sections most related to the course are Section 1.5 on page 10, and Parts 2 and 3. Of particular interest is Section 3.3 on page 30 which outlines the broader impacts of Taubes’s work to symplectic geometry and 

J-holomorphic curves. A general outline of the main ideas of the paper are as follows 1. We start with an exploration of the Seiberg-Witten invariants. • Given a Spin Structure ˜P → M (Section 1.1 on page 1) over a 4 dimension manifold with metric 

g, one can use the Dirac operator (Subsection 1.1.2) to set up an equation searching for positive spinors that satisfy a certain set of equations, the Seiberg-Witten Equations • By taking a slight perturbation η to the Seiberg-Witten Equations, the moduli space of the solutions MSW ∗ 

> η

( ˜P ) is a compact smooth manifold whose dimension can be computed with the Atiyah-Singer index theorem (Section 1.2 on page 3). • It can be shown that a homotopy of metric g induces a cobordism between associated moduli spaces. Therefore the cobordism type of MSW ∗ 

> η

is independent of metric. By counting solutions by taking an appropriate integral over MSW ∗ 

> η

( ˜P ) of certain homology class, we get a number associated to every spin bundle that is independent of g. We can think of the Seiberg-Witten invariants therefore as an assignment 

SW ∶ Spin (M ) → Z.

> V.2014/11/17.09:25:57

ii 

• We spend the last section exploring the Seiberg-Witten equations over symplectic 4 manifolds. Here, we show that there is a particularly nice choice of perturbation parameter that relies on the symplectic structure. Furthermore, by using the almost complex structure we are able to identify 

Spin (M ) ≃ H2(M, Z), and therefore can think of the Seiberg-Witten invariant as an assignment 

SW ∶ H2(M, Z) → Z.

2. The second chapter is used to look at pseudoholomorphic curves and Gromov-Taubes invariant. • We first explore the basics of psuedoholomorphic curves and their associated moduli spaces. • Given a class A ∈ H2(M, Z), we then look at H( A), the space of pseudoholomorphic submani-folds that pass through some specified number of generic points, modulo the case of multiply covered tori, which we will explore later. • We will not talk about the awfulness which is multiply covered tori. • The final section on Gromov-Taubes invariant is to count the number of curves that show up in 

H( A). We can therefore view Gromov-Taubes invariant as an assignment 

Gr ∶ H2(M, Z) → Z.

3. Finally, we would like to show some relations between these invariants. In the third part, we explore a small section of Taubes’s proof: we construct a surface from the Seiberg-Witten equations. We leave off the proof that the surface that we have constructed is a submanifold or pseudoholomorphic, but show that the “interesting” behavior of the Seiberg-Witten solutions fall on a Hausdorff dimension 2 set. Our outline of this proof is roughly as follows: • By looking at a set of solutions to the perturbed symplectic Seiberg-Witten equations, we can create a sequence of currents on the manifold related to solutions of the Seiberg-Witten equations. • In Subsection 3.2.1, we study the energy of these currents, and show that they are bounded. In particular, we can find a convergent subsequence of these currents. • To better understand the behavior of these currents, we look at the zero set of the solution of the Seiberg-Witten equations. • In fact, most of the interesting behavior of a solution of the Seiberg-Witten equations is deter-mined by this zero set (Subsection 3.2.2). We show that most characteristics of the Seiberg-Witten equations all drop off exponentially from the zero set of the solution when we vary the perturba-tion parameter. • We characterize the zero set of the Seiberg-Witten equations by a set of Hausdorff dimension 2 in Subsection 3.2.3. This completes the relation between the Seiberg-Witten equations and Gromov-Taubes invariant. Taubes later goes on to show that this set C is a psuedoholomorphic curve, and that it contains the relevant information to recover the Gromov Taubes invariant. 

Resources 

Our primary resources for this exposition are • For the Seiberg-Witten invariants, [8], [4] and [9]. • For understanding psuedoholomorphic curves, besides notes from class, we used [6]. For the definition of Gromov-Taubes invariants, both [7] and [14] were used. • The construction of psuedoholomorphic curves from Seiberg-Witten monopoles is from [15] and [13]. 

> V.2014/11/17.09:25:57

iii 

Notation 

cl The Clifford multiplication map 

C( ˜P ) The SW configuration space 

˜C( ˜P ) The Reduced SW configuration space 

ev (φ, τ, z 1 . . . z l) The evaluation mapping 

F + 

> A

The self dual part of the curvature FA

FSW The Seiberg-Witten Function 

G( ˜P ) Gauge actions on SW configuration space 

Gr (A) The Gromov Invariant of AJ Almost complex structure 

L The line bundle associated to a Spin structure 

Mg (A) Moduli space of genus g pseudoholomorphic curves representing A

MSW ( ˜P ) The Seiberg-Witten moduli space 

MSW η ( ˜P ) η-perturbed redusce SW moduli space 

q(φ) The quadratic map of a spinor 

Spin (n) The n-dimensional spin group 

S± The positive and negative spin representations 

ω Symplectic Form 

W k,p (E) Sobelov (k, p ) sections of a bundle E

> V.2014/11/17.09:25:57

# Contents 

1 The Seiberg-Witten Invariants 1

1.1 Spin Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.1.1 Spin Groups and Spin Bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.1.2 The Dirac operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21.2 The Seiberg-Witten Equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31.3 The Seiberg-Witten Moduli Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61.3.1 Compactness of MSW ( ˜P ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61.3.2 The Perturbed Moduli Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81.4 The Seiberg-Witten Invariants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91.4.1 The Invariant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 1.5 Seiberg-Witten over Symplectic Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 

2 Taubes’s Gromov Invariant 12 

2.1 Background on Pseudoholomorphic Curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 2.1.1 Almost Complex Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 2.1.2 J-holomorphic Curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 2.1.3 The moduli space of somewhere injective holomorphic curves . . . . . . . . . . . . . 14 2.1.4 Cusp Curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 2.1.5 Evaluation Mapping and Pseudocycles . . . . . . . . . . . . . . . . . . . . . . . . . . 19 2.2 Taubes’s Gromov invariant, with Caveats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 

3 SW ⇒ Gromov 22 

3.1 Outline of Proof of Theorem 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 3.2 Constructing C . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 3.2.1 Energy of the Seiberg-Witten Equations . . . . . . . . . . . . . . . . . . . . . . . . . 24 3.2.2 Exponential Decay of Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 3.2.3 Covering the Solution with Balls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28 3.2.4 Further Properties of C . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28 3.2.5 Other Properties of C . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 3.3 Where to Proceed from here . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30 

Bibliography 30 

> V.2014/11/17.09:25:57

# The Seiberg-Witten Invariants 

For our introduction to Seiberg-Witten invariants, we will first talk about the construction of Spin structures over a manifold, before moving onto the construction of the Seiberg-Witten equations. We then discuss the topology of the solution space of those equations. Our conclusion will explore some of the additional structure that a symplectic manifold can impose on the moduli space of solutions. 

## 1.1 Spin Structures 

Our exposition follows several parts: • In Subsection 1.1.1 we will look at the spin group and its representations. In particular, we will look at splittings of the Clifford algebra and the action of the spin group on this. • Having developed the representation theory of spin groups and Clifford algebras, Subsection ?? looks at principal spin bundles. We are interested in knowing the number of different principal Spin c bundles there are over a manifold, and the natural connections that rise out of the metric structure on that bundle. • Of particular interest to us is the fact that over the Spin bundles, the Laplacian has a square root, the Dirac Operator. Subsection 1.1.2 develops the basic properties of the Dirac operator, as well as giving it an explicit description. • Finally, as the Seiberg Witten equations are define for four manifolds, we explore some nice properties of Spin bundles and Dirac operators in dimension 4. 

1.1.1 Spin Groups and Spin Bundles 

This is a quick overview of the terminology and notation that we will be using here; for an introduction to spin geometry we refer the reader to [18], [2], and [8]. Recall that given a metric structure on M , we can form the principal bundle of orthonormal frames which has an action on the tangent bundle via the standard representation. The group SO (n) which acts on these frames has a double cover Spin (n) which acts on SO (n) by conjugation. We would like to know when this map gives us principal Spin (n)-bundle over a manifold M .

Definition 1.1.1 A spin structure on an oriented Riemannian manifold M is a principal Spin (n)-bundle ˜P → M along with a map to the frame bundle ˜P → Fr such that the following diagram commutes 

˜P × Spin (n) ˜P

Fr × SO (n) Fr 

M

In other words, a spin structure is a lift of the frame bundle to a representation of Spin (n) which is compatible with the double cover Spin (n) → SO (n). If a manifold admits a spin structure, it is called spinnable .As suggested by the definition, not every manifold admits a spin structure. The obstruction to the existence of a spin structure is given by this proposition. 

> V.2014/11/17.09:25:57

2 The Seiberg-Witten Invariants Proposition 1.1.2 There are natural correspondence between the following three sets. (a) A spin structure ˜P → M

(b) An element α ∈ H1(Fr (M ); Z2) that restricts to the generator of each fiber. (c) A trivialization of Fr (M ) over the 2-skeleton Not every four manifold admits a spin structure, but by adding an additional degree of freedom to the spin group we can form group which always admits this kind of desired lifting. 

Definition 1.1.3 Define the group Spin c(n) by 

Spin c(n) = ( Spin (n) × U (1))~ Z2

Where Z2 is the subgroup {( 1, 1), (− 1, −1)} of Spin (n) × U (1)

Likewise, we can define a complex spin bundle over a manifold. A manifold is said to posses a Spin c structure if there exists a Spin c bundle whose representation over the frame bundle gives the same bundle structure as the orthogonal frame bundle. The extra degree of freedom in this bundle ensures in the four dimensional case there is always a lifting of a principal SO (n) bundle to a principal Spin c bundle. 

Proposition 1.1.4 There exists a Spin c structure whenever ctop  

> 1

(L) ≅ w2(M ) mod 2 .Finally, the Spin c structures on a manifold are a H2(M, Z) torsor. 

Claim 1.1.5 There is a natural association between the Spin c structures above M and H2(M, Z).This identification can be seen by taking the associated line bundle L = √det S which is associated to the bundle of Spinor fields. This associated line bundle is has a U (1) gauge action which extends to a U (1)

gauge action on the complex spinor bundle. From here on out, M will be a four dimensional real manifold. In the four dimensional case, we have an isomorphism between Spin (4) ≃ U (2) × U (2), which gives us two complex representations of the spin group. We will call these the positive and negative spinor representations and denote then 

ρ± ∶ Spin (4) → S± ≃ C2

The groups Spin (n) and Spin c(n) are subgroups of the Clifford algebra and its complexification. For us, it will be easiest to think of the Clifford algebra associated to the tangent bundle T M with inner product g by 

Λ∗T M equipped with the Clifford multiplication structure defined on vectors by: 

cl (a)b = a ∧ b − g(a, b ).

and extended by linearity. The Clifford multiplication structure induces a map between the positive and negative (complex) spin representations 

cl ∶ S+ ⊗ T M → S−

cl ∶ S− ⊗ T M → S+

and satisfy the relation cl (v)2 = − 1.

1.1.2 The Dirac operator 

If M is a Riemannian manifold, it comes with the Levi-Civita connection ∇ attached to it. This naturally lifts to a connection on the real spinor bundles by pulling back the connection 1-form along its representation. 

> V.2014/11/17.09:25:57

1.2 The Seiberg-Witten Equations 3

However, when we are working with complex spinors, we must also specify how to take derivatives along the added U (1) direction in order to get a connection on complex spin bundles. Once we have picked a 

U (1) connection A, we can define a connection ∇A on the complex spinor bundle. 

Proposition 1.1.6 

> Properties of the Spin Connection

The connection ∇A has the following properties 1. It is unitary, that is if s1, s 2 are two sections of ˜P , we have that 

d⟨s1, s 2⟩ = ⟨∇ As1, s 2⟩ + ⟨ s1, ∇As2⟩

2. It is a “module derivation”: if α is a section of T M , and φ a section of S, then 

∇A(α ⋅ φ) = ˜∇A(α) ⋅ φ + α ⋅ (∇ Aφ)

where the ˜∇ is the Levi-Civita connection, and the ⋅ is Clifford multiplication. 3. The U (1) gauge action of σ on L is compatible with the action on the connection; that is 

˜∇A⋅σ = σ−1 ˜∇Aσ

Dirac operators are a kind of square root to a Laplacian. When a manifold comes with a Spin c structure, there is a natural Dirac operator to consider. 

Definition 1.1.7 Let P → M be a principal SO (n) bundle, and let SC( ˜P ) be the associated (complex) spin bundle. Let 

˜∇A be the connection on SC induced from the Levi-Civita connection and a fixed U (1) connection A.Pick {ei} an orthonormal frame for T M x, then define the Dirac Operator on spinors σ(x) by 

~∂A ∶ Ω0(M, S C( ˜P )) → Ω0(M, S C( ˜P )) 

σ ↦ cl (σ)∇ A(σ)

where Clifford multiplication acts on ∇A(σ) by using the metric. This definition is independent of the choice of frame for T M x. In local coordinates we can write Dirac multiplication as n

Q

> i=1

cl (ei)( ˜∇ei (σ)( x).

We have the following facts about the Dirac operator 

Proposition 1.1.8 If ~∂ is a Dirac operator associated to a spin structure, then it is self adjoint ~∂ = ~ ∂∗ and has the following Weitzenboöck presenation: 

~∂2 = (∇ E )∗∇E + cl (F (∇ E )) = ∇ ∗

> A

∇A + κ

4 + F1

2 .

## 1.2 The Seiberg-Witten Equations 

We now have the appropriate set up for the Seiberg-Witten equations. Our plan of attack is roughly: • State the Seiberg-Witten equations, and provide some intuition for them. We’ll also be interested in the differential of these equations, and presenting them as a functional. • Look at the analytical considerations that need to be taken into account in order to topologize the space of Seiberg-Witten configurations. 

> V.2014/11/17.09:25:57

4 The Seiberg-Witten Invariants 

• Show how the compatibility of the gauge group with the Seiberg-Witten equations allow us to remove the choice of U (1) connection. 

Definition 1.2.1 

> Seiberg-Witten Equations

Given ˜P → M a Spin c structure, the Seiberg-Witten equations are 

F + 

> A

=q(φ)~∂Aφ =0

where φ ∈ Ω0(M, S +( ˜P )) is a positive spinor field for the orthogonal frame bundle P → M (and q and 

F + 

> A

as defined below) Let’s explain what these equations mean. According the physicists, the second equation means that we are looking for a field which represents a 

Fermion in quantum field theory. Mathematically, it is not too hard of an equation to understand— we are interested in an element of the kernel of the dirac operator. The first equation is a little more complicated. The left hand side F + 

> A

= 12 (FA +∗ FA) represents the self-dual 

portion of the curvature two form. The right hand side is the quadratic map 

q ∶ Ω0(M, S +( ˜P )) → Ω2(M, T CM )

φ ↦φ ⊗ φ∗ − SφS2

2 id 

sending a section of the positive spinor bundle to a self dual two form. Notice that φ⊗φ∗ is an endomorphism of the positive spinor bundle. There exists an isomorphism End C(S+( ˜P )) ≅ ( Cl 0(P ) ⊗ C)+ ≅ C  1 + ωC

2  ⊕ ( Λ2

> +

(T M ) ⊗ C)

which tells us that q(φ) is a purely imaginary self-dual two-form. Here, ωC the Clifford product of all the elements of an orthonormal basis. So given a fixed unitary connection A, a solution to the Seiberg-Witten equations corresponds to a spinor field whose quadratic part matches the self-dual portion of the curvature. When we are finding solutions to the Seiberg-Witten Equations, we will be changing both the connection A

and the spinor field φ. So in general we will want to look at pairs (A, φ ) where A is a U (1) connection on the determinant line bundle and φ is a positive spinor field. While we will eventually want smooth solutions to these equations, we will start with W 2,2 sections of these bundles to topologize the space of solutions; in the end, elliptic regularity will give us that all of our solutions are smooth. Define AW 2,2 (L) to be the space of unitary W 2,2 connections on L .

Definition 1.2.2  

> SW-Configurations

Let M be a riemannian manifold with spin structure ˜P → M a spin bundle with determinant line bundle 

L. Then the configuration space is defined to be 

C( ˜P ) = A W 2,2 (L) × W 2,2(S+( ˜P )) 

Claim 1.2.3 The tangent space of the configuration space at a point can be identified with 

W 2,2(T ∗M ⊗ iR) ⊕ S+( ˜P )

In order to study solutions to the Seiberg-Witten equations, we define the Seiberg-Witten function 

FSW ∶ C( ˜P ) → W 1,2 ( Λ2

> +

T ∗M × iR) ⊕ S−( ˜P ) (A, φ ) ↦( F + 

> A

− q(φ), ~∂A(φ)) 

> V.2014/11/17.09:25:57

1.2 The Seiberg-Witten Equations 5

and the Seiberg-Witten Functional 

SW (A, φ ) = S M

S ~ ∂AφS2 + S F + 

> A

− q(φ)S 2 dv 

Notice that the solutions to the Seiberg-Witten equations that we have defined above are simply the configu-rations which have FSW (A, φ ) = 0.

Lemma 1.2.4 The Seiberg-Witten function FSW is a smooth mapping and its differential is described by the map 

dF SW A,φ =  P+d −dq φ

⋅ 12 φ ~∂A



where P+ stands for the self-dual component. The gauge group on the spin bundle gives us an action on the configuration space. In order for this action to be well defined, we need a little more control on the derivatives of the gauge transformations. We define the 

space of gauge transformations to be maps 

G( ˜P ) ∶= W 3,2(M ; S1).

Given σ ∈ G( ˜P ), define the right action of σ on C( ˜P ) by 

(A, φ ) ⋅ σ = (( det σ)∗A, S +(σ−1(φ)) .

Notice that the space of gauge transformation is a group under Sobelov multiplication. Furthermore, the 

G( ˜)) has the necessary regularity so that its action on C( ˜P ) is well defined. Notice here that det (σ) = σ2.Furthermore, this action is going to play extremely nicely with the Seiberg-Witten function. There is also a way to define an action of G( ˜P ) on the codomain of the Seiberg-Witten function. 

Lemma 1.2.5 Let σ ∈ G( ˜P ) be a gauge transformation. Then we have that 

FSW (( A, φ ) ⋅ σ)) = ( FSW (A, φ )) ⋅ φ

This gives us the nice result that the solutions to the Seiberg-Witten equations are invariant under the gauge transformations. So we can ignore the choice of unitary connection A by passing the quotient space. In general, this quotient is not a smooth manifold, as some elements may have a nontrivial stabilizer in G( ˜P ).However, there is a nice way to remove such elements. A configuration (A, φ ) is called irreducible if φ ≠ 0.Let Cirr ( ˜P ) be the open subset of irreducible configurations. 

Lemma 1.2.6 Let (A, φ ) ∈ Cirr ( ˜P ) be an irreducible configuration. Then the stabilizer of (A, φ ) in the gauge group is trivial. If none of our solutions are reducible, then we can remove the reducible configurations from our configuration space. 

Proposition 1.2.7 

> Removing Reducible Solutions

Suppose we have a spin structure ˜P → M , and we know additionally that • b+ 

> 2

(M ) > 0.

• c1(L) is not a torsion homology class. Then for a generic metric on M , there are no reducible solutions to the Seiberg-Witten Equations 

Definition 1.2.8 

> Quotient Configuration Space

Define the quotiented Seiberg-Witten configuration space to be 

˜C( ˜P ) ∶= C( ˜P )~G ˜P ).

> V.2014/11/17.09:25:57

6 The Seiberg-Witten Invariants 

The irreducibe Seiberg-Witten configurations are defined to be 

˜Cirr ( ˜P ) ∶= (C( ˜P ) ∖ { Reducible Configurations })~G ˜P ).

The Seiberg-Witten moduli space associated to a Spin c structure ˜P → M is defined to be 

MSW ( ˜P ) ∶= F −1(0) ⊂ ˜C( ˜P ).

As mentioned above, the obstruction from the quotient being a smooth manifold is these reducible configura-tions. While there are a lot of technical details to check (in particular, showing that ˜C( ˜P ) is Hausdorff) one can show the following: 

Proposition 1.2.9 The reduced configuration space ˜Cirr ( ˜P ) is a Hilbert manifold, with tangent space at [A, φ ] isomorphic to 

W 2,2 ( T ∗M ⊗ iR) ⊕ S+( ˜P ) ~ Im (2d, − ⋅ φ)

In the case where b+ 

> 2

(M ) > 0 and c1(L) is not a torsion cohomology class, the Seiberg-Witten moduli space is the preimage of 0 in ˜Cirr ( ˜P ).

## 1.3 The Seiberg-Witten Moduli Space 

In this section, we will want to prove two fact about MSW ( ˜P ). We will make the assumption that b+ 

> 2

(M ) is greater than 0, to remove reducible solutions. 1. Our first goal will be to get an idea of the dimension of this space. 2. We will also want to show that this space is compact. We will then look at a slight variation of the Seiberg-Witten Moduli space, to finally show 3. For generic perturbations, MSW ∗ 

> η

( ˜P ) is a smooth manifold We will focus on proving the compactness and smoothness result. For dimension, we can use the Atiyah-Singer index theorem to prove the following claim. 

Claim 1.3.1 Let (A, φ ) ∈ M SW ( ˜P ) be an irreducible solution. Then the dimension MSW ( ˜P ) around 

(A, φ ) is given by 

d = ( c1(L) 2 − 2χ(M ) − 3 sgn (M ))~ 4.

1.3.1 Compactness of MSW ( ˜P )

Definition 1.3.2  

> Palais-Smale Condition

Let Y be a Hilbert manifold with the action of a Lie group G and a smooth functional f ∶ Y → R which is 

G-invariant. Then f is Palais-Smale if for any sequence {xk} ⊂ Y such that 1. f (xk) is bounded and 2. df (xk) → 0 as k → ∞ 

there exists a subsequence {x′

> k

} and a sequence {gk} ⊂ G such that gkx′ 

> k

→ x with df (x) = 0 and 

f (x) = lim k f (xk).Here is the theorem that we want to prove. 

Theorem 1.3.3   

> Compactness of
> MSW (˜P)

Given a sequence (An, φ n) of solutions to the Seiberg-Witten Equations, there exist gauge transforma-tions σn such that 

σn(An, φ n)

> V.2014/11/17.09:25:57

1.3 The Seiberg-Witten Moduli Space 7

has a smoothly convergent subsequence to a Solution of the Seiberg-Witten equations. The meat of this prove relies on proving bounds on the Seiberg-Witten equations. 

A priori bounds on curvature 

To show compactness of the Moduli space of the Seiberg-Witten equations, we use a bound on the curvature. From an earlier section, we know that we can write the square of the Dirac operator in its Weitzenbock presentation Proposition ?? . We start by bounding the norm of the Seiberg-Witten equations, first by bounding the norm of F +

> A

. From here, we can try and get a bound on the norms of the solutions. 

Lemma 1.3.4 

> Curvature Identity to SW Equations

If (A, φ ) is a solution to the Seiberg-Witten equations, then we have that 

Y∇ A(φ)Y 2 

> L2

+ 14 ⟨κφ, φ ⟩L2 + YφY4

> L4

4 = 0

The proof is just a standard application of the Weitzenbock presentation, then you reexpress the curvature in terms of the spinor field using the Seiberg-Witten equation. We can naturally extend these estimates to create a bound for the Seiberg-Witten solutions in terms of the maximal curvature of M .

Lemma 1.3.5 

> Curvature Bounds for SW Equations

Let (A, φ ) be a solution to the Seiberg-Witten equations. Then for every point x ∈ M we have that 

Sφ(x)S ≤ κ−

> M

SF +

> A

(x)S ≤ κ− 

> M

~2

Where κ− 

> M

is the maximal curvature over all of M

Notice that if the maximal negative curvature is 0, there are no solutions to the Seiberg-Witten Equations. 

... And now a bound on the norm 

In general we are not able to show that the space of solutions to the Seiberg-Witten equations is compact. While the curvature is bounded, changes of gauge allow you to “escape” this compactness and find a set of solutions that do not converge. However, when quotient out by the action of the gauge group, we have enough symmetry to get compactness of the Seiberg-Witten moduli space. The argument to get a bound on 

A is gauge fixing argument and we only sketch an outline here. Fix a smooth connection A0. Given any other connection A on L, there exists a gauge transformation σ ∈ G( ˜P ) such that 

d∗(A − σdσ − A0) = 0

The coclosedness of the gauge allows us to pick a preferential gauge to work in; we will then bound the curvature with respect to that gauge. There exists a change of gauge with d∗(σ(A) − A0) = 0 and 

Yσ(A) − A0Y2  

> Wl, 2

≤ CYF +

> A

Y2 

> Wl−1,2

Putting together these bounds gives us the following restriction on the behavior of the Seiberg-Witten functional 

Corollary 1.3.6 

> Seiberg-Witten Coerciveness [5]

The Seiberg-Witten functional is coercive, that is, there exists constant c > 0 such that 

SW (A, φ ) ≥ c−1(Y σ−1φYW 1,2 + Y σ(A)Y W 1,2 − c

...and now putting it all together. 

We are now ready to put together a proof of the convergence result. 

> V.2014/11/17.09:25:57

8 The Seiberg-Witten Invariants 

Theorem 1.3.1. By the above section, we may assume that the sequence is that of coclosed one forms. This gives us that 

d∗FAn =( d + d∗)FAn

d∗dF An =( dd ∗ + d∗d)FAn

By coercivity of the Seiberg-Witten functional, we may additionally assume that (up to another gauge transformation) that the W l, 2 norms of φn and An − A0 are bounded for some fixed A0. Since W l, 2

embeds into Cl−2, we have that all of the continuous norms are bounded, and we may take a convergent subsequence. ∎

One can modify this proof slightly to get that the Seiberg-Witten functional satisfies the Palais-Smale properties. As a corollary we get 

Corollary 1.3.7 Let ˜P → M be a spin-structure on a manifold. Then MSW ( ˜P ) is compact. 

1.3.2 The Perturbed Moduli Space 

It isn’t always the case that MSW ( ˜P ) is a smooth manifold, in fact, we can only generically hope for it to be some choice of perturbation. In order to make this a smooth space we use the standard pertubation trick and a tranversality argument on generic sections. In order to have all of our derivatives work in the future, we will give ourselves a bit of extra regularity in the perturbation. Instead of working with the Seiberg-Witten functional, we will work with the perturbed Seiberg-Witten functional. 

Definition 1.3.8 Define the ( η)-perturbed Seiberg-Witten Equations to be the map 

F ∶ C 4( ˜P ) × W 3,2(Λ2

> +

T ∗M ⊗ R) → W 3,2(( Λ2

> +

T ∗M ⊗ R) ⊕ S−( ˜P )) 

Fη (A, φ ) ↦( F + 

> A

− q(φ) + iη, ~∂A(φ)) 

where C4( ˜P ) is the configuration space with W 4,2 regularity. Let η be a self-dual real 2-form. The associated Perturbed Seiberg-Witten Functional is given by 

SW η (A, φ ) ∶= S M

(S ~ ∂AφS2 + s

4 SφS2 + 12 S 12 q(φ) − cl (iη )S 2 + S FA + 2iη S2

Redefine the gauge group to have extra W 5,2 Sobelov regularity to act on the Perturbed Seiberg-Witten configuration space. By adding in this small perturbation parameter, we can use a Sard’s theorem type of argument in the section parameter to find a zero section that is smooth. 

Lemma 1.3.9 Suppose that (A, φ ) is a solution to the η-perturbed Seiberg-Witten equation. Then at (A, φ, η ) the differential DF is onto. The surjectivity of this differential is the kind of result that will allow us to make a transveraslity argument for the intersection with the zero section to be a smooth manifold. Note in the case where we have b+ 

> 2

(M )

greater than 0, we had no reducible solutions. 

Corollary 1.3.10 Let MSW −( ˜P ) be the space of irreducible perturbed solutions (up to gauge action) to the Seiberg-Witten equations. This space is a smooth submanifold of Cirr, 4( ˜P )~G × W 3,2(Λ2

> +

T ∗M ⊗ R).The proof of this corollary is by using the Atiyah-Singer index theorem to compute the index of the Fredholm operator associated to the elliptic complex given by the transveraslity result. 

> V.2014/11/17.09:25:57

1.4 The Seiberg-Witten Invariants 9

This space is far too large—it not only contains the solutions to the Seiberg-Witten equations, but a solution for every single perturbation. We would like to look at the solution above a single perturbation. This is going to be the final form of the moduli space of solutions that we are interested in . 

Definition 1.3.11 We have a projection from Cirr, 4( ˜P ) × W 3,2(Λ2

> +

T ∗M ⊗ R) → W 3,2(Λ2

> +

T ∗M ⊗ R) which is a smooth mapping. We denote the fiber over a perturbation η by MSW η , the η-perturbed moduli space .

Theorem 1.3.12 For generic η, we have that MSW η ( ˜P ) is a smooth submanifold of Cirr, 4( ˜P )~G of dimension 

c1(L) 2 − 2χ(M ) − 6(σ(M )) 

4

> Wrapping it up

Let’s throw together all of the results from this section into one giant theorem. 

Theorem 1.3.13  

> Properties of MSW η

Let M be a smooth oriented 4 Riemannian manifold with Spin c structure ˜P → M . Additionally, suppose that b+ 

> 2

(M ) > 0. Then for generic choice of η a self dual real two-form, we have that MSW η ( ˜P ) is an oriented compact manifold of dimension 

c1(L) 2 − 2χ(M ) − 6(σ(M )) 

4 .

With this in hand, we are ready to proceed to the production of the Seiberg-Witten invariants. 

## 1.4 The Seiberg-Witten Invariants 

With our construction of the perturbed moduli space to the Seiberg Witten equations, we are ready to actually go ahead and define the Seiberg-Witten invariants. Now that we have constructed these very nice moduli spaces MSW ( ˜P ), we would like to use them as invariants of a manifold M . However, these moduli spaces were constructed with a number of different choices, most importantly; • The choice of Spin c structure ˜P

• The choice of metric g

• The choice of pertubation. It turns out that only the first choice makes any difference, but the space of Spin c structures is fairly nice. As mentioned before, the Spin c structures form an H2(M, Z) torsor, so the Seiberg-Witten invariants that we are going to construct will give us an assignment 

SW ∶ Spin c(M ) → Z.

However, the choices of g and of pertubation do change the structure of the moduli space. However, these changes will induce a cobordism on the moduli spaces of solutions, and so an invariant that captures the cobordism type of MSW ( ˜P ) will be our invariant. How can we do this? We know that the Chern numbers of certain bundles over a manifold are dependent only on the cobordism type of the manifold; we therefore expect to look for things like this to define our Seiberg-Witten invariant. Our construction of the invariant will therefore come in two parts: showing that the moduli spaces of solutions actually are cobordant, and picking out an appropriate bundle to do this characteristic class construction. 

> V.2014/11/17.09:25:57

10 The Seiberg-Witten Invariants 1.4.1 The Invariant 

There are several ways to pick different characteristic classes to integrate and construct an invariant, but this is the one that we are going to pick. 

Definition 1.4.1 Let MSW ( ˜P ) be the moduli space of solutions to the Seiberg-Witten eqautions, with b+ 

> 2

> 1 so we have no reducible solutions. • In the case where dim (M SW ( ˜P )) < 0, define SW ( ˜P ) = 0.• In the case where dim (M SW ( ˜P )) = 0, define SW ( ˜P ) to be the signed count of points in MSW ( ˜P )

with orientation. • In the case where dim (M SW ( ˜P )) > 0, define 

SW ( ˜P ) ∶= S MSW 

c1(L) d

> 2

where L is the determinant bundle given by the bundle MSW − → M SW η .These invariants are independent of choice of metric on M and pertubation η. Given two metrics g0 and g1

and pertubations, a generic homotopy between g0 and g1 induces a cobordism between the associated moduli space of solutions to the Seiberg-Witten equations. Since the integral of characteristic classes is dependent only on cobordism type, this shows that SW ∶ Spin c → Z is a well defined invariant. 

## 1.5 Seiberg-Witten over Symplectic Manifolds 

In this section we explore how a J-holomorphic structure on a manifold induces adds additional structure to Spin structures and how we can express the Seiberg-Witten equations in these cases. A short over view of notation. 

Definition 1.5.1 Let M 2n be a manifold. An almost complex structure on M is a bundle map J ∶ T M → T M such that 

J2 = − 1. . We say that J is compatible with a metric g on M if J is an orthogonal transformation on the tangent spaces with respect to g.This gives us a decomposition of the complexified exterior bundle into holomorphic and antiholomorphic forms. 

ΩkM ⊗ C = k

?

> i=0
> i

 T 1,0 ⊗ k−i

 T 0,1

which is now equipped with a holomorphic and antiholomorphic differential, d and ¯d.One interesting property of the complex valued forms is the amount of flexibility we have for raising and lowering the degree of forms. On the one hand, we can raise the degree of a form by multiplication. In the other direction, we can lower the degree of a form either by taking interior multiplication with the metric, or by taking on the of the canonical projections to the holomorphic or antiholomorphic parts, it turns out that it is possible to encode the Clifford multiplication structure by using these operations. 

Proposition 1.5.2 If (M, g ) is a Riemannian manifold equipped with compatible J-holomorphic structure, then we can create a spin structure with the following • The Spin bundle is identified with the complex (0, q ) forms. • The positive spinor representation is identified with the even (0, 2q) forms. • The negative spinors are identified with the odd (0, 2q + 1) forms. 

> V.2014/11/17.09:25:57

1.5 Seiberg-Witten over Symplectic Manifolds 11 

We additionally can explicitly express the Clifford multiplication of T M on Λ(0,q ) 

> C

T ∗M as follows: 

v ⋅ μ = √2(π0,1(v∗) ∧ μ − ιπ0,1(v∗)μ)

This happens to be the spinor representation associated with the canonical bundle. One can check in this case, the Dirac operator can be replaced with 

~∂A(σ)( p) = √2( ¯∂(σ)( p) + ¯∂∗σ(p)) .

Furthermore, we can represent spinor fields σ as (α, β ) where α is a section of Ω0(M ) and β is a section of 

Ω0,2(M ).This gives us one example of a spin structure over a manifold with almost complex structure; how do we get the other ones? Given a Spin c bundle, we can take describe the positive spinor bundle as follows: 

Proposition 1.5.3 Let P → M be the Spin c structure associated to complex line bundle E. Then we can identify the positive spinors with 

S+ = E ⊕ ( K−1 ⊗ E)

If we pick a section u0 of the canonical bundle, then we can pick a compatible spin covariant derivative A0

by taking DA0 u0 = 0. We have from before that the set of Spin c structures is a H2(M, Z) torsor. However when we pick out a canonical element of the Spin c structures, we can actually identify the set of spin structures with H2(M, Z). We should therefore interpret the Seiberg Witten invariants not a function from Spin structures to Z, but instead as 

SW ∶ H2(M, Z) → Z.

The symplectic form also allows for a nice choice of perturbation factor η. We can give a real parameterization to a perturbation factors by writing them as 

η = − i ⋅ r

4 ω + F +

> A0

where A0 is the canonical connection associated to the bundle. With this choice of perturbation, we have that the Seiberg-Witten equations are given by 

~∂(φ) = 0

F + 

> A

= F + 

> A0

+ q(φ) − irω 

If we choose to represent the spinor field in terms of the decomposition of Proposition 1.5 then we can write 

φ = r 12 (αu 0 + β)

where α is a section of E and β is a section of K−1 ⊗ E. Then we can write the Seiberg-Witten equations as follows 

Claim 1.5.4 The solutions to the perturbed Seiberg Witten equations are equivalent to finding solutions for a parameter r to the symplectic Seiberg Witten equations. 

σ(u0 ⊗ ∇ aα) + DAβ = 0

F + 

> a

= −i

8 r(1 − S αS2 + S βS2) ⋅ ω + ir 

4 (αβ ∗ + α∗β)

We therefore can define the r-perturbed moduli space of solutions to be MSW r ( ˜P ). This is a smooth compact manifold for generic r.

> V.2014/11/17.09:25:57

# Taubes’s Gromov Invariant 

In this exposition, we will take the approach used by Taubes in his paper [14]. Given a symplectic manifold M , one can look at the number of pseudoholomorphic curves which intersect a specified homology cycle in M . This general idea gives you a mapping from Φ ∶ H2(M, Z) → Z by taking a signed count of these curves. There are some principle differences between Taubes’s Gromov invariant and the Gromov-Witten invariant. The biggest change is the Taubes considers pseudoholomorphic submanifolds independent of parameterization. Here is an outline of how we define Taubes’s Gromov Invariant • We start with a bit of background on pseudoholomorphic curves. Section 2.1 covers the basic definitions and constructions. Of particular interest is the construction of the moduli space of J holomorphic curves, and the evaluation map of this moduli space. We show that this map is a pseudocycle and therefore represents an element of homology. This construction allows us to count the number of pseudoholomorphic curves that pass through k generic points. • In Section 2.2 on page 20, we define Taubes’s Gromov invariant, modulo some cases involving counting multiply covered torii. The majority of this section is devoted to showing that it is well defined. • We leave off the more complicated case of counting multiply covered torii. 

## 2.1 Background on Pseudoholomorphic Curves 

McDuff has a number of great resources for learning more about Pseudoholomorphic curves, our primary reference here is [7] and [6]. Before we can get into developing Taubes’s Gromov invariant, we start with some basic definitions for Pseudoholomorphic curves. 

2.1.1 Almost Complex Structures Definition 2.1.1 Let (M 2n, ω ) be a symplectic manifold with almost complex structure J. Then we say that J is ω-compatible if 1. g(v, w ) = ω(v, Jw ) is a Riemannian metric. 2. ω(Jv, Jw ) = ω(v, w )

If J satisfies the weaker property that ω(v, Jv ) > 0 whenever v ≠ 0, then we say that J is ω-tame .For example, M = Cn with the standard two form and standard J-structure has ω-compatibility. 

Exercise 2.1.2 For any p ∈ M , we can choose a basis for TpM in which ω, J, g are standard. Notice that property 2 gives us that g is symmetric. 

g(w, v ) = ω(w, Jv )=ω(− J2w, Jv )=ω(− Jw, v )=ω(v, Jw )=g(v, w )

When we have that J is ω-tame, we can get a Riemannian metric by taking 

g(v, w ) = 12 (ω(v, Jw ) + ω(w, Jv )) 

> V.2014/11/17.09:25:57

2.1 Background on Pseudoholomorphic Curves 13 

Notice in the case where J is ω compatible this simplifies to the metric that we had above. When we are talking about J-holomorphic curves, we will want to use (tame or) compatible J.

Proposition 2.1.3 The set of ω-compatible almost complex structures J on M is nonempty and contractible. Moreover, any 

ω-compatible almost complex structure or homotopy of ω-compatible almost complex structures on a compact subset of M can be extended over M .This follows from the following lemma: 

Lemma 2.1.4 Let (V, ω ) be a symplectic vector space. Let Jc(V, ω ) be the linear maps J such that J2 = − 1 and J is 

ω-compatible. Then Jc(V, ω ) is contractible. 

Proof. Done in the class! ∎

The proposition also holds with “compatible” replaced by the word “tame”. 

Exercise 2.1.5 If dim V = 4, then g comes from an ω compatible almost complex structure J if and only if ω is self-dual with respect to g and SωS = √2.

2.1.2 J-holomorphic Curves Definition 2.1.6 A Riemann Surface is a closed, connected two dimensional manifold Σ with an almost complex structure 

j. The genus of Σ is the number of holes in the surface. Given (M, ω, J ), a J-holomorphic curve 1(Σ, j ) → ( M, J ) is a smooth map u ∶ Σ → M such that 

J ○ du = du ○ j

People go bananas over pseudoholomorphic curves. Here are a few examples. Let (M, ω, J ) be symplectic manifold with almost complex structure. 1. The constant map is a pseudoholomorphic curve. 2. If Σ ⊂ CP 2 is a nonsingular algebraic curve then the inclusion map is holomorphic. 3. If M = Σ × N and Jm = j ⊕ JN for each p ∈ N , then Σ → M is holomorphic. In general we are going to be interested in counting the number of pseudoholomorphic curves that pass through some prespecified number of sets. 

Definition 2.1.7 Let (M, ω, J ) be a compact symplectic manifold. Let A ∈ H2(M ). Then define the moduli space of genus g J -holomorphic curves in A to be 

Mg (A) ∶= { u ∶ Σ → M Su is J-holomorphic }

where Σ is a closed Riemannian surface with almost complex structure j, and u ∶ Σ → M a map with 

J ○ du = du ○ j and u∗[Σ] = A.It is tricky to count the curves in Mg (A), because you can sometimes take a curve and then get a new one by factoring through a branched cover. Clearly, these should be counted in a different way, otherwise you could build an infinite number of such curves by simply taking more and more branched covers. What do we know about Mg (A) in general? We have this general properties of J holomorphic curves, 

> 1Also called a pseudoholomorphic curve or holomorphic curve
> V.2014/11/17.09:25:57

14 Taubes’s Gromov Invariant Theorem 2.1.8  

> Adjunction Formula

If C is a genus g holomorphic curve in the class of A, then 

A ⋅ A = c1(A) + 2(g − 1) + 2m

where m is the number of double points. 

Proof. First let us suppose that C is immersed. Then we have that the first Chern class of A is given by 

c1(A) = c1(T M, J )( C)=c1(T C )( C) + c1(N C )( C)

The Chern class is related to the genus, while generic sections of the normal bundle has zeros related to the homology class that C represents, and the number of double points of the map C

=2 − 2g + C ⋅ C − 2m

∎

While the general moduli space of parameterized J-holomorphic curves is a little difficult to get a hand on because many times the parameterization can be factored through another parameterization. We are not interested in such representations, so we will simplify by discounting them. 

Definition 2.1.9 A holomorphic map i ∶ ( Σ, j ) → ( M, J ) is somewhere injective if there exists z ∈ Σ such that 

u−1(U (z)) = { z} and du ∶ Tz Σ → Tu(z)M is injective. We say that u ∶ ( Σ, j ) → ( M, j ) is Multiply covered if there exists a branched over ρ ∶ Σ → Σ′ of degree 

d > 1 and a holomorphic map u′ ∶ ( Σ′, j ′) → ( M, J ) such that u = u′ ○ ρ

In other words, a map is multiply covered if you can factor it through a branched cover, and somewhere injective means that there is a disk for which your map is an embedding. Notice that the image of every multiply covered curve can be represented by the somewhere injective curve that it factors through, therefore if we are only interested in the number of unparameterized J-holomorphic curves, we may “throw out” all of the multiply covered parameterizations. 

2.1.3 The moduli space of somewhere injective holomorphic curves 

Introduction 

To prepare to understand the overall story, it would be better for you to know Fredholm theory and Atiyah-Singer index theorem (or Riemann-Roch theorem). Basically, what we are going to discuss is that 

H( A, J )

is a smooth manifold of dimension n(2−2g)+ 2c1(A) where A is an element of H2(M ; Z).

Definition 2.1.10   

> The moduli space of somewhere injective
> J-holomorphic curves with 2nd homology A

H( A, J ) = { u ∶ Σ → M S u(Σ) is somewhere injective J-holomorphic and u∗[Σ] = A ∈ H2(M ; Z)} 

Fredholm theory 

One of main ingredients for studying the moduli space H( A, J ) is Fredholm theory. Let’s see what Fredholm theory is, briefly. Suppose that we have an operator f ∶ X → Y where X and Y are Banach spaces. A 

Fredholm operator is a bounded linear operator whose kernel and cokernel are finite-dimensional and 

range is closed . For such an operator we define the index of the operator ind f by ind f = dim ker f − dim coker f. 

> V.2014/11/17.09:25:57

2.1 Background on Pseudoholomorphic Curves 15  

> A fredholm operator ¯∂J

Let’s first think about what H( A, J ) is. Basically, it is a subset of all smooth maps u ∶ Σ → M such that u

is J-holomorphic. It means that du has no complex anti-linear part. Hence, if we define a map ¯∂J which represents the complex anti-linear part of du then H( A, J ) will be ker ¯∂J . From here, we can get some help from Fredholm theory! So, let’s move on to defining an appropriate Fredholm operator ¯∂J .Let’s define M( A) as a space of all smooth maps u ∶ Σ → M which are somewhere injetive and u∗[Σ] = 

A ∈ H2(M ; Z). This space can be interpreted as an infinite dimensional manifold of which tangent space at each point (which is a function u) is the space of all smooth vector fields on u(Σ),

TuM = C∞(u∗T M ).

Next, consider a vector bundle ∶ E → M such that 

> −1

(u) = { smooth J-anti-linear 1-forms with values in u∗T M }.

Then, we have a section ¯∂J ∶ M → E which maps u to the complex anti-linear part of du . As we have discussed just before, H( A, J ) = ¯∂−1 

> J

(0).We want H( A, J ) to be a manifold and it requires ¯∂J be transversal to the zero section. For the next, let’s define Du = πu ○ d ¯∂J ∶ TuM → T(u, ¯∂J (u)= 0)E → −1(u) so that Du is an operator from C∞(u∗T M ) to the space of complex anti-linear 1-forms with values in u∗T M . Then the trasversality condition is equivalent to that Du is surjective at the point u where ¯∂J (u) = 0.Basically, through computation, we can figure out that Du is an elliptic first order partial differential operator and such kind of operator is always Fredholm. From PDE theory, we have a series of claims about this operator 

Claim 2.1.11 Consider the operator Du ∶ C∞(u∗T M → Ω0,1(u∗T M ) as above. • Du is an elliptic first order PDO. • C∞(u∗T M ) and Ω0,1(u∗T M ) are complex vector spaces. • The antilinear part of Du is order 0, so Du has the same index as a Cauchy-Riemann operator. • The set of almost complex structures J such that Du is onto is generic. Also we have a lemma stated as below.[6] 

Lemma 2.1.12 Let u ∶ Σ → M be a smooth map and Qu ∶ C∞(∧ 0,1T ∗Σ ⊗J u∗T M ) → C∞(u∗T M ) be a right inverse of Du such that 

SS QuSS ≤ c0, SS du SS Lp ≤ c0, SS ¯∂J (u)SS Lp ≤ δ

with respect to a metric on Σ such that vol (Σ) ≤ c0. Then for every ξ ∈ ker Du with SS ξSS Lp ≤ δ there exists a section ˆξ = Quη ∈ C∞(u∗T M ) such that 

¯∂J (exp u(ξ + ˆξ)) = 0, SS ˆξSS C∞ ≤ cSS ¯∂J (exp u(ξ))SS Lp .

(Here, p can be any value > 2.) In words, what the lemma implies is that for a given small section ξ of C∞(u∗T M ) which is in the kernel of 

Du, we can find a unique ˆξ ∈ im D∗ 

> u

such that ξ + ˆξ (∈the tangent space TuM) makes u to be a J-holomorphic curve via the exponential map defined on M. In mathematical expression, we have found a smooth map 

ker Du → im D∗

> u

which help ξ ∈ ker Du make u a J-holomorphic curve. The next lemma we would like to use is 

> V.2014/11/17.09:25:57

16 Taubes’s Gromov Invariant Lemma 2.1.13 Under the same assumption as before with 

SS QuSS ≤ c0, SS du SS Lp ≤ c0,

if v0 = exp u(ξ0) and v1 = exp u(ξ1) are J-holomorphic curves such that ξ0, ξ1 ∈ C∞(u∗T M ) satisfy 

SS ξSS W 1,p ≤ δ, SS ξSS W 1,p ≤ c0,

and 

SS ξ1 − ξ0SS Lp ≤ δ, ξ1 − ξ0 ∈ im Qu,

then v0 = v1.Using this lemma, we can now conclude that every J-holomorphic curve v, which is bounded in W 1,p and sufficiently close to u can be uniquely expressed as 

v = exp u(ξ + ˆξ)

for some ξ ∈ ker Du. So far we have just given a local chart from ker Du to H( A, J ) so that H( A, J ) is a manifold. Now, we get the dimension of H( A, J ) agreeing with dim ker Du which is finally ind Du since 

Du is onto. Now, by Atiyah-Singer index theorem or Riemman-Roch theorem, dim H( A, J ) = ind Du =

n(2 − 2g) + 2c1(u∗T M ).For smoothness of the manifold we can use this argument : for a generic choice of J, we have ¯∂−1 

> J

(0) asmooth manifold by the infinite dimensional version of Sard’s Theorem (Sards-Smale Theorem). Therefore, the moduli space H( A, J ) is a smooth manifold of dimension n(2 − 2g) + 2c1(u∗T M ).

Definition 2.1.14 Define the moduli space of somewhere injective holomorphic curves to be 

M∗ 

> g

(A) = { φ ∈ Hom (Σg , M ) × T g S (∗)} 

where the conditions (∗) are • If we give Σ the complex structure τ , then φ ∶ Σg → M is J-holomorphic. • The map φ is somewhere injective. • φ(Σ) represents the homology class A.This space is much nicer to work with. The benefit of using the multiply covered curves is that we (generically) get a manifold out of this moduli space. If we don’t use these equivalence classes, these moduli spaces look like manifolds of various dimension that touch each other— with each component corresponding to curves of different multiplicity in branching. It should be noted that we introduce a different problem at tis point, in that some sequences of parameterizations of tori can converge to a multiply covered torii, but we will not discuss that at all. We would like to study properties like the dimension of this manifold– before we can get there, we should look at the ways that we can represent different elements of M∗ 

> g

(A) by reparameterization. 

Definition 2.1.15 Given a Riemann surface Σg , let Tg denote the Teichmüller space of Σg , the set of all complex structures taken up isotopy. It is a common result [10] that the Teichmüller space of a manifold has dimension 

dim R Tg = 6g − 6

and that we have a smooth mapping from the Teichmüller pace to the set of j-holomorphic structures on 

J .

> V.2014/11/17.09:25:57

2.1 Background on Pseudoholomorphic Curves 17 

Definition 2.1.16 Given a Riemann surface Σg , let Gg be the reparameterization group. We can actually compute these explicitly to begin with: • if g = 0, we have that reparameterization is given by PSL (2, C)

• if g = 1, we have that we can reparameterize by SL (2, Z) extended by the torus. • otherwise, Gg is the mapping class group π0(Diff (Σ)) .

Theorem 2.1.17 For generic ω-tame J, the moduli space M∗ 

> g

(A) is an oriented manifold of real dimension 

dim R(M ∗ 

> g

(A)) = 2(c1(A) + g − 1) + dim Gg

Proof. 

dim M∗ 

> g

(A) = dim H( A, J ) + dim Tg + dim Gg = 2c1(A) + 2g − 2 + dim Gg

∎

Corollary 2.1.18 If l = lg (A) = c1(A + g − 1), there is a evaluation mapping 

ev ∶ M ∗ 

> g

(A) × Gg Σl →M l

(φ, τ, z 1, . . . z l) ↦( φ(z1), . . . , φ (zl)) 

between manifolds of equal dimension 4l.

Proof. This is just a dimension count. ∎

What we would like now is a statement along the lines of “the number of curves (counted with sign) that pass through l generic points is given by the degree of the mapping ev .” This would tell us that the choice of 

l points is not consequential and that we’ve actually defined an invariant of the manifold. However, the space 

M∗ 

> g

(A) is not compact, and therefore the degree of the mapping is not well defined. The failure to M∗ 

> g

(A)

being compact is due to the possible convergence of J-holomorphic curves to “cusp curves” This is summed up in the following theorem 

Theorem 2.1.19  

> Gromov’s Compactness

Assume that (M, ω ) is compact, and let Ji be a sequence of J holomorphic structures compatible with ω.Then any sequence of Ji holomorphic spheres converges weakly up to cusp curves. In order to actually study this manifold M∗ 

> g

(A) properly, we will want to work with its compactification, which may include cusp curves. Then we will be able to introduce an idea of degree which is compatible with our notion of degree for maps but works for compact manifolds with boundary. 

2.1.4 Cusp Curves 

For this section we will restrict to looking at the moduli space of genus 2 curves. 

Definition 2.1.20 Let (M, ω ) be a compact symplectic manifold with ω-tame almost complex structure J. A cusp curve is a connected union C = ⋃ ni=1 Cj of J holomorphic spheres. We can think of cusp-curves as being like a necklace of spheres that are just about to come apart. The reason to introduce cusp curves is to compactify the space of J-holomorphic curves. For instance, one can take the 

> V.2014/11/17.09:25:57

18 Taubes’s Gromov Invariant 

curves converging as follows: The curves on the left may be J-holomorphic, but the curve on the right is a cusp curve. We can parameterize cusp curves in two different ways. The first is to provide a J-holomorphic parameteri-zation for each sphere on the curve. In this way, we represent the cusp curve as a collection of functions 

ui ∶ CP 1 → M .A second way to parameterize the cusp curve is with a single function. Notice that every singe cusp curve can still be parameterized as a smooth map from a connected domain to M , but this map will necessarily not be J-holomorphic. Both of these characterizations of cusp curves is useful in defining what it should mean for a series of J

-holomorphic curves to converge to a cusp curve. 

Definition 2.1.21 Let uj ∶ CP 1 → M be a sequence of J-holomorphic curve, u ∶ CP 1 → M be a smooth parameterization of the cusp curve, and ui ∶ CP 1 → M be its associated J-holomorphic parameterization. Then we say that uj

converges to u if it converges in both of the following senses: • ( J-holomorphic convergence) We have associated fractional linear transformations φij and finite sets 

Xj such that uiφji converges to φi uniformly on all derivatives over all compact sets of CP 1 ∖ Xj .• (Smooth Convergence) There exists diffeomorphisms fi ∶ CP 1 → CP 1 such that uifi converges to 

u in the sup-norm topology. We should expect that the space of cusp curves that pass through k generic points to have real dimension 2 less than the space of J-holomorphic curves that pass through k points, because we are imposing the additional condition on these curves that they are also connected to each other. The second reason that we would expect the cusp curves to have a smaller dimension than the pseudoholomorphic curves is because we think of them in some way as the limit of pseudoholomorphic curves that are about to bubble off. We will represent these cusp curves by the homology class that each bubble has along with which bubbles it is connected to; this is called the framing data and is denoted 

D = ( A1, . . . A N , j 2, . . . j N )

where the Ai denotes the homology class of the ith bubble in the cusp curve, and ji denotes that the i and j

bubbles share a point in common. 

Theorem 2.1.22 Let M( D, J ) be the moduli space of cusp curves that fit the framing D. For generic J we have the dimension of this space is 

M( D, J ) = 2

> N

Q

> j=1

(c1(Aj ) + 2n + 4(N − 1)

While M( D, J ) is not codimension 2 with respect to M( A, J ), when we look at the evaluation map, we notice that the fiber product will cut down the dimension a lot. Therefore when we look at unparameterized curves, we have that: 

Corollary 2.1.23 In the case of dimension four, the space of cusp curves is codimension 2 in the compactification of 

Mg (A) × G Σl.This means that the “boundary” of the compactification of moduli space of pseudoholomorphic curves is not very big; this stratification will be extremely useful for us when we want to talk about the homological properties of the evaluation map. 

> V.2014/11/17.09:25:57

2.1 Background on Pseudoholomorphic Curves 19 

2.1.5 Evaluation Mapping and Pseudocycles 

In order to understand the number the number of pseudoholomorphic curves that have image containing a specified number of generic points, we will look at the evaluation mapping for Pseudoholomorphic curves. 

Theorem 2.1.24 The evaluation map represents a class in homology, whose multiplicity counts the number of curves passing through a generic point in M l.This will give us the corollary that allows us to count these curves. 

Corollary 2.1.25 Given a generic set of points (x1, . . . x l) ∈ M l, the preimage ev −1(x1, . . . , x l) is finite. If A is sufficiently nice 2then the number of points in the inverse image is independent of choice of J.Since the manifold M( A, J, g ) is only compact with the addition of cusp curves, we cannot use the usual degree of this mapping to count the number of points in the preimage of a generic point in M l. However, we can get a very similar result by introducing the concept of a pseudocycle [7]. 

Definition 2.1.26  

> Pseudo-cycles

Let M be a compact manifold. A k-dimensional pseudo-cycle in M is a smooth map f ∶ V → M where 

V is k dimensional and the boundary of f (V ) is of dimension at most k − 2.

Lemma 2.1.27 In dimension 4, The evaluation map is a Pseudocycle 

Proof. This is immediate from 2.1.4. ∎

Definition 2.1.28 Let f0 ∶ V0 → M and f1 ∶ V1 → M be two k dimensional pseudocycles. Then we say that they are 

bordant if there exists a (k + 1) dimensional oriented manifold W with ∂W = V1 − V0 and an extension of f0 and f1 to F ∶ W → M .

Claim 2.1.29 If M is a compact smooth manifold of dimension greater than three, every element of 

H2(M, Z) can be represented by an embedded surface. We will first show that pseudocycles naturally represent classes of cohomology, and then take the Poincaré dual. 

Lemma 2.1.30 Let e and f be pseudocycles of complementary dimension. Then the intersection number of e and f

depends only on the bordism class of e and f .

Proof. What we will show is that if f is bordant to ∅, then the intersection number of e and f is zero. Let 

F be a bordism between f and the empty set. This bordism can be chosen to be transverse to e, so the intersection of F and e is a 1 dimensional manifold. Then the intersection of e and f is given by the boundary of F ∩ e. The number of signed points in the boundary of a 1 dimensional manifold is zero. ∎

We can use this property to define a class of cohomology for a pseudocycle e. Let e be a (n − d) pseudocycle, and let α ∈ Hd(M, Z) be a class of homology. Then let a be a cycle which represents the element α, and define 

Φ[e](α) ∶= e ⋅ f

to be the intersection number of e and f . Since any two representatives of α are bordant, and intersec-tion number is only defined up to bordism class, this map is well defined and we have that φ[e](α) ∈ 

Hd(M ).           

> 2The conditions here are Acannot be of the form A2=0, A =mB and g=1.
> V.2014/11/17.09:25:57

20 Taubes’s Gromov Invariant Definition 2.1.31 We say that a (m − d) pseudocycle e is a weak representative of αe ∈ Hd(M, Z) if 

PD (Φ[e]) = β

where PD is the isomorphism of Poincaré duality. This formulation of representing homology classes gives us a way to translate between the evalution mapping and homology. In particular, it allows us to define something along the lines of “degree” without having a closed manifold. We have that the number of points in ev −1(x) counted with sign is generically the multiplicity of 

PD (Φ[e]) ∈ H1(M l, Z).

This gives us Theorem 2.1.5. 

## 2.2 Taubes’s Gromov invariant, with Caveats 

We now have a basic understanding of the Moduli space of pseudoholomorphic curves that pass through a specified number of generic points. In order to define Taubes’s Gromov invariant, we will count the number of curves that pass through these points in a specified way. 

Definition 2.2.1 Given a symplectic manifold (M, ω ) with compatible holomorphic structure J, a class A , and a set of 

k(A = 12 (c1(A) + A ⋅ A) points Ωk, define the set of J- holomorphic curves passing through Ωk to be the set 

H( A, Ωk) ∶= {( φ ∶ Σ → M S (∗)}~ ∼ 

Where the conditions (∗) are • The curves φ ∶ Σ → M are J holomorphic (possibly disconnected) curves. • The points Ωk are contained within the image of φ.• The images of each connected component are distinct. • [φ∗(Σ)] = A

We say that two representations of the curve are similar (and write φ ∼ φ′ ) if • φ and φ′ have the same images. • The multiplicity of φ and φ′ restricted to a connected component have the same multiplicity. We denote the equivalence classes (φ, Σ).Roughly, the space H( A, Ωk) denotes the unparameterized pseudoholomorphic curves that pass through the sets Ωk. We should feel like we have a pretty good understanding of this set by thinking about the evaluation mapping from the previous section. There are only a few problems, most of them related to counting the multiplicity of certain mappings. We will need to cover this later, but let us look at the nice case first. 

Definition 2.2.2 Given (φ, Σ) ∈ H( A, Ωk), we say that it is good if φSΣi has multiplicity 1 (i.e. φ(Σi) ⋅ ( Σi) ≤ 0). There are some surprising facts about having good submanifolds representing a class of homology. 

Theorem 2.2.3   

> Structure of
> H( A, Ωk)

For generic ω-tame almost complex structure J on M , and A ∈ H2(M, Z), we have the following characterizations of H( A, Ωk).1. Suppose that (φ, Σ) ∈ H( A, Ωk) is good. Then : (a) Every (φ′, Σ′) ∈ H( A, Ωk) is good. 

> V.2014/11/17.09:25:57

2.2 Taubes’s Gromov invariant, with Caveats 21 

(b) The image of the connected components are disjoint, that is φ(Σi) ∩ φ(Σj ) = ∅ 

(c) The multiplicity of φSΣi is one, unless g(Σi) = 1 and φ(Σi) has no self intersections. (d) H( A) is zero dimensional. 2. If (φ, Σ) ∈ H( A, Ωk), then the image φ(Σi) of every Σi such that φ(Σi) ⋅ φ(Σi) < 0 is an embedded exceptional sphere, with multiplicity possibly greater than 1.The proof of this theorem is mainly due to the evaluation map defined in the previous section. Refer to [11] for the proof of ev −1(x1, ⋯, x k) is compact for a generic choice of (x1, ⋯, x k) and it is an invariant. Now, we will present the definition of Taubes’s Gromov invariant in a special case. 

Definition 2.2.4 

> Taubes’s Gromov invariant

Suppose A ∈ H2(M, Z) is a homology class such that H( A) only contains elements with components of multiplicity 1, then define 

Gr (A) = Q

> (φ, Σ)∈H( A)

(φ, Σ)

where (φ, Σ) is the orientation of the point in H( A).In the case where A can be parameterized by a good surface, then Gr (A) is literally just counting with orientation the number of surfaces that represent this homology class passing through k generic points. From our work with the evaluation mapping before, we should expect this to be a finite number, as the space 

H( A, Ωk) should be identifiable with the preimage of the evaluation mapping. We therefore do not seem to be doing too poorly in the cases where H( A, Ωk) contains a good representative. 

> V.2014/11/17.09:25:57

# SW ⇒ Gromov 

The goal of this section is to show how one can use solutions the Seiberg-Witten equations to construct the pseudoholomorphic curves that are used in Definition 2.2 for the Gromov invariants. Taubes’s pa-per [13] gives a method to construct pseudoholomorphic curves given a sequence of solutions to the Seiberg-Witten equations with varying pertubation parameter. The precise result of Taubes’s paper is the following: 

Theorem 3.0.5 Let M be a compact 4 manifold with symplectic form ω. Let ˜P → M be a Spin c structure with associated complex line bundle L. Let Ωi be a finite set of closed sets, and assume there is an unbounded sequence 

rn for which MSW rn ( ˜P ) has a solution, where α−1(0) ∩ Ωi ≠ ∅ . Then there exists a smooth compact pseudoholomorphic curve that passes through Ωi with φ∗(Σ) equal to the Poincaré dual to c1(L) .In this exposition, we will show that the solutions of the Seiberg-Witten equations give us enough information to construct a 2 dimensional subspace of M . We will not show that the subspace is a submanifold, or even 

J-holomorphic. 

## 3.1 Outline of Proof of Theorem 3 

We would like to show that a sequence of the Seiberg-Witten solutions parameterized by r has a convergent subsequence. However, we are unable to do this for several reasons (the first being, that they do not live in the same space, unless we take parameterized configuration space.) In order to get these sections to converge, we will have to weaken our sense of convergence, and work with currents, instead of differential forms. 

Definition 3.1.1  

> Currents

Let M be a differentiable manifold. A k-current on M is a linear functional from Ωkc (M ). It comes equipped with the mass norm 

SFS ∶= sup 

ω ∈ Ωkc (M )SωS ≤ 1

F( ω)

The reason to use currents is that they have much nicer convergence properties than differential forms. We should think of currents as being the differential form equivalent to distributions. Given a solution to the Seiberg-Witten equations we can translate the data about the connection into a much-better beahved current: 

Definition 3.1.2  

> Associated Current

Let (A, α, β be a solution to the Seiberg-Witten equation. Define the associated current to be the current 

FA(μ) ∶= S i

2π FA ∧ μ. 

Now let’s show how these currents relate to the problem of constructing a surface from solutions to the Seiberg-Witten equations. Recall the Taubes Formulation for the Seiberg-Witten equations over a symplectic manifold 

σ(u0 ⊗ ∇ aα) + DAβ =0

F + 

> a

= −i

8 r(1 − S αS2 + S βS2) ⋅ ω + ir 

4 (αβ ∗ + α∗β)

where we use the decomposition S+ = ( E ⊕ ( K−1 ⊗ E)) so that configurations (a, α, β ) are given by • a is a connection on E

> V.2014/11/17.09:25:57

3.1 Outline of Proof of Theorem 3 23 

• α is a section of E

• β is a section of K−1 ⊗ E

In this equation αβ ∗ and α∗β are sections of K and K−1 respectively. The perturbation parameter r comes from the section of perturbations 

η = −ir 

4 ω + F + 

> A0

+ iη 0

We therefore can define the r-perturbed moduli space of solutions to be MSW r ( ˜P ). This is a smooth compact manifold for generic r. Let’s assume the conditions of Theorem 3, which are a given 1. ˜P → M be a Spin c structure with associated complex line bundle L

2. An unbounded sequence rn of real numbers 3. Ωi, a finite collection of closed sets. with the conditions MSW rn ( ˜P ) has a solution, where α−1(0) ∩ Ωi ≠ ∅ . Then we may construct associated currents to each of these specified solutions, Fn.

Lemma 3.1.3 The sequence of currents is bounded with respect to the mass norm, that is 

YF nYM ≤ 12π YFAn YL1 ≤ [ ω] ⋅ c1(E) + c~r

where C is some constant. This is proven by taking the a priori bounds for the curavture and massaging them to show that they have no 

r dependence. As the mass norm is bounded, we have the foloowing corollary 
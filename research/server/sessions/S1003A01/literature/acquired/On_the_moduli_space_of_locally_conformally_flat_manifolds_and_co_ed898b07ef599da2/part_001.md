---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: On the moduli space of locally conformally flat manifolds and collapsed constant scalar manifolds]

# On the moduli space of locally conformally flat manifolds and collapsed constant scalar manifolds

> Source: https://escholarship.org/content/qt31v740r5/qt31v740r5.pdf
> Fetched: 2026-10-09 09:03
> Method: FULLTEXT_HTML_JINA|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA

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
  "source_url": "https://escholarship.org/content/qt31v740r5/qt31v740r5.pdf",
  "metadata": {
    "provenance_urls": [
      "https://escholarship.org/content/qt31v740r5/qt31v740r5.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "scalar-flat conformally flat asymptotically Euclidean Green function metric insertion smooth point connected sum"
      }
    ]
  },
  "declared_files": [
    {
      "url": "https://escholarship.org/content/qt31v740r5/qt31v740r5.pdf",
      "name": "qt31v740r5.pdf",
      "label": "",
      "role": "primary_object_file",
      "parent_url": "https://escholarship.org/content/qt31v740r5/qt31v740r5.pdf",
      "identity_bound": true,
      "primary_label": false,
      "download_eligible": true
    }
  ]
}
```

## Source description

Theorem 5.2 (VW gluing theorem: collapsing factors ). Let (Zn t , gt) be a collapsing 125 factor with S(gt) ≡v and base point zt. Let (N n, ˆ g) be an asymptotically flat manifold with S(ˆ g) = 0. Suppose the spectral condition of Theorem 4.1 holds on the limit (X, g∞).
Then, for t sufficiently small and suitable gluing parameters a = a(t), b = b(t) with b ≪ injgt(zt), the connected sum Zt#M (where N = M \ {p}, p ∈M) admits a constant scalar curvature metric g′ t such that: (i) S(g′ t) = a2b2v + O(a2+δ) for some δ > 0; (ii) g′ t is N-invariant; (iii) As t →0, the family (Zt#M, g′ t) degenerates: the Zt-factor collapses while the M-factor remains at fixed scale. [...] Proof. By the existence theory for the Green’s function on ALE spaces , for each qi there exists a positive Green’s function Gi for Lg with pole at qi. The superposition H = P i Gi > 0 is a positive solution of LgH = 0 on M \ {qi}, with the leading singularity Gi ∼ci r2−n near each qi resolving the orbifold point into an ALE end. Since Rg ≥0 and LgH = 0 with H > 0, the conformal change formula gives RH4/(n−2)g = H−(n+2)/(n−2)LgH = 0, so the blown-up metric is scalar-flat (in particular R ≥0). An alternative construction is given by Lemma 2.1 of . [...] Let (M, u 4 n−2g) to be the above conformal scalar-flat, ALE metric. We want to relate the mass between (M, u 4 n−2g) and (M, g). Note that we can adjust the scaling such that u solves:      −∆u + c(n)Su = 0 u →1 as |x| →∞ Note that S ≥0. The asymptotic of u i

## Retrieved source content

Title: On the moduli space of locally conformally flat manifolds and collapsed constant scalar manifolds

URL Source: https://escholarship.org/content/qt31v740r5/qt31v740r5.pdf

Published Time: Fri, 29 May 2026 13:35:50 GMT

Number of Pages: 160

Markdown Content:
UC Irvine 

UC Irvine Electronic Theses and Dissertations 

Title 

On the moduli space of locally conformally flat manifolds and collapsed constant scalar 

manifolds 

Permalink 

https://escholarship.org/uc/item/31v740r5 

ISBN 

9798247922315 

Author 

Wang, Xiaokang 

Publication Date 

2026-05-28 

Copyright Information 

This work is made available under the terms of a Creative Commons Attribution License, 

available at  https://creativecommons.org/licenses/by/4.0/ 

Peer reviewed|Thesis/dissertation 

eScholarship.org  Powered by the  California Digital Library 

University of California UNIVERSITY OF CALIFORNIA, IRVINE On the moduli space of locally conformally flat manifolds and collapsed constant scalar manifolds DISSERTATION submitted in partial satisfaction of the requirements for the degree of DOCTOR OF PHILOSOPHY in Mathematics by Xiaokang Wang Dissertation Committee: Professor Jeff Viaclovsky, Chair Professor Richard Schoen Professor Zhiqin Lu Professor Timothy Tait 2026 © 2026 Xiaokang Wang DEDICATION 

To my parents and my partner Wenlin, for their endless love, patience, and unwavering support. ii TABLE OF CONTENTS 

Page 

LIST OF FIGURES vi LIST OF TABLES vii ACKNOWLEDGMENTS viii VITA ix ABSTRACT OF THE DISSERTATION xi Notations 11 Introduction 3

1.1 Background in Riemannian Geometry . . . . . . . . . . . . . . . . . . . . . . 31.1.1 Group action and Quotients . . . . . . . . . . . . . . . . . . . . . . . 41.1.2 ALE manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91.1.3 Conformal change of scalar curvature . . . . . . . . . . . . . . . . . . 11 1.2 Background in PDE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 1.3 Nilpotent group and actions . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 1.4 Gromov-Hausdorff Convergence . . . . . . . . . . . . . . . . . . . . . . . . . 20 1.5 Cheeger-Gromov Convergence . . . . . . . . . . . . . . . . . . . . . . . . . . 23 1.6 Cheeger-Fukaya-Gromov Collapsing Theory . . . . . . . . . . . . . . . . . . 26 

2 Special Metrics and Moduli Space 31 

2.1 Locally Conformally Flat Metrics . . . . . . . . . . . . . . . . . . . . . . . . 31 2.1.1 Local Analytic Aspect for LCF manifolds . . . . . . . . . . . . . . . . 33 2.1.2 Global Geometric Aspect for LCF manifolds . . . . . . . . . . . . . . 40 2.2 Yamabe Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45 2.3 Positive Mass Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48 2.4 Examples and Classification Results for LCF Manifolds . . . . . . . . . . . . 51 2.4.1 Standard examples of LCF manifolds and their Yamabe class . . . . . 52 2.4.2 Classification of LCF manifolds in the positive Yamabe class . . . . . 53 2.4.3 Classification in dimension 3 . . . . . . . . . . . . . . . . . . . . . . . 54 2.4.4 Classification in dimension 4 . . . . . . . . . . . . . . . . . . . . . . . 55 iii 2.4.5 Complete noncompact LCF manifolds with non-negative Ricci curvature 56 2.5 Moduli Space Analogy: Teichm¨ uller Space . . . . . . . . . . . . . . . . . . . 56 2.5.1 Teichm¨ uller space of a surface . . . . . . . . . . . . . . . . . . . . . . 57 2.5.2 The LCF moduli space as a higher-dimensional analog . . . . . . . . 58 

3 Locally Conformally Flat Moduli Space 60 

3.1 The Moduli Space and Tian-Viaclovsky Compactification . . . . . . . . . . . 60 3.2 Locally Conformally Flat ALE Manifolds . . . . . . . . . . . . . . . . . . . . 66 3.2.1 Totally umbilic submanifolds . . . . . . . . . . . . . . . . . . . . . . . 67 3.2.2 Harmonic functions on ALE manifolds . . . . . . . . . . . . . . . . . 69 3.2.3 LCF ALE manifolds are AE . . . . . . . . . . . . . . . . . . . . . . . 70 3.2.4 Universal cover as a domain in Sn . . . . . . . . . . . . . . . . . . . . 73 3.3 Structure Theory of LCF ALE Manifolds and Orbifolds . . . . . . . . . . . . 74 3.3.1 Injectivity theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74 3.3.2 Local isotropy groups . . . . . . . . . . . . . . . . . . . . . . . . . . . 75 3.3.3 Finite manifold cover . . . . . . . . . . . . . . . . . . . . . . . . . . . 76 3.4 The Good Orbifold Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . 77 3.5 Classification Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79 3.5.1 Conformal compactification and Yamabe invariant . . . . . . . . . . . 79 3.5.2 Local isotropy and paired orbifold points . . . . . . . . . . . . . . . . 80 3.5.3 Dimension-specific classification . . . . . . . . . . . . . . . . . . . . . 82 3.5.4 The Schwarzschild example and the pairs conjecture . . . . . . . . . . 85 3.6 Application to the Moduli Space: Refined Description . . . . . . . . . . . . . 86 3.6.1 The oriented moduli space . . . . . . . . . . . . . . . . . . . . . . . . 87 3.6.2 Non-orientable limiting configurations . . . . . . . . . . . . . . . . . . 90 3.7 The positive mass theorem for LCF, ALE orbifolds . . . . . . . . . . . . . . 92 

4 Collapsing Constant Scalar Curvature Metrics 97 

4.1 The Question of Cheeger–Fukaya–Gromov . . . . . . . . . . . . . . . . . . . 97 4.2 Cheeger–Fukaya–Gromov Theory with Finite Regularity . . . . . . . . . . . 101 4.2.1 Finite-regularity fibration and connections . . . . . . . . . . . . . . . 101 4.2.2 The N -invariant nearby metric . . . . . . . . . . . . . . . . . . . . . 106 4.3 Convergence of Eigenvalues of the Laplacian . . . . . . . . . . . . . . . . . . 109 4.4 Proof Strategy: Invariant Metric and Scalar Curvature Estimates . . . . . . 111 4.4.1 The N -invariant nearby metric . . . . . . . . . . . . . . . . . . . . . 112 4.4.2 Scalar curvature in the distributional norm . . . . . . . . . . . . . . . 112 4.4.3 Laplacian on N -invariant functions . . . . . . . . . . . . . . . . . . . 113 4.4.4 Weighted Sobolev spaces on the base . . . . . . . . . . . . . . . . . . 115 4.5 Linearized Equation Estimates . . . . . . . . . . . . . . . . . . . . . . . . . . 115 4.5.1 The operator P and its linearization . . . . . . . . . . . . . . . . . . 116 4.5.2 Calder´ on-Zygmund estimate . . . . . . . . . . . . . . . . . . . . . . . 118 4.5.3 Uniform injectivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119 4.6 Nonlinear Equation Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . 120 

5 Further Discussions and Open Problems 124 

iv 5.1 A Gluing Construction of Constant Scalar Curvature Metrics . . . . . . . . . 124 5.1.1 Joyce’s gluing theorem . . . . . . . . . . . . . . . . . . . . . . . . . . 124 5.1.2 Collapsing factors and a new type of degeneration . . . . . . . . . . . 125 5.2 An ε-Regularity Theorem in the Collapsing Setting . . . . . . . . . . . . . . 127 5.2.1 Failure in the collapsing setting . . . . . . . . . . . . . . . . . . . . . 127 5.2.2 The conjecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128 5.3 The Full Picture of the LCF Moduli Space . . . . . . . . . . . . . . . . . . . 129 5.3.1 Collapsing LCF sequences and their limits . . . . . . . . . . . . . . . 129 5.3.2 Scalar curvature is not preserved under collapsing . . . . . . . . . . . 130 5.3.3 Open problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131 

Bibliography 133 Appendix A The proof of Cheeger-Fukaya-Gromov Theorem 138 

A.1 Proof of Theorem 1.11 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138 

Appendix B Orbifold Points in Pairs 144 

vLIST OF FIGURES 

Page 2.1 Compact Riemann surfaces of genus g = 0, 1, and 2. The Teichm¨ uller space Tg

parametrizes complex (equivalently, constant-curvature) structures on genus-g

surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 3.1 A sequence ( Mi, g i) ∈ M converging in the Gromov-Hausdorff topology to an LCF orbifold ( M∞, g ∞). At each concentration point a rescaled bubble ( ˆM∞, ˆg∞), a non-compact LCF ALE manifold, detaches. . . . . . . . . . . . 62 3.2 An ALE manifold ( M, g ) and its end E, diffeomorphic to ( Rn \ B)/Γ. The two colored curves are large coordinate spheres that become totally umbilic under the conformal map ¯ϕ : M → Rn. . . . . . . . . . . . . . . . . . . . . . 72 3.3 The Schwarzschild ALE manifold ( M, g ) (left), its quotient ( M/σ, g ) by the antipodal map (center), and the blow-up at the resulting single orbifold point, which produces the football metric Sn/Z2 (bottom). . . . . . . . . . . . . . . 86 3.4 Two non-orientable GH limiting configurations. Top row (Example 3.3): the limit is a non-orientable cap, and one non-orientable Schwarzschild ALE bub-ble detaches. Bottom row (Example 3.4): the limit is the football metric S4/Γ, and two non-orientable Schwarzschild ALE pieces bubble off. . . . . . . . . . 96 vi LIST OF TABLES 

Page 2.1 Comparison of the two proofs of the classical PMT. . . . . . . . . . . . . . . 50 2.2 Comparison of the classical and LCF Positive Mass Theorems. . . . . . . . . 51 2.3 Standard LCF manifolds by Yamabe class. . . . . . . . . . . . . . . . . . . . 52 2.4 Dictionary between Teichm¨ uller theory and LCF moduli theory. . . . . . . . 59 vii ACKNOWLEDGMENTS 

The author gratefully acknowledges the financial support provided by the NSF Research Grant DMS-2105478 during the course of this research. I would like to thank my advisor, Jeff Viaclovsky, whose expertise was invaluable in for-mulating the research questions and methodology. Your insightful feedback pushed me to sharpen my thinking and brought my work to a higher level. I would also like to thank all the geometric analysis faculties in UCI: Jeff Streets, Richard Schoen, Zhiqin Lu, Xiangwen Zhang, Li Sheng Tseng, Yi Lai. We had a lot of seminars and deep conversation, and I learned a lot from you. This whole experience shapes my academic interest and guides me in the future. In addition, I would like to thank my friend, Yifan Guo, who has been my room mate for a long time and my closest academic collaborator. We had a quite pleasant time learning geometry together and learn from each other. I would thank Chaoming Lin, Kuanhui Lee, Joe Lee, Qizhi Zhao, Michael Womack, Anna Cusenza, Bryan Dimler, Jonathan Delgado for numerous conversation in geometry. Also, I would like to thank my friends in my cohort, Tianhao Wang, Xiaonan Chen, Dingjia Mao, Yuxiang Yao, Yiyun He, So Nakamura, Jong-won Kim, Xu Zhuang, for the long-time friendship and all the help along the way. I could not have completed this dissertation without the support of my friends. Finally, I would like to thank my parents and my partner, Wenlin. Thanks for all your support. You are always my strongest backing for all the things. viii VITA 

## Xiaokang Wang 

EDUCATION Doctor of Philosophy in Mathematics 2026 

University of California, Irvine Irvine, CA, USA 

Bachelor of Science in Mathematics and Applied Mathematics 2020 

Southern University of Science and Technology, China Shenzhen, Guangdong, China 

RESEARCH EXPERIENCE Graduate Research Assistant 2021–2024 

University of California, Irvine Irvine, California 

TEACHING EXPERIENCE Teaching Assistant 2024–2026 

University of California, Irvine Irvine, CA 

ix REFEREED JOURNAL PUBLICATIONS On the structure of locally conformally flat orbifolds and ALE metrics 2025 

Preprint 

Pluriclosed flow on Oeljeklaus-Toma manifolds (with Jeff Streets) 2025 

Journal of Mathematic Study 

REFEREED CONFERENCE PUBLICATIONS Machine Learning and LLM-Boost Symbolic Regres-sion for Predicting Q-Gonality of Modular Curves (with X.Zhuang, Y.Yao, P.Hsu, P.Qi) Jun 2025 

ICML, AI4Math xABSTRACT OF THE DISSERTATION 

On the moduli space of locally conformally flat manifolds and collapsed constant scalar manifolds By Xiaokang Wang Doctor of Philosophy in Mathematics University of California, Irvine, 2026 Professor Jeff Viaclovsky, Chair We prove several structure theorems for locally conformally flat, positive Yamabe orbifolds and nonnegative scalar curvature, ALE manifolds. These two kinds of spaces can be related by conformal blow-up and conformal compactification. For the orbifolds, we prove that such orbifolds admit a manifold cover. For the ALE manifolds, the homomorphism of the fundamental group for the ALE space induced by the embedding of the ALE end is always injective. Using these properties, several classifications of such ALE manifolds and orbifolds are given in low dimensions. As an application to the moduli space, we prove that the football orbifold S4/Γ cannot be realized as the Gromov-Hausdorff limit. In addition, we prove the positive mass theorem of these ALE ends and give a simple proof for the optimal decay rate. Using the positive mass theorem, we can solve the orbifold Yamabe problem in the locally conformally flat case. Also, we prove that a sequence of constant scalar curvature (CSC) metrics which is collapsing with bounded curvature to a manifold ( X, g ) can be perturbed to a sequence of N -invariant collapsing CSC metrics, under a natural assumption involving the eigenvalues of the drift Laplacian on ( X, g ). This answers a special case of a question of Cheeger-Fukaya-Gromov. We also give some natural conditions on the limiting metric-measure space under which the eigenvalue assumption is automatically satisfied. xi Notations 

This section collects the main notation used throughout the thesis. (M, g ) A smooth Riemannian manifold with metric g.

n The dimension of M .

dV g The Riemannian volume element induced by g.

∇ The Levi-Civita connection of g.∆g The Laplace-Beltrami operator with respect to g.Ric g The Ricci curvature tensor of g.

Rg The scalar curvature of g.Rm g The full Riemann curvature tensor of g.

|Rm g| The pointwise norm of Rm g.dist g(x, y ) The geodesic distance between x, y ∈ M .

Bgr (x) The geodesic ball centered at x with radius r.inj g(x) The injectivity radius at x.1[g] The conformal class of the metric g.

Y (M, [g]) The Yamabe constant of the conformal class [ g]. 

M A moduli space of metrics (context-dependent). 

LCF Locally conformally flat. 

CSC Constant scalar curvature. 

ALE Asymptotically locally Euclidean. 

Ck,α Holder spaces with k derivatives and exponent α ∈ (0 , 1). 

W k,p Sobolev spaces with k weak derivatives in Lp.

ε A small positive constant used in perturbative arguments. 

ωn The volume of the unit ball in Rn.2Chapter 1 Introduction 

This chapter collects the background material required for the rest of the thesis. We do not prove any new results here. §1.1 reviews the basic language of Riemannian geometry, orb-ifolds, and ALE manifolds. §1.2 collects the elliptic estimates (Schauder, Calder´ on-Zygmund, Sobolev embedding) and the asymptotic expansion of harmonic functions that are used in later chapters. §1.3 review the fundamental theory of nilpotent group and the actions. 

§1.4– §1.6 develop the three convergence frameworks central to the thesis: Gromov-Hausdorff convergence, Cheeger-Gromov convergence for non-collapsing sequences, and the Cheeger-Fukaya-Gromov collapsing theory. 

# 1.1 Background in Riemannian Geometry 

This thesis studies Riemannian metrics with special curvature properties on compact man-ifolds, asymptotically locally Euclidean (ALE) manifolds, and orbifolds. We collect in this section the foundational definitions and fix notation. 

Definition 1.1 (Riemannian manifold) . A Riemannian manifold (M n, g ) is a smooth 

n-dimensional manifold M equipped with a smooth, symmetric, positive-definite (0 , 2) -tensor 

3field g called the Riemannian metric . In local coordinates (x1, . . . , x n), we write 

g = gij dx i ⊗ dx j .

The metric g determines the following canonical structures: 

• The Levi-Civita connection ∇: the unique torsion-free connection satisfying ∇g =0.

• The Riemann curvature tensor Rm , with components Rijkl , defined by R(X, Y )Z =

∇X ∇Y Z − ∇ Y ∇X Z − ∇ [X,Y ]Z.

• The Ricci tensor Ric ij = R kikj (trace of Rm ). 

• The scalar curvature Rg = gij Ric ij (trace of Ric ). 

• The volume form dV g = pdet( gij ) dx 1 ∧ · · · ∧ dx n.A Riemannian manifold is complete if every geodesic extends to all of R, equivalently, if 

(M, d g) is complete as a metric space where dg is the Riemannian distance. 

Standard references for Riemannian geometry are do Carmo [23] and Petersen [50]. 

## 1.1.1 Group action and Quotients 

In order to introduce symmetry and quotient of a manifold, we need to introduce group actions. 

Definition 1.2 (Group action) . Let (M, g ) be a Riemannian manifold and Γ a group. A

smooth action Γ ↷ M is a homomorphism ρ : Γ → Diff( M ). A smooth isometric action Γ ↷ M is a homomorphism ρ : Γ → Isom( M, g ). The action is: 

4• properly discontinuous : for every compact K ⊂ M , the set {γ ∈ Γ : γ(K)∩K̸ = ∅} 

is finite; 

• free : no γ̸ = id has a fixed point. 

A free, properly discontinuous, isometric action yields a smooth Riemannian manifold M/ Γ. Now, we talk about several examples of constructing quotient manifolds. 

Example 1.1 (Finite Group) . Let Γ ≤ O(n + 1) be a finite group acting freely and isomet-rically on the unit sphere Sn ⊂ Rn+1 . Then the quotient 

Sn/Γ

is a compact Riemannian orbifold, and it is in fact a smooth manifold precisely when the action is free. In dimension three, a standard example is a lens space L(p, q ) = S3/Zp, where 

Zp acts by a finite subgroup of unitary rotations. Such quotients are called spherical space forms .

Example 1.2 (Discrete Group) . Let Γ = Zn act on Rn by translations: 

k · x = x + k, k ∈ Zn, x ∈ Rn.

This action is free, properly discontinuous, and cocompact, and the quotient is the flat torus 

Rn/Zn ∼= Tn.

More generally, any lattice Γ ≤ Rn gives a compact flat manifold Rn/Γ. This is the basic model of a quotient by a discrete cocompact subgroup. 

Example 1.3 (Continuous Group) . Let S1 act on the flat two-torus T2 = S1 ×S1 by rotation 

5in the first factor: 

eiθ · (z1, z 2) = ( eiθ z1, z 2),

for eiθ ∈ S1 and (z1, z 2) ∈ S1 × S1. This action is smooth, continuous, and free, so the orbit space is again a circle, 

T2/S 1 ∼= S1.

This is the simplest example of a continuous group action on a compact torus. A similar phenomenon occurs for the standard S1-action on S3 ⊂ C2, whose quotient is S2 via the Hopf fibration. This example shows that allowing a continuous group changes the geometry of the quotient fundamentally. 

Example 1.4 (Infranilmanifold) . Let H3 denote the three-dimensional Heisenberg group, viewed as the simply-connected nilpotent Lie group of upper triangular matrices of the form 



1 x z

0 1 y

0 0 1

 , x, y, z ∈ R.

The subgroup H3(Z) consisting of matrices with x, y, z ∈ Z is a cocompact lattice, and the quotient 

H3/H 3(Z)

is a compact nilmanifold. More generally, if N is a simply-connected nilpotent Lie group and Γ ≤ N L ⋊ Aut( N ) is a discrete cocompact subgroup, then Γ\N is called an infranil-manifold . In the collapsing theory of Chapter 4, these spaces appear as the typical fibers of 

6Cheeger–Fukaya–Gromov fibrations (see §1.6). 

A properly discontinuous (but not necessarily free) isometric action yields a Riemannian orbifold M/ Γ. Now, we can introduce this slightly generalization of manifolds. 

Definition 1.3 (Riemannian orbifold) . A topological space M n is an orbifold if every point 

x ∈ M has a neighborhood U , an open set eU ⊆ Rn, a finite group Gx acting smoothly on eU ,and a Gx-equivariant homeomorphism eU → U inducing a homeomorphism U ∼= eU /G x.A point x is singular (an orbifold point ) if Gx̸ = {1}; otherwise it is regular . A

Riemannian orbifold (M, g ) is an orbifold with a Gx-invariant Riemannian metric on each uniformizing chart, compatible on overlaps. 

In this thesis we consider orbifolds with isolated singularities : at each singular point xi,the local group Gi ≤ O(n) acts on Rn with only the origin fixed, so a punctured neighborhood of xi is diffeomorphic to ( Rn \ { 0})/G i. The link of the singularity is Sn−1/G i.A prototypical example is Rn/Γ for a finite group Γ ≤ O(n): the origin is the unique singular point with isotropy group Γ, and the link Sn−1/Γ is a spherical space form. The football orbifold S2/Zk (a sphere with two cone points of angle 2 π/k ) is the simplest two-dimensional example (see §2.1). 

Definition 1.4 (Orbifold fundamental group) . Let O be a connected good orbifold, written as a quotient 

O = fM / Γ,

where fM is simply connected and Γ acts properly discontinuously by orbifold isometries. The 

7orbifold fundamental group of O is the deck transformation group 

πorb 1 (O) := Γ .

Equivalently, it is the group of homotopy classes of orbifold loops, where loops are allowed to carry local isotropy data at singular points. 

Example 1.5 (Football orbifold) . Let Γ ≤ O(n) ⊂ O(n + 1) be finite, and let it act on 

Sn ⊂ Rn+1 through the first n coordinates, fixing the north and south poles. Assume these are the only fixed points. Then 

F := Sn/Γ

is a football orbifold with exactly two orbifold points. Since Sn is the orbifold universal cover (for n ≥ 2), the deck group is Γ, hence 

πorb 1 (F) ∼= Γ .

On the other hand, the underlying topological quotient |F| is homeomorphic to Sn (the action only changes the two cone neighborhoods), so 

π1(|F| ) = 0 (n ≥ 2) .

Thus the orbifold fundamental group detects isotropy information that the ordinary topological fundamental group does not see. 

There is a very special way of constructing the orbifolds, where the orbifolds can be raised as a quotient of manifolds. 8Definition 1.5 (Good orbifold) . An orbifold M is a good orbifold (or developable orb-ifold ) if M ∼= fM / Γ for some smooth Riemannian manifold fM and some group Γ acting properly discontinuously and isometrically on fM . An orbifold that does not arise this way is called bad .

Remark 1.1. A concrete model of the teardrop orbifold is the weighted projective line 

CP 1(1 ,k ), equivalently the 2-sphere with one cone point of order k. Topologically, its underlying space is S2; a neighborhood of the singular point is modeled on D2/Zk, where Zk acts by rotations z 7 → e2πi/k z, and the rest of the orbifold is smooth. This orbifold is not developable, so it cannot be covered by a manifold. The teardrop is 2-dimensional, locally conformally flat, and admits a metric of positive curvature. 

Remark 1.2. In this thesis, we have proved the following theorem: all compact locally conformally flat (LCF) orbifolds with isolated singularities and positive scalar curvature with diemnsion n ≥ 3 are good orbifolds; see Theorem 3.13 in §3.3. 

## 1.1.2 ALE manifolds 

Definition 1.6 (ALE manifold and ALE orbifold) . Let Γ ≤ O(n) be a finite subgroup. A complete Riemannian manifold (M n, g ) is asymptotically locally Euclidean (ALE) of order τ > 0 if there exists a compact set K ⊂ M and a diffeomorphism 

Φ : M \ K −→  Rn \ B(0 , R )/Γ

for some R > 0, such that in coordinates induced by Φ:

(Φ ∗g)ij (x) = δij + O(|x|−τ ),∂ k(Φ ∗g)ij (x) = O(|x|−τ −k)9for all k ≥ 1 as |x| → ∞ . The group Γ is the group at infinity of the end. When Γ = {1},we call (M, g ) asymptotically flat (AF) .A Riemannian orbifold (M, g ) is an ALE orbifold if the same condition holds and M may have isolated orbifold singularities in its interior. 

The model ALE end is Rn \ B(0 , R ) quotiented by Γ; the trivial ALE manifold (with bound-ary) is Rn/Γ (minus a small ball). This definition, due to Bartnik [11], is the setting for the Positive Mass Theorem ( §2.3) and the ALE orbifold moduli theory of Chapter 3. 

Example 1.6. The Eguchi–Hanson metric is the standard Ricci-flat ALE metric on the total space of the complex line bundle OCP 1 (−2) ∼= T ∗S2, which resolves the quotient singularity 

C2/{± 1}. In coordinates (r, θ, ϕ, ψ ) with r ≥ a > 0, it can be written as 

gEH =



1 − a4

r4

−1

dr 2 + r2

4



1 − a4

r4



(dψ + cos θ dϕ )2

+ r2

4

 dθ 2 + sin 2 θ dϕ 2.

As r → ∞ , this metric approaches the flat metric on R4/Z2, so its group at infinity is Z2.

Example 1.7. The Schwarzschild metric is the standard scalar-flat AF metric on Rn \ { 0}.In polar coordinates (r, ω ) on Rn \ { 0}, it is given by 

gSch =



1 + m

2rn−2

 4 

> n−2

 dr 2 + r2gSn−1

,

where m > 0 is the mass parameter and gSn−1 is the round metric on the unit sphere. This metric is complete, has vanishing scalar curvature away from the origin, and is asymptotic to the Euclidean metric, so its group at infinity is trivial. It is the basic AF model in the study of the Positive Mass Theorem and appears as the simplest nontrivial scalar-flat exterior solution. 

10 1.1.3 Conformal change of scalar curvature 

In this thesis, we will talk about a special way of changing the metric while preserving certain geometric properties. We are particularly interested in the behavior of scalar curvature under conformal changes of metric, which is governed by the Yamabe equation. This is a nonlinear elliptic PDE that plays a central role in our analysis. 

Definition 1.7 (Conformal change of scalar curvature) . Let (M n, g ) be a Riemannian man-ifold with n ≥ 3. Under a conformal change ˜g = u4/(n−2) g with u > 0 smooth, the scalar curvatures satisfy: 

R˜g = u− n+2 

> n−2



−4( n − 1) 

n − 2 ∆gu + Rg u



. (1.1) 

The operator 

Lg := −4( n − 1) 

n − 2 ∆g + Rg

is the conformal Laplacian (or Yamabe operator ). The equation R˜g = λ (constant scalar curvature) is equivalent to 

Lgu = λ u n+2  

> n−2

, u > 0, (1.2) 

known as the Yamabe equation . The conformal Laplacian satisfies the covariance identity 

L˜gv = φ−(n+2) /(n−2) Lg(φv ) for ˜g = φ4/(n−2) g.

Equation (1.1) is a standard computation via Christoffel symbols; see Lee-Parker [45] for details. This formula is the starting point for the Yamabe problem ( §2.2) and for the Green’s function method in the Positive Mass Theorem ( §2.3). The geometric objects defined in this section — curvature tensors, orbifold charts, ALE 11 asymptotics, and the conformal Laplacian — are the stage on which all subsequent analysis takes place. To extract information from them, we need the language of function spaces and elliptic estimates, which we collect in the next section. 

# 1.2 Background in PDE 

The geometric equations of this thesis — the Yamabe equation, the scalar curvature equation under conformal deformation, and the estimates for collapsing fibrations — are all second-order elliptic PDE. To state and prove these results with appropriate precision, we need a common framework of function spaces and elliptic estimates. We collect the relevant tools in this section; all manifolds are smooth and n-dimensional. 

Definition 1.8 (Ck,α and W k,p spaces) . Fix a compact Riemannian manifold (M, g ) with a finite atlas {(Uℓ, ϕ ℓ)} and a subordinate partition of unity {ρℓ}. For a function u : M → R,set uℓ = ( ρℓu) ◦ ϕ−1 

> ℓ

: Rn → R.1. H¨ older spaces : for k ≥ 0 and α ∈ (0 , 1) , the norm 

∥u∥Ck,α (M ) = X

> ℓ

∥uℓ∥Ck,α (Rn)

defines the Banach space Ck,α (M ), where ∥v∥Ck,α (Rn) is the standard H¨ older norm (supremum of v and its derivatives up to order k, plus the α-H¨ older seminorm of the 

k-th order derivatives). 2. Sobolev spaces : for k ∈ N and p ≥ 1, the norm 

∥u∥W k,p (M ) = X

> ℓ

∥uℓ∥W k,p (Rn)

defines the Banach space W k,p (M ), where W k,p (Rn) is the standard Sobolev norm (sum 

12 of Lp norms of weak derivatives up to order k). These definitions are independent of the choice of atlas and partition of unity up to equivalent norms. 

Theorem 1.1 (Sobolev embedding) . Let Ω ⊂ Rn be a bounded Lipschitz domain, k ≥ 1,

p ≥ 1.1. Subcritical (kp < n ): W k,p (Ω) ,→ Lp∗

(Ω) continuously, where p∗ = np/ (n − kp ).2. Supercritical (kp > n ): W k,p (Ω) ,→ Cj,β ( ¯Ω) continuously for all j + β < k − n/p 

with j ∈ N0, β ∈ (0 , 1) .3. Critical (kp = n): W k,p (Ω) ,→ Lq(Ω) for all 1 ≤ q < ∞.The embeddings in (1) and (2) are compact (Rellich-Kondrachov) when the target exponent is strictly below the critical threshold. The same embeddings hold for W k,p sections of vector bundles over compact Riemannian manifolds. 

See Gilbarg-Trudinger [30] §7 or Evans [24] §5.6 for proofs. 

Theorem 1.2 (Schauder estimates) . Let L = aij (x)∂i∂j + bi(x)∂i + c(x) be a second-order uniformly elliptic operator on Ω ⊂ Rn with coefficients in Ck,α (Ω) , k ≥ 0, α ∈ (0 , 1) . If 

Lu = f with f ∈ Ck,α (Ω) , then for any Ω′ ⋐ Ω:

∥u∥Ck+2 ,α (Ω ′) ≤ C ∥f ∥Ck,α (Ω) + ∥u∥L∞(Ω) 

, (1.3) 

where C depends on n, k, α, the ellipticity constants, the Ck,α norms of the coefficients, and 

dist(Ω ′, ∂ Ω) .Under Ck+2 ,α boundary conditions on a Ck+2 ,α domain, the global estimate ∥u∥Ck+2 ,α ( ¯Ω) ≤

C(∥f ∥Ck,α + ∥u∥L∞ ) holds. The same estimate holds on compact Riemannian manifolds with 

13 Ck,α metrics. 

See Gilbarg-Trudinger [30] §6.1–6.2. 

Theorem 1.3 (Calder´ on-Zygmund W 2,p estimate) . Let ∆u = f ∈ Lp(Ω) for 1 < p < ∞

and Ω′ ⋐ Ω ⊂ Rn. Then u ∈ W 2,p  

> loc

(Ω) and 

∥u∥W 2,p (Ω ′) ≤ C(n, p ) ∥f ∥Lp(Ω) + r−2∥u∥Lp(Ω) 

, (1.4) 

where r = dist(Ω ′, ∂ Ω) . More generally, for a uniformly elliptic operator L with VMO leading coefficients, if Lu = f ∈ W k,p then u ∈ W k+2 ,p with the analogous estimate. 

See Gilbarg-Trudinger [30] §9. As an example of geometric structure effecting the analysis result, we put the following harmonic function expansion result on Rn here. Latter, we will apply this result to geneal ALE manifolds. 

Lemma 1.4 (Asymptotic expansion of harmonic functions on Rn). Let n ≥ 3 and let u be harmonic on Rn \ B1(0) with u(x) = O(|x|2−n+ε) as |x| → ∞ for some ε > 0. Then: 

u(x) = a |x|2−n + b + O(|x|−(n−1) ) (1.5) 

as |x| → ∞ , for constants a, b ∈ R.Proof. Write u in polar coordinates ( r, ω ) ∈ (1 , ∞) × Sn−1 and expand u(r, ·) in L2(Sn−1): 

u(r, ω ) = 

> ∞

X

> ℓ=0

fℓ(r) Yℓ(ω),

where Yℓ is a spherical harmonic of degree ℓ, satisfying ∆ Sn−1 Yℓ = −ℓ(ℓ + n − 2) Yℓ.14 Since ∆ u = 0, each radial coefficient fℓ satisfies the Euler ODE 

f ′′  

> ℓ

+ n − 1

r f ′ 

> ℓ

− ℓ(ℓ + n − 2) 

r2 fℓ = 0 .

The general solution is 

fℓ(r) = Aℓrα+ 

> ℓ

+ Bℓrα−

> ℓ

with exponents α± 

> ℓ

= −(n − 2) ± p(n − 2) 2 + 4 ℓ(ℓ + n − 2) /2. For ℓ = 0: α+0 = 0, 

α− 

> 0

= 2 − n, giving f0(r) = b + ar 2−n. For ℓ ≥ 1: α+ 

> ℓ

= ℓ > 0 and α− 

> ℓ

= −(n − 2 + ℓ) < 0. The hypothesis u = O(|x|2−n+ε) forces Aℓ = 0 for all ℓ ≥ 1, since rℓ grows. Thus fℓ(r) = 

Bℓr−(n−2+ ℓ) for ℓ ≥ 1, giving 

u(r, ω ) = b + ar 2−n +

> ∞

X

> ℓ=1

Bℓr−(n−2+ ℓ)Yℓ(ω).

The first correction decays like r−(n−1) , establishing (1.5). 

Remark 1.3. The constant a is proportional to the capacity (or ADM mass) of the end; 

b is the asymptotic value. On an ALE manifold (M, g ) with g = gRn + O(r−τ ), the same expansion holds for harmonic functions on the ALE end, and is used in §3.2 and §3.3. 

See Axler-Bourdon-Ramey [8] Ch. 5 for a more general treatment. With these PDE tools in hand, we can now discuss how sequences of Riemannian manifolds converge to limit spaces. The interplay between curvature bounds and compactness — the subject of the next two sections — is what makes the moduli-space analysis in this thesis possible. 15 1.3 Nilpotent group and actions 

We now make some notes on the nilpotent Lie group and their actions. 

Definition 1.9 (Nilpotent group) . A nilpotent Lie group is a Lie group, N , which is simply connected and whose Lie algebra is g is a nilpotent Lie algebra, that is 

g1 = [ g, g], g2 = [ g, g1], ... (1.6) 

eventually vanishes, i.e., gk = 0 , for some k, finite. 

Remark 1.4. A connected simply connected nilpotent Lie group N is diffeomorphic to Rn,given by the exponential map. This can be seen from the Baker-Campbell-Hausdorff formula since it terminates in finitely many steps. 

Definition 1.10 (Automorphism and Left action) . The automorphism group of a nilpo-tent Lie group, Aut( N ) is the group of Lie group automorphisms of N :

Aut( N ) = {ϕ : N → N : ϕ is a smooth group isomorphism }. (1.7) 

Let h ∈ N , then we define the left action: 

Lh : N → N , x 7 → hx. (1.8) 

Then, we denote the group of left translation :

NL := {Lh : h ∈ N } . (1.9) It can be easily seen that there is a natural isomorphism NL ∼= N . Similarly, we can define 16 the right translation group NR ∼= N .

Definition 1.11 (Left and right invariant vector fields) . For V ∈ n, the corresponding 

left-invariant vector field is 

V Lg = ( Lg)∗V, (1.10) 

and the corresponding right-invariant vector field is 

V Rg = ( Rg)∗V, (1.11) 

where 

Lg(h) = gh, Rg(h) = hg. (1.12) It can be shown that left action is generated by a right invariant vector field 

eVg = ddt t=0 

exp( tV )g = ( Rg)∗V = V Rg . (1.13) There is a natural flat affine connection on N . We now define it. 

Definition 1.12 (Affine connection and affine structure) . The canonical affine connec-tion , ∇can , is the connection for which the left-invariant vector fields are parallel, i.e., 

∇can V L = 0 (1.14) 

for every left-invariant vector field V L.

17 Note that, ∇can is flat, and, in general, not torsion free, in fact: 

T ∇can 

(X, Y ) = −[X, Y ]. (1.15) Since the left-invariant vector fields are parallel, so is T ∇can 

.Note also that, when ∇can acts on right invariant vector field, we have: 

∇can W R V R = [ V, W ]R, (1.16) which is a constant right invariant vector field. 

Definition 1.13. An affine structure on a smooth manifold is given by a choice of a flat, affine connection ∇ on T M with parallel torsion. Two affine manifiolds, (M, ∇M ), (N, ∇N ) are affine equivalent , if there is a diffeomor-phism ϕ : M → N , so that ϕ∗∇N = ∇M .The affine group , Aff( M, ∇M ) (or just Aff( M )), of (M, ∇M ), is defined to be the affine isomorphism group of (M, ∇M ).

Note that Aff( N ) of a nilpotetn Lie group N is equivalent to the group that preserves the left invariant vector fields. Thus, Aff( N ) = NL ⋊ Aut( N ). (1.17) Now, we define the nilmanifolds and infranilmanifolds. 

Definition 1.14 (nilmanifold and infranilmanifold) . A compact nilmanifold is a quotient 

M = Λ \N , (1.18) 18 where Λ ⊂ N L is a discrete cocompact subgroup. A compact infranilmanifold is a quotient 

Z = Γ \N , (1.19) 

where Γ is a torsion-free discrete cocompact subgroup of NL ⋊ Aut( N ).

It can be shown that Λ = Γ ∩ N L, the pure translation subgroup, is a normal subgroup of Γ with finite index. Thus, an infranilmanifold is finitely covered by a nilmanifold. Furthermore, the canonical affine connection descends to an affine connection on the quotient, so that the group Aff(Γ \N ) is defined. Finally, we will talk about the structure of affine group of an infranilmaniofld, Aff(Γ \N ), and its identity component Aff 0(Γ \N ). 

Proposition 1.5. Let Γ ⊆ N L ⋊ Aut( N ) be a cocompact lattice group, then we have 

Aff(Γ \N ) ∼= NAff( N )(Γ) /Γ (1.20) 

and 

Aff 0(Γ \N ) ∼= CAff( N )(Γ) /Γ, (1.21) 

where NAff( N )(Γ) and CAff( N )(Γ) are normalizer and centeralizer of Γ in Aff( N ), respectively. Proof. For every element in Aff(Γ \N ) can be lifted to Aff( N ) that makes every Γ-orbit to a Γ-orbit. Thus, the lift of Aff(Γ \N ) can be identified with NAff( N )(Γ). Thus, we have Aff(Γ \N ) ∼= NAff( N )(Γ) /Γ after the quotient. Note that since Γ is a discrete subgroup, and the identity map is in the centralizer. Thus, 19 we have Aff 0(Γ \N ) ∼= CAff( N )(Γ) /Γ. 

Remark 1.5. It is natural to identify the centeralizer of the left action group NL as the the right action subgroup NR. Indeed, for any g ∈ N L and ϕ ∈ CAff( N )(NL), if ϕ(g(x)) = gϕ (x),for any x ∈ N , then if we choose x = e, let ϕ(e) = h, then ϕ(g) = gh . Thus, we may view 

CAff( N )(Γ) as a subgroup of NR, and acts trivially on the right-invariant vector fields. 

# 1.4 Gromov-Hausdorff Convergence 

A fundamental tool in the study of moduli spaces of Riemannian metrics is convergence in the Gromov-Hausdorff sense. This notion measures how close two metric spaces are, allowing sequences of Riemannian manifolds to converge to a limit space that may not itself be a manifold. 

Definition 1.15 (Gromov-Hausdorff distance and convergence) . The Hausdorff distance 

between two subsets A, B of a metric space (Z, d ) is 

dH (A, B ) = inf {r > 0 : A ⊆ Br and B ⊆ Ar},

where Ar = {z ∈ Z : d(z, A ) < r }.The Gromov-Hausdorff (GH) distance between compact metric spaces (X, d X ) and 

(Y, d Y ) is 

dGH (X, Y ) = inf dZH (f (X), g (Y )) ,

where the infimum is over all metric spaces Z and isometric embeddings f : X , → Z, g : Y , →

Z. A sequence (Xi, d i) converges in the GH sense to (X∞, d ∞) if dGH (Xi, X ∞) → 0.An ε-GH approximation is a map f : X → Y satisfying 

20 (i) |dY (f (x1), f (x2)) − dX (x1, x 2)| < ε for all x1, x 2 ∈ X, and (ii) f (X) is ε-dense in Y .

Example 1.8. A guiding example: the flat tori (T2, ε 2dθ 21 ⊕ dθ 22 ), as ε → 0, GH-converge to a circle S1: the torus collapses by shrinking one S1 factor to a point. More precisely, write 

T2 = S1 

> ε

× S11 where the first factor has length ε; a ε-GH approximation is the projection 

(θ1, θ 2) 7 → θ2, since any two points over the same θ2 are within distance ε of each other. As ε → 0 this becomes an isometry in the limit. The limit S1 carries no information about the collapsed S1 factor. This illustrates a key phenomenon of collapsing geometry studied in 

§1.6. 

Example 1.9. An anisotropic collapsing model is 

(T2, g ε), gε = ε2dθ 21 + ε4dθ 22 ,

with θ1, θ 2 ∈ R/2πZ. Since both circle factors shrink to length O(ε) and O(ε2), respectively, we have 

diam( T2, g ε) → 0,

so (T2, g ε) GH-converges to a single point. The same phenomenon occurs for nilmanifolds (Example 1.4): if Γ\N is a compact nilman-ifold with a fixed left-invariant metric g, then 

(Γ \N , ε 2g) GH 

−−→ 

> ε→0

{pt }.

This is the basic “collapse to a point” model used repeatedly in collapsing theory. 

Example 1.10. A standard smooth-to-singular example is convergence to a metric cone. 

21 Fix α ∈ (0 , 2π), and let 

Cα = ([0 , ∞) × S1)/ ∼,

where all points (0 , θ ) are identified, with cone metric 

gcone = dr 2 +

 α

2π

2

r2dθ 2.

The cone tip is singular (not a smooth manifold point). Now choose a sequence of smooth surfaces of revolution (Mi, g i) that agree with gcone outside r ≤ 1/i and smooth out the tip inside r ≤ 1/i . Then 

(Mi, g i) GH 

−−−→ 

> i→∞

(Cα, g cone ).

Thus a sequence of smooth manifolds can GH-converge to a space with a genuine singular point. 

Although, there is not a priori regularity guaranteed by Gromov-Hausdorff convergence, there is a compactness theorem, which is closely related to the Riemannian structure, thanks to Gromov. 

Theorem 1.6 (Gromov pre-compactness, Ricci bounded below) . Fix n ≥ 2, κ ∈ R, D > 0.The class of compact n-dimensional Riemannian manifolds satisfying 

Ric( g) ≥ − (n − 1) κ and diam( M, g ) ≤ D

is pre-compact in the Gromov-Hausdorff topology: every sequence has a GH-convergent sub-sequence, and the limit is a compact metric space (X, d ).Proof sketch. The key tool is the Bishop-Gromov volume comparison : for Ric ≥ − (n −

22 1) κ, the ratio Vol( Br(x)) /V κ(r) is monotone non-increasing in r, where Vκ(r) is the volume of an r-ball in the simply-connected space of constant curvature κ. This gives a uniform upper bound N ≤ N (n, κ, D, ε ) on the cardinality of any ε-separated subset, i.e. a uniform covering number estimate. Pre-compactness in dGH then follows from the completeness of the space of compact metric spaces under dGH and the criterion that uniform total boundedness implies sequential compactness. 

Remark 1.6. No regularity of the limit is assumed: (X, d ) need not be a manifold. In partic-ular, collapsing sequences (injectivity radius → 0) are permitted. The stronger assumption 

| Rm | ≤ C (used in the CFG theory of §1.6) additionally guarantees that X has integer Hausdorff dimension and admits a fibration structure. 

The moduli space manifolds with | Rm | ≤ C and diameter ≤ D satisfies the Ricci bound (since | Rm | ≤ C implies | Ric | ≤ (n − 1) C), so its GH closure is compact by Theorem 1.6. For LCF moduli space, an even weaker Riemannian curvature Ln 

> 2

can guarantee the existence of GH limit. The Tian-Viaclovsky theorem (Chapter 3) further identifies the limit as an LCF orbifold. Gromov-Hausdorff convergence is the weakest notion of convergence we use: it detects the correct limit metric space but provides no smooth structure. When injectivity radii are bounded below, the Cheeger-Gromov theory ( §1.5) recovers a smooth limit manifold. When they collapse to zero, the finer CFG structure ( §1.6) is needed. 

# 1.5 Cheeger-Gromov Convergence 

Gromov-Hausdorff convergence gives a limit metric space, but provides no smooth structure on the limit. When the sequence is non-collapsing (injectivity radius bounded below), one obtains a smooth limit manifold via Cheeger-Gromov convergence. 23 Definition 1.16 (Cheeger-Gromov convergence) . A sequence of pointed Riemannian mani-folds {(Mi, g i, p i)} converges in the pointed Ck,α Cheeger-Gromov sense to (M∞, g ∞, p ∞)

if there exist: 

• an exhaustion K1 ⊆ K2 ⊆ · · · of M∞ by compact domains, and 

• smooth embeddings Φi : Kj ,→ Mi (for i ≫ j) with Φi(p∞) = pi,such that Φ∗ 

> i

gi → g∞ in Ck,α  

> loc

on M∞.For a sequence of compact manifolds with global diffeomorphisms Φi : M∞ → Mi, the con-vergence is Φ∗ 

> i

gi → g∞ in Ck,α (M∞).

Theorem 1.7 (Cheeger’s compactness theorem, Ck+1 ,α version) . Fix n ≥ 2, k ≥ 0, α ∈

(0 , 1) , constants Cj > 0 for j = 0 , . . . , k , and ι0 > 0. Let {(Mi, g i, p i)} be a sequence of pointed complete Riemannian n-manifolds satisfying 

|∇ j Rm( gi)| ≤ Cj (j = 0 , . . . , k ), inj( Mi, p i) ≥ ι0.

Then a subsequence converges in the pointed Ck+1 ,α Cheeger-Gromov sense to a complete pointed Riemannian manifold (M∞, g ∞, p ∞).Proof outline. Step 1 (Harmonic coordinates). By the injectivity radius bound ι0 > 0and the curvature bound | Rm | ≤ C0, every x ∈ Mi has a harmonic coordinate chart on 

Br0 (x) (for r0 = r0(n, C 0, ι 0) > 0 uniform in i) in which the metric satisfies 12 δij ≤ gij ≤ 2δij 

and ∥gij ∥Ck+1 ,α ≤ C. The key point is that in harmonic coordinates, ∆ ggij = Q(g, ∂g ) where the right side involves curvature; hence Schauder estimates (Theorem 1.2) convert bounds on |∇ j Rm | into Ck+1 ,α bounds on gij .

Step 2 (Arzel` a-Ascoli). In each harmonic chart, the metric components g(i) 

> ij

form a sequence in Ck+1 ,α with uniform bounds. By the compact Rellich embedding Ck+1 ,α ,→ Ck,α ′

24 (Theorem 1.1), a subsequence converges in Ck+1 ,α ′

.

Step 3 (Diagonal subsequence). Applying this chart-by-chart and diagonalizing over an exhaustion of the limit manifold gives the global Ck+1 ,α convergence. See Cheeger [16], Peters [49], and Greene-Wu for the foundational results. 

Theorem 1.8 (Cheeger’s compactness theorem, W k+2 ,p version) . Under the weaker hypoth-esis 

∥∇ j Rm( gi)∥Lp ≤ Cj (j = 0 , . . . , k − 1) , p > n/ 2, inj( Mi, p i) ≥ ι0,

the same conclusion holds with Φ∗ 

> i

gi → g∞ in W k+2 ,p  

> loc

.

The proof replaces Schauder estimates with Calder´ on-Zygmund estimates (Theorem 1.3) and Arzel` a-Ascoli with Rellich-Kondrachov compactness (Theorem 1.1). See Anderson-Cheeger [5]. 

Remark 1.7. The W k+2 ,p version is used in Chapter 4 (finite-regularity CFG theory), where the PDE estimates naturally produce Lp curvature bounds rather than pointwise Ck bounds. The Ck+1 ,α version is used throughout the non-collapsing compactification of Chapter 3, where pointwise curvature bounds are available. 

Definition 1.17 (Equivariant Cheeger-Gromov convergence) . Let {(Mi, g i)} be compact n-manifolds converging in GH to a compact d-manifold (X, g ∞) with d ≤ n (possibly collapsing). The convergence is equivariant local Ck,α if there is a uniform r > 0 such that for every sequence of points xi ∈ Mi → x∞ ∈ X, the universal covers lift to equivariant convergence: 

( eBr(˜ xi), ˜gi, G i) Ck,α 

−−−→ ( eBr(˜ x∞), ˜g∞, G ∞),

where Gi, G∞ are the deck transformation groups and the convergence is Ck,α Cheeger-

25 Gromov. In this setting, when d < n , then G∞ is a nilpotent Lie group N acting by isome-tries, and the projection π∞ : eBr(˜ x∞) → Br(x∞) is a Riemannian submersion. 

This definition, due to Fukaya [26] and developed in CFG [19], makes precise the local structure of a collapsing sequence: upstairs on universal covers there is genuine non-collapsing 

Ck,α convergence, even though the original sequence collapses. The nilpotent group N that appears is the structure group of the CFG fibration constructed in §1.6. The key limitation of Cheeger-Gromov theory is the non-collapsing hypothesis inj( Mi, p i) ≥

ι0 > 0: when injectivity radii collapse to zero, the harmonic coordinate construction breaks down entirely. The Cheeger-Fukaya-Gromov theory of §1.6 replaces the injectivity radius assumption with the fibration structure of the collapsing, enabling a parallel analysis in the collapsing regime. 

# 1.6 Cheeger-Fukaya-Gromov Collapsing Theory 

Let {(M ni , g i)} be a sequence of closed Riemannian manifolds with |Rm( gi)| ≤ C1 and diam( Mi, g i) ≤ C2, and assume ( Mi, g i) → (Xd, d X ) in the Gromov-Hausdorff sense with d < n. This is the collapsing regime where classical non-collapsed Cheeger-Gromov compactness is not directly applicable. At an introductory level, the CFG mechanism used later in this thesis has three steps: (1) local non-collapsing after passing to local universal covers, (2) global fibration over the limit with almost-flat fibers, and (3) nilpotent algebraic structure and a canonical N -action. We first start with a characterization of the limit when curvature is bounded. 

Theorem 1.9 (GH compactness with bounded curvature) . Let {(M ni , g i)} be a sequence of closed n-manifolds with |Rm( gi)| ≤ C1 and diam( Mi, g i) ≤ C2. Then, after passing to a subsequence, (Mi, g i) converges in GH to a compact metric space (X, d X ). If the sequence 

26 collapses, Fukaya showed that the Hausdorff dimension of X is still an integer d ≤ n [29]. 

To fully understand the collapsing sequence and get regularity, we need the following steps. 

Step 1: local universal covers are non-collapsed. The key point is that collapsing in the base does not force collapsing on small local universal covers. One uses a uniform lower bound for the conjugate radius, together with the lower bound for homotopically trivial closed geodesics. 

Theorem 1.10 (Klingenberg’s lemma for contractible closed geodesics) . Let (M, g ) be com-plete with sectional curvature Kg ≤ Λ2 for some Λ > 0. If γ is a homotopically trivial closed geodesic, then 

L(γ) ≥ 2π

Λ .

A standard reference for this estimate is Klingenberg’s injectivity-radius argument in com-parison geometry; see, for example, [18, Ch. 6] and [23, Ch. 13]. In the collapsing context, this is one of the inputs in Fukaya’s local analysis of collapsing and equivariant limits [26, 28, 19]. Combined with a uniform lower conjugate-radius bound, Theorem 1.10 gives a uniform lower local injectivity-radius bound on the lifted balls, hence local non-collapsing there. Therefore one can pass to equivariant Cheeger-Gromov limits on local universal covers. 

Definition 1.18 (Local convergence in the collapsing setting) . Suppose (M ni , g i) → (Xd, g ∞)

in GH with d < n . We say the convergence is local Ck,α if there exists r > 0 (independent of i) such that for every xi → x∞ one has equivariant convergence 

( ˜B˜xi (r), ˜gi, G i) ( ˜B˜x∞ (r), ˜g∞, G ∞)(Bxi (r), g i) (Bx∞ (r), g ∞). 

> Ck,α
> πiπ∞
> GH

27 Step 2: global fibration and almost-flat fibers. After the local model is understood, one globalizes to a fibration over the limit space. In the bounded-curvature setting used here, this is the classical CFG fibration picture. The regularity is latter improved to C2,α 

by Naber-Zhang [46] and related refinements such as [61]. We adapt their result so that the fiber structure can be easily derived since to make second fundamental form well defined, we need the fibration map to be at least C2

AF −1 

> i(x)

(V, W ) = Hess Fi(V, W )

|∇ Fi| .

Theorem 1.11 (Cheeger-Fukaya-Gromov fibration theorem [19]) . Let {(M ni , g i)} be a se-quence of closed Riemannian n-manifolds with |Rm( gi)| ≤ C1 and diam( Mi, g i) ≤ C2, and suppose (Mi, g i) → (Xd, g ∞) in GH, where (Xd, g ∞) is a compact Riemannian manifold with 

d < n .Then for all sufficiently large i, and each fixed α ∈ (0 , 1) , there is a C2,α fiber-bundle map 

Fi : ( Mi, g i) → (X, g ∞)

such that: 1. Fi is a τi-GH approximation, with τi → 0.2. ∥Fi∥C2,α ≤ C uniformly in i.3. For each fiber F −1 

> i

(x), the second fundamental form is uniformly bounded (equivalently, 

∥AF −1 

> i(x)

∥C0,α ≤ C0). 4. Fi is an almost-Riemannian submersion: for every horizontal vector v,

(1 − τi)|v|gi ≤ | dF i(v)|g∞ ≤ (1 + τi)|v|gi .

28 5. Each fiber is an infranilmanifold, namely F −1 

> i

(x) ∼= Γ \N , where N is simply connected nilpotent and Γ ≤ N ⋊ Aut( N ) is cocompact. 6. With Λ := N ∩ Γ, one has Λ ◁ Γ and #(Λ \Γ) ≤ w0(n).

The proof of the fibration theorem can be found in Appendix A. The fiber geometry is controlled quantitatively by combining bounded ambient curvature and bounded second fundamental form with the Gauss equation: 

|Rm fiber | ≤ C |Rm Mi | + |Afiber |2.

Since fiber diameters go to zero in the collapsing regime, one obtains almost-flat fibers in the sense of Gromov-Ruh [32, 52]. 

Theorem 1.12 (Ruh’s theorem on almost-flat manifolds [52]) . There exists ε(n) > 0 such that if (Zn, h ) is closed and satisfies 

diam( Z, h )2 sup 

> Z

|Rm( h)| ≤ ε(n),

Then we have Z ≃ Γ\N , where N is a simply-connected nilpotent Lie group, and Γ is a cocompact subgroup of NL ⋊ Aut( N ), where NL ∼= N is the left translation subgroup, i.e., Z

is an infranilmanifold. Also, Λ = N ∩ Γ is normal in Γ with #(Λ \Γ) ≤ w0 for some constant 

w0 = w0(n). Equivalently, Z admits a finite covering by a compact nilmanifold (Example 1.4). 

The nilpotent manifold collapsing to a point in Example 1.9 can be viewed as a specail case of Theorem 1.11 when X = {pt }.

Step 3: nilpotent algebraic structure and N -action. The almost-flat conclusion is promoted to a canonical nilpotent structure in CFG: locally over simply connected base sets, 29 the lifted fibration carries a nilpotent Lie group action that is compatible with changing trivializations. 

Definition 1.19 (Affine structure, affine equivalence, and N -invariance) . An affine struc-ture on a manifold Z is a flat torsion-free connection ∇ on T Z . Two affinely structured manifolds (Z, ∇Z ) and (W, ∇W ) are affinely equivalent if a diffeomorphism Φ : Z → W

satisfies Φ∗∇W = ∇Z .Given a local CFG trivialization over simply connected U ⊆ X, ^F −1 

> i

(U ) ∼= U × N , the N -action is the right action on the nilpotent factor. A tensor on ^F −1 

> i

(U ) is N -invariant if it is invariant under this action. 

Theorem 1.13 (Existence of nilpotent action) . For each simply connected open set U ⊆ X,and all large i, the structure group of the fiberation reduced to Aff 0(Γ \N ) ∼= CAff( N )(Λ) /Λ ⊂

Aff(Γ \N ). Thus there exists a global N -action on Mi for i sufficiently large. 

Equivalently, each fiber has the form Γ \N (up to finite extension), where N is simply connected nilpotent and Γ ≤ N L ⋊ Aut( N ) is cocompact. This is the algebraic structure that later supports the invariant-geometry and regularity arguments in Chapter 4. 30 Chapter 2 Special Metrics and Moduli Space 

This chapter introduces the two types of special metrics studied in this thesis — locally conformally flat (LCF) metrics, Yamabe metrics. §2.1 defines LCF manifolds, develops the Kleinian group framework via the developing map (Schoen-Yau [59]), and collects the key analytic estimates (Kato inequalities, Tian-Viaclovsky volume comparison) needed for the moduli theory. §2.2 reviews the resolution of the Yamabe problem [72, 67, 7, 53] and its orbifold analog. §2.3 presents the Positive Mass Theorem and its LCF variant, which is the main technical tool in Schoen’s solution of the Yamabe problem for LCF manifolds. §2.4 gives the standard examples and the known classification results for compact LCF manifolds. 

# 2.1 Locally Conformally Flat Metrics 

Locally conformally flat (LCF) metrics generalize constant-curvature surfaces to higher di-mensions. In dimension n = 2, every Riemannian metric is locally conformally flat. For 

n ≥ 3, conformal flatness is characterized by the Weyl and Cotton tensors. 

Definition 2.1 (Locally conformally flat manifold) . A Riemannian manifold (M n, g ) is 

locally conformally flat (LCF) if for every p ∈ M , there exists a neighborhood U and a 

31 chart ϕ : B ⊂ Rn → U such that ϕ∗g = λ g Rn for some smooth positive function λ on B.

Definition 2.2 (Weyl and Cotton tensors) . Let (M n, g ) be a Riemannian manifold with Riemann tensor Rijkl , Ricci tensor Rij , and scalar curvature S. The Weyl tensor is defined by 

Wijkl = Rijkl − 1

n − 2

 Rik gjl − Ril gjk + Rjl gik − Rjk gil 



+ S

(n − 1)( n − 2) 

 gik gjl − gil gjk 

.

Let 

Aij = 1

n − 2



Rij − S

2( n − 1) gij 



be the Schouten tensor. The Cotton tensor is 

Cijk = ∇kAij − ∇ j Aik = ∇kRij − ∇ j Rik − 12( n − 1) 

 gij ∇kS − gik ∇j S.

The next theorem gives the equivalence between these tensor identities and local conformal flatness. 

Theorem 2.1 (Weyl-Schouten theorem [12, Ch. 1]) . Let (M n, g ) be a Riemannian manifold. 1. If n ≥ 4, then (M, g ) is locally conformally flat if and only if W ≡ 0.2. If n = 3 , then (M, g ) is locally conformally flat if and only if C ≡ 0.

A direct computation yields 

∇lWlijk = n − 3

n − 2 Cijk . (2.1) 32 Hence, if W ≡ 0 and the scalar curvature is constant (for example, for a Yamabe metric), then 

∇kRij − ∇ j Rik = 0 , (2.2) which is the harmonic curvature condition. This chain of implications is the analytic starting point for the Ricci estimates below. 

## 2.1.1 Local Analytic Aspect for LCF manifolds 

First, we will discuss the local analytic aspect of LCF manifolds and their consequence. In particular, we study the local curvature properties of LCF manifolds. Because of curvature property of LCF, there is a very restrictive classification of the product structure that has LCF property. 

Theorem 2.2 (LCF product classification [42]) . Let (M n, g ) = ( M n1 

> 1

, g 1) × (M n2 

> 2

, g 2) be an LCF Riemannian product with n = n1 + n2 ≥ 3. Then one of the following holds: 1. Cylinder : (M1, g 1) is a space form, and (M2, g 2) is one dimensional, so (M, g ) is a cylinder M n1 

> 1

× R (or its quotient). 2. Bi-space-form : (M1, g 1) and (M2, g 2) are space forms of opposite curvatures: κ1 =

−κ2̸ = 0 , so the scalar curvature is zero. 3. Flat : (M, g ) is flat. Proof. For n ≥ 4, ( M, g ) is LCF iff W ≡ 0; for n = 3, LCF is equivalent to C ≡ 0. We treat 

n ≥ 4 in detail. The case n = 3 forces ( n1, n 2) ∈ { (1 , 2) , (2 , 1) } and falls into case (1); the analogous Cotton-tensor computation gives the same conclusion. 33 Step 1: Both factors are Einstein. Let a, b (resp. α, β ) index an orthonormal frame for T M 1 (resp. T M 2). On a Riemannian product, cross-curvature and cross-Ricci tensors vanish, so the mixed Weyl component is 

Waαbβ = − 1

n − 2

 (Ric 1)ab (g2)αβ + ( Ric 2)αβ (g1)ab 

 + S1 + S2

(n − 1)( n − 2) (g1)ab (g2)αβ .

Setting Waαbβ = 0 and contracting with ( g2)αβ gives (Ric 1)ab =

S1 + S2

n − 1 − S2

n2



(g1)ab ,

so M1 is Einstein. For n1 ≥ 2, Schur’s lemma then forces S1 + S2, and hence S2, to be constant; a symmetric contraction with ( g1)ab shows M2 is Einstein with constant S1.

Step 2: Both factors are space forms. With Ric i = λigi constant, the pure M1 compo-nents of W ≡ 0 reduce to (R1)abcd = κ1

 (g1)ac (g1)bd − (g1)ad (g1)bc 

, κ1 = 2( n − 1) λ1 − n1λ1 − n2λ2

(n − 1)( n − 2) ,

so M1 is a space form of sectional curvature κ1. Analogously M2 is a space form of curvature 

κ2.

Step 3: Classification. Substituting Ric i = ( ni − 1) κigi into the mixed Weyl condition yields (n1 − 1)( n2 − 1)( κ1 + κ2) = 0 .

• n1 = 1 or n2 = 1: the one-dimensional factor is flat; the other is any space form. This gives case (1). 

• n1, n 2 ≥ 2 and κ1 + κ2 = 0, κi̸ = 0: bi-space-form, case (2). 34 • n1, n 2 ≥ 2 and κ1 = κ2 = 0: ( M, g ) is flat, case (3). This theorem shows that LCF product metrics are essentially cylinders M ×R or bi-spherical spaces Sk(κ) × Hn−k(κ) (see §2.4). When W ≡ 0 and Rg is constant (for example, for a Yamabe metric), (2.2) implies ∆ Ric = Ric ∗ Ric + Ric ∗ Rm .

The following estimates for the Ricci curvature of LCF manifolds are used in the compacti-fication theory of Chapter 3. 

Lemma 2.3 (Kato’s inequality for Ricci curvature) . For any tensor T : |∇| T || 2 ≤ |∇ T |2

(classical Kato inequality ). For a complete LCF manifold with constant scalar curvature, the harmonic curvature condition and W ≡ 0 imply: 

∆| Ric | + C| Ric |2 ≥ 0. (2.3) 

Proof. Assume ( M, g ) is LCF with constant scalar curvature. Then ∇S ≡ 0, so from (2.2) we get the harmonic curvature identity 

∇j Rik − ∇ iRjk = 0 .

Using this identity and commuting covariant derivatives, one obtains the Ricci equation ∆ Ric = ∇i(∇iRjk ) = gil ∇l∇j Rik = Ric ∗ Ric + Ric ∗ Rm .

Since W ≡ 0, the full curvature tensor is algebraically controlled by Ricci and scalar curva-35 ture; because S is constant, this gives 

| Rm | ≤ C | Ric |.

Hence 

|∆ Ric | ≤ C | Ric |2.

Now apply the Bochner identity to Ric: 12∆| Ric |2 = ⟨∆ Ric , Ric ⟩ + |∇ Ric |2

= | Ric | ∆| Ric | + |∇| Ric || 2.

Therefore 

| Ric | ∆| Ric | = ⟨∆ Ric , Ric ⟩ + |∇ Ric |2 − |∇| Ric || 2.

By classical Kato inequality, |∇| Ric || 2 ≤ |∇ Ric |2, so 

| Ric | ∆| Ric | ≥ ⟨ ∆ Ric , Ric ⟩ ≥ − C| Ric |3.

At points where | Ric | > 0, divide by | Ric | to get ∆| Ric | + C| Ric |2 ≥ 0.

By standard barrier/approximation at the zero set, the same inequality holds weakly on all of M .A direct consequence of (2.3) is the following ϵ-regularity. 36 Lemma 2.4 (ε-regularity for Ricci curvature [64]) . Let (M n, g ) be a complete LCF, scalar-flat manifold with Y (M, [g]) ≥ δ > 0. There exist C and ε0 (depending on n, δ) such that if 

R  

> Br(p)

| Ric |n/ 2 dV g < ε 0, then: 

sup 

> Br/ 2(p)

| Ric | ≤ Cr2

Z  

> Br(p)

| Ric |n/ 2 dV g

2/n 

. (2.4) The proof applies Moser iteration to (2.3), using the Sobolev inequality provided by Y (M, [g]) ≥

δ. Since the proof is standard, we will not write the detailed in here and sketch the proof later in Lemma 3.2. On the other hand, since the symmetry of the Ricci curvature is identical with the second fundamental form in [54], we have the following Refined Kato inequality. 

Lemma 2.5 (Refined Kato inequality under LCF) . Let (M n, g ) be a complete LCF, scalar-flat manifold ( n ≥ 3). Under the harmonic curvature condition: 



1 + 2

n



|∇| Ric || 2 ≤ |∇ Ric |2, (2.5) 

and consequently ∆| Ric |1−2/n ≥ − C| Ric |2−2/n .Proof. Following the refined Kato strategy in the literature (cf. [10]), we work at a fixed point p ∈ M and choose an orthonormal frame that diagonalizes Ric at p. Write Rij = λiδij 

at p. Then 4| Ric |2|∇| Ric || 2 = |∇| Ric |2|2 =

> n

X

> k=1

 nX

> i=1

2Rii ∇kRii 

2

≤ 4| Ric |2

> n

X

> k=1
> n

X

> i=1

(∇kRii )2,

37 so 

|∇| Ric || 2 ≤

> n

X

> k=1
> n

X

> i=1

(∇kRii )2.

Because Rg ≡ 0, we have Pnj=1 Rjj = 0 and hence ∇i

Pnj=1 Rjj = 0. Therefore 

X

> k,i

(∇kRii )2 = X

> i̸=k

(∇kRii )2 + X

> i

(∇iRii )2

= X

> i̸=k

(∇kRii )2 + X

> i

 X  

> j̸=i

∇iRjj 

2

≤ X

> i̸=k

(∇kRii )2 + ( n − 1) X

> i

X 

> j̸=i

(∇iRjj )2

= n X

> i̸=k

(∇kRii )2.

Under harmonic curvature (Codazzi), 

∇kRii = ∇iRki (i̸ = k),

so 

X

> k,i

(∇kRii )2 ≤ n X

> i̸=k

(∇iRki )2.

Combining this with the standard decomposition of |∇ Ric |2 into diagonal and off-diagonal parts gives the refined estimate 



1 + 2

n



|∇| Ric || 2 ≤ |∇ Ric |2,

which is (2.5). For the differential inequality, apply the Kato-type Bochner computation from Lemma 2.3 38 and combine it with (2.5): ∆| Ric | ≥ − C| Ric |2 =⇒ ∆| Ric |1− 2 

> n

≥ − C| Ric |2− 2 

> n

.

Follow the same type of estimate as in [10], we can prove the following decay estimate for LCF ALE manifolds. 

Theorem 2.6 (ALE order from refined Kato’s inequality [10]) . Let (M n, g ) be a complete LCF, scalar-flat ALE manifold satisfying the hypotheses of Lemma 2.5. Then for any ε > 0,[10] yields the pointwise decay estimates 

| Ric |1− 2 

> n

= O(r−n+2+ ε),

| Ric | = O(r−n+ε).

Consequently, (M, g ) is an ALE space of order n − 2 − ε (in the sense of Definition 1.6 in Chapter 1) for any ε > 0, i.e. the metric satisfies 

gij = δij + O(r−n+2+ ε).

If we only assume R 

> M

| Ric |n/ 2 dV g ≤ Λ < ∞ for a complete non-compact, locally non-collapsing, LCF manifold, due to the lack of Bishop-Gromov volume comparison, we cannot directly get an ALE coordinate at infinity, like the Ricci flat case in [10]. We need the following theorem to determine the structure. 

Theorem 2.7 (Tian-Viaclovsky volume comparison [64, 65]) . Let (M n, g ) be a complete LCF, scalar-flat manifold with Euclidean volume growth Vol( Bt) ≥ V t n, R 

> M

| Ric |n/ 2 dV g ≤

Λ < ∞, and Y (M, [g]) ≥ δ > 0. Then Vol( Br(p)) ≤ Cr n for all p, r, and (M, g ) has finitely 

39 many ends. 

Thus, we have the desired volume upper bound to construct the ALE coordinate at infinity using [10]. Consequently, we have 

Corollary 2.8. Let (M n, g ) be a complete LCF, scalar-flat manifold with Euclidean volume growth Vol( Bt) ≥ V t n, R 

> M

| Ric |n/ 2 dV g ≤ Λ < ∞, and Y (M, [g]) ≥ δ > 0. Then, (M, g ) is an ALE space of order n − 2 − ε (in the sense of Definition 1.6 in Chapter 1) for any ε > 0.

Lemma 2.4 and Theorem 2.7 together are the analytic engine of the Tian-Viaclovsky com-pactification: the ε-regularity controls curvature away from finitely many concentration points, and the volume comparison prevents non-ALE end behavior. Thus, we have. These tools are applied in Chapter 3. 

## 2.1.2 Global Geometric Aspect for LCF manifolds 

The defining feature of a locally conformally flat manifold is the existence of local conformal charts into Rn. A key insight is that these local charts can be analytically continued over the universal cover to produce a globally defined conformal map into Sn. We now describe this construction and the additional structure it carries. 

Definition 2.3 (Developing map) . Let (M n, g ) be a locally conformally flat manifold with 

n ≥ 3. Since each point p ∈ M admits a neighborhood Up with a conformal diffeomorphism 

ϕp : ( Up, g ) → (Vp, g Rn ), via stereographic projection σ : Rn ,→ Sn one regards each chart as a conformal map into Sn. Performing analytic continuation along paths in the universal cover fM — starting from an initial chart at a basepoint and propagating consistently along any path by composing overlapping charts — yields, since fM is simply connected, a globally defined conformal local diffeomorphism 

ϕ : fM −→ Sn,

40 called the developing map . In general, ϕ is a conformal immersion but need not be injective or surjective. 

Theorem 2.9 (Liouville’s theorem) . Let U, V ⊂ Sn be open connected subsets with n ≥

3, and f : U → V a conformal diffeomorphism. Then f extends uniquely to a conformal automorphism of Sn.

Definition 2.4 (Holonomy representation) . Let (M n, g ) be a locally conformally flat man-ifold with developing map ϕ : fM → Sn. Each deck transformation γ ∈ π1(M ) satisfies an equivariance relation 

ϕ ◦ γ = ρ(γ) ◦ ϕ

for a unique element ρ(γ) ∈ M¨ ob( Sn) ∼= O+(n + 1 , 1) , given by Liouville’s theorem (Theo-rem 2.9). The resulting group homomorphism 

ρ : π1(M ) −→ M¨ ob( Sn)

is the holonomy representation . Its image Γ = ρ(π1(M )) is the Kleinian holonomy group .

Under the additional assumption Rg ≥ 0, Schoen and Yau showed that the developing map is in fact an embedding. 

Theorem 2.10 (Schoen-Yau conformal embedding [59]) . Let (M n, g ) be a complete LCF manifold with n ≥ 3 and Rg ≥ 0. Then the developing map ϕ : fM → Sn is a conformal embedding. 

Remark 2.1. When Y (M, [g]) ≥ 0 (which implies Rg ≥ 0 in the Yamabe class), The-orem 2.10 upgrades the developing map from a mere immersion to an embedding: ϕ( fM )41 is a proper open subdomain of Sn. By Liouville’s theorem, each deck transformation then acts on ϕ( fM ) by the restriction of a global M¨ obius transformation, so the holonomy ρ of Definition 2.4 is injective and Γ = ρ(π1(M )) embeds as a discrete subgroup of M¨ ob( Sn) ∼=

O+(n + 1 , 1) . The pair (ϕ, ρ ) thus endows (M, g ) with a Kleinian structure : the domain of discontinuity Ω ⊂ Sn is the maximal open set on which Γ acts properly discontinuously, and the limit set Λ = Sn \ Ω encodes the asymptotic geometry of M .

The pair ( ϕ, ρ ) endows ( M, g ) with the following structure. 

Definition 2.5 (Kleinian structure [59]) . With Γ = ρ(π1(M )) ≤ M¨ ob( Sn):

• The domain of discontinuity Ω ⊆ Sn is the maximal open set on which Γ acts properly discontinuously. 

• The limit set Λ = Sn \ Ω is the minimal Γ-invariant closed subset of Sn.

(M, g ) is conformally equivalent to ϕ( fM )/Γ ⊆ Ω/Γ.

Definition 2.6 (Elliptic, parabolic, hyperbolic elements) . An element γ ∈ M¨ ob( Sn) ∼=Isom( Hn+1 ) is: 

• elliptic if it has a fixed point in Hn+1 ;

• parabolic if it has exactly one fixed point on Sn;

• hyperbolic if it has two distinct fixed points on Sn.Elements of finite order are elliptic; infinite-order elements acting freely on Ω are parabolic or hyperbolic. 

The limit set Λ and the domain of discontinuity Ω encode the coarse structure of the LCF manifold: the smaller Λ is (in Hausdorff dimension), the closer ( M, g ) is to a spherical space form, and Schottky-type structure (with Λ a Cantor set) corresponds to multi-ended 42 connected sums. The classification results in §2.4 are organized by the geometry of Λ. 

Definition 2.7 (Conformal connected sum [36]) . Let (M1, g 1) and (M2, g 2) be LCF orbifolds. Fix an orientation-preserving conformal embedding of an annulus A ∼= [0 , 1] × Sn−1 ,→

Sn, with complementary components D1, D 2 ∼= Bn. The conformal connected sum 

(M1, g 1)# C (M2, g 2) is the LCF orbifold obtained by gluing (Mj \ ψj (Ej ), g j ) along ψj (A)

via orientation-preserving conformal maps ψj : Ej → Mj (Ej = A ∪ Dj ). 

Example 2.1 (S3 ×S1#S3 ×S1). Start from two loxodromic M¨ obius transformations γ1, γ 2 ∈

M¨ ob( S4) with disjoint isometric spheres, so that 

Γ = ⟨γ1, γ 2⟩ ∼= F2

is a classical Schottky group. Its domain of discontinuity Ω ⊂ S4 is connected, and the quotient 

M = Ω /Γ

is a compact LCF 4-manifold. Topologically, this quotient is 

M ∼= ( S3 × S1)#( S3 × S1),

since each generator contributes one S3 × S1 handle in the conformal connected-sum picture. Its limit set 

Λ = S4 \ Ω43 is a Cantor set: equivalently, 

Λ = \

> m≥1

[

> |w|=m

Bw,

where w runs over reduced words in γ±11 , γ ±12 and Bw are the nested images of the fundamental round balls. This is a compact, perfect, totally disconnected set. 

Regarding the conformal group structure. Note that for a manifold equipped with a Kleinian structure. The fundamental group can be viewed as a subgroup of M¨ ob( Sn) ≃ O+(n + 1 , 1). Thus, we can use the following Selberg’s lemma to characterize these groups. 

Theorem 2.11 (Selberg’s lemma [60]) . A finitely generated subgroup of GL (N, C) has a finite-index torsion-free subgroup, and in fact a normal finite-index torsion-free subgroup. 

In particular, any Kleinian LCF manifold ( M, g ) with π1(M ) finitely generated has a finite orbifold cover that is a smooth manifold. This is used in §3.3. Lastly, we will give the definition of a special type of orbifold that will appear a lot of places in this thesis. 

Definition 2.8 (Football orbifold) . A football orbifold is Sn/Γ where Γ ≤ O(n) ⊂

O(n + 1) acts with exactly two antipodal fixed points. The quotient metric is spherical, and πorb 1 (Sn/Γ) ∼= Γ . (cf. Example 1.5). 

In particular, football orbifolds are LCF. When n is odds, the only football orbifolds are 

Sn/Z2, by a elementary eigenvalue argument. The geometric tools above — developing maps, Kleinian groups, conformal connected sums — characterize the global topology of LCF manifolds. To analyze their metric properties and control their degeneration in moduli space, we need to combine analytic estimates and global structure of LCF manifolds. 44 The next canonical object in the LCF world is the Yamabe metric — the constant scalar curvature representative in a conformal class — whose existence is guaranteed by the Yamabe theorem. 

# 2.2 Yamabe Metrics 

The Yamabe problem asks whether every compact Riemannian manifold ( M n, g ) admits a metric of constant scalar curvature in its conformal class. This was posed by Yamabe [72] and resolved by Trudinger, Aubin, and Schoen over the period 1968–1984. The resolution in the locally conformally flat case uses the Positive Mass Theorem ( §2.3) and is central to this thesis. 

Definition 2.9 (Yamabe constant and Yamabe invariant) . Let (M n, g ) be a compact Rie-mannian manifold with n ≥ 3. Recall the Yamabe functional from (1.1) :

Yg(u) = 

Z

> M

u L gu dV g

∥u∥2

> L2n/ (n−2)

, u ∈ W 1,2(M ), u ̸ ≡ 0.

The Yamabe constant of the conformal class [g] is 

Y (M, [g]) = inf   

> 0̸=u∈W1,2(M)

Yg(u) = inf 

> ˜g∈[g]

Vol(˜ g)−(n−2) /n 

Z

> M

R˜g dV ˜g.

The functional is scaling-invariant, hence Y (M, [g]) depends only on the conformal class. A 

Yamabe metric is a metric ˜g ∈ [g] realizing the infimum. The Yamabe invariant of M

is Y (M ) = sup [g] Y (M, [g]) .For a Riemannian orbifold (M, g ), the orbifold Yamabe constant Yorb (M, [g]) is defined by the same infimum over the orbifold conformal class. 

Theorem 2.12 (Yamabe problem [72, 67, 7, 53]) . Let (M n, g ) be a compact Riemannian 

45 manifold without boundary, n ≥ 3. Then every conformal class [g] contains a smooth metric of constant scalar curvature (a Yamabe metric). Equivalently, the Yamabe equation 

Lgu = λ u (n+2) /(n−2) , u > 0 smooth , λ = Y (M, [g]) , (2.6) 

has a smooth positive solution. Proof sketch. The proof was completed in four stages. 

Step 1 (Yamabe 1960). Writing ˜ g = u4/(n−2) g, the Yamabe equation (2.6) is the Euler-Lagrange equation for Yg. A minimizing sequence {uk} for Yg is bounded in W 1,2, but the Sobolev embedding is only continuous (not compact) at the critical exponent 2 ∗ = 2 n/ (n−2), so concentration phenomena may occur. 

Step 2 (Trudinger 1968). Corrected Yamabe’s argument; proved existence when Y (M, [g]) ≤

0 by a subcritical approximation: replace the exponent 2 ∗ by 2 ∗ − ε, obtain subcritical min-imizers uε by compact Sobolev embedding, and pass to the limit. 

Step 3 (Aubin 1976). For Y > 0, bubbling may occur. The key criterion is Y (M, [g]) <Y (Sn): if this holds, a minimizing sequence cannot concentrate, so a minimizer exists. Aubin constructed test functions uε (cutoffs of the Euclidean bubble (1 + |x|2)−(n−2) /2 near a point 

p) and showed Yg(uε) < Y (Sn) when n ≥ 6 and ( M, g ) is not LCF, using the Weyl tensor at p to gain a negative correction. In the LCF case W ≡ 0, this correction vanishes to all orders, so Aubin’s argument does not apply and a fundamentally different tool is needed. 
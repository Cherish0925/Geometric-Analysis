---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Contents]

• (CPn,gFS), where gFS is the Fubini-Study metric. We will not have time
to prove this case in these lectures, since the nicest proof involves the theory of deformations of K¨ahler-Einstein metrics, and needs a considerable
amount of background in complex geometry.

$$
\\left(\\mathbb{C}\\mathbb{P}^n,g\_{FS}\\right)
$$

It is remarked that there are examples of positive Einstein metrics admitting nontrivial infinitesimal Einstein deformations, yet which are rigid as Einstein metrics,
for example _S2 ×_ CP2‘ \[Koi82\]. This shows that, in general, determining the
Kuranishi is not an easy problem.

$$
S^{2}\\times\\mathbb{C P}^{2\\ell}
$$

#### 5.3. The zero case

We saw that, in the case of a flat metric, _H1_ consists of parallel sections. The
Kuranishi map turns out to be identically zero in this case, since all of these are
“integrable”, corresponding to deformations of the flat structure.

$$
H^{1}
$$

Exercise 4.16. Determine the moduli space of flat structures on a 2-torus. (Hint:
a flat structure is equivalent to a choice of lattice in R2.)

$$
\\mathbb{R}^{2}.
$$

Another special class of Ricci-flat metrics are Calabi-Yau metrics, which are
K¨ahler Ricci-flat metrics. It is known that Calabi-Yau metrics are _unobstructed:_

Theorem 4.17 (Bogomolov-Tian). _For a Calabi-Yau metric_ ( _X,g), the Kuranishi_
_map_ Ψ _≡ 0\. That is, every infinitesimal Einstein deformation integrates to an_
_actual deformation._

$$
\\Psi\\equiv0
$$

We will not discuss the proof, since it involves a considerable amount of complex
geometry, see \[Bog78, Tia87\].

* * *

#### 5\. RIGIDITY OF EINSTEIN METRICS

We also mention that Dai-Wei-Wang have proved stability results for manifolds
admitting a parallel spinor \[DWW05\].

* * *

* * *

# Quadratic curvature functionals

### 1\. Quadratic curvature functionals

First recall that the curvature tensor admits the orthogonal decomposition

(5.1)

$$
R m=W+\\frac{1}{n-2}E\\oslash g+\\frac{R}{2n(n-1)}g\\oslash g,
$$

where

$$
E=Ric-\\frac{R}{n}g
$$

(5.2)

is the _traceless Ricci tensor._ The 7 symbol is the Kulkarni-Nomizu product, which
takes 2 symmetric (0,2) tensors and produces a (0,4) tensor with the same algebraic
symmetries of the curvature tensor, and is defined by

$$
\\bigcirc
$$

$$
\\begin{aligned}{A\\circlearrowleft B(X,Y,Z,W)=}&{{}A(X,Z)B(Y,W)-A(Y,Z)B(X,W)}\ {}&{{}-A(X,W)B(Y,Z)+A(Y,W)B(X,Z).}\ \\end{aligned}
$$

The tensor _W_ occurring in (5.1) is called the Weyl tensor (use (5.1) to _define_
the Weyl tensor), and is the part of the curvature tensor which lies in the kernel of
the Ricci contraction map. An important property of the Weyl tensor is given by:

Exercise 5.1. The Weyl tensor, viewed as a (1,3)-tensor with components Wijkl,
is pointwise conformally invariant. That is, if _˜g_ = _f · g_ where _f_ is a strictly positive
function, then W(˜g) = _W_ (g).

$$
W\_{ijk}^{\\quad l}
$$

$$
\\tilde{g}=f\\cdot g
$$

$$
W(\\tilde{g})=W(g)
$$

We will now turn our attention to functionals on the space of Riemannian
metrics _M_ which are quadratic in the curvature; see \[Bes08, Bla00, Smo05\] for
surveys.

A basis for the space of quadratic curvature functionals is
∫ ∫

(5.3)

$$
\\mathcal{W}(g)=\\int\_{M}\|W\_{g}\|^{2}d V\_{g},\ \\rho(g)=\\int\_{M}\|R i c\_{g}\|^{2}d V\_{g},\ \\mathcal{S}(g)=\\int\_{M}R\_{g}^{2}d V\_{g}.
$$

Let us now restrict the rest of this lecture to dimension four. In this dimension, for
_M_ compact without boundary, the Chern-Gauss-Bonnet formula states that
∫ ∫ ∫

(5.4)

$$
32\\pi^{2}\\chi(M)=\\int\_{M}\|W\_{g}\|^{2}d V\_{g}-2\\int\_{M}\|R i c\_{g}\|^{2}d V\_{g}+\\frac{2}{3}\\int\_{M}R\_{g}^{2}d V\_{g},
$$

where _χ(M_) is the Euler characteristic of _M._ This implies that any one of the
functionals in (5.3) can be written as a linear combination of the other two (plus a
topological term).

$$
\\chi(M)
$$

Remark 5.2. We are using the tensor norm on \|W \|2, that is \|W \|2 = W ijklWijkl,
where all indices are summed from 1 to 4. This differs from the norm of _W_ as a

$$
\|W\|^{2}
$$

$$
\|W\|^{2}=W^{i j k l}W\_{i j k l},
$$

$$
W
$$ mapping on 2-forms by a factor of 4, that is

(5.5)

$$
\|W\|^{2}=4\|\\widehat{W}\|^{2}
$$

(see below for the definition of Wc).

$$
\\widehat{W})
$$

We next present the Euler-Lagrange equations of these functionals:

Proposition 5.3 (Berger \[Ber70\]). _The Euler-Lagrange equations of the functionals in_ (5.3) _are given by_
()

(5.6)

$$
(\\nabla\\mathcal{W}) _{i j}=-4\\Big(\\nabla^{k}\\nabla^{l}W_{i k j l}+\\frac{1}{2}R^{k l}W\_{i k j l}\\Big),
$$

(5.7)

$$
(\\nabla\\rho) _{i j}=-\\Delta(R i c)_{i j}-2R\_{i k j l}R^{k l}+\\nabla\_{i}\\nabla\_{j}R-\\frac{1}{2}(\\Delta R)g\_{i j}+\\frac{1}{2}\|R i c\|^{2}g\_{i j},
$$

(5.8)

$$
(\\nabla\\mathcal{S}) _{i j}=2\\nabla_{i}\\nabla\_{j}R-2(\\Delta R)g\_{i j}-2R R\_{i j}+\\frac{1}{2}R^{2}g\_{i j}.
$$

Outline of proof. Let _g(t_) be a path of metrics such that g(0) = _g_ and
g′(0) = h. Using the formula for the derivative of the inverse of a matrix

$$
g(t)
$$

$$
g(0)=g
$$

$$
g^{\\prime}(0)=h
$$

(5.9)

$$
\\left(g^{p q}\\right)^{\\prime}=-g^{p k}h\_{k l}g^{l q},
$$

the formula for the derivative of the volume element (1.16), and the formula for
the linearization of the Ricci tensor (1.25), equation (5.7) follows upon integrating
by parts. Next, recalling the formula for the linearization of the scalar curvature
(1.14), the formula (5.8) follows similarly.

Finally, instead of computing the linearization of the Weyl tensor directly, use
the Chern-Gauss-Bonnet formula (5.4) to express the Euler-Lagrange equations
of _W_ as a linear combination of the Euler-Lagrange equations of the other two
functionals. Note that the formula obtained in this way shows that _∇W_ depends
only upon the Ricci tensor (and it covariant derivatives). Use the Bianchi identities
to show these are equivalent to the form (5.6).

We point out some obvious critical metrics:

Proposition 5.4. _Any Einstein metric is critical for all of the functionals W,ρ,_
_and S. Also, any scalar-flat metric is critical for S._

Proof. These statements follow easily from the Euler-Lagrange equations
computed above in Proposition 5.3.

We note that the functional _S_ has been deeply studied in K¨ahler geometry;
critical points of this functional when restricted to a K¨ahler class are known as
extremal K¨ahler metrics, see \[Cal82, Cal85\]. The Euler-Lagrange equations of
the restricted functional are that the gradient of the scalar curvature is the real
part of a holomorphic vector field. In particular, constant scalar curvature K¨ahler
metrics are extremal.

Also, the functional _W_ has been studied in depth (see for example \[Gur98\]),
and it was introduced by Rudolf Bach in 1921 \[Bac21\]. Thus the Euler-Lagrange
tensor _∇W_ is known as the _Bach tensor._ Conformal invariance of the functional
_W_ implies that the Bach tensor is also conformally invariant.

* * *

### 2\. Curvature in dimension four

If (M4,g) is oriented, the Hodge star operator on Λ2 satisfies ∗2 = I. The space of
2-forms then decomposes into

$$
\\Lambda^{2}
$$

$$
\\left(M^{4},g\\right)
$$

$$
\*^{2}=I
$$

(5.10)

$$
\\Lambda^{2}=\\Lambda\_{+}^{2}\\oplus\\Lambda\_{-}^{2},
$$

the +1 and _−1_ eigenspaces of the Hodge star operator, respectively. Note that
dimR(Λ2) = 6, and dimR(Λ2±) = 3\. Elements of Λ2+ are called self-dual 2-forms,
and elements of Λ2− are called anti-self-dual 2-forms

$$
dim\_{\\mathbb{R}}(\\Lambda^{2})=6
$$

$$
dim\_{\\mathbb{R}}(\\Lambda\_{\\pm}^{2})=3
$$

$$
\\Lambda\_{+}^{2}
$$

$$
\\Lambda\_{-}^{2}
$$

We fix an oriented orthonormal basis _{e1,e2,e3,e4}_ and denote the dual basis
by _{e1,e2,e3,e4}._ Define

$$
{e^{1},e^{2},e^{3},e^{4}}
$$

$$
{e\_{1},e\_{2},e\_{3},e\_{4}}
$$

$$
\\begin{aligned}\\omega\_{1}^{\\pm}&=e^{1}\\wedge e^{2}\\pm e^{3}\\wedge e^{4},\\\omega\_{2}^{\\pm}&=e^{1}\\wedge e^{3}\\pm e^{4}\\wedge e^{2},\\\omega\_{3}^{\\pm}&=e^{1}\\wedge e^{4}\\pm e^{2}\\wedge e^{3}.\\end{aligned}
$$

√1
Note that _∗ω_ i±= _±ω_ i±, and _ω_ i±is an orthonormal basis of Λ2±.
2

$$
\*\\omega\_{i}^{\\pm}=\\pm\\omega\_{i}^{\\pm}
$$

$$
\\frac{1}{\\sqrt{2}}\\omega\_{i}^{\\pm}
$$

$$
\\Lambda\_{\\pm}^{2}
$$

In dimension 4 there is the special coincidence that the curvature operator acts
on 2-forms, and the space of 2-forms decomposes as above. Recall from above that
full curvature tensor decomposes as

(5.11)

$$
R m=W+\\frac{1}{2}E\\oslash g+\\frac{R}{24}g\\oslash g.
$$

Consider the curvature tensor as a mapping on 2-forms defined by
∑

(5.12)

$$
\\widehat{R m}(\\omega)=\\frac{1}{4}\\sum\_{i,j,k,l}R\_{i j k l}\\omega\_{k l}e^{i}\\wedge e^{j},
$$

where

(5.13)

$$
\\omega=\\frac{1}{2}\\sum\_{i,j}\\omega\_{ij}e^i\\wedge e^j.
$$

We call this mapping the _curvature operator,_ which has a corresponding decomposition, see \[ST69\]:
0 1

$$
\\widehat{Rm}=\\left(\\begin{array}{c\|c}\\widehat{W}^{+}+\\frac{R}{12}I&\\widehat{E}\\\hline&\\\widehat{E}&\\widehat{W}^{-}+\\frac{R}{12}I\\&\\\end{array}\\right).
$$

(5.14)

The operators Wc+ and Wc− are traceless as endomorphisms of Λ2+ and Λ2−, respectively.

$$
\\widehat{W}^{+}
$$

$$
\\Lambda\_{+}^{2}
$$

$$
\\widehat{W}^{-}
$$

$$
\\Lambda\_{-}^{2}
$$

Exercise 5.5. Prove the decomposition (5.14). (Hint: this is equivalent to saying
that _Wc_ commutes with _∗_ and _E_ anti-commutes with _∗,_ where _Wc_ and _Eb_ are the
operators on 2-forms corresponding to W and 2E1 7 g, respectively.)

$$
\\widehat{W}
$$

$$
\\widehat{W}
$$

$$
\\mathcal{E}
$$

$$
\\hat{E}
$$

$$
W
$$

$$
\\begin{array}{l}\\frac{1}{2}E\\oslash g\\end{array}
$$

A beautiful theorem relates the _L2_-norms of the tensors _W±_ to the topology
of the manifold, and is called the Hirzebruch Signature Theorem.

$$
L^{2}
$$

$$
W^{\\pm}
$$

* * *

$$
(M^{4},g)
$$

Theorem 5.6 (Hirzebruch \[Hir95\]). _Let_ ( _M_
∫

4,g) be compact and oriented. Then
∫

$$
48\\pi^{2}\\tau(M)=\\int\_{M}\|W\_{g}^{+}\|^{2}d V\_{g}-\\int\_{M}\|W\_{g}^{-}\|^{2}d V\_{g},
$$

where τ = b2+ − b2− is the signature of M.

$$
\\tau=b\_{2}^{+}-b\_{2}^{-}
$$

### 3\. Einstein metrics in dimension four

From Proposition 5.3, it is not hard to see that any Einstein metric is critical for
all three functionals in (5.3). One of the only known obstructions to the existence
of Einstein metrics is the following inequality which is called the Hitchin-Thorpe
Inequality.

Theorem 5.7 (Hitchin-Thorpe). If (M4,g) is Einstein and oriented, then

(5.15)

$$
\\textit{If}\\left(M^{4},g\\right)
$$

$$
2\\chi(M)\\geq3\|\\tau(M)\|,
$$

_with equality if and only if g is flat or finitely covered by a K3 surface with a_ _Ricci-flat metric._

Proof. This inequality follows from the Chern-Gauss-Bonnet Formula and
Hirzebruch Signature Theorem, this was first noted in \[Tho69\], and the equality
case was characterized by Hitchin in \[Hit74\].

We give an outline of the equality case: if equality holds, then one concludes
that R = 0 and that either W + = 0 or W − = 0\. Reversing orientation if necessary,
we may assume that W + = 0\. If g is flat, then we are done, so assume that W −
does not vanish identically. Since _g_ is assumed to be Einstein, then the entire top
half of (5.14) vanishes. This says that the bundle Λ2+(T ∗M) is flat. Since W − 6≡ 0,
the Chern-Gauss-Bonnet theorem implies that _χ(M_) \> 0\. If _b1(M_) (the first Betti
number) were non-zero, then from Hodge Theory, there would exists a non-trivial
harmonic 1-form _α._ But since _Ric ≡_ 0, by the Bochner formula on 1-forms (3.5),
_α_ would be parallel. The dual vector field would be a non-zero vector field on _M,_
contradicting the fact that _χ(M_) \> 0 (from the Poincaŕe-Hopf Index Theorem for
vector fields). So we conclude that _b1(M_) = 0\. By the Cheeger-Gromoll splitting
theorem, we can then conclude that _π1(M_) is finite \[CG72\], so we just consider
the universal cover M˜ of M. Since the bundle Λ2+(T ∗M˜) is flat and M˜ is simplyconnected, it must be trivial, and consequently the holonomy can be reduced to
SU(2), which implies that _g_ is K¨ahler with vanishing first Chern class, and must
therefore be a K3 surface.

$$
W^{+}=0
$$

$$
W^{-}=0
$$

$$
R=0
$$

$$
W^{+}=0
$$

$$
W^{-}
$$

$$
\\Lambda\_{+}^{2}(T^{\*}M)
$$

$$
W^{-}\\not\\equiv0
$$

$$
\\chi(M)>0.\ If\ b\_1(M)
$$

$$
\\alpha
$$

$$
Ric\\equiv0,
$$

$$
\\chi(M)>0
$$

$$
b\_{1}(M)=0
$$

$$
\\pi\_{1}(M)
$$

$$
\\Lambda\_{+}^{2}(T^{\*}\\tilde{M})
$$

$$
\\mathrm{SU}(2)
$$

Exercise 5.8. (i) Show that if k#CP2 admits an Einstein metric then _k ≤_ 3.
(ii) Show that if CP2#kCP2 admits an Einstein metric then _k ≤_ 8.

$$
k#\\mathbb{C}\\mathbb{P}^2
$$

$$
k\\leq3
$$

$$
\\mathbb{C}\\mathbb{P}^2#k\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

$$
k\\leq8
$$

We also mention there are improvements of (5.15) using Seiberg-Witten Theory,
see for example \[LeB99\].

Next, we will list some examples of Einstein metrics in dimension 4. The only
known compact examples with positive Einstein constant in dimension four:

_• S4_ or RP4 with the round metric.

$$
S^{4}
$$

$$
\\mathbb{R}\\mathbb{P}^4
$$

_• S2 × S2_ with the product metric, its orientable Z/2Z quotient G(2,4),
RP2 _×_ RP2 with the product metric, and _S2 ×_ RP2 with the product
metric.

$$
S^{2}\\times S^{2}
$$

$$
\\mathbb{Z}/2\\mathbb{Z}
$$

$$
G(2,4)
$$

$$
\\mathbb{R}\\mathbb{P}^{2}\\times\\mathbb{R}\\mathbb{P}^{2}
$$

$$
S^{2}\\times\\mathbb{R}\\mathbb{P}^{2}
$$

* * *

_•_ CP2 with the Fubini-Study metric.

$$
\\mathbb{C}\\mathbb{P}^2
$$

_•_ CP2#CP2 with the Page metric, an explicit U(2)-invariant Einstein metric, see \[Pag78a\]. This admits a non-orientable quotient CP2#RP4.

$$
\\mathbb{C}\\mathbb{P}^2#\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

$$
\\mathbb{C}\\mathbb{P}^2#\\mathbb{R}\\mathbb{P}^4
$$

$$
\\left\[\\mathrm{Pag78a}\\right\]
$$

_•_ CP2#2CP2 with the Chen-LeBrun-Weber metric \[CLW08\]. This metric
is conformal to an extremal K¨ahler metric. See Section 4 in Lecture 9
below for a more discussion of this metric.

$$
\\mathbb{C}\\mathbb{P}^2#2\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

2
_•_ CP2#kCP , _k_ = _3,...,8,_ admits positive K¨ahler-Einstein metrics (Tian-
Yau \[TY87\], Tian \[Tia90\]).

$$
\\mathbb{C}\\mathbb{P}^2#k\\overline{\\mathbb{C}\\mathbb{P}}^2,k=3,\\ldots,8
$$

It is an interesting problem to find other topological manifolds admitting positive Einstein metrics, and also to possibly find other Einstein metrics on the manifolds listed above. For example, it is unknown whether _S4_ admits an Einstein
metric which is not of constant curvature. However, if one exists, it is known that
its Yamabe energy cannot be too large.

$$
S^{4}
$$

Theorem 5.9 (Gursky \[Gur00\]). _Suppose S4 admits a positive Einstein metric g_
_which is not isometric to the standard round metric, normalized so that Ric(g_) = _3g._ _Then_

$$
S^{4}
$$

$$
Ric(g)=3g
$$

(5.16)

$$
{V o l}(g)<\\frac{8}{9}\\pi^{2}=\\frac{1}{3}{V o l}(g\_{S}).
$$

The only known compact examples with zero Einstein constant in dimension
four:

_•_ K3 surface with Calabi-Yau Ricci-flat metric \[Yau78\], and its quotients.

_•_ Flat metrics.

There are many more examples of Einstein metrics with negative Einstein constant. Of course, any hyperbolic manifold is an example. Complex hyperbolic
manifolds are another interesting class with negative Einstein constant \[LeB95\].
Any K¨ahler manifold with _c1_ < 0 carries an Einstein metric by Aubin-Yau \[Aub78,\
Yau78\]. There are in fact many such manifolds, for example, any non-singular hypersurface in CP3 of degree _d_ \> 4 satisfies _c1_ < 0\. The case _d_ = 4 is the K3 surface
which has _c1_ = 0, and carries the Calabi-Yau Ricci-flat metric mentioned above.
Also, see \[And10\] for a nice survey and other examples.

$$
c\_{1}<0
$$

$$
\\mathbb{C}\\mathbb{P}^3
$$

$$
d>4
$$

$$
c\_{1}<0
$$

$$
c\_{1}=0
$$

$$
d=4
$$

#### 3.1. Higher dimensions

We note that, in dimensions _n_ \> 4, there is no known topological obstruction to the
existence of an Einstein metric. There are in fact quite a large number of known
examples of Einstein metrics in higher dimensions (too many to list here). It could
be the case that every compact manifold of dimension _n_ \> 4 admits an Einstein
metric.

$$
n>4
$$

$$
n>4
$$

### 4\. Optimal metrics

Another interesting class of metrics are called optimal metrics, and are defined to
be those metrics which _globally_ minimize the functional
∫

(5.17)

$$
\\mathcal{R}(g)=\\int\_{M}\|R m\_{g}\|^{2}d V\_{g}.
$$

* * *

Using the formula

(5.18)

$$
\|R m\_{g}\|^{2}=\|W\_{g}\|^{2}+2\|R i c\_{g}\|^{2}-\\frac{1}{3}R\_{g}^{2},
$$

the Chern-Gauss-Bonnet formula (5.4) may be written
∫

(5.19)

$$
\\mathcal{R}(g)=32\\pi^{2}\\chi(M)+4\\int\_{M}\|E\_{g}\|^{2}d V\_{g},
$$

which shows immediately that Einstein metrics are necessarily optimal.

We will not go into much more details about optimal metrics in general, but
just make a few remarks taken from \[LeB04\]:

_•_ There are optimal metrics which are not Einstein.

_•_ There are compact 4-manifolds which do not admit optimal metrics.

_•_ There are topological 4-manifolds which admit an optimal metric for some
smooth structure, but do not admit any optimal metric for a different
smooth structure.

We may also write

(5.20)

$$
\\mathcal{R}(g)=-32\\pi^{2}(\\chi(M)+3\\tau(M))+\\int\_{M}\\left(\\frac{R\_{g}^{2}}{3}+4\|W\_{g}^{+}\|^{2}\\right)d V\_{g}.
$$

Thus we see that another class of optimal metrics are those with W + ≡ 0 and
_R_ = 0, these are called scalar-flat anti-self-dual metrics, which we will discuss in
more detail next.

$$
W^{+}\\equiv0
$$

$$
R=0
$$

Remark 5.10. On a related note, we mention that the functionals _ρ_ and _S_ are
known to be globally minimized in dimension four at a negative K¨ahler-Einstein
metric. This is proved in \[LeB01\] using Seiberg-Witten theory, along with many
other interesting results regarding minimal volumes.

$$
\\mathcal{S}
$$

Exercise 5.11. (i) Prove (5.20) using the Hirzebruch Signature Theorem 5.6.
(ii) Show that
∫ ()

(5.21)

$$
32\\pi^{2}(\\chi(M)-3\\tau(M))=\\int\_{M}\\left(-\|W\_{g}^{+}\|^{2}+\\frac{1}{6}R\_{g}^{2}+3\|W\_{g}^{-}\|^{2}-2\|E\_{g}\|^{2}\\right)d V\_{g}.
$$

If _g_ is K¨ahler then the first two terms cancel (see (6.26) below), and one is left with
∫
()

(5.22)

$$
32\\pi^{2}(\\chi(M)-3\\tau(M))=\\int\_{M}\\left(3\|W\_{g}^{-}\|^{2}-2\|E\_{g}\|^{2}\\right)d V\_{g}
$$

(see \[Der83\]). Show that this implies that gFS is the unique K¨ahler-Einstein metric
on CP2, up to scaling.

$$
\\mathbb{C}\\mathbb{P}^2
$$

### 5\. Anti-self-dual or self-dual metrics

In dimension 4, the curvature condition

W + = 0 is called anti-self-dual (ASD),

$$
W^{+}=0
$$

W − = 0 is called self-dual (SD).

$$
W^{-}=0
$$

Since the Weyl tensor is conformally invariant and the Hodge star operator on
2-forms in dimension 4 is also conformally invariant, it follows that either condition
is conformally invariant.

* * *

Proposition 5.12. If (M4,g0) compact and self-dual, then g0 is a global minimizer
_of the functional W, so is necessarily a critical metric for W._

$$
\\mathit{If}\\left(M^{4},g\_{0}\\right)
$$

$$
g\_{0}
$$

$$
\\mathcal{W},
$$

Proof. For any metric _g_ on _M,_ using the Hirzebruch Signature Theorem, we
have
∫ ∫ ∫

$$
M,
$$

$$
\\begin{align\*}\\mathcal{W}(g)=\\int\_{M}\|W\_g\|^2dV\_g&=\\int\_{M}\|W\_g^+\|^2dV\_g+\\int\_{M}\|W\_g^-\|^2dV\_g\\&=48\\pi^2\\tau(M)+2\\int\_{M}\|W\_g^-\|^2dV\_g\\geq48\\pi^2\\tau(M),\\end{align\*}
$$

with equality if and only if _g_ is self-dual.

The only obvious topological obstruction to existence of a self-dual or anti-selfdual metric comes from the Hirzebruch Signature Theorem.

Proposition 5.13. _If (M,g) is self-dual (anti-self-dual) then τ ≥_ 0 _(τ ≤ 0) with_
_equality if and only if g is locally conformally flat._

$$
\\textit{If}\\left(M,g\\right)
$$

$$
\\tau\\geq0\\quad(\\tau\\leq0)
$$

One can get a stronger restriction if one assumes the scalar curvature is positive:

Proposition 5.14. If (M,g) is self-dual (anti-self-dual) and R > 0, then b2− = 0
(b2+ = 0).

$$
\\textit{If}\\left(M,g\\right)
$$

$$
R>0
$$

$$
b\_{2}^{-}=0
$$

$$
(b\_{2}^{+}=0)
$$

Proof. On 2-forms in dimension 4, the Weitzenb¨ock formula is
∑

(5.23)

$$
(\\Delta\_{H}\\omega^{\\pm}) _{i j}=-(\\Delta\\omega^{\\pm})_{i j}-\\sum\_{l,m}W\_{l m i j}^{\\pm}\\omega\_{l m}^{\\pm}+\\frac{R}{3}\\omega\_{i j}^{\\pm}.
$$

± ±
The result follows by choosing _ω_ be harmonic, pairing (5.23) with _ω,_ and integrating.

$$
\\omega^{\\pm}
$$

$$
\\omega^{\\pm}
$$

* * *

* * *

# Anti-self-dual metrics

### 1\. Deformation theory of anti-self-dual metrics

There are now a wealth of examples of anti-self-dual metrics on 4-manifolds. But
before we get into specific examples, let us consider the deformation theory of
these metrics. Let _(M,g)_ denote an anti-self-dual 4-manifold (the deformation
theory of self-dual metrics is identical upon reversing orientation). The anti-selfdual deformation complex is given by

$$
(M,g)
$$

(6.1)

$$
\\Gamma(T^{ _}M)\\stackrel{\\mathcal{K}{g}}{\\longrightarrow}\\Gamma(S{0}^{2}(T^{_}M))\\stackrel{\\mathcal{D}}{\\longrightarrow}\\Gamma(S\_{0}^{2}(\\Lambda\_{+}^{2})),
$$

where Kg is the conformal Killing operator defined by

$$
\\mathcal{K}\_{g}
$$

(6.2)

$$
(\\mathcal{K} _{g}(\\omega))_{i j}=\\nabla\_{i}\\omega\_{j}+\\nabla\_{j}\\omega\_{i}-\\frac{1}{2}(\\delta\\omega)g\_{i j},
$$

with δω = ∇iωi, S02(T ∗M) denotes traceless symmetric tensors, and D = (W+)′g is
the linearized self-dual Weyl curvature operator. This complex is elliptic \[KK92\].

$$
\\delta\\omega=\\nabla^{i}\\omega\_{i},S\_{0}^{2}(T^{\*}M)
$$

$$
\\mathcal{D}=(\\mathcal{W}^{+})\_{g}^{\\prime}
$$

The cohomology groups of this complex are given as follows:

(6.3)

$$
H\_{c}^{0}(M,g)={\\kappa\\in T^{\*}M\\mid\\mathcal{K}\_{g}\\kappa=0}.
$$

Letting Dg denote (W +

)′g, we have

$$
\\mathcal{D}\_{g}
$$

$$
(W^{+})\_{g}^{\\prime}
$$

(6.4)

$$
H\_{c}^{1}(M,g)={h\\in S\_{0}^{2}(T^{\*}M)\|\\mathcal{D} _{g}h=0,\\delta_{g}h=0}.
$$

Finally,

(6.5)

$$
H\_{c}^{2}(M,g)={Z\\in S\_{0}^{2}(\\Lambda\_{+}^{2})\|\\mathcal{D}\_{g}^{\*}Z=0},
$$

where Dg∗ is the formal

L2-adjoint of Dg.

$$
\\mathcal{D}\_{g}^{\*}
$$

$$
L^{2}.
$$

$$
\\mathcal{D}\_{g}.
$$

If _M_ is a compact manifold then there is a formula for the index depending
only upon topological quantities. The analytical index is given by

$$
\\breve{M}
$$

(6.6)

$$
I n d(M,g)=\\dim(H\_{c}^{0}(M,g))-\\dim(H\_{c}^{1}(M,g))+\\dim(H\_{c}^{2}(M,g)).
$$

The index is given in terms of topology via the Atiyah-Singer index theorem:

Theorem 6.1 (I.M. Singer). _If (M,g) is compact and anti-self-dual, then_

$$
\\textit{If}\\left(M,g\\right)
$$

(6.7)

$$
{I n d}(M,g)=\\frac{1}{2}(15\\chi(M)+29\\tau(M)).
$$

_where χ(M_) _is the Euler characteristic and τ(M_) _is the signature of M_

$$
\\chi(M)
$$

$$
\\tau(M)
$$

This was first computed by I.M. Singer in 1978, see also \[LeB92, page 303\]
and \[KK92\].

The cohomology groups of the complex (6.1) yield information about the local
structure of the moduli space of anti-self-dual conformal classes, which we discuss next (see also \[Ito93, KK92\]). Letting Conf(M,g) denote the conformal automorphism group, we note that Conf(M,g) acts on the space of symmetric tensors, and
therefore, by linearizing at the identity transformation, so does Hc0(M,g), since the
space of conformal Killing Fields is the Lie algebra of Conf(M,g).

$$
H\_{c}^{0}(M,g)
$$

Theorem 6.2. _If (M,g) is anti-self-dual, then there is a map_

$$
\\textit{If}\\left(M,g\\right)
$$

)(6.8)

$$
\\Psi:H\_{c}^{1}(M,g)\\rightarrow H\_{c}^{2}(M,g)
$$

_called the_ Kuranishi map _which is equivariant with respect to the action of the_ _conformal group. The moduli space of anti-self-dual conformal structures near g_ _(anti-self-dual metrics modulo diffeomorphism and conformal equivalence) is locally_
isomorphic Ψ−1(0)/Hc0(M,g).

$$
\\Psi^{-1}(0)/H\_{c}^{0}(M,g)
$$

Proof. The proof is similar to the Einstein case considered above, and we
only give a brief outline here. If g is anti-self-dual, for θ ∈ S02(T ∗M), consider the
map

$$
g
$$

$$
\\theta\\in S\_{0}^{2}(T^{\*}M)
$$

)(6.9)

$$
P\_{g}:\\Gamma(S\_{0}^{2}(T^{ _}M))\\to\\Gamma(S\_{0}^{2}(\\Lambda\_{+}^{2}(T^{_}M)))\\times\\Gamma(T^{\*}M)
$$

defined by

(6.10)

$$
P\_{g}(\\theta)={\\Pi\_{g}(W^{+}(g+\\theta)),\\delta\_{g}\\theta},
$$

where Πg is projection onto S02(Λ2+) with respect to
θ = 0 is given by

_g._ The linearized operator at

$$
\\Pi\_{g}
$$

$$
S\_{0}^{2}(\\Lambda\_{+}^{2})
$$

$$
\\theta=0
$$

(6.11)

$$
P\_{g}^{\\prime}(h)=(\\mathcal{D} _{g}h,\\delta_{g}h).
$$

This is a mixed-order elliptic operator in the sense of Douglis-Nirenberg \[DN55\].
The kernel is isomorphic to Hc1, while the cokernel is isomorphic to H2c ⊕ Hc0.
The gauging result in Theorem 3.6 can be refined to allow conformal deformations,
which then allows one to gauge to be transverse-traceless, see for example \[GV15,\
Theorem 2.11\], or \[FM77\]. The result then follows from the implicit function
theorem in Lemma 4.11.

$$
H\_{c}^{1}
$$

$$
H\_{c}^{2}\\oplus H\_{c}^{0}
$$

In general, it is a difficult problem to compute the Kuranishi map, but we have
the obvious corollary:

Corollary 6.3. _If (M,g) is anti-self-dual and satisfies_ 02

(6.12)

$$
H\_{c}^{0}(M,g)={0}{ ~~a n d~~}H\_{c}^{2}(M,g)={0},
$$

_then the moduli space of anti-self-dual conformal structures near g is a smooth_
finite-dimensional manifold of dimension dim(Hc1(M,g)).

$$
\\left(H\_{c}^{1}(M,g)\\right)
$$

### 2\. Weitzenb¨ock formulas

For _(M,g)_ Einstein, with _Ric_ = _λ · g,_ define the _Lichnerowicz Laplacian_ by

(6.13)

$$
Ric=\\lambda\\cdot g.
$$

$$
\\Delta\_{L}h\_{i j}=\\Delta h\_{i j}+2R\_{i p j q}h^{p q}-2\\lambda\\cdot h\_{i j}.
$$

We next have the following Weitzenb¨ock formulae.

Theorem 6.4 (Kobayashi \[Kob85\], Itoh \[Ito95\]).
_dual Einstein with Ric_ = _λ · g, then_
()
1

_If (M,g) is compact and self_-
)
4

$$
\\textit{If}\\left(M,g\\right)
$$

$$
Ric=\\lambda\\cdot g
$$

(6.14)

$$
\\mathcal{D}^{\*}\\mathcal{D}h=\\frac{1}{2}\\Big(\\Delta\_{L}+2\\lambda\\Big)(\\Delta\_{L}+\\frac{4}{3}\\lambda\\Big)h.
$$

$$
\\mathcal{D}\\mathcal{D}^{\*}Z=\\frac{1}{12}(3\\Delta-8\\lambda)(\\Delta-2\\lambda)Z.
$$

* * *

Proof. One uses the formula for the adjoint operator
1

(6.16)

$$
(\\mathcal{D}^{\*}Z) _{i j}=2(\\nabla^{k}\\nabla^{l}+\\frac{1}{2}R^{k l})Z_{i k j l}.
$$

The computations are lengthy, so are left as an exercise.

Remark 6.5. We note that the gradient of _W_ may also be written as
1

$$
\\mathcal{W}
$$

(6.17)

$$
\\begin{aligned}{\\nabla\\mathcal{W}}&{{}=-8(\\nabla^{k}\\nabla^{l}+\\frac{1}{2}R^{k l})W\_{i k j l}^{+}}\ {}&{{}=-8(\\nabla^{k}\\nabla^{l}+\\frac{1}{2}R^{k l})W\_{i k j l}^{-}.}\ \\end{aligned}
$$

The details are left as an exercise, see \[Ito95\]. It follows that if _g_ is any anti-selfdual metric, then

$$
g
$$

$$
(\\nabla\\mathcal{W})'(h)=-4\\mathcal{D}^\*\\mathcal{D}h.
$$

(6.18)

$$
H\_{c}^{i}(M,g)
$$

Exercise 6.6. Compute Hci(M,g) for the following examples:

• S4 with the round metric gS. This is locally conformally flat, so obviously
anti-self-dual.

$$
S^{4}
$$

$$
g\_{S}
$$

• CP2 with the Fubini-Study metric gFS. This is self-dual with respect to
the complex orientation. To see this, the tensor W − must be in S02(Λ01,1)
(see (6.22) below). The isometry group of gFS contains SU(3), and the
stabilizer of a point contains SU(2). It is not hard to see that SU(2) acts on
Λ01,1 as the standard representation of SO(3) = SU(2)/Z2. Consequently,
the only tensor in S02(Λ01,1) invariant under SU(2) is the zero tensor, so
W − ≡ 0.

$$
\\mathbb{C}\\mathbb{P}^2
$$

$$
g\_{FS}
$$

$$
W^{-}
$$

$$
S\_{0}^{2}(\\Lambda\_{0}^{1,1})
$$

$$
\\mathrm{SU(3)}
$$

$$
\\Lambda\_{0}^{1,1}
$$

$$
\\mathrm{SO(3)=SU(2)/Z\_{2}}
$$

$$
S\_{0}^{2}(\\Lambda\_{0}^{1,1})
$$

$$
W^{-}\\equiv0
$$

_• S1 × S3_ with the product metric _g_ (this is not Einstein, so you cannot
directly use the Weitzenb¨ock formulas. But it is locally conformally flat).
What is the dimension of the moduli space near _g?_

$$
S^{1}\\times S^{3}
$$

$$
g?
$$

We mention the following conjecture.

Conjecture 6.7 (I.M. Singer). _If (M,g) is anti-self-dual and R_ \> _0, then_

$$
R>0
$$

(6.19)

$$
H\_{c}^{2}(M,g)=0.
$$

In the Einstein case, this follows easily from the Weitzenb¨ock formula (6.15).
However, Hitchin proved that the only smooth positive ASD Einstein metrics are
(S4,gS) or (CP2,gFS), see \[Bes08, Theorem 13.30\].

$$
(S^{4},g\_{S})
$$

$$
(\\mathbb{C P}^{2},g\_{\\mathrm{FS}})
$$

A wealth of examples of anti-self-dual metrics have been found since this conjecture was made, and all of the ones with positive scalar curvature have turned out
to have Hc2(M,g) = 0. But despite all of the evidence, a proof of this conjecture
remains elusive.

$$
H\_{c}^{2}(M,g)=0
$$

### 3\. Calabi-Yau metric on K3 surface

The K3 surface is defined to be a nondegenerate quartic surface in CP3, that is

$$
\\mathbb{C}\\mathbb{P}^3
$$

$$
K3={\[z\_{0},z\_{1},z\_{2},z\_{3}\]\\in\\mathbb{C P}^{3}\|z\_{0}^{4}+z\_{1}^{4}+z\_{2}^{4}+z\_{3}^{4}=0}.
$$

The topology of K3 is described by: π1(K3) = {e}, b2 = 22, b2+ = 3, b2− = 19.

$$
\\pi\_{1}(K3)={e},;b\_{2}=22,;b\_{2}^{+}=3,;b\_{2}^{-}=19.
$$

Since _c1(K3_) = 0, by Yau’s solution of the Calabi conjecture \[Yau78\], K3
admits a Ricci-flat K¨ahler metric gY.

$$
c\_{1}(K3);=;0
$$

$$
g\_{Y}
$$

* * *

Proposition 6.8. (K3,gY) is anti-self-dual with respect to the complex orientation.

Proof. To see this we use that fact that for any K¨ahler metric, W + is entirely
determined by the scalar curvature. In fact,

$$
W^{+}
$$

(6.20)

$$
\\widehat{W}^{+}=\\frac{R}{12}(3\\omega\\odot\\omega-I),
$$

where _ω_ is the K¨ahler form. To see this, one proves the following: for a K¨ahler
surface

$$
\\omega
$$

)(6.21)

(6.22)

$$
\\begin{align\*}\\Lambda\_{+}^{2}&=\\mathbb{R}\\cdot\\omega\\oplus(\\Lambda^{2,0}\\oplus\\Lambda^{0,2}),\\\Lambda\_{-}^{2}&=\\Lambda\_{0}^{1,1}.\\end{align\*}
$$

Next, use the fact that if _(M,g,J)_ is K¨ahler, then

(6.23)

$$
\\begin{align\*}Rm(X,Y,Z,W)&=Rm(JX,JY,Z,W)=Rm(X,Y,JZ,JW),\\Ric(X,Y)&=Ric(JX,JY).\\end{align\*}
$$

(6.24)

This implies that the curvature operator

(6.25)

$$
\\widehat{R}\\in S^{2}(\\Lambda^{1,1}).
$$

Choose an ONB so that the K¨ahler form is given by ω1+. Since ω2+ and ω3+ are in
Λ2,0⊕Λ0,2, which is orthogonal to the space of (1,1)-forms, they must be annihilated
by Wc+ \+ 12IR. The formula (6.20) then follows since Wc+ is traceless.

$$
\\omega\_{1}^{+}
$$

$$
\\omega\_{+}^{2}
$$

$$
\\omega\_{+}^{3}
$$

$$
\\Lambda^{2,0}\\oplus\\Lambda^{0,2}
$$

$$
\\widehat{W}^{+}+\\frac{R}{12}I
$$

$$
\\widehat{W}^{+}
$$

Remark 6.9. Note that (6.20) implies that

(6.26)

$$
\|W\_{g}^{+}\|^{2}=\\frac{1}{6}R\_{g}^{2}
$$

for any K¨ahler metric _g._

$$
g.
$$

Exercise 6.10. Using Theorem 6.1 and the Weitzenb¨ock formulas in Theorem 6.4,
show that:

$$
\\bullet\\dim(H\_c^0(K3,g\_Y))=0.
$$

$$
\\bullet\\dim(H\_c^1(K3,g\_Y))=57.
$$

$$
\\bullet\\dim(H\_c^2(K3,g\_Y))=5.
$$

In fact, using the isomorphism
Hc1(K3,gY) has a basis

S02(T ∗M) = Λ2+ ⊗ Λ2−, it can be shown that

$$
S\_{0}^{2}(T^{\*}M)=\\Lambda\_{+}^{2}\\otimes\\Lambda\_{-}^{2}
$$

$$
H\_{c}^{1}(K3,g\_{Y})
$$

$$
{\\omega\_{I}\\otimes\\omega\_{j}^{-},\\omega\_{J}\\otimes\\omega\_{j}^{-},\\omega\_{K}\\otimes\\omega\_{j}^{-}},
$$

where ωI,ωJ,ωK are a basis of the space of self-dual harmonic 2-forms (these are
actually K¨ahler forms for complex structures I,J,K), and {ωj−,j = 1,...,19} is a
basis of the space of anti-self-dual harmonic 2-forms.

$$
\\omega\_{I},\\omega\_{J},\\omega\_{K}
$$

$$
\\bar{I},\\bar{J},\\bar{K})
$$

$$
{\\omega\_{j}^{-},j=1,\\ldots,19}
$$

1
Furthermore, by the Weitzenb¨ock formula, H1c = HE (infinitesimal Einstein
deformations) and the moduli space is exactly 57-dimensional; the Kuranishi map
Ψ _≡_ 0 by the Bogomolov-Tian Theorem 4.17.

$$
H\_{c}^{1}=H\_{E}^{1}
$$

$$
\\Psi\\equiv0
$$

* * *

### 4\. Twistor methods

No discussion of anti-self-dual metrics in dimension four can be complete without
mentioning twistor theory, which was first proposed by Penrose in the Lorentzian
case. This was then studied in depth by Atiyah-Hitchin-Singer in the Riemannian
case \[AHS78\].

Given any oriented Riemannian 4-manifold ( _M,g),_ one may consider the bundle
of unit-norm self-dual 2-forms:

$$
(M,g)
$$

(6.27)

$$
S^{2}\\rightarrow\\mathcal{Z}^{+}(M)\\rightarrow M.
$$

This has a “tautological” almost complex structure defined as follows. At any point
in Z+(M), the horizontal space carries a tautological complex structure, while the
vertical space has the complex structure of S2. With the correct choice of orientation on the fiber, it was shown in \[AHS78\] that this almost complex structure
is integrable if and only if the metric _g_ is anti-self-dual. Thus to any anti-self-dual
four-manifold, one can associate a compact complex 3-fold, and techniques from
complex geometry may be used. We only mention that the cohomology groups
Hci(M,g) ⊗ C are isomorphic to Hi(Z+(M),Θ), the Kuranishi cohomology groups
corresponding to the deformations of complex structure. The Kuranishi map defined above is exactly the Kuranishi map for this complex 3-fold.

$$
\\mathcal{Z}^{+}(M)
$$

$$
S^{2}
$$

$$
H\_{c}^{i}(M,g)\\otimes\\mathbb{C}
$$

$$
H^{i}(\\mathcal{Z}^{+}(M),\\Theta)
$$

In \[Poo86\] and \[Poo92\], Poon found examples of self-dual conformal classes
on the connected sums CP2#CP2 and 3#CP2 using techniques from algebraic geometry. In \[LeB91\], LeBrun gave a more explicit construction of U(1)-invariant
self-dual conformal classes on n#CP2 for any _n,_ and identified the twistor spaces
of these metrics. Joyce constructed a large class of toric ASD metrics on n#CP2
in \[Joy95\], and these were classified by Fujiki \[Fuj00\]. Rollin-Singer constructed
scalar-flat K¨ahler metrics on CP2#10CP2 in \[RS05\]. Honda has constructed many
new examples, see for example \[Hon06, Hon07\]. There are now so many known
examples that we cannot possibly list all of them here.

$$
\\mathbb{C}\\mathbb{P}^2\\dot{#}\\mathbb{C}\\mathbb{P}^2
$$

$$
3#\\mathbb{C}\\mathbb{P}^2
$$

$$
\\mathrm{U}(1)
$$

$$
\\overset{\\frown}{n}#\\mathbb{C}\\mathbb{P}^2
$$

$$
n,
$$

$$
n#\\mathbb{C}\\mathbb{P}^2
$$

$$
\\mathbb{C}\\mathbb{P}^2#10\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

### 5\. Gluing theorems for anti-self-dual metrics

A very successful technique for producing new examples of ASD metrics is given
by the following.

Theorem 6.11 (Donaldson-Friedman, Floer). _If (M1,g1) and (M2.g2) are anti-_
self-dual and Hc2(Mi,gi) = {0} for i = 1,2, then there exist anti-self-dual metrics
_on the connected sum M1#M2._

$$
\\textit{If}\\left(M\_{1},g\_{1}\\right)
$$

$$
(M\_{2}.g\_{2})
$$

$$
H\_{c}^{2}(M\_{i},g\_{i})={0}
$$

$$
i=1,2
$$

$$
M\_{1}#M\_{2}
$$

Donaldson-Friedman proved Theorem 6.11 in the case of smooth manifolds using twistor theory, together with methods from the deformation theory of singular
complex 3-folds \[DF89\]. LeBrun-Singer generalized this proof to the case of orbifolds with Z/2Z-orbifold points \[LS94\]. In \[Flo91\], Floer gave an analytic proof
for the case of the connected sum of _n_ copies of CP2. The strategy of his proof
is to delete points from the summands, and conformally change the metrics to become asymptotically cylindrical. The metrics are then pasted together by very long
cylindrical regions in between. An analysis of the indicial roots of the linearized
problem on the cylinder together with a fixed point theorem as in Lemma 4.11,
then allowed Floer to perturb to an exact solution.

$$
\\mathbb{Z}/2\\mathbb{Z}
$$

$$
\\mathbb{C}\\mathbb{P}^2
$$

There are also many interesting examples of ASD orbifolds, (see for example
\[CS06, LeB04, LV15a, Wri11\] and the references therein), and it is also an interesting problem to glue together orbifold metrics with complementary singularities to produce smooth examples. We mention that Kovalev-Singer presented
a generalization of Floer’s argument which works also in the orbifold case \[KS01\],
but see also \[AV15, RS05, LM08\] for some clarifications.

We end this lecture by mentioning Taubes’ stable existence claim for antiself-dual metrics: for any compact, oriented, smooth 4-manifold _M,_ the manifold
2
_M_ #nCP carries an anti-self-dual metric for some _n,_ see \[Tau92\].

$$
M#n\\overline{\\mathbb{C}}\\overline{\\mathbb{P}}^2
$$

$$
n,
$$

* * *

## Rigidity and stability for quadratic functionals

### 1\. Strict local minimization

We saw that critical points of the Einstein-Hilbert functional in general have a
saddle-point structure. However, critical points for certain quadratic functionals
have a nicer local variational structure. For example, one result we will discuss in
this lecture is the following. Define the functional
∫ ∫

$$
\\mathcal{F} _{\\tau}(g)=\\int_{M}\|R i c\_{g}\|^{2}d V\_{g}+\\tau\\int\_{M}R\_{g}^{2}d V\_{g}.
$$

(7.1)

Theorem 7.1 (Gursky-Viaclovsky \[GV15\]). On S4, the round metric gS is a
strict local minimizer (modulo diffeomorphisms and scaling) for the functional Fτ _provided that_

$$
S^{4}
$$

$$
g\_{S}
$$

$$
\\mathcal{F}\_{\\tau}
$$

(7.2)

$$
-\\frac{1}{3}<\\tau<\\frac{1}{6}.
$$

Many other stability results are given in \[GV15\]; various results are proved for
hyperbolic metrics, complex projective spaces, products of spheres, and Ricci-flat
metrics. But for simplicity, we will only concentrate on the case of the spherical
metric in this lecture.

#### 1.1. The Jacobi operator

Just as in the case of the Einstein-Hilbert functional, the second variation is orthogonal with respect to the splitting

(7.3)

$$
S^{2}(T^{\*}M)={f\\cdot g}\\oplus{\\mathcal{L}(\\alpha)}\\oplus{\\delta h=0,t r\_{g}(h)=0}.
$$

Therefore, if _h_ is any symmetric 2-tensor, then it decomposes as

(7.4)

$$
h=f\\cdot g+\\mathcal{L}\\alpha+z,
$$

where _z_ is TT. Then

(7.5)

$$
\\mathcal{F} _{\\tau}^{\\prime\\prime}(\\bar{h},h)=\\mathcal{F}_{\\tau}^{\\prime\\prime}(\\bar{f}\\cdot g,\\bar{f}\\cdot g)+\\mathcal{F}\_{\\tau}^{\\prime\\prime}(z,z).
$$

Consequently, to check the second variation, we only need to consider conformal
variations and TT variations separately.

As mentioned above, Einstein metrics are indeed critical for Fτ. Let us write
the second variation at an Einstein metric as
∫

$$
\\mathcal{F}\_{\\tau}
$$

$$
\\mathcal{F} _{\\tau}^{\\prime\\prime}(h_{1},h\_{2})=\\int\_{M}\\langle h\_{1},J h\_{2}\\rangle d V\_{g}.
$$

(7.6)

The Jacobi operator _J_ is given explicitly in the following for TT tensors for any
Einstein metric.

* * *

Proposition 7.2 (\[GV15\]).
the Jacobi operator of Fτ

_If g is Einstein with Ric(g_) = _λ · g and h is TT, then_
_is_
()( ())
1

$$
Ric(g)=\\lambda\\cdot g
$$

$$
\\mathcal{F}\_{\\tau}
$$

$$
TT\_{}
$$

(7.7)

$$
J h=\\frac{1}{2}\\Big(\\Delta\_{L}+2\\lambda\\Big)\\Big(\\Delta\_{L}+4\\Big(1+2\\tau\\Big)\\lambda\\Big)h,
$$

_where_

(7.8)

$$
\\Delta\_{L}h\_{i j}=\\Delta h\_{i j}+2R\_{i p j q}h^{p q}-2\\lambda\\cdot h\_{i j}.
$$

The proof of this is a long computation, and will not be presented here.

For conformal variations we have the following.

Proposition 7.3 (\[GV15\]). _If g is Einstein with Ric(g_) = _λ · g and h_ = _fg, then_
4 + 12τ

$$
Ric(g)=\\lambda\\cdot g
$$

(7.9)

$$
h=f g
$$

$$
{t r}\_{g}(J f)=\\frac{4+12\\tau}{2}(3\\Delta+4\\lambda)\\Delta f.
$$

Again, the proof is a long computation, and will not be presented here.

#### 1.2. The case of the round sphere

We will now restrict to the case of (S4,gS). In this case, the Lichnerowicz Laplacian
on TT-tensors is

$$
\\left(S^{4},g\_{S}\\right)
$$

(7.10)

$$
\\Delta\_{L}h=\\Delta h-8h.
$$

Proposition 7.4. _The least eigenvalue of the rough Laplacian on TT-tensors is 8._

Proof. The proof is left as an exercise, with the following hint: use the inequality
∫

(7.11)

$$
\\int\_{S^{4}}\|\\nabla\_{i}h\_{j k}+\\nabla\_{j}h\_{k i}+\\nabla\_{k}h\_{i j}\|^{2}d V\_{g\_{S}}\\geq0.
$$

Consequently, the least eigenvalue of the Lichnerowicz Laplacian on TT-tensors
is 16. Proposition 7.2 then implies that if
1

(7.12)

$$
\\tau<\\frac{1}{6},
$$

then the Jacobi operator is positive definite when restricted to TT-tensors. This
results in the upper bound in (7.2).

Proposition 7.3 implies that the Jacobi operator is non-negative in conformal
directions for
1

$$
-\\frac{1}{3}<\\tau,
$$

(7.13)

with the zero eigenvalues given by _h_ = _f · g,_ where _f_ is a lowest nontrivial eigenfunction of ∆ (by Lichnerowicz’ Theorem). This results in the lower bound in (7.2).

$$
\\mathit{h}=\\mathit{f}\\cdot\\mathit{g},
$$

$$
\\Delta
$$

To summarize, we have shown that on (S4,gS), the second variation is strictly
positive on TT-tensors, and strictly positive in conformal directions (except for
lowest nontrivial eigenfunction directions) in the range
1 1

$$
(S^{4},g\_{S})
$$

(7.14)

$$
-\\frac{1}{3}<\\tau<\\frac{1}{6}.
$$

We next need to integrate this result to make a conclusion about the actual behavior of the functional in a neighborhood of the spherical metric. To this end, using a
modification of the Ebin-Palais slicing, we can ignore Lie derivative directions (as
before), and we can also ignore the conformal zero eigentensors using conformal diffeomorphisms, so the functional is in fact strictly locally minimized at the spherical metric modulo diffeomorphisms. For details, we refer the reader to \[GV15,\
Section 6\].
∫

Notice that for _τ_ = −(1/4), the functional is
minimized for this _τ,_ but our improvement of the range of
an interesting application, which we will discuss next.

\|E\|2, so is obviously strictly
_τ_ for minimization has

$$
\\tau=-(1/4)
$$

$$
\\int\|E\|^{2},
$$

#### 1.3. A reverse Bishop’s inequality

The classical Bishop’s inequality implies that if (M4,g) is a closed manifold with
Ric(g) ≥ Ric(S4,gS) = 3g, then the volume satisfies Vol(g) ≤ Vol(S4,gS), and
equality holds only if (M,g) is isometric to (S4,gS). An interesting consequence of
strict local minimization for _τ_ = 0 is that, locally, a “reverse Bishop’s inequality”
holds.

$$
(M^{4},g)
$$

$$
Ric(g)\\geq Ric(S^4,g\_S)=3g
$$

$$
V o l(g)\\leq V o l(S^{4},g\_{S})
$$

$$
(M,g)
$$

$$
(S^{4},g\_{S})
$$

$$
\\tau=0
$$

Corollary 7.5 (\[GV15\]).
C2,α-norm such that if g˜

On (S4,gS), there exists a neighborhood U of gS in the
_∈ U with_

$$
\\left(S^{4},g\_{S}\\right)
$$

$$
g\_{S}
$$

$$
C^{2,\\alpha}
$$

$$
{}^{\\cdot}\\tilde{g}\\in U
$$

(7.15)

$$
R i c(\\tilde{g})\\leq3\\tilde{g},
$$

_then_

(7.16)

$$
{V o l}(\\tilde{g})\\geq{V o l}(g\_{S}),
$$

with equality if and only if g˜ = φ∗gS for some diffeomorphism φ : M → M.

$$
\\tilde{g}=\\phi^{\*}
$$

$$
\\phi:M\\rightarrow M
$$

There remain some very interesting questions:

_•_ What is the largest neighborhood _U_ for which this holds?
∫

• Is the functional \|Ricg\|2dVg globally minimized at gS?
S4

$$
\\int\_{S^{4}}\|R i c\_{g}\|^{2}d V\_{g}
$$

$$
g\_{S}?
$$

### 2\. Local description of the moduli space

We will next discuss a way to describe local structure of the moduli space of solutions using a procedure analogous to that for the Einstein equations which we
discussed above in Lecture 4. We again consider the functional Fτ, and denote the
Euler-Lagrange equations by

$$
\\mathcal{F}\_{\\tau}
$$

(7.17)

$$
\\nabla\\mathcal{F}\_{\\tau}=0.
$$

Due to diffeomorphism invariance, the linearization of (7.17) is not elliptic, so we
have to make a gauge choice. We will work in transverse-traceless gauge, so define
the operator
1

$$
\\beta\_{g}h=\\delta\_{g}h-\\frac{1}{4}d(t r\_{g}h).
$$

(7.18)

Also, since the functional is scale invariant, we will be interested in the space
{ ∫}
∣

(7.19)

$$
\\overline{{S}} _{0}^{2}(T^{}M)=\\Big{h\\in S^{2}(T^{}M)\\big\|\\int_{M}(t r\_{g}h)d V\_{g}=0\\Big}.
$$

Recall that K denotes the Lie algebra of Killing vector fields.

Theorem 7.6. Assume g is critical for Fτ with τ 6= −1/3. Then the space of
_critical metrics near g modulo diffeomorphism and scaling is locally isomorphic to_
Ψ−1(0)/K, where Ψ is a smooth mapping

$$
\\mathcal{F}\_{\\tau}
$$

$$
\\tau\\neq-1/3
$$

$$
\\Psi^{-1}(0)/\\mathfrak{K},
$$

(7.20)

$$
\\Psi:H\_{\\tau}^{1}\\to H\_{\\tau}^{1},
$$

* * *

_with_

$$
H\_{\\tau}^{1}=\\big{h\\in C^{\\infty}(\\overline{{S}} _{0}^{2}(T^{\*}M))\\big\|(\\nabla\\mathcal{F}_{\\tau}) _{g}^{\\prime}h=0,\\beta_{g}h=0\\big}.
$$

_Consequently, if g is infinitesimally rigid, then g is rigid._

Remark 7.7. For _τ_ = −1/3, the functional is equivalent to the _L2_-norm of the
Weyl tensor, so is conformally invariant. The above result then holds if one restricts
to the space of pointwise traceless tensors, and one considers the moduli space of
conformal classes near _g._ For details, see \[GV15, Section 2.3\].

$$
\\tau=-1/3,
$$

$$
L^{2}.
$$

$$
g.
$$

The first step to prove Theorem 7.6 is to construct a nonlinear mapping whose
zeroes correspond to the moduli space (locally). Assume U⊂ S2(T ∗M) is a neighborhood of the zero section, sufficiently small so that _θ ∈ U0 ⇒ g˜_ = _g_ \+ _θ_ is a
metric. We define the map

$$
\\mathcal{U}\\subset S^{2}(T^{\*}M)
$$

$$
\\theta\\in\\mathcal{U}\_{0}\\Rightarrow\\tilde{g}=g+\\theta
$$

$$
P\_{g}:\\mathcal{U}\\to\\overline{{S}}\_{0}^{2}(T^{\*}M),
$$

(7.21)

by

(7.22)

$$
P\_{g}(\\theta)=\\nabla\\mathcal{F}(g+\\theta)+\\frac{1}{2}\\mathcal{K} _{g+\\theta}\[\\beta_{g}\\mathcal{K} _{g}\\beta_{g}\\theta\].
$$

We have the following analogue of Proposition 4.5.

Proposition 7.8. If τ 6= −1/3, then the linearized operator of Pg at g is elliptic.
Furthermore, if Pg(θ) = 0, and θ ∈ C4,α is sufficiently small for some 0 < α < 1,
∞
then Bt(g + θ) = 0 and θ ∈ C.

$$
\\mathit{If}\\tau\\neq-1/3
$$

$$
P\_{g}
$$

$$
P\_{g}(\\theta)=0
$$

$$
\\theta\\in C^{4,\\alpha}
$$

$$
0<\\alpha<1
$$

$$
B^{t}(g+\\theta)=0
$$

$$
\\theta\\in C^{\\infty}
$$

Proof. The proof involves an integration-by-parts argument. It is crucial that
the equations are variational (since Fτ is the functional), so δ∇Fτ = 0\. This is
equivalent to diffeomorphism invariance of Fτ. The proof is similar to that of
Proposition 4.5.

$$
\\mathcal{F}\_{\\tau}
$$

$$
\\delta\\nabla\\mathcal{F}\_{\\tau}=0
$$

$$
\\mathcal{F}\_{\\tau}
$$

We also have an analogue of Proposition 4.8.

Proposition 7.9. If g1 = g +θ1 is a critical metric in a sufficiently small Ck+1,α-
neighborhood of g (k ≥ 3), then there exists a Ck+2,α-diffeomorphism φ : M→M
_and a constant c such that_

$$
\\mathit{If};g\_{1}=g+\\theta\_{1}
$$

$$
C^{k+1,\\alpha}.
$$

$$
g(k\\geq3)
$$

$$
C^{k+2,\\alpha}-\\textit{diffe}
$$

$$
\\phi:M\\rightarrow M
$$

(7.23)

$$
e^{c}\\phi^{\*}g\_{1}=g+\\tilde{\\theta}
$$

_with_

$$
P\_{g}(\\tilde{\\theta})=0
$$

) = 0(7.24)

_and_

(7.25)

$$
\\int\_{M}t r\_{g}\\tilde{\\theta}d V\_{g}=0.
$$

Proof. The proof is a gauging argument using an infinitesimal Ebin-Palais
gauging as done above in the proof of Theorem 3.6, the details are similar and are
omitted.

We also require a proposition analogous to Proposition 4.10, which shows that
the nonlinear terms are under control.

* * *

Proposition 7.10. _There exists a constant C such that if we write_

(7.26)

$$
P\_{g}(h)=P\_{g}(0)+S\_{g}h+Q\_{g}(h),
$$

then for h1,h2 ∈ C4,α of sufficiently small norm,

$$
h\_{1},h\_{2}\\in C^{4,\\alpha}
$$

(7.27)

$$
\|Q\_{g}(h\_{1})-Q\_{g}(h\_{2})\| _{C^{\\alpha}}\\leq C(\|h_{1}\| _{C^{4,\\alpha}}+\|h_{2}\| _{C^{4,\\alpha}})\\cdot\|h_{1}-h\_{2}\|\_{C^{4,\\alpha}}.
$$

Since the equation is fourth order, the proof is involved, and we refer the reader
to \[GV15, Lemma 2.13\] for the details. We then follow the same procedure as in
Lecture 4 to construct the Kuranishi map, using the implicit function theorem. The
details are left to the reader.

To finish the proof, we note that the gauge term is also carefully chosen so that
solutions of the linearized equation must be in the transverse-traceless gauge. That
is, if (Pg)′h = 0 then we have separately,

$$
(P\_g)'h=0
$$

(7.28)

$$
(\\nabla\\mathcal{F}\_{t})^{\\prime}(h)=0\\mathrm{and}\\delta\\overset{\\circ}{h}=0,
$$

which is an analogue of Proposition 4.12.

### 3\. Some rigidity results

For h transverse-traceless, recall from above that the linearized operator of ∇Fτ at
an Einstein metric is given by
()( ())

$$
\\nabla F\_{\\tau}
$$

(7.29)

$$
(\\nabla F\_{\\tau})^{\\prime}h=\\frac{1}{2}\\Big(\\Delta\_{L}+\\frac{1}{2}R\\Big)\\Big(\\Delta\_{L}+\\Big(1+2\\tau\\Big)R\\Big)h.
$$

_•_ This formula was previously obtained for the linearized Bach tensor, which
is the case of _τ_ = _−1/3_ by O. Kobayashi \[Kob85\].

$$
\\tau=-1/3
$$

_•_ Recall that infinitesimal Einstein deformations are given by TT kernel of
the operator ∆L \+ 2R1, which we studied in Lecture 4. These deformations
are still present, but note there is now the possibility of non-Einstein
deformations.

$$
\\Delta\_{L}+\\frac{1}{2}R
$$

Also, recall that for _h_ = _fg,_ we have

$$
h=f g
$$

(7.30)

$$
t r\_{g}((\\nabla F\_{\\tau})^{\\prime}h)=2(1+3\\tau)(3\\Delta+R)(\\Delta f).
$$

The rigidity question is then reduced to a separate analysis of the eigenvalues of
∆L on transverse-traceless tensors, and of ∆ on functions. Such an analysis of the
eigenvalues of these operators yields the following rigidity theorems. Let H1τ denote
the space of transverse-traceless kernel of the linearized operator. In the case of the
Fubini-Study metric, we have

$$
\\Delta\_{L}
$$

$$
\\Delta
$$

$$
H\_{\\tau}^{1}
$$

Theorem 7.11 (\[GV15\]).

On (CP2,gFS

), H1τ = {0} provided that τ < 1/6.

$$
\\tau<1/6
$$

In the case of the product metric, we have

Theorem 7.12 (\[GV15\]).
_and τ_ 6= _−1/2. If τ_ = _−1_
_element g1 − g2._

On (S2 × S2
/2, then H1τ

,gS2×S2), H1τ = {0} provided that τ < 0
_is one-dimensional and spanned by the_

$$
(S^{2}\\times S^{2},g\_{S^{2}\\times S^{2}}),H\_{\\tau}^{1}={0}
$$

$$
\\tau<0
$$

$$
\\tau\\ne-1/2.\ \\mathrm{If}\\tau=-1/2
$$

$$
H\_{\\tau}^{1}
$$

$$
g\_{1}-g\_{2}
$$

In particular, in the case _τ_ = −1/2, this gives an example of a deformation of
critical metrics for this functional which is not an Einstein deformation.

$$
\\tau=-1/2
$$

Many other rigidity results are presented in \[GV15\], which we will not go into
detail here. We have stated the above two results because these rigidity results will
play a crucial rˆole in the gluing construction which will be discussed in Lecture 9.

* * *

### 4\. Other dimensions
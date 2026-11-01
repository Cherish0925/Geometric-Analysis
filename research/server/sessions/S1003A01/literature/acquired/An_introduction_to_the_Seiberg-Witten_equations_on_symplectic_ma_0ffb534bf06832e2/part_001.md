---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: An introduction to the Seiberg-Witten equations on symplectic manifolds]

# An introduction to the Seiberg-Witten equations on symplectic manifolds

> Source: https://math.berkeley.edu/~hutching/pub/tn.pdf
> Fetched: 2026-10-09 12:08
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
  "source": "tavily",
  "source_url": "https://math.berkeley.edu/~hutching/pub/tn.pdf",
  "metadata": {
    "provenance_urls": [
      "https://math.berkeley.edu/~hutching/pub/tn.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "Taubes Seiberg-Witten canonical class J-holomorphic curves arbitrary compatible almost complex structure closed symplectic 4-manifold"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

For example if E, F are vector bundles over X, then we can deﬁne Hom(E, F) to be the set of (x, h) such that x ∈X and h : Ex →Fx commutes with the C action. Digression: Recall that if E is a line bundle on X, the ﬁrst Chern class c1(E) ∈H2(X; Z) is (at least if X is a closed oriented manifold) the Poincar´ e dual of the zero set of a generic section of E. Explicitly, if X is Euclidean space, with ˆ F the trivial SpinC(4) bundle, S+ the trivial C2 bundle, and L the trivial line bundle, then the connection A is an imaginary-valued 1-form Ajdxj (imaginary-valued, not C-valued, because the connection is compatible with the metric), and ∇A = dxj ⊗(∂j + 1 2Aj) acting on C2-valued functions. (2.8) 16 2.8 The Seiberg-Witten equations Let X be a smooth oriented Riemannian 4-manifold with a SpinC structure. (4.22) 5 The symplectic case, part II We will now discuss the Seiberg-Witten invariant on a symplectic manifold X (with b2 + > 1) for the remaining SpinC structures, and explain that it is equal to a certain count of pseudoholomorphic curves in X. 33 An element e ∈H2(X; Z) corresponds to a SpinC structure with S+ = E ⊕K−1E where c1(E) = e, and K is the canonical bundle coming from an ω-compatible almost complex structure J. Given a sequence rn →∞ and (an, (αn, βn)) satisfying the equations (5.1) for r = rn, then after taking an appropriate subsequence, there is a compact, complex curve C and a J-holomorphic map f : C →X such that: • f∗[C] is the Poincar´ e dual of e in H2(X; Z). For

## Retrieved source content

# An introduction to the Seiberg-Witten

∗

# equations on symplectic manifolds

†

### Michael Hutchings and Clifford Henry Taubes Summer 1997

The Seiberg-Witten equations are defined on any smooth 4-manifold. By appropriately counting the solutions to the equations, one obtains smooth 4-manifold invariants. On a symplectic 4-manifold, these invariants have a symplectic interpretation, as a count of pseudoholomorphic curves. This al- lows us to transfer information between the smooth and symplectic categories in four dimensions. In the following lectures, we will try to explain this story. In the first two lectures, we review some background from differential geometry, which will allow us to write down the Seiberg-Witten equations at the end of the second lecture. In the third lecture we define the Seiberg-Witten invariants and discuss their most basic properties. In the fourth lecture we compute the simplest of the Seiberg-Witten invariants on a symplectic 4-manifold. In the fifth lecture we relate the remaining Seiberg-Witten invariants in the symplectic case to pseudoholomorphic curves.

## Contents

1 Background from differential geometry 3

1.1 Vector bundles. .. . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Connections. .. .. . . . . . . . . . . . . . . . . . . . . . . . 5
1.3 Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 ∗ Based on the lectures of the second author at the 1997 Park City-IAS Summer Institute. † Both authors are supported in part by grants from the National Science Foundation.

---

1.4 Curvature............................. 8
1.5 Self-dual two-forms........................ 9
2 Spin and the Seiberg-Witten equations 9
2.1 Principal bundles and associated bundles............ 9
C
2.2 Spin structures . ......................... 11
2.3 Some group theory........................ 12
2.4 The spinor bundles........................ 14
2.5 Clifford multiplication...................... 14
2.6 The spin connection....................... 15
2.7 The Dirac operator........................ 16
2.8 The Seiberg-Witten equations.................. 17
3 The Seiberg-Witten invariants 18
3.1 Gauge transformations...................... 18
3.2 Basic properties of the moduli space.............. 19
3.3 Why the conditions on b2+?.................... 21
3.4 Outline of the proof of compactness . . . . . .......... 21
3.5 The Seiberg-Witten invariant.................. 23
3.6 Examples and applications . . . . . . . . . . .......... 25
4 The symplectic case, part I 25
4.1 Statement of the theorem.................... 26
C
4.2 The canonical Spin structure.................. 26
4.3 Step 1: Understanding the Dirac equation........... 28
4.4 Step 2: deforming the curvature equation . . . . . . . . . . . . 30
4.5 Step 3: uniqueness of the solution................ 30
4.6 Appendix: an estimate on beta................. 33
5 The symplectic case, part II 33
5.1 Summary of the last lecture................... 33
5.2 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
5.3 Seiberg-Witten and pseudoholomorphic curves......... 35
5.4 Definition of the Gromov invariant............... 36

---

1 Background from differential geometry

The data for the Seiberg-Witten equations are a connection A on a certain
line bundle, and a section ψ of a certain C2 bundle. In this lecture we will
review bundles and connections. We assume familiarity with the tangent
bundle and differential forms. (The material in this lecture can be found in
almost any modern book on differential geometry; see e.g. [10].)

\psi

\mathbb{C}^{2}

1.1 Vector bundles

Let X be a smooth manifold. (In this lecture all spaces will be smooth
manifolds.) A vector bundle on X is essentially a family of vector spaces
parametrized by X. More precisely:

Definition 1.1 Let n ∈{1, 2,...}. A (complex) vector bundle on X of
rank n is a space E with an action C × E → E of C and a surjective map
π : E → X such that:

n\,\in\,1,2,\ldots\,

\mathbb{C}\times E\to E

\pi:E\to X

\pi

• π commutes with the C action,

∗
• C acts freely,

\mathbb{C}^{*}

• E is locally isomorphic to a product, i.e. for each x ∈ X, there is a
−1
neighborhood U ⊂ X of x and a diffeomorphism ξ : E|U= π (U) →
n
U × C, such that the diagram

x\in X

U\subset X

\xi:E|_{U}=\pi^{-1}(U)\to

U\times\mathbb{C}^{n}

commutes, and such that ξ intertwines the C action with the standard
n
C action on C. (ξ is called a local trivialization.)

If n = 1, we call E a line bundle. One similarly defines a real vector bundle
by replacing C above with R. A section of E is a smooth choice of a vector
in each fiber, i.e. a smooth map s : X → E such that πs = identity. We
∞
denote the space of sections of E by C (E).

\xi

\mathbb{C}^{n}

n=1

\pi s=\mathrm{i d e n t i t y}

s\,X\to\,E

C^{\infty}(E)

---

It is a consequence of the definition that the fiber Exof E at any x ∈ X
−1 n
(that is, π (x)) has, in a natural way, a vector space structure of C. This
is why E is called a vector bundle.
In particular, it follows from the definition that the space of sections

E_{x}

x\in X

\pi^{-1}(x)]

\mathbb{C}^{n}

In particular, it follows from the definition that the space of sections
of E forms a vector space, where (s1 + s2)(x) = s1(x) + s2(x), and where
λ · s1(x) = mλ(s1(x)) for λ ∈ C. (We sometimes use mλto denote the action
of λ on E.) In this regard, note that there is a canonical section, the “zero
section: 0 : X → E which is a bijection onto the image of multiplication by
0 on E. Note that if s is a section and f : X → C a smooth function, then
f · s is a section.
One can make new vector bundles out of old ones by analogy with the

(s_{1}+s_{2})(x)=s_{1}(x)+s_{2}(x)

\lambda\cdot\!s_{1}(x)=m_{\lambda}\big(s_{1}(x)\big)

\lambda\in\mathbb{C}

m_{\lambda}

0:X\to E

f:X\to\mathbb{C}

One can make new vector bundles out of old ones by analogy with the
standard operations on vector spaces. For example if E,F are vector bundles
over X, then we can define Hom(E,F) to be the set of (x,h) such that x ∈ X
∗
and h : Ex→ Fxcommutes with the C action. Likewise, the dual bundle E
consisting of (x,h) such that h : Ex→ C and h commutes with the C action.
∗
We also have the tensor product E ⊗ F = Hom(E,F).
A fundamental example of a (real) vector bundle is the cotangent bundle

\mathfrak x\in X

h:E_{x}\rightarrow F_{x}

E^{*}

(x,h)

h:E_{x}\to C

E\otimes F=\operatorname{H o m}(E,F^{*})

A fundamental example of a (real) vector bundle is the cotangent bundle
∗ k ∞ k ∗
T X → X. We let Ω (X) = C (∧ T X) denote the space of differential
forms on X. If E is another vector bundle on X, we can consider “E-valued
k ∞ k ∗
differential forms”, namely Ω (X,E) = C (∧ T X ⊗ E).
One more basic construction is the following.

T^{*}X\,\rightarrow\,X

\Omega^{k}(X)=C^{\infty}(\Lambda^{k}T^{*}X)

X

\Omega^{k}(X,E)=\mathcal{C}^{\infty}\big(\Lambda^{k}T^{*}X\otimes E\big)

One more basic construction is the following.

Definition 1.2 If π : E → X is a vector bundle and f : Y → X is a map,
∗
the pullback bundle f E → Y is the fiber product of π and f,

{\operatorname{I f}}\pi:E\to X

f^{*}E\to Y

\begin{aligned}{}&{{}f^{*}E\xrightarrow{\quad\mathrm{}{f}\quad}}{{mathrm}~{~E~}}\\ {}&{{}\left\begin\}{matrix{}}{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}{}{}&&{{{}}}\\ {{{}}{{}}}&{Y{}}&&{{}}X,}\end{matrix}\right]}\\ {}&{{}}&{}\\ {}&{{}Y\quad\xrightarrow{\quad\mathrm{}{}}{{}}}&{{}X X,}\\ \end{aligned}

∗ ∗
i.e. f E = {(y,e) | y ∈ Y, e ∈ Ef (y)}, and the projection f E → Y sends
(y,e) 7→ y.
∗
There is a natural map f˜ : f E → E defined by

\begin{array}{l}{\mathrm{i.e.}}\ \ f^{*}E=\{(y,e)\ |\ y\,in Y,\ e\,\,\ E_{f(y)}\},}\\ {(y,e)\mapsto y.}\end{array}

∗
For each y ∈ Y, f˜ restricts to an isomorphism (f E)y→ Ef (y).

{\tilde{f}}(y,e)=e.

{\tilde{f}}:f^{*}E\to E

∗
There is a natural map f˜ : f E → E defined by

y\in Y,\tilde{f}

(f^{*}E)_{y}\to E_{f(y)}

---

1.2 Connections

In general, there is no canonical isomorphism of a fiber of a vector bundle
n
with C. Let us explore what this means at the infinitesimal level, i.e. at the
level of tangent bundles. If π : E → X is a vector bundle, there is an exact
sequence of (real) vector bundles on the space E,

\mathbb{C}^{n}

\pi:E\to X

0\ \underset\}{\longrightarrow\ \pi^{*}E\ \ \ {scriptstyle};{{scriptstylescriptstyle\ \\ \imath\ \ \ \ }}\ T E\ \xrightarrow{\ \pi_{*}\ \ }\pi^{*}T X\ \xrightarrow{\;}\ 0..

(1.1)

∗
In this sequence, π E is the bundle whose fiber over e ∈ E is the vector space
∗
in which e lives, namely Eπ(e). There is a natural map ı from π E to the
tangent bundle TE, whose image consists of the “vertical” tangent vectors
∣
d∣
in E. (The map ı sends v ∈ E to the tangent vector (e + tv).) And π∗
dt t=0
is the derivative of π.
This sequence does not have a canonical splitting. In other words, there

\pi^{*}E\ {}

e\in E

E_{\pi(e)}

\pi^{*}E\ {}

v\in E

\frac{d}{d t}\Big|_{t=0}\ e+e v\ ..

\pi

\pi_{*}

This sequence does not have a canonical splitting. In other words, there
is no canonical way to choose a “horizontal” subspace of TE complementary
∗
to the vertical subspace π E. However we can choose a splitting; and if
the splitting satisfies certain compatiblity conditions, we call the splitting a
connection. (Such a splitting “connects” the fibers over nearby points of X.)
We impose the compatibility condition as follows.

\pi^{*}E\,

∗
Definition 1.3 A connection on E is a map A : TE → π E, i.e. a 1-form
∗
on E with values in π E, such that:

\mathbf{A}:T E\to\pi^{*}E

E

∗ ∗
• A is a splitting of the exact sequence (1.1), i.e. A ◦ ı = 1 : π E → π E.

\ {mathfrak A\circ}\iota=1:\pi^{*}E\to\pi^{*}E

• A commutes with multiplication by scalars, i.e. if λ ∈ C and mλ: E →
∗
E is multiplication by λ, then m A = λ · A.
λ

\lambda\in\mathbb{C}\,{\mathrm{a n d}}\,m_{\lambda}:E\to

\lambda\in\mathbb{C}\,{\mathrm{a n d}}\,m_{\lambda}:E\to

\lambda

m_{\lambda}^{*}\mathbf{A}=\lambda\cdot\mathbf{A}

(1.2)

It is sometimes useful to write a connection in terms of a local trivializan n
tion ξ : E|U→ U × C. Let ξ1,...,ξ be the n corresponding C-valued funcn
tions on E|U, i.e. ξ(e) = (π(e), (ξ1(e),...,ξ (e))). The connection 1-form A
n a n
now takes values in C; let A be the coordinates, i.e. A = (A1,..., A).
Then we can write
a a ab b
A = dξ + A ξ. (1.2)

\xi^{1},\ldots,\xi^{n}

ab n
Here A is a 1-form pulled back from U; we can think of A as an End(C)-
valued 1-form on U. (In (1.2) and elsewhere, repeated indices are summed.)

\mathbf{A}^{a}=d\xi^{a}+A^{a b}\xi^{b}.

E|_{U}

\ \mathrm{A}^{a}

U;

E\vert_{U}

\mathbf{A}=(\mathbf{A}^{1},\ldots,\mathbf{A}^{n})

{\mathfrak{G}}{\big(}e{\big)}=\big(\pi\big(e e\big),\big(\xi^{1}\big(e\big),\ldots,\xi^{n}\big(e\big)\big)\big)

A^{a b}

U

U,

---

Exercise 1.5 Show that the space of all connections on E is an affine space
′
over Ω1(X, End(E)). In other words, if A is a connection, then a 1-form A ∈
∗
Ω1(E,π E) is also a connection if and only if there exists α ∈ Ω1(X, End(E))
′ ∗
such that (A − A)e= (π α)(e).

\Omega^{1}(X,\ \mathrm{E n d}(E))

\mathbf{A}^{\prime}\in

\Omega^{1}(E,\pi^{*}E)

\alpha\in\Omega^{1}(X,\ \mathrm{E n d}(E))

(\mathbf{A}^{\prime}-\mathbf{A})_{e}=(\pi^{*}\alpha)(e)

A connection gives us a way to differentiate sections of E.

Definition 1.6 Given a connection A, we define the covariant derivative

\nabla_{\mathbf{A}}:C^{\infty}(E)\to C^{\infty}(T^{*}X\otimes E)

∞
as follows. If ψ ∈ C (E), then ∇Aψ : TxX → Exis the composition

\psi\in C^{\infty}(E)

\nabla_{\mathrm{A}}\psi:T_{x}X\to E_{x}

T_{x}X\xrightarrow{\ \\\psi_{*}\ \ }T_{\psi(x)}E\xrightarrow{\ \ \ \ A\ \ }\left(\pi^{*}E\right)_{\psi(x)}\xrightarrow{\ \ \ \tilde{\pi}\ \ \ }E_{x}.

Here is another way to understand this definition. The “horizontal” sub-
∗
space of TE is Ker(A). There is a map H : (π TX)e→ TeE which sends
a tangent vector v ∈ TX to its horizontal lift at e, namely the unique
horizontal vector h ∈ TeE such that π∗h = v. Given a section ψ : X → E
and v ∈ TxX, we can compare the derivative of ψ along v, namely ψ∗v, with
the horizontal lift of v, namely Hv. The difference ψ∗v − Hv is a vertical
∗
vector in π E, and this is the covariant derivative, i.e.

\operatorname{K e r}(\mathbf{A})

H:(\pi^{*}T X)_{e}\rightarrow T_{e}E\ ,

v\in T X

{,}

h\in T_{e}E

\psi:X\to\,E

\pi_{*}h=v

v\in T_{x}X

\psi

v

H v

\psi_{*}v\ H\,v\ H v

\pi^{*}E\

\nabla_{\mathbf{A}}\psi(v)=\tilde{\pi}\big(\psi_{*}v-H v\big).

So the covariant derivative measures the deviation of a section from the
horizontal subspace.

Exercise 1.7 1. Check that the map ∇Aψ : TX → E is linear.

\nabla_{\mathbf{A}}\psi

3. Prove the Leibniz rule ∇A(fψ) = df ⊗ ψ + f ∇Aψ.

\nabla_{\mathbf{A}}\big(\psi_{1}+\psi_{2}\big)=\nabla_{\mathbf{A}}\big(\psi_{1}\big)+\nabla_{\mathbf{A}}\big(\psi_{2}\big).

ab
If A is the matrix for A in a local trivialization as in (1.2), and if ψ is
n
a section over U, which we think of as a C-valued function on U, then

\psi

A^{a b}

\mathbb{C}^{n}

(\nabla_{\bf{A}}\psi)^{a}=d\psi^{a}+A^{a b}\psi^{b}

U,

---

1.3 Metrics

We will need to consider vector bundles with a bit more structure on them.

Definition 1.8 Let E → X be a complex vector bundle. A metric on E is
a map g : E ⊗ E → C such that, if 〈v,w〉 denotes g(v,w), then:

E\to X

g:E\otimes E\to\mathbb{C}

\langle v,w\rangle

g(v,w)

• g is antilinear in the first variable and linear in the second variable, i.e.
〈λv,w〉 = λ〈v,w〉 and 〈v,λw〉 = λ〈v,w〉.

\langle\lambda v,w\rangle=\overline{{\lambda}}\langle v,w\rangle

\langle v,\lambda w\rangle=\lambda\langle v,w\rangle.

\left\langle w,v\right\rangle={\overline{{\left\langle v,w\right\rangle}}}.

• g is positive definite, i.e. 〈v,v〉 > 0 for all v 6= 0.

\langle v,v\rangle>0

v\neq0.

If E is a real vector bundle, a metric on E is defined the same way, but
without the complex conjugation.

Definition 1.9 If E is a vector bundle with a metric g, a connection A on
E is compatible with the metric g if for any two sections ψ,η of E, we have
an equality of 1-forms

\psi,\eta

d\langle\psi,\eta\rangle=\langle\nabla_{\mathbf{A}}\psi,\eta\rangle+\langle\psi,\nabla_{\mathbf{A}}\eta\rangle.

Exercise 1.10 Let E be a complex (resp. real) vector bundle with a metric.
Choose a local trivialization sending the metric on E to the standard metric
n n
on C (resp. R). Show that A is compatible with the metric if and only
if the matrix-valued 1-form A from equation (1.2) takes values in the Lie
algebra Lie(U(n)) (resp. Lie(SO(n))).

:(\mathrm{S O}(n)))

A Riemannian metric on X is a metric g on the cotangent bundle
∗ ∗
E = T X. Given g, there is a unique connection Γ on T X such that:

E=T^{*}X

T^{*}X

• Γ is compatible with g,

• Γ is torsion-free, i.e. the composition

\Omega^{1}(X)\:\xrightarrow{\;\;\nabla_{\Gamma}\;}\:C^{\infty}(X,T^{*}X\otimes T^{*}X)\:\xrightarrow{\;{\mathrm{a n t i s s y m.}}\;}\Omega^{2}(X)

We can compute with Γ as follows. At any point p ∈ X, one can choose
n j k 2
local coordinates x1,...,x centered at p such that 〈dx,dx 〉 = δjk+O(|x|).
j
Then ∇Γ(dx) = 0 at p.

p\in X

x^{1},\ldots,x^{n}

E=T^{*}X.)

This Γ is called the Levi-Civita connection.
We can compute with Γ as follows. At any point p ∈ X, one can choose

\nabla_{\Gamma}(d x^{j})=0

\bigl d x^{j},d x^{k}\bigr\rangle=\delta_{j k}\!+\!O\bigl(|x|^{2}\bigr)

---

1.4 Curvature

The curvature of a connection is a measure of the nonintegrability of the
horizontal distribution in E; in other words it is an obstruction to finding
nontrivial local sections of E with covariant derivative zero.

Definition 1.11 If A is a connection on E, the curvature

F_{\mathrm{A}}\in\Omega^{2}(X,\operatorname{E n d}(E))

is defined as follows. If v,w are two vectors in TxX, extend them to local
vector fields. Let Hv,Hw be the horizontal lifts in TE. If e ∈ E, then

T_{x}X

e\in E

F_{\mathbf{A}}(v,w)(e)=\tilde{\pi}(-\mathbf{A}_{e}([H v,H w])).

In local coordinates,

F_{\mathbf{A}}^{a b}=d A^{a b}+A^{a c}\wedge A^{c b}.

(1.3)

Exercise 1.12 Check that the definition of curvature makes sense, i.e. FA
is an honest tensor which does not depend on the choice of extension to local
vector fields, and prove equation (1.3).

F_{\mathbf{A}}

We will need the following facts for the computations in the third and
fourth lectures.

n
Exercise 1.13 Choose local coordinates x1,...,x on X. Let ∇idenote the
i i j
dx component of ∇A. Show that the dx ∧ dx component of FAequals the
commutator [∇i, ∇j].

x^{1},\ldots,x^{n}

\nabla_{i}

d x^{i}

\nabla_{A}

d x^{i}\wedge d x^{j}

F_{A}

[\nabla_{i},\nabla_{j}]

Exercise 1.14 1. Show that one can extend the covariant derivative to
a map
k k+1
∇ : Ω (X,E) → Ω (X,E)

\alpha\in\Omega^{k}(X)

2 ∞
2. Show that FA= ∇ : C (E) → Ω2(X,E).
A

\nabla_{A}:\Omega^{k}(X,E)\to\Omega^{k+1}(X,E)

F_{A}=\nabla_{A}^{2}:C^{\infty}(E)\to\Omega^{2}(X,E).

---

## 1.5 Self-dual two-forms

In the four-dimensional world, there are two special vector bundles which we will need. If X is a smooth 4-manifold with an orientation and a Riemannian metric, the 2-forms have a decomposition into two R3-bundles

Λ2T ∗ X = Λ2−⊕ Λ2+

constructed as follows. There is a map ∗ : Λ2 → Λ2 defined by

ω ∧∗η = g(ω,η) vol,

where g is the induced metric on Λ2 and vol ∈ Ω4(X) is the volume form, defined as follows: if e1,...,e4 is an oriented orthonormal basis for T ∗ X at a point x ∈ X, then vol(x) = e1 ∧ e2 ∧ e3 ∧ e4. We have ∗ 2 = 1, and we define Λ2±to be the ±1 eigenspace. Explicitly, if e1,...,e4 is a basis as above, then Λ2±is spanned by e1 ∧ e2 ± e3 ∧ e4, e1 ∧ e3 ∓ e2 ∧ e4, and e1 ∧ e4 ± e2 ∧ e3. Sections of Λ2+(resp. Λ2−) are called self-dual (resp. anti-self-dual) 2-forms. Note that switching the orientation on X interchanges Λ2+and Λ2−, while deforming the metric moves Λ2±continuously inside Λ2.

# 2 Spin and the Seiberg-Witten equations

As we said at the beginning of the last lecture, the data for the Seiberg- Witten equations are a connection on a certain line bundle and a section of a certain C2 bundle. Having explained connections in the last lecture, we now need to specify the line bundle and the C2 bundle. At the end of the lecture we will finally be able to write down the Seiberg-Witten equations.

## 2.1 Principal bundles and associated bundles

We will use the following general procedure for constructing interesting vector bundles.

Definition 2.1 Let X be a smooth manifold and G a Lie group. A prin- cipal G bundle on X is a manifold P, a surjective map π : P → X, and a (right) G action on P such that:

---

- The G action respects π, i.e. the diagram
// P × G P GG GG GGπ GG G## X

commutes.

- The G action is free and transitive on each fiber.
- Over open balls U ⊂ X there exist G-equivariant, fiber-preserving dif- feomorphisms
P |U’ U × G.

The canonical example is the frame bundle Fr of a smooth manifold X. If X is n-dimensional, oriented, and has a Riemannian metric, then Fr is a principal SO(n) bundle on X. The fiber over x ∈ X consists of all linear n n maps R → TxX sending the standard metric and orientation on R to the metric and orientation on TxX. The group SO(n) acts by composition on the right. Out of a principal bundle we can construct many vector bundles as follows. Let V be a vector space and ρ : G → Aut(V) a representation of G. We define the associated vector bundle

VP=(P × V)/ ∼, (pg,v) ∼ (p,ρ(g)v).

Exercise 2.2 1. VPis a vector bundle whose fibers are isomorphic to V.

n

2. If V = R is the fundamental representation of SO(n), then VFr= TX.
3. A G-invariant metric on V gives rise to a metric on VP.
4. The associated bundle construction commutes with linear algebra, i.e. (V ⊗ W)P= VP⊗ WP, etc. The material in this section can also be found in almost any modern
differential geometry book.

---

C

# 2.2 Spin structures

From the above exercise we see that starting with the frame bundle and taking the vector bundles associated to the exterior powers of the dual fun- damental representation of SO(n), we obtain the bundles of differential forms. Now for n ≥ 3, π1 SO(n) = Z2, and we denote the connected double cover of SO(n) by Spin(n). It turns out that there are representations of Spin(n) which do not descend to SO(n). So, if we could somehow “lift” Fr to a prin- cipal Spin(n) bundle, we would get more associated vector bundles. This motivates the following definition:

Definition 2.3 A spin structure on an oriented Riemannian manifold X is a principal Spin(n)-bundle Fˆ on X together with a map Fˆ → Fr such that the following diagram commutes:

Fˆ × Spin(n) // Fˆ

## Fr × SO(n)//Fr

X

Not every 4-manifold has a spin structure. For example S4 and S2 × S2 have spin structures, but there does not exist any spin structure on CP2. However a certain weak version of a spin structure exists more often. Define C Spin (n) = (Spin(n) × U(1))/Z2.

(Here Z2 acts on the first factor by the covering transformation of π : Spin(n) → SO(n) and on the second factor by multiplication by −1.) There C is a well defined map Spin (n) → SO(n) sending (x,λ) 7→ π(x).

C C Definition 2.4 A Spin structure is like a spin structure, but using Spin (n) C C instead of Spin(n). That is, a Spin structure is a principal Spin bundle, Fˆ, whose projection π to X factors through Fr to give, fiberwise, the standard group homomorphism. C Note that although the definition of spin (resp. Spin) structure uses a Riemannian metric, in fact for any two metrics there is a canonical identifi- C cation between the spin (resp. Spin) structures for one metric and the spin C (resp. Spin) structures for the other metric.

---

C
Theorem 2.5 On any oriented 4-manifold X, Spin structures exist, and
C 2
the set SXof Spin structures on X is an affine space modelled on H (X; Z).

\mathrm{S{i i n}^{\}}

\mathcal{S}_{X}\textit{o f S p i n}^{\mathbb{C}}

H^{2}(X;\mathbb{Z})

This is slightly nontrivial, and we will not prove it here. (Higher dimen-
C
sional manifolds do not always have Spin structures, although when they
do, they always form an affine space over H2.)

H^{2}.\

2.3 Some group theory

C
To see what associated vector bundles we can get from a Spin structure on a
C
4-manifold, we now need to discuss the representation theory of Spin (4). We
will give explicit four-dimensional constructions, even though some of these
constructions have higher-dimensional generalizations. Some more general
theory is discussed in [1, 2, 11, 13, 8].
We want to explain the following fundamental diagram:

\mathrm{S p i n^{\mathbb{C}}}

\mathrm{S p i n}^{\mathbb{C}}(4)

We want to explain the following fundamental diagram:

\begin{array}{c c c}}&{\ {\\operatorname{U}(2)\ \ \stackrel{\mathrm}~\ \ \ \ \ {\_{{}}}{\ \operatorname\{S{n}}}^{\mathbb{C}}(4)\ \stackrel{\mathrm{}{~\ ~_{{}}{~}}}{\ \stackrel{\mathrm{}{~\ {s}_{{}}}{~}}{{~}}}}\ {

(2.1)

(For us, the most important maps in the diagram are the three maps from
C
Spin (4).) Recall that
{()}

\dot{\mathrm{S p i n}}^4(4).

\operatorname{S U}(2)=\left\{\left(\begin{matrix}{a}&{-{overline b}}\\ {b}&{{\overline{a}}}\end{array}\right):|a|^{2}+|b|^{2}=1\right\}.

We can define an isomorphism

(2.2)

\mathrm{S O}(4)\simeq(\mathrm{S U}(2)\times\mathrm{S U}(2))/\pm1

(h_{-},h_{+})\in\mathbb{S U}(2)\times\mathbb{S U}(2)

(2.3)

Exercise 2.6 Check that this gives an isomorphism as in (2.2).

---

We then have Spin(4) ’ SU (2) × SU (2) and

\sin(4)\simeq\sin U(2)\times S U(2)

\operatorname{S p i n}^{\mathbb{C}}(4)\simeq(\operatorname{S U}(2)\times\operatorname{S U}(2)\times\operatorname{U}(1))/\pm1.

Observe that

\mathbb{U}(2)=(\mathbb{S U}(2)\times\mathbb{U}(1))/\pm1.

C
We can then define the two maps s+,s−: Spin (4) → U(2) in the diagram
(2.1) by
s [h,h,λ] = [h,λ].

s_{+},s_{-}:\mathrm{S p i n}^{\mathbb{C}}(4)\to\mathrm{U}(2)

s_{\pm}[h_{-},h_{+},\lambda]=[h_{\pm},\lambda].

To explain the map U(2) → SO(3), note that there is an isomorphism

(2.4)

\mathrm{U}(2)\to\mathrm{S O}(3)

\mathrm{S O}(3)\simeq\mathrm{S U}(2)/\pm1

defined as follows: identify

\mathbb{R}^{3}\simeq\left\{\left(\begin{matrix}{a}&{-\overline{{b}}}\\ {b}&{\overline{{a}}}\\ \end{matrix}\right):\operatorname{R e}(a)=0\right\},

and let h ∈ SU(2) act on x ∈ R3 by

h\in\operatorname{S U}(2)

x\in\mathbb{R}^{3}

h\cdot x=h x h^{-1}.

Exercise 2.7 Check that this gives an isomorphism as in (2.4).

Now the map U(2) → SO(3) sends [h,λ] 7→±h.
Finally, the fundamental representation of SO(4) on R4

\mathrm{U}(2)\to\mathrm{S O}(3)

[h,\lambda]\mapsto\pm h.

Finally, the fundamental representation of SO(4) on R4 induces an orthogonal representation of SO(4) on Λ2R4 which preserves the decomposition
Λ2R4 = Λ2−R4 ⊕ Λ2+R4. The maps ρ−,ρ+are given by the action of SO(4) on
Λ2−R4, Λ2+R4 respectively.

\Lambda^{2}\mathbb{R}^{4}

\mathrm{S O}(4)

\Lambda^{2}\bar{\mathbb{R}^{4}}=\Lambda_{-}^{2}\bar{\mathbb{R}^{4}}\oplus\Lambda_{+}^{2}\mathbb{R}^{4}

\rho_{-},\rho.

Exercise 2.8 Show that if appropriate identifications of Λ2−R4 and Λ2+R4
with R3 are chosen, then the diagram (2.1) commutes.

\Lambda_{-}^{2}\mathbb{R}^{4}

\Lambda_{+}^{2}\mathbb{R}^{4}

\Lambda_{-}^{2}\mathbb{R}^{4},\Lambda_{+}^{2}\mathbb{R}^{4}

\begin{aligned}{\operatorname{S p i n}^{\mathbb{C}}(4)}&{{}\longrightarrow\operatorname{U}(1),}\\ {\left[h_{-},h_{+},\lambda\right]}&{{}\longmapsto\lambda^{2}.}\\ \end{aligned}

---

2.4 The spinor bundles

C
Let X be an oriented Riemannian 4-manifold with a Spin structure. As-
C 2
sociated to the representations s+,s−of Spin (4) are C bundles S+,S−.
Sections of these bundles are sometimes called spinors. Since the representations s+,s−are unitary, the spinor bundles S+,S−come with Hermitian
metrics.
An important related bundle is the (Hermitian) line bundle L associated

\mathrm{S p i n^{\mathbb{C}}}

S_{+},S_{-}

\mathrm{S p i n}^{\mathbb{C}}(4)

S_{+},S_{-}

S_{+},S_{-}

An important related bundle is the (Hermitian) line bundle L associated
to the representation (2.5).

Exercise 2.9 Show that Λ2S±= L. (This follows from a certain equality of
C
representations of Spin (4).)

\Lambda^{2}S_{+}=L

\mathrm{S p i n}^{\mathbb{C}}(4).)

2.5 Clifford multiplication

The spinor bundles are distinguished from arbitrary vector bundles by their
relation with the frame bundle. This relation manifests itself in the existence
of Clifford multiplication, a map

\operatorname{c l}:T^{*}X\to\operatorname{E n d}(S_{+}\oplus S_{-})

with the following properties:

∗
• For v ∈ T X, cl(v) sends S+to S−and vice-versa.

v\in T^{*}X

S_{+}

S_{-}

\operatorname{c l}(v)^{2}=-|v|^{2}.

• If |v| = 1 then cl(v) is unitary.

\ \mathrm{f}}\ |v|=1\ \mathrm{t t}

∗
We define cl : T X ⊗ S+→ S−as follows. We begin by defining a map
R4 × C2 → C2: using matrix multiplication with the identification (2.3), we
∗
map (x,ψ) 7→ xψ. To show that this induces a map T X ⊗ S+→ S−, by
the definition of associated vector bundle, we have to check that it commutes
C C
with the representations of Spin (4), i.e. that for [h−,h+,λ] ∈ Spin (4),

(h_{-}x h_{+}^{-1})\big(h_{+}\lambda\psi\big)=h_{-}\lambda x\psi

T^{*}X\otimes S_{+}\to\xi

\mathbb{R}^{4}\times\mathbb{C}^{2}\to\mathbb{C}^{2}.

(x,\psi)\mapsto-{\overline{{x}}}^{t}\psi

If α is a 1-form and ψ is a spinor then the notations cl(α)ψ, cl(α ⊗ ψ),
α · ψ all indicate Clifford multiplication by α on ψ.

[h_{-},h_{+},\lambda]\in\mathrm{S p i n}^{\mathbb{C}}(4)

\operatorname{c l}(\alpha)\psi,\,\operatorname{c l}(\alpha\otimes\psi)

\alpha\cdot\psi

---

C
Remark 2.10 A Spin structure is actually equivalent to the bundle S =
S−⊕ S+together with the Clifford action. From this point of view it easy to
describe the H2(X; Z) action on SX: an element α ∈ H2(X; Z) sends S to
S ⊗ E, where E is the line bundle with c1(E) = α.

\mathrm{~A~S p i n^{\mathbb{C}}}

S=

H^{2}(X;\mathbb{Z})

\mathcal{S}_{X}

\alpha\in H^{2}(X;\mathbb{Z})

S\otimes E

c_{1}(E)=\alpha

Digression: Recall that if E is a line bundle on X, the first Chern class
c1(E) ∈ H2(X; Z) is (at least if X is a closed oriented manifold) the Poincar´e
dual of the zero set of a generic section of E. On any X, c1 gives a bijection
between the set of isomorphism classes of line bundles on X and H2(X; Z).

c_{1}(E)\in H^{2}(X;\mathbb{Z})

X,\,c_{1}

H^{2}(X;\mathbb{Z})

Exercise 2.11 (Chern-Weil theory) Prove: If A is a connection on a line
bundle E, then dFA= 0 and the cohomology class [FA] equals −2πic1(E).

d F_{A}=0

-2\pi i c_{1}(E)

2.6 The spin connection

Let A be a connection on L compatible with the metric. This A induces a
C
“Spin connection” A on S+(and S−too).
To really explain this requires a bit more background than we have given

^\mathrm{^{S G}S p i n^{C}}

S_{+}

To really explain this requires a bit more background than we have given
so far. But the idea, abstractly, is that a connection on a principal G bundle
P is a 1-form with values in Lie(G), the Lie algebra of G, satisfying certain
conditions, and this induces a connection on every associated vector bundle.
So to define a connection on S+it is enough to construct a connection on
C
the principal Spin (4) bundle Fˆ. Now the maps

\mathrm{S p i n^^{\mathbb{C}}(4)}

S_{+}

defined previously induce an isomorphism of Lie algebras

(2.6)

\operatorname{L i e}(\operatorname{S p i n}^{\mathbb{C}}(4))\simeq\operatorname{L i e}(\operatorname{S O}(4))\oplus\operatorname{L i e}(\operatorname{U}(1)).

If L is the principal U(1) bundle corresponding to L, then we have maps

---

The Levi-Civita connection gives a Lie(SO(4))-valued 1-form on Fr, and the
connection A gives a Lie(U(1))-valued 1-form on L. Now pull these back to
Fˆ via the above maps, add them, and apply the isomorphism (2.6) to get
the required 1-form on Fˆ.
C
Explicitly, if X is Euclidean space, with Fˆ the trivial Spin (4) bundle, S

\hat{F}

\mathcal{L}

\hat{F}

C
Explicitly, if X is Euclidean space, with Fˆ the trivial Spin (4) bundle, S+
the trivial C2 bundle, and L the trivial line bundle, then the connection A is
j
an imaginary-valued 1-form Ajdx (imaginary-valued, not C-valued, because
the connection is compatible with the metric), and

\hat\{F{

\mathrm{S{i i n}^{\mathbb{C}}(4)}

S_{+}

\mathbb{C}^{2}

A_{j}d x^{j}

\nabla_{\bf A}=d x^{j}\otimes(\partial_{j}+\frac{1}{2}A_{j})

1
acting on C2-valued functions. (The factor of comes from the squaring of λ
2
in the map (2.5).) Note in particular that the spin connection is compatible
with the metric on S+.

\frac{1}{2}

\mathbb{C}^{2}

S_{+}

Exercise 2.12 Show that ∇Ais a module derivation: if α is a 1-form and
ψ is a section of S+⊕ S−then

\nabla_{\mathbf{A}}

\psi

(2.7)

S_{+}\oplus S.

\nabla_{\mathbf{A}}\big(\alpha\cdot\psi\big)=(\nabla_{\Gamma}\alpha)\cdot\psi+\alpha\cdot\nabla_{\mathbf{A}}\psi

\Omega^{1}(X,S_{+}\oplus S_{-})

2.7 The Dirac operator

Definition 2.13 If A is a compatible connection on L, the Dirac operator
DAis the composition

C^{\infty}(S_{+})\;\xrightarrow{\;\nabla_{\mathbf{A}}\;}\;C^{\infty}(T^{*}X\otimes S_{+})\;\xrightarrow{\;\;\operatorname{c l}\;\;\;}C\;^{\infty}(S_{-}).

1
where ∇j= ∂j+ Aj. If we introduce complex coordinates z = x1 + ix2,w =
2
1
x3 + ix4 and let ∇z= (∇1− i∇2), etc., then
2
() ()

D_{A}=\left(\begin{matrix}{\nabla_{1}+i\nabla_{2}}&{-\nabla_{3}+i\nabla_{4}}\\ {\nabla_{3}+i\nabla_{4}}&{\nabla_{1}-i\nabla_{2}.}\\ \end{matrix}\right)

\nabla{_{j}}=\partial_{j}+{\textstyle\frac{1}{2}}A A_{j}

z=x^{1}\!+\!i x^{2},w=

\mathring{\nabla}_{z}=\textstyle{\frac{1}{2}}\big(\nabla_{1}-i\nabla_{2}\big)

(2.8)

In the local model described above,
(

---

2.8 The Seiberg-Witten equations

C
Let X be a smooth oriented Riemannian 4-manifold with a Spin structure.
Fix a self-dual 2-form µ. The Seiberg-Witten equations are

\mathrm{S p i n^{\mathbb{C}}}

\mu.

\begin{array}{c}{{D_{A}\psi=0,}}\\ {{F_{A}^{+}=q(\psi)+i\mu}}\end{array}

where A is a compatible connection on L and ψ is a section of S+.
+
Here F is the self-dual component of F, which is an imaginary-valued

\psi

S_{+}

+
+
Here F is the self-dual component of FA, which is an imaginary-valued
A
2-form. Also
∗
q : S → iΛ2 T X

F_{A}^{+}

F_{A}

q:S_{+}\rightarrow i\Lambda_{+}^{2}T^{*}X

is a quadratic form defined as follows. We extend Clifford multiplication to
a map Λ2 → End(S+) by defining

\Lambda^{2}\to\operatorname{E n d}(S_{+})

\operatorname{c l}(v\wedge w)={\frac{1}{2}}(\operatorname{c l}(v)\operatorname{c l}(w)-\operatorname{c l}(w)\operatorname{c l}(v)).

(2.9)

We extend complex linearly to Λ2 ⊗ C and restrict to get a map

\Lambda^{2}\otimes\mathbb{C}

\operatorname{c l}_{+}:\Lambda_{+}^{2}\otimes\mathbb{C}\to\operatorname{E n d}(S_{+}).

We then define

q(\psi)=\mathrm{c l}_{+}^{\dagger}(\psi\otimes\psi^{\dagger}).

Let’s work out the second of the Seiberg-Witten equations in our local
model. If {e1,...,e4} is the standard basis for R4 then
()

\{e^{1},\ldots,e^{4}\}

(2.10)

\mathbb{R}^{4}

\begin{array}{r l}{{\mathrm{c l}_{+}(e^{1}\wedge e^{2}+e^{3}\wedge e^{4})=\left(\begin{matrix}{{-2i}}&{{}}\\ {{}}&{{2i}}\end{matrix}\right),}}\\ {{}}&{{}}\\ {{\mathrm{c l}_{+}(e^{1}\wedge e^{3}-e^{2}\wedge e^{4})=\left(\begin{matrix}{{}}&{{2}}\\ {{-2}}&{{}}\end{array}\right),}}\\ {{}mathrm{{{c l}_{+}(e^{1}\wedge e^{4}+e^{2}\wedge e^{3})=\left(\begin{matrix}{{}}&{{-2i}}\\ {{-2i}}&{{}}\end{matrix}\right)}}}\end{array}

{\mathrm{I f}}\ \psi={\binom{a}{b}}\,{\mathrm{t h e n}}\ \psi\otimes\psi^{\dagger}={\left(\begin{matrix}{|a|^{2}}&{a{\overline{{b}}}}\\ {{\overline{{a}}}b}&{|b|^{2}}\end{matrix}\right)}\,.

\begin{aligned}{q\left(\begin{matrix}{a}\\ {b}\\ \end{matrix}\right)=}&{{}i(|a|^{2}-|b|^{2})(e^{1}\wedge e^{2}+e^{3}\wedge e^{4})+2i\operatorname{I m}(a\bar{b})(e^{1}\wedge e^{3}-e^{2}\wedge e^{4})}\\ {}&{{}+2i\operatorname{R e}(a\bar{b})(e^{1}\wedge e^{4}+e^{2}\wedge e^{3}).}\\ \end{aligned}

---

′ i j
Let Fijdenote the e ∧ e component of FA− iµ. Then the second Seiberg-
Witten equation becomes

F_{i j}^{\prime\

e^{i}\wedge e^{j}

F_{A}-i\mu

\begin{array}{c}{{F_{12}^{\prime}+F_{34}^{\prime}=2i(|a|^{2}-|b|^{2}),}}\\ {{F_{13}^{\prime}-F_{24}^{\prime}-i(F_{14}^{\prime}+F_{23}^{\prime})=4a\overline{{b}}.}}\end{array}

(2.11)

Remark 2.14 Each paper on Seiberg-Witten theory seems to have a slightly
different version of these equations. This is due to different conventions
for Clifford multiplication and things of this nature. For example, some
authors define q using the inverse of cl+instead of the adjoint, which makes
their q half as large as ours. The conventions in different papers should be
isomorphic under appropriate rescaling.

\mathrm{c l}_{+}

Remark 2.15 The Seiberg-Witten equations were first written down by
Witten [20]. See [9, 13, 8] for more details.

3 The Seiberg-Witten invariants

Let X be a closed oriented smooth 4-manifold. Let g be a Riemannian metric
C
on X and let µ be a self-dual 2-form. Let s ∈SXbe a Spin structure and
let S+,S−,L be the corresponding vector bundles. If A is a connection on
L and ψ is a section of S+, then (A,ψ) satisfy the Seiberg-Witten equations
when ()
D ψ

\mu

s\in\mathcal{S}_{X}

\mathrm{S p i n^{}}

\beta_{+},\beta_{-},L

\psi

S_{+}

(A,\psi)

\mathcal{F}(A,\psi)=\left(\begin{matrix}{D_{A}\psi}\\ {F_{A}^{+}-q(\psi)-i\mu}\end{matrix}\right)

3.1 Gauge transformations

vanishes. Let us introduce

to denote the space of solutions of the Seiberg-Witten equations. In this
lecture we will discuss how to get information about X by studying topological properties of ms,g,µthat do not depend on g and µ. This information
constitutes the Seiberg-Witten invariants of X. For more details on the construction of these invariants, see [13, 8].

{mathfrak\mathfrak m{}}_{s,g,\mu} a finite dimensional space. The group in question is C ∞ (X,S1). A function h : X → S1 (a gauge transformation) acts on m by

h(A,ψ) = (A − 2h −1 dh,hψ).

Exercise 3.1 1. Check that this action sends m to itself.

2. Show that this action is free, except that a point with ψ ≡ 0 has stabilizer S1. Define
M = m/C ∞ (X,S1), M0 = m/{φ ∈ C ∞ (X,S1) : φ(∗) = 1}.

Here ∗∈ X is some base point. The group {φ ∈ C ∞ (X,S1) : φ(∗) = 1} of based gauge transformations always acts freely on m, so the space M0 is a bit more likely than M to be nonsingular. We topologize these spaces as follows. We topologize the set of all pairs (A,ψ) (not necessarily satisfying the Seiberg-Witten equations) with the C ∞

Frechet topology. We give m the subspace topology, and we then give M and M0 the quotient topology.

# 3.2 Basic properties of the moduli space

We need the following notation. ∫ There is a quadratic form Q on H2(X; R) given by Q(α,β) = X α ∧ β ∈ R. Often we write α · β instead of Q(α,β). We define b2+(resp. b2−) to be the dimension of a maximal positive definite (resp. negative definite) subspace of H2(X; R). Also b i denotes dim H i (X; R). (The numbers b i and b2±and the quadratic form Q depend only on the homotopy type of X.) C 0 Fix a Spin structure s. The moduli spaces M, M have the following basic properties.

Proposition 3.2 (a) M is always compact.

(b) For generic µ (if g is fixed), M0 is a smooth finite dimensional manifold with a C
∞ circle action. If b 2+ > 0, then for generic µ, M is smooth and M0 →M is a principal S1 bundle.

---

(c) For generic µ,
1 2 c21− τ dim(M) = b − 1 − b++. (3.1) 4 Here τ = b2+−b2−is the signature of X, c1 = c1(L), and c21= Q(c1,c1).

(d) M is orientable (for generic µ). Moreover there is a canonical bijec- tion between orientations of M and orientations of the vector space H0(X; R) ⊕ H1(X; R) ⊕ H+
2 (X; R), where H+ 2 (X; R) is a maximal pos- itive definite subspace for Q.

(e) If (g0,µ0) and (g1,µ1) are generic, then for a generic path (gt,µt) con- necting them, W0 = {t, M0g
t ,µt} is a smooth compact oriented manifold with boundary −M00+ M01. If b2+> 1, we can choose the path so that W = {t, Mgt,µt} is also smooth and ∂W = −M0 + M1.

The compactness property (a) is remarkable for two reasons. First, there is no a priori reason to expect compactness in a situation like this. For exam- ple, if we change q to −q in the second of the Seiberg-Witten equations, then compactness will fail. Second, one might have previously thought that an equation with a compact moduli space would not contain interesting topolog- ical information. For example, the noncompactness of the moduli spaces for the older Yang-Mills equations played a key role in the proof of Donaldson’s first theorem (which says that if Q is positive definite or negative definite then Q : H2(X; Z) → Z can be diagonalized over the integers, which is a very strong restriction on Q). We will outline the proof of compactness later in this lecture. On the other hand, properties (b)–(e) follow from standard machinery. This is because the deformation complex for the Seiberg-Witten equations (i.e. the linearization of the equations, which defines T(A,ψ)M) is elliptic, and there is a standard package for dealing with equations of this type. Another example of an elliptic equation is the equation for pseudoholomorphic curves, for which analogues of properties (b)–(e) are proved using similar techniques. In particular, the dimension formula (c) is proved using the Atiyah-Singer index theorem. Property (d) is proved using the index theorem for families. The rough idea is that the derivative of the Seiberg-Witten equations is a family of operators parametrized by M, and one applies the theorem to this family. Properties (b) and (e) are proved using the Sard-Smale theorem, which is a basic tool for proving infinite-dimensional transversality results.

---

These proofs can be found in, e.g., [13, 8]. Even so, Proposition 3.2 was understood by Witten [20]. In particular, Witten has a proof of compactness.

# 3.3 Why the conditions on b

+ ?

If M0 is smooth, then M = M0/S1 will also be smooth provided that S1 acts freely, i.e. as long as there are no solutions (A,ψ) to the Seiberg-Witten equations with ψ ≡ 0. (As a throwback to Yang-Mills theory, one might call such a solution reducible.) If ψ ≡ 0 then the Seiberg-Witten equations read

F A + = iµ. (3.2)

Let H2 be the space of harmonic 2-forms on X. Recall the Hodge decom- position Ω2 = H2 ⊕ dΩ1 ⊕∗dΩ1.

Let h : Ω2 →H2 be the projection.

Exercise 3.3 1. Equation (3.2) has a solution A if and only if

h(F A + ) = h(iµ).

2. h(F A + ) is the self-dual part of the harmonic representative of −2πic1(L), and hence depends only on L. From this exercise we see that reducibles exist if and only if h(iµ) equals
a certain invariant of L in the space H+ 2 of harmonic self-dual 2-forms. Since dim(H+ 2 ) = b 2+ , this is a codimension b2+condition on µ, at least at the level of heuristic dimension counting. So if b2+> 0, then for generic µ we expect no reducibles, and if b2+> 1 then we expect no reducibles for generic 1-parameter families of µ.

# 3.4 Outline of the proof of compactness

The outline that follows is based on arguments in [9]. The key to compactness is the following a priori estimate:

Lemma 3.4 [9] If F (A,ψ) = 0 (and ψ is not identically zero), then () 2 −s |ψ| ≤ max + 2|µ| (3.3) X 2

## at every point in X.

---

Here s is the scalar curvature of the Riemannian metric on TX. (With
respect to a local orthonormal frame, the curvature of the Levi-Civita conij
nection is a tensor with components R, antisymmetric in (i,j) and also in
∑kl
ij
(k,l). Then s = R. For example, the scalar curvature of the round
i,j ij
metric on S4 is 12.)
To prove this lemma we need the following background:

^\mathrm{a}

R_{k l}^{i j}

(k,l)

(i,j)

\begin{array}{r}{s=\sum_{i,j}R_{i j}^{i j}}\end{array}

S^{4}

To prove this lemma we need the following background:

Exercise 3.5 1. Prove the Bochner-Weitzenb¨ock formula:

D_{A}^{\dagger}D_{A}=\nabla_{\bf A}^{\dagger}\nabla_{\bf A}+\frac{s}{4}+\frac{1}{2}\operatorname{c l}(F_{A})

∞
as operators on C (S+⊕ S−). (The curvature terms arise from commutators of covariant derivatives as in Exercise 1.13.)

C^{\infty}(S_{+}\oplus S_{-})

2. Show that if ψ is a section of S+then
(

\psi

S_{+}

D_{A}^{\dagger}D_{A}\psi=\left(\nabla_{\bf A}^{\dagger}\nabla_{\bf A}+\frac{s}{4}+\frac{1}{2}\operatorname{c l}_{+}(F_{A}^{+})\right)\psi.

(3.4)

†
Remark 3.6 It turns out that D = DA. So the Bochner-Weitzenb¨ock
A
2 †
formula says that D equals the “covariant Laplacian” ∇ ∇A, modulo lower
A A
order terms. This is basically the property that Dirac was looking for when
he defined the Dirac operator, and this requirement naturally leads to the
notion of Clifford multiplication. (See [3].)

D_{A}^{\dagger}\,=\,D_{A}

D_{A}^{2}

\nabla_{A}^{\dagger}\nabla_{A}.

2
Proof of Lemma 3.4. Choose a point in X at which |ψ| is maximized. Then

|\psi|^{2}

\triangle|\psi|^{2}\geq0

∗
at this point. (Here 4 = dd.) Compatibility of A with the metric implies

Plugging both Seiberg-Witten equations into the Bochner-Weitzenb¨ock formula (3.4) gives

\begin{array}{r}{\triangle|\psi|^{2}=2\operatorname{R e}\langle\nabla_{\mathbf A}^{\dagger}\nabla_{\mathbf A}\psi,\psi\rangle-2|\nabla_{\mathbf A}\psi|^{2}}\\ {\leq2\operatorname{R e}\langle\nabla_{\mathbf A}^{\dagger}\nabla_{\mathbf A}\psi,\psi\rangle.}\end{array}

---

Putting this into the inequalities above and using the definition of q we get 〈() 〉 −s 1† † 0 ≤ 2 Re − cl+(cl+(ψ ⊗ ψ) + iµ) ψ,ψ. 4 2

Now cl+: Λ2+→ End(S+) is injective and multiplies lengths by 2, and its image consists of the traceless endomorphisms. It follows that () † † †12 cl+(cl+(ψ ⊗ ψ)) = 2 ψ ⊗ ψ − |ψ|. 2

Putting this into the inequality above we get () −s 2 2 0 ≤ −|ψ| + 2|µ| |ψ| 2

at a point where |ψ| 2 is maximized. This implies the a priori estimate (3.3). ✷ Starting from this, the idea of the proof of compactness is to use “boot- strapping” to get bounds on all the higher derivatives of A and ψ. Schemat- ically, the Seiberg-Witten equations are of the form () () A ψ2 D = + smooth (3.5) ψ Aψ

where D is a certain linear combination of derivatives. By this equation, the bound on ψ2 gives a bound on certain linear combinations of the derivatives of A and ψ. If these bounds imply bounds on all derivatives of A and ψ, then (3.5) can be differentiated to obtain estimates for the second derivatives of A and ψ in terms of the estimates for the first derivatives. Repeating this procedure over and over gives bounds on all higher derivatives. Compactness then comes from the Arzela-Ascoli theorem. Thus the key is whether the bounds for the linear combinations of derivatives in (3.5) give bounds on all derivatives. This turns out to be the case, as the Seiberg-Witten equations are elliptic after gauge fixing (which we will not discuss).

# 3.5 The Seiberg-Witten invariant

Assume b2+(X) > 1 and µ is generic. Suppose also that we have fixed an orientation of the vector space H0(X; R) ⊕ H1(X; R) ⊕ H+ 2 (X; R).

---

Definition 3.7 Using the basic properties of the moduli space in Proposi- tion 3.2, we define the Seiberg-Witten invariant

## SWX: SX→ Z

as follows. If b2+− b1 is odd, it turns out (using topological facts about the 2 c 2 1 −τ intersection form Q) that the dimension of the moduli space b1− 1 − b++ 4 is an even integer 2d. With this understood, set:

- SWX= 0 if b2+− b1 is even.
C

- For a Spin structure s, if d < 0 then SWX(s) = 0.
- If d = 0, then M is a finite set of points, and the orientation assigns
∑ an element of {±1} to each point. Set SWX(s) = M ±1.

- If d > 0 then M is a smooth, oriented 2
∫ d dimensional compact mani- fold. Set SWX(s) = M e d , where e ∈ H2(M; Z) is the first Chern class of M0 →M (more precisely the first Chern class of the associated line bundle (M0 × C)/S1).

The following are some “formal” properties of SW which can be proved more or less directly from the definition, and the basic properties listed in Proposition 3.2. (See e.g. [13, 8].)

Theorem 3.8 (a) If b2+(X) > 1, then SWX(s) depends only on s and gives a diffeomorphism invariant SWX: SX→ Z.

(b) SWX(s) = 0 for all but finitely many s.
(c) SW X#CP2
contains the same information as SWX. (There is a blowup formula which we will not give here.)

(d) If X = Y #Z and b2+(Y),b2+(Z) > 0 then SWX≡ 0. (This does not contradict (c) because b2+(CP2) = 0.)
C

(e) There is a charge conjugation involution s 7→ s on the set of Spin structures (which sends c1(L) to −c1(L)), and SW(s) = ± SW(s).
(Note that Y #Z is the connect sum of Y and Z. It is obtained by cutting out small balls in Y and Z and gluing the results together along the boundary spheres. The invariants b2+,b1 are additive under this operation. Note that CP2 is complex projective space with its non-complex orientation.)

---

3.6 Examples and applications

For an example where the Seiberg-Witten invariant is nontrivial and has an
interesting application, consider the K3 surface

K3=\left(z_{1}^{4}+z_{2}^{4}+z_{3}^{4}+z_{4}^{4}=0\right)\subset\mathbb{C}P^{3}.

2 2 C
This 4-manifold has b+= 3,b−= 19. On K3, there is a unique Spin
C
structure s with c1(s) = 0. For this s, SWK3(s) = ±1. For all other Spin
structures, SW = 0. (This will follow from the computation in the next
lecture.)
Theorem 3.8(c) implies that the blow up K3#CP2 has nontrivial Seiberg-

b_{\pm}^{2}\,=\,3,b_{-}^{2}\,=\,19

\mathrm{S p i n^{\mathbb{C}}}

c_{1}(s)=0

S W_{K3}(s)=\pm1

\S N\,=\,0

Theorem 3.8(c) implies that the blow up K3#CP2 has nontrivial Seiberg-
Witten invariants. (In fact if e is the Poincar´e dual of the exceptional divisor,
C
and if s is a Spin structure with c1(L) = ±e, then SW(s) = ±1. This can
also be deduced from the computation in the next lecture.) Now Freedman’s theorem, which classifies topological 4-manifolds, says that K3#CP2
is homeomorphic to Y = #3CP2#20CP2 (because the two 4-manifolds have
equivalent intersection forms over Z). But SWY≡ 0 by Theorem 3.8(d). So
we recover the following theorem of Donaldson:

K3\#{\overline{{\mathbb{C}P^{2}}}}

\mathrm{S p i n^{C\mathbb}}

c_{1}(L)=\pm e

\mathrm{S W}(s)=\pm1

K3\#{overline{{\mathbb{C}P^{2}}}}

Y=\#_{3}\mathbb{C}P^{2}\#_{20}\overline{{\mathbb{C}P^{2}}}

\S W_{Y}\equiv0

Theorem 3.9 K3#CP2 and #3CP2#20CP2 are not diffeomorphic, even
though they are homeomorphic.

K3\#{\overline{{\mathbb{C}P^{2}}}}

\#_{3}\mathbb{C}P^{2}\#_{20}\overline{{\mathbb{C}P^{2}}}

(This theorem was first proved by Simon Donaldson using his celebrated
4-manifold invariants [4]. See also [5].)
For another application, we will show in the next lecture that if X has a

For another application, we will show in the next lecture that if X has a
2 C
symplectic structure and b+> 1 then there exists a Spin structure s with
SW(s) = ±1. This combines with the vanishing theorem 3.8(d) to give an
obstruction to the existence of symplectic forms. For example, we get:

b_{+}^{2}>1

\mathrm{S{i i i}^{mathbb{C}}}

\mathrm{S W}(s)=\pm1

Theorem 3.10 [14] ⊕mCP2 does not have a symplectic form when m > 1.

Let X be a closed smooth 4-manifold with b2+> 1. Suppose that X has a
symplectic form ω (i.e. ω is a 2-form, dω = 0, and ω ∧ ω never vanishes).
In this lecture we will compute the Seiberg-Witten invariant of X for the
C
simplest Spin structures.

\omega

(4)\oplus_{m}\mathbb{C}P^{2}

b_{+}^{2}>1

(This is true for homotopy theoretic reasons when m is even, so the interesting
case is when m is odd.)

d\omega=0

\omega\wedge\omega

m>1

4 The symplectic case, part I

\mathrm{S p i n^{c}}

---

4.1 Statement of the theorem

We need the following basic facts about our symplectic 4-manifold:

1. X has a canonical orientation, given by ω ∧ ω.

\omega\wedge\omega.

C
2. There is a canonical Spin structure s0 ∈ SX. Thus we can identify
SX’ H2(X; Z), by sending s0 to 0 and extending equivariantly. (We
will explain this shortly.)

\mathrm{S p i n^{}}

s_{0}\in\mathcal{S}_{X}

{\mathcal{S}}_{X}\simeq H^{2}(X;\mathbb{Z})

3. The moduli spaces M have canonical orientations. (This is subtle and
we will not explain it.)

These three facts allow us to regard the Seiberg-Witten invariant as a map

\mathrm{S W}:H^{2}(X;\mathbb{Z})\to\mathbb{Z}.

2,0
Let K = T X (defined below) and c = c1(K). Then:

K=T^{2,0}X

c=c_{1}(K)

Theorem 4.1 [14, 15]

[14,15]

\operatorname{S W}(0)=1.

(a) SW(0) = 1.

(b) SW(c) = ±1.

\operatorname{S W}(c)=\pm1.

\ {mathrm boldmath\~~W}}(e)=\pm\operatorname{S W}(c-e)

(d) If SW(e) 6= 0, then

\mathrm{S W}(e)\neq0

0\leq[\omega]\cdot e\leq[\omega]\cdot c,

and if either equality holds then e = 0 or e = c.

(4.1)

Part (c) comes from the “charge conjugation invariance” stated in Theorem 3.8(e). Parts (a) and (c) clearly imply (b). The rest of this lecture will
be devoted to proving (a) and (d).

e=0\;o r\;e=c.

g(v,w)=\omega(v,J w)

C
4.2 The canonical Spin structure
An ω-compatible almost complex structure is a map J : T

J:T^{*}X\to T^{*}X

\ dot J{{}}^2=-1

---

Exercise 4.2 Given a nondegenerate 2-form ω and a Riemannian metric g,
there exists√J satisfying (4.1) if and only if ω is self-dual with respect to g
and |ω| = 2.

\omega

|\omega|={\sqrt{2}}

\omega

Choose an ω-compatible J, and endow X with the Riemannian metric g
given by (4.1). The almost complex structure gives a decomposition
⊕

\Lambda^{*}T^{*}X\otimes\mathbb{C}=\bigoplus_{p,q}T^{p,q},

p,q p 1,0 q 0,1 1,0 0,1
where T = ∧ T ⊗∧ T and T (resp. T) is the holomorphic (resp.
∗
antiholomorphic) part of T X ⊗ C.
C
Suppose a Spin structure is chosen. Clifford multiplication by ω, cl (ω) :

T^{p,q}=\Lambda^{p}T^{1,0}\otimes\wedge^{q}T^{0,1}

T^{1,0}\;\mathrm{(r e s p.~}T^{0,1}{\big)}

T^{*}X\otimes\mathbb{C}

C
Suppose a Spin structure is chosen. Clifford multiplication by ω, cl+(ω) :
S+→ S+splits S+into ±2i eigenspaces. (In the local model of the second
lecture, ω = dx1dx2+dx3dx4, so this claim follows from equation (2.10).) Let
E be the −2i eigenspace. This is a line bundle on X. We define the canonical
C
Spin structure to be the one for which E is trivial. Thus the identification
SX→ H2(X; Z) sends s to c1(E).
Here are some key facts about the spin bundles and the Clifford action.

\mathrm{S p i n}^{\ {\bar{c}}}

\omega,\mathrm{c}]_{+}(\omega)

\mathcal{S}_{+}\rightarrow\mathcal{S}_{+}

S_{+}

\pm2i

\omega=d x^{1}d x^{2}\!+\!d x^{3}d x^{4}

\mathrm{S{i i n}^{\mathbb{C}}}

{\mathcal{S}}_{X}\to H^{2}(X;\mathbb{Z})

c_{1}(E)

Here are some key facts about the spin bundles and the Clifford action.

Lemma 4.3 There are natural identifications

S_{+}=(T^{0,0}\oplus T^{0,2})\otimes E=E\oplus(K^{-1}\otimes E),

(4.2)

(4.3)

S_{-}=T^{0,1}\otimes E

∗
such that the formula for Clifford multiplication by v ∈ T X ⊗ C acting on
0,∗
α ∈ T ⊗ E is
√
0,1 1,0
cl(v) · α = 2(v ∧ α − ı(v)α). (4.4)

v\in T^{*}X\otimes\mathbb{C}

\alpha\in T^{0,*}\otimes E

(4.4)

\mathrm{c l}\ v(big)\cdot\alpha=\sqrt{2}\big(v^{0,1}\wedge\alpha-\imath\big\(\overline{{v^{1,0}}}\big)\alpha\big).

−1
In particular, cl(ω) equals −2i on E and +2i on K E.
0,1 0,1
(Here v is the T component of v, and ı denotes interior product.)

0,1 0,1
(Here v is the T component of v, and ı denotes interior product.)

T^{0,1}

\omega

S_{+}

{\frac{1}{2}}\,\mathrm{c l}

C
Proof. Starting with a Spin structure as we defined it in the second lecture,
the isomorphisms (4.2), (4.3) are given by rescaled Clifford multiplication.
More precisely we extend Clifford multiplication to a complex linear map
∗ ∗
cl : Λ T X ⊗ C → End(S+⊕ S−) as in (2.9). Then there is an isomorphism
−1 1
from K ⊗ E to the +2i eigenspace of ω on S+given by cl. (We put in the
2
1
factor of to make this an isometry.) We can see that this gives the desired
2
isomorphism because in the local model of the second lecture,
()

+2i

K^{-1}\otimes E

\frac{1}{2}

---

This explains (4.2). The isomorphism T 0,1 ⊗E → S−in (4.3) is given similarly by√1cl. It is then straightforward to check (4.4). ✷ 2() α∞ With the preceding understood, we can write ψ = with α ∈ C (E) β and β ∈ Ω 0,2 (X,E). The second Seiberg-Witten equation is then

F A + = i(|α| 2 −|β| 2

) + 2(αβ − αβ) + iµ. (4.5)
(We obtain this from the local calculation (2.11) by putting α = a and β = −21 bdzdw.) We can also state the formula for the dimension 2d of the moduli space M. If e = c1(E) and c = c1(K), then (3.1) and some fiddling with characteristic classes imply 2d = e · e − c · e. (4.6)

In particular, when e = 0 the moduli space is a finite number of points, and to prove Theorem 4.1(a) we must show that the signed number of points is ±1.

# 4.3 Step 1: Understanding the Dirac equation

The first step in the proof of Theorem 4.1 is to write the first of the Seiberg- Witten equations in a nice form, by writing the Dirac operator in terms of the Cauchy-Riemann operator ∂. We begin by observing that there is a canonical connection A0 on K −1 . C −1 Consider the canonical Spin structure and identify S+= (X × C) ⊕ K. Let u0 be the constant section of X × C which assigns 1 ∈ C to each point of X.

Lemma 4.4 There exists a unique compatible connection A0 on K −1 such that ∇A0u0 ∈ Ω1(X,K −1 ),

where A0 is the spin connection associated to A0.

Proof. Let A be a compatible connection on K. Any other compatible connection can be written as A + a where a is an imaginary-valued 1-form. We have 1 ∇A+au0 = ∇Au0 + au0. 2

---

Since A is compatible with the metric, the X × C component of ∇Au0 is an
imaginary-valued 1-form (times u0). So the unique solution is A0 = A + a
where a = −2(∇Au0)X×C. ✷
If X is K¨ahler, ∇ u0 vanishes altogether. If X is not K¨ahler, we still

X\times\mathbb{C}

\nabla_{\mathbf{A}}u_{0}

u{{\}_{{}00}}}}

A_{0}=A+a

a=-2(\nabla_{\mathbf{A}}u_{0})_{X\times\mathbb{C}}

A X×C
If X is K¨ahler, ∇A0u0 vanishes altogether. If X is not K¨ahler, we still
have
D u0 = 0. (4.7)

\nabla_{\mathbf{A}_{0}}u_{0}

D_{A_{0}}u_{0}=0.

To see this, note the following Leibniz-type formula for the Dirac operator:

D_{A_{0}}(\boldsymbol{\omega}\cdot\boldsymbol{u}_{0})=\big(d\boldsymbol{\omega}+d^{*}\boldsymbol{\omega}\big)\cdot\boldsymbol{u}_{0}+\mathrm{c l}\big(\boldsymbol{\omega}\cdot\nabla_{\mathbf{A}_{0}}\boldsymbol{u}_{0}\big).

(4.8)

(This much is true for any connection, differential form, and spinor, and can
be derived from (2.7). The rightmost term here means the following: start
∞ ∗
with ∇A0u0 ∈ C (T X ⊗ S+), first apply 1 ⊗ cl(ω) to get another element
∞ ∗ ∞
of C (T X ⊗ S+), and then apply cl to get an element of C (S−).)
∗
Now u0 is in the −2i eigenspace of cl(ω) and ∇ u0 is in (T X tensor)

\nabla_{\mathbf{A}_{0}}u_{0}\in C\mathcal^{\infty}(T^{*}X\otimes S\_{+})

1\otimes\mathrm{c l}(\omega)

C^{\infty}(T^{*}X\otimes S_{+})

C\!^{\infty}(\!\!S_{-})!\

∗
Now u0 is in the −2i eigenspace of cl(ω) and ∇A0u0 is in (T X tensor)
the +2i eigenspace. Also ω is closed and self-dual. So (4.8) becomes

u_{0}

\nabla_{\mathbf{A}_{0}}u_{0}

\omega

-2i D_{A_{0}}u_{0}=0+2i D_{A_{0}}u_{0}.

This proves (4.7).
Now we come to the point.

C
Now we come to the point. Consider an arbitrary Spin structure with
−1 −1
S+= E ⊕ K E. We can write any connection A on L = K E2 as A0 + 2a
−1
where A0 is the canonical connection on K and a is a connection on E.
Then the formula for the Dirac operator is the following.

\mathrm{S p i n^{}

S_{+}=E\oplus K^{-1}E

L=K^{-1}E^{2}

A_{0}+2a

K^{-1}

A_{0}

Lemma 4.5 If a is a connection on E, α is a section of E, and β is a
−1
section of K E, then
()
√

K^{-1}\overset{\circ}{E}

(4.9)

0,k 0,k+1
(Here ∂a: Ω (X,E) → Ω (X,E) denotes the antiholomorphic part of
∇a.)

\overline{{\partial}}_{a}:\Omega^{0,k}(X,E)\,\to\,\Omega^{0,k+1}(X,E)

\nabla_{a}.

\mathrm{S p i n^{C}}

\begin{aligned}{D_{A_{0}}(\alpha+\beta)}&{{}=D_{A_{0}}\left(\left(\alpha+\frac{\beta}{2}\right)\cdot u_{0}\right)}\\ {}&{{}=\left(d\alpha+\frac{d\beta+d^{*}\beta}{2}\right)\cdot u_{0}}\\ {}&{{}=\sqrt{2}(\overline{{\partial}}\alpha+\overline{{\partial}}^{*}\beta).}\\ \end{aligned}

C
Proof. First consider the canonical Spin structure. By (4.4), the Leibniz
rule as in (4.8), and (4.7), we have
(())

---

∗ C (Since β is self-dual, cl(dβ) = cl(d β).) The case of a general Spin structure and connection a follows formally from this. ✷ (When X is K¨ahler, A0 comes from the Levi-Civita connection, and (4.9) follows more straightforwardly from (4.4).)

## Exercise 4.6 Prove Theorem 4.1(c).

# 4.4 Step 2: deforming the curvature equation

Since the Seiberg-Witten invariant does not depend on µ, we can choose µ to suit our convenience. Normally one might think of choosing µ to be small, so as to perturb the equations and get a smooth moduli space. But we will choose µ to be very large. We take

µ = rω − iF A + 0

where r is a large positive real number. √ Let’s also rescale by writing ψ = r(α,β). Then the Seiberg-Witten equations become, by (4.5) and (4.9), ∗ ∂aα = −∂aβ, (4.10) −ir 2 2 Fa+= (1 −|α| + |β|)ω − r(αβ − αβ). (4.11) 2

We will later need to decompose the curvature equation (4.11) as follows. We have Λ2+⊗ C = Cω ⊕ K ⊕ K −1 .

## So (4.11) implies

Fa0,2= rαβ, (4.12) 〈ω,Fa〉 = −ir(1 −|α| 2 + |β| 2

). (4.13)
# 4.5 Step 3: uniqueness of the solution

C For the canonical Spin structure, a is just an imaginary-valued 1-form, and the equations (4.10), (4.11) have an obvious solution, given by a ≡ 0, α ≡ 1, β ≡ 0. We will now show that this is the only solution (up to gauge equivalence) if r is sufficiently large. This will prove Theorem 4.1(a) (modulo a transversality issue, see below). In the following calculations we will begin

---

C
with an arbitrary Spin structure, which will allow us to simultaneously prove
Theorem 4.1(d).
We need the following background. First, the Nijenhuis tensor is a

\mathrm{S p i n^{\mathbb{C}}}

We need the following background. First, the Nijenhuis tensor is a
1,0 0,2
map N : Ω (X) → Ω (X) defined by

N:\Omega^{1,0}(X)\to\Omega^{0,2}(X)

N(\alpha)=(d\alpha)^{0,2}.

This is a measure of the failure of the almost complex structure to be inte-
1,0 0,2
grable. We claim that N is actually a tensor, i.e. a section of Hom(T,T).
∞
To show this, we have to check that N (fα) = fN (α) for every f ∈ C (X, C);
and this follows readily from the definition.
Second, we need another Weitzenb¨ock formula, which says that

(T^{1,0},T^{0,2})

N(f\alpha)=f N(\alpha)

f\in C^{\infty}(X,\mathbb{C})

Second, we need another Weitzenb¨ock formula, which says that

(4.14)

2\overline{{{partial\}}}_{a}^{*}\overline{{{\partial}}}_{a}=\nabla_{a}^{*}\nabla_{a}-i\langle\omega,F_{a}\rangle

∞
on C (E). (See e.g. [5, p. 212]; there X is assumed to be K¨ahler, but the
proof does not use the assumption that J is integrable.)
Now here is the proof that the solution is unique. Applying ∂ to the Dirac

C^{\infty}(E)

Now here is the proof that the solution is unique. Applying ∂ato the Dirac
equation (4.10) and then using Exercise 1.14 and the curvature equation
(4.12) gives

\overline{{\partial}}_{a}

\begin{array}{r}{{overline{{\partialpartial}}}}_{{a}{\overline{{\partial}}}_{a}^{*}\beta=-{\overline{{\partial}}}_{a}{\overline{{\partial}}}_{a}\alpha}\\ {=-F_{a}^{0,2}\alpha+N(\partial_{a}\alpha)}\\ {=-r|\alpha|^{2}\beta+N(\partial_{a}\alpha).}\end{array}

Multiply by β and integrate over X to get
∫ ∫

\overline{{\beta}}

(4.15)

\int|\overline{{\partial}}_{a}^{*}\beta|^{2}=\int\left(\langle\beta,N(\partial_{a}\alpha)\rangle-r|\alpha|^{2}|\beta|^{2}\right).

Since N is a tensor bounded independent of r, we can use the triangle inequality to estimate
∫ ∫ ∫

\int\left(|\overline{{\partial}}_{a}^{*}\beta|^{2}+r|\alpha|^{2}|\beta|^{2}-\frac{r}{2}|\beta|^{2}\right)\leq\frac{z}{r}\int|\nabla_{a}\alpha|^{2}

(4.17)

\int\langle\beta,N(\partial_{a}\alpha)\rangle\leq\frac{r}{2}\int|\beta|^{2}+\frac{z}{r}\int|\nabla_{a}\alpha|^{2}

---

∫
2
We next want to estimate |∇aα|. Apply the Weitzenb¨ock formula
(4.14) to α, take the inner product with α, integrate over X, and apply the
curvature equation (4.13) to get
∫ ∫

\int|\nabla_{a}\alpha|^{2}

\alpha.

\alpha

\int|\nabla_{a}\alpha|^{2}=\int\left(2|\overline{{\partial}}_{a}\alpha|^{2}+r(1-|\alpha|^{2}+|\beta|^{2})|\alpha|^{2}\right).

(4.18)

Now comes a key step, where we bring in cohomological information about
e = c1(E). Chern-Weil theory tells us that
∫

e=c_{1}(E)

-2\pi i[\omega]\cdot e=\int\omega\wedge F_{a}.

Using the fact that ω is self-dual and putting in the curvature equation (4.13)
gives
∫

2\pi[\omega]\cdot e=\int r(1-|\alpha|^{2}+|\beta|^{2}).

Putting this into (4.18) gives
∫ ∫

\int|\nabla_{a}\alpha|^{2}=2\pi[\omega]\cdot e+\int\left(2|\overline{{\partial}}_{a}\alpha|^{2}+r(1-|\alpha|^{2}+|\beta|^{2})(|\alpha|^{2}-1)\right).

2 2 2
(It is auspicious that the square (1−|α|) appears.) Now replace |∂aα| with
∗
2
|∂aβ| (by the Dirac equation (4.10)), put (4.17) (times 2) into the integral
2 2
on the right, discard the positive term r|α| |β|, and rearrange to obtain
∫ (())

(1\!-\!|\alpha|^{2})^{2}

|\overline{{\partial}}_{a}\alpha|^{2}

|\overline{{\partial}}_{a}^{*}\beta|^{2}

\int\left(\left(1-{frac22}r\right)|\nabla_{a}\alpha|^{2}+r(1-|\alpha|^{2})^{2}\right)\leq2\pi[\omega]\cdot e.

r|\alpha|^{2}|\beta|^{2}

(4.19)

If we choose r > 2z, then we can now read off the conclusions of Theorem 4.1 from the inequality (4.19).
If [ω] · e < 0 then clearly no solution is possible.

If [ω] · e < 0 then clearly no solution is possible.
If [ω] · e = 0 then we must have |α|≡ 1 and β ≡ 0. In particular E has a

\alpha\equiv1

|\alpha|\equiv1

\beta\equiv0

a\equiv0

If [ω] · e = 0 then we must have |α|≡ 1 and β ≡ 0. In particular E has a
nonvanishing section, so e = 0. After a gauge transformation, α ≡ 1. From
previous equations we have ∇aα ≡ 0, which implies a ≡ 0. So this is the
only solution. To complete the proof that SW (e) = ±1, one must check that
the moduli space is cut out transversely at this point. The proof is similar
to the above calculation and we omit it.
If [ω] · e ≥ [ω] · c, we draw analogous conclusions by using charge conju-

\nabla_{a}\alpha\,\equiv\,0.

\ \big[\omega\big]\cdot e\ 0

---

## 4.6 Appendix: an estimate on beta

We are done with the proof of Theorem 4.1. The key was the estimate (4.19) involving α. Using some of the same techniques, we can also get an estimate on β. We will now do this, as it will help motivate the main theorem in the next lecture. We are going to use equation (4.15) a different way. There is another Weitzenb¨ock formula which tell us that ∫ ∫ ∗ 21 (∗ 2 2) |∂aβ| = |∇aβ| − i〈ω,Fa〉|β|. 2

Putting in the curvature equation (4.13), we get ∫ ∫ () ∗ 21∗ 2r2 2 2 |∂aβ| = |∇aβ| + (1 −|α| + |β|)|β|. (4.20) 2 2

Also, by using the triangle inequality differently, we can replace (4.16) with ∫ ∫ ∫ r 2 z 2 〈β,N (∂aα)〉≤ |β| + |∇aα|, (4.21) 4 r

where z is a new constant which is still independent of r. Putting (4.20) and (4.21) into (4.15) and discarding the positive |α| 2 |β| 2 term, we obtain the following estimate: ∫ () ∫ 1 ∗ 2 r 4 r 2 z 2 |∇aβ| + |β| + |β| ≤ |∇aα| . (4.22) 2 2 4 r

# 5 The symplectic case, part II

We will now discuss the Seiberg-Witten invariant on a symplectic manifold 2 C X (with b+> 1) for the remaining Spin structures, and explain that it is equal to a certain count of pseudoholomorphic curves in X.

## 5.1 Summary of the last lecture

Since X is symplectic, there is an identification

### SX’ H2(X; Z).

---

2 C
An element e ∈ H (X; Z) corresponds to a Spin structure with

e\in H^{2}(X;\mathbb{Z})

\mathrm{S p i n^{\mathbb{C}}}

S_{+}=E\oplus K^{-1}E

where c1(E) = e, and K is the canonical bundle coming from an ω-compatible
almost complex structure J. We can regard the Seiberg-Witten invariant as
a map
SW : H2(X; Z) → Z.

c_{1}(E)=e

\mathrm{S W}:H^{2}(X;\mathbb{Z})\to\mathbb{Z}.

√
∞ ∞ −1
If we write ψ = r(α,β) with α ∈ C (E) and β ∈ C (K E), write
+
A = A0 + 2a, and choose µ = rω − iF, then the Seiberg-Witten equations
A0
are
∗
∂ α = −∂ β,

\psi\;=\;\sqrt{r}(\alpha,\beta)

\alpha\;\in\;C^{\infty}(E

\beta\,\in\,C^{\infty}(K^{-1}E)

A=A_{0}+2a

\mu=r\omega-i F_{A_{0}}^{+}

\begin{array}{l}{{\displaystyle\overline{{\partial}}_{a}\alpha=-\overline{{\partial}}_{a}^{*}\beta,}}\\ {{\displaystyle F_{a}^{+}=\frac{-i r}{2}(1-|\alpha|^{2}+|\beta|^{2})\omega-r(\alpha\overline{{\beta}}-\overline{{\alpha}}\beta).}}\end{array}

(5.1)

We showed that any solution of these equations must satisfy the estimates
∫ (())

\int\left(\left(1-\frac{2z}{r}\right)|\nabla_{a}\alpha|^{2}+r(1-|\alpha|^{2})^{2}\right)\leq2\pi[\omega]\cdot e,

(5.2)

\int\left(\frac{1}{2}|\nabla_{a}^{*}\beta|^{2}+\frac{r}{2}|\beta|^{4}+\frac{r}{4}|\beta|^{2}\right)\leq\frac{z}{r}\int|\nabla_{a}\alpha|^{2}.

(5.3)

Taking r > 2z, we see from (5.2) that if [ω] · e < 0 then there is no solution,
and if [ω] · e = 0 then e = 0 and there is a unique solution. We conclude
that SW(e) = 0 for [ω] · e < 0, and SW(0) = ±1. (Also SW(e) = SW(c − e)
where c = c1(K).)

r>2z.

[\omega]\cdot e<0

[\omega]\cdot e\,=\,0

e=0

\mathrm{S W}(e)=0

[\omega]\cdot e<0

{\mathrm{l s o~S W}}(e)=\mathrm{S W}(c-e)

Fix e with [ω] · e > 0. Suppose SW(e) 6= 0. Then for every r the equations
(5.1) must have a solution. Let’s think about what the estimates (5.2), (5.3)
say when r is large.
• By (5.2), |α| wants to equal 1 as much as possible. (But it can’t equal

5.2 Motivation

c=c_{1}(K).)

\mathrm{c a n^{\prime}t}

∗
∗
• By the Dirac equation, |∂aα| = |∂aβ| = |∇aβ|, which wants to be
considerably smaller than |∇aα| by (5.3).

|\beta|

\big|\overline{{\partial}}_{a}\alpha\big|\,=\,\big|\overline{{\partial}}_{a}^{*}\beta\big|\,=\,|\nabla_{a}^{*}\beta|,

|\nabla_{a}^{*}\beta|

|\nabla_{a}\alpha|

---

This last remark suggests that the zero set of α is close to a pseudoholomorphic curve. The zero set of α is necessarily Poincar´e dual to e = c1(E),
so this suggests that there is some relation between SW(e) and pseudoholomorphic curves Poincar´e dual to e. Notice also that the formal dimension of
the space of (unparametrized) pseudoholomorphic curves Poincar´e dual to e
is (by Riemann-Roch)
2d = e · e − c · e,

\alpha

e=c_{1}(E)

2d=e\cdot e-c\cdot e,

which is the same as the dimension of the Seiberg-Witten moduli space.

5.3 Seiberg-Witten and pseudoholomorphic curves

A nonzero Seiberg-Witten invariant does indeed lead to the existence of a
pseudoholomorphic curve, as follows.

C
Theorem 5.1 [16, 17] Fix a Spin structure e. Given a sequence rn→∞
and (an, (αn,βn)) satisfying the equations (5.1) for r = rn, then after taking
an appropriate subsequence, there is a compact, complex curve C and a J -
holomorphic map f : C → X such that:

r_{n}\to\infty

\mathrm{S{i i n}^{c}}

(a_{n},(\alpha_{n},\beta_{n}))

r=r_{n}

f:C\rightarrow X

• f∗[C] is the Poincar´e dual of e in H2(X; Z).
{

H_{2}(X;\mathbb{Z})

f_{*}[C]

\textstyle\bullet\;\operatorname*{l i m}_{n\to\infty}\left\{\operatorname*{s u p}_{x\in C}\operatorname{d i s t}(x,\alpha_{n}^{-1}(0))+\operatorname*{s u p}_{x\in\alpha_{n}^{-1}(0)}\operatorname{d i s t}(x,f(C))\right\}=0.

−1
• If G ⊂ X is a closed set and αn(0)∩G 6= 0 for all n, then f (C)∩G 6= 0.

I f\!G\subset X

\alpha_{n}^{-1}(0)\cap G\neq0

f(C)\cap G\neq0

Note that C is not necessarily connected, and the map f is not necessarily
an embedding. But it is worth noting that if C is connected and f is an
embedding, then the genus g of C is given by the adjunction formula

Theorem 5.1 has a number of applications to the topology of symplectic
4-manifolds. For example, we showed in the last lecture that SW(c) = ±1,
so Theorem 5.1 implies that there exists a pseudoholomorphic map f : C →
X with f∗[C] Poincar´e dual to c = c1(K). One can use the Sard-Smale
theorem together with the adjunction formula to show that if J is generic,
then f : C → X is an embedding except that some components might be
multiply covered tori with self-intersection number zero. From this one can
further deduce that if c · c < 0 then some component of C is an embedded
pseudoholomorphic sphere with self-intersection number −1. So we get:

f:C\rightarrow

c\,=\,c_{1}(K)

f_{*}[C]

X

2g-2=e\cdot e+c\cdot e.

c\cdot c<0

f:C\to\,X

---

Corollary 5.2 Let X be a closed connected symplectic 4-manifold with b2+>
2
1 and c1(K) < 0. Then there exists an embedded pseudoholomorphic sphere
in X with self-intersection number −1, and hence X = Y #CP2 where Y is
symplectic.

b_{+}^{2}>

\ _11K K)^{2}<0.

X=Y\#\overline{{\mathbb{C}P^{2}}}

We can go beyond Theorem 5.1 to show that the Seiberg-Witten invariant
SW(e) is equal to a suitable count of pseudoholomorphic curves Poincar´e dual
to e. This count is given by a “Gromov invariant” Gr : H2(X; Z) → Z, which
we will define in the next section.

{{}^{\ }}{{_{{}{\ G}}}}{{}^{\ }}

{operatorname{G r}}:H^{2}(X;\mathbb{Z})\to\mathbb{Z}

Theorem 5.3 [16, 19] If b2+> 1, then SW = Gr : H2(X; Z) → Z.

I!,it f\,b_{+}^{2}>1

\mathrm{S W}=\mathrm{G r}:H^{2}(X;\mathbb{Z})\to\mathbb{Z}

5.4 Definition of the Gromov invariant

We want to count unparametrized, possibly disconnected, pseudoholomorphic curves Poincar´e dual to e. We will do this in a fairly standard way,
except that we allow tori to be multiply covered and count the multiple covers in a subtle way. The results in this section are discussed in greater detail
in [18].

Definition 5.4 Given e ∈ H2(X; Z), let Hedenote the set of finite sets
h = {(Ci,mi)} such that:

e\,\in\,H^{2}(X;Z)

h=\{(C_{i},m_{i})\}

\mathcal{H}_{e}

X

• Ciis an embedded, connected, pseudoholomorphic submanifold of X,
and if ei∈ H2(X; Z) is the Poincar´e dual of [Ci], then the formal
dimension
2d = e · e − c · e ≥ 0.

C_{i}

e_{i}\;\in\;H^{2}(X;\mathbb{Z})

[C_{i}]

2d_{i}=e_{i}\cdot e_{i}-c\cdot e_{i}\geq0.

• Ci∩ Cj= ∅ for i 6= j.

1
• If d = (e·e−c·e) > 0, fix a set Ω ⊂ X of d points, and require Ω = ∪iΩi
2∑
where Ωicontains dipoints and Ωi⊂ C. (Notice that d = di.)

i\neq j

\begin{array}{r}{d\!=\frac{1}{2}(e{\cdot}e{-}c{\cdot}e{\bigr)}>0}\end{array}

∑
• miei= e.
i

\mathrm{r e}\,\Omega=\cup_{i}\

\textstyle{\sum_{i}m_{i}e_{i}=e.}

C_{i}

The following theorem is the result of arguments due to Ruan, McDuff-
Salamon, Ye, Parker-Wolfson and Taubes.

d_{i}

\mathrm{Y e},

---

Theorem 5.5 If J is generic, then Heis a finite set. Furthermore, for each
i, the pair (Ci, Ωi) is (strongly) nondegenerate (in a technical sense which is
specified below).

\mathcal{H}_{e}

(C_{i},\Omega_{i})

Given e ∈ H2(X; Z), we define Gr(e) ∈ Z as follows. If d < 0, we set
Gr(e) = 0. We set Gr(0) = 1. If d ≥ 0, we choose a generic J and define
∑ ∏

e\,\in\,H^{2}(X;\mathbb{Z})

\operatorname{G r}(e)\,\in\,\mathbb{Z}

d<0

\ \mathrm{G r}(e)=0

\operatorname{G r}(0)=1

d\geq0

\operatorname{G r}(e)=\sum_{h\in\mathcal{H}_{e}}\prod_{i}r(C_{i},m_{i}).

Here r(Ci,mi) is an integer which we will now describe.
For this purpose, we must digress momentarily to consider deformations

r(\mathcal{C}_{i},m_{i})
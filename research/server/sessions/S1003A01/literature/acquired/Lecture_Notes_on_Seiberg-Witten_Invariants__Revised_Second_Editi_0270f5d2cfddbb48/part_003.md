---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Lecture Notes on Seiberg-Witten Invariants (Revised Second Edition)]

If $M$ is not a spin manifold, we can still construct bundles $W \\otimes L$
for various choices of line bundles $L^2$. A Spin(4)$^c$-connection on $W \\otimes L$
determines a connection on the Clifford algebra bundle End($W$) and also
on the determinant line bundle $N^2(W\_a \\otimes L) = L^2$. When we denote the
connection on $W \\otimes L$ by $d\_A$, we will denote the induced connection on $L^2$
by $d\_{A\_2}$.

**Theorem 2.** Suppose that $M$ is a four-dimensional oriented Riemannian
manifold with a spin$^c$ structure which has determinant line bundle $L^2$.
Given a connection $d\_{A\_2}$ on $L^2$, there is a unique Spin(4)$^c$-connection on $W \\otimes L$
which induces the Levi-Civita connection on End($W$) and the connection
$d\_{A\_2}$ on $L^2$.

The proof is similar to that of Theorem 1. The curvature of this connection
is still given by (2.12), in agreement with the case of spin manifolds.

2.6 The Dirac operator

Let $M$ be a four-dimensional Riemannian manifold with a spin$^c$ structure
and a Spin(4)$^c$-connection $d\_A$ on the spin bundle $W \\otimes L$.

**Definition.** The Dirac operator $D\_A : \\Gamma(W \\otimes L) \\rightarrow \\Gamma(W \\otimes L)$ with coefficients in the line bundle $L$ is defined by

$$D\_A(\\psi) = \\sum\_{i=1}^{4} e\_i \\cdot d\_A \\psi(e\_i) = \\sum\_{i=1}^{4} e\_i \\cdot \\nabla\_{e\_i}^A \\psi.$$

(2.13)

In the case where $M$ is four-dimensional Euclidean space with the global
Euclidean coordinates $(x\_1, x\_2, x\_3, x\_4)$ the bundle $W$ is trivial-$W = M \\times \\mathbb{C}^4$.
If, in addition, $L$ is the trivial line bundle, the Dirac operator is just

$$D\_A \\psi = \\sum\_{i=1}^{4} e\_i \\frac{\\partial \\psi}{\\partial x\_i},$$ the $e\_i$'s being constant matrices such that

$$e\_i \\cdot e\_j + e\_j \\cdot e\_i = -2\\delta\_{ij} = \\begin{cases} -2 & \\text{for } i=j, \ 0 & \\text{for } i \\neq j. \\end{cases}$$

Thus we find that

$$D\_A \\circ D\_A(\\psi) = -\\sum\_{i=1}^{4} \\frac{\\partial^2 \\psi}{\\partial x\_i^2}.$$

In this case, the Dirac operator is (up to sign) a square root of the usual
Encidean Laplacian.

The notion of Dirac operator with coefficients in a line bundle can be extended further to coefficients in a general vector bundle. This is a powerful
extension which includes many of the familiar first order elliptic operators
of differential geometry.

Indeed, if $M$ has a spin structure, and $E$ is a complex vector bundle
over $M$ with Hermitian metric and unitary connection, we have an induced
Hermitian metric and a unitary connection on $W \\otimes E$. If $M$ has only a
spin$^c$ structure with spin bundle $W \\otimes L$, a Hermitian metric and unitary
connection in a complex vector bundle $E \\otimes L^{-1}$ will induce a Hermitian
metric and unitary structure in $W \\otimes E$. In either case we can construct a
Dirac operator $D\_A : \\Gamma(W \\otimes E) \\rightarrow \\Gamma(W \\otimes E)$ with coefficients in $E$ by a
straightforward extension of (2.13):

$$D\_A(\\psi \\otimes \\sigma) = \\sum\_{i=1}^{4} e\_i \\cdot d\_A \\psi(e\_i \\otimes \\sigma),$$

in which $d\_A$ now denotes the connection on $W \\otimes E$.

For example, if we take the bundle of coefficient $E$ to be $W$ itself, we
obtain in this way a familiar operator from Hodge theory:

**Proposition.** The Dirac operator with coefficients in $W$ is

$$D\_W = d + \\delta : \\sum\_{k=0}^{4} \\Lambda^k TM \\otimes \\mathbb{C} \\rightarrow \\sum\_{k=0}^{4} \\Lambda^k TM \\otimes \\mathbb{C},$$

Sketch of proof: First one shows that if $\\nabla$ denotes the Levi-Civita connection on the exterior algebra $\\sum\_{k=0}^{4} \\Lambda^k TM$, then the exterior derivative $d$ is
given by the formula

$$d\\omega = \\sum\_{i=1}^{4} e\_i \\wedge \\nabla\_e \\omega,$$

* * *

2.6. THE DIRAC OPERATOR

while the codifferential $\\delta$ is given by

$$\\delta \\omega = -\\sum\_{i=1}^{4} i(e\_j) \\nabla\_{e\_i} \\omega,$$

where $i(e\_j)$ denotes the interior product. The claimed formula can then be derived from (2.6).

The main result of this section, Weitzenböck's formula, gives a simple relationship between a Dirac operator and the "vector bundle Laplacian" $\\Delta^A : \\Gamma(W \\otimes E) \\rightarrow \\Gamma(W \\otimes E)$ defined by the formula

$$\\Delta^A \\psi = -\\sum\_{i=1}^{4} \[\\nabla\_{e\_i}^A \\circ \\nabla\_{e\_j}^A \\psi - \\nabla\_{\\nabla\_{e\_i} e\_j}^A \\psi\],$$

(2.14)

where $(e\_1, e\_2, e\_3, e\_4)$ is a moving orthonormal frame. (The term $\\nabla\_{\\nabla\_{e\_i} e\_j}^A \\psi$ is needed to make $\\Delta^A \\psi$ independent of the choice of frame.)

Theorem (Weitzenböck's formula). The square of the Dirac operator with coefficients in a line bundle bundle $L$ is related to the Laplace operator $\\Delta^A$ by the formula

$$D\_A^A \\psi = \\Delta^A \\psi + \\frac{s}{4} \\psi - \\sum\_{i<j} F\_A(e\_i, e\_j)(iu\_i \\cdot e\_j \\cdot \\psi).$$

(2.15)

Here $s$ is the scalar curvature of $M$ and $F\_A$ is the curvature of the connection in $L$.

Proof: Choose a moving orthonormal frame on a neighborhood of $p$ in $M$ so that $\\nabla\_{e\_i} e\_j(p) = 0$. (Recall that the Spin(4)$^c$-connection $\\nabla^A$ acts as the Levi-Civita connection $\\nabla$ on vector fields.) Then at $p$,

$$D\_A^A \\psi = \\left(\\sum\_{i=1}^{4} e\_i \\nabla\_{e\_i}^A\\right)\\left(\\sum\_{j=1}^{4} e\_j \\nabla\_{e\_j}^A\\right) \\psi = \\sum\_{i,j=1}^{4} e\_i e\_j \\nabla\_{e\_i}^A \\nabla\_{e\_j}^A \\psi$$

$$= -\\sum\_{i=1}^{4} \\nabla\_{e\_i}^A \\nabla\_{e\_j}^A \\psi + \\frac{1}{2} \\sum\_{i,j=1}^{4} e\_i e\_j \[\\nabla\_{e\_i}^A \\nabla\_{e\_j}^A - \\nabla\_{e\_j}^A \\nabla\_{e\_i}^A\] \\psi$$

$$= \\Delta^A \\psi + \\frac{1}{2} \\sum\_{i,j=1}^{4} e\_i e\_j (d\_A^A \\psi)(e\_i, e\_j) = \\Delta^A \\psi + \\frac{1}{2} \\sum\_{i,j=1}^{4} e\_i e\_j \\Omega\_A(e\_i, e\_j) \\cdot \\psi,$$ where $\\Omega\_{A}$ is the curvature of the Spin(4)$^{c}$-connection. Substituting (2.12) into this expression and utilizing (2.11) yields

$$D\_{A}^{2}\\psi = \\Delta^{A}\\psi - \\frac{1}{2} \\sum\_{i,j=1}^{4} F\_{A}(e\_{i}, e\_{j}) i e\_{i} \\cdot e\_{j} \\psi - \\frac{1}{8} \\sum\_{i,j,k,l=1}^{4} \\Omega\_{kl}(e\_{i}, e\_{j}) e\_{i} \\cdot e\_{j} \\cdot e\_{k} \\cdot e\_{l} \\psi$$
$$= \\Delta^{A}\\psi - \\sum\_{i<j} F\_{A}(e\_{i}, e\_{j}) i e\_{i} \\cdot e\_{j} \\psi + \\frac{s}{4}\\psi,

which proves the theorem.

In addition to being almost the square root of a Laplacian, the Dirac operator has another key property—self-adjointness:

**Proposition. The Dirac operator is "formally self-adjoint":**

$$\\int\_{M} \\langle D\_{A}(\\psi), \\eta\\rangle dV = \\int\_{M} \\langle \\psi, D\_{A}(\\eta)\\rangle dV$$

(2.16)

Proof: (Compare \[24\], page 114.) As in the preceding proof, we choose a moving orthonormal frame on a neighborhood of $p$ in $M$ so that $\\nabla\_{e\_i} e\_j(p) = 0$. Then

$$\\langle D\_{A}(\\psi), \\eta\\rangle(p) = \\sum\_{i=1}^{4} \\langle e\_{i} \\cdot \\nabla\_{e\_i}^{A}\\psi, \\eta\\rangle(p) = -\\sum\_{i=1}^{4} \\langle \\nabla\_{e\_i}^{A}\\psi, e\_{i} \\cdot \\eta\\rangle(p)$$
$$= -\\sum\_{i=1}^{4} \\left\[ e\_{i} \\langle \\psi, e\_{i} \\cdot \\eta\\rangle(p) - \\langle \\psi, \\nabla\_{e\_i}^{A}(e\_{i} \\cdot \\eta)\\rangle(p) \\right\]$$
$$= -\\sum\_{i=1}^{4} e\_{i} \\langle \\psi, e\_{i} \\cdot \\eta\\rangle(p) + \\langle \\psi, D\_{A}(\\eta)\\rangle(p),

because $e\_{i}$ is skew-Hermitian and $\\nabla^{A}$ is a unitary connection. If we define a one-form $b$ on $M$ by $\\langle b, e\_{i}\\rangle = \\langle \\psi, e\_{i} \\cdot \\eta\\rangle$, we can reexpress the result of this calculation as

$$\\langle D\_{A}(\\psi), \\eta\\rangle(p) - \\langle \\psi, D\_{A}(\\eta)\\rangle(p) = \\delta b.$$

(2.17)

Integration over $M$ now yields equation (2.16).

It follows from (2.10) that the vector bundle Laplacian $\\Delta^{A}$ is also formally self-adjoint; one could prove this via the integral formula

$$\\int\_{M} \\langle \\Delta^{A}\\psi, \\psi\\rangle dV = \\int\_{M} \|\\nabla^{A}\\psi\|^{2}dV.$$

(2.18)

* * *

2.7 THE ATIYAH-SINGER INDEX THEOREM

2.7 The Atiyah-Singer Index Theorem

In many respects, the simplest Dirac operator with coefficients is the operator $d + \\delta$ from Hodge theory, whose square is the Hodge Laplacian
$\\Delta = d\\delta + \\delta d$. Since

$(d + \\delta)\\omega = 0 \\iff d\\omega = 0$ and $\\delta\\omega = 0 \\iff \\Delta\\omega = 0,$

we see that the kernel of $d + \\delta$ is the finite-dimensional space of harmonic
forms. We can set

$$\\Omega^{+} = \\Omega^{0}(M) \\oplus \\Omega^{2}(M) \\oplus \\Omega^{4}(M), \\quad \\Omega^{-} = \\Omega^{1}(M) \\oplus \\Omega^{3}(M)$$

and divide the operator $d + \\delta$ into two pieces,

$$(d + \\delta)^{+}: \\Omega^{+} \\rightarrow \\Omega^{-}, \\quad (d + \\delta)^{-}: \\Omega^{-} \\rightarrow \\Omega^{+}.$$

we define the index of $(d + \\delta)^{+}$ to be

index of $(d + \\delta)^{+} = \\dim(\\text{Ker}(d + \\delta)^{+}) - \\dim(\\text{Ker}(d + \\delta)^{-}).$

But

$$\\text{Ker}((d + \\delta)^{+}) = \\mathcal{H}^{0}(M) \\oplus \\mathcal{H}^{2}(M) \\oplus \\mathcal{H}^{4}(M),$$

$$\\text{Ker}((d + \\delta)^{-}) = \\mathcal{H}^{1}(M) \\oplus \\mathcal{H}^{3}(M),$$

so

index of $(d + \\delta)^{+} = b\_{0} + b\_{2} + b\_{4} - (b\_{1} + b\_{3}) = \\chi(M),$

the Euler characteristic of $M$.

In a similar spirit, the Atiyah-Singer Index Theorem gives a formula for
the index of any first order elliptic linear differential operator in terms of
topological data. Of most importance to us is the Dirac operator $D\_{A}$ with
coefficients in a line bundle.

First note that the Dirac operator $D\_{A}$ divides into two pieces,

$$D\_{A}^{+}: \\Gamma(W\_{+} \\otimes L) \\rightarrow \\Gamma(W\_{-} \\otimes L), \\quad D\_{A}^{-}: \\Gamma(W\_{-} \\otimes L) \\rightarrow \\Gamma(W\_{+} \\otimes L),$$

which are formal adjoints of each other by (2.16 ). Just as in Hodge theory,
the theory of elliptic operators implies that the kernels of the operators $D\_{A}^{+}$
and $D\_{A}^{-}$ are finite-dimensional complex vector spaces. We define the index
of $D\_{A}^{+}$ to be

index of $D\_{A}^{+} = \\dim(\\text{Ker}(D\_{A}^{+})) - \\dim(\\text{Ker}(D\_{A}^{-})).$$

* * *

70 CHAPTER 2. SPIN GEOMETRY ON FOUR-MANIFOLDS

Atiyah-Singer Index Theorem (for the Dirac operator with coef- cients in a line bundle). If DAis a Dirac operator with coecients in a line bundle L on a compact oriented four-manifold M, then Z +1 12 index of DA= (M) + c1(L); (2.19) 8 2M

where (M) = b+b, the signature of M.

This theorem is a consequence of a more general theorem to be stated later in this section. It has many striking applications. In particular, if we take L to be the trivial line bundle over a spin manifold, we can derive:

Rochlin’s Theorem. The signature of a compact oriented smooth spin manifold of dimension four satises the condition

(M) 0; mod 16:
Proof: If D + is the Dirac operator with coecients in the trivial line bundle,

(M)
index of D = : 8

This shows immediately that the signature of M is divisible by 8. But there are also endomorphisms J : W! W dened by Cliord multiplication on the right by the quaternion j. If is a harmonic section of W+, so is J (), a section which is perpendicular to. In fact, the kernel of D + is quaternionic, and we can construct an orthonormal basis of Ker(D + ) of the form 1 J (1);:::;k;J (k):

The same argument applies to Ker(D), so Ker(D + ) and Ker(D) are both even-dimensional over C. Thus the index of D + is divisible by two, and the signature of M is divisible by 16.

Another striking application of the Atiyah-Singer Index Theorem is to the problem of relating curvature to topology of Riemannian manifolds:

Theorem of Lichnerowicz. If M is a compact oriented spin manifold of dimension four with a Riemannian metric of positive scalar curvature, then the signature of M is zero.

Proof: We use the Weitzenbock formula for the Dirac operator D in the case of the trivial line bundle with the trivial connection. If is a harmonic

* * *

2.7. THE ATIYAH-SINGER INDEX THEOREM 71 spinor eld (D = 0), then
Z h i 2s2 0 = jrAj + j j dv; M4

and hence positive scalar curvature implies that = 0. Thus the kernel of D + and are both zero, which implies that

(M)

- = (index of D) = 0: 8

This theorem shows that most compact oriented four-manifolds with spin structure do not admit Riemannian metrics with positive scalar curvature.

Coecients in a general complex vector bundle: The Atiyah-Singer Index Theorem with coecients in a line bundle is a special case of a more general theorem, which gives the index of a Dirac operator

DA + : (W+E) ! (W E)

with coecients in a general complex vector bundle or virtual complex vector bundle E. To state the more general theorem, we need the Chern character discussed in x1.5 and the A^-polynomial in the Pontrjagin classes. It follows from our earlier discussion of the Chern character and (1.16) that

12 ch(E) = dim E + c1(E) + (c1(E)) c2(E) +; (2.20) 2

the dots denoting terms of degree > 4. We can apply these formulae to the quaternionic line bundles W+and W which have vanishing rst Chern classes: ch(W+) = 2 c2(W+); ch(W) = 2 c2(W):

Since W+is isomorphic to its conjugate or dual bundle,

TM C = Hom(W+;W) = W+W;

## and hence

ch(TM C) = ch(W+)ch(W) = 4 2c2(W+) 2c2(W):

Thus according to the denition of Pontrjagin class,

p1(TM) = c2(TM C) = 2c2(W+) 2c2(W) = 2c2(W): (2.21)

* * *

72 CHAPTER 2. SPIN GEOMETRY ON FOUR-MANIFOLDS

It follows from the product formula for the Chern character that if E is any SU (2)-bundle, then

(2 c2(E) +) 2 = 4 c2(E E) +;

which implies that 1 c2(E) = c2(E E): 4 If M is not spin, we can use this formula to dene c2(W+) and c2(W), since the vector bundles W+W+and W W always exist as bona de vector bundles. Similarly, we set c1(L) = (1=2)c1(L2), when L2 exists as a complex line bundle, but L does not. Thus we can use the product formula for Chern characters to dene c1(E) and c2(E) when E is only a virtual vector bundle. The A^-polynomial is dened by a power series

A^(TM) = 11(TM) + 2 H (M; R); 1 p 24

where p1 is the rst Pontrjagin class and the dots indicate terms in higher order Pontrjagin classes, which once again will vanish on a manifold of dimension 4.

Atiyah-Singer Index Theorem (over four-manifolds). If DAis a Dirac operator with coecients in a virtual vector bundle E over a compact oriented four-manifold M, then

index of DA + = A^(TM)ch(E)\[M\] Z = \[ (1=24)(dim E)p1(TM) + (1=2)(c1(E)) 2 c2(E)\]: M

For the proof of this theorem, one of the monuments of twentieth century mathematics, we refer the reader to \[6\] or \[24\]. This theorem gives a formula for the indices of virtually all the geometrically interesting elliptic operators on a compact oriented four-manifold.

How does this theorem imply the Atiyah-Singer Theorem we previously stated for Dirac operators with coecients in line bundles? To answer this question, we need to consider rst the special case where E = W, so that

X4 W E = k TM C and DA= (d +): k=1

* * *

2.7. THE ATIYAH-SINGER INDEX THEOREM 73 In this case, Ker(DA) = Ker(d +) = f complex-valued harmonic forms g: This is the operator considered at the beginning of this section, but now we divide up the operator dierently\|this time we take
DA + : (W+W) ! (W W):

It is easiest to understand the new decomposition in the case where M is simply connected, so b1 = b3 = 0. In this case, the harmonic forms consist of the constant functions, constant multiples of the volume form ?1, and elements of H+ 2

(M) and H2 (M);
which are sections of W+W+and W W, respectively. Since 1 + ?1 and 1?1 are sections of W+W+and W W respectively, we see that

the index of DA + = b+b = (M);

the signature of M. With a little more work, one can show that this formula also holds in the case where b1 = b3 6= 0, and hence by the Atiyah-Singer Index Theorem and (2.21), Z

(M) = \[ (1=24)(dim W)p1(TM) c2(W)\] M Z Z = \[ (1=6)p1(TM) + (1=2)p1(TM)\] = (1=3)p1(TM): M M
We have sketched the proof of:

Hirzebruch Signature Theorem (for four-manifolds). The signature of a compact oriented smooth four-manifold M is given by the formula Z 1

(M) = p1(TM): 3M
The Signature Theorem allows us to eliminate the term containing p1(TM) in the general Atiyah-Singer Index Theorem, thereby obtaining (2.19) in the case of coecients in a line bundle. We conclude this chapter by deriving the characteristic class invariants for the bundles W L. From (2.21) we conclude that Z 1 3 c2(W+)\[M\] + c2(W)\[M\] = p1(TM) = (M): 2M2

* * *

74 CHAPTER 2. SPIN GEOMETRY ON FOUR-MANIFOLDS

On the other hand, we can take Dirac operators DW+and DWwith coef- cients in W+and W respectively, and verify that

the index of DW + + the index of DW + = 2b0 2b1 + b2 = (M);

the Euler characteristic of M. Hence by the Atiyah-Singer Theorem,

## c2(W+)\[M\] + c2(W)\[M\] = (M):

We can solve for the Chern classes of W+and W, obtaining

3 1 3 1 c2(W+)\[M\] = (M) (M); c2(W)\[M\] = (M) + (M): 4 2 4 2

By the classication theorem for quaternionic line bundles, these numbers completely determine the spinor bundles W+and W, when they exist. Applying the product formula for Chern characters to W+L gives

12 (2 c2(W+) +)(1 + c1(L) + (c1(L)) +) 2

12 = 2 + c1(W+L) + \[c1(W+L)\] c2(W+L) + : 2 Thus c1(W+L) = 2c1(L) = c1(L2)

and nally,

3 1 12 2 c2(W+L)\[M\] = (M) (M) + c1(L) \[M\]; (2.22) 4 2 4

3 1 12 2 c2(W L)\[M\] = (M) + (M) + c1(L) \[M\]: (2.23) 4 2 4

* * *

## Chapter 3

# Global analysis of the Seiberg-Witten equations

### 3.1 The Seiberg-Witten equations

As we have seen, the theory of linear partial dierential equations\|in particular, the Atiyah-Singer index theorem\|yields topological invariants which have striking geometric applications. We now investigate more re- ned invariants constructed with nonlinear partial dierential equations, invariants that are not available from the linear theory. Here is the procedure we might try to follow. Choose a nonlinear PDE. Show that its space of solutions is a compact nite-dimensional smooth manifold which lies in some ambient \\conguration space." The solution space will in general depend upon certain choices, such as the choice of a Riemannian metric, but in favorable cases the \\cobordism class" of the so- lution space may be independent of the choices. This cobordism class may then become a new topological invariant. Since it is dened in terms of a PDE (which requires a smooth structure), it may be possible for the invari- ant to distinguish between smooth structures on the underlying topological manifold associated to M. In broad outline, this is in fact the way Donaldson’s original instan- ton theory works, as described in \[12\]. The moduli space of anti-self-dual connections in an SU (2)-bundle over a compact oriented four-manifold is generically a smooth manifold. However, this moduli space is not usually compact, and much eort is expended towards nding a suitable compact- ication. Gromov’s theory of pseudoholomorphic curves \[26\] is a second case in which the above procedure can be carried through, with compactification once again providing difficulties. A body of techniques has been developed for studying these and related geometrical theories. Perhaps the Seiberg-Witten invariants, which we will proceed to describe, provide the simplest context for the working out of these techniques.

Let $(M, \\langle , \\rangle)$ be an oriented four-dimensional Riemannian manifold with a spin² structure and corresponding positive spinor bundle $W\_+ \\otimes L$. We seek pairs $(d\_{2A}, \\psi)$, where $d\_{2A}$ is a connection on the line bundle $L^2$ and $\\psi$ is a section of $W\_+ \\otimes L$ such that

$$D\_A^+ \\psi = 0, \\quad F\_A^+(e\_i, e\_j) = -\\frac{i}{2}(e\_i \\cdot e\_j \\cdot \\psi, \\psi), \\quad \\text{for } i < j.$$ (3.1)

Here $F\_A^+ = (1/2)F\_{2A}^+$ where $F\_{2A}^+$ is the self-dual part of the curvature of the connection $d\_{2A}$. In the expression $e\_i \\cdot e\_j \\cdot \\psi$, Clifford multiplication is understood.

We will sometimes write $(d\_{2A}, \\psi)$ instead of $(d\_{2A}, \\psi)$ and think of $d\_A$ as a connection in the line bundle $L$, a bundle which strictly speaking does not exist unless $M$ is spin. Often, we will simplify yet further, and write $(A, \\psi)$ instead of $(d\_A, \\psi)$.

If $J : W\_+ \\otimes L \\rightarrow W\_+ \\otimes L^{-1}$ is the conjugate-linear multiplication on the right by the quaternion $J$, then any solution $(d\_A, \\psi)$ for the Seiberg-Witten equations for $L$ yields a corresponding solution $(d\_{2A}, J \\otimes \\psi)$ for the Seiberg-Witten equations for $L^{-1}$.

Equations (3.1) are known as the Seiberg-Witten equations. It follows from (2.7) that they can also be written in the form

$$D\_A^+ \\psi = 0, \\quad F\_A^+ = \\sigma(\\psi),$$ (3.2)

where $\\sigma : W\_+ \\rightarrow \\Lambda^2 V$ is the standard quadratic map. We will also need the "perturbed" Seiberg-Witten equations,

$$D\_A^+ \\psi = 0, \\quad F\_A^+ = \\sigma(\\psi) + \\phi,$$ (3.3)

in which $\\phi$ is a prescribed self-dual two-form. Note that equations (3.2) and (3.3) fail to be linear only because of the presence of the term $\\sigma(\\psi)$, which is quadratic in $\\psi$. This nonlinearity is much milder than that encountered in the Yang-Mills equations from nonabelian gauge theory.

Just like the Yang-Mills equations, the Seiberg-Witten equations are related to a variational principle. We define a nonnegative real-valued functional $S$ on the space

$$\\mathcal{A} = {(A, \\psi) : A \\text{ is a unitary connection on } L, \\psi \\in \\Gamma(W\_+ \\otimes L)},$$

* * *

3.2. THE MODULI SPACE

by the formula

$$S(A, \\psi) = \\int\_{M} \\left\[ \|D\_A \\psi\|^2 + \|F\_A^+ - \\sigma(\\psi)\|^2 \\right\] dV,$$

(3.4)

where $dV$ denotes the volume element on $M$. Clearly the absolute minimum of this functional is assumed at solutions to (3.2) when these solutions exist.

We expand, using the fact that $D\_A$ is self-adjoint, to obtain

$$S(A, \\psi) = \\int\_{M} \\left\[ \|D\_A \\psi\|^2 + \|F\_A^+ - 2(F\_A^+, \\sigma(\\psi)) + \|\\sigma(\\psi)\|^2 \\right\] dV$$

$$= \\int\_{M} \\left\[ \|D\_A \\psi\|^2 + \|F\_A^+\|^2 + \\sum\_{i<j} F\_A^+(e\_i, e\_j)(ie, e\_j \\psi, \\psi) + \|\\sigma(\\psi)\|^2 \\right\] dV.$$

Hence we obtain

$$S(A, \\psi) = \\int\_{M} \\left\[ \\nabla^A \\psi\|^2 + \\frac{s}{4}\|\\psi\|^2 + \|F\_A^+\|^2 + \|\\sigma(\\psi)\|^2 \\right\] dV.$$

(3.5)

where in the last step we have used the Weitzenböck formula. If the scalar curvature $s$ is strictly positive, all terms in the last expression are nonnegative and thus there are no nonzero solution to the Seiberg-Witten equations in this case. Moreover, since

$$\|\\sigma(\\psi)\|^2 = \\frac{1}{2}\|\\psi\|^4 \\text{ and } \\left(\\frac{s}{4} + \|\\psi\|^2\\right)^2 \\geq 0,

if $(A, \\psi)$ is a solution to the Seiberg-Witten equations,

$$\\int\_{M} \|F\_A^+\|^2 dV \\leq \\int\_{M} \\left\[ -\\frac{s}{4}\|\\psi\|^2 - \\frac{1}{2}\|\\psi\|^4 \\right\] dV \\leq \\frac{1}{2} \\int\_{M} \\frac{s^2}{10} dV.$$

In the next few sections, we will study the properties of the space of solutions to the Seiberg-Witten equations. We will see that in the generic case, the moduli space of solutions to the perturbed Seiberg-Witten equations is a compact finite-dimensional manifold.

3.2 The moduli space

We choose a “base connection” $d\_{A\_0}$ in $L$ so that our configuration space becomes

$$A = {(d\_{A\_0} - ia, \\psi): a \\in \\Omega^1(M), \\psi \\in \\Gamma(W\_+ \\otimes L)}.$$

* * *

## 78 CHAPTER 3. GLOBAL ANALYSIS

As in x1.8, the group of gauge transformations,

G = Map(M;S1) = f maps g : M ! S1g

acts on A by

(g; (dA0ia; )) 7! (dA0ia + gd(g 1 );g ):

In the case where M is simply connected, each element g 2G has a global logarithm u, so we can write

g = e iu ; u : M ! R;

and the action of G on A simplies to

(g; (dA0ia; )) 7! (dA0i(a + du));e iu ):

As we saw in x1.8, G possesses a subgroup of \\based gauge transforma- tions," G0 = fg 2G : g(p0) = 1g;

p0 being a chosen basepoint in M. The importance of the group G0 is that it acts freely on A. Let Be = A=G0.

Proposition. If M is simply connected, each element of Be has a unique representative of the form

## (dA0ia; ); where a = 0:

Proof of existence: It suces to nd a function u : M! R such that (a + du) = 0. In other words, it suces to nd an element u 2 0

(M)
such that u = (du) = a; (3.7)

which is simply Poisson’s equation. To solve it, we use Hodge theory: The theorem of Stokes shows that Z Z 1 ^ ?(a) = d(?a) = 0; M M

so a lies in the orthogonal complement of the space H0(M) of constant functions on M, with respect to the L2 inner product ( ;). Since this is also the orthogonal complement to the range of by Hodge’s Theorem, there does indeed exist a solution u to (3.7).

* * *

3.2. THE MODULI SPACE

Proof of uniqueness: If
$(d\_{A0} - ia\_1, \\psi\_1), \\quad (d\_{A0} - ia\_2, \\psi\_2)$

are two elements of A which are equivalent under the action of $G\_0$ such that $b\_{A1}$ and $b\_{A2}$ are both zero, then since $da\_1 = da\_2$ and M is simply connected, there exists a map u : M → R such that $a\_1 - a\_2 = du$. Hence
$(a\_1 - a\_2, a\_1 - a\_2) = (du, a\_1 - a\_2) = (u, \\delta(a\_1 - a\_2)) = 0 \\Rightarrow a\_1 - a\_2 = 0.$

Thus when M is simply connected, the quotient space $\\tilde{B}$ is in one-to-one correspondence with a linear subspace of A:
$$\\tilde{B} \\cong {(d\_{A0} - ia, \\psi): a \\in \\Omega^1(M), \\psi \\in \\Gamma(W\_+ \\otimes L), \\delta a = 0}. \\tag{3.8}$$

We can think of this linear space as giving a global coordinate system on $\\tilde{B}$.

However, we actually want to divide out by the full gauge group, and now we encounter an essential difference between the Seiberg-Witten theory and abelian gauge theory—instead of acting trivially, the group U(1) of constant gauge transformations acts freely on $\\tilde{B}$ except at the points $(d\_{A0} - ia, 0)$. The quotient space $\\mathcal{B} = \\mathcal{A}/\\mathcal{G}$ by the full gauge group will have singularities at the "reducible" elements $(d\_{A0} - ia, 0)$. Sometimes, we can avoid dealing with the reducible elements by excising these singular points and setting
$$\\mathcal{A}^\* = {(d\_{A0} - ia, \\psi) \\in \\mathcal{A}: \\psi \\neq 0}, \\quad \\tilde{\\mathcal{B}}^\* = \\mathcal{A}^ _/G\_0, \\quad \\mathcal{B}^_ = \\mathcal{A}^\*/\\mathcal{G}.$$

We want to think of $\\mathcal{B}^\*$ as an infinite-dimensional manifold modeled on a Hilbert or Banach space, as described in \[23\]. To do this precisely, we need to complete our spaces of sections—just as in the older instanton theory—with respect to suitable Sobolev norms. We give only the basic definitions here and refer the reader to \[14\] or \[12\] for a more detailed treatment of "Sobolev completions."

If E is a smooth O(m)-or U(m)-bundle over a compact Riemannian manifold M with connection d\_A, we can use the Levi-Civita connection on TM to define connections (also denoted by d\_A) on the bundles $\\otimes^k T^ _M \\otimes E = \\text{Hom}(\\otimes^k TM, E)$. If $\\sigma \\in \\Gamma(E)$, we can define_
_$$d\_A^_\\sigma = (d\_A \\circ \\cdots \\circ d\_A)\\sigma \\in \\Gamma(\\text{Hom}(\\otimes^k TM, E)).$$

For p > 1, let
$$\|\\sigma\|\_{p,k} = \\left\[ \\int\_M \|\|\\sigma\|\|^p + \|d\_A\\sigma\|^p + \\cdots + \|d\_A^k\\sigma\|^p \|dV\| \\right\]^{(1/p)}.$$

* * *

It can be checked that this is a norm on $\\Gamma(E)$, and we let $L\_{k}^{p}(E)$ denote the completion of $\\Gamma(E)$ with respect to this norm. The choice of Riemannian metric, the fiber metric on $E$ or the connection $d\_{A}$ replaces the norms on $\\Gamma(E)$ by equivalent norms, and hence does not affect the resulting completions.

For all choices of $p$, $L\_{k}^{p}(E)$ is a Banach space, and it is a Hilbert space if $p = 2$. The spaces $L\_{k}^{p}(E)$ are called Sobolev spaces.

Here are some key results from functional analysis (which are described in more detail in the appendix to Donaldson and Kronheimer \[12\]): In the case where the base manifold has dimension four, the Sobolev Embedding Theorem states that if $k - (4/p) > l$ there is a continuous embedding

$$L\_{k}^{p}(E) \\rightarrow C^{l}(E),$$

the space of $C^{l}$ sections of $E$. Rollich's Theorem states that the inclusion

$$L\_{k+1}^{p}(E) \\rightarrow L\_{k}^{p}(E)$$

is compact for all $p$ and $k$, meaning that a sequence $\\sigma\_{i}$ which is bounded in $L\_{k+1}^{p}$ possesses a subsequence which converges in $L\_{k}^{p}$. When $k - (4/p) > 0$, the multiplication theorem state that there are continuous multiplications

$$L\_{k}^{p}(E) \\times L\_{k}^{p}(F) \\rightarrow L\_{k}^{p}(E \\otimes F).$$

Thus for $p$ and $k$ in this range and for $E$ the trivial line bundle, $L\_{k}^{p}(E)$ is a Banach algebra.

With these preparations out of the way, we can set

$$\\tilde{\\mathcal{B}} _{k}^{p} = \\left{(d_{\\mathrm{A} _{0}} - ia, \\psi) : a \\in L_{k}^{p}(T^{\*}M), \\psi \\in L\_{k}^{p}(W\_{+} \\otimes L), \\delta a = 0\\right}.$$

Similarly, we can define $\\mathcal{A}\_{k}^{p}$,

$$\\mathcal{G} _{k+1}^{p} = L_{k}^{p}(\\text{End}(E)) \\cap C^{0}(M, S^{1}),$$

when $k + 1 - (4/p) > 0$, and so forth. It can also be shown that $\\mathcal{G} _{k+1}^{p}$ is an infinite-dimensional Lie group which acts smoothly on $\\mathcal{A}_{k}^{p}$, although these last facts will not be needed in our subsequent arguments.

Henceforth, when we write spaces such as $\\mathcal{A}, \\tilde{\\mathcal{B}}$, or $\\mathcal{G}$, appropriate Sobolev completions will be understood. We will only include the indices $p$ and $k$ when explicit values are needed for clarity.

After Sobolev completion, $\\tilde{\\mathcal{B}}^{ _}$ can be regarded as an $S^{1}$ bundle over the infinite-dimensional manifold $\\mathcal{B}^{_}$. Just as $\\pi\_{n}(S^{n}) = 0$ for $k < n$, the $k$-th homotopy group of an infinite-dimensional sphere must vanish for all $k$. Thus $\\mathcal{A}^{\*}$, which is homotopy equivalent to an infinite-dimensional linear

* * *

3.3. COMPACTNESS OF THE MODULI SPACE 81 space minus a point, must have the homotopy groups of a point. If M is simply connected, G0 is also contractible, and hence Be has the homotopy groups of a point. It follows from the exact homotopy sequence of the ber bundle
S1! Be!B (3.9)

that B is a K(Z; 2), just like P1C. In fact, all K(Z; 2)’s are homotopy equivalent, so B is homotopy equivalent to P1C. We can dene a complex line bundle E over B which pulls back to the universal bundle under the homotopy equivalence P1C !B . Then Be can be identied with the bundleof unit-length vectors in E.

Denition. The monopole moduli space is

MM;L= f\[A; \] 2B : (A; ) satises (3.2)g;

or more generally, if is a given self dual two-form,

MM;L;= f\[A; \] 2B : (A; ) satises (3.3)g:

Using (3.8), we see that the latter space is the quotient of

M f M;L;= f(dA0ia; ) 2 1

(M) (W+L) :
a = 0 and (dA0ia; ) satises (3.3) g

## by the action of S1.

We will often simplify notation, and write ML;or M for MM;L;, for example. Our next goal is to show that M is a nite-dimensional manifold, a submanifold of B, except for possible singularities at points where = 0.

# 3.3 Compactness of the moduli space

The rst remarkable property of the moduli spaces M or M is that they are compact, as we now show following the treatment in Kronheimer and Mrowka \[22\]:

Lemma. If (A; ) is a solution to the Seiberg-Witten equations with not identically zero, and the maximum value of j j is assumed at a point p 2 M, then 2s(p) j j (p); 4 where s is the scalar curvature. Similarly, if (A, $ \\psi $) is a solution to the perturbed Seiberg-Witten equations (3.3), then

$$\|\\psi\|^2(p) \\leq -\\frac{s(p)}{4} + \\sqrt{2} \|\\phi(p)\|.$$

Proof: The restriction of the Hodge Laplacian to zero-forms or functions can be expressed as

$$\\Delta = -\\frac{1}{\\sqrt{g}} \\sum\_{i,j=1}^{4} \\frac{\\partial}{\\partial x\_i} \\left( g^{ij} \\frac{\\partial}{\\partial x\_j} \\right),$$

where the $ g\_{ij} $'s are the components of the metric with respect to coordinates $(x\_1, \\dots, x\_k)$ and $(g^j) = (g\_{ij})^{-1}$. Note that $\\Delta(f) \\geq 0$ at a local maximum of a function $f$, and hence since $p$ is a maximum for $\|\\psi\|^2$.

$$d(\|\\psi\|^2)(p) = 0, \\quad \\Delta(\|\\psi\|^2)(p) \\geq 0.$$

Since $ d\_A $ is a metric connection,

$$-\\langle d\_A \\psi, d\_A \\psi\\rangle(p) + \\langle \\Delta^A \\psi, \\psi\\rangle(p) \\geq 0 \\Rightarrow \\langle \\Delta^A \\psi, \\psi\\rangle(p) \\geq 0,$$

where $\\Delta^A$ is the vector bundle Laplacian defined by (2.14). It follows from the first of the Seiberg-Witten equations and the Weitzenböck formula (2.15) that

$$0 = D\_A^2 \\psi = \\Delta^A \\psi + \\frac{s}{4} \\psi - \\sum\_{i<j} F\_A^4(e\_i, e\_j)(ie\_i \\cdot e\_j \\cdot \\psi).$$

Take the inner product with $ \\psi $ to obtain

$$\\langle \\Delta^A \\psi, \\psi\\rangle + \\frac{s}{4} \|\\psi\|^2 + 2 \\langle F\_A^4, \\sigma(\\psi)\\rangle = 0.$$

It follows from the second of the Seiberg-Witten equations and the fact that $\\langle \\Delta^A \\psi, \\psi\\rangle(p) \\geq 0$ that

$$\\frac{s(p)}{4} \|\\psi(p)\|^2 + 2 \\langle \\sigma(\\psi) + \\phi, \\sigma(\\psi)\\rangle(p) \\leq 0.$$

Thus

$$\|\\psi(p)\|^4 = 2 \|\\sigma(\\psi)(p)\|^2 \\leq -\\frac{s(p)}{4} \|\\psi(p)\|^2 + 2 \|\\sigma(\\psi)(p)\| \|\\phi(p)\|,$$

and the desired result follows by dividing by $ \|\\psi(p)\|^2$.

* * *

3.3. COMPACTNESS OF THE MODULI SPACE 83 Thus the range of is contained in a compact subset of W+L. To show that the moduli space itself is compact, however, we need to use the Sobolev completions described in the preceding section, as well as the following key inequality from PDE theory: If D is a Dirac operator or a Dirac operator with coecients (such as d +), then

## k kp;k+1c\[kDkp;k+ k kp;k\]; (3.10)

where c is a constant. The k kp;kterm can be omitted in the case where D has trivial kernel. In the case where p = 2 inequality (3.10) is often used to prove Hodge’s Theorem. The general case is discussed in the Appendix to \[12\] and Appendix B to \[26\].

Compactness Theorem. If M is simply connected, then for every choice of self-dual two-form, the moduli space Mf of solutions to the perturbed Seiberg-Witten equations is compact.

Remark: Simple connectedness of M is not actually necessary, but makes the proof especially simple.

Proof: We choose a base connection A0, so that any unitary connection on L is of the form dA0ia, for some a 2 1

(M). We need to show that
any sequence \[dA0iai;i\] of solutions to the perturbed Seiberg-Witten equations possesses a convergent subsequence. Imposing the gauge condition a = 0 puts the perturbed Seiberg-Witten equations into the form ( DA0ia = 0; (da) + + FA + 0 = () +; a = 0;

or equivalently, ( DA0= ia ; (da) + = () + FA + 0 ; a = 0: On the left-hand side of this system appear the two Dirac operators DA0 and ( d + ), the second of these being the Dirac operator with coecients in W+described in x2.7. The Lemma implies thatiis bounded in C0 and hence in every L p . Since M is simply connected, the operator

d + : 1

(M) ! 0
(M) 2 +(M)
has trivial kernel. It therefore follows from (3.10) applied to the last two equations that aiis bounded in L p 1for all p. In particular, taking p > 4, we see that it is bounded in C0 by the Sobolev Embedding Theorem, and hence $a\_i \\psi\_i$ is bounded in $L^p$ for all $p$. Then it follows from (3.10) applied to the first equation that $\\psi\_i$ is bounded in $L^l\_1$ for all $p$. If $p > 4$, $L^l\_1$ is in Banach algebra range, so

$$a\_i, \\psi\_i \\text{ bounded in } L^p\_1 \\Rightarrow a\_i \\psi\_i, \\sigma(\\psi\_i) \\text{ bounded in } L^p\_1$$

$$\\Rightarrow a\_i, \\psi\_i \\text{ bounded in } L^p\_2.$$

Similarly,

$$a\_i, \\psi\_i \\text{ bounded in } L^p\_k \\Rightarrow a\_i \\psi\_i, \\sigma(\\psi\_i) \\text{ bounded in } L^p\_k$$

$$\\Rightarrow a\_i, \\psi\_i \\text{ bounded in } L^p\_{k+1}.$$

Thus we can "bootstrap" to conclude that $a\_i, \\psi\_i$ are bounded in $L^p\_k$ for all $k$. Then Rellich's Theorem produces a subsequence which converges in $L^p\_k$ for all $k$, and the sequence must converge in $C^l$ for all $l$ by the Sobolev Embedding Theorem. This proves compactness.

3.4 Transversality

The second remarkable property of the moduli space $\\mathcal{M}\_p$ is that for generic choice of $\\phi$ it is a smooth manifold, except possibly at reducible elements. To prove this, we need to use Smale's infinite-dimensional version of Sard's theorem \[35\].

A familiar method for constructing smooth submanifolds of a finite-dimensional smooth manifold $M^m$ goes like this: Suppose that $F : M^m \\rightarrow N^n$ be a smooth map which has $q$ as a regular value. Then $F^{-1}(q)$ is a smooth embedded submanifold of $M^m$ by the implicit function theorem, and its dimension is $m - n$. This is complemented by Sard's theorem, which states that almost all $q \\in N^n$ are regular values.

In order to apply this idea to nonlinear PDE's, we need to generalize to maps between manifolds modeled on infinite-dimensional Banach spaces. To do this we need the notion of Fredholm map. Suppose that $E\_1$ and $E\_2$ are reductive Banach spaces. A continuous linear map $T : E\_1 \\rightarrow E\_2$ is said to be Fredholm if

1. the kernel of $T$ is finite-dimensional,
2. the range of $T$ is closed, and
3. the range of $T$ has finite codimension in $E\_2$.

* * *

3.4. TRANSVERSALITY 85

The index of a Fredholm map $T$ is defined to be

$$\\dim(\\text{Ker}(T)) - \\text{codim}(\\text{T}(E\_1)) = \\dim(\\text{Ker}(T)) - \\dim(\\text{Ker}(T^\*))$$

where $T^\* : E\_A^2 \\rightarrow E\_A^1$ is the adjoint of $T$ defined by $T^\*(\\phi)(v) = \\phi(T(v))$. A key feature of Fredholm operators is that their index is invariant under perturbation; if a family depends continuously upon a parameter which ranges through a connected topological space, the index of the family must be constant.

For example, if $M$ is a compact four-manifold and

$$D\_A^+ : \\Gamma(W\_+ \\otimes L) \\rightarrow \\Gamma(W\_- \\otimes L)$$

is a Dirac operator with coefficients in a line bundle $L$, $D\_A^+$ extends to a continuous linear map

$$D\_A^+ : L\_{k+1}^p (W\_+ \\otimes L) \\rightarrow L\_k^p (W\_- \\otimes L),$$

for every choice of $p$ and $k \\geq 0$. This extension is a Fredholm map with adjoint $D\_A$ \[24\], Theorem 5.2, page 193 and its Fredholm index is twice the complex index defined before, which is calculated by the Atiyah-Singer Index Theorem.

Suppose now that $F : M\_1 \\rightarrow M\_2$ is a smooth nonlinear map from a Banach manifold $M\_1$ to a Banach manifold $M\_2$. We say that $F$ is a Fredholm map between Banach manifolds of index $k$ if its linearization at $p$,

$$dF(p) : T\_p M\_1 \\rightarrow T\_F(p) M\_2.$$

is a Fredholm map of index $k$ for every $p \\in M\_1$. Note that a smooth map $F : M\_1 \\rightarrow M\_2$ between finite-dimensional manifolds is automatically Fredholm of index $M\_2 \\rightarrow \\dim M\_2$.

A point $q \\in M\_2$ is said to be a regular value of $F$ if $dF(p)$ is surjective for every $p \\in F^{-1}(q)$; otherwise it is called a critical value. It follows from the implicit function theorem on Banach spaces (see \[23\]) that if $q \\in M\_2$ is a regular value, then $F^{-1}(q)$ is a smooth submanifold of $M\_1$ just as in the finite-dimensional case. Moreover, $F^{-1}(q)$ is finite-dimensional, its dimension being the Fredholm index of $F$.

Finally, a subset of the Banach manifold $M\_2$ is called residual if it is a countable intersection of open dense sets. Recall that the Baire Category Theorem states that a residual subset of a complete metric space is dense. It is customary to refer to an element of a residual subset of $M\_2$ as a generic element.

With these preparations out of the way, we can now state Smale's extension of Sard's theorem \[35\]:

* * *

Sard-Smale Theorem. If F : M₁ → M₂ is a Cᵃ Fredholm map between separable Banach manifolds and k > max(0, index of F), then the set of regular values of F is residual in M₂.

In other words, a generic element of M₂ is a regular value. In our applications, the separability assumption will automatically hold, since all of the manifolds modeled on the L²₄ spaces that we have constructed are separable. The idea behind the proof of the Sard-Smale Theorem is to reduce to the finite-dimensional version of Sard's theorem; we refer the reader to \[35\] for further details.

We will need one further theorem from the theory of elliptic PDE's, the Unique Continuation Theorem found in \[2\]. This theorem asserts that if $\\psi$ is a solution to the equation $D\_A^+ \\psi = 0$ on a connected manifold, then $\\psi$ cannot vanish on an open set without vanishing identically. This is analogous to a familiar property of holomorphic functions. (Indeed, the Dirac operator could be thought of as a generalization of the Cauchy-Riemann operator from two to four dimensions.)

Transversality Theorem 1. Let M be a compact simply connected smooth four-manifold with a spin²-structure. In the special case in which bₚ(M) = 0, we make the additional assumption that the index of the Dirac operator D'A associated to the spin²-structure is positive. Then for a generic choice of self-dual two-form $\\phi$, Mφ is an oriented smooth manifold, whose dimension is given by the formula

$$\\dim(\\widetilde{M} _\\phi) = 2(index of D\_A^+) - b_ +.$$

(3.11)

Proof: Define

$$F : \\widetilde{B} \\times \\Omega\_i^2(M) \\rightarrow \\Gamma(W\_{-} \\otimes L) \\times \\Omega\_i^2(M)$$

by

$$F(A, \\psi, \\phi) = (D\_A^+ \\psi, F\_A^+ - \\sigma(\\psi) - \\phi).$$

The differential of F at (A, $\\psi$, $\\phi)$ is

$$dF(A, \\psi, \\phi)(a, \\psi', \\phi') = (D\_A^+ \\psi' - ia \\cdot \\psi, (da)^+ - 2\\sigma(\\psi, \\psi') - \\phi'),$$

where

$$\\sigma(\\psi, \\psi') = 2i \\text{ Trace-free Hermitian part of } \\left( \\frac{\\psi\_1}{\\psi\_2} \\right) (\\bar{\\psi}\_1^+ \\bar{\\psi}\_2^).$$

We claim that if (A, $\\psi$, $\\phi)$ is a solution to F(A, $\\psi$, $\\phi) = 0 with $\\psi \\neq 0$, then dF(A, $\\psi$, $\\phi)$ is surjective. Indeed, by letting $\\phi'$ vary, we see that the

* * *

3.4. TRANSVERSALITY

image of $dF(A, \\psi, \\phi)$ is foliated by translates of the linear space ${0} \\oplus \\Omega\_+^2(M)$. Thus it suffices to show that the projection on the first component is surjective when we set $\\phi' = 0$. Suppose that $(\\sigma, 0)$ is an $L^2$ section of $(W\_- \\otimes L) \\oplus (\\Lambda^0 \\oplus \\Lambda\_+^2)$ which is $L^2$-perpendicular to

$$dF(A, \\psi, \\phi)(T\_{A\_\\psi}\\bar{\\Bracket}\\vec{B} \\times {0}).$$

By self-adjointness of the Dirac operator, we know that $D\_A^\\sigma = 0$, so $\\sigma$ is actually smooth, and if it is not identically zero, it is nonvanishing on an open dense set by the Unique Continuation Theorem. The Unique Continuation Theorem also implies that the set of points $U$ on which $\\psi \\neq 0$ is open and dense. On $U$, the linear map $a \\mapsto a \\circ \\psi$ is painterwise injective (because $a \\cdot a \\cdot \\psi = -\|a\|^2 \\psi$, and hence it is an isomorphism (since the fibers of $T^\*M$ and $W\_+ \\otimes L$ have the same dimension). Since $\\sigma$ is $L^2$-perpendicular to the image of $a \\mapsto a \\cdot \\psi$, it must vanish identically, and hence $dF(A, \\psi, \\phi)$ is surjective when $\\psi \\neq 0$, as claimed.

By the implicit function theorem

$$\\mathcal{N} = {(A, \\psi, \\phi) \\in \\bar{\\Bracket}\\vec{B} \\times \\Omega\_+^2(M): F(A, \\psi, \\phi) = 0, \\psi \\neq 0}$$

$$= {(A, \\psi, \\phi) \\in \\bar{\\Bracket}\\vec{B} \\times \\Omega\_+^2(M): D\_A^\\psi = 0, F\_A^+ = \\sigma(\\psi) + \\phi, \\psi \\neq 0}$$

is a submanifold of $\\bar{\\Bracket}\\vec{B} \\times \\Omega\_+^2(M)$ whose tangent space at the point $(A, \\psi, \\phi)$ is

$$T\_{\[A, \\psi, \\phi\]}\\mathcal{N} = {(a, \\psi', \\phi') : L(a, \\psi') = (0, 0, \\psi')},$$

where

$$L(a, \\psi') = (D\_A^\\psi' - ia \\cdot \\psi, \\delta a, (da)^+ - 2\\sigma(\\psi, \\psi')).$$

In this last formula, $L$ is an elliptic operator,

$$L: \\Gamma(W\_+ \\otimes L) \\oplus \\Omega^1(M) \\rightarrow \\Gamma(W\_- \\otimes L) \\oplus \\bar{\\Omega}^0(M) \\oplus \\Omega\_+^2(M),$$

the symbol $\\bar{\\Omega}^0(M)$ denoting the space of smooth functions on $M$ which integrate to zero.

We claim that the projection

$$\\pi: \\mathcal{N} \\rightarrow \\Omega\_+^2(M), \\quad \\text{defined by} \\quad \\pi(A, \\psi, \\phi) = \\phi,$$

is a Fredholm map. Indeed, the kernel of $d\\pi$ is immediately seen to be the kernel of $L$, while

(Image of $d\\pi$) = ${\\phi' \\in \\Omega\_+^2 : (0, 0, \\phi') = L(a, \\psi')$ for some $a, \\psi'}$

= (Image of $L$) $\\cap {0} \\oplus {0} \\oplus \\Omega\_+^2$.

* * *

## 88 CHAPTER 3. GLOBAL ANALYSIS

Since L is an elliptic operator, the image of d is closed and of nite codi- mension. To show that the cokernel of d has the same dimension as the cokernel of L, it suces to show that

((W L) e0(M) f0g) \ (Image of L) ? = f0g: (3.12)

But if (;u; 0) 2 (W L) e0(M) 2 +(M) is perpendicular to the image of L, then DA= 0, and (ia ;) = (a;u), for all a 2 1

(M). We can dene a one-form b on M by

## hb;ai = hia ; i:

and since DA + = 0 and DA= 0, it follows from (2.17) that b = 0. Thus

(b;b) = (ib ;) = 0) b = 0) hia ; i = 0;

for all a 2 1

(M). It follows that = 0 on a nonempty open subset of
M, and by the Unique Continuation Theorem once again, 0 and hence (a;u) = 0 for all a 2 1 . Thus u = 0 and (3.12) holds. Choose to be a regular value of. Then 1 () is a submanifold of N whose dimension is the index of L, which is one more than the index of

L0 = DA + d + ;

since we replaced 0

(M) by e0(M). The index we want is a real index, so
the index of DA + given by the Atiyah-Singer index must be doubled in the present calculation. We nd that

real index of L = 2(complex index of DA + ) b+

(M)2
= \+ c1(L)\[M\] b+: 4

Thus the moduli space Mf = 1 () is indeed a smooth submanifold of the required dimension, so long as we can arrange that 6= 0. If b+> 0, we can choose so that it does not lie within the ane subspace of codimension b+described in the Proposition from x1.9. In this case, there are never any solutions (A; ;) to the perturbed Seiberg- Witten equations with = 0, and the theorem is proven. In the case where b+= 0 we need a special argument to handle the possibility that = 0. For this, we dene a modied map

F0 : B e 2 +(M) ! (W L) 2 +(M)

* * *

3.4. TRANSVERSALITY 89 which omits the quadratic term,
F0(A; ;) = (DA + ;FA + ):

The above argument then provides a submanifold

N0 = f(A; ;) 2 B e 2 +(M) : DA + = 0;FA + = ; 6= 0g;

and once again : N0! 2 +(M) is a Fredholm map whose Fredholm index is the index of the map DA + ( d + ). Since b+= 0, the summand

d + : 1

(M) ! e0(M)
2 +(M)

and by hypothesis the Fredholm index of DA + is positive. For a given 2 2

(M), 1 () consists of the pairs (A; ) such that D

- = 0 and F + =. + A A By the Sard-Smale theorem, there is a residual set V of 2 2 +(M), for which DA + is surjective. We note that V must be an open set. Thus if b+= 0, dF (A; ;) is surjective when either 6= 0 or 2 V, and N e = f(A; ;) 2 B e2 +(M) : F (A; ;) = 0; 2 V g is a submanifold by the implicit function theorem. The above argument then shows that for generic 2 V, Mf = 1 () is a smooth submanifold of the required dimension, nishing the proof of the theorem when b+= 0.

Orientation of the moduli space: To nish the proof of Transversality Theorem 1, we need to show that the moduli space Mf is oriented. This requires some results from the theory of families of Fredholm operators (presented, for example, in the Appendix to \[3\] or in Chapter III, x7 of \[24\]). In particular, we need the notion of the determinant line bundle for a family of Fredholm operators, the operators depending upon a parameter which ranges through a smooth manifold. To make this precise, we suppose that p 7! L(p) is a family of Fred- holm operators on a real Hilbert space H, say L(p) : H ! H, depending continuously on p 2 M, where M is a nite-dimensional compact smooth manifold. Then by Proposition A.5 on page 156 of \[3\], there is a closed linear subspace V H of nite codimension such that

1. V does not intersect the kernel of L(p) for any p 2 M.
2. (L(p)(V)) has constant codimension and p 7! H=(L(p)(V)) is a nite- dimensional vector bundle E over M.
3. The linear maps L(p) induce a vector bundle map L~ : (H=V) M !
   E.

* * *

## 90 CHAPTER 3. GLOBAL ANALYSIS

We can then dene the determinant line bundle of L by

det(L) = max((H=V) M) \[max(E)\] ;

where max denotes the rank of the vector bundle in question. We claim that the determinant line bundle is independent of the choice of V. Indeed, if V1 is a second choice of linear subspace satisfying the above conditions, we can assume without loss of generality that V1 V, and then

H H V V =; E = E1; V1 V V1 V1

where E1 is the line bundle whose ber at p is H=(L(p)(V)). Since

max(W W ) = max(W ) max(W ); 1 2 1 2

max(W) max(W ) =;

being the trivial line bundle, we see that

max((H=V )

M) \[max(E )\] =
max((H=V)

M) \[max(E)\] :
1 1

Now we can use the exact sequence

H H 0 ! Ker(L(p)) !!! Coker(L(p)) ! 0 V L(p)(V)

to show that there is a natural isomorphism

det(L)(p) = max(Ker(L(p))) \[max(Coker(L(p)))\] :

The key point of this construction is that the determinant line bundle of a family of elliptic operators L is well-dened even though the dimensions of the kernels and cokernels vary from point to point. It is not dicult to extend the above discussion to families of Fredholm maps, L(p) : H1! H2, between two dierent Hilbert spaces. In our case, we have a family of surjective linear operators (A; ) 2 Mf 7! LA;which are Fredholm on the suitable L2kcompletions, with

## Ker(LA; ) = TA; (Mf ):

Hence if d is the dimension of the moduli space, the determinant line bundle of L is the top exterior power of the tangent bundle to Mf ,

det(L) = d Ker(L) = d (Mf ):

* * *

3.4. TRANSVERSALITY 91 Thus a nowhere zero section of det(L) will give an orientation of Mf . If we dene a family of elliptic operators Lt, for t 2 \[0; 1\], by
Lt(a; 0 ) = (DA + 0 ita ;a; (da) + 2t( ; 0 ));

the determinant line bundle det(Lt) is dened for every t and depends continuously on t. Thus the bundles det(Lt) are all isomorphic, and it suces to construct a nowhere zero section of det(L0), where L0 = DA +

d + . But det(L0) = det(DA + ) det( d + ):

The rst factor has a nowhere zero section which comes from the orienta- tions of the kernel and cokernel of DA + dened by complex multiplication, whereas the second factor inherits a nowhere zero section from an orienta- tion of H+ 2

(M). Thus det(L0) is trivialized, which in turn trivializes the top
exterior power of the tangent space to the moduli space, thereby orienting the moduli space and nishing the proof of the theorem.

Transversality Theorem 2. Let M be a compact oriented simply con- nected smooth four-manifold with a spin c -structure. If b+(M) > 0, then for generic choice of self-dual two-form, M is an oriented smooth manifold, whose dimension is given by the formula

dim(M) = 2(index of DA +

) b+1;

## or equivalently

21 dim(M) = hc1(L); \[M\]i (2 (M) + 3 (M)): (3.13) 4

Proof: Note that a solution to the perturbed Seiberg-Witten equations with = 0 will occur only if c1(L) contains a connection with FA + =, and this will occur for lying in a subspace of 2 +(M) of codimension b+one, by the Proposition of x1.9. This theorem therefore follows from the preceding one by dividing out by the free S1-action, which decreases the dimension by one. The second formula for the index follows from the Atiyah-Singer Index Theorem applied to DA + .

Remark. Note that for the moduli space to have nonnegative formal di- mension, 2(M) c1(L) \[M\] b+1; 4 and hence for any unitary connection on $L$,

$$\\frac{1}{4\\pi^2} \\int\_M \|F\_A^+\|^2 - \|F\_A^-\|^2 dV \\geq \\frac{\\tau(M)}{4} - b\_+ - 1,$$

or

$$\\int\_M \|F\_A^-\|^2 dV \\leq \\int\_M \|F\_A^+\|^2 dV - (4\\pi^2) \\left( \\frac{\\tau(M)}{4} - b\_+ - 1 \\right).$$

(3.14)

This, together with an extension of inequality (3.6) to the case of nonzero $\\phi$, shows that $\\int\_M \|F\_A^+\|^2 dV$ is bounded, and hence for generic $\\phi$, the moduil space given by the Transversality Theorem 2 will be empty except for
finitely many line bundles $L$.

3.5 The intersection form

We now describe some of the classical topological invariants of simply connected four-dimensional manifolds.

Let $M$ be a compact simply connected four-manifold. The intersection
form on integer cohomology is a symmetric bilinear map

$$Q : H^2(M; \\mathbb{Z}) \\times H^2(M; \\mathbb{Z}) \\to \\mathbb{Z},$$

defined to be the composition of the cup product

$$H^2(M; \\mathbb{Z}) \\times H^2(M; \\mathbb{Z}) \\to H^4(M; \\mathbb{Z})$$

with the standard isomorphism of $H^4(M; \\mathbb{Z})$ to $\\mathbb{Z}$ which pairs an element
of $H^4(M; \\mathbb{Z})$ with the orientation class of $M$.

The intersection form can also be defined on de Rham cohomology by
integration of differential forms. Indeed, we can let

$$\\tilde{Q} : H^2(M; \\mathbb{R}) \\times H^2(M; \\mathbb{R}) \\to \\mathbb{R}$$

by

$$\\tilde{Q}(\[\\alpha\], \[\\beta\]) = \\int\_M \\alpha \\wedge \\beta.$$

In the case where $M$ is simply connected, it follows from the universal
coefficient theorem that

$$H^2(M; \\mathbb{Z}) \\cong \\text{Hom}(H\_2(M; \\mathbb{Z}), \\mathbb{Z}).$$

a free abelian group. This group lies inside the real cohomology as a lattice,

$$H^2(M; \\mathbb{Z}) = {\[\\alpha\] \\in H^2(M; \\mathbb{R}): \\text{the integral}$$ of α over any compact surface in M is an integer}.

The restriction of $Q$ to $H^2(M; \\mathbb{Z})$ is integer-valued, and this restriction is the intersection form defined before.

Finally, we can also regard the intersection form as defined on integer homology $H\_2(M; \\mathbb{Z})$. To see this, we need to utilize an important fact from the topology of four-manifolds, any element of $H\_2(M; \\mathbb{Z})$ can be represented by a compact oriented surface $\\Sigma$ which is embedded in $M$. One way of proving this is to note that since $M$ is simply connected, it follows from the Hurewiz isomorphism theorem that $H\_2(M; \\mathbb{Z}) \\cong \\pi\_2(M)$ and hence any element of $H\_2(M; \\mathbb{Z})$ can be represented by a smooth map $f : S^2 \\rightarrow M$. We can arrange, after a possible perturbation, that this map be an immersion with transverse self-intersections, and the self-intersections can be removed by surgeries, each of which replaces two intersecting disks by an annulus. The result is that a given element of $H\_2(M; \\mathbb{Z})$ can be represented by an embedded surface which may have several components, each of which may have arbitrary gems.

Using this fact, we can define a map

$$\\mu : H\_2(M; \\mathbb{Z}) \\rightarrow H^2(M; \\mathbb{Z})$$

as follows: An element of $H\_2(M; \\mathbb{Z})$ can be represented by a compact oriented surface $\\Sigma$. This surface $\\Sigma$ lies within a small tubular neighborhood $V$, the image under the exponential map of an $e$-neighborhood of the zero section in the normal bundle of $\\Sigma$ in $M$. The Thom form on the total space of the normal bundle, chosen as described in §1.6 to have compact support within the given $e$-neighborhood, can be pushed forward under the exponential map to a closed two-form $\\Phi\_\\Sigma$ which has compact support contained within $V$. Extending $\\Phi\_\\Sigma$ by zero to all of $M$ gives a closed two-form defined on $M$, which we still denote by $\\Phi\_\\Sigma$. If $\\Lambda'$ is an oriented embedded surface in $M$ which has transverse intersection with $\\Sigma$, the integral of $\\Phi\_\\Sigma$ over $\\Sigma'$ will be an integer, since the integral of the Thom form over any fiber is an integer. In fact this integer is exactly the intersection number of $\\Sigma$ with $\\Sigma'$ as described at the end of §1.6. Thus the de Rham cohomology class $\[\\Phi\_\\Sigma\]$ of $\\Phi\_\\Sigma$ lies in the image of $H^2(M; \\mathbb{Z})$ under the coefficient homomorphism. We set

$$\\mu(\[\\Sigma\]) = \[\\Phi\_\\Sigma\] \\in H^2(M; \\mathbb{Z}).$$

By the Classification Theorem for Complex Line Bundles, an element of $H^2(M; \\mathbb{Z})$ is the first Chern class of a complex line bundle $L$ over $M$. Choose a smooth section $\\sigma : M \\rightarrow L$ which has transverse intersection with the zero section, and let

$$Z\_{\\sigma} = \\sigma^{-1}(\\text{zero section}).$$

* * *

## 94 CHAPTER 3. GLOBAL ANALYSIS

IfZis the dierential form constructed in the previous paragraph, the integral ofZover any compact oriented surface 0 is the intersection number of Z with 0 , which is just hc1(L); 0 i, by the Corollary in x1.6. In particular, we see that that \[Z\] = c1(L) and hence

## NZ = LjZ; (3.15)

which is sometimes called the adjunction formula (see \[18\], page 146). Thus (\[Z\]) = c1(L), and must be onto. Since H2(M; Z) and H2(M; Z) are free abelian groups of the same rank, is an isomorphism. (The fact that is an isomorphism is one manifestation of Poincare duality.) If is a smooth two-form on M it follows quickly from Fubini’s theorem that Z Z

^ = i ; M where the i on the right denotes the inclusion of in M. Thus Z Q( (\[\]); \[\]) = i = h\[\]; \[\]i:

Finally, we can use the isomorphism to dene the intersection form on homology,

Q : H2(M; Z) H2(M; Z) ! Z by Q(\[\]; \[ 0 \]) = Q( (\[\]);(\[ 0 \])):

We therefore have several equivalent ways of regarding Q: Z Z Z Q(\[\]; \[ 0 \]) = ^ 0 = 0 = M0

= intersection number of with 0 ;

when and 0 intersect transversely. The last interpretation of Q is the motivation for calling it the intersection form. Since H2(M; Z) = Hom(H2(M); Z), any group homomorphism : H2(M; Z) ! Z is of the form

(b) = h\[M\];bi = Q( (\[M\]);b);
for some \[M\] 2 H2(M; Z). This implies that Q is a unimodular symmetric bilinear form. Thus in terms of a basis for the free abelian group H2(M; Z), the intersection form Q can be represented by a b2 b2 symmetric matrix with integer entries and determinant 1.

* * *

3.5. THE INTERSECTION FORM

The integer-valued intersection form $Q$ carries more information than the real-valued form $\\bar{Q}$ defined on de Rham cohomology. Indeed, the integer-valued symmetric bilinear forms represented by the matrices

$$\\begin{pmatrix} 0 & 1 \ 1 & 0 \\end{pmatrix}, \\quad \\begin{pmatrix} 1 & 0 \ 0 & -1 \\end{pmatrix}$$

are equivalent over the reals, but not over the integers because

$$(x y) \\begin{pmatrix} 0 & 1 \ 1 & 0 \\end{pmatrix} \\begin{pmatrix} x y \\end{pmatrix} = 2xy$$

takes on only even values, while

$$(x y) \\begin{pmatrix} 1 & 0 \ 0 & -1 \\end{pmatrix} \\begin{pmatrix} x y \\end{pmatrix} = x^2 - y^2$$

can be either even or odd, in general, we say that a unimodular symmetric bilinear form

$$Q : \\mathbb{Z}^r \\times \\mathbb{Z}^r \\rightarrow \\mathbb{Z}$$

is even if $Q(a, a)$ is always even; otherwise it is said to be odd.

It is an interesting problem to classify unimodular symmetric bilinear forms of a given rank up to isomorphism. Indefinite unimodular symmetric bilinear forms are classified in \[28\]; in the odd case, they are direct sums of $(\\pm 1)'s$, while in the even case, they are direct sums of $H'$s and $E8'$s, where these forms are represented by the matrices

$$H = \\begin{pmatrix} 0 & 1 \ 1 & 0 \\end{pmatrix}$$

and

$$E8 = \\begin{pmatrix} -2 & 1 & 0 & 0 & 0 & 0 & 0 \ 1 & -2 & 1 & 0 & 0 & 0 & 0 \ 0 & 1 & -2 & 1 & 0 & 0 & 0 \ 0 & 0 & 1 & -2 & 1 & 0 & 0 \ 0 & 0 & 0 & 1 & -2 & 1 & 0 \ 0 & 0 & 0 & 0 & 1 & -2 & 0 \ 0 & 0 & 0 & 0 & 1 & -2 & 0 \ 0 & 0 & 0 & 0 & 1 & -2 & 0 \\end{pmatrix}.$$

This last matrix is negative-definite, has only even entries down the diagonal, and has determinant one. It can be shown to be the smallest rank matrix with these properties.

* * *

## 96 CHAPTER 3. GLOBAL ANALYSIS

On the other hand, there are often many denite forms of a given rank. For example, in the even case, there are over 10 51 negative denite forms of rank 40! Here are the intersection forms of some important simply connected four-manifolds.

Example 1. The intersection form of the complex projective plane P2C with its usual orientation is represented by the matrix

## ( 1 ) :

This follows immediately from the fact that the cohomology ring of P2C is generated by an element a 2 H2(P2C) subject to a single relation a3 = 0. The intersection form of the complex projective plane with the opposite orientation, denoted by P2C, is

## ( 1 ) :

Example 2. The intersection form of S2 S2 is represented by the matrix

H. Indeed, if !1and !2are the area forms of the two factors, normalized to give area one,
Z 0 1 !i^ !j= : S2S2 1 0

Example 3. The K3 surface is the smooth complex hypersurface in P3C which is dened in homogeneous coordinates by the equation

(z0) 4 + (z1) 4 + (z2) 4 + (z3) 4 = 0:

As we will see in x3.8, this four-manifold has an even intersection form and the topological invariants

b += 3; b = 19:

It then follows from the classication of indenite forms that the intersec- tion form of this algebraic surface is

## E8 E8 H H H:

Example 4. Let M1 and M2 be two compact oriented four-manifolds. Choose points p 2 M1 and q 2 M2 and positively oriented coordinate systems (U;) and (V; ) centered at p and q. By rescaling the coordinates if necessary, we can arrange that

B2(0) (U); B2(0) (V);

* * *

3.5. THE INTERSECTION FORM 97 where B2(0) is the ball of radius two about the origin. We form the oriented connected sum M1\]M2 as the quotient of
\[M1 1 (B1=2(0))\] \[ \[M2 1 (B1=2(0))\]\
\
by identifying 1\
\
(x) with\
1 (x=jxj2). This corresponds to taking a disk out of each manifold and identifying the boundaries by an orientation re- versing dieomorphism. If M1 and M2 have intersection forms Q1 and Q2 respectively, then the oriented connected sum M1\]M2 has intersection form Q1 Q2.

An element a 2 H2(M; Z) is said to be characteristic if it satises the criterion

Q(a;b) = Q(b;b) mod 2; for all b 2 H2(M; Z):

Theorem. If L is the virtual line bundle for a spin c structure on a smooth four-manifold M, then c1(L2) is a characteristic element. Conversely, any characteristic element is c1(L2) for some spin c structure on M.

Proof: If E is a genuine line bundle on M, then L E corresponds to a second spin c structure. Using (2.19), we calculate the dierence between the indices of the Dirac operators with coecients in L and L E, and conclude that Z Z 12 c1(L) ^ c1(E) + (c1(E)) 2 Z; M2M

which immediately implies that

121 Q(c1(L );c1(E)) + Q(c1(E);c1(E)) = 0; mod Z: 2 2

Since any element of H2(M; Z) is the rst Chern class of some line bundle E, we conclude that c1(L2) is characteristic. We prove the converse using the the fact that every oriented four- manifold has a spin c structure. Thus there exists at least one characteristic element a which corresponds to a spin c structure with some virtual line bundle, which we call L. If a0 is a second characteristic element, then

Q(a0 a;b) = 0 mod 2; for all b 2 H2(M; Z);

from which it follows that a0 a is divisible by two. Thus there is a line bundle E over M with c1(E2) = a0 a, and we can construct a spin c

structure on M with virtual line bundle L E. Clearly c1((L E) 2 ) = a0.

* * *

## 98 CHAPTER 3. GLOBAL ANALYSIS

Corollary. A smooth four-manifold has an even intersection form if and only if it has a spin structure.

Proof: Simply note that Q is even if and only if 0 is a characteristic element.

The intersection form is the basic topological invariant of a compact simply connected topological four-manifold. In fact, a classical theorem of J. H. C. Whitehead and John Milnor states that two such four-manifolds are homo- topy equivalent if and only if they have the same intersection form. More recently, Michael Freedman showed that any unimodular symmetric bilin- ear form is realized as the intersection form of a compact simply connected topological four-manifold, and that there are at most two such manifolds with the same intersection form \[15\]. Not all unimodular symmetric bilinear forms are realized on smooth four-manifolds, however. In particular, although E8 can be realized as the intersection form of a compact oriented topological four-manifold, it cannot be realized on a smooth manifold, because such a manifold would be spin by the above theorem and hence would contradict Rochlin’s theorem.

# 3.6 Donaldson’s Theorem

There is a very striking restriction on the denite intersection forms that can be realized on a a simply connected four-manifold which possesses a smooth structure:

Theorem (Donaldson \[8\]). The only negative denite unimodular form represented by a compact smooth simply connected four-manifold is the standard form Q = I.

There are two cases to the proof, Q even and Q odd. We will only give a complete proof in the even case\|we will show that an even negative denite form (such as E8 E8) cannot be realized on a smooth four-manifold. In the even case, we can take L to be the trivial bundle and use Transver- sality Theorem 1 of x3.4. Since b+= 0 and we can assume without loss of generality that b > 0, this theorem implies that Mf is a smooth manifold of dimension k = b =4 > 0, and the quotient manifold M is a smooth manifold of dimension k 1 except for a singularity at the point \[dA; 0\], dAbeing the unique connection for which FA + =. The tangent space to M f at d Ais simply the space of harmonic spinor elds ker(DA + ) on which the group S1 of unit-length complex numbers acts in the usual fashion by complex multiplication. Hence M is a smooth manifold except for a singularity at \[dA; 0\], which is a cone on P m 1 C, where 2m = k.

* * *

3.6. DONALDSON'S THEOREM

Now we recall the fiber bundle (3.9) in which the total space $B^\*$ is homotopy equivalent to the total space of the universal sphere bundle $E$. We have a commutative diagram

$$\\widetilde{M}\_\\phi - {\[d\_A, 0\]} \\subset \\widetilde{B}^\* = E$$

$$\\downarrow$$

$$\\downarrow$$

$$\\downarrow$$

$$M\_\\phi - {\[d\_A, 0\]} \\subset B^\* = P^\\infty C$$

The bundle $E$ over $P^\\infty C$ restricts to a bundle over $P^{m-1}C$ which we easily verify to be homotopy equivalent to the Hopf fibration

$$S^1 \\rightarrow S^{2m-1} \\rightarrow P^{m-1}C.$$

Hence the restriction of $E$ to $P^{m-1}C$ has nontrivial first Chern class, and since the cohomology of $P^{m-1}C$ is a truncated polynomial algebra,

$$H^\*(P^{m-1}C; \\mathbb{Z}) \\cong P\[a\]/(a^m),$$

where $a$ has degree two, we see that

$$\\int\_{P^{m-1}C} (c\_1(E))^{m-1} \\neq 0 \\Rightarrow \[P^{m-1}C\] \\neq 0$$

as an element of $H\_{2m-2}(B^ _, \\mathbb{Z})$. But this contradicts the fact that $M\_\\phi$ exhibits $P^{m-1}C$ as a boundary in $B^_ $.

Here is a sketch of how to proceed if in the case where $Q$ is odd. Note that if the intersection form of $M$ is negative definite, for any choice of virtual line bundle $L$, we can always construct a unique connection such that $F\_A^\* = \\phi$ giving rise to a reducible solution $\[d\_A, 0\] \\in M\_\\phi L$. Thus the argument in the preceding paragraphs will again yield a contradiction so long as we can find a characteristic element $\[L^2\]$ such that the corresponding moduli space $M\_\\phi$ has positive formal dimension.

Since $b\_+ = b\_1 = 0$, this will occur exactly when the index of $D\_A^\*$ is positive. By the Aiyah-Singer index theorem, this means that

$$-\\frac{\\tau(M)}{8} + \\frac{1}{2} \\int\_M c\_1(L)^2 = \\frac{1}{8} (b\_- + Q(a, a)) > 0, \\text{ or } -Q(a, a) < b\_2,$$

since $b\_2 = b\_-$. An argument of Elkies \[13\] shows that either $Q = -I$ or there is a characteristic element satisfying this last inequality, thereby completing this approach to proving Donaldson's theorem.

Donaldson's theorem gives a complete answer to the question of which definite unimodular symmetric bilinear forms can be realized as intersection

* * *

## 100 CHAPTER 3. GLOBAL ANALYSIS

forms on compact simply connected smooth four-manifolds\|the only pos- sibilities are the intersection forms of

P2C \]\] P2C and P2C \]\] P2C:

One could ask a similar question for the indenite forms. All the odd indenite forms can be realized on connected sums of P2C’s and P2C’s. If s 3r, the even form 2r(E8) sH

can be realized on a connected sum of r copies of the K3 surfaces and s 3r copies of S2 S2. One of the striking successes of the Seiberg-Witten theory is a theorem due to Furuta: If 2rE8 sH is realized on a compact simply connected smooth four-manifold, then s 2r +1. (See \[17\] or \[1\] for further details.) Coupled with results of Freedman, which are described in \[15\], Don- aldson’s Theorem implies that there are smooth four-manifolds which are homeomorphic but not dieomorphic to R4. A relatively elementary pre- sentation of the basic idea is presented in \[14\], x1.

# 3.7 Seiberg-Witten invariants

For four-manifolds with indenite intersection form, the Seiberg-Witten equations provide a collection of invariants which depend upon the choice of a spin c structure. We will see that these invariants sometimes allow us to distinguish between smooth structures on a given topological four-manifold. Let L be a virtual complex line bundle over M such that W+L is dened as a genuine complex vector bundle. Assuming that b+(M) > 0, we can then form the moduli space ML;, which depends upon L. Ac- cording to the Transversality Theorem 2 from x3.4, this moduli space is a compact manifold for a generic choice of. The key point in the argument is that a solution to the perturbed Seiberg-Witten equations with = 0 can occur only if c1(L) contains a connection with FA + =. This will not occur generically, but only for lying in an ane subspace of 2 +(M) of codimension b+one, by the Proposition at the end of x1.9. Of course, the moduli space ML;depends upon the choice of Rieman- nian metric on M and the choice of. If1and2are two choices and b +2, then a generic path from1to2will miss the subspace . It fol- lows from Smale’s innite-dimensional generalization of transversality (see \[35\], Theorems 3.1 and 3.3) that W = 1 () is an oriented submanifold of N such that @W = ML;2ML;1:

* * *

3.7. SEIBERG-WITTEN INVARIANTS 101 In other words, dierent choices of yield cobordant moduli spaces. It follows that if \[\] is any cohomology class in B , then

## h\[\]; \[ML;1\]i = h\[\]; \[ML;2\]i: (3.16)

Similarly, changing the Riemannian metric on M alters the moduli space by a cobordism.

Denition. Suppose that b+2 and that the dimension of ML;is even. Then the Seiberg-Witten invariant of L is

d1 SW(L) = hc1; \[ML;\]i; where d = dim ML;; 2

c1 is the rst Chern class of the complex line bundle E associated to the S1-bundle Be!B , and is chosen to be generic.

Equation (3.16) and the corresponding equation for change of Riemannian metrics shows that the Seiberg-Witten invariants are well-dened. If (dA; ) is a solution to the Seiberg-Witten equations for L, the (dA;J ) is a solution for L 1 , where J : W+L! W+L 1 represents conjugate-linear multiplication on the right by the quaternion J. From this fact, one can show that SW (L 1 ) = SW (L). If b+= 1, the moduli space ML;is still a smooth manifold for generic choice of so long as does not lie in a certain hyperplane 2 +(M); is the image of 1

(M) under the map a 7! (FA0+ da)

- , where FA0is the curvature of a base connection in L. By Hodge theory, is perpendicular to H+ 2

(M) in the orthogonal direct sum decomposition
2

(M) = H2 (M) d

- ( 1

(M)):

However, two moduli spaces ML;1and ML;1are not necessarily cobor- dant if1and2belong to dierent components of 2 +(M). In particular, we can dene SW (L) when L 6= 0 and hc1(L) 2 ; \[M\]i 0. Indeed, these conditions imply that the curvature of any connection in L satises FA + 6= 0, and hence no connection satises FA + =, when is suciently small, so we can take

SW(L) = hc d 1 ; \[ML;\]i; for generic small choice of.

Theorem (Witten \[41\]). If an oriented Riemannian manifold has a Rie- mannian metric of positive scalar curvature, all of its Seiberg-Witten in- variants vanish.

* * *

Proof. This follows immediately from the Lemma of §3.3 that the modified Seiberg-Witten equations have no solutions when the scalar curvature is positive and $\\phi$ is sufficiently small.

Manifolds which admit metrics of positive scalar curvature include $S^4$, $P^2C$ and $P^2C$. A theorem of Gromov and Lawson \[19\] implies that if $M$ and $N$ are four-manifolds of positive scalar curvature, their connected sum $M\_2N$ also admits a metric of positive scalar curvature. Thus Witten’s theorem implies that the manifolds

$$k(P^2C) \\downarrow l(P^2C)$$

all have vanishing Seiberg-Witten invariants.

The simplest examples of manifolds with nonvanishing Seiberg-Witten invariants come from the theory of simply connected complex algebraic surfaces, as we will see in the next two sections. Such algebraic surfaces are of simple type. The formal dimension of the moduli space $M\_L$ is zero when

$$c\_1(L^2)^2\[M\] = 3r(M) + 2\\chi(M),$$

which according to (2.22) occurs exactly when $c\_2(W\_+ \\otimes L) = 0$. The following lemma explains the relationship this last condition and the existence of almost complex structures.

**Lemma.** Homotopy classes of almost complex structures on $M$ are in one-to-one correspondence with line bundles $L^2$ over $M$ such that

1. $W\_+ \\otimes L$ exists as a bundle,
2. $c\_1(L^2)^2\[M\] = 3r(M) + 2\\chi(M).

Proof. An almost complex structure $J$ on $M$ yields a spin-$^-$structure as we described in §2.3. If $L$ is the corresponding virtual line bundle, then $W\_+ \\otimes L$ exists as a genuine vector bundle and divides as a Whitney sum,

$$W\_+ \\otimes L = \\Theta \\oplus L^2.$$
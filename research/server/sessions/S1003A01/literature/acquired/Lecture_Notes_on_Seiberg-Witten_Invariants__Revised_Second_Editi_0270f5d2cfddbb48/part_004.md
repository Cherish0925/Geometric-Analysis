---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: Lecture Notes on Seiberg-Witten Invariants (Revised Second Edition)]

where $\\Theta$ is the trivial line bundle. It follows from Proposition 4 from §1.5 that

$$\\text{ch}(W\_+ \\otimes L) = 1 + \\text{ch}(L^2) = 2 + c\_1(L^2) + \\frac{1}{2}(c\_1(L^2))^2.$$

Thus $c\_1(W\_+ \\otimes L) = c\_1(L^2)$, and by (2.20), $c\_2(W\_+ \\otimes L) = 0$. The second condition of the Lemma now follows from (2.22).

To prove the converse, note that if the conditions in the statement of the Lemma hold, then according to (2.22), $c\_2(W\_+ \\otimes L) = 0$. It then follows

* * *

3.8. DIRAC OPERATORS ON KAHLER SURFACES 103 from obstruction theory for complex vector bundles of rank two that W+L has a nowhere vanishing section. Thus
p () ! = 2 j ()j p is a self-dual two-form on M of length 2. Such a self-dual two-form denes an almost complex structure J (L2) on M by !(Jx; ) = hx; i: It is readily checked that the two construction we have described are inverse to each other.

# 3.8 Dirac operators on Kahler surfaces

Among the most important examples of smooth four-manifolds are Kahler surfaces, Kahler manifolds of complex dimension two. In fact, it is relatively easy to do computations with these manifolds. Recall that a Riemannian metric h ; i on a complex manifold M is called Hermitian if hJx;Jyi = hx;yi; for all x;y 2 TpM: In this case we can dene a rank two covariant tensor eld ! on M by !(x;y) = hJx;yi: (3.17) Since !(y;x) = hJy;xi = hJ2y;Jxi = hy;Jxi = hJx;yi =!(x;y); we see that ! is skew-symmetric. Thus ! is a two-form, called the Kahler form on M. Denition. A Kahler manifold is a complex manifold M with a Hermitian metric h ; i whose Kahler form is closed. Let us consider the case where M has dimension four. In terms of a moving orthonormal frame (e1;e2;e3;e4) such that e2 = Je1 and e4 = Je3, we can express the Kahler form as ! = e1 ^ e2 + e3 ^ e4:

* * *

This formula makes it clear that the Kähler form $\\omega$ is self-dual when the complex manifold is given its standard orientation. The Kähler condition $d\\omega = 0$ therefore implies also that $\\delta \\omega = 0$, so $\\omega \\in \\mathcal{H}\_2^1(M)$.

**Example 1.** The complex projective space $P^N \\mathbb{C}$ can be made into a Kähler manifold. To do this, we let $\\pi : \\mathbb{C}^{N+1} - {0} \\rightarrow P^N \\mathbb{C}$ denote the usual projection. If $U$ is an open subset of $P^N \\mathbb{C}$ and $Z : U \\rightarrow \\mathbb{C}^{N+1} - {0}$ is a holomorphic map with $\\pi \\circ Z = \\mathrm{id}$, we set

$$\\omega = i\\partial\\bar{\\theta}\\log(\|Z\|^2) = i\\sum\_{i,j=1}^N \\frac{\\partial^2}{\\partial z\_i \\partial z\_j}\\log(\|Z\|^2)dz\_i dz\_j.$$

It is readily checked that $\\omega$ is independent of the choice of holomorphic section $Z$. Indeed, if $Z = fW$, where $f$ is a nonzero holomorphic complex-valued function on $U$, then

$$i\\partial\\bar{\\theta}\\log(\|Z\|^2) = i\\partial\\bar{\\theta}\\log(\|f\|^2) + \\log(\|W\|^2\]$$

$$= i\\partial\\bar{\\theta}\\log f + i\\partial\\bar{\\theta}\\log \\bar{f} - i\\partial\\bar{\\theta}\\log(\|W\|^2) = i\\partial\\bar{\\theta}\\log(\|W\|^2).$$

Moreover, one checks immediately that $\\omega$ is closed, and a calculation in local coordinates shows that it is of maximal rank $(\\omega^N \\neq 0)$. One uses (3.17) in reverse to define a Hermitian metric on $P^N \\mathbb{C}$ which makes $P^N \\mathbb{C}$ into a Kähler manifold with the Kähler form $\\omega$.

**Example 2.** Any complex submanifold of a Kähler manifold is itself a Kähler manifold in the induced metric. According to a famous theorem of Chow, compact complex submanifolds of $P^N \\mathbb{C}$ are projective algebraic varieties without singularities, each describable as the zero locus of a finite collection of homogeneous polynomials.

For example, given a positive integer $n$, we can consider the complex surface $M\_n \\subset P^N \\mathbb{C}$ defined in homogeneous coordinates by the polynomial equation

$$P(z\_0, z\_1, z\_2, z\_3) \\cong (z\_0)^n + (z\_1)^n + (z\_2)^n + (z\_3)^n = 0. \\tag{3.18}$$

It follows from a theorem of Lefschetz on hyperplane sections (which is proven on pages 156-159 of \[18\] and in 57 of \[27\]) that $M\_n$ is simply connected. The other topological invariants of $M\_n$ can be calculated by regarding the polynomial $P$ as a section of $H^n$, where $H$ is the hyperplane section bundle over $P^N \\mathbb{C}$.

The hyperplane section bundle $H$ over $P^N \\mathbb{C}$ is defined via the open covering ${U\_0, \\ldots, U\_N}$, where

$$U\_i = {\[z\_1, \\ldots, z\_N\] \\in P^N \\mathbb{C}: z\_i \\neq 0}.$$

* * *

3.8. DIRAC OPERATORS ON KÄHLER SURFACES

by the transition functions $g\_j = (z\_j/z\_i)$. Thus a complex linear form
$a\_0 z\_0 + \\cdots + a\_N z\_N$ defines a section of $H$ with local representatives

$$\\sigma\_j = a\_0 \\frac{z\_0}{z\_j} + \\cdots + a\_N \\frac{z\_N}{z\_j},$$

and similarly, any polynomial of degree $n$ (such as the polynomial $P$ occurring in (3.18)) will define a section of $H^n$. By the adjunction formula
(3.15) the normal bundle to $M\_n$ is simply the restriction of $H^n$ to $M\_n$.

The hyperplane section bundle is the inverse of the universal bundle,
which has total space $E\_\\infty$ given by (1.22), as we described in §1.7. Recall
that the first Chern class of $E\_\\infty$ is $-a$, where $a$ is the standard generator of
$H^2(P^N\\mathbb{C}; \\mathbb{Z})$, such that $\[P^2\\mathbb{C}\], a = 1$. (Equivalently, $a$ is the cohomology
class of the Kähler form $\\omega$). Thus the first Chern class of $H$ is $a$, and the
Chern characters of these bundles are

$$\\text{ch}(E\_\\infty) = e^{-a}, \\quad \\text{ch}(H) = e^{a}.$$

Using Proposition 4 of §1.5, we see that

$$\\text{ch}(H^n) = e^{na}, \\quad \\text{ch}(E\_\\perp^1) = (N+1) - e^{-a},$$

the latter equality following from the fact that $E\_\\infty \\oplus E\_\\perp^1$ is the trivial
bundle of rank $N+1$.

On the other hand, we have an isomorphism

$$TP^N\\mathbb{C} \\cong \\text{Hom}(E\_\\infty, E\_\\perp^1) = E\_\\infty^\\perp \\otimes E\_\\perp^1 = H \\otimes E\_\\perp^1;$$

to see this, note that complex lines in $\\mathbb{C}^{N+1}$ near a given complex line
$\[z\_0, \\ldots, z\_N\]$ correspond to linear maps from the one-dimensional linear space
spanned by $(z\_0, \\ldots, z\_N)$ to its orthogonal complement. It follows that

$$\\text{ch}(TP^N\\mathbb{C}) = \\text{ch}(H)\\text{ch}(E\_\\perp^1) = e^n\[(N+1) - e^{-a}\] = (N+1)e^n - 1.$$

We can apply these calculations to our hypersurface $M = M\_n$ contained
in $P^3\\mathbb{C}$. Since

$$TP^3\\mathbb{C} = TM \\oplus NM \\cong TM \\oplus (H^n)\|M\|,$$

we see that

$$4e^n - 1 = \\text{ch}(TM) + e^{na} \\text{ or } \\text{ch}(TM) = 4e^n - e^{na} - 1,$$

where $a$ now denotes the pullback of the standard generator of $H^2(P^N\\mathbb{C}; \\mathbb{Z})$
to $M$. Hence

$$2 + c\_1(TM) + \\frac{1}{2}\[c\_1(TM)\]^2 - c\_2(TM) = 2 + (4-n)a + \\frac{1}{2}(4-n^2)a^2,$$

* * *

## 106 CHAPTER 3. GLOBAL ANALYSIS

modulo terms of degree greater than four, from which we conclude that

c1(TM) = (4 n)a; c2(TM) = (n2 4n + 6)a2:

As explained in detail in \[18\], pages 171 and 172, the Kahler surface Mnintersects a generic line in P3C in n points and therefore has degree n in the sense of algebraic geometry. By a theorem of Wirtinger, its volume is therefore n times as large as that of P2C, and hence ha2; \[Mn\]i = n. Therefore,

h\[c1(TM)\] 2 ; \[M\]i = (4 n) 2 n; hc2(TM); \[M\]i = n3 4n2 + 6n:

In particular, in the case n = 4, which gives the K3 surface described in x3.5, c1(TM) = 0 and hc2(TM); \[M\]i = 24:

But we will see shortly (3.23) that c2(TM)\[M\] = (M), the Euler charac- teristic of M, and hence

b0 = b4 = 1 and b1 = b3 = 0) b2 = 22:

Since M has a complex structure with rst Chern class zero, it follows from the Lemma at the end of the previous section that

3 (M) + 2 (M) = 0; which implies (M) = 16;

from which it follows that

b += 3 and b = 19;

as we claimed in x3.5. Moreover, the complex structure denes a canonical spin c structure on M with canonical bundle L2 satisfying c1(L2) = 0. Thus L must be trivial, M4 must have a genuine spin structure and its intersection form must be even. A similar computation in the case n = 5 would yield

h\[c1(TM)\] 2 ; \[M\]i = 5; hc2(TM); \[M\]i = (M) = 55;

and since 5 + 3 (M) + 2 (M) = 0, we must have (M) = 35, which implies that b += 9 and b = 44;

in this case, c1(L2) is odd and hence 0 is not characteristic, so the inter- section form is odd. Clearly, we could do similar calculations for arbitrary choice of n.

* * *

3.8. DIRAC OPERATORS ON KAHLER SURFACES 107 On a complex manifold M, a (p;q)-form is a complex-valued dierential form which can be expressed in local complex coordinates (z1;:::;zn) as
X f i 1 ip;j1 jqdzi1^^ dzip^ dzj1^^ dzjq:

We can decompose the space of complex-valued k-forms into forms of type (p;q), X k

(M) C =
p;q

(M);
p;q

(M) = f(p;q)-formsg: (3.19)
p+q=k

The exterior derivative divides into two components,

d = @ + @; @ : p;q

(M) ! p+1;q
(M); @ :
p;q

(M) ! p;q+1
(M);
and the Kahler condition implies the identities:

@ @ = 0; @ @ = 0; @ @ + @ @ = 0:

The Hermitian metric h; i on TM extends to TM C so that the extension is complex linear in the rst variable and conjugate linear in the second. This in turn denes a Hermitian metric on each k T M C and a Hermitian inner product ( ; ) on the space of smooth k-forms by Z

(;) = h;i(1=n!)!
n ; M

where ! is the Kahler form. Note that the decomposition (3.19) is orthog- onal with respect to this inner product. We can therefore dene formal adjoints,

@ : p+1;q

(M) ! p;q
(M); @ :
p;q+1

(M) ! p;q
(M);

## just as in x1.9, by requiring

(;@) = (@;); (; @) = (@;): (3.20)

In the case of complex surfaces, the Hermitian metric reduces the struc- ture group to U (2), and the various representations of U (2) correspond to the dierent types of tensor elds, sections of various associated vector bundles. For example, the standard representation of U (2) on C2 yields the complex tangent bundle TM, while the representation A 7! t A 1 = A yields the complex cotangent bundle whose sections are the (1; 0)-forms on

M. If the transition functions for TM are
g : U \ U! U (2);

* * *

## 108 CHAPTER 3. GLOBAL ANALYSIS

then the transition functions for the cotangent bundle are

t g 1 = g : U \ U! U (2):

Sections of the conjugate of this bundle are either (0; 1)-forms or complex vector elds\|in the presence of a Hermitian metric, we can identify (0; 1)- forms with complex vector elds. The complex exterior power K = 2 CT M of the cotangent bundle is called the canonical bundle. Its sections are (2; 0)-forms on M and it has transition functions

(det t g 1 ) = det g : U \ U! U (1):

The canonical bundle played a key role in the classication of complex surfaces due to Enriques and Kodaira (see \[21\] or \[5\]). Conjugation gives the anti-canonical bundle whose sections are the (0; 2)-forms and whose transition functions are

det g : U \ U! U (1):

We would like to relate all of this to the canonical Spin(4) c -structure constructed in x2.3. Recall that the transition functions for the distin- guished line bundle L2 selected by the Spin(4) c -structure are

det g : U \ U! U (1);

so L2 is just the anti-canonical bundle. Moreover,

W+L = W+K (1=2) = K 1 ; (3.21)

where denotes the trivial line bundle. On the other hand, since c j is the usual representation of U (2) on C2,

## W L = TM; (3.22)

the tangent bundle of M with its almost complex structure. Observe that it follows from (3.21) that c2(W+L) = 0, and then from (2.22) and (2.23) that c2(W L)\[M\] = (M), the Euler characteristic of M. Hence, by (3.22), c2(TM)\[M\] = (M): (3.23)

By the method given in x2.5, we can constuct a Spin(4) c connection on W L, with local representative

X4 1 d iaI!ijeiej; (3.24) 4 i;j=1

* * *

3.8. DIRAC OPERATORS ON KÄHLER SURFACES

the local moving orthonormal frame $(e\_1, e\_2, e\_3, e\_4)$ being chosen so that the Kähler form is

$$e\_1 \\cdot e\_2 + e\_3 \\cdot e\_4 = \\begin{pmatrix}
-2i & 0 & 0 & 0 \
0 & 2i & 0 & 0 \
0 & 0 & 0 & 0 \
0 & 0 & 0 & 0
\\end{pmatrix}.$$

The local representative (3.24) can be rewritten in matrix form as

$$d - i a I - \\frac{1}{2} \\begin{pmatrix}
-i(\\omega\_{12} + \\omega\_{34}) & (\\omega\_{13} + \\omega\_{42}) - i(\\omega\_{14} + \\omega\_{25}) & 0 & 0 \
\\sharp & i(\\omega\_{12} + \\omega\_{34}) & 0 & 0 \
0 & 0 & \\sharp & \\sharp \
0 & 0 & \\sharp & \\sharp
\\end{pmatrix},$$

Since the Kähler form is parallel with respect to the Levi-Civita connection,

$$\\omega\_{13} + \\omega\_{42} = 0 \\quad \\text{and} \\quad \\omega\_{14} + \\omega\_{23} = 0.$$

We determine a connection $d\_{A\_0}$ on $K^{-(1/2)}$ by setting

$$a = \\frac{1}{2}(\\omega\_{12} + \\omega\_{34}),$$

so that the induced connection on the trivial summand $\\Theta$ of $W\_+ \\otimes L$ is the trivial connection. The connection induced on the other summand $K^{-1}$ is then exactly the same as that induced by the Levi-Civita connection. (It follows that the curvature of a Kähler surfaces is always of type (1,1), a fact that is also easy to prove directly.)

**Proposition. In the Kähler case, the Dirac operator corresponding to the Spin(4)ᵀ connection $d\_{A\_0}$ is**

$$D\_{A\_0} = \\sqrt{2}(\\hat{\\partial} + \\tilde{\\partial}^\*),$$

(3.25)

when we identify sections of $\\Theta$ with $(0,0)$-forms, sections of $K^{-1}$ with $(0,2)$-forms, and sections of $W\_- \\otimes L = TM$ with $(0,1)$-forms.

Sketch of proof: It suffices to show that the two sides of the above equation agree at a given point of $M$. A key feature of Kähler manifolds (discussed in \[18\], Chapter 1, §7) is that one can choose local coordinates $z\_1 = x\_1 + ix\_2$, $z\_2 = x\_3 + ix\_4$, which are "normal" at $p$, so that

$$g\_{ij}(p) = \\delta\_{ij}, \\quad (\\partial g\_{ij}/\\partial x\_k)(p) = 0.$$

This implies that covariant derivatives can be replaced by ordinary derivatives of components at $p$. We set $e\_1(p) = (\\partial/\\partial x\_1)(p)$ and choose

$$\\varepsilon\_1(p), \\varepsilon\_2(p) \\in (W\_+ \\otimes L) _p, \\quad \\varepsilon\_3(p), \\varepsilon\_4(p) \\in (W_\- \\otimes L)\_p$$ with respect to which $(e\_1(p), \\dots, e\_4(p))$ are represented by the matrices given in §2.4. By means of the isomorphisms (3.21) and (3.22), we can make the identifications

$$\\varepsilon\_1(p) = 1, \\quad \\varepsilon\_2(p) = \\frac{1}{2}(d\\bar{z}\_1 \\wedge d\\bar{z}\_1)(p),$$

$$\\varepsilon\_3(p) = \\frac{1}{\\sqrt{2}}d\\bar{z}\_1(p), \\quad \\varepsilon\_4(p) = \\frac{1}{\\sqrt{2}}d\\bar{z}\_2(p).$$

in which the $(1/\\sqrt{2})'$s occur to normalize $d\\bar{z}\_1(p)$ and $d\\bar{z}\_2(p)$ to unit length.

At the point $p$, the Dirac operator can be expressed in matrix form as

$$\\begin{pmatrix}
0 & 0 & -\\frac{\\partial}{\\partial x\_1} + i \\frac{\\partial}{\\partial z\_2} & -\\frac{\\partial}{\\partial x\_3} + i \\frac{\\partial}{\\partial z\_4} \
0 & 0 & -\\frac{\\partial}{\\partial x\_2} + i \\frac{\\partial}{\\partial z\_4} & -\\frac{\\partial}{\\partial x\_1} + i \\frac{\\partial}{\\partial z\_2} \
\\frac{\\partial}{\\partial x\_3} + i \\frac{\\partial}{\\partial z\_4} & -\\frac{\\partial}{\\partial x\_2} + i \\frac{\\partial}{\\partial z\_4} & 0 & 0 \
\\frac{\\partial}{\\partial x\_3} + i \\frac{\\partial}{\\partial z\_4} & -\\frac{\\partial}{\\partial x\_2} + i \\frac{\\partial}{\\partial z\_4} & 0 & 0
\\end{pmatrix}.$$

Applying our identifications, we find that

$$D\_{A\_0}\\left( \\begin{array}{c} f \ 0 \ 0 \ 0 \\end{array} \\right) = \\left( \\begin{array}{c} 0 \ 0 \ \\frac{\\partial f}{\\partial x\_1} + i \\frac{\\partial f}{\\partial x\_2} \ \\frac{\\partial f}{\\partial x\_3} + i \\frac{\\partial f}{\\partial x\_4} \\end{array} \\right) = \\sqrt{2}\\left( \\frac{\\partial f}{\\partial \\bar{z}\_1} d\\bar{z}\_1 + \\frac{\\partial f}{\\partial \\bar{z}\_2} d\\bar{z}\_2 \\right),$$

which is just $\\sqrt{2}(\\partial f)(p)$. Similarly,

$$D\_{A\_0}\\left( \\begin{array}{c} 0 \ 0 \ h\_1 \ h\_2 \\end{array} \\right) = \\left( \\begin{array}{c} \\frac{\\partial h\_1}{\\partial x\_3} + i \\frac{\\partial h\_1}{\\partial x\_4} & \\frac{\\partial h\_2}{\\partial x\_3} - i \\frac{\\partial h\_2}{\\partial x\_4} \ 0 & 0 \\end{array} \\right).$$

Thus

the $K^{-1}$-component of $D\_{A\_0}(h\_1 d\\bar{z}\_1 + h\_2 d\\bar{z}\_2) = \\sqrt{2}\\partial(h\_1 d\\bar{z}\_1 + h\_2 d\\bar{z}\_2).

If $\\Pi^{(0,2)}$ denotes the orthogonal projection on $(0,2)$-forms, then

$$D\_{A\_0} = \\sqrt{2}\\partial : \\Omega^{(0,0)}(M) \\longrightarrow \\Omega^{(0,1)}(M),$$

$$\\Pi^{(0,2)} \\circ D\_{A\_0} = \\sqrt{2}\\partial : \\Omega^{(0,1)}(M) \\longrightarrow \\Omega^{(0,2)}(M).$$

The argument for the Proposition is completed by noting that the only self-adjoint operator with these two properties is $\\sqrt{2}(\\partial + \\partial^\*)$.

* * *

3.8. DIRAC OPERATORS ON KAHLER SURFACES 111 Remark. Any other Spin(4)
c connection is of the form dA= dA0ia, for some real-valued one-form a on M. In the general case, the above proof shows that 0 1 0 0 1 f +B 0 C B 0 C p DA@ A = B @ @f ia( @ )f + i @f + a( @ )f CA = 2@Af; (3.26) 0@x 1 @x1 @x2 @x2 0 @x @f ia( @x @ )f + i @x @f + a( @x @ )f 3 3 4 4

where @Adenotes the @-operator, twisted by the connection dA= dA0ia, a being a globally dened one-form on M.

In the case of the canonical Spin(4) c -structure associated to a Kahler surface, the Atiyah-Singer Index Theorem for the operator DA + 0 specializes to one of the key theorems of the theory of complex surfaces:

Riemann-Roch Theorem for Kahler surfaces. The index of DA + 0 is given by Noether’s formula

+12 complex index of DA 0 = fc1(TM)\[M\] + c2(TM)\[M\]g: 12

Proof: According to the Index Theorem,

+1 11 2 index of DA 0 = (M) + c1(K) \[M\]: 8 8

By the lemma from the preceding section,

3 (M) = 2 (M) c1(K 1 ) 2 \[M\];

and hence +1 12 index of DA 0 = (M) + c1(TM) \[M\]: 12 12 The formula we want now follows from (3.23).

On the other hand, the index of @ + @ can also be calculated directly by means of Hodge theory. We give only a brief indication of how this goes, and refer the reader to \[18\] for a more complete discussion. On a Kahler manifold, J and ? are parallel with respect to the Levi- Civita connection, from which it follows that the Hodge Laplacian com- mutes with orthogonal projection onto the space of (p;q)-forms, and we can therefore write X H k

(M) = H
p;q

(M);
p+q=k where $H^{p,q}(M)$ is the space of harmonic $(p, q)$-forms. Moreover, the Hodge Laplacian can be expressed in terms of the operator $\\bar{\\partial}$ and its adjoint:

$$\\Delta = 2(\\bar{\\partial} + \\bar{\\partial}^\*)^2.$$

In the case of a Kähler surface, it follows that

$$\\text{Index of } (\\bar{\\partial} + \\bar{\\partial}^\*) = \\dim H^{0,0}(M) + \\dim H^{0,2}(M) - \\dim H^{0,1}(M). \\quad (3.27)$$

Note that under conjugation, we have $H^{0,2}(M) \\cong H^{2,0}(M)$.

Since $d = \\bar{\\partial}$ on $H^{2,0}(M)$ and $(0,2)$-forms are automatically self-dual,
elements of $H^{2,0}(M)$ are just the $\\bar{\\partial}$-closed $(2,0)$-forms. These are just the holomorphic sections of the canonical bundle $K$, and the dimension of the
space of such sections is called the geometric genus of $M$. We denote the
geometric genus by $p\_g$. If $M$ is simply connected, $H^{0,1}(M) = 0$ and it
follows from (3.27) that

$$\\text{Index of } (\\bar{\\partial} + \\bar{\\partial}^\*) = 1 + p\_g.$$

Noether's formula now yields

$$1 + p\_g = \\frac{1}{12}\\left{c\_1^2(TM)\[M\] + c\_2(TM)\[M\]\\right}.$$

The invariants on the right-hand side can be reexpressed in terms of Euler
characteristic and signature,

$$1 + p\_g = \\frac{1}{4}\\left{\\tau(M) + \\chi(M)\\right} = \\frac{1}{2}(b\_+ + 1),$$

so $b\_+ = 2p\_g + 1$. In particular, $b\_+$ is odd for any simply connected Kähler
surface. Holomorphic sections of $K$ or antiholomorphic sections of $K^{-1}$ are
self-dual harmonic forms of type $(2,0)$ or $(0,2)$, and these fill out a linear
space of dimension $2p\_g$. We therefore conclude that the space of self-dual
harmonic forms of type $(1,1)$ is exactly one-dimensional, and any self-dual
harmonic two-form of type $(1,1)$ must be a constant multiple of the Kähler
form.

3.9 Invariants of Kähler surfaces

We are finally in a position to describe some compact simply connected
four-manifolds which have nontrivial Seiberg-Witten invariants. In this
section, we will calculate the Seiberg-Witten invariant SW($L$) in the case
where $M$ is a Kähler manifold with canonical bundle $K$ and $L = K^{-1/2}$.

* * *

3.9. INVARIANTS OF KAHLER SURFACES 113 Recall that in this case, W+= K
1 , where is the trivial line bundle. The following theorem is due to Witten \[41\]:

Theorem. A simply connected Kahler surface with b + 2 must satisfy SW (K 1=2

) = 1.
Proof: Let A0 denote the connection dened by the Kahler structure, as described in the previous section. Recall that we have some freedom in choosing in the modied Seiberg-Witten equations. Following an idea of Taubes \[37\], we set = FA + 0 + ! so that the Seiberg-Witten equations become DA + = 0; FA + = () + FA + 0 + !; (3.28)

The advantage to these equations is that they have an obvious solution p 2 A = A0; =; 0

since () =!. We will prove that the obvious solution is the only solution in the moduli space, and that it forms a nondegenerate zero- dimensional submanifold. This will show that SW (L) = 1. Suppose that (A; ) is any solution to (3.28) and write

=; where 2 (); 2 (K 1

): (3.29)
We make use of a transformation due to Witten,

A 7! A; 7! ; 7!: (3.30)

We claim that this transformation leaves invariant the zeros of the func- tional Z

S (A; ) = jDAj2 + jFA + () j2 dV; M and hence takes solutions of the perturbed Seiberg-Witten equations to other solutions. To see this, we write r A = r A0 ia, where a is a real-valued one-form, so that FA + = (da) + !;

and the functional becomes Z S (A; ) = jDAj2 + j(da) + ! ()j2 dV: M

* * *

## 114 CHAPTER 3. GLOBAL ANALYSIS

Apply the Weitzenbock formula as in x3.1 to obtain Z h A 2s2 + S (A; ) = jr j + j j + 2hFA;()i M4

+j () + ! (da) + j2 dV:

We can rewrite this as Z h A 2 A 2s2 2 + 2 S (A; ) = jr j + jr j + (j j + j j) + j(da)!j M4

- j ()j2 + 2h ();FA + 0 + !i dV:

Using the formula 02 21 j j j j 2 0 0 B 2 j j2 j j2 0 0 C () = i @ A; (3.31) 0 0 0 0 0 0 0 0

together with the fact that FA + 0 and ! are represented by diagonal matrices, we can easily check that every term in the last expression for S (A; ) is invariant under the transformation (3.30). Invariance under (3.30) implies that if (A; ) is a solution to the Seiberg- Witten equations with of the form (3.29), each of the components

0 and 0

must be a solution to the Dirac equation. Moreover, it follows from (3.31), invariance under (3.30) and the second of the Seiberg-Witten equations,

(da) + ! = ()

that = 0, and since a solution to the Dirac equation which vanishes on an open set must vanish identically, we see that either = 0 or = 0. Comparison of (3.31) with the Cliord algebra expression for the Kahler form, 0 1 2i 0 0 0 B 0 2i 0 0 C ! = e1 e2 + e3 e4 = @ A; 0 0 0 0 0 0 0 0

shows that 12 2 () ^ ! = (j j j j)! ^ !: 2

* * *

* * *

## 116 CHAPTER 3. GLOBAL ANALYSIS

p the maximum principle yields a contradiction. It follows that j j 2, (da) + 0 and FA + = FA + 0 . Since b1 = 0, it follows from Hodge theory that

(da) + = 0 = a) a = 0;

and hence the connection in the trivial bundle is the trivial connection. Thus is holomorphic in the usual sense, and it follows from the maximum modulus principle that is constant. Moreover, A = A0, while is uniquely determined up to multiplication by a complex number of length one. After dividing by the constant gauge transformations, we obtain a moduli space which consists of a single point. To conclude the proof of the Theorem, we note that we have found a unique S1-orbit of solutions which provides a unique orbit in the mod- uli space B. Since the formal dimension of the moduli space is zero, the dierential of : B 2 +(M) ! 2 +(M)

is automatically surjective at our solution \[A; ; 0\], so this solution is auto- matically regular.

Remark. The theorem of Witten has been extended by Taubes to sym- plectic manifolds with K taken to be the canonical bundle for a compatible almost complex structure. See \[38\] for further developments of this theory.

Corollary. A simply connected Kahler surface with b + 2 cannot be smoothly decomposed into a connected sum of P2C’s and P2C’s.

Proof: As we have seen before, a connected sum of P2C’s and P2C’s can be given a metric of positive scalar curvature by the construction given in \[19\], and must therefore have vanishing Seiberg-Witten invariants. However the preceding theorem shows that a Kahler manifold with b1 = 0 and b + 2 has nonvanishing Seiberg-Witten invariants.

This corollary allows us to construct many pairs of smooth manifolds which are homeomorphic but not dieomorphic. For example, by the discussion in x3.7, a complex surface in P3C dened by a nonsingular homogeneous polynomial of fth degree is a simply connected Kahler manifold which has odd intersection form, and

b += 9; b = 44:

Hence by the classication of odd quadratic forms, its intersection form is

Q = 9(1) 44( 1);

* * *

3.9. INVARIANTS OF KAHLER SURFACES 117 and by Freedman’s theory it is also homeomorphic to 9(P2C)\]44(P2C). However, it has nonvanishing Seiberg-Witten invariants, so it cannot be dieomorphic to 9(P2C)\]44(P2C). More generally, each of the hypersur- faces Mnof odd degree n, described in x3.7, is homeomorphic but not dieomorphic to a connected sum of P2C’s and P2C’s. Thus we get many pairs of compact simply connected four-manifolds which are homeomorphic but not dieomorphic, corroborating Theorem B from x1.1. In the earlier technology, the above corollary would have been obtained by means of Donaldson’s polynomial invariants which are constructed via nonabelian Yang-Mills theory\[10\]. Actually, the rst examples provided by Donaldson of compact simply con- nected four-manifolds that are homeomorphic but not dieomorphic sat- isfy the condition b+= 1. The Seiberg-Witten theory allows a very simple treatment of these examples, based upon the following proposition. Proposition. Suppose that a simply connected Kahler manifold with b

- = 1 has a canonical bundle K which satises the conditions

hc1(K) 2 ; \[M\]i 0; hc1(K) \[ \[!\]; \[M\]i > 0: (3.32)\
\
Then SW (K 1=2 ) is well-dened and SW (K 1=2\
\
) = 1.\
Proof: Note that according to the discussion in x3.7, the rst of these hy- potheses on the canonical bundle, together with the fact that the canonical bundle is not trivial, imply that the Seiberg-Witten invariant SW (K 1=2 ) is well-dened (when the perturbation is chosen to be small) even though b += 1. The proof of the previous theorem once again shows that the moduli space of solutions to the Seiberg-Witten equations (3.28) when = FA + 0 + ! consists of a single nondegenerate point. To see that the same conclusion holds when is small, we need to check that there are no singular solutions to the Seiberg-Witten equations with = 0 when = t(FA + 0 + !), for any t 2 (0; 1). But such a solution would imply Z Z FA + = t(FA + 0 + !)) (1 t) (FA + ) ^ ! > 0) (FA) ^ ! > 0: M M This would contradict the second hypothesis since c1(K) = c1(K 1 ) = 2\[FA\].\
\
To describe Donaldson’s examples, we need to utilize some results from the theory of algebraic surfaces which can be found in \[18\], as well as other sources. Let f and g be two generic cubic homogeneous polynomials in three variables, which dene a map\
\
\[f;g\] : P2C ! P1C; [f;g](https://web.math.ucsb.edu/~moore/%5Bz0;z1;z2%5D) = \[f (z0;z1;z2);g(z0;z1;z2)\];\
\
* * *\
\
## 118 CHAPTER 3. GLOBAL ANALYSIS\
\
except at nine points of P2C at which f and g have common zeros. (In the language of algebraic geometry, \[f;g\] is a rational map; see \[18\], page 491 for the denition.) The preimage of a generic point in P1C via \[f;g\] is a Riemann surface of genus one, dened by a cubic polynomial equation f + g = 0. To handle the nine singularities of \[f;g\], we use the notion of blow-up of an algebraic surface (\[18\], page 182). Blowing M up at the nine common zeros of f and g yields a new algebraic surface Y which is dieomorphic to P2C\](9P2C) and a genuine holomorphic map Y! P1C in which the preimage of a generic point is still a torus. Y is an example of an elliptic surface as described in \[18\], pages 564-572. Acording to a general formula for the canonical bundle of an elliptic surface (\[18\], page 572),

c1(K) = ( \[F\]);

where \[F\] is the homology class of the ber of Y! P1C and is the Poincare duality isomorphism described at the beginning of x3.5. Since two distinct bers have empty intersection and the integral of the Kahler form over a ber must be positive,

hc1(K) 2 ; \[M\]i = 0; hc1(K) \[ \[!\]; \[M\]i < 0:\
\
The last inequality is reassuring, since P2C\](9P2C) has a metric of positive scalar curvature, as we have seen, so SW (K 1=2 ) must vanish. However, we can modify the sign of the canonical bundle by performing appropriate logarithmic transformations on the bers of F, thereby ob- taining a manifold which satises the hypotheses of the proposition. The logarithmic transformation, described in \[18\], page 566, excises a tubular neighborhood of a smooth ber and glues it back in with a new dieomor- phism along the boundary, thereby obtaining a new elliptic surface. We can perform two logarithmic transformations on Y obtaining a new algebraic surface Z, with holomorphic map Z ! P1C, such that two of the bers (which we denote by F2 and F3) have multiplicities two and three, and hence \[F\] = 2\[F2\] = 3\[F3\]:

The new surface Z is called a Dolgachev surface. We can still apply the formula for c1(K), but this time we obtain

c1(K) = ( \[F\] + \[F2\] + 2\[F3\]) = ((1=6)\[F\]):

Since the integral of the Kahler form over F is positive, (3.32) holds. Dolgachev showed that Z is simply connected, and it is possible to verify that Y and Z have the same intersection forms (see \[9\]). Thus by

* * *

3.9. INVARIANTS OF KAHLER SURFACES 119 Freedman’s theory, Y and Z are homeomorphic. However, the proposition implies that SW (K
1=2

) = 1, and hence Y and Z are not dieomorphic.
Using more general logarithmic transformations, one can construct el- liptic surfaces homeomorphic to P2C\]9(P2C) in which c1(K) satises (3.32) and is divisible by an arbitarily large integer. (See Proposition 3.7 on page 316 of \[16\].) Given any smooth four-manifold, inequalities (3.6) and (3.14) give a bound on how divisible c1(L) can be if SW (L) is dened and nonzero. Any nite collection of smooth manifolds is also subject to such a bound. This fact yields a simple proof of the following striking theorem:

Theorem \[16\], \[33\]. The compact topological manifold P2C\]9P2C has innitely many distinct smooth structures.

* * *

120 CHAPTER 3. GLOBAL ANALYSIS

* * *

# Bibliography

\[1\] S. Akbulut, Lectures on Seiberg-Witten invariants, Proc. 1995 Gokova Geometry-Topology Conference, Scientic and Technical Research Council of Turkey, 1996, 95-118. \[2\] N. Aronszahn, A unique continuation theorem for solutions of ellip- tic partial dierential equations or inequalities of the second order, J. Math. Pure Appl. 36 (1957), 235-249. \[3\] M. F. Atiyah, K-theory, Benjamin, New York, 1967. \[4\] M. F. Atiyah, R. Bott and A. Shapiro Cliord modules, Topology 3, Suppl. I (1964), 3-38. \[5\] W. Barth, C. Peters and A. Van de Ven, Compact complex surfaces, Springer, New York, 1984. \[6\] N. Berline, E. Getzler and M. Vergne, Heat kernels and Dirac opera- tors, Springer, New York, 1991. \[7\] R. Bott and L. Tu, Dierential forms and algebraic topology, Springer, New York, 1982. \[8\] S. Donaldson, An application of gauge theory to four-dimensional topology, J. Dierential Geometry 18 (1983), 279-315. \[9\] S. Donaldson, Irrationality and the h-cobordism conjecture, J. Dier- ential Geometry 26 (1987), 141-168. \[10\] S. Donaldson, Polynomial invariants for smooth 4-manifolds, Topology 29 (1990), 257-315. \[11\] S. Donaldson, The Seiberg-Witten equations and 4-manifold topology, Bull. Amer. Math. Soc. 33 (1996), 45-70. 121

* * *

## 122 BIBLIOGRAPHY

\[12\] S. Donaldson and P. B. Kronheimer, The geometry of four-manifolds, Oxford Univ. Press, Oxford, 1984.

\[13\] N. Elkies, A characterization of the Z n lattice, Math. Research Letters 2 (1995), 321-326.

\[14\] D. Freed and K. Uhlenbeck, Instantons and four-manifolds, Springer, New York, 1990.

\[15\] M. Freedman and F. Quinn, Topology of 4-manifolds, Princeton Univ. Press, Princeton, New Jersey, 1990.

\[16\] R. Friedman and J. W. Morgan, On the dieomorphism type of certain algebraic surfaces I, II, J. Dierential Geometry 27 (1988), 297-369.

\[17\] M. Furuta, Monopole equation and the (11=8)-conjecture, Math. Re- search Letters 8 (2001), 279-291.

\[18\] P. Griths and J. Harris, Principles of algebraic geometry, Wiley, New York, 1978.

\[19\] M. Gromov and H. B. Lawson, The classication of simply connected manifolds of positive scalar curvature, Annals of Math. 111 (1980), 423-434.

\[20\] V. Guillemin and A. Pollack, Dierential topology, Prentice-Hall, New York, 1974.

\[21\] J. Kollar, The structure of algebraic three-folds: an introduction to Mori’s program, Bull. Amer. Math. Soc. 17 (1987), 211-273.

\[22\] P. B. Kronheimer and T. S. Mrowka, The genus of embedded surfaces in the projective plane, Math. Research Letters 1 (1994), 797-808.

\[23\] S. Lang, Dierential and Riemannian manifolds, Springer Verlag, New York, 1995.

\[24\] H. B. Lawson and M. L. Michelsohn, Spin geometry, Princeton univ. Press, Princeton, New Jersey, 1989.

\[25\] V. Mathai and D. Quillen, Superconnections, Thom classes, and equiv- ariant dierential forms, Topology 25 (1986), 85-110.

\[26\] D. McDu and D. Salamon, J -holomorphic curves and quantum co- homology, American Mathematical Society, Providence, Rhode Island,

* * *

## BIBLIOGRAPHY 123

\[27\] J. Milnor, Morse theory, Princeton Univ. Press, Princeton, New Jersey,

\[28\] J. Milnor and D. Husemoller, Symmetric bilinear forms, Springer, New York, 1973.

\[29\] J. Milnor and J. Stashe, Characteristic classes, Princeton Univ. Press, Princeton, New Jersey, 1974.

\[30\] C. W. Misner, K. Thorne and J. A. Wheeler, Gravitation, W. H. Free- man, New York, 1973.

\[31\] J. Morgan, The Seiberg-Witten equations and applications to the topol- ogy of smooth four-manifolds, Princeton Univ. Press, Princeton, New Jersey, 1996.

\[32\] J. Morgan, Z. Szabo and C. Taubes, A product formula for the Seiberg- Witten invariants and the generalized Thom conjecture, J. Dierential Geometry 44(1996), 706-788.

\[33\] C. Okonek and A. Van de Ven, Stable vector bundles and dierentiable structures on certain elliptic surfaces, Inventiones Math. 86 (1986), 357-370.

\[34\] M. Peskin and D. Schroeder, An introduction to quantum eld theory, Perseus Books, Reading, Mass, 1995.

\[35\] S. Smale, An innite-dimensional version of Sard’s theorem, Amer. J. Math. 87 (1966), 861-866.

\[36\] N. Steenrod, The topology of ber bundles, Princeton Univ. Press, Princeton, New Jersey, 1951.

\[37\] C. Taubes, The Seiberg-Witten and Gromov invariants, Math. Re- search Letters 2 (1995), 221-238.

\[38\] C. Taubes, Seiberg-Witten and Gromov invariants for symplectic four- manifolds, International Press, Somerville, MA, 2000.

\[39\] F. W. Warner, Foundations of dierentiable manifolds and Lie groups, Scott-Foresman, Glenview, Illinois, 1971.

\[40\] G. W. Whitehead, Elements of homotopy theory, Springer Verlag, New York, 1978.

\[41\] E. Witten, Monopoles and four-manifolds, Math. Research Letters 1 (1994), 769-796.

* * *

Index

$A$, 35, 76
almost complex structure, 55
anticanonical bundle, 56, 108
anti-selfdual, 44
Atiyah-Singer Theorem, 70,72
$b\_0, b\_1, b\_2$, 43
$b\_+, b\_-$, 44
$B$, 36, 79
$B'$, 78
Bianchi identity, 18
$c\_1(E), c\_2(E)$, 24
canonical bundle, 107
Cech cohomology, 51
characteristic class, 22
Chern character, 22
Chern class, 24
$\\chi(\\Sigma), \\chi(M)$, 27, 69
Clifford algebra, 57
connected sum, 96
connection
orthogonal connection, 12
pullback connection, 14
spin connection, 60
unitary connection, 13
universal connection, 13
Yang-Mills connection, 45
covariant derivative, 9
curvature
curvature of a connection, 18
Gaussian curvature, 19
Riemann-Christoffel curvature,
63
scalar curvature, 63

$d\_A$, 10
$D\_A$, 65, 66
$D^+\_A$, $D^-\_A$, 69
$g\_A$, 41
$\\Delta$, 42, 82
de Rham cohomology, 17
Dirac operator, 65, 66
Dolgachev surface, 118
Donaldson's Theorem, 98
Eilenberg-MacLane space, 32
elliptic bootstrapping, 83
elliptic complex, 44
$F\_A$, 19
$F^+ _A$, 76_
_Faraday tensor, 39_
_Fredholm map, 84_
_$g_{ab}$, 4
$\\mathcal{G}$, $\\mathcal{G}\_0$, 35, 76
gauge transformation, 34, 78
geometric genus, 112
$H^P(M; R)$, 17
$H^P(M)$, 42
harmonic form, 42
Hermitian metric, 7, 55
Hirzebruch Signature Theorem, 73
Hodge star, 41
Hodge's Theorem, 42
holonomy, 38
hyperplane section bundle, 104
index
of elliptic operator, 69
of Fredholm map, 84
of section, 26 instanton, 45
intersection form, 92
j. 55
K3 surface, 96
Kähler form, 103
Kähler manifold, 103
L$^2\_E$(E), 80
Laplace operator
Hodge Laplacian, 42
vector bundle Laplacian, 67
Lichnerowicz's Theorem, 70
line bundle
complex line bundle, 5, 9
quaternionic line bundle, 6, 9
determinant line bundle, 89
M, M$\_p$, M$\_q$, 81
Maxwell's equations, 39
moduli space, 81
N, 87
ω, 103
Ω$^2$(M), 16
Ω$^2\_2$(M), Ω$^2\_2$(M), 44
orientation, 89
p$\_1$(E), 24
p$\_p$, 112
parallel transport, 15
Pauli matrices, 50
Poincaré duality, 43, 94
Poisson's equation, 42
Poutrign class, 24
Q, 92
quaternion, 6
regular value, 85
Rellich's Theorem, 80
ρ, 48
ρ'', 49
Riemann-Roch Theorem, 111
Rochlin's Theorem, 70
S, 77
S$\_p$, 113
Sard-Smale Theorem, 85
Seiberg-Witten equations, 76

Seiberg-Witten invariant, 101
self-dual, 44
σ(v), 59
signature, 44, 70
Sobolev Embedding Theorem, 80
Sobolev space, 80
spin manifold, 51
spin structure, 51
spin$^+$ structure, 52
Spin(4), 48
Spin(4)$^+$, 49
spinor field, 54
Stitch Whitney class, 51
SU$ _u$(2), SU$u$(2), 48_
_τ(M), 44_
_Thom conjecture, 2_
_Thom form, 25_
_Transversality Theorems, 86, 91_
_unimodular form, 94_
_Unique Continuation Theorem, 86_
_universal bundle, 13, 29_
_universal connection, 13_
_vector bundle, 4_
_virtual vector bundle, 54_
_w$2$(TM), 51_
_W${+}$, W${-}$, 50_
_W$_{+}$ $\\otimes$ L, W$\_{-}$ $\\otimes$ L, 52, 54
Weitzenbock's formula, 67
Written Theorems, 101, 112
y, 45
Yang-Mills functional, 45
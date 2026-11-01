---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Lecture Notes on Seiberg-Witten Invariants (Revised Second Edition)]

$$\\Phi = \\eta(t\_1^2+t\_2^2)\\Omega\_{12} - 2\\nu'(t\_1^2+t\_2^2)(dt\_1 + \\omega\_{12}t\_2) \\wedge (dt\_2 - \\omega\_{12}t\_1),$$ where $\\eta : \[0, \\infty) \\rightarrow R$ is any smooth function such that\
\
$$\\eta(0) = \\frac{1}{2\\pi}, \\quad \\eta(u) \\rightarrow 0 \\text{ sufficiently rapidly as } u \\rightarrow \\infty,$$\
\
thereby still obtaining a smooth two-form with the same key properties. The choice $\\eta(u) = (1/2\\pi)e^{-u}$ we made in (1.17) may simplify the calculations a little, but choosing $\\eta$ to vanish for $r \\geq \\epsilon$, where $\\epsilon$ is a small positive number, yields a Thom form with compact support, which vanishes outside an $e$-neighborhood of the zero section.\
\
Choice of a section $\\sigma : M \\rightarrow L$ does not affect the de Rham cohomology class of $\\sigma^ _(\\Phi)$, since any two sections are homotopic. Thus the cohomology class $\[\\sigma^_(\\Phi)\]$ equals its pullback via the zero section:\
\
$$\[\\sigma^\*(\\Phi)\] = \\frac{1}{2\\pi}\[\\Omega\_{12}\] = \\frac{1}{2\\pi}\[F\_A\] = c\_1(L).$$\
\
We now focus on the special case of a complex line bundle $L$ with Hermitian metric over a smooth oriented surface $\\Sigma$. We say that a smooth section $\\sigma : \\Sigma \\rightarrow L$ has a nondegenerate zero at $p \\in \\Sigma$ if $\\sigma(p) = 0$ and\
\
$\\sigma(\\Sigma)$ has transverse intersection with the zero section at $p$.\
\
Such an intersection has a sign, which is positive if and only if the orientations of the zero section and $\\sigma(\\Sigma)$ add up to give the orientation of the total space of $L$. If $p$ is a nondegenerate zero of $\\sigma$, the index of $\\sigma$ at $p$ is\
\
$$\\omega(\\sigma,p) = \\begin{cases} 1, & \\text{if the intersection at } p \\text{ is positive}, \ -1, & \\text{if the intersection is negative}. \\end{cases}$$\
\
Theorem. If $L$ is a complex unitary line bundle with unitary connection over a smooth compact oriented surface $\\Sigma$, and $\\sigma : \\Sigma \\rightarrow L$ is a section with only nondegenerate zeros, say at $p\_1, \\ldots, p\_k$, then\
\
$$\\sum\_{i=1}^{k} \\omega(\\sigma,p\_i) = \\frac{1}{2\\pi} \\int\_M F\_A = (c\_1(L), \[\\Sigma\]).$$\
\
Sketch of Proof: We consider the sections $\\sigma\_s = s\\sigma$ as the real number $s$ approaches $\\infty$. If $\\sigma\_i = t\_i \\circ \\sigma,$\
\
$$\\sigma\_s^\*\\Phi = \\frac{1}{2\\pi} e^{-s^2(\\sigma\_1^2 + \\sigma\_2^2)} \\left\[ \\Omega\_{12} + 2s^2(d\\sigma\_1 + \\omega\_{12}\\sigma\_2) \\wedge (d\\sigma\_2 - \\omega\_{12}\\sigma\_1) \\right\],$$\
\
* * *\
\
1.6. THE THOM FORM 27 an expression which goes to zero as s ! 1 except in very small neigh- borhoods V1;:::;Vkcentered at p1;:::;pk. We can arrange to choose the moving frame so that !12vanishes at each pi. Then\
Z X kZ 1(s 1 ) 2 (s2 2 ) lims= lim e d(s1) ^ d(s2): s!1 M s!1 V i i=1\
\
According to (1.18), the integral over Viin the sum must approach 1, depending upon whether the intersection of () with the zero section at piis positive or negative. Thus\
\
Z Z X k 1 FA= lims() =!(;pi); 2 s!1 i=1\
\
and our sketch of the proof is complete.\
\
For example, suppose that L = T the tangent bundle to a surface which possesses a Riemannian metric. A function f : M ! R is said to be a Morse function if the gradient rf of f (with respect to the Riemannian metric) has nondegenerate zeros. It is readily checked that the index of this gradient eld is one at every local maximum and local minimum, and minus one at every saddle point, so the sum of the indices at the critical points p1;:::;pkof f is\
\
X k !(rf;pi) = (# of maxima) (# of saddle points) + (# of minima): i=1\
\
According to the main theorem of Morse theory \[27\], the last sum on the right is the Euler characteristic () of . Thus the preceding theorem specializes to yield the Gauss-Bonnet formula for a surface: Z Z 1 1 hc1(T); \[\]i = FA= KdA = (); 2 2\
\
K : ! R being the Gaussian curvature of the surface. However, the theorem is far more general; when coupled with the notion of intersection number, it also yields a geometric interpretation of the rst Chern class of a complex line bundle over a higher-dimensional smooth manifold M. If and Z are two compact submanifolds of complemen- tary dimension in M which intersect transversely at nitely many points p1;:::;pk, we dene the intersection number of and Z at pito be\
\
1; if the orientations of TpiTpiZ and TpiM agree, I(;Z;pi) = 1; if these orientations disagree,\
\
* * *\
\
## 28 CHAPTER 1. PRELIMINARIES\
\
Pk and the intersection number of and Z isi=1I(;Z;pi). (The notion of intersection number is studied in more detail in books on dierential topology, such as \[20\].)\
\
Corollary. Suppose that L is a complex line bundle with Hermitian metric over a smooth manifold M and : M ! L is a section which has transverse intersection with the zero section. Let\
\
Z = 1 (zero section):\
\
If i :! M is an imbedding of an oriented surface in M which has transverse intersection with Z, then\
\
hc1(L); \[\]i = Intersection number of with Z :\
\
Sketch of Proof: The section pulls back to a section i of the line bundle i L over . The zeros of this pullback correspond exactly to the points of intersection of with Z. Moreover, if p is a point in the intersection \ Z, !(i ;p) is just the intersection number of with Z at p.\
\
A similar interpretation is possible for the second Chern class for a quater- nionic line bundle over a compact oriented four-manifold M. The Thom form needed for that case is constructed in \[25\].\
\
# 1.7 The universal bundle\
\
An alternative approach to the construction of characteristic classes relies on the universal bundle construction. Suppose that\
\
## z = (z1;z2;:::;zi;:::); w = (w1;w2;:::;wi;:::)\
\
are nonzero elements of innite-dimensional complex Hilbert space C1. We say that z and w are equivalent, written z w, if\
\
z i= wi; for some 2 C f0g:\
\
Let \[z\] = \[z1;z2;:::;zi;:::\] denote the resulting equvalence class of z, P1C the set of equivalence classes. We call P1C innite-dimensional complex projective space. It is not dicult to show that P1C satises the denition of innite- dimensional smooth Hilbert manifold, as described for example in \[23\]. Indeed, one can contruct a countable atlas of smooth charts\
\
## f(U1;1); (U2;2);:::g\
\
* * *\
\
1.7. THE UNIVERSAL BUNDLE\
\
by setting\
$U\_i = {\[z\_1, z\_2, \\dots\] \\in P^\\infty \\mathbb{C}: z\_i \\neq 0}$,\
and defining $\\phi\_i : U\_i \\rightarrow \\mathbb{C}^\\infty$ by\
$\\phi\_i(\[z\_1, z\_2, \\dots\]) = \\left(\\frac{z\_1}{z\_i}, \\frac{z\_2}{z\_i}, \\dots, \\frac{z\_{i-1}}{z\_i}, \\frac{z\_{i+1}}{z\_i}, \\dots\\right)$.\
\
It is quickly verified that\
$\\phi\_j \\circ (\\phi\_i)^{-1} : \\phi\_i(U\_i \\cap U\_j) \\rightarrow \\phi\_j(U\_i \\cap U\_j)$\
is smooth, just as in the case of finite-dimensional projective space.\
We can regard $P^\\infty \\mathbb{C}$ as the space of one-dimensional subspaces $V \\subset \\mathbb{C}^\\infty$.\
There is a universal bundle over $P^\\infty \\mathbb{C}$ whose total space is\
$E\_\\infty = {(V, (z\_1, z\_2, \\dots)) \\in P^\\infty \\mathbb{C} \\times \\mathbb{C}^\\infty : (z\_1, z\_2, \\dots) \\in V}$.\
\
(Note that $E\_\\infty$ minus the zero section is just $\\mathbb{C}^\\infty - {0}$.) The trivialization\
$\\psi\_i : \\pi^{-1}(U\_i) \\rightarrow U\_i \\times \\mathbb{C}$ over $U\_i$ is defined by\
$\\psi\_i(V, (z\_1, z\_2, \\dots)) = (V, z\_i)$,\
\
and the transition functions corresponding to the covering ${U\_1, U\_2, \\dots}$ are\
$g\_{ij} : U\_i \\cap U\_j \\rightarrow GL(1, \\mathbb{C}), \\quad g\_{ij} = \\frac{z\_i}{z\_j}$.\
\
We have just described a special case of a more general construction.\
Just like infinite-dimensional projective space, the infinite Grassmannian\
$G\_m(\\mathbb{C}^\\infty) = {m$-dimensional complex subspaces of $\\mathbb{C}^\\infty}$\
\
is an infinite-dimensional smooth manifold, and\
$E\_\\infty = {(V,v) \\in G\_m(C^\\infty) \\times \\mathbb{C}^\\infty : v \\in V}$\
\
is the total space of a smooth vector bundle over $G\_m(C^\\infty)$, called the universal bundle. Trivializations and transition functions for this bundle are described in standard references, such as \[29\].\
If $M$ is a smooth manifold, we let $\[M,G\_m(C^\\infty)\]$ denote the space of homotopy classes of maps from $M$ to $G\_m(C^\\infty)$.\
\
Universal Bundle Theorem. If $M$ is a smooth manifold, there is a bijection\
$\\Gamma : \[M,G\_m(C^\\infty)\] \\rightarrow \\text{Vect} _m^{\\mathbb{C}}(M)$ defined by $\\Gamma(F) = F^\* E_\\infty$.\
\
Sketch of proof: First note that Proposition 2 from §1.3 shows that $\\Gamma$ is well-defined.\
\
To see that $\\Gamma$ is surjective, suppose that $(E, \\pi)$ is a smooth complex vector bundle of rank $m$ over $M$. We claim that if $M$ has dimension $n$, it can be covered by $n + 1$ open sets ${U\_0, U\_1, \\dots, U\_n}$ whose components are contractible. Indeed, let ${s^i\_i : i \\in I}$ denote the $k$-simplices in a simplical decomposition of $M$. Each $k$-simplex $s^i\_k$ has a barycenter $b^i\_k$ which is a zero-simplex in the first barycentric subdivision. Let $U\_k$ be the union of the open stars of all the barycenters $b^i\_k$ in the first barycentric subdivision. Then ${U\_0, U\_1, \\dots, U\_n}$ is a covering of $M$ and although $U\_k$ is not connected, each component of $U\_k$ is contractible.\
\
By the Corollary at the end of §1.3, we can use this covering as a trivializing covering for the bundle $E$. Let\
\
$$\\psi\_k : \\pi^{-1}(U\_k) \\rightarrow U\_k \\times C^m$$\
\
be the trivialization over $U\_k$, and compose it with projection on the second factor to obtain\
\
$$\\eta\_k = \\pi\_2 \\circ \\psi\_k : \\pi^{-1}(U\_k) \\rightarrow C^m.$$\
\
Finally, let ${\\zeta\_0, \\zeta\_1, \\dots, \\zeta\_m}$ be a partition of unity subordinate to the open cover and define $\\tilde{F}: E \\rightarrow C^{n+1}m \\subset C^\\infty$ by\
\
$$\\tilde{F}(e) = (\\zeta\_0(\\pi(e))n\_0(e), \\zeta\_1(\\pi(e))n\_1(e), \\dots, \\zeta\_m(\\pi(e))n\_m(e)).$$\
\
Since $\\tilde{F}$ is injective on each fiber, it induces a continuous map $F: M \\rightarrow G\_m(C^\\infty)$ such that $F(p) = \\tilde{F}(E\_p)$. It is easily proven that $F^\* E\_m = E$, and surjectivity is established.\
\
Before proving injectivity we need some preliminaries. Let\
\
$$C^\\infty = {(z\_1, z\_2, z\_3, z\_4, \\dots) \\in C^\\infty : z\_1 = 0, z\_2 = 0, \\dots},$$\
\
the set of elements in $C^\\infty$ in which only the even components can be nonzero,\
\
$$C^\\infty = {(z\_1, z\_2, z\_3, z\_4, \\dots) \\in C^\\infty : z\_2 = 0, z\_3 = 0, \\dots},$$\
\
the set of elements in which only the odd components can be nonzero. Define linear maps\
\
$$\\tilde{T}\_e : C^\\infty \\rightarrow C\_e^\\infty, \\quad \\tilde{T}\_o : C^\\infty \\rightarrow C\_o^\\infty$$\
\
by\
\
$$\\tilde{T}\_e(z\_1, z\_2, z\_3, z\_4, \\dots) = (0, z\_1, 0, z\_2, \\dots),$$\
\
* * *\
\
1.7. THE UNIVERSAL BUNDLE\
\
$$\\tilde{T}\_o(z\_1, z\_2, z\_3, z\_4, \\dots) = (z\_1, 0, z\_2, 0, \\dots).$$\
\
These induce maps\
\
$$T\_e : G\_m(\\mathbb{C}^\\infty) \\rightarrow G\_m(\\mathbb{C}^\\infty) \\subset G\_m(\\mathbb{C}^\\infty),$$\
\
$$T\_o : G\_m(\\mathbb{C}^\\infty) \\rightarrow G\_m(\\mathbb{C}^\\infty) \\subset G\_m(\\mathbb{C}^\\infty).$$\
\
which we claim are homotopic to the identity. Indeed, we can define\
\
$$\\tilde{H}\_e : \\mathbb{C}^\\infty \\times \[0, 1\] \\rightarrow \\mathbb{C}^\\infty$$ by $$\\tilde{H}\_e(\\mathbf{z}, t) = tz + (1 - t)\\tilde{T}\_e(z).$$\
\
If $z\_1, \\dots, z\_k$ are linearly independent elements of $\\mathbb{C}^\\infty$, then so are\
\
$$\\tilde{H}(\\mathbf{z}\_1, t), \\dots, \\tilde{H}(\\mathbf{z}\_k, t)$$\
\
for every choice of $t \\in \[0, 1\].$ Hence $\\tilde{H}\_e$ induces a homotopy\
\
$$H\_e : G\_m(\\mathbb{C}^\\infty) \\times \[0, 1\] \\rightarrow G\_m(\\mathbb{C}^\\infty)$$\
\
from $T\_e$ to the identity. A similar construction gives a homotopy from $T\_o$ to the identity.\
\
To see that $\\Gamma$ is injective, we need to show that if $F: G : M \\rightarrow G\_m(\\mathbb{C}^\\infty)$ are two smooth maps such that $F^\* E\_\\infty = G^\* E\_\\infty$, then $F$ and $G$ are homotopic. To do this, it suffices to show that $T\_e \\circ F$ and $T\_o \\circ G$ are homotopic. But the maps $T\_e \\circ F$ and $T\_o \\circ G$ are covered by\
\
$$\\tilde{T}\_e \\circ \\tilde{F}: E \\rightarrow \\mathbb{C}^\\infty, \\quad \\tilde{T}\_o \\circ \\tilde{G}: E \\rightarrow \\mathbb{C}^\\infty.$$\
\
We can define\
\
$$\\tilde{H}: E \\times \[0, 1\] \\rightarrow \\mathbb{C}^\\infty$$ by $$\\tilde{H}(e, t) = t\\tilde{T}\_e \\circ \\tilde{F}(e, t) + (1 - t)\\tilde{T}\_o \\circ \\tilde{G}(e, t).$$\
\
Then $\\tilde{H}\[(E\_p \\times {t})\]$ is a vector space monomorphism for each $(p, t) \\in M \\times \[0, 1\],$ and hence $\\tilde{H}$ induces a continuous map\
\
$$H: M \\times \[0, 1\] \\rightarrow G\_m(\\mathbb{C}^\\infty), \\quad H(p, t) = \\tilde{H}\[(E\_p \\times {t}).$$\
\
This map is the desired homotopy from $F$ to $G$, and injectivity of $\\Gamma$ is established.\
\
We will use the preceding theorem in the case where $m = 1$ to classify complex line bundles. We need a few facts about the homotopy and homology groups of $G\_1(\\mathbb{C}^\\infty) = P^\\infty C$, facts that are worked out in books on algebraic topology. We refer the reader to standard references, such as \[36\] or \[40\] for the few topological results that we need.\
\
* * *\
\
## 32 CHAPTER 1. PRELIMINARIES\
\
First of all, the universal bundle restricts to a ber bundle with ber C f0g, C f0g! (C1 f0g) ! P1C;\
\
which yields an exact homotopy sequence (as described in \[36\], x17)\
\
!k(C1 f0g) !k(P1C) !k 1(C f0g) !k 1(C1 f0g) ! (1.19) Now C1 f0g is homotopy equivalent to an innite-dimensional sphere, and just ask(S n\
\
) = 0 for k < n, the k-th homotopy group of an innitedimensional sphere must vanish for all k. Thusk(C1 f0g) = 0 for all k > 0 and hence n (P1(C)) = (C f0g) = Z if k = 2, k k 1 0 otherwise.\
\
In other words, P1(C) is a K(Z; 2), an Eilenberg-MacLane space (as de- scribed on pages 244-250 of \[40\]). On the other hand, this Eilenberg-MacLane space has the remarkable property (\[40\], page 250) that if M is any smooth manifold,\
\
\[M;K(Z; 2)\] = fhomotopy classes of maps M ! K(Z; 2)g = H2(M; Z):\
\
Combining this with the isomorphism of the Universal Bundle Theorem yields a bijection Vect C 1(M) = H2(M; Z): (1.20)\
\
This proves the Classication Theorem for Complex Line Bundles stated in x1.2. The mapping that realizes the isomorphism (1.20) is (up to sign) just an integral version of the rst Chern class. To see this, we could use the theory of dierential forms on innite-dimensional smooth manifolds, to- gether with the corresponding version of de Rham cohomology. Using this theory we could dene a connection on the line bundle E1 and the rst Chern class c1(E1) 2 H2(P1(C); R). Naturality would then imply that\
\
c1(E) = F (c1(E1)); where (F) = E:\
\
Alternatively, we can avoid working with innite-dimensional manifolds by using N -dimensional projective space P N\
\
(C) as a nite-dimensional\
approximation to P1(C). The argument for the Universal Bundle Theorem shows that for line bundles over M it suces to take N = dim M + 1.\
\
* * *\
\
1.7. THE UNIVERSAL BUNDLE\
\
Let's adopt the second procedure and put two homotopy sequences like (1.19) together to obtain\
\
$$\\cdots \\rightarrow \\pi\_2(\\mathbb{C}^2 - {0}) \\rightarrow \\pi\_2(P^1(\\mathbb{C})) \\rightarrow \\pi\_1(\\mathbb{C} - {0}) \\rightarrow \\cdots$$\
\
$$\\downarrow \\quad \\downarrow \\quad \\downarrow$$\
\
$$\\cdots \\rightarrow \\pi\_2(\\mathbb{C}^{N+1} - {0}) \\rightarrow \\pi\_2(P^N(\\mathbb{C})) \\rightarrow \\pi\_1(\\mathbb{C} - {0}) \\rightarrow \\cdots.$$\
\
Since $\\pi\_1(\\mathbb{C}^2 - {0}) \\cong \\pi\_1(\\mathbb{C}^{N+1} - {0}) \\cong 0$ for $i = 1$ or 2, application of the five-lemma shows that the top horizontal arrow in the diagram\
\
$$\\pi\_2(P^1(\\mathbb{C})) \\rightarrow \\pi\_2(P^N(\\mathbb{C}))$$\
\
$$\\downarrow \\quad \\downarrow$$\
\
$$H\_2(P^1(\\mathbb{C}); \\mathbb{Z}) \\rightarrow H\_2(P^N(\\mathbb{C}); \\mathbb{Z})$$\
\
is an isomorphism. The vertical arrows are isomorphisms by the Hurewicz isomorphism theorem (\[36\], page 79), so the bottom horizontal arrow is also an isomorphism. The universal coefficient theorem then shows that the maps\
\
$$H^2(P^1(\\mathbb{C}); \\mathbb{Z}) \\rightarrow H^2(P^N(\\mathbb{C}); \\mathbb{Z})$$ and $$H^2(P^1(\\mathbb{C}); \\mathbb{R}) \\rightarrow H^2(P^N(\\mathbb{C}); \\mathbb{R})$$\
\
(1.21)\
\
are both isomorphisms.\
\
Let $E\_\\infty$ denote the universal bundle over $P^N(\\mathbb{C})$, a line bundle with total space\
\
$$E\_\\infty = {(V, z\_1, \\ldots, z\_{N+1}) \\in P^N\\mathbb{C} \\times \\mathbb{C}^N : (z\_1, \\ldots, z\_{N+1}) \\in V}.$$ (1.22)\
\
We claim that $c\_1(E\_\\infty)$ is the image under the coefficient homomorphism\
\
$$H^2(P^N(\\mathbb{C}); \\mathbb{Z}) \\rightarrow H^2(P^N(\\mathbb{C}); \\mathbb{R})$$\
\
of a generator of $H^2(P^N(\\mathbb{C}); \\mathbb{Z})$. Because of the isomorphisms (1.21) it suffices to check this for the universal bundle $H^{-1}$ over $P^1(C) = S^2$. But the Gauss-Bonnet theorem implies that\
\
$$c\_1(H^2)\[S^2\] = c\_1(TS^2)\[S^2\] = \\int\_{S^2} (1/2\\pi)KdA = 2.$$\
\
Recall that by Proposition 4 from §1.5, if $L\_1$ and $L\_2$ are line bundles,\
\
$$c\_1(L\_1 \\otimes L\_2) = c\_1(L\_1) + c\_2(L\_2).$$\
\
* * *\
\
## 34 CHAPTER 1. PRELIMINARIES\
\
Hence c1(H)\[S2\] = 1 and c1(H 1\
\
)\[S2\] = 1.\
Using naturality, we see that under the isomorphism (1.20),\
\
F E1 7! F 2 \[M;P1(C)\] 7! F (generator of H2(P1(C); Z)):\
\
This element of H2(M; Z) maps to c1(E) under the coecient homomor- phism. In particular, the rst Chern class of a line bundle E over any smooth manifold M is \\quantized"; c1(E) integrates to an integer over any two-dimensional cycle in M. There is a real version of the Universal Bundle Theorem which is proven by exactly the same method: If M is a smooth manifold, there is a bijection\
\
: \[M;Gm(R1)\] ! Vect R m(M)\
\
dened by (F) = F E1, where E1 is the universal bundle dened over the real Grassmannian Gm(R1). Just as in the case of the rst Chern class, higher degree Chern classes and Pontrjagin classes can be dened by pulling back Chern or Pontrjagin classes of universal bundles over Gm(C1) or Gm(R1). Using cohomology with Z2-coecients, one can also dene Stiefel-Whitney classes. Details of these constructions can be found in \[29\]. There is also a version of the Universal Bundle Theorem for quaternionic bundles which can be used to prove the Classication Theorem for Quater- nionic Line Bundles from x1.2. If P1(H) denotes innite-dimensional quaternionic projective space, then just as in the complex case there is a bijection\
\
: \[M;P1(H)\] ! Vect H 1(M):\
\
Unfortunately, unlike the complex case, this quaternionic projective space is not an Eilenberg-MacLane space. Nevertheless, a homotopy sequence argument shows that it does satisfy the weaker condition\
\
(P1(H)) = (H f0g) = Z if k = 4, k k 1 0 if 0 k 3.\
\
This is sucient to show that\
\
fhomotopy classes of maps M ! P1(H)g = H4(M; Z);\
\
when M is a manifold of dimension 4, thereby establishing the Classi- cation Theorem for Quaternionic Line Bundles.\
\
* * *\
\
1.8. CLASSIFICATION OF CONNECTIONS 35\
\
# 1.8 Classication of connections\
\
Now that we have classied the complex line bundles over a smooth mani- fold M, we turn to the problem of classifying the unitary connections in a given complex line bundle L over M. At rst glance, the classication might appear to be trivial. Indeed, we claim that if dA0is a unitary connection on L, chosen as base point, then any unitary connection on L can be written uniquely in the form\
\
dA0ia; where a 2 1\
\
(M): (1.23)\
To establish the claim, we work rst in a local trivialization, in terms of which the connection dA0takes the form\
\
(dA0) = d + !;\
\
where ! is a purely imaginary one-form on U. The local representative of any other unitary connection in L is\
\
(dA) = d + ! ia;\
\
where a is a real-valued one-form on U. Using the formula (1.8) one quickly veries that\
\
a = a on the overlap U \ U;\
\
Thus the a ’s t together into a real-valued one form a on M and (1.23) holds. In other words, the space A of unitary connections on L is an \\ane space," isomorphic to the space of one-forms on M. However, we really want to classify connections up to isomorphism, also known as gauge equivalence. In the case of U (1)-bundles, a gauge transformation of L is just a smooth map g : M ! S1, where S1 is regarded as the complex numbers of length one. A gauge transformation induces a vector bundle isomorphism g : L ! L, g acting by scalar multiplication. Conversely, any vector bundle isomorphism of L over M which preserves the Hermitian metric can be regarded as a gauge transformation. Let G denote the a space of gauge transformation, a group under mul- tiplication in S1. If p0 is some choice of base point in M, let\
\
G0 = fg 2G : g(p0) = 1g:\
\
Elements of G0 are called based gauge transformations. We have a direct product of groups, G = G0 S1;\
\
* * *\
\
## 36 CHAPTER 1. PRELIMINARIES\
\
where S1 is the group of constant gauge transformations. Gauge transformations act on connections by conjugation,\
\
(g;dA) 7! g dAg 1 = da+ gd(g 1 ):\
\
Constant gauge transformations act trivially on the space A, while the group G0 acts freely. Thus the space of equivalence classes of connections on L is B = A=G = A=G0:\
\
It is easy to describe the topology of these spaces. (To be precise, we should complete the spaces A and G with respect to suitable norms, such as C k norms or the Sobolev norms that will be described in more detail in x3.2.) In the case where M is simply connected any based gauge transformation g : M ! S1; g(p0) = 1;\
\
has a global logarithm; it can be written in the form\
\
g = e iu ; where u : M ! R; u(p0) = 0:\
\
Since the space of maps from M to R is contractible, so is G0, and hence G is homotopy equivalent to S1. In this case, since A and G0 are both contractible, so is the space B of connections. Suppose that M is not simply connected. Since S1 is a K(Z; 1), the theorem on Eilenberg-MacLane spaces cited earlier implies that\
\
\[M;S1\] = f homotopy classes of maps M ! S1 g = H1(M; Z):\
\
Thus the components of G0 are in one-to-one correspondence with Z b 1 , each component being contractible by an argument similar to that given for the simply connected case. The exact homotopy sequence of the bration\
\
G0!A!B\
\
then shows that each connected component of B is a K(G; 1), where G = H1(M; Z). For example, if H1(M; Z) has no torsion (which always happens for compact oriented manifolds by Poincare duality), it is a free abelian group on b1 generators, where b1 is the rst Betti number of M, and each component of B is homotopy equivalent to a torus of rank b1. Actually, there is also a far more concrete description of B, which comes from asking the question: If F is an ordinary real-valued two-form on M, when is = iF the curvature of a unitary connection in some line bundle over M ?\
\
* * *\
\
1.8. CLASSIFICATION OF CONNECTIONS 37 One necessary condition is that F satisfy the Bianchi identity\
\
## dF = 0:\
\
From the previous section, we also know that the de Rham cohomology class of (1=2)F must lie in the image of the coecient homomorphism\
\
## H2(M; Z) ! H2(M; R):\
\
We claim that these two conditions are sucient. Assume rst that M is simply connected. Let L be a complex line bundle over M and let C denote the space of closed two-forms on M which represent the rst Chern class of L. Dene\
\
1 : B!C by (\[A\]) = FA; 2\
\
where iFAis the curvature of A. We claim that is an isomorphism. To see that is surjective, choose a unitary connection A0 on L to serve as base point. If F is any element of C, we can write\
\
F FA0= da;\
\
where a is a real-valued one-form on M. Then dA= dA0ia is a unitary connection on L which has curvature iF. To see that is injective, note that if\
\
## dA0ia1 and dA0ia2\
\
are two unitary connections on L which have the same curvature, then da1 = da2. Since H1(M; R) = 0 by hypothesis,\
\
a1 a2 = d; for some : M ! R such that (p0) = 0.\
\
Then e i : M ! S1 is a gauge transformation such that\
\
dA0ia1 = e i (dA0ia2) (e i ) 1 ;\
\
and hence the two connections are gauge equivalent. It is possible to establish a similar result when M is not simply con- nected. Suppose, for simplicity, that1;:::;b1are oriented smooth simple closed curves representing generators for the free part of H1(M; Z), all pass- ing through a given point p0 2 M. Given a unitary connection dA2A, parallel translation aroundidenes an isomorphism\
\
i: Lp0! Lp0:\
\
* * *\
\
## 38 CHAPTER 1. PRELIMINARIES\
\
Since the connection is assumed to be unitary, the isomorphismiis simply a rotation through some angle\
\
= e i (A) i ; i\
\
which is invariant under gauge transformations. This isomorphismiis called the holonomy aroundi. Holonomy and curvature completely determine a unitary connection in a complex line bundle:\
\
Theorem on Classication of Connections. If H1(M; Z) is free abelian of rank b1, the map\
\
b1 z}\| { : B!C S1 S1;\
\
dened by 1i 1\
\
(A) ib1(A)\
(\[A\]) = FA;e;:::;e; 2\
\
## is a bijection.\
\
To see that is injective, suppose that\
\
## dA0ia1 and dA0ia2\
\
are two unitary connections on L which have the same curvature and holon- omy. Let M~ be the universal cover of M, ~~a1 and ~a2 the pullbacks of a1 and a2 to the universal cover. Then da~~ 1= da~2and hence\
\
a ~~1a~~ 2= d;~ for some ~ : M~ ! R.\
\
Using the fact that the two connections have the same holonomy, one can i ~~1 i 1 check that the map e : M! S descends to a map e : M ! S such that dA0ia1 = e i (dA0ia2) (e i ) 1 ;\
\
and hence the two connections are gauge equivalent. To see that is surjective, we rst note that if (1=2)FArepresents c1(L), then FAFA0is exact, so there is a smooth one-form a such that the connection dA0ia has curvature FA. Moreover, we can add a closed one-form to a with arbitrary periods over1;:::;b1without changing the curvature. Thus we can arrange that the connection dA0ia not only has curvature FA, but also has any prescribed holonomy around each curve 1 ;:::;b1.\
\
* * *\
\
1.8. CLASSIFICATION OF CONNECTIONS 39 Example. Suppose that is a Riemann surface of genus g and E is the trivial complex line bundle over . Then H1(;Z) = Z\
2g , and this Classication Theorem implies that the at connections in E are in one- to-one correspondence with a torus S1 S1 with 2g factors. In the theory of Riemann surfaces, this torus is called the Picard variety of .\
\
The Classication Theorem has an interesting application to electricity and magnetism. Recall that in general relativity (as explained for example in \[30\]), space-time is a four-dimensional manifold with a pseudo-Riemannian metric of Lorentz signature. It can be proven that any point p in such a manifold lies in a normal coordinate system (x0;x1;x2;x3) = (t;x;y;z) in terms of which the metric is expressed as\
\
X3 ds2 = dt2 + dx2 + dy2 + dz2 + hijdx i dx j ; i;j=0\
\
where hij(p) = 0 and dhij(p) = 0. What is the right form for Maxwell’s equations (the equations of elec- tricity and magnetism) on such a manifold? It turns out that Maxwell’s equations can be expressed quite nicely in terms of dierential forms, in a way that carries over to curved space-time. In the case of at space-time with coordinates (t;x;y;z), we set\
\
F = Exdt ^ dx Eydt ^ dy Ezdt ^ dz\
\
+Bxdy ^ dz + Bydz ^ dx + Bzdx ^ dy;\
\
where E = (Ex;Ey;Ez) and B = (Bx;By;Bz)\
\
are the electric and magnetic elds. We agree to call the two-form F the Faraday tensor. Then two of Maxwell’s equations,\
\
@B div(B) = 0; curl(E) + = 0; @t\
\
can be expressed in the simple equation\
\
## dF = 0:\
\
The other two Maxwell equations utilize the \\Hodge star," a linear operator ? : 2 T M ! 2 T M, which interchanges the role of E and B:\
\
?F = Bxdt ^ dx + Bydt ^ dy + Bzdt ^ dz\
\
* * *\
\
## 40 CHAPTER 1. PRELIMINARIES\
\
+Exdy ^ dz + Eydz ^ dx + Ezdx ^ dy:\
\
The remaining Maxwell equations are (with appropriate choice of units)\
\
@E div(E) = ; curl(B) = J; @t\
\
where is the charge density and J = (Jx;Jy;Jz) is the current density. This pair of equations can be reexpressed as\
\
## d?F =\
\
where\
\
= dx ^ dy ^ dz Jxdt ^ dy ^ dz Jydt ^ dz ^ dx Jzdt ^ dx ^ dy:\
\
The exterior derivative operator and the Hodge star can be dened on an arbitrary pseudo-Riemannian manifold of Lorentz signature. Thus as described in more detail in \[30\], Chapter 4, Maxwell’s equations can be formulated in terms of the Faraday tensor on the curved space-times of general relativity as dF = 0; d?F = :\
\
We can now ask the question: When is F = FA, where iFAis the curvature of a unitary connection dAon some line bundle L over M with Hermitian metric? Note that since F is closed, it represents a cohomology class \[F\] 2 H2(M; R). The preceding theorem states that iF is the cur- vature of a unitary connection precisely when this cohomology class lies in the image of coecient homomorphism\
\
## H2(M; Z) ! H2(M; R):\
\
This fact can be interpreted as requiring quantization of magnetic charge. What does one gain by regarding the electromagnetic eld as a uni- tary connection on a line bundle instead of as merely a two-form? First, a connection gives a family of one-forms, the \\electromagnetic gauges," which are useful for solving Maxwell’s equations in terms of a locally de- ned gauge. Second, the connection allows for holonomy around closed curves, which might be detected experimentally (the Bohm-Aharonov ef- fect). Third, regarding the electromagnetic eld as a connection suggests fruitful generalizations to other structure groups which may help explain other basic forces (such as weak and strong interactions). Indeed, this is the basis for the standard model for interactions between elementary particles, which isdescribed in \[34\], for example.\
\
* * *\
\
1.9. HODGE THEORY 41\
\
# 1.9 Hodge theory\
\
The Hodge star, which is used to formulate Maxwell’s equations in the case of metrics of Lorentz signature, also plays an important role in four- manifolds with positive-denite Riemannian metrics. Let p be a point in an oriented four-dimensional Riemannian manifold M and let V = TpM. We can use the Riemannian metric to identify V with the cotangent space TpM. If (e1;e2;e3;e4) is a positively oriented orthonormal basis for V, then\
\
e1 ^ e2; e1 ^ e3; e1 ^ e4; e2 ^ e3; e2 ^ e4; e3 ^ e4\
\
forms an orthonormal basis for 2\
\
V. We dene the Hodge star\
? 2 V! 2 V\
\
by ?(ei^ ej) = er^ es;\
\
whenever (i;j;r;s) is an even permutation of (1; 2; 3; 4). More generally, we dene the Hodge star\
\
? p V! 4 p V\
\
by ?1 = e1 ^ e2 ^ e3 ^ e4;?ei= er^ es^ et;\
\
where (i;r;s;t) is an even permutation of (1; 2; 3; 4), and so forth. The Hodge star is invariant under the action of the orthogonal group and satis- es the identity ? 2 = ( 1) p on p-forms. If M is compact, we can use the Hodge star to dene a bilinear form Z ( ;) : p\
\
(M) p\
(M) ! R by (!;) =! ^ ?:\
M\
\
It is easily veried that this bilinear form is symmetric and positive-denite, and hence it is an inner product on p\
\
(M). We can use the Hodge star to\
dene the codierential\
\
=?d? : p\
\
(M) ! p 1\
(M);\
which is the formal adjoint of the exterior derivative, as one veries by the calculation, Z Z Z (d!;) = d! ^ ? = d(! ^ ?) ( 1) p ! ^ d(?) M M M\
\
* * *\
\
## 42 CHAPTER 1. PRELIMINARIES\
\
Z Z =! ^ (??d?) =! ^ ? = (!;); M M where p = deg !. Finally, we can dene the Hodge Laplacian\
\
= d + d : p\
\
(M) ! p\
(M):\
In the case of 0\
\
(M), the Hodge Laplacian reduces to the standard Laplace\
operator on functions. Using the fact that d and are formal adjoints of each other, we nd that on a compact manifold M without boundary,\
\
(!;!) = ((d + d)!;!) = (!;!) + (d!;d!) 0:\
\
On such a manifold,\
\
! = 0, (!;!) = 0, d! = 0 and! = 0:\
\
These last two equations can be thought of as analogs of Maxwell’s equa- tions in the case where the charge density and current density vanish.\
\
Denition. A dierential p-form ! on a smooth oriented Riemannian man- ifold M is harmonic if ! = 0. Let H p\
\
(M) denote the space of harmonic\
p-forms on M.\
\
Hodge’s Theorem. Every de Rham cohomology class on a compact ori- ented Riemannian manifold M possesses a unique harmonic representative. Thus H p (M; R) = H p\
\
(M):\
Moreover, H p\
\
(M) is nite-dimensional and\
p\
\
(M) possesses direct sum\
decompositions\
\
p\
\
(M) = H p\
(M) (\
p\
\
(M)) = H p\
(M) d( p 1\
(M)) (\
p+1\
\
(M));\
which are orthogonal with respect to the inner product ( ;).\
\
For the proof, we refer the reader to Chapter 6 of \[39\].\
\
One nice application of Hodge’s Theorem is to existence of solutions to Poisson’s equation f = g:\
\
If M is connected, then the space H0(M) of harmonic zero-forms is just the space of constant functions. Thus Hodge’s Theorem implies that if the smooth function g : M ! R is orthogonal to the constant functions with\
\
* * *\
\
1.9. HODGE THEORY\
\
repeat to ( , ), then $g = \\Delta f$ for some smooth function $f$. Of course, $g$ is orthogonal to the constant functions if and only if its average value is zero,\
\
$$\\int\_M g \* 1 = 0.$$\
\
A second application of Hodge's Theorem is to topology. Since $\\star$ takes harmonic forms to harmonic forms, we see that if $M$ is a compact oriented Riemannian manifold without boundary,\
\
$$\\mathcal{H}^p(M) \\cong \\mathcal{H}^{n-p}(M),$$\
\
and hence one has an isomorphism of de Rham cohomology,\
\
$$H^p(M; \\mathbb{R}) \\cong H^{n-p}(M; \\mathbb{R}).$$\
\
This isomorphism is known as Poincaré duality for cohomology with real coefficients.\
\
Algebraic topology texts prove a more refined version of Poincaré duality for integer coefficients: If $M$ is a compact oriented $n$-manifold,\
\
$$H\_p(M; \\mathbb{Z}) \\cong H^{n-p}(M; \\mathbb{Z}).$$\
\
Together with the universal coefficients theorem, this puts strong restrictions on the homology of $M$. If\
\
$$H\_p(M; \\mathbb{Z}) = F\_p \\oplus T\_p,$$\
\
where $F\_p$ is free abelian and $T\_p$ is torsion, then\
\
$$F\_p \\cong F\_{n-p}$$ and $T\_p \\cong T\_{n-p-1}.$$\
\
In particular, if $M$ is a compact oriented four-manifold all the torsion in the homology of $M$ is determined by $T\_1 \\cong T\_2$ and $H\_3(M; \\mathbb{Z})$ is automatically free abelian.\
\
If $b\_p$ denotes the $p$-th Betti number of $M$, defined by $b\_p = \\dim H^p(M; \\mathbb{R})$, then Poincaré duality implies that $b\_p = b\_{n-p}$. The Betti numbers of a compact oriented four-manifold are determined by $b\_0$ (which is 1 if $M$ is connected), $b\_1$ (which is 0 if $M$ is simply connected) and $b\_2$. The second Betti number $b\_2$ possesses a further decomposition, which we now describe.\
\
Since $\\star^2 = 1$ on two-forms, we can divide $\\Lambda^2 V$ into a direct sum,\
\
$$\\Lambda^2 V = \\Lambda\_+^2 V \\oplus \\Lambda\_-^2 V,$$\
\
where\
\
$$\\Lambda\_+^2 V = {\\omega \\in \\Lambda^2 V : \\star \\omega = \\omega},$$\
\
$$\\Lambda\_-^2 V = {\\omega \\in \\Lambda^2 V : \\star \\omega = -\\omega}.$$\
\
* * *\
\
Thus $A\_2^2 V$ is generated by\
\
$$e\_1 \\wedge e\_2 + e\_3 \\wedge e\_4, \\quad e\_1 \\wedge e\_3 + e\_4 \\wedge e\_2, \\quad e\_1 \\wedge e\_4 + e\_2 \\wedge e\_3.$$\
\
while $A\_2^2 V$ is generated by\
\
$$e\_1 \\wedge e\_2 - e\_3 \\wedge e\_4, \\quad e\_1 \\wedge e\_3 - e\_4 \\wedge e\_2, \\quad e\_1 \\wedge e\_4 - e\_2 \\wedge e\_3.$$\
\
Sections of the bundles whose fibers are $A\_2^2 V$ and $A\_2^2 V$ are called self-dual and anti-self-dual two-forms respectively. If $\\omega$ is any smooth two-form on $M$, it can be divided into two orthogonal components,\
\
$$\\omega^+ = P\_+(\\omega) = \\frac{1}{2}(\\omega + \*\\omega) \\in \\Omega\_+^2(M) = { \\text{self-dual two-forms on } M },$$\
\
$$\\omega^- = P\_-(\\omega) = \\frac{1}{2}(\\omega - \*\\omega) \\in \\Omega\_-^2(M) = { \\text{anti-self-dual two-forms on } M }.$$\
\
Since $\*$ interchanges the kernels of the operators $d$ and $\\delta$, the self-dual and anti-self-dual components of a harmonic two-form are again harmonic. Thus the space of harmonic two-forms on $M$ divides into a direct sum decomposition\
\
$$\\mathcal{H}^2(M) \\cong \\mathcal{H} _+^2(M) \\oplus \\mathcal{H}_-^2(M),$$\
\
the two summands consisting of self-dual and anti-self-dual harmonic two-forms, respectively. Let\
\
$$b\_+ = \\dim \\mathcal{H} _+^2(M), \\quad b_\- = \\dim \\mathcal{H}\_-^2(M).$$\
\
Then $b\_+ + b\_- = b\_2$, the second Betti number of $M$, while\
\
$$r(M) = b\_+ - b\_-$$\
\
is called the signature of $M$.\
\
On a compact oriented four-manifold, the operator $d^+ = P\_+ \\circ d : \\Omega^1(M) \\rightarrow \\Omega^2(M)$ fits into a fundamental elliptic complex\
\
$$0 \\rightarrow \\Omega^0(M) \\rightarrow \\Omega^1(M) \\rightarrow \\Omega^2(M) \\rightarrow 0.$$ (1.24)\
\
Hodge's Theorem allows us to calculate the cohomology groups of this complex. Indeed, if $\\omega \\in \\Omega\_+^2(M)$ is $(,)$-orthogonal to the image of $d^+$, then $\\delta \\omega = 0$. Self-duality then implies that $d \\omega = 0$, so $\\omega$ is harmonic. On the other hand, suppose that $\\omega \\in \\Omega^1(M)$ lies in the kernel of $d^+$ and is perpendicular to the image of $d$. Then $\\delta \\omega = 0$ and $d \\star \\omega = 0$, and hence\
\
$$(d + \\delta)(\\omega + \*\\omega) = d\\omega + \\delta \\omega = d\\omega + d\\omega = 2d^+\\omega = 0.$$\
\
* * *\
\
1.9. HODGE THEORY\
\
Thus $\\omega \\in \\mathcal{H}^{1}(M)$, and the cohomology groups of the complex (1.24) are just\
$$\\mathcal{H}^{0}(M) \\cong R, \\quad \\mathcal{H}^{1}(M), \\quad \\mathcal{H}^{2}\_{+}(M).$$\
This leads to an immediate proof of the following\
\
Proposition. Let $L$ be a complex line bundle over the compact oriented Riemannian manifold $M$. An element $\\phi \\in \\Omega^{2} _{+}(M)$ will be the self-dual part of the curvature of some unitary connection on $L$ if and only if $\\phi$ lies in an affine subspace $\\Pi$ of $\\Omega^{2}_{+}(M)$ of codimension $b\_{+}$.\
\
Indeed, we can choose a base connection $d\_{A\_{0}}$ on $L$ and let $\\Pi$ be the image of the map\
$$a \\mapsto F\_{A\_{0}} + (da)^{+}.$$\
Then $\\Pi$ is the required affine space of codimension $b\_{+}$ its orthogonal complement being the space $\\mathcal{H}^{2}\_{+}(M)$ of self-dual harmonic two forms.\
\
From Hodge's Theorem and the classification theorem for connections presented in the previous section, we see that every complex line bundle with Hermitian inner product over a compact oriented simply connected Riemannian four-manifold $M$ has a canonical connection, one with harmonic curvature.\
\
This connection has an important variational characterization. We define the Yang-Mills functional\
$$\\mathcal{Y}: \\mathcal{A} \\rightarrow R \\text{ by } \\mathcal{Y}(d\_{A}) = \\int\_{M} F\_{A} \\wedge \\star F\_{A}.$$\
A critical point of this functional is a Yang-Mills connection or an abelian instanton (said to be abelian because the Lie group $U(1)$ is abelian). Since\
$$\\mathcal{Y}(d\_{A} - ita) = \\int\_{M} (F\_{A} + tda) \\wedge \\star(F\_{A} + tda)$$\
$$= \\mathcal{Y}(d\_{A}) + 2t \\int\_{M} da \\wedge \\star F\_{A} + t^{2}(\\cdots) = \\mathcal{Y}(d\_{A}) - 2t \\int\_{M} a \\wedge (d \\star F\_{A}) + t^{2}(\\cdots),$$\
we see that\
$$\\frac{d}{dt}\\mathcal{Y}(d\_{A} - ita) \\bigg\| _{t=0} = -2 \\int_{M} a \\wedge (d \\star F\_{A}),$$\
so the critical points of the Yang-Mills functional are solutions to the Yang-Mills equation\
$$d(\\star F\_{A}) = 0.$$\
Since $dF\_{A} = 0$ by the Bianchi identity, we see that a Yang-Mills connection is just a connection whose curvature form is harmonic.\
\
* * *\
\
## 46 CHAPTER 1. PRELIMINARIES\
\
The Yang-Mills equation can be generalized to quaternionic line bun- dles, thus leading to a nonabelian gauge theory, which is the foundation for Donaldson’s original approach to the geometry and topology of four- manifolds discussed in \[12\].\
\
* * *\
\
## Chapter 2\
\
# Spin geometry on four-manifolds\
\
### 2.1 Euclidean geometry and the spin groups\
\
The fact that R2 possesses a complex multiplication making it into a eld has important applications, leading for example to the theory of Riemann surfaces. Similarly, the quaternion multiplication on R4 has important applications to the geometry of four-manifolds. In four dimensions, quater- nions yield a simplication of the theory of spinors (which is presented in full generality in the highly recommended references\[24\] and \[4\]). We will consider Euclidean four-space to be the space V of quaternions, complex 2 2 matrices of the form\
\
t + iz x + iy Q =; x + iy t iz p where i = 1. Recall that as a real vector space, V is generated by the four matrices 1 0 0 1 0 i i 0 1 =; i =; j =; k =; 0 1 1 0 i 0 0 i\
\
the matrix product restricting to minus the cross product on the subspace spanned by i, j and k. The determinant of a quaternion Q is given by the formula det Q = t2 + z2 + x2 + y2 = hQ;Qi; where h ; i denotes the Euclidean dot product. Moreover, t QQ = (t2 + x2 + y2 + z2)I;\
\
* * *\
\
so the unit sphere in Euclidean four-space can be identified with the special unitary group\
\
$$SU(2) = {Q \\in V : \\langle Q, Q \\rangle = 1},$$\
\
while Euclidean four-space itself can be regarded as the set of real multiples of $SU(2)$ matrices. The sphere of unit quaternions $SU(2)$ forms a Lie group under quaternion multiplication, whose Lie algebra—the tangent space to the unit sphere at the identity—is the linear space of "purely imaginary quaternions" spanned by i, j and k, or equivalently, the linear space of offrace-free 2 × 2 skew-Hermitian matrices.\
\
The four-dimensional spin group is simply the direct product of two copies of the special unitary group,\
\
$$Spin(4) = SU\_{+}(2) \\times SU\_{-}(2);$$\
\
a typical element is $(A\_{+}, A\_{-})$, where $A\_{\\pm} \\in SU\_{\\pm}(2)$. We have a representation\
\
$$\\rho : Spin(4) \\rightarrow GL(V) = { \\text{isomorphisms from } V \\text{ to itself} }$$\
\
defined by\
\
$$\\rho(A\_{+}, A\_{-})(Q) = A\_{-}Q(A\_{+})^{-1}.$$\
\
Since $A\_{+}$ and $A\_{-}$ have determinant one,\
\
$$\\langle A\_{-}Q(A\_{+})^{-1}, A\_{-}Q(A\_{+})^{-1} \\rangle = \\det(A\_{-}Q(A\_{+})^{-1}) = \\det Q = \\langle Q, Q \\rangle,$$\
\
and hence the representation preserves the Euclidean inner product. In other words,\
\
$$\\rho : Spin(4) \\rightarrow SO(4) \\subset GL(V).$$\
\
To get an idea of how this action works, consider the element\
\
$$A = \\begin{pmatrix} e^{i\\theta} & 0 \ 0 & e^{-i\\theta} \\end{pmatrix} \\in SU(2).$$\
\
Then\
\
$$\\rho(A, I)\\begin{pmatrix} t + iz & z \ x + iy & z \\end{pmatrix} = \\begin{pmatrix} t + iz & z \ x + iy & z \\end{pmatrix}\\begin{pmatrix} e^{i\\theta} & 0 \ 0 & e^{-i\\theta} \\end{pmatrix}$$\
\
$$= \\begin{pmatrix} e^{i\\theta}(t + iz) & z \ e^{i\\theta}(x + iy) & z \\end{pmatrix},$$\
\
a rotation through the angle $\\theta$ in the same direction in the $(t, z)$- and $(x, y)$-planes. On the other hand, one checks that $\\rho(I, A)$ rotates the $(t, z)$- and $(x, y)$-planes in opposite directions.\
\
* * *\
\
2.1. EUCLIDEAN GEOMETRY AND THE SPIN GROUPS 49 More generally, any element A 2 SU (2) is conjugate to an element of the form\
e i 0 i; 0 e\
\
and hence there is a positively oriented orthonormal basis (e1;e2;e3;e4) of V such that (A;I) rotates the planes e1 ^ e2 and e3 ^ e4 through an angle in the same direction, while (I;A) rotates e1 ^ e2 and e3 ^ e4 in opposite directions. Since SO(4) is generated by rotations constructed as above, any element of SO(4) lies in the image of and : Spin(4) ! SO(4) is surjective. The image and range are both compact Lie groups of the same dimension and induces an isomorphism on the level of Lie algebras, so the kernel K of is a nite subgroup and is a smooth covering. Topologically, Spin(4) is a product S3 S3, hence simply connected, while1(SO(4);I) = Z2. The homotopy exact sequence\
\
1 (Spin(4);I) !1(SO(4);I) ! K ! 0\
\
shows that K is isomorphic to Z2 and one easily checks that\
\
## K = f(I;I); ( I; I)g:\
\
We can regard Spin(4) as the space of (4 4)-matrices\
\
A+0 ; where A 2 SU (2): 0 A\
\
This Lie group of dimension six is contained in an important Lie group of dimension seven,\
\
cA+0 Spin(4) = : A+2 SU+(2); A 2 SU (2); 2 U (1) : 0 A\
\
Moreover, the representation described above extends to a representation\
\
c : Spin(4) c ! GL(V);\
\
## given by the formula\
\
cA+0\
\
(Q) = (A)Q(A)\
1 : 0 A +\
\
We also have a group homomorphism : Spin(4) c ! U (1) dened by\
\
A+02 = det(A+) = det(A) = : 0 A\
\
* * *\
\
50 CHAPTER 2. SPIN GEOMETRY ON FOUR-MANIFOLDS\
\
The spin groups Spin(4) and Spin(4) c t into exact sequences\
\
0 ! Z2! Spin(4) ! SO(4) ! 0; (2.1)\
\
0 ! Z2! Spin(4) c ! SO(4) U (1) ! 0: The key advantage to using the spin groups is that these groups have representations which are more basic that the representations we have de- scribed on Euclidean space V itself. Indeed, each factor has its own basic unitary representation. Let W+and W be two copies of C2 with its stan- dard hermitian metric h; i, one each for SU+(2) and SU (2). Then Spin(4) acts on W+and W by\
\
A+0 + 0 A (w+) = A+w+;\
\
A+0\
\
(w) = A w :\
0 A Similarly, Spin(4) c acts on W+and W by\
\
A+0 + 0 A (w+) = A+w+;\
\
A+0\
\
(w) = A w :\
0 A These actions preserve the standard Hermitian metrics on W+and W, and we have an isomorphism of representation spaces\
\
## V C = Hom(W+;W):\
\
Since unit-length elements of V are represented by unitary matrices, they act as isometries from W+to W.\
\
Remark: In physics one is often concerned with four-dimensional space- times of Lorentz signature, and the relevant group is SL(2; C) instead of Spin(4). In this case, a point of at space-time can be thought of as a 2 2 Hermitian matrix t + z x iy X = = tI + xx+ yy+ zz; x + iy t z\
\
wherex,yandzare the so-called Pauli matrices. Note that\
\
det X = t2 x2 y2 z2 = hX;Xi;\
\
where h ; i is the usual Lorentz metric of special relativity. An element A 2 SL(2; C) acts on Hermitian matrices by X 7! AX t A, and since det(AX t\
\
A) = det X, SL(2; C) covers the component of the identity in\
the Lorentz group.\
\
* * *\
\
2.2. WHAT IS A SPIN STRUCTURE? 51\
\
# 2.2 What is a spin structure?\
\
Suppose that (M; h ; i) is an oriented Riemannian manifold of dimension four. The Riemannian metric enables us to reduce the structure group of TM from GL(4; R) to SO(4). Thus we can choose a trivializing open cover fU : 2 Ag for TM so that the corresponding transition functions take their values in SO(4): g : U \ U! SO(4) GL(4; R):\
\
Denition 1. A spin structure on (M; h; i) is given by an open covering fU : 2 Ag of M and a collection of transition functions g~ : U \ U! Spin(4) such that g~ = g and the cocycle condition g~ g~ = ~~g on U \ U \ U is satised. Manifolds which admit spin structures are called spin manifolds. Topolo- gists have found a nice necessary and sucient condition for existence of a spin structure: M admits a spin structure if and only if w2(TM) = 0, where w2(TM) represents the second Stiefel-Whitney class of the tangent bundle, an element of H2(M; Z2). Indeed, the second Stiefel-Whitney class can be dened in terms of Cech cohomology as follows. We say that an open covering fU : 2 Ag of M is a good cover (following \[7\], page 42) if it satises the condition, U1\ U2\ Ukis either empty or dieomorphic to R4, for every choice of (1;:::;k). Suppose that we choose a good cover as trivializing cover for TM. Since U \ U is contractible, each g : U \ U! SO(4) can be lifted to g~~ : U \ U! Spin(4): The problem is that the cocycle condition may not hold. However, by exactness of (2.1), = ~~g g~~ g~ : U \ U \ U!f1g = Z2: It is readily veried that = = = 1 ;\
\
* * *\
\
52 CHAPTER 2. SPIN GEOMETRY ON FOUR-MANIFOLDS\
\
the last equality holding because elements of Z2 are their own inverses, and 1 1 = 1:\
\
Thus in the language of Cech cohomology, f : (;;) 2 A A Ag is a Cech cocycle which, since the cover is good, represents a cohomology class in H2(M; Z2). That cohomology class is called the second Stiefel- Whitney class of the tangent bundle and is denoted by w2(TM). If M has a spin structure, we can choose the ~~g ’s to satisfy the cocycle condition, so the second Stiefel-Whitney class must be zero. Conversely, if the second Stiefel-Whitney class is zero, the Cech theory implies that f g is a coboundary, which means that there exist constant maps : U \ U! Z2 such that = : Then f g~~ g are transition functions dening a spin structure on M. Recall that once we have transition functions satisfying the cocycle con- dition, we get a corresponding vector bundle. Thus if we have a spin struc- ture on (M; h ; i) dened by g~ : U \ U! Spin(4) the transition functions\
\
+g~ : U \ U! SU+(2); g~ : U \ U! SU (2) determine complex vector bundles of rank two over M, which we denote by W+and W. Moreover, TM C = Hom(W+;W); so a spin structure allows us to represent the complexied tangent bundle of M in terms of two more basic complex vector bundles. These bundles W+and W can be regarded as quaternionic line bundles over M. More generally, if L is a complex line bundle over M, we can also write TM C = Hom(W+L;W L); because the transition functions for L cancel out. Denition 2. A spin c structure on (M; h; i) is given by an open covering fU : 2 Ag and a collection of transition functions g~ : U \ U! Spin(4) c\
\
* * *\
\
2.2. WHAT IS A SPIN STRUCTURE? 53 such that g~ = g and the cocycle condition is satised. If (M; h; i) has a spin structure dened by the transition functions\
\
## g~ : U \ U! Spin(4)\
\
and L is a complex line bundle over M with Hermitian metric and transition functions h : U \ U! U (1);\
\
we can dene a spin c structure on M by taking the transition functions to be h g~ : U \ U! Spin(4) c :\
\
In fact, on a simply connected spin manifold, isomorphism classes of spin c\
\
structures on a given Riemannian manifold are in one-to-one correspon- dence with complex line bundles L over M. However, spin c structures also exist on manifolds which do not have genuine spin structures:\
\
Theorem. Every compact oriented four-manifold possesses a spin c struc- ture.\
\
Sketch of proof: The key fact we need is that the second Stiefel-Whitney class is the Z2-reduction of an integral cohomology class. For simply con- nected four-manifolds (the case we need for subsequent applications), this fact follows from the long exact sequence corresponding to the sequence of coecient groups 1 ! Z ! Z ! Z2! 1\
\
and the fact that H3(M; Z) = 0 by Poincare duality. (For the general case, we refer the reader to Appendix D of \[24\].) If fU : 2 Ag is a good trivializing cover for TM, we now know that there is a Cech cocycle : U \ U \ U!f1g representing w2(TM) which lifts to an integral cocycle\
\
~ : U \ U \ U! Z so that exp(i~) = :\
\
Here ~ changes sign under an odd permutation of the indices and the cocycle condition is\
\
~ ~ \+ ~ ~ = 0: (2.2)\
\
Let f : 2 Ag be a partition of unity subordinate to fU : 2 Ag and dene X f : U \ U! R by f = ~ :\
\
* * *\
\
54 CHAPTER 2. SPIN GEOMETRY ON FOUR-MANIFOLDS\
\
Then a straightforward calculation using (2.2) shows that X X X f + f + f = ~ + ~ + ~\
\
X = ~ = ~ :\
\
## Thus if we set\
\
h = exp(if) : U \ U! U (1);\
\
we nd that the h ’s fail to satisfy the cocycle condition for a line bundle with exactly the same discrepancy as the ~g ’s:\
\
## h h h =\
\
## It follows that the maps\
\
h g~ : U \ U! Spin(4) c\
\
do satisfy the cocycle condition and therefore dene a spin c structure on M, nishing our sketch of the proof.\
\
Given a spin c structure dened by the transition functions\
\
g~ : U \ U! Spin(4) c ;\
\
## the transition functions\
\
g~ : U \ U! U (1)\
\
determine a complex line bundle. We denote this bundle by L2 to remind ourselves of the fact that it is the square of the line bundle L used in the construction of a spin c structure on a spin manifold. It follows from the proof of the above theorem that w2(TM) is the reduction mod 2 of c1(L2). Similarly, the representations c +and c yield U (2)-bundles W+L and W L. Note that the bundles W+L and W L exist as genuine vector bundles even though the factors W+, W and L do not unless M is spin. In these notes, we will call W+, W and L virtual vector bundles. Just as in the case of spin structures, we see that a spin c structure allows us to represent the complexied tangent bundle in terms of two more basic bundles, TM C = Hom(W+L;W L):\
\
Sections of W+L and W L are called spinor elds of positive or negative chirality, respectively.\
\
* * *\
\
2.3. ALMOST COMPLEX AND SPIN\
C STRUCTURES 55\
\
c\
\
# 2.3 Almost complex and spin structures\
\
Suppose now that M is a complex manifold of complex dimension two. Thus M has complex coordinate systems\
\
(z1;z2) = (x1 + iy1;x2 + iy2)\
\
which are related holomorphically on overlaps. We can dene a complex multiplication\
\
@ @ @ @ J : TM ! TM by J =; J = : @xi@yi@yi@xi\
\
This is a vector bundle endomorphism which satises the identity J2 = I. More generally, an almost complex structure on a manifold M is simply a vector bundle endomorphism\
\
J : TM ! TM such that J2 = I:\
\
An almost complex structure on a four-manifold enables us to construct trivializations of the tangent bundle TM so that the corresponding transi- tion functions take their values in GL(2; C) GL(4; R). This enables us to regard TM as a complex vector bundle. A Riemannian metric h; i on an almost complex manifold M is said to be Hermitian if it satises the condition\
\
hJv;Jwi = hv;wi;\
\
for all v;w 2 TpM. Such a metric can be constructed using a partition of unity. The Hermitian metric reduces the structure group further from GL(2; C) to U (2) SO(4). We claim that this allow us to construct a canonical spin c structure on M. Indeed, we have a canonical embedding j : U (2) ! Spin(4) c dened by 0 1 1 0 0 0 B 0 det A 0 0 C j(A) = @ A 0 0 A 0 0\
\
such that\
\
c j(A); t + iz x + iy = A t + iz\] : x + iy t iz x + iy \]

This is the usual unitary action on C2 with coordinates (t + iz;x + iy) and hence c j : U (2) ! SO(4)

* * *

56 CHAPTER 2. SPIN GEOMETRY ON FOUR-MANIFOLDS

is the usual inclusion. Thus a U (2)-structure

fg : U \ U! U (2) : ; 2 Ag

on M determines a corresponding spin c structure

fg~ = j g : U \ U! Spin(4) c : ; 2 Ag:

As described in the preceding section, this allows us to dene the complex vector bundles W+L and W L. Of course, when M has a bona de spin structure, these vector bundles are just the tensor products of the spin bundles W+and W with a complex line bundle L. In the general case, L is not well-dened, but L2 is. It has the transition functions g~ : U \ U! U (1)

where : Spin(4) c ! U (1) is the \\determinant map"

A+02 = det(A) = : 0 A

The line bundle L2 will be called the anticanonical bundle of the U (2)-struc- ture. Note that W L can be identied with the holomorphic tangent bundle of the complex manifold M and the anticanonical bundle L2 is isomorphic to the second exterior power of the holomorphic tangent bundle.

# 2.4 Cliord algebras

Instead of using the tangent bundle TM as the foundation for tensor algebra on a Riemannian manifold, we can use the more basic bundles W+and W or W+L and W L, where L is a line bundle with Hermitian metric. Let’s start on the vector space level. An element of Euclidean space V can be regarded as a complex linear homomorphism from W+to W and represented by a quaternion Q. It can be extended to a skew-Hermitian en- domorphism of W = W+W which is represented by the 2 2 quaternion matrix 0 t Q

(Q) = : Q 0
This formula denes a complex linear map

## : V C ! End(W):

* * *

2.4. CLIFFORD ALGEBRAS 57 Note that End(W) is a sixteen-dimensional algebra over the complex num- bers with composition (or matrix multiplication) as the algebra multiplica- tion. If Q 2 V,
t QQ 0 ( (Q)) 2 =t= ( det Q)I = hQ;Qi: (2.3) 0 Q Q

Because of this formula, we can regard End(W) as the complexication of the Cliord algebra of (V; h ; i); matrix multiplication in this algebra is referred to as Cliord multiplication. There is another way that is commonly used to obtain the Cliord algebra of (V C; h ; i). One simply constructs complex 4 4 matrices e1;e2;e3;e4 which satisfy the identities

2 if i = j, e iej+ ejei= 2ij= 0 if i 6= j.

These matrices correspond to the image under of an orthonormal basis of V. Although any such choice would work, it is often convenient to have an explicit one in mind. We take 0 1 0 1 0 0 1 0 0 0 i 0 B 0 0 0 1 C B 0 0 0 i C e1 = @ A; e2 = @ A; 1 0 0 0 i 0 0 0 0 1 0 0 0 i 0 0

0 1 0 1 0 0 0 1 0 0 0 i B 0 0 1 0 C B 0 0 i 0 C e3 = @ A; e4 = @ A : 0 1 0 0 0 i 0 0 1 0 0 0 i 0 0 0

As a complex vector space End(W) has a basis consisting of the matrices

I; ei; eiejfor i < j; eiejekfor i < j < k; e1e2e3e4: (2.4)

It follows immediately from (2.3) that

e i e j= ejei; when i 6= j:

Thus we can identify the complexied second exterior power 2 V C with the complex subspace of End(W) generated by the products eiejfor i < j. Similarly, the third exterior power of V sits inside End(W). Indeed, the basis (2.4) corresponds to a direct sum decomposition

End(W) = 0 V C 1 V C 2 V C 3 V C 4 V C: (2.5)

* * *

We can therefore regard the Clifford algebra as just the complexified exterior algebra with a new multiplication. Clifford product instead of wedge product. In fact, the Clifford product of $e\_i$ with an element $\\omega \\in \\sum\_{i=0}^{k-1} \\Lambda^k V$ can be defined in terms of the wedge product and the interior product

$$i(e\_i) : \\Lambda^k V \\rightarrow \\Lambda^{k-1} V, \\quad (i(e\_i)\\omega,\\theta) = (\\omega,e\_i\\wedge \\theta)$$

by means of the formula

$$e\_i \\cdot \\omega = e\_i \\wedge \\omega - i(e\_i)\\omega.$$

(2.6)

As in §1.8, $\\Lambda^2 V$ has a direct sum decomposition into self-dual and anti-self-dual parts,

$$\\Lambda^2 V = \\Lambda\_4^2 V \\oplus \\Lambda\_2^2 V,$$

the self-dual part being generated by

$$e\_1 \\wedge e\_2 + e\_3 \\wedge e\_4, \\quad e\_1 \\wedge e\_3 + e\_4 \\wedge e\_2, \\quad e\_1 \\wedge e\_4 + e\_2 \\wedge e\_3.$$

The corresponding elements in the Clifford algebra are

$$e\_1 \\cdot e\_2 + e\_3 \\cdot e\_4 = \\begin{pmatrix}
-2i & 0 & 0 & 0 \
0 & 2i & 0 & 0 \
0 & 0 & 0 & 0 \
0 & 0 & 0 & 0
\\end{pmatrix},$$

$$e\_1 \\cdot e\_3 + e\_4 \\cdot e\_2 = \\begin{pmatrix}
0 & 2 & 0 & 0 \
-2 & 0 & 0 & 0 \
0 & 0 & 0 & 0 \
0 & 0 & 0 & 0
\\end{pmatrix},$$

$$e\_1 \\cdot e\_4 + e\_2 \\cdot e\_3 = \\begin{pmatrix}
0 & -2i & 0 & 0 \
-2i & 0 & 0 & 0 \
0 & 0 & 0 & 0 \
0 & 0 & 0 & 0
\\end{pmatrix}.$$

Thus we see that $\\Lambda\_2^2 V$ is just the space of trace-free skew-Hermitian endomorphisms of $W\_+$, which is the Lie algebra of $SU\_+(2)$. Similarly, $\\Lambda\_2^2 V$ is the space of trace-free skew-Hermitian endomorphisms of $W\_+$.

If we represent an element $\\psi \\in W\_+$ in terms of its components as

$$\\psi = \\begin{pmatrix}
\\psi\_1 \
\\psi\_2
\\end{pmatrix},$$

then if $(\\langle ., \\rangle)$ denotes the standard Hermitian inner product on $W\_+$, a direct calculation yields

$$\\langle e\_1 e\_2 \\psi, \\psi \\rangle = (e\_3 e\_4 \\psi, \\psi) = (\\bar{\\psi}\_1 \\bar{\\psi}\_2) \\begin{pmatrix}
-i & 0 \
0 & i
\\end{pmatrix} \\begin{pmatrix}
\\psi\_1 \
\\psi\_2
\\end{pmatrix} = -i(\|\\psi\_1\|^2 - \|\\psi\_2\|^2).$$

* * *

2.4. CLIFFORD ALGEBRAS

$$\\langle e\_1 e\_3 \\psi, \\psi \\rangle = \\langle e\_4 e\_2 \\psi, \\psi \\rangle = (\\bar{\\psi}\_1 \\bar{\\psi}\_2) \\begin{pmatrix} 0 & 1 \ -1 & 0 \\end{pmatrix} \\begin{pmatrix}\\psi\_1 \ \\psi\_2\\end{pmatrix}$$

$= (\\bar{\\psi}\_1 \\bar{\\psi}\_2 - \\psi\_1 \\bar{\\psi}\_2) = -2i \\operatorname{Im}(\\psi\_1 \\bar{\\psi}\_2),$

$$\\langle e\_1 e\_4 \\psi, \\psi \\rangle = \\langle e\_2 e\_3 \\psi, \\psi \\rangle = (\\bar{\\psi}\_1 \\bar{\\psi}\_2) \\begin{pmatrix} 0 & -i \ -i & 0 \\end{pmatrix} \\begin{pmatrix}\\psi\_1 \ \\psi\_2\\end{pmatrix}$$

$= -i(\\bar{\\psi}\_1 \\bar{\\psi}\_2 + \\psi\_1 \\bar{\\psi}\_2) = -2i \\operatorname{Re}(\\psi\_1 \\bar{\\psi}\_2).$

We can define a quadratic map $\\sigma : W\_+ \\rightarrow \\Lambda^2\_V$ in one of two ways: The simplest approach is to identify $\\Lambda^2\_V$ with $2 \\times 2$ trace-free skew-Hermitian matrices and set

$$\\sigma(\\psi) = 2i \\text{ Trace-free part of } \\left( \\frac{\\psi\_1}{\\psi\_2} \\right)(\\bar{\\psi}\_1 \\bar{\\psi}\_2)$$

$= i \\left( \|\\psi\_1\|^2 - \|\\psi\_2\|^2 \\quad 2\\psi\_1 \\bar{\\psi}\_2 \\quad 2\\psi\_2 \\bar{\\psi}\_1 \\quad \|\\psi\_2\|^2 - \|\\psi\_1\|^2 \\right).$

Equivalently, we can identify $\\Lambda^2\_V$ with trace-free skew-Hermitian matrices lying in the upper left $2 \\times 2$ block of the Clifford algebra, and set

$$\\sigma(\\psi) = -\\frac{i}{2} \\sum\_{i<j} \\left( e\_i \\cdot e\_j \\cdot \\psi \\right) e\_i \\cdot e\_j.$$

(2.7)

Since $e\_i \\cdot e\_j$ has length one, we can readily verify that

$$\|\\sigma(\\psi)\|^2 = \\frac{1}{2}(\|\\psi\_1\|^2 - \|\\psi\_2\|^2)^2 + 4\|\\psi\_1 \\psi\_2\|^2 = \|\\psi\|^4,$$ or $\|\\sigma(\\psi)\| = \\frac{1}{\\sqrt{2}} \|\\psi\|^2.$$

Note that $\\sigma$ forgets the phase of $\\psi$: $\\sigma(e^{i\\theta}\\psi) = \\sigma(\\psi)$.

The groups Spin(4) and Spin'(4) act on the linear space End(W) by conjugation; these actions are denoted by Ad and Ad' and are called the adjoint representations. If $T \\in \\text{End}(W)$,

$$\\text{Ad} \\left( \\begin{array}{cc} A\_+ & 0 \ 0 & A\_- \\end{array} \\right)(T) = \\begin{array}{cc} A\_+ & 0 \ 0 & A\_- \\end{array} T \\left( \\begin{array}{cc} A\_+^{-1} & 0 \ 0 & A\_^{-1} \\end{array} \\right),$$

while

$$\\text{Ad}' \\left( \\begin{array}{cc} \\lambda A\_+ & 0 \ 0 & \\lambda A\_- \\end{array} \\right)(T) = \\begin{array}{cc} \\lambda A\_+ & 0 \ 0 & \\lambda A\_- \\end{array} T \\left( \\begin{array}{cc} (\\lambda A\_+)^{-1} & 0 \ 0 & (\\lambda A\_-)^{-1} \\end{array} \\right).$$

If $(M, (, ))$ has a spin or spin' structure, we can use these representations to construct a sixteen-dimensional complex vector bundle over $M$, a bundle of Clifford algebras. For simplicity, we denote this bundle also by End(W).

* * *

Note that this bundle of Clifford algebras is defined even when M is not a spin manifold and W+ and W- are not defined, because the adjoint representations factor through SO(4).

Since the actions of Spin(4) and Spin'(4) preserve the direct sum decomposition (2.5), the bundle End(W) divides into a direct sum decomposition

$$\\text{End}(W) = \\sum\_{k=1}^{4} \\Lambda^{k} TM \\otimes \\mathbb{C}, \\quad \\Lambda^{2}TM \\otimes \\mathbb{C} = \\Lambda\_{+}^{2}TM \\otimes \\mathbb{C} \\oplus \\Lambda^{2}TM \\otimes \\mathbb{C}$$

Moreover, since the vector space quadratic map $\\sigma : W\_{+} \\rightarrow \\Lambda\_{+}^{2}V$ is equivariant with respect to the group action, it extends to a quadratic map on the vector bundle level $\\sigma : W\_{+} \\otimes L \\rightarrow \\Lambda\_{+}^{2}TM$.

The trace of the Hermitian matrix

$$\\begin{pmatrix}
\\psi\_{1} \
\\psi\_{2}
\\end{pmatrix} (\\bar{\\psi} _{1} \\quad \\bar{\\psi}_{2})$$

is the length of the spinor field $\\psi$. The trace-free part of this matrix is $\\sigma(\\psi)$, which can be thought of as a field of infinitesimal rotations, rotating two planes $e\_{1} \\wedge e\_{2}$ and $\\star(e\_{1} \\wedge e\_{2})$ through the same angle in the same direction. The quadratic map $\\sigma$ gives a geometric interpretation to spinor fields: a spinor field of positive chirality can be regarded as the square root of a self-dual two-form, together with a choice of phase.

2.5 The spin connection

From Riemannian geometry we know that if $(M, (, ))$ is a Riemannian manifold, its tangent bundle TM inherits a canonical connection, the Levi-Civita connection. We claim that when W+ and W- are defined, they inherit canonical connections from the Levi-Civita connection.

There are two steps to the construction of these connections. First we construct a connection on the bundle End(W). This is easy, because the Levi-Civita connection on TM induces a connection on $\\Lambda^{k}TM$ for each k and hence a connection on

$$\\text{End}(W) = \\sum\_{k=1}^{4} \\Lambda^{k}TM \\otimes \\mathbb{C}$$

However, we want a connection on W itself. A connection $d\_{A}$ on W is called a Spin(4)-connection if it can be expressed in terms of each local trivialization as

$$\\left(d\_{A}\\sigma\\right) _{\\alpha} = d\\sigma_{\\alpha} + \\phi\_{\\alpha}\\sigma\_{\\alpha},$$

* * *

2.5. THE SPIN CONNECTION

where $\\phi\_a$ is a one-form with values in the Lie algebra of Spin(4) = $SU\_n(2) \\times SU\_{-}(2)$. Now the Lie algebra of Spin(4) is $A^2TM$ which is generated by $e\_j \\cdot e\_j$ for $i < j$. Thus the condition that $d\_A$ is a Spin(4)-connection is simply

$$\\phi\_a = \\sum\_{i,j} \\phi\_{aij} e\_i \\cdot e\_j, \\quad \\phi\_{aij} = -\\phi\_{aji},$$

where $\\phi\_{aij}$ are ordinary real-valued one-forms.

Given a Spin(4)-connection $d\_A$ on $W$, there is a unique connection (also to be denoted by $d\_A$) on End(W) which satisfies the Leibniz rule:

$$d\_A(\\omega \\sigma) = (d\_A \\omega)\\sigma + \\omega d\_A \\sigma, \\quad \\text{for } \\omega \\in \\Gamma(\\text{End}(W)), \\sigma \\in \\Gamma(W). \\tag{2.8}$$

The following theorem allows us to go the other direction:

**Theorem 1.** Suppose that $M$ is a four-dimensional oriented Riemannian manifold with a spin structure. Then there is a unique Spin(4)-connection on $W$ which induces the Levi-Civita connection on End(W).

Proof: In fact, we claim that there is a one-to-one correspondence between Spin(4)-connections on $W$ and SO(4)-connections on $TM$. To see this, let $\\tilde{\\psi}$ be a trivialization of $W$ over an open set $U \\subset M$. The trivialization of $W$ determines a trivialization of End(W) as well as trivializations of the subbundles of End(W) which correspond to linear subspaces of the Clifford algebra which are left fixed by the action of Spin(4). In particular, $\\tilde{\\psi}$ induces a trivialization $\\psi$ of TM over $U$.

Let $(e\_1, e\_2, e\_3, e\_4)$ be the orthonormal sections of $W\|U$ defined by

$$\\tilde{\\psi} \\circ e\_1(p) = \\left( p, \\begin{pmatrix} 1 \ 0 \ 0 \ 0 \\end{pmatrix} \\right), \\quad \\ldots, \\quad \\tilde{\\psi} \\circ e\_4(p) = \\left( p, \\begin{pmatrix} 0 \ 0 \ 0 \ 1 \\end{pmatrix} \\right),$$

and let $(e\_1, e\_2, e\_3, e\_4)$ be the orthonormal sections of TM\|U defined by

$$\\psi \\circ e\_1(p) = \\left( p, \\begin{pmatrix} 0 & 0 & -1 & 0 \ 0 & 0 & 0 & -1 \ 1 & 0 & 0 & 0 \ 0 & 1 & 0 & 0 \\end{pmatrix} \\right), \\quad \\ldots,$$

$$\\psi \\circ e\_4(p) = \\left( p, \\begin{pmatrix} 0 & 0 & 0 & i \ 0 & 0 & i & 0 \ 0 & i & 0 & 0 \ i & 0 & 0 & 0 \\end{pmatrix} \\right).$$

* * *

Then

$$e\_i \\cdot e\_\\lambda = \\sum\_{\\mu=1}^{4} c\_{i\\lambda}^{\\mu} e\_\\mu,$$

where the $c\_{i\\lambda}^{\\mu}$'s are fixed constants.

Suppose now that $d\_A$ is a Spin(4)-connection on $W$, given over $U$ by

$$d + \\sum\_{i,j=1}^{4} \\phi\_{ij} e\_i \\cdot e\_j, \\quad \\phi\_{ij} = -\\phi\_{ji}.$$

Since the components of $e\_\\lambda$ and $e\_k \\cdot e\_\\lambda$ with respect to the given trivializations are constant,

$$d\_A e\_\\lambda = \\sum\_{i,j=1}^{4} \\phi\_{ij} e\_i e\_j e\_\\lambda, \\quad d\_A(e\_k e\_\\lambda) = \\sum\_{i,j=1}^{4} \\phi\_{ij} e\_i e\_j e\_\\lambda.$$

Hence it follows from condition (2.8) that

$$\\sum\_{i,j=1}^{4} \\phi\_{ij} e\_i e\_j e\_k e\_\\lambda = (d\_A e\_k) e\_\\lambda + e\_k \\sum\_{i,j=1}^{4} \\phi\_{ij} e\_i e\_j e\_\\lambda,$$

or equivalently,

$$(d\_A e\_k) e\_\\lambda = \\sum\_{i,j=1}^{4} \\phi\_{ij}(e\_i e\_j e\_k - e\_k e\_i e\_j) e\_\\lambda.$$

The only terms surviving in the sum on the right are those in which $i \\neq j$
and $k = i$ or $k = j$. A short calculation shows that

$$d\_A e\_k = -4 \\sum\_{i=1}^{4} \\phi\_{ik} e\_i.$$

It follows directly from this formula the induced connection $d\_A$ on
End(W) preserves TM and is an orthogonal connection.

Conversely, given an orthogonal connection

$$d\_A e\_k = \\sum\_{i=1}^{4} \\omega\_{ik} e\_i$$

on TM, we can define a corresponding Spin(4)-connection on $W$ by setting

$$\\phi\_{ij} = -\\frac{1}{4} \\omega\_{ij}.$$

* * *

2.5. THE SPIN CONNECTION 63

This is the unique Spin(4)-connection on W which induces the SO(4)-connection. In terms of the local trivialization, the connection is simply

$$d - \\frac{1}{4} \\sum\_{i,j=1}^{4} \\omega\_{ij} e\_i \\cdot e\_j.$$ (2.9)

Note that in terms of the local trivializations, the products $e\_i \\cdot e\_j$ for $i \\neq j$ are represented by skew-Hermitian matrices, and hence covariant differentiation does indeed satisfy the metric condition:

$$d\\langle \\psi, \\eta \\rangle = \\langle d\_A \\psi, \\eta \\rangle + \\langle \\psi, d\_A \\eta \\rangle.$$ (2.10)

What is the curvature

$$\\Omega = \\left(d - \\frac{1}{4} \\sum\_{i,j=1}^{4} \\omega\_{ij} e\_i \\cdot e\_j\\right)^2$$

of the spin connection? It is not difficult to answer this question if we remember that in the local trivializations, the $e\_i$'s are constant elements of End(W). A short calculation shows that

$$\\Omega = d\\left(-\\frac{1}{4} \\sum\_{i,j=1}^{4} \\omega\_{ij} e\_i \\cdot e\_j\\right) + \\left(\\frac{1}{4} \\sum\_{i,j=1}^{4} \\omega\_{ij} e\_i \\cdot e\_j\\right)^2 = -\\frac{1}{4} \\sum\_{i,j=1}^{4} \\Omega\_{ij} e\_i \\cdot e\_j,

where

$$\\Omega\_{ij} = d\\omega\_{ij} + \\sum\_{k=1}^{4} \\omega\_{ik} \\wedge \\omega\_{kj}.

We can set

$$R\_{ijkl} = \\Omega\_{ij}(e\_k, e\_l),$$ so that

$$\\Omega\_{ij} = \\sum\_{k,l=1}^{4} R\_{ijkl}\\theta\_k \\wedge \\theta\_l,

where $\\theta\_1, \\theta\_2, \\theta\_3, \\theta\_4$ is the coframe dual to $(e\_1, e\_2, e\_3, e\_4)$. The $R\_{ijkl}$'s are the components of the Riemann-Christoffel curvature tensor, which is studied extensively in Riemannian geometry texts, and the components satisfy the curvature symmetries

$$R\_{ijkl} = -R\_{jkl} = R\_{ijlk},$$ $$R\_{ijkl} + R\_{iklj} + R\_{dljk} = 0.

An important invariant of the Riemannian manifold M is the scalar curvature s, given by the formula

$$s = \\sum\_{i,j=1}^{4} R\_{ijj}.$$

* * *

We claim that

$$\\sum\_{i,j=1}^{4} e\_i e\_j \\Omega(e\_i, e\_j) = \\frac{s}{2}. \\tag{2.11}$$

Indeed, since $R\_{kij} = R\_{ijkl}$,

$$\\sum\_{i,j=1}^{4} e\_i e\_j \\Omega(e\_i, e\_j) = -\\frac{1}{4} \\sum\_{i,j,k,l=1}^{4} e\_i e\_j e\_i \\Omega\_{kl}(e\_i, e\_j)$$

$$= -\\frac{1}{4} \\sum\_{i,j,k,l=1}^{4} e\_i e\_j e\_k e\_l R\_{ijkl}.$$

Now observe that if $i, j, k$ and $l$ are distinct,

$$e\_i e\_j e\_k e\_l R\_{ijkl} + e\_i e\_j e\_k e\_j R\_{ikj} + e\_i e\_j e\_k e\_r R\_{ijk}$$

$$= e\_i e\_j e\_k e\_l (R\_{ikj} + R\_{ikj} + R\_{ijk}) = 0,$$

by the last of the curvature symmetries. Similarly, if $i, j$ and $l$ are distinct,

$$e\_i e\_j e\_k e\_l R\_{ijil} + e\_i e\_j e\_k e\_j R\_{ijl} = e\_i e\_j e\_i (R\_{ijl} - R\_{ijj}) = 0.$$

Hence the only terms surviving in the sum are those containing $R\_{ijij}$ or $R\_{ijji}$, and

$$\\sum\_{i,j=1}^{4} e\_i e\_j \\Omega(e\_i, e\_j) = -\\frac{1}{4} \\sum\_{i,j=1}^{4} e\_i e\_j e\_i R\_{ijij} - \\frac{1}{4} \\sum\_{i,j=1}^{4} e\_i e\_j e\_i R\_{ijji} = \\frac{s}{2},$$

establishing the claim.

Given a unitary connection $d\_A$ on a complex line bundle $L$ over a spin manifold $M$, we can define a connection on the bundle $W \\otimes L$ by taking the tensor product of this connection with the connection given by Theorem 1. This connection will also be denoted by $d\_A$. It is a Spin(4)$^c$-connection, which means that it can be expressed in terms of each local trivialization as

$$(d\_A \\sigma) _\\alpha = d\\sigma_\\alpha + \\phi\_\\alpha \\sigma\_\\alpha,$$

where $\\phi\_\\alpha$ is a one-form with values in the Lie algebra of Spin(4)$^c$. In fact,

$$\\phi\_\\alpha = -iaI - \\frac{1}{4} \\sum\_{i,j=1}^{4} \\omega\_{ij} e\_i \\cdot e\_j,$$

* * *

2.6. THE DIRAC OPERATOR 65

a being an ordinary real-valued one-form. Moreover, $da = F\_A$, where $-iF\_A$
is the curvature of the original connection on $L$. The curvature of the new
connection on $W \\otimes L$ is

$$\\Omega\_A = -iF\_A I + \\Omega = -iF\_A I - \\frac{1}{4} \\sum\_{i,j=1}^{4} \\Omega\_{ij} e\_i \\cdot e\_j,$$

(2.12)

a two-form with values in End($W$). In this formula, the $\\Omega\_{ij}$'s are the
curvature forms for the Levi-Civita connection corresponding to the given
Riemannian metric on $M$.
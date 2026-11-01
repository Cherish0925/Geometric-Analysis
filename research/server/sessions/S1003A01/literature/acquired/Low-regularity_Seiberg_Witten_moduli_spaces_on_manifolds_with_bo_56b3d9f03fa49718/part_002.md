---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Low-regularity Seiberg–Witten moduli spaces on manifolds with boundary]

Composing H^1(X; {\\mathbb {Z}}) \\xrightarrow {\\cdot 2 \\pi i} \\pi \_0 {{\\mathcal {G}}}^{h}(X) \\xrightarrow {s} {{\\mathcal {G}}}^{h}(X) \\xrightarrow {\\frac{\\delta }{2 \\pi i}} H^1(X, \\partial X; {\\mathbb {R}}) we get a linear map which by linearity uniquely extends to a section s\_H: H^1(X; {\\mathbb {R}}) \\rightarrow H^1(X, \\partial X; {\\mathbb {R}}) of the aforementioned exact sequence. \\square

### Definition 3.12

(Gauge splitting) By a _gauge splitting_ we call a splitting {s: \\pi \_0{{\\mathcal {G}}}^{h}(X)}{ \\rightarrow {{\\mathcal {G}}}^{h}(X)} of the exact sequence (3). We denote by

\\begin{aligned} {s^H: H^1(X;{\\mathbb {R}}) \\rightarrow H^1(X,\\partial X;{\\mathbb {R}})} \\end{aligned}

the associated _homological splitting_.

We clarify the relationship between gauge splittings and homological splittings.

### Proposition 3.13

(Gauge splittings from homological splittings) Let \\sigma : H^1(X; {\\mathbb {R}}) \\rightarrow H^1(X, \\partial X; {\\mathbb {R}}) be a homological splitting, i.e., a splitting of ( [5](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ3)). Then up to action of S^1 there exists a unique gauge splitting _s_ such that \\sigma = s^H.

### Proof

For existence, choose x\_0 \\in X and consider the map

\\begin{aligned} I\_{x\_0} : \\left\\{ \\eta \\in {\\mathcal {H}}^1\_D(X)\\right.&\\left\| \\, \[\\eta \] \\in H^1(X; 2 \\pi i {\\mathbb {Z}}) \\right\\} \\longrightarrow {{\\mathcal {G}}}^{h}(X), \\nonumber \\\ \\eta&\\longmapsto \\left( I\_{x\_0}(\\eta )(x) = \\exp \\left( \\int \_{x\_0}^x \\eta \\right) \\right) . \\end{aligned}

(6)


Notice that \\delta (I\_{x\_0}(\\eta )) = \\eta . Therefore taking s(\[u\]) = I\_{x\_0}(\\sigma (\[\\delta (u)\])) we get a gauge splitting s: \\pi \_0 {{\\mathcal {G}}}^{h}(X) \\rightarrow {{\\mathcal {G}}}^{h}(X) with \\sigma = s^H.

The uniqueness up to action of S^1 follows from the exactness of the middle vertical sequence in (4). \\square

In order to find the appropriate gauge fixing we need the following analogue of Proposition [3.8](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar21) for 1-forms.

### Lemma 3.14

(Decomposing 1-forms) \\Omega ^1(X) = \\Omega ^1\_{CC}(X) + d(\\Omega ^0(X)) and \\Omega ^1\_{CC}(X) \\cap d(\\Omega ^0(X)) = d({\\mathcal {H}}(X)).

### Proof

This follows from the proof of \[ [12](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR12 "Khandhawit, T.: A new gauge slice for the relative Bauer-Furuta invariants. Geom. Topol. 19(3), 1631–1655 (2015)"), Proposition 2.2\]. (Note that our definition of \\Omega ^1\_{CC}(X) differs from Khandhawit’s, which we denote by \\Omega ^1\_{s^\\perp }(X) (cf. Definition [3.22](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar44)).) \\square

In particular, we can decompose 1-forms as

\\begin{aligned} \\Omega ^1(X) = \\Omega ^1\_{CC}(X) \\oplus d(\\Omega ^0\_\\partial (X)) \\end{aligned}

where

\\begin{aligned} \\Omega ^0\_\\partial (X) = \\left\\{ f \\in \\Omega ^0(X) \\big \| \\int \_{Y\_i} f = 0 \\text { for each component }Y\_i \\subset \\partial X \\right\\} . \\end{aligned}

Denote by {\\Pi }\_{CC} the projection onto \\Omega ^1\_{CC}(X) along d(\\Omega ^0\_\\partial (X)), and define {{\\mathcal {G}}}^{e,\\partial }(X) = \\exp \\left( L^2\_2\\left(i \\Omega ^0\_\\partial (X)\\right)\\right). We obtain the following analog of Lemma [3.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar13).

### Lemma 3.15

(Coulomb gauge fixing in 4d) There is a unique homomorphism

![](https://media.springernature.com/lw164/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ112_HTML.png)

such that

![](https://media.springernature.com/lw320/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ113_HTML.png)

### Proof

The projection  (1-\\Pi \_{CC}) on \\Omega ^1(X) has image in d( \\Omega ^0\_\\partial (X)) and that _d_ is injective on \\Omega ^0\_\\partial (X). Therefore there is a unique homomorphism L^2\_1(i \\Omega ^1(X)) \\rightarrow L^2\_2(i \\Omega ^0\_\\partial (X)) sending _a_ to the unique f\_a^{CC} \\in \\Omega ^0\_\\partial (X) such that a - df\_a^{CC} \\in \\Omega ^1(X). Then we take u\_a^{CC} = \\exp (f\_a^{CC}). \\square

This means that any configuration in ![](https://media.springernature.com/lw55/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq446_HTML.gif) can be put into the Coulomb slice by a gauge transformation, i.e., is gauge equivalent to an element of

![](https://media.springernature.com/lw409/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ114_HTML.png)

We can further decompose

\\begin{aligned} \\Omega ^1\_{CC}(X) = \\left(\\Omega ^1\_{CC}(X) \\cap ({\\mathcal {H}}^1\_D(X))^\\perp \\right) \\oplus {\\mathcal {H}}^1\_D(X). \\end{aligned}

(7)


A homological splitting s^H provides a decomposition

\\begin{aligned} {\\mathcal {H}}^1\_D(X) = s^H(H^1(X;{\\mathbb {R}})) \\oplus d({\\mathcal {H}}(X)) \\end{aligned}

(8)


which is an analogue of (3) for {\\mathcal {H}}^1\_D(X). With these in hand, we are ready to define the split Coulomb slice.

### Definition 3.16

(Split Coulomb slice) Let _s_ be a gauge splitting and s^H its associated homological splitting. The _split Coulomb slice_ is

\\begin{aligned} \\Omega ^1\_{s}(X) = \\{ a \\in \\Omega ^1\_{CC}(X) \| a \\in (\\Omega ^1\_{CC}(X) \\cap ({\\mathcal {H}}^1\_D(X))^\\perp ) \\oplus s^H(H^1(X;i{\\mathbb {R}})) \\}. \\end{aligned}

The space of configurations in the split Coulomb slice with respect to _s_ will be denoted by

![](https://media.springernature.com/lw480/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ115_HTML.png)

We have that

\\begin{aligned} \\Omega ^1(X) = \\Omega ^1\_{s}(X) \\oplus d(\\Omega ^0(X)). \\end{aligned}

(9)


Parallel to Lemmas [3.15](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar33) and [3.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar13), denote by {\\Pi }\_s the projection onto the first factor along the second one and define ![](https://media.springernature.com/lw187/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq451_HTML.gif). We obtain:

### Lemma 3.17

(Split gauge fixing in 4d) There is a unique homomorphism

![](https://media.springernature.com/lw162/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ116_HTML.png)

such that

![](https://media.springernature.com/lw265/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ117_HTML.png)

### Proof

The projection  (1-\\Pi \_s) on \\Omega ^1(X) has image in d( \\Omega ^0(X)) and _d_ is injective on \\Omega ^0\_0(X). Therefore there is a unique homomorphism L^2\_1(i \\Omega ^1(X)) \\rightarrow L^2\_2(i \\Omega ^0\_0(X)) sending _a_ to the unique f\_a^{s} \\in \\Omega ^0\_0(X) such that a - df\_a^s \\in \\Omega ^1(X). Then we take u\_a^s = \\exp (f\_a^s). \\square

### Remark 3.18

(Continuous gauge fixing within double Coulomb slice) If we only consider a \\in \\Omega ^1\_{CC}(X), then the above map has image in {{\\mathcal {G}}}^{h}(X), which is finite-dimensional. Since the latter gauge group acts continuously on the configuration space by Lemma [3.10](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar24), we conclude that putting ![](https://media.springernature.com/lw139/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq463_HTML.gif) into split Coulomb slice ![](https://media.springernature.com/lw61/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq464_HTML.gif) can be done continuously with respect to (A,\\Phi ).

The gauge group acting on this split Coulomb slice is the product of S^1 and the split gauge group:

### Definition 3.19

(Split harmonic gauge group) Let _s_ be a gauge splitting. The _split gauge group_ is defined to be

![](https://media.springernature.com/lw159/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ118_HTML.png)

### Lemma 3.20

(Split gauge group preserves the split Coulomb slice) For ![](https://media.springernature.com/lw82/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq467_HTML.gif) we have ![](https://media.springernature.com/lw149/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq468_HTML.gif).

Conversely, if ![](https://media.springernature.com/lw149/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq469_HTML.gif), then for some z \\in S^1 we have ![](https://media.springernature.com/lw90/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq471_HTML.gif).

### Proof

One direction follows directly from the definition of s^H: if u = s(\[u\]), then s^H(\[\\delta (u)\]) = \\delta (u) = u^{-1}du \\in {\\mathcal {H}}^1\_D(X) \\simeq H^1(X,\\partial X;i {\\mathbb {R}}), so ![](https://media.springernature.com/lw211/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq475_HTML.gif).

The other direction follows by chasing arrows in the diagram (4). \\square

The circle \\circ  in the superscript indicates that the only constant gauge transformation contained in ![](https://media.springernature.com/lw53/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq478_HTML.gif) is the identity. This way we do not forget the S^1-action when taking the quotient by the split gauge group.

We want to compare different split slices together with the split gauge group actions. Choose two splittings s, s'. These determine a map  s' \\cdot s^{-1}: \\pi \_0 {{\\mathcal {G}}}^{h}(X) \\rightarrow {{\\mathcal {G}}}^{h,e}(X). Viewing \\pi \_0 {{\\mathcal {G}}}^{h}(X) \\simeq H^1(X; 2 \\pi i {\\mathbb {Z}}) as a sublattice of H^1(X; i {\\mathbb {R}}), let \\nu : H^1(X; i {\\mathbb {R}}) \\rightarrow {{\\mathcal {G}}}^{h,e}(X) be any homomorphism extending s' \\cdot s^{-1}. Define

![](https://media.springernature.com/lw330/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ119_HTML.png)

where {\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H}: i\\Omega ^1\_{CC}(X) \\rightarrow s^H(H^1(X; i{\\mathbb {R}})) is the projection along  i (\\Omega ^1\_{CC}(X) \\cap {\\mathcal {H}}^1\_D(X)) \\oplus i d({\\mathcal {H}}(X)) (cf. ( [7](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ5)), ( [8](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ6))).

### Proposition 3.21

(Equivalence of slices) The map F\_\\nu  is well-defined, a diffeomorphism, equivariant with respect to the action of ![](https://media.springernature.com/lw212/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq489_HTML.gif).

### Proof

Firstly, we need to show that the image of F\_\\nu  actually lies in ![](https://media.springernature.com/lw61/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq491_HTML.gif). Equivalently, we want to show that

\\begin{aligned} A\_\\nu : \\Omega ^1\_{CC}(X)&\\longrightarrow \\Omega ^1\_{CC}(X) \\\ a&\\longmapsto \\nu \\left({\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H} a \\right) \\cdot a = a + \\delta \\left(\\nu \\left({\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H} a \\right) \\right) \\end{aligned}

maps \\Omega ^1\_s(X) to \\Omega ^1\_{s'}(X). We have \\delta ({{\\mathcal {G}}}^{h,e}(X)) = d({\\mathcal {H}}(X)) and, moreover, \\delta \\circ \\nu  is a homomorphism, thus a linear map H^1(X; i{\\mathbb {R}}) \\rightarrow d({\\mathcal {H}}(X)). What follows is that A\_\\nu  is a linear map. Now A\_\\nu  restricted to \\Omega ^1\_{CC}\\left(X\\right) \\cap ({\\mathcal {H}}^1\_D(X))^\\perp  is identity by definition, so it suffices to show A\_\\nu ( {{\\,\\textrm{im}\\,}}s^H ) \\subset {{\\,\\textrm{im}\\,}}((s')^H). Furthermore, H^1(X; i {\\mathbb {R}}) is spanned by \[\\delta (\\pi \_0{{\\mathcal {G}}}^{h}(X))\]  and therefore s^H(H^1(X; i{\\mathbb {R}})) is spanned by ![](https://media.springernature.com/lw74/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq504_HTML.gif), so it suffices to show ![](https://media.springernature.com/lw194/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq505_HTML.gif). But we defined \\nu  so that for any ![](https://media.springernature.com/lw82/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq507_HTML.gif)![](https://media.springernature.com/lw144/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq508_HTML.gif), which implies A\_\\nu ( \\delta (u)) = \\delta ( \\nu (\\delta (u)) \\cdot u) \\in {{\\,\\textrm{im}\\,}}( (s')^H), as wished.

The map F\_\\nu  is smooth because the map \\nu  is smooth and the action of the finite-dimensional {{\\mathcal {G}}}^{h}(X) on ![](https://media.springernature.com/lw55/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq513_HTML.gif) is smooth.

It is invertible because F\_{1/\\nu } is its inverse. Indeed, since {{\\,\\textrm{im}\\,}}\\nu \\subset {{\\mathcal {G}}}^{h,e}(X), we have that \\delta \\nu \\in d({\\mathcal {H}}(X)), so {\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H}(\\delta \\nu ) \\equiv 0. Therefore

\\begin{aligned} {\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H} \\left( \\nu ({\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H}(A-A\_0)) A - A\_0\\right) = {\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H}(A-A\_0), \\end{aligned}

so

\\begin{aligned} \\left( \\nu \\left( {\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H} \\left( \\nu ({\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H}(A-A\_0)) A - A\_0\\right) \\right) \\right) ^{-1} = (\\nu ({\\Pi }\_{{{\\,\\textrm{im}\\,}}s^H}(A-A\_0)))^{-1} \\end{aligned}

and F\_{1/\\nu } \\circ F\_\\nu = \\textrm{id} follows. \\square

Finally, we discuss the gauge slice used by Lipyanskiy \[ [21](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR21 "Lipyanskiy, M.: A semi-infinite cycle construction of Floer homology (2008). Thesis (Ph.D.)—Massachusetts Institute of Technology")\] and Khandhawit \[ [12](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR12 "Khandhawit, T.: A new gauge slice for the relative Bauer-Furuta invariants. Geom. Topol. 19(3), 1631–1655 (2015)"), [13](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR13 "Khandhawit, T., Lin, J., Sasahira, H.: Unfolded Seiberg-Witten Floer spectra, I: definition and invariance. Geom. Topol. 22(4), 2027–2114 (2018)")\]. They require that a \\in \\Omega ^1\_{CC}(X) and that for each component Y\_i \\subset \\partial X we have \\int \_{Y\_i} \\iota ^\*(\\star a) = 0. Using Stokes’ theorem one can show that for a \\in \\Omega ^1\_{CC}(X) this integral condition is equivalent to the condition that \\int \_X df \\wedge \\star a = 0 for any f \\in {\\mathcal {H}}(X). This fits into our setup perfectly, since there is exactly one homological splitting s^H\_\\perp  such that {{\\,\\textrm{im}\\,}}s^H\_\\perp = {\\mathcal {H}}^1\_D(X) \\cap (d({\\mathcal {H}}(X)))^\\perp .

### Definition 3.22

(Orthogonal splitting) We call s^H\_\\perp  the _orthogonal homological splitting_. We say that a splitting _s_ is a _orthogonal splitting_ if s^H = s^H\_\\perp .

### 3.3 Restriction to the boundary and twisting

Unless \\partial X is connected, we are not guaranteed that the _restriction_ to the boundary is invariant under the action of the split gauge group ![](https://media.springernature.com/lw53/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq531_HTML.gif). If it happens to be invariant for some _s_, we call such _s_ an _integral splitting_. For a general _s_, we introduce and prove the existence of _twistings_ of the restriction map, making it invariant under the action of ![](https://media.springernature.com/lw53/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq532_HTML.gif) action even for non-integral _s_. As mentioned before, integral splittings are utilized in the proof of the Gluing Theorem, while non-integral splittings may be more convenient in other contexts (e.g., in constructions of \[ [12](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR12 "Khandhawit, T.: A new gauge slice for the relative Bauer-Furuta invariants. Geom. Topol. 19(3), 1631–1655 (2015)"), [13](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR13 "Khandhawit, T., Lin, J., Sasahira, H.: Unfolded Seiberg-Witten Floer spectra, I: definition and invariance. Geom. Topol. 22(4), 2027–2114 (2018)"), [21](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR21 "Lipyanskiy, M.: A semi-infinite cycle construction of Floer homology (2008). Thesis (Ph.D.)—Massachusetts Institute of Technology")\]).

We start by defining the restriction maps for an embedding \\iota \_Y: Y \\hookrightarrow X of an oriented 3-manifold _Y_. Denote by {\\mathfrak {s}} the restriction to _Y_ of the spin^{c} structure \\hat{{\\mathfrak {s}}} on _X_. Precisely, the orientations of _X_ and _Y_ induce an orientation on the normal bundle of _Y_ (recall that we are using the “outward normal first” convention), and denote by \\textbf{n} the outward (or “positive”) normal to _Y_. The Clifford multiplication \\rho \_X induces an isomorphism \\rho \_X(\\textbf{n}): S^+\_X\|\_Y \\rightarrow S^-\_X\|\_Y, and can define the spinor bundle on _Y_ to be S\_Y = S^+\_X\|\_Y \\simeq S^-\_X\|\_Y with the Clifford multiplication \\rho \_Y(v) = \\rho \_X(\\textbf{n})^{-1} \\rho \_X(v). In particular, we have canonical identifications S^\\pm \_X\|\_Y \\simeq S\_Y.

Assuming _Y_ is a totally geodesic codimension-1 submanifold of _X_ (usually we will consider _Y_ which is a boundary component with a product metric on its tubular neighborhood), the spin^{c} connection A\_0 induces a spin^{c} connection B\_0 on _Y_ by simple restriction: \\nabla ^{B\_0} = \\iota \_Y^\*\\nabla ^{A\_0}. Let ![](https://media.springernature.com/lw113/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq548_HTML.gif), ![](https://media.springernature.com/lw155/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq549_HTML.gif), ![](https://media.springernature.com/lw109/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq550_HTML.gif) and u \\in {{\\mathcal {G}}}(X). We define the restrictions:

![](https://media.springernature.com/lw334/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ120_HTML.png)

Integral splittings are the ones for which restriction maps are invariant under the split gauge group.

### Definition 3.23

(Integral splitting) We call a gauge splitting _s_ _integral_ if for each ![](https://media.springernature.com/lw82/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq552_HTML.gif) we have u\|\_{\\partial X} \\equiv 1.

Equivalently, _s_ is integral if the composition \\pi \_0{{\\mathcal {G}}}^{h}(X) \\xrightarrow {s} {{\\mathcal {G}}}^{h}(X) \\xrightarrow {R} {{\\mathcal {G}}}^{h}(\\partial X) \\simeq (S^1)^{\\pi \_0(\\partial X)} is trivial.

The integrality of _s_ is closely connected to the integrality of s^H.

### Proposition 3.24

(Homological classification of integral splittings) If _s_ is integral, then s^H(H^1(X;{\\mathbb {Z}})) \\subset H^1(X, \\partial X; {\\mathbb {Z}}), i.e., s^H is integral as well.

Given any integral homological splitting \\sigma  there exists a unique integral splitting _s_ such that \\sigma = s^H.

### Proof

Assume _s_ is integral. Choose y\_0 \\in \\partial X and consider the map I\_{y\_0} defined in ( [6](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ4)). We know _s_ and I\_{y\_0} \\circ s^H \\circ \[\\delta \] differ by action of S^1, but since both are equal to 1 at y\_0, thus s = I\_{y\_0} \\circ s^H \\circ \[\\delta \]. This implies that for any y \\in \\partial X and any embedded curve \\gamma : \[0,1\] \\rightarrow X with \\gamma (0) = y\_0 and \\gamma (1) = y we have that \\exp \\left( \\int \_{y\_0}^{y} s^H(\[\\delta (u)\])\\right) = 1 and thus \\int \_{y\_0}^{y\_1} s^H(\[\\delta (u)\]) \\in 2 \\pi i {\\mathbb {Z}}. This proves that s^H is integral.

Similarly, if \\sigma  is integral, then s = I\_{y\_0} \\circ \\sigma \\circ \[\\delta \] satisfies that \\sigma = s^H and s(y) = \\exp \\left( \\int \_{y\_0}^{y} s^H(\[\\delta (u)\])\\right) = 1 for any y \\in \\partial X. \\square

To find a consistent way of _twisting_ the boundary values of 1-forms we consider ways to “undo” the action of ![](https://media.springernature.com/lw53/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq579_HTML.gif) on the boundary “in a linear fashion”.

### Definition 3.25

(Gauge twisting) We call a homomorphism \\tau :H^1(X; i {\\mathbb {R}}) \\rightarrow {{\\mathcal {G}}}^{h}(\\partial X) \\simeq (S^1)^{\\pi \_0(\\partial X)} a _gauge twisting_ for _s_ if the composition

\\begin{aligned} \\pi \_0{{\\mathcal {G}}}^{h}(X) \\simeq H^1(X; 2 \\pi i {\\mathbb {Z}}) \\hookrightarrow H^1(X; i {\\mathbb {R}}) \\xrightarrow {\\tau } {{\\mathcal {G}}}^{h}(\\partial X) \\end{aligned}

agrees with the action of the split gauge group on the boundary,  R \\circ s: \\pi \_0{{\\mathcal {G}}}^{h}(X) \\rightarrow {{\\mathcal {G}}}^{h}(\\partial X).

Continuous homomorphisms from a vector space to S^1 correspond to linear functionals on the vector space, and the correspondence is given by taking the differential at 0. Thus, every such twisting \\tau  comes from a linear map d\\tau : H^1(X;i{\\mathbb {R}}) \\rightarrow H^0(\\partial X; i {\\mathbb {R}})  and \\tau = \\exp \\circ (d \\tau ). We utilize it to prove the existence of gauge twistings for _s_, and one could use it to classify all possible gauge twistings for _s_. Actually, every such homomorphism \\tau  is a gauge twisting for some _s_, but we do not use this fact in this article.

### Lemma 3.26

(Existence of gauge twistings) For a given gauge splitting _s_ there exists a gauge twisting \\tau .

### Proof

Since \\pi \_0 {{\\mathcal {G}}}^{h}(X) is free, we can lift the map  R \\circ s: H^1(X; 2 \\pi i{\\mathbb {Z}}) \\simeq \\pi \_0 {{\\mathcal {G}}}^{h}(X) \\rightarrow {{\\mathcal {G}}}^{h}(\\partial X) \\simeq (S^1)^{\\pi \_0(X)} to a homomorphism {\\widetilde{\\tau }}: H^1(X; 2 \\pi i {\\mathbb {Z}}) \\rightarrow H^0(\\partial X; i{\\mathbb {R}}):

![figure c](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Figc_HTML.png)

and this extends to a map {\\widetilde{\\tau }}: H^1(X; i {\\mathbb {R}}) \\rightarrow H^0(\\partial X; i{\\mathbb {R}}) by linearity. Taking \\tau = \\exp \\circ {\\widetilde{\\tau }}: H^1(X; i {\\mathbb {R}}) \\rightarrow (S^1)^{\\pi \_0(\\partial X)} gives a gauge twisting for _s_. \\square

With \\tau  in hand, there is a way of defining a twisting on the whole Coulomb slice, enabling us to finally define the twisted restriction maps.

### Definition 3.27

(Twisted restriction map) We define the _Coulomb slice twisting_![](https://media.springernature.com/lw217/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq595_HTML.gif) associated to \\tau  to be the composition

![](https://media.springernature.com/lw372/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ121_HTML.png)

We define the _twisted restriction map_

![](https://media.springernature.com/lw211/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ122_HTML.png)

by the formula R\_\\tau (A,\\Phi ) = (R(A), \\tau \_{CC}(A-A\_0) R(\\Phi )).

### Remark 3.28

What is of importance for defining the twisted restriction maps is the map \\tau \_{CC}: i \\Omega ^1\_{s}(X) \\rightarrow (S^1)^{\\pi \_0(\\partial X)}. The extension of \\tau \_{CC} to the whole of i \\Omega ^1\_{CC}(X) is artificial: it does not undo the action of {{\\mathcal {G}}}^{h,e}(X) on the boundary as one might expect.

With more work, including a choice of a based gauge group  {{\\mathcal {G}}}^{h}\_o(X) \\subset {{\\mathcal {G}}}^{h}(X)  (such that  {{\\mathcal {G}}}^{h}(X) / {{\\mathcal {G}}}^{h}\_o(X) \\simeq S^1) and a more general twisting, one could work with the full i \\Omega ^1\_{CC}(X) and then quotient by the action of {{\\mathcal {G}}}^{h}\_o(X). However, this would introduce unnecessary complications.

These twisted restriction maps are indeed invariant under ![](https://media.springernature.com/lw53/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq606_HTML.gif).

### Lemma 3.29

(Twisted restriction map is invariant under split gauge group) Let \\tau  be a gauge twisting for _s_. For any ![](https://media.springernature.com/lw139/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq608_HTML.gif) (resp. ![](https://media.springernature.com/lw222/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq609_HTML.gif)) and ![](https://media.springernature.com/lw82/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq610_HTML.gif) we have

\\begin{aligned} R\_\\tau (u(A,\\Phi )) = R\_\\tau (A,\\Phi ) \\end{aligned}

(resp. R\_\\tau (u(a,\\phi )) = R\_\\tau (a,\\phi )).

### Proof

Since u \\in {{\\mathcal {G}}}^{h}(X), we have \\iota \_{\\partial X}^\*(u^{-1}du) = 0, so R(A - u^{-1} du) = R(A).

It remains to prove

\\begin{aligned} \\tau \_{CC}(A - A\_0 - u^{-1}du) R(u \\Phi ) = \\tau \_{CC}(A-A\_0) R(\\Phi ) \\end{aligned}

but that is equivalent to

\\begin{aligned} (\\tau \_{CC}(-u^{-1}du) R(u)) \\tau \_{CC}(A - A\_0) R(\\Phi ) = \\tau \_{CC}(A-A\_0) R(\\Phi ) \\end{aligned}

so it suffices to prove \\tau \_{CC}(u^{-1}du) = R(u). Since _s_ splits (3), we have u = s(\[u\]), where  \[u\] \\in \\pi \_0{{\\mathcal {G}}}^{h}(X) is the homotopy class of _u_. So we have to prove \\tau \_{CC}(u^{-1}du) = R\\circ s(\[u\]). This follows directly from Definition [3.25](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar48) of the twistings and Definition [3.27](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar51) of the twisted restriction map, since u^{-1}du \\in {\\mathcal {H}}^1\_D(X) and the isomorphism \\pi \_0{{\\mathcal {G}}}^{h}(X) \\simeq H^1(X; 2 \\pi i {\\mathbb {Z}}) is given by  \[u\] \\mapsto \[u^{-1}du\]. \\square

We conclude these sections by showing that choosing \\tau  is essentially equivalent to choosing an integral splitting. In general, one can restrict themselves to considering integral splittings without any twisting at all.

### Proposition 3.30

(Twistings are integral splittings) Let \\tau  be a twisting for _s_. Then there is an integral splitting s\_{{\\mathbb {Z}}} and an equivariant diffeomorphism

![](https://media.springernature.com/lw196/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ123_HTML.png)

such that R \\circ F\_{s,\\tau } = R\_\\tau .

### Proof

Every function f \\in {\\mathcal {H}}(X) is determined by its restriction to the boundary f\|\_{\\partial X}, which is locally constant. We thus have the exact sequence

\\begin{aligned} 0 \\rightarrow H^0(\\partial X; 2 \\pi i {\\mathbb {Z}}) \\rightarrow H^0(\\partial X; i {\\mathbb {R}}) \\simeq i {\\mathcal {H}}(X) \\xrightarrow {f \\mapsto \\exp (f\|\_{\\partial X})} {{\\mathcal {G}}}^{h}(\\partial X) \\rightarrow 0 \\end{aligned}

as well as

\\begin{aligned} 0 \\rightarrow H^0(X; 2 \\pi i {\\mathbb {Z}}) \\rightarrow i {\\mathcal {H}}(X) \\xrightarrow {\\exp } {{\\mathcal {G}}}^{h,e}(X) \\rightarrow 0 \\end{aligned}

and from these two it follows that

\\begin{aligned} 0 \\rightarrow H^0(\\partial X; 2 \\pi i {\\mathbb {Z}}) / H^0(X; 2 \\pi i {\\mathbb {Z}}) \\rightarrow {{\\mathcal {G}}}^{h,e}(X) \\xrightarrow {\\cdot \|\_{\\partial X}} {{\\mathcal {G}}}^{h}(\\partial X) \\rightarrow 0 \\end{aligned}

(10)


is exact. Since the group to the left is discrete it follows that there exists a unique lift {\\tilde{\\tau }} of \\tau  to {{\\mathcal {G}}}^{h,e}(X):

![figure d](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Figd_HTML.png)

We define

\\begin{aligned} s\_{{\\mathbb {Z}}}(\[u\]) = ({\\tilde{\\tau }}(\[u\]))^{-1} \\cdot s(\[u\]) \\end{aligned}

for any  \[u\] \\in \\pi \_0 {{\\mathcal {G}}}(X) \\simeq H^1(X; 2 \\pi i {\\mathbb {Z}}), and

\\begin{aligned} F\_{s,\\tau } = F\_{({\\tilde{\\tau }})^{-1}} \\end{aligned}

using the construction of F\_\\nu  of Proposition [3.21](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar42). This gives an equivariant diffeomorphism from ![](https://media.springernature.com/lw61/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq634_HTML.gif) to ![](https://media.springernature.com/lw67/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq635_HTML.gif).

The equality R \\circ F\_{s,\\tau } = R\_\\tau  follows from the construction. \\square

Even though the spaces ![](https://media.springernature.com/lw67/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq638_HTML.gif) and ![](https://media.springernature.com/lw67/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq639_HTML.gif) are equivariantly diffeomorphic by Proposition [3.21](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar42), the corresponding restriction maps differ by a twist. Thus, _a priori_ we cannot get rid of the choice of a splitting. However, this is not relevant to most of the applications because for connected boundary there is no choice to make.

### Lemma 3.31

(Uniqueness of integral splittings) If \\partial X \\ne \\varnothing  is connected, there exists exactly one integral splitting s\_{\\mathbb {Z}}.

### Proof

In this case, the restriction map {{\\mathcal {G}}}^{h,e}(X) \\rightarrow {{\\mathcal {G}}}^{h}(\\partial X) is an isomorphism (cf. ( [10](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ8))). Therefore for each element \\pi \_0 {{\\mathcal {G}}}(X) there exists exactly one representative u \\in {{\\mathcal {G}}}^{h}(X) such that u\|\_{\\partial X} = 1. \\square

### 3.4 Seiberg–Witten moduli in split Coulomb slice

We conclude this section by defining the _Seiberg–Witten moduli spaces_, the main object of study of this article. We also prove they only depend on the choice of s\_{{\\mathbb {Z}}} associated to _s_ and \\tau .

Thanks to Lemma [3.20](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar40), we can define the following.

### Definition 3.32

(Moduli spaces on 4-manifolds with boundary) We define the moduli spaces in split slice:

![](https://media.springernature.com/lw351/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ124_HTML.png)

We also define a version of the moduli space using the full double Coulomb slice,

![](https://media.springernature.com/lw373/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ125_HTML.png)

which will be utilized in some of the proofs.

From Lemma [3.29](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar53) it follows that

### Corollary 3.33

There is a well-defined restriction map

![](https://media.springernature.com/lw214/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ126_HTML.png)

A direct consequence of Proposition [3.30](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar55) is

### Corollary 3.34

(Dependence on twistings) Given _s_ and \\tau , there is an integral splitting s\_{{\\mathbb {Z}}} and a diffeomorphism

![](https://media.springernature.com/lw218/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ127_HTML.png)

such that R \\circ F\_{s,\\tau } = R\_\\tau .

## 4 Properties of moduli spaces

In this section we prove that (Semi-infinite-dimensionality Theorem):

- the moduli spaces of solutions to the Seiberg–Witten equations on _X_ are Hilbert manifolds,

- the restriction map to the boundary is “semi-infinite”, i.e., Fredholm in the negative direction and compact in the positive direction,

- if \\partial X is disconnected, restriction to a single boundary component has dense differential.


This is done by analyzing the properties of the linearized Seiberg–Witten operator D{{\\,\\textrm{SW}\\,}}. We start by investigating an extended version of this operator, \\widetilde{D{{\\,\\textrm{SW}\\,}}}. The reason is that the standard Atiyah–Patodi–Singer boundary value problem as well as the elliptic theory developed in Sect. [2](https://link.springer.com/article/10.1007/s00029-023-00845-y#Sec6) can be directly applied to the study of \\widetilde{D{{\\,\\textrm{SW}\\,}}}. Our understanding of the gauge action (Sect. [3.2](https://link.springer.com/article/10.1007/s00029-023-00845-y#Sec11)) will allow us to transfer these properties to D{{\\,\\textrm{SW}\\,}}.

### 4.1 Extended linearized SW operator

Here we apply the Atiyah–Patodi–Singer boundary value problem to an extended version of the linearized Seiberg–Witten operator, \\widetilde{D{{\\,\\textrm{SW}\\,}}}. The properties we prove are the direct analogues of the properties of D{{\\,\\textrm{SW}\\,}} which are proved in the next section.

### Definition 4.1

(Extended linearized SW operator) We define the extended linearized Seiberg–Witten operator

![](https://media.springernature.com/lw284/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ128_HTML.png)

by adding a component related to the linearization of gauge action:

\\begin{aligned} \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}(a,\\phi ) = (d^\*a, D{{\\,\\textrm{SW}\\,}}\_{(A,\\Phi )}(a,\\phi )). \\end{aligned}

In order to study the Atiyah–Patodi–Singer boundary value problem we need to introduce the appropriate operator on the boundary and consider its Calderón projector. Denote Y = \\partial X and define

![](https://media.springernature.com/lw424/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ129_HTML.png)

This is a first-order self-adjoint elliptic operator. Denote by \\widetilde{H}^+(Y,{\\mathfrak {s}}) (resp. \\widetilde{H}^-(Y,{\\mathfrak {s}}) the closure of the span of positive (resp. nonpositive) eigenspaces of \\widetilde{L} in  L^2\_{1/2}(i \\Omega ^1(Y) \\oplus \\Gamma (S\_Y) \\oplus i \\Omega ^0(Y)), and by {\\widetilde{{\\Pi }}}^\\pm  the projection onto \\widetilde{H}^\\pm (Y,{\\mathfrak {s}}) along \\widetilde{H}^\\mp (Y,{\\mathfrak {s}}). The proof of the following proposition follows a standard argument; we briefly recall it to set up the stage for the proofs in the rest of this section.

### Proposition 4.2

(Semi-infinite-dimensionality of \\widetilde{D{{\\,\\textrm{SW}\\,}}}) The operator

![](https://media.springernature.com/lw383/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ9_HTML.png)

(11)


is Fredholm of index

![](https://media.springernature.com/lw296/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ10_HTML.png)

(12)


where ![](https://media.springernature.com/lw64/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq668_HTML.gif) is the index of ![](https://media.springernature.com/lw28/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq669_HTML.gif) with the Atiyah–Patodi–Singer (APS) spectral boundary condition (i.e., the index of

![](https://media.springernature.com/lw393/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ130_HTML.png)

where ![](https://media.springernature.com/lw37/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq670_HTML.gif) is the projection to the span ![](https://media.springernature.com/lw186/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq671_HTML.gif) of nonnegative eigenvectors of ![](https://media.springernature.com/lw28/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq672_HTML.gif)).

Moreover, the positive part of the restriction map from the kernel of \\widetilde{D{{\\,\\textrm{SW}\\,}}},  {\\widetilde{{\\Pi }}}^+ R: \\ker \\left(\\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}\\right) \\rightarrow \\widetilde{H}^+(Y,{\\mathfrak {s}}) , is compact.

### Proof

We can write \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} = \\widetilde{D} + \\widetilde{K} where

![](https://media.springernature.com/lw199/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ131_HTML.png)

and

\\begin{aligned} \\widetilde{K}(a,\\phi ) = (0, -\\rho ^{-1}(\\phi \\Phi ^\*+ \\Phi \\phi ^\*)\_0, \\rho (a) \\Phi + \\rho ({A}^\\delta ) \\phi ). \\end{aligned}

As explained in \[ [12](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR12 "Khandhawit, T.: A new gauge slice for the relative Bauer-Furuta invariants. Geom. Topol. 19(3), 1631–1655 (2015)"), Proposition 3.1\], applying the Atiyah–Patodi–Singer boundary value problem \[ [14](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR14 "Kronheimer, P.B., Mrowka, T.S.: Monopoles and Three-Manifolds. New Mathematical Monographs, vol. 10. Cambridge University Press, Cambridge (2007)"), Theorem 17.1.3\] to \\widetilde{D} proves that \\widetilde{D}\\oplus {\\widetilde{{\\Pi }}}R is Fredholm with index equal to ( [12](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ10)). Furthermore, \[ [14](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR14 "Kronheimer, P.B., Mrowka, T.S.: Monopoles and Three-Manifolds. New Mathematical Monographs, vol. 10. Cambridge University Press, Cambridge (2007)"), Theorem 17.1.3\] implies that for any bounded sequence ![](https://media.springernature.com/lw198/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq678_HTML.gif) such that  (\\widetilde{D}(u\_i))  is Cauchy, the sequence  ({\\widetilde{{\\Pi }}}^+R u\_i)  is precompact.

The operator \\widetilde{K} is compact by Theorem [A.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar92). Since \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} = \\widetilde{D} + \\widetilde{K}, thus \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} is Fredholm with the same index as \\widetilde{D}. Moreover, since \\widetilde{K} is compact, for any sequence  (u\_i) \\subset \\ker \\left(\\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}\\right) we can choose a subsequence such that the sequence of  \\widetilde{D}(u\_i) = - \\widetilde{K}(u\_i) is convergent, thus Cauchy. By what we proved in the previous paragraph, the sequence  ({\\widetilde{{\\Pi }}}^+R u\_i)  is precompact. This shows that  {\\widetilde{{\\Pi }}}^+ R: \\ker \\left(\\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}\\right) \\rightarrow \\widetilde{H}^+(Y,{\\mathfrak {s}})  is compact. \\square

The proof of surjectivity utilizes both of the analytical results of Sect. [2](https://link.springer.com/article/10.1007/s00029-023-00845-y#Sec6) (cf. \[ [21](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR21 "Lipyanskiy, M.: A semi-infinite cycle construction of Floer homology (2008). Thesis (Ph.D.)—Massachusetts Institute of Technology"), Theorem 2\]).

### Proposition 4.3

(Surjectivity of \\widetilde{D{{\\,\\textrm{SW}\\,}}}) The operator \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} is surjective.

### Proof
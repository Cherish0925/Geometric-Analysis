---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Smoothing Singular Extremal Kähler Surfaces and Minimal Lagrangians]

---
source_file: 1211_6957v3.pdf
converter: mathpix
format: mmd
---

\title{
SMOOTHING SINGULAR EXTREMAL KÄHLER SURFACES AND MINIMAL LAGRANGIANS
}

\author{
OLIVIER BIQUARD AND YANN ROLLIN
}

\begin{abstract}
Given a complex surface $\mathcal{X}$ with singularities of class $T$ and no nontrivial holomorphic vector field, endowed with a Kähler class $\Omega_{0}$, we consider smoothings $\left(\mathcal{M}_{t}, \Omega_{t}\right)$, where $\Omega_{t}$ is a Kähler class on $\mathcal{M}_{t}$ degenerating to $\Omega_{0}$. Under an hypothesis of non degeneracy of the smoothing at each singular point, we prove that if $\mathcal{X}$ admits an extremal metric in $\Omega_{0}$, then $\mathcal{M}_{t}$ admits an extremal metric in $\Omega_{t}$ for small $t$.
\end{abstract}

In addition, we construct small Lagrangian stationary spheres which represent Lagrangian vanishing cycles when $t$ is small.

\section*{1. Introduction}

Let $\mathcal{X}$ be a normal compact complex surface with singularities of class T. Such singularities are isolated and of orbifold type $\mathbb{C}^{2} / \Gamma$ for some finite group $\Gamma \subset \mathrm{U}_{2}$. The possible singularities are either rational double points $\left(\Gamma \subset \mathrm{SU}_{2}\right)$ or cyclic quotient singularities of type $\frac{1}{d n^{2}}(1, d n a-1)$, for positive integers $d, n, a$ such that $a$ and $n$ are relatively prime.

Since there is no general answer to the existence problem of constant scalar curvature Kähler metrics (CSCK for short), numerous constructions relying on gluing techniques have been made (cf. for instance [8, 1, 2]). In the case of canonical singularities (rational double points), the idea is to start from a CSCK orbifold metric on $\mathcal{X}$ and to deduce a smooth CSCK metric on the minimal resolution $\widehat{\mathcal{X}}$ by perturbation theory. The exceptional divisor of $\widehat{\mathcal{X}} \rightarrow \mathcal{X}$ is a union of holomorphic -2 spheres, whose configuration is described by the Dynkin diagram of a complex semisimple Lie algebra $\mathfrak{g}_{\mathbb{C}}$ determined by $\Gamma$ (this is a part of the McKay correspondence).

In this work we consider smoothings of singularities rather than resolutions. We prove, under natural hypotheses, that $\mathbb{Q}$-Gorenstein smoothings admit CSCK metrics.

In the special case of Kähler-Einstein metrics, the desingularizations cannot carry Kähler-Einstein metrics unless $c_{1}(\mathcal{X})=0$, since they contain holomorphic -2 spheres. But smoothings may carry Kähler-Einstein metrics, and our result gives a construction of those Kähler-Einstein metrics close to the singular ones. Also it is interesting to note that for general singularities of class T, the smoothings are not diffeomorphic to the minimal resolution.

If the homology class of a -2 sphere of the desingularization is Lagrangian in the smoothing, we prove that it can be represented by a small Hamiltonian stationary sphere. This gives a concrete construction of the Lagrangian minimizer, whose existence is proved by Schoen and Wolfson [9].
1.1. CSCK metrics. We now give precise statements. Let $\mathcal{X}$ be a normal complex surface with quotient singularities. We consider a $\mathbb{Q}$-Gorenstein smoothing
of $\mathcal{X}$, denoted $p: \mathcal{M} \rightarrow \Delta$, where $\Delta$ is an open disc centered at the origin in $\mathbb{C}$. This means that a multiple of the canonical divisor of $\mathcal{M}$ is Cartier and $\mathcal{M}$ is Cohen-Macaulay. Moreover, the central fiber is the given $\mathcal{X}$, and the general fiber $\mathcal{M}_{t}$ is smooth.

Kóllar and Shepherd-Barron [7] proved that the singularities which appear must be of class $T$; this class subdivides into two classes:
\begin{itemize}
\item[-] canonical singularities of type $\mathbb{C}^{2} / \Gamma$ for a finite subgroup $\Gamma \subset \mathrm{SU}_{2}$; one gets the list $A_{d}(d \geq 1), D_{d}(d \geq 4), E_{d}(d=6,7,8)$;
\item[-] cyclic quotients obtained by a quotient of a $A_{d n-1}$ singularity by $\mathbb{Z}_{n}$.
\end{itemize}

The local theory of smoothings of such a singularity is well understood: there is an (explicit) hypersurface $\mathcal{Y} \subset \mathbb{C}^{3} \times \mathbb{C}^{d}$, such that the projection $p: \mathcal{Y} \rightarrow \mathbb{C}^{d}$ is a $\mathbb{Q}$-Gorenstein smoothing of $\mathcal{Y}_{0} \simeq \mathbb{C}^{2} / \Gamma$. Moreover, any $\mathbb{Q}$-Gorenstein smoothing of $\mathcal{Y}_{0}$ is isomorphic to the pull-back of $p$ under a germ of holomorphic maps $f: \mathbb{C} \rightarrow \mathbb{C}^{d}$. The fibers $\mathcal{Y}_{t}=p^{-1}(t)$ over the discriminant locus $\mathcal{D} \subset \mathbb{C}^{d}$ are singular. This leads us to introduce a non degeneracy condition in the following way. As recalled below, there is a particular ramified covering map $\pi: \mathbb{C}^{d} \rightarrow \mathbb{C}^{d}$ associated to the singularity. This map is ramified exactly above $\mathcal{D}$, and moreover the ramification locus $\pi^{-1}(\mathcal{D})$, which turns out to be a union of linear hyperplanes:
$$\pi^{-1}(\mathcal{D})=\cup H_{i} .$$
Up to taking a ramified covering (which we choose of smallest possible degree), the germ $f: \mathbb{C} \rightarrow \mathbb{C}^{d}$ can be lifted to $\hat{f}: \mathbb{C} \rightarrow \mathbb{C}^{d}$ such that $f=\pi \circ \hat{f}$. The following definition is a way to say that the deformation is transversal to the discriminant locus:

Definition 1. We say that a smoothing $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ is non degenerate at the singular point $x \in \mathcal{X}$ if the corresponding $\hat{f}$ satisfies $\frac{\partial \hat{f}}{\partial t}(0) \notin \cup H_{i}$.

Example. Consider the $A_{k}$-singularity $w^{k+1}=x y$, desingularized by the family
$$x y=w^{k+1}+a_{k-1} w^{k-1}+a_{k-2} w^{k-2}+\cdots+a_{0} .$$
A deformation is given by a map $f(z)=\left(a_{0}(z), \ldots, a_{k-1}(z)\right)$. It is easy to check that if $\frac{\partial a_{0}}{\partial z} \neq 0$ then the deformation is non degenerate.

To state the theorem, we need to fix a Kähler class. Along a ray to the origin in $\Delta$, the Gauß-Manin connection identifies $H^{2}\left(\mathcal{M}_{t}, \mathbb{R}\right)$ with a fixed vector space; going to the origin, we identify this vector space with
$$H_{\text {orb }}^{2}(\mathcal{X}, \mathbb{R}) \oplus \underset{x \text { singular }}{\oplus} \mathbb{R}^{e_{x}}$$
where $e_{x}$ is the dimension of the real $H^{2}$ of the local smoothing of the singularity at $x$. As we shall see later, if $d_{x}$ is the dimension of the space of smoothings of the singularity at $x$,
$$e_{x}= \begin{cases}d_{x} & \text { for a canonical singularity, } \\ d_{x}-1 & \text { for other singularities. }\end{cases}$$
(One cannot get such an identification on the whole disk, because of the monodromy of the Gauß-Manin connection; but since the data of a Kähler class is real, it is natural to give it only on a ray).

The simplest form of our results can now be stated:

Theorem A. Suppose that we are given
\begin{itemize}
\item[-] a normal complex surface $\mathcal{X}$, with no holomorphic vector fields, and a $\mathbb{Q}$ -Gorenstein smoothing $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$, which is non degenerate at each singular point;
\item[-] along the ray $t \in \mathbb{R}_{+} \cap \Delta$, a Kähler class $\Omega_{t} \in H^{2}\left(\mathcal{M}_{t}, \mathbb{R}\right)$, depending smoothly on $t$, such that $\Omega_{0}$ is an orbifold Kähler class on $\mathcal{X}$, containing an orbifold CSCK metric.
\end{itemize}

Then for small $t>0$ the class $\Omega_{t}$ contains a CSCK metric on $\mathcal{M}_{t}$.
The behavior of the CSCK metric for $t$ small is well understood: outside the singularities it converges to the orbifold CSCK metric on $\mathcal{X}$, but near a singularity $x$ some rescaling converges to an ALE Kähler Ricci flat space, which appears as the 'bubble' at $x$.

One special case is when the smoothing is given with a polarization $\Omega$, resulting in a constant $\Omega_{t}$. This covers in particular the Kähler-Einstein case: when $\Omega_{t}=$ $\pm c_{1}\left(\mathcal{M}_{t}\right)$ our result gives a construction of the Kähler-Einstein metric on the smoothing of $\mathcal{X}$, as well as a concrete description of its degeneracy to an orbifold Kähler-Einstein metric. This Kähler-Einstein picture is recently obtained in the case of $A_{1}$ singularities by Spotti [10].

Complex orbifold singularities of codimension at least 3 are rigid by a result of Schlessinger. However, it would be interesting to extend our results in dimension 3 or more, allowing orbifold singularities of codimension 2. A natural problem would be to remove the triviality assumption of the automorphism group: one may expect the existence of the CSCK metric to be related to a K-stability property, like in [12].

One can replace the non degeneracy hypothesis on the smoothing $\mathcal{M}_{t}$ by a weaker non degeneracy hypothesis on the data $\left(\mathcal{M}_{t}, \Omega_{t}\right)$ of the smoothing with the Kähler class. This requires slightly more material that we now explain.

Let us come back to the $\mathbb{Q}$-Gorenstein smoothing $\mathcal{Y} \rightarrow \mathbb{C}^{d}$ of a canonical singularity. The parameter space $\mathbb{C}^{d}$ can be identified with $\mathfrak{h}_{\mathbb{C}} / W$, where $\mathfrak{h}_{\mathbb{C}}$ is a Cartan subalgebra of the Lie algebra $\mathfrak{g}_{\mathbb{C}}$ associated to $\Gamma$ by the McKay correspondence $\left(\mathfrak{g}_{\mathbb{C}}\right.$ is exactly the $A_{d}, D_{d}$ or $E_{d}$ simple Lie algebra), and $W$ is the Weyl group. Here the canonical projection $\mathfrak{h}_{\mathbb{C}} \rightarrow \mathbb{C}^{d}$ is ramified over the discriminant locus $\mathcal{D} \subset \mathbb{C}^{d}$. The real 2-cohomology is isomorphic to the real Cartan subalgebra $\mathfrak{h}_{\mathbb{R}}$ (actually, the smoothing is diffeomorphic to the minimal resolution, whose -2 spheres give a basis of $\left.\left(\mathfrak{h}_{\mathbb{R}}\right)^{*}\right)$. But there is some ambiguity in this identification, because the monodromy of the Gauß-Manin connection is given by the action of $W$.

In the smoothing $\mathcal{Y} \rightarrow \mathbb{C}^{d}=\mathfrak{h}_{\mathbb{C}} / W$, the general fiber is smooth, but there are singular fibers, given by the walls of the Weyl chambers of $\mathfrak{h}_{\mathbb{C}}$. Nevertheless, there exist a simultaneous resolution of singularities $\widehat{\mathcal{Y}} \rightarrow \mathfrak{h}_{\mathbb{C}}$ (Brieskorn, Slodowy). Then all the fibers are smooth and their real 2-cohomology can be identified to $\mathfrak{h}_{\mathbb{R}}$.

The case of the other T singularities is similar: they are quotients of $A_{d n-1}$ singularities by a $\mathbb{Z}_{n}$ action, and one obtains the same structure by taking the $\mathbb{Z}_{n}$ fixed points of the $A_{d n-1}$ simultaneous resolution: the space of parameters is therefore $\mathfrak{h}_{\mathbb{C}}^{\mathbb{Z}_{n}} \simeq \mathbb{C}^{d}$, and the real 2-cohomology is $\mathfrak{h}_{\mathbb{R}}^{\mathbb{Z}_{n}} \simeq \mathbb{R}^{d-1}$.

Now come back to our setup of a smoothing $\mathcal{M} \rightarrow \Delta$ with a family of Kähler classes $\Omega_{t}$. At a singular point $x \in \mathcal{X}$, the smoothing is induced from the standard
smoothing $\mathcal{Y}$ by a map (we denote the dependence in $x$ by an index $x$ )
$$f_{x}: \Delta_{c} \longrightarrow\left(\left(\mathfrak{h}_{\mathbb{C}}\right)_{x} / W_{x}\right)^{G_{x}},$$
where $G_{x}=1$ for a canonical singularity, and $\Delta_{c} \subset \Delta$ is a smaller disk of radius $c$. Up to a finite ramified covering $\Delta_{b} \rightarrow \Delta_{c}$, we can lift this map into a map into $\left(\mathfrak{h}_{\mathbb{C}}\right)_{x}^{G_{x}}$ :
$$\left(\zeta_{c}\right)_{x}: \Delta_{b} \longrightarrow\left(\mathfrak{h}_{\mathbb{C}}\right)_{x}^{G_{x}} .$$

Up to taking a higher degree covering, we can take the same covering $\Delta_{b} \rightarrow \Delta_{c}$, say of order d, for all singular points. Adding the data $\left(\zeta_{r}\right)_{x}$ of the Kähler class in a neighborhood of the singularity, we obtain at each singularity a map
$$\zeta_{x}: \Delta_{b} \longrightarrow\left(\mathfrak{h}_{\mathbb{R}}\right)_{x}^{G_{x}} \oplus\left(\mathfrak{h}_{\mathbb{C}}\right)_{x}^{G_{x}}, \quad \zeta_{x}=\left(\left(\zeta_{r}\right)_{x},\left(\zeta_{c}\right)_{x}\right),$$
which represents the deformation of both the Kähler parameter and the complex parameter. We consider the Kähler class as depending smoothly on the parameter on $\Delta_{b}$ (since $\Delta_{b}$ is a covering, this is more general than the setting of Theorem A). Then at the origin we have for some integer $p$
$$\zeta_{x}(t)=t^{p} \dot{\zeta}_{x}+O\left(t^{p+1}\right) .$$
We can now define an extended notion of non degeneracy:
Definition 2. We say that $\left(\mathcal{M}_{t}, \Omega_{t}\right)$ is non degenerate at the point $x$ if $p \leq \mathbf{d}$ and $\dot{\zeta}_{x}$ does not belong to a wall of a Weyl chamber.

The above definition is clearly a generalization of Definition 1. We now extend Theorem A under the form:

Theorem B. Suppose that we are given
\begin{itemize}
\item[-] a normal complex surface $\mathcal{X}$, with no holomorphic vector fields, and a $\mathbb{Q}$-Gorenstein smoothing $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$;
\item[-] along the ray $t \in \mathbb{R}_{+} \cap \Delta_{b}$, a Kähler class $\Omega_{t} \in H^{2}\left(\mathcal{M}_{t}, \mathbb{R}\right)$, such that $\Omega_{0}$ is an orbifold Kähler class on $\mathcal{X}$, containing an orbifold CSCK metric.
\end{itemize}
If $\left(\mathcal{M}_{t}, \Omega_{t}\right)$ is non degenerate at each singular point in the sense of Definition 2, then for small $t>0$ the class $\Omega_{t}$ contains a CSCK metric on $\mathcal{M}_{t}$.

There is a final extension of the results in the case of canonical singularities: then we do not need the initial family $\mathcal{M}$ to be a smoothing. Indeed suppose that $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ is any deformation of a surface with rational double points, then near each singularity $x$, the family is still induced by some map $\Delta_{c} \rightarrow\left(\mathfrak{h}_{\mathbb{C}}\right)_{x} / W_{x}$ (because this is a semi-universal deformation), which can again be lifted to $\left(\zeta_{c}\right)_{x}$ : $\Delta_{b} \rightarrow\left(\mathfrak{h}_{\mathbb{C}}\right)_{x}$. Pulling back $\widehat{\mathcal{Y}} \rightarrow\left(\mathfrak{h}_{\mathbb{C}}\right)_{x}$ near each singular point, we obtain a simultaneous resolution $\widehat{\mathcal{M}} \rightarrow \Delta_{b}$ of the singularities of $\mathcal{M} \rightarrow \Delta$ and we can apply our method in this setting to obtain:

Theorem C. Suppose that we are given
\begin{itemize}
\item[-] a normal complex surface $\mathcal{X}$, with no holomorphic vector fields, with only rational double points, and a deformation $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$; let then $\widehat{\mathcal{M}} \rightarrow \Delta_{b}$ the simultaneous resolution of singularities as above;
\item[-] along the ray $t \in \mathbb{R}_{+} \cap \Delta_{b}$, a Kühler class $\Omega_{t} \in H^{2}\left(\widehat{\mathcal{M}}_{t}, \mathbb{R}\right)$, such that $\Omega_{0}$ is an orbifold Kähler class on $\mathcal{X}$, containing an orbifold CSCK metric.
\end{itemize}

If $\left(\widehat{\mathcal{M}}_{t}, \Omega_{t}\right)$ is non degenerate at each singular point in the sense of Definition 2, then for small $t>0$ the class $\Omega_{t}$ contains a CSCK metric on $\widehat{\mathcal{M}}_{t}$.

This result covers the known case of minimal resolutions, but also the case of partial resolutions which are not smoothings. It is not valid for $T$ singularities because the deformations include other components that are not induced from the $\mathbb{Q}$-Gorenstein smoothing $\mathcal{Y}$.
1.2. Hamiltonian stationary spheres. Suppose we are under the hypothesis of Theorem B. As we have seen,
$$H^{2}\left(\mathcal{M}_{t}, \mathbb{R}\right)=H_{\text {orb }}^{2}(\mathcal{X}, \mathbb{R}) \oplus \oplus_{x \text { singular }}\left(\mathfrak{h}_{\mathbb{R}}\right)_{x}^{G_{x}} .$$
Fix a singular point $x$, and a system $\Re_{x}^{+} \subset\left(\mathfrak{h}_{\mathbb{C}}\right)_{x}^{*}$ of positive roots. If $x$ is a rational double point $\left(G_{x}=1\right)$, a root $\theta \in \Re_{x}^{+}$represents an integral homology class on $\mathcal{M}_{t}$; in general, $\theta$ represents a homology class in the local $G_{x}$-covering, so after projection still represents a (possibly zero) homology class in $\mathcal{M}_{t}$.

Remind that the deformation $\left(\mathcal{M}_{t}, \Omega_{t}\right)$ is given near the singular point $x$ by a map $\zeta_{x}=\left(\zeta_{r}\right)_{x}+\left(\zeta_{c}\right)_{x}: \Delta_{b} \rightarrow\left(\mathfrak{h}_{\mathbb{R}}\right)_{x}^{G_{x}} \oplus\left(\mathfrak{h}_{\mathbb{C}}\right)_{x}^{G_{x}}$, in which $\left(\zeta_{r}\right)_{x}(t)$ represents the class of the restriction of $\Omega_{t}$ near the singularity. Therefore the homology class defined by $\theta$ is $\Omega_{t}$-Lagrangian if $\left\langle\theta,\left(\zeta_{r}\right)_{x}(t)\right\rangle \equiv 0$, which implies in particular $\left\langle\theta,\left(\dot{\zeta}_{r}\right)_{x}\right\rangle=0$.

Theorem D. Suppose that we are under the hypothesis of Theorem B or C. Fix a singular point $x \in \mathcal{X}$ and a root $\theta \in \Re_{x}^{+}$, such that $\left\langle\theta,\left(\dot{\zeta}_{r}\right)_{x}\right\rangle=0$, and $\theta$ is primitive for this property (that is cannot decompose as $\theta_{1}+\theta_{2}$ with $\theta_{i} \in \Re_{x}^{+}$satisfying the same property). Finally suppose that for all $t>0$, one has $\left\langle\theta,\left(\zeta_{r}\right)_{x}(t)\right\rangle \equiv 0$, that is the homology class represented by $\theta$ remains $\Omega_{t}$-Lagrangian. Then:
\begin{itemize}
\item[(1)] If $x$ is a rational double point, then the homology class in $\mathcal{M}_{t}$ (or $\widehat{\mathcal{M}}_{t}$ in the setting of Theorem C) corresponding to $\theta$ is represented by a smooth Hamiltonian stationary sphere $S_{t}$, which is also a global Lagrangian minimizer of the area in its homotopy class.
\item[(2)] If $G_{x}=\mathbb{Z}_{n}$, and if the homology class defined by $\theta$ is nonzero, then it is represented by a smooth Hamiltonian stationary sphere $S_{t}$.
\end{itemize}

Moreover (see section 5), one gets an explicit description when $t \rightarrow 0$ : after dilations, the Hamiltonian stationary representative of $\theta$ converges to a special Lagrangian sphere in the ALE Kähler Ricci flat space obtained at the limit.

In the second case $\left(G_{x}=\mathbb{Z}_{n}\right)$, if the homology class defined by $\theta$ in the quotient vanishes, one can still get in some cases a Hamiltonian stationary embedded $S^{2}$ or $\mathbb{R P}^{2}$, see section 6.2. We do not state a minimizing property which is less clear, because the models in the ALE Kähler Ricci flat space are not calibrated.

For example, from Theorem A we recover Kähler-Einstein metrics on certain 4-point blowup of $\mathbb{C P}^{2}$ constructed by Tian [13], and Theorem D provides a construction of stationary Lagrangian spheres (cf §7.1).
1.3. Organization of the paper. In most of the article, we suppose that $\mathcal{X}$ has only canonical singularities and we prove directly Theorem C, which implies Theorem A, Theorem B) and Theorem D. At the end, we explain the case of general singularities of the class T: there is not much change, because they are obtained as cyclic quotients of canonical singularities and all our constructions pass to the quotient.

One of the main point in the paper is the construction of 'good' Kähler metrics on the deformations: this is not obvious, because the complex structure changes. It turns out that what is needed is an extension to the singular setting of the theorem of Kodaira on the stability of the Kähler condition under complex deformations. This is done in section 3, after the introduction of the 'tangent graviton' in section 2. In section 4, we extend arguments in the literature to produce the CSCK metrics, so we only point out the new features in our situation. In section 5, we produce the Hamiltonian stationary Lagrangian spheres. The case of general singularities is explained in section 6, and some applications are given in section 7.
1.4. Acknowledgements. The authors would like to thank Claude Le Brun for some stimulating discussions.

\section*{2. Deformations of singular surfaces and Kähler classes}

In this section, $\mathcal{X}$ will always denote a compact complex surface with canonical singularities endowed with an orbifold Kähler metric $\bar{g}$ with Kähler form $\bar{\omega}$ and Kähler class $\Omega_{0}$. We consider a flat deformation $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ of $\mathcal{X}$.
2.1. Complex deformations near singularities. Our first goal is to understand a simultaneous resolution $\widehat{\mathcal{X}} \hookrightarrow \widehat{\mathcal{M}} \rightarrow \Delta_{d}$ of the deformation, focusing near the singular points. For this purpose, we choose a set of adapted isomorphisms $U_{i} \simeq \Delta_{\varepsilon_{i}}^{2} / \Gamma_{i}$ near each singularity $x_{i} \in \mathcal{X}$. Actually, for simplicity of notations we will suppose that there is only one singular point $x_{0}$, and we will point out from place to place what changes for several singular points. So near $x_{0}$, one can choose local coordinates $z$ with values in $\Delta_{\varepsilon}^{2}$ defined modulo $\Gamma$, such that the pullback of $\bar{\omega}$ on the disc is expressed as
$$d d^{c}\left(|z|^{2}+\eta\right)$$
where $|z|$ is the Euclidean distance to the origin in $\mathbb{C}^{2}$ and $\eta$ is a smooth $\Gamma$-invariant real function such that $\eta=\mathcal{O}\left(|z|^{4}\right)$. Up to scaling the metric, and shrinking the open set $U$, we may assume that $\varepsilon=1$. In the sequel, we shall always assume that the identification $U \simeq \Delta^{2} / \Gamma$ is chosen in such a way.

By restricting $\mathcal{M}$ to a suitable neighborhood of the singular point $x_{0}$, we deduce a flat deformation
$$\Delta^{2} / \Gamma \hookrightarrow \mathcal{N} \rightarrow \Delta_{c}$$
of the singularity $U=\mathcal{N}_{0}$. The singularity $U$ admits a semi-universal flat family of deformations by a result of Kas-Schlessinger [6]: there is a deformation
$$\mathbb{C}^{2} / \Gamma \hookrightarrow \mathcal{Y} \rightarrow \mathfrak{h}_{\mathbb{C}} / W,$$
where $\mathfrak{h}_{\mathbb{C}}$ is a Cartan subalgebra of the complex semisimple Lie algebra associated to the Dynkin diagram of the singularity (this is the Lie algebra associated to the finite group $\Gamma$ by the McKay correspondence), and $W$ is the Weyl group. Then, $\mathcal{N}$ is induced by some holomorphic map $\psi: \Delta_{c} \rightarrow \mathfrak{h}_{\mathbb{C}} / W$. Thus, there is a
holomorphic commutative diagram
![](https://cdn.mathpix.com/cropped/911d392c-4fdb-42b8-a6b9-5cd96a58272a-07.jpg?height=350&width=308&top_left_y=583&top_left_x=927)
such that the restriction $\Psi: \mathcal{N}_{t} \rightarrow \mathcal{Y}_{\psi(t)}$ is an embedding for every $t \in \Delta_{c}$.
A remarkable feature of canonical singularities is that $\mathbb{C}^{2} / \Gamma \hookrightarrow \mathcal{Y} \rightarrow \mathfrak{h}_{\mathbb{C}} / W$ admits a simultaneous resolution $\widehat{\mathbb{C}^{2} / \Gamma} \hookrightarrow \widehat{\mathcal{Y}} \rightarrow \mathfrak{h}_{\mathbb{C}}$ given by a diagram
![](https://cdn.mathpix.com/cropped/911d392c-4fdb-42b8-a6b9-5cd96a58272a-07.jpg?height=361&width=304&top_left_y=1147&top_left_x=930)
where the map $\mathfrak{h}_{\mathbb{C}} \rightarrow \mathfrak{h}_{\mathbb{C}} / W$ is the canonical projection (Brieskorn, Slodowy).
A priori, one cannot lift the map $\psi: \Delta_{c} \rightarrow \mathfrak{h}_{\mathbb{C}} / W$ to $\mathfrak{h}_{\mathbb{C}}$. The obstruction is the monodromy of $\psi$, which lies in $W$. By taking a ramified cover, with order d equal to the order of the monodromy of $\psi$, we obtain a lifting
![](https://cdn.mathpix.com/cropped/911d392c-4fdb-42b8-a6b9-5cd96a58272a-07.jpg?height=215&width=286&top_left_y=1754&top_left_x=939)
If there are several singular points, one has to take the order to be the least common multiple of the orders at each point.

Thus, the family of deformations $\mathcal{N}^{\prime}=\Delta_{d} \times_{r_{k}} \mathcal{N}$ admits a simultaneous resolution $\widehat{\mathcal{N}} \rightarrow \mathcal{N}^{\prime}$ and we have a commutative holomorphic diagram
![](https://cdn.mathpix.com/cropped/911d392c-4fdb-42b8-a6b9-5cd96a58272a-07.jpg?height=484&width=560&top_left_y=2216&top_left_x=804)
where the maps $\Psi$ an $\hat{\Psi}$ restrict to fiberwise embeddings. Here we should point out that the maps also commute with the embeddings $\widehat{\Delta^{2} / \Gamma} \hookrightarrow \widehat{\mathcal{N}}, \Delta^{2} / \Gamma \hookrightarrow \mathcal{N}$, $\widehat{\mathbb{C}^{2} / \Gamma} \hookrightarrow \widehat{\mathcal{Y}}, \mathbb{C}^{2} / \Gamma \hookrightarrow \mathcal{Y}$ and the canonical inclusion $\Delta^{2} \hookrightarrow \mathbb{C}^{2}$.

Remark 3. The fact that deformations of simple singularities do admit simultaneous resolutions after passing to a sufficiently high ramified cover, as recalled above, is the essential ingredient used in [6] to construct a simultaneous resolution for deformations of compact complex surfaces with canonical singularities.

Remark 4. Conversely, if the simultaneous resolution $\widehat{\mathcal{X}} \hookrightarrow \widehat{\mathcal{M}} \rightarrow \Delta_{d}$ is already given as a data, the preimage $\widehat{\mathcal{N}}$ of $\mathcal{N}$ via the map $\widehat{\mathcal{M}} \rightarrow \mathcal{M}$ provides a simultaneous resolution of the deformation of the singularity for free. However, by a universal property of simultaneous resolutions of canonical singularities [4], it turns out that $\widehat{\Delta^{2} / \Gamma} \hookrightarrow \widehat{\mathcal{N}} \rightarrow \Delta_{d}$ must be given by the above construction.
2.2. Kronheimer's gravitons. The simultaneous resolution $\widehat{\mathcal{Y}} \rightarrow \mathfrak{h}_{\mathbb{C}}$ of the semiuniversal family of deformations $\mathcal{Y} \rightarrow \mathfrak{h}_{\mathbb{C}} / W$ is explicitly constructed by Kronheimer. At this point, we need more details. Kronheimer actually constructs a family $Y_{\zeta}$ of hyperKähler manifolds, parameterized by a triple $\zeta=\left(\zeta_{1}, \zeta_{2}, \zeta_{3}\right) \in$ $\mathfrak{h} \otimes \mathbb{R}^{3}$. To explain its properties, we choose a positive root system $\Re^{+} \subset \mathfrak{h}^{*}$, and for a root $\theta \in \Re^{+}$we define a hyperplane of $\mathfrak{h}$ by
$$D_{\theta}=\operatorname{ker} \theta .$$
Then the family $\left(Y_{\zeta}\right)$ has the following properties:
\begin{itemize}
\item[(1)] $Y_{\zeta}$ is a smooth manifold if
$$\zeta \notin D=\cup_{\theta \in \Re+} \mathbb{R}^{3} \otimes D_{\theta} ;$$
\item[(2)] all $\left(Y_{\zeta}\right)_{\zeta \notin D}$ are diffeomorphic to the minimal resolution $\widehat{\mathbb{C}^{2} / \Gamma}$ of $\mathbb{C}^{2} / \Gamma$; the diffeomorphism
$$F_{\zeta}: \widehat{\mathbb{C}^{2} / \Gamma} \xrightarrow{\sim} Y_{\zeta}$$
can be chosen so that the metric is asymptotic to the Euclidean metric: actually there is an asymptotic development at any order
$$F_{\zeta}^{*} \mathrm{~g}_{\zeta}=g^{\mathrm{euc}}+\sum_{i=2}^{k-1} g_{\zeta}^{i} R^{-2 i}+\mathcal{O}\left(R^{-2 k}\right)$$
where $g_{\zeta}^{i}$ is a homogeneous polynomial in $\zeta$ of degree $i$; in the sequel, we will suppose that such a diffeomorphism is chosen (this is possible smoothly in the $\zeta$ parameter because $\mathfrak{h} \otimes \mathbb{R}^{3}-D$ is simply connected);
\item[(3)] $H^{2}\left(Y_{\zeta}, \mathbb{R}\right)$ is identified with $\mathfrak{h}$ in such a way that the homology classes of the -2 curves of the resolution get identified with the simple roots of $\mathfrak{h}$ (and so $H_{2}\left(Y_{\zeta}, \mathbb{Z}\right)$ is identified with the root lattice of $\mathfrak{h}$ ); under this identification, the cohomology classes of the three Kähler forms $\left(\omega_{1}, \omega_{2}, \omega_{3}\right)$ of $Y_{\zeta}$ are $\zeta_{1}$, $\zeta_{2}$ and $\zeta_{3}$;
\item[(4)] there is a $\mathrm{SO}_{3}$ action which for $u \in \mathrm{SO}_{3}$ identifies isometrically
$$Y_{\zeta} \longrightarrow Y_{u(\zeta)},$$
permuting $\left(\omega_{1}, \omega_{2}, \omega_{3}\right)$ to $u\left(\omega_{1}, \omega_{2}, \omega_{3}\right)$;
\end{itemize}
\begin{itemize}
\item[(5)] when we want to underline the holomorphic symplectic structure ( $I_{1}, \omega_{2}+$ $\left.i \omega_{3}\right)$ of $Y_{\zeta}$, we use the notation $Y_{\zeta_{r}, \zeta_{c}}$, where $\zeta_{r}=\zeta_{1}$ and $\zeta_{c}=\zeta_{2}+i \zeta_{3} \in \mathfrak{h}_{\mathbb{C}}$; then there is a $\mathbb{C}^{*}$-action, giving for $\lambda \in \mathbb{C}^{*}$ an isomorphism of holomorphic symplectic manifolds, which is actually also an isometry,
$$H_{\lambda}: Y_{\zeta_{r}, \zeta_{c}} \longrightarrow \frac{1}{|\lambda|^{2}} Y_{|\lambda|^{2} \zeta_{r}, \lambda^{2} \zeta_{c}} ;$$
Here the leading fraction means that the metric has been rescaled by a factor $\frac{1}{|\lambda|^{2}}$.
\item[(6)] if $\zeta_{r} \notin \cup_{\theta \in R_{+}} D_{\theta}$, then there is a map $Y_{\zeta_{r}, \zeta_{c}} \rightarrow Y_{0, \zeta_{c}}$ which is a minimal resolution of singularities, actually $Y_{\zeta_{r}, \zeta_{c}}$ and $Y_{0, \zeta_{c}}$ are the fibers $\widehat{\mathcal{Y}}_{\zeta_{c}}$ and $\mathcal{Y}_{\zeta_{c}}$ of the simultaneous resolution (2.2).
\end{itemize}

Remark 5. In this paper, the notation $\mathcal{O}\left(R^{k}\right)$ for a function $f$ on $\mathbb{C}^{2}$, or more generally a tensor, means that when $R$ goes to $\infty$, then for any integer $l=0,1, \ldots$, one has $\nabla^{l} f=\mathcal{O}\left(R^{k-l}\right)$.

We now point out the statement which will be central in this paper: it gives the geometric meaning of the walls $D_{\theta}$.

Lemma 6. Suppose $\theta$ is a root and $\zeta \notin D$, so $\theta$ corresponds to some homology class in $H_{2}\left(Y_{\zeta}, \mathbb{Z}\right)$.
\begin{itemize}
\item[1)] If $\zeta_{1} \in \operatorname{ker} \theta$, then $\theta$ is a Lagrangian homology class for $Y_{\zeta_{1}, \zeta_{c}}$.
\item[2)] If $\zeta_{c} \in \operatorname{ker} \theta$, then $\theta$ is represented by a holomorphic cycle in $Y_{\zeta_{1}, \zeta_{c}}$; moreover if $\theta$ is primitive for this property (that is cannot be written as $\theta_{1}+\theta_{2}$, with $\theta_{i} \in \Re^{+}$ and $\zeta_{c} \in \operatorname{ker} \theta_{i}$ ), then $\theta$ is represented by a holomorphic sphere.
\end{itemize}

The condition $\zeta \notin D_{\theta}$ can now be understood in terms of this lemma: indeed, if $\zeta \in D_{\theta}$, then both $\zeta_{r}, \zeta_{c} \in \operatorname{ker} \theta$ which means that $\theta$ would represent at the same time a Lagrangian class and a holomorphic cycle, which is impossible, so $Y_{\zeta_{r}, \zeta_{c}}$ has to be singular.

The first part of the lemma is obvious from (iii). The second part is basically contained in the work of Brieskorn and Slodowy on Kleinian singularities. By property (vi), the holomorphic map $Y_{\zeta_{r}, \zeta_{c}} \rightarrow Y_{0, \zeta_{c}}=\mathcal{Y}_{\zeta_{c}}$ is a minimal resolution of singularities, but the semi-universal deformation $\mathcal{Y}$ is explicit and its singularities are completely understood: the discriminant locus $\mathcal{D} \subset \mathbb{C}^{k}=\mathfrak{h} / W$, that is the set of $v \in \mathbb{C}^{k}$ such that $\mathcal{Y}_{v}$ is singular, is exactly the branch locus of the projection $\mathfrak{h}_{\mathbb{C}} \rightarrow \mathfrak{h}_{\mathbb{C}} / W$, i.e. the projection of the kernels of the roots. (And the monodromy representation $\pi_{1}\left(\mathbb{C}^{k}-\mathcal{D}\right) \rightarrow \operatorname{Aut} H^{2}\left(\mathcal{Y}_{v_{0}}, \mathbb{C}\right)$ is the standard representation of $W$ on $\mathfrak{h} \mathbb{C}$ ).

If $\zeta_{c} \in \operatorname{ker} \theta$ for only one root $\theta$ (this is the generic case), then $\mathcal{Y}_{\zeta_{c}}$ has a singular point with a singularity of type $\mathbb{C}^{2} / \mathbb{Z}_{2}$, giving a -2 holomorphic sphere in the minimal resolution $Y_{\zeta_{r}, \zeta_{c}}$, in the homology class corresponding to $\theta$. For a general $\zeta_{c} \in \operatorname{ker} \theta$, then of course $\theta$ is still represented by a holomorphic cycle in $Y_{\zeta_{r}, \zeta_{c}}$, which might be a union of several curves if it can be decomposed as a sum of roots $\theta=\theta_{1}+\cdots+\theta_{\ell}$ such that $\zeta_{c} \in \operatorname{ker} \theta_{i}$.

Remark 7. The $A_{k}$-gravitational instantons are known explicitly (multi-Eguchi-Hanson metrics given by the Gibbons-Hawking ansatz). In that case one can see explicitly the holomorphic cycles of Lemma 6.
2.3. The tangent graviton. We come back to our setting of a flat deformation $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ of a Kähler orbifold surface $\mathcal{X}$ with a simultaneous resolution $\widehat{\mathcal{X}} \hookrightarrow$ $\widehat{\mathcal{M}} \rightarrow \Delta_{d}$ after passing to a ramified cover. We deduce a family of deformations of the singularity $\Delta^{2} / \Gamma \hookrightarrow \mathcal{N} \rightarrow \Delta_{c}$ and a simultaneous resolution $\widehat{\Delta^{2} / \Gamma} \hookrightarrow \widehat{\mathcal{N}} \rightarrow$ $\Delta_{d}$. As explained in §2.1 we have a morphism
![](https://cdn.mathpix.com/cropped/911d392c-4fdb-42b8-a6b9-5cd96a58272a-10.jpg?height=210&width=203&top_left_y=768&top_left_x=980)
The cohomology class $\Omega_{t}$ defined for $t \in \Delta_{d} \cap \mathbb{R}^{+}$, restricted to $\widehat{\mathcal{N}}_{t}$ defines a class on $\widehat{\mathcal{Y}}_{\hat{\psi}(t)}$ identified to an element $\zeta_{r}(t) \in \mathfrak{h}$. So that the whole data $\left(\widehat{\mathcal{Y}}_{\hat{\psi}(t)}, \zeta_{r}(t)\right)$ is exactly that of the Kronheimer graviton $Y_{\zeta_{r}(t), \zeta_{c}(t)}$ with the definition $\zeta_{c}(t)=\hat{\psi}(t)$. In view of Lemma 6, it is clear that the parameters $\left(\zeta_{r}(t), \zeta_{c}(t)\right)$ satisfy condition (2.5), so $Y_{\zeta_{r}(t), \zeta_{c}(t)}$ is smooth.

The fact that $\Omega_{t}$ converges to an orbifold Kähler class $\Omega_{0}$ means that $\zeta_{r}(t)$ converges to 0 , and we suppose that it depends smoothly on the parameter $t$, including at $t=0$.

We assume that the map
$$\begin{aligned}
\zeta: \Delta_{d} \cap \mathbb{R}^{+} & \rightarrow \mathfrak{h} \oplus \mathfrak{h}_{\mathbb{C}} \\
t & \mapsto\left(\zeta_{r}(t), \zeta_{c}(t)\right)
\end{aligned}$$
does not vanish at infinite order at $t=0$ and introduce the first nonzero derivative $\dot{\zeta}$ for some order $p>0$. This means that
$$\zeta(t)=t^{p} \dot{\zeta}+O\left(t^{p+1}\right)$$
for some $p>0$ and $\dot{\zeta} \neq 0$.
The domain $\widehat{\mathcal{N}}_{t}$ identifies to a small domain of $Y_{\zeta(t)}$. Zooming by a factor $\varepsilon^{-1}=t^{-p / 2}$, and multiplying the Kähler class by a factor $\varepsilon^{-2}=t^{-p}$, we obtain by (2.6) that this domain is identified via $H_{t^{-p / 2}}$ with a larger and larger domain in $Y_{\varepsilon^{-2} \zeta(t)}$, which converges to $Y_{\dot{\zeta}}$ on compact subsets.

This discussion motivates:
Definition 8. The Kronheimer space $Y_{\dot{\zeta}}$ is called the tangent graviton to the deformation $\left(\widehat{\mathcal{N}},\left.\Omega_{t}\right|_{\widehat{\mathcal{N}_{t}}}\right)$.

Remark 9. There are choices in the construction of $\dot{\zeta}$ :
\begin{itemize}
\item[-] the choice of lifting to the simultaneous resolution is done up to the action of the Weyl group $W$, acting on the parameter $\zeta_{c}(t)$ : but this does not change the space $Y_{\zeta_{r}(t), \zeta_{c}(t)}$;
\item[-] the choice of a coordinate in the disc: since we have chosen a real ray, the ambiguity is the rescaling by a real $\lambda>0$, but in view of (2.6), this amounts to rescale the graviton.
\end{itemize}

Remark 10. If the restriction of $\Omega_{t}$ to $\widehat{\mathcal{N}}_{t}$ is identically zero, then $\zeta_{r}(t) \equiv 0$. In this case, as $\zeta$ is a holomorphic map and the nonzero derivative $\dot{\zeta}$ can be defined without restricting to a particular ray in $\Delta_{d}$. Thus, all the above definition make
sense if we allow $t \in \Delta_{d}$. This property is of special interest in the case of polarized smoothings.

\section*{3. Representing Kähler classes}

The one point blowup of a complex manifold endowed with a Kähler metric $\omega$, carries a family of Kähler metric $\omega_{\varepsilon}$. This is a very nice argument due to Kodaira in which the metric $\omega_{\varepsilon}$ can be constructed almost explicitly. The construction of $\omega_{\varepsilon}$ is done by cut and paste, where the Burns-Simanca metric defined on a neighborhood of the exceptional divisor is glued with the original metric. As $\varepsilon \rightarrow 0$, the metrics $\omega_{\varepsilon}$ converge smoothly away from the exceptional divisor toward the original metric $\omega$.

The aim of the current section is to prove a similar result for families of deformations of a Kähler orbifold surface with isolated singularities. In particular, we shall prove the following proposition.

Proposition 11. Let $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ be a family of deformations of a compact complex surface with canonical singularities. Let $\bar{\omega}$ be an orbifold Kähler metric on $\mathcal{X}$ with Kähler class $\Omega_{0}$ and $\Omega$ a family of Kähler classes supported by a simultaneous resolution $\widehat{\mathcal{X}} \rightarrow \widehat{\mathcal{M}} \rightarrow \Delta_{d}$ degenerating toward $\Omega_{0}$, such that the variation of Kähler class and complex structure is non degenerate in the sense of Definition 2.

Then, there exists a family of Kähler metrics $g_{t}$ with Kähler forms $\omega_{t}$ on $\widehat{\mathcal{M}}_{t}$ defined for $t \in \Delta_{d} \cap(0,+\infty)$ and a smooth trivialization $\phi: \Delta_{d} \times \widehat{\mathcal{X}} \rightarrow \widehat{\mathcal{M}}$ identifying all the fibers $\mathcal{M}_{t}$ with the property that
\begin{itemize}
\item[-] $\left[\omega_{t}\right]=\Omega_{t}$;
\item[-] the family of metrics $g_{t}$ converges in the $C^{2}$-sense toward the orbifold metric $\bar{g}$ on every compact set of $X=\widehat{\mathcal{X}} \backslash E$, where $E$ is the exceptional divisor of $\widehat{\mathcal{X}} \rightarrow \mathcal{X}$.
\end{itemize}

Remark 12. The above proposition also holds if $\Omega$ is only assumed to be a family of (1, 1)-classes (instead of Kähler). As a corollary, under the assumptions of admissibility, $\Omega_{t}$ must be a Kähler class for $t \in(0,+\infty)$ sufficiently small.

The rest of the section will be devoted to prove the proposition as well as giving more accurate results about the behavior of $\omega_{t}$ as $t \rightarrow 0$.
3.1. Summary of the setup. We use the notations introduced at §2. As in §2.1, we shall assume to keep the notations simple that there is exactly one singularity in $\mathcal{X}$ with a neighborhood $U$ identified to $\Delta^{2} / \Gamma$. The minimal resolution of the singularity will be denoted $\widehat{U} \rightarrow U$ and $\widehat{\mathcal{X}} \rightarrow \mathcal{X}$. The case when several singularities occur is a straightforward generalization of the constructions explained below.

The smooth manifold or orbifold deduced from $\widehat{\mathcal{X}}$ and $\mathcal{X}$ will be denoted $\widehat{X}$ and $\bar{X}$, and $X$ will denote the complement of the singularity in $\bar{X}$, or equivalently, the complement of the exceptional divisor in $\widehat{X}$.

Using a smooth trivialization $\phi: \Delta_{d} \times \widehat{X} \rightarrow \widehat{\mathcal{M}}$ of the simultaneous resolution $\widehat{\mathcal{X}} \hookrightarrow \widehat{\mathcal{M}} \rightarrow \Delta_{d}$, we have a family of complex structures $J_{t}$ defined on $\widehat{X}$ deduced from $\widehat{\mathcal{M}}_{t}$ and $\phi$. The degenerating family of Kähler classes $\Omega_{t}$ on $\left(\widehat{X}, J_{t}\right)$ also provides a cohomology class $\left.\Omega_{t}\right|_{\widehat{U}} \in H^{2}(\widehat{U}, \mathbb{R}) \simeq H^{2}\left(\widehat{\mathbb{C}^{2} / \Gamma}, \mathbb{R}\right)$. As explained in §2.3, this is the Kähler class of a Kähler Ricci-flat metric $\mathrm{g}_{\zeta(t)}$ compatible with the complex structure $\mathrm{I}_{\zeta(t)}$ on $\widehat{\mathbb{C}^{2} / \Gamma}$ provided by Kronheimer's construction.

If the variation of the deformation is non degenerate, there is a scaling parameter $\varepsilon=t^{p / 2}$ defined for some $p \geq 1$, and homotheties $H_{\varepsilon^{-1}}$ by a factor $t^{-p / 2}=\varepsilon^{-1}$ such that we have the following properties: $H_{\varepsilon^{-1}}$ induces a map $\widehat{U} \rightarrow \widetilde{\Delta_{\varepsilon^{-1}}^{2} / \Gamma}$ such that the image of the Kähler structure $\left(\mathrm{I}_{\zeta(t)}, \mathrm{g}_{\zeta(t)}\right)$ is $\left(\mathrm{I}_{\varepsilon^{-2} \zeta(t)}, \varepsilon^{2} \mathrm{~g}_{\varepsilon^{-2} \zeta(t)}\right)$. Up to rescaling the metric by a factor $\varepsilon^{-2}$, the family of Kähler structure converges to to the tangent graviton graviton $Y_{\dot{\zeta}}$ which is smooth (not in Kronheimer's wall). Thus by 2.2 (ii), we have uniform estimates in $t$ as $R \rightarrow+\infty$ of the form
$$\mathrm{g}_{\varepsilon^{-2} \zeta(t)}=g^{\text {euc }}+\xi_{t} \quad \text { with } \xi_{t}=\mathcal{O}\left(R^{-4}\right)$$
where $g^{\text {euc }}$ is the Euclidean metric on $\mathbb{C}^{2} / \Gamma$, and $R$ is the Euclidean distance to the origin. The function $R$ is related to $r$ by the scaling factor $r=\varepsilon R$. Similar estimates hold for the complex structures
$$\mathrm{I}_{\varepsilon^{-2} \zeta(t)}=\text { euc }+\mathcal{O}\left(R^{-4}\right),$$
where euc is the canonical complex structure of $\mathbb{C}^{2} / \Gamma$.
3.2. Background Hermitian metrics. Let $\bar{g}$ be the orbifold Kähler metric on $\left(\bar{X}, J_{0}\right)$ with Kähler form $\bar{\omega}$. Recall that the isomorphism between $U$ and $\Delta^{2} / \Gamma$ is chosen so that the Kähler form can be written as (2.1). We modify $\bar{g}$ so that it is flat near the the singularity. For this purpose, we need to choose a gluing scale of the form
$$b=\varepsilon^{\beta}=t^{p \beta / 2}$$
where $\beta$ is a constant very close to $\frac{1}{2}$ and such that $1>\beta>\frac{1}{2}$. The precise value of this constant will be decided later on (cf. (3.4)).

We also need to define suitable cut-off functions. We fix a standard bump function $\chi: \mathbb{R} \rightarrow \mathbb{R}$, that is a smooth non decreasing function such that $\chi(x)=0$ for $x \leq 0$ and $\chi(x)=1$ for $x \geq 1$. Then we choose a pair of real parameters $\left(x_{1}, x_{2}\right)$ such that $0<x_{1}<x_{2}$ and define
$$\chi_{\left(x_{1}, x_{2}\right)}(x)=\chi\left(\frac{x-x_{1}}{x_{2}-x_{1}}\right)$$

Let $r$ be the function on $U$ corresponding to the Euclidean distance to the origin via the isomorphism $U \simeq \Delta^{2} / \Gamma$. Then we define
$$\begin{aligned}
& \omega_{B, t}=\bar{\omega} \quad \text { away from the domain } r \leq 4 b \text { of } U \text { and } \\
& \omega_{B, t}=d d_{J_{0}}^{c}\left(r^{2}+\chi_{(2 b, 4 b)}(r) \eta\right) \quad \text { on the domain } r \leq 4 b \text { of } U
\end{aligned}$$
so that $\omega_{B, t}$ is the Kähler form of a Kähler orbifold metric on $\left(\bar{X}, J_{0}\right)$ for $t$ small enough.

Similarly, we modify the model metric $\mathrm{g}_{\varepsilon^{-2} \eta(t)}$ on $\widehat{\mathbb{C}^{2} / \Gamma}$ as follows:
$$\begin{aligned}
& g_{A, t}=\mathrm{g}_{\varepsilon^{-2} \zeta(t)} \text { on the domain } R \leq b / \varepsilon \\
& g_{A, t}=g^{\text {euc }} \text { on the domain } 2 b / \varepsilon \leq R, \\
& g_{A, t}=g^{\text {euc }}+\left(1-\chi_{(b / \varepsilon, 2 b / \varepsilon)}(R)\right) \xi_{t} \quad \text { on the annulus } b / \varepsilon \leq R \leq 2 b / \varepsilon .
\end{aligned}$$
Hence $g_{A, t}$ defines a Riemannian metric on $\widehat{\mathbb{C}^{2} / \Gamma}$ for $t$ small enough.
The homothety $H_{\varepsilon^{-1}}$ identifies the annuli $b \leq r \leq 4 b$ and $b / \varepsilon \leq R \leq 4 b / \varepsilon$. By construction $g_{B, t}$ is Euclidean at $r=2 b$ and so is $g_{A, t}$ near $R=2 b / \varepsilon$. Identifying
the annuli via $H_{\varepsilon^{-1}}$, we define a Riemannian metric on $\widehat{X}$ by
$$\begin{aligned}
\tilde{h}_{t} & =\varepsilon^{2} H_{\varepsilon^{-1}}^{*} g_{A, t} \quad \text { on the domain } r \leq 2 b \text { of } \widehat{U} \\
& =g_{B, t} \quad \text { outside the domain } r \leq 2 b \text { of } \widehat{U}
\end{aligned}$$

By definition, the metric $\tilde{h}_{t}$ is $J_{t}$-Hermitian on the domain $r \leq b$ of $\widehat{U}$ and $J_{0}$-Hermitian on the complement of $r \leq 2 b$. We construct a globally $J_{t}$-Hermitian metric on $\widehat{X}$ by introducing its projection
$$h_{t}(u, v)=\frac{1}{2}\left(\tilde{h}_{t}(u, v)+\tilde{h}_{t}\left(J_{t} u, J_{t} v\right)\right) .$$
Similarly, one can construct $\mathrm{I}_{\varepsilon}-2 \zeta(t)$-Hermitian metrics $h_{A, t}$ on $\widehat{\mathbb{C}^{2} / \Gamma}$ deduced from $g_{A, t}$.
3.3. Hölder spaces. Elliptic operators, Laplacians for instance, may not be Fredholm on a singular or noncompact manifold. At this point, we ought to introduce suitable weighted Hölder spaces to deal with this issue.

Hölder spaces for ALE spaces. We consider a radius function $\rho_{A}$ on $\widehat{\mathbb{C}^{2} / \Gamma}$. That is a smooth function such that $\rho_{A}>0$ with the property that $\rho_{A}=R$, say on the domain $R \geq 2$. For $\delta \in \mathbb{R}$, we define the weighted Hölder $C_{\delta}^{k, \alpha}$-norm given by
$$\|f\|_{C_{\delta}^{k, \alpha}\left(\widehat{\mathbb{C}^{2} / \Gamma}, t\right)}=\sum_{j=0}^{k} \sup \left|\rho_{A}^{j-\delta} \nabla^{j} f\right|+\left\|\rho_{A}^{j-\delta-\alpha} \nabla^{k} f\right\|_{\alpha}$$
where ( $i_{0}>0$ being fixed and chosen smaller than the injectivity radius)
$$\|f\|_{\alpha}=\sup _{d(x, y) \leq i_{0}} \frac{|f(x)-f(y)|}{d(x, y)^{\alpha}} .$$
Here, $f$ can be any tensor, and the pointwise norms are taken with respect to the metric $\mathrm{g}_{\varepsilon^{-} 2 \zeta(t)}$ (or alternatively $g_{A, t}$ ).

Remark 13. All the norms on $\widehat{\mathbb{C}^{2} / \Gamma}$ obtained in such a way are commensurate uniformly in $t$. Thus, any of these norms could be used in the estimating process.

Hölder spaces on orbifold. Similarly, we define a radius function $\rho_{B}$ on $\bar{X}$, that is a smooth function such that $\rho_{B}>0$ and $\rho_{B}=r$ on $U$. We define the $C_{\delta}^{k, \alpha}(\bar{X})$ with the same formula as above, using instead the metric $\bar{g}$ (or alternatively $g_{B, t}$ ).

Hölder spaces on the gluing. Finally a third weighted norm can be defined on $\widehat{X}$ itself. For this purpose, we define a weight function $\rho$ (depending on the parameters $t$ ) on $\widehat{X}$ as follows: put $\rho=\rho_{B}$ on the complement of $\widehat{U}, \rho=r$ on the domain $b \leq r \leq 1$ of $\widehat{U}$ and $\rho=\varepsilon H_{\varepsilon^{-1}}^{*} \rho_{A}$ on the rest. Using the same formula as above with metrics $h_{t}$ (or alternatively $\tilde{h}_{t}$ ), we define a norm $\|f\|_{C_{\delta}^{k, \alpha}(\widehat{X}, t)}$ on $\widehat{X}$.

Given a $m$-form $f$ on $\widehat{X}$, we can interpret a $C_{\delta}^{k, \alpha}(t)$-estimate on $f$ as an estimate on each piece of the manifold. We decompose $f=f_{A}+f_{B}$ where $f_{A}=$ ( 1 - $\left.\chi_{(b, 2 b)}(\rho)\right) f$ and $f_{B}=\chi_{(b, 2 b)}(\rho) f$. Then $f_{A}$ is supported on the domain $\rho \leq 2 b$ and $f_{A}=f$ on the domain $\rho \leq b$. Similarly $f_{B}$ is supported in the domain $\rho \geq b$ and
$f=f_{B}$ on the domain $\rho \geq 2 b$. Then $\|f\|_{C_{\delta}^{k, \alpha}(\widehat{X}, t)}$ is uniformly commensurate with the norms
$$\left\|f_{B}\right\|_{C_{\delta}^{k, \alpha}(\bar{X}, t)}+\varepsilon^{-m-\delta}\left\|\left(H_{\varepsilon^{-1}}\right)_{*} f_{A}\right\|_{C_{\delta}^{k, \alpha}}\left(\widehat{\mathbb{C}^{2} / \Gamma, t}\right)$$
where $m$ is the degree of the form $f$ and $H_{\varepsilon^{-1}}$ is used to identify the domain $\rho \leq 2 b$ with the domain $\rho_{A} \leq 2 b / \varepsilon$.

Remark 14. The asymptotics of the metrics $\bar{g}, \mathrm{~g}_{\varepsilon^{-2} \zeta(t)}$ and complex structures $\mathrm{I}_{\varepsilon^{-2} \zeta(t)}$, together with the naturality of the constructions of the metrics $g_{A}, g_{B}, h_{A}$, $\tilde{h}_{t}, h_{t}$ and the fact that the functions $\chi_{(c, 2 c)}$ are uniformly bounded in $C_{0}^{k}$-norm imply that the Hölder norms defined using any of these metrics lead to uniformly commensurate norms. Therefore, we could use any of these metrics for estimating the $C_{\delta}^{k, \alpha}$-norms.
3.4. Background Laplacian. The Cauchy-Riemann operator on $\left(\widehat{X}, J_{t}\right)$ is denoted $\bar{\partial}_{J_{t}}$ or $\bar{\partial}_{t}$. Its adjoint deduced from the Hermitian metric $h_{t}$ is denoted $\bar{\partial}_{t}^{*}$. Then the Dolbeault Laplacian is given by
$$\square_{t}=\bar{\partial}_{t}^{*} \bar{\partial}_{t}+\bar{\partial}_{t} \bar{\partial}_{t}^{*}$$
for $(p, q)$-forms on $\left(\widehat{X}, J_{t}\right)$.
Error terms. It should be pointed out that the Dolbeault Laplacian $\square_{t}$ need not agree with the Riemannian Laplacian $\Delta_{t}$ of $h_{t}$. Indeed, the metric $h_{t}$ is not necessarily Kähler. Thus, $h_{t}$ is Hermitian, by construction, but its Kähler form $\varpi_{t}=h_{t}\left(J_{t} \cdot, \cdot\right)$ is not a priori closed. In this section, we investigate how close $h_{t}$ is to be Kähler. In particular, we prove the following lemma:

Lemma 15. For every $k \geq 0$, there exist a constant $C_{k}>0$ such that for every $\delta<0$ sufficiently close to $-2, t>0$ and $\beta=\frac{2}{2-\delta}$, we have
$$\left\|d \varpi_{t}\right\|_{C_{\delta-1}^{k, \alpha}(t)} \leq C_{k} \varepsilon^{2}$$
Similarly, we have an estimate
$$\left\|\nabla^{L C} J_{t}\right\|_{C_{\delta-1}^{k, \alpha}(t)} \leq C_{k} \varepsilon^{2}$$
Proof. On the compact domain $\widehat{X} \backslash \widehat{U}$, the family of complex structure $J_{t}$ converges smoothly to $J_{0}$, and $\left|J_{t}-J_{0}\right|=\mathcal{O}\left(t^{\mathbf{d}}\right)$ where d is the order of the covering (2.3). By assumption, the variation is non degenerate $(\mathbf{d} \geq p)$, hence $\left|J_{t}-J_{0}\right|=\mathcal{O}\left(\varepsilon^{2}\right)$ on the compact domain. It follows that $\varpi_{t}$ converges smoothly to $\bar{\omega}$, the Kähler form of the orbifold metric $\bar{g}$. Since $d \bar{\omega}=0$, the estimate $\left\|d \varpi_{t}\right\|_{C^{1, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right)$ on this domain follows.

On the domain $r \leq b$, the metric $\tilde{h}_{t}$ is $J_{t}$-Hermitian. In fact it agrees with the model metric $\mathrm{g}_{\varepsilon^{-2}(\zeta(t)}$ up to a scaling factor $\varepsilon^{2}$. Therefore $\tilde{h}_{t}=h_{t}$ and the $J_{t}$-Hermitian metric is Kähler on this domain. In particular $d \varpi_{t}=0$.

On the domain $2 b \leq \rho \leq 1$, we have $\tilde{h}_{t}=g_{B, t}$ and $J_{t}=\mathrm{I}_{\zeta(t)}=H_{t}^{*} \mathrm{I}_{\varepsilon^{-2} \zeta(t)}$. However $\mathrm{I}_{\varepsilon^{-2} \zeta(t)}=$ euc $+\mathcal{O}\left(R^{-4}\right)$. It follows that $J_{t}=J_{0}+\mathcal{O}\left(\varepsilon^{4} r^{-4}\right)$. Since $g_{B, t}$ is Kähler w.r.t. the complex structure $J_{0}$, we have $h_{t}=g_{B, t}+\mathcal{O}\left(\varepsilon^{4} r^{-4}\right)$ and $\varpi_{t}=\omega_{B, t}+\mathcal{O}\left(\varepsilon^{4} r^{-4}\right)$. Thus, $d \varpi_{t}=\mathcal{O}\left(\varepsilon^{4} r^{-5}\right)$ hence $r^{1-\delta} d \varpi_{t}=\mathcal{O}\left(\varepsilon^{4-\beta(5+\delta)}\right)$ on the domain $2 b \leq r \leq 1$. That is to say $\left\|d \varpi_{t}\right\|_{C_{\delta-1}^{k, \alpha}}=\mathcal{O}\left(\varepsilon^{4-\beta(5+\delta)}\right)$ on the annulus
$2 b \leq r \leq 1$. We see that if delta is sufficiently close to -2 then the error term is a $\mathcal{O}\left(\varepsilon^{2}\right)$.

On the domain $b \leq \rho \leq 2 b$, we can rescale via the homothety $H_{t}$ and look at the construction on the annulus $b / \varepsilon \leq R \leq 2 b / \varepsilon$ of $\widehat{\mathbb{C}^{2} / \Gamma}$. Up to a scaling factor $\varepsilon^{2}$, the metric $\tilde{h}_{t}$ corresponds to $g_{A, t}$. On the other had, we have $g_{A, t}=$ $\mathrm{g}_{\varepsilon^{-2} \zeta(t)}+\mathcal{O}\left(R^{-4}\right)$. It follows that the $\mathrm{I}_{\varepsilon^{-2} \zeta(t)}$-Hermitian metric $h_{A, t}$ deduced from $g_{A, t}$ satisfies the estimate $h_{A, t}=\mathrm{g}_{\varepsilon^{-2} \zeta(t)}+\mathcal{O}\left(R^{-4}\right)$ and we have a similar estimate for the corresponding Kähler forms $\varpi_{A, t}$ and $\omega_{\varepsilon^{-2} \zeta(t)}^{\text {mod }}$ defined using $\mathrm{I}_{\varepsilon^{-2} \zeta(t)}$. Hence $d \varpi_{A, t}=\mathcal{O}\left(R^{-5}\right)$. Using the homothety again, we obtain the estimate $d \varpi_{t}=$ $\mathcal{O}\left(\varepsilon^{4} r^{-5}\right)$ (there is an factor $\varepsilon$ coming from the fact that we are taking the norm of a 3-form for the rescaled metric) on the annulus $b \leq r \leq 2 b$. As in the previous case, we deduce an estimate $\left\|d \varpi_{t}\right\|_{C_{\delta-1}^{k, \alpha}}=\mathcal{O}\left(\varepsilon^{4-\beta(5+\delta)}\right)$ on the annulus $b \leq r \leq 2 b$ as well. \(\square\)

From now on, we shall fix the gluing scale $b=\varepsilon^{\beta}$, with the convention
$$\beta=\frac{2}{2-\delta}$$
as in the above lemma. The point is that for $\delta \in(-2,0)$, we have $\beta \in\left(\frac{1}{2}, 1\right)$, $\lim _{\delta \rightarrow-2} \beta=\frac{1}{2}$.

Then we deduce that the Kähler form $\varpi_{t}$ is almost harmonic in the sense of the following corollary:

Corollary 16. For $\delta<0$ sufficiently close to -2 there exists a constant $C>0$ such that for all $t>0$
$$\left\|\square_{t} \varpi_{t}\right\|_{C_{\delta-2}^{0, \alpha}(t)} \leq C \varepsilon^{2}$$
and
$$\left\|\Delta_{t} \varpi_{t}\right\|_{C_{\delta-2}^{0, \alpha}(t)} \leq C \varepsilon^{2}$$
Proof. Using Lemma 15, together with the fact that $* \varpi_{t}=\varpi_{t}$ we deduce an estimate
$$\left\|d^{*} \varpi_{t}\right\|_{C_{\delta-1}^{1, \alpha}(t)} \leq C_{1} \varepsilon^{2}$$
Therefore we have an estimate on $d d^{*} \varpi_{t}$ and $d^{*} d \varpi_{t}$ in $C_{\delta-2}^{0, \alpha}(t)$-norm and the result follows for $\Delta_{t} \varpi_{t}$.

The same proof works with the Dolbeault Laplacian. We merely use the fact that the norm of $* \bar{\partial}_{t} \varpi_{t}$ is controlled by the norm of $d \varpi_{t}$. The next step to deduce a control on $\bar{\partial}_{t} * \bar{\partial}_{t} \varpi_{t}$. The pointwise norm of this tensor is controlled by the pointwise norm of $\nabla_{t}^{\text {Chern }} * \bar{\partial}_{t} \varpi_{t}$. The metric being Hermitian, we only have $\nabla_{t}^{\text {Chern }}=\nabla_{t}^{L C}+T$ where $T$ is a tensor such that $T=\mathcal{O}\left(\nabla_{t}^{L C} J_{t}\right)$. Using again 15, we conclude that
$$\left|\nabla_{t}^{\text {Chern }} * \bar{\partial}_{t} \varpi_{t}\right| \rho^{\delta-2} \leq\left|\nabla_{t}^{L C} * \bar{\partial}_{t} \varpi_{t}\right| \rho^{\delta-2}+(|T| \rho)\left(\left|* \bar{\partial}_{t} \varpi_{t}\right| \rho^{1-\delta}\right) .$$
The estimate follows and we have the control on $\square_{t} \varpi_{t}$ with the $C_{\delta-2}^{0, \alpha}$-norm. \(\square\)

The Laplacian and gravitons. The space $\widehat{\mathbb{C}^{2} / \Gamma}$ is endowed with a complex structure $\mathrm{I}_{\varepsilon^{-2} \zeta(t)}$ and Kähler metric $\mathrm{g}_{\varepsilon^{-2} \zeta(t)}$. The parameter $t=0$ corresponds to the tangent graviton. Each of these spaces has a corresponding Laplacian $\square_{t}^{A}=\frac{1}{2} \Delta_{t}^{A}$. If $\delta$ is not an indicial root, the operator
$$\square_{t}^{A}: C_{\delta}^{2, \alpha} \rightarrow C_{\delta-2}^{2, \alpha}$$
defined on $(p, q)$-forms with respect to $\mathrm{g}_{\varepsilon^{-2} \zeta(t)}$ is Fredholm.
Indicial roots are well understood for such operators
Lemma 17. Every $\delta \in(-2,0)$ is not an indicial root. In the case of 1-forms every $\delta \in(-3,1)$ is not an indicial root.

Proof. For the first part, see [8]. For the second part, one has to check that 0 is not an indicial root. This boils down to check that there are no $\Gamma$-invariant parallel 1 -forms on $\mathbb{C}^{2}$. By duality, it follows that -2 is not an indicial root either. \(\square\)

Harmonic forms on ALE spaces. The space of Harmonic forms of type $(p, q)$ on the ALE space, denoted $\mathcal{H}_{A, t}^{p, q}$, is defined as the kernel of $\square_{t}^{A} C_{\delta}^{2, \alpha} \rightarrow C_{\delta-2}^{2, \alpha}$, for $\delta \in(-2,0)$. Since there are no indicial root in the interval, it follows that the definition for $\mathcal{H}_{A, t}^{p, q}$ in independent of the choice of $\delta \in(-2,0)$. For 1-forms we could also choose $\delta \in(-3,1)$ as there are no indicial roots in this interval by Lemma 17.

If we choose $\delta$ sufficiently close to -2, we see that harmonic forms are in $L^{2}$. In fact, the decay is even better according to the following lemma

Lemma 18. Any harmonic form $\gamma \in \mathcal{H}_{A, t}^{p, q}$ satisfies $\gamma=\mathcal{O}\left(R^{-3}\right)$.
Proof. It suffices to understand the case of a harmonic function $\gamma \in C_{\delta}^{2, \alpha}$. The standard theory for Laplacian on ALE spaces shows that $\gamma=c R^{-2}+\mathcal{O}\left(R^{-3}\right)$ since there are no indicial roots in (-3, -2). The coefficient $c$ is a constant multiple of $\int \square_{t}^{A}$ vol $=0$ (cf. [5, Theorem 8.3.6]) and the lemma follows. \(\square\)

We recall some standard results for Hodge theory on ALE spaces (cf. [5] for instance): The canonical map $\mathcal{H}_{A, t}^{p, q} \rightarrow H^{p+q}\left(\widehat{\mathbb{C}^{2} / \Gamma}, \mathbb{C}\right)$ is injective with image denoted $H_{t}^{p, q}$. In addition
$$H^{k}\left(\widehat{\mathbb{C}^{2} / \Gamma}, \mathbb{C}\right)=\bigoplus_{j=0}^{k} H_{t}^{j, j-k}$$
for all $0<k<4$. In particular we see that $\mathcal{H}_{A, t}^{1,0}=\mathcal{H}_{A, t}^{0,1}=0$.
We also have the following result
Lemma 19.
$$\mathcal{H}_{A, t}^{2,0}=\mathcal{H}_{A, t}^{0,2}=0$$
and
$$\mathcal{H}_{A, t}^{1,1} \simeq H^{2}\left(\widehat{\mathbb{C}^{2} / \Gamma, \mathbb{C}}\right)$$
for all $t$ sufficiently small.

Proof. If $t$ is sufficiently small, $\zeta^{\prime}=\varepsilon^{-2} \zeta(t)$ does not belong to the wall $D$ since the variation is assumed to be non degenerate. Similarly, let $\zeta^{\prime \prime}=\left(\left(\zeta_{r}\right)^{\prime \prime},\left(\zeta_{c}\right)^{\prime \prime}\right) \notin D$ be a parameter such that $\mathcal{Y}_{\left(\zeta_{c}\right) \prime}$ is isomorphic to $\widehat{\mathbb{C}^{2} / \Gamma}$ with its canonical complex structure. We have $H^{2,0}\left(\widehat{\mathbb{C}^{2} / \Gamma}\right)=H^{0,2}\left(\widehat{\mathbb{C}^{2} / \Gamma}\right)=0$ (cf. [5, Theorem 8.4.2]). The semi-continuity of the dimension of the kernel for Fredholm operator forces this property to hold along the path from $\zeta^{\prime \prime}$ to $\zeta^{\prime}$ and we deduce the lemma. \(\square\)

Laplacian and orbifold. One can consider the Kähler orbifold $\left(\bar{X}, J_{0}, \bar{g}\right)$ together with its Laplacian. Alternatively, we can look at the manifold $X$, the smooth locus of $\bar{X}$ and the Laplacian defined between weighted Hölder spaces
$$\square^{B}: C_{\delta}^{2, \alpha} \rightarrow C_{\delta-2}^{2, \alpha}$$
acting on $(p, q)$-forms with respect to $J_{0}$.
Like on the ALE space, this operator is Fredholm for $\delta \in(-2,0)$, and for $\delta \in(-3,1)$ in the case of 1-forms. Moreover, its kernel $\mathcal{H}_{B}^{p, q}$ corresponds to smooth harmonic forms on $\bar{X}$.
3.5. Approximate kernel. One can construct an approximate kernel of the operator $\square_{t}$ on $\left(\widehat{X}, J_{t}, h_{t}\right)$ as follows. The spaces $\mathcal{H}_{A, t}^{1,1}$ are the fibers of a smooth (trivial) vector bundle over the base $t \in[0, d)$. Given $\gamma_{A, t} \in \mathcal{H}_{A, t}^{1,1}$ and $\gamma_{B} \in \mathcal{H}_{B}^{p, q}$, we construct a form $\gamma_{t}^{\prime}$ on $\widehat{X}$ by requiring that $\gamma_{t}^{\prime}=H_{\varepsilon^{-1}}^{*} \gamma_{A, t}$ on the domain $\rho \leq b$, $\gamma_{t}^{\prime}=\gamma_{B}$ on the domain $\rho \geq 4 b$ and
$$\gamma_{t}^{\prime}=\left(1-\chi_{(b, 2 b)}(r)\right) H_{\varepsilon^{-1}}^{*} \gamma_{A, t}+\chi_{(2 b, 4 b)}(r) \gamma_{B}$$
Then we call $\gamma_{t}$ the projection of $\gamma_{t}^{\prime}$ onto forms of type $(1,1)$ for the complex structure $J_{t}$. Thus we have constructed a linear map
$$\Phi_{t}: \mathcal{H}_{A, t}^{1,1} \oplus \mathcal{H}_{B}^{1,1} \rightarrow \Omega_{J_{t}}^{1,1}(\widehat{X})$$
For every $t>0$ small enough, the linear map (3.5) is injective and its image will be denoted $\mathcal{K}_{t}^{1,1}$.

Alternatively, using the isomorphisms $H^{2}\left(\widehat{\mathbb{C}^{2} / \Gamma}, \mathbb{C}\right) \simeq \mathcal{H}_{A, t}^{1,1}$ and $H^{1,1}(\mathcal{X}) \simeq$ $\mathcal{H}_{B}^{1,1}$, the map $\Phi_{t}$ can be though of as an isomorphism
$$\Psi_{t}: H^{2}\left(\widehat{\mathbb{C}^{2} / \Gamma}, \mathbb{C}\right) \oplus H^{1,1}(\mathcal{X}) \rightarrow \mathcal{K}_{t}^{1,1} .$$

In the case of 1 -forms, we have $\mathcal{H}_{A, t}^{1,0}=0$ and $\mathcal{H}_{A, t}^{0,1}=0$. A similar construction gives linear maps
$$\Phi_{t}: \mathcal{H}_{B}^{0,1} \rightarrow \Omega_{J_{t}}^{0,1}(\widehat{X}), \quad \Phi_{t}: \mathcal{H}_{B}^{1,0} \rightarrow \Omega_{J_{t}}^{1,0}(\widehat{X})$$
These maps are injective for $t$ small enough and their images are denoted $\mathcal{K}_{t}^{0,1}$ and $\mathcal{K}_{t}^{1,0}$. Then, we define isomorphisms $\Psi_{t}: H^{0,1}(\mathcal{X}) \rightarrow \mathcal{K}_{t}^{0,1}, \Psi_{t}: H^{1,0}(\mathcal{X}) \rightarrow \mathcal{K}_{t}^{1,0}$.

Let $\|\cdot\|_{A}$ be an arbitrary norm on the cohomology $H^{\bullet}\left(\widehat{\mathbb{C}^{2} / \Gamma}, \mathbb{C}\right)$ and $\|\cdot\|_{B}$ an arbitrary norm on the cohomology $H^{\bullet}(\bar{X}, \mathbb{C})$. We introduce a family of norms $\|\cdot\|_{\delta, t}$ on $H^{2}\left(\widehat{\mathbb{C}^{2} / \Gamma}, \mathbb{C}\right) \oplus H^{2}(\bar{X}, \mathbb{C}) \simeq H^{2}(\widehat{X}, \mathbb{C})$ given by
$$\left\|\Omega_{A} \oplus \Omega_{B}\right\|_{\delta, t}=\varepsilon^{-2-\delta}\left\|\Omega_{A}\right\|+\left\|\Omega_{B}\right\|$$

Lemma 20. Given $k \geq 0$, there are constants $c_{1}, c_{2}>0$ such that for every $\delta \in(-2,0)$ sufficiently close to -2 and every $t>0$ sufficiently small, we have for all $\Omega \in H^{2}\left(\widehat{\mathbb{C}^{2} / \Gamma}, \mathbb{C}\right) \oplus H^{1,1}(\mathcal{X})$
$$c_{1}\|\Omega\|_{\delta, t} \leq\left\|\Psi_{t}(\Omega)\right\|_{C_{\delta}^{k, \alpha}(\widehat{X}, t)} \leq c_{2}\|\Omega\|_{\delta, t} .$$
For cohomology classes $\Xi \in H^{0,1}(\mathcal{X})$, we have a similar result with the estimate
$$c_{1}\|\Xi\|_{B} \leq\left\|\Psi_{t}(\Xi)\right\|_{C_{\delta+1}^{k, \alpha}(\widehat{X}, t)} \leq c_{2}\|\Xi\|_{B}$$
Proof. The injection $\mathcal{H}_{B}^{1,1} \rightarrow \mathcal{K}_{t}^{1,1}$ induced by $\Phi_{t}$ allows to pull-back the $C_{\delta}^{k, \alpha}(\widehat{X}, t)$ norm. It is readily checked that this norm is uniformly commensurate with the $C_{\delta}^{k, \alpha}(\bar{X})$-norm.

Similarly, the injection $\mathcal{H}_{A, t}^{1,1} \rightarrow \mathcal{K}_{t}^{1,1}$ induced by $\Phi_{t}$ allows to pull-back the $C_{\delta}^{k, \alpha}\left(\widehat{\mathbb{C}^{2} / \Gamma}, t\right)$ norm. This norm is uniformly commensurate with the $C_{\delta}^{k, \alpha}(\bar{X})$ -norm up to a factor $\varepsilon^{-\delta-2}$ by (3.3).

The proof of the second part of the statement goes along the same lines, except that we do not have to deal with harmonic forms on the ALE space. \(\square\)

Uniform elliptic estimates. A key step in order to construct Kähler forms is Hodge theory. More precisely, we should control the first eigenvalues of the Dolbeault Laplacian between weighted Hölder spaces:

Proposition 21. There exists a constant $c>0$ such that for all $t>0$ sufficiently small and every $(1,1)$-form $\gamma$ on $\left(\widehat{X}, J_{t}\right)$, we have
$$c\|\gamma\|_{C_{\delta}^{2, \alpha}(t)} \leq\|\gamma\|_{C_{\delta}^{0, \alpha}(t)}+\left\|\square_{t} \gamma\right\|_{C_{\delta-2}^{0, \alpha}(t)} .$$

If in addition $\gamma$ is $L^{2}$-orthogonal to the space $\mathcal{K}_{t}^{1,1}$ and $\delta \in(-2,0)$ sufficiently close to -2, we have
$$c\|\gamma\|_{C_{\delta}^{2, \alpha}(t)} \leq\left\|\square_{t} \gamma\right\|_{C_{\delta-2}^{0, \alpha}(t)} .$$
Similarly, if $\gamma$ is a (0, 1)-form orthogonal to $\mathcal{K}_{t}^{0,1}$, we have an estimate
$$c\|\gamma\|_{C_{\delta+1}^{2, \alpha}(t)} \leq\left\|\square_{t} \gamma\right\|_{C_{\delta-1}^{0, \alpha}(t)} .$$
Proof. The first part of the proposition is standard. For the second part, let us argue by contradiction. If the proposition is not true, there are weights $\delta \in(-2,0)$ arbitrarily close to -2 with and families of parameter $t_{j} \rightarrow 0$ and (1, 1)-forms $\gamma_{j}$ on $\left(\widehat{X}, J_{t}\right)$ such that
$$\left\|\gamma_{j}\right\|_{C_{\delta}^{0, \alpha}\left(t_{j}\right)}=1, \text { and }\left\|\square_{t_{j}} \gamma_{j}\right\|_{C_{\delta-2}^{0, \alpha}\left(t_{j}\right)} \rightarrow 0 .$$
The first part of the proposition provides a uniform $C_{\delta}^{2, \alpha}$ estimate on $\gamma_{j}$.
Then, up to extraction of a subsequence, we may assume that $\gamma_{j}$ converges in the $C^{0, \alpha}$ sense on every compact set of $X$ toward a form $\gamma$ on $X$ which is $\bar{g}$ harmonic and in $C_{\delta}^{2, \alpha}\left(\bar{X}, t_{j}\right)$. This implies that $\gamma$ extends as a smooth orbifold form on the orbifold $\bar{X}$. Since each $\gamma_{j}$ is orthogonal to $\mathcal{K}_{t}$ and $\delta>-3$, it follows that $\gamma$ is orthogonal to $\mathcal{H}_{B}^{1,1}$. This forces $\gamma=0$.

Similarly, we can transport $\gamma_{j}$ on the domain $R \leq 4 b_{j} / \varepsilon_{j}$ of $\widehat{\mathbb{C}^{2} / \Gamma}$ using the homothety $H_{j}=H_{\varepsilon_{j}^{-1}}$. Put $\mu_{j}=\varepsilon^{-2-\delta} H_{j}^{*} \gamma_{j}$. By definition of the norm we obtain a uniform $C^{2, \alpha}$ bound on $\mu_{j}$. Up to extraction, we may assume that $\mu_{j}$ converge on
every compact set of $\widehat{\mathbb{C}^{2} / \Gamma}$ to a harmonic form $\mu \in C_{\delta}^{2, \alpha}$ on the tangent graviton. Again, the fact that harmonic forms must have a strong decay forces $\mu \in C_{-3}^{2, \alpha}$ by Lemma 18. Then, the fact that $\gamma_{j}$ is orthogonal to $\mathcal{K}^{1,1} t$ implies that $\mu$ is orthogonal to $\mathcal{K}_{A, t}^{1,1}$. We conclude $\mu=0$.

Let $m_{j}$ be a point where the function $\left|\rho_{j}^{-\delta} \gamma_{j}\right|$ is maximal equal to 1 (cf. assumption (3.6)). Up to extraction of a converging subsequence, we have either
\begin{itemize}
\item[(1)] $\rho_{j}\left(m_{j}\right) \leq 2 b_{j}$
\item[(2)] $\rho_{j}\left(m_{j}\right) \geq 2 b_{j}$
\end{itemize}
for all $j$.
Case (ii): If $\rho_{j}\left(m_{j}\right)$ is bounded away from zero we clearly have a contradiction. Indeed, after further extraction, we may assume that $m_{j}$ converges to a point in $X$. But we know that $\gamma_{j}$ converges to 0 on every compact set of $X$ hence hence $\left|\rho_{j}^{-\delta} \gamma_{j}\right|\left(m_{j}\right) \rightarrow 0$ which is impossible.

So we may assume up to extraction that $\lim \rho_{j}\left(m_{j}\right)=0$. Using homotheties and rescaling for $\gamma_{j}$ again, we can extract a converging subsequence on every compact set of the cone $\left.\mathbb{C}^{2} \backslash 0\right) / \Gamma$ such that the limit is nonvanishing, harmonic and in $C_{\delta}^{2, \alpha}$ on the cone. This is not possible for $\delta$ is not an indicial root of the Laplacian.

Case (i): If $\rho_{j}\left(m_{j}\right) / \varepsilon_{j}$ is bounded, we have a contradiction. The proof is the same as in the first case, using the rescaled forms $\mu_{j}$ instead.

If it is not bounded, we may assume that it goes to infinity after extraction. Then we use rescaling to extract a harmonic limit on the cone, exactly as in the first case. \(\square\)

From approximate kernel to harmonic forms. The spaces $\mathcal{K}_{t}$ consist of forms which are approximately harmonic in the sense of the following lemma.

Lemma 22. Fix $-2<\delta<0$ sufficiently close to -2. There is a constant $c>0$ such that for all $\Omega_{A} \in H^{2}\left(\widehat{\mathbb{C}^{2} / \Gamma}, \mathbb{C}\right), \Omega_{B} \in H^{1,1}(\mathcal{X})$ and $\Omega=\Omega_{A} \oplus \Omega_{B}$, we have
$$c\left\|\square_{t} \Psi_{t}\left(\Omega_{A}\right)\right\|_{C_{\delta-2}^{0, \alpha}} \leq \varepsilon^{2-\beta(\delta+4)}\left\|\Omega_{A}\right\|_{A}$$
and
$$c\left\|\square_{t} \Psi_{t}\left(\Omega_{B}\right)\right\|_{C_{\delta-2}^{0, \alpha}} \leq \varepsilon^{-\beta \delta}\left\|\Omega_{B}\right\|_{B}$$
In particular
$$c\left\|\square_{t} \Psi_{t}(\Omega)\right\|_{C_{\delta-2}^{0, \alpha}} \leq \varepsilon^{\beta_{1}}\|\Omega\|_{\delta, t}$$
where $\beta_{1}=\min (-\beta \delta, 4+\delta-\beta(\delta+4))$ is very close to 1, by definition.
Similarly, if $\Xi \in H^{0,1}(\mathcal{X})$, we have
$$c\left\|\square_{t} \Psi_{t}(\Xi)\right\|_{C_{\delta-1}^{0, \alpha}} \leq \varepsilon^{-\beta(\delta+1)}\|\Xi\|_{B} .$$
Proof. The proof is similar to the one for Lemma 15 and Corollary 16. Let $\gamma_{A, t} \in$ $\mathcal{H}_{A, t}^{1,1}$ be a family of harmonic (1, 1)-forms on the family of ALE representing $\Omega_{A}$. Then, we have uniform estimates $\gamma_{A, t}=\mathcal{O}\left(R^{-4}\right)$ on the annulus $b / \varepsilon \leq R \leq$ $4 b / \varepsilon$. Using the rescaled metric, we deduce an estimate $\left|\Psi_{t}\left(\Omega_{A}\right)\right|=\mathcal{O}\left(\varepsilon^{2} r^{-4}\right)$ on the annulus $b \leq r \leq 4 b$. Hence $\left|\square_{t} \Psi_{t}\left(\Omega_{A}\right)\right|=\mathcal{O}\left(\varepsilon^{2} r^{-6}\right)$ so $\left|r^{2-\delta} \square_{t} \Psi_{t}\left(\Omega_{A}\right)\right|=$ $\mathcal{O}\left(\varepsilon^{2} r^{-4-\delta}\right)$, that is to say $\left|r^{2-\delta} \square_{t} \Psi_{t}\left(\Omega_{A}\right)\right|=\mathcal{O}\left(\varepsilon^{2-\beta(4+\delta)}\right)$ on the annulus. The first part of the lemma follows.

For the second part of the statement, we start with the uniform estimate $\Psi_{t}\left(\Omega_{B}\right)=\mathcal{O}(1)$ on the annulus $b \leq r \leq 4 b$. It follows that $\left|r^{2-\delta} \square_{t} \Psi_{t} \Omega_{B}\right|=$ $\mathcal{O}\left(\varepsilon^{-\beta \delta}\right)$ on the annulus.

On the annulus $4 b \leq r \leq 1$ we have the estimate $\left|J_{0}-J_{t}\right|=\mathcal{O}\left(R^{-4}\right)=\mathcal{O}\left(\varepsilon^{4} r^{-4}\right)$. It follows that $\left|\square_{t} \Psi_{t}\left(\Omega_{B}\right)\right|=\mathcal{O}\left(\varepsilon^{4} r^{-6}\right)$ on this annulus. Thus $\left|r^{2-\delta} \square_{t} \Psi_{t}\left(\Omega_{B}\right)\right|=$ $\mathcal{O}\left(\varepsilon^{4-\beta(4+\delta)}\right)$ on the annulus $4 b \leq r \leq 1$. We see that $4-\beta(4+\delta)$ goes to 3 as $\beta$ is close to -2 and $\beta$ close to 1/2.
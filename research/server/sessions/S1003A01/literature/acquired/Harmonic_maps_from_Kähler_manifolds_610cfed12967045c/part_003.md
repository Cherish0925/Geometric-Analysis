---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: Harmonic maps from Kähler manifolds]

Let $G$ be a reductive ${ }^{23}$ complex algebraic group. The Riemann-Hilbert correspondence gives a bijection between group representations $\rho: \pi_{1} M \rightarrow G, G$-local systems, and flat principal $G$-bundles.

Let $\rho: \pi_{1} M \rightarrow G$ be a reductive representation. Denote by $E_{G}$ be the associated flat principal $G$-bundle and $\omega \in \mathcal{A}^{1}(M, \mathfrak{g})$ its principal connection, which is flat: $\mathrm{d} \omega+\frac{1}{2}[\omega, \omega]=0$. The Cartan decomposition $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$ splits the connection as $\omega=\omega_{\mathfrak{k}}+\omega_{\mathfrak{p}}$.
Remark 6.18. Since $G$ is complex reductive, it is isomorphic to the complexification of its maximal compact: $G \approx K^{\mathbb{C}}$ (the converse is also true). In particular, $\mathfrak{p}=i \mathfrak{k}$.

Theorem 6.4 gives a $\rho$-equivariant harmonic map $f: \tilde{M} \rightarrow \mathrm{X}=G / K$. This induces a reduction of the structure group of $E_{G}$ : we have $K$-bundle $E_{K}$ and an isomorphism of $G$-bundles $\iota: E_{K} \rightarrow E_{G}$. We denote $\imath^{*} \omega=A+\psi$ the splitting of the flat connection in $E_{K}$. Now $A \in \mathcal{A}^{1}\left(E_{K}, \mathfrak{k}\right)$ is a connection on $E_{K}$, and $\psi \in \mathcal{A}^{1}\left(E_{K}, \mathfrak{p}\right)$ descends as a one-form on $M$ with values in $E_{K}(\mathfrak{p})$, the bundle associated to $E_{K}$ via the isotropy representation Ad: $K \rightarrow \operatorname{GL}(\mathfrak{p})$.

The vanishing of the curvature of $\iota^{*} \omega$, broken into $\mathfrak{k}$ and $\mathfrak{p}$ components, gives the equations
$$\begin{aligned}
F^{A}+\frac{1}{2}[\psi, \psi] & =0 \\
\mathrm{~d}_{A} \psi & =0
\end{aligned}$$
(compare with (32)), while the harmonicity of $f$ equates to $\mathrm{d}_{A}^{*} \psi=0$. We are now halfway in the nonabelian Hodge correspondence, having obtained a harmonic bundle (see (27)).

\footnotetext{
${ }^{23}$ i.e. with trivial unipotent radical. Equivalently, it admits a faithful semisimple representation [Mil17]. A connected affine algebraic group over $\mathbb{C}$ is reductive if and only if it has a reductive Lie algebra and its center is of multiplicative type.
}

We can now apply the Siu-Sampson theorem; in fact, Lemma 6.8 still holds verbatim. The $(1,0)$ -form $\varphi=\psi^{1,0}$ makes sense as a form with values in $E_{K}(\mathfrak{g})$ (since $\mathfrak{p}^{\mathbb{C}}=\mathfrak{g}$ ), but we deliberately extend the structure group from $K$ to $G$-to "forget the harmonic metric" in the Higgs bundle. As in Theorem 6.11, we obtain a Higgs bundles, according to the definition:

Definition 6.19. A $G$-Higgs bundle is a pair $\left(\mathcal{E}_{G}, \varphi\right)$, where $\mathcal{E}_{G}$ is a holomorphic principal $G$-bundle and $\varphi$ is a holomorphic section of $\mathcal{E}_{G}(\mathfrak{g}) \otimes \Omega^{1}$ such that $[\varphi, \varphi]=0$.

Remark 6.20. When defining real Higgs bundles, i.e. when $G$ is a real reductive group, tracing back our discussion shows that the Higgs field should be defined as a holomorphic section of $E_{K^{\mathbb{C}}}\left(\mathfrak{p}^{\mathbb{C}}\right) \otimes \Omega^{1}$.

We have successfully constructed a Higgs bundle starting from a reductive representation. Moreover, as in Theorem 6.11, the flatness of the connection yields Hitchin's equation
$$F^{A}-[\varphi, \tau(\varphi)]=0$$
where $\tau: \mathfrak{g} \rightarrow \mathfrak{g}$ is the Cartan involution, extended to $\mathcal{E}_{G}(\mathfrak{g}) \otimes \mathcal{A}^{1}$ by $\tau(A \otimes \alpha)=\tau(A) \otimes \bar{\alpha}$.
As expected, Theorem 6.16 also extends to this setting. First notice that a reduction of the structure group of $\mathcal{E}$ from $G$ to $K$ induces a Chern connection $A$, so that (33) makes sense (see [GGR12]).

Theorem 6.21 (Simpson). Let $(\mathcal{E}, \varphi)$ be a $G$-Higgs bundles with vanishing Chern classes. There exists a reduction of the structure group of $\mathcal{E}$ from $G$ to $K$ such that (33) holds if and only if $(\mathcal{E}, \varphi)$ is polystable.

As before, this theorem gives an inverse of the nonabelian Hodge correspondence from representations to Higgs bundles, and the circle is complete.

\subsection*{6.2.4 The character variety and the moduli space of Higgs bundles}

At this point we have described the nonabelian Hodge correspondence from group representations to Higgs bundles and vice-versa, but avoided talking about the moduli spaces of such objects. It turns out that their construction works strikingly well. Let us very briefly sketch the essential ideas at play.

There are natural morphisms between the objects under consideration, in particular:
\begin{itemize}
\item[-] Two representations are equivalent if they are conjugated by an element of $G$.
\item[-] Two Higgs bundles are equivalent if they differ by a gauge transformation ${ }^{24}$.
\end{itemize}
With these isomorphisms, the nonabelian Hodge correspondence is an equivalence of categories between reductive representations and polystable Higgs bundles with vanishing Chern classes ([Sim94], see [GX08] for a nice exposition of the rank one case). In particular there is a 1:1 correspondence between the isomorphism classes. That being said, it is possible to considerably strengthen this assertion.

Firstly, Simpson extended the equivalence of categories to all representations $\pi_{1} M \rightarrow G$ and all semistable Higgs bundles with vanishing Chern classes [Sim92, §3]. Secondly, and more importantly, the quotient sets can beautifully be realized as algebraic or analytic quotients, yielding a very rich structure.

The best scenario is when $M$ and $G$ both have algebraic structures. The sets $\operatorname{Hom}^{\text {red }}\left(\pi_{1} M, G\right) / G$ (reductive representations up to conjugation) and $\operatorname{Higgs}_{0}^{\mathrm{ps}}(M, G) / \mathcal{G}$ (polystable Higgs bundles with vanishing Chern classes up to equivalence) can then be realized as GIT quotients. Consequently, they inherit an algebraic structure, and are the universal categorical quotients. The first GIT quotient is straightforward to construct, see below. The second is more involved: refer to [Fuj91; Sim94; Sim97].

Remark 6.22. The standard reference for GIT is [MFK94]. For our usage, a nice alternative is [Tho06]. I also point to my notes [Lou15, §B] for an easy introduction to symplectic reduction and GIT.

\footnotetext{
${ }^{24}$ A gauge transformation of a complex vector bundle $E$ is a smooth section of $\operatorname{GL}(E)$. This definition easily generalizes to $G$-bundles. We are being sloppy when talking about gauge equivalence between Higgs bundles, because this assumes that they all have the same underlying complex vector bundle-which is true up to isomorphism.
}

Let $X$ be an algebraic variety over $\mathbb{C}$ and let $G$ be a complex reductive algebraic group acting on $X$. For simplicity we assume $X$ is affine; this includes $X=\operatorname{Hom}(\pi, G)$ where $\pi$ is any finitely presented group. Let $\mathbb{C}[X]$ denote the coordinate ring of regular functions on $M$ and $\mathbb{C}[X]^{G} \subseteq \mathbb{C}[X]$ the subalgebra of $G$-invariant functions. $\mathbb{C}[X]^{G}$ is finitely generated provided $G$ is reductive by Nagata's theorem (answering Hilbert's 14th problem), therefore it is the coordinate ring of an affine algebraic set, namely Spec $\mathbb{C}[X]^{G}$. This algebraic set is the GIT quotient of $X$, denoted $X / / G$. As a topological space, $X / / G$ is isomorphic to the set $X^{\mathrm{ps}} / G$ of orbits of polystable points, i.e. whose orbit is closed, or to the set $X^{\text {ss }} / \sim$ of semistable ${ }^{25}$ points up to equivalence, where two points are equivalent if their orbit closures interset. Indeed, it is a general fact that any semistable orbit contains a unique polystable orbit.

We call the GIT quotients $\mathcal{M}_{\mathrm{B}}:=\operatorname{Hom}\left(\pi_{1} M, G\right) / / G$ and $\mathcal{M}_{\text {Dol }}:=\operatorname{Higgs}_{0}(M, G) / / \mathcal{G}$ the $G$-character variety or Betti moduli space, and the moduli space of G-Higgs bundles (with vanishing Chern classes) or Dolbeault moduli space. Both are finite-dimensional quasiprojective varieties. One can check that polystability in the sense of GIT coincides with reductivity for representations and polystability for Higgs bundles. Since the nonabelian Hodge correspondence induces a bijection between the sets $\operatorname{Hom}^{\text {red }}\left(\pi_{1} M, G\right) / G$ and $\operatorname{Higgs}_{0}^{\mathrm{ps}}(M, G) / \mathcal{G}$, we obtain:

Theorem 6.23. The nonabelian Hodge correspondence induces a bijection $\mathcal{M}_{B} \xrightarrow{\sim} \mathcal{M}_{\text {Dol }}$.
We shall see that this bijection is a real-analytic map between varieties, but not complex-analytic.
In addition to giving a natural framework for the nonabelian Hodge correspondence, the benefit of constructing the moduli spaces is to provide additional structure and features. For instance, we have seen that GIT quotients provide an algebraic structure. Another remarkable feauture is their relation to symplectic reduction (this is essentially the Kempf-Ness theorem, see [MFK94, Chap. 8]).

Goldman [Gol84], following Atiyah-Bott [AB83], adapted the technique of symplectic reduction to the infinite-dimensional space of connections in a vector bundle, interpreting the curvature of a connection as a moment map for the action of the gauge group. The main result of [Gol84] is the existence of a natural complex symplectic structure in the character variety $\mathcal{M}_{\mathrm{B}}$ when $\operatorname{dim}_{\mathbb{C}} M=1$.

Hitchin [Hit87] used similar techniques to construct the moduli space of Higgs bundles $\mathcal{M}_{\text {Dol }}$ as a hyper-Kähler quotient, and showed that the nonabelian Hodge correspondence $\mathcal{M}_{\mathrm{B}} \stackrel{\sim}{\rightarrow} \mathcal{M}_{\text {Dol }}$ is complex-analytic with respect to one of the complex structures. Deligne (unpublished, see [Sim97]) realized that the twistor space of this hyper-Kähler structure can elegantly be realized as the moduli space of $\lambda$-connections, which Simpson calls Hodge moduli space $\mathcal{M}_{\text {Hod }}$. In this picture, $\mathcal{M}_{\mathrm{B}}$ and $\mathcal{M}_{\text {Dol }}$ are two special fibers of the holomorphic fiber bundle $\mathcal{M}_{\text {Hod }} \rightarrow \mathbb{C} P^{1}$.

We finally mention two other remarkable features of the moduli space of Higgs bundles $\mathcal{M}_{\text {Dol }}$, both going back to Hitchin [Hit87]. Via the nonabelian Hodge correspondence, they also describe fascinating features of the character variety:
\begin{itemize}
\item[-] The $\mathbb{C}^{*}$-action. There is an action of $\mathbb{C}^{*}$ on Higgs bundles by $\lambda \cdot(\mathcal{E}, \varphi)=(\mathcal{E}, \lambda \varphi)$, inducing an action on $\mathcal{M}_{\text {Dol }}$. When transported to the character variety , this $\mathbb{C}^{*}$-action should be interpreted as a Hodge structure on $\mathrm{H}^{1}(M, G)=\operatorname{Hom}\left(\pi_{1} M, G\right) / G$ that generalizes the Hodge decomposition of $\mathrm{H}^{1}(M, \mathbb{C})$ (see § 6.1.3 and Remark 6.2). Simpson additionally showed that the fixed points of the action correspond to variations of Hodge structure [Sim92].
\item[-] The Hitchin fibration. For simplicity, we take $G=\mathrm{GL}(n, \mathbb{C})$. The coefficients of the characteristic polynomial of the Higgs field defines a holomorphic fibration
$$\mathcal{M}_{\mathrm{Dol}} \rightarrow \bigoplus_{j=0}^{n} \mathrm{H}^{0}\left(M,\left(\Omega^{1}\right)^{\otimes j}\right) .$$
The study of this map and its fibers by various authors has produced an abundance of interesting results concerning both Higgs bundles and group representations. It was also famously used by Ngô [Ngô10] to prove the fundamental lemma, a key result in the Langlands program.
\end{itemize}

\footnotetext{
${ }^{25}$ Let us not give the general definition, but point out that all points are semistable when $X$ is affine.
}

\section*{References}
\begin{itemize}
\item[] [Alb68] S. I. Al'ber. "Spaces of mappings into a manifold of negative curvature". In: Dokl. Akad. Nauk SSSR 178 (1968), pp. 13-16 (cited p. 31).
\item[] [Amo+96] J. Amorós et al. Fundamental groups of compact Kähler manifolds. Vol. 44. Mathematical Surveys and Monographs. American Mathematical Society, Providence, RI, 1996, pp. xii+140. doi: 10.1090/surv/044 (cited pp. 2, 14, 17, 20-22, 25, 27).
\item[] [AF05] C. S. Aravinda and F. T. Farrell. "Nonpositivity: curvature vs. curvature operator". In: Proc. Amer. Math. Soc. 133.1 (2005), pp. 191-192. doi: 10.1090/S0002-9939-04-07531-8 (cited p. 17).
\item[] [AB83] M. F. Atiyah and R. Bott. "The Yang-Mills equations over Riemann surfaces". In: Philos. Trans. Roy. Soc. London Ser. A 308.1505 (1983), pp. 523-615. doi: 10.1098/rsta. 1983.0017 (cited p. 35).
\item[] [Ber+02] José Bertin et al. Introduction to Hodge theory. Vol. 8. SMF/AMS Texts and Monographs. Translated from the 1996 French original by James Lewis and Peters. American Mathematical Society, Providence, RI; Société Mathématique de France, Paris, 2002, pp. x+232 (cited pp. 8, 28).
\item[] [Bra12] Steven Bradlow. "Introduction to Higgs bundles". Series of lectures given at the 2012 GEAR retreat. Slides and videos available at http://gear.math.illinois.edu/programs/retreats2012-archive.html. 2012 (cited p. 27).
\item[] [Bra20] Lukas Brantner. "Abelian and nonabelian Hodge theory". Online notes. URL: https://scholar.harvard.edu/files/brantner/files/hodge.pdf. 2020 (cited pp. 27, 32).
\item[] [Bry85] Robert L. Bryant. "Lie groups and twistor spaces". In: Duke Math. J. 52.1 (1985), pp. 223-261. doi: 10.1215/S0012-7094-85-05213-5 (cited p. 18).
\item[] [CV59] Eugenio Calabi and Edoardo Vesentini. "Sur les variétés complexes compactes localement symétriques". In: Bull. Soc. Math. France 87 (1959), pp. 311-317 (cited p. 27).
\item[] [CV60] Eugenio Calabi and Edoardo Vesentini. "On compact, locally symmetric Kähler manifolds". In: Ann. of Math. (2) 71 (1960), pp. 472-507. doi: 10.2307/1969939 (cited p. 27).
\item[] [CMP17] James Carlson, Stefan Müller-Stach, and Chris Peters. Period mappings and period domains. Vol. 168. Cambridge Studies in Advanced Mathematics. Second edition of [ MR2012297]. Cambridge University Press, Cambridge, 2017, pp. xiv+562 (cited p. 28).
\item[] [CH91] James A. Carlson and Luis Hernández. "Harmonic maps from compact Kähler manifolds to exceptional hyperbolic spaces". In: J. Geom. Anal. 1.4 (1991), pp. 339-357. doi: 10.1007/BF02921310 (cited p. 26).
\item[] [CT89] James A. Carlson and Domingo Toledo. "Harmonic mappings of Kähler manifolds to locally symmetric spaces". In: Inst. Hautes Études Sci. Publ. Math. 69 (1989), pp. 173-201 (cited pp. 2, 20, 25, 26).
\item[] [CT93] James A. Carlson and Domingo Toledo. "Rigidity of harmonic maps of maximum rank". In: J. Geom. Anal. 3.2 (1993), pp. 99-140. doi: 10.1007/BF02921579 (cited p. 26).
\item[] [Chi13] Yuan-Jen Chiang. Developments of harmonic maps, wave maps and Yang-Mills fields into biharmonic maps, biwave maps and bi-Yang-Mills fields. Frontiers in Mathematics. Birkhäuser/Springer, Basel, 2013, pp. xxii+399. doi: 10.1007/978-3-0348-0534-6 (cited p. 3).
\item[] [Cor88] Kevin Corlette. "Flat $G$-bundles with canonical metrics". In: J. Differential Geom. 28.3 (1988), pp. 361-382 (cited pp. 2, 30).
\item[] [Cor92] Kevin Corlette. "Archimedean superrigidity and hyperbolic geometry". In: Ann. of Math. (2) 135.1 (1992), pp. 165-182. doi: 10.2307/2946567 (cited p. 27).
\item[] [Dem12] Jean-Pierre Demailly. Complex Analytic and Differential Geometry. OpenContent Book. Freely available at https://www-fourier.ujf-grenoble.fr/~demailly/documents.html. 2012 (cited p. 13).
\item[] [Don85] S. K. Donaldson. "Anti self-dual Yang-Mills connections over complex algebraic surfaces and stable vector bundles". In: Proc. London Math. Soc. (3) 50.1 (1985), pp. 1-26. doi: 10.1112/plms/s3-50.1.1 (cited p. 29).
\item[] [Don87] S. K. Donaldson. "Twisted harmonic maps and the self-duality equations". In: Proc. London Math. Soc. (3) 55.1 (1987), pp. 127-131. doi: 10.1112/plms/s3-55.1.127 (cited p. 2).
\item[] [Dup03] Johan Dupont. "Fibre bundles and Chern-Weil theory". https://data.math.au.dk/publications/ln/2003/imf-ln-2003-69.pdf. 2003 (cited p. 33).
\item[] [EL95a] J. Eells and L. Lemaire. "Another report on harmonic maps [Bull. London Math. Soc. 20 (1988), no. 5, 385-524; MR0956352 (89i:58027)]". In: Two reports on harmonic maps. World Sci. Publ., River Edge, NJ, 1995, pp. 69-208 (cited p. 22).
\item[] [ES64] James Eells Jr. and J. H. Sampson. "Harmonic mappings of Riemannian manifolds". In: Amer. J. Math. 86 (1964), pp. 109-160 (cited pp. 2-4, 9, 10, 18).
\end{itemize}
[EL83] James Eells and Luc Lemaire. Selected topics in harmonic maps. Vol. 50. CBMS Regional Conference Series in Mathematics. Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 1983, pp. v+85. doi: 10.1090/cbms/050 (cited pp. 3, 8, 13).
[EL95b] James Eells and Luc Lemaire. Two reports on harmonic maps. World Scientific Publishing Co., Inc., River Edge, NJ, 1995, pp. xii+216. doi: 10.1142/9789812832030 (cited p. 3).
[Fuj91] Akira Fujiki. "Hyper-Kähler structure on the moduli space of flat bundles". In: Prospects in complex geometry (Katata and Kyoto, 1989). Vol. 1468. Lecture Notes in Math. Springer, Berlin, 1991, pp. 1-83. doi: 10.1007/BFb0086187 (cited p. 34).
[GHL04] Sylvestre Gallot, Dominique Hulin, and Jacques Lafontaine. Riemannian geometry. Third. Universitext. Springer-Verlag, Berlin, 2004, pp. xvi+322. doi: 10.1007/978-3-642-18855-8 (cited p. 3).
[GGR12] Oscar Garcia-Prada, Peter B. Gothen, and Ignasi Mundet i Riera. The Hitchin-Kobayashi correspondence, Higgs pairs and surface group representations. 2012 (cited p. 34).
[GR15] Alberto García-Raboso and Steven Rayan. "Introduction to nonabelian Hodge theory: flat connections, Higgs bundles and complex variations of Hodge structure". In: Calabi-Yau varieties: arithmetic, geometry and physics. Vol. 34. Fields Inst. Monogr. Fields Inst. Res. Math. Sci., Toronto, ON, 2015, pp. 131-171. doi: 10. 1007/978-1-4939-2830-9_5 (cited p. 27).
[GLM18] Jonah Gaster, Brice Loustau, and Léonard Monsaingeon. "Computing discrete equivariant harmonic maps". In: Preprint: arXiv:1810.11932 (2018) (cited p. 10).
[Gol84] William M. Goldman. "The symplectic nature of fundamental groups of surfaces". In: Adv. in Math. 54.2 (1984), pp. 200-225. doi: 10.1016/0001-8708 (84) 90040-9 (cited p. 35).
[Gol10] William M. Goldman. "Locally homogeneous geometric manifolds". In: Proceedings of the International Congress of Mathematicians. Volume II. Hindustan Book Agency, New Delhi, 2010, pp. 717-744 (cited p. 25).
[GX08] William M. Goldman and Eugene Z. Xia. "Rank one Higgs bundles and representations of fundamental groups of Riemann surfaces". In: Mem. Amer. Math. Soc. 193.904 (2008), pp. viii+69. doi: 10.1090/memo/0904 (cited p. 34).
[Got14] Peter B. Gothen. "Representations of surface groups and Higgs bundles". In: Moduli spaces. Vol. 411. London Math. Soc. Lecture Note Ser. Cambridge Univ. Press, Cambridge, 2014, pp. 151-178 (cited pp. 27, 33).
[GP91] M. Gromov and P. Pansu. "Rigidity of lattices: an introduction". In: Geometric topology: recent developments (Montecatini Terme, 1990). Vol. 1504. Lecture Notes in Math. Springer, Berlin, 1991, pp. 39-137. doi: 10.1007/BFb0094289 (cited p. 27).
[GS92] Mikhail Gromov and Richard Schoen. "Harmonic maps into singular spaces and $p$-adic superrigidity for lattices in groups of rank one". In: Inst. Hautes Études Sci. Publ. Math. 76 (1992), pp. 165-246 (cited p. 27).
[Gui18] Olivier Guichard. "An introduction to the differential geometry of flat bundles and of Higgs bundles". In: The geometry, topology and physics of moduli spaces of Higgs bundles. Vol. 36. Lect. Notes Ser. Inst. Math. Sci. Natl. Univ. Singap. World Sci. Publ., Hackensack, NJ, 2018, pp. 1-63 (cited p. 27).
[Har67] Philip Hartman. "On homotopic harmonic maps". In: Canad. J. Math. 19 (1967), pp. 673-687. doi: 10.4153/CJM-1967-062-6 (cited p. 31).
[Hel01] Sigurdur Helgason. Differential geometry, Lie groups, and symmetric spaces. Vol. 34. Graduate Studies in Mathematics. Corrected reprint of the 1978 original. American Mathematical Society, Providence, RI, 2001, pp. xxvi+641. doi: 10.1090/gsm/034 (cited pp. 23, 24).
[Hit87] N. J. Hitchin. "The self-duality equations on a Riemann surface". In: Proc. London Math. Soc. (3) 55.1 (1987), pp. 59-126. doi: 10.1112/plms/s3-55.1.59 (cited pp. 2, 31, 32, 35).
[Ish79] Tôru Ishihara. "A mapping of Riemannian manifolds which preserves harmonic functions". In: J. Math. Kyoto Univ. 19.2 (1979), pp. 215-229. doi: 10.1215/kjm/1250522428 (cited p. 18).
[Jos84] Jürgen Jost. Harmonic mappings between Riemannian manifolds. Vol. 4. Proceedings of the Centre for Mathematical Analysis, Australian National University. Australian National University, Centre for Mathematical Analysis, Canberra, 1984, pp. iv+177 (cited pp. 10, 11).
[Jos08] Jürgen Jost. "Harmonic mappings". In: Handbook of geometric analysis. No. 1. Vol. 7. Adv. Lect. Math. (ALM). Int. Press, Somerville, MA, 2008, pp. 147-194 (cited p. 3).
[Jos17] Jürgen Jost. Riemannian geometry and geometric analysis. Seventh. Universitext. Springer, Cham, 2017, pp. xiv+697. doi: 10.1007/978-3-319-61860-9 (cited p. 3).
[JY83] Jürgen Jost and Shing Tung Yau. "Harmonic mappings and Kähler manifolds". In: Math. Ann. 262.2 (1983), pp. 145-166. doi: 10.1007/BF01455308 (cited p. 17).
[JY97] Jürgen Jost and Shing-Tung Yau. "Harmonic maps and superrigidity". In: Tsing Hua lectures on geometry \& analysis (Hsinchu, 1990-1991). Int. Press, Cambridge, MA, 1997, pp. 213-246 (cited p. 27).
[JZ97] Jürgen Jost and Kang Zuo. "Harmonic maps of infinite energy and rigidity results for representations of fundamental groups of quasiprojective varieties". In: J. Differential Geom. 47.3 (1997), pp. 469-503 (cited p. 27).
[KN96] Shoshichi Kobayashi and Katsumi Nomizu. Foundations of differential geometry. Vol. II. Wiley Classics Library. Reprint of the 1969 original, A Wiley-Interscience Publication. John Wiley \& Sons, Inc., New York, 1996, pp. xvi+468 (cited p. 23).
[KM97] Andreas Kriegl and Peter W. Michor. The convenient setting of global analysis. Vol. 53. Mathematical Surveys and Monographs. American Mathematical Society, Providence, RI, 1997, pp. x+618. doi: 10.1090/surv/053 (cited p. 5).
[Lab91] François Labourie. "Existence d'applications harmoniques tordues à valeurs dans les variétés à courbure négative". In: Proc. Amer. Math. Soc. 111.3 (1991), pp. 877-882. doi: 10.2307/2048427 (cited p. 31).
[Le 91] Joseph Le Potier. "Fibrés de Higgs et systèmes locaux". In: 201-203. Séminaire Bourbaki, Vol. 1990/91. 1991, Exp. No. 737, 221-268 (1992) (cited p. 27).
[Lee18] John M. Lee. Introduction to Riemannian manifolds. Vol. 176. Graduate Texts in Mathematics. Second edition of [ MR1468735]. Springer, Cham, 2018, pp. xiii+437 (cited p. 3).
[Li19] Qiongling Li. "An introduction to Higgs bundles via harmonic maps". In: SIGMA Symmetry Integrability Geom. Methods Appl. 15 (2019), Paper No. 035, 30. doi: 10.3842/SIGMA. 2019.035 (cited p. 27).
[LW08] Fanghua Lin and Changyou Wang. The analysis of harmonic maps and their heat flows. World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ, 2008, pp. xii+267. doi: 10.1142/9789812779533 (cited p. 11).
[Lou15] Brice Loustau. Minimal surfaces and quasi-Fuchsian structures. Online notes. URL: http://www.brice.loustau.eu/ressources/Loustau-Asheville2015.pdf. 2015 (cited p. 34).
[Mar75] G. A. Margulis. "Discrete groups of motions of manifolds of nonpositive curvature". In: Proceedings of the International Congress of Mathematicians (Vancouver, B.C., 1974), Vol. 2. 1975, pp. 21-34 (cited p. 27).
[Mil17] J. S. Milne. Algebraic groups. Vol. 170. Cambridge Studies in Advanced Mathematics. The theory of group schemes of finite type over a field. Cambridge University Press, Cambridge, 2017, pp. xvi+644. doi: 10.1017/9781316711736 (cited p. 33).
[Mok89] Ngaiming Mok. Metric rigidity theorems on Hermitian locally symmetric manifolds. Vol. 6. Series in Pure Mathematics. World Scientific Publishing Co., Inc., Teaneck, NJ, 1989, pp. xiv+278. doi: 10.1142/0773 (cited p. 27).
[MSY93] Ngaiming Mok, Yum Tong Siu, and Sai-Kee Yeung. "Geometric superrigidity". In: Invent. Math. 113.1 (1993), pp. 57-83. doi: 10.1007/BF01244302 (cited p. 27).
[Mos64] Jürgen Moser. "A Harnack inequality for parabolic differential equations". In: Comm. Pure Appl. Math. 17 (1964), pp. 101-134. doi: 10.1002/cpa. 3160170106 (cited p. 11).
[Mos68] G. D. Mostow. "Quasi-conformal mappings in $n$-space and the rigidity of hyperbolic space forms". In: Inst. Hautes Études Sci. Publ. Math. 34 (1968), pp. 53-104 (cited p. 27).
[Mos73] G. D. Mostow. Strong rigidity of locally symmetric spaces. Annals of Mathematics Studies, No. 78. Princeton University Press, Princeton, N.J.; University of Tokyo Press, Tokyo, 1973, pp. v+195 (cited p. 27).
[MS80] G. D. Mostow and Yum Tong Siu. "A compact Kähler surface of negative curvature not covered by the ball". In: Ann. of Math. (2) 112.2 (1980), pp. 321-360. doi: 10.2307/1971149 (cited p. 18).
[MFK94] D. Mumford, J. Fogarty, and F. Kirwan. Geometric invariant theory. Third. Vol. 34. Ergebnisse der Mathematik und ihrer Grenzgebiete (2) [Results in Mathematics and Related Areas (2)]. Springer-Verlag, Berlin, 1994, pp. xiv+292. doi: 10.1007/978-3-642-57916-5 (cited pp. 34, 35).
[NS65] M. S. Narasimhan and C. S. Seshadri. "Stable and unitary vector bundles on a compact Riemann surface". In: Ann. of Math. (2) 82 (1965), pp. 540-567. doi: 10.2307/1970710 (cited p. 29).
[Ngô10] Bao Châu Ngô. "Le lemme fondamental pour les algèbres de Lie". In: Publ. Math. Inst. Hautes Études Sci. 111 (2010), pp. 1-169. doi: 10.1007/s10240-010-0026-7 (cited p. 35).
[Nic13] Liviu I. Nicolaescu. Weitzenböck Identities. MathOverflow. https://mathoverflow.net/q/107189 (version: 2013-10-25). 2013 (cited p. 13).
[OU90] Yoshihiro Ohnita and Seiichi Udagawa. "Stability, complex-analyticity and constancy of pluriharmonic maps from compact Kaehler manifolds". In: Math. Z. 205.4 (1990), pp. 629-644. doi: 10.1007/BF02571268 (cited pp. 16, 22, 26).
[OV90] Yoshihiro Ohnita and Giorgio Valli. "Pluriharmonic maps into compact Lie groups and factorization into unitons". In: Proc. London Math. Soc. (3) 61.3 (1990), pp. 546-570. doi: 10.1112/plms/s3-61.3.546 (cited p. 20).
[Pan95] Pierre Pansu. "Sous-groupes discrets des groupes de Lie: rigidité, arithméticité". In: 227. Séminaire Bourbaki, Vol. 1993/94. 1995, Exp. No. 778, 3, 69-105 (cited p. 27).
[Pau20] Frédéric Paulin. "Groupes et géométries". Online notes. URL: https://www.imo.universite-paris-saclay.fr/~paulin/notescours/cours_georiem.pdf. 2020 (cited p. 23).
[Pec17] Vincent Pecastaing. "Riemannian symmetric spaces". Online notes. URL: http://math.uni.lu/~georeading/attachments/vincent_pecastaing.pdf. 2017 (cited p. 23).
\begin{itemize}
\item[] [Pra73] Gopal Prasad. "Strong rigidity of Q-rank 1 lattices". In: Invent. Math. 21 (1973), pp. 255-286. doi: 10.1007/BF01418789 (cited p. 27).
\item[] [Rat06] John G. Ratcliffe. Foundations of hyperbolic manifolds. Second. Vol. 149. Graduate Texts in Mathematics. Springer, New York, 2006, pp. xii+779 (cited p. 25).
\item[] [Sam86] J. H. Sampson. "Applications of harmonic maps to Kähler geometry". In: Complex differential geometry and nonlinear differential equations (Brunswick, Maine, 1984). Vol. 49. Contemp. Math. Amer. Math. Soc., Providence, RI, 1986, pp. 125-134. doi: 10.1090/conm/049/833809 (cited pp. 2, 17, 18, 20-22, 26).
\item[] [Sik12] Adam S. Sikora. "Character varieties". In: Trans. Amer. Math. Soc. 364.10 (2012), pp. 5173-5208. doi: 10.1090/S0002-9947-2012-05448-1 (cited p. 30).
\item[] [Sim88] Carlos T. Simpson. "Constructing variations of Hodge structure using Yang-Mills theory and applications to uniformization". In: J. Amer. Math. Soc. 1.4 (1988), pp. 867-918. doi: 10.2307/1990994 (cited pp. 2, 32).
\item[] [Sim91] Carlos T. Simpson. "Nonabelian Hodge theory". In: Proceedings of the International Congress of Mathematicians, Vol. I, II (Kyoto, 1990). Math. Soc. Japan, Tokyo, 1991, pp. 747-756 (cited pp. 2, 30).
\item[] [Sim92] Carlos T. Simpson. "Higgs bundles and local systems". In: Inst. Hautes Études Sci. Publ. Math. 75 (1992), pp. 5-95 (cited pp. 2, 27, 34, 35).
\item[] [Sim94] Carlos T. Simpson. "Moduli of representations of the fundamental group of a smooth projective variety, I and II". In: Inst. Hautes Études Sci. Publ. Math. 79 and 80 (1994), 47-129 and 5-79 (cited pp. 2, 34).
\item[] [Sim97] Carlos T. Simpson. "The Hodge filtration on nonabelian cohomology". In: Algebraic geometry-Santa Cruz 1995. Vol. 62. Proc. Sympos. Pure Math. Amer. Math. Soc., Providence, RI, 1997, pp. 217-281. doi: 10.1090/pspum/062.2/1492538 (cited pp. 27, 34, 35).
\item[] [Siu80] Yum Tong Siu. "The complex-analyticity of harmonic maps and the strong rigidity of compact Kähler manifolds". In: Ann. of Math. (2) 112.1 (1980), pp. 73-111. doi: 10.2307/1971321 (cited pp. 2, 17, 18, 21).
\item[] [Siu82] Yum Tong Siu. "Complex-analyticity of harmonic maps, vanishing and Lefschetz theorems". In: J. Differential Geometry 17.1 (1982), pp. 55-138 (cited p. 26).
\item[] [Spa04] R. J. Spatzier. "An invitation to rigidity theory". In: Modern dynamical systems and applications. Cambridge Univ. Press, Cambridge, 2004, pp. 211-231 (cited p. 27).
\item[] [Tho06] R. P. Thomas. "Notes on GIT and symplectic reduction for bundles and varieties". In: Surveys in differential geometry. Vol. X. Vol. 10. Surv. Differ. Geom. Int. Press, Somerville, MA, 2006, pp. 221-273. doi: 10.4310/SDG.2005.v10.n1.a7 (cited p. 34).
\item[] [Tol99] Domingo Toledo. "Rigidity theorems in Kähler geometry and fundamental groups of varieties". In: Several complex variables (Berkeley, CA, 1995-1996). Vol. 37. Math. Sci. Res. Inst. Publ. Cambridge Univ. Press, Cambridge, 1999, pp. 509-533 (cited p. 21).
\item[] [Uda88] Seiichi Udagawa. "Holomorphicity of certain stable harmonic maps and minimal immersions". In: Proc. London Math. Soc. (3) 57.3 (1988), pp. 577-598. doi: 10.1112/plms/s3-57.3.577 (cited p. 26).
\item[] [UY86] K. Uhlenbeck and S.-T. Yau. "On the existence of Hermitian-Yang-Mills connections in stable vector bundles". In: vol. 39. S, suppl. Frontiers of the mathematical sciences: 1985 (New York, 1985). 1986, S257-S293. doi: 10. 1002/cpa. 3160390714 (cited p. 29).
\item[] [Voi07] Claire Voisin. Hodge theory and complex algebraic geometry. I. English. Vol. 76. Cambridge Studies in Advanced Mathematics. Translated from the French by Leila Schneps. Cambridge University Press, Cambridge, 2007, pp. x+322 (cited p. 28).
\item[] [Voi08] Claire Voisin. Hodge theory and the topology of compact Kähler and complex projective manifolds. Lecture notes published online. URL: https://www.math.columbia.edu/~thaddeus/seattle/voisin.pdf. 2008 (cited p. 21).
\item[] [Wei62] André Weil. "On discrete subgroups of Lie groups. II". In: Ann. of Math. (2) 75 (1962), pp. 578-602. doi: 10.2307/1970212 (cited p. 27).
\item[] [Wel08] Raymond O. Wells Jr. Differential analysis on complex manifolds. Third. Vol. 65. Graduate Texts in Mathematics. With a new appendix by Oscar Garcia-Prada. Springer, New York, 2008, pp. xiv+299. doi: 10.1007/978-0-387-73892-5 (cited p. 27).
\item[] [Wen16] Richard A. Wentworth. "Higgs bundles and local systems on Riemann surfaces". In: Geometry and quantization of moduli spaces. Adv. Courses Math. CRM Barcelona. Birkhäuser/Springer, Cham, 2016, pp. 165-219 (cited pp. 27, 33).
\item[] [Wu14] Yunhui Wu. "The Riemannian sectional curvature operator of the Weil-Petersson metric and its application". In: $\mathcal{J}$. Differential Geom. 96.3 (2014), pp. 507-530 (cited p. 17).
\item[] [Xin96] Yuanlong Xin. Geometry of harmonic maps. Vol. 23. Progress in Nonlinear Differential Equations and their Applications. Birkhäuser Boston, Inc., Boston, MA, 1996, pp. x+241. doi: 10.1007/978-1-4612-4084-6 (cited pp. 3, 13, 19, 20).
\item[] [YZ91] S.-T. Yau and F. Zheng. "Negatively $\frac{1}{4}$-pinched Riemannian metric on a compact Kähler manifold". In: Invent. Math. 103.3 (1991), pp. 527-535. doi: 10.1007/BF01239525 (cited p. 17).
\item[] [Zhe00] Fangyang Zheng. Complex differential geometry. Vol. 18. AMS/IP Studies in Advanced Mathematics. American Mathematical Society, Providence, RI; International Press, Boston, MA, 2000, pp. xii+264 (cited pp. 17, 18).
\end{itemize}
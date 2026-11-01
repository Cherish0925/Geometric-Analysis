---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: The Yamabe Problem]

$$\int_{S_{\rho}} z^{i}z^{j} d\omega_{\rho} = \frac{1}{n} \delta^{i j} \rho^{2} \omega_{\rho},$$

we find that

$$h(\rho) = \begin{cases}
1 + \frac{1}{96n(n-6)} |W(P)|^2 \rho^{-4} + O''(\rho^{-5}) & \text{if } n \geqslant 7, \\
1 + \frac{1}{576} |W(P)|^2 \rho^{-4} \log \rho + O''(\rho^{-4}) & \text{if } n = 6.
\end{cases}$$

Thus if $M$ is not locally conformally flat we can choose a point $P \in M$ with $W(P) \neq 0$, and then $\mu = C|W(P)|^2 > 0$. On the other hand, if $n < 6$ or $M$ is locally conformally flat, then Lemma 9.7 and the positive mass theorem show that $\mu > 0$ unless $\hat{M}$ is conformal to $\mathbf{R}^{n}$, in which case $M$ is conformal to $S^n$. $\square$

---

There are several questions related to the Yamabe problem that are of considerable current interest. Yau [Yau] and others have posed the Yamabe problem for complete noncompact Riemannian manifolds. Using the methods of weighted spaces discussed in §9, one can show that an asymptotically flat manifold $N$ of order $\tau > (n-2)/2$ with positive Yamabe invariant $\lambda(N)$ has an asymptotically flat conformal metric of zero scalar curvature provided the scalar curvature satisfies $S \in C_{-r-2}^{0,\alpha}(N)$. More generally, Patricio Aviles and Robert McOwen [AM] have recently obtained some interesting results about conformal deformations of noncompact manifolds, including a proof that the Yamabe problem is solvable for complete Riemannian manifolds whose scalar curvature is negative near infinity. In [SY6], Schoen and Yau have made progress toward understanding which open submanifolds of the sphere admit complete conformal metrics of constant scalar curvature.

A second question concerns the properties of the functional $Q_g$. The solution of the Yamabe problem is based on showing that the minimum of $Q_g$ is realized. It would be interesting to have a better understanding of the analytic properties of $Q_g$, and in particular to examine the higher critical points. Recently Ding Weiyue [Wy] has shown that $Q_{\hat{g}}$ has infinitely many critical values on the sphere (although it follows from Obata’s theorem that the minima are the only critical functions that are strictly positive). Schoen has shown that the convergence theorem 4.5 holds for sequences $\{\varphi_s\}$ that are solutions—but not necessarily minima—of the subcritical problem, and for which $\{Q_g(\varphi_s)\}$ is bounded.

In another direction, the Yamabe problem can also be posed for CR manifolds, the abstract models of real hypersurfaces in complex manifolds. A strictly pseudoconvex CR manifold is an odd-dimensional manifold with a given codimension 1 sub-bundle of its tangent bundle, which carries a complex structure and a hermitian metric (the Levi form) defined only up to a conformal factor. S. Webster [We] has defined a notion of covariant differentiation and curvature for the Levi form, and it is natural to ask whether the conformal factor can be chosen so that the Webster scalar curvature is constant. This is the CR Yamabe problem.

The formal structure of this problem is identical in many respects to that of the Riemannian Yamabe problem. The analysis, however, is considerably more difficult since the operator that takes the place of the Laplacian is only subelliptic rather than elliptic. Nonetheless, by using more delicate Sobolev estimates, one can still prove the analogue of Theorem A; this has been done by Lee and David Jerison in [JL1 and JL2].

In order to determine when the problem can be solved, one must identify the extremals for the “model case”, the sphere in $C^{n+1}$. Using a generalization of Obata’s argument, Lee and Jerison have shown in [JL3] that the CR Yamabe functional is minimized by the standard Levi form on the sphere and its images under CR automorphisms.

Once the extremals are known, one must calculate the asymptotic expansion for the Yamabe functional of an appropriate test function, and relate it to local CR invariants. This calculation is significantly more complicated than in the Riemannian case, and requires the construction of special coordinates analogous to conformal normal coordinates. In [JL4], Lee and Jerison have carried out this calculation and proved the following analogue of Theorem B: the CR Yamabe problem can be solved on CR manifolds of dimension $ \geqslant 5 $ that are not locally CR equivalent to the sphere ("locally spherical").

When the dimension is 3 or the manifold is locally spherical, this local approach does not work and we are in a situation analogous to Theorem C. In that case one needs an analogue of the positive mass theorem for CR manifolds. This problem is still completely open.

Appendix: Witten's proof. In this appendix we give a proof of Witten's Theorem 10.3, beginning with a rapid summary of the geometric context of spinors. More details on the constructions discussed here may be found in [PT].

The group SO(n), $ n \geqslant 3 $ , has a twofold universal covering group called Spin(n). This group has a fundamental unitary representation on a space V of complex dimension $ 2^{n-2} $ called the spin representation $\rho$: Spin(n) $\rightarrow$ Aut(V). When n is odd V is irreducible, and when n is even V = $ V_{+} \oplus V_{-} $ is the direct sum of two irreducible representations. In addition there is an equivariant linear Clifford multiplication map c: $ \mathbf{R}^{n} \rightarrow $ End(V). The map $ c(x) $ is skew-hermitian and satisfies $ c(x)c(y)+c(y)c(x)=-2\langle x,y\rangle $ Id for all x, y $\in$ $ \mathbf{R}^{n} $ .

For example, Spin(3) $\cong$ SU(2) is the universal cover of SO(3), and $\rho$ is the standard representation of SU(2) on $ \mathbf{C}^{2} $ . In this case Clifford multiplication is simply

$$c(x,y,z)=\begin{pmatrix} ix & iy+z \\ iy-z & -ix\end{pmatrix}\in \mathscr{S}u(2).$$

For later use we note that the Lie algebra representation $\bar{\rho}$: spin(n) $\rightarrow$ End(V) can be written in terms of Clifford multiplication. Namely, for any skew-symmetric matrix $ A\in\mathscr{S}o(n)\cong $ spin(n) we have

(A.1) $$\bar{\rho}(A)=-\frac{1}{4}A_{ij}c(e^{i})c(e^{j})=-\frac{1}{8}A_{ij}[c(e^{i}),c(e^{j})],$$

where $ \{e^{i}\} $ is the standard basis of $ \mathbf{R}^{n} $ . (It is easy to verify that this is a Lie algebra representation.)

Now suppose $(N,g)$ is an oriented Riemannian manifold, and $ F_{N} $ the bundle of oriented orthonormal frames for $ T^{*}N $ (a principal SO(n) bundle). When the second Stiefel-Whitney class $ \omega_{2}(N) $ vanishes we can choose a lift $ \tilde{F}_{N} $ of $ F_{N} $ to a principal Spin(n) bundle; in this case one says N is a spin manifold. We then have an associated Hermitian vector bundle $ S=\tilde{F}_{N} \times_{\rho} V $ called the spin vector bundle, and a global Clifford multiplication $ c:$ $ \Gamma(T^{*}N)\rightarrow $ $ \Gamma(\text{End}(S)) $ . A section $ \psi\in\Gamma(S) $ is called a spinor on N, and for a 1-form $ \omega $ we will denote Clifford multiplication by $ c(\omega)\psi=\omega\cdot\psi $ .

The metric g on N gives a Levi-Civita connection on $ F_{N} $ , on $ \tilde{F}_{N} $ , and on all associated vector bundles. The composition of the covariant derivative $ \nabla $ on $ \Gamma(S) $ with Clifford multiplication gives a first-order elliptic operator

$$\mathcal{D}: \Gamma(S) \overset{\nabla}{\rightarrow} \Gamma(T^{*}N \otimes S) \overset{c}{\rightarrow} \Gamma(S)$$

called the Dirac operator. If $ \{e_{i}\} $ is an orthonormal frame on $ U \subset N $ , and $ \{e^{i}\} $ the dual coframe, then on U

$$\mathcal{D}=\sum e^{i}\cdot\nabla_{e_{i}}.$$

---

The square of this operator satisfies the important formula of Lichnerowicz:

(A.2) $D^2 = \nabla^*\nabla + \frac{1}{4}S,$

where $\nabla^*\nabla\psi = -\psi_{,i}$ is the covariant Laplacian on spinors. It is this formula that Witten used in place of the Bochner formula (10.1).

To prove (A.2), choose $P \in M$ and an orthonormal frame $\{e_i\}$ with $\nabla e_i(P) = 0$. Since $e^i \cdot e^j \cdot + e^j \cdot e^i \cdot = -2\delta^{ij}$, at $P$ we have

$$D^2 = e^i \cdot e^j \cdot \nabla_i\nabla_j = \left(-\delta^{ij} + \frac{1}{2}\left[e^i \cdot, e^j \cdot\right]\right)\nabla_i\nabla_j$$

$$= \nabla^*\nabla + \frac{1}{2}e^i \cdot e^j \cdot\left[\nabla_i,\nabla_j\right].$$

At $P$, the curvature endomorphism $R(e_i,e_j) = [\nabla_i,\nabla_j]$ acts on 1-forms via the skew-symmetric matrix $R(e_i,e_j)_{kl} = R_{klij}$, so by (A.1) its action on spinors is

$$\bar{\rho}\left(R(e_i,e_j)\right)\psi = -\frac{1}{4}R_{klij}e^k \cdot e^l \cdot\psi.$$

Thus

$$D^2 = \nabla^*\nabla - \frac{1}{8}R_{klij}e^i \cdot e^j \cdot e^k \cdot e^l \cdot.$$

By the symmetries of the curvature tensor,

$$0 = \left(R_{klij} + R_{kijl} + R_{kjli}\right)e^i \cdot e^j \cdot e^k \cdot e^l \cdot$$

$$= 3R_{klij}e^i \cdot e^j \cdot e^k \cdot e^l \cdot -6R_{ij}e^i \cdot e^j \cdot$$

$$= 3R_{klij}e^i \cdot e^j \cdot e^k \cdot e^l \cdot +6S.$$

Then (A.2) follows.

Now suppose $N$ is asymptotically flat with metric $g_{ij} = \delta_{ij} + h_{ij}$, where $h_{ij} \in C^{2,\alpha}_{-\tau}(N)$, $\tau > (n-2)/2$. Orthonormalizing $\{dz^i\}$ yields an orthonormal coframe $e^i = dz^i + \frac{1}{2}h_{ik}dz^k + O(\rho^{-\tau-1})$. The connection coefficients of this frame are

$$\bar{\Gamma}^{k}_{ij} = -\left\langle \nabla_i e^k, e_j \right\rangle = \Gamma^{k}_{ij} - \frac{1}{2}\partial_i h_{jk} + O(\rho^{-2\tau-1})$$

$$= \frac{1}{2}\left(\partial_j g_{ik} - \partial_k g_{ij}\right) + O(\rho^{-2\tau-1}).$$

This orthonormal coframe induces a trivialization of $F_N$, and hence of the spin bundle $\tilde{F}_N$, over the asymptotic end $N_\infty$. With respect to this trivialization, the Dirac operator is (using (A.1) and the above formula)

(A.3) $$\psi = e^i \cdot \nabla_i\psi = e^i \cdot \partial_i\psi - \frac{1}{8}\left(\partial_k g_{ij}\right)e^i \cdot [e^j \cdot, e^k \cdot]\psi + O(\rho^{-2\tau-1})\psi.$$

The trivialization also enables us to define 'constant spinors' on $N_\infty$. Choose such a constant spinor $\psi_0$ with $|\psi_0| \to 1$ at infinity, and extend it to a smooth spinor on $N$. It follows from (A.3) that $$\dot{D}^2\psi_0 \in C^{0,\alpha}_{-\tau-2}(N).$$ Now note that $S \geqslant 0$ implies that

(A.4) $$\dot{D}^2: C^{2,\alpha}_{-\tau}(N) \to C^{0,\alpha}_{-\tau-2}(N)$$

is injective. Indeed, suppose $$\dot{D}^2\xi = 0$$ for some $\xi \in C^{2,\alpha}_{-\tau}(N)$. Then $\xi = O(\rho^{-\tau})$ and $\nabla\xi = O(\rho^{-\tau-1})$. Applying (A.2) to $\xi$ and integrating by parts we see that the boundary terms vanish, leaving

$$0 = \int_N \left\langle \xi, \dot{D}^2\xi \right\rangle dV_g = \int_N |\nabla\xi|^2 + \frac{1}{4}S|\xi|^2 dV_g.$$

---

Since $S \geqslant 0$ this shows that $\nabla\xi = 0$, so $\nabla|\xi|^2 = \langle\nabla\xi, \xi\rangle + \langle\xi, \nabla\xi\rangle = 0$. Thus $|\xi|$ is a constant, which is zero since $\xi$ vanishes at infinity.

Theorem 9.2(d) also holds for the operator $\nabla^*\nabla$ acting on spinors (with essentially the same proof). Therefore (A.4) is an isomorphism, so there exists $\xi \in C_{-\tau}^{2,\alpha}(N)$ with $\dot{\mathcal{B}}^2\xi = \dot{\mathcal{B}}^2\psi_0$. The spinor $\psi = \psi_0 - \xi$ then satisfies $\dot{\mathcal{B}}^2\psi = 0$. Furthermore, $\varphi = \dot{\mathcal{B}}\psi = \dot{\mathcal{B}}\psi_0 - \dot{\mathcal{B}}\xi$ satisfies $\dot{\mathcal{B}}\varphi = 0$ and lies in $C_{-\tau-1}^{1,\alpha}(N)$, so integrating by parts as above shows that $\varphi \equiv 0$. We have thus obtained a spinor $\psi$ which is asymptotic to $\psi_0$ and satisfies $\dot{\mathcal{B}}\psi = 0$.

Now apply (A.2) to $\psi$ and integrate by parts over the region $N_R = \{$ $\rho \leqslant R$ \}. This time there is a boundary term:

(A.5) $$\int_{N_R} |\nabla\psi|^2 + \frac{1}{4} S |\psi|^2 dV_g = \text{Re}\int_{S_R} \langle\psi, \nabla_i\psi\rangle e_i \downarrow dV_g$$

$$= \text{Re}\int_{S_R} \left( \langle\psi_0, \nabla_i\psi_0 \rangle - \langle\psi_0, \nabla_i\xi\rangle - \langle\xi, \nabla_i\psi_0 \rangle + \langle\xi, \nabla_i\xi\rangle \right) e_i \downarrow dV_g.$$

As in (A.3) we have

$$\text{Re}\langle\psi_0, \nabla_i\psi_0 \rangle = -\frac{1}{8} \text{Re}\left(\partial_k g_{ij}\right)\langle\psi_0, [e^j \cdot, e^k \cdot]\psi_0 \rangle + O\left(\rho^{-2\tau-1}\right).$$

Since $[e^j \cdot, e^k \cdot]$ is skew-Hermitian, this is $O(\rho^{-2\tau-1})$ and so the first term in (A.5) vanishes as $R \to \infty$. Furthermore, since $\xi = O(\rho^{-\tau})$, $\nabla\xi = O(\rho^{-\tau-1})$, and $\nabla\psi_0 = O(\rho^{-\tau-1})$, the third and fourth terms also vanish.

To analyze the remaining term, let $L_i$ denote the operator

$$L_i = \nabla_i + e^i \cdot \dot{\mathcal{B}} = \left(\delta_{ij} + e^i \cdot e^j \cdot\right) \nabla_j = \frac{1}{2}[e^i \cdot, e^j \cdot] \nabla_j.$$

If $\alpha$ is the $(n-2)$-form $\alpha = \langle[e^i \cdot, e^j \cdot]\psi_0, \xi\rangle e_i \downarrow e_j \downarrow dV_g$, then

$$d\alpha = -2 \left( \langle[e^i \cdot, e^j \cdot]\nabla_j\psi_0, \xi\rangle + \langle[e^i \cdot, e^j \cdot]\psi_0, \nabla_j\xi\rangle \right) e_i \downarrow dV_g$$

$$= -4 \left( \langle L_i\psi_0, \xi\rangle - \langle\psi_0, L_i\xi\rangle \right) e_i \downarrow dV_g.$$

Therefore, by Stokes' theorem and the fact that $\dot{\mathcal{B}}\xi = \dot{\mathcal{B}}\psi_0$, the second term in (A.5) is

(A.6) $$\text{Re}\int_{S_R} \langle\psi_0, \left(e^i \cdot \dot{\mathcal{B}} - L_i\right)\xi\rangle e_i \downarrow dV_g$$

$$= \text{Re}\int_{S_R} \left( \langle\psi_0, e^i \cdot \dot{\mathcal{B}}\psi_0 \rangle - \langle L_i\psi_0, \xi\rangle \right) e_i \downarrow dV_g.$$

As before, $\langle L_i\psi_0, \xi\rangle = O(\rho^{-2\tau-1})$, while (A.3) gives

$$e^i \cdot \dot{\mathcal{B}}\psi_0 = -\frac{1}{8} \left(\partial_k g_{ij} + O(\rho^{-2\tau-1})\right) e^i \cdot e^j \cdot [e^j \cdot, e^k \cdot]\psi_0$$

$$= -\frac{1}{4} \left(\partial_k g_{ij} + O(\rho^{-2\tau-1})\right) e^i \cdot e^j \cdot (\delta^{jk} + e^j \cdot e^k \cdot)\psi_0$$

$$= -\frac{1}{4} \left(\partial_j g_{kj} - \partial_k g_{jj} + O(\rho^{-2\tau-1})\right) e^i \cdot e^k \cdot\psi_0.$$

Writing $e^i \cdot e^k \cdot = \frac{1}{2}[e^i \cdot e^k \cdot] - \delta^{ik}$ and noting that $[e^i \cdot, e^k \cdot]$ is skew, we see that (A.6) becomes

$$\frac{1}{4} \int_{S_R} \left(\partial_j g_{ij} - \partial_i g_{jj} + O(\rho^{-2\tau-1})\right)|\psi_0|^2 e_i \downarrow dV_g.$$

---

Putting this into (A.5) and letting $R \rightarrow \infty$ gives Witten's formula

$$\int_N |\nabla \psi|^2 + \frac{1}{4} S|\psi|^2 dV_g = \frac{\omega}{4} m(g).$$

The theorem follows immediately. □

We remark that with a little more work the weighted Hölder spaces can be replaced by weighted Sobolev spaces in the above proof, and one need only assume that $g$ is asymptotically flat of order $\tau > (n-2)/2$ and has finite mass.

## BIBLIOGRAPHY

[ADM1] R. Arnowitt, S. Deser, and C. Misner, Canonical variables for general relativity, Phys. Rev. 117 (1960), 1595–1602.

[ADM2] _____, Energy and the criteria for radiation in general relativity, Phys. Rev. 118 (1960), 1100–1104.

[ADM3] _____, Coordinate invariance and energy expressions in general relativity, Phys. Rev. 122 (1961), 997–1006.

[A1] T. Aubin, Problèmes isopérimétriques et espaces de Sobolev, J. Diff. Geom. 11 (1976), 533–598.

[A2] _____, Équations différentielles non linéaires et problème de Yamabe concernant la courbure scalaire, J. Math. Pures Appl. 55 (1976), 269–296.

[A3] _____, Nonlinear analysis on manifolds. Monge-Ampère equations, Springer-Verlag, New York, 1982.

[AM] P. Aviles and R. McOwen, Conformal deformation to constant negative scalar curvature on noncompact Riemannian manifolds, preprint.

[B] R. Bartnik, The mass of an asymptotically flat manifold, Comm. Pure Appl. Math. 34 (1986), 661–693.

[BL] H. Brezis and E. Lieb, A relation between pointwise convergence of functions and convergence of functionals, Proc. Amer. Math. Soc. 88 (1983), 486–490.

[BN] H. Brezis and L. Nirenberg, Positive solutions of nonlinear elliptic equations involving critical Sobolev exponents, Comm. Pure Appl. Math. 36 (1983), 437–477.

[C] M. Cantor, Elliptic operators and the decomposition of tensor fields, Bull. Amer. Math. Soc. (N.S.) 5 (1981), 235–262.

[CSCB] A. Chaljub-Simon and Y. Choquet-Bruhat, Problèmes elliptiques du second ordre sur une variété euclidienne à l'infini, Ann. Fac. Sci. Toulouse 1 (1978), 9–25.

[CBC] Y. Choquet-Bruhat and D. Christodoulou, Elliptic systems in $H_{s,8}$ spaces on manifolds which are Euclidean at infinity, Acta Math. 146 (1981), 129–150.

[E] L. Eisenhart, Riemannian geometry, Princeton University Press, Princeton, N. J., 1926.

[GHP] G. Gibbons, S. Hawking, and M. Perry, Path integrals and the indefiniteness of the gravitational action, Nucl. Phys. B138 (1978), 141–150.

[GT] D. Gilbarg and N. Trudinger, Elliptic partial differential equations of second order, Springer-Verlag, New York, 1983.

[G] R. Graham, A conformal normal form, in preparation.

[HE] S. Hawking and S. Ellis, The large scale structure of space-time, Cambridge University Press, Cambridge, 1973.

[JL1] D. Jerison and J. Lee, A subelliptic, nonlinear eigenvalue problem and scalar curvature on CR manifolds, Contemp. Math. 27 (1984), 57–63.

[JL2] _____, The Yamabe problem on CR manifolds, J. Diff. Geom. 25 (1987) (to appear).

[JL3] _____, Extremals for the Sobolev inequality on the Heisenberg group and the CR Yamabe problem, J. Amer. Math. Soc. 1 (1988) (to appear).

[JL4] _____, Intrinsic CR normal coordinates and the CR Yamabe problem, in preparation.

[K] J. Kazdan, Some applications of partial differential equations to problems in geometry, Surveys in Geometry, Japan, 1983 (preprint).

---

[KN] S. Kobayashi and N. Nomizu, Foundations of differential geometry. I, Interscience, New York, 1963.

[L] P.-L. Lions, Applications de la méthode de concentration-compacité à l’existence de fonctions extremales, C. R. Acad. Sci. Paris 296 (1983), 645–648.

[Lo] R. Lockhart, Fredholm properties of a class of elliptic operators on non-compact manifolds, Duke Math. J. 48 (1981), 289–312.

[M] R. McOwen, Behavior of the Laplacian on weighted Sobolev spaces, Comm. Pure Appl. Math. 32 (1979), 783–795.

[NW] L. Nirenberg and H. Walker, The null spaces of elliptic partial differential operators in $R^n$, J. Math. Anal. Appl. 42 (1973), 271–301.

[O] M. Obata, The conjectures on conformal transformations of Riemannian manifolds, J. Diff. Geom. 6 (1971), 247–258.

[PR] T. Parker and S. Rosenberg, Invariants of conformal Laplacians, J. Diff. Geom., to appear.

[PT] T. Parker and C. Taubes, On Witten’s proof of the positive energy theorem, Comm. Math. Phys. 84 (1982), 223–238.

[SU] J. Sacks and K. Uhlenbeck, The existence of minimal 2-spheres, Ann. of Math. 113 (1981), 1–24.

[S] R. Schoen, Conformal deformation of a Riemannian metric to constant scalar curvature, J. Diff. Geom. 20 (1984), 479–495.

[SY1] R. Schoen and S.-T. Yau, On the proof of the positive mass conjecture in general relativity, Comm. Math. Phys. 65 (1979), 45–76.

[SY2] _____, Proof of the positive action conjecture in quantum relativity, Phys. Rev. Lett. 42 (1979), 547–548.

[SY3] _____, The energy and the linear momentum of space-times in general relativity, Comm. Math. Phys. 79 (1981), 47–51.

[SY4] _____, Proof of the positive mass theorem. II, Comm. Math. Phys. 79 (1981), 231–260.

[SY5] _____, The geometry and topology of manifolds of positive scalar curvature, in preparation.

[SY6] _____, Conformally flat manifolds, Kleinian groups and scalar curvature (preprint).

[Ta] G. Talenti, Best constant in Sobolev inequality, Ann. Mat. Pura Appl. 110 (1976), 353–372.

[T] N. Trudinger, Remarks concerning the conformal deformation of Riemannian structures on compact manifolds, Ann. Scuola Norm. Sup. Pisa 22 (1968), 265–274.

[We] S. Webster, Pseudohermitian structures on a real hypersurface, J. Diff. Geom. 13 (1978), 25–41.

[Wy] D. Weiyue, On a conformally invariant elliptic equation on $R^n$, Comm. Math. Phys. 107 (1986), 331–335.

[W] E. Witten, A new proof of the positive energy theorem, Comm. Math. Phys. 80 (1981), 381–402.

[Y] H. Yamabe, On a deformation of Riemannian structures on compact manifolds, Osaka Math. J. 12 (1960), 21–37.

[Yau] S.-T. Yau, Problem section, Seminar on Differential Geometry (S.-T. Yau, ed.), Princeton University Press, Princeton, N. J., 1982.

DEPARTMENT OF MATHEMATICS, HARVARD UNIVERSITY, CAMBRIDGE, MASSACHUSETTS 02138

DEPARTMENT OF MATHEMATICS, BRANDEIS UNIVERSITY, WALTHAM, MASSACHUSETTS 02254

---


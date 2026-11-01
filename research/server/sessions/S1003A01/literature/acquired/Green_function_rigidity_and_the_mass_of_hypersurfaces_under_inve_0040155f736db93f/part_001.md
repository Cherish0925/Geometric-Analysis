---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Green function rigidity and the mass of hypersurfaces under inversion]

---
source_file: 2501_15805.pdf
converter: mathpix
format: mmd
---

\title{
Green function rigidity and the mass of hypersurfaces under inversion
}

\author{
Xuezhang Chen,*, Jiaxue Gan ${ }^{\dagger}$ and Yalong Shi ${ }^{\ddagger}$ \\ ${ }^{* \dagger \ddagger}$ School of Mathematics \& IMS, Nanjing University, Nanjing 210093, P.R. China
}

\begin{abstract}
This is a sequel to [6]. We prove the Green function rigidity conjecture in [6] for conformal Laplacian in dimension $n \geq 3$. For the Paneitz operator, we prove the Green function rigidity conjecture when $n \neq 4 k+2, k \geq 2$. Important ingredients in our proof are the positive mass theorem and the positive energy theorem for Paneitz operator. As a byproduct, we also obtain a new formula for the ADM mass of an asymptotically flat hypersurface that allows for a non-entire graph.
\end{abstract}

MSC2020: 35J08, 53C18, 53C40, 53C21.

\section*{Contents}
1 Introduction ..... 1
2 Integrability of scalar curvature ..... 6
3 Adapted asymptotic coordinates and the ADM mass ..... 13
4 A new mass formula and GFRC for $P_{2}^{g}$ ..... 18
5 Positive energy theorem and GFRC for $P_{4}^{g}$ ..... 23
A A generalization of Reilly formula for entire graphs ..... 29
B Mass of Green function for Paneitz operator and $\mathrm{m}_{4}$ ..... 29

\section*{1 Introduction}

A complete Riemannian manifold ( $N^{n}, g$ ) is called asymptotically flat of asymptotic order $\tau>0$ and regularity order $\ell \in \mathbb{N}$, if there exists a compact set $K \subset N$ such that $N \backslash K$ is diffeomorphic to $\mathbb{R}^{n} \backslash B_{R}(0)$ for some $R>0$, and under this coordinate chart, $g-\delta \in$

\footnotetext{
*X. Chen and J. Gan are partially supported by NSFC (No.11771204). Email: xuezhangchen@nju.edu.cn.
${ }^{\dagger}$ J. Gan's email: 602025210004@smail.nju.edu.cn.
${ }^{\ddagger}$ Y. Shi is partially supported by NSFC (No.12371058). Email:shiy1@nju.edu.cn.
}
$O_{\ell}\left(|y|^{-\tau}\right)$ as $|y| \rightarrow \infty$. The coordinates $y$ are called asymptotic coordinates. Here, $g-\delta \in$ $O_{\ell}\left(|y|^{-\tau}\right)$ means that
$$\left|\partial^{k}\left(g_{\alpha \beta}-\delta_{\alpha \beta}\right)\right|=O\left(|y|^{-\tau-k}\right), \quad \forall 0 \leq k \leq \ell .$$
In the literature, the regularity order $\ell$ is usually chosen to be 2. Accordingly, when we go to study the fourth order energy for the Paneitz operator, the regularity order requires to be 4.

The ADM mass of an asymptotically flat (AF) manifold $\left(N^{n}, g\right)$ was defined by Arnowitt-Deser-Misner [1] in the 1960s in the context of general relativity:
$$m(g):=\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}} g^{\beta \gamma}\left(\partial_{\gamma} g_{\alpha \beta}-\partial_{\alpha} g_{\beta \gamma}\right) v^{\alpha} \mathrm{d} \sigma$$
if the limit exists. Here, $v$ is the outward unit normal vector field on the sphere $\mathbb{S}_{t}^{n-1}:=$ $\{|y|=t\}$ with respect to the Euclidean metric. In [3], Bartnik proved that when the asymptotic order $\tau>\frac{n-2}{2}$, regularity order $\ell=2$ and the scalar curvature is integrable, the mass for AF manifold is independent of the choice of asymptotic coordinates and is thus a geometric invariant for $(N, g)$. See Lee-Parker [18] for a good introduction to the basics of ADM mass.

In [27, 26], R. Schoen and S.T. Yau proved the Positive Mass Theorem (PMT): Assume that $\left(N^{n}, g\right), 3 \leq n \leq 7$ is an asymptotically flat manifold of asymptotic order $\tau>\frac{n-2}{2}$ (regularity order at least 2 ), and $0 \leq R_{g} \in L^{1}(N, g)$. Then the mass $m(g) \geq 0$, with equality if and only if $(N, g)$ is isometric to the flat $\mathbb{R}^{n}$.

When $N$ is a spin manifold, an alternative proof is given by E. Witten [29] in dimension 3 (see also [23]), which works for all dimension under the spin assumption, see [3].

The Positive Mass Theorem plays an important role in the study of first and third named authors [6] of the Green function for the conformal Laplacian on closed Euclidean hypersurfaces. Based on the belief that the explicit representation formula of the Green function for certain conformally invariant linear (pseudo-)differential operator should determine the geometry and topology of the manifold, the authors [6] raised the following Green Function Rigidity Conjecture (GFRC).

Conjecture. Let $M^{n} \subset \mathbb{R}^{n+1}$ be a closed embedded hypersurface with induced metric $g$. Assume that for some $k \in \mathbb{Z}_{+}$, the Green function $G$ for the GJMS operator $P_{2 k}^{g}$ exists. Suppose one of the following conditions holds:
\begin{itemize}
\item[(1)] $2 k=n$ and for some $Q \in M, G(\cdot, Q)$ is of the form $-c_{n} \log \|\cdot-Q\|+c$, where $c \in \mathbb{R}$ and $c_{n}=\frac{2}{(n-1)!\left|\mathbb{S}^{n}\right|}$;
\item[(2)] $2 k<n$ or $2 k>n$ when $n$ is odd, and for some $Q \in M, G(\cdot, Q)$ is of the form $c_{n, k}\|\cdot-Q\|^{2 k-n}$, where $c_{n, k}=\frac{\Gamma\left(\frac{n}{2}-k\right)}{2^{2 k} \pi^{\frac{n}{2}} \Gamma(k)}$.
\end{itemize}
Then $(M, g)$ is a round sphere. Here and throughout, let $\|\cdot\|$ denote the Euclidean norm.
Recall that the GJMS operator $P_{2 k}^{g}$ for $k \in \mathbb{Z}_{+}$on a Riemannian manifold $\left(M^{n}, g\right)$ is a conformally invariant linear differential operator whose principal part agrees with $\left(-\Delta_{g}\right)^{k}$,
named after Graham, Jenne, Mason and Sparling [8]. When $k=1, P_{2}^{g}$ is precisely the conformal Laplacian:
$$P_{2}^{g}=-\Delta_{g}+\frac{n-2}{4(n-1)} R_{g}, \quad n \geq 2 .$$
When $n=2$, it reduces to the Laplacian.
The operator $P_{4}^{g}$ was discovered earlier by Paneitz [21] in 1983 on a smooth Riemmanian manifold ( $\left.M^{n}, g\right), n \geq 3$, and hence also referred to as 'Paneitz operator':
$$P_{4}^{g}=\Delta_{g}^{2}+\frac{4}{n-2} \operatorname{div}\left(\sum_{\alpha} \operatorname{Ric}\left(\nabla^{g} \cdot e_{\alpha}\right) e_{\alpha}\right)-\frac{n^{2}-4 n+8}{2(n-1)(n-2)} \operatorname{div}\left(R_{g} \nabla^{g} \cdot\right)+\frac{n-4}{2} Q_{g},$$
where $Q_{g}$ is Branson's $Q$-curvature, defined by
$$Q_{g}=-\Delta_{g} \sigma_{1}\left(A_{g}\right)+4 \sigma_{2}\left(A_{g}\right)+\frac{n-4}{2} \sigma_{1}\left(A_{g}\right)^{2} .$$
Here
$$A_{g}=\frac{1}{n-2}\left(\operatorname{Ric}_{g}-\frac{R_{g}}{2(n-1)} g\right)$$
is the Schouten tensor and $\sigma_{k}\left(A_{g}\right)$ is the $k$-th elementary symmetric function of $g^{-1} A_{g}$.
For more about the GJMS operators and their applications, readers are referred to [4] for a recent survey.

For the conformal Laplacian and Paneitz operator, the authors [6] carried out the first step towards the above conjecture. For example, they proved that the pole $Q$ of Green function must be an umbilical point, and succeeded in verifying GFRC for the conformal Laplacian in dimensions $n=3,4,5$.

The proof of GFRC for the conformal Laplacian in [6] goes as follows. First, the familiar inverted coordinates happen to provide asymptotic coordinates of order 2 for $(M \backslash\{Q\}, \hat{g})$, where $\hat{g}=G(\cdot, Q)^{\frac{4}{n-2}} g$, such that when $n=3,4,5$, the mass for $(M \backslash\{Q\}, \hat{g})$ is well defined. Then a direct computation yields that the mass of $(M \backslash\{Q\}, \hat{g})$ vanishes. Since the scalar curvature of $\hat{g}$ is zero, the Positive Mass Theorem guarantees that $(M \backslash\{Q\}, \hat{g})$ is isometric to the flat Euclidean space. Observe that $\hat{g}=\left(c_{n, 2}\right)^{\frac{4}{n-2}}\|\cdot-Q\|^{-4} g$ is essentially the induced metric of $I_{Q}(M \backslash\{Q\}) \subset \mathbb{R}^{n+1}$, where
$$I_{Q}(z)=Q+\frac{z-Q}{\|z-Q\|^{2}}, \quad \forall z \in \mathbb{R}^{n+1} \backslash\{Q\}$$
is the inversion of $\mathbb{R}^{n+1}$ with respect to $Q$. Thus $I_{Q}(M \backslash\{Q\})$ is a complete flat hypersurface. Hartman-Nirenberg's theorem in [13] states that this hypersurface must be a generalized cylinder in $\mathbb{R}^{n+1}$. This gives an almost explicit parametrization of $I_{Q}(M \backslash\{Q\})$, hence also of $M \backslash\{Q\}$. Combining this with the fact that $Q$ is umbilical forces such a generalized cylinder to be a hyperplane. Hence, $(M, g)$ is a round sphere.

In this paper, we extend the above result to all dimensions $n \geq 3$.
Theorem 1. GFRC is true for the conformal Laplacian in all dimensions $n \geq 3$.

Very recently, Lai and Zhang [16] proved the $\boldsymbol{G F R C}$ for the Laplacian on surfaces using a different approach. Hence, the $\boldsymbol{G} \boldsymbol{F} \boldsymbol{R} \boldsymbol{C}$ is now completely resolved for $P_{2}^{g}$ in all dimensions $n \geq 2$.

The general strategy for proving Theorem 1 is similar to that of [6]. However, there are serious difficulties in higher dimensions.
\begin{itemize}
\item[-] We need to construct asymptotic coordinate system for all dimensions of order $\tau>\frac{n-2}{2}$. The inversion of the usual geodesic normal coordinate is far from enough.
\item[-] Accordingly, to prove the vanishing of mass, we need much more computations even though following the same strategy. Some exceptional phenomenon occurs in dimensions $n=4 k, k \geq 2$.
\end{itemize}

The key idea for solving these problems is to study the contact order of $M$ with its osculating sphere at $Q$, with which we construct the adapted asymptotic coordinate system for all dimensions. Here for an umbilical point $Q$ of $M$ with principal curvature $\lambda$, the osculating sphere of $M$ at $Q$ is the sphere of radius $\frac{1}{|\lambda|}$ that tangent to $M$ at $Q$ with the same outer normal vector. To this end, we are able to prove a general theorem for hypersurfaces, which should be of independent interest.

Theorem 2. Let $M^{n}, n \geq 3$ be a closed embedded hypersurface of $\mathbb{R}^{n+1}$ with induced metric $g$. Assume that $Q \in M$ is umbilical. Write $\rho:=\|\cdot-Q\|^{2}$, and set $\hat{g}:=\rho^{-2} g$. Then the following are true.
\begin{itemize}
\item[(1)] If $n=3,4,5$, then $R_{\hat{g}} \in L^{1}(M, \hat{g})$;
\item[(2)] if $n \geq 6$ and $R_{\hat{g}} \in L^{1}(M \backslash\{Q\}, \hat{g})$, or $n=3,4,5$, then there exists an asymptotic coordinate system such that when $4 \nmid n,(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order $\left\lfloor\frac{n}{2}\right\rfloor+1$; when $4 \mid n,(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order $\frac{n}{2}$.
\end{itemize}
Furthermore, the ADM mass $m(\hat{g})$ of $(M \backslash\{Q\}, \hat{g})$ is non-negative, and $m(\hat{g})=0$ except for $n=4 k, k \geq 2$.

Remark 1. The integrability of $R_{\hat{g}}$ ensures that the contact order of $M$ with its osculating sphere at $Q$ is at least $\left\lfloor\frac{n}{2}\right\rfloor+1$ (resp. $\frac{n}{2}$ ) when $4 \nmid n$ (resp. $4 \mid n$ ). As we shall show, similar phenomena also occur for the $Q$-curvature.

Remark 2. When $n=4 k, k \geq 2$, there are indeed examples whose mass is strictly positive under the same assumptions of Theorem 2 see Example 1

Thanks to Theorem 2, the same argument of [6] applies to establish Theorem 1 when $4 \nmid n$. However, to cope with the $4 \mid n$ case, a direct consequence of Example 1 is that the local analysis in the proof of Theorem 2 fails. At this point, we instead need a new mass formula for asymptotically flat hypersurfaces, which was once discovered by Lam in his thesis [17] for entire graphs.

Theorem 3. Let $N$ be a complete non-compact hypersurface in $\mathbb{R}^{n+1}$ with induced metric $g$. Assume that there is a compact subset $K \subset N$ such that $N \backslash K$ is the graph of a smooth function $\psi: \mathbb{R}^{n} \backslash B_{R}(0) \rightarrow \mathbb{R}$, satisfying
$$\left|\partial_{\alpha} \psi\right|+\left|y \| \partial_{\alpha \beta}^{2} \psi\right|+|y|^{2}\left|\partial_{\alpha \beta \gamma}^{3} \psi\right|=O\left(|y|^{-\frac{\tau}{2}}\right),$$
with $\tau>\frac{n-2}{2}$. Then there is a global tangent vector field $X$ on $N$ such that $\operatorname{div}_{g} X=$ $\left\langle e_{n+1}, \mathbf{n}\right\rangle R_{g}$ where $\mathbf{n}$ is the unit normal vector field of $N$ such that $\left\langle e_{n+1}, \mathbf{n}\right\rangle>0$ on the end $N \backslash K$ for $|y| \gg 1$, and that
$$m(g)=\frac{1}{\left|\mathbb{S}^{n-1}\right|} \int_{N} \operatorname{div}_{g} X \mathrm{~d} V_{g}=\frac{1}{\left|\mathbb{S}^{n-1}\right|} \int_{N}\left\langle e_{n+1}, \mathbf{n}\right\rangle R_{g} \mathrm{~d} V_{g} .$$
In particular, if $R_{g} \equiv 0$, then $m(g)=0$.
Since the metric $\hat{g}$ in the proof of Theorem 1 has zero scalar curvature, the above theorem in fact implies that the mass automatically vanishes. Hence, this concludes the proof of Theorem 1 using the same strategy as in [6].

We proceed to study the $\boldsymbol{G} \boldsymbol{F} \boldsymbol{R} \boldsymbol{C}$ for the Paneitz operator $P_{4}^{g}$. In parallel to Theorem 1, the $Q$-curvature version of the positive energy theorem in [9, 10, 11, 2] plays a key role.

In the past decade, some great advances have been made in the constant $Q$-curvature problem on a closed manifold $\left(M^{n}, g\right)$. For $n \geq 5 \mathrm{M}$. Gursky and A. Malchiodi [9] proposed a sufficient condition of $\operatorname{ker} P_{4}^{g}=\{0\}$ that $R_{g} \geq 0$ and $Q_{g} \succcurlyeq 0$, which leads to the existence of conformal metrics with positive constant $Q$-curvature. Subsequently, Hang and Yang [12, Proposition 1.1] improved the sufficient condition to the hypothesis that $Y(M,[g])>0$ and $Q_{g} \not \geq 0$. The most general existence result for $P_{4}^{g}$ and $n \geq 6$ was proved by Gursky, Hang and Lin [7]. For $n=3$, Hang and Yang [11] proved a PMT theorem associated to the Paneitz operator.

In a recent paper [2], on an asymptotically flat manifold ( $N^{n}, g$ ), $n \geq 5$ of order $\tau>\frac{n-4}{2}$ and regularity order $\ell=4$, R. Avalos, P. Laurain and J. Lira introduced a fourth-order mass (called "energy" by the authors) by
$$\mathrm{m}_{4}(g)=\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}}\left(\partial_{\beta} \partial_{\gamma} \partial_{\gamma} g_{\alpha \alpha}-\partial_{\beta} \partial_{\gamma} \partial_{\alpha} g_{\alpha \gamma}\right) v^{\beta} \mathrm{d} \sigma_{\mathbb{S}_{t}^{n-1}},$$
which had been defined earlier by B. Michel [20] for higher-order GJMS operators. Furthermore, the authors [2] established a positive energy theorem; see Section 5 for precise statement.

Next we establish a $Q$-curvature analogue to Theorem 2.
Theorem 4. Let $M^{n}, n \geq 5$ be a closed embedded hypersurface of $\mathbb{R}^{n+1}$ with induced metric $g$. Assume that $Q \in M$ is umbilical. Write $\rho:=\|\cdot-Q\|^{2}$ and set $\hat{g}:=\rho^{-2} g$. Then the following are true.
\begin{itemize}
\item[(1)] If $n=5,6,7$, then $Q_{\hat{g}} \in L^{1}(M, \hat{g})$, and $(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order 3;
\item[(2)] if $n \geq 8$ and $Q_{\hat{g}} \in L^{1}(M \backslash\{Q\}, \hat{g})$, there exists an asymptotic coordinate system such that when when $n \neq 4 j+2, j \geq 2,(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order $\left\lfloor\frac{n}{2}\right\rfloor$; when $n=4 j+2, j \geq 2,(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order $\frac{n}{2}-1$.
\end{itemize}
Furthermore, the fourth-order energy $\mathrm{m}_{4}(\hat{g})$ of $(M \backslash\{Q\}, \hat{g})$ is nonnegative, and $\mathrm{m}_{4}(\hat{g})=0$ except for $n=4 j+2, j \geq 2$.

Using the same strategy as the conformal Laplacian case, we make elaborate efforts to establish the following Green function rigidity for the Paneitz operator.

Theorem 5. For $n \geq 5$ and $n \neq 4 j+2, j \geq 2$, let $\left(M^{n}, g\right)$ be a closed embedded hypersurface in $\mathbb{R}^{n+1}$ such that the Yamabe constant $Y(M,[g])>0$. Then $\boldsymbol{G F R C}$ is true for the Paneitz operator $P_{4}^{g}$. When $n=3$, under the same assumption, $\left(M^{3}, g\right)$ is globally conformal to $\mathbb{S}^{3}$.

At present, we have to exclude the case $n=4 j+2, j \geq 2$ in the statement of Theorem 5, since the vanishing of $\mathrm{m}_{4}(\hat{g})$ in such dimensions remains open. As in Theorem 1, a global analysis together with the fact $Q_{\hat{g}}=0$ should come into play. It is interesting to know whether we can find a nice formula for $\mathrm{m}_{4}$ similar to that of Theorem 3 . Moreover, the $n=3,4$ cases differ significantly from other cases and need to be further explored.

In the next section, we describe the relationship between the integrability of $R_{\hat{g}}$ and the contact order of $M$ with its osculating sphere at an umbilical point $Q$. This is crucial for subsequent discussions. Then in Section 3, we first prove Theorem 2 by introducing the adapted asymptotic coordinates, and derive the mass formula in Theorem 3 for asymptotically flat hypersurfaces those are graphs outside a compact subset. Combining ideas from [6], we prove Theorem 1. Finally, similar ideas apply to prove Theorems 45 for the Paneitz operator, and such proofs occupy Sections 4, 5] There are two appendices, those should be of independent interest. The first one is an application of our method of proving Theorem 3: we generalize a formula of Reilly for graphs to general Euclidean hypersurfaces. The second one is an elementary and simplified proof of the known fact (cf. [2]) that the mass of Green function for the Paneitz operator in [9, 10] is a constant multiple of $\mathrm{m}_{4}(\hat{\mathrm{~g}})$.

\section*{2 Integrability of scalar curvature}

Let $M$ be an embedded hypersurface in $\mathbb{R}^{n+1}$ with induced metric $g$, and $Q \in M$ be an umbilical point. Without loss of generality, we may assume $Q=0 \in \mathbb{R}^{n+1}$. Define $\rho:=\|P-Q\|^{2}=\langle\mathbf{r}, \mathbf{r}\rangle$, and $\eta:=\langle\mathbf{r}, \mathbf{n}\rangle$, where $\mathbf{r}$ is the position vector of $M$ in $\mathbb{R}^{n+1}$ and $\mathbf{n}$ is the inward unit normal vector field. Given any point $P \in M$, we choose an orthonormal frame of $M,\left\{e_{\alpha} ; 1 \leq \alpha \leq n\right\}$. Then we have $\nabla_{g} \rho=2 \sum_{\alpha}\left\langle\mathbf{r}, e_{\alpha}\right\rangle e_{\alpha}=2\left(\mathbf{r}-\mathbf{r}^{\perp}\right)=2 \mathbf{r}-2 \eta \mathbf{n}$ and consequently
$$\left|\nabla_{g} \rho\right|^{2}=\sum_{\alpha} 4\left\langle\mathbf{r}, e_{\alpha}\right\rangle^{2}=4\|\mathbf{r}\|^{2}-4\langle\mathbf{r}, \mathbf{n}\rangle^{2}=4 \rho-4 \eta^{2} .$$
Also, at $P$ we have
$$\nabla_{g}^{2} \rho\left(e_{\alpha}, e_{\beta}\right)=\left\langle\nabla_{e_{\alpha}}^{g}\left(\nabla_{g} \rho\right), e_{\beta}\right\rangle=2 \delta_{\alpha \beta}+2 \eta I I\left(e_{\alpha}, e_{\beta}\right),$$
where $I I\left(e_{\alpha}, e_{\beta}\right)=-\left\langle\nabla_{e_{\alpha}} \mathbf{n}, e_{\beta}\right\rangle$ is the second fundamental form. As a consequence,
$$\Delta_{g} \rho=2 n+2 \eta H .$$
To sum up, in any coordinate system we have
$$\left|\nabla_{g} \rho\right|^{2}=4 \rho-4 \eta^{2}, \quad \rho_{, \alpha \beta}=2 g_{\alpha \beta}+2 \eta h_{\alpha \beta}, \quad \Delta_{g} \rho=2 n+2 \eta H .$$

Locally $M$ is given as the graph of a smooth function $f: B_{\delta}(0) \rightarrow \mathbb{R}$ with $f(0)=0$ and $\nabla f(0)=0$. Here, $\nabla$ means the gradient with respect to the flat metric on $\mathbb{R}^{n}$. Then
under the coordinate chart $x=\left(x_{1}, \cdots, x_{n}\right)$, the induced metric on $M$ is $g_{\alpha \beta}=\delta_{\alpha \beta}+f_{\alpha} f_{\beta}$, where $f_{\alpha}$ means $\frac{\partial f}{\partial x_{\alpha}}$. It is straightforward that $\rho=|x|^{2}+f^{2}(x)$ and
$$\eta=\frac{f-x \cdot \nabla f}{\sqrt{1+|\nabla f|^{2}}} .$$
Also, it is direct to check that the second fundamental form is
$$I I=\sum_{\alpha, \beta} h_{\alpha \beta} \mathrm{d} x_{\alpha} \otimes \mathrm{d} x_{\beta}=\frac{1}{\sqrt{1+|\nabla f|^{2}}} \sum_{\alpha, \beta} f_{\alpha \beta} \mathrm{d} x_{\alpha} \otimes \mathrm{d} x_{\beta}$$
and the mean curvature is
$$H=\operatorname{tr}_{g}(I I)=\frac{1}{\sqrt{1+|\nabla f|^{2}}} g^{\alpha \beta} f_{\alpha \beta} .$$
At $Q$, we have
$$g_{\alpha \beta}=\delta_{\alpha \beta}, \quad \Gamma_{\alpha \beta}^{\gamma}=0, \quad h_{\alpha \beta}=f_{\alpha \beta}(0), \quad \text { and } \quad H=\Delta f(0),$$
where $\Delta$ denotes the Euclidean Laplacian. In the following, $\left(x_{1}, \cdots, x_{n}\right)$ will always be the above graph coordinate system.

It is well known that if the order $\tau$ of an asymptotically flat $n$-manifold is $>\frac{n-2}{2}$, and the scalar curvature is $L^{1}$, then the ADM mass is well defined and independent of the asymptotic coordinates (cf. [3]). Now we are ready to study the integrability of the scalar curvature. Since the integral of the scalar curvature is geometric and then coordinate free, we prefer to work under the coordinate system $x=\left(x_{1}, \cdots, x_{n}\right)$.

Under the conformal change of metric $\hat{g}:=\rho^{-2} g$, the scalar curvature transforms by
$$\begin{aligned}
R_{\hat{g}} & =\rho^{2}\left(R_{g}+2(n-1) \frac{\Delta_{g} \rho}{\rho}-n(n-1) \frac{\left|\nabla^{g} \rho\right|^{2}}{\rho^{2}}\right) \\
& =\rho^{2}\left(R_{g}+4(n-1) H \frac{\eta}{\rho}+4 n(n-1) \frac{\eta^{2}}{\rho^{2}}\right)
\end{aligned}$$
where we used (2.1) in the last equality. Fix an umbilical point $Q \in M$. Then in a punctured neighborhood of $Q$, we have
$$R_{\hat{g}} \mathrm{~d} V_{\hat{g}}=\rho^{2-n}\left(R_{g}+4(n-1) H \frac{\eta}{\rho}+4 n(n-1) \frac{\eta^{2}}{\rho^{2}}\right) \mathrm{d} V_{g} .$$
Notice that $R_{g}=H^{2}-|I I|^{2}$ by Gauss equation. Clearing a common nonzero factor ( $1+$ $\left.|\nabla f|^{2}\right)^{-1}$ in (2.2), we only need to expand
$$\mathcal{R}:=4 n(n-1)\left(\frac{f-x \cdot \nabla f}{\rho}\right)^{2}+4(n-1) g^{\alpha \beta} f_{\alpha \beta} \frac{f-x \cdot \nabla f}{\rho}+\left(g^{\alpha \beta} f_{\alpha \beta}\right)^{2}-g^{\alpha \mu} g^{\beta v} f_{\alpha \beta} f_{\mu v}$$
around $Q$. For brevity, let $B$ denote a matrix $\left(B_{v}^{\alpha}\right)$ with the element $B_{v}^{\alpha}:=g^{\alpha \beta} f_{\beta v}$, then the above equation becomes
$$\mathcal{R}=4 n(n-1)\left(\frac{f-x \cdot \nabla f}{\rho}+\frac{1}{2 n} \operatorname{tr} B\right)^{2}-\operatorname{tr}\left(\dot{B}^{2}\right),$$
where $\stackrel{\circ}{B}_{v}^{\alpha}=B_{v}^{\alpha}-\frac{\operatorname{tr} B}{n} \delta_{v}^{\alpha}$ is the trace-free part of $B$.

Proposition 1. There hold $\mathcal{R}=O\left(|x|^{2}\right)$ and $R_{\hat{g}}=O\left(|x|^{6}\right)$ near $Q$.
Proof. From the assumption that $Q$ is umbilical, near $Q$ we write
$$f(x)=\frac{H(Q)}{2 n}|x|^{2}+A_{3}(x)+O\left(|x|^{4}\right),$$
where $A_{3}(x)$ denotes a homogeneous polynomial of degree 3. Set $r:=|x|, A_{3}(x)=r^{3} A_{3}(\theta)$ and $\Delta_{\theta}:=\Delta_{\mathbb{S}^{n-1}}$, where $\theta=x|x|^{-1} \in \mathbb{S}^{n-1}$. Short $H$ for $H(Q)$, and $A_{3}$ for $A_{3}(x)$. Then
$$x \cdot \nabla f=\frac{H}{n} r^{2}+3 A_{3}(\theta) r^{3}+O\left(r^{4}\right)$$
and thereby
$$f-x \cdot \nabla f=-\frac{H}{2 n} r^{2}-2 A_{3}(\theta) r^{3}+O\left(r^{4}\right) .$$
On the other hand, we have
$$\rho=|x|^{2}+f^{2}(x)=r^{2}\left(1+\frac{H^{2}}{4 n^{2}} r^{2}+O\left(r^{3}\right)\right) .$$
Putting the above two equations together yields
$$\frac{f-x \cdot \nabla f}{\rho}=-\frac{H}{2 n}-2 A_{3}(\theta) r+O\left(r^{2}\right) .$$

Observe that
$$\begin{aligned}
B_{\alpha}^{v} & =g^{\alpha \mu} f_{\mu v} \\
& =\left(\delta^{\alpha \mu}-\frac{f_{\alpha} f_{\mu}}{1+|\nabla f|^{2}}\right) f_{\mu v}=\left(\delta^{\alpha \mu}-f_{\alpha} f_{\mu}\right) f_{\mu v}+O\left(r^{3}\right) \\
& =\left(\delta^{\alpha \mu}-\frac{H^{2}}{n^{2}} x_{\alpha} x_{\mu}+O\left(r^{3}\right)\right) \cdot\left(\frac{H}{n} \delta_{\mu v}+\partial_{\mu v}^{2} A_{3}+O\left(r^{2}\right)\right)+O\left(r^{2}\right) \\
& =\frac{H}{n} \delta_{v}^{\alpha}+\partial_{\alpha v}^{2} A_{3}+O\left(r^{2}\right),
\end{aligned}$$
thereby
$$\stackrel{\circ}{B}_{\alpha}^{v}=\partial_{\alpha v}^{2} A_{3}-\frac{\Delta A_{3}}{n} \delta_{\alpha}^{v}$$
and
$$\begin{aligned}
\operatorname{tr} B=g^{\alpha \beta} f_{\alpha \beta} & =H+\Delta A_{3}+O\left(r^{2}\right) \\
& =H+\left(3(n+1) A_{3}(\theta)+\Delta_{\theta} A_{3}(\theta)\right) r+O\left(r^{2}\right) .
\end{aligned}$$
This follows that
$$\begin{gathered}
\operatorname{tr} \stackrel{\circ}{B}^{2}=\left|\nabla^{2} A_{3}\right|^{2}-\frac{\left(\Delta A_{3}\right)^{2}}{n}, \\
\left.\frac{f-x \cdot \nabla f}{\rho}+\frac{1}{2 n} \operatorname{tr} B=\left(-\frac{1}{2}+\frac{3}{2 n}\right) \Delta_{\theta} A_{3}(\theta)\right) r+O\left(r^{2}\right) .
\end{gathered}$$
Hence, we obtain $\mathcal{R}=O\left(r^{2}\right)$ and $R_{\hat{g}}=O\left(r^{6}\right)$ by (2.4) and (2.2). \(\square\)

Lemma 1. Suppose we have
$$R_{g}+4(n-1) H \frac{\eta}{\rho}+4 n(n-1) \frac{\eta^{2}}{\rho^{2}}=c(\theta)|x|^{k}+o\left(|x|^{k}\right),$$
with $c(\theta)$ not identically zero. Then $R_{\hat{g}} \in L^{1}(\hat{M}, \hat{g})$ if and only if $k>n-4$.
Proof. Since $\rho=|x|^{2}(1+o(1))$, if $k>n-4$, then we deduce from
$$\int_{B_{\delta}(0)}|x|^{2(2-n)+k} \mathrm{~d} x<\infty$$
that $R_{\hat{g}} \in L^{1}(\hat{M}, \hat{g})$.
On the other hand, assume that $R_{\hat{g}} \in L^{1}(\hat{M}, \hat{g})$ and $c\left(\theta_{0}\right) \neq 0$ for some $\theta_{0}$. Then we may choose a spherical neighborhood $U \subset \mathbb{S}^{n-1}$ of $\theta_{0}$, over which $|c(\theta)|$ has a positive lower bound $c_{0}>0$. Let $C_{U}$ be the corresponding cone in $\mathbb{R}^{n}$ emanating from the origin. Then for small $\delta>0$, by (2.3) we have
$$\rho^{-n}\left|R_{\hat{g}}\right| \geq \frac{c_{0}}{2}|x|^{2(2-n)+k}, \quad \forall x \in B_{\delta}(0) \cap C_{U} .$$
Consequently, we have $\int_{B_{\delta}(0) \cap C_{U}}|x|^{2(2-n)+k} \mathrm{~d} x<\infty$, and hence $2(2-n)+k>-n$. This means $k>n-4$. \(\square\)

Let $\lambda \in \mathbb{R}$ be the principal curvature of $M$ at $Q$, and define
$$\phi(x)=\frac{\lambda|x|^{2}}{1+\sqrt{1-\lambda^{2}|x|^{2}}}, \quad x \in B_{\frac{1}{|\lambda|}(0)} .$$
Then a direct calculation yields
$$\frac{\lambda}{2}\left(|x|^{2}+\phi^{2}\right)=\phi, \quad 1+|\nabla \phi|^{2}=\left(1-\lambda^{2}|x|^{2}\right)^{-1}, \quad \phi-x \cdot \nabla \phi=-\frac{\phi}{\sqrt{1-\lambda^{2}|x|^{2}}} .$$
It is convenient to use $\phi(x)=\lambda^{-1}\left(1-\sqrt{1-\lambda^{2}|x|^{2}}\right)$ for $\lambda \neq 0$. Note that the graph of $\phi$ is precisely the osculating sphere of $M$ at $Q$.

Proposition 2. If $R_{\hat{g}} \in L^{1}(\hat{M}, \hat{g})$, then near $Q$ we have
\begin{itemize}
\item[(i)] when $4 \nmid n, f(x)=\phi(x)+O\left(|x|^{\left\lfloor\frac{n}{2}\right\rfloor+1}\right)$;
\item[(ii)] when $\left.4|n, f(x)=\phi(x)+\kappa| x\right|^{\frac{n}{2}}+O\left(|x|^{\frac{n}{2}+1}\right), \kappa \in \mathbb{R}$.
\end{itemize}

To simplify the computation, we use the following formula for $\mathcal{R}$ :
$$\mathcal{R}=4 n(n-1)\left(\frac{f-x \cdot \nabla f}{\rho}+\frac{g^{\alpha \beta} f_{\alpha \beta}}{2 n}\right)^{2}+\frac{\left(g^{\alpha \beta} f_{\alpha \beta}\right)^{2}}{n}-g^{\alpha \mu} g^{\beta \nu} f_{\alpha \beta} f_{\mu \nu} .$$
As before, we denote by $B_{v}^{\alpha}:=g^{\alpha \beta} f_{\beta v}$ and its trace-free part $\stackrel{\circ}{B}_{v}^{\alpha}=B_{v}^{\alpha}-\frac{\operatorname{tr} B}{n} \delta_{v}^{\alpha}$. Then we have
$$\mathcal{R}=4 n(n-1)\left(\frac{f-x \cdot \nabla f}{\rho}+\frac{1}{2 n} \operatorname{tr} B\right)^{2}-\operatorname{tr}\left(\dot{B}^{2}\right) .$$

Proof of Proposition 2 Let $m=\left\lfloor\frac{n}{2}\right\rfloor$ be the integer part and $r=|x|$. Recall that $f(0)=$ $0, \nabla f(0)=0$. Suppose
$$f(x)-\phi(x)=A_{k}(x)+O\left(r^{k+1}\right)$$
for some $3 \leq k \leq m$, where $A_{k}$ is a homogeneous polynomial of degree $k$, we shall prove by induction that $A_{k}=0$ except when $4 \mid n$ and $k=m=\frac{n}{2}$. Short $A$ for $A_{k}$. Then we have
$$f(x)=\phi(x)+A(x)+O\left(r^{k+1}\right)$$
near $Q$.
Notice that
$$\begin{aligned}
f-x \cdot \nabla f & =\phi-x \cdot \nabla \phi+(A-x \cdot \nabla A)+O\left(r^{k+1}\right) \\
& =-\frac{\phi}{\sqrt{1-\lambda^{2} r^{2}}}+(A-x \cdot \nabla A)+O\left(r^{k+1}\right) \\
& =-\frac{\phi}{\sqrt{1-\lambda^{2} r^{2}}}-(k-1) A+O\left(r^{k+1}\right)
\end{aligned}$$
and
$$\begin{aligned}
\rho=r^{2}+f^{2} & =r^{2}+\phi^{2}+2 \phi A+O\left(r^{k+3}\right) \\
& =2 \lambda^{-1} \phi+2 \phi A+O\left(r^{k+3}\right) \\
& =2 \lambda^{-1} \phi\left(1+\lambda A+O\left(r^{k+1}\right)\right),
\end{aligned}$$
thereby
$$\rho^{-1}=\frac{\lambda}{2} \phi^{-1}\left(1-\lambda A+O\left(r^{k+1}\right)\right) .$$
Hence putting the above equations together yields
$$\frac{f-x \cdot \nabla f}{\rho}=-\frac{\lambda}{2} \frac{1}{\sqrt{1-\lambda^{2} r^{2}}}-\frac{(k-1) \lambda}{2} \phi^{-1} A+O\left(r^{k-1}\right) .$$

Observe that
$$1+|\nabla f|^{2}=1+|\nabla \phi|^{2}+O\left(r^{k}\right)=\frac{1}{1-\lambda^{2} r^{2}}\left(1+O\left(r^{k}\right)\right)$$
and then
$$\left(1+|\nabla f|^{2}\right)^{-1}=\left(1-\lambda^{2} r^{2}\right)\left(1+O\left(r^{k}\right)\right) .$$
Now we have
$$\begin{aligned}
g^{\alpha \beta} & =\delta^{\alpha \beta}-\frac{f_{\alpha} f_{\beta}}{1+|\nabla f|^{2}} \\
& =\delta^{\alpha \beta}-\left(\frac{\lambda x_{\alpha}}{\sqrt{1-\lambda^{2} r^{2}}}+O\left(r^{k-1}\right)\right)\left(\frac{\lambda x_{\beta}}{\sqrt{1-\lambda^{2} r^{2}}}+O\left(r^{k-1}\right)\right) \cdot\left(1-\lambda^{2} r^{2}\right)\left(1+O\left(r^{k}\right)\right) \\
& =\delta^{\alpha \beta}-\lambda^{2} x_{\alpha} x_{\beta}+O\left(r^{k}\right) .
\end{aligned}$$

This gives
$$\begin{aligned}
B_{v}^{\alpha}=g^{\alpha \beta} f_{\beta v} & =\left(\delta^{\alpha \beta}-\lambda^{2} x_{\alpha} x_{\beta}+O\left(r^{k}\right)\right) \cdot\left(\frac{\lambda \delta_{\beta v}}{\sqrt{1-\lambda^{2} r^{2}}}+\frac{\lambda^{3} x_{\beta} x_{v}}{\left(1-\lambda^{2} r^{2}\right)^{\frac{3}{2}}}+A_{\beta v}+O\left(r^{k-1}\right)\right) \\
& =\frac{\lambda \delta_{\alpha v}}{\sqrt{1-\lambda^{2} r^{2}}}+\frac{\lambda^{3} x_{\alpha} x_{v}}{\left(1-\lambda^{2} r^{2}\right)^{\frac{3}{2}}}+A_{\alpha v}-\frac{\lambda^{3} x_{\alpha} x_{v}}{\sqrt{1-\lambda^{2} r^{2}}}-\frac{\lambda^{5} r^{2} x_{\alpha} x_{v}}{\left(1-\lambda^{2} r^{2}\right)^{\frac{3}{2}}}+O\left(r^{k-1}\right) \\
& =\frac{\lambda \delta_{\alpha v}}{\sqrt{1-\lambda^{2} r^{2}}}+A_{\alpha v}+O\left(r^{k-1}\right) .
\end{aligned}$$
Hence,
$$\operatorname{tr} B=g^{\alpha \beta} f_{\alpha \beta}=\frac{n \lambda}{\sqrt{1-\lambda^{2} r^{2}}}+\Delta A+O\left(r^{k-1}\right)$$
and then
$$\stackrel{\circ}{B}_{v}^{\alpha}=A_{\alpha v}-\frac{\Delta A}{n} \delta_{\alpha v}+O\left(r^{k-1}\right) .$$
Notice that $\frac{\lambda}{2} \phi^{-1}=r^{-2}+O(1)$. Combining (2.7) and (2.8) yields
$$\begin{aligned}
4 n(n-1)\left(\frac{f-x \cdot \nabla f}{\rho}+\frac{\operatorname{tr} B}{2 n}\right)^{2} & =4 n(n-1)\left(\frac{\Delta A}{2 n}-\frac{(k-1) A}{r^{2}}+O\left(r^{k-1}\right)\right)^{2} \\
& =4 n(n-1)\left(\frac{\Delta A}{2 n}-\frac{(k-1) A}{r^{2}}\right)^{2}+O\left(r^{2 k-3}\right) .
\end{aligned}$$
Moreover, by (2.9) we have
$$\operatorname{tr}\left(\dot{B}^{2}\right)=\left|\nabla^{2} A\right|^{2}-\frac{(\Delta A)^{2}}{n}+O\left(r^{2 k-3}\right) .$$
Therefore, combining (2.10) and (2.11) we obtain
$$\mathcal{R}=4 n(n-1)(k-1)^{2} \frac{A^{2}}{r^{4}}-4(n-1)(k-1) \frac{A}{r^{2}} \Delta A+(\Delta A)^{2}-\left|\nabla^{2} A\right|^{2}+O\left(r^{2 k-3}\right) .$$
Since $\mathcal{R}=O\left(r^{n-3}\right)$, when $k \leq m$ we have
$$4 n(n-1)(k-1)^{2} A^{2}-4(n-1)(k-1) r^{2} A \Delta A+r^{4}\left[(\Delta A)^{2}-\left|\nabla^{2} A\right|^{2}\right]=0 .$$

Lemma 2. If $A=A_{k}$ satisfies (2.13) for $2 k<n$, then $A \equiv 0$.
Proof. In terms of polar coordinates, (2.13) is equivalent to
$$\begin{array}{r}
(n-1)(k-2)^{2}(n-2 k) A^{2}(\theta)-2(k-2)(n-k-1) A(\theta) \Delta_{\theta} A(\theta) \\
-2(k-1)^{2}\left|\nabla_{\theta} A(\theta)\right|^{2}+\left(\Delta_{\theta} A(\theta)\right)^{2}-\left|\nabla_{\theta}^{2} A(\theta)\right|^{2}=0 .
\end{array}$$
Integrating over $\mathbb{S}^{n-1}$ and using the Bochner identity on spheres, we obtain
$$(n-2 k) \int_{\mathbb{S}^{n-1}}(n-1)(k-2)^{2} A^{2}(\theta)+(2 k-3)\left|\nabla_{\theta} A(\theta)\right|^{2} \mathrm{~d} \sigma=0$$
from which we conclude that $A(\theta) \equiv 0$. \(\square\)

When $2 k=n$, we obtain
$$-2(k-2)(k-1) A(\theta) \Delta_{\theta} A(\theta)-2(k-1)^{2}\left|\nabla_{\theta} A(\theta)\right|^{2}+\left(\Delta_{\theta} A(\theta)\right)^{2}-\left|\nabla_{\theta}^{2} A(\theta)\right|^{2}=0 .$$

This in turn implies $r^{2} \mid A_{k}^{2}$. Furthermore, since $r^{2}$ is an irreducible polynomial, we obtain $r^{2} \mid A_{k}$.

Claim. If $r^{2 l} \mid A_{k}$, then $r^{2 l+2} \mid A_{k}$, where $2 l \leq k$ and $4 l \neq n$.
To this end, we write $A_{k}(x)=r^{2 l} p(x)$, where $p(x)$ is a homogeneous polynomial of degree $k-2 l$. Then
$$\begin{aligned}
\partial_{\alpha \beta}^{2} A_{k}= & 2 l r^{2 l-2} p(x) \delta_{\alpha \beta}+4 l(l-1) r^{2 l-4} x_{\alpha} x_{\beta} p(x) \\
& +2 l r^{2 l-2}\left(x_{\alpha} \partial_{\beta} p(x)+x_{\beta} \partial_{\alpha} p(x)\right)+r^{2 l} \partial_{\alpha \beta}^{2} p(x) .
\end{aligned}$$
So,
$$\begin{aligned}
\frac{1}{r^{2 l-2} \Delta A_{k}} & =2 n l p(x)+4 l(l-1) p(x)+4 l(k-2 l) p(x)+r^{2} \Delta p(x) \\
& \equiv 2 l(n+2 k-2 l-2) p(x) \quad \bmod r^{2}
\end{aligned}$$
and
$$\begin{aligned}
\frac{1}{r^{4 l-4}}\left|\nabla^{2} A_{k}\right|^{2} \equiv & 4 n l^{2} p^{2}(x)+16 l^{2}(l-1) p^{2}(x)+16 l^{2} p(x) x_{\alpha} \partial_{\alpha} p(x) \\
& +16 l^{2}(l-1)^{2} p^{2}(x)+32 l^{2}(l-1) p(x) x_{\alpha} \partial_{\alpha} p(x) \\
& +8 l(l-1) p(x) x_{\alpha} x_{\beta} \partial_{\alpha \beta}^{2} p(x)+8 l^{2} x_{\alpha} x_{\beta} \partial_{\alpha} p(x) \partial_{\beta} p(x) \bmod r^{2} \\
\equiv & {\left[4 l^{2}\left(n+2 k^{2}-4 k-4 l^{2}+4 l\right)+8 l(l-1)(k-2 l)(k-2 l-1)\right] p^{2}(x) \bmod r^{2} . }
\end{aligned}$$
Inserting these terms into (2.13) gives
$$\begin{aligned}
0= & 4 n(n-1)(k-1)^{2} \frac{A_{k}^{2}}{r^{4 l}}-4(n-1)(k-1) \frac{A_{k}}{r^{2 l}} \frac{\Delta A_{k}}{r^{2 l-2}}+\frac{1}{r^{4 l-4}}\left[\left(\Delta A_{k}\right)^{2}-\left|\nabla^{2} A_{k}\right|^{2}\right] \\
\equiv & {\left[4 n(n-1)(k-1)^{2}-4(n-1)(k-1) \cdot 2 l(n+2 k-2 l-2)+4 l^{2}(n+2 k-2 l-2)\right.} \\
& \left.-4 l^{2}\left(n+2 k^{2}-4 k-4 l^{2}+4 l\right)-8 l(l-1)(k-2 l)(k-2 l-1)\right] p^{2}(x) \bmod r^{2} \\
\equiv & 4(k-l-1)[(k-l-1)(n-4 l)(n-1)+2 l(k-2 l)] p^{2}(x) \bmod r^{2} .
\end{aligned}$$
Hence, when $2 l \leq k$ and $4 l \neq n$, the above coefficient does not vanish, so $r^{2} \mid p^{2}(x)$, thereby $r^{2} \mid p(x)$. This directly yields $r^{2 l+2} \mid A_{k}$. We finish the proof of the claim.

When $k \leq m-1$, the above claim implies $\left.r^{2\left(\left\lfloor\frac{k}{2}\right\rfloor+1\right)} \right\rvert\, A_{k}$, but $\operatorname{deg} A_{k}=k<2\left(\left\lfloor\frac{k}{2}\right\rfloor+1\right)$. This forces
$$A_{k}(x)=0, \quad k \leq m-1 .$$
Finally, our discussion is divided into two cases.
\begin{itemize}
\item[(i)] If $4 \nmid n$, then $\left.r^{2\left(\left\lfloor\frac{m}{2}\right\rfloor+1\right)} \right\rvert\, A_{m}$, also $\operatorname{deg} A_{m}=m<2\left(\left\lfloor\frac{m}{2}\right\rfloor+1\right)$, so $A_{m}(x)=0$.
\item[(ii)] If $4 \mid n$, then $r^{m} \mid A_{m}$, so $A_{m}(x)=\kappa r^{m}$ for some constant $\kappa$.
\end{itemize}
This completes the proof. \(\square\)

\section*{3 Adapted asymptotic coordinates and the ADM mass}

Throughout this section, we let $\lambda=\frac{H(Q)}{n}$ and fix $m=\left\lfloor\frac{n}{2}\right\rfloor$ as before.
The following elementary lemma demonstrates that for all $n \geq 3$, there exists an adapted asymptotic coordinate system for $(M \backslash\{Q\}, \hat{g})$ such that the mass $m(\hat{g})$ is well defined thanks to Proposition 2.

Lemma 3. If $f(x)=\phi(x)+O\left(|x|^{k}\right)$ for some integer $k \geq 3$, then there is an adapted asymptotic coordinate system
$$y=\frac{\lambda}{2} \frac{x}{\phi(x)}=\frac{1+\sqrt{1-\lambda^{2}|x|^{2}}}{2} \frac{x}{|x|^{2}}$$
such that $(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order $k$.
Proof. Let $r=|x|$ and $t=|y|$. A direct computation together with (2.5) yields
$$\frac{\lambda^{2}}{4}+|y|^{2}=\frac{\lambda^{2}}{4}+\frac{\lambda^{2}}{4} \frac{|x|^{2}}{\phi^{2}}=\frac{\lambda}{2} \frac{1}{\phi(x)} .$$
This gives
$$\phi(x)=\frac{\lambda}{2} \frac{1}{\frac{\lambda^{2}}{4}+|y|^{2}}$$
and the inverse of the above asymptotic coordinate map is
$$x=\frac{y}{\frac{\lambda^{2}}{4}+|y|^{2}} .$$
In terms of the variable $y$, we can express
$$f(y)=\frac{\lambda}{2} \frac{1}{\frac{\lambda^{2}}{4}+|y|^{2}}+\sum_{i=k}^{2 k-3} \widetilde{A_{i}}(y)+O\left(|y|^{2-2 k}\right),$$
where $\widetilde{A_{i}}(y)$ is a homogeneous polynomial of degree $-i$.
Remark 3. Since $f$ is smooth by assumption and the coordinate change is explicit, it is evident that the $O\left(|y|^{2-2 k}\right)$ term behaves nice when taking derivatives, and is in fact $O_{l}\left(|y|^{2-2 k}\right)$ for any $l$ by a direct mathematical induction argument. This fact will be frequently used later.

Notice that
$$\begin{aligned}
\rho & =r^{2}+f^{2} \\
& =\frac{t^{2}}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}}+\frac{\lambda^{2}}{4} \frac{1}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}}+\frac{\lambda}{t^{2}+\frac{\lambda^{2}}{4}} \sum_{i=k}^{2 k-3} \widetilde{A_{i}}+O\left(t^{-2 k}\right) \\
& =\frac{1}{t^{2}+\frac{\lambda^{2}}{4}}\left(1+\lambda \sum_{i=k}^{2 k-3} \widetilde{A_{i}}+O\left(t^{2-2 k}\right)\right)
\end{aligned}$$

So,
$$\rho^{-2}=\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}\left(1-2 \lambda \sum_{i=k}^{2 k-3} \widetilde{A_{i}}+O\left(t^{2-2 k}\right)\right) .$$

In terms of the new variable $y$ we obtain
$$\begin{aligned}
g= & \mathrm{d} x_{\alpha} \otimes \mathrm{d} x_{\alpha}+\mathrm{d} f \otimes \mathrm{~d} f \\
= & \mathrm{d}\left(\frac{y_{\alpha}}{t^{2}+\frac{\lambda^{2}}{4}}\right) \otimes \mathrm{d}\left(\frac{y_{\alpha}}{t^{2}+\frac{\lambda^{2}}{4}}\right) \\
& +\mathrm{d}\left(\frac{\lambda}{2} \frac{1}{t^{2}+\frac{\lambda^{2}}{4}}+\sum_{i=k}^{2 k-3} \widetilde{A_{i}}(y)+O\left(t^{2-2 k}\right)\right) \otimes \mathrm{d}\left(\frac{\lambda}{2} \frac{1}{t^{2}+\frac{\lambda^{2}}{4}}+\sum_{i=k}^{2 k-3} \widetilde{A_{i}}(y)+O\left(t^{2-2 k}\right)\right) \\
= & \left(\frac{\mathrm{d} y_{\alpha}}{t^{2}+\frac{\lambda^{2}}{4}}-\frac{2 y_{\alpha} t \mathrm{~d} t}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}}\right) \otimes\left(\frac{\mathrm{d} y_{\alpha}}{t^{2}+\frac{\lambda^{2}}{4}}-\frac{2 y_{\alpha} t \mathrm{~d} t}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}}\right) \\
& +\frac{\lambda^{2}}{4} \frac{4 t^{2} \mathrm{~d} t \otimes \mathrm{~d} t}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{4}}-\frac{\lambda t}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}} \mathrm{~d} t \otimes \mathrm{~d}\left(\sum_{i=k}^{2 k-3} \widetilde{A_{i}}\right) \\
& -\frac{\lambda t}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}} \mathrm{~d}\left(\sum_{i=k}^{2 k-3} \widetilde{A_{i}}\right) \otimes \mathrm{d} t+O\left(t^{-2 k-2}\right) \\
= & \left(t^{2}+\frac{\lambda^{2}}{4}\right)^{-2}\left(\mathrm{~d} y_{\alpha} \otimes \mathrm{d} y_{\alpha}-\lambda t \mathrm{~d} t \otimes \mathrm{~d}\left(\sum_{i=k}^{2 k-3} \widetilde{A_{i}}\right)-\lambda t \mathrm{~d}\left(\sum_{i=k}^{2 k-3} \widetilde{A_{i}}\right) \otimes \mathrm{d} t+O\left(t^{2-2 k}\right)\right) .
\end{aligned}$$
Then we have
$$\begin{aligned}
\hat{g}= & \rho^{-2}\left(\mathrm{~d} x_{\alpha} \otimes \mathrm{d} x_{\alpha}+\mathrm{d} f \otimes \mathrm{~d} f\right) \\
= & \left(1-2 \lambda \sum_{i=k}^{2 k-3} \widetilde{A_{i}}+O\left(t^{2-2 k}\right)\right) \\
& \cdot\left(\mathrm{d} y_{\alpha} \otimes \mathrm{d} y_{\alpha}-\lambda t \mathrm{~d} t \otimes \mathrm{~d}\left(\sum_{i=k}^{2 k-3} \widetilde{A_{i}}\right)-\lambda t \mathrm{~d}\left(\sum_{i=k}^{2 k-3} \widetilde{A_{i}}\right) \otimes \mathrm{d} t+O\left(t^{2-2 k}\right)\right) \\
= & \left(1-2 \lambda \sum_{i=k}^{2 k-3} \widetilde{A_{i}}\right) \mathrm{d} y_{\alpha} \otimes \mathrm{d} y_{\alpha}-\lambda t \mathrm{~d} t \otimes \mathrm{~d}\left(\sum_{i=k}^{2 k-3} \widetilde{A_{i}}\right) \\
& -\lambda t \mathrm{~d}\left(\sum_{i=k}^{2 k-3} \widetilde{A_{i}}\right) \otimes \mathrm{d} t+O\left(t^{2-2 k}\right)
\end{aligned}$$
This directly yields
$$\hat{g}_{\alpha \beta}=\delta_{\alpha \beta}+\hat{h}_{\alpha \beta}$$
with $\hat{h}_{\alpha \beta}=O\left(t^{-k}\right), \partial \hat{h}_{\alpha \beta}=O\left(t^{-k-1}\right)$ and $\partial^{2} \hat{h}_{\alpha \beta}=O\left(t^{-k-2}\right)$. Hence $y$ is an asymptotically flat coordinate system of order $k$. \(\square\)

Now we are ready to prove Theorem 2

Proof of Theorem 2 By Proposition 2, we have $f(x)=\phi(x)+O\left(r^{m+1}\right)$ when $4 \nmid n$. By Lemma 3, we know that $y$ is an asymptotic coordinate system of order $m+1$.

Since $m+1=\left\lfloor\frac{n}{2}\right\rfloor+1>\frac{n-2}{2}$, the ADM mass is well defined. Observe that
$$\begin{aligned}
\sum_{\alpha} \hat{g}_{\alpha \alpha} & =n\left(1-2 \lambda \sum_{i=m+1}^{2 m-1} \widetilde{A_{i}}\right)+2 \lambda \sum_{i=m+1}^{2 m-1} i \widetilde{A_{i}}+O\left(t^{-2 m}\right), \\
\hat{g}_{t t} & =\sum_{\alpha, \beta} \hat{g}_{\alpha \beta} y_{\alpha} y_{\beta} t^{-2} \\
& =\left(1-2 \lambda \sum_{i=m+1}^{2 m-1} \widetilde{A_{i}}\right)+2 \lambda \sum_{i=m+1}^{2 m-1} i \widetilde{A_{i}}+O\left(t^{-2 m}\right) .
\end{aligned}$$
Subsequently, in view of Remark 3
$$\begin{aligned}
\partial_{t}\left(\hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right) & =-(n-1) \partial_{t}\left(1-2 \lambda \sum_{i=m+1}^{2 m-1} \widetilde{A_{i}}\right)+O\left(t^{-2 m-1}\right) \\
& =-2(n-1) \lambda t^{-1} \sum_{i=m+1}^{2 m-1} i \widetilde{A_{i}}+O\left(t^{-2 m-1}\right), \\
\frac{1}{t}\left(n \hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right) & =2(n-1) \lambda t^{-1} \sum_{i=m+1}^{2 m-1} i \widetilde{A_{i}}+O\left(t^{-2 m-1}\right) .
\end{aligned}$$
Hence we obtain
$$\begin{aligned}
m(\hat{g}) & =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{|y|=t} \partial_{t}\left(\hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right)+\frac{1}{t}\left(n \hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right) \mathrm{d} \sigma \\
& =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{|y|=t} O\left(t^{-2 m-1}\right) \mathrm{d} \sigma \\
& =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}^{n-1}} O\left(t^{n-2 m-2}\right) \mathrm{d} \sigma=0 .
\end{aligned}$$
For the $4 \mid n$ case, we have the following lemma, which concludes the proof. \(\square\)

Lemma 4. When $n=4 k, k \geq 2$, there hold
$$f(x)=\phi(x)+\kappa|x|^{\frac{n}{2}}+O\left(|x|^{\frac{n}{2}+1}\right), \quad \kappa \in \mathbb{R},$$
near $Q$, and under the asymptotic coordinates $y=\frac{\lambda}{2} \phi^{-1}(x) x,(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order $\frac{n}{2}$. Moreover, the mass of $\hat{g}$ is $m(\hat{g})=\frac{(n-1)(n-4)^{2}}{4} \kappa^{2}$.

Proof. In terms of the variable $y$ we have
$$\begin{aligned}
f(y) & =\frac{\lambda}{2} \frac{1}{t^{2}+\frac{\lambda^{2}}{4}}+\frac{\kappa t^{\frac{n}{2}}}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{\frac{n}{2}}} \\
& =\frac{\lambda}{2} \frac{1}{t^{2}+\frac{\lambda^{2}}{4}}+\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{\infty} a_{i} t^{-i}, \quad a_{i} \in \mathbb{R} .
\end{aligned}$$

So,
$$\begin{aligned}
\rho & =r^{2}+f^{2} \\
& =\frac{t^{2}}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}}+\frac{\lambda^{2}}{4} \frac{1}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}}+\frac{\kappa \lambda t^{-\frac{n}{2}}}{t^{2}+\frac{\lambda^{2}}{4}}+\frac{\lambda}{t^{2}+\frac{\lambda^{2}}{4}} \sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}+\kappa^{2} t^{-n}+O\left(t^{-n-1}\right) \\
& =\frac{1}{t^{2}+\frac{\lambda^{2}}{4}}\left[1+\kappa \lambda t^{-\frac{n}{2}}+\lambda \sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}+\kappa^{2} t^{2-n}+O\left(t^{1-n}\right)\right]
\end{aligned}$$
and then
$$\rho^{-2}=\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}\left(1-2 \kappa \lambda t^{-\frac{n}{2}}-2 \lambda \sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}-2 \kappa^{2} t^{2-n}+O\left(t^{1-n}\right)\right) .$$

Similarly as before, we have
$$\begin{aligned}
g= & \mathrm{d} x_{\alpha} \otimes \mathrm{d} x_{\alpha}+\mathrm{d} f \otimes \mathrm{~d} f \\
= & \left(t^{2}+\frac{\lambda^{2}}{4}\right)^{-2} \mathrm{~d} y_{\alpha} \otimes \mathrm{d} y_{\alpha}-\frac{\lambda t}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}} \mathrm{~d} t \otimes \mathrm{~d}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{\infty} a_{i} t^{-i}\right) \\
& -\frac{\lambda t}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}} \mathrm{~d}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{\infty} a_{i} t^{-i}\right) \otimes \mathrm{d} t \\
& +\mathrm{d}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{\infty} a_{i} t^{-i}\right) \otimes \mathrm{d}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{\infty} a_{i} t^{-i}\right)+O\left(t^{-n-3}\right) \\
= & \left(t^{2}+\frac{\lambda^{2}}{4}\right)^{-2} \mathrm{~d} y_{\alpha} \otimes \mathrm{d} y_{\alpha}-\frac{\lambda t}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}} \mathrm{~d} t \otimes \mathrm{~d}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}\right) \\
& -\frac{\lambda t}{\left(t^{2}+\frac{\lambda^{2}}{4}\right)^{2}} \mathrm{~d}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}\right) \otimes \mathrm{d} t+\frac{n^{2}}{4} \kappa^{2} t^{-n-2} \mathrm{~d} t \otimes \mathrm{~d} t+O\left(t^{-n-3}\right)
\end{aligned}$$
Then,
$$\begin{aligned}
\hat{g}= & \rho^{-2}\left(\mathrm{~d} x_{\alpha} \otimes \mathrm{d} x_{\alpha}+\mathrm{d} f \otimes \mathrm{~d} f\right) \\
= & \left(1-2 \kappa \lambda t^{-\frac{n}{2}}-2 \lambda \sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}-2 \kappa^{2} t^{2-n}\right) \mathrm{d} y_{\alpha} \otimes \mathrm{d} y_{\alpha} \\
& -\lambda t \mathrm{~d} t \otimes \mathrm{~d}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}\right)-\lambda t \mathrm{~d}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}\right) \otimes \mathrm{d} t \\
& +\frac{n^{2}}{4} \kappa^{2} t^{2-n} \mathrm{~d} t \otimes \mathrm{~d} t+O\left(t^{1-n}\right)
\end{aligned}$$
equivalently,
$$\begin{aligned}
\hat{g}_{\alpha \beta}= & \delta_{\alpha \beta}\left(1-2 \kappa \lambda t^{-\frac{n}{2}}-2 \lambda \sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}-2 \kappa^{2} t^{2-n}\right) \\
& -\lambda\left(y_{\alpha} \partial_{\beta}+y_{\beta} \partial_{\alpha}\right)\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}\right)+\frac{n^{2}}{4} \kappa^{2} t^{-n} y_{\alpha} y_{\beta}+O\left(t^{1-n}\right) .
\end{aligned}$$
This indicates that $y$ is an asymptotically flat coordinate system of order $\frac{n}{2}$. So the mass is well defined.

Observe that
$$\begin{aligned}
\sum_{\alpha} \hat{g}_{\alpha \alpha}= & n\left(1-2 \kappa \lambda t^{-\frac{n}{2}}-2 \lambda \sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}-2 \kappa^{2} t^{2-n}\right) \\
& -2 \lambda t \partial_{t}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}\right)+\frac{n^{2}}{4} \kappa^{2} t^{2-n}+O\left(t^{1-n}\right)
\end{aligned}$$
and
$$\begin{aligned}
\hat{g}_{t t}= & \left(1-2 \kappa \lambda t^{-\frac{n}{2}}-2 \lambda \sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}-2 \kappa^{2} t^{2-n}\right) \\
& -2 \lambda t \partial_{t}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}\right)+\frac{n^{2}}{4} \kappa^{2} t^{2-n}+O\left(t^{1-n}\right) .
\end{aligned}$$
Combining these terms above yields, as before,
$$\begin{aligned}
\partial_{t}\left(\hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right) & =-(n-1) \partial_{t}\left(1-2 \kappa \lambda t^{-\frac{n}{2}}-2 \lambda \sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}-2 \kappa^{2} t^{2-n}+O\left(t^{1-n}\right)\right) \\
& =2 \lambda(n-1) \partial_{t}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}\right)+2(n-1)(2-n) \kappa^{2} t^{1-n}+O\left(t^{-n}\right) \\
\frac{1}{t}\left(n \hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right) & =-2 \lambda(n-1) \partial_{t}\left(\kappa t^{-\frac{n}{2}}+\sum_{i=\frac{n}{2}+1}^{n-2} a_{i} t^{-i}\right)+(n-1) \frac{n^{2}}{4} \kappa^{2} t^{1-n}+O\left(t^{-n}\right)
\end{aligned}$$
This leads to
$$\begin{aligned}
& \partial_{t}\left(\hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right)+\frac{1}{t}\left(n \hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right) \\
= & 2(n-1)(2-n) \kappa^{2} t^{1-n}+(n-1) \frac{n^{2}}{4} \kappa^{2} t^{1-n}+O\left(t^{-n}\right) \\
= & \frac{(n-1)(n-4)^{2}}{4} \kappa^{2} t^{1-n}+O\left(t^{-n}\right) .
\end{aligned}$$

Consequently, we obtain
$$\begin{aligned}
m(\hat{g}) & =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{|y|=t} \partial_{t}\left(\hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right)+\frac{1}{t}\left(n \hat{g}_{t t}-\sum_{\alpha} \hat{g}_{\alpha \alpha}\right) \mathrm{d} \sigma \\
& =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}^{n-1}} \frac{(n-1)(n-4)^{2}}{4} \kappa^{2}+O\left(t^{-1}\right) \mathrm{d} \sigma \\
& =\frac{(n-1)(n-4)^{2}}{4} \kappa^{2} .
\end{aligned}$$ \(\square\)

Example 1. When $n=4 k, k \geq 2$, the vanishing order of $f-\phi$ in Proposition 2 cannot be improved. For example, locally we may take
$$f(x)=\phi(x)+\kappa|x|^{2 k}+|x|^{2 k} l(x)+O\left(|x|^{2 k+2}\right),$$
where $\kappa \in \mathbb{R} \backslash\{0\}$ and $l(x)$ is any linear function, and extend this local graph to a closed hypersurface smoothly. Then we always have $R_{\hat{g}}=O\left(r^{n+2}\right)$, that is,
$$\mathcal{R}=O\left(r^{n-2}\right) \quad \Rightarrow \quad m(\hat{g})=\frac{(n-1)(n-4)^{2}}{4} \kappa^{2}>0 .$$
Also, even if we impose a stronger condition that $R_{\hat{g}}=0$ in a punctured neighborhood of the umbilical point $Q$ and $f$ is real analytic, it fails to obtain the vanishing of $\kappa$. Since the above computations are similar to those of Proposition 2. we leave the details to interested readers.

The above example demonstrates that in dimensions $n=4 k+2, k \geq 2$, a global analysis is crucial to the resolution of GFRC, which occupies the whole Section 4.

\section*{4 A new mass formula and GFRC for $\boldsymbol{P}_{\mathbf{2}}^{\boldsymbol{g}}$}

Recall that locally $M$ is a graph of a smooth function $f: B_{\delta}(0) \rightarrow \mathbb{R}$ near $Q$. Without loss of generality, we assume that $Q$ is the origin of $\mathbb{R}^{n+1}$. Under the inversion $I_{Q}$ as in (1.3), the inverted hypersurface becomes
$$\left\{\left(\frac{x}{|x|^{2}+f(x)^{2}}, \frac{f(x)}{|x|^{2}+f(x)^{2}}\right) ; \quad x \in B_{\delta}(0) \subset \mathbb{R}^{n}\right\} .$$
Now we introduce a new coordinate change by
$$y=\frac{x}{|x|^{2}+f(x)^{2}} .$$
When $|x| \ll 1$, this gives an asymptotic coordinate system for the end of $I_{Q}(M \backslash\{Q\})$. Combining the fact that $f(x)=\phi(x)+O\left(|x|^{\frac{n}{2}}\right)$ by Proposition 2 and (2.5) we obtain
$$\frac{\lambda}{2}\left(|x|^{2}+f^{2}(x)\right)=\frac{\lambda}{2}\left(|x|^{2}+\phi^{2}(x)\right)+O\left(|x|^{\frac{n}{2}+2}\right)=\phi(x)+O\left(|x|^{\frac{n}{2}+2}\right) .$$

So this new coordinate change is very close to that of Section 3 Using this coordinate chart $y$, the end of $I_{Q}(M \backslash\{Q\})$ becomes a graph of the function
$$\psi(y)=\frac{f(x)}{|x|^{2}+f^{2}(x)} .$$
Here the coordinates $x$ and $y$ are related by the formula (4.1). Then under the coordinates $y, \hat{g}=\rho^{-2} g=|\mathrm{d} y|^{2}+\mathrm{d} \psi \otimes \mathrm{d} \psi$ is the induced metric, thereby $\hat{g}_{\alpha \beta}=\delta_{\alpha \beta}+\psi_{\alpha} \psi_{\beta}$.

Note that
$$\psi(y)=\frac{\frac{\lambda}{2} \phi(x)+O\left(|x|^{\frac{n}{2}}\right)}{\phi(x)+O\left(|x|^{\frac{n}{2}+2}\right)}=\frac{\lambda}{2}+O\left(|x|^{\frac{n}{2}-2}\right)=\frac{\lambda}{2}+O\left(|y|^{-\frac{n}{2}+2}\right) .$$
It is direct to check that
$$|\partial \psi|+|y| \cdot\left|\partial^{2} \psi\right|+|y|^{2} \cdot\left|\partial^{3} \psi\right|=O\left(|y|^{-\frac{n}{2}+1}\right) .$$
As in Lam's work [17], we have
$$\begin{aligned}
m(\hat{g}) & =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}}\left(\partial_{\alpha} \hat{g}_{\alpha \beta}-\partial_{\beta} \hat{g}_{\alpha \alpha}\right) v^{\beta} \mathrm{d} \sigma_{\mathbb{S}_{t}^{n-1}} \\
& =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}}\left(\psi_{\alpha \alpha} \psi_{\beta}-\psi_{\alpha \beta} \psi_{\alpha}\right) v^{\beta} \mathrm{d} \sigma_{\mathbb{S}_{t}^{n-1}} .
\end{aligned}$$
However, since $I_{Q}(M \backslash\{Q\})$ may not be an entire graph, it seems impossible to write this directly as a global integration as in [17]. To overcome this difficulty, we discover a new mass formula that works for a general asymptotically flat hypersurface, which is a graph only at its end.

The key observation is that the vector field
$$\frac{1}{1+|\nabla \psi|^{2}}\left(\psi_{\alpha \alpha} \psi_{\beta}-\psi_{\alpha \beta} \psi_{\alpha}\right) \frac{\partial}{\partial y_{\beta}}$$
is in fact globally defined on the hypersurface, although it is not necessarily an entire graph, and its divergence equals a smooth function multiple of the scalar curvature. This can be verified directly using the fact that the hypersurface can be realized as a level set of some smooth function $\mathcal{F}$ on $\mathbb{R}^{n+1}$, and each term above can be expressed by $\mathcal{F}$ and its derivatives. Instead, we switch to the following simpler and more geometric approach here.

We start with an elementary lemma regarding hypersurfaces.
Proposition 3. Let $M \subset \mathbb{R}^{n+1}$ be an oriented hypersurface with a unit normal vector field n. Let $\mathbf{e}$ be a constant vector field on $\mathbb{R}^{n+1}$ and let $v:=\mathbf{e}^{\top}$ be its tangential part along $M$. For a symmetric 2-tensor $T$, consider $X:=\left(i_{v} T\right)^{\sharp}$, the dual of the 1-form $i_{v} T$ or raising index of $i_{v} T$, then
$$\operatorname{div}_{g} X=\left(\operatorname{div}_{g} T\right)(v)+\langle\mathbf{e}, \mathbf{n}\rangle\langle I I, T\rangle .$$
In particular, if $\operatorname{div}_{g} T=0$, then
$$\operatorname{div}_{g} X=\langle\mathbf{e}, \mathbf{n}\rangle\langle I I, T\rangle .$$

Proof. Let $\left\{e_{\alpha}\right\}_{\alpha=1}^{n}$ be a local orthonormal frame along $M$. First we compute $\nabla_{e_{\alpha}}^{g} v$ :
$$\begin{aligned}
\nabla_{e_{\alpha}}^{g} v & =\left(\nabla_{e_{\alpha}} v\right)^{\top} \\
& =\left(\nabla_{e_{\alpha}}(\mathbf{e}-\langle\mathbf{e}, \mathbf{n}\rangle \mathbf{n})\right)^{\top} \\
& =\left(-e_{\alpha}\langle\mathbf{e}, \mathbf{n}\rangle \mathbf{n}-\langle\mathbf{e}, \mathbf{n}\rangle \nabla_{e_{\alpha}} \mathbf{n}\right)^{\top} \\
& =\langle\mathbf{e}, \mathbf{n}\rangle h_{\alpha \beta} e_{\beta} .
\end{aligned}$$
This follows that ${ }^{1}$
$$\begin{aligned}
\operatorname{div}_{g} X & =\sum_{\alpha}\left\langle\nabla_{e_{\alpha}}^{g} X, e_{\alpha}\right\rangle \\
& =\sum_{\alpha}\left(\nabla_{e_{\alpha}}^{g}\left(i_{v} T\right)\right)\left(e_{\alpha}\right) \\
& =\sum_{\alpha}\left(e_{\alpha} T\left(v, e_{\alpha}\right)-T\left(v, \nabla_{e_{\alpha}}^{g} e_{\alpha}\right)\right) \\
& =\sum_{\alpha}\left(\left(\nabla_{e_{\alpha}}^{g} T\right)\left(v, e_{\alpha}\right)+T\left(\nabla_{e_{\alpha}}^{g} v, e_{\alpha}\right)\right) \\
& =\left(\operatorname{div}_{g} T\right)(v)+\langle\mathbf{e}, \mathbf{n}\rangle \sum_{\alpha, \beta} h_{\alpha \beta} T\left(e_{\beta}, e_{\alpha}\right) \\
& =\left(\operatorname{div}_{g} T\right)(v)+\langle\mathbf{e}, \mathbf{n}\rangle\langle I I, T\rangle .
\end{aligned}$$ \(\square\)

Now we are ready to prove Theorem 3
Proof of Theorem 3 Recall that $N$ is a complete non-compact hypersurface in $\mathbb{R}^{n+1}$ with induced metric $g$. And there is a compact subset $K \subset N$ such that $N \backslash K$ is the graph of a smooth function $\psi: \mathbb{R}^{n} \backslash B_{R}(0) \rightarrow \mathbb{R}$, satisfying
$$\left|\partial_{\alpha} \psi\right|+\left|y \| \partial_{\alpha \beta}^{2} \psi\right|+|y|^{2}\left|\partial_{\alpha \beta \gamma}^{3} \psi\right|=O\left(|y|^{-\frac{\tau}{2}}\right)$$
with $\tau>\frac{n-2}{2}$. By the Codazzi equation, $I I-H g$ is divergence-free ${ }^{2}$. From now on, we choose $\mathbf{e}=e_{n+1}, T=H g-I I$ such that
$$\operatorname{div}_{g} X=\langle\mathbf{e}, \mathbf{n}\rangle\left(H^{2}-|I I|^{2}\right)=\langle\mathbf{e}, \mathbf{n}\rangle R_{g} .$$

Claim. We have
$$\left.i_{X} \mathrm{~d} V_{g}=X\right\lrcorner \mathrm{d} V_{g}=\frac{1}{1+|\nabla \psi|^{2}}\left(\psi_{\alpha \alpha} \psi_{\beta}-\psi_{\alpha \beta} \psi_{\alpha}\right) \nu^{\beta} \mathrm{d} \sigma_{\mathbb{S}_{t}^{n-1}}$$

In fact, along $N \backslash K$, we identify $\frac{\partial}{\partial y_{\alpha}}$ with $e_{\alpha}+\psi_{\alpha} e_{n+1}$. So we have
$$\mathbf{e}^{\top}=e_{n+1}-\frac{(-\nabla \psi, 1)}{1+|\nabla \psi|^{2}}=\frac{\psi_{\alpha} e_{\alpha}+|\nabla \psi|^{2} e_{n+1}}{1+|\nabla \psi|^{2}}=\frac{\psi_{\alpha}}{1+|\nabla \psi|^{2}} \frac{\partial}{\partial y_{\alpha}} .$$

\footnotetext{
${ }^{1}$ Similar computations also appear in [28, Proposition 2.6] for Newton transforms.
${ }^{2}$ This is essentially the first order Newton transform for the hypersurface.
}

Then we obtain
$$\begin{aligned}
\left(i_{\mathbf{e}^{\top} I} I\right)^{\sharp} & =\left(\frac{\psi_{\alpha \beta} \psi_{\alpha} \mathrm{d} y_{\beta}}{\left(1+|\nabla \psi|^{2}\right)^{\frac{3}{2}}}\right)^{\sharp} \\
& =\left(\delta_{\gamma \beta}-\frac{\psi_{\gamma} \psi_{\beta}}{1+|\nabla \psi|^{2}}\right) \frac{\psi_{\alpha \beta} \psi_{\alpha}}{\left(1+|\nabla \psi|^{2}\right)^{\frac{3}{2}}} \frac{\partial}{\partial y_{\gamma}} \\
& =\left(\frac{\psi_{\alpha \gamma} \psi_{\alpha}}{\left(1+|\nabla \psi|^{2}\right)^{\frac{3}{2}}}-\frac{\psi_{\gamma} \psi_{\alpha \beta} \psi_{\alpha} \psi_{\beta}}{\left(1+|\nabla \psi|^{2}\right)^{\frac{5}{2}}}\right) \frac{\partial}{\partial y_{\gamma}}
\end{aligned}$$
and
$$\begin{aligned}
\left(i_{\mathbf{e}^{\top}}(H g)\right)^{\sharp} & =\left(\frac{H \psi_{\alpha}}{1+|\nabla \psi|^{2}}\left(\delta_{\alpha \beta}+\psi_{\alpha} \psi_{\beta}\right) \mathrm{d} y_{\beta}\right)^{\sharp}=\left(H \psi_{\beta} \mathrm{d} y_{\beta}\right)^{\sharp} \\
& =H \psi_{\beta}\left(\delta_{\gamma \beta}-\frac{\psi_{\gamma} \psi_{\beta}}{1+|\nabla \psi|^{2}}\right) \frac{\partial}{\partial y_{\gamma}}=\frac{H \psi_{\gamma}}{1+|\nabla \psi|^{2}} \frac{\partial}{\partial y_{\gamma}} \\
& =\frac{\psi_{\gamma}}{1+|\nabla \psi|^{2}}\left(\frac{\Delta \psi}{\sqrt{1+|\nabla \psi|^{2}}}-\frac{\psi_{\mu \nu} \psi_{\mu} \psi_{\nu}}{\left(1+|\nabla \psi|^{2}\right)^{\frac{3}{2}}}\right) \frac{\partial}{\partial y_{\gamma}} .
\end{aligned}$$

Consequently,
$$X=\left(i_{\mathbf{e}^{\top}}(H g-I I)\right)^{\sharp}=\frac{1}{\left(1+|\nabla \psi|^{2}\right)^{\frac{3}{2}}}\left(\psi_{\alpha \alpha} \psi_{\beta}-\psi_{\alpha \beta} \psi_{\alpha}\right) \frac{\partial}{\partial y_{\beta}} .$$
Thus, we also have
$$i_{X} \mathrm{~d} V_{g}=i_{X}\left(\sqrt{1+|\nabla \psi|^{2}} \mathrm{~d} V_{\mathbb{R}^{n}}\right)=\frac{1}{1+|\nabla \psi|^{2}}\left(\psi_{\alpha \alpha} \psi_{\beta}-\psi_{\alpha \beta} \psi_{\alpha}\right) \nu^{\beta} \mathrm{d} \sigma_{\mathbb{S}_{t}^{n-1}} .$$

Using this and Proposition 3 we conclude that
$$\begin{aligned}
m(g) & =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}}\left(\psi_{\alpha \alpha} \psi_{\beta}-\psi_{\alpha \beta} \psi_{\alpha}\right) \nu^{\beta} \mathrm{d} \sigma_{\mathbb{S}_{t}^{n-1}} \\
& \left.=\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}} X\right\lrcorner \mathrm{d} V_{g} \\
& =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \int_{N} \operatorname{div}_{g}(X) \mathrm{d} V_{g} \\
& =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \int_{N}\left\langle e_{n+1}, \mathbf{n}\right\rangle R_{g} \mathrm{~d} V_{g} .
\end{aligned}$$
This completes the proof of Theorem 3 \(\square\)

As a direct application of Theorem 3, we give a unified proof of $m(\hat{g})=0$ when $n \geq 3$, including the exceptional case $n=4 k, k \geq 2$.

Now we can prove Theorem 1.
Proof of Theorem 1 Since we now have Theorems 2 and 3, the remaining part of the proof is identical to that of [6, Theorem 4]. So we only outline the proof and refer the interested readers to [6] for details.

As in [6, Lemma 5], we have already proved that if there is a point $Q \in M$ such that the Green function for the conformal Laplacian has the form of $G(P, Q)=\frac{1}{(n-2)\left|\mathbb{S}^{n-1}\right|} \| P-$ $Q \|^{2-n}, \forall P \in M \backslash\{Q\}$, then $Q$ is umbilical. Also, the Green function for the conformal Laplacian implies that $R_{\hat{g}} \equiv 0$. Then we deduce from Theorems 2 and 3 that the mass of $\hat{g}$ is zero. Since our manifold has an induced spin structure from $\mathbb{R}^{n+1}$, we can apply the spin version of the Positive Mass Theorem in [3] to conclude that $(M \backslash\{Q\}, \hat{g})$ is isometric to the flat $\mathbb{R}^{n}$. Then the theorem follows from the following lemma, which is contained in the proof in [6] of $\boldsymbol{G F R C}$ when $n=3,4,5$. \(\square\)

Lemma 5. Let $M \subset \mathbb{R}^{n+1}$ be an embedded closed hypersurface, and $Q \in M$ is an umbilical point. Let $I_{Q}$ be the inversion of $\mathbb{R}^{n+1}$ with center $Q$ as in (1.3). If $I_{Q}(M \backslash\{Q\})$ with induced metric $\hat{g}$ is isometric to the flat space form $\mathbb{R}^{n}$, then $M$ is a round sphere.

For the convenience of readers, we include a heuristic and sketched proof.
Proof. Regarding the isometry as the identity map and $Q$ as the origin, we obtain a smooth embedding $F: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n+1}$ such that
$$g=F^{*} g_{\mathbb{R}^{n+1}}=|F|^{4} g_{\mathbb{R}^{n}} \quad \text { in } \quad \mathbb{R}^{n}$$
with the normalization that $\lim _{|y| \rightarrow \infty} F(y)=0$. Consider an inverted hypersurface $U$
$$w:=U(y)=I_{Q} \circ F(y), \quad y \in \mathbb{R}^{n} .$$
A nice observation
$$U^{*} g_{\mathbb{R}^{n+1}}=F^{*} I_{Q}^{*} g_{\mathbb{R}^{n+1}}=F^{*}\left(|w|^{-4}|\mathrm{~d} w|^{2}\right)=|F(y)|^{-4} g=|\mathrm{d} y|^{2}$$
implies that $U$ is a complete flat hypersurface in $\mathbb{R}^{n+1}$.
Using Hartman-Nirenberg's characterization in [13] of complete flat hypersurfaces in $\mathbb{R}^{n+1}$, we know that $\left(I_{Q}(M \backslash\{Q\}), \hat{g}\right)$ is a generalized cylinder in $\mathbb{R}^{n+1}$ and can be parametrized as
$$U(t, z)=(x(t), y(t), z), \quad t \in \mathbb{R}, z \in \mathbb{R}^{n-1},$$
where $t \mapsto(x(t), y(t))$ is a regular plane curve parametrized by arc length $t$. Consequently, $M$ can be parametrized by
$$F(t, z)=\frac{(x(t), y(t), z)}{x(t)^{2}+y(t)^{2}+|z|^{2}} .$$
Using this special parametrization of $M$, we can compute the principal curvatures of $M$ in $\mathbb{R}^{n+1}$. It turns out that there are only two possible values for the principal curvatures at any point. The first one,
$$\lambda=-2\left(x y^{\prime}-x^{\prime} y\right)$$
is a principal curvature of multiplicity at least $n-1$, and the other one is
$$\mu=\lambda-k(t)\left(x^{2}+y^{2}+|z|^{2}\right),$$
where $k(t)$ is the relative curvature of the plane curve $(x(t), y(t))$.
Since $Q$ is umbilical, $\lambda-\mu$ tends to zero when the point approaches $Q$. This forces $k(t)$ to vanish everywhere and hence $I_{Q}(M \backslash\{Q\}) \subset \mathbb{R}^{n+1}$ must be a hyperplane. As a consequence, $M$ is itself a round sphere. \(\square\)

\section*{5 Positive energy theorem and GFRC for $P_{4}^{g}$}

Now we turn to the GFRC for Paneitz operator $P_{4}^{g}$. Similar to the conformal Laplacian case, the main tool is the positive energy theorem for $P_{4}^{g}$.

For $n \geq 5$, let $\left(N^{n}, \hat{g}\right)$ be an asymptotically flat manifold of order $\tau>\frac{n-4}{2}$ and regularity order 4. If $Q_{\hat{g}} \in L^{1}(N, \hat{g})$, then a delicate calculation together with the definition (1.2) of $Q$-curvature yields (cf. [2, p.8])
$$Q_{\hat{g}}=-\frac{1}{2(n-1)} \Delta_{\hat{g}} R_{\hat{g}}+O\left(t^{-2 \tau-4}\right)$$
under asymptotic coordinates $y$ with $t=|y|$, and thus $\mathrm{m}_{4}(\hat{g})$ is well defined. Notice that
$$v_{\hat{g}}=\frac{\hat{g}^{\alpha \beta} y_{\beta} \partial_{\alpha}}{\|y\|_{\hat{g}}} \quad \text { with } \quad\|y\|_{\hat{g}}:=\sqrt{\hat{g}^{\alpha \beta} y_{\alpha} y_{\beta}}$$
is the outward unit normal vector field on $\mathbb{S}_{t}^{n-1}$ with respect to $\hat{g}$, thereby
$$\left|v_{\hat{g}}-v\right|=O\left(t^{-\tau}\right) .$$
Based on these facts the authors [2 Proposition 2] established another equivalent formula of geometric flavor:
$$\mathrm{m}_{4}(\hat{g})=-\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}} \partial_{t} R_{\hat{g}} \mathrm{~d} \sigma_{\mathbb{S}_{t}^{n-1}}$$
In our setting, we prefer to use the latter formula.
To continue, we introduce the Yamabe constant of an AF manifold ( $N^{n}, g$ ), $n \geq 3$ by
$$Y(N,[\hat{g}]):=\inf _{u \in C_{c}^{\infty}(N) \backslash\{0\}} \frac{\int_{N} \frac{4(n-1)}{n-2}\left|\nabla_{g} u\right|^{2}+R_{g} u^{2} \mathrm{~d} V_{g}}{\left(\int_{N}|u|^{\frac{2 n}{n-2}} \mathrm{~d} V_{g}\right)^{\frac{n-2}{n}}} .$$
In [2], the authors proved the following fourth-order positive energy theorem.
Theorem A ([2, Theorem 4]). Let $\left(N^{n}, g\right)$ be an AF manifold of asymptotic order $\tau>\frac{n-4}{2}$ and regularity order $\ell=4$, with $n \geq 5$. Assume that (a) $Q_{g} \geq 0$ and $Y(N,[g])>0$; (b) $Q_{g} \in L^{1}(N, g)$. Then $\mathrm{m}_{4}(g) \geq 0$, with equality if and only if $(N, g)$ is isometric to the flat Euclidean space $\mathbb{R}^{n}$.

To prove Theorem 4, let $M \subset \mathbb{R}^{n+1}$ be a cloded embedded hypersurface and $Q \in M$ is umbilical. As before, let $\hat{M}=M \backslash\{Q\}$ and $\hat{g}=\rho^{-2} g$. Then it is in fact the induced Riemannian metric on $I_{Q}(M \backslash Q) \subset \mathbb{R}^{n+1}$.

Proof of Theorem 4 As in Section 3, write $M$ as a graph of a smooth function $f$ near $Q$. If $f(x)=\phi(x)+A_{k}+O\left(r^{k+1}\right)$ for $k \geq 3$, then the calculations in Section 3 indicate that
$$\hat{g}=\rho^{-2} g=\rho^{-2}\left(|\mathrm{~d} x|^{2}+\mathrm{d} f \otimes \mathrm{~d} f\right)=|\mathrm{d} y|^{2}+O\left(|y|^{-k}\right) .$$

We use the same adapted asymptotic coordinates as in (3.1) and (3.2):
$$y=\frac{\lambda}{2} \frac{x}{\phi(x)} \quad \Longleftrightarrow \quad x=\frac{y}{\frac{\lambda^{2}}{4}+|y|^{2}},$$
and agian denote $r=|x|, t=|y|$. By the inductive estimates (2.12) and (2.2) we know that
$$R_{\hat{g}}=O\left(r^{2 k}\right)=O\left(t^{-2 k}\right) .$$
Observe that
$$\begin{aligned}
\Delta_{\hat{g}} R_{\hat{g}} & =\hat{g}^{\alpha \beta} \frac{\partial^{2} R_{\hat{g}}}{\partial y_{\alpha} \partial y_{\beta}}-\hat{g}^{\alpha \beta} \hat{\Gamma}_{\alpha \beta}^{\gamma} \frac{\partial R_{\hat{g}}}{\partial y_{\gamma}} \\
& =\left(\delta_{\alpha \beta}+O\left(t^{-k}\right)\right) \frac{\partial^{2} R_{\hat{g}}}{\partial y_{\alpha} \partial y_{\beta}}+\hat{g}^{\alpha \beta} O\left(t^{-k-1}\right) O\left(t^{-2 k-1}\right) \\
& =\sum_{\alpha} \frac{\partial^{2} R_{\hat{g}}}{\partial y_{\alpha}^{2}}+O\left(t^{-3 k-2}\right) .
\end{aligned}$$
Here we also used Remark 3. To adopt the Einstein summation convention, we write the main term as $\frac{\partial^{2} R_{\hat{\delta}}}{\partial y_{\alpha}^{2}}$. A direct computation yields
$$\begin{aligned}
\frac{\partial x_{\beta}}{\partial y_{\alpha}} \frac{\partial x_{\gamma}}{\partial y_{\alpha}} & =\frac{\delta_{\beta \gamma}}{\left(\frac{\lambda^{2}}{4}+t^{2}\right)^{2}}-\frac{\lambda^{2} y_{\beta} y_{\gamma}}{\left(\frac{\lambda^{2}}{4}+t^{2}\right)^{4}} \\
& =t^{-4} \delta_{\beta \gamma}+O\left(t^{-6}\right) \\
& =r^{4} \delta_{\beta \gamma}+O\left(r^{6}\right)
\end{aligned}$$
and
$$\begin{aligned}
\frac{\partial^{2} x_{\beta}}{\partial y_{\alpha}^{2}} & =-(2 n+4) \frac{y^{\beta}}{\left(\frac{\lambda^{2}}{4}+t^{2}\right)^{2}}+\frac{8 t^{2} y^{\beta}}{\left(\frac{\lambda^{2}}{4}+t^{2}\right)^{3}} \\
& =(4-2 n) \frac{t^{2} y^{\beta}}{\left(\frac{\lambda^{2}}{4}+t^{2}\right)^{3}}-\frac{n+2}{2} \frac{\lambda^{2} y^{\beta}}{\left(\frac{\lambda^{2}}{4}+t^{2}\right)^{3}} \\
& =(4-2 n) r^{2} x_{\beta}+O\left(r^{5}\right) .
\end{aligned}$$
Hence, putting these facts together we obtain
$$\begin{aligned}
\sum_{\alpha} \frac{\partial^{2} R_{\hat{g}}}{\partial y_{\alpha}^{2}} & =\frac{\partial^{2} R_{\hat{g}}}{\partial x_{\beta} \partial x_{\gamma}} \frac{\partial x_{\beta}}{\partial y_{\alpha}} \frac{\partial x_{\gamma}}{\partial y_{\alpha}}+\frac{\partial R_{\hat{g}}}{\partial x_{\beta}} \frac{\partial^{2} x_{\beta}}{\partial y_{\alpha}^{2}} \\
& =r^{4} \Delta R_{\hat{g}}+(4-2 n) r^{2} x_{\alpha} \partial_{\alpha} R_{\hat{g}}+O\left(r^{2 k+4}\right) .
\end{aligned}$$
Notice that $2 k+4 \leq 3 k+2$ for $k \geq 3$. This in turn implies that
$$\Delta_{\hat{g}} R_{\hat{g}}=r^{4} \Delta R_{\hat{g}}+(4-2 n) r^{2} x_{\alpha} \partial_{\alpha} R_{\hat{g}}+O\left(r^{2 k+4}\right) .$$

For simplicity, we introduce
$$B_{2 k-4}:=4 n(n-1)(k-1)^{2} \frac{A_{k}^{2}}{r^{4}}-4(n-1)(k-1) \frac{A_{k}}{r^{2}} \Delta A_{k}+\left(\Delta A_{k}\right)^{2}-\left|\nabla^{2} A_{k}\right|^{2},$$
which is a homogeneous polynomial of degree $2 k-4$. Then we have
$$R_{\hat{g}}=r^{4} B_{2 k-4}+O\left(r^{2 k+1}\right)$$
again by (2.12) and (2.2). Consequently, these together with (5.2), (5.1), (1.2) lead to
$$\begin{aligned}
Q_{\hat{g}} & =-\frac{1}{2(n-1)} \Delta_{\hat{g}} R_{\hat{g}}+O\left(t^{-2 k-4}\right) \\
& =-\frac{1}{2(n-1)}\left(r^{4} \Delta\left(r^{4} B_{2 k-4}\right)+(4-2 n) r^{2} x_{\alpha} \partial_{\alpha}\left(r^{4} B_{2 k-4}\right)\right)+O\left(r^{2 k+4}\right) .
\end{aligned}$$

Now we need the following technical lemma.
Lemma 6. Suppose we have
$$Q_{\hat{g}}=q(\theta)|x|^{2 \ell+2}+o\left(|x|^{2 \ell+2}\right),$$
with $q(\theta)$ not identically zero. Then $Q_{\hat{g}} \in L^{1}(\hat{M}, \hat{g})$ if and only if $\ell>\frac{n-2}{2}$.
Proof. Since $\rho=r^{2}(1+o(1))$, we have
$$\left|Q_{\hat{g}}\right| \mathrm{d} V_{\hat{g}}=r^{2 \ell+2}(1+o(1)) \rho^{-n} \mathrm{~d} V_{g}=r^{2 \ell+2-2 n}(1+o(1)) \mathrm{d} V_{g} .$$
Then the remaining proof is identical to that of Lemma 1 \(\square\)

Since initially $k \geq 3$, we automatically obtain that $Q_{\hat{g}}=q(\theta)|x|^{2 \ell+2}+o\left(|x|^{2 \ell+2}\right)$ for some $\ell \geq 3$ by (5.4). Hence a direct consequence of Lemma 6 is that $Q_{\hat{g}} \in L^{1}(M, \hat{g})$ when $5 \leq n \leq 7$.

Next we assume $n \geq 8$ and fix $3 \leq k \leq \frac{n-2}{2}$. Since $Q_{\hat{g}} \in L^{1}(\hat{M}, \hat{g})$, by Lemma 6 and (5.4) we have
$$\begin{aligned}
0 & =r^{2} \Delta\left(r^{4} B_{2 k-4}\right)+(4-2 n) x_{\alpha} \partial_{\alpha}\left(r^{4} B_{2 k-4}\right) \\
& =r^{2}\left[\left(\Delta r^{4}\right) B_{2 k-4}+2 \nabla r^{4} \cdot \nabla B_{2 k-4}+r^{4} \Delta B_{2 k-4}\right]+(4-2 n) \cdot 2 k r^{4} B_{2 k-4} \\
& =r^{4}\left[r^{2} \Delta B_{2 k-4}+(24 k+4 n-4 k n-24) B_{2 k-4}\right] \\
& =r^{4}\left[r^{2} \Delta B_{2 k-4}-4(n-6)(k-1) B_{2 k-4}\right] .
\end{aligned}$$
This implies $r^{2} \mid B_{2 k-4}$.
By induction, we assume that $B_{2 k-4}=r^{2 l} p(x)$ for $2 l \leq 2 k-4$ and $l \geq 0$. A direct calculation yields
$$\frac{1}{r^{2 l-2}} \Delta B_{2 k-4} \equiv 2 l(n+4 k-2 l-10) p(x) \quad \bmod r^{2}$$
and then
$$\begin{aligned}
0 & =\frac{1}{r^{2 l}}\left[r^{2} \Delta B_{2 k-4}-4(n-6)(k-1) B_{2 k-4}\right] \\
& \equiv[2 l(n+4 k-2 l-10)-4(n-6)(k-1)] p(x) \bmod r^{2} \\
& \equiv-2(2 k-2-l)(n-6-2 l) p(x) \bmod r^{2} .
\end{aligned}$$
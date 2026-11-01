---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Green function rigidity and the mass of hypersurfaces under inversion]

We first notice that $2 k-2-l \geq l+2 \geq 2$ as $2 l \leq 2 k-4$.
When $2 l \leq 2 k-6, n-2 l-6 \geq n-2 k>0$, then $r^{2} \mid p(x)$. So, $r^{2 l+2} \mid B_{2 k-4}$. In particular $r^{2 k-4} \mid B_{2 k-4}$ implies $B_{2 k-4}=c r^{2 k-4}$ for some $c \in \mathbb{R}$. When $2 l=2 k-4$, we already have $B_{2 k-4}=c r^{2 k-4}$. Consequently, in all cases we have $B_{2 k-4}=c r^{2 k-4}$.

For clarity we let $A_{k}(x)=r^{2 i} p(x), 0 \leq i \leq \frac{k}{2}$, and we distinguish two cases:
\begin{itemize}
\item[(1)] If $n=2 k+2$, then we use the same calculation as in (2.15) together with the definition of $B_{2 k-4}$ to conclude that
$$\begin{aligned}
c r^{n-4 i-2} & =4 n(n-1)(k-1)^{2} \frac{A_{k}^{2}}{r^{4 i}}-4(n-1)(k-1) \frac{A_{k}}{r^{2 i}} \frac{\Delta A_{k}}{r^{2 i-2}}+\frac{1}{r^{4 i-4}}\left[\left(\Delta A_{k}\right)^{2}-\left|\nabla^{2} A_{k}\right|^{2}\right] \\
& \equiv 4(k-i-1)[(k-i-1)(n-4 i)(n-1)+2 i(k-2 i)] \tilde{p}^{2}(x) \bmod r^{2} .
\end{aligned}$$
Notice that the coefficient of $\tilde{p}^{2}(x)$ is nonzero. When $i<\frac{k}{2}$, we have $r^{2} \mid \tilde{p}^{2}(x)$ and hence $r^{2} \mid \tilde{p}(x)$, that is, $r^{2 i+2} \mid A_{k}$. To continue, we further distinguish it by two cases.
\begin{itemize}
\item[(i)] If $k=2 j-1$ for $j \geq 2$ and $n=4 j$, then we apply (5.5) with $i=j-1$ to show that $r^{2 j} \mid A_{k}$, which implies $A_{k}=0$.
\item[(ii)] If $k=2 j$ for $j \geq 2$ and $n=4 j+2$, then letting $i=j-1$ in (5.5) we obtain
$$4 j[6(n-1) j+4(j-1)] \tilde{p}^{2}(x) \equiv 0 \quad \bmod r^{2} .$$
This implies $r^{2} \mid \tilde{p}^{2}(x)$ and then $r^{2} \mid \tilde{p}(x)$. Eventually, we have $A_{k}=\tilde{\kappa} r^{2 j}=$ $\tilde{\kappa} r^{\frac{n-2}{2}}$ for some $\tilde{\kappa} \in \mathbb{R}$.
\end{itemize}
\item[(2)] If $n \neq 2 k+2$, then $n-2 l-6 \neq 0$. So, the same argument above gives $r^{2 k-2} \mid B_{2 k-4}$ and then $B_{2 k-4}=0$. This together with (5.5) yields $\tilde{p}^{2}(x) \equiv 0 \bmod r^{2}$, which implies $r^{2} \mid \tilde{p}(x)$ and then $r^{2 i+2} \mid A_{k}$. So, we repeat the procedure up to $k=\left\lfloor\frac{n}{2}\right\rfloor-1$ and obtain $\left.r^{\left\lfloor\frac{n}{2}\right\rfloor} \right\rvert\, A_{k}=0$, which implies $A_{k}=0$.
\end{itemize}

Therefore, collecting these facts together we arrive at
Proposition 4. If $n \geq 8$ and $Q_{\hat{g}} \in L^{1}(M, \hat{g})$, then near $Q$ we have
\begin{itemize}
\item[(i)] when $n \neq 4 j+2$ for $\left.j \geq 2, f(x)=\phi(x)+O\left(|x|^{\frac{n}{2}}\right\rfloor\right)$;
\item[(ii)] when $n=4 j+2$ for $j \geq 2, f(x)=\phi(x)+\tilde{\kappa}|x|^{\frac{n}{2}-1}+O\left(|x|^{\frac{n}{2}}\right), \tilde{\kappa} \in \mathbb{R}$.
\end{itemize}

To complete the proof of Theorem 4, we only need to determine the asymptotic order and to explicitly compute the fourth-order energy.
\begin{itemize}
\item[(1)] When $5 \leq n \leq 7$, then $f(x)=\phi(x)+O\left(|x|^{3}\right)$, and Lemma 3 yields that $(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order 3. Note that we do not need to worry about the regularity order in view of Remark 3 Since $R_{\hat{g}}=O\left(t^{-6}\right)$, we have
$$\begin{aligned}
\mathrm{m}_{4}(\hat{g}) & =-\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}} \partial_{t} R_{\hat{g}} \mathrm{~d} \sigma_{\mathbb{S}_{t}^{n-1}} \\
& =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}^{n-1}} O\left(t^{n-8}\right) \mathrm{d} \sigma \\
& =0
\end{aligned}$$
\item[(2)] When $n \neq 4 j+2$ for $j \geq 2$, by Proposition 4 (2.12) and (2.2) we obtain
$$R_{\hat{g}}=O\left(t^{-2 m}\right) \quad \text { with } \quad m=\left\lfloor\frac{n}{2}\right\rfloor .$$
Combing Proposition 4 and Lemma 3 yields that $(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order $\left\lfloor\frac{n}{2}\right\rfloor$. Hence, it is direct to calculate
$$\begin{aligned}
\mathrm{m}_{4}(\hat{g}) & =-\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}} \partial_{t} R_{\hat{g}} \mathrm{~d} \sigma_{\mathbb{S}_{t}^{n-1}} \\
& =\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}^{n-1}} O\left(t^{n-2 m-2}\right) \mathrm{d} \sigma \\
& =0
\end{aligned}$$
\item[(3)] When $n=4 j+2$, letting $i=\frac{n-2}{4}$ in (5.5) we obtain
$$c=\frac{(n-1)(n-6)^{2}}{2} \tilde{\kappa}^{2},$$
whence
$$R_{\hat{g}}=c t^{2-n}+O\left(t^{1-n}\right)$$
by (5.3). Similarly, Lemma 3 together with Proposition 4 yields that $(M \backslash\{Q\}, \hat{g})$ is asymptotically flat of order $\frac{n}{2}-1$. Then we have
$$\begin{aligned}
\mathrm{m}_{4}(\hat{g}) & =-\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}} \partial_{t} R_{\hat{g}} \mathrm{~d} \sigma_{\mathbb{S}_{t}^{n-1}} \\
& =-\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}^{n-1}}\left((2-n) c t^{1-n}+O\left(t^{-n}\right)\right) t^{n-1} \mathrm{~d} \sigma \\
& =\frac{(n-1)(n-2)(n-6)^{2}}{2} \tilde{\kappa}^{2} .
\end{aligned}$$
\end{itemize}
Hence the fourth-order energy is always non-negative and vanishes except for the case $n=4 j+2, j \geq 2$. This concludes the proof. \(\square\)

Now we use Theorem 4 to prove Theorem 5

Proof of Theorem 5 For $n \geq 5$ and $n \neq 4 j+2, j \geq 2$, let $\left(M^{n}, g\right)$ be a closed embedded hypersurface in $\mathbb{R}^{n+1}$ such that the Yamabe constant $Y(M,[g])>0$. Assume that for some point $Q$, the Green function for $P_{4}^{g}$ with pole $Q$ is of the form $c_{n, 2}\|\cdot-Q\|^{4-n}$. As before, let $\hat{M}=M \backslash\{Q\}$ and $\hat{g}=\rho^{-2} g$. Then by definition of the Green function for $P_{4}^{g}$, we know that $Q_{\hat{g}} \equiv 0$ and hence integrable. Finally, by Theorem 4, we have $\mathrm{m}_{4}(g)=0$

To apply the positive energy Theorem A, we need to show that $Y(\hat{M}, \hat{g})>0$.
Lemma 7. Under the assumption that $Y(M, g)>0$, we also have $Y(\hat{M}, \hat{g})>0$.
Proof. For clarity, we set $L_{g}=P_{2}^{g}$. Since $Y(M,[g])>0$, we let
$$\begin{aligned}
\bar{g} & =G_{L_{g}}(\cdot, Q)^{\frac{4}{n-2}} g \\
& =G_{L_{g}}(\cdot, Q)^{\frac{4}{n-2}} c_{n, 2}^{-\frac{4}{n-4}} \rho^{2} \hat{g} \\
& =\left(c_{n, 2}^{-1} \rho^{\frac{n-2}{2}} G_{L_{g}}(\cdot, Q)\right)^{\frac{4}{n-2}} \hat{g} .
\end{aligned}$$
Clearly, $R_{\bar{g}}=0$ on $M \backslash\{Q\}$. Notice that
$$\rho^{2-n}=r^{2-n}\left(1+O\left(r^{2}\right)\right)$$
by [6, Lemma 9] and
$$c_{n, 2}^{-1} G_{L_{g}}(\cdot, Q)=r^{2-n}\left(1+O\left(r^{2}\right)\right)$$
by Parker-Rosenberg [22, Theorem 2.2 and (4.4)], where $r=\mathrm{d}_{g}(\cdot, Q)$. Take
$$\phi=c_{n, 1}^{-1} \rho^{\frac{n-2}{2}} G_{L_{g}}(\cdot, Q)=1+O\left(r^{2}\right),$$
such that $\phi-1 \in W_{-\tau}^{2, p}(M \backslash\{Q\})^{3}$ for some $p>n / 2$ and all $\tau \in(0,2)$, and $R_{\phi^{4 /(n-2)} \hat{g}}=0$ on $M \backslash\{Q\}$. Thanks to Maxwell [19, Proposition 3 and Remark 1], we obtain $Y(\hat{M},[\hat{g}])>$ 0. \(\square\)

Now the positive energy Theorem A states that $(M \backslash\{Q\}, \hat{g})$ is isometric to $\left(\mathbb{R}^{n}, \delta\right)$. Consequently, by Lemma 5. $M$ is itself a round sphere.

In the remaining case $n=3$, we notice that $Y(M, g)>0$ by assumption and $G(\cdot, Q)=$ $c_{n, 2} \rho^{1 / 2} \leq 0$. Now we use the following conformal positive mass theorem due to Hang-Yang ${ }^{4}$

Proposition A ([11, Propositon 2.4]). Let $\left(M^{3}, g\right)$ be a close manifold such that $Y(M,[g]>$ 0 ) and $\operatorname{ker} P_{4}^{g}=\{0\}$. If the Green function of $P_{4}^{g}$ satisfies $G(\cdot, Q)<0$ for some $Q \in M$, then $G(Q, Q)<0$ unless ( $M, g$ ) is conformally equivalent to $\left(\mathbb{S}^{3}, g_{\mathbb{S}^{3}}\right)$.

Then it follows that $(M, g)$ is conformal to $\mathbb{S}^{3}$. \(\square\)

Remark 4. When $5 \leq n \leq 7$, since $Y(M,[g])>0$ by assumption, together with Proposition 6 we can adapt the approach of Gursky-Malchiodi [9] Theorem 2.9] to show that $\left(M \backslash\{Q\}, G(\cdot, Q)^{\frac{4}{n-4}} g\right)$ is isometric to the flat Euclidean space $\mathbb{R}^{n}$. This gives an alternative proof in the lower dimensions.

\footnotetext{
${ }^{3}$ See [19] p.566] for the definition of $W_{-\tau}^{2, p}(M \backslash\{Q\})$.
${ }^{4}$ Since Hang-Yang's proof also hinges on the Green function for the conformal Laplacian, the assumption $Y(M,[g])>0$ is implicitly needed.
}

\section*{A A generalization of Reilly formula for entire graphs}

As another application of Proposition 3, we generalize the result due to Reilly [24, Proposition 4.1] for $\sigma_{k}$ curvature of graphs in Euclidean spaces, which should be of independent interest. Although Reilly's formula is originally meaningful only for graphs, the following proposition shows that it is not the case.

Proposition 5. Let $M \subset \mathbb{R}^{n+1}$ be an oriented hypersurface with a unit normal vector field n. Let $\mathbf{e}$ be a constant vector field on $\mathbb{R}^{n+1}$ and let $v:=\mathbf{e}^{\top}$ be its tangential part along $M$. For $1 \leq k \leq n$, denote by $\sigma_{k}(\mathcal{S})$ the $k$-th elementary symmetric function of the shape operator $\mathcal{S}=-\nabla \mathbf{n}$ and by
$$T_{k-1}(\mathcal{S})_{\alpha}^{\beta}=\frac{\partial \sigma_{k}(\mathcal{S})}{\partial h_{\beta}^{\alpha}}$$
its ( $k-1$ )-th Newton transform. Then we have
$$k \sigma_{k}(\mathcal{S})\langle\mathbf{e}, \mathbf{n}\rangle=\operatorname{div}_{g}\left(i_{v} T_{k-1}(\mathcal{S})\right)^{\sharp} .$$
Proof. Since $T_{k-1}(\mathcal{S})$ is divergent-free, taking the symmetric 2-tensor $T_{\alpha \beta}=g_{\alpha \gamma} T_{k-1}(\mathcal{S})_{\beta}^{\gamma}$ in Proposition 3 yields the desired assertion. \(\square\)

Note that when $M$ is a graph of the form $\left\{(x, f(x)) \mid x \in U \subset \mathbb{R}^{n}\right\}$, if we take $\mathbf{e}=e_{n+1}$ in (A.1) and identify $\frac{\partial}{\partial x_{\alpha}}$ with $e_{\alpha}+f_{\alpha} e_{n+1}$ as above, thereby $e_{n+1}^{\top}=\frac{f_{\alpha}}{1+|\nabla f|^{2}} \frac{\partial}{\partial x_{\alpha}}$, and hence (A. 1 ) recovers Reilly's original result.

\section*{B Mass of Green function for Paneitz operator and $\mathrm{m}_{4}$}

We give an alternative proof of [2, Proposition 6], which characterizes the relation between the mass of the Green function $G(\cdot, Q)$ and $\mathrm{m}_{4}(\hat{g})$ for the asymptotic manifold $\left(M \backslash\{Q\}, \hat{g}:=G(\cdot, Q)^{\frac{4}{n-4}} g\right)$. Our proof is elementary and greatly simplifies the original proof in [2].

Proposition 6. Let $\left(M^{n}, g\right)$ be a closed manifold with $n=5,6,7$ or $(M, g)$ is locally conformally flat and $n \geq 8$. Suppose $(M, g)$ admits a positive Green function $G(\cdot, Q)$ for the Paneitz operator $P_{4}^{g}$. Then there is a conformal metric of $g$ (still denoted by itself) such that
$$\left(c_{n, 2}\right)^{-1} G(\cdot, Q)=r^{4-n}+\mathrm{A}+O(r), \quad r=|x|=\mathrm{d}_{g}(x, Q), \mathrm{A} \in \mathbb{R},$$
and $\mathrm{m}_{4}(\hat{g})=8(n-1)(n-2) A c_{n, 2}$ for $\hat{g}=G(\cdot, Q)^{\frac{4}{n-4}} g$. Here, $c_{n, 2}=\left(2(n-2)(n-4)\left|\mathbb{S}^{n-1}\right|\right)^{-1}$.
Proof. Under conformal normal coordinates around $Q$, for any $N>n+3$ we have
$$\operatorname{det} g=1+O\left(r^{N}\right), \quad R_{g}=O\left(r^{2}\right)$$
and from Gursky-Malchiodi [9, Theorem 2.9] or Hang-Yang [10, Proposition 2.1] that the expansion of $G(\cdot, Q)$ around $Q$ is given by
$$c_{n, 2}^{-1} G(\cdot, Q)=r^{4-n}+\mathrm{A}+O(r) .$$

The readers refer to Lee-Parker [18] for the basics of the conformal normal coordinates.
In the following, we normalize $c_{n, 2}=1$.
Consider the asymptotically flat manifold $\left(\hat{M}:=M \backslash\{Q\}, \hat{g}=G(\cdot, Q)^{\frac{4}{n-4}} g\right)$. For $n=$ 5, 6, 7, under inverted coordinates $y=x|x|^{-2}$ with $t=|y|=r^{-1}$, we have
$$\hat{g}_{\alpha \beta}(y)=\gamma(y)^{\frac{4}{n-4}}\left(\delta_{\alpha \beta}+O\left(t^{-2}\right)\right),$$
where
$$\gamma(y)=1+\mathrm{A} t^{4-n}+O\left(t^{3-n}\right) .$$
This means that $(\hat{M}, \hat{g})$ is asymptotically flat of order $\tau=1$ for $n=5$ and of order $\tau=2$ for $n=6,7$; if ( $M, g$ ) is locally conformally flat and $n \geq 8$, then we may take $g_{i j}=\delta_{i j}$ near $Q$, thereby $(\hat{M}, \hat{g})$ is asymptotically flat of order $\tau=n-4$. So, in both cases $\mathrm{m}_{4}(\hat{g})$ is well defined.

By definition of the fourth-order energy we have
$$\mathrm{m}_{4}(\hat{g})=-\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{t \rightarrow \infty} \int_{\mathbb{S}_{t}^{n-1}} \partial_{t} R_{\hat{g}} \mathrm{~d} \sigma_{\mathbb{S}_{t}^{n-1}}=\frac{1}{\left|\mathbb{S}^{n-1}\right|} \lim _{r \rightarrow 0} \int_{\mathbb{S}^{n-1}} r^{3-n} \partial_{r} R_{\hat{g}} \mathrm{~d} \sigma .$$

Write $\hat{g}=G^{\frac{4}{n-4}} g=\left(G^{\frac{n-2}{n-4}}\right)^{\frac{4}{n-2}} g$. Then the scalar curvature equation gives
$$R_{\hat{g}}=G^{-\frac{n+2}{n-4}}\left(-\frac{4(n-1)}{n-2} \Delta_{g} G^{\frac{n-2}{n-4}}+R_{g} G^{\frac{n-2}{n-4}}\right) .$$

For any radial function $u=u(r)$ we have
$$\Delta_{g} u=\Delta u+O\left(r^{N-1}\right) u^{\prime},$$
where $\Delta=\partial_{r}^{2}+\frac{n-1}{r} \partial_{r}$. Observe that
$$\Delta_{g} G^{\frac{n-2}{n-4}}=\frac{n-2}{n-4} r^{1-n} \partial_{r}\left(r^{n-1} G^{\frac{2}{n-4}} G^{\prime}\right)+O\left(r^{N-1}\right) G^{\frac{2}{n-4}}\left|G^{\prime}\right|=-2(n-2) \mathrm{A} r^{-4}+O\left(r^{-3}\right) .$$
This follows that
$$-\frac{4(n-1)}{n-2} G^{-\frac{n+2}{n-4}} \Delta_{g} G^{\frac{n-2}{n-4}}=8(n-1) \mathrm{A} r^{n-2}+O\left(r^{n-1}\right) .$$
Also we obtain
$$R_{g} G^{-\frac{4}{n-4}}=O\left(r^{6}\right) .$$
Hence, inserting these estimates into (B. 1 ) yields $\mathrm{m}_{4}(\hat{g})=8(n-1)(n-2) \mathrm{A}$. \(\square\)

Remark 5. In [5] Proposition 2.1(c)], Hou and the first named author proved that there is a mass of the Green function for $P_{6}^{g}$ provided that $\left(M^{n}, g\right)$ is locally conformally flat and $n \geq 10$ or $n=7,8,9$.

\section*{References}
\begin{itemize}
\item[] [1] R. Arnowitt, S. Deser and C. Misner, Coordinate invariance and energy expressions in general relativity, Physical Review, 112 (1961), 997-1006.
\item[] [2] R. Avalos, P. Laurain and J. Lira, A positive energy theorem for fourth-order gravity, Calc. Var. Partial Differential Equations 61 (2022), no. 2, Paper No. 48, 33 pp.
\item[] [3] R. Bartnik, The mass of an asymptotically flat manifold, Comm. Pure Appl. Math. 34 (1986), 661-693.
\item[] [4] J. Case and A. Gover, The GJMS operators in geometry, analysis and physics, J. Lond. Math. Soc. (2) 113 (2026), no. 1, Paper No. e70375, 21 pp.
\item[] [5] X. Chen and F. Hou, Remarks on GJMS operator of order six, Pacific J. Math. 289 (2017), no. 1, 35-70.
\item[] [6] X. Chen and Y. Shi, Green functions for GJMS operators on spheres, Gegenbauer polynomials and rigidity theorems, arxiv:2401.02087.
\item[] [7] M. Gursky, F. Hang and Y. Lin, Riemannian manifolds with positive Yamabe invariant and Paneitz operator, Int. Math. Res. Not. IMRN 2016, no. 5, 1348-1367.
\item[] [8] C.R. Graham, R. Jenne, L. Mason and G. Sparling, Conformally invariant powers of the Laplacian, I: existence, J. London Math. Soc. (2) 46 (1992), no.3, 557-565.
\item[] [9] M. Gursky and A. Malchiodi, A strong maximum principle for the Paneitz operator and a non-local flow for the Q-curvature, J. Eur. Math. Soc. (JEMS) 17 (2015), no. 9, 2137-2173.
\item[] [10] F. Hang and P. Yang, Q-curvature on a class of manifolds with dimension at least 5, Comm. Pure Appl. Math. 69 (2016), no. 8, 1452-1491.
\item[] [11] F. Hang and P. Yang, Q curvature on a class of 3-manifolds, Comm. Pure Appl. Math. 69 (2016), no. 4, 734-744.
\item[] [12] F. Hang and P. Yang, Sign of Green's function of Paneitz operators and the Q-curvature, Int. Math. Res. Not. IMRN 2015, no. 19, 9775-9791.
\item[] [13] P. Hartman and L. Nirenberg, On spherical image maps whose Jacobians do not change sign, Amer. J. Math. 81 (1959), 901-920.
\item[] [14] L. Huang and D. Wu, The equality case of the Penrose inequality for asymptotically flat graphs,Trans. Amer. Math. Soc. 367 (2015), no. 1, 31-47.
\item[] [15] E. Humbert and S. Raulot, Positive mass theorem for the Paneitz-Branson operator, Calc. Var. Partial Differential Equations 36 (2009), no.4, 525-531.
\item[] [16] M. Lai and C. Zhang, Green function rigidity for two dimensional sphere, arXiv:2601.03773.
\end{itemize}
\begin{itemize}
\item[] [17] M. Lam, The Graph Cases of the Riemannian Positive Mass and Penrose Inequalities in All Dimensions, ProQuest LLC, Ann Arbor, MI, 2011. Thesis (Ph.D.)-Duke University.
\item[] [18] J. Lee and T. Parker, The Yamabe problem, Bull. Amer. Math. Soc. (N.S.) 17 (1987), no. 1, 37-91.
\item[] [19] D. Maxwell, Solutions of the Einstein constraint equations with apparent horizon boundaries, Comm. Math. Phys. 253 (2005), no. 3, 561-583.
\item[] [20] B. Michel, Masse des opérateurs GJMS, arXiv:1012.4414.
\item[] [21] S. Paneitz, A quartic conformally covariant differential operator for arbitrary pseudo-Riemannian manifolds, preprint, 1983. See also, SIGMA Symmetry Integrability Geom. Methods Appl. 4 (2008), Paper 036, 3 pp.
\item[] [22] T. Parker and S. Rosenberg, Invariants of conformal Laplacians, J. Differential Geometry, 25(1987), no.2, 199-222.
\item[] [23] T. Parker and C. Taubes, On Witten's proof of the positive energy theorem, Comm. Math. Phys. 84 (1982), no. 2, 223-238.
\item[] [24] R. Reilly, On the Hessian of a function and the curvatures of its graph, Michigan Math. J. 20 (1973), 373-383.
\item[] [25] R. Schoen, Conformal deformation of a Remannian metric to constant scalar curvature, J. Differential Geom. 20 (1984), no. 2, 479-495.
\item[] [26] R. Schoen, Variational theory for the total scalar curvature functional for Riemannian metrics and related topics, Topics in calculus of variations (Montecatini Terme, 1987), 120-154. Lecture Notes in Math., 1365.
\item[] [27] R. Schoen and S.-T. Yau, On the proof of the positive mass conjecture in general relativity, Comm. Math. Phys. 65 (1979), no. 1, 45-76.
\item[] [28] G. Wang, L. Weng and C. Xia, Alexandrov-Fenchel inequalities for convex hypersurfaces in the half-space with capillary boundary, Math. Ann. 388(2024), 2121-2154.
\item[] [29] E. Witten, A new proof of the positive energy theorem, Comm. Math. Phys. 80 (1981), no. 3, 381-402.
\end{itemize}
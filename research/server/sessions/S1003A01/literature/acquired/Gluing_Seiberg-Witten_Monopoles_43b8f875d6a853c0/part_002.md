---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Gluing Seiberg-Witten Monopoles]

For the first component, we have
$$q\left(\psi_{1}\right)-q\left(\psi_{2}\right)=b\left(\psi_{1}+\psi_{2}, \psi_{1}-\psi_{2}\right),$$
where $b$ denotes the symmetric bilinear form associated to $q$ and its pointwise norm is bounded above by $\left|b\left(\psi_{1}+\psi_{2}, \psi_{1}-\psi_{2}\right)\right| \leq 2\left|\psi_{1}+\psi_{2}\right|\left|\psi_{1}-\psi_{2}\right|$. Therefore,
$$\begin{aligned}
\left\|q\left(\psi_{1}\right)-q\left(\psi_{2}\right)\right\|_{1,-\delta} & \leq 2\left\|\psi_{1}+\psi_{2}\right\|_{L_{1,-\delta}^{4}}\left\|\psi_{1}-\psi_{2}\right\|_{L_{1,-\delta}^{4}} \\
& \leq 2 e^{2 \frac{\delta}{4} \ell}\left\|\psi_{1}+\psi_{2}\right\|_{L_{1,-2 \delta}^{4}}\left\|\psi_{1}-\psi_{2}\right\|_{L_{1,-2 \delta}^{4}} \\
& \leq \tilde{c}_{1} e^{\delta \ell}\left\|\psi_{1}+\psi_{2}\right\|_{2,-\delta}\left\|\psi_{1}-\psi_{2}\right\|_{2,-\delta} .
\end{aligned}$$
For the second component, we similarly write
$$\begin{aligned}
\left\|a_{1} \cdot \psi_{1}-a_{2} \cdot \psi_{2}\right\|_{1,-\delta} & =\left\|a_{1}\left(\psi_{1}-\psi_{2}\right)+\left(a_{1}-a_{2}\right) \psi_{2}\right\|_{1,-\delta} \\
& \leq\left\|a_{1}\right\|_{L_{1,-\delta}^{4}}\left\|\psi_{1}-\psi_{2}\right\|_{L_{1,-\delta}^{4}}+\left\|\psi_{2}\right\|_{L_{1,-\delta}^{4}}\left\|a_{1}-a_{2}\right\|_{L_{1,-\delta}^{4}} \\
& \leq e^{2 \frac{\delta}{4} \ell}\left(\left\|a_{1}\right\|_{L_{1,-2 \delta}^{4}}\left\|\psi_{1}-\psi_{2}\right\|_{L_{1,-2 \delta}^{4}}+\left\|\psi_{2}\right\|_{L_{1,-2 \delta}^{4}}\left\|a_{1}-a_{2}\right\|_{L_{1,-2 \delta}^{4}}\right) \\
& \leq \tilde{c}_{2} e^{\delta \ell}\left(\left\|a_{1}\right\|_{2,-\delta}\left\|\psi_{1}-\psi_{2}\right\|_{2,-\delta}+\left\|\psi_{2}\right\|_{2,-\delta}\left\|a_{1}-a_{2}\right\|_{2,-\delta}\right) .
\end{aligned}$$
So, to finish the estimates on the components, we need estimates on the $L_{2,-\delta}^{2}$-norms of $a_{i}$ and $\psi_{i}$, for $i=1,2$, as well as the differences $a_{1}-a_{2}$ and $\psi_{1}-\psi_{2}$. First, note that $\left(a_{i}, \psi_{i}\right)=\mathcal{R}\left(\zeta_{i}\right)$ for $i=1,2$, so that each of $\left\|a_{i}\right\|_{2,-\delta}$ and $\left\|\psi_{i}\right\|_{2,-\delta}$ is bounded above by
$$\left\|\mathcal{R}\left(\zeta_{i}\right)\right\|_{2,-\delta} \leq C e^{\delta \ell / 2}\left\|\zeta_{i}\right\|_{1,-\delta} .$$
Similarly, $a_{1}-a_{2}$ and $\psi_{1}-\psi_{2}$ are the two components of $\mathcal{R}\left(\zeta_{1}\right)-\mathcal{R}\left(\zeta_{2}\right)$, so that both of $\left\|a_{1}-a_{2}\right\|_{2,-\delta}$ and $\left\|\psi_{1}-\psi_{2}\right\|_{2,-\delta}$ are bounded above by
$$\left\|\mathcal{R}\left(\zeta_{1}\right)-\mathcal{R}\left(\zeta_{2}\right)\right\|_{2,-\delta} \leq\left\|D_{\zeta} \mathcal{R}\right\| .\left\|\zeta_{1}-\zeta_{2}\right\|_{1,-\delta} \leq C e^{\delta \ell / 2}\left\|\zeta_{1}-\zeta_{2}\right\|_{1,-\delta} .$$
These inequalities, in conjunction with estimates 3.4 and 3.5, show that for $\zeta_{1}, \zeta_{2}$ in a ball $B(0, R)$ of radius $R$, we have
$$\begin{aligned}
& \left\|q\left(\psi_{1}\right)-q\left(\psi_{2}\right)\right\|_{1,-\delta} \leq 2 \tilde{c}_{1} C^{2} R e^{2 \delta \ell}\left\|\zeta_{1}-\zeta_{2}\right\|_{1,-\delta} \\
& \left\|a_{1} \cdot \psi_{1}-a_{2} \cdot \psi_{2}\right\|_{1,-\delta} \leq 2 \tilde{c}_{2} C^{2} R e^{2 \delta \ell}\left\|\zeta_{1}-\zeta_{2}\right\|_{1,-\delta} .
\end{aligned}$$
Combining with Equation 3.3, we obtain
$$\left\|\mathcal{F}\left(\zeta_{1}\right)-\mathcal{F}\left(\zeta_{2}\right)\right\|_{1,-\delta} \leq \tilde{c} R e^{2 \delta \ell}\left\|\zeta_{1}-\zeta_{2}\right\|_{1,-\delta}$$
for some constant $\tilde{c}$ and $\mathcal{F}$ will be a $\frac{1}{2}$-contraction for $R=\frac{1}{2 \tilde{c}} e^{-2 \delta \ell}$.
Now, the unique fixed point of $\mathcal{F}$ can be obtained by finding the limit of the iterations of any point in the ball. Therefore, the sequence of iterations $\left\{\mathcal{F}^{\circ n}(0)\right\}$ converges to the fixed point $\hat{\zeta}$ and we have
$$\|\hat{\zeta}\|_{1,-\delta} \leq 2\|\mathcal{F}(0)\|_{1,-\delta} \leq 2 \tilde{C} e^{-\left(\kappa+\frac{\delta}{2}\right)\left(\ell-2 L_{0}\right)} .$$
From here, the estimates claimed in the theorem on $\|\hat{\zeta}\|$ and $\|\mathcal{R}(\hat{\zeta})\|$ follow. Finally, to estimate the norm of $\mathcal{R}(\hat{\zeta})^{\prime}=\mathcal{R}^{\prime}(\hat{\zeta})+\mathcal{R}\left(\hat{\zeta}^{\prime}\right)$, we need to estimate $\left\|\hat{\zeta}^{\prime}\right\|_{1,-\delta}$ first. To avoid complicated notation, we will write $\hat{\zeta}$ for $\left.\hat{\zeta}(t)\right|_{t=0}$ and $\hat{\zeta}^{\prime}$ for $\left.\frac{d}{d t} \hat{\zeta}(t)\right|_{t=0}$. We will also consider the one-parameter family of operators $\mathcal{F}_{t}=\mathcal{F}\left(\boldsymbol{\xi}^{+}(t), \boldsymbol{\xi}^{-}(t)\right)$ and write $\mathcal{F}$ for $\mathcal{F}(0)$ and $\mathcal{F}^{\prime}$ for the $t$-derivative of $\mathcal{F}_{t}$ at $t=0$. Similar notation was already used in the case of $\mathcal{R}$ and $\mathcal{R}^{\prime}$ at the beginning of this paragraph.
By $t$-differentiating the fixed point equation $\mathcal{F}_{t}(\hat{\zeta}(t))=\hat{\zeta}(t)$ at $t=0$, we obtain
$$D_{\zeta} \mathcal{F}\left(\hat{\zeta}^{\prime}\right)+\mathcal{F}^{\prime}(\hat{\zeta})=\hat{\zeta}^{\prime} .$$
(To see this, write $\mathcal{F}_{t}=\mathcal{F}+t \mathcal{F}^{\prime}+o\left(t^{2}\right)$ and $\hat{\zeta}(t)=\hat{\zeta}+t \hat{\zeta}^{\prime}+o\left(t^{2}\right)$, then substitute in the fixed point equation and find the coefficient of $t$. Note that $\mathcal{F}$ is not a linear map, so the coefficient of $t$ in $\mathcal{F}\left(t \hat{\zeta}^{\prime}\right)$ is $D_{\zeta} \mathcal{F}\left(\hat{\zeta}^{\prime}\right)$.)
We can rewrite the last equation as $\left(\mathrm{I}-D_{\zeta} \mathcal{F}\right)\left(\hat{\zeta}^{\prime}\right)=\mathcal{F}^{\prime}(\hat{\zeta})$. Since $\mathcal{F}$ is a contraction, $\left\|D_{\zeta} \mathcal{F}\right\| \leq \frac{1}{2}$, so $\mathrm{I}-D_{\zeta} \mathcal{F}$ is invertible and $\left\|\left(\mathrm{I}-D_{\zeta} \mathcal{F}\right)^{-1}\right\| \leq 2$. Therefore,
$$\left\|\hat{\zeta}^{\prime}\right\|_{1,-\delta} \leq 2\left\|\mathcal{F}^{\prime}(\hat{\zeta})\right\|_{1,-\delta} .$$
On the other hand, as in the preceding arguments, we find
$$\left\|\mathcal{F}^{\prime}(\hat{\zeta})\right\|_{1,-\delta} \leq C^{\prime} e^{\delta \ell}\left\|\mathcal{R}^{\prime}(\hat{\zeta})\right\|_{2,-\delta}\|\mathcal{R}(\hat{\zeta})\|_{2,-\delta}+\left\|\operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)^{\prime}\right\|_{1,-\delta} .$$
We, moreover, have
$$\left\|\mathcal{R}^{\prime}(\hat{\zeta})\right\|_{2,-\delta}\|\mathcal{R}(\hat{\zeta})\|_{2,-\delta} \leq C^{\prime} e^{\delta \ell}\left(\left\|\left(\boldsymbol{\xi}^{+}\right)^{\prime}\right\|+\left\|\left(\boldsymbol{\xi}^{-}\right)^{\prime}\right\|\right)\|\hat{\zeta}\|_{1,-\delta}^{2} .$$
Combining the last two inequalities and using the estimate on $\left\|\mathrm{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)^{\prime}\right\|_{1,-\delta}$ (cf. Proposition 3.1) and the facts $\delta<\kappa$ and $\ell>4 L_{0}$, we see that, for some constant $C^{\prime}$,
$$\left\|\mathcal{F}^{\prime}(\hat{\zeta})\right\|_{1,-\delta} \leq C^{\prime} e^{-(\kappa+\delta / 2)\left(\ell-2 L_{0}\right)}\left(\left\|\left(\boldsymbol{\xi}^{+}\right)^{\prime}\right\|+\left\|\left(\boldsymbol{\xi}^{-}\right)^{\prime}\right\|\right)$$
and, using (3.9), we get, for some $C^{\prime}$,
$$\left\|\hat{\zeta}^{\prime}\right\|_{1,-\delta} \leq C^{\prime} e^{-(\kappa+\delta / 2)\left(\ell-2 L_{0}\right)}\left(\left\|\left(\boldsymbol{\xi}^{+}\right)^{\prime}\right\|+\left\|\left(\boldsymbol{\xi}^{-}\right)^{\prime}\right\|\right) .$$
Now, using the equation $\mathcal{R}(\hat{\zeta})^{\prime}=\mathcal{R}^{\prime}(\hat{\zeta})+\mathcal{R}\left(\hat{\zeta}^{\prime}\right)$, the estimates on the norms of $\hat{\zeta}$ and $\hat{\zeta}^{\prime}$ (Equations 3.8 and 3.10) and the estimates on the operator norms $\|\mathcal{R}\|$ and $\left\|\mathcal{R}^{\prime}\right\|$ (Proposition 3.11 and its following remark) gives the desired estimate on $\left\|\mathcal{R}(\hat{\zeta})^{\prime}\right\|_{2,-\delta}$. \(\square\)

We are now in the final stage of gluing. Recall that we started with a couple of solutions $\boldsymbol{\xi}^{+}$and $\boldsymbol{\xi}^{-}$on $X^{+}$and $X^{-}$, respectively. They solved $\operatorname{SW}\left(\boldsymbol{\xi}^{ \pm}\right)=$ 0 . Then, we truncated and glued these solutions, using a partition of unity, to obtain an approximate solution $\tilde{\boldsymbol{\xi}}_{\ell}$. Set $\boldsymbol{\xi}_{\ell}=\tilde{\boldsymbol{\xi}}_{\ell}+\mathcal{R}(\hat{\zeta})$, where $\mathcal{R}: \mathcal{E}^{2}\left(X_{\ell}\right) \rightarrow$ $\mathcal{E}^{1}\left(X_{\ell}\right)$ is the right inverse of $\mathcal{D}^{1}$ constructed before (Proposition 3.11) and $\hat{\zeta}=(\hat{\alpha}, \hat{s}) \in \mathcal{E}^{2}\left(X_{\ell}\right)=\Omega_{+, 1}^{2}\left(X_{\ell} ; i \mathbb{R}\right) \oplus \Gamma_{1}\left(S^{-}\right)$is the unique fixed point of $\mathcal{F}$ of Proposition 3.12. As we have
$$\operatorname{SW}(\boldsymbol{\xi}+\xi)=\operatorname{SW}(\boldsymbol{\xi})+\mathcal{D}^{1}(\xi)+\left(-q(\psi), \frac{1}{2} a . \psi\right),$$
where $\xi=(a, \psi)$, we obtain $\operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}+\mathcal{R}(\hat{\zeta})\right)=0$, so $\boldsymbol{\xi}_{\ell}$ is a solution of SW.

\section*{4. Acknowledgments.}

This work is based on the author's PhD dissertation [12]. Special thanks go to John Morgan, Cumrun Vafa, Seif Randjbar Daemi and Ramadas Ramakrishnan for encouraging the author for its publication, as well as to the Abdus Salam ICTP for kind hospitality and partial support while this article was under evaluation.

\section*{References.}
\begin{itemize}
\item[] [1] A. L. Carey, M. Marcolli, and B. L. Wang. The geometric triangle for 3-dimensional Seiberg-Witten monopoles. Commun. Contemp. Math., 5(2):197-250, 2003. arXiv: math.DG/9907065, MR 1966258.
\item[] [2] Alan L. Carey and Bai Ling Wang. Seiberg-Witten-Floer homology and gluing formulae. Acta Math. Sin. (Engl. Ser.), 19(2):245-296, 2003. arXiv: math.GT/0206047, MR 1987794.
\item[] [3] Weimin Chen. The seiberg-witten theory of homology 3-spheres. unpublished preprint, arXiv: dg-ga/9703009.
\end{itemize}
\begin{itemize}
\item[] [4] Ronald Fintushel and Ronald J. Stern. Knots, links, and 4-manifolds. Invent. Math., 134(2):363-400, 1998. MR 99j:57033.
\item[] [5] Dosang Joe. Symplectic structures on connected sums with a ruled surface and product formulas for Seiberg-Witten invariants along a nilmanifold. PhD thesis, Columbia Univerity, 1998.
\item[] [6] P. B. Kronheimer and T. S. Mrowka. The genus of embedded surfaces in the projective plane. Math. Res. Lett., 1(6):797-808, 1994. MR 96a:57073.
\item[] [7] John W. Morgan. The Seiberg-Witten equations and applications to the topology of smooth four-manifolds, volume 44 of Mathematical Notes. Princeton University Press, Princeton, NJ, 1996. MR 97d:57042.
\item[] [8] John W. Morgan, Tomasz Mrowka, and Daniel Ruberman. The $L^{2}$ -moduli space and a vanishing theorem for Donaldson polynomial invariants. Monographs in Geometry and Topology, II. International Press, Cambridge, MA, 1994. MR 95h:57039.
\item[] [9] John W. Morgan and Tomasz S. Mrowka. On the gluing theorem for instantons on manifolds containing long cylinders. unpublished preprint.
\item[] [10] John W. Morgan, Zoltán Szabó, and Clifford Henry Taubes. A product formula for the Seiberg-Witten invariants and the generalized Thom conjecture. J. Differential Geom., 44(4):706-788, 1996. MR 97m:57052.
\item[] [11] Tomasz Mrowka, Peter Ozsváth, and Baozhen Yu. Seiberg-Witten monopoles on Seifert fibered spaces. Comm. Anal. Geom., 5(4):685-791, 1997. arXiv: math.GT/9612221, MR 98m:58017.
\item[] [12] Pedram Safari. A gluing theorem for Seiberg-Witten moduli spaces. PhD thesis, Columbia Univerity, 2000.
\item[] [13] Clifford Henry Taubes. The Seiberg-Witten and Gromov invariants. Math. Res. Lett., 2(2):221-238, 1995. MR 96a:57076.
\item[] [14] Clifford Henry Taubes. Seiberg Witten and Gromov invariants for symplectic 4-manifolds, volume 2 of First International Press Lecture Series. International Press, Somerville, MA, 2000. Edited by Richard Wentworth. MR 2002j:53115.
\end{itemize}

School of Mathematics
Institute for Studies in Theoretical Physics and Mathematics (IPM)
P.O. Box 19395-5746
Niavaran, Tehran, Iran
E-mail address: safari@ipm.ir
Received June 4, 2004.
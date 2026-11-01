# On 4-dimensional Ricci-flat ALE manifolds

- Category: papers
- Identity: arxiv:2304.01609
- Content status: fulltext_ok

---

---
source_file: 2304_01609.pdf
converter: mathpix
format: mmd
---

\section*{ON 4-DIMENSIONAL RICCI-FLAT ALE MANIFOLDS}

MINGYANG LI

Abstract. In this paper, we prove:
\begin{itemize}
\item[-] There is a one-to-one correspondence between:
\begin{itemize}
\item[-] Hermitian non-Kähler ALE gravitational instantons $(M, h)$;
\item[-] Bach-flat Kähler orbifolds $(\widehat{M}, \widehat{g})$ of complex dimension 2 with exactly one orbifold point $q$, such that the scalar curvature $s_{\hat{g}}$ satisfies $s_{\hat{g}}(q)=0$ while being positive elsewhere.
\end{itemize}
\item[-] There is no Hermitian non-Kähler ALE gravitational instanton with structure group contained in SU(2), except for the Eguchi-Hanson metric with reversed orientation.
\end{itemize}
A 4-dimensional Ricci-flat metric being Hermitian non-Kähler is equivalent to being non-trivially conformally Kähler.

Contents
\begin{itemize}
\item[1.] Introduction
\item[2.] Preliminary results
\item[3.] Compactification
\item[4.] Holomorphic vector fields and minimal resolutions
\item[5.] Log del Pezzo surfaces with holomorphic vector fields
\item[6.] Case (iii)
\item[7.] The $\mathcal{A}$-functional and Bach-flat Kähler metrics
\end{itemize}
Appendix A. Proof of Theorem 4.6
References
1. Introduction

The following question is a long-standing problem:
Question 1.1. Is there an ALE Ricci-flat 4-manifold that is neither self-dual nor anti-self-dual?
In this paper, we refer to complete non-compact Ricci-flat 4-manifolds $(M, h)$ with $\int_{M}\left|R m_{h}\right|_{h}^{2}<\infty$ as gravitational instantons. It is a famous conjecture by Bando-Kasue-Nakajima [1, 18] that any ALE gravitational instanton is either self-dual or anti-self-dual. In this paper, we give a negative answer to the problem introduced at the beginning in a special case. By saying that a 4-manifold $(M, h)$ is asymptotically locally Euclidean (ALE), we mean

Definition 1.2. A Riemannian 4-manifold $(M, h)$ is ALE with order $\tau$, if there is a smooth diffeomorphism $\Phi$ : $M \backslash K \rightarrow\left(\mathbb{R}^{4} \backslash \overline{B_{R}(0)}\right) / \mathrm{Y}$, where $K$ is a large compact subset of $M$ and $\mathrm{Y} \subset S O(4)$ is a finite group acting freely on $S^{3}$, such that
$$\left|\nabla_{h}^{k}\left(h-\Phi^{*} h_{E}\right)\right|_{h}=O\left(\rho^{-\tau-k}\right)$$
as $\rho \rightarrow \infty$ for any $k \geq 0$. Here $\rho$ is the distance function under $h$ to some base point $p, h_{E}$ is the standard Euclidean metric on $\mathbb{R}^{4} / \mathrm{Y}$, and $\nabla_{h}$ is the Levi-Civita connection of $h$.

There is the following curvature decomposition for oriented 4-manifolds by identifying the curvature tensor $R m$ as an automorphism of the bundle of two-forms $\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-}$
$$\operatorname{Rm}=\left(\begin{array}{cc}
\frac{s}{12}+W^{+} & \operatorname{Ric}^{0} \\
\operatorname{Ric}^{0} & \frac{s}{12}+W^{-}
\end{array}\right) .$$
Here $s$ is the scalar curvature, $W^{ \pm}$are the self-dual and anti-self-dual Weyl curvatures, and Ric ${ }^{0}$ is the trace-less Ricci curvature. In particular, for oriented Einstein 4-manifolds, we only have the scalar curvature part $s$ and the Weyl curvature part $W^{ \pm}$. Locally the self-dual Weyl curvature $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$is a $3 \times 3$ matrix. By the work of Derdziński [5], oriented Einstein 4-manifolds can be broadly classified into the following three cases.

Definition-Proposition. An oriented Einstein 4-manifold $(M, h)$ can be classified into one of the following types:
\begin{itemize}
\item[-] Type I: If $W^{+} \equiv 0$, then the metric is anti-self-dual.
\item[-] Type II: If $W^{+}$has exactly two distinct eigenvalues, treated as an automorphism $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$everywhere, then up to passing to a double cover ${ }^{1}$, there exists a compatible complex structure $J$ such that $(M, h, J)$ is Hermitian and the conformal metric $g=\lambda^{2 / 3} h$ is Kähler, where $\lambda=2 \sqrt{6}\left|W^{+}\right|_{h}$. The scalar curvature $s_{g}$ of $g$ satisfies $\left|s_{g}\right|=\lambda^{1 / 3}$.
\item[-] Type III: If $W^{+}$generically has three distinct eigenvalues, then $(M, h)$ is not locally conformally Kähler under this orientation.
\end{itemize}

Type I ALE gravitational instantons are precisely the anti-self-dual ALE gravitational instantons. A very important class of such gravitational instantons are those hyperkähler ones, which are completely classified by Kronheimer [11, 10]. Finite quotients of hyperkähler gravitational instantons, which are still Type I, are also classified by [4, 21].

For Type II ALE gravitational instantons, after passing to a double cover if necessarily, they are precisely the Hermitian non-Kähler ALE gravitational instantons. It turns out that the conformal metric $g=\lambda^{2 / 3} h$ is not only Kähler, but also Bach-flat, and extremal Kähler in the sense of Calabi. Note that in the complex 2-dimensional case, a Bach-flat Kähler metric is automatically extremal Kähler [14].

This paper focuses on Type II (equivalently, after passing to the cover being Hermitian non-Kähler) ALE gravitational instantons, specifically proving the following two main theorems.

Theorem 1.3. There is a one-to-one correspondence between:
\begin{itemize}
\item[-] Hermitian non-Kähler ALE gravitational instantons (M, h);
\item[-] Bach-flat Kähler orbifolds ( $\widehat{M}, \widehat{g}$ ) of complex dimension 2 with exactly one orbifold point $q$, whose scalar curvature $s_{\widehat{g}}$ satisfies $s_{\widehat{g}}>0$ except at $q$ while $s_{\widehat{g}}(q)=0$.
\end{itemize}

The structure group of a Hermitian non-Kähler ALE gravitational instanton must be contained in U(2), in the sense that outside of a suitable compact set, the end is biholomorphic to $\mathrm{B}^{*} / \Gamma$, where $\mathrm{B}^{*} \subset \mathbb{C}^{2}$ is the standard punctured unit ball and $\Gamma \subset U(2)$.

Theorem 1.4. With the exception of the Eguchi-Hanson metric with reversed orientation, there are no Hermitian non-Kähler ALE gravitational instantons with structure group contained in SU(2).

Note that the group $\Gamma$ in Theorem 1.3 is different from the group Y in Definition 1.2-they are conjugate as subgroups of $S O(4)$. We shall refer to the group $\Gamma$ as the structure group. Here the Eguchi-Hanson space is usually understood as a hyperkähler space. However, it turns out that it also carries a complex structure whose orientation is opposite to the hyperkähler orientation. The metric is Hermitian non-Kähler under this complex structure with opposite orientation. Metrics corresponding to Hermtian non-Kähler ALE gravitational instantons in Theorem 1.3 will be refered to as special Bach-flat Kähler metrics for simplicity.
Definition 1.5. A Bach-flat Kähler metric $\widehat{g}$ on a compact complex 2-dimensional orbifold with only one orbifold point $q$ is said to be special Bach-flat Kähler, if its scalar curvature $s_{\widehat{g}}$ is positive at all points except at the orbifold point $q$, where $s_{\widehat{g}}(q)=0$.

Now we explain some main ideas in the proof:
\begin{itemize}
\item[-] For a Hermitian non-Kähler ALE gravitational instanton $(M, h)$, with $\lambda:=2 \sqrt{6}\left|W^{+}\right|_{h}$, the extremal Kähler metric $g:=\lambda^{2 / 3} h$ turns out to be incomplete, whose metric completion is just adding one point. Using a singularity removal argument, we can show that $g$ extends to a smooth orbifold extremal Kähler metric $\widehat{g}$ (Section 3.2). The metric $\widehat{g}$ is the special Bach-flat Kähler metric in the correspondence of Theorem 1.3.
\item[-] Denote the compactified special Bach-flat Kähler orbifold as $(\widehat{M}, \widehat{g})$. In Section 3.3, it is shown that $\widehat{M}$ is a log del Pezzo surface, which is a Fano surface with only one quotient singularity. This is proved based on an important observation by LeBrun [12]. We therefore conclude that the compactified surface $\widehat{M}$ must be rational.
\item[-] Each special Bach-flat Kähler orbifold gives us a pair $(\widehat{M}, \mathfrak{E})$, where $\widehat{M}$ is the underlying orbifold and $\mathfrak{E}$ is the holomorphic extremal vector field associated to the extremal Kähler metric $\widehat{g}$. Such pairs have the following algebraic properties:
\end{itemize}

\footnotetext{
${ }^{1}$ It was pointed out by Claude LeBrun to the author that one should include passing to a double cover here. The author is very grateful for that.
}
\begin{itemize}
\item[-] The orbifold $\widehat{M}$ has only one orbifold point $q$.
\item[-] The orbifold $\widehat{M}$ is log del Pezzo.
\item[-] The orbifold point $q$ is an isolated fixed point of the action by $\mathfrak{E}$. Moreover, the weights of the $\mathfrak{E}$ action on the tangent space of $q$ are the same.
\end{itemize}

It will be an algebraic geometry problem to classify all such pairs with the above algebraic properties, and we classify them under the additional technical assumption that the orbifold group $\Gamma \subset \operatorname{SU}(2)$. Importantly, we find that there exist only a finite number of such pairs when the orbifold group is in $S U(2)$. This is done in Section 5-6.
\begin{itemize}
\item[-] These classified pairs $(\widehat{M}, \mathfrak{E})$ are candidates for special Bach-flat Kähler orbifolds with structure group in $S U(2)$. If an extremal Kähler metric exists with $\mathfrak{E}$ as the holomorphic extremal vector field on these candidates, we will show in Section 7 that the minimum of its scalar curvature can never be zero, except for the pair corresponding to the Eguchi-Hanson metric with reversed orientation. Together with Theorem 1.3, this proves Theorem 1.4.
\end{itemize}

Note that in the smooth setting, the holomorphic extremal vector field of an extremal Kähler metric always generates a holomorphic $\mathbb{C}^{*}$-action, as a consequence of [9]. Theorem 1.3, 1.4 have several interesting corollaries. During the course of our proof of the main theorems, we also prove

Corollary 1.6 (Finiteness of topological types). For each fixed finite subgroup $\Gamma \subset U(2)$, there exist at most finitely many diffeomorphism types of Hermitian non-Kähler ALE gravitational instantons with structure group $\Gamma$.

We will discuss later that we actually expect that there is no Type II ALE gravitational instanton at all, except for the Eguchi-Hanson metric with reversed orientation. We also have the following corollary which will be established during the proof of Theorem 1.3
Corollary 1.7. For a Hermitian ALE gravitational instanton, if its self-dual Weyl curvature $W^{+}$decays faster than $\rho^{-6}$, then it must be Kähler.

Relating to previous works, compact 4-dimensional Hermitian Einstein metrics are classified by LeBrun [13]. Le-Brun's work [12, 13] has shown that compact Hermitian Einstein 4-manifolds are limited to being either Kähler-Einstein, the Page metric in [19], or the Chen-LeBrun-Weber metric in [3]. Our Theorem 1.3 and 1.4 can be treated as a non-compact analogue of [3, 13].

It is important to note that proving the non-existence of Hermitian non-Kähler ALE gravitational instantons with structure group not in $S U(2)$ requires a classification of log del Pezzo surfaces with only one $U(2)$ singularity and a holomorphic vector field $\mathfrak{E}$ having the same weights at the singularity point. While the case-by-case classification we will use for the $\operatorname{SU}(2)$ case can be extended to the U(2) case, it will be more complicated. Unlike the $\operatorname{SU}(2)$ case, the $U(2)$ case may yield an infinite number of candidates $(\widehat{M}, \mathfrak{E})$. Given the difficulty in achieving the condition that the scalar curvature of the Bach-flat Kähler metric vanishes precisely at the orbifold point, we make the following conjecture:

Conjecture 1.8. There exist no Hermitian non-Kähler ALE gravitational instantons, without any restrictions on the structure group, except for the Eguchi-Hanson metric with reversed orientation.

We finally would like to remark that very little is currently known about general ALE gravitational instantons. Lock and Viaclovsky [16] showed that if the minimal resolution of $\mathbb{C}^{2} / \Gamma$ with $\Gamma \subset U(2)$ or its further blow-up supports a Ricci-flat ALE metric, then $\Gamma \subset \operatorname{SU}(2)$ and the metric is hyperkähler, through some topological calculation based on the Hitchin-Thorpe inequality. In Biquard-Hein [2], they constructed an optimal ALE coordinate and an associated renormalized volume, and showed that the renormalized volume has to be nonpositive. This volume is zero if and only if the Ricci-flat manifold is a flat cone $\mathbb{R}^{4} / \Gamma$. It is notable that our result in this paper is based on complex-analytic method. To solve the problem we mentioned at the beginning, the difficulty enssentially lies in

Question 1.9. Is there a Type III ALE gravitational instanton?
Notations.
\begin{itemize}
\item[-] On a Riemannian manifold $(M, h)$ with a chosen base point $p, \rho$ denotes the distance function to $p$.
\item[-] If $T$ is a tensor on $(M, h)$, then we say that $T=O_{h}^{\prime}\left(\rho^{-\tau}\right)$ if, for any integer $k \geq 0$,
$$\left|\nabla_{h}^{k} T\right|_{h}=O\left(\rho^{-\tau-k}\right),$$
as $\rho$ approaches infinity. We will omit $h$ when it is clear from the context.
\end{itemize}
\begin{itemize}
\item[-] Given a holomorphic vector field $\mathfrak{E}$, by flows of this vector field, we mean the flows of the real vector field Re E.
\item[-] We will use $H_{r}$ to denote the Hirzebruch surface $\mathbb{P}(\mathcal{O} \oplus \mathcal{O}(r))$.
\item[-] For an extremal Kähler metric $g$, by extremal vector field we mean $J \nabla_{g} s_{g}$. By holomorphic extremal vector field we mean $\nabla_{g}^{1,0} s_{g}$.
\end{itemize}

Acknowledgement. I would like to express my sincere gratitude to my advisor, Song Sun, for introducing me to this problem and for providing constant support throughout the course of my research. I am grateful for his willingness to engage in fruitful discussions and for generously sharing his ideas with me. I would like to extend my thanks to Junsheng Zhang for providing me with a helpful example. I am grateful to Bing Wang for his warm hospitality during my visit to the Institute of Geometry and Physics at USTC, where this work was completed. I am thankful to Gonçalo Oliveira for pointing out a mistake in an earlier version of this paper.

This work is supported by NSF grant DMS-2004261 and Simons Collaboration Grant on Special Holonomy in Geometry, Analysis, and Physics (488633, S.S.).

\section*{2. Preliminary results}

In this section we introduce the Type I-III classification by Derdziński [5] metioned in the introduction.
Proposition 2.1 (Derdziński). For an oriented Einstein 4-manifold (M, h), it must be of Type I, Type II, or Type III.
Proof. Let $\mu, v$, and $\eta$ be the three eigenvalues of $W^{+}$(some of which possibly could coincide). The function $\Delta:=$ $(\mu-v)(v-\eta)(\eta-\mu)$ is well-defined and real analytic because Einstein metrics are real analytic. Therefore, we must have either $\Delta \neq 0$ and $W^{+}$has three distinct eigenvalues generically, or $\Delta \equiv 0$ and $W^{+}$has at most two distinct eigenvalues everywhere. If the second case happens, Proposition 5 in [5] implies that we either have $W^{+} \equiv 0$, or $W^{+}$ has exactly two distinct eigenvalues everywhere which are both nowhere vanishing. \(\square\)

Proposition 2.2 (Derdziński). Let $(M, h)$ be an oriented Einstein 4-manifold that is of Type II. Then up to passing to a double cover, there exists a complex structure $J$ on $M$ such that $(M, h, J)$ is Hermitian and conformally Kähler. The conformal metric $g=\lambda^{2 / 3} h$ is Kähler under $J$, where
$$\lambda=2 \sqrt{6}\left|W^{+}\right|_{h} .$$
It turns out that the scalar curvature $s_{g}$ of $g$ satisfies $\left|s_{g}\right|=\lambda^{1 / 3}$. The function $\lambda$ is positive everywhere because $W^{+} \neq 0$ everywhere.

Proof. This proposition follows from Proposition 5 in [5]. We briefly outline the construction of $J$ for the reader's convenience. Since $(M, h)$ is of Type II, $W^{+}$has exactly two distinct eigenvalues at every point, and due to its tracelessness, two of its three eigenvalues coincide. Derdziński proved that the eigen-2-forms $\pm \omega$ of $W^{+}$corresponding to the eigenvalue with multiplicity one, normalized to have unit length under $g$, are parallel with respect to the metric $g$. Passing to a double cover if necessary, one can pick a global eigen-two-form $\omega$. Now the eigen-2-form $\omega$ serves as the Kähler form, and together with $g$, determine the complex structure $J$. \(\square\)

The next lemma, which was first discovered by Goldberg and Sachs, shows that if an Einstein 4-dimensional metric is Hermitian but non-ASD, then it must be Type II.

Lemma 2.3 (Goldberg-Sachs). Let $(M, h, J)$ be a Hermitian Einstein 4-manifold, with the orientation given by the complex structure $J$. Then the self-dual Weyl curvature $W^{+}$of $h$ must be $J$-invariant, hence $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$has at most two distinct eigenvalues at every point of $M$.

Now we move to Hermitian non-Kähler ALE gravitational instantons. Note that as a general fact the decay order $\tau$ is always at least 4.

Theorem 2.4 (Bando-Kasue-Nakajima). Let $(M, h)$ be a 4-dimensional Ricci-flat manifold with Euclidean volume growth and finite $\int_{M}\left|R m_{h}\right|_{h}^{2}$, then ( $M, h$ ) is ALE with order 4.

Let us next briefly discuss the associated Kähler metric $g$. Recall that for a Hermitian non-Kähler ALE gravitational instanton $(M, h)$, we define $\lambda:=2 \sqrt{6}\left|W^{+}\right|_{h}$, and the Kähler metric is given by $g=\lambda^{2 / 3} h$. Straightforward calculation shows $\left|s_{g}\right|=\lambda^{1 / 3}>0$. By looking at the conformal change of scalar curvature equation and examining it at the maximum/minimum of $s_{g}$, it follows $s_{g}>0$, therefore $s_{g}=\lambda^{1 / 3}$. As the Kähler metric $g$ is conformal to a Ricciflat metric, it is Bach-flat Kähler, which therefore is extremal Kähler in the sense of Calabi [14]. In this case, $(M, g)$
automatically possesses a Killing field $J \nabla_{g} s_{g}$. Since it preserves the conformal factor $\lambda^{1 / 3}, J \nabla_{g} s_{g}$ is also Killing with respect to $(M, h)$.

Proposition 2.5. The vector field $\mathcal{K}=J \nabla_{g} \lambda^{1 / 3}$ is a Killing field with respect to $g$, hence also a Killing field with respect to $h$.

From basic calculations, we find that $\mathcal{K}=-J \nabla_{h} \lambda^{-1 / 3}$. Due to the decay of the Riemannian curvature, the conformal factor $\lambda=2 \sqrt{6}\left|W^{+}\right|_{h}$ decays as $\lambda=O_{h}^{\prime}\left(\rho^{-6}\right)$ as $\rho \rightarrow \infty$. Note $J \nabla_{g} s_{g}$ is the imaginary part of the holomorphic extremal vector field
$$J \nabla_{g} s_{g}=-2 \operatorname{Im} \nabla_{g}^{1,0} s_{g} .$$

Next we introduce the Eguchi-Hanson metric but with reversed orientation, which is an example of Type II ALE gravitational instanton.

Example 2.6 (Eguchi-Hanson). The Eguchi-Hanson metric was constructed in [7]. Let $\sigma_{x}, \sigma_{y}, \sigma_{z}$ be left-invariant orthogonal coframes for the sphere $S^{3}$. The Eguchi-Hanson metric can be explicitly written down as
$$h=\frac{1}{1-\left(\frac{a}{r}\right)^{4}} d r^{2}+r^{2}\left(\sigma_{x}^{2}+\sigma_{y}^{2}+\left(1-\left(\frac{a}{r}\right)^{4}\right) \sigma_{z}^{2}\right)$$
with $r>a$, and the entire metric is obtained by considering the metric completion. With the following orthonormal basis
$$e^{0}=\sqrt{\frac{1}{1-\left(\frac{a}{r}\right)^{4}}} d r, e^{1}=r \sigma_{x}, e^{2}=r \sigma_{y}, e^{3}=r \sqrt{\left(1-\left(\frac{a}{r}\right)^{4}\right)} \sigma_{z}$$
and orientation given by $-e^{0} \wedge e^{1} \wedge e^{2} \wedge e^{3}$, the self-dual Weyl curvature was calculated in [7] as
$$W^{+}=\left(\begin{array}{ccc}
-\frac{2 a^{4}}{r^{6}} & & \\
& -\frac{2 a^{4}}{r^{6}} & \\
& & \frac{4 a^{4}}{r^{6}}
\end{array}\right) .$$
Here we are using $e^{1} \wedge e^{0}+e^{2} \wedge e^{3}, e^{2} \wedge e^{0}+e^{3} \wedge e^{1}, e^{3} \wedge e^{0}+e^{1} \wedge e^{2}$ as a basis for $\Lambda^{+}$. So it is clear that the metric with this orientation is of Type II. The complex structure is given by $J: e^{0} \rightarrow e^{3}, e^{2} \rightarrow e^{1}$. The function $\lambda$ is $\lambda=2 \sqrt{6}\left|W^{+}\right|=24 \frac{a^{4}}{r^{6}}$. The conformal metric $g=\lambda^{2 / 3} h$ is Kähler and is incomplete. The scalar curvature of $g$ is $s_{g}=\lambda^{1 / 3}=2 \sqrt[3]{3 a^{4}} \frac{1}{r^{2}}$, which is decaying to 0. Under the complex structure $J$, the Eguchi-Hanson space as a complex surface is $\mathcal{O}(2)$. It can be compactified to the Hirzebruch surface $H_{2}=\mathbb{P}(\mathcal{O} \oplus \mathcal{O}(2))$ by adding a curve $C_{\infty}=\mathbb{P}^{1}$ with self-intersection -2 at infinity, and this divisor can be contracted to an orbifold point with orbifold group $\mathbb{Z}_{2}$. The orbifold $\widehat{M}$ we get after the contraction is log del Pezzo, and the Kähler metric $g$ extends to $\widehat{M}$ as an orbifold Kähler metric $\widehat{g}$. The pair $(\widehat{M}, \widehat{g})$ is the corresponding special Bach-flat Kähler orbifold for the Eguchi-Hanson space with reversed orientation, appearing in Theorem 1.3.

\section*{3. Compactification}

In this section, for a Hermitian non-Kähler gravitational instanton $(M, h)$, we prove that the conformal Kähler space $(M, g)$ can be naturally compactified to a Kähler orbifold by adding one point. This establishs the correspondence stated in Theorem 1.3.
3.1. Metric completion and lower bound on the Killing field $\mathcal{K}$. By fixing an ALE coordinate for the Hermitian non-Kähler gravitational instanton ( $M, h$ ), it is easy to conclude that there is an Euclidean Killing field $\mathcal{K}_{\infty}$ on $\mathbb{R}^{4} / \mathrm{Y}$, such that $\mathcal{K}-\mathcal{K}_{\infty}=O^{\prime}\left(\rho^{-3}\right)$. The rate can be chosen as 3 since the rate of $h$ asymptotic to the Euclidean metric is at least 4 by Bando-Kasue-Nakajima. The norm of the Killing field $\mathcal{K}=-J \nabla_{h} \lambda^{-1 / 3}$ at most grows like $\rho$ by basic comparison geometry over the ALE end. Integrating this from the base point $p$, one gets
$$\lambda^{-1 / 3}(x) \leq \lambda^{-1 / 3}(p)+\int_{p x}\left|\nabla_{h} \lambda^{-1 / 3}\right|_{h} \leq \lambda^{-1 / 3}(p)+C \int_{p x} \rho \leq C \rho^{2}(x)$$
for some constant $C$ when $\rho$ is large enough. This implies $\lambda \geq C \rho^{-6}$. With the curvature decay ensured by Bando-Kasue-Nakajima, it follows that
$$C_{1} \rho^{-6} \leq \lambda \leq C_{2} \rho^{-6}$$
holds on the end of $M$.
Proposition 3.1. The Euclidean Killing field $\mathcal{K}_{\infty}$ is nowhere vanishig.
Proof. We prove the proposition by contradiction. Suppose that the Euclidean Killing field $\mathcal{K}_{\infty}=\sum_{i, j} \alpha_{i j} x_{i} \frac{\partial}{\partial x_{j}}$ vanishes at some point. Then it must vanish along the entire ray, starting from origin passing through the point in $\mathbb{R}^{4} / \mathrm{Y}$. Along this ray we have
$$\nabla_{h} \lambda^{-1 / 3}=J \mathcal{K}_{\infty}+O\left(\rho^{-3}\right)=O\left(\rho^{-3}\right) .$$
Integrating (4), one gets that along this ray $\lambda^{-1 / 3} \leq C$, which contradicts the fact that $\lambda$ is decaying to 0. \(\square\)

Remark 3.2. Equation (3) implies the existence of constants $C_{1}$ and $C_{2}$ such that
$$C_{1} \rho^{-6} \leq\left|W^{+}\right|_{h} \leq C_{2} \rho^{-6} .$$
This result has an interesting consequence: if the self-dual Weyl curvature of a Hermitian ALE gravitational instanton decays faster than $\rho^{-6}$, then the manifold must be Kähler. This shows Corollary 1.7.

The bound (3) tells us that the conformal factor satisfies $C_{1} \rho^{-4} \leq \lambda^{2 / 3} \leq C_{2} \rho^{-4}$ at infinity, therefore the following proposition is a direct computation.

Proposition 3.3. The metric completion of $(M, g)$ is adding one point $q$ at infinity.
The metric completion will be denoted by $\widehat{M}=M \cup\{q\}$.
3.2. Removing singularity. In this subsection we derive estimates on the curvature tensor $R m_{g}$ of the Kähler metric $g$ near the added point $q$, in order to show that $g$ extends as a smooth orbifold metric across $q$. We define $r_{q}$ to be the distance function to $q$ in $\widehat{M}$ equipped with the length space structure induced by the metric $g$. A tensor $T$ on $\widehat{M} \backslash\{q\}$ is said to be $O_{g}^{\prime}\left(r_{q}^{\delta}\right)$ if for any integer $k \geq 0$, there exists a constant $C$ such that $\left|\nabla_{g}^{k} T\right|_{g} \leq C r_{q}^{\delta-k}$ near the added point $q$.

Theorem 3.4. The extremal Kähler metric $g$ on $M$ extends to a smooth extremal Kähler orbifold metric $\widehat{g}$ on $\widehat{M}$. The metric $\widehat{g}$ is Bach-flat.

The rest of this subsection is devoted to proving this theorem. Only need to show that $g$ can be extended smoothly. This theorem already establishes one direction of the correspondence in Theorem 1.3.

Proposition 3.5. $\left|R m_{g}\right|_{g}$ is bounded near $q$ and $\nabla_{g} R m_{g}=O_{g}^{\prime}\left(r_{q}\right)$.
Proof. Since the Riemannian curvature decomposes to the scalar curvature part, the traceless Ricci curvature part, and the Weyl curvature part, we only need to treat them separately. In the proof ∇ refers to the Levi-Civita connection of $g$. For the scalar curvature, $s_{g}=\lambda^{1 / 3}=O_{h}^{\prime}\left(\rho^{-2}\right)$. It is a direct calculation to check that $s_{g}=O_{g}^{\prime}\left(r_{q}^{2}\right)$ near $q$, and particularly it is bounded. For the Weyl curvature, $W=O_{h}^{\prime}\left(\rho^{-2}\right)$. Based on the conformal invariance of the Weyl curvature, it is again straightforward to compute that $W=O_{g}^{\prime}\left(r_{q}^{2}\right)$.

The estimate on the Ricci curvature however does not follow directly from the conformal change. The following computation was used by Tanno [20]. In dimension 4 we have
$$2 \nabla_{\alpha} W_{\beta \gamma \eta}^{\alpha}=\left(\nabla_{\eta} R_{\beta \gamma}-\nabla_{\gamma} R_{\beta \eta}\right)-\frac{1}{6}\left(g_{\beta \gamma} \nabla_{\eta} s_{g}-g_{\beta \eta} \nabla_{\gamma} s_{g}\right) .$$
Here $R_{\alpha \beta}$ is the Ricci curvature. This shows
$$\begin{aligned}
\nabla_{\eta} R_{\beta \gamma}-\nabla_{\gamma} R_{\beta \eta} & =2 \nabla_{\alpha} W_{\beta \gamma \eta}^{\alpha}+\frac{1}{6}\left(g_{\beta \gamma} \nabla_{\eta} s_{g}-g_{\beta \eta} \nabla_{\gamma} s_{g}\right) \\
& =O_{g}^{\prime}\left(r_{q}\right)
\end{aligned}$$
as a $(3,0)$ tensor. The Kähler condition gives that the Ricci curvature is $J$-invariant and the complex structure $J$ is parallel, so we have
$$\begin{aligned}
R_{\beta \gamma} & =R_{\mu v} J_{\beta}^{\mu} J_{\gamma}^{v} . \\
\nabla_{\alpha} R_{\beta \gamma} & =\nabla_{\alpha} R_{\mu v} J_{\beta}^{\mu} J_{\gamma}^{v} .
\end{aligned}$$

Therefore by applying (7),
$$\begin{aligned}
\nabla_{\alpha} R_{\beta \gamma} & =\nabla_{\beta} R_{\alpha \gamma}+O_{g}^{\prime}\left(r_{q}\right) \\
& =\nabla_{\beta} R_{\mu \nu} J_{\alpha}^{\mu} J_{\gamma}^{v}+O_{g}^{\prime}\left(r_{q}\right) \\
& =\nabla_{\mu} R_{\beta v} J_{\alpha}^{\mu} J_{\gamma}^{v}+O_{g}^{\prime}\left(r_{q}\right),
\end{aligned}$$
Similarly,
$$\nabla_{\alpha} R_{\beta \gamma}=\nabla_{\mu} R_{v \gamma} J_{\alpha}^{\mu} J_{\beta}^{v}+O_{g}^{\prime}\left(r_{q}\right) .$$
Combining (8), (9), and (10), we have
$$\begin{aligned}
\nabla_{\alpha} R_{\beta \gamma} & =\nabla_{\mu} R_{v \gamma} J_{\alpha}^{\mu} J_{\beta}^{v}+O_{g}^{\prime}\left(r_{q}\right) \\
& =\nabla_{\mu} R_{\phi \psi} J_{\nu}^{\phi} J_{\gamma}^{\psi} J_{\alpha}^{\mu} J_{\beta}^{v}+O_{g}^{\prime}\left(r_{q}\right) \\
& =\nabla_{\theta} R_{\phi \tau} J_{\mu}^{\theta} J_{\psi}^{\tau} J_{\nu}^{\phi} J_{\gamma}^{\psi} J_{\alpha}^{\mu} J_{\beta}^{v}+O_{g}^{\prime}\left(r_{q}\right) \\
& =-\nabla_{\alpha} R_{\beta \gamma}+O_{g}^{\prime}\left(r_{q}\right) .
\end{aligned}$$
Thus $\nabla_{\alpha} R_{\beta \gamma}=O_{g}^{\prime}\left(r_{q}\right)$ as a $(3,0)$ tensor, which shows the Ricci curvature of $g$ is also bounded near $q$. \(\square\)

Proposition 3.6. There are positive constants $V_{1}, V_{2}$ such that
$$V_{1} r^{4} \leq \operatorname{Vol}\left(B_{g}(q, r)\right) \leq V_{2} r^{4} .$$
Proof. This is because $g=\lambda^{2 / 3} h$ with $h$ ALE and $C_{1} \rho^{-6}<\lambda<C_{2} \rho^{-6}$. \(\square\)

Proposition 3.7. The tangent cone of $(\widehat{M}, g)$ at $q$ is unique, isometric to a Euclidean quotient $\mathbb{R}^{4} / \Gamma$. Moreover, the convergence to the tangent cone is in $C^{\infty}$ topology.

Proof. Propositions 3.5 and 3.6 imply that each tangent cone must be a flat cone, thus is isomorphic to some $\mathbb{R}^{4} / \Gamma$. The estimate $\left|\nabla_{g}^{k} R m_{g}\right|_{g}=O_{g}^{\prime}\left(r_{q}^{2-k}\right)$ shows that when we consider the rescaled spaces $\left(\widehat{M}, s_{i}^{-2} g, q\right)$ with $s_{i} \rightarrow 0$, the quantity $\left|\nabla_{s_{i}^{-2} g}^{k} R m_{s_{i}^{-2} g}\right|_{s_{i}^{-2} g}$ is uniformly bounded, from which we obtain the $C^{\infty}$ convergence to each tangent cone. \(\square\)

It is easy to see the specific relation between Y and $\Gamma$. Let $\mathbb{R}^{4} / \mathrm{Y}$ be equipped with the Euclidean metric $g_{\mathrm{Y}}$. Then the conformal metric $\frac{1}{r^{4}} g_{\mathrm{Y}}$ is again flat, with $r$ being the distance function to the origin. With the conformal flat metric $\frac{1}{r^{4}} g_{\mathrm{Y}}$, it is isometric to another Euclidean quotient (after completion), which is exactly $\mathbb{R}^{4} / \Gamma$. Denote by $B_{\Gamma}$ the standard metric ball in $\mathbb{R}^{4} / \Gamma$ with radius 1 and $B_{\Gamma}^{*}$ the corresponding punctured ball.

Proposition 3.8. There is a $C^{3}$ diffeomorphism $E: B_{\Gamma}^{*} \rightarrow B_{1}(q) \backslash\{q\}$, such that $E^{*} g$ extends to a $C^{1, \alpha}$ orbifold metric on $B_{\Gamma}$.

Proof. The information about the tangent cone already tells us we can find a smooth diffeomorphism $E^{\prime}: B_{\Gamma}^{*} \rightarrow$ $B_{1}(q) \backslash\{q\}$, such that $E^{\prime *} g$ extends to a $C^{0}$ orbifold metric. See Proposition 5.10 in [6]. Then with the bound on the Riemannian curvature, Proposition 5.14 in [6] gives us the desired $C^{3}$ diffeomorphism $E$. \(\square\)

From now on, by passing to the orbifold cover, we can always assume that we are working in the case where $\Gamma=\{e\}$. Since $g$ is $C^{1, \alpha}$, the complex structure, which is compatible with $g$, is also $C^{1, \alpha}$. The Newlander-Nirenberg integrability theorem says, modifying by a $C^{2, \alpha}$ diffeomorphism, the complex structure $J$ is standard near the point $q$, meaning that there is a $C^{2, \alpha}$ coordinates system near $q$ in which the complex structure is standard. In the following we will work in this standard complex coordinate.

Proposition 3.9. In the above complex coordinate, there are functions $f_{i}$ that are smooth in terms of the complex coordinate, such that $\frac{\partial g_{g}}{\partial \bar{z}_{j}}=f_{i} g_{i j}$. In particular, when $g_{i j}$ is $C^{p, \alpha}$ in the fixed complex coordinates system, $s_{g}$ is $C^{p+1, \alpha}$.

Proof. The Kähler metric $g$ is $C^{1, \alpha}$ in this complex coordinate. The holomorphic vector field $\nabla^{1,0} s_{g}=\frac{\partial s_{g}}{\partial \bar{z}_{j}} g^{i \bar{j}} \frac{\partial}{\partial z_{i}}$ in this coordinate can be extended across the origin by the Hartogs' theorem, since $\nabla s_{g}$ is bounded by Proposition 3.5. In particular, coefficients of this holomorphic vector field, $\frac{\partial s_{g}}{\partial \bar{z}_{j}} g^{i \bar{j}}$, must be $C^{\infty}$ functions in this coordinate system. From this, setting $f_{i}=\frac{\partial s_{g}}{\partial \bar{z}_{j}} g^{i \bar{j}}$, one gets $\frac{\partial s_{g}}{\partial \bar{z}_{k}}=f_{i} g_{i \bar{k}}$. The proposition follows. \(\square\)

Next we improve the regularity of the metric around the point $q$. Proposition 3.8 already shows that we can treat $g$ as a $C^{1, \alpha}$ metric on $B_{1}(q)$. We fix a base Kähler metric $h_{i \bar{j}}$ that is smooth in the complex coordinate. Then the scalar curvature $s\left(h_{i \bar{j}}+\varphi_{i \bar{j}}\right)$ of any Kähler metric $h_{i \bar{j}}+\varphi_{i \bar{j}}$ can be computed via
$$\begin{gathered}
\operatorname{det}\left(h_{i \bar{j}}+\varphi_{i \bar{j}}\right)=e^{F} \operatorname{det}\left(h_{i \bar{j}}\right), \\
s\left(h_{i \bar{j}}+\varphi_{i \bar{j}}\right)=-\Delta_{\varphi} F+\operatorname{tr}_{\varphi} \operatorname{Ric}(h) .
\end{gathered}$$
Here, $\Delta_{\varphi}$ denotes the the Laplace operator of the Kähler metric $h_{i \bar{j}}+\varphi_{i \bar{j}}$.
Proposition 3.10. For $p \geq 3, C^{p, \alpha}$ bound on $F$ and $C^{p, \alpha}$ bound on $\varphi$ give $C^{p+1, \alpha}$ bound on $\varphi$.
Proof. This follows from a standard bootstrap arguments for the Monge-Ampère equation (13). \(\square\)

Proposition 3.11. The metric $g$ on $B_{1}(q) \backslash\{q\}$ extends to a metric on $B_{1}(q)$ that is smooth in the standard complex coordinate.

Proof. In the complex coordinate, we have $C^{1, \alpha}$ bound on $g_{i \bar{j}}$. By choosing the potential function $\varphi$ suitably, it can be assumed that $\varphi$ is $C^{3, \alpha}$ bounded, where $g_{i \bar{j}}=h_{i \bar{j}}+\varphi_{i \bar{j}}$.

Starting with $C^{k+2, \alpha}$ bound on $\varphi$, we have $C^{k, \alpha}$ bound on $\varphi_{i \bar{j}}$. Together with Proposition 3.9, the elliptic equation for $F$ (14) at least has $C^{k, \alpha}$ bounded coefficients. Schauder estimate gives $C^{k+2, \alpha}$ bound on $F$. Choosing $p=k+2$ in Proposition 3.10, one gets $C^{k+3, \alpha}$ bound on $\varphi$. This shows, beginning from $k=1$, by applying this bootstrap argument repeatly, we can finally get $C^{\infty}$ bound on $\varphi$ in the standard complex coordinate. The proposition is proved. \(\square\)

This finishes the proof of Theorem 3.4. The extended complex structure on $\widehat{M}$ is denoted by $\widehat{J}$. Theorem 3.4 has the following corollaries.
Corollary 3.12. On $(\widehat{M}, \widehat{g})$, the Killing field $\mathcal{K}=J \nabla_{g} s_{g}$ extends to the Killing field $\widehat{J}_{\widehat{g}} \widehat{s}_{\widehat{g}}$, which vanishes at the orbifold point $q$. Moreover, $s_{\widehat{g}} \geq 0$ and $s_{\widehat{g}}=0$ only at $q$. The scalar curvature $s_{\widehat{g}}$ is a Morse-Bott function.
Proof. The vanishing of the extended Killing field at $q$ follows from the fact that $|\mathcal{K}|_{g} \leq C \rho^{-1}$. The vanishing of $s_{\widehat{g}}(q)$ follows from the decay of $s_{g}=\lambda^{1 / 3}$ as $O\left(\rho^{-2}\right)$. Outside of $q, s_{\widehat{g}}>0$ because $\lambda=2 \sqrt{6}\left|W^{+}\right|_{h}>0$. The last statement follows from Lemma 1 in [14]. \(\square\)

Corollary 3.13. Near the point $q$, we have $s_{\widehat{g}}=\frac{1}{2} a r_{q}^{2}+O\left(r_{q}^{3}\right)$ for some positive constant $a$. There exists a constant $t_{0}$ such that the time $t_{0}$ flow of the Killing field $\widehat{J}_{\widehat{\mathrm{g}}} \widehat{s}_{\widehat{g}}$ is the identity map.
Proof. Since the Killing field $\widehat{J} \nabla_{\widehat{g}} s_{\widehat{g}}$ vanishes at $q$, we have $\nabla_{\widehat{g}} s_{\widehat{g}}(q)=0$. The Morse-Bott property implies that Hess $\left(s_{\widehat{g}}\right)$ is nondegenerate at $q$. As the Kähler metric is Bach-flat, there is the equation
$$0=s_{g} \operatorname{Ric}_{g}^{0}+2 \operatorname{Hess}_{0}\left(s_{g}\right),$$
which is equation (11) in [14]. So we have $\operatorname{Hess}_{0}\left(s_{\widehat{g}}\right)(q)=0$. Therefore, $\operatorname{Hess}\left(s_{\widehat{g}}\right)(q)=a \widehat{g}$ for some positive $a$, and we conclude that $s_{\widehat{g}}=\frac{1}{2} a r_{q}^{2}+O\left(r_{q}^{3}\right)$ near $q$. Because $\operatorname{Hess}\left(s_{\widehat{g}}\right)(q)=a \widehat{g}$, the time $2 \pi / a$ flow of $\widehat{J} \nabla_{\widehat{g}} s_{\widehat{g}}$ fixes the point $q$ and its tangent space, meaning that the time $2 \pi / a$ flow of this Killing field is the identity map. \(\square\)
3.3. Complex structure on the compactification. The special property of $s_{\widehat{g}}$ leads to the following proposition, which is based on a key observation by LeBrun in [12].
Proposition 3.14. The underlying complex orbifold $(\widehat{M}, \widehat{J})$ is a log del Pezzo surface. That is, $(\widehat{M}, \widehat{J})$ is a normal projective surfaces with at worst quotient singularities and ample anticanonical bundle.

Proof. First, we show the existence of a Kähler current in $2 \pi c_{1}\left(-K_{\widehat{M}}\right)$. Then we prove $-K_{\widehat{M}}$ is positive using regularization. Note that although $-K_{\widehat{M}}$ is only Q -Cartier, for simplicity we will work as if it were Cartier.

The conformal relation $g=\lambda^{2 / 3} h=s_{g}^{2} h$ and the Ricci-flat property of $h$ imply
$$\operatorname{Ric}_{g, a b}=-2 s_{g}^{-1} \nabla_{a} \nabla_{b} s_{g}+\left(-s_{g}^{-1} \Delta s_{g}+3\left|d \log s_{g}\right|_{g}^{2}\right) g_{a b} .$$
Here we are using the Levi-Civita connection of $g$. Taking the trace of (15), we get $s_{g}=-6 s_{g}^{-1} \Delta s_{g}-12\left|d \log s_{g}\right|_{g}^{2}$. Therefore,
$$\operatorname{Ric}_{g, a b}+2 s_{g}^{-1} \nabla_{a} \nabla_{b} s_{g}=\left(\frac{s_{g}}{6}+\left|d \log s_{g}\right|_{g}^{2}\right) g_{a b}$$

This suggests that we should consider the current $T=\rho_{g}+2 \sqrt{-1} \partial \bar{\partial} \log s_{g}$ in the class $2 \pi c_{1}\left(-K_{\widehat{M}}\right)$, where $\rho_{g}$ is the Ricci form of $g$. With (16), the associated symmetric form $T_{J}:=T(\cdot, J \cdot)$ is given by
$$T_{J, a b}=\frac{s_{g}}{6} g_{a b}+s_{g}^{-2}\left(\left|d s_{g}\right|_{g}^{2} g_{a b}-\left(d s_{g}\right)_{a}\left(d s_{g}\right)_{b}-\left(J d s_{g}\right)_{a}\left(J d s_{g}\right)_{b}\right)$$
It is clear that $T_{J}$ is strictly positive, hence the current $T$ is a Kähler current.
To show the ampleness, if $\widehat{g}_{-K}$ denotes the hermitian metric on the line bundle $-K_{\widehat{M}}$ induced by $\widehat{g}$, then the form $\rho_{g}+2 \sqrt{-1} \partial \bar{\partial} \log s_{g}$ is the curvature form of the singular hermitian metric $\widehat{g}_{-K} e^{-2 \log s_{g}}$. The current $T$ as the curvature of the singular metric $g_{-K} e^{-2 \log s_{g}}$ on $-K_{\widehat{M}}$, having Lelong number
$$v(T, x)= \begin{cases}0, & \text { if } x \neq q, \\ 2, & \text { if } x=q,\end{cases}$$
because of Corollary 3.13. Taking a Riemannian normal coordinate near $q$, we have
$$\widehat{g}_{i j}=\delta_{i j}+O\left(r_{q}^{2}\right), \partial_{k} \widehat{g}_{i j}=O\left(r_{q}\right), s_{\widehat{g}}=\frac{1}{2} a r_{q}^{2}+O\left(r_{q}^{3}\right) .$$
So,
$$\frac{s_{g}}{6} g_{a b}+s_{g}^{-2}\left(\left|d s_{g}\right|^{2} g_{a b}-\left(d s_{g}\right)_{a}\left(d s_{g}\right)_{b}-\left(J d s_{g}\right)_{a}\left(J d s_{g}\right)_{b}\right) \geq \frac{1}{12} a r_{q}^{2} g_{a b}+\epsilon \frac{1}{r_{q}^{2}} g_{a b}$$
for some small $\epsilon$, as a symmetric 2-form near $q$. It is a consequence of the standard regularization theorem of Demailly that there is a smooth $(1,1)$ form $\theta$ in $2 \pi c_{1}\left(-K_{\widehat{M}}\right)$ that is strictly positive. \(\square\)

Classical result now says that $(\widehat{M}, \widehat{J})$ is rational, since it is log del Pezzo.
Proposition 3.15. The minimal resolution $\widetilde{M}$ of $\widehat{M}$, denoted as $r: \widetilde{M} \rightarrow \widehat{M}$, is a smooth rational surface.
3.4. The correspondence. The previous discussion has demonstrated that the compactification of a Hermitian non-Kähler ALE gravitational instanton is a special Bach-flat Kähler orbifold. To complete the proof of Theorem 1.3, we still need to prove the other direction of our correspondence.

Theorem 3.16. Given a special Bach-flat Kähler orbifold ( $\widehat{M}, \widehat{g}$ ) with the orbifold point $q$, there exists a Hermitian non-Kähler ALE gravitational instanton $(M, h)$, where $M=\widehat{M} \backslash\{q\}$ and $h=s_{\hat{g}}^{-2} \widehat{g}$.

Proof. Because $\widehat{g}$ is Bach-flat Kähler, after the conformal change, we have $\operatorname{Ric}_{h}^{0}=\operatorname{Ric}_{\widehat{\widehat{g}}}^{0}+2 s_{\widehat{\widehat{g}}}^{-1} \operatorname{Hess}_{0}\left(s_{\widehat{g}}\right)=0$. The vanishing of the traceless Ricci curvature implies $h$ is Einstein. Conformal relation also gives
$$s_{h}=s_{\widehat{g}}^{3}+6 s_{\widehat{g}} \Delta s_{\widehat{g}}-12\left|\nabla s_{\widehat{g}}\right|^{2} .$$
The right side is a continuous function on $\widehat{M}$ which should be a constant because $s_{h}$ is a constant. Since $s_{\widehat{g}}$ achieves its minimum at $q, \nabla_{\widehat{g}}(q)=0$. Evaluating this equation at $q$, we get $s_{h}=0$. Therefore $h$ is a Ricci-flat metric. Near $q$, $s_{\widehat{g}}=\frac{1}{2} a r_{q}^{2}+O\left(r_{q}^{3}\right)$. Hence $h=s_{\widehat{g}}^{-2} \widehat{g}$ has Euclidean volume growth. It is also direct to check that $\int\left|R m_{h}\right|_{h}^{2}<\infty$ over the end. By [1], it is ALE. \(\square\)

This finshes the proof of Theorem 1.3.

\section*{4. Holomorphic vector fields and minimal resolutions}

In Section 4, we take a detour to study weights of holomorphic vector fields, which is necessary for us to classify all the log del Pezzo surfaces coming from Hermitian non-Kähler ALE gravitational instantons. We conclude previous sections before we start. With the correspondence Theorem 1.3, to study Hermitian non-Kähler ALE gravitational instantons $(M, h)$, it suffices to study special Bach-flat Kähler orbifolds $(\widehat{M}, \widehat{g})$. Some key features of special Bach-flat Kähler orbifolds are:
\begin{itemize}
\item[-] The underlying complex surface $\widehat{M}$ is log del Pezzo, with only one orbifold point $q$.
\item[-] The underlying complex surface $\widehat{M}$ carries a holomorphic $\mathbb{C}^{*}$-action: the extremal vector field $\mathcal{K}$ induces a holomorphic $S^{1}$-action by Corollary 3.13, so there is the associated holomorphic $\mathbb{C}^{*}$-action.
\item[-] The holomorphic $\mathbb{C}^{*}$-action has same weights at the orbifold point $q$, in the sense that it fixes $q$ and the two weights of the induced $\mathbb{C}^{*}$-action on the tangent space at $q$ coincide, because of Corollary 3.13.
\end{itemize}

These already are very strong constraints. Denote the infinitesimal generator of the holomorphic $\mathbb{C}^{*}$-action as $\mathfrak{E}$. The holomorphic $\mathbb{C}^{*}$-action always can be taken as primitive and the holomorphic vector field $\mathfrak{E}$ can always be taken as flowing out of the orbifold point $q$. We shall ultimately classify all pairs $(\widehat{M}, \mathfrak{E})$ that satisfy the above conditions, with one more technical assumption that the orbifold group is in $S U(2)$. They are candidates for special Bach-flat Kähler orbifolds with structure group $\Gamma \subset \operatorname{SU}(2)$.

Before proceeding, we fix some notations. By a $\mathbb{C}^{*}$-action on $\mathbb{C}^{2} / \Gamma$ given by $t \curvearrowright(x, y)=\left(t^{\theta} x, t^{\tau} y\right)$, we mean that after passing to the orbifold cover $\mathbb{C}^{2}$, the action is given by $t \curvearrowright(x, y)=\left(t^{\theta} x, t^{\tau} y\right)$. The action must commute with the $\Gamma$-action on $\mathbb{C}^{2}$. By the infinitesimal generator of a $\mathbb{C}^{*}$-action, we mean the holomorphic vector field generated by $\partial_{z}$.
4.1. Quotient singularities and their minimal resolutions. Minimal resolutions of quotient singularities $\mathbb{C}^{2} / \Gamma$ were studied by Brieskorn. In this section we briefly recall their structures. Materials in this section are taken from Lock-Viaclovsky [16, 17].

Consider the quotient singularity $\mathbb{C}^{2} / \Gamma$, where $\Gamma \subset U(2)$ is a finite subgroup and we require that $\mathbb{C}^{2} / \Gamma$ only has an orbifold singularity at the origin. The group $S U(2)$ can be identified with unit quaternions $z_{1}+z_{2} j \in \mathbb{H}$, where $z_{1}, z_{2} \in \mathbb{C}$. This identification allows us to view $\operatorname{SU}(2)$ as the unit sphere $S^{3}$. Define the map $\phi: S^{3} \times S^{3} \rightarrow S O(4)$ by
$$\phi\left(q_{1}, q_{2}\right)(h)=q_{1} h \overline{q_{2}}$$
for $h \in \mathbb{H}$, where we are taking quaternions multiplication. This map $\phi$ is a double cover of $\operatorname{SO}(4)$, and when we restrict it to $S^{1} \times S^{3}$ with $S^{1} \subset S^{3}$ understood as the set of unit $z_{1} \in \mathbb{C} \subset \mathbb{H}$, it provides a double cover of $U(2)$. Now finite subgroups of $U(2)$ acting freely on $S^{3}$ are described by Table 1.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 1. Finite subgroups of $U(2)$ acting freely on $S^{3}$.}
\begin{tabular}[t]{|l|l|l|}
\hline $\Gamma \subset U(2)$ & Conditions & Order \\
\hline $L(m, n)$ & $(m, n)=1$ & $n$ \\
\hline $\phi\left(L(1,2 m) \times D_{4 n}^{*}\right)$ & $(m, 2 n)=1$ & $4 m n$ \\
\hline $\phi\left(L(1,2 m) \times T^{*}\right)$ & $(m, 6)=1$ & $24 m$ \\
\hline $\phi\left(L(1,2 m) \times O^{*}\right)$ & $(m, 6)=1$ & $48 m$ \\
\hline $\phi\left(L(1,2 m) \times I^{*}\right)$ & $(m, 30)=1$ & $120 m$ \\
\hline $\mathfrak{J}_{m, n}^{2}=$ Index-2 diagonal $\subset \phi\left(L(1,4 m) \times D_{4 n}^{*}\right)$ & $(m, 2)=2,(m, n)=1$ & $4 m n$ \\
\hline $\mathfrak{J}_{m}^{3}=$ Index-3 diagonal $\subset \phi\left(L(1,6 m) \times T^{*}\right)$ & $(m, 6)=3$ & $24 m$ \\
\hline
\end{tabular}
\end{table}

Here, the group $L(q, p)$ with coprime $p, q$ denotes the cyclic subgroup of $U(2)$ generated by
$$\left(\begin{array}{cc}
\exp \left(\frac{2 \pi i}{p}\right) & 0 \\
0 & \exp \left(\frac{2 \pi i q}{p}\right)
\end{array}\right) .$$
The finite subgroups of $S U(2)$, denoted by $D_{4 n}^{*}, T^{*}, O^{*}, I^{*}$, correspond to the binary dihedral, tetrahedral, octahedral, and icosahedral groups, respectively. Using the $A D E$ classification for finite subgroups of $S U(2)$, we have that $A_{n}$ corresponds to $L(-1, n+1), D_{n+2}$ corresponds to $D_{4 n}^{*}$, and $E_{6}, E_{7}, E_{8}$ corresponds to $T^{*}, O^{*}, I^{*}$, respectively. Set $[\alpha, \beta]=$ $\phi(\alpha, \beta)$ with $\alpha, \beta \in S U(2)$ for simplicity. We can write down the generators of the above groups in a more explicit manner as in Table 2.

Now we describe the structure of the minimal resolution of $\mathbb{C}^{2} / \Gamma$.
For the cyclic case, when the group $\Gamma$ is $L(q, p)$, the orbifold singularity is a Hirzebruch-Jung singularity. The exceptional divisors of its minimal resolution is a chain of rational curves with self-intersection $-e_{i}$, as illustrated below
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-10.jpg?height=67&width=473&top_left_y=2411&top_left_x=831)
Each vertex denotes a rational curve with self-intersection $-e_{i}$, and if there is a segment between two vertices, it means the two curves intersect transversely at one point. The numbers $e_{i}$ are determined by the relatively prime

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 2. Generators of finite subgroups of $U(2)$ acting freely on $S^{3}$.}
\begin{tabular}[t]{|l|l|}
\hline $\Gamma \subset U(2)$ & Generators \\
\hline $L(q, p)$ & $\left[e^{2 \pi i k / p}, e^{2 \pi i(1-k) / p}\right]$ with $2 k \equiv(q+1) \bmod p$ \\
\hline $\phi\left(L(1,2 m) \times D_{4 n}^{*}\right)$ & $\left[e^{\pi i / m}, 1\right],\left[1, e^{\pi i / n}\right],[1, j]$ \\
\hline $\phi\left(L(1,2 m) \times T^{*}\right)$ & $\left[e^{\pi i / m}, 1\right],[1,(1+i+j-k) / 2],[1,(1+i+j+k) / 2]$ \\
\hline $\phi\left(L(1,2 m) \times O^{*}\right)$ & $\left[e^{\pi i / m}, 1\right],\left[1, e^{\pi i / 4}\right],[1,(1+i+j+k) / 2]$ \\
\hline $\phi\left(L(1,2 m) \times I^{*}\right)$ & $\left[e^{\pi i / m}, 1\right],\left[1,\left(1+\tau i-\tau^{-1} k\right) / 2\right],\left[1,\left(\tau+i+\tau^{-1} j\right) / 2\right]$ with $\tau=(1+\sqrt{5}) / 2$ \\
\hline $\mathfrak{J}_{m, n}^{2}$ & $\left[e^{\pi i / m}, 1\right],\left[1, e^{\pi i / n}\right],\left[e^{\pi i /(2 m)}, j\right]$ \\
\hline $\mathfrak{J}_{m}^{3}$ & $\left[e^{\pi i / m}, 1\right],[1, i],[1, j],\left[e^{\pi i /(3 m)},(-1-i-j+k) / 2\right]$ \\
\hline
\end{tabular}
\end{table}
integers $1 \leq q<p$, via the Hirzebruch-Jung continued fraction expansion with $e_{i} \geq 2$ :
$$\frac{q}{p}=\frac{1}{e_{1}-\frac{1}{e_{2}-\cdots \frac{1}{e_{k}}}} .$$

The minimal resolutions of non-cyclic finite subgroups of $U(2)$ that act freely on $S^{3}$ have exceptional curves consisting of three chains of rational curves, each intersecting a single central rational curve.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-11.jpg?height=238&width=879&top_left_y=1216&top_left_x=627)
Each chain $\left\{e_{i}^{j}\right\}$ with fixed $j=1,2,3$ is the chain of exceptional curves of the minimal resolution for some $L\left(\alpha_{j}, \beta_{j}\right)$. The number $b_{\Gamma}$ here is given by
$$b_{\Gamma}=2+\frac{4 m}{|\Gamma|}\left(m-\left(m \bmod \frac{|\Gamma|}{4 m}\right)\right),$$
with $m$ as in Table 1. The groups $L\left(\alpha_{j}, \beta_{j}\right)$ for each $\Gamma$ is given by Table 3.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 3. $L\left(\alpha_{j}, \beta_{j}\right)$ for non-cyclic subgroups.}
\begin{tabular}[t]{|l|l|}
\hline $\Gamma \subset U(2)$ & $L\left(\alpha_{j}, \beta_{j}\right)$ \\
\hline $\phi\left(L(1,2 m) \times D_{4 n}^{*}\right)$ & $L(1,2), L(1,2), L(-m, n)$ \\
\hline $\phi\left(L(1,2 m) \times T^{*}\right)$ & $L(1,2), L(-m, 3), L(-m, 3)$ \\
\hline $\phi\left(L(1,2 m) \times O^{*}\right)$ & $L(1,2), L(-m, 3), L(-m, 4)$ \\
\hline $\phi\left(L(1,2 m) \times I^{*}\right)$ & $L(1,2), L(-m, 3), L(-m, 5)$ \\
\hline $\mathfrak{J}_{m, n}^{2}$ & $L(1,2), L(1,2), L(-m, n)$ \\
\hline $\mathfrak{J}_{m}^{3}$ & $L(1,2), L(1,3), L(2,3)$ \\
\hline
\end{tabular}
\end{table}
4.2. Weights of holomorphic vector fields at fixed points. For a primitive holomorphic $\mathbb{C}^{*}$-action and its infinitesimal generator $\mathfrak{E}$, we define

Definition 4.1. The weights of the holomorphic vector field $\mathfrak{E}$ at a fixed point $p$ is the pair $[\theta, \tau]$, where $\theta$ and $\tau$ are the weights of the $\mathbb{C}^{*}$-action on the tangent space at $p$. If $p$ is an orbifold point, weights can be similarly defined by passing to the local orbifold cover.

Weights could be fractions when $p$ is an orbifold point. For example, the primitive $\mathbb{C}^{*}$-action on $\mathbb{C}^{2} / \mathbb{Z}_{2}$, given by $t \curvearrowright(x, y)=\left(t^{1 / 2} x, t^{1 / 2} y\right)$ on the orbifold cover $\mathbb{C}^{2}$, has weights [1/2, 1/2] at the origin. The following simple lemma says near a smooth fixed point $q$, there is a holomorphic coordinate such that the holomorphic $\mathbb{C}^{*}$-action with weights $[\theta, \tau]$ is standard.

Lemma 4.2. There exists a holomorphic coordinate $(x, y)$ near $p$ such that the $\mathbb{C}^{*}$-action is given by $t \curvearrowright(x, y)=$ $\left(t^{\theta} x, t^{\tau} y\right)$, and $\mathfrak{E}=\theta x \frac{\partial}{\partial x}+\tau y \frac{\partial}{\partial y}$.

The following proposition explains how blow-up changes weights of a holomorphic $\mathbb{C}^{*}$-action.
Proposition 4.3. For a non-trivial holomorphic $\mathbb{C}^{*}$-action with weights $[\theta, \tau]$ at a fixed point $p$, which is locally given byt $\curvearrowright(x, y)=\left(t^{\theta} x, t^{\tau} y\right)$, the $\mathbb{C}^{*}$-action lifts to the blow-up at $p$. And,
\begin{itemize}
\item[-] if $\theta=\tau$, the exceptional curve $E$ is a fixed curve of the lifted action, points in which all have weights $[\theta, 0]$;
\item[-] if $\theta \neq \tau$, the exceptional curve $E$ admits two fixed points $p_{1}, p_{2}$, with weights $\left[\theta_{1}, \tau_{1}\right],\left[\theta_{2}, \tau_{2}\right]$. Weights of them are $[\theta, \tau-\theta],[\theta-\tau, \tau]$.
\end{itemize}

Proof. Direct calculation. \(\square\)

Remark 4.4. The above proposition can be explained in the following intuitive way. Take $\theta>\tau>0$ for an example. Arrows in the following picture shows the direction of the flows of the $\mathbb{C}^{*}$-action. Then a blow-up at the fixed point changes weights by
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-12.jpg?height=251&width=872&top_left_y=1094&top_left_x=627)
Here $E$ is the exceptional curve. Other situations are similar.
4.3. Toric geometry of $\mathbb{C}^{2} / L(q, p)$ and weights of actions. In this subsection, we consider cyclic groups $\Gamma=$ $L(q, p)$. The minimal resolution of $\mathbb{C}^{2} / \Gamma$ has been described in Section 4.1. Using the languague of toric geometry (see [8] for example), the minimal resolution of $\mathbb{C}^{2} / \Gamma$ can be described more precisely. Recall that for $q / p$ we have the Hirzebruch-Jung continued fraction
$$\frac{q}{p}=\frac{1}{e_{1}-\frac{1}{e_{2}-\ldots-\frac{1}{e_{k}}}} .$$

Theorem 4.5. Define the vertices $v_{0}, \ldots, v_{k+1}$ with $v_{0}=(0,1), v_{1}=(1,0), v_{i+1}=e_{i} v_{i}-v_{i-1}$. Notice that $v_{k+1}=(p,-q)$. Then the fan $F_{L(q, p)}$ of the minimal resolution $\widetilde{\mathbb{C}^{2} / \Gamma}$ is given by Figure 1. The exceptional set is as follows. The curve $E_{i}$ corresponds to the ray given by $v_{i}$ in the fan $F_{L(q, p)}$.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-12.jpg?height=155&width=640&top_left_y=2000&top_left_x=743)

See Section 2.6 of [8] for a proof of the above theorem. The holomorphic $\mathbb{C}^{*}$-action $t \curvearrowright(x, y)=\left(t^{\theta} x, t^{\tau} y\right)$ on $\mathbb{C}^{2} / \Gamma$ can be lifted to the minimal resolution of $\mathbb{C}^{2} / \Gamma$, whose weights can be described by the following theorem.

Theorem 4.6. Consider the $\mathbb{C}^{*}$-action on $\mathbb{C}^{2} / L(q, p)$ defined by $t \curvearrowright(x, y)=\left(t^{\theta} x, t^{\tau} y\right)$ with $\theta \geq \tau \geq 0$ and its minimal resolution $\widetilde{\mathbb{C}^{2} / \Gamma}$ given by Theorem 4.5. Given vertices $v_{0}, \ldots, v_{k}$ as in Theorem 4.5, write $v_{i}=\left(v_{i, U}, v_{i, V}\right)$ and for $i=0, \ldots, k+1$ define
$$w_{i}=\theta\left(p v_{i, V}+q v_{i, U}\right)-\tau v_{i, U} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-13.jpg?height=471&width=533&top_left_y=172&top_left_x=795}
\captionsetup{labelformat=empty}
\caption{Figure 1. The fan $F_{L(q, p)}$ of the minimal resolution $\widetilde{\mathbb{C}^{2} / \Gamma}$.}
\end{figure}

Then the weights of the lifted action are:
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-13.jpg?height=312&width=1369&top_left_y=870&top_left_x=376)
Notice that there is the inductive relation $w_{i+1}=e_{i} w_{i}-w_{i-1}$, and we have $w_{0}=\theta p, w_{1}=\theta q-\tau, w_{k}=\theta-\tau v_{k, U}$, and $w_{k+1}=-\tau p$.

Proof. This should be a standard computation but the author cannot find suitable references in previous literatures. We will provide a proof in the appendix. \(\square\)

Next several corollaries follow from Theorem 4.6.
Corollary 4.7. Consider the $\mathbb{C}^{*}$-action on $\mathbb{C}^{2} / L(q, p)$ defined by $t \curvearrowright(x, y)=\left(t^{\theta} x, y\right)$ with $\theta>0$. Then the weights of the lifted action and direction of flows on the exceptional set are:
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-13.jpg?height=312&width=1366&top_left_y=1622&top_left_x=378)
In this case, $x=0$ is a fixed curve.
Proof. $\tau=0$ implies $w_{i}=\theta(q, p) \cdot\left(v_{i, U}, v_{i, V}\right)>0$, and the corollary follows. \(\square\)

Corollary 4.8. Consider the $\mathbb{C}^{*}$-action on $\mathbb{C}^{2} / L(q, p)$ defined by $t \curvearrowright(x, y)=\left(t^{\theta} x, t^{\tau} y\right)$ with $\theta \geq \tau \geq 0$. Then, when $\theta \neq 0$ or $\tau \neq 0$, the weights $\left[w_{0},-w_{1}\right]$ or the weights $\left[w_{k},-w_{k+1}\right]$, together with $[\theta, \tau]$, uniquely determine the numbers $p$ and $q$, respectively.

Proof. Recall $w_{0}=\theta p, w_{1}=\theta q-\tau, w_{k}=\theta-\tau v_{k, U}, w_{k+1}=-\tau p$. It is clear that once we know $\left[w_{0},-w_{1}\right]$ when $\theta \neq 0$, we can find $q$ and $p$. As for $\left[w_{k},-w_{k+1}\right]$, notice that
$$\left\langle\left(\begin{array}{cc}
\exp \left(\frac{2 \pi i}{p}\right) & 0 \\
0 & \exp \left(\frac{2 \pi i q}{p}\right)
\end{array}\right)\right\rangle=\left\langle\left(\begin{array}{cc}
\exp \left(\frac{2 \pi i q^{-1: p}}{p}\right) & 0 \\
0 & \exp \left(\frac{2 \pi i}{p}\right)
\end{array}\right)\right\rangle .$$
Replacing $x$ by $y$ and $y$ by $x$ and treating $L(q, p)$ as $L\left(q^{-1: p}, p\right.$ ), we learn that $w_{k}=-\tau q^{-1: p}+\theta$. Thus, when $\tau \neq 0$, $\left[w_{k}, w_{k+1}\right]$ determines $q^{-1: p}$ and $p$, which determines $q$ and $p$. \(\square\)

Corollary 4.9. In the case that $\Gamma \subset \operatorname{SU}(2), w_{i+1}-w_{i}=w_{i}-w_{i-1}$. In particular, $w_{i}$ is decreasing, and we have $-\tau p=w_{k+1}<\ldots<w_{0}=\theta p$.

Proof. Follows from $e_{i}=2$ trivially. \(\square\)
4.4. $\mathbb{C}^{2} / \Gamma$ for non-cyclic $\Gamma$ and weights of actions. When $\Gamma$ is non-cyclic, there are elements in $\Gamma$ swapping the two standard complex planes in $\mathbb{C}^{2}$. Therefore, any holomorphic $\mathbb{C}^{*}$-action on $\mathbb{C}^{2} / \Gamma$ must have same weights at the orbifold point, and is given by $t \curvearrowright(x, y)=\left(t^{\theta} x, t^{\theta} y\right)$. Taking $\theta=\frac{1}{2 m}$, we can ensure the holomorphic $\mathbb{C}^{*}$-action on $\mathbb{C}^{2} / \Gamma$ is primitive. From the proof of Theorem 4.1 in [17], we have the following lemma:

Lemma 4.10. For a non-cyclic group $\Gamma$ in Table 3, set $\Gamma^{\prime} \subset \Gamma$ to be the subgroup of $\Gamma$ generated by the same generators listed in Table 2 but without $\left[e^{\pi i / m}, 1\right]$. Then $\mathcal{O}(-2 m) / \Gamma^{\prime}$ has three orbifold points lying on the quotient of the zero-section $\mathbb{P}^{1} \subset \mathcal{O}(-2 m)$. The structure groups of these three orbifold points are precisely the $L\left(\alpha_{j}, \beta_{j}\right)$ listed in Table 3.

Contracting the $\mathbb{P}^{1} \subset \mathcal{O}(-2 m)$ to the origin gives the minimal resolution $\mathcal{O}(-2 m) \rightarrow \mathbb{C}^{2} / L(1,2 m)$. Therefore, the map that contracts $\mathbb{P}^{1} / \Gamma^{\prime}$ in $\mathcal{O}(-2 m) / \Gamma^{\prime}$ to the origin provides the map $\kappa_{\Gamma}: \mathcal{O}(-2 m) / \Gamma^{\prime} \rightarrow \mathbb{C}^{2} / \Gamma$, with $\mathbb{P}^{1} / \Gamma^{\prime}$ serving as the exceptional set. The minimal resolution $\widetilde{\mathbb{C}^{2} / \Gamma}$ is then just the minimal resolution of $\mathcal{O}(-2 m) / \Gamma^{\prime}$. Therefore, above lemma implies that we only need to determine the weights of the lifted $\mathbb{C}^{*}$-action on $\mathcal{O}(-2 m) / \Gamma^{\prime}$ at the three orbifold points and then apply Theorem 4.6, to study the weights on the minimal resolution $\widetilde{\mathbb{C}^{2} / \Gamma}$.
Proposition 4.11. With the $\mathbb{C}^{*}$-action on $\mathbb{C}^{2} / \Gamma$ given by $t \curvearrowright(x, y)=\left(t^{1 / 2 m} x, t^{1 / 2 m} y\right)$, where $m$ is the number appearing in Table 2, weights at the three orbifold points in $\mathcal{O}(-2 m) / \Gamma^{\prime}$ are all $[0,1]$.

Proof. By passing to the covering space, we can reduce to the case where $\Gamma^{\prime}=1$. In other words, we only need to compute the weights of points in the exceptional curve of the map $\mathcal{O}(-2 m) \rightarrow \mathbb{C}^{2} / L(1,2 m)$. The multi-valued map from $\mathcal{O}(-2 m)$ to the orbifold cover $\mathbb{C}^{2}$ of $\mathbb{C}^{2} / L(1,2 m)$ can be expressed as
$$[x: y] \times s \mapsto\left(x s^{1 / 2 m}, y s^{1 / 2 m}\right) .$$
The action with weights $[1 / 2 m, 1 / 2 m]$ lifted to the orbifold cover $\mathbb{C}^{2}$ can be expressed as
$$t \curvearrowright\left(x s^{1 / 2 m}, y s^{1 / 2 m}\right)=\left(x s^{1 / 2 m} t^{1 / 2 m}, y s^{1 / 2 m} t^{1 / 2 m}\right) .$$
After lifting to $\mathcal{O}(-2 m)$, the action is given by $t \curvearrowright[x: y] \times s=[x: y] \times s t$. It is clear that the exceptional curve is a fixed curve and points in the exceptional curve all have weights [0, 1]. \(\square\)

An application of Theorem 4.6 gives:
Theorem 4.12. For $\mathbb{C}^{2} / \Gamma$ with $\Gamma$ being one of the non-cyclic groups in Table 3, consider the $\mathbb{C}^{*}$-action defined by $t \curvearrowright$ $(x, y)=\left(t^{1 / 2 m} x, t^{1 / 2 m} y\right)$. Its minimal resolution consists of three chains of rational curves, which are chains of exceptional curves of the minimal resolutions of $L\left(\alpha_{k}, \beta_{k}\right)$, connected by one central rational curve. The central rational curve is a fixed curve under the lifted action. Weights of the lifted action on these three chains are given by Corollary 4.7 with $\theta=1$.

Proof. Proposition 4.11 shows that the action at the orbifold points is locally given by $t \curvearrowright(x, y)=(t x, y)$ with a suitable coordinate. At the same time, the central curve in $\widetilde{\mathbb{C}^{2} / \Gamma}$ is the proper transform of $\mathbb{P}^{1} / \Gamma^{\prime}$ in $\mathcal{O}(-2 m) / \Gamma^{\prime}$, which is a fixed curve under the lifted action. The theorem follows from Corollary 4.7 now. \(\square\)

\section*{5. Log del Pezzo surfaces with holomorphic vector fields}

In Section 5 and 6, we classify the pairs $(\widehat{M}, \mathfrak{E})$ where
\begin{itemize}
\item[-] The complex surface $\widehat{M}$ is a log del Pezzo surface with only one $\operatorname{SU}(2)$ orbifold point $q$.
\item[-] The vector field $\mathfrak{E}$ is a holomorphic vector field on $\widehat{M}$, which generates a primitive holomorphic $\mathbb{C}^{*}$-action that flows out of $q$.
\item[-] The holomorphic $\mathbb{C}^{*}$-action has same weights at $q$.
\end{itemize}
As mentioned at the beginning of Section 4, these pairs $(\widehat{M}, \mathfrak{E})$ are candidates for special Bach-flat Kähler orbifolds $(\widehat{M}, \widehat{g})$ with structure group in $\operatorname{SU}(2)$.

Denote the minimal resolution of $\widehat{M}$ by $r: \widetilde{M} \rightarrow \widehat{M}$. To classify such pairs $(\widehat{M}, \mathfrak{E})$, one only needs to classify their minimal resolution $\widetilde{M}$ with the lifted $\mathbb{C}^{*}$-action. So it suffices to classify ( $\widetilde{M}, \mathfrak{E}$ ). Because $\widetilde{M}$ is smooth rational, it must have $\mathbb{P}^{2}$ or $H_{k}$ with $k \geq 2$ as its minimal model. The following is standard because there is no curve in $\widetilde{M}$ with self-intersection less than -2 .

Lemma 5.1. The minimal resolution $\widetilde{M}$ either is an iterative blow-up of $\mathbb{P}^{2}$, or is exactly $H_{2}=\mathbb{P}(\mathcal{O} \oplus \mathcal{O}(2))$.
Proposition 5.2. If $\widetilde{M}=H_{2}=\mathbb{P}(\mathcal{O} \oplus \mathcal{O}(2))$, then the correpsonding $\widehat{M}$ is $H_{2}$ contracting $C_{\infty}$. The complex surface $M=\widehat{M} \backslash\{q\}$ is $\mathcal{O}(2)$.

Proof. This is clear since the (-2)-curve $C_{\infty}$ is the only curve with negative self-intersection in $\widetilde{M}$, therefore $M=$ $\widehat{M} \backslash\{q\}=H_{2} \backslash C_{\infty}$. \(\square\)

It is direct to check that the Hitchin-Thorpe inequality [18] holds with an equality on $\mathcal{O}(2)$. Consequently, any ALE gravitational instanton with $\mathcal{O}(2)$ as the underlying space, under the correct orientation, must be anti-self-dual, hence hyperkähler, under this orientation. This exactly correpsonds to the Eguchi-Hanson space.

So in the following, we only need to consider iterative blow-ups of $\mathbb{P}^{2}$. We only need to consider pairs $(\widetilde{M}, \mathfrak{E})$ that are iterative blow-ups of some pairs $\left(\mathbb{P}^{2}, \mathfrak{F}\right)$, where $\mathfrak{F}$ is a holomorphic vector field on $\mathbb{P}^{2}$ that generates a primitive holomorphic $\mathbb{C}^{*}$-action. When we blow up $\mathbb{P}^{2}$ to get $\widetilde{M}$, blow-ups can only be performed at the fixed points of $\mathfrak{F}$. As a result, classifying these pairs $(\widehat{M}, \mathfrak{E})$ becomes a case-by-case study. We introduce some notations first.

Notations.
\begin{itemize}
\item[-] By curves, we particularly mean rational curves that are the closure of $\mathbb{C}^{*}$-orbits.
\item[-] We will describe the structure of each surface by picture. In the following pictures, each black line refers to a curve. Arrow on each line represents the direction of the flow on the curve. Thin black lines with two arrows refer to (-1)-curves. Thick black lines refer to (-2)-curves. When there is a black box ■ on a line, it means the curve is a fixed curve.
\item[-] The blow-up map from $\widetilde{M}$ to $\mathbb{P}^{2}$ is denoted by $\pi$. The map $\pi$ is realized by successive blow-ups of $\mathbb{P}^{2}$, and the intermediate surfaces are denoted by $M_{i}$ :
$$\widetilde{M}=M_{n} \xrightarrow{\pi_{n}} M_{n-1} \xrightarrow{\pi_{n-1}} \ldots \xrightarrow{\pi_{2}} M_{1} \xrightarrow{\pi_{1}} M_{0}=\mathbb{P}^{2} .$$
Each $\pi_{i}$ is a blow-up at a point $p_{i} \in M_{i-1}$. We use $B l_{p_{1}, \ldots, p_{k}} \mathbb{P}^{2}$ to denote the blow-up of $\mathbb{P}^{2}$, where the $i$-th blow-up $\pi_{i}$ is taken at $p_{i} \in B l_{p_{1}, \ldots, p_{i-1}} \mathbb{P}^{2}$. The exceptional curve of the $i$-th blow-up $\pi_{i}$ is denoted by $E_{i}$.
\item[-] We use $[x: y: z]$ as coordinate on $\mathbb{P}^{2}$. The curves $\{x=0\},\{y=0\},\{z=0\}$ in $\mathbb{P}^{2}$ and their proper transforms in each $M_{i}$ are denoted by $X, Y, Z$.
\item[-] Denote the exceptional set of the minimal resolution $r: \widetilde{M} \rightarrow \widehat{M}$ by $E$, which is the cycle of all (-2)-curves in $\widetilde{M}$ and is of type $A_{n}, D_{n}$, or $E_{n}$.
\item[-] We will use $E_{i}$ to denote the proper transform of the curve $E_{i}$ as well for simplicity.
\end{itemize}

To find all possible $(\widetilde{M}, \mathfrak{E})$, our strategy is to proceed the following inductive steps.
Step 1. Choose a pair $\left(M_{0}, \mathfrak{F}_{0}\right)=\left(\mathbb{P}^{2}, \mathfrak{F}\right)$. Equivalently, we choose a primitive holomorphic $\mathbb{C}^{*}$-action on $\mathbb{P}^{2}$, with the infinitesimal generator $\mathfrak{F}$.
Step 2. Assuming we have determined $\left(M_{i-1}, \mathfrak{F}_{i-1}\right)$, we then identify all the fixed points of $\mathfrak{F}_{i-1}$ in $M_{i-1}$ that are not contained in any (-2)-curve.
Step 3. Possible $\left(M_{i}, \mathfrak{F}_{i}\right)$ then are the blow-up $\pi_{i}$ of $\left(M_{i-1}, \mathfrak{F}_{i-1}\right)$ at one of the fixed points $p_{i}$ identified in Step 2. It must be ensured that finally in $\widetilde{M}=M_{n}$ the exceptional set $E$ is of $A D E$ type, and $\mathfrak{E}=\mathfrak{F}_{n}$ has correct weights so that the $\mathfrak{E}$ action on the contraction $\widehat{M}$ has same weights at $q$. In particular, Corollary 5.7 and Lemma 5.5 in the following Section 5.2 hold.
The $\mathbb{C}^{*}$-action on $\widehat{M}$ given by $\mathfrak{E}$ has same weights at the orbifold point $q$ in the cyclic case, if and only if the action on $E \subset \widetilde{M}$ has the weights given by Corollary 4.9 with $\theta=\tau$. In the non-cyclic case, the $\mathbb{C}^{*}$-action on $\widehat{M}$ always has same weights at the orbifold point. We make the following definition before we proceed.

Definition 5.3. The attractive set $c_{+}$is defined as the set where generic $\mathbb{C}^{*}$-orbits flow into. The repulsive set $c_{-}$is defined as the set where generic $\mathbb{C}^{*}$-orbits flow out of.

It is clear that $c_{ \pm}$of each $\left(M_{i}, \mathfrak{F}_{i}\right)$ can only be a fixed point or a fixed curve, since they arise from $\left(\mathbb{P}^{2}, \mathfrak{F}\right)$.
5.1. $\mathbb{C}^{*}$-actions on $\mathbb{P}^{2}$. For a pair $\left(\mathbb{P}^{2}, \mathfrak{F}\right)$, the primitive holomorphic $\mathbb{C}^{*}$-action generated by $\mathfrak{F}$ and its weights must take one of the following three forms.
\begin{itemize}
\item[(1)] The $\mathbb{C}^{*}$-action is given by $t \curvearrowright[x: y: z]=[t x: t y: z]$. In this case, the fixed points set of $\mathfrak{F}$ is the curve $Z$ and the point $[0: 0: 1]$.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-16.jpg?height=359&width=513&top_left_y=279&top_left_x=810)
The attractive set $c_{+}$is $Z$ and the repulsive set $c_{-}$is the point $[0: 0: 1]$.
\item[(2)] The $\mathbb{C}^{*}$-action is given by $t \curvearrowright[x: y: z]=\left[t^{-1} x: t^{-1} y: z\right]$. In this case, the fixed points set of $\mathfrak{F}$ is the curve $Z$ and the point [0 : 0 : 1].
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-16.jpg?height=361&width=466&top_left_y=838&top_left_x=834)
The attractive set $c_{+}$is the point $[0: 0: 1]$ and the repulsive set $c_{-}$is $Z$.
\item[(3)] The $\mathbb{C}^{*}$-action is given by $t \curvearrowright[x: y: z]=\left[t^{\alpha} x: t^{\beta} y: z\right]$, with coprime $\alpha>\beta>0$. In this case, the fixed points set of $\mathfrak{F}$ consists of the points [ 1 : 0 : 0], [0 : 1 : 0], and [0: 0 : 1].
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-16.jpg?height=365&width=655&top_left_y=1409&top_left_x=741)
The attractive set $c_{+}=[1: 0: 0]$ and the repulsive set $c_{-}=[0: 0: 1]$.
\end{itemize}

We therefore divide into three possibilities:
\begin{itemize}
\item[(i)] The $\mathbb{C}^{*}$-action on $\widetilde{M}$ is lifted from $t \curvearrowright[x: y: z]=[t x: t y: z]$ on $\mathbb{P}^{2}$.
\item[(ii)] The $\mathbb{C}^{*}$-action on $\widetilde{M}$ is lifted from $t \curvearrowright[x: y: z]=\left[t^{-1} x: t^{-1} y: z\right]$ on $\mathbb{P}^{2}$;
\item[(iii)] The $\mathbb{C}^{*}$-action on $\widetilde{M}$ is lifted from $t \curvearrowright[x: y: z]=\left[t^{\alpha} x: t^{\beta} y: z\right]$ on $\mathbb{P}^{2}$ with coprime $\alpha>\beta>0$.
\end{itemize}

We will refer to these three cases as case (i), case (ii), and case (iii) in the following discussion. Before we proceed, we prove Corollary 1.6, the topological finiteness of Hermitian non-Kähler ALE gravitational instantons. For this proposition we do not require that $\Gamma \subset \operatorname{SU}(2)$.

Proposition 5.4. For a log del Pezzo surface $\widehat{M}$ with only one U(2) orbifold singularity, the degree of its minimal resolution $K_{\widetilde{M}}^{2}$ has a lower bound $k_{\Gamma}$ that only depends on $\Gamma$.

Proof. As $\widetilde{M}$ is the minimal resolution of $\widehat{M}$, one has $-K_{\widetilde{M}}=-r^{*} K_{\widehat{M}}-\sum a_{i} C_{i}$. Here $C_{i}$ are the exceptional curves. The discrepancies $a_{i}$ and the cycle of exceptional curves are determined by the group $\Gamma$. Therefore, the degree of $\widetilde{M}$ satisfies $K_{\widetilde{M}}^{2}=\left(r^{*} K_{\widehat{M}}+\sum a_{i} C_{i}\right)^{2}=K_{\widehat{M}}^{2}+\left(\sum a_{i} C_{i}\right)^{2} \geq\left(\sum a_{i} C_{i}\right)^{2}$. The number $k_{\Gamma}:=\left(\sum a_{i} C_{i}\right)^{2}$ depends only on $\Gamma \subset U(2)$, as claimed. \(\square\)

The lower bound on $K_{\widetilde{M}}^{2}$ implies that if $\widetilde{M}$ has $\mathbb{P}^{2}$ as its minimal model, then at most $9-k_{\Gamma}$ blow-ups can be performed. If $\widetilde{M}$ has a Hizebruch surface as a minimal model, then at most $8-k_{\Gamma}$ blow-ups can be performed. This proves Corollary 1.6.
5.2. Flows on $\widetilde{M}$. In this subsection, we establish some technical lemmas regarding the structure of $\widetilde{M}$. Because $\widetilde{M}$ cannot contain curves with intersection number $\leq-3$, the following lemma is straightforward:

Lemma 5.5. Fixed point $p \in M_{i}$ lying on a (-2)-curve cannot be blown up.
Lemma 5.6. Let $p \in M_{i}$ be a transverse intersection of two curves $C_{1}, C_{2} \subset M_{i}$, whose proper transforms in $\tilde{M}$ are both contained in $E$. Assume that weights $[\theta, \tau]$ at $p$ are not strictly positive or strictly negative, then $p$ cannot be blown up in the resolution $\pi: \widetilde{M} \rightarrow \mathbb{P}^{2}$.

Proof. Without loss of generality we can assume $\theta \geq 0 \geq \tau$. If there were a blow-up at $p \in M_{i}$, then there would not be any fixed curve in the preimage of $p$ in any $M_{j}$ with $j>i$ because of Proposition 4.3. The preimage of $p$ then necessarily contains a (-1)-curve. As $C_{1}$ and $C_{2}$ have their proper transforms in $E$ and $E$ entirely consists of (-2)-curves, the appearance of the (-1)-curve will make $E$ disconnected, contradiction. \(\square\)

As a corollary, we have:
Corollary 5.7. Let $p \in M_{i}$ be a transverse intersection of two curves $C_{1}, C_{2} \subset M_{i}$, where each $C_{i}$ is either a curve whose proper transform is contained in $E$, or a curve with negative self-intersection. Assume that weights at $p$ are not strictly positive or negative. Then $p$ cannot be blown up in the resolution $\pi: \widetilde{M} \rightarrow \mathbb{P}^{2}$.
Proof. If such $p_{i}$ is blown up, then proper transform of $C_{i}$ in $\widetilde{M}$ has self intersection $\leq-2$. This shows that proper transform of $C_{i}$ is contained in $E$ and the corollary follows from the above lemma. \(\square\)
5.3. Case (i). In this subsection, we focus on case (i) and show that the pair $(\widetilde{M}, \mathfrak{E})$ admits three possibilities.

Proposition 5.8. In case $(i)$, there are three possible $(\widetilde{M}, \mathfrak{E})$.
Proof. Recall flows on $\mathbb{P}^{2}$ in case (i) is given in Section 5.1. Following our strategy, we analyze as follows.
If there is no blow-up at $X \cap Y$, then the repulsive set $c_{-}$is exactly $X \cap Y$ in $\widetilde{M}$. Since $c_{-} \subset E$ in $\widetilde{M}$, without loss of generality, we can assume that $X \subset E$ in $\widetilde{M}$. Then $X$ in $\widetilde{M}$ must have self-intersection -2. To achieve this, one needs to perform blow-ups in $X$ inside $\mathbb{P}^{2}$. Therefore we take $p_{1}=X \cap Z$. Flows and weights on $M_{1}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-17.jpg?height=352&width=488&top_left_y=1571&top_left_x=823)
After the blow-up $\pi_{1}$ the curve $X$ in $M_{1}$ is a 0 -curve, and we still need to take blow-ups in $X$. However,
\begin{itemize}
\item[-] $X \cap Y$ cannot be blown up because of our assumption.
\item[-] $X \cap E_{1}$ cannot be blown up because of Corollary 5.7.
\end{itemize}
Hence, the situation that there is no blow-up at $X \cap Y$ can not happen.
If there is a blow-up at $X \cap Y$, we can take $M_{1}$ as the blow-up at $p_{1}=X \cap Y$. Flows and weights on $M_{1}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-17.jpg?height=352&width=486&top_left_y=2232&top_left_x=825)

There is still no (-2)-curve in $M_{1}$. The repulsive set $c_{-}$is already the fixed curve $E_{1}$. So the proper transform of $E_{1}$ in $\widetilde{M}$ must be a (-2)-curve. Since $E_{1}$ in $M_{1}$ has self-intersection -1, another blow-up is necessary in $E_{1} \subset M_{1}$. It can be assumed that the blow-up $\pi_{2}$ is at $p_{2}=X \cap E_{1}$. Flows and weights on $M_{2}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-18.jpg?height=354&width=490&top_left_y=350&top_left_x=821)
Now,
\begin{itemize}
\item[-] $X \cap E_{2}$ cannot be blown up because of Corollary 5.7.
\item[-] $X \cap Z$ cannot be blown up because then $X$ will be a (-2)-curve, which makes $E$ disconnected in $\widetilde{M}$.
\end{itemize}
If there are further blow-ups in $M_{2}$, the only option is to blow up points in $Z$ other than the point $X \cap Z$. The intersection number of $Z$ is 1 in $M_{2}$. If there are more blow-ups, then we can suppose $p_{3}=Z \cap Y$. Flows and weights on $M_{3}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-18.jpg?height=378&width=503&top_left_y=1091&top_left_x=808)
Now,
\begin{itemize}
\item[-] $X \cap E_{2}, E_{1} \cap E_{2}, Y \cap E_{1}, Y \cap E_{3}$ cannot be blown up because of Corollary 5.7.
\item[-] $X \cap Z, Z \cap E_{3}$ cannot be blown up because then $X$ or $E_{3}$ will be a (-2)-curve, which makes $E$ disconnected in $\widetilde{M}$.
\end{itemize}
In $M_{3}, Z$ is a 0-curve. Any further blow-up in $M_{3}$ must be made at points in $Z$ other than $X \cap Z$ and $Z \cap E_{3}$. If there is a further blow-up at $p_{4} \in Z$, then flows and weights on $M_{4}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-18.jpg?height=374&width=599&top_left_y=1876&top_left_x=758)
Here $F$ is the proper transform of the curve in $M_{3}$, flowing from $E_{1}$ to $p_{4}$. Any further blow-up in $M_{4}$ must be made in $Z$. However, since $Z$ is already a (-1)-curve, no more points in $Z$ can be blown up. Therefore, we conclude that in case (i), the only possible $(\widetilde{M}, \mathfrak{E})$ are $M_{2}, M_{3}$, and $M_{4}$, with the primitive action with weights described above. \(\square\)

Using Corollary 4.9, it is direct to check the action by $\mathfrak{E}$ on the corresponding $\widehat{M}$ for these three cases above all have same weights at the orbifold point. Structures of these three possible $(\widetilde{M}, \mathfrak{E})$ are listed as follows:

Case 1A.
\begin{itemize}
\item[-] The orbifold group is $A_{1}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, E_{1} \cap X} \mathbb{P}^{2}$$
is 7 and the picard number of $\widehat{M}$ is 2.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-19.jpg?height=348&width=475&top_left_y=174&top_left_x=1222)

Case 1B.
\begin{itemize}
\item[-] The orbifold group is $A_{1}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, E_{1} \cap X, Y \cap Z} \mathbb{P}^{2}$$
is 6 and the picard number of $\widehat{M}$ is 3.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}-2 E_{3}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-19.jpg?height=376&width=501&top_left_y=539&top_left_x=1212)

Case 1C.
\begin{itemize}
\item[-] The orbifold group is $A_{1}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, E_{1} \cap X, Y \cap Z, p_{4}} \mathbb{P}^{2}$$
is 5 and the picard number of $\widehat{M}$ is 4. Here $p_{4}$ is a point in $Z$ different from $X \cap Z, E_{3} \cap Z$.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}-2 E_{3}-2 E_{4}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-19.jpg?height=378&width=602&top_left_y=945&top_left_x=1160)
5.4. Case (ii). We now move on to the classification of pairs $(\widetilde{M}, \mathfrak{E})$ in case (ii). Recall weights and flows on $\mathbb{P}^{2}$ in case (ii) is given in Section 5.1. Note that $c_{-}$in $\mathbb{P}^{2}$ is already the fixed curve $Z$, having self-intersection 1 . The repulsive set $c_{-}$in $\widetilde{M}$ is the proper transform of $Z$, which must be a (-2)-curve. Three blow-ups in $Z$ must be performed to achieve this. We assume that the first blow-up $\pi_{1}$ is at $p_{1}=X \cap Z$. Flows and weights on $M_{1}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-19.jpg?height=348&width=501&top_left_y=1573&top_left_x=810)
In $M_{1}, Z$ is a 0-curve. Two more blow-ups must be performed in $Z$, but $Z \cap E_{1}$ can not be blown up because of Corollary 5.7. Therefore, the two additional blow-ups must be performed at distinct points in $Z$ that are different from the point $Z \cap E_{1}$. After two such blow-ups, the resulting surface is $M_{3}$, flows and weights on which are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-19.jpg?height=395&width=571&top_left_y=2118&top_left_x=773)
Now, points that can be blown up in $M_{3}$ are $X \cap E_{1}, F \cap E_{2}, Y \cap E_{3}$, and $X \cap Y$.

Lemma 5.9. If there is a further blow-up $\pi_{4}$ at $p_{4}=X \cap Y \in M_{3}$, no further blow-ups can be made in $M_{4}$.
Proof. Flows and weights on $M_{4}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-20.jpg?height=352&width=606&top_left_y=344&top_left_x=756)
Now,
\begin{itemize}
\item[-] Points in $E_{4}$ can not be blown up because $E_{4}$ is already a (-1)-curve.
\item[-] $X \cap E_{1}, F \cap E_{2}, Y \cap E_{3}$ can not be blown up because of Corollary 5.7.
\end{itemize}
The lemma is proved. \(\square\)

If instead there is a further blow-up $\pi_{4}$ at $p_{4}=X \cap E_{1}$ (the cases of $p_{4}=F \cap E_{2}$ or $p_{4}=Y \cap E_{4}$ are similar), flows and weights on $M_{4}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-20.jpg?height=397&width=576&top_left_y=1179&top_left_x=773)

Lemma 5.10. If there is a further blow-up $\pi_{4}$ at $p_{4}=X \cap E_{1} \in M_{3}$, further blow-ups can only be taken at $F \cap E_{2}, Y \cap E_{3}$.
Proof. $E_{1} \cap E_{4}, X \cap E_{4}$ can not be blown up because of Corollary 5.7. $X \cap Y$ cannot be blown up since this will make $E$ disconnected in $\widetilde{M}$. Points in $Z$ cannot be blown up because of Lemma 5.5. \(\square\)

To summarize, based on Lemma 5.9 and Lemma 5.10, we obtain 5 possible $(\widetilde{M}, \mathfrak{E})$ by examining all the possibilities, denoted by Case 2A, 2B, 2C, 2D, and 2E. However, it turns out that for Case 2C the action by $\mathfrak{E}$ on $\widehat{M}$ does not have same weights at the orbifold point $q$. Therefore, there are actually only 4 possible structures of $(\widetilde{M}, \mathfrak{E})$ in case (ii).

Proposition 5.11. There are 4 possible pairs $(\widetilde{M}, \mathfrak{E})$ in case (ii), namely the following Case $2 A$, Case 2B, Case 2D, and Case 2E.

Case 2A.
\begin{itemize}
\item[-] The orbifold group is $A_{1}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Z, p_{2}, Y \cap Z} \mathbb{P}^{2}$$
is 6 and the picard number of $\widehat{M}$ is 3. Here $p_{2}$ is a point in $Z$ different from $E_{1} \cap Z, Y \cap Z$.
\item[-] $K_{\widetilde{M}}=-3 Z-2 E_{1}-2 E_{2}-2 E_{3}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-20.jpg?height=395&width=483&top_left_y=2196&top_left_x=1220)

Case 2B.
\begin{itemize}
\item[-] The pair $(\widetilde{M}, \mathfrak{E})$ is biholomorphic to the pair of Case 1C.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-21.jpg?height=397&width=576&top_left_y=174&top_left_x=1195)

Case 2C.
\begin{itemize}
\item[-] This can be excluded since by Theorem 4.6, the action by $\mathfrak{E}$ on $\widehat{M}$ at the orbifold point $q$ has weights $\left[\frac{2}{3}, \frac{1}{3}\right]$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-21.jpg?height=357&width=554&top_left_y=574&top_left_x=1186)

Case 2D.
\begin{itemize}
\item[-] The orbifold group is $A_{3}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Z, p_{2}, Y \cap Z, X \cap E_{1}, Y \cap E_{3}} \mathbb{P}^{2}$$
is 4 and the picard number of $\widehat{M}$ is 3. Here $p_{2}$ is a point in $Z$ different from $E_{1} \cap Z, Y \cap Z$.
\item[-] $K_{\widetilde{M}}=-3 Z-2 E_{1}-2 E_{2}-2 E_{3}-E_{4}-E_{5}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-21.jpg?height=462&width=647&top_left_y=960&top_left_x=1139)

Case 2E.
\begin{itemize}
\item[-] The orbifold group is $D_{4}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Z, p_{2}, Y \cap Z, X \cap E_{1}, Y \cap E_{3}, F \cap E_{2}} \mathbb{P}^{2}$$
is 3 and the picard number of $\widehat{M}$ is 3. Here $p_{2}$ is a point in $Z$ different from $E_{1} \cap Z, Y \cap Z$.
\item[-] $K_{\widetilde{M}}=-3 Z-2 E_{1}-2 E_{2}-2 E_{3}-E_{4}-E_{5}-E_{6}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-21.jpg?height=462&width=647&top_left_y=1452&top_left_x=1139)
6. Case (iii)

This section focuses on case (iii). Recall fixed points and flows of the action on $\mathbb{P}^{2}$ are the following with $\alpha>\beta$.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-21.jpg?height=359&width=651&top_left_y=2084&top_left_x=741)
6.1. Cyclic $\Gamma$. The first observation is that there must be a blow-up at $X \cap Y$.

Lemma 6.1. There must be a blow-up at $X \cap Y$. Therefore, $\tilde{M}$ is a blow-up of $M_{1}=B l_{X \cap Y} \mathbb{P}^{2}$.

Proof. If there were no blow-up at $X \cap Y$, then $c_{-}=X \cap Y$ in $\widetilde{M}$ and $E$ would either contain the proper transform of $X$ or the proper transform of $Y$. If the proper transform of $X$ were contained in $E$, then it would be a (-2)-curve. Blow-up must be performed at $p_{1}=X \cap Z$ in $\mathbb{P}^{2}$. But Corollary 5.7 prevents further blow-up at $X \cap E_{1}$. Therefore this case cannot happen. The situation is exactly the same if we assume the proper transform of $Y$ is contained in $E$. \(\square\)

Let $M_{1}$ be $B l_{X \cap Y} \mathbb{P}^{2}$. Weights and direction of flows on $M_{1}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-22.jpg?height=357&width=632&top_left_y=443&top_left_x=752)
Further blow-ups must be performed. Because of Corollary 4.8, weights at either of the two ending fixed points in $E$ determine $p$ and $q$. Because $E$ must contain $c_{-}$in $\widetilde{M}$, if there is no blow-up at $X \cap E_{1}$, then either the proper transform of $X$, or the proper transform of $E_{1}$, is contained in $E$. Therefore, if there is no blow-up at $X \cap E_{1}$, then either $X \cap Z$, or $E_{1} \cap Y$, must be blown up. It follows that the next blow-up $\pi_{2}$ can be chosen to be one of the following
\begin{itemize}
\item[-] $\pi_{2}$ is the blow-up at $p_{2}=E_{1} \cap Y$.
\item[-] $\pi_{2}$ is the blow-up at $p_{2}=X \cap E_{1}$.
\item[-] $\pi_{2}$ is the blow-up at $p_{2}=X \cap Z$, and there is no blow-up at $X \cap E_{1}, E_{1} \cap Y$ in further blow-ups.
\end{itemize}
These three cases are studied in the following Section 6.1.1, Section 6.1.2, and Section 6.1.3.
6.1.1. $p_{2}=E_{1} \cap Y$. Then $M_{2}$ is
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-22.jpg?height=350&width=612&top_left_y=1289&top_left_x=756)

Now:
\begin{itemize}
\item[-] $X \cap E_{1}$ and $E_{1} \cap E_{2}$ cannot be blown up because of Lemma 5.5.
\item[-] $E_{2} \cap Y$ cannot be blown up because of Corollary 5.7.
\item[-] $Z \cap Y$ cannot be blown up because this will make $E$ in $\widetilde{M}$ disconnected.
\end{itemize}
Additional blow-ups are necessary since the weights on $E_{1}$ does not satisfy $\beta=2 \alpha-\beta$. If we contract $E_{1}$ now, the action by $\mathfrak{E}$ at the orbifold point $q$ does not have same weights. Indeed, contracting $E_{1}$ gives an $A_{1}$ singularity, and the weights are $\left[\alpha-\frac{\beta}{2}, \frac{\beta}{2}\right]$ at the orbifold point. Hence there must be a blow-up at $X \cap Z$, and $p_{3}$ can be taken as $X \cap Z$. So $M_{3}$ is
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-22.jpg?height=367&width=614&top_left_y=2058&top_left_x=758)

Now:
\begin{itemize}
\item[-] $E_{3} \cap X, X \cap E_{1}, E_{1} \cap E_{2}, E_{2} \cap Y$ all cannot be blown up because of Corollary 5.7.
\item[-] $E_{3} \cap Z, Y \cap Z$ cannot be blown up because such blow-ups will make $E$ in $\widetilde{M}$ disconnected.
\end{itemize}

No further blow-ups can be taken in $M_{3}$. This leads to a contradiction, as after contracting $E_{1}$ the weights at the orbifold point are still $\left[\alpha-\frac{\beta}{2}, \frac{\beta}{2}\right]$. In conclusion, $E_{1} \cap Y$ cannot be blown up in $M_{1}$.
6.1.2. $p_{2}=X \cap E_{1}$. The weights and direction of flows on $M_{2}$ are as follows:
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-23.jpg?height=352&width=621&top_left_y=361&top_left_x=752)
The direction of the flow on $E_{2}$ is determined by the sign of $\alpha-2 \beta$.
Lemma 6.2. The proper transform of $Y$ in $\widetilde{M}$ cannot be contained in $E$.
Proof. If the proper transform of $Y$ in $\widetilde{M}$ were contained in $E$, then it would have self-intersection -2. Blow-up must be performed at $Y \cap Z$ in $M_{2}$. Take $p_{3}=Y \cap Z$. Then $M_{3}$ is
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-23.jpg?height=380&width=621&top_left_y=1005&top_left_x=748)
No further blow-ups can be taken to make $Y$ a (-2)-curve. Contradiction. \(\square\)

It follows that $E_{1} \cap Y$ must be one of the ending fixed points of $E$ in $\widetilde{M}$. Since the holomorphic $\mathbb{C}^{*}$-action must have same weights at the orbifold point, we must have
$$w_{0}=\theta p=\alpha, w_{1}=\theta(p-1)-\theta=\alpha-\beta,$$
or
$$w_{k}=\theta-\theta(p-1)=\beta-\alpha, w_{k+1}=-\theta p=-\alpha .$$
It follows that $\alpha=\theta p$ and $\beta=2 \theta$.
Lemma 6.3. $E_{2}$ in $M_{2}$ is a fixed curve and it is the repulsive set $c_{-}$in $M_{2}$.
Proof. The curve $E_{2}$ in $M_{2}$ is a fixed curve if and only if $\alpha=2 \beta$. Hence, if the lemma were not true, we would have two cases: either $\alpha>2 \beta$, or $\alpha<2 \beta$. In the following we will show that neither of these cases is possible. If $\boldsymbol{\alpha}>2 \boldsymbol{\beta}$. Flows on $M_{2}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-23.jpg?height=348&width=621&top_left_y=2071&top_left_x=752)

Now:
\begin{itemize}
\item[-] $E_{2} \cap E_{1}$ and $E_{1} \cap Y$ can not be blown up because of Lemma 5.5.
\item[-] There must be a blow-up at $X \cap E_{2}$ because $E$ in $\widetilde{M}$ must contain $c_{-}$.
\end{itemize}

Take $p_{3}=X \cap E_{2}$. Weights and direction of flows on $M_{3}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-24.jpg?height=490&width=773&top_left_y=286&top_left_x=675)
The direction of the flow on $E_{3}$ depends on the sign of $\alpha-3 \beta$. Now to ensure $E$ is connected, the only possibility is that $E_{3}$ is a fixed curve, which implies $\alpha=3 \beta$. To make $E_{3}$ a (-2)-curve, another blow-up at a point in $E_{3}$ other than $E_{3} \cap X, E_{3} \cap E_{2}$ is necessary.

But $X \cap Z$ can not serve as the other ending fixed point in $E$ : If $X \cap Z$ were the other ending fixed point, by Corollary 4.9, we would have $\alpha-\beta=\alpha$, which is not possible. Thus, the proper transform of $Z$ in $\widetilde{M}$ should also be contained in $E$. Three further blow-ups in $Z$ must be taken at $Y \cap Z$ to make $Z$ a (-2)-curve since $Z$ has self-intersection 1 in $M_{3}$. This is not possible, because the exceptional curves of these blow-ups contain (-2)-curves, which will disconnect $E$. If $\boldsymbol{\alpha}<2 \boldsymbol{\beta}$. Then flows on $M_{2}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-24.jpg?height=352&width=629&top_left_y=1302&top_left_x=752)

Now $X \cap E_{2}$ cannot be blown up because of Corollary 5.7. The exceptional set $E$ in $\widetilde{M}$ must entirely consist of $E_{1}$, which leads to a contradiction, as $\mathfrak{E}$ would not have same weights at the orbifold point. \(\square\)

With Lemma 6.3 being proved, $E_{2}$ in $M_{2}$ is a fixed curve. We have $\alpha=2 \beta$, and $p=4$. The orbifold group must be $L(3,4)$. As the $\mathbb{C}^{*}$-action is assumed to be primitive, we should take $\alpha=2$ and $\beta=1$. So $M_{2}$ is
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-24.jpg?height=352&width=511&top_left_y=2073&top_left_x=812)
Now $X \cap E_{2}$ cannot be blown up because of Corollary 5.7. Because $E_{2}$ is the repulsive set, it has to be contained in $E$. Consequently $E_{2}$ has to be a (-2)-curve. We need to perform one more blow-up in $E_{2}$ at a point $p_{3}$ other than $X \cap E_{2}$
and $E_{2} \cap E_{1}$. Weights and flows in $M_{3}$ now are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-25.jpg?height=350&width=513&top_left_y=236&top_left_x=810)
Similar as before, $X \cap E_{2}$ cannot serve as the other ending fixed point of $E$ because of the weight issue. Blow-up must be performed at $p_{4}=X \cap Z$ in $M_{3}$. Weights and flows on $M_{4}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-25.jpg?height=451&width=612&top_left_y=726&top_left_x=761)
Due to the weight constraints (see Corollary 4.9), $E_{4} \cap X$ must be the other ending fixed point, and $E=X \cup E_{2} \cup E_{1}$. By analyzing all further blow-ups in $M_{4}$, the following proposition holds.

Proposition 6.4. If $p_{2}=X \cap E_{1}, \widetilde{M}$ can only be the $M_{4}$ above, or $M_{5}=B l_{Z \cap Y} M_{4}$, whose configuration is
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-25.jpg?height=445&width=567&top_left_y=1384&top_left_x=778)

The first case in the above proposition will be labeled as Case 3A, and the second case will be Case 3B.
Proof. The only possible blow-up in $M_{4}$ is at $p_{5}=Z \cap Y$. If such a blow-up occurs, then no more fixed points can be blown up in $M_{5}$. Therefore, the proposition is proved. \(\square\)
6.1.3. $p_{2}=X \cap Z$, and there is no blow-up at $X \cap E_{1}, E_{1} \cap Y$ in further blow-ups. Flows on $M_{2}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-25.jpg?height=365&width=610&top_left_y=2110&top_left_x=761)
The repulsive set $c_{-}$must be contained in $E$. However, blow-ups cannot be taken at $X \cap E_{2}, X \cap E_{1}, E_{1} \cap Y$. It follows this case cannot happen.

Section 6.1.1-6.1.3 together conclude the cyclic case (iii).
Proposition 6.5. In case (iii), if the orbifold group $\Gamma$ is cyclic, then there are only Case 3A and Case 3B in the following.
Note that the $\mathfrak{E}$ action is lifted from $t \curvearrowright[x: y: z]=\left[t^{2} x: t y: z\right]$ on $\mathbb{P}^{2}$.

Case 3A.
\begin{itemize}
\item[-] The orbifold group is $A_{3}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, X \cap E_{1}, p_{3}, X \cap Z} \mathbb{P}^{2}$$
is 5 and the picard number of $\widehat{M}$ is 2 . Here $p_{3}$ is a point in $E_{2}$ different from $X \cap E_{2}, E_{1} \cap E_{2}$.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}+3 E_{3}-2 E_{4}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-26.jpg?height=443&width=595&top_left_y=387&top_left_x=1164)

Case 3B.
\begin{itemize}
\item[-] The pair $(\widetilde{M}, \mathfrak{E})$ is biholomorphic to the pair of Case 2D.
\end{itemize}
6.2. Non-cyclic $\Gamma$. In the non-cyclic case, the orbifold group can only be of $D_{n}$ or $E_{n}$ type. An important feature is the central curve in $E$ is a fixed curve, which is also the repulsive set $c_{-}$. Lemma 6.1 also holds by the same proof in this case and $M_{1}=B l_{X \cap Y} \mathbb{P}^{2}$.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-26.jpg?height=354&width=627&top_left_y=1439&top_left_x=752)
To create the fixed central curve, blow-up must be taken at $p_{2}=X \cap E_{1}$. Now $M_{2}$ is
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-26.jpg?height=350&width=617&top_left_y=1904&top_left_x=754)
The direction of the flow on $E_{2}$ is determined by the sign of $\alpha-2 \beta$, resulting in three possible cases.
\begin{itemize}
\item[-] $\alpha=2 \beta$. In this case, $E_{2}$ is already a fixed curve.
\item[-] $\alpha<2 \beta$. To get the fixed curve, a further blow-up should be taken at $p_{3}=E_{2} \cap E_{1}$ in $M_{2}$. However, this is not possible as $E_{1}$ is already a (-2)-curve.
\item[-] $\alpha>2 \beta$. In this case, to get the fixed curve, a further blow-up should be taken at $p_{3}=X \cap E_{2}$ in $M_{2}$.
\end{itemize}
In the following Section 6.2.1 and Section 6.2.2, we analyze the remaining cases in detail.
6.2.1. $\boldsymbol{\alpha}=2 \boldsymbol{\beta}$. Weights and flows on $M_{2}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-27.jpg?height=354&width=629&top_left_y=234&top_left_x=750)
It is clear that the proper transform of $E_{2}$ in $\widetilde{M}$ is the central curve in $E$, since $E_{2}$ is already the fixed curve. Now
\begin{itemize}
\item[-] Similar to Lemma 6.2, $Y$ cannot be contained in $E$.
\item[-] $X \cap E_{2}, E_{2} \cap E_{1}$ can not be blown up because of Corollary 5.7.
\end{itemize}
Therefore, $E_{1}$ must be one of the three chains of(-2)-curves intersecting the central curve in $E$, which is a chain of type $A_{1}=L(1,2)$. According to Theorem 4.12, the weights at the ending fixed point of this chain must be $[p,-q]=[2,-1]$. Hence,
$$\alpha=p=2, \beta-\alpha=-q=-1,$$
which shows $\alpha=2, \beta=1$. Another blow-up is necessary in $E_{2}$ to make it a (-2)-curve. As there are three chains of (-2)-curves intersecting $E_{2}$, there also should be a blow-up at $X \cap Z$. Hence the next lemma is clear.

Lemma 6.6. There must be a blow-up at $p_{3}=X \cap Z$ in $M_{2}$ and a blow-up at a point $p_{4} \in E_{2}$ other than $X \cap E_{2}, E_{2} \cap E_{1}$.
The resulting surface is $M_{4}$.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-27.jpg?height=451&width=608&top_left_y=1186&top_left_x=763)
Here, $F$ is the proper transform of the curve from $p_{4}$ to $Y \cap Z$. To guarantee the presence of three chains of (-2)-curves intersecting $E_{2}$, an extra blow-up at the intersection point $p_{5}=E_{4} \cap F$ is required. We have the following proposition.
Proposition 6.7. The surface $\widetilde{M}$ must be a blow-up of $M_{5}=B l_{E_{4} \cap F} M_{4}$.
Flows on $M_{5}$ are given by
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-27.jpg?height=544&width=696&top_left_y=1891&top_left_x=713)
Note that here $F$ intersects $Z$ non-transversely, and a simple calculation shows $F^{2}=Z^{2}=0$. Blow up $Y \cap Z$ lowers the self intersection of $F$ by 1 . By analyzing all further possible blow-ups case-by-case, we can classify all $(\widetilde{M}, \mathfrak{E})$ in the case that $\alpha=2 \beta$.

Proposition 6.8. In case (iii), when $\alpha=2 \beta$ and the orbifold group is non-cyclic, there are five possible $(\tilde{M}, \mathfrak{E})$.

The structures of these $(\widetilde{M}, \mathfrak{E})$ are given below. Note that the $\mathfrak{E}$ action is lifted from $t \curvearrowright[x: y: z]=\left[t^{2} x: t y: z\right]$ on $\mathbb{P}^{2}$.

Case 3C.
\begin{itemize}
\item[-] The orbifold group is $D_{4}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, X \cap E_{1}, X \cap Z, p_{4}, E_{4} \cap F} \mathbb{P}^{2}$$
is 4 and the picard number of $\widehat{M}$ is 2 . Here $p_{4}$ is a point in $E_{2}$ different from $E_{1} \cap E_{2}, X \cap E_{2}$.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}-2 E_{3}+3 E_{4}+4 E_{5}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-28.jpg?height=490&width=629&top_left_y=367&top_left_x=1182)

Case 3D.
\begin{itemize}
\item[-] The pair $(\widetilde{M}, \mathfrak{E})$ is biholomorphic to the pair of Case 2E.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-28.jpg?height=578&width=692&top_left_y=874&top_left_x=1152)

Case 3E.
\begin{itemize}
\item[-] The orbifold group is $D_{5}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, X \cap E_{1}, X \cap Z, p_{4}, E_{4} \cap F, E_{5} \cap F} \mathbb{P}^{2}$$
is 3 and the picard number of $\widehat{M}$ is 2 . Here $p_{4}$ is a point in $E_{2}$ different from $X \cap E_{2}, E_{1} \cap E_{2}$.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}-2 E_{3}+3 E_{4}+4 E_{5}+5 E_{6}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-28.jpg?height=578&width=692&top_left_y=1467&top_left_x=1152)

Case 3F.
\begin{itemize}
\item[-] The pair $(\widetilde{M}, \mathfrak{E})$ is biholomorphic to the pair of Case 3E.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-28.jpg?height=541&width=546&top_left_y=2050&top_left_x=1216)

Case 3G.
\begin{itemize}
\item[-] The orbifold group is $E_{6}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, X \cap E_{1}, X \cap Z, p_{4}, E_{4} \cap F, Z \cap E_{3}, E_{5} \cap F} \mathbb{P}^{2}$$
is 2 and the picard number of $\widehat{M}$ is 2 . Here $p_{4}$ is a point in $E_{2}$ different from $X \cap E_{2}, E_{1} \cap E_{2}$.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}-2 E_{3}+3 E_{4}+4 E_{5}+5 E_{7}-4 E_{6}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-29.jpg?height=580&width=692&top_left_y=174&top_left_x=1152)
6.2.2. $\boldsymbol{\alpha}>2 \boldsymbol{\beta}$. Weights and flows on $M_{2}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-29.jpg?height=352&width=623&top_left_y=870&top_left_x=752)
To get the fixed curve, blow-up should be taken at $p_{3}=X \cap E_{2}$. Weights and flows on $M_{3}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-29.jpg?height=490&width=769&top_left_y=1336&top_left_x=675)
Now $E_{3}$ has to be a fixed curve to ensure $E$ is connected. This means $\alpha=3 \beta$ and $E_{3}$ is the central curve in $E$. Similar proof of Lemma 6.2 shows $Y$ is not contained in $E$. Thus $E_{1} \cup E_{2}$ is one of the three chains of (-2)-curves in $E$, and this chain is of type $A_{2}$. The ending fixed point is $E_{1} \cap Y$, therefore it has weights $[p, q]=[2,3]$, which gives $\alpha=3, \alpha-\beta=2$. This shows $\alpha=3, \beta=1$. There must be one more blow-up at a point $p_{4}$ different from $X \cap E_{3}, E_{3} \cap E_{2}$ in $E_{3}$ to make it a (-2)-curve. Weights and flows on $M_{4}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-29.jpg?height=455&width=599&top_left_y=2123&top_left_x=761)

In $M_{4}$, there is only one chain of (-2)-curves. Therefore, we need to perform one more blow-up at the intersection $p_{5}=E_{4} \cap F$ to make $E_{4}$ a (-2)-curve. Weights and flows on $M_{5}$ are
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-30.jpg?height=537&width=705&top_left_y=296&top_left_x=709)

It is clear that the following proposition holds.
Proposition 6.9. In case (iii), when $\alpha>2 \beta$ and the orbifold group is non-cyclic, the pair $(\widetilde{M}, \mathfrak{E})$ must be a blow-up of $M_{5}$ with the $\mathbb{C}^{*}$-action described above.

Note that the intersection of $F$ and $Z$ is non-transverse. It is direct to check that $F^{2}=4$ in $M_{5}$ and blowing up $Y \cap Z$ will decrease the intersection number of $F$ by 4 . By examining all further blow-ups, we have

Proposition 6.10. In case (iii), when $\alpha>2 \beta$ and the orbifold group is non-cyclic, there are six possible $(\widetilde{M}, \mathfrak{E})$.
In the following we describe the $\operatorname{six}(\widetilde{M}, \mathfrak{E})$ in details. Note that the $\mathfrak{E}$ action is lifted from the action $t \curvearrowright[x: y:$ $z]=\left[t^{3} x: t y: z\right]$ on $\mathbb{P}^{2}$.

Case 3H.
\begin{itemize}
\item[-] The orbifold group is $D_{5}$.
\item[-] The degree of
$$\widetilde{M}=B l_{X \cap Y, X \cap E_{1}, X \cap E_{2}, p_{4}, E_{4} \cap F} \mathbb{P}^{2}$$
is 4 and the picard number of $\widehat{M}$ is 1 . Here $p_{4}$ is a point in $E_{2}$ different from $X \cap E_{3}, E_{2} \cap E_{3}$.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}+3 E_{3}+4 E_{4}+5 E_{5}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-30.jpg?height=589&width=715&top_left_y=1401&top_left_x=1139)

Case 3 I.
\begin{itemize}
\item[-] The pair $(\widetilde{M}, \mathfrak{E})$ is biholomorphic to the pair of Case 3E.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-30.jpg?height=587&width=696&top_left_y=2007&top_left_x=1147)

Case 3J.
\begin{itemize}
\item[-] The orbifold group is $E_{6}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, X \cap E_{1}, X \cap E_{2}, p_{4}, E_{4} \cap F, E_{5} \cap F} \mathbb{P}^{2}$$
is 3 and the picard number of $\widehat{M}$ is 1 . Here $p_{4}$ is a point in $E_{2}$ different from $X \cap E_{3}, E_{2} \cap E_{3}$.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}+3 E_{3}+4 E_{4}+5 E_{5}+6 E_{6}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-31.jpg?height=591&width=718&top_left_y=189&top_left_x=1139)

Case 3K.
\begin{itemize}
\item[-] The pair $(\widetilde{M}, \mathfrak{E})$ is biholomorphic to the pair of Case 3G.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-31.jpg?height=535&width=522&top_left_y=791&top_left_x=1238)

Case 3L.
\begin{itemize}
\item[-] The orbifold group is $E_{7}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, X \cap E_{1}, X \cap E_{2}, p_{4}, E_{4} \cap F, E_{5} \cap F, E_{6} \cap F} \mathbb{P}^{2}$$
is 2 and the picard number of $\widehat{M}$ is 1 . Here $p_{4}$ is a point in $E_{2}$ different from $X \cap E_{3}, E_{2} \cap E_{3}$.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}+3 E_{3}+4 E_{4}+5 E_{5}+6 E_{6}+7 E_{7}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-31.jpg?height=589&width=715&top_left_y=1356&top_left_x=1139)

Case 3M.
\begin{itemize}
\item[-] The orbifold group is $E_{8}$.
\item[-] The degree of
$$\tilde{M}=B l_{X \cap Y, X \cap E_{1}, X \cap E_{2}, p_{4}, E_{4} \cap F, E_{5} \cap F, E_{6} \cap F, E_{7} \cap F} \mathbb{P}^{2}$$
is 1 and the picard number of $\widehat{M}$ is 1 . Here $p_{4}$ is a point in $E_{2}$ different from $X \cap E_{3}, E_{2} \cap E_{3}$.
\item[-] $K_{\widetilde{M}}=-3 Z+E_{1}+2 E_{2}+3 E_{3}+4 E_{4}+5 E_{5}+6 E_{6}+$ $7 E_{7}+8 E_{8}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-31.jpg?height=533&width=526&top_left_y=1955&top_left_x=1233)
6.3. Conclusion. To summarize, concluding Propositions 5.8, 5.11, 6.5, 6.8, we obtain a list of candidates of pairs ( $\widehat{M}, \mathfrak{E}$ ), except the reversed Eguchi-Hanson, where $M=\widehat{M} \backslash E$ could potentially support Hermitian non-Kähler ALE gravitational instantons with structure group in $S U(2)$, and $\mathfrak{E}$ being the holomorphic extremal vector field up to constant multiples. These surfaces are listed in Table 4.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 4. Possible $(\widehat{M}, \mathfrak{E})$.}
\begin{tabular}[t]{|l|l|l|l|}
\hline Case & $\Gamma \subset S U(2)$ & Picard rank of $\widehat{M}$ & The $\mathfrak{E}$ action \\
\hline 1A & $A_{1}$ & 2 & $t \curvearrowright[x: y: z]=[t x: t y: z]$ on $\mathbb{P}^{2}$ \\
\hline 1B & $A_{1}$ & 3 & $t \curvearrowright[x: y: z]=[t x: t y: z]$ on $\mathbb{P}^{2}$ \\
\hline 1C & $A_{1}$ & 4 & $t \curvearrowright[x: y: z]=[t x: t y: z]$ on $\mathbb{P}^{2}$ \\
\hline 2A & $A_{1}$ & 3 & $t \curvearrowright[x: y: z]=\left[t^{-1} x: t^{-1} y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 2D & $A_{3}$ & 3 & $t \curvearrowright[x: y: z]=\left[t^{-1} x: t^{-1} y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 2E & $D_{4}$ & 3 & $t \curvearrowright[x: y: z]=\left[t^{-1} x: t^{-1} y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 3A & $A_{3}$ & 2 & $t \curvearrowright[x: y: z]=\left[t^{2} x: t y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 3C & $D_{4}$ & 2 & $t \curvearrowright[x: y: z]=\left[t^{2} x: t y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 3E & $D_{5}$ & 2 & $t \curvearrowright[x: y: z]=\left[t^{2} x: t y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 3G & $E_{6}$ & 2 & $t \curvearrowright[x: y: z]=\left[t^{2} x: t y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 3H & $D_{5}$ & 1 & $t \curvearrowright[x: y: z]=\left[t^{3} x: t y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 3J & $E_{6}$ & 1 & $t \curvearrowright[x: y: z]=\left[t^{3} x: t y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 3L & $E_{7}$ & 1 & $t \curvearrowright[x: y: z]=\left[t^{3} x: t y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline 3M & $E_{8}$ & 1 & $t \curvearrowright[x: y: z]=\left[t^{3} x: t y: z\right]$ on $\mathbb{P}^{2}$ \\
\hline
\end{tabular}
\end{table}

Proposition 6.11. If a Hermitian non-Kähler ALE gravitational instanton $(M, h)$ with structure group in $S U(2)$ other than the reversed Eguchi-Hanson exists, then $M$ would be one of the surfaces listed in Table 4. The corresponding holomorphic extremal vector field would be $\mathfrak{E}$ up to scaling.

\section*{7. The $\mathcal{A}$-functional and Bach-flat Kähler metrics}

We need to use finer techniques to detect whether $(\widehat{M}, \mathfrak{E})$ in Table 4 admits special Bach-flat Kähler metrics. For extremal Kähler metrics whose holomorphic extremal vector field induces a $\mathbb{C}^{*}$-action, explicitly knowing what the action is, we can calculate the minimum of its scalar curvature by combining symplectic and complex geometry techniques, following LeBrun-Simanca [15]. This will be done in this section.
7.1. Computing the minimum of scalar curvature. We calculate the minimum of $s_{g}$ for an extremal Kähler $g$ following the idea of [15]. It turns out that $\min s_{g}$ only depends on the Kähler class $[\omega]$ and the holomorphic extremal vector field. Recall $\mathfrak{K}=\nabla^{1,0} s_{g}=\frac{1}{2}\left(\nabla s_{g}-\sqrt{-1} J \nabla s_{g}\right)$ is the holomorphic extremal vector field. We only consider the situation that the complex surface (orbifold) $X$ is rational since this is enough for our application.

On a complex surface (or orbifold) $M$, given a Kähler metric $g$ in a Kähler class $[\omega]$, for a holomorphic field $\xi=\nabla^{1,0} f$ that admits a potential function $f: M \rightarrow \mathbb{C}$, where $\nabla^{1,0} f$ refers to the vector field dual to $\bar{\partial} f$, the Futaki invariant is defined as
$$\mathcal{F}(\xi,[\omega])=-\int f\left(s_{g}-s_{0}\right) d \mu$$
Here, $s_{g}$ is the scalar curvature of the metric $g$ and $s_{0}=8 \pi c_{1}[\omega] /[\omega]^{2}$ is the average of the scalar curvature. The volume form is $d \mu=\omega^{2} / 2$. It turns out that the Futaki invariant does not depend on the choice of the Kähler metric $g$ in the Kähler class $[\omega]$ and the potential function $f$, so it makes sense to write it as $\mathcal{F}(\xi,[\omega])$. Note that the Futaki invariant can also be defined even if the holomorphic field $\xi$ does not admit a potential function. The Calabi functional is defined as
$$\mathcal{C}(g)=\int s_{g}^{2} d \mu$$
on the space of Kähler metrics $g$. Restricted to a fixed Kähler class $[\omega]$, a Kähler metric $g \in[\omega]$ is a critical point of $\mathcal{C}$ over $[\omega]$ if and only if $\nabla^{1,0} s_{g}$ is a holomorphic vector field. Such metrics are the extremal Kähler metrics in the sense of Calabi. If a Kähler metric $g$ is an extremal metric, the following equality holds
$$\mathcal{C}(g)=s_{0}^{2} \int d \mu+\int\left(s_{g}-s_{0}\right)^{2} d \mu=32 \pi^{2} \frac{\left(c_{1}[\omega]\right)^{2}}{[\omega]^{2}}-\mathcal{F}(\mathfrak{E},[\omega])$$
with $\mathfrak{E}=\nabla^{1,0}\left(s_{g}-s_{0}\right)$, which is a holomorphic vector field.
Assumption. The Kähler metric $g$ in the Kähler class $[\omega]$ is an extremal Kähler metric on a rational complex 2-dimensional orbifold $X$, whose scalar curvature is nonconstant. The holomorphic extremal vector field $\mathfrak{K}$ induces a holomorphic $\mathbb{C}^{*}$-action. Orbifold points only appear in $c_{ \pm}$.

To compute $\mathcal{F}(\mathfrak{K},[\omega])$, assuming the existence of extremal metrics, it suffices to consider $\mathcal{F}(\mathfrak{K},[\omega])=-\int_{X}\left(s_{g}-\right.$ $\left.s_{0}\right)^{2} d \mu$. The function $s_{g}-s_{0}$ is a Hamiltonian function of the real holomorphic vector field $-2 \operatorname{Im} \mathfrak{K}=J \nabla s_{g}$, in the sense that
$$d\left(s_{g}-s_{0}\right)=-\omega(-2 \operatorname{Im} \mathfrak{K}, \cdot)$$
It is more convenient to work with the generator $\mathfrak{E}$ of the $\mathbb{C}^{*}$-action instead of $\mathfrak{K}$. Hence, let $\xi$ be the infinitesimal generator of the $S^{1}$-action associated to the primitive holomorphic $\mathbb{C}^{*}$-action, and $t$ be the moment map associated to this $S^{1}$-action with $\max t=-\min t=a$. That is,
$$d t=-\omega(\xi, \cdot) .$$
The average of $t$ over $X$ is denoted by $t_{0}$. There exists a nonzero positive constant $h$ such that
$$t-t_{0}=h\left(s_{g}-s_{0}\right) .$$

Initially in $X, c_{+}, c_{-}$might be fixed points. But as in [15], we can consider $\sigma: X^{\prime} \rightarrow X$, where $\sigma$ comes from blowing up $c_{ \pm}$suitably, so that the attractive set and repulsive set in $X^{\prime}$ are both fixed curves, and if there are orbifold points in $c_{ \pm}, \sigma$ resolves these orbifold points at the same time. The fact that repulsive and attractive sets in $X^{\prime}$ are fixed curves implies generic $\mathbb{C}^{*}$-orbits are rational curves with trivial self-intersection. This indicates that $X^{\prime}$ is fibered over a rational curve $\Sigma$, in the sense that after contracting some curves in some fibers, it becomes a ruled surface over $\Sigma \simeq \mathbb{P}^{1}$. Because blow-ups are only taken in $c_{ \pm}$, pulling back the Kähler form, $\sigma^{*} \omega$ is still a Kähler form defined on $X^{\prime} \backslash \sigma^{-1}\left(c_{ \pm}\right)$. Generic flows of the $\mathbb{C}^{*}$-action are flowing out of $\sigma^{-1}\left(c_{-}\right)$and flowing into $\sigma^{-1}\left(c_{+}\right)$. In $X^{\prime}, \sigma^{-1}\left(c_{ \pm}\right)$may be union of curves.

Example 7.1. Consider the quotient $X=\mathbb{P}^{2} / \mathbb{Z}_{3}$, where the $\mathbb{Z}_{3}$-action is defined by $\xi_{3} \cdot[x: y: z]=\left[\xi_{3}^{2} x: \xi_{3} y: z\right]$. Here, $\xi_{3}$ is the cubic unit root. The orbifold $X$ has three $A_{2}$ orbifold points located at $[1 ~: ~ 0: 0]$, [0 : $1: 0$ ], and $[0: 0: 1]$. We consider the holomorphic $\mathbb{C}^{*}$-action on $\mathbb{P}^{2}$ given by $t \cdot[x: y: z]=[t x: t y: z]$. This action has weights [1, 1] at [0 : 0 : 1] and weights [-1, 0] at $[1: 0: 0]$ and $[0: 0: 1]$. Note that this action commutes with the $\mathbb{Z}_{3}$-action, therefore descends to a $\mathbb{C}^{*}$-action on $X$.

In $X$, the attractive set $c_{+}$is the quotient $\{[x: y: 0]\} / \mathbb{Z}_{3}$, which is a $\mathbb{P}^{1}$. The repulsive set $c_{-}$is the point $[0: 0: 1]$. Denote $\{[x: y: 0]\} / \mathbb{Z}_{3}$ by $L$. Now we take the blow-up $\sigma$ :
\begin{itemize}
\item[-] $c_{-}=[0: 0: 1]$ is an orbifold point, so a blow-up needs to be taken at $[0: 0: 1]$. The resulting exceptional set is a union of two (-2)-curves, $E_{1}^{z}$ and $E_{2}^{z}$.
\item[-] $c_{+}=\{[x: y: 0]\} / \mathbb{Z}_{3}$ is a curve with two orbifold points, so blow-ups need to be taken at $[1: 0: 0],[0: 1:$ $0]$. They are $A_{2}$ singularities so the exceptional set of these two blow-ups are both unions of two (-2)-curves, $E_{1}^{x}, E_{2}^{x}, E_{1}^{y}, E_{2}^{y}$.
\end{itemize}

This way we get the minimal resolution of $X$. The following picture illustrates the situation.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-34.jpg?height=412&width=1253&top_left_y=277&top_left_x=436)
However, the repulsive set is still a fixed point $E_{1}^{z} \cap E_{2}^{z}$. To resolve this, we need to perform one more blow-up at $E_{1}^{z} \cap E_{2}^{z}$. The resulting exceptional curve of this blow-up is denoted by $E_{3}^{z}$, and the resulting surface is the desired $X^{\prime}$. Specifically, $E_{1}^{z} \cup E_{3}^{z} \cup E_{2}^{z}$ is $\sigma^{-1}\left(c_{-}\right)$, while $E_{2}^{y} \cup E_{1}^{y} \cup L \cup E_{1}^{x} \cup E_{2}^{x}$ is $\sigma^{-1}\left(c_{+}\right)$.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-34.jpg?height=468&width=550&top_left_y=894&top_left_x=786)
Generic $\mathbb{C}^{*}$-orbits are flowing from $E_{3}^{z}$ to $L$. If we consider the Kähler form $\omega$ on $X$ descended from the Fubini-Study metric $\omega_{F S}=\sqrt{-1} \partial \bar{\partial} \log \left(|x|^{2}+|y|^{2}+|z|^{2}\right)$ on $\mathbb{P}^{2}$, after passing to $X^{\prime}$, the pulled back Kähler form $\sigma^{*}(\omega)$ lives on $X^{\prime} \backslash \sigma^{-1}\left(c_{ \pm}\right)$. The moment map for the $S^{1}$-action on $X=\mathbb{P}^{2} / \mathbb{Z}_{3}$ is given by
$$[x: y: z] \mapsto \frac{|x|^{2}+|y|^{2}}{|x|^{2}+|y|^{2}+|z|^{2}},$$
and this is also the moment map for the $S^{1}$-action on $X^{\prime} \backslash \sigma^{-1}\left(c_{ \pm}\right)$. The symplectic quotient at level $t$ gives a symplectic form with area $\frac{1}{3} 2 \pi t$ on $\mathbb{P}^{1}$ (because of the $\mathbb{Z}_{3}$ quotient).

As in [15], there is a projection map
$$p: X^{\prime} \backslash \sigma^{-1}\left(c_{ \pm}\right) \rightarrow \Sigma \times(-a, a) .$$
The first factor is given by the fibration to $\Sigma$ while the second factor is the moment map $t$. Fibers of the map $p$ are the $S^{1}$-orbits. Fixed points of this $S^{1}$-action inside $X^{\prime}$ are denoted by $\alpha_{1}, \ldots \alpha_{m}$. For $t \notin\left\{t\left(\alpha_{1}\right), \ldots, t\left(\alpha_{m}\right)\right\}$, the restriction of $p$ over $\Sigma \times t$ has the structure of orbifold $S^{1}$-bundle over the orbifold $\Sigma \times t$. Globally the map $p$ provides a structure of orbifold $S^{1}$-bundle
$$p: Y \rightarrow \Sigma \times(-a, a) \backslash\left\{p\left(\alpha_{1}\right), \ldots, p\left(\alpha_{m}\right)\right\},$$
where $Y$ denotes the preimage of $\Sigma \times(-a, a) \backslash\left\{p\left(\alpha_{1}\right), \ldots, p\left(\alpha_{m}\right)\right\}$ under the projection map $p$, excluding the fixed points of the $S^{1}$-action.

On each $\Sigma \times t$ with $t \notin\left\{t\left(\alpha_{1}\right), \ldots, t\left(\alpha_{m}\right)\right\}$ there is the metric $g(t)$ induced by the symplectic reduction. The orthogonal complement of the $S^{1}$-orbits in $Y$ with respect to the Kähler metric on $Y$ defines a connection 1-form for the orbifold $S^{1}$-bundle. Denote the curvature two-form of this $U(1)$-connection by $\Omega$. Let $t_{j}=t\left(\alpha_{j}\right)$ be critical values of the moment map. If we set $A(t)$ as the area of $(\Sigma, g(t))$ and $t$ is not a critical value, then same calculation in page 314 of [15] gives
$$\frac{d A}{d t}(t)=\int_{\Sigma \times\{t\}}-\sqrt{-1} \Omega=-2 \pi c_{1}(Y)\left[\Sigma_{t}\right] .$$

Here $\left[\Sigma_{t}\right]$ is the homology class of $\Sigma \times t$ and $c_{1}(Y)$ is the Chern class of the orbifold $S^{1}$-bundle. For any $b, c \in(-a, a)$, if we let $S_{j} \subset \Sigma \times(-a, a) \backslash\left\{p\left(\alpha_{1}\right), \ldots, p\left(\alpha_{m}\right)\right\}$ be small 2-spheres around points $p\left(\alpha_{j}\right)$, we then have
$$\left[\Sigma_{c}\right]-\left[\Sigma_{b}\right]=\sum_{t_{j} \in[b, c]}\left[S_{j}\right] .$$
Here $S_{j}$ is assigned with the outward pointing orientation. Then,
$$-2 \pi c_{1}(Y)\left[\Sigma_{c}\right]+2 \pi c_{1}(Y)\left[\Sigma_{b}\right]=-2 \pi \sum_{t_{j} \in[b, c]} c_{1}(Y)\left[S_{j}\right] .$$
Generally, if the weights of a fixed point $\alpha$ are $[r, s]$, then the Chern class of the orbifold $S^{1}$-bundle, evaluated on the class $[S]$ of 2 -sphere around $p(\alpha)$, can be calculated as
$$c_{1}(Y)[S]=-\frac{1}{r} .$$
In particular, if weights of the fixed point $\alpha_{j}$ is $\left[r_{j}, s_{j}\right]$ (as $\alpha_{j}$ is not in $c_{ \pm}$, we can always assume $r_{j}>0, s_{j}<0$ ), we then have $c_{1}(Y)\left[S_{j}\right]=-\frac{1}{r_{j} s_{j}}$. In conclusion, with equation (21), we have the formula
$$-2 \pi c_{1}(Y)\left[\Sigma_{c}\right]+2 \pi c_{1}(Y)\left[\Sigma_{b}\right]=2 \pi \sum_{t_{j} \in[b, c]} \frac{1}{r_{j} s_{j}},$$
from which it follows that
$$\frac{d^{2} A}{d t^{2}}(t)=2 \pi \sum \frac{1}{r_{j} s_{j}} \delta_{t_{j}}$$
Here $\delta_{t_{j}}$ is the Dirac measure at $t=t_{j}$. We adopt the notations $-2 \pi c_{1}(Y)\left[\Sigma_{a}\right]$ and $-2 \pi c_{1}(Y)\left[\Sigma_{-a}\right]$ to denote the limits of $-2 \pi c_{1}(Y)\left[\Sigma_{t}\right]$ as $t$ approaches $a$ and $-a$, respectively. Equation (23) gives
$$c_{1}(Y)\left[\Sigma_{a}\right]-c_{1}(Y)\left[\Sigma_{-a}\right]=\sum_{t_{j} \in(-a, a)}-\frac{1}{r_{j} s_{j}} .$$

Consider the chains of rational curves $E_{j}^{\prime}$ and $E_{j}$, obtained by tracing the $\mathbb{C}^{*}$-action forward from $\alpha_{j}$ to $c_{+}$and backward from $\alpha_{j}$ to $c_{-}$, respectively. For a generic $\mathbb{C}^{*}$-orbit $F$ in $M$, its area is $\omega(F)=4 \pi a$. As approaching to singular orbits, generic orbits break into several orbits with multiplicities. If $\alpha_{j}$ is a fixed point with weights $\left[r_{j}, s_{j}\right]$, then generic orbits $F$ break into $r_{j} E_{j}^{\prime}-s_{j} E_{j}$. In particular, $\omega\left(r_{j} E_{j}^{\prime}-s_{j} E_{j}\right)=\omega(F)=4 \pi a$. Computation in Theorem 3 in [15] now completely carries over:
$$\int_{M} t s_{g} d \mu=\omega(F)\left(\omega\left(c_{+}\right)-\omega\left(c_{-}\right)\right)$$
$$\begin{aligned}
& \int_{M} d \mu=2 \pi \int_{-a}^{a} A(t) d t \\
= & \frac{\omega(F)^{2}}{8}\left[4 \frac{\omega\left(c_{+}\right)+\omega\left(c_{-}\right)}{\omega(F)}+\sum_{j} \frac{1}{r_{j} s_{j}}\left(\frac{\omega\left(r_{j} E_{j}^{\prime}\right)-\omega\left(-s_{j} E_{j}\right)}{\omega(F)}\right)^{2}+c_{1}(Y)\left[\Sigma_{a}\right]-c_{1}(Y)\left[\Sigma_{-a}\right]\right],
\end{aligned}$$
$$\begin{aligned}
& \int_{M} t d \mu=2 \pi \int_{-a}^{a} t A(t) d t \\
= & \frac{\omega(F)^{3}}{96 \pi}\left[6 \frac{\omega\left(c_{+}\right)-\omega\left(c_{-}\right)}{\omega(F)}-\sum_{j} \frac{1}{r_{j} s_{j}}\left(\frac{\omega\left(r_{j} E_{j}^{\prime}\right)-\omega\left(-s_{j} E_{j}\right)}{\omega(F)}\right)^{3}+c_{1}(Y)\left[\Sigma_{-a}\right]+c_{1}(Y)\left[\Sigma_{a}\right]\right],
\end{aligned}$$
$$\begin{aligned}
& \int_{M} t^{2} d \mu=2 \pi \int_{-a}^{a} t^{2} A(t) d t \\
= & \frac{\omega(F)^{4}}{768 \pi^{2}}\left[8 \frac{\omega\left(c_{+}\right)+\omega\left(c_{-}\right)}{\omega(F)}+\sum_{j} \frac{1}{r_{j} s_{j}}\left(\frac{\omega\left(r_{j} E_{j}^{\prime}\right)-\omega\left(-s_{j} E_{j}\right)}{\omega(F)}\right)^{4}+c_{1}(Y)\left[\Sigma_{a}\right]-c_{1}(Y)\left[\Sigma_{-a}\right]\right] .
\end{aligned}$$

For simplicity, let
$$T=\left(T_{s}, T_{0}, T_{1}, T_{2}\right):=\left(\int_{M} t s_{g} d \mu, \int_{M} d \mu, \int_{M} t d \mu, \int_{M} t^{2} d \mu\right)$$
Then
$$s_{0}=\frac{8 \pi c_{1}[\omega]}{[\omega]^{2}}=\frac{4 \pi c_{1}[\omega]}{T_{0}} .$$

Example 7.2. Again we take the above example $\mathbb{P}^{2} / \mathbb{Z}_{3}$. The region $X^{\prime} \backslash \sigma^{-1}\left\{c_{ \pm}\right\}$is biholomorphic to $X \backslash\{[0: 0:$ $\left.1],[x: y: 0] / \mathbb{Z}_{3}\right\}$.

To compute $c_{1}(Y)\left[\Sigma_{-a}\right]$, note that the orbifold point [ $0: 0: 1$ ] has weights [1,1] and is an $A_{2}$ orbifold point. By (22), it is direct to see
$$c_{1}(Y)\left[\Sigma_{-a}\right]=-\frac{1}{3} .$$

To compute $c_{1}(Y)\left[\Sigma_{a}\right]$, the $S^{1}$-bundle over $\Sigma_{t}$ with $t$ close to $a$, after passing to the orbifold cover, is the dual of the normal bundle of $\Sigma_{t} \simeq c_{+}$, as described by equations (3.12), (3.13) in [15]. The curve $c_{+}$in $X$ lifted to the orbifold cover has self-intersection 1. Since the order of the orbifold structure group is 3, we have
$$c_{1}(Y)\left[\Sigma_{a}\right]=-\frac{1}{3} .$$

There is no fixed point when $t \in(-a, a)$ and equation (25) holds, as expected. Moreover, for the metric $\omega$ on $\mathbb{P}^{2} / \mathbb{Z}_{3}$ descended from the standard Fubini-Study metric, $\omega\left(c_{+}\right)=\frac{\pi}{3}, \omega\left(c_{-}\right)=0, \omega(F)=2 \pi$. As there is no fixed point when $t \in(-a, a)$, equations (26)-(29) give
$$T=\left(4 \pi^{2} / 3,2 \pi^{2} / 3, \pi^{2} / 9, \pi^{2} / 18\right) .$$
The area of $\omega$ is exactly $2 \pi^{2} / 3$ because of the $\mathbb{Z}_{3}$ quotient. And the scalar curvature of $\omega_{F S}=\sqrt{-1} \partial \bar{\partial} \log \left(|x|^{2}+|y|^{2}+|z|^{2}\right)$ is 12 because of our choice of $\omega_{F S}$ on $\mathbb{P}^{2}$, which is compatible with $\int_{X} t s_{g} d \mu=12 \int_{X} t d \mu=4 \pi^{2} / 3$ by our computation.

Example 7.3. Take Case 2D as another example.
To compute $c_{1}(Y)\left[\Sigma_{a}\right]$, note $c_{+}$as a fixed point has weights [-1, -1]. The orbifold $S^{1}$-bundle over small spheres around the point $c_{+}$has Chern number -1. But we should use the opposite orientation here (the orientation given by the symplectic form on $\Sigma_{t}$ ) when we compute $c_{1}(Y)\left[\Sigma_{a}\right]$. Thus,
$$c_{1}(Y)\left[\Sigma_{a}\right]=1 .$$

To compute $c_{1}(Y)\left[\Sigma_{-a}\right]$, observe that $c_{-}$in $\widehat{M}$ is the orbifold point resulting from contracting $E \subset \widetilde{M}$. Since this orbifold point is an $A_{3}$ singularity, Theorem 4.6 tells us that the weights of the point $c_{-}$are $\left[\frac{1}{2}, \frac{1}{2}\right]$. So we have
$$c_{1}(Y)\left[\Sigma_{-a}\right]=\frac{1}{4}\left(-\frac{1}{\frac{1}{2} \times \frac{1}{2}}\right)=-1 .$$

There are three fixed points when $t \in(-a, a)$, with weights $[-2,1],[-1,1],[-2,1]$, and equation (25) holds as expected
$$c_{1}(Y)\left[\Sigma_{a}\right]-c_{1}(Y)\left[\Sigma_{-a}\right]=2=\frac{1}{2}+1+\frac{1}{2} .$$

Now the extremal Futaki invariant can be computed as
$$\begin{aligned}
\mathcal{F}(\mathfrak{E},[\omega]) & =-\int_{M}\left(s_{g}-s_{0}\right)^{2} d \mu \\
& =-\frac{1}{h} \int_{M} t s_{g} d \mu+s_{0} \frac{1}{h} \int_{M} t d \mu \\
& =-\frac{1}{h} T_{s}+s_{0} \frac{1}{h} T_{1}
\end{aligned}$$
with $h$ defined by (20). Multiplying (20) by $t$ and take the integration one obtains
$$h=\left(-T_{2}+\frac{1}{T_{0}} T_{1}^{2}\right) /\left(-T_{s}+s_{0} T_{1}\right) .$$

The minimum of $s_{g}$ is
$$\begin{aligned}
\min s_{g} & =\min \left\{\frac{1}{h}\left(t-t_{0}\right)\right\}+s_{0} \\
& =\frac{1}{h} \min t-\frac{2}{h[\omega]^{2}} \int_{M} t d \mu+\frac{8 \pi c_{1}[\omega]}{[\omega]^{2}} \\
& =-\frac{\omega(F)}{4 \pi h}-\frac{1}{h T_{0}} T_{1}+\frac{4 \pi c_{1}[\omega]}{T_{0}} .
\end{aligned}$$
7.2. Bach-flat Kähler metrics and its scalar curvature. The computation we just performed gives a function
$$\min _{\mathfrak{E}} s_{g}([\omega]):=-\frac{\omega(F)}{4 \pi h}-\frac{1}{h T_{0}} T_{1}+\frac{4 \pi c_{1}[\omega]}{T_{0}}$$
defined on the Kähler cone $\mathcal{K}$. When there is an extremal Kähler metric in the Kähler class $[\omega]$ with extremal vector field proportional to the vector field $\mathfrak{E}$, the function exactly coincides with the minimum of its scalar curvature. We added the lower index $\mathfrak{E}$ to emphasize the dependence of the function on the $\mathbb{C}^{*}$-action induced by $\mathfrak{E}$. The function $\min _{\mathfrak{E}} s_{g}$ defined on $\mathcal{K}$ is clearly homogeneous. Note that it is possible that $-T_{s}+s_{0} T_{1}=0$ in (20), but in this case, as a consequence, $\int t\left(t-t_{0}\right)=\int\left(t-t_{0}\right)^{2}=0$, which is absurd. Hence when $-T_{s}+s_{0} T_{1}=0$, the corresponding Kähler class can never contain an extremal Kähler metric with $\mathfrak{E}$ as the extremal vector field up to scaling.

Example 7.4 (Eguchi-Hanson). Recall that the reversed Eguchi-Hanson metric is a Hermitian non-Kähler ALE gravitational instanton as in Example 2.6. The compactified surface $\widehat{M}$ is $H_{2}=\mathbb{P}(\mathcal{O} \oplus \mathcal{O}(2))$ contracting the curve $C_{\infty}$. The Picard number of $\widehat{M}$ is 1 . Choosing $\mathfrak{K}$ as the holomorphic vector field which preserves the curve $C_{0}$ and the curve $C_{\infty}$, while flows points from $C_{\infty}$ to $C_{0}$, our calculation in Section 7.1 can be applied. If we assume that $[\omega]$ is the Kähler class such that $[\omega]\left(C_{0}\right)=1$, it is direct to check by our above formulas that
$$\min _{\mathfrak{E}} s_{g}([\omega])=0 .$$
This shows that, if there is an extremal metric that does not have constant scalar curvature with $\mathfrak{E}$ as the holomorphic extremal vector field, then the minimum of the scalar curvature is 0 and is achieved at the orbifold point. And indeed, by our correspondence Theorem 1.3, there is the extremal metric on $\widehat{M}$ whose scalar curvature is nonnegative, and vanishes exactly at the orbifold point.

We will see that the function $\min _{\mathfrak{E}} s_{g}$ turns out to be always nonzero over the region of the Kähler cone $\mathcal{K}$ where special Bach-flat Kähler metrics could exist, for pairs ( $\widehat{M}, \mathfrak{E}$ ) in Table 4. It follows that there is no Hermitian non-Kähler ALE gravitational instanton with structure group in $S U(2)$, except the reversed Eguchi-Hanson. To compute $\min _{\mathfrak{E}} S_{g}$, we only need to
\begin{itemize}
\item[(1)] use (26)-(29) to compute $T$;
\item[(2)] use (33) to compute $h$;
\item[(3)] compute $\min _{\mathfrak{E}} s_{g}$ using (34).
\end{itemize}
It suffices to know $\omega\left(c_{ \pm}\right), \omega\left(E_{i}\right), \omega\left(E_{i}^{\prime}\right), \omega(F), c_{1}[\omega]$, and $c_{1}(Y)\left[\Sigma_{ \pm a}\right]$ in each case. The number of variables one needs to parametrize $\mathcal{K}(\widehat{M}) / \mathbb{R}_{+}$is the picard number minus one. Mathematical software Mathematica will be used to simplify the expressions since the computation is complicated. The notations in each figure are adapted to be compatible with our discussion in Section 7.1. The notation $\sum$ in the following denotes cyclic sum. For example, if there are variables $a, b, c$ and $S$ is the set of permutations $\sigma$ of $a, b, c$, then $\sum a^{r} b^{s} c^{t}:=\sum_{\sigma \in S} \sigma(a)^{r} \sigma(b)^{s} \sigma(c)^{t}$. For example, $\sum a=2(a+b+c)$. The Chern numbers $c_{1}(Y)\left[\Sigma_{ \pm a}\right]$ can be computed as in Example 7.2-7.3 and we shall list them for each case without details.

Case 1A.
\begin{itemize}
\item[-] There is only one fixed point $E_{1} \cap E_{1}^{\prime}$ with weights [-1, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=-1, c_{1}(Y)\left[\Sigma_{-a}\right]=-2$.
\item[-] Set $\omega\left(c_{+}\right)=1, \omega\left(E_{1}^{\prime}\right)=a$. Then
$$\omega\left(E_{1}\right)=(1-a) / 2, \omega(F)=(1+a) / 2,$$
and $\omega\left(c_{-}\right)=0$.
\item[-] $c_{1}[\omega]=2+a$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-37.jpg?height=352&width=490&top_left_y=2245&top_left_x=1311)

Here $a$ must satisfy the bound $0<a<1$. The function $\min _{\mathfrak{E}} s_{g}$ is given by
$$\min _{\mathfrak{E}} s_{g}=-\frac{48 \pi a\left(a^{4}-2 a^{3}-8 a^{2}+2 a-1\right)}{3 a^{6}-18 a^{5}+3 a^{4}+12 a^{3}+9 a^{2}+6 a+1},$$
which is positive when $0<a<1$.
Case 1B.
\begin{itemize}
\item[-] There are two fixed points $E_{1} \cap E_{1}^{\prime}, E_{2} \cap E_{2}^{\prime}$, with weights $[-1,1],[-1,1]$.
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=0, c_{1}(Y)\left[\Sigma_{-a}\right]=-2$.
- Set $\omega\left(c_{+}\right)=1, \omega\left(E_{1}^{\prime}\right)=a, \omega\left(E_{2}^{\prime}\right)=b$. Then
$$\begin{gathered}
\omega\left(E_{1}\right)=(1+b-a) / 2, \omega\left(E_{2}\right)=(1+a-b) / 2, \\
\omega(F)=(1+a+b) / 2 .
\end{gathered}$$
Moreover $\omega\left(c_{-}\right)=0$.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-38.jpg?height=376&width=505&top_left_y=415&top_left_x=1296)
\item[-] $c_{1}[\omega]=2+a+b$.
\end{itemize}

Here we have $|a-b|<1$ and $a, b$ are positive. Hence,
$$\begin{aligned}
\min _{\mathfrak{E}} s_{g}= & 48 \pi\left(\sum a-2 \sum a^{2}+8 \sum a^{3}+2 \sum a^{4}-\sum a^{5}+4 \sum a b+12 \sum a^{3} b+3 \sum a^{4} b\right. \\
& \left.-6 \sum a^{2} b^{2}-2 \sum a^{3} b^{2}\right) / \\
& \left(1+6 \sum a+9 \sum a^{2}+12 \sum a^{3}+3 \sum a^{4}-18 \sum a^{5}+3 \sum a^{6}+15 \sum a b+36 \sum a^{2} b\right. \\
& \left.+36 \sum a^{3} b+6 \sum a^{4} b-18 \sum a^{5} b+9 \sum a^{2} b^{2}+45 \sum a^{4} b^{2}+12 \sum a^{3} b^{2}-30 \sum a^{3} b^{3}\right)
\end{aligned}$$
Using some elementary inequalities, we have
\begin{itemize}
\item[-] $6 \sum a^{3} b-6 \sum a^{2} b^{2} \geq 0$.
\item[-] $2 \sum a^{4} b-2 \sum a^{3} b^{2} \geq 0$.
\item[-] $\sum a^{4} b-\sum a^{5}=-(a-b)^{2}\left(\sum a^{3}+\sum a^{2} b\right)>-\sum a^{3}-\sum a^{2} b \geq-2 \sum a^{3}$.
\item[-] $\sum a+\sum a^{3} \geq 2 \sum a^{2}$.
\end{itemize}

Add these together and note the extra term $8 \sum a^{3}$ in the numerator, we get that the numerator is positive. Therefore, $\min _{\mathfrak{E}} s_{g} \neq 0$ on the entire Kähler cone $\mathcal{K}$.

Case 1C.
\begin{itemize}
\item[-] There are three fixed points $E_{1} \cap E_{1}^{\prime}, E_{2} \cap E_{2}^{\prime}, E_{3} \cap E_{3}^{\prime}$, with weights [-1, 1], [-1, 1], [-1, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=1, c_{1}(Y)\left[\Sigma_{-a}\right]=-2$.
- Set $\omega\left(c_{+}\right)=1, \omega\left(E_{1}^{\prime}\right)=a, \omega\left(E_{2}^{\prime}\right)=b, \omega\left(E_{3}^{\prime}\right)=c$. Then
$$\begin{aligned}
\omega\left(E_{1}\right) & =(1-a+b+c) / 2, \omega\left(E_{2}\right)
\end{aligned}=(1+a-b+c) / 2, .$$
Moreover $\omega\left(c_{-}\right)=0$.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-38.jpg?height=374&width=599&top_left_y=1586&top_left_x=1253)
\item[-] $c_{1}[\omega]=2+a+b+c$.
\end{itemize}

Here we have $a-b-c,-a+b-c,-a-b+c<1$ and $a, b, c$ are positive. Hence,
$$\begin{aligned}
\min _{\mathfrak{E}} s_{g}= & 48 \pi\left(\frac{1}{2} \sum a-\sum a^{2}+4 \sum a^{3}+\sum a^{4}-\frac{1}{2} \sum a^{5}+4 \sum a b+12 \sum a^{3} b+3 \sum a^{4} b\right. \\
& \left.-6 \sum a^{2} b^{2}-2 \sum a^{3} b^{2}+6 \sum a b c+6 \sum a^{2} b c-3 \sum a^{2} b^{2} c+4 \sum a^{3} b c\right) / \\
& \left(1+3 \sum a+\frac{9}{2} \sum a^{2}+6 \sum a^{3}+\frac{3}{2} \sum a^{4}-9 \sum a^{5}+\frac{3}{2} \sum a^{6}+15 \sum a b+36 \sum a^{2} b\right. \\
& +36 \sum a^{3} b+6 \sum a^{4} b-18 \sum a^{5} b+9 \sum a^{2} b^{2}+45 \sum a^{4} b^{2}+12 \sum a^{3} b^{2}-30 \sum a^{3} b^{3} \\
& \left.+18 \sum a^{2} b^{2} c+20 \sum a b c+54 \sum a^{2} b c+36 \sum a^{3} b c+3 \sum a^{4} b c+12 \sum a^{3} b^{2} c-3 \sum a^{2} b^{2} c^{2}\right) .
\end{aligned}$$
Elementary inequalities give
\begin{itemize}
\item[-] $3 \sum a^{3} b c-3 \sum a^{2} b^{2} c \geq 0$.
\end{itemize}
\begin{itemize}
\item[-] $2 \sum a^{4} b-2 \sum a^{3} b^{2} \geq 0$.
\item[-] $\sum a^{4} b-\frac{1}{2} \sum a^{5}=a^{4}(b+c-a)+b^{4}(a+c-b)+c^{4}(a+b-c)>-\frac{1}{2} \sum a^{4}$.
\item[-] $6 \sum a^{3} b-6 \sum a^{2} b^{2} \geq 0$.
\item[-] $\frac{1}{2} \sum a+2 \sum a^{3}-\sum a^{2} \geq 0$.
\end{itemize}

Therefore the numerator is positive. The function $\min _{\mathfrak{E}} s_{g} \neq 0$ on the Kähler cone $\mathcal{K}$.
Case 2A.
\begin{itemize}
\item[-] There are three fixed points, $E_{1} \cap E_{1}^{\prime}, E_{2} \cap E_{2}^{\prime}, E_{3} \cap E_{3}^{\prime}$, with weights [-1, 1], [-1, 1], [-1, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=1, c_{1}(Y)\left[\Sigma_{-a}\right]=-2$.
- Set $\omega\left(E_{1}^{\prime}\right)=a, \omega\left(E_{2}^{\prime}\right)=b, \omega\left(E_{3}^{\prime}\right)=1$. Then
$$\begin{gathered}
\omega\left(E_{1}\right)=(-a+b+1) / 2, \omega\left(E_{2}\right)=(a-b+1) / 2 \\
\omega\left(E_{3}\right)=(a+b-1) / 2, \omega(F)=(a+b+1) / 2
\end{gathered}$$
Moreover $\omega\left(c_{ \pm}\right)=0$.
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-39.jpg?height=391&width=483&top_left_y=432&top_left_x=1308)
\item[-] $c_{1}[\omega]=a+b+1$.
\end{itemize}

Here we have $|a-b|<1, a+b>1$, and $a, b>0$. Hence,
$$\begin{aligned}
\min _{\mathfrak{E}} s_{g}= & 16 \pi\left(1+\sum a\right)\left(-1+4 \sum a-6 \sum a^{2}+4 \sum a^{3}-\sum a^{4}+4 \sum a^{3} b-3 \sum a^{2} b^{2}\right) \\
& \left(1-6 \sum a+15 \sum a^{2}+\sum a b-20 \sum a^{3}+4 \sum a^{2} b+15 \sum a^{4}+4 \sum a^{3} b-3 \sum a^{2} b^{2}\right. \\
& \left.-6 \sum a^{5}+2 \sum a^{4} b+4 \sum a^{3} b^{2}+\sum a^{6}-6 \sum a^{5} b+15 \sum a^{4} b^{2}-10 \sum a^{3} b^{3}\right) .
\end{aligned}$$
The numerator can be rewritten as
$$16 \pi\left(1+\sum a\right)\left(-1+4 \sum a-6 \sum a^{2}+4 \sum a^{3}-(a-b)^{4}\right) .$$
If either $a$ or $b$ is greater than or equal to one, then we have the following inequality
$$-1+4 \sum a-6 \sum a^{2}+4 \sum a^{3}-(a-b)^{4} \geq-1+2 \sum a^{2}-(a-b)^{4}>2 \sum a^{2}-2>0 .$$
If $a$ and $b$ are both less than one, then
$$\begin{aligned}
& -1+4 \sum a-6 \sum a^{2}+4 \sum a^{3}-\sum a^{4}+4 \sum a^{3} b-3 \sum a^{2} b^{2} \\
> & 3 \sum a-6 \sum a^{2}+3 \sum a^{3}+4 \sum a^{3} b-3 \sum a^{2} b^{2}>0
\end{aligned}$$
Thus, we conclude that $\min _{\mathfrak{E}} s_{g} \neq 0$ on the entire Kähler cone $\mathcal{K}$.
Case 2D.
\begin{itemize}
\item[-] There are three fixed points, $E_{1} \cap E_{1}^{\prime}, E_{2} \cap E_{2}^{\prime}, E_{3} \cap E_{3}^{\prime}$, with weights [-2, 1], [-1, 1], [-2, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=1, c_{1}(Y)\left[\Sigma_{-a}\right]=-1$.
\item[-] Set $\omega\left(E_{2}^{\prime}\right)=1, \omega\left(E_{1}^{\prime}\right)=a, \omega\left(E_{3}^{\prime}\right)=b$. Then
$$\begin{gathered}
\omega\left(E_{1}\right)=(2+b-a) / 4, \omega\left(E_{2}\right)=(a+b) / 2, \\
\omega\left(E_{3}\right)=(2+a-b) / 4, \omega(F)=(2+a+b) / 2 .
\end{gathered}$$
Moreover $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=1+a+b$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-39.jpg?height=462&width=657&top_left_y=1680&top_left_x=1227)
Here we have the bound $|a-b|<2$ and $a, b>0$. Hence,
$$\begin{aligned}
\min _{\mathfrak{E}} s_{g}= & 32 \pi\left(1+\sum a\right)\left(8 \sum a-12 \sum a^{2}+8 \sum a^{3}-\sum a^{4}+12 \sum a b+4 \sum a^{3} b-3 \sum a^{2} b^{2}\right) \\
& \left(32 \sum a^{2}-32 \sum a^{3}+32 \sum a^{4}-12 \sum a^{5}+\sum a^{6}+32 \sum a b+32 \sum a^{2} b+32 \sum a^{3} b+4 \sum a^{4} b\right. \\
& \left.-6 \sum a^{5} b+8 \sum a^{3} b^{2}+15 \sum a^{4} b^{2}-10 \sum a^{3} b^{3}\right)
\end{aligned}$$
Elementary inequalities argument gives
\begin{itemize}
\item[] $\cdot 3 \sum a^{3} b-3 \sum a^{2} b^{2} \geq 0$.
\item[-] $\sum a^{3} b-\sum a^{4}=-(a-b)^{2}\left(\sum a^{2}+\frac{1}{2} \sum a b\right)>-4 \sum a^{2}-2 \sum a b$ 。
\end{itemize}
\begin{itemize}
\item[-] $8 \sum a+8 \sum a^{3} \geq 16 \sum a^{2}$.
\end{itemize}

Add these together we get that the numerator is positive. Hence we have $\min _{\mathfrak{E}} s_{g} \neq 0$ on the entire Kähler cone $\mathcal{K}$.
Case 2E.
\begin{itemize}
\item[-] There are three fixed points, $E_{1} \cap E_{1}^{\prime}, E_{2} \cap E_{2}^{\prime}, E_{3} \cap E_{3}^{\prime}$, with weights [-2, 1], [-2, 1], [-2, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=1, c_{1}(Y)\left[\Sigma_{-a}\right]=-\frac{1}{2}$.
\item[-] Set $\omega\left(E_{1}^{\prime}\right)=1, \omega\left(E_{2}^{\prime}\right)=a, \omega\left(E_{3}^{\prime}\right)=b$. Then
$$\begin{gathered}
\omega\left(E_{1}\right)=(a+b) / 2, \omega\left(E_{2}\right)=(1+b) / 2, \\
\omega\left(E_{3}\right)=(1+a) / 2, \omega(F)=1+a+b .
\end{gathered}$$
Moreover $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=1+a+b$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-40.jpg?height=466&width=662&top_left_y=305&top_left_x=1225)

Here $a, b>0$. Hence,
$$\begin{aligned}
\min _{\mathfrak{E}} s_{g}= & 8 \pi\left(1+\sum a\right)\left(\sum a+\sum a^{3}+3 \sum a b+6 \sum a^{2} b+\sum a^{3} b\right) / \\
& \left(\sum a^{2}+\sum a^{4}+\sum a b+4 \sum a^{2} b+4 \sum a^{3} b+2 \sum a^{4} b+3 \sum a^{2} b^{2}+4 \sum a^{3} b^{2}+\sum a^{4} b^{2}\right) .
\end{aligned}$$

Clearly this is positive. Therefore, $\min _{\mathfrak{E}} s_{g}>0$ on the entire Kähler cone.
Case 3A.
\begin{itemize}
\item[-] There are two fixed points $E_{1} \cap E_{1}^{\prime}, E_{2} \cap E_{2}^{\prime}$, with weights $[-2,1],[-1,1]$.
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=\frac{1}{2}, c_{1}(Y)\left[\Sigma_{-a}\right]=-1$.
\item[-] Set $\omega\left(E_{3}\right)=1, \omega\left(E_{2}\right)=a$. Then
$$\begin{gathered}
\omega\left(E_{1}\right)=1-a, \omega\left(E_{1}^{\prime}\right)=2 a \\
\omega\left(E_{2}^{\prime}\right)=2-a, \omega(F)=2
\end{gathered}$$
Moreover $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=2+a$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-40.jpg?height=451&width=604&top_left_y=1113&top_left_x=1248)

Here $0<a<1$. Hence,
$$\min _{\mathfrak{E}} s_{g}=-\frac{8 \pi(a+2)\left(9 a^{3}-26 a^{2}+24 a-8\right)}{a\left(21 a^{4}-84 a^{3}+128 a^{2}-96 a+32\right)} .$$

It is easy to verify that this is positive when $0<a<1$. Therefore, $\min _{\mathfrak{E}} s_{g}>0$ on the entire Kähler cone $\mathcal{K}$.

Case 3C.
\begin{itemize}
\item[-] There are two fixed points $E_{1} \cap E_{1}^{\prime}, E_{2} \cap E_{2}^{\prime}$, with weights $[-2,1],[-2,1]$.
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=\frac{1}{2}, c_{1}(Y)\left[\Sigma_{-a}\right]=-\frac{1}{2}$.
\item[-] Set $\omega\left(E_{3}\right)=1, \omega\left(E_{2}\right)=a$. Then
$$\begin{gathered}
\omega\left(E_{1}\right)=1-a, \omega\left(E_{1}^{\prime}\right)=2 a \\
\omega\left(E_{2}^{\prime}\right)=2-2 a, \omega(F)=2
\end{gathered}$$
Moreover $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=2$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-40.jpg?height=550&width=700&top_left_y=1830&top_left_x=1203)

Here $0<a<1$. Hence,
$$\min _{\mathfrak{E}} s_{g}=\frac{4 \pi}{a-a^{2}} .$$

Clearly this is positive. Therefore $\min _{\mathfrak{E}} s_{g}>0$ on the entire Kähler cone $\mathcal{K}$.

Case 3E.
\begin{itemize}
\item[-] There are two fixed points $E_{1} \cap E_{1}^{\prime}, E_{2} \cap E_{2}^{\prime}$, with weights [-2, 1], [-3, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=\frac{1}{2}, c_{1}(Y)\left[\Sigma_{-a}\right]=-\frac{1}{3}$.
\item[-] Set $\omega\left(E_{3}\right)=1, \omega\left(E_{2}\right)=a$. Then
$$\begin{gathered}
\omega\left(E_{1}\right)=1-a, \omega\left(E_{1}^{\prime}\right)=2 a, \\
\omega\left(E_{2}^{\prime}\right)=2-3 a, \omega(F)=2 .
\end{gathered}$$
Moreover $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=2-a$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-41.jpg?height=589&width=726&top_left_y=189&top_left_x=1143)
Here $0<a<\frac{2}{3}$. Hence,
$$\min _{\mathfrak{E}} s_{g}=\frac{24 \pi(a-2)\left(35 a^{3}-42 a^{2}+24 a-8\right)}{a\left(475 a^{4}-1140 a^{3}+1056 a^{2}-480 a+96\right)} .$$
It is easy to verify that this is positive when $0<a<\frac{2}{3}$. Hence $\min _{\mathfrak{E}} s_{g}>0$ on the entire Kähler cone $\mathcal{K}$.

Case 3G.
\begin{itemize}
\item[-] There are two fixed points $E_{1} \cap E_{1}^{\prime}, E_{2} \cap E_{2}^{\prime}$, with weights [-3, 1], [-3, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=\frac{1}{2}, c_{1}(Y)\left[\Sigma_{-a}\right]=-\frac{1}{6}$.
\item[-] Set $\omega\left(E_{3}\right)=1, \omega\left(E_{2}\right)=a$. Then
$$\begin{gathered}
\omega\left(E_{1}\right)=1-a, \omega\left(E_{1}^{\prime}\right)=3 a-1, \\
\omega\left(E_{2}^{\prime}\right)=2-3 a, \omega(F)=2 .
\end{gathered}$$
Moreover $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=1$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-41.jpg?height=584&width=724&top_left_y=1031&top_left_x=1145)
Here $\frac{1}{3}<a<\frac{2}{3}$. Hence,
$$\min _{\mathfrak{E}} s_{g}=-\frac{216 \pi\left(6 a^{4}-12 a^{3}+12 a^{2}-6 a+1\right)}{972 a^{6}-2916 a^{5}+3564 a^{4}-2268 a^{3}+774 a^{2}-126 a+7} .$$
It is easy to verify that this is positive when $\frac{1}{3}<a<\frac{2}{3}$. Hence $\min _{\mathfrak{E}} s_{g}>0$ on the entire Kähler cone.
For the following cases the picard number of $\widehat{M}$ is 1, hence only one Kähler class exists on the orbifold.

Case 3H.
\begin{itemize}
\item[-] There is one fixed point $E_{2} \cap E_{2}^{\prime}$ with weights [-2, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=\frac{1}{6}, c_{1}(Y)\left[\Sigma_{-a}\right]=-\frac{1}{3}$.
\item[-] Set $\omega\left(E_{2}\right)=1$. Then
$$\omega\left(E_{1}\right)=3, \omega\left(E_{2}^{\prime}\right)=4, \omega\left(E_{3}\right)=2, \omega(F)=6 .$$
Moreover, $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=4$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-41.jpg?height=606&width=730&top_left_y=1938&top_left_x=1143)
We have $\min _{\mathfrak{E}} s_{g}=\frac{24 \pi}{7}>0$.

Case 3J.
\begin{itemize}
\item[-] There is one fixed point $E_{2} \cap E_{2}^{\prime}$ with weights [-3, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=\frac{1}{6}, c_{1}(Y)\left[\Sigma_{-a}\right]=-\frac{1}{6}$.
\item[-] Set $\omega\left(E_{2}\right)=1$. Then
$$\omega\left(E_{1}\right)=3, \omega\left(E_{2}^{\prime}\right)=3, \omega\left(E_{3}\right)=2, \omega(F)=6 .$$
Moreover, $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=3$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-42.jpg?height=606&width=735&top_left_y=189&top_left_x=1139)

In this case we hace $-T_{s}+s_{0} T_{1}=0$. Therefore it can never support an extremal Kähler metric with extremal vector field proportional to $\mathfrak{E}$, by our discussion at the beginning of Section 7.2.

Case 3L.
\begin{itemize}
\item[-] There is one fixed point $E_{2} \cap E_{2}^{\prime}$ with weights [-4, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=\frac{1}{6}, c_{1}(Y)\left[\Sigma_{-a}\right]=-\frac{1}{12}$.
\item[-] Set $\omega\left(E_{2}\right)=1$. Then
$$\omega\left(E_{1}\right)=3, \omega\left(E_{2}^{\prime}\right)=2, \omega\left(E_{3}\right)=2, \omega(F)=6 .$$
Moreover, $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=2$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-42.jpg?height=608&width=735&top_left_y=909&top_left_x=1139)

We have $\min _{\mathfrak{E}} s_{g}=\frac{96 \pi}{7}>0$.

Case 3M.
\begin{itemize}
\item[-] There is one fixed point $E_{2} \cap E_{2}^{\prime}$ with weights [-5, 1].
\item[-] $c_{1}(Y)\left[\Sigma_{a}\right]=\frac{1}{6}, c_{1}(Y)\left[\Sigma_{-a}\right]=-\frac{1}{30}$.
\item[-] Set $\omega\left(E_{2}\right)=1$. Then
$$\omega\left(E_{1}\right)=3, \omega\left(E_{2}^{\prime}\right)=1, \omega\left(E_{3}\right)=2, \omega(F)=6 .$$
Moreover, $\omega\left(c_{ \pm}\right)=0$.
\item[-] $c_{1}[\omega]=1$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-42.jpg?height=606&width=735&top_left_y=1594&top_left_x=1139)

We have $\min _{\mathfrak{E}} s_{g}=\frac{600 \pi}{31}>0$.
Till now, we have already proved that,
Theorem 7.5. For the pairs $(\widehat{M}, \mathfrak{E})$ listed in Table 4, they can never support special Bach-flat Kähler metrics.
Combining Theorem 1.3, Proposition 5.2, and Proposition 6.11 with the results obtained in this section, we have completed the proof of Theorem 1.4.

It is worth noting that in higher dimensions, there also exist Hermitian non-Kähler Ricci-flat ALE manifolds. For instance, consider a Kronheimer's hyperkähler ALE 4-manifold $X$, where the space of hyperkähler complex structures
is parameterized by $S^{2}$. Take $\mathbb{C} \subset S^{2}$ and consider $\mathbb{C} \times X$. Define the complex structure $J$ on $\mathbb{C} \times X$ by
$$\left.J\right|_{X_{t}}=J_{t},$$
where here $X_{t}$ refers to $t \times X$, and $J_{t}$ refers to the hyperkähler complex structure on $X$ given by $t \in \mathbb{C} \subset S^{2}$. For any $p \in X$, we require that $\left.J\right|_{\mathbb{C} \times p}$ is the standard complex structure on $\mathbb{C}$. This defines an integrable complex structure on $\mathbb{C} \times X$, and the product metric on $\mathbb{C} \times X$ is clearly Hermitian non-Kähler Ricci-flat ALE. However, this example is trivial in the sense that there are complex structures on $\mathbb{C} \times X$, namely the product complex structures, such that the metric is Kähler. This example was pointed out to the author by Junsheng Zhang. It will be interesting to find more nontrivial Hermtian non-Kähler Ricci-flat ALE manifolds in the higher dimensional case.

Finally we would like to remark that given any $\Gamma \subset U(2)$, we could repeat the classification for the pairs $(\widetilde{M}, \mathfrak{E})$ and the calculation for $\min _{\mathfrak{E}} s_{g}$, to derive some non-existence results for Hermitian non-Kähler ALE gravitational instantons with structure group $\Gamma$. The difficulty for the general $U(2)$ case is, if we do not fix $\Gamma \subset U(2)$, there could be infinite number of candidates $(\widetilde{M}, \mathfrak{E})$.

\section*{Appendix A. Proof of Theorem 4.6}

In the appendix we give a proof of Theorem 4.6. We adopt some notations from toric geometry. For a cyclic group $\Gamma=L(q, p)$ and the fan $F_{L(q, p)}$ of its minimal resolution as shown in Figure 1, we set each $v_{i}=\left(v_{i, U}, v_{i, V}\right)$ and define $v_{i}^{\perp}=\left(-v_{i, V}, v_{i, U}\right)$. Denote $\sigma_{i}$ by the cone $\sigma\left(v_{i+1}, v_{i}\right)$ spanned by $v_{i+1}, v_{i}$, so that the fan $F_{L(q, p)}$ is the union of the cones $\sigma_{i}$. For each cone $\sigma_{i}=\sigma\left(v_{i+1}, v_{i}\right)$ in the fan, there is the dual cone $\sigma_{i}^{\vee}=\sigma\left(-v_{i+1}^{\perp}, v_{i}^{\perp}\right)$. Denote $\sigma_{\Gamma}$ by the cone $\sigma((0,1),(p,-q))$, hence the fan of $\mathbb{C}^{2} / \Gamma$ consists of a single cone $\sigma_{\Gamma}$. For a cone $\sigma$, by $S_{\sigma}$ we mean the $\mathbb{C}$-algebra generated by $U^{a} V^{b}$ with all integral $(a, b) \in \sigma$. From standard results of toric geometry we have:
\begin{itemize}
\item[-] As a variety $\mathbb{C}^{2} / \Gamma=\operatorname{Spec} \mathbb{C}[X, Y]^{\Gamma}=\operatorname{Spec} S_{\sigma_{\Gamma}^{\vee}}$. Here, $\mathbb{C}[X, Y]^{\Gamma}$ refers to the polynomials that are $\Gamma$-invariant. The $\mathbb{C}$-algebra $S_{\sigma_{\Gamma}^{\vee}}$ is related to $\mathbb{C}[X, Y]^{\Gamma}$ via the isomorphism $U=X^{p}$ and $V=Y / X^{q}$.
\item[-] The minimal resolution $\widetilde{\mathbb{C}^{2} / \Gamma}$ is the affine varieties $\operatorname{Spec} S_{\sigma_{i}^{\vee}}$ glued together along $\operatorname{Spec} S_{\sigma_{i}^{\vee} \cup \sigma_{i-1}^{\vee}}$. Notice that $S_{\sigma_{i}^{\vee}} \subset S_{\sigma_{i}^{\vee} \cup \sigma_{i-1}^{\vee}}$ is a sub-C-algebra.
\end{itemize}

Theorem A.1. Consider the $\mathbb{C}^{*}$-action on $\mathbb{C}^{2} / L(q, p)$ defined by $t \curvearrowright(x, y)=\left(t^{\theta} x, t^{\tau} y\right)$ with $\theta \geq \tau \geq 0$ and its minimal resolution $\widetilde{\mathbb{C}^{2} / \Gamma}$ given by Theorem 4.5. Given vertices $v_{0}, \ldots, v_{k}$ as in Theorem 4.5, write $v_{i}=\left(v_{i, U}, v_{i, V}\right)$ and for $i=0, \ldots, k+1$ define
$$w_{i}=\theta\left(p v_{i, V}+q v_{i, U}\right)-\tau v_{i, U} .$$
Then the weights of the lifted action are:
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-43.jpg?height=309&width=1366&top_left_y=1620&top_left_x=378)
Notice that there is the inductive relation $w_{i+1}=e_{i} w_{i}-w_{i-1}$, and we have $w_{0}=\theta p, w_{1}=\theta q-\tau, w_{k}=\theta-\tau v_{k, U}$, and $w_{k+1}=-\tau p$.
Proof. As $\mathbb{C}^{2} / L(q, p)=\operatorname{Spec} \mathbb{C}[X, Y]^{L(q, p)}=\operatorname{Spec} S_{\sigma_{\Gamma}^{\vee}}$, the orbifold point in $\mathbb{C}^{2} / L(q, p)$ is defined by $U^{a} V^{b}=0$ in $S_{\sigma_{\Gamma}^{\vee}}$, for all $U^{a} V^{b} \in S_{\sigma_{\Gamma}^{\vee}}$. To find the exceptional set in the minimal resolution, it suffices to consider the preimage of the orbifold point.

Lemma A.2. In the affine piece $\operatorname{Spec} S_{\sigma_{i+1}^{\vee}}, E_{i}$ is parametrized by $U^{v_{i, V}} V^{-v_{i, U}} \in S_{\sigma_{i+1}^{\vee}}$, and $E_{i+1}$ is parametrized by $U^{-v_{i+1, V}} V^{v_{i+1, U}} \in S_{\sigma_{i+1}^{\vee}}$.
Proof. The dual cone $\sigma_{i+1}^{\vee}$ is spanned by $-v_{i}^{\perp}$ and $v_{i+1}^{\perp}$. Note that $\sigma\left(-v_{0}^{\perp}, v_{k+1}^{\perp}\right)$ is exactly $\sigma_{\Gamma}^{\vee}$.
The algebra $S_{\sigma_{i+1}^{\vee}}$ is the $\mathbb{C}$-algebra finitely generated by $U^{a} V^{b}$ with $(a, b) \in \sigma_{i+1}^{\vee}$. The dual cone $\sigma_{i+1}^{\vee}=\sigma\left(-v_{i}^{\perp}, v_{i+1}^{\perp}\right)$ can be decomposed as the union of four cones:
\begin{itemize}
\item[-] $\sigma\left(-v_{i}^{\perp},-v_{1}^{\perp}\right)$ spanned by $-v_{i}^{\perp},-v_{1}^{\perp}$;
\item[-] $\sigma\left(-v_{1}^{\perp},-v_{0}^{\perp}\right)$ spanned by $-v_{1}^{\perp},-v_{0}^{\perp}$;
\end{itemize}
\begin{itemize}
\item[-] $\sigma_{\Gamma}^{\vee}=\sigma\left(-v_{0}^{\perp}, v_{k+1}^{\perp}\right)$ spanned by $-v_{0}^{\perp}, v_{k+1}^{\perp}$;
\item[-] $\sigma\left(v_{k+1}^{\perp}, v_{i+1}^{\perp}\right)$ spanned by $v_{k+1}^{\perp}, v_{i+1}^{\perp}$.
\end{itemize}
![](https://cdn.mathpix.com/cropped/9abe049f-ab44-4518-b4d2-740341233cf9-44.jpg?height=758&width=846&top_left_y=329&top_left_x=636)
Write $S_{\sigma\left(-v_{i}^{\perp},-v_{1}^{\perp}\right) \cup \sigma\left(-v_{1}^{\perp},-v_{0}^{\perp}\right) \cup \sigma_{\Gamma}^{\vee} \cup \sigma\left(v_{k+1}^{\perp}, v_{i+1}^{\perp}\right)}$ as the $\mathbb{C}$-algebra generated by $S_{\sigma\left(-v_{i}^{\perp},-v_{1}^{\perp}\right)}, S_{\sigma\left(-v_{1}^{\perp},-v_{0}^{\perp}\right)}, S_{\sigma_{\Gamma}^{\vee}}$, and $S_{\sigma\left(v_{k+1}^{\perp}, v_{i+1}^{\perp}\right)}$, then
$$S_{\sigma_{i+1}^{\vee}}=S_{\sigma\left(-v_{i}^{\perp},-v_{1}^{\perp}\right) \cup \sigma\left(-v_{1}^{\perp},-v_{0}^{\perp}\right) \cup \sigma_{\Gamma}^{\vee} \cup \sigma\left(v_{k+1}^{\perp}, v_{i+1}^{\perp}\right)} .$$
Henceforth, to determine the exceptional set in $S p e c S_{\sigma_{i+1}^{\vee}}$, it suffices to write down a set of generators of the four $\mathbb{C}$-algebras and determine the equations that define the exceptional set. We have:
\begin{itemize}
\item[-] For $S_{\sigma_{\Gamma}^{\vee}}$ :
\begin{itemize}
\item[-] $U^{-v_{j, V}} V^{v_{j, U}}$ is a set of generators of $S_{\sigma_{\Gamma}^{\vee}}$ with $j=0, \ldots, k+1$.
\item[-] All generators of $S_{\sigma_{\Gamma}^{\vee}}$ vanish in the preimage of the orbifold point.
\end{itemize}
\item[-] For $S_{\sigma\left(-v_{1}^{\perp},-v_{0}^{\perp}\right)}$ :
\begin{itemize}
\item[-] $S_{\sigma\left(-v_{1}^{\perp},-v_{0}^{\perp}\right)}$ is generated by $U, V^{-1}$.
\item[-] In the preimage of the orbifold point, $U=0$. We will see that $V^{-1}=0$ also holds in the preimage of the orbifold point.
\end{itemize}
\item[-] For $S_{\sigma\left(-v_{i}^{\perp},-v_{1}^{\perp}\right)}$ :
\begin{itemize}
\item[-] Generators of $S_{\sigma\left(-v_{i}^{\perp},-v_{1}^{\perp}\right)}$ can be taken as
$$P_{j}=U^{v_{j, V}} V^{-v_{j, U}}, j=1, \ldots, i .$$
They form a set of generators for $S_{\sigma^{\vee}\left(-v_{i}^{\perp},-v_{1}^{\perp}\right)}$ because $\operatorname{det}\left(-v_{j}^{\perp},-v_{j-1}^{\perp}\right)=1$.
\item[-] In the preimage of the orbifold point, for any $1 \leq j<i$, the above generators in $S_{\sigma_{i+1}^{\vee}}$ have the relations
$$P_{j}^{-v_{i, V}}=P_{i}^{-v_{j, V}}\left(V^{-1}\right)^{-v_{j, U} v_{i, V}+v_{i, U} v_{j, V}},$$
where $-v_{j, U} v_{i, V}+v_{i, U} v_{j, V}=\operatorname{det}\left(v_{i}, v_{j}\right)>0$ as $i>j$. We also have the relation
$$\left(V^{-1}\right)^{v_{i, U}}=P_{i} U^{-v_{i, V}}$$
in $S_{\sigma_{i+1}^{\vee}}$ (note $-v_{i, V}>0$ ). Thus, in the preimage of the orbifold point in $S$ pec $S_{\sigma_{i+1}^{\vee}}$, as $U=0$, we must have $V^{-1}=0$. So the equations $P_{j}=0$ hold for $1 \leq j<i$.
\end{itemize}
\item[-] For $S_{\sigma\left(v_{k+1}^{\perp}, v_{i+1}^{\perp}\right)}^{\perp}$ :
\begin{itemize}
\item[-] Generators of $S_{\sigma\left(v_{k+1}^{\perp}, v_{i+1}^{\perp}\right)}^{\perp}$ can be taken as
$$Q_{j}=U^{-v_{j, V}} V^{v_{j, U}}, j=i+1, \ldots, k+1,$$
for the same reason as above.
\end{itemize}
\end{itemize}
\begin{itemize}
\begin{itemize}
\item[-] The relations
$$Q_{j}^{v_{i+1, U}}=Q_{i+1}^{v_{j, U}} U^{v_{i+1, V} v_{j, U}-v_{i+1, U} v_{j, V}}$$
hold for $i+1<j \leq k+1$ where $v_{i+1, V} v_{j, U}-v_{i+1, U} v_{j, V}=-\operatorname{det}\left(v_{i+1}, v_{j}\right)>0$. Thus, in the preimage of the orbifold point in $\operatorname{Spec} S_{\sigma_{i+1}^{\vee}}$, equations $Q_{j}=0$ hold for $i+1<j \leq k+1$.
\item[-] Moreover, since $v_{i, V}-v_{i+1, V}, v_{i+1, U}-v_{i, U}>0$ and $0<\left(v_{i+1, U}-v_{i, U}\right) /\left(v_{i, V}-v_{i+1, V}\right)<q / p$,
$$P_{i} Q_{i+1}=U^{v_{i, V}-v_{i+1, V}} V^{v_{i+1, U}-v_{i, U}} \in S_{\sigma_{\Gamma}^{\vee}} .$$
This shows in the preimage of the orbifold point, the equation $P_{i} Q_{i+1}=0$ holds.
\end{itemize}
\end{itemize}

Therefore, the preimage of the orbifold point is parametrized by $P_{i}$ and $Q_{i+1}$ in the affine piece $\operatorname{Spec} S_{\sigma_{i+1}^{\vee}}$, which exactly correspond to the exceptional curves $E_{i}$ and $E_{i+1} . P_{i}$ parametrizes $E_{i}$ and $Q_{i+1}$ parametrizes $E_{i+1} . E_{i}$ and $E_{i+1}$ intersects in this affine piece at the point where $P_{i}=Q_{i+1}=0$. The equation $P_{i} Q_{i+1}=0$ holds in the preimage of the orbifold point in the affine piece $\operatorname{Spec} S_{\sigma_{i+1}^{\vee}}$, which means the preimage of the orbifold point in $\operatorname{Spec} S_{\sigma_{i+1}^{\vee}}$ is exactly $\operatorname{Spec} S_{\sigma_{i+1}^{\vee}} \cap\left(E_{i} \cup E_{i+1}\right)$. \(\square\)

Recall that $U=X^{p}, V=Y / X^{q}$, and the $\mathbb{C}^{*}$-action on $X, Y$ is $t \curvearrowright X, Y=t^{\theta} X, t^{\tau} Y$. The prameters $P_{i}, Q_{i+1}$ are given by
$$\begin{gathered}
P_{i}=U^{v_{i, V}} V^{-v_{i, U}}=X^{p v_{i, V}}\left(Y / X^{q}\right)^{-v_{i, U}}=X^{p v_{i, V}+q v_{i, U}} Y^{-v_{i, U}} . \\
Q_{i+1}=U^{-v_{i+1, V}} V^{v_{i+1, U}}=X^{-p v_{i+1, V}}\left(Y / X^{q}\right)^{v_{i+1, U}}=X^{-p v_{i+1, V}-q v_{i+1, U}} Y^{v_{i+1, U}} .
\end{gathered}$$
This implies the $\mathbb{C}^{*}$-action on the exceptional curve $E_{i}$ parametrized by $P_{i}$ is given by
$$t \curvearrowright P_{i}=t^{\theta\left(p v_{i, V}+q v_{i, U}\right)-\tau v_{i, U}} P_{i} ;$$
and the $\mathbb{C}^{*}$-action on the exceptional curve $E_{i+1}$ parametrized by $Q_{i+1}$ is given by
$$t \curvearrowright Q_{i+1}=t^{-\theta\left(p v_{i+1, V}+q v_{i+1, U}\right)+\tau v_{i+1, U}} Q_{i+1} .$$
Note that here
$$\theta\left(p v_{i, V}+q v_{i, U}\right)-\tau v_{i, U}=\theta(q, p) \cdot\left(v_{i, U}, v_{i, V}\right)-\tau v_{i, U}=w_{i} .$$
The way that $\mathbb{C}^{*}$-acts on $E_{i}, E_{i+1}(36)(37)$ show that the intersection point $E_{i} \cap E_{i+1}$ should have weights $\left[w_{i},-w_{i+1}\right]$.
The ray given by $v_{0}$ in the fan $F_{M}$ corresponds to the proper transform of $y=0$, which is parametrized by $U=X^{p}$. The action on $y=0$ is given by $t \curvearrowright U=t^{p \theta} U$, which implies the weights at the intersection of $y=0$ and $E_{1}$ are $\left[w_{0},-w_{1}\right]$. Similarly, the ray given by $v_{k+1}=(p,-q)$ corresponds to the proper transform of $x=0$, which is parametrized by $U^{q} V^{p}=Y^{p}$. The action on $x=0$ is given by $t \curvearrowright U^{q} V^{p}=t^{\tau} U^{q} V^{p}$, which implies the weights at the intersection of $x=0$ and $E_{k}$ are $\left[w_{k},-w_{k+1}\right]$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] S. Bando, A. Kasue, and H. Nakajima. On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth. Inventiones mathematicae, 97(2):313-349, 1989.
\item[] [2] O. Biquard and H. Hein. The renormalized Volume of a 4-dimensional Ricci-flat ALE Space. arXiv:1901.03647, 2019.
\item[] [3] X. Chen, C. LeBrun, and B. Weber. On conformally Kähler, Einstein manifolds. Journal of the American Mathematical Society, 21(4):1137-1168, 2008.
\item[] [4] I. Şuvaina. ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities. Annals of Global Analysis and Geometry, 41(1):109-123, 2012.
\item[] [5] A. Derdziński. Self-dual Kähler manifolds and Einstein manifolds of dimension four. Compositio Mathematica, 49(3):405-433, 1983.
\item[] [6] S. Donaldson and S. Sun. Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry. Acta Mathematica, 213(1):63-106, 2014.
\item[] [7] T. Eguchi and A. Hanson. Self-dual solutions to Euclidean gravity. Annals of Physics, 120(1):82-106, 1979.
\item[] [8] W. Fulton. Introduction to toric varieties. Princeton University Press, Princeton, 1993.
\item[] [9] A. Futaki and T. Mabuchi. Bilinear forms and extremal Kähler vector fields associated with Kähler classes. Mathematische Annalen, 301(1):199-210, 1995.
\item[] [10] P. Kronheimer. A Torelli-type theorem for gravitational instantons. Journal of Differential Geometry, 29(3):685-697, 1989.
\item[] [11] P. Kronheimer. The construction of ALE spaces as hyper-Kähler quotients. Journal of Differential Geometry, 29(3):665-683, 1989.
\item[] [12] C. LeBrun. Einstein Metrics on Complex Surfaces. In Geometry and Physics, pages 167-176. CRC Press, 1995.
\item[] [13] C. LeBrun. On Einstein, Hermitian 4-manifolds. Journal of Differential Geometry, 90(2):277-302, 2012.
\item[] [14] C. LeBrun. Bach-Flat Kähler Surfaces. The Journal of Geometric Analysis, 30(3):2491-2514, 2020.
\item[] [15] C. LeBrun and S. Simanca. Extremal Kähler metrics and complex deformation theory. Geometric and Functional Analysis, 4(3):298-336, 1994.
\item[] [16] M. Lock and J. Viaclovsky. Quotient singularities, eta invariants, and self-dual metrics. Geometry \& Topology, 20(3):1773-1806, 2016.
\item[] [17] M. Lock and J. Viaclovsky. A smörgåsbord of scalar-flat Kähler ALE surfaces. Journal für die reine und angewandte Mathematik (Crelles fournal), 2019(746):171-208, 2019.
\end{itemize}
\begin{itemize}
\item[] [18] H. Nakajima. Self-Duality of ALE Ricci-Flat 4-Manifolds and Positive Mass Theorem. In Recent Topics in Differential and Analytic Geometry, pages 385-396. 1990.
\item[] [19] D. Page. A compact rotating gravitational instanton. Physics Letters B, 79(3):235-238, 1978.
\item[] [20] S. Tanno. 4-dimensional conformally flat Kähler manifolds. Tóhoku Mathematical Journal, 24(3):501-504, 1972.
\item[] [21] E. Wright. Quotients of Gravitational Instantons. Annals of Global Analysis and Geometry, 41(1):91-108, 2012.
\end{itemize}

Department of Mathematics, University of California, Berkeley, CA 94720, USA.
E-mail address: mingyang_li@berkeley.edu

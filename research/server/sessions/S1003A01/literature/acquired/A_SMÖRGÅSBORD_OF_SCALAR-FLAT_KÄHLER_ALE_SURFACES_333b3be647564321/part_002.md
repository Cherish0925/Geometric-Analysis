---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: A SMÖRGÅSBORD OF SCALAR-FLAT KÄHLER ALE SURFACES]

Remark 5.3. Notice that only weighted projective spaces with one or two singularities, i.e. those of the form $\mathbb{C P}_{(1, q, p)}^{2}$ where $1 \leq q<p$ are relatively prime integers, are made use of in this construction. This is so because taking the Green's function metrics of a weighted projective space with three singular points, i.e. one of the form $\mathbb{C P}_{(r, q, p)}^{2}$ where $1<r<q<p$ are relatively prime integers, and resolving by attaching the appropriate scalar-flat Kähler ALE spaces to the remaining singularities tends to yield a scalar-flat Kähler ALE metric on a blow-up (in the complex analytic sense) of the minimal resolution.
5.3. Construction of the metrics for non-cyclic groups. For each non-cyclic finite subgroup $\Gamma \subset \mathrm{U}(2)$ containing no complex reflections, consider the scalar-flat Kähler ALE orbifold with group at infinity $\Gamma$ obtained in Theorem 4.1. All singularities of this space lie on the $\mathbb{C P}^{1}$ at the origin and are of cyclic type with the orbifold groups $L\left(\alpha_{i}, \beta_{i}\right)$ for $i=1,2,3$, recall Remark 4.2. To resolve these singularities, we use Theorem 5.1 to attach a Calderbank-Singer space with group at infinity $L\left(\alpha_{i}, \beta_{i}\right)$ to the singularity with the corresponding orbifold group. Furthermore, since both the ALE orbifold, obtained as a quotient of a LeBrun negative mass metric, and all of the Calderbank-Singer spaces admit holomorphic isometric circle actions corresponding to rotations of the Hopf fiber, we can impose an $S^{1}$ symmetry in the gluing argument, that is, we may perform the gluing $S^{1}$-equivariantly, to obtain a scalar-flat Kähler ALE space with group at infinity $\Gamma$ which admits a holomorphic isometric circle action.

It is straightforward to see that the conditions in Definition 1.1 are satisfied, so we have obtained scalar-flat Kähler ALE metrics on the minimal resolution of $\mathbb{C}^{2} / \Gamma$. This completes the proof of Theorem 1.3

Remark 5.4. It would perhaps be possible to use gluing results for constant scalar curvature Kähler metrics, instead of the Hermitian anti-self-dual gluing theorem. We used the latter here since it is easier to generalize the result of Rollin-Singer to the case
that the base orbifold is ALE. However, gluing results for extremal Kähler metrics will indeed be used in Section 7.
5.4. Topology of the minimal resolutions. The intersection matrix of the exceptional curve in the minimal resolution is described in Figure 5.1.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a5edf7e0-2a3e-42c8-b335-be18e7a456e8-24.jpg?height=681&width=1272&top_left_y=574&top_left_x=412}
\captionsetup{labelformat=empty}
\caption{Figure 5.1. The exceptional divisor of the minimal resolution.}
\end{figure}

In Figure 5.1, each string of $e_{i}^{j}$ corresponds to the intersection matrix of the respective Calderbank-Singer space attached to the central rational curve at a particular singularity. Clearly, the signature of the minimal resolution of $\mathbb{C}^{2} / \Gamma$ is
$$\tau=-b_{2}^{-}=-1-\sum_{i=1}^{3} k_{L\left(\alpha_{i}, \beta_{i}\right)} .$$
The orbifold points which arise on the $\mathbb{C P}^{1}$ at the origin in our work correspond, in fact, to those in Brieskorn's resolution, and our procedure of resolving singularities by attaching the appropriate Calderbank-Singer spaces is a metric version of Brieskorn's complex analytic resolution of those singularities by a Hirzebruch-Jung string.

Finally, the self-intersection number of the central rational curve is given by
$$-b_{\Gamma}=-\left(\frac{\alpha_{1}}{\beta_{1}}+\frac{\alpha_{2}}{\beta_{2}}+\frac{\alpha_{3}}{\beta_{3}}+\frac{2 m}{h}\right),$$
where $h$ is the order of the image of the group in $\operatorname{PGL}(2, \mathbb{C})$ and $m$ corresponds to that of the group, see [Bri68]. When $\Gamma$ is the image under $\phi$ of the product of $L(1,2 m)$ with a binary polyhedral group, its image in $\operatorname{PGL}(2, \mathbb{C})$ is just the corresponding polyhedral group. Similarly, the images of $\mathfrak{I}_{m, n}^{2}$ and $\mathfrak{I}_{m}^{3}$ in $\operatorname{PGL}(2, \mathbb{C})$ are the dihedral and tetrahedral groups respectively. Finally, we note that
$$b_{\Gamma}=2+\frac{4 m}{|\Gamma|}\left[m-\left(m \bmod \frac{|\Gamma|}{4 m}\right)\right] .$$
Observe, from this, that $-b_{\Gamma}<-1$.

\section*{6. Scalar-flat Kähler deformations}

We begin by finding the dimension of the space of infinitesimal scalar-flat Kähler deformations of the ALE orbifolds given in Theorem 4.1. An essential ingredient here is Honda's work in understanding the deformation theory of compactifications of the LeBrun negative mass metrics [Hon13, Hon14]. The space $\left(\mathcal{O}(-2), g_{L B}\right)$ is the Eguchi-Hanson metric, for which it is well known that there are no such deformations. This is the $m=1$ case, and the groups corresponding to this are exactly the binary polyhedral groups. Therefore it is only necessary to consider $m>1$. In the following proposition we not only find the dimension of the space of such deformations, but in fact show that it can be given very simply in terms of the respective $b_{\Gamma}$, which recall is negative the self-intersection number of the central rational curve.

Proposition 6.1. Let $\Gamma \subset \mathrm{U}(2)$ be a non-cyclic finite subgroup containing no complex reflections with $m>1$. Then, the dimension of the space of infinitesimal scalar-flat Kähler deformations of the quotient $\left(\mathcal{O}(-2 m), g_{L B}\right) / \Gamma^{\prime}$, which preserve all orbifold singularities, is given by
$$\operatorname{dim}\left(H_{\Gamma^{\prime}}^{s f k}\right)=2 b_{\Gamma}-2=2+\frac{8 m}{|\Gamma|}\left[m-\left(m \bmod \frac{|\Gamma|}{4 m}\right)\right] .$$
Proof. Finding the dimension of scalar-flat Kähler deformation of $\left(\mathcal{O}(-2 m), g_{L B}\right) / \Gamma^{\prime}$ is equivalent to finding the dimension of the space of scalar-flat Kähler deformations of $\left(\mathcal{O}(-2 m), g_{L B}\right)$ that are invariant under the action of $\Gamma^{\prime}$. In general, for a representation $\rho$ of a finite group $\Gamma^{\prime}$, the dimension of the space of invariant elements is given by
$$\frac{1}{\left|\Gamma^{\prime}\right|} \sum_{\gamma \in \Gamma^{\prime}} \chi_{\rho}(\gamma),$$
where $\chi_{\rho}(\gamma)$ denotes the character of $\gamma \in \Gamma^{\prime}$. For $\gamma=\left[1, e^{i \theta}\right] \neq \pm 1 \in \operatorname{SU}(2)$, there is the following well-known character identity on $S^{2 k}\left(\mathbb{C}^{2}\right)$ as a representation of $\operatorname{SU}(2)$
$$\chi_{S^{2 k}\left(\mathbb{C}^{2}\right)}(\gamma)=\sum_{p=0}^{2 k}\left(e^{i \theta}\right)^{2 k-2 p}=\frac{\sin ((2 k+1) \theta)}{\sin (\theta)}=\sin (2 k \theta) \cot (\theta)+\cos (2 k \theta) .$$
Notice that $\chi_{S^{2 k}}\left(\mathbb{C}^{2}\right)(\gamma=[1, i])=\cos (\pi k)$, since $\sin (\pi k) \cot (\pi / 2)=0$. It will be useful here to introduce the sawtooth function which, for any $x \in \mathbb{R}$, is defined as
$$((x))= \begin{cases}x-\lfloor x\rfloor-\frac{1}{2} & \text { when } x \notin \mathbb{Z} \\ 0 & \text { when } x \in \mathbb{Z},\end{cases}$$
where $\lfloor x\rfloor$ denotes the greatest integer less than $x$. When $\theta=\pi / n$, there is the following useful identity due to Eisenstein, see Apo90.
$$\sum_{j=1}^{n-1} \sin \left(\frac{2 \pi k}{n} j\right) \cot \left(\frac{\pi}{n} j\right)=-2 n\left(\left(\frac{k}{n}\right)\right)$$

For $m>1$, Honda showed that the complexification of the space of infinitesimal scalar-flat Kähler deformations of $\left(\mathcal{O}(-2 m), g_{L B}\right)$ is equivalent to
$$\rho \oplus \bar{\rho} \quad \text { where } \quad \rho=S^{2 m-2}\left(\mathbb{C}^{2}\right) \otimes \operatorname{det},$$
as a representation space of U(2) , see [Hon13]. Using this along with (6.1), we will compute $\operatorname{dim}\left(H_{\Gamma^{\prime}}^{s f k}\right)$ for all appropriate $\Gamma^{\prime}$.

Write the maximal torus in $\mathrm{U}(2)$ as $\operatorname{diag}\left\{z_{1}=e^{i \theta_{1}}, z_{2}=e^{i \theta_{2}}\right\}$, and observe that
$$\chi_{\rho}\left(z_{1}, z_{2}\right)=\left(z_{1} z_{2}\right) \sum_{p=0}^{2 m-2} z_{1}^{2 m-2-p} z_{2}^{p}$$
where $\chi_{\rho}\left(z_{1}, z_{2}\right)$ denotes the character of any $\gamma \in \Gamma^{\prime}$ with eigenvalues $\left\{z_{1}, z_{2}\right\}$. Note that $\operatorname{dim}\left(H^{s f k}\right)=2 \chi_{\rho}(1,1)=2 \chi_{\rho}(-1,-1)=4 m-2$.

Consider when $\Gamma$ is the image under $\phi$ of the product of $L(1,2 m)$ and a binary polyhedral group. (Although the proofs for $\Im_{m, n}^{2}$ and $\Im_{m}^{3}$ will follow similarly, there is a certain delicate difference.) Here, since the $\Gamma^{\prime} \subset \mathrm{SU}(2)$ are the respective binary polyhedral groups so any $\gamma \in \Gamma^{\prime}$ has eigenvalues $\left\{z=e^{i \theta_{\gamma}}, z^{-1}=e^{-i \theta_{\gamma}}\right\}$. Thus, from (6.2), the character for $\gamma \neq \pm 1$ reduces to
$$\chi_{\rho}(\gamma)=\sum_{p=0}^{2 m-2}\left(e^{i \theta_{\gamma}}\right)^{2 m-2-2 p}=\sin \left((2 m-2) \theta_{\gamma}\right) \cot \left(\theta_{\gamma}\right)+\cos \left((2 m-2) \theta_{\gamma}\right),$$
and therefore
$$\operatorname{dim}\left(H_{\Gamma^{\prime}}^{s f k}\right)=\frac{2}{\left|\Gamma^{\prime}\right|}\left[2 \cdot(2 m-1)+\sum_{\gamma \neq \pm I d \in \Gamma^{\prime}} \sin \left((2 m-2) \theta_{\gamma}\right) \cot \left(\theta_{\gamma}\right)+\cos \left((2 m-2) \theta_{\gamma}\right)\right] .$$
We will now find $\operatorname{dim}\left(H_{\Gamma^{\prime}}^{s f k}\right)$ in terms of certain greatest integer functions for each binary polyhedral group separately. The conjugacy classes of the binary polyhedral groups are well known, see [Ste08], and from the trace of a representative element one can determine the eigenvalues of the elements in its class. We use this to decompose the binary polyhedral groups into sets of elements having the same eigenvalues. Then, we further group the elements in such a way as to be able to repeatedly use (6.4) to compute $\operatorname{dim}\left(H_{\Gamma^{\prime}}^{s f k}\right)$ in terms of sawtooth functions, which we examine with respect to the possible congruencies of $m$ and in turn write in terms of greatest integer functions.
$\boldsymbol{D}_{4 n}^{*}$ : The binary dihedral group is composed of two disjoint sets of elements; the elements of the cyclic group $L(-1,2 n)$, and the set of elements
$$S=\left\{\left[1, e^{\pi i k / n} * \hat{j}\right]\right\}_{1 \leq k \leq 2 n} .$$
Since each element of $S$ has eigenvalues $\{i,-i\}$, and because $((x / 2))=0$ for all $x \in \mathbb{Z}$, observe that it does not contribute to the sum in (6.8). Decomposing the sum over
these sets, we find that
$$\begin{aligned}
\operatorname{dim}\left(H_{D_{4 n}^{*}}^{s f k}\right)= & \frac{1}{n}\left[(2 m-1)-2 n\left(\left(\frac{m-1}{n}\right)\right)\right. \\
& \left.+n \cos (\pi(m-1))+\sum_{j=1}^{n-1} \cos \left(\frac{2 \pi}{n}(m-1) j\right)\right] \\
= & \begin{cases}2\left\lfloor\frac{m-1}{n}\right\rfloor+2 & m \not \equiv 1 \bmod n \\
2\left(\frac{m-1}{n}\right)+2 & m \equiv 1 \bmod n .\end{cases}
\end{aligned}$$
$\boldsymbol{T}^{*}$ : The elements of the binary tetrahedral group are separated into sets according to their eigenvalues as in Table 6.1. Group together the elements with eigenvalues

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 6.1.}
\begin{tabular}[t]{|l|l|}
\hline $\left\{z_{1}, z_{2}\right\}$ & $\#\left\{\gamma \in T^{*}: \operatorname{diag}(\gamma)=\left\{z_{1}, z_{2}\right\}\right\}$ \\
\hline \{1, 1\} & 1 \\
\hline \{-1, -1\} & 1 \\
\hline $\{i,-i\}$ & 6 \\
\hline $\left\{e^{\pi i / 3}, e^{-\pi i / 3}\right\}$ & 8 \\
\hline $\left\{e^{2 \pi i / 3}, e^{-2 \pi i / 3}\right\}$ & 8 \\
\hline
\end{tabular}
\end{table}
$\left\{e^{\pi i \ell / 3}, e^{-\pi i \ell / 3}\right\}$, for $\ell=1,2$, since these constitute the elements of $\left.\left(L(-1,6) / \mathbb{Z}_{2}\right) \backslash I d\right)$, and ignore the terms having eigenvalues $\{i,-i\}$ since they do not contribute to the sum in (6.8). Decomposing the sum over these sets, we find that
$$\begin{aligned}
\operatorname{dim}\left(H_{T^{*}}^{s f k}\right)= & \frac{1}{6}\left[(2 m-1)-24\left(\left(\frac{m-1}{3}\right)\right)\right. \\
& \left.+3 \cos (\pi(m-1))+4 \sum_{j=1}^{2} \cos \left(\frac{2 \pi}{3}(m-1) j\right)\right] \\
= & \begin{cases}4\left\lfloor\frac{m-1}{3}\right\rfloor-m+3 & m \equiv 5 \bmod 6 \\
\frac{m-1}{3}+2 & m \equiv 1 \bmod 6 .\end{cases}
\end{aligned}$$
$\boldsymbol{O}^{*}$ : The elements of the binary octahedral group are separated into sets according to their eigenvalues as in Table 6.2. Group together the elements with eigenvalues $\left\{e^{\pi i \ell / 3}, e^{-\pi i \ell / 3}\right\}$, for $\ell=1,2$, as before. Also, group together the elements with eigenvalues $\left\{e^{\pi i \ell / 4}, e^{-\pi i \ell / 4}\right\}$, for $\ell=1,2,3$, since these constitute $\left.\left(L(-1,8) / \mathbb{Z}_{2}\right) \backslash I d\right)$. Since, the $\{i,-i\}$ elements do not contribute to the sum in (6.8), it does not matter that the order of that set differs from the orders of the other sets in this grouping.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 6.2.}
\begin{tabular}[t]{|l|l|}
\hline $\left\{z_{1}, z_{2}\right\}$ & $\#\left\{\gamma \in O^{*}: \operatorname{diag}(\gamma)=\left\{z_{1}, z_{2}\right\}\right\}$ \\
\hline \{1, 1\} & 1 \\
\hline \{-1, -1\} & 1 \\
\hline $\{i,-i\}$ & 18 \\
\hline $\left\{e^{\pi i / 3}, e^{-\pi i / 3}\right\}$ & 8 \\
\hline $\left\{e^{2 \pi i / 3}, e^{-2 \pi i / 3}\right\}$ & 8 \\
\hline $\left\{e^{\pi i / 4}, e^{-\pi i / 4}\right\}$ & 6 \\
\hline $\left\{e^{3 \pi i / 4}, e^{-3 \pi i / 4}\right\}$ & 6 \\
\hline
\end{tabular}
\end{table}
Decomposing the sum over these sets, we find that
$$\begin{aligned}
\operatorname{dim}\left(H_{O^{*}}^{s f k}\right)= & \frac{1}{12}\left[(2 m-1)-24\left(\left(\frac{m-1}{3}\right)\right)-24\left(\left(\frac{m-1}{4}\right)\right)+6 \cos (\pi(m-1))\right. \\
& \left.\quad+4 \sum_{j=1}^{2} \cos \left(\frac{2 \pi}{3}(m-1) j\right)+3 \sum_{j=1}^{3} \cos \left(\frac{2 \pi}{4}(m-1) j\right)\right] \\
= & \begin{cases}2\left\lfloor\frac{m-1}{3}\right\rfloor+2\left\lfloor\frac{m-1}{4}\right\rfloor-m+3 & m \equiv 11 \bmod 12 \\
2\left\lfloor\frac{m-1}{4}\right\rfloor+\frac{1-m}{3}+2 & m \equiv 7 \bmod 12 \\
2\left\lfloor\frac{m-1}{3}\right\rfloor+\frac{1-m}{2}+2 & m \equiv 5 \bmod 12 \\
\frac{m-1}{6}+2 & m \equiv 1 \bmod 12 .\end{cases}
\end{aligned}$$
$\boldsymbol{I}^{*}$ : The elements of the binary icosahedral group are separated into sets corresponding to their eigenvalues as in Table 6.3. Group together elements with eigen-

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 6.3.}
\begin{tabular}[t]{|l|l|}
\hline $\left\{z_{1}, z_{2}\right\}$ & $\#\left\{\gamma \in I^{*}: \operatorname{diag}(\gamma)=\left\{z_{1}, z_{2}\right\}\right\}$ \\
\hline \{1, 1\} & 1 \\
\hline \{-1, -1\} & 1 \\
\hline \{ $i,-i$ \} & 30 \\
\hline $\left\{e^{\pi i / 3}, e^{-\pi i / 3}\right\}$ & 20 \\
\hline $\left\{e^{2 \pi i / 3}, e^{-2 \pi i / 3}\right\}$ & 20 \\
\hline $\left\{e^{\pi i / 5}, e^{-\pi i / 5}\right\}$ & 12 \\
\hline $\left\{e^{2 \pi i / 5}, e^{-2 \pi i / 5}\right\}$ & 12 \\
\hline $\left\{e^{3 \pi i / 5}, e^{-3 \pi i / 5}\right\}$ & 12 \\
\hline $\left\{e^{4 \pi i / 5}, e^{-4 \pi i / 5}\right\}$ & 12 \\
\hline
\end{tabular}
\end{table}
values $\left\{e^{\pi i \ell / 3}, e^{-\pi i \ell / 3}\right\}$, for $\ell=1,2$, as before. Also, group together elements with eigenvalues $\left\{e^{\pi i \ell / 5}, e^{-\pi i \ell / 5}\right\}$, for $\ell=1,2,3,4$, since these constitute the elements of $\left.\left(L(-1,10) / \mathbb{Z}_{2}\right) \backslash I d\right)$. Ignoring elements with eigenvalues $\{i,-i\}$ since they do not
contribute to the sum in (6.8), and decomposing the sum over these sets, we find that
$$\begin{aligned}
\operatorname{dim}\left(H_{I^{*}}^{s f k}\right)= & \frac{1}{30}\left[(2 m-1)-60\left(\left(\frac{m-1}{3}\right)\right)-60\left(\left(\frac{m-1}{5}\right)\right)+15 \cos (\pi(m-1))\right. \\
& \left.\quad+10 \sum_{j=1}^{2} \cos \left(\frac{2 \pi}{3}(m-1) j\right)+6 \sum_{j=1}^{4} \cos \left(\frac{2 \pi}{5}(m-1) j\right)\right] \\
= & \begin{cases}2\left\lfloor\frac{m-1}{3}\right\rfloor+2\left\lfloor\frac{m-1}{5}\right\rfloor-m+3 & m \equiv 17,23,29 \bmod 30 \\
2\left\lfloor\frac{m-1}{5}\right\rfloor+\frac{1-m}{3}+2 & m \equiv 7,13,19 \bmod 30 \\
2\left\lfloor\frac{m-1}{3}\right\rfloor+3\left(\frac{1-m}{5}\right)+2 & m \equiv 11 \bmod 30 \\
\frac{m-1}{15}+2 & m \equiv 1 \bmod 30 .\end{cases}
\end{aligned}$$

The proof for these groups is completed as follows. We have found each $\operatorname{dim}\left(H_{\Gamma^{\prime}}^{s f k}\right)$ in terms of certain greatest integer functions with respect to the particular congruences $\bmod |\Gamma| / 4$. For any positive integers $x, y, z$, satisfying $y<x \bmod z$, notice that
$$\left\lfloor\frac{x-y}{z}\right\rfloor=\frac{x-(x \bmod z)}{z} \in \mathbb{Z} .$$
Using this, the expressions for $\operatorname{dim}\left(H_{\Gamma^{\prime}}^{s f k}\right)$ are easily simplified to obtain $2 b_{\Gamma}-2$.
The idea for the groups $\mathfrak{I}_{m, n}^{2}$ and $\mathfrak{I}_{m}^{3}$ is similar, however as the authors are unaware of a decomposition of these groups into conjugacy classes, we perform an element-wise decomposition of these groups into sets, from which we are able to find the respective eigenvalue decompositions and proceed as above. We will see that all eigenvalues here will be of the form $\left\{z_{1}, z_{2}\right\}=e^{i \theta_{1}}\left\{e^{i \theta_{2}}, e^{-i \theta_{2}}\right\}$, for some $0 \leq \theta_{1}, \theta_{2}<2 \pi$, and therefore prove the following useful identity before we begin.
$$\begin{aligned}
\chi_{\rho}\left(e^{i\left(\theta_{1}+\theta_{2}\right)},\right. & \left.e^{\left(\theta_{1}-i \theta_{2}\right)}\right)=e^{i\left(2 \theta_{1}\right)} \sum_{p=0}^{2 m-2}\left(e^{i\left(\theta_{1}+\theta_{2}\right)}\right)^{2 m-2-p}\left(e^{i\left(\theta_{1}-\theta_{2}\right)}\right)^{p} \\
= & e^{i\left(2 m \theta_{1}\right)} \sum_{p=0}^{2 m-2}\left(e^{i \theta_{2}}\right)^{2 m-2-2 p} \\
= & e^{i\left(2 m \theta_{1}\right)}\left[\sin \left(2(m-1) \theta_{2}\right) \cot \left(\theta_{2}\right)+\cos \left(2(m-1) \theta_{2}\right)\right]
\end{aligned}$$
$\Im_{\boldsymbol{m}, \boldsymbol{n}}^{\mathbf{2}}:$ Recall that $\Gamma^{\prime} \subset \mathrm{U}(2)$ is generated by $\left[1, e^{\pi i / n}\right],\left[e^{\pi i /(2 m)}, \hat{j}\right]$. In Section 3.2, we saw that these actually generate the entire group $\mathfrak{I}_{m, n}^{2}$, but in order to obtain a smooth quotient it was necessary to take a quotient of $\left(\mathcal{O}(-2 m), g_{L B}\right)$, and included $\left[e^{\pi i / m}, 1\right]$ in the set of generators accordingly. To find $\operatorname{dim}\left(H_{\mathfrak{I}_{m, n}^{2}}^{1}\right)$, we first decompose $\Gamma^{\prime}=\mathfrak{I}_{m, n}^{2}$ into the two disjoint sets of elements
\begin{itemize}
\item[-] $S_{1}=\left\{\gamma_{1}^{\ell, k}:=\left[e^{\pi i /(2 m)}, \hat{j}\right]^{2 \ell} \cdot\left[1, e^{\pi i k / n}\right]\right\}_{0 \leq \ell \leq m-1 \text { and } 0 \leq k \leq 2 n-1}$
\item[-] $S_{2}=\left\{\gamma_{2}^{\ell, k}:=\left[e^{\pi i /(2 m)}, \hat{j}\right]^{2 \ell+1} \cdot\left[1, e^{\pi i k / n}\right]\right\}_{0 \leq \ell \leq m-1 \text { and } 0 \leq k \leq 2 n-1}$.
\end{itemize}

Clearly $S_{1}, S_{2} \subset \mathfrak{I}_{m, n}^{2}$ and $S_{1} \cap S_{2}=\varnothing$, so since $\left|S_{1}\right|=\left|S_{2}\right|=2 m n$ and $\left|\mathfrak{I}_{m, n}^{2}\right|=4 m n$ we see that $S_{1} \sqcup S_{2}$ constitutes all of $\mathfrak{I}_{m, n}^{2}$. Next, for arbitrary $\gamma_{1}^{\ell, k} \in S_{1}$ and $\gamma_{2}^{\ell, k} \in S_{2}$, as given above, observe that
\begin{itemize}
\item[-] The eigenvalues of $\gamma_{1}^{\ell, k} \in S_{1}$ are $(-1)^{\ell}\left\{e^{\pi i\left(\frac{\ell}{m}+\frac{k}{n}\right)}, e^{\pi i\left(\frac{\ell}{m}-\frac{k}{n}\right)}\right\}$
\item[-] The eigenvalues of $\gamma_{2}^{\ell, k} \in S_{2}$ are $(-1)^{\ell}\left\{e^{\pi i\left(\frac{2 \ell+1}{2 m}+\frac{1}{2}\right)}, e^{\pi i\left(\frac{2 \ell+1}{2 m}-\frac{1}{2}\right)}\right\}$.
\end{itemize}
From (6.10), the characters of these elements are found to be as follows.
\begin{itemize}
\item[-] $\chi_{\rho}\left(\gamma_{1}^{\ell, k}\right)= \begin{cases}\sin \left(\frac{2 \pi}{n} k(m-1)\right) \cot \left(\frac{\pi}{n} k\right)+\cos \left(\frac{2 \pi}{n} k(m-1)\right) & k \neq 0 \text { or } n \\ 2 m-1 & k=0 \text { or } n .\end{cases}$
\item[-] $\chi_{\rho}\left(\gamma_{2}^{\ell, k}\right)=1$ since $m$ is even.
\end{itemize}
Therefore, decomposing the sum over these sets, we find that
$$\begin{aligned}
\operatorname{dim}\left(H_{\mathfrak{J}_{m, n}^{2}}^{s f k}\right)= & \frac{1}{2 m n}\left[2 m \cdot(2 m-1)-4 m n\left(\left(\frac{m-1}{n}\right)\right)\right. \\
& \left.+2 m n+2 m \sum_{j=1}^{n-1} \cos \left(\frac{2 \pi}{n}(m-1) j\right)\right] \\
= & \begin{cases}2\left\lfloor\frac{m-1}{n}\right\rfloor+2 & m \not \equiv 1 \bmod n \\
2\left(\frac{m-1}{n}\right)+2 & m \equiv 1 \bmod n .\end{cases}
\end{aligned}$$
Finally, using (6.9), observe that $\operatorname{dim}\left(H_{\mathfrak{J}_{m, n}^{2}}^{s f k}\right)=2 b_{\mathfrak{J}_{m, n}^{2}}-2$.
$\boldsymbol{\mathfrak { I }}_{\boldsymbol{m}}^{\mathbf{3}}:$ Recall that $\Gamma^{\prime} \subset \mathrm{U}(2)$ is generated by $[1, \hat{i}],[1, \hat{j}],\left[e^{\pi i /(3 m)},(-1-\hat{i}-\hat{j}+\hat{k}) / 2\right]$. In Section 3.2, we saw that these actually generate the entire group $\Im_{m}^{3}$, but in order to obtain a smooth quotient it was necessary to take a quotient of $\left(\mathcal{O}(-2 m), g_{L B}\right)$, and included $\left[e^{\pi i / m}, 1\right]$ in the set of generators accordingly. Therefore, $\Gamma^{\prime}=\mathfrak{I}_{m}^{3}$ is just $\phi\left(D_{8}^{*} \times\left\langle\left[e^{\pi i /(3 m)},(-1-\hat{i}-\hat{j}+\hat{k}) / 2\right]\right\rangle\right)$. To find $\operatorname{dim}\left(H_{\mathfrak{J}_{m, n,}^{2}}^{1}\right)$, we first decompose $\Gamma^{\prime}=\Im_{m}^{3}$ into twenty-four disjoint sets of elements which we write compactly below as $S_{\alpha, s}$ where the index $\alpha \in\{ \pm 1, \pm \hat{i}, \pm \hat{j}, \pm \hat{k}\}$ and the index $s \in\{0,1,2\}$.
\begin{itemize}
\item[-] $S_{ \pm 1, s}=\left\{\gamma_{ \pm 1, s}^{r}:= \pm\left[e^{\pi i /(3 m)},(-1-\hat{i}-\hat{j}+\hat{k}) / 2\right]^{3 r+s}\right\}_{0 \leq r<m}$
\item[-] $S_{ \pm \hat{i}, s}=\left\{\gamma_{ \pm \hat{i}, s}^{r}:=[1, \pm \hat{i}] *\left[e^{\pi i /(3 m)},(-1-\hat{i}-\hat{j}+\hat{k}) / 2\right]^{3 r+s}\right\}_{0 \leq r<m}$
\item[-] $S_{ \pm \hat{j}, s}=\left\{\gamma_{ \pm \hat{j}, s}^{r}:=[1, \pm \hat{j}] *\left[e^{\pi i /(3 m)},(-1-\hat{i}-\hat{j}+\hat{k}) / 2\right]^{3 r+s}\right\}_{0 \leq r<m}$
\item[-] $S_{ \pm \hat{k}, s}=\left\{\gamma_{ \pm \hat{k}, s}^{r}:=[1, \pm \hat{k}] *\left[e^{\pi i /(3 m)},(-1-\hat{i}-\hat{j}+\hat{k}) / 2\right]^{3 r+s}\right\}_{0 \leq r<m}$
\end{itemize}
Any pair of sets with differing index $s$ are clearly disjoint, so to see that these sets are all pairwise disjoint it is enough to observe that $\gamma_{ \pm 1,1}^{0} \neq \gamma_{ \pm \hat{i}, 1}^{0} \neq \gamma_{ \pm \hat{j}, 1}^{0} \neq \gamma_{ \pm \hat{k}, 1}^{0}$. Since $\left|S_{\alpha, s}\right|=m$, for all $\alpha$ and $s$, and $\left|\Im_{m}^{3}\right|=24 m$, we see that the disjoint union of these sets constitutes all of $\mathfrak{I}_{m}^{3}$. As $r$ ranges from 0 to $m-1$, the eigenvalues of the elements in each of these sets can be found to be as follows.
\begin{itemize}
\begin{itemize}
\item[-] Eigenvalues for $S_{ \pm 1, s}: \pm e^{\frac{\pi i(3 r+s)}{3 m}} \begin{cases}\{1,1\} & s=0 \\ \left\{e^{\frac{2 \pi i}{3}}, e^{\frac{-2 \pi i}{3}}\right\} & s=1,2 .\end{cases}$
- Eigenvalues for $S_{ \pm \hat{i}, s}: \pm e^{\frac{\pi i(3 r+s)}{3 m}} \begin{cases}\{i,-i\} & s=0 \\ \left\{e^{\frac{\pi i}{3}}, e^{\frac{-\pi i}{3}}\right\} & s=1 \\ \left\{e^{\frac{2 \pi i}{3}}, e^{\frac{-2 \pi i}{3}}\right\} & s=2 .\end{cases}$
- Eigenvalues for $S_{ \pm \hat{j}, s}: \pm e^{\frac{\pi i(3 r+s)}{3 m}} \begin{cases}\{i,-i\} & s=0 \\ \left\{e^{\frac{\pi i}{3}}, e^{\frac{-\pi i}{3}}\right\} & s=1 \\ \left\{e^{\frac{2 \pi i}{3}}, e^{\frac{-2 \pi i}{3}}\right\} & s=2 .\end{cases}$
- Eigenvalues for $S_{ \pm \hat{k}, s}: \pm e^{\frac{\pi i(3 r+s)}{3 m}} \begin{cases}\{i,-i\} & s=0 \\ \left\{e^{\frac{2 \pi i}{3}}, e^{\frac{-2 \pi i}{3}}\right\} & s=1,2 .\end{cases}$
Using (6.10), the characters are found to be as follows.
\end{itemize}
\item[-] $\chi_{\rho}\left(\gamma_{ \pm 1,0}^{r}\right)=2 m-1$
\item[-] $\chi_{\rho}\left(\gamma_{ \pm \hat{i}, 0}^{r}\right)=\chi_{\rho}\left(\gamma_{ \pm \hat{j}, 0}^{r}\right)=\chi_{\rho}\left(\gamma_{ \pm \hat{k}, 0}^{r}\right)=1$
\item[-] $\chi_{\rho}\left(\gamma_{ \pm 1,1}^{r}\right)=\chi_{\rho}\left(\gamma_{ \pm \hat{k}, 1}^{r}\right)=e^{2 \pi i / 3}\left[\sin \left(2(m-1) \frac{2 \pi}{3}\right) \cot \left(\frac{2 \pi}{3}\right)+\cos \left(2(m-1) \frac{2 \pi}{3}\right)\right]$ $=-e^{2 \pi i / 3}$ since $m \equiv 0 \bmod 3$
\item[-] $\chi_{\rho}\left(\gamma_{ \pm \hat{i}, 1}^{r}\right)=\chi_{\rho}\left(\gamma_{ \pm \hat{j}, 1}^{r}\right)=e^{2 \pi i / 3}\left[\sin \left(2(m-1) \frac{\pi}{3}\right) \cot \left(\frac{\pi}{3}\right)+\cos \left(2(m-1) \frac{\pi}{3}\right)\right]$ $=-e^{2 \pi i / 3}$ since $m \equiv 0 \bmod 3$
\item[-] $\chi_{\rho}\left(\gamma_{ \pm 1,1}^{r}\right)=\chi_{\rho}\left(\gamma_{ \pm \hat{k}, 1}^{r}\right)=\chi_{\rho}\left(\gamma_{ \pm \hat{i}, 1}^{r}\right)=\chi_{\rho}\left(\gamma_{ \pm \hat{j}, 1}^{r}\right)$ $=e^{4 \pi i / 3}\left[\sin \left(2(m-1) \frac{2 \pi}{3}\right) \cot \left(\frac{2 \pi}{3}\right)+\cos \left(2(m-1) \frac{2 \pi}{3}\right)\right]$ $=-e^{4 \pi i / 3}$ since $m \equiv 0 \bmod 3$.
\end{itemize}
Finally, we find that
$$\begin{aligned}
\operatorname{dim}\left(H_{\mathfrak{J}_{m}^{3}}^{s f k}\right) & =\frac{1}{12 m}\left[2 m \cdot(2 m-1)+6 m-8 m\left(e^{2 \pi i / 3}+e^{4 \pi i / 3}\right)\right] \\
& =\frac{m}{3}+1=2 b_{\mathfrak{J}_{m}^{3}}-2 .
\end{aligned}$$ \(\square\)
6.1. Deformations of complex structure. In this subsection, we give the proof of Theorem 1.4, and discuss the formula (1.8).

Proof of Theorem 1.4. From Proposition 6.1, for any finite non-cyclic subgroup $\Gamma \subset$ U(2) containing no complex reflections, we see that $\left(\mathcal{O}(-2 m), g_{L B}\right)$ always has $H_{\Gamma^{\prime}}^{s f k}$ of positive dimension. As in [Hon13, Hon14], using equivariant deformation theory of the twistor space of LeBrun metrics, the LeBrun metrics consequently have small deformations of complex structure admitting scalar-flat Kähler ALE metrics, which are invariant under the group $\Gamma^{\prime}$. Choose any such deformed metric, and call it $\tilde{g}$.

The quotient of $(\mathcal{O}(-2 m), \tilde{g})$ by $\Gamma^{\prime}$ will then be a complex ALE orbifold with the same types of singular points as before. Consequently, the entire construction in the proof of Theorem 1.3 can be carried out, using one of these deformations as the base metric, to construct scalar-flat Kähler ALE metrics with respect to a small deformation of complex structure (it is important to note that the proof of Theorem 5.1 did not assume the existence of holomorphic coordinates at infinity on $X_{2}$ ). Note, the resulting space is diffeomorphic to the minimal resolution, but is no longer a minimal resolution, since the central rational curve is no longer holomorphic.

Next, notice that each of the corresponding deformations of complex structure has a Kähler cone of real dimension $k_{\Gamma}$. If one of these Kähler classes admits a scalar-flat Kähler ALE metric near the metric constructed in Theorem 1.3, then it is locally unique; this follows from invertibility of the linearized operator shown in the proof of Theorem 1.3. We also use the following: we know there is at least one scalar-flat Kähler ALE metric with respect to the deformed complex structure, so invertibility of the linearized operator as shown in the proof of Theorem 1.3 implies that there is an open set in the Kähler cone of Kähler classes admitting scalar-flat Kähler ALE metrics. This is completely analogous to the situation considered in [LS94a]; the details are similar and are omitted.

The formula (1.7) follows since the deformations arisings from $H_{\Gamma^{\prime}}^{s f k}$ are transverse to the Kähler cone, which holds because Honda's deformations of the LeBrun negative mass metrics on $\mathcal{O}(-2 m)$ are traceless and do not include scalings of the metrics (the Kähler cone is 1-dimensional in this case) [Hon13]. In other words, the parameter space for scalar-flat Kähler deformations of a LeBrun metric on $\mathcal{O}(-n)$ (which is $(n-1)$-dimensional) is naturally isomorphic to the parameter space of the Kuranishi family of complex structures of the Hirzebruch surface $\mathbb{F}_{n}$, and therefore they are not relevant to deformations of a scalar-flat Kähler metric caused by moving a Kähler class. \(\square\)

We next briefly discuss the dimension formula (1.8). The following argument is known, but we give an outline of the proof as it is not easily found by a non-algebraic geometer. Given a minimal resolution $\tilde{X}$ of $\mathbb{C}^{2} / \Gamma$ with exceptional divisor $E=\cup_{i=1}^{k} E_{i}$, with rational curves $E_{i}$, we have the exact sequence
$$0 \rightarrow \operatorname{Der}_{E}(\tilde{X}) \rightarrow \Theta_{\tilde{X}} \rightarrow \oplus_{i=1}^{k} \mathcal{O}_{E_{i}}\left(E_{i}\right) \rightarrow 0,$$
where $\operatorname{Der}_{E}(\tilde{X})$ is sheaf of vector fields on $\tilde{X}$ dual to $\Omega_{\tilde{X}}^{1}(\log (E))$, see [Kaw78]. We next examine the following portion of the associated long exact sequence in cohomology
$$H^{1}\left(\tilde{X}, \operatorname{Der}_{E}(\tilde{X})\right) \rightarrow H^{1}\left(\tilde{X}, \Theta_{\tilde{X}}\right) \rightarrow \oplus_{i=1}^{k} H^{1}\left(\mathcal{O}_{E_{i}}\left(E_{i}\right)\right) \rightarrow H^{2}\left(\operatorname{Der}_{E}(\tilde{X})\right) .$$
By Serre duality,
$$\begin{aligned}
\operatorname{dim}\left(H^{1}\left(\mathcal{O}_{E_{i}}\left(E_{i}\right)\right)\right) & =\operatorname{dim}\left(H^{0}\left(\mathbb{P}^{1}, K \otimes N_{E_{i}}^{*}\right)\right) \\
& =\operatorname{dim}\left(H^{0}\left(\mathcal{O}\left(e_{i}-2\right)\right)=e_{i}-1,\right.
\end{aligned}$$
where $E_{i} \cdot E_{i}=-e_{i}$. Since $\operatorname{dim}_{\mathbb{C}}(\tilde{X})=2$, by Siu's vanishing theorem [Siu69],
$$H^{2}\left(\operatorname{Der}_{E}(\tilde{X})\right)=0 .$$
Finally, using results from [Bri68, Lau73, Wah75] (see also [BK87]), there are no nontrivial deformations of $\tilde{X}$ preserving the entire tree of rational curves, so we have
$$H^{1}\left(\tilde{X}, \operatorname{Der}_{E}(\tilde{X})\right)=0 .$$
Combining the above, this implies that
$$\operatorname{dim}\left(H^{1}\left(\tilde{X}, \Theta_{\tilde{X}}\right)\right)=\sum_{i=1}^{k}\left(e_{i}-1\right) .$$

\section*{7. Extremal Kähler metrics on rational surfaces}

We next discuss complex analytic compactifications of the Brieskorn minimal resolutions. For this, recall the canonical Bochner-Kähler metrics on weighted projective spaces, as well as the notion of conformal compactification discussed in Section 2.4. Also, recall that $\left(\mathbb{C P}_{(1,1, n)}^{2}, g_{B K}\right)$ and $\left(\mathcal{O}(-n), g_{L B}\right)$ are related via Kähler conformal compactification/conformal blow-up [Joy91, DL14].
7.1. Proof of Proposition 1.6. We consider the weighted projective space $\mathbb{C P}_{(1,1,2 m)}^{2}$ and have the following analogue of Theorem 4.1. The group U(2) acts as holomorphic automorphisms. For each non-cyclic finite subgroup $\Gamma \subset \mathrm{U}(2)$ containing no complex reflections, the quotient $\left(\mathbb{C P}_{(1,1,2 m)}^{2}, g_{B K}\right) / \Gamma^{\prime}$ has four singularities: one at the point $[0,0,1]$ with orbifold group $\Gamma$, and three on the 2 -sphere $\Sigma=\left[z_{0}, z_{1}, 0\right]$ (which, once resolved, has self-intersection number $b_{\Gamma}^{\prime}>0$ with respect to the complex orientation on the weighted projective space) with cyclic orbifold groups orientation reversed conjugate to those given in Theorem 4.1 for the corresponding $\Gamma$. (Recall that the canonical Bochner-Kähler metrics and LeBrun negative mass metrics are Kähler with respect to orientation reversed complex structures.) Consequently, these orbifold singularities are of type $L\left(\beta_{i}-\alpha_{i}, \beta_{i}\right)$ for $i=1,2,3$. It is not difficult to see that $\left\{\mathbb{C P}_{(1,1,2 m)}^{2} \backslash \Sigma\right\} / \Gamma^{\prime}$ is biholomorphic to $\mathbb{C}^{2} / \Gamma$. Let $b_{j}^{i}$ be the Hirzebruch-Jung string associated to $L\left(\beta_{i}-\alpha_{i}, \beta_{i}\right)$ for $i=1,2,3$, and $j=1 \ldots \ell_{i}$. Then the compactification is found by adding the tree of rational curves at infinity in Figure 7.1.

Note that by [LM08, Lemma 4.1], a scalar-flat Kähler ALE metric always has a complex analytic compactification which is a rational surface. This also follows directly from the above construction since the compactification is birational to the quotient $\mathbb{C P}_{(1,1,2 m)}^{2} / \Gamma^{\prime}$, and any finite quotient of a rational surface is rational. In particular it is diffeomorphic to either $S^{2} \times S^{2}$ or $\mathbb{C} \mathbb{P}^{2} \# \overline{\mathfrak{C}} \overline{\mathbb{P}}^{2}$ for some $\mathfrak{k} \geq 0$, and this finishes the proof.
7.2. Proof of Theorem 1.7. We begin by noting that the complex analytic compactification of $\mathcal{O}(-n)$ is a Hirzebruch surface $\mathbb{F}_{n}$, obtained by adding the $[+n]$ curve at infinity. With a minor modification of the above process, we start the process with one of Calabi's extremal Kähler metrics $g_{C}$ on the Hirzebruch surface $\mathbb{F}_{2 m}$ [Cal82].

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a5edf7e0-2a3e-42c8-b335-be18e7a456e8-34.jpg?height=681&width=1269&top_left_y=326&top_left_x=410}
\captionsetup{labelformat=empty}
\caption{Figure 7.1. The compactification divisor.}
\end{figure}
This has an isometric U(2) action. Arguing as in Theorem 4.1, it is not hard to see that the quotient by the subgroup $\Gamma$ produces 6 singular points. There are 3 on the quotient of the $[-2 m]$ curve of type $L\left(\alpha_{i}, \beta_{i}\right)$ and 3 on the quotient of the $[2 m]$ curve of type $L\left(\beta_{i}-\alpha_{i}, \beta_{i}\right)$, for $i=1,2,3$. Note that there is a moduli of Calabi's metrics, and the area of the $[2 m]$ and $[-2 m]$ curves can be chosen independently to be any two positive real numbers.

The existence result then follows from a recent gluing theorem for extremal Kähler metrics due to Arezzo-Lena-Mazzieri [ALM15b]. It is interesting to remark, however, that we do not actually need the full generality of this theorem. In our case, using the results of [McC02], we simply note that the quotient of $\left(\mathbb{F}_{2 m}, g_{C}\right)$ by $\Gamma$ has identity component of the isometry group exactly $S^{1}$, so the Lie algebra of Hamiltonian biholomorphisms is 1-dimensional. It is therefore trivial to overcome the obstructions, and it follows, as in Arrezo-Pacard-Singer [APS11], that we may obtain extremal Kähler metrics on the resolution by attaching Calderbank-Singer metrics at each singular point. Furthermore, the metrics obtained will admit a holomorphic isometric $S^{1}$-action. We note that the Calderbank-Singer metrics come in moduli, and the area of each rational curve can be chosen arbitrarily. If any of these spaces happens to be Ricci-flat, then the only change is that the scaling of this space must be chosen differently, which accounts for the factor of $\epsilon^{4}$ in the definition of $f$ and $f^{\prime}$ above.

Finally, since any Calabi metric $g_{C}$ on $\mathbb{F}_{2 m}$ for $m \geq 1$ does not have constant scalar curvature, and the extremal metrics we obtain are small perturbations of the Calabi metric away from the singularities, these extemal metrics do not have constant scalar curvature either (for sufficiently small gluing parameter $\varepsilon$ ).

Remark 7.1. In the above proof, instead of starting with the Hirzebruch surface, we could have started with a Bochner-Kähler metric on $\mathbb{C P}_{(1,1,2 m)}^{2}$ (see below), taken the quotient by $\Gamma^{\prime}$, and then used one of the scalar-flat Kähler metrics from Theorem 1.3 to resolve one of the resulting singularities. However, doing this would make the
$[-b]$ curve have small area. So starting with the Calabi metric allows us to obtain existence for a larger collection of Kähler classes. This is of course related to the fact that the Calabi metrics on $\mathbb{F}_{n}$ limit to the Bochner-Kähler metric on $\mathbb{C P}_{(1,1, n)}^{2}$ as the area of the $[-n]$ curve shrinks to zero [Gau09].

\section*{8. Hyperkähler metrics}

We will now show that the spaces obtained by our construction for $\Gamma \subset \operatorname{SU}(2)$ are in fact hyperkähler (and are therefore ALE of order 4, see [BKN89, CT94]). Note that it follows from [Str10, AV12] that all of the spaces obtained in the proof of Theorem 1.3, are necessarily ALE of order at least 2. Since these spaces are scalar-flat Kähler, hence anti-self-dual, we begin with the following Lemma.

Lemma 8.1. If $(X, g)$ is a scalar-flat anti-self-dual ALE space with $H^{1}(X ; \mathbb{R})=0$, then
$$b_{2}^{-}(X) \geq 2-\frac{2}{|\Gamma|}-3 \eta\left(S^{3} / \Gamma\right)$$
with equality if and only if $g$ is Ricci-flat and $b_{2}^{+}(X)=0$.
Proof. Since $(X, g)$ is an ALE space with $H^{1}(X ; \mathbb{R})=0$, it is clear that
$$\tau_{\text {top }}(X)=b_{2}^{+}-b_{2}^{-} \quad \text { and } \quad \chi_{\text {top }}(X)=1+b_{2}^{+}+b_{2}^{-} .$$
Now, consider the ALE versions of the signature and Chern-Gauss-Bonnet theorems, which for an $\operatorname{ALE}$ space $(M, g)$ with group at infinity $\Gamma \subset \operatorname{SO}(4)$, are given as follows.
$$\tau_{t o p}(M)=\tau_{o r b}(M)+\eta\left(S^{3} / \Gamma\right) \quad \text { and } \quad \chi_{t o p}(M)=\chi_{o r b}(M)+\frac{1}{|\Gamma|},$$
where $\tau_{\text {orb }}(M)$ is the orbifold signature defined by
$$\tau_{o r b}(M)=\frac{1}{12 \pi^{2}} \int_{M}\left(\left|W_{g}^{+}\right|^{2}-\left|W_{g}^{-}\right|^{2}\right) d V_{g},$$
$\eta\left(S^{3} / \Gamma\right)$ is the eta-invariant and $\chi_{\text {orb }}(M)$ is the orbifold Euler characteristic defined by
$$\chi_{o r b}(M)=\frac{1}{8 \pi^{2}} \int_{M}\left(\left|W_{g}\right|^{2}-\frac{\left|E_{g}\right|^{2}}{2}+\frac{R_{g}^{2}}{24}\right) d V_{g} .$$
Then, since $(X, g)$ is anti-self-dual, observe that
$$3 \tau_{\text {top }}(X)+2 \chi_{\text {top }}(X)=5 b_{2}^{+}-b_{2}^{-}+2=-\frac{1}{8 \pi^{2}} \int_{X}\left|E_{g}\right|^{2} d V_{g}+\frac{2}{|\Gamma|}+3 \eta\left(S^{3} / \Gamma\right) .$$
Therefore
$$b_{2}^{-}=\frac{1}{8 \pi^{2}} \int_{X}\left|E_{g}\right|^{2} d V_{g}-\frac{2}{|\Gamma|}-3 \eta\left(S^{3} / \Gamma\right)+2+5 b_{2}^{+},$$
so we find that
$$b_{2}^{-}(X) \geq 2-\frac{2}{|\Gamma|}-3 \eta\left(S^{3} / \Gamma\right),$$
with equality if and only if $E_{g} \equiv 0$, hence $\operatorname{Ric}_{g} \equiv 0$ since $R_{g} \equiv 0$, and $b_{2}^{+}(X)=0$. \(\square\)

Proposition 8.2. For $\Gamma$ a binary polyhedral group, the construction of Theorem 1.3 yields a hyperkähler ALE space which admits a holomorphic isometric circle action.

Proof. The proof of Proposition 8.2 follows easily from Lemma 8.1 below as follows. The spaces obtained in Section 5.3 are scalar-flat Kähler, hence anti-self-dual, and simply connected. From inserting the respective $\eta\left(S^{3} / \Gamma\right)$, given in [Nak90], and $b_{2}^{-}$ into the inequality in Lemma 8.1, we find that these spaces are Ricci-flat, and therefore hyperkähler, if and only if $\Gamma \subset \operatorname{SU}(2)$. \(\square\)

Remark 8.3. It is interesting to note that the only ALE spaces needed for in this construction of hyperkähler metrics are the Gibbons-Hawking multi-Eguchi-Hanson metrics.

Remark 8.4. For the weighted projective space $\mathbb{C P}_{(r, q, q+r)}^{2}$, by a result of Derdzinski [Der83], the conformal metric $R^{-2} g_{B K}$ is Einstein. A simple calculation shows that it is Ricci-flat. This turns out to be the conformal compactification of a multi-Eguchi-Hanson metric with 2 points, one of multiplicity $q$ and the other of multiplicity $r$. Again, these are Kähler with respect to reverse-oriented complex structures.
8.1. Anti-self-dual gluing. We first discuss an "inverse" to the process of conformal compactification described above. Given a compact Riemannian orbifold $(\widehat{X}, \widehat{g})$ with nonnegative Yamabe invariant, and letting $G_{p}$ denote the Green's function of the conformal Laplacian associated to a point $p$, the space $\left(\widehat{X} \backslash\{p\}, G_{p}^{2} \widehat{g}\right)$ is a complete noncompact scalar-flat anti-self-dual ALE orbifold. A coordinate system at infinity arises from using inverted normal coordinates in the metric $\widehat{g}$ around $p$. We refer to this as a conformal blow-up.

In Proposition 8.2, we obtained hyperkähler ALE metrics with groups at infinity the binary polyhedral groups (the "DE" in "ADE"). For these cases, the singularities on the $\mathbb{C P}^{1}$ at the origin of Theorem 4.1 are all of type $L\left(-1, \beta_{i}\right)$, and we used the scalarflat Kähler gluing theorem of Section 5.1 to glue on the appropriate multi-Eguchi-Hanson metrics (the "A" in "ADE") to the quotients of $\left(\mathcal{O}(-2), g_{L B}\right)$. However, this construction only produces some hyperkähler metrics. We will next show that we can obtain examples for all small deformations of complex structure, and therefore an open set in the moduli space, by using the following gluing result for (anti-)self-dual orbifolds.

Theorem 8.5 ([DF89, Flo91, LS94b, KS01, AV15]). Let $\left(X_{1},\left[g_{1}\right]\right)$ and $\left(X_{2},\left[g_{2}\right]\right)$ be self-dual conformal structures on compact 4-dimensional orbifolds with $H_{S D}^{2}$ of the respective self-dual deformation complexes vanishing. Let $p_{1} \in X_{1}$ and $p_{2} \in X_{2}$ be orbifold points with the respective orbifold groups $\Gamma_{1}$ and $\Gamma_{2} \subset \operatorname{SO}(4)$ orientation reversed conjugate in the sense that there is an orientation-reversing intertwining map between these groups. Then, the orbifold connect sum $X_{1} \# X_{2}$, taken at these points, admits self-dual conformal structures.

We will replace the scalar-flat Kähler gluing result in Theorem 5.1 with Theorem 8.5. For any binary polyhedral group $\Gamma^{\prime} \subset \operatorname{SU}(2)$, consider the compact self-dual

Kähler orbifold $\left(\mathbb{C P}_{(1,1,2)}^{2}, g_{B K}\right) / \Gamma^{\prime}$, as discussed above, which has four orbifold points: one with orbifold group $\Gamma$ at the point of compactification, and three on the 2-sphere at infinity with cyclic orbifold groups $L\left(1, \beta_{i}\right)$ for $i=1,2,3$. Recall that these are just the Kähler conformal compactifications of the corresponding quotients of the Eguchi-Hanson metric. LeBrun-Maskit proved that $H_{S D}^{2}$ of the compactification of any scalar-flat Kähler ALE metric vanishes [LM08, Theorem 4.2]. Therefore, to each orbifold point with group $L\left(1, \beta_{i}\right)$ on the 2 -sphere at infinity of $\left(\mathbb{C P}_{(1,1,2 m)}^{2}, g_{B K}\right) / \Gamma^{\prime}$, Theorem 8.5 can be used to attach the conformal compactification of the multi-Eguchi-Hanson metric with group $L\left(-1, \beta_{i}\right)$ at infinity, and obtain a self-dual orbifold with a single orbifold point of type $\Gamma$, and positive Yamabe invariant. Since the Yamabe invariant is positive, we can take the conformal blow-up at the orbifold point to obtain a scalar-flat anti-self-dual ALE metric on the minimal resolution of $\mathbb{C}^{2} / \Gamma$. Once again, notice that the only building blocks here were the multi-Eguchi-Hanson metrics.

Finally, for each binary polyhedral group $\Gamma$, we examine these scalar-flat anti-selfdual ALE metrics using Lemma 8.1. As in the proof of Proposition 8.2, from inserting $\eta\left(S^{3} / \Gamma\right)$ given in [Nak90] and $b_{2}^{-}$into the inequality of Lemma 8.1, it is clear that these metrics are necessarily Ricci-flat, and are therefore hyperkähler ALE metrics.

\section*{References}
[ALM15a] Claudio Arezzo, Riccardo Lena, and Lorenzo Mazzieri, On the Kummer construction for Kcsc metrics, arXiv.org:1507.05105, 2015.
[ALM15b] $\_\_\_\_$, On the resolution of extremal and constant scalar curvature Kähler orbifolds, Int. Math. Res. Not. IMRN (2015), no. RNV346, 1-38.
[AP06] Claudio Arezzo and Frank Pacard, Blowing up and desingularizing constant scalar curvature Kähler manifolds, Acta Math. 196 (2006), no. 2, 179-228.
[AP09] $\_\_\_\_$, Blowing up Kähler manifolds with constant scalar curvature. II, Ann. of Math. (2) 170 (2009), no. 2, 685-738.
[Apo90] Tom M. Apostol, Modular functions and Dirichlet series in number theory, second ed., Graduate Texts in Mathematics, vol. 41, Springer-Verlag, New York, 1990.
[APS11] Claudio Arezzo, Frank Pacard, and Michael Singer, Extremal metrics on blowups, Duke Math. J. 157 (2011), no. 1, 1-51.
[AR15] Vestislav Apostolov and Yann Rollin, ALE scalar-flat Kähler metrics on non-compact weighted projective spaces, arXiv.org:1510.02226, to appear in Math. Ann., 2015.
[AV12] Antonio G. Ache and Jeff A. Viaclovsky, Obstruction-flat asymptotically locally Euclidean metrics, Geom. Funct. Anal. 22 (2012), no. 4, 832-877.
[AV15] $\_\_\_\_$, Asymptotics of the self-dual deformation complex, J. Geom. Anal. 25 (2015), no. 2, 951-1000.
[BK87] Kurt Behnke and Horst Knörrer, On infinitesimal deformations of rational surface singularities, Compositio Math. 61 (1987), no. 1, 103-127.
[BKN89] Shigetoshi Bando, Atsushi Kasue, and Hiraku Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth, Invent. Math. 97 (1989), no. 2, 313-349.
[Boy86] Charles P. Boyer, Conformal duality and compact complex surfaces, Math. Ann. 274 (1986), no. 3, 517-526.
[BR95] Kurt Behnke and Oswald Riemenschneider, Quotient surface singularities and their deformations, Singularity theory (Trieste, 1991), World Sci. Publ., River Edge, NJ, 1995, pp. 1-54.
[BR15] Olivier Biquard and Yann Rollin, Smoothing singular extremal Kähler surfaces and minimal Lagrangians, Advances in Math. 285 (2015), 980-1024.
[Bri68] Egbert Brieskorn, Rationale Singularitäten komplexer Flächen, Invent. Math. 4 (1967/1968), 336-358.
[Bry01] Robert L. Bryant, Bochner-Kähler metrics, J. Amer. Math. Soc. 14 (2001), no. 3, 623-715.
[Bur86] Daniel Burns, Twistors and harmonic maps, Talk in Charlotte, N.C., October 1986.
[Cal82] Eugenio Calabi, Extremal Kähler metrics, Seminar on Differential Geometry, Ann. of Math. Stud., vol. 102, Princeton Univ. Press, Princeton, N.J., 1982, pp. 259-290.
[Cal85] $\_\_\_\_$, Extremal Kähler metrics. II, Differential geometry and complex analysis, Springer, Berlin, 1985, pp. 95-114.
[CH14] Ronan J. Conlon and Hans-Joachim Hein, Asymptotically conical Calabi-Yau manifolds, III, arXiv.org:1405.7140, 2014.
[CLW08] Xiuxiong Chen, Claude Lebrun, and Brian Weber, On conformally Kähler, Einstein manifolds, J. Amer. Math. Soc. 21 (2008), no. 4, 1137-1168.
[Cox40] H. S. M. Coxeter, The binary polyhedral groups, and other generalizations of the quaternion group, Duke Math. J. 7 (1940), 367-379.
[Cox91] $\_\_\_\_$, Regular complex polytopes, 2nd ed., Cambridge University Press, Cambridge, 1991.
[Cro61] D. W. Crowe, The groups of regular complex polygons, Canad. J. Math. 13 (1961), 149-156.
[CS04] David M. J. Calderbank and Michael A. Singer, Einstein metrics and complex singularities, Invent. Math. 156 (2004), no. 2, 405-443.
[CT94] Jeff Cheeger and Gang Tian, On the cone structure at infinity of Ricci flat manifolds with Euclidean volume growth and quadratic curvature decay, Invent. Math. 118 (1994), no. 3, 493-571.
[Der83] Andrzej Derdziński, Self-dual Kähler manifolds and Einstein manifolds of dimension four, Compositio Math. 49 (1983), no. 3, 405-433.
[DF89] S. Donaldson and R. Friedman, Connected sums of self-dual manifolds and deformations of singular spaces, Nonlinearity 2 (1989), no. 2, 197-239.
[DG06] Liana David and Paul Gauduchon, The Bochner-flat geometry of weighted projective spaces, Perspectives in Riemannian geometry, CRM Proc. Lecture Notes, vol. 40, Amer. Math. Soc., Providence, RI, 2006, pp. 109-156.
[DL14] Michael G. Dabkowski and Michael T. Lock, On Kähler conformal compactifications of U $(n)$-invariant ALE spaces, to appear in Ann. Global Anal. Geom., 2014.
[DV64] Patrick Du Val, Homographies, quaternions and rotations, Oxford Mathematical Monographs, Clarendon Press, Oxford, 1964.
[EH79] Tohru Eguchi and Andrew J. Hanson, Self-dual solutions to Euclidean gravity, Ann. Physics 120 (1979), no. 1, 82-106.
[Flo91] Andreas Floer, Self-dual conformal structures on lCP ${ }^{2}$, J. Differential Geom. 33 (1991), no. 2, 551-573.
[FP04] Elisha Falbel and Julien Paupert, Fundamental domains for finite subgroups in $U(2)$ and configurations of Lagrangians, Geom. Dedicata 109 (2004), 221-238.
[Gau09] Paul Gauduchon, Hirzebruch surfaces and weighted projective planes, Riemannian topology and geometric structures on manifolds, Progr. Math., vol. 271, Birkhäuser Boston, Boston, MA, 2009, pp. 25-48.
[GH78] G. W. Gibbons and S. W. Hawking, Gravitational multi-instantons, Physics Letters B 78 (1978), no. 4, 430-432.
[Hir53] Friedrich Hirzebruch, Über vierdimensionale Riemannsche Flächen mehrdeutiger analytischer Funktionen von zwei komplexen Veränderlichen, Math. Ann. 126 (1953), 1-22.
[Hon13] Nobuhiro Honda, Deformation of LeBrun's ALE metrics with negative mass, Comm. Math. Phys. 322 (2013), no. 1, 127-148.
[Hon14] $\_\_\_\_$, Scalar flat Kähler metrics on affine bundles over $\mathbb{C P}^{1}$, SIGMA Symmetry Integrability Geom. Methods Appl. 10 (2014), Paper 046, 25.
[HP78] S. W. Hawking and C. N. Pope, Symmetry breaking by instantons in supergravity, Nuclear Phys. B 146 (1978), no. 2, 381-392.
[Joy91] Dominic Joyce, The hypercomplex quotient and the quaternionic quotient, Math. Ann. 290 (1991), no. 2, 323-340.
[Joy95] $\_\_\_\_$, Explicit construction of self-dual 4-manifolds, Duke Math. J. 77 (1995), no. 3, 519-552.
[Kaw78] Yujiro Kawamata, On deformations of compactifiable complex manifolds, Math. Ann. 235 (1978), no. 3, 247-265.
[Kro89a] P. B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients, J. Differential Geom. 29 (1989), no. 3, 665-683.
[Kro89b] $\_\_\_\_$, A Torelli-type theorem for gravitational instantons, J. Differential Geom. 29 (1989), no. 3, 685-697.
[KS01] A. Kovalev and M. Singer, Gluing theorems for complete anti-self-dual spaces, Geom. Funct. Anal. 11 (2001), no. 6, 1229-1281.
[Lam03] T. Y. Lam, Hamilton's quaternions, Handbook of algebra, Vol. 3, Handb. Algebr., vol. 3, Elsevier/North-Holland, Amsterdam, 2003, pp. 429-454.
[Lau73] Henry B. Laufer, Taut two-dimensional singularities, Math. Ann. 205 (1973), 131-164.
[LeB88] Claude LeBrun, Counter-examples to the generalized positive action conjecture, Comm. Math. Phys. 118 (1988), no. 4, 591-596.
[Li14] Chi Li, On sharp rates and analytic compactifications of asymptotically conical Kähler metrics, arXiv.org:1405.2433, 2014.
[LM08] Claude LeBrun and Bernard Maskit, On optimal 4-dimensional metrics, J. Geom. Anal. 18 (2008), no. 2, 537-564.
[LS94a] C. LeBrun and S. R. Simanca, Extremal Kähler metrics and complex deformation theory, Geom. Funct. Anal. 4 (1994), no. 3, 298-336.
[LS94b] Claude LeBrun and Michael Singer, A Kummer-type construction of self-dual 4manifolds, Math. Ann. 300 (1994), no. 1, 165-180.
[McC02] Darryl McCullough, Isometries of elliptic 3-manifolds, J. London Math. Soc. (2) 65 (2002), no. 1, 167-182.
[McK80] John McKay, Graphs, singularities, and finite groups, The Santa Cruz Conference on Finite Groups (Univ. California, Santa Cruz, Calif., 1979), Proc. Sympos. Pure Math., vol. 37, Amer. Math. Soc., Providence, R.I., 1980, pp. 183-186.
[Nak90] Hiraku Nakajima, Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem, Recent topics in differential and analytic geometry, Academic Press, Boston, MA, 1990, pp. 385-396.
[OR70] Peter Orlik and Frank Raymond, Actions of the torus on 4-manifolds. I, Trans. Amer. Math. Soc. 152 (1970), 531-559.
[RS05] Yann Rollin and Michael Singer, Non-minimal scalar-flat Kähler surfaces and parabolic stability, Invent. Math. 162 (2005), no. 2, 235-270.
[RŞ15] R. Răsdeaconu and I. Şuvaina, ALE Ricci-flat Kähler surfaces and weighted projective spaces, Ann. Global Anal. Geom. 47 (2015), no. 2, 117-134.
[Sco83] Peter Scott, The geometries of 3-manifolds, Bull. London Math. Soc. 15 (1983), no. 5, 401-487.
[Sei33] H. Seifert, Topologie Dreidimensionaler Gefaserter Räume, Acta Math. 60 (1933), no. 1, 147-238.
[Siu69] Yum-tong Siu, Analytic sheaf cohomology groups of dimension $n$ of $n$-dimensional noncompact complex manifolds, Pacific J. Math. 28 (1969), 407-411.
[Ste08] R. Stekolshchik, Notes on Coxeter transformations and the McKay correspondence, Springer Monographs in Mathematics, Springer-Verlag, Berlin, 2008.
[Str10] Jeffrey Streets, Asymptotic curvature decay and removal of singularities of Bach-flat metrics, Trans. Amer. Math. Soc. 362 (2010), no. 3, 1301-1324.
[Szé12] Gábor Székelyhidi, On blowing up extremal Kähler manifolds, Duke Math. J. 161 (2012), no. 8, 1411-1453.
[Szé15] $\_\_\_\_$, Blowing up extremal Kähler manifolds II, Invent. Math. 200 (2015), no. 3, 925-977.
[TS31] W. Threlfall and H. Seifert, Topologische Untersuchung der Diskontinuitätsbereiche endlicher Bewegungsgruppen des dreidimensionalen sphärischen Raumes, Math. Ann. 104 (1931), no. 1, 1-70.
[TS33] $\_\_\_\_$, Topologische Untersuchung der Diskontinuitätsbereiche endlicher Bewegungsgruppen des dreidimensionalen sphärischen Raumes (Schluß), Math. Ann. 107 (1933), no. 1, 543-586.
[TV05] Gang Tian and Jeff Viaclovsky, Moduli spaces of critical Riemannian metrics in dimension four, Adv. Math. 196 (2005), no. 2, 346-372.
[Via10] Jeff Viaclovsky, Monopole metrics and the orbifold Yamabe problem, Annales de L'Institut Fourier 60 (2010), no. 7, 2503-2543.
[Wah75] Jonathan M. Wahl, Vanishing theorems for resolutions of surface singularities, Invent. Math. 31 (1975), no. 1, 17-41.
[Wri11] Dominic Wright, Compact anti-self-dual orbifolds with torus actions, Selecta Math. (N.S.) 17 (2011), no. 2, 223-280.

Department of Mathematics, University of Texas, Austin, TX, 78712
E-mail address: mlock@math.utexas.edu
Department of Mathematics, University of Wisconsin, Madison, WI, 53706
E-mail address: jeffv@math.wisc.edu
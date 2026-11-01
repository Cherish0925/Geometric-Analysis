---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: [1210.4707] Boundary pairs associated with quadratic forms]

Let us now relate the Dirichlet solution operator in different points $z, w \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$. For $f \in \mathscr{H}$ we set
$$U(z, w) f:=f+(z-w) R^{\mathrm{D}}(z) f .$$
Recall the convention $R^{\mathrm{D}}(z) f=\left(H^{\mathrm{D}}-z\right)^{-1} f^{\mathrm{D}} \oplus 0$ if $f=f^{\mathrm{D}} \oplus f^{\perp} \in \mathscr{H}^{0, \mathrm{D}} \oplus\left(\mathscr{H}^{0, \mathrm{D}}\right)^{\perp}=\mathscr{H}$ if ker $\Gamma$ is not dense in $\mathscr{H}$ (see Definition 2.2 (iv)), so that we can also write
$$U(z, w)=\left(H^{\mathrm{D}}-w\right) R^{\mathrm{D}}(z) \oplus \operatorname{id}_{\left(\mathscr{H}^{0, \mathrm{D}}\right)^{\perp}}: \mathscr{H} \longrightarrow \mathscr{H} .$$
It is clear from the spectral calculus that this operator extends respectively restricts to a topological isomorphism $U(z, w)^{k, \mathrm{D} \rightarrow k, \mathrm{D}}: \mathscr{H}^{k, \mathrm{D}} \longrightarrow \mathscr{H}^{k, \mathrm{D}}$ for all $k$ with norm bounded by $C^{\mathrm{D}}(z, w)$, where
$$C^{\mathrm{D}}(z, w):=\left\|\left(H^{\mathrm{D}}-w\right)\left(H^{\mathrm{D}}-z\right)^{-1}\right\|=\sup _{\lambda \in \sigma\left(H^{\mathrm{D}}\right)} \frac{|\lambda-w|}{|\lambda-z|} \leq 1+\frac{|z-w|}{d\left(z, \sigma\left(H^{\mathrm{D}}\right)\right)} .$$
Moreover, an easy calculation using the resolvent equality $R^{\mathrm{D}}(z)-R^{\mathrm{D}}(w)=(z-w) R^{\mathrm{D}}(z) R^{\mathrm{D}}(w)$ shows that $U(z, w) U(w, z) f=f$ for $f \in \mathscr{H}$, i.e., the inverse of $U(z, w)$ is $U(w, z)$. In particular, we have
$$\frac{1}{C^{\mathrm{D}}(w, z)}\|f\|_{\mathscr{H}} \leq\|U(z, w) f\|_{\mathscr{H}} \leq C^{\mathrm{D}}(z, w)\|f\|_{\mathscr{H}}$$
for all $f \in \mathscr{H}$. If $z, w$ are both real, then
$$\frac{1}{C^{\mathrm{D}}(w, z)}\|f\|_{\mathscr{H}}^{2} \leq\langle U(z, w) f, f\rangle_{\mathscr{H}} \leq C^{\mathrm{D}}(z, w)\|f\|_{\mathscr{H}}^{2}$$
for all $f \in \mathscr{H}$, as $U(z, w)$ is self-adjoint in this case. If we restrict $U(z, w)$ to functions $f \in \mathscr{H}^{1}$, then we also have $U(z, w) f \in \mathscr{H}^{1}$ since $R^{\mathrm{D}}(z) f \in \mathscr{H}^{2, \mathrm{D}} \subset \mathscr{H}^{1}$. Therefore, $U(z, w)$ is also an operator in $\mathscr{H}^{1}$ denoted by
$$U(z, w)^{1 \rightarrow 1}: \mathscr{H}^{1} \longrightarrow \mathscr{H}^{1} .$$

The following theorem shows that this operator is a topological isomorphism respecting the solution space splitting; and therefore also relates solution operators at different points:

Theorem 2.21. Let $z, w \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\begin{itemize}
\item[i.] We have $U(z, w)^{1 \rightarrow 1} S(w)=S(z)$ or equivalently
$$S(z)-S(w)=(z-w) R^{\mathrm{D}}(z)^{1 \rightarrow 1} S(w)=(z-w) R^{\mathrm{D}}(w)^{1 \rightarrow 1} S(z): \mathscr{G}^{1 / 2} \longrightarrow \mathscr{H}^{1} .$$
Moreover, the projection onto $\mathscr{N}^{1}(z)$ in $\mathscr{H}^{1}=\mathscr{H}^{1, \mathrm{D}} \dot{+} \mathscr{N}^{1}(z)$ is given by $P(z)=S(z) \Gamma$.
\item[ii.] The map
$$U(z, w)^{1 \rightarrow 1}: \mathscr{H}^{1, \mathrm{D}} \dot{+} \mathscr{N}^{1}(w) \longrightarrow \mathscr{H}^{1, \mathrm{D}} \dot{+} \mathscr{N}^{1}(z)$$
is a topological isomorphism (extending $U(z, w)^{1, \mathrm{D} \rightarrow 1, \mathrm{D}}$ ), respecting the splitting, and its inverse is $U(w, z)^{1 \rightarrow 1}$. Moreover, $U(z, w)^{1 \rightarrow 1}$ has norm bounded by
$$C^{1}(z, w):=\left\|U(z, w)^{1 \rightarrow 1}\right\|_{1 \rightarrow 1} \leq 1+|z-w| \sup _{\lambda \in \sigma\left(H^{\mathrm{D}}\right)} \frac{(\lambda+1)^{1 / 2}}{|\lambda-z|} .$$
\item[iii.] The solution operator $S(z): \mathscr{G}^{1 / 2} \longrightarrow \mathscr{N}^{1}(z)$ is a topological isomorphism with left inverse given by $\Gamma$. Moreover,
$$\frac{1}{C^{1}(-1, z)}\|\varphi\|_{\mathscr{G}^{1 / 2}} \leq\|S(z) \varphi\|_{\mathscr{H}^{1}} \leq C^{1}(z,-1)\|\varphi\|_{\mathscr{G}^{1 / 2}}$$
with $C^{1}(z, w)$ defined in (2.22b).
\item[iv.] The solution operator as function $z \mapsto S(z)$ is holomorphic and the $k$-th derivative is given by $S^{(k)}(z)=$ $k!R^{\mathrm{D}}(z)^{k} S(z): \mathscr{G}^{1 / 2} \longrightarrow \mathscr{H}^{2 k, \mathrm{D}} \hookrightarrow \mathscr{H}^{1}(k \geq 1)$.
\end{itemize}

Proof. (i) Let $f:=S(w) \varphi \in \mathscr{N}^{1}(w)$ and $g:=U(z, w)^{1 \rightarrow 1} f=f+(z-w) R^{\mathrm{D}}(z) f$. We have to show that $g$ is the weak solution of the Dirichlet problem in $z$. The fact that $\Gamma g=\Gamma f=\varphi$ is obvious since $\Gamma R^{\mathrm{D}}(z)=0$. It remains to show that $g \in \mathscr{N}^{1}(z)$. Let $u \in \mathscr{H}^{1, \mathrm{D}}$, then
$$(\mathfrak{h}-z \mathbf{l})(g, u)=(\mathfrak{h}-z \mathbf{l})(f, u)+(z-w)(\mathfrak{h}-z \mathbf{l})\left(R^{\mathrm{D}}(z) f, u\right) .$$
But the latter summand equals $(z-w)\langle f, u\rangle$, so that $(\mathfrak{h}-z \mathbf{l})(g, u)=(\mathfrak{h}-w \mathbf{1})(f, u)=0$ since $f \in \mathscr{N}^{1}(w)$. In particular, we have shown that $g \in \mathscr{N}^{1}(z)$. Moreover, $P(z)=S(z) \Gamma$ follows from (2.22a) with $w=-1$ (see (2.16b)). (ii) We have $U(z, w) U(w, z) f=f$ for $f \in \mathscr{H}^{1}$ since this equality is already true for $f \in \mathscr{H}$. The norm bound can be seen by the estimate
$$\begin{aligned}
\left\|U(z, w)^{1 \rightarrow 1}\right\|_{1 \rightarrow 1} & =\left\|1+(z-w)(H+1)^{1 / 2} R^{\mathrm{D}}(z)(H+1)^{-1 / 2}\right\| \\
& \leq\left\|1+(z-w)\left(H^{\mathrm{D}}+1\right)^{1 / 2} R^{\mathrm{D}}(z)\right\|,
\end{aligned}$$
and this norm bound shows that $U(z, w)^{1 \rightarrow 1}$ is a topological isomorphism from $\mathscr{H}^{1}$ onto $\mathscr{H}^{1}$ with inverse given by $U(z, w)^{1 \rightarrow 1}$. That $U(z, w)^{1 \rightarrow 1}$ respects the splitting actually can be seen as follows: From (i) we know that $U(z, w)^{1 \rightarrow 1} \mathscr{N}^{1}(w) \subset \mathscr{N}^{1}(z)$, and by the definition of $U(z, w)^{1 \rightarrow 1}$, we have $U(z, w)^{1 \rightarrow 1} \mathscr{H}^{1, \mathrm{D}} \subset \mathscr{H}^{1, \mathrm{D}}$. (iii) That $S(z)$ is a topological isomorphism follows already from the fact that $\Gamma$ restricted as map $\mathscr{N}^{1}(z) \rightarrow \mathscr{G}^{1 / 2}$ is bounded and bijective. Finally, the norm bounds on $S(z) \varphi$ follow easily from $S(z)=U(z,-1)^{1 \rightarrow 1} S$. (iv) The formula for the derivative follows immediately from (2.22a). \(\square\)

\subsection*{2.4 The Dirichlet-to-Neumann form at arbitrary points}

Let us now define a sesquilinear form which will be associated with the Dirichlet-to-Neumann operator at $z \in$ $\mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$. We have seen in (1.16) that this form and its associated operator is indeed what we expect from a Dirichlet-to-Neumann operator: Roughly speaking, $\Lambda(z) \varphi$ is the "normal derivative" $\Gamma^{\prime}$ restricted to the boundary of the Dirichlet solution associated with $\varphi$ at $z$, i.e., $\Lambda(z)=\Gamma^{\prime} S(z) \varphi$.

Let us start first with what we call the Dirichlet-to-Neumann form later on:
Theorem 2.23. Let $(\Gamma, \mathscr{G})$ be a boundary pair, $z, w \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$, and $\lambda \in \mathbb{R} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\begin{itemize}
\item[i.] The expression
$$\mathfrak{l}_{z}(\varphi, \psi):=(\mathfrak{h}-z \mathbf{1})(S(z) \varphi, g),$$
where $g \in \mathscr{H}^{1}$ with $\Gamma g=\psi$, is well-defined (i.e., independent of the choice of $g$ ) and defines a symmetric family $\left(\mathfrak{l}_{z}\right)_{z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)}$ of sesquilinear forms $\mathfrak{l}_{z}: \mathscr{G}^{1 / 2} \times \mathscr{G}^{1 / 2} \longrightarrow \mathbb{C}$ (see Section 2.1).
\item[ii.] We have
$$\mathfrak{l}_{z}(\varphi, \psi)-\mathfrak{l}_{w}(\varphi, \psi)=-(z-w)\langle S(z) \varphi, S(\bar{w}) \psi\rangle=-(z-w)\langle S(w) \varphi, S(\bar{z}) \psi\rangle .$$
\end{itemize}
\begin{itemize}
\item[iii.] The sesquilinear form $\mathfrak{l}_{z}: \mathscr{G}^{1 / 2} \times \mathscr{G}^{1 / 2} \longrightarrow \mathbb{C}$ is bounded, i.e., $\left|\mathfrak{l}_{z}(\varphi, \psi)\right| \leq L(z)\|\varphi\|_{1 / 2}\|\psi\|_{1 / 2}$, where
$$L(z):=1+|z+1|\|S(z)\|_{1 / 2 \rightarrow 1} \leq 1+|z+1| C^{1}(z,-1) .$$
\item[iv.] The quadratic form $\mathfrak{l}_{\lambda}: \mathscr{G}^{1 / 2} \longrightarrow \mathbb{C}$ (see Section 2.1) is non-negative for $\lambda \leq 0$ and closed for $\lambda<0$ as form in $\mathscr{G}$ with $\operatorname{dom} \mathfrak{l}_{\lambda}=\mathscr{G}^{1 / 2}$.
\item[v.] If $\lambda_{1} \leq \lambda_{2}$ and $\lambda_{1}, \lambda_{2} \notin \sigma\left(H^{\mathrm{D}}\right)$ then $\mathfrak{l}_{\lambda_{1}} \geq \mathfrak{l}_{\lambda_{2}}$.
\item[vi.] The Dirichlet-to-Neumann form is holomorphic in $z$, i.e., $z \mapsto \mathfrak{l}_{z}(\varphi, \psi)$ depends holomorphically on $z \in \mathbb{C} \backslash$ $\sigma\left(H^{\mathrm{D}}\right)$ for all $\varphi, \psi \in \mathscr{G}^{1 / 2}$. Its derivatives (denoted by $\mathfrak{l}_{z}^{\prime}$ and $\mathfrak{l}_{z}^{(k)}$ ) are bounded sesquilinear forms on $\mathscr{G}^{1 / 2} \times \mathscr{G}^{1 / 2}$ given by
$$\left.\mathfrak{l}_{z}^{\prime}(\varphi, \psi)=-\langle S(z) \varphi, S(\bar{z}) \psi\rangle_{\mathscr{H}} \quad \text { resp. } \quad \mathfrak{l}_{z}^{(k)}(\varphi, \psi)=-k!\left\langle R^{\mathrm{D}}(z)\right)^{k-1} S(z) \varphi, S(\bar{z}) \psi\right\rangle_{\mathscr{H}} .$$
In particular, if $\lambda \in \mathbb{R} \backslash \sigma\left(H^{\mathrm{D}}\right)$ then $\mathfrak{l}_{\lambda}^{\prime} \leq 0$.
\item[vii.] We have (see Section 2.1 for the notion $\operatorname{Im} \mathfrak{l}_{z}$ )
$$\left(\operatorname{Im} \mathfrak{l}_{z}\right)(\varphi)=-(\operatorname{Im} z)\|S(z) \varphi\|_{\mathscr{H}}^{2} \leq 0$$
for $\varphi \in \mathscr{G}^{1 / 2}$ provided $\operatorname{Im} z \geq 0$. In particular, $\left(-\mathfrak{l}_{z}\right)_{z}$ is a form-valued Nevanlinna function.
\end{itemize}

Proof. (i) Let $g_{1}, g_{2} \in \mathscr{H}^{1}$ such that $\Gamma g_{1}=\Gamma g_{2}=\varphi$. Then $g_{1}-g_{2} \in \mathscr{H}^{1, \mathrm{D}}$, and
$$(\mathfrak{h}-z \mathbf{l})\left(S(z) \varphi, g_{1}-g_{2}\right)=0$$
since $S(z) \varphi \in \mathscr{N}^{1}(z)$ is a weak solution by Definitions 2.14 and 2.17. The symmetry of the family is obvious.
(ii) Choosing $g=S(\bar{w}) \varphi$ and using (2.22a), we have
$$\begin{aligned}
\mathfrak{l}_{z}(\varphi, \psi) & =(\mathfrak{h}-z \mathbf{1})(S(z) \varphi, g) \\
& =(\mathfrak{h}-w \mathbf{1})(S(w) \varphi, g)+(z-w)(\mathfrak{h}-w \mathbf{1})\left(R^{\mathrm{D}}(z) S(w) \varphi, g\right)-(z-w)\langle S(z) \varphi, g\rangle \\
& =\mathfrak{l}_{w}(\varphi)-(z-w)\langle S(z) \varphi, g\rangle .
\end{aligned}$$
Note that by this choice of $g$, the middle term in the second line vanishes (by definition of $\mathscr{N}^{1}(w)$ ).
For (iii), we set $w=-1$ in (2.24b) and obtain
$$\left|\mathfrak{l}_{z}(\varphi)\right| \leq\|\varphi\|_{1 / 2}^{2}+|z+1|\|S(z) \varphi\|_{\mathscr{H}}\|S \varphi\|_{\mathscr{H}} .$$
Using the estimates $\|S(z) \varphi\|_{\mathscr{H}} \leq\|S(z) \varphi\|_{\mathscr{H}^{1}}$ and $\|S \varphi\|_{\mathscr{H}} \leq\|S \varphi\|_{\mathscr{H}^{1}}=\|\varphi\|_{1 / 2}$, we obtain the desired bound.
(iv) Obviously, $\mathfrak{l}_{\lambda}(\varphi) \geq 0$ as $(\mathfrak{h}-\lambda \mathfrak{l})(f) \geq 0$ for $\lambda \leq 0$. Moreover, if $\lambda<0$, then
$$\min \{1,-\lambda\}(\mathfrak{h}+\mathbf{\imath})(f) \leq(\mathfrak{h}-\lambda \mathbf{\imath})(f) \leq \max \{1,-\lambda\}(\mathfrak{h}+\mathbf{\imath})(f),$$
hence $\mathfrak{l}_{\lambda}(\varphi)$ defines a squared norm equivalent with $\mathfrak{l}_{-1}(\varphi)=\|S \varphi\|_{\mathscr{H}^{1}}^{2}$, hence $\mathfrak{l}_{\lambda}$ is closed on $\mathscr{G}^{1 / 2}=\operatorname{dom} \mathfrak{l}_{-1}$.
(v) We have
$$\begin{aligned}
\left(\mathfrak{l}_{\lambda_{1}}-\mathfrak{l}_{\lambda_{2}}\right)(\varphi) & =\left(\lambda_{2}-\lambda_{1}\right)\left\langle S\left(\lambda_{1}\right) \varphi, S\left(\lambda_{2}\right) \varphi\right\rangle_{\mathscr{H}} \\
& =\left(\lambda_{2}-\lambda_{1}\right)\left\langle S\left(\lambda_{1}\right) \varphi, U\left(\lambda_{2}, \lambda_{1}\right) S\left(\lambda_{1}\right) \varphi\right\rangle_{\mathscr{H}} \\
& \geq \frac{\lambda_{2}-\lambda_{1}}{C^{\mathrm{D}}\left(\lambda_{1}, \lambda_{2}\right)}\left\|S\left(\lambda_{1}\right) \varphi\right\|_{\mathscr{H}}^{2}
\end{aligned}$$
using (2.24b) for the first equality, Theorem 2.21 (i) for the second and (2.20b) for the last inequality. Since $\lambda_{2}-\lambda_{1} \geq 0$, the result follows.
(vi) and (vii) follow from (2.24b) by letting $w \rightarrow z$ and $w=\bar{z}$, respectively. \(\square\)

Definition 2.25. We call the sesquilinear form $\mathfrak{l}_{z}$ defined in (2.24a) the Dirichlet-to-Neumann form at $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ associated with the boundary pair $(\Gamma, \mathscr{G})$ and the quadratic form $\mathfrak{h}$.

By the previous proposition, $\mathfrak{l}_{z}$ is bounded as form on $\mathscr{G}^{1 / 2} \times \mathscr{G}^{1 / 2}$. We therefore can define an operator
$$\breve{\Lambda}(z): \mathscr{G}^{1 / 2} \longrightarrow \mathscr{G}^{-1 / 2}, \quad \varphi \mapsto \mathfrak{l}_{z}(\varphi, \cdot),$$
called the weak Dirichlet-to-Neumann operator, i.e.,
$$\langle\breve{\Lambda}(z) \varphi, \psi\rangle_{-1 / 2,1 / 2}=\mathfrak{l}_{z}(\varphi, \psi)=(\mathfrak{h}-z \mathbf{l})(S(z) \varphi, S \psi),$$
or $\breve{\Lambda}(z)=S^{*}(\breve{H}-z) S(z): \mathscr{G}^{1 / 2} \rightarrow \mathscr{H}^{1} \rightarrow \mathscr{H}^{-1} \rightarrow \mathscr{G}^{-1 / 2}$ in the scale of Hilbert spaces.

We always have an associated operator with $\mathfrak{l}_{z}$, defined by
$$\operatorname{dom} \Lambda(z):=\left\{\varphi \in \mathscr{G}^{1 / 2} \mid \exists \eta \in \mathscr{G} \forall \psi \in \mathscr{G}^{1 / 2}: \mathfrak{l}_{z}(\varphi, \psi)=\langle\eta, \psi\rangle_{\mathscr{G}}\right\}$$
and $\Lambda(z) \varphi:=\eta$, and that the latter definition is well-defined (since $\mathscr{G}^{1 / 2}=\operatorname{ran} \Gamma$ is dense in $\mathscr{G}$ by definition of a boundary pair). We call this operator the (strong) Dirichlet-to-Neumann operator associated with a boundary pair. Actually, $\Lambda(z)$ is the restriction of $\breve{\Lambda}(z)$ to those $\varphi$ such that $\breve{\Lambda}(z) \varphi \in \mathscr{G}$. It is easily seen that $\varphi \in \operatorname{dom} \Lambda(z)$ can equivalently expressed by
$$\exists u \in \mathscr{H}^{1}, \Gamma u=\varphi \quad \exists \eta \in \mathscr{G} \forall v \in \mathscr{G}^{1 / 2}: \quad(\mathfrak{h}-z \mathbf{l})(u, v)=\langle\eta, \Gamma v\rangle_{\mathscr{G}}$$
without referring to the solution operator (see also the text after (1.22) for this Arendt and ter Elst approach in [AtE12a]).

We use the notation $\breve{\Lambda}(z)$ when we want to stress that we mean the weak Dirichlet-to-Neumann operator, and not the strong Dirichlet-to-Neumann operator.

Note that $\mathfrak{l}_{-1}=\mathfrak{l}$ where $\mathfrak{l}$ is defined in Proposition 2.8 (ii) and that $\Lambda$ is the operator associated with $\mathfrak{l}$ by Definition 2.10 , therefore $\Lambda=\Lambda(-1)$.

\section*{Remark 2.28.}
\begin{itemize}
\item[i.] The Dirichlet-to-Neumann form $\mathfrak{l}_{z}$ with domain dom $\mathfrak{l}_{z}=\mathscr{G}^{1 / 2}$ is closed for $z<0$ by Theorem 2.23 (iv). We will see in Theorem 3.10 that for so-called elliptically regular boundary pairs, $\mathfrak{l}_{z}$ is a closed (and sectorial) form for all $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$; in particular, $\Lambda(z)$ is the associated operator and hence closed. Moreover, the domain of $\Lambda(z)$ is independent of $z$ in this case.
\item[ii.] In general, the forms $\mathfrak{l}_{z}$ are not closed or sectorial resp. bounded from below: In Example 6.15, we construct an example where $\mathfrak{l}_{z}$ is unbounded from both sides for all $z>0$ not in $\sigma\left(H^{\mathrm{D}}\right)$. In this situation, we cannot speak of the closure of a form (in the classical sense) anymore, and more advanced techniques are necessary, see [McI69, McI70] or [GKMV13] and references therein: A sesquilinear form $\mathfrak{a}: \mathscr{G}_{0} \times \mathscr{G}_{0} \longrightarrow \mathbb{C}$ is said to be 0 -closed iff $\mathfrak{a}$ is non-degenerative $\left(\mathfrak{a}(\varphi, \cdot)=0\right.$ implies $\varphi=0$ and $\mathfrak{a}(\cdot, \psi)=0$ implies $\psi=0$ ) and if $\mathscr{G}_{0} \subset \mathscr{G}$ is densely and continuously embedded.
We can show here that $\mathfrak{l}_{z}$ is non-degenerative if $z \notin \sigma(H)$, an argument very similar to the proof of Proposition 2.31 (i) (using the non-degeneracy of the form $\mathfrak{h}-z \mathbf{l}$ as $z \notin \sigma(H)$ ). It follows from Theorem 3.2 of [McI69] that the associated operator $\Lambda(z)$ is closed and has a bounded inverse ( $0 \notin \sigma(\Lambda(z))$ ) (this is actually Theorem 4.11 (iii)). We will show these facts independently in Proposition 2.31.
\item[iii.] It is a priori not clear whether $\Lambda(\lambda)$ as operator associated with $\mathfrak{l}_{z}$ is closed also for $\lambda \in \sigma(H)$ (we need this fact in Theorem 4.14 in order to speak of the spectrum of $\Lambda(z)$ ).
With a trick, we can show that $\Lambda(z)$ is closed for all $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ even for non-elliptically regular boundary pairs under the additional assumption that $R$ is compact, see Theorem 2.36 (v)
\end{itemize}

We state more results on the strong Dirichlet-to-Neumann operator later on (see Proposition 2.31, Theorem 3.10 and Proposition 3.13).

Remark 2.29. Theorem 2.23 (vii) allows us to express the quadratic form $\mathfrak{q}_{z}$ defined by $\mathfrak{q}_{z}(\varphi):=\|S(z) \varphi\|_{\mathscr{H}}^{2}$ in terms of the Dirichlet-to-Neumann form $\mathfrak{l}_{z}$, namely, $\mathfrak{q}_{z}=-\operatorname{Im} \mathfrak{l}_{z} / \operatorname{Im} z$ for $z \in \mathbb{C} \backslash \mathbb{R}$. This fact allows us to detect elliptic regularity and positivity (see Section 3 and Definition 1.10) from the family of Dirichlet-to-Neumann forms. This fact is also useful in reconstructing a boundary pair from a given form-valued Nevanlinna function in the sense of LT77. We will treat this and related questions in a forthcoming publication.

Let us close this subsection with the following result, needed in the proof of Theorem 3.5 (vii) ⇒ (vi):
Proposition 2.30. Let $z \in \mathbb{C} \backslash\left(\sigma\left(H^{\mathrm{D}}\right) \cup \sigma(H)\right)$. Then we have
$$(\breve{\Lambda}(z) \Gamma \breve{R}(z))^{*}=S(\bar{z}): \mathscr{G}^{1 / 2} \longrightarrow \mathscr{H}^{1}$$
Proof. Let $u \in \mathscr{H}^{-1}$ and $\varphi \in \mathscr{G}^{1 / 2}$, then the result follows from
$$\begin{aligned}
\langle\breve{\Lambda}(z) \Gamma \breve{R}(z) u, \varphi\rangle=\mathfrak{l}_{z}(\Gamma \breve{R}(z) u, \varphi) & =(\mathfrak{h}-z \mathbf{l})(S(z) \Gamma \breve{R}(z) u, S(\bar{z}) \varphi) \\
& =(\mathfrak{h}-z \mathbf{l})(\breve{R}(z) u, S(\bar{z}) \varphi)=\langle u, S(\bar{z}) \varphi\rangle
\end{aligned}$$
using the fact that $S(z) \Gamma \breve{R}(z) u-\breve{R}(z) u \in \mathscr{H}^{1, \mathrm{D}}$ and the definition of $\mathscr{N}^{1}(z)$ for the third equality. \(\square\)

\subsection*{2.5 The Neumann-to-Dirichlet operator}

Let us first show that the weak Dirichlet-to-Neumann operator $\breve{\Lambda}(z)$ is invertible if $z$ is not in the Neumann spectrum, and that the function $z \mapsto \Lambda(z)^{-1}$ extends continuously into the Dirichlet spectrum $z \in \sigma\left(H^{\mathrm{D}}\right)$.

Proposition 2.31. Let $z \in \mathbb{C} \backslash\left(\sigma\left(H^{\mathrm{D}}\right) \cup \sigma(H)\right)$. Then we have:
\begin{itemize}
\item[i.] The weak Dirichlet-to-Neumann operator $\breve{\Lambda}(z): \mathscr{G}^{1 / 2} \longrightarrow \mathscr{G}^{-1 / 2}$ is bijective with inverse
$$\breve{\Lambda}(z)^{-1}=\Gamma \breve{R}(z) \Gamma^{*}: \mathscr{G}^{-1 / 2} \longrightarrow \mathscr{G}^{1 / 2} .$$
\item[ii.] The operator-valued function $z \mapsto \breve{\Lambda}(z)^{-1}$ extends into $z \in \sigma\left(H^{\mathrm{D}}\right)$, and the value is again a bounded operator denoted by the same symbol $\breve{\Lambda}(z)^{-1}: \mathscr{G}^{-1 / 2} \longrightarrow \mathscr{G}^{1 / 2}$. The norm of $\breve{\Lambda}(z)^{-1}$ is bounded by $C^{\mathrm{N}}(z,-1)$ where $C^{\mathrm{N}}(z, w)$ is defined as in (2.19) with $H^{\mathrm{D}}$ replaced by $H$.
\item[iii.] Denote by $\Lambda(z)^{-1}: \mathscr{G} \longrightarrow \mathscr{G}$ the operator $\breve{\Lambda}(z)^{-1}$ restricted to $\mathscr{G}$ and with range space $\mathscr{G}$, then $\Lambda(z)^{-1}$ is the inverse of the strong Dirichlet-to-Neumann operator $\Lambda(z): \operatorname{dom} \Lambda(z) \longrightarrow \mathscr{G}$ and $\Lambda(z)^{-1}$ is bounded by $\|\Gamma\|_{1 \rightarrow 0}^{2} C^{\mathrm{N}}(z,-1)$. Moreover, $\Lambda(z)$ is closed for all $z \in \mathbb{C} \backslash\left(\sigma\left(H^{\mathrm{D}}\right) \cup \sigma(H)\right)$ and $0 \notin \sigma(\Lambda(z))$.
\end{itemize}

Proof. (i) Let $\varphi \in \operatorname{ker} \breve{\Lambda}(z)$, i.e., $\mathfrak{l}_{z}(\varphi, \eta)=0$ for all $\eta \in \mathscr{G}^{1 / 2}$. Therefore,
$$0=\mathfrak{l}_{z}(\varphi, \eta)=(\mathfrak{h}-z \mathfrak{l})(S(z) \varphi, g)$$
for all $g \in \mathscr{H}^{1}$ with $\Gamma g=\eta$. Since $z \notin \sigma(H)$, the form $\mathfrak{h}-z \mathbf{l}$ is non-degenerative, and therefore $S(z) \varphi=0$, i.e., $\varphi=0$. In particular, we have shown that $\breve{\Lambda}(z)$ is injective.

For the surjectivity, let $\psi \in \mathscr{G}^{-1 / 2}$. Set $\varphi:=\Gamma \breve{R}(z) \Gamma^{*} \psi$, then $\varphi \in \mathscr{G}^{1 / 2}$, and
$$\langle\breve{\Lambda}(z) \varphi, \eta\rangle_{-1 / 2,1 / 2}=\mathfrak{l}_{z}(\varphi, \eta)=(\mathfrak{h}-z \mathbf{l})\left(S(z) \Gamma \breve{R}(z) \Gamma^{*} \psi, g\right),$$
where $g \in \mathscr{H}^{1}$ with $\Gamma g=\eta$. Moreover, $h=\breve{R}(z) \Gamma^{*} \psi \in \mathscr{N}^{1}(z)$, since $(\mathfrak{h}-z \mathbf{l})(h, f)=\langle\psi, \Gamma f\rangle=0$ for all $f \in \mathscr{H}^{1, \mathrm{D}}$, hence $h=S(z) \Gamma h$ by Theorem 2.21 (i), and we have
$$\langle\breve{\Lambda}(z) \varphi, \eta\rangle_{-1 / 2,1 / 2}=(\mathfrak{h}-z \mathbf{l})(h, g)=\langle\psi, \eta\rangle_{-1 / 2,1 / 2},$$
i.e., we have shown that $\breve{\Lambda}(z) \varphi=\psi$ and $\varphi=\Gamma \breve{R}(z) \Gamma^{*} \psi$, i.e., that $\breve{\Lambda}(z)^{-1}=\Gamma \breve{R}(z) \Gamma^{*}$.
(ii) is obvious from the representation of $\breve{\Lambda}(z)^{-1}$.
(iii) By (i), $\Lambda(z): \operatorname{dom} \Lambda(z) \longrightarrow \mathscr{G}$ is bijective as a restriction of a bijective function and since $\operatorname{dom} \Lambda(z)=\{\varphi \in$ $\left.\mathscr{G}^{1 / 2} \mid \breve{\Lambda}(z) \varphi \in \mathscr{G}\right\}$. Its inverse $\Lambda(z)^{-1}$ is bounded as map $\mathscr{G} \rightarrow \mathscr{G}$ provided $z \notin \sigma(H)$. The strong Dirichlet-to-Neumann operator $\Lambda(\lambda)$ is closed as its inverse is bounded. In particular, it makes sense to speak of the spectrum of $\Lambda(\lambda)$, and by definition of the spectrum, if $\Lambda(\lambda)$ has a bounded inverse then $0 \notin \sigma(\Lambda(\lambda))$. \(\square\)

Definition 2.33. We call $\Lambda(z)^{-1}: \mathscr{G} \longrightarrow \mathscr{G}$ the Neumann-to-Dirichlet operator.
Let us now look at the Neumann-to-Dirichlet operator at different points:
Proposition 2.34. Let $z, w \in \mathbb{C} \backslash \sigma(H)$,
\begin{itemize}
\item[i.] We have
$$\Lambda(z)^{-1}-\Lambda(w)^{-1}=(z-w) \Gamma R(w)(\Gamma R(\bar{z}))^{*}=(z-w) \Gamma R(z)(\Gamma R(\bar{w}))^{*}: \mathscr{G} \longrightarrow \mathscr{G} .$$
\item[ii.] We have $\operatorname{Im} \Lambda(z)^{-1}:=\frac{1}{2 \mathrm{i}}\left(\Lambda(z)^{-1}-\Lambda(\bar{z})^{-1}\right)=(\operatorname{Im} z)(\Gamma R(z))(\Gamma R(z))^{*} \geq 0$. In particular, the map $\Lambda(\cdot)^{-1}: \mathbb{C} \backslash$ $\sigma(H) \longrightarrow \mathscr{B}(\mathscr{G}), z \mapsto \Lambda(z)^{-1}$ is an operator-valued Nevanlinna function.
\end{itemize}

Proof. (i) follows immediately from (2.32) and the resolvent equation. (ii) is obvious from (i). \(\square\)

Theorem 2.36. The following assertions are equivalent:
\begin{itemize}
\item[i.] $\Lambda^{-1}: \mathscr{G} \longrightarrow \mathscr{G}$ is compact,
\item[ii.] $\Lambda(z)^{-1}: \mathscr{G} \longrightarrow \mathscr{G}$ is compact for all $z \in \mathbb{C} \backslash \sigma(H)$ (for some $z \in(-\infty, 0] \backslash \sigma(H)$ )
\item[iii.] $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$ is compact
\end{itemize}

Assume additionally that $R$ is compact. Then any of the above condition is also equivalent with the following:
\begin{itemize}
\item[iv.] For all $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$, there exists $a \geq 0$ such that $(\Lambda(z)+a)^{-1}$ is compact,
\item[v.] For all $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$, the operator $\Lambda(z)$ is closed and has purely discrete spectrum.
\end{itemize}

Proof. (i) ⇒ (ii)\&(iii): We have the factorisation $\Lambda^{-1}=K^{*} K$ with $K=\left(\Gamma R^{1 / 2}\right)^{*}: \mathscr{G} \longrightarrow \mathscr{H}$ by Theorem 2.11 (i) (or Proposition 2.31). Assume now that $\Lambda^{-1}$ is compact, then $K$ is compact, and therefore also $\Gamma=K^{*}(H+1)^{1 / 2}$ (hence (iii) is shown). Moreover, $(\Gamma R)^{*}=R^{1 / 2} K: \mathscr{G} \longrightarrow \mathscr{H}$ is compact, too, and $\Gamma R(z): \mathscr{H} \longrightarrow \mathscr{G}$ is bounded. Hence, by (2.35), we have
$$\Lambda(z)^{-1}=\Lambda^{-1}+(z+1)(\Gamma R(z))(\Gamma R)^{*}$$
which shows that $\Lambda(z)^{-1}$ is compact as operator $\mathscr{G} \rightarrow \mathscr{G}$ for any $z \in \mathbb{C} \backslash \sigma(H)$.
(ii) ⇒ (i) is obvious if the statement is true for all $z \in \mathbb{C} \backslash \sigma(H)$. If it is only true for one $z \in(-\infty, 0] \backslash \sigma(H)$, then we can use a factorisation $\Lambda(z)^{-1}=K^{*} K$ similarly as in the proof of (i) ⇒ (ii) to show the compactness of $\Lambda^{-1}$. (iii) ⇒ (i): The compactness of $\Lambda^{-1}$ follows from $\Lambda^{-1}=\Gamma \Gamma^{1 *}: \mathscr{G} \longrightarrow \mathscr{G}$ (see Theorem 2.11 (i)).

For the assertions (iv) and (v) we need some more notation: Denote by $\mathfrak{h}_{a}$ the quadratic form $\mathfrak{h}_{a}(u)=\mathfrak{h}(u)+a\|\Gamma u\|^{2}$. It can be seen that $\mathfrak{h}_{a}$ is closed, and its associated operator $H_{a}$ is non-negative; moreover $(\Gamma, \mathscr{G})$ is still a boundary pair associated with $\mathfrak{h}_{a}$ (see Section 5.1 for details).
(i) ⇒ (iv): Let $z \notin \sigma\left(H^{\mathrm{D}}\right)$. By Proposition 5.3, there exists $a>0$ such that $z \notin \sigma\left(H_{a}\right)$. By assumption, $\Lambda^{-1}$ is compact, hence $\Lambda_{a}^{-1}=(\Lambda+a)^{-1} \leq \Lambda^{-1}$ is also compact. We can now apply (i) ⇒ (ii) for the boundary pair $(\Gamma, \mathscr{G})$ associated with $\mathfrak{h}_{a}$ and obtain that $\Lambda_{a}(z)^{-1}=(\Lambda(z)+a)^{-1}$ is compact.
(iv) ⇒ (i): Set $z=-1$, then $\Lambda^{-1}=\left(1+a \Lambda^{-1}\right)(\Lambda+a)^{-1}$ and this operator is compact, if $(\Lambda+a)^{-1}$ is. The equivalence (iv) ⇔ (v) is a general fact from operator theory. \(\square\)

We want to remark that, in general, the compactness of $R$ and $\Lambda^{-1}$ are independent of each other as the following tabular shows:

\begin{tabular}[t]{|l|l|l|l|l|}
\hline \multicolumn{3}{|l|}{Operator is compact:} & \multirow[t]{2}{*}{Examples} & \multirow[t]{2}{*}{Remarks} \\
\hline $R$ & $R^{\mathrm{D}}$ & $\Lambda^{-1}$ & & \\
\hline ✓ & ✓ & ✓ & Section 6.3 (compact manifold) & \multirow{6}{*}{Examples cannot be ell. reg.} \\
\hline ✓ & ✓ & × & Example 6.30 (modified manifold example) & \\
\hline × & ✓ & ✓ & Example 6.16 ( $\alpha>2$ ) & \\
\hline × & ✓ & × & Example $6.16(\alpha=2)$ & \\
\hline × & × & ✓ & Example 6.31 cylindrical manifold & \\
\hline × & × & × & Example 6.32 modified cylindrical manifold & \\
\hline
\end{tabular}
✓ - yes; - no. Note that $R$ compact implies $R^{\mathrm{D}}$ compact as $R \geq R^{\mathrm{D}} \geq 0$. Moreover, for elliptically regular boundary pairs (see next section) the compactness of $\Lambda^{-1}$ and $R^{\mathrm{D}}$ implies the compactness of $R$ by the resolvent formula (4.4c).

\section*{3 Boundary pairs with additional properties}

Let us now describe further properties of boundary pairs described in terms of the Dirichlet solution operator and an associated quadratic form. It turns out that these properties allow us to relate the concept of boundary pairs to other concepts such as boundary triples (see Section 1.4). Moreover, one of these properties, called elliptic regularity, allows us to show stronger results on resolvent formulae and spectral characterisations (see Theorem 4.3 (ii) and Theorem 4.14).

\subsection*{3.1 Elliptically regular boundary pairs}

An important case is when the solution form $\mathfrak{q}$ (defined by $\mathfrak{q}(\varphi):=\|S \varphi\|_{\mathscr{H}}^{2}$ for $\varphi \in \mathscr{G}^{1 / 2}$ ) is bounded as form in $\mathscr{G}$. Surprisingly, this property has already been recognised as important in a different context by Brasche et al, and also by Arlinskii, see Remark 3.7

One of the main consequences of the boundedness of $\mathfrak{q}$ is that the Dirichlet-to-Neumann form $\mathfrak{l}_{z}$ is sectorial, and hence, the strong Dirichlet-to-Neumann operator (the operator associated with the form $\mathfrak{l}_{z}$ ) is closed and sectorial. Moreover, its domain $\operatorname{dom} \Lambda(z)$ is independent of $z$ (see Theorem 3.10).

Definition 3.1. Let $(\Gamma, \mathscr{G})$ be a boundary pair. We say that the boundary pair is elliptically regular if the solution form $\mathfrak{q}$ is bounded, i.e., if there is a constant $C>0$ such that
$$\mathfrak{q}(\varphi)=\|S \varphi\|_{\mathscr{H}}^{2} \leq C^{2}\|\varphi\|_{\mathscr{G}}^{2}$$
for all $\varphi \in \mathscr{G}^{1 / 2}$.
Let us first present a simple result for bounded boundary pairs:

Proposition 3.2. Let $(\Gamma, \mathscr{G})$ be a boundary pair and let $S(z)$ be the corresponding weak Dirichlet solution operator. If the boundary pair $(\Gamma, \mathscr{G})$ is bounded, then it is elliptically regular.

Proof. If the boundary pair is bounded, then $\Lambda$ is a bounded operator in $\mathscr{G}$ by Theorem 2.11 (iii). Moreover,
$$\mathfrak{q}(\varphi)=\|S \varphi\|_{\mathscr{H}}^{2} \leq\|S \varphi\|_{\mathscr{H}^{1}}^{2}=\|\varphi\|_{\mathscr{G}^{1 / 2}}^{2}=\langle\Lambda \varphi, \varphi\rangle_{\mathscr{G}} \leq\|\Lambda\|\|\varphi\|_{\mathscr{G}}^{2},$$
for $\varphi \in \mathscr{G}$, i.e., we can choose $C^{2}:=\|\Lambda\|$. \(\square\)

Remark 3.3.
\begin{itemize}
\item[i.] Not all boundary pairs are elliptically regular, see the unbounded Jacobi operator examples in Section 6.2 or the Zaremba problem in Theorem 6.39. Moreover, not all elliptic boundary pairs are bounded (see the manifold examples in Sections 6.3-6.5).
\item[ii.] The notion "elliptically regular" for boundary pairs is actually inspired by our basic example presented in detail in Section 6.3, see in particular Remark 6.23 and also Remark 1.11.
\end{itemize}

The name "elliptically regular" is also justified by the following definition and Theorem 3.5 (v):
Definition 3.4. We say that the sesquilinear form $\mathfrak{l}_{z}: \mathscr{G}^{1 / 2} \times \mathscr{G}^{1 / 2} \longrightarrow \mathbb{C}$ is elliptic in $\mathscr{G}$ if there exist $\alpha>0$ and $\omega(z) \in \mathbb{R}$ such that
$$\left(\operatorname{Re~}_{z}\right)(\varphi)+\omega(z)\|\varphi\|_{\mathscr{G}}^{2} \geq \alpha\|\varphi\|_{\mathscr{G}^{1 / 2}}^{2}$$
for all $\varphi \in \mathscr{G}^{1 / 2}$.
Let us now present some equivalent characterisations:
Theorem 3.5. Let $(\Gamma, \mathscr{G})$ be a boundary pair, then the following assertions are equivalent:
\begin{itemize}
\item[i.] The boundary pair is elliptically regular.
\item[ii.] The solution form $\mathfrak{q}_{z}$ (defined by $\mathfrak{q}_{z}(\varphi):=\| S(z) \varphi^{2}$ for $\varphi \in \mathscr{G}^{1 / 2}$ ) extends to a bounded form, and is associated with a bounded operator $Q(z)$ on $\mathscr{G}$ for some (any) $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\item[iii.] The imaginary part $\operatorname{Im} \mathfrak{l}_{z}:=\frac{1}{2 \mathrm{i}}\left(\mathfrak{l}_{z}-\mathfrak{l}_{z}^{*}\right)\left(=-(\operatorname{Im} z) \mathfrak{q}_{z}\right)$ of the Dirichlet-to-Neumann form $\mathfrak{l}_{z}$ is bounded, and hence associated with a bounded operator $-(\operatorname{Im} z) Q(z)$ on $\mathscr{G}$ for some (any) $z \in \mathbb{C} \backslash \mathbb{R}$.
\item[iv.] The derivative $\mathfrak{l}_{\lambda}^{\prime}$ of the Dirichlet-to-Neumann form is bounded, and hence associated with a bounded operator on $\mathscr{G}$ (given by $\Lambda^{\prime}(\lambda):=-Q(\lambda)$ ) for some (any) $\lambda \in \mathbb{R} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\item[v.] For $z \in \mathbb{R}$ in a neighbourhood of -1 (resp. for all $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ ), there exists $\omega(z)$ such that $\omega(-1)=0$ and $\lim \sup _{a \rightarrow-1} \frac{\omega(a)}{a+1}$ is finite, and the sesquilinear form $\mathfrak{l}_{z}$ is elliptic (in the sense of Definition 3.4) with constants $\alpha=1$ and $\omega(z)$.
\item[vi.] We have $\Gamma(\operatorname{dom} H) \subset \mathscr{G}^{1}(=\operatorname{dom} \Lambda)$.
\item[vii.] The operator $\Lambda \Gamma R$ maps $\mathscr{H}$ into $\mathscr{G}$ and is bounded as operator $\mathscr{H} \rightarrow \mathscr{G}$.
\end{itemize}

Remark 3.6. We have another characterisation using the second boundary map $\Gamma^{\prime}$ and some more rather obvious equivalent characterisations:
\begin{itemize}
\item[i.] In Remark 1.11 we showed that if a boundary pair is elliptically regular, then $\Gamma^{\prime} R^{\mathrm{D}} f \in \mathscr{G}$ for all $f \in \mathscr{H}$. One can extend the definition of $\Gamma^{\prime}$ to $\check{\Gamma}^{\prime}$ such that Green's formula (1.14) remains true, but $\check{\Gamma}^{\prime} f \in \mathscr{G}^{-1 / 2}$ (hence $\left\langle\check{\Gamma}^{\prime} f, \Gamma g\right\rangle$ is the dual pairing $\mathscr{G}^{-1 / 2} \times \mathscr{G}^{1 / 2}$ ). Then we have the equivalent characterisation that $(\Gamma, \mathscr{G})$ is elliptically regular iff $\check{\Gamma}^{\prime} u \in \mathscr{G}$ for all $u \in \operatorname{dom} H^{\mathrm{D}}$, or, formulated in analogy with (vi),
$$\check{\Gamma}^{\prime}\left(\operatorname{dom} H^{\mathrm{D}}\right) \subset \mathscr{G} .$$
\item[] ii] The weak Dirichlet solution operator $S(z)$ extends to a bounded operator $\bar{S}(z): \mathscr{G} \longrightarrow \mathscr{H}$ for some (any) $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\item[] iii' The dual $S(\bar{z})^{*}: \mathscr{H}^{-1} \longrightarrow \mathscr{G}^{-1 / 2}$ of the Dirichlet solution operator $S(\bar{z})$ restricts to a bounded operator $\mathscr{H} \rightarrow \mathscr{G}$ (denoted by $B(z)$ ) for some (any) $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\item[] ii] ${ }^{\prime}$ There is a constant $c>0$ such that $\|\Gamma h\|_{\mathscr{G}} \geq c\|h\|_{\mathscr{H}}$ for all $h \in \mathscr{N}^{1}$.
\end{itemize}

There are equivalent characterisations of elliptic regularity by other authors:
Remark 3.7.
\begin{itemize}
\item[i.] Arlinskii expressed in [Ar00, Sec. 2.4]) a condition under the name condition (e) (in [Ar12, p. 62] it is called condition $(F)$ ) which is equivalent to what we call "elliptic regularity". Note that Arlinskii considers (in our notation) bounded boundary pairs associated with the quadratic form of the Krein extension (see Section 1.5).
\end{itemize}
\begin{itemize}
\item[ii.] The characterisations Theorem 3.5 (vi) and (vii) are due to Ben Amor and Brasche [BABr08] (see also the publication [BBABr11, Thm. 2.7] and the references therein). They showed that elliptic regularity (more precisely, that Theorem 3.5 (vil) and (vii)) are also equivalent to
$$\lim _{a \rightarrow \infty} a\left\|R_{a}-R^{\mathrm{D}}\right\|<\infty,$$
where $R_{a}=\left(H_{a}+1\right)^{-1}$ and where $H_{a}$ is the operator associated with the quadratic form $\mathfrak{h}_{a}(f):=\mathfrak{h}(f)+a\|\Gamma f\|_{\mathscr{G}}^{2}$ for $a \geq 0$ (see Section 5.1 for such Robin-type boundary conditions).
\end{itemize}

Proof of Theorem 3.5. (i) ⇔ (ii): This is a direct consequence of the estimate
$$\frac{1}{C^{\mathrm{D}}(-1, z)^{2}} \mathfrak{q}(\varphi) \leq \mathfrak{q}_{z}(\varphi) \leq C^{\mathrm{D}}(z,-1)^{2} \mathfrak{q}(\varphi)$$
for all $\varphi \in \mathscr{G}^{1 / 2}: \mathfrak{q}_{z}$ is bounded iff $\mathfrak{q}$ is bounded.
For the equivalence of (iii) with (ii), note that $\mathrm{Im}_{z}=-(\operatorname{Im} z) \mathfrak{q}_{z}$ by Theorem 2.23 (vii). Similarly, for (iv) we note that $\mathfrak{l}_{\lambda}^{\prime}=-\mathfrak{q}_{\lambda}$ by Theorem 2.23 (vi).
(i) ⇒ (v) We have
$$\operatorname{Re} \mathfrak{l}_{z}(\varphi)-\mathfrak{l}(\varphi)=-\operatorname{Re}\langle(z+1) U(z,-1) S \varphi, S \varphi\rangle \geq-\omega(z)\|\varphi\|^{2}$$
for $\varphi \in \mathscr{G}^{1 / 2}$ (see Theorem 2.23 (ii) and Theorem 2.21 (i)), where
$$\omega(z):=C^{2} \max \left\{\sup _{\lambda \in \sigma\left(H^{\mathrm{D}}\right)} \operatorname{Re}\left(\frac{(z+1)(\lambda+1)}{\lambda-z}\right), 0\right\},$$
where $C=\|\bar{S}\|_{\mathscr{G} \rightarrow \mathscr{H}}$. Note that the inequality holds by the spectral calculus. Since the real part of the fraction as a function in $\lambda \in \sigma\left(H^{\mathrm{D}}\right)$ is continuous and has a limit as $\lambda \rightarrow \infty$, it attains a maximum $C_{+}(z) \in \mathbb{R}$ (and a minimum $C_{-}(z) \in \mathbb{R}$ ) for $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$. In particular, $\omega(z)=C^{2} \max \left\{C_{+}(z), 0\right\}<\infty$.

If $z=a<0$, then $C_{+}(a)=-(a+1)$ and $C_{-}(a)=(a+1) / a$. Moreover, $\omega(a) /(a+1) \leq 0$ and the limes superior is finite.
(v) ⇒ (i) From Theorem 2.23 (vi) we know that $\mathfrak{l}_{-1}^{\prime}=-\mathfrak{q}_{-1}$. Moreover, from the assumption, we have $-\left(\mathfrak{l}_{a}(\varphi)-\right.$ $\mathfrak{l}(\varphi)) \leq \omega(a)\|\varphi\|^{2}$ for $a<0$ near -1 and $\varphi \in \mathscr{G}^{1 / 2}$. Therefore, we conclude
$$0 \leq\|S \varphi\|^{2}=\mathfrak{q}_{-1}(\varphi)=-\lim _{a \rightarrow-1} \frac{\mathfrak{l}_{a}(\varphi)-\mathfrak{l}(\varphi)}{a+1} \leq \limsup _{a \rightarrow-1} \frac{\omega(a)}{a+1} \cdot\|\varphi\|^{2},$$
hence the boundary pair is elliptically regular with $C^{2}=\limsup _{a \rightarrow-1} \omega(a) /(a+1)$.
(vi) ⇒ (vii) By assumption, $\breve{\Lambda} \Gamma \widetilde{R}(\mathscr{H})=\Lambda \Gamma R(\mathscr{H}) \subset \mathscr{G}$. Assume that $f_{n} \rightarrow f$ in $\mathscr{H}$ and $\psi_{n}:=\Lambda \Gamma R f_{n} \rightarrow \psi$ in $\mathscr{G}$, hence also in $\mathscr{G}^{-1 / 2}$. Moreover, $\psi_{n}=\breve{\Lambda} \Gamma \breve{R} f_{n} \rightarrow \breve{\Lambda} \Gamma \breve{R} f$ in $\mathscr{G}^{-1 / 2}$ since $\breve{\Lambda} \Gamma \breve{R}$ is bounded as operator $\mathscr{H} \hookrightarrow \mathscr{H}^{-1} \xrightarrow[\rightarrow]{\breve{R}}$ $\mathscr{H}^{1} \xrightarrow{\Gamma} \mathscr{G}^{1 / 2} \xrightarrow{\breve{\Lambda}} \mathscr{G}^{-1 / 2}$. Since limits in $\mathscr{G}^{-1 / 2}$ are unique, we have $\breve{\Lambda} \Gamma \breve{R} f=\psi \in \mathscr{G}$. In particular, $\Lambda \Gamma R: \mathscr{H} \longrightarrow \mathscr{G}$ is closed, hence bounded by the closed graph theorem.
(vii) ⇒ (vi) Since $\Lambda \Gamma(\operatorname{dom} H)=\Lambda \Gamma R(\mathscr{H}) \subset \mathscr{G}$ by assumption, we have $\Gamma(\operatorname{dom} H) \subset \mathscr{G}^{1}=\operatorname{dom} \Lambda$.
(i) ⇔ (vii) We have $(\breve{\Lambda} \Gamma \breve{R})^{*}=S: \mathscr{G}^{1 / 2} \longrightarrow \mathscr{H}^{1}$ by Proposition 2.30 for $z=-1$, hence $S$ extends to a bounded operator $\mathscr{G} \rightarrow \mathscr{H}$ (i.e., $\mathfrak{q}$ is a bounded form) iff $\breve{\Lambda} \Gamma \widetilde{R}$ restricts to a bounded operator $\mathscr{H} \rightarrow \mathscr{G}$. \(\square\)

Here are some consequences of elliptic regularity:
Theorem 3.10. Let $(\Gamma, \mathscr{G})$ be an elliptically regular boundary pair and $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$, then the following assertions are true:
\begin{itemize}
\item[i.] The norms $\|\cdot\|_{\mathfrak{l}_{z}}$ and $\|\cdot\|_{\mathscr{G}^{1 / 2}}$ are equivalent, i.e.,
$$\|\varphi\|_{\mathscr{G}^{1 / 2}}^{2} \leq\|\varphi\|_{\mathfrak{l}_{z}}^{2}:=\operatorname{Rel}_{z}(\varphi)+\omega(z)\|\varphi\|_{\mathscr{G}}^{2} \leq\left(L(z)+\omega(z)\|\Gamma\|_{1 \rightarrow 0}^{2}\right)\|\varphi\|_{\mathscr{G}^{1 / 2}}^{2},$$
where $L(z)$ is defined in (2.24c).
\item[ii.] The form $\mathfrak{l}_{\lambda}$ resp. the associated operator $\Lambda(\lambda)$ is bounded from below for all $\lambda \in \mathbb{R} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\item[iii.] The form $\mathfrak{l}_{z}$ is closed and sectorial, i.e., $\mathfrak{l}_{z}(\varphi) \in \Sigma_{\vartheta}-\omega(z)$ for all $\varphi \in \mathscr{G}^{1 / 2}$, where
$$\Sigma_{\vartheta}:=\{w \in \mathbb{C}| | \arg w \mid \leq \vartheta\}$$
for $\vartheta=\vartheta_{z}:=\arctan L(z)$.
\end{itemize}
\begin{itemize}
\item[iv.] The associated operator family $(\Lambda(z))_{z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)}$ is self-adjoint, i.e., $\Lambda(z)^{*}=\Lambda(\bar{z})$. In particular, $\Lambda(z)$ is closed and self-adjoint for $z \in \mathbb{R} \backslash \sigma\left(H^{\mathrm{D}}\right)$. Moreover, the domain is $\operatorname{dom} \Lambda(z)=\mathscr{G}^{1}$, i.e., independent of $z$, and $\Lambda(z)$ considered as operator $\Lambda(z)^{1 \rightarrow 0}: \mathscr{G}^{1} \longrightarrow \mathscr{G}$ is bounded.
\item[v.] The operator $\Lambda(z)$ is sectorial, i.e., we have $\sigma(\Lambda(z)) \subset \Sigma_{\vartheta}-\omega(z)$, i.e., the spectrum of the Dirichlet-to-Neumann map is contained in the sector $\Sigma_{\vartheta}-\omega(z)$ for $\vartheta=\vartheta_{z}$.
\item[vi.] The operator $\Lambda(z)$ is $m$-sectorial in the sense of Kato, i.e.,
$$\left\|(\Lambda(z)-w)^{-1}\right\|_{\mathscr{L}(\mathscr{G})} \leq \frac{1}{|w+\omega(z)| \sin \left(\vartheta_{0}-\vartheta\right)}$$
for $\vartheta_{0} \in(\vartheta, \pi)$ and $w \in \mathbb{C} \backslash\left(\Sigma_{\vartheta_{0}}-\omega(z)\right)$.
\end{itemize}

Proof. (i) follows from the ellipticity of $\mathfrak{l}_{z}$ shown in Theorem 3.5 (v), (2.7) and Theorem 2.23 (iii). (ii) follows immediately from (i) and again (2.7). (iii) The closeness of $\mathfrak{l}_{z}$ on $\mathscr{G}^{1 / 2}$ follows from (i). Moreover, for $\varphi \in \mathscr{G}^{1 / 2} \backslash\{0\}$ we have
$$\frac{\left|\operatorname{Im} \mathfrak{l}_{z}(\varphi)\right|}{\operatorname{Rel}_{z}(\varphi)+\omega(z)\|\varphi\|^{2}} \leq \frac{L(z)}{\alpha}=L(z)$$
using again Theorem 2.23. In particular, $\mathfrak{l}_{z}(\varphi)$ lies in the sector $\Sigma_{\vartheta}-\omega(z)$.
(iv) Note that $\Lambda(z)$ is the operator associated with $\mathfrak{l}_{z}$ in the sense of sesquilinear forms, see [Ka66, Thm. VI.2.1]; in particular, $\Lambda(z)$ is closed and sectorial, and $\operatorname{dom} \Lambda(z)$ is a form core (i.e., dense in $\mathscr{G}^{1 / 2}$. Moreover, $\Lambda(z)$ is the (strong) operator associated with $\mathfrak{l}_{z}$, see (2.26)

For $\mathscr{G}^{1}=\operatorname{dom} \Lambda(z)$ we use the equality
$$\mathfrak{l}_{z}(\varphi, \psi)-\mathfrak{l}(\varphi, \psi)=-(z+1)\langle S(z) \varphi, S \psi\rangle .$$
for $\varphi, \psi \in \mathscr{G}^{1 / 2}$ (see (2.24b)). The inclusion " $\subseteq$ " follows from
$$\begin{aligned}
\|\Lambda(z) \varphi\|=\sup _{\psi \in \mathscr{G}^{1 / 2}} \frac{\mathfrak{l}_{z}(\varphi, \psi)}{\|\psi\|_{\mathscr{G}}} \leq \sup _{\psi \in \mathscr{G}^{1 / 2}} \frac{\langle\Lambda \varphi, \psi\rangle_{\mathscr{G}}+|z+1| \sqrt{\mathfrak{q}_{z}(\varphi) \mathfrak{q}(\psi)}}{\|\psi\|_{\mathscr{G}}} & \\
& \leq\|\Lambda \varphi\|+|z+1| \sqrt{C^{\mathrm{D}}(z, 1)} C^{2}\|\varphi\|_{\mathscr{G}}
\end{aligned}$$
for $\varphi \in \operatorname{dom} \Lambda=\mathscr{G}^{1}$ using (3.8) and the boundedness of $\mathfrak{q}$.
For the inclusion " $\supseteq$ " we argue similarly. The boundedness of $\Lambda(z)$ as operator $\mathscr{G}^{1} \rightarrow \mathscr{G}$ follows also from (3.12). (v)-(vi) can be deduced similarly as in [MuNP13, Sec. 2]. \(\square\)

Note that if the boundary pair is not elliptically regular then $\mathfrak{l}_{z}$ is not necessarily closed on $\mathscr{G}^{1 / 2}$; even worse, $\mathfrak{l}_{z}$ might not be bounded from below or sectorial, see Remark 2.28.

We denote by $B(z): \mathscr{H} \longrightarrow \mathscr{G}$ the adjoint of $\bar{S}(\bar{z}): \mathscr{G} \longrightarrow \mathscr{H}$, i.e., the restriction of $S(\bar{z})^{*}: \mathscr{H}^{-1} \longrightarrow \mathscr{G}^{-1 / 2}$ to $\mathscr{H}$ for an elliptically regular boundary pair. The proof of the following is straightforward from Theorems 2.21 and 2.23:
Proposition 3.13. Assume that $(\Gamma, \mathscr{G})$ is an elliptically regular boundary pair, and that $z, w \notin \sigma\left(H^{\mathrm{D}}\right)$, then the following assertions are true:
\begin{itemize}
\item[i.] We have $B(z)-B(w)=(z-w) B(w) R^{\mathrm{D}}(z): \mathscr{H} \longrightarrow \mathscr{G}$ and the operator is bounded.
\item[ii.] The map $z \rightarrow B(z)$ is holomorphic and the derivatives $B^{(k)}(z)=k!B(z) R^{\mathrm{D}}(z)^{k}: \mathscr{H} \longrightarrow \mathscr{G}$ are bounded.
\item[iii.] We have $\Lambda(z)-\Lambda(w)=-(z-w) \bar{S}(\bar{z})^{*} \bar{S}(w)=-(z-w) B(z) B(\bar{w})^{*}: \mathscr{G} \longrightarrow \mathscr{G}$ and the operator is bounded.
\item[iv.] The derivatives of $\Lambda(\cdot)$ are bounded, i.e.,
$$\Lambda^{(k)}(z)=-k!\bar{S}(\bar{z})^{*} R^{\mathrm{D}}(z)^{k} \bar{S}(z)=-k!B(z) R^{\mathrm{D}}(z)^{k} B(\bar{z})^{*}: \mathscr{H} \longrightarrow \mathscr{G} ;$$
in particular, $\Lambda^{\prime}(z)=-\bar{S}(\bar{z})^{*} \bar{S}(z)=-B(z) B(\bar{z})^{*}$.
\item[v.] The imaginary part $\operatorname{Im} \Lambda(z)=-(\operatorname{Im} z) \bar{S}(z)^{*} \bar{S}(z)=-(\operatorname{Im} z) B(\bar{z}) B(\bar{z})^{*}$ is bounded and non-positive for $\operatorname{Im} z \geq$ 0.
\item[vi.] Assume that $0 \notin \sigma(\Lambda(z))$ and $0 \notin \sigma(\Lambda(w))$, then we have
\end{itemize}
$$\Lambda(z)^{-1}-\Lambda(w)^{-1}=(z-w) \Lambda(z)^{-1} \bar{S}(\bar{w})^{*} \bar{S}(z) \Lambda(w)^{-1}=\Lambda(z)^{-1} B(z) B(\bar{w})^{*} \Lambda(w)^{-1} .$$
Proof. Let us just give a proof for the last assertion: it follows from $\Lambda(z)^{-1}-\Lambda(w)^{-1}=-\Lambda(z)^{-1}(\Lambda(z)-\Lambda(w)) \Lambda(w)^{-1}$ and (iii) and the fact that $\operatorname{dom} \Lambda(z)=\operatorname{dom} \Lambda(w)=\mathscr{G}^{1}$. \(\square\)

Remark 3.14. The last assertion is useful if we know that $\Lambda(\lambda)$ has a bounded inverse without a priori knowing that $\lambda \notin \sigma(H)$, this is needed in the proof of Theorem 4.14 (i). Note that the formula in Proposition 2.34 (i) requires that $z$ and $w$ are not in the Neumann spectrum $\sigma(H)$.

\subsection*{3.2 Positive boundary pairs}

We have a sort of "converse" notion of elliptic regularity, namely, that the solution form $\mathfrak{q}$ is (uniformly) positive:
Definition 3.15. We say that the boundary pair $(\Gamma, \mathscr{G})$ is positive, if the solution form $\mathfrak{q}\left(\mathfrak{q}(\varphi):=\|S \varphi\|_{\mathscr{H}}^{2}, \varphi \in \mathscr{G}^{1 / 2}\right)$ is uniformly positive, i.e., if there is a constant $c>0$ such that
$$\mathfrak{q}(\varphi)=\|S \varphi\|_{\mathscr{H}}^{2} \geq c^{2}\|\varphi\|_{\mathscr{G}}^{2}$$
for all $\varphi \in \mathscr{G}^{1 / 2}$.
Remark 3.16. Not all boundary pairs are positive: a counterexample is given by the manifold model of Section 6.3. We have indicated in Theorem 1.20 how this notion relates to ordinary boundary triples.

For the positivity of a boundary pair, we have the following equivalent characterisations. The proof is very much the same as the one of Theorem 3.5, hence we omit it:

Theorem 3.17. Let $(\Gamma, \mathscr{G})$ be a boundary pair, then the following assertions are equivalent:
\begin{itemize}
\item[i.] The boundary pair is positive.
\item[ii.] The solution form $\mathfrak{q}_{z}$ is uniformly positive for some (any) $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\item[iii.] There is a constant $c(z)>0$ such that $\|S(z)\|_{\mathscr{H}} \geq c(z)\left\|_{\varphi}\right\|_{\mathscr{G}}$ for all $\varphi \in \mathscr{G}^{1 / 2}$ for some (any) $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\item[iv.] The form-valued function $z \rightarrow-\mathfrak{l}_{z}$ is a uniformly strict Nevanlinna function, i.e., $-\operatorname{Im}_{z}$ is uniformly positive for some (any) $z \in \mathbb{C}$ with $\operatorname{Im} z>0$.
\item[] $v$. The negative derivative - $\mathfrak{l}_{\lambda}^{\prime}$ is a uniformly positive form for some (any) $\lambda \in \mathbb{R} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\end{itemize}

Operator-valued functions $-\Lambda(\cdot)$ with $-\operatorname{Im} \Lambda(z)$ being uniformly positive are called uniformly strict Nevanlinna functions in [DHMdS06, p. 5354]. In (iv), we have a form equivalent notion.

\section*{4 Resolvent formulae and spectral relations}

In this section we present some of our main results: a Krein-type resolvent formula (Theorem 4.3) and spectral relations between the Neumann operator and the family of Dirichlet-to-Neumann operators (Theorems 4.11 and 4.14).

\subsection*{4.1 Resolvent formula for boundary pairs}

We will prove a resolvent formula in a rather abstract way. To do so, we first need some technical preparation. Denote by $\pi_{z}: \mathscr{H}^{1} \longrightarrow \mathscr{H}^{1, \mathrm{D}}$ the canonical map associating with $f=w+h \in \mathscr{H}^{1}=\mathscr{H}^{1, \mathrm{D}} \dot{+} \mathscr{N}^{1}(z)$ the component $w \in \mathscr{H}^{1, \mathrm{D}}$ (see (2.16a)) and by $\pi_{z}^{*}$ its dual. We denote by $\breve{H}, \breve{H}^{\mathrm{D}}$ and $\breve{\Lambda}(z)$ the operators $H, H^{\mathrm{D}}$ and $\Lambda(z)$ extended to $\mathscr{H}^{1} \rightarrow \mathscr{H}^{-1}, \mathscr{H}^{1, \mathrm{D}} \rightarrow \mathscr{H}^{-1, \mathrm{D}}, \mathscr{G}^{1 / 2} \rightarrow \mathscr{G}^{-1 / 2}$. respectively. The natural inclusion $\iota=\iota_{1, \mathrm{D} \rightarrow 1}: \mathscr{H}^{1, \mathrm{D}} \hookrightarrow \mathscr{H}^{1}$ is an isometry and induces an operator $\iota^{*}: \mathscr{H}^{-1} \longrightarrow \mathscr{H}^{-1, \mathrm{D}}$. Note that $\iota^{*} \widetilde{f}: \mathscr{H}^{1, \mathrm{D}} \longrightarrow \mathbb{C}$ is defined by $\left(\iota^{*} \widetilde{f}\right)(g)=\widetilde{f}(\iota g)$ for $\widetilde{f} \in \mathscr{H}^{-1}$ and $g \in \mathscr{H}^{1, \mathrm{D}}$. If $f \in \mathscr{H}$ is embedded in $\mathscr{H}^{-1}$ via $\widetilde{f}=\langle f, \cdot\rangle$, then
$$\left(\iota^{*} \widetilde{f}\right)(g)=\langle f, \iota g\rangle=\langle f, g\rangle=\widetilde{f}(g),$$
i.e., $\iota^{*}$ restricted to $\mathscr{H}$ acts as the identity on $\mathscr{H}$.
We have now the following relation between the operators $\breve{H}$ and $\breve{H}^{\mathrm{D}}$ and their resolvents extended to the scale of Hilbert spaces.

Lemma 4.2. Let $z \in \mathbb{C} \backslash\left(\sigma\left(H^{\mathrm{D}}\right) \cup \sigma(H)\right.$, then we have the following identities:
\begin{itemize}
\item[i.] $\iota^{*}(\breve{H}-z)=\left(\breve{H}^{\mathrm{D}}-z\right) \pi_{z}: \mathscr{H}^{1} \longrightarrow \mathscr{H}^{-1, \mathrm{D}}$,
\item[ii.] $\breve{R}^{\mathrm{D}}(z) \iota^{*}=\pi_{z} \breve{R}(z): \mathscr{H}^{-1} \longrightarrow \mathscr{H}^{1, \mathrm{D}}$,
\item[iii.] $\iota \pi_{z}=\iota \breve{R}^{\mathrm{D}}(z) \iota^{*}(\breve{H}-z): \mathscr{H}^{1} \longrightarrow \mathscr{H}^{1}$ is the projection onto $\mathscr{H}^{1, \mathrm{D}}$ with kernel $\mathscr{N}^{1}(z)$, Moreover, the comple-mentary projection is given by $\mathrm{id}_{\mathscr{H}^{1}}-\iota \pi_{z}=P(z)(=S(z) \Gamma)$.
\item[iv.] $P(z) \breve{R}(z)=\breve{R}(z) P(\bar{z})^{*}: \mathscr{H}^{-1} \longrightarrow \mathscr{H}^{1}$.
\end{itemize}

Proof. (i) Let $f \in \mathscr{H}^{1}$ and $g \in \mathscr{H}^{1, \mathrm{D}}$. Then $f=w+h$ with $w=\pi_{z} f$ according to the decomposition $\mathscr{H}^{1}=$ $\mathscr{H}^{1, \mathrm{D}} \dot{+} \mathscr{N}^{1}(z)$. Moreover,
$$\left\langle\iota^{*}(\breve{H}-z) f, g\right\rangle_{\mathscr{H}^{-1, \mathrm{D}}, \mathscr{H}^{1, \mathrm{D}}}=(\mathfrak{h}-z \mathbf{l})(f, g)=(\mathfrak{h}-z \mathbf{l})(w, g)=\left\langle\left(\breve{H}^{\mathrm{D}}-z\right) \pi_{z} f, g\right\rangle_{1,-1},$$
since $(\mathfrak{h}-z \mathbf{l})(h, g)=0\left(h \in \mathscr{N}^{1}(z)\right.$ and $g \in \mathscr{H}^{1, \mathrm{D}}$, see Definition 2.14).
(ii) follows from (i) by multiplying with the resolvents.

For (iii), note that $\left(\mathrm{id}_{\mathscr{H}^{1}}-\imath \pi_{z}\right) f=h=P(z) f$ is the complementary projection onto $\mathscr{N}^{1}(z)$. Moreover, we have $\iota \breve{R}^{\mathrm{D}}(z) \iota^{*}(\breve{H}-z)=\iota \pi_{z} \breve{R}(z)(\breve{H}-z)=\iota \pi_{z}$ by (iii).
(iv) follows from
$$\begin{aligned}
& P(z) \breve{R}(z)=\left(\operatorname{id}_{\left.\mathscr{H}^{1}-\iota \pi_{i}\right) \breve{R}(z)=\breve{R}(z)-\iota \breve{R}^{\mathrm{D}}(z) \iota^{*}=\breve{R}(z)}-\left(\breve{R}^{\mathrm{D}}(\bar{z}) \iota^{*}\right)^{*} \iota^{*}\right. \\
&=\breve{R}(z)-\left(\pi_{\bar{z}} \breve{R}(\bar{z})\right)^{*} \iota^{*}=\breve{R}(z)\left(\operatorname{id}_{\mathscr{H}-1}-\left(\iota \pi_{\bar{z}}\right)^{*}=\breve{R} P(\bar{z})^{*},\right.
\end{aligned}$$
where we used (ii) twice (once for $z$ in the second and once in its dual version for $\bar{z}$ in the fourth equality). \(\square\)

We have now prepared all ingredients in order to prove one of the main theorems for boundary pairs, a weak version of the so-called Krein's resolvent formula. This formula allows us to detect the Neumann spectrum as the "zeros" (Theorems 4.11 and 4.14) of the Dirichlet-to-Neumann operator.
Theorem 4.3. Assume that $(\Gamma, \mathscr{G})$ is a boundary pair associated with the quadratic form $\mathfrak{h}$ and that $z \in \mathbb{C} \backslash\left(\sigma\left(H^{\mathrm{D}}\right) \cup\right.$ $\sigma(H))$.
\begin{itemize}
\item[i.] We have the following weak versions of Krein's resolvent identity:
$$\begin{aligned}
\breve{R}(z)-\iota \breve{R}^{\mathrm{D}}(z) \iota^{*} & =P(z) \breve{R}(z) \\
& =S(z) \breve{\Lambda}(z)^{-1} S(\bar{z})^{*}: \mathscr{H}^{-1} \xrightarrow{S(\bar{z})^{*}} \mathscr{G}^{-1 / 2} \xrightarrow{\breve{\Lambda}(z)^{-1}} \mathscr{G}^{1 / 2} \xrightarrow{S(z)} \mathscr{H}^{1}, \\
R(z)-R^{\mathrm{D}}(z) & =S(z) \breve{\Lambda}(z)^{-1} S(\bar{z})^{*}: \mathscr{H}^{S} \xrightarrow{S(\bar{z})^{*}} \mathscr{G}^{-1 / 2} \xrightarrow{\breve{\Lambda}(z)^{-1}} \mathscr{G}^{1 / 2} \xrightarrow{S(z)} \mathscr{H} .
\end{aligned}$$
\item[ii.] If, in addition, the boundary pair is elliptically regular, then
$$R(z)-R^{\mathrm{D}}(z)=\bar{S}(z) \Lambda(z)^{-1} \bar{S}(\bar{z})^{*}: \mathscr{H} \xrightarrow{\bar{S}(\bar{z})^{*}} \mathscr{G} \xrightarrow{\Lambda(z)^{-1}} \mathscr{G} \xrightarrow{\bar{S}(z)} \mathscr{H},$$
i.e., these operators do not leave the original Hilbert spaces $\mathscr{G}$ and $\mathscr{H}$.
\end{itemize}
Proof. (i) We have
$$\begin{aligned}
\breve{R}(z)-\iota \breve{R}^{\mathrm{D}}(z) \iota^{*} & =\left(\operatorname{id}_{\mathscr{H}^{1}}-\iota \pi_{z}\right) \breve{R}(z) \\
& =P(z) \breve{R}(z)=P(z)^{2} \breve{R}(z)=P(z) \breve{R}(z) P(\bar{z})^{*}=S(z) \Gamma \breve{R}(z) \Gamma^{*} S(\bar{z})^{*}
\end{aligned}$$
using Lemma 4.2. Finally, in Proposition 2.31 we showed that
$$\Gamma \breve{R}(z) \Gamma^{*}=\breve{\Lambda}(z)^{-1}$$
as an operator $\mathscr{G}^{-1 / 2} \rightarrow \mathscr{G}^{1 / 2}$, and the resolvent formula (4.4a) follows, as well as (4.4b). (ii) is just a consequence of (4.4a) together with Remark 3.6 and Proposition 2.31 (iii). \(\square\)

\subsection*{4.2 Operator pencils}

For the spectral relations in Theorem 4.14, we need some results on operator pencils on $\mathscr{G}$, which we define here in the form we need it (see e.g. [Tr00, EL04] and references therein). We restrict ourselves to the case where $T(z)-T\left(z_{0}\right)$ are bounded operators for all $z$ (which corresponds to the elliptic regular case in our application later on, see Remark 4.9 (ii)):
Definition 4.5. Let $D \subset \mathbb{C}$ be open with $\bar{D}=D$. We say that $T(\cdot)=\{T(z)\}_{z \in D}$ is a holomorphic self-adjoint operator pencil if $T(z)^{*}=T(\bar{z})$ and $z \mapsto T(z)-T\left(z_{0}\right)$ is holomorphic with values in the set of bounded operators on $\mathscr{G}$ for some $z_{0} \in D$.

The spectrum of the operator pencil $T(\cdot)$ is given by
$$\sigma(T(\cdot)):=\{z \in \mathbb{C} \mid T(z) \text { is not invertible }\} .$$
We say that $\lambda$ is an eigenvalue of $T(\cdot)$ (shortly $\lambda \in \sigma_{\mathrm{p}}(T(\cdot))$ if $T(\lambda)$ is not injective.
Note that the usual spectrum of an operator $A$ is the operator pencil spectrum of the operator pencil $z \mapsto A-z$. Fix $\lambda \in D \cap \mathbb{R}$. It follows that if
$$T(z)=A_{0}-(z-\lambda) A_{1}-(z-\lambda)^{2} A_{2}(z)$$
then $A_{0}=T(\lambda)$ is self-adjoint (and possibly unbounded), where $A_{1}=-T^{\prime}(\lambda)$ is self-adjoint and bounded and where $z \mapsto A_{2}(z)$ is holomorphic with values in the bounded operators on $\mathscr{G}$. Then it is obvious that $\lambda \in \sigma_{\mathrm{p}}(T(\cdot))$ iff $\lambda \in \sigma_{\mathrm{p}}\left(A_{0}\right)$, but it is not clear whether $\lambda \in \sigma(T(\cdot))$ iff $\lambda \in \sigma\left(A_{0}\right)$ or whether $\lambda$ is isolated in $\sigma(T(\cdot))$ iff $\lambda$ is isolated in $\sigma\left(A_{0}\right)$. For the latter assertion, we need more assumptions:

Proposition 4.6. Assume that $T(\cdot)$ is a holomorphic self-adjoint operator pencil on $D$ and that $\lambda \in D \cap \mathbb{R}$. Assume that $A_{1}:=-T^{\prime}(\lambda)$ is (bounded and) uniformly positive (i.e., there are constants $0<c \leq C<\infty$ such that $c\|\varphi\|^{2} \leq$ $\left\langle A_{1} \varphi, \varphi\right\rangle \leq C\|\varphi\|^{2}$ ). Then the following assertions are equivalent:
\begin{itemize}
\item[i.] $\lambda$ is isolated in $\sigma(T(\cdot))$ and
$$T(z)^{-1}=\frac{1}{z-\lambda} T_{\lambda}(z)+\hat{T}_{\lambda}(z)$$
where $T_{\lambda}(\cdot)$ and $\hat{T}_{\lambda}(\cdot)$ are holomorphic (bounded) operator functions near $z=\lambda$;
\item[ii.] 0 is isolated in the individual operator spectrum $\sigma(T(\lambda))$.
\end{itemize}

Proof. Without loss of generality, we can assume that $\lambda=0$; otherwise consider $\widetilde{T}(z):=T(z+\lambda)$.
Let us first consider the situation $A_{2}(z)=0$ for all $z \in D$. In this case, we do not need the expression (4.7) for $T(z)^{-1}$. Note first that $\operatorname{ker} T(0)=\operatorname{ker} A_{0}$, hence $0 \in \sigma_{\mathrm{p}}(T(\cdot))$ iff $0 \in \sigma_{\mathrm{p}}\left(A_{0}\right)$. Moreover, we have
$$T(z)=A_{0}-z A_{1}=A_{1}^{1 / 2}\left(A_{1}^{-1 / 2} A_{0} A_{1}^{-1 / 2}-z\right) A_{1}^{1 / 2} .$$
Now, $T(z)$ is invertible iff $A_{1}^{-1 / 2} A_{0} A_{1}^{-1 / 2}-z$ is invertible, and 0 is isolated in $\sigma\left(A_{1}^{-1 / 2} A_{0} A_{1}^{-1 / 2}\right)$ iff 0 is isolated in $\sigma\left(A_{0}\right)$ (see e.g. [BGPa08, Lem 3.1]).

Let us now consider the general situation and prove (i)⇒(ii): We have
$$S(z):=T(z)^{-1}\left(A_{0}-z A_{1}\right)=T(z)^{-1}\left(T(z)+z^{2} A_{2}(z)\right)=\operatorname{id}_{\mathscr{G}}+z^{2} T(z)^{-1} A_{2}(z) .$$
Using (4.7) we have
$$z^{2} T(z)^{-1} A_{2}(z)=\left(z T_{0}(z)+z^{2} \hat{T}_{0}(z)\right) A_{2}(z)$$
and this operator family is bounded near $z=0$ (including $z=0$ ). In particular, if $|z|$ is small enough, then $S(z)$ is invertible, hence $A_{0}-z A_{1}=T(z) S(z)$ is invertible, too. Therefore, we have shown that 0 is isolated in the spectrum of the operator pencil $z \mapsto A_{0}-z A_{1}$. From the first part (the case $A_{2}(z)=0$ ), it follows that $0 \in \sigma\left(A_{0}\right)$ is isolated. (ii) ⇒(i): Let $0 \in \sigma\left(A_{0}\right)$ be isolated then 0 is isolated in the spectrum of $z \mapsto A_{0}-z A_{1}$, again by the first part (the case $A_{2}(z)=0$ ). Using (4.8) we have
$$\left(A_{0}-z A_{1}\right)^{-1}=A_{1}^{-1 / 2}(B-z)^{-1} A_{1}^{-1 / 2}=A_{1}^{-1 / 2}\left(-\frac{1}{z} \mathbb{1}_{\{0\}}(B)+B_{0}^{-1}\right) A_{1}^{-1 / 2}$$
where $B:=A_{1}^{-1 / 2} A_{0} A_{1}^{-1 / 2}$ and where $B_{0}$ is the restriction of $B$ onto $\operatorname{ker} B^{\perp}$. In particular, we have a representation of the inverse as in (4.7), and in order to show that $T(z)$ has a bounded inverse for $0<|z|$ small enough we can argue similarly as in (i) ⇒ (ii). \(\square\)

\section*{Remark 4.9.}
\begin{itemize}
\item[i.] The non-trivial assertion in Proposition 4.6 is the fact that $\lambda$ and 0 are isolated in the spectra, i.e., that $T(z)$ and $T(\lambda)-z$ are invertible for all $z \neq \lambda$ near $\lambda$.
\item[ii.] In our application, the operator pencil will be $\Lambda(\cdot)$. If we assume that the boundary pair is elliptically regular, then $\Lambda(\cdot)$ is a holomorphic self-adjoint operator pencil on $D=\mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ as in Definition 4.5 since $\Lambda(z)^{*}=\Lambda(\bar{z})$ (Theorem 3.10 (iv)) and
$$\begin{aligned}
\Lambda(z) & =\Lambda(\lambda)-(z-\lambda) \bar{S}(\lambda)^{*} \bar{S}(z) \\
& =\Lambda(\lambda)-(z-\lambda) \bar{S}(\lambda)^{*}\left(\bar{S}(\lambda)+(z-\lambda) R^{\mathrm{D}}(z) \bar{S}(\lambda)\right) \\
& =\Lambda(\lambda)-(z-\lambda) Q(\lambda)-(z-\lambda)^{2} A_{2, \lambda}(z), \quad A_{2, \lambda}(z):=\bar{S}(\lambda)^{*} R^{\mathrm{D}}(z) \bar{S}(\lambda)
\end{aligned}$$
by Theorem 2.21 and Proposition 3.13. In particular, $A_{0}=\Lambda(\lambda)$ and $A_{1}=Q(\lambda)$. Moreover, $z \rightarrow A_{2, \lambda}(z)$ is holomorphic and $\left\|A_{2, \lambda}(z)\right\| \leq\|\bar{S}(\lambda)\|^{2} / d\left(z, \sigma\left(H^{\mathrm{D}}\right)\right)$. In particular, $\Lambda(z)-\Lambda(\lambda)$ is a bounded operator.
The boundedness of $A_{1}=Q(\lambda)$ means that the boundary pair is elliptically regular and the uniform positivity of $A_{1}$ means that the boundary pair is positive.
\item[iii.] We are not aware of a counterexample of an operator pencil where $A_{1}=-T^{\prime}(\lambda)$ is uniformly positive, but not bounded. However, we use Proposition 4.6 in Theorem 4.14 (iv), and Example 6.18 is a counterexample to the assertion of the theorem (the boundary pair is positive, but not elliptically regular), see also Remark 4.17 (iii).
\item[iv.] Also, we cannot drop the uniform positivity of $A_{1}$, as the counterexample given below in Example 4.10 shows (e.g. assuming that $A_{1}$ is bounded and injective, but not uniformly positive). This means that it is not enough for the application of Proposition 4.6 that the boundary pair is elliptically regular, but not positive (as in the case of our basic example, a Laplacian on a manifold with boundary). Nevertheless, we are not aware of a boundary pair which is elliptically regular but not positive, such that the assertion of Proposition 4.6 is false for $T(\cdot)=\Lambda(\cdot)$.
\end{itemize}

The author is indebted to Michael Strauss for the following example:
Example 4.10. We give here a counterexample for "(ii)⇒(i)" in Proposition 4.6 violating the uniform positivity of $A_{1}$, even in the situation when $A_{2}(z)=0$ : Let $T(z):=A_{0}-z A_{1}$ with $A_{0}=A_{0}^{*}$ and $A_{1}=A_{1}^{*} \geq 0$ specified below:

Let 0 be an isolated eigenvalue of $A_{0}$ of infinite multiplicity in the essential spectrum of $A_{0}$. Denote by $\left(\varphi_{n}\right)_{n}$ an orthonormal basis of the eigenspace $\operatorname{ker} A_{0}$. Set
$$A_{1}:=\mathbb{1}_{\mathbb{R} \backslash\{0\}}\left(A_{0}\right)+\sum_{n} \frac{1}{n}\left\langle\varphi_{n}, \cdot\right\rangle \varphi_{n}$$
then $A_{1}$ is bounded, non-negative and injective (but not uniformly positive). Moreover, $T(z) \varphi_{n}=-(z / n) \varphi_{n}$, hence $-z / n \in \sigma(T(\cdot))$ and $\left\|T(z) \varphi_{n}\right\| \rightarrow 0$ showing that $T(z)$ does not have a bounded inverse for any $z \in \mathbb{C}$. In particular, $0 \in \sigma(T(\cdot))$, but 0 is not isolated.

\subsection*{4.3 Spectral relations between the Neumann and the Dirichlet-to-Neumann operator family}

We can now prove some important consequences of Krein's resolvent formula and other formulae for the Dirichlet-to-Neumann operator. In particular, we have the following spectral relations:

Theorem 4.11. Assume that $(\Gamma, \mathscr{G})$ is a boundary pair associated with the quadratic form $\mathfrak{h}$ and let $\lambda \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$. Then the following assertions are true:
\begin{itemize}
\item[i.] The Dirichlet solution operator $S(\lambda)$ is a topological isomorphism from $\operatorname{ker} \Lambda(\lambda)$ onto $\operatorname{ker}(H-\lambda)$ with inverse $\Gamma$, i.e.,
$$\operatorname{ker}(H-\lambda)=S(\lambda) \operatorname{ker} \Lambda(\lambda) .$$
In particular, we have the spectral relation
$$\lambda \in \sigma_{\mathrm{p}}(H) \quad \Leftrightarrow \quad 0 \in \sigma_{\mathrm{p}}(\Lambda(\lambda)) .$$
for the point spectrum (the set of eigenvalues). Moreover, the multiplicity of an eigenspace is preserved.
\item[ii.] Assume that $R: \mathscr{H} \longrightarrow \mathscr{H}$ and $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$ are compact operators, then the spectra of $H, H^{\mathrm{D}}$ and $\Lambda(\lambda)$ are purely discrete. Moreover, the spectral relation (4.12b) is true for the discrete (hence the entire) spectrum, i.e., (4.12b) holds with $\sigma_{\mathrm{p}}(\cdot)$ replaced by $\sigma_{\text {disc }}(\cdot)$ or $\sigma(\cdot)$.
\item[iii.] If $\lambda \notin \sigma(H)$, then $\Lambda(\lambda)$ has a bounded inverse. In particular, $\Lambda(\lambda)$ is closed and $0 \notin \sigma(\Lambda(\lambda))$. (The converse is in general false, see Remark 4.17 (i) and Example 6.17, but true for isolated eigenvalues, see (i) and the next assertion (iv) ).
\item[iv.] Assume that $\lambda$ is isolated in $\sigma(H)$, then there exist $r_{1}>0$ and $C_{\lambda}>0$ (depending only on $\lambda, \sigma(H)$ and $r_{1}$ ) such that
$$\left\|\Lambda(z)^{-1}\right\|_{\mathscr{G} \rightarrow \mathscr{G}} \leq\|\Gamma\|_{1 \rightarrow 0}^{2} \frac{C_{\lambda}}{|z-\lambda|}$$
for all $z \neq \lambda$ and $|z-\lambda| \leq r_{1}$. Moreover, $\lambda$ is an isolated eigenvalue in the operator pencil spectrum $\sigma(\Lambda(\cdot))$, i.e.,
$$\lambda \text { is isolated in } \sigma(H) \quad \Rightarrow \quad \lambda \text { is isolated in the operator pencil spectrum } \sigma(\Lambda(\cdot)) \text {. }$$
\end{itemize}

Proof. (i) Let $\varphi \in \operatorname{ker} \Lambda(\lambda)$ and $h:=S(\lambda) \varphi$, then
$$(\mathfrak{h}-\lambda \mathfrak{l})(h, g)=\mathfrak{l}_{\lambda}(\varphi, \Gamma g)=\langle\Lambda(\lambda) \varphi, \Gamma g\rangle=0$$
for $g \in \mathscr{H}^{1}$ by the definition of $\mathfrak{l}_{\lambda}$ in (2.24a), hence $h \in \operatorname{dom} H$ and $(H-\lambda) h=0$.
On the other hand, if $h \in \operatorname{ker}(H-\lambda)$ then it is easily seen that $h \in \mathscr{N}^{1}(\lambda)$. Set $\varphi:=\Gamma h$, then $h=S(\lambda) \varphi$ and a similar calculation as above shows that $\varphi \in \operatorname{dom} \Lambda(\lambda)$ and $\Lambda(\lambda) \varphi=0$.

The spectral equivalence (4.12b) for the point spectrum is obvious from (4.12a), as well as the preserved multiplicity. (ii) It follows from Theorem 2.36 that the spectrum of $\Lambda(\lambda)$ is discrete (see also Proposition 5.2 (vi) for the discreteness of $\sigma\left(H^{\mathrm{D}}\right)$ ). The spectral relation is then a consequence of part (i).
(iii) Assume that $\lambda \notin \sigma(H)$, then $\Lambda(\lambda)^{-1}=\Gamma R(\lambda) \Gamma^{*}$ exists and is bounded as operator $\mathscr{G} \rightarrow \mathscr{G}$ by Proposition 2.31 (iii). In particular, $\Lambda(\lambda)$ is closed and has a bounded inverse, hence $0 \notin \sigma(\Lambda(\lambda))$.
(iv) If $\lambda$ is isolated in $\sigma(H)$, then there exists $r_{1}>0$ such that, for all $z \in \mathbb{C}$ with $0<|z-\lambda| \leq r_{1}$, the resolvent $R(z)$ has a first order pole at $\lambda$, i.e.,
$$R(z)=\frac{1}{\lambda-z} \mathbb{1}_{\{\lambda\}}(H)+R_{\lambda}(z),$$
where $R_{\lambda}(z)$ is the resolvent of $H \upharpoonright_{\operatorname{ker}(H-\lambda)^{\perp}}$, and the same equation is true with $R(z), \mathbb{1}_{\{\lambda\}}(H)$ and $R_{\lambda}(z): \mathscr{H} \longrightarrow \mathscr{H}$ replaced by $\breve{R}(z), \breve{\mathbb{1}}_{\{\lambda\}}(H)$ and $\breve{R}_{\lambda}(z): \mathscr{H}^{-1} \longrightarrow \mathscr{H}^{1}$. By Proposition 2.31, we have
$$\Lambda(z)^{-1}=\Gamma \breve{R}(z) \Gamma^{*}=\frac{1}{\lambda-z} \Gamma \breve{\mathbb{1}}_{\{\lambda\}}(H) \Gamma^{*}+\Gamma \breve{R}_{\lambda}(z) \Gamma^{*}$$
as operator in $\mathscr{G}$. In particular, $\Lambda(z)^{-1}$ has a first order pole at $z=\lambda$ and
$$\begin{aligned}
& \left\|(\lambda-z) \Lambda(z)^{-1}\right\| \leq\|\Gamma\|_{1 \rightarrow 0}^{2}\left(\left\|\breve{\mathbb{1}}_{\{\lambda\}}(H)\right\|_{-1 \rightarrow 1}+|\lambda-z|\left\|\breve{R}_{\lambda}(z)\right\|_{-1 \rightarrow 1}\right)=\|\Gamma\|_{1 \rightarrow 0}^{2} C_{\lambda}(z), \\
& \text { where } \quad C_{\lambda}(z):=|\lambda+1|+|\lambda-z| \sup _{\lambda^{\prime} \in \sigma(H) \backslash\{\lambda\}} \frac{\left|\lambda^{\prime}+1\right|}{\left|z-\lambda^{\prime}\right|}
\end{aligned}$$
Note that $C_{\lambda}(z)<\infty$ since $\lambda$ is isolated in $\sigma(H)$ and since the fraction tends to 1 as $\lambda^{\prime} \rightarrow \infty$. Since $z \rightarrow C_{\lambda}(z)$ is continuous, $C_{\lambda}:=\sup C_{\lambda}\left(\left\{z \in \mathbb{C}| | z-\lambda \mid \leq r_{1}\right\}\right)<\infty$.

We have therefore shown that $z \notin \sigma(\Lambda(\cdot))$ for $0<|z| \leq r_{1}$. For the last assertion, it remains to show that $\lambda$ is an eigenvalue of $\Lambda(\lambda)$, but this follows immediately from (i). \(\square\)
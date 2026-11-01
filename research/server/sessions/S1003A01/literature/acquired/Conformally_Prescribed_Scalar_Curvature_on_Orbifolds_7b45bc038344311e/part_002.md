---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Conformally Prescribed Scalar Curvature on Orbifolds]

Next, we estimate the most important term $M_{k}^{2} I_{k, 5}$.
Lemma 4.5. There exists a constant $0<\delta<1$ such that when $\sigma<\delta$,
$$\lim _{k \rightarrow \infty} M_{k}^{2} I_{k, 5}=\frac{2 \Delta_{x} K_{\infty}(\bar{x}) \cdot \operatorname{Vol}\left(S^{3}\right)}{3|\Gamma| K_{\infty}(\bar{x})^{2}} .$$
Proof. First, note that $\lim _{k \rightarrow \infty} f_{k}^{-\tau_{k}}(x)=1$, and
$$\lim _{k \rightarrow \infty}\left|\nabla_{x} f_{k}^{-\tau_{k}}(x)\right|=\lim _{k \rightarrow \infty}-\tau_{k} f_{k}^{-\tau_{k}-1}(x)\left|\nabla_{x} f_{k}(x)\right|=0$$
uniformly for $|x| \leq \sigma$. It follows
$$\begin{aligned}
\lim _{k \rightarrow \infty} M_{k}^{2} I_{k, 5} & =\frac{1}{p_{k}+1} M_{k}^{2} \int_{\{|x| \leq \sigma\} / \Gamma}\left(x \cdot \nabla_{x}\left(K_{k} f_{k}^{-\tau_{k}}\right)\right) u_{k}^{p_{k}+1} \\
& =\frac{1}{p_{k}+1} M_{k}^{2} \int_{\{|x| \leq \sigma\} / \Gamma}\left(x \cdot \nabla_{x} K_{k}\right) u_{k}^{p_{k}+1} \\
& =\frac{1}{p_{k}+1} M_{k}^{2+\tau_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left(y \cdot \nabla_{y} \tilde{K}_{k}\right) v_{k}^{p_{k}+1} .
\end{aligned}$$
There exists a constant $0<\delta<1$ such that when $\sigma<\delta$, by power series expansion and Proposition 3.10, we have
$$\begin{aligned}
K_{k}(x) & =K_{k}(0)+\left(K_{k}\right)_{, i}(0) x^{i}+\frac{1}{2}\left(K_{k}\right)_{, i j}(0) x^{i} x^{j}+O\left(|x|^{3}\right) \\
& =K_{k}(0)+\frac{1}{2}\left(K_{k}\right)_{, i j}(0) x^{i} x^{j}+O\left(M_{k}^{-2+2 \delta}|x|\right)+O\left(|x|^{3}\right),
\end{aligned}$$
for $|x| \leq \sigma$, where $\left(K_{k}\right)_{, i j}(0)$ denotes the second order partial derivatives of $K_{k}$ in coordinates $\left\{x^{i}\right\}$ at the point $x_{k}$. It is not hard to verify that
$$\begin{aligned}
& x \cdot \nabla_{x}\left[K_{k}(0)+O\left(M_{k}^{-2+2 \delta}|x|\right)+O\left(|x|^{3}\right)\right]=O\left(M_{k}^{-2+2 \delta}|x|\right)+O\left(|x|^{3}\right), \\
& x \cdot \nabla_{x}\left(\frac{1}{2}\left(K_{k}\right)_{, i j}(0) x^{i} x^{j}\right)=\left(K_{k}\right)_{, i j}(0) x^{i} x^{j} .
\end{aligned}$$
Thus
$$x \cdot \nabla_{x} K_{k}(x)=\left(K_{k}\right)_{, i j}(0) x^{i} x^{j}+O\left(M_{k}^{-2+2 \delta}|x|\right)+O\left(|x|^{3}\right),$$
which implies
$$y \cdot \nabla_{y} \tilde{K}_{k}(y)=M_{k}^{-\left(p_{k}-1\right)}\left(K_{k}\right)_{, i j}(0) y^{i} y^{j}+O\left(M_{k}^{-2-\frac{p_{k}-1}{2}+2 \delta}|y|\right)+O\left(M_{k}^{-3 \frac{p_{k}-1}{2}}|y|^{3}\right) .$$
Hence
$$\left|y \cdot \nabla_{y} \tilde{K}_{k}(y)\right| \leq C M_{k}^{-\left(p_{k}-1\right)}(1+|y|)^{2}$$
and
$$\left|y \cdot \nabla_{y} \tilde{K}_{k}(y)-M_{k}^{-\left(p_{k}-1\right)}\left(K_{k}\right)_{, i j}(0) y^{i} y^{j}\right| \leq C M_{k}^{-3 \frac{p_{k}-1}{2}}(1+|y|)^{3},$$
for $|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}$ and large $k$.
On the other hand, by power series expansion and Proposition 3.13,
$$\begin{aligned}
\left|v_{k}^{p_{k}+1}(y)-U_{K_{k}\left(x_{k}\right)}^{p_{k}+1}(y)\right| & \leq C \cdot\left(p_{k}+1\right) U_{K_{k}\left(x_{k}\right)}^{p_{k}}(y)\left|v_{k}(y)-U_{K_{k}\left(x_{k}\right)}(y)\right| \\
& \leq C\left(1+|y|^{2}\right)^{-p_{k}} M_{k}^{-2} .
\end{aligned}$$
Together with estimate (4.41), for large $k$, we have
$$\begin{aligned}
& M_{k}^{2+\tau_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left(y \cdot \nabla_{y} \tilde{K}_{k}\right)\left|v_{k}^{p_{k}+1}-U_{K_{k}\left(x_{k}\right)}^{p_{k}+1}\right| \\
\leq & C M_{k}^{2+\tau_{k}} M_{k}^{-\left(p_{k}-1\right)} M_{k}^{-2} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}(1+|y|)^{2}\left(1+|y|^{2}\right)^{-p_{k}} \\
\leq & C M_{k}^{-\left(p_{k}-1\right)+\tau_{k}} \int_{0}^{\sigma M_{k}^{\frac{p_{k}-1}{2}}} r^{3}(1+r)^{2}\left(1+r^{2}\right)^{-3+o(1)} d r \\
\leq & C M_{k}^{-\left(p_{k}-1\right)+\tau_{k}}\left(\sigma M_{k}^{\frac{p_{k}-1}{2}}+C_{1}\right) \leq C M_{k}^{-\frac{p_{k}-1}{2}+\tau_{k}} \rightarrow 0 \text { as } k \rightarrow \infty .
\end{aligned}$$
Therefore,
$$\lim _{k \rightarrow \infty} M_{k}^{2} I_{k, 5}=\lim _{k \rightarrow \infty} \frac{1}{p_{k}+1} M_{k}^{2+\tau_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left(y \cdot \nabla_{y} \tilde{K}_{k}\right) U_{K_{k}\left(x_{k}\right)}^{p_{k}+1} .$$
Using estimate (4.42), for large $k$, we have
$$\begin{aligned}
& M_{k}^{2+\tau_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left|y \cdot \nabla_{y} \tilde{K}_{k}(y)-M_{k}^{-\left(p_{k}-1\right)}\left(K_{k}\right), i j(0) y^{i} y^{j}\right| \cdot U_{K_{k}\left(x_{k}\right)}^{p_{k}+1} \\
& \leq C M_{k}^{2+\tau_{k}} M_{k}^{-3 \frac{p_{k}-1}{2}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}(1+|y|)^{3}\left(1+|y|^{2}\right)^{-4+o(1)} \\
& \leq C M_{k}^{2-3 \frac{p_{k}-1}{2}+\tau_{k}} \int_{0}^{\sigma M_{k}^{\frac{p_{k}-1}{2}}} r^{3}(1+r)^{3}\left(1+r^{2}\right)^{-4+o(1)} d r \\
& \leq C M_{k}^{2-3 \frac{p_{k}-1}{2}+\tau_{k}}\left(\left(\sigma M_{k}^{\frac{p_{k}-1}{2}}\right)^{-1+o(1)}+C_{1}\right) \rightarrow 0 \text { as } k \rightarrow 0 .
\end{aligned}$$
Therefore,
$$\lim _{k \rightarrow \infty} M_{k}^{2} I_{k, 5}=\lim _{k \rightarrow \infty} \frac{1}{p_{k}+1} M_{k}^{2 \tau_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left(K_{k}\right)_{, i j}(0) y^{i} y^{j} U_{K_{k}\left(x_{k}\right)}^{p_{k}+1} .$$
Since $U_{K_{k}\left(x_{k}\right)}$ is a radial function,
$$\int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma} y^{i} y^{j} U_{K_{k}\left(x_{k}\right)}= \begin{cases}0, & i \neq j, \\ \frac{1}{4} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}|y|^{2} U_{K_{k}\left(x_{k}\right)}, & i=j .\end{cases}$$

Thus we obtain
$$\lim _{k \rightarrow \infty} M_{k}^{2} I_{k, 5}=\lim _{k \rightarrow \infty} \frac{1}{p_{k}+1} M_{k}^{2 \tau_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma} \frac{1}{4} \Delta_{x} K_{k}(0) \cdot|y|^{2} U_{K_{k}\left(x_{k}\right)}^{p_{k}+1},$$
where $\Delta_{x} K_{k}(0)=\Delta_{x} K_{k}\left(x_{k}\right)$ is the Laplacian of $K_{k}$ in coordinates $\left\{x^{i}\right\}$ at the point $x_{k}$. Because $\Delta_{x} K_{k}\left(x_{k}\right) \rightarrow \Delta_{x} K_{\infty}(\bar{x})$ and $U_{K_{k}\left(x_{k}\right)}^{p_{k}+1} \rightarrow U_{K_{\infty}(\bar{x})}^{4}$ uniformly on $\mathbb{R}^{4} / \Gamma$, we have
$$\begin{aligned}
\lim _{k \rightarrow \infty} M_{k}^{2} I_{k, 5} & =\frac{1}{16} \int_{y \in \mathbb{R}^{4} / \Gamma} \Delta_{x} K_{\infty}(\bar{x}) \cdot|y|^{2}\left(\frac{8}{K_{\infty}(\bar{x})}\right)^{2}\left(1+|y|^{2}\right)^{-4} \\
& =\frac{4 \Delta_{x} K_{\infty}(\bar{x}) \cdot \operatorname{Vol}\left(S^{3}\right)}{|\Gamma| K_{\infty}(\bar{x})^{2}} \int_{0}^{\infty} r^{5}\left(1+r^{2}\right)^{-4} d r \\
& =\frac{2 \Delta_{x} K_{\infty}(\bar{x}) \cdot \operatorname{Vol}\left(S^{3}\right)}{3|\Gamma| K_{\infty}(\bar{x})^{2}}
\end{aligned}$$ \(\square\)

Finally, we have achieved the following proposition.
Proposition 4.6. Assuming Condition 3.7, we have the following inequality
$$\lim _{\sigma \rightarrow 0} P\left(\sigma, h_{\bar{x}}\right) \geq \frac{2 \Delta_{g} K_{\infty}(\bar{x}) \cdot \operatorname{Vol}\left(S^{3}\right)}{3|\Gamma| K_{\infty}(\bar{x})^{2}} .$$
Moreover, if $\tau_{k}=0$ for all $k$, we have the equality
$$\lim _{\sigma \rightarrow 0} P\left(\sigma, h_{\bar{x}}\right)=\frac{2 \Delta_{g} K_{\infty}(\bar{x}) \cdot \operatorname{Vol}\left(S^{3}\right)}{3|\Gamma| K_{\infty}(\bar{x})^{2}} .$$
Here, $\Delta_{g}$ is the Laplacian with respect to the limit conformal normal metric $g$.
Proof. By Lemma 4.1 - Lemma 4.5 and equation (4.16),
$$\lim _{\sigma \rightarrow 0} \limsup _{k \rightarrow \infty} M_{k}^{2} I_{k, 7}=\frac{2 \Delta_{g} K_{\infty}(\bar{x}) \cdot \operatorname{Vol}\left(S^{3}\right)}{3|\Gamma| K_{\infty}(\bar{x})^{2}}+\lim _{\sigma \rightarrow 0} \limsup _{k \rightarrow \infty} M_{k}^{2} I_{k, 6} .$$
By Corollary 3.12,
$$\begin{aligned}
& \limsup _{k \rightarrow \infty} M_{k}^{2} I_{k, 7} \\
= & \limsup _{k \rightarrow \infty} \int_{\{|x|=\sigma\} / \Gamma}\left\{\left(\left|\frac{\partial\left(M_{k} u_{k}\right)}{\partial \nu_{x}}\right|^{2}-\frac{1}{2}\left|\nabla_{x}\left(M_{k} u_{k}\right)\right|^{2}\right) \sigma+\left(M_{k} u_{k}\right) \frac{\partial\left(M_{k} u_{k}\right)}{\partial \nu_{x}}\right\} \\
= & P\left(\sigma, h_{\bar{x}}\right) .
\end{aligned}$$
On the other hand, recall that
$$I_{k, 6}=\frac{\tau_{k}}{p_{k}+1} \int_{\{|x| \leq \sigma\} / \Gamma} K_{k} f_{k}^{-\tau_{k}} u_{k}^{p_{k}+1} .$$
It's clear that $I_{k, 6} \geq 0$, and $I_{k, 6}=0$ if $\tau_{k}=0$. Our proposition is proved. \(\square\)
4.3. Green Function. Assuming Condition 3.7, Corollary 3.12 tells us that $M_{k} u_{k} \rightarrow h_{\bar{x}}=a G(\cdot, \bar{x})$ in $C_{\text {loc }}^{2}\left(\left(B_{r}(\bar{x})-\{\bar{x}\}\right) / \Gamma\right)$. We are going to determine the constant $a$ and the regular part of $G(\cdot, \bar{x})$ evaluated at $\bar{x}$, where $G(\cdot, \bar{x})$ is the standard Green function for $L_{g}=\Delta_{g}-\frac{1}{6} R_{g}$ at the point $\bar{x}$, and $g$ is the limit metric, i.e. for any $C^{2}$ function $\phi$ and small $\sigma>0$,
$$\int_{\{|x| \leq \sigma\} / \Gamma} G\left(L_{g} \phi\right) d V_{g}=\phi(\bar{x}) .$$

Hence Corollary 3.12 implies that
$$\lim _{k \rightarrow \infty} \int_{\{|x| \leq \sigma\} / \Gamma}\left(M_{k} u_{k}\right)\left(L_{g_{k}} \phi\right) d V_{g_{k}}=a \phi(\bar{x})$$

Lemma 4.7. The constant a in Corollary 3.12 is
$$a=-\frac{4 \sqrt{2} \operatorname{Vol}\left(S^{3}\right)}{|\Gamma| \sqrt{K_{\infty}(\bar{x})}} .$$

Proof. Recall Remark 3.3 and the change of variables in (3.8), (3.9). For any $C^{2}$ function $\phi$, define $\tilde{\phi}(y)=\phi\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right)$. Integrating by parts, we obtain
$$\begin{aligned}
& \int_{\{|x| \leq \sigma\} / \Gamma}\left(M_{k} u_{k}\right)\left(L_{g_{k}} \phi\right) \\
= & \int_{\{|x| \leq \sigma\} / \Gamma}\left(\Delta_{x}-\frac{1}{6} R_{k}\right)\left(M_{k} u_{k}\right) \cdot \phi \\
= & M_{k}^{-2\left(p_{k}-1\right)} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left(M_{k}^{p_{k}-1} \Delta_{y}-\frac{1}{6} \tilde{R}\right)\left(M_{k}^{2} v_{k}\right) \cdot \tilde{\phi} \\
= & \left(M_{k}^{\tau_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left(\Delta_{y} v_{k}\right) \cdot \tilde{\phi}\right)-\left(\frac{1}{6} M_{k}^{4-2 p_{k}} \int_{\left\{|y| \leq M_{k}^{\frac{p_{k}-1}{2}} \sigma\right\} / \Gamma} \tilde{R}_{k} v_{k} \tilde{\phi}\right) .
\end{aligned}$$
Since $\lim _{k \rightarrow \infty} M_{k}^{4-2 p_{k}}=0$, the second integral vanishes when $k \rightarrow \infty$. Thus
$$\begin{aligned}
a \phi(\bar{x}) & =\lim _{\sigma \rightarrow 0} \lim _{k \rightarrow \infty} \int_{\{|x| \leq \sigma\} / \Gamma}\left(M_{k} u_{k}\right)\left(L_{g_{k}} \phi\right) \\
& =\lim _{\sigma \rightarrow 0} \lim _{k \rightarrow \infty} \int_{\left\{|y| \leq M_{k}^{\frac{2}{n-2}} \sigma\right\} / \Gamma}\left(\Delta_{y} v_{k}\right) \cdot \phi\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right) \\
& =\left(\int_{\mathbb{R}^{n} / \Gamma} \Delta_{y} U_{K_{\infty}(\bar{x})}(y) d y\right) \cdot \phi(\bar{x}),
\end{aligned}$$
where the last equality is by Proposition 3.4. Therefore the constant $a$ is
$$\begin{aligned}
a=\int_{\mathbb{R}^{n} / \Gamma} \Delta_{y} U_{K_{\infty}(\bar{x})}(y) d y & =-\int_{\mathbb{R}^{n} / \Gamma} K_{\infty}(\bar{x}) U_{K_{\infty}(\bar{x})}^{3}(y) d y \\
& =-\frac{16 \sqrt{2}}{\sqrt{K_{\infty}(\bar{x})}} \int_{\mathbb{R}^{n} / \Gamma}\left(1+|y|^{2}\right)^{-3} d y \\
& =-\frac{16 \sqrt{2} V o l\left(S^{3}\right)}{|\Gamma| \sqrt{K_{\infty}(\bar{x})}} \int_{0}^{\infty} r^{3}\left(1+r^{2}\right)^{-3} d r=-\frac{4 \sqrt{2} \operatorname{Vol}\left(S^{3}\right)}{|\Gamma| \sqrt{K_{\infty}(\bar{x})}} .
\end{aligned}$$ \(\square\)

On the other hand, recall that we assume for each $k, g_{k}$ is the conformal normal metric with conformal normal coordinates centered at point $x_{k}$, hence the limit metric $g$ is the conformal normal metric with conformal normal coordinates centered at point $\bar{x}$. Thus we have the following proposition.
Proposition 4.8. In $g$-conformal normal coordinates $\left\{x^{i}\right\}$ centered at $\bar{x}, G(\cdot, \bar{x})$ has the expansion
$$G(\cdot, \bar{x})=b \psi_{\bar{x}}=b\left[r^{-2}+A_{\bar{x}}+O(r)\right],$$
where $r=|x|, \psi_{\bar{x}}$ is from Definition 1.8, $A_{\bar{x}}$ is a constant, and
$$b=-\frac{|\Gamma|}{2 \operatorname{Vol}\left(S^{3}\right)} .$$

Proof. The proof is given by [LP87, Definition 6.2 and Lemma 6.4]. Note that our notation is different from [LP87]. Our point $\bar{x}$ is their point $P$; our operator $L_{g}$ is equal to -1/6 multiplied with their box operator $\square$; our $G(\cdot, \bar{x})$ is equal to -6 multiplied with their $\Gamma_{P}$, our $\psi_{\bar{x}}$ is their $G$. And the $\Gamma$ in our equation (4.63) is the quotient group near point $\bar{x}$. \(\square\)

Then we can relate the Pohozaev identity with the constant term $A_{\bar{x}}$.
Lemma 4.9. We have
$$\lim _{\sigma \rightarrow 0} P\left(\sigma, h_{\bar{x}}\right)=-\frac{16 \operatorname{Vol}\left(S^{3}\right)}{|\Gamma| K_{\infty}(\bar{x})} \cdot A_{\bar{x}} .$$
Proof. We will write $G$ instead of $G(\cdot, \bar{x})$. Using $h_{\bar{x}}=a G$, we have
$$P\left(\sigma, h_{\bar{x}}\right)=a^{2} \int_{\{|x|=\sigma\} / \Gamma}\left\{\left(\left|\frac{\partial G}{\partial \nu}\right|^{2}-\frac{1}{2}|\nabla G|^{2}\right) \sigma+G \frac{\partial G}{\partial \nu_{x}}\right\} .$$
By Proposition 4.8, on $|x|=\sigma$ for small $\sigma$,
$$G=b\left[\sigma^{-2}+A_{\bar{x}}+O(\sigma)\right], \quad\left|\frac{\partial G}{\partial \nu}\right|=b\left[-2 \sigma^{-3}+O(1)\right], \quad|\nabla G|=b\left[-2 \sigma^{-3}+O(1)\right] .$$
Then we have
$$\begin{aligned}
\left(\left|\frac{\partial G}{\partial \nu}\right|^{2}-\frac{1}{2}|\nabla G|^{2}\right) \sigma+G \frac{\partial G}{\partial \nu_{x}} & =b^{2}\left(\frac{\sigma}{2} \cdot\left[-2 \sigma^{-3}+O(1)\right]^{2}+\left[\sigma^{-2}+A_{\bar{x}}+O(\sigma)\right] \cdot\left[-2 \sigma^{-3}+O(1)\right]\right) \\
& =b^{2}\left(\frac{\sigma}{2} \cdot\left[4 \sigma^{-6}+O\left(\sigma^{-3}\right)\right]-2 \sigma^{-5}-2 A_{\bar{x}} \sigma^{-3}+O\left(\sigma^{-2}\right)\right) \\
& =-2 b^{2} A_{\bar{x}} \sigma^{-3}+O\left(\sigma^{-2}\right) .
\end{aligned}$$
Hence
$$P\left(\sigma, h_{\bar{x}}\right)=a^{2} \int_{\{|x|=\sigma\} / \Gamma}\left(-2 b^{2} A_{\bar{x}} \sigma^{-3}+O\left(\sigma^{-2}\right)\right)=-\frac{2 a^{2} b^{2} A_{\bar{x}} \cdot \operatorname{Vol}\left(S^{3}\right)}{|\Gamma|}+O(\sigma) .$$
Letting $\sigma \rightarrow 0$, using Lemma 4.7 and Proposition 4.8, we have
$$\begin{aligned}
\lim _{\sigma \rightarrow 0} P\left(\sigma, h_{\bar{x}}\right) & =-\frac{2 a^{2} b^{2} A_{\bar{x}} \cdot \operatorname{Vol}\left(S^{3}\right)}{|\Gamma|} \\
& =(-2) \cdot \frac{\operatorname{Vol}\left(S^{3}\right)}{|\Gamma|} \cdot \frac{32 \operatorname{Vol}\left(S^{3}\right)^{2}}{|\Gamma|^{2} K_{\infty}(\bar{x})} \cdot \frac{|\Gamma|^{2}}{4 \operatorname{Vol}\left(S^{3}\right)^{2}} \cdot A_{\bar{x}}=-\frac{16 \operatorname{Vol}\left(S^{3}\right)}{|\Gamma| K_{\infty}(\bar{x})} \cdot A_{\bar{x}} .
\end{aligned}$$ \(\square\)

Proposition 4.10. Assuming Condition 3.7, we have the following inequality
$$A_{\bar{x}} \leq-\frac{\Delta_{g} K_{\infty}(\bar{x})}{24 K_{\infty}(\bar{x})} .$$
Moreover, if $\tau_{k}=0$ for all $k$, we have the equality
$$A_{\bar{x}}=-\frac{\Delta_{g} K_{\infty}(\bar{x})}{24 K_{\infty}(\bar{x})} .$$
Here, $\Delta_{g}$ is the Laplacian with respect to the limit conformal normal metric $g$.
Proof. Assuming Condition 3.7, by Proposition 4.6, we have
$$\lim _{\sigma \rightarrow 0} P\left(\sigma, h_{\bar{x}}\right) \geq \frac{2 \Delta_{g} K_{\infty}(\bar{x}) \cdot \operatorname{Vol}\left(S^{3}\right)}{3|\Gamma| K_{\infty}(\bar{x})^{2}} .$$

By Lemma 4.10, we have
$$\lim _{\sigma \rightarrow 0} P\left(\sigma, h_{\bar{x}}\right)=-\frac{16 \operatorname{Vol}\left(S^{3}\right)}{|\Gamma| K_{\infty}(\bar{x})} \cdot A_{\bar{x}} .$$
Hence
$$A_{\bar{x}} \leq-\frac{2 \Delta_{g} K_{\infty}(\bar{x}) \cdot \operatorname{Vol}\left(S^{3}\right)}{3|\Gamma| K_{\infty}(\bar{x})^{2}} \cdot \frac{|\Gamma| K_{\infty}(\bar{x})}{16 \operatorname{Vol}\left(S^{3}\right)}=-\frac{\Delta_{g} K_{\infty}(\bar{x})}{24 K_{\infty}(\bar{x})} .$$
The case that $\tau_{k}=0$ for all $k$ follows similarly. \(\square\)

Moreover, by relating $A_{\bar{x}}$ with the mass, we can remove the assumption "conformal normal metric", as follows.

Proposition 4.11. Assuming Condition 3.7, let $g=\lim _{k \rightarrow \infty} g_{k}$ be the limit metric, but do not necessarily assume that $g_{k}, g$ are conformal normal metrics. Let $\hat{g}_{\bar{x}}=\psi_{\bar{x}}^{2} g$ be the conformal blow-up of $g$ at the point $\bar{x}$, as in Definition 1.8. We have the following inequality
$$m\left(\hat{g}_{\bar{x}}\right) \leq-\frac{\Delta_{g} K_{\infty}(\bar{x})}{2 K_{\infty}(\bar{x})} .$$
Moreover, if $\tau_{k}=0$ for all $k$, we have the equality
$$m\left(\hat{g}_{\bar{x}}\right)=-\frac{\Delta_{g} K_{\infty}(\bar{x})}{2 K_{\infty}(\bar{x})} .$$
Proof. For each $k$, let $r_{k}$ denote the $g_{k}$-distance function from the point $x_{k}$. Assume $\tilde{g}_{k}=\phi_{k}^{2} g_{k}$ is the conformal normal metric with conformal normal coordinates $\left\{\tilde{x}^{i}\right\}$ centered at point $x_{k}$. By [LP87, Theorem 5.6], after applying a dilation and a translation to the coordinates $\left\{\tilde{x}^{i}\right\}$, we may assume $\phi_{k}\left(x_{k}\right)=1$ and $\nabla \phi_{k}\left(x_{k}\right)=0$, in other words, for small $r_{k}, \phi_{k}=1+O\left(r_{k}^{2}\right)$. When $k \rightarrow 0$, we have that $\tilde{g}=\phi^{2} g$, where $g, \tilde{g}, \phi$ are the limit of $g_{k}, \tilde{g}_{k}, \phi_{k}$ as $k \rightarrow \infty$. Moreover, $\phi=1+O\left(r^{2}\right)$, where $r$ is the $g$-distance function from the point $\bar{x}$. Next, recall that the conformal transformation law of the Laplacian for $\tilde{g}=e^{2 \varphi} g$ is
$$\Delta_{\tilde{g}}=e^{-2 \varphi} \Delta_{g}+(n-2) e^{-2 \varphi} g^{i j} \frac{\partial \varphi}{\partial x_{j}} \frac{\partial}{\partial x_{i}} .$$
Thus, for any $f \in C^{2}$, we have $\Delta_{\tilde{g}} f(\bar{x})=\Delta_{g} f(\bar{x})$. Let $A_{\bar{x}}$ be the regular part corresponding to conformal blow-up of $\tilde{g}$ at point $\bar{x}$. Let $\hat{g}_{\bar{x}}$ be the conformal blow-up of $g$ at point $\bar{x}$. By LLP87, Lemma 9.7], we have
$$m\left(\hat{g}_{\bar{x}}\right)=12 A_{\bar{x}} .$$
Therefore, we know
$$\begin{aligned}
& m\left(\hat{g}_{\bar{x}}\right) \leq-\frac{\Delta_{g} K_{\infty}(\bar{x})}{2 K_{\infty}(\bar{x})} \Longleftrightarrow A_{\bar{x}} \leq-\frac{\Delta_{\tilde{g}} K_{\infty}(\bar{x})}{24 K_{\infty}(\bar{x})}, \\
& m\left(\hat{g}_{\bar{x}}\right)=-\frac{\Delta_{g} K_{\infty}(\bar{x})}{2 K_{\infty}(\bar{x})} \Longleftrightarrow A_{\bar{x}}=-\frac{\Delta_{\tilde{g}} K_{\infty}(\bar{x})}{24 K_{\infty}(\bar{x})},
\end{aligned}$$
which implies that this proposition is equivalent to Proposition 4.10. \(\square\)

\section*{5. Blow-up points must be isolated and simple}

In [LZ99], they proved that on a 3-dimensional compact manifold, all blow-up points for (3.5) must be isolated simple blow-up points. The same result in higher dimensions is proved by [KMS09], [LZ05], but only for constant prescribed scalar curvature. Here, we will modify their proofs to show that the same result holds on 4-dimensional compact orbifolds, for a sequence of variable prescribed scalar curvatures.

Let $(M, g)$ be a compact Riemannian 4-dimensional orbifold with singularities
$$\Sigma_{\Gamma}=\left\{\left(q_{1}, \Gamma_{1}\right), \cdots,\left(q_{l}, \Gamma_{l}\right)\right\}$$
and positive scalar curvature $R_{g}$. Assume $u$ is a positive $C^{2}$ solution of equation (3.1) on $M$, where $K$ is a positive $C^{2}$ function and $f$ is a positive $C^{1}$ function. For any point $\bar{x} \in M$, define $\Omega_{\bar{x}, \sigma}$ in the following:
a) if $\bar{x}$ is a smooth point, define $\Omega_{\bar{x}, \sigma}=B_{\sigma}(\bar{x})$ for some $\sigma>0$ such that its closure $\bar{\Omega}_{\bar{x}, \sigma}$ doesn't include any singular point. In other words, $d_{g}\left(\bar{x},\left\{q_{1}, \cdots, q_{l}\right\}\right)>\sigma$;
b) if $\bar{x}=q_{j}$ for some $1 \leq j \leq l$, choose $\sigma=\sigma_{j}$ where $\sigma_{j}$ is as defined in Definition 1.1. Then the neighborhood of $\bar{x}$ is a quotient ball $B_{\sigma}(\bar{x}) / \Gamma$. Define $\Omega_{\bar{x}, \sigma}=\pi_{j}^{*}\left(B_{\sigma}(\bar{x}) / \Gamma\right)$ to be the lifting-up space. Denote the lifting-up functions and metric still by $u, f, K$ and $g$.

First, let us recall a lemma from [LZ99].
Lemma 5.1 ([LZ99] Lemma 5.1). Let $(M, g), u, K, f, \Omega_{\bar{x}, \sigma}$ be as defined above. Given any small $\varepsilon>0$ and large $R^{\prime}>1$, there exists a large positive $C_{0}$, depending only on $M, g,\|f\|_{C^{1}(M)}$, $\inf _{M} K,\|K\|_{C^{2}(M)}, \varepsilon$ and $R^{\prime}$ such that for any compact $S \subset \bar{\Omega}_{\bar{x}, \sigma}$, if $u$ satisfies
$$\max _{x \in \bar{\Omega}_{\bar{x}, \sigma} \backslash S} d_{g}(x, S)^{\frac{2}{p-1}} u(x) \geq C_{0},$$
then we have $p>3-\varepsilon$ and for some local maximum point of $u$ in $\Omega_{\bar{x}, \sigma} \backslash S$, denoted as $x_{0}$,
$$\left\|u\left(x_{0}\right)^{-1} u\left(\exp _{x_{0}}\left(u\left(x_{0}\right)^{-\frac{p-1}{2}} x\right)\right)-U_{K\left(x_{0}\right)}(x)\right\|_{C^{2}\left(|x|<2 R^{\prime}\right)}<\varepsilon,$$
where $d_{g}(x, S)$ denotes the distance of $y$ to $S$, and $d_{g}(x, S)=1$ if $S=\emptyset$.
Proof. The case that $K$ is a positive constant and $\Omega_{\bar{x}, \sigma}$ is replaced by a compact 3-dimensional manifold $M$ is proved in [LZ99, Lemma 5.1]. As mentioned in [LZ99, Section 7], it can be generalized to the case $K$ is a variable function. With a straightforward modification, it can also be generalized to higher dimensions. Moreover, note that the statement and proof in [LZ99, Lemma 5.1] is just a local argument in $M \backslash S$. Thus their proof remains valid in our case by choosing their $S$ to be any compact subset of $M$ satisfying $M \backslash S \subset B_{\sigma}(\bar{x}) / \Gamma$, and considering the lifting-up of $M \backslash S$ if $\bar{x}$ is a singular point. \(\square\)

Using Lemma 5.1, we can prove the following.
Proposition 5.2 ([LZ99] Proposition 5.1). Let $(M, g), u, K, f, \Omega_{\bar{x}, \sigma}$ be as defined in the beginning of this section. Given small $\varepsilon>0$ and large $R^{\prime}$, there exist some positive constants $C_{0}$ and $C_{1}$ depending on $M, g,\|f\|_{C^{1}(M)}, \inf _{M} K,\|K\|_{C^{2}(M)}, \varepsilon$ and $R^{\prime}$ such that if
$$\max _{\Omega_{\bar{x}, \sigma}} u>C_{0},$$
then there exists some integer $N=N(u) \geq 1$ and $N$ local maximum points of $u$ denoted as $\left\{x_{1}, \cdots, x_{N}\right\} \subset \Omega_{\bar{x}, \sigma}$, such that:
1) $3-\varepsilon<p \leq 3$,
2) $\overline{B_{r_{i}}\left(x_{i}\right)} \cap \overline{B_{r_{j}}\left(x_{j}\right)}=\emptyset$ for $i \neq j$, where $r_{j}=R^{\prime} u\left(x_{j}\right)^{-\frac{p-1}{2}}$, and for each $j$,
$$\left\|u\left(x_{j}\right)^{-1} u\left(\exp _{x_{j}}\left(u\left(x_{j}\right)^{-\frac{p-1}{2}} x\right)\right)-U_{K\left(x_{j}\right)}(x)\right\|_{C^{2}\left(|x|<2 R^{\prime}\right)}<\varepsilon,$$
3) $d_{g}\left(x_{i}, x_{j}\right)^{\frac{2}{p-1}} u\left(x_{j}\right) \geq C_{0}$ for $j>i$, while $d_{g}\left(x,\left\{x_{1}, \cdots, x_{N}\right\}\right)^{\frac{2}{p-1}} u(x) \leq C_{1}$ for all $x \in \Omega_{\bar{x}, \sigma}$.

Proof. The case that $K$ is a positive constant and $\Omega_{\bar{x}, \sigma}$ is replaced by a compact 3-dimensional manifold $M$ is proved in [LZ99, Proposition 5.1]. Briefly, that proof was completed by an induction process as following: first apply [LZ99, Lemma 5.1] with $S=\emptyset$ to get the first local maximum
point of $u$, denoted by $x_{1}$; assuming we have already got local maximum points $\left\{x_{1}, \cdots, x_{l}\right\}$, apply [LZ99, Lemma 5.1] with $S=\cup_{j=1}^{l} \overline{B_{r_{j}}\left(x_{j}\right)}$ to get the next local maximum point. If the condition (5.2) is not satisfied in any step, the process stops. This process must stop after a finite number of times because each time $\int_{B_{r_{j}}\left(x_{j}\right)}|\nabla u|^{2}$ is greater than some positive universal constant and their sum $\sum_{j} \int_{B_{r_{j}}\left(x_{j}\right)}|\nabla u|^{2} \leq \int_{M}|\nabla u|^{2}$ which is finite. It is not hard to verify the set $\left\{x_{1}, \cdots, x_{N}\right\}$ constructed by the process satisfies all the above properties. In our case, we can continue the same process by inductively applying our Lemma 5.1 with $S$ as mentioned above. Everything follows the same way and our proposition is proved. \(\square\)

Next, we can rule out bubble accumulation.
Proposition 5.3. Let $(M, g), u, K, f, \Omega_{\bar{x}, \sigma}$ be as defined in the beginning of this section. Let $\varepsilon, R^{\prime}, C_{0}, C_{1}$ and $\left\{x_{1}, \cdots, x_{N}\right\}$ be as defined in Proposition 5.2. If $\varepsilon$ is sufficiently small and $R^{\prime}$ is sufficiently large, then there exists a positive constant $\bar{C}$, which only depends on $M, g,\|f\|_{C^{1}(M)}$, $\inf _{M} K,\|K\|_{C^{2}(M)}, \varepsilon$ and $R^{\prime}$, such that if $\max _{\Omega_{\bar{x}, \sigma}} u \geq C_{0}$, then $d_{g}\left(x_{j}, x_{l}\right) \geq \bar{C}$, for all $j \neq l$.

Proof. The proof is similar to [KMS09, Proposition 8.3] and [LZ99, Proposition 5.2]. We will prove it by contradiction. Suppose that such a constant $\bar{C}$ does not exist, then there exist sequences $p_{k} \rightarrow p \in(3-\varepsilon, 3]$ and $\left\{u_{k}\right\}$ with $\max _{\Omega_{\bar{x}, \sigma}} u_{k} \geq C_{0}$ and
$$\lim _{k \rightarrow \infty} \min _{j \neq l} d_{g}\left(x_{j}\left(u_{k}\right), x_{l}\left(u_{k}\right)\right)=0 .$$
Without loss of generality, assume that
$$\delta_{k}=d_{g}\left(x_{1}\left(u_{k}\right), x_{2}\left(u_{k}\right)\right)=\min _{j \neq l} d_{g}\left(x_{j}\left(u_{k}\right), x_{l}\left(u_{k}\right)\right) \rightarrow 0 \text { as } k \rightarrow \infty .$$
For each $k$, take normal coordinates $\left\{x^{i}\right\}$ centered at point $x_{1}\left(u_{k}\right)$ and consider change of variables $y=\delta_{k}^{-1} x$. Rescale $u_{k}$ by
$$v_{k}(y)=\delta_{k}^{\frac{2}{p_{k}-1}} u_{k}\left(\delta_{k} y\right), \quad \forall|y|<\delta_{k}^{-1} .$$
Then $v_{k}$ satisfies
$$L_{h_{k}} v_{k}+\tilde{K}_{k} \tilde{f}_{k}^{-\tau_{k}} v_{k}^{p_{k}}=0,$$
where $\left(h_{k}\right)_{i j}(y)=g_{i j}\left(\delta_{k} y\right), \tilde{K}_{k}(y)=K\left(\delta_{k} y\right)$ and $\tilde{f}_{k}(y)=f\left(\delta_{k} y\right)$. If $x_{j}\left(u_{k}\right) \in B_{\sqrt{\delta_{k}}}\left(x_{1}\right)$, denote by $y_{j}\left(u_{k}\right)=\delta_{k}^{-1} x_{j}\left(u_{k}\right)$ the $y$-coordinate of point $x_{j}\left(u_{k}\right)$. By the proof of [KMS09, Proposition 8.3], we have $y_{1}\left(u_{k}\right)=0, y_{2}\left(u_{k}\right) \rightarrow \bar{y}_{2}$ with $\left|\bar{y}_{2}\right|=1,\left\{0, \bar{y}_{2}\right\}$ are isolated simple blow-up points for $\left\{v_{k}\right\}$, and
$$v_{k}(0) v_{k}(y) \rightarrow a_{1}\left(|y|^{-2}+b_{1}+O(y)\right) \text { in } C_{l o c}^{2}\left(\mathbb{R}^{4}-S^{\prime}\right),$$
where $S^{\prime}$ denotes the set of blow-up points for $\left\{v_{k}\right\}$ and $a_{1}, b_{1}>0$ are some positive constants. On the other hand,
$$\begin{aligned}
\tilde{K}_{k}(y) & =K\left(\delta_{k} y\right) \rightarrow K(0) \text { in } C_{l o c}^{0} \text { norm }, \\
\left|\nabla_{y} \tilde{K}_{k}(y)\right| & =\delta_{k}\left|\nabla_{x} K\left(\delta_{k} y\right)\right| \rightarrow 0 \text { in } C^{0} \text { norm, }, \\
\left|\nabla_{y}^{2} \tilde{K}_{k}(y)\right| & =\delta_{k}^{2}\left|\nabla_{x}^{2} K\left(\delta_{k} y\right)\right| \rightarrow 0 \text { in } C^{0} \text { norm. }
\end{aligned}$$
Hence $\tilde{K}_{k}$ converges to the constant $K(0)$ in the $C_{\text {loc }}^{2}$ norm, where $K(0)$ by definition is the $K$ value at the limit point of $x_{1}\left(u_{k}\right)$ as $k \rightarrow \infty$, possibly by passing to a subsequence. Applying Proposition 4.10 to the blow-up sequence $\left\{v_{k}\right\}$, we get $b_{1} \leq 0$, which contradicts $b_{1}>0$. Therefore our proposition is proved. \(\square\)

Corollary 5.4. Let $(M, g)$ be a compact Riemannian 4-dimensional orbifold with positive scalar curvature. Suppose $\left\{f_{k}\right\}$ is a sequence of positive $C^{1}$ functions converging in the $C_{\text {loc }}^{1}$ topology to a positive function $f$. Also suppose $\left\{K_{k}\right\}$ is a sequence of positive $C^{2}$ functions converging in the $C_{\text {loc }}^{2}$ topology to a positive function $K_{\infty}$. Let $\left\{u_{k}\right\}$ be a sequence of positive solutions of equation (3.5) on $M$ with $g_{k}=g$ and $\max _{M} u_{k} \rightarrow \infty$. Then $p_{k} \rightarrow 3$ and the set of blow-up points is finite and consists only of isolated blow-up points. Moreover, if blow-up occurs at a singular point, i.e. $x_{k} \rightarrow \bar{x}$ and $u_{k}\left(x_{k}\right) \rightarrow \infty$ where $\bar{x}$ is a singular point, then there exists an integer $N \in \mathbb{N}^{*}$ such that for any $k>N, x_{k}=\bar{x}$.

Proof. By the assumption of $f_{k}$ and $K_{k}$, there exists a constant $C_{2}$ such that for large $k$,
$$\left\|f_{k}\right\|_{C^{1}(M)} \leq C_{2}\|f\|_{C^{1}(M)}, \quad \inf _{M} K_{k} \geq C_{2} \inf _{M} K_{\infty}, \quad\left\|K_{k}\right\|_{C^{2}(M)} \leq C_{2}\left\|K_{\infty}\right\|_{C^{2}(M)} .$$
By Proposition 5.3, in each $\Omega_{x, \sigma}$, blow-up points must be isolated blow-up points and the number $N\left(u_{k}\right)$ as defined in Proposition 5.2 must have an uniformly upper bound, otherwise, there cannot exist a constant $\bar{C}$ such that $d_{g}\left(x_{i}\left(u_{k}\right), x_{j}\left(u_{k}\right)\right) \geq \bar{C}$ for all $i \neq j$ and $k$. A compact orbifold can be covered by finitely many sufficiently small open balls, which gives us finitely many $\Omega_{x, \sigma}$ as defined in the beginning of this section. Therefore the set of blow-up points on $M$ is finite and consists only of isolated blow-up points.

Moreover, if blow-up occurs at a singular point, i.e. $x_{k} \rightarrow \bar{x}$ and $u_{k}\left(x_{k}\right) \rightarrow \infty$ where $\bar{x}$ is a singular point associated with a nontrivial quotient group $\Gamma$. Suppose there exists a subsequence, still denoted by $\left(u_{k}, x_{k}\right)$, such that $x_{k} \neq \bar{x}$ for any $k$. Consider the lifting-up space $\Omega_{\bar{x}, \sigma}$ as defined in the beginning of this section. Let $\tilde{x}_{k}^{(1)}, \cdots, \tilde{x}_{k}^{(|\Gamma|)}$ denote the lifting-up points of $x_{k}$. In the lifting-up space, it's clear that
$$d_{\tilde{g}}\left(\tilde{x}_{k}^{(1)}, \tilde{x}_{k}^{(2)}\right) \rightarrow 0 \text { as } k \rightarrow \infty,$$
which contradicts against Proposition 5.3. Thus our corollary is proved. \(\square\)

Given Corollary 5.4, we are able to conclude the following.
Proposition 5.5. Let $(M, g), f_{k}, K_{k}, g_{k}$ be as defined in Corollary 5.4. Assume $u_{k}$ is a sequence of positive functions satisfying equation (3.5) and $x_{k} \rightarrow \bar{x}$ is an isolated blow-up point. Then $\bar{x}$ is an isolated simple blow-up point for $\left\{u_{k}\right\}$.

Proof. The proof is similar to [KMS09, Lemma 8.2] and [LZ99, Proposition 4.1]. First, by Corollary 5.4, without loss of generality, we may assume $x_{k}=\bar{x}$ for all $k$ if $\bar{x}$ is a singular point. Suppose $\bar{x}$ is an isolated blow-up point, but not an isolated simple blow-up point. Let $x=\left\{x^{i}\right\}$ be normal coordinates centered at $x_{k}$ and define the rescaled function
$$v_{k}(y)=\tau_{k}^{\frac{2}{p_{k}-1}} u_{k}\left(\tau_{k} y\right), \quad \forall|y|<\tau_{k}^{-1} .$$
Then $v_{k}$ satisfies
$$L_{h_{k}} v_{k}+\tilde{K}_{k} \tilde{f}_{k}^{-\tau_{k}} v_{k}^{p_{k}}=0,$$
where $\left(h_{k}\right)_{i j}(y)=\left(g_{k}\right)_{i j}\left(\tau_{k} y\right), \tilde{K}_{k}(y)=K_{k}\left(\tau_{k} y\right)$ and $\tilde{f}_{k}(y)=f_{k}\left(\tau_{k} y\right)$. By the proof of KMS09, Lemma 8.2], the origin $y=0$ is an isolated simple blow-up point for $\left\{v_{k}\right\}$ and
$$v_{k}(0) v_{k}(y) \rightarrow h(y)=a_{2}\left(|y|^{-2}+b_{2}\right) \text { in } C_{l o c}^{2}\left(\left(\mathbb{R}^{4}-\{0\}\right) / \Gamma\right),$$
where $a_{2}=b_{2}=1$, where $\Gamma=\{e\}$ if $\bar{x}$ is a smooth point, but $\Gamma$ is the quotient group if $\bar{x}$ is a singular point.

On the other hand, because $K_{k}$ converges to $K_{\infty}$ in the $C_{\text {loc }}^{2}$ norm, we know
$$\begin{aligned}
\tilde{K}_{k}(y) & =K_{k}\left(\tau_{k} y\right) \rightarrow K_{\infty}(\bar{x}) \text { in } C_{l o c}^{0} \text { norm }, \\
\left|\nabla_{y} \tilde{K}_{k}(y)\right| & =\tau_{k}\left|\nabla_{x} K_{k}\left(\tau_{k} y\right)\right| \rightarrow 0 \text { in } C_{l o c}^{0} \text { norm }, \\
\left|\nabla_{y}^{2} \tilde{K}_{k}(y)\right| & =\tau_{k}^{2}\left|\nabla_{x}^{2} K_{k}\left(\tau_{k} y\right)\right| \rightarrow 0 \text { in } C_{l o c}^{0} \text { norm. }
\end{aligned}$$
Hence $\tilde{K}_{k}$ converges to the constant $K_{\infty}(\bar{x})$ in the $C_{\text {loc }}^{2}$ norm. Applying Proposition 4.10 to the blow-up sequence $\left\{v_{k}\right\}$, we obtain $b_{2} \leq 0$, which contradicts $b_{2}=1$. Therefore $\bar{x}$ is an isolated simple blow-up points for $\left\{u_{k}\right\}$. \(\square\)

Corollary 5.6. Let $(M, g), f_{k}, K_{k}, g_{k}$ be as defined in Corollary 5.4. Assume $u_{k}$ is a sequence of positive functions satisfying equation (3.5), then Condition 3.7 is a necessary condition for any blow-up point.

Proof. This follows immediately from combining Corollary 5.4 and Proposition 5.5. \(\square\)

Proof of Theorem 1.11. To prove the upper bound $u \leq C$ under assumption (1.10) in Theorem 1.11, suppose the contrary. Then there exist $p_{k} \rightarrow 3$ and $\left\{u_{k}\right\}$ satisfying
$$L_{g} u_{k}+K_{k} u_{k}^{p_{k}}=0,$$
with $\max _{M} u_{k} \rightarrow \infty$, where $\left\{K_{k}\right\}$ is a sequence of positive $C^{2}$ functions converging in the $C_{\text {loc }}^{2}$ topology to a positive function $K_{\infty}$. Let $x_{k}$ denote the point where $u_{k}$ obtains a maximum, after possibly passing to a subsequence, we may assume $x_{k} \rightarrow \bar{x}$ is a blow-up point. By Corollary 5.6, the sequence $\left(u_{k}, x_{k}\right)$ satisfies Condition 3.7, where $g_{k}$ in equation (3.5) is the metric conformal to $g$ with conformal normal coordinates centered at $x_{k}$. By Proposition 4.11, we know
$$m\left(\hat{g}_{\bar{x}}\right) \leq-\frac{\Delta_{g} K_{\infty}(\bar{x})}{2 K_{\infty}(\bar{x})},$$
which contradicts against assumption (1.10) in Theorem 1.11. Therefore we know that $u \leq C$ for $u$ and $C$ as stated in Theorem 1.11. Next, assume $u$ obtains $\sup _{M} u$ at a point $P$, then $\Delta u(P) \leq 0$. By (1.3), $u(P) \geq \sqrt{R_{g}(P) /(6 K(P))} \geq c_{0}$. By the Harnack inequality,
$$\inf _{M} u \geq\left(1 / c_{1}\right) u(P) \geq c_{0} / c_{1} \geq 1 / C,$$
for sufficiently large $C$. By standard elliptic estimates, we conclude that $\|u\|_{C^{2, \alpha}(M)} \leq C$. Furthermore, because for $p<3$, there always exist subcritical solutions for any $K$ (the proof on manifolds remains valid in the orbifold setting; see for example [ES86, LP87]). Take a sequence of subcritical solutions and let $p \rightarrow 3$, due to (1.9), they limit to a critical solution for $p=3$. Thus the second part of Theorem 1.11 is proved.

The first part of Theorem 1.11 can be proved similarly, by fixing $p_{k}=3$ in the above proof. \(\square\)

\section*{6. Variational methods}

Let $(M, g)$ be a compact Riemannian $n$-orbifold with singularities $\Sigma_{\Gamma}=\left\{\left(q_{1}, \Gamma_{1}\right), \cdots,\left(q_{l}, \Gamma_{l}\right)\right\}$ and positive scalar curvature $R_{g}$. Let $K$ be a positive smooth function on $M$. In this section, we will study equation (1.3) using a variational method. Consider the energy functional
$$J_{p}(u, K, M)=\frac{\int_{M}\left(|\nabla u|^{2}+c(n) R_{g} u^{2} d\right) V o l_{g}}{\left(\int_{M} K|u|^{p+1} d V o l_{g}\right)^{\frac{2}{p+1}}},$$
for $1<p \leq \frac{n+2}{n-2}$ and $u \in W^{1,2}(M)$. Define the minimal energy to be
$$E(p, K)=\inf _{u \in W^{1,2}(M)} J_{p}(u, K, M) .$$

Let $Q\left(S^{n}\right)$ denote the Sobolev quotient of $S^{n}$, which is also the minimal energy on $S^{n}$ for $K \equiv 1$, that is,
$$Q\left(S^{n}\right)=\inf _{\phi \in W^{1,2}\left(S^{n}\right)} J_{\frac{n+2}{n-2}}\left(\phi, 1, S^{n}\right)=\frac{n(n-2)}{4} \operatorname{Vol}\left(S^{n}\right)^{2 / n} .$$
The following theorem generalizes [ES86, Proposition 1.1] to the orbifold case, and also generalizes [Aku12, Theorem 3.1] from the case $K=$ constant to the case of variable $K$.

Theorem 6.1. Let $(M, g)$ be a compact Riemannian $n$-orbifold with positive scalar curvature and singularities $\Sigma_{\Gamma}=\left\{\left(q_{1}, \Gamma_{1}\right), \cdots,\left(q_{l}, \Gamma_{l}\right)\right\}$. Let $K$ be a positive smooth function on $M$. Define the modified maximum value of $K$
$$B_{K}:=\max \left\{\sup _{x \in M}\{K(x)\}, \max _{1 \leq i \leq l}\left\{\left|\Gamma_{i}\right|^{\frac{2}{n-2}} K\left(q_{i}\right)\right\}\right\} .$$
Then the following inequality always holds
$$\left(B_{K}\right)^{\frac{n-2}{n}} E\left(\frac{n+2}{n-2}, K\right) \leq Q\left(S^{n}\right) .$$
Furthermore, if
$$\left(B_{K}\right)^{\frac{n-2}{n}} E\left(\frac{n+2}{n-2}, K\right)<Q\left(S^{n}\right),$$
then there exists a positive smooth solution $u$ of (1.3) with $p=\frac{n+2}{n-2}$, such that
$$J_{\frac{n+2}{n-2}}(u, K, M)=E\left(\frac{n+2}{n-2}, K\right) .$$
Proof. We first prove the inequality (6.5). The quantity $B_{K}$ is attained at either a singular point or a smooth point. Consider any point $q$ with $|\Gamma|^{\frac{2}{n-2}} K(q)=B_{K}$, where $\Gamma$ is the orbifold group at $q$ if $q$ is a singular point, or $\Gamma=\{e\}$ if $q$ is a smooth point. Take a conformal mapping $g_{q}=u_{q}^{\frac{4}{n-2}} g$ such that $g_{q}$ is the conformal normal metric centered at the point $q$. Consider the Green function with the power series expansion
$$G_{q}=\frac{1}{4 n(n-1) \operatorname{Vol}\left(S^{n-1}\right)}\left(r_{q}^{2-n}+H_{q}\right),$$
where $r_{q}$ is the geodesic distance from $q$ based on the metric $g_{q}$ and $H_{q}$ is the higher order term. Take a family of test functions
$$\varphi_{q, \lambda}=u_{q} \cdot\left(\frac{\lambda}{1+\lambda^{2}\left(r_{q}^{2-n}+H_{q}\right)^{\frac{2}{2-n}}}\right)^{\frac{n-2}{2}},$$
where $\lambda>0$. By [MM21, Proposition 5.1], we have the estimation
$$J_{\frac{n+2}{n-2}}\left(\varphi_{q, \lambda}, K, M\right)=\frac{c(n) \hat{c}_{0}}{|\Gamma|^{\frac{2}{n}} K(q)^{\frac{n-2}{n}}}+O\left(1 / \lambda^{2}\right),$$
where
$$\hat{c}_{0}=4 n(n-1)\left(\int_{\mathbb{R}^{n}} \frac{d x}{\left(1+r^{2}\right)^{n}}\right)^{\frac{2}{n}} .$$
Note that our functional $J_{\frac{n+2}{n-2}}$ is equal to $c(n)$ multiplied with the functional $J$ defined in [MM21, Chapter 1]. If $q$ is an orbifold point, we estimate integrals in $J_{\frac{n+2}{n-2}}$ by lifting everything up to the
universal cover near the orbifold point $q$. Therefore, compared to [MM21, Proposition 5.1], our estimation (6.10) has an extra factor of $c(n) /|\Gamma|^{\frac{2}{n}}$. By a direct computation, we know that
$$c(n) \hat{c}_{0}=Q\left(S^{n}\right) .$$
Clearly, we have
$$E\left(\frac{n+2}{n-2}, K\right) \leq \lim _{\lambda \rightarrow \infty} J_{\frac{n+2}{n-2}}\left(\varphi_{q, \lambda}, K, M\right)=\frac{Q\left(S^{n}\right)}{|\Gamma|^{\frac{2}{n}} K(q)^{\frac{n-2}{n}}} .$$
By our assumption, we have $|\Gamma|^{\frac{2}{n}} K(q)^{\frac{n-2}{n}}=B_{K}^{\frac{n-2}{n}}$, hence (6.5) is proved.
We next show that the strict inequality (6.6) implies the existence result. The proof is a modification of [Aku12, Theorem 3.1]. If we have proved the case that $M$ has only one singularity, the more general cases can be proved by an induction on the number of singularity points. Hence we may assume $M$ has only one singularity $(q, \Gamma)$. Let $X=M-\{q\}$. Note that
$$E\left(\frac{n+2}{n-2}, K\right)=\inf _{u \in C_{c}^{\infty}(X)} J_{\frac{n+2}{n-2}}(u, K, X) .$$
Let $B_{\rho}$ denote the open geodesic ball centered at $q$ of radius $\rho$. Define
$$Y_{k} \equiv \inf _{u \in C_{c}^{\infty}\left(X \backslash \overline{B_{1 / k}}\right)} J_{\frac{n+2}{n-2}}\left(u, K, X \backslash \overline{B_{1 / k}}\right),$$
for $k \in \mathbb{N}^{*}$. It follows that
$$Y_{k} \geq Y_{k+1} \geq Y_{k+2} \geq \cdots, \text { and } \lim _{k \rightarrow \infty} Y_{k}=E\left(\frac{n+2}{n-2}, K\right) .$$
By (6.6), there exists a large integer $k_{0}$, such that
$$\left(B_{K}\right)^{\frac{n-2}{n}} Y_{k}<Q\left(S^{n}\right) \text { for any } k \geq k_{0} .$$
Due to (6.4), it implies
$$\left(\sup _{x \in X \backslash B_{1 / k}}\{K(x)\}\right)^{\frac{n-2}{n}} Y_{k}<Q\left(S^{n}\right) \text { for any } k \geq k_{0} .$$
Note that on the manifold with boundary $(N, \partial N)=\left(X-B_{1 / k}, \partial B_{1 / k}\right)$, when we apply integration by parts to any function in $C_{c}^{\infty}\left(X \backslash \overline{B_{1 / k}}\right)$, the boundary integral term always vanishes. As a result, the variational method used in [ES86, Proposition 1.1] remains valid here. Thus, (6.18) implies that for each $k \geq k_{0}$, there exists a non-negative $J_{\frac{n+2}{n-2}}\left(\cdot, K, X \backslash \overline{B_{1 / k}}\right)$-minimizer $u_{k} \in C^{\infty}\left(X-B_{1 / k}\right)$, such that
$$\begin{aligned}
& J_{\frac{n+2}{n-2}}\left(u_{k}, K, X \backslash \overline{B_{1 / k}}\right)=Y_{k}, \quad \int_{X \backslash \overline{B_{1 / k}}} K u_{k}^{\frac{2 n}{n-2}} d V o l_{g}=1, \\
& u_{k}=0 \text { on } \partial B_{1 / k} \text { and } u_{k}>0 \text { in } X \backslash \overline{B_{1 / k}} .
\end{aligned}$$
Denote the zero extension of each $u_{k}$ to $M$ by also the same symbol $u_{k}$. Suppose the sequence $\left\{u_{k}\right\}$ has a uniform $C^{0}$-bound, i.e., there exists a constant $C>0$ such that $\left\|u_{k}\right\|_{C^{0}(M)} \leq C$ for $k \geq k_{0}$, then there exists a non-negative $J_{\frac{n+2}{n-2}}(\cdot, K, M)$-minimizer $u \in W^{1,2}(M)$ with $\|u\|_{C^{0}(M)} \leq C$, such that
$$u_{k} \rightarrow u \text { weakly in } W^{1,2}(M), \quad u_{k} \rightarrow u \text { strongly in } L^{2}(M) .$$
By (6.19), Lebesgue's bounded convergence theorem, and the above uniform $C^{0}$-bound, we have
$$\int_{M} K u^{\frac{2 n}{n-2}} d V o l_{g}=1,$$
which further implies
$$u_{k} \rightarrow u \text { strongly in } W^{1,2}(M) .$$
By the standard elliptic estimate, we obtain that $u \in C^{\infty}(M)$. The maximum principle implies that $u>0$ everywhere on $M$; see for example [Aub98b, Proposition 3.75].

To complete the proof, it is sufficient to show a uniform $C^{0}$-bound for the sequence $\left\{u_{k}\right\}$. For each $k$, take the absolute maximum point $x_{k} \in X$ of $u_{k}$ and denote $M_{k} \equiv u_{k}\left(x_{k}\right)$. Taking a subsequence if necessary, there exists a point $\bar{x} \in M$ such that
$$\lim _{k \rightarrow \infty} x_{k}=\bar{x} .$$
Suppose that there is not a uniform $C^{0}$-bound for $\left\{u_{k}\right\}$, that is $\lim _{k \rightarrow \infty} M_{k}=\infty$. There will be two cases.

Case 1: $\bar{x}=q$ (blow-up occurs at the singular point). In this case, we consider the universal cover of a small neighborhood around $q$. Let $\left\{\tilde{x}_{k}\right\}$ be a sequence of lifting-up points of $\left\{x_{k}\right\}$ in the same branch of the lifting-up space. Let $\tilde{u}_{k}, \tilde{K}$ denote the lifting-up functions of $u_{k}, K$, respectively. In the lifting-up space, for each $k$, let $\left\{\tilde{x}^{i}\right\}$ be a normal coordinate system in a small ball $B_{\sigma}\left(\tilde{x}_{k}\right)$ centered at each $\tilde{x}_{k}$. Consider the change of variables $\tilde{y}=M_{k}^{\frac{2}{n-2}} \tilde{x}$ and define the rescaled function $\tilde{v}_{k}(\tilde{y})=M_{k}^{-1} \cdot \tilde{u}_{k}\left(M_{k}^{-\frac{2}{n-2}} \tilde{y}\right)$. By Theorem 2.1 of Chapter 5 in [SY94],
$$\tilde{v}_{k} \rightarrow \tilde{v} \text { in } C_{l o c}^{2}\left(\mathbb{R}^{n}\right),$$
where $\tilde{v}$ satisfies the equation
$$-\Delta_{0} \tilde{v}=E\left(\frac{n+2}{n-2}, K\right) K(q) \tilde{v}^{\frac{n+2}{n-2}} \text { on } \mathbb{R}^{n} .$$
Note that
$$\int_{\mathbb{R}^{n}} K(q) \tilde{v}(y)^{\frac{2 n}{n-2}} d y=\lim _{r \rightarrow \infty} \int_{|\tilde{y}| \leq r} K(q) \tilde{v}(\tilde{y})^{\frac{2 n}{n-2}} d \tilde{y}$$
For each $r>0$, by (6.25) and changing variables, we have
$$\begin{aligned}
\int_{|\tilde{y}| \leq r} K(q) \tilde{v}(\tilde{y})^{\frac{2 n}{n-2}} d \tilde{y} & =\lim _{k \rightarrow \infty} \int_{|\tilde{y}| \leq r} \tilde{K}\left(M_{k}^{-\frac{2}{n-2}} \tilde{y}\right) \tilde{v}_{k}(\tilde{y})^{\frac{2 n}{n-2}} d \tilde{y} \\
& =\lim _{k \rightarrow \infty} \int_{|\tilde{x}| \leq M_{k}^{-\frac{2}{n-2}} r} \tilde{K}(\tilde{x}) \tilde{u}_{k}(\tilde{x})^{\frac{2 n}{n-2}} d \tilde{x} \\
& \leq|\Gamma| \cdot \lim _{k \rightarrow \infty} \int_{M} K u_{k}^{\frac{2 n}{n-2}} d V o l_{g}=|\Gamma|
\end{aligned}$$
which implies
$$\int_{\mathbb{R}^{n}} \tilde{v}^{\frac{2 n}{n-2}} \leq|\Gamma| K(q)^{-1} .$$
Multiplying $\tilde{v}$ with (6.26) and integrating by parts, we obtain
$$\int_{\mathbb{R}^{n}}|\nabla \tilde{v}|^{2}=E\left(\frac{n+2}{n-2}, K\right) K(q) \cdot \int_{\mathbb{R}^{n}} \tilde{v}^{\frac{2 n}{n-2}} .$$
Together with (6.29), we have
$$\begin{aligned}
Q\left(S^{n}\right) & \leq J_{\frac{n+2}{n-2}}\left(\tilde{v}, 1, \mathbb{R}^{n}\right)=\frac{\int_{\mathbb{R}^{n}}|\nabla \tilde{v}|^{2}}{\left(\int_{\mathbb{R}^{n}} \tilde{v}^{\frac{2 n}{n-2}}\right)^{\frac{n-2}{n}}} \\
& =E\left(\frac{n+2}{n-2}, K\right) K(q) \cdot\left(\int_{\mathbb{R}^{n}} \tilde{v}^{\frac{2 n}{n-2}}\right)^{\frac{2}{n}} \leq E\left(\frac{n+2}{n-2}, K\right)\left[|\Gamma|^{\frac{2}{n-2}} K(q)\right]^{\frac{n-2}{n}} .
\end{aligned}$$

Note that $q$ is a singular point on $M$, so $|\Gamma|^{\frac{2}{n-2}} K(q) \leq B_{K}$, which leads to a contradiction against (6.6).

Case 2: $\bar{x} \neq q$ (blow-up occurs at a smooth point). The argument is identical to Case 1 with $|\Gamma|=1$. Hence
$$E\left(\frac{n+2}{n-2}, K\right) K(\bar{x})^{\frac{n-2}{n}} \geq Q\left(S^{n}\right) .$$
Since $\bar{x}$ is a smooth point on $M, K(\bar{x}) \leq B_{K}$, which again leads to a contradiction against (6.6). □
Proof of Theorem 1.13. The proof will be based on Theorem 6.1 and [MM21, Proposition 5.1]. Under the assumptions of Theorem 1.13, we simply denote the singular point $\left(q_{i_{0}}, \Gamma_{i_{0}}\right)$ by $(q, \Gamma)$. Let $\varphi_{q, \lambda}$ be as defined in (6.9). By [MM21, Proposition 5.1] and (6.12), we have the estimation
$$J_{\frac{n+2}{n-2}}\left(\varphi_{q, \lambda}, K, M\right)=\frac{Q\left(S^{n}\right)}{|\Gamma|^{\frac{2}{n}} K(q)^{\frac{n-2}{n}}}\left(1-\hat{c}_{2} \frac{\Delta K(q)}{K(q) \lambda^{2}}-\hat{d}_{1}\left(\begin{array}{ll}
\frac{H_{q}+O\left(\frac{\log \lambda}{\lambda^{2}}\right)}{\lambda^{2}} & \text { for } n=4 \\
\frac{H_{q}}{\lambda_{q}^{3}} \log \lambda & \text { for } n=5 \\
\frac{\hat{\gamma}^{4}}{0} & \text { for } n \geq 6
\end{array}\right)\right)$$
up to error $O\left(1 / \lambda^{4}\right)$ for large $\lambda$, where ${ }^{1}$
$$\hat{c}_{2}=\frac{\int_{\mathbb{R}^{n}} \frac{r^{2} d x}{\left(1+r^{2}\right)^{n}}}{2 n \int_{\mathbb{R}^{n}} \frac{d x}{\left(1+r^{2}\right)^{n}}} \quad \text { and } \quad \hat{d}_{1}=\frac{2 n \int_{\mathbb{R}^{n}} \frac{r^{n} d x}{\left(1+r^{2}\right)^{n+1}}}{(n-2) \int_{\mathbb{R}^{n}} \frac{d x}{\left(1+r^{2}\right)^{n}}} .$$
Moreover, in dimension 4, $\hat{c}_{2}=1 / 4$ and $\hat{d}_{1}=6$. Then, it is clear that under the following assumptions
$$\begin{cases}H_{q}+\frac{\Delta_{g} K(q)}{24 K(q)}>0, & \text { for } n=4, \\ \Delta_{g} K(q)>0, & \text { for } n \geq 5,\end{cases}$$
by choosing sufficiently large $\lambda$, we can get
$$J_{\frac{n+2}{n-2}}\left(\varphi_{q, \lambda}, K, M\right)<\frac{Q\left(S^{n}\right)}{|\Gamma|^{\frac{2}{n}} K(q)^{\frac{n-2}{n}}} .$$
Note that we have $B_{K}=|\Gamma|^{\frac{2}{n-2}} K(q)$ under the assumption of Theorem 1.13, hence the above inequality implies
$$\left(B_{K}\right)^{\frac{n-2}{n}} E\left(\frac{n+2}{n-2}, K\right)<Q\left(S^{n}\right) .$$
By Theorem 6.1, there exists a postive smooth solution of equation (1.3). Moreover, by (4.78), we know that condition (1.12) is equivalent to condition (6.35) in dimension 4. \(\square\)

\section*{7. LeBrun metrics}

Recall the LeBrun metric $\left(\mathcal{O}_{\mathbb{P}^{1}}(-n), g_{L E B(n)}\right)$ in $\hat{r}$-coordinates and its conformal compactification $\left(\check{\mathcal{O}}_{\mathbb{P}^{1}}(-n), \check{g}_{L E B(n)}\right)$ from Section 1.4. On $\check{\mathcal{O}}_{\mathbb{P}^{1}}(-n)$, define $s=1 / \hat{r}$ to be the inverted radial coordinate centered at the orbifold point $\check{q}$. Then
$$\begin{aligned}
\check{g}_{L E B(n)} & =\frac{1+s^{2}}{\left(1+n s^{2}\right)^{3}} d s^{2}+\frac{s^{2}\left(s^{2}+1\right)}{\left(n s^{2}+1\right)^{2}}\left[\sigma_{1}^{2}+\sigma_{2}^{2}+\frac{\left(1+n s^{2}\right)}{\left(1+s^{2}\right)^{2}} \sigma_{3}^{2}\right] \\
& =d s^{2}+s^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\sigma_{3}^{2}\right)+O\left(s^{2}\right) \quad \text { as } s \rightarrow 0 .
\end{aligned}$$

\footnotetext{
${ }^{1}$ The constant factor $\frac{2 n}{n-2}$ was missing when the authors computed $\hat{d}_{1}$ in [MM21, Proposition 5.1]. We've corrected the mistake here.
}

Hence we may choose normal coordinates $\left\{x^{i}\right\}$ centered at $\check{q}$ such that $s=|x|+O\left(|x|^{3}\right)$. Also note that $g_{L E B(n)}=\left(n+\hat{r}^{2}\right)^{2} \cdot \check{g}_{L E B(n)}=\left(s^{-2}+n\right)^{2} \cdot \check{g}_{L E B(n)}$ is scalar-flat, hence $g_{L E B(n)}$ is the conformal blow-up of $\check{g}_{L E B(n)}$ at the point $\check{q}$, as in Definition 1.8. We will next study
$$\Delta_{\check{g}_{L E B(n)}} u-\frac{1}{6} R_{\check{g}_{L E B(n)}} u=-K u^{p}, \quad 1<p \leq 3 .$$
In the $U(2)$-invariant case, Theorem 1.11 specializes to the following.
Proposition 7.1. Let $\mathcal{X}_{n}, \mathcal{X}_{n,+}, \mathcal{X}_{n, 0}$ and $\mathcal{X}_{n,-}$ be as defined in (1.22) and (1.24). On the orbifold $\left(\check{\mathcal{O}}_{\mathbb{P}^{1}}(-n), \check{g}_{L E B(n)}\right)$, for any $K \in \mathcal{X}_{n,+} \cup \mathcal{X}_{n,-}$, there exists some constant $C$, depending only on $\inf K$ and $\|K\|_{C^{2}}$, such that
$$1 / C \leq u \leq C \text { and }\|u\|_{C^{2, \alpha}} \leq C,$$
for all $U(2)$-invariant solutions $u \in \mathcal{X}_{n}$ of (7.3) with $p=3$, where $0<\alpha<1$. Moreover, if $K \in \mathcal{X}_{n,+}$, then (7.4) holds for all $1<1+\varepsilon<p \leq 3$, where $C$ in addition depends on $\varepsilon$. Consequently, in this case there exists a $U(2)$-invariant solution $u$ of (7.3) with $p=3$.

Proof. Assume $\left\{u_{k}\right\} \subset \mathcal{X}_{n}$ is a family of U(2)-invariant solutions of (7.3) with corresponding exponents $p_{k} \rightarrow 3$ as $k \rightarrow \infty$. Assume $u_{k}$ blows up at a point $\bar{x}$ when $k \rightarrow \infty$. Suppose $\bar{x}$ is in the set $\left\{s=s_{0}\right\}$ for some $s_{0}>0$. Because $u_{k}$ is U(2)-invariant, $u_{k}$ blows up on the entire set $\left\{s=s_{0}\right\}$, which is either a hypersurface if $s_{0}<\infty$ or the $\mathbb{C P}^{1}$ component if $s_{0}=\infty$. However, either case is impossible, because Proposition 5.3 implies that blow-up points are isolated. Therefore, $u_{k}$ must blow up at the orbifold point $\check{q}$. It is clear that if $K \in \mathcal{X}_{n,+}$ implies (1.10), and $K \in \mathcal{X}_{n,-}$ implies (1.8). By the proof and statement of Theorem 1.11, this proposition is proved. \(\square\)

If $u(s)$ satisfies equation (1.23), then $u^{2} g_{\check{g}_{L E B(n)}}$ has scalar curvature $6 K(s)$. This latter condition is equivalent to $v^{2} g_{g_{L E B(n)}}$ having scalar curvature $6 K(s)$, where
$$v(s) \equiv \frac{u(s)}{n+1 / s^{2}},$$
which is equivalent to
$$\Delta_{g_{L E B(n)}} v=-K v^{3} .$$
Define another function space
$$\mathcal{Y}_{n}=\left\{h(s):(0, \infty) \rightarrow \mathbb{R}_{+} \left\lvert\, h(s)=\frac{f(s)}{n+1 / s^{2}}\right., f(s) \in \mathcal{X}_{n}\right\} .$$
There is an obvious bijection between the solution set of equation (1.23) in $\mathcal{X}_{n}$ and the solution set of equation (7.6) in $\mathcal{Y}_{n}$.

Proposition 7.2. On $\left(\mathcal{O}_{\mathbb{P}^{1}}(-2), g_{L E B(2)}\right)$, assume $K(s) \in \mathcal{X}_{2}$ satisfies
$$K^{\prime}(s) \leq 0 \text { for any } s \geq 0,$$
then there is no solution in $\mathcal{Y}_{2}$ that solves (7.6). Consequently, there is no solution in $\mathcal{X}_{2}$ that solves (1.23).

Proof. Suppose $v(s) \in \mathcal{Y}_{2}$ solves equation (7.6). It implies that $\check{g}=v^{2} g_{L E B(2)}$ is a compact orbifold metric with $R_{\check{g}}=6 K(s)$, and it has an orbifold point $\check{q}$ at $s=0$. Denote this orbifold by $\check{M}$. Define $\hat{v}(\hat{r})=v(1 / \hat{r})$ and $\hat{K}(\hat{r})=K(1 / \hat{r})$. Then in the $\hat{r}$-coordinate, we have
$$\frac{n+3 \hat{r}^{2}}{\hat{r}\left(1+\hat{r}^{2}\right)} \hat{v}^{\prime}(\hat{r})+\frac{n+\hat{r}^{2}}{1+\hat{r}^{2}} \hat{v}^{\prime \prime}(\hat{r})=-\hat{K}(\hat{r}) \hat{v}(\hat{r})^{3} .$$

Denote the left hand side of the above equation by LHS. We observe that
$$\text { LHS } \leq 0 \text { and } \mathrm{LHS}=\frac{\left[\left(n \hat{r}+\hat{r}^{3}\right) \hat{v}^{\prime}(\hat{r})\right]^{\prime}}{\hat{r}\left(1+\hat{r}^{2}\right)} .$$
It follows that
$$\left[\left(n \hat{r}+\hat{r}^{3}\right) \hat{v}^{\prime}(\hat{r})\right]^{\prime} \leq 0,$$
which implies that
$$\left(n \hat{r}+\hat{r}^{3}\right) \hat{v}^{\prime}(\hat{r}) \leq 0 .$$
Thus $\hat{v}^{\prime}(\hat{r}) \leq 0$ for any $\hat{r} \geq 0$, which implies that
$$v^{\prime}(s) \geq 0, \text { for any } s \geq 0 .$$
Similar to the proof of [Via10, Theorem 1.3], letting $E$ denote the traceless Ricci tensor, by the conformal transformation formula for $E$ and the fact that $g_{L E B(2)}$ is Ricci-flat, we have
$$E_{\check{g}}=v^{-1}\left(-2 \nabla^{2} v+(\Delta v / 2) \check{g}\right),$$
where ∇ and $\Delta$ are respect to metric $\check{g}$. Using the argument of [Oba72], integrating $v\left|E_{\check{g}}\right|^{2}$ on $\check{M}$, we obtain
$$\begin{aligned}
\int_{\check{M}} v\left|E_{\check{g}}\right|^{2} d V o l_{\check{g}} & =\int_{\check{M}} v E_{\check{g}}^{i j}\left\{v^{-1}\left(-2 \nabla^{2} v+(\Delta v / 2) \check{g}\right)_{i j}\right\} d V o l_{\check{g}} \\
& =-2 \int_{\check{M}} E_{\check{g}}^{i j}\left(\nabla^{2} v\right)_{i j} d V o l_{\check{g}} \\
& =-2 \lim _{\varepsilon \rightarrow 0} \int_{\check{M} \backslash B_{\varepsilon}(\check{q})} E_{\check{g}}^{i j}\left(\nabla^{2} v\right)_{i j} d V o l_{\check{g}},
\end{aligned}$$
where $B_{\varepsilon}(\check{q})$ denotes the geodesic ball centered at $\check{q}$ with radius $\varepsilon$, and the indices $i=0,1,2,3$ denote the directions $d s, \sigma_{1}, \sigma_{2}, \sigma_{3}$ in the moving coframe. Integrating by parts, we have
$$\int_{\check{M}} v\left|E_{\check{g}}\right|^{2} d V o l_{\check{g}}=-2 \lim _{\varepsilon \rightarrow 0}\left(\int_{\partial B_{\varepsilon}(\check{q})} E_{\check{g}}^{i j}(\nabla v)_{i} \nu_{j} d \sigma_{\check{g}}-\int_{\check{M} \backslash B_{\varepsilon}(\check{q})} \nabla_{j} E_{\check{g}}^{i j} \cdot(\nabla v)_{i} d V o l_{\check{g}}\right) .$$
By (7.5), it is clear that $v(s)=O\left(s^{2}\right)$ near $s=0$. Also because the curvature and volume term for $\check{g}$ are bounded near $s=0$, the first integral term on the right hand side goes to zero as $\varepsilon \rightarrow 0$. For the second integral term on the right hand side, since $v(s)$ is a radial function, the only nonvanishing component of $(\nabla v)_{i}$ is $(\nabla v)_{0}=v^{\prime}(s)$ along the $\partial / \partial s$ direction. On the other hand, by the Bianchi identity,
$$\nabla_{j} E_{\check{g}}^{i j}=\nabla_{j}\left(R i c_{\check{g}}^{i j}-\frac{1}{4} R_{\check{g}} \cdot \check{g}^{i j}\right)=\frac{1}{2} \nabla^{i} R_{\check{g}}-\frac{1}{4} \nabla^{i} R_{\check{g}}=\frac{3}{2} \nabla^{i} K .$$
Since $K(s)$ is a radial function, the only nonvanishing component of $(\nabla K)^{i}$ is $(\nabla K)^{0}=K^{\prime}(s)$ along the $d s$ direction. Hence
$$\nabla_{j} E_{\check{g}}^{i j}= \begin{cases}\frac{3}{2} K^{\prime}(s), & i=0, \\ 0, & i=1,2,3 .\end{cases}$$
It follows
$$\int_{\check{M}} v\left|E_{\check{g}}\right|^{2} d V o l_{\check{g}}=\lim _{\varepsilon \rightarrow 0} \int_{\varepsilon}^{\infty} C(s) K^{\prime}(s) v^{\prime}(s) d s,$$
where $C(s)$ is a positive function in $s$, depending on the volume term of $\check{g}$ at each $s$. By (7.8) and (7.13), we know
$$\lim _{\varepsilon \rightarrow 0} \int_{\varepsilon}^{\infty} C(s) K^{\prime}(s) v^{\prime}(s) d s \leq 0$$
hence
$$\int_{\check{M}} v\left|E_{\check{g}}\right|^{2} d V o l_{\check{g}} \leq 0,$$
which implies $E_{\check{g}}=0$. By (7.18), we know $K^{\prime}(s) \equiv 0$, so that $K=$ constant. By [Via10, Theorem 1.3], such a solution $v$ does not exist. \(\square\)

For each $n$, we define another radial coordinate by
$$t(\hat{r})=\log \left(\frac{n+\hat{r}^{2}}{\hat{r}^{2}}\right) \text { and its inverse } \hat{r}(t)=\sqrt{\frac{n}{e^{t}-1}} \text {. }$$
Hence
$$t(s)=\log \left(n s^{2}+1\right) \text { and } s(t)=\sqrt{\frac{e^{t}-1}{n}} .$$
We have defined three radial coordinates $\hat{r}, s, t \in[0, \infty]$. It is not hard to see that $1 / \hat{r}, s$ and $t$ are monotonic to each other. By basic computations, on the ALE manifold $\mathcal{O}_{\mathbb{P}^{1}}(-n)$, we have
$$\Delta_{g_{L E B(n)}}=\frac{n+3 \hat{r}^{2}}{\hat{r}\left(1+\hat{r}^{2}\right)} \frac{\partial}{\partial \hat{r}}+\frac{n+\hat{r}^{2}}{1+\hat{r}^{2}} \frac{\partial^{2}}{\partial \hat{r}^{2}}=\frac{4\left(1-e^{-t}\right)^{3}}{e^{-t}\left(1+(n-1) e^{-t}\right)} \frac{\partial^{2}}{\partial t^{2}} .$$
Next, we prove the following non-existence result.
Theorem 7.3. For any $n \in \mathbb{N}^{*}$, on $\left(\check{\mathcal{O}}_{\mathbb{P}^{1}}(-n), \check{g}_{L E B(n)}\right)$, there is no solution in $\mathcal{X}_{n}$ for equation (1.23) with
$$K=K_{n,-}(s)=\frac{2+n s^{2}}{n+n s^{2}} K_{2,-}(s),$$
where $K_{2,-}(s) \in \mathcal{X}_{n}$ is any monotonically decreasing function in $s$. Moreover, we know
$$K=K_{n,-}(s) \in \mathcal{X}_{n,-} \text { if } K_{2,-}^{\prime \prime}(0)<0 .$$
In particular, for $n \geq 2$, it implies that there is no $U(2)$-invariant solution for the Yamabe Problem $K=$ constant.

Proof. For such a $K=K_{n,-}(s)$, suppose there is a $u_{n}(s) \in \mathcal{X}_{n}$ that solves equation (1.23), then $v_{n}(s)=u_{n}(s) /\left(n+s^{-2}\right) \in \mathcal{Y}_{n}$ solves equation (7.6). Define
$$\bar{v}_{n}(t)=v_{n}\left(\sqrt{\frac{e^{t}-1}{n}}\right), \quad \bar{K}_{n,-}(t)=K_{n,-}\left(\sqrt{\frac{e^{t}-1}{n}}\right) .$$
By (7.23) and (7.24), we know (7.6) is equivalent to the following equation
$$\bar{v}_{n}^{\prime \prime}(t)=-\bar{K}_{n,-}(t) \cdot \frac{e^{-t}\left(1+(n-1) e^{-t}\right)}{4\left(1-e^{-t}\right)^{3}} \bar{v}_{n}(t)^{3} .$$
It implies
$$\bar{v}_{n}^{\prime \prime}(t)=-\frac{\left(1+(n-1) e^{-t}\right) \bar{K}_{n,-}(t)}{1+e^{-t}} \cdot \frac{e^{-t}\left(1+e^{-t}\right)}{4\left(1-e^{-t}\right)^{3}} \bar{v}_{n}(t)^{3} .$$
Define
$$\bar{K}_{2,-}(t)=\frac{\left(1+(n-1) e^{-t}\right) \bar{K}_{n,-}(t)}{1+e^{-t}},$$
then (7.29) becomes
$$\bar{v}_{n}^{\prime \prime}(t)=-\bar{K}_{2,-}(t) \cdot \frac{e^{-t}\left(1+e^{-t}\right)}{4\left(1-e^{-t}\right)^{3}} \bar{v}_{n}(t)^{3},$$
which can be viewed as (7.6) on $\left(\mathcal{O}_{\mathbb{P}^{1}}(-2), g_{L E B(2)}\right)$ in the $t$-coordinate, with $K=\bar{K}_{2,-}(t)$ and $v=\bar{v}_{n}(t)$. To transform $\bar{v}_{n}(t)$ and $\bar{K}_{2,-}(t)$ back to $s$-coordinate on $\mathcal{O}_{\mathbb{P}^{1}}(-2)$, using (7.23) with $n=2$, we define
$$v_{2}(s)=\bar{v}_{n}\left(\log \left(2 s^{2}+1\right)\right) \text { and } K_{2}(s)=\bar{K}_{2,-}\left(\log \left(2 s^{2}+1\right)\right) .$$
Thus we know that on $\mathcal{O}_{\mathbb{P}^{1}}(-2), v_{2}(s) \in \mathcal{Y}_{2}$ solves (7.6) with $K=K_{2}(s) \in \mathcal{X}_{2}$. By combining (7.25), (7.27) and (7.30), it is not hard to see that
$$K_{2}(s)=\frac{n+2 s^{2}}{2+2 s^{2}} \bar{K}_{n,-}\left(\log \left(2 s^{2}+1\right)\right)=\frac{n+2 s^{2}}{2+2 s^{2}} K_{n,-}\left(\sqrt{\frac{2}{n}} s\right)=K_{2,-}\left(\sqrt{\frac{2}{n}} s\right) .$$
Our assumption that $K_{2,-}(s)$ is a monotonically decreasing function in $s$ implies $K_{2}^{\prime}(s) \leq 0$ for all $s$, which leads to a contradiction against Proposition 7.2.

For the last part, assume $K(s) \in \mathcal{X}_{n}$. Near $s=0, K$ has a power series expansion
$$K(s)=K(0)+\frac{1}{2} K^{\prime \prime}(0) s^{2}+O\left(s^{4}\right) .$$
By (4.77) and (7.2),
$$\Delta_{\check{g}_{L E B(n)}} K(0)=\Delta_{g_{\mathbb{R}^{4} / \Gamma_{n}}} K(0)=K^{\prime \prime}(0)+\left.\frac{3}{s} K^{\prime}(s)\right|_{s=0}=4 K^{\prime \prime}(0) .$$
So, $K_{n,-}(s) \in \mathcal{X}_{n,-}$ is equivalent to
$$\frac{K_{n,-}^{\prime \prime}(0)}{K_{n,-}(0)}<n-2 .$$
If $K_{2,-}^{\prime \prime}(0)<0$, then we have
$$\frac{K_{n,-}^{\prime \prime}(0)}{K_{n,-}(0)}=\left.\frac{\frac{d^{2}}{d s^{2}}\left(\frac{2+n s^{2}}{n+n s^{2}} K_{2,-}(s)\right)}{\frac{2+n s^{2}}{n+n s^{2}} K_{2,-}(s)}\right|_{s=0}=n-2+\frac{K_{2,-}^{\prime \prime}(0)}{K_{2,-}(0)}<n-2 .$$
It follows $K_{n,-}(s) \in \mathcal{X}_{n,-}$. \(\square\)

Proof of Theorem 1.18. By Proposition 7.1, and homotopy invariance of the Leray-Schauder degree, $\operatorname{deg}\left(F_{p, K, n}, \Omega_{\Lambda, n}, 0\right)$ is equal to a constant in either case (1) or (2) in Theorem 1.18. For any $n \in \mathbb{N}^{*}$, Theorem 7.3 implies that
$$\operatorname{deg}\left(F_{3, K, n}, \Omega_{\Lambda, n}, 0\right)=0,$$
for $K \in \mathcal{X}_{n,-}$ satisfying the assumptions of Theorem 7.3. Homotopy invariance implies that the degree is zero for any $K \in \mathcal{X}_{n,-}$, which proves (2) of Theorem 1.18. Part (1) of Theorem 1.18 is proved by a standard subcritical degree counting argument; see [Sch91]. \(\square\)

\section*{References}
\begin{itemize}
\item[] [AB03] K. Akutagawa and B. Botvinnik, Yamabe metrics on cylindrical manifolds, Geom. Funct. Anal. 13 (2003), no. 2, 259-333.
\item[] [AB04] Kazuo Akutagawa and Boris Botvinnik, The Yamabe invariants of orbifolds and cylindrical manifolds, and $L^{2}$-harmonic spinors, J. Reine Angew. Math. 574 (2004), 121-146.
\item[] [ACM14] Kazuo Akutagawa, Gilles Carron, and Rafe Mazzeo, The Yamabe problem on stratified spaces, Geom. Funct. Anal. 24 (2014), no. 4, 1039-1079.
\item[] [ACM19] \_\_\_\_, The Yamabe problem on Dirichlet spaces, Tsinghua lectures in mathematics, Adv. Lect. Math. (ALM), vol. 45, Int. Press, Somerville, MA, 2019, pp. 101-122.
\item[] [Aku12] Kazuo Akutagawa, Computations of the orbifold Yamabe invariant, Math. Z. 271 (2012), no. 3-4, 611-625.
\item[] [Aub98a] Thierry Aubin, Some nonlinear problems in Riemannian geometry, Springer-Verlag, Berlin, 1998.
\item[] [Aub98b] \_\_\_\_, Some nonlinear problems in Riemannian geometry, Springer Monographs in Mathematics, Springer-Verlag, Berlin, 1998.
\end{itemize}
\begin{itemize}
\item[] [BAA08] Mohamed Ben Ayed and Mohameden Ould Ahmedou, Multiplicity results for the prescribed scalar curvature on low spheres, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 7 (2008), no. 4, 609-634.
\item[] [BACCH96] Mohamed Ben Ayed, Yansong Chen, Hichem Chtioui, and Mokhles Hammami, On the prescribed scalar curvature problem on 4-manifolds, Duke Math. J. 84 (1996), no. 3, 633-677.
\item[] [Bar86] Robert Bartnik, The mass of an asymptotically flat manifold, Comm. Pure Appl. Math. 39 (1986), no. 5, 661-693.
\item[] [Bor92] Joseph Ernest Borzellino, Riemannian geometry of orbifolds, ProQuest LLC, Ann Arbor, MI, 1992, Thesis (Ph.D.)-University of California, Los Angeles.
\item[] [CGS89] Luis A. Caffarelli, Basilis Gidas, and Joel Spruck, Asymptotic symmetry and local behavior of semilinear elliptic equations with critical Sobolev growth, Comm. Pure Appl. Math. 42 (1989), no. 3, 271-297.
\item[] [CGY93] Sun-Yung A. Chang, Matthew J. Gursky, and Paul C. Yang, The scalar curvature equation on 2- and 3-spheres, Calc. Var. Partial Differential Equations 1 (1993), no. 2, 205-229.
\item[] [CL01] Chiun-Chuan Chen and Chang-Shou Lin, Prescribing scalar curvature on $S^{N}$. I. A priori estimates, J. Differential Geom. 57 (2001), no. 1, 67-171.
\item[] [CLV21] Gilles Carron, Jørgen Olsen Lye, and Boris Vertman, Convergence of the Yamabe flow on singular spaces with positive Yamabe constant, arXiv.org:2106.01799, 2021.
\item[] [DL16] Michael G. Dabkowski and Michael T. Lock, On Kähler conformal compactifications of $U(n)$-invariant ALE spaces, Ann. Global Anal. Geom. 49 (2016), no. 1, 73-85.
\item[] [Dru03] Olivier Druet, From one bubble to several bubbles: the low-dimensional case, J. Differential Geom. 63 (2003), no. 3, 399-473.
\item[] [ES86] José F. Escobar and Richard M. Schoen, Conformal metrics with prescribed scalar curvature, Invent. Math. 86 (1986), no. 2, 243-254.
\item[] [Hab00] Lutz Habermann, Riemannian metrics of constant mass and moduli spaces of conformal structures, Lecture Notes in Mathematics, vol. 1743, Springer-Verlag, Berlin, 2000.
\item[] [HL16] Hans-Joachim Hein and Claude LeBrun, Mass in Kähler geometry, Comm. Math. Phys. 347 (2016), no. 1, 183-221.
\item[] [HM20] Sven Hirsch and Pengzi Miao, A positive mass theorem for manifolds with boundary, Pacific J. Math. 306 (2020), no. 1, 185-201.
\item[] [KMS09] M. A. Khuri, F. C. Marques, and R. M. Schoen, A compactness theorem for the Yamabe problem, J. Differential Geom. 81 (2009), no. 1, 143-196.
\item[] [LeB88] Claude LeBrun, Counter-examples to the generalized positive action conjecture, Comm. Math. Phys. 118 (1988), no. 4, 591-596.
\item[] [Li95] Yanyan Li, Prescribing scalar curvature on $S^{n}$ and related problems. I, J. Differential Equations 120 (1995), no. 2, 319-410.
\item[] [Li96] \_\_\_\_, Prescribing scalar curvature on $S^{n}$ and related problems. II. Existence and compactness, Comm. Pure Appl. Math. 49 (1996), no. 6, 541-597.
\item[] [LP87] John M. Lee and Thomas H. Parker, The Yamabe problem, Bull. Amer. Math. Soc. (N.S.) 17 (1987), no. 1, 37-91.
\item[] [LZ99] Yanyan Li and Meijun Zhu, Yamabe type equations on three-dimensional Riemannian manifolds, Commun. Contemp. Math. 1 (1999), no. 1, 1-50.
\item[] [LZ05] Yanyan Li and Lei Zhang, Compactness of solutions to the Yamabe problem. II, Calc. Var. Partial Differential Equations 24 (2005), no. 2, 185-237.
\item[] [LZ14] Man Chun Leung and Feng Zhou, Prescribed scalar curvature equation on $S^{n}$ in the presence of reflection or rotation symmetry, Proc. Amer. Math. Soc. 142 (2014), no. 5, 1607-1619.
\item[] [Mal02] Andrea Malchiodi, The scalar curvature problem on $S^{n}$ : an approach via Morse theory, Calc. Var. Partial Differential Equations 14 (2002), no. 4, 429-445.
\item[] [Mar05] Fernando Coda Marques, A priori estimates for the Yamabe problem in the non-locally conformally flat case, J. Differential Geom. 71 (2005), no. 2, 315-346.
\item[] [May17] Martin Mayer, A scalar curvature flow in low dimensions, Calc. Var. Partial Differential Equations 56 (2017), no. 2, Paper No. 24, 41.
\item[] [MM20] Andrea Malchiodi and Martin Mayer, Prescribing Morse scalar curvatures: subcritical blowing-up solutions, J. Differential Equations 268 (2020), no. 5, 2089-2124.
\item[] [MM21] \_\_\_\_, Prescribing Morse Scalar Curvatures: Blow-Up Analysis, Int. Math. Res. Not. IMRN (2021), no. 18, 14123-14203.
\item[] [Mon17] Ilaria Mondello, The local Yamabe constant of Einstein stratified spaces, Ann. Inst. H. Poincaré Anal. Non Linéaire 34 (2017), no. 1, 249-275.
\item[] [Mon18] \_\_\_\_, An Obata singular theorem for stratified spaces, Trans. Amer. Math. Soc. 370 (2018), no. 6, 4147-4175.
\end{itemize}
\begin{itemize}
\item[] [MV20] Peyman Morteza and Jeff A. Viaclovsky, The Calabi metric and desingularization of Einstein orbifolds, J. Eur. Math. Soc. (JEMS) 22 (2020), no. 4, 1201-1245.
\item[] [Nak90] Hiraku Nakajima, Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem, Recent topics in differential and analytic geometry, Adv. Stud. Pure Math., vol. 18, Academic Press, Boston, MA, 1990, pp. 385-396.
\item[] [Oba72] Morio Obata, The conjectures on conformal transformations of Riemannian manifolds, J. Differential Geometry 6 (1971/72), 247-258.
\item[] [Sch84] Richard M. Schoen, Conformal deformation of a Riemannian metric to constant scalar curvature, J. Differential Geom. 20 (1984), no. 2, 479-495.
\item[] [Sch89a] \_\_\_\_, Courses at Courant Institute and Stanford University, 1989.
\item[] [Sch89b] \_\_\_\_, Variational theory for the total scalar curvature functional for Riemannian metrics and related topics, Topics in calculus of variations (Montecatini Terme, 1987), Lecture Notes in Math., vol. 1365, Springer, Berlin, 1989, pp. 120-154.
\item[] [Sch91] \_\_\_\_, On the number of constant scalar curvature metrics in a conformal class, Differential geometry, Pitman Monogr. Surveys Pure Appl. Math., vol. 52, Longman Sci. Tech., Harlow, 1991, pp. 311-320.
\item[] [SY79] Richard M. Schoen and Shing-Tung Yau, On the proof of the positive mass conjecture in general relativity, Comm. Math. Phys. 65 (1979), no. 1, 45-76.
\item[] [SY81] \_\_\_\_, Proof of the positive mass theorem. II, Comm. Math. Phys. 79 (1981), no. 2, 231-260.
\item[] [SY94] R. Schoen and S.-T. Yau, Lectures on differential geometry, Conference Proceedings and Lecture Notes in Geometry and Topology, I, International Press, Cambridge, MA, 1994.
\item[] [SY17] Richard M. Schoen and Shing-Tung Yau, Positive scalar curvature and minimal hypersurface singularities, arXiv.org:1704.05490, 2017.
\item[] [SZ96] Richard M. Schoen and Dong Zhang, Prescribed scalar curvature on the $n$-sphere, Calc. Var. Partial Differential Equations 4 (1996), no. 1, 1-25.
\item[] [Via10] Jeff A. Viaclovsky, Monopole metrics and the orbifold Yamabe problem, Ann. Inst. Fourier (Grenoble) 60 (2010), no. 7, 2503-2543 (2011).
\item[] [Via13] \_\_\_\_, Einstein metrics and Yamabe invariants of weighted projective spaces, Tohoku Math. J. (2) 65 (2013), no. 2, 297-311.
\item[] [Yam60] Hidehiko Yamabe, On a deformation of Riemannian structures on compact manifolds, Osaka Math. J. 12 (1960), 21-37.
\end{itemize}

Department of Mathematics, University of California, Irvine, CA 92697
Email address: jut1@uci.edu, jviaclov@uci.edu
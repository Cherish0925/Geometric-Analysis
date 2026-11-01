---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Einstein deformations of Kähler Einstein metrics]

Lemma 4.16. Assume that $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$. We have
$$-\left\langle\nabla_{\delta^{g}(H J)}^{g} h, h J\right\rangle_{L^{2}}=\left\langle\delta^{\star g}\left(\left(2 \delta^{g}+\frac{1}{2} \mathrm{~d} \operatorname{tr}\right) h^{2}-2 h \delta^{g} h\right), H\right\rangle_{L^{2}}-2\left\langle\bar{\partial} h, \delta^{g} H \wedge h\right\rangle_{L^{2}}$$
for all $H \in \Gamma\left(\operatorname{Sym}^{2,+} T M\right)$.
Proof. Letting $X:=\delta^{g} H$ we have $\delta^{g}(H J)=J X$ and $-\left\langle\nabla_{\delta^{g}(H J)}^{g} h, h J\right\rangle_{L^{2}}=\left\langle\nabla_{J X}^{g}(h J), h\right\rangle_{L^{2}}$. We compute
$$\begin{aligned}
\left\langle\nabla_{J X}^{g}(h J), h\right\rangle_{L^{2}} & =\left\langle\left(\nabla_{J X}^{g} h\right) J e_{i}, h e_{i}\right\rangle_{L^{2}} \\
& =\left\langle\left(\nabla_{J X}^{g} h\right) J e_{i}-\left(\nabla_{X}^{g} h\right) e_{i}, h e_{i}\right\rangle_{L^{2}}+\left\langle\left(\nabla_{X}^{g} h\right) e_{i}, h e_{i}\right\rangle_{L^{2}} \\
& =\left\langle\left(\nabla_{J e_{i}}^{g} h\right) J X-\left(\nabla_{e_{i}}^{g} h\right) X, h e_{i}\right\rangle_{L^{2}}+2\left\langle\bar{\partial} h\left(e_{i}, X\right), h e_{i}\right\rangle_{L^{2}}+\frac{1}{2} \mathscr{L}_{X} \operatorname{tr}\left(h^{2}\right)
\end{aligned}$$
by essentially taking into account the symmetry property in (22). Since $h$ is symmetric and $J$-anti-invariant we have $\left\langle\left(\nabla_{J e_{i}}^{g} h\right) J X-\left(\nabla_{e_{i}}^{g} h\right) X, h e_{i}\right\rangle_{L^{2}}=-2\left\langle X,\left(\nabla_{e_{i}}^{g} h\right) h e_{i}\right\rangle_{L^{2}}$. Furthermore $-\left(\nabla_{e_{i}}^{g} h\right) h e_{i}=-\left(\nabla_{e_{i}}^{g} h^{2}\right) e_{i}+h\left(\nabla_{e_{i}}^{g} h\right) e_{i}=\delta^{g} h^{2}-h \delta^{g} h$. Summarising, we have showed that $\left\langle\nabla_{J X}^{g}(h J), h\right\rangle_{L^{2}}=\left\langle X, 2 \delta^{g} h^{2}-2 h \delta^{g} h+\frac{1}{2} \mathrm{~d} \operatorname{tr} h^{2}\right\rangle_{L^{2}}-2\left\langle\bar{\partial} h, \delta^{g} H \wedge h\right\rangle_{L^{2}}$ after also taking into that $\left\langle\bar{\partial} h, \delta^{g} H \wedge h\right\rangle_{L^{2}}=-\left\langle\bar{\partial} h\left(e_{i}, X\right), h e_{i}\right\rangle_{L^{2}}$. The claim follows now by integration by parts. \(\square\)

Yet another preliminary fact which will be needed is
pl-4
Lemma 4.17. Letting $h$ belong to $\Gamma\left(\mathrm{Sym}^{2,-} T M\right)$ we have
$$\left\langle\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right\rangle_{L^{2}}=-\left\langle\nabla_{\delta^{g}(H J)}^{g} h, h J\right\rangle_{L^{2}}+2 g\left(\stackrel{\circ}{R}\left(h^{2}\right), H\right)$$
whenever $H$ belongs to $\Gamma\left(\operatorname{Sym}^{2,+} T M\right)$.
Proof. We first observe that
$$\left.g\left(\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right)=-g\left(\nabla_{A e_{j}}^{g} h\right) e_{i},\left(\nabla_{e_{j}}^{g} h\right) J e_{i}\right)=-g\left(\nabla_{A e_{j}}^{g} h, \nabla_{e_{j}}^{g}(h J)\right)$$
where the skew symmetric tensor $A:=H J$. The rest of the proof is by integration by parts as follows. Consider the 1-form $\alpha$ on $M$ given by $\alpha(X)=g\left(\nabla_{A X}^{g} h, h J\right)$; its divergence reads
$$-\mathrm{d}^{\star g} \alpha=g\left(\left(\nabla^{g}\right)_{e_{i}, A e_{i}}^{2} h, h J\right)-g\left(\nabla_{\delta^{g} A}^{g} h, h J\right)+g\left(\nabla_{A e_{j}}^{g} h, \nabla_{e_{j}}^{g}(h J)\right) .$$
In addition, since $A$ is skew-symmetric, using the Ricci identity shows that
$$\begin{aligned}
g\left(\left(\nabla^{g}\right)_{e_{i}, A e_{i}}^{2} h, h J\right) & =\frac{1}{2} g\left(\left(\nabla^{g}\right)_{e_{i}, A e_{i}}^{2} h-\left(\nabla^{g}\right)_{A e_{i}, e_{i}}^{2} h, h J\right) \\
& =-\frac{1}{2} g\left(\left[R^{g}\left(e_{i}, A e_{i}\right), h\right], h J\right)=2 g\left(\stackrel{\circ}{R} H, h^{2}\right)=2 g\left(\stackrel{\circ}{R}\left(h^{2}\right), H\right),
\end{aligned}$$
after also taking into account that $R^{g}\left(e_{i}, A e_{i}\right)=2 J \AA h$ and that $\stackrel{\circ}{R}$ is a symmetric operator. Integration over $M$ then yields $\left\langle\nabla_{A e_{j}}^{g} h, \nabla_{e_{j}}^{g}(h J)\right\rangle_{L^{2}}=\left\langle\nabla_{\delta^{g} A}^{g} h, h J\right\rangle_{L^{2}}-2 g\left(\stackrel{\circ}{R}\left(h^{2}\right), H\right)$ and the claim follows. \(\square\)

One last technical step which is subsequently needed is contained in the following
bdd
Lemma 4.18. Assume that the pair $(h, H)$ belongs to $\Gamma\left(\operatorname{Sym}^{2,-} T M\right) \oplus \Gamma\left(\operatorname{Sym}^{2,+} T M\right)$. Then
$$\left\langle\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right\rangle_{L^{2}}=-\langle H \sharp \bar{\partial} h, \bar{\partial} h\rangle_{L^{2}}+\left\langle\frac{1}{4}\left\{h, \widetilde{\Delta}_{E}^{-} h\right\}-\frac{1}{4}\left[h, \mathrm{~d}^{-} \delta^{g} h\right]-\delta^{g}(h \circ \bar{\partial} h), H\right\rangle_{L^{2}} .$$

Proof. Start from $\left.\left.\left\langle\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right)\right\rangle_{L^{2}}=\left\langle\bar{\partial} h\left(e_{i}, H e_{j}\right), \mathrm{d}_{\nabla^{g}} h\left(e_{j}, e_{i}\right)+\left(\nabla_{e_{i}}^{g} h\right) e_{j}\right)\right\rangle_{L^{2}}$. The first summand reads
$$\begin{aligned}
\left\langle\bar{\partial} h\left(e_{i}, H e_{j}\right), \mathrm{d}_{\nabla^{g}} h\left(e_{j}, e_{i}\right)\right\rangle_{L^{2}} & =-\frac{1}{2}\left\langle(H \sharp \bar{\partial} h)\left(e_{i}, e_{j}\right), \mathrm{d}_{\nabla^{g}} h\left(e_{j}, e_{i}\right)\right\rangle_{L^{2}} \\
& =-\left\langle H \sharp \bar{\partial} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}=-\langle H \sharp \bar{\partial} h, \bar{\partial} h\rangle_{L^{2}} .
\end{aligned}$$

In the last step we have used that the tensor $H \sharp \bar{\partial} h$ belongs to $\lambda^{2}(M, T M)$, as entailed by having $H J=J H$. Since $H$ is symmetric,
$$\begin{aligned}
\left\langle\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{e_{i}}^{g} h\right) e_{j}\right\rangle_{L^{2}} & =\left\langle\bar{\partial} h\left(e_{i}, e_{j}\right),\left(\nabla_{e_{i}}^{g} h\right) H e_{j}\right\rangle_{L^{2}} \\
& =\left\langle\bar{\partial} h\left(e_{i}, e_{j}\right), \nabla_{e_{i}}^{g}(h \circ H) e_{j}-h\left(\nabla_{e_{i}}^{g} H\right) e_{j}\right\rangle_{L^{2}} \\
& =\left\langle\bar{\partial} h\left(e_{i}, e_{j}\right), \nabla_{e_{i}}^{g}(h \circ H) e_{j}\right\rangle_{L^{2}}-\left\langle h \circ \bar{\partial} h\left(e_{i}, e_{j}\right),\left(\nabla_{e_{i}}^{g} H\right) e_{j}\right\rangle_{L^{2}} \\
& =\left\langle\delta^{g} \bar{\partial} h, h \circ H\right\rangle_{L^{2}}-\left\langle h \circ \bar{\partial} h, \mathrm{~d}_{\nabla^{g}} H\right\rangle_{L^{2}}
\end{aligned}$$
after also integrating by parts. In addition, by using the Weitzenböck-type formula in Corollary 4.3 and that $h \circ H=\frac{1}{2}\{h, H\}+\frac{1}{2}[h, H]$ we obtain that
$$\begin{aligned}
\left\langle\delta^{g} \bar{\partial} h, h \circ H\right\rangle_{L^{2}} & =\left\langle\frac{1}{2} \Delta_{E} h-\delta^{\star_{g},-} \delta^{g} h-\frac{1}{2} \mathrm{~d}^{-} \delta^{g} h, h \circ H\right\rangle_{L^{2}} \\
& =\frac{1}{2}\left\langle\left\{h, \frac{1}{2} \Delta_{E} h-\delta^{\star_{g},-} \delta^{g} h\right\}, H\right\rangle_{L^{2}}-\frac{1}{4}\left\langle\left[h, \mathrm{~d}^{-} \delta^{g} h\right], H\right\rangle_{L^{2}} .
\end{aligned}$$
The claim follows now by gathering terms. \(\square\)

We define the operator $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right) \mapsto \mathbf{D} h \in \Gamma\left(\operatorname{Sym}^{2,+} T M\right)$ according to
$$\mathbf{D} h:=\left\{\stackrel{\circ}{R} h+\delta^{\star_{g},-} \delta^{g} h, h\right\}-\left(\frac{1}{2} \Delta_{E}-\stackrel{\circ}{R}\right) h^{2}+\delta^{\star_{g},+}\left(\left(2 \delta^{g} h^{2}+\frac{1}{2} \mathrm{~d} \operatorname{tr} h^{2}\right)-2 h \delta^{g} h\right)+\frac{1}{2}\left[h, \mathrm{~d}^{-} \delta^{g} h\right] .$$
To render computations easier to follow it is sometimes convenient to isolate the terms containing $\delta^{g} h$ by splitting $\mathbf{D}(h)=\mathbf{D}_{1}(h)+\operatorname{div}_{1}(h, h)$ where
$$\begin{aligned}
\mathbf{D}_{1}(h) & :=\{\stackrel{\mathrm{R}}{R} h, h\}-\left(\frac{1}{2} \Delta_{E}-\stackrel{\circ}{R}\right) h^{2}+\delta^{\star_{g},+}\left(2 \delta^{g} h^{2}+\frac{1}{2} \mathrm{~d} \operatorname{tr} h^{2}\right) \\
\operatorname{div}_{1}(h, h) & :=\left\{\delta^{\star_{g},-} \delta^{g} h, h\right\}-2 \delta^{\star_{g},+}\left(h \delta^{g} h\right)+\frac{1}{2}\left[h, \mathrm{~d}^{-} \delta^{g} h\right] .
\end{aligned}$$
Based on the preliminary material thus developed we may prove the main result in this section which reads as follows.
type-I Proposition 4.19. Let $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$. Then
$$\begin{aligned}
\left\langle H \sharp \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}} & =\langle\mathbf{D} h, H\rangle_{L^{2}}+2\langle H \sharp \bar{\partial} h, \bar{\partial} h\rangle_{L^{2}}+2\left\langle\delta^{g}(h \circ \bar{\partial} h), H\right\rangle_{L^{2}} \\
& -2\left\langle\bar{\partial} h, \delta^{g} H \wedge h\right\rangle_{L^{2}}
\end{aligned}$$
whenever $H$ belongs to $\Gamma\left(\operatorname{Sym}^{2,+} T M\right)$.

Proof. We first record that, after expanding in a local orthonormal frame $\left\{e_{i}\right\}$ on $M$, we have $g\left(H \sharp \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} h\right)=\frac{1}{2} g\left(\mathrm{~d}_{\nabla^{g}} h\left(H e_{i}, e_{j}\right)+\mathrm{d}_{\nabla^{g}} h\left(e_{i}, H e_{j}\right), \mathrm{d}_{\nabla^{g}} h\left(e_{i}, e_{j}\right)\right)=g\left(\mathrm{~d}_{\nabla^{g}} h\left(e_{i}, H e_{j}\right), \mathrm{d}_{\nabla^{g}} h\left(e_{i}, e_{j}\right)\right)$.

According to the definition of $\mathrm{d}_{\nabla^{g}}$ we compute
$$\begin{aligned}
g\left(\mathrm{~d}_{\nabla^{g}} h\left(e_{i}, H e_{j}\right), \mathrm{d}_{\nabla^{g}} h\left(e_{i}, e_{j}\right)\right) & =g\left(\left(\nabla_{e_{i}}^{g} h\right) H e_{j}-\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{e_{i}}^{g} h\right) e_{j}-\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) \\
& =g(\mathrm{~L}(h), H)+g\left(\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) \\
& -g\left(\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{e_{i}}^{g} h\right) e_{j}\right)-g\left(\left(\nabla_{e_{i}}^{g} h\right) H e_{j},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) \\
& =g(\mathrm{~L}(h), H)+g\left(\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) \\
& -2 g\left(\left(\nabla_{e_{i}}^{g} h\right) H e_{j},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right)
\end{aligned}$$
after also taking into account that $H$ is symmetric. The second summand above may be computed alternatively according to the following observation which essentially takes into account that $H J=J H$. Indeed,
$$\begin{aligned}
g\left(\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) & =g\left(\left(\nabla_{J H e_{j}}^{g} h\right) J e_{i},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right) \\
& =g\left(\left(\nabla_{J H e_{j}}^{g} h\right) J e_{i}-\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right) \\
& +g\left(\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right) .
\end{aligned}$$
Taking into account the symmetry property in (22) and the fact that $\bar{\partial} h$ is $J$-anti-invariant we compute
$$\begin{aligned}
& g\left(\left(\nabla_{J H e_{j}}^{g} h\right) J e_{i}-\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right) \\
= & g\left(\left(\nabla_{J e_{i}}^{g} h\right) J H e_{j}-\left(\nabla_{e_{i}}^{g} h\right) H e_{j},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right)+2 g\left(\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right) \\
= & g\left(\left(\nabla_{e_{i}}^{g} h\right) H e_{j},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right)-g\left(\left(\nabla_{e_{i}}^{g} h\right) H e_{j},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right)-2 g\left(\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) \\
= & g\left(\left(\nabla_{e_{i}}^{g} h\right) H e_{j},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right)+g\left(\left(\nabla_{e_{i}}^{g} h\right) J H e_{j},\left(\nabla_{e_{j}}^{g} h\right) J e_{i}\right)-2 g\left(\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) \\
= & 2 g\left(\left(\nabla_{e_{i}}^{g} h\right) H e_{j},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right)-2 g\left(\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) .
\end{aligned}$$
To obtain the last two lines above we have operated the basis change $e_{j} \mapsto J e_{j}$, used that $H J=J H$ and also taken into account that covariant derivatives of the type $\nabla_{X}^{g} h$ with $X \in T M$ anti-commute with $J$. It follows that
$$\begin{aligned}
g\left(\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) & =2 g\left(\left(\nabla_{e_{i}}^{g} h\right) H e_{j},\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right)+g\left(\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right) \\
& -2 g\left(\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) .
\end{aligned}$$
Replacing this in (23) shows that
$$\begin{aligned}
g\left(\mathrm{~d}_{\nabla^{g}} h\left(e_{i}, H e_{j}\right), \mathrm{d}_{\nabla^{g}} h\left(e_{i}, e_{j}\right)\right) & =g(\mathrm{~L}(h), H)+g\left(\left(\nabla_{H e_{j}}^{g} h\right) e_{i},\left(\nabla_{J e_{j}}^{g} h\right) J e_{i}\right) \\
& -2 g\left(\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) .
\end{aligned}$$
Thus gathering terms and taking into account Lemma 4.17 to express the last summand above leads to
$$\left\langle H \sharp \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}=\left\langle 2 \AA\left(h^{2}\right)+\mathrm{L}(h), H\right\rangle_{L^{2}}-\left\langle\nabla_{\delta^{g}(H J)}^{g} h, h J\right\rangle_{L^{2}}-2 g\left(\bar{\partial} h\left(e_{i}, H e_{j}\right),\left(\nabla_{e_{j}}^{g} h\right) e_{i}\right) .$$

The claim follows using the expression for $\mathrm{L}(h)$ in Lemma 4.15, Lemma 4.16 for the divergence type summand in the right-hand side above respectively Lemma 4.18 for the term containing $\bar{\partial} h$. \(\square\)
4.4. Proof of Theorem 1.6. Proposition 4.19 allows computing explicitly the quantity $\mathbf{v}(h, h)$ with $h \in \mathscr{E}(M, g)$ as indicated below; at the same time we also fully determine the components of $\mathbf{v}(h, h)$ with respect to the complex type decomposition of symmetric tensors, that is $\operatorname{Sym}^{2} T M=\operatorname{Sym}^{2,+} T M \oplus \operatorname{Sym}^{2,-} T M$.
Proposition 4.20. Let $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ satisfy $\bar{\partial} h=0$ and $\delta^{g} h=0$. Then
$$E h^{2}-\mathbf{v}(h, h)+\frac{1}{2} \widetilde{\Delta}_{E} h^{2}=-2 \delta^{g}[h, h]^{c}-\frac{1}{2} \delta^{\star_{g},-} \mathrm{d} \operatorname{tr} h^{2} .$$
Proof. According to (12) we have
$$\begin{aligned}
\langle\mathbf{v}(h, h), H\rangle_{L^{2}}= & \left\langle 2 \delta^{g}[h, h]^{\mathrm{FN}}-\delta^{g} \mathrm{~d}_{\nabla^{g}} h^{2}, H\right\rangle_{L^{2}} \\
& -\left\langle H \sharp \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}+\left\langle H,\left\{h, \delta^{g} \mathrm{~d}_{\nabla^{g}} h\right\}\right\rangle_{L^{2}}
\end{aligned}$$
whenever $H \in \Gamma\left(\operatorname{Sym}^{2} T M\right)$. In addition, using Proposition 4.13 together with the comparison formula (7) shows that the first line above reads
$$\begin{aligned}
& \left\langle 2 \delta^{g}[h, h]^{\mathrm{FN}}-\delta^{g} \mathrm{~d}_{\nabla^{g}} h^{2}, H\right\rangle_{L^{2}} \\
= & \left\langle\left(\Delta_{E}+2 \stackrel{\circ}{R}\right) h^{2}+2 \delta^{g}[h, h]^{c}-2 \delta^{\star_{g},-} \delta^{g} h^{2}+\delta^{\star_{g}} \delta^{g} h^{2}-\left(\Delta_{E}+E+\stackrel{\circ}{R}\right) h^{2}, H\right\rangle_{L^{2}} \\
= & \left\langle(\stackrel{\circ}{R}-E) h^{2}+\left(\delta^{\star_{g},+}-\delta^{\star_{g},-}\right) \delta^{g} h^{2}+2 \delta^{g}[h, h]^{c}, H\right\rangle_{L^{2}} .
\end{aligned}$$
The rest of the proof amounts to computing the remaining terms in the right hand side of (24), according to $H \in \Gamma\left(\operatorname{Sym}^{2,+} T M\right)$ or $H \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$.
(i) Assume that $H \in \Gamma\left(\operatorname{Sym}^{2,+} T M\right)$. Then (25) entails
$$\left\langle 2 \delta^{g}[h, h]^{\mathrm{FN}}-\delta^{g} \mathrm{~d}_{\nabla^{g}} h^{2}, H\right\rangle_{L^{2}}=\left\langle\left(\stackrel{\circ}{R}-E+\delta^{\star_{g},+} \delta^{g}\right) h^{2}, H\right\rangle_{L^{2}} .$$
To compute the remaining terms in (24) we use this time Proposition 4.19 and again (7) to see that $\delta^{g} \mathrm{~d}_{\nabla^{g}} h=(\stackrel{\circ}{R}+E) h$. Thus
$$\begin{aligned}
& -\left\langle H \sharp \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}+\left\langle H,\left\{h, \delta^{g} \mathrm{~d}_{\nabla^{g}} h\right\}\right\rangle_{L^{2}} \\
= & \left\langle-\{\stackrel{\circ}{R} h, h\}+\frac{1}{2}\left(\Delta_{E}-2 \stackrel{\circ}{R}\right) h^{2}+\{h, E h+\stackrel{\circ}{R} h\}-\delta^{\star_{g},+}\left(2 \delta^{g}+\frac{1}{2} \mathrm{~d} \operatorname{tr}\right) h^{2}, H\right\rangle_{L^{2}} \\
= & \left\langle\left(\frac{1}{2} \Delta_{E}-\stackrel{\circ}{R}+2 E\right) h^{2}-\delta^{\star_{g},+}\left(2 \delta^{g}+\frac{1}{2} \mathrm{~d} \operatorname{tr}\right) h^{2}, H\right\rangle_{L^{2}} .
\end{aligned}$$
Gathering these terms in (24) whilst using the definition of $\widetilde{\Delta}_{E}$ shows that
$$\left\langle E h^{2}-\mathbf{v}(h, h)+\frac{1}{2} \widetilde{\Delta}_{E} h^{2}, H\right\rangle_{L^{2}}=0 .$$
(ii) Now assume that $H$ belong to $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$. Since the operator $\stackrel{\circ}{R}-E$ preserves the space $\Gamma\left(\operatorname{Sym}^{2,+} T M\right)$ we find that (25) reduces to
$$\left\langle 2 \delta^{g}[h, h]^{\mathrm{FN}}-\delta^{g} \mathrm{~d}_{\nabla^{g}} h^{2}, H\right\rangle_{L^{2}}=\left\langle 2 \delta^{g}[h, h]^{c}-\delta^{\star_{g},-} \delta^{g} h^{2}, H\right\rangle_{L^{2}} .$$

Finally, having $\mathrm{d}_{\nabla^{g}} h \in \Omega^{1,1}(M, T M)$ entails that $H \sharp \mathrm{~d}_{\nabla^{g}} h$ is a section of $\lambda^{2}(M, T M)$ hence the scalar product $\left\langle H \sharp \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}=0$. Furthermore, using (7) as previously, we obtain that the anti-commutator $\left\{h, \delta^{g} \mathrm{~d}_{\nabla^{g}} h\right\}=\{h, E h+\stackrel{\circ}{R}(h)\}$ belongs to $\Gamma\left(\operatorname{Sym}^{2,+} T M\right)$ hence $\left\langle H,\left\{h, \delta^{g} \mathrm{~d}_{\nabla^{g}} h\right\}\right\rangle_{L^{2}}=0$. We have showed that
$$-\left\langle H \sharp \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}+\left\langle H,\left\{h, \delta^{g} \mathrm{~d}_{\nabla^{g}} h\right\}\right\rangle_{L^{2}}=0 .$$
Plugging the last two displayed equations in (24) thus yields
$$\langle\mathbf{v}(h, h), H\rangle_{L^{2}}=\left\langle 2 \delta^{g}[h, h]^{c}-\delta^{\star g,-} \delta^{g} h^{2}, H\right\rangle_{L^{2}} .$$
The claim follows now from $\left\langle\widetilde{\Delta}_{E} h^{2}, H\right\rangle_{L^{2}}=-\left\langle\delta^{\star g,-}\left(2 \delta^{g} h^{2}+\operatorname{dtr}\left(h^{2}\right)\right), H\right\rangle_{L^{2}}$. \(\square\)

As a consequence of these computations we show below that the Einstein deformation theory to order 2 is entirely explicit. Strikingly, the Hermitian component of $h_{2}$ is determined algebraically in terms of $h_{1}$ only.

Theorem 4.21. Let $\left(M^{2 m}, g, J\right)$ be Kähler-Einstein with $E<0$ and let $g_{t}$ be a normalised Einstein deformation of $g$ with $g_{0}=g$. Then up to a suitable gauge transformation $g_{t} \mapsto f_{t}^{\star} g_{t}$ with $f_{t} \in \mathbf{G}$ we have
$$h_{2}^{+}=h_{1}^{2} \text { and } h_{2}^{-}=\mathbf{h}_{2}-\frac{1}{2} \mathscr{L}_{J \text { gradf }} J$$
where the pair $\left(\mathbf{h}_{2}, \mathbf{f}\right)$ in $\operatorname{TT}^{-}(M, g) \oplus C^{\infty} M$ satisfies
$$\Delta_{E}^{g} \mathbf{h}_{2}=-2 \delta^{g}\left[h_{1}, h_{1}\right]^{c} \text { and }\left(\Delta^{g}-2 E\right) \mathbf{f}=-\frac{1}{2} \operatorname{tr}\left(h_{1}^{2}\right) .$$
Proof. We use the normalisation from Theorem 3.9 so that
$$\Delta_{E}\left(h_{2}-h_{1}^{2}\right)=\frac{1}{2} \widetilde{\Delta}_{E} h_{1}^{2}+E h_{1}^{2}-\mathbf{v}\left(h_{1}, h_{1}\right) .$$
Next take into account that $\Delta_{E}$ preserves complex type and use the expression for $\mathbf{v}\left(h_{1}, h_{1}\right)$ obtained in Proposition 4.20. Thus
$$\begin{aligned}
& \Delta_{E}\left(h_{2}-h_{1}^{2}\right)^{+}=0 \\
& \Delta_{E} h_{2}^{-}=-\frac{1}{2} \delta^{\star_{g},-} \mathrm{d} \operatorname{tr} h_{1}^{2}-2 \delta^{g}\left[h_{1}, h_{1}\right]^{c} .
\end{aligned}$$
Since $E<0$ the comparison formula (17) ensures that $\left(h_{2}-h_{1}^{2}\right)^{+}=0$, that is $h_{2}-h_{1}^{2}$ belong to $\operatorname{Sym}^{2,-} T M$. To solve the last equation in (26) we proceed as follows; since $E<0$ the operator $\Delta^{g}-2 E$ acting on functions is invertible. Hence there exists a unique solution $\mathbf{f}$ to $\left(\Delta^{g}-2 E\right) \mathbf{f}=-\frac{1}{2} \operatorname{tr}\left(h_{1}^{2}\right)$. Furthemore, taking into that $\Delta_{E}$ preserves complex tensor type and Lemma 2.1,(i) we find $\Delta_{E} \delta^{\star^{g},-} X=\delta^{\star^{g},-}\left(\Delta^{g}-2 E\right) X$. Thus letting $X:=$ gradf we see that the second equation in (26) amounts to $\Delta_{E} \mathbf{h}_{2}=-2 \delta^{g}\left[h_{1}, h_{1}\right]^{c}$ where $\mathbf{h}_{2}:=h_{2}^{-}-\delta^{\star_{g},-} X$ belongs to $\operatorname{Sym}^{2,-} T M$. Note that $\delta^{\star_{g},-} X=-\frac{1}{2} \mathscr{L}_{\text {Jgradf }} J$ as entailed by (15).

Since $\delta^{g}\left[h_{1}, h_{1}\right]^{c}$ is divergence free by Proposition 4.12 it follows that
$$0=\delta^{g} \Delta_{E} \mathbf{h}_{2}=\left(\Delta^{g}-2 E\right) \delta^{g} \mathbf{h}_{2}$$
after also taking into account Lemma 2.1,(ii). Because $E<0$ we conclude that the tensor $\mathbf{h}_{2}$ is divergence free, and thus belongs to $\mathrm{TT}^{-}(M, g)$. The claim is now fully proved. \(\square\)

We end the paper with the following
Remark 4.22. The tensor $\bar{\partial} \mathbf{h}_{2}+\left[h_{1}, h_{1}\right]^{c}$ clearly belong to ker $\bar{\partial}$; see also Remark 4.9. By Corollary 4.3 we have $\delta^{g}\left(\bar{\partial} \mathbf{h}_{2}+\left[h_{1}, h_{1}\right]^{c}\right)=\frac{1}{2} \Delta_{E} \mathbf{h}_{2}+\delta^{g}\left[h_{1}, h_{1}\right]^{c}=0$ since $\mathbf{h}_{2}$ is divergence free. Thus the tensor
$$\bar{\partial} \mathbf{h}_{2}+\left[h_{1}, h_{1}\right]^{c} \in \operatorname{ker} \bar{\partial} \cap \operatorname{ker} \delta^{g} .$$
The vanishing of the harmonic tensor $\bar{\partial} \mathbf{h}_{2}+\left[h_{1}, h_{1}\right]^{c}$ characterises the obstruction to second order deformations of the complex structure $J$; see also Remark 4.9, (i).

\section*{References}
\begin{itemize}
\item[] [1] Wafaâ Batat, Stuart James Hall, Thomas Murphy, James Waldron, Rigidity of SUn-type symmetric spaces, Int. Math. Res. Not. IMRN 2024, no. 3, 2066-2098.
\item[] [2] Stuart James Hall, Paul Schwahn, Uwe Semmelmann, On the rigidity of the complex Grassmannians, Trans. Amer. Math. Soc. 378 (2025), no. 6, 4335-4367.
\item[] [3] A.Besse, Einstein manifolds, Classics in Mathematics, Springer-Verlag, Berlin, 2008.
\item[] [4] Xianzhe Dai, Xiaodong Wang, Guofang Wei, On the variational stability of Kähler-Einstein metrics, Comm. Anal. Geom. 15 (2007), no. 4, 669-693.
\item[] [5] Daniel Huybrechts, Complex Geometry. An introduction, Universitext, Springer-Verlag, Berlin, 2005.
\item[] [6] Norihito Koiso, Rigidity and deformability of Einstein metrics, Osaka Math. J. 19 (1982), 643-668.
\item[] [7] Norihito Koiso, Einstein metrics and complex structures, Invent. Math. 73 (1983), no. 1, 71-106.
\item[] [8] Ivan Kolár, Peter Michor, Jan Slovák, Natural operations in differential geometry, Springer-Verlag, Berlin, 1993.
\item[] [9] Emilio A. Lauret, Jorge Lauret, The stability of standard homogeneous Einstein manifolds, Math. Z. 303 (2023), no. 1, Paper No. 16, 36 pp.
\item[] [10] Andrei Moroianu, Uwe Semmelmann, Infinitesimal Einstein deformations of nearly Kähler metrics, Trans. Amer. Math. Soc. 363 (2011), no. 6, 3057-3069.
\item[] [11] Paul-Andi Nagy, Uwe Semmelmann, The $\mathrm{G}_{2}$ geometry of 3-Sasaki structures, J. Geom. Anal. 34 (2024), no. 2, Paper No. 61, 53 pp.
\item[] [12] Paul-Andi Nagy, Uwe Semmelmann, Second order Einstein deformations, J. Math. Soc. Japan 77 (2025), no. 2, 345-389.
\item[] [13] Paul Schwahn, Uwe Semmelmann, Einstein metrics, their moduli spaces and stability, https://arxiv.org/pdf/2507.18463.
\item[] [14] Craig van Coevering, Deformations of Killing spinors on Sasakian and 3-Sasakian manifolds, J. Math. Soc. Japan 69 (2017), no. 1, 53-91.
\end{itemize}
(Paul-Andi Nagy) Center for Complex Geometry, Institute for Basic Science(IBS), 55 Exporo, Yuseong-gu, 34126 Daejeon, South Korea
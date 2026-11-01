---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The Dirichlet-to-Neumann Map for Poincaré–Einstein Fillings]

Recall that $X_{a b}^{(\ell)}$ has transverse order $\ell+2$ and $I$ has transverse order at most $m=k-1$. So there exists an expression for $I$ such that for any appearance of $X$ (from above we have that $Y$ and $Z$ can be reduced to terms involving only $X$ at leading order) one has that that $\ell$ is not greater than $k-3$. But for $\mathrm{APE}_{k-2}$ structures the $k^{\text {th }}$ fundamental form (which has transverse order $k-1$ ), and all lower order fundamental forms vanish. Hence, $I$ is expressible in terms of $T$-curvatures and intrinsic tensors alone. But (see [22, Theorem 6.15] or Proposition 3.2) there exists a scale for which these $T$-curvatures vanish. Moreover, natural intrinsic curvatures are composed of sums of products of the Riemann tensor, metrics as well as covariant derivatives and traces thereof, all of which have even homogeneity under constant metric rescalings. Thus, because the weight of $I$ is odd, there are no such intrinsic tensors available as these are taken to be (polynomially) built from $\bar{g}, \bar{g}^{-1}, \bar{R}, \bar{\nabla}$ and contractions thereof. This establishes that $I$ vanishes for one choice of scale, and hence by its conformal invariance, $I=0$. \(\square\)

Remark 3.8. Note that another approach to establishing this result is to examine the tensor structures that can appear as coefficients in the Fefferman-Graham expansion of an $\mathrm{APE}_{k-2}$ metric; this approach might be used to write a more general result for $d$ odd. \(\square\)

We will need explicit formulæ for Dirichlet-to-Neumann tensors in even dimensions in order to prove Theorem 1.2

Lemma 3.9. Let $\left(M_{+}^{d}, g^{o}\right)$ be a Poincaré-Einstein structure with $d \geqslant 6$ even. Then,
$$\mathrm{DN}_{a b}^{(d)} \propto \stackrel{\circ}{\top}: \nabla_{\hat{n}}^{d-5}: B_{a b}^{g_{r}},$$
where the right hand side is evaluated on the Graham-Lee compactified metric $g_{r}$ used to define the left hand side.

Proof. By definition, the image of the Dirichlet-to-Neumann map of a metric representative $\bar{g} \in \boldsymbol{c}_{\Sigma}$ is given by $\left.\left(\mathcal{L}_{\frac{\partial}{\partial r}}\right)^{d-1} g_{r}\right|_{\Sigma}$, where $g_{r}$ is the corresponding Graham-Lee compactified metric. Calling $n=\mathrm{d} r, n^{\sharp}:=g_{r}^{-1}(n, \cdot)$, and using that $|n|=1$, it follows that
$$\mathrm{DN}_{a b}^{(d)}=\left(\mathcal{L}_{n^{\sharp}}\right)^{d-1} g_{a b} \stackrel{\Sigma}{=}\left(\mathcal{L}_{n^{\sharp}}\right)^{d-2}\left(\nabla_{a} n_{b}+\nabla_{b} n_{a}\right) .$$
Now evidently, the leading derivative term in the above is the same as that of
$$2 \nabla_{n^{\sharp}}^{d-2} \nabla_{(a} n_{b)} .$$
Moreover, the natural hypersurface invariant $\mathrm{DN}_{a b}^{(d)}-2 \nabla_{n^{\sharp}}^{d-2} \nabla_{(a} n_{b)}$ has transverse order no larger than $d-2$. So from [8], it is expressible entirely in terms of Riemannian invariants intrinsic to $\Sigma$,
conformal fundamental forms ranging from $\stackrel{\circ}{\text { I }}$ to $\stackrel{\circ}{\frac{d-1}{}}$, and $T$-curvatures up to order $d-2$. However, as $\left(M_{+}^{d}, g^{o}\right)$ is Poincaré-Einstein, it follows from [10] that all conformal fundamental forms from İ to $\underline{\underline{d-1}}$ vanish. Hence, by the hypersurface invariant decomposition of type (3.2) established earlier in this section, the difference in question can be expressed solely in terms of intrinsic invariants and $T$-curvatures. Now, because this difference has a definite odd homogeneity of $3-d$ under constant rescalings of the metric $g \mapsto \lambda^{2} g$, and because intrinsic invariants always have even homogeneity, it follows that every summand in any such decomposition must involve at least one occurence of an odd-order $T$-curvature. But, as $g$ is a Graham-Lee compactified metric, it follows from Theorem 3.6 that all odd order $T$-curvatures up to order $d-1$ inclusive vanish, and so
$$\mathrm{DN}_{a b}^{(d)}=\left.\left(\mathcal{L}_{n^{\sharp}}\right)^{d-1} g_{a b}\right|_{\Sigma}=\left.2 \nabla_{n}^{d-2} \nabla_{(a} n_{b)}\right|_{\Sigma} .$$

Now, using the Ricci identity, we have the following identity:
$$\begin{aligned}
\nabla_{n} \nabla_{a} n_{b} & =n^{c} \nabla_{c} \nabla_{a} \nabla_{b} r \\
& =n^{c} R_{c a b d} n^{d}+n^{c} \nabla_{a} \nabla_{b} n_{c} \\
& =R_{n a b n}-\left(\nabla_{a} n^{c}\right)\left(\nabla_{b} n_{c}\right)+\frac{1}{2} \nabla_{a} \nabla_{b} n^{2} \\
& =R_{n a b n}-\left(\nabla_{a} n^{c}\right)\left(\nabla_{b} n_{c}\right),
\end{aligned}$$
where the last identity follows because $n^{2}=1$. Now using this identity in the formula for $\mathrm{DN}^{(d)}$, and throwing away lower transverse order terms because they either involve (vanishing) odd order $T$-curvatures or conformal fundamental forms, we have that
$$\mathrm{DN}_{a b}^{(d)}=2 \nabla_{n}^{d-3} R_{n a b n} .$$
Now applying the same reasoning as directly above to the decomposition of Riemann into its Weyl and Schouten tensor pieces, we may in turn express this as
$$\mathrm{DN}_{a b}^{(d)}=-2(d-2) \stackrel{\circ}{\top}^{\circ}: \nabla_{\hat{n}}^{d-3}: P_{a b} .$$
Finally, using Equation (1.3) we have $\stackrel{\circ}{\top} B=\stackrel{\circ}{\top} \nabla_{n}^{2} P$ modulo lower order terms (which again vanish by similar reasoning to above), we have that
$$\mathrm{DN}_{a b}^{(d)} \propto \stackrel{\circ}{\top}: \nabla_{\hat{n}}^{d-5}: B_{a b},$$
thus completing the proof. \(\square\)

We are now ready to prove Theorem 1.2
Proof of Theorem 1.2. To unify the $d=6$ and $\geqslant 8$ formulæ, let us denote $\delta_{0,1}:=\delta_{R}$. We shall begin by checking that $\bar{q}^{*} \stackrel{\circ}{\top} \delta_{\frac{d-6}{2}, \frac{d-4}{2}} W$ has the required leading transverse order and that the tractor $\delta_{\frac{d-6}{2}, \frac{d-4}{2}} W$ has a projecting part with the correct tensor structure-this will establish that the leading transverse order term in $\frac{\circ}{\underline{d}}^{\mathrm{DN}}$ is as required by the theorem. (Note that by its construction, $\frac{\circ}{\underline{d}}^{\mathrm{DN}}$ is clearly a natural conformal hypersurface invariant.)

From [8, Theorem 3.4] we have that $\delta_{\frac{d-6}{2}, \frac{d-4}{2}}$ acting on weight -2 tractors has transverse order $d-5$, and thus
$$\delta_{\frac{d-6}{2}, \frac{d-4}{2}} W \propto: \nabla_{\hat{n}}^{d-5}: W+\text { ltots } .$$
The highest transverse order tensor component of the $W$-tractor is the Bach tensor, so
$$(d-4) W_{A B C D} \stackrel{\tau_{g}}{=} 4 X_{[A} Z_{B]}^{a} X_{[C} Z_{D]}^{b} B_{a b}^{g}+\text { ltots } .$$
(Here $g \in \boldsymbol{c}$ is any choice of metric representative and we employ this choice for the remainder of this proof.) Thus, we have that
$$\stackrel{\circ}{\top} \delta_{\frac{d-6}{2}, \frac{d-4}{2}} W_{A B C D} \propto \stackrel{\circ}{\top} X_{[A} Z_{B]}^{a} X_{[C} Z_{D]}^{b}: \nabla_{\hat{n}}^{d-5}: B_{a b}^{g}+\text { ltots }_{d-2},$$
where ltots ${ }_{d-2}$ are tensor-valued tractors with transverse order less than or equal to $d-2$. The $d \geqslant 4$ Bach tensor $B_{b d}=\left(\frac{1}{d-3} \nabla^{a} \nabla^{c}+P^{a c}\right) W_{a b c d}$ has transverse order 4. To see this we apply Equation (3.8) to the Weyl tensor and find
$$\begin{aligned}
W_{a b c d}^{g+s^{\ell} h}-W_{a b c d}^{g}=-\frac{\ell(\ell-1)}{2(d-2)} s^{\ell-2} & \left(\left[(d-3) \hat{n}_{a} \hat{n}_{c}-\bar{g}_{a c}\right] h_{b d}^{\top}-\left[(d-3) \hat{n}_{b} \hat{n}_{c}-\bar{g}_{b c}\right] h_{a d}^{\top}\right. \\
& \left.-\left[(d-3) \hat{n}_{a} \hat{n}_{d}-\bar{g}_{a d}\right] h_{b c}^{\top}+\left[(d-3) \hat{n}_{b} \hat{n}_{d}-\bar{g}_{b d}\right] h_{a c}^{\top}\right)+\mathcal{O}\left(s^{\ell-1}\right),
\end{aligned}$$
where $\bar{g}_{a b}$ is any extension of $g_{a b}-\hat{n}_{a} \hat{n}_{b}$ to $M$ and $h_{a b}^{\text {° }}$ any such extension of $\bar{g}_{a c} \bar{g}^{c d} h_{d b}-$ $\frac{1}{d-1} \bar{g}_{a b} \bar{g}^{c d} h_{c d}$. Hence for the Bach tensor we obtain
$$B_{a b}^{g+s^{\ell} h}-B_{a b}^{g}=-\frac{\ell(\ell-1)(\ell-2)(\ell-3)}{2(d-2)} s^{\ell-4} h_{a b}^{\top}+\mathcal{O}\left(s^{\ell-3}\right) .$$
This establishes the claimed transverse order result. In turn, it follows that the tractor in Equation (3.11) has transverse order $d-1$. It is also now clear that, for generic structures, the coefficient of $\stackrel{ণ}{\top} X_{[A} Z_{B]}^{a} X_{[C} Z_{D]}^{b}$ in $\stackrel{\circ}{\top} \delta_{\frac{d-6}{2}, \frac{d-4}{2}} W$ is non-zero.

Now suppose the projecting part of $\stackrel{\circ}{\top} \delta_{\frac{d-6}{2}, \frac{d-4}{2}} W_{A B C D}$ is not proportional to $\stackrel{\circ}{\top} X_{[A} Z_{B]}^{a} X_{[C} Z_{D]}^{b}$. In that case it must consist of terms appearing among those labeled ltots $_{d-2}$ in Equation (3.11). But then the putative projecting part of $\stackrel{\circ}{\top} \delta_{\frac{d-6}{2}, \frac{d-4}{2}} W_{A B C D}$ would have both odd weight and transverse order strictly less than $d-1$ and thus vanish by Theorem 3.7. Thus we must now have
$$\stackrel{\circ}{\top} \delta_{\frac{d-6}{2}, \frac{d-4}{2}} W_{A B C D} \propto \stackrel{\circ}{\top} X_{[A} Z_{B]}^{a} X_{[C} Z_{D]}^{b}\left(: \nabla_{\hat{n}}^{d-5}: B_{a b}^{g}+\operatorname{ltots}_{d-2}\right) .$$
So by construction, we have that
$$\bar{q}^{*} \stackrel{\circ}{\top} \delta_{\frac{d-6}{2}, \frac{d-4}{2}} W \propto \stackrel{\circ}{\top}: \nabla_{\hat{n}}^{d-5}: B^{g}+\operatorname{ltots}_{d-2} \in \Gamma\left(\left.\stackrel{\circ}{\top} \odot^{2} T^{*} M[3-d]\right|_{\Sigma}\right) .$$

We next must show that $\underline{\bar{d}}^{\mathrm{DN}}$ is the unique (up to multiplication by a constant and natural) conformal hypersurface invariant of transverse order $d-1$ in $\Gamma\left(\left.\stackrel{\circ}{\top} \odot^{2} T^{*} M[3-d]\right|_{\Sigma}\right)$ determined by the Poincaré-Einstein structure. The $d=6$ case is handled in Theorem 1.1 whose proof is given in Appendix A. By similar considerations as those given there, the leading transverse order term of $\frac{\circ}{\underline{d}}^{\mathrm{DN}}$ for $d \geqslant 8$ is unique. Now suppose that there exist two distinct conformal hypersurface invariants
$$\stackrel{\circ}{\top}: \nabla_{\hat{n}}^{d-5}: B+Q \text { and } \stackrel{\circ}{\top}: \nabla_{\hat{n}}^{d-5}: B+Q^{\prime},$$
where $Q \neq Q^{\prime}$ are tensors with transverse order less than or equal to $d-2$. Necessarily $Q-Q^{\prime}$ is conformally invariant, has transverse order at most $d-2$, and weight $3-d$ (an odd integer) so vanishes by dint of Theorem 3.7. This establishes uniqueness of $\underline{\bar{d}}^{\mathrm{DN}}$.

Finally, we must check that $\underline{\bar{d}}^{\mathrm{DN}} \simeq \mathrm{DN}^{(d)}$. From Lemma 3.9 this amounts to checking that the terms labeled ltots $_{d-2}$ in Equation (3.12) vanish when evaluated on a Graham-Lee compactified metric. This is achieved by recycling the argument used to prove Lemma 3.9. Because it has already been established that $\mathrm{DN}^{(d)}$ is the functional gradient of the renormalized volume-see [14, Section 3.4], [5, below Theorem 2.2] and [1, Theorem 1.3])-we have completed the proof. \(\square\)

Remark 3.10. As discussed above the tensor $\mathrm{DN}^{(d)}$ is a functional gradient along a path of Poincaré-Einstein metrics which can be labelled by a path of boundary metrics, so its boundary divergence must vanish,
$$\bar{\nabla}^{a} \mathrm{DN}_{a b}^{(d)}=0 .$$
In fact both $\bar{\nabla}^{a} \mathrm{DN}_{a b}^{(d)}$ and $\bar{\nabla}^{a} \frac{\circ}{d}_{a b}^{\mathrm{DN}}$ are conformally invariant. Theorem 1.2 therefore establishes the vanishing of the latter. \(\square\)
3.3. Odd dimensional bulk. We first need to characterize conformal hypersurface invariants for (asymptotically) Poincaré-Einstein structures with conformally flat boundaries. The following is an analog of Theorem 3.7.

Lemma 3.11. Let $\Sigma \hookrightarrow\left(M^{d}, \boldsymbol{g}\right)$ be a conformal hypersurface embedding where $\left(M^{d}, \boldsymbol{g}, \sigma\right) \in$ $\mathrm{APE}_{k-2}$ with $2 \leqslant k \leqslant d-1$. Moreover, suppose that the boundary $\left(\Sigma, \boldsymbol{c}_{\Sigma}\right)$ is conformally flat. Then any natural conformal hypersurface invariant $I \in \Gamma(\mathbb{T} \Sigma[w])$ with transverse order $1 \leqslant m \leqslant k-1$ vanishes.

Proof. First we choose a scale for which the boundary metric $\bar{g}=\bar{\delta}$ is flat. Then, the corresponding Fefferman-Graham expansion of the compactified metric $g_{r}$ of an $\mathrm{APE}_{k-2}$ structure is
$$g_{r}=\mathrm{d} r^{2}+\bar{\delta}+r^{k} Y$$
for some smooth, rank two, symmetric tensor $Y$ which is trace-free by virtue of the Poincaré-Einstein condition. The above expansion follows directly from the treatment of conformally flat and conformally Einstein spaces in [17, Chapter 7]; see also Equation (3.14) below. The statement now follows since the only local conformal invariants for a flat metric are those built from the metric itself, and that the order $r^{k}$ term cannot contribute to invariants of transverse order strictly less than $k$. Vanishing in one scale implies the same for all other scales. \(\square\)

We are now ready to prove Theorems 1.3 and 1.4.
Proof of Theorem 1.3. By Lemma 3.11, we only need consider invariants of transverse order zero or four. Because the boundary conformal class is flat, the only intrinsic (and hence transverse order zero) conformal invariants of the correct homogeneity and tensor type are powers of the metric and its inverse (see also Remark 3.12). No trace-free tensors can be made this way. Then an exhaustive search establishes that the only Riemannian hypersurface invariant of the desired homogeneity, tensor type and transverse order four, for the metric of Equation (3.13) (with $k=4$ ), is $B_{(a b) \circ}^{\top}$. But the conformal transformation of the Bach tensor is
$$\Omega^{2} B_{a b}^{\Omega^{2} g}-B_{a b}^{g}=(d-4)\left(2 C_{\Upsilon(a b)}-W_{\Upsilon a b \Upsilon}\right),$$
and the right hand side vanishes when evaluated on the metric of Equation (3.13), so $B_{(a b) \circ}^{\top}$ is conformally invariant. Finally, a calculation of the $B_{(a b) \circ}^{\top}$ in the metric of Equation (3.13) shows that this is proportional to $Y$ along $\Sigma$, which establishes that $\stackrel{\circ}{\mathrm{V}}^{\mathrm{DN}^{b}} \simeq \mathrm{DN}^{(5)}$. \(\square\)

Remark 3.12. Note that the only non-zero, transverse order zero, $d=5$, natural, conformally invariant, sections of $\odot_{0}^{2} T^{*} \Sigma[-2]$ are $\bar{B}_{a b}$ and $\bar{W}_{(a \mid c d e} \bar{W}_{b) \circ}{ }^{c d e}$. Also, for APE ${ }_{2}$ structures with a generic conformal class $\boldsymbol{c}_{\Sigma}$, there are no conformally-invariant transverse-order 2 or 4 tensors of this type. A simpler version of the exhaustive analysis of tensor structures and their conformal variations given in Appendix A can be used to establish this. \(\square\)

Proof of Theorem 1.4. We must verify the well-definedness of two definitions, perform a computation for $\mathrm{DN}^{(d)}$, and establish a proportionality statement. To start with, it is known (see [17]) that a $d \geqslant 7$ Poincaré-Einstein metric $g^{o}$ with conformally flat boundary has the Fefferman-Graham expansion
$$g_{r}:=r^{2} g^{o}=\mathrm{d} r^{2}+\bar{g}-\bar{P} r^{2}+\frac{1}{4} \bar{P}^{\odot 2} r^{4}+\mathcal{O}\left(r^{d-1}\right),$$
where $\bar{P}$ is the Schouten tensor of $\bar{g}$. Importantly the above expansion holds for any $\bar{g} \in \boldsymbol{c}_{\Sigma}$. In particular, choosing (locally) $\bar{g}$ to be the flat metric $\bar{\delta}$, it follows that the Weyl tensor of $g_{r}$ obeys
$$W_{a b}{ }^{c}{ }_{d}=\mathcal{O}\left(r^{d-3}\right) .$$

In turn, for any $g \in \boldsymbol{c}$ we have that the tractor curvature
$$F_{a b}{ }^{A}{ }_{B}=W_{a b}{ }^{c d} Z_{c}^{A} Z_{d B}+C_{a b}{ }^{c}\left(Z_{c}^{A} X_{B}-Z_{c B} X^{A}\right)=\left(\begin{array}{ccc}
0 & 0 & 0 \\
\mathcal{O}\left(r^{d-4}\right) & \mathcal{O}\left(r^{d-3}\right) & 0 \\
0 & \mathcal{O}\left(r^{d-4}\right) & 0
\end{array}\right),$$
so that, for any $1 \leqslant k \leqslant d-4$ and $\sigma=[g ; s]$,
$$: \nabla_{\hat{n}}^{k}: F_{a b}{ }^{A}{ }_{B} \stackrel{\tau_{g}}{=}\left(\begin{array}{ccc}
\mathcal{O}\left(s^{d-k-3}\right) & \mathcal{O}\left(s^{d-k-2}\right) & 0 \\
\mathcal{O}\left(s^{d-k-4}\right) & \mathcal{O}\left(s^{d-k-3}\right) & \mathcal{O}\left(s^{d-k-2}\right) \\
0 & \mathcal{O}\left(s^{d-k-4}\right) & \mathcal{O}\left(s^{d-k-3}\right)
\end{array}\right) .$$
But any failure of $: \nabla_{\hat{n}}^{d-4}: F_{a b}{ }^{A}{ }_{B}$ to be conformally invariant necessarily involves terms proportional to the above display with $k \leqslant d-5$. These vanish along $\Sigma$; to see this, one can re-express the tractor connection (2.2) in a matrix notation and then explicitly examine the failure of the above to transform correctly.

Thus we now observe that
$$\hat{n}^{a}: \nabla_{\hat{n}}^{d-4}: F_{a b}{ }_{D} \stackrel{\Sigma}{=}\left(\begin{array}{ccc}
0 & 0 & 0 \\
\hat{n}^{a}: \nabla_{\hat{n}}^{d-4}: C_{a b}^{c} & 0 & 0 \\
0 & -\hat{n}^{a}: \nabla_{\hat{n}}^{d-4}: C_{a b d} & 0
\end{array}\right) .$$
Note that $C_{n[b c]}=-\frac{1}{2} C_{b c n}=-n^{a} \nabla_{[b} P_{c] a}$ so $C_{n[b c]}-n_{[b} C_{c] n n}$ (which restricts along $\Sigma$ to $C_{\hat{n}[b c]}^{\top}$ ) vanishes to one higher order than its symmetric counterpart and thus
$$\left.\left(\hat{n}^{a}: \nabla_{\hat{n}}^{d-4}: C_{a[b c]}\right)^{\top}\right|_{\Sigma}=0 .$$
Since $\left.\hat{n}^{a}\left(: \nabla_{\hat{n}}^{d-4}: C_{a b c}\right)\right|_{\Sigma}$ appears as the projecting part of a tractor, and is symmetric, we then have that
$$\stackrel{\circ}{\uparrow} \circ q^{*}\left(\left.\left[\hat{n}^{a}: \nabla_{\hat{n}}^{d-4}: F_{a b}^{C} D\right]\right|_{\Sigma}\right)=\left.\stackrel{\circ}{\top} \circ\left[\hat{n}^{a}: \nabla_{\hat{n}}^{d-4}: C_{a b c}\right]\right|_{\Sigma}$$
is a well-defined element of $\Gamma\left(\left.\stackrel{\circ}{\top} \odot^{2} T^{*} M[3-d]\right|_{\Sigma}\right)$. In the case $d=5$, a short computation shows that, in the current setting, the right hand side above equals $B_{(a b) \circ}^{\top}$.

Unlike in the even dimensional case, no parity argument ensures that the relevant Fefferman-Graham expansion coefficient defining $\mathrm{DN}^{(d)}$ is covariant with respect to different choices of the boundary metric representative. We shall check that it is by hand. For that we define a reference metric
$$\tilde{g}_{r}:=\mathrm{d} r^{2}+\bar{g}-\bar{P} r^{2}+\frac{1}{4} \bar{P} \odot 2 r^{4}$$
on a collar neighborhood of $\Sigma$. Note that the above is conformal to the hyperbolic metric [17]. Then we define a smooth tensor $X^{\bar{g}}$ in a collar of the boundary (and by dint of smoothness, along $\Sigma$ itself) by
$$r^{d-1} X^{\bar{g}}=g_{r}-\tilde{g}_{r} .$$
Upon choosing a different metric $\bar{g}^{\prime} \in \boldsymbol{c}_{\Sigma}$, with respect to the new distance function $r^{\prime}=\Omega(r) r$ (suppressing the dependence of $\Omega(r)$ on boundary directions), the new compactified metric $g^{\prime}$ then obeys (by virtue of Equation(3.14))
$$g_{r^{\prime}}^{\prime}-\tilde{g}_{r^{\prime}}=r^{\prime d-1} X^{\bar{g}^{\prime}}$$
But, again relying on [17],
$$g_{r^{\prime}}^{\prime}-\tilde{g}_{r^{\prime}}=\Omega(r)^{2}\left(g_{r}-\tilde{g}_{r}\right)+\mathcal{O}\left(r^{d}\right) .$$
Thus we learn that
$$r^{\prime d-1} X^{\bar{g}^{\prime}}=\Omega(r)^{2} r^{d-1} X^{\bar{g}}+\mathcal{O}\left(r^{d}\right) .$$
So using $r^{\prime}=\Omega(r) r$ and $0<\Omega(0)=\bar{\Omega} \in C^{\infty} \Sigma$, we have that
$$X^{\bar{g}^{\prime}} \stackrel{\Sigma}{=} \bar{\Omega}^{3-d} X^{\bar{g}}$$

Clearly $\left.(d-1)!X^{\bar{g}}\right|_{\Sigma}=\left.\left(\mathcal{L}_{\frac{\partial}{\partial r}}\right)^{d-1} g_{r}\right|_{\Sigma}$. To show that $\left.X\right|_{\Sigma}$ is trace-free, we first note that the Poincaré-Einstein condition implies that (see for example [19])
$$n^{2}+2 \rho \sigma=1,$$
where $n:=\mathrm{d} r$ and $\rho:=-\left(\nabla^{a} n_{a}+r J\right) / d$, which in the scale $\sigma=\left[g_{r} ; r\right]$ implies
$$0=-d \rho=\nabla \cdot n+r J^{g_{r}} .$$
With impunity, we may once again compute in the boundary flat metric $\bar{\delta}$ scale for which
$$g_{r}=\mathrm{d} r^{2}+\bar{\delta}+r^{d-1} X^{\bar{\delta}} .$$
Then simple computations show
$$\nabla . n=\frac{d-1}{2} r^{d-2} \operatorname{tr}_{\bar{\delta}} X^{\bar{\delta}}+\mathcal{O}\left(r^{d-1}\right)$$
and
$$r J^{g_{r}}=-\frac{d-2}{2} r^{d-2} \operatorname{tr}_{\bar{\delta}} X^{\bar{\delta}}+\mathcal{O}\left(r^{d-1}\right) .$$
Hence the right hand side of Equation (3.15) equals $\frac{1}{2} \operatorname{tr}_{\bar{\delta}} X^{\bar{\delta}}$. So $\left.X^{\bar{g}}\right|_{\Sigma}$ must be trace-free for any choice of boundary scale, so indeed $\mathrm{DN}^{(d)}:=\left.\left(\mathcal{L}_{\frac{\partial}{\partial r}}\right)^{d-1} g_{r}\right|_{\Sigma}$ defines an element of $\Gamma\left(\odot_{\diamond}^{2} T^{*} \Sigma[3-d]\right)$.

It only remains to check that $\mathrm{DN}^{(d)}$ and $\underline{\bar{d}}^{\mathrm{DN}^{\mathrm{b}}}$ are proportional when evaluated on a Graham-Lee compactified metric. By their respective conformal invariance, we may perform this computation in the metric choice of Equation (3.16). It is now easy to verify the stated proportionality result. \(\square\)

Remark 3.13. Fefferman and Graham [17] show that the expansion (3.14) also applies when the boundary class of metrics admits an Einstein metric when written in the Fefferman-Graham coordinate $r$ corresponding to the boundary Einstein metric, and that these expansions are diffeomorphic if there happen to be distinct Einstein metrics in the boundary conformal class. This implies the existence of a Dirichlet-to-Neumann map that is an invariant of the Poincaré-Einstein structure for the boundary-Einstein case. It is likely that there are other such constructions for distinguished boundary conformal classes. \(\square\)

\section*{Acknowledgements}

We thank Robin Graham for useful discussions. S.B. acknowledges the support of the Czech Science Foundation (GACR) grant GA22-00091S and the Operational Programme Research Development and Education Project No. CZ.02.01.01/00/22-010/0007541. A.R.G. and A.W. acknowledge support from the Royal Society of New Zealand via Marsden Grants 19-UOA-008 and 24-UOA-005. J.K. acknowledges funding received from the Norwegian Financial Mechanism 2014-2021, project registration number UMO-2019/34/H/ST1/00636. A.W. was also supported by Simons Foundation Collaboration Grant for Mathematicians ID 686131, and thanks the University of Auckland for warm hospitality.

\section*{Appendix A. Proof of Theorem 1.1}

The uniqueness part of the proof is by exhaustion. The key details are as follows. Given an embedded hypersurface $\Sigma \hookrightarrow(M, g)$, any natural diffeomorphism invariant along $\Sigma$ can be fully described by contractions of the conormal $\hat{n}$, its tangential derivatives, the metric and its inverse, and the bulk curvature $R^{g}$ along with its derivatives $\nabla^{k} R^{g}$. Note the embedding $\Sigma \hookrightarrow\left(M_{+}, g^{o}\right)$ for Poincaré-Einstein structures is necessarily umbilic [34, 19]. Hence tangential derivatives of $\hat{n}$ only produce the mean curvature, its hypersurface derivatives and the induced metric. The latter can be expressed in terms of the unit conormal and ambient metric. So, in a choice of metric representative $g \in \boldsymbol{c}$, any natural conformal hypersurface invariant of $\Sigma \hookrightarrow(M, \boldsymbol{c})$ is expressible by such a diffeomorphism invariant. This is established in [8, Proposition 2.2] (which is based
on [25, Proposition 2.7]). Thus we construct all possible candidate diffeomorphism invariants and then show that only a single combination of these produces the desired, transverse order 5, conformal hypersurface invariant in $\Gamma\left(\odot_{\circ}^{2} T^{*} \Sigma[-3]\right)$. The homogeneity under constant metric rescalings of the above set of "letters" is tabulated below:

\begin{tabular}[t]{|l|l|}
\hline Ingredient & Weight \\
\hline $g^{a b}$ & -2 \\
\hline $\hat{n}_{a}$ & 1 \\
\hline $H^{g}$ & -1 \\
\hline $\bar{\nabla}_{a}$ & 0 \\
\hline $\nabla_{a}$ & 0 \\
\hline $R_{a b c d}$ & 2 \\
\hline
\end{tabular}
We note that when building a rank-2 trace-free tensor with conformal weight -3 from the above letters, only the inverse metric can reduce tensor rank. Hence, to find all words with the aforementioned properties, we are faced with a non-negative, integer-valued linear algebra problem whose solutions are listed below:
$$\begin{gathered}
\bar{\nabla}^{2} H^{3}, g^{-1} H^{3} R,\left(g^{-1}\right)^{2} \hat{n}^{2} H^{3} R,\left(g^{-1}\right)^{2} \hat{n}\left(\bar{\nabla} H^{2}\right) R,\left(g^{-1}\right)^{2} \hat{n} H^{2} \nabla R,\left(g^{-1}\right)^{2}\left(\bar{\nabla}^{2} H\right) R, g^{-1} \bar{\nabla}^{4} H, \\
\left(g^{-1}\right)^{3} \hat{n}^{2}\left(\bar{\nabla}^{2} H\right) R,\left(g^{-1}\right)^{3} H R^{2},\left(g^{-1}\right)^{4} \hat{n}^{2} H R^{2},\left(g^{-1}\right)^{2}(\bar{\nabla} H) \nabla R,\left(g^{-1}\right)^{3} \hat{n}^{2}(\bar{\nabla} H) \nabla R, \\
\left(g^{-1}\right)^{2} H \nabla^{2} R,\left(g^{-1}\right)^{3} \hat{n} H \nabla^{2} R,\left(g^{-1}\right)^{4} \hat{n} \nabla R^{2},\left(g^{-1}\right)^{3} \hat{n} \nabla^{3} R .
\end{gathered}$$
Note that the condition $\hat{n}_{a} \hat{n}^{a}=1$ gives an upper bound on the number of appearances of $\hat{n}$ conditioned on the other letters appearing. Also, since we are searching for rank-two, trace-free covariant tensors, all inverse metrics $g^{-1}$ must be completely contracted.

The number of independent rank two tensors built from linear combinations of the above list of words reduces significantly because ( $M_{+}^{6}, g^{o}$ ) is Poincaré-Einstein, which allows these tensors to be re-expressed in terms of $\bar{g}, \bar{g}^{-1}, \bar{\nabla}, \bar{R}, J, \nabla_{\hat{n}} J, H$, and $\stackrel{\circ}{\top} \nabla_{\hat{n}} B$. The list of all weight -3, rank-2 combinations of these letters is given by
$$\begin{gathered}
\stackrel{\circ}{\top} \nabla_{\hat{n}} B, \bar{\nabla}^{2} \nabla_{\hat{n}} J, \bar{g}^{-1} \bar{R} \nabla_{\hat{n}} J, \bar{\nabla}^{2} H J, \bar{g}^{-1} H J \bar{R}, \\
\bar{g}^{-1} \bar{\nabla}^{4} H,\left(\bar{g}^{-1}\right)^{2} \bar{\nabla} H \bar{R},\left(\bar{g}^{-1}\right)^{3} H \bar{R}^{2}, \bar{\nabla}^{2} H^{3}, \bar{g}^{-1} H^{3} \bar{R} .
\end{gathered}$$
These yield 24 linearly independent symmetrized and trace-free tensors of the correct weight and transverse orders:
$$\begin{gathered}
\odot_{\diamond}^{2}\left\{\uparrow \nabla_{\hat{n}} B_{a b}, \bar{P}_{c d} \nabla_{\hat{n}} J, \bar{\nabla}_{c} \bar{\nabla}_{d} \nabla_{\hat{n}} J,\left(\bar{\nabla}_{c} H\right) \bar{\nabla}_{d} J, H J \bar{P}_{c d}, H \bar{\nabla}_{c} \bar{\nabla}_{d} J, \bar{W}^{a c d b} \bar{\nabla}_{a} \bar{\nabla}_{b} H,\right. \\
\bar{C}_{a c d} \bar{\nabla}^{a} H, H \bar{B}_{c d}, H \bar{W}_{c}^{e a b} \bar{W}_{d a b e}, H \bar{W}_{c}^{a b e} \bar{W}_{d a b e}, H \bar{W}_{c}^{b a e} \bar{W}_{d a b e}, H \bar{P}_{c a} \bar{P}_{d}^{a} \\
H \bar{P}^{a b} \bar{W}_{a c d b}, H \bar{J} \bar{P}_{c d}, H^{3} \bar{P}_{c d} \bar{J} \bar{\nabla}_{c} \bar{\nabla}_{d} H,\left(\bar{\nabla} H_{c}\right) \bar{\nabla}_{d} \bar{J}, H \bar{\nabla}_{c} \bar{\nabla}_{d} \bar{J}, \bar{\nabla}_{c} \bar{\nabla}_{d} \bar{\Delta} H \\
\left.\bar{P}_{c}^{a} \bar{\nabla}_{a} \bar{\nabla}_{d} H, H^{2} \bar{\nabla}_{c} \bar{\nabla}_{d} H, H\left(\bar{\nabla}_{c} H\right)\left(\bar{\nabla}_{d} H\right), \bar{P}_{c d} \bar{\Delta} H\right\}
\end{gathered}$$
Requiring that the conformal variation of an arbitrary linear combination of the above basis elements vanishes, we find a unique combination for which the coefficient of the (only) transverse order five tensor $\stackrel{+}{\top} \nabla_{\hat{n}} B$ is unity. In a choice of metric $g \in \boldsymbol{c}$ this is
$$\stackrel{\circ}{\top} \nabla_{\hat{n}} B_{a b}-4 \bar{C}_{c(a b)} \bar{\nabla}^{c} H+4 H \bar{B}_{a b} .$$
The Poincaré-Einstein condition in six dimensions gives $2 \bar{B}=\left.\stackrel{\circ}{\top} B\right|_{\Sigma}[9]$, and in turn the expression quoted in the theorem. The conformal property ensures that the tensor defines an invariant of the Poincaré-Einstein structure.

Finally, when evaluated on the Graham-Lee compactified metric $g_{r}$ associated with a boundary choice of metric representative $\bar{g} \in \boldsymbol{c}_{\Sigma}$, we must show that $\mathrm{VI}^{\mathrm{DN}}$ agrees with $\mathrm{DN}^{(6)}$. It has already been established in Lemma 3.9 that $\mathrm{DN}^{(6)} \propto \stackrel{\circ}{\top} \nabla_{\hat{n}} B$. Because $g_{r}$ is a Graham-Lee compactified metric, it follows by virtue of Theorem 3.6 that the first, third, and fifth $T$-curvatures
then vanish. In particular, the first $T$-curvature is the mean curvature, so it trivially follows that in this metric representative,
$$\stackrel{\circ}{\mathrm{VI}}^{\mathrm{DN}}=\stackrel{\circ}{\top} \nabla_{\hat{n}} B .$$
The theorem follows. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] P. Albin. Renormalizing curvature integrals on Poincaré-Einstein manifolds. Adv. Math., 221(1):140-169, 2009, arXiv:math/0504161.
\item[] [2] S. Alexakis, On the decomposition of global conformal invariants I. Ann. of Math. (2) 170: 1241-1306, 2009, arXiv:math/0509571.
\item[] [3] S. Alexakis, On the decomposition of global conformal invariants II. Adv. Math. 206: 466-502. (2006), arXiv:math/0509572.
\item[] [4] S. Alexakis and R. Mazzeo, Renormalized area and properly embedded minimal surfaces in hyperbolic 3manifolds. Commun. Mathematical Phys., 297(3):621-651, (2010), arXiv:0802.2250.
\item[] [5] M. T. Anderson. $L^{2}$ curvature and volume renormalization of AHE metrics on 4-manifolds. Math. Res. Lett., 8(1-2):171-188, 2001, arXiv:math/0011051.
\item[] [6] T. N. Bailey, M. G. Eastwood, and A. R. Gover. Thomas's structure bundle for conformal, projective and related structures. Rocky Mountain J. Math., 24(4):1191-1217, 1994.
\item[] [7] S. Blitz, A sharp characterization of the Willmore invariant, Int. J. Math. 34: 2350054 (2023), arXiv:2112.14378.
\item[] [8] S. Blitz, Toward a classification of conformal hypersurface invariants. J. Math. Phys. 64: 082504 (2023), arXiv: 2212.11711.
\item[] [9] S. Blitz, A. R. Gover, and A. Waldron, Conformal fundamental forms and the asymptotically Poincaré-Einstein condition. Indiana 72: 2215-2284 (2023), arXiv:2107.10381.
\item[] [10] S. Blitz, A. R. Gover, and A. Waldron, Generalized Willmore Energies, $Q$-curvatures, extrinsic Paneitz operators, and extrinsic Laplacian powers. Commun. Contemp. Math. 26, 2350014 (2024), arXiv:2111.00179.
\item[] [11] S.-Y. A. Chang, J. Qing, and P. Yang. Renormalized volumes for conformally compact Einstein manifolds. J. Math. Sci. (N.Y.), 149(6): 1755-1769, 2008, arXiv:math/0512376.
\item[] [12] P. Cherrier. Problèmes de Neumann non linéaires sur les variétés Riemanniennes. J. Funct. Anal., 57(2):154-206, 1984.
\item[] [13] S. N. Curry and A. R. Gover. An introduction to conformal geometry and tractor calculus, with a view to applications in general relativity. In Asymptotic analysis in general relativity, volume 443 of London Math. Soc. Lecture Note Ser., pages 86-170. Cambridge Univ. Press, Cambridge, 2018.
\item[] [14] S. de Haro, K. Skenderis and S. Solodukhin,, Holographic Reconstruction of Spacetime and Renormalization in the AdS/CFT Correspondence, Commun. Math. Phys. 217: 595-622 (2001), arXiv:hep-th/0002230.
\item[] [15] S. Deser and A. Schwimmer, Geometric classification of conformal anomalies in arbitrary dimensions. Phys. Lett. B 309: 279-284 (1993), arXiv:hep-th/9302047.
\item[] [16] C. Fefferman and C. R. Graham. Conformal invariants. Number Numéro Hors Série, pages 95-116. 1985. The mathematical heritage of Élie Cartan (Lyon, 1984).
\item[] [17] C. Fefferman and C. R. Graham. The ambient metric, volume 178 of Annals of Mathematics Studies. Princeton University Press, Princeton, NJ, 2012, arXiv:0710.0919.
\item[] [18] A. R. Gover. Invariant theory and calculus for conformal geometries. Adv. Math., 163(2):206-257, 2001.
\item[] [19] A. R. Gover. Almost Einstein and Poincaré-Einstein manifolds in Riemannian signature. J. Geom. Phys., 60(2):182-204, 2010, arXiv:0803.3510.
\item[] [20] A. R. Gover, and J. Kopiński. Higher fundamental forms of the conformal boundary of asymptotically de Sitter spacetimes. Class. Quantum Grav. 40: 015001, 2023: arXiv:2208.09302.
\item[] [21] A. R. Gover and L. J. Peterson. Conformally invariant powers of the Laplacian, $Q$-curvature, and tractor calculus. Comm. Math. Phys., 235(2):339-378, 2003, arXiv:math-ph/0201030.
\item[] [22] A. R. Gover and L. J. Peterson. Conformal boundary operators, $t$-curvatures, and conformal fractional Laplacians of odd order. Pac. J. Math. 311: 277-32, 2021, arXiv:1802.08366.
\item[] [23] A. R. Gover and A. Waldron. Boundary calculus for conformally compact manifolds. Indiana Univ. Math. J., 63(1):119-163, 2014.
\item[] [24] A. Rod Gover and A. Waldron. Renormalized Volume. Commun. Math. Phys., 354:1205-1244, 2017.
\item[] [25] A. Rod Gover and A. Waldron. Conformal hypersurface geometry via a boundary Loewner-Nirenberg-Yamabe problem. Commun. Anal. Geom., 29(4):779-836, 2021.
\item[] [26] C. R. Graham. Volume and area renormalizations for conformally compact Einstein metrics, Proceedings of the 19th Winter School Geometry and Physics (Srní, 1999). Rend. Circ. Mat. Palermo (2) Suppl. No. 63: 31-42 2000, arXiv:math/9909042.
\item[] [27] C. R. Graham. Dirichlet-to-Neumann map for Poincaré-Einstein metrics. Oberwolfach Reports 2, 2200-2203, 2005.
\end{itemize}
[28] C. R. Graham, R. Jenne, L. Mason, G. A. J. Sparling, Conformally invariant powers of the Laplacian. I. Existence, J. London Math. Soc. (2), 46: 557-565, 1992.
[29] C. R. Graham and J. M. Lee. Einstein metrics with prescribed conformal infinity on the ball. Adv. Math., 87(2):186-225, 1991.
[30] C. R. Graham and E. Witten. Conformal anomaly of submanifold observables in AdS/CFT correspondence. Nucl. Phys. B 546: 52-64 1999, arXiv:hep-th/9901021.
[31] C. R. Graham and M. Zworski. Scattering matrix in conformal geometry. Invent. Math., 152(1):89-118, 2003, arXiv:math/0109089.
[32] M. Henningson and K. Skenderis. The holographic Weyl anomaly. J. High Energy Phys., (7):Paper 23, 12, 1998, arXiv:hep-th/9806087.
[33] Y. Herfray Tractor geometry of asymptotically flat spacetimes Ann. Henri Poincaré, 23(9): 3265-3310, 2022, arXiv:2103.10405.
[34] C. R. LeBrun. $\mathcal{H}$-space with a cosmological constant. Proc. Roy. Soc. London Ser. A, 380(1778):171-185, 1982.
[35] J. Maldacena. The large $N$ limit of superconformal field theories and supergravity. Adv. Theor. Math. Phys., 2(2):231-252, 1998, arXiv:hep-th/9711200.
[36] J. Marx-Kuo, Variations of Renormalized Volume for Minimal Submanifolds of Poincaré-Einstein Manifolds. Commun. Anal. Geom. 33 17-29, 2025: arXiv:2111.04294.
[37] F. Wang. Dirichlet-to-Neumann Map for Poincaré-Einstein Metrics in Even Dimensions. Calc. Var. Partial Differ. Equ. 58(1): 9-39, 2019, arXiv:0905.2457.

◇ Department of Mathematics and Statistics, Masaryk University, Building 08, Kotlárská 2, Brno, CZ 61137
Email address: blitz@math.muni.cz
${ }^{\circ}$ Department of Mathematics, The University of Auckland, Private Bag 92019, Auckland 1142, New Zealand, and, Mathematical Sciences Institute, Australian National University, ACT 0200, Australia
Email address: r.gover@auckland.ac.nz
* Center for Theoretical Physics, Polish Academy of Sciences, Warsaw, Poland
Email address: jkopinski@cft.edu.pl
* Center for Quantum Mathematics and Physics (QMAP), Department of Mathematics, University of California, Davis, CA95616, USA
Email address: wally@math.ucdavis.edu
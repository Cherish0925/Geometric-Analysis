---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: [2107.00354] On the stability of homogeneous Einstein manifolds II]

The two $G$-stable standard metrics found on $E_{7} / \operatorname{SO}(8)$ and $E_{8} /(\operatorname{Spin}(8) \times \operatorname{Spin}(8))$ deserve special attention, note that they are in particular local maxima of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$. We do not know whether these Einstein metrics are stable in the classical sense (see Remark 1.1). We do not know whether they realize the Yamabe invariant either.
4.2. Case $d_{1}=d_{2} \neq d_{3}$. We set $b:=a_{1}=a_{2}$ and $c:=a_{3}$. According to LNF, Theorem 4], under this assumption, $G / K$ admits at most four $G$-invariant Einstein metrics given by:
\begin{itemize}
\item[-] $g_{q^{ \pm}}=\left(1,1, q^{ \pm}\right)$, where
$$q^{ \pm}=\frac{1 \pm \sqrt{1-4(b+c)(1-2 c)}}{2(b+c)},$$
\item[-] $g_{p^{ \pm}}=\left(p^{ \pm}, 1,2 b\left(p^{ \pm}+1\right)\right)$, where
$$p^{ \pm}=\frac{-1+2 b-8 b^{2}(b+c) \pm \sqrt{\left(1-2 b+8 b^{2}(b+c)\right)^{2}-4(b+c)^{2}\left(1-4 b^{2}\right)^{2}}}{2(b+c)\left(1-4 b^{2}\right)} .$$
\end{itemize}

Note that $p^{+} p^{-}=1$ and $1<p^{+}$. The radicand is positive if and only if
$$T:=1-2(2 b+c)+16 b^{2}(b+c)>0 .$$
It is worth pointing out that the non-negativity of the radicands is a necessary condition for the existence of the corresponding metric, which may o may not hold.

For the family $W_{1}$ with $l=m$, it is easy to see that
$$T=\frac{-2 k^{2}+2(k+m)(m-2)^{2}+8(m-1)}{(k+2 m-2)^{3}},$$
and
$$p^{ \pm}=\frac{5 m^{3}+(9 k-16) m^{2}+\left(20+5 k^{2}-20 k\right) m+k^{3}-6 k^{2}-8+12 k \pm 2(2 m+k-2) \sqrt{D_{1}(k, m)}}{(k-2+m)(k-2+3 m)(k+m)},$$
where
$$D_{1}(k, m):=\frac{1}{2}(k-1+m)(k+2 m-2)^{3} T,$$
which is positive if and only if $T>0$.
On the other hand, for $W_{3}$ with $l=m$,
$$p^{ \pm}=\frac{10 m k+5 m^{3}+5 m k^{2}+9 m^{2} k+(k+1)^{3}+5 m+8 m^{2} \pm(2 m+k+1) \sqrt{D_{2}(k, m)}}{(k+1+3 m)(k+1+m)(m+k)},$$
where
$$D_{2}(k, m):=(2 k+1+2 m)\left((k+1)^{2}+4 m k+2 m^{2} k+2 m^{3}+4 m^{2}+4 m\right),$$
is always positive. All these metrics have been listed in Table 4 and the values of $\operatorname{Sc}_{N}(g)$ are given in Table 5.

We compute next the spectrum of $\mathrm{L}_{\mathfrak{p}}$ for each of these metrics. For $q=q^{ \pm}$, we have that $2 \rho=1-b q$ by (18), and from (23) we obtain that
$$L_{\mathfrak{p}}\left(g_{q}\right)=\left[\begin{array}{ccc}
\frac{2 b}{q} & \frac{b\left(q^{2}-2\right)}{q} & -\sqrt{b c} q \\
\frac{b\left(q^{2}-2\right)}{q} & \frac{2 b}{q} & -\sqrt{b c} q \\
-\sqrt{b c} q & -\sqrt{b c} q & 2 c q
\end{array}\right], \quad \operatorname{Spec}\left(\mathrm{L}_{\mathfrak{p}}\right)=\left\{0, \frac{b\left(4-q^{2}\right)}{q}, q(b+2 c)\right\} .$$
For $p=p^{ \pm}$, one obtains from (18) that $2 \rho=\frac{(1+p)\left(1-4 b^{2}\right)}{2 p}$ and it follows from (23) that
$$L_{\mathfrak{p}}\left(g_{p}\right)=\left[\begin{array}{ccc}
\frac{p}{p+1} & \frac{4 b^{2} p^{2}+8 b^{2} p+4 b^{2}-p^{2}-1}{2 p(p+1)} & -\frac{\sqrt{c}\left(4 b^{2} p+p+4 b^{2}-1\right)}{2 p \sqrt{b}} \\
\frac{4 b^{2} p^{2}+8 b^{2} p+4 b^{2}-p^{2}-1}{2 p(p+1)} & \frac{1}{p(p+1)} & -\frac{\sqrt{c}\left(4 b^{2} p-p+4 b^{2}+1\right)}{2 p \sqrt{b}} \\
-\frac{\sqrt{c}\left(4 b^{2} p+p+4 b^{2}-1\right)}{2 p \sqrt{b}} & -\frac{\sqrt{c}\left(4 b^{2} p-p+4 b^{2}+1\right)}{2 p \sqrt{b}} & \frac{4 b c(p+1)}{p}
\end{array}\right] .$$
It is therefore straightforward to check that the spectrum is given by
$$\operatorname{Spec}\left(\mathrm{L}_{\mathfrak{p}}\right)=\left\{0, \frac{4 c b^{2}(p+1)^{2}+b\left(p^{2}+1\right) \pm \sqrt{2 b D(p)}}{2 b p(p+1)}\right\},$$
where $D(p):=c_{4} p^{4}+c_{3} p^{3}+c_{2} p^{2}+c_{3} p+c_{4}$ and
$$\begin{gathered}
c_{4}=(b+c)\left(8 b^{3} c+1-4 b^{2}+8 b^{4}\right), \quad c_{3}=8 b^{2}(b+c)\left(4 b c+4 b^{2}-1\right), \\
c_{2}=96 c b^{4}-8 b^{3}+48 c^{2} b^{3}+48 b^{5}-2 c-8 c b^{2} .
\end{gathered}$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline $W_{i}$ & $\mathfrak{g} / \mathfrak{k}$ & $b$ & $c$ & $g$ \\
\hline $W_{1}$ & $\frac{\mathfrak{s} \mathfrak{o}(4)}{\mathfrak{s} \mathfrak{o}(2)}$ & $\frac{1}{4}$ & $\frac{1}{2}$ & $$\begin{gathered}
q^{+}=\frac{4}{3} \\
g_{\times}(\text {see Ex. } 3.8)
\end{gathered}$$ \\
\hline $W_{1}$ & $$\begin{gathered}
\frac{\mathfrak{s} \mathfrak{o}(k+2)}{\mathfrak{s} \mathfrak{o}(k)} \\
k \geq 3
\end{gathered}$$ & $\frac{1}{2 k}$ & $\frac{1}{2}$ & $q^{+}=\frac{2 k}{k+1}$ (see Ex. 3.7) \\
\hline $W_{1}$ & $$\begin{gathered}
\frac{\mathfrak{s} \mathfrak{o}(k+2 m)}{\mathfrak{s} \mathfrak{o}(k) \oplus \mathfrak{2} \mathfrak{s} \mathfrak{o}(m)} \\
m \geq 3
\end{gathered}$$ & $\frac{m}{2(k+2 m-2)}$ & $\frac{k}{2(k+2 m-2)}$ & $$\begin{gathered}
q^{ \pm}=\frac{k+2 m-2 \pm \sqrt{k^{2}-4 m+4}}{k+m} \\
p^{ \pm}(\operatorname{see}(26))
\end{gathered}$$ \\
\hline $W_{2}$ & $\frac{\mathfrak{s u}(k+2 m)}{\mathfrak{s}(\mathfrak{u}(k) \oplus 2 \mathfrak{u}(m))}$ & $\frac{m}{2(k+2 m)}$ & $\frac{k}{2(k+2 m)}$ & $$\begin{gathered}
q^{+}=2 \\
q^{-}=\frac{2 m}{k+m} \\
p^{+}=\frac{k+3 m}{k+m} \\
p^{-}=\frac{k+m}{k+3 m}
\end{gathered}$$ \\
\hline $W_{3}$ & $\frac{\mathfrak{s p}(k+2 m)}{\mathfrak{s p}(k) \oplus 2 \mathfrak{s p}(m)}$ & $\frac{m}{2(k+2 m+1)}$ & $\frac{k}{2(k+2 m+1)}$ & $$\begin{gathered}
q^{ \pm}=\frac{k+2 m+1 \pm \sqrt{k^{2}+2 m+1}}{k+m} \\
p^{ \pm}(\operatorname{see}(27))
\end{gathered}$$ \\
\hline $W_{5}$ & $$\begin{gathered}
\frac{\mathfrak{s} \mathfrak{o}(2 l)}{\mathfrak{u}(1) \oplus \mathfrak{u}(l-1)} \\
l \geq 5
\end{gathered}$$ & $\frac{l-2}{4(l-1)}$ & $\frac{1}{2(l-1)}$ & $$\begin{gathered}
q^{+}=2 \\
q^{-}=\frac{2(l-2)}{l} \\
p^{+}=\frac{3 l-4}{l} \\
p^{-}=\frac{l}{3 l-4}
\end{gathered}$$ \\
\hline $W_{6}$ & $\frac{\mathfrak{e}_{6}}{\mathfrak{s} \mathfrak{u}(4) \oplus 2 \mathfrak{s} \mathfrak{p}(1) \oplus \mathbb{R}}$ & $\frac{1}{4}$ & $\frac{1}{6}$ & $$\begin{aligned}
& p^{+}=\frac{5}{3} \\
& p^{-}=\frac{3}{5}
\end{aligned}$$ \\
\hline $W_{12}$ & $\frac{\mathfrak{e}_{8}}{\mathfrak{s} \mathfrak{o}(12) \oplus 2 \mathfrak{s} \mathfrak{p}(1)}$ & $\frac{1}{5}$ & $\frac{4}{15}$ & $$\begin{aligned}
& q^{+}=\frac{15+\sqrt{29}}{14} \\
& q^{-}=\frac{15-\sqrt{29}}{14}
\end{aligned}$$ \\
\hline $W_{14}$ & $\frac{\mathfrak{f}_{4}}{\mathfrak{s} \mathfrak{o}(5) \oplus 2 \mathfrak{s} \mathfrak{p}(1)}$ & $\frac{5}{18}$ & $\frac{1}{9}$ & $$\begin{aligned}
& p^{+}=\frac{499+9 \sqrt{1177}}{392} \\
& p^{-}=\frac{499-9 \sqrt{1177}}{392}
\end{aligned}$$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 4. Einstein metrics on generalized Wallach spaces with $a_{1}=a_{2}=$ $b \neq a_{3}=c$, given by $g_{q^{ \pm}}=\left(1,1, q^{ \pm}\right)$and $g_{p^{ \pm}}=\left(p^{ \pm}, 1,2 b\left(p^{ \pm}+1\right)\right)$ (see [LNF]). Assume that $k \neq m$ everywhere.}
\end{table}

The case $W_{1}$ with $m=1$, i.e., the Stiefel manifold $\operatorname{SO}(k+2) / \operatorname{SO}(k), k \geq 2$, was separately worked out in Example 3.7 since it is not multiplicity-free.

Finally, a straightforward inspection of all the above information gives that either $\lambda_{\mathfrak{p}}<$ $2 \rho<\lambda_{\mathfrak{p}}^{\text {max }}$ or $\lambda_{\mathfrak{p}}^{\text {max }}<2 \rho$ in all cases. This produces Table 6, containing the $G$-stability and critical point types of all the metrics in Table 4.

Remark 4.1. For each space in Table 2, the Einstein metrics $g_{i}$ 's have the same value of $\mathrm{Sc}_{N}$ (see Table 3) and identical eigenvalues of $\mathrm{L}_{\mathfrak{p}}$ up to scaling. The same holds for the two Einstein metrics on $W_{6}$ and $W_{14}$ (see Table 5). As far as we know, the question of

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline $W_{i}$ & $g$ & $\left(\operatorname{det}_{g_{\mathrm{B}}} g\right)^{\frac{1}{n}} \operatorname{Sc}(g)$ \\
\hline $W_{1}$ & $q^{ \pm}$ & $\frac{m(2 k+m)(4 m+2 k-4-m q)}{4(2 m+k-2)} q^{\frac{m}{2 k+m}}$ \\
\hline $m \geq 3$ & $p^{ \pm}$ & $\frac{(p+1) m(2 k+m)\left(3 m^{2}+4 k m-8 m+k^{2}-4 k+4\right)}{4 p(2 m+k-2)^{2}} p^{\frac{m}{2 k+m}}\left(\frac{m(p+1)}{2 m+k-2}\right)^{\frac{k}{2 k m+m^{2}}}$ \\
\hline \multirow{4}{*}{$W_{2}$} & $q^{+}$ & $\frac{m(2 k+m)(m+k)}{(2 m+k)} 2^{\frac{m}{2 k+m}}$ \\
\hline & $q^{-}$ & $\frac{m(2 k+m)\left(m^{2}+3 k m+k^{2}\right)}{(2 m+k)(m+k)}\left(\frac{2 m}{m+k}\right)^{\frac{m}{2 k+m}}$ \\
\hline & $p^{+}$ & $\frac{m(2 k+m)(m+k)}{2 m+k}\left(\frac{3 m+k}{m+k}\right)^{\frac{k}{2 k+m}}\left(\frac{2 m}{m+k}\right)^{\frac{m}{2 k+m}}$ \\
\hline & $p^{-}$ & $\frac{m(2 k+m)(3 m+k)}{2 m+k}\left(\frac{m+k}{3 m+k}\right)^{\frac{k}{2 k+m}}\left(\frac{2 m}{3 m+k}\right)^{\frac{m}{2 k+m}}$ \\
\hline \multirow{2}{*}{$W_{3}$} & $q^{ \pm}$ & $\frac{m(2 k+m)(4 m+2 k+2-m q)}{2 m+k+1} q^{\frac{m}{2 k+m}}$ \\
\hline & $p^{ \pm}$ & $\frac{(p+1) m(2 k+m)\left(3 m^{2}+4 k m+4 m+k^{2}+2 k+1\right)}{p(2 m+k+1)^{2}} p^{\frac{k}{2 k+m}}\left(\frac{m(p+1)}{2 m+k+1}\right)^{\frac{m}{2 k+m}}$ \\
\hline \multirow{2}{*}{$W_{5}$} & $q^{+}$ & $\frac{l(2+l)}{4} 2^{\frac{l-2}{l+2}}$ \\
\hline & $q^{-}$ & $\frac{(2+l)\left(l^{2}+2 l-4\right)}{4 l}\left(\frac{2(l-2)}{l}\right)^{\frac{l-2}{l+2}}$ \\
\hline \multirow{2}{*}{$l \geq 5$} & $p^{+}$ & $\frac{l(2+l)}{4}\left(\frac{3 l-4}{l}\right)^{\frac{2}{l+2}}\left(\frac{2(l-2)}{l}\right)^{\frac{l-2}{l+2}}$ \\
\hline & $p^{-}$ & $\frac{(3 l-4)(2+l)}{4}\left(\frac{l}{3 l-4}\right)^{\frac{2}{l+2}}\left(\frac{2(l-2)}{3 l-4}\right)^{\frac{l-2}{l+2}}$ \\
\hline \multirow{2}{*}{$W_{6}$} & $p^{+}$ & $\frac{28}{5}(120)^{\frac{2}{7}} \approx 21.9907$ \\
\hline & $p^{-}$ & $\frac{28}{5}(120)^{\frac{2}{7}} \approx 21.9907$ \\
\hline \multirow{2}{*}{$W_{12}$} & $q^{+}$ & $\approx 69.1037$ \\
\hline & $q^{-}$ & $\approx 68.5187$ \\
\hline \multirow[t]{2}{*}{$W_{14}$} & $p^{+}$ & $\approx 14.5750$ \\
\hline & $p^{-}$ & $\approx 14.5750$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 5. Volume normalized scalar curvature of Einstein metrics in Table 4. In cases $W_{1}$ and $W_{3}$ we set $q:=q^{ \pm}$and $p:=p^{ \pm}$.}
\end{table}
whether these metrics are homothetic (i.e., isometric up to scaling) or not remains open, except for few particular cases.
4.3. Case $d_{1}, d_{2}, d_{3}$ pairwise different. This case will be treated partially, since the Einstein metrics are not available in the literature for all the spaces. It follows from [CKL] that in the case $W_{2}$ (with $k, l, m$ pairwise different), $G / K$ admits exactly four $G$-invariant Einstein metrics up to scaling (see also [LNF, Theorem 5]):
$$\begin{array}{ll}
g_{0}=(l+m, k+m, k+l), & g_{k}=(l+m+2 k, k+m, k+l), \\
g_{l}=(l+m, k+2 l+m, k+l), & g_{m}=(l+m, k+m, k+l+2 m) .
\end{array}$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $W_{i}$ & $g$ & $\lambda_{\mathfrak{p}}$ & $\lambda_{\mathfrak{p}}^{\max }$ & $2 \rho$ & Type \\
\hline \multirow{2}{*}{$W_{1}$} & $g_{q^{+}}$ & $\frac{5}{12}$ & $\frac{5}{3}$ & $\frac{2}{3}$ & saddle \\
\hline & $g_{\times}$ & & & & saddle \\
\hline $W_{1}$ & $$\begin{gathered}
g_{q^{+}} \\
k \geq 3, m=2
\end{gathered}$$ & $\frac{2 k+1}{k^{2}(k+1)}$ & $\frac{2 k+1}{k+1}$ & $\frac{k}{k+1}$ & saddle \\
\hline \multirow{5}{*}{$W_{1}$} & $$g_{q^{+}}$$ & $$\frac{m\left(4-q^{2}\right)}{2(k+2 m-2) q}$$ & $$\frac{q(2 k+m)}{2(k+2 m-2)}$$ & $$\frac{2(k+2 m-2)-m q}{2(k+2 m-2)}$$ & saddle \\
\hline & $$\begin{gathered}
g_{q^{-}}, T>0 \\
k<m
\end{gathered}$$ & $\frac{m\left(4-q^{2}\right)}{2(k+2 m-2) q}$ & $\frac{q(2 k+m)}{2(k+2 m-2)}$ & $\frac{2(k+2 m-2)-m q}{2(k+2 m-2)}$ & loc.min. \\
\hline & $$\begin{gathered}
g_{q^{-}}, T>0 \\
k>m
\end{gathered}$$ & $\frac{q(2 k+m)}{2(k+2 m-2)}$ & $\frac{m\left(4-q^{2}\right)}{2(k+2 m-2) q}$ & $\frac{2(k+2 m-2)-m q}{2(k+2 m-2)}$ & loc.min. \\
\hline & $$g_{q^{-}}, T<0$$ & $$\frac{q(2 k+m)}{2(k+2 m-2)}$$ & $$\frac{m\left(4-q^{2}\right)}{2(k+2 m-2) q}$$ & $$\frac{2(k+2 m-2)-m q}{2(k+2 m-2)}$$ & saddle \\
\hline & $g_{p^{ \pm}}$ & see (28) & see (28) & $\frac{\left(1+p^{ \pm}\right)\left(1-4 b^{2}\right)}{2 p^{ \pm}}$ & saddle \\
\hline \multirow{5}{*}{$W_{2}$} & $g_{q^{+}}$ & 0 & $$\frac{2 k+m}{k+2 m}$$ & $$\frac{k+m}{k+2 m}$$ & saddle \\
\hline & $$g_{q^{-}}, k<m$$ & $$\frac{k}{k+m}$$ & $$\frac{m(2 k+m)}{(k+2 m)(k+m)}$$ & $$\frac{k^{2}+m^{2}+3 k m}{(k+m)(k+2 m)}$$ & loc.min. \\
\hline & $g_{q^{-}}, k>m$ & $$\frac{m(2 k+m)}{(k+2 m)(k+m)}$$ & $$\frac{k}{k+m}$$ & $$\frac{k^{2}+m^{2}+3 k m}{(k+m)(k+2 m)}$$ & loc.min. \\
\hline & $g_{p^{+}}$ & 0 & $$\frac{(k+5 m)(k+m)}{(2 m+k)(k+3 m)}$$ & $$\frac{m+k}{k+2 m}$$ & saddle \\
\hline & $g_{p^{-}}$ & 0 & $\frac{k+5 m}{k+2 m}$ & $\frac{k+3 m}{k+2 m}$ & saddle \\
\hline \multirow{4}{*}{$W_{3}$} & $g_{q^{+}}$ & $$\frac{m\left(4-q^{2}\right)}{2 q(k+2 m+1)}$$ & $$\frac{q(2 k+m)}{2(k+2 m+1)}$$ & $$\frac{2(k+2 m+1)-m q}{2(k+2 m+1)}$$ & saddle \\
\hline & $$g_{q^{-}}, k<m$$ & $$\frac{m\left(4-q^{2}\right)}{2 q(k+2 m+1)}$$ & $$\frac{q(2 k+m)}{2(k+2 m+1)}$$ & $$\frac{2(k+2 m+1)-m q}{2(k+2 m+1)}$$ & loc.min. \\
\hline & $g_{q^{-}}, k>m$ & $$\frac{q(2 k+m)}{2(k+2 m+1)}$$ & $$\frac{m\left(4-q^{2}\right)}{2 q(k+2 m+1)}$$ & $$\frac{2(k+2 m+1)-m q}{2(k+2 m+1)}$$ & loc.min. \\
\hline & $g_{p^{ \pm}}$ & see (28) & see (28) & $\frac{\left(1+p^{ \pm}\right)\left(1-4 b^{2}\right)}{2 p^{ \pm}}$ & saddle \\
\hline \multirow{4}{*}{$W_{5}$} & $g_{q^{+}}$ & 0 & $\frac{l+2}{2(l-1)}$ & $\frac{l}{2(l-1)}$ & saddle \\
\hline & $g_{q^{-}}$ & $\frac{2}{l}$ & $\frac{l^{2}-4}{2 l(l-1)}$ & $\frac{l^{2}+2 l-4}{2 l(l-1)}$ & loc.min. \\
\hline & $g_{p^{+}}$ & 0 & $\frac{l(5 l-8)}{2\left(3 l^{2}-7 l+4\right)}$ & $\frac{l}{2(l-1)}$ & saddle \\
\hline & $g_{p^{-}}$ & 0 & $\frac{5 l-8}{2(l-1)}$ & $\frac{3 l-4}{2(l-1)}$ & saddle \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 6. Einstein metrics in Table 4 on the spaces $W_{1}-W_{5}$ (see (25) for the value of $T$ in case $W_{1}$ ). They are all $G$-unstable and $G$-non-degenerate. Any $g_{q^{-}}$is a local minimum with coindex 2 and the rest are all saddle points with coindex 1, except $g_{q^{+}}$on $W_{1}(m=2)$, which has coindex 3 if $k=2$ and coindex 2 if $k \geq 3$ (see Examples 3.7 and 3.8). Note that $g_{q}-$ is the non-Kähler Einstein metric on the flag manifolds $W_{2}$ and $W_{5}$, the other three are Kähler-Einstein.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $W_{i}$ & $g$ & $\lambda_{\mathfrak{p}}$ & $\lambda_{\mathfrak{p}}^{\text {max }}$ & $2 \rho$ & Type \\
\hline \multirow{2}{*}{$W_{6}$} & $g_{p^{+}}$ & $\frac{67-\sqrt{1465}}{120} \approx 0.2393$ & $\frac{67+\sqrt{1465}}{120} \approx 0.8772$ & $\frac{3}{5}=0.6$ & saddle \\
\hline & $g_{p^{-}}$ & $\frac{67-\sqrt{1465}}{72} \approx 0.3989$ & $\frac{67+\sqrt{1465}}{72} \approx 1.4621$ & 1 & saddle \\
\hline \multirow{2}{*}{$W_{12}$} & $g_{q^{+}}$ & $\frac{9-\sqrt{29}}{14} \approx 0.2582$ & $\frac{165+11 \sqrt{29}}{210} \approx 1.0677$ & $\frac{55-\sqrt{29}}{70} \approx 0.7087$ & saddle \\
\hline & $g_{q-}$ & $\frac{165-11 \sqrt{29}}{210} \approx 0.5036$ & $\frac{9+\sqrt{29}}{14} \approx 1.0275$ & $\frac{55+\sqrt{29}}{70} \approx 0.8626$ & saddle \\
\hline \multirow{2}{*}{$W_{14}$} & $g_{p+}$ & 0.1494 & 0.8657 & $\frac{28(99+\sqrt{1177})}{9(499+\sqrt{1177})} \approx 0.5134$ & saddle \\
\hline & $g_{p^{-}}$ & 0.3080 & 1.7839 & $\frac{28(99-\sqrt{1177})}{9(499-\sqrt{1177})} \approx 1.0579$ & saddle \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 7. Einstein metrics in Table 4 on the spaces $W_{6}, W_{12}$ and $W_{14}$. They are all $G$-unstable and $G$-non-degenerate saddle points with coindex 1.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $W_{i}$ & $\mathfrak{g} / \mathfrak{k}$ & $g$ & $\lambda_{\mathfrak{p}}$ & $\lambda_{\mathfrak{p}}^{\text {max }}$ & $2 \rho$ \\
\hline \multirow{4}{*}{$W_{2}$} & \multirow{4}{*}{$\frac{\mathfrak{s u}(k+l+m)}{\mathfrak{s}(\mathfrak{u}(k) \oplus \mathfrak{u}(l) \oplus \mathfrak{u}(m))}$} & $g_{0}$ & see (30) & see (30) & see (29) \\
\hline & & $g_{k}$ & 0 & $\frac{4 k+l+m}{(k+l+m)(2 k+l+m)}$ & $\frac{1}{k+l+m}$ \\
\hline & & $g_{l}$ & 0 & $\frac{k+4 l+m}{(k+l+m)(k+2 l+m)}$ & $\frac{1}{k+m+l}$ \\
\hline & & $g_{m}$ & 0 & $\frac{k+l+4 m}{(k+l+m)(k+l+2 m)}$ & $\frac{1}{k+m+l}$ \\
\hline \multirow[t]{2}{*}{$W_{8}$} & \multirow[t]{2}{*}{$\frac{\mathfrak{e}_{6}}{\mathfrak{s} \mathfrak{p}(3) \oplus \mathfrak{s p}(1)}$} & $g_{1}=(1,1.4618,1.8845)$ & 0.1605 & 0.9669 & 0.5745 \\
\hline & & $g_{2}=(1,0.8640,0.4838)$ & 0.3464 & 1.6227 & 1.0116 \\
\hline \multirow{2}{*}{$W_{10}$} & \multirow[t]{2}{*}{$\frac{\mathfrak{e}_{7}}{\mathfrak{s} \mathfrak{u}(6) \oplus \mathfrak{s} \mathfrak{p}(1) \oplus \mathbb{R}}$} & $g_{1}=(1,0.8882,0.5717)$ & 0.4354 & 1.3150 & 0.9492 \\
\hline & & $g_{2}=(1,1.1896,1.6291)$ & 0.2118 & 1.0217 & 0.6480 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{TABLE 8. Einstein metrics on some generalized Wallach spaces with $a_{i} \neq$ $a_{j}$ for $i \neq j$ (see [CKL] and [LNF]). In case $W_{2}, k, l, m$ are pairwise different and for $W_{8}$ and $W_{10}$ the numbers are all approximate values. All these metrics are $G$-unstable and $G$-non-degenerate. The non-Kähler metric $g_{0}$ on the flag manifold $W_{2}$ (note that the other three are Kähler-Einstein) has coindex 2 (i.e., $\lambda_{\mathfrak{p}}^{\max }<2 \rho$ ), so it is a local minimum, and the rest are all saddle points of coindex 1 (i.e., $\lambda_{\mathfrak{p}}<2 \rho<\lambda_{\mathfrak{p}}^{\text {max }}$ ). See Example 4.2 for $W_{4}$.}
\end{table}

For $g_{0}$ one obtains from (18) that
$$2 \rho=\frac{(k+l)(k+m)(l+m)+2 k l m}{(k+l+m)(k+l)(k+m)(l+m)},$$
and from (23) that
$$\operatorname{Spec}\left(\mathrm{L}_{\mathfrak{p}}\left(g_{0}\right)\right)=\left\{0, \frac{(k+l)(k+m)(l+m)+4 k l m \pm \sqrt{P(k, l, m)}}{2(k+l+m)(k+l)(k+m)(l+m)}\right\},$$
where
$$P(k, l, m)=(k+l)(k+m)(l+m)((k+l)(k+m)(l+m)-8 k l m) .$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $G / K$ & $g$ & $\left(x_{1}, x_{2}, x_{3}\right)$ & $\left(\operatorname{det}_{g_{\mathrm{B}}} g\right)^{\frac{1}{n}} \operatorname{Sc}(g)$ \\
\hline \multirow{3}{*}{$\frac{E_{8}}{E_{6} \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3) & $\frac{1577}{30} 1207959552^{\frac{1}{83}} \approx 67.6289$ \\
\hline & $g_{1}$ & (1, 0.914286, 1.54198) & 66.9159 \\
\hline & $g_{2}$ & (1,1.0049, 0.129681) & 65.6151 \\
\hline \multirow{3}{*}{$\frac{E_{8}}{\mathrm{SU}(8) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3) & $\frac{782}{15} 1152^{\frac{1}{23}} \approx 70.8307$ \\
\hline & $g_{1}$ & (1, 0.717586, 1.25432) & 69.5453 \\
\hline & $g_{2}$ & (1,1.06853, 0.473177) & 69.1155 \\
\hline \multirow{3}{*}{$\frac{E_{7}}{\mathrm{SU}(5) \times \mathrm{SU}(3) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3) & $\frac{250}{9} 24^{\frac{1}{10}} \approx 38.1696$ \\
\hline & $g_{1}$ & (1, 0.678535, 1.201221) & 37.4141 \\
\hline & $g_{2}$ & (1, 1.090568, 0.546044) & 37.3277 \\
\hline \multirow{3}{*}{$\frac{E_{7}}{\mathrm{SU}(6) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3) & $\frac{517}{18} 294912^{\frac{1}{47}} \approx 37.5486$ \\
\hline & $g_{1}$ & (1, 0.85368, 1.45259) & 37.0717 \\
\hline & $g_{2}$ & (1,1.01573, 0.229231) & 36.4084 \\
\hline \multirow{3}{*}{$\frac{E_{6}}{\mathrm{SU}(3) \times \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3) & $\frac{203}{12} 4608^{\frac{1}{29}} \approx 22.6278$ \\
\hline & $g_{1}$ & (1, 0.771752, 1.33186) & 22.2677 \\
\hline & $g_{2}$ & (1, 1.04268, 0.373467) & 22.0134 \\
\hline \multirow{3}{*}{$\frac{F_{4}}{\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3) & $\frac{100}{9} 24^{\frac{1}{10}} \approx 15.2678$ \\
\hline & $g_{1}$ & (1, 0.678535, 1.201221) & 14.9656 \\
\hline & $g_{2}$ & (1, 1.090568, 0.546044) & 14.9311 \\
\hline \multirow{3}{*}{$\frac{G_{2}}{\mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3) & $\frac{25}{12} 18^{\frac{1}{5}} \approx 3.7137$ \\
\hline & $g_{1}$ & (1, 1.67467, 2.05238) & 3.7104 \\
\hline & $g_{2}$ & (1, 0.186894, 0.981478) & 3.4422 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 9. Einstein metrics on flag manifolds with $b_{2}(M)=1$ and $r=3$ (see [AC1]). On the fourth row, the embedding of $\mathrm{SU}(6) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ on $E_{7}$ is different from the one for the generalized Wallach space $W_{10}$.}
\end{table}
For the others metrics on $W_{2}$, as well as for the cases $W_{8}$ and $W_{10}$, which both admit exactly two Einstein metrics (see [CKL]), we proceeded as above and all the information has been collected in Table 8. The volume normalized scalar curvature of the metrics on $W_{8}$ and $W_{10}$ are given by
$$\begin{gathered}
\mathrm{Sc}_{N}\left(W_{8}, g_{1}\right) \approx 21.7434, \quad \mathrm{Sc}_{N}\left(W_{8}, g_{2}\right) \approx 21.5470, \\
\mathrm{Sc}_{N}\left(W_{10}, g_{1}\right) \approx 36.7796, \quad \mathrm{Sc}_{N}\left(W_{10}, g_{2}\right) \approx 37.1468 .
\end{gathered}$$
Example 4.2. It is proved in [CKL, Section 4.1] that $W_{4}=\operatorname{SU}(2 l) / \mathrm{U}(l), l \geq 2$, admits exactly two Einstein metrics, given by $g=\left(1, x_{2}, x_{3}\right)$, where $x_{3}$ is one of the only two

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $G / K$ & $g$ & $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$ & $\left(\operatorname{det}_{g_{\mathrm{B}}} g\right)^{\frac{1}{n}} \operatorname{Sc}(g)$ \\
\hline \multirow{3}{*}{$\frac{F_{4}}{\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3,4) & $\frac{70}{9} 24^{\frac{1}{10}} \approx 14.5995$ \\
\hline & $g_{1}$ & (1, 1.2761, 1.9578, 2.3178) & 14.5693 \\
\hline & $g_{2}$ & (1, 0.9704, 0.2291, 1.0097) & 14.0370 \\
\hline \multirow{3}{*}{$\frac{E_{7}}{\mathrm{SU}(4) \times \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3,4) & $\frac{212}{9} 24^{\frac{8}{53}} \approx 38.0563$ \\
\hline & $g_{1}$ & (1, 0.8233, 1.2942, 1.3449) & 37.6284 \\
\hline & $g_{2}$ & (1, 0.9912, 0.5783, 1.1312) & 37.3618 \\
\hline \multirow{3}{*}{$\frac{E_{8}}{\mathrm{SU}(7) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3,4) & $\frac{637}{15} \sqrt{2} 3^{\frac{1}{7}} \approx 70.2624$ \\
\hline & $g_{1}$ & (1, 0.9133, 1.4136, 1.5196) & 69.6567 \\
\hline & $g_{2}$ & (1, 0.9663, 0.4898, 1.0809) & 68.8049 \\
\hline \multirow{5}{*}{$\frac{E_{8}}{\mathrm{SU}(10) \times \mathrm{SU}(3) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3,4) & $\frac{658}{15} 41472^{\frac{2}{47}} \approx 68.9659$ \\
\hline & $g_{1}$ & (1, 0.6496, 1.1094, 1.0610) & 66.5752 \\
\hline & $g_{2}$ & (1, 1.1560, 1.0178, 0.2146) & 66.1753 \\
\hline & $g_{3}$ & (1, 1.0970, 0.7703, 1.2969) & 66.9855 \\
\hline & $g_{4}$ & (1, 0.7633, 1.0090, 0.1910) & 65.7898 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{TABLE 10. Einstein metrics on flag manifolds with $b_{2}(M)=1$ and $r=4$ (see [ArC]).}
\end{table}
positive roots of the quartic polynomial
$$12 l^{4} x^{4}-(48 l-8) l^{3} x^{3}+\left(72 l^{2}-36 l-4\right) l^{2} x^{2}-\left(48 l^{3}-48 l^{2}+4 l+4\right) l x+12 l^{4}-20 l^{3}+7 l^{2}+2 l-1,$$
and
$$x_{2}=\frac{2 l^{2} x_{3}^{2}+2 l x_{3}+1-l-2 l^{2}}{2 l\left(2 l x_{3}-2 l+1\right)} .$$
Using respectively (23) and (18), it is straightforward to check that both metrics satisfy:
$$\left\{\lambda_{\mathfrak{p}}, \lambda_{\mathfrak{p}}^{\max }\right\}=\frac{(l-1) x_{2}^{2}+(l+1) x_{3}^{2}+l \pm \sqrt{Q\left(l, x_{2}, x_{3}\right)}}{4 l x_{2} x_{3}}, \quad 2 \rho=\frac{1+4 x_{2} x_{3}-x_{2}^{2}-x_{3}^{2}}{4 x_{2} x_{3}},$$
where
$$Q\left(l, x_{2}, x_{3}\right)=\left(2 l+4 l^{2}\right) x_{3}^{4}+\left(2-4 l^{2}-4 l^{2} x_{2}^{2}+2 l\right) x_{3}^{2}-1+2 x_{2}^{2}-2 l x_{2}^{2}-4 l^{2} x_{2}^{2}+4 l^{2} x 2^{4}-2 l x_{2}^{4}+4 l^{2} .$$
With the help of a computer, we have checked that $\lambda_{\mathfrak{p}}<2 \rho<\lambda_{\mathfrak{p}}^{\text {max }}$ holds for any $2 \leq l \leq 20$, so in these cases both metrics are $G$-non-degenerate and $G$-unstable saddle critical points of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ of coindex 1. This numerical evidence suggests that these metrics are saddle points for any $l \geq 2$.

The only cases which have not been considered in this paper all have pairwise different $d_{1}, d_{2}, d_{3}$ and correspond to the spaces $W_{1}$ (between two and four Einstein metrics, see [CN], Theorem 1.3]) and $W_{3}$ (four Einstein metrics, see LNF, Example 4]). This is due to the fact that the Einstein metrics are not explicitly given in these papers, only existence results are provided.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $G / K$ & $g$ & $\left(x_{1}, \ldots, x_{r}\right)$ & $\left(\operatorname{det}_{g_{\mathrm{B}}} g\right)^{\frac{1}{n}} \operatorname{Sc}(g)$ \\
\hline \multirow{6}{*}{$\frac{E_{8}}{\mathrm{SU}(5) \times \mathrm{SU}(4) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3,4,5) & $$\begin{gathered}
\frac{572}{15} 2^{\frac{25}{52}} 3^{\frac{5}{26}} 5^{\frac{1}{26}} \\
\approx 69.9307
\end{gathered}$$ \\
\hline & $g_{1}$ & (1, 0.599785, 1.08371, 0.901823, 1.22291) & 68.8905 \\
\hline & $g_{2}$ & (1, 1.02137, 0.546007, 1.05352, 1.10879) & 68.7023 \\
\hline & $g_{3}$ & (1, 1.08294, 1.04088, 0.532615, 1.10351) & 68.7757 \\
\hline & $g_{4}$ & (1, 0.720713, 1.02546, 0.475234, 1.07095) & 68.6913 \\
\hline & $g_{5}$ & (1, 1.03732, 1.04718, 1.03082, 0.29862) & 68.4798 \\
\hline \multirow{5}{*}{$\frac{E_{8}}{\mathrm{SU}(5) \times \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & (1,2,3,4,5,6) & $$\begin{gathered}
\frac{159}{5} 2^{\frac{65}{106}} 3^{\frac{25}{106}} 5^{\frac{5}{53}} \\
\approx 69.0420
\end{gathered}$$ \\
\hline & $g_{1}$ & (1, 0.823084, 1.1467, 1.17377, 1.42664, 1.46519) & 68.6856 \\
\hline & $g_{2}$ & (1, 0.986536, 0.636844, 1.06853, 1.13323, 0.921127) & 68.4684 \\
\hline & $g_{3}$ & (1, 0.90422, 0.778283, 0.927483, 1.03408, 0.359949) & 68.2283 \\
\hline & $g_{4}$ & (1, 0.954875, 0.965321, 1.00534, 0.290091, 1.01965) & 67.8054 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 11. Einstein metrics on flag manifolds with $b_{2}(M)=1$ and $r=5,6$ (see [CS1]).}
\end{table}
4.4. Application to the prescribed Ricci curvature problem. Given a symmetric 2-tensor $T$ on a differentiable manifold $M$, asking about the existence and uniqueness (up to scaling) of a Riemannian metric $g$ and a constant $c>0$ such that $\operatorname{Rc}(g)=c T$, is called the prescribed Ricci curvature problem (see e.g. [B, Chapter 5]). For a $G$-invariant tensor $T$ and metric $g$ on a homogeneous space $M=G / K$, the question is therefore about the image and the injectivity (up to scaling) of the differentiable function Rc $: \mathcal{M}^{G} \longrightarrow \mathcal{S}^{2}(M)^{G}$. A metric $g \in \mathcal{M}^{G}$ is called Ricci locally invertible if Rc is as invertible as it can be near $g$, i.e., for any $T$ near $\operatorname{Rc}(g)$, existence and (local) uniqueness of solutions to the prescribed Ricci curvature problem are guaranteed (see LW] for a more detailed treatment). According to [LW, Lemma 6.1] (see also [L, Lemma 4.5]), $\left.d \mathrm{Rc}\right|_{g}=\frac{1}{2} \mathrm{~L}_{\mathfrak{p}}$ after identifications, so a necessary condition for the Ricci local invertibility of $g$ is that $\left.\operatorname{dim} \operatorname{Ker} \mathrm{L}_{\mathfrak{p}}\right|_{\mathcal{S}^{2}(M)^{G}}=1$ (see [LW, Theorem 1.3]). The metrics with $\lambda_{\mathfrak{p}}=0$ contained in Tables 2, 6 and 8 are therefore examples of $G$-invariant Einstein metrics which are not Ricci locally invertible. These are precisely the Kähler-Einstein metrics on flag manifolds with $b_{2}(M)=2$. On the other hand, it is easy to check that the remaining Einstein metrics considered in this paper are all Ricci locally invertible.

In what follows, we give examples of curves of $G$-invariant metrics with identical Ricci tensors. The metric $g_{K E}=(1,1,2)$ is Kähler-Einstein on each of the following homogeneous spaces,
$$\mathrm{SO}(2 l) / \mathrm{U}(1) \times \mathrm{U}(l-1), \quad l \geq 4, \quad E_{6} / \mathrm{SO}(8) \times \mathrm{U}(1) \times \mathrm{U}(1),$$
and $g_{K E}=(l+m, k+m, k+l+2 m)$ is a Kähler-Einstein metric on
$$\mathrm{SU}(k+l+m) / \mathrm{S}(\mathrm{U}(k) \times \mathrm{U}(l) \times \mathrm{U}(m)), \quad k, l, m \geq 1 .$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline $G / K$ & $g$ & $\lambda_{\mathfrak{p}}$ & $\lambda_{\mathfrak{p}}^{\text {max }}$ & $2 \rho$ \\
\hline \multirow{3}{*}{$\frac{E_{8}}{E_{6} \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{6}{5}-\frac{1}{30} \sqrt{51}$ & $\frac{6}{5}+\frac{1}{30} \sqrt{51}$ & $\frac{19}{30}$ \\
\hline & $g_{1}$ & 0.478572 & 1.55965 & 0.821452 \\
\hline & $g_{2}$ & 0.118731 & 1.272251 & 0.829109 \\
\hline \multirow{3}{*}{$\frac{E_{8}}{\mathrm{SU}(8) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{11-\sqrt{6}}{10}$ & $\frac{11+\sqrt{6}}{10}$ & $\frac{17}{30}$ \\
\hline & $g_{1}$ & 0.4676547 & 1.340237 & 0.819949 \\
\hline & $g_{2}$ & 0.326773 & 1.166896 & 0.785751 \\
\hline \multirow{3}{*}{$\frac{E_{7}}{\mathrm{SU}(5) \times \mathrm{SU}(3) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{5}{6}$ & $\frac{4}{3}$ & $\frac{5}{9}$ \\
\hline & $g_{1}$ & 0.469601 & 1.311724 & 0.825338 \\
\hline & $g_{2}$ & 0.352429 & 1.157063 & 0.772758 \\
\hline \multirow{3}{*}{$\frac{E_{7}}{\mathrm{SU}(6) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{7-\sqrt{2}}{6}$ & $\frac{7+\sqrt{2}}{6}$ & $\frac{11}{18}$ \\
\hline & $g_{1}$ & 0.469565 & 1.485343 & 0.816530 \\
\hline & $g_{2}$ & 0.194860 & 1.232011 & 0.820660 \\
\hline \multirow{3}{*}{$\frac{E_{6}}{\mathrm{SU}(3) \times \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{9}{8}-\frac{1}{24} \sqrt{33}$ & $\frac{9}{8}+\frac{1}{24} \sqrt{33}$ & $\frac{7}{12}$ \\
\hline & $g_{1}$ & 0.465849 & 1.391997 & 0.815861 \\
\hline & $g_{2}$ & 0.281933 & 1.187358 & 0.801967 \\
\hline \multirow{3}{*}{$\frac{F_{4}}{\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{5}{6}$ & $\frac{4}{3}$ & $\frac{5}{9}$ \\
\hline & $g_{1}$ & 0.469601 & 1.311722 & 0.825338 \\
\hline & $g_{2}$ & 0.352428 & 1.157064 & 0.772757 \\
\hline \multirow{3}{*}{$\frac{G_{2}}{\mathrm{U}(2)}$} & $g_{0}$ & $\frac{1}{2}$ & $\frac{5}{4}$ & $\frac{5}{12}$ \\
\hline & $g_{1}$ & 0.413430 & 1.211009 & 0.502068 \\
\hline & $g_{2}$ & 0.19355 & 2.670881 & 0.970058 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 12. Einstein metrics in Table 9. The Kähler metric $g_{0}$ is always $G$-stable and the rest are all $G$-non-degenerate and $G$-unstable of coindex 1.}
\end{table}

Note that the last $g_{K E}$ is a multiple of $(1,1,2)$ if $k=l$. In all the above cases, a straight-forward computation using (18) gives that if $g=\left(x_{1}, x_{2}, x_{3}\right)$, then $\mathrm{Rc}(g)=\mathrm{Rc}\left(g_{K E}\right)$ if and only if $x_{3}=x_{1}+x_{2}$ (recall that the Ricci tensor in terms of a $-\mathrm{B}_{\mathfrak{g}}$-orthonormal basis is given by $\left.\operatorname{Rc}(g)=\left(x_{1} \rho_{1}, x_{2} \rho_{2}, x_{3} \rho_{3}\right)\right)$. This implies that the metrics
$$g_{t}:=\left(t, \frac{1}{2}\left(-t+\left(t^{2}+\frac{8}{t}\right)^{1 / 2}\right), \frac{1}{2}\left(t+\left(t^{2}+\frac{8}{t}\right)^{1 / 2}\right)\right), \quad t>0,$$
have all the same volume and Ricci tensor as $g_{1}=g_{K E}=(1,1,2)$. This curve was recently discovered by Pulemotov and Ziller on the full flag manifold SU(3)/S(U(1) ${ }^{3}$ ).

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|}
\hline $G / K$ & $g$ & $\lambda_{\mathfrak{p}}$ & $\lambda_{2}$ & $\lambda_{\mathfrak{p}}^{\max }$ & $2 \rho$ & cx \\
\hline \multirow{3}{*}{$\frac{F_{4}}{\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{1}{2}$ & $\frac{20}{27}$ & $\frac{7}{6}$ & $\frac{14}{36}$ & 0 \\
\hline & $g_{1}$ & 0.4111 & 0.8447 & 1.2064 & 0.5380 & 1 \\
\hline & $g_{2}$ & 0.2108 & 1.2583 & 2.1506 & 0.8231 & 1 \\
\hline \multirow{3}{*}{$\frac{E_{7}}{\mathrm{SU}(4) \times \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{11-\sqrt{13}}{12}$ & $\frac{53}{54}$ & $\frac{11+\sqrt{13}}{12}$ & $\frac{4}{9}$ & 0 \\
\hline & $g_{1}$ & 0.5001 & 1.0457 & 1.2838 & 0.7173 & 1 \\
\hline & $g_{2}$ & 0.4331 & 1.0696 & 1.3332 & 0.7626 & 1 \\
\hline \multirow{3}{*}{$\frac{E_{8}}{\mathrm{SU}(7) \times \mathrm{SU}(2) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{9}{10}-\frac{\sqrt{21}}{15}$ & $\frac{14}{15}$ & $\frac{9}{10}+\frac{\sqrt{21}}{15}$ & $\frac{13}{30}$ & 0 \\
\hline & $g_{1}$ & 0.4826 & 1.0134 & 1.2468 & 0.6781 & 1 \\
\hline & $g_{2}$ & 0.3937 & 1.1307 & 1.3923 & 0.7826 & 1 \\
\hline \multirow{5}{*}{$\frac{E_{8}}{\mathrm{SU}(10) \times \mathrm{SU}(3) \times \mathrm{U}(1)}$} & $g_{0}$ & $\frac{19}{20}-\frac{\sqrt{309}}{60}$ & $\frac{97}{90}$ & $\frac{19}{20}+\frac{\sqrt{309}}{60}$ & $\frac{7}{15}$ & 0 \\
\hline & $g_{1}$ & 0.5039 & 1.1437 & 1.4399 & 0.7970 & 1 \\
\hline & $g_{2}$ & 0.1698 & 0.9025 & 1.1115 & 0.7038 & 1 \\
\hline & $g_{3}$ & 0.4527 & 1.0347 & 1.3018 & 0.7173 & 1 \\
\hline & $g_{4}$ & 0.2157 & 0.6048 & 1.5116 & 0.8030 & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 13. Einstein metrics in Table 10. The Kähler metric $g_{0}$ is always $G$-stable and all the other ones are $G$-non-degenerate and $G$-unstable with coindex as in the last column.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|}
\hline $g$ & $\lambda_{\mathfrak{p}}$ & $\lambda_{2}$ & $\lambda_{3}$ & $\lambda_{\mathfrak{p}}^{\text {max }}$ & $2 \rho$ & $c x$ \\
\hline $g_{0}$ & 0.483308 & 0.807779 & 1.002382 & 1.156529 & $\frac{11}{30} \approx 0.36$ & 0 \\
\hline $g_{1}$ & 0.510214 & 1.027352 & 1.238460 & 1.655126 & 0.757540 & 1 \\
\hline $g_{2}$ & 0.444857 & 1.112644 & 1.251940 & 1.598781 & 0.731014 & 1 \\
\hline $g_{3}$ & 0.387659 & 0.850534 & 1.094764 & 1.233562 & 0.678788 & 1 \\
\hline $g_{4}$ & 0.458617 & 0.613228 & 1.437954 & 1.612703 & 0.773963 & 2 \\
\hline $g_{5}$ & 0.240674 & 0.791323 & 1.169060 & 1.320873 & 0.674542 & 1 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 14. Einstein metrics on $E_{8} / \operatorname{SU}(5) \times \operatorname{SU}(4) \times \mathrm{U}(1)$ (see Table 11). The Kähler metric $g_{0}$ is $G$-stable and the remaining ones are all $G$-non-degenerate and $G$-unstable.}
\end{table}

On the spaces $\mathrm{SO}(8) / \mathrm{U}(1) \times \mathrm{U}(3), E_{6} / \mathrm{SO}(8) \times \mathrm{U}(1) \times \mathrm{U}(1)$ and $\mathrm{SU}(3 k) / \mathrm{S}\left(\mathrm{U}(k)^{3}\right)$ (i.e., when $d_{1}=d_{2}=d_{3}$ ), the scalar curvature is given by
$$\operatorname{Sc}\left(g_{t}\right)=c\left(-t^{2}+3\left(t^{2}+\frac{8}{t}\right)^{1 / 2}+\frac{4}{t}\right), \quad \text { for some } c>0,$$
which is a convex function on $(0, \infty)$ with a global minimum at $t=1$. The family $\left\{g_{t}: 1 \leq t\right\}$ is therefore pairwise non-homothetic as $\operatorname{Sc}\left(g_{t}\right)$ is strictly increasing on $[1, \infty)$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $g$ & $\lambda_{\mathfrak{p}}$ & $\lambda_{2}$ & $\lambda_{3}$ & $\lambda_{4}$ & $\lambda_{\mathfrak{p}}^{\max }$ & $2 \rho$ & $c x$ \\
\hline $g_{0}$ & 0.373056 & 0.616209 & 0.784713 & 0.907323 & 1.025363 & $\frac{3}{10}=0.3$ & 0 \\
\hline $g_{1}$ & 0.560023 & 0.753518 & 0.990611 & 1.177858 & 1.218291 & 0.627866 & 1 \\
\hline $g_{2}$ & 0.499591 & 0.995988 & 1.060532 & 1.188804 & 1.256011 & 0.697205 & 1 \\
\hline $g_{3}$ & 0.371562 & 0.622626 & 0.981804 & 1.317906 & 1.460064 & 0.735036 & 2 \\
\hline $g_{4}$ & 0.262279 & 0.832143 & 1.186281 & 1.385267 & 1.473554 & 0.698590 & 1 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 15. Einstein metrics on $E_{8} / \mathrm{SU}(5) \times \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ (see Table 11). The Kähler metric $g_{0}$ is $G$-stable and the other ones are all $G$ -unstable.}
\end{table}
(note that also $\left\{g_{t}: 0<t \leq 1\right\}$ is pairwise non-homothetic). Since for any $t>1, g_{t}$ has the same Ricci eigenvalues as $g_{s}$, where $s:=\frac{1}{2}\left(-t+\left(t^{2}+\frac{8}{t}\right)^{1 / 2}\right)$, we do not know whether these pairs of metrics are isometric or not.

For the rest of the Kähler-Einstein metrics which are not Ricci locally invertible, i.e., $g_{p^{ \pm}}$on $\mathrm{SO}(2 l) / \mathrm{U}(1) \times \mathrm{U}(l-1), l \geq 5$ and $W_{2}$ with $k=l$, and the three Kähler-Einstein metrics on $W_{2}$ with pairwise different $k, l, m$, the same behavior occurs and an explicit curve $g_{t}$ such that $\operatorname{Rc}\left(g_{t}\right) \equiv \operatorname{Rc}\left(g_{1}\right)$ and with the same properties as above can easily be given.

Remark 4.3. After the first version of this paper appeared in arXiv, these examples were generalized in [PZ].

\section*{5. Flag manifolds}

A flag manifold (or generalized flag manifold) is a homogeneous space $M=G / K$, where $G$ is a compact semisimple Lie group and $K$ is the centralizer of a torus in $G$. It is called full flag when $K$ is a maximal torus of $G$. Any compact, simply connected and de Rham irreducible homogeneous Kähler manifold is isometric to a $G$-invariant metric on a flag manifold $G / K$ with $G$ simple and simply connected. The isotropy representation of any flag manifold is multiplicity-free. We refer to [Ar, AC2] and references therein for more information on flag manifolds.

In this section, we compute the $G$-stability and critical point types of all Einstein metrics on flag manifolds with $b_{2}(M)=1$, where $b_{2}(M)$ denotes the second Betti number of $M$. As in §4, this will follow from the knowledge of the spectrum of $\mathrm{L}_{\mathfrak{p}}$, which is computed using Theorem 3.1 and explicitly provided for all Einstein metrics. Our results on $G$ -stability agree with [AC2, Theorem 3.1], where the Ricci flow behavior on flag manifolds with $b_{2}(M)=1$ is studied, and also with [GMPSS, Theorems 1 and 2], where the case of flag manifolds with three isotropy summands is considered.

The number $r$ of $\operatorname{Ad}(K)$-irreducible summands of the isotropy representation of these spaces goes from 2 to 6, and each of them admits a unique Kähler-Einstein metric given by $g_{0}:=(1,2, \ldots, r)$, with respect to a suitable decomposition $\mathfrak{p}=\mathfrak{p}_{1} \oplus \cdots \oplus \mathfrak{p}_{r}$ in $\operatorname{Ad}(K)$ -irreducible subspaces. Note that $\operatorname{dim} \mathcal{M}_{1}^{G}=r-1$.

The case when $r=2$ has been worked out in Example 3.9. Actually any flag manifold with $r=2$ has $b_{2}(M)=1$. On the other hand, the remaining flag manifolds with $r=3$ all have $b_{2}(M)=2$ and are given by the generalized Wallach spaces $W_{2}, W_{5}$ and $W_{7}$, already studied in §4.

The structural constants and numerical approximations of all Einstein metrics (other than $g_{0}$ ) on flag manifolds with $b_{2}(M)=1$ are given in [AC1] for $r=3$ (the case $E_{7} / \mathrm{SU}(5) \times \mathrm{SU}(3) \times \mathrm{U}(1)$ had to be corrected since the right dimensions are (60, 30, 10), see [CS2]), in [ArC] for $r=4$ and in [CS1] for $r=5,6$. The metrics, including their volume normalized scalar curvature $\mathrm{Sc}_{N}$ relative to the Killing metric $g_{\mathrm{B}}=(1, \ldots, 1)$ (see (20)), are listed in Tables 9, 10 and 11. It follows that the Einstein metrics on each space are always pairwise non-homothetic. Also note that $\operatorname{Sc}_{N}\left(g_{0}\right)>\operatorname{Sc}_{N}\left(g_{i}\right)$ for any $i \geq 1$ in all cases.

It is straightforward to check that the corresponding numerical approximations for the eigenvalues of the $r \times r$ matrix $\mathrm{L}_{\mathfrak{p}}$ and the $G$-stability types of these Einstein metrics are given as in Tables 12, 13, 14 and 15, according to the number $r$. They are all $G$-non-degenerate and Ricci locally invertible (see §4.4).

\section*{References}
\begin{itemize}
\item[] [AFD] D. Alekseevsky, C. Ferraris, I. Dotti, Homogeneous Ricci positive 5-manifolds, Pacific J. Math. 175 (1996), 1-12.
\item[] [AANS] N.A. Abiev, A. Arvanitoyeorgos, Y.G. Nikonorov, P. Siasos, The Ricci Flow on Some Generalized Wallach Spaces, Springer Proc. Math. Stat. 72 (2014), 3-37.
\item[] [Ar] A. Arvanitoyeorgos, Progress on homogeneous Einstein manifolds and some open problems, Bull. Greek Math. Soc. 58 (2015), 75-97.
\item[] [ArC] A. Arvanitoyeorgos, I. Chrysikos, Invariant Einstein metrics on flag manifolds with four isotropy summands, Ann. Glob. Anal. Geom. 37 (2010), 185-219.
\item[] [AC1] S. Anastassiou, I. Chrysikos, The Ricci flow approach to homogeneous Einstein metrics on flag manifolds, J. Geom. Phys. 61 (2011), 1587-1600.
\item[] [AC2] S. Anastassiou, I. Chrysikos, Ancient solutions of the homogeneous Ricci flow on flag manifolds, Extracta Math. 36 (2021), 99-145.
\item[] [Be] M. Berger, Quelques formules des variation pour une structure riemannienne, Ann. Sc. Ec. Norm. Sup. 3 (1970), 285-294.
\item[] [B] A. Besse, Einstein manifolds, Ergeb. Math. 10 (1987), Springer-Verlag, Berlin-Heidelberg.
\item[] [Bo] C. Böhm, Homogeneous Einstein metrics and simplicial complexes, J. Diff. Geom. 67 (2004), 79-165.
\item[] [BL] C. Böhm, R. Lafuente, Real geometric invariant theory, Diff. Geom. in the Large, edited by Dearricott, Tuschmann, Nikolayevsky, Leistner and Crowley, Cambridge Univ. Press, 2020.
\item[] [BWZ] C. Böhm, M.Y. Wang, W. Ziller, A variational approach for compact homogeneous Einstein manifolds, Geom. Funct. Anal. 14 (2004), 681-733.
\item[] [CHI] Huai-Dong Cao, R.S. Hamilton, T. Ilmanen, Gaussian densities and stability for some Ricci solitons, preprint 2004 (arXiv).
\item[] [CH] Huai-Dong Cao, Chenxu He, Linear stability of Perelman's $\nu$-entropy on symmetric spaces of compact type, J. reine angew. Math., 709 (2015), 229-246.
\item[] [CKL] Zhiqi Chen, Yifang Kang, Ke Liang, Invariant Einstein metrics on three-locally-symmetric spaces, Comm. Anal. Geom. 24 (2016), 769-792.
\item[] [CN] Zhiqi Chen, Y.G. Nikonorov, Invariant Einstein metrics on generalized Wallach spaces, Sci. China Math 62 (2019), 569-584.
\item[] [CS1] I. Chrysikos, Y. Sakane, The classification of homogeneous Einstein metrics on flag manifolds with $b_{2}(M)=1$, Bull. Sci. Math. 138 (2014), 665-692.
\item[] [CS2] I. Chrysikos, Y. Sakane, Non-naturally reductive homogeneous metrics on exceptional Lie groups, J. Geom. Phys. 116 (2017), 152-186.
\item[] [DK] W. Dickinson, M. Kerr, The geometry of compact homogeneous spaces with two isotropy summands, Ann. Global Anal. Geom. 34 (2008), 329-350.
\item[] [GHP] G. W. Gibbons, S.A. Hartnoll, C. N. Pope, Böhm and Einstein-Sasaki metrics, black holes, and cosmological event horizons, Phys. Rev. D 67 (2003), 084024.
\item[] [GR] C. Godsil, G. Royle, Algebraic graph theory, GTM 207 (2001), Springer.
\item[] [GMPSS] L. Grama, R. Martins, M. Patrao, L. Seco, L. Speranca, Global dynamics of the Ricci flow on flag manifolds with three isotropy summands, preprint 2020 (arXiv).
\item[] [He] Chenxu He, Cohomogeneity one manifolds with a small family of invariant metrics, Geom. Dedicata 157 (2012), 41-90.
\end{itemize}
[H] D. Hilbert, Die grundlagen der physik, Nac. Ges. Wiss. (1915), Gottingen, 461-472.
[J] G. Jensen, The Scalar Curvature of Left-Invariant Riemannian Metrics, Indiana Math. J. 20 (1971), 1125-1144.
[K] M. Kerr, New examples of homogeneous Einstein metrics, Michigan J. Math. 45 (1998), 115-134.
[Ko1] N. Koiso, On the second derivative of the total scalar curvature, Osaka J. Math. 16 (1979), 413-421.
[Ko2] N. Koiso, Rigidity and stability of Einstein metrics: the case of compact symmetric spaces, Osaka J. Math. 17 (1980), 51-73.
[Kr] K. Kröncke, Stability and instability of Ricci solitons, Calc. Var. PDE. 53 (2015), 265-287.
[LfL] R. Lafuente, J. Lauret, Structure of homogeneous Ricci solitons and the Alekseevskii conjecture, J. Diff. Geom. 98 (2014), 315-347.
[LaL] E.A. Lauret, J. Lauret, The stability of standard homogeneous Einstein manifolds, preprint 2021 (arXiv).
[L] J. Lauret, On the stability of homogeneous Einstein manifolds, Asian J. Math., in press (arXiv).
[LW] J. Lauret, C.E. Will, Prescribing Ricci curvature on homogeneous manifolds, J. reine angew. Math. 783 (2022), 95-133.
[LNF] A. Lomshakov, Y. Nikonorov, E. Firsov, Invariant Einstein metrics on three-locally-symmetric spaces, Siberian Adv. Math. 14 (2004), 43-62.
[N] Y.G. Nikonorov, Classification of generalized Wallach spaces, Geom. Ded. 181 (2016), 193-212. Correction Geom. Ded. (2021), in press.
[PZ] A. Pulemotov, W. Ziller, On the variational properties of the prescribed Ricci curvature functional, preprint 2021 (arXiv).
[SSW] P. Schwahn, U. Semmelmann, G. Weingart, Stability of the Non-Symmetric Space $E_{7} / P S O(8)$, preprint 2022 (arXiv).
[S] M. Statha, Invariant metrics in homogeneous spaces with equivalent isotropy summands, Toyama Math. J. 38 (2016), 35-60.
[WW] Changliang Wang, M. Y. Wang, Instability of some Riemannian manifolds with real Killing spinors, Comm. Anal. Geom., in press (arXiv).
[WZ] M.Y. Wang, W. Ziller, Existence and nonexistence of homogeneous Einstein metrics, Invent. Math. 84 (1986), 177-194.

\section*{6. Appendix: Maple codes}

In this appendix, we include the computational Maple codes used in the paper.
The first part concerns generalized Wallach spaces and computes the three eigenvalues (one of them is always zero) of the generic $3 \times 3$ matrix of $\mathrm{L}_{\mathfrak{p}}$ given in (23), in terms of the structural constants $a_{i}:=[123] / d_{i}, i=1,2,3$ (see Table 1) and the Einstein metric $g=\left(x_{1}, x_{2}, x_{3}\right)$. The eigenvalues exhibited in Tables 2, 6, 7 and 8 are obtained by just replacing in the general formula for each case with the corresponding $a_{i}$ 's and $x_{i}$ 's, which are given in Tables 2, 4 and 8.

In the second part, we consider flag manifolds and first compute the Ricci eigenvalues and the entries of the generic matrix of $\mathrm{L}_{\mathfrak{p}}$ in the case $r=6$, i.e., for $E_{8} / \operatorname{SU}(5) \times \operatorname{SU}(3) \times$ $\mathrm{SU}(2) \times \mathrm{U}(1)$. It turns out that for the other cases $r=3,4,5$ such a matrix is obtained by considering the principal $r \times r$ submatrix and setting $A i j k=0$ whenever at least one of $i, j, k$ is $>r$.

As an example, the third part computes all the information given in the last row of Table 11 and Table 15 for the five Einstein metrics on $E_{8} / \operatorname{SU}(5) \times \operatorname{SU}(3) \times \operatorname{SU}(2) \times \mathrm{U}(1)$.

\footnotetext{
FaMAF, Universidad Nacional de Córdoba and CIEM, CONICET (Argentina)
Email address: jorgelauret@unc.edu.ar
Email address: cynthia.will@unc.edu.ar
}

\section*{Generalized Wallach Spaces}
$$\left[\begin{array}{l}
\mathrm{Lp}:=\text { Matrix }(3,3, \text { shape }=\text { symmetric }): \\
\mathrm{Lp}[1,1]:=2 * a 1 * x 1 /(x 2 * x 3): \\
\mathrm{Lp}[2,2]:=2 * a 2 * x 2 /(x 1 * x 3): \\
\mathrm{Lp}[3,3]:=2 * a 3 * x 3 /(x 2 * x 1): \\
\mathrm{Lp}[1,2]:=\operatorname{sqrt}(a 1) * \operatorname{sqrt}(a 2) *(x 3 /(x 1 * x 2)-x 1 /(x 2 * x 3)-x 2 /(x 1 * x 3)): \\
\operatorname{Lp}[1,3]:=\operatorname{sqrt}(a 1) * \operatorname{sqrt}(a 3) *(x 2 /(x 1 * x 3)-x 1 /(x 2 * x 3)-x 3 /(x 1 * x 2)): \\
L p[2,3]:=\operatorname{sqrt}(a 2) * \operatorname{sqrt}(a 3) *(x 1 /(x 2 * x 3)-x 2 /(x 1 * x 3)-x 3 /(x 1 * x 2)):
\end{array}\right.$$
$$\left[\begin{array}{r}
>\operatorname{simplify}(L p) ; \\
{\left[\left[\frac{2 a 1 x 1}{x 2 x 3},-\frac{\sqrt{a 1} \sqrt{a 2}\left(-x 3^{2}+x 1^{2}+x 2^{2}\right)}{x 2 x 3 x 1},-\frac{\sqrt{a 1} \sqrt{a 3}\left(-x 2^{2}+x 1^{2}+x 3^{2}\right)}{x 2 x 3 x 1}\right]\right.} \\
{\left[-\frac{\sqrt{a 1} \sqrt{a 2}\left(-x 3^{2}+x 1^{2}+x 2^{2}\right)}{x 2 x 3 x 1}, \frac{2 a 2 x 2}{x 1 x 3}, \frac{\sqrt{a 2} \sqrt{a 3}\left(x 1^{2}-x 2^{2}-x 3^{2}\right)}{x 2 x 3 x 1}\right],} \\
\left.\left[-\frac{\sqrt{a 1} \sqrt{a 3}\left(-x 2^{2}+x 1^{2}+x 3^{2}\right)}{x 2 x 3 x 1}, \frac{\sqrt{a 2} \sqrt{a 3}\left(x 1^{2}-x 2^{2}-x 3^{2}\right)}{x 2 x 3 x 1}, \frac{2 a 3 x 3}{x 2 x 1}\right]\right]
\end{array},\right.$$
$$\left[\begin{array}{l}
>\text { Eigenvalues }(L p) ; \\
{\left[\left[\begin{array}{l}
{[0],} \\
\\
{\left[\frac { 1 } { x 3 x 2 x 1 } \left(a 3 x 3^{2}+a 2 x 2^{2}+a 1 x 1^{2}\right.\right.} \\
+\left(a 3^{2} x 3^{4}+a 2^{2} x 2^{4}+a 1^{2} x 1^{4}+a 3 a 2 x 2^{4}+a 3 a 2 x 3^{4}+a 2 a 1 x 3^{4}+a 3 a 1 x 2^{4}\right.
\end{array}\right.\right.} \\
-2 a 3 a 1 x 2^{2} x 1^{2}-2 a 3 a 1 x 3^{2} x 2^{2}+a 3 a 1 x 1^{4}+a 3 a 1 x 3^{4}+a 3 a 2 x 1^{4}-2 a 3 a 2 x 2^{2} x 1^{2} \\
\left.\left.\left.-2 a 3 a 2 x 3^{2} x 1^{2}-2 a 2 a 1 x 3^{2} x 1^{2}-2 a 2 a 1 x 3^{2} x 2^{2}+a 2 a 1 x 1^{4}+a 2 a 1 x 2^{4}\right)^{1 / 2}\right)\right], \\
{\left[\frac { 1 } { x 3 x 2 x 1 } \left(a 3 x 3^{2}+a 2 x 2^{2}+a 1 x 1^{2}\right.\right.} \\
-\left(a 3^{2} x 3^{4}+a 2^{2} x 2^{4}+a 1^{2} x 1^{4}+a 3 a 2 x 2^{4}+a 3 a 2 x 3^{4}+a 2 a 1 x 3^{4}+a 3 a 1 x 2^{4}\right. \\
-2 a 3 a 1 x 2^{2} x 1^{2}-2 a 3 a 1 x 3^{2} x 2^{2}+a 3 a 1 x 1^{4}+a 3 a 1 x 3^{4}+a 3 a 2 x 1^{4}-2 a 3 a 2 x 2^{2} x 1^{2} \\
\left.\left.\left.\left.-2 a 3 a 2 x 3^{2} x 1^{2}-2 a 2 a 1 x 3^{2} x 1^{2}-2 a 2 a 1 x 3^{2} x 2^{2}+a 2 a 1 x 1^{4}+a 2 a 1 x 2^{4}\right)^{1 / 2}\right)\right]\right]
\end{array}\right.$$

\section*{Flag Manifolds}
$$\begin{aligned}
>\rho I: & =\frac{1}{2 x 1}-\frac{A 112}{2 d 1} \frac{x 2}{x 1^{\wedge} 2}+\left(\frac{A 123}{2 d 1}\right)\left(\frac{x 1}{x 2 x 3}-\frac{x 2}{x 1 x 3}-\frac{x 3}{x 1 x 2}\right)+\frac{A 134}{2 d 1} \\
& *\left(\frac{x 1}{x 3 x 4}-\frac{x 3}{x 1 x 4}-\frac{x 4}{x 1 x 3}\right)+\frac{A 145}{2 d 1}\left(\frac{x 1}{x 4 x 5}-\frac{x 4}{x 1 x 5}-\frac{x 5}{x 1 x 4}\right)
\end{aligned}$$
$$\begin{aligned}
& +\frac{A 156}{2 d 1}\left(\frac{x 1}{x 5 x 6}-\frac{x 5}{x 1 x 6}-\frac{x 6}{x 1 x 5}\right): \\
\rho 2:= & \frac{1}{2 x 2}-\frac{A 224}{2 d 2} * \frac{x 4}{x 2^{\wedge} 2}+\frac{A 112}{4 d 2} *\left(\frac{x 2}{x 1^{\wedge} 2}-\frac{2}{x 2}\right)+\frac{A 123}{2 d 2} *\left(\frac{x 2}{x 1 x 3}-\frac{x 1}{x 2 x 3}\right. \\
- & \left.\frac{x 3}{x 1 x 2}\right)+\frac{A 235}{2 d 2} *\left(\frac{x 2}{x 3 x 5}-\frac{x 3}{x 2 x 5}-\frac{x 5}{x 2 x 3}\right)+\frac{A 246}{2 d 2} *\left(\frac{x 2}{x 4 x 6}-\frac{x 4}{x 2 x 6}\right. \\
- & \left.\frac{x 6}{x 2 x 4}\right): \\
\rho 3:= & \frac{1}{2 x 3}+\frac{A 123}{2 d 3} *\left(\frac{x 3}{x 1 x 2}-\frac{x 2}{x 1 x 3}-\frac{x 1}{x 2 x 3}\right)+\frac{A 134}{2 d 3} *\left(\frac{x 3}{x 1 x 4}-\frac{x 1}{x 3 x 4}\right. \\
- & \left.\frac{x 4}{x 1 x 3}\right)+\frac{A 235}{2 d 3} *\left(\frac{x 3}{x 2 x 5}-\frac{x 2}{x 3 x 5}-\frac{x 5}{x 2 x 3}\right)-\frac{A 336}{2 d 3} * \frac{x 6}{x 3^{\wedge} 2}: \\
\rho 4:= & \frac{1}{2 x 4}+\frac{A 224}{4 d 4} *\left(\frac{x 4}{x 2^{\wedge} 2}-\frac{2}{x 4}\right)+\frac{A 134}{2 d 4} *\left(\frac{x 4}{x 1 x 3}-\frac{x 1}{x 3 x 4}-\frac{x 3}{x 1 x 4}\right)+\frac{A 145}{2 d 4} \\
* & \left(\frac{x 4}{x 1 x 5}-\frac{x 1}{x 4 x 5}-\frac{x 5}{x 1 x 4}\right)+\frac{A 246}{2 d 4} *\left(\frac{x 4}{x 2 x 6}-\frac{x 2}{x 4 x 6}-\frac{x 6}{x 2 x 4}\right): \\
\rho 5:= & \frac{1}{2 x 5}+\frac{A 145}{2 d 5} *\left(\frac{x 5}{x 1 x 4}-\frac{x 1}{x 4 x 5}-\frac{x 4}{x 1 x 5}\right)+\frac{A 235}{2 d 5} *\left(\frac{x 5}{x 2 x 3}-\frac{x 2}{x 3 x 5}\right. \\
- & \left.\frac{x 3}{x 2 x 5}\right)+\frac{A 156}{2 d 5} *\left(\frac{x 5}{x 1 x 6}-\frac{x 1}{x 5 x 6}-\frac{x 6}{x 1 x 5}\right): \\
\rho 6:= & \frac{1}{2 x 6}+\frac{A 156}{2 d 6} *\left(\frac{x 6}{x 1 x 5}-\frac{x 1}{x 5 x 6}-\frac{x 5}{x 1 x 6}\right)+\frac{A 246}{2 d 6} *\left(\frac{x 6}{x 2 x 4}-\frac{x 2}{x 4 x 6}\right. \\
- & \left.\frac{x 4}{x 2 x 6}\right)+\frac{A 336}{4 d 6} *\left(\frac{x 6}{x 3^{\wedge} 2}-\frac{2}{x 6}\right):
\end{aligned}$$
$[>$ Rho $:=(\rho 1, \rho 1, \rho 3, \rho 4, \rho 5, \rho 6)$ :
\begin{itemize}
\item[□] Lp := Matrix(6, 6, shape = symmetric ) :
$$\begin{aligned}
& L p[1,1]:=\frac{2 A 123}{d 1} \frac{x 1}{x 2 x 3}+2 \frac{A 134}{d 1} \frac{x 1}{x 3 x 4}+2 \frac{A 145}{d 1} \frac{x 1}{x 4 x 5}+2 \frac{A 156}{d 1} \frac{x 1}{x 5 x 6} \\
& \quad+\frac{A 112}{d 1} \frac{x 2}{x 1^{2}}:
\end{aligned}$$
$$\begin{aligned}
& L p[2,2]:=2 \frac{A 123}{d 2} \frac{x 2}{x 1 x 3}+\frac{A 112}{d 2} \frac{x 2}{x 1^{2}}+\frac{A 224}{d 2} \frac{x 4}{x 2^{2}}+2 \frac{A 235}{d 2} \frac{x 2}{x 3 x 5} \\
& \quad+2 \frac{A 246}{d 2} \frac{x 2}{x 4 x 6}:
\end{aligned}$$
$$\begin{aligned}
& \operatorname{Lp}[3,3]:=2 \frac{A 123}{d 3} \frac{x 3}{x 1 x 2}+2 \frac{A 134}{d 3} \frac{x 3}{x 1 x 4}+\frac{2 A 235}{d 3} \frac{x 3}{x 2 x 5}+\frac{A 336}{d 3} \frac{x 6}{x 3^{2}}: \\
& \operatorname{Lp}[4,4]:=2 \frac{A 134}{d 4} \frac{x 4}{x 1 x 3}+2 \frac{A 145}{d 4} \frac{x 4}{x 1 x 5}+2 \frac{A 246}{d 4} \frac{x 4}{x 2 x 6}+\frac{A 224}{d 4} \frac{x 4}{x 2^{2}}: \\
& \operatorname{Lp}[5,5]:=2 \frac{A 145}{d 5} \frac{x 5}{x 1 x 4}+2 \frac{A 235}{d 5} \frac{x 5}{x 2 x 3}+2 \frac{A 156}{d 5} \frac{x 5}{x 1 x 6}: \\
& \operatorname{Lp}[6,6]:=2 \frac{A 156}{d 6} \frac{x 6}{x 1 x 5}+2 \frac{A 246}{d 6} \frac{x 6}{x 2 x 4}+\frac{A 336}{d 6} \frac{x 6}{x 3^{2}}:
\end{aligned}$$
$L p[1,2]:=\left(\left(x 3^{\wedge} 2-x 1^{\wedge} 2-x 2^{\wedge} 2\right) * A 123 /\left(x 1^{*} x 2^{*} x 3\right)+\left(x 1^{\wedge} 2-x 1^{\wedge} 2-x 2^{\wedge} 2\right) * A 112 /(x 1\right.$ $* x 2 * x 1)) /(\operatorname{sqrt}(d 1) * \operatorname{sqrt}(d 2)):$
\end{itemize}
$L p[1,3]:=\left(\left(x 2^{\wedge} 2-x 1^{\wedge} 2-x 3^{\wedge} 2\right) * A 123 /\left(x 1^{*} x 2^{*} x 3\right)+\left(x 4^{\wedge} 2-x 1^{\wedge} 2-x 3^{\wedge} 2\right) * A 134 /(x 1\right.$
```
        *x3*x4))/(sqrt(d1)*sqrt(d3)) :
    Lp[1,4] := (x3^2-x1^2-x4^2) *A134/(sqrt(d1)*sqrt(d4)*x1*x3*x4)+(x5^2-x1^2
        -x4^2) *A145/(sqrt(d1)*sqrt(d4)*x1*x4*x5) :
    Lp[1,5]:=(x4^2-x1^2-x5^2)*A145/(sqrt(d1)*sqrt(d5)*x1*x4*x5)+(x6^2-x1
        ^2 -x5^2) *A156/ (sqrt(d1) * sqrt (d5) * x1 * x5 * x6 ) :
    Lp[1, 6] := (x5^2 -x1^2 -x6^2) *A156/ (sqrt(d1) * sqrt(d6) * x1 * x5 * x6) :
    Lp[2, 3] := (x1^2-x2^2-x3^2) *A123/ (sqrt(d2) * sqrt(d3) * x1* x2 * x3) + (x5^2 - x2^2
        -x3^2) *A235/(sqrt(d2) *sqrt(d3) * x2 * x3* x5) :
    Lp[2, 4] := (x2^2-x2^2-x4^2) *A224/ (sqrt(d2) * sqrt(d4) * (x2* x2) * x4) + (x6^2 - x2
        ^2 -x4^2 ) *A246/ (sqrt(d2) * sqrt (d4) *x2* x4* x6) :
    Lp[2,5]:=(x3^2-x2^2-x5^2)*A235/(sqrt(d2)*sqrt(d5)*x2*x3*x5):
    Lp[2, 6] := (x4^2 -x2^2 -x6^2) *A246/ (sqrt(d2) * sqrt(d6) *x2* x4 * x6) :
    Lp[3, 4] := (x1^2-x3^2-x4^2)*A134/ (sqrt(d3)*sqrt(d4)*x1*x3*x4) :
    Lp[3, 5] := (x2^2 -x3^2 -x5^2) *A235/ (sqrt(d3) * sqrt(d5) * x2 * x3 * x5) :
    Lp[3, 6] := (x3^2 -x3^2 -x6^2) *A336/ (sqrt(d3) * sqrt(d6) * x3 * x3 * x6) :
    Lp[4, 5] := (x1^2 -x4^2 -x5^2) *A145/(sqrt(d4) * sqrt(d5) * x1 * x4 * x5) :
    Lp[4, 6] := (x2^2 -x4^2 -x6^2) *A246/ (sqrt(d4) * sqrt(d6) *x2* x4 * x6) :
    Lp[5, 6] := (x1^2 -x5^2 -x6^2) *A156/(sqrt(d5) *sqrt(d6) * x1 * x5 * x6) :
```


$\mathbf{E 8} / \mathbf{S U}(\mathbf{5}) \times \mathbf{S U}(\mathbf{3}) \times \mathbf{S U}(\mathbf{2}) \times \mathbf{U}(\mathbf{1})$
\begin{lstlisting}[mathescape=true]
> A112 $:=8:$ A123 $:=6:$ A134 $:=4:$ A145 $:=2:$ A156 $:=1:$ A224 $:=6:$ A235 $:=2:$ A246
        $:=2: A 336:=2:$
    $d 1:=60: d 2:=60: d 3:=40: d 4:=30: d 5:=12: d 6:=10: n:=d 1+d 2+d 3+d 4$
        $+d 5+d 6$ :
\end{lstlisting}


g0
\begin{lstlisting}[mathescape=true]
    $x 1:=1: x 2:=2: x 3:=3: x 4:=4: x 5:=5: x 6:=6:$
    $L p$ : Rho; Eigenvalues (Lp) :
    $E:=\operatorname{[evalf}($ Eigenvalues $(L p)[1])$, evalf $($ Eigenvalues $(L p)[2])$,
        $\operatorname{evalf}(\operatorname{Eigenvalues}(L p)[3]), \operatorname{evalf}(\operatorname{Eigenvalues}(L p)[4]), \operatorname{evalf}(\operatorname{Eigenvalues}(L p)[5])$,
        evalf ( Eigenvalues (Lp) [6]) ];
    $S:=\operatorname{simplify}\left(n \rho I \sqrt[n]{x 1^{d 1} x 2^{d 2} x 3^{d 3} x 4^{d 4} x 5^{d 5} x 6^{d 6}}\right) ; \operatorname{evalf}(S)$;
            $\frac{3}{20}, \frac{3}{20}, \frac{3}{20}, \frac{3}{20}, \frac{3}{20}, \frac{3}{20}$
    $E:=[0 ., 0.3730569046,0.6162097030,0.7847133138,0.9073230286,1.025363717]$
            $S:=\frac{159}{5} 2^{\frac{65}{106}} 3^{\frac{25}{106}} 5^{3 / 53}$
            69.04208899
\end{lstlisting}


g1
\begin{lstlisting}[mathescape=true]
> x1 : = ' x1 ' : x2 : = ' x2' : x3 : = ' x 3' : x4 : = ' x 4' : x5 : = ' x 5' : x6 : = ' x6 ' : S : = ' S':
    $x 1:=1: x 2:=0.823084: x 3:=1.1467: x 4:=1.17377: x 5:=1.42664: x 6:=1.46519:$
    $L p$ : Rho; Eigenvalues (Lp) :
    $E:=\operatorname{[evalf}($ Eigenvalues $(L p)[1])$, evalf $($ Eigenvalues $(L p)[2])$,
        evalf ( Eigenvalues $(L p)$ [3]), evalf ( Eigenvalues $(L p)$ [4]), evalf ( Eigenvalues $(L p)$ [5]),
\end{lstlisting}

```
        evalf( Eigenvalues (Lp) [6]) ];
    S := simplify(n pl n x1 x2 x2 x3 di x4 d4 x5 d5 x6 d6 );
0.3139332385, 0.3139332385, 0.3139328022, 0.3139338925, 0.3139330303, 0.3139322352
E:= [0.5600234542, 0.7535183722, 0.9906114813, 1.177858956, 1.218291564,
    -1.166944215 10-10]
            S := 68.68562011
```

g2
\begin{lstlisting}[mathescape=true]
> x1 : = 'x1': x2 : = 'x2': x3 : = 'x3': x4 := 'x4': x5 : = 'x5': x6 : = 'x6': S : = 'S':
        $x 1:=1: x 2:=0.986536: x 3:=0.636844: x 4:=1.06853: x 5:=1.13323: x 6$
            $:=0.921127$ :
        $L p$ : Rho; Eigenvalues $(L p)$ :
        $E:=\operatorname{[evalf}($ Eigenvalues $(L p)[1])$, evalf $($ Eigenvalues $(L p)[2])$,
            evalf ( Eigenvalues $(L p)$ [3]), evalf ( Eigenvalues $(L p)$ [4]), evalf ( Eigenvalues $(L p)$ [5]),
            evalf (Eigenvalues (Lp) [6]) ];
    $S:=\operatorname{simplify}\left(n \rho I \sqrt[n]{x 1^{d 1} x 2^{d 2} x 3^{d 3} x 4^{d 4} x 5^{d 5} x 6^{d 6}}\right)$;
    0.3486027100, 0.3486027100, 0.3486028028, 0.3486031268, 0.3486029995, 0.3486027654
$E:=[0.4995917513,0.9959880812,1.060533751,1.188803385,1.256012444$,
        $\left.-1.90367755310^{-10}\right]$
            $S:=68.46848748$
\end{lstlisting}

g3
\begin{lstlisting}[mathescape=true]
> x1 : = 'x1': x2 : = 'x2': x3 : =' x3': x4 : = 'x4': x5 : = 'x5': x6 : = 'x6': S : = 'S':
        $x 1:=1: x 2:=0.90422: x 3:=0.778283: x 4:=0.927483: x 5:=1.03408: x 6$
            $:=0.359949$ :
        $L p$ : Rho; Eigenvalues $(L p)$ :
        $E:=[$ evalf $($ Eigenvalues $(L p)[1])$, evalf $($ Eigenvalues $(L p)[2])$,
            evalf ( Eigenvalues (Lp) [3]), evalf ( Eigenvalues $(L p)$ [4]), evalf ( Eigenvalues $(L p)$ [5]),
            evalf (Eigenvalues (Lp) [6]) ];
        $S:=\operatorname{simplify}\left(n \rho I \sqrt[n]{x 1^{d 1} x 2^{d 2} x 3^{d 3} x 4^{d 4} x 5^{d 5} x 6^{d 6}}\right)$;
    0.3675183203, 0.3675183203, 0.3675183901, 0.3675184633, 0.3675188076, 0.3675185485
$E:=\left[1.34993003310^{-10}, 0.3715622521,0.6226262530,0.9818043769,1.317906464\right.$,
        1.460064982 ]
            $S:=68.22833762$
\end{lstlisting}

g4
\begin{lstlisting}[mathescape=true]
> x1 : = 'x1': x2 : = 'x2': x3 : = 'x3': x4 : = 'x4': x5 : = 'x5': x6 : = 'x6': S : = ' S':
        $x 1:=1: x 2:=0.954875: x 3:=0.965321: x 4:=1.00534: x 5:=0.290091: x 6$
            $:=1.01965$ :
    $L p$ : Rho; Eigenvalues $(L p)$ :
    $E:=[$ evalf $($ Eigenvalues $(L p)[1])$, evalf $($ Eigenvalues $(L p)[2])$,
            evalf ( Eigenvalues $(L p)$ [3]), evalf ( Eigenvalues $(L p)$ [4]), evalf ( Eigenvalues $(L p)$ [5]),
            evalf (Eigenvalues (Lp)[6])];
\end{lstlisting}

$$\begin{gathered}
S:=\operatorname{simplify}\left(n \rho l \sqrt[n]{x 1^{d 1} x 2^{d 2} x 3^{d 3} x 4^{d 4} x 5^{d 5} x 6^{d 6}}\right) ; \\
0.3492954321,0.3492954321,0.3492960272,0.3492971362,0.3492958309,0.3492967860 \\
E:=[0 ., 0.2622798888,0.8321437515,1.186281998,1.385267799,1.473554617] \\
S:=67.80543204
\end{gathered}$$
---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: On cohomogeneity one Hermitian non-Kähler metrics]

Let $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}, \mathrm{g}\right)$ be a Bérard-Bergery standard cohomogeneity one Hermitian manifold and fix a unit speed geodesic $\gamma: \bar{I} \rightarrow M$ which intersects orthogonally any G-orbit. Then, by means of proposition 3.15, the second-Chern-Einstein equation
$$\operatorname{Ric}^{\operatorname{Ch[2]}}(\mathfrak{g})=\frac{\lambda}{2 m} \mathfrak{g}$$
becomes
$$\left\{\begin{array}{l}
-\frac{f^{\prime \prime}(r)}{f(r)}+\frac{2 m(m-1) n}{p} \frac{f^{\prime}(r)}{h(r)^{2}}+\frac{2 m^{2}(m-1) n^{2}}{p^{2}} \frac{f(r)^{2}}{h(r)^{4}}=\frac{\lambda(r)}{2 m} \\
-\frac{h^{\prime \prime}(r)}{h(r)}+\frac{h^{\prime}(r)^{2}}{h(r)^{2}}-\frac{f^{\prime}(r)}{f(r)} \frac{h^{\prime}(r)}{h(r)}+\frac{2 m(m-1) n}{p} f(r) \frac{h^{\prime}(r)}{h(r)^{3}} \\
\quad-2\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{4}}+\frac{2 m}{h(r)^{2}}=\frac{\lambda(r)}{2 m}
\end{array},\right.$$
where $\lambda: I \rightarrow \mathbb{R}$ is an admissible function (see remark 3.10). Note that, in this case, it holds that $\lambda=\operatorname{scal}^{\mathrm{Ch}}(\mathrm{g})$.

Our first result in this section concerns the local existence and uniqueness of second-Chern-Einstein metrics, with prescribed Chern-scalar curvature, in a neighbourhood of a singular orbit. More precisely

Theorem 5.1. Assume that the complex manifold $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K})\right.$, J) has a singular orbit, corresponding to the value $r=0$ of the orthogonal geodesic $\gamma$. For any constant $a \in \mathbb{R}_{>0}$ and for any admissible function $\lambda: I \rightarrow \mathbb{R}$, there exist $\varepsilon>0$ and two smooth functions $f, h:[0, \varepsilon) \rightarrow \mathbb{R}$ satisfying the following conditions:
\begin{itemize}
\item[(I)] $f, h$ solve the second-Chern-Einstein equations (5.1);
\item[(II)] $f, h$ determine a smooth Hermitian metric $\mathfrak{g}=\mathbb{g}(f, h)$ on the open set
$$\mathcal{U}_{\varepsilon}^{\mathrm{reg}}:=\bigcup_{r \in(0, \varepsilon)} \mathrm{G} \cdot \gamma(r) \subset M_{(i, n)}(\mathrm{G}, \mathrm{~K})^{\mathrm{reg}}$$
which extends smoothly over the singular orbit $\mathrm{G} \cdot \gamma(0)$;
\item[(III)] $h(0)=a$ and the Chern-scalar curvature of $\mathfrak{g}$ verifies $\operatorname{scal}^{\mathrm{Ch}}(\mathfrak{g})(r)=\lambda(r)$ for any $r \in[0, \varepsilon)$.
\end{itemize}

Moreover, it holds that:
\begin{itemize}
\item[-] if there exist $\tilde{\varepsilon} \geqslant \varepsilon$ and $\tilde{f}, \tilde{h}:[0, \tilde{\varepsilon}) \rightarrow \mathbb{R}$ satisfying the conditions (I), (II), (III) above, then $\tilde{f}(r)=f(r)$ and $\tilde{h}(r)=h(r)$ for any $r \in[0, \varepsilon)$;
\item[-] $f, h$ depends continuously on the data $a, \lambda$.
\end{itemize}

Proof. Fix a positive number $a>0$ and an admissible function $\lambda: I \rightarrow \mathbb{R}$. Let us write
$$x(r):=\frac{f(r)}{r}, \quad y(r):=x^{\prime}(r), z(r):=h(r), w(r):=h^{\prime}(r) .$$
Then, a straightforward computation shows that equations (5.1) become
$$\left\{\begin{array}{l}
v^{\prime}(r)=\frac{1}{r} A \cdot v(r)+N(r, v(r)) \\
v(0)=v_{\mathrm{o}}
\end{array},\right.$$
with
$$\begin{aligned}
& v(r)=(x(r), y(r), z(r), w(r))^{t}, \quad A:=\left(\begin{array}{cccc}
0 & 0 & 0 & 0 \\
0 & -2 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & -1
\end{array}\right), \\
& N(r, v):=\left(\begin{array}{c}
\left(\frac{2 m(m-1) n}{p} x^{2}-\frac{\lambda}{2 m} x\right)+r\left(\frac{2 m(m-1) n}{p} x y\right) \\
+r^{2}\left(\frac{2 m^{2}(m-1) n^{2}}{p^{2}} \frac{x^{3}}{z^{4}}\right)^{w} \\
\left(\frac{w^{2}}{z}-\frac{y w}{x}+\frac{2 m}{z}-\frac{\lambda}{2 m} z\right)+r\left(\frac{2 m(m-1) n}{2} \frac{x w}{z^{2}}\right) \\
+r^{2}\left(-\frac{2 m^{2}(m-1) n^{2}}{p^{2}} \frac{x^{2}}{z^{3}}\right)^{p}
\end{array}\right) .
\end{aligned}$$

Moreover, the smoothness conditions for the functions $f$ and $h$, together with the equation $h(0)=a$, imply that
$$v_{\mathrm{o}}=(1,0, a, 0)^{t} .$$
We stress now that the following conditions are satisfied:
\begin{itemize}
\item[-] the function $N=N(r, v)$ is smooth in a neighbourhood of ( $0, v_{\mathrm{o}}$ ),
\item[-] $A \cdot v_{\mathrm{o}}=0$,
\item[-] $\operatorname{det}\left(A-k \mathrm{Id}_{4}\right) \neq 0$ for any integer $k \geqslant 1$.
\end{itemize}

Then, by the Malgrange theorem [39, theorem 7.1], see also [14, theorem 2.2], there exists a unique solution $v(r)$, defined on an interval $(-\varepsilon, \varepsilon)$, to equation (5.3) with initial condition (5.4), which depends continuously on the data $a, \lambda$.

By equation (5.2), we obtain a pair $(f, h)$ of smooth functions $f, h:(-\varepsilon, \varepsilon) \rightarrow \mathbb{R}$ which satisfy equations (5.1) such that
$$f(0)=0, \quad f^{\prime}(0)=1, f^{\prime \prime}(0)=0, h(0)=a, h^{\prime}(0)=0 .$$
Since the pair $(\hat{f}, \hat{h})$ of functions defined by
$$\hat{f}, \hat{h}:(-\varepsilon, \varepsilon) \rightarrow \mathbb{R}, \quad \hat{f}(r):=-f(-r), \hat{h}(r):=h(-r)$$
satisfy equations (5.1) with the initial conditions (5.5), by uniqueness we conclude that $f$ is odd and $h$ is even. Therefore, these functions give rise to a smooth Hermitian metric $\mathfrak{g}=\mathfrak{g}(f, h)$ on the open set $\mathcal{U}_{\varepsilon}^{\text {reg }} \subset M_{(i, n)}(\mathrm{G}, \mathrm{K})^{\text {reg }}$, which admits a unique smooth extension over the singular orbit $\mathrm{G} \cdot \gamma(0)$. \(\square\)

Concerning complete solutions to equations (5.1), we point out the following

Remark 5.2. Fundamental examples of complete, non-Kähler, second-Chern-Einstein metrics can be easily found on the manifolds $\left(M_{(1, n)}(\mathrm{G}, \mathrm{K}), \complement\right)$ and $\left(M_{(3, n)}(\mathrm{G}, \mathrm{K})\right.$, J $)$. Indeed, the constant functions
$$f(r):=\frac{p}{m n}, \quad h(r):=1$$
verify the smoothness conditions in case $i=1,3$ and so they give rise to homogeneous, smooth metrics which are non-Kähler by equation (3.11) and second-Chern-Einstein by equation (5.1) with constant Chern-scalar curvature $\lambda=4 m(m-1)$. These examples include the standard metric on the linear Hopf manifold (see example 3.8).

We also stress that, on manifolds $\left(M_{(1, n)}(\mathrm{G}, \mathrm{K}), J\right)$ and $\left(M_{(3, n)}(\mathrm{G}, \mathrm{K})\right.$, J) , all the metrics (not necessarily of cohomogeneity one) in the conformal class of $\mathfrak{g}=g(f, h)$, with $f, h$ given by formula (5.6), are second-Chern-Einstein (see remark 2.4). In particular, by remark 3.11, for any admissible positive function $\phi: I \rightarrow \mathbb{R}$, the pair
$$f_{\phi}(r):=\frac{p}{m n} \phi(r), \quad h_{\phi}(r):=\phi(r)$$
solve equations (5.1) with Chern-scalar curvature $\lambda(r)=2 m\left(-\frac{\phi^{\prime \prime}(r)}{\phi(r)}\right.$ $+2(m-1) \frac{\phi^{\prime}(r)+1}{\phi(r)}$ ). Therefore, in the following, we will focus on Bérard-Bergery manifolds $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}\right)$ with singular orbits, namely, the cases $i=2$ and $i=4$.

\subsection*{5.2. Complete second-Chern-Einstein metrics in case of singular orbits}

In this section, we will construct complete second-Chern-Einstein metrics on the manifolds $\left(M_{(2, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}\right)$ by using the same technique as [9, §11].

Let us start by noticing that, for the manifold $\mathcal{O}_{\mathbb{C P}^{m-1}}(-1)$, the functions
$$f(r):=r, \quad h_{k}(r):=\sqrt{r^{2}+k^{2}}, \quad r \in[0,+\infty), k>0$$
solve the second-Chern-Einstein equations (5.1) and define Hermitian metrics $\mathbb{g}_{k}=$ $\mathbb{g}\left(f, h_{k}\right)$ which extend smoothly over the singular orbit. All the metrics $\mathbb{g}_{k}$ are non-Kähler and their Chern-scalar curvatures are given by
$$\operatorname{scal}^{\mathrm{Ch}}\left(\mathrm{~g}_{k}\right)(r)=4 m(m-1) \frac{2 r^{2}+k^{2}}{\left(r^{2}+k^{2}\right)^{2}} .$$
Note that all these metrics are homothetic, indeed the satisfy $\mathfrak{g}_{k}=k^{2} \mathbb{g}_{1}$ (see remark 3.11). More in general, we have

Theorem 5.3. All the complex manifolds $\left(M_{(2, n)}(\mathrm{G}, \mathrm{K}), J^{)}\right)$have a complete, Hermitian, non-Kähler, second-Chern-Einstein, cohomogeneity one metric.

Proof. Fix a manifold $\left(M_{(2, n)}(\mathrm{G}, \mathrm{K}), J^{\prime}\right)$ and set
$$f_{\phi}(r):=\frac{p}{2 m n} \phi^{\prime}(r), \quad h_{\phi}(r):=\sqrt{\phi(r)}$$
for some smooth, positive, increasing function $\phi:[0,+\infty) \rightarrow \mathbb{R}$. Note that, in this case
$$h_{\phi}(r) h_{\phi}^{\prime}(r)+\frac{m n}{p} f_{\phi}(r)=\phi^{\prime}(r)$$
and so this metric is necessarily non-Kähler by equation (3.11). Setting the initial condition $h(0)=1$, second-Chern-Einstein equations (5.1) become
$$\left\{\begin{array}{l}
\phi(r) \frac{\phi^{\prime \prime \prime}(r)}{\phi^{\prime}(r)}-m \phi^{\prime \prime}(r)+2 m=0 \\
\phi(0)=1, \quad \phi^{\prime}(0)=0, \phi^{\prime \prime}(0)=\frac{2 m n}{p}
\end{array} .\right.$$
Cauchy problem (5.10) admits a unique smooth solution on some interval $[0, \varepsilon)$, which extends to an even smooth function on $(-\varepsilon, \varepsilon)$. Let us prove that this solution can be extended to the whole $[0,+\infty)$.

Assume that the solution to equation (5.10) is of the form
$$\phi^{\prime}(r)=\sqrt{u(\phi(r))} .$$
Then, from equations (5.10) and (5.11), we get the following Cauchy problem for $u(t)$ :
$$\left\{\begin{array}{l}
t u^{\prime \prime}(t)-m u^{\prime}(t)+4 m=0 \\
u(1)=0, \quad u^{\prime}(1)=\frac{4 m n}{p}
\end{array} .\right.$$
The unique solution to equation (5.12) is the function $u:[1,+\infty) \rightarrow \mathbb{R}$ defined by
$$u(t):=-\frac{4 m(n+p)}{p(m+1)}+4 t+\frac{4(m n-p)}{p(m+1)} t^{m+1},$$
which is smooth, positive and increasing. Hence, the function
$$\varphi:[1,+\infty) \rightarrow \mathbb{R}, \quad \varphi(r):=\int_{1}^{r} \frac{\mathrm{~d} t}{\sqrt{u(t)}}$$
is smooth, positive, increasing and, by construction, its inverse $\phi:=\varphi^{-1}$ solves the Cauchy problem (5.10). Therefore, by means of equation (5.9), the proof is completed. \(\square\)

Remark 5.4. The Chern-scalar curvature of the metric $\mathbb{g}_{\phi}=g\left(f_{\phi}, h_{\phi}\right)$ constructed from equation (5.9) by solving Cauchy problem (5.10) is given by
$$\operatorname{scal}^{\mathrm{Ch}}\left(\mathbb{g}_{\phi}\right)(r)=2 m\left(-\frac{\phi^{\prime \prime \prime}(r)}{\phi^{\prime}(r)}+(m-1) \frac{\phi^{\prime \prime}(r)}{\phi(r)}+(m-1)\left(\frac{\phi^{\prime}(r)}{\phi(r)}\right)^{2}\right) .$$
Note that, if $m n-p=0$, which correspond to the manifolds $\mathcal{O}_{\mathbb{C P}^{m-1}}(-1)$, function (5.13) is $u(t)=4(t-1)$. Hence, we recover the family of examples introduced in formula (5.8).

Finally we observe that, concerning the compact simply-connected manifolds $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}\right)$, we have the following

Proposition 5.5. On the complex manifolds $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ there are no cohomogeneity one, submersion-type Hermitian metrics that are second-Chern-Einstein.

Proof. Assume that there exists cohomogeneity one, submersion-type Hermitian metric $\mathbb{g}$ on a complex manifold $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ which is second-Chern-Einstein. Then, by corollary 4.2, it is globally conformally Kähler. By remark 2.4, this implies the existence of a Kähler-Einstein metric on $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K})\right.$, J) , that is not possible (see [9, remarques 8.14, (1)] and [10, remarks 9.126, (b)]). \(\square\)

Remark 5.6. The projective space $\mathbb{C P}^{m}$ is a standard cohomogeneity one manifold with respect to the action of $\mathrm{G}=\mathrm{SU}(m)$ given by $a \cdot\left[z^{0}: z\right]:=\left[z^{0}: a \cdot z\right]$. Even if it is not a Berard-Bérgéry manifold according to definition 3.7, all the formulas in § 3 and § 4 still apply to this specific case. In particular, all the G-invariant metrics on $\mathbb{C P}^{m}$ are of the form (3.10) with $n=1$ and $p=m$, where $f, h:\left[0, \frac{\pi}{2}\right] \rightarrow \mathbb{R}$ are smooth, positive function satisfying:
\begin{itemize}
\item[-] $f$ is the restriction of a smooth odd function on $\mathbb{R}$ satisfying
$$f\left(r+\frac{\pi}{2}\right)=-f\left(r-\frac{\pi}{2}\right) \quad \text { and } \quad f^{\prime}(0)=1=-f^{\prime}\left(\frac{\pi}{2}\right) ;$$
\item[-] $h$ is the restriction of a smooth even function on $\mathbb{R}$ satisfying
$$h\left(r+\frac{\pi}{2}\right)=-h\left(r-\frac{\pi}{2}\right) \quad \text { and } \quad h^{\prime}\left(\frac{\pi}{2}\right)=-1 .$$
\end{itemize}

Note that the Fubini-Study metric $\mathcal{G}_{\mathrm{FS}}$ with sectional curvature $1 \leqslant \sec \leqslant 4$ corresponds to the functions
$$f(r):=\frac{1}{2} \sin (2 r), \quad h(r):=\cos (r) .$$
As argued in the proof of proposition 5.5, all the G-invariant second-Chern-Einstein metrics on $\mathbb{C P}^{m}$ are necessarily conformal to the Fubini-Study metric $\mathbb{G}_{\mathrm{FS}}$. For example, the functions
$$f(r):=\frac{1}{2} \sin (2 r), \quad h_{k}(r):=\cos (r) \sqrt{\sin (r)^{2}+k^{2} \cos (r)^{2}}, k>0$$
define non-Kähler, second-Chern-Einstein metrics $\mathbb{g}_{k}$ on $\mathbb{C} \mathbb{P}^{m}$ of the form
$$\mathrm{g}_{k}=\varphi_{k}^{2} \mathrm{~g}_{\mathrm{FS}}, \quad \text { with } \quad \varphi_{k}(r):=\frac{k}{\cos (r)^{2}+k^{2} \sin (r)^{2}} .$$

\subsection*{5.3. Constant Chern-scalar curvature metrics in case of singular orbits}

In this section, we construct complete constant Chern-scalar curvature metrics $\mathbb{g}=\mathbb{g}(f, h)$ on the complex manifolds $\left(M_{(2, n)}(\mathrm{G}, \mathrm{K}), \sqrt{ }\right)$ and $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}\right)$ by using again the technique exploited in [9, §11].

Fix a complex manifold $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathcal{J}\right)$, with $i \in\{2,4\}$, and set
$$f_{\phi}(r):=\frac{p}{2 m n} \phi(r) \phi^{\prime}(r), \quad h_{\phi}(r):=\phi(r)$$
for some smooth, increasing, positive, function $\phi: I \rightarrow \mathbb{R}$. Note that, in this case,
$$h_{\phi}(r) h_{\phi}^{\prime}(r)+\frac{m n}{p} f_{\phi}(r)=\frac{1}{2} \phi(r) \phi^{\prime}(r)$$
and so this metric is necessarily non-Kähler by equation (3.11). Let $c \in \mathbb{R}$ to be fixed later. Then, the constant Chern-scalar curvature equation
$$\operatorname{scal}^{\mathrm{Ch}}\left(\mathrm{~g}_{\phi}\right)=c$$
for the metric $\mathbb{g}_{\phi}:=\mathbb{g}\left(f_{\phi}, h_{\phi}\right)$ becomes
$$\phi(r)^{2} \frac{\phi^{\prime \prime \prime}(r)}{\phi^{\prime}(r)}+(m+2) \phi(r) \phi^{\prime \prime}(r)-m(m-1) \phi^{\prime}(r)^{2}+\frac{c}{2} \phi(r)^{2}-2 m(m-1)=0 .$$
We look for a solution of the form
$$\phi^{\prime}(r)=\sqrt{u(\phi(r))}$$
for some smooth real function $u=u(t)$. Then, we get the following ODE
$$t^{2} u^{\prime \prime}(t)+(m+2) t u^{\prime}(t)-2 m(m-1) u(t)+c t^{2}-4 m(m-1)=0,$$
which can be explicitly integrated. Indeed, the following cases occur.
\begin{itemize}
\item[-] If $m=2$, then the solutions to equation (5.17) are
$$u_{a, b, c}(t)=a t^{-4}-2+b t-\frac{c}{6} t^{2}, \quad \text { with } a, b \in \mathbb{R} .$$
In this case, the base space of the fibration $M_{(i, n)}(\mathrm{G}, \mathrm{K}) \rightarrow P$ is necessarily $P=\mathbb{C P}^{1}$ and so $p=2$.
\item[-] If $m=3$, then the solutions to equation (5.17) are
$$u_{a, b, c}(t)=a t^{-6}-2+b t^{2}-\frac{c}{8} \log (t) t^{2}, \quad \text { with } a, b \in \mathbb{R} .$$
In this case, the only possibilities for the base space of the fibration $M_{(i, n)}(\mathrm{G}, \mathrm{K}) \rightarrow P$ are
$$P=\mathbb{C P}^{2}=\mathrm{SU}(3) / \mathrm{S}(\mathrm{U}(1) \times \mathrm{U}(2)), \quad P=\operatorname{Gr}\left(2, \mathbb{R}^{5}\right)=\mathrm{Sp}(2) / \mathrm{U}(2)$$
and so $p=3$.
\item[-] If $m>3$, then the solutions to equation (5.17) are given by
$$u_{a, b, c}(t)=a t^{-2 m}-2+\frac{c}{2(m+1)(m-3)} t^{2}+b t^{m-1}, \quad \text { with } a, b \in \mathbb{R} .$$
\end{itemize}

Then, by means of equations (5.14) and (5.16), we are able to construct constant Chern-scalar curvature metrics on the manifolds $\left(M_{(2, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ and $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}\right)$.

Theorem 5.7. Let $c \in \mathbb{R}, c \leqslant 0$. Then, all the complex manifolds $\left(M_{(2, n)}(\mathrm{G}, \mathrm{K}), J_{)}\right.$ have a complete, Hermitian, non-Kähler, cohomogeneity one metric $\mathfrak{g}$ with $\operatorname{scal}^{\mathrm{Ch}}(\mathrm{g})=c$.

Proof. Setting $h(0)=1$, the smoothness conditions for $f, h$ imply that
$$\phi(0)=1, \quad \phi^{\prime}(0)=0, \quad \phi^{\prime \prime}(0)=\frac{2 m n}{p} .$$
Let us stress that, if there exists a smooth solution $\phi:[0,+\infty) \rightarrow \mathbb{R}$ to equation (5.15) satisfying the boundary conditions (5.21), then it can be extended to a smooth even function on $\mathbb{R}$.

Note that, by means of equation (5.16), conditions (5.21) imply that the solution $u_{a, b, c}$ to the ODE (5.17) verifies
$$u_{a, b, c}(1)=0, \quad u_{a, b, c}^{\prime}(1)=\frac{4 m n}{p} .$$
Therefore, we obtain two values $a(c), b(c)$, depending on $c$, by imposing conditions (5.22):
\begin{itemize}
\item[-] if $m=2$, then by formula (5.18) we get
$$a(c):=\frac{2}{5}-\frac{c}{30}-\frac{4}{5} n, \quad b(c):=\frac{8}{5}+\frac{c}{5}+\frac{4}{5} n ;$$
\item[-] if $m=3$, then by formula (5.19) we get
$$a(c):=\frac{1}{2}-\frac{c}{64}-\frac{n}{2}, \quad b(c):=\frac{3}{2}+\frac{c}{64}+\frac{n}{2} ;$$
\item[-] if $m>3$, then by formula (5.20) we get
$$\begin{aligned}
& a(c):=-\frac{(m+1)(4 m(2 n-p)+4 p)+c p}{2 p(m+1)(3 m-1)}, \\
& b(c):=\frac{4 m(m-3)(n+p)-c p}{p(3 m-1)(m-3)} .
\end{aligned}$$
\end{itemize}

In all of these three cases it can be directly checked that, for any $c \leqslant 0$, the function $u_{c}:=u_{a(c), b(c), c}$ is positive and increasing for $t \in(1,+\infty)$. Indeed, by means of conditions (5.22), there exists $\varepsilon_{\mathrm{o}}>0$ such that $u_{c}(t)>0$ and $u_{c}^{\prime}(t)>0$ for any $t \in\left(1,1+\varepsilon_{\mathrm{o}}\right)$. Assume by contradiction that there exists $t_{\mathrm{o}}>1$ such that $u_{c}^{\prime}(t)>0$ for any $t \in\left[1, t_{\mathrm{o}}\right)$ and $u_{c}^{\prime}\left(t_{\mathrm{o}}\right)=0$. Then, $t_{\mathrm{o}}$ is a local maximum point or a stationary
point of inflection for $u(t)$, but equation (5.17) implies that
$$u_{c}^{\prime \prime}\left(t_{\mathrm{o}}\right)=2 m(m-1) \frac{u_{c}\left(t_{\mathrm{o}}\right)}{t_{\mathrm{o}}^{2}}-c+\frac{4 m(m-1)}{t_{\mathrm{o}}^{2}}>0,$$
which is not possible. Hence
$$\varphi_{c}:[1,+\infty) \rightarrow \mathbb{R}, \quad \varphi_{c}(r):=\int_{1}^{r} \frac{\mathrm{~d} t}{\sqrt{u_{c}(t)}}$$
is smooth, increasing and, by construction, its inverse $\phi_{c}:=\varphi_{c}^{-1}$ solves equation (5.15) with the initial conditions (5.21). \(\square\)

Constant Chern-scalar curvature metrics on Hirzebruch surfaces have been constructed by Koca and Lejmi by using the Bérard-Bergery ansatz in [33, theorem 1]. Since in complex dimension $m=2$ the complex manifolds $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K}), J^{0}\right)$ reduces to the Hirzebruch surfaces (see example 3.8), the next theorem extends their result to $m>2$.

Theorem 5.8. Let $c \in \mathbb{R}, c>0$. Then, all the complex manifolds $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ have a Hermitian, non-Kähler, cohomogeneity one metric $\mathbb{g}_{\text {with }} \operatorname{scal}^{\mathrm{Ch}}(\mathbb{g})=c$.

Proof. Setting $h(0)=1$ and $h(\pi)=k>1$, the smoothness conditions for $f, h$ imply that
$$\begin{array}{ll}
\phi(0)=1, & \phi^{\prime}(0)=0, \\
\phi(\pi)=k, & \phi^{\prime \prime}(\pi)=0,
\end{array} \quad \phi^{\prime \prime}(\pi)=-\frac{2 m n}{k p} .$$
Let us stress that, if there exists a smooth solution $\phi:[0, \pi] \rightarrow \mathbb{R}$ to equation (5.15) satisfying the boundary conditions (5.24), then it can be extended to a smooth even function on $\mathbb{R}$ satisfying $\phi(\pi+r)=\phi(\pi-r)$. Since the case $m=2$ has already been addressed in [33], we limit ourselves to prove the statement for $m \geqslant 3$.

Assume $m=3$. Then, by means of equation (5.16), conditions (5.24) imply that the solution $u_{a, b, c}$ given in formula (5.19) verifies
$$u_{a, b, c}(1)=0, \quad u_{a, b, c}(k)=0, \quad u_{a, b, c}^{\prime}(1)=4 n, \quad u_{a, b, c}^{\prime}(k)=-\frac{4 n}{k} .$$
By imposing the first three conditions
$$u_{a, b, c}(1)=0, \quad u_{a, b, c}(k)=0, \quad u_{a, b, c}^{\prime}(1)=4 n,$$
we obtain three values $a(k), b(k), c(k)$ depending on $k$, that are
$$\begin{aligned}
& a(k):=-\frac{2 k^{6}\left(6(n-1) \log (k) k^{2}+3\left(k^{2}-1\right)\right)}{(8 \log (k)-1) k^{8}+1}, \\
& b(k):=\frac{32\left((n+3) k^{8}-4 k^{6}-n+1\right)}{(8 \log (k)-1) k^{8}+1}, \\
& c(k):=\frac{32\left((n+3) k^{8}-4 k^{6}-n+1\right)}{(8 \log (k)-1) k^{8}+1} .
\end{aligned}$$

Set $u_{k}:=u_{a(k), b(k), c(k)}$ and observe that
$$u_{k}^{\prime}(k)+\frac{4 n}{k}=\frac{\alpha(k)}{\left.k(8 \log (k)-1) k^{8}+1\right)},$$
with
$$\begin{aligned}
\alpha(k):= & -4(n+3) k^{10}+32(n+1) k^{8} \log (k)-4(n-3) k^{8} \\
& +32(n-1) k^{2} \log (k)+4(n+3) k^{2}+4(n-3) .
\end{aligned}$$
Note that
$$\begin{aligned}
& \alpha(1)=\alpha^{\prime}(1)=\alpha^{\prime \prime}(1)=0, \quad \alpha^{\prime \prime \prime}(1)=512 n>0, \\
& \lim _{k \rightarrow+\infty} \alpha(k)=-\infty
\end{aligned}$$
and so there exists $\tilde{k}>1$ such that $\alpha(k)>0$ for any $1<k<\tilde{k}$ and $\alpha(\tilde{k})=0$. Then, we set $u:=u_{\tilde{k}}$, so that the function
$$\varphi:[1, \tilde{k}] \rightarrow[0, \pi], \quad \varphi(r):=\int_{1}^{r} \frac{\mathrm{~d} t}{\sqrt{u(t)}}$$
is smooth, increasing and its inverse $\phi:=\varphi^{-1}$ solves the ODE (5.15) with the boundary conditions (5.24).

Assume $m>3$. Then, by means of equation (5.16), conditions (5.24) imply that the solution $u_{a, b, c}$ given in formula (5.19) verifies
$$u_{a, b, c}(1)=0, \quad u_{a, b, c}(k)=0, \quad u_{a, b, c}^{\prime}(1)=\frac{4 m n}{p}, \quad u_{a, b, c}^{\prime}(k)=-\frac{4 m n}{k p} .$$
By imposing the first three conditions
$$u_{a, b, c}(1)=0, \quad u_{a, b, c}(k)=0, \quad u_{a, b, c}^{\prime}(1)=\frac{4 m n}{p},$$
we obtain three values $a(k), b(k), c(k)$ depending on $k$, that are
$$\begin{aligned}
& a(k):=\frac{2\left(2(m n-p) k^{m-1}+(m p-2 m n-p) k^{2}-p(m-3)\right)}{p\left(2(m+1) k^{m-1}-(3 m-1) k^{2}+(m-3) k^{-2 m}\right)}, \\
& b(k):=\frac{4\left(-m(n+p) k^{2}+(m n-p) k^{-2 m}+(m+1) p\right)}{p\left(2(m+1) k^{m-1}-(3 m-1) k^{2}+(m-3) k^{-2 m}\right)}, \\
& c(k):=\frac{4 \tilde{c}(k)}{p\left(2(m+1) k^{m-1}-(3 m-1) k^{2}+(m-3) k^{-2 m}\right)},
\end{aligned}$$
with
$$\begin{aligned}
\tilde{c}(k):= & 2 m(m+1)(m-3)(n+p) k^{m-1}-(3 m-1)(m+1)(m-3) p \\
& +\left(m^{3}(p-2 n)+m^{2}(4 n-3 p)+m(6 m n-p)+3 p\right) k^{-2 m} .
\end{aligned}$$

Set $u_{k}:=u_{a(k), b(k), c(k)}$ and observe that
$$u_{k}^{\prime}(k)+\frac{4 m n}{k p}=\frac{\alpha(k)}{p k^{2} \beta(k)},$$
where $\alpha(k), \beta(k)$ are the polynomials in $k$ defined by
$$\begin{aligned}
\alpha(k):= & -4 m(m-3)(n+p) k^{3 m+2}+4(m+1)((m-1) p+2 m n) k^{3 m} \\
& -4(3 m-1)(m n+p) k^{2 m+3}+4(3 m-1)(m n-p) k^{m} \\
& +4(m+1)((m-1) p-2 m n) k^{3}-4 m(m-3)(p-n) k, \\
\beta(k):= & 2(m+1) k^{3 m-1}-(3 m-1) k^{2(m+1)}+(m-3) .
\end{aligned}$$
Note that $\beta(1)=0$ and
$$\beta^{\prime}(k)=2(m+1)(3 m-1)\left(k^{m-3}-1\right) k^{2 m+1}>0 \text { for any } k>1,$$
hence $\beta(k)>0$ for any $k>1$. Moreover
$$\begin{aligned}
& \alpha(1)=\alpha^{\prime}(1)=\alpha^{\prime \prime}(1)=0, \\
& \alpha^{\prime \prime \prime}(1)=8 m n(3 m-1)(m-3)(m-1)(m+1)>0, \\
& \lim _{k \rightarrow+\infty} \alpha(k)=-\infty
\end{aligned}$$
and so there exists $\tilde{k}>1$ such that $\alpha(k)>0$ for any $1<k<\tilde{k}$ and $\alpha(\tilde{k})=0$. Then, we set $u:=u_{\tilde{k}}$, so that the function
$$\varphi:[1, \tilde{k}] \rightarrow[0, \pi], \quad \varphi(r):=\int_{1}^{r} \frac{\mathrm{~d} t}{\sqrt{u(t)}}$$
is smooth, increasing and its inverse $\phi:=\varphi^{-1}$ solves the ODE (5.15) with conditions (5.24).

Finally, by means of an argument similar to the one used in the proof of theorem 5.7 (see equation (5.23)), it holds necessarily that $c>0$ in all the cases. This concludes the proof. \(\square\)

\section*{Acknowledgements}

The authors are warmly grateful to Christoph Böhm, Simone Calamai, Liviu Ornea, Alexandra Otiman, Fabio Podestà, Andrea Spiro, Cristiano Spotti and Luigi Verdiani for several interesting discussions and suggestions on the topic.

The authors are supported by project PRIN2017 'Real and Complex Manifolds: Topology, Geometry and holomorphic dynamics' (code 2017JZ2SW5), and by GNSAGA of INdAM.

\section*{Appendix A.}

In this appendix, we provide the details for the proofs of proposition 3.15 computing the Chern-Ricci tensors of Bérard-Bergery manifolds $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}, \mathrm{g}\right)$, proposition 3.17 computing their torsion and the Lee form and equation (4.3) concerning the pluriclosed condition $\mathrm{dd}^{c} \omega=0$.

\section*{Appendix A.1. Proof of proposition 3.15}

Let $X, Y \in \mathfrak{p}$ be such that $Q(X, X)=Q(Y, Y)=1$ and $\left(e_{\alpha}, J e_{\alpha}\right)$ a $\left(Q_{\mathfrak{p}}, J\right)$ - unitary basis for $\mathfrak{p}$. Set $F:=\frac{2 m n}{\lambda p} f$. Then, by using formulas (2.4), (3.1), (3.2), (3.3), (3.4), (3.5), (3.8), (3.9), (3.10), proposition 3.3 and corollary 3.4, we get
$$\begin{aligned}
\mathfrak{g}\left(R^{\operatorname{Ch}}\right. & \left.(\mathbb{g})\left(N, T^{*}\right) N, T^{*}\right)_{\gamma}(r) \\
= & \mathbb{g}\left(\nabla_{\left[N, T^{*}\right]} N, T^{*}\right)_{\gamma(r)}-\mathfrak{g}\left(\nabla_{N} \nabla_{T^{*}} N, T^{*}\right)_{\gamma(r)}+\mathfrak{g}\left(\nabla_{T^{*}} \nabla_{N} N, T^{*}\right)_{\gamma(r)} \\
= & -\mathcal{L}_{N}\left(\mathfrak{g}\left(\nabla_{T^{*}} N, T^{*}\right)\right)_{\gamma(r)}+\mathfrak{g}\left(\nabla_{T^{*}} N, \nabla_{N} T^{*}\right)_{\gamma(r)} \\
& +\mathcal{L}_{T^{*}}\left(\mathfrak{g}\left(\nabla_{N} N, T^{*}\right)\right)_{\gamma(r)}-\mathbb{g}\left(\nabla_{N} N, \nabla_{T^{*}} T^{*}\right)_{\gamma(r)} \\
= & -F(r) \frac{\partial}{\partial r}\left(F^{\prime}(r) F(r)^{2}\right)+2 F^{\prime}(r)^{2} F(r)^{2} \\
= & -F(r)^{3} F^{\prime \prime}(r), \\
\mathfrak{g}\left(R^{\operatorname{Ch}}(\mathbb{g})\left(X^{*},(J X)^{*}\right) N, T^{*}\right)_{\gamma(r)} & \\
= & -\mathbb{g}\left(\nabla_{[X, J X]^{*}} N, T^{*}\right)_{\gamma(r)}-\mathfrak{g}\left(\nabla_{X^{*}} \nabla_{(J X)^{*}} N, T^{*}\right)_{\gamma(r)}+\mathfrak{g}\left(\nabla_{(J X)^{*}} \nabla_{X^{*}} N, T^{*}\right)_{\gamma(r)} \\
= & -\mathbb{g}\left(\nabla_{[X, J X]^{*}} N, T^{*}\right)_{\gamma(r)}-\mathcal{L}_{X^{*}}\left(\mathfrak{g}\left(\nabla_{(J X)^{*}} N, T^{*}\right)\right)_{\gamma(r)} \\
& +\mathbb{g}\left(\nabla_{(J X)^{*}} N, \nabla_{X^{*}} T^{*}\right)_{\gamma(r)} \\
& +\mathcal{L}_{(J X)^{*}}\left(\mathfrak{g}\left(\nabla_{X^{*}} N, T^{*}\right)\right)_{\gamma(r)}-\mathbb{g}\left(\nabla_{X^{*}} N, \nabla_{(J X)^{*}} T^{*}\right)_{\gamma(r)} \\
= & -\lambda F(r)^{2} F^{\prime}(r)+\frac{1}{2} \lambda^{2} F(r)^{2}+\lambda F(r)^{2} F^{\prime}(r)+\frac{1}{2} \lambda^{2} F(r)^{2}+\lambda F(r)^{2} F^{\prime}(r) \\
& -\frac{1}{4} \lambda^{2} F(r)^{2}\left(2-\frac{F(r)^{2}}{h(r)^{2}}\right)-\frac{1}{4} \lambda^{2} F(r)^{2}\left(2-\frac{F(r)^{2}}{h(r)^{2}}\right) \\
= & \lambda F(r)^{2} F^{\prime}(r)+\frac{1}{2} \lambda^{2} \frac{F(r)^{4}}{h(r)^{2}}, \\
\mathfrak{g}\left(R^{\operatorname{Ch}}\right. & \left.(\mathbb{g})\left(N, T^{*}\right) X^{*},(J X)^{*}\right)_{\gamma(r)} \\
= & \mathbb{g}\left(\nabla_{\left[N, T^{*}\right]} X^{*},(J X)^{*} \gamma_{(r)}-\mathbb{g}\left(\nabla_{N} \nabla_{T^{*}} X^{*},(J X)^{*}\right)_{\gamma(r)}\right. \\
& +\mathbb{g}\left(\nabla_{T^{*}} \nabla_{N} X^{*},(J X)^{*}\right)_{\gamma(r)} \\
= & -\mathcal{L}_{N}\left(\mathbb{g}\left(\nabla_{T^{*}} X^{*},(J X)^{*}\right)\right)_{\gamma(r)}+\mathfrak{g}\left(\nabla_{T^{*}} X^{*}, \nabla_{N}(J X)^{*}\right)_{\gamma(r)} \\
& +\mathcal{L}_{T^{*}}\left(\mathfrak{g}\left(\nabla_{N} X^{*},(J X)^{*}\right)\right)_{\gamma(r)}-\mathbb{g}\left(\nabla_{N} X^{*}, \nabla_{T^{*}}(J X)^{*}\right)_{\gamma(r)} \\
= & -F(r) \frac{\partial}{\partial r}\left(F(r) h(r) h^{\prime}(r)\right)+2 F(r)^{2} h^{\prime}(r)^{2} \\
= & -F(r)^{2} h(r)^{2}\left(\frac{h^{\prime \prime}(r)}{h(r)}-\frac{h^{\prime}(r)^{2}}{h(r)^{2}}+\frac{F^{\prime}(r)}{F(r)} \frac{h^{\prime}(r)}{h(r)}\right) .
\end{aligned}$$

Hence, we obtain
$$\begin{aligned}
\operatorname{Ric}^{\operatorname{Ch}[1]}(\mathrm{g})(N, N)_{\gamma(r)} & \\
= & F(r)^{-2} g\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(N, T^{*}\right) N, T^{*}\right)_{\gamma(r)} \\
& +h(r)^{-2} \sum_{e_{\alpha} \in \mathfrak{p}} g\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(N, T^{*}\right) e_{\alpha}^{*},\left(J e_{\alpha}\right)^{*}\right)_{\gamma(r)} \\
= & -F(r) F^{\prime \prime}(r)-(m-1) F(r)^{2}\left(\frac{h^{\prime \prime}(r)}{h(r)}-\frac{h^{\prime}(r)^{2}}{h(r)^{2}}+\frac{F^{\prime}(r)}{F(r)} \frac{h^{\prime}(r)}{h(r)}\right) \\
= & F(r)^{2}\left(-\frac{F^{\prime \prime}(r)}{F(r)}-(m-1) \frac{h^{\prime \prime}(r)}{h(r)}+(m-1) \frac{h^{\prime}(r)}{h(r)}\left(\frac{h^{\prime}(r)}{h(r)}-\frac{F^{\prime}(r)}{F(r)}\right)\right) \\
= & \frac{2 m(m-1) n^{2}}{p^{2}} f(r)^{2}\left(-\frac{f^{\prime \prime}(r)}{f(r)}+(m-1)\left(-\frac{h^{\prime \prime}(r)}{h(r)}+\frac{h^{\prime}(r)^{2}}{h(r)^{2}}-\frac{f^{\prime}(r)}{f(r)} \frac{h^{\prime}(r)}{h(r)}\right)\right)
\end{aligned}$$
and
$$\begin{aligned}
\operatorname{Ric}^{\mathrm{Ch}[2]}(\mathrm{g})(N, N)_{\gamma(r)} & \\
= & F(r)^{-2} g\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(N, T^{*}\right) N, T^{*}\right)_{\gamma(r)} \\
& +h(r)^{-2} \sum_{e_{\alpha} \in \mathfrak{p}} g\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(e_{\alpha}^{*},\left(J e_{\alpha}\right)^{*}\right) N, T^{*}\right)_{\gamma(r)} \\
= & -F(r) F^{\prime \prime}(r)+(m-1) h(r)^{-2}\left(\lambda F(r)^{2} F^{\prime}(r)+\frac{1}{2} \lambda^{2} \frac{F(r)^{4}}{h(r)^{2}}\right) \\
= & F(r)^{2}\left(-\frac{F^{\prime \prime}(r)}{F(r)}+(m-1) \lambda \frac{F^{\prime}(r)}{h(r)^{2}}+\frac{1}{2}(m-1) \lambda^{2} \frac{F(r)^{2}}{h(r)^{4}}\right) \\
= & \frac{2 m(m-1) n^{2}}{p^{2}} f(r)^{2}\left(-\frac{f^{\prime \prime}(r)}{f(r)}+\frac{2 m(m-1) n}{p} \frac{f^{\prime}(r)}{h(r)^{2}}+\frac{2 m^{2}(m-1) n^{2}}{p^{2}} \frac{f(r)^{2}}{h(r)^{4}}\right) .
\end{aligned}$$
By the symmetries of the tensors $\operatorname{Ric}^{\operatorname{Ch[i]}}(\mathrm{g})$, it holds that
$$\operatorname{Ric}^{\operatorname{Ch}[\mathrm{i}]}(\mathrm{g})\left(T^{*}, T^{*}\right)_{\gamma(r)}=\operatorname{Ric}^{\operatorname{Ch}[\mathrm{i}]}(\mathrm{g})(N, N)_{\gamma(r)} \quad \text { and } \quad \operatorname{Ric}^{\operatorname{Ch}[\mathrm{i}]}(\mathrm{g})\left(N, T^{*}\right)_{\gamma(r)}=0 .$$
Moreover, by a direct computation, we get
$$\begin{aligned}
& \mathrm{g}\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(N,(J X)^{*}\right) N, T^{*}\right)_{\gamma(r)}=\mathrm{g}\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(N, T^{*}\right) N,(J X)^{*}\right)_{\gamma(r)}=0, \\
& \mathrm{~g}\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(N,(J X)^{*}\right) Y^{*},(J Y)^{*}\right)_{\gamma(r)}=\mathrm{g}\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(Y^{*},(J Y)^{*}\right) N,(J X)^{*}\right)_{\gamma(r)}=0
\end{aligned}$$
and hence
$$\operatorname{Ric}^{\operatorname{Ch}[\mathrm{i}]}(\mathrm{g})\left(N, X^{*}\right)_{\gamma(r)}=\operatorname{Ric}^{\operatorname{Ch}[\mathrm{i}]}(\mathrm{g})\left(T, X^{*}\right)_{\gamma(r)}=0 .$$

Finally, we have
$$\begin{aligned}
\mathfrak{g}\left(R^{\operatorname{Ch}}\right. & \left.(\mathbb{g})\left(N, T^{*}\right) X^{*},(J X)^{*}\right)_{\gamma(r)} \\
= & \mathbb{g}\left(\nabla_{\left[N, T^{*}\right]} X^{*},(J X)^{*}\right)_{\gamma(r)}-\mathfrak{g}\left(\nabla_{N} \nabla_{T^{*}} X^{*},(J X)^{*}\right)_{\gamma(r)} \\
& +\mathbb{g}\left(\nabla_{T^{*}} \nabla_{N} X^{*},(J X)^{*}\right)_{\gamma(r)} \\
= & -\mathcal{L}_{N}\left(\mathfrak{g}\left(\nabla_{T^{*}} X^{*},(J X)^{*}\right)\right)_{\gamma(r)}+\mathbb{g}\left(\nabla_{T^{*}} X^{*}, \nabla_{N}(J X)^{*}\right)_{\gamma(r)} \\
& +\mathcal{L}_{T^{*}}\left(\mathfrak{g}\left(\nabla_{N} X^{*},(J X)^{*}\right)\right)_{\gamma(r)}-\mathbb{g}\left(\nabla_{N} X^{*}, \nabla_{T^{*}}(J X)^{*}\right)_{\gamma(r)} \\
= & -F(r) \frac{\partial}{\partial r}\left(F(r) h(r) h^{\prime}(r)\right)+2 F(r)^{2} h^{\prime}(r)^{2} \\
= & -F(r)^{2} h(r)^{2}\left(\frac{h^{\prime \prime}(r)}{h(r)}-\frac{h^{\prime}(r)^{2}}{h(r)^{2}}+\frac{F^{\prime}(r)}{F(r)} \frac{h^{\prime}(r)}{h(r)}\right), \\
\mathfrak{g}\left(R^{\operatorname{Ch}}\right. & \left.(\mathbb{g})\left(X^{*},(J X)^{*}\right) Y^{*},(J Y)^{*}\right)_{\gamma(r)} \\
= & -\mathbb{g}\left(\nabla_{[X, J X)^{*}} Y^{*},(J Y)^{*}\right)_{\gamma(r)}-\mathbb{g}\left(\nabla_{X^{*}} \nabla_{(J X)^{*}} Y^{*},(J Y)^{*}\right)_{\gamma(r)} \\
& +\mathbb{g}\left(\nabla_{(J X)^{*}} \nabla_{X^{*}} Y^{*},(J Y)^{*}\right)_{\gamma(r)} \\
= & -\lambda g\left(\nabla_{T^{*}} Y^{*},(J Y)^{*}\right)_{\gamma(r)}-\mathcal{L}_{X^{*}}\left(\mathfrak{g}\left(\nabla_{(J X)^{*}} Y^{*},(J Y)^{*}\right)\right)_{\gamma(r)} \\
& +\mathbb{g}\left(\nabla_{(J X)^{*}} Y^{*}, \nabla_{X^{*}}(J Y)^{*}\right)_{\gamma(r)} \\
& +\mathcal{L}_{(J X)^{*}}\left(\mathfrak{g}\left(\nabla_{X^{*}} Y^{*},(J Y)^{*}\right)\right)_{\gamma(r)}-\mathbb{g}\left(\nabla_{X^{*}} Y^{*}, \nabla_{(J X)^{*}}(J Y)^{*}\right)_{\gamma(r)} \\
= & -\lambda g\left(\nabla_{T^{*}} Y^{*},(J Y)^{*}\right)_{\gamma(r)}+2 \mathbb{g}\left(\nabla_{(J X)^{*}} Y^{*}, \nabla_{X^{*}}(J Y)^{*}\right)_{\gamma(r)} \\
& -\mathcal{L}_{X^{*}}\left(\mathfrak{g}\left(\nabla_{(J X)^{*}} Y^{*},(J Y)^{*}\right)\right)_{\gamma(r)}+\mathcal{L}_{(J X)^{*}}\left(\mathfrak{g}\left(\nabla_{X^{*}} Y^{*},(J Y)^{*}\right)\right)_{\gamma(r)} \\
= & -\lambda F(r) h(r) h^{\prime}(r) \\
& +\frac{1}{2} h(r)^{2}\left(|[X, Y]|_{Q}^{2}+|[X, J Y]|_{Q}^{2}+|[J X, Y]|_{Q}^{2}+|[J X, J Y]|_{Q}^{2}\right) \\
& +2 \lambda F(r) h(r) h^{\prime}(r)-\frac{1}{2} F(r)^{2}\left(Q([T, X], Y)^{2}+Q([T, X], J Y)^{2}\right) \\
= & h(r)^{2}\left(\lambda F(r) \frac{h^{\prime}(r)}{h(r)}-\frac{1}{2} \lambda^{2} \frac{F(r)^{2}}{h(r)^{2}}\left(Q(X, Y)^{2}+Q(J X, Y)^{2}\right)\right. \\
& \left.+\frac{1}{2}\left(|[X, Y]|_{Q}^{2}+|[X, J Y]|_{Q}^{2}+|[J X, Y]|_{Q}^{2}+|[J X, J Y]|_{Q}^{2}\right)\right) .
\end{aligned}$$
Note that
$$\sum_{e_{\alpha} \in \mathfrak{p}}\left(Q\left(X, e_{\alpha}\right)^{2}+Q\left(X, J e_{\alpha}\right)^{2}\right)=1 .$$

Moreover, setting $\left(\tilde{e}_{\alpha}\right):=\left(e_{\alpha}, J e_{\alpha}\right)$, since $[\mathfrak{p}, \mathfrak{p}] \subset \mathfrak{k}$ and $|X|_{Q}=1$, by the Schur lemma we obtain
$$\begin{aligned}
& \sum_{e_{\alpha} \in \mathfrak{p}}\left(\left|\left[X, e_{\alpha}\right]\right|_{Q}^{2}+\left|\left[X, J e_{\alpha}\right]\right|_{Q}^{2}+\left|\left[J X, e_{\alpha}\right]\right|_{Q}^{2}+\left|\left[J X, J e_{\alpha}\right]\right|_{Q}^{2}\right) \\
& \quad=\frac{1}{m-1} \sum_{\tilde{e}_{\alpha}, \tilde{e}_{\beta} \in \mathfrak{p}}\left|\left[\tilde{e}_{a}, \tilde{e}_{\beta}\right] \mathfrak{k}\right|_{Q}^{2}=4 m .
\end{aligned}$$
Hence, we get
$$\begin{aligned}
& \operatorname{Ric}^{\mathrm{Ch}[1]}(\mathrm{g})\left(X^{*}, X^{*}\right)_{\gamma(r)} \\
&= F(r)^{-2} g\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(X^{*},(J X)^{*}\right) N, T^{*}\right)_{\gamma(r)} \\
&+h(r)^{-2} \sum_{e_{\alpha} \in \mathfrak{p}} g\left(R^{\mathrm{Ch}}(\mathrm{~g})\left(X^{*},(J X)^{*}\right) e_{\alpha}^{*},\left(J e_{\alpha}\right)^{*}\right)_{\gamma(r)} \\
&= \lambda F^{\prime}(r)+\frac{1}{2} \lambda^{2} \frac{F(r)^{2}}{h(r)^{2}}+(m-1) \lambda F(r) \frac{h^{\prime}(r)}{h(r)}-\frac{1}{2} \lambda^{2} \frac{F(r)^{2}}{h(r)^{2}}+2 m \\
&= h(r)^{2}\left(\lambda \frac{F(r)}{h(r)^{2}}\left(\frac{F^{\prime}(r)}{F(r)}+(m-1) \frac{h^{\prime}(r)}{h(r)}\right)+\frac{2 m}{h(r)^{2}}\right) \\
&= h(r)^{2}\left(\frac{2 m n}{p} \frac{f(r)}{h(r)^{2}}\left(\frac{f^{\prime}(r)}{f(r)}+(m-1) \frac{h^{\prime}(r)}{h(r)}\right)+\frac{2 m}{h(r)^{2}}\right)
\end{aligned}$$
and
$$\begin{aligned}
\operatorname{Ric}^{\mathrm{Ch}[2]}(\mathrm{g})\left(X^{*}, X^{*}\right)_{\gamma(r)} & \\
= & F(r)^{-2} g\left(R^{\mathrm{Ch}}\left(N, T^{*}\right) X^{*},(J X)^{*}\right)_{\gamma(r)} \\
& +h(r)^{-2} \sum_{e_{\alpha} \in \mathfrak{p}} g\left(R^{\mathrm{Ch}}\left(e_{\alpha}^{*},\left(J e_{\alpha}\right)^{*}\right) X^{*},(J X)^{*}\right)_{\gamma(r)} \\
= & -h(r)^{2}\left(\frac{h^{\prime \prime}(r)}{h(r)}-\frac{h^{\prime}(r)^{2}}{h(r)^{2}}+\frac{F^{\prime}(r)}{F(r)} \frac{h^{\prime}(r)}{h(r)}\right) \\
& +(m-1) \lambda F(r) \frac{h^{\prime}(r)}{h(r)}-\frac{1}{2} \lambda^{2} \frac{F(r)^{2}}{h(r)^{2}}+2 m \\
= & h(r)^{2}\left(-\frac{h^{\prime \prime}(r)}{h(r)}+\frac{h^{\prime}(r)^{2}}{h(r)^{2}}-\frac{F^{\prime}(r)}{F(r)} \frac{h^{\prime}(r)}{h(r)}\right. \\
& \left.+(m-1) \lambda F(r) \frac{h^{\prime}(r)}{h(r)^{3}}-\frac{1}{2} \lambda^{2} \frac{F(r)^{2}}{h(r)^{4}}+\frac{2 m}{h(r)^{2}}\right) \\
= & h(r)^{2}\left(-\frac{h^{\prime \prime}(r)}{h(r)}+\frac{h^{\prime}(r)^{2}}{h(r)^{2}}-\frac{f^{\prime}(r)}{f(r)} \frac{h^{\prime}(r)}{h(r)}+\frac{2 m(m-1) n}{p} f(r) \frac{h^{\prime}(r)}{h(r)^{3}}\right. \\
& \left.-2\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{4}}+\frac{2 m}{h(r)^{2}}\right)
\end{aligned}$$
which concludes the proof of equations (3.12), (3.13) and (3.14).
For what concerns the scalar curvature, we have
$$\begin{aligned}
\operatorname{scal}^{\operatorname{Ch}}(\mathrm{g})(r)= & 2 F(r)^{-2} \operatorname{Ric}^{\operatorname{Ch}[2]}(\mathrm{g})\left(T^{*}, T^{*}\right)_{\gamma(r)} \\
& +2 h(r)^{-2} \sum_{e_{\alpha} \in \mathfrak{p}} \operatorname{Ric}^{\operatorname{Ch}[2]}(\mathbb{g})\left(e_{\alpha}^{*}, e_{\alpha}^{*}\right)_{\gamma(r)} \\
= & -2 \frac{f^{\prime \prime}(r)}{f(r)}-2(m-1) \frac{h^{\prime \prime}(r)}{h(r)} \\
& \quad+2(m-1)\left(\frac{h^{\prime}(r)}{h(r)}-\frac{f^{\prime}(r)}{f(r)}\right) \frac{h^{\prime}(r)}{h(r)}+4 m(m-1) \frac{1}{h(r)^{2}} \\
& \quad+\frac{4 m(m-1) n}{p}\left(f^{\prime}(r)+(m-1) f(r) \frac{h^{\prime}(r)}{h(r)}\right) \frac{1}{h(r)^{2}}
\end{aligned}$$
which proves equation (3.15).

\section*{Appendix A.2. Proof of proposition 3.17}

By equation (3.16) and corollary 3.16, the only non-vanishing components of $\tau$ are
$$\begin{aligned}
\mathrm{g}\left(\tau\left(X^{*}, T^{*}\right), Z^{*}\right)_{\gamma(r)} & =-\frac{2 m n}{\lambda p} f(r)\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right) Q_{\mathfrak{p}}(J X, Z), \\
\mathrm{g}\left(\tau\left(X^{*}, N\right), Z^{*}\right)_{\gamma(r)} & =-\frac{2 m n}{\lambda p} f(r)\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right) Q_{\mathfrak{p}}(X, Z),
\end{aligned}$$
and so $\tau\left(N, T^{*}\right)_{\gamma(r)}=\tau\left(X^{*}, Y^{*}\right)_{\gamma(r)}=0$. Moreover, letting $\left(e_{\alpha}, J e_{a}\right)$ be a $\left(Q_{\mathfrak{p}}, J\right)$ - unitary basis for $\mathfrak{p}$, we get
$$\begin{aligned}
\tau\left(N, X^{*}\right)_{\gamma(r)}= & -\left(\frac{2 m n}{\lambda p} f(r)\right)^{-2} \\
& \times\left(\mathfrak{g}\left(\tau\left(X^{*}, N\right), N\right)_{\gamma(r)} N_{\gamma(r)}+\mathfrak{g}\left(\tau\left(X^{*}, N\right), T^{*}\right)_{\gamma(r)} T_{\gamma(r)}^{*}\right) \\
& -h(r)^{-2} \sum_{e_{\alpha} \in \mathfrak{p}}\left(\mathfrak{g}\left(\tau\left(X^{*}, N\right), e_{\alpha}^{*}\right)_{\gamma(r)}\left(e_{\alpha}^{*}\right)_{\gamma(r)}\right. \\
& \left.+\mathbb{g}\left(\tau\left(X^{*}, N\right),\left(J e_{\alpha}\right)^{*}\right)_{\gamma(r)}\left(J e_{\alpha}\right)_{\gamma(r)}^{*}\right) \\
= & \frac{2 m n}{\lambda p} \frac{f(r)}{h(r)^{2}}\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right) X_{\gamma(r)}^{*} .
\end{aligned}$$
Therefore, by equations (3.2) and (3.4), it follows that
$$\tau\left(T^{*}, X^{*}\right)_{\gamma(r)}=\frac{2 m n}{\lambda p} \frac{f(r)}{h(r)^{2}}\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right)(J X)_{\gamma(r)}^{*} .$$

Finally
$$\begin{aligned}
\vartheta(N)_{\gamma(r)}= & \left(\frac{2 m n}{\lambda p} f(r)\right)^{-2}\left(\mathfrak{g}(\tau(N, N), N)_{\gamma(r)}+\mathbb{g}\left(\tau\left(N, T^{*}\right), T^{*}\right)_{\gamma(r)}\right) \\
& +h(r)^{-2} \sum_{e_{\alpha} \in \mathfrak{p}}\left(\mathfrak{g}\left(\tau\left(N, e_{\alpha}^{*}\right), e_{\alpha}^{*}\right)_{\gamma(r)}+\mathbb{g}\left(\tau\left(N,\left(J e_{\alpha}\right)^{*}\right),\left(J e_{\alpha}\right)^{*}\right)_{\gamma(r)}\right) \\
= & \frac{4 m(m-1) n}{\lambda p} \frac{f(r)}{h(r)^{2}}\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right),
\end{aligned}$$
and analogously one can show that $\vartheta\left(T^{*}\right)_{\gamma(r)}=\vartheta\left(X^{*}\right)_{\gamma(r)}=0$, which concludes the proof.

\section*{Appendix A.3. Proof of equation (4.3)}

Let us compute $\mathrm{dd}^{c} \omega$. Since $J \omega=\omega$, it follows that
$$\mathrm{d}^{c} \omega(A, B, C)=\mathrm{d} \omega(\nu A, \nu B, \nu C)$$
and so
$$\begin{aligned}
\operatorname{dd}^{c} \omega & (A, B, C, D) \\
= & \mathcal{L}_{A} \mathrm{~d} \omega(\sqrt{ } B, \sqrt{ } C, \sqrt{ } D)-\mathcal{L}_{B} \mathrm{~d} \omega(\sqrt{ } A, \sqrt{ } C, \sqrt{ } D) \\
& +\mathcal{L}_{C} \mathrm{~d} \omega(\nu A, \nu B, \nu D)-\mathcal{L}_{D} \mathrm{~d} \omega(\nu A, \nu B, \nu C) \\
& -\mathrm{d} \omega(\nu[A, B], \nu C, \nu D)+\mathrm{d} \omega(\nu[A, C], \nu B, \nu D)-\mathrm{d} \omega(\nu[A, D], \nu B, \nu C) \\
& -\mathrm{d} \omega(\nu[B, C], \nu A, \nu D)+\mathrm{d} \omega(\nu[B, D], \nu A, \nu C)-\mathrm{d} \omega(\nu[C, D], \nu A, \nu B) .
\end{aligned}$$
If $A$ is a holomorphic Killing vector field, then $\mathcal{L}_{A} \mathrm{~d} \omega=\mathrm{d} \mathcal{L}_{A} \omega=0$ and so
$$\begin{aligned}
\mathcal{L}_{A} \mathrm{~d} \omega(Л B, Л C, \Downarrow D)= & \mathrm{d} \omega(\Downarrow[A, B], \Downarrow C, \Downarrow D) \\
& +\mathrm{d} \omega(\Downarrow B, \Downarrow[A, C], \Downarrow D)+\mathrm{d} \omega(\Downarrow B, \Downarrow C, Л[A, D]) .
\end{aligned}$$
Therefore, if $A, B, C, D$ are holomorphic Killing, we get
$$\begin{aligned}
\mathrm{dd}^{c} \omega(A, B, C, D)= & +\mathrm{d} \omega(\nu[A, B], \nu C, \nu D)-\mathrm{d} \omega(\nu[A, C], \nu B, \nu D) \\
& +\mathrm{d} \omega(\nu[A, D], \nu B, \nu C)+\mathrm{d} \omega(\nu[B, C], \nu A, \nu D) \\
& -\mathrm{d} \omega(\nu[B, D], \nu A, \nu C)+\mathrm{d} \omega(\nu[C, D], \nu A, \nu B) .
\end{aligned}$$
Letting $\rho(X, Y)=Q_{\mathfrak{p}}(J X, Y)$, we have
$$\begin{aligned}
& (\rho \wedge \rho)(X, Y, Z, W) \\
& \quad=2(Q(J X, Y) Q(J Z, W)-Q(J X, Z) Q(J Y, W)+Q(J X, W) Q(J Y, Z))
\end{aligned}$$
and so, by using proposition 3.2 and equations (3.8), (3.10) we get
$$\begin{aligned}
\operatorname{dd}^{c} \omega & \left(X^{*}, Y^{*}, Z^{*}, W^{*}\right)_{\gamma(r)} \\
= & \lambda Q(J X, Y) \mathrm{d} \omega\left(Z^{*}, W^{*}, N\right)_{\gamma(r)}-\lambda Q(J X, Z) \mathrm{d} \omega\left(Y^{*}, W^{*}, N\right)_{\gamma(r)} \\
& +\lambda Q(J X, W) \mathrm{d} \omega\left(Y^{*}, Z^{*}, N\right)_{\gamma(r)}+\lambda Q(J Y, Z) \mathrm{d} \omega\left(X^{*}, W^{*}, N\right)_{\gamma(r)} \\
& -\lambda Q(J Y, W) \mathrm{d} \omega\left(X^{*}, Z^{*}, N\right)_{\gamma(r)}+\lambda Q(J Z, W) \mathrm{d} \omega\left(X^{*} Y^{*}, N\right)_{\gamma(r)} \\
= & 4 \frac{m n}{p} f(r)\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right)(\rho \wedge \rho)(X, Y, Z, W)
\end{aligned}$$
which concludes the proof.

\section*{References}
\begin{itemize}
\item[1] D. V. Alekseevsky and A. M. Perelomov. Invariant Kaehler-Einstein metrics on compact homogeneous spaces. Funct. Anal. Appl. 20 (1986), 171-182.
\item[2] D. V. Alekseevsky and F. Podestà. Homogeneous almost-Kähler manifolds and the Chern-Einstein equation. Math. Z. 296 (2020), 831-846.
\item[3] D. V. Alekseevsky and A. Spiro. Invariant CR structures on compact homogeneous manifolds. Hokkaido Math. J. 32 (2003), 209-276.
\item[4] D. V. Alekseevsky and F. Zuddas. Cohomogeneity one Kähler and Kähler-Einstein manifolds with one singular orbit I. Ann. Global Anal. Geom. 52 (2017), 99-128.
\item[5] D. V. Alekseevsky and F. Zuddas. Cohomogeneity one Kähler and Kähler-Einstein manifolds with one singular orbit II. Ann. Global Anal. Geom. 57 (2020), 153-174.
\item[6] D. Angella, S. Calamai and C. Spotti. On the Chern-Yamabe problem. Math. Res. Lett. 24 (2017), 645-677.
\item[7] D. Angella, S. Calamai and C. Spotti. Remarks on Chern-Einstein Hermitian metrics. Math. Z. 295 (2020), 1707-1722.
\item[8] Th. Aubin. Équations du type Monge-Ampère sur les variétés kählériennes compactes. Bull. Sci. Math. (2) 102 (1978), 63-95.
\item[9] L. Bérard-Bergery. Sur de nouvelles variétès riemanniennes d'Einstein. Institut Élie Cartan 6 (1982), 1-60. Inst. Élie Cartan, 6, Univ. Nancy, Nancy, 1982.
\item[10] A. L. Besse, Einstein manifolds, Ergebnisse der Mathematik und ihrer Grenzgebiete (3), Vol. 10 (Springer-Verlag, Berlin, 1987).
\item[11] W. M. Boothby. Hermitian manifolds with zero curvature. Michigan Math. J. 5 (1958), 229-233.
\item[12] M. Bordermann, M. Forger and H. Römer. Homogeneous Kähler Manifolds: paving the way towards new supersymmetric Sigma Models. Commun. Math. Phys. 102 (1986), 605-647.
\item[13] A. Borel and F. Hirzebruch. Characteristic classes and homogeneous spaces. I. Am. J. Math. 80 (1958), 458-538.
\item[14] C. Böhm. Inhomogeneous Einstein metrics on low-dimensional spheres and other low-dimensional spaces. Invent. Math. 134 (1998), 145-176.
\item[15] C. Böhm. Non-compact cohomogeneity one Einstein manifolds. Bull. Soc. Math. France 127 (1999), 135-177.
\item[16] G. E. Bredon, Introduction to compact transformation groups, Pure and Applied Mathematics, Vol. 46 (Academic Press, New York-London, 1972).
\item[17] A. Dancer and M. Y. Wang. Kähler Einstein metrics of cohomogeneity one and bundle construction for Einstein Hermitian metrics. Math. Ann. 312 (1998), 503-526.
\item[18] A. Derdziński and G. Maschler. Local classification of conformally-Einstein Kähler metrics in higher dimensions. Proc. London Math. Soc. 87 (2003), 779-819.
\item[19] S. Dragomir and L. Ornea, Locally conformal Kähler geometry, Progress in Mathematics, Vol. 155 (Birkhäuser Boston, Inc., Boston, MA, 1998).
\item[20] J.-H. Eschenburg and McK. Y. Wang. The initial value problem for cohomogeneity one Einstein metrics. J. Geom. Anal. 10 (2000), 109-137.
\end{itemize}
\begin{itemize}
\item[21] P. Gauduchon. Le théorème de l'excentricité nulle. C. R. Acad. Sci. Paris Sér. A-B 285 (1977), A387-A390.
\item[22] P. Gauduchon. La topologie d'une surface hermitienne d'Einstein. C. R. Acad. Sci. Paris Sér. A-B 290 (1980), A509-A512.
\item[23] P. Gauduchon. La 1-forme de torsion d'une variété hermitienne compacte. Math. Ann. 267 (1984), 495-518.
\item[24] P. Gauduchon and S. Ivanov. Einstein-Hermitian surfaces and Hermitian Einstein-Weyl structures in dimension 4. Math. Z. 226 (1997), 317-326.
\item[25] P. Gauduchon, A. Moroianu and L. Ornea. Compact homogeneous lcK manifolds are Vaisman. Math. Ann. 361 (2015), 1043-1048.
\item[26] A. Gray. Curvature identities for Hermitian and almost Hermitian manifolds. Tohoku Math. J. (2) 28 (1976), 601-612.
\item[27] K. Grove and W. Ziller. Cohomogeneity one manifolds with positive Ricci curvature. Invent. Math. 149 (2002), 619-646.
\item[28] D. Guan and X.x. Chen. Existence of extremal metrics on almost homogeneous manifolds of cohomogeneity one, Loo-Keng Hua: a great mathematician of the twentieth century. Asian J. Math. 4 (2000), 817-829.
\item[29] K. Hasegawa and Y. Kamishima. Compact homogeneous locally conformally Kähler manifolds. Osaka J. Math. 53 (2016), 683-703.
\item[30] S. Helgason, Differential geometry, Lie groups, and symmetric spaces, Corrected reprint of the 1978 original. Graduate Studies in Mathematics, Vol. 34 (American Mathematical Society, Providence, RI, 2001).
\item[31] A. Huckleberry and D. Snow. Almost-homogeneous Kahler manifolds with hypersurface orbits. Osaka J. Math. 19 (1982), 763-786.
\item[32] S. Kobayashi and K. Nomizu, Foundations of differential geometry. Vol. II, Reprint of the 1969 original, Wiley Classics Library, A Wiley-Interscience Publication (John Wiley \& Sons, Inc., New York, 1996).
\item[33] C. Koca and M. Lejmi. Hermitian metrics of constant Chern scalar curvature on ruled surfaces. Kodai Math. J. 43 (2020), 409-430.
\item[34] N. Koiso and Y. Sakane, Nonhomogeneous Kähler-Einstein metrics on compact complex manifolds, Curvature and topology of Riemannian manifolds (Katata, 1985), 165-179, Lecture Notes in Math., Vol. 1201 (Springer, Berlin, 1986).
\item[35] N. Koiso and Y. Sakane. Nonhomogeneous Kähler-Einstein metrics on compact complex manifolds. II. Osaka J. Math. 25 (1988), 933-959.
\item[36] C. LeBrun, Einstein metrics on complex surfaces, Geometry and physics (Aarhus, 1995), Lecture Notes in Pure and Appl. Math., Vol. 184 (Dekker, New York, 1997), 167-176.
\item[37] K.-F. Liu and X.-k. Yang. Geometry of Hermitian manifolds. Int. J. Math. 23 (2012), 1250055.
\item[38] F. Madani, A. Moroianu and M. Pilca. Conformally related Kähler metrics and the holonomy of lcK manifolds. J. Eur. Math. Soc. (JEMS) 22 (2020), 119-149.
\item[39] B. Malgrange. Sur les points singuliers des équations différentielles. Enseign. Math. (2) 20 (1974), 147-176.
\item[40] M. L. Michelsohn. On the existence of special metrics in complex geometry. Acta Math. 149 (1982), 261-295.
\item[41] P. S. Mostert. On a compact Lie group acting on a manifold. Ann. Math. (2) 65 (1957), 447-455. Errata, 'On a compact Lie group acting on a manifold', Ann. Math. 66 (1957), 589.
\item[42] M. Nishiyama. Classification of invariant complex structures on irreducible compact simply connected coset spaces. Osaka J. Math. 21 (1984), 39-58.
\item[43] B. O'Neill. The fundamental equations of a submersion. Michigan Math. J. 13 (1966), 459-469.
\item[44] L. Ornea and M. Verbitsky. An immersion theorem for Vaisman manifolds. Math. Ann. 332 (2005), 121-143.
\item[45] D. N. Page. A compact rotating gravitational instanton. Phys. Lett. B 79 (1978), 235-238.
\item[46] D. N. Page and C. N. Pope. Inhomogeneous Einstein metrics on complex line bundles. Classical Q. Gravity 4 (1987), 213-225.
\end{itemize}
\begin{itemize}
\item[47] F. Podestá. Homogeneous Hermitian manifolds and special metrics. Transform. Groups 23 (2018), 1129-1147.
\item[48] F. Podestà and A. Spiro. Kähler manifolds with large isometry group. Osaka J. Math. 36 (1999), 805-833.
\item[49] F. Podestà and A. Spiro. New examples of almost homogeneous Kähler-Einstein manifolds. Indiana Univ. Math. J. 52 (2003), 1027-1074.
\item[50] Y. Sakane. Examples of compact Kähler-Einstein manifolds with positive Ricci curvature. Osaka Math. J. 23 (1986), 585-616.
\item[51] J. Streets and G. Tian. Hermitian curvature flow. J. Eur. Math. Soc. (JEMS) 13 (2011), 601-634.
\item[52] V. Tosatti, Non-Kähler Calabi-Yau manifolds, Analysis, complex geometry, and mathematical physics: in honor of Duong H. Phong, 261-277, Contemp. Math., Vol. 644 (Am. Math. Soc., Providence, RI, 2015).
\item[53] V. Tosatti and B. Weinkove. The complex Monge-Ampère equation on compact Hermitian manifolds. J. Am. Math. Soc. 23 (2010), 1187-1195.
\item[54] L. Verdiani and W. Ziller, Smoothness Conditions in Cohomogeneity manifolds, arXiv:1804.04680, to appear in Transf. Groups.
\item[55] H. C. Wang. Closed manifolds with homogeneous complex structures. Am. J. Math. 76 (1954), 1-32.
\item[56] McK. Y.-K. Wang, Einstein metrics from symmetry and bundle constructions, Surveys in differential geometry: essays on Einstein manifolds, 287-325, Surv. Differ. Geom., Vol. 6 (Int. Press, Boston, MA, 1999).
\item[57] McK. Y.-K. Wang, Einstein metrics from symmetry and bundle constructions: a sequel, Differential geometry, 253-309, Adv. Lect. Math. (ALM), Vol. 22 (Int. Press, Somerville, MA, 2012).
\item[58] B. Yang and F. Zheng. On curvature tensors of Hermitian manifolds. Comm. Anal. Geom. 26 (2018), 1195-1222.
\item[59] S.-T. Yau. On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I. Comm. Pure Appl. Math. 31 (1978), 339-411.
\end{itemize}
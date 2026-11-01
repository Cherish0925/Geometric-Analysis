---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: hep-th_9612055.pdf
converter: mathpix
format: mmd
---

\title{
Einstein -Weyl structures corresponding to diagonal Kähler Bianchi IX metrics
}

\author{
Guy Bonneau*
}

December 23, 2017

\begin{abstract}
We analyse in a systematic way the four dimensionnal Einstein-Weyl spaces equipped with a diagonal Kähler Bianchi IX metric. In particular, we show that the subclass of Einstein-Weyl structures with a constant conformal scalar curvature is the one with a conformally scalar flat - but not necessarily scalar flat - metric ; we exhibit its 3-parameter distance and Weyl one-form. This extends previous analysis of Pedersen, Swann and Madsen , limited to the scalar flat, antiself-dual case. We also check that, in agreement with a theorem of Derdzinski, the most general conformally Einstein metric in the family of biaxial Kähler Bianchi IX metrics is an extremal metric of Calabi, conformal to Carter's metric, thanks to Chave and Valent's results.
\end{abstract}

\footnotetext{
*Laboratoire de Physique Théorique et des Hautes Energies, Unité associée au CNRS URA 280, Université Paris 7, 2 Place Jussieu, 75251 Paris Cedex 05. bonneau@lpthe.jussieu.fr
}

\section*{1 Introduction}

In a recent paper, Tod [1] exhibits the relationship between some Einstein-Weyl geometry without torsion (the four-dimensional self-dual Einstein-Weyl geometry studied by Pedersen and Swann [2]) and some local heterotic geometry (i.e. the Riemannian geometry with torsion and three complex structures, associated with $(4,0)$ supersymmetric non-linear $\sigma$ models [3, 4, 5]).

To extend these ideas to other situations, as a first step, we analyse in this work in a systematic way a larger class of Einstein-Weyl geometries : the ones, recently considered by Madsen [8, 9] where the metric lies in the diagonal Kähler Bianchi IX family. We think that this will help in finding new bridges with a larger class of heterotic geometries.

The paper is organised as follows : in Section 2, we describe Bianchi IX metrics and recall the definition of Einstein-Weyl structures and the constraints that result for the metric and the Weyl connection (for recent reviews see refs. [2, 6, 7, 8]).

The Section 3 contains the complete solution of the aforementioned constraints and discusses some special cases previously known. We first obtain a four-parameter Einstein-Weyl structure, not conformally equivalent to Einstein metrics (Subsection 3.1). A particularly interesting subclass is the one with a constant conformal scalar curvature : the constant has to be zero but the scalar curvature is not constant. Some details on these (non-compact) metrics are given in Subsection 4.1. Another subclass is the one with a constant scalar curvature first analysed by Madsen [8] : we prove that the constant has to be zero, leading to the Einstein-Weyl structure given in ref. [8].
Second, in Subsection 3.2 we exhibit the most general conformally Einstein metric in the family of biaxial Kähler Bianchi IX metrics : the distance is a three-parameter dependent one. As explained in Subsection 4.2, due to their U(2) isometries, they fall into the class proposed by Carter [10] and are related to extremal Calabi metrics [11] by the explicit change of coordinates given by Chave and Valent [12].

\section*{2 Bianchi IX metrics and Einstein-Weyl structures}

Bianchi metrics [6, 7] are real four dimensional metrics with a 3-dimensional isometry group, transitive on 3-surfaces. A complete classification has been given in 1897 by Bianchi and their expression is usually written as :
$$\begin{aligned}
g & =(a b c)^{2} d t^{2}+a^{2} \sigma_{1}^{2}+b^{2} \sigma_{2}^{2}+c^{2} \sigma_{3}^{2} \\
& =\omega_{1} \omega_{2} \omega_{3} d t^{2}+\frac{\omega_{2} \omega_{3}}{\omega_{1}} \sigma_{1}^{2}+\frac{\omega_{1} \omega_{3}}{\omega_{2}} \sigma_{2}^{2}+\frac{\omega_{1} \omega_{2}}{\omega_{3}} \sigma_{3}^{2}
\end{aligned}$$
where a, b, c ( or $\omega_{1}, \omega_{2}, \omega_{3}$ ) are functions of t, and the $\sigma_{i}$ are invariant one-forms satisfying :
$$\begin{aligned}
d \sigma_{1} & =n_{1} \sigma_{2} \wedge \sigma_{3} \\
d \sigma_{2} & =n_{2} \sigma_{3} \wedge \sigma_{1}-\tilde{a} \sigma_{1} \wedge \sigma_{2} \\
d \sigma_{3} & =n_{3} \sigma_{1} \wedge \sigma_{2}-\tilde{a} \sigma_{1} \wedge \sigma_{3} .
\end{aligned}$$
The $n_{a}$ 's and $\tilde{a}$ are constant parameters the possible values of which may be found for example in refs. [6, 7]). We shall restrict our analysis to the so-called diagonal Bianchi IX family ${ }^{1}$,

\footnotetext{
${ }^{1}$ One may always diagonalise the metric at a particular $t_{0}$; then we have to assume that the evolution equations are such that the non-diagonal components remain zero.
}
characterised by
$$n_{a}=1, \quad a=1,2,3 \quad ; \quad \tilde{a}=0 .$$
Due to its SU(2) isometry group, it has been frequently considered.
A Weyl space [2] is a conformal manifold with a torsion-free connection D and a one-form $\gamma$ such that for each representative metric g in a conformal class [g],
$$D_{i} g_{j k}=\gamma_{i} g_{j k}$$
A different choice of representative metric : $g \longrightarrow \tilde{g}=e^{f} g$ is accompanied by a change in $\gamma: \gamma \longrightarrow \tilde{\gamma}=\gamma+d f$. Conversely, if the one-form $\gamma$ is exact, the metric g is conformally equivalent to a Riemannian metric $\tilde{g}: D_{i} \tilde{g}_{j k}=0$.
The Ricci tensor associated to the Weyl connection D is defined by :
$$\left[D_{i}, D_{j}\right] v^{k}=\mathcal{R}^{(D) k}{ }_{l, i j} v^{l} \quad, \quad \mathcal{R}_{i j}^{(D)}=\mathcal{R}^{(D) k}{ }_{i, k j} .$$
$\mathcal{R}_{i j}^{(D)}$ is related to $R_{i j}^{(\nabla)}$, the Ricci tensor associated to the Levi-Civita connection [2]:
$$\mathcal{R}_{i j}^{(D)}=R_{i j}^{(\nabla)}+\frac{3}{2} \nabla_{j} \gamma_{i}-\frac{1}{2} \nabla_{i} \gamma_{j}+\frac{1}{2} \gamma_{i} \gamma_{j}+\frac{1}{2} g_{i j}\left[\nabla_{k} \gamma^{k}-\gamma_{k} \gamma^{k}\right] .$$
As a consequence, the Ricci tensor is no longer symmetric as :
$$\mathcal{R}_{[i j]}^{(D)}=-2 \nabla_{[i} \gamma_{j]} .$$
In this work, we shall be interested in Einstein-Weyl spaces defined by :
$$\begin{aligned}
\mathcal{R}_{(i j)}^{(D)} & =\Lambda^{\prime} g_{i j} \Leftrightarrow \\
R_{i j}^{(\nabla)}+\nabla_{(i} \gamma_{j)}+\frac{1}{2} \gamma_{i} \gamma_{j} & =\Lambda g_{i j}, \quad \Lambda=\Lambda^{\prime}-\frac{1}{2}\left[\nabla_{k} \gamma^{k}-\gamma_{k} \gamma^{k}\right] .
\end{aligned}$$
Notice that for an exact Einstein-Weyl structure, the representative metric is conformally Einstein. Notice also that the conformal scalar curvature is related to the scalar curvature through:
$$S^{(D)}=g^{i j} \mathcal{R}_{i j}^{(D)}=4 \Lambda^{\prime}=S^{(\nabla)}+3\left[\nabla_{i} \gamma^{i}-\frac{1}{2} \gamma_{i} \gamma^{i}\right] .$$
Diagonal Bianchi IX metrics being invariant under SU(2), it is natural to look for one-forms $\gamma$ covariant under SU(2) :
$$\gamma=P(t) d t+A_{1}(t) \sigma_{1}+A_{2}(t) \sigma_{2}+A_{3}(t) \sigma_{3} .$$
It is then proven in [8, 9] that the metric is either conformally Einstein :
$$A_{a}(t)=0, \quad a=1,2,3, \quad \gamma=P(t) d t .$$
or biaxial if at least one of the $A_{a}(t)$ does not vanish, say $A_{3}$ :
$$\omega_{1}=\omega_{2}, \quad A_{1}=A_{2}=0 .$$
In the following, when the three $A_{a}$ 's vanish, we shall also restrict ourselves to this hypothesis of U(2) isometry.

It is convenient to introduce the auxiliary functions $\alpha_{a}$ through
$$\omega_{a}^{\prime}=\omega_{b} \omega_{c}+\alpha_{a} \omega_{a}, \quad(a, b, c)=\text { cir. perm. }(1,2,3)$$
where a prime means derivation with respect to t. Equation (11) implies
$$\alpha_{1}=\alpha_{2} .$$
Moreover, as we shall be interested only in Kähler metrics, we may use a theorem of Dancer and Strachan [13] to obtain
$$\alpha_{3}=0 .$$

To sum up, when we look for an Einstein-Weyl structure with a Kähler diagonal Bianchi IX metric, we have 5 unknown functions $\omega_{1}(t)=\omega_{2}(t), \omega_{3}(t), P(t), A_{3}(t)$ and $\alpha_{1}(t)=\alpha_{2}(t):=\alpha(t)$ that define the metric, the Weyl one-form $\gamma$, the Kähler form $\Omega$, the scalar curvatures and the Einstein function (cosmological term) $\Lambda$ :
$$\begin{aligned}
g & =\omega_{1} \omega_{2} \omega_{3} d t^{2}+\frac{\omega_{2} \omega_{3}}{\omega_{1}} \sigma_{1}^{2}+\frac{\omega_{1} \omega_{3}}{\omega_{2}} \sigma_{2}^{2}+\frac{\omega_{1} \omega_{2}}{\omega_{3}} \sigma_{3}^{2} \\
\gamma & =P d t+A_{3} \sigma_{3} \\
\Omega & =d \omega_{3} \wedge \sigma_{3}+\omega_{3} \sigma_{1} \wedge \sigma_{2}, d \Omega=0 \\
S^{(D)} & =4 \Lambda+\frac{2}{\omega_{1} \omega_{2} \omega_{3}}\left[P^{\prime}-P^{2}-\omega_{3}^{2}\left(A_{3}\right)^{2}\right] \\
S^{(\nabla)} & =\frac{-2 \alpha^{\prime}}{\omega_{1} \omega_{2} \omega_{3}} \\
\Lambda & =\frac{1}{2 \omega_{3}^{2}}(P-2 \alpha)
\end{aligned}$$
with 5 constraints through first order differential equations first obtained by Madsen [8, 9] (the last three come from the diagonal matrix elements of equation (7) [8]:
$$\begin{aligned}
\alpha & =\frac{\omega_{1}^{\prime}}{\omega_{1}}-\omega_{3}, \quad \omega_{3}^{\prime}=\left(\omega_{1}\right)^{2}, \\
\alpha^{\prime} & =2 \frac{\left(\omega_{1}\right)^{2}}{\omega_{3}} \alpha+P\left(\alpha+\omega_{3}-\frac{\left(\omega_{1}\right)^{2}}{\omega_{3}}\right)+\frac{1}{2}\left(\omega_{3}\right)^{2}\left(A_{3}\right)^{2}, \\
P^{\prime} & =-\frac{1}{2} P^{2}+2 P\left(\alpha+\omega_{3}\right)+\frac{1}{2}\left(\omega_{3}\right)^{2}\left(A_{3}\right)^{2}, \\
A_{3}^{\prime} & =A_{3}\left[2\left(\alpha+\omega_{3}\right)-\frac{\left(\omega_{1}\right)^{2}}{\omega_{3}}-P\right] .
\end{aligned}$$
As a consequence, it is expected that everything should be fixed, up to some integration constants.

For further use, the special cases of a (anti)self-dual Weyl connection will be interesting. As :
$$d \gamma=A_{3}^{\prime} d t \wedge \sigma_{3}+A_{3} \sigma_{1} \wedge \sigma_{2}=\frac{1}{a b c}\left[\frac{A_{3}^{\prime}}{c} e^{0} \wedge e^{3}+c A_{3} e^{1} \wedge e^{2}\right],$$
where $e^{i}, i=0,1,2,3$ are the vierbeins corresponding to the metric (1), these connections are defined by :
$$A_{3}^{\prime}= \pm \frac{\omega_{1} \omega_{2}}{\omega_{3}} A_{3} .$$

\section*{3 Solution of the constraints.}

As proposed by Pedersen and Poon [14], due to the positivity of $\omega_{3}^{\prime}$, one may change the variable t to r : $\omega_{3}=r^{2} / 4$. We rewrite the system $(12,13)$ with the new quantities :
$$\omega_{3}=r^{2} / 4 \quad, \quad\left(\frac{\omega_{1}}{\omega_{3}}\right)^{2}=W(r), W>0 .$$
Then (a dot means a differentiation with respect to r) :
$$\begin{aligned}
g & =\frac{1}{W} d r^{2}+\frac{1}{4} r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+W \sigma_{3}^{2}\right), \quad \gamma=\frac{8 P}{r^{3} W} d r+A_{3} \sigma_{3}, \\
\Omega & =\frac{1}{4}\left(d r^{2} \wedge \sigma_{3}+r^{2} \sigma_{1} \wedge \sigma_{2}\right), \quad \alpha=\frac{1}{16} r^{3} \dot{W}-\frac{1}{4} r^{2}(1-W), \\
S^{(D)} & =-\frac{4\left(A_{3}\right)^{2}}{r^{2} W}-\frac{192 P^{2}}{r^{6} W}+\frac{96 P}{r^{4}}+\frac{16 P \dot{W}}{r^{3} W}-\frac{4 \dot{W}}{r}+\frac{16(1-W)}{r^{2}}, \\
S^{(\nabla)} & =-\frac{16 \dot{\alpha}}{r^{3}}, \quad \Lambda=\frac{8}{r^{4}}(P-2 \alpha),
\end{aligned}$$
and the constraints, also given in [8, 9] write :
$$\begin{aligned}
\dot{\alpha} & =\frac{r\left(A_{3}\right)^{2}}{4 W}+\frac{\dot{W} P}{2 W}+r\left(\frac{r \dot{W}}{4}+W-1\right), \\
\dot{P} & =-\frac{4 P^{2}}{r^{3} W}+P\left(\frac{\dot{W}}{W}+\frac{4}{r}\right)+\frac{r\left(A_{3}\right)^{2}}{4 W}, \\
\dot{A}_{3} & =A_{3}\left[\frac{\dot{W}}{W}+\frac{2}{r}-\frac{8 P}{r^{3} W}\right] .
\end{aligned}$$
Notice also that with the new variable r, the (anti)self-duality of the Weyl connection (14) writes :
$$\dot{A}_{3}= \pm \frac{2}{r} A_{3} \Leftrightarrow A_{3}=\lambda r^{ \pm 2},$$

Coming now to the system (17), we distinguish 3 cases, corresponding to $A_{3}$ or $P$ being zero or not.

\subsection*{3.1 Non exact Weyl form : $A_{3} \neq 0$.}

Let us define new functions by :
$$R(r)=\frac{W(r)}{A_{3}(r)} \quad, \quad T(r)=\frac{P(r)}{r^{2} A_{3}(r)} .$$
The second and third equations (17) give :
$$\begin{gathered}
T=R / 4+r \dot{R} / 8, \\
2 r^{2} R \ddot{R}-(r \dot{R})^{2}+2 r R \dot{R}-4 R^{2}-4=0,
\end{gathered}$$
Thanks to (19), the Weyl form becomes :
$$\gamma=\frac{8 T}{r R} d r+A_{3} \sigma_{3}=d \log \left|r^{2} R\right|+A_{3} \sigma_{3} .$$

Notice the invariance of the equations in the simultaneous change of R, T and $A_{3}$ in their opposite. The non-linear, but homogeneous, differential equation (20) may be integrated once to give ( $\beta$ being an arbitrary constant)
$$r \dot{R}=2 \epsilon \sqrt{R^{2}+2 \beta R-1} \equiv 2 \epsilon \sqrt{\left(R-a_{1}\right)\left(R+a_{2}\right)}, \epsilon= \pm 1 .$$
A further integration gives ( $d_{\epsilon}$ being other strictly positive arbitrary constants)
$$\log \left(d_{\epsilon} r\right)=\epsilon \log \left[\sqrt{R_{\epsilon}-a_{1}}+\sqrt{R_{\epsilon}+a_{2}}\right] .$$
The function $\mathrm{R}(\mathrm{r})$ is then obtained :
$$R_{\epsilon}(r)=-\beta+\frac{\left(d_{\epsilon} r\right)^{2 \epsilon}}{8}+2 \frac{\left(1+\beta^{2}\right)}{\left(d_{\epsilon} r\right)^{2 \epsilon}},$$
but there is a positivity constraint that writes
$$\left(d_{\epsilon} r\right)^{2 \epsilon} \geq 4 \sqrt{1+\beta^{2}} .$$
So, $R_{+}$is defined for $\left(d_{+} r\right)^{2} \geq 4 \sqrt{1+\beta^{2}}$ and $R_{-}$for $\left(d_{-} r\right)^{2} \leq \frac{1}{4 \sqrt{1+\beta^{2}}}$. A continuous solution of (20) is obtained iff. $d_{-}=\frac{d_{+}}{4 \sqrt{1+\beta^{2}}}$, and writes, using the variable $\tau=d^{2} r^{2} / 4$ :
$$R(r)=-\beta+\frac{\tau}{2}+\frac{\left(1+\beta^{2}\right)}{2 \tau}=\frac{1}{2 \tau}\left[(\tau-\beta)^{2}+1\right] .$$
Equation (19) then gives
$$T(r)=\frac{1}{4}[\tau-\beta] .$$
Differentiating $\alpha(r)$ given in equ.(16) with respect to r, when compared to the first equ.(17), gives a second order linear differential equation on $G(\tau) \equiv A_{3}(r)$ :
$$\frac{\tau^{2}}{2} \frac{d^{2} G}{d \tau^{2}}\left[\left(1+\beta^{2}\right)-2 \beta \tau+\tau^{2}\right]+\tau \frac{d G}{d \tau}\left[-\beta \tau+\tau^{2}\right]-G\left[\left(1+\beta^{2}\right)-\beta \tau+\tau^{2}\right]=-2 \tau .$$
Using $G=2 / \tau+\lambda_{1}\left[\tau / 4-\left(1+\beta^{2}\right) /(4 \tau)\right]$ as one parameter family of solutions ( easily found by inspection of the recursion relation associated to a Laurent series expansion of G around 0), one finds the general solution of (25) :
$$G=\frac{2}{\tau}+\frac{\lambda_{1}}{4 \tau}\left[\tau^{2}-\left(1+\beta^{2}\right)\right]+\frac{\lambda_{2}}{8 \tau}\left[\tau+\beta+\left[\tau^{2}-\left(1+\beta^{2}\right)\right] \arctan (\tau-\beta)\right] .$$
Furthermore, thanks to the previous remark, a ±1 factor may be introduced, simultaneously, in R(r), T(r) and $A_{3}(r)$.

As a consequence, we have the following Theorem :
Theorem 1 : Any diagonal Kähler Bianchi IX metric $g$ and non-exact Weyl one-form $\gamma$ such that the structure $(g, \gamma)$ is that of an Einstein-Weyl space, depend on 4 parameters $\left(\lambda_{1}, \lambda_{2}, \beta\right.$
and d) and are given by :
i) the metric $g$
$$\begin{aligned}
g & =\frac{1}{d^{2}}\left[\frac{d \tau^{2}}{\tau V(\tau)}+\frac{\tau}{4}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\frac{1}{4} \tau V(\tau) \sigma_{3}^{2}\right], \quad \tau V(\tau)=\frac{1}{2}\left[1+(\tau-\beta)^{2}\right] G(\tau), \\
\tau V(\tau) & =\left[\tau-2 \beta+\frac{1+\beta^{2}}{\tau}\right]+\frac{\lambda_{1}}{8}\left[\tau^{3}-2 \beta \tau^{2}+2 \beta\left(1+\beta^{2}\right)-\frac{\left(1+\beta^{2}\right)^{2}}{\tau}\right]+ \\
& +\frac{\lambda_{2}}{16}\left[\tau^{2}-\beta \tau+\left(1-\beta^{2}\right)+\frac{\beta\left(1+\beta^{2}\right)}{\tau}+\frac{\left[(\tau-\beta)^{2}+1\right]\left[\tau^{2}-\left(1+\beta^{2}\right)\right]}{\tau} \arctan (\tau-\beta)\right],
\end{aligned}$$
where $\tau=\frac{d^{2} r^{2}}{4}, \quad V(\tau) \equiv W(r)$,
ii) the one-form $\gamma$
$$\begin{aligned}
\gamma & =d \log \left[1+(\tau-\beta)^{2}\right] \pm G(\tau) \sigma_{3}, \\
G(\tau) & =\frac{2}{\tau}+\frac{\lambda_{1}}{4 \tau}\left[\tau^{2}-\left(1+\beta^{2}\right)\right]+\frac{\lambda_{2}}{8 \tau}\left[\tau+\beta+\left[\tau^{2}-\left(1+\beta^{2}\right)\right] \arctan (\tau-\beta)\right] ;
\end{aligned}$$
iii) the geometrical quantities result from equation (16),
$$\begin{aligned}
\frac{1}{d^{2}} S^{(D)} & =-\frac{\lambda_{2}}{2\left[1+(\tau-\beta)^{2}\right]} \\
\frac{1}{d^{2}} S^{(\nabla)} & =-\frac{3 \lambda_{1}}{2}[\tau-\beta]-\frac{3 \lambda_{2}}{4}\left[[\tau-\beta] \arctan (\tau-\beta)+\frac{(\tau-\beta)^{2}+2 / 3}{(\tau-\beta)^{2}+1}\right] \\
d^{2} \alpha & =-\beta+\frac{\lambda_{1}}{8}\left[\beta\left(1+\beta^{2}\right)-3 \beta \tau^{2}+2 \tau^{3}\right]+ \\
& +\frac{\lambda_{2}}{16}\left[(\tau-\beta)(2 \tau+\beta)+\left[\beta\left(1+\beta^{2}\right)-3 \beta \tau^{2}+2 \tau^{3}\right] \arctan (\tau-\beta)\right], \\
\frac{1}{d^{2}} \Lambda & =\frac{1}{\tau}-\frac{\lambda_{1}}{8 \tau}\left[(\tau-\beta)^{2}+1\right]-\frac{\lambda_{2}}{16 \tau}\left[\tau-\beta+\left[1+(\tau-\beta)^{2}\right] \arctan (\tau-\beta)\right] .
\end{aligned}$$

A few comments and corollaries are in order :
\begin{itemize}
\item[-] The expression of the conformal scalar curvature exhibits a well-defined sign, depending only on the parameter $\lambda_{2}$. For 4-dimensional compact Einstein-Weyl spaces, this results from the work of Pedersen and Swann [15]. In particular, for the compact case, if $S^{(D)}$ vanishes, the space is conformally Einstein.
\item[-] In the basis of self-dual two-forms, the self-dual part of the Weyl curvature tensor writes:
$$W^{+}=\frac{S^{(\nabla)}}{12}\left[\begin{array}{ccc}
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & +2
\end{array}\right]$$
\item[-] The condition $S^{(D)}=$ constant implies $S^{(D)}=0$ which is equivalent to $\lambda_{2}=0$. This leads to the following corollary :
\end{itemize}

Proposition 1 : Given a diagonal Kähler Bianchi IX metric $g$ and a Weyl one-form $\gamma$ such that the structure $(g, \gamma)$ is that of an Einstein-Weyl space, the two following conditions are equivalent :
\begin{itemize}
\item[i)] the space has a constant conformal scalar curvature,
\item[ii)] the metric, depending on 3 parameters submitted to some positivity requirements ${ }^{2}$, is
\end{itemize}
$$\begin{aligned}
g & =\frac{1}{W} d r^{2}+\frac{1}{4} r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+W \sigma_{3}^{2}\right) \\
W(r) & =1+\frac{\kappa r^{2}}{6}+\frac{\kappa(3 \lambda-\kappa \mu) r^{4}}{144 \lambda^{2}}+\frac{8 \lambda}{r^{2}}+\frac{16 \mu}{r^{4}}=\left(2 \mu+\lambda r^{2}+\frac{3 \lambda-\kappa \mu}{24 \lambda} r^{4}\right)\left(\frac{8}{r^{4}}+\frac{\kappa}{6 \lambda}\right),
\end{aligned}$$
the conformal scalar curvature vanishes and the one-form and the scalar curvature are respectively :
$$\begin{aligned}
\gamma & =d \log \left[2 \mu+\lambda r^{2}+\frac{3 \lambda-\kappa \mu}{24 \lambda} r^{4}\right] \pm \sigma_{3} \sqrt{\left[\mu-\lambda^{2}-\frac{\kappa \mu^{2}}{3 \lambda}\right]}\left[\frac{8}{r^{2}}+\frac{\kappa r^{2}}{6 \lambda}\right] \\
S^{(\nabla)} & =-4 \kappa\left[1+\frac{3 \lambda-\kappa \mu}{12 \lambda^{2}} r^{2}\right] .
\end{aligned}$$
\begin{itemize}
\item[-] The condition of constant scalar curvature enforces $\lambda_{1}=\lambda_{2}=0$, i.e. $S^{(\nabla)}=0$. This leads to a special case $(\kappa=0)$ of the previous proposition which appears to be the scalar-flat metric of Madsen with an anti-self dual Weyl connection (see equ.(18)) [8, 9]. Then we have the following corollary :
\end{itemize}

Proposition 2 : Given a diagonal Kähler Bianchi IX metric $g$ and a Weyl one-form $\gamma$ such that the structure $(g, \gamma)$ is that of an Einstein-Weyl space, the two following conditions are equivalent :
i) the space has a constant scalar curvature,
ii) the metric, Weyl form and geometric parameters, depending on 2 parameters submitted to $\mu \geq \lambda^{2}$, are :
$$\begin{aligned}
& g=\frac{1}{W} d r^{2}+\frac{1}{4} r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+W \sigma_{3}^{2}\right), \quad W=1+\frac{8 \lambda}{r^{2}}+\frac{16 \mu}{r^{4}}=\left(1+\frac{4 \lambda}{r^{2}}\right)^{2}+\frac{16\left(\mu-\lambda^{2}\right)}{r^{4}}>0, \\
& \gamma=d \log \left[r^{4} W\right] \pm \frac{8 \sqrt{\mu-\lambda^{2}}}{r^{2}} \sigma_{3}, \quad W^{+}=S^{(\nabla)}=S^{(D)}=0 .
\end{aligned}$$
This structure has been recently related to Ricci-flat metrics with torsion [1].
\begin{itemize}
\item[-] The special case $\lambda_{2}=0, \lambda_{1}=8 /\left(1+\beta^{2}\right)$ leads to :
\end{itemize}
$$W=1-\frac{\beta d^{2}}{2\left(1+\beta^{2}\right)} r^{2}+\frac{d^{4}}{16\left(1+\beta^{2}\right)} r^{4}, A_{3}= \pm \frac{d^{2}}{2\left(1+\beta^{2}\right)} r^{2},$$

\footnotetext{
${ }^{2}$ To agree with commonly used notations, we make the following changes of parameters :
$$\kappa / 6=-\frac{\lambda_{1} \beta d^{2}}{16}, \quad 8 \lambda=-\frac{\beta}{d^{2}}\left[8-\lambda_{1}\left(1+\beta^{2}\right)\right], \quad 16 \mu=\frac{2\left(1+\beta^{2}\right)}{d^{4}}\left[8-\lambda_{1}\left(1+\beta^{2}\right)\right] .$$
Then the quantity $\left[\mu-\lambda^{2}-\frac{\kappa \mu^{2}}{3 \lambda}\right] / \lambda^{2}$ equals the positive constant $1 / \beta^{2}$; this, as we shall see in Subsect. 4.1 needs $\kappa \lambda<3 / 4$. Moreover, W should be a positive function.
}
\begin{itemize}
\item[] which is an Einstein-Weyl structure with a self-dual Weyl connection (see equ.(18)) :
$$\begin{aligned}
W & =1+\frac{\kappa}{6} r^{2}+\frac{\nu}{48} r^{4}=\left(1+\frac{\kappa r^{2}}{12}\right)^{2}+\frac{\left(3 \nu-\kappa^{2}\right) r^{4}}{144}>0, \quad \nu>\kappa^{2} / 3, \\
\gamma & =d \log [W] \pm \sqrt{3 \nu-\kappa^{2}}\left(\frac{r^{2}}{6}\right) \sigma_{3}, \quad S^{(D)}=0, \quad S^{(\nabla)}=-\left(4 \kappa+\nu r^{2}\right) .
\end{aligned}$$
\item[-] By inspection of expression (28) and use of equation (18), we have the following corollary:
\end{itemize}

Proposition 3 : Given a diagonal Kähler Bianchi IX metric $g$ and a non exact Weyl one-form $\gamma$ such that the structure $(g, \gamma)$ is that of an Einstein-Weyl space, the only (anti)self dual Weyl connections are those of equations (32) and (33).

Some properties of the conformally scalar flat metric (30) will be offered in Subsection 4.1.

\subsection*{3.2 Conformally Einstein metrics : $A_{3}=0, P \neq 0$.}

As said before, we consider this case as a limit of the general class, and we still ask $\omega_{1}=\omega_{2}$ (biaxial or U(2) metrics), which is definitely a restriction (see for example see some attempts in [14]).
We add to the Einstein-Weyl conditions (16,17), the exactedness of the Weyl one-form $\gamma$,
$$\gamma=d \tilde{\gamma} \Leftrightarrow A_{3}(r)=0 .$$
A first constraint writes :
$$\frac{\dot{P}}{P}=\frac{\dot{W}}{W}+\frac{4}{r}-\frac{4 P}{r^{3} W} .$$
The function $P(r)$ being different from zero (to have a non vanishing Weyl form), we define an auxiliary function
$$R(r)=\frac{r^{4} W(r)}{P(r)} ;$$
it satisfies :
$$\dot{R}=4 r$$
which gives ( $\delta$ being an arbitrary constant) :
$$P(r)=W(r) \frac{r^{4}}{2\left(r^{2}+4 \delta\right)} .$$
Notice that, thanks to (35), the Weyl form writes :
$$\gamma=\frac{8 r}{R}=2 d \log R$$
The constraint (17) on the function $\alpha(r)$ of (16) then gives
$$\ddot{W} \frac{r^{2}}{16}-\dot{W}\left[\frac{r^{3}}{4\left(r^{2}+4 \delta\right)}-\frac{3 r}{16}\right]-\frac{1}{2}(W-1)=0,$$
which writes, using the variable $\tau=r^{2}$ and the function $V(\tau)=W(r)-1$
$$\tau^{2}(\tau+4 \delta) \ddot{V}+8 \delta \tau \dot{V}-2(\tau+4 \delta) V=0 .$$
This linear equation integrates to
$$V=a_{1} \tau\left(1+\frac{\tau}{8 \delta}\right)+b_{1} \frac{(\tau+2 \delta)}{\tau^{2}},$$
and this gives
$$W(r)=1+a_{1} r^{2}+\frac{a_{1}}{8 \delta} r^{4}+\frac{b_{1}}{r^{2}}+\frac{2 \delta b_{1}}{r^{4}} .$$
With the following change of parameters : $a_{1}=\kappa / 6, b_{1}=8 \lambda$ and $\delta=\mu / \lambda$, we have the following theorem :

Theorem 2 : Given a diagonal Kähler Bianchi IX metric $g$ and a Weyl one-form $\gamma$ such that the structure $(g, \gamma)$ is that of an Einstein-Weyl space, the two following conditions are equivalent :
i) The space is conformally equivalent to an Einstein space, and the metric is biaxial,
ii) The metric depends on 3 arbitrary parameters :
$$g=\frac{1}{W} d r^{2}+\frac{1}{4} r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+W \sigma_{3}^{2}\right) \quad, \quad W(r)=1+\frac{\kappa r^{2}}{6}+\frac{\kappa \lambda r^{4}}{48 \mu}+\frac{8 \lambda}{r^{2}}+\frac{16 \mu}{r^{4}}$$
and the one-form is
$$\gamma=d \log \left[4 \mu+\lambda r^{2}\right]^{2} .$$
Moreover, with (16),
$$\begin{aligned}
S^{(D)}=\frac{192\left[\lambda \mu-\lambda^{3}-\frac{\kappa \mu^{2}}{3}\right]}{\left[4 \mu+\lambda r^{2}\right]^{2}} \quad, \quad S^{(\nabla)}=-4 \kappa\left[1+\frac{\lambda r^{2}}{4 \mu}\right], \\
\alpha=\lambda+\frac{\kappa r^{4}}{16}+\frac{\lambda \kappa r^{6}}{96 \mu} \quad, \quad r^{2} \Lambda=\frac{16}{4 \mu+\lambda r^{2}}\left[\lambda^{2}+\frac{\lambda-\kappa \mu}{4} r^{2}-\frac{\kappa \lambda}{16} r^{4}-\frac{\kappa \lambda^{2}}{192 \mu} r^{6}\right] .
\end{aligned}$$
A few comments are in order :
\begin{itemize}
\item[-] The request of a constant scalar curvature leads either to $\lambda=0$, which is an Einstein metric and will be discussed in the next subsection, or $\kappa=0$ which is scalar flat (see the next item).
\item[-] The special case $a_{1}=0 \Rightarrow \kappa=0$, where the scalar curvature vanishes, gives a metric conformally equivalent to the Lebrun metric [16] which generalises Eguchi-Hanson $(\kappa=$ $\lambda=0$ ).
\item[-] The special case $b_{1}=0 \Rightarrow \lambda=\mu=0$ with a fixed ratio $\delta$ leads to :
$$\begin{aligned}
& W(r)=1+(\kappa / 6) r^{2}+(\kappa / 48 \delta) r^{4} \quad, \quad \gamma=d \log \left[4 \delta+r^{2}\right]^{2}, \\
& S^{(D)}=\frac{-64 \delta(\delta \kappa-3)}{\left[4 \delta+r^{2}\right]^{2}} \quad, \quad S^{(\nabla)}=-4 \kappa\left[1+\frac{r^{2}}{4 \delta}\right] .
\end{aligned}$$
With $\nu=\frac{\kappa}{\delta}$, we recover the metric (33), but the Weyl one-form and the conformal scalar curvature are different.
\end{itemize}
\begin{itemize}
\item[-] The special case $b_{1}=0, \delta \infty$ such that $b_{1} \delta=\mu \Rightarrow \lambda=0$, is the aforementioned Einstein metric.
\item[-] The special case $a_{1}=\delta=0$ with a fixed ratio $a_{1} / \delta=\nu / 6 \Rightarrow \kappa=\mu=0$ with a fixed ratio $\kappa / \mu=\nu / \lambda$ leads to :
$$\begin{aligned}
W(r)=1+(8 \lambda) / r^{2}+(\nu / 48) r^{4} & , \gamma=d \log \left[r^{2}\right]^{2}, \\
S^{(D)}=\frac{-192 \lambda}{r^{4}} \quad, & S^{(\nabla)}=-\nu r^{2} .
\end{aligned}$$
\item[-] The special case
$$b_{1}=8 \delta\left[1-2 a_{1} \delta\right] \Rightarrow\left[\mu / \lambda-\lambda-\frac{\kappa \mu^{2}}{3 \lambda^{2}}\right]=0 \Rightarrow S^{(D)}=0,$$
is common to this subsection and the previous one : under this hypothesis, the two quantities $\frac{\kappa(3 \lambda-\kappa \mu)}{144 \lambda^{2}}$ in equ.(30)(Proposition 1) and $\frac{\kappa \lambda}{48 \mu}$ in equ.(40)(Theorem 2) are indeed the same.
\end{itemize}

In Subsection 4.2, we shall analyse the Einstein metrics conformally equivalent to (40) and recognise previously known ones.

\subsection*{3.3 Einstein metrics : $A_{3}=P=0$.}

The constraint (17) on the function $\alpha(r)$ of (16) gives the homogeneous equation
$$r^{2} \ddot{W}+3 r \dot{W}-8(W-1)=0,$$
which integrates to
$$W=1+a_{2} r^{2}+b_{2} / r^{4},$$
that was obtained by Gibbons and Pope [17] and Pedersen [18] (It interpolates between Eguchi-Hanson $\left(a_{2}=0\right)$ and the pseudo Fubini-Study metric $\left(b_{2}=0\right)$.) It is the only Kähler Einstein biaxial Bianchi IX metric [13]. The scalar curvatures $S^{(D)}$ and $S^{(\nabla)}$ - as well as the cosmological term $\Lambda$ - are both equal to the constant $-6 a_{2}$.

\section*{4 More on our Einstein-Weyl metrics}

\subsection*{4.1 Conformally scalar flat metrics}

In the present work, we comment only the conformally scalar flat special case ( $\lambda_{2}=0$ in equation (27), i.e. the result of Proposition 1). A first remark is that such spaces cannot be compact, because according to a result of Pedersen and Swann [15], they should then be conformally Einstein.
When rewritten as a function of $\tau=r^{2}$, the distance ${ }^{3}$ and Weyl form are :
$$g=\frac{1}{4}\left[\frac{1}{\rho(\tau)} d \tau^{2}+\tau\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\rho(\tau) \sigma_{3}^{2}\right], \text { with } \rho(\tau) \equiv \tau W(r)$$

\footnotetext{
${ }^{3}$ The expression (47) of the distance appears to be the same as the one obtained in [12] for the extremal metrics of Calabi [11], and compared to equation 8 of [12], satisfies the relation
$$c_{1} c_{3}^{2}+c_{2} c_{3}+c_{2}^{2} c_{4}=0$$
}
$$\begin{aligned}
\rho(\tau) & =\frac{16 \mu}{\tau}+8 \lambda+\tau+\frac{\kappa}{6} \tau^{2}+\frac{\kappa(3 \lambda-\kappa \mu)}{144 \lambda^{2}} \tau^{3}=\left(2 \mu+\lambda \tau+\frac{3 \lambda-\kappa \mu}{24 \lambda} \tau^{2}\right)\left(\frac{8}{\tau}+\frac{\kappa}{6 \lambda} \tau\right) \\
\gamma & =d \log \left[2 \mu+\lambda \tau+\frac{3 \lambda-\kappa \mu}{24 \lambda} \tau^{2}\right] \pm \sigma_{3} \sqrt{\left[\mu-\lambda^{2}-\frac{\kappa \mu^{2}}{3 \lambda}\right]}\left[\frac{8}{\tau}+\frac{\kappa}{6 \lambda} \tau\right] .
\end{aligned}$$
Remember that the quantity $\mu-\lambda^{2}-\frac{\kappa \mu^{2}}{3 \lambda}$ has to be positive. One easily finds that this requires
$$\kappa \lambda \leq 3 / 4 .$$
One gets :
$$\mu \leq \frac{3 \lambda}{2 \kappa}\left[\sqrt{1-\frac{4 \kappa \lambda}{3}}+1\right] \leq 0 \quad \text { or } \quad \mu \geq-\frac{3 \lambda}{2 \kappa}\left[\sqrt{1-\frac{4 \kappa \lambda}{3}}-1\right] \geq 0,$$
if $\kappa \lambda \leq 0$, and, if $0 \leq \kappa \lambda \leq 3 / 4$ :
$$0 \leq \frac{3 \lambda}{2 \kappa}\left[1-\sqrt{1-\frac{4 \kappa \lambda}{3}}\right] \leq \mu \leq \frac{3 \lambda}{2 \kappa}\left[1+\sqrt{1-\frac{4 \kappa \lambda}{3}}\right] .$$
Moreover, the first parenthesis of $\rho(\tau)$ given in equ.(47) cannot vanish and has the same sign as $\mu$. Let us now discuss the positivity of the metric. The second parenthesis in $\rho$ may vanish, for $\tau=\tau_{0}=4 \sqrt{\frac{-3 \lambda}{\kappa}}$, iff. $\kappa \lambda \leq 0$. Finally, three situations arise :
\begin{itemize}
\item[-] a) $0 \leq \kappa \lambda \leq 3 / 4$ : the parameter $\mu$ is positive (restricted as mentioned above) and the function $\rho(\tau)$ too. The variable $\tau$ belongs to the interval $] 0, \infty[$;
\item[-] b) $\kappa \lambda \leq 0$ and $\mu \geq \frac{-3 \lambda}{2 \kappa}\left[\sqrt{1-\frac{4 \kappa \lambda}{3}}-1\right] \geq 0$ : the function $\rho(\tau)$ - and the metric - is positive in the interval $] 0, \tau_{0}[$;
\item[-] c) $\kappa \lambda \leq 0$ and $\mu \leq \frac{3 \lambda}{2 \kappa}\left[\sqrt{1-\frac{4 \kappa \lambda}{3}}+1\right] \leq 0$ : the function $\rho(\tau)$ - and the metric - is positive in the interval $] \tau_{0}, \infty[$.
\end{itemize}

Let us now discuss the kind of singularities of the metric with respect to the terminology of Gibbons and Hawking [19]. The value $\tau=0$ is an incurable singularity except when $\mu=0$ (then $\lambda$ has to vanish and one is led to the particular self-dual case (33) where, the function $W$ being positive definite, $\tau$ belongs to $] 0, \infty[$ and the other end, $+\infty$, is singular). The value $\tau=+\infty$ is an incurable singularity except when $\lambda=\kappa \mu / 3$ (then $\kappa$ has to vanish and one is led to the particular antiself-dual case (32) where, the function $W$ being positive definite, $\tau$ belongs to $] 0, \infty[$ and the other end, 0 , is singular).
With respect to the singularity at $\tau_{0}$, we now prove that, only in subcase c), it may be an apparent bolt-like singularity . $\rho(\tau)$ being positive, the expansion
$$\rho(\tau)=\left(\tau-\tau_{0}\right) \rho^{\prime}\left(\tau_{0}\right)+\ldots$$
allows the change of variable :
$$\tau-\tau_{0}=x^{2} \rho^{\prime}\left(\tau_{0}\right),$$
and the metric behaves like
$$(d x)^{2}+x^{2}\left[\frac{\rho^{\prime}\left(\tau_{0}\right)}{2}\right]^{2} \sigma_{3}^{2}+\frac{1}{4}\left[\tau_{0}+x^{2} \rho^{\prime}\left(\tau_{0}\right)\right]\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+. .$$
exhibiting a bolt [19] of order k iff. :
$$\frac{\rho^{\prime}\left(\tau_{0}\right)}{2}=k \quad, \quad k=1,2, \ldots ;$$
indeed, in such a case, the singularity at $\tau_{0}$ is an apparent polar-coordinate like singularity, which disappears when the range in the angle $\psi\left(\sigma_{3}=d \psi+\cos \theta d \phi, ..\right)$ is limited to $\left[0, \frac{4 \pi}{k}\right]$. This requires :
$$\mu=-\frac{k+1}{32} \tau_{0}^{2}-\frac{\lambda}{4} \tau_{0}, \quad \kappa=-\frac{48 \lambda}{\tau_{0}^{2}},$$
and the positivity of $\mu-\lambda^{2}-\frac{\kappa \mu^{2}}{3 \lambda}$ writes :
$$\lambda \geq-\frac{k^{2}-1}{16 k} \tau_{0} \Rightarrow \mu \leq-\frac{(k+1)^{2}}{64 k} \tau_{0}^{2}<0 .$$
Then, we can summarise the previous discussion according to cases a), b) and c) defined above:
\begin{itemize}
\item[-] a) $\tau \in] 0, \infty[$ : the metric is singular at both ends, except for the (anti)self-dual cases mentioned above ;
\item[-] b) $\tau \in] 0, \tau_{0}[$ : the metric is singular at both ends ;
\item[-] c) $\tau \in\left[\tau_{0}, \infty\left[\right.\right.$ : if the parameters are related as in equ. (48), the singularity at $\tau_{0}$ is bolt-like, and the metric is complete at $\tau_{0}$, but anyway singular at $\infty$.
\end{itemize}
As explained above, they are never ${ }^{4}$ compact [15].

\subsection*{4.2 Conformally Einstein metrics}

The metric g (40), with
$$\gamma=d \log \left[h^{2}\right], \quad h=4 \mu+\lambda r^{2}, \quad S_{g}^{(\nabla)}=-\frac{\kappa}{\mu} h,$$
is conformally equivalent to the metric $\bar{g}=g h^{-2}$ which is Einstein, with a scalar curvature given by :
$$S_{\bar{g}}^{(\nabla)}=h^{2} S_{g}^{(\nabla)}-6\left[h \triangle h+2|d h|^{2}\right]=192\left[\lambda \mu-\lambda^{3}-\frac{\kappa \mu^{2}}{3}\right] .$$
This is in agreement with a theorem of Derdzinski [20] quoted in the book of A. Besse ([21], Theorem 11.81) as the function
$$\left(S_{g}^{(\nabla)}\right)^{3}-6\left[S_{g}^{(\nabla)} \triangle S_{g}^{(\nabla)}+2\left|d S_{g}^{(\nabla)}\right|^{2}\right]=\frac{\kappa^{2}}{\mu^{2}} S_{\bar{g}}^{(\nabla)}$$
is a constant ; moreover, this theorem proves that g is a conformally Einstein extremal metric of Calabi [11]. Then the work of Valent and Chave [12], giving an explicit form for their distance

\footnotetext{
${ }^{4}$ Except when they are in fact conformally Einstein $\left(\mu-\lambda^{2}-\frac{\kappa \mu^{2}}{3 \lambda}=0.\right)$
}
and the change of coordinates ensuring this link, is of great help. Our U(2) symmetric metrics (40), when expressed as a function of $\tau=r^{2}$ :
$$\begin{aligned}
g & \left.=\frac{\tau}{4 \rho(\tau)} d \tau^{2}+\frac{1}{4} \tau\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\frac{1}{4 \tau}(\rho(\tau)) \sigma_{3}^{2}\right), \\
\rho(\tau) & =\tau^{2} W(r)=16 \mu+8 \lambda \tau+\tau^{2}+\frac{\kappa}{6} \tau^{3}+\frac{\kappa \lambda}{48 \mu} \tau^{4},
\end{aligned}$$
and compared to equation 8 of [12], satisfies the relation $4 c_{1} c_{4}=c_{2} c_{3}$ of proposition 7 (equ. 15 of [12]), so ensuring their conformally Einstein character. With respect to $\bar{g}$, the change of coordinate :
$$\rho=\frac{\lambda \tau-4 \mu}{\lambda \tau+4 \mu} \quad, \quad-1<\rho<+1$$
gives a Carter metric [10]
$$\begin{aligned}
\bar{g} & =\frac{1}{64 \mu \lambda}\left\{\frac{1-\rho^{2}}{\Delta(\rho)} d \rho^{2}+\frac{4 \Delta(\rho)}{1-\rho^{2}} \sigma_{3}^{2}+\left(1-\rho^{2}\right)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)\right\} \\
\Delta(\rho) & =\left[1+\frac{\kappa \mu}{\lambda}+\frac{3 \lambda^{2}}{\mu}\right]+\frac{8}{3}\left[\frac{\kappa \mu}{\lambda}-\frac{3 \lambda^{2}}{\mu}\right] \rho+2\left[-1+\frac{\kappa \mu}{\lambda}+\frac{3 \lambda^{2}}{\mu}\right] \rho^{2}-\frac{1}{3}\left[-3+\frac{\kappa \mu}{\lambda}+\frac{3 \lambda^{2}}{\mu}\right] \rho^{4} .
\end{aligned}$$
Finally, if one require compactness and special behavior at end points (bolt-bolt), one gets definite values for our parameters $\lambda, \kappa$ and $\mu$. In particular, $\bar{g}$ is the Page metric [22] iff.
$$\frac{2 \kappa \mu}{3 \lambda}=\frac{2 \lambda^{2}}{\mu}=1-\frac{1+\nu^{2}}{\nu\left(3+\nu^{2}\right)} \simeq-.2443$$
where the Page parameter $\nu \simeq .2817$ is the unique root of the algebraic equation $-\nu^{4}+6 \nu^{2}+3=$ $4 \nu\left(3+\nu^{2}\right)$ in the range $0<\nu<1$.

\section*{5 Concluding remarks}

In this paper, we have presented a complete analysis of the Einstein-Weyl structures $(g, \gamma)$ corresponding to diagonal Kähler Bianchi IX metrics first analysed from this point of view by Madsen. The general solution is a 4-parameter metric (27). In the subclass where the conformal scalar curvature is a constant, our Proposition 1 extends previously known results [8, 9] to non scalar-flat cases. Unfortunately these metrics, known to be non-compact, are always singular. We refer to a further publication for a discussion on the link between our Einstein-Weyl structures and geometries with torsion as initiated by Tod [1].

With respect to conformally Einstein structures, we recover the U(2) symmetric metrics conformally equivalent to the Einstein metrics of Carter [10, 12].

\section*{References}
\begin{itemize}
\item[] [1] K. P. Tod, Class. Quantum Grav. 13 (1996) 2609.
\item[] [2] H. Pedersen and A. Swann, Proc. Lond. Math. Soc. 66 (1993) 381.
\end{itemize}
\begin{itemize}
\item[] [3] C. M. Hull and E. Witten, Phys. Lett. 160B (1985) 398 ; C. M. Hull Nucl. Phys. B267 (1986) 266.
\item[] [4] E. Bergshoef and E. Sezgin, Mod. Phys. Lett. A1 (1986) 191 ;
P. Howe and G. Papadopoulos, Nucl. Phys. B289 (1986) 264 ; Class. Quantum Grav. 4 (1987) 1749 ; Class. Quantum Grav. 5 (1988) 1647 ;
Ph. Spindel, A. Sevrin, W. Troost and A. Van Proyen, Nucl. Phys. B308 (1988) 662 ;
F. Delduc, S. Kalitzin and E. Sokatchev, Class. Quantum Grav. 7 (1990) 1567.
\item[] [5] F. Delduc and G. Valent, Class. Quantum Grav. 10 (1993) 1201.
\item[] [6] A. S. Dancer and Ian A. B. Straham, Cohomogeneity-One Kähler metrics in "Twistor theory", S. Huggett ed., Marcel Dekker Inc., New York, 1995, p.9.
\item[] [7] K. P. Tod, Cohomogeneity-One metrics with Self-Dual Weyl tensor in "Twistor theory", S. Huggett ed., Marcel Dekker Inc., New York, 1995, p.171.
\item[] [8] A. Madsen, Compact Einstein-Weyl manifolds with large symmetry group, PhD. Thesis (especially section 9.2), Odense University, 1995.
\item[] [9] A. Madsen, Einstein-Weyl strutures in the conformal classes of Lebrun metrics, to be published in Class. Quantum Grav.
\item[] [10] B. Carter, Comm. Math. Phys. 10 (1968) 280.
\item[] [11] E. Calabi, Extremal Kähler metrics", Seminars on differential geometry, ed. S. T. Yau, Ann. Math. Stu., Princeton University Press (1982), p. 259.
\item[] [12] T. Chave and G. Valent, Class. Quantum Grav. 13 (1996) 2097.
\item[] [13] A. S. Dancer and Ian A. B. Straham, Proc. Camb. Phil. Soc. 115 (1994) 513.
\item[] [14] H. Pedersen and Y. S. Poon, Class. Quantum Grav. 7 (1990) 1707.
\item[] [15] H. Pedersen and A. Swann, J. reine angew. Math. 441 (1993) 99.
\item[] [16] C. Lebrun, Comm. Math. Phys. 118 (1988) 591.
\item[] [17] G. W. Gibbons and C. N. Pope, Comm. Math. Phys. 66 (1979) 267.
\item[] [18] H. Pedersen, Class. Quantum Grav. 2 (1985) 579.
\item[] [19] G. W. Gibbons and S. W. Hawking, Comm. Math. Phys. 66 (1979) 291.
\item[] [20] A. Derdzinski, Comput. Math. 49 (1983) 405.
\item[] [21] A. L. Besse, "Einstein Manifolds", Ergebnisse der Mathematik und ihrer Grenzgebeite, 3. Folge, Band 10, Springer-Verlag Berlin Heidelberg (1987).
\item[] [22] D. Page, Phys. Lett. 79B (1978) 235.
\end{itemize}
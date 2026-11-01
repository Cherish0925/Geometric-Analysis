---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: Einstein-Weyl_structures_and_Bianchi_metrics_55abf3ae0cc0.pdf
converter: mathpix
format: mmd
---

\title{
Einstein - Weyl structures and Bianchi metrics
}

\author{
Guy Bonneau*
}

July 3, 2021

\begin{abstract}
We analyse in a systematic way the (non-)compact four dimensional Einstein-Weyl spaces equipped with a Bianchi metric. We show that Einstein-Weyl structures with a Class A Bianchi metric have a conformal scalar curvature of constant sign on the manifold. Moreover, we prove that most of them are conformally Einstein or conformally Kähler ; in the non-exact Einstein-Weyl case with a Bianchi metric of the type $V I I_{0}, V I I I$ or $I X$, we show that the distance may be taken in a diagonal form and we obtain its explicit 4-parameters expression. This extends our previous analysis, limited to the diagonal, Kähler Bianchi $I X$ case.
\end{abstract}

\footnotetext{
*Laboratoire de Physique Théorique et des Hautes Energies, Unité associée au CNRS URA 280, Université Paris 7, 2 Place Jussieu, 75251 Paris Cedex 05. bonneau@lpthe.jussieu.fr
}

\section*{1 Introduction}

In the last years, Einstein-Weyl geometry has raised some interest, in particular when in a recent paper, Tod [1] exhibits the relationship between a particular Einstein-Weyl geometry without torsion (the four-dimensional self-dual Einstein-Weyl geometry studied by Pedersen and Swann [2]) and local heterotic geometry (i.e. the Riemannian geometry with torsion and three complex structures, associated with $(4,0)$ supersymmetric non-linear $\sigma$ models [3, 4, 5]).

To extend these ideas to other situations, we analysed in a first step [6](hereafter referred to as [GB]) Einstein-Weyl equations in the subclass of diagonal Kähler Bianchi $I X$ metrics (in the standard classification [7, 8]). In the present work, we study (non-)compact 4-dimensional Einstein-Weyl structures (for recent reviews see refs. [2, 9]) on cohomogenity-one manifolds with a 3 dimensional group of isometries transitive on codimension-one surfaces, i.e., in the general relativity terminology, Bianchi metrics, and neither require a diagonal metric nor the Kähler property ; we however obtain interesting results for any (class A) Bianchi metrics.

Let us recall that, in the compact case, on general grounds, strong results on Einstein-Weyl structures have been known for some time :
\begin{itemize}
\item[-] There exits a unique metric in a given conformal class [g] such that the Weyl form is co-closed [10] ,
$$\nabla_{\mu} \gamma^{\mu}=0$$
\end{itemize}

One then speaks of the "Gauduchon's gauge" and of a "Gauduchon's metric".
\begin{itemize}
\item[-] The analysis of Einstein-Weyl equations in this gauge gives two essential results :
\begin{itemize}
\item[-] The dual of the Weyl form $\gamma$ is a Killing vector [11]:
$$\nabla_{(\mu} \gamma_{\nu)}=0,$$
\item[-] Four dimensional Einstein-Weyl spaces have a constant conformal scalar curvature [12]:
$$\nabla_{\mu} S^{D}=-\frac{n(n-4)}{4} \nabla_{\mu}\left(\gamma_{\nu} \gamma^{\nu}\right) .$$
\end{itemize}
\end{itemize}
The paper is organised as follows : in the next Section, we recall the classification of Bianchi metrics and the expressions of geometrical objects, separating the 4-dimensional metric g into a "time part" and a 3-dimensional homogeneous one. Focussing ourselves on Class A Bianchi metrics, we exhibit a specific Gauduchon's gauge and show how, in the diagonal case the Einstein-Weyl equations simplify and ensure that the dual $\gamma_{\mu}$ of the Weyl one-form $\gamma$ is a Killing vector, as in the compact case, and that the metric is either conformally Einstein or conformally Kähler. In particular, this proves that four-dimensional Einstein-Weyl spaces equipped with a diagonal Bianchi $I X$ metrics are necessarily conformally Kähler, i.e. that our previous solution [GB] is the general one, up to a conformal transformation.
In Section 3, we show that for all class A Bianchi metrics, there exits a simple Gauduchon's gauge such that the conformal scalar curvature is constant on the manifold and the dual $\gamma_{\mu}$ of the Weyl one-form $\gamma$ satisfies $D^{\mu}\left(\nabla_{(\mu} \gamma_{\nu)}\right)=0$, where $D$ denotes the covariant derivative with respect to the Weyl connection $\gamma$. Using these results, we prove that for Bianchi $V I_{0}, V I I_{0}, V I I I$, and $I X$, the most general solution of Einstein-Weyl constraints is the same as the one in the diagonal case, i.e. in the non-conformally Einstein cases, the Kähler one of previous subsection, up to a conformal transformation. Finally, we also prove that the only self-dual Einstein-Weyl structures are the Bianchi $I X$ ones of Madsen [9, 13].

\section*{2 Bianchi metrics and Einstein-Weyl structures.}

\subsection*{2.1 The geometrical setting}
\begin{itemize}
\item[-] A Weyl space [2] is a conformal manifold with a torsion-free connection D and a one-form $\gamma$ such that for each representative metric g in a conformal class [g],
$$D_{\mu} g_{\nu \rho}=\gamma_{\mu} g_{\nu \rho} .$$
A different choice of representative metric : $g \longrightarrow \tilde{g}=e^{f} g$ is accompanied by a change in $\gamma: \gamma \longrightarrow \tilde{\gamma}=\gamma+d f$. Conversely, if the one-form $\gamma$ is exact, the metric g is conformally equivalent to a Riemannian metric $\tilde{g}: D_{\mu} \tilde{g}_{\nu \rho}=0$. In that case, we shall speak of an exact Weyl structure.
\item[-] On the other hand, Bianchi metrics are real four-dimensional metrics with a three-dimensional isometry group, transitive on 3-surfaces. Their classification was done by Bianchi in 1897 according to the Lie algebras of their isometry group, i.e. according to the Lie algebra structure constants $C_{j k}^{i},(i, j, k=1,2,3)$; on general grounds, these ones may be decomposed into two parts [14]:
$$C_{j k}^{i}=n^{i l} \epsilon_{j k l}+a_{l}\left[\delta_{j}^{i} \delta_{k}^{l}-\delta_{k}^{i} \delta_{j}^{l}\right]$$
where the symmetric $3 \times 3$ tensor $n^{i l}$ may be reduced to a diagonal matrix with entries 0,1 or -1 and the vector $a_{l}$ satisfies
$$n^{i l} a_{l}=0 .$$
This splits Bianchi metrics into two classes : class A in which the vector $a_{l}$ is zero, and class B in which it has one non vanishing component, say $a_{1}$.
\item[-] An invariant Weyl struture may then be written as :
$$\begin{aligned}
d s^{2}=g_{\mu \nu} d x^{\mu} d x^{\nu}=d T^{2}+h_{i j}(T) \sigma^{i} \sigma^{j} & ; \quad \gamma=\gamma_{0}(T) d T+\gamma_{i}(T) \sigma^{i}, \\
d \sigma^{i}=\frac{1}{2} C_{j k}^{i} \sigma^{j} \wedge \sigma^{k} i, j, k=1,2,3 & ; \quad \mu, \nu=(0, \alpha),(0, \beta) ; \sigma^{i}=\sigma_{\alpha}^{i} d x^{\alpha} \\
\sigma_{\alpha}^{i} \sigma_{\beta}^{j} h_{i j}(T)=g_{\alpha \beta} & ; \quad \sigma_{i}^{\alpha} \sigma_{\alpha}^{j}=\delta_{i}^{j}, \sigma_{i}^{\alpha} \sigma_{\beta}^{i}=\delta_{\beta}^{\alpha},
\end{aligned}$$
where the three $\sigma^{i}$ are one-forms invariant under the isometries of the homogeneous 3-space, characterised by the aforementionned structure constants $C_{j k}^{i}$. Notice that there is no loss of generality in choosing the metric element $g_{00}=1$ as this corresponds to a choice of "proper time " T, but the matrix $h_{i j}$ is a priori non-diagonal. On another hand, one might always choose a representative in the conformal class [g] such that $\gamma_{0}(T) \equiv 0$.
The Ricci tensor associated to the Weyl connection D is defined by :
$$\left[D_{\mu}, D_{\nu}\right] v^{\rho}=\mathcal{R}^{(D) \rho}{ }_{\lambda, \mu \nu} v^{\lambda} \quad, \quad \mathcal{R}_{\mu \nu}^{(D)}=\mathcal{R}_{\mu, \rho \nu}^{(D) \rho}$$
$\mathcal{R}_{\mu \nu}^{(D)}$ is related to $R_{\mu \nu}^{(\nabla)}$, the Ricci tensor associated to the Levi-Civita connection [GB]:
$$\mathcal{R}_{\mu \nu}^{(D)}=R_{\mu \nu}^{(\nabla)}+\frac{3}{2} \nabla_{\nu} \gamma_{\mu}-\frac{1}{2} \nabla_{\mu} \gamma_{\nu}+\frac{1}{2} \gamma_{\mu} \gamma_{\nu}+\frac{1}{2} g_{\mu \nu}\left[\nabla_{\rho} \gamma^{\rho}-\gamma_{\rho} \gamma^{\rho}\right] .$$
\end{itemize}
$R_{\mu \nu}^{(\nabla)}$ may be expressed as (for exemple see [14]) :
$$\begin{aligned}
R_{00}^{(\nabla)} & =-\frac{1}{2} \frac{d}{d T}\left(\frac{h^{\prime}}{h}\right)-\frac{1}{4} K_{i}^{j} K_{j}^{i} ; K_{i}^{j}=\frac{d h_{i k}}{d T} h^{k j} ; h=\operatorname{det}\left[h_{i j}\right], h^{\prime}=\frac{d h}{d T}, \\
R_{0 \alpha}^{(\nabla)} & =\frac{1}{2} \sigma_{\alpha}^{k}\left[C_{j k}^{i}-\delta_{k}^{i} C_{m j}^{m}\right] K_{i}^{j}, \\
R_{\alpha \beta}^{(\nabla)} & =\sigma_{\alpha}^{i} \sigma_{\beta}^{j}\left[R_{i j}^{(3)}-\frac{1}{2} \frac{d K_{i j}}{d T}+\frac{1}{2} K_{i}^{k} K_{k j}-\frac{h^{\prime}}{4 h} K_{i j}\right] ; K_{i j}=K_{i}^{k} h_{k j}=\frac{d h_{i j}}{d T}, \text { e.t.c... }
\end{aligned}$$
where $R_{i j}^{(3)}$, the 3-dimensional Ricci tensor associated to the homogeneous space Levi-Civita connection, in the basis of the one-forms $\sigma^{i}$, may be expressed as a function of the 3-metric $h_{i j}$ and of the structure constants of the group [14, 15].
In the same way, the 4-dimensional Bianchi identity splits :
$$C_{j k}^{i} R_{i}^{(3) j}+C_{j i}^{i} R_{k}^{(3) j}=0 \quad, k=1,2,3 \quad([14], \text { equ. }(116,26))$$
and (see the appendix) :
$$h^{i j} \frac{d}{d T} R_{i j}^{(3)} \equiv \frac{d R^{(3)}}{d T}+K_{i}^{j} R_{j}^{(3) i}=2 C_{j i}^{i} R_{0}^{j}, \text { with } R_{0}^{j}=h^{j i} \sigma_{i}^{\alpha} R_{0 \alpha}^{(\nabla)}, R^{(3)}=R_{i j}^{(3)} h^{i j} .$$
We do not find equation (8) in the standard textbooks on gravity.

\subsection*{2.2 The Gauduchon's gauges}

We computed (using equations (39,40 of the appendix) the components of the tensor $\nabla_{(\mu} \gamma_{\nu)}$ and find ;
$$\begin{aligned}
\nabla_{0} \gamma_{0} & =\frac{d \gamma_{0}}{d T} \\
\nabla_{(0} \gamma_{\alpha)} & =\frac{1}{2} \sigma_{\alpha}^{i} h_{i j} \frac{d \gamma^{j}}{d T} \\
\nabla_{(\alpha} \gamma_{\beta)} & =\frac{1}{2} \sigma_{(\alpha}^{i} \sigma_{\beta)}^{j}\left[\gamma_{0} K_{i j}+2 \gamma^{k} h_{i l} C_{k j}^{l}\right],
\end{aligned}$$
and, as a consequence,
$$\nabla_{\mu} \gamma^{\mu}=\frac{1}{\sqrt{h}} \frac{d}{d T}\left[\sqrt{h} \gamma_{0}\right]-C_{i j}^{i} \gamma^{j} .$$
When $C_{i j}^{i} \equiv 2 a_{j}=0$, which corresponds to class A Bianchi metrics, a special Gauduchon's gauge is obtained through the choice :
$$\gamma_{0}(T) \equiv 0 .$$
In the compact case, the choice (11) is the unique good one ([9],Proposition 5.20).

\subsection*{2.3 The Einstein-Weyl equations}

Einstein-Weyl spaces are defined by :
$$\begin{aligned}
\mathcal{R}_{(\mu \nu)}^{(D)} & =\Lambda^{\prime} g_{\mu \nu} \Leftrightarrow \\
R_{\mu \nu}^{(\nabla)}+\nabla_{(\mu} \gamma_{\nu)}+\frac{1}{2} \gamma_{\mu} \gamma_{\nu} & =\Lambda g_{\mu \nu}, \quad \Lambda=\Lambda^{\prime}-\frac{1}{2}\left[\nabla_{\lambda} \gamma^{\lambda}-\gamma_{\lambda} \gamma^{\lambda}\right] .
\end{aligned}$$

Note that for an exact Einstein-Weyl structure, $\gamma=d f$, the representative metric is conformally Einstein. Note also that the conformal scalar curvature is related to the scalar curvature through:
$$S^{(D)}=g^{\mu \nu} \mathcal{R}_{\mu \nu}^{(D)}=4 \Lambda+2\left[\nabla_{\lambda} \gamma^{\lambda}-\gamma_{\lambda} \gamma^{\lambda}\right]=R^{(\nabla)}+3\left[\nabla_{\lambda} \gamma^{\lambda}-\frac{1}{2} \gamma_{\lambda} \gamma^{\lambda}\right] .$$

For Class A Bianchi metrics, in the special Gauduchon's gauge (11), Einstein-Weyl constraints (12) splits into :
$$\begin{gathered}
\Lambda=-\frac{1}{2} \frac{d}{d T}\left(\frac{h^{\prime}}{h}\right)-\frac{1}{4} K_{i}^{j} K_{j}^{i}, \\
n^{i j} \epsilon_{j k l} K_{i}^{k}=-h_{l i} \frac{d \gamma^{i}}{d T}, \\
\Lambda h_{i j}=R_{i j}^{(3)}-\frac{1}{2} \frac{d K_{i j}}{d T}+\frac{1}{2} K_{i}^{k} K_{k j}-\frac{h^{\prime}}{4 h} K_{i j}+\frac{1}{2} \gamma_{i} \gamma_{j}+\frac{1}{2} \gamma^{k}\left[h_{i m} n^{m n} \epsilon_{n k j}+h_{j m} n^{m n} \epsilon_{n k i}\right] .
\end{gathered}$$

\subsection*{2.4 Diagonal metrics and conformal Kählerness}

Let us restrict ourselves to the diagonal Bianchi metrics, usually written as [7, 8]:
$$d s^{2}=\omega_{1} \omega_{2} \omega_{3}(d t)^{2}+\frac{\omega_{2} \omega_{3}}{\omega_{1}}\left(\sigma^{1}\right)^{2}+\frac{\omega_{1} \omega_{3}}{\omega_{2}}\left(\sigma^{2}\right)^{2}+\frac{\omega_{1} \omega_{2}}{\omega_{3}}\left(\sigma^{3}\right)^{2}$$
Define $\alpha_{i}$ through :
$$\frac{d \omega_{i}}{d t}=\alpha_{i} \omega_{i}+n^{i i} \omega_{j} \omega_{k} \quad, \quad(i, j, k)=\text { circ. perm. }(1,2,3) .$$
In [7], Dancer and Strachan gave the conditions on the $\alpha_{i}$ under which the four dimensional diagonal Bianchi metric is Kähler, but not Hyper-Kähler. These conditions are :
- Class A : two of the $\alpha_{i}$ have to be equal, the third one vanishing ;
- Class B : the three $\alpha_{i}$ have to be proportional to $\omega_{1}$ and to satisfy : $\alpha_{1}=\alpha_{2}+\alpha_{3}$.
Under a conformal transformation preserving the cohomogeneity-one character of a Bianchi metric : $\tilde{g}=\mu^{2}(T) g$, these conditions are easily converted into conditions for Kählerness up to a conformal transformation :
Lemma 1 : A diagonal Bianchi metric (17) is conformal to a Kähler one iff. :
\begin{itemize}
\item[-] Class $A$ metric $\left(a_{i}=0\right)$ : two of the $\alpha_{i}$ are equal ;
\item[-] Class $B$ metric $\left(a_{i}=a \delta_{i 1}\right)$ : the following relations hold :
$$\frac{\alpha_{1}-\alpha_{3}}{a \omega_{1}}=\frac{a \omega_{1}}{\alpha_{2}-\alpha_{1}}=\text { Cste } .$$
\end{itemize}
For a Class A diagonal Bianchi metric , equation (15) leads to
$$\gamma^{i}(T)=\Gamma^{i} \text { constant, }$$
and equations (16) wrote for $i \neq j$ :
$$\begin{aligned}
\frac{1}{2} \gamma_{i} \gamma_{i}+\nabla_{(i} \gamma_{j)}=0 & , \quad i \neq j \quad \Leftrightarrow \\
\omega_{1} \omega_{2} \omega_{3} \Gamma^{i} \Gamma^{j}=\Gamma^{k}\left[n^{i i} \omega_{j}^{2}-n^{j j} \omega_{i}^{2}\right] & , \quad(i, j, k)=\text { circ. perm. }(1,2,3) .
\end{aligned}$$

By inspection of the different possibilities for the $n^{i i}$ [14], it is readily shown that at least two of the $\Gamma^{i}$ necessarily vanish, with no other constraint for Bianchi $I$ and $I I$; for Bianchi $V I_{0}$, the three of them vanishing, the metric is necessarily conformally Einstein ; for Bianchi $V I I_{0}$ and $V I I I\left[n^{11}=n^{22}=+1\right]$ the third $\Gamma^{3}$ is constrained by
$$\Gamma^{3}\left[\omega_{1}^{2}-\omega_{2}^{2}\right]=0$$
then, either the metric is conformally Einstein or, with $\omega_{1}^{2}=\omega_{2}^{2}$, the metric is conformally Kähler (thanks to Lemma 1). For Bianchi $I X$ case, the same result holds, the special direction being unfixed (it will be chosen in the same direction as for Bianchi $V I I_{0}$ and $V I I I$ ). A Corollary of this analysis is that in all Class A cases, the dual of the one form $\gamma$ is a Killing vector.

In these three types of Bianchi metrics,
$$n^{11}=n^{22}=+1, \quad \Gamma^{1}=\Gamma^{2}=0, \quad \omega_{1}=\omega_{2}=\omega, \quad \alpha_{1}=\alpha_{2}=\alpha,$$
and the remaining equations $(14,16)$ wrote in the vierbein basis corresponding to (17)( a comma indicates a derivative with respect to $t$ ):
$$\text { (00) } 2(\omega)^{2} \omega_{3} \Lambda=-2 \alpha^{\prime}-\alpha_{3}^{\prime}-\left(\alpha_{3}\right)^{2}+4 \alpha_{3} \alpha+2 \alpha_{3} \omega_{3}+n^{33} \frac{(\omega)^{2}}{\omega_{3}}\left(2 \alpha-\alpha_{3}\right) .$$
Consider the function $u(t)=\frac{\alpha_{3}}{\omega^{2}}$. Its derivative is readily obtained, using the difference of the (00) and (33) equations (21) :
$$\frac{d u}{d t}=-\frac{1}{2} \omega^{2}\left[\left(\Gamma^{3}\right)^{2}+u^{2}\right]<0 .$$
Then one can change the variable $t$ into $u$ and compute :
$$\frac{d \omega_{3}}{d u}=-2 \frac{n^{33}+u \omega_{3}}{\left(\Gamma^{3}\right)^{2}+u^{2}},$$
which integrates to :
$$\omega_{3}(u)=2 \frac{-n^{33} u+k}{\left(\Gamma^{3}\right)^{2}+u^{2}} .$$
Then one gets :
$$\alpha(u)=-2 \frac{-n^{33} u+k}{\left(\Gamma^{3}\right)^{2}+u^{2}}-\frac{1}{4}\left[\left(\Gamma^{3}\right)^{2}+u^{2}\right] \frac{d \omega^{2}}{d u} \quad, \quad \alpha_{3}(u)=u \omega^{2}(u) .$$
The difference of the (11) and (33) equations (21) then gives a second order linear differential equation on $\omega^{2}(u)$ :
$$\begin{aligned}
\frac{d^{2} \omega^{2}}{d u^{2}} & +\left[\frac{6 u}{\left(\Gamma^{3}\right)^{2}+u^{2}}-\frac{2 n^{33}}{n^{33} u-k}\right] \frac{d \omega^{2}}{d u} \\
& -4\left[\frac{\left(\Gamma^{3}\right)^{2}}{\left(\left(\Gamma^{3}\right)^{2}+u^{2}\right)^{2}}+\frac{k}{\left(n^{33} u-k\right)\left(\left(\Gamma^{3}\right)^{2}+u^{2}\right)}\right] \omega^{2}+\frac{8 n^{33}}{\left(\left(\Gamma^{3}\right)^{2}+u^{2}\right)^{2}}=0 .
\end{aligned}$$

The solution is :
$$\begin{aligned}
\omega^{2} & =\frac{4}{\left(\Gamma^{3}\right)^{2}+u^{2}} \Omega^{2}, \text { with } \Omega^{2}=n^{33}+\lambda_{1}\left[n^{33}\left(u^{2}-\left(\Gamma^{3}\right)^{2}\right)-2 k u\right]+ \\
& +\lambda_{2}\left[\left[n^{33}\left(u^{2}-\left(\Gamma^{3}\right)^{2}\right)-2 k u\right] \Gamma^{3} \arctan \left(\frac{u}{\Gamma^{3}}\right)+\left(\Gamma^{3}\right)^{2}\left[n^{33} u-2 k\right]\right] .
\end{aligned}$$
Equations $(22,25)$ and
$$\frac{d u}{d t}=-2 \Omega^{2}$$
give the distance ${ }^{1}$ and Weyl form as functions of the new "proper time" $u$ :
$$\begin{aligned}
d s^{2} & =2 \frac{-n^{33} u+k}{\Omega^{2}\left(\left(\Gamma^{3}\right)^{2}+u^{2}\right)^{2}}(d u)^{2}+2 \frac{-n^{33} u+k}{\left(\Gamma^{3}\right)^{2}+u^{2}}\left[\left(\sigma^{1}\right)^{2}+\left(\sigma^{2}\right)^{2}\right]+2 \frac{\Omega^{2}}{-n^{33} u+k}\left(\sigma^{3}\right)^{2}, \\
\gamma & =\frac{2 \Gamma^{3} \Omega^{2}}{-n^{33} u+k} \sigma^{3} .
\end{aligned}$$
Finaly, the conformal scalar curvature is the constant
$$S^{D}=4 \lambda_{2}\left(\Gamma^{3}\right)^{4} .$$
Under the conformal transformation $\tilde{g}=\left[\left(\Gamma^{3}\right)^{2}+u^{2}\right] g / 2$, the metric may be rewriten in the standard form (17) with
$$\tilde{\omega}_{1}=\tilde{\omega}_{2}=\Omega \sqrt{\left.\left(\Gamma^{3}\right)^{2}+u^{2}\right)}, \quad \tilde{\omega}_{3}=-n^{33} u+k,$$
the "proper time" $\tilde{t}$ being given by
$$d \tilde{t}=-\frac{d u}{\Omega^{2}\left(\left(\Gamma^{3}\right)^{2}+u^{2}\right)} .$$
Then,
$$\frac{d \tilde{\omega}_{3}}{d \tilde{t}}-n^{33} \tilde{\omega}_{1} \tilde{\omega}_{2}=\tilde{\omega}_{3} \tilde{\alpha}_{3}=0 \quad, \tilde{\alpha}_{1}=\tilde{\alpha}_{2},$$
ensuring that the metric $\tilde{g}$ is Kähler.
Then we have proved the
Theorem 1 : The most general (non-)compact non-exact Einstein-Weyl structure with a diagonal Bianchi VII , VIII or IX metric is conformal to a Kähler 4-parameters's one. In particular, in the Bianchi IX case, the Kähler metric is the one found in [GB, equ.(27)].

In the following Section, we shall consider non-diagonal Bianchi metrics ${ }^{2}$, but still restrict ourselves to Class A ones, where the particular choice of Gauduchon's gauge (11) will be of great help.

\footnotetext{
${ }^{1}$ Of course, the 4 parameters $k, \Gamma^{3}, \lambda_{1}, \lambda_{2}$ and the "time" variable $u$ are constrained by positivity : $\Omega^{2}>0, \quad-n^{33} u+k>0$.
${ }^{2}$ When $\gamma=0$ (Einstein equations), and for Bianchi VIII and IX metrics, it was shown in [8] that, thanks to (15), the looked-for Einstein metrics may be chosen to be diagonal. I thank Paul Tod for a clarifying discussion on that assertion.
}

\section*{3 (Non-)compact Einstein-Weyl structures with class A Bianchi metrics.}

We first prove the
Lemma 2 : In the special gauge $\gamma_{0}=0$, Einstein-Weyl structures with a Class A Bianchi metric have a constant conformal scalar curvature $S^{D}$.

Using $\nabla_{\mu} \gamma^{\mu}=0$, the conformal scalar curvature (13) writes
$$S^{(D)}=4 \Lambda-2 \gamma_{i} \gamma^{i} .$$
Contracting equation (16) with $K^{i j}$, using (14,15), leads to :
$$K^{i j} R_{i j}^{(3)}=\frac{d}{d T}\left[\frac{1}{4} K_{i}^{j} K_{j}^{i}-\left(\frac{h^{\prime}}{2 h}\right)^{2}-\frac{1}{2} \gamma_{i} \gamma^{i}\right] .$$
Our Bianchi identity (8), with $C_{i j}^{i}=2 a_{j}=0$, then gives :
$$R^{(3)}+\frac{1}{4} K_{i}^{j} K_{j}^{i}-\left(\frac{h^{\prime}}{2 h}\right)^{2}-\frac{1}{2} \gamma_{i} \gamma^{i}=\text { Constant } .$$
Contracting now equation (16) with $h^{i j}$, using (14), leads to :
$$R^{(3)}+\frac{3}{4} K_{i}^{j} K_{j}^{i}+\frac{d}{d T}\left(\frac{h^{\prime}}{h}\right)-\left(\frac{h^{\prime}}{2 h}\right)^{2}+\frac{1}{2} \gamma_{i} \gamma^{i}=0$$
which, combined with $(31,14)$ gives
$$2 \Lambda-\gamma_{i} \gamma^{i} \equiv S^{(D)} / 2=\text { Constant } \quad \text { Q.E.D. }$$
We have the
Corollary 1 : Einstein-Weyl structures with a Class A Bianchi metric have a conformal scalar curvature $S^{(D)}$ of constant sign on the manifold.

We may now prove the
Lemma 3 : In any Gauduchon's gauge $\nabla_{\mu} \gamma^{\mu}=0$, all Einstein-Weyl structures with a constant conformal scalar curvature $S^{D}$ are such that $D^{\mu}\left[\nabla_{(\mu} \gamma_{\nu)}\right]$ vanishes.

Acting with $\nabla^{\mu}$ on the Einstein-Weyl constraint (12) in the Gauduchon gauge and using the four-dimensional Bianchi identity, the constant value of $S^{D} \equiv R^{(\nabla)}-3 / 2 \gamma_{\mu} \gamma^{\mu}$, one gets :
$$\nabla^{\mu}\left[\nabla_{(\mu} \gamma_{\nu)}\right]+\gamma^{\mu}\left[\nabla_{(\mu} \gamma_{\nu)}\right]=-\frac{1}{4} \nabla_{\nu} S^{D} \quad \text { Q.E.D. }$$
Note that in the compact case, contraction of the previous identity with $\gamma^{\nu}$, followed by an integration on the manifold, leads to the vanishing of $\nabla_{(\mu} \gamma_{\nu)}$ [11].
\begin{itemize}
\item[-] Considering the $\nu=0$ component of the previous equation, the expression of $\left[\nabla_{(\mu} \gamma_{\nu)}\right]$ given by (9), and the formula (41) given in the appendix, we obtain for any class A Bianchi metric :
$$h_{i j} \frac{d}{d T}\left(\frac{1}{2} \gamma^{i} \gamma^{j}\right)=0 .$$
\end{itemize}
\begin{itemize}
\item[-] In the same way, considering the $\nu=\alpha$ component of the equation (34), and multiplying by $\sigma_{i}^{\alpha}$ gives after some manipulations [using the expression of $\nabla_{\alpha} \sigma_{\beta}^{i}$ given in the appendix (40)]:
$$\frac{d}{d T}\left(h_{i j} \frac{d}{d T}\left(\gamma^{j}\right)\right)+\frac{h^{\prime}}{2 h}\left(h_{i j} \frac{d}{d T}\left(\gamma^{j}\right)\right)=C_{i k}^{j} \gamma_{j} \gamma^{k}+X_{i j}\left[h_{m n}\right] \gamma^{j},$$
where the 3 × 3 symmetric matrix $X_{i j}\left[h_{m n}\right]$ is given by
$$X_{i j}=h_{m n} h^{p q} C_{p i}^{m} C_{q j}^{n}+C_{n i}^{m} C_{m j}^{n},$$
which may be expressed for a Class A Bianchi metric as:
$$X_{i j}=\frac{1}{\operatorname{det} h_{m n}}\left[\operatorname{Tr}(h n h n) h_{i j}-(h n h n h)_{i j}\right]+\epsilon_{i k r} \epsilon_{j l s} n^{k l} n^{r s} .$$
\end{itemize}
The contraction of (36) by $\gamma^{i}$ and the use of (35), finally gives :
$$\frac{d \gamma^{i}}{d T} h_{i j} \frac{d \gamma^{j}}{d T}+\gamma^{i} X_{i j} \gamma^{j}=0 .$$
Then we have:
Lemma 4 : For any Class A Bianchi metric $h_{i j}$ such that $(\gamma, h)$ is an Einstein-Weyl structure, the Weyl form $\gamma$ may be written in our particular Gauduchon's gauge as $: \gamma=\Gamma^{i} h_{i j}(T) \sigma^{j}$, where the $\Gamma^{i}$ are constant parameters.

Indeed, at any given time $T$ one can find coordinates $\tilde{\sigma}^{i}$ such that $h_{i j}$ is a diagonal matrix $\tilde{h}_{i j}$, the structure constants being unchanged. The matrix $\tilde{X}$ is then diagonal too, with elements
$$\tilde{X}_{11}=\left[\left(n^{22} \tilde{h}_{22}-n^{33} \tilde{h}_{33}\right)^{2}\right] /\left(\tilde{h}_{22} \tilde{h}_{33}\right)$$
and circular permutations. $h_{i j}$ being a strictly positive definite matrix, we get the vanishing of $\frac{d \tilde{\gamma}^{i}}{d T}$, and, at that time of $\frac{d \gamma^{j}}{d T}$ in any coordinate frame ; the same results then holds at any proper time. Q.E.D.

We are now in position to discuss the issue of the diagonal hypothesis for the metric $h_{i j}(T)$. In the Einstein equation analysis, as explained by Tod [8], the condition (15, with $\gamma_{i}=0$ ) ensures - at least for Bianchi $I X$ and $V I I I$ cases ${ }^{3}$-, a possible simultaneous diagonalisation of the matrices $h_{i j}$ and $\frac{d h_{i j}}{d T}$ or $K_{i j}$ at $T_{0}$, with no change of the structure constants $n^{i j}$.

Here ${ }^{4}$, let us start from a proper time $T_{0}$ such that $h_{i j}$ (and $n^{i j}$ ) is diagonal. By inspection of the possible values of $n^{i i}$, equation (38) ensures that the value of the constants $\Gamma^{i}$ fall into one of three cases :
\begin{itemize}
\item[-] all zero : in particular, this is the sole solution in the Bianchi $V I_{0}$ case. In such a situation, there exists no non-exact Einstein-Weyl structure, and Tod's argument ensures that for Bianchi $V I_{0}, V I I_{0}, V I I I$ and $I X$ cases, there is no loss of generality in the choice of a diagonal metric $h_{i j}(T)$.
\end{itemize}

\footnotetext{
${ }^{3}$ As a matter of facts, Tod's argument can be also used in Bianchi $V I_{0}$ and $V I I_{0}$ cases.
${ }^{4}$ We leave aside the Bianchi $I$ case, with vanishing structure constants and matrix $X$, constant one-form coefficients $\Gamma^{i}$ and where, locally, $\sigma^{i} \equiv d x^{i}$. Two of the $\Gamma^{i}$ vanish, but one cannot prove that the metric stay in a diagonal form.
}
\begin{itemize}
\item[-] at most one of them vanishes : this may happen only in the Bianchi $I X$ case with $\tilde{h}_{i j}\left(T_{0}\right)=h_{0} \delta_{i j}$. Then, a possible simultaneous diagonalisation of the matrix $\frac{d \tilde{h}_{i j}}{d T}$ or $\tilde{K}_{i j}$ at $T_{0}$ is possible, and (38), at $T=T_{0}+\epsilon$, enforces the equalness of the $\tilde{\tilde{K}}_{i i}$ at $T_{0}$. So, at that time, the matrices $\tilde{\tilde{n}}, \tilde{\tilde{h}}, \tilde{\tilde{K}}$ are proportional to the $3 \times 3$ unit matrix. Then, one can find new coordinates where $\frac{d \tilde{\tilde{K}}}{d T}$ is also diagonal, which ensures that the matrices $h$ and $K$ stay in a diagonal form. But, equation (16), where the term $\tilde{\tilde{\gamma}}_{i} \tilde{\tilde{\gamma}}_{j}$ is not in a diagonal form, contradicts the hypothesis of at most one of the $\Gamma^{i}$ vanishing.
\item[-] one of them subsists :
\begin{itemize}
\item[-] this is the case for Bianchi $I I$ case, but (15) enforces no further constraint on the metric and it seems hard to prove that the metric will stay in a diagonal form ;
\item[-] this occurs in Bianchi $V I I_{0}, V I I I$ and $I X$ cases, when at that time, one of the $\tilde{X}_{i i}$ given previously vanishes, say $\tilde{X}_{33}$. For these three cases, we have, for a non-exact Eintein-Weyl structure:
\end{itemize}
\end{itemize}
$$\tilde{n}^{11}=\tilde{n}^{22}=+1, \quad \tilde{\Gamma}^{1}=\tilde{\Gamma}^{2}=0, \quad \tilde{\Gamma}^{3} \neq 0, \quad \tilde{h}_{11}\left(T_{0}\right)=\tilde{h}_{22}\left(T_{0}\right) .$$
Condition (15) ensures that at $T_{0}$ :
$$\frac{d \tilde{h}_{31}}{d T}=\frac{d \tilde{h}_{32}}{d T}=0 .$$
As a consequence, the particular block diagonal structure of the matrices $\tilde{h}_{i j}, \tilde{n}^{i j}$ and $\frac{d \tilde{h}_{i j}}{d T}$ ensures that they may be simultaneously diagonalised at $T_{0}$. So $\tilde{\tilde{h}}_{i j}$ and $\tilde{\tilde{K}}_{i j}$ (thanks to equ. (16)) stay diagonal and we have proved that the constraints that result from Einstein-Weyl equations for Bianchi $I X, V I I I$ and $V I I_{0}$ in the non-diagonal case, are the same as the ones in the diagonal situation.

We can summarize this discussion in a theorem :
Theorem 2 : (Non-)compact Einstein-Weyl Bianchi metrics of the types V $I_{0}, V I I_{0}, V I I I$ and IX are conformally Kähler or conformally Einstein and the metric may be taken in a diagonal form. In the non-exact Einstein-Weyl case, the metric and Weyl form were given in equ.(27). The conformal scalar curvature has a constant sign on the manifold and, in our particular Gauduchon's gauge, the dual of the Weyl form is a Killing vector.

Theorem 1 then gives the following :
Corollary 2 : (Non-)compact non-exact Einstein-Weyl Bianchi IX metrics are conformally Kähler. The metric may be taken in a diagonal form and is conformal to the 4-parameters' one given in [GB.equ.(27)].

\section*{4 Concluding remarks}

In this paper, we have presented a (nearly) complete analysis of the Einstein-Weyl structures $(g, \gamma)$ corresponding to Class A Bianchi metrics. We have shown that, also in the non-compact case, there exists a conformal gauge in which the conformal scalar curvature is a constant, and we have proved that types $V I_{0}, V I I, V I I I$ and $I X$, diagonal or not, are conformally Kähler or
conformally Einstein. We have explained why, in these cases, one can restrict oneself to diagonal metrics. Moreover, in the non-exact Eintein-Weyl cases, the explicit expression for the distance and Weyl 1-form, depending on 4 parameters submitted to some positivity requirements has also been obtained in subsection 2.4.

The further requirement of completeness and compactness will restrict the parameters of our solutions : in particular, Bianchi $V I_{0}, V I I$ and $V I I I$ metrics cannot give compact metrics, their isometry group being non-compact. We shall give elsewhere the full family of Compact Bianchi $I X$ Einstein-Weyl metrics, which, as we have proven here, are conformally Kähler [16].

Let us make a final comment on self-duality constraints on the Weyl connection $\gamma$. In the vierbein basis corresponding to expression (27), one obtains
$$d \gamma=\Gamma^{3}\left(\left(\Gamma^{3}\right)^{2}+u^{2}\right)\left[\frac{d}{d u}\left[\frac{\Omega^{2}}{-n^{33} u+k}\right] e^{0} \wedge e^{3}+n^{33} \frac{\Omega^{2}}{\left(-n^{33} u+k\right)^{2}} e^{1} \wedge e^{2}\right] .$$
The (anti-)self duality of the Weyl connection then needs
$$\Omega^{2}=C\left(-n^{33} u+k\right)^{1 \pm 1} .$$
Due to positivity requirements on $\Omega^{2}$, solutions exist only in the Bianchi $I X$ case, and were given in [GB.Corollary 3][2, 13].

\section*{5 Appendix}

Using equations (3) and the definition of $K_{i}^{j}$ given in (6), the Christoffel connection components are expressed as :
$$\begin{array}{lll}
2 \Gamma_{0 \beta}^{\alpha}=\sigma_{i}^{\alpha} \sigma_{\beta}^{j} K_{j}^{i} & , & 2 \Gamma_{\alpha \beta}^{0}=-\sigma_{\alpha}^{i} \sigma_{\beta}^{j} K_{i j}, \\
2 \Gamma_{\beta \gamma}^{\alpha}=g^{\alpha \delta}\left[g_{\delta \beta, \gamma}+g_{\delta \gamma, \beta}-g_{\beta \gamma, \delta}\right] & , & \text { the other components vanishing } .
\end{array}$$
Then, the covariant derivative of the three basis vectors $\sigma_{\alpha}^{i}$ are found to be :
$$\nabla_{\alpha} \sigma_{\beta}^{i}=\partial_{\alpha} \sigma_{\beta}^{i}-\Gamma_{\alpha \beta}^{(3) \gamma} \sigma_{\gamma}^{i}=\frac{1}{2} C_{j k}^{i} \sigma_{\alpha}^{j} \sigma_{\beta}^{k}+h^{i j} h_{k l} C_{j n}^{k} \sigma_{(\alpha}^{l} \sigma_{\beta)}^{n} .$$
The expression
$$K_{i}^{j} \sigma_{j}^{\beta} \nabla_{\beta} \sigma_{\alpha}^{i}=C_{j k}^{i} K_{i}^{j} \sigma_{\alpha}^{k}$$
will be useful, as well as
$$\nabla_{\alpha} \sigma_{i}^{\alpha}=-\sigma_{i}^{\beta} \sigma_{j}^{\alpha} \nabla_{\alpha} \sigma_{\beta}^{j}=C_{i j}^{j} .$$
The $\nu=0$ component of the Bianchi identity $2 \nabla_{\mu} R_{\nu}^{(\nabla) \mu}=\nabla_{\nu} R^{(\nabla)}$ is split according to $\mu=$ $(0, \alpha)$. Using $(6,40)$ and
$$R^{(\nabla)}=R^{(3)}+2 R_{00}^{(\nabla)}-\frac{1}{4}\left(\frac{h^{\prime}}{h}\right)^{2}+\frac{1}{4} K_{i j} K^{i j}$$
one obtains :
$$2 \nabla_{\mu} R_{0}^{(\nabla) \mu}=\nabla_{0} R^{(\nabla)}-h^{i j} \frac{d R_{i j}^{(3)}}{d T}+2 \nabla_{\alpha}^{(3)} R_{0}^{(\nabla) \alpha} .$$
As a consequence :
$$h^{i j} \frac{d R_{i j}^{(3)}}{d T}=2\left[\nabla_{\alpha}^{(3)} \sigma_{k}^{\alpha}\right] R_{0}^{k},$$
where $R_{0}^{k}=h^{i j} \sigma_{i}^{\alpha} R_{0 \alpha}^{(\nabla)}$.

\section*{References}
[1] K. P. Tod, Class. Quantum Grav. 13 (1996) 2609.
[2] H. Pedersen and A. Swann, Proc. Lond. Math. Soc. 66 (1993) 381.
[3] C. M. Hull and E. Witten, Phys. Lett. 160B (1985) 398 ; C. M. Hull Nucl. Phys. B267 (1986) 266.
[4] E. Bergshoef and E. Sezgin, Mod. Phys. Lett. A1 (1986) 191 ;
P. Howe and G. Papadopoulos, Nucl. Phys. B289 (1986) 264 ; Class. Quantum Grav. 4 (1987) 1749 ; Class. Quantum Grav. 5 (1988) 1647 ;
Ph. Spindel, A. Sevrin, W. Troost and A. Van Proyen, Nucl. Phys. B308 (1988) 662.
[5] F. Delduc and G. Valent, Class. Quantum Grav. 10 (1993) 1201.
[6] G. Bonneau, Class. Quantum Grav. 14 (1997) 2123.
[7] A. S. Dancer and Ian A. B. Straham, Cohomogeneity-One Kähler metrics in "Twistor theory", S. Huggett ed., Marcel Dekker Inc., New York, 1995, p.9.
[8] K. P. Tod, Cohomogeneity-One metrics with Self-Dual Weyl tensor in "Twistor theory", S. Huggett ed., Marcel Dekker Inc., New York, 1995, p.171.
[9] A. Madsen, Compact Einstein-Weyl manifolds with large symmetry group, PhD. Thesis, Odense University, 1995.
[10] R. Gauduchon, Math. Ann. 267 (1984) 495.
[11] K. P. Tod, J. London Math.Soc. 245(1992) 341.
[12] H. Pedersen and A. Swann, J. Reine Angew. Math. 441 (1993) 99.
[13] A. Madsen, Class. Quantum Grav. 14 (1997) 2635.
[14] L. D. Landau and E. M. Lifshitz, The Classical Theory of Fields, 4th edition (Oxford : Pergamon Press, 1975).
[15] V. A. Belinskii et al., Advances in Phys. 31 (1982) 639.
[16] G. Bonneau, Compact Einstein-Weyl four-dimensionnal manifolds, preprint PAR/LPTHE/98-25.
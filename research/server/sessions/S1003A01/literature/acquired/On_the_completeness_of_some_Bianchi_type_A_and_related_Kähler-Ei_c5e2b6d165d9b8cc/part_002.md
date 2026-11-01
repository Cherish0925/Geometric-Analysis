---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: On the completeness of some Bianchi type A and related Kähler-Einstein metrics]

Similarly the pair in the third line in (59) translates to $a_{y y}-(c \nu)_{y} /(c \nu) a_{y}-$ $c^{2} \chi \nu a=0$ and $r=a_{y} /(c \nu)$, with a similar remark as above if $\nu$ vanishes and local existence as an ODE in $y$ is again guaranteed.

The integrability conditions ensuring that the above partial integrations give consistent solutions to these PDEs are all guaranteed to hold via (50). For example, from the first and third lines of (59), $a_{x y}=\left(\alpha_{y}+c \beta \chi\right) a+\left(\beta_{y}+c \alpha \nu\right) r$ and $a_{y x}=-c \beta \nu a+\left((c \nu)_{x}-c \alpha \nu\right) r$, so that the mixed partials of $a$ will be equal if
$$\begin{array}{r}
\alpha_{y}+c \beta \chi=-c \beta \nu, \\
\beta_{y}+c \alpha \nu=(c \nu)_{x}-c \alpha \nu .
\end{array}$$
Unraveling the definitions of these quantities, the first equation reduces to (50)iii), while the second equation holds in lieu of (50)ii),v).

We now intend to apply Theorem 4, so we need to verify the Lie bracket relations (3)-(7). Clearly x and y commute, whereas $[\mathbf{k}, \mathbf{t}]$ was already discussed. The remaining four relations follow from (59), so long as the functions $A, \ldots H$ are defined by $\alpha=A-E=H-D, \beta=B-F=G-C, \nu=B+F$, $\chi=C+G$ and $0=A+E=D+H$. It is a routine matter to check that under these definitions (6)-(7) also hold, and $P, Q, R, S$ are derived from $A, \ldots H$ in accordance with (12). Finally, the domain of $\tau$ is clearly that of $x$, i.e. all of $M$.

By Theorem 4, (10) holds, and as $N=0$, the metric
$$\begin{aligned}
g=\hat{\mathbf{x}}^{2}+ & \hat{\mathbf{y}}^{2}+2\left(\widehat{\mathbf{k}-\mathbf{t}}^{2}+\widehat{\mathbf{k}+\mathbf{t}}^{2}\right) \\
& =\frac{1}{(a s-r b)^{2}}\left((s d u-r d v)^{2}+(-b d u+a d v)^{2}\right)+2\left(d x^{2}+c^{2} d y^{2}\right)
\end{aligned}$$
is Kähler and Ricci-flat, and has a totally geodesic foliation with leaf metric $\bar{g}$. Since its coefficients depend on at most two coordinates, the dimension of
the Lie algebra of Killing fields is at least two. This concludes the proof of Theorem 5.

\section*{Appendix A. Outline of the derivation of the ODE and PDE SYSTEMS}
A.1. Generalized PDEs. Suppose one is given a 4-manifold with a frame k, t, x, y satisfying the Lie bracket relations (3)-(5) for functions $A, B, C, D, E$, $F, G, H, L, N$ on the frame domain. The dual coframe $\hat{\mathbf{k}}, \hat{\mathbf{t}}, \hat{\mathbf{x}}, \hat{\mathbf{y}}$ then satisfies
$$\begin{aligned}
& d \hat{\mathbf{k}}=-N \hat{\mathbf{x}} \wedge \hat{\mathbf{y}}-L \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}, \\
& d \hat{\mathbf{t}}=-N \hat{\mathbf{x}} \wedge \hat{\mathbf{y}}-L \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}, \\
& d \hat{\mathbf{x}}=-A \hat{\mathbf{k}} \wedge \hat{\mathbf{x}}-C \hat{\mathbf{k}} \wedge \hat{\mathbf{y}}-E \hat{\mathbf{t}} \wedge \hat{\mathbf{x}}-G \hat{\mathbf{t}} \wedge \hat{\mathbf{y}}, \\
& d \hat{\mathbf{y}}=-B \hat{\mathbf{k}} \wedge \hat{\mathbf{x}}-D \hat{\mathbf{k}} \wedge \hat{\mathbf{y}}-F \hat{\mathbf{t}} \wedge \hat{\mathbf{x}}-H \hat{\mathbf{t}} \wedge \hat{\mathbf{y}} .
\end{aligned}$$
The vanishing of $d^{2}$ on the coframe 1-forms gives four equations, two of which are identical. Writing, for example, $d N=d_{\mathbf{k}} N \hat{\mathbf{k}}+d_{\mathbf{t}} N \hat{\mathbf{t}}+d_{\mathbf{x}} N \hat{\mathbf{x}}+d_{\mathbf{y}} N \hat{\mathbf{y}}$ etc. and separating components yields 12 scalar equations
$$\begin{aligned}
& d_{\mathrm{x}} L=0, \quad d_{\mathrm{y}} L=0, \\
& d_{\mathrm{y}} A=d_{\mathrm{x}} C, \quad d_{\mathrm{y}} B=d_{\mathrm{x}} D, \quad d_{\mathrm{y}} E=d_{\mathrm{x}} G, \quad d_{\mathrm{y}} F=d_{\mathrm{x}} H, \\
& d_{\mathrm{t}} N=N E+N H+L N, \quad d_{\mathrm{k}} N=N A+N D-L N, \\
& d_{\mathrm{t}} A=d_{\mathrm{k}} E-A L+C F-E L-G B, \\
& d_{\mathrm{t}} B=d_{\mathrm{k}} F-B L+B E+D F-F L-F A-H B, \\
& d_{\mathrm{t}} C=d_{\mathrm{k}} G+A G-C L+C H-E C-G L-G D, \\
& d_{\mathrm{t}} D=d_{\mathrm{k}} H+B G-D L-F C-H L .
\end{aligned}$$
Adding and subtracting the two equations (61), the two equations (62) and (65) and the two equations (63)-(64), while using relations (6)-(7), yields six equations of which only five are independent. The resulting equivalent system is
$$\begin{aligned}
& d_{\mathbf{x}} L 0, \quad d_{\mathbf{y}} L=0, \\
& d_{\mathbf{y}} A=d_{\mathbf{x}} C, \quad d_{\mathbf{y}} B=d_{\mathbf{x}} D, \quad d_{\mathbf{y}} E=d_{\mathbf{x}} G, \quad d_{\mathbf{y}} F=d_{\mathbf{x}} H, \\
& d_{\mathbf{k}+\mathbf{t}} N=0, \quad d_{\mathbf{k}-\mathbf{t}} N=2 N^{2}-2 L N, \\
& d_{\mathbf{t}}(F+G)=-d_{\mathbf{k}}(B+C)-(F+G) L+(B+C) L-2(F+G) B+2(B+C) F \\
& d_{\mathbf{k}}(F+G)=d_{\mathbf{t}}(B+C)+(B+C) L+(F+G) L+F^{2}-G^{2}+B^{2}-C^{2}, \\
& d_{\mathbf{t}}(B-C)=d_{\mathbf{k}}(F-G)-(B-C) L-(F-G) L-(B+C)^{2}-(F+G)^{2} .
\end{aligned}$$
Assume now that $M$ admits a Kähler metric making our frame orthonormal, which is additionally Einstein. Then, in addition to the above system, the six
equations (10) reproduced below also hold.
$$\begin{aligned}
& \lambda=-N(2 L+C-H+A-F) \\
& \lambda=-L(2 L+C-H+A-F)+d_{\mathbf{k}-\mathbf{t}} L-d_{\mathbf{t}}(C-H)+d_{\mathbf{k}}(A-F), \\
& 0=d_{\mathbf{x}}(L+C-H), \quad 0=d_{\mathbf{x}}(L+A-F), \\
& 0=d_{\mathbf{y}}(L+C-H), \quad 0=d_{\mathbf{y}}(L+A-F) .
\end{aligned}$$
At this point our derivation splits into cases.
A.2. The case $\lambda \neq 0$. If the Einstein constant $\lambda$ is nonzero, then by (72)
$$2 L+C-H+A-F \text { is nowhere vanishing. }$$
In that case, (72), (74) and (75) clearly imply
$$d_{\mathbf{x}} N=0, \quad d_{\mathbf{y}} N=0 .$$
Additionally, by the second of equations (3), we have the following basic fact: for any smooth function $f$ on the frame domain,
$$\text { if } d_{\mathbf{x}} f=d_{\mathbf{y}} f=0 \text { then } d_{\mathbf{k}+\mathbf{t}} f=0 \text {. }$$
Thus from (66) $d_{\mathbf{k}+\mathbf{t}} L=0$. This, in conjunction with (66), (74), (75) and the basic fact imply in turn
$$\begin{array}{lll}
d_{\mathbf{x}}(A-F)=0, & d_{\mathbf{y}}(A-F)=0, & d_{\mathbf{k}+\mathbf{t}}(A-F)=0, \\
d_{\mathbf{x}}(C-H)=0, & d_{\mathbf{y}}(C-H)=0, & d_{\mathbf{k}+\mathbf{t}}(C-H)=0 .
\end{array}$$
Among these, the third and sixth equations imply
$$d_{\mathbf{k}-\mathbf{t}}(2 L+C-H+A-F)=2\left(d_{\mathbf{k}-\mathbf{t}} L-d_{\mathbf{t}}(C-H)+d_{\mathbf{k}}(A-F)\right) .$$
As we can substitute this in (73) we note the following: (72) implies both that $N$ is nowhere vanishing, and that we can replace $2 L+C-H+A-F$ with $-\lambda / N$. This then implies that the second equation in (68) yields (73). We can thus drop (73) from our system.

We now introduce the change of variables (12) valid at points of the frame domain where
$$F+G \neq 0,$$
and note its inverse.
$$\begin{array}{ll}
B=[(P+Q)+2 R \sin S] / 4, & C=[-(P+Q)+2 R \sin S] / 4, \\
F=[(P-Q)+2 R \cos S] / 4, & G=[-(P-Q)+2 R \cos S] / 4 .
\end{array}$$
Since
$$A-F=(N-F+G) / 2, \quad C-H=(N-B+C) / 2$$
by (6)-(7), it follows from (78) and (77) that
$$d_{\mathbf{x}}(F-G)=0, d_{\mathbf{y}}(F-G)=0, d_{\mathbf{x}}(B-C)=0 \text { and } d_{\mathbf{y}}(B-C)=0 .$$
Hence
$$\begin{array}{lll}
d_{\mathbf{x}} P=0, & d_{\mathbf{y}} P=0, & d_{\mathbf{k}+\mathbf{t}} P=0, \\
d_{\mathbf{x}} Q=0, & d_{\mathbf{y}} Q=0, & d_{\mathbf{k}+\mathbf{t}} Q=0,
\end{array}$$
where the above basic fact was also employed.

Next we show that the four equations (67) can be replaced by two equivalent equations in terms of $R$ and $S$. On the one hand, by (82), $d_{\mathbf{y}} B=d_{\mathbf{y}}(B+$ $C) / 2=d_{\mathbf{y}}(R \sin S) / 2, d_{\mathbf{x}} C=d_{\mathbf{x}}(B+C) / 2=d_{\mathbf{x}}(R \sin S) / 2, d_{\mathbf{y}} F=d_{\mathbf{y}}(F+$ $G) / 2=d_{\mathbf{y}}(R \cos S) / 2, d_{\mathbf{x}} G=d_{\mathbf{x}}(F+G) / 2=d_{\mathbf{x}}(R \cos S) / 2$. On the other hand $d_{\mathbf{y}} A=d_{\mathbf{y}}(R \cos S) / 2, d_{\mathbf{x}} D=-d_{\mathbf{x}}(R \cos S) / 2, d_{\mathbf{y}} E=-d_{\mathbf{y}}(R \sin S) / 2, d_{\mathbf{x}} H=$ $d_{\mathbf{x}}(R \sin S) / 2$, because (6)-(7) imply $A=(N+F+G) / 2, D=(N-F-G) / 2$, $E=-(N+B+C) / 2, H=(-N+B+C) / 2$. Thus (67) can be replaced by the two equations
$$\begin{aligned}
d_{\mathbf{y}}(R \cos S) & =d_{\mathbf{x}}(R \sin S), \\
d_{\mathbf{y}}(R \sin S) & =-d_{\mathbf{x}}(R \cos S) .
\end{aligned}$$

Finally, equations (69)-(71) are replaced by
$$\begin{aligned}
d_{\mathbf{t}}(R \cos S) & =-d_{\mathbf{k}}(R \sin S)-R L(\cos S-\sin S) \\
& +\frac{1}{2}(P-Q) R \sin S-\frac{1}{2}(P+Q) R \cos S, \\
d_{\mathbf{k}}(R \cos S) & =d_{\mathbf{t}}(R \sin S)+R L(\sin S+\cos S) \\
& +\frac{1}{2}(P-Q) R \cos S+\frac{1}{2}(P+Q) R \sin S, \\
\frac{1}{2} d_{\mathbf{t}}(P+Q) & =\frac{1}{2} d_{\mathbf{k}}(P-Q)-P L-R^{2} .
\end{aligned}$$
The justification is straightforward, except for noting that the last two terms of (69) equal $2(C F-G B)$, which, via (80), is calculated to equal $[R(P-Q) \sin S-$ $R(P+Q) \cos S] / 2$.

So far, we know that the $d_{\mathbf{x}}, d_{\mathbf{y}}, d_{\mathbf{k}+\mathbf{t}}$ derivatives of $L, N, P$ and $Q$ vanish. Our goal now is to prove the same for $R$ and $S$, and also find the $d_{\mathbf{k}-\mathbf{t}}$ derivatives of all these quantities. Looking at (86), as $d_{\mathbf{k}+\mathbf{t}} Q=0$, it becomes
$$\frac{1}{2} d_{\mathbf{k}-\mathbf{t}} P=P L+R^{2}$$
Applying $d_{\mathbf{x}}, d_{\mathbf{y}}$, and $d_{\mathbf{k}+\mathbf{t}}$ to this equation, and employing the Lie bracket relations (3)-(5), we find that
$$d_{\mathbf{x}} R=0, \quad d_{\mathbf{y}} R=0, \quad d_{\mathbf{k}+\mathbf{t}} R=0 .$$
Using this we see from (83) that, as $R \neq 0$ under our assumptions, we have
$$d_{\mathbf{x}} S=0, \quad d_{\mathbf{y}} S=0, \quad d_{\mathbf{k}+\mathbf{t}} S=0 .$$

Now (84)-(85) can be converted to the form
$$\alpha=-\beta \tan S, \quad \beta=\alpha \tan S,$$
for certain expressions $\alpha, \beta$ which thus vanish. Their vanishing is equivalent to the equations
$$d_{\mathbf{t}} R=-R d_{\mathbf{k}} S-R L-\frac{1}{2}(P+Q) R, \quad d_{\mathbf{k}} R=R d_{\mathbf{t}} S+R L+\frac{1}{2}(P-Q) R .$$

As $d_{\mathbf{k}+\mathbf{t}} R=0$ and $d_{\mathbf{k}+\mathbf{t}} S=0$, adding and subtracting these to the above gives
$$d_{\mathbf{k}-\mathbf{t}} S=-Q, \quad d_{\mathbf{k}-\mathbf{t}} R=2 R L+P R .$$
Now from (11) we have $d \tau=\hat{\mathbf{k}}-\hat{\mathbf{t}}$ in an open set $V$, and $d_{\mathbf{k}-\mathbf{t}} \tau=2$ due to the metric values on $\mathbf{k}$ and t. Thus $L, N, P, Q, R$ and $S$ are functions of $\tau$ in the sense of section 6. Employing the abuse of notation described there, the second of equations (68) along with equations (87) and (89) show that ODEs in (13) hold for $N^{\prime}, P^{\prime}, R^{\prime}$ and $S^{\prime}$.

As $N$ is nowhere vanishing, the only remaining independent equation is (72), which in the variables (12) is written, with the help of the definition of $P$ and (6)-(7), in the form
$$2 \lambda=-N(4 L+2 N-P) .$$
However, differentiating (90) with respect to $\tau$, then replacing $N^{\prime}$ by its expression from (13) and simplifying yields, as $N$ is nowhere vanishing, the equation for $L^{\prime}$ in (13). This concludes the case $\lambda \neq 0$.
A.3. The case $\lambda=0, N=0$. If $\lambda=0$, by (72), at each point either (76) does not hold, or $N=0$. We assume the latter everywhere:
$$N=0 \text { on } V \cap\{F+G \neq 0\} .$$
Using (81), which still holds, when $N=0$ equation (73) can be written in the form
$$-L(2 L-P / 2)+d_{\mathbf{k}-\mathbf{t}} L+d_{\mathbf{t}}(B-C) / 2-d_{\mathbf{k}}(F-G) / 2=0 .$$
Applying (71) and (12) gives (14)iii). Applying $d_{\mathbf{x}}$ and $d_{\mathbf{y}}$ to the latter and using (66) gives $d_{\mathbf{x}} R=0, d_{\mathbf{y}} R=0$. As the passage from (67) to (83) is still valid, the latter gives the vanishing of $d_{\mathbf{x}} S$ and $d_{\mathbf{y}} S$. As the $d_{\mathbf{x}}, d_{\mathbf{y}}$ parts of (78) still hold, they lead as before to the vanishing of the $d_{\mathbf{x}}$ and $d_{\mathbf{y}}$ derivatives of $P$ and $Q$.

Of equations (66)-(75), that always hold, the ones whose consequences have not yet been explored are (69)-(71), which translate in the variables (12) to (84)-(86). Of the latter equations, the first two translate as before to (88), and adding and subtracting these gives (14)i),ii). Whereas (86) is equivalent (14)iv).

After the rotation in $\mathcal{H}$ that gives $S=\pi / 4$, the equations of (14) turn into those of (50). Conversely, on $(M, g)$ with (3)-(7) and $N=0$, starting from (50) or its general $S$ form (14), along with the assumption on the vanishing of $d_{\mathrm{x}}$ and $d_{\mathbf{y}}$ on $P, Q, R, S, L$, one easily checks that the above steps are reversible and lead to equations (72)-(75) with $\lambda=0$, i.e. to (10), so that the metric is Ricci flat.

\section*{References}
\begin{itemize}
\item[] [AM1] A. B. Aazami and G. Maschler, Kähler metrics via Lorentzian geometry in dimension four, Complex Manifolds 7 (2020), 36--61.
\item[] [AM2] A. B. Aazami and G. Maschler, Canonical Kähler metrics on classes of Lorentzian 4-manifolds, Ann. Global Anal. Geom. 57 (2020), 175-204.
\item[] [BGPP] V. A. Belinskii, G. W. Gibbons, D. N. Page and C. N. Pope, Asymptotically Euclidean Bianchi IX metrics in quantum gravity, Phys. Lett 76B (1978), 433-435.
\end{itemize}
[BDW] A. Betancourt de la Parra, A. S. Dancer and M. Y. Wang, A Hamiltonian approach to the cohomogeneity one Ricci soliton equations and explicit examples of non-Kähler solitons, J. Math. Phys. 57 (2016), 122501, 17 pp.
[B] C. Böhm, Non-compact cohomogeneity one Einstein manifolds, Bull. Soc. math. France, 127 (1999), 135-177.
[C] S. Cecchini, A note on the Gaussian curvature on noncompact surfaces, arXiv:1609.07631.
[DHW] A. S. Dancer, S. J. Hall and M. Y. Wang, Cohomogeneity one shrinking Ricci solitons: an analytic and numerical study, Asian J. Math. 17 (2013), 33-61.
[DS1] A. S. Dancer and I. A. B. Strachan, Kähler-Einstein metrics with SU(2) action, Math. Proc. Cambridge Philos. Soc. 115 (1994), 513-525.
[DS2] A. S. Dancer and I. A. B. Strachan, Cohomogeneity-one Kähler metrics, Twistor theory (Plymouth), 9--27, Lecture Notes in Pure and Appl. Math., 169, Dekker, New York, 1995.
[DW1] A. S. Dancer and M. Y. Wang, Kähler-Einstein Metrics of Cohomogeneity One, Math. Ann., 312 (1998), 503-526.
[DW2] A. S. Dancer and M. Y. Wang, On Ricci solitons of cohomogeneity one, Ann. Global Anal. Geom. 39 (2011), 259-292.
[DM] A. Derdzinski and G. Maschler, Local classification of conformally-Einstein Kähler metrics in higher dimensions, Proc. London Math. Soc. 87 (2003), 779--819.
[L] F. Leitner, Examples of almost Einstein structures on products and in cohomogeneity one, Differential Geom. Appl. 29 (2011), 440-462.
[ON] B. O'Neill, Semi-Riemannian geometry. With applications to relativity, vol. 103 of Pure and Applied Mathematics, Academic Press, 1983.
[Pd] H. Pedersen, Eguchi-Hanson metrics with cosmological constant, Classical and Quantum Gravity 2 (1985), 579-587.
[Pt] P. Petersen, Riemannian geometry, Third edition. Graduate Texts in Mathematics, 171. Springer, Cham, 2016.
[VZ] L. Verdiani and W. Ziller, smoothness conditions in cohomogeneity one manifolds, arXiv:1804.04680.
[W] M. Wink, Cohomogeneity one Ricci Solitons from Hopf Fibrations, arXiv:1706.09712.
[Y] S. T. Yau, Some function-theoretic properties of complete Riemannian manifold and their applications to geometry, Indiana Univ. Math. J. 25 (1976), 659--670.

Department of Mathematics and Computer Science, Clark University, Worcester, MA

Email address: Gmaschler@clarku.edu , Rream@clarku.edu
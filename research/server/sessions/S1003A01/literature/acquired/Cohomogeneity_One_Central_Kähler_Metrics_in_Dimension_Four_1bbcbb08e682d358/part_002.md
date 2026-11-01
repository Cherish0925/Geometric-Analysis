---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Cohomogeneity One Central Kähler Metrics in Dimension Four]

Proof. For any $E(2)$ invariant metric $g$ on $M$, with $r$ the distance along a geodesic perpendicular to the singular orbit,
$$g=d r^{2}+g_{r} .$$
For a metric $g$ of the form (16), as usual, let $r=\int_{-\infty}^{t} a(s) b(s) c(s) d s$, then
$$g=d r^{2}+a^{2} \sigma_{1}^{2}+b^{2} \sigma_{2}^{2}+c^{2} \sigma_{3}^{2} .$$
The ODE's (45)-(48) in this coordinate become
$$\begin{aligned}
& \frac{d a}{d r}=\frac{a}{2}\left(-\frac{a}{b c}+\frac{c}{a b}\right), \\
& \frac{d b}{d r}=\frac{1}{2}\left(\frac{a}{c}+\frac{c}{a}\right), \\
& \frac{d c}{d r}=\frac{c}{2}\left(\frac{a}{b c}-\frac{c}{a b}+\frac{2 \alpha}{a b c}\right), \\
& \frac{d \alpha}{d r}=\alpha \frac{c}{a b} .
\end{aligned}$$
From these it is seen that $a, b, c$ and $\alpha$ can be extended at $r=0$ so that $a$, $c$ and $\alpha$ are even and $b$ is odd, as functions of $r$. Following the notations of Verdiani and Ziller [VZ], the tangent space for $r \neq 0$ splits as
$$T_{p} M=\mathbb{R} \partial_{r} \oplus \mathfrak{k} \oplus \mathfrak{m},$$
where
$$\begin{gathered}
\mathfrak{k}=\operatorname{span}\left\{X_{2}\right\}, \\
\mathfrak{m}=\operatorname{span}\left\{X_{1}, X_{3}\right\}=: \ell_{1},
\end{gathered}$$
and we set
$$V=\operatorname{span}\left\{\partial_{r}, X_{2}\right\}=: \ell_{-1}^{\prime} .$$
Now $\exp \left(\theta X_{2}\right)$ acts on both $V$ and $\mathfrak{m}$ as a rotation by $\theta$, so the weights are $a_{1}=d_{1}=1$. The smoothness conditions for $V$ is that $b$ can be extended to an odd function and $b^{\prime}(0)=1$. Since we know that $b$ can be extended to be odd, we complete from (54) the check that
$$\left.\frac{d b}{d r}\right|_{r=0}=\frac{1}{2}\left(\frac{q}{q}+\frac{q}{q}\right)=1 .$$

Since $\ell_{-1}^{\prime}$ and $\ell_{1}$ are perpendicular, the smoothness conditions in table C of [VZ] are automatically satisfied, while those in table B there, are
$$\begin{aligned}
& a^{2}+c^{2}=\phi_{1}\left(r^{2}\right), \\
& a^{2}-c^{2}=r^{2} \phi_{2}\left(r^{2}\right),
\end{aligned}$$
for some smooth functions $\phi_{1}$ and $\phi_{2}$. Now to see that (57) is satisfied, note that
$$a^{2}+c^{2}=2 a c \frac{d b}{d r} .$$
Since $a, c$, and $\frac{d b}{d r}$ are even, it just remains to check (58). Solving the equations in their power series expansions in $r$ gives $a=q+o\left(r^{4}\right), c=q+o\left(r^{4}\right)$, so that $a^{2}-c^{2}$ has the required form. Thus $g$ extends to a smooth metric on $M$.

The derivation that the Kähler form also extends smoothly proceeds as in [MR1], so we just state the resulting smoothness conditions:
$$\begin{aligned}
& c r+a b=r \phi_{2}\left(r^{2}\right) \\
& c r-a b=r^{3} \phi_{3}\left(r^{2}\right) .
\end{aligned}$$
The first of these is clear from the oddness/evenness properties of $a, b, c$. The above Taylor series expansion of $a, c$, in addition to the one for $b$, namely $b=r+o\left(r^{5}\right)$ easily shows that $c r-a b$ has the required form. \(\square\)

\subsection*{7.4. Completeness.}

Proposition 7.6. For the metrics of Proposition 7.5, all finite length curves remain inside some compact set.

The proof here is identical to that in [MR1], and will thus be omitted. This completes the proof of Theorem 4.

\section*{8. Acknowledgements}

The authors thank Robert Ream for helpful exchanges pertaining to the Verdiani-Ziller method.

\section*{Appendix A. Outline of the derivation of the ODE and PDE systems}
A.1. Generalized PDEs. Suppose one is given a 4-manifold with a frame k, t, x, y satisfying the Lie bracket relations (3)-(5) for functions $A, B, C, D, E$, $F, G, H, L, N$ on the frame domain. The dual coframe $\hat{\mathbf{k}}, \hat{\mathbf{t}}, \hat{\mathbf{x}}, \hat{\mathbf{y}}$ then satisfies
$$\begin{aligned}
& d \hat{\mathbf{k}}=-N \hat{\mathbf{x}} \wedge \hat{\mathbf{y}}-L \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}, \\
& d \hat{\mathbf{t}}=-N \hat{\mathbf{x}} \wedge \hat{\mathbf{y}}-L \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}, \\
& d \hat{\mathbf{x}}=-A \hat{\mathbf{k}} \wedge \hat{\mathbf{x}}-C \hat{\mathbf{k}} \wedge \hat{\mathbf{y}}-E \hat{\mathbf{t}} \wedge \hat{\mathbf{x}}-G \hat{\mathbf{t}} \wedge \hat{\mathbf{y}}, \\
& d \hat{\mathbf{y}}=-B \hat{\mathbf{k}} \wedge \hat{\mathbf{x}}-D \hat{\mathbf{k}} \wedge \hat{\mathbf{y}}-F \hat{\mathbf{t}} \wedge \hat{\mathbf{x}}-H \hat{\mathbf{t}} \wedge \hat{\mathbf{y}} .
\end{aligned}$$

The vanishing of $d^{2}$ on the coframe 1-forms gives four equations, two of which are identical. Writing, for example, $d N=d_{\mathbf{k}} N \hat{\mathbf{k}}+d_{\mathbf{t}} N \hat{\mathbf{t}}+d_{\mathbf{x}} N \hat{\mathbf{x}}+d_{\mathbf{y}} N \hat{\mathbf{y}}$ etc. and separating components yields 12 scalar equations
$$\begin{aligned}
& d_{\mathrm{x}} L=0, \quad d_{\mathrm{y}} L=0, \quad \\
& d_{\mathrm{y}} A=d_{\mathrm{x}} C, \quad d_{\mathrm{y}} B=d_{\mathrm{x}} D, \quad d_{\mathrm{y}} E=d_{\mathrm{x}} G, \quad d_{\mathrm{y}} F=d_{\mathrm{x}} H, \\
& d_{\mathrm{t}} N=N E+N H+L N, \quad d_{\mathrm{k}} N=N A+N D-L N, \\
& d_{\mathrm{t}} A=d_{\mathrm{k}} E-A L+C F-E L-G B, \\
& d_{\mathrm{t}} B=d_{\mathrm{k}} F-B L+B E+D F-F L-F A-H B, \\
& d_{\mathrm{t}} C=d_{\mathrm{k}} G+A G-C L+C H-E C-G L-G D, \\
& d_{\mathrm{t}} D=d_{\mathrm{k}} H+B G-D L-F C-H L .
\end{aligned}$$
Adding and subtracting the two equations (60), the two equations (61) and (64) and the two equations (62)-(63), while using relations (6)-(7), yields six equations of which only five are independent. The resulting equivalent system is
$$\begin{aligned}
& d_{\mathrm{x}} L=0, \quad d_{\mathrm{y}} L=0, \\
& d_{\mathrm{y}} A=d_{\mathrm{x}} C, \quad d_{\mathrm{y}} B=d_{\mathrm{x}} D, \quad d_{\mathrm{y}} E=d_{\mathrm{x}} G, \quad d_{\mathrm{y}} F=d_{\mathrm{x}} H, \\
& d_{\mathrm{k}+\mathrm{t}} N=0, \quad d_{\mathrm{k}-\mathrm{t}} N=2 N^{2}-2 L N, \\
& d_{\mathrm{t}}(F+G)=-d_{\mathrm{k}}(B+C)-(F+G) L+(B+C) L-2(F+G) B+2(B+C) F
\end{aligned}$$
$$d_{\mathbf{k}}(F+G)=d_{\mathbf{t}}(B+C)+(B+C) L+(F+G) L+F^{2}-G^{2}+B^{2}-C^{2},$$
$$d_{\mathbf{t}}(B-C)=d_{\mathbf{k}}(F-G)-(B-C) L-(F-G) L-(B+C)^{2}-(F+G)^{2} .$$
Assume now that $M$ admits a Kähler metric making our frame orthonormal, which is additionally central. Then, in addition to the above system, we have equation (11), which we now reproduce:
$$\begin{aligned}
& -N(2 L+C-H+A-F)[-L(2 L+C-H+A-F) \\
& \left.+d_{\mathbf{k}-\mathbf{t}} L-d_{\mathbf{t}}(C-H)+d_{\mathbf{k}}(A-F)\right] \\
& -d_{\mathbf{x}}(L+C-H) d_{\mathbf{y}}(L+A-F)+d_{\mathbf{y}}(L+C-H) d_{\mathbf{x}}(L+A-F)=\lambda .
\end{aligned}$$
Equations (65)-(71) constitute our system in the general case. With the help of (65), equation (71) can be simplified a little to the form
$$\begin{aligned}
& -N(2 L+C-H+A-F)[-L(2 L+C-H+A-F) \\
& \left.+d_{\mathbf{k}-\mathbf{t}} L-d_{\mathbf{t}}(C-H)+d_{\mathbf{k}}(A-F)\right] \\
& -d_{\mathbf{x}}(C-H) d_{\mathbf{y}}(A-F)+d_{\mathbf{y}}(C-H) d_{\mathbf{x}}(A-F)=\lambda .
\end{aligned}$$
A.2. The equations in new variables. Recall our functions $L, N$ along with the four given in (13) reproduced here.
$$\begin{aligned}
P & =(B-C)+(F-G), & Q & =(B-C)-(F-G), \\
R & =\sqrt{(B+C)^{2}+(F+G)^{2}}, & S & =\tan ^{-1}\left(\frac{B+C}{F+G}\right),
\end{aligned}$$
where $S$ is only defined on the set $\{F+G\} \neq 0$.
In terms of these, we have the inverse transformation
$$\begin{array}{ll}
B=[(P+Q)+2 R \sin S] / 4, & C=[-(P+Q)+2 R \sin S] / 4, \\
F=[(P-Q)+2 R \cos S] / 4, & G=[-(P-Q)+2 R \cos S] / 4 .
\end{array}$$

We can write the system (65)-(70), (72) in these variables as follows
$$\begin{aligned}
& d_{\mathbf{x}} L=0, \quad d_{\mathbf{y}} L=0, \\
& d_{\mathbf{y}} N+d_{\mathbf{y}}(R \cos S)=d_{\mathbf{x}}(R \sin S)-d_{\mathbf{x}}(P+Q) / 2 \\
& d_{\mathbf{x}} N-d_{\mathbf{x}}(R \cos S)=d_{\mathbf{y}}(R \sin S)+d_{\mathbf{y}}(P+Q) / 2 \\
& -d_{\mathbf{y}} N-d_{\mathbf{y}}(R \sin S)=d_{\mathbf{x}}(R \cos S)-d_{\mathbf{x}}(P-Q) / 2 \\
& -d_{\mathbf{x}} N+d_{\mathbf{x}}(R \sin S)=d_{\mathbf{y}}(R \cos S)+d_{\mathbf{y}}(P-Q) / 2 \\
& d_{\mathbf{k}+\mathbf{t}} N=0, \quad d_{\mathbf{k}-\mathbf{t}} N=2 N^{2}-2 L N \\
& d_{\mathbf{t}}(R \cos S)=-d_{\mathbf{k}}(R \sin S)-R L(\cos S-\sin S) \\
& +\frac{1}{2}(P-Q) R \sin S-\frac{1}{2}(P+Q) R \cos S \\
& d_{\mathbf{k}}(R \cos S)=d_{\mathbf{t}}(R \sin S)+R L(\sin S+\cos S) \\
& +\frac{1}{2}(P-Q) R \cos S+\frac{1}{2}(P+Q) R \sin S \\
& \frac{1}{2} d_{\mathbf{t}}(P+Q)=\frac{1}{2} d_{\mathbf{k}}(P-Q)-P L-R^{2} \\
& -N(2 L+N-P / 2)\left[-L(2 L+N-P / 2)+d_{\mathbf{k}-\mathbf{t}} L-\left(d_{\mathbf{t}} N / 2-d_{\mathbf{t}}(P+Q) / 4\right)\right. \\
& \left.+\left(d_{\mathbf{k}} N / 2-d_{\mathbf{k}}(P-Q) / 4\right)\right]-\left(d_{\mathbf{y}} N / 2-d_{\mathbf{y}}(P-Q) / 4\right)\left(d_{\mathbf{x}} N / 2-d_{\mathbf{x}}(P+Q) / 4\right) \\
& +\left(d_{\mathbf{y}} N / 2-d_{\mathbf{y}}(P+Q) / 4\right)\left(d_{\mathbf{x}} N / 2-d_{\mathbf{x}}(P-Q) / 4\right)=\lambda
\end{aligned}$$
The verification is as in [MR1], except that for (84) we used
$$A-F=(N-F+G) / 2, \quad C-H=(N-B+C) / 2,$$
which follows from (6)-(7).
Of these equations, (81)-(82) can be simplified as in [MR1] to
$$d_{\mathbf{t}} R=-R d_{\mathbf{k}} S-R L-\frac{1}{2}(P+Q) R, \quad d_{\mathbf{k}} R=R d_{\mathbf{t}} S+R L+\frac{1}{2}(P-Q) R .$$
Additionally, (84) can be rewritten as
$$\begin{aligned}
& -N(2 L+N-P / 2)\left[-L(2 L+N-P / 2)+d_{\mathbf{k}-\mathbf{t}} L+d_{\mathbf{k}-\mathbf{t}} N / 2-d_{\mathbf{k}-\mathbf{t}} P / 4+d_{\mathbf{k}+\mathbf{t}} Q / 4\right] \\
& +d_{\mathbf{y}} N d_{\mathbf{x}} Q / 4-d_{\mathbf{x}} N d_{\mathbf{y}} Q / 4+d_{\mathbf{y}} Q d_{\mathbf{x}} P / 8-d_{\mathbf{y}} P d_{\mathbf{x}} Q / 8=\lambda .
\end{aligned}$$

At this point our derivation splits into cases.
A.3. The case where all functions depend on $\tau$. Recall that there exists a local function $\tau$ such that $\nabla \tau=\mathbf{k}-\mathbf{t}$. Since
$$d_{\mathbf{x}} \tau=0, \quad d_{\mathbf{y}} \tau=0, \quad d_{\mathbf{k}+\mathbf{t}} \tau=0,$$
it follows that if $A, \ldots H, L, N$ are locally compositions of functions of $\tau$, the equations (65)-(70), (72) simplify to (67)-(70) without the first equation in (67), together with
$$\begin{aligned}
& -N(2 L+C-H+A-F)[-L(2 L+C-H+A-F) \\
& \left.+d_{\mathbf{k}-\mathbf{t}} L-d_{\mathbf{t}}(C-H)+d_{\mathbf{k}}(A-F)\right]=\lambda .
\end{aligned}$$
In terms of the variables (73) this system takes the form
$$\begin{aligned}
& d_{\mathbf{k}-\mathbf{t}} N=2 N^{2}-2 L N, \\
& d_{\mathbf{k}-\mathbf{t}} R=R(P+2 L), \quad 0=-R\left(d_{\mathbf{k}-\mathbf{t}} S+Q\right), \\
& d_{\mathbf{k}-\mathbf{t}} P=2 L P+2 R^{2}, \\
& -N(2 L+N-P / 2)\left[-L(2 L+N-P / 2)+d_{\mathbf{k}-\mathbf{t}}(L+N / 2-P / 4)\right]=\lambda,
\end{aligned}$$
where we have used (86) as well as $d_{\mathbf{k}} \tau=1, d_{\mathbf{t}} \tau=-1$. Alternatively, with a prime denoting differentiation with respect to $\tau$, since $d_{\mathbf{k}-\mathbf{t}} \tau=2$, we can write the system as
$$\begin{aligned}
& N^{\prime}=N^{2}-L N, \\
& R^{\prime}=R(P / 2+L), \quad 0=-R\left(2 S^{\prime}+Q\right), \\
& P^{\prime}=L P+R^{2}, \\
& -N(2 L+N-P / 2)\left[-L(2 L+N-P / 2)+\left(2 L^{\prime}+N^{\prime}-P^{\prime} / 2\right)\right]=\lambda .
\end{aligned}$$
A.4. The case $N=0$. When $N=0$, the only equations that become trivial are (80), but some equations simplify. We only write the resulting system in the variables (73). We have
$$\begin{aligned}
& d_{\mathbf{x}} L=0, \quad d_{\mathbf{y}} L=0, \\
& d_{\mathbf{y}}(R \cos S)=d_{\mathbf{x}}(R \sin S)-d_{\mathbf{x}}(P+Q) / 2, \\
- & d_{\mathbf{x}}(R \cos S)=d_{\mathbf{y}}(R \sin S)+d_{\mathbf{y}}(P+Q) / 2, \\
- & d_{\mathbf{y}}(R \sin S)=d_{\mathbf{x}}(R \cos S)-d_{\mathbf{x}}(P-Q) / 2, \\
& d_{\mathbf{x}}(R \sin S)=d_{\mathbf{y}}(R \cos S)+d_{\mathbf{y}}(P-Q) / 2, \\
& d_{\mathbf{y}} Q d_{\mathbf{x}} P / 8-d_{\mathbf{y}} P d_{\mathbf{x}} Q / 8=\lambda, \\
& d_{\mathbf{k}-\mathbf{t}} R=R\left(d_{\mathbf{k}+\mathbf{t}} S+P+2 L\right), \\
& d_{\mathbf{k}+\mathbf{t}} R=-R\left(d_{\mathbf{k}-\mathbf{t}} S+Q\right), \\
& d_{\mathbf{k}-\mathbf{t}} P-d_{\mathbf{k}+\mathbf{t}} Q=2 L P+2 R^{2},
\end{aligned}$$
where we have written the central curvature equation in (95).
We see that the system decouples, in the sense that the first six equations involve only $d_{\mathbf{x}}, d_{\mathbf{y}}$ derivatives, while the last three involve only $d_{\mathbf{k} \pm \mathbf{t}}$. For these last three, recall from [MR1] that a rotation in the planes spanned by
x, y allows us to dispense with $d_{\mathbf{k} \pm \mathbf{t}} S$ in (96)-(97), simplifying the equations further.

\section*{References}
\begin{itemize}
\item[] [AM1] A. B. Aazami and G. Maschler, Kähler metrics via Lorentzian geometry in dimension four, Complex Manifolds 7 (2020), 36--61.
\item[] [AM2] A. B. Aazami and G. Maschler, Canonical Kähler metrics on classes of Lorentzian 4-manifolds, Ann. Global Anal. Geom. 57 (2020), 175-204.
\item[] [BGPP] V. A. Belinskii, G. W. Gibbons, D. N. Page and C. N. Pope, Asymptotically Euclidean Bianchi IX metrics in quantum gravity, Phys. Lett 76B (1978), 433-435.
\item[] [BM] S. Bando and T. Mabuchi, On some integral invariants on complex manifolds, I. Proc. Japan Acad. Ser. A Math. Sci. 62 (1986), 197--200.
\item[] [CT] X. X. Chen and G. Tian, Ricci flow on Kähler-Einstein surfaces, Invent. Math. 147 (2002), 487-544.
\item[] [DS1] A. S. Dancer and I. A. B. Strachan, Kähler-Einstein metrics with SU(2) action, Math. Proc. Cambridge Philos. Soc. 115 (1994), 513-525.
\item[] [DS2] A. S. Dancer and I. A. B. Strachan, Cohomogeneity-one Kähler metrics, Twistor theory (Plymouth), 9--27, Lecture Notes in Pure and Appl. Math., 169, Dekker, New York, 1995.
\item[] [FT] A. Futaki and K. Tsuboi, Eta invariants and automorphisms of compact complex manifolds, Recent topics in differential and analytic geometry, 251-270, Adv. Stud. Pure Math., 18-I, Academic Press, Boston, MA, 1990.
\item[] [K] S. Kobayashi, Hyperbolic manifolds and holomorphic mappings. An introduction, Second edition. World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ, 2005.
\item[] [L] J. Lafontaine, Courbure de Ricci et fonctionnelles critiques, C. R. Acad. Sci. Paris Sér. I Math. 295 (1982), no. 12, 687-690.
\item[] [M] G. Maschler, Central Kähler metrics, Trans. Amer. Math. Soc. 355 (2003), 2161--2182.
\item[] [MR1] G. Maschler and R. Ream, On the completeness of some Bianchi type A and related Kähler-Einstein metrics, arXiv:2007.06471, to appear in the Journal of Geometric Analysis.
\item[] [MR2] G. Maschler and R. Ream, Cohomogeneity one Kähler-Ricci solitons under a Heisenberg group action and related metrics, arXiv:2010.09218.
\item[] [ON] B. O'Neill, Semi-Riemannian geometry. With applications to relativity, vol. 103 of Pure and Applied Mathematics, Academic Press, 1983.
\item[] [PP] H. Pedersen and Y. S. Poon, Kähler surfaces with zero scalar curvature, Classical Quantum, Gravity 7 (1990), 1707-1719.
\item[] [R] Y. A. Rubinstein, On energy functionals, Kähler-Einstein metrics, and the Moser-Trudinger-Onofri neighborhood, J. Funct. Anal. 255 (2008), 2641--2660.
\item[] [SW] J. Song and B. Weinkove, Energy functionals and canonical Kähler metrics. Duke Math. J. 137 (2007), 159--184.
\item[] [T] V. Tosatti, On the critical points of the $E_{k}$ functionals in Kähler geometry, Proc. Amer. Math. Soc. 135 (2007), 3985--3988.
\item[] [VZ] L. Verdiani and W. Ziller, smoothness conditions in cohomogeneity one manifolds, arXiv:1804.04680.
\end{itemize}

Wichita State University, Wichita, KS
Email address: jeffres@math.wichita.edu
Department of Mathematics and Computer Science, Clark University, Worcester, MA

Email address: gmaschler@clarku.edu
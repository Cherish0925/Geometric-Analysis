---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: Monodromy of certain Painlevé–VI transcendents and reflection groups]

This concludes the proof of the theorem.
2.2.5. The asymptotic behaviour near $1, \infty$ and the monodromy data. We can prove the analogue of Theorem 2.2 near 1 and $\infty$. Namely, for any pair of values $\left(a_{1}, \sigma_{1}\right)$ there exists a unique branch of the solution of $\mathrm{PVI} \mu$ with the asymptotic behaviour
$$y(x) \sim 1-a_{1} x^{1-\sigma_{1}} \quad \text { as } \quad x \rightarrow 1 .$$
It is possible to parameterize the monodromy matrices as in Theorem 2.2 substituting $\sigma_{0}$ with $\sigma_{1}$ and $M_{0}$ with $M_{1}$ and vice-versa. Analogously, for any pair of values ( $a_{\infty}, \sigma_{\infty}$ ) there exists a unique branch of the solution of (PVI) with the asymptotic behaviour
$$y(x) \sim a_{\infty} x^{\sigma_{\infty}} \quad \text { as } \quad x \rightarrow \infty,$$
and it is possible to parameterize the monodromy matrices as before, substituting $\sigma_{0}$ with $\sigma_{\infty}$ and applying the braid $\beta_{2}$ to the monodromy matrices.

\subsection*{2.3. From the local asymptotic behaviour to the global one.}

In this section we prove Theorem 2.1 which gives the asymptotic behaviour of the branches of the solutions in terms of the triplets $\left(x_{0}, x_{1}, x_{\infty}\right)$.
Lemma 2.10. For the solution $y^{(0)}(x)$ of PVI $\mu$ behaving as
$$y^{(0)}(x)=a_{0} x^{1-\sigma_{0}}\left(1+\mathcal{O}\left(x^{\varepsilon}\right)\right) \quad \text { as } \quad x \rightarrow 0,$$
with $0 \leq \sigma_{0}<1$ and $a_{0} \neq 0, a_{0} \neq 1$ for $\sigma_{0}=0$, the canonical form (1.20) of the monodromy matrices $M_{0}^{(0)}, M_{x}^{(0)}, M_{1}^{(0)}$ given by (2.42), (2.41), (2.40), or (2.46), (2.47), (2.45) for $\sigma_{0}=0$, is the following:
$$M_{0}=\left(\begin{array}{cc}
1 & -x_{0}^{(0)} \\
0 & 1
\end{array}\right), \quad M_{x}=\left(\begin{array}{cc}
1 & 0 \\
x_{0}^{(0)} & 1
\end{array}\right), \quad M_{1}=\left(\begin{array}{cc}
1+\frac{x_{1}^{(0)} x_{\infty}^{(0)}}{x_{0}^{(0)}} & -\frac{\left(x_{1}^{(0)}\right)^{2}}{x_{0}^{(0)}} \\
\frac{\left(x_{\infty}^{(0)}\right)^{2}}{x_{0}^{(0)}} & 1-\frac{x_{1}^{(0)} x_{\infty}^{(0)}}{x_{0}^{(0)}}
\end{array}\right),$$
where the triple $\left(x_{0}^{(0)}, x_{1}^{(0)}, x_{\infty}^{(0)}\right)$ is defined, up to equivalence, by the following formulae, for $\sigma_{0} \neq 0$ :
$$\begin{aligned}
& x_{0}^{(0)}=-2 \sin \frac{\pi \sigma_{0}}{2}, \\
& x_{1}^{(0)}=-\sqrt{2\left(\cos \pi \sigma_{0}-\cos 2 \pi \mu\right)} \frac{\sin \frac{\pi \phi}{2}}{\sin \frac{\pi \sigma_{0}}{2}}, \\
& x_{\infty}^{(0)}=-\sqrt{2\left(\cos \pi \sigma_{0}-\cos 2 \pi \mu\right)} \frac{\cos \frac{\pi\left(\sigma_{0}+\phi\right)}{2}}{\sin \frac{\pi \sigma_{0}}{2}},
\end{aligned}$$
with $\phi$ given by
$$e^{i \pi \phi}=\frac{1}{4 a_{0}} \frac{\sigma_{0}+2 \mu}{\sigma_{0}-2 \mu} \frac{\Gamma\left(1+\sigma_{0}\right)^{2} \Gamma\left(1-\frac{\sigma_{0}}{2}\right)^{2} \Gamma\left(1+\mu-\frac{\sigma_{0}}{2}\right) \Gamma\left(1-\mu-\frac{\sigma_{0}}{2}\right)}{\Gamma\left(1-\sigma_{0}\right)^{2} \Gamma\left(1+\frac{\sigma_{0}}{2}\right)^{2} \Gamma\left(1+\mu+\frac{\sigma_{0}}{2}\right) \Gamma\left(1-\mu+\frac{\sigma_{0}}{2}\right)},$$
and for $\sigma_{0}=0$ :
$$\begin{aligned}
& x_{0}^{(0)}=0, \\
& x_{1}^{(0)}=-|\sin \pi \mu| \sqrt{1-a_{0}} \\
& x_{\infty}^{(0)}=-|\sin \pi \mu| \sqrt{a_{0}} .
\end{aligned}$$

The proof of this lemma can be obtained by straightforward computations, using the algorithm of lemma 1.5. Similar formulae for the parameters $\left(x_{0}^{(1)}, x_{1}^{(1)}, x_{\infty}^{(1)}\right)$ and $\left(x_{0}^{(\infty)}, x_{1}^{(\infty)}, x_{\infty}^{(\infty)}\right)$ can be obtained respectively starting from a solution $y^{(1)}(x)$ of PVI $\mu$ behaving as
$$y^{(1)}(x)=1-a_{1}(1-x)^{1-\sigma_{1}}\left(1+\mathcal{O}(1-x)^{\varepsilon}\right) \quad \text { as } \quad x \rightarrow 1,$$
or from another solution $y^{(\infty)}(x)$ of $\mathrm{PVI} \mu$ behaving as
$$y^{(\infty)}(x)=a_{\infty} x^{\sigma_{\infty}}\left(1+\mathcal{O}\left(\frac{1}{x^{\varepsilon}}\right)\right) \quad \text { as } \quad x \rightarrow \infty .$$
So, given an admissible triple $\left(x_{0}, x_{1}, x_{\infty}\right)$, with $x_{i} \in \mathbb{R},\left|x_{i}\right|<2$ for $i=0,1, \infty$, we choose the parameters $\mu,\left(a_{0}, \sigma_{0}\right),\left(a_{1}, \sigma_{1}\right)$ and $\left(a_{\infty}, \sigma_{\infty}\right)$ in such a way that (2.8) is satisfied and
$$x_{i}^{(0)}=x_{i}^{(1)}=x_{i}^{(\infty)}=x_{i}, \quad \text { for } \quad i=0,1, \infty .$$
Using the explicit formulae (2.68), (2.69) for $x_{0} \neq 0$, we derive the expressions (2.10), (2.11). Similarly, using (2.70) for $x_{0}=0$ we derive the expression (2.12). In the same way, we derive the analogous expressions for $\left(a_{1}, \sigma_{1}\right)$ and $\left(a_{\infty}, \sigma_{\infty}\right)$. The three correspondent branches $y^{(0)}(x), y^{(1)}(x), y^{(\infty)}(x)$ of solutions of $\mathrm{PVI} \mu$, with $\mu$ given by (2.8) must coincide. In fact, the associated auxiliary Fuchsian systems have the same, modulo diagonal conjugation, monodromy matrices. This proves the existence of a solution of $\mathrm{PVI} \mu$ with the asymptotic behaviour (2.1), with the indices given by (2.9) and the coefficients specified as above, for any admissible triple $\left(x_{0}, x_{1}, x_{\infty}\right)$, with $x_{i} \in \mathbb{R},\left|x_{i}\right|<2$ for $i=0,1, \infty$. The uniqueness of such a branch follows from theorem 1.3.

Conversely, for any such a solution we obtain an admissible triple $\left(x_{0}, x_{1}, x_{\infty}\right)=$ $\left(x_{0}^{(0)}, x_{1}^{(0)}, x_{\infty}^{(0)}\right)=\left(x_{0}^{(1)}, x_{1}^{(1)}, x_{\infty}^{(1)}\right)=\left(x_{0}^{(\infty)}, x_{1}^{(\infty)}, x_{\infty}^{(\infty)}\right)$, using the formulae (2.68), (2.69) or (2.70) and their analogies. Let us prove that the numbers ( $x_{0}, x_{1}, x_{\infty}$ ) are real and satisfy $\left|x_{i}\right|<2$ for $i=0,1, \infty$. Indeed, from the definition of the parameters, it follows:
$$\left(x_{0}^{(0)}\right)^{2}=4 \sin ^{2} \pi \sigma_{0},\left(x_{1}^{(1)}\right)^{2}=4 \sin ^{2} \pi \sigma_{1},\left(x_{\infty}^{(\infty)}\right)^{2}=4 \sin ^{2} \pi \sigma_{\infty} .$$
This proves that our construction covers, for real $\mu$, all the solutions of $\mathrm{PVI} \mu$ with critical behaviour of algebraic type.

Finally, using corollary 1.5, we infer that the class of solutions of $\mathrm{PVI} \mu$, with real $\mu$, having critical behaviour of algebraic type is invariant with respect to the analytic continuation. The law of transformation of the critical indices $l_{0}, l_{1}, l_{\infty}$ of the expansions (2.1), is described by theorem 1.5.

\subsection*{2.4. The complete list of algebraic solutions}

We summarize the results of this paper in the following
Classification Theorem. Any algebraic solution of the equation $P V I \mu$ with $2 \mu \notin \mathbb{Z}$ is equivalent, in the sense of symmetries (1.22), (1.23), (1.24) to one of the five solutions $\left(A_{3}\right),\left(B_{3}\right),\left(H_{3}\right),\left(H_{3}\right)^{\prime},\left(H_{3}\right)^{\prime \prime}$ below.

We already know that the classes of equivalent algebraic solutions are labelled by the five regular polyhedra and star-polyhedra in the three-dimensional space. We will construct representatives in these classes for the following values of the parameter $\mu$
$$\mu=-\frac{1}{4}, \quad-\frac{1}{3}, \quad-\frac{2}{5}, \quad-\frac{1}{5}, \quad-\frac{1}{3} .$$
The correspondent algebraic solutions will have 4, 3, 10, 10, 18 branches respectively. Recall that these are the lenghts of the orbits (1.33), (1.34), (1.35), (1.36), (1.37) respectively with respect to the action of the pure braid group (see remark 1.11 above). We give now the explicit formulae for the solutions with brief explanations of the derivations of them.

Tetrahedron. We have $\left(x_{0}, x_{1}, x_{\infty}\right)=(-1,0,-1)$, then $\mu=-\frac{1}{4}$ and
$$\begin{aligned}
& y=\frac{(s-1)^{2}(1+3 s)\left(9 s^{2}-5\right)^{2}}{(1+s)\left(25-207 s^{2}+1539 s^{4}+243 s^{6}\right)}, \\
& x=\frac{(s-1)^{3}(1+3 s)}{(s+1)^{3}(1-3 s)} .
\end{aligned}$$
(We present the solution in the parametric form). The monodromy matrices, in the canonical form (1.20), are:
$$M_{0}=\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right) \quad M_{x}=\left(\begin{array}{cc}
1 & 0 \\
-1 & 1
\end{array}\right) \quad M_{1}=\left(\begin{array}{ll}
1 & 0 \\
1 & 1
\end{array}\right) .$$
This solution was found in [Dub] in the implicit form (E.29). This was also obtained, independently, by N. Hitchin (see [Hit2]). To reduce (E.29) to the above form, we have to solve the cubic equation (E. 29 b) with the substitution:
$$t=\frac{32\left(1-18 s^{2}+81 s^{4}\right)}{27\left(1+9 s^{2}+27 s^{4}+27 s^{6}\right)} .$$
Then the three roots of (E. 29 b) are:
$$\begin{aligned}
\omega_{1} & =\frac{13-66 s^{2}-27 s^{4}}{3\left(1+3 s^{2}\right)^{2}} \\
\omega_{2,3} & =\frac{-5+42 s^{2} \pm 144 s^{3}+27 s^{4}}{3\left(1+3 s^{2}\right)^{2}} .
\end{aligned}$$

Cube. We have $\left(x_{0}, x_{1}, x_{\infty}\right)=(-1,0,-\sqrt{2})$ and $\mu=-\frac{1}{3}$. The solution
$$\begin{aligned}
& y=\frac{(2-s)^{2}(1+s)}{(2+s)\left(5 s^{4}-10 s^{2}+9\right)}, \\
& x=\frac{(2-s)^{2}(1+s)}{(2+s)^{2}(1-s)},
\end{aligned}$$
was obtained in [Dub]. The canonical form for the monodromy matrices is:
$$M_{0}=\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right) \quad M_{x}=\left(\begin{array}{cc}
1 & 0 \\
-1 & 1
\end{array}\right) \quad M_{1}=\left(\begin{array}{cc}
1 & 0 \\
-2 & 1
\end{array}\right) .$$

Coxeter group $\mathbf{W}\left(\mathbf{H}_{\mathbf{3}}\right)$, of symmetries of icosahedron. We have three possible choices of the point $\left(x_{0}, x_{1}, x_{\infty}\right)$ which lead to three different solutions.

Icosahedron. The orbit (1.35) corresponds to the standard triple of reflections for the icosahedron. $\left(x_{0}, x_{1}, x_{\infty}\right)=\left(0,-1,-\frac{1+\sqrt{5}}{2}\right)$, then $\mu=-\frac{2}{5}$ and
$$\begin{aligned}
& y=\frac{(s-1)^{2}(1+3 s)^{2}\left(-1+4 s+s^{2}\right)\left(7-108 s^{2}+314 s^{4}-588 s^{6}+119 s^{8}\right)^{2}}{(1+s)^{3}(-1+3 s) P(s)} \\
& x=\frac{(-1+s)^{5}(1+3 s)^{3}\left(-1+4 s+s^{2}\right)}{(1+s)^{5}(-1+3 s)^{3}\left(-1-4 s+s^{2}\right)}
\end{aligned}$$
with
$$\begin{aligned}
P(s)= & 49-2133 s^{2}+34308 s^{4}-259044 s^{6}+16422878 s^{8}-7616646 s^{10}+13758708 s^{12} \\
& +5963724 s^{14}-719271 s^{16}+42483 s^{18} .
\end{aligned}$$
The canonical form for the monodromy matrices is:
$$M_{0}=\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right) \quad M_{x}=\left(\begin{array}{cc}
1 & 0 \\
-1 & 1
\end{array}\right) \quad M_{1}=\left(\begin{array}{cc}
1 & 0 \\
\frac{-3-\sqrt{5}}{2} & 1
\end{array}\right) .$$
The above solution was already obtained in [Dub] in the implicit form (E.33). The above explicit formula can be obtained solving (E. 33 b) in the form:
$$\begin{gathered}
t=\frac{\left(1-4 s-s^{2}\right)\left(-1-4 s+s^{2}\right)\left(-1+5 s^{2}\right)}{\left(1+3 s^{2}\right)^{3}} \\
\omega_{1}=\frac{25-585 s^{2}+3530 s^{4}-6690 s^{6}-3955 s^{8}+507 s^{10}}{\left(1+3 s^{2}\right)^{5}} \\
\omega_{2}=\frac{-7+215 s^{2}-1910 s^{4}-4096 s^{5}+5150 s^{6}+20480 s^{7}+6125 s^{8}-357 s^{10}}{\left(1+3 s^{2}\right)^{5}} \\
\omega_{3}=\frac{-7+215 s^{2}-1910 s^{4}+4096 s^{5}+5150 s^{6}-20480 s^{7}+6125 s^{8}-357 s^{10}}{\left(1+3 s^{2}\right)^{5}}
\end{gathered}$$

The last two solutions for the orbits (1.36) and (1.37), with the icosahedral symmetry are new. They correspond to great icosahedron and great dodecahedron respectively. To compute them we use the following algorithm. The leading terms of the Puiseux expansions near the ramification points $0,1, \infty$ of each branch can be computed by the formulae (2.9), (2.10), (2.11) and (2.12). From this the genus of the algebraic curve $F(y, x)=0$ is easily computed. Namely, the genus of (1.36) is 0 and the genus of (1.37) is 1. Since the symmetries of $\mathrm{PVI} \mu$ preserve the indices $l_{0}, l_{1}, l_{\infty}$ (up to permutations), they preserve the genus too.

We observe that the appearance of genus 1 in the last solution related to the great dodecahedron could seem less surprising if we recall that the topology of this immersed two-dimensional surface is different from the topology of all the other polyhedra and starpolyhedra. In fact, this is a surface of genus 4, while all the others have genus 0 (see [Cox]).

Let us now list the last two solutions.
Great Icosahedron. $\left(x_{0}, x_{1}, x_{\infty}\right)=\left(-1,0, \frac{1-\sqrt{5}}{2}\right)$, then $\mu=-\frac{1}{5}$ and
$$\begin{aligned}
& y=\frac{(-1+s)^{4}(1+3 s)^{2}\left(-1+4 s+s^{2}\right)\left(3-30 s^{2}+11 s^{4}\right)^{2}}{(1+s)(-1+3 s)\left(1+3 s^{2}\right) P(s)} \\
& x=\frac{(-1+s)^{5}(1+3 s)^{3}\left(-1+4 s+s^{2}\right)}{(1+s)^{5}(-1+3 s)^{3}\left(-1-4 s+s^{2}\right)}
\end{aligned}$$
with
$$P(s)=\left(9-342 s^{2}+4855 s^{4}-28852 s^{6}+63015 s^{8}-1942 s^{10}+121 s^{12}\right) .$$
The canonical form for the monodromy matrices is
$$M_{0}=\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right) \quad M_{x}=\left(\begin{array}{cc}
1 & 0 \\
-1 & 1
\end{array}\right) \quad M_{1}=\left(\begin{array}{cc}
1 & 0 \\
\frac{-3+\sqrt{5}}{2} & 1
\end{array}\right) .$$

Great Dodecahedron. $\left(x_{0}, x_{1}, x_{\infty}\right)=\left(-1,-1, \frac{1-\sqrt{5}}{2}\right), \mu=-\frac{1}{3}$. The canonical form for the monodromy matrices is
$$M_{0}=\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right) \quad M_{x}=\left(\begin{array}{cc}
1 & 0 \\
-1 & 1
\end{array}\right) \quad M_{1}=\left(\begin{array}{cc}
\frac{3-\sqrt{5}}{2} & 1 \\
\frac{-3+\sqrt{5}}{2} & \frac{1+\sqrt{5}}{2}
\end{array}\right) .$$
This is the most complicated solution and we will briefly explain how did we obtain it. As we already said, it is an algebraic function with 18 branches. It has two branch points of order 5, two of order 3 and two regular branches, over every ramification
point $0,1, \infty$. The branches $y_{1}(x), \cdots, y_{18}(x)$ near $x=0$ have the form:
$$\begin{aligned}
y_{k}(x) & =e^{\frac{2 \pi i k}{5}}\left(\frac{7}{13}\right)^{2} 6^{\frac{-2}{5}} x^{\frac{4}{5}}+\mathcal{O}(x), \quad k=1, \cdots, 5 \\
y_{k+5}(x) & =e^{\frac{2 \pi i k}{5}} \frac{6^{\frac{4}{5}}}{19^{2}} x^{\frac{2}{5}}+\mathcal{O}\left(x^{\frac{4}{5}}\right), \quad k=1, \cdots, 5 \\
y_{10+k}(x) & =e^{\frac{2 \pi i k}{3}} \frac{2^{\frac{2}{3}}}{18} \frac{1+i \sqrt{15}}{4} x^{\frac{2}{3}}+\mathcal{O}(x), \quad k=1, \cdots, 3 \\
y_{13+k}(x) & =e^{\frac{2 \pi i k}{3}} \frac{2^{\frac{2}{3}}}{18} \frac{1-i \sqrt{15}}{4} x^{\frac{2}{3}}+\mathcal{O}(x), \quad k=1, \cdots, 3 \\
y_{17,18}(x) & =\frac{3 \pm \sqrt{5}}{6} x+\mathcal{O}\left(x^{2}\right) .
\end{aligned}$$
The Puiseux expansions near $x=1$ and $x=\infty$ can be obtained from these formulae applying the symmetries (1.22) and (1.23) respectively. Using these formulae, one can compute any term of the Puiseux expansions of all the branches. Due to computer difficulties, at the moment, we do not manage to produce the explicit elliptic parameterization of the algebraic curve. We give this in the form of an algebraic curve of degree 36.
$$x^{15} F(x, y, t)=0 \quad\left(H_{3}\right)^{\prime \prime}$$
where
$$t=x+\frac{1}{x}$$
and
$$\begin{gathered}
F(x, y, t)=\left(11423613917539180989-57169813730203944 t-13869163074392577 t^{2}\right. \\
\left.+1307302991918736 t^{3}-31962210377 t^{4}-556854952 t^{5}+282475249 t^{6}\right)^{2} x^{9}+ \\
+9(-42194267411458338799378785573556538817 \\
-58759262104428568315429822622247510492 t+ \\
+10095266581644469686796601774497789110 t^{2} \\
-969805106597038829472153249647160780 t^{3} \\
+13082239583395373581545441399627177 t^{4} \\
-77058446549850745165440956773416 t^{5} \\
-2150599531632473735225276196788 t^{6} \\
+5521397776112060589691860200 t^{7} \\
+34431689430132242698256649 t^{8}-4868379539328005204126748 t^{9} \\
+543298990997997546590 t^{10}-5420393254540081020 t^{11}
\end{gathered}$$
$$\begin{gathered}
\left.-79792266297612001 t^{12}\right) x^{8}(1+x) y \\
+3(1958540422461728364360419152068949457061 \\
-2209393132972329408615760780334959957197 t \\
+3730909713982979160856372675878664915614 t^{2} \\
-998456940153012666787445238400320871842 t^{3} \\
+127635631698846877473536225998246411623 t^{4} \\
-1482254497297246657880332587875322027 t^{5} \\
+8847488219466307166390055942913100 t^{6} \\
+115442527212405524632938663371228 t^{7} \\
-1429542565820801871766655325509 t^{8} \\
+7631245862019705473945545029 t^{9} \\
+215859931310548879418863190 t^{10} \\
-61369918621176379581242 t^{11} \\
+443864075501101414537 t^{12} \\
\left.+239376798892836003 t^{13}\right) x^{8} y^{2} \\
+8(-14176454404869485146893293606614356611775 \\
+28055900200716580071561317517835005937542 t \\
-22805214425386778204880821526748969126548 t^{2} \\
+7203824414325261553629527716660045847442 t^{3} \\
-941980967212371956151450075677431178469 t^{4} \\
+8038149376577574092957422850094452382 t^{5} \\
-22951481031624768208910085230213950 t^{6} \\
-1567265072303229457696028497735362 t^{7} \\
+17710721122570843039502588273105 t^{8} \\
-100631536944878626686735036764 t^{9} \\
-513222963217440801801106854 t^{10} \\
+346131811374226777113368 t^{11} \\
\left.-1385596068253512936373 t^{12}\right) x^{7}(1+x) y^{3} \\
+6(372245126038285018174621123839906354129684
\end{gathered}$$
\begin{itemize}
\begin{itemize}
\item[] $-538123164074188598920246979212739683700019 t$
\item[] $+148097514409311992531878851512796911164392 t^{2}$
\item[] $+131183971273631981690818920653550831952470 t^{3}$
\item[] $-81255871706326021946002239342890704787124 t^{4}$
\item[] $+13496764871847929345618085983834973142347 t^{5}$
\begin{itemize}
\item[] $-77522788387610267024773351181536807752 t^{6}$
\begin{itemize}
\item[] $-15773276759106249673670395386220524 t^{7}$
\item[] $+43306225979803766149728090033557588 t^{8}$
\item[] $-398429371182004923439978792917533 t^{9}$
\item[] $+1762391142835398582269106251136 t^{10}$
\begin{itemize}
\item[] $+2388970787440139757429804470 t^{11}$
\begin{itemize}
\item[] $-3439831965306734927530580 t^{12}$
\end{itemize}
\item[] $\left.+6227088023782555081845 t^{13}\right) x^{7} y^{4}$
\end{itemize}
\end{itemize}
\end{itemize}
\end{itemize}
\item[] +6 (-1723593607166532080927038166074395946035900
\begin{itemize}
\item[] $+2040599178888751273951239802196511605636025 t$
\item[] $+233403452055579960658996997839662220718652 t^{2}$
\item[] $-1266443503829326206558682114543567079698662 t^{3}$
\item[] $+601472177228487289796456276889218593842200 t^{4}$
\item[] $-90437995682218432847116536290883275511849 t^{5}$
\begin{itemize}
\item[] $+312726298388429638276816726813440288752 t^{6}$
\item[] $+2550025722128829156352333577788952604 t^{7}$
\item[] $-575104019542617989271403929336386084 t^{8}$
\begin{itemize}
\item[] $+4033434111720024901257683928676919 t^{9}$
\item[] $-12117519775974826925705049828908 t^{10}$
\begin{itemize}
\item[] $-6556200250126220600244219830 t^{11}$
\item[] $+14241314959493049268655304 t^{12}$
\end{itemize}
\item[] $\left.-9850799841945252913527 t^{13}\right) x^{6}(1+x) y^{5}$
\end{itemize}
\end{itemize}
\end{itemize}
\item[] +2 (21644465131825357400382632120971734649857264
\begin{itemize}
\item[] $+1609281090760898028021044308156991213714259 t$
\end{itemize}
\end{itemize}
$$\begin{gathered}
-38819578264561008264384235926474662382590097 t^{2} \\
+19461702669444598007359556763777303231431634 t^{3} \\
+6809228919729818789589103927528063675916654 t^{4} \\
-6502005871163632747227392004794985000703103 t^{5} \\
+1176880351448958476049654953342289787508545 t^{6} \\
-2305666451065939258487468463173953769764 t^{7} \\
-66480299243646643579685794767909280748 t^{8} \\
+15241200180683229312383060139285323669 t^{9} \\
-78386104021612006912908252437015263 t^{10} \\
+148880803913659745854808576095474 t^{11} \\
+57461755817453559455002717038 t^{12} \\
-103978838096755580164874073 t^{13} \\
\left.+22079893897296692642367 t^{14}\right) x^{6} y^{6} \\
+12(-3846090734682844350682028823106084687428444 \\
-6334186503545807261781842904989156398103475 t \\
+13149149531444644750567430723972640952739601 t^{2} \\
-833478059474840476986699901359926517619482 t^{3} \\
-6957568559854570720866520753764257206265698 t^{4} \\
+3704223179468379920674190362976879513996499 t^{5} \\
-576109607175627912516018268715191958362489 t^{6} \\
+449528751470785721434087640482632944192 t^{7} \\
+97703132604175842587572789513022822852 t^{8} \\
-16011119124352462144696375400709770865 t^{9} \\
+57470033726311385832789992330535883 t^{10} \\
-64186326557416461737056084783958 t^{11} \\
-26094692352698228396829172726 t^{12} \\
+25456979816863844482106097 t^{13} \\
\left.-1051423518918890125827 t^{14}\right) x^{5}(1+x) y^{7} \\
+3(10610560214390717981593236262575236159801442
\end{gathered}$$
$+111851425974428655491946571184648885748780846 t$
$-46715489836280837819492546495478177251546881 t^{2}$
$-139030514021835704781706562226557058780091068 t^{3}$
$+91919803393449431080407081029445741045516160 t^{4}$
$+17286168898942635534811373112001322602942242 t^{5}$
$-24220067368877156108293128216367359106738667 t^{6}$
$+4637848726272650440828320863095758089676600 t^{7}$
$-768878602349792937649689712426759282462 t^{8}$
$-1741702208080601219941076960674171058190 t^{9}$
$+291817792658031512381548036217335383393 t^{10}$
$-703979549232767832584811827025318204 t^{11}$
$+431869052449224832223544125220252 t^{12}$
$+211026301709949401515207349982 t^{13}$
$\left.-88672767468343194407328645 t^{14}\right) x^{5} y^{8}$
+ (29516093700614758561713684532397059536112914
$-250427363718702318175164789552712875171021018 t$
$-276026230387316277405019906885146213095909789 t^{2}$
$+798207668051094993868151955635553085940964248 t^{3}$
$-344467523172443772269951999752021715572380244 t^{4}$
$-120301086904813944940738235485125501727252554 t^{5}$
$+109511261517293051818507102282993534830623481 t^{6}$
$-19194080365623650515069714757340701033233072 t^{7}$
$-51032394918091643798626435084286655402518 t^{8}$
$+23520399409116636731567242035209841281394 t^{9}$
$-2981630391452674856104059990243312091171 t^{10}$
$+4599349671236813290177817558881705144 t^{11}$
$-1416023622121443571963532624008680 t^{12}$
$-884464824710945312016748613390 t^{13}$
$\left.+126470477973158698785100695 t^{14}\right) x^{4}(1+x) y^{9}$
\begin{itemize}
\item[] +3 (-10911639347758887707980330460476045164474906
\begin{itemize}
\item[] $-58595420545899882777261835025201788418411880 t$
\item[] $+510148671470006459933001332369933260295921507 t^{2}$
\item[] $-421411310692898883818707378130970229534690273 t^{3}$
\item[] $-167152535194408490298020642999503515413037404 t^{4}$
\item[] $+259430867087315198025819011038004422708530022 t^{5}$
\item[] $-46562493376530130089912033636689480134093531 t^{6}$
\item[] $-21317412351831533402564088853511437604716591 t^{7}$
\item[] $+5998321070650622801147765820299240777440702 t^{8}$
\begin{itemize}
\item[] $+42318724644239526363080933921378429784628 t^{9}$
\item[] $-20025402467700581457477461594500061379211 t^{10}$
\item[] $+2543243908066676381203685445622311376505 t^{11}$
\item[] $-2382710944926354080442398446589552744 t^{12}$
\begin{itemize}
\item[] $+326767340108407733203130499898126 t^{13}$
\begin{itemize}
\item[] $+276491632581630260746191363123 t^{14}$
\item[] $\left.-8431365198210579919006713 t^{15}\right) x^{4} y^{10}$
\end{itemize}
\end{itemize}
\end{itemize}
\end{itemize}
\item[] +12 (-8733106988589310312964985955814462819079774
\begin{itemize}
\item[] $+64016502559572741731505856556403573520814046 t$
\item[] $-144735875200699985710584864792377620711111027 t^{2}$
\item[] $+66707682241185015299381142924382044312819100 t^{3}$
\item[] $+73079504596828994404469155513764487920535332 t^{4}$
\item[] $-75764221368814908722894464652763782420369670 t^{5}$
\item[] $+18144429124108777614777763808360976174204563 t^{6}$
\item[] $+1935278311931502378271609920389021155764328 t^{7}$
\item[] $-842229927380965714885405569219684268010166 t^{8}$
\item[] $-43576284807293907660657241391770657495742 t^{9}$
\item[] $+12197493655076249609592887507484958732619 t^{10}$
\item[] $-1236906021392508491488029828633988502116 t^{11}$
\begin{itemize}
\item[] $+656542960338462752927669545849000176 t^{12}$
\end{itemize}
\end{itemize}
\end{itemize}
$-33306604264547610372382676649434 t^{13}$
$\left.-41617303783672454910317327355 t^{14}\right) x^{3}(1+x) y^{11}$
+2 (187554318014748213259275472412247634165779260
$-762602529289184570716467664651505597594612711 t$
$+781137281074558579579982041608982979326338521 t^{2}$
$+609916709974782293997005108542677011211842354 t^{3}$
$-1300509731487820027375772452301766352965003310 t^{4}$
$+495021556835245340779707559257082787835603199 t^{5}$
$+115214340026017185187174532535570472667840767 t^{6}$
$-93151202230256791649185399844658098150754584 t^{7}$
$+7202343146876999296118334182261935450026080 t^{8}$
$+1570014403002611359784317587694467895480399 t^{9}$
$+371422610102654444897802704145750294582991 t^{10}$
$-107776513895628817503345944747365689465454 t^{11}$
$+10941070332070115448154615812894796283346 t^{12}$
$-3005301616251624310474021462023025751 t^{13}$
$+41932897601387821985740913526761 t^{14}$
$\left.+87168052345572726428101766292 t^{15}\right) x^{3} y^{12}$
+6 (-49769698820686378083743112964571467299790844
$+144208424244836145109900273916270122534480379 t$
$-31061701177281181816778329394184658654578125 t^{2}$
$-316115877280896274823885457480018099381675270 t^{3}$
$+413355491574586200245516861333774692564805758 t^{4}$
$-189323246544195194714568800051070616915145871 t^{5}$
$+16358105769812410561563772201680559507177601 t^{6}$
$+10699064629034472787428641330738981639504716 t^{7}$
$-2410111354335748769859016926649172233001216 t^{8}$
$+411171528032730820725099829153187243925077 t^{9}$
$-226789949801107593485509158636442297272707 t^{10}$
\begin{itemize}
\item[] $+47843156588060602804351104035547186862994 t^{11}$
\item[] $-4050842729096500910242692387785686802242 t^{12}$
\begin{itemize}
\item[] $+503056665812777017090193080924335791 t^{13}$
\begin{itemize}
\item[] $-1358120473689033753999092690625 t^{14}$
\end{itemize}
\end{itemize}
\item[] $\left.-4470156530542191098877013656 t^{15}\right) x^{2}(1+x) y^{13}$
\item[] +6 (40840375974497844675523416705994772589613816
\item[] $-31065278771086485580585566101107070670979537 t$
\item[] $-256058709793754221748465779158452450846012816 t^{2}$
\item[] $+559068508134217391316137877579221486889948317 t^{3}$
\item[] $-405356674135473476033247305191846353227354396 t^{4}$
\item[] $+56661024338479719866449660305901198060970619 t^{5}$
\item[] $+64125926679095609696574105582575413252584004 t^{6}$
\item[] $-28890521413485617192612359619257982301215223 t^{7}$
\item[] $+2839341861289460260556040613235064311172368 t^{8}$
\item[] $+465313317652398071330581978147640308517821 t^{9}$
\item[] $-351597845897601623389761113030041346811064 t^{10}$
\item[] $+179321665024113431049966683538039741491991 t^{11}$
\item[] $-39080763389941286051140782872898013637420 t^{12}$
\item[] $+3329327789375495478533443619894892092425 t^{13}$
\begin{itemize}
\item[] $-149553232132910627041355116122361020 t^{14}$
\item[] $\left.+205192601853360299747062918515 t^{15}\right) x^{2} y^{14}$
\end{itemize}
\item[] +4 (-5628131126860710389875035169789649454420876
\item[] $-78804574894375995596657603789677394324984101 t$
\item[] $+352860279249727357643015437757245513637138672 t^{2}$
\item[] $-564941261129218367227412931528430799748606546 t^{3}$
\item[] $+430939089346630550106464017811753376858010640 t^{4}$
\item[] $-148284188482685309994113608598302973692022739 t^{5}$
\item[] $+4873973943047627527185771161170310871611116 t^{6}$
\item[] $+10181461701693419091610691800269773692583228 t^{7}$
\end{itemize}
\begin{itemize}
\begin{itemize}
\item[] $-1226684412907984419281022032089194096771900 t^{8}$
\item[] $-1114701349894370233505605371103641055314707 t^{9}$
\item[] $+706698148832598485833137372995728746006888 t^{10}$
\item[] $-230885597278675059768074093486733449982986 t^{11}$
\item[] $+40110760213781966306595755424591426952408 t^{12}$
\item[] $-2944406938738808019234484282441173992613 t^{13}$
\end{itemize}
\item[] $\left.+29909989810256194655311832623132956 t^{14}\right) x(1+x) y^{15}$
\item[] +3 (-19345311524103689299806429866595584344434933
\begin{itemize}
\item[] $+165880840018062517894524148661179410853072546 t$
\item[] $-433975351186661527899190510419861031681577223 t^{2}$
\item[] $+515516306674309051714096086492072331808918060 t^{3}$
\item[] $-283562876761607595979024343783955270990852289 t^{4}$
\item[] $+35089717870652037166528865782071242284918734 t^{5}$
\item[] $+33297928990127187049831304457387943687578909 t^{6}$
\item[] $-12917764244851664872827620472556082803226856 t^{7}$
\item[] $-266713623245328356955979252488258143292463 t^{8}$
\item[] $+555900198844440351814987030522263162652334 t^{9}$
\item[] $+344809125199575823496923125385565831315595 t^{10}$
\item[] $-325689072459807008457121908075371991483716 t^{11}$
\item[] $+117388439783020206894897144460070846332949 t^{12}$
\item[] $-21123688072686368568170196496753937437182 t^{13}$
\end{itemize}
\item[] $\left.+1569161588742434760282235480090100082255 t^{14}\right) x y^{16}$
\begin{itemize}
\item[] +3 (9783299760488948030219433006083570296689357
\item[] $-59321119347918543659930676521984384042169430 t$
\item[] $+141416477837529651726686264572772822193430055 t^{2}$
\item[] $-177096809878289456793903796377476455257673500 t^{3}$
\item[] $+127907586479651422318564410835908192786763365 t^{4}$
\item[] $-54372658309139640733439296021048049726746698 t^{5}$
\item[] $+13488394375983259178386269031077826541323679 t^{6}$
\end{itemize}
\end{itemize}
\begin{itemize}
\begin{itemize}
\item[] $-2113244794203694376441274534558687456380488 t^{7}$
\item[] $+141785257824097311610019381070069013792095 t^{8}$
\item[] $+316821091130460893567937727374441119017078 t^{9}$
\item[] $-305480360931755555721215775431316200256739 t^{10}$
\item[] $+142141070595224470100170760768533902542116 t^{11}$
\item[] $-38457837145846954116338584809621985652097 t^{12}$
\item[] $+5806436836462494743682658146129894324810 t^{13}$
\end{itemize}
\item[] $\left.-380650359326333515862984779019865187923 t^{14}\right)(1+x) y^{17}$
\begin{itemize}
\item[] + (-10524240525647109159259219575804205851284241
\item[] $+54473554541130948618895564303322618142908415 t$
\item[] $-116506041709060140591221129409148683447467665 t^{2}$
\item[] $+134582692171688928175407226575844795641654895 t^{3}$
\item[] $-91188532083602481766920967127844408926436405 t^{4}$
\item[] $+36353592052137018784330858422674753425698363 t^{5}$
\item[] $-7639385747972665348009342010125607135270845 t^{6}$
\begin{itemize}
\item[] $+93749989416978017153766638267237965058515 t^{7}$
\item[] $+613514003480165484061014972915970847589645 t^{8}$
\item[] $-277973572971202497026511206431230055671555 t^{9}$
\item[] $+4186799108745525715968930085758736947197 t^{10}$
\item[] $+68475809505229552273919737578535787115805 t^{11}$
\item[] $-41025357958210023316522198089867194215575 t^{12}$
\item[] $+12129433061687109251202289166065827342585 t^{13}$
\item[] $-1903251796631667579314923895099325939615 t^{14}$
\end{itemize}
\item[] $\left.+126883453108777838620994926339955062641 t^{15}\right) y^{18}$.
\end{itemize}
\end{itemize}

\section*{BIBLIOGRAPHY}
\begin{itemize}
\item[] [AgLak] R.P. Agarwal and V. Lakshmikantham, Uniqueness and Non-uniqueness Criteria for Ordinary Differential Equations, World Scientific (1993).
\item[] [Bat] H. Bateman and A. Erdelyi, Higher Transcendental Functions, Krieger Publishing, Florida (1981).
\item[] [Bir] J.S. Birman, Braids, Links, and Mapping Class Groups, Ann. Math. Stud. Princeton University (1975).
\item[] [Cox] H.S.M. Coxeter, Regular Polytopes, Macmillan Company New York (1963).
\item[] [Cro] W.J.R. Crosby, Problems and Solutions, Mounthly Amer. Math. (1946) 104-107.
\item[] [Dek] W. Dekkers, The Matrix of a Connection having Regular Singularities on a Vector Bundle of Rank 2 on $P^{1}(\mathbb{C})$, Springer Lect. Notes Math. 712 (1979) 33-43.
\item[] [Dub] B. Dubrovin, Geometry of 2D Topological Field Theories, Springer Lect. Notes Math. 1620, (1995) 120-348.
\item[] [FlN] H. Flashka and A.C. Newell, Monodromy and Spectrum Preserving Deformations, Comm. Math. Phys. 76 (1980) 67-116.
\item[] [Fuchs] R. Fuchs, Über Lineare Homogene Differentialgleichungen Zweiter Ordnung mit im drei im Endrichen Gelegene Wesentlich Singulären Stellen, Math. Ann. 63 (1907) 301-321.
\item[] [Gamb] B. Gambier, Sur les Equations Differentielles du Second Ordre et du Primier Degrè dont l'Integrale est a Points Critiques Fixes, Acta Math. 33, (1910) 1-55.
\item[] [Gar] R. Garnier, Sur des Equations Differentielles du Troisieme Ordre dont l'Integrale Generale est Uniforme et sur una Classe d'Equations nouvelles d'Ordre Superieur dont l'Integrale Generale a ses Points Critiques Fixes, Ann. Sci. Ecole Norm. Sup. 3 No. 29 (1912) 1-126.
\item[] [Gor] P. Gordan, Uber endliche Gruppen linearer Transformationen einer Veranderlichen, Math. Ann. 12, 1877, 23-46.
\item[] [Hit] N.J. Hitchin, Twistor Spaces, Einstein Metrics and Isomonodromic Deformations, J. Differential Geometry 42, No. 1 July 1995 30-112.
\item[] [Hit1] N.J. Hitchin, Poncelet Polygons and the Painlevé Transcendents, Geometry and Analysis, edited by Ramanan, Oxford University Press (1995) 151-185.
\item[] [Hit2] N.J. Hitchin, Talk at I.C.T.P. (Trieste) April 1993.
\item[] [IKSY] K. Iwasaki, H. Kimura, S. Shimomura, M. Yoshida, From Gauss to Painlevé, a Modern Theory for Special Functions, Chapter 4, Aspects of Mathematics, Vieweg (1991).
\item[] [Ince] E.L. Ince, Ordinary Differential Equations, Dover Publications, New York (1956).
\item[] [ItN] A.R. Its and V.Yu. Novokshenov, The Isomonodromic Deformation Method in the Theory of Painlevé Equations, Springer Lect. Notes Math. 1191 (1986).
\end{itemize}
\begin{itemize}
\item[] [Jim] M. Jimbo, Monodromy Problem and the Boundary Condition for some Painlevé Equations, Publ. RIMS 18 (1982), 1137-1161.
\item[] [JMU] M. Jimbo, T. Miwa and K. Ueno, Monodromy Preserving Deformation of the Linear Ordinary Differential Equations with Rational Coefficients I, II, Publ. RIMS 14 (1978) 223-267, 15 (1979) 201-278.
\item[] [Kit] A.V. Kitaev, Rational Solutions of the Fifth Painlevé Equation, Differential and Integral Equations 7 (1994) no.3-4, 967-1000.
\item[] [Kr] L. Kronecker, J. de Math. 19 (1854) 177-192.
\item[] [Lak] V. Lakshmikantham and S. Leela, Differential and Integral Inequalities, Academic Press New York (1969).
\item[] [Luka] N.A. Lukashevich, On the Theory of the Third Painlevé Equation, Differ. Uravn. 3 (1967) no.11, 1913-1923.
\item[] [Luke] L. Yu. Luke, Mathematical Functions and Their Approximations, Academic Press (1975).
\item[] [Mag] W. Magnus, Ring of Fricke Characters and Automorphism Groups of Free Groups, Math. Z. 170, (1980) 91-103.
\item[] [Mal] B. Malgrange, Sur les Deformations Isomonodromiques I, Singularités Régulières, Seminaire de l'Ecole Normale Superieure 1979-1982, Progress in Mathematics 37, Birkhäuser, Boston (1983) 401-426.
\item[] [Man] Yu.I. Manin, Sixth Painlevé Equation, Universal Elliptic Curve and Mirror of $\mathbf{P}^{2}$, preprint al-geom/9605010 (1996).
\item[] [Ma] M. Mazzocco, Picard and Chazy Solutions to PVI Equation, preprint 1998.
\item[] [Miwa] T. Miwa, Painlevé Property of Monodromy Preserving Deformation Equations and the Analyticity of $\tau$-function, Publ. RIMS, Kyoto Univ. 17 (1981) 703-721.
\item[] [Mur] Y. Murata, Classical Solutions of the Third Painlevé Equation, Nagoya Math. J. 139 (1995) 37-65.
\item[] [Mur1] Y. Murata, Rational Solutions of the Second and Fourth Painlevé equations, Funk. Ekvacioj 28, no. 1 (1995).
\item[] [Nor] N.E. Nörlund, The Logarithmic Solutions of the Hypergeometric equation, Mat. Fys. Skr. Dan. Vid. Selsk. 2, no. 5 (1963) 1-58.
\item[] [Ok] K. Okamoto, On the $\tau$-Function of the Painlevé Equations, Physica 2D (1981) 525-535.
\item[] [Ok1] K. Okamoto, Studies on the Painlevé Equations I, Sixth Painlevé Equation, Ann. Mat. Pura Appl. 148 (1987) 337-381.
\item[] [Ok2] K. Okamoto, Painlevé Equations and Dynkin Diagrams, Painlevé Transcendents, edited by D. Levi and P. Winternitz, Plenum Press, New York (1992) 299-313.
\end{itemize}
[Ok3] K. Okamoto, Sur les Feuilletages Associés aux Equation du Second Ordre à Points Critiques Fixes de Painlevé, Espaces des Conditions Initiales, Japan. J. Math. 5 (1979), 1-79.
[Pain] P. Painlevé, Sur les Equations Differentielles du Second Ordre et d'Ordre Superieur, dont l'Interable Generale est Uniforme, Acta Math. 25 (1902) 1-86.
[Pic] E. Picard, Mémoire sur la Théorie des Functions Algébriques de deux Varables, Journal de Liouville 5 (1889), 135-319.
[Seg] J. Segert, Frobenius Manifolds from Yang-Mills Instantons, preprint October (1997) dg-ga/9710031.
[SMJ] M. Sato, T. Miwa and M. Jimbo, Holonomic Quantum Fields II, Publ. RIMS 15 (1979) 201-278.
[Sch] L. Schlesinger, Über eine Klasse von Differentsial System Beliebliger Ordnung mit Festen Kritischer Punkten, J. fur Math. 141 (1912), 96-145.
[Schw] H.A. Schwartz, Über Diejenigen Fälle in Welchen die Gaussische Hypergeometrische Reihe einer Algebraische Funktion iheres vierten Elementes Darstellit, Crelle J. 75 (1873) 292-335.
[S1] S. Shimomura, Painlevé Transcendents in the Neighbourhood of a Fixed Singular Point, Funkcial. Ekvac. 25 (1982) 163-184.
[S2] S. Shimomura, Series Expansions for Painlevé Transcendents in the Neighbourhood of a Fixed Singular Point, Funkcial. Ekvac. 25 (1982) 185-197.
[S3] S. Shimomura, Supplement to "Series Expansions for Painlevé Transcendents in the Neighbourhood of a Fixed Singular Point", Funkcial. Ekvac. 25 (1982) 363-371.
[Sib] Y. Sibuya, Linear Differential Equations in the Complex Domain: Problems of Analytic Continuation, AMS TMM 82 (1990).
[Tod] K.P. Tod, Self-dual Einstein Metrics from the Painlevé VI Equation, Phys. Lett. A, 190 (1994) 221-224.
[Um] H. Umemura, Birational Automorphism Groups and Differential Equations, Nagoya Math. J., 119 (1990) 1-80.
[Um1] H. Umemura, Irreducebility of the First Differential Equation of Painlevé, Nagoya Math. J., 117 (1990) 231-252.
[Um2] H. Umemura, H. Watanabe, Solutions of the Second and Fourth Differential Equations of Painlevé, to appear in Nagoya Math. J., (1997).
[Um3] H. Umemura, H. Watanabe, Solutions of the Third Differential Equation of Painlevé, preprint (1997).
[Wat] H. Watanabe, Birational Canonical Transformations and Classical Solutions of the Sixth Painlevé Equation, preprint of the Kyushu University, Japan (1997).
[Wat1] H. Watanabe, Solutions of the Fifth Painlevé Equation I, Hokkaido Math. J. XXIV, 2 (1995) p. 53-89.
[Wey] H. Weyl, Algebraic Theory of Numbers, Ann. Math. Stud. 1, Princeton University Press (1940).
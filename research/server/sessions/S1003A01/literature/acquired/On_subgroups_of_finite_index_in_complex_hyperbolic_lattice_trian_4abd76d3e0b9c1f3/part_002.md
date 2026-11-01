---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: On subgroups of finite index in complex hyperbolic lattice triangle groups]

It is well known to experts that Livne's thesis [30] gives maps from some Mostow lattices to surface groups, which shows that some specific Mostow lattices are large. For a description of Livne's lattices in relation to Mostow's groups, see §16 in the book by Deligne and Mostow [8]. Recall that Livne constructs smooth ball quotients $X_{n}$ indexed by $n=5,6,7,8,9,10,12,18$, whose automorphism group $A$ fits is an extension
$$1 \rightarrow \mathbb{Z} / d \mathbb{Z} \rightarrow A \rightarrow S L(2, \mathbb{Z} / n \mathbb{Z}) \times(\mathbb{Z} / n \mathbb{Z})^{2} \rightarrow 1,$$
and the quotient $A \backslash X_{n}$ is $\Gamma_{\mu, \Sigma} \backslash \mathbb{H}_{\mathbb{C}}^{2}$, where $d=\operatorname{gcd}(6, n)$. The order of these automorphism groups gives the index of the corresponding subgroup of the relevant Mostow group; we list these in the last column of Table 8. For some Mostow groups, we will give subgroups

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline Mostow group & $n$ & $d$ & $|S L(2, n)|$ & Index \\
\hline $\Gamma\left(5, \frac{7}{10}\right)$ & 5 & 5 & 120 & 15000 \\
\hline $\Gamma\left(6, \frac{2}{3}\right)$ & 6 & 1 & 144 & 5184 \\
\hline $\Gamma\left(7, \frac{9}{14}\right)$ & 7 & 7 & 336 & 115248 \\
\hline $\Gamma\left(8, \frac{5}{8}\right)$ & 8 & 4 & 384 & 98304 \\
\hline $\Gamma\left(9, \frac{11}{18}\right)$ & 9 & 3 & 648 & 157464 \\
\hline $\Gamma\left(10, \frac{3}{5}\right)$ & 10 & 5 & 720 & 360000 \\
\hline $\Gamma\left(12, \frac{7}{12}\right)$ & 12 & 2 & 1152 & 331776 \\
\hline $\Gamma\left(18, \frac{5}{9}\right)$ & 18 & 3 & 3888 & 3779136 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 8. Index of torsion-free subgroups coming from Livne's construction}
\end{table}
of much smaller index that map onto a non-Abelian free group, see Proposition 7.1 and Table 10.

Note that the maps from Livne groups to Fuchsian groups are actually induced by holomorphic fibrations of the corresponding ball quotients over suitable Riemann surfaces (actually $X_{n}$ fibers over the quotient of the upper half plane under the principal congruence subgroup modulo $n$, see [8]). The maps we construct are also induced by holomorphic maps to curves, as can be seen from their interpretation as forgetful maps of moduli spaces of points on $\mathbb{P}_{\mathbb{C}}^{1}$, see [12].

Rather than going into the details of Deligne-Mostow theory and forgetful maps, we give a more down to earth approach that requires only group theory.

Proposition 7.1. The Mostow groups $\Gamma(7,9 / 14), \Gamma(8,5 / 8), \Gamma(9,11 / 18), \Gamma(10,3 / 5), \Gamma(12,7 / 12)$, $\Gamma(18,5 / 9), \Gamma(7,13 / 42), \Gamma(8,7 / 24), \Gamma(9,5 / 18), \Gamma(10,4 / 15), \Gamma(12,1 / 4), \Gamma(18,2 / 9), \Gamma(6,1 / 6)$, $\Gamma(8,1 / 8), \Gamma(12,1 / 12), \Gamma(4,3 / 20), \Gamma(10,0), \Gamma(4,1 / 12), \Gamma(6,0), \Gamma(4,0)$ have a surjective homomorphism onto a lattice in $P S L(2, \mathbb{R})$.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|}
\hline $p$ & 7 & 8 & 9 & 10 & 12 & 18 \\
\hline Index & 84 & 48 & 36 & 30 & 24 & 18 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 9. Optimal index of torsion-free subgroups in the triangle group $T_{2,3, p}$.}
\end{table}

The basis of the construction of these homorphisms is simply to combine Mostow's braid group description of the lattices $\Gamma(p, t)$ with the results in [12] about forgetful maps of Deligne-Mostow moduli spaces.

We briefly sketch how this is done; the reader without any knowledge of Deligne-Mostow theory can skip this part. Each group $\Gamma(p, t)=\left\langle R_{1}, J\right\rangle$ is conjugate in $P U(2,1)$ to a specific Deligne-Mostow group from [7], [34], namely $\Gamma_{\mu, \Sigma}$ where
$$\mu=\left(\frac{1}{2}-\frac{1}{p}, \frac{1}{2}-\frac{1}{p}, \frac{1}{2}-\frac{1}{p}, \frac{1}{4}+\frac{3}{2 p}-\frac{t}{2}, \frac{1}{4}+\frac{3}{2 p}+\frac{t}{2}\right)$$
and $\Sigma=S_{3}$ permutes the first three weights.
If $\mu$ satisfies the Deligne-Mostow INT condition, then the corresponding Deligne-Mostow group $\Gamma_{\mu}$ is contained in $\Gamma_{\mu, \Sigma}$ as a subgroups of index $|\Sigma|=3!=6$. Mostow explains in [35] how to write explicit generators for $\Gamma_{\mu}$, namely $A_{j}, B_{j}, j=1,2,3$ with
$$B_{j}=R_{j}^{2}, \quad A_{j}^{-1}=J^{-1} R_{j} R_{j+1} .$$
Recall that $R_{j+1}=J R_{j} J^{-1}$ index $j$ taken mod $3\left(J^{3}=I d\right)$. From this information, it is easy to ask Magma for a presentation for each $\Gamma_{\mu}$.

Note also that when $\mu$ satisfies Mostow's $\Sigma$-INT condition for $\Sigma=S_{3}$ but not the INT condition, we have $\Gamma_{\mu}=\Gamma_{\mu, \Sigma}$, see [38] for instance.

Recall the presentation for $\Gamma(p, t)$ given in Appendix A. 9 of[14], namely
$$\begin{gathered}
\Gamma(p, t)=\left\langle R_{1}, R_{2}, R_{3}, J\right| R_{1}^{p}, J^{3},\left(R_{1} J\right)^{2 k}, J R_{1} J^{-1}=R_{2}, J R_{2} J^{-1}=R_{3} \\
\left.\operatorname{br}_{3}\left(R_{1}, R_{2}\right),\left(R_{1} R_{2}\right)^{\frac{6 p}{p-6}},\left(J R_{2} R_{1}\right)^{\frac{4 k p}{(2 k-4) p-4 k}}\right\rangle
\end{gathered}$$
where the last two relations are omitted when the corresponding exponent is negative.
We wish to construct a homomorphism of $\Gamma(p, t)$ onto the $(2,3, p)$ triangle group
$$T_{2,3, p}=\left\langle\beta, \gamma \mid(\beta \gamma)^{2}, \beta^{3}, \gamma^{p}\right\rangle .$$
For convenience, recall that the optimal index of a torsion-free subgroup in the hyperbolic triangle groups are as in Table 9 (cf. [17]).

Proposition 7.2. Suppose $p>6$ and $\Gamma(p, t)$ satisfies the Mostow $\Sigma$-INT condition. Then there is a unique group homomorphism $\varphi: \Gamma(p, t) \rightarrow T_{2,3, p}$ such that $\varphi(J)=\beta$ and $\varphi\left(R_{1}\right)=\gamma$.

Proof: If the map exists, then we must have $\varphi\left(R_{2}\right)=\beta \gamma \beta^{-1}$ and $\varphi\left(R_{3}\right)=\beta^{-1} \gamma \beta$. We then check that, under the hypotheses of Proposition 7.2, for every relator $w_{1} \ldots w_{n}$ in the presentation of $\Gamma(p, t)$, the relation $\varphi\left(w_{1}\right) \ldots \varphi\left(w_{n}\right)=i d$ holds in $T_{2,3, p}$ (in that case, we say that the relation is compatible).

For example, $\varphi\left(R_{1}\right) \varphi\left(R_{2}\right) \varphi\left(R_{1}\right)=\gamma \beta \gamma \beta^{-1} \gamma=\beta^{-2} \gamma=\beta \gamma$, and $\varphi\left(R_{2}\right) \varphi\left(R_{1}\right) \varphi\left(R_{2}\right)=$ $\beta \gamma \beta^{-1} \gamma \beta \gamma \beta^{-1}=\beta \gamma \beta^{2} \gamma \beta \gamma \beta^{2}=\gamma^{-1} \beta^{-1}=\beta \gamma$, so the braid relation $R_{1} R_{2} R_{1}\left(R_{2} R_{1} R_{2}\right)^{-1}$ is compatible.

For the other relations, one checks that $\varphi\left(R_{1}\right) \varphi\left(R_{2}\right)=\beta$ and $\varphi\left(R_{1}\right) \varphi\left(R_{2}\right) \varphi(J)=\gamma^{-2}$. It is then easy to verify that for the relevant values of $k=2,3,4$ and $5,6 p /(p-6)$ is a multiple of 3 and $4 k p /((k-2) p-2 k)$ is a multiple of $p$. \(\square\)

Proposition 7.2 implies Proposition 7.1 for the Mostow groups $\Gamma\left(7, \frac{9}{14}\right), \Gamma\left(8, \frac{5}{8}\right), \Gamma\left(9, \frac{11}{18}\right)$, $\Gamma\left(10, \frac{3}{5}\right), \Gamma\left(12, \frac{7}{12}\right), \Gamma\left(18, \frac{5}{9}\right), \Gamma\left(7, \frac{13}{42}\right), \Gamma\left(8, \frac{7}{24}\right), \Gamma\left(9, \frac{5}{18}\right), \Gamma\left(10, \frac{4}{15}\right), \Gamma\left(12, \frac{1}{4}\right), \Gamma\left(18, \frac{12}{9}\right), \Gamma\left(8, \frac{1}{8}\right)$, $\Gamma\left(12, \frac{1}{12}\right), \Gamma(10,0)$. Note that the first 6 groups in this list are Livne lattices; one can check that the corresponding maps are the same as the ones that come from the Livné construction (the construction is conveniently reviewed in [8], §16).

For the other cases of Proposition 7.1, we use $\Gamma_{\mu}$ instead of $\Gamma_{\mu, \Sigma}$. We define two kinds of subgroups of $\Gamma_{\mu}$, namely
$$K=\left\langle\left\langle A_{1}, A_{2}, A_{3}\right\rangle\right\rangle, \quad L=\left\langle\left\langle A_{1}, B_{2}, B_{3}\right\rangle\right\rangle,$$
see the notation in equation (10).
We then use group theory software to compute a simplified presentation for $\Gamma_{\mu} / K$ and $\Gamma_{\mu} / L$, and find that in each of the cases listed in Proposition 7.1, the corresponding quotient is a $p, q, r$ triangle group.

The details are listed in Table 10. In the last column of the table, we list the index of the subgroups we obtain that map to a non-Abelian free group. The factor 6 comes from the index of $\Gamma_{\mu}$ in $\Gamma_{\mu, \Sigma}$, the other factor comes from the minimal index of a torsion-free subgroup in a Fuchsian group [17].

Recall that when $1 / p+1 / q+1 / r$, the $(p, q, r)$ is a lattice in $P S L(2, \mathbb{R})$, and this is satisfied for at least one triple $(p, q, r)$ of each row of table 10, so the proof of Proposition 7.1 is complete.

Now Lemma 7.1 implies the following.
Theorem 7.3. Let $\Gamma$ be one of the Mostow lattices listed in Proposition 7.1. Then $\Gamma$ is large.

Note also that our proof give a way to describe explicit subgroups, and explicit morphisms to $F_{2}$.
7.3. Neat subgroups. We summarize the results of our search for neat subgroups of small index in Tables 11 through 72. In these tables, for each triangle group, we give
\begin{itemize}
\item[-] The Euler characteristic and the least common multiple (LCM) of the orders of isotropy groups; this gives a lower bound for the index of torsion-free subgroups. Note that by Noether's formula (see section 3), compact ball quotients have Euler characteristic an integer multiple of 3. In some cases, this yields a slightly higher lower bound (given by 3‧LCM);
\item[-] The arithmeticity (A/NA) and cocompactness (C/NC) of the group;
\item[-] Its Abelianization;
\end{itemize}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline $\Gamma(p, t)$ & Cocompact, Arithmetic? & $\Gamma_{\mu} / K$ & $\Gamma_{\mu} / L$ & Index \\
\hline $\Gamma(8,5 / 8)$ & C,A & 4,4,4 & 2,2,4 & $6 \cdot 8=48$ \\
\hline $\Gamma(10,3 / 5)$ & C,A & 5,5,5 & 2,2,5 & $6 \cdot 5=30$ \\
\hline $\Gamma(12,7 / 12)$ & C,A & 6,6,6 & 2,2,2 & $6 \cdot 12=72$ \\
\hline $\Gamma(18,5 / 9)$ & C,A & 9,9,9 & 2,2,3 & $6 \cdot 9=54$ \\
\hline $\Gamma(8,7 / 24)$ & C,NA & 4,4,4 & 3,3,4 & $6 \cdot 8=48$ \\
\hline $\Gamma(10,4 / 15)$ & C,NA & 5,5,5 & 3,3,5 & $6 \cdot 5=30$ \\
\hline $\Gamma(12,1 / 4)$ & C,A & 6,6,6 & 2,3,3 & $6 \cdot 12=72$ \\
\hline $\Gamma(18,2 / 9)$ & C,A & 9,9,9 & 3,3,3 & $6 \cdot 3=18$ \\
\hline $\Gamma(6,1 / 6)$ & NC,NA & 3,3,3 & 3,4,4 & $6 \cdot 3=18$ \\
\hline $\Gamma(8,1 / 8)$ & C,A & 4,4,4 & 4,4,4 & $6 \cdot 12=72$ \\
\hline $\Gamma(12,1 / 12)$ & C,A & 6,6,6 & 2,2,2 & $6 \cdot 12=72$ \\
\hline $\Gamma(4,3 / 20)$ & C,A & 2,2,2 & 2,5,5 & $6 \cdot 20=120$ \\
\hline $\Gamma(10,0)$ & C,A & 5,5,5 & 5,5,5 & $6 \cdot 5=30$ \\
\hline $\Gamma(4,1 / 12)$ & C,NA & 2,2,2 & 2,6,6 & $6 \cdot 12=72$ \\
\hline $\Gamma(6,0)$ & NC,A & 3,3,3 & 3,6,6 & $6 \cdot 3=18$ \\
\hline $\Gamma(4,0)$ & C,A & 2,2,2 & 2,8,8 & $6 \cdot 8=48$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 10. List of maps to triangle groups; in the last column, we list the index of the subgroups we find that map to a non-Abelian free group.}
\end{table}
\begin{itemize}
\item[-] Generators for (representatives of) its cusps (inside one given box corresponding to the description of the cusps, each line corresponds to different conjugacy classes of cusps).
\item[-] The order of the smallest congruence image such that the corresponding principal congruence subgroup is torsion-free (we also an explicit description of the congruence image group, if we know one). In some cases, the congruence image seems too large to compute anything about it, in which case we simply write "?" in the corresponding box of the table. In the last column, we list the rational prime whose prime ideal factor was used to get a torsion-free congruence subgroup (in some rare cases, one can get a smaller congruence by reduction modulo a non-prime ideal).
\item[-] If we found any neat subgroup with index smaller than the order of the congruence image, we list some basic invariants for the corresponding subgroups (index, index of the normal core, quotient by the normal core, abelianization, self-intersections of the elliptic curves in the toroidal compactification, first Betti number).
\end{itemize}

Remark 7.4. (1) When the Congruence image column of the following tables contains a question mark "?", we mean that the corresponding finite group seems too large to compute anything. We suspect that one could probably work a little more and compute the order of these groups and identify them as explicit projectivized
\begin{itemize}
\item[] linear groups over finite fields, but it is probably hopeless to try and compute anything about the corresponding principal congruence subgroups (presentation, Abelianization).
\item[(2)] In Tables 11 through 72, we write $\mathbb{Z}_{n}$ for $\mathbb{Z} / n \mathbb{Z}$, and $P U(m, n)$ denotes $P U\left(m, \mathbb{F}_{n}\right)$, $P G L(m, n)$ denotes $P G L\left(m, \mathbb{F}_{n}\right)$ where $F_{n}$ is the field with $n$ elements ( $n$ is a power of a single prime).

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|}
\hline \multicolumn{9}{|c|}{$\mathcal{S}\left(3, \sigma_{1}\right)$} \\
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & \multicolumn{2}{|c|}{Congr. image (mod 5)} \\
\hline $\frac{2}{9}$ & 72 & NA & NC & $\mathbb{Z}_{3}$ & $R_{1}, R_{2}$ & $\operatorname{br}_{6}\left(R_{1}, R_{2}\right)$ & \multicolumn{2}{|c|}{378000, $\operatorname{PGU}(3,5)$} \\
\hline \multicolumn{2}{|l|}{Index} & \multicolumn{3}{|r|}{Core Index} & \multicolumn{2}{|c|}{Quotient} & Ab & Self-int \\
\hline \multicolumn{2}{|r|}{$432=6 \cdot 72$} & \multicolumn{2}{|r|}{16868} & \multicolumn{2}{|c|}{$\mathbb{Z}_{3} \times \operatorname{PGL}(3,3)$} & $\mathbb{Z}_{3} \oplus \mathbb{Z}_{6} \oplus \mathbb{Z}_{18}$ & $(-3)^{6},(-9)^{14}$ & 0 \\
\hline \multicolumn{2}{|c|}{$864=12 \cdot 72$} & \multicolumn{2}{|r|}{18144} & \multicolumn{2}{|c|}{$\mathbb{Z}_{3} \times \operatorname{PSU}(3,3)$} & $\mathbb{Z}_{2}^{2} \oplus \mathbb{Z}^{2}$ & $(-2)^{36}$ & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 11. Neat subgroups of $\mathcal{S}\left(3, \sigma_{1}\right)$ with core index $\leq 20000$}
\end{table}
$\mathcal{S}\left(4, \sigma_{1}\right)$

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{7}{16}$ & 96 & NA & NC & $\mathbb{Z}_{4}$ & 1,232 & $\mathrm{br}_{4}(1,23 \overline{2})$ & $42456960, \operatorname{PGL}(3,9)$ \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 96 & 96 & & $\mathbb{Z}_{2}^{2} \oplus \mathbb{Z}_{4}^{3} \oplus \mathbb{Z}^{4}$ & $(-8)^{24}$ & 4 \\
\hline 96 & 384 & & $\mathbb{Z}_{2}^{5} \oplus \mathbb{Z}_{8}^{2}$ & $(-8)^{6}$ & 0 \\
\hline 96 & 384 & & $\mathbb{Z}_{2}^{5} \oplus \mathbb{Z}_{4}^{3}$ & $(-4)^{12}$ & 0 \\
\hline 96 & 384 & & $\mathbb{Z}_{2}^{2} \oplus \mathbb{Z}_{4}^{3} \oplus \mathbb{Z}_{8}^{2}$ & $(-4)^{12}$ & 0 \\
\hline 96 & 384 & & $\mathbb{Z}_{2}^{5} \oplus \mathbb{Z}_{4}^{2} \oplus \mathbb{Z}_{8}^{2}$ & $(-2)^{8},(-4)^{8}$ & 0 \\
\hline 96 & 384 & & $\mathbb{Z}_{2}^{3} \oplus \mathbb{Z}_{4}^{3} \oplus \mathbb{Z}^{2}$ & $(-2)^{8},(-4)^{8}$ & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 12. Neat subgroups of $\mathcal{S}\left(3, \sigma_{1}\right)$ with core index $\leq 384$}
\end{table}
\end{itemize}

\section*{References}
\begin{itemize}
\item[] [1] Roger C. Alperin. An elementary account of Selberg's lemma. Enseign. Math. (2), 33:269-273, 1987.
\item[] [2] Avner Ash, David Mumford, Michael Rapoport, and Yung-Sheng Tai. Smooth compactifications of locally symmetric varieties. Cambridge: Cambridge University Press, 2010.
\item[] [3] Gottfried Barthel, Friedrich Hirzebruch, and Thomas Höfer. Geradenkonfigurationen und algebraische Flächen, volume D4 of Aspects Math. Springer, Wiesbaden, 1987.
\item[] [4] Armand Borel. Introduction aux groupes arithmétiques. Paris: Hermann \& Cie, 1969.
\item[] [5] J. O. Button. Proving finitely presented groups are large by computer. Exp. Math., 20(2):153-168, 2011.
\end{itemize}
$$\mathcal{S}\left(6, \sigma_{1}\right)$$

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{43}{72}$ & 72 & NA & NC & $\mathbb{Z}_{6}$ & 1,23232 & $\mathrm{br}_{3}(1,232 \overline{3} \overline{2})$ & 378000, PGU(3, 5) \\
\hline & & & & & 1, $\overline{3} 2323$ & $\mathrm{br}_{3}(1, \overline{3} \overline{2} 323)$ & \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $1728=24 \cdot 72$ & 36288 & $P S U(3,3) \times \mathbb{Z}_{3}$ & $\mathbb{Z}_{2}^{3} \oplus \mathbb{Z}_{4} \oplus \mathbb{Z}^{4}$ & $(-2)^{72}$ & 4 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 13. Neat subgroups of $\mathcal{S}\left(6, \sigma_{1}\right)$.}
\end{table}
$$\mathcal{S}\left(3, \bar{\sigma}_{n}\right)$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{2}{63}$ & 504 & A & C & $\mathbb{Z}_{3}$ & & & $378000, P G U(3,5)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 14. Neat subgroups of $\mathcal{S}\left(3, \bar{\sigma}_{4}\right)$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $6048=12 \cdot 504$ & 18144 & $P S U(3,3) \times \mathbb{Z}_{3}$ & $\mathbb{Z}^{10}$ & & 10 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 14. Neat subgroups of $\mathcal{S}\left(3, \bar{\sigma}_{4}\right)$.}
\end{table}
$$\mathcal{S}\left(4, \bar{\sigma}_{n}\right)$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{25}{224}$ & 672 & NA & NC & \{0\} & $R_{1}, R_{2}$ & $\operatorname{br}_{4}\left(R_{1}, R_{2}\right)$ & 6048, PGU $(3,3)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 15. Neat subgroups of $\mathcal{S}\left(3, \bar{\sigma}_{4}\right)$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $6048=9 \cdot 672$ & 6048 & $P S U(3,3)$ & $\mathbb{Z}_{3}^{8}$ & $(-6)^{56}$ & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 16. Invariants for $\mathcal{S}\left(5, \bar{\sigma}_{4}\right)$}
\end{table}
$$\mathcal{S}\left(5, \bar{\sigma}_{n}\right)$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{47}{280}$ & 4200 & NA & C & \{0\} & & & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 16. Invariants for $\mathcal{S}\left(5, \bar{\sigma}_{4}\right)$}
\end{table}
$$\mathcal{S}\left(6, \bar{\sigma}_{0}\right)$$

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{25}{126}$ & 252 & NA & NC & $\mathbb{Z}_{3}$ & 1,232 & $\mathrm{br}_{3}(1,23 \overline{2})$ & 378000, PGU(3, 5) \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $3024=12 \cdot 252$ & 378000 & PGU(3, 5) & $\mathbb{Z}_{5}^{3}$ & $(-1)^{4},(-5)^{4}$ & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 17. Torsion-free subgroups of $\mathcal{S}\left(6, \bar{\sigma}_{4}\right)$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|}
\hline \multicolumn{10}{|c|}{$\mathcal{S}\left(8, \bar{\sigma}_{4}\right)$} \\
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & \multicolumn{3}{|l|}{Congr. image (mod 3)} \\
\hline $\frac{99}{448}$ & 1344 & NA & C & \{0\} & & & \multicolumn{3}{|l|}{$42456960, \operatorname{PGL}(3,9)$} \\
\hline \multirow{2}{*}{} & \multicolumn{4}{|c|}{Index} & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline & \multicolumn{4}{|c|}{$131712=98 \cdot 1344$} & 5663616 & PGU(3, 7) & ? & & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 18. Torsion-free subgroups of $\mathcal{S}\left(8, \bar{\sigma}_{4}\right)$.}
\end{table}
$$\mathcal{S}\left(12, \bar{\sigma}_{4}\right)$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & \multicolumn{3}{|l|}{Congr. image (mod 5)} \\
\hline $\frac{221}{1008}$ & 1008 & NA & C & $\mathbb{Z}_{3}$ & & & \multicolumn{3}{|c|}{?} \\
\hline \multirow{2}{*}{} & \multicolumn{3}{|c|}{Index} & \multicolumn{2}{|c|}{Core Index} & Quotient & Ab & Self-int & $b_{1}$ \\
\hline & \multicolumn{3}{|c|}{$6048=6 \cdot 1008$} & \multicolumn{2}{|c|}{18144} & $P G U(3,3) \times \mathbb{Z}_{3}$ & $\mathbb{Z}_{3}^{4}$ & & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 19. Torsion-free subgroups of $\mathcal{S}\left(12, \bar{\sigma}_{4}\right)$ with core index $\leq 20000$.}
\end{table}
$$\mathcal{S}\left(2, \sigma_{5}\right)$$

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{45}$ & 360 & A & C & $\mathbb{Z}_{6}$ & & & $378000, P G U(3,5)$ \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $54,000=50 \cdot 1080$ & 378000 & PGU(3, 5) & $\mathbb{Z}_{2}^{10} \oplus \mathbb{Z}_{10} \oplus \mathbb{Z}_{70}$ & & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 20. Torsion-free subgroups of $\mathcal{S}\left(2, \sigma_{5}\right)$}
\end{table}
$$\mathcal{S}\left(3, \sigma_{5}\right)$$

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{49}{180}$ & 360 & NA & NC & $\mathbb{Z}_{3}^{2}$ & $c_{1}=2, c_{2}=2(\bar{J} 1)^{2} 121 \overline{2} \overline{1}(\bar{J} \overline{1})^{3} 2$ & $c_{1}^{3}, c_{2}^{6}, \mathrm{br}_{4}\left(c_{1}, c_{2}\right)$ & 378000, PGU(3, 5) \\
\hline
\end{tabular}

\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 360 & 360 & & $\mathbb{Z}_{3} \oplus \mathbb{Z}^{8}$ & $(-1)^{20}$ & 8 \\
\hline 360 & 360 & & $\mathbb{Z}_{3}^{9}$ & $(-1)^{20}$ & 0 \\
\hline 360 & 1080 & & $\mathbb{Z}_{3}^{2} \oplus \mathbb{Z}^{6}$ & $(-1)^{20}$ & 6 \\
\hline
\end{tabular}

Table 21. Neat subgroups of $\mathcal{S}\left(3, \sigma_{5}\right)$ with core index $\leq 10,000$
$$\mathcal{S}\left(4, \sigma_{5}\right)$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{17}{36}$ & 720 & NA & NC & $\mathbb{Z}_{6}$ & $R_{1}, R_{2}$ & $\operatorname{br}_{4}\left(R_{1}, R_{2}\right)$ & $152334000000, P G L(3,25)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 22. Invariants for $\mathcal{S}\left(4, \sigma_{5}\right)$}
\end{table}
$$\mathcal{S}\left(3, \sigma_{10}\right)$$

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{45}$ & 360 & A & C & $\mathbb{Z}_{3}$ & & & $378000, P G U(3,5)$ \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $2160=2 \cdot 1080$ & 2160 & & $\mathbb{Z}^{16}$ & & 16 \\
\hline $2160=2 \cdot 1080$ & 34560 & & $\mathbb{Z}_{2}^{8} \oplus \mathbb{Z}_{8}$ & & 0 \\
\hline $2160=2 \cdot 1080$ & 34560 & & $\mathbb{Z}_{2}^{2} \oplus \mathbb{Z}_{4}^{2} \oplus \mathbb{Z}_{16}$ & & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 23. Neat subgroups of $\mathcal{S}\left(3, \sigma_{10}\right)$ with core index $\leq 40,000$}
\end{table}
$$\mathcal{S}\left(4, \sigma_{10}\right)$$

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{3}{32}$ & 480 & A & C & \{1\} & & & $42456960, P G L(3,9)$ \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $12,000=25 \cdot 480$ & 372, 000 & $P G L(3,5)$ & $\mathbb{Z}_{5} \oplus \mathbb{Z}_{155}$ & & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 24. Neat subgroups of $\mathcal{S}\left(4, \sigma_{10}\right)$}
\end{table}
$$\mathcal{S}\left(5, \sigma_{10}\right)$$

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{1}{8}$ & 600 & A & C & $\mathbb{Z}_{5}$ & & & $42573600, P G U(3,9)$ \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 600 & 600 & & $\mathbb{Z}^{20}$ & & 20 \\
\hline 600 & 15000 & & $\mathbb{Z}_{5}^{7}$ & & 0 \\
\hline 600 & 15000 & & $\mathbb{Z}_{5} \oplus \mathbb{Z}^{8}$ & & 8 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 25. Neat subgroups of $\mathcal{S}\left(5, \sigma_{10}\right)$ with core index $\leq 20,000$}
\end{table}
$$\mathcal{S}\left(10, \sigma_{10}\right)$$

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{13}{100}$ & 300 & A & C & $\mathbb{Z}_{5}$ & & & $42573600, P G U(3,9)$ \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 300 & 18,000 & & $\mathbb{Z}_{5}^{2} \oplus \mathbb{Z}_{15}$ & & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 26. Neat subgroups of $\mathcal{S}\left(10, \sigma_{10}\right)$ with core index $\leq 20,000$}
\end{table}
\begin{itemize}
\item[] [6] Donald I. Cartwright and Tim Steger. Enumeration of the 50 fake projective planes. C. R., Math., Acad. Sci. Paris, 348(1-2):11-13, 2010.
\end{itemize}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|l|l|l|}
\hline \multicolumn{13}{|c|}{$\mathcal{T}\left(3, \mathbf{S}_{2}\right)$} \\
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & \multicolumn{3}{|c|}{Cusp relations} & \multicolumn{4}{|l|}{Congr. image (mod 5)} \\
\hline $\frac{2}{15}$ & 360 & A & C & $\mathbb{Z}_{3}$ & & & \multicolumn{2}{|c|}{} & \multicolumn{4}{|c|}{$378000, P G U(3,5)$} \\
\hline \multicolumn{2}{|c|}{\multirow{2}{*}{}} & \multicolumn{2}{|c|}{Index} & \multicolumn{2}{|c|}{Core Index} & Quotient & \multicolumn{2}{|c|}{Ab} & Self-int & \multicolumn{2}{|c|}{$b_{1}$} & \multirow{2}{*}{} \\
\hline & & \multicolumn{2}{|c|}{360} & \multicolumn{2}{|c|}{360} & & $\mathbb{Z}^{16}$ & & & \multicolumn{2}{|c|}{16} & \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 27. Neat subgroups of $\mathcal{T}\left(3, \mathbf{S}_{2}\right)$ with core index $\leq 2,000$}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|}
\hline \multicolumn{10}{|c|}{$\mathcal{T}\left(4, \mathbf{S}_{2}\right)$} \\
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & \multicolumn{3}{|c|}{Congr. image (mod 5)} \\
\hline $\frac{1}{3}$ & 480 & NA & NC & \{1\} & $R_{1}, R_{2}$ & $\operatorname{br}_{4}\left(R_{1}, R_{2}\right)$ & \multicolumn{3}{|c|}{$42456960, P G L(3,9)$} \\
\hline & \multicolumn{4}{|c|}{Index} & \multicolumn{2}{|l|}{Core Index} & Quotient & Ab & Self-int \\
\hline & \multicolumn{4}{|r|}{$155,520=324 \cdot 480$} & \multicolumn{2}{|c|}{42456960} & & ? & \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 28. Neat subgroups of $\mathcal{T}\left(4, \mathbf{S}_{2}\right)$}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline \multicolumn{8}{|c|}{$\mathcal{T}\left(5, \mathbf{S}_{2}\right)$} \\
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{133}{300}$ & 600 & NA & C & $\mathbb{Z}_{5}$ & & & 23619600 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 29. Neat subgroups of $\mathcal{T}\left(5, \mathbf{S}_{2}\right)$}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $3600=2 \cdot 1800$ & 3600 & & $\mathbb{Z}_{3}^{8}$ & & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 29. Neat subgroups of $\mathcal{T}\left(5, \mathbf{S}_{2}\right)$}
\end{table}

\section*{$\mathcal{T}\left(3, \mathbf{E}_{2}\right)$}

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{4}$ & 72 & A & NC & $\mathbb{Z}_{3}^{2}$ & $c_{1}=2, c_{2}=(\overline{3} \overline{2} \overline{1})^{2} \overline{2} \overline{1} 2$ & $c_{1}^{3}, c_{2}^{6}\left(c_{1} c_{2}\right)^{-4},\left(c_{1} c_{2}\right)^{2}$ central & 378000, PGU(3, 5) \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 72 & 72 & & $\mathbb{Z}^{8}$ & $(-1)^{12}$ & 8 \\
\hline 72 & 648 & & $\mathbb{Z}_{3}^{2} \oplus \mathbb{Z}^{4}$ & $(-1)^{3},(-3)^{3}$ & 4 \\
\hline 72 & 648 & & $\mathbb{Z}_{3}^{3} \oplus \mathbb{Z}^{2}$ & $(-3)^{4}$ & 2 \\
\hline 72 & 648 & & $\mathbb{Z}_{3}^{4} \oplus \mathbb{Z}^{2}$ & $(-1)^{3},(-3)^{3}$ & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 30. Neat subgroups of $\mathcal{T}\left(3, \mathbf{E}_{2}\right)$ of core index $\leq 1000$}
\end{table}
\begin{itemize}
\item[] [7] P. Deligne and G. D. Mostow. Monodromy of hypergeometric functions and non-lattice integral monodromy. Publ. Math., Inst. Hautes Étud. Sci., 63:5-89, 1986.
\item[] [8] Pierre Deligne and George Daniel Mostow. Commensurabilities among lattices in $P U(1, n)$, volume 132 of Ann. Math. Stud. Princeton, NJ: Princeton University Press, 1993.
\end{itemize}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|}
\hline \multicolumn{9}{|c|}{$\mathcal{T}\left(4, \mathbf{E}_{2}\right)$} \\
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & \multicolumn{2}{|c|}{Cusp relations} & Congr. image (mod 5) \\
\hline $\frac{17}{32}$ & 96 & NA & NC & $\mathbb{Z}_{2} \oplus \mathbb{Z}_{4}$ & $$\begin{gathered}
R_{1}, R_{2} \\
R_{1}, R_{3} \\
R_{1}, R_{2} R_{3} R_{2}^{-1}
\end{gathered}$$ & \multicolumn{2}{|c|}{$$\begin{gathered}
\operatorname{br}_{4}\left(R_{1}, R_{2}\right) \\
\operatorname{br}_{4}\left(R_{1}, R_{3}\right) \\
\operatorname{br}_{4}\left(R_{1}, R_{2} R_{3} R_{2}^{-1}\right)
\end{gathered}$$} & $50778000000, P S L(3,25)$ \\
\hline \multicolumn{2}{|c|}{\multirow{4}{*}{}} & Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ & \multirow{4}{*}{} \\
\hline & & 96 & 192 & & $\mathbb{Z}_{2}^{4} \oplus \mathbb{Z}_{4}^{2} \oplus \mathbb{Z}^{4}$ & $(-2)^{18}$ & 4 & \\
\hline & & 96 & 768 & & $\mathbb{Z}_{2}^{4} \oplus \mathbb{Z}_{4}^{2} \oplus \mathbb{Z}^{4}$ & $(-2)^{10},(-4)^{4}$ & 4 & \\
\hline & & 96 & 768 & & $\mathbb{Z}_{2}^{6} \oplus \mathbb{Z}_{4}^{3} \oplus \mathbb{Z}_{8}$ & $(-2)^{10},(-4)^{4}$ & 0 & \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 31. Neat subgroups of $\mathcal{T}\left(4, \mathbf{E}_{2}\right)$ of core index $\leq 1000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\mathcal{T}\left(6, \mathbf{E}_{2}\right)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{3}{4}$ & 36 & A & NC & $\mathbb{Z}_{6}^{2}$ & $R_{2}, R_{3}$ & $\mathrm{br}_{3}\left(R_{2}, R_{3}\right)$ & 378000, PGU(3, 5) \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 72 & 72 & & $\mathbb{Z}_{2}^{3} \oplus \mathbb{Z}^{8}$ & $(-1)^{12}$ & 8 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 32. Neat subgroups of $\mathcal{T}\left(6, \mathbf{E}_{2}\right)$ of core index $\leq 200$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\mathcal{T}\left(2, \mathbf{H}_{1}\right)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{49}$ & 1176 & A & C & $\mathbb{Z}_{2}$ & & & ? \\
\hline
\end{tabular}
\end{table}

Table 33. Invariants for $\mathcal{T}\left(2, \mathbf{H}_{1}\right)$

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\mathcal{T}\left(2, \mathbf{H}_{2}\right)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{1}{100}$ & 300 & A & C & \{1\} & & & $42573600, P G U(3,9)$ \\
\hline
\end{tabular}
\end{table}

Table 34. Invariants for $\mathcal{T}\left(2, \mathbf{H}_{2}\right)$
$\mathcal{T}\left(3, \mathbf{H}_{2}\right)$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 7) \\
\hline $\frac{26}{75}$ & 1800 & NA & C & $\mathbb{Z}_{3}$ & & & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 35. Invariants for $\mathcal{T}\left(3, \mathbf{H}_{2}\right)$}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|l|}
\hline \multicolumn{11}{|c|}{$\mathcal{T}\left(5, \mathbf{H}_{2}\right)$} \\
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & \multicolumn{2}{|l|}{Cusp relations} & \multicolumn{3}{|l|}{Congr. image (mod 3)} \\
\hline $\frac{73}{100}$ & 600 & A & C & $\mathbb{Z}_{5}$ & & \multicolumn{2}{|c|}{} & \multicolumn{3}{|c|}{23619600} \\
\hline \multicolumn{2}{|c|}{\multirow{2}{*}{}} & \multicolumn{2}{|c|}{Index} & \multicolumn{2}{|c|}{Core Index} & Quotient & Ab & Self-int & $b_{1}$ & \multirow{2}{*}{} \\
\hline & & \multicolumn{2}{|c|}{600} & \multicolumn{2}{|c|}{600} & & $\mathbb{Z}^{20}$ & & 20 & \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 36. Neat subgroups of $\mathcal{T}\left(5, \mathbf{H}_{2}\right)$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(5,7 / 10)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{1}{200}$ & 600 & A & C & \{1\} & & & $42573600, P G U(3,9)$ \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $3000=5 \cdot 600$ & 15000 & & $\mathbb{Z}_{5} \oplus \mathbb{Z}^{4}$ & & 4 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 37. Neat subgroups of $\Gamma(5,7 / 10)$ of core index $\leq 40,000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(6,2 / 3)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{72}$ & 72 & A & NC & $\mathbb{Z}_{6}$ & $R_{1}, R_{2}$ & $\operatorname{br}_{3}\left(R_{1}, R_{2}\right)$ & $378000, P G U(3,5)$ \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 72 & 1944 & & $\mathbb{Z}_{3} \oplus \mathbb{Z}^{2}$ & -1, -3 & 2 \\
\hline 72 & 1944 & & $\mathbb{Z}^{4}$ & $(-1)^{4}$ & 4 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 38. Neat subgroups of $\Gamma(6,2 / 3)$ of core index $\leq 2000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(7,9 / 14)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{1}{49}$ & 588 & A & C & \{1\} & & & ? \\
\hline
\end{tabular}
\end{table}

Table 39. Invariants for $\Gamma(7,9 / 14)$

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(8,5 / 8)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{3}{128}$ & 384 & A & C & $\mathbb{Z}_{4}$ & & & 42 456 960, PGL $(3,9)$ \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $466560=1215 \cdot 384$ & 42456960 & & ? & & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 40. Neat subgroups of $\Gamma(8,5 / 8)$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(9,11 / 18)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{2}{81}$ & 324 & NA & C & $\mathbb{Z}_{3}$ & & & ? \\
\hline
\end{tabular}
\end{table}

Table 41. Invariants for $\Gamma(9,11 / 18)$

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(10,3 / 5)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{1}{40}$ & 600 & A & C & $\mathbb{Z}_{2}$ & & & $42573600, P G U(3,9)$ \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $583200=972 \cdot 600$ & 42573600 & & ? & & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 42. Neat subgroups of $\Gamma(10,3 / 5)$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(12,7 / 12)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{7}{288}$ & 288 & A & C & $\mathbb{Z}_{12}$ & & & 152334000000 \\
\hline
\end{tabular}
\end{table}

Table 43. Invariants for $\Gamma(12,7 / 12)$

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(18,5 / 9)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{5}{9}$ & 648 & A & C & $\mathbb{Z}_{6}$ & & & ? \\
\hline
\end{tabular}
\end{table}

Table 44. Invariants for $\Gamma(18,5 / 9)$

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(4,5 / 12)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{72}$ & 288 & A & C & $\mathbb{Z}_{6}$ & & & 152334000000 \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 864 & 18144 & $P G U(3,3) \times \mathbb{Z}_{3}$ & $\mathbb{Z}_{2}^{3} \oplus \mathbb{Z}^{2}$ & & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 45. Neat subgroups of $\Gamma(4,5 / 12)$ of core index $\leq 40,000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(5,11 / 30)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 7) \\
\hline $\frac{8}{225}$ & 1800 & A & C & $\mathbb{Z}_{3}$ & & & ? \\
\hline
\end{tabular}
\end{table}

Table 46. Invariants for $\Gamma(5,11 / 30)$
\begin{lstlisting}[mathescape=true]
    $\Gamma(6,1 / 3)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{18}$ & 18 & A & NC & $\mathbb{Z}_{3} \oplus \mathbb{Z}_{6}$ & $$\begin{gathered}
R_{1}, R_{2} \\
c_{1}=R_{1}, c_{2}=J \overline{2}
\end{gathered}$$ & $$\begin{gathered}
\operatorname{br}_{3}\left(R_{1}, R_{2}\right) \\
c_{1}^{6}, c_{2}^{3}, \operatorname{br}_{4}\left(c_{1}, c_{2}\right)
\end{gathered}$$ & 378000, PGU(3, 5) \\
\hline
\end{tabular}

\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 18 & 18 & & $\mathbb{Z}^{4}$ & $(-1)^{4}$ & 4 \\
\hline 18 & 54 & & $\mathbb{Z}_{3} \oplus \mathbb{Z}^{2}$ & -1, -3 & 2 \\
\hline 18 & 162 & & $\mathbb{Z}^{2}$ & -1, -3 & 2 \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
Table 47. Neat subgroups of $\Gamma(6,1 / 3)$ of core index $\leq 1,000$
    $\Gamma(7,13 / 42)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{61}{882}$ & 1764 & NA & C & $\mathbb{Z}_{3}$ & & & ? \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
    Table 48. Invariants for $\Gamma(7,13 / 42)$
    $\Gamma(8,7 / 24)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{11}{144}$ & 576 & NA & C & $\mathbb{Z}_{6}$ & & & ? \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
    Table 49. Invariants for $\Gamma(8,7 / 24)$
    $\Gamma(9,5 / 18)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{13}{162}$ & 324 & A & C & $\mathbb{Z}_{3}^{2}$ & & & ? \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
    Table 50. Invariants for $\Gamma(9,5 / 18)$
    $\Gamma(10,4 / 15)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 7) \\
\hline $\frac{37}{450}$ & 450 & NA & C & $\mathbb{Z}_{6}$ & & & ? \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
    Table 51. Invariants for $\Gamma(10,4 / 15)$
    $\Gamma(12,1 / 4)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{12}$ & 144 & A & C & $\mathbb{Z}_{3} \oplus \mathbb{Z}_{6}$ & & & 152334000000 \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
    Table 52. Invariants for $\Gamma(12,1 / 4)$
\end{lstlisting}


\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(18,2 / 9)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{13}{162}$ & 162 & A & C & $\mathbb{Z}_{3} \oplus \mathbb{Z}_{6}$ & & & \\
\hline
\end{tabular}
\end{table}

Table 53. Invariants for $\Gamma(18,2 / 9)$

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(3,1 / 3)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{288}$ & 288 & A & C & $\mathbb{Z}_{3}$ & & & 152334000000 \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 864 & 18,144 & $\mathbb{Z}_{3} \times \operatorname{PSU}(3,3)$ & $\mathbb{Z}^{2}$ & & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 54. Neat subgroups of $\Gamma(3,1 / 3)$ of core index $\leq 30,000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(4,1 / 4)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{1}{32}$ & 96 & A & NC & $\mathbb{Z}_{4}$ & $c_{1}=1, c_{2}=J \overline{2} \overline{1}$ & $c_{1}^{4}, c_{2}^{4}, \mathrm{br}_{4}\left(c_{1}, c_{2}\right)$ & 6048 \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 96 & 96 & & $\mathbb{Z}_{2}^{2} \oplus \mathbb{Z}^{4}$ & $(-2)^{6}$ & 4 \\
\hline 96 & 384 & & $\mathbb{Z}_{2} \oplus \mathbb{Z}_{4}^{2} \oplus \mathbb{Z}^{2}$ & $(-2)^{2},(-4)^{2}$ & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 55. Neat subgroups of $\Gamma(4,1 / 4)$ of core index $\leq 1,000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(5,1 / 5)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{23}{400}$ & 1200 & NA & C & \{1\} & & & 1852734273062400 \\
\hline
\end{tabular}
\end{table}

Table 56. Invariants for $\Gamma(5,1 / 5)$
[9] M. Deraux. Spocheck. https://hal.archives-ouvertes.fr/hal-02398953, 2019.
[10] Martin Deraux. gitlab project neat subgroups. https://plmlab.math.cnrs.fr/deraux/neat-subs.
[11] Martin Deraux. Deforming the $\mathbb{R}$-fuchsian (4, 4, 4)-triangle group into a lattice. Topology, 45(6):989-1020, 2006.
[12] Martin Deraux. Forgetful maps between Deligne-Mostow ball quotients. Geom. Dedicata, 150:377-389, 2011.
[13] Martin Deraux, John R. Parker, and Julien Paupert. New nonarithmetic complex hyperbolic lattices. Invent. Math., 203(3):681-771, 2016.
[14] Martin Deraux, John R. Parker, and Julien Paupert. New nonarithmetic complex hyperbolic lattices II. Michigan Math. J., 70(1):133-205, 2021.
[15] Luca Di Cerbo and Matthew Stover. Classification and arithmeticity of toroidal compactifications with $3 \bar{c}_{2}=\bar{c}_{1}^{2}=3$. Geom. Topol., 22(4):2465-2510, 2018.
\begin{lstlisting}[mathescape=true]
    $\Gamma(6,1 / 6)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{11}{144}$ & 144 & NA & NC & $\mathbb{Z}_{6}$ & $R_{1}, R_{2}$ & $\operatorname{br}_{3}\left(R_{1}, R_{2}\right)$ & 152334000000 \\
\hline
\end{tabular}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $864=6 \cdot 144$ & 20736 & & $\mathbb{Z}_{3} \oplus \mathbb{Z}_{6}^{2} \oplus \mathbb{Z}^{2}$ & -1, -2, (-3) ${ }^{5},(-6)^{5}$ & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 57. Neat subgroup of $\Gamma(6,1 / 6)$ obtained from reduction $\bmod 6$}
\end{table}
\begin{lstlisting}[mathescape=true]
    $\Gamma(8,1 / 8)$
\end{lstlisting}


\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 57. Neat subgroup of $\Gamma(6,1 / 6)$ obtained from reduction $\bmod 6$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{3}{32}$ & 192 & A & C & $\mathbb{Z}_{8}$ & & & $42456960, P G L(3,9)$ \\
\hline
\end{tabular}
\end{table}
\begin{lstlisting}[mathescape=true]
        Table 58. Invariants for $\Gamma(8,1 / 8)$
    $\Gamma(12,1 / 12)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{7}{72}$ & 144 & A & C & $\mathbb{Z}_{12}$ & & & 152334000000 \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
    Table 59. Invariants for $\Gamma(12,1 / 12)$
    $\Gamma(3,7 / 30)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 7) \\
\hline $\frac{2}{225}$ & 1800 & A & C & $\mathbb{Z}_{3}$ & & & ? \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
    Table 60. Invariants for $\Gamma(3,7 / 30)$
    $\Gamma(4,3 / 20)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{33}{800}$ & 2400 & NA & C & $\mathbb{Z}_{2}$ & & & 1852734273062400 \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
    Table 61. Invariants for $\Gamma(4,3 / 20)$
    $\Gamma(5,1 / 10)$
\end{lstlisting}


\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{13}{200}$ & 600 & A & C & $\mathbb{Z}_{5}$ & & & $42573600, P G U(3,9)$ \\
\hline
\end{tabular}

\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 600 & 600 & & $\mathbb{Z}^{8}$ & & 8 \\
\hline 600 & 15000 & & $\mathbb{Z}_{5}^{2} \oplus \mathbb{Z}^{4}$ & & 4 \\
\hline 600 & 15000 & & $\mathbb{Z}_{5}^{5}$ & & 0 \\
\hline
\end{tabular}
\begin{lstlisting}[mathescape=true]
    Table 62. Neat subgroups of $\Gamma(5,1 / 10)$ of core index $\leq 30,000$
\end{lstlisting}


\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(10,0)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{1}{10}$ & 150 & A & C & $\mathbb{Z}_{10}$ & & & $42573600, P G U(3,9)$ \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 150 & 600 & & $\mathbb{Z}_{2}^{4} \oplus \mathbb{Z}^{4}$ & & 4 \\
\hline 150 & 750 & & $\mathbb{Z}_{5}^{2} \oplus \mathbb{Z}^{4}$ & & 4 \\
\hline 150 & 1800 & & $\mathbb{Z}_{5}^{2} \oplus \mathbb{Z}^{4}$ & & 4 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 63. Neat subgroups of $\Gamma(10,0)$ of core index $\leq 2,000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(3,1 / 6)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{72}$ & 72 & A & NC & $\mathbb{Z}_{3}^{2}$ & $c_{1}=1, c_{2}=J \overline{2} \overline{1}$ & $c_{1}^{3}, c_{2}^{6}, \mathrm{br}_{4}\left(c_{1}, c_{2}\right)$ & 378000, $\operatorname{PGU}(3,5)$ \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 72 & 72 & & $\mathbb{Z}^{4}$ & $(-1)^{4}$ & 4 \\
\hline 72 & 648 & & $\mathbb{Z}_{3} \oplus \mathbb{Z}^{2}$ & -1, -3 & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 64. Neat subgroups of $\Gamma(3,1 / 6)$ of core index $\leq 2,000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(4,1 / 12)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{13}{288}$ & 288 & NA & C & $\mathbb{Z}_{12}$ & & & 152334000000 \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 864 & 864 & & $\mathbb{Z}_{2}^{6} \oplus \mathbb{Z}^{4}$ & & 4 \\
\hline 864 & 3456 & & $\mathbb{Z}_{2}^{8} \oplus \mathbb{Z}^{2}$ & & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 65. Neat subgroups of $\Gamma(4,1 / 12)$ of core index $\leq 10,000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(6,0)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{12}$ & 36 & A & NC & $\mathbb{Z}_{3} \oplus \mathbb{Z}_{6}$ & $R_{1}, R_{2}$ & $\operatorname{br}_{3}\left(R_{1}, R_{2}\right)$ & $378000, P G U(3,5)$ \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline 72 & 216 & & $\mathbb{Z}_{3} \oplus \mathbb{Z}^{4}$ & $(-1)^{3},(-3)^{3}$ & 4 \\
\hline 72 & 216 & & $\mathbb{Z}_{3}^{2} \oplus \mathbb{Z}^{2}$ & (-3) ${ }^{4}$ & 2 \\
\hline 72 & 648 & & $\mathbb{Z}_{3} \oplus \mathbb{Z}^{2}$ & -3, -9 & 2 \\
\hline 72 & 864 & & $\mathbb{Z}_{3} \oplus \mathbb{Z}^{2}$ & -12 & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 66. Neat subgroups of $\Gamma(6,0)$ of core index $\leq 1,000$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(3,5 / 42)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{61}{3528}$ & 3528 & NA & C & $\mathbb{Z}_{3}$ & & & ? \\
\hline
\end{tabular}
\end{table}

Table 67. Invariants for $\Gamma(3,5 / 42)$

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(3,1 / 12)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{11}{576}$ & 576 & NA & C & $\mathbb{Z}_{3}$ & & & ? \\
\hline
\end{tabular}
\end{table}

Table 68. Invariants for $\Gamma(3,1 / 12)$

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(4,0)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 3) \\
\hline $\frac{3}{64}$ & 192 & A & C & $\mathbb{Z}_{4}$ & & & $42456960, P G L(3,9)$ \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $16512=86 \cdot 192$ & 5663616 ( $P G U(3,7)$ ) & & ? & & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 69. Neat subgroups of $\Gamma(4,0)$}
\end{table}

$\Gamma(3,1 / 18)$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{13}{648}$ & 648 & A & C & $\mathbb{Z}_{3}^{2}$ & & & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 70. Invariants for $\Gamma(3,1 / 18)$}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(3,1 / 30)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 7) \\
\hline $\frac{37}{1800}$ & 1,800 & NA & C & $\mathbb{Z}_{3}$ & & & ? \\
\hline
\end{tabular}
\end{table}

Table 71. Invariants for $\Gamma(3,1 / 30)$

\begin{table}
\captionsetup{labelformat=empty}
\caption{$\Gamma(3,0)$}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $\chi$ & LCM & A? & C? & Ab & Cusps & Cusp relations & Congr. image (mod 5) \\
\hline $\frac{1}{48}$ & 144 & A & C & $\mathbb{Z}_{3}^{2}$ & & & ? \\
\hline
\end{tabular}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Index & Core Index & Quotient & Ab & Self-int & $b_{1}$ \\
\hline $2016=14 \cdot 144$ & 54,432 & $P G U(3,3) \times \mathbb{Z}_{3}^{2}$ & $\mathbb{Z}_{3}^{4} \oplus \mathbb{Z}^{4}$ & & 4 \\
\hline 2016 & 54,432 & $P G U(3,3) \times \mathbb{Z}_{3}^{2}$ & $\mathbb{Z}_{3}^{6} \oplus \mathbb{Z}^{2}$ & & 2 \\
\hline 2016 & 54,432 & $P G U(3,3) \times \mathbb{Z}_{3}^{2}$ & $\mathbb{Z}_{3}^{8}$ & & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 72. Neat subgroups of $\Gamma(3,0)$}
\end{table}
[16] Luca F. Di Cerbo and Matthew Stover. Bielliptic ball quotient compactifications and lattices in PU(2, 1) with finitely generated commutator subgroup. Ann. Inst. Fourier, 67(1):315-328, 2017.
[17] Allan L. Edmonds, John H. Ewing, and Ravi S. Kulkarni. Torsion free subgroups of Fuchsian groups and tessellations of surfaces. Invent. Math., 69:331-346, 1982.
[18] Philippe Eyssidieux. Orbifold kähler groups related to arithmetic complex hyperbolic lattices. Preprint https://arxiv.org/abs/1805.00767.
[19] H. Garland and M. S. Raghunathan. Fundamental domains for lattices in R-rank 1 semisimple Lie groups. Ann. Math. (2), 92:279-326, 1970.
[20] William M. Goldman. Complex hyperbolic geometry. Oxford: Clarendon Press, 1999.
[21] Phillip Griffiths and Joseph Harris. Principles of algebraic geometry. New York, NY: John Wiley \& Sons Ltd., 2nd ed. edition, 1994.
[22] Friedrich Hirzebruch. Automorphe Formen und der Satz von Riemann-Roch. Sympos. Int. Topologia Algebraica 129-144 (1958), 1958.
[23] Friedrich Hirzebruch. Chern numbers of algebraic surfaces : an example. Math. Ann., 266:351-356, 1984.
[24] Rolf-Peter Holzapfel. Ball and surface arithmetics, volume E29. Wiesbaden: Vieweg, 1998.
[25] Kerry N. Jones and Alan W. Reid. Minimal index torsion-free subgroups of Kleinian groups. Math. Ann., 310(2):235-250, 1998.
[26] Michael Kapovich. Hyperbolic manifolds and discrete groups, volume 183 of Progress in Mathematics. Boston, MA: Birkhäuser, 2001.
[27] Bruno Klingler. On the rigidity of certain fundamental groups, arithmeticity of complex hyperbolic lattices, and the "fake projective planes". Invent. Math., 153(1):105-143, 2003.
[28] Shoshichi Kobayashi and Katsumi Nomizu. Foundations of differential geometry. Vol. II, volume 15 of Intersci. Tracts Pure Appl. Math. Interscience Publishers, New York, NY, 1969.
[29] Alexander Kolpakov and Bruno Martelli. Hyperbolic four-manifolds with one cusp. Geom. Funct. Anal., 23(6):1903-1933, 2013.
[30] R. A. Livné. On certain covers of the universal elliptic curve. PhD thesis, Harvard University, 1981.
[31] D. D. Long and A. W. Reid. All flat manifolds are cusps of hyperbolic orbifolds. Algebr. Geom. Topol., 2:285-296, 2002.
[32] Ngaiming Mok. Projective algebraicity of minimal compactifications of complex-hyperbolic space forms of finite volume. In Perspectives in analysis, geometry, and topology. On the occasion of the 60th birthday of Oleg Viro. Based on the Marcus Wallenberg symposium on perspectives in analysis, geometry, and topology, Stockholm, Sweden, May 19-25, 2008, pages 331-354. Basel: Birkhäuser, 2012.
[33] G. D. Mostow. On a remarkable class of polyhedra in complex hyperbolic space. Pacific J. Math., 86:171-276, 1980.
[34] G. D. Mostow. Generalized Picard lattices arising from half-integral conditions. Publ. Math., Inst. Hautes Étud. Sci., 63:91-106, 1986.
[35] G. D. Mostow. Braids, hypergeometric functions, and lattices. Bull. Am. Math. Soc., New Ser., 16:225-246, 1987.
[36] Jürgen Neukirch. Algebraic Number Theory, volume 322 of Grundlehren Math. Wiss. Berlin: Springer, 1999.
[37] Gopal Prasad and Sai-Kee Yeung. Fake projective planes. Invent. Math., 168(2):321-370, 2007.
[38] John Kurt jun. Sauter. Isomorphisms among monodromy groups and applications to lattices in PU(1, 2). Pac. J. Math., 146(2):331-384, 1990.
[39] Atle Selberg. On discontinuous groups in higher-dimensional symmetric spaces. Contrib. Function Theory, Int. Colloqu. Bombay, Jan. 1960, 1960.
[40] G. C. Shephard and J. A. Todd. Finite unitary reflection groups. Canadian J. Math., 6:274-304, 1954.
[41] Matthew Stover. Cusps of Picard modular surfaces. Geom. Dedicata, 157:239-257, 2012.
[42] J. M. Thompson. Complex Hyperbolic Triangle Groups. PhD thesis, Durham University, 2010.
[43] William P. Thurston. Shapes of polyhedra and triangulations of the sphere. In The Epstein Birthday Schrift dedicated to David Epstein on the occasion of his 60th birthday, pages 511-549. Warwick: University of Warwick, Institute of Mathematics, 1998.
[44] Jacques Tits. Sur la classification des groupes algébriques semisimples. C. R. Acad. Sci., 249:1438-1440, 1959.
[45] Paula Tretkoff. Complex ball quotients and line arrangements in the projective plane. With an appendix by Hans-Christoph Im Hof, volume 51 of Math. Notes (Princeton). Princeton, NJ: Princeton University Press, 2016.
[46] A. Weil. Algebras with involutions and the classical groups. J. Indian Math. Soc., New Ser., 24:589-623, 1961.
[47] Sai-Kee Yeung. Integrality and arithmeticity of co-compact lattice corresponding to certain complex two-ball quotients of Picard number one. Asian J. Math., 8(1):107-130, 2004.

Martin Deraux : Université Grenoble Alpes, Institut Fourier, 100 rue des Mathématiques 38610 Gières; Sorbonne Université and Université de Paris, CNRS, INRIA, IMJ-PRG, Ouragan, F-75005 Paris, France
Email address: martin.deraux@univ-grenoble-alpes.fr
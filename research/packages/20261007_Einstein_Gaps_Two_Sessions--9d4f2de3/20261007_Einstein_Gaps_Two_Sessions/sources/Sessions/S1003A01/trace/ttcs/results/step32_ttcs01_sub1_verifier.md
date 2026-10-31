# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md",
    "Knowledge/objects/papers/Degenerating-Kähler-Einstein-cones-locally-symmetric-cusps-and-the-Tian--adb04d311c2f--499d8f08a8b4/object.md",
    "Knowledge/objects/papers/Invariants-of-some-compactified-Picard-modular-surfaces-and-applications--a2801b1afe2c--6270e445600c/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Skills/geometric-analysis/research/paper/sections/variational_geometry.tex",
    "Skills/geometric-analysis/research/paper/sections/linear_coercivity.tex"
  ]
}
```

## Task

Independently verify the theorem-level ramified Kähler–Einstein background and actual-field part of the proposed Einstein-gap transfer. Read the revised Step-31 note and the cited original-source representations. Check: (i) whether a preliminary principal-congruence cover can contain the required fixed buffered CH ball and later high-ramification congruence covers can be taken inside it; (ii) whether Biquard–Guenancia gives smooth compact Ric=-g pullbacks and uniform local C^2 convergence on every lifted marked ball; (iii) the Hurwitz/adjunction/log-proportionality formulas for A=K^2 and Delta=3chi-A; (iv) the positive-r tower assertion, especially the use of Dzambic’s index and boundary self-intersection formulas to obtain Delta→∞ and Delta/A→0; (v) ampleness/minimal general type and LeBrun’s metricwise polarized class after blowups and S1xS3 handles, including b+=1 chambers, exceptional signs, p>=A, and a^2>=T+. Give precise corrections if any step is stronger than its sources.

## Output

# Scientific verification memo

## Overall assessment

The ramified Kähler–Einstein background and the metricwise Seiberg–Witten field supply are mathematically supported by the cited sources. Four wording refinements make the argument source-exact:

1. After constructing the preliminary congruence cover, all later notation should be reset relative to that cover and its toroidal compactification.
2. Later high-ramification covers are **chosen** inside the preliminary subgroup; this is not automatic for an arbitrary sequence from Biquard–Guenancia.
3. The uniform \(C^{2}\) estimate on all lifted marked regions follows by pulling back one estimate on the fixed base region; Biquard–Guenancia themselves provide local \(C^\infty\) convergence only on fixed compact subsets of the open quotient.
4. The Džambić growth statement is best made with an explicit inert-prime-power tower. “Degree-eight level growth” is then precise; for a general ideal parameter, the relation between ideal norm, rational level, and index needs separate notation.

With these refinements, items (i)–(v) all hold.

---

## 1. Preliminary congruence cover and the marked complex-hyperbolic ball

Let \(\Gamma\) be represented faithfully as an arithmetic matrix group and let \(o\in\mathbb B^{2}\). Put
\[
R_* = R_{128}+R_{\mathrm{buf}},
\]
where \(R_{\mathrm{buf}}>0\) is the fixed annular allowance. Proper discontinuity implies that
\[
S_{R_*}
 =\{\gamma\in\Gamma\setminus\{1\}:d(o,\gamma o)\le 2R_*\}
\]
is finite.

For principal congruence subgroups \(\Gamma(\mathfrak a)\),
\[
\bigcap_{\mathfrak a}\Gamma(\mathfrak a)=\{1\}.
\]
Hence one can choose a sufficiently deep ideal \(\mathfrak a_0\) such that
\[
\Gamma(\mathfrak a_0)\cap S_{R_*}=\varnothing.
\]
It follows that the projection
\[
B_{\mathbb{CH}^{2}}(o,R_*)\longrightarrow
\Gamma(\mathfrak a_0)\backslash\mathbb B^{2}
\]
is injective. Indeed, two points in this ball identified by \(\gamma\) would give
\(d(o,\gamma o)\le 2R_*\).

Because the starting group is neat, or because \(\mathfrak a_0\) may be chosen neat, the quotient and its toroidal compactification are smooth. One should now rename
\[
X_0^\circ=\Gamma(\mathfrak a_0)\backslash\mathbb B^{2},
\qquad (\bar X_0,D_0)
\]
and regard this as the fixed base for everything that follows.

Later congruence subgroups can be chosen inside \(\Gamma(\mathfrak a_0)\). In ideal notation, it is enough to take
\[
\mathfrak a_m\subset\mathfrak a_0,
\qquad
\Gamma(\mathfrak a_m)\subset\Gamma(\mathfrak a_0).
\]
Alternatively, intersect any high-ramification congruence subgroup with \(\Gamma(\mathfrak a_0)\), or replace its level by the product with \(\mathfrak a_0\). Passing to a deeper subgroup does not reduce cusp ramification: the corresponding central cusp-translation lattice only becomes smaller.

Thus the preliminary marked-ball construction and the later ramified construction are compatible. Mutual nesting among all later covers is unnecessary.

---

## 2. What Biquard–Guenancia supplies

For the fixed smooth toroidal pair \((\bar X_0,D_0)\), write
\[
D_0=\coprod_{\lambda=1}^{N}D_\lambda.
\]
Section 4.1 of Biquard–Guenancia explicitly permits a vector of cone parameters
\[
\boldsymbol\beta_m=(\beta_{m,1},\ldots,\beta_{m,N})
\]
with componentwise convergence to zero. Their Theorem 1.1 and §4.1 give
\[
\omega_{\boldsymbol\beta_m}\longrightarrow\omega_{\mathrm{hyp}}
\quad\text{in }C^\infty_{\mathrm{loc}}(X_0^\circ).
\]

For a congruence cover
\[
\pi_m:X_m^\circ\longrightarrow X_0^\circ
\]
whose ramification order over \(D_\lambda\) is \(v_{m,\lambda}\), §4.3 takes
\[
\beta_{m,\lambda}=v_{m,\lambda}^{-1}.
\]
The conic metric on \(\bar X_0\) is then an orbifold Kähler metric, and
\[
g_m:=\bar\pi_m^*\omega_{\boldsymbol\beta_m}
\]
is a genuine smooth Kähler metric on the compact smooth manifold \(\bar X_m\), satisfying
\[
\operatorname{Ric}(g_m)=-g_m.
\]
This is stated directly in §4.3.

Let \(K\Subset X_0^\circ\) be the fixed marked ball together with its buffer. Then
\[
\varepsilon_m
 :=\|\omega_{\boldsymbol\beta_m}-\omega_{\mathrm{hyp}}\|_{C^2(K)}
 \longrightarrow0.
\]
If \(d_m=\deg(\pi_m)\), the preimage \(\pi_m^{-1}(K)\) consists of \(d_m\) disjoint copies of \(K\), since \(K\) is simply connected and embedded. In the marked identifications of those copies with \(K\),
\[
\|g_m-g_{\mathrm{CH}}\|_{C^2(K_{m,j})}=\varepsilon_m
\]
for every sheet \(j\). Thus the estimate is uniform across all lifts and, in fact, identical sheet by sheet.

The source gives no quantitative rate in \(m\), and none is needed here. The equality of the sheetwise discrepancies comes from the pullback construction, not from an additional global convergence theorem.

---

## 3. Hurwitz, adjunction, Euler characteristic, and \(\Delta_m\)

Assume, as in §4.3, that the covers are Galois after passing to a further congruence subgroup. Then each component \(D_\lambda\) has a well-defined ramification order \(v_{m,\lambda}\). Put
\[
\beta_{m,\lambda}=v_{m,\lambda}^{-1},
\qquad
L=K_{\bar X_0}+D_0.
\]

Hurwitz gives
\[
K_{\bar X_m}
 =\bar\pi_m^*\!\left(
 K_{\bar X_0}
 +\sum_\lambda(1-\beta_{m,\lambda})D_\lambda
 \right)
 =\bar\pi_m^*\!\left(
 L-\sum_\lambda\beta_{m,\lambda}D_\lambda
 \right).
\]
Therefore, with \(A_m=K_{\bar X_m}^{2}\),
\[
\frac{A_m}{d_m}
 =\left(L-\sum_\lambda\beta_{m,\lambda}D_\lambda\right)^2.
\]

The curves \(D_\lambda\) are disjoint elliptic curves. Adjunction yields
\[
(K_{\bar X_0}+D_\lambda)\cdot D_\lambda=2g(D_\lambda)-2=0.
\]
Since all other \(D_\mu\) are disjoint from \(D_\lambda\),
\[
L\cdot D_\lambda=0.
\]
Consequently,
\[
\boxed{\frac{A_m}{d_m}
 =L^2+\sum_\lambda\beta_{m,\lambda}^{2}D_\lambda^{2}.}
\]
Each \(D_\lambda^{2}<0\), so \(A_m/d_m<L^2\), while
\[
\frac{A_m}{d_m}\longrightarrow L^2>0.
\]

For Euler characteristic, decompose
\[
\bar X_m=X_m^\circ\sqcup D_m.
\]
The open part is a degree-\(d_m\) cover and every component of \(D_m\) is elliptic. Hence
\[
\chi(\bar X_m)
 =\chi(X_m^\circ)+\chi(D_m)
 =d_m\chi(X_0^\circ).
\]
Logarithmic proportionality for a complex-hyperbolic surface gives
\[
L^2=3\chi(X_0^\circ),
\]
and therefore
\[
\chi(\bar X_m)=\frac{d_mL^2}{3}.
\]

It follows exactly that
\[
\boxed{
\Delta_m:=3\chi(\bar X_m)-A_m
 =-d_m\sum_\lambda
       \beta_{m,\lambda}^{2}D_\lambda^{2}>0.
}
\]
Moreover,
\[
\frac{\Delta_m}{d_m}\longrightarrow0,
\qquad
\frac{A_m}{d_m}\longrightarrow L^2,
\qquad
\frac{\Delta_m}{A_m}\longrightarrow0.
\]
Thus \(d_m\asymp A_m\), and the \(d_m\) lifted marked balls have positive density relative to \(A_m\).

---

## 4. An explicit Džambić tower with \(\Delta_m\to\infty\)

Džambić’s relevant formulas are:

- Theorem 2.5: the principal-congruence index.
- Proposition 3.2:
  \[
  c_1^2(\widetilde{Y(\mathfrak a)})
  =3c_2(Y(\mathfrak a))+T_{\mathfrak a}^{\,2},
  \]
  where \(T_{\mathfrak a}\) is the total toroidal divisor.
- Proposition 3.3:
  \[
  c_2(Y(\mathfrak a))
  =[\Gamma_K:\Gamma_K(\mathfrak a)]\,c_2(Y(1)).
  \]
- Proposition 3.5:
  \[
  T_{\mathfrak a}^{\,2}
  =-\frac{h_K\eta_K}{\vartheta_{\mathfrak a}^{\,2}}
       [\Gamma_K:\Gamma_K(\mathfrak a)],
  \]
  with
  \[
  \vartheta_{\mathfrak a}
   =\min\{q\in\mathbb N:\mathfrak a\mid q\sqrt{-d}\}.
  \]

For a source-exact growth argument, choose the preliminary ideal
\(\mathfrak a_0\) as above, then choose an odd rational prime \(p\) inert in
\(K\), coprime to \(\mathfrak a_0\) and to the discriminant. Set
\[
\mathfrak a_n=\mathfrak a_0(p)^n.
\]
Then
\[
\Gamma_K(\mathfrak a_n)\subset\Gamma_K(\mathfrak a_0).
\]

Džambić’s inert-prime local factor gives
\[
I_n:=[\Gamma_K:\Gamma_K(\mathfrak a_n)]
 \asymp p^{8n}.
\]
Since \(p\nmid d\mathfrak a_0\),
\[
\vartheta_{\mathfrak a_n}
 =\vartheta_{\mathfrak a_0}p^n
 \asymp p^n.
\]
Hence
\[
\Delta_n=-T_{\mathfrak a_n}^{\,2}
 =\frac{h_K\eta_K I_n}{\vartheta_{\mathfrak a_n}^{\,2}}
 \asymp p^{6n}\longrightarrow\infty.
\]
At the same time,
\[
A_n
 =3I_n c_2(Y(1))-\Delta_n
 \asymp p^{8n},
\]
and therefore
\[
\boxed{\frac{\Delta_n}{A_n}\asymp p^{-2n}\longrightarrow0.}
\]

The cusp-width quantity \(\vartheta_{\mathfrak a_n}\) is the arithmetic input governing the central cusp-translation period. Relative to the preliminary level, that period acquires the factor \(p^n\), so all ramification orders tend to infinity. This is compatible with the high-ramification construction in Biquard–Guenancia §4.3.

Thus the existence of towers with
\[
\Delta_m\to\infty,
\qquad
\Delta_m/A_m\to0
\]
is fully established. The phrase “degree-eight level growth” should refer specifically to a rational prime-power level such as the inert tower above. For arbitrary integral ideals, the ideal norm is a different parameter and should not be identified silently with the rational level.

---

## 5. Ampleness, minimality, and the metricwise actual class

Since \(g_m\) is Kähler and
\[
\operatorname{Ric}(g_m)=-g_m,
\]
its Ricci form satisfies
\[
[\rho_{g_m}]=2\pi c_1(\bar X_m)=-[\omega_m].
\]
Thus
\[
[\omega_m]=2\pi c_1(K_{\bar X_m}).
\]
The canonical line bundle therefore has a positive curvature representative and is ample by Kodaira. It follows that \(\bar X_m\) is a smooth surface of general type. It is minimal: if \(E\) were a \((-1)\)-curve, adjunction would give
\[
K_{\bar X_m}\cdot E=-1,
\]
incompatible with ampleness.

Let
\[
X=\bar X_m,\qquad A=K_X^2.
\]
The canonical Spin\(^c\) structure has determinant class
\[
c=c_1(X)=-K_X,
\qquad c^2=A.
\]
The nonzero invariant needed here is the polarization/small-perturbation invariant used in LeBrun’s Definition 1 and Proposition 3.2. For \(b^+=1\), this is the chamber selected by that polarized construction; it is not a chamber-free statement about an arbitrary class.

Now form
\[
M=X\#k\overline{\mathbb{CP}}^{\,2}
   \#\ell(S^1\times S^3).
\]
For a given metric \(g\), let \(H=H_g^+\). Choose signs of the exceptional generators so that
\[
E_i\cdot E_j=-\delta_{ij},
\qquad
c\cdot E_i=0,
\qquad
c_H^+\cdot E_i\le0.
\]
LeBrun’s Proposition 3.2 and its proof then supply an actual Spin\(^c\) structure with
\[
a_H=c-\sum_{i=1}^{k}E_i
\]
and nonzero polarized invariant. The \(\ell\) handle summands are represented by the \(\ell\) degree-one holonomy insertions described there. Hence its unperturbed monopole equations are solvable for every \(H\)-adapted metric. Since \(H_g^+\) is unchanged under conformal rescaling in dimension four, the same structure works throughout the conformal class.

Its self-dual square satisfies
\[
\begin{aligned}
p:=(a_H^+)^2
 &= (c_H^+)^2
   -2\sum_i c_H^+\cdot E_i
   +\left|\sum_iE_i^+\right|^2 \\
 &\ge (c_H^+)^2
 \ge c^2=A.
\end{aligned}
\]
Its ordinary square is
\[
a_H^2
 =c^2-k
 =A-k.
\]
On the connected sum,
\[
T_+=2\chi(M)+3\tau(M)=A-k-4\ell,
\]
so
\[
\boxed{a_H^2=A-k\ge A-k-4\ell=T_+.}
\]

This verifies exactly the two inputs used by the linear-window theorem:
\[
p\ge A,\qquad a_H^2\ge T_+.
\]
The selected determinant class depends on the metric through the exceptional signs; the theorem needs precisely this metricwise selection, not one fixed sign choice for every metric.

Finally, the scalar monopole estimate gives
\[
\int_M s_g^2\,d\mu_g\ge32\pi^2p\ge32\pi^2A>0,
\]
which rules out Ricci-flat metrics independently of the traceless-Ricci estimate.

---

## Source-exact formulation recommended for Step 31

A precise condensed version is:

> After replacing the original Picard modular quotient by a sufficiently deep neat principal-congruence cover, fix an embedded buffered complex-hyperbolic ball. Choose all later principal levels inside this preliminary subgroup and with cusp ramification orders tending to infinity. Biquard–Guenancia §4.1 and §4.3 then provide conic metrics on the fixed compactification converging locally smoothly to the complex-hyperbolic metric, whose pullbacks are smooth compact Kähler–Einstein metrics with \(\operatorname{Ric}=-g\). The sheetwise \(C^2\) discrepancy on every lift of the marked region is the same and tends to zero. Hurwitz, adjunction, and logarithmic proportionality give
> \[
> \frac{K_{\bar X_m}^2}{d_m}
> =L^2+\sum_\lambda v_{m,\lambda}^{-2}D_\lambda^2,
> \qquad
> 3\chi(\bar X_m)-K_{\bar X_m}^2
> =-d_m\sum_\lambda v_{m,\lambda}^{-2}D_\lambda^2.
> \]
> For an explicit inert-prime-power Picard tower, Džambić’s index and toroidal-divisor formulas give
> \(\Delta_m\asymp p^{6m}\), \(A_m\asymp p^{8m}\), and
> \(\Delta_m/A_m\to0\). The smooth Kähler–Einstein metric makes
> \(K_{\bar X_m}\) ample. LeBrun’s polarized blow-up/handle construction then supplies, for every metric on the surgically modified manifold, a conformally actual Spin\(^c\) class with
> \[
> (a_H^+)^2\ge A_m,\qquad
> a_H^2=A_m-k_m\ge T_{+,m}.
> \]

This formulation matches the supplied original sources without requiring any additional global convergence or chamber-independent invariant.
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 32,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step32_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step32_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the theorem-level ramified Kähler–Einstein background and actual-field part of the proposed Einstein-gap transfer. Read the revised Step-31 note and the cited original-source representations. Check: (i) whether a preliminary principal-congruence cover can contain the required fixed buffered CH ball and later high-ramification congruence covers can be taken inside it; (ii) whether Biquard–Guenancia gives smooth compact Ric=-g pullbacks and uniform local C^2 convergence on every lifted marked ball; (iii) the Hurwitz/adjunction/log-proportionality formulas for A=K^2 and Delta=3chi-A; (iv) the positive-r tower assertion, especially the use of Dzambic’s index and boundary self-intersection formulas to obtain Delta→∞ and Delta/A→0; (v) ampleness/minimal general type and LeBrun’s metricwise polarized class after blowups and S1xS3 handles, including b+=1 chambers, exceptional signs, p>=A, and a^2>=T+. Give precise corrections if any step is stronger than its sources.

## Integrated Scientific Memo

# Verification memo: Step 31 ramified KE background and actual-field supply

## Verdict

The ramified Kähler–Einstein transfer is valid after several source-exact qualifications:

1. Reset the base after the preliminary congruence cover, and choose all later covers inside it.
2. Use covers Galois over that fixed base so each base boundary component has a single ramification index.
3. Attribute local \(C^\infty\) convergence to Biquard–Guenancia (BG), but attribute uniformity across all lifted marked balls to the pullback/deck-cover structure.
4. State the positive-\(r\) tower using an explicit inert rational prime-power Picard tower. This removes ambiguity in “degree-eight level growth.”
5. LeBrun supplies a metricwise polarization-adapted actual Spin\(^c\) class. The exceptional signs may depend on the metric; for \(b^+=1\), one must use the polarization-selected chamber. In the present tower \(b^+>1\) eventually, so chambers are asymptotically irrelevant.

With these corrections, items (i)–(v) are supported.

---

## 1. Preliminary cover and the buffered marked ball

Let \(o\in\mathbb B^2\), and let
\[
R_*=R_{128}+R_{\mathrm{buf}}.
\]
Proper discontinuity makes
\[
F_{R_*}=\{\gamma\in\Gamma\setminus\{1\}:d(o,\gamma o)\le 2R_*\}
\]
finite. Since the intersection of the principal congruence subgroups is trivial, a sufficiently deep principal congruence subgroup \(\Gamma_0\) avoids \(F_{R_*}\). Therefore
\[
B_{\mathbb{CH}^2}(o,R_*)\longrightarrow \Gamma_0\backslash\mathbb B^2
\]
is injective: an identification of two points in the ball would produce a nontrivial \(\gamma\in\Gamma_0\) moving \(o\) by at most \(2R_*\).

The quoted radius
\[
R_{128}=\sqrt6\,\operatorname{arsinh}\sqrt{128}
       =7.645126\ldots
\]
is consistent with the \(\operatorname{Ric}=-g\) normalization and the cell coordinate \(X=|z|^2/(1-|z|^2)\).

After this step, notation should be reset:
\[
X_0^\circ=\Gamma_0\backslash\mathbb B^2,\qquad (\bar X_0,D_0),
\]
and all subsequent ramified covers should be taken over this fixed pair.

Choose later principal levels so that
\[
\Gamma_m\subset \Gamma_0.
\]
For ideal levels this can be enforced by taking \(\mathfrak a_m\subset\mathfrak a_0\), or by multiplying/intersecting levels. Passing to a deeper subgroup cannot reduce cusp ramification. Mutual nesting among the \(\Gamma_m\) is unnecessary.

### Necessary correction

BG §4.3 uses a single ramification order over each base divisor \(D_\lambda\). Thus the covers should be chosen **Galois over \(X_0^\circ\)**. Principal congruence subgroups normal in a fixed ambient Picard modular group provide this automatically. The sentence “later high-ramification covers can be taken inside the preliminary cover” is correct; “an arbitrary cofinal sequence automatically has the required structure” would be too strong.

Because the marked ball is contractible and embedded, its preimage in a degree-\(d_m\) unramified interior cover is exactly \(d_m\) disjoint copies.

---

## 2. What Biquard–Guenancia proves

Write
\[
D_0=\coprod_{\lambda=1}^N D_\lambda.
\]
For a Galois cover \(\bar\pi_m:\bar X_m\to\bar X_0\), let \(v_{m,\lambda}\) be the ramification order over \(D_\lambda\), and set
\[
\beta_{m,\lambda}=v_{m,\lambda}^{-1}.
\]

BG §4.1 permits independent cone angles along the disjoint boundary components and states that, as all components tend to zero,
\[
\omega_{\boldsymbol\beta_m}\longrightarrow\omega_{\mathrm{hyp}}
\quad\text{in }C^\infty_{\mathrm{loc}}(X_0^\circ).
\]
Their detailed proof is written first for proportional angle vectors, while §4.1 says the vector-angle argument carries over. This extension is also justified directly by the componentwise monotonicity of the potentials, sandwiching an arbitrary angle vector between diagonal vectors with its minimum and maximum components, followed by the same local Chern–Lu estimates and elliptic bootstrapping. Thus the vector-angle use in Step 31 is defensible.

BG §4.3 then shows that, for \(\beta_{m,\lambda}=1/v_{m,\lambda}\),
\[
g_m:=\bar\pi_m^*\omega_{\boldsymbol\beta_m}
\]
is a genuine smooth Kähler–Einstein metric on the compact smooth manifold \(\bar X_m\), with
\[
\operatorname{Ric}(g_m)=-g_m.
\]

Let \(K\Subset X_0^\circ\) be the fixed marked ball and buffer. Then
\[
\varepsilon_m
=\|\omega_{\boldsymbol\beta_m}-\omega_{\mathrm{hyp}}\|_{C^2(K)}
\longrightarrow0.
\]
On every lifted copy \(K_{m,j}\), the marked pullback identification gives
\[
\|g_m-g_{\mathrm{CH}}\|_{C^2(K_{m,j})}=\varepsilon_m.
\]
Hence uniformity over all \(d_m\) lifts is exact, not merely a supremum estimate.

### Necessary attribution refinement

BG supplies local smooth convergence on each fixed compact subset of the **base open quotient**. Equality of the discrepancy on every lifted marked region follows from pullback and the covering structure, not from a separate global convergence theorem. No convergence rate is provided or required.

---

## 3. Hurwitz, adjunction, and logarithmic proportionality

Let
\[
L=K_{\bar X_0}+D_0.
\]
For a Galois cover with ramification orders \(v_{m,\lambda}\), Hurwitz gives
\[
K_{\bar X_m}
=\bar\pi_m^*\left(
K_{\bar X_0}
+\sum_\lambda(1-v_{m,\lambda}^{-1})D_\lambda
\right)
=\bar\pi_m^*\left(
L-\sum_\lambda\beta_{m,\lambda}D_\lambda
\right).
\]

The \(D_\lambda\) are disjoint elliptic curves. Adjunction yields
\[
(K_{\bar X_0}+D_\lambda)\cdot D_\lambda=0,
\]
and disjointness gives
\[
L\cdot D_\lambda=0.
\]
Therefore, with \(d_m=\deg\bar\pi_m\) and
\[
A_m=K_{\bar X_m}^2,
\]
one has
\[
\boxed{
\frac{A_m}{d_m}
=L^2+\sum_\lambda \beta_{m,\lambda}^2D_\lambda^2.
}
\]
Since \(D_\lambda^2<0\),
\[
\frac{A_m}{d_m}<L^2,\qquad
\frac{A_m}{d_m}\longrightarrow L^2>0.
\]

For Euler characteristic,
\[
\chi(\bar X_m)
=\chi(X_m^\circ)+\chi(D_m)
=d_m\chi(X_0^\circ),
\]
because every boundary component is elliptic. Logarithmic proportionality gives
\[
L^2=3\chi(X_0^\circ),
\]
hence
\[
\chi(\bar X_m)=\frac{d_mL^2}{3}.
\]
Thus
\[
\boxed{
\Delta_m:=3\chi(\bar X_m)-A_m
=-d_m\sum_\lambda\beta_{m,\lambda}^2D_\lambda^2>0.
}
\]
Consequently,
\[
\frac{\Delta_m}{d_m}\to0,\qquad
\frac{\Delta_m}{A_m}\to0,\qquad
d_m\asymp A_m.
\]

Equivalently, if \(T_m\) denotes the total toroidal boundary in \(\bar X_m\), then
\[
\Delta_m=-T_m^2.
\]
This is exactly Džambić’s compactification formula
\[
c_1^2(\bar X_m)=3c_2(X_m^\circ)+T_m^2.
\]

These formulas are correct as written in Step 31.

---

## 4. Positive-\(r\) towers and Džambić’s formulas

The claim that there exist towers satisfying
\[
\Delta_m\to\infty,\qquad \frac{\Delta_m}{A_m}\to0
\]
is correct, but it should be stated using an explicit level parameter.

Fix the preliminary ideal \(\mathfrak a_0\). Choose an odd rational prime \(p\) inert in \(K\), coprime to the discriminant and to \(\mathfrak a_0\), and set
\[
\mathfrak a_n=\mathfrak a_0(p)^n.
\]
Then
\[
\Gamma_K(\mathfrak a_n)\subset\Gamma_K(\mathfrak a_0),
\]
and the covers are Galois.

Džambić’s inert-prime local index formula gives
\[
I_n=[\Gamma_K:\Gamma_K(\mathfrak a_n)]\asymp p^{8n}.
\]
His boundary formula is
\[
T_{\mathfrak a_n}^2
=-\frac{h_K\eta_K}{\vartheta_{\mathfrak a_n}^{\,2}}\,I_n.
\]
For this tower,
\[
\vartheta_{\mathfrak a_n}
=\vartheta_{\mathfrak a_0}p^n\asymp p^n.
\]
Therefore
\[
\boxed{
\Delta_n=-T_{\mathfrak a_n}^2\asymp p^{6n}\to\infty,
}
\]
while
\[
A_n=3c_2(\bar X_n)-\Delta_n\asymp p^{8n},
\]
so
\[
\boxed{
\frac{\Delta_n}{A_n}\asymp p^{-2n}\to0.
}
\]

Thus the prescribed-\(r\) regime is genuine: for \(0<r<1\), taking
\[
Q_n\sim\frac{\Delta_n}{r}
\]
gives \(Q_n\to\infty\) and \(Q_n=o(A_n)\).

### Required wording correction

“Index has degree-eight level growth” should mean degree eight in a rational prime-power level \(p^n\). Since \(N((p)^n)=p^{2n}\), it is degree four in the ideal norm. For arbitrary ideal levels, these parameters must not be conflated. Restriction to inert primes also avoids possible ambiguity in a literal use of Džambić’s split-prime product notation.

The surgery algebra is correct:
\[
T_+=A-k-4\ell,
\qquad
T_-=\frac A3+\frac{4\Delta}{3}+5k-4\ell.
\]
For
\[
k=\frac{2(Q-\Delta)}9,\qquad
\ell=\frac{7Q}{36}+\frac{\Delta}{18},
\]
one has
\[
k+4\ell=Q,\qquad
T_-=\frac{A+Q}{3}.
\]
After \(O(1)\) rounding,
\[
U_{\mathrm{top}}
=\frac{3\min(T_+,T_-)}A
=1+\frac QA+O(A^{-1})
=1+h+o(h),
\]
because \(Q\to\infty\). Nonnegativity of \(k\) requires \(r\le1\), as reflected in the stated \(0\le r<1\).

---

## 5. Ampleness, minimality, and the actual Seiberg–Witten class

Since \(g_m\) is Kähler and
\[
\operatorname{Ric}(g_m)=-g_m,
\]
its Ricci form gives
\[
[\omega_m]=2\pi c_1(K_{\bar X_m}).
\]
Hence \(K_{\bar X_m}\) is positive and therefore ample by Kodaira. It follows that \(\bar X_m\) is a smooth surface of general type. It is minimal: if \(E\) were a \((-1)\)-curve, adjunction would give
\[
K_{\bar X_m}\cdot E=-1,
\]
contradicting ampleness.

Now set \(X=\bar X_m\), \(A=K_X^2\), and let
\[
c=c_1(X)=-K_X,\qquad c^2=A.
\]
For
\[
M=X\#k\overline{\mathbb{CP}}^{\,2}
  \#\ell(S^1\times S^3)
\]
and a given metric \(g\), put \(H=H_g^+\). Choose signs of the exceptional generators so that
\[
E_i\cdot E_j=-\delta_{ij},\qquad
c\cdot E_i=0,\qquad
c_H^+\cdot E_i\le0.
\]
LeBrun’s Proposition 3.2 and its proof supply an actual Spin\(^c\) structure with determinant class
\[
a_H=c-\sum_{i=1}^kE_i
\]
and nonzero polarization-dependent invariant. For the handle summands, the expected dimension is \(\ell\), and the invariant uses the \(\ell\) degree-one holonomy insertions described by LeBrun. Hence the unperturbed monopole equations are solvable for every \(H\)-adapted metric.

Its self-dual square obeys
\[
\begin{aligned}
p:=(a_H^+)^2
&=(c_H^+)^2
 -2\sum_i c_H^+\cdot E_i
 +\left|\sum_iE_i^+\right|^2 \\
&\ge(c_H^+)^2\ge c^2=A.
\end{aligned}
\]
Also
\[
a_H^2=A-k,
\]
whereas
\[
T_+=2\chi(M)+3\tau(M)=A-k-4\ell.
\]
Therefore
\[
\boxed{
p\ge A,\qquad a_H^2=A-k\ge T_+.
}
\]
These are exactly the hypotheses required by the linear-window theorem.

The exceptional signs may depend on \(g\); that metricwise selection is what LeBrun’s proof provides and what the application needs. Since the Hodge star on two-forms is conformally invariant in dimension four, \(H_g^+\) and the selected Spin\(^c\) structure remain fixed throughout the conformal class.

### The \(b^+=1\) qualification

If \(b^+=1\), nonvanishing must be understood in the polarization-selected chamber; it is not a chamber-independent statement for an arbitrary class. However, in the explicit Picard tower,
\[
\chi(\mathcal O_{\bar X_m})
=\frac{K_{\bar X_m}^2+c_2(\bar X_m)}{12}\to\infty,
\]
so \(p_g\to\infty\), and
\[
b^+=2p_g+1>1
\]
for all sufficiently large \(m\). Thus the chamber issue does not affect the asymptotic sequence, although retaining the chamber-correct statement makes the general formulation valid.

Finally,
\[
\int_M s_g^2\,d\mu_g\ge32\pi^2p\ge32\pi^2A>0,
\]
so Ricci-flat metrics are independently excluded.

---

## Recommended source-exact replacement

A compact formulation is:

> Replace the original quotient by a sufficiently deep neat principal-congruence cover \((X_0^\circ,\bar X_0,D_0)\) containing the prescribed buffered complex-hyperbolic ball. Choose all subsequent principal-congruence subgroups normal in and contained in this fixed subgroup, with ramification orders \(v_{m,\lambda}\to\infty\). BG §4.1 and §4.3 give conic Kähler–Einstein metrics on \((\bar X_0,D_0)\), with cone angles \(2\pi/v_{m,\lambda}\), converging in \(C^\infty_{\mathrm{loc}}(X_0^\circ)\) to the complex-hyperbolic metric; their pullbacks are smooth compact metrics with \(\operatorname{Ric}=-g\). On every lift of the fixed marked region, the \(C^2\) discrepancy is the same and tends to zero. Moreover,
> \[
> \frac{K_{\bar X_m}^2}{d_m}
> =L^2+\sum_\lambda v_{m,\lambda}^{-2}D_\lambda^2,
> \qquad
> 3\chi(\bar X_m)-K_{\bar X_m}^2
> =-d_m\sum_\lambda v_{m,\lambda}^{-2}D_\lambda^2.
> \]
> For an inert-prime-power Picard tower, Džambić’s formulas yield
> \[
> \Delta_m\asymp p^{6m},\qquad A_m\asymp p^{8m},
> \qquad \Delta_m/A_m\to0.
> \]
> The pulled-back negative Kähler–Einstein metric makes \(K_{\bar X_m}\) ample. LeBrun’s polarized blow-up/handle construction then supplies, for every metric on the surgically modified manifold, a conformally actual Spin\(^c\) class satisfying
> \[
> (a_H^+)^2\ge A_m,\qquad a_H^2=A_m-k_m\ge T_{+,m}.
> \]

No theorem-level defect remains in the checked background or actual-field components after these qualifications.
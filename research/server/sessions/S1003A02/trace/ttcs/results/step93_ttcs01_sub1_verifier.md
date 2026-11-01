# TTCS Independent Branch Record

```json
{
  "step_id": 93,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Sessions/S1003A01/workspace/scripts/step74_neck_and_screen.py",
    "Sessions/S1003A01/workspace/data/step74/neck_and_screen.json",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/state_of_problems_1_4.md",
    "Knowledge/objects/papers/Ricci-Curvature-Minimal-Volumes-and-Seiberg-Witten-Theory--995c93498a8f--cab40be18df4/object.md",
    "Knowledge/objects/papers/Kodaira-dimension-and-the-Yamabe-problem--d0edcef7bc67--1bd338503143/object.md"
  ]
}
```

## Task

Independently verify the mathematical correctness and exact scope of A01 Step-74 Theorem 74.A. Check: transfer of the smooth scalar-curvature lower bound through arbitrary A1 orbifold resolution; all characteristic-number normalizations; the weighted-mean lower bound for the human defect; the Green-football cap construction and its topology/asymptotics; exact values of P_{*,orb} and alpha_orb; equality and nonattainment statements; and what this genuinely supersedes in A02 Theorem 87.O. Pay special attention to whether the scalar lower bound needs the stated SW supply or follows unconditionally for general-type blowups from the Yamabe invariant, and to fake-projective-plane/b^+=1 scope. Give precise corrections if needed.

## Output

# Scientific verification memo: Step-74 Theorem 74.A

## 1. Overall assessment

Subject to the smooth identification

\[
(R)\qquad \operatorname{Res}\!\left(S^{4}/\mathbb Z _2\right)
\cong \overline{\mathbb{CP}}^{\,2}\#\overline{\mathbb{CP}}^{\,2}
\]

with the two \(A_{1}\) points resolved by orientation-matched Eguchi–Hanson spaces, the two principal formulas are correct:

\[
P_{*,\mathrm{orb}}(V_m)=8\pi ^2k,
\qquad
\alpha_{\mathrm{orb}}(V_m)
=\min\left\{1,\frac{4k}{A+k}\right\},
\quad k=2m.
\]

The resulting exclusion of Einstein orbifold metrics on \(V_m\) for every \(m\ge1\) is also correct.

A substantive strengthening is available: the stated metric-wise SW hypothesis is not needed for these three conclusions. The scalar estimate follows from the exact Yamabe invariant of the smooth resolution \(M_k\), and this includes fake projective planes. The transferred mixed Weyl–scalar estimate used in the equality discussion is likewise available for \(b^{+}=1\) through the argument of LeBrun 2001, Proposition 3.2 together with Theorem 2.3; the chamber reasoning should be cited directly rather than left as an unresolved fake-plane exception.

The characteristic-number arithmetic, weighted-mean argument, football cap energy, gluing orders, and nonattainment statement for \(k>A/3\) all agree.

---

## 2. Scalar-curvature transfer: the SW assumption is unnecessary

LeBrun’s Yamabe theorem for every compact complex surface of general type and all its blow-ups gives

\[
\mathcal Y(M_k)=-4\pi\sqrt{2A},
\qquad
M_k=X\#k\overline{\mathbb{CP}}^{\,2}.
\]

This is Theorem 2 of *Kodaira Dimension and the Yamabe Problem*. It applies to all Kähler-type general-type surfaces, including the \(b^{+}=1\) case. In particular, it applies when \(X\) is a fake projective plane.

For any smooth metric \(\widetilde g\) on \(M_k\),

\[
-\|s_{\widetilde g}^{-}\|_{2}
\le Y([\widetilde g])
\le \mathcal Y(M_k)
=-4\pi\sqrt{2A},
\]

and therefore

\[
\int_{M_k}(s_{\widetilde g}^{-})^{2}\,d\mu_{\widetilde g}
\ge 32\pi ^2A.
\tag{2.1}
\]

Now resolve an arbitrary smooth orbifold metric \(g\) on \(V_m\) by scaled Eguchi–Hanson metrics. Lemma 86.S gives bounded curvature on the transition annuli, volume \(O(\rho ^4)\), scalar curvature zero on the exact EH pieces, and equality with \(g\) away from shrinking orbifold balls. Consequently one has the stronger convergence

\[
\int_{M_k}(s_{g_\varepsilon}^{-})^{2}\,d\mu_{g_\varepsilon}
\longrightarrow
\int_{V_m}(s_g^{-})^{2}\,d\mu_g.
\]

Passing (2.1) to the limit gives

\[
\boxed{\int_{V_m}(s_g^{-})^{2}\,d\mu_g\ge32\pi ^2A.}
\tag{2.2}
\]

In particular,

\[
S(g)=\int_{V_m}s_g^2\,d\mu_g\ge32\pi ^2A.
\]

Thus:

* no extra metric-wise monopole supplier is needed for the scalar estimate;
* no \(b^{+}\ge2\) hypothesis enters;
* fake projective planes are included;
* the transferred result is actually (2.2), which is stronger than the displayed estimate for \(S\).

This stronger form is useful in the equality discussion: if \(S=32\pi ^2A\), then necessarily \(s\le0\) everywhere.

---

## 3. Characteristic numbers and curvature normalizations

The normalization

\[
16\pi ^2\chi_{\rm orb}
=\frac{S}{12}+2(I_++I_-)-P,
\qquad
12\pi ^2\tau_{\rm orb}=I_+-I_-
\]

is consistent with the session tensor conventions.

For a compact ball quotient \(X\),

\[
\chi(X)=\frac A3,\qquad \tau(X)=\frac A9.
\]

For \(O=S^{4}/\mathbb Z _2\) with its two isolated \(A_1\) points,

\[
\chi_{\rm orb}(O)=1,\qquad \tau_{\rm orb}(O)=0.
\]

The signature \(\eta\)-term of \(L(2,1)=\mathbb{RP}^{3}\) is zero. Since orbifold connected sum at a regular point subtracts \(2\) from the Euler characteristic,

\[
\chi_{\rm orb}(V_m)=\frac A3-m=\frac A3-\frac k2,
\qquad
\tau_{\rm orb}(V_m)=\frac A9.
\tag{3.1}
\]

Hence

\[
T_+(V_m)=2\chi_{\rm orb}+3\tau_{\rm orb}=A-k,
\]

\[
T_-(V_m)=2\chi_{\rm orb}-3\tau_{\rm orb}=\frac A3-k.
\tag{3.2}
\]

For the smooth resolution,

\[
\chi(M_k)=\frac A3+k,\qquad
\tau(M_k)=\frac A9-k,
\]

so

\[
T_+(M_k)=A-k,\qquad
T_-(M_k)=\frac A3+5k.
\]

A complex-oriented EH space has

\[
(c_+,c_-)=(0,-6).
\]

There are \(k=2m\) EH spaces, so \(C_+=0\), \(C_-=-6k\), and indeed

\[
T_-(V_m)=T_-(M_k)+C_-
=\frac A3+5k-6k=\frac A3-k.
\]

Thus the general charge ledger and the direct orbifold computation agree exactly.

The signature identity from (3.1) gives

\[
I_+-I_-=12\pi ^2\frac A9=\frac{4\pi ^2A}{3},
\]

and therefore

\[
W:=I_++I_-\ge \frac{4\pi ^2A}{3}.
\tag{3.3}
\]

Set

\[
\sigma=S-32\pi ^2A\ge0,\qquad
w=W-\frac{4\pi ^2A}{3}\ge0.
\]

Substitution into orbifold Gauss–Bonnet yields

\[
\boxed{P=8\pi ^2k+\frac{\sigma}{12}+2w.}
\tag{3.4}
\]

Since \(R=P+S/4\),

\[
\boxed{R=8\pi ^2(A+k)+\frac{\sigma}{3}+2w.}
\tag{3.5}
\]

All coefficients in Step 74.A are therefore correct.

---

## 4. Weighted-mean lower estimate for \(\mathscr D\)

From (3.4)–(3.5),

\[
\frac{4P}{R}
=
\frac{
\frac{4k}{A+k}\,[8\pi ^2(A+k)]
+1\cdot\frac{\sigma}{3}
+4\cdot 2w
}{
8\pi ^2(A+k)+\frac{\sigma}{3}+2w
}.
\tag{4.1}
\]

This is exactly a weighted mean of

\[
\frac{4k}{A+k},\qquad 1,\qquad 4
\]

with weights

\[
8\pi ^2(A+k),\qquad \frac{\sigma}{3},\qquad 2w.
\]

Since

\[
\mathscr D(g)=\frac{4P+L_s}{R}\ge \frac{4P}{R},
\]

one obtains

\[
\boxed{
\mathscr D(g)\ge
\min\left\{1,\frac{4k}{A+k}\right\}.
}
\tag{4.2}
\]

Also, (3.4) gives

\[
P(g)\ge8\pi ^2k>0.
\]

An Einstein orbifold metric has \(P=0\), so none exists on \(V_m\) for any \(m\ge1\). This conclusion uses only the Yamabe transfer, signature, and orbifold Gauss–Bonnet.

---

## 5. Green-football cap

### 5.1 Exact energy

For

\[
h=(1+r^{-2})^{2}\delta
\quad\text{on }\mathbb R^{4}\setminus\{0\},
\]

the conformal factor is harmonic, hence \(s_h=0\), and conformal flatness gives \(W_h=0\).

A direct warped-product computation gives

\[
|\operatorname{Ric}^{\circ}_h|^2
=
\frac{192r^8}{(1+r^2)^8},
\]

\[
d\mu_h
=
2\pi ^2\frac{(1+r^2)^4}{r^5}\,dr.
\]

Thus the radial energy density is

\[
|\operatorname{Ric}^{\circ}_h|^2d\mu_h
=
384\pi ^2\frac{r^3}{(1+r^2)^4}\,dr,
\]

and

\[
P(h)=32\pi ^2.
\]

Moreover,

\[
\int_{r>R}|\operatorname{Ric}^{\circ}_h|^2d\mu_h
=
\frac{\pi ^2(96R^2+32)}{(R^2+1)^3}
=
\frac{96\pi ^2}{R^4}+O(R^{-6}),
\]

while

\[
|\operatorname{Ric}^{\circ}_h|
=
\frac{8\sqrt3\,r^4}{(1+r^2)^4}
=
8\sqrt3\,r^{-4}+O(r^{-6}).
\]

These formulas agree with the script and JSON.

### 5.2 The involution and orbifold topology

Let

\[
\iota(x)=\frac{\sigma x}{|x|^2},
\qquad
\sigma=\operatorname{diag}(-1,-1,-1,1).
\]

Inversion contributes the pullback factor \(r^{-4}\), and the conformal factor transforms so that \(\iota^{*}h=h\). The fixed-point equation gives exactly

\[
x=(0,0,0,\pm1).
\]

At both points,

\[
D\iota=-I,
\]

so their quotient models are \(A_1\) singularities. The map exchanges \(r\to0\) and \(r\to\infty\), and therefore the quotient has one ordinary AE end. Compactifying the exchanged pair of ends produces one regular point; the compactified quotient is \(S^{4}/\mathbb Z _2\) with the two displayed \(A_1\) points.

Since the action has degree two away from two measure-zero fixed points,

\[
P(G)=\frac12P(h)=16\pi ^2.
\]

For \(R>1\), the quotient end is represented one-to-one by \(r>R\), so the quoted tail formula applies directly to the omitted end of \(G\).

### 5.3 Gluing orders

In host normal coordinates,

\[
g_X-\delta=O(|y|^2),
\]

with

\[
|\partial^j(g_X-\delta)|\lesssim \rho^{2-j},
\qquad j\le2.
\]

After scaling \(G\) by \(\varepsilon^2\) and writing \(y=\varepsilon x\), its end is

\[
\left(1+\frac{\varepsilon^2}{|y|^2}\right)^2\delta,
\]

so

\[
|\partial^j(g_{\rm cap}-\delta)|
\lesssim \varepsilon^2\rho^{-2-j},
\qquad j\le2.
\]

With \(\rho=\varepsilon^{1/2}\), both second-derivative contributions are \(O(1)\). Hence transition curvature is \(O(1)\) on volume

\[
O(\rho^4)=O(\varepsilon^2).
\]

The omitted cap tail is

\[
O\!\left((\varepsilon/\rho)^4\right)=O(\varepsilon^2).
\]

For \(m\) disjoint insertions,

\[
P(g_\varepsilon)\to16\pi ^2m=8\pi ^2k,
\]

\[
S(g_\varepsilon)\to32\pi ^2A,
\qquad
W(g_\varepsilon)\to\frac{4\pi ^2A}{3},
\]

and, because the scalar-flat cap and transition regions have shrinking volume,

\[
L_s(g_\varepsilon)\to0.
\]

Therefore

\[
\mathscr D(g_\varepsilon)
\longrightarrow
\frac{4(8\pi ^2k)}{8\pi ^2(A+k)}
=
\frac{4k}{A+k}.
\tag{5.1}
\]

The inserted piece is \(O\) minus a regular ball, so the resulting orbifold is \(X\#mO=V_m\).

### 5.4 The value \(1\)

On a unit product cylinder \(S^3\times[0,L]\),

\[
s=6,\qquad |\operatorname{Ric}|^2=12,\qquad
|\operatorname{Ric}^{\circ}|^2=3.
\]

Thus both \(4P\) and \(R\) have leading term

\[
24\pi ^2L,
\]

while the scalar variance stays \(O(1)\): the average scalar tends to \(6\), and all fixed transition pieces have bounded volume. Hence

\[
\mathscr D\to1.
\]

The cylinder can be inserted at a regular orbifold point without changing the singularity data.

Combining this family with (5.1) proves both exact infima.

---

## 6. Equality and attainment

### 6.1 A \(P\)-minimizer

If

\[
P=8\pi ^2k,
\]

then (3.4) forces

\[
\sigma=0,\qquad w=0.
\]

Therefore

\[
S=32\pi ^2A,\qquad
W=\frac{4\pi ^2A}{3}.
\]

Together with the signature identity,

\[
I_-=0,\qquad I_+=\frac{4\pi ^2A}{3},
\]

so

\[
W^-\equiv0.
\]

The stronger scalar transfer (2.2), combined with \(S=32\pi ^2A\), gives directly

\[
s\le0.
\tag{6.1}
\]

For complex-oriented EH fillers, \(W^+=0\), so the transferred mixed inequality is

\[
\int_{V_m}(s-\sqrt6|W^+|)^2\ge72\pi ^2A.
\tag{6.2}
\]

Using (6.1),

\[
\int(s-\sqrt6|W^+|)^2
=
\int(|s|+\sqrt6|W^+|)^2.
\]

Minkowski gives

\[
\int(|s|+\sqrt6|W^+|)^2
\le
\left(\sqrt S+\sqrt{6I_+}\right)^2
=72\pi ^2A.
\]

Thus equality holds throughout. Equality in Minkowski implies

\[
\sqrt6|W^+|=\frac12|s|,
\]

hence

\[
\boxed{
W^-=0,\qquad s\le0,\qquad |W^+|^2=\frac{s^2}{24}.
}
\]

Since \(P=8\pi ^2k>0\), the metric is not Einstein. These identities determine only the norm of the \(W^+\) block, not its three eigenvalues.

### 6.2 An \(\alpha_{\rm orb}\)-minimizer

* If \(k<A/3\), then \(4k/(A+k)<1\). Equality in the weighted mean requires

  \[
  \sigma=w=0,
  \]

  and equality in \(\mathscr D\ge4P/R\) requires \(L_s=0\). Hence \(s\) is constant, and (2.2) makes it strictly \(<0\).

* If \(k=A/3\), the two first weighted values in (4.1) are both \(1\). Equality \(\mathscr D=1\) requires

  \[
  w=0,\qquad L_s=0,
  \]

  but does not require \(\sigma=0\). The constant scalar curvature is again strictly \(<0\), by (2.2).

* If \(k>A/3\), the fixed weight \(8\pi ^2(A+k)\) multiplies a value \(4k/(A+k)>1\), while the other weighted values are \(1\) and \(4\). Therefore every individual metric satisfies

  \[
  \frac{4P}{R}>1,
  \qquad
  \mathscr D>1.
  \]

  Since the cylinder family has \(\mathscr D\to1\),

  \[
  \alpha_{\rm orb}(V_m)=1
  \]

  and it is not attained.

The last sentence of Step 74 should distinguish the two variational problems: \(\alpha_{\rm orb}\)-attainment is unsettled for \(k\le A/3\), while \(P_{*,\rm orb}\)-attainment is not settled by this argument for any \(k\).

---

## 7. Fake projective planes and the mixed estimate

For the exact values of \(P_{*,\rm orb}\), \(\alpha_{\rm orb}\), and the Einstein exclusion, fake projective planes require no separate treatment because the Yamabe theorem already supplies (2.2).

For the pointwise equality description, the required smooth estimate is

\[
\int_{M_k}(s-\sqrt6|W^+|)^2\ge72\pi ^2A.
\tag{7.1}
\]

LeBrun 2001, Theorem 2.3 gives

\[
\int\left(\frac23s-2\sqrt{\frac23}|W^+|\right)^2
\ge32\pi ^2(a^+)^2,
\]

which is exactly (7.1) when \((a^+)^2\ge A\). Proposition 3.2 and its proof select the required signed blow-up class for each metric. The source explicitly notes that \(A>0\) keeps the relevant polarization under control even when \(b^+=1\).

Thus the parenthetical statement in Step 74 that the chamber issue remains confined to fake projective planes should be replaced by a direct citation to this all-\(b^+\) argument. For \(b^+=1\), one should phrase the input as a metric-wise choice of Spin\(^c\) class rather than as one fixed chamber-independent monopole class. No convergence of these classes is needed in the orbifold transfer.

---

## 8. Relation to Theorem 87.O

The cap family also gives

\[
\inf_{\mathscr G_{\rm orb}(V_m)}W=\frac{4\pi ^2A}{3}.
\]

Therefore

\[
\begin{aligned}
d_{*,\rm orb}(V_m)
&=
8\pi ^2\chi_{\rm orb}(V_m)
-\inf W\\
&=
8\pi ^2\left(\frac A3-\frac k2\right)
-\frac{4\pi ^2A}{3}\\
&=
4\pi ^2\left(\frac A3-k\right)
=
4\pi ^2\left(\frac A3-2m\right).
\end{aligned}
\]

This reproduces Theorem 87.O exactly.

Step 74.A adds three facts not contained in the Weyl-deficit computation:

1. the scalar budget \(\int(s^-)^2\ge32\pi ^2A\);
2. the exact trace-free Ricci infimum \(8\pi ^2k\);
3. the exact human defect and its nonattainment for \(k>A/3\).

Most importantly, Theorem 87.O only implied that an Einstein metric would require \(k<A/3\). The scalar transfer combined with Gauss–Bonnet removes all \(k\ge1\) on this particular paired-\(A_1\) orbifold.

The absolute deficit formula of 87.O remains useful and unchanged. Step 74.A does not turn the orbifold estimate into a lower estimate for smooth metrics on \(M_k\); the supplied finite-scale Burns construction gives \(P_*(M_k)<8\pi ^2k\). It also says nothing by itself about other orbifold topologies or other ALE charge patterns.

## 9. Precise revised formulation

A clean formulation is:

> Let \(X\) be any compact ball quotient, including a fake projective plane, and let \(V_m=X\#m(S^4/\mathbb Z _2)\), \(k=2m\). Assume the supplied smooth identification (R). Then, without any extra SW hypothesis,
> \[
> P_{*,\rm orb}(V_m)=8\pi ^2k,\qquad
> \alpha_{\rm orb}(V_m)=\min\left\{1,\frac{4k}{A+k}\right\},
> \]
> and \(V_m\) admits no Einstein orbifold metric.  
> The displayed structure of a \(P\)-minimizer follows from the metric-wise LeBrun mixed estimate, which is available for all these \(X\), including \(b^+=1\), by LeBrun 2001, Theorem 2.3 and Proposition 3.2.

This is the mathematically strongest version supported by the supplied derivations and sources.
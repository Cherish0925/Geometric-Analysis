# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 32,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step32_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step32_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the upper-construction and normalization part of the revised ramified KE transfer. Check the exact physical radius of the certified x0=.03, X=128 cell after scaling to Ric=-g; the fixed-buffer interpolation g_CH+chi(g_m-g_CH), its positivity and C^2/Ricci/volume/scalar estimates; how those errors enter the complete-cell formula at the Q=o(A) scale; the separated shrinking-handle contribution; integer rounding under Delta/Q→r∈[0,1); and the coefficient limsup alpha/h <= 4-(8 eta/9)(1-r), including the distinction between a diagonal smoothing sequence and a fixed reduced margin. Check also that the statement is only an upper construction law and not an optimality or r=1 transition theorem. Identify any missing quantifier or mismatch between the rigorous certificate and the geometric marked-ball hypothesis.

## Integrated Scientific Memo

# Verification memo: ramified KE upper transfer

## 1. Radius and normalization

For the complex-hyperbolic model in the cell coordinates,
\[
g_{CH,\mathrm{rad}}=\frac{dx^2}{4x(1+x)}.
\]
Putting \(x=\sinh^2\rho\) gives \(g_{CH,\mathrm{rad}}=d\rho^2\). Hence the level \(x=X\) is at radius
\[
\rho_X=\operatorname{arsinh}\sqrt X
\]
in the normalization \(\operatorname{Ric}=-6g\).

After scaling \(\widetilde g=6g\), one has
\[
\operatorname{Ric}_{\widetilde g}=-\widetilde g,
\]
and distances are multiplied by \(\sqrt6\). Therefore
\[
\boxed{
R_{128}=\sqrt6\,\operatorname{arsinh}\sqrt{128}
=\sqrt6\log(\sqrt{128}+\sqrt{129})
=7.64512629467772\ldots .
}
\]
The value near \(4.32\) belongs to \(X=8\), not \(X=128\). The parameter \(x_0=.03\) controls the bolt location of the replacement cell but does not enter the ambient marked CH-ball radius, whose center is \(x=0\).

The defect normalization is unchanged:
\[
\int |\operatorname{Ric}_{6g}+6g|_{6g}^{2}\,dV_{6g}
=
\int |\operatorname{Ric}_{g}+6g|_{g}^{2}\,dV_g.
\]
Thus a certificate for \(J_6/(8\pi^2)\) transfers directly to \(J_1/(8\pi^2)\).

The marked compact set must contain the closed ball of radius \(R_{128}\) plus the entire fixed interpolation buffer. If the buffer has physical width \(b>0\), the preliminary cover must exclude all nonidentity elements moving the chosen lift by at most \(2(R_{128}+b)\), not merely \(2R_{128}\).

---

## 2. Fixed-buffer interpolation

Let
\[
h_m=g_m-g_{CH},\qquad
\|h_m\|_{C^2(K)}\le\varepsilon_m\to0
\]
on the fixed marked ball and buffer, and choose \(0\le\chi\le1\), equal to \(0\) on the inner subannulus and \(1\) on the outer one. Set
\[
g_{m,\mathrm{ann}}=g_{CH}+\chi h_m
=(1-\chi)g_{CH}+\chi g_m.
\]

### Positivity

Because this is a convex combination of positive-definite tensors, it is positive definite for every \(m\), not merely for sufficiently large \(m\). If one does not impose \(0\le\chi\le1\), eventual positivity still follows from \(C^0\)-closeness.

### Two-jet and curvature estimates

The annulus and cutoff are fixed, so
\[
\|g_{m,\mathrm{ann}}-g_{CH}\|_{C^2}
\le C_\chi\varepsilon_m.
\]
On a uniformly elliptic neighborhood of \(g_{CH}\), the Ricci tensor is locally Lipschitz as a function of the metric two-jet. Since
\[
\operatorname{Ric}(g_{CH})+g_{CH}=0,
\]
one obtains
\[
\|\operatorname{Ric}(g_{m,\mathrm{ann}})
     +g_{m,\mathrm{ann}}\|_{C^0}
\le C\varepsilon_m.
\]
The buffer has fixed volume, hence
\[
\int_{\mathrm{ann}}
|\operatorname{Ric}(g_{m,\mathrm{ann}})
       +g_{m,\mathrm{ann}}|^2\,dV
=O(\varepsilon_m^2).
\]

Likewise,
\[
dV_{g_{m,\mathrm{ann}}}-dV_{CH}=O(\varepsilon_m),
\qquad
s_{g_{m,\mathrm{ann}}}+4=O(\varepsilon_m),
\]
and therefore
\[
\Delta V_{\mathrm{ann}}=O(\varepsilon_m),\qquad
\Delta\!\int s\,dV=O(\varepsilon_m).
\]

The same \(O(\varepsilon_m)\) volume and scalar-moment comparison is needed for the whole removed \(g_m\)-region relative to the CH reference region, not only for the transition annulus.

Across \(k_m=O(Q_m)\) cell sites,
\[
O(k_m\varepsilon_m^2)=o(Q_m),\qquad
O(k_m\varepsilon_m)=o(Q_m),
\]
because \(\varepsilon_m\to0\). No rate such as \(Q_m\varepsilon_m\to0\) is required.

The untouched exterior is exactly Einstein, so it contributes zero raw defect. In particular there is no \(A_m\varepsilon_m^2\) term.

### Uniformity over the growing collection of lifts

The needed estimate is uniform over all selected lifts. This follows if \(g_m\) is literally the pullback of one downstairs conical KE metric: every lifted marked ball then has the same discrepancy
\[
\|g_m-g_{CH}\|_{C^2(K)}=\varepsilon_m.
\]
Bare compact convergence on varying manifolds would not by itself control the maximum discrepancy over a growing set of lifts.

---

## 3. Exact complete-cell accounting

For a constructed metric write
\[
V=\operatorname{Vol}(g),\qquad
I=\int s_g\,dV_g,\qquad
D=\int|\operatorname{Ric}_g+g|^2\,dV_g,
\]
and put
\[
T=I+4V.
\]
Since
\[
D=\int|\operatorname{Ric}|^2+2I+4V,
\]
we have
\[
\int|\operatorname{Ric}|^2=D+4V-2T,\qquad I=T-4V.
\]
Consequently
\[
\boxed{
\mathcal E(g)
=4-\frac{I^2}{V\int|\operatorname{Ric}|^2}
=\frac{4D-T^2/V}{4V+D-2T}.
}
\]

For the negative KE background,
\[
V_m^0=\frac12(2\pi c_1(K_{\bar X_m}))^2
=2\pi^2A_m.
\]
After all surgeries,
\[
V_m=2\pi^2A_m+O(Q_m),\qquad T_m=O(Q_m),
\]
and
\[
D_m=k_mJ_{1,m}+32\pi^2\ell_m+o(Q_m).
\]
Here the \(o(Q_m)\) includes the cell-buffer defects and shrinking-handle excesses.

Because \(Q_m=o(A_m)\),
\[
\frac{T_m^2}{V_m}
=O\!\left(\frac{Q_m^2}{A_m}\right)
=o(Q_m),
\]
and
\[
4V_m+D_m-2T_m=8\pi^2A_m+O(Q_m).
\]
Thus
\[
\mathcal E(g_m^{\mathrm{constr}})
=
\frac{D_m}{2\pi^2A_m}
+o(Q_m/A_m),
\]
so, with \(h_m=Q_m/A_m\),
\[
\boxed{
\frac{\alpha(M_m)}{h_m}
\le
\frac{k_mJ_{1,m}+32\pi^2\ell_m}{2\pi^2Q_m}
+o(1).
}
\]

This calculation explains why the volume and scalar-moment changes do not alter the first coefficient: their linear effects cancel, while \(T_m^2/V_m=o(Q_m)\).

Strictly speaking, only the defect excess must be \(o(Q_m)\). Uniform \(O(Q_m)\) control of volume and scalar moment would already suffice. The stronger \(o(Q_m)\) estimates stated in Step 31 are nevertheless valid because \(\varepsilon_m\to0\).

---

## 4. Separated shrinking handles

The pure-handle exact-CH infimum supplied by Step 11 is
\[
\inf J_{\mathrm{handle}}=32\pi^2\ell,
\]
approached, but not attained by a fixed smooth handle cell, as the handle cores shrink.

Choose the scale on the \(m\)-th manifold so that the per-handle excess \(e_m\to0\). Since \(\ell_m=O(Q_m)\),
\[
D_{\mathrm{handles}}
=32\pi^2\ell_m+O(\ell_me_m)
=32\pi^2\ell_m+o(Q_m).
\]
The aggregate handle volume and scalar-moment changes can simultaneously be made \(o(Q_m)\). Each metric remains smooth because its scale is positive for every fixed \(m\).

If desired, the inherited CH handle construction can be inserted after first interpolating a marked background ball to an exact CH subregion. The additional per-site buffer defect is then \(O(\varepsilon_m^2)\).

The required number of sites is
\[
k_m+\ell_m=O(Q_m)=o(A_m),
\]
whereas the number of marked lifts is comparable to \(A_m\), so site availability is sufficient.

---

## 5. Integer rounding and topology

Begin with an integer target \(\widehat Q_m\) satisfying
\[
\widehat Q_m\to\infty,\qquad
\widehat Q_m=o(A_m),\qquad
\frac{\Delta_m}{\widehat Q_m}\to r\in[0,1).
\]
The real balanced solution is
\[
k_m^*=\frac{2(\widehat Q_m-\Delta_m)}9,\qquad
\ell_m^*=\frac{7\widehat Q_m+2\Delta_m}{36}.
\]

A clean integer realization is either:

1. round \(k_m^*,\ell_m^*\) independently and then define
   \[
   Q_m=k_m+4\ell_m=\widehat Q_m+O(1);
   \]
   or

2. keep \(Q_m=\widehat Q_m\) exactly, choose \(k_m\equiv Q_m\pmod4\) nearest to \(k_m^*\), and set
   \[
   \ell_m=\frac{Q_m-k_m}{4}.
   \]

In both cases,
\[
16\ell_m-14k_m-4\Delta_m=O(1),
\]
and
\[
\frac{k_m}{Q_m}\to\frac{2(1-r)}9,\qquad
\frac{\ell_m}{Q_m}\to\frac{7+2r}{36}.
\]
Since \(r<1\), both surgery numbers are eventually nonnegative, with \(k_m>0\).

The topology then gives
\[
T_{+,m}=A_m-Q_m,
\]
and, if
\[
b_m=16\ell_m-14k_m-4\Delta_m,
\]
\[
T_{-,m}
=\frac{A_m+Q_m}{3}-\frac{b_m}{3}
=\frac{A_m+Q_m}{3}+O(1).
\]
Since \(Q_m=o(A_m)\), \(T_-\) is the smaller term for large \(m\), so
\[
\frac{3\min(T_{+,m},T_{-,m})}{A_m}
=1+h_m+O(A_m^{-1})
=1+h_m+o(h_m).
\]
The last equality uses
\[
\frac{A_m^{-1}}{h_m}=\frac1{Q_m}\to0.
\]

Step 31’s algebra is correct, but its wording is mildly circular because it first defines \(Q_m=k_m+4\ell_m\) and then rounds a real solution expressed using \(Q_m\). One of the two conventions above should be stated explicitly.

---

## 6. Coefficient and smoothing quantifiers

If
\[
\frac{J_{1,m}}{8\pi^2}\le1-\eta+o(1),
\]
then
\[
\begin{aligned}
\limsup_m\frac{\alpha(M_m)}{h_m}
&\le
4(1-\eta)\frac{2(1-r)}9
+16\frac{7+2r}{36}\\
&=
\boxed{
4-\frac{8\eta}{9}(1-r).
}
\end{aligned}
\]
Thus the symbolic coefficient in `step32_ramified_transfer_law.py` is correct.

With the recorded numerical upper value
\[
U=0.9956710815089548,\qquad
\eta=1-U=0.004328918491045219,
\]
the \(r=0\) coefficient is
\[
4-\frac{8\eta}{9}
=3.996152072452404\ldots .
\]

### Diagonal smoothing sequence

If the certified profile is only \(C^2\) at the exact matching sphere, let \(g_{\delta}\) be a smooth flat-cutoff version with
\[
J(g_\delta)\to J(g).
\]
Choosing \(\delta_m\to0\), together with handle scales tending to zero and \(\varepsilon_m\to0\), yields one diagonal sequence satisfying the endpoint coefficient with the full certified \(\eta\).

### One fixed smooth cell

For any chosen \(0<\eta'<\eta\), continuity provides a sufficiently small fixed smoothing width such that
\[
J(g_\delta)\le8\pi^2(1-\eta').
\]
Replication of this fixed cell gives
\[
\limsup_m\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta'}9(1-r)<4.
\]

A fixed smoothing or a fixed nonsymmetric perturbation has some uniform positive margin; it need not mathematically be smaller than \(\eta\), because the energy variation has no known sign. Describing it by a prescribed conservative \(\eta'<\eta\) is safe, but “necessarily smaller” is too strong.

---

## 7. Gaps between the supplied \(X=128\) certificate and the geometric hypothesis

The file `rigorous_x00.03_X128_d20.json` certifies an integral enclosure but is not, by itself, a complete geometric certificate for the replacement cell. Its referenced profile file was not supplied. The available material therefore does not independently establish for the \(x_0=.03,\ X=128\), degree-20 profile:

1. the exact profile and integrand normalization;
2. positivity throughout the cell;
3. the ordinary \((-1)\)-sphere bolt conditions at \(x=x_0\);
4. the relative topology \(D\#\overline{\mathbb{CP}}^2\);
5. third-order or otherwise adequate matching to CH at \(x=128\);
6. the smoothing estimate producing a smooth exact-CH collar;
7. use of the corrected strict-Arb implementation whose Taylor-tail bounds avoid float mediation.

The older \(x_0=.01,\ X=8\) documents prove analogous facts for a different profile; they cannot substitute for the missing \(X=128\) admissibility record. Hence the transfer theorem is rigorous conditional on those geometric facts for the degree-20 profile.

There is also a precision/provenance issue. The serialized proof ball is displayed only as
\[
[0.99567\pm1.09\times10^{-6}],
\]
which directly supports the coarser bound
\[
J/(8\pi^2)\le0.99567109
\]
and consequently a coefficient around \(3.99615208\). The sharper decimal
\[
0.9956710815089548
\]
appears in a binary64 convenience field. To certify the displayed ninth-digit statement
\[
<3.996152073,
\]
one should record the outward-rounded Arb upper endpoint at sufficient precision. This does not affect the strict inequality below \(4\).

Additional geometric quantifiers that should be explicit are:

- the compact convergence set contains \(\overline B(R_{128}+b)\);
- it lies compactly inside the open ball quotient, away from cusp divisors;
- all cusp ramification indices tend to infinity, in the required vector-parameter sense;
- the pullback is smooth for each reciprocal ramification angle;
- for \(r>0\), the selected tower has \(\Delta_m\to\infty\);
- degree and lift counts are measured relative to the post-preliminary cover. If degree is measured from the original quotient, the number of lifts differs by a fixed preliminary-cover factor, harmless asymptotically but not literally equal to \(d_m\).

---

## 8. Scope of the result

What is verified is the existential upper construction law
\[
\boxed{
\limsup_m\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta}{9}(1-r),
\qquad 0\le r<1,
}
\]
for a suitably chosen ramified tower, the balanced rounded surgery proportions, replicated single-blowup cells, and separated shrinking handles.

It is not:

- a matching lower bound;
- a determination of the optimal first coefficient;
- an exclusion of cheaper mixed cells or unrestricted global metrics;
- a statement for every preassigned ramified tower;
- a transition theorem at \(r=1\).

At \(r=1\), the balanced blowup fraction tends to zero and this particular saving disappears algebraically. Moreover, \(\Delta_m/Q_m\to1\) alone does not ensure eventual \(Q_m\ge\Delta_m\), needed for \(k_m\ge0\). Thus the construction neither proves a value nor a phase transition at \(r=1\).

Subject to the missing \(X=128\) admissibility/provenance record, the normalization, interpolation, complete-cell expansion, handle accounting, rounding law, and coefficient formula are mutually consistent.
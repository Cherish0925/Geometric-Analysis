# TTCS Independent Branch Record

```json
{
  "step_id": 74,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step74_packing_weyl_theorem_and_scope.md",
    "Sessions/S1003A02/workspace/scripts/step74_certified_weyl_saving.py",
    "Sessions/S1003A02/workspace/data/step74_weyl_x003_X128.json",
    "Sessions/S1003A02/workspace/data/step74_weyl_x001_X8.json",
    "Sessions/S1003A02/workspace/notes/step72_orientation_free_weyl_deficit_law.md",
    "Sessions/S1003A02/workspace/notes/step69_P_form_upper_law_balanced_towers.md",
    "Skills/geometric-analysis/research/supplements/20261007-einstein-gaps/web_research_collected.tex"
  ]
}
```

## Task

Independently verify the new Step-74 theorem and numerical normalization. Check: (i) the relative Chern–Weil coefficient and subtraction of the missing CH core 3 x0^2; (ii) the interval outputs for both certified cells; (iii) the mixed closed-manifold implication d >= 4π²(A/3-k+eta n) and its cover/packing quantifiers; (iv) the CH Ric=-g ball-volume formula and the resulting beta0 and footprint efficiencies; (v) the fixed-complex Kähler Hodge-index comparison and its relation to the h=1/3 frontier; (vi) the algebraic capacity equivalence alpha<1 iff kappa>(3k-A)/4. Identify any normalization, sign, topology, or quantifier error and give corrected formulas. Also check that the added Fino construction is represented at exactly its proved scope (complete noncompact R4, not closed Goldberg).

## Output

# Scientific verification memo

## 1. Relative Chern–Weil identity and the omitted CH core

In the session’s curvature-operator norm,
\[
4\pi^2T_+=\frac1{24}\int s^2+2\int|W^+|^2-\frac12P,
\qquad T_+=2\chi+3\tau .
\]
Hence
\[
\frac{P}{8\pi^2}
=\frac1{96\pi^2}\int s^2
+\frac1{2\pi^2}\int|W^+|^2-T_+.
\]
A local \(\overline{\mathbb{CP}}^{\,2}\) insertion changes
\[
\Delta T_+=2(1)+3(-1)=-1.
\]
Because the cell and the CH model agree on an outer collar, their transgression terms cancel. Since the CH model is Einstein and has \(P=0\),
\[
p-1=
\frac{\Delta\int|W^+|^2}{2\pi^2}
+\frac{\Delta\int s^2}{96\pi^2},
\qquad p=\frac{P_{\rm cell}}{8\pi^2}.
\]
Thus (74.1) has the correct coefficient and sign.

At \(\operatorname{Ric}=-6g\), \(s=-24\), and the radial coordinate satisfies
\[
\frac{dV}{8\pi^2}=\frac{x\,dx}{8}.
\]
Therefore
\[
V(0\le x<x_0)=\frac{\pi^2x_0^2}{2},
\]
and
\[
\frac1{96\pi^2}\int_{0\le x<x_0}s^2\,dV
=\frac{576}{96\pi^2}\frac{\pi^2x_0^2}{2}
=3x_0^2.
\]
The shell computation must therefore be corrected by
\[
\Delta S_{96}
=\Delta S_{96,\mathrm{shell}}-3x_0^2.
\]
This validates the Step-74 subtraction.

## 2. Interval arithmetic for the two cells

The post-processing identity used by the script is
\[
\frac{\Delta W^+}{2\pi^2}=p-1-\Delta S_{96},
\qquad
\eta=-\frac{\Delta W^+}{2\pi^2}.
\]

The supplied JSON endpoints give:

| Cell | \(p\) | \(\Delta S_{96}\) | \(\Delta W^+/(2\pi^2)\) | \(\eta\) |
|---|---:|---:|---:|---:|
| \(x_0=.03,\ X=128\) | \([0.9956627327532543293,\ 0.9956627327711141997]\) | \([0.0707969335693406631,\ 0.0707969335693407692]\) | \([-0.0751342008160864399,\ -0.0751342007982264634]\) | \([0.0751342007982264634,\ 0.0751342008160864399]\) |
| \(x_0=.01,\ X=8\) | \([0.9991087027335926475,\ 0.9991087027335926485]\) | \([0.0213032806029568625,\ 0.0213032806029568703]\) | \([-0.0221945778693642227,\ -0.0221945778693642141]\) | \([0.0221945778693642141,\ 0.0221945778693642227]\) |

Direct interval subtraction reproduces all four displayed Step-74 intervals. The corresponding formal all-cell values are also consistent:
\[
\frac1{3(1-\eta_{128})}
\in[0.3604126497282353818,\ 0.3604126497351953751],
\]
\[
\frac1{3(1-\eta_8)}
\in[0.3408994527837662833,\ 0.3408994527837662864].
\]

The supplied material supports independent verification of the post-processing and interval propagation. A fresh quadrature execution additionally requires the imported `FrozenCell` implementation and the two source certificate files.

## 3. Closed-manifold deficit formula and cover quantifiers

With
\[
d_*(M)=8\pi^2\chi(M)-\inf_g\int|W_g|^2,
\]
the signature identity gives
\[
d([g])=4\pi^2T_+(M)-2\int|W_g^+|^2.
\]
One special cell changes
\[
\Delta T_+=-1,\qquad
\Delta\int|W^+|^2=-2\pi^2\eta,
\]
and hence
\[
\Delta d=-4\pi^2+4\pi^2\eta
=-4\pi^2(1-\eta).
\]
An ordinary reversed-\(\mathbb{CP}^2\) insertion changes the limiting deficit by \(-4\pi^2\). Starting from a CH ball quotient with
\[
d_*(X)\ge\frac{4\pi^2}{3}c_1^2(X),
\]
\(n\) special cells and \(k-n\) ordinary cells therefore give
\[
\boxed{
d_*(M)\ge4\pi^2\left(\frac{\widetilde A}{3}-k+\eta n\right),
\qquad
M=\widetilde X\#k\overline{\mathbb{CP}}^{\,2},
}
\]
where
\[
\widetilde A=c_1^2(\widetilde X).
\]

This exposes a notation error in Step 74: after passing from \(X\) to a further cover \(\widetilde X\), every occurrence of \(A\) in (74.10)–(74.16) must mean \(\widetilde A\), not the Chern number of the original base quotient. Equivalently,
\[
\widetilde A=\deg(\widetilde X\to X)\,c_1^2(X).
\]

The exact quantifiers are:

- choose one finite cover \(X'\) with global injectivity radius \(>2R\);
- every further finite cover \(\widetilde X\to X'\) inherits that injectivity-radius estimate;
- if \(N\) disjoint usable sites are supplied, then every
  \[
  0\le n\le\min\{k,N\}
  \]
  is allowed.

Positive right-hand side gives \(d_*(M)>0\), hence \(\alpha(M)<1\).

The most precise normalized form is
\[
\frac{d_*(M)}{4\pi^2\widetilde A}
\ge
\frac13-h+\eta\min\left\{h,\frac N{\widetilde A}\right\},
\qquad h=\frac{k}{\widetilde A}.
\]
Once the preliminary cover is fixed, no further depth assumption is needed. The phrase “all sufficiently deep further covers” is weaker than the actual packing statement.

If exact collar smoothing occupies radius \(R+\delta\), one uses the packing coefficient at \(R+\delta\). Since the final inequalities are strict, letting \(\delta\downarrow0\) recovers the displayed open endpoints.

## 4. CH ball volume, packing coefficient, and footprint normalization

Scaling a \(\operatorname{Ric}=-6g\) CH metric by \(6\) gives \(\operatorname{Ric}=-g\). With
\[
X=\sinh^2(R/\sqrt6),
\]
the ball volume is
\[
\boxed{V(B_R)=18\pi^2X^2.}
\]
Its small-\(R\) expansion is \(\pi^2R^4/2+O(R^6)\), agreeing with Euclidean four-volume.

For a maximal \(2R\)-separated set, the \(R\)-balls are disjoint and the \(2R\)-balls cover. Since
\[
V(\widetilde X)=2\pi^2\widetilde A,
\qquad
X(2R)=4X(1+X),
\]
one gets
\[
\boxed{
\frac N{\widetilde A}\ge
\beta_0(X)=\frac1{9[4X(1+X)]^2}.
}
\]

The numerical values are:

- \(X=8\):
  \[
  X(2R)=288,\qquad
  \beta_0=\frac1{746496}
  =1.33959190672153635\times10^{-6},
  \]
  \[
  \frac13+\eta_{8,\mathrm{lo}}\beta_0
  =0.33333336306501022023455\ldots;
  \]

- \(X=128\):
  \[
  X(2R)=66048,\qquad
  \beta_0=\frac1{39261044736}
  =2.54705397353591197\times10^{-11},
  \]
  \[
  \frac13+\eta_{128,\mathrm{lo}}\beta_0
  =0.33333333333524704198024\ldots.
  \]

These agree with (74.15)–(74.16).

### Footprint-field inconsistency in the JSON files

For CH with \(\operatorname{Ric}=-g\),
\[
|W^+|^2=\frac23,
\qquad
\frac1{4\pi^2}\int_{B_R}|W^+|^2=3X^2.
\]
Thus the efficiency defined in (74.9) is
\[
\frac{\eta}{3X^2}.
\]
Its correct intervals are approximately
\[
X=8:\quad
[1.15596759736271948,\ 1.15596759736271994]\times10^{-4},
\]
\[
X=128:\quad
[1.5286092284795423,\ 1.5286092288429045]\times10^{-6}.
\]
Their ratio is about \(75.6222\).

The two JSON files instead record
\[
3.467902792\ldots\times10^{-4},
\qquad
4.585827686\ldots\times10^{-6},
\]
which equal \(\eta/X^2\), not \(\eta/(3X^2)\). This contradicts their own footprint fields \(3X^2=192\) and \(49152\). The visible current script computes the correct quotient, so the JSON files were generated from an earlier expression and should be regenerated.

There is also a physical factor of two in the wording. Since
\[
-\Delta\int|W^+|^2=2\pi^2\eta,
\]
the actual fraction of the CH ball’s self-dual Weyl energy removed is
\[
\frac{2\pi^2\eta}{12\pi^2X^2}
=\boxed{\frac{\eta}{6X^2}}.
\]
Thus \(\eta/(3X^2)\) is a deficit-saving efficiency, not the literal self-dual-Weyl removal fraction. This distinction is needed for the \(\Theta\) normalization in (74.21).

## 5. Fixed-complex Kähler comparison

There are two corrections to the displayed cohomology calculation.

First, for the blow-up complex surface,
\[
K_M=H+\sum_iE_i,
\qquad
c_1(M)=-H-\sum_iE_i.
\]
The sign \(c_1(M)=-H+\sum E_i\) in Step 74 is inconsistent with the standard exceptional divisor convention
\[
E_i^2=-1,\qquad [\omega]\cdot E_i=e_i>0.
\]

Second, not every Kähler class on a ball quotient blow-up is of the form \(tH-\sum e_iE_i\). In general write
\[
[\omega]=\pi^*\alpha-\sum_i e_iE_i,
\]
where \(\alpha\) lies in the positive cone of the base. Put
\[
q=H\cdot\alpha,\qquad E=\sum_i e_i.
\]
The Hodge index theorem gives
\[
q^2\ge A\,\alpha^2,\qquad A=H^2.
\]
Therefore
\[
\frac{(c_1(M)\cdot[\omega])^2}{[\omega]^2}
=
\frac{(q+E)^2}{\alpha^2-\sum e_i^2}\ge A,
\]
because
\[
(q+E)^2-A\left(\alpha^2-\sum e_i^2\right)
=
(q^2-A\alpha^2)+2qE+E^2+A\sum e_i^2\ge0.
\]

For a Kähler metric,
\[
\int|W^+|^2=\frac1{24}\int s^2
\ge\frac{4\pi^2}{3}
\frac{(c_1\cdot[\omega])^2}{[\omega]^2}
\ge\frac{4\pi^2A}{3}.
\]

The correct positive-deficit condition in the session’s operator norm is
\[
\boxed{
\int|W^+|^2<2\pi^2(A-k).
}
\]
Indeed,
\[
d([g])=4\pi^2(A-k)-2\int|W^+|^2.
\]
Consequently the Kähler lower estimate is compatible with positive deficit only when
\[
\frac{4\pi^2A}{3}<2\pi^2(A-k)
\iff k<\frac A3.
\]

Equation (74.19a),
\[
\int|W^+|^2<\frac{4\pi^2A}{3}-4\pi^2k,
\]
is incorrect and is not related to \(2\pi^2(A-k)\) by a tensor-norm conversion. In the corresponding \((0,4)\)-tensor norm, both valid Weyl expressions are multiplied by four:
\[
\int|W^+|_{\mathrm{tensor}}^2<8\pi^2(A-k),
\qquad
\int|W^+|_{\mathrm{tensor}}^2\ge\frac{16\pi^2A}{3}.
\]

Thus \(h=1/3\) is the fixed blow-up complex structure’s Kähler frontier. The argument does not exclude a Kähler metric associated with some unrelated complex structure on the same smooth manifold.

## 6. Capacity equivalence

For a Yamabe representative scaled to \(s=-4\), define
\[
p=\frac{P}{8\pi^2},
\qquad
\upsilon=\frac{V}{2\pi^2}-A,
\qquad
\kappa=\frac A2-\frac{3}{8\pi^2}\int|W^+|^2.
\]
Chern–Weil gives
\[
A-k=\frac{A+\upsilon}{3}
+\frac1{2\pi^2}\int|W^+|^2-p,
\]
hence
\[
\boxed{
p=k-\frac43\kappa+\frac13\upsilon.
}
\]

At this constant-scalar representative,
\[
\mathcal E=\frac{4P}{P+4V},
\]
so
\[
\mathcal E<1
\iff 3P<4V
\iff 3p<A+\upsilon.
\]
Substitution yields
\[
3k-4\kappa+\upsilon<A+\upsilon
\iff
\boxed{\kappa>\frac{3k-A}{4}}.
\]

The global quantifier should be written
\[
\boxed{
\alpha(M)<1
\iff
\text{there exists such a Yamabe representative with }
\kappa>\frac{3k-A}{4}.
}
\]
Equivalently, if \(\kappa_*\) is the supremum over realizable representatives,
\[
\alpha(M)<1\iff \kappa_*>\frac{3k-A}{4}.
\]

This normalization also cross-validates the mixed-cell theorem: one special cell changes
\[
\Delta\kappa=\frac{3\eta}{4},
\]
so the capacity inequality becomes
\[
\frac{3\eta n}{4}>\frac{3k-A}{4}
\iff
k<\frac A3+\eta n.
\]

If \(\Theta\) denotes the actual fraction of the host Weyl budget removed, then
\[
\kappa=\frac A2\Theta,
\qquad
h<\frac13+\frac23\Theta.
\]
Thus (74.21) has the correct factor provided \(\Theta\) uses the literal Weyl-energy fraction \(\eta/(6X^2)\), not the quantity \(\eta/(3X^2)\).

## 7. Fino construction

The added construction is represented at the proved level:

- a smooth complete metric and closed compatible two-form on \(\mathbb R^4\);
- \(\operatorname{Ric}=-3g\), \(W^-=0\), \(|\Omega|^2=2\);
- \(|\nabla\Omega|^2>0\) at every finite point;
- nonhomogeneity certified by the variation of \(|W^+|^2\) from \(2/3\) to the asymptotic value \(6\).

It therefore supplies a complete, noncompact, non-invariant, non-Ricci-flat example on the underlying additive Lie group \(\mathbb R^4\).

It does not settle the closed Goldberg problem for Einstein constant \(<0\). On a closed almost-Kähler Einstein four-manifold, the torsion lies in
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2},
\qquad
\langle c_2(E),[M]\rangle=5\chi+6\tau
=\chi+2(2\chi+3\tau)>0.
\]
Hence a torsion section must have a zero. The complete \(\mathbb R^4\) example has no finite zero, so the same pair cannot descend unchanged to a compact quotient. This does not imply that torsion vanishes identically on every closed example.

## Main corrections to Step 74

1. Replace \(A\) by \(\widetilde A=c_1^2(\widetilde X)\) throughout the further-cover formulas.
2. Regenerate the two JSON footprint fields; they currently equal \(\eta/X^2\) instead of \(\eta/(3X^2)\).
3. Relabel \(\eta/(3X^2)\) as deficit-saving efficiency; literal Weyl removal is \(\eta/(6X^2)\).
4. Replace \(c_1(M)=-H+\sum E_i\) by \(c_1(M)=-H-\sum E_i\), and use a general base class \(\alpha\), not only \(tH\).
5. Delete (74.19a) and use
   \[
   \int|W^+|^2<2\pi^2(A-k)
   \]
   in operator norm.
6. State the capacity equivalence with an existential Yamabe representative, or with the supremal realizable capacity \(\kappa_*\).
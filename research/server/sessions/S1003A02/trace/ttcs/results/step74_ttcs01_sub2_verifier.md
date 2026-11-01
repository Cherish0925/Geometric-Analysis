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

# Verification memo: Step 74 (certified Weyl saving, mixed Weyl frontier, Kähler comparison, capacity form, Fino representation)

Conventions used throughout are the session's. Weyl uses the operator Hilbert–Schmidt norm, with \(4\pi^2T_\pm=S/24+2\int|W^\pm|^2-P/2\). This gives two consequences:

- \(\int|W^+|^2-\int|W^-|^2=12\pi^2\tau\).
- \(d=8\pi^2\chi-\mathcal W=S/24-P/2\) for every metric. This is Gauss–Bonnet, and it gives a second, independent route to every deficit increment below.

**Summary.** The relative coefficient (i), the core subtraction, the interval arithmetic (ii), the Hodge-index inequality (v), the capacity algebra (vi), the CH ball volume and \(\beta_0\) (iv), and the Fino representation are correct. The material errors are:

1. Display (74.19a) is wrong.
2. One JSON field disagrees with the script.
3. The packing radius must be the smoothed cell's support radius.
4. \(A\) must be \(c_1^2\) of the cover actually used.
5. The Kähler statement uses too narrow a class and too narrow a set of complex structures.
6. The formal value (74.6) is unrealizable by disjoint placement, not merely unrealized.

## (i) Relative Chern–Weil coefficient and core subtraction: correct

**Coefficient.** \(P=S/12+4\int|W^+|^2-8\pi^2T_+\). One reversed-\(\mathbb{CP}^2\) summand gives \(\Delta T_+=2(1)+3(-1)=-1\). The CH ball has \(P=0\). Hence
\[
p-1=\frac{\Delta\int|W^+|^2}{2\pi^2}+\frac{\Delta\int s^2}{96\pi^2},
\]
which is (74.1). Boundary terms cancel because the cell is exactly CH on its collar.

**Independent check through Gauss–Bonnet.** \(\Delta d=\Delta S/24-\Delta P/2=4\pi^2(\mathrm{ds96}-p)\). With \(\eta=1-p+\mathrm{ds96}\) this is \(\Delta d=-4\pi^2(1-\eta)\), in agreement with the signature route (\(\Delta\int|W^-|^2=\Delta\int|W^+|^2+12\pi^2\), \(\Delta\chi=1\)). The bookkeeping is therefore closed. The deficit change of a cell is simply \(4\pi^2(\mathrm{ds96}_{\rm total}-p)\):

| Cell | \(\Delta d/4\pi^2\) |
|---|---|
| \(X=8\) | \(-0.97781\) |
| \(X=128\) | \(-0.92487\) |

**Core term.** In \(\mathrm{Ric}=-6g\) the CH metric is \(dt^2+\sinh^2t(\sigma_1^2+\sigma_3^2)+\sinh^2t\cosh^2t\,\sigma_2^2\). Then:

- \(dV=2\pi^2\sinh^3t\cosh t\,dt=\pi^2x\,dx\) with \(x=\sinh^2t\), so \(dV/8\pi^2=x\,dx/8\), matching the script's `vol_ch`.
- With \(s^2=576\): \(\frac1{96\pi^2}\int_0^{x_0}576\,\pi^2x\,dx=3x_0^2\). This is (74.2).
- The script's `/12` correctly converts \(\int s^2\,(dV/8\pi^2)\) to \(\int s^2 dV/(96\pi^2)\).

The subtraction is right provided the cell's coordinate \(x\) at its outer edge is the CH coordinate of the replaced ball. This holds for the exact-CH collar.

**Sign check against the Kähler identity.** For Kähler metrics \(|W^+|^2=s^2/24\) pointwise, so \(p-1=3\,\Delta S/(96\pi^2)\). Kähler cells therefore have \(\eta\le0\) exactly when \(p\ge1\). A positive \(\eta\) is consistent only for a non-Kähler cell, and the perpendicular cells are non-Kähler.

**Smoothing requirement.** \(\Delta d\) involves \(\int s^2\) as well as \(P\). The exact-collar smoothing must therefore have arbitrarily small effect on \(\int s^2\), not only on \(P\). Step 69 §2(C) states only \(p\le p_c+\delta\). The A01 smoothing is controlled in \(J_6=P+\int(s+24)^2/4\), which does control the scalar term on the smoothing region. The proof of 74.W should cite the \(J\)-controlled version.

## (ii) Interval outputs: arithmetic verified

**\(X=128\).**

- \(1-p\in[0.0043372672289,\,0.0043372672467]\).
- \(\mathrm{ds96}_{\rm total}=0.07349693357-0.0027=0.07079693357\).
- \(\eta=0.0751342008\), with endpoints matching (74.5) to every displayed digit.
- \(1/(3\cdot0.9248657992)=0.36041264973\).

**\(X=8\).**

- \(1-p=0.000891297266\).
- \(\mathrm{ds96}_{\rm total}=0.0213032806030\).
- \(\eta_8=0.0221945778694\).
- \(1/(3\cdot0.977805422)=0.340899453\).

All outward endpoints are ordered consistently: lower \(p\) pairs with upper \(\mathrm{ds}\) for the lower end of \(\Delta W^+\).

**JSON field disagreement.** In both JSON files `eta_per_host_Wplus_footprint` equals \(\eta/X^2\), not \(\eta/(3X^2)\):

| Cell | JSON value | Equals | \(\eta/(3X^2)\) |
|---|---|---|---|
| \(X=8\) | \(3.46790\times10^{-4}\) | \(\eta_8/64\) | \(1.15597\times10^{-4}\) |
| \(X=128\) | \(4.5858\times10^{-6}\) | \(\eta_{128}/16384\) | \(1.52861\times10^{-6}\) |

The dyadic denominators confirm this: \(2^{261}=2^{255}\cdot2^6\). Yet the same files record `host_Wplus_footprint_in_4pi2_units` \(=192\) and \(49152\), which equal \(3X^2\). The shown script computes \(\eta/(3X^2)\). The JSON was therefore produced by an earlier code version. The note's (74.9) values follow the shown formula, and the ratio \(75.62\) is unaffected. The JSON should be regenerated before it is cited as the authoritative output.

**Minor endpoint mismatch.** Step 69 quotes the \(X=128\) upper endpoint numerator as \(\dots565914367157197246841/2^{128}\). The Step-74 JSON hull gives \(\dots570526053175624634745/2^{128}\), which is larger by \(\approx1.4\times10^{-20}\). Both are valid upper bounds. One endpoint should be named as the certificate's.

## (iii) Mixed theorem 74.W: correct after two corrections

**Host and cell increments.** For the \(\mathrm{Ric}=-g\) KE host, \(d=S/24-P/2=\tfrac{16\cdot2\pi^2A}{24}=4\pi^2A/3\). Each special cell contributes \(-4\pi^2(1-\eta)\), by (i).

**Ordinary insertions.** Each ordinary insertion contributes \(-4\pi^2\) in the limit. This uses \(d_*(\overline{\mathbb{CP}}^2)=12\pi^2\), Euler loss \(16\pi^2\), and Kobayashi/LeBrun conformal gluing at a flattened point. The tiny balls are disjoint from the special cells.

**Implication.** Positive \(d\) forces \(Y\ne0\), so \(\alpha<1\) by Step 72. The implication \(k<A/3+\eta n\Rightarrow\alpha<1\) is correct.

**Corrections.**

1. **\(A\) must refer to the cover.** \(A\) is defined as \(c_1^2(X)\), but the manifold is \(\widetilde X\#k\overline{\mathbb{CP}}^2\). The correct statement is
   \[
   d_*(M)\ge4\pi^2\Big(\tfrac{c_1^2(\widetilde X)}3-k+\eta n\Big),\qquad c_1^2(\widetilde X)=\deg(\widetilde X\to X)\,c_1^2(X).
   \]
   The phrase "conformal classes whose Weyl deficit approaches \(d(M)\ge\dots\)" should read \(\sup_{[g]}d([g])\ge\dots\).

2. **Packing radius.** The radius in the packing must be the support radius \(R_s\) of the smoothed cell, including its collar. Step 69 places the smoothed cell in \(R_c=\sqrt6\,\mathrm{arsinh}\sqrt{128}+1\), which is larger than \(R(X)\). With an extra unit of collar the coordinate becomes \(X_s=\sinh^2(\mathrm{arsinh}\sqrt X+1/\sqrt6)\). For \(X
# TTCS Independent Branch Record

```json
{
  "step_id": 49,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A02/workspace/notes/step49_cell_Y_measurement_bad_set_obstruction.md",
    "Sessions/S1003A02/workspace/scripts/step49_cell_theoremY_profile.py",
    "Sessions/S1003A02/workspace/data/step49_cell_theoremY_profile_x003_X128_N1600.json",
    "Sessions/S1003A01/workspace/notes/step43_period_linear_lebrun_ledger_and_ricci_flow.md",
    "Sessions/S1003A02/workspace/data/step48_bianchi_indicial.json"
  ]
}
```

## Task

Verify the mathematical substance and normalization of Step 49's two principal results. (A) Read the Step-48 Theorem-Y definitions, the new Step-49 note/script/data, and the A01 Step-43 ledger note. Check the conversion among delta W, D_W, Delta V, the spectral integrals Psi/dist^2/splitting, and the conclusion that the certified cell is far from Theorem-Y/LeBrun equality. Identify any formula or normalization error. (B) Check the handwritten exact first-order derivation for the nu=4 triaxial diagonal Bianchi-IX Einstein tail, especially e^{4r} delta W+=diag(-12,12,0) at Ric=-6 and the scalar--4 conclusions delta mu_min=delta|W+|^2=0, sigma=2 eps e^-4r, Psi=16 eps^2 e^-8r. Provide corrected formulas if needed. (C) Assess whether the stated obstruction to an unconditional linear bad-ball count is mathematically valid from the available hypotheses: can critical L2 Ricci defect plus Theorem K/closed identity force linearly many unit balls not C2a-close to CH, absent an Euler-Lagrange equation or per-ball load bound? Focus on correctness and any stronger unconditional weighted statement actually justified.

## Output

# Verification memo: Step 49 (Theorem‑Y ledger of the certified cell, the ν=4 triaxial tail, and bad‑ball counting)

**Summary.**
- **(A)** The conversion chain among \(\delta W\), \(D_W\), \(\Delta V\), \(\Psi\), \(\operatorname{dist}^2\) and \(4\sigma^2\) is correct. The "far from field equality" reading is correct in the formal closed‑replica sense, provided the replica has \(\Pi_g\approx0\). Four textual or bookkeeping defects remain:
  - the stale ceiling 0.0332 inherited from Step 48;
  - a tautological "check" in the script;
  - "stable" attached to the superseded ledger;
  - the letter \(x\) used for two different objects.
- **(B)** The ν=4 derivation is correct as written, with every coefficient reproduced independently. The only additional facts needed are which radius \(r\) is meant, and that the leading coefficient does not depend on the exact Jacobi field.
- **(C)** The conclusion that no linear bad‑ball count follows is mathematically sound. The prescription for repairing the count is incomplete: a per‑ball load bound plus Theorem K is still insufficient, because the good region can absorb Theorem K's \(L^1\) weight. One stated bulk‑volume estimate is missing its linear flux term.

---

## A. Normalizations and the cell ledger

### A1. Identities, rederived

Gauss–Bonnet with the endomorphism norm on \(\Lambda^+\) gives
\[
\textstyle P=4\int|W^+|^2+\tfrac1{12}\int s^2-8\pi^2(A-k).
\]
- **KE check.** At \(s\equiv-4\) with \(|W^+|^2=\tfrac23\), this gives \(V=2\pi^2A\).
- **(Y0).** Substituting \(\int|W^+|^2=\tfrac23\hat V-D_W\) and \(\hat V=2\pi^2A+\Delta V\) gives \(P=8\pi^2k+4\Delta V-4D_W\). This is (Y0) exactly.
- **Relative \(D_W\).** Since \(\int|W^+|^2\) is conformally invariant, relative to the replaced CH ball
\[
D_W=\tfrac23\Delta V+\delta W .
\]
  Hence the saving equals \(4\delta W-\tfrac43\Delta V\).
- **Numerical check.** With A01's values, \(4(0.0187835)-\tfrac43(0.0530963)=0.0043389\). The saving is 0.0043391.
- **Theorem Y.** \(\int\sup f=2D_W-\int\Psi\) follows from \(\varphi-4|W|^2=2(\tfrac23-|W|^2)-\Psi\). Eliminating \(D_W\) with (Y0) gives \(8\pi^2k-P\le4\Delta V-2\int\Psi\). Correct.
- **\(\varphi\) and \(\Psi\).** I rederived \(\varphi\): \(r_*=(6x+14)/9\), value \(r_*^3/2-\tfrac43\), clamped value \(4x\). I rederived \(\Psi=\tfrac53h^2+\tfrac4{27}h^3+4\sigma^2\) by expanding \(r_*=2-\tfrac23h\). Both correct.
- **(Y‑LeB)/(LeB\(_{\rm full}\)).** These follow from \((4+w)^2=3w^2+24-2(w-2)^2\) and the GB formula. Correct.
- **Corollary Y1.** \(Y^2\ge32\pi^2(A+(1-c)k)+\tfrac{80}9\int\operatorname{dist}^2\). Correct.
- **Formal common mode.** Recomputed: LHS \(4-5h\), \(4\Delta V=4-h\), \(2\int\Psi=\tfrac{10}3h+\tfrac8{27}h^2\), slack \(\tfrac23h-\tfrac8{27}h^2\). With \(u=-3h\), (Y‑LeB) is saturated exactly. Correct.

### A2. Script normalizations (`step49_cell_theoremY_profile.py`)

- **Measure.** `measure` \(=a_1a_2a_3\,dt\). With \(\mathrm{vol}(S^3)=2\pi^2\) for \(d\sigma_i=2\sigma_j\wedge\sigma_k\), we have \(d\mu/8\pi^2=\tfrac14\)measure.
  - So `Pnorm=integ(ric0sq/4)` is \(\int|\mathrm{Ric}^\circ|^2/8\pi^2\).
  - `mhat=9·measure·u⁴` \(=36\cdot\tfrac14\cdot u^4\cdot\)measure is the \(s=-4\) measure of \(u^2g\) scaled by 6.
- **Spectrum.** `eig_hat=W/(6u²)` is correct. \(W^+=R^+-s/12\) is traceless, and the CH spectrum is \((-4,2,2)\to(-\tfrac23,\tfrac13,\tfrac13)\).
- **Distance.** The sorted‑eigenvalue distance is the true orbit distance (Hoffman–Wielandt). \(\sigma=(\mu_3-\mu_2)/2\) matches the lemma's parametrization.
- **Pointwise cross‑check at the \(\Psi\) maximum (JSON).** At the bolt the spectrum is \((-0.20133,-0.20133,0.40275)\), so \(h=0.46534\) and \(\sigma=0.30204\). Then:
  - \(\tfrac53h^2+\tfrac4{27}h^3+4\sigma^2=0.36090+0.01493+0.36491=0.7407\). The JSON gives `Psi_max` 0.74077.
  - \(\operatorname{dist}^2=0.2166+0.2859+0.0048=0.5073\). The JSON gives 0.50723.

  The bolt is where \(\mu_{\min}\) becomes doubly degenerate and the eigenline leaves the Kähler slot. A01 reports the Kähler‑slot value \(-1.12/6=-0.187\) there, which is the reported \(x_{\min}\).
- **Global consistency.** \(\int4\sigma^2=0.01092\le\int\Psi=0.01323\), consistent with \(\Psi\ge4\sigma^2\). The ratio 1.764 lies in \([10/9,2)\).
- **Exterior CH region.** This region is not integrated. Its contribution is \(O(w^2)\) times volume with \(u-1<10^{-8}\) at the collar, so it is negligible.

### A3. Defects

1. **Stale ceiling 0.0332 (Step 48 check; repeated in Step 49 §1).**
   - The number is \(((4/3)\bar\Delta V-\text{saving})/2=(0.07080-0.00434)/2=0.03323\). It was built from the misidentified quantity \(\tfrac43\Delta V\).
   - Theorem Y actually requires \(2\int\bar\Psi\le4\bar\Delta V-\text{saving}=0.20805\), i.e. \(\int\bar\Psi\le0.1040\).
   - The comparison "\(0.0265<0.0332\)" therefore compares against a meaningless number, and in mixed form (\(2\int\Psi\) against a half‑quantity). The conclusion of no tension holds a fortiori, but the displayed ceiling should be replaced.

2. **The \(D_W\) entry in the script is not a measurement.**
   - `DW_stable = dV_stable + saving_hat/4` is (Y0) imposed. So the displayed \(4(\bar D_W-\bar\Delta V)=0.0043391\) is an identity by construction.
   - `fourDeltaWplus` \(=-4\delta W\) is likewise derived, giving \(\delta\bar W=\text{saving}/4+\bar\Delta V/3=0.018787\).
   - The independent closure is A01's: \(\delta W\) from the chiral \(\int|W^-|^2=1.48122\) together with the tail‑free \(\Delta V\) identity. It closes the GB identity to \(2\times10^{-7}\).

3. **Ledger labeling is inverted.**
   - The script calls the Step‑39 `RV_hat` value (\(\bar\Delta V=0.0531062\)) "stable".
   - The note then attributes the \(10^{-5}\) discrepancy to the "old finite‑grid relative‑volume error". That error belongs to the Step‑39 value.
   - The superseding number is A01 Step 43's tail‑free identity, \(\bar\Delta V=0.0530963\).
   - The gap in \(4\bar\Delta V\) is \(4\times10^{-5}\), larger than A01's stated \(10^{-5}\) uncertainty. It is irrelevant against slacks of about 0.18, but A01's table is the correct authority.

4. **Notation collision.** In Step 49 §1, "\(x=-\mu_{\min}\) ranges from 0.1873 to 0.6667" and "bolt layer \(x\in[.03,.0315]\)", "50% of \(\Psi\) by \(x\simeq0.814\)" use one letter for the spectral parameter and for the radial profile coordinate.

5. **Units of the Y1 number.** "\(\Delta V\ge0.085614\) per class" equals \(2\pi^2\cdot0.0043373\) in absolute units. In barred units it is \(0.0010843\). The ratio "about 49" compares \(\bar\Delta V=0.0531\) with the barred value \((1-c)/4\).

### A4. How strong "far from equality" is

- Slack against saving: about 0.18 for Theorem Y and about 0.20 for LeBrun, against 0.0043. Numerical uncertainty does not affect this.
- The LeBrun slack is computed with \(\Pi_g=0\). In a closed replica, (LeB\(_{\rm full}\)) removes \(2\bar\Pi_g\) from the slack, with \(\Pi_g\ge|K^-|^2+\sum|E_i^+|^2\). So "far from LeBrun equality" holds exactly to the extent that the glued replica keeps \(E_i^+\approx0\), i.e. \(2\bar\Pi_g\ll0.20\).
- Theorem Y's slack carries no \(\Pi_g\) term.
- The radial quantiles of \(\Psi\) (90% by profile \(x\simeq16\)) describe the degree‑20 non‑Einstein profile ansatz. They are not governed by the Einstein indicial roots of Step 48, so the "long but integrable tail" is a property of this cell, not of Einstein tails.

## B. The ν=4 triaxial tail: independent rederivation

**Background check.** With \(A=B=s\) and \(C=sc\), I get \(\gamma_1=\gamma_2=C/B=c=A'\), so \(v_{1,2}=0\). Also \(\gamma_3=2-c^2\) and \(C'=2c^2-1\), so \(v_3=3s^2\). The formula then gives \(R^+=(0,0,-6)\) and \(W^+=(2,2,-4)\), which is CH at \(\mathrm{Ric}=-6\). Correct.

**First variation of \(v_1\).** Take \(\delta A=\varepsilon sq\), \(\delta B=-\varepsilon sq\), \(\delta C=0\).
- \(\delta C=0\) is forced at first order by the \(1\leftrightarrow2\), \(q\mapsto-q\) symmetry. The indicial rows of `step48_bianchi_indicial.json` with \(a=-b\), \(c=0\) give \(-\nu(\nu-4)\) in rows 11 and 22, and identically 0 in rows 00 and 33.
- From \(\delta N=-4s^2\varepsilon q\) and \(\delta M=-s^2c\,\varepsilon q\):
\[
\delta\gamma_1=\varepsilon q\,(c-4/c),\qquad \delta v_1=\varepsilon\,(sq'+4q/c).
\]
- This holds for general \(q(r)\). For \(q=e^{-4r}\) it gives \(d=4\varepsilon q(\operatorname{sech}r-\sinh r)\). Correct.

**Other components.** \(\delta v_2=-d\). \(\delta v_3=0\), because \(A^2+B^2\), \(AB\) and \(C\) are all stationary.

**Curvature variation.** Background \(v_1'=0\) and numerator \(0\), so
\[
\delta R^+_{11}=-\frac{d'}{2s}+\frac{d\,(3s^2/2-1)}{s^2c}.
\]
Also \(\delta R^+_{22}=-\delta R^+_{11}\) and \(\delta R^+_{33}=0\). Hence \(\operatorname{tr}\delta R^+=0\), so \(\delta s=0\) and \(\delta W^+=\delta R^+\).

**Asymptotics.**
- \(d\approx-2\varepsilon e^{-3r}\) and \(d'\approx6\varepsilon e^{-3r}\).
- \(-d'/2s\approx-6\varepsilon e^{-4r}\), and the second term \(\approx\tfrac32 d/c\approx-6\varepsilon e^{-4r}\).
- Sum: \(e^{4r}\delta W^+\to\operatorname{diag}(-12,12,0)\varepsilon\). **Confirmed.**

**Robustness of the coefficient.** The exact Jacobi field has \(q=e^{-4r}(1+\beta e^{-2r}+\dots)\). The correction enters \(d\) at \(O(e^{-5r})\), so \(-12\) is independent of \(\beta\). The leading term uses only the indicial root.

**Scalar −4 consequences.**
- After dividing by 6, the upper pair shifts by \((-2,+2)\varepsilon e^{-4r}\) and the Kähler slot is fixed. So \(\delta\mu_{\min}=0\).
- \(\delta|W^+|^2=2\langle W,\delta W\rangle=\tfrac23(-2+2)\varepsilon e^{-4r}=0\).
- \(\sigma=2|\varepsilon|e^{-4r}+O(\varepsilon^2e^{-8r})\).
- \(\operatorname{dist}=2\sqrt2|\varepsilon|e^{-4r}\).
- \(\Psi=16\varepsilon^2e^{-8r}+O(\varepsilon^3e^{-12r})\). Second‑order changes of \(x\) are \(O(\varepsilon^2q^2)\) and enter \(\Psi\) only at \(O(\varepsilon^4q^4)\).

**The radius.** \(r\) is the geodesic radius of the \(\mathrm{Ric}=-6\) profile metric. In the scaled \(s=-4\) metric, \(e^{-4r}=e^{-4\hat r/\sqrt6}\). The volume growth \(e^{4r}\) is in the same \(r\), so the marginality statements stand. The formulas should state which radius is used.

**What the computation implies.** Theorem K's \(L^1\) quantity grows linearly in \(r\) along such a tail, while \(\int\Psi\) converges. Correct.

**The ν=0 (CR) triaxial mode.** Here \(\delta v_1=\varepsilon(sq'+4q/c)\) has its two terms at the same order \(e^{-r}\) once the \(e^{-2r}\) correction of \(q\) is included. So the coefficient of \(\delta W^+\sim e^{-2r}\) cannot be read off without the exact Jacobi field.

Generically, \(\Psi\sim e^{-4r}\) for that mode, which makes \(\int\Psi\) grow linearly in \(r\). The localization of Theorem Y on a collar therefore relies on the collar carrying no ν=0 (CR) component. Exact CH‑asymptotic collars satisfy this; a general core does not automatically.

## C. Can the available inputs force linearly many non‑CH‑close unit balls?

### C1. Step 49's three points are mathematically sound

1. **No ε‑regularity.** Without an Euler–Lagrange equation, "not \(C^{2,\alpha}\)‑close" carries no energy.
   - A rescaled bump \(h=\lambda^2\eta(\cdot/\lambda)\) has \(|\nabla^2h|=O(1)\) but \(\|\nabla^2h\|_{L^2}=O(\lambda^2)\).
   - It changes \(P\) by \(o(1)\), and the Yamabe rescaling restores \(s\equiv-4\) at \(o(1)\) cost.
   - So bad balls can be produced in any number at negligible cost. Badness in the \(C^{2,\alpha}\) sense is not a cost‑bearing notion.
2. **Per‑ball load is controlled only by the global budget.** The weighted relation bounds \(\int|W^+|^2\le2\pi^2(A-k)+P/4\) and \(\hat V\le6\pi^2(A-k)+\tfrac34P\). Without a Ricci lower bound there is no Bishop–Gromov control, so a unit \(\hat g\)‑ball can carry \(O(A)\) volume, Weyl energy and many exceptional classes.
   - **Correction to the model cited.** Gibbons–Hawking multi‑centres carry \((-2)\)‑classes. A \((-1)\)‑carrying model is the scalar‑flat Kähler ALE metrics on \(\mathbb C^2\) blown up at several points (LeBrun's hyperbolic‑ansatz family), scaled into one small ball.
3. **No canonical marking.** Without a reference map, \(\Delta V\) is a global number with no local density.

### C2. A per‑ball load bound would still not suffice with Theorem K

Step 49 states that a count follows once a per‑ball bound is added. Suppose every bad ball has \(V_B\le v_0\) and \(\int_B|W^+|^2\le w_0\). The bad term in Step 49's inequality is then linear in the number \(N\) of bad balls, which is correct.

The good term is the obstacle. It is \(\sqrt{\mathrm{Vol}(G)\,C\,P(G_1)}\sim\sqrt{A\,P(G_1)}\). It exceeds \((1-c)k\) as soon as \(P(G_1)\gtrsim k^2/A\), which is compatible with \(P\le8\pi^2ck\) when \(k\ll A\).

A uniformly \(\varepsilon\)‑close bulk with \(\varepsilon\sim\sqrt{k/A}\) carries \(P\sim k\) and Theorem‑K weight \(\sim\sqrt{kA}\gg k\), with \(N=0\). This is the \(L^1\)/\(L^2\) mismatch that Theorem Y was built to remove.

The term \(\varepsilon_0^2V_{\rm margin}\) can likewise be \(\gg k\). A linear count therefore needs both:
- per‑ball load bounds; and
- the Theorem‑Y localization of the good region (48.L, Lemma 48.5, 48.LY), which in turn needs a marked CH bulk.

### C3. Missing flux term

Step 49 §3 states "\(|\Delta V_{\rm bulk}|\le C(P+\Lambda^2)\)". Lemma 48.5 gives
\[
\Delta V_{\rm bulk}=\tfrac1{24}\oint\partial_\nu\operatorname{tr}h+O(\|h\|^2_{H^2}).
\]
I rechecked the coefficient: Bianchi gauge gives \(s'=\tfrac12(\Delta+12)\operatorname{tr}h\), and the factor becomes \(\tfrac14\) at \(s=-4\). The flux is linear in \(h\). The quadratic estimate holds only for the flux‑corrected bulk excess, as in 48.LY's definition of \(\Delta V_U\).

### C4. Weighted statements the inputs actually justify

**(i) Unconditional, from (Y0), Theorem Y and Y1.** If \(P\le8\pi^2ck\), then
\[
\Delta V\ge2\pi^2(1-c)k+\tfrac59\int\operatorname{dist}^2,\qquad
D_W=\Delta V+\tfrac14(8\pi^2k-P)\ge4\pi^2(1-c)k .
\]
Since \(\tfrac23-|W^+|^2\le\tfrac23\), for every \(\delta>0\)
\[
\operatorname{Vol}_{\hat g}\{\,|W^+|^2\le\tfrac23-\delta\,\}\ \ge\ \tfrac32\bigl(4\pi^2(1-c)k-\delta\hat V\bigr),\qquad \hat V\le6\pi^2(A-k)+\tfrac34P .
\]
This gives a Weyl‑depleted set of volume linear in \(k\), but only at depletion threshold \(\delta\lesssim k/A\). It is a weight, not a count.

**(ii) Near‑CH, ball‑quotient host with marked bulk (48.LY).**
\[
4\Delta V_U\ \ge\ 8\pi^2k-(1+C)P-C\Lambda^2 .
\]
Because \(P\) reappears with constant \(C\), this forces linear core excess only for \(c<1/(1+C)\). The Step‑48 gloss "unless the cores carry \(\sim2\pi^2(1-c)k\)" should read \(2\pi^2(1-(1+C)c)k\). It is still linear in \(k\) with no \(\sqrt A\) loss, so it is the strongest localized statement currently justified.

### C5. What remains unresolved

Two inputs are missing. Both are needed together; neither suffices alone.
- **A ball count** needs an energy‑defined notion of badness, e.g. local \(\int_B\Psi\), \(\int_B\operatorname{dist}^2\), or flux‑corrected local \(\Delta V\), together with quantization or a per‑ball upper load. This is what an approximate Euler–Lagrange equation and small‑energy regularity would supply.
- **The good region** must be handled through Theorem Y and flux‑corrected volume, not through Theorem K.

The note establishes non‑derivability from the present inputs. It does not prove that the count is false; no metric realizing order‑\(k\) saving with \(O(1)\) bad balls has been constructed.
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 49,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step49_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step49_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematical substance and normalization of Step 49's two principal results. (A) Read the Step-48 Theorem-Y definitions, the new Step-49 note/script/data, and the A01 Step-43 ledger note. Check the conversion among delta W, D_W, Delta V, the spectral integrals Psi/dist^2/splitting, and the conclusion that the certified cell is far from Theorem-Y/LeBrun equality. Identify any formula or normalization error. (B) Check the handwritten exact first-order derivation for the nu=4 triaxial diagonal Bianchi-IX Einstein tail, especially e^{4r} delta W+=diag(-12,12,0) at Ric=-6 and the scalar--4 conclusions delta mu_min=delta|W+|^2=0, sigma=2 eps e^-4r, Psi=16 eps^2 e^-8r. Provide corrected formulas if needed. (C) Assess whether the stated obstruction to an unconditional linear bad-ball count is mathematically valid from the available hypotheses: can critical L2 Ricci defect plus Theorem K/closed identity force linearly many unit balls not C2a-close to CH, absent an Euler-Lagrange equation or per-ball load bound? Focus on correctness and any stronger unconditional weighted statement actually justified.

## Integrated Scientific Memo

# Step 49 verification memo

## A. Cell ledger and Theorem‑Y normalization

### A.1 Correct conversion formulas

At scalar curvature \(s=-4\), the complex-hyperbolic/Kähler model has
\[
\operatorname{spec}(W^+)=\left(-\frac23,\frac13,\frac13\right),
\qquad |W^+|^2=\frac23 .
\]
Writing all integrals in units of \(8\pi^2\), the relative cell Weyl deficit is
\[
\delta\bar W
=\frac1{8\pi^2}\left(
\int_{\rm CH}|W^+_{\rm CH}|^2-\int_{\rm cell}|W^+|^2
\right).
\]
Because the reference density \(2/3\) also changes with relative volume,
\[
\boxed{\bar D_W=\delta\bar W+\frac23\bar\Delta V.}
\]
The closed identity
\[
8\pi^2k-P=4D_W-4\Delta V
\]
therefore becomes, for one formally replicated cell,
\[
\boxed{
1-\bar P(\hat g)
=4\bar D_W-4\bar\Delta V
=4\delta\bar W-\frac43\bar\Delta V.}
\]

Thus the old numbers \(0.07513\) and \(0.07080\) are respectively
\[
4\delta\bar W,\qquad \frac43\bar\Delta V,
\]
not \(4\bar D_W\) and \(4\bar\Delta V\).

Using the Step‑49 script’s imported ledger,
\[
\bar\Delta V=0.05310615828,\qquad
1-\bar P(\hat g)=0.00433914896,
\]
gives
\[
\bar D_W=\bar\Delta V+\frac{1-\bar P(\hat g)}4
       =0.05419094552,
\]
hence
\[
4\bar D_W=0.2167637821,\qquad
4\bar\Delta V=0.2124246331.
\]
Their difference is exactly \(0.00433914896\).

The superseding A01 tail-free ledger instead gives approximately
\[
\bar\Delta V=0.0530963,\qquad
\delta\bar W=0.0187835,\qquad
4\bar D_W\simeq0.216724,\quad
4\bar\Delta V\simeq0.212385.
\]
The \(10^{-5}\)-level discrepancy belongs to the older finite-grid relative-volume value imported by the Step‑49 script. Consequently, the script’s label `stable_ledger` is misleading: A01 Step 43’s tail-free identity is the authoritative volume ledger.

A second bookkeeping point is that
```text
fourDeltaWplus = -0.075147...
```
is defined in the script as
\[
-4\left(\bar D_W-\frac23\bar\Delta V\right)=-4\delta\bar W.
\]
It has the opposite sign from the positive deficit \(4\delta\bar W\) used in the prose.

Finally, the script does not independently measure \(D_W\): it sets
\[
\bar D_W=\bar\Delta V+\frac14(1-\bar P(\hat g)),
\]
thereby imposing the closed identity. The independent consistency evidence is the A01 Weyl/signature calculation and tail-free volume computation.

### A.2 Conformal and spectral normalization

The script’s conformal scaling is correct. Starting from the \(\operatorname{Ric}=-6g\), \(s=-24\) metric, first pass to \(u^2g\), then multiply the metric by \(6\). As an endomorphism of \(\Lambda^+\),
\[
W^+_{\hat g}=\frac{1}{6u^2}W^+_g,\qquad
d\mu_{\hat g}=36u^4\,d\mu_g.
\]
The code
```python
eig_hat = Wplus/(6*uconf**2)
mhat = 9*measure*uconf**4
```
is consistent because its internal radial `measure` is four times \(d\mu_g/(8\pi^2)\). Likewise,
```python
Pnorm = integ(ric0sq/4)
```
has the correct \(8\pi^2\) normalization.

For sorted eigenvalues \(\mu_1\le\mu_2\le\mu_3\), define
\[
x=-\mu_1,\qquad \sigma=\frac{\mu_3-\mu_2}{2}.
\]
Then
\[
\operatorname{dist}(W^+,\mathcal K)^2
=(\mu_1+\tfrac23)^2+(\mu_2-\tfrac13)^2+(\mu_3-\tfrac13)^2
\]
is the correct Hoffman–Wielandt orbit distance, and
\[
\Psi=
\begin{cases}
\frac53h^2+\frac4{27}h^3+4\sigma^2,
&h=\frac23-x\ge0,\\[2mm]
3t^2+4\sigma^2,
&t=x-\frac23\ge0.
\end{cases}
\]
Hence the script’s `upper_pair_splitting_contribution_4sigma2` is exactly the splitting component of \(\Psi\).

The numerical values
\[
\bar\Psi=0.01323261190,\qquad
\overline{\operatorname{dist}^2}=0.00750240585,
\]
\[
\overline{4\sigma^2}=0.01092171560,\qquad
\frac{\bar\Psi}{\overline{\operatorname{dist}^2}}=1.76378247
\]
are internally consistent with
\[
\Psi\ge\frac{10}{9}\operatorname{dist}^2,\qquad \Psi\ge4\sigma^2.
\]
Approximately \(82.5\%\) of the measured \(\Psi\) comes from upper-pair splitting.

These spectral values are stable floating quadrature, not interval certificates. The existing rigorous certificate concerns the original cell’s Ricci-defect cost, not these new \(\Psi\) and distance integrals.

### A.3 Equality comparison

Using the script ledger,
\[
4\bar\Delta V-2\bar\Psi
=0.1859594093,
\]
while
\[
1-\bar P(\hat g)=0.0043391490.
\]
Thus the Theorem‑Y slack is
\[
0.1816202604.
\]
For LeBrun’s magnitude penalty,
\[
\frac49\overline{\int(\sqrt6|W^+|-2)^2}
=0.00429707163,
\]
so
\[
4\bar\Delta V-\text{LeB}=0.2081275615,
\]
with slack \(0.2037884125\).

Therefore the cell is decisively far from Theorem‑Y equality. It is also far from the zero-period version of LeBrun equality. For an actual closed replica, the full LeBrun right side additionally contains \(-16\pi^2\Pi_g\), i.e. \(-2\Pi_g\) in the barred normalization. Thus an unconditional statement about distance from full LeBrun equality requires control of the replica’s period term; the isolated cell data alone do not supply that.

The efficiency
\[
\frac{1-\bar P(\hat g)}{4\bar\Delta V}
\simeq0.0204
\]
is correct: only about \(2\%\) of \(4\Delta V\) appears as direct saving.

One displayed check is erroneous: the repeated “consistency ceiling”
\[
2\bar\Psi<0.0332
\]
does not follow from Theorem Y. The actual condition is
\[
2\bar\Psi\le4\bar\Delta V-(1-\bar P(\hat g))
\simeq0.20809.
\]
The number \(0.0332\) was inherited from the former misidentification of \((4/3)\Delta V\). The conclusion of ample slack remains true, but that ceiling should be deleted.

The prose also overloads \(x\): \(x=-\mu_{\min}\) is a spectral parameter, while \(x=0.03,\ldots,128\) is the radial profile coordinate. These must be distinguished.

---

## B. The \(\nu=4\) triaxial Einstein tail

Let
\[
s=\sinh r,\qquad c=\cosh r,\qquad q=e^{-4r},
\]
and perturb
\[
A=s(1+\varepsilon q),\qquad
B=s(1-\varepsilon q),\qquad
C=sc .
\]
Here \(r\) is the geodesic radial coordinate in the \(\operatorname{Ric}=-6g\) normalization.

For the CH background,
\[
v_1=v_2=0,\qquad v_3=3s^2.
\]
At first order,
\[
\dot v_1=d=4q\left(\frac1c-s\right),\qquad
\dot v_2=-d,\qquad
\dot v_3=0,
\]
where the dot denotes the coefficient of \(\varepsilon\). Substitution in
\[
R^+_{ii}
=-\frac{v_i'}{2A_i}
+\frac{-v_i-v_jv_k/2}{A_jA_k}
\]
gives
\[
\dot R^+_{11}
=-\frac{d'}{2s}
+\frac{d(3s^2/2-1)}{s^2c},
\qquad
\dot R^+_{22}=-\dot R^+_{11},
\qquad
\dot R^+_{33}=0.
\]
Since this variation is trace-free, \(\dot s=0\) and \(\dot W^+=\dot R^+\). Its asymptotic expansion is
\[
\dot R^+_{11}=-12e^{-4r}+O(e^{-6r}),
\]
so
\[
\boxed{
e^{4r}\dot W^+
\longrightarrow\operatorname{diag}(-12,12,0)}
\]
at \(\operatorname{Ric}=-6g\). This coefficient is correct.

After scaling the metric by \(6\) to scalar curvature \(-4\),
\[
W^+_0=\operatorname{diag}\left(\frac13,\frac13,-\frac23\right),
\]
and
\[
W^+_\varepsilon
=
W^+_0+
\varepsilon e^{-4r}\operatorname{diag}(-2,2,0)
+O(\varepsilon e^{-6r})+O(\varepsilon^2e^{-8r}).
\]
Consequently,
\[
\left.\frac{d}{d\varepsilon}\right|_0\mu_{\min}=0,\qquad
\left.\frac{d}{d\varepsilon}\right|_0|W^+|^2=0.
\]
These are first-variation statements, not exact finite-\(\varepsilon\) equalities.

For the signed splitting coordinate one may write
\[
\widetilde\sigma
=2\varepsilon e^{-4r}
+O(\varepsilon e^{-6r})
+O(\varepsilon^2e^{-8r}).
\]
For the script’s sorted, nonnegative half-gap,
\[
\boxed{
\sigma
=2|\varepsilon|e^{-4r}
+O(|\varepsilon|e^{-6r})
+O(\varepsilon^2e^{-8r}).}
\]
Thus Step 49’s formula omitted a linear but faster-decaying \(O(\varepsilon e^{-6r})\) term and, for sorted \(\sigma\), the absolute value.

The resulting leading formulas are
\[
\operatorname{dist}(W^+,\mathcal K)
=2\sqrt2\,|\varepsilon|e^{-4r}
+O(|\varepsilon|e^{-6r})+O(\varepsilon^2e^{-8r}),
\]
and
\[
\boxed{
\Psi
=16\varepsilon^2e^{-8r}
+O(\varepsilon^2e^{-10r})+\text{higher orders in }\varepsilon .}
\]
Hence the substantive conclusion is correct:

- with shell volume growing as \(e^{4r}\), the Theorem‑K \(L^1\) orbit departure is marginal and accumulates linearly in tail length;
- the Theorem‑Y quadratic penalty is integrable.

The same statement in the scalar-\(-4\) metric’s geodesic radius \(\hat r=\sqrt6\,r\) uses \(e^{-4\hat r/\sqrt6}\); one should not silently reuse \(r\) after constant rescaling.

---

## C. The bad-ball claim

### C.1 No unconditional linear count follows

From the available hypotheses one cannot infer \(ck\) pairwise disjoint unit balls that fail to be \(C^{2,\alpha}\)-close to CH.

1. **No elliptic regularity mechanism.**  
   A scalar-normalized arbitrary metric does not solve a critical elliptic curvature equation. Small local
   \[
   \int|\operatorname{Ric}^{\circ}|^2
   \]
   therefore does not imply \(C^{2,\alpha}\) proximity to CH. Theorem 48.L assumes a marked region, nonlinear gauge, and uniform \(C^{2,\alpha}\) closeness; it does not produce these from small defect.

2. **No per-ball load bound or topological quantization.**  
   Theorem K controls the total \(L^1\) orbit departure, but the available results do not bound the Weyl energy, volume, interface flux, or exceptional topology carried by one unit ball. Order-\(k\) weight can therefore concentrate in \(O(1)\) regions.

3. **No canonical CH marking.**  
   An arbitrary metric on \(X\#k\overline{\mathbb{CP}}^{\,2}\) has no supplied reference map identifying a coherent CH bulk. Independent local CH comparisons need not patch into the marked setting required by Theorem 48.LY.

Moreover, a per-bad-ball upper load by itself is not sufficient if the argument still uses only Theorem K: the nominally good region may absorb an order-\(k\), or larger, \(L^1\) signal through the \(L^1/L^2\) mismatch. One also needs a Theorem‑Y/flux-corrected localization of the good region, or an equivalent mechanism suppressing diffuse good-region weight.

The present results therefore prove non-derivability from the stated inputs, not falsity of every possible bad-ball theorem.

### C.2 Unconditional weighted statements

Let
\[
d_K=\operatorname{dist}(W^+,\mathcal K),\qquad
\mathcal L=\frac{(8\pi^2k-P)_+}{4\sqrt6/3}.
\]
Theorem K yields
\[
\mathcal L\le\int_M d_K.
\]
Since
\[
d_K^2\le2|W^+|^2+\frac43
\]
and, at \(s=-4\),
\[
\int_M\left(|W^+|^2+\frac13\right)
=2\pi^2(A-k)+\frac14P,
\]
one obtains
\[
\int_Md_K^2\le8\pi^2(A-k)+P
\]
and hence
\[
\boxed{
\mathcal L^2
\le
\operatorname{Vol}(M)\,[8\pi^2(A-k)+P].}
\]

For a threshold set \(B_\tau=\{d_K>\tau\}\),
\[
\boxed{
\operatorname{Vol}(B_\tau)
\ge
\frac{(\mathcal L-\tau\operatorname{Vol}M)_+^2}
{8\pi^2(A-k)+P}.}
\]
This is an unconditional lower bound on weighted departure volume, not on the number of unit balls.

If a marked good region \(G\) already satisfies
\[
E_G:=\int_Gd_K^2
\le C\bigl(P(G_1)+\varepsilon_0^2V_{\rm margin}\bigr),
\]
and \(B=M\setminus G\), then
\[
\boxed{
\bigl(\mathcal L-\sqrt{V_GE_G}\bigr)_+^2
\le
V_B\left(2\int_B|W^+|^2+\frac43V_B\right).}
\]
This is the justified weighted concentration alternative.

Theorem Y also gives, whenever \(P\le8\pi^2ck\),
\[
\boxed{
\Delta V\ge2\pi^2(1-c)k+\frac59\int d_K^2,}
\]
and Y0 gives
\[
D_W=\Delta V+\frac14(8\pi^2k-P)
\ge4\pi^2(1-c)k.
\]
These are strong global weighted statements, but again contain no atom count.

### C.3 Flux correction

The Step‑49 assertion
\[
|\Delta V_{\rm bulk}|\le C(P+\Lambda^2)
\]
is not correct for the uncorrected bulk volume. Lemma 48.5 gives, at \(s=-24\),
\[
\Delta V_{\rm bulk}
=\frac1{24}\oint_{\partial\Omega}\partial_\nu\operatorname{tr}h
+O(\|h\|_{H^2}^2),
\]
or coefficient \(1/4\) after scaling to \(s=-4\). The boundary flux is linear. Only the **flux-corrected** bulk excess, as incorporated in the definition of \(\Delta V_U\) in Theorem 48.LY, is quadratically controlled by \(P+\Lambda^2\).

## Final verdict

- The main \(\delta W\)-\(D_W\)-\(\Delta V\) conversion, conformal scaling, spectral formulas, and conclusion that the cell is far from Theorem‑Y equality are correct.
- The old \(0.0332\) “ceiling” is erroneous and should be removed.
- The script’s \(D_W\) is identity-derived, its `stable_ledger` label is outdated, and `fourDeltaWplus` has the opposite sign from the prose convention.
- The triaxial coefficient
  \[
  e^{4r}\dot W^+\to\operatorname{diag}(-12,12,0)
  \]
  and the leading conclusions
  \[
  \dot\mu_{\min}=0,\qquad \dot{|W^+|^2}=0,\qquad
  \Psi\sim16\varepsilon^2e^{-8r}
  \]
  are correct. The splitting remainder must include \(O(\varepsilon e^{-6r})\), and sorted \(\sigma\) has leading term \(2|\varepsilon|e^{-4r}\).
- Critical \(L^2\) Ricci defect, Theorem K, and the closed identity do not force linearly many non-CH unit balls without additional variational regularity, coherent marking, good-region localization, and per-atom load/quantization. The valid unconditional conclusions are weighted integral or departure-volume estimates, not a ball count.
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 47,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step47_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step47_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the new Step-47 formal common-mode calculation in scalar -4 normalization. Starting only from the Step-40 formal formulas r=2-h, beta=16/r-5-12/r^2, r^2 V=8 pi^2 A, W+(n,n)=4/3-r, and Kähler orbit spectrum (-2/3,1/3,1/3), compute P/(8 pi^2 k), pointwise and integrated distance to the orbit, Theorem-K threshold, and their ratio. Check all factors and determine asymptotic saturation as h=k/A ->0. Then assess whether the proposed two-scale inference P~k^2/A follows only as a compatible model or from any proved inequality. Give exact corrections if needed.

## Integrated Scientific Memo

## Verification of the Step‑47 common-mode calculation

Set
\[
h=\frac{k}{A},\qquad r=2-h,
\]
and use the Step‑40 formal identities
\[
\frac{P}{8\pi^2}=k-A\beta(r)=A\bigl(h-\beta(r)\bigr),\qquad
\beta(r)=\frac{16}{r}-5-\frac{12}{r^2}.
\]

### 1. Exact formal value of \(P\)

Substitution gives
\[
\beta(2-h)
=\frac{16(2-h)-5(2-h)^2-12}{(2-h)^2}
=\frac{h(4-5h)}{(2-h)^2}.
\]
Therefore
\[
h-\beta(2-h)
=\frac{h^2(1+h)}{(2-h)^2},
\]
and hence
\[
\boxed{\frac{P}{8\pi^2}
=A\frac{h^2(1+h)}{(2-h)^2}},
\qquad
\boxed{\frac{P}{8\pi^2k}
=c(h)=\frac{h(1+h)}{(2-h)^2}}.
\]
Equivalently,
\[
\boxed{
P=8\pi^2\frac{k^2}{A}\frac{1+h}{(2-h)^2}}.
\]

For \(h\to0\),
\[
\frac{1+h}{(2-h)^2}
=\frac14+\frac12h+\frac{7}{16}h^2+O(h^3),
\]
so
\[
\boxed{
P=2\pi^2\frac{k^2}{A}
\left(1+2h+\frac74h^2+O(h^3)\right)}
\]
and
\[
c(h)=\frac h4+\frac{h^2}{2}+\frac{7h^3}{16}+O(h^4).
\]
Thus the formal profile has leading scalar-\(-4\) coefficient \(2\pi^2\).

---

### 2. Weyl spectrum and pointwise orbit distance

The datum
\[
W^+(n,n)=\frac43-r=-\frac23+h
\]
alone does **not** determine the full orbit distance. One must also use the Step‑40 axial common-mode ansatz
\[
M=\operatorname{diag}(x,-x/2,-x/2),
\]
which forces equal transverse eigenvalues. With this ingredient,
\[
W_h^+
=\operatorname{diag}\left(
-\frac23+h,\,
\frac13-\frac h2,\,
\frac13-\frac h2
\right).
\]
Relative to the Kähler-orbit element with the same distinguished direction,
\[
W_*=\operatorname{diag}\left(-\frac23,\frac13,\frac13\right),
\]
one has
\[
W_h^+-W_*
=\operatorname{diag}\left(h,-\frac h2,-\frac h2\right).
\]

Using the Frobenius norm,
\[
\boxed{
\operatorname{dist}(W_h^+,\mathcal K)
=\sqrt{h^2+2(h/2)^2}
=\sqrt{\frac32}\,h.}
\]
For \(0<h<1/3\), the eigenvalue ordering is unchanged, so the closest orbit element is indeed the one aligned with \(n\).

Since
\[
r^2V=(2-h)^2V=8\pi^2A,
\qquad
V=\frac{8\pi^2A}{(2-h)^2},
\]
the integrated \(L^1\) distance is
\[
\boxed{
D_{\mathcal K}
:=\int_M\operatorname{dist}(W^+,\mathcal K)\,d\mu
=\frac{4\sqrt6\,\pi^2k}{(2-h)^2}.}
\]
Its expansion is
\[
D_{\mathcal K}
=\sqrt6\,\pi^2k
\left(1+h+\frac34h^2+O(h^3)\right).
\]

---

### 3. Theorem‑K threshold

Theorem K states
\[
8\pi^2k-P
\le \frac{4\sqrt6}{3}\,D_{\mathcal K}.
\]
For \(P=8\pi^2kc(h)\), this requires
\[
D_{\mathcal K}\ge
\sqrt6\,\pi^2(1-c(h))k.
\]
Now
\[
1-c(h)
=1-\frac{h(1+h)}{(2-h)^2}
=\frac{4-5h}{(2-h)^2}.
\]
Hence the exact threshold is
\[
\boxed{
D_{\min}
=\frac{\sqrt6\,\pi^2(4-5h)k}{(2-h)^2}.}
\]
As \(h\to0\),
\[
D_{\min}
=\sqrt6\,\pi^2k
\left(1-\frac h4-\frac{h^2}{2}+O(h^3)\right).
\]

---

### 4. Saturation ratio

The exact ratio is
\[
\boxed{
\frac{D_{\mathcal K}}{D_{\min}}
=\frac{4}{4-5h}.}
\]
Therefore
\[
\frac{D_{\mathcal K}}{D_{\min}}
=1+\frac54h+\frac{25}{16}h^2+O(h^3)
\longrightarrow1
\qquad(h\to0).
\]
At \(h=1/3\),
\[
\frac{D_{\mathcal K}}{D_{\min}}=\frac{12}{7}.
\]

The absolute excess is
\[
\boxed{
D_{\mathcal K}-D_{\min}
=\frac{5\sqrt6\,\pi^2kh}{(2-h)^2}
=\frac{5\sqrt6}{4}\pi^2\frac{k^2}{A}
+O\!\left(\frac{k^3}{A^2}\right).}
\]
Thus relative saturation requires only \(k/A\to0\); the absolute excess tends to zero only under the stronger condition \(k^2/A\to0\).

There is also the exact profile identity
\[
\boxed{
\frac{4\sqrt6}{3}D_{\mathcal K}-(8\pi^2k-P)
=\frac{5}{1+h}P,}
\]
so the Theorem‑K slack is itself of order \(k^2/A\).

All Step‑47 numerical factors
\[
\sqrt{\frac32},\qquad 4\sqrt6,\qquad \sqrt6,\qquad
\frac4{4-5h}
\]
are correct.

---

## Meaning of the saturation

The correct statement is:

> The formal common mode asymptotically saturates the **pointwise algebraic inequality underlying Theorem K** as \(h\to0\).

It should not be presented as an actual closed near-equality family. In the formal state, \(\rho=r>0\), \(d\psi=0\), and all sign-family forms coincide, so one obtains a nowhere-zero self-dual harmonic form with null exceptional periods. The supplied Step‑47 account itself invokes Lemma T to exclude such an exact closed configuration. Therefore no closed metric realization of this profile, or of near-equality in Theorem K, has been proved.

The scaling agreement is also not independent evidence for realizability: Theorem K is derived from Theorem W, and the formal profile was constructed to satisfy the Step‑40 identities.

---

## Does \(P\sim k^2/A\) follow from a proved inequality?

No. The supplied results establish only that this is a compatible formal scale.

The common mode gives the conditional statement
\[
\text{if realizable,}\qquad
P\sim2\pi^2\frac{k^2}{A}.
\]
But no actual closed metric family realizing that asymptotic is supplied, and no all-metric estimate
\[
P\ge c_0\frac{k^2}{A}
\]
is proved.

Specifically:

- LeBrun’s bound gives
  \[
  \frac{P}{8\pi^2}\ge k-\frac A3,
  \]
  which is nonpositive and therefore vacuous in \(0<k<A/3\).
- Theorem E shows the existing affine pointwise scheme cannot improve this.
- Theorem K forces an order-\(k\) integrated Weyl-orbit departure when \(P=o(k)\), but does not bound the energetic cost of that departure in terms of \(P\).
- Theorems N and the amplitude identities similarly force Nijenhuis/depletion quantities but do not turn those quantities into a global lower bound for \(P\).
- \(A_C\) is perturbative and applies to the nearby canonical branch on closed complex-hyperbolic hosts. It does not apply globally to blow-ups without the missing localized collar/core and branch-selection theorem.

A global quadratic transport estimate such as
\[
D_{\mathcal K}^{\,2}\le C A P
\]
—or the corresponding Cotton/Nijenhuis estimate—would provide the missing implication when combined with Theorem K. No such all-metric estimate is proved in the supplied material.

---

## Normalization caveat for the conditional Cotton display

Step 47 writes the conditional pair
\[
P\ge \frac{R^2}{\Lambda A},
\qquad
P\ge8\pi^2k-2R,
\]
which correctly implies
\[
P\ge
\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2
\sim
\frac{16\pi^4}{\Lambda}\frac{k^2}{A}.
\]
This algebra is correct **for that normalization of \(R\)**.

However, if \(R\) is intended to be the Step‑40 quantity
\[
R_{W_2}=\mathbb E\int\rho^2|\nabla n|_{W_2}^2,
\]
then Theorem N gives
\[
8\pi^2k-P\le\frac12R_{W_2},
\qquad\text{i.e.}\qquad
P\ge8\pi^2k-\frac12R_{W_2},
\]
not \(P\ge8\pi^2k-2R_{W_2}\). Under the quadratic hypothesis
\[
P\ge \frac{R_{W_2}^2}{\Lambda A},
\]
the resulting conditional bound is instead
\[
\boxed{
P\ge
\left(
\sqrt{\frac{\Lambda A}{16}+8\pi^2k}
-\sqrt{\frac{\Lambda A}{16}}
\right)^2.}
\]
Thus Step 47 must define \(R\) next to its Cotton display. The apparent discrepancy is a normalization issue, but it changes \(\Lambda\) by a factor of \(16\).

For the formal profile,
\[
R_{W_2}=16\pi^2k
\]
and
\[
\frac{R_{W_2}^2}{AP}
=\frac{32\pi^2(2-h)^2}{1+h}
\longrightarrow128\pi^2.
\]
This calibrates the formal transport constant, but proves no global transport theorem because the profile itself is not a realizable closed state.

## Final assessment

The Step‑47 common-mode arithmetic and Theorem‑K factors are correct, subject to explicitly citing the axial transverse-eigenvalue assumption. The formal mode has
\[
P\sim2\pi^2\frac{k^2}{A}
\]
and asymptotically saturates the pointwise mechanism behind Theorem K. The proposed two-scale law remains a conjectural, model-compatible scale supported by a conditional transport argument—not a consequence of any proved all-metric inequality in the supplied notes.
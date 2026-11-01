# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step47_consolidation_two_scale_program.md",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step45_lemmaM_and_weyl_departure.md"
  ]
}
```

## Task

Independently verify the new Step-47 formal common-mode calculation in scalar -4 normalization. Starting only from the Step-40 formal formulas r=2-h, beta=16/r-5-12/r^2, r^2 V=8 pi^2 A, W+(n,n)=4/3-r, and Kähler orbit spectrum (-2/3,1/3,1/3), compute P/(8 pi^2 k), pointwise and integrated distance to the orbit, Theorem-K threshold, and their ratio. Check all factors and determine asymptotic saturation as h=k/A ->0. Then assess whether the proposed two-scale inference P~k^2/A follows only as a compatible model or from any proved inequality. Give exact corrections if needed.

## Output

## Scientific verification memo

Let
\[
h=\frac{k}{A},\qquad r=2-h,
\]
and use the Step-40 formal identity
\[
\frac{P}{8\pi^2}=k-A\beta(r)=A\bigl(h-\beta(r)\bigr).
\]

### 1. Formal value of \(P\)

Direct substitution gives
\[
\begin{aligned}
\beta(2-h)
&=\frac{16}{2-h}-5-\frac{12}{(2-h)^2}\\
&=\frac{16(2-h)-5(2-h)^2-12}{(2-h)^2}\\
&=\frac{h(4-5h)}{(2-h)^2}.
\end{aligned}
\]
Therefore
\[
h-\beta(2-h)
=\frac{h(2-h)^2-h(4-5h)}{(2-h)^2}
=\frac{h^2(1+h)}{(2-h)^2}.
\]
Hence
\[
\boxed{\frac{P}{8\pi^2}
=A\frac{h^2(1+h)}{(2-h)^2}}
\]
and, since \(k=Ah\),
\[
\boxed{\frac{P}{8\pi^2k}
=c(h)=\frac{h(1+h)}{(2-h)^2}}.
\]

Equivalently,
\[
P=8\pi^2\frac{k^2}{A}\frac{1+h}{(2-h)^2}.
\]
As \(h\to0\),
\[
\frac{1+h}{(2-h)^2}
=\frac14+\frac12h+\frac7{16}h^2+O(h^3),
\]
so the formal mode has
\[
\boxed{
P=2\pi^2\frac{k^2}{A}
\left(1+2h+\frac74h^2+O(h^3)\right)}
\]
and
\[
c(h)=\frac h4+\frac{h^2}{2}+\frac{7h^3}{16}+O(h^4).
\]

Thus the exact leading coefficient of the formal \(k^2/A\) behavior in scalar-\(-4\) normalization is \(2\pi^2\).

---

### 2. Distance from the scalar-\(-4\) Kähler orbit

The Kähler-orbit representative with distinguished direction \(n\) is
\[
W_*=\operatorname{diag}\left(-\frac23,\frac13,\frac13\right).
\]

The full Step-40 common-mode ansatz is axially symmetric about \(n\): equivalently,
\[
W_h=\operatorname{diag}\left(-\frac23+h,\frac13-\frac h2,\frac13-\frac h2\right).
\]
It can be written
\[
W_h=tW_*,\qquad t=1-\frac{3h}{2}.
\]
In the stated range \(0<h<1/3\), one has \(t>0\), so the closest orbit point has the same distinguished direction. Indeed, writing
\[
K_u=\frac13I-u\otimes u\in\mathcal K,\qquad
q=\langle n,u\rangle^2,
\]
one has
\[
|K_u|^2=\frac23,\qquad
\langle K_n,K_u\rangle=q-\frac13.
\]
Thus \(|tK_n-K_u|^2\) is minimized at \(q=1\).

Consequently,
\[
W_h-W_*=\operatorname{diag}\left(h,-\frac h2,-\frac h2\right),
\]
and the Hilbert–Schmidt distance is
\[
\boxed{
\operatorname{dist}(W_h,\mathcal K)
=\sqrt{h^2+2\left(\frac h2\right)^2}
=\sqrt{\frac32}\,h.}
\]

Using
\[
r^2V=(2-h)^2V=8\pi^2A,
\qquad
V=\frac{8\pi^2A}{(2-h)^2},
\]
the integrated \(L^1\) departure is
\[
\begin{aligned}
D_{\mathcal K}
&=\int_M\operatorname{dist}(W^+,\mathcal K)\,d\mu\\
&=\sqrt{\frac32}\,h\,\frac{8\pi^2A}{(2-h)^2}\\
&=\boxed{\frac{4\sqrt6\,\pi^2k}{(2-h)^2}}.
\end{aligned}
\]

Its small-\(h\) expansion is
\[
D_{\mathcal K}
=\sqrt6\,\pi^2k
\left(1+h+\frac34h^2+O(h^3)\right).
\]

#### Logical dependency of this calculation

The single datum
\[
W^+(n,n)=-\frac23+h
\]
does not by itself determine the orbit distance. For example,
\[
W_d=\operatorname{diag}\left(
-\frac23+h,\,
\frac13-\frac h2+d,\,
\frac13-\frac h2-d
\right)
\]
has the same trace and the same \(W(n,n)\), while for sufficiently small \(d\) its squared distance is
\[
\frac32h^2+2d^2.
\]
The exact value \(\sqrt{3/2}\,h\) therefore uses the axial common-mode specification from Step 40,
\[
M=\operatorname{diag}(x,-x/2,-x/2),
\]
or an equivalent statement that the two transverse eigenvalues coincide. Step 47 should cite this tensorial ingredient explicitly; with it, the displayed spectrum and distance are correct.

---

### 3. Theorem-K threshold

Theorem K states
\[
8\pi^2k-P
\le\frac{4\sqrt6}{3}D_{\mathcal K}.
\]
Thus, if \(P=8\pi^2kc(h)\),
\[
D_{\mathcal K}\ge
\frac{3}{4\sqrt6}\,8\pi^2k(1-c(h))
=\sqrt6\,\pi^2k(1-c(h)).
\]

Now
\[
\begin{aligned}
1-c(h)
&=1-\frac{h(1+h)}{(2-h)^2}\\
&=\frac{(2-h)^2-h(1+h)}{(2-h)^2}\\
&=\frac{4-5h}{(2-h)^2}.
\end{aligned}
\]
Therefore the exact Theorem-K threshold is
\[
\boxed{
D_{\min}
=\frac{\sqrt6\,\pi^2(4-5h)k}{(2-h)^2}.}
\]

Its expansion is
\[
D_{\min}
=\sqrt6\,\pi^2k
\left(1-\frac h4-\frac{h^2}{2}+O(h^3)\right).
\]

---

### 4. Saturation ratio

The ratio of the formal departure to the threshold is
\[
\boxed{
\frac{D_{\mathcal K}}{D_{\min}}
=\frac{4}{4-5h}.}
\]
Hence
\[
\frac{D_{\mathcal K}}{D_{\min}}
=1+\frac54h+\frac{25}{16}h^2+O(h^3),
\]
and at \(h=1/3\),
\[
\frac{D_{\mathcal K}}{D_{\min}}
=\frac{4}{4-5/3}
=\frac{12}{7}.
\]

The absolute excess is
\[
\boxed{
D_{\mathcal K}-D_{\min}
=\frac{5\sqrt6\,\pi^2kh}{(2-h)^2}
=\frac{5\sqrt6}{4}\pi^2\frac{k^2}{A}
+O\!\left(\frac{k^3}{A^2}\right).}
\]

Therefore Theorem K is saturated in the relative sense:
\[
\frac{D_{\mathcal K}}{D_{\min}}\longrightarrow1
\qquad\text{as }h=\frac{k}{A}\to0.
\]
The relative excess is \(O(k/A)\). The absolute excess tends to zero only along sequences for which \(k^2/A\to0\); relative saturation requires only \(k/A\to0\).

All numerical factors in Step 47—the \(\sqrt{3/2}\), \(4\sqrt6\), \(\sqrt6\), and \(4/(4-5h)\)—are correct.

---

### 5. Status of the proposed \(k^2/A\) scale

The calculation establishes the following formal fact:

> If the Step-40 common mode is realizable by the required closed metrics and actual monopole fields, then its curvature cost satisfies
> \[
> P\sim2\pi^2\frac{k^2}{A}.
> \]

It does not establish either an actual metric family with this asymptotic value or a general estimate
\[
P\ge c_0\frac{k^2}{A}.
\]

Theorem K alone gives
\[
D_{\mathcal K}\ge
\frac{3}{4\sqrt6}(8\pi^2k-P),
\]
so it forces order-\(k\) integrated Weyl departure when \(P=o(k)\). It does not price that departure quadratically in \(P\). A global transport estimate of schematic form
\[
D_{\mathcal K}^2\le C\,A\,P
\]
or an analogous estimate for the Cotton/rotation quantity would supply the missing relation and would yield the \(k^2/A\) scale after combination with Theorem K. No such all-metric estimate is proved in the supplied notes.

The conditional pair recorded in Step 47,
\[
P\ge\frac{R^2}{\Lambda A},
\qquad
P\ge8\pi^2k-2R,
\]
does algebraically imply
\[
P\ge
\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2.
\]
Indeed, \(R\le\sqrt{\Lambda AP}\) gives
\[
P\ge8\pi^2k-2\sqrt{\Lambda AP},
\]
and solving the quadratic inequality in \(\sqrt P\) gives the displayed expression. Its expansion is
\[
\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2
=
\frac{16\pi^4}{\Lambda}\frac{k^2}{A}
+O\!\left(\frac{k^3}{A^2}\right).
\]
The first inequality in that pair remains the unproved global transport input outside the perturbative canonical-branch setting.

Accordingly, \(P\asymp k^2/A\) is presently a model-compatible and algebraically well-matched scale. The formal mode, Theorem K, and the conditional Cotton calculation all support the same scaling, but the supplied proved inequalities do not yet establish it for the full metric infimum.
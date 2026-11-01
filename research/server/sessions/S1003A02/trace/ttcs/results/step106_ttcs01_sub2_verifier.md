# TTCS Independent Branch Record

```json
{
  "step_id": 106,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step105_cusp_channel_restored_and_cap_charge_theorem.md",
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Sessions/S1003A02/workspace/scripts/step105_cap_charge_check.py",
    "Sessions/S1003A02/workspace/data/step105/cap_charge_check.json",
    "Knowledge/objects/papers/Hitchin-Thorpe-Inequality-for-Noncompact-Einstein-4--fd6e60eeeaa2--deedf5d03a5f/object.md"
  ]
}
```

## Task

Independently verify Theorem 105.Q and Corollaries 105.L/105.H in the Step-105 note. Check orientation and normalization from Theorem G and Dai–Wei, the scalar-cap vanishing argument, the C_+(Omega) decomposition, the cap contribution to the mixed LeBrun estimate, and the arithmetic 9k+8 sum c <=3A and A/11. Identify any gap or needed repair precisely. Also assess whether (E2) is exactly implied by D(g_i)->0 at a fixed nonzero Einstein normalization plus total-volume convergence.

## Output

## Verification memo for Step-105: Theorem 105.Q, Corollaries 105.L/105.H

### 1. Theorem G sign and cap-charge orientation

The sign convention in Theorem 105.Q is consistent with Step-33 Theorem G.

Step-33 writes
\[
\chi(D)=\int_D e+\mathcal E(\partial D),\qquad 
\int_D L=\tau(D)+\mathcal H(\partial D),
\]
and
\[
\widehat P(D)=C_+(D)-(2\chi+3\tau)(D)+\mathcal Q_+(\partial D),
\qquad 
\mathcal Q_+=2\mathcal E-3\mathcal H .
\]
This follows directly from
\[
2e+3L=\frac1{4\pi^2}\Bigl(2|W^+|^2-\frac12|\mathrm{Ric}^\circ|^2+\frac{s^2}{24}\Bigr).
\]

Let \(L_\rho\) be oriented as \(\partial\Omega_\rho\). The corresponding cut of a cap \(C_j\) carries the reversed orientation, so
\[
\mathcal Q_+(\partial C_j)=\mathcal Q_+(-L_\rho)=-\mathcal Q_+(L_\rho).
\]
Applying Theorem G to \(C_j^{(\rho)}\) and using \(\widehat P(g_i;C_j^{(\rho)})\to0\) gives
\[
\lim_i C_+(g_i;C_j^{(\rho)})
=(2\chi+3\tau)(C_j)+\mathcal Q_+(L_\rho;g_\infty).
\]
Thus the cap charge formula
\[
c_j=(2\chi+3\tau)(C_j)+\sum_{\ell\in J_j}\mathcal Q_+^\infty(L_\ell)
\]
has the correct sign: the link is oriented as part of \(\partial\Omega_\rho\), not as part of the cap.

The script `step105_cap_charge_check.py` implements exactly this convention:
```python
cap_charge(chi, tau, e_out) = 2*chi + 3*tau + Qplus(-e_out),
```
where `e_out` is the Euler number seen from the cap orientation, so \(-e_out\) is the Euler number seen from the Einstein-side orientation. This matches Theorem 105.Q.

---

### 2. Dai–Wei normalization and the circle-bundle charge

For a Dai–Wei fibred end with circle fibre over a closed surface, the relevant index formulas are Dai–Wei Thm 3.5 for fibred cusps and Thm 4.3 for fibred ends with positive-dimensional fibre. In both cases the Euler transgression and the Chern–Simons correction vanish in the end limit, and
\[
\tau=\int L-\frac12\,\mathrm{a}\text{-}\lim\eta .
\]
In Step-33 notation this means
\[
\mathcal E\to0,\qquad 
\mathcal H\to\frac12\,\mathrm{a}\text{-}\lim\eta .
\]

Dai–Wei Thm 5.1 gives, for a circle bundle over a surface with Euler number \(e\),
\[
\frac12\,\mathrm{a}\text{-}\lim\eta=\frac e3-\operatorname{sign}e .
\]
Therefore
\[
\mathcal Q_+^\infty
=2\mathcal E-3\mathcal H
=-3\Bigl(\frac e3-\operatorname{sign}e\Bigr)
=-e+3\operatorname{sign}e .
\]
If the cap-oriented Euler number is \(e_{\rm out}=-e\), then
\[
\mathcal Q_+^\infty
=e_{\rm out}-3\operatorname{sign}e_{\rm out},
\]
and hence
\[
c=(2\chi+3\tau)(C)+e_{\rm out}-3\operatorname{sign}e_{\rm out}.
\]
This is the formula used in Step-105.

The orientation convention is independently fixed by the model checks:

- Taub–NUT, \(W^-=0\) orientation: \((\chi,\tau)=(1,0)\), \(e_{\rm out}=-1\).  
  Formula gives \(c=2+2=4\).  
  Since \(\frac1{8\pi^2}\int |W^+|^2=1\), the \(C_+\)-normalization gives
  \[
  C_+=\frac1{2\pi^2}\int |W^+|^2=4.
  \]

- Taub–NUT, \(W^+=0\) orientation: \(e_{\rm out}=+1\), formula gives \(c=0\).

- Taub-bolt on \(O(-1)\): \((\chi,\tau)=(2,-1)\), \(e_{\rm out}=-1\).  
  Formula gives \(c=1+2=3\), matching the Step-27 value.

- Multi-Taub–NUT \(A_{m-1}\) hyperkähler orientation: \((\chi,\tau)=(m,-(m-1))\), \(e_{\rm out}=m\).  
  Formula gives
  \[
  (2\chi+3\tau)=3-m,\qquad 
  \mathcal Q_+^\infty=m-3,
  \]
  so \(c=0\) for every \(m\). This is the expected invisible hyperkähler charge.

The JSON check records all of these as exact rational equalities, and `all_ok=true`.

One presentational inconsistency: the Step-105 table heading says “independent value of \(C_+\)”, but the Taub–NUT row lists
\[
\frac1{8\pi^2}\int |W^+|^2=1,
\]
whereas the corresponding \(C_+\)-value is \(4\). The mathematical content is correct, but the table should either list \(C_+=4\) or explicitly state the factor-of-four normalization difference.

---

### 3. Scalar vanishing on caps

The scalar argument is valid under the stated exhaustion and volume hypotheses.

For a cap region \(C_j^{(\rho)}\),
\[
\int_{C_j^{(\rho)}}s_i^2
\le
2\int_M(s_i-\bar s_i)^2
+
2\bar s_i^2\,\mathrm{Vol}(g_i;C_j^{(\rho)}).
\]
By (E2),
\[
\int_M(s_i-\bar s_i)^2\to0,
\qquad 
\bar s_i\to s_\infty.
\]
Local convergence on \(\Omega_\rho\) plus total-volume convergence gives
\[
\mathrm{Vol}(g_i;C_j^{(\rho)})
\to
\mathrm{Vol}(g_\infty;\Omega\setminus\Omega_\rho).
\]
Since \(\Omega\) has finite volume and \(\Omega_\rho\uparrow\Omega\),
\[
\mathrm{Vol}(g_\infty;\Omega\setminus\Omega_\rho)\to0.
\]
Therefore the scalar part of the cap \(C_+\)-energy vanishes in the double limit:
\[
\lim_{\rho\to0}\lim_{i\to\infty}
\frac1{96\pi^2}\int_{C_j^{(\rho)}}s_i^2=0.
\]
Consequently
\[
c_j=
\lim_{\rho\to0}\lim_{i\to\infty}
\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W^+_{g_i}|^2,
\]
and \(c_j\ge0\) because it is a limit of \(C_+\)-energies.

A small but important point of order: for fixed \(\rho\), the scalar contribution on the cap need not be zero; it is only forced to disappear after the final \(\rho\to0\) limit. The proof in the note compresses this double-limit structure, but the mathematics is sound once the order of limits is made explicit.

---

### 4. Decomposition of \(C_+(g_\infty;\Omega)\)

For closed \(M\), Theorem G gives
\[
C_+(g_i;M)=(2\chi+3\tau)(M)+\widehat P(g_i;M).
\]
With \(M=X\#k\overline{\mathbb{CP}}^2\),
\[
(2\chi+3\tau)(M)=A-k,
\]
and \(\widehat P(g_i)\to0\), so
\[
C_+(g_i;M)\to A-k.
\]
For each fixed \(\rho\),
\[
C_+(g_i;\Omega_\rho)
=
C_+(g_i;M)-\sum_j C_+(g_i;C_j^{(\rho)}).
\]
Taking \(i\to\infty\) using local \(C^2_{\rm loc}\) convergence on \(\Omega_\rho\),
\[
C_+(g_\infty;\Omega_\rho)
=
A-k-\sum_j \lim_i C_+(g_i;C_j^{(\rho)}).
\]
Then \(\rho\to0\) yields
\[
C_+(g_\infty;\Omega)=A-k-\sum_j c_j.
\]
This part is correct, provided the end charges \(\mathcal Q_+^\infty(L_\ell)\) exist.

---

### 5. The required repair: existence of the end charge limit

The one substantive gap in Theorem 105.Q as written is the assertion that the limit
\[
c_j=\lim_{\rho\to0}\lim_{i\to\infty}C_+(g_i;C_j^{(\rho)})
\]
exists under (E) alone.

For fixed \(\rho\), the limit in \(i\) follows from Theorem G and \(C^2_{\rm loc}\) convergence on \(\Omega_\rho\). But the remaining \(\rho\to0\) limit is equivalent to the existence of
\[
\lim_{\rho\to0}\mathcal Q_+(L_\rho;g_\infty).
\]
The hypotheses (E), as stated, do not themselves supply this. The eta invariant and transgression terms may have nontrivial adiabatic behaviour, and without fibred-end asymptotics or another source of control, the limit need not be determined.

The note partially acknowledges this in its final section: the topological evaluation in §3 uses Dai–Wei fibred-cusp asymptotics, and Theorem 105.Q itself does not use them. But the existence of \(\mathcal Q_+^\infty\) is still part of what must be supplied. A precise repair is:

- state Theorem 105.Q conditionally on the existence of the limits
  \[
  \mathcal Q_+^\infty(L_\ell)=\lim_{\rho\to0}\mathcal Q_+(L_{\ell,\rho};g_\infty),
  \]
  or
- add fibred-cusp/fibred-end asymptotics, bounded-curvature Cheeger–Gromov conditions, or another mechanism giving the adiabatic eta and transgression limits.

With that addition, the proof is complete. Without it, the theorem is correct as a conditional statement but not as a consequence of (E) alone.

---

### 6. LeBrun transfer: constants and cap contribution

Assume the LeBrun estimate
\[
\int_M(s-\sqrt6|W^+|)^2\ge72\pi^2A
\]
holds for the metrics under consideration.

#### Cap contribution

On a cap, scalar energy vanishes in the double limit and
\[
\frac1{2\pi^2}\int |W^+|^2\to c_j.
\]
Thus
\[
\int_{C_j}(s-\sqrt6|W^+|)^2
\to
6\int_{C_j}|W^+|^2
=
12\pi^2 c_j.
\]
Equivalently, by Cauchy–Schwarz,
\[
\int_{C_j}(s-\sqrt6|W^+|)^2
\le
\bigl(\|s\|_{L^2(C_j)}+\sqrt6\|W^+\|_{L^2(C_j)}\bigr)^2
\to12\pi^2c_j.
\]
This is the point where positive-charge caps become visible: they concentrate \(W^+\)-energy, and their contribution to the mixed LeBrun integral is \(12\pi^2c_j\), not zero.

#### Einstein-side contribution

On \(\Omega\), write
\[
\int_\Omega s^2=96\pi^2x,\qquad
\int_\Omega |W^+|^2=2\pi^2y.
\]
Then
\[
C_+(g_\infty;\Omega)=x+y=A-k-\sum_jc_j.
\]
By Cauchy–Schwarz,
\[
\int_\Omega(s-\sqrt6|W^+|)^2
\le
\bigl(\|s\|_{L^2(\Omega)}+\sqrt6\|W^+\|_{L^2(\Omega)}\bigr)^2.
\]
Using the above normalizations,
\[
\|s\|_{L^2(\Omega)}=\sqrt{96\pi^2x},
\qquad
\sqrt6\|W^+\|_{L^2(\Omega)}=\sqrt{12\pi^2y},
\]
so
\[
\int_\Omega(s-\sqrt6|W^+|)^2
\le
12\pi^2(\sqrt{8x}+\sqrt y)^2.
\]
The elementary inequality
\[
(\sqrt{8x}+\sqrt y)^2\le9(x+y)
\]
gives
\[
\int_\Omega(s-\sqrt6|W^+|)^2
\le
108\pi^2(x+y)
=
108\pi^2\Bigl(A-k-\sum_jc_j\Bigr).
\]

#### Global inequality

Combining the Einstein-side and cap contributions,
\[
72\pi^2A
\le
108\pi^2\Bigl(A-k-\sum_jc_j\Bigr)
+
12\pi^2\sum_jc_j.
\]
Divide by \(12\pi^2\):
\[
6A\le9A-9k-9\sum_jc_j+\sum_jc_j
=9A-9k-8\sum_jc_j.
\]
Therefore
\[
\boxed{9k+8\sum_jc_j\le3A}.
\]
This is exactly the stated Corollary 105.L.

The second inequality follows from the scalar estimate
\[
\int_Ms^2\ge32\pi^2A.
\]
Since cap scalar energy vanishes in the limit,
\[
96\pi^2x\ge32\pi^2A,
\]
so
\[
x\ge A/3.
\]
Because \(x\le x+y=A-k-\sum c_j\),
\[
k+\sum_jc_j\le\frac{2A}{3}.
\]
Both inequalities are arithmetically correct.

The only presentational repair is to make the double-limit/limsup argument explicit: at fixed \(\rho\) the cap scalar contribution is small only up to the end volume \(\mathrm{Vol}(g_\infty;\Omega\setminus\Omega_\rho)\), and the final cap estimate uses \(\rho\to0\).

---

### 7. Hopf-cap arithmetic and the \(A/11\) threshold

For an \(S^3\)-Hopf cap in the admissible chirality \(e_{\rm out}=-1\), with \(r\) exceptional classes,
\[
\chi=1+r,\qquad \tau=-r,
\]
so
\[
(2\chi+3\tau)=2-r.
\]
The Einstein-side link has \(e=+1\), hence
\[
\mathcal Q_+^\infty= -1+3=2.
\]
Therefore
\[
c=(2-r)+2=4-r.
\]

If there are \(N\) such caps carrying \(r_1,\dots,r_N\ge1\) classes with \(\sum r_j=k\), then
\[
\sum_jc_j=\sum_j(4-r_j)=4N-k.
\]
Substitute into
\[
9k+8\sum_jc_j\le3A:
\]
\[
9k+8(4N-k)=k+32N\le3A.
\]
Thus
\[
\boxed{k+32N\le3A}.
\]

#### Singleton caps

If each class sits in its own cap, \(N=k\). Then
\[
k+32k=33k\le3A,
\]
so
\[
\boxed{k\le A/11}.
\]
This confirms the \(A/11\) singleton threshold.

#### Four-class caps

If classes are packed four to a cap, \(r_j=4\), each cap has \(c_j=0\). If \(k\) is divisible by four, \(N=k/4\), and
\[
k+32(k/4)=9k\le3A,
\]
so
\[
\boxed{k\le A/3}.
\]
This is the same condition as the smooth case.

For general \(k\), the minimal number of caps with capacity four is \(\lceil k/4\rceil\), so the exact packed condition is
\[
k+32\left\lceil\frac{k}{4}\right\rceil\le3A.
\]
The equality with the smooth threshold occurs when \(4\mid k\).

#### Chirality selection and four-class bound

For the opposite chirality \(e_{\rm out}=+1\), the Einstein-side link has \(e=-1\), so
\[
\mathcal Q_+^\infty=1-3=-2,
\]
and
\[
c=(2-r)-2=-r.
\]
For \(r>0\) this is less than zero, contradicting \(c\ge0\). Hence exceptional classes cannot sit in the opposite \(S^3\)-Hopf chirality.

In the admissible chirality,
\[
c=4-r\ge0
\]
forces
\[
r\le4.
\]
Thus each \(S^3\)-Hopf cap can carry at most four exceptional classes.

Charge-four ball caps, with \(r=0\) and \(e_{\rm out}=-1\), contribute \(c=4\) and further tighten the inequality. Zero-charge ball caps contribute nothing to these aggregate estimates.

The zero-charge four-class cap is therefore not excluded by the charge law or the LeBrun transfer. Its actual geometric realization is a separate construction problem; Step-105 correctly identifies the lattice/spin issue as open rather than treating the charge calculation as an existence theorem.

---

### 8. Does (E2) follow exactly from \(\mathscr D(g_i)\to0\)?

This point depends on the precise definition of \(\mathscr D\), which is not included in the supplied Step-105 text.

The components of (E2) are:
\[
\widehat P(g_i)\to0,
\qquad
\int_M(s_i-\bar s_i)^2\to0,
\qquad
\bar s_i\to s_\infty,
\qquad
\mathrm{Vol}(g_i)\to\mathrm{Vol}(g_\infty).
\]

There are three different situations.

#### 8.1 Full fixed-\(\lambda\) Einstein residual

If the functional is the gauge-fixed full residual
\[
\mathscr D_\lambda(g)
=
\frac1{8\pi^2}\int_M|\mathrm{Ric}_g-\lambda g|^2\,d\mu_g
\]
with fixed \(\lambda=s_\infty/4\), then
\[
\mathrm{Ric}-\lambda g
=
\mathrm{Ric}^\circ+\frac{s-4\lambda}{4}g.
\]
Since \(g\) is orthogonal to \(\mathrm{Ric}^\circ\),
\[
|\mathrm{Ric}-\lambda g|^2
=
|\mathrm{Ric}^\circ|^2+\frac14(s-4\lambda)^2.
\]
Decomposing \(s-4\lambda=(s-\bar s)+(\bar s-4\lambda)\),
\[
\mathscr D_\lambda(g)
=
\widehat P(g)
+
\frac1{32\pi^2}\int_M(s-\bar s)^2
+
\frac{\mathrm{Vol}(g)}{32\pi^2}(\bar s-4\lambda)^2.
\]
If \(\mathscr D_\lambda(g_i)\to0\) and \(\mathrm{Vol}(g_i)\to\mathrm{Vol}(g_\infty)>0\), then all three parts of (E2) follow:
\[
\widehat P(g_i)\to0,\qquad
\int(s_i-\bar s_i)^2\to0,\qquad
\bar s_i\to4\lambda=s_\infty.
\]
In this gauge-fixed sense, the Step-105 sentence is correct.

#### 8.2 Scale-invariant optimal residual

A scale-invariant version is
\[
\mathscr D_{\rm opt}(g)
=
\frac1{8\pi^2}\int_M
\left|\mathrm{Ric}_g-\frac{\bar s_g}{4}g\right|^2d\mu_g.
\]
Then
\[
\mathscr D_{\rm opt}(g)
=
\widehat P(g)
+
\frac1{32\pi^2}\int_M(s-\bar s)^2.
\]
This gives
\[
\widehat P(g_i)\to0,
\qquad
\int(s_i-\bar s_i)^2\to0,
\]
but it does not by itself force
\[
\bar s_i\to s_\infty.
\]
The mean scalar could converge to another constant value. To obtain \(\bar s_i\to s_\infty\), one needs either an explicit normalization fixing the average scalar, or local \(C^2_{\rm loc}\) convergence on a positive-volume subset of \(\Omega\), as in (E1).

Indeed, if (E1) gives \(s_i\to s_\infty\) locally on some \(\Omega_\rho\) of positive limiting volume and \(\int(s_i-\bar s_i)^2\to0\), then
\[
\bar s_i\to s_\infty.
\]
But that uses (E1), not merely total-volume convergence.

#### 8.3 Traceless-Ricci-only functional

If \(\mathscr D\) controls only
\[
\widehat P(g)=\frac1{8\pi^2}\int|\mathrm{Ric}^\circ|^2,
\]
then (E2) does not follow. The Bianchi identity gives
\[
ds=4\,\delta\mathrm{Ric}^\circ
\]
in dimension four, but \(L^2\)-smallness of \(\mathrm{Ric}^\circ\) does not control \(\delta\mathrm{Ric}^\circ\). Thus scalar variance and mean scalar are independent data unless the functional or the normalization controls them.

Total-volume convergence fixes the scale of a scale-invariant problem, but it does not by itself fix the average scalar or force scalar variance to vanish.

#### Conclusion on (E2)

The statement in Step-105 that (E2) is “exactly what \(\mathscr D(g_i)\to0\) gives” is correct only if \(\mathscr D\) is understood as a full Einstein residual that includes both the traceless Ricci part and the scalar-variance part, together with a normalization that pins the mean scalar, or if (E1) is already available to pin the mean scalar. If \(\mathscr D\) is only the traceless Ricci energy, or if the scalar part is not included in \(\mathscr D\), then (E2) is an additional extraction hypothesis.

This matches the final section of Step-105, which lists the derivation of the full structure (E) from an actual \(\mathscr D\to0\) sequence as not supplied by a theorem in the corpus.

---

## Summary of verification

- Theorem G signs and the cap orientation convention are correct.
- The Dai–Wei normalization
  \[
  \mathcal H\to\frac e3-\operatorname{sign}e,
  \qquad
  \mathcal Q_+^\infty=-e+3\operatorname{sign}e
  \]
  is consistent with Step-33 and with the independent Taub–NUT, Taub-bolt, and multi-Taub–NUT checks.
- The scalar-cap vanishing argument is valid, with the double limit made explicit.
- The decomposition
  \[
  C_+(g_\infty;\Omega)=A-k-\sum_jc_j
  \]
  follows correctly from Theorem G and volume convergence.
- The LeBrun transfer constants are correct:
  \[
  9k+8\sum c_j\le3A,
  \qquad
  k+\sum c_j\le\frac{2A}{3}.
  \]
- The Hopf-cap arithmetic is correct:
  \[
  k+32N\le3A,
  \]
  singleton caps give \(k\le A/11\), and four-class zero-charge caps recover the smooth threshold \(k\le A/3\) when \(4\mid k\).
- The main mathematical repair needed is to state that the end-charge limits \(\mathcal Q_+^\infty\) must exist; (E) alone does not prove this without fibred-end asymptotics or equivalent control.
- The implication from \(\mathscr D(g_i)\to0\) to (E2) is exact only for a functional that includes scalar variance and a normalization fixing the mean scalar; otherwise (E2) remains an additional hypothesis.
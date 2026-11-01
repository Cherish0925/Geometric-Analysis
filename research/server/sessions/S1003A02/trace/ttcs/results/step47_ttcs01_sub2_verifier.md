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

# Memo: Step‑47 formal common mode, factor‑by‑factor verification, and the status of the \(k^2/A\) law

**Summary.** Every displayed formula in Step 47 §3 is correct. Theorem K is asymptotically saturated by the formal mode as \(h=k/A\to0\). That saturation is a pointwise algebraic fact, because the profile is not a realizable closed state. The quadratic law \(P\sim k^2/A\) has two supports: compatibility with this profile, and the conditional Cotton inequality. No proved inequality yields it, or any positive \(k\)-dependent lower bound for all metrics, when \(0<k<A/3\). One normalization in the Cotton display needs fixing (§4.2).

Inputs used: \(r=2-h\), \(\beta(r)=16/r-5-12/r^2\), \(P/(8\pi^2)=k-A\beta(r)\), \(r^2V=8\pi^2A\), \(W^+(n,n)=\tfrac43-r\), and the Kähler orbit \(\mathcal K\) with spectrum \((-\tfrac23,\tfrac13,\tfrac13)\). Norms on \(S^2_0\Lambda^+\) are Frobenius. This matches \(|W_0|^2=\rho^4/24\) and \(|M|^2=\tfrac32x^2\) for \(M=\operatorname{diag}(x,-x/2,-x/2)\) in Step 40, and \(|G_{2,\hat\omega}|^2=32/3\) in Step 45.

---

## 1. The algebra

**\(\beta\) and \(c(h)\).** Over the common denominator \((2-h)^2\):
\[
16(2-h)-5(2-h)^2-12=4h-5h^2,
\qquad\text{so}\qquad
\beta(2-h)=\frac{h(4-5h)}{(2-h)^2}.
\]
Then
\[
h-\beta=\frac{h[(2-h)^2-4+5h]}{(2-h)^2}=\frac{h^2(1+h)}{(2-h)^2}.
\]
This gives
\[
\frac{P}{8\pi^2k}=c(h)=\frac{h(1+h)}{(2-h)^2},
\qquad
1-c(h)=\frac{(2-h)^2-h-h^2}{(2-h)^2}=\frac{4-5h}{(2-h)^2}.
\]
The expansion \(\beta=h-\tfrac{h^2}{4}+O(h^3)\) from Step 40 agrees, and gives \(P\simeq 2\pi^2k^2/A\).

**Spectrum of \(W^+\).** Write \(W^+=W_0+M\) with \(W_0=\tfrac{r^2}{4}(I/3-nn)\) and \(x=(2-r)(4-r)/6\).

- Along \(n\): \(-r^2/6+x=\tfrac43-r\). This reproduces the input.
- Orthogonal to \(n\): \(r^2/12-x/2=r/2-\tfrac23\).
- At \(r=2-h\) the spectrum is \((-\tfrac23+h,\ \tfrac13-\tfrac h2,\ \tfrac13-\tfrac h2)\). It is traceless.

**Pointwise distance.** By Hoffman–Wielandt, the nearest point of an orthogonal orbit is codiagonal, with eigenvalues matched in sorted order. The ordering \(-\tfrac23+h\le\tfrac13-\tfrac h2\) holds iff \(h\le\tfrac23\), which covers \(0<h<\tfrac13\). Hence
\[
\operatorname{dist}(W^+,\mathcal K)=\sqrt{h^2+2(h/2)^2}=\sqrt{3/2}\,h.
\]
The nearest \(W_*\) has \(\hat\omega=n\), so \(q=1\).

**Integrated distance.** With \(V=8\pi^2A/(2-h)^2\) and \(\sqrt{3/2}\cdot8=4\sqrt6\):
\[
D_{\mathcal K}=\frac{4\sqrt6\,\pi^2k}{(2-h)^2}.
\]

**Theorem‑K threshold.**
\[
\frac{8\pi^2(1-c)k}{4\sqrt6/3}=\sqrt6\,\pi^2(1-c)k=\frac{\sqrt6\,\pi^2(4-5h)k}{(2-h)^2}.
\]

**Ratio.**
\[
\frac{D_{\mathcal K}}{D_{\min}}=\frac{4}{4-5h}=1+\tfrac54h+O(h^2).
\]
At \(h=\tfrac13\) the ratio is \(12/7\). Equivalently, the saving divided by the Theorem‑K bound is \((4-5h)/4\).

The certified‑cell number also checks: \(\sqrt6\pi^2\approx24.1755\), and \(24.1755\times0.00433727\approx0.104856\).

---

## 2. Independent cross‑checks

**(a) Closed identity.** Use \(P=4\!\int|W^+|^2+\tfrac43V-8\pi^2(A-k)\) with \(|W^+|^2=\tfrac23-2h+\tfrac32h^2\):
\[
\frac{P}{8\pi^2A}=\frac{4-8h+6h^2-(1-h)(4-4h+h^2)}{(2-h)^2}=\frac{h^2(1+h)}{(2-h)^2}.
\]
This matches §1 by a route that does not use \(\beta\).

**(b) Theorem‑W density.** With \(\zeta=0\), \(\mathcal W=0\) and \(|M|^2=\tfrac32x^2\), where \(x=h(2+h)/6\):
\[
f=r^2x-6x^2+\frac{(2-r)(r-1)(3r+2)}3
=\frac{h(2+h)(2-3h)}3+\frac{h(1-h)(8-3h)}3
=h(4-5h).
\]
Then \(Vf=8\pi^2A\beta=8\pi^2k-P\). The profile therefore satisfies Theorem W with equality in every dropped term.

**(c) Nijenhuis energy.** Here \(a=b=v_4=0\) and \(|\nabla n|^2=2h\), all of it of type \(W_2\). So
\[
R_{W_2}=r^2\cdot2h\cdot V=16\pi^2k
\]
exactly, for every \(h\). Theorem N then reads \(\mathfrak S=\tfrac12R_{W_2}-(\text{nonnegative})\). In the limit \(h\to0\) the saving is \(8\pi^2k=\tfrac12R_{W_2}\). This is consistent with the item‑5 bound \(R_{W_2}\ge16\pi^2(1-c)k\).

---

## 3. Why saturation occurs, and what it does and does not show

**Mechanism.** Theorem K comes from
\[
f(W_*+E)=f_0+\langle G_{r,n},E\rangle-4|E|^2,
\]
with \(f_0\le0\), together with the sharp constant \(C_{\mathcal K}=4\sqrt6/3\). In the profile:

- \(E=\operatorname{diag}(h,-h/2,-h/2)\) is positively parallel to \(G\propto\operatorname{diag}(2,-1,-1)\).
- \(q=1\).
- \(r\to2\).

This is exactly the limiting equality state. One new exact fact: at \(q=1\),
\[
|G_{r,n}|^2=\tfrac23(8-r^2)^2,
\qquad\text{so}\qquad
|G_{2-h,n}|=\sqrt{2/3}\,(4+4h-h^2)>C_{\mathcal K}.
\]
The sharp constant survives only because \(f_0=-h^2(3-h)\) compensates. The pointwise slack \(C|E|-f=5h^2\) decomposes as
\[
5h^2=\underbrace{6h^2}_{4|E|^2}+\underbrace{(3h^2-h^3)}_{-f_0}-\underbrace{(4h^2-h^3)}_{\langle G,E\rangle-C|E|}.
\]
Integrated, the slack of Theorem K is
\[
C_{\mathcal K}D_{\mathcal K}-\mathfrak S=\frac{40\pi^2kh}{(2-h)^2}=\frac{5}{1+h}\,P.
\]
So the slack and \(P\) are of the same order \(k^2/A\).

**Why the check is not independent evidence.** Theorem K is a pointwise consequence of Theorem W, and the profile satisfies Theorem W identically. Agreement in scaling is therefore automatic. It confirms the algebra, not a global mechanism.

**The profile is not a closed configuration.** It has constant \(\rho=r>0\) and \(d\psi=0\), so \(\psi\) is a nowhere‑zero self‑dual harmonic form. All the \(\psi_\epsilon\) coincide, which forces \(E_i^+=0\) and hence \(E_i\cdot[\psi]=0\). Lemma T excludes exactly this. Consequently:

- "Sharp at first order" is a statement about the pointwise constant \(C_{\mathcal K}\).
- No closed metric is known that approaches equality in (K3).
- The phrase "nearly saturates Theorem K in the tower limit" should say "pointwise/formally saturates".

---

## 4. Does \(P\gtrsim k^2/A\) follow from anything proved?

### 4.1 The proved inequalities in the open window \(0<k<A/3\)

- **LeBrun.** \(P/(8\pi^2)\ge k-A/3\). This is \(\le0\) in the window, so it gives nothing there.
- **Theorem E.** Affine pointwise combinations reproduce exactly LeBrun's bound and nothing stronger.
- **Kähler theorem.** \(P\ge8\pi^2k\), but only for Kähler metrics. The rotated certified cells show it does not extend to conformally almost‑Kähler metrics.
- **Theorems K, N, the amplitude theorem.** These give lower bounds on departure quantities, namely \(D_{\mathcal K}\), \(R_{W_2}\) and \(L\), conditional on \(P\le8\pi^2ck\). They give no lower bound on \(P\).
- **\(A_C\).** Combined with Theorem N it would give a linear bound, \(P\ge8\pi^2k/(1+C/2)\), which is stronger than \(k^2/A\). But \(A_C\) is stated on closed ball quotients in a uniform \(C^{2,\alpha}_b\) neighbourhood of the complex‑hyperbolic metric. No metric on \(X\#k\overline{\mathbb{CP}}^2\) with \(k>0\) lies in such a neighbourhood globally, because the bolt cores change topology. So \(A_C\) applies to no metric on \(M\) until the localized version (Step 47, §5 item 1) exists.

Conclusion: no proved statement gives \(\inf_gP>0\) for all metrics in the window. The two‑scale law is a compatible model plus a conditional implication.

### 4.2 The conditional Cotton route: algebra and a factor to fix

Suppose \(P\ge R^2/(\Lambda A)\) and \(P\ge8\pi^2k-\mu R\). Then
\[
P\ge\frac{(8\pi^2k-P)^2}{\mu^2\Lambda A},
\]
whose smaller root is
\[
P\ \ge\ \Bigl(\sqrt{\tfrac{\mu^2\Lambda A}{4}+8\pi^2k}-\sqrt{\tfrac{\mu^2\Lambda A}{4}}\Bigr)^2
\ \simeq\ \frac{64\pi^4k^2}{\mu^2\Lambda A}\qquad(k\ll A).
\]
For \(\mu=2\) this is exactly the Step‑47 display, and the algebra is correct.

The issue is the value of \(\mu\). If \(R\) means \(R_{W_2}\), as in dependency‑spine item 5, then Theorem N gives \(\mu=\tfrac12\), not 2. The display then becomes
\[
P\ge\Bigl(\sqrt{\Lambda A/16+8\pi^2k}-\sqrt{\Lambda A/16}\Bigr)^2.
\]
The Step‑43 definition of \(R\) must be stated next to the display; the two choices differ by a factor 16 in \(\Lambda\).

**Calibration from the profile.** With \(R=R_{W_2}=16\pi^2k\) and the exact \(P\):
\[
\frac{P}{R^2/A}=\frac{1+h}{32\pi^2(2-h)^2}
\quad\Longrightarrow\quad
\Lambda_{\rm profile}=\frac{32\pi^2(2-h)^2}{1+h}\to128\pi^2.
\]
With \(\mu=\tfrac12\) and \(\Lambda=128\pi^2\), the formula gives \(64\pi^4k^2/(32\pi^2A)=2\pi^2k^2/A\), the profile's leading \(P\). The profile saturates both inputs of the Cotton route simultaneously. This gives a concrete reference value of \(\Lambda\) for any proposed transport estimate. It is not a lower bound on \(\Lambda\), because the profile is excluded by Lemma T.

### 4.3 Where the quadratic order actually comes from

Expand the closed identity around the Kähler orbit:
\[
P=4\bigl(V-2\pi^2A\bigr)+8\pi^2k+8\!\int\!\langle W_*,E\rangle+4\!\int|E|^2 .
\]
In the profile:

- \(\langle W_*,E\rangle=-h\).
- \(V-2\pi^2A=2\pi^2A\,h(4-h)/(2-h)^2\).

At first order the three linear terms are \(+8\pi^2k\), \(+8\pi^2k\) and \(-16\pi^2k\). They cancel, and \(P=O(k^2/A)\) is what remains.

That cancellation is enforced by two facts specific to the profile:

1. The constant‑amplitude, \(\mathcal W=0\) volume law \(r^2V=8\pi^2A\).
2. The Weitzenböck relation \(W^+(n,n)=\tfrac43-r\).

For real solutions these become inequalities: \(\mathcal W\ge0\), \(\rho\le2\), and \(\zeta\)/Walsh remainders. Nothing proved prevents the linear terms from cancelling only partially, or prevents \(P\) from being smaller still.

The missing theorem is therefore a quantitative coupling of three things on closed \(M\):

- volume excess \(V-2\pi^2A\),
- the first moment \(\int\langle W_*,E\rangle\),
- \(\int|E|^2\).

Equivalently, it is the non‑perturbative quadratic transport estimate. Bach stationarity supplies this coupling only perturbatively about an Einstein host.

**A cheap optional sharpening, not verified globally.** Since \(|G|-C\) vanishes to first order as \(h\to0\) and \(\epsilon=1-q\to0\), a bound
\[
f\le C_{\mathcal K}|E|-c|E|^2
\]
may hold with some \(c>0\). It requires pointwise
\[
(|G_{r,n}|-C_{\mathcal K})_+^2\le4(4-c)(-f_0).
\]
Along \(q=1\) at leading order this forces \(c\le28/9\); the \(q\)-direction at \(r=2\) imposes nothing at leading order. If true, it would give \(\mathfrak S\le C_{\mathcal K}D_{\mathcal K}-c\int|E|^2\). That records the \(6h^2\) part of the slack but still bounds departure, not \(P\).

---

## 5. Exact corrections

1. **Arithmetic in §3.** All values are correct: \(c(h)\), \(1-c(h)\), the spectrum, \(\sqrt{3/2}\,h\), \(D_{\mathcal K}=4\sqrt6\pi^2k/(2-h)^2\), \(D_{\min}\), the ratio \(4/(4-5h)\), and \(12/7\). Two points should be stated with them:
   - Norms are Frobenius.
   - The orbit distance uses ordered‑eigenvalue matching, valid for \(h\le2/3\).
2. **Wording of "nearly saturates Theorem K".** Replace with "saturates the pointwise inequality behind Theorem K as \(h\to0\)". The profile is Lemma‑T‑excluded, so no closed realization of near‑equality is known.
3. **Cotton display.** Fix the normalization of \(R\). With \(R=R_{W_2}\), Theorem N gives \(P\ge8\pi^2k-R/2\), and the display becomes \(\bigl(\sqrt{\Lambda A/16+8\pi^2k}-\sqrt{\Lambda A/16}\bigr)^2\). Record \(\Lambda_{\rm profile}\to128\pi^2\) as the reference value.
4. **§2 "structural reason".** "Natural diffuse cost quadratic" holds in the profile because the linear terms of the closed identity cancel through \(r^2V=8\pi^2A\) and \(W^+(n,n)=\tfrac43-r\). No proved inequality enforces that cancellation for actual metrics.
5. **\(A_C\).** It currently applies to ball‑quotient metrics, not to any metric on \(X\#k\overline{\mathbb{CP}}^2\) with \(k>0\). The localized collar/branch version is what would make it bear on the blow‑up window.
6. **Optional addition to the note.** The identity \(C_{\mathcal K}D_{\mathcal K}-\mathfrak S=5P/(1+h)\) shows that, in the profile, the Theorem‑K slack and \(P\) are of the same order. A proof of the \(k^2/A\) law must capture both.
# TTCS Independent Branch Record

```json
{
  "step_id": 48,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A02/workspace/notes/step45_lemmaM_and_weyl_departure.md",
    "Sessions/S1003A02/workspace/notes/step47_consolidation_two_scale_program.md",
    "Sessions/S1003A02/workspace/scripts/step48_theoremY.py",
    "Sessions/S1003A02/workspace/data/step48_theoremY.json",
    "Sessions/S1003A02/workspace/data/step48_lemmaP.json",
    "Knowledge/objects/papers/math-0111228-Curvature-Connected-Sums-and-Seiberg-Witten-Theory--84e6ef833958--5b74c8864d85/object.md"
  ]
}
```

## Task

Verify the new Step-48 results in Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md §§1-2 as exact mathematics. Specifically: (1) Proposition 48.1: the algebraic simplification f(W,r,n)=r^2M(n,n)-4|M|^2+p(r) = -r^2W(n,n)-4|W|^2+p(r) with M=W-(r^2/4)(I/3-nn^T), and the explicit sup over r in [0,2] giving phi(x). (2) Lemma 48.2: Psi>=0, Psi=0 exactly on the Kähler orbit, sharp constant 10/9 for Psi>=c dist^2. (3) Theorem Y: check the exact closed identity (Y0) 8π²k−P(ĝ)=4D_W−4ΔV at s≡−4 from C_+=A−k+P/8π² (with C_+=(1/2π²)∫|W+|²+(1/96π²)∫s²), the use of Theorem W/K's averaged pointwise bound (read the step45 note §3 for the saving density and its hypotheses, r∈[0,2]), and the elimination step. (4) The LeBrun comparison (Y-LeB) derived from LeBrun's Proposition 4 ∫(s−√6|W+|)²≥72π²(a+)² with the sign choice (a+)²≥A, and the claimed period lower bound ΔV≥2π²(|K_X^-|²+Σ|E_i^+|²). (5) The three consistency checks: certified cell numbers, formal common mode (P/8π²k=h(1+h)/(2−h)², V̂=8π²A/(2−h)², axial x=2/3−h; Step-47 note gives D_K formulas), rotated cells. Decide whether Corollary Y1 (ΔV≥2π²(1−c)k for P≤8π²ck) and Corollary Y2 (tariff ⇔ D_W−ΔV≤2π²(1−c)k; fields give D_W−ΔV≤ΔV−½∫Ψ) are correct and correctly scoped, and assess honestly how much of Theorem Y is already contained in LeBrun's estimate. Report any sign, normalization or factor errors with corrected statements.

## Output

# Scientific verification memo: Step 48, §§1–2

## 1. Algebraic optimization in Proposition 48.1

Let
\[
P_n=\frac I3-nn^T,\qquad |P_n|^2=\frac23,\qquad
M=W-\frac{r^2}{4}P_n,
\]
with \(W\) traceless symmetric and \(|n|=1\). Since
\[
P_n(n,n)=-\frac23,\qquad \langle W,P_n\rangle=-W(n,n),
\]
one obtains directly
\[
M(n,n)=W(n,n)+\frac{r^2}{6},
\]
and
\[
|M|^2
=|W|^2-\frac{r^2}{2}\langle W,P_n\rangle+\frac{r^4}{16}|P_n|^2
=|W|^2+\frac{r^2}{2}W(n,n)+\frac{r^4}{24}.
\]
Consequently,
\[
\begin{aligned}
r^2M(n,n)-4|M|^2
&=r^2W(n,n)+\frac{r^4}{6}
 -4|W|^2-2r^2W(n,n)-\frac{r^4}{6}\\
&=-r^2W(n,n)-4|W|^2.
\end{aligned}
\]
Thus Proposition 48.1 is exact, including all signs and factors.

For fixed \(r\), the maximizing direction is a lowest-eigenvalue direction of \(W\). Writing
\[
x=-\mu_{\min}(W)\ge0,
\]
the remaining one-variable function is
\[
q_x(r)=xr^2+p(r)
=-r^3+\left(x+\frac73\right)r^2-\frac43,
\]
with
\[
q_x'(r)=r\left(2x+\frac{14}{3}-3r\right).
\]
Hence
\[
r_*=\frac{6x+14}{9}.
\]
For \(0\le x\le2/3\), \(r_*\in[14/9,2]\) and is the maximum on \([0,2]\). For \(x\ge2/3\), \(q_x\) is increasing up to \(r=2\), so the maximum occurs at \(r=2\). At the interior stationary point,
\[
q_x(r_*)=\frac12r_*^3-\frac43,
\]
while \(q_x(2)=4x\). Therefore
\[
\varphi(x)=
\begin{cases}
\dfrac12\left(\dfrac{6x+14}{9}\right)^3-\dfrac43,&0\le x\le\dfrac23,\\[6pt]
4x,&x\ge\dfrac23.
\end{cases}
\]
At \(x=2/3\), both pieces have value \(8/3\), and both derivatives are \(4\). Thus the stated \(C^1\) matching is also correct.

The file `step48_lemmaP.json` should not be used as numerical corroboration of this constrained optimization: its reported maximizing amplitudes \(2.0333\ldots\) and \(2.1243\ldots\) lie outside the admissible interval \(0\le r\le2\). The symbolic derivation above is sufficient.

---

## 2. Exact proof of Lemma 48.2 and the constant \(10/9\)

Order the eigenvalues of \(W\) as
\[
\left(-x,\frac{x}{2}-\sigma,\frac{x}{2}+\sigma\right),
\qquad x\ge0,\quad 0\le \sigma\le\frac{3x}{2}.
\]
Then
\[
|W|^2=\frac32x^2+2\sigma^2.
\]
The exact distance to the \(SO(3)\)-orbit with spectrum
\((-2/3,1/3,1/3)\) is
\[
d_{\mathcal K}(W)^2
=\frac32\left(x-\frac23\right)^2+2\sigma^2.
\]
This follows from the Hoffman–Wielandt formula; the \(SO(3)\) orbit gives the same minimum as orthogonal conjugation.

Set
\[
\Psi(W)=\frac43+2|W|^2-\varphi(x).
\]
For \(0\le x\le2/3\), put \(h=2/3-x\). Direct substitution gives the exact polynomial identity
\[
\boxed{\;
\Psi(W)=\frac53h^2+\frac4{27}h^3+4\sigma^2.
\;}
\]
For \(x\ge2/3\), put \(t=x-2/3\). Then
\[
\boxed{\;
\Psi(W)=3t^2+4\sigma^2.
\;}
\]
These formulas immediately imply
\[
\Psi(W)\ge0,
\]
with equality precisely when \(x=2/3\) and \(\sigma=0\), namely precisely on \(\mathcal K\).

They also prove the global quadratic estimate without any numerical scan:
\[
\Psi-\frac{10}{9}d_{\mathcal K}^2
=
\begin{cases}
\dfrac4{27}h^3+\dfrac{16}{9}\sigma^2,
&0\le x\le\dfrac23,\\[7pt]
\dfrac43t^2+\dfrac{16}{9}\sigma^2,
&x\ge\dfrac23.
\end{cases}
\]
Therefore
\[
\boxed{\;
\Psi(W)\ge\frac{10}{9}\operatorname{dist}(W,\mathcal K)^2.
\;}
\]
The coefficient is sharp because along the axial deficit direction
\(\sigma=0\), \(x=2/3-h\),
\[
\frac{\Psi}{d_{\mathcal K}^2}
=\frac{\frac53h^2+\frac4{27}h^3}{\frac32h^2}
=\frac{10}{9}+\frac8{81}h
\longrightarrow\frac{10}{9}
\qquad(h\downarrow0).
\]
No point outside \(\mathcal K\) realizes the ratio \(10/9\); it is approached from the magnitude-deficit side.

Thus the lemma is correct, but the final numerical-scan sentence in its supplied proof should be replaced by the exact two-case computation above. The value \(1.111102\ldots\) in `step48_theoremY.json`, slightly below \(10/9\), is floating-point cancellation near the orbit rather than mathematical evidence against the exact constant.

---

## 3. Closed identity (Y0) and Theorem Y

Write
\[
I_W=\int_M|W^+_{\hat g}|^2\,d\mu_{\hat g},
\qquad \hat V=\operatorname{Vol}(\hat g).
\]
At \(s_{\hat g}\equiv-4\),
\[
C_+(\hat g)=\frac{I_W}{2\pi^2}+\frac{\hat V}{6\pi^2}.
\]
Combining this with
\[
C_+=A-k+\frac{P(\hat g)}{8\pi^2}
\]
gives
\[
4I_W+\frac43\hat V=8\pi^2(A-k)+P(\hat g).
\]
Hence
\[
8\pi^2k-P(\hat g)
=8\pi^2A-4I_W-\frac43\hat V.
\]
On the other hand,
\[
\begin{aligned}
4D_W-4\Delta V
&=4\left(\frac23\hat V-I_W\right)
 -4(\hat V-2\pi^2A)\\
&=8\pi^2A-4I_W-\frac43\hat V.
\end{aligned}
\]
Therefore
\[
\boxed{\;
8\pi^2k-P(\hat g)=4D_W-4\Delta V.
\;}
\]
The sign and all coefficients in (Y0) are correct.

For an arbitrary representative \(g\) in the same conformal class,
\[
P(g)-P(\hat g)
=\frac1{12}\left(\int_M s_g^2\,d\mu_g-Y[g]^2\right)\ge0,
\]
because the scalar-\(-4\) Yamabe representative minimizes the scalar \(L^2\) energy in a class with \(Y[g]<0\). Thus
\[
8\pi^2k-P(g)\le8\pi^2k-P(\hat g).
\]

From Proposition 48.1,
\[
\sup_{r,n}f(W,r,n)
=\varphi(-\mu_{\min}(W))-4|W|^2
=2\left(\frac23-|W|^2\right)-\Psi(W).
\]
Using the averaged Theorem-W inequality recorded in Step 45, with the \(\zeta\) and Walsh contributions that are \(\le0\) omitted and with \(0\le r\le2\),
\[
S_{\hat g}:=8\pi^2k-P(\hat g)
\le 2D_W-\int_M\Psi.
\]
Substitute
\[
D_W=\frac14S_{\hat g}+\Delta V
\]
from (Y0):
\[
S_{\hat g}
\le\frac12S_{\hat g}+2\Delta V-\int\Psi.
\]
Therefore
\[
\boxed{\;
S_{\hat g}\le4\Delta V-2\int_M\Psi.
\;}
\]
Lemma 48.2 then gives
\[
S_{\hat g}
\le4\Delta V-\frac{20}{9}
\int_M\operatorname{dist}(W^+_{\hat g},\mathcal K)^2.
\]
Since
\[
4\Delta V=\frac{Y[g]^2-32\pi^2A}{4},
\]
the displayed Theorem Y is exact.

This derivation requires precisely the all-sign field supply used by Theorem W, including the relevant chamber assumption when \(b^+=1\), and the maximum-principle amplitude cap \(r\le2\). No almost-Kähler representative or field-selection continuity is used.

---

## 4. Comparison with LeBrun’s Proposition 4

Let
\[
w=|W^+|,\qquad u=\sqrt6\,w-2.
\]
At \(s=-4\), LeBrun’s Proposition 4 becomes
\[
\int_M(4+\sqrt6\,w)^2\,d\mu
\ge72\pi^2(a^+)^2.
\]
The pointwise algebraic identity
\[
\frac12(4+\sqrt6\,w)^2
=9w^2+12-u^2
\]
holds after integration in the form
\[
\frac12\int(4+\sqrt6w)^2
=9I_W+12\hat V-\int u^2.
\]
A sign choice from
\[
a_\varepsilon=K_X+\sum_i\varepsilon_iE_i
\]
has \((a_\varepsilon^+)^2\ge A\), so
\[
9I_W+12\hat V-\int u^2\ge36\pi^2A.
\]
A direct rearrangement using (Y0) gives
\[
\boxed{\;
8\pi^2k-P(\hat g)
\le4\Delta V-\frac49\int_Mu^2.
\;}
\]
Thus (Y-LeB) has the correct sign and factor \(4/9\).

There is a useful stronger version. Sign averaging gives
\[
\mathbb E_\varepsilon (a_\varepsilon^+)^2
=|K_X^+|^2+\sum_i|E_i^+|^2
=A+|K_X^-|^2+\sum_i|E_i^+|^2.
\]
Define
\[
Q_{\rm per}:=|K_X^-|^2+\sum_i|E_i^+|^2.
\]
Choosing a maximizing sign yields
\[
(a^+)^2\ge A+Q_{\rm per},
\]
and hence
\[
\boxed{\;
8\pi^2k-P(\hat g)
\le4\Delta V-\frac49\int u^2-16\pi^2Q_{\rm per}.
\;}
\]
The Step-48 formula is the weaker consequence obtained by retaining only
\((a^+)^2\ge A\).

The stated period estimate is also correct:
\[
\boxed{\;
\Delta V\ge2\pi^2
\left(|K_X^-|^2+\sum_i|E_i^+|^2\right).
\;}
\]
Its direct source is LeBrun’s scalar estimate, Proposition 2:
\[
16\hat V=\int s^2\ge32\pi^2(a^+)^2
\ge32\pi^2(A+Q_{\rm per}).
\]
Subtracting \(2\pi^2A\) gives the formula. Thus this estimate comes from the scalar Seiberg–Witten inequality with the sign choice, rather than from Proposition 4 alone.

### Exact amount already present in LeBrun’s estimate

LeBrun’s estimate already supplies:

- the coefficient \(4\) in
  \[
  8\pi^2k-P\le4\Delta V;
  \]
- the base conclusion
  \[
  \Delta V\ge2\pi^2(1-c)k
  \]
  whenever \(P\le8\pi^2ck\);
- stronger control in the axial magnitude-deficit direction.

Theorem Y adds spectral information unavailable from \(|W^+|\) alone. At
\[
\operatorname{spec}(W)=
\left(-\frac23,\frac13-\sigma,\frac13+\sigma\right),
\]
one has
\[
\Psi=4\sigma^2,
\]
so Theorem Y charges \(8\sigma^2\) in its right-hand side, whereas
\[
u=3\sigma^2+O(\sigma^4),
\]
and LeBrun’s \(u^2\) term begins at order \(\sigma^4\).

For an axial deficit \(x=2/3-h\),
\[
\frac49u^2=4h^2,\qquad
2\Psi=\frac{10}{3}h^2+\frac8{27}h^3,
\]
so LeBrun is stronger throughout \(0<h\le2/3\). For an axial excess
\(x=2/3+t\),
\[
\frac49u^2=4t^2,\qquad 2\Psi=6t^2,
\]
so Theorem Y is stronger. The two estimates are complementary rather than one uniformly subsuming the other.

---

## 5. Corollaries Y1 and Y2

If
\[
P(g)\le8\pi^2ck,
\]
then
\[
8\pi^2(1-c)k\le8\pi^2k-P(g).
\]
Combining with Theorem Y gives
\[
4\Delta V\ge
8\pi^2(1-c)k+
\frac{20}{9}\int\operatorname{dist}(W^+,\mathcal K)^2.
\]
Since \(Y[g]^2=32\pi^2A+16\Delta V\),
\[
\boxed{\;
Y[g]^2\ge
32\pi^2\bigl(A+(1-c)k\bigr)
+\frac{80}{9}\int
\operatorname{dist}(W^+,\mathcal K)^2.
\;}
\]
In particular,
\[
\boxed{\;
\Delta V\ge2\pi^2(1-c)k.
\;}
\]
Corollary Y1 is correct.

For Corollary Y2, (Y0) gives the exact equivalence
\[
\boxed{\;
P(\hat g)\ge8\pi^2ck
\iff
D_W-\Delta V\le2\pi^2(1-c)k.
\;}
\]
It is also an equivalence for a universal statement over all metrics, because every Yamabe representative is itself among those metrics and every conformal representative satisfies \(P(g)\ge P(\hat g)\).

For one arbitrary representative \(g\), however,
\[
P(g)\ge8\pi^2ck
\]
does not by itself imply the displayed condition on \(D_W-\Delta V\); conformal scalar-energy excess can raise \(P(g)\) above \(P(\hat g)\). Thus the word “equivalent” is exact only with \(P(\hat g)\), with \(g\) already Yamabe-normalized, or at the universal all-metrics level.

The field consequence is exact:
\[
4(D_W-\Delta V)
\le4\Delta V-2\int\Psi,
\]
hence
\[
\boxed{\;
D_W-\Delta V
\le\Delta V-\frac12\int\Psi.
\;}
\]

---

## 6. Consistency objects

### Complex-hyperbolic Kähler–Einstein metric

For \(k=0\),
\[
P=0,\qquad \Delta V=0,\qquad W^+\in\mathcal K,\qquad \Psi=0,
\]
so all equalities are exact.

### Certified cell numbers

The quoted normalized values satisfy (Y0):
\[
0.07513-0.07080\approx0.00433,
\]
consistent with the saving \(0.00434\) after rounding.

They do not, by themselves, establish “large slack” in Theorem Y. If
\[
\bar J_\Psi:=\frac1{8\pi^2}\int\Psi,
\]
the numerical theorem requires
\[
0.00434\le0.07080-2\bar J_\Psi,
\]
or
\[
\bar J_\Psi\le0.03323.
\]
No value of \(\int\Psi\), or of the corresponding distance-square integral, is supplied. Moreover, the isolated cell is a relative local object rather than a closed manifold carrying the all-sign family. The \(D_W,\Delta V\) entries verify the relative version of (Y0), but an independent numerical test of Theorem Y requires the cell’s \(\Psi\)-integral together with its collar bookkeeping. The conclusion that the cell is far from equality is therefore not established by the three quoted numbers alone.

### Formal common mode

Let
\[
h=\frac{k}{A},\qquad x=\frac23-h,\qquad
\hat V=\frac{8\pi^2A}{(2-h)^2},
\]
and define
\[
\mathcal U=\frac{8\pi^2k}{(2-h)^2}.
\]
The Step-47 formula
\[
\frac{P}{8\pi^2k}=\frac{h(1+h)}{(2-h)^2}
\]
gives
\[
\frac{8\pi^2k-P}{\mathcal U}=4-5h.
\]
Also,
\[
\frac{4\Delta V}{\mathcal U}=4-h.
\]
Since
\[
\Psi=\frac53h^2+\frac4{27}h^3,
\]
one gets
\[
\frac{2\int\Psi}{\mathcal U}
=\frac{10}{3}h+\frac8{27}h^2.
\]
Thus Theorem Y has right-hand side
\[
4-\frac{13}{3}h-\frac8{27}h^2,
\]
and its slack is exactly
\[
\boxed{\;
\frac23h-\frac8{27}h^2.
\;}
\]
In absolute size this is \(O(k^2/A)\), so the statement about leading-order saturation is correct.

For comparison, \(u=-3h\) in this formal axial mode, and
\[
\frac{\frac49\int u^2}{\mathcal U}=4h.
\]
Consequently LeBrun’s right-hand side is exactly
\[
(4-h)-4h=4-5h,
\]
so the formal mode saturates the LeBrun algebra exactly. It remains a formal configuration rather than an admissible closed family.

### Rotated cells

Theorem Y applies directly to every smooth rotated metric through its smooth Yamabe representative and does not use the conformal almost-Kähler metric near its degenerating set. That qualitative statement is correct.

Two refinements are needed:

1. The central inequality for \(P(\hat g)\) is conformal-class data; the leftmost \(P(g)\) term is attached to the chosen representative and enters only through \(P(g)\ge P(\hat g)\).
2. The supplied files do not contain a first-variation computation proving that \(P\), \(\Delta V\), and the Weyl data agree with the diagonal cell to \(O(\vartheta^2)\) in the rotation parameter \(\vartheta\). Continuity supports persistence of a strict subthreshold inequality for sufficiently small rotation, but the stated \(O(\vartheta^2)\) agreement requires its own variation formula.

## Overall mathematical status

Proposition 48.1, the formula for \(\varphi\), Lemma 48.2, (Y0), Theorem Y, Corollary Y1, and the field inequality in Y2 are all mathematically correct with the stated normalizations. The main textual adjustments are:

- replace the scan-based end of Lemma 48.2 by the exact eigenvalue proof above;
- state Y2’s equivalence using \(P(\hat g)\), or as a universal all-metrics equivalence;
- attribute the period estimate directly to the scalar Seiberg–Witten inequality;
- record the stronger LeBrun term \(-16\pi^2Q_{\rm per}\) when period data are retained;
- treat the certified-cell and rotated-cell remarks as qualitative until their \(\Psi\)-integrals and rotation variations are supplied.
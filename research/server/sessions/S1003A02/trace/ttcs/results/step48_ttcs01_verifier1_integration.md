# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 48,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step48_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step48_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the new Step-48 results in Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md §§1-2 as exact mathematics. Specifically: (1) Proposition 48.1: the algebraic simplification f(W,r,n)=r^2M(n,n)-4|M|^2+p(r) = -r^2W(n,n)-4|W|^2+p(r) with M=W-(r^2/4)(I/3-nn^T), and the explicit sup over r in [0,2] giving phi(x). (2) Lemma 48.2: Psi>=0, Psi=0 exactly on the Kähler orbit, sharp constant 10/9 for Psi>=c dist^2. (3) Theorem Y: check the exact closed identity (Y0) 8π²k−P(ĝ)=4D_W−4ΔV at s≡−4 from C_+=A−k+P/8π² (with C_+=(1/2π²)∫|W+|²+(1/96π²)∫s²), the use of Theorem W/K's averaged pointwise bound (read the step45 note §3 for the saving density and its hypotheses, r∈[0,2]), and the elimination step. (4) The LeBrun comparison (Y-LeB) derived from LeBrun's Proposition 4 ∫(s−√6|W+|)²≥72π²(a+)² with the sign choice (a+)²≥A, and the claimed period lower bound ΔV≥2π²(|K_X^-|²+Σ|E_i^+|²). (5) The three consistency checks: certified cell numbers, formal common mode (P/8π²k=h(1+h)/(2−h)², V̂=8π²A/(2−h)², axial x=2/3−h; Step-47 note gives D_K formulas), rotated cells. Decide whether Corollary Y1 (ΔV≥2π²(1−c)k for P≤8π²ck) and Corollary Y2 (tariff ⇔ D_W−ΔV≤2π²(1−c)k; fields give D_W−ΔV≤ΔV−½∫Ψ) are correct and correctly scoped, and assess honestly how much of Theorem Y is already contained in LeBrun's estimate. Report any sign, normalization or factor errors with corrected statements.

## Integrated Scientific Memo

# Verification of Step 48, §§1–2

## Verdict

The core statements are correct:

- Proposition 48.1 and the explicit function \(\varphi\);
- Lemma 48.2, including the sharp constant \(10/9\);
- the closed identity (Y0);
- Theorem Y and its constants;
- (Y-LeB);
- Corollary Y1;
- the field inequality in Y2.

Several qualifications/corrections are needed:

1. Lemma 48.2 should be proved by exact eigenvalue algebra, not by the numerical scan.
2. Y2’s “tariff equivalence” is pointwise exact for \(P(\hat g)\), not for an arbitrary conformal representative \(P(g)\); it is also valid as an all-metrics universal equivalence.
3. The LeBrun comparison naturally retains a stronger negative period term
   \[
   -16\pi^2\Pi_g,\qquad
   \Pi_g=(a^+)^2-A.
   \]
4. The stated period lower bound is correct, but follows most directly from LeBrun’s scalar estimate (Proposition 2), not from Proposition 4 alone.
5. The formal common mode saturates (Y-LeB) **exactly**, while it saturates Theorem Y only to leading order, with \(O(k^2/A)\) slack.
6. The certified-cell numbers verify only (Y0) after rounding; without \(\int\Psi\), they do not establish “large slack” in Theorem Y.
7. The claim that rotated cells have the same data to \(O(\psi^2)\) is not established in the supplied material; only continuity and persistence of strict subthreshold cost are supported.
8. The assertion that opening periods “makes saving possible” is misleading once the retained LeBrun period term is included: at fixed \(\Delta V\), periods reduce the saving bound. Period stiffness alone nevertheless does not yield a tariff because no supplied result forces the period contribution to be order \(k\).

---

## 1. Proposition 48.1

Let
\[
P_n=\frac I3-nn^T,\qquad M=W-\frac{r^2}{4}P_n,
\]
where \(W\) is traceless symmetric and \(|n|=1\). Then
\[
P_n(n,n)=-\frac23,\qquad |P_n|^2=\frac23,\qquad
\langle W,P_n\rangle=-W(n,n).
\]
Therefore
\[
M(n,n)=W(n,n)+\frac{r^2}{6}
\]
and
\[
|M|^2
=|W|^2-\frac{r^2}{2}\langle W,P_n\rangle
 +\frac{r^4}{16}|P_n|^2
=|W|^2+\frac{r^2}{2}W(n,n)+\frac{r^4}{24}.
\]
Thus
\[
\begin{aligned}
r^2M(n,n)-4|M|^2
&=r^2W(n,n)+\frac{r^4}{6}
 -4|W|^2-2r^2W(n,n)-\frac{r^4}{6}\\
&=-r^2W(n,n)-4|W|^2.
\end{aligned}
\]
Hence
\[
\boxed{f(W,r,n)=-r^2W(n,n)-4|W|^2+p(r).}
\]

For fixed \(r\), the maximizing direction is a lowest-eigenvalue direction. Put
\[
x=-\mu_{\min}(W)\ge0.
\]
Since
\[
p(r)=-r^3+\frac73r^2-\frac43,
\]
the remaining function is
\[
q_x(r)=-r^3+\left(x+\frac73\right)r^2-\frac43,
\]
with
\[
q_x'(r)=r\left(2x+\frac{14}{3}-3r\right).
\]
Its nonzero critical point is
\[
r_*=\frac{6x+14}{9}.
\]
This lies in \([0,2]\) exactly when \(x\le2/3\). At that point,
\[
x+\frac73=\frac32r_*,
\qquad
q_x(r_*)=\frac12r_*^3-\frac43.
\]
For \(x\ge2/3\), \(q_x\) is increasing up to \(r=2\), and
\[
q_x(2)=4x.
\]
Therefore
\[
\boxed{
\varphi(x)=
\begin{cases}
\dfrac12\left(\dfrac{6x+14}{9}\right)^3-\dfrac43,
&0\le x\le\dfrac23,\\[6pt]
4x,&x\ge\dfrac23.
\end{cases}}
\]
At \(x=2/3\), both pieces have value \(8/3\) and derivative \(4\), so \(\varphi\in C^1\).

The symbolic script correctly returns zero residual. By contrast, `step48_lemmaP.json` is not valid corroboration of the constrained optimization because some reported maximizing amplitudes exceed \(2\).

---

## 2. Lemma 48.2

Write the ordered eigenvalues as
\[
\left(-x,\frac{x}{2}-\sigma,\frac{x}{2}+\sigma\right),
\qquad x\ge0.
\]
Then
\[
|W|^2=\frac32x^2+2\sigma^2.
\]
Hoffman–Wielandt gives the exact orbit distance
\[
d_{\mathcal K}(W)^2
=\frac32\left(x-\frac23\right)^2+2\sigma^2.
\]

Recall
\[
\Psi(W)=\frac43+2|W|^2-\varphi(x).
\]

### Deficit side: \(0\le x\le2/3\)

Put \(h=2/3-x\). Exact substitution gives
\[
\boxed{\Psi(W)=\frac53h^2+\frac4{27}h^3+4\sigma^2.}
\]

### Excess side: \(x\ge2/3\)

Put \(t=x-2/3\). Since \(\varphi(x)=4x\),
\[
\boxed{\Psi(W)=3t^2+4\sigma^2
      =2\,d_{\mathcal K}(W)^2.}
\]

These formulas immediately prove
\[
\Psi\ge0,
\]
with equality exactly when \(x=2/3\) and \(\sigma=0\), namely precisely on \(\mathcal K\).

They also prove globally
\[
\Psi-\frac{10}{9}d_{\mathcal K}^2
=
\begin{cases}
\dfrac4{27}h^3+\dfrac{16}{9}\sigma^2,
&x\le2/3,\\[6pt]
\dfrac43t^2+\dfrac{16}{9}\sigma^2,
&x\ge2/3,
\end{cases}
\]
and hence
\[
\boxed{\Psi(W)\ge\frac{10}{9}\operatorname{dist}(W,\mathcal K)^2.}
\]
The constant is sharp because along \(\sigma=0\), \(x=2/3-h\),
\[
\frac{\Psi}{d_{\mathcal K}^2}
=\frac{10}{9}+\frac8{81}h
\longrightarrow\frac{10}{9}.
\]
It is an infimum approached from the deficit side, not attained off \(\mathcal K\).

The scan value slightly below \(10/9\) in `step48_theoremY.json` is floating-point cancellation near the orbit and should not appear in the proof.

---

## 3. Identity (Y0) and Theorem Y

Let
\[
I_W=\int_M|W^+_{\hat g}|^2\,d\mu_{\hat g}.
\]
At \(s_{\hat g}\equiv-4\),
\[
C_+(\hat g)
=\frac{I_W}{2\pi^2}+\frac{\hat V}{6\pi^2}.
\]
Using
\[
C_+=A-k+\frac{P(\hat g)}{8\pi^2}
\]
gives
\[
4I_W+\frac43\hat V
=8\pi^2(A-k)+P(\hat g).
\]
Thus
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
\boxed{8\pi^2k-P(\hat g)=4D_W-4\Delta V.}
\tag{Y0}
\]

For an arbitrary \(g\) in the same negative Yamabe class,
\[
P(g)-P(\hat g)
=\frac1{12}\left(\int s_g^2\,d\mu_g-Y[g]^2\right)\ge0,
\]
so
\[
8\pi^2k-P(g)\le8\pi^2k-P(\hat g).
\]

Proposition 48.1 gives
\[
\sup_{0\le r\le2,\ |n|=1}f(W,r,n)
=\varphi(-\mu_{\min}W)-4|W|^2
=2\left(\frac23-|W|^2\right)-\Psi(W).
\]
Under precisely Theorem W’s all-sign hypotheses—including the relevant chamber conditions—and using the maximum-principle cap \(r\le2\), averaging and discarding the nonpositive \(\zeta\)/Walsh terms yields
\[
S:=8\pi^2k-P(\hat g)
\le2D_W-\int_M\Psi.
\]
From (Y0),
\[
D_W=\frac14S+\Delta V.
\]
Consequently
\[
S\le\frac12S+2\Delta V-\int\Psi,
\]
so
\[
\boxed{
8\pi^2k-P(\hat g)
\le4\Delta V-2\int_M\Psi.}
\]
Applying Lemma 48.2 gives
\[
\boxed{
8\pi^2k-P(g)
\le8\pi^2k-P(\hat g)
\le4\Delta V-\frac{20}{9}
\int_M\operatorname{dist}(W^+_{\hat g},\mathcal K)^2.}
\]
Finally,
\[
4\Delta V=\frac{Y[g]^2-32\pi^2A}{4}.
\]
Thus Theorem Y is correct, including every displayed coefficient.

---

## 4. LeBrun comparison and period contribution

Let
\[
w=|W^+|,\qquad u=\sqrt6\,w-2.
\]
At \(s=-4\), Proposition 4 reads
\[
\int(4+\sqrt6w)^2\,d\mu
\ge72\pi^2(a^+)^2.
\]
The identity
\[
\frac12(4+\sqrt6w)^2=9w^2+12-u^2
\]
gives, after integration,
\[
9I_W+12\hat V-\int u^2
\ge36\pi^2(a^+)^2.
\]

Write
\[
\Pi_g=(a^+)^2-A\ge0.
\]
Rearrangement using (Y0) yields the stronger form
\[
\boxed{
8\pi^2k-P(\hat g)
\le4\Delta V-\frac49\int u^2-16\pi^2\Pi_g.}
\tag{LeB\(_{\rm full}\)}
\]
Dropping \(\Pi_g\) gives exactly
\[
\boxed{
8\pi^2k-P(\hat g)
\le4\Delta V-\frac49\int u^2,}
\tag{Y-LeB}
\]
so the sign and factor \(4/9\) are correct.

### Period lower bound

For
\[
a_\varepsilon=K_X+\sum_i\varepsilon_iE_i,
\]
sign averaging gives
\[
\mathbb E_\varepsilon(a_\varepsilon^+)^2
=|K_X^+|^2+\sum_i|E_i^+|^2
=A+|K_X^-|^2+\sum_i|E_i^+|^2.
\]
Hence some sign satisfies
\[
(a^+)^2\ge A+Q_{\rm per},
\qquad
Q_{\rm per}:=|K_X^-|^2+\sum_i|E_i^+|^2.
\]
LeBrun’s scalar estimate,
\[
16\hat V=\int s^2\ge32\pi^2(a^+)^2,
\]
then gives
\[
\boxed{
\Delta V\ge2\pi^2Q_{\rm per}.}
\]
Thus the claimed lower bound is correct, but its clean direct source is Proposition 2.

Retaining the same sign in Proposition 4 also gives
\[
8\pi^2k-P(\hat g)
\le4\Delta V-\frac49\int u^2-16\pi^2Q_{\rm per}.
\]
Therefore period opening has two effects: it forces Yamabe excess, but it also enters the saving estimate with a negative coefficient. It is inaccurate to infer from the lower bound on \(\Delta V\) alone that periods make saving possible. At fixed \(\Delta V\), periods reduce the allowed saving. No tariff follows, however, unless one can force \(Q_{\rm per}\gtrsim k\).

### What is genuinely beyond LeBrun?

LeBrun already contains:

- the leading coefficient
  \[
  8\pi^2k-P\le4\Delta V;
  \]
- Y1’s leading lower bound on \(\Delta V\);
- the period correction above;
- stronger axial control on the deficit side.

Theorem Y adds information depending on the full spectrum rather than merely \(|W^+|\). For
\[
\operatorname{spec}W
=\left(-\frac23,\frac13-\sigma,\frac13+\sigma\right),
\]
\[
\Psi=4\sigma^2,
\]
so Theorem Y subtracts \(8\sigma^2\) pointwise. Meanwhile,
\[
u=\sqrt{4+6\sigma^2}-2
=\frac32\sigma^2+O(\sigma^4),
\]
so LeBrun’s \(u^2\) penalty is quartic in \(\sigma\).  
(The coefficient \(3\sigma^2\) stated in one branch is a factor-two error.)

For an axial deficit \(x=2/3-h\),
\[
\frac49u^2=4h^2,\qquad
2\Psi=\frac{10}{3}h^2+\frac8{27}h^3,
\]
and LeBrun is stronger for \(0<h\le2/3\).

For axial excess \(x=2/3+t\),
\[
\frac49u^2=4t^2,\qquad
2\Psi=6t^2,
\]
and Theorem Y is stronger.

Thus Theorem Y is not a replacement for LeBrun: its genuinely new content is principally upper-eigenvalue splitting and the stronger excess-side penalty.

---

## 5. Corollaries

### Y1

If
\[
P(g)\le8\pi^2ck,
\]
then
\[
8\pi^2(1-c)k\le8\pi^2k-P(g).
\]
Theorem Y implies
\[
4\Delta V\ge
8\pi^2(1-c)k
+\frac{20}{9}\int\operatorname{dist}(W^+,\mathcal K)^2.
\]
Therefore
\[
\boxed{
\Delta V\ge
2\pi^2(1-c)k
+\frac59\int\operatorname{dist}(W^+,\mathcal K)^2,}
\]
and
\[
\boxed{
Y[g]^2\ge
32\pi^2\bigl(A+(1-c)k\bigr)
+\frac{80}{9}\int\operatorname{dist}(W^+,\mathcal K)^2.}
\]
In particular,
\[
\Delta V\ge2\pi^2(1-c)k.
\]
Y1 is correct.

Because \(Y[g]<0\), the statement
\[
|Y[g]|\ge4\pi\sqrt{2(A+(1-c)k)}
\]
is also correct. Saying that the conformal-class Yamabe constant lies “below” the manifold invariant should be read in the numerical sense
\[
Y[g]\le-4\pi\sqrt{2(A+(1-c)k)}
<\mathcal Y(M)=-4\pi\sqrt{2A}.
\]

### Y2

From (Y0),
\[
P(\hat g)
=8\pi^2k-4(D_W-\Delta V).
\]
Hence
\[
\boxed{
P(\hat g)\ge8\pi^2ck
\iff
D_W-\Delta V\le2\pi^2(1-c)k.}
\]
This is exact if \(g=\hat g\), or as a universal all-metrics tariff statement. It is not pointwise equivalent to \(P(g)\ge8\pi^2ck\) for an arbitrary non-Yamabe representative, because \(P(g)\) can exceed \(P(\hat g)\) by conformal scalar-energy excess.

Theorem Y gives
\[
4(D_W-\Delta V)
\le4\Delta V-2\int\Psi,
\]
hence
\[
\boxed{
D_W-\Delta V
\le\Delta V-\frac12\int\Psi.}
\]
This field consequence is correct.

---

## 6. Consistency checks

### Kähler–Einstein ball quotient

For \(k=0\),
\[
P=0,\qquad \Delta V=0,\qquad W^+\in\mathcal K,\qquad \Psi=0.
\]
All inequalities are equalities.

### Certified cell

The quoted normalized data satisfy
\[
4D_W-4\Delta V
\approx0.07513-0.07080
=0.00433,
\]
consistent with the quoted saving \(0.00434\) after rounding. This checks the relative version of (Y0), assuming both quantities were independently computed in scalar-\(-4\) normalization.

It does **not** establish large slack in Theorem Y. Writing quantities in the quoted \(8\pi^2\)-normalized units, one would need
\[
\frac1{8\pi^2}\int\Psi\le
\frac{0.07080-0.00434}{2}\approx0.03323.
\]
No \(\Psi\)-integral is supplied. Moreover, applying the closed theorem to an isolated cell requires explicit collar/localization bookkeeping.

### Formal common mode

Let
\[
h=\frac{k}{A},\qquad
x=\frac23-h,\qquad
\hat V=\frac{8\pi^2A}{(2-h)^2},
\]
and use units
\[
\mathcal U=\frac{8\pi^2k}{(2-h)^2}.
\]
The Step-47 formula gives
\[
\frac{8\pi^2k-P}{\mathcal U}=4-5h,
\qquad
\frac{4\Delta V}{\mathcal U}=4-h.
\]
Because
\[
\Psi=\frac53h^2+\frac4{27}h^3,
\]
\[
\frac{2\int\Psi}{\mathcal U}
=\frac{10}{3}h+\frac8{27}h^2.
\]
Thus Theorem Y’s right side is
\[
4-\frac{13}{3}h-\frac8{27}h^2,
\]
and the exact slack is
\[
\boxed{\frac23h-\frac8{27}h^2.}
\]
In absolute terms this is \(O(k^2/A)\), so leading-order saturation is correct.

Here \(u=-3h\), and
\[
\frac{(4/9)\int u^2}{\mathcal U}=4h.
\]
Therefore the right side of (Y-LeB) is
\[
(4-h)-4h=4-5h,
\]
exactly the left side. The formal common mode saturates LeBrun’s estimate exactly, not merely asymptotically. Equality also forces \(\Pi_g=0\), corresponding to null exceptional periods—the forbidden feature identified by Lemma T.

### Rotated cells

Theorem Y is indeed applied to the smooth Yamabe representative and is unaffected by singularities of a separate conformal almost-Kähler representative. However, the supplied files establish only continuity of the rotated construction and persistence of strict subthreshold cost for sufficiently small rotation. They do not establish
\[
P,\ \Delta V,\ W^+
\quad\text{agree with the diagonal cell to }O(\psi^2).
\]
That claim requires first-variation calculations. Quantitative comparison should also retain the nonzero period term in the LeBrun inequality.

---

## Corrected concise formulation

The reliable combined statement is:

\[
\boxed{
8\pi^2k-P(g)
\le8\pi^2k-P(\hat g)
\le4\Delta V-2\int\Psi
\le4\Delta V-\frac{20}{9}\int d_{\mathcal K}^2,
}
\]
under Theorem W’s all-sign/chamber hypotheses, with
\[
\Psi=
\begin{cases}
\frac53(2/3-x)^2+\frac4{27}(2/3-x)^3+4\sigma^2,
&x\le2/3,\\[4pt]
3(x-2/3)^2+4\sigma^2,
&x\ge2/3.
\end{cases}
\]

Independently, for an appropriate monopole sign,
\[
\boxed{
8\pi^2k-P(\hat g)
\le4\Delta V-\frac49\int(\sqrt6|W^+|-2)^2
-16\pi^2\Pi_g,
}
\]
where
\[
\Pi_g\ge |K_X^-|^2+\sum_i|E_i^+|^2,
\qquad
\Delta V\ge2\pi^2\Pi_g.
\]

The leading Yamabe-excess mechanism and Y1 are already contained in LeBrun’s estimates. The new mathematical contribution of Theorem Y is the coercive control of spectral splitting and stronger excess-side curvature departure; it is complementary to, not uniformly stronger than, LeBrun’s estimate.
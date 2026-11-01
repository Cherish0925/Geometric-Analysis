# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 62,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step62_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step62_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Step 62 (workspace/notes/step62_weyl_channel_reduction.md) line by line. Setting: X minimal general type, A=c1^2(X), b+>=2, SW(X)!=0, M=X#kCP2bar, sign family a_eps=K+sum eps_i E_i are monopole classes, P=int|Ric°|^2, p=P/8pi^2. Check: (1) Identity 62.1 p(g~)=(k-kappa)+(upsilon-kappa)/3 with kappa=A/2-(3/8pi^2)int|W+|^2, upsilon=Y^2/(32pi^2)-A, via Chern-Weil 2chi+3tau=(1/4pi^2)int(2|W+|^2+s^2/24-|Ric°|^2/2), and P(g)>=P(g~) for the s=-4 Yamabe representative; check against the certified cell numbers in step48 note §2 (omega=4*0.018784, upsilon=4*0.053096 per class gives p≈0.99566). (2) The envelope 62.2 2sqrt(A+upsilon)+sqrt(A-2kappa)>=3sqrt(A+Pi) from LeBrun Prop 4 (Knowledge LeBrun object lines 145-149) and Cauchy-Schwarz; whether max_eps (a_eps^+)^2>=A is correct and Pi>=|K^-|^2+sum|E_i^+|^2. (3) Theorem 62.A L_A(k,kappa)=(k-kappa)+(1/2)(A-kappa-sqrt(A^2-2A kappa)) for kappa<=4A/9, including the elimination algebra, monotonicity, and the k-A/3 regime. (4) Kähler metrics have kappa<=0 (Hodge index on the Kähler cone of blow-ups), recovering the Kähler tariff. (5) Formal common mode expansions (kappa=k-k^3/4A^2, upsilon=k+3k^2/4A+k^3/2A^2, p=k^2/4A+k^3/2A^2) and that it lies on the equality locus to O(k^3/A^2). (6) Corollary 62.C equivalences and the resulting k^2/((4+4beta)A) bound and tariff k/(gamma+1). (7) The ASD reformulation for ball quotients (inf int|W-|^2 >= 28pi^2 k/3) and the tariff c=1-(9/2)(1-lambda). (8) The Gursky analogy (b+>0, Y>0 => int|W+|^2>=(4pi^2/3)(2chi+3tau)) and its per-point reading, and whether Conjecture 62.G is contradicted by anything standard (e.g. Taubes ASD metrics, known ASD metrics with b+>0, LeBrun estimates). (9) The claim that near a negative KE metric on X, KE is a local maximum of kappa among conformal classes (because negative KE is a local minimizer of int|W|^2 via the TT second variation of the Weyl functional), so the coupled inequality kappa<=beta p holds locally on X; state what formula for the second variation of int|W|^2 at Einstein metrics is needed. Report errors with corrected statements and say precisely what is new versus a direct rewriting of LeBrun's estimates.

## Integrated Scientific Memo

# Verification memo: Step 62

The coordinate reduction is sound, but several ranges and geometric conclusions require correction. In particular, **62.1 and 62.2 are correct; the fixed-\(\kappa\) lower bound is correct for \(0\le\kappa\le A/2\); 62.C’s equivalences are correct; 62.D is not a consequence of the stated estimates; and local maximality of \(\kappa\) at a negative KE metric requires additional spectral and nonlinear information.**

Below, \(p\) without an argument means \(P(\widetilde g)/(8\pi^2)\). Bounds for this quantity imply the same bounds for \(P(g)/(8\pi^2)\). Statements involving \(\alpha\) assume that \(\alpha=\inf_g P(g)\); another normalization of \(\mathscr D\) must be adjusted accordingly.

## 1. Identity 62.1, conformal minimization, and the cell ledger

The supplied Chern–Weil formula gives
\[
P(g)=4\int|W^+|^2+\frac1{12}\int s^2-8\pi^2(A-k).
\]
At the negative Yamabe representative,
\[
\int s^2=Y[g]^2=32\pi^2(A+\upsilon),\qquad
\int|W^+|^2=\frac{4\pi^2}{3}(A-2\kappa).
\]
Consequently,
\[
\boxed{p=k-\frac43\kappa+\frac13\upsilon
=(k-\kappa)+\frac13(\upsilon-\kappa).}
\]

**Correct the intermediate coefficient in the proof:** it is
\[
\frac23(A-2\kappa),
\]
not \(\frac16(A-2\kappa)\).

The sign-family scalar estimate excludes a scalar-flat Yamabe representative, so every class here has \(Y[g]<0\). Conformal invariance of the Weyl integral and the negative-class scalar minimization stated in the supplied paper, §4, yield
\[
P(g)-P(\widetilde g)
=\frac1{12}\left(\int s_g^2-Y[g]^2\right)\ge0.
\]
Thus the boxed identity and conformal minimization assertion are correct.

For the quoted cell data,
\[
\omega=0.075136,\quad \kappa=\frac34\omega=0.056352,\quad
\upsilon=0.212384,
\]
and
\[
p=1-0.075136+\frac{0.212384}{3}
=0.995658666\ldots.
\]
This is consistent at the few-\(10^{-6}\) level with the ledgers, but **the claimed interval agreement is not independently certified by the supplied files**. Step 48 quotes \(p=0.9956609\); Step 62 quotes \(0.9956627\). Moreover, if the two six-decimal inputs were ordinary nearest-rounded numbers, their combined uncertainty in \(p\) would be at most \(2.67\times10^{-6}\), smaller than the \(4.03\times10^{-6}\) discrepancy from the latter value. The numerical consistency check is useful; “the difference is rounding” needs the underlying ledger or interval data.

The interpretation following 62.1 needs a qualification: \(\upsilon-\kappa\ge0\), but **\(k-\kappa\) is not known to be nonnegative**. The two terms need not separately become small when \(p/k\to0\).

## 2. Sign-family periods and the LeBrun envelope

Use \(|a^-|^2=-(a^-)^2\). Averaging signs gives
\[
\begin{aligned}
\mathbb E_\varepsilon(a_\varepsilon^+)^2
&=A-k+|K^-|^2+\sum_i|E_i^-|^2\\
&=A+|K^-|^2+\sum_i|E_i^+|^2,
\end{aligned}
\]
because \(|E_i^-|^2=1+|E_i^+|^2\). Hence
\[
\boxed{\Pi:=\max_\varepsilon(a_\varepsilon^+)^2-A
\ge |K^-|^2+\sum_i|E_i^+|^2\ge0.}
\]
Both requested sign-family assertions are correct.

Proposition 2 gives \(\upsilon\ge\Pi\). Proposition 4 in the supplied Ishida–LeBrun object gives
\[
\|s-\sqrt6|W^+|\|_2^2\ge72\pi^2(A+\Pi).
\]
The \(L^2\) triangle inequality gives
\[
\|s-\sqrt6|W^+|\|_2
\le\|s\|_2+\sqrt6\|W^+\|_2.
\]
No assumption that “\(s<0\) somewhere” is needed for this upper bound. At \(\widetilde g\), division by \(\sqrt{8\pi^2}\) yields exactly
\[
\boxed{2\sqrt{A+\upsilon}+\sqrt{A-2\kappa}
\ge3\sqrt{A+\Pi}.}\tag{62.2}
\]

Equality requires equality in Proposition 4 and in the triangle/Cauchy–Schwarz step. Since \(s=-4\), the latter requires \(|W^+|\) constant. Setting \(\Pi=0\) adds another equality requirement. The supplied paper describes Proposition 4’s equality metrics as a very special almost-Kähler class, but does not provide its full characterization.

A useful additional consequence, valid throughout the domain, follows from concavity:
\[
2\sqrt{A+\upsilon}+\sqrt{A-2\kappa}
\le3\sqrt{A+\frac23(\upsilon-\kappa)}.
\]
Therefore
\[
\boxed{\upsilon-\kappa\ge\frac32\Pi\ge0,\qquad p\ge k-\kappa.}\tag{*}
\]
This is the clean universal inequality used by the tariff arguments.

## 3. Theorem 62.A: correct elimination and domain

Necessarily \(\kappa\le A/2\). For \(0\le\kappa\le A/2\), put
\[
y=\sqrt{1-\frac{2\kappa}{A}}\in[0,1].
\]
Dropping \(\Pi\) and solving 62.2 gives
\[
\upsilon\ge\upsilon_L(\kappa)
=\frac{3A}{2}(1-y)-\frac{\kappa}{2}.
\]
Its expansion is
\[
\upsilon_L
=\kappa+\frac{3\kappa^2}{4A}
+\frac{3\kappa^3}{4A^2}
+O(\kappa^4/A^3).
\]
Thus
\[
\boxed{
p\ge L_A(k,\kappa)
=k-\frac32\kappa+\frac A2(1-y)
=(k-\kappa)+\frac12\left(A-\kappa-\sqrt{A^2-2A\kappa}\right).
}
\]
The elimination algebra and displayed expansion of \(L_A\) are correct.

The precise monotonicity is
\[
\partial_\kappa L_A=-\frac32+\frac1{2y}.
\]
It decreases up to \(4A/9\), increases thereafter, and
\[
L_A(k,4A/9)=k-A/3.
\]
Accordingly:

* The fixed-\(\kappa\) estimate holds on **all of \(0\le\kappa\le A/2\)**.
* For fixed \(\kappa>4A/9\), it is stronger than \(k-A/3\).
* \(k-A/3\) is the minimum after optimizing over \(\kappa\), not the best fixed-\(\kappa\) estimate.
* “Decreasing for \(\kappa<2A\)” in 62.C is false.

### Negative \(\kappa\)

The branches disagree here; unrestricted squaring is the error. For all \(\kappa\le A/2\), the directly valid bound is
\[
\upsilon\ge
\max\left\{0,\,
A\left[\frac{(3-\sqrt{1-2\kappa/A})_+^2}{4}-1\right]\right\}.
\]
For \(\kappa\le0\), this reduces to \(\upsilon\ge0\), giving
\[
\boxed{p\ge k-\frac43\kappa\ge k.}
\]
One cannot extend the displayed \(L_A\) bound to arbitrarily negative \(\kappa\) by the original argument. Indeed, with \(y=\sqrt{1-2\kappa/A}\),
\[
L_A-(k-\tfrac43\kappa)=\frac A{12}(y-1)(y-5),
\]
which is positive when \(\kappa<-12A\). The clean corrected theorem is therefore
\[
p\ge
\begin{cases}
k-\frac43\kappa,&\kappa\le0,\\[2mm]
L_A(k,\kappa),&0\le\kappa\le A/2.
\end{cases}
\]
The claimed “pure second-order overpayment”
\(\upsilon-\kappa\ge3\kappa^2/(4A)\) should likewise be restricted to \(0\le\kappa\le A/2\).

### Corollary 62.B

The substitution \(\kappa_*\le k\Rightarrow p\ge L_A(k,k)\) requires
\[
0\le k\le4A/9.
\]
In that range,
\[
P\ge4\pi^2\left(A-k-\sqrt{A^2-2Ak}\right)
=\frac{2\pi^2k^2}{A}\left(1+\frac{k}{A}+O((k/A)^2)\right).
\]
For \(k>4A/9\), the cap \(\kappa_*\le k\) alone gives the optimized bound \(p\ge k-A/3\) by this argument. All bounds may of course be combined with \(p\ge0\).

The tariff implication
\[
\kappa_*\le(1-c)k\Longrightarrow p\ge ck
\]
is valid without this range restriction, by \((*)\).

## 4. Kähler metrics and recovery

For a Kähler metric in the complex orientation,
\[
|W^+|^2=s^2/24.
\]
The sign-family scalar estimate immediately gives
\[
\int|W^+|^2=\frac1{24}\int s^2
\ge\frac{4\pi^2}{3}A,
\]
so
\[
\boxed{\kappa\le0,\qquad P\ge8\pi^2k.}
\]
This proof avoids the unsupported blanket classification assertion that every compatible Kähler complex structure is the specified blow-up.

For the given complex blow-up, the Hodge-index argument is valid: writing
\[
[\omega]=\pi^*\beta-\sum e_iE_i,
\]
one has
\[
\frac{(K_M\cdot\omega)^2}{\omega^2}
=\frac{(K_X\cdot\beta+\sum e_i)^2}{\beta^2-\sum e_i^2}
\ge\frac{(K_X\cdot\beta)^2}{\beta^2}\ge A.
\]
It is enough that \(\beta\) lies in the appropriate positive cone; the proof need not assert that the pushed-forward class is Kähler.

For a negative cscK metric, which is its own Yamabe representative,
\[
\kappa=-\upsilon/2,\qquad \boxed{p=k+\upsilon}.
\]
This makes recovery transparent whenever a suitable cscK gluing construction exists. Arezzo–Pacard recovery requires its host and gluing hypotheses; it is not supplied merely by the lower-bound calculation. A minimal general-type surface need not itself admit a smooth negative KE metric.

## 5. Formal common mode: exact algebraic equality

Let \(h=k/A\). The quoted formal curvature and volume give
\[
\boxed{
\frac{\kappa}{A}=\frac{4h(1-h)}{(2-h)^2},\quad
\frac{\upsilon}{A}=\frac{h(4-h)}{(2-h)^2},\quad
\frac pA=\frac{h^2(1+h)}{(2-h)^2}.
}
\]
Thus all three requested expansions are correct:
\[
\begin{aligned}
\kappa&=k-\frac{k^3}{4A^2}+O(k^4/A^3),\\
\upsilon&=k+\frac{3k^2}{4A}+\frac{k^3}{2A^2}+O(k^4/A^3),\\
p&=\frac{k^2}{4A}+\frac{k^3}{2A^2}+O(k^4/A^3).
\end{aligned}
\]

For \(0\le h\le2/3\),
\[
2\sqrt{1+\upsilon/A}+\sqrt{1-2\kappa/A}
=\frac{4+(2-3h)}{2-h}=3.
\]
Hence the formal mode lies **exactly on the algebraic \(\Pi=0\) envelope**, and \(p=L_A(k,\kappa)\) exactly in this range. The claim of exact equality “for all \(h\)” in one branch is wrong: the square root contains \(|2-3h|\).

This does **not** construct a closed metric saturating Proposition 4.

The formal mode does not exactly saturate the affine susceptibility:
\[
\boxed{k+3p-\upsilon=4(k-\kappa)
=\frac{4Ah^3}{(2-h)^2}>0\quad(h>0).}
\]
It saturates only to quadratic order. The corresponding anti-self-dual energy tariff \(28\pi^2/3\) per class is also a leading-order value, with a positive cubic correction.

## 6. Corollary 62.C and the necessary-structure claim

From \(4\kappa=3k+\upsilon-3p\),
\[
\kappa\le k+\beta p
\iff
\upsilon\le k+(3+4\beta)p.
\]
Moreover,
\[
\int|W^+|^2+\frac{\beta}{3}P(\widetilde g)
=\frac{4\pi^2}{3}(A-2\kappa+2\beta p),
\]
so all three formulations in 62.C are exactly equivalent.

For \(x=k+\beta p\le4A/9\), monotonicity and rationalization give
\[
p\ge L_A(k,x)
\ge-\beta p+\frac{x^2}{4A},
\]
and therefore
\[
p\ge\frac{k^2}{4(1+\beta)A}.
\]
The restriction on \(x\) cannot simply be omitted. Nevertheless, the claimed small-\(k/A\) conclusion is valid: large \(p\) already exceeds the desired scale. More concretely, the **exact** bound
\[
\boxed{p\ge\frac{k^2}{4(1+\beta)A}}
\]
holds under the uniform coupled hypothesis for \(k/A\le1/3\). To see this, suppose the bound fails. Then
\[
x<k+\frac{k^2}{4A}\le\frac{13A}{36}<\frac{4A}{9},
\]
so the preceding argument applies and contradicts the supposition. Negative \(\kappa\) is harmless because then \(p\ge k\).

For the linear susceptibility \(\upsilon\le\gamma p\), \((*)\) and 62.1 give \(p\ge k-\upsilon\), hence
\[
\boxed{p\ge\frac{k}{\gamma+1}}\qquad(\gamma\ge0).
\]
This tariff is exact.

### Corollary 62.D must be replaced

The supplied inequalities alone give
\[
\kappa\ge k-p,
\]
not \(\kappa/k\to1\). For example, the algebraic values
\[
\kappa=2k,\quad \upsilon=5k,\quad p=0,\quad \Pi=k
\]
satisfy 62.1, \(\upsilon\ge\Pi\), and 62.2 for sufficiently small \(k/A\). This is not a proposed metric; it disproves the claimed logical implication from those inequalities.

With the **additional** coupled cap \(\kappa\le k+\beta p\), however,
\[
\boxed{
k-p\le\kappa\le k+\beta p,\quad
0\le\upsilon-\kappa\le3(1+\beta)p,\quad
0\le\Pi\le2(1+\beta)p.
}
\]
Then \(p/k\to0\) does imply the three numerical conclusions in 62.D. Under a fixed \(\beta\), the quadratic bound also forces \(k/A\to0\) in such a family.

Neither small numerical slack nor small periods alone proves convergence to an almost-Kähler equality metric. That further conclusion requires geometric compactness and quantitative rigidity. The cited Step-47 period obstruction is absent from this input and cannot be checked here.

The concluding assertion that the Yamabe channel is “slaved” to \(\kappa\) is too strong: LeBrun supplies a **lower envelope**, not an upper relation. Excess above that envelope remains independent.

## 7. Anti-self-dual reformulation

The signature formula gives
\[
\int|W^+|^2-\int|W^-|^2=12\pi^2(\tau_X-k).
\]
Thus the Weyl-capacity hypothesis in 62.B is exactly equivalent to
\[
\boxed{
\inf_g\int|W^-|^2
\ge\frac{4\pi^2}{3}(A-9\tau_X)+\frac{28\pi^2}{3}k.
}
\]
For a ball quotient, \(A=9\tau_X\), giving the requested \(28\pi^2k/3\).

If instead
\[
\inf_g\int|W^-|^2\ge12\pi^2\lambda k,
\]
then
\[
\kappa\le\frac92(1-\lambda)k,
\]
and \((*)\) gives
\[
\boxed{p\ge ck,\qquad c=1-\frac92(1-\lambda).}
\]
The threshold is precisely \(\lambda>7/9\), with no unspecified extra term.

For the formal mode, the exact energy is
\[
\int|W^-|^2
=\frac{28\pi^2}{3}k+\frac{8\pi^2}{3}(k-\kappa),
\]
not exactly \(28\pi^2k/3\).

The quoted cell’s relative energy is consistent with
\[
12\pi^2-\delta W=(12-0.150272)\pi^2.
\]
As Step 48 itself stresses, an isolated cell is a consistency test, not an established closed sign-family realization.

## 8. Gursky analogy and Conjecture 62.G

The stated standard Gursky inequality has the correct normalization:
\[
b^+>0,\quad Y[g]>0
\Longrightarrow
\int|W^+|^2\ge\frac{4\pi^2}{3}(2\chi+3\tau).
\]
Here \(Y[g]\) is the conformal class’s Yamabe constant. A blow-up lowers its topological right-hand side by \(4\pi^2/3\). This is a decrease in the **lower-bound benchmark**, not a bound on the actual change between arbitrary metrics.

The scalar-flat Kähler examples on rational blow-ups have \(Y[g]=0\), outside this hypothesis. They therefore do not establish near-sharpness within the positive-Yamabe regime. The count \(12\pi^2/(4\pi^2/3)=9\) is a suggestive endpoint comparison only.

Conjecture 62.G is equivalent to \(\kappa_*\le k/2\). By \((*)\), it would imply the exact tariff \(P\ge4\pi^2k\). In the small-\(k/A\) range, the stronger expansion is
\[
p\ge L_A(k,k/2)
=\frac k2+\frac{k^2}{16A}+O(k^3/A^2).
\]

**No contradiction is exhibited by the supplied material or the standard examples identified in the task.**

* Taubes’s sufficiently-many-blow-ups ASD theorem does not provide here a numerical threshold below \(A\). For \(k\ge A\), 62.G’s right-hand side is nonpositive.
* Known ASD metrics with \(b^+>0\) outside these general-type blow-ups do not supply the required counterexample.
* At \(W^+=0\), Proposition 4 permits the geometry to pay through scalar curvature:
  \[
  Y[g]^2\ge72\pi^2(A+\Pi),\qquad
  p\ge k-\frac A4+\frac34\Pi.
  \]
  It does not establish the proposed ASD threshold.

An ASD metric on one of these \(X\#k\overline{\mathbb{CP}}^{\,2}\) with \(k<A\) would contradict 62.G; with \(k<A/2\), it would contradict 62.W. No such example is supplied. Conversely, 62.G would exclude approximate realization of the small-\(h\) formal common mode, whose \(\kappa\sim k\).

The statement that neither conjecture can follow from SW “alone” is not proved. What is proved is narrower: **Propositions 2 and 4, reduced to these variables, do not imply either cap.** Large-\(k\) ASD existence rules out a positive \(k\)-independent pure-\(W^+\) lower bound, not a \(k\)-dependent conjecture that becomes vacuous.

## 9. Local Weyl behavior at a negative KE metric

The exact Step-62 file proposes a local quadratic comparison; it does not prove the stronger local-maximum claim. Einstein/Bach-flat criticality alone cannot justify that claim.

Let \(\operatorname{Ric}(g_E)=\lambda g_E\), \(\lambda<0\), and use
\[
\Delta_Lh=\nabla^*\nabla h+\operatorname{Ric}\circ h+h\circ\operatorname{Ric}
-2\mathring Rh,\qquad
L=\frac12(\Delta_L-2\lambda)
\]
on TT tensors. In the curvature-operator norms used by the supplied Chern–Weil formula, the required Hessian is
\[
\boxed{
D^2\mathcal W_{g_E}(h,h)
=\frac14\left\langle
(\Delta_L-2\lambda)h,\,
(\Delta_L-\tfrac43\lambda)h
\right\rangle_{L^2}
=\langle Lh,(L+\lambda/3)h\rangle,
}
\]
where \(\mathcal W=\int(|W^+|^2+|W^-|^2)\).
The \(W^+\) Hessian is half this expression, since signature is fixed.

This resolves the apparent factor-four disagreement between the branches: the larger formula uses the full \((0,4)\)-tensor norm, which is four times the curvature-operator Weyl norm.

A derivation fixing the normalization uses
\[
8\pi^2\chi=\mathcal W-\frac12P+\frac1{24}\int s^2,
\]
together with
\[
P''(h,h)=2\|Lh\|_2^2,\qquad
\left(\int s^2\right)''(h,h)=-8\lambda\langle Lh,h\rangle.
\]

For an \(L\)-eigenvalue \(\mu\), the Weyl Hessian has sign
\[
\mu(\mu+\lambda/3).
\]
Thus, even if Einstein stability gives \(L\ge0\), Weyl local minimality requires exclusion of
\[
0<\mu<-\lambda/3.
\]
At the Step-48 ball-quotient normalization \(\lambda=-6\), this requires a gap up to \(2\). The supplied Proposition 48.3 gives only \(L\ge1\); it is insufficient. Zero modes and higher-order terms must also be handled before inferring an actual local minimum.

### A local coupled estimate needs less

On a Yamabe/gauge slice through a KE metric on \(X\), the quadratic expansions are
\[
\kappa(g_t)
=-\frac{3t^2}{32\pi^2}
\langle Lh,(L+\lambda/3)h\rangle+O(t^3),
\qquad
p(g_t)=\frac{t^2}{8\pi^2}\|Lh\|^2+O(t^3).
\]
For a ball quotient, the supplied \(L\ge1\) gives
\[
\boxed{\kappa\le\frac34p\quad\text{at quadratic order}.}
\]
Indeed, the ratio on an eigenmode is
\[
\frac34\left(\frac2\mu-1\right)\le\frac34.
\]

With a smooth Yamabe slice, elliptic control, and nonlinear remainder estimates, this yields a genuine sufficiently-small-neighborhood estimate with **any fixed \(\beta>3/4\)**. The branch’s assertion of an exact nonlinear \(\beta=3/4\) is not justified by a quadratic calculation.

More generally, a coercive gap \(L\ge m>0\) gives the quadratic upper constant
\[
\beta_{\rm quad}
=\max\left\{0,\frac34\left(\frac{-\lambda}{3m}-1\right)\right\}.
\]
For general negative KE hosts with Einstein zero modes, integrability/moduli control is an additional issue. The supplied files do not resolve it.

## What is genuinely added

**Direct reformulations of existing estimates:** 62.1; the period averaging; 62.2; elimination to \(L_A\); its global minimum \(k-A/3\); 62.C’s equivalences; and the signature-based ASD reformulation. These do not establish a new unconditional Einstein gap in the open range.

**Useful new consequences and research objects:** the explicit conditional dependence on the conformal Weyl infimum \(\kappa_*\); exact algebraic common-mode formulas; the corrected coupled-cap consequences for periods and near-small-defect families; Conjectures 62.W/62.G; and the local Hessian comparison distinguishing a finite susceptibility bound from Weyl local minimality.

The unresolved geometric input is precise: an all-metric or near-minimizer **upper bound on \(\kappa\)**, such as \(\kappa\le k+\beta p\), or an equivalent anti-self-dual Weyl-energy bound. The supplied LeBrun estimates constrain the lower cost in \(\upsilon\) of a chosen \(\kappa\); they do not supply that upper capacity bound.
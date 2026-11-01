# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md",
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Knowledge/objects/papers/math-0111228-Curvature-Connected-Sums-and-Seiberg-Witten-Theory--84e6ef833958--5b74c8864d85/object.md"
  ]
}
```

## Task

Verify Step 62 (workspace/notes/step62_weyl_channel_reduction.md) line by line. Setting: X minimal general type, A=c1^2(X), b+>=2, SW(X)!=0, M=X#kCP2bar, sign family a_eps=K+sum eps_i E_i are monopole classes, P=int|Ric°|^2, p=P/8pi^2. Check: (1) Identity 62.1 p(g~)=(k-kappa)+(upsilon-kappa)/3 with kappa=A/2-(3/8pi^2)int|W+|^2, upsilon=Y^2/(32pi^2)-A, via Chern-Weil 2chi+3tau=(1/4pi^2)int(2|W+|^2+s^2/24-|Ric°|^2/2), and P(g)>=P(g~) for the s=-4 Yamabe representative; check against the certified cell numbers in step48 note §2 (omega=4*0.018784, upsilon=4*0.053096 per class gives p≈0.99566). (2) The envelope 62.2 2sqrt(A+upsilon)+sqrt(A-2kappa)>=3sqrt(A+Pi) from LeBrun Prop 4 (Knowledge LeBrun object lines 145-149) and Cauchy-Schwarz; whether max_eps (a_eps^+)^2>=A is correct and Pi>=|K^-|^2+sum|E_i^+|^2. (3) Theorem 62.A L_A(k,kappa)=(k-kappa)+(1/2)(A-kappa-sqrt(A^2-2A kappa)) for kappa<=4A/9, including the elimination algebra, monotonicity, and the k-A/3 regime. (4) Kähler metrics have kappa<=0 (Hodge index on the Kähler cone of blow-ups), recovering the Kähler tariff. (5) Formal common mode expansions (kappa=k-k^3/4A^2, upsilon=k+3k^2/4A+k^3/2A^2, p=k^2/4A+k^3/2A^2) and that it lies on the equality locus to O(k^3/A^2). (6) Corollary 62.C equivalences and the resulting k^2/((4+4beta)A) bound and tariff k/(gamma+1). (7) The ASD reformulation for ball quotients (inf int|W-|^2 >= 28pi^2 k/3) and the tariff c=1-(9/2)(1-lambda). (8) The Gursky analogy (b+>0, Y>0 => int|W+|^2>=(4pi^2/3)(2chi+3tau)) and its per-point reading, and whether Conjecture 62.G is contradicted by anything standard (e.g. Taubes ASD metrics, known ASD metrics with b+>0, LeBrun estimates). (9) The claim that near a negative KE metric on X, KE is a local maximum of kappa among conformal classes (because negative KE is a local minimizer of int|W|^2 via the TT second variation of the Weyl functional), so the coupled inequality kappa<=beta p holds locally on X; state what formula for the second variation of int|W|^2 at Einstein metrics is needed. Report errors with corrected statements and say precisely what is new versus a direct rewriting of LeBrun's estimates.

## Output

# Scientific verification memo: Step 62

## Overall assessment

The central coordinate change is useful and mostly correct:

- Identity 62.1 is exact.
- The sign-family averaging and envelope 62.2 are correct.
- The displayed function \(L_A(k,\kappa)\), its expansion, and its turning point at \(\kappa=4A/9\) are correct for \(0\le \kappa\le A/2\).
- The formal common mode computations are correct and can be strengthened to exact algebraic equality with the envelope in the small-\(k/A\) regime.
- Corollary 62.C’s three formulations are exactly equivalent.

Several statements need repair:

1. The proof of Identity 62.1 contains a coefficient typo.
2. Solving the envelope by squaring requires attention when \(\kappa<0\); Theorem 62.A as written is too broad on that side.
3. Corollary 62.B requires \(k\le4A/9\) for the displayed \(L_A(k,k)\) substitution.
4. The assertion about arbitrary Kähler complex structures being standard blow-ups is not established by the stated hypotheses, although \(\kappa\le0\) follows directly from the monopole scalar estimate.
5. The formal mode satisfies \(\upsilon\le k+3p\) with cubic slack, not exact equality.
6. Corollary 62.D does not follow from 62.1 and 62.2 alone.
7. Local minimality of the Weyl functional at an Einstein metric with Einstein constant \(\lambda<0\) requires a spectral statement; Einstein/Bach-flat criticality alone is insufficient.

---

## 1. Identity 62.1 and the certified-cell arithmetic

From
\[
4\pi^2(2\chi+3\tau)
 =\int_M\left(2|W^+|^2+\frac{s^2}{24}-\frac{|\operatorname{Ric}^\circ|^2}{2}\right)d\mu
\]
one obtains
\[
P
=4\int|W^+|^2+\frac1{12}\int s^2
 -8\pi^2(2\chi+3\tau).
\]
Since
\[
(2\chi+3\tau)(M)=A-k,
\]
and
\[
\int|W^+|^2=\frac{4\pi^2}{3}(A-2\kappa),\qquad
Y[g]^2=32\pi^2(A+\upsilon),
\]
the Yamabe representative satisfies
\[
\begin{aligned}
p(\widetilde g)
&=\frac{1}{8\pi^2}\left[
\frac{16\pi^2}{3}(A-2\kappa)
+\frac{8\pi^2}{3}(A+\upsilon)
-8\pi^2(A-k)\right]\\
&=k-\frac43\kappa+\frac13\upsilon\\
&=(k-\kappa)+\frac13(\upsilon-\kappa).
\end{aligned}
\]

Thus Identity 62.1 is correct.

### Typo in the written proof

The line
\[
p=\frac16(A-2\kappa)+\frac13(A+\upsilon)-A+k
\]
must read
\[
\boxed{\;
p=\frac23(A-2\kappa)+\frac13(A+\upsilon)-A+k.
\;}
\]
The final formula in the note uses the correct coefficient.

### Why \(P(g)\ge P(\widetilde g)\)

In dimension four, \(\int|W^+|^2\) is conformally invariant. Hence
\[
P(g)-P(\widetilde g)
=\frac1{12}\left(\int s_g^2\,d\mu_g-Y[g]^2\right).
\]
The monopole scalar estimate and \(\max_\varepsilon(a_\varepsilon^+)^2\ge A>0\) imply that every conformal class has \(Y[g]<0\). In a class with \(Y[g]<0\), the Yamabe representative minimizes the \(L^2\)-norm of scalar curvature, so
\[
\int s_g^2\,d\mu_g\ge Y[g]^2.
\]
Therefore \(P(g)\ge P(\widetilde g)\).

### Cell arithmetic

Using the Step-48 units,
\[
\omega=4(0.018784)=0.075136,\qquad
\kappa=\frac34\omega=0.056352,
\]
and
\[
\upsilon=4(0.053096)=0.212384.
\]
For one exceptional class,
\[
p=1-\omega+\frac{\upsilon}{3}
 =1-0.075136+0.070794666\ldots
 =0.995658666\ldots.
\]
This agrees with the quoted interval value \(0.9956627\) to the precision permitted by the rounded Step-48 inputs.

---

## 2. Sign-family averaging and envelope 62.2

Write \(|a^-|^2:=-(a^-)^2\). Since
\[
a_\varepsilon^2=A-k,
\]
we have
\[
(a_\varepsilon^+)^2=A-k+|a_\varepsilon^-|^2.
\]
Averaging over all signs gives
\[
\mathbb E_\varepsilon |a_\varepsilon^-|^2
=|K_X^-|^2+\sum_i|E_i^-|^2.
\]
Because
\[
-1=E_i^2=|E_i^+|^2-|E_i^-|^2,
\]
it follows that
\[
|E_i^-|^2=1+|E_i^+|^2.
\]
Consequently,
\[
\mathbb E_\varepsilon(a_\varepsilon^+)^2
=A+|K_X^-|^2+\sum_i|E_i^+|^2.
\]
Thus, with
\[
\Pi=\max_\varepsilon(a_\varepsilon^+)^2-A,
\]
one indeed has
\[
\boxed{\;
\Pi\ge |K_X^-|^2+\sum_i|E_i^+|^2\ge0.
\;}
\]

Proposition 2 in the supplied Ishida–LeBrun source then gives
\[
Y[g]^2\ge32\pi^2(A+\Pi),
\qquad\text{hence}\qquad
\upsilon\ge\Pi.
\]

For the selected sign class, Proposition 4 gives
\[
\int(s-\sqrt6|W^+|)^2\,d\mu
\ge72\pi^2(A+\Pi).
\]
At the representative \(s=-4\), Minkowski’s inequality gives
\[
\left\|s-\sqrt6|W^+|\right\|_2
\le \|s\|_2+\sqrt6\|W^+\|_2.
\]
The two terms are
\[
\|s\|_2
=4\sqrt2\,\pi\sqrt{A+\upsilon},
\]
and
\[
\sqrt6\|W^+\|_2
=2\sqrt2\,\pi\sqrt{A-2\kappa}.
\]
Comparing with
\[
\sqrt{72\pi^2(A+\Pi)}
=6\sqrt2\,\pi\sqrt{A+\Pi}
\]
gives exactly
\[
\boxed{\;
2\sqrt{A+\upsilon}+\sqrt{A-2\kappa}
\ge3\sqrt{A+\Pi}.
\;}
\]

Thus 62.2 is a direct consequence of Proposition 4 plus the \(L^2\) triangle inequality.

### Solving the envelope

For \(\Pi=0\), put
\[
y=\sqrt{1-\frac{2\kappa}{A}}.
\]
When \(0\le\kappa\le A/2\), one has \(0\le y\le1\), and squaring is valid:
\[
\upsilon\ge
A\left[\left(\frac{3-y}{2}\right)^2-1\right]
=:\upsilon_L(\kappa).
\]
Its expansion is
\[
\boxed{\;
\upsilon_L(\kappa)
=\kappa+\frac{3\kappa^2}{4A}
+\frac{3\kappa^3}{4A^2}
+O\!\left(\frac{\kappa^4}{A^3}\right).
\;}
\]

For arbitrary \(\kappa\le A/2\), the universally valid consequence is instead
\[
\upsilon\ge
\max\left\{
0,\,
A\left[\left(\frac{(3-y)_+}{2}\right)^2-1\right]
\right\}.
\]
In particular, for \(\kappa\le0\), the useful estimate is simply
\[
\upsilon\ge0.
\]
The unqualified formula \(\upsilon\ge\upsilon_L(\kappa)\) is not obtained by this squaring argument when \(\kappa<-12A\).

For all \(\kappa\), the estimates imply
\[
\boxed{\;\upsilon\ge\kappa.\;}
\]
Indeed, this is immediate from \(\upsilon\ge0\) when \(\kappa\le0\); for \(\kappa\ge0\),
\[
\upsilon_L-\kappa
=\frac{3A}{4}(1-y)^2\ge0.
\]

The supplied source states that equality in Proposition 4 requires a symplectic structure with the relevant first Chern class and refers to a more detailed special almost-Kähler equality structure in LeBrun’s earlier paper. The exact curvature characterization is not contained in the supplied passage.

---

## 3. Theorem 62.A: algebra, monotonicity, and corrected domain

For \(0\le\kappa\le A/2\), Identity 62.1 and the envelope yield
\[
\begin{aligned}
p
&\ge k-\frac43\kappa+\frac13\upsilon_L(\kappa)\\
&=k-\frac32\kappa
+\frac A2\left(1-\sqrt{1-\frac{2\kappa}{A}}\right)\\
&=(k-\kappa)
+\frac12\left(A-\kappa-\sqrt{A^2-2A\kappa}\right).
\end{aligned}
\]
Thus
\[
\boxed{\;
L_A(k,\kappa)
=(k-\kappa)
+\frac12\left(A-\kappa-\sqrt{A^2-2A\kappa}\right)
\;}
\]
is correct. Its expansion is
\[
L_A(k,\kappa)
=(k-\kappa)
+\frac{\kappa^2}{4A}
+\frac{\kappa^3}{4A^2}
+O\!\left(\frac{\kappa^4}{A^3}\right).
\]

For \(\kappa\le0\), the clean bound is
\[
\boxed{\;
p\ge k-\frac43\kappa\ge k.
\;}
\]

Accordingly, the directly proved pointwise statement is
\[
p\ge
\begin{cases}
k-\dfrac43\kappa,&\kappa\le0,\\[6pt]
L_A(k,\kappa),&0\le\kappa\le A/2.
\end{cases}
\]
The original wording “for every \(\kappa\le4A/9\)” includes arbitrarily low values of \(\kappa\), where its proof by squaring does not apply.

### Monotonicity and the \(4A/9\) turning point

For \(0<\kappa<A/2\),
\[
\frac{\partial L_A}{\partial\kappa}
=-\frac32+\frac{1}{2\sqrt{1-2\kappa/A}}.
\]
Hence:

- \(L_A\) decreases for \(0\le\kappa<4A/9\);
- it is stationary at \(\kappa=4A/9\);
- it increases for \(4A/9<\kappa<A/2\).

At the stationary point,
\[
L_A\left(k,\frac{4A}{9}\right)=k-\frac A3.
\]
Therefore the global consequence of LeBrun’s mixed estimate is
\[
\boxed{\;p\ge k-\frac A3.\;}
\]
For a fixed \(\kappa>4A/9\), the fixed-\(\kappa\) estimate \(L_A(k,\kappa)\) is actually stronger than \(k-A/3\); the latter is the minimum after optimizing over \(\kappa\).

### Corollary 62.B needs an explicit \(k/A\) hypothesis

The implication
\[
\kappa_*\le k
\quad\Longrightarrow\quad
p\ge L_A(k,k)
\]
uses that \(L_A\) is decreasing up to the cap \(k\). It therefore requires
\[
\boxed{\;k\le\frac{4A}{9}.\;}
\]
Under this hypothesis,
\[
P\ge8\pi^2L_A(k,k)
=4\pi^2\left(A-k-\sqrt{A^2-2Ak}\right),
\]
with expansion
\[
P\ge\frac{2\pi^2k^2}{A}
\left(1+\frac{k}{A}+O((k/A)^2)\right).
\]
For \(4A/9<k\le A/2\), the cap \(\kappa_*\le k\) only gives the minimum \(p\ge k-A/3\) through this argument.

---

## 4. Kähler metrics and the tariff

The conclusion
\[
\kappa\le0
\]
for every Kähler metric is correct, but it has a shorter proof that avoids classifying all complex structures on the smooth manifold.

For a Kähler metric in real dimension four,
\[
|W^+|^2=\frac{s^2}{24}.
\]
Choose the sign class with \((a^+)^2\ge A\). Proposition 2 gives
\[
\int s^2\,d\mu\ge32\pi^2A.
\]
Therefore
\[
\int|W^+|^2\,d\mu
=\frac1{24}\int s^2\,d\mu
\ge\frac{4\pi^2}{3}A,
\]
which is equivalent to
\[
\boxed{\;\kappa\le0.\;}
\]

Then Identity 62.1 gives
\[
p(\widetilde g)\ge k,
\qquad
p(g)\ge p(\widetilde g),
\]
so
\[
\boxed{\;P(g)\ge8\pi^2k.\;}
\]

The Hodge-index calculation in the note is valid for a Kähler structure explicitly presented as the blow-up of a minimal model with canonical square \(A\). The sentence asserting that every Kähler complex structure on the underlying smooth manifold has this presentation is not established by the hypotheses written in Step 62. The monopole argument above proves the desired conclusion without that extra classification statement.

An Arezzo–Pacard recovery sequence is an additional construction: it requires a suitable cscK or Kähler–Einstein host and the corresponding gluing hypotheses. It is not a consequence of the Hodge-index estimate alone.

---

## 5. Formal common mode

Let
\[
h=\frac{k}{A}.
\]
The formal mode has
\[
\int|W^+|^2
=\frac{4\pi^2A}{3}\frac{(2-3h)^2}{(2-h)^2}.
\]
Hence
\[
\frac{\kappa}{A}
=\frac12\left[1-\frac{(2-3h)^2}{(2-h)^2}\right]
=\frac{4h(1-h)}{(2-h)^2}.
\]
Also
\[
\frac{\upsilon}{A}
=\frac{4}{(2-h)^2}-1
=\frac{h(4-h)}{(2-h)^2}.
\]
Identity 62.1 then gives the exact expression
\[
\frac pA=\frac{h^2(1+h)}{(2-h)^2}.
\]

Expanding,
\[
\boxed{
\begin{aligned}
\kappa
&=k-\frac{k^3}{4A^2}
+O\!\left(\frac{k^4}{A^3}\right),\\
\upsilon
&=k+\frac{3k^2}{4A}
+\frac{k^3}{2A^2}
+O\!\left(\frac{k^4}{A^3}\right),\\
p
&=\frac{k^2}{4A}
+\frac{k^3}{2A^2}
+O\!\left(\frac{k^4}{A^3}\right).
\end{aligned}}
\]

For \(0\le h\le2/3\),
\[
\sqrt{1+\upsilon/A}=\frac{2}{2-h},
\qquad
\sqrt{1-2\kappa/A}=\frac{2-3h}{2-h},
\]
so
\[
2\sqrt{1+\upsilon/A}
+\sqrt{1-2\kappa/A}=3
\]
exactly. Thus the formal mode lies exactly on the \(\Pi=0\) envelope at the algebraic level in this interval, not merely through cubic order. Consequently \(p=L_A(k,\kappa)\) exactly there.

There is, however, cubic slack in the affine susceptibility relation:
\[
k+3p-\upsilon
=4(k-\kappa)
=\frac{4Ah^3}{(2-h)^2}.
\]
Therefore
\[
\upsilon=k+3p
\]
holds only through order \(k^2/A\), not exactly and not through order \(k^3/A^2\).

---

## 6. Corollary 62.C and Corollary 62.D

From Identity 62.1,
\[
4\kappa=3k+\upsilon-3p.
\]
Therefore
\[
\kappa\le k+\beta p
\]
is equivalent to
\[
\upsilon\le k+(3+4\beta)p.
\]
Also,
\[
\int|W^+|^2+\frac{\beta}{3}P
=\frac{4\pi^2}{3}\left(A-2\kappa+2\beta p\right),
\]
so this is at least \(\frac{4\pi^2}{3}(A-2k)\) exactly when
\[
\kappa\le k+\beta p.
\]
Thus the three statements in Corollary 62.C are exactly equivalent, with \(P=P(\widetilde g)\).

### The \(k^2/A\) estimate

Put
\[
x=k+\beta p.
\]
When \(0\le x\le4A/9\), monotonicity gives
\[
p\ge L_A(k,x).
\]
Since
\[
\frac12\left(A-x-\sqrt{A^2-2Ax}\right)
=\frac{x^2}{2(A-x+\sqrt{A^2-2Ax})}
\ge\frac{x^2}{4A},
\]
one obtains
\[
p\ge-\beta p+\frac{(k+\beta p)^2}{4A}.
\]
For fixed \(\beta\) and \(k/A\to0\), the small root gives
\[
\boxed{\;
p\ge\frac{k^2}{4(1+\beta)A}
\left(1+O(k/A)\right).
\;}
\]
The \(x\le4A/9\) condition is automatic in the small-\(k/A\), small-\(p\) branch; if \(x\) is already larger, then \(p\) is much larger than the displayed \(k^2/A\) scale.

### Linear susceptibility

Since \(\upsilon\ge\kappa\),
\[
p=k-\frac43\kappa+\frac13\upsilon
\ge k-\upsilon.
\]
Thus
\[
\upsilon\le\gamma p
\quad\Longrightarrow\quad
p\ge k-\gamma p,
\]
and therefore
\[
\boxed{\;p\ge\frac{k}{\gamma+1}.\;}
\]
This part is exact.

### Corollary 62.D does not follow from 62.1 and 62.2 alone

The decomposition
\[
p=(k-\kappa)+\frac13(\upsilon-\kappa)
\]
has \(\upsilon-\kappa\ge0\), but \(k-\kappa\) need not be \(\ge0\). Hence the two terms can cancel when \(\kappa>k\).

A concrete algebraic family illustrating this is
\[
\kappa=2k,\qquad
\upsilon=5k,\qquad
p=0,\qquad
\Pi=k,
\]
with \(k/A\to0\). Identity 62.1 is exact:
\[
k-\frac83k+\frac53k=0.
\]
Moreover,
\[
2\sqrt{A+5k}+\sqrt{A-4k}
=3\sqrt A+\frac{3k}{\sqrt A}+O(k^2/A^{3/2}),
\]
while
\[
3\sqrt{A+k}
=3\sqrt A+\frac{3k}{2\sqrt A}+O(k^2/A^{3/2}),
\]
so 62.2 holds for sufficiently small \(k/A\). Also \(\upsilon\ge\Pi\).

No geometric realization of these algebraic values is asserted; they show that 62.1 and 62.2 by themselves do not force
\[
\kappa/k\to1,\qquad
\upsilon-\kappa=o(k),\qquad
\Pi=o(k).
\]

Those conclusions do follow after adding substantive information such as
\[
\kappa\le k+o(k),
\]
together with \(p=o(k)\) and the near-equality expansion of 62.2. That extra upper relation is precisely the missing Weyl-channel input.

The Step-47 period lemma was not supplied here, so the sentence connecting exact common modes to that lemma cannot be independently verified from the present files.

---

## 7. Anti-self-dual reformulation

The signature identity is
\[
\int|W^+|^2-\int|W^-|^2=12\pi^2\tau(M),
\qquad
\tau(M)=\tau_X-k.
\]
Therefore
\[
\int|W^+|^2\ge\frac{4\pi^2}{3}(A-2k)
\]
is equivalent to
\[
\begin{aligned}
\int|W^-|^2
&\ge \frac{4\pi^2}{3}(A-2k)-12\pi^2(\tau_X-k)\\
&=\frac{4\pi^2}{3}(A-9\tau_X)+\frac{28\pi^2}{3}k.
\end{aligned}
\]
This is correct.

For a complex-hyperbolic surface,
\[
A=9\tau_X,
\]
so the condition becomes
\[
\boxed{\;
\int|W^-|^2\ge\frac{28\pi^2}{3}k.
\;}
\]

If instead
\[
\int|W^-|^2\ge12\pi^2\lambda k,
\]
then
\[
\int|W^+|^2
\ge\frac{4\pi^2}{3}A-12\pi^2(1-\lambda)k.
\]
Hence
\[
\kappa\le\frac92(1-\lambda)k.
\]
Using \(p\ge k-\kappa\) gives
\[
p\ge
\left[1-\frac92(1-\lambda)\right]k.
\]
Thus
\[
\boxed{\;
c=1-\frac92(1-\lambda)
\;}
\]
is correct, and \(c>0\) exactly when \(\lambda>7/9\).

The listed per-class values are consistent:

- reversed Fubini–Study and Burns: \(12\pi^2\);
- certified cell: \(12\pi^2-0.150272\pi^2\), using \(8(0.018784)\pi^2=0.150272\pi^2\);
- formal mode: \(12\pi^2-\frac{8\pi^2}{3}=\frac{28\pi^2}{3}\).

---

## 8. Gursky analogy and Conjecture 62.G

The standard Gursky theorem is correctly stated provided \(Y[g]>0\) refers to the Yamabe constant of the conformal class:
\[
b^+>0,\quad Y[g]>0
\quad\Longrightarrow\quad
\int|W^+|^2\,d\mu
\ge\frac{4\pi^2}{3}(2\chi+3\tau).
\]
Its source is not among the supplied files, so the equality characterization is not source-verifiable here.

Under one blow-up, \(2\chi+3\tau\) decreases by one. Thus this inequality allows a decrease of at most \(4\pi^2/3\) in the lower bound per blow-up, whereas Conjecture 62.W requires control corresponding to \(8\pi^2/3\) per blow-up. The “half” comparison is correct.

For \(\mathbb{CP}^2\),
\[
\int|W^+|^2=12\pi^2.
\]
Reaching \(W^+=0\) after ten blow-ups corresponds to an average decrease
\[
\frac{12\pi^2}{10}=1.2\pi^2
\]
per point, close to \(4\pi^2/3\).

Conjecture 62.G,
\[
\inf_g\int|W^+|^2
\ge\frac{4\pi^2}{3}(A-k),
\]
is equivalent to
\[
\kappa_*\le\frac k2.
\]
For \(k\le4A/9\), Theorem 62.A would then give
\[
p\ge L_A(k,k/2)
=\frac k2+\frac{k^2}{16A}+O(k^3/A^2),
\]
hence
\[
P\ge4\pi^2k\left(1+\frac{k}{8A}+O((k/A)^2)\right).
\]

Nothing in the supplied standard results contradicts this conjecture:

- Taubes’ construction produces anti-self-dual metrics after sufficiently many blow-ups but supplies no universal threshold below \(A\).
- When \(k\ge A\), the right side of Conjecture 62.G is already \(\le0\), so such metrics are automatically compatible with it.
- Anti-self-dual metrics on manifolds such as K3 concern \(A=0\), not the general-type situation here.
- Proposition 4 permits \(W^+=0\) if the scalar-curvature term pays for the monopole lower bound; it does not by itself impose the proposed \(k\ge A\) threshold.

An anti-self-dual metric with \(k<A\) on one of these blow-ups would contradict Conjecture 62.G. No such example appears in the supplied material.

---

## 9. Local Weyl behavior near a Kähler–Einstein metric

Let \(g_E\) be Einstein with
\[
\operatorname{Ric}(g_E)=\lambda g_E,\qquad \lambda<0.
\]
Einstein metrics are Bach-flat, so the Weyl functional is critical. Criticality alone does not imply local minimality.

Use the positive-sign Lichnerowicz Laplacian
\[
(\Delta_Lh)_{ij}
=\nabla^*\nabla h_{ij}
+R_i{}^kh_{kj}+R_j{}^kh_{ik}
-2R_{ikjl}h^{kl}.
\]
On transverse-traceless tensors, define the linearized trace-free Ricci operator
\[
\mathcal E h
=\frac12(\Delta_L-2\lambda)h.
\]
With the curvature normalizations used in Step 62, the second variation of the total Weyl functional is
\[
\boxed{\;
D^2\!\left(\int|W|^2d\mu\right)_{g_E}(h,h)
=
\frac14\int
\left\langle
(\Delta_L-2\lambda)h,\,
(\Delta_L-\tfrac43\lambda)h
\right\rangle d\mu.
\;}
\]
Equivalently,
\[
D^2\mathcal W(h,h)
=\int\langle\mathcal Eh,(\mathcal E+\lambda/3)h\rangle\,d\mu.
\]

Since
\[
\int|W|^2
=2\int|W^+|^2-12\pi^2\tau,
\]
the Hessian of \(\int|W^+|^2\) is one half of this expression.

If \(\mu\) is an eigenvalue of \(\mathcal E\), the corresponding Weyl Hessian factor is
\[
\mu(\mu+\lambda/3).
\]
For \(\lambda<0\), local Weyl minimality on the TT slice therefore requires, after treating zero modes,
\[
\mu\notin(0,-\lambda/3).
\]
At the Step-48 normalization \(\lambda=-6\), this requires a gap from \(0\) to \(2\). Proposition 48.3 only proves
\[
\mathcal E\ge1,
\]
which does not establish Weyl local minimality.

Thus the general assertion that a Kähler–Einstein metric with \(\lambda<0\) locally minimizes \(\int|W|^2\) is not justified by Einstein/Bach-flat criticality or by the Step-48 estimate alone. It becomes valid under the required spectral statement, plus control of zero modes and higher-order terms.

For a TT deformation \(g_t=g_E+th+\cdots\),
\[
P(g_t)=t^2\|\mathcal Eh\|_2^2+O(t^3),
\]
while \(\kappa\) is governed quadratically by the Weyl Hessian. A local coupled estimate
\[
\kappa\le\beta p
\]
therefore requires an operator inequality of the form
\[
-\frac12D^2\mathcal W(h,h)
\le C\|\mathcal Eh\|_2^2
\]
on the slice transverse to Einstein moduli. For a fixed compact Einstein metric with a spectral gap away from the kernel, such a finite \(C\) is plausible from the factorized formula. Uniformity over families or quotients requires a uniform spectral gap. If the kernel contains infinitesimal Einstein deformations, their integrability and the higher-order expansion must also be included.

If full local Weyl minimality is established, then \(\kappa\le0\) locally and the coupled inequality holds with \(\beta=0\). That conclusion is stronger than what is needed; a finite comparison between the two quadratic forms would already give a local \(\beta\).

---

## What is new here versus direct use of LeBrun’s estimates

The following parts are algebraic reformulations of established ingredients:

- Identity 62.1: Chern–Weil plus conformal invariance and Yamabe minimization.
- Envelope 62.2: Proposition 4 plus the \(L^2\) triangle inequality.
- The function \(L_A(k,\kappa)\): elimination of \(\upsilon\) from those two formulas.
- The bound \(p\ge k-A/3\): optimization of the same LeBrun estimate.
- Corollary 62.C: exact algebraic equivalence among three presentations.
- The anti-self-dual formula: signature identity.

The genuinely useful added structure is the identification of
\[
\kappa_*=
\frac A2-\frac{3}{8\pi^2}\inf_g\int|W^+|^2
\]
as the missing conformal invariant whose upper control would yield stronger Einstein-defect bounds. Conjectures 62.W and 62.G supply new geometric input not contained in Proposition 2, Proposition 4, or their Weitzenböck derivations. The proposed local comparison near an Einstein metric likewise requires a new spectral estimate for the factorized Weyl Hessian.
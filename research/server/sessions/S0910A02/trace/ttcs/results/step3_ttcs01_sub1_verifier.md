# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md",
    "Sessions/S0910A02/workspace/notes/step3_corrections_lebrun_and_collapse.md",
    "Sessions/S0910A02/workspace/notes/step3_stable_integral_obstruction_principle.md",
    "Sessions/S0910A02/workspace/scripts/step3_corrected_lebrun_bounds.py",
    "Sessions/S0910A02/workspace/scripts/lens_space_positive_collapse.py",
    "Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md",
    "Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md"
  ]
}
```

## Task

Check the Step 3 repaired LeBrun/Ishida-LeBrun analysis for Yau Problem 26. Read the active goal, the correction note, the stable integral obstruction theorem note, the repaired script, and the primary source excerpts/files. Verify the constants in the 4D Chern-Gauss-Bonnet identity, the scalar-only k/A=2/3 and mixed k/A=1/3 thresholds, the derivation of the pinching lower bound δ/(1-δ) >= sqrt((p-1/3)/2), and the corrected interpretation of positive collapse via lens spaces. Identify any algebraic mistakes, missing hypotheses (orientation, b_+, monopole class, strict/equality cases), or overclaims relative to the full Yau26 proposition. Give a direct scientific memo, not a checklist.

## Output

# Scientific verification memo

## Overall assessment

The repaired Chern–Gauss–Bonnet constants, the \(2/3\) scalar threshold, the \(1/3\) mixed Seiberg–Witten threshold, and the pinching estimate are mathematically correct. Three qualifications matter:

1. `step3_corrected_lebrun_bounds.py` mishandles the endpoint \(p=2/3\): LeBrun’s strict scalar estimate excludes \(p=2/3\), not only \(p>2/3\).
2. The pinching application of the stable theorem requires \(T_+=A-k>0\), hence \(1/3<p<1\). The displayed formula has not been established there for \(p>1\).
3. At \(p=1/3\), Einstein nonexistence uses LeBrun’s equality characterization, not merely the weak inequality \(F_+\ge 2A/3\).

The lens-space interpretation is correct and gives genuine bounded-sectional-curvature collapse with exact Einstein metrics.

## 1. Four-dimensional curvature constants

With
\[
E=\mathring{\operatorname{Ric}},\qquad
T_+(M)=2\chi(M)+3\tau(M),
\]
the source normalization is
\[
T_+(M)=\frac1{4\pi^2}\int_M
\left(2|W^+|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)d\mu.
\]

For an Einstein metric \(\operatorname{Ric}=\lambda g\) in dimension four,
\[
s=4\lambda,\qquad E=0.
\]
Consequently,
\[
8\pi^2T_+
=4\int_M|W^+|^2\,d\mu+\frac43\lambda^2V,
\]
and therefore
\[
\int_M|W^+|^2\,d\mu
=2\pi^2T_+-\frac13\lambda^2V.
\]
Thus the Step 3 correction of the previous factor \(16/3\) to \(4/3\) is exact.

## 2. Scalar estimate and the \(p=2/3\) endpoint

For
\[
M=X\#k\overline{\mathbb{CP}}^{\,2},\qquad
A=c_1^2(X),\qquad T_+(M)=A-k,
\]
LeBrun 1996 gives, for \(k>0\),
\[
\int_Ms^2\,d\mu>32\pi^2A.
\]
For an Einstein metric this becomes
\[
16\lambda^2V>32\pi^2A,
\qquad\text{so}\qquad
\lambda^2V>2\pi^2A.
\]
Substitution into the corrected curvature identity yields
\[
\int_M|W^+|^2\,d\mu
<
2\pi^2(A-k)-\frac23\pi^2A
=
\pi^2A\left(\frac43-2p\right),
\qquad p=\frac{k}{A}.
\]
Since the left side is \(\ge0\), this is impossible whenever
\[
p\ge\frac23.
\]
At \(p=2/3\), the right side is strictly below zero because LeBrun’s scalar estimate is strict.

Accordingly, the following script output is inconsistent with source Theorem 3:

```python
"contradiction": coeff < 0
```

At `p = 2/3`, `coeff == 0`, but the actual estimate is strict:
\[
W_2<\pi^2A\,\mathrm{coeff}=0.
\]
The printed sentence “Contradiction begins only for \(p>2/3\)” and the JSON wording using \(k/A>2/3\) omit the equality endpoint. The correction note itself handles this endpoint correctly.

## 3. Mixed estimate and the \(p=1/3\) endpoint

LeBrun 2001 Proposition 3.1, equivalently the Ishida–LeBrun mixed estimate followed by Cauchy–Schwarz, gives
\[
F_+(g):=
\frac1{4\pi^2}\int_M
\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu
\ge \frac23(a^+)^2.
\]
The blow-up sign selection gives
\[
(a^+)^2\ge A,
\]
hence
\[
F_+(g)\ge\frac23A.
\]
Combining this with
\[
F_+(g)=A-k+\frac1{4\pi^2}\int_M\frac{|E|^2}{2}\,d\mu
\]
gives
\[
\int_M\frac{|E|^2}{2}\,d\mu
\ge4\pi^2\left(k-\frac A3\right).
\]

For an Einstein metric \(E=0\), the weak inequality excludes \(k>A/3\). At \(k=A/3\), LeBrun 2001 Proposition 3.2 supplies the additional fact that equality in the \(F_+\) estimate is possible only when no blow-up or \(S^1\times S^3\) summand occurs. Thus \(k=A/3>0\) is excluded as well, producing the exact source statement
\[
k\ge\frac A3\quad\Longrightarrow\quad
M\text{ carries no Einstein metric}.
\]

For \(k>0\), that equality statement actually strengthens the energy relation to
\[
\int_M\frac{|E|^2}{2}\,d\mu
>
4\pi^2\left(k-\frac A3\right).
\]
The non-strict version in the note remains valid, but the sentence calling the displayed weak estimate “equivalent” to the endpoint-inclusive theorem needs the source equality statement as part of the argument.

## 4. Pinching estimate

Assume
\[
\|\operatorname{Ric}+\!g\|_{\mathrm{op}}\le\delta<1.
\]
Writing the Ricci eigenvalues as \(-1+e_i\), with \(|e_i|\le\delta\), gives
\[
|E|^2=\sum_{i=1}^4(e_i-\bar e)^2
=\sum_i e_i^2-4\bar e^2
\le4\delta^2
\]
and
\[
|s|\ge4(1-\delta),\qquad
\frac{s^2}{24}\ge\frac23(1-\delta)^2.
\]
Define
\[
b(\delta)=\frac23(1-\delta)^2-2\delta^2.
\]
Dropping \(2|W^+|^2\ge0\) in the curvature identity yields
\[
A-k\ge\frac{V}{4\pi^2}b(\delta).
\]
When \(b(\delta)>0\),
\[
V\le\frac{4\pi^2(A-k)}{b(\delta)}.
\]
The mixed energy estimate and the pointwise estimate for \(E\) give
\[
4\pi^2\left(k-\frac A3\right)
\le\int_M\frac{|E|^2}{2}\,d\mu
\le2\delta^2V.
\]
Combining them,
\[
\left(k-\frac A3\right)
\left[\frac23(1-\delta)^2-2\delta^2\right]
\le2\delta^2(A-k).
\]
Moving the \(\delta^2\) terms to the right gives
\[
\frac23\left(k-\frac A3\right)(1-\delta)^2
\le\frac43A\delta^2,
\]
hence
\[
\boxed{\;
\frac{\delta}{1-\delta}
\ge
\sqrt{\frac{k-A/3}{2A}}
=
\sqrt{\frac{p-1/3}{2}}
\; }.
\]
The algebra is exact. At \(p=2/3\),
\[
\delta\ge
\frac{1/\sqrt6}{1+1/\sqrt6}
=
\frac1{1+\sqrt6}
\approx0.289897949.
\]

The stable theorem’s general formula is also correct:
\[
\frac{\delta}{1-\delta}
\ge
\sqrt{\frac{L_+-T_+}{3L_+}}.
\]

### Required hypothesis on \(p\)

The volume estimate in this proof uses
\[
T_+=A-k>0,
\]
so the direct application requires
\[
\frac13<p<1.
\]
This is already present in the stable theorem through the assumption \(T_+(M)>0\), but it is omitted in the final LeBrun application, which states only \(p>1/3\).

For \(1/3<p<1\), the condition \(b(\delta)>0\) causes no gap in the final conclusion. Indeed,
\[
b(\delta)>0
\iff
\delta<\delta_b:=\frac1{1+\sqrt3}.
\]
The derived lower value
\[
\delta_0(p)=
\frac{\sqrt{(p-1/3)/2}}
{1+\sqrt{(p-1/3)/2}}
\]
satisfies \(\delta_0(p)<\delta_b\) for \(p<1\). If \(b(\delta)\le0\), then automatically \(\delta\ge\delta_b>\delta_0(p)\). Thus a short case split extends the displayed lower estimate to every \(\delta<1\) when \(1/3<p<1\).

At \(p=1\), one separately obtains \(\delta\ge\delta_b=\delta_0(1)\). For \(p>1\), the same square-root formula is not supplied by this argument.

## 5. Orientation and Seiberg–Witten hypotheses

The application uses the complex orientation of \(X\), so that
\[
T_+=2\chi+3\tau=A-k
\]
and the relevant Weyl tensor is \(W^+\). The Einstein conclusion itself is orientation-independent, but the integral estimate is tied to this chosen orientation.

There is also a source distinction concerning \(b_+\):

- Ishida–LeBrun’s global monopole-class formulation is stated for \(b_+\ge2\).
- Minimal complex surfaces of general type may have \(b_+=1\).
- LeBrun’s 1996 polarization argument and the 2001 Proposition 3.2/Corollary 3.4 handle the \(b_+=1\) case through metric-dependent chamber or polarization choices.

Thus the all-metric estimate for general-type blow-ups is supported by the 1996/2001 sources. Deriving it solely from the 2003 global monopole-class definition would require \(b_+\ge2\).

For the \(\sigma=+1\) normalized branch, the algebraic stable theorem remains valid because it uses \(s^2\) and \(|E|^2\). On these particular LeBrun manifolds, however, Seiberg–Witten theory already excludes metrics with everywhere positive scalar curvature. Hence
\[
\|\operatorname{Ric}-g\|_{\mathrm{op}}<1
\]
cannot occur at all; the mixed pinching estimate is much weaker on that sign.

## 6. Repaired optimization script

The continuous optimization in `step3_corrected_lebrun_bounds.py` is internally consistent. At \(\delta=0\),
\[
W_2=2\pi^2C-\frac V3,\qquad C=A-k,
\]
and with
\[
x=\frac{V}{\pi^2C},\qquad
y=\frac{W_2}{\pi^2C}=2-\frac x3,
\]
the objective is
\[
16x+8\sqrt6\sqrt{xy}+6y.
\]
Its exact maximizer is
\[
x=\frac{16}{3},\qquad y=\frac29,
\]
and the maximum is
\[
108.
\]
Therefore the script’s numerical value \(F_{\max}=108\) and
\[
p_{\mathrm{crit}}=1-\frac{72}{108}=\frac13
\]
are correct for the relaxed optimization.

The material code defect is confined to the scalar-only \(p=2/3\) endpoint and associated text/JSON, not the mixed optimizer.

## 7. Lens-space collapse

Let \(g_m\) be the quotient of the unit round metric on
\[
L(m,1)=S^3/\mathbb Z_m.
\]
Then
\[
\sec_{g_m}=1,\qquad \operatorname{Ric}_{g_m}=2g_m.
\]
For
\[
h_m=2g_m,
\]
constant metric scaling leaves the Ricci tensor unchanged as a \((0,2)\)-tensor, so
\[
\operatorname{Ric}_{h_m}=2g_m=h_m,
\qquad
\sec_{h_m}=\frac12.
\]
Moreover,
\[
\operatorname{Vol}(L(m,1),h_m)
=2^{3/2}\frac{2\pi^2}{m}\longrightarrow0,
\]
and, for \(m\ge2\),
\[
\operatorname{inj}(L(m,1),h_m)
=\frac{\sqrt2\,\pi}{m}\longrightarrow0.
\]
Sectional curvature and diameter remain uniformly bounded. This is genuine bounded-curvature collapse.

The topology varies with \(m\), since \(\pi_1(L(m,1))\cong\mathbb Z_m\). Every member already carries the displayed Einstein metric, so this sequence is fully compatible with Yau’s desired implication. It decisively shows that tight positive Ricci pinching does not by itself provide noncollapse or topology finiteness.

## 8. Relation to the full Yau proposition

The established theorem concerns dimension four and a specific family of blow-ups with an all-metric Seiberg–Witten estimate. It does not provide universal constants \(c_n<C_n\), a theorem for arbitrary smooth manifolds, or a Lean proof.

For same-sign constants, rescaling identifies the original interval with normalized pinching. If \(0<c<C\), the relative width is
\[
\delta=\frac{C-c}{C+c};
\]
if \(c<C<0\), it is
\[
\delta=\frac{C-c}{-(c+C)}.
\]
The LeBrun estimate therefore says that fixed-margin no-Einstein blow-ups cannot satisfy arbitrarily narrow normalized intervals around \(-g\). It does not exclude the possibility that Yau’s constants select an interval narrower than every such blow-up permits.

There is one immediate fact about the full proposition: in dimension four, constants with
\[
c_4<0<C_4
\]
cannot work. Given any LeBrun manifold carrying no Einstein metric and any initial metric \(g_0\), the metrics \(t g_0\) have Ricci eigenvalues relative to \(t g_0\) tending to zero as \(t\to\infty\). They eventually satisfy
\[
c_4\,t g_0\le\operatorname{Ric}_{t g_0}\le C_4\,t g_0,
\]
while the underlying manifold still carries no Einstein metric.

The concluding heuristic about stability is rigorously established for inequalities of the form
\[
F_\pm(g)\ge L_\pm
\]
that connect to \(T_\pm\) through the four-dimensional curvature identity. The supplied sources do not establish the analogous statement for every possible Einstein nonexistence mechanism, nor do they provide a literature census supporting the phrase “only known examples.” The precise surviving LeBrun scenario is \(p\to1/3^+\), together with an actual construction of metrics whose normalized \(-g\) pinching tends to zero; no such construction appears in the supplied artifacts.
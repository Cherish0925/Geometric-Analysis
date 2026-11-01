# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step2_quantitative_4d_analysis.tex",
    "Sessions/S0910A03/workspace/notes/step2_cap_analysis_and_route.tex",
    "Sessions/S0910A03/workspace/scripts/verify_chern_weil_pinching.py",
    "Sessions/S0910A03/workspace/scripts/critical_compatibility_model.py"
  ]
}
```

## Task

Verify the following chain of quantitative estimates for closed 4-manifolds M = X # k CPbar^2 under negative Ricci pinching ||Ric_g + g||_op <= delta < 1/(1+sqrt(3)).

CLAIM 1 (Theorem A): Using LeBrun 1996 (scalar curvature SW bound int s^2 >= 32pi^2 A where A=c_1^2(X)), the CGB + signature combination 4pi^2 k <= 4pi^2 A - E_s + E_R with E_R/E_s <= 3delta^2/(1-delta)^2, and E_s >= 4pi^2 A/3 from SW, one gets k/A <= 2/3 + delta^2/(1-delta)^2.

CLAIM 2 (Theorem A'): Using LeBrun 1998 Theorem A (the Weyl estimate 2 int|W+|^2 + int s^2/24 > (32/57)*4pi^2 A for any metric on M with nonvanishing SW invariant), combined with the CGB+signature identity 2 int|W+|^2 + int s^2/24 - int|Ric_0|^2/2 = 4pi^2(A-k), the LeBrun bound becomes int|Ric_0|^2/2 > 4pi^2(k - 25A/57). For k = 25A/57 exactly, this reduces to int|Ric_0|^2/2 > 0, giving NO pinching constraint.

CLAIM 3: For k/A slightly above 25/57, the leading-order pinching gap is delta^2 > (k/A - 25/57)/(3(1-k/A)). For k integer, k/A-25/57 >= 1/(57A), giving delta > C/sqrt(A) -> 0 as A -> infinity.

CLAIM 4: M = X_19 # 1875 CPbar^2 (degree-19 smooth hypersurface in CP^3, A = 19*15^2 = 4275, k = 25*4275/57 = 1875) satisfies: (a) LeBrun 1998 excludes all Einstein metrics, (b) 2chi-3|tau| = 2400 > 0, (c) k/A = 25/57 exactly, so no Chern-Weil/SW obstruction to tight pinching.

CLAIM 5: The positive branch is consistent with Q_4 true: tight positive pinching (Ric approx +g) forces s>0, killing SW invariant, finite pi_1 (Myers), and 2chi>3|tau| (strengthened HT). All known no-Einstein 4-manifolds have obstructions that are eliminated by these conditions.

For each claim, check the algebra, identify any gaps, and assess whether the chain from SW bound through CGB through pointwise ratio to the final k/A bound is rigorous.

## Output

# Scientific verification memo

Let
\[
E_s=\int_M\frac{s^2}{24}\,d\mu,\qquad
E_R=\int_M\frac{|\operatorname{Ric}_0|^2}{2}\,d\mu,\qquad
I_+=\int_M|W^+|^2\,d\mu.
\]
Use the complex orientation on \(X\) and its blowups.

## 1. Scalar SW estimate and the \(2/3\) bound

For \(M=X\#k\overline{\mathbb{CP}}^2\),
\[
(2\chi+3\tau)(M)=A-k.
\]
The clean Chern–Gauss–Bonnet/signature identity is
\[
4\pi^2(A-k)=2I_++E_s-E_R. \tag{1}
\]
Consequently,
\[
4\pi^2k
=4\pi^2A-2I_+-E_s+E_R
\le 4\pi^2A-E_s+E_R. \tag{2}
\]
This avoids the note’s use of
\(\int|W|^2\ge12\pi^2|\tau|\), which introduced the extra assumption \(k>\tau(X)\). Equation (1) proves (2) for every \(k\).

Write the Ricci eigenvalues as \(-1+\varepsilon_i\), \(|\varepsilon_i|\le\delta\). Then
\[
|s|\ge4(1-\delta)
\]
and
\[
|\operatorname{Ric}_0|^2
=\sum_i(\varepsilon_i-\bar\varepsilon)^2
=\sum_i\varepsilon_i^2-4\bar\varepsilon^2
\le4\delta^2.
\]
Hence
\[
\frac{|\operatorname{Ric}_0|^2}{s^2}
\le \frac{\delta^2}{4(1-\delta)^2},
\qquad
E_R\le c_\delta E_s,\qquad
c_\delta=\frac{3\delta^2}{(1-\delta)^2}. \tag{3}
\]
The threshold
\[
c_\delta<1
\quad\Longleftrightarrow\quad
\delta<\frac1{1+\sqrt3}
=\frac{\sqrt3-1}{2}
\]
is correct.

Assuming the stated SW estimate
\[
\int_M s^2\,d\mu\ge32\pi^2A,
\]
one has
\[
E_s\ge\frac{4\pi^2A}{3}.
\]
Equations (2)–(3) therefore give
\[
\begin{aligned}
4\pi^2k
&\le4\pi^2A-(1-c_\delta)E_s\\
&\le4\pi^2A-\frac{4\pi^2A}{3}(1-c_\delta),
\end{aligned}
\]
and thus
\[
\boxed{\frac{k}{A}\le
\frac23+\frac{\delta^2}{(1-\delta)^2}}. \tag{4}
\]
The algebra is fully correct.

### Geometric premise needing a more precise presentation

On the blowup, the relevant classes are generally
\[
K_X\pm E_1\pm\cdots\pm E_k,
\]
rather than the pullback of \(K_X\) alone. For \(b^+>1\), the blowup formula and a sign-selection argument produce a class \(a\) with
\[
(a_g^+)^2\ge A,
\]
after which the standard estimate
\(\int s^2\ge32\pi^2(a_g^+)^2\) yields the displayed bound. For \(b^+=1\), chamber data must be included explicitly in the theorem statement. The sentence that nonvanishing follows “when \(s\le0\)” is not the right mechanism: the smooth invariant or monopole-class input comes first and is not created by the sign of \(s\).

Thus the chain after the global SW estimate is rigorous, but the supplied proof needs the blowup-class argument and the exact \(b^+=1\) hypotheses.

There is also an endpoint correction to the stated corollary. If
\[
\varepsilon=\frac{k}{A}-\frac23,\qquad
\delta_{\min}=\frac{\sqrt\varepsilon}{1+\sqrt\varepsilon},
\]
equation (4) excludes \(\delta<\delta_{\min}\), not automatically
\(\delta=\delta_{\min}\). The supplied inequalities permit equality.

The SymPy script correctly verifies the algebraic simplification in (4), but it hardcodes the geometric identities and SW input rather than verifying their hypotheses.

## 2. The 1998 Weyl estimate

Let
\[
L=2I_++E_s.
\]
Accepting the stated LeBrun 1998 estimate,
\[
L>\frac{32}{57}\,4\pi^2A,
\]
equation (1) gives
\[
E_R=L-4\pi^2(A-k)
>4\pi^2\left(k-\frac{25}{57}A\right). \tag{5}
\]
The coefficient \(25/57\) and the strict inequality are correct.

At
\[
k=\frac{25}{57}A,
\]
equation (5) reduces to \(E_R>0\). This excludes \(\delta=0\), because an Einstein metric has \(E_R=0\), but it supplies no fixed lower value of \(\delta\): every \(\delta>0\) remains algebraically compatible with this 1998 estimate alone. This does not produce metrics with \(\delta\to0\); it only says that (5) by itself does not prohibit such a sequence.

As in the scalar estimate, “a metric with nonvanishing SW invariant” should be replaced by the appropriate smooth basic-class or monopole-class hypothesis and the metric-dependent selection of \(a_g^+\).

## 3. Exact pinching gap above \(25/57\)

Set
\[
\lambda=\frac{k}{A},\qquad q=\frac{25}{57},\qquad
c_\delta=\frac{3\delta^2}{(1-\delta)^2}.
\]
Assume \(q<\lambda<1\). From (1) and \(I_+\ge0\),
\[
E_s\le4\pi^2A(1-\lambda)+E_R.
\]
Combining this with \(E_R\le c_\delta E_s\) gives
\[
E_R\le
\frac{c_\delta}{1-c_\delta}\,4\pi^2A(1-\lambda).
\]
Together with (5),
\[
\lambda-q
<
\frac{c_\delta}{1-c_\delta}(1-\lambda).
\]
This simplifies exactly to
\[
c_\delta>\frac{\lambda-q}{1-q}. \tag{6}
\]
Therefore, writing
\[
r=\sqrt{\frac{\lambda-q}{3(1-q)}}
=\sqrt{\frac{57\lambda-25}{96}},
\]
one obtains the exact condition
\[
\boxed{\delta>\frac{r}{1+r}}. \tag{7}
\]

For \(\eta=\lambda-q\to0\),
\[
\delta^2\sim\frac{\eta}{3(1-q)}.
\]
The expression
\[
\delta^2>\frac{\eta}{3(1-\lambda)}
\]
in the script is asymptotically equivalent under the joint scaling
\(\eta=O(\delta^2)\), but it is not the clean exact formula. Equation (7) is preferable.

If \(57k-25A\ge1\), then
\[
r^2=\frac{57k-25A}{96A}\ge\frac1{96A},
\]
so the exact arithmetic consequence is
\[
\boxed{\delta>\frac1{\sqrt{96A}+1}}
\sim\frac1{\sqrt{96A}}.
\]
Thus the \(A^{-1/2}\) behavior is correct, and the gap tends to zero as \(A\to\infty\). At \(57k=25A\), equation (7) reduces to \(\delta>0\), in agreement with the strict \(E_R>0\) statement.

## 4. The degree-19 model and the later LeBrun estimate

For a smooth degree-\(19\) hypersurface,
\[
A=c_1^2=19(19-4)^2=4275,
\]
and
\[
\chi(X)=c_2(X)=19(19^2-4\cdot19+6)=5529.
\]
Therefore
\[
\tau(X)=\frac{A-2\chi(X)}3=-2261.
\]
Since \(4275/57=75\),
\[
k=\frac{25A}{57}=1875.
\]
After the blowups,
\[
\chi(M)=7404,\qquad \tau(M)=-4136,
\]
and hence
\[
2\chi(M)-3|\tau(M)|
=14808-12408
=2400.
\]
Also \(A-k=2400\). These computations are correct.

The strict 1998 estimate excludes every Einstein metric at equality:
an Einstein metric would have \(E_R=0\) and therefore
\[
L=4\pi^2(A-k)
=\frac{32}{57}\,4\pi^2A,
\]
contradicting the strict \(1998\) inequality.

However, the broader sentence that no Chern–Weil/SW estimate yields a fixed pinching gap is not correct once the later LeBrun monopole-class estimate is included. LeBrun’s published estimate in *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, Invent. Math. 145 (2001), 279–316, is commonly stated in the form
\[
\frac1{4\pi^2}
\int_M\left(2|W^+|^2+\frac{s^2}{24}\right)d\mu
\ge\frac23(a_g^+)^2. \tag{8}
\]
For the blowup classes
\[
a_\epsilon=K_X+\sum_i\epsilon_iE_i,
\]
sign averaging gives
\[
2^{-k}\sum_\epsilon(a_\epsilon^+)^2
=(K_X^+)^2+\sum_i(E_i^+)^2
\ge K_X^2=A.
\]
Thus some \(a_\epsilon\) satisfies \((a_\epsilon^+)^2\ge A\), and (8) yields
\[
L\ge\frac23\,4\pi^2A. \tag{9}
\]
Combining (9), (1), and (3) gives the stronger quantitative estimate
\[
\boxed{\frac{k}{A}\le
\frac13+\frac{2\delta^2}{(1-\delta)^2}}. \tag{10}
\]
For \(k/A=25/57\), equation (10) requires
\[
\frac{\delta^2}{(1-\delta)^2}\ge\frac1{19},
\]
or
\[
\boxed{\delta\ge\frac1{1+\sqrt{19}}\approx0.1866}. \tag{11}
\]
Equivalently, (9) gives
\[
E_R\ge4\pi^2\left(k-\frac A3\right)
=1800\pi^2
\]
for this model. Therefore \(X_{19}\#1875\overline{\mathbb{CP}}^2\) cannot support arbitrarily tight \(\operatorname{Ric}\approx-g\) pinching if (8) is applied. This later estimate materially changes the model analysis in `critical_compatibility_model.py`.

## 5. The \(+g\)-pinching observations

Under
\[
\|\operatorname{Ric}-g\|_{\mathrm{op}}\le\delta<1,
\]
one has
\[
\operatorname{Ric}\ge(1-\delta)g,\qquad
s\ge4(1-\delta)>0.
\]

- Myers’ theorem gives
  \[
  \operatorname{diam}(M)\le
  \pi\sqrt{\frac3{1-\delta}},
  \]
  and the universal cover is compact, so \(\pi_1(M)\) is finite.

- For \(b^+>1\), a positive-scalar-curvature metric forces the ordinary SW invariants to vanish. More invariantly, such a metric is incompatible with a nonzero monopole class. For \(b^+=1\), chamber dependence must be stated rather than saying that all SW invariants simply vanish.

- The correct Chern–Weil formulas are
  \[
  2\chi+3\tau=\frac1{4\pi^2}\int
  \left(2|W^+|^2+\frac{s^2}{24}-\frac{|\operatorname{Ric}_0|^2}{2}\right)d\mu,
  \]
  \[
  2\chi-3\tau=\frac1{4\pi^2}\int
  \left(2|W^-|^2+\frac{s^2}{24}-\frac{|\operatorname{Ric}_0|^2}{2}\right)d\mu.
  \]
  The \(W^\mp\) notation in the TeX note is reversed. The final absolute-sign inequality is nevertheless unchanged:
  \[
  2\chi-3|\tau|
  \ge
  \frac{\operatorname{Vol}(M,g)}{4\pi^2}
  \left[\frac23(1-\delta)^2-2\delta^2\right]>0
  \]
  for \(\delta<1/(1+\sqrt3)\).

These are rigorous necessary consequences. They do not show Einstein existence: finite \(\pi_1\), strict Hitchin–Thorpe, and absence of monopole classes do not classify smooth \(4\)-manifolds or solve the Einstein PDE. Pure Ricci pinching also gives no Weyl bound, injectivity-radius lower bound, or Einstein-flow convergence theorem in the supplied material. The sentence about “all known” no-Einstein manifolds is not supported by an exhaustive theorem or sourced enumeration.

For the original existential formulation, a universal theorem for the \(+g\) interval alone would suffice: one could take
\[
c_4=1-\delta_4,\qquad C_4=1+\delta_4.
\]
Proving both the \(+g\) and \(-g\) versions is stronger than required.

## Bottom line

- The derivation of (4) is algebraically correct once the global SW scalar estimate is properly justified; the signature step in the note should be replaced by (1).
- The \(32/57\to25/57\) arithmetic is correct, and equality supplies no fixed \(\delta>0\) floor from the 1998 estimate alone.
- The exact arithmetic gap is (7), with the integer consequence \(\delta>1/(\sqrt{96A}+1)\).
- The degree-19 topology and the 1998 no-Einstein conclusion are correct.
- The proposed degree-19 tight-pinching model is ruled out by the later \(2/3\) monopole-class curvature estimate, which yields the explicit gap \(\delta\ge1/(1+\sqrt{19})\).
- The \(+g\) consequences are necessary topology and curvature facts, not yet an Einstein-existence argument.
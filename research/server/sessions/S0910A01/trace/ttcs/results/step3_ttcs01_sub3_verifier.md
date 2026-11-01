# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step3_mixed_bound_analysis.md",
    "Sessions/S0910A01/workspace/scripts/mixed_sw_bound_analysis.py",
    "Knowledge/objects/papers/Spin-Manifolds-Einstein-Metrics-and-Differential-Topology--1a2235341441--f19aa00d70c8/object.md"
  ]
}
```

## Task

Verify the following argument for a uniform Ricci-pinching lower bound on LeBrun manifolds using the mixed Seiberg-Witten estimate. The claim is: for M = X#k CP̄² (X a minimal surface of general type, A = c₁²(X)), any metric g with δ_-(g) = δ (Ricci eigenvalues in (-(1+δ), -(1+δ))) satisfies δ/(1-δ) ≥ √((k/A - 1/3)/2) whenever k > A/3. The argument uses: (1) Proposition 4 from Ishida-LeBrun with the sign-trick optimization giving (a⁺)² ≥ A; (2) CGB formula giving ∫|r̊|²/2 ≥ 4π²(k-A/3); (3) pointwise bound |r̊|² ≤ 4δ²; (4) volume upper bound from CGB V ≤ 4π²(A-k)/(2(1-δ)²/3 - 2δ²). Check each step, especially: (a) Is the sign trick valid for a single factor X (not just X#Y as in the Ishida-LeBrun proof)? (b) Is the pointwise bound |r̊|² ≤ 4δ² correct (given |Ric - σg|_op ≤ δ)? (c) Does the volume bound follow correctly from CGB? (d) Is the final inequality tight? (e) Does the argument correctly imply that the no-Einstein range extends from k > 2A/3 (scalar-only) to k > A/3 (mixed)?

## Output

# 科学复核备忘

## 总结

四个主要计算中：

1. 单因子上的符号选择在代数上完全成立；其 Seiberg–Witten 前提在 \(b_+(X)\ge2\) 时可由 Taubes 定理与 blow-up 公式得到。
2. \(|\mathring r|^2\le4\delta^2\) 正确，常数 \(4\) 也是该独立点态估计的最佳常数。
3. 所写体积上界只有在
   \[
   D_0(\delta):=\frac23(1-\delta)^2-2\delta^2>0
   \quad\Longleftrightarrow\quad
   \delta<\delta_*:=\frac1{1+\sqrt3}
   \]
   时才能除以分母。
4. 由这套推导可严格得到
   \[
   \frac{\delta}{1-\delta}\ge
   \sqrt{\frac{k/A-1/3}{2}}
   \]
   的区间是
   \[
   \frac A3<k\le A,\qquad 0\le\delta<1,
   \]
   前提是所需 monopole classes 对每个度量都可用。对 \(k>A\)，现有体积论证只给出 \(\delta\ge\delta_*\)，不能推出所述随 \(k/A\) 增长的公式。
5. Einstein 非存在结论本身确实从 \(k>2A/3\) 改进到 \(k>A/3\)，而且这一步不需要体积估计。
6. 最终常数不是几何上锐利的；脚本中“symbolic boundary is tight”只表示最后的代数式取等。构成该代数式的两个点态取等条件在 \(\delta>0\) 时互不相容。

---

## 1. 单因子 \(X\) 上的符号选择

令
\[
\alpha=c_1(X),\qquad
a_\varepsilon=\alpha+\sum_{j=1}^k\varepsilon_jE_j .
\]
对给定度量 \(g\)，逐个选择符号，使
\[
\widehat E_j\cdot\alpha^+\ge0 .
\]
于是
\[
\begin{aligned}
(a^+)^2
&=\left(\alpha^++\sum_j\widehat E_j^+\right)^2\\
&=(\alpha^+)^2
 +2\sum_j\alpha^+\cdot\widehat E_j^+
 +\left(\sum_j\widehat E_j^+\right)^2\\
&\ge(\alpha^+)^2
\ge\alpha^2=A.
\end{aligned}
\]
最后一个平方非负，是因为 \(H_g^+\) 上的交叉形式正定。这里不需要第二个因子 \(Y\)。

真正需要补充的是：每个 \(a_\varepsilon\) 必须是 monopole class。对 \(b_+(X)\ge2\)，这可由所给文件中的材料组成：

- \(X\#k\overline{\mathbf{CP}}^{\,2}\) 的不同 blow-up 符号给出 Chern 类
  \(\alpha+\sum\varepsilon_jE_j\)；
- Taubes 非消失与 blow-up 公式使这些类成为 Seiberg–Witten basic classes；
- 在 \(b_+\ge2\) 时，非零不变量给出每个度量上的解。

但“任意 minimal surface of general type”还包括 \(p_g=0\)、因而 \(b_+=1\) 的曲面。所给 Ishida–LeBrun 文件的 Definition 1 明确采用 \(b_+\ge2\)。\(b_+=1\) 情形需要另写 chamber continuation；当 \(k<A\) 时
\[
a_\varepsilon^2=A-k>0
\]
对避免 \(a^+=0\) 很有帮助，但这一段不在现有论证中。

---

## 2. 混合估计与 CGB 的组合

记
\[
I_g=\frac1{4\pi^2}\int_M
\left(\frac{s^2}{24}+2|W_+|^2\right)d\mu,
\qquad
J_g=\frac1{4\pi^2}\int_M\frac{|\mathring r|^2}{2}\,d\mu .
\]
混合估计与符号选择给出
\[
I_g\ge\frac23(a^+)^2\ge\frac{2A}{3}.
\]
另一方面，
\[
(2\chi+3\tau)(M)=A-k=I_g-J_g.
\]
所以
\[
J_g=I_g-(A-k)\ge k-\frac A3.
\]
等价地，
\[
\int_M\frac{|\mathring r|^2}{2}\,d\mu
\ge4\pi^2\left(k-\frac A3\right).
\]
这一步的系数正确。

---

## 3. 点态 traceless Ricci 估计

按提问中的算子范数解释，写
\[
\operatorname{Ric}=-g+E,\qquad \|E\|_{\rm op}\le\delta.
\]
若 \(e_1,\dots,e_4\in[-\delta,\delta]\) 是 \(E\) 的特征值，令
\[
\bar e=\frac14\sum_i e_i.
\]
则
\[
\mathring r=E-\bar e\,g
\]
以及
\[
|\mathring r|^2
=\sum_i(e_i-\bar e)^2
=\sum_i e_i^2-4\bar e^2
\le\sum_i e_i^2
\le4\delta^2.
\]
因此
\[
k-\frac A3
\le J_g
\le\frac{\delta^2V}{2\pi^2},
\]
从而
\[
V\ge\frac{2\pi^2(k-A/3)}{\delta^2}.
\]
常数 \(4\) 可由 \((e_i)=(\delta,\delta,-\delta,-\delta)\) 取到。

题文中的特征值区间
\[
\bigl(-(1+\delta),-(1+\delta)\bigr)
\]
是空区间；这里显然应为
\[
[-(1+\delta),-(1-\delta)]
\]
或等价的 \(\|\operatorname{Ric}+g\|_{\rm op}\le\delta\)。

---

## 4. 体积上界及其分母

当 \(0\le\delta<1\) 时，
\[
s=-4+\sum_i e_i\le-4(1-\delta),
\]
所以
\[
\frac{s^2}{24}\ge\frac23(1-\delta)^2.
\]
再由
\[
-\frac{|\mathring r|^2}{2}\ge-2\delta^2,\qquad |W_+|^2\ge0,
\]
CGB 给出
\[
A-k\ge\frac{V}{4\pi^2}
\left[\frac23(1-\delta)^2-2\delta^2\right].
\]
这条不等式始终成立，但只有在
\[
D_0(\delta)=\frac23(1-\delta)^2-2\delta^2>0
\]
时才可写成
\[
V\le\frac{4\pi^2(A-k)}{D_0(\delta)}.
\]
而
\[
D_0(\delta)>0
\iff
\delta<\frac1{1+\sqrt3}.
\]

因此脚本中的无条件体积上界需要改成带有分母正性假设的形式。

---

## 5. 最终不等式

设
\[
q=k-\frac A3,\qquad B=A-k.
\]
在 \(D_0(\delta)>0\) 时，组合上下体积估计：
\[
q\left[\frac23(1-\delta)^2-2\delta^2\right]
\le2B\delta^2.
\]
移项得
\[
\frac23q(1-\delta)^2
\le2(B+q)\delta^2.
\]
因为
\[
B+q=(A-k)+\left(k-\frac A3\right)=\frac{2A}{3},
\]
故
\[
q(1-\delta)^2\le2A\delta^2,
\]
即
\[
\frac{\delta}{1-\delta}
\ge\sqrt{\frac{q}{2A}}
=\sqrt{\frac{k/A-1/3}{2}}.
\]

对 \(1/3<p=k/A\le1\)，若 \(\delta\ge\delta_*\)，则
\[
\frac{\delta}{1-\delta}\ge\frac1{\sqrt3}
\ge\sqrt{\frac{p-1/3}{2}}.
\]
若 \(\delta<\delta_*\)，则使用上述体积组合。因此在
\[
\frac13<p\le1
\]
时结论完整成立。

对 \(p>1\)，右端严格大于 \(1/\sqrt3\)，而 CGB 的分母正性至多迫使
\(\delta\ge\delta_*\)。现有推导不能继续得到所述 \(p\)-依赖公式。

此外，\(\delta/(1-\delta)\) 的写法本身要求 \(\delta<1\)。若希望覆盖全部 \(\delta\ge0\)，应改写成
\[
\delta\ge
\frac{\sqrt{(p-1/3)/2}}
{1+\sqrt{(p-1/3)/2}}.
\]

---

## 6. 最终常数并不锐利

粗估计的两个取等条件彼此冲突：

- \(|\mathring r|^2=4\delta^2\) 要求 \(e_i=\pm\delta\)、迹为零，即两个 \(+\delta\) 与两个 \(-\delta\)；
- \(s^2=16(1-\delta)^2\) 要求 \(\sum e_i=4\delta\)，即四个 \(e_i\) 全为 \(+\delta\)。

所以当 \(\delta>0\) 时，最终等号不可能由这些估计同时实现。脚本中的 SymPy 计算只核实了移项后的代数等价性。

事实上可以直接联合优化 CGB 中的 Ricci 部分。令 \(t=\sum_i e_i\)，则
\[
\frac{s^2}{24}-\frac{|\mathring r|^2}{2}
=
\frac23-\frac t3+\frac{t^2}{6}
-\frac12\sum_i e_i^2.
\]
在立方体 \(e_i\in[-\delta,\delta]\) 上计算得
\[
\min\left(
\frac{s^2}{24}-\frac{|\mathring r|^2}{2}
\right)
=
\begin{cases}
\frac23(1-\delta)^2,
&0\le\delta\le\frac13,\\[1mm]
\frac23(1-\delta-2\delta^2),
&\frac13\le\delta\le1.
\end{cases}
\]
这严格强于所用的 \(D_0(\delta)\)。例如它在 \(\delta<1/2\) 时仍为正，因此 \(k\ge A\) 已迫使 \(\delta\ge1/2\)，强于粗估计的 \(1/(1+\sqrt3)\)。

---

## 7. Einstein 非存在区段

若 \(g\) 是 Einstein，则 \(\mathring r=0\)，故
\[
A-k=I_g\ge\frac{2A}{3}.
\]
于是
\[
k\le\frac A3.
\]
因此
\[
k>\frac A3
\quad\Longrightarrow\quad
M\text{ 不承载 Einstein 度量},
\]
前提仍是上述 monopole class 输入成立。

只使用 scalar-only 估计时，
\[
\frac1{4\pi^2}\int\frac{s^2}{24}\,d\mu\ge\frac A3,
\]
Einstein 条件仅给出
\[
A-k\ge\frac A3,
\qquad k\le\frac{2A}{3}.
\]
所以从 \(2A/3\) 改进到 \(A/3\) 是正确的。不过这些都是单向非存在结果；脚本中写成 “iff” 没有依据，且 \(k=A/3\) 的等号情形不能仅由所引 Proposition 4 排除。

最后，脚本关于旧 scalar-only 定量式的描述彼此不一致。按同一粗体积方法，正确结果是
\[
\frac{\delta}{1-\delta}\ge
\sqrt{\frac{k-2A/3}{A}}
=\sqrt{\frac{k}{A}-\frac23},
\]
因而固定 \(k/A>2/3\) 时本来就与 \(A\) 无关。混合估计真正新增的是：即使 \(k/A\to2/3\)，它仍给出
\[
\delta\ge\frac1{1+\sqrt6},
\]
并把非存在区段推进到 \(k/A>1/3\)。
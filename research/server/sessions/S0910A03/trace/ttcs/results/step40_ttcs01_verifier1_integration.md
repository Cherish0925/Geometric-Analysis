# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 40,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step40_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step40_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the proposed m=2 coupled continuation mechanism in step40_m2_coupled_continuation_mechanism.md for the normalized cutoff flow. Focus on the exact hard residual: V=∇²U, Z=∇³χ, W=∇U, Θ=∇²χ, and I=∫χ Z*W*|V|^{p-2}V. Check whether integrating once more off Z really yields only (i) a signed χΘ*V*P(V) term amenable to the Step 38 Hessian lemma, (ii) a weighted-dissipation term with coefficient ΘW controlled from the m=1 base pair at finite exponents, and (iii) lower products—without hidden current-level Z at 2p or W in L∞. Check tensor/covariant-derivative commutators and whether the Γ1, Γ2, Γ3 coefficients/contractions can be grouped this way rather than merely schematically. Also verify the Z evolution derivative count and same-p closure. Identify precisely any remaining term that invalidates the displayed m=2 Grönwall inequality. Treat the note as a mathematical proposal, not as established.

## Integrated Scientific Memo

# \(m=2\) 耦合机制核验结论

## 结论

Step 40 的核心二次分部积分机制是成立的，但其结论只能表述为一个**以所有所需有限指数范数在整个区间上一致有界为前提的条件性 \(m=2\) 引理**。

对于
\[
V=\nabla^2U,\qquad Z=\nabla^3\chi,\qquad
W=\nabla U,\qquad \Theta=\nabla^2\chi,
\]
硬项
\[
I=\int_M\chi\,Z*W*P(V)\,d\mu,\qquad P(V)=|V|^{p-2}V
\]
再分部积分一次，确实只产生：

1. 可由 Step 38 控制的有符号项 \(\chi\Theta*V*P(V)\)；
2. 含 \(\nabla P(V)\) 的加权耗散项，其系数仅为 \(\Theta W\)；
3. \(d\chi\,\Theta W P(V)\) 型低阶乘积。

它不要求 \(Z\in L^{2p}\)，也不要求 \(W\in L^\infty\)。协变导数换序不会恢复当前层的高阶 \(Z\)，至多产生由 \(T,\nabla T\) 的有限 \(L^q\) 范数控制的低阶曲率项。\(Z\) 的演化最高只含 \(V*d\chi\) 和 \(W*\Theta\)，因此在同一指数 \(p\) 闭合。

在 Step 40 明确假定
\[
\sup_{t<T}\bigl(
\|W\|_{L^q}+\|\Theta\|_{L^q}+\|T\|_{L^q}+\|\nabla T\|_{L^q}
\bigr)<\infty
\]
（所需 \(q\) 至少包括 \(2p,4p\)）时，没有额外项破坏
\[
Y_{2,p}'\le C_p(1+Y_{2,p}),\qquad
Y_{2,p}=\|V\|_p^p+\|Z\|_p^p.
\]

目前真正未完成、并阻止把该结论视为无条件证明的对象，是归一化 shifted-flow 下
\[
\sup_{t<T}\|\nabla T(t)\|_{L^q}<\infty
\]
的独立积分估计。若该输入不可用，\(V\)-方程中的
\[
aW*\nabla T,\qquad \nabla a*U*\nabla T
\]
即为使 displayed Grönwall 不闭合的精确剩余项。

---

## 1. 硬残余的逐收缩计算

固定任意一个由 \(g,g^{-1}\) 构成的平行收缩。保留实际协变导数次序，写
\[
Z_{abc}=\nabla_a\Theta_{bc}.
\]
对应项可表示为
\[
I_{\mathcal C}
=\int_M\chi(\nabla_a\Theta_{bc})
   \,\mathcal C^{abc}(W,P(V))\,d\mu .
\]
由于 \(\nabla g=\nabla g^{-1}=0\)，分部积分不会对收缩系数产生导数：
\[
\begin{aligned}
I_{\mathcal C}
={}&-\int (\nabla_a\chi)\Theta_{bc}\,
       \mathcal C^{abc}(W,P(V))\\
&-\int \chi\Theta_{bc}\,
       \mathcal C^{abc}(\nabla_aW,P(V))\\
&-\int \chi\Theta_{bc}\,
       \mathcal C^{abc}(W,\nabla_aP(V)).
\end{aligned}
\tag{1}
\]

### 1.1 导数落在 \(W\)

若 \(V\) 按相同迭代次序定义，则 \(\nabla W=V\)；因此第二项逐收缩具有
\[
J=\int_M\chi\,\Theta_{bc}B^{bc}(V)\,d\mu,
\]
且
\[
|B(V)|\le C_p|V|^p,\qquad
|\nabla B(V)|\le C_p|V|^{p-1}|\nabla V|.
\]
即使 \(B^{bc}\) 不对称也无妨，因为对称的 \(\Theta_{bc}\) 仅看到其对称部分。Step 38 的 Hessian 引理严格给出
\[
|J|
\le \varepsilon D_{2,p}
 +C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p,
\qquad
D_{2,p}=\int\chi^2|\nabla V|^2|V|^{p-2}.
\tag{2}
\]

若为了统一指标次序而交换 \(\nabla_a\nabla_bU\)，则产生
\[
[\nabla_a,\nabla_b]U=\operatorname{Rm}*U=(T-G)*U.
\]
对应积分至多为
\[
C\int |\Theta|\,|T|\,|U|\,|V|^{p-1},
\]
由 \(\|U\|_\infty\)、\(\Theta,T\in L^{2p}\) 控制；它不是新的当前层高阶项。

### 1.2 导数落在 \(P(V)\)

正则化 \(P\) 后再令正则参数趋零，可使用
\[
|\nabla P(V)|\le C_p|V|^{p-2}|\nabla V|.
\]
于是
\[
\begin{aligned}
\int\chi|\Theta||W||V|^{p-2}|\nabla V|
&\le \varepsilon D_{2,p}
 +C_{p,\varepsilon}
   \int|\Theta|^2|W|^2|V|^{p-2}.
\end{aligned}
\tag{3}
\]
有限体积 Hölder 给出
\[
\int|\Theta|^2|W|^2|V|^{p-2}
\le
\operatorname{Vol}(M,g(t))^{1/p}
\|\Theta\|_{4p}^2\|W\|_{4p}^2\|V\|_p^{p-2}.
\tag{4}
\]
倒数指数为
\[
\frac1{2p}+\frac1{2p}+\frac{p-2}{p}+\frac1p=1.
\]
故
\[
(3)\le \varepsilon D_{2,p}
+C_{p,W,\Theta}(1+\|V\|_p^p).
\tag{5}
\]
这一步与维数无关；Step 40 中提到“四维”并非必要条件。

### 1.3 导数落在显式 \(\chi\)

\[
\begin{aligned}
\int |d\chi|\,|\Theta|\,|W|\,|V|^{p-1}
&\le \|d\chi\|_\infty
   \|\Theta\|_{2p}\|W\|_{2p}\|V\|_p^{p-1}\\
&\le C_p(1+\|V\|_p^p).
\end{aligned}
\tag{6}
\]

综上，对每个实际张量收缩分别有
\[
|I_{\mathcal C}|
\le \varepsilon D_{2,p}+C_p(1+\|V\|_p^p).
\tag{7}
\]
此结论不依赖 \(\Gamma_1,\Gamma_2,\Gamma_3\) 之间的数值系数或抵消，因此 Step 40 所说“精确系数不重要”在这个局部估计意义下是正确的。

---

## 2. 高 cutoff 项的完整清单

由
\[
\nabla^\alpha\chi*\nabla^\beta\chi*\nabla^\gamma U,
\qquad
\alpha+\beta+\gamma=4,\quad \gamma\le3,
\]
在 \(m=2\) 时除交换两个 cutoff 因子的重复项外，实际类型为
\[
\begin{gathered}
\chi\nabla^4\chi*U,\qquad
d\chi*Z*U,\qquad
\chi Z*W,\\
\Theta*\Theta*U,\qquad
d\chi*\Theta*W,\qquad
\chi\Theta*V,\\
d\chi*d\chi*V,\qquad
\chi d\chi*\nabla V.
\end{gathered}
\tag{8}
\]

因此 Step 40 的 (3.9) 在文字上并未列尽“所有 high-cutoff terms”：它显式估计的 \(\Gamma_1,\dots,\Gamma_4\) 只是四个 top-jet 类型。不过遗漏的四类均可控制：

- \(\chi\Theta*V\) 测试后是 Step 38 的 signed Hessian 项；
- \(\Theta*\Theta*U\) 由
  \[
  K\|\Theta\|_{2p}^2\|V\|_p^{p-1}
  \]
  控制；
- \(d\chi*\Theta*W\) 由 \(\Theta,W\in L^{2p}\) 控制；
- \(d\chi*d\chi*V\) 线性贡献 \(C\|V\|_p^p\)。

故这是陈述归类不完整，而不是分析障碍。把这些项补入后，完整高-cutoff 行满足
\[
\left|\int P(V)*\mathcal H_2\right|
\le \varepsilon D_{2,p}
+C_p\bigl(1+\|V\|_p^p+\|Z\|_p^p\bigr).
\tag{9}
\]

特别地，对
\[
\Gamma_1=\chi\nabla^4\chi*U=\chi\nabla Z*U
\]
逐收缩分部积分严格产生
\[
\chi ZU*\nabla P(V),\qquad
d\chi ZU*P(V),\qquad
\chi ZW*P(V).
\tag{10}
\]
前两项分别由
\[
\varepsilon D_{2,p}
+CK^2\int |Z|^2|V|^{p-2}
\]
及
\[
CK\int |Z||V|^{p-1}
\]
控制，因而只要求 \(Z\in L^p\)。第三项正是上节处理的硬残余。

---

## 3. 协变换序不会产生隐藏的当前层高阶量

二次分部积分本身不需要换序，因此无内生 commutator。若为了匹配张量槽位而换序：

\[
[\nabla_i,\nabla_j]d\chi=\operatorname{Rm}*d\chi,
\]
四阶换序还可能产生
\[
\operatorname{Rm}*\Theta,\qquad
\nabla\operatorname{Rm}*d\chi.
\]
由于
\[
\operatorname{Rm}=T-G,\qquad \nabla\operatorname{Rm}=\nabla T,
\]
这些分别由 \(T,\nabla T\) 的有限 \(L^q\) 范数控制。典型测试项为
\[
|T|\,|\Theta|\,|U|\,|V|^{p-1},
\qquad
|\nabla T|\,|d\chi|\,|U|\,|V|^{p-1}.
\tag{11}
\]
它们不要求 \(Z\in L^{2p}\)、\(W\in L^\infty\) 或 \(\nabla^2T\)。

---

## 4. \(Z\) 演化的精确导数计数

令
\[
C^k{}_{ij}=\partial_t\Gamma^k{}_{ij}.
\]
因 \(\chi\) 在时间上固定，
\[
\partial_t\Theta_{ij}=-C^k{}_{ij}\nabla_k\chi.
\]
对
\[
Z_{\ell ij}=\nabla_\ell\Theta_{ij}
\]
直接求导：
\[
\begin{aligned}
\partial_tZ_{\ell ij}
={}&-(\nabla_\ell C^k{}_{ij})\nabla_k\chi
-C^k{}_{ij}\Theta_{\ell k}\\
&-C^k{}_{\ell i}\Theta_{kj}
-C^k{}_{\ell j}\Theta_{ik}.
\end{aligned}
\tag{12}
\]
由
\[
\partial_tg=-2\operatorname{Ric}(U)
\]
及标准连接变分，
\[
C=g^{-1}*\nabla\operatorname{Ric}(U),\qquad
|C|\le C|W|,\qquad |\nabla C|\le C|V|.
\tag{13}
\]
这里 \(\operatorname{Ric}\) 对 \(U\) 是代数收缩；\(\nabla g=0\)，故不存在额外 \(\nabla T\) 或 \(\nabla^3U\)。于是
\[
|\partial_tZ|
\le C\bigl(|V||d\chi|+|W||\Theta|\bigr).
\tag{14}
\]
张量范数与体积形式的时间变化由 \(|U|\le K\) 控制，故
\[
\begin{aligned}
\frac d{dt}\|Z\|_p^p
\le{}&
C_pK\|Z\|_p^p+
C_p\|d\chi\|_\infty\|V\|_p\|Z\|_p^{p-1}\\
&+
C_p\|W\|_{2p}\|\Theta\|_{2p}\|Z\|_p^{p-1}.
\end{aligned}
\]
Young 不等式给出
\[
\frac d{dt}\|Z\|_p^p
\le C_p\bigl(1+\|V\|_p^p+\|Z\|_p^p\bigr).
\tag{15}
\]
所以 \(Z\)-方程确实在同一 \(p\) 闭合。

---

## 5. \(V\)-方程的精确条件性缺口

除高-cutoff 行外，\(m=2\) 方程含
\[
\nabla^ia*\nabla^jU*\nabla^kT,
\qquad i+j+k=2,\quad k\le1.
\]
含最高允许的未加权曲率导数 \(k=1\) 的项包括
\[
aW*\nabla T,\qquad
\nabla a*U*\nabla T.
\tag{16}
\]
测试后产生
\[
\int a|\nabla T||W||V|^{p-1},
\qquad
\int |\nabla a||U||\nabla T||V|^{p-1}.
\tag{17}
\]
若
\[
\sup_{t<T}\|\nabla T(t)\|_{2p}<\infty,
\]
则它们由 Hölder–Young 控制为 \(C(1+\|V\|_p^p)\)。没有 \(\nabla^2T\) 出现；含 \(T*V\) 的潜在最高项带有 \(a\)，因 \(aT=U\) 而成为有界系数 \(U*V\)。

因此，在所声明的先验输入下，
\[
\frac d{dt}\|V\|_p^p+cD_{2,p}
\le C_p\bigl(1+\|V\|_p^p+\|Z\|_p^p\bigr).
\tag{18}
\]
与 (15) 相加即得
\[
Y_{2,p}'\le C_p(1+Y_{2,p}).
\tag{19}
\]

但现有材料没有完整证明归一化方程下的 \(\nabla T\) 一致 \(L^q\) 估计。Wang Proposition 4.13 支持相应结构，却不能替代对 shifted normalized equation 的推导。因此：

- 若把 \(\nabla T\in L^q\) 视为已知输入，Step 40 的 \(m=2\) Grönwall 成立；
- 若只假设 \(\sup|U|\) 以及 \(m=1\) 基础对 \(W,\Theta\) 的估计，则 (17) 是尚未控制的精确项，(18) 尚未证明。

该缺口原则上可用 \(\nabla T\)-方程自身的 signed integration-by-parts 处理：其 top-cutoff 项 \(\chi Z*T\) 分部积分后产生 \(d\chi\,\Theta T\)、\(\chi\Theta\nabla T\) 和 \(\chi\Theta T\nabla P(\nabla T)\)，看起来只需 \(T,\Theta\) 的有限指数范数及该方程自身的耗散。但这套归一化方程及所有反应、commutator 项尚需完整展开，不能在本次核验中视为已经建立。

**最终判定：**硬残余修复本身有效；同指数 \(m=2\) 耦合闭合在假设 (1.1) 下有效；当前唯一实质性未闭合对象是归一化 shifted-flow 的未加权 \(\nabla T\) 有限指数估计，而非隐藏的 \(Z\in L^{2p}\)、\(W\in L^\infty\) 或错误的 \(Z\)-演化导数计数。
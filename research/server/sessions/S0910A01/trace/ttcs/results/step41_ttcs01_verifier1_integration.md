# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 41,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step41_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step41_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the corrected restricted negative defect gap theorem note (step41_corrected_restricted_defect_gap_theorem.md), focusing on §3 (zero-order unweighted T∈L^p lemma) and §4 (structural equations for the staggered induction). Verify:

1. §3 ZERO-ORDER T LEMMA: Under |U|=|aT|≤K, does the reaction bound a|T|^{p+1} ≤ K|T|^p actually follow? Is the G-evolution term |∂_tG| ≤ Ca|T| correct given ∂_tG = -2a(E⊛g)/(n-1) and E=Ric(T)? Does the Hessian-cutoff signed IBP actually remove the ∇²χ dependence? Is the additive C'_p term genuinely harmless for the continuation application (which only needs finiteness, not multiplicative Gronwall)? Are there missing terms?

2. §4 STRUCTURAL EQUATIONS: Is it true that ∇G=0 because ∇g=0? Does ∇^jT = ∇^jRm for j≥1 follow? In the expansion of ∇^{r+1}a = Σ C_s·C_t (s+t=r+1), is it correct that only the s=0 and t=0 terms use C_{r+1}? Does the cutoff-jet evolution ∂_t C_m (equation 4.6) genuinely avoid C_m and U_m in its RHS? Does ∂_tΓ = g^{-1}*∇Ric(U) introduce at most one derivative of U? Are the dangerous terms (4.12) correctly identified?

3. INTERACTION WITH A03 INDUCTION: Does the structural analysis genuinely show that A03's staggered ordering T_0→(U_1,C_2)→T_1→... has no upward dependencies? Are there additional terms from the Kulkarni-Nomizu product, commutators, or normalization that could defeat the induction?

Provide a direct scientific memo identifying any errors, missing terms, or gaps.

## Integrated Scientific Memo

# 科学核验备忘录

## 总结判断

§3 的零阶无权 \(T\in L^p\) 估计在核心机制上成立，但当前证明遗漏了张量范数随 \(g(t)\) 变化产生的项，并且 Hessian-\(a\) 部分应显式写出适用于 \(T\)-能量的收缩张量；这些遗漏是可吸收的，不破坏结论。

§4 中
\[
\nabla G=0,\qquad \nabla^jT=\nabla^j\Rm\quad(j\ge1)
\]
及 cutoff-jet 方程的三角依赖是正确的。不过：

1. (4.3) 的 \(\partial_t\Gamma\) 公式符号及系数错误；
2. 从 \(\partial_tU=a\,\partial_tT\) 推导主部时漏写了一个 \(a\)；
3. (4.12) 没列出关键的 \(\chi C_{m+1}U_1\) 项；
4. 顶阶 cutoff 项的 \(\chi\)-权重需要从精确方程重新核对，不能直接把它写成 \(\chi C_{m+2}U_0\)。

修正后，没有发现 Kulkarni–Nomizu、交换子或归一化项导致高于当前层的未知量；A03 的 staggered ordering 在导数依赖意义上仍然可行。但 Step 41 §4 目前只是结构性/示意性验证，不是完整的任意阶演化与能量证明。

---

## 1. §3：零阶无权 \(T\in L^p\) 引理

### 1.1 反应项估计正确

由于 \(a=\chi^2\ge0\)，
\[
|U|=|aT|=a|T|.
\]
因此
\[
a|T|^{p+1}=|U|\,|T|^p\le K|T|^p,
\]
以及
\[
a|T|^{p-1}=|U|\,|T|^{p-2}\le K|T|^{p-2}.
\]
所以 Hamilton 二次反应项在假设 \(\|U\|_\infty\le K\) 下确实降为对无权 \(L^p\) 能量线性的项。这里必须保留二次曲率项前面的 \(a\)；若丢失该权重，论证不能闭合。

### 1.2 \(G\) 的演化及大小估计正确

由
\[
G=\frac{g\owedge g}{2(n-1)},\qquad \partial_tg=-2aE
\]
以及 Kulkarni–Nomizu 积的对称性，
\[
\partial_tG
=\frac{\partial_tg\owedge g+g\owedge\partial_tg}{2(n-1)}
=-\frac{2a}{n-1}(E\owedge g).
\]
又因 \(E=\Ric(T)\)，
\[
|\partial_tG|
\le C_n a|E|
\le C_n a|T|
=C_n|U|
\le C_nK.
\]
故与 \(|T|^{p-2}T\) 配对后得到
\[
CK\int |T|^{p-1},
\]
可由 Young 不等式控制为 \(C(K)\int|T|^p+C(K)\Vol\)。

### 1.3 Hessian-cutoff 的 IBP 机制成立，但当前写法不完整

\(T\)-能量中的 Hessian 项具有结构
\[
I_H
=p\int (\nabla_i\nabla_j a)\,
|T|^{p-2}\,\mathcal B^{ij}(T,E)\,d\mu,
\]
其中
\[
|\mathcal B(T,E)|\le C|T||E|\le C|T|^2,
\]
并且因为 \(\nabla E\) 是 \(\nabla T\) 的迹收缩且 \(\nabla G=0\)，
\[
|\nabla\mathcal B|
\le C\bigl(|E||\nabla T|+|T||\nabla E|\bigr)
\le C|T||\nabla T|.
\]
在闭流形上对 \(\nabla^2a\) 积分一次：
\[
I_H
=-p\int \nabla a\cdot
\nabla\!\left(|T|^{p-2}\mathcal B(T,E)\right)d\mu.
\]
于是
\[
|I_H|
\le \varepsilon\int a|T|^{p-2}|\nabla T|^2
+C_{p,\varepsilon}\int\frac{|\nabla a|^2}{a}|T|^p.
\]
对 \(a=\chi^2\)，
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le Cr^{-2}
\]
（在 \(a=0\) 处按零延拓）。因此确实不需要任何点态 \(\nabla^2\chi\) 控制。

但 §3 不应直接笼统引用 Step 35 的 \(B_{\rm curv}\)、\(B_{\rm def}\)：那些张量来自不同的测试量。应显式给出上述适用于 \(T\)-能量的 \(T*E\) 收缩结构。

另外，§3 中“导数击中 \(\eta=1\)、借助 collar 消失”的叙述是从带权证明误植而来。此处没有 \(\eta\)；边界项消失是因为 \(M\) 闭合。

### 1.4 漏项：张量范数的逆度量变化

仅测试 \(\partial_tT\) 并不足以得到 \(\partial_t|T|^p\)。由于 \(T\) 是四阶协变张量，
\[
\partial_t|T|^p
=p|T|^{p-2}\langle \partial_tT,T\rangle
+O\!\left(p\,a|E|\,|T|^p\right).
\]
这里
\[
a|E|\le C|\Ric(aT)|\le C|U|\le CK,
\]
故漏掉的项满足
\[
\left|\int O(p\,a|E|\,|T|^p)\right|
\le C_pK\int |T|^p.
\]
它不破坏 (3.1)，但完整证明必须列出。

体积项也可更直接地写成
\[
|a\tr E|\le C|aE|\le CK.
\]
若引理声称适用于一般 \(n\)，则 \(\tr E=s+n\)，不是 \(s+4\)。

### 1.5 加性常数对 continuation 确实无害

只要将常数明确为不依赖待证明的高阶曲率，例如
\[
C_{n,p}(1+K^{\alpha_p})
\sup_{t\in[\tau,T_*)}\Vol(M,g(t)),
\]
则它在有限时间 slab 上有统一上界。因为
\[
|\partial_tg|=2|\Ric(U)|\le C_nK,
\]
得到双 Lipschitz 比较及体积控制。由 \(\tau>0\) 时解光滑，
\(\|T(\tau)\|_p<\infty\)，带加性源项的 Gronwall 足以给出
\[
\sup_{\tau\le t<T_*}\|T(t)\|_p<\infty.
\]
continuation 只需要有限性，并不需要纯乘法型估计。

“bounded metric data”应删除或具体化，不能让常数依赖尚未获得的曲率导数。

### 1.6 非必要但有误导性的段落

“\(E=0\) 时 \(T\) 平行且曲率为空间形式”的暗示不正确。一般满足
\(\Ric=-g\) 的 Einstein 度量不必局部常曲率，\(T\) 也不必平行。静止性来自完整曲率椭圆恒等式中扩散、二次项和归一化项的抵消，而不是该段给出的空间形式论证。此段与能量估计无关，宜删除。

---

## 2. §4：结构方程

### 2.1 \(G\) 的空间平行性正确

在每个固定时间，
\[
\nabla g=0
\quad\Longrightarrow\quad
\nabla G=\frac{\nabla(g\owedge g)}{2(n-1)}=0,
\qquad \Delta G=0.
\]
因此
\[
\nabla^jT=\nabla^j\Rm,\qquad j\ge1.
\]

需要区分空间与时间陈述：
\[
0=\partial_t(\nabla^jG)
=[\partial_t,\nabla^j]G+\nabla^j(\partial_tG).
\]
所以不能单独丢弃 \(\nabla^j(\partial_tG)\)；它与时间连接交换子共同抵消为 \(\partial_t(\nabla^jG)=0\)。导数计数上，\(\partial_tG\) 至多带来当前阶 \(U_j\)，不会产生 \(U_{j+1}\)。

### 2.2 \(\nabla^{r+1}a\) 的顶阶 cutoff 分类正确

\[
\nabla^{r+1}a
=\sum_{s+t=r+1}\binom{r+1}{s}C_s*C_t.
\]
只有
\[
(s,t)=(0,r+1),\qquad (r+1,0)
\]
含 \(C_{r+1}\)，二者合并为
\[
2\chi C_{r+1}.
\]
其余各项的 cutoff 阶数均不超过 \(r\)。

### 2.3 (4.3) 的连接变化公式符号/系数错误

令 \(S=\Ric(U)\)，则 \(\partial_tg=-2S\)。标准公式给出
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}
\left(
\nabla_iS_{j\ell}
+\nabla_jS_{i\ell}
-\nabla_\ell S_{ij}
\right).
\]
Step 41 的 (4.3) 写成正号且末项带 \(1/2\)，与 \(\partial_tg=-2S\) 不一致。

不过其导数阶结论仍正确：
\[
\partial_t\Gamma=g^{-1}*\nabla\Ric(U),
\]
而 \(\Ric(U)\) 是 \(U\) 的代数迹收缩，所以原始连接变化恰含一阶 \(U\)。

### 2.4 cutoff-jet 方程的三角性正确

对有序协变导数 \(C_m=\nabla^m\chi\)，
\[
\partial_tC_m
=\sum_{\ell=0}^{m-2}
\nabla^\ell(\partial_t\Gamma)*C_{m-1-\ell},
\]
差异仅在符号和组合系数。最高阶项为
\[
\nabla^{m-2}(\partial_t\Gamma)*C_1
=U_{m-1}*C_1+\text{较低阶交换子}.
\]
因此 raw evolution 中不含 \(U_m\) 或 \(C_m\)。相应地，
\[
\partial_tC_{m+1}
\]
可含当前变量 \(U_m\)，但不含 \(U_{m+1}\) 或 \(C_{m+1}\)。

在 \(\|C_m\|_p^p\) 的能量导数中，逆度量和体积变化会产生代数项
\[
U_0*C_m,
\]
但这不是 raw jet evolution 的新高阶依赖。

### 2.5 \(\partial_tU\) 主部推导漏了一个 \(a\)

因为 \(a\) 是固定标量，
\[
\partial_tU=a\,\partial_tT.
\]
若
\[
\partial_tT\supset a\Delta T,
\]
则
\[
\partial_tU\supset a^2\Delta T,
\]
而非 §4.4 所写的 \(a\Delta T\)。将 \(U=aT\) 展开后，主部才重写为
\[
a\Delta U
\]
加上 \(\nabla a*\nabla T\)、\(\nabla^2a*T\) 等项。因此最终退化扩散算子是合理的，但当前推导在转换前丢失了一个 \(a\)。

### 2.6 (4.12) 的危险项列表不完整

除
\[
\chi C_{m+2}*U_0,\qquad
C_1*C_{m+1}*U_0
\]
之外，还必须列入
\[
\boxed{\chi C_{m+1}*U_1}.
\]
它来自 \(\nabla^{m+1}a*U_1\)，也会在对顶阶
\(C_{m+2}\) 项第一次积分分部后出现。该项正是 A03 (2.6) 需要第二次积分分部修复的对象：

- \(m\ge2\) 时写 \(C_{m+1}=\nabla C_m\)，再积分一次；
- \(m=1\) 时并入 signed Hessian 项。

所以“只对 \(C_{m+2}\) 积分一次即可完成处理”的表述不足。正确结论是：不存在 \(C_{m+2}U_j\)（\(j\ge1\)），但存在当前 cutoff jet 与 \(U_1\) 的耦合，需 A03 的额外 IBP。

此外，顶阶项的 \(\chi\)-权重必须从精确的 \(U\)-方程重新推导。原始扩散产生
\[
a\,C_{m+2}T=\chi^2C_{m+2}T.
\]
若改写成 \(U_0=aT\)，不能无验证地写为
\(\chi C_{m+2}U_0\)，后者等于 \(\chi^3C_{m+2}T\)。由于 A03 的论证非常依赖真实的 \(\chi\) 因子位置，此处不是可忽略的记号问题；应先给出精确 product-rule 展开，再决定采用 \(T\) 还是 \(U\) 表示。

---

## 3. 与 A03 staggered induction 的相容性

修正上述问题后，以下 ordering 在导数阶数上仍是三角的：
\[
T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
\longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots .
\]

关键依赖为：

- \(U_{m+1}\) 只以 \(\chi C_1U_{m+1}\) 型出现，可由加权扩散吸收；
- \(C_2U_m\) 型当前 Hessian 项通过 signed IBP；
- \(C_{m+2}U_0\) 与 \(C_{m+1}U_1\) 由 A03 的两次 IBP 处理；
- \(C_{m+1}\) 方程依赖 \(U_m\)，但不依赖 \(U_{m+1}\)；
- 随后的 \(T_m\) 方程可使用已得到的 \(U_m,C_{m+1}\)。

Kulkarni–Nomizu、归一化和交换子没有发现新的 upward branch：

- \(\partial_tG\) 的 \(m\) 阶导数至多含 \(U_m\)；
- 归一化项只产生 \(\nabla^sa*\nabla^{m-s}T\)；
- 时间连接交换子的顶阶形式为当前阶 \(U_m\) 乘零阶量；
- Laplacian 交换子产生曲率乘低阶导数；其中无权 \(T_0\) 因子依赖 §3 提供的所有有限 \(L^q\) 控制，再由 Hölder 使用；
- cutoff 导数换序产生 \(\Rm*C_{\le m}\)，仍属于先前 \(T_j\) 和 cutoff 层。

但 §4 单独并未证明完整任意阶能量不等式。其 derivative-counting 公式没有精确跟踪所有 \(a,\chi\) 因子的放置，而这正是确保当前无权曲率只以 \(aT=U\) 作为有界系数出现所必需的。可严格支持的表述是：

> §4 给出了 A03 schematic induction 的导数三角性证据；结合 A03 对关键当前-jet 项的额外积分分部，没有发现破坏 induction 的项。它尚不是完整的任意阶张量展开证明。

最后，这些结论均以正时间 slab 上已有光滑解为前提。§5.1 明确尚未给出 transported DeTurck 的完整 start/restart tame estimates，因此 continuation theorem 及全文 Theorem 1.1 目前仍是有条件的，而不能由 §3–§4 单独推出。
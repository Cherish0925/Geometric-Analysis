# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 7,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step7_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step7_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the obstruction-amplitude principle for the positive branch of Yau Problem 26 in dimension 4. The claim: if a sequence (M_i, g_i) of closed oriented smooth 4-manifolds has |Ric_{g_i} - g_i|_{C^0} ≤ δ_i → 0 and is noncollapsed (Vol(B_1) ≥ v > 0), then at any orbifold singularity p of the GH limit, det R|_{Λ²_+}(p) = 0. The argument: (1) the MV Calabi region estimate gives Ric_{g_t} - Λg_t - tλχ_t o = O(t²ρ²) in g_cal-norm, where o is the first obstruction endomorphism; (2) converting to g_t-operator norm, the obstruction tλo has g_t-norm of order 1 (since g_t^{-1} ~ t^{-1} g_cal^{-1}); (3) since o is non-scalar when det R ≠ 0, it cannot be absorbed into a scalar Einstein constant; (4) therefore ||Ric - λg||_{C^0} ≥ c > 0, contradicting δ_i → 0. Check: (a) does this scaling argument apply to positive λ (the MV original is for negative Einstein orbifolds)? (b) is the conversion from g_cal-norm to g_t-norm correct in the core and transition regions? (c) does the non-scalar nature of o genuinely force a C^0 lower bound, or could cancellation between multiple singularities or between the obstruction and higher-order terms eliminate the defect? (d) Ozuch Example 1 on S^4/Z_2 shows L^p-close sequences exist without C^0 convergence when det R ≠ 0 — does this confirm or is it merely consistent with the principle? (e) What are the main gaps between this heuristic principle and a rigorous theorem?

## Integrated Scientific Memo

## 核验结论

所述命题目前**没有由给定论证证明**。正确结论是：

> 障碍振幅机制在已经具有 Biquard–Ozuch/Eguchi–Hanson 加权拼接展开的四维度量族中成立；但从“非塌缩且  
> \(\|\operatorname{Ric}_{g_i}-g_i\|_{L^\infty}\to0\)”推出任意轨形奇点满足  
> \(\det R_+(p)=0\)，仍缺少决定性的结构与正则性定理。

其中 \(R_+=R|_{\Lambda^2_+}=W_++\frac{s}{12}I\)，但必须按 ALE 泡诱导的定向选择块；反向定向会交换 \(R_+\) 与 \(R_-\)。

---

## 1. 在拼接正规形内，尺度计算是正确的

设在 ALE 核心区
\[
g_t=t\,h_t,\qquad h_t=g_{\mathrm{ALE}}+O(t\rho^2),
\]
并有
\[
Q_t:=\operatorname{Ric}_{g_t}-\Lambda g_t-t\mu\,\chi_t o,
\qquad
|Q_t|_{g_{\mathrm{ALE}}}\le Ct^2\rho^2 .
\]
这里用 \(\mu\) 表示障碍系数，避免与 Einstein 常数混淆。对 \((0,2)\)-张量 \(T\)，
\[
\|T\|_{g_t,\mathrm{op}}
=\|g_t^{-1}T\|_{\mathrm{op}}
\asymp t^{-1}\|g_{\mathrm{ALE}}^{-1}T\|_{\mathrm{op}} .
\]
故
\[
\|Q_t\|_{g_t,\mathrm{op}}\le Ct\rho^2.
\]

- 固定紧 ALE 核心中 \(\rho=O(1)\)，余项为 \(O(t)\)；
- 过渡区 \(\rho\asymp t^{-1/4}\)，余项为 \(O(t^{1/2})\)。

而
\[
g_t^{-1}(t\mu o)=\mu\,h_t^{-1}o
\longrightarrow \mu\,g_{\mathrm{ALE}}^{-1}o
\]
在 \(o\neq0\) 的固定核心子集上是 \(O(1)\)。四维 Eguchi–Hanson 情形的障碍张量是非零、无迹的，因此其端同态不是标量。

在过渡区，四维障碍模态按 \(\rho^{-4}\) 衰减，故障碍项本身约为 \(O(t)\)。所以一致的 \(C^0\) 下界来自缩小的核心，而不是过渡区；这也正是有限 \(L^p\) 范数可以趋零的机制。

### 一个必要的源文修正

MV 文本的 Lemma 4.2 支持上述
\[
\operatorname{Ric}_{g_t}-\Lambda g_t-t\mu\chi_t o
=O_{g_{\rm cal}}(t^2\rho^2)
\]
形式。其 Lemma 4.1 转录附近存在一次漏写 \(t\) 的排版/OCR 不一致，但证明和 Lemma 4.2 明确给出 \(t\mu o\)。尺度判断应以后者为准。

---

## 2. 非标量障碍确实不能被 Einstein 常数吸收

若 \(S=g_{\mathrm{ALE}}^{-1}o\) 是自伴、非标量的，则
\[
\inf_{a\in\mathbb R}\|\mu S-aI\|_{\mathrm{op}}
=\frac{|\mu|}{2}
\bigl(\lambda_{\max}(S)-\lambda_{\min}(S)\bigr)>0.
\]
因此在某个固定核心子集 \(K\) 上，
\[
\inf_{a\in\mathbb R}
\|t\mu o-a g_t\|_{g_t,\mathrm{op}}
\ge c_K|\mu|-O(t).
\]
这比仅说“\(o\) 非标量”更精确：真正给出下界的是端同态谱宽。

由此可得，在已有该展开且 \(|\mu|\ge\mu_0>0\) 时，
\[
\inf_a\|\operatorname{Ric}_{g_t}-a g_t\|_{C^0}
\ge c\mu_0-o(1).
\]

不过本题假设已经固定为
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{C^0}\to0,
\]
所以其实无需优化全局标量 \(a\)：任何非零无迹核心分量直接与该假设矛盾。讨论改变 Einstein 常数只是在处理更一般的“近某个标量 Einstein”版本时需要。

---

## 3. 正 Einstein 符号本身不是问题，但 MV 不能直接充当四维定理

### 局部尺度方面

上述升指标计算不依赖 \(\Lambda\) 的正负。MV 的局部展开也以一般
\[
\operatorname{Ric}(g_0)=\Lambda g_0
\]
书写；其紧致非存在定理和正 Kähler–Einstein 非例也表明，不能把该机制描述为仅适用于负 \(\Lambda\)。

### 真正的问题是模型和维数

MV 的主要 Calabi 分析针对复维 \(n\ge3\)，即实维至少六；四维是 \(n=2\) 的 Eguchi–Hanson 情形，并有额外旋转参数。因此不能把 MV 的标量障碍公式直接等同于四维条件
\[
\det R_+(p)=0.
\]

四维正确图景是：Eguchi–Hanson 的定向/旋转参数选择一个自对偶方向，首阶障碍由 \(R_+(p)\) 对该方向的作用控制；存在某个可使首阶障碍消失的方向，当且仅当 \(R_+(p)\) 有核，即
\[
\det R_+(p)=0.
\]
若 \(\det R_+(p)\ne0\)，旋转不能创造核。因此首阶必要性对旋转是稳定的，但定量振幅应由四维 Biquard–Ozuch 展开重新写出，不能沿用 MV 的高维系数。

对于归一化 \(\operatorname{Ric}=g\)，\(s=4\)，故
\[
R_+=W_++\frac13I.
\]
给定计算中：

- 圆 \(S^4\)：\(R_+=\frac13I\)，\(\det R_+=1/27\ne0\)；
- \(S^2\times S^2\)、\(\mathbb{CP}^2\)：相应定向下 \(R_+\) 特征值为 \((1,0,0)\)，行列式为零。

这些代数计算与障碍条件相容，但不是一般定理的证明。

---

## 4. 多奇点和高阶项不会在既定拼接展开内消除首阶缺陷

### 多奇点

各 ALE 核心在小尺度上互不相交。\(C^0\) 是点态上确界，因此不同核心之间不存在积分意义的正负抵消：
\[
\|E\|_{C^0}\ge \|E\|_{C^0(K_j)}
\]
对每个核心 \(K_j\) 都成立。局部无迹谱宽也不可能被另一个奇点改变。

### 高阶项

在固定核心中，首阶障碍升指标后为 \(O(1)\)，所引余项为 \(O(t)\)。因此若首阶系数趋于一个非零值，高阶项不能抵消它。

真正可能改变结论的是：

1. 旋转、尺度或 ALE 模参数令首阶系数本身为零；
2. 轨形的全局 infinitesimal Einstein 变形改变奇点处曲率数据；
3. 存在多层泡树，需证明局部测试能隔离指定尺度；
4. 原序列根本不落入所假设的拼接正规形。

所以“取消”问题在正规形内已排除；未解决的是正规形的适用性和完整有限维参数方程。

---

## 5. Ozuch Example 1 只是强烈相容证据，不是确认

Ozuch 的例子在 \(S^4/\mathbb Z_2\) 的光滑化上构造
\[
\|\operatorname{Ric}(g_i)-3g_i\|_{L^p}\to0,\qquad
\operatorname{Ric}(g_i)\ge3g_i,
\]
且 GH 极限为该圆轨形，但不存在具有同一极限的精确正 Einstein 序列。

这与核心振幅机制完全一致：若核心上的点态缺陷为 \(O(1)\)，而四维尺度 \(g_t=t g_{\rm ALE}\) 下核心体积为 \(O(t^2)\)，则
\[
\|E_t\|_{L^p}^p=O(t^2),\qquad
\|E_t\|_{C^0}\asymp1.
\]
但该例没有证明：

- 所构造度量的 \(C^0\) 缺陷趋零；
- 任意可能的光滑化度量都必须具有统一 \(C^0\) 下界；
- 底层光滑流形完全不承载任何 Einstein 度量。

因此它说明为何有限 \(L^p\) 接近不足，并支持障碍集中图景；它不证明本题的 \(C^0\) 原理。

---

## 6. 从启发式到严格定理的主要缺口

### (i) 题设本身没有保证 GH 极限是 Einstein 轨形

非塌缩和双边 Ricci 界给出 GH/Ricci-limit 紧性，但在仅有
\[
\operatorname{Ric}=g+E_i,\qquad \|E_i\|_{L^\infty}\to0
\]
时，并没有现成定理给出：

- 只有有限个轨形奇点；
- 奇点附近光滑轨形坐标；
- Ricci-flat ALE 泡和泡树；
- 加权 \(C^{k,\alpha}\) 颈区收敛。

确切 Einstein 情形中的这些结论依赖 Einstein 方程及其曲率椭圆系统。仅 \(C^0\) Ricci 缺陷不给出 \(\nabla\operatorname{Ric}\) 或 Weyl 的相应方程。

因此严格表述应是：

> **若** GH 极限另已知为光滑 Einstein 轨形并且序列在该奇点形成合适 ALE 泡，是否可推出 \(\det R_+(p)=0\)？

即便这个条件版也还需要下一项。

### (ii) 缺少“近 Einstein 度量”的加权拼接正规形

Ozuch 给出的 GH 接近轨形 \(\Rightarrow\) 加权拼接描述，适用于**精确 Einstein 度量**。目前没有由纯 \(L^\infty\) Ricci 夹逼推出同样正规形的结果。没有它，不能断言任意 \(g_i\) 的 Ricci 缺陷含有 \(t_i\mu_i o\) 这一项。

### (iii) 需要四维的局部投影/Pohozaev 恒等式，并控制低正则残差

最有希望的替代是构造局部障碍测试张量 \(o_i\)，证明类似
\[
\langle \operatorname{Ric}(g_i)-g_i,o_i\rangle
=
t_i\,\mathcal O(R_+(p),\text{orientation})
+o(t_i).
\]
四维尺度有利：\(L^\infty\) 缺陷的投影预计也是 \(O(\delta_i t_i)\)，于是除以 \(t_i\) 后可令障碍系数趋零。但要使该论证成立，仍必须建立：

- ALE 坐标与测试张量；
- 边界通量和规范误差控制；
- 其他奇点、较深泡和颈区交叉项为低阶；
- 仅 \(L^\infty\) Ricci 残差足以合法化分部积分。

### (iv) 必须声明泡模型和定向假设

给定 Ozuch Theorem 0.3 只覆盖选定定向下的 Kähler Ricci-flat ALE 泡。若一般近 Einstein 序列产生其他 ALE 模型，所给来源不能直接推出行列式条件。

### (v) 点态非零与统一定量下界要区分

对固定极限奇点，\(\det R_+(p)\ne0\) 给出 \(R_+(p)\) 可逆，故相应首阶障碍有正下界。若极限轨形本身随子序列变化，则需控制最小奇异值；仅“每项行列式非零”并不自动给出统一常数。不过在题目已固定一个 GH 极限及其点 \(p\) 时，这不是主要障碍。

### (vi) \(\det R_+=0\) 只是首阶必要条件

即使首阶条件成立，高阶和全局阻碍仍可能阻止 Einstein 去奇点。故该原理即使证明，也只给出必要条件，不能单独推出原光滑流形承载 Einstein 度量。

---

## 可严格保留的条件命题

现有材料支持如下精确版本：

> 设一族四维光滑化度量在某 Eguchi–Hanson 核心上满足 Biquard–Ozuch 型展开
> \[
> \operatorname{Ric}_{g_t}-\Lambda g_t
> =t\,\mathcal O_p\,o+Q_t,
> \qquad
> |Q_t|_{g_{\rm EH}}\le Ct^2\rho^2,
> \]
> 且 \(g_t=t(g_{\rm EH}+O(t\rho^2))\)。若首阶障碍系数
> \(\mathcal O_p\ne0\)，则
> \[
> \inf_{a\in\mathbb R}
> \|\operatorname{Ric}_{g_t}-a g_t\|_{C^0(g_t)}
> \ge c|\mathcal O_p|-o(1).
> \]
> 特别地，这类度量不可能满足
> \(\|\operatorname{Ric}_{g_t}-g_t\|_{C^0}\to0\)。

将 \(\mathcal O_p\ne0\) 精确等同于 \(\det R_+(p)\ne0\)，需要引用或重新导出四维 Eguchi–Hanson 首阶障碍映射。将该条件命题推广到题设中的任意非塌缩 \(C^0\)-夹逼序列，则正是目前未闭合的核心科学对象。
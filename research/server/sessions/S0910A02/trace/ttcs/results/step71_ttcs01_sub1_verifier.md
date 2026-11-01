# TTCS Independent Branch Record

```json
{
  "step_id": 71,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step71_collapse_quantum_and_lean_scope.md",
    "Sessions/S0910A02/workspace/scripts/step71_collapse_quantum_diophantine.py",
    "Sessions/S0910A02/workspace/data/step71_collapse_quantum_diophantine.json",
    "Sessions/S0910A02/workspace/notes/step58_biquard_ct_and_collapse_ceiling.md",
    "Sessions/S0910A02/workspace/notes/step64_positive_mirror_homeomorphism_and_allocation.md",
    "Knowledge/objects/papers/Curvature-cones-and-characteristic-numbers--8d08033cf0c7--47e3a363f7a4/object.md",
    "Knowledge/objects/papers/The-collapsing-geometry-of-almost-Ricci-flat-4-manifolds--a6608f08b3f8--f94b3ef0dffe/object.md",
    "Sessions/S0910A02/workspace/proofs/Step71RicciOnlySearch.lean",
    "Sessions/S0910A02/workspace/proofs/Step71Yau26SyntheticStatement.lean"
  ]
}
```

## Task

Verify the Step-71 collapse quantum/chiral-split audit for the positive-collapse front of Yau Problem 26. The target is the spin balanced row homeomorphic to #_3(S^2 x S^2), with chi=8 and tau=0, under a hypothetical positive Ricci-pinched collapse Vol->0. Check: (1) the corrected Chern--Gauss--Bonnet ledger total int|W|^2 -> 64 pi^2 and chiral split int|W+|^2=int|W-|^2 ->32 pi^2; (2) ALE Ricci-flat quantum Q=chi-1/|Gamma| and ALF quantum Q=chi as used; (3) the ADE enumeration result that total Q=8 has only 3*A2 but no ADE multiset has Q=4 in one chiral half; (4) whether the inference to a compatibility gate for half-flat ALE/ALF concentration is valid or needs caveats about orientation, signature boundary terms, ALF/ALG/collapsed bubbles, or non-hyperkaehler Ricci-flat limits; (5) whether the Lean/Mathlib scoping conclusion is accurately separated from mathematical proof. Give a direct mathematical memo: identify errors, overclaims, missing assumptions, and the strongest valid conclusion for the next research step.

## Output

# Step 71 数学核验备忘录

## 总结

Chern–Gauss–Bonnet 数值、手征总量以及 ADE 精确枚举均正确。真正需要收紧的是它们与实际坍缩序列之间的连接：

- 对假设序列，可直接证明全局 Weyl 能量趋于 \(64\pi ^2\)，两个手征部分分别趋于 \(32\pi ^2\)。
- ALE、ALF 量子公式在文中采用的曲率算子范数以及标准端部衰减条件下正确。
- 纯 Kronheimer ADE、半共形平坦并且无颈部能量残留的分解不可能实现每个手征 \(Q=4\)。
- 仅由 \(C^0\) Ricci 夹逼尚不能得到这种量子分解：可能没有光滑 Ricci-flat 泡极限，也可能有过渡区、弥散能量或非半共形平坦模型。
- Lean 文件清楚地区分了“量词骨架”和真正的 Riemann 几何形式化；它没有构成原命题的形式化证明。

---

## 1. Chern–Gauss–Bonnet 账本正确，且手征相等对每个度量都成立

令
\[
\varepsilon_i=\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op},g_i}\longrightarrow0,
\qquad
\operatorname{Vol}(M,g_i)\longrightarrow0.
\]
在四维中，
\[
s_i=4+O(\varepsilon_i),\qquad |E_i|=O(\varepsilon_i),
\]
其中 \(E_i=\operatorname{Ric}_{g_i}-\frac{s_i}{4}g_i\)。因此
\[
I_i:=\int_M\left(\frac{s_i^2}{24}-\frac{|E_i|^2}{2}\right)d\mu_i
=O(\operatorname{Vol}(M,g_i))\longrightarrow0.
\]

由
\[
8\pi^2\chi(M)
=\int_M\left(|W_i|^2+\frac{s_i^2}{24}-\frac{|E_i|^2}{2}\right)d\mu_i
\]
及 \(\chi(M)=8\)，得到
\[
\int_M|W_i|^2\,d\mu_i=64\pi^2-I_i\longrightarrow64\pi^2.
\]

另一方面，\(\tau(M)=0\) 给出
\[
\int_M|W_i^+|^2\,d\mu_i-\int_M|W_i^-|^2\,d\mu_i
=12\pi^2\tau(M)=0.
\]
所以两个手征能量对每个 \(i\) 已经精确相等，而不只是极限相等：
\[
\int_M|W_i^\pm|^2\,d\mu_i
=32\pi^2-\frac{I_i}{2}
\longrightarrow32\pi^2.
\]
归一化后，
\[
\frac1{8\pi^2}\int|W_i^\pm|^2\longrightarrow4.
\]

“曲率有界区域贡献趋零”需要写成统一有界：若 \(U_i\subset M\) 且
\[
\sup_{U_i}|\operatorname{Rm}_{g_i}|\le K
\]
其中 \(K\) 与 \(i\) 无关，则
\[
\int_{U_i}|W_i|^2\le C(K)\operatorname{Vol}(M,g_i)\to0.
\]
这只说明保留下来的能量位于不存在统一全曲率上界的区域；它本身并不产生有限个泡点或量子化分解。这里 spin 性质没有参与计算，所用的只有 \(\chi=8,\tau=0\)。

---

## 2. ALE 与 ALF 量子公式正确，但必须固定范数约定和端部假设

所引 Atiyah–LeBrun 文本给出：

- 对 Ricci-flat ALE 空间，端部为 \(S^3/\Gamma\)，
  \[
  \frac1{8\pi^2}\int_X|\mathcal R|^2\,d\mu
  =\chi(X)-\frac1{|\Gamma|}.
  \]
- 对具有标准 ALF 渐近、有限拓扑型及相应衰减的 Ricci-flat 瞬子，截断端面项趋零，故
  \[
  \frac1{8\pi^2}\int_X|\mathcal R|^2\,d\mu=\chi(X).
  \]

这里脚本中的 \(|Rm|^2\) 必须解释为该文采用的曲率算子范数；该文对 Weyl 范数含有
\[
|W|^2=\frac14W_{ijkl}W^{ijkl}.
\]
若改用另一种四阶张量范数，数值会相差固定因子。对 Ricci-flat 空间，采用同一约定时 \(\mathcal R=W\)，所以这些量子可以和全局 Weyl 能量直接比较。

ALF 的整数性是总能量
\[
Q_{\mathrm{ALF}}=\chi(X)\in\mathbb Z,
\]
并不自动意味着两个手征分量分别为整数。只有在该 ALF 模型半共形平坦时，全部能量才落入一个手征。

文献对若干 ALG/ALH 例子也得到相同的 Euler 数公式，但所给文本把一般 ALG/ALH 情形表述为预期模式，而非统一定理。Ooguri–Vafa 过渡区又是另一类不完备、混合坍缩几何，不能直接作为一个独立 ALF 整数量子处理。

---

## 3. ADE 枚举正确且脚本是完备的精确枚举

对 Kronheimer \(A_k,D_k,E_k\) 空间，
\[
Q=\chi-\frac1{|\Gamma|}.
\]
脚本列出的数据与标准群阶相符：
\[
Q(A_k)=k+1-\frac1{k+1},\qquad
Q(D_k)=k+1-\frac1{4(k-2)},
\]
以及 \(E_6,E_7,E_8\) 的群阶 \(24,48,120\)。

脚本只枚举 \(Q\le8\) 的类型是充分的，因为所有量子严格为正。最小量子为
\[
Q(A_1)=\frac32,
\]
所以总和为 \(8\) 时至多有五个非平凡 ADE 项。代码用 `Fraction` 和 `combinations_with_replacement` 做精确有理数比较，并且实际搜索长度超过五，因此不会遗漏。

输出
\[
8=3\left(3-\frac13\right)=3Q(A_2)
\]
确实是唯一的 ADE 多重集解。

对单个手征目标 \(Q=4\)，可以直接人工验证：可能出现的单项只有
\[
Q(A_1)=\frac32,\qquad Q(A_2)=\frac83,\qquad Q(A_3)=\frac{15}{4},
\]
均不等于 \(4\)。三个 \(A_1\) 已有 \(Q=9/2>4\)，故最多两个项；唯一不超过 \(4\) 的双项是
\[
2Q(A_1)=3.
\]
因此不存在 ADE 多重集总和为 \(4\)。

若再加入半共形平坦 ALF 整数量子，则 ADE 部分也必须是整数。小于等于 \(4\) 的 ADE 整数总和只有
\[
0,\qquad 2Q(A_1)=3.
\]
所以每个手征只有两类算术配置：
\[
\begin{cases}
Q_{\rm ADE}=0,\quad Q_{\rm ALF}=4,\\[2mm]
Q_{\rm ADE}=3\;(2A_1),\quad Q_{\rm ALF}=1.
\end{cases}
\]
这里“4 个 ALF 单位”应理解为 ALF 总量等于 \(4\)，不一定是四个不同泡；它也可能由一个 \(\chi=4\) 的 ALF 空间承担。

---

## 4. 手征不相容结论成立所需的附加结构

可以精确表述为以下条件命题。设归一化手征能量测度
\[
\nu_i^\pm=\frac1{8\pi^2}|W_i^\pm|^2d\mu_i
\]
完全分解为若干光滑完备半共形平坦 Ricci-flat 浓缩模型，且：

1. 所有 ALE 模型都是 Kronheimer ADE 空间；
2. 其余模型都是满足上述端部衰减的半共形平坦 ALF 空间；
3. 基底、颈部和过渡区没有留下非零 Weyl 能量；
4. 每个模型的定向由母流形定向诱导，因此其全部能量明确落入 \(W^+\) 或 \(W^-\)。

则
\[
\nu_i^\pm(M)\to4
\]
要求每一手征的泡量子和为 \(4\)。由上述枚举，纯 ADE 分解不可能；唯一的总 ADE 解 \(3A_2\) 也无法按整泡分成两个总量均为 \(4\) 的手征组。

这是一条有效的算术排除结果，但目前的 \(C^0\) Ricci 假设尚未提供上述四项结构。主要数学缺口是：

- 在尺度 \(r_i\to0\) 下，重标后的 Ricci 算子大小确实为 \(O(r_i^2)\)，所以任何已有的光滑极限都会 Ricci-flat；但 \(L^\infty\) Ricci 控制本身不给出光滑紧性。Step 58 所引相反翘曲尖峰还说明可有高曲率而局部 \(L^2\) 能量趋零。
- 因而尚不能断言存在有限个具有固定正量子的泡，也不能排除弥散浓缩。
- 非半共形平坦 Ricci-flat 模型可同时含有 \(W^+\) 与 \(W^-\)。其总 CGB 量子不能决定手征拆分；截断非紧空间的 signature 公式还含 APS \(\eta\) 型端项。
- ALF、ALG、Ooguri–Vafa 过渡区或更深层的坍缩泡树可以承担额外手征能量。
- 即使能量配置允许，还需核对端部三流形、交叉格、spin 结构及全局粘接拓扑。量子算术没有编码这些数据。

Lott 文献中的 Taub–NUT、二面体 ALF 和 Ooguri–Vafa 现象说明这些几何确实会出现在几乎 Ricci-flat K3 坍缩中；但该文假设的是尺度不变量
\[
\|\operatorname{Ric}\|_\infty\operatorname{diam}^2\to0.
\]
当前正 Ricci 序列 \(\operatorname{Ric}\approx g\) 并不自动满足这一条件。因此 Lott 的结果在这里提供模型证据，而不是正 Ricci 坍缩的分类定理。

---

## 5. Lean 环境结论与数学证明分离得当

`Step71RicciOnlySearch.lean` 找到了 `IsRiemannianManifold` 和 `Bundle.ContMDiffRiemannianMetric`，但在当前导入环境中没有找到名称含 Ricci、Riemann curvature、scalar curvature、Levi-Civita 等关键词的常量。这充分支持一个实践性结论：当前 Mathlib 没有已经定位到的、可直接表达该命题的 Ricci 曲率接口。名称搜索不能排除某个完全不同命名的底层构件，但即使存在连接或一般曲率构件，Ricci 收缩、二次型次序和 Einstein 方程仍需额外开发。

`Step71Yau26SyntheticStatement.lean` 只记录量词结构。尤其：

- `RicciPinched` 与 `EinsteinMetric` 是任意谓词；
- 没有定义 Levi-Civita 连接、Ricci 张量或
  \[
  \exists\lambda,\ \operatorname{Ric}_h=\lambda h;
  \]
- `M : Type` 本身没有显式携带选定的光滑结构，故同一载体上的不同光滑结构也没有被原生区分；
- 已证明的 `dimensionStatement_of_normalizedSignBranch` 只是区间端点的线性算术。

文件注释已经明确说明这一点，所以它没有把逻辑骨架混同为 Yau 第 26 题的形式化证明。

## 最强可用结论

目前可以独立复核的结论是：

> 对 \(\chi=8,\tau=0\) 的假想正 Ricci 夹逼坍缩，两个手征 Weyl 能量各趋于 \(4\cdot8\pi^2\)。若全部能量由无残留的半共形平坦 Kronheimer ALE 泡承担，则这种分解不可能；若允许标准半共形平坦 ALF 泡，则每个手征的 ADE 部分只能为空或恰为两个 \(A_1\)。

把这条算术事实转化为坍缩不存在性，仍需一个适用于 \(C^0\) Ricci 夹逼的浓缩紧性与能量恒等式，以及对 ALF/ALG/过渡区、手征端项和全局粘接拓扑的分类。
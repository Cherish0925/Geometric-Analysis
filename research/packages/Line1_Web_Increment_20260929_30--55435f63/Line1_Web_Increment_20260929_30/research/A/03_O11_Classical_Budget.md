# O11 的经典全曲率入口：已知精确值、完整类预算与真正缺失的斜率

日期：2026-09-29。对照底本：`upload/27b3cef6-aeed-442c-9e66-fef1a757828e.tex`，重点为第5334–6040行的手术变分部分、第4217行起经典包络、第8950行起有符号特征数选择以及第9884行起开放问题。

本轮没有证明一般 O11 的最优首项，也没有构造低于4的原族竞争度量。独立核查确认：经典 Ricci 能量的精确值不能直接关闭 O11；但原 O11 手术族的**完整 monopole 凸包与 period minimax 预算可以精确算出**，无需识别全部类。这关闭了一条可能的纯预算攻法。另一个直接相关的一手结果是 ABKS 的 Yamabe–Weyl 边界定理；它说明缺失的是可实现域的首阶斜率，而不是该域边界上的数值。

## 1. 统一范数及原族

令
\[
M=X\#k\overline{\mathbb {CP}}^2\#\ell(S^1\times S^3),\quad
A=c_1^2(X)>0,\quad Q=k+4\ell,
\]
其中 X 是复双曲曲面。Ricci 用张量范数；Weyl 用作用在二形式上的 Hilbert–Schmidt 范数。记
\[
S=\int s^2,\quad P=\int|\operatorname{Ric}^{\circ}|^2,\quad
R=P+S/4,\quad W_\pm=\int|W^\pm|^2,\quad W=W_++W_-.
\]
于是
\[
\chi(M)=A/3+k-2\ell,\qquad \tau(M)=A/9-k.
\]
全部竞争度量具有原稿明确构造的实际单极子供给。下述完整类集合结果取高覆盖族中的 \(b^+\ge2\) 情形，因而没有 chamber 问题。

## 2. 经典精确 Ricci 能量公式确实覆盖完全相同的手术族

LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, Theorem 4.3，给出
\[
\inf_gR(g)=8\pi^2(A+Q).
\]
其 Proposition 4.2 的度量逐点版本是
\[
R(g)\ge8\pi^2\{2p_g-T_+\}\ge8\pi^2(A+Q).
\]
相应标量最小值为 \(\inf_g S(g)=32\pi^2A\)，恢复构造同时趋于这两个下界。

**不能据此相减得到 \(\inf P=8\pi^2Q\)。** 对任意 g，R 的下界只给
\[
P(g)\ge8\pi^2(A+Q)-S(g)/4,
\]
右端随 S 增大而减小；标量下界并不能从右端替换出一个更强下界。

LeBrun 2004 的 *Curvature Functionals, Optimal Metrics, and the Differential Topology of 4-Manifolds*，末节在讨论一般型曲面时明确区分全曲率与 Ricci 曲率最小值：前者当时只有上下界，后者可精确计算。因此该篇不能被援引为一般 O11 已由经典定理解决。

一手来源：

- https://arxiv.org/pdf/math/0003068 ，Propositions 4.1–4.2、Theorem 4.3。
- https://arxiv.org/pdf/math/0404251 ，第38–39页的最后讨论（PDF页码）。

上述第二篇的历史开放状态不是对2026年所有文献的穷尽断言。本轮定向检索没有获得解决本项目原平衡族首项的后续定理。

## 3. 一个可严格加入的结论：原族的完整 monopole 预算已经封顶

为避免与本文 \(\alpha_j=\inf\mathcal E\) 混淆，将 LeBrun 的 period minimax 记作 \(\mathfrak a^2\)，凸包平方记作 \(\mathfrak b^2\)。设 \(\mathcal C(M)\) 为全部实际 monopole 类的实上同调集合，定义
\[
\mathfrak b^2(M)=\max_{v\in\operatorname{Hull}(\mathcal C(M))}v^2,
\quad
\mathfrak a^2(M)=\inf_H\max_{a\in\mathcal C(M)}(a_H^+)^2,
\]
H 遍历最大正子空间。采用 \(b^+\ge2\) 的全度量单极子定义。

**命题。** 对上述原 O11 手术族，
\[
\boxed{\mathfrak b^2(M)=\mathfrak a^2(M)=A.}
\]

**证明。** 实际吹起与柄供给包含所有 exceptional sign choices
\[
c+\sum_{i=1}^k\epsilon_iE_i,\quad \epsilon_i\in\{\pm1\},\quad c^2=A.
\]
它们的平均为 c，所以 \(c\in\operatorname{Hull}\mathcal C(M)\)，从而 \(\mathfrak b^2\ge A\)。

对于任何 H 及凸组合 \(v=\sum t_i a_i\)，
\[
v^2\le|v_H^+|^2\le\max_{a\in\mathcal C(M)}|a_H^+|^2.
\]
故 \(\mathfrak b^2\le\mathfrak a^2\)。另一方面，取原稿已有 scalar recovery 度量 \(g_\varepsilon\)，使
\[
S(g_\varepsilon)\longrightarrow32\pi^2A.
\]
**每一个**实际 monopole 类都可在同一个 \(g_\varepsilon\) 上应用标量估计，因而同时满足
\[
\max_{a\in\mathcal C(M)}(a_{g_\varepsilon}^+)^2
\le\frac{S(g_\varepsilon)}{32\pi^2}.
\]
实际 Hodge 正平面是 minimax 中允许的正平面，所以 \(\mathfrak a^2\le A\)。夹逼即得结论。证毕。

这沿用了本项目早期 all-class ceiling 的思想，是它对原 O11 surgery 族的直接应用；不应宣称为一种全新的分析机制。定义与一般比较的一手来源是 LeBrun, *Four-Manifolds, Curvature Bounds, and Convex Geometry*, Definition 4.3 与 §5：
https://arxiv.org/pdf/math/0611450 。

**作用与边界。** 无论还有多少未列出的 monopole 类，它们都不能把该族的统一凸包/period-minimax 平方预算提升到 A 之上。因此“寻找遗漏的类，让统一预算变成 A+cQ”不能解决这个原族的 O11。它不排除多个实际解的更强微分相容性信息，也不决定某个指定 g 上的投影预算；更不计算另一个 stable-cohomotopy BF 连通和族的完整类预算。

## 4. 已有但原稿未显式引用的直接前置：Yamabe–Weyl 边界

Akutagawa–Botvinnik–Kobayashi–Seshadri, *The Weyl functional near the Yamabe invariant*, Theorem C，研究的正是
\(X\#k\overline{\mathbb {CP}}^2\#\ell(S^1\times S^3)\)。

用本文 Weyl **算子**范数换算，他们计算出的 Yamabe 边界 Weyl 最小值是
\[
\omega_{\mathrm{op}}(M)=\frac{4\pi^2A}{3}+12\pi^2k.
\]
原论文的完整 Weyl 张量范数比这里大4倍；不换算会直接造成错误系数。其 Yamabe 不变量满足
\[
Y(M)=-4\sqrt2\pi\sqrt A.
\]

该边界结论控制：在固定 M 上，当共形类的 Yamabe 常数趋向 \(Y(M)\) 时，Weyl 能量的极限下界。它没有给出原 O11 中 \(M_j\) 改变、误差为 \(O(Q_j)\) 时所需要的一致斜率。

一手来源：https://arxiv.org/pdf/math/0201153 ，Theorem C、第2.1节；其中第9页说明了Weyl范数换算。

## 5. 精确的联合能量表达：所缺斜率为 −1/24

对负 Yamabe 代表定义
\[
\Delta_S=S-32\pi^2A\ge0,\qquad
\Delta_W=W-\omega_{\mathrm{op}}(M).
\]
Gauss–Bonnet 与 signature 直接给出
\[
\boxed{P=8\pi^2Q+\frac{\Delta_S}{12}+2\Delta_W.}\tag{1}
\]
证明只需代入 \(P=S/12+2W-16\pi^2\chi\)，所有常数都已固定。

同理
\[
R=8\pi^2(A+Q)+\frac{\Delta_S}{3}+2\Delta_W.
\]
所以经典精确 Ricci 下界只有
\[
\boxed{\Delta_W\ge-\Delta_S/6.}\tag{2}
\]
而原 O11 的系数4要求在真正近极小序列上证明
\[
\boxed{\Delta_W\ge-\Delta_S/24-o(Q).}\tag{3}
\]
这个斜率差是四倍。ABKS 的边界值告诉我们 \(\Delta_S\to0\) 的固定M端点上不能存在负极限；它不把(2)升级成(3)。

公式(3)是 O11 的精确重写，**不是新的下界证明**。它的用途是辨认文献、测试候选及指出为何 sharp Ricci/Yamabe 两个已知定理不足。若能另外证明近极小序列 \(\Delta_S=o(Q)\)，则(2)确实立即与(1)给出目标，但这个小量结论本身目前没有一般证明。

更细地，经典 scalar–Weyl 包络满足（在括号为非负的邻域）
\[
W_+\ge\frac{4\pi^2A}{3}
\left(3-2\sqrt{1+\Delta_S/(32\pi^2A)}\right)^2.
\]
其首阶 Taylor 项仍是(2)的斜率。继续精确优化这个数值包络不会自行获得(3)。

## 6. 原平衡族上，低成本候选至少必须满足什么？

令
\[
t=\frac P{8\pi^2Q},\qquad
\sigma=\frac{S-32\pi^2A}{32\pi^2Q},\qquad
b=\frac{W_-}{2\pi^2Q},\qquad
\theta=\frac{4\ell-5k}{A}.
\]
则全部度量满足精确关系
\[
t=\frac\sigma3+b+\frac\theta h.
\]
原平衡族 \(k/Q\to2/9\) 给 \(\theta/h\to-1/3\)，故竞争序列的极限必须满足
\[
t=\frac\sigma3+b-\frac13,
\qquad 1-t\le\sigma\le1+3t,
\qquad b=t+\frac13-\frac\sigma3\ge0.
\]
左侧不等式来自完整经典 Ricci 下界，右侧来自 \(W_-\ge0\)。

标准恢复序列对应 \((t,\sigma,b)\to(1,0,4/3)\)。任何把代价降低到 \(t\le1-\eta\) 的真实候选，必然具有 \(\sigma\ge\eta\)：它必须增加同阶标量平方预算，同时减少相应Weyl预算，而不能只把原来的局部核心压缩得更小。

这些必要条件没有证明该候选存在。它们可以直接用于筛选构造输出：若声称低于阈值，却仍有 \(S-32\pi^2A=o(Q)\)，则已与经典 Ricci 下界矛盾。

## 7. 2023 Weyl 平衡论文并没有自动补出缺失箭头

LeBrun, *Curvature in the Balance: The Weyl Functional and Scalar Curvature of 4-Manifolds*，Theorem B，含有闭 almost-Kähler 且 \(\delta W^+=0\) 时的 scalar/Weyl 比较。这个输入要求实际全局 almost-Kähler 结构与零散度；任意 O11 竞争度量尚未提供它们。其不等式方向也不能直接替代(3)。

一手来源：https://arxiv.org/pdf/2203.02528 。出版信息：PAMQ 19 (2023), 2737–2763。

因此本轮可合并的数学增量是第3节完整类预算的直接应用；可合并的文献增量是第4节ABKS的精确边界。一般最优首项的缺口仍在第5节(3)或与之等价的全局实际结构/真实竞争构造，不能将这些核查写成已闭合O11。

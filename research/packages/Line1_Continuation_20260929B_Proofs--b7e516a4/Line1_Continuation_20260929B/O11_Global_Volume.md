# O11：自适应试验的正量恒等式与体积入口核验

2026-09-29，续研 B。接续前包 `Line1_O10_O11_Proof_Increments_20260929.zip` 中的经典预算及弱驻点论证，并独立核验本轮相邻文件 `O11_Descent_or_Recovery.md`。本记没有证明 O11 的最佳系数为 4，也没有构造较低系数。主要新增结果是：直接无迹 Ricci 自适应 resolvent 的一阶变分中，有一块原先未定号的组合实际上非负；近极小弱驻点必须由曲率耦合补偿这一正量。文末仅记录 BCG 体积路线的准确适用边界。

## 1. 设置与已核验的预算

在原平衡族上，取上一轮允许选择的负 Yamabe 近极小序列，归一化为标量曲率 `s=-4`。记

\[
Z=\operatorname{Ric}^{\circ},\qquad P=\int_M|Z|^2=O(Q),\qquad
\int_M|\operatorname{Rm}|^2=O(A),\qquad Q/A\longrightarrow0.
\]

以下令 \(\Delta=\nabla^*\nabla\) 为正 rough Laplacian。定义

\[
v=\sqrt{1+|Z|^2},\qquad (\Delta+v)H=Z. \tag{1}
\]

在每个光滑闭流形上，正势保证唯一光滑解，且联络保持对称无迹子丛。独立核验得到

\[
\|H\|_\infty\le1,\quad
\int\bigl(|H|^2+|\nabla H|^2+|\Delta H|^2\bigr)=O(Q), \tag{2}
\]

\[
\int\bigl(|\nabla^2H|^2+|\nabla H|^4\bigr)=O(A). \tag{3}
\]

证明 (2) 时，最大值原理控制上确界；与 H 配对控制 H 的二次能量；随后

\[
\int v^2|H|^2=\int|H|^2+\int|Z|^2|H|^2=O(Q)
\]

控制 \(\Delta H=Z-vH\)。证明 (3) 所需的统一估计是

\[
\int|\nabla^2H|^2\le C\left(\int|\Delta H|^2+
\|H\|_\infty^2\int|\operatorname{Rm}|^2\right),
\qquad
\int|\nabla H|^4\le C\|H\|_\infty^2\int|\nabla^2H|^2.
\]

第一式中的曲率导数先分部积分，化为 \(\operatorname{Rm}*H*\nabla^2H\) 与 \(\operatorname{Rm}*\nabla H*\nabla H\)，再用第二式和 Young 吸收。第二式由散度积分直接得到。这里不需要 v、Z 的导数界，也不使用 Sobolev 或直径常数。因此，经固定常数缩放，H 是上一轮 Q 尺度弱驻点允许的试验。

**原实际族上的更强预算。** 本轮 `O11_Descent_or_Recovery.md` 已利用原稿的实际场 Weyl 估计，将 (3) 加强为 O(Q)。这一步也已独立核验。具体令

\[
\xi=(w_3^++w_3^- -1/3)_+.
\]

原稿 `Conformal Ricci flow` 部分的同场估计给

\[
\int\xi^2\le\frac89\left(D_2/18+3\int|W^-|^2\right)=O(Q).
\]

每个 Weyl 块迹为零，全部特征值绝对值受最大特征值控制；在 s=-4 时，

\[
|\operatorname{Rm}|\le C(1+\xi+|Z|).
\]

以 \(e=\xi+|Z|\)、\(\|e\|_2^2=O(Q)\) 重新估计 Hessian 交换式：有界背景项使用 (2)，e 项使用 H 的上确界及

\[
\|\nabla H\|_4^2\le C\|H\|_\infty\|\nabla^2H\|_2.
\]

Young 吸收后得到

\[
\boxed{\int(|\nabla^2H|^2+|\nabla H|^4)=O(Q).} \tag{3+}
\]

这里无须对 e 或 Weyl 特征值求导。因此 (3) 是一般预算，(3+) 是本轮实际族上的强化版本。

## 2. 新的单调性恒等式

**命题。** 对任意光滑闭流形上的光滑欧氏向量丛、度量联络及光滑截面 Z，令 v、H 满足 (1)。则

\[
\boxed{
\mathfrak D(Z):=\int|Z|^2-\int v\langle Z,H\rangle
\ge \int|\nabla H|^2+\int\frac{|\Delta H|^2}{v}\ge0.
} \tag{4}
\]

该结论不依赖维数、曲率符号或几何紧性。注意它给出的是两个积分之差的正性，不是 \(\int v\langle Z,H\rangle\) 单独的正性。

**完整证明。** 置

\[
z=Z/v,\qquad F(u)=\frac{u}{\sqrt{1-|u|^2}},\qquad |u|<1.
\]

因 M 紧且 Z 光滑，

\[
m:=\max_M\frac{|Z|}{\sqrt{1+|Z|^2}}<1.
\]

方程写为 \((\Delta+v)H=vz\)。Kato 不等式及最大值原理给 \(|H|\le m<1\)。所以 F(H) 是全局光滑截面。这里不要求一列度量上的 m 一致远离 1。

由定义，\(F(z)=Z\)，且

\[
\Delta H=v(z-H). \tag{5}
\]

F 的纤维微分为

\[
DF(u)[w]=\frac{w}{\sqrt{1-|u|^2}}
 +\frac{u\langle u,w\rangle}{(1-|u|^2)^{3/2}},
\]

从而

\[
\langle DF(u)[w],w\rangle\ge|w|^2,
\qquad
\langle F(u)-F(w),u-w\rangle\ge|u-w|^2 \tag{6}
\]

（第二式中的 u、w 均在开单位球内）。现在有精确恒等式

\[
\begin{aligned}
\mathfrak D(Z)
&=\int v\langle F(z),z-H\rangle\\
&=\int v\langle F(z)-F(H),z-H\rangle
  +\int\langle F(H),\Delta H\rangle\\
&=\int v\langle F(z)-F(H),z-H\rangle
  +\int\langle DF(H)[\nabla H],\nabla H\rangle.
\end{aligned} \tag{7}
\]

最后一步只对 H 分部积分；联络保持纤维度量，所以 \(\nabla F(H)=DF(H)[\nabla H]\)。将 (6) 代入，再用 (5)，便得

\[
\mathfrak D(Z)\ge\int v|z-H|^2+\int|\nabla H|^2
=\int v^{-1}|\Delta H|^2+\int|\nabla H|^2.
\]

证毕。

同一个证明也给出常数 \(\lambda>0\) 的版本：若

\[
v_\lambda=\sqrt{\lambda^2+|Z|^2},\qquad
(\Delta+v_\lambda)H_\lambda=Z,
\]

则使用 \(F_\lambda(u)=\lambda u/\sqrt{1-|u|^2}\)、\(DF_\lambda\ge\lambda I\)，得到

\[
\int|Z|^2-\int v_\lambda\langle Z,H_\lambda\rangle
\ge\lambda\int|\nabla H_\lambda|^2
 +\lambda\int v_\lambda^{-1}|\Delta H_\lambda|^2. \tag{8}
\]

本轮应用只需 \(\lambda=1\)。

## 3. 对 O11 弱驻点的实际后果

在 s=-4 的四维度量上，标准一阶变分为

\[
\operatorname{grad}P=\Delta Z-2\operatorname{Rm}(Z)+\tfrac12|Z|^2g,
\qquad \operatorname{grad}S=8Z,\quad S=\int s^2.
\]

因此，对 (1) 的无迹试验 H，

\[
DP[H]=\mathfrak D(Z)-2\int\operatorname{Rm}(Z,H). \tag{9}
\]

在选定的 Q 尺度弱驻点序列上，\(DP[H]=o(Q)\)，所以

\[
\boxed{
2\int\operatorname{Rm}(Z,H)
 =\mathfrak D(Z)+o(Q)
 \ge\int|\nabla H|^2+\int v^{-1}|\Delta H|^2-o(Q).
} \tag{10}
\]

这给出曲率耦合的**积分补偿约束**。它在这些近极小序列上不能有一个负的 Q 级主项；必须补偿 (7) 的非负量。

对于实际极值比值对应的修正泛函

\[
\mathscr F_\alpha=P-c_\alpha S,\qquad
c_\alpha=\frac{\alpha}{4(4-\alpha)},\qquad\alpha=O(h),
\]

有

\[
D\mathscr F_\alpha[H]
=\mathfrak D(Z)-2\int\operatorname{Rm}(Z,H)
 -8c_\alpha\int\langle Z,H\rangle. \tag{11}
\]

由 (2)，\(\int\langle Z,H\rangle=O(Q)\)；最后一项是 \(O(hQ)=o(Q)\)。所以修正泛函的弱驻点也推出 (10)。这一步没有把 P 的近极小序列和 \(\mathscr F_\alpha\) 的近极小序列混同：分别在已证明相应弱驻点选择的序列上使用即可。

还可由 (2) 直接知道

\[
\left|\int v\langle Z,H\rangle\right|
\le\|Z\|_2\|vH\|_2=O(Q).
\]

故 \(\mathfrak D(Z)=O(Q)\)。在本轮实际族上还可利用 (3+) 前的点态曲率控制，直接得到更强的绝对值估计：

\[
\begin{aligned}
\int|\operatorname{Rm}(Z,H)|
&\le C\|Z\|_2\|H\|_2
 +C\|H\|_\infty\|\xi+|Z|\|_2\|Z\|_2\\
&=O(Q). \tag{12a}
\end{aligned}
\]

这个绝对值 O(Q) 估计不需要弱驻点；它改进了仅用全曲率 O(A) 所能给出的 O(√(AQ))。但它仍非 o(Q)，没有决定补偿项的最佳系数。

**剩余的准确缺口。** (10) 没有出现手术拓扑量 \(8\pi^2Q\)，所以不能单独推出 \(P\ge8\pi^2Q-o(Q)\)。要用它闭合 O11，仍须把这项被迫存在的曲率补偿与实际规范场或拓扑标记连接起来，或者证明每个低于阈值的竞争者都违反 (10)。目前未获得这种估计。

另一个变分边界必须保留：在 (9)–(11) 中，H 是在当前 g 上构造后**固定的方向**。对这些表达式沿 g 再求导，会产生 \(D_gH\) 和 \(D_gv\)；它不自动等于固定方向的二阶变分。现有预算不能让这些额外项自动消失。

## 4. 体积路线：确切需要什么，以及 BCG 为什么未提供它

本节只给出本轮来源核验，不重复上轮的经典曲率下界报告。

原实际类满足 \(p=(a^+)^2\ge A\)。定义两种不同的松弛量：

\[
\Delta_S=S-32\pi^2A=16(V-2\pi^2A),\qquad
\Sigma=S-32\pi^2p.
\]

经典实际类 Ricci 估计在此给出

\[
P\ge8\pi^2Q+8\pi^2(p-A)-\Sigma/4. \tag{12}
\]

因此，\(\Sigma=o(Q)\) 足以关闭系数 4；\(\Delta_S=o(Q)\)、即 \(V=2\pi^2A+o(Q)\)，也是一个充分但更强的入口。不能混淆这两种松弛量。

原手术流形存在向 CH 基底的 degree-one 映射。BCG 主定理提供

\[
h_{\mathrm{vol}}(g)^4V(g)\ge h_{\mathrm{vol}}(g_X)^4V(g_X). \tag{13}
\]

这是熵—体积乘积的**下界**。熵上界与 (13) 结合仍只给体积下界，而这里需要的是接近已有下界的上界。即使额外假设点态 \(\operatorname{Ric}\ge-g\)，在 Ric(gX)=-gX 的 CH² 归一化下，\(h_X^2=8/3\)，Bishop 给 \(h(g)^2\le3\)，故这一路组合仅得 \(V(g)\ge(64/81)V(g_X)\)。现有 SW 标量预算 \(V\ge V(g_X)\) 已更强。BCG 原文明确将其 sharp Ricci 最小体积直接推论限定于实双曲目标；这里不把它误套成复双曲的 sharp 推论。

陈—魏的积分 Ricci 熵上界定理要求 \(p>n/2\) 的小积分负 Ricci 误差及直径控制。原 O11 只有四维临界 p=2 的控制，不满足这些条件；该文相关实双曲稳定性定理还**另外假设**接近最小体积的上界，不能反用结论来产生这个假设。即便取得该类熵上界，不等式 (13) 的方向问题仍然存在。

上述检查排除了“仅凭现有 L² Ricci defect 直接套 BCG 得到所需体积上界”的推导；它不是反例，也不排除需要新定理的熵—曲率联合方法。

## 5. 一手文献与本记边界

1. G. Besson, G. Courtois, S. Gallot, *Entropies et rigidités des espaces localement symétriques de courbure strictement négative*, GAFA 5 (1995), 731–799。主定理及实双曲 Ricci 体积推论见 pp.734–735。https://www.aimath.org/WWN/entropyrigidity/papers/BessonCourtoisGallot.pdf
2. L. Chen, G. Wei, *Improved relative volume comparison for integral Ricci curvature and applications to volume entropy*, Theorems 1.4–1.5。https://arxiv.org/pdf/1810.05773
3. 项目内前置：前包 `Line1_O10_O11_Proof_Increments_20260929.zip` 中的近极小弱驻点选择及原族经典预算；本轮相邻 `O11_Descent_or_Recovery.md`（自适应 resolvent、实际 Weyl 预算与修正泛函）。

本轮可纳入主研究记录的新命题是 (4)/(7) 和其弱驻点后果 (10)。预算及一阶变分经交叉核验；O11 的全局拓扑补偿下界仍未证明。

# 第一科学主线：新外部定理的实际接入与定量 Ricci 流推论

日期：2026-10-07。
外部源版本：openai/math，`adc7f1241b42e322a6451854ab7e4b4c146bf78a`。

## 0. 本轮结论与来源层级

本轮没有证明无密度 O10，没有决定 O11 的最佳首项，也没有构造低于现有首项的真实度量。原 N1、I40/I41、有限密度 O10 和线性阶仍按各自已写明的假设使用；本文件不是对其全部前置分析的重新认证。

实际完成的组合推导是：将新发布的“四维 Ricci 流在有限时间标量有界时光滑延拓”定理，与第一主线的全度量正无迹 Ricci 间隙连接，得到**每个正标量曲率阈值都必须在可显式控制的时间内达到**。同时得到永生归一化 Ricci 流的历史最大标量曲率至少线性增长的下界。有限时间阈值结论确实使用新延拓定理；时间积分估计本身由下列完整计算证明。

这是当前已有理论的定量动态应用，不是 O10/O11 的解答，不主张独立历史首创性。外部延拓结果仍以其指定版本的发表稿证明作为输入；本轮读取了该主定理及证明结构，没有重证整个长证明。

另一部分是对 342（taming-to-compatible）和 351（Ricci-flat trees）进入 O10/O11 的逐假设检查。它们提供重要方法，但不能直接替换项目缺失的命题。这里给出的是具体数学差别，而非新增一张方向清单。

## 1. 统一的静态输入

令 M 为闭连通光滑四流形，设

\[
 P(g)=\int_M|\operatorname{Ric}^{\circ}_g|^2\,dV_g\ge p_0>0
 \quad\text{对 M 上每一个光滑度量成立},
 \qquad \mathcal Y(M)<0.
\]

这两项输入必须在对应实际供给范围内验证。只有 \(P+D_2\) 的正下界不够。

第一主线的一个直接输入方式是：存在统一 \(A>0\) 与 \(j_0>0\)，使每个竞争度量满足

\[
 \mathcal J(g)=\frac{4P(g)}{R(g)}\ge j_0,
 \qquad S_2(g)=\int s_g^2\ge32\pi^2A,
 \qquad R(g)=P(g)+\frac14S_2(g).
\]

于是可以取

\[
 \boxed{p_0=2\pi^2 A j_0.}
\]

例如从 N1 取得 \(j_0\) 时，必须保留拓扑超额项：\(\mathcal J+d\ge\varepsilon\) 只有在 \(\varepsilon-d>0\) 时给出正 \(j_0\)。短缺版同理。小 h 平衡族则使用已经证明的线性正 \(\mathcal J\)-下界。

若同一全度量正投影供给还给出负 Yamabe 上界

\[
 \mathcal Y(M)\le-4\pi\sqrt{2A},
\]

则下文可以取 \(a=4\pi\sqrt{2A/V}\)。这可由各个负 Yamabe 代表上的标量预算得到，并非只从任意一个度量的标量积分得到。

## 2. 外部输入：四维有限时间标量延拓

采用 openai/math 第351族中的下述结果。

**外部定理 F。** 若闭光滑四流形上的未归一化 Ricci 流
\(\partial_\tau\widetilde g=-2\operatorname{Ric}(\widetilde g)\)
在有限区间 \([0,\widetilde T)\) 满足
\(\sup|s_{\widetilde g}|<\infty\)，则它在原光滑流形上可以光滑延拓。

精确源文件：
`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/01-introduction.tex`，`thm:extension`。

这里借用外部定理的实际结论，不把其证明中要求的 Ricci 流时空估计改名成静态 O10 的已知预算。

## 3. 定量阈值定理

考虑体积归一化 Ricci 流

\[
 \partial_t g=-2\operatorname{Ric}+\frac12\bar s\,g,
 \qquad \bar s(t)=\fint_M s_{g(t)},
 \qquad V=\operatorname{Vol}_{g(0)}M.
\]

定义初始数据

\[
 m_0=\min_Ms_{g(0)},\qquad b_0=-m_0>0,
 \qquad \bar s_0=\fint_Ms_{g(0)}.
\]

任选 \(a>0\) 使

\[
 \mathcal Y(M)\le-a\sqrt V.
\]

则 \(b_0\ge a\)。对任意
\(K>\max\{0,\max_Ms_{g(0)}\}\)，令

\[
 \tau_K=\inf\{t:\max_Ms_{g(t)}\ge K\}.
\]

**定理 A（本轮组合推导）。** 在第1节静态输入及外部定理 F 下，\(\tau_K\) 在最大光滑时间之前存在，且

\[
 \boxed{
 \tau_K\le\frac{V}{2p_0}
 \left[
 K\left(1+\log\frac{b_0}{a}\right)-\bar s_0+b_0-a
 \right].
 }
\tag{A}
\]

它既不预设流永生，也不预设曲率、直径或 Sobolev 常数统一有界。

### 3.1 Yamabe 上界约束标量最小值

令 \(m(t)=\min s_{g(t)}\)。由于 Yamabe 不变量为负，每个时刻有 \(m(t)<0\)。对于任意非零正函数 u，

\[
 \frac{\int(6|du|^2+s u^2)}{(\int u^4)^{1/2}}
 \ge m(t)\frac{\int u^2}{(\int u^4)^{1/2}}
 \ge m(t)\sqrt V.
\]

最后一个方向使用 \(m(t)<0\) 与 Hölder。取下确界并使用
\(Y([g(t)])\le\mathcal Y(M)\)，得

\[
 \boxed{m(t)\le-a<0.}
\tag{3.1}
\]

### 3.2 两条精确演化关系

使用 \(\Delta=\operatorname{div}\nabla\)，标量演化为

\[
 \partial_t s=\Delta s+2|\operatorname{Ric}^{\circ}|^2
             +\frac12s(s-\bar s).
\]

最小值是局部 Lipschitz 函数；在其几乎处处可微处，最大值原理给

\[
 m'\ge\frac{-m}{2}(\bar s-m)\ge0.
\tag{3.2}
\]

因此 \(m_0\le m(t)\le-a\)。

另一方面，\(\partial_t dV=(\bar s-s)dV\)，故

\[
 \boxed{
 \bar s'=\frac{2P(g(t))}{V}-\frac12\operatorname{Var}(s),
 \quad \operatorname{Var}(s)=\fint(s-\bar s)^2.
 }
\tag{3.3}
\]

### 3.3 有界标量区间最多能持续多久

在任意满足 \(s\le K\)、\(K\ge0\) 的光滑时间区间 \([0,t]\) 内，点态 \((s-m)(K-s)\ge0\) 给

\[
 \operatorname{Var}(s)\le(K-\bar s)(\bar s-m)
                      \le(K-m)(\bar s-m).
\]

由式(3.2)，

\[
 \frac12\operatorname{Var}(s)
 \le\left(1+\frac{K}{-m}\right)m'.
\]

令 \(u_t=-m(t)\)，积分得

\[
 \frac12\int_0^t\operatorname{Var}(s)\,du
 \le K\log\frac{b_0}{u_t}+b_0-u_t
 \le K\log\frac{b_0}{a}+b_0-a.
\tag{3.4}
\]

这里最后一步使用 \(u_t\ge a\) 和 \(K\ge0\)。将式(3.4)与(3.3)积分合并，并使用 \(P\ge p_0\)、\(\bar s(t)\le K\)，得到

\[
 \boxed{
 \frac{2p_0}{V}t
 \le K\left(1+\log\frac{b_0}{a}\right)-\bar s_0+b_0-a.
 }
\tag{3.5}
\]

这条不等式本身不使用新延拓定理。

### 3.4 新延拓定理排除提前终止的分支

若流在达到 K 之前已有有限最大时间 T，则在 \([0,T)\) 上
\(m_0\le s\le K\)。因此 \(\bar s\) 有界。

定义

\[
 c(t)=\exp\left(-\frac12\int_0^t\bar s(u)du\right),
 \quad \widetilde t=\int_0^t c(u)du,
 \quad \widetilde g(\widetilde t)=c(t)g(t).
\]

在有限区间上 c 有正的上下界。直接求导可核对
\(\partial_{\widetilde t}\widetilde g=-2\operatorname{Ric}(\widetilde g)\)，
且 \(s_{\widetilde g}=s_g/c\) 有界。外部定理 F 允许延拓 \(\widetilde g\)，再按其体积归一化即可延拓 g，矛盾。

若永远没有达到 K，且流永生，则式(3.5)与 \(t\to\infty\) 矛盾。因此 \(\tau_K<T_{\max}\) 存在；在 \(t<\tau_K\) 使用(3.5)，令 \(t\uparrow\tau_K\)，得到(A)。证毕。

## 4. 两项直接后果

### 4.1 永生时，历史最大正标量至少线性增长

定义

\[
 K(t)=\max\left\{0,\sup_{0\le u\le t}\max_Ms_{g(u)}\right\}.
\]

将 K(t) 用作式(3.5)的区间上界，有

\[
 \boxed{
 K(t)\ge
 \frac{(2p_0/V)t+\bar s_0-b_0+a}
 {1+\log(b_0/a)}.
 }
\tag{4.1}
\]

因而若流永生，

\[
 \liminf_{t\to\infty}\frac{K(t)}t
 \ge\frac{2p_0/V}{1+\log(b_0/a)}>0.
\]

这是历史最大值的增长，不是每个时刻 \(\max_Ms_{g(t)}\) 都单调，也不是有限时间爆破率。

### 4.2 第一主线的显式拓扑版本

若使用 \(p_0=2\pi^2Aj_0\)、\(a=4\pi\sqrt{2A/V}\)，则

\[
 \boxed{
 \tau_K\le\frac{V}{4\pi^2Aj_0}
 \left[K\left(1+\log\frac{b_0}{a}\right)-\bar s_0+b_0-a\right].
 }
\tag{4.2}
\]

若初始度量已归一化为 \(s=-4\)，则 \(b_0=4\)、\(\bar s_0=-4\)、\(a\le4\)，从而

\[
 \boxed{
 \tau_K\le\frac{V}{2p_0}
 \left[K\left(1+\log\frac4a\right)+8-a\right].
 }
\tag{4.3}
\]

对原平衡族，已经成立的线性 \(\mathcal J\)-gap 给 \(p_{0,j}\ge cA_jh_j\)。对选定的 \(s=-4\) 初始代表，若已有 \(V_j\le C A_j\)，则 a 有统一正下界，故

\[
 \boxed{\tau_{K,j}\le\frac{C_K}{h_j}.}
\tag{4.4}
\]

原稿可选的低缺陷代表满足这一体积预算：由
\(8\pi^2A+P\le R\le8\pi^2AU+4P\)，
\(U=1+O(h)\)、\(\mathcal J=O(h)\)，得 \(R=O(A)\)，再用 \(s=-4\) 的 \(V=(R-P)/4\)。

式(4.4)是上界，不是精确寿命公式，也不决定 O11 的系数。它使用已证线性阶，不需要先完成无密度 O10 或 O11。

## 5. 为什么第342族主定理不能直接替代 O10 的最后一步

外部定理要求一个全局光滑 J 和处处驯服它的闭二形式。它得到同一个 J 的相容辛形式，但一般不保证类不变，也不估计新度量的 P 能量。

在四维，实际非零正旋量定义的 J 满足

\[
 \Lambda_J^-=\omega_J^\perp\cap\Lambda^+,
 \qquad \Lambda_J^+=\mathbb R\omega_J\oplus\Lambda^-.
\]

SW 的 \(F_A^+\) 已沿 \(\omega_J\)；所以 \(F_A\) 在 \(\Phi\ne0\) 处本来就是 J-不变的。这里尚缺的是全局零点处理、处处正性及其在退化中的定量控制，而不是再做一次 J-不变投影。这是代数检查，不是 O10 已解。

此外，原 O11 手术族的自然供给类满足

\[
 a_\epsilon^2=A-k,
 \quad T_+=A-k-4\ell,
 \quad c_2(S^+_{a_\epsilon})[M]=\ell.
\]

当 \(\ell>0\) 时，不存在这个 Spin^c 正旋量丛的处处非零截面。因此不能为了调用342，未经新的论证就把该实际旋量规范化为全局单位截面。这里没有声称这个 M 不存在任何别的 almost-complex 结构。

第342族仍值得迁移的是密度分裂定理：给定已经满足要求的正二维流 P、J-反不变 L2 修正 Q、闭性、质量增长和角度控制，则正二维密度部分 \(P_E\) 闭合。

但在 O10 中，以下两项尚未建立：

1. 由实际集中得到具有所需方向、闭性及几何控制的二维流。标量能量测度不自动是这种流；新稿的固定几何热核常数也不自动统一。
2. 证明其与某个闭形式的配对同时受到正下界与零值约束。一个正闭流可以代表非零同调类，闭性本身不导致矛盾。尤其第五线丛的特征类本来就是非零的，不能将它未经证明当成精确流。

这两项应从完整实际系统中证明；本轮未完成，因而不宣称使用342闭合了 O10。

## 6. 第351族树定理进入 O11 的精确位置

源定理固定有限 Ricci-flat 树、非平凡拼接端群、高阶加权误差和端部识别。其 E 是重整化 Einstein–Hilbert 泛函，长度尺度为2；目标 P 是四维尺度不变量。

以下三个区别必须保留。

**(i) 固定树不等于树复杂度可随 j 增长。** 原文明确不提供对不同树统一的指数。若用于数量随手术规模增长的核心，必须控制总误差为 o(Q)，不能逐个说“小误差”后不加总。

**(ii) Ricci-flat 极限不等于一般 P 极小化核心。** 一个收费 AE 单元可以标量平坦而不是 Ricci-flat，具有非零 P。源定理的 Ricci 小误差不能在这样的单元上自动满足。

**(iii) 变分估计需要正确的零阶参考值。** 源 E 在精确 Ricci-flat 几何上为零，并将这一事实与导数控制、真实有限维约化、路径选择连接。对 O11，仅有 DP 近零不能确定 P 应当等于 8π²Q。后者仍需原手术标记和边界能量的真实对应。

因此本轮不把树定理写成 O11 下界。可迁移的是核—余核保留、端部模态及合法参数约化；要真正改变 O11，必须为目标曲率平方泛函建立自己的比较，并保留 Q 尺度的拓扑参考值。当前还没有完成这一项。

## 7. 本轮状态，不重新移动终点

| 内容 | 状态 |
|---|---|
| 定理 A：全度量正 P-gap 强迫每个标量阈值在显式时间内达到 | 本轮给出完整组合证明，采用外部定理 F |
| 永生流历史最大标量的线性下界；原平衡族阈值时间 O(1/h) | 上述证明的定量推论，列明初始体积条件 |
| 342 的直接主定理应用 | 原输入尚不足；核对了实际 J/零点/正性及同调障碍 |
| 342 的集中流分裂移植 | 尚缺实际流构造和可用配对，不宣称完成 |
| 351 的树约化用于 P 的全局最优首项 | 尚缺目标泛函、原标记、覆盖范围及总误差连接 |
| 无密度 O10、O11 最佳首项 | 未解决；本轮没有新增相应最终上下界 |

这份补充可放在主稿的动态推论中，不取代 N1 或 I40/I41，不把它改名为端点闭合。原研究文件未修改。

## 8. 来源、定位与核查

外部固定版本：`adc7f1241b42e322a6451854ab7e4b4c146bf78a`。

- openai/math，四维 Ricci 流光滑延拓，`build/sections/01-introduction.tex`，`thm:extension`；Git blob `79ad3cccfc0ea53356596fdde428ee9527ddfc18`。
- openai/math，Taming implies compatibility on four-manifolds，`01-introduction.tex` 的主定理与锥比较；`04-energy.tex` 的相对投影与角度控制；`06-splitting.tex` 的正密度限制闭性。分别 blob `797ccd700e3e15d3a0b94791f0db090361490b47`、`42dea8fc1e2415e2675879ecfadc16630cb33e41`、`4dbdd71553fe9e86100b37fb824e506b8c5d3cd0`。
- openai/math，Path selection and an elliptic inequality on degenerating Ricci-flat trees，`02-tree.tex` 的设置、泛函变分及 tree inequality；`07-observables.tex` 的标量展开和微分估计。blobs `fadb54a125c0a23211313ca134cda70babf9f0e0`、`40c8ea2464f0da603bd8300c55f9d48755ee2f4b`。
- Masashi Ishida，The Normalized Ricci Flow on Four-Manifolds and Exotic Smooth Structures，arXiv:0807.2169，§§2–3：归一化方程、标量最小值及负 Yamabe 的作用。本轮的显式时间不等式在正文重证，不将经典 Ricci 流障碍关系称为首次发现。
- 项目 `03_N1_Complete_Inheritance.md`：全度量应用的正预算与准确 gap 区域；原整合稿 `eq:vg-two-sided-R` 及约5979–5991行：两侧 Ricci 预算、c2(S+) 恒等式。

外部主入口（代码形式便于精确复制）：

`https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a`

`https://arxiv.org/html/0807.2169`

有限核验脚本 `verify_constants.py` 检查方差代数、积分原函数、时间阈值、尺度变换、Spin^c 第二陈数及 P-gap 常数。它不验证 Ricci 流 PDE 或外部长证明。

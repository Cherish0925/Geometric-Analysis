# openai/math 对 Qiushi 第一科学主线的研究接口

核对日期：2026-10-07。
仓库版本基线：`adc7f1241b42e322a6451854ab7e4b4c146bf78a`。
用途：给 O10、O11 主研究会话直接使用；不是两个开放问题的解答。

## 1. 发布规模、核对范围与结论

该版本 README 登记 **722 份稿件、372 个结果族**。结果族可以包含主论文、伴随论证、推论和不同证明，不能把稿件数量当作独立定理数量。README 明确说明验证阶段不同，并非全部有 Lean 形式化，未形式化部分可能需要修正。本次未核实到“766 项均已认证的重大突破”这一计数与状态。

本次进行了目录与学科概览筛查，随后读取下面四篇主稿的定理和关键证明部分，另检查了相关形式化范围与若干不能直接套用的结果。没有逐式审读全部 722 篇，也没有在本地重新编译 Lean 库。

核心结论：

1. **O10 最值得研究的新接口**是第342族论文的“正密度集中流仍然闭合”机制，而不是再使用一次 resolvent 本身。
2. **O11 最值得研究的新接口**是第351族的“保留核与余核的多尺度椭圆约化＋路径选择”，但原定理控制的泛函、范数和树类别不同，不能直接替代 O11。
3. 第348族 L2 Einstein gap 是必须比较的新近邻；非负截面曲率是实质假设，不能换成负 Einstein 的积分逼近。
4. 第351族四维 Ricci 流延拓定理能够直接接出一个主线的动态推论，见第6节。这不解决 O10/O11，也不需要为使用它重启另一项科研任务。

## 2. 保留本项目的目标与量词

O10 的最高目标仍是在实际供给、`p >= A > 0`、`a^2 >= T_+` 下，不预设 Euler 密度上界，证明

\[
\kappa_\beta\ge c\frac{(\beta-2)^2}{\beta^2},\qquad
\kappa_\beta=\fint|\operatorname{Ric}+g|^2+D_\beta/V.
\]

已经登记的有限密度结论不是新的待证任务。剩余障碍是反手性曲率密度无界时，中间幅度径向集中、实际方程相容性及第五线丛质量不能同时得到控制。单纯改善缺陷与曲率增长的速率关系，不等于无密度结论。

O11 要决定原实际平衡族的最优首项，不预设结果必须等于4。原族

\[
M_j=X_j\#k_j\overline{\mathbb{CP}}^2\#\ell_j(S^1\times S^3),
\quad Q_j=k_j+4\ell_j,\quad h_j=Q_j/A_j\to0.
\]

沿用已登记的归约

\[
\alpha_j=4\frac{\inf_gP(g)}{8\pi^2A_j}+O(h_j^2),
\qquad P(g)=\int|\operatorname{Ric}^{\circ}|^2.
\]

外部资料若要改善首项，必须提供 `Q_j` 尺度的真实信息，不能只给 `o(V_j)`。本次不以未获得原始证明证书的跨会话数值摘要，改变最优值状态。

## 3. 第342族：Taming implies compatibility on four-manifolds

论文日期：2026-09-23。

### 原稿的定理与真正可迁移的机制

原稿主定理：闭连通光滑四流形上的光滑 almost-complex structure J，若被某个 symplectic form tame，则存在与同一个 J compatible 的 symplectic form。一般不保证保持原来的上同调类；`b_2^+=1` 的类保持结论是另一个推论。

证明并非直接将二形式作 J-不变投影，因为那样会破坏闭性。其反证方法构造正流 P 和 J-反不变修正 Q，使 T=P+Q 满足闭性或相应消去关系。正流带有复直线方向的测度表示，因而比一个标量能量测度保留更多几何信息。

原稿得到：

\[
\mu(B_r(x))\le Cr^2,
\]

以及近邻复直线的角度二阶矩

\[
\mathcal A_r=\iint_{d(x,y)<r}|\ell-\tau_{yx}m|^2\,d\lambda(x,\ell)d\lambda(y,m)
=O(r^4).
\]

令 E 为正二维密度集合，核心分裂定理证明 **限制流 P_E 仍然闭合**。决定性边界项不是分别要求两个误差有很快的收敛率，而是把角度误差与横向偏离保留成乘积：

\[
Cr^{-3}\sqrt{\mathcal A_r}\sqrt{\mathcal T_r}
=r^{-3}O(r^2)o(r)=o(1).
\]

再分开正密度与零密度部分，消除修正，完成正流与 tame 形式的矛盾。

### 与 O10 的具体接口

项目已经知道标量幅度矩关系允许径向集中。该论文提供另一种思路：**不先要求集中消失，而是证明集中携带一个闭合、定向、可配对的几何对象，再用拓扑关系限制它。**

应先检查能否从原实际曲率与径向结构构造有几何方向的二维流，证明相应闭性、正性、质量增长及角度估计。不能把 `|grad v|^2 dV` 这样的标量测度直接叫成正闭二维流。

两个必须处理的差别：

- 原稿固定一个闭流形及光滑 J-Hermitian 度量；热核、小球坐标、投影交换子常数可依赖这些固定数据。O10 的流形、J 和几何都可退化，不能直接把原常数当成密度无关常数。
- O10 的几乎复结构来自可能有零点的实际旋量。必须保留零点与中间幅度层，不能由 L2 近似得到处处的全局 tame 结构。

因此优先移植的是分裂定理及其临界边界乘积，而不是主定理的名称。

### 已读源码

目录：
`preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/`

- `build/sections/01-introduction.tex`：主定理、分裂框架与范围。
- `build/sections/04-energy.tex`：`lem:mixing`、`prop:energy`，Hodge resolvent、相对投影估计及角度控制。
- `build/sections/06-splitting.tex`：`thm:splitting` 的证明；`eq:critical-scaling` 是关键临界配对。

形式化入口：`lean/docs/342.md`；`lean/ComparatorChallenges/TamingCompatibility.json` 指向 `OAI.Geometry.TamingCompatibility.Main`。已读取 main theorem 与 comparator 的对应声明，没有运行整库验证。Comparator challenge 文件中的 `sorry` 是待比较的目标陈述，不能脱离 JSON 指向的 solution module 便断言没有证明。

## 4. 第351族：退化 Ricci-flat 树上的路径选择与椭圆估计

论文：*Path selection and an elliptic inequality on degenerating Ricci-flat trees*，2026-09-24。

### 原稿精确控制的对象

固定一棵有限 Ricci-flat 四维几何树，拼接端的群非平凡，固定端部识别，根部 ALE 衰减阶 q>1。假设给定顶点上的光滑收敛、至20阶的端部度量界，以及至10阶的加权、尺度化 Ricci 小误差 M。

控制的是重整化 Einstein–Hilbert 泛函

\[
\mathscr H(g)=\lim_{R\to\infty}
\left[\int_{r<R}s_g\,dV_g-
\int_{r=R}(\partial_jg_{ij}-\partial_ig_{jj})n_i\,dS\right],
\]

结论为 `mathscr H(g_j)=o(M_j)`，只对固定树及其数据成立。该泛函的长度量纲为2；O11 的 P 是四维尺度不变量。不要使用同一个字母 E 掩盖这个区别。

### 最值得复用的两个步骤

**保留核与余核的有限维约化。** 核由有限个核心测试控制；余核以紧支撑源保留；颈部临界球面模态作为独立匹配数据。不是先假设 Lichnerowicz 算子可逆，也不预设所有无穷小 Ricci-flat 变形都可积。构造实际的有限维模障碍族 h_*(L,z)，并控制原度量到该族的距离及泛函误差。

**多尺度路径选择。** 颈长可以以不同速率趋无穷，幂—对数渐近展开不被冒充为收敛幂级数。选取保留符号和极限的解析路径，使

\[
\int\left(\sum|dz_\alpha|+\sum e^{-cL_e}|dL_e|\right)<\infty.
\]

若 F 为约化观测量，J 为约化 Ricci 平方误差，论文证明

\[
|dF|\le C\sqrt J\left(\sum|dz|+\sum e^{-cL}|dL|\right).
\]

假设失败序列满足 `F != 0`、`F -> 0`、`F^2 >= c J`，路径选择保留这些关系，使 `log|F|` 的总变差有限，与 `F -> 0` 矛盾。

### 对 O11 的用法与缺口

可借用的是：不盲目从全度量序列跳到有限参数，而先保留全部慢模态和障碍，建立到真实参数族的定量比较，然后处理多尺度边界。

目前项目的近驻点选择并不自动提供论文要求的高阶加权范数、固定有限树或标准端部。原普通 AE 手术还可能出现平凡端群，不属于原文明确的拼接端类别。必须补入相应临界模态与估计，不能直接套用。

若应用于 O11，还须将比较误差控制为 `o(Q_j)`，并对实际曲率平方泛函证明自己的变分关系。`mathscr H=o(M)` 不等于 `P >= 8 pi^2 Q-o(Q)`。

### 对 O10 的另一项启发

同族四维 Ricci 流论文将最外层曲率尺度作为主要对象，保留所有更小子尺度；最终得到

\[
cK^2\le o(1)(K+1)^2,
\]

从而 K->0，而不是预设 K 有界后改善误差增长率。这是一种值得复用的闭合形态。但是它的时间变化、Ricci 能量和选尺度来自实际 Ricci 流，不能对静态 O10 直接使用。

### 已读源码

树论文目录：
`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/`

- `build/sections/01-introduction.tex`：约化、路径选择与最终对数矛盾。
- `build/sections/02-tree.tex`：`thm:tree-inequality`、准确几何与范数要求。

进一步阅读入口（本次只核实目录与引言定位，未完整逐式检查）：
`03-path.tex`、`04-family.tex`、`05-tails.tex`、`06-length.tex`、`07-observables.tex`。

## 5. 第348族：L2 Einstein gap 的相邻结果，不能删除曲率符号

论文：*An L2 Einstein Gap for Nonnegatively Curved Four-Manifolds*，2026-10-05。

原稿假设闭、单连通、四维、**截面曲率非负**；若无迹 Ricci 的未体积归一化 L2 平方积分足够小，推出底层光滑流形为 S4、CP2 或 S2xS2。它使用伴随论文对精确非负截面曲率正 Einstein 度量的分类。

可借鉴的分析是高曲率尾部的动态阈值：

\[
w(t)=(|Rm|-K(t))_+,\quad K'=C_qK^2,
\qquad \int w(t)^2\le e^{Ct}\int w(0)^2.
\]

但启动它之前，原稿使用 sec>=0 得到 `|Rm| <= C s`，用 Ric>=0 的 almost-Schur 和几何比较获得体积、直径、Sobolev 控制。O10 的 s=-4 和不受控制的 W- 并不满足这些条件。O11 中总曲率常为 O(A)、局部修正总量为 O(Q)，体积平均小也不能直接替换原文的绝对小尾能量。

因此这篇是新近邻和方法来源，不是已经解决项目负 Einstein 分支的同一个定理。它也说明“无需预设几何紧性”可能通过结构条件先推出紧性；项目的实际场路线不能与此混同。

已读源码：
`preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/build/source/main.tex`

读取范围包含定理、初始归一化、背景高尾、Sobolev与尾传播部分。`lean/docs/348.md` 当前明确描述的是严格正截面曲率 Einstein 分类，不是这篇后来新增的全部 L2 gap 分析；同一族的 Lean 标记不能自动扩展到所有伴随稿件。

## 6. 一项能直接写入主线的条件性动态推论

下面是本次从来源定理推出的连接，不是来源已经替我们陈述的定理，也不声称全球首创。

假设闭定向光滑四流形 M 满足

\[
\mathcal Y(M)<0,\qquad
\inf_g\int_M|\operatorname{Ric}^{\circ}_g|^2\,dV_g=p_0(M)>0.
\]

这些输入应在项目确有单独正 P-gap 的窗口验证；不能用 `P+D_2>0` 代替。

采用第351族的四维标量曲率有界延拓定理，则 M 上从任意光滑初始度量出发的体积归一化 Ricci 流，在整个最大存在区间不可能有统一的标量曲率绝对值上界：

\[
\sup_{0\le t<T_{\max}}\|s_{g(t)}\|_{\infty}=\infty.
\]

证明分两种时间结局。

1. `T_max < infinity`：若标量一致有界，解除体积归一化的比例因子在这个有限时间区间有统一正上下界，转换后的未归一化流也在有限时间保持标量有界。新延拓定理使其延拓，反推原流可延拓，矛盾。
2. `T_max = infinity`：负 Yamabe 不变量给出标量最小值的统一负上界。在标量绝对值有界假设下，Fang–Zhang–Zhang／Ishida 的耗散结论给 `integral_0^infinity P(g(t)) dt < infinity`，与 `P(g(t)) >= p0(M)>0` 矛盾。

这个推论没有证明一定在有限时间爆破，没有给出爆破率，也不解决 O10/O11；它说明新结果可以直接加强既有主线的动态结论。

来源：
- `preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/01-introduction.tex`，`thm:extension`。
- M. Ishida, *The Normalized Ricci Flow on Four-Manifolds and Exotic Smooth Structures*, arXiv:0807.2169，第2节 Proposition 3、第3节 Proposition 5。

## 7. 已筛过但不宜优先套用的条目

- **341 hypersymplectic deformation**：需要三条全局闭二形式，每个非零线性组合都保持正辛性。多个 SW 解不等于这样的三元组；一条有零点的形式也不满足它。其类保持超Kähler实现很强，但目前不是 O10/O11 的直接输入。
- **335 Gromov integral scalar inequality**：在四维给出标量平方对实单纯体积的下界。它不是 P 的锐利手术成本；也不允许相减两个独立下确界。
- **336 spectral scalar width**：需要 `-4 Delta+s >= 1`。在 s=-4 的闭代表上测试常数函数已经失败；第五线丛的正势不是这个标量算子。
- **337 Cartan–Hadamard/CAT(0)**：要求截面曲率上界或 CAT(0) 几何；L2 近 Einstein 不提供这些条件，带吹起的整个流形也不能被当成原复双曲主体。
- **338 Yau uniformization**：是完备非紧 Kähler、严格正全纯双截曲率的复解析统一化，不是 Yau26 的纯 Ricci 夹逼问题。
- **346/355 varifold/MCF**：需要相应驻定、整性、演化方程；一般曲率缺陷测度不能直接按此调用。
- **356/357 RCD**：需要指定测度、合成 Ricci 下界，某些结论还有非塌缩；四维临界 L2 Ricci 误差不能直接充当 RCD 输入。

## 8. 实际采用顺序

O10 会话先读取342的密度分裂证明：检验实际集中是否能携带闭合的正几何流，并列出在变动几何上需要且尚未取得的统一常数。只移植可证明的部分，不将固定度量定理直接写成无密度定理。

O11 会话先读取351的核—余核约化与路径选择：判断能否对一个真实竞争分支建立带标记、正确尺度的比较。不预设所有竞争者都属于该分支，也不把高阶强范数换成现有L2残差。

348作为相邻文献与尾传播工具对照；第6节的短推论可以同步核对后纳入应用，不把它计作O10/O11闭合。

最终继续研究的目标不变：无密度端点的统一判定，以及原平衡族最优首项。外部定理的引用只需在其准确输入范围内成立，不必从零重新证明；项目真正新增的贡献在验证新接口和由此获得的新结论。

## 9. 原始来源链接与核对状态

- 发布说明：[README，固定版本](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/README.md)
- [全目录 CONTENTS](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/CONTENTS.md)
- [342：taming-to-compatible](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026)
- [351：Ricci-flat tree inequality](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026)
- [351：4D Ricci-flow extension](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026)
- [348：L2 Einstein gap](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026)
- [342 Lean范围](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/342.md)
- [342 Comparator配置](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/TamingCompatibility.json)
- [348 Lean范围](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/348.md)
- [Ishida原文](https://arxiv.org/html/0807.2169)

重要源文件的 Git blob SHA（可作版本核对，不代表正确性认证）：

| 文件 | blob SHA |
|---|---|
| 342 introduction | `797ccd700e3e15d3a0b94791f0db090361490b47` |
| 342 energy | `42dea8fc1e2415e2675879ecfadc16630cb33e41` |
| 342 splitting | `4dbdd71553fe9e86100b37fb824e506b8c5d3cd0` |
| 351 tree introduction | `f30e9214e39607401c1a56f9ee52108c54c2472d` |
| 351 tree theorem | `fadb54a125c0a23211313ca134cda70babf9f0e0` |
| 351 flow introduction | `79ad3cccfc0ea53356596fdde428ee9527ddfc18` |
| 348 gap main.tex | `cd6105f33aea5f42f658b2e13edaf6579c21eb63` |

文件中的“原稿定理”指发布稿明确陈述并提供证明的结果；本次是针对接口的阅读与推导，不是对这些新发布长证明的完整独立认证。没有重新运行 comparator，不将目录中一个族的形式化标签扩展为族内全部稿件的形式化。

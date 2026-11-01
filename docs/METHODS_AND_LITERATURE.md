# 方法、文献与共同数学结构

本文组织本项目采用的场方程、曲率恒等式、变分方法与构造，并说明它们对相应研究问题给出的结论。下文公式来自所链接的研究原稿；经典文献与本项目推导分列于第 3 节。

## 1. 研究对象与输入

设 $M$ 为闭、连通、定向光滑四流形，$g$ 为光滑黎曼度量；$\chi$、$\tau$ 分别为 Euler 示性数和签名。记 $s$ 为标量曲率，$\operatorname{Ric}^{\circ}=\operatorname{Ric}-sg/4$，$W^\pm$ 为两手性 Weyl 算子，$V=\operatorname{Vol}_g(M)$。未标明测度的积分均相对于 $dV_g$，Weyl 算子采用 Hilbert–Schmidt 范数。定义
$$
P(g)=\int|\operatorname{Ric}^{\circ}|^2,\quad R(g)=\int|\operatorname{Ric}|^2,\quad T_\pm=2\chi\pm3\tau.
$$
四维 Chern–Weil 恒等式为
$$
4\pi^2T_+=\frac1{24}\int s^2+2\int|W^+|^2-\frac12P.
$$
本项目研究这些积分关系与微分方程的联合限制：同一度量的曲率、实际规范场及其协变导数必须同时满足 Weitzenböck、Bianchi 和场方程。几乎 Kähler 分支则要求同一度量承载相容闭二形式。两类输入分别给出下述分析问题。

| 输入 | 数学内容 | 所用命题 |
|---|---|---|
| 普通或 special monopole 类 | 指定 Spin$^c$ 结构的实际 SW 解、自对偶 Hodge 投影及类平方条件 | 单解参数估计、N1、I40/I41 |
| Bauer–Furuta 非消失 | 在相应连通和定理条件下存在单极子类 | 相同分析对这些连通和的应用 |
| Pin$^{-}(2)$ 非消失 | 扭曲解及双覆盖上的普通 SW 解 | 覆盖上积分估计及其归一化下降 |
| 两取向的实际单极子类 | 同一度量的两手性投影与类间交叉积 | 有限密度估计结合双取向配对 |
| 闭二形式 $\Omega$，$\vert\Omega\vert^2=2$，且自对偶 | 与 $g$ 相容的几乎复结构 $J$，由 $\Omega(X,Y)=g(JX,Y)$ 定义 | 几乎 Kähler–Einstein 可积性 |
| $P(g_j)-\inf_gP(g)\to0$ 的高精度序列 | 对所有竞争度量的能量比较 | 指定测试范数中的一阶、二阶变分估计 |
| 内部插入度量与精确外领口匹配 | 闭流形上的光滑竞争度量及全部过渡能量 | 严格上界与覆盖构造 |

单极子类的凸组合可通过凸性进入投影平方估计。需要场方程的步骤则使用实际类及其解。参见 [03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§1、4–6 和 [Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) 的配对定理。

## 2. 方法与证明依赖

在 SW 分支，记 $L$ 为行列式线丛、$a=c_1(L)$、$p=(a_g^+)^2$，并设 $p\ge A>0$。符号 $A$ 表示投影平方的下界。对 $\beta\ge2$ 定义
$$
D_\beta=(1+\beta^{-1})\int s^2+6(\beta+1)\int|W^+|^2-72\pi^2p,
\quad \Sigma=\int s^2-32\pi^2p,
\quad Y=(T_+-a^2)_+,
$$
其中 $x_+=\max\{x,0\}$。以下涉及端点极限的范数均采用归一化测度 $dV/V$。

| 方法 | 处理的问题 | 原稿结论及适用条件 | 尚需研究的命题 |
|---|---|---|---|
| 相容背景消去 | 校准曲率背景对实际旋量的作用 | I40/I41 在其单解输入下控制 $\Sigma$ 与 $P+D_2$ | 对新的场方程建立相应消去及联络估计 |
| 有界截面 Hessian 估计 | 无统一 Sobolev 常数时的二阶协变导数 | 通过 Ricci 缩并、丛曲率及粗 Laplacian 控制积分 Hessian | 负旋量丛中的无界 $W^-$ 项 |
| 同场弱 Bianchi 测试 | 场选出的 Weyl 模型与微分曲率恒等式的相容性 | 曲率偏差、联络能量与标量超额的联合估计 | 未被当前投影控制的径向和相位分量 |
| 慢梯度截断与强收敛 | 极限中的临界四次梯度 | 正旋量四次梯度一致可积及三次扭率的相应强收敛 | 无密度条件下负旋量导数的集中 |
| 同丛预解算子与第五幂线丛 | 将扭率转为有界截面 | 固定有限密度下得到 $L^5$ 截面的正质量与导数估计 | 无密度时同时保留质量和完整弱方程 |
| 对数正则化与陈类局部化 | 几乎常正模长截面与非零陈数平方的相容性 | 固定 Dirichlet 能量界下陈数密度趋零 | 能量增长时的密度依赖 |
| 高精度近极小选择 | 下确界未必取得时的变分约束 | 指定临界测试类中得到 $o(Q)$ 一阶、二阶估计，$Q$ 定义于 §2.2 | 由实际拓扑或场方程构造下降方向 |
| 插入构造的相互作用项 | 标准手术上界的最优性 | 固定领口下的负对数项及严格较低上界 | 全部竞争度量的匹配下界 |
| 谐和通量与秩条件 | 临界度量中的曲率和调和形式 | 精确分解及指定几乎 Kähler 类中的下降方向 | 全局极小值的光滑取得性 |
| Weyl 方程、Green 势与扭率零点 | 闭负 Einstein 几何中的可积性 | 一个扭率零点处的势符号即给刚性 | 该势符号是否由一般闭几何强迫 |

前四项的证明关系见 [00_Line1_Research_Atlas_20260928.md](../archive/originals/2026-09-28/00_Line1_Research_Atlas_20260928.md) §§1–3；强收敛与 Hessian 估计见 [O10_Strong_Current_Prerequisite.md](../archive/originals/2026-09-29/O10_Strong_Current_Prerequisite.md)。

### 2.1 积分障碍、有限密度端点与双取向应用

I41 从负 Yamabe 代表上的一个实际解出发，给出
$$
\Sigma\le C\{\Pi+\sqrt{\Pi Y}\},\qquad \Pi=P+D_2.
$$
在 $Y=0$ 时，$\Sigma\le C\Pi$。结合两手性 Chern–Weil 关系，该估计给出原平衡族的线性下界。有限参数分析在 $\beta=8$ 时与 Chern–Weil 系数对齐，得到
$$
\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+\ge\frac{c}{1+Y/A},
\qquad \mathcal J(g)=\frac{4P(g)}{R(g)}.
$$
该 N1 短缺版本要求相应负 Yamabe 代表上的实际 SW 解及 $p\ge A>0$；$Y=0$ 恢复原 N1。

端点分析沿反证序列，先由实际解 $\Phi$ 构造三次扭率 $\mathfrak t\in\Gamma(S^-\otimes L)$，再通过同丛预解算子得到有界截面 $v$，最后取
$$
\sigma=\Phi\wedge t(v)\in\Gamma(L^5).
$$
这里 $S^-$ 是负旋量丛，$t(v)$ 是源稿定义的一阶三次旋量表达式。在固定 Euler 密度 $\chi/A\le B<\infty$ 下，$|\sigma|$ 趋于正常数，且 $\int|\nabla\sigma|^2/V$ 有界。线丛引理给 $c_1(L^5)^2[M]/V\to0$，同一实际曲率恒等式则给极限 $25/(6\pi^2)$。由此得到有限密度命题
$$
\kappa_\beta:=\fint|\operatorname{Ric}+g|^2+D_\beta/V
\ge c_{\rm FD}(B)\frac{(\beta-2)^2}{\beta^2}.
$$
这里仍要求同一结构的整共形类实际供给，以及 $p\ge A>0$、$a^2\ge T_+$；常数依赖 $B$。另一证明以 $L^5$ 上的弱 Cauchy–Riemann 型方程和正势算子完成矛盾。

若 $Q=A-T_+\ge0$ 且 $\chi\le CA+Q$，则按 $Q/A\ge1/3$ 和 $Q/A<1/3$ 分别使用 N1 与有限密度命题，得到依赖 $C$ 的统一端点常数。双取向应用则取固定 $B=2$ 的命题 **FD2**，结合实际类间的交叉配对，推出曲面丛间隙及 Kodaira 斜率上界。FD2 是这些结论的分析前置；一般无密度端点命题不在此依赖链中。

原稿：[O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md) §§2–5；[O10_Finite_Density_Fifth_Line.md](../archive/originals/2026-09-29/O10_Finite_Density_Fifth_Line.md)；[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §2；[Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md) §§1–7。

### 2.2 变分选择与竞争度量

原平衡族写为 $M_j=X_j\#k_j\overline{\mathbb{CP}}^{\,2}\#\ell_j(S^1\times S^3)$，令 $A_j=c_1^2(X_j)$、$Q_j=k_j+4\ell_j$、$h_j=Q_j/A_j\to0$。原稿选取 $P$ 的足够高精度近极小序列，使
$$
|DP_{g_j}[H]|=o(Q_j),\qquad D^2P_{g_j}[H,H]\ge-o(Q_j)
$$
对 $\|H\|_\infty\le1$、$\int(|\nabla^2H|^2+|\nabla H|^4)\le A_j$ 的光滑对称二张量一致成立。导数沿 $g_j+tH$ 定义。这些估计为近极小序列提供变分条件；匹配下界仍需由这些条件及场方程推出。

固定复双曲领口半径 $R_0>0$、背景归一化 $\operatorname{Ric}=-6g$，插入构造给出
$$
\frac{P(g_\epsilon)}{8\pi^2}=1-9\epsilon^2\log(1/\epsilon)+O_{R_0}(\epsilon^2).
$$
积分包括全部过渡区域。先固定充分小的 $\epsilon>0$，再在原稿允许的覆盖族上复制，即得到严格低于标准首项的上界。一般负 Kähler–Einstein 背景的推广采用相应张量展开。

在闭几乎 Kähler 流形且 Ricci 张量 $J$-不变的条件下，源稿证明
$$
DP_g[\operatorname{Ric}^{\circ}]=\frac18\int|ds|^2-\frac12\int s|\operatorname{Ric}^{\circ}|^2.
$$
若 $s$ 为非零常数且 $\operatorname{Ric}^{\circ}\not\equiv0$，则取 $\operatorname{Ric}^{\circ}$ 或其负值给出下降方向。因此该类中的非 Einstein 常标量度量不是 $P$ 的临界点。光滑全局极小元的存在性还要求处理极小序列的退化。

原稿：[02_O11_Variational_Selection.md](../archive/originals/2026-09-29/02_O11_Variational_Selection.md) §§2–3；[O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md)；[01_Research_Synthesis.tex](../archive/originals/2026-10-08/01_Research_Synthesis.tex) §3；[Q3_Descent_and_Flux_Equality.tex](../archive/originals/2026-10-08/Q3_Descent_and_Flux_Equality.tex)；[Q3_Harmonic_Rank_Rigidity.tex](../archive/originals/2026-10-08/Q3_Harmonic_Rank_Rigidity.tex)。

### 2.3 扭率零点与 Green 势

设 $(M,g,J,\Omega)$ 为闭、连通几乎 Kähler 四流形，取 $J$ 诱导的取向，并假设 $\operatorname{Ric}=-a_Eg$、$a_E>0$。于是 $s=-4a_E$。记
$$
q=|\nabla\Omega|^2,\quad n=\Omega/\sqrt2,\quad t=\langle W^+n,n\rangle=s/6+q/4,\quad \eta=W^+\Omega-t\Omega.
$$
采用 $\Delta=-\operatorname{div}\nabla$，定义
$$
\mathcal R_+=W^+-a_EI/3,\quad \mathsf A=-\mathcal R_+,\quad
L_{a_E}=\Delta+2a_E,\quad
\Psi=L_{a_E}^{-1}\det\mathcal R_+,\quad
\mathcal D=L_{a_E}^{-1}|\nabla\mathsf A|^2.
$$
这里 $\mathsf A$ 是曲率算子，与前述投影下界 $A$ 区别。Weyl 方程结合零点 Hessian 恒等式，在每个 $q(p)=0$ 的点给出
$$
18\Psi(p)=\mathcal D(p)+\frac18|\nabla^2\Omega(p)|^2+\frac54|\eta(p)|^2.
$$
正算子 $L_{a_E}$ 的 Green 核为正。因此若某个扭率零点满足 $\Psi(p)\le0$，则 $\nabla\Omega\equiv0$，并有 $\mathcal R_+=-a_En\otimes n$。Armstrong 的零点定理提供零点存在性；势符号条件是本项目命题的附加假设。

其他两条约化分别使用规范曲率与全局闭反不变形式的正交关系，以及调和形式乘积中的正半定、迹一、秩一矩阵条件。完备非紧严格几乎 Kähler–Einstein 构造不满足闭性假设，故与上述闭几何问题分列。

原稿：[Q4_Canonical_Orthogonality.tex](../archive/originals/2026-10-12/Q4_Canonical_Orthogonality.tex)；[Q4_Harmonic_Product_Reduction.tex](../archive/originals/2026-10-13/Q4_Harmonic_Product_Reduction.tex)；[Q4_Green_Potential_Rigidity.tex](../archive/originals/2026-10-14/Q4_Green_Potential_Rigidity.tex)；[Goldberg_Two_Conversations_Merged_20261015.tex](../research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)。

### 2.4 保留全部核的几何修复

在循环覆盖的双曲乘积上，Einstein 线性化的核包含维数随覆盖增长的 Teichmüller 方向。把这些方向积分为精确 Einstein 族，随后仅在核补空间求解，得到
$$
\|g-H_m(k)\|_{C^{3,\alpha}_{\rm uloc}}
\le Cm^2\|\operatorname{Ric}_g+g\|_{C^{1,\alpha}_{\rm uloc}}
$$
及 $cm^{-2}$ 的修复邻域。增长损失来自实际慢通道；统一投影估计处理核维数的增长。慢模态构造达到这一损失，因而它同时说明修复结果的尺度。

对于曲面丛，沿完整闭路积累的纤维度量变形控制单值映射的 Teichmüller 位移。固定厚部内的群作用适当性再将小位移转换为有限单值性。这里起作用的是实际闭路的累计量，局部导数小并不消除长领口上的 Dehn twist。详见[完整核修复与闭路变形](CONSTRUCTIONS_AND_REALIZATION.md)。

### 2.5 实际场的转移与带标记的解消

退化中的场传递需要同时处理方程、能量和拓扑。Wahl 有理球的恢复族具有统一标量界，最大值原理因而控制实际旋量。收缩区的体积趋零排除四次旋量质量集中；阿贝尔可去奇点给出轨形场；实上同调配对和 Chern–Weil 恒等式再传递联络能量。顺序不能倒置为“先假设极限有一个具有正确预算的场”。

在 $\frac1{n^2}(1,n-1)$ 奇点，转移保留 $a^2$、$T_+$ 和相应 Dirac 指标，而
$$
T_-^{\rm orb}=T_-(M)-4(1-n^{-2}).
$$
局部字符还记录哪些实际旋量必须在奇点消失。指定符号类族的平均能够在保留这种零点约束时仍提供正投影预算。具体字符、Fourier 指标计算、强迫零点与连续证明见[Wahl 实际场](../research/notes/Wahl_Fields_and_Formal_Completion.md)。

相同的逐阶分析也给出一项方法边界：辅助 SW 主算子在等变齐次多项式上有右逆，允许的 Dirac 首项可完成到任意形式阶。因此全局排除必须利用实际场、振幅或几何尺度；仅增加有限阶展开不会产生该辅助系统不存在的局部障碍。

### 2.6 用相反符号的缺陷恒等式排除集中

在固定拓扑、非塌缩且直径有界的负 Einstein 序列中，设自对偶 Weyl 的集中质量为 $m_+\ge0$。若每个度量具有同取向相容几乎 Kähler 形式，则该常模长调和形式可延拓到轨形极限。

令 $D_W=s^2V/24-\int|W^+|^2$，$\mathcal T$ 为专题中定义的非负扭率能量。光滑与轨形上的恒等式均给 $D_W=\mathcal T$，而能量传递给
$$
D_W(V)=\lim D_W(g_j)+m_+,\qquad
\lim\mathcal T(g_j)=\mathcal T(V)+m_{\mathcal T}.
$$
因此 $m_++m_{\mathcal T}=0$，两项集中同时消失。这个论证保留集中测度，再由同一全局关系确定其质量；不需要先逐项证明所有导数强收敛。反手性 Weyl 仍可集中。

另一个全局约束来自规范化 Einstein–Hilbert 作用。解析 Einstein 解集上的临界值局部常数，使具有同取向 Kähler–Einstein 轨形端点的连通分支不能含严格几乎 Kähler–Einstein 度量。所需紧性、解析模空间及端点条件见[作用量与能量传递](GOLDBERG.md)。

## 3. 经典结果与本项目推导的关系

下表列出所收原稿引用的主要文献。第二列陈述经典结果；第三列列出本项目采用这些结果的命题及来源。

| 文献 | 经典结果 | 本项目中的推导与来源 |
|---|---|---|
| LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, Invent. Math. 145 (2001), 279–316；[原文](https://arxiv.org/abs/math/0003068) | 实际 SW 的锐利曲率估计、部分 Ricci 极值、等号和恢复构造 | N1/I41 比较临界强制与联合变化；插入构造比较整个过渡区域的能量；[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md)，[Yau26_Line1_External_Review_20260927.md](../archive/originals/2026-09-27/Yau26_Line1_External_Review_20260927.md) |
| LeBrun, *Four-Manifolds, Curvature Bounds, and Convex Geometry*；[原文](https://arxiv.org/abs/math/0611450) | 单极子类凸包、投影优化和边界情形 | 一侧凸包的标量输入、全部普通单极子类的凸包估计与 BF 应用族的相应问题；[Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) |
| Kotschick, *Monopole Classes and Einstein Metrics*, IMRN 2004(12), 593–609；[原文](https://arxiv.org/abs/math/0306022) | special monopole 类及 Theorem 12 的类平方条件 | 原条件进入共同实际分析，短缺由额外项量化；[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) |
| Ishida–LeBrun, *Curvature, Connected Sums, and Seiberg–Witten Theory*；[原文](https://arxiv.org/abs/math/0111228) | BF 所检测的实际类、连通和曲率与 Einstein 障碍；Corollary 8、Theorem 9、Theorem D 等 | 连通和上的单极子解存在性用于线性估计及拓扑数分区；[Yau26_Line1_External_Review_20260927.md](../archive/originals/2026-09-27/Yau26_Line1_External_Review_20260927.md)，[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) |
| Ishida–Matsuo–Nakamura, *Yamabe Invariants and the Pin$^{-}(2)$-monopole Equations*, MRL 23(4) (2016)；[原文](https://arxiv.org/abs/1505.05948) | 扭曲单极子解存在性、Yamabe 与 Einstein 障碍及覆盖结构 | 扭曲解的双覆盖提升、积分同倍缩放及归一化不等式下降；[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §4 |
| Kotschick, *On regularly fibered complex surfaces* (1999), Theorem 3；[原文](https://arxiv.org/abs/math/9911255)；LeBrun, *Diffeomorphisms, symplectic forms and Kodaira fibrations* (2000)；[原文](https://arxiv.org/abs/math/0005195) | 双取向辛结构、实际类关系与经典严格签名不等式 | 同度量交叉配对加 FD2，形成统一正间隙；[Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md) §§2、6–9 |
| Catanese–Rollenske, *Double Kodaira fibrations*；[原文](https://arxiv.org/abs/math/0611428)；Catanese 综述 §1.3；[原文](https://arxiv.org/abs/1611.06617)；Polizzi, Remark 4.10；[原文](https://arxiv.org/abs/2002.01363) | Kodaira Chern 斜率能否任意逼近 3 的背景与明确问句 | 以 FD2 为前置推导斜率上界 $3-\varepsilon$，其中 $\varepsilon>0$ 与纤维化无关；最优斜率尚未确定；[00_All_Recent_Research.tex](../archive/originals/2026-10-07/00_All_Recent_Research.tex) 双取向章 |
| Anderson, *Canonical metrics on 3-manifolds and 4-manifolds*, Asian J. Math. 10 (2006), 127–163；[原文](https://arxiv.org/abs/math/0511034) | Theorem 4.10 的理想极小序列、轨形／开放／塌缩分支及能量关系 | 用于极小序列的分解；原手术类的标记对应、ALE 端修正及光滑取得性保留为后续命题；[O10_Low_Amplitude_Energy_and_O11_Scope.md](../archive/originals/2026-09-29/O10_Low_Amplitude_Energy_and_O11_Scope.md) §5，[Q3_Global_Attainment.tex](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) |
| Gursky–Viaclovsky, *Rigidity and stability of Einstein metrics for quadratic curvature functionals*；[原文](https://arxiv.org/abs/1105.4648) | 二次曲率泛函的临界性和稳定性 | 区分精确临界理论与近极小序列的弱变分选择；[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) |
| Armstrong, *Almost-Kähler Geometry* (1998), Theorem 2.2.4；[原文](https://johnarmstrongmaths.com/publications/resources/thesis.pdf)；*An ansatz for almost-Kähler, Einstein 4-manifolds*, J. Reine Angew. Math. 542 (2002), 53–84；[原文](https://doi.org/10.1515/crll.2002.009) | 闭情形的扭率零点拓扑与实际局部构造框架 | 零点正规形、完整延拓与非紧实例；[Q4_Torsion_Zero_Structure.tex](../archive/originals/2026-10-09/Q4_Torsion_Zero_Structure.tex)，[Q4_Complete_Example_and_Fino_Question.tex](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex) |
| Apostolov–Armstrong–Drăghici, *Local models and integrability of certain almost Kähler 4-manifolds*, Math. Ann. 323 (2002), 633–666；[原文](https://arxiv.org/abs/math/0109098) | 局部模型与所列 Gray 条件下的可积性 | 本项目规范正交命题在其所列条件下导出相应 Gray 条件，继而应用经典可积性定理；[Q4_Canonical_Orthogonality.tex](../archive/originals/2026-10-12/Q4_Canonical_Orthogonality.tex) |
| Derdziński, *Self-dual Kähler manifolds and Einstein manifolds of dimension four*, Compositio Math. 49 (1983), 405–433；[原文](https://archive.numdam.org/item/CM_1983__49_3_405_0/) | 四维 Einstein 的 Weyl 微分恒等式 | 组合零点 Hessian 恒等式与正势逆算子，得到行列式／Green 势条件；[Q4_Green_Potential_Rigidity.tex](../archive/originals/2026-10-14/Q4_Green_Potential_Rigidity.tex) |
| Di Scala–Nagy, *On the uniqueness of almost-Kähler structures*, C. R. Math. 348 (2010), 423–425；[原文](https://doi.org/10.1016/j.crma.2010.01.005) | 所列非零标量 Kähler–Einstein 度量的相容结构唯一性 | 处理固定度量调和乘积中已有平行形式的分支；[Q4_Harmonic_Product_Reduction.tex](../archive/originals/2026-10-13/Q4_Harmonic_Product_Reduction.tex) |
| Fino, *Almost Kähler 4-dimensional Lie groups with J-invariant Ricci tensor*, DGA 23 (2005), 26–37；[原文](https://doi.org/10.1016/j.difgeo.2005.03.003) | 已发表版 Corollary 2.1 后的非不变、非 Ricci-flat Einstein 严格几乎 Kähler 存在性问句 | 本项目给出定义于 $\mathbb R^4$ 的完备非不变 Einstein 严格几乎 Kähler 例子；闭流形的存在性另属 Goldberg 问题；[Q4_Complete_Example_and_Fino_Question.tex](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex) §§5–6 |

综述入口 Apostolov–Drăghici, *The curvature and the integrability of almost-Kähler manifolds*（[作者稿](https://arxiv.org/abs/math/0302152)）用于区分非负标量的经典刚性、负标量问题、局部模型与紧致条件。[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) 和完备非紧例子稿保留了其具体使用位置。

## 4. 后续命题

三组结论分别需要下列补充：

- 无密度端点：在 $\chi/A$ 无界时，同时证明第五幂线丛截面的正质量和完整弱方程，或构造满足全部输入的端点序列。
- 曲率极值：在全部竞争度量上证明与现有构造匹配的下界，并确定下确界是否由光滑度量取得。
- 闭负 Goldberg：由闭 Einstein–几乎 Kähler 条件推出所需全局可积性约束，例如上述扭率零点处的 Green 势符号。

各自条件、已得结论与源稿索引见 [间隙与端点](GAPS_AND_ENDPOINTS.md)、[曲率变分](CURVATURE_VARIATION.md)、[几乎 Kähler–Einstein 几何](GOLDBERG.md)；证明依赖见 [研究图谱](RESEARCH_MAP.md)。

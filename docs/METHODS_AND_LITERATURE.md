# 方法、文献与共同数学结构

本图谱按研究中的证明作用组织方法与文献：实际输入决定可以使用哪些方程，微分相容性产生全局约束，变分和构造判断约束的强度，极限分析与精确几何判断是否达到。来源是本仓库收录的原稿及其参考文献。

## 1. 共同问题：曲率数据能否同时实现

四维 Chern–Weil 恒等式联系标量曲率、两手性 Weyl 曲率与无迹 Ricci：
$$
4\pi^2(2\chi+3\tau)=\frac1{24}\int s^2+2\int|W^+|^2-\frac12\int|\operatorname{Ric}^{\circ}|^2.
$$
它约束积分数据。实际规范场与相容闭二形式进一步要求这些数据、曲率方向及其导数来自同一个度量和联络。研究的共同分析对象是这种联合可实现性，而不只是单个积分的数值界。

这一思想有两条具体实现。积分障碍分支利用实际 SW 解选定曲率模型，保留 Weitzenböck 与曲率预算中的误差，再以 Hessian、联络能量和弱 Bianchi 控制误差之间的关系。几乎 Kähler–Einstein 分支从实际闭形式出发，将扭率、规范曲率、Weyl 方程和拓扑零点关系同时保留。两条分支共享相容性问题，所需供给不同。

| 输入 | 它实际提供的数学信息 | 进入的分析 |
|---|---|---|
| 普通／special monopole 类 | 指定结构的实际解、Hodge 投影和类平方 | 单解参数、N1、I40/I41、端点 |
| Bauer–Furuta 连通和供给 | 普通数值不变量之外的实际单极子类 | 同一分析在已验证连通和范围的应用 |
| Pin$^{-}(2)$ 供给 | 扭曲实际解及双覆盖上的普通 SW 提升 | 覆盖兼容的归一化障碍 |
| 两取向的真实类及混合交叉积 | 同一 Hodge 分解中的联合投影限制 | FD2 的曲面丛、Kodaira 与配对推广 |
| 实际闭二形式 $\Omega$，$\vert \Omega\vert ^2=2$ | 相容几乎复结构、扭率和规范联络 | 闭负 Goldberg、规范正交和零点分析 |
| 真正近极小序列 | 对合法真实度量变分的全局比较 | 弱驻点、弱稳定、极小化与替换 |
| 完整插入单元及精确外领口 | 可复制的光滑竞争度量及总能量 | 严格上界、覆盖恢复与背景相互作用 |

实际供给不是分析结论的别名；一侧真实类的凸组合可以用于凸性预算，却不能直接替代必须求解场方程的真实类。来源：[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§1、4–6；[Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) 的配对定理。

## 2. 方法在证明中承担什么

| 方法 | 要处理的问题 | 原稿最强输出及其作用 | 接续所需信息 |
|---|---|---|---|
| 相容背景消去 | 非小背景是否导致强制估计丢失一个体积量 | I40/I41 控制 $\Sigma$ 与 $P+D_2$，建立线性窗口 | 在新的实际输入中重建背景作用与剩余联络控制 |
| 有界截面 Hessian 换指标 | 无统一坐标、Sobolev 控制时如何估计二阶量 | 只保留 Ricci 缩并、丛曲率和粗 Laplacian 的能量预算 | 负旋量丛仍含 $W^-$；其无界增长不能被省略 |
| 同场弱 Bianchi | 数值预算允许的 Weyl 模型是否来自真实度量 | 曲率与实际场微分之间的强制关系 | 用完整方程取得未被既有投影消去的新约束 |
| 慢梯度截断与强流 | 临界四次梯度如何通过退化极限 | 正旋量四次梯度一致可积，实际三次扭率强信息 | 不自动给负扭率所有高阶量一致可积 |
| 同丛 resolvent 与第五幂线丛 | 如何把退化扭率转成可作全局测试的对象 | 有界辅助截面、$L^5$ 非零质量、有限密度端点 | 无密度时同时保留第五线质量和完整弱方程 |
| 对数正则化与陈类局部化 | 拓扑平方能否全部隐藏在低幅度区域 | 有限 Dirichlet 预算下陈数密度消失，与实际预算矛盾 | 增长能量版本留下明确密度依赖 |
| 高精度近极小选择 | 无光滑极小元时能否合法使用变分约束 | 在临界测试预算中得到 $o(Q)$ 弱驻点和弱稳定 | 找到决定性下降方向或锐利全局补偿 |
| 完整拼接相互作用 | 标准手术费用是否最优 | 总能量负对数项、严格次四及一般负 KE 背景节省 | 将匹配下界作用于所有竞争几何 |
| 谐和通量与秩对齐 | 临界度量能否容许给定曲率组织 | 精确分解、真实下降方向及若干非 Einstein 临界点排除 | 取得性另需控制气泡、轨形与塌缩 |
| Weyl–Green 势与扭率零点 | 闭性怎样产生实际可积性 | 行列式符号及零点处 Green 势的充分刚性条件 | 证明一般闭候选必满足所需整体符号 |

前四项原始联系见 [00_Line1_Research_Atlas_20260928.md](../archive/originals/2026-09-28/00_Line1_Research_Atlas_20260928.md) §§1–3；强流与 Hessian 细节见 [O10_Strong_Current_Prerequisite.md](../archive/originals/2026-09-29/O10_Strong_Current_Prerequisite.md)。下列三组关系给出方法之间的实际连接。

### 2.1 强制估计、端点与双取向应用

$$
\Sigma\le C\{\Pi+\sqrt{\Pi Y}\},\qquad
\Pi=P+D_2,\quad Y=(T_+-a^2)_+
$$
控制同一度量上的联合变化。$\beta=8$ 的精确 Chern–Weil 对齐给 N1；保留类平方成本又给 $c/(1+Y/A)$ 的短缺版。$\beta=2$ 附近的精细机制与另一手性预算给线性阶。

端点采用不同的放大信息：
$$
\tau\in S^-\otimes L
\ \longrightarrow\ v\in S^-\otimes L
\ \longrightarrow\ \sigma=\Phi\wedge t(v)\in L^5.
$$
在固定有限密度下，$\sigma$ 具有近常正模长及 Dirichlet 预算。对数线丛方法要求 $c_1(L^5)^2/V\to0$，实际曲率却要求极限为 $25/(6\pi^2)$。另一条弱 CR–正势路线使用同一实际前置。

N1 与 FD 按地理关系分区，得到所列一般型手术族统一常数；FD 在单个固定 $B=2$ 的特例再与两个实际类的交叉配对结合，得到 Kodaira 斜率统一宽度。后者保留 **FD2**，不依赖一般无密度 O10，也不承担 FD2 的上游证明。

原稿：[O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md) §§2–5；[O10_Finite_Density_Fifth_Line.md](../archive/originals/2026-09-29/O10_Finite_Density_Fifth_Line.md)；[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §2；[Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md) §§1–7。

### 2.2 真实竞争几何与全局极值

对原平衡族，精确变分归约连接 $\alpha$ 与 $\inf P$。选择足够精确的近极小序列，使
$$
|DP[H]|=o(Q),\qquad D^2P[H,H]\ge-o(Q)
$$
对 $|H|_\infty\le1$、$\int(|\nabla^2H|^2+|\nabla H|^4)\le A$ 一致成立。这是对真实度量变化的约束；尚需用实际拓扑和方程构造一个决定性方向。

构造侧已改变标准上界：完整复双曲领口单元满足
$$
P(g_\epsilon)/(8\pi^2)=1-9\epsilon^2\log(1/\epsilon)+O_R(\epsilon^2),
$$
而一般负 KE 背景有相应张量展开。必须先固定正的节省，再作覆盖极限；对允许的闭流形族才保留严格首项改进。

谐和通量揭示哪些曲率组织可能成为临界点。例：
$$
DP_g[\operatorname{Ric}^{\circ}]
=\frac18\int|ds|^2-\frac12\int s|\operatorname{Ric}^{\circ}|^2
$$
在原稿所列闭 almost-Kähler、Ricci 为 $J$-不变的类别成立。非零常标量下得到真实下降方向；这限制候选，却不产生光滑全局极小元。

原稿：[02_O11_Variational_Selection.md](../archive/originals/2026-09-29/02_O11_Variational_Selection.md) §§2–3；[O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md)；[01_Research_Synthesis.tex](../archive/originals/2026-10-08/01_Research_Synthesis.tex) §3；[Q3_Descent_and_Flux_Equality.tex](../archive/originals/2026-10-08/Q3_Descent_and_Flux_Equality.tex)；[Q3_Harmonic_Rank_Rigidity.tex](../archive/originals/2026-10-08/Q3_Harmonic_Rank_Rigidity.tex)。

### 2.3 闭几何、零点与非局部刚性

闭负 Einstein–almost-Kähler 情形有扭率零点，但零点并不自动传播。令
$$
\mathcal R_+=W^+-aI/3,\quad A=-\mathcal R_+,\quad
L_a=\Delta+2a,\quad
\Psi=L_a^{-1}\det\mathcal R_+,\quad
\mathcal D=L_a^{-1}|\nabla A|^2.
$$
合并 Weyl 方程与零点结构，在每个扭率零点 $p$ 得到
$$
18\Psi(p)=\mathcal D(p)+\frac18|\nabla^2\Omega(p)|^2+\frac54|\eta(p)|^2.
$$
若一个零点有 $\Psi(p)\le0$，Green 核正性给刚性。一般候选是否必满足该条件仍是整体问题；谱重根相交只消去局部项，未消去 $\mathcal D$。

完备非紧严格例子说明局部方程确实容许非可积性。因此闭性必须通过全局配对、拓扑或势方程进入证明。规范正交和调和乘积是两个额外接口：前者利用全局闭反不变形式，后者保留正、迹一、秩一矩阵条件。

原稿：[Q4_Canonical_Orthogonality.tex](../archive/originals/2026-10-12/Q4_Canonical_Orthogonality.tex)；[Q4_Harmonic_Product_Reduction.tex](../archive/originals/2026-10-13/Q4_Harmonic_Product_Reduction.tex)；[Q4_Green_Potential_Rigidity.tex](../archive/originals/2026-10-14/Q4_Green_Potential_Rigidity.tex)；[Goldberg_Two_Conversations_Merged_20261015.tex](../research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)。

## 3. 主要文献的继承与本研究所接的环节

以下文献链接与定位取自所收原稿的参考文献。经典结果、本项目新增推导及外部问句承担不同作用。

| 文献 | 已有内容及本项目使用 | 原稿中的连接 |
|---|---|---|
| LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, Invent. Math. 145 (2001), 279–316；[原文](https://arxiv.org/abs/math/0003068) | 实际 SW 的锐利曲率预算、部分 Ricci 极值、等号和恢复构造；并非仅有 Einstein 非存在性 | N1/I41 比较临界强制与联合变化；低成本构造比较完整手术费用；[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md)，[Yau26_Line1_External_Review_20260927.md](../archive/originals/2026-09-27/Yau26_Line1_External_Review_20260927.md) |
| LeBrun, *Four-Manifolds, Curvature Bounds, and Convex Geometry*；[原文](https://arxiv.org/abs/math/0611450) | 单极子类凸包、投影优化和边界情形 | 一侧凸包的标量输入、完整普通类预算及 BF 完整预算的区别；[Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) |
| Kotschick, *Monopole Classes and Einstein Metrics*, IMRN 2004(12), 593–609；[原文](https://arxiv.org/abs/math/0306022) | special monopole 类及 Theorem 12 的类平方条件 | 原条件进入共同实际分析，短缺由额外项量化；[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) |
| Ishida–LeBrun, *Curvature, Connected Sums, and Seiberg–Witten Theory*；[原文](https://arxiv.org/abs/math/0111228) | BF 所检测的实际类、连通和曲率与 Einstein 障碍；Corollary 8、Theorem 9、Theorem D 等 | 已验证连通和供给进入线性窗口和地理分区；[Yau26_Line1_External_Review_20260927.md](../archive/originals/2026-09-27/Yau26_Line1_External_Review_20260927.md)，[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) |
| Ishida–Matsuo–Nakamura, *Yamabe Invariants and the Pin$^{-}(2)$-monopole Equations*, MRL 23(4) (2016)；[原文](https://arxiv.org/abs/1505.05948) | 扭曲规范供给、Yamabe 与 Einstein 障碍及覆盖结构 | 真实双覆盖提升、同倍缩放、归一化下降；[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §4 |
| Kotschick, *On regularly fibered complex surfaces* (1999), Theorem 3；[原文](https://arxiv.org/abs/math/9911255)；LeBrun, *Diffeomorphisms, symplectic forms and Kodaira fibrations* (2000)；[原文](https://arxiv.org/abs/math/0005195) | 双取向辛结构、实际类关系与经典严格签名不等式 | 同度量交叉配对加 FD2，形成统一正宽度；[Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md) §§2、6–9 |
| Catanese–Rollenske, *Double Kodaira fibrations*；[原文](https://arxiv.org/abs/math/0611428)；Catanese 综述 §1.3；[原文](https://arxiv.org/abs/1611.06617)；Polizzi, Remark 4.10；[原文](https://arxiv.org/abs/2002.01363) | Kodaira Chern 斜率能否任意逼近 3 的背景与明确问句 | FD2 依赖下的统一分离对应该问题，不计算最佳斜率；[00_All_Recent_Research.tex](../archive/originals/2026-10-07/00_All_Recent_Research.tex) 双取向章 |
| Anderson, *Canonical metrics on 3-manifolds and 4-manifolds*, Asian J. Math. 10 (2006), 127–163；[原文](https://arxiv.org/abs/math/0511034) | Theorem 4.10 的理想极小序列、轨形／开放／塌缩分支及能量关系 | 提供极小化框架；手术标记、ALE 端修正和光滑取得仍须另证；[O10_Low_Amplitude_Energy_and_O11_Scope.md](../archive/originals/2026-09-29/O10_Low_Amplitude_Energy_and_O11_Scope.md) §5，[Q3_Global_Attainment.tex](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) |
| Gursky–Viaclovsky, *Rigidity and stability of Einstein metrics for quadratic curvature functionals*；[原文](https://arxiv.org/abs/1105.4648) | 二次曲率泛函的临界性和稳定性 | 区分精确临界理论与近极小序列的弱变分选择；[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) |
| Armstrong, *Almost-Kähler Geometry* (1998), Theorem 2.2.4；[原文](https://johnarmstrongmaths.com/publications/resources/thesis.pdf)；*An ansatz for almost-Kähler, Einstein 4-manifolds*, J. Reine Angew. Math. 542 (2002), 53–84；[原文](https://doi.org/10.1515/crll.2002.009) | 闭情形的扭率零点拓扑与实际局部构造框架 | 零点正规形、完整延拓与非紧实例；[Q4_Torsion_Zero_Structure.tex](../archive/originals/2026-10-09/Q4_Torsion_Zero_Structure.tex)，[Q4_Complete_Example_and_Fino_Question.tex](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex) |
| Apostolov–Armstrong–Drăghici, *Local models and integrability of certain almost Kähler 4-manifolds*, Math. Ann. 323 (2002), 633–666；[原文](https://arxiv.org/abs/math/0109098) | 局部模型与所列 Gray 条件下的可积性 | 规范正交或额外条件完成后调用经典刚性；不是从任意负 Einstein 自动得到该条件；[Q4_Canonical_Orthogonality.tex](../archive/originals/2026-10-12/Q4_Canonical_Orthogonality.tex) |
| Derdziński, *Self-dual Kähler manifolds and Einstein manifolds of dimension four*, Compositio Math. 49 (1983), 405–433；[原文](https://archive.numdam.org/item/CM_1983__49_3_405_0/) | 四维 Einstein 的 Weyl 微分恒等式 | 组合零点 Hessian 恒等式与正势逆算子，得到行列式／Green 势条件；[Q4_Green_Potential_Rigidity.tex](../archive/originals/2026-10-14/Q4_Green_Potential_Rigidity.tex) |
| Di Scala–Nagy, *On the uniqueness of almost-Kähler structures*, C. R. Math. 348 (2010), 423–425；[原文](https://doi.org/10.1016/j.crma.2010.01.005) | 所列非零标量 Kähler–Einstein 度量的相容结构唯一性 | 处理固定度量调和乘积中已有平行形式的分支；[Q4_Harmonic_Product_Reduction.tex](../archive/originals/2026-10-13/Q4_Harmonic_Product_Reduction.tex) |
| Fino, *Almost Kähler 4-dimensional Lie groups with J-invariant Ricci tensor*, DGA 23 (2005), 26–37；[原文](https://doi.org/10.1016/j.difgeo.2005.03.003) | 已发表版 Corollary 2.1 后的非不变、非 Ricci-flat Einstein 严格 almost-Kähler 存在性问句 | 完备 $\mathbb R^4$ 例子给出对应；它不要求闭性，也不是闭负 Goldberg 的反例；[Q4_Complete_Example_and_Fino_Question.tex](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex) §§5–6 |

综述入口 Apostolov–Drăghici, *The curvature and the integrability of almost-Kähler manifolds*（[作者稿](https://arxiv.org/abs/math/0302152)）用于区分非负标量的经典刚性、负标量问题、局部模型与紧致条件。[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) 和完整非紧例子稿保留了其具体使用位置。

## 4. 研究接续的共同原则

最强结论不是把所有输入压成一个抽象名词，而是明确哪些实际信息能同时约束全部竞争几何。供给可以变化，分析机制可以推广；每次推广需体现为更自然的输入、更强的全局结论、真实构造或精确极限结构。

目前三项连接仍然分别决定更强结论：无密度端点中的实际集中与第五线质量；全部度量极值中的匹配下界与光滑取得；闭负 Goldberg 中扭率零点与全局 Green 势符号。已完成的地理统一、严格节省、双取向应用与非紧存在构造保持其各自结论，后续方法须与这些事实同时相容。

详细状态分别见 [间隙与端点](GAPS_AND_ENDPOINTS.md)、[曲率变分](CURVATURE_VARIATION.md)、[几乎 Kähler–Einstein 几何](GOLDBERG.md)；证明关系总览见 [研究图谱](RESEARCH_MAP.md)。

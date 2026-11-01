# 研究沿革与主要修正

整理日期：2026-11-01。

本记录按数学依赖与研究时间整理积分间隙、曲率极值、精确构造和负 Goldberg 分支。各命题的完整陈述及证明见所链接原稿；文献与材料范围见[方法与文献](METHODS_AND_LITERATURE.md)及[收录说明](COVERAGE.md)。

## 贯穿的问题

研究对象是四维 Einstein 几何的存在、逼近、曲率极值和附加几何结构的刚性。原积分间隙主干以实际规范场为输入，利用同一度量下场方程与曲率微分恒等式的相容性，对全部允许度量建立归一化 Einstein 障碍。上界构造、近极小几何与精确实现分别判断这些障碍的强度、适用边界和可达到性。

规范场的解存在性定理为相容性分析提供输入，所得估计推出积分障碍及应用；度量构造给出极值上界并揭示等号与退化的几何。几乎 Kähler–Einstein 构造和闭 Goldberg 刚性研究附加相容结构，采用独立的曲率方程与全局分析。

## 原积分间隙与参数分析

原归一化缺陷为

$$
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|^2}
{\lambda^2\operatorname{Vol}_g(M)}.
$$

后续以 $P=\int|\operatorname{Ric}^{\circ}|^2$、$R=\int|\operatorname{Ric}|^2$，以及 $R>0$ 时的 $\mathcal J=4P/R$ 表述无迹 Ricci 障碍。这里 $s$ 为标量曲率，积分使用相应度量的体积形式。令 $T=2\chi+3\tau$，$a$ 为所选 Spin$^c$ 结构行列式线丛的第一陈类，$p=(a_g^+)^2$ 为其自对偶调和投影的平方，$A>0$ 为 $p$ 的下界。N1 假设负 Yamabe 代表上存在相应未扰动 SW 解，且 $p\ge A$、$a^2\ge T$，得到

$$
\mathcal J(g)+\left(\frac{T}{A}-\frac23\right)_+\ge\varepsilon_0>0.
$$

参数泛函为

$$
D_\beta=(1+\beta^{-1})\int s^2+6(\beta+1)\int|W^+|^2-72\pi^2p.
$$

Weyl 项采用曲率算子范数。取 $\beta=8$，Chern–Weil 恒等式给出

$$
D_8=108\pi^2(T-2p/3)+\frac{27}{2}P.
$$

结合负 Yamabe 代表与原度量之间的精确共形比较，单解参数估计推出 N1；再由 $\mathcal E\ge\mathcal J$ 得到原积分间隙。

令 $\Sigma=\int s^2-32\pi^2p$。I40/I41 证明

$$
\Sigma\le C\{\Pi+\sqrt{\Pi Y}\},\qquad
\Pi=P+D_2,\quad Y=(T-a^2)_+.
$$

证明使用相容背景作用的消去、协变 Hessian 估计、联络能量控制及同场弱 Bianchi 恒等式。随后 [03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §5 另行保留有限参数的类平方短缺项，证明 N1 的短缺版

$$
\mathcal J(g)+(T/A-2/3)_+\ge c/(1+y),\qquad y=(T-a^2)_+/A.
$$

对 $y\le L_0<\infty$，这给出统一下界 $c/(1+L_0)$；关于无界 $y$ 的最优依赖仍未确定。

普通单极子、special monopole、Bauer–Furuta 和 Pin⁻ 理论分别提供解存在性结论。Pin⁻ 分支通过双覆盖将扭曲解提升为普通 SW 解，积分与类平方按覆盖次数缩放，归一化间隙下降到底空间。各应用采用相应非消失定理所保证的度量、结构与解的范围。

## O10：端点范围逐步扩大

原目标为 $\beta\ge2$ 时的统一积分端点估计，不预设点态 Ricci、直径、非塌缩或统一 Sobolev 控制。记 $V=\operatorname{Vol}_g(M)$、$r=V^{-1}\int|\operatorname{Ric}_g+g|^2$，则端点量为 $\kappa_\beta=r+D_\beta/V$；在 $s=-4$ 代表上，$r=P/V$。有限参数定理估计的是 $r+D_\beta/(\beta V)$。

主要推导依次为：

1. $\chi/A\le B<3/8$ 时，单解幅度估计与反手性 Weyl 能量非负性给出端点分离；原平衡族属于该范围。
2. 流估计、同丛预解算子及第一延拓，将剩余导数分量表示为第五张量幂线丛上的截面 $\sigma=\Phi\wedge t(v)\in L^5$。
3. 任意固定有限 $B$ 的版本有两种证明：一是弱 Cauchy–Riemann 关系与零阶项为 $10/3$ 的正算子，二是对数正则化、截断及陈数密度。二者共用实际场的先验估计。
4. 密度常数的定量下界先得到指数型估计，随后在相应原始缺陷的幂次换算下得到多项式型估计。各版本的误差定义和换算列于端点专题。
5. 不含反手性 Weyl 能量上界的逆幅度矩估计，证明辅助截面的梯度能量在模长趋零的区域一致消失；固定中间幅度层的集中仍待研究。

有限密度版本为

$$
\frac{\chi(M)}A\le B\quad\Longrightarrow\quad
\kappa_\beta\ge c(B)\frac{(\beta-2)^2}{\beta^2}.
$$

后续 [Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) 将 N1 与有限密度端点按拓扑数分区：若 $Q=A-T\ge0$、$\chi\le CA+Q$，则整族具有统一端点常数；它允许该族的 $\chi/A$ 无界，并适用于满足所列解存在性条件的一般型曲面吹起、添柄及相应多主体构造。

在一般允许范畴中，$\inf_{B<\infty}c(B)>0$ 及相反的闭流形逃逸构造均未确定。标量幅度矩与已用曲率投影容许中间幅度层的形式集中测度；剩余问题是这类集中能否满足完整场方程。

## O11：严格上界与匹配下界

原平衡族已有线性下界和标准恢复上界，手术参数满足 $Q=k+4\ell=Ah$。全曲率归约给出

$$
\alpha=4\rho+O(h^2),\qquad
\rho=\frac{\inf_gP(g)}{8\pi^2A},
$$

其中 $\alpha=\inf_g\mathcal E(g)$，$k$、$\ell$ 分别为吹起与连接柄的数目。临界测试范数下的近极小序列选择给出 $o(Q)$ 级近驻点与近稳定估计。

之后系统构造在适当覆盖族上将归一化首项上界严格降到 4 以下；后续一般负 Kähler–Einstein 背景与固定领口的解析构造进一步解释该节省。在背景归一化 $\operatorname{Ric}=-6g$ 下，以 $\varepsilon$ 表示原稿插入参数，局部构造的展开为

$$
\frac{P(g_\varepsilon)}{8\pi^2}
=1-9\varepsilon^2\log(1/\varepsilon)+O_{R_0}(\varepsilon^2).
$$

这里 $R_0$ 为固定领口半径，展开包含内核、颈部和外部过渡的积分。覆盖序列的适用范围随后扩大：[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) 处理预定嵌套残余塔；[O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) 用基底固定小领口处理固定紧复双曲主体的任意度数趋无穷的有限覆盖序列。两者分别固定局部构造后令覆盖度数趋于无穷。在所覆盖的平衡族上，$\limsup_j\alpha(M_j)/h_j$ 的上界严格小于 $4$；实际最优值及匹配下界仍未确定。

同场 Walsh 分解、度量变分与曲率补偿给出进一步必要条件。全局下界仍涉及手术类在 Anderson 极小序列极限中的分布，以及相对特征数公式中的端群与边界修正。完备 AE 核心的能量估计有其负定性与端部假设；Ricci 平坦的 Eguchi–Hanson 空间具有非平凡二循环而 $P=0$，说明一般 ALE 分支需要另行处理。

相应普通手术族的全部单极子类凸包估计已纳入比较；全部 BF 应用族的完整类集合仍需逐族确定。两类计算分别关系到新结论与经典障碍的比较范围。

## 两项外部问题的连接

### Kodaira 纤维化斜率

双取向稿以固定密度 $B=2$ 的 FD2 为前置，利用两实际辛规范类在同一 Hodge 极化下的交叉配对，陈述全曲面丛范畴的

$$
\mathcal J(g)+\left(1-\frac{3|\tau|}{\chi}\right)_+
\ge\varepsilon_{\mathrm{SB}}>0.
$$

对 Kodaira 纤维化的负 Kähler–Einstein 度量代入，得到
$c_1^2/c_2\le3-\varepsilon_{\mathrm{SB}}$，对应文献中斜率是否统一远离 $3$ 的问题。其前置为固定密度 FD2，无需一般无密度 O10 或 O11 的最优值；最佳斜率仍未确定。

10 月 8 日 [Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) 进一步将双取向间隙推广至一侧真实类的凸包与另一取向真实类，保留混合配对短缺项。FD2 始终作用于真实类；不要求凸组合本身有实际解。

### Fino 的非不变存在性问题

系统构造稿给出 $\mathbb R^4$ 上完备非紧严格几乎 Kähler 结构，满足

$$
\operatorname{Ric}=-3g,\qquad W^-=0,\qquad
d\Omega=0,\qquad |\Omega|^2=2,\qquad\nabla\Omega\ne0.
$$

构造源于系统 A01；后续稿补充曲率计算、光滑延拓、完备性与 Fino 期刊原问题的对应。Fino 2005 年期刊版 Corollary 2.1 后询问实四维 Lie 群上非不变、非 Ricci-flat 的 Einstein 严格几乎 Kähler 度量是否存在，并不要求底空间闭。将该结构拉回加法 Lie 群 $(\mathbb R^4,+)$，得到所询问的非不变、非 Ricci 平坦例子，并具有完备性。闭负 Goldberg 则要求紧致无边界的底空间。

## 四个问题与后续 Goldberg 研究

| 问题 | 现有结果 | 未解决部分 |
|---|---|---|
| 非极小一般型曲面的 Einstein 存在性 | 精确能量分解、Weyl 可行域反解、特定范围经典排除 | 一般小吹起范围的 Einstein 排除或存在 |
| 全曲率／无迹 Ricci 极值 | 严格低成本构造、完整共形 Kähler 类的分离、覆盖恢复 | 全部竞争度量的匹配下界与最优值 |
| 非 Bach-flat 光滑全局极小元 | Horikawa 单吹起的明确候选：经典正下界与新严格上界；Einstein 分支已排除 | 光滑全局达到性 |
| 闭四维负 Goldberg | 非紧精确例子、主符号与规范处理、扭率零点、Weyl 与 Green 势关系 | 一般闭情形的可积性证明或闭反例 |

第四题后续研究将扭率零集 $Z=\{\nabla\Omega=0\}$、Weyl 最大特征值的重根集 $\Sigma$、典范联络正交关系与 Green 势联系起来。设 $\operatorname{Ric}=-ag$、$a>0$，$\Omega$ 为相容闭二形式，$|\Omega|^2=2$，并采用非负 Laplace 算子 $\Delta=-\operatorname{div}\nabla$。定义

$$
\mathcal R_+=W^+-\frac a3I,\quad \mathsf A=-\mathcal R_+,\quad
U=\sigma_2(\mathsf A),\quad L=\Delta+2a,
\quad\Psi=L^{-1}\det\mathcal R_+,\quad
\mathcal D=L^{-1}|\nabla\mathsf A|^2.
$$

其中 $\sigma_2$ 为第二初等对称函数。令 $q=|\nabla\Omega|^2$、$t=s/6+q/4$、$\eta=W^+\Omega-t\Omega$。Einstein Weyl 方程给出 $U=\mathcal D-18\Psi$；在每个 $p\in Z$ 有

$$
18\Psi(p)=\mathcal D(p)+\frac18|\nabla^2\Omega|^2
+\frac54|\eta|^2.
$$

若存在 $p\in Z$ 使 $\Psi(p)\le0$，上式与 Green 核的严格正性推出 $\nabla\mathsf A\equiv0$，进而得到 $\nabla\Omega=0$。在 $Z\cap\Sigma$ 上有 $18\Psi=\mathcal D$；一般闭非 Kähler 候选须在每个扭率零点满足 $\Psi>0$。是否存在这样的闭候选仍未确定。

截至 10 月 16 日的研究记录包含上述条件性刚性定理、零点结构及完备非紧构造；一般闭负 Goldberg 仍为开放问题。

## 文件位置与研究交接顺序

下表列出主要版本及其用途。资料包的展开目录与全部来源见[来源索引](../catalog/README.md)。

| 时间 | 文件／资料包 | 用途 |
|---|---|---|
| 2026-09-27 | [Yau26_Line1_Recent_Research_20260927.zip](../archive/originals/2026-09-27/Yau26_Line1_Recent_Research_20260927.zip) | I40/I41、线性阶、零端、核心能量 |
| 2026-09-28 | [完整续研包](../archive/originals/2026-09-28/8f121eef-4045-4b73-a442-bccba42aa584.zip) | 本地原件已找回，并与仓库已有同字节资料包接通；原始名字保存在来源表 |
| 2026-09-28/29 | [Qiushi_Line1_Unified_Gap_20260928.md](../archive/originals/2026-09-28/Qiushi_Line1_Unified_Gap_20260928.md) 及对应回接稿 | N1 与旧积分障碍的继承 |
| 2026-09-29 | [20260929_Line1_Integrated_Manuscript.tex](../archive/originals/2026-09-29/27b3cef6-aeed-442c-9e66-fef1a757828e.tex) | 整月连续主稿及数学附录 |
| 2026-09-29/30 | `Line1_Web_Increment_20260929_30` | 有限密度端点、定量依赖、O11 变分及比较 |
| 2026-10-01 | [连续综合底稿](../research/server/codex/project/handoff/20261001_Line1_Integrated_Manuscript.tex) | 本地完整原件与模块化论文同时纳入 |
| 2026-10-07 | [20261007_Einstein_Gaps_Two_Sessions.zip](../archive/originals/2026-10-07/20261007_Einstein_Gaps_Two_Sessions.zip) | 两系统会话的原稿、程序、文献及综述 |
| 2026-10-07 | [Line1_All_Research_20261007.zip](../archive/originals/2026-10-07/Line1_All_Research_20261007.zip) | 网页续研总稿与十二分卷 |
| 2026-10-08 | `20261008_Einstein_Gaps_Four_Problems` | 四题主稿、原始数学记录与后续增量 |
| 2026-10-08 | [Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) / [Line1_Four_Problems_Direct_Work_20261008.zip](../archive/originals/2026-10-08/Line1_Four_Problems_Direct_Work_20261008.zip) | 共形 Kähler 分离、Horikawa 候选、主符号程序 |
| 2026-10-08 | [Q4_Complete_Example_and_Fino_Question.tex](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex) | 完备非紧构造与外部问题对应 |
| 2026-10-07 起 | [06_Two_Orientation_Global_Gap.tex](../archive/originals/2026-10-07/06_Two_Orientation_Global_Gap.tex) / [Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md) | 双取向及 Kodaira 应用，保留 FD2 前置 |
| 2026-10-09 | [Q4_Torsion_Zero_Structure.tex](../archive/originals/2026-10-09/Q4_Torsion_Zero_Structure.tex) | 扭率零集结构 |
| 2026-10-12 | [Q4_Canonical_Orthogonality.tex](../archive/originals/2026-10-12/Q4_Canonical_Orthogonality.tex) | 规范正交与相容性 |
| 2026-10-13 | [Q4_Harmonic_Product_Reduction.tex](../archive/originals/2026-10-13/Q4_Harmonic_Product_Reduction.tex) | 调和乘积归约 |
| 2026-10-13 | [Q4_Determinant_Sign_Rigidity.tex](../archive/originals/2026-10-13/Q4_Determinant_Sign_Rigidity.tex) | 行列式符号与刚性 |
| 2026-10-14 | [Q4_Green_Potential_Rigidity.tex](../archive/originals/2026-10-14/Q4_Green_Potential_Rigidity.tex) | Green 势条件及剩余符号问题 |
| 2026-10-15 | [Goldberg_Global_Connections_20261015.tex](../archive/originals/2026-10-15/Goldberg_Global_Connections_20261015.tex) | 全局联系 |
| 2026-10-15 | [Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex](../archive/originals/2026-10-15/Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex) | 零点与 Weyl 方程 |
| 2026-10-15 | [Goldberg_Two_Conversations_Merged_20261015.zip](../archive/originals/2026-10-15/Goldberg_Two_Conversations_Merged_20261015.zip) | 两会话后期研究合并 |

## 本服务器原研究与后续接续

本次将早期三会话各100步、A01的95步、A02的108步以及两个会话组的数学交流接回原稿；Codex工程保留86个历史工作树中的独特数学版本、661条独特科研最终回复与214条研究提交记录。目录见[服务器研究入口](../research/server/README.md)。

后期新增联系包括：一般背景的完整 Burns 插入、配对 $A_1$ 轨形的精确曲率极值与非取得、负 AKE 非塌缩极限中的自对偶能量无集中、Wahl 实际场与指标转移、Einstein 域补区域的手性费用。许可 SW 高阶零点可以形式补全，说明原先依赖有限阶可解性矛盾的路线没有获得所需全局障碍。详见两会话导览及相应专题。

10月31日的[两项公开问题比较](../research/server/codex/project/continuation/20261031_Kodaira_Fino_Literature_and_Proof_Status.md)补充了实际证明阅读和精确计算：Fino构造的曲率程序已运行，光滑延拓、完备性和非齐性已检查；Kodaira应用及有限密度关键链未发现所检查部分的实质错误，全部上游旋量分量尚未完成一次独立重建。该记录没有确立任一结果的历史首答地位。

## 主要修正

- **经典比较。** LeBrun 等经典理论已有定量曲率下界、部分精确极值及等号研究。本项目的比较集中于参数临界处的统一分离、线性强制、退化端点和新的构造上界。
- **端点量词。** 任意固定有限 $B$ 的定理、特定拓扑关系下的整族统一定理、完全无密度条件的命题分别陈述。
- **构造修正。** 严格次四上界已改变所覆盖平衡族的候选最优值；其余族保留各自的构造条件与下界问题。
- **泛函比较。** Step 44 的双向比较已由后续稿订正；$P$、$\mathcal E$ 和局部残差积分分别保留。仍有效的独立结论与修正位置列于[曲率变分](CURVATURE_VARIATION.md)。
- **填充证书。** A02早期ACH/Rossi填充的Fuchs余项证书存在分量顺序与余项界错误，尚未找到修复；它不影响独立的严格次四构造或显式Fino例。
- **退化排除。** A02 Step104的cusp基本群排除和实际字符指定已由105–106撤回；Wahl、棱柱端和塌缩补域分别保留各自条件。
- **几何范畴。** 有限阶形式解、局部精确解、完备非紧解和闭流形解分别记述。Fino 的存在性回答属于完备非紧范畴；Goldberg 的剩余问题属于闭流形范畴。

## 当前未解决的问题

一般无密度端点需要确定过渡幅度集中与完整场方程的相容性；曲率极值需要全部竞争度量的匹配下界及光滑取得性；固定流形的 Einstein 存在性与闭负 Goldberg 需要相应整体几何条件或反例构造。具体假设和目标分别列于[间隙与端点](GAPS_AND_ENDPOINTS.md)、[曲率变分](CURVATURE_VARIATION.md)、[构造与实现](CONSTRUCTIONS_AND_REALIZATION.md)及[几乎 Kähler–Einstein 几何](GOLDBERG.md)。

10 月 16 日的研究讨论进一步明确了各分支的关系：Kodaira 斜率是积分间隙的应用，Fino 非紧例子属于精确实现，闭负 Goldberg 研究 Einstein 度量上的相容辛结构。三者围绕存在、逼近与刚性组织，但采用各自的证明链。

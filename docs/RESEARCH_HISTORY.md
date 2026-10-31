# 研究沿革与会话继承

整理日期：2026-10-31。

本记录依据研究原稿、过程记录、可见会话内容及跨会话检索片段整理。材料涉及《Yau 26 23 19 等问题》及后续几何分析、Einstein Gaps 与负 Goldberg 研究；尚不能将所有文件唯一分配给某一个网页会话，也未取得这些会话的完整逐字导出。数学命题以对应原稿的完整假设和证明为准。

## 贯穿的问题

研究对象是四维 Einstein 几何的存在、逼近、曲率极值和附加几何结构的刚性。原积分间隙主干以实际规范场为输入，利用同一度量下场方程与曲率微分恒等式的相容性，对全部允许度量建立归一化 Einstein 障碍。上界构造、近极小几何与精确实现分别判断这些障碍的强度、适用边界和可达到性。

统一性依靠明确的证明联系：规范供给进入共同分析；共同分析推出积分障碍及应用；真实构造检验锐利性。精确几乎 Kähler–Einstein 构造与闭 Goldberg 刚性相互检验，但尚未成为原 gap 定理的一条完整推论。

## 原积分间隙与参数分析

原归一化缺陷为


$$
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|^2}
{\lambda^2\operatorname{Vol}_g(M)}.
$$


后续以 $P=\int|\operatorname{Ric}^{\circ}|^2$、$R=\int|\operatorname{Ric}|^2$、$\mathcal J=4P/R$ 表述无迹 Ricci 障碍。N1 在其负 Yamabe、实际单解、正预算及类平方条件下陈述


$$
\mathcal J(g)+\left(\frac{T}{A}-\frac23\right)_+\ge\varepsilon_0>0.
$$


有限参数分析在 $\beta=8$ 与 Chern–Weil 组合对齐：


$$
D_8=108\pi^2(T-2p/3)+\frac{27}{2}P.
$$


负 Yamabe 代表与原度量之间有精确共形比较。这条连接将原积分 gap 接回单解参数理论，而非仅将新旧结论并列存放。

I40/I41 的进一步输入是


$$
\Sigma\le C\{\Pi+\sqrt{\Pi Y}\},\qquad
\Pi=P+D_2,\quad Y=(T-a^2)_+.
$$


其中校准背景消去、Hessian 预算、剩余联络能量及同场弱 Bianchi 测试承担主要分析。随后 [03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §5 另行保留有限参数的类平方成本，证明 N1 的短缺版

$$
\mathcal J(g)+(T/A-2/3)_+\ge c/(1+y),\qquad y=(T-a^2)_+/A.
$$

因此，有界短缺范围已有直接继承证明；短缺无界时的无损常数与最佳依赖仍未确定。

普通单极子、special monopole、Bauer–Furuta、Pin⁻ 对应的是不同实际供给。Pin⁻ 的覆盖提升与归一化下降已有专门兼容关系。各分支必须沿其原始量词继承，不能把某一分支的单解削弱自动赋予全部输入。

## O10：端点范围逐步扩大

原目标为 $\beta\ge2$ 时的统一弱积分端点估计，且不预设点态 Ricci、直径、非塌缩或统一 Sobolev 控制。有限参数量 $r+D_\beta/(\beta V)$ 与端点量 $\kappa_\beta=r+D_\beta/V$ 不同，不能混用。

可见研究轨迹如下：

1. $\chi/A\le B<3/8$ 的版本由单解幅度预算和另一手性 Weyl 非负性闭合；原平衡族处于该范围内。
2. 强流估计、同丛 resolvent、第一延拓将剩余导数转为第五幂线丛上的截面 $\sigma=\Phi\wedge t(v)\in L^5$。
3. 任意固定有限 $B$ 的版本在稿件中获得两条矛盾路线：弱 CR 关系与 $10/3$ 正势；对数正则化、线丛截断与陈数密度矛盾。两条路线共享上游实际场估计，不计为两个独立主定理。
4. 随后稿件记录指数型、再到某个多项式型的密度依赖。不同稿中的误差量必须先换算，不能只因同名 $\eta$ 就比较强弱。
5. 无密度的低幅度估计排除了梯度能量全部集中到模长趋零的最深区域；固定中间幅度层的径向集中仍未被排除。

有限密度版本为


$$
\frac{\chi(M)}A\le B\quad\Longrightarrow\quad
\kappa_\beta\ge c(B)\frac{(\beta-2)^2}{\beta^2}.
$$


后续 [Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) 将 N1 与有限密度端点按地理参数分区：若 $Q=A-T\ge0$、$\chi\le CA+Q$，则整族具有统一端点常数；它允许该族的 $\chi/A$ 无界，并覆盖实际供给已验证的一般型吹起、添柄及相应多主体范畴。

一般实际供给范畴仍没有得到 $\inf_{B<\infty}c(B)>0$，也没有满足全部原输入的闭流形逃逸反例。标量幅度矩、逆幅度矩和若干正曲率投影仍允许形式集中测度；继续组合这些已用预算不能自动结束一般 O10。

## O11：由候选系数 4 转向严格节省与匹配下界

原平衡族已有线性阶及标准恢复上界；$Q=Ah$。全曲率归约把相应最优问题连接到 $\inf P$，并有 $\alpha=4\rho+O(h^2)$。临界测试范数下的真正近极小、近驻点和近稳定选择已经建立，误差需控制在 $o(Q)$ 尺度。

之后系统构造在适当覆盖族上将归一化首项上界严格降到 4 以下；后续一般负 Kähler–Einstein 背景与固定领口的解析构造进一步解释该节省。一个记录中的展开为


$$
\frac{P(g_\varepsilon)}{8\pi^2}
=1-9\varepsilon^2\log(1/\varepsilon)+O_R(\varepsilon^2).
$$


内核、颈部和外部过渡均需计入。覆盖量词随后已有明确加强：[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) 处理预定嵌套残余塔；[O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) 用基底固定小领口处理固定紧复双曲主体的任意度数趋无穷的有限覆盖序列。两条结论分别保留其准确输入和极限次序。因此，系数 4 已不能作为所有后续构造范围内必须证明的答案；未知目标是实际最优值及匹配下界。

同场 Walsh 分解、合法变分和曲率补偿为下界提供输入，但尚未决定全部竞争度量的最优首项。Anderson 极小序列理论不自动识别全部手术标记；AE 完整核心费用不适用于所有 ALE 气泡。Ricci-flat 的 Eguchi–Hanson 例子说明不能按每个二周期统一计算正的无迹 Ricci 费用。

完整普通单极子类预算与全部 BF 应用族的完整预算不同。前者的特定计算不能自动解决后者，相关原创性比较应按流形族分别保留。

## 两项外部问题的连接

### Kodaira 纤维化斜率

双取向稿以固定密度 $B=2$ 的 FD2 为前置，利用两实际辛规范类在同一 Hodge 极化下的交叉配对，陈述全曲面丛范畴的


$$
\mathcal J(g)+\left(1-\frac{3|\tau|}{\chi}\right)_+
\ge\varepsilon_{\mathrm{SB}}>0.
$$


对 Kodaira 纤维化的负 Kähler–Einstein 度量代入，得到
$c_1^2/c_2\le3-\varepsilon_{\mathrm{SB}}$，对应文献中整个范畴是否统一远离 3 的问题。此应用不需要无密度 O10，也不需要 O11 的最佳值。其证明依赖 FD2，应用本身不能反向认证 FD2 上游分析；也没有由此确定最佳斜率或证明 $8/3$ 最优。

### Fino 的非不变存在性问题

系统构造稿给出 $\mathbb R^4$ 上完整非紧严格几乎 Kähler 结构，满足


$$
\operatorname{Ric}=-3g,\qquad W^-=0,\qquad
d\Omega=0,\qquad |\Omega|^2=2,\qquad\nabla\Omega\ne0.
$$


构造源于系统 A01；后续稿补充曲率计算、光滑延拓、完备性与 Fino 期刊原问题的对应。Fino 2005 年期刊版 Corollary 2.1 后询问实四维 Lie 群上非不变、非 Ricci-flat 的 Einstein 严格几乎 Kähler 度量是否存在，并不要求底空间闭。完整例子对应这一存在性问题，不能据此称闭负 Goldberg 已被证伪；存在性回答与历史首创性也不是同一判断。

10 月 8 日 [Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) 进一步将双取向间隙推广至一侧真实类的凸包与另一取向真实类，保留混合配对短缺项。FD2 始终作用于真实类；不要求凸组合本身有实际解。

## 四个问题与后续 Goldberg 研究

| 问题 | 可见记录中的进展 | 最后仍缺的结论 |
|---|---|---|
| 非极小一般型曲面的 Einstein 存在性 | 精确能量分解、Weyl 可行域反解、特定范围经典排除 | 一般小吹起范围的 Einstein 排除或存在 |
| 全曲率／无迹 Ricci 极值 | 严格低成本构造、完整共形 Kähler 类的分离、覆盖恢复 | 全部竞争度量的匹配下界与最优值 |
| 非 Bach-flat 光滑全局极小元 | Horikawa 单吹起的明确候选：经典正下界与新严格上界；Einstein 分支已排除 | 光滑全局达到性 |
| 闭四维负 Goldberg | 非紧精确例子、主符号与规范处理、扭率零点、Weyl 与 Green 势关系 | 一般闭情形的可积性证明或闭反例 |

第四题最近材料把扭率零集 $Z$、Weyl 最大特征值重根集 $\Sigma$、规范正交与 Green 势联系起来。在 $\operatorname{Ric}=-ag$、$a>0$ 下，稿中记


$$
\mathsf A=-\left(W^+-\frac a3I\right),\quad
U=\sigma_2(\mathsf A),\quad L=\Delta+2a,
\quad\Psi=L^{-1}\det R_+,\quad
\mathcal D=L^{-1}|\nabla\mathsf A|^2.
$$


相应恒等式为 $U=\mathcal D-18\Psi$。在扭率零点有


$$
18\Psi(p)=\mathcal D(p)+\frac18|\nabla^2\Omega|^2
+\frac54|\eta|^2.
$$


若在某个零点取得稿件要求的 Green 势非正条件，可推出刚性；尚未证明每个闭候选都满足这个符号条件。即使得到 $Z\cap\Sigma\ne\varnothing$，交点处也只是 $18\Psi=\mathcal D$，没有自动推出 $\mathcal D=0$。零点相交与全局可积之间的这一步不得略去。

非紧实际例子说明，纯点态负 Einstein 公式不足以排除严格非可积性。后续证明需要闭性提供的全局约束。当前可见记录截至 10 月 16 日仍将一般闭负 Goldberg 列为开放目标。

## 文件位置与研究交接顺序

以下保留交接过程中出现的文件名。可定位原件直接链接；未取得的历史文件名仅作线索，完整收录情况见 [来源目录](../catalog/sources.json)。

| 时间 | 文件／资料包 | 用途 |
|---|---|---|
| 2026-09-27 | [Yau26_Line1_Recent_Research_20260927.zip](../archive/originals/2026-09-27/Yau26_Line1_Recent_Research_20260927.zip) | I40/I41、线性阶、零端、核心费用 |
| 2026-09-28 | `Yau26_Line1_Full_Continuation_20260928.zip` | 历史包名线索；本次未定位同名独立 ZIP，续研内容按现存原稿与包内目录索引 |
| 2026-09-28/29 | [Qiushi_Line1_Unified_Gap_20260928.md](../archive/originals/2026-09-28/Qiushi_Line1_Unified_Gap_20260928.md) 及对应回接稿 | N1 与旧积分障碍的继承 |
| 2026-09-29 | [20260929_Line1_Integrated_Manuscript.tex](../archive/originals/2026-09-29/27b3cef6-aeed-442c-9e66-fef1a757828e.tex) | 整月连续主稿及数学附录 |
| 2026-09-29/30 | `Line1_Web_Increment_20260929_30` | 有限密度端点、定量依赖、O11 变分及比较 |
| 2026-10-01 | `20261001_Line1_Integrated_Manuscript.tex` | 历史记录中的后续综合底稿；本次未定位该独立文件，不能将其他整合稿改名代替 |
| 2026-10-07 | [20261007_Einstein_Gaps_Two_Sessions.zip](../archive/originals/2026-10-07/20261007_Einstein_Gaps_Two_Sessions.zip) | 两系统会话的原稿、程序、文献及综述 |
| 2026-10-07 | [Line1_All_Research_20261007.zip](../archive/originals/2026-10-07/Line1_All_Research_20261007.zip) | 网页续研总稿与十二分卷 |
| 2026-10-08 | `20261008_Einstein_Gaps_Four_Problems` | 四题主稿、原始数学记录与后续增量 |
| 2026-10-08 | [Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) / [Line1_Four_Problems_Direct_Work_20261008.zip](../archive/originals/2026-10-08/Line1_Four_Problems_Direct_Work_20261008.zip) | 共形 Kähler 分离、Horikawa 候选、主符号程序 |
| 2026-10-08 | [Q4_Complete_Example_and_Fino_Question.tex](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex) | 完整非紧构造与外部问题对应 |
| 2026-10-07 起 | [06_Two_Orientation_Global_Gap.tex](../archive/originals/2026-10-07/06_Two_Orientation_Global_Gap.tex) / [Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md) | 双取向及 Kodaira 应用，保留 FD2 前置 |
| 2026-10-15 | [Q4_Torsion_Zero_Structure.tex](../archive/originals/2026-10-09/Q4_Torsion_Zero_Structure.tex) | 扭率零集结构 |
| 2026-10-15 | [Q4_Canonical_Orthogonality.tex](../archive/originals/2026-10-12/Q4_Canonical_Orthogonality.tex) | 规范正交与相容性 |
| 2026-10-15 | [Q4_Harmonic_Product_Reduction.tex](../archive/originals/2026-10-13/Q4_Harmonic_Product_Reduction.tex) | 调和乘积归约 |
| 2026-10-15 | [Q4_Determinant_Sign_Rigidity.tex](../archive/originals/2026-10-13/Q4_Determinant_Sign_Rigidity.tex) | 行列式符号与刚性 |
| 2026-10-15 | [Q4_Green_Potential_Rigidity.tex](../archive/originals/2026-10-14/Q4_Green_Potential_Rigidity.tex) | Green 势条件及剩余符号问题 |
| 2026-10-15 | [Goldberg_Global_Connections_20261015.tex](../archive/originals/2026-10-15/Goldberg_Global_Connections_20261015.tex) | 全局联系 |
| 2026-10-15 | [Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex](../archive/originals/2026-10-15/Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex) | 零点与 Weyl 方程 |
| 2026-10-15 | [Goldberg_Two_Conversations_Merged_20261015.zip](../archive/originals/2026-10-15/Goldberg_Two_Conversations_Merged_20261015.zip) | 两会话后期研究合并 |

## 必须继承的修正

- LeBrun 等经典理论已经具有定量曲率下界、部分精确极值和等号研究；不能把“首次发现曲率 gap 或首次同时研究上下界”作为整个项目的原创性表述。
- 有限密度 O10 与完全无密度 O10 的量词不同；前者不能每轮重新记为未完成，也不能被扩大为后者。
- 对已覆盖的严格次四构造族，标准首项 4 已不再是正确的待证最优答案；其他流形族应保留原量词。
- Step 44 双向比较的错误及有效独立结论需按后续订正保留；不同泛函 $P$、$\mathcal E$、局部费用不能相互代替。
- 几何局部核心、完整非紧空间与闭流形是不同范畴；有限阶形式计算也不等于实际局部解或闭解。
- 两个外部问题的回答分别依靠 FD2 应用链和实际非紧构造；闭 Goldberg 未解不使前两条链自动失效。
- 论文完成以已声明且有完整证明的定理为准；不能要求解决全部相关公开问题才允许已有成果成文。

## 后续接续

按原稿逐项继承证明，将已完成的有限密度端点、严格上界构造、双取向应用与非紧实现放在各自准确范围中。无密度 O10 仍需要处理完整实际系统中的过渡幅度集中；曲率极值仍需要全部竞争度量的匹配下界；闭负 Goldberg 仍需要将闭性转化为足以结束可积性证明的全局信息。任一新方法均可使用，完成标准是改变这些明确结论，而非增加同一目标的等价改写。

## 10月16日的主旨澄清

历史会话检索保留的10月16日说明，将共同问题表述为“拓扑与相容几何结构决定四维 Einstein 度量的存在、逼近及刚性”。Kodaira 斜率是积分间隙机制的直接应用，Fino 非紧例子属于精确实现及适用边界，闭负 Goldberg 研究 Einstein 度量上的附加相容结构。三者可以形成连续研究，但尚不是同一条已证定理的三个直接推论。这是研究组织的澄清，未增加一项新的猜想解答。

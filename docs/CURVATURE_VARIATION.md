# 曲率变分、低成本构造与全局取得性

本导引按证明关系串联已经汇入的原稿；公式的假设以所引章节为准。全文证明、构造程序及历史版本保存在来源文件中，本导引不替代它们。

## 1. 三个相关但不同的极值对象

在闭四维流形上记

$$
P=\int|\operatorname{Ric}^{\circ}|^2,\quad S=\int s^2,\quad
R=P+S/4,\quad V=\operatorname{Vol},\quad T_s=\int s.
$$

研究同时涉及

$$
P_*(M)=\inf_gP(g),\qquad
\alpha(M)=\inf_g\mathcal E(g),\qquad
\mathcal E=4-\frac{T_s^2}{VR}
=\frac{4P}{R}+\frac{S-T_s^2/V}{R}\quad(R>0).
$$

曲率算子范数下，$\int|\operatorname{Rm}_{\rm op}|^2=8\pi^2\chi+P$，所以固定流形上的全曲率极小化与 $P$ 极小化相同；归一化泛函 $\mathcal E$ 则另有标量和分母。其定义要求 $\lambda\ne0$，故 Ricci-flat 度量的 $\mathcal E$ 值为 4，不能直接指定为 0。

来源：[03_Subsequent_Mathematical_Developments(1).tex](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §1；较早同名文件应按内部覆盖的 Step 范围识别版本。

## 2. O11 已经发生的实质变化：标准费用并非最优

### 2.1 从有限尺度证书到任意固定复双曲领口

系统两会话首先得到完整光滑单元的严格区间证书及适当覆盖族上的严格次四上界。后续解析构造给出：每个固定半径 $R_0>0$ 的复双曲领口内，都存在普通负单吹起单元，在外部精确等于 $\operatorname{Ric}=-6g$，并满足

$$
\frac{P(g_\epsilon)}{8\pi^2}
=\frac{\int|\operatorname{Ric}_{g_\epsilon}+6g_\epsilon|^2}{8\pi^2}
+O_{R_0}(\epsilon^2)
=1-9\epsilon^2\log(1/\epsilon)+O_{R_0}(\epsilon^2).
$$

更准确地说，两个泛函各自具有上述同一主项。普通 Burns 核心、颈部、外过渡全部计入；内外两过渡的总误差为 $O_{R_0}(\epsilon^2)$。负对数项因此给出真正严格节省，而非只计算中间区域。

来源：[O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) §§0–6。其 §8 指向系统 A01 Step10、A02 Step11、[theorem_package_v1.md](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md) 和原颈部符号程序，保留了发现与后续接续的来源区别。

### 2.2 覆盖量词和极限次序

对固定紧复双曲曲面 $X_0$ 的任意有限非分歧覆盖序列 $X_j\to X_0$，只要度数趋于无穷，原平衡比例

$$
Q_j=k_j+4\ell_j,\quad h_j=Q_j/A_j\to0,\quad
k_j/Q_j\to2/9,\quad\ell_j/Q_j\to7/36
$$

便允许复制适合基底小嵌入球的固定单元，得到

$$
\limsup_j\frac{\alpha(M_j)}{h_j}
\le4-\frac89\delta_{X_0}<4.
$$

先固定领口，再固定一个足够小但正的插入参数，最后令覆盖度数趋于无穷。若同时令插入参数趋零，严格首项节省可能随之消失。

另一路使用一个已有固定半径单元：对于事先给定、嵌套且子群交集平凡的残余覆盖塔，某一级以后具有正比例的该单元安放位置。不要求正规塔，也不要求全局单射半径处处趋于无穷。在该量词下，既有区间证书与共形尾部恢复给出

$$
\limsup_j\alpha(M_j)/h_j\le3.9961446513521015108\ldots<4.
$$

这条数值证书与任意固定小领口的解析结论是互补入口。

来源：[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §§3–5；任意固定基底覆盖序列的扩展见 [O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) §6。

稳定混合单元费用 $\gamma_{\rm bal}$ 的 Fekete 极限提供相应闭流形序列的上界；它与全度量最优首项相等仍需要反向局部化或直接全局下界。不能将单元极小值的存在误写为闭流形最优值已求出。

### 2.3 一般背景的张量机制

10 月 8 日主稿将特殊复双曲构造推进到一般负 Kähler–Einstein 背景。对完整插入支撑邻域内的 $P$-临界背景、固定方向和固定角修正，原稿给出

$$
P(g_\epsilon)=P(g)+8\pi^2-8\pi^2\epsilon R^+_p(\zeta,\zeta)
 +4\pi^2\Phi\epsilon^2\log(1/\epsilon)+O(\epsilon^2).
$$

当 $\operatorname{Ric}^{\circ}_p=0$、$R^+\zeta=\mu\zeta$ 时，优化系数为

$$
\Phi=-\mu(\mu-s/8)-|T|^2,\qquad
T=(R^+|_{\zeta^\perp})^{\circ}.
$$

角修正使反手性 Weyl 二阶背景项在目标曲率组合 $(2W^+,s/\sqrt{12})$ 中消去。核方向上的负对数项为 $-4\pi^2|T|^2\epsilon^2\log(1/\epsilon)$。在负 KE 背景的垂直方向，$|T|^2=s^2/32$，故固定 $k$ 个点的构造满足

$$
\frac{P(\widetilde g_\epsilon)}{8\pi^2}
=k-\frac{ks^2}{64}\epsilon^2\log(1/\epsilon)+O(\epsilon^2)<k.
$$

原稿还通过先固定节省、再缩小 ADE 解消尺度，将上界传至所述极小一般型曲面。

必须保留两项修正：系数并非在整个 $R^+\le0$ 锥上非正；非特征向量方向的角修正有额外旋转零模。固定光滑背景的余项也没有自动给出任意退化背景族的一致余项。

来源：[01_Research_Synthesis.tex](../archive/originals/2026-10-08/01_Research_Synthesis.tex) §3，尤其 A01.52、A02.59D 的修正版及 §3.5。

## 3. 全局竞争类别与归一化结论

对 $M=X\#k\overline{\mathbb{CP}}^{\,2}$、$A=c_1^2(X)>0$，若经典全度量标量预算为 $S\ge32\pi^2A$，则对原取向上任意复结构的 Kähler 度量 $h$ 及 $g=u^2h$，有

$$
P(g)-8\pi^2k
=\frac{S(g)-32\pi^2A}{12}
 +\frac{S(h)-32\pi^2A}{6}\ge0.
$$

所以已有严格上界不仅离开原复结构的 Kähler 类，也低于整个原取向全局共形 Kähler 类。相反取向的扩展还须保留原稿签名条件。

来源：[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §2。

同一负 Yamabe 类中的最小代表不增加 $P$。在统一标量预算下，归一化上界为

$$
\alpha(M)\le\frac{4\mathfrak p_*(M)}{A+\mathfrak p_*(M)},
\qquad\mathfrak p_*=P_*/(8\pi^2),
$$

由严格插入得到 $\alpha(X\#k\overline{\mathbb{CP}}^{\,2})<4k/(A+k)$。这不等于算出了 $P_*$，也不确定小 $k/A$ 的精确尺度。

更一般的归一化成果不应漏掉：长圆柱构造给每个闭四维流形 $0\le\alpha\le1$；若 $2\chi-3|\tau|\le0$，则 $\alpha=1$，严格负时不取得。令

$$
d([g])=8\pi^2\chi-\int|W|^2,
$$

则原稿给出不需规范场供给的全局共形表达式

$$
\alpha(M)=1-6\sup\left(\{0\}\cup
\left\{\frac{d([g])}{Y([g])^2/3-2d([g])}:d([g])>0\right\}\right),
$$

以及 $\alpha<1\iff\inf_g\int|W|^2<8\pi^2\chi$。这是联合 Weyl–Yamabe 极值刻画，尚未在全部目标吹起族上计算该上确界。

来源：[03_Subsequent_Mathematical_Developments(1).tex](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §§5–6。

## 4. Q1 与 Q3：精确 Einstein 候选和光滑全局极小元

Q1 的未决小吹起范围不能靠重新组合经典预算排除。[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §3 精确反解了经典可行区：在 $0<k<A/3$ 时，Einstein 候选必须使 Weyl 缺额

$$
\kappa\ge k+\frac{k^2}{A(1+\sqrt{1-3k/A})^2}>k.
$$

仍需 Einstein 方程本身产生的新增限制，或真实 Einstein 构造；此处 $\kappa$ 不是 O10 缺陷。

Q3 询问闭光滑流形上的全局 $P$ 极小值是否可由非 Bach-flat 光滑度量取得。原稿提出两种明确候选：Horikawa 单吹起和 Godeaux 单吹起，均具有

$$
16\pi^2/3\le P_*<8\pi^2.
$$

经典预算已排除 Einstein；若取得，则负 Yamabe 性、$P$-临界性和变分关系保证极小元非 Bach-flat。尚缺的是光滑取得性本身。

来源：[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §4 的 Horikawa 例；[Q3_Global_Attainment.tex](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) §1 的 Fermat 商 Godeaux 例。它们是不同的候选，不应混成同一个曲面。

### 4.1 谐和通量与真实下降方向

[03_Subsequent_Mathematical_Developments(1).tex](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §3 给出

$$
p=q^2(1-\delta)^2+L,\qquad L\ge0,
$$

其中 $L$ 明确分成混合曲率块的秩偏离和幅度方差。这个等式自身仍容许 $p=0,\delta=1,L=0$。

后续稿提供有符号的真实度量变分。在闭 almost-Kähler、Ricci 为 $J$-不变的类别，

$$
DP_g[\operatorname{Ric}^{\circ}]
=\frac18\int|ds|^2-\frac12\int s|\operatorname{Ric}^{\circ}|^2.
$$

常非零标量时，非 Einstein 度量有保体积形式的下降方向，因而不能是无限制 $P$-临界点。负标量下进一步的精确谐和秩对齐条件
$\operatorname{im}B_x\subset\mathbb Rh_x$
给出局部化下降，无须对零集上的商另加有界假设。因此负标量 Einstein–Maxwell 非 Einstein 度量也不可能成为 $P$-临界点。

来源：[Q3_Descent_and_Flux_Equality.tex](../archive/originals/2026-10-08/Q3_Descent_and_Flux_Equality.tex) §§2–3；[Q3_Harmonic_Alignment_Descent.tex](../archive/originals/2026-10-08/Q3_Harmonic_Alignment_Descent.tex) §§2–5；[Q3_Harmonic_Rank_Rigidity.tex](../archive/originals/2026-10-08/Q3_Harmonic_Rank_Rigidity.tex) §§1、4。后者用完整点态方程处理两幅度变化，强于早期只在一个幅度恒定时闭合的积分变分。

这些结果限制极小元的结构：假想非 Einstein 光滑极小元须有非零通量或秩偏离余项。强迫余项为零会排除候选，不能用来证明该候选取得。

### 4.2 取得性不能由“低于标准单核费用”推出

[Q3_Global_Attainment.tex](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) §§2–5 构造一个显式节点 Godeaux 退化，配合固定严格插入得到 $P<8\pi^2$ 的退化序列，其缩放核心为 Ricci-flat Eguchi–Hanson。它否定整个次 $8\pi^2$ 子水平集必紧的想法，但不证明这条序列极小，也不否定另有光滑极小元。

同稿的带标记整体分裂估计保留规范类在主体和各 ALE 核心的分量；相对特征数项相加抵消后，某些核心被排除，但规范类在真实 $(-2)$-球上的限制可为零。不能按每个二循环统一收取正 $P$ 费用。

### 4.3 后续非正曲率背景、ALE 核心与替换

[Scalar_Curvature_and_Global_Attainment_20261012.tex](../archive/originals/2026-10-12/Scalar_Curvature_and_Global_Attainment_20261012.tex) §§2–3：闭 aspherical 四维环境中，若嵌入紧域边界连通、基本群有限，且该域有 $s\ge0$、严格向外平均凸度量，则包含映射零伦。由此对所列单端光滑 ALE 核心得 $\chi=1,\tau=0$ 及边界群限制；非平凡端群时

$$
P\ge4\pi^2+S/12,
$$

Ricci-flat ALE 核心只能平坦。此处没有把环境 aspherical 条件转移给所有先前候选。

[AE_Bubble_Replacement_20261015.tex](../archive/originals/2026-10-15/AE_Bubble_Replacement_20261015.tex) §§2–3 处理平凡端群：完整单端 AE、$s\ge0,\chi=1,P<16\pi^2$ 时，利用经典 Chang–Gursky–Yang 球定理证明紧核心为标准光滑球；若它作为完整核心以 $C^2$ 缩放收敛出现在真正 $P$ 极小化序列中，正能量可由平坦填充和小能量过渡严格降低，因此不可能保留这样的气泡。

这些结论没有产生任意极小化序列的完整核心收敛，也没有排除所有轨形、中间尺度、多端和塌缩情况。$S^3/Q_8$ 界面的正能量核心不是平凡球替换覆盖的对象。

同一 10 月 12 日稿 §4 的双曲尖点加倍例说明另一个独立现象：可有闭 aspherical 流形上 $P_* =0$ 而不取得，曲率一致有界、退化来自塌缩环面颈。排除曲率气泡不足以保证取得性。

## 5. 接续研究的精确状态

| 问题 | 已改变的数学判断 | 仍需获得的结论 |
|---|---|---|
| 原平衡族 O11 | 严格次四的真实闭度量构造；覆盖量词扩大 | 全部竞争度量的匹配下界或最终最优首项 |
| Q1 非极小一般型 Einstein 存在性 | 精确候选阈值、实际通量与等号结构 | 剩余小吹起范围的存在或排除 |
| Q2 最优全曲率 | 一般 KE 背景严格节省；整个共形 Kähler 类分离；联合共形刻画 | 目标流形上 $P_*$ 或匹配渐近的实际计算 |
| Q3 非 Bach-flat 光滑全局极小元 | 明确候选；下降方向和秩刚性；真实退化例；部分核心排除和替换 | 至少一个符合要求的光滑取得实例 |

这些工作共同研究“同一流形上的全部度量极值、真实构造和极限几何”。下界、竞争构造、临界点与取得性各有独立证明任务；后续应使用已经完成的连接，并保留改变了候选答案的严格节省与退化反例。

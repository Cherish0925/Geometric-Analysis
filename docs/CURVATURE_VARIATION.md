# 曲率变分、低成本构造与全局取得性

本文介绍曲率极值问题的构造、变分与取得性。各节列出命题的适用条件和证明来源。

## 1. 三个相关但不同的极值对象

设 $M$ 为闭连通定向光滑四维流形，$g$ 遍历其光滑 Riemannian 度量。记 $s_g$ 为标量曲率，$\operatorname{Ric}^{\circ}_g=\operatorname{Ric}_g-(s_g/4)g$。以下积分均使用 $dV_g$，Ricci 使用张量范数，Weyl 和完整曲率使用曲率算子范数。定义

$$
P=\int|\operatorname{Ric}^{\circ}|^2,\quad S=\int s^2,\quad
R=\int|\operatorname{Ric}|^2=P+S/4,\quad V=\operatorname{Vol},\quad T_s=\int s.
$$

定义相对 Einstein 缺陷和两个极小值

$$
\mathcal E(g)=\inf_{\lambda\in\mathbb R\setminus\{0\}}
\frac{\int|\operatorname{Ric}_g-\lambda g|^2}{\lambda^2 V},
\qquad P_*(M)=\inf_gP(g),\qquad\alpha(M)=\inf_g\mathcal E(g).
$$

当 $R>0$ 时，令 $\mathcal J=4P/R$，则

$$
\mathcal E=4-\frac{T_s^2}{VR}
=\mathcal J+\frac{S-T_s^2/V}{R}.
$$

Chern–Weil 恒等式给 $\int|\operatorname{Rm}_{\rm op}|^2=8\pi^2\chi(M)+P$，所以固定流形上的全曲率极小化与 $P$ 极小化等价。相对缺陷另取决于标量方差及 $R$。Ricci-flat 度量在上述 $\lambda\ne0$ 定义下满足 $\mathcal E=4$；$\mathcal J$ 在该情形不定义。以下 $\chi$、$\tau$ 分别表示 Euler 数和签名。

来源：[03_Subsequent_Mathematical_Developments(1).tex](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §1。

## 2. O11：严格低于标准手术能量的构造

### 2.1 从有限尺度证书到任意固定复双曲领口

早期构造以区间证书建立光滑单元的严格上界，并传至相应覆盖族。后续解析构造证明：每个固定半径 $R_0>0$ 的复双曲领口内，都存在普通负单吹起单元，在外部精确等于 $\operatorname{Ric}=-6g$，并满足

$$
\frac{P(g_\epsilon)}{8\pi^2}
=1-9\epsilon^2\log(1/\epsilon)+O_{R_0}(\epsilon^2),
\qquad
\frac{J_6(g_\epsilon)}{8\pi^2}
=1-9\epsilon^2\log(1/\epsilon)+O_{R_0}(\epsilon^2),
$$

其中 $J_6(g)=\int|\operatorname{Ric}_g+6g|^2$。两式均包括 Burns 核心、颈部和外过渡；内外过渡的总误差为 $O_{R_0}(\epsilon^2)$。因此充分小的正 $\epsilon$ 给出 $P,J_6<8\pi^2$。

来源：[O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) §§0–6。其 §8 指向系统 A01 Step10、A02 Step11、[theorem_package_v1.md](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md) 和原颈部符号程序。

### 2.2 覆盖量词和极限次序

设 $X_0$ 为固定紧复双曲曲面，$X_j\to X_0$ 为度数趋于无穷的有限非分歧覆盖，$A_j=c_1^2(X_j)$。令

$$
M_j=X_j\#k_j\overline{\mathbb{CP}}^{\,2}\#\ell_j(S^1\times S^3).
$$

原平衡比例为

$$
Q_j=k_j+4\ell_j\to\infty,\quad h_j=Q_j/A_j\to0,\quad
k_j/Q_j\to2/9,\quad\ell_j/Q_j\to7/36
$$

在这些比例下，适合基底小嵌入球的固定单元可复制至 $M_j$，得到

$$
\limsup_j\frac{\alpha(M_j)}{h_j}
\le4-\frac89\delta_{X_0}<4.
$$

其中 $\delta_{X_0}>0$ 是固定单元相对于 $8\pi^2$ 的归一化节省，可依赖 $X_0$。极限次序为：固定领口和一个足够小的正插入参数，再令覆盖度数趋于无穷。

另一路使用一个已有固定半径单元：对于事先给定、嵌套且子群交集平凡的残余覆盖塔，某一级以后具有正比例的该单元安放位置。此结论也适用于非正规塔，仅使用固定球在某一级的嵌入。在该量词下，既有区间证书与共形尾部恢复给出

$$
\limsup_j\alpha(M_j)/h_j\le3.9961446513521015108\ldots<4.
$$

数值证书给出特定单元的显式上界；任意固定小领口的构造扩大了覆盖序列的适用范围。

来源：[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §§3–5；任意固定基底覆盖序列的扩展见 [O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) §6。

令 $\mathfrak P_{8n,7n}$ 为原稿定义的完整标记混合单元能量下确界。次可加性给出

$$
\gamma_{\rm bal}=\lim_{n\to\infty}
\frac{\mathfrak P_{8n,7n}}{72\pi^2n}
=\inf_n\frac{\mathfrak P_{8n,7n}}{72\pi^2n},
\qquad \limsup_j\alpha(M_j)/h_j\le\gamma_{\rm bal}.
$$

反向不等式需要将一般竞争度量局部化至该单元范畴，或建立相应全局下界。

### 2.3 一般背景的张量机制

10 月 8 日主稿将特殊复双曲构造推进到一般负 Kähler–Einstein 背景。写 $R^+=W^++sI/12$，表示自对偶曲率块，与积分量 $R$ 采用不同记号。对插入支撑邻域内的 $P$-临界背景、点 $p$、单位方向 $\zeta\in\Lambda_p^+$ 和固定角修正，原稿给出

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

这里 $T$ 是 $\zeta^\perp$ 上限制算子的无迹部分；$\Phi$ 为插入角修正所确定的二阶对数系数。系数公式适用于所列特征向量方向；一般方向还含旋转零模。其非正性在核方向成立，在整个 $R^+\le0$ 锥上则不成立。余项常数依赖固定光滑背景和插入数据。

来源：[01_Research_Synthesis.tex](../archive/originals/2026-10-08/01_Research_Synthesis.tex) §3，尤其 A01.52、A02.59D 的修正版及 §3.5。

## 3. 全局竞争类别与归一化结论

设 $X$ 为极小一般型复曲面，$M=X\#k\overline{\mathbb{CP}}^{\,2}$、$A=c_1^2(X)>0$。在经典全度量标量曲率估计 $S\ge32\pi^2A$ 下，对原取向上任意复结构的 Kähler 度量 $h$ 及 $g=u^2h$，有

$$
P(g)-8\pi^2k
=\frac{S(g)-32\pi^2A}{12}
 +\frac{S(h)-32\pi^2A}{6}\ge0.
$$

结合严格构造上界，整个原取向全局共形 Kähler 类与低于 $8\pi^2k$ 的竞争度量分离。当 $\tau(M)\ge0$ 时，原稿还将该比较扩展至相反取向。

来源：[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §2。

同一负 Yamabe 类中的最小代表不增加 $P$。在统一标量曲率下界下，归一化上界为

$$
\alpha(M)\le\frac{4\mathfrak p_*(M)}{A+\mathfrak p_*(M)},
\qquad\mathfrak p_*=P_*/(8\pi^2),
$$

由严格插入得到 $\alpha(X\#k\overline{\mathbb{CP}}^{\,2})<4k/(A+k)$。$P_*$ 的精确值和小 $k/A$ 时的最优尺度仍待确定。

在一般闭四维流形上，长圆柱构造给每个闭四维流形 $0\le\alpha\le1$；若 $2\chi-3|\tau|\le0$，则 $\alpha=1$，严格负时不取得。令

$$
d([g])=8\pi^2\chi-\int|W|^2,
$$

令 $Y([g])$ 为共形类的 Yamabe 常数。原稿给出无需规范场假设的全局共形表达式

$$
\alpha(M)=1-6\sup\left(\{0\}\cup
\left\{\frac{d([g])}{Y([g])^2/3-2d([g])}:d([g])>0\right\}\right),
$$

以及 $\alpha<1\iff\inf_g\int|W|^2<8\pi^2\chi$。这是联合 Weyl–Yamabe 极值刻画，尚未在全部目标吹起族上计算该上确界。

来源：[03_Subsequent_Mathematical_Developments(1).tex](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §§5–6。

## 4. Q1 与 Q3：精确 Einstein 候选和光滑全局极小元

Q1 研究非极小一般型曲面的 Einstein 存在性。[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §3 精确反解了经典可行区：在 $0<k<A/3$ 时，定义 $W_+(g)=\int|W^+_g|^2$ 和 $\kappa=A/2-3W_+/(8\pi^2)$。Einstein 候选满足

$$
\kappa\ge k+\frac{k^2}{A(1+\sqrt{1-3k/A})^2}>k.
$$

这是候选 Einstein 度量的必要条件。小吹起范围的存在或排除仍待解决；本节 $\kappa$ 表示 Weyl 缺额，与端点问题中的参数缺陷采用不同定义。

Q3 询问闭光滑流形上的全局 $P$ 极小值是否可由非 Bach-flat 光滑度量取得。原稿提出两种明确候选：Horikawa 单吹起和 Godeaux 单吹起，均具有

$$
16\pi^2/3\le P_*<8\pi^2.
$$

经典曲率下界已排除 Einstein 度量；若取得，则负 Yamabe 性、$P$-临界性和变分关系保证极小元非 Bach-flat。尚缺的是光滑取得性本身。

来源：[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §4 的 Horikawa 例；[Q3_Global_Attainment.tex](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) §1 的 Fermat 商 Godeaux 例。两种候选具有各自的光滑拓扑。

### 4.1 谐和通量与下降方向

[03_Subsequent_Mathematical_Developments(1).tex](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §3 中，令 $B:\Lambda^+\to\Lambda^-$ 为混合曲率块，$a$ 为给定第一 Chern 类，$h$ 为单位 $L^2$ 范数的非零谐和反自对偶形式，$q=(a_g^-,h)_{L^2}>0$。定义

$$
p=P/(8\pi^2),\qquad\mathfrak F_h=\sqrt2\int|B^*h|,
\qquad\delta=1-\mathfrak F_h/(2\pi q),
\qquad L=(P/2-\mathfrak F_h^2)/(4\pi^2).
$$

则

$$
p=q^2(1-\delta)^2+L,\qquad L\ge0,
$$

其中 $L$ 明确分成混合曲率块的秩偏离和幅度方差。这个等式自身仍容许 $p=0,\delta=1,L=0$。

后续稿给出度量变分公式。在闭 almost-Kähler 结构 $(g,J,\Omega)$、Ricci 为 $J$-不变的类别，

$$
DP_g[\operatorname{Ric}^{\circ}]
=\frac18\int|ds|^2-\frac12\int s|\operatorname{Ric}^{\circ}|^2.
$$

常非零标量时，每个非 Einstein 度量均有保体积形式的下降方向。负标量下进一步的精确谐和秩对齐条件
$\operatorname{im}B_x\subset\mathbb Rh_x$
给出局部化下降，无须对零集上的商另加有界假设。因此负标量 Einstein–Maxwell 非 Einstein 度量也不可能成为 $P$-临界点。

来源：[Q3_Descent_and_Flux_Equality.tex](../archive/originals/2026-10-08/Q3_Descent_and_Flux_Equality.tex) §§2–3；[Q3_Harmonic_Alignment_Descent.tex](../archive/originals/2026-10-08/Q3_Harmonic_Alignment_Descent.tex) §§2–5；[Q3_Harmonic_Rank_Rigidity.tex](../archive/originals/2026-10-08/Q3_Harmonic_Rank_Rigidity.tex) §§1、4。后者用完整点态方程处理两幅度变化，将早期一个幅度恒定时的积分变分结论推广至两幅度均变化的情形。

因此非 Einstein、负标量的光滑极小元若存在，对每个非零谐和反自对偶形式均有严格正的对齐余项；这一正数允许依赖度量。

### 4.2 次标准能量子水平集中的退化

[Q3_Global_Attainment.tex](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) §§2–5 构造一个显式节点 Godeaux 退化，配合固定严格插入得到 $P<8\pi^2$ 的退化序列，其缩放核心为 Ricci-flat Eguchi–Hanson。因此次 $8\pi^2$ 子水平集可非紧。该构造未确定退化序列是否极小，光滑取得性仍为独立问题。

同稿的带标记整体分裂估计保留规范类在主体和各渐近局部欧氏（ALE）核心的分量；相对特征数项相加抵消后，某些核心被排除，但规范类在嵌入 $(-2)$-球上的限制可为零；Ricci-flat 核心具有非平凡二循环而 $P=0$。

### 4.3 非球面背景中的 ALE 核心与替换

[Scalar_Curvature_and_Global_Attainment_20261012.tex](../archive/originals/2026-10-12/Scalar_Curvature_and_Global_Attainment_20261012.tex) §§2–3：闭 aspherical 四维环境中，若嵌入紧域的边界连通且边界基本群有限，且该域有 $s\ge0$、严格向外平均凸度量，则包含映射零伦。由此对所列单端光滑 ALE 核心得 $\chi=1,\tau=0$ 及边界群限制；非平凡端群时

$$
P\ge4\pi^2+S/12,
$$

满足这些嵌入条件的 Ricci-flat ALE 核心只能平坦。Aspherical 指环境流形的万有覆盖可缩。

[AE_Bubble_Replacement_20261015.tex](../archive/originals/2026-10-15/AE_Bubble_Replacement_20261015.tex) §§2–3 处理平凡端群：对满足原稿微分衰减条件、$s\ge0,\chi=1,P<16\pi^2$ 的完备单端渐近欧氏（AE）流形，利用经典 Chang–Gursky–Yang 球定理证明紧核心为标准光滑球；若它作为完整核心以 $C^2$ 缩放收敛出现在 $P$ 极小化序列中，正能量可由平坦填充和小能量过渡严格降低，因此不可能保留这样的气泡。

替换定理以完整核心的光滑缩放收敛为输入。一般极小化序列的轨形、中间尺度、多端及塌缩分支仍待分析；边界为 $S^3/Q_8$ 的正能量核心属于非平凡端群分支。

同一 10 月 12 日稿 §4 的双曲尖点加倍例说明另一个独立现象：可有闭 aspherical 流形上 $P_* =0$ 而不取得，曲率一致有界、退化来自塌缩环面颈。取得性因而同时涉及曲率集中和塌缩退化。

## 5. 接续研究的精确状态

| 问题 | 已改变的数学判断 | 仍需获得的结论 |
|---|---|---|
| 原平衡族 O11 | 严格次四的闭度量构造；覆盖量词扩大 | 全部竞争度量的匹配下界或最终最优首项 |
| Q1 非极小一般型 Einstein 存在性 | 精确候选阈值、实际通量与等号结构 | 剩余小吹起范围的存在或排除 |
| Q2 最优全曲率 | 一般 KE 背景严格节省；整个共形 Kähler 类分离；联合共形刻画 | 目标流形上 $P_*$ 或匹配渐近的实际计算 |
| Q3 非 Bach-flat 光滑全局极小元 | 明确候选；下降方向和秩刚性；退化例；部分核心排除和替换 | 至少一个符合要求的光滑取得实例 |

上述结果分别约束竞争度量、临界点和退化极限。完整的极值结论需要全局下界与构造上界匹配；光滑取得性还涉及极小化序列的选择和极限正则性。

# S1003A02：Einstein 间隙、低成本构造与奇异极限

本会话承接实际场强制估计、有限密度端点和曲率极值理论，研究其在全部竞争度量、手术构造及退化中的适用范围。现存记录包括 108 个完成步骤，时间从 2026 年 10 月 3 日至 10 月 14 日。原始目标见 [original_research_goal.md](workspace/briefing/original_research_goal.md)。

阅读入口：

- [问题状态与定理依赖](workspace/notes/state_of_problems_1_4.md)：更新至 Step 108，优先用于理解后期结论。
- [连续定理正文](workspace/notes/theorem_package_v1.md)：定义、证明、构造、程序和文献的主索引。
- [108 步研究交接](research_steps.md)：各步完成的数学、路线选择及当时提出的下一步。
- [科学讨论](research_exchange.md)与[会话组往来](../../groups/geometric-analysis.md)：保留判断形成、独立核算和修正的过程。
- [引用文献](references.bib)：与正文引用键对应；[来源表](reference_sources.json)保留论文标识和原研究库位置。

这里按数学依赖组织成果；历史文件保留原文，后续撤回和修订在下文指出。

## 1. 泛函：何种“间隙”正在被计算

设 $M$ 为闭定向四维流形，记

$$
P=\int|\operatorname{Ric}^{\circ}|^2,\quad
S=\int s^2,\quad R=P+S/4,\quad
L_s=\int(s-\bar s)^2.
$$

原目标泛函为

$$
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V}
=\frac{4P+L_s}{R}\quad(R>0),
\qquad \alpha(M)=\inf_g\mathcal E(g).
$$

$P_*(M)=\inf_gP(g)$ 是另一个极值问题。Ricci-flat 度量满足 $P=0$，而原定义给 $\mathcal E=4$；因此从 $P\to0$ 推出 $\mathcal E\to0$ 需要非零 Einstein 尺度。实际场参数量 $\kappa_\beta$ 还包含场—曲率对齐缺陷，不能删去其中的场项。

[Steps 71–72](workspace/notes/step72_orientation_free_weyl_deficit_law.md)把原泛函写成不依赖取向的 Weyl 缺额。令 $\mathcal W=\int|W|^2$，则

$$
\mathcal E-1=\frac{6(\mathcal W-8\pi^2\chi)+L_s}{R}.
$$

长圆柱球形哑铃构造给出每个闭四流形上的 $0\le\alpha\le1$；结合签名界，$2\chi\le3|\tau|\Rightarrow\alpha=1$。在等号 $2\chi=3|\tau|$ 上，取得 $\alpha=1$ 要求相应半共形平坦、非零常标量度量。K3 和 $T^4$ 的 $\alpha=1$，并不由其 Ricci-flat 度量取得。这个区分贯穿后续解消、取得性和精确存在性研究。

## 2. 端点范围与真实构造：Steps 1–24

[Step 1](workspace/notes/step1_field_compatibility_and_route_portfolio.md)将共同机制写为实际场供给、代数对齐、微分延拓和集中/实现。它从原 O10 中分离出尚未受控的低幅度径向集中；单纯增加标量矩估计不能提供完整场方程缺少的信息。

[L′ 与 K](workspace/notes/step6_theorems_and_O11_rotation.md)扩展了端点控制：

- 固定 $\theta<3/4$，同一 Spin$^{c}$ 结构在整个共形类内实际可解，且 $p\ge A>0$、$a^2\ge T_+$、$T_+\le\theta A$ 时，L′ 对所有有限 $\beta\ge2$ 给 $\kappa_\beta\ge c_L(\theta)>0$，无需 Euler 密度界。
- 对满足原实际供给的一般型曲面吹起，K 按 $k/A$ 分区，将 L′ 与一个固定有限密度端点常数组合，得到与吹起次数无关的参数估计。
- 同稿的 canonical-model 解消给一般型极小曲面上的 $\alpha=0$；精确 Einstein 存在性仍是该值是否取得的问题。对齐缺陷为正与 $\alpha=0$ 可以共存。

其中 $2/3$、$\beta=8$、$3/4$ 来自同一个二次多项式

$$
N_\theta(\beta)
=(3/4-\theta)\beta^2+(1/2-11\theta/4)\beta+6-\theta.
$$

$N_{2/3}(\beta)=(\beta-8)^2/12$，而 $\theta=3/4$ 消去其最高次项。这解释经典估计与有限参数强制各自在哪个区间发挥作用；一般无密度 O10 仍未闭合。

[Theorem F](workspace/notes/step20_burns_response_and_neck_quantization.md)在任意固定光滑背景上计算标记吹起的响应：

$$
P(\widehat g_x)=P(g)+8\pi^2
\bigl[1-x\mathbf R_p^+(\zeta,\zeta)\bigr]+O(x^{6/5}),
\qquad\mathbf R^+=W^++sI/12.
$$

背景曲率及插入方向共同决定修正项。核方向进入二阶计算。[严格低成本单元](workspace/notes/step11_subthreshold_perpendicular_cell.md)与 A01 的后续区间证书证明成本可以小于 $8\pi^2$；标准恢复首项 $4$ 因此不能作为固定的下界目标。

同一阶段研究真实 Einstein 填充、CH 与实双曲背景的差别、Yamabe 归约及相对体积。须区分两项存在性材料：Fino 问题所用的完整 $\mathbb R^4$ 显式 almost-Kähler Einstein 例来自 A01；本会话的 ACH/Rossi $\mathcal O(-1)$ 填充是另一条计算辅助链。后者在 [Fuchsian 初值程序](workspace/scripts/ach_bolt_fuchs.py)中存在已指出的分量排列和余项界问题，尚未见本地修复。旧定理包 §6 的“完整认证”不能据此沿用；这不影响独立的严格次 $4$ 构造。

## 3. 哪种局部费用可以用于全局问题：Steps 25–48

[特征数边界通量](workspace/notes/step33_link_charges_global_decomposition_static_channel.md)将有边界区域的费用写为

$$
\frac{P(D)}{8\pi^2}
=\frac1{2\pi^2}\int_D|W^\pm|^2
+\frac1{96\pi^2}\int_Ds^2
-(2\chi\pm3\tau)(D)+\mathcal Q_\pm(\partial D).
$$

领口的完整几何数据参与 $\mathcal Q_\pm$。几乎平直边界、ALE 边界、CH 边界及塌缩 Hopf 边界的支付不同，因而不能把普通 AE 核心的单价直接用于全部竞争度量。标记单元的次可加性产生单元族的极限费用；该极限与闭流形的全度量极值之间还缺少全局连接。

这一阶段留下的实质结构包括：

| 数学内容 | 原文与作用 |
|---|---|
| 标定、Hamilton–Jacobi 和对称单元分支 | [Step 35](workspace/notes/step35_calibration_theorem_and_branch_classification.md)：精确平方分解与校准流，区分真正的核和路径连接费用 |
| 同度量多个实际场、振幅和 Nijenhuis/Weyl 关系 | [Step 40](workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md)：仿射预算的饱和范围及仍需控制的共同模态 |
| 实际周期和扭率预算 | [Step 42](workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md)：指出谐和投影控制尚不足以控制扭率的恰当部分 |
| Cotton 配对及二次尺度候选 | [Step 43](workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md)、[Step 47](workspace/notes/step47_consolidation_two_scale_program.md)：记录精确恒等式、候选尺度和未证连接 |
| CH 附近与局部区域的强制 | [Step 46](workspace/notes/step46_lemmaM_elementary_and_AC.md)、[Step 48](workspace/notes/step48_yamabe_channel_and_localized_CH.md)：带指定邻域、规范和边界项的结论 |

这些工具不把任意近极小序列自动变成已标记、边界受控的单元。纯吹起族的 $k^2/A$ 尺度在研究中曾是候选，并未成为上下界匹配的定理。

## 4. 二阶 Burns 节省及闭流形上界：Steps 49–74

### P-critical 背景的二阶展开

[Theorem 59.R](workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md)在插入点附近 $P$-临界的固定背景上，保留背景二阶曲率和齐次修正 $K$，得到

$$
\frac{P(\widetilde g_\varepsilon)-P(g)}{8\pi^2}
=1-\varepsilon\mathbf R_p^+(\zeta,\zeta)
+\frac{\Phi(\operatorname{Rm}_p,\zeta,K)}2
\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
$$

证明使用手性平方 $F_+=4|W^+|^2+s^2/12$ 在 Burns 背景上恒为零，分别控制内核、中间环带和外过渡。三阶以上背景导数只进入二次余项；$P$-临界性控制一次变分。

在 Kähler–Einstein 背景取 $\zeta\perp\omega$，可消去反手性背景项，并有 $\Phi=-s^2/32$。于是

$$
\frac{P(\widetilde g_\varepsilon)}{8\pi^2}
=k-\frac{ks^2}{64}\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2)<k.
$$

Corollary 59.KE 再用 canonical-model 的 ADE 解消扩展到每个一般型极小曲面 $X$ 及任意 $k\ge1$：

$$
P_*(X\#k\overline{\mathbb{CP}}^2)<8\pi^2k.
$$

这是全部度量下确界的严格**上界**。固定复结构的 Kähler 度量范围仍有下确界 $8\pi^2k$，不取得；因此新构造体现了非 Kähler 竞争者的实际作用。它没有确定 $P_*$ 的值或取得性。

### 平衡族的非渐近上界

[Step 69](workspace/notes/step69_P_form_upper_law_balanced_towers.md)利用 A01 的严格 $P$-区间证书，令

$$
C_c=\frac{28}{9}+\frac89p_c
=3.99614465135210151\ldots<4.
$$

在先取足够厚的固定球商覆盖、随后任意有限覆盖且满足实际放置数量条件时，对 $k=8n,\ell=7n,Q=36n,h=Q/A$ 的平衡族有

$$
\frac{\alpha(M)}h\le\frac{C_c}{1+C_ch/4}.
$$

这同时保留全局复制、柄费用和 Yamabe 分母，强于单一选定序列的渐近陈述。覆盖与放置条件是定理的一部分。[Step 74](workspace/notes/step74_packing_weyl_theorem_and_scope.md)还将构造接入 Weyl 缺额和中间参数区间；匹配的全度量下界仍缺。

### 取得性及精确存在

[Steps 50–58](workspace/notes/step58_consolidated_hypothesis_ledger.md)研究 Anderson 型极小序列分解、Kronheimer 吸收、光滑/轨形极小元和例外类费用。$k=1$ 上的“Einstein 或非 Bach-flat 全局极小元”定理保留明确的光滑紧性、下半连续、分解、等号与可去奇点假设，并需排除塌缩和非标准 cap。Ekeland/流选择并未自动提供这些输入。它是一项条件取得性结果，Q3 的无条件光滑取得性没有完成。

## 5. 闭负 Goldberg：Steps 75–84 及后续衔接

[Step 75](workspace/notes/step75_Q4_half_twistor_torsion_and_zero_index.md)将 $J$-不变 Ricci 条件写为扭率截面的精确半 twistor 方程，给出过定椭圆主符号及最优 refined Kato 平方常数 $3/4$。同一个结构包含 Einstein 和 Blair–Ianus 情形。

闭 Einstein almost-Kähler 四流形的扭率截面所在复秩二丛满足

$$
c_2=5\chi+6\tau>0,
$$

所以扭率必有零点。与 A01 的独立计算结合，二阶方程在非退化零点给

$$
\|A\|^2=\|S\|^2+8|c|^2,
\qquad \operatorname{ind}=+1.
$$

这与正的总拓扑计数相容。[Steps 77–80](workspace/notes/step80_Q4_universal_functional_and_lambda_quadratic.md)撤回了“六阶阻碍一切非退化零点”的候选判断：广泛扫描得到相反符号和实际有限阶数值见证。被交叉核算的八阶见证是有限精度数据，不是收敛解析解。

[Step 84](workspace/notes/step84_scalar_compat_derivation.md)辨认出 Darboux/anti-$J$ 度量变分的额外标量相容算子

$$
\mathcal P(E)=J^i{}_aJ^j{}_b\partial_a\partial_bE_{ij}
-\tfrac12\Delta\operatorname{tr}E.
$$

在所计算的 $d=4,6,8$ 次数，顶阶 Ricci 映射余核由 Bianchi 行与 $\mathcal P$ 行组成。两系统八阶比较还解释了“秩 91”已是消去 28 个变量方向后的满秩，先前的秩亏解释不成立。

后期对 A01 精确 Einstein 序列定理的接入见[状态稿 §4](workspace/notes/state_of_problems_1_4.md)：在固定负标量、非塌缩和有界直径下，相关 deficit 与扭率分裂排除 $W^+$ 及扭率能量集中，泡为取向匹配的 Kähler Ricci-flat ALE。这针对**精确 Einstein 序列**，不覆盖定义 $\alpha$ 的任意近 Einstein 序列。

Fino 的完整非紧例确实提供存在性答案，并检验局部恒等式可能支持的刚性范围；闭负 Goldberg 仍需要紧性、零点及全局耦合的信息。无条件可积性没有从这些局部延拓中推出。

## 6. 特定轨形范畴的精确极值：Steps 85–93

令 $X$ 为紧复双曲曲面，$A=c_1^2(X)$，在 regular points 作连通和

$$
V_m=X\#m(S^4/\mathbb Z_2),\qquad k=2m>0.
$$

[Step 93](workspace/notes/step93_paired_A1_transfer_review.md)接续 A01 Step 74，对此固定轨形拓扑上的**全部光滑轨形度量**证明

$$
P_{*,\mathrm{orb}}(V_m)=8\pi^2k,
\qquad
\alpha_{\mathrm{orb}}(V_m)
=\min\{1,4k/(A+k)\}.
$$

关键是 EH 解消将 smooth $X\#k\overline{\mathbb{CP}}^2$ 上的标量预算传回轨形，得到 $\sigma=S-32\pi^2A\ge0$。签名给 $w=\mathcal W-4\pi^2A/3=2\int|W^-|^2\ge0$，从而

$$
P=8\pi^2k+\sigma/12+2w,
\qquad
R=8\pi^2(A+k)+\sigma/3+2w.
$$

Green football cap 给匹配恢复序列。$P$ 的下确界永不取得；$\alpha$ 在 $k\ne A/3$ 时不取得，在边界 $k=A/3$ 的取得性仍为相应负常标量半共形平坦轨形问题。任何 $m>0$ 的 $V_m$ 都没有 Einstein 轨形度量。

这是一个指定奇异范畴的完整极值结果。其光滑解消上的 $P_*$ 严格小于 $8\pi^2k$，所以不能把轨形公式转述为 Q2 在光滑吹起族上的完整解答。Step 101 再次阅读了非取得证明；Steps 105–108 的后续修正未撤回此结论。

## 7. Wahl、ALE 格与塌缩端：Steps 94–108

### 填充费用与整数拓扑

[Steps 95–96](workspace/notes/step95_verified_transfer_lattice_thresholds.md)把传递方法扩展到 Kähler Ricci-flat ALE 填充，得到

$$
9C_-+2C_++42k+12(3c_2(X)-c_1^2(X))\ge0.
$$

在球商、全部例外秩被填充吸收的范围，根格分类迫使存在 Kronheimer $D_a$、$a\ge6$ 块，故 $k\ge6$；$k=6$ 时只剩单个 $D_6$ 型及相应参数必要条件。这里筛出的数据不是 Einstein 度量构造。

[Step 99](workspace/notes/step99_independent_verification_and_repairs.md)完成 Wahl 有理球的整数格连接：在 aspherical、无挠基本群背景上，边界映射消失，补空间格指数为 $\prod n_j$，判别形式等于指定 lens linking form，并有 $L=Q_X\oplus L_0$、$L_0\subset-I_k$。四平方构造给每个 Wahl 点四个例外坐标的统一充分条件 $k\ge4t$，并保留低秩障碍。它还修正了 Şuvaina 填充的等变提升证明。

### 真正的 Wahl 拓扑与尚缺的 Einstein 度量

[Step 102](workspace/notes/step102_wahl_orbifold_realization_and_K2_invariance.md)使用 Park–Park–Shin/Khodorovskiy 嵌入构造实际 Wahl 轨形。对 $1/n^2(1,n-1)$ 点，特征数修正满足

$$
T_+^{\rm orb}=A-k,
\qquad
T_-^{\rm orb}=T_-(M)-4\sum_j(1-n_j^{-2}).
$$

于是标准标量/$W^+$ 预算与光滑化后的阈值一致；新信息须来自标记、奇异类或方程。[Step 103](workspace/notes/step103_independent_reading_wahl_isotropy_and_known_mechanisms.md)说明局部各向同性迫使 Weyl 两块具有重特征值，但允许不变 Einstein germ，不能单凭局部锥点数据排除。

[Step 108](workspace/notes/step108_independent_reading_and_synchronized_close.md)接入 A01 经修正的 WFL 实际场极限、可延拓 Dirac 指数及标记复实现。可传递的是 $a^2,T_+$、指定指数、实际供给和标量/$W^+$ 界；$T_-$、局部 character、强制零点和全部模空间并不随之等同。强制零点给严格标量不等式，但统一分离仍取决于标记尺度 $\lambda r_0^2$ 及其在 Ricci-flat 泡中的行为。

### 手性费用与 Einstein 端部

[Step 105](workspace/notes/step105_cusp_channel_restored_and_cap_charge_theorem.md)在有限体积 Einstein 主体、无体积损失和稳定 nested caps 等假设 $E$ 下证明

$$
C_+(\Omega)=A-k-\sum_jc_j,\qquad c_j\ge0,
\qquad 9k+8\sum_jc_j\le3A.
$$

多端 cap 先控制 incident charges 的总和；各端单独极限还需端部渐近信息。四类 Hopf cap 的 $(c_+,c_-)=(0,20)$，即可以不付正手性费用而保留反手性曲率 $40\pi^2$。[D4 ALF 架构](workspace/notes/step106_independent_cap_charge_and_D4_candidate.md)与此相容，但相对微分同胚类型、塌缩过渡和 Einstein 宿主尚未构造。

[Steps 107–108](workspace/notes/step108_independent_reading_and_synchronized_close.md)从 Einstein 端方程进一步排除：

- 相对度量与 Ricci 渐近成立的固定底圆纤维 cusp 必须有双曲底，不能是固定 $S^2$ 或平直 $T^2$ 底。
- 有限能量并具相应曲率控制的球形端，若 lift 为双轴，不能具有所假设的有限体积。
- 对角三轴端在 $\liminf\sigma_2>0$ 的条件下同样被排除。

无对称假设的 Hopf 端、缩底尖端、多类 cap，以及从任意近极小序列提取 $E$，仍是未完成连接。这些结果将“拓扑怎样在受控手性中隐藏、Einstein 方程是否允许其端部”变成具体问题。

## 8. 更正与当前未完成部分

| 历史判断 | 应采用的后续内容 |
|---|---|
| 标准吹起单价 $8\pi^2$、首项 $4$ 应为普遍最优 | 被真实低成本单元及 59.KE 否定；下界必须允许背景—核心相互作用 |
| 只要近驻点/近稳定就可取得光滑全局极小元 | [假设说明](workspace/notes/step58_consolidated_hypothesis_ledger.md)保留自身尺度紧性、解消及端部输入 |
| Conjecture 79.C：六阶排除非退化扭率零点 | Step 80 的数值见证和 Step 84 的独立系统比较推翻该有限阶判断 |
| 104.C/104.F 消除了实际类 character 与 cusp 路线 | [Step 105 §0](workspace/notes/step105_cusp_channel_restored_and_cap_charge_theorem.md)撤回；边界类误识及非单射 cusp 基本群不能支持该结论 |
| 四类 cap 为“零能量”，D4 格识别给光滑型 | 仅 $C_+=0$；$C_-=20$。Donaldson/Freedman 到同胚型为止，相对光滑识别仍缺 |
| ACH/Rossi 填充旧证书完整 | Fuchsian 初值证书缺口待修，不能与显式 Fino 例的完整证明混用 |

Q1 的一般非极小 Einstein 存在性、Q2 的光滑全度量精确极值、Q3 的无条件非 Bach-flat 光滑全局极小元、Q4 的闭负 Goldberg，均未在 Step 108 前获得完整解答。已获得的范围扩张、严格构造上界、指定轨形精确极值、整数拓扑实现和端部排除则各有独立数学内容。

保存的程序与结果覆盖符号曲率、Arb/CAPD 区间计算、精确格论、有限阶 AKE 张量和数值构造。大型可重算 Hessian/算子缓存未重复纳入正文材料；数值见证、生成脚本、运行参数及结果保留。本文组织研究来源，不以这次归档重新赋予原计算新的证明等级。

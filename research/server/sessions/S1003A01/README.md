# S1003A01：构造、曲率变分与实际场相容性

本会话共有 95 个完成步骤，研究记录覆盖 2026 年 10 月 3 日至 10 月 14 日；本次保存截至 11 月 1 日取得的文件版本，包括步骤结束后的数学修订。它继承 N1、I40/I41、有限密度 O10 和原平衡族，先改变 O11 的候选最优值，再发展一般背景插入、轨形曲率转移、负 Einstein 几乎 Kähler 几何与 Wahl 点上的实际场分析。

本文给出数学演进和主结果入口。[全部步骤交接](history/research_steps.jsonl)保存各步骤的原始研究总结与后续任务，[科研问答](history/research_dialogue.jsonl)保存实际沟通；历史交接中的判断以随后修订的证明为准。共同记号与跨会话关系见[总研究图](../../../../docs/RESEARCH_MAP.md)、[曲率变分](../../../../docs/CURVATURE_VARIATION.md)和[负 Goldberg 分支](../../../../docs/GOLDBERG.md)。

## 1. 核心问题和研究转折

记
\[
P(g)=\int|\operatorname{Ric}^{\circ}|^2,\qquad
\mathcal J(g)=\frac{4P(g)}{\int|\operatorname{Ric}|^2},\qquad
\alpha(M)=\inf_g\mathcal E(g).
\]
\(\mathcal E\) 还包含标量方差，在常标量代表上等于 \(\mathcal J\)。曲率范数、不同 Einstein 归一化与各种局部残差的关系在各证明开头固定；局部 \(J_6=\int|\operatorname{Ric}+6g|^2\) 不应与归一化 \(\mathcal J\) 混用。

| 步骤 | 问题与实际变化 | 连续证明入口 |
|---|---|---|
| 1–11 | 从尝试证明每个吹起单元固定费用，转为构造并严格包围费用低于 \(8\pi^2\) 的真实单元；闭流形上的首项 \(4\) 因而不再是正确的普遍最优值 | [有限尺度单元](workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md)、[独立复核与混合费用](workspace/notes/step11_independent_review_O11_and_mixed_cost.md) |
| 13–29 | 研究重叠尾部、领口阻力、bolt 面积、Hamilton–Jacobi 和共形归约；保留实际场非可积能量与正余项，区分真实降能与数值拟合 | [共形归约](workspace/notes/step22_exact_CH_conformal_reduction.md)、[几乎 Kähler 费用恒等式](workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md)、[边界通量](workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md) |
| 31–43 | 将严格节省接到分歧负 KE 背景、两参数手术族；分析实际调和形式、例外周期与辛结构，明确 cap 试验没有提供同等范围的改善 | [全局斜率律](workspace/notes/step33_surgery_slope_law_and_ASD_retention.md)、[周期预算](workspace/notes/step43_period_linear_lebrun_ledger_and_ricci_flow.md) |
| 45–47、89–91 | 研究 O10 的实际 Taub–NUT 扭率载体与第五幂线丛投影；平均恒等式、局部能量与闭全局匹配之间的缺口得到具体化 | [有限标记块](workspace/notes/step46_o10_finite_marked_block_and_spinor_matching.md)、[实际扭率模型](workspace/notes/step47_o10_tn_core_free_at_energy_scale.md)、[投影与平均约束](workspace/notes/step90_review_and_tn_projected_charge5.md) |
| 48–53 | 将 CH 负对数节省推广到一般 Einstein 背景的自对偶曲率核方向，给出显式修正项和完整缩放余项 | [一般背景插入定理](workspace/notes/step52_kernel_insertion_theorem.md) |
| 55–68 | 从几何相容方程得到完备非紧严格 AKE 模型；研究扭率零点、零曲线、形式 jets 与高阶相容性 | [显式模型](workspace/notes/step58_verified_bianchiVIII_AKE_and_closed_zero_locus.md)、[零点结构](workspace/notes/step65_homogeneous_torsion_zero_classification_and_surface_transport.md)、[高阶模型](workspace/notes/step67_nondegenerate_zero_order6_reconstruction.md) |
| 71–75 | 将完整混合曲率预算经 Ricci-flat 解消转到轨形主体；计算配对 \(A_1\) 轨形的精确极值并排除该退化架构 | [轨形转移与精确极值](workspace/notes/step74_orbifold_transfer_theorem.md)、[取得性与根格限制](workspace/notes/step75_review_nonattainment_and_root_restriction.md) |
| 76–87 | 在闭负 Goldberg 问题中区分局部恒等式与紧致整体信息；得到作用量、无集中和二阶形式障碍，节点 KE 端点闭合仍依赖指定比较估计 | [作用量与退化](workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md)、[二阶中心](workspace/notes/step85_coupled_center_theorem_neck_trace_and_endpoint_reduction.md)、[条件性节点端点](workspace/notes/step87_csck_calibration_and_nodal_endpoint_rigidity.md) |
| 92–95 | 在已标记 Wahl 填充中转移真实 SW 场、能量、指标与字符；证明许可的高阶零点不存在有限 jet 可解性阻碍，将未解决信息定位到全局归一化与几何尺度 | [场极限定理](workspace/notes/step93_wfl_theorem_removability_index_transfer_and_wahl_self_similarity.md)、[正确的同场预算](workspace/notes/step94_same_field_budget_and_marked_wahl_route_decision.md)、[形式补全](workspace/notes/step95_sw_formal_completion_at_wahl_points_and_route_value.md) |

## 2. 严格次四构造与一般背景的节省机制

### 有限尺度单元和闭流形上界

Step 10 的三轴单元在 bolt 光滑闭合，在外部精确等于复双曲度量；其曲率残差通过消去坐标奇性的表达式交给 Arb 积分。Step 33 的改进单元满足
\[
\frac{J_6}{8\pi^2}\le0.995670030355130639<1.
\]
对原平衡比例 \(k_j/Q_j\to2/9\)、\(4\ell_j/Q_j\to7/9\)，复制与平滑给出
\[
\limsup_j\frac{\alpha(M_j)}{h_j}
\le\frac{28}{9}+\frac{J_6}{9\pi^2}
\le3.9961511381\ldots<4.
\]
这里的全局系数同时计入吹起和连接柄。A01 最初证明的是适当选择的覆盖族；网页后续的解析小领口及预定覆盖量词加强见[曲率变分主文](../../../../docs/CURVATURE_VARIATION.md)，不能倒写为最初数值单元已经覆盖任意塔。

原始证据包括 [曲率与区间积分程序](workspace/scripts/perp_rigorous_enclosure.py)、[Step 33 推导](workspace/notes/step33_surgery_slope_law_and_ASD_retention.md)及相应 `workspace/data/perp_collar/`、`workspace/data/perp_area/` 中的固定参数和包围结果。这里改变的是最优性判断；真正的最优首项仍需要全度量下界。

### 共形归约与实际场解释

[Step 22](workspace/notes/step22_exact_CH_conformal_reduction.md)对任意光滑精确 CH 端单元建立负常标量共形代表，控制其衰减、边界项和唯一性，从而将局部极值问题归约到常标量几何，而不要求单元有对称性。

[Step 28](workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md)在规定对角单元类中，把节省写为实际 almost-Kähler 非可积能量与非负费用之差；[Step 29](workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md)补入切割边界的准确通量。[Step 40](workspace/notes/step40_harmonic_class_compatibility_and_period_stiffness.md)和[Step 41](workspace/notes/step41_symplectic_closure_bolt_layer_and_new_inputs.md)分析近似辛对、bolt 层和标量方差。它们解释局部节省如何产生，没有由此确定全部竞争度量的最优值。

### 一般 Einstein 背景的核方向插入

设背景 Einstein 度量的自对偶曲率块为
\(\mathcal R^+=W^++sI/12\)，取单位 \(\zeta\in\ker\mathcal R_p^+\)，令 \(T\) 为 \(\mathcal R_p^+|_{\zeta^\perp}\) 的无迹部分。[Step 52](workspace/notes/step52_kernel_insertion_theorem.md)构造局部 Burns 插入，满足
\[
P(g_\varepsilon)=P(g)+8\pi^2
-4\pi^2|T|^2\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
\]
度量在一个固定小球外保持背景。修正项分解消去 \(W^-\) 对该对数系数的贡献；常数依赖固定背景及插入邻域。对于 KE 背景、\(\zeta\perp\omega\)，\(|T|^2=s^2/32\)，因而恢复 CH 的负对数机制，并扩大到任意固定非零标量 KE 背景。

构造、角向表示分解和通量推导都保留在原稿；[精确二次型程序](workspace/scripts/step52_exact_su2minus_fast.py)、[二次型分析](workspace/scripts/step52_analyze_Q.py)与 [结果](workspace/data/step52a/exact_su2minus_analysis.json)记录系数来源。Step 52 §3.3 的直接 Chern–Weil 通量计算取代其早先依赖 CH 校准的论证。

## 3. 轨形变分值与实际场转移

### 配对 \(A_1\) 架构的精确值

令 \(X\) 为紧复双曲曲面，\(A=c_1^2(X)\)，\(V_m=X\#m(S^4/\mathbb Z_2)\)，\(k=2m\)。取向匹配的 Eguchi–Hanson 解消给出 \(X\#k\overline{\mathbb{CP}}^2\)。[Step 74](workspace/notes/step74_orbifold_transfer_theorem.md)得到
\[
\inf_{g\text{ orbifold on }V_m}P(g)=8\pi^2k,
\qquad
\alpha_{\rm orb}(V_m)=\min\left\{1,\frac{4k}{A+k}\right\}.
\]
下界来自经解消转移的标量预算与双手性 Chern–Weil 关系，上界由 Green football cap 和长圆柱分别实现。每个 \(m\ge1\) 的 \(V_m\) 均不承载 Einstein 轨形度量。\(P\) 的下确界不取得；\(\alpha_{\rm orb}\) 在 \(k\ne A/3\) 时不取得，临界墙的特定常标量半共形平坦取得性仍开放。

这是指定轨形架构的完整极值计算。它同时排除这一架构作为费用严格低于 \(8\pi^2k\) 的光滑极小化序列极限；不能把轨形下界当作光滑全度量下界。

### 全混合预算保留泡的手性

若轨形 \(V\) 的奇点由匹配的 scalar-flat ALE 空间 \(N_j\) 填充，平滑恢复与原 SW 预算给出
\[
\int_V(s-\sqrt6|W^+|)^2+6\sum_j\int_{N_j}|W^+|^2
\ge72\pi^2A.
\]
对复杂取向的 Ricci-flat Kähler 填充，自对偶泡项为零。该关系比单独标量下界排除更多主体／填充组合；根格与标记的作用见 [Step 75](workspace/notes/step75_review_nonattainment_and_root_restriction.md)。通过数值预算的组合仍需实际填充、嵌入和 Einstein 主体存在。

### Wahl 场极限和有限 jet 的边界

[Step 93](workspace/notes/step93_wfl_theorem_removability_index_transfer_and_wahl_self_similarity.md)在指定的光滑恢复族、有限实际 Spin\(^c\) 供给及正投影预算下，选取固定结构子列。统一标量控制和最大值原理保证旋量及 \(F_A^+\) 不在缩小填充内集中；等变可去奇点延拓后，实类平方、完整联络曲率能量和旋量导数能量转移到 Wahl 轨形。原稿 §8 给出供给量词、规范系数、椭圆正则性和指标的最终修正。

在 \(\frac1{n^2}(1,n-1)\) 奇点，实际可延拓字符属于 \(n\mathbb Z/n^2\)。对于所列奇数 \(n\) 的强迫零点字符 \(2\le j\le n-1\)，最低许可 monogenic 次数为
\[
\ell_{\min}=2\min\{j-1,n-j\}.
\]
[Step 95](workspace/notes/step95_sw_formal_completion_at_wahl_points_and_route_value.md)用平坦主符号
\[
D_0\oplus(d^*\oplus\sqrt2d^+)
\]
的等变实多项式右逆逐阶解方程：给定许可的 leading mode、核分量和反自对偶联络数据，可完成形式 SW 解，并由 Borel 引理得到无限阶光滑近似解。它没有构造解析 germ 或全局解；其意义是排除所测试的有限 jet 可解性阻碍。继续增加局部展开阶数不会自动得到 Q1 的 Einstein 非存在性。

Wahl 平滑与奇点主体并非对所有曲率和场数据不可区分：\(T_-^{\rm orb}\)、局部字符、强迫零点和模空间信息均可能改变。Step 93 旧版的过强“所有障碍均转移”叙述由 §8.7 收窄。

## 4. 负 Einstein 几乎 Kähler 几何

### 显式完备非紧模型

[Steps 57–59](workspace/notes/step58_verified_bianchiVIII_AKE_and_closed_zero_locus.md)构造 Bianchi VIII 严格 almost-Kähler Einstein 度量，独立曲率计算确认
\[
\operatorname{Ric}=-3g,\qquad W^-=0,\qquad d\Omega=0,
\qquad |\Omega|^2=2,\qquad |\nabla\Omega|^2>0.
\]
后续网页稿补齐 \(\mathbb R^4\) 上的光滑全局延拓、完备性和与 Fino 问句的联系，见[共同主文](../../../../docs/GOLDBERG.md)。原构造、符号程序和引用关系在此保留。闭负 Goldberg 的紧致量词仍未由这个非紧例子满足。

### 扭率零集与有限阶可实现性

[Step 62](workspace/notes/step62_torsion_zero_prolongation.md)至 [Step 68](workspace/notes/step68_scalar_compatibility_and_radial_multiplier.md)研究 \(N_J\) 的零点、零曲线、局部指数及高阶 prolongation。闭 Einstein 几何要求扭率零集携带 \(5\chi+6\tau\) 的拓扑信息；正指数和某些局部 jet 仍与之相容。符号计算、线性代数和有限阶模型的结果保留各自阶数，不记为精确局部 Einstein 解。

[Steps 77–82](workspace/notes/step80_regularized_torsion_transport.md)把 torsion、Weyl 与典范形式的积分关系放到同一套正则化变量中。完整非紧模型说明部分可积、端通量消失的局部恒等式体系仍容许严格非可积几何；这没有排除紧致极值、零集拓扑、奇异权极限或其他整体机制。

### 作用量、无集中和二阶中心

对 Einstein 度量定义
\[
\widehat S=V^{-1/2}\int s,\qquad
D=\int\left(\frac{s^2}{24}-|W^+|^2\right)
=\frac{\widehat S^2}{16}-2\pi^2(2\chi+3\tau).
\]
对闭 AKE 度量，已有积分恒等式化为
\[
D=T_{\rm AK}:=\int\left(|W_3^+|^2+\frac{3}{32}|\nabla\Omega|^4\right)\ge0.
\]
[Step 83](workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md)利用 Einstein 局部解析模空间，得到 \(\widehat S\) 在每个连通分支上恒定；包含负 KE 度量的分支没有同取向严格 AKE 度量。

在原稿 (N) 的归一化、非塌缩轨形收敛条件下，极限实际形式可去奇点延拓，且 \(W^+\) 能量集中与 \(T_{\rm AK}\) 集中在同一恒等式中异号出现，因此两者均为零。泡为取向匹配的 Ricci-flat Kähler 几何；反手性 \(W^-\) 仍可集中。直径发散和塌缩没有被这个定理覆盖。

[Step 85](workspace/notes/step85_coupled_center_theorem_neck_trace_and_endpoint_reduction.md)在负 KE 背景的形式二阶 Einstein–AK 系统中识别障碍
\[
Q_0(\beta)=|\beta|^2-\fint|\beta|^2,
\qquad \beta\in\operatorname{Re}H^{2,0},
\]
其消失迫使 \(\beta=0\)。在明确的移动领口假设 (H) 下，另证调和自对偶形式的 trace 转移与统一中心常数。

[Step 87](workspace/notes/step87_csck_calibration_and_nodal_endpoint_rigidity.md)用实际 CSCK 比较族校准 \(A_1\) 法向障碍。CSCK 余弦／周期公式和 Hermitian 特征值计算已完成；跨全方向的加权比较、规范调制、相对参数匹配和共同约化中的唯一性仍是该端点刚性定理的输入，详见原稿 §9–10。它尚未成为闭负 Goldberg 的普遍解答。

## 5. O10 的实际载体与当前未决问题

[Step 47](workspace/notes/step47_o10_tn_core_free_at_energy_scale.md)给出 Taub–NUT 上的实际扭率模型。[Step 90](workspace/notes/step90_review_and_tn_projected_charge5.md)进一步精确计算第五幂线丛投影：
\[
\sigma_{\rm TN}=\frac{2048\sqrt6}{2187}\frac{\ell\bar f}{(r+\ell)^3}.
\]
其能量、幅度能量、质量与尾部分布可直接计算。[Step 91](workspace/notes/step91_dense_carrier_consistency_and_wahl_cone_withdrawal.md)说明所构造的形式密集载体满足列出的平均端点恒等式；这只说明这些平均信息不足以决定 O10，不是实际闭流形反例。未闭合信息是相位、联络、标记和外部匹配能否由同一个实际解同时实现。

截至本会话最后记录：

| 目标 | 本会话的实际推进 | 尚未解决 |
|---|---|---|
| Q1 非极小一般型 Einstein 存在性 | 扩展排除的退化架构；转移实际场及完整混合预算；定位 Wahl 局部信息的范围 | 全部小吹起数范围的存在或非存在 |
| Q2 最优全曲率 | 严格次四闭构造；一般 Einstein 核方向负对数节省；指定轨形架构的精确极值 | 光滑全部竞争度量的精确最优值 |
| Q3 非 Bach-flat 光滑全局最优度量 | 排除若干低效泡构型，明确剩余负曲率块主体和取得性条件 | 所要求的全局极小元或普遍排除 |
| Q4 闭负 Goldberg | 完备非紧严格模型；零集分析；作用量、无集中及形式二阶障碍 | 闭流形上的完整证明或反例 |
| 无密度 O10 | 实际局部载体、投影和密度无关平均约束的边界 | 无界密度下的全局统一间隙或实际闭反例 |

Kodaira 全范畴斜率分离沿 FD2—双取向主链进入共同稿，不应把 A01 本会话的局部场分析重复计为那条证明。两项公开问题的证明范围和文献关系以[共同间隙主文](../../../../docs/GAPS_AND_ENDPOINTS.md)及[负 Goldberg 主文](../../../../docs/GOLDBERG.md)为准。

## 6. 后续使用必须接续的修正

以下修正改变了可使用的数学结论，已在上述入口中接回：

- Step 18 修正横向 Riccati 变量；Step 24 修正角向表示重数。旧数值分支不能跨规范直接比较。
- Step 38 的粗网格拟合改善在独立精度上未保持；保留试验结果，不登记为新的有效上界。
- Steps 79–82 收窄“非紧模型排除所有整体证明”的说法：仅适用于明确可积、端通量与极限条件成立的恒等式体系。
- Step 85 的 neck-trace 使用移动领口；法向障碍须按原始尺度归一化。Step 87 的加权调制比较仍待证明，不能以两个不同约化中的“唯一性”直接接通。
- Step 89 的一阶自然线丛方向阻碍与二阶 charge-five 检测有各自假设；一般 first-jet 映射没有自动的 \(H^1\) 控制，秩二截面拓扑不能代替所需 Chern 能量控制。详见 [Step 90](workspace/notes/step90_review_and_tn_projected_charge5.md)。
- Step 91 撤回 Wahl cone mode 计数；相关脚本作为失败路线保留，不是 Einstein 障碍。
- Step 93 §8 修正场转移量词、指数计算与标记范围；Step 94 的旧 \(\ell=n\) 来自不等变 Dirac 算子，已换成正确的 \(2\min\{j-1,n-j\}\)。
- Step 95 最后修订仅排除有限 jet **可解性**障碍，未排除实际全局场的局部强制估计；双 hyperbolic-bolt 闭合的拓扑排除不推广成所有 Bianchi quotient 的分类。

## 7. 文件与计算接续

`workspace/notes` 保存推导、反例和路线决策；`workspace/scripts` 与 `workspace/data` 保存程序、固定参数、精确结果、区间证书和有意义的负结果；`reviews` 保存 TTCS 的数学论证与纠错；`literature` 保存取得的原文、可读文本和引用键。相同文件在整个仓库只保留一份，由来源表连接其不同出处。

未复制可重建的解释器缓存、OCR 页面坐标、空文件、worker 生命周期日志及下列大矩阵。相应代码、参数和数学输出均已保存：

| 可重建数据 | 重建入口与保留结果 |
|---|---|
| `data/step49/quadform_*_A4_K0.npz`、`quadform_H2H2_*_A6_K0.npz` | [step49_kernel_log_coefficient.py](workspace/scripts/step49_kernel_log_coefficient.py)；同名前缀 JSON 记录背景、角阶与二次型结论 |
| `data/step50/wminus_compat_A4.npz`、`wminus_compat_A6.npz` | [step50_wminus_compatibility.py](workspace/scripts/step50_wminus_compatibility.py)；对应 JSON 与 Step 50 精确恒等式 |
| `data/step50/natural_corrector.npz` | [step50_natural_corrector.py](workspace/scripts/step50_natural_corrector.py)；`natural_corrector.json` |
| `data/step64/level6_lam-1.0_s0.npz`、`level6_lam0.0_s1.npz` | [step64_level6.py](workspace/scripts/step64_level6.py)，参数分别 `-1 0`、`0 1`；对应 JSON、[内在二次型程序](workspace/scripts/step64_intrinsic_quadric.py) |
| `data/step67/reconstruct_neg_lam-40_j0.pt` | [step67_reconstruct_phi6.py](workspace/scripts/step67_reconstruct_phi6.py)；已保留相应系数与残差输出，此 checkpoint 用于继续数值优化 |
| `data/step68/flat_mats.npz`、`multiplier_exact.npz` | [step68_flat_cokernel.py](workspace/scripts/step68_flat_cokernel.py)、[step68_multiplier_exact.py](workspace/scripts/step68_multiplier_exact.py)；对应 JSON 与精确有理计算 |

这些材料保存已经发生的研究和当前数学状态。原始脚本中的 Session 相对路径属于执行时的研究环境，运行时按导入后的来源映射定位输入。

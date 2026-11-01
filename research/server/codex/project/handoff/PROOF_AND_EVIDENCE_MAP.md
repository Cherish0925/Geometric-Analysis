# 第一主线：命题—原证明—计算与审读

2026-10-01 新增入口：[全量英文整合稿](20261001_Line1_Integrated_Manuscript.tex)、
[当前研究到正文的映射](../paper/RESEARCH_TO_MANUSCRIPT.md)、
[两网页增量逐件索引](../catalog/web_increment_20261001.json)。
其中 I56 是任意固定有限密度端点，I57 是临界变分选择与同场代价分析，
I58 是普通手术族完整类预算的经典推论。下表保留早期研究的原证明导航。

本表是阅读导航，不重新认证数学。完整逐项范围见 [catalog/results.json](../catalog/results.json)。导出时另生成 `LINE1_RESULT_INDEX.md` 与 `FIRST_LINE_PROOFS.md`：前者从结果目录提取第一线及其递归依赖，后者汇集对应 Markdown／TeX 原证明全文，保留路径和源哈希。它们不以短摘要替代证明，也不声称穷尽档案里的每个引理。

## 1. 障碍主干

| 分组 | 必读原稿 | 对应证据及其范围 |
| --- | --- | --- |
| I01–I03：核心积分校准、极化、全符号 | [独立主稿](../mathematics/current/line1_integral_rigidity_paper.md)，尤其第5–8节；[第4轮源稿](../mathematics/current/round4_rigidity.md)；[应用闭合](../mathematics/current/lebrun_stability_closure.md)；[chamber](../mathematics/current/round13_chamber.md) | [composition记录](../mathematics/current/line1_composition_verification.md)、[closure记录](../mathematics/current/lebrun_closure_verification.md)。实际／理想矩、平滑化、丛 Hessian、弱 Bianchi、平方成本与 Ricci-flat 分支须由正文判断 |
| I07–I09：参数族、能量窗口、双手性 | [泛函](../mathematics/current/line1_functional_pencil.md) → [下包络](../mathematics/current/line1_energy_envelope_gap.md) → [双手性](../mathematics/current/line1_two_chirality_topology.md)；[紧化与上包络](../mathematics/current/line1_compactified_pencil.md) | [泛函审读](../mathematics/current/line1_functional_pencil_review.md)、[双手性记录](../mathematics/current/line1_two_chirality_verification.md)、[搬迁后有限复算](../verification/relocation-checks/results.json)。经典配方／Chern–Weil 与新增微分非饱和分开 |
| I04、I10、I12：实际供给与多类 | [扭曲类](../mathematics/current/round14_twisted_rigidity.md)、[BF对象](../mathematics/current/line1_bauer_furuta_geography.md)、[多类周期](../mathematics/current/line1_period_inertia.md) | [周期记录](../mathematics/current/line1_period_inertia_verification.md)。一个实际类贯穿所需权重；正惯性不等于全矩阵控制；谱尺度和体积归一化不可省略 |

共同机制：真实加权解提供有界场；光滑多项式模型避开特征向量的微分困难；二阶积分预算使弱 Bianchi 自测试合法；同一散度能量的正下界与小上界冲突。这个机制的证明在源稿中，不能以本文代替。

## 2. 允许几何与真实边界

| 分组 | 原稿入口 | 不能替换成的结论 |
| --- | --- | --- |
| I05–I06：解析判据与实际形式 | [有界二形式](../mathematics/current/round21_analytic.md)、[实际供给合成](../mathematics/current/line1_composed_application.md) | 形式上的类不等于真实场；有限二阶量也不自动使联合预算小 |
| I11、I13–I16：乘积与 Weyl 结构 | [任意标量结构估计](../mathematics/current/round17_integral.md)、[调和 Weyl](../mathematics/current/line1_signed_harmonic_weyl.md)、[精确谱应用](../mathematics/current/line1_einstein_spectral_application.md)、[半平坦核心](../mathematics/current/line1_aspherical_no_bubbles.md) | 特定模型不是任意 Einstein Weyl 谱分类；小分裂估计不自动意味着分裂消失 |
| I17–I18、X 条目：等号与适用边界 | [Kähler能量](../mathematics/current/line1_kahler_energy.md)、[非Kähler连接](../mathematics/current/line1_non_kahler_bridge.md)、[Yamabe端点](../mathematics/current/line1_yamabe_endpoint.md)、[熵范围](../mathematics/current/line1_rank_one_entropy_scope.md) | cscK不等于Einstein；积分稀释不构成逐点反例；受限熵比较不排除全部熵方法 |

这些部分的早期与较新版本同时保留。具体程序和输出在各稿相邻 check／review／evidence 路径及结果目录中；不要未经读取就批量执行历史脚本，其中一些带旧路径或覆盖式渲染行为。

## 3. 已成文的精确实现及最新续接

| 范围 | 主阅读入口 | 验证与内部审读 |
| --- | --- | --- |
| I19–I23：早期紧致、饱和与谱刚性 | [9月23日实现组](../continuation/20260923_realization_and_rigidity.md) | [当日记录](../verification/20260923_realization.md) |
| I24–I27：拓扑／双手性／数值强迫与局部范围 | [9月24日全局实现](../continuation/20260924_global_realization.md)、[I24](../continuation/20260924_ale_boundary_compatibility.md)、[I25](../continuation/20260924_bilateral_realization.md)、[I26](../continuation/20260924_chern_boundary_realization.md)、[I27](../continuation/20260924_local_to_global_scope.md) | [globalization记录](../verification/20260924_globalization.md) |
| I28–I31：覆盖、局部修正、塌缩、轨形 | [frontier组](../continuation/20260924_frontier_bridges.md)、[轨形与平滑](../continuation/20260924_orbifold_smoothing_bridge.md) | [frontier记录](../verification/20260924_frontier.md) |
| I32–I34：回路数据、完整核、带标记核心 | [global-data组](../continuation/20260924_global_data_realization.md)、[完整核修正](../continuation/20260924_integrable_kernel_cyclic_repair.md)、[contact/Milnor匹配](../continuation/20260924_harmonic_contact_milnor_matching.md) | [内部审读](../verification/20260924_global_data_review.md)、[有限检查](../verification/20260924_global_data_checks.json) |
| I35–I37：薄纤维单值群、非线性慢模态、核心尺度 | [最新实质研究入口](../continuation/20260924_global_structure_and_scales.md)、[thin monodromy](../continuation/20260924_thin_monodromy_alternative.md)、[slow moduli](../continuation/20260924_nonlinear_slow_moduli.md)、[实际规范能量](../continuation/20260924_moduli_energy_gauge.md)、[harmonic zero scale](../continuation/20260924_harmonic_zero_scale.md) | [内部审读](../verification/20260924_structure_scales_review.md)、[有限检查](../verification/20260924_structure_scales_checks.json) |

I24 不要求预设饱和不等于所有实现都无条件。I30 的良好大区域不是全局纤维化。I31 的 KE 轨形不是原光滑类型上的 KE；I34／I37 仍需带标记匹配与单独的全局复平滑输入。I35 已给定曲面丛；I36 的固定幅度分离限于保纤维乘积，不能升级为排除全部 Einstein。

## 4. 三条科学主线之间的依赖

保留[完整研究地图](../navigation/RESEARCH_MAP.md)中的构造线与全局线：A1/log-Weyl、E_D、固定闭整数剪切是不同构造；普通基本类、非虚Kähler与对称性限制不是全体Einstein不存在性。第一线使用这些对象作应用或反例时，必须连同构造的逐点估计、光滑类型及全局范围读取。

因此当前审读包携带整个 `mathematics/current/`，而不是只按文件名抽取 line1。更早的过程来源留在完整包 `archive/sources/`，来源目录保留具体原路径和 SHA-256。

## 5. 证据等级

原证明承担数学论证；代数程序与计算输出支持所测有限恒等式；内部审读记录说明谁检查过哪些部分；文件哈希证明字节保全。四者不能互相替代。旧记录里的文件数、页数、通过数和目录项数均是当时快照，不是当前独立定理数。

已有纲领与最新网页评论是研究指导，不进入 theorem 列表。下一步应以新的统一障碍、真实锐利性、实际应用或精确实现为交付，而不是继续解释为什么研究有思想。

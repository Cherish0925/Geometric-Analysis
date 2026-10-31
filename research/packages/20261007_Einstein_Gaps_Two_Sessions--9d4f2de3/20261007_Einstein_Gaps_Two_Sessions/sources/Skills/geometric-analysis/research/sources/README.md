# Yau26：长期研究总入口

The current English mathematical manuscript is [Integral Einstein Rigidity and the Geometry of Monopole Defects](paper/Integral_Einstein_Rigidity.tex), also included in the [Geometric Analysis Skill](skills/geometric-analysis/research/Curvature_Realizability.tex). It retains the month-wide proofs, the complete September 29–30 web integration, and the October 3 actual-field and curvature-interaction connections. Editable sections and build instructions are in [paper/README.md](paper/README.md). Earlier sources and handoffs remain unchanged.

本工程把三条科学主线及后续第一主线的集中研究放在同一处。它保存原始推导、程序、论文、来源与修订过程，不以新综述替代旧证明。2026-09-23 建立；原目录、运行会话、已安装 Skill 均未修改。

## Geometric Analysis：独立研究 Skill

2026-10-04，新建 [Geometric Analysis](skills/geometric-analysis/SKILL.md)，主题为
**曲率方程的可实现性及其定量结构——拓扑约束、实际场与极值几何**。
它将精确解、逼近、极值构造和退化与定量障碍一并组织，不以 O10／O11 代替整个研究。
[知识树与证明图](skills/geometric-analysis/references/research-map.md)、
[当前数学结论](skills/geometric-analysis/references/results-and-questions.md)和
[完整文本库](skills/geometric-analysis/references/source-library.md)都在同一个可移植目录中。
原项目继续保存计算程序、运行记录和源包；新 Skill 保存去重的数学文本与全部来源别名。
构建入口为 `tools/build_geometric_analysis_skill.py`，不会改写原数学文件。

## 从哪里开始

**10月3日科学概要整合：**以“实际场、曲率相容性与 Einstein 几何”为数学主题，
新版[阅读概要（TeX）](handoff/20261003_Einstein_Compatibility_Overview.tex)与
[PDF](handoff/20261003_Einstein_Compatibility_Overview.pdf)接回当前完整正文。
[网页原稿](archive/sources/20261003-scientific-overview/Line1_Scientific_Overview_20261003.tex)
原样保存；[七节对应与14篇文献入口](catalog/web_increment_20261003.json)逐项定位。
新增[英文数学节](paper/sections/field_interfaces_and_curvature_interactions.tex)明确
抽象场接口、谱缺陷、Weyl 与标量的联合成本，以及局部节省如何按实际复制比例影响首项。
当前无密度 O10 与最优 O11 仍开放；这次整合不新增定理编号。
该轮仅整合概要；独立 Skill 已在后续以 `geometric-analysis` 建立，见上面的新入口。

**10月1日增量整合：**两网页原包及全部附件已原样保存在
[增量来源目录](archive/sources/20261001-web-increment/)。新的连续英文稿补入
任意固定有限密度 O10 的两条证明、多项式密度损失、无密度径向分析，以及 O11
的临界变分选择、普通手术族完整类预算和同场分解。
[当前任务](guidance/LINE1_CURRENT.md)与[知识图谱](navigation/RESEARCH_MAP.md)
已同步更新：**有限密度 O10 已成文；无密度 O10 与原平衡族最佳首项仍开放。**
来源到正文的对应见[论文映射](paper/RESEARCH_TO_MANUSCRIPT.md)和
[本次来源索引](catalog/web_increment_20261001.json)。

9月29日的[第一主线综合稿（独立 LaTeX）](handoff/20260929_Line1_Synthesis.tex)与[PDF 阅读版](handoff/20260929_Line1_Synthesis.pdf)汇合最近两轮本地讨论、最新网页意见和 N1 补充：包含知识树、证明依赖图、研究演化、两种类平方成本、极值归约、慢模态及固定 E_D 的范围修正，以及连续主论文的有限完成事项。O10、O11仍分别开放；原始分析证明按文末来源定位保留。

此前交流使用[9月28日完整续研阅读包](handoff/20260928_REVIEW.md)：覆盖上次全文快照844e62f之后的七次研究提交，十一份新数学稿及技术前置、完整核查和外部指导，合为12份MD与对应TeX。ZIP约915 KiB，不含脚本、缓存或运行日志。[上一份近期包](handoff/RECENT_REVIEW.md)与[更早八卷正文版](handoff/COMPACT_READING.md)继续保留。各包均按主题合并原稿，不以摘要替代证明；不需上传303 MB来源档案。[完整来源交接入口](WEB_REVIEW_START_HERE.md)保留历史档案范围与追溯说明。

| 需要理解什么 | 阅读入口 |
| --- | --- |
| 第一主线的稳定成果主干、已成文延伸与当前真正重要的工作 | [第一主线当前入口（更新至2026-10-03）](guidance/LINE1_CURRENT.md)；[上一轮助手完整分析](guidance/source/20260926_assistant_priorities.zh.md)；[用户转交的网页完整分析](guidance/source/20260926_user_web_backbone.zh.md) |
| 三条主线各自解决什么、当前最强结论与尚未闭合的连接 | [三主线研究地图](navigation/RESEARCH_MAP.md) |
| 从早期会话、十二轮、十三至二十一轮到第一主线深化，思想怎样发展 | [研究演化与因果脉络](navigation/EVOLUTION.md) |
| 哪些是当前结论，哪些是旧版、受限结论或被纠正推断 | [结论与修订](navigation/CLAIMS_AND_CORRECTIONS.md) |
| 长期研究视野与原始宪章（具体状态使用上面的当前入口） | [第一主线研究宪章与续接](guidance/LINE1_CHARTER.md)；[用户提供的中文原文](guidance/source/20260923_user_research_charter.zh.md) |
| 最新实质研究及其完整证明 | [有限密度端点](paper/sections/finite_density_endpoint.tex)；[原缺陷到定量密度损失](paper/sections/web_primitive_rate.tex)；[变分选择与全局代价](paper/sections/variational_selection_and_global_cost.tex)；[两网页原文](archive/sources/20261001-web-increment/Line1_Web_Increment_20260929_30/) |
| 可改进的研究方法与工具入口 | [项目研究 Skill](skills/line1-research/SKILL.md)；不是已部署的运行系统 Skill，不限制替代方法 |
| 本次推导、交叉复核、原文保存与验证范围 | [局域首项与全局通量核查](verification/20260928_localization_and_global_flux.md)；[前置：区域成本与实际交换子核查](verification/20260928_relative_cells_and_actual_bracket.md) |
| 查某份原稿、旧会话、上传包、Skill 或复算证据 | [原始来源地图](navigation/source-discovery.md)；[档案使用说明](archive/README.md) |

`mathematics/current/` 完整保留建立本工程时的 884 文件研究基线，内部相对路径不变。其中 `skill/` 是当时的知识快照，不代表后续所有研究已经安装到系统 Skill。该目录也保留旧轮次与旧说明；“current”表示本次继承树，**不是目录内每个历史断言都仍有效**。判读优先使用上面的结论与修订表。

## 三条主线没有合并成一条

1. **刚性与定量障碍**：实际规范输入、积分校准、经典障碍的定量加强、参数泛函、双手性可行区域，以及允许谱的结构与实现问题。
2. **近 Einstein 构造**：分别保留 A₁/log-Weyl、E_D、固定闭剪切拓扑；还包括完整算子、全模态响应、非线性修正及未完成的其他输入对象。
3. **全局判定**：同一光滑流形上的全部 Einstein 输出、基本群与基本类、虚非 Kähler、对称性、正分支、代数平滑、连接器与全局匹配。

第一主线的 A“障碍”、B“允许几何”、C“精确实现”是它内部的三个问题，不取代整个项目的三条科学主线。原题仍未解决；当前附加条件下的定理不等于维数独立之外无其他依赖的 Yau26 阈值。

## 第一主线先看稳定主干，再看最新延伸

9月28日继续得到[I53](continuation/20260928_intrinsic_caps_and_stability.md)：仅由小 C0 振幅与小全曲率积分，构造精确匹配原领口的低能量帽。部分吹降将少量坏核心的代价明写入公式，得到无规范、无常标量前提的首项下界。所选实际恢复序列的**任意收缩 C0 邻域内**，全部光滑度量的归一化下确界趋于4；允许任意微分同胚拉回，也不要求幅度相对 h 的速率。更一般地，只需绝大部分吹起具有平均振幅小的长标记环带。尚未证明任意近极小序列都具有这些环带，故全部度量首项仍开放。这一推进没有依赖修复 X09 所否定的精确规范。

9月28日的[实际构造 X09](continuation/20260928_marked_centers_and_harmonic_slices.md)证明：两列相对 C0 趋近、均有首项4且规范残差也趋零的恢复度量，仍可能不存在一致控制的固定基底精确 Bianchi 规范。收缩核心的标记位置与唯一极限调和映射产生冲突。允许中心移动后，该构造被精确纳入恢复族；I52 的紧致配置族与共形／微分同胚扩展也已证明。X09 本身仍满足近似规范判据，不是更低首项的反例。一般弱零端与全部度量首项仍未解决。本轮继续研究并保存完整证明，没有制作或发送网页包。

从 e75105d 继续的[首项稳定性证明 I52](continuation/20260927_endpoint_covariance_and_surgery_limits.md)已推进到复双曲收缩手术恢复序列的统一邻域定理：明示 TT／常标量 Bianchi 规范内，任意趋零幅度都不能将首项降到4以下，不要求导数界、相对 h 的速率或终点竞争能量。正二次余项还给出首项等于4的必要充分条件；非零规范误差可以按幅度加权纳入。一般度量的统一规范归约与全部度量首项仍未完成。零端则准确保留了尚未受控的单位扭率相位曲率。本次继续更新同一工程，不制作新的网页包。

9月27日从 `e58b867` 接续，[I51 的完整证明](continuation/20260927_constant_weight_and_global_fit.md)以同一个常权重实际解分解全部有限参数缺陷，分别控制 Ricci 与 Weyl 贴合误差，得到全度量 `（1+b_a）（r+P_t/V）≥c t²(1−2t)²`。它将此前纯积分版本的零端三次间隙提高到二次，并加强同一实际拓扑范畴的上能量壁；不添加点态 Ricci、Euler 密度、直径或 Sobolev 假设。高指数核心的延拓代价与分裂零点模型、平衡族的曲率作用抵消也纳入同一正文。**一般弱零端的非退化间隙和最佳首项仍开放**；原始任务书及当前证明依赖见[当前入口](guidance/LINE1_CURRENT.md)。未制作或上传新的网页包。

第一主线的中心仍是**实际规范输入 → 曲率方程的微分相容性 → 定量非饱和 → 全局拓扑间隙**。已有积分主稿、极化全符号应用、参数族及其紧化、双侧能量窗口、双手性拓扑应用和实际 BF／扭曲供给构成连续主链；LeBrun 经典输入与新增分析分别归属。受限 Einstein／KE 实现是正面延伸，不把原障碍论文变成必须等待所有退化问题的无限工程。

2026-09-26 的[合并指导](guidance/LINE1_CURRENT.md)恢复“已有主成果—已成文延伸—开放目标”的阅读顺序。整个核心填充、统一慢模态分类与全局转移保留为候选；其中“核心填充优先”仅指扩大存在性范围，不取代整条主线的规范／拓扑研究。本次指导归档没有新增定理。

同日晚间的[数学续接](continuation/20260926_boundary_compatibility.md)继承实际场后补出统一近闭合估计，证明标准符号类的联合矩阵证书受经典标量预算控制，并构造真实小 h 家族。**9月27日的[线性证明](continuation/20260927_mixed_current_and_signed_cores.md)已将该家族的下界由 h² 提高到 h，与既有 `4h/(1+h)` 上界同阶。** 随后的[持续推进](continuation/20260927_conformal_separation_and_zero_end.md)又闭合去标量方差的 `Σ≤C(P_Ric+D₂)`，给出真实 BF 新排除带，并证明零端的曲率尺度退化、精确 Einstein 的 Euler 密度间隙及相应非退化上能量壁。最优首项系数、无几何假设的零端弱间隙及无直径精确实现仍分别开放。按用户要求，本次不重新打包网页交付。

[覆盖与锐利性续接](continuation/20260927_covering_geometry_and_sharp_subfamilies.md)进一步给出局部万有覆盖塌缩的必要性，以及真实平滑输入下无直径的近 Einstein 零端间隙；对只添柄子族计算全部度量的精确下确界；将最佳系数问题的逆手术要求降为单侧 Weyl 帽成本，并给出完整领口的精确代价与反例。其后的 I45–I46 去掉有界 Ricci 范畴的各球小能量条件，识别了两个真实局部旋量允许类。

[完整核心与极值续接](continuation/20260927_full_core_cost_and_extremal_metrics.md)算出这些允许商的整个光滑填充的锐利曲率代价，并排除忠实行列式的 Ricci-flat ALE 延拓；椭圆曲率类中以小局部积分 Ricci 预算替代逐点界。普通实际 SW 解的精确余量又与 Cotton/变分方程连接，强迫平衡族光滑低能驻点保留点态缺陷。

最新[有符号能量与共形流续接](continuation/20260927_signed_balance_and_conformal_flow.md)将三项静态预算接到实际共形 Ricci 流：平衡族虽有积分缺陷趋零的真实近极小化输入，其最大光滑流时间仍有统一上界。另用固定光滑曲面乘积上的实际未扰动 SW 解证明 Weyl 支付系数 2 锐利；它不能从通用有符号估计中删去。完整 Hessian 将极值稳定性归约到明确 TT 二次型，驻点／Sobolev 范畴还取得独立零端间隙与有条件的实际终端核心提取。**平衡族系数 4、一般弱零端、完整核心场匹配及 Yau26 仍未解决。** 此前各轮按用户要求暂不打包；现依新的交流请求，已制成本地全文阅读包，未上传外部平台。

此前实现续接的三处扩大也继续保留：小回路形变迫使有限单值群或共同多曲线，因此不可约单值群下不再预设厚纤维即可实现负 KE；真实双曲纤维族得到完整非线性慢方程，其实际双手性泛函缺陷精确等于模参数能量与 Ricci 残差，允许固定振幅的近 Einstein 序列；总缺陷与整块核心尺度的四次方比较，替代此前的调和形式无零点假设并接上带标记 Milnor 匹配。各项保留其输入条件，不合称无条件二分定理。此前的[全局数据与完整核](continuation/20260924_global_data_realization.md)、[覆盖输入、塌缩和轨形桥梁](continuation/20260924_frontier_bridges.md)、[紧致范畴实现](continuation/20260924_global_realization.md)、[前一阶段成果](continuation/20260923_realization_and_rigidity.md)和旧版[实现证明](continuation/20260923_compact_realization.md)均保留。负 KE 已经满足原题的存在性输出要求。

## 查证与继续工作

```bash
python3 tools/library.py verify
python3 tools/library.py find 'round12'
python3 tools/library.py find 'Fable'
python3 tools/library.py find '闭合稿'
```

`find` 搜索文件来源与路径；数学内容可用 `rg` 在 `mathematics/current/`、`continuation/` 或指定历史来源中搜索。旧档案包含已纠正文字，不能将全文命中直接视为有效定理。

新增研究写入 `continuation/`，结果成熟后更新导航与结果目录；需要修订时写明替代关系，保留原版本。不要每轮再复制一套无差别的“最新总论”。原始档案不编辑、不执行；检查程序的适用范围与原日志一起保留。

本工程的文件校验、计算复现和数学证明审读是三件不同的事。哈希相同说明字节保全，程序通过说明所测计算通过，都不自动证明 PDE、拓扑结论或世界首创性。

本次具体覆盖范围、复算结果以及尚未找到的外部原件，见[整理与研究交付记录](verification/INTEGRATION.md)。交付归档内另附 Git 历史包与恢复说明；即使旧 runtime 工作树不再可用，仍可读取全部文件并恢复本地研究历史。

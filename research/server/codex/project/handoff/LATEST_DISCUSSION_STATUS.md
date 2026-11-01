# 最新讨论入口与历史记录

2026-10-01：两网页9月29–30日的新增证明已接入
[完整英文稿](20261001_Line1_Integrated_Manuscript.tex)，全部原件见
[来源目录](../archive/sources/20261001-web-increment/)，逐件对应见
[来源索引](../catalog/web_increment_20261001.json)。
当前结论和继续工作以[第一主线当前入口](../guidance/LINE1_CURRENT.md)为准：
任意固定有限密度 O10 已成文；无密度 O10 和原平衡族最佳首项仍开放。
以下保留9月27日讨论原貌，不以其中的历史开放状态替代当前状态。

## 2026-09-27 讨论的保存与定位

## 从 168bea5 继续：线性代价与最佳阶已闭合

用户的新[临界混合项核查文件](../guidance/source/20260927_web_critical_mixed_term.zh.md)逐字保存。[最新完整证明](../continuation/20260927_mixed_current_and_signed_cores.md)先按来源吸收该文的混合项与曲率关系，再证明新的 β=2 精细 Hessian—弱 Bianchi 吸收。其结果不再停在集中必要性：`p−T₊≤C(rV+D₂)` 给出全度量窗口 `E+(U−1−h)₊≥ch`，在原真实小 h 家族上确定 `inf E≍h`。

另有带平方短缺成本的版本，以及低能逆手术帽下系数 4 的匹配。它们的准确范围在同一正文中，不将受限系数推成全部度量的最优常数。不声称已证明 `Σ≤C(P_Ric+D₂)` 或零 Weyl 端统一间隙。下一次网页审读可以直接发送这份新证明和[核对记录](../verification/20260927_linear_cost.md)，不必重传303 MB档案。下文为保留的历史讨论，当前状态以本节、I40及当前入口为准。

线性定理成文之后还继续推进了零端：新稿第8节把 I39 的扭率平均质量加强为所有 `L^q_avg, q<2` 的模长收敛，并证明正则化耦合能量恒等式。下一障碍是低扭率区中的实际曲率与边界通量；不能把 β=2 的正旋量有符号核心结论移植到另一手性的扭率丛。

## 从 f48f385 继续：实际能量与拓扑集中

最新[执行书](../guidance/source/20260926_web_parallel_execution.zh.md)及[两份评议与用户请求](../guidance/source/20260926_user_topological_cost_discussion.txt)完整保存。新增[证明正文](../continuation/20260926_actual_topological_cost.md)包含两项不同但共享实际场预算的推进：带符号正 Chern 代价的过渡层四次能量局部化，以及零端三次扭率场的弱 Dirac 方程。普通解与加权解之间的疑问用同一个加权解上的精确恒等式处理，不假设解可连续比较。

两项均未升级为零端统一间隙或小 h 线性下界。前者剩临界混合集中与扭率零集特征数；后者剩 `Ah` 尺度的四次集中。I37 选定模型还直接有 `liminf r>0`，不构成完整 PDE 匹配的反例。本轮没有重新研究标准 BF 符号枚举或宣称解决固定 E_D。后续网页阅读可先传这一份新证明，不必重复上传八卷或运行档案。

## 八卷交付后的两份新原件与证明续接

已完整保存下载目录里的[八卷综合研判](../guidance/source/20260926_web_eight_volume_synthesis.zh.md)和[研究主线深化与证明方案](../guidance/source/20260926_web_boundary_proof_program.zh.md)，以及用户转交的[通用性指导及讨论全文](../guidance/source/20260926_user_generality_and_parallel_guidance.txt)、[新报告请求](../guidance/source/20260926_user_boundary_program.txt)。[接收记录](../guidance/source/20260926_boundary_guidance_receipt.json)逐件记载来源和哈希。未复制完整执行日志，未对外上传。

本地推导见[单份续接证明](../continuation/20260926_boundary_compatibility.md)。网页的联合矩阵判据保留来源归属；本地进一步将“标准符号类可能冗余”落实为带有限 Ricci 误差的明确定理。小 h 构造得到经典拼接支持的显式上界；零端供给成立但弱误差排除尚未证明。更详细的研究状态已并入[当前入口](../guidance/LINE1_CURRENT.md)，不再要求网页从所有旧对话中拼接状态。

以下保留八卷之前的累计讨论，不用新反馈覆盖它。

本轮保留最近五段完整消息：[此前网页的范围与成熟度分析](../guidance/source/20260926_user_web_scope_and_maturity.txt)、[助手的范围与优先级](../guidance/source/20260926_assistant_scope_and_priorities.md)、[用户要求解释数学思想](../guidance/source/20260926_user_request_for_mathematical_insight.txt)、[助手的核心机制解释](../guidance/source/20260926_assistant_core_mechanism.md)、[用户粘贴的两篇最新网页分析及本轮请求](../guidance/source/20260926_user_web_maturity_and_mechanism.txt)。此前长期宪章、上轮主干分析与助手优先级原文仍在 `guidance/source/`，没有被新消息覆盖。

来源是当前对话中准确选定的消息正文，不是新取得的网页导出；没有复制完整私有执行日志。字节数、时间、消息定位和 SHA-256 见[提取记录](../guidance/source/20260926_selected_messages.json)。网页原文中的 `:chatgpt-content-reference{...}` 原样保存；它们不是本工程可解析的文献链接，不为它们编造来源。

## 已有成果、正确解释与研究提案分别登记

1. **第二正惯性无需控制全部负项 N：已有结论。** [period-inertia](../mathematics/current/line1_period_inertia.md)式(5)、(7)及第5节已有 Q 的秩一正项＋R−N 分解与极小极大论证。网页解释正确，但不是本次新发现。只有恢复完整交叉矩阵、负向结构或其他明确目标时，才另论 N；不将“先控制所有 N”设为普遍任务。
2. **保留低能谱变量：研究路线，不是已证联合规范定理。** 高频余项的标准谱投影估计说明如何避免把全部慢变化压成常数。低能系数与实际规范方程、配对和全局转移的共同相容性仍需证明。
3. **F(h)−(1+h) 的二阶分离：已有恒等式。** [energy-envelope](../mathematics/current/line1_energy_envelope_gap.md)第2节式(7)已写出 `4h²/(1+sqrt(1−3h))²`。网页重新推导不增加定理；它也不证明相对缺陷间隙的 h² 速率最优。
4. **KE端与零端分别检验：保留。** [compactified-pencil](../mathematics/current/line1_compactified_pencil.md)明确未宣称零端三次损失锐利。真实 KE 的二次校准不能代替另一端的实际序列。
5. **退化线性化的两个标量例子：方法说明。** 相同小特征值可对应唯一解或邻近分支，说明必须分析完整非线性；不是已经构造出新的 Einstein 度量。
6. **相容填充与指定调和形式无零点不同：开放实现目标。** 不把辅助形式的成功当作唯一可能路径，也不把辛填充、复平滑和精确 KE 混为一个接口。
7. **同一散度能量上下界：已有主证明的解释。** 原稿第4轮与独立主稿都包含该机制；本次解释不算新增理论或外部认证。

## 当前实际取舍

保持障碍主干；联合类研究需要超过既有正惯性／小谱替代；锐利性用同一适用范畴的真实几何检验；实现分支选择一个完整目标持续研究。原有核心证明已成文的部分不重复布置，必要的实质缺口不能以脚本或积极评价替代。

公开／投稿不是本次操作。这里记录的是证明、理论、应用、可使用性四种成熟度；不承诺“无人能继续改进”，也不把所有未来开放问题设置为现有论文的前置条件。此前 [当前指导](../guidance/LINE1_CURRENT.md) 继续有效，以本文的 N／已有恒等式定位作精确补充。

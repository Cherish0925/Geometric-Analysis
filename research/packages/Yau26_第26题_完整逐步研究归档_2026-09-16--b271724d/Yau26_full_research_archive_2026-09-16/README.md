# Yau 第26题研究完整归档（2026-09-16）

本归档是对当前可访问的 Yau26 研究记录所做的**证据分层、逐步追踪、推导级重构与错误清洗**。目标不是写一份简短汇报，而是让后续研究者/求是引擎能够继续研究，同时避免把旧的探索性猜测、数值证据、被撤回的论证或局部模型误当成定理。

## 当前总状态

- 当前研究采用的工作命题是“Ricci 夹逼 ⇒ 同一光滑流形上存在某个 Einstein metric”。
- 1982 年 *Seminar on Differential Geometry* 的 Problem Section 已定位，但**原始 Problem 26 的题页、原句与完整量词仍未逐字核定**。正式声称“解决 Yau Problem 26”之前必须再次核验。
- 在当前工作命题下，\(n=2,3\) 可由经典理论处理；真正困难从 \(n=4\) 开始。
- \(n\ge4\) 的完整、无附加假设版本**没有在当前记录中被证明或反驳**。
- 四维负分支的 Ishida–LeBrun 临界路线最成熟，已经形成 gauge-theoretic calibration + selected-support smoothing + terminal recalibration + local forbidden-germ 的完整研究架构，但还不应声称为独立发表级、族一致的最终定理。
- 四维正分支已形成 noncollapsed orbifold/ALE + Eguchi–Hanson obstruction projection + product-orbifold multi-node Kuranishi/Green interaction 路线。
- graph/surface-bundle 路线仍缺“同一 smooth type 同时拥有 \(\delta\to0\) 输入与全 Einstein 不存在”这一决定性合并。
- \(n\ge5\) 缺少四维的 gauge/Chern–Weil/\(\Lambda^2_\pm\) 工具链。
- Lean 仅形式化了少量有限维代数恒等式。

## 本归档包含

- 最新状态与核心结论；
- 原命题的量词与 normalized branch 逻辑；
- 所有重要原创突破、原理、构造与推导；
- Step 1–100 合并账本；
- IL 临界分支、ALE/EH、Moser/退化流、正分支、graph/Koiso、高维的专题推导；
- 所有重要撤回、错误修正与 supersession；
- 结果证明等级；
- 当前未解决缺口；
- 服务器 artifact / File Library 文件索引；
- 核心公式 TeX；
- 机器可读的 CSV/JSON；
- 上一轮 2026-09-15 的本地总结文件（若当前 sandbox 仍可访问）。

## 状态标签

- **A / 已闭合**：来源和推导可复核，且未被后续记录撤回。
- **B / 强内部结果**：推导链较完整，有脚本/交叉核验，但尚未达到独立发表级审计。
- **C / 条件性接口**：依赖额外几何、PDE、紧性、gluing 或 global topology 假设。
- **D / 数值/有限维证据**：用于路线判别，不是 continuum theorem。
- **X / 已撤回或 superseded**：只保留历史价值，禁止再次当作结论引用。

## 关于“原始得到的文件”

File Library 中跨会话的 `meta_trace_report (93/94/95)`、`Yau26_synthesis.*`、`Yau26_Ricci_pinching_research.md`，以及求是引擎服务器上的 `workspace/...` 是**文件引用，不是当前 Python sandbox 中可复制的 raw bytes**。因此本 ZIP 不伪造“已复制原始文件”，而是：
1. 打包当前 sandbox 中可直接访问的产物；
2. 保存完整 path-level artifact inventory；
3. 保存 File Library source index；
4. 把核心数学内容重新整理为可独立阅读的 Markdown/TeX/CSV/JSON。

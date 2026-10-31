# 丘成桐（Yau）问题集研究交接说明

> 用途：将此前关于 **Shing-Tung Yau《Problem Section》问题集**的讨论迁移到新的会话继续研究。本交接文件只负责恢复研究背景、候选问题与此前形成的判断；进入新会话后，仍应重新核查截至当前日期的最新论文、预印本和公开结果，不能把本文件中的“开放状态/优先级判断”当作免复核事实。

## 1. 总体背景

我们讨论的是丘成桐 1982 年发表于 *Seminar on Differential Geometry*（Annals of Mathematics Studies 102）的经典 **Problem Section**。原问题集共约 120 个问题，覆盖微分几何、曲率、极小曲面、谱几何、Kähler 几何、调和映射、广义相对论等多个方向。

此前研究目的不是简单罗列“还有哪些题没解”，而是：

1. 找出截至 2026 年仍具有真实开放核心的问题；
2. 判断哪些问题最适合当前 AI/Agent 系统进行**严格、可验证、能够形成真正新数学知识**的攻关；
3. 优先选择问题定义清楚、成功标准明确、现有理论边界清晰、能够通过证明/计算形成高质量反馈的问题；
4. 最终目标是解决原始开放问题本身，而不是把某个容易很多的受限版本包装成“解决了 Yau 问题”。

此前使用的重要整理资料为：

- `two_major_open_problem_list.md`
- `two_major_open_problem_list.pdf`

如果新会话可以访问这些文件，应优先读取；如果不能访问，本交接文件已经保留核心结论。

---

## 2. 此前重点核查过的 Problems 18–32

此前曾集中讨论 Yau Problems 18–32，并筛出当时仍具有明显开放核心的一组候选。此前讨论中重点保留的是：

**19、20、22、23、25、26、28。**

这不是说其他编号完全没有开放问题，而是这些题在当时的状态核查中仍保留了比较明确的原始开放核心。

### Problem 19：Pontryagin/Chern-Weil 曲率形式的实现问题

核心问题：给定代表 Pontryagin 类的闭 $4k$-形式，能否找到一个 Riemannian metric，使该形式恰好由其 Levi-Civita 曲率通过 Chern-Weil 构造实现？如果不能，完整的拓扑/微分几何障碍是什么？

此前状态判断：**开放。** 第一 Chern 类的 Kähler 情形与 Calabi–Yau 理论相关并已得到经典解决，但高阶 Pontryagin/Chern-Weil form 的 Levi-Civita 实现问题没有一般必要充分条件。

研究特点：概念深、涉及全曲率张量和非线性 PDE/微分拓扑；原创价值高，但反馈相对稀疏，完整解决难度很大。

### Problem 20：规定 Einstein tensor

核心问题：给定紧致流形上的对称张量 $T$，寻找 metric $g$ 使其 Einstein tensor 等于 $T$，并刻画必要充分条件；带边界时还要确定合理边界条件。

此前状态判断：**作为全局 prescription problem 仍开放。** 局部 prescribed Ricci 理论已有重要结果，但不存在完整的全局必要充分条件。

研究特点：和 Einstein 方程、几何 PDE、gauge fixing、Bianchi identity 紧密相关；理论意义很大，但全局问题极宽，AI 要直接终结原题难度极高。

### Problem 22：正 Ricci 曲率完备流形的基本群

核心问题：刻画 complete positive-Ricci manifolds 的 fundamental groups，特别是非紧致情形。

此前状态判断：**完整正 Ricci 情形仍开放。** 非负 Ricci 情形近年来已有反例推翻一些旧的 finite-generation 预期，但这些不能直接替代严格正 Ricci 的分类问题。

研究特点：几何、群论、拓扑、极限空间高度交织；价值高，但目标“characterize”较宽，不如尖锐不等式/明确命题适合当前 Agent 形成闭环。

### Problem 23：K3 的显式 Ricci-flat metric 与四维 Ricci-flat 分类

包含两个方向：

1. 给紧致 K3 surface 写出真正显式的 Ricci-flat metric；
2. 四维是否存在不被 torus 或 K3 有限覆盖的 Ricci-flat manifold，例如 $S^4$ 或 $S^2\times S^2$ 是否可能具有 Ricci-flat metric。

此前状态判断：**仍有明确开放核心。** Yau 定理证明 K3 上 Ricci-flat Kähler metric 的存在唯一性，但不是 closed-form explicit formula。

研究特点：显式 K3 metric 很适合数值/符号/AI 辅助探索，但从高精度近似跨越到 exact closed-form identity 极难；分类方向又非常深。

### Problem 25：四维负 Einstein manifold 的分类

核心问题：分类 compact four-dimensional Einstein manifolds with negative Ricci curvature；特别问 $S^4$ 是否可能带负 Einstein metric。

此前状态判断：**开放。** Hitchin–Thorpe、Seiberg–Witten 等给出大量限制，但离完整分类很远；$S^4$ 的负 Einstein 问题仍是清晰特例。

研究特点：地位高，但“完整分类”尺度极大。若攻关，最好先问清晰的二元子问题（例如 $S^4$ 是否存在负 Einstein metric），但必须承认这只是原题中的核心子问题而不是完整分类。

### Problem 26：Ricci pinching 是否强迫存在 Einstein metric

核心问题：是否对每个维数 $N$ 存在只依赖 $N$ 的 Ricci pinching 常数，使满足相应双边 Ricci pinching 的紧致流形必然承认某个 Einstein metric。

此前状态判断：**一般形式开放。** 现有强结果通常还需要 full curvature、非塌缩、导数控制、Ricci flow 稳定性等附加假设。

研究特点：命题相对明确，存在“证明/反例”两条出口，理论结构比分类题更适合 AI；但关键困难是 Ricci tensor 本身不控制 Weyl curvature。

### Problem 28：正标量曲率的四维 compact Einstein manifold 分类

核心问题：分类所有 compact four-dimensional Einstein manifolds with positive scalar curvature。

此前状态判断：**一般情形开放。** Kähler/Fano、某些 Weyl-curvature 条件、特定对称性等重要子类已有深刻结果，但纯 Riemannian 的整体分类远未完成。

研究特点：数学地位很高，但完整分类面过宽；不属于“有限、清晰、可快速证伪”的类型。

---

## 3. 后来跨越 18–32 后重点讨论的四个候选

在继续扫整个 Yau 问题集时，此前讨论逐渐集中到以下几个更值得 AI 系统研究的方向：

### A. Problem 109 —— 极小子流形的尖锐等周不等式

这是此前讨论中**最值得作为理论旗舰候选之一**的问题。

原问题：若 $\Omega$ 是 $\mathbb R^N$ 中一个 $k$ 维紧致 minimal submanifold，希望证明与欧氏 $k$ 维球完全相同的 sharp isoperimetric constant：

\[
\operatorname{Vol}(\Omega)^{k-1}
\le c_k\operatorname{Vol}(\partial\Omega)^k,
\]

其中 $c_k$ 是欧氏单位球给出的最优常数。

截至此前资料整理：

- 一般较弱常数的不等式早已知道；
- Simon/Michael–Simon 等提供经典非尖锐 Sobolev/isoperimetric 机制；
- Simon Brendle 在 2021 年 *JAMS* 的工作证明了欧氏 sharp constant 在 **codimension ≤ 2** 的情形；
- equality case 是 flat round ball；
- **codimension ≥ 3 的完整 sharp statement 仍开放**；
- 2024–2026 的 ABP、optimal transport、$L^p$ Sobolev、log-Sobolev 等工作继续逼近这一结构，但没有关闭 $p=1$、高余维的原始尖锐常数问题。

此前为什么认为它非常值得 AI：

1. **原命题非常精确**，不是模糊的“分类所有对象”；
2. **成功标准清楚**：同一个 Euclidean sharp constant；
3. **已有强理论脚手架**：ABP、optimal transport、Michael–Simon、normal bundle Jacobian、varifold/rigidity；
4. 已知 codim 1/2 成功、codim ≥3 失败点明确，可以定位“现有证明到底在哪一步损失常数”；
5. 可以允许非常多的创造性路线，但最后都能通过严格不等式逐步验证；
6. 若完整解决高余维情形，是一个真正有分量的几何分析结果。

需要特别强调：此前把 Problem 109 作为“最适合 AI 的强候选”是**研究战略判断**，不是数学定理，也不是已经证明它比所有其他 119 个问题更容易。新会话必须重新比较最新进展。

### B. Problem 70 —— Pólya 特征值猜想

原问题（Dirichlet planar version）：对平面有界区域，逐项证明 Laplace eigenvalue 满足 Weyl 常数对应的 Pólya lower bound。

此前状态整理：**一般情形仍开放。** 已知 tiling domains，近年来 disk、sectors、balls、annuli 等特殊情形有重要突破；Li–Yau 给出 sharp averaged inequalities，但不能推出逐项 Pólya inequality。

为什么适合 AI：

- analytic + combinatorial + rigorous-computation 反馈非常强；
- 已有 Bessel zeros、lattice counting、Weyl remainder、finite certified computation 等可操作结构；
- 可以快速产生反例搜索、特殊域验证、常数改进和 rigorous finite checks；
- 比许多纯几何分类问题更容易建立“实验 → 猜想 → 精确证明”的 Agent loop。

此前倾向：**如果强调 AI 的高反馈、高迭代效率，Problem 70 是非常强的候选。**

### C. Problem 108 —— area-minimizing hypersurface 的 generic regularity

原问题：通过对 ambient metric 做扰动，消除 area-minimizing hypersurface 的奇点，同时保留其 homology class。

截至此前资料整理：

- ambient dimension ≤ 11 的相关 homological minimizing hypersurface 版本已经取得完整 generic-smoothing 结果；
- dimension ≥ 12 仍只能得到改进后的 singular-set dimension bound，不能全部消除奇点；
- PL structure 问题是另外一个仍开放的问题。

为什么关注：这是近年进展极快的 frontier，Chodosh–Mantoulidis–Schulze–Wang 等工作把边界推进到 11 维；剩余问题高度集中在高维 singularity/tangent cone/deformation mechanism。

此前判断：价值很高，但技术门槛极高，且对最新文献状态极其敏感，进入研究前必须重新做 priority/status audit。

### D. Problem 111 —— 负曲率流形之间调和映射的单叶性

原问题：两个 compact negatively curved manifolds 之间的 diffeomorphism，其同伦类中的 harmonic representative 是否一定是 univalent。

截至此前资料整理：

- dimension 2：成立（Schoen–Yau / Sampson）；
- dimension ≥ 6：已有 counterexamples，原始“所有维数都成立”已经是 false；
- **dimensions 3, 4, 5 仍是自然的未决窗口。**

此前判断：这个问题的剩余维数窗口很清楚，正反两种答案都可以形成完整结论，适合 AI 进行定向攻关；但它的历史原题已经在高维被否定，所以宣传时必须说“解决剩余维数 3–5”，不能说“证明 Yau 111 原猜想”。

---

## 4. 此前形成的战略排序（需要新会话重新验证）

此前讨论大致形成过如下判断：

### 理论旗舰优先

**Problem 109**：高余维极小子流形 sharp Euclidean isoperimetric inequality。

原因：命题锐利、历史深、已有 codim≤2 突破、剩余障碍明确，若解决高余维就是直接关闭 Yau 原题的剩余核心。

### AI 高反馈/计算辅助优先

**Problem 70**：Pólya conjecture。

原因：强可计算反馈、谱数值/严格计算/解析不等式/格点计数可以高频互动，适合 Agent 快速学习和淘汰路线。

### 其他强候选

- **Problem 111（3–5维）**：剩余窗口有限且结论二元化；
- **Problem 108（≥12维 generic regularity）**：前沿非常新、价值大，但技术深且最新文献依赖强；
- Problems **19/20/22/23/25/26/28**：都是真问题，但很多属于“大尺度 prescription/classification”，目前相对不如 109/70 适合作为第一 AI 旗舰攻关。

这只是“AI 研究适配性”的排序，不是“数学价值”的绝对排序。

---

## 5. 用户对后续研究的硬性标准

新会话必须保留以下标准：

1. **首先核查开放状态。** 不能研究已经解决、已经证伪或被新论文改变了含义的旧问题。
2. **目标是原始问题的严格解决。** 受限 family、特殊参数、数值实验、solver timeout、局部排除、近似证明不能冒充原题解决。
3. 任何“AI 已解决”必须有完整证明/反例，以及明确的适用维数、底层假设、正则性和边界条件。
4. 允许产生强中间结果，但必须准确标记为 partial result，并说明距原题还有什么逻辑缺口。
5. 优先寻找能够产生**新的可靠数学知识**的路线，而不是为了增加 Step 数、文件数、候选数而机械推进。
6. 若路线连续只产生局部改进、更多 UNKNOWN 或越来越大的搜索而不改变核心未知，应重新审视 representation、lemma、dual formulation 或整个路线。
7. 研究最终应形成可供专家审阅的完整论文级材料；此前曾讨论以不少于约 10 页英文/数学论文稿、较完整中文研究报告以及多轮 Agent Steps 作为工程性交付要求，但这些格式要求不能替代数学完成度。

---

## 6. 推荐新会话首先做什么

新会话不要直接从某个旧证明路线开始。第一轮应完成：

1. **截至当前日期的全网状态复核**：Problem 109、70、108、111，尤其核查 2026 年最新论文是否改变 open status；
2. 明确每个问题当前真正剩余的“最小未解决核心”；
3. 比较：
   - 完整解决的科学价值；
   - 当前 AI/计算系统能否产生快速、可靠 feedback；
   - 是否已有可复用的 proof machinery；
   - 是否存在清晰的 two-sided success condition（构造/反例，证明/证伪）；
   - 是否容易因特殊情形成功而误报解决；
4. 在重新核查后决定是否仍把 **Problem 109** 作为首选理论旗舰，或改选 Problem 70 / 111 / 108；
5. 选定后再写正式“最高研究目标 + 研究方法和心智 + 验证标准”的研究 prompt。

---

## 7. 对 Problem 109 的最简交接语

如果新会话只想立即恢复我们此前最关注的方向，可以直接使用下面这一段作为上下文：

> 我们此前系统讨论过丘成桐 1982 Problem Section，并比较了 Problems 18–32 以及整个问题集中若干仍开放问题。当前最值得重新核查并考虑作为理论旗舰的是 **Problem 109：高余维紧致极小子流形的尖锐欧氏等周不等式**。已知 Brendle 已解决 codimension ≤2，并证明 equality rigidity；codimension ≥3 的 sharp Euclidean constant 版本截至此前资料仍开放。请首先重新核查截至今天的公开状态和最新 2026 文献，然后独立判断它是否仍是整个 Yau 问题集中最适合当前 AI 系统严格解决的候选之一。目标必须是原始高余维 sharp statement 的严格证明或反例，不能把特殊族、非尖锐常数或局部结果冒充完整解决。

---

## 8. 一句话总览

此前讨论不是简单得出“Yau Problem 109 一定最容易”，而是形成了更严格的判断：

> **如果要从 Yau 问题集中选择一个兼具历史地位、明确剩余核心、严格成功标准和现代 AI 可攻击结构的理论问题，Problem 109 是此前最强候选之一；若优先考虑高频计算反馈，则 Problem 70 更有优势。Problem 108 和 Problem 111 是另外两个值得重新核查的强候选。**


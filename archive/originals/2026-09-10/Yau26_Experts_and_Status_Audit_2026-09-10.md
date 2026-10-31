# Yau Problem 26：专家、文献与开放状态核查

核查日期：2026-09-10。对象：1982 年《Problem Section》第26题。

本报告依据公开论文、论文版本记录、期刊页面和作者主页建立研究联系。名单不是全球人员普查，也不表示所有被列专家都公开宣布正在专攻第26题。本次没有与任何作者通信，没有获得未发表工作的确认，也没有逐行重审所有论文的证明。

**结论：本次公开检索没有找到完整覆盖第26题原始量词的证明或反例。可以继续把它作为开放研究目标，但不能把检索未发现升级为“已确定全球无人解决”。** 下列文献提供了具体的已知结果与仍然缺少的条件；开放状态结论是本次检索判断，不是其中某篇论文证明的定理。

## 1. 我们核查的命题

根据已提供的问题集材料，原题要求：对每个维数 n，存在常数 c_n<C_n，使光滑紧致无边界流形上的度量 g 若满足

\[
c_n g\leq\operatorname{Ric}_g\leq C_n g,
\]

则同一个光滑流形 M 上存在某个 Einstein 度量 h。

结论没有要求 h=g、h 接近 g、h 保留 g 的对称性或复结构。原文常数符号需保留；正、负归一化分支应分别记录。证明所有维数的一个可用分支可以给出原题所需常数；仅否定某个预先选定的正区间，不能自动否定原题对区间的存在量词。

核查每篇候选解答时，需要检查：维数范围、紧致性、光滑性、曲率类型、误差范数、常数依赖，以及结论是否只是局部变形、特定族存在或某种 Einstein 度量不存在。

## 2. 与“almost Einstein 推出 Einstein 存在”最直接的研究者

| 研究者 | 可核实的工作 | 对我们的具体用途与边界 |
|---|---|---|
| Michael T. Anderson | 1989 年 *Ricci curvature bounds and Einstein metrics on compact manifolds*；其本人[出版物目录](https://www.math.stonybrook.edu/~anderson/publ.pdf)确认书目信息 | 经典 Ricci 控制、紧性与 Einstein 存在路线。此次 AMS 原文访问失败，不能把此前整理的 Corollary B(4) 全部假设标为本轮已逐项复核；应优先取得原文 |
| Maung Min-Oo | 1990 年 *Almost Einstein manifolds of negative Ricci curvature*，[原论文扫描副本](https://scispace.com/pdf/almost-einstein-manifolds-of-negative-ricci-curvature-59se5bvv0c.pdf) | 直接研究负分支的近似解到严格解；使用 Ricci 流。定理另有直径与截面曲率的组合控制，阈值依赖相应参数，不是仅依赖维数 |
| Frieder Jäckel | *Effective stability of negatively curved Einstein metrics in dimensions at least four*，[原文](https://arxiv.org/html/2502.16692v2)、[2026 年期刊页](https://link.springer.com/article/10.1007/s12220-026-02563-1) | 当前本次检索中最贴近负分支的一条新结果；第1.1定理另要求负截面曲率、薄部双曲结构、Ricci 导数控制及 C⁰/L² 误差条件 |
| Ursula Hamenstädt 与 Jäckel | 2022 年[稳定性与有效双曲化](https://arxiv.org/abs/2206.10438)；2024 年提交、2025 年修订的[Gromov–Thurston 流形构造](https://arxiv.org/abs/2411.12956) | 前者延伸田刚早期工作；后者构造有负曲率 Einstein 度量但无局部对称度量的闭流形。提醒我们：排除双曲或局部对称度量，不等于排除一切 Einstein 度量 |
| Joel Fine 与 Bruno Premoselli | *Examples of compact Einstein four-manifolds with negative curvature*，[论文](https://arxiv.org/abs/1802.00608)，作者目录列为 JAMS 2020 | 在特定分支覆盖族上先构造近似度量，再用参数相关逆函数定理得到严格解。可复用其拼接及估计技术，不能把特定构造推广成原题 |
| Richard H. Bamler | *Construction of Einstein metrics by generalized Dehn filling*，[论文](https://arxiv.org/abs/0911.4730) | 通过广义 Dehn 填充构造 Einstein 度量；适合检查手术、拼接、退化参数中的分析问题，不是纯 Ricci 夹逼的普遍定理 |

这条研究线有真实的人际与机构连接：[Jäckel 主页](https://www.friederjaeckel.com/)记载，他于2021—2025年在波恩师从 Hamenstädt，目前在布鲁塞尔自由大学 Fine 与 Premoselli 的研究组工作。[Hamenstädt 的波恩主页](https://www.math.uni-bonn.de/people/ursula/)和[Fine 的论文目录](https://joel.fine.web.ulb.be/papers.html)提供持续追踪入口。这里的“目前”以本次访问页面为依据。

## 3. 对核心障碍最相关的专家

这些专家有相关成果；下表的“用途”是研究匹配判断，不是本人承诺能解决第26题。

| 研究者 | 论文依据 | 适合核实的关键问题 |
|---|---|---|
| 江文帅 Wenshuai Jiang、Aaron Naber | [Annals 2021：有界 Ricci 下的 L² 全曲率估计](https://annals.math.princeton.edu/2021/193-1/p02) | 非塌缩条件下的曲率能量与奇异集控制。仅 Ricci 夹逼能获得哪些控制？哪些附加假设不能省略？ |
| 田刚 Gang Tian、王兵 Bing Wang | [On the structure of almost Einstein manifolds](https://arxiv.org/abs/1202.2912) | 近似 Einstein 序列的极限结构；论文使用非塌缩与流相关条件。极限空间结论不能直接替代原光滑流形上存在 h |
| Tristan Ozuch | [Integrability of Einstein deformations and desingularizations](https://arxiv.org/abs/2105.13193)；[Higher order obstructions](https://arxiv.org/abs/2012.13316) | 无穷小变形可积性、奇点消除及高阶阻碍。某个 orbifold 不能成为光滑 Einstein 极限，尚不等于某个光滑流形完全不存在 Einstein 度量 |
| Claude LeBrun | [Einstein metrics and Mostow rigidity](https://www.math.stonybrook.edu/~claude/lmo.pdf)；[Einstein Constants and Smooth Topology](https://arxiv.org/abs/2502.10560) | 四维拓扑、Seiberg–Witten、曲率不等式及 Einstein 常数符号。反例路线必须核查阻碍是否排除了任意 Einstein 度量 |
| Olivier Biquard、Ozuch | [Instability of conformally Kähler, Einstein metrics](https://arxiv.org/abs/2310.10109) | Einstein 稳定性及变形分析。该论文版本记录明确说明曾补足一个缺失论证，是必须追踪修订而非只下载首版的具体例子 |
| Klaus Kröncke | [Stability of Einstein metrics under Ricci flow](https://arxiv.org/abs/1312.2224) | 线性与非线性稳定性、谱条件、Ricci 流。研究的是已知 Einstein 度量附近的行为，不是所有 Ricci 夹逼输入的全局存在 |
| Christoph Böhm、Burkhard Wilking | [正曲率算子下的 Ricci 流收敛](https://arxiv.org/abs/math/0606187) | 正分支的重要方法来源；必须区分曲率算子为正与 Ricci 为正 |
| Simon Brendle、Richard Schoen | [逐点四分之一截面曲率夹逼球面定理](https://arxiv.org/abs/0705.0766) | 高维曲率夹逼与 Ricci 流的重要参照；假设控制截面曲率，不能直接作为第26题解答 |
| Timothy Buttsworth、Liam Hodgkinson | [S¹² 上新 Einstein 度量的计算机辅助严格证明](https://arxiv.org/abs/2412.01184) | 学习数值候选、严格误差界、近似到精确的验证流程。其成果属于具体对称族，不能自动称为 AI 解决第26题 |

补充阅读入口：[Paul Schwahn、Uwe Semmelmann 的 Einstein 模空间与稳定性综述](https://arxiv.org/html/2507.18463v3)。作者明确将重点放在局部稳定性与模空间，而不是一般流形的 Einstein 存在问题；它可用作查文献的地图，不能作为第26题开放状态的单独证明。

丘成桐是原题提出者，Hamilton 的三维正 Ricci 工作是历史起点。历史贡献者名单与“目前持续专攻第26题”的名单必须分开。也没有必要把所有研究 Einstein 方程的物理学家列进来：这里研究的是闭流形上的黎曼 Einstein 度量，不能用领域同名代替具体论文关联。

## 4. 新文献是否已经改变开放状态？

### 4.1 Jäckel：确实推进了存在理论，仍有额外假设

arXiv 记录：2025-02-23 首稿，2025-12-29 第二版移除原先的维数上限。期刊页面记录正式发表于2026-08-04。其价值在于去掉了对直径、体积上界和注入半径下界的阈值依赖，但第1.1定理仍有前述其他条件。因此“移除了若干几何限制”不能读成“所有几何限制都移除”。[版本记录](https://arxiv.org/abs/2502.16692)

### 4.2 Hamenstädt–Jäckel：重要构造，不能当成反例

其 Gromov–Thurston 工作的作者研究页面列为 JEMS 待刊。论文还明确提出“是否每个 Gromov–Thurston 流形都承载 Einstein 度量”等问题；它构造的是一批存在例，不能认为该族全已解决，也不能把“不局部对称”当作“不 Einstein”。[作者出版记录](https://www.friederjaeckel.com/research)、[原文问题](https://arxiv.org/html/2411.12956v2)

### 4.3 LeBrun–Ozuch：2026 年去奇点新结果

*Desingularizations of Conformally Kähler, Einstein Orbifolds* 于2026-01-27提交、02-05修订。本次检查了第二版的引言和定理A/B。结论涉及正 Einstein 常数、Hermitian orbifold 极限及反自对偶 ALE 泡条件下的刚性。从一开始就假设已有 Einstein 度量序列，故没有解决从单纯 Ricci 夹逼得到其存在的问题。[原文](https://arxiv.org/html/2601.19215v2)

### 4.4 关于 AI

本次未找到可核验的 AI 完整解决第26题的公开论文。不能从“计算机辅助构造了某个 Einstein 度量”推出“解决了夹逼所强迫的普遍存在问题”。也不能从论文摘要中的 AI 贡献说明，推断其证明已获得独立审查。

## 5. 已发现但尚未完成全文核查的线索

这是本次调查的明确边界。访问失败表示未取得文本，不表示论文不存在或无效。

| 线索 | 本次取得的信息 | 仍需处理 |
|---|---|---|
| Anderson 1989 JAMS 原文 | 作者书目确认；AMS全文访问失败 | 获取原文，逐项抄录 Corollary B(4) 的假设、范数及常数依赖 |
| 田刚 *A Pinching Theorem on Manifolds with Negative Curvature* | Jäckel 论文参考文献明确标为 unpublished manuscript；2022合作论文说明延伸了其工作 | 向作者或相关研究者核对版本、可引用结论及后续改进；不是假定有秘密完整解答 |
| LeBrun，*An Overview of Einstein 4-Manifolds*，[arXiv:2609.03033](https://arxiv.org/abs/2609.03033) | 搜索索引显示2026-09-02及题名；摘要页/HTML/PDF未成功读取 | 获取真实全文，核实书目及其中开放问题；本报告未把它作为已读综述 |
| Ozuch，[arXiv:2608.31008](https://arxiv.org/abs/2608.31008) | 索引摘要指向非紧 Ricci-flat 引力瞬子的稳定性；直接访问失败 | 核实原文；摘要层面不属于闭流形第26题的完整存在定理 |
| Kim–Park，[arXiv:2609.03739](https://arxiv.org/abs/2609.03739) | 索引显示梯度估计、体积夹逼与刚性；直接访问失败 | 核实原文，不能仅因出现 Ricci、pinching、Einstein 就判定解决26题 |
| Gao–Liu–Zhang，[arXiv:2609.07252](https://arxiv.org/abs/2609.07252) | 索引摘要显示2026-09-07，讨论曲率符号刚性，并自述 AI 参与；直接访问失败 | 核实作者、全文及贡献声明。按索引描述，曲率符号刚性与 Einstein 度量存在是不同结论；不能称为已核实的26题突破 |

本轮也没有独立完成 MathSciNet/zbMATH 全部引用网络的系统导出。因此这份报告是有明确证据和缺项的研究地图，不是宣称“全网全部论文已经看完”。

## 6. 如何减少信息闭塞

建议把以下机制加入现有研究流程，而不是仅依赖一个问题编号的关键词：

1. **追踪命题与同义词。** 同时使用 `Yau 1982 problem 26`、`almost Einstein manifolds`、`Ricci pinching Einstein existence`、`stability of Einstein metrics`、`desingularization Einstein metrics`、`obstructions Einstein metrics`。注意共形几何中的 almost Einstein、向量丛上的 Hermite–Einstein 可以是不同含义。
2. **追踪作者和引用。** 以 Anderson、Min-Oo、Tian–Wang、Hamenstädt–Jäckel、Fine–Premoselli、Ozuch、LeBrun、Kröncke 为种子；正分支另跟进 Jiang–Naber、Böhm–Wilking、Brendle–Schoen 路线。看参考文献，也看后续引用和作者主页。
3. **保存版本与命题卡。** 每项记录作者、题名、DOI/arXiv、版本日期、定理号、全部假设、结论、常数依赖、是否正式发表、勘误以及已检查范围。新版本出现后检查修改点。
4. **在重大投入与投稿前复核状态。** 具体命题对照比“标题中说 solved”可靠；查询失败必须保留为缺项。
5. **用针对性问题向专家核实。** 专家回复可以补上未发表文献与错误路线，但应记录其所指文献或论证，不能把个人印象当作数学证明。

以上是建议的工作流程；本次没有建立自动定期检索，也没有向任何人发送邮件。

## 7. 建议首先核实的对象与问题

| 对象 | 建议核实的问题 |
|---|---|
| 江文帅；必要时扩展至 Naber、Tian、Wang | 对正分支，仅靠 Ricci 夹逼的现有最强结论是什么？是否有已知反例族、未发表结果，或不能省略的退化机制？ |
| Jäckel、Hamenstädt | 最新负分支定理之外是否有更一般结果？田刚手稿的准确版本是什么？是否存在已知的维数唯一阈值或反例？ |
| Anderson | 1989 结果及后续工作的精确边界；原题的现代解释、已知否定结果及容易遗漏的老文献 |
| LeBrun、Ozuch | 是否存在同时兼容任意紧 Ricci 夹逼、又能排除所有 Einstein 度量的拓扑/分析障碍？去奇点阻碍能否提供这种全球非存在结论？ |
| Kröncke；正曲率路线中的 Böhm、Wilking、Brendle、Schoen | 仅 Ricci 小误差与稳定性假设之间缺少什么？哪些看似可用的流收敛论证实际上加强了原题？ |

**特别建议：先让江老师判断精确研究命题，再用 Jäckel/Hamenstädt 的存在理论与 LeBrun/Ozuch 的阻碍理论做交叉核对。** 这是基于论文的匹配建议，尚未得到任何人的参与承诺。

可供专家核对的核心表述为：我们研究闭光滑 n 维流形上的条件 `(1−ε_n)g ≤ Ric_g ≤ (1+ε_n)g` 是否以仅依赖 n 的阈值，强迫同一光滑流形存在某个不受对称性或邻近性限制的 Einstein 度量；同时单独记录原题未指定常数符号的量词。请提供任何已发表、预印本、未发表的完整结果、反例或相关障碍，并指出精确假设。

获得原文和专家反馈之后，再更新开放状态。当前最重要的未完成事项是这些具体核查，不是重复扩大无差别关键词搜索或把更多人名堆进名单。

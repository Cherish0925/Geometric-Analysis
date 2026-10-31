# Geometric Analysis

四维 Einstein 几何、曲率变分、定量刚性与几何退化的研究档案。

核心问题是：给定光滑流形及其拓扑、规范或几何结构，Einstein 方程能被满足或逼近到什么程度；相应曲率泛函的下确界、达到性和退化结构由什么决定？主要对象包括


$$
P_*(M)=\inf_g\int_M|\operatorname{Ric}^{\circ}_g|^2\,dV_g,
\qquad
\alpha(M)=\inf_g\inf_{\lambda\ne0}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|^2\,dV_g}
{\lambda^2\operatorname{Vol}_g(M)}.
$$


规范场、相容闭二形式与曲率微分恒等式提供全局约束；真实度量构造检验最优性；精确 Einstein 与几乎 Kähler 研究进一步分析可实现性和刚性。各分支共享几何问题与分析方法，保留各自实际输入和证明依赖。

## 阅读路径

| 目的 | 入口 |
|---|---|
| 掌握各分支的证明联系 | [研究图谱](docs/RESEARCH_MAP.md) |
| 原积分 gap、N1、I40/I41、O10、双取向与 Kodaira | [间隙与端点](docs/GAPS_AND_ENDPOINTS.md) |
| 严格低成本构造、全部度量极值、Q1–Q3 与取得性 | [曲率变分](docs/CURVATURE_VARIATION.md) |
| 完备非紧实例、Fino 问题、零点及闭负 Goldberg | [几乎 Kähler–Einstein 几何](docs/GOLDBERG.md) |
| 版本演化、改正与跨会话接续 | [研究沿革](docs/RESEARCH_HISTORY.md) |
| 原件、文件哈希与包内材料 | [来源索引](catalog/README.md) · [收录范围](docs/COVERAGE.md) · [来源元数据](catalog/sources.json) · [解包目录](catalog/packages.json) · [包内文件索引](catalog/archive_members.json) |

专题导航直接链接原始证明及程序。连续阅读可从 [00_All_Recent_Research.tex](archive/originals/2026-10-07/00_All_Recent_Research.tex) 进入早期汇总，再接 [01_Research_Synthesis.tex](archive/originals/2026-10-08/01_Research_Synthesis.tex)、[03_Subsequent_Mathematical_Developments(1).tex](archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) 及 [Goldberg_Two_Conversations_Merged_20261015.tex](research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)；具体成果的最新状态以专题导航中的后续修订为准。

## 主要结果与未完成问题

| 研究部分 | 原稿中已写出的结果 | 仍需解决 |
|---|---|---|
| 统一积分障碍 | 单解参数分析回接 N1 无迹 Ricci gap；有界类平方短缺；I40/I41 线性强制 | 更自然的真实输入、最佳依赖及新的实际适用对象 |
| 弱积分端点 | 任意固定有限 Euler 密度下的 O10；N1 与 FD 的地理分区覆盖若干密度可无界的手术族 | 原全部输入下不受地理或密度限制的统一常数，或实际闭反例 |
| 双取向应用 | 以固定密度 **FD2** 为前置，得到曲面丛统一间隙、Kodaira 斜率统一远离 3；后续允许一侧凸包及配对短缺 | 最佳宽度；更一般真实双取向供给 |
| 构造与最优值 | 完整单元的严格节省、严格次四恢复、一般负 KE 背景推广、共形 Kähler 类分离 | 全部竞争度量的匹配下界和最优值 |
| 全局极小元 | 明确候选、真实下降方向、秩刚性、退化例以及部分 AE/ALE 核心排除 | 非 Bach-flat 光滑全局极小元的取得实例 |
| 几乎 Kähler–Einstein | 完备非紧严格例子及其 Fino 问句对应；扭率零点结构、行列式和 Green 势刚性 | 闭四维负 Goldberg 的一般证明或闭反例 |

FD2 是 Kodaira 推论的解析前置，不能从应用反向认证。严格低成本构造已经改变其适用族中“标准系数 4 最优”的候选答案。完备非紧例子与闭 Goldberg 是不同结论。以上状态整理自所收原稿；不以归档或程序核算代替其完整分析证明。

## 档案结构

- `archive/originals/`：原始文件和压缩包，按来源时间保存；同名版本由目录与来源记录区分。
- `research/packages/`：压缩包展开的数学正文、笔记、程序、计算证书和文献材料。
- `docs/`：按数学对象组织的阅读导航、证明联系和版本沿革。
- `catalog/`：来源身份、哈希、解包对应与取得情况。
- `tools/`：归档与检索辅助程序。

原稿中的旧结论、更正和失败路线一并保存。导航指出已被更新的状态；原始文件不因后续整理而覆盖。会话沿革根据可取得的文件和记录重建，不等同于全部历史会话的逐字导出。

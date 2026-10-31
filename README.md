# Geometric Analysis

四维 Einstein 几何：积分间隙、曲率变分、几何退化与几乎 Kähler 刚性。

本研究讨论光滑四维流形上 Einstein 度量的存在与逼近，以及拓扑、规范结构和相容闭二形式对曲率极值与刚性的限制。

设 $M$ 为闭、定向、连通的光滑四维流形，$\mathscr G(M)$ 为其全部光滑 Riemannian 度量。记
$$
P(g)=\int_M|\operatorname{Ric}^{\circ}_g|_g^2\,dV_g,
\qquad \operatorname{Ric}^{\circ}_g=\operatorname{Ric}_g-\frac{s_g}{4}g,
$$
$$
\mathcal E(g)=\inf_{\lambda\in\mathbb R\setminus\{0\}}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|_g^2\,dV_g}
{\lambda^2\operatorname{Vol}_g(M)},\qquad
P_*(M)=\inf_{g\in\mathscr G(M)}P(g),\quad
\alpha(M)=\inf_{g\in\mathscr G(M)}\mathcal E(g).
$$
$P(g)=0$ 等价于 $g$ 为 Einstein 度量。$\mathcal E$ 采用非零 Einstein 常数归一化；Ricci-flat 度量满足 $P=0$、$\mathcal E=4$。

主要问题是确定这些泛函的正下界、匹配上界、下确界的取得性及近极小序列的退化结构。分析部分利用规范场方程与曲率微分恒等式之间的相容性；构造部分研究轨形解消、拓扑手术及背景曲率的相互作用；几乎 Kähler 分支研究 Einstein 条件下相容辛结构的可积性。

## 研究内容

| 主题 | 原稿中的主要结论 | 进一步问题 |
|---|---|---|
| 积分间隙 | 单解参数估计、N1 无迹 Ricci 间隙、类平方短缺估计、I40/I41 线性强制及规范理论应用 | 弱化解存在性条件、确定最佳常数依赖、扩大适用流形类 |
| 参数端点 | 对每个固定有限 $B$，在 $\chi/A\le B$ 下得到 $c(B)>0$；由拓扑数关系进一步得到所列手术族的统一常数 | 一般无密度条件下的统一估计或闭流形反例 |
| 双取向应用 | 固定密度端点 FD2 与交叉配对给出曲面丛间隙及 Kodaira 斜率分离；推广至一侧凸包与配对短缺 | 最佳分离常数及更一般的双取向规范结构 |
| 曲率极值 | 严格低于标准手术能量的构造、相应族的严格次四上界、一般负 Kähler–Einstein 背景推广 | 全部光滑度量上的匹配下界与精确极值 |
| 极小值取得性 | 共形 Kähler 类的能量分离、候选度量的下降方向与临界点排除、谐和秩刚性及部分 AE/ALE 退化分析 | 非 Bach-flat 光滑全局极小元的存在 |
| 点态逼近与精确实现 | 固定轨形解消、固定剪切流形上的逼近序列、周期与慢模态分析，以及所列有界几何条件下的 Einstein 实现 | 固定对象的全部 Einstein 存在性及一般退化下的实现 |
| 几乎 Kähler–Einstein 几何 | 完备非紧严格例子、扭率零点结构、行列式符号与 Green 势刚性条件 | 闭四维负 Goldberg 猜想 |

各结论的假设、常数依赖及证明来源列于下述专题。Kodaira 分离依赖 FD2；严格次四构造适用于相应恢复族；非紧存在性与闭流形刚性分别处理。

## 阅读顺序

1. [研究结构与定理关系](docs/RESEARCH_MAP.md)：问题之间的联系、定理依赖与未完成命题。
2. [方法与文献](docs/METHODS_AND_LITERATURE.md)：相容性估计、变分、构造、极限方法及其文献基础。
3. [间隙与端点](docs/GAPS_AND_ENDPOINTS.md)：N1、I40/I41、O10、双取向与 Kodaira 应用。
4. [点态构造与精确实现](docs/CONSTRUCTIONS_AND_REALIZATION.md)：解消、固定流形、周期、慢模态及存在性。
5. [曲率变分](docs/CURVATURE_VARIATION.md)：O11、严格上界、Q1–Q3 与极小值取得性。
6. [几乎 Kähler–Einstein 几何](docs/GOLDBERG.md)：Fino 存在性问题、零点结构与闭负 Goldberg。
7. [研究沿革](docs/RESEARCH_HISTORY.md)：主要推导的先后关系及修正。

连续数学正文见 [10月7日研究总稿](archive/originals/2026-10-07/00_All_Recent_Research.tex)、[四题综述](archive/originals/2026-10-08/01_Research_Synthesis.tex)、[后续数学进展](archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) 及 [Goldberg 合并稿](research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)。

## 原稿与程序

`archive/originals/` 保存原始文稿和资料包；`research/packages/` 保存展开后的证明、笔记、程序、计算数据与文献。各版本及其修正同时保留。全部文件见[来源索引](catalog/README.md)，材料范围见[收录说明](docs/COVERAGE.md)。

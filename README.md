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
| 曲率极值 | 背景曲率作用产生严格较低的手术上界；Weyl–Yamabe 精确归约；指定成对 $A_1$ 轨形上的精确值与非取得性 | 一般吹起与平衡族的全度量最优值 |
| 极小值取得性 | 共形 Kähler 类的能量分离、候选度量的下降方向与临界点排除、谐和秩刚性及部分 AE/ALE 退化分析 | 非 Bach-flat 光滑全局极小元的存在 |
| 点态逼近与精确实现 | 固定轨形与剪切流形上的逼近；循环覆盖完整核修复、增长—强制条件下的无直径修复；闭路变形及完整填充条件下的精确实现 | 固定对象的全部 Einstein 存在性及一般退化下的实现 |
| 几何退化与实际场 | ALE 混合曲率转移、根格限制及补域电荷；Wahl 收缩中的实际场、局部字符和形式延拓 | 将局部拓扑与场信息转为统一全局障碍 |
| 几乎 Kähler–Einstein 几何 | 完备非紧严格例子、Green 势刚性、调和秩条件、模空间作用量及非塌缩退化中的能量传递 | 闭四维负 Goldberg 猜想 |

各专题以定义、命题、推导与构造组织，注明实际供给、取向、归一化和常数依赖。Kodaira 斜率分离由 FD2 与双取向配对推出；Fino 的非不变存在性问句由完备非紧实例回答。一般吹起极值、光滑取得性和闭负 Goldberg 保留各自尚未解决的部分。

## 阅读顺序

1. [研究结构与定理关系](docs/RESEARCH_MAP.md)：问题之间的联系、定理依赖与未完成命题。
2. [方法与文献](docs/METHODS_AND_LITERATURE.md)：相容性估计、变分、构造、极限方法及其文献基础。
3. [间隙与端点](docs/GAPS_AND_ENDPOINTS.md)：N1、I40/I41、O10、双取向与 Kodaira 应用。
4. [点态构造与精确实现](docs/CONSTRUCTIONS_AND_REALIZATION.md)：解消、固定流形、周期、慢模态及存在性。
5. [曲率变分](docs/CURVATURE_VARIATION.md)：O11、严格上界、Q1–Q3 与极小值取得性。
6. [几乎 Kähler–Einstein 几何](docs/GOLDBERG.md)：Fino 存在性问题、零点结构与闭负 Goldberg。
7. [研究沿革](docs/RESEARCH_HISTORY.md)：从曲率预算到微分强制、从标准核心费用到背景相互作用，以及研究方向改变的数学原因。

早期连续文稿见 [10月7日研究总稿](archive/originals/2026-10-07/00_All_Recent_Research.tex)、[四题综述](archive/originals/2026-10-08/01_Research_Synthesis.tex)、[后续数学进展](archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) 及 [Goldberg 合并稿](research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)。

## 原稿与程序

`archive/originals/` 保存原始文稿和资料包；`research/packages/` 保存展开后的证明、笔记、程序、计算数据与文献。各版本及其修正同时保留。全部文件见[来源索引](catalog/README.md)，材料范围见[收录说明](docs/COVERAGE.md)。

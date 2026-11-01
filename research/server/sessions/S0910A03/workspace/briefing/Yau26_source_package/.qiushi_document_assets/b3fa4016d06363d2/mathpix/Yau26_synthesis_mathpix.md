---
source_file: Yau26_synthesis.pdf
converter: mathpix
format: mmd
---

微分几何研究工作稿

\title{
Ricci 夹逼
}

\section*{与 Einstein 度量}

Yau 26 相关累计研究的审计与重构

本稿保留累计记录中具有独立数学内容的结论、构造和方法，将重复推导合并，并把尚未闭合的全局推论恢复为明确的条件接口。正文按问题结构组织，包含可检查的证明、常数与尺度依赖，以及相应文献来源。

本稿不提供一般问题的完整证明或反例；会话内推导不附带首创性或同行评审认证。它的用途是把真正可用的数学积累与仍需证明的环节放在同一份可审查文本中。

\section*{阅读说明}

这份文本的重点是研究中哪些数学可以继续使用。它不是历轮讨论的转录，也不把反复出现的计划、乐观判断和＂接近完成＂的措辞计作成果。对于被后续计算修正的早期断言，正文采用最后能够支持的形式；有价值但未充分闭合的想法，则保留精确假设和缺口。

文中＂命题＂＂引理＂表示在所列假设下提供了证明或明确经典来源，不表示已得到外部审稿认可。＂条件接口＂表示结论依赖另列的输入，本稿没有将这些输入全部解决。对来源本身为预印本的结果，按所查版本引用。编译成功、符号计算和多次内部复核均不能代替数学证明。

\section*{问题的工作版本}

累计记录使用的归一化问题是：对每个固定维数 $n$ 和符号 $\sigma \in\{+1,-1\}$ ，是否存在只依赖维数的 $\varepsilon_{n, \sigma}>0$ ，使每个闭光滑 $n$ 维流形 $M$ 只要承载满足
$$\left\|\operatorname{Ric}_{g}-\sigma g\right\|_{\mathrm{op}, \infty ; g}<\varepsilon_{n, \sigma}$$
的度量，就承载某个光滑 Einstein 度量？输出度量不必接近 $g$ ，不必属于同一共形类，也不必适应输入的复结构、纤维化或对称性。

出处边界。本稿沿用＂Yau 26＂作为既有研究的名称。现有归档未提供已经核准的原始题页全文，因此这里的工作版本不冒充原题逐字引文，原题对两个符号与夹逼常数的最终逻辑连接仍须回到题页核对。本文给出的数学结论均自行列出量词，不依赖这项命名核准。

令 $P_{n,+}, P_{n,-}$ 表示上述两个分支。若原题要求两者都成立，反驳任一分支便否定这一合取；若原题只要求至少一者成立，则须否定相应析取。不能不看原文便断言＂一个符号反例一定足够＂或＂一定不够＂。在固定维数上反例序列允许 $M_{j}$ 随 $j$ 变化；在同一个 $M$ 上构造全序列是更强目标。

\section*{积累的数学结构}

当前较实质的积累可以按＂构造侧＂和＂障碍侧＂理解。曲面丛与局部 ALE 消解提供近似 Einstein 度量及其误差尺度；规范理论、代数形变、纤维积分和 Weyl 方程提供不同层次的约束。没有一项现存论证把这些约束无条件施加到所有可能的输出度量。

\begin{tabular}[t]{|l|l|l|}
\hline 研究对象 & 保留的核心内容 & 结论边界 \\
\hline 四维一般输入 & 严格 Hitchin－Thorpe 端点、SW体积窗口、熵与颈部的定量障碍 & 是筛选和必要条件；只有指定复或辛类别的正分支得到存在性推论 \\
\hline 局部消解 & $A_{1} / \mathrm{ADE} /$ type T 模型、二次与四次匹配、标量修正、临界通量 & 局部误差可控不等于无障碍的全局 Einstein 修正 \\
\hline 高度四代数模型 & 典范覆盖、带权完全交、形变空间与局部平滑参数的限制 & 排除特定复代数平滑，不自动排除底层的全部实 Ein－ stein 度量 \\
\hline 规范理论饱和 & 普通 monopole 类、半 Weyl 能量、临界 Lorentz 工具、泡上 Stokes约束 & 端点全局体积间隙保留显式分类和评价接口 \\
\hline Dehn twist 曲面丛 & 固定总空间的最大范数近 Ein－ stein 构造、真实修正阶数、谱与体积账本 & 一般负 Einstein 不存在性尚未证明 \\
\hline Weyl 与调和压缩 & 负特征线平衡、四阶闭合缺陷、有限维核、带源首项 & 精确方程与近似方程必须分开；缺统一核控制 \\
\hline 下沉与调和映射 & 完整 Ricci 分块、面积方程、带非 basic 项的修正、目标权重界与反例 & 受限结构的刚性不能扩成任意度量的刚性 \\
\hline 扩展图四流形 & 经典全局无 Einstein 结论、Weyl集中约束与附加条件下直径代价 & 尚未构造该类上的全局 Ricci 最大误差趋零序列 \\
\hline
\end{tabular}

正文的统一线索是相对尺度。一个残差趋零，只有在对应的逆算子、边界通量、障碍投影和非线性项的同一尺度下才有决定意义。累计研究中有价值的修正，常常来自把先前省略的混合 Ricci 分量、Cotton 源项、非 basic 平均项或谐和核重新写回方程。这里保留这些修正，是为了让后续工作从正确的方程出发。

\section*{符号与使用方式}

通常 Ric 为 $(0,2)$ 张量，$\|$ Ric $-\sigma g \|_{\mathrm{op}}$ 指相对 $g$ 的特征值最大误差。四维 $W^{ \pm}$默认视为 $\Lambda^{ \pm}$上的算子，范数为算子的 Hilbert－Schmidt 范数；无迹 Ricci $E$ 使用二阶张量范数。完整四阶曲率张量的范数会另行标出，避免因相差 4 的平方范数产生常数错误。

不同章节的 $s$ 可能表示标量曲率，也可能表示明确重新定义的形变尺度；局部定义优先。Laplace 符号也逐处标明：$\Delta_{d}=d \delta+\delta d$ 非负，而 $\Delta=\operatorname{div} \nabla$ 在函数最大点非正。所有 $O(\cdot)$ 估计均相对于该节固定的背景、支集、规范和导数阶数；若背景同时退化，不能默认为常数仍一致。

先读各章的结论范围，再按研究方向检查证明。源码包附编辑审计，记录原章节的合并、修正和条件降级。

\section*{目录}
阅读说明 ..... i
第一章 リ一化、拓扑筛选与定量障碍 ..... 1
1.1 必须固定的量词与范数 ..... 1
1.2 严格 Hitchin－Thorpe 端点及正分支的已覆盖类别 ..... 1
1．3 Seiberg－Witten 禁区的误差窗口 ..... 2
1.4 从规范理论缺陷到局部不可实现谱 ..... 3
1.5 熵障碍、直径与有限覆盖 ..... 5
第二章 可核查的局部构造与其真实边界 ..... 7
2.1 为什么普通缩小内核不够 ..... 7
2．2 Eguchi－Hanson 核的显式修正 ..... 7
2．3同Ricci、不同 Weyl 的对数拼接 ..... 8
2．4 ADE、周期与 type T 核：相同机制的准确推广 ..... 9
2.5 最短的 Wahl 填充证明与高阶增强的分离 ..... 11
2.6 常标量修正：权重端点与可用的局部替代 ..... 12
2.7 对数阶为何不能任意改进：无规范的通量 ..... 15
2.8 临界导数能量：三阶可小，四阶不自动小 ..... 17
2.9 标准光滑模型：几何构造与拓扑识别须分别证明 ..... 17
2.10 某条修正路线无解，与流形无解是不同结论 ..... 18
2.11 负分支候选：必须辨认光滑结构与边界 spin 数据 ..... 20
第三章 局部灵活性的限度与带边界连接障碍 ..... 21
3.1 固定宽度的负 Ricci 灵活性不能代替紧夹逼 ..... 21
3.2 去核、正分支障碍与高频误差 ..... 22
3.3 平坦及 Heisenberg 颈：可复核的最大误差下界 ..... 23
3.4 一般最小截面没有同样的局部间隙 ..... 24
3．5 Berger 小核：局部精确可行，指定延拓不可行 ..... 25
3.6 普通点短把手的覆盖体积障碍 ..... 27
3.7 任意内部几何也无法跨越的平均曲率阈值 ..... 28
3.8 变化拓扑熵候选：不存在性已知，近似输入尚缺 ..... 29
第四章 高度四随圆曲面：全局典范关系与复形变障碍 ..... 31
4.1 候选对象与数值等号分类 ..... 31
4.2 消解、自然轨形与典范覆盖栈 ..... 32
4.3 低次典范乘法控制全部 Artin 平滑参数 ..... 33
4.4 完整 QG 计算：三十八维与无穷小厚化 ..... 34
4.5 自然形变障碍空间：一维并非普遍成立 ..... 35
4．6 Wahl 商与 ADE 插值：障碍空间不等于实际障碍 ..... 37
4.7 一般高度的对照计算与高度四的特殊性 ..... 38
4.8 与实 Einstein 问题之间尚未建立的桥梁 ..... 39
第五章 规范理论饱和、临界分析与泡上的周期约束 ..... 40
5.1 固定对象、规范与两类不同的极限 ..... 40
5．2 Seiberg－Witten 缺陷与全部普通单极类 ..... 40
5.3 自对偶曲率的全局控制：为何允许另一半曲率集中 ..... 43
5.4 闭典范形式、Hodge 投影与精确体积账本 ..... 44
5.5 从非平行性提取非零全纯张量 ..... 46
5.6 可重复使用的临界分析工具 ..... 47
5.7 外部 Green－Jacobi 模式与真正能量的边界 ..... 50
5.8 双典范残值：明确可计算的固定背景响应 ..... 51
5.9 精确局部 KE 参考与三阶净通量的抵消 ..... 53
5.10 泡上的 Stokes 约束与全奇点评价 ..... 55
5.11 有界直径体积间隙：保留完整逻辑接口 ..... 56
5.12 本章留下的可执行数学接口 ..... 57
第六章 固定曲面丛上的全局逼近、修正与退化 ..... 58
6.1 不退化纤维的慢插值：一个完整的闭流形构造 ..... 58
6.2 双领圈平衡：全局二阶误差及精确首系数 ..... 61
6.3 一次真实的二阶校正：最大误差降至三阶 ..... 63
6.4 真正的全局测试张量与三阶下界 ..... 65
6.5 整个共形类的控制与一个真实的临界抵消 ..... 66
6.6 精确标量归一化与五阶体积首项 ..... 67
6.7 原始与修正背景的谱：不能借小距离转移符号 ..... 69
6.8 精确线性模型：良好的 $L^{2}$ 谱并不控制最大范数逆 ..... 70
6.9 曲面丛候选的拓扑、精确全局不变量与 Einstein 必要条件 ..... 72
第七章 Weyl 特征线、谐和压缩与不能删除的源项 ..... 88
7.1 最大特征值刚性恰在乘积模型处退化 ..... 88
7.2 负最小特征线的精确平衡 ..... 88
7.3 谐和核不能由近乎闭性删除 ..... 90
7.4 带源的一阶恒等式 ..... 91
7.5 在慢插值构造中，源项确实占据首阶 ..... 92
7.6 最大正截面处的必要谱分裂 ..... 93
第八章 适应曲面纤维化的 Einstein 方程与条件刚性 ..... 94
8.1 统一约定与全部相关曲率块 ..... 94
8.2 两种可完整证明的乘积刚性 ..... 96
8.3 纤维面积方程、等号刚性和残差界 ..... 97
8.4 非基本平均曲率：测度变分、四次矩与条件控制 ..... 99
8．5 Gram 各向同性与局部复结构 ..... 101
8.6 协方差的局部精确反例与闭延拓门槛 ..... 102
8.7 反向检验：高频形变与未适应投影的源项 ..... 103
8.8 固定双曲乘积排除另一类下沉反例 ..... 104
8.9 与 Teichmüller 有效方程的接口 ..... 105
第九章 面向任意源度量的谐和代表、Hodge 缺陷与最优目标 ..... 106
9.1 唯一谐和代表与无 Weyl 的 Bochner 缺陷 ..... 106
9.2 拉回面积形式：真实缺陷和条件平行性 ..... 107
9．3 Hodge 投影、Euler 配对与杯积的准确作用 ..... 108
9.4 谐和一形式完整测试：共形缺陷与盲点 ..... 109
9.5 最优目标确实存在，但最优不等于共形 ..... 111
9.6 现有工具之间的实际接口 ..... 113
第十章 全局候选的定量约束与有效方程的边界 ..... 114
10.1 扩展图四流形：已知不存在性与未知近似性 ..... 114
10．2 WP 长度下降排除无强迫的有效模型 ..... 116
10.3 现有存在性定理的准确距离 ..... 117

\section*{第一章 归一化、拓扑筛选与定量障碍}

本章将早期研究中的重复计算合并为三组内容：不依赖构造的拓扑与曲率必要条件；从缺陷积分到局部极限矛盾的分析机制；能够实际产生近 Einstein 度量的局部消解方法。经典输入均注明来源；会话内推导和构造不附带首创性或同行评审认证。原始题页与两符号分支的逻辑关系以本稿总论为准。

\section*{1.1 必须固定的量词与范数}

对闭流形上的度量定义
$$\delta_{\sigma}(g)=\left\|\operatorname{Ric}_{g}-\sigma g\right\|_{\mathrm{op}, \infty ; g}, \quad \sigma \in\{1,-1\} .$$
这是相对 Ricci 特征值的最大误差。若 $a g \leq \sigma \operatorname{Ric}_{g} \leq b g 、 0<a \leq b$ ，则 $g^{\prime}=(a+b) g / 2$满足 $\delta_{\sigma}\left(g^{\prime}\right) \leq(b-a) /(b+a)$ 。负分支的单边参数 $-(1+\varepsilon) g \leq \operatorname{Ric}_{g} \leq-g$ 与上述对称参数之间为 $\delta=\varepsilon /(2+\varepsilon)$ 。

记 $\mathcal{N}_{n}$ 为不承载任何 Einstein 度量的闭 $n$ 维流形类，则归一化分支的统一存在性问题等价于
$$\inf _{M \in \mathcal{N}_{n}} \inf _{g \in \operatorname{Met}(M)} \delta_{\sigma}(g)>0 .$$
其否定允许流形随序列变化，只须维数固定。固定一个流形实现误差趋零是更强的构造任务。结论中的 Einstein 度量未被要求与输入接近、属于同一共形类、适应指定投影，或具有预先指定的 Einstein 常数符号。

以下四维曲率积分使用 $E=$ Ric $-\frac{s}{4} g$ 的张量 Hilbert－Schmidt 范数；$W^{ \pm}$视为 $\Lambda^{ \pm}$上的对称无迹算子，使用该算子的 Hilbert－Schmidt 范数。完整四阶曲率张量的范数另记 $|\mathrm{Rm}|_{\text {full }}$ 。相应恒等式为
$$2 \chi \pm 3 \tau=\frac{1}{4 \pi^{2}} \int_{M}\left(2\left|W^{ \pm}\right|^{2}+\frac{s^{2}}{24}-\frac{|E|^{2}}{2}\right) d V, \quad \int_{M}|\operatorname{Rm}|_{\text {full }}^{2}=32 \pi^{2} \chi+4 \int_{M}|E|^{2}$$
这些是经典 Chern－Weil 公式。 ${ }^{1}$

\section*{1.2 严格 Hitchin－Thorpe 端点及正分支的已覆盖类别}

命题1．1（逐点比值3的严格端点）。设 $M^{4}$ 闭、连通、定向。若 $\sigma \operatorname{Ric}_{g}$ 处处正定，且每一点均满足
$$\lambda_{\max }\left(\sigma g^{-1} \operatorname{Ric}_{g}\right) \leq 3 \lambda_{\min }\left(\sigma g^{-1} \operatorname{Ric}_{g}\right),$$
则 $2 \chi(M)>3|\tau(M)|$ 。特别地，$\delta_{\sigma}(g) \leq 1 / 2$ 已足以得到严格不等式。

\footnotetext{
${ }^{1}$ C．LeBrun，Ricci Curvature，Minimal Volumes，and Seiberg－Witten Theory，尤其公式（1）与第三节，https： ／／arxiv．org／pdf／math／0003068。
}

证明．设正特征值为 $r_{i}, a=\min r_{i}>0 、 S=\sum r_{i} 、 Q=\sum r_{i}^{2}$ 。由 $a \leq r_{i} \leq 3 a$ ，
$$Q \leq 4 a S-12 a^{2}, \quad F:=\frac{s^{2}}{24}-\frac{|E|^{2}}{2}=\frac{S^{2}-3 Q}{6} \geq \frac{(S-6 a)^{2}}{6} \geq 0 .$$
等号 $F=0$ 恰要求特征值为 $(3 a, a, a, a)$ ，差一个排列。若（1．1）达到 $2 \chi=3|\tau|$ ，则$F \equiv 0$ ，且一个半 Weyl 张量恒零。简单特征值定义光滑实线丛；在其定向双覆盖上有单位截面 $V$ ，故 Euler 数为零。覆盖乘法性及等号遂给 $\chi=\tau=0$ ，另一个半 Weyl 张量也恒零。

令 $\theta=V^{b}$ ，则 Ric $=\sigma a\left(g+2 \theta^{2}\right) 、 s=6 \sigma a$ 。Schouten 张量为 $P=\sigma a \theta^{2} ; W=0$ 使$P$ 满足 Codazzi 方程。取 $X, Y \perp V$ ，比较 $\left(\nabla_{X} P\right)(V, Y)$ 与 $\left(\nabla_{V} P\right)(X, Y)$ ，得 $\nabla_{X} V=0$ 。因此若 $A=\nabla_{V} V$ ，则
$$\nabla V=\theta \otimes A, \quad d \theta=\theta \wedge A^{b}, \quad \delta \theta=0, \quad|d \theta|^{2}=|\nabla \theta|^{2} .$$
闭覆盖上的一形式积分 Bochner 公式给 $\int \operatorname{Ric}(V, V)=0$ ，但 $\operatorname{Ric}(V, V)=3 \sigma a$ 处处严格同号，矛盾。 \(\square\)

这补上了纯代数在比值3处不能提供的严格性。对于 $2 \chi \leq 3|\tau|$ 的流形，每个度量有 $\delta_{\sigma}(g)>1 / 2$ ；不能进一步声称所有度量的下确界严格大于1／2。

对箱体 $r_{i} \in[1-\delta, 1+\delta]$ ，逐变量凹性使 $F$ 的最小值在顶点取得，直接比较得到
$$q_{*}(\delta)=\min F= \begin{cases}\frac{2}{3}(1-\delta)^{2}, & 0 \leq \delta \leq 1 / 3, \\ \frac{2}{3}(1+\delta)(1-2 \delta), & 1 / 3 \leq \delta \leq 1 / 2 .\end{cases}$$
这里1／2是点态代数非负性的锐端点，不是一般 Einstein 存在性的锐阈值。
命题1．2（复或辛四流形的正分支）。若闭四维流形承载复结构或辛结构，且某个任意度量具有正 Ricci 曲率并满足上述逐点比值条件，则底层光滑流形承载正 Einstein 度量。

证明。命题1．1给出结构定向下 $c_{1}^{2}=2 \chi+3 \tau>0$ ，输入同时有正标量曲率。Chen－LeBrun－Weber 引言中的分类论证将底层微分类型限制为 $S^{2} \times S^{2}$ 或 $\mathbb{C P}^{2} \# k \overline{\mathbb{C P}}^{2} 、 0 \leq k \leq 8$ ；同文结合既有存在性结果保证这些类型均有正 Einstein 度量。 ${ }^{2}$ \(\square\)

输入无须与指定复或辛结构兼容；输出也未必兼容原结构。这是经典分类与存在性定理的推论。

\section*{1．3 Seiberg－Witten 禁区的误差窗口}

令 $X$ 为极小一般型紧复曲面，$c=c_{1}^{2}(X)>0$ ，并设
$$M=X \# k \overline{\mathbb{C P}}^{2} \# \ell\left(S^{1} \times S^{3}\right), \quad K=k+4 \ell, \quad T=2 \chi+3 \tau=c-K, \quad r=\frac{K}{c}-\frac{1}{3} .$$

\footnotetext{
${ }^{2}$ X．Chen，C．LeBrun，B．Weber，On conformally Kähler，Einstein manifolds，引言与 Corollary 2，https：／／arxiv．org／pdf／0705．0710。
}

LeBrun 的估计对任意输入度量给出
$$I:=\int_{M}\left(\frac{s^{2}}{24}+2\left|W^{+}\right|^{2}\right) d V=4 \pi^{2} T+\frac{1}{2} \mathcal{E}, \quad I \geq \frac{8 \pi^{2} c}{3}, \quad \mathcal{E}:=\int_{M}|E|^{2} \geq 8 \pi^{2} c r$$
同一原论文证明 $K \geq c / 3$ 时这些流形不承载任何 Einstein 度量。此处保留其极化和monopole 类选取，不能以只适用于 $b_{+}>1$ 的简化表述替代全部输入。

命题1．3（对称归一化的显式下界）。若 $c / 3 \leq K<c$ ，则任意光滑度量满足
$$\delta_{-}(g) \geq \Phi(r), \quad \Phi(r)= \begin{cases}\sqrt{r / 2}, & 0 \leq r \leq 2(2-\sqrt{3})^{2}, \\ \frac{2 \sqrt{r}}{\sqrt{6}+\sqrt{r}}, & 2(2-\sqrt{3})^{2} \leq r<2 / 3 .\end{cases}$$
证明．当 $\delta<1$ ，写 Ricci 特征值为 $-y_{i}$ ，则
$$\frac{|E|^{2}}{s^{2}}=\frac{\sum y_{i}^{2}}{\left(\sum y_{i}\right)^{2}}-\frac{1}{4} \leq A(\delta):= \begin{cases}\delta^{2} / 4, & \delta \leq 2-\sqrt{3} \\ 3 \delta^{2} /\left[4(2-\delta)^{2}\right], & \delta \geq 2-\sqrt{3}\end{cases}$$
固定其余三个变量后，$\left(t^{2}+B\right) /(t+A)^{2}$ 的导数只由 $A t-B$ 决定，内部临界点是极小值，故最大值在箱体顶点。若 $m$ 个变量取 $1+\delta$ ，顶点值为 $m(4-m) \delta^{2} /[4+(2 m-4) \delta]^{2}$ ；比较 $m=1,2$ 即得上式。当 $\delta<1 / 2$ ，由 $T>0$ 与前述积分下界，
$$3 r \leq \frac{\mathcal{E}}{I} \leq 24 A(\delta) .$$
反解即得 $\Phi$ 。因 $\Phi(r) \leq 1 / 2$ ，其余 $\delta$ 自动满足结论。 \(\square\)

因此若 $\delta \leq 2-\sqrt{3}$ ，候选只能位于
$$\frac{1}{3} \leq \frac{K}{c} \leq \frac{1}{3}+2 \delta^{2}$$
若严格超过临界值，整数性还要求 $c \geq 1 /\left(6 \delta^{2}\right)$ 。例如
$$X_{m}=\Sigma_{2} \times \Sigma_{3 m+1}, \quad M_{m}=X_{m} \#(8 m+1) \overline{\mathbb{C P}}^{2}$$
满足 $c=24 m$ ，故 $\delta_{-}(g) \geq 1 / \sqrt{48 m}$ 。下界趋零不产生达到该下界的度量。固定临界例子 $X_{6} \# 8 \overline{\mathbb{C P}}^{2}$ 中 $X_{6} \subset \mathbb{C P}^{3}$ 为光滑六次曲面，$c=24$ ；其误差下确界未由该式决定。

\section*{1.4 从规范理论缺陷到局部不可实现谱}

以下取 $\ell=0, k \geq c / 3$ ，采用复定向和 $s<0$ 。令
$$u=-s, \quad w=\left|W^{+}\right|, \quad \mu_{1} \leq \mu_{2} \leq \mu_{3}, \quad q=-\mu_{1}, \quad d=k-c / 3$$
以及
$$D_{W}=\int\left(w-\frac{u}{8 \sqrt{6}}\right)^{2}, \quad P=\int\left(\frac{2}{3} u+2 \sqrt{\frac{2}{3}} w\right)^{2}, \quad P_{e}=\int\left(\frac{2}{3} u+2 q\right)^{2} .$$
LeBrun 最小 Weyl 特征值估计给 $P_{e} \geq 32 \pi^{2} c$ ；无迹三阶算子的代数性质给 $P \geq P_{e}$ 。

命题1．4（非负缺陷分解）。上述条件下，
$$6 \mathcal{E}=\frac{64}{3} D_{W}+\left(P-P_{e}\right)+\left(P_{e}-32 \pi^{2} c\right)+48 \pi^{2} d$$
特别地，
$$D_{W} \leq \frac{9}{32} \mathcal{E}, \quad \int\left(\mu_{3}-\mu_{2}\right)^{2} \leq \frac{9}{2} \mathcal{E} .$$
证明。展开平方得 $12 I=P+\frac{64}{3} D_{W}$ ，代入 $I$ 的拓扑表达式即得恒等式。置 $b=\sqrt{2 / 3} w- q \geq 0$ ，则
$$\left(\mu_{3}-\mu_{2}\right)^{2}=3 b(\sqrt{2 / 3} w+q), \quad P-P_{e}=\int 4 b\left(\frac{2}{3} u+\sqrt{2 / 3} w+q\right)$$
得到第二个界。 \(\square\)

其几何内容并非只有一个积分下界：若误差趋零并在固定尺度上获得强 $W^{2, p} 、 p>$4 的局部极限，则极限必须同时满足
$$\operatorname{Ric}=-g, \quad s=-4, \quad \operatorname{spec}\left(W^{+}\right)=(-1 / 6,1 / 12,1 / 12) .$$
Einstein 条件使 $W^{+}$调和；Derdziński 定理使具有此非零恒范数双特征值谱的度量局部 Kähler。但 Kähler 恒等式要求 $\left|W^{+}\right|^{2}=s^{2} / 24=2 / 3$ ，目标谱却给 $1 / 24$ ，矛盾。 ${ }^{3}$

命题1．5（三个有完整附加条件的间隙）。在上述全部吹起流形组成的类中：
\begin{itemize}
\item[1．] 给定 $v>0$ ，若每个单位球体积至少为 $v$ ，则 $\delta_{-}(g) \geq \eta(v)>0$ 。
\item[2．] 给定 $\Lambda<\infty$ ，若 $\sup |\operatorname{Rm}|_{\text {full }} \leq \Lambda$ ，则 $\delta_{-}(g) \geq \eta(\Lambda)>0$ ，允许塌缩。
\item[3．] 限制输人为常标量且 Bach－flat 度量时，存在全类统一的 $\eta_{\mathrm{B}}>0$ ，不需要总体积、直径或注入半径界。
\end{itemize}

证明机制。令 $f=(w-u /(8 \sqrt{6}))^{2}+\left(\mu_{3}-\mu_{2}\right)^{2}$ 。由 $|E|^{2} \leq 4 \delta^{2}, f_{M} f \leq 153 \delta^{2} / 8$ 。Ricci下界与 Fubini 允许选取固定半径球，使其缺陷积分或归一化平均趋零。

第一项使用 Cheeger－Naber 四维谐和半径估计：在 Ricci 有界且球非塌缩时，小谐和半径集合的体积至多 $C r^{4}$ ，因而可找到固定大小的谐和坐标片。 ${ }^{4}$ 在共同谐和坐标中， $\operatorname{Ric}_{i j}=-\frac{1}{2} g^{a b} \partial_{a} \partial_{b} g_{i j}+Q_{i j}(g, \partial g)$ 。先取得 $C^{1, \alpha}$ 强收敛和 $W^{2, p}$ 弱收敛，再利用Ricci 残差趋零对差方程作内部随圆估计，升级为强 $W^{2, p}$ ；只断言极限光滑。

第二项以曲率界取得固定无共轭半径，在指数映射定义域展开塌缩球。需要的积分传递不是基础球的绝对积分，而是
$$\int_{B_{\phi^{*} g}(0, r)} f \circ \phi \leq C r^{4} f_{B_{g}(p, r)} f .$$

\footnotetext{
${ }^{3}$ A．Derdziński，Self－dual Kähler manifolds and Einstein manifolds of dimension four，Propositions 2、5， https：／／www．numdam．org／item／CM＿1983＿＿49＿3＿405＿0．pdf。
${ }^{4}$ J．Cheeger，A．Naber，Regularity of Einstein manifolds and the codimension 4 conjecture，Theorem 1．13， https：／／arxiv．org／pdf／1406．6534。
}

这里 $\phi: B_{\mathbb{R}^{4}}(0, R) \rightarrow M$ 为局部微分同胚，$\phi^{*} g$ 与欧氏度量统一双侧可比，且 $r$ 相对内部边界距离足够小。证明是：从任一纤维原像沿长度小于 $2 r$ 的路径提升至基础球任一点；不同起点给不同终点。面积公式将局部覆盖重数乘基础球体积控制于展开球体积，得到（1．4）。无需覆盖重数统一有界。此外 Bishop－Gromov 比较使 $\int_{M} f_{B(p, r)} f d V_{p} \leq C(r) \int_{M} f$ ，保证可选低平均缺陷中心。展开后复用第一项的局部矛盾。

第三项还要找到一个有曲率界的好球。SW 标量估计给 $V \geq 32 \pi^{2} c / 25(\delta \leq 1 / 4)$ ，Noether 不等式与 $k<c$ 给 $\chi(M) \leq 42 c$ ，故 $f \mid$ Rm $\left.\right|_{\text {full }} ^{2} \leq 1051$ 。Fubini 及 Markov 在固定足够小半径上产生占至少 $3 / 4$ 总体积的低曲率能量中心。Ge－Jiang 对固定 critical类型的无塌缩条件局部正则性，给该球内的统一曲率界；在这些中心中再选低平均缺陷球，最后用（1．4）。 ${ }^{5}$ \(\square\)

第三项的附加曲率方程不能删除；仅有 Ricci 界与小绝对曲率能量时，原记录所需的无塌缩展开接口并未在全量词下核准，本稿不列无条件全族间隙。

命题1．6（临界固定流形的必要退化）。固定 $k=c / 3$ 的上述流形。若 $\delta_{-}\left(g_{j}\right) \rightarrow 0$ ，则
$$\begin{aligned}
\operatorname{Vol}\left(g_{j}\right) \rightarrow \frac{32 \pi^{2} c}{9}, & \sup _{p} \operatorname{Vol} B_{g_{j}}(p, 1) \rightarrow 0, \\
\operatorname{diam}\left(g_{j}\right) \rightarrow \infty, & \sup \left|\operatorname{Rm}_{g_{j}}\right|_{\text {full }} \rightarrow \infty .
\end{aligned}$$
证明．（1．2）与固定拓扑先给体积上界，故两个缺陷的绝对积分趋零。任一不塌缩单位球都会产生前述局部矛盾。又 $\int w^{2}=\int u^{2} / 384+o(1) 、 u \rightarrow 4$ ，于是 $I=\frac{3}{4} V+o(1)= 8 \pi^{2} c / 3+o(1)$ ，得到体积极限。有界直径结合 Ricci 下界和正总体积会给单位球体积下界；最后一项来自命题1．5。 \(\square\)

另一个直接作用于构造的结论是：若 $U \subset M$ 是与复定向一致的 Kähler 区域，则
$$\frac{\operatorname{Vol}(U)}{\operatorname{Vol}(M)} \leq \frac{3 \delta^{2}}{(1-\delta)^{2}} .$$
因为 $U$ 上 $w=u /(2 \sqrt{6})$ ，缺陷被积函数至少为 $3(1-\delta)^{2} / 8$ 。若 $U$ 更是 Ric $=-g$ 的KE 区域，右端可改为 $3 \delta^{2}$ 。因此保留正比例 Kähler 外部而只缩小局部手术区，不能在该禁区实现误差趋零。

\section*{1.5 熵障碍、直径与有限覆盖}

定义
$$\lambda(M)=\inf _{g} h(g) \operatorname{Vol}(g)^{1 / 4}, \quad A=\chi-\frac{3}{2}|\tau|, \quad B=\frac{\lambda(M)^{4}}{108 \pi^{2}},$$
其中 $h(g)$ 为普适覆盖上的体积熵。Kotschick 的 Einstein 必要条件为 $A \geq B$ 。 ${ }^{6}$

\footnotetext{
${ }^{5}$ H．Ge，W．Jiang，є－regularity for shrinking Ricci solitons and Ricci flows，Theorem 5．1，https：／／arxiv． org／pdf／1707．05511；C．Liedtke，Algebraic surfaces of general type with small $c_{1}^{2}$ in positive characteristic， Noether 不等式的相关表述，https：／／arxiv．org／pdf／math／0702548。
${ }^{6}$ D．Kotschick，Entropies，volumes，and Einstein metrics，https：／／arxiv．org／pdf／math／0410215。
}

命题 1.7 （带最大 Ricci 误差的熵界）。若 $0 \leq \delta=\delta_{-}(g) \leq 1 / 2$ ，则
$$A \geq F(\delta) B, \quad F(\delta)= \begin{cases}((1-\delta) /(1+\delta))^{2}, & \delta \leq 1 / 3 \\ (1-2 \delta) /(1+\delta), & 1 / 3 \leq \delta \leq 1 / 2\end{cases}$$
当 $B>0,0 \leq x=A / B<1$ ，任意度量均有
$$\delta_{-}(g) \geq \begin{cases}(1-x) /(2+x), & 0 \leq x \leq 1 / 4, \\ (1-\sqrt{x}) /(1+\sqrt{x}), & 1 / 4 \leq x<1 .\end{cases}$$
证明．由（1．1）、（1．2），$A \geq q_{*}(\delta) V /\left(8 \pi^{2}\right)$ 。Ricci 比较给 $h(g) \leq \sqrt{3(1+\delta)}$ ，故 $\lambda(M)^{4} \leq 9(1+\delta)^{2} V$ 。合并并反解单调函数 $F$ 即得。 \(\square\)

给定 $D<\infty$ ，若另有 $A \leq B$ 且 $\operatorname{diam}(g) \leq D$ ，则足够小的 $\delta_{-}(g)$ 强迫 $M$ 微分同胚于闭实双曲四流形。证明是：当 $\delta \leq 1 / 3$ ，上式给 $h(g) \geq \sqrt{3(1-\delta)}$ ；缩放为$\widehat{g}=(1+\delta) g / 3$ 后，
$$\operatorname{Ric}_{\widehat{g}} \geq-3 \widehat{g}, \quad h(\widehat{g}) \geq 3 \sqrt{\frac{1-\delta}{1+\delta}} \rightarrow 3 .$$
Chen－Xu 的有界直径、近最大熵微分同胚刚性适用，不需体积下界。 ${ }^{7}$ 阈值依赖 $D$ ，不能换成维数统一阈值。

若 $N \rightarrow M$ 为 $d$ 层有限无分歧覆盖，则 $\lambda(N)^{4} \leq d \lambda(M)^{4} 、 A(N)=d A(M)$ 。所以$A(M)>B(M)$ 会传到每个有限覆盖，已失效的严格熵障碍不能靠取有限覆盖恢复。

\footnotetext{
${ }^{7}$ L．Chen，S．Xu，Quantitative rigidity of almost maximal volume entropy for both RCD spaces and integral Ricci curvature bound，Theorem 1．2，https：／／arxiv．org／pdf／2211．01082。
}

\section*{第二章 可核查的局部构造与其真实边界}

本章的核心区别是：可以改变输入度量的 Weyl 二次项而保持 Ricci 二次项；这允许构造最大 Ricci 误差趋零的退化度量，却不保证能在同一底层流形上排除其他 Einstein度量。以下构造均指固定局部群表示、固定填入核、固定端部标记；不对任意抽象边界粘接作断言。

\section*{2.1 为什么普通缩小内核不够}

若内核仅 Ricci－flat，则缩放核 $a^{2} k 上 \|$ Ric $-\sigma g \|_{\mathrm{op}}=1$ ，不会趋零。若内核仅标量平坦而 Ricci 非零，缩放反而使 $\left|\operatorname{Ric}_{a^{2} k}\right|_{a^{2} k}=a^{-2}\left|\operatorname{Ric}_{k}\right|_{k}$ 。因此普通 Burns 吹起不能直接用作最大误差构造。保持普通吹起复结构的 Kähler 度量更不可能有严格负 Ricci：异常曲线 $C^{2}=-1$ 满足 $\int_{C} \rho=2 \pi c_{1} \cdot C=2 \pi>0$ 。

所需内核必须先解真实线性 Ricci 方程
$$D \operatorname{Ric}_{k}(h)=\sigma k .$$
这与仅解消去规范项后的方程有别；恢复 Bianchi 条件是构造的一部分。

\section*{2．2 Eguchi－Hanson 核的显式修正}

采用
$$\sigma_{3}=d \psi+\cos \theta d \phi, \quad \sigma_{1}^{2}+\sigma_{2}^{2}=d \theta^{2}+\sin ^{2} \theta d \phi^{2}, \quad e=d r^{2}+\frac{r^{2}}{4} \sum_{i} \sigma_{i}^{2}$$
且 $\psi$ 的周期为 $2 \pi$ 。在 $r=1$ 收缩 Hopf 纤维，所得光滑核为 $\mathcal{O}(-2)$ 盘丛。对小实参数 $\Lambda$ ，置
$$c_{\Lambda}=(1-\Lambda / 4)^{2}-1, \quad G_{\Lambda}(r)=\frac{\sqrt{1+c_{\Lambda} r^{2}}}{r^{4}} \int_{1}^{r} \frac{s^{3}\left(4-\Lambda s^{2}\right)}{\left(1+c_{\Lambda} s^{2}\right)^{3 / 2}} d s, \quad F_{\Lambda}=\left(1+c_{\Lambda} r^{2}\right) G_{\Lambda} .$$
则
$$q_{\Lambda}=\frac{d r^{2}}{F_{\Lambda}}+\frac{r^{2}}{4}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+G_{\Lambda} \sigma_{3}^{2}\right), \quad \operatorname{Ric}\left(q_{\Lambda}\right)=\Lambda q_{\Lambda} .$$
有效域要求 $1+c_{\Lambda} r^{2}>0 、 4-\Lambda r^{2}>0$ 。每个固定 $0<\beta<1 / 2$ 都允许 $1<r \leq 2|\Lambda|^{-\beta}$ ，只要 $|\Lambda|$ 足够小。

方程及光滑性核验。双轴 Bianchi IX 的00－33方程由 $F=\left(1+c r^{2}\right) G$ 恒满足； $11=22$方程化为
$$r\left(1+c r^{2}\right) G^{\prime}+\left(4+3 c r^{2}\right) G=4-\Lambda r^{2}$$

其积分因子为 $r^{4} / \sqrt{1+c r^{2}}$ ，初值 $G(1)=0$ 给上述解。余下 $00=33=Q$ 的共同分量，由收缩 Bianchi 恒等式 $Q^{\prime}+2(\dot{\alpha} / \alpha)(Q-\Lambda)=Q^{\prime}$ 强迫 $Q=\Lambda$ ，其中 $\alpha=r / 2$ 。在异常球面附近，$F^{\prime}(1)=4-\Lambda 、 G^{\prime}(1)=(4-\Lambda) /\left(1+c_{\Lambda}\right)$ ；测地距离 $t$ 下收缩纤维系数为$(4-\Lambda)^{2} t^{2} /\left[16\left(1+c_{\Lambda}\right)\right]+O\left(t^{4}\right)=t^{2}+O\left(t^{4}\right)$ 。配合 $2 \pi$ 周期，整个度量在固定盘丛上光滑。 \(\square\)

双轴 Einstein 方程和该度量族的背景属于经典理论。 ${ }^{1}$
在 $\Lambda=0$ 处求导，并减去光滑径向规范场 $V=\frac{5}{72}\left(r^{3}-r^{-1}\right) \partial_{r}$ 的 Lie 导数，得到
$$\begin{aligned}
\widetilde{h}= & -\frac{r^{2}\left(7 r^{2}-5\right)}{36\left(r^{2}-1\right)\left(r^{2}+1\right)^{2}} d r^{2}-\frac{5\left(r^{4}-1\right)}{144}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right) \\
& +\left(-\frac{r^{4}}{72}+\frac{1}{16}-\frac{r^{-2}}{12}+\frac{5 r^{-4}}{144}\right) \sigma_{3}^{2}
\end{aligned}$$
其极坐标表面极点不破坏光滑性，且
$$D \operatorname{Ric}_{\mathrm{EH}} \widetilde{h}=g_{\mathrm{EH}}, \quad \widetilde{h}=H_{*}+O\left(r^{-2}\right),$$
其中
$$H_{*}=-\frac{5}{36}\left(r^{2} e-(x \cdot d x)^{2}\right)+\frac{1}{12}\langle J x, d x\rangle^{2}, \quad D \operatorname{Ric}_{e} H_{*}=e .$$
尾项可逐阶求导。这里 $J$ 对应 $\sigma_{3}$ 的 Hopf 方向； $\mathcal{R}_{+}\left(H_{*}\right)=\operatorname{diag}(1 / 2,1 / 2,0)$ ，指定 EH周期方向位于零特征空间。乘以 $\sigma$ 得两个符号的真实线性修正。

\section*{2.3 同 Ricci、不同 Weyl 的对数拼接}

命题2．1（固定 $A_{1}$ 分辨上的近 Einstein 构造稿）。设 $\left(\mathcal{O}, g_{0}\right)$ 是闭、定向四维 Einstein轨形， $\operatorname{Ric}_{g_{0}}=\sigma g_{0}$ ，仅有有限个孤立 $A_{1}$ 点。按标准 ALE 端部坐标在每一点填入固定EH 核，方向和固定正交标记可逐点指定。所得固定光滑分辨 $M$ 上有光滑度量族满足
$$\delta_{\sigma}\left(g_{a}\right) \leq C|\log a|^{-1} \rightarrow 0 .$$
它在趋零的奇点邻域外等于 $g_{0}$ ，GH 收敛到 $\mathcal{O}$ ，并具有 EH 泡极限。
证明。正规坐标中写 $g_{0}=e+H_{0}+O\left(r^{4}\right)$ 。选择（2．3）的对应方向内端 $H_{1}=\sigma H_{*}$ ，并用 $h=\sigma \widetilde{h}$ 。二者 Ricci 线性项相同，故 $K=H_{0}-H_{1}$ 是纯 Weyl 正规二次项，满足
$$K_{i j}=-\frac{1}{3} C_{i k j l} x^{k} x^{l}, \quad \operatorname{tr} K=\operatorname{div} K=\Delta K=0, \quad K(x, \cdot)=0 .$$
取物理长度尺度 $a$ 、内截断半径 $b=a^{1 / 2}$ 、外半径 $R=a^{1 / 4}$ 。内核用 $G_{a}=a^{2}\left(g_{\mathrm{EH}}+a^{2} h\right)$ 。真实 Ricci Taylor 余项在物理范数中为
$$\left|\operatorname{Ric}\left(G_{a}\right)-\sigma G_{a}\right|_{G_{a}} \leq C a^{-2} a^{4}(1+\rho)^{2} \leq C\left(a^{2}+r^{2}\right), \quad r=a \rho .$$

\footnotetext{
${ }^{1}$ M．Cvetič，G．Gibbons，H．Lü，C．Pope，Bianchi IX self－dual Einstein metrics and singular $G_{2}$ manifolds，第4．1节，https：／／arxiv．org／pdf／hep－th／0206151。这里使用完整 Einstein 双轴方程，不把所有双轴解误称为自对偶解。
}

关键缩放因子是 $a^{-2}$ 。在 $r \asymp b$ 截到 $e+H_{1}$ ，误差为
$$O\left(b^{2}+a^{4} b^{-6}+a^{4} b^{-4}\right)=O(a)$$

在 $4 b<r<R / 2$ 取 $\chi(r)=\psi(\log (r /(4 b)) / L), L=\log (R /(8 b))$ ，并令 $g=e+H_{1}+ \chi K$ 。径向截断保持 $\chi K$ 无迹、无散度，故
$$D \operatorname{Ric}_{e}(\chi K)=-\frac{1}{2 r^{2}}\left(\frac{\psi^{\prime \prime}}{L^{2}}+\frac{6 \psi^{\prime}}{L}\right) K .$$
因为 $K=O\left(r^{2}\right)$ ，它为全环带统一的 $O\left(L^{-1}\right)$ 。非线性余项由 $|q|\left|D^{2} q\right|+|D q|^{2}=O\left(r^{2}\right)$控制。最后于 $r \asymp R$ 加回外部 $O\left(r^{4}\right)$ 余项，贡献 $O\left(R^{2}\right)$ 。全部替换区直径为 $O(R)$ ，逐点有限拼接即得结论。 \(\square\)

该命题是一份有完整局部误差证明的会话构造稿；它与 Ozuch 提出的球面商最大Ricci 误差平滑化问题相接，但此处不认证其文献优先权。 ${ }^{2}$ 它未提供任何所得 $M$ 的全局 Einstein 不存在性。

旧两次截断允许 $b=a^{\gamma}, R=a^{\kappa}, 0<\kappa<\gamma<2 / 3$ 。其各误差必须相加：$O\left(b^{2}+\right. a^{4} b^{-6}+a^{4-\epsilon} b^{-4+\epsilon}+R^{2}+L^{-1}$ ）。若改用（2．2）的完整精确核 $h_{a}=a^{2} q_{\sigma a^{2}}$ ，并在对数环带直接取 $h_{a}+\chi K$ ，则可取消内端截断，得到更强尺度范围
$$\delta_{\sigma}\left(g_{a}\right) \leq C\left(L^{-1}+R^{2}+a^{4} b^{-4}+a^{4} R^{-6}\right), \quad 0<\gamma<1, \quad 0<\kappa<\min (\gamma, 2 / 3) .$$
在新尺度上应以物理 Ricci－flat EH 度量为背景，不能仍假定整个度量与欧氏度量之差为统一 $O\left(r^{2}\right)$ 。

\section*{2．4 ADE、周期与 type T 核：相同机制的准确推广}

\section*{2．4．1 共线周期的 ADE 核}

设 $\Gamma \subset S U(2)$ 非平凡，选固定光滑 Kronheimer ALE 度量，周期为 $\left(\zeta_{1}, 0,0\right)$ ，且$\zeta_{1}$ 避开所有根超平面。则可构造
$$D \operatorname{Ric}_{k} h_{\sigma}=\sigma k, \quad h_{\sigma}=\sigma H_{*}+O\left(r^{-2} \log r\right),$$
并有各固定阶导数估计。所需 Fredholm、束分解及 ALE 渐近分别来自 Ozuch、Biquard、Auvray。 ${ }^{3}$

这里不能仅检查三个熟悉的核模式。完整证明有两个不可省略的接口。其一，任意负权对偶核 $q=O\left(r^{-\gamma}\right)$ 先由迹与 Bianchi 一形式的 Bochner 最大值原理变成 TT 张量。Newton 势展开给
$$q_{i j}=\frac{C_{i j}}{r^{2}}+\frac{A_{i j k} x_{k}}{r^{4}}+Q_{i j}^{(-4)}+O\left(r^{-4-\gamma}\right) .$$

\footnotetext{
${ }^{2}$ T．Ozuch，Noncollapsed degeneration of Einstein 4－manifolds，II，Corollary 15 后的问题及 Remark 51， https：／／arxiv．org／pdf／1909．12960v2。
${ }^{3}$ T．Ozuch，上引 Noncollapsed degeneration II，Lemmas 4．2－4．3；O．Biquard，Non dégénérescence et sin－ gularités des métriques d＇Einstein，https：／／arxiv．org／pdf／1704．05389；H．Auvray，From ALE to ALF gravitational instantons．II，https：／／arxiv．org／pdf／1304．3342。
}

无散度消去 $C$ ；负三次项还必须使用无迹：若 $b_{j}=\sum_{i} A_{i j i}$ ，无散度只给 $A_{i j k}=\left(b_{j} \delta_{i k}+\right. \left.b_{i} \delta_{j k}-b_{k} \delta_{i j}\right) / 4$ ，无迹才给 $b=0$ 。故所有对偶核实际属于 $L^{2}$ ，首项为负四次。

其二，由 $\operatorname{Sym}_{0}^{2} \simeq \Lambda^{+} \otimes \Lambda^{-}$，完整 $L^{2}$ 核写成 $o=\sum_{i} \omega_{i} \circ \Omega_{i}$ 。反演 $\iota(x)=x / r^{2}$使 $\Omega_{i}^{(-4)}=\sum_{j} c_{i j} \iota^{*} \omega_{j}^{e}$ 。将 $\Omega_{i}$ 减去端部原始形式的微分，得到紧支撑闭代表；以 $\left[\omega_{2}\right]= \left[\omega_{3}\right]=0$ 作 Stokes 配对，得 $c_{i 2}=c_{i 3}=0$ 。完整 $3 b_{2}$ 维核的首项像因而位于三个方向中，绝不是说核只有三维。

将 $\sigma H_{*}$ 变到 Bianchi 规范，其四元数径向标架系数为 $-\sigma r^{2} \operatorname{diag}(1 / 3,1 / 6,1 / 4,1 / 4)$ ；它与所有余核首项的边界配对为零。负权求解后，Bianchi 一形式趋零并满足齐次粗Laplace 方程，恢复（2．1）；Newton 势再给 $O\left(r^{-2} \log r\right)$ 尾项。因此对表示与定向匹配的 ADE 填入，复用对数构造得到
$$\delta_{\sigma}\left(g_{a}\right) \leq C\left(|\log a|^{-1}+a^{1 / 4}\right) .$$
一般群不含 $-I$ 时，外部余项仅为 $O\left(r^{3}\right)$ ，外截断误差是 $O(R)$ 。也不能把 $A_{1}$ 的任意方向选择搬到一般 ADE 链接。

\section*{2．4．2 零 Kähler 周期与 type T 平滑}

若固定 hyperkähler ALE 核满足 $\left[\omega_{1}\right]=0$ ，周期允许张成另两个方向组成的平面。此时可用
$$H_{T}=-\frac{\sigma}{18}\left(r^{2} e-(x \cdot d x)^{2}\right)-\frac{\sigma}{6}\left\langle J_{1} x, d x\right\rangle^{2}, \quad \mathcal{R}_{+}\left(H_{T}\right)=\sigma P_{\omega_{1}}$$
Stokes 现在给 $c_{i 1}=0$ ；Bianchi 首项为 $-\sigma r^{2} \operatorname{diag}(1 / 3,1 / 3,1 / 6,1 / 6)$ ，与剩余所有首项配对为零。因此真实线性延拓仍成立。

每个循环 type $T$ 锥
$$\frac{1}{d m^{2}}(1, d m q-1), \quad d \geq 1, m \geq 2, \operatorname{gcd}(m, q)=1$$
都有一个可选择的平面周期 ALE 填充。覆盖模型可写为
$$x y=\prod_{j=1}^{d}\left(z^{m}-c_{j}\right), \quad(x, y, z) \longmapsto\left(\eta x, \eta^{-1} y, \eta^{q} z\right), \quad \eta^{m}=1,$$
其中 $c_{j} \neq 0$ 且互异。非恒等群元的固定点只能是环境原点，而原点不在曲面上，故商光滑。Şuvaina 的平面 Gibbons－Hawking 中心构造提供保持该作用的 Ricci－flat ALE度量及标准端部标记。 ${ }^{4}$ 先在覆盖上消去全部余核，再有限平均下降；商的 $b_{2}=0$ 不意味着 Einstein 线性核为零。

\section*{2．4．3 KE 外部完整二次项可直接匹配}

若外部是与 $\omega_{1}$ 匹配的 KE 度量，则其实际二次项 $H_{0}$ 满足 $\mathcal{R}_{+}\left(H_{0}\right)=\sigma P_{\omega_{1}}$ 。因此$H_{0}-H_{T}$ 仅含 $W^{-}$。固定全部自对偶形式的 $S U(2)$ 因子，对 $W^{-}$的球面平均为零，而

\footnotetext{
${ }^{4}$ I．Şuvaina，ALE Ricci－flat Kähler metrics and deformations of quotient surface singularities，https：／／arxiv．org／html／1102．2672v1；E．Wright，Quotients of gravitational instantons，https：／／arxiv．org／pdf／1102．2442。
}

余核首项在该群下不变；故新增边界配对全部为零。先在 $S^{3}$ 上平均，再除以群阶，不要求该旋转群在实际 ALE 核上延拓为等距作用。

于是可将完整 $H_{0}$ 解人核，不再需要对数过渡。普通半径 $b$ 截断得到
$$\delta_{\sigma}\left(g_{a}\right) \leq C\left[a^{2}+b^{2}+b^{\nu}+a^{4} b^{-6}+a^{4} b^{-4} \log (b / a)\right]$$
其中一般外端 $\nu=1$ ，含 $-I$ 的外群给 $\nu=2$ 。分别取 $b=a^{4 / 7} 、 b=a^{1 / 2}$ ，得到 $O\left(a^{4 / 7}\right)$ 、$O(a)$ 。固定复结构的 Kähler 势变分通常不够：其 Ricci 形式变化全局正合，不能在具有非零 Kähler 周期的异常曲线上满足 $D \rho=\sigma \omega$ ；上述一般对称张量方法准确避开这一限制。

\section*{2.5 最短的 Wahl 填充证明与高阶增强的分离}

指定1／4（1，1）KE 奇点时，上述一般 ADE 分析可用更短的已发表 EH 定理替代。取
$$Q=\left\{x y=z^{2}-1\right\}, \quad \tau(x, y, z)=(-x,-y,-z) .$$
它自由作用，且 $Q / \tau \simeq T^{*} \mathbb{R P}^{2}$ ：将 $Q$ 化为 $\sum z_{i}^{2}=1$ 后，映射 $(q, p) \mapsto \sqrt{1+|p|^{2}} q+i p$给 $T^{*} S^{2} \simeq Q, \tau$ 为 $(q, p) \mapsto(-q,-p)$ 。中心锥的参数 $(x, y, z)=\left(u^{2}, v^{2}, u v\right)$ 下，商作用来自 $(u, v) \mapsto(i u, i v)$ ，故端表示确为1／4（1，1）。

外部 Kähler 方向记为 $\omega_{3}$ 。群作用保持 $\omega_{3}$ 而反转零截面，故其周期为零，EH 非零周期方向 $\zeta$ 满足 $\zeta \perp \omega_{3}$ 。KE 曲率块 $\mathcal{R}_{+}\left(H_{0}\right)=\sigma P_{\omega_{3}}$ 因而满足 $\mathcal{R}_{+}\left(H_{0}\right) \zeta=0$ 。Biquard的 EH 真实线性延拓定理遂给 $D \operatorname{Ric}_{k} h=\sigma k 、 h=H_{0}+O\left(\rho^{-2+\epsilon}\right)$ ；其定理允许 $H_{0}$ 不预先在 Bianchi 规范中。 ${ }^{5}$ 有限平均后下降。取 $b=a^{1 / 2} 、 \epsilon=1 / 2$ ，残差为
$$C\left[b^{2}+a^{4} b^{-6}+a^{4-\epsilon} b^{-4+\epsilon}\right]=C\left(a+a+a^{7 / 4}\right)=O(a) .$$
应用于 Şuvaina 指定的 $\widehat{X}_{4}$ 及其标准 rational blowdown $N=Y_{4}=W_{4,1}$ ，便是在同一个指定光滑流形上的构造；其代数与拓扑输入在后章详述。 ${ }^{6}$ 该最低阶结果不依赖四次匹配、外部 Green 模式或 QG 障碍计算。

高阶增强需要额外解
$$D \operatorname{Ric}_{k}\left(k_{4}\right)=\sigma k_{2}-\operatorname{Ric}_{k}^{(2)}\left(k_{2}, k_{2}\right), \quad B_{k} k_{4}=0, \quad k_{4}=H_{4}+O\left(\rho^{\epsilon}\right), \quad 0<\epsilon<1,$$
其中 $k_{2}$ 为第一解、 $\operatorname{Ric}^{(2)}$ 包含 Taylor 系数1／2。会话内针对该 Wahl／KE 组合计算了三个内端障碍的消失：周期方向分量含秩一曲率块的二阶小行列式；第三分量由自由商奇偶性消失；第二分量须利用一阶连接仅沿一个 Lie 代数方向、 $d \phi_{2}=0$ 、规范周期$\int_{\Sigma} \phi_{2}=0$ ，以及
$$\Omega=\Omega_{-4}+O\left(\rho^{-8}\right), \quad \lim _{R \rightarrow \infty} \int_{Y_{R}} \Omega \wedge \phi_{2}=0 .$$

\footnotetext{
${ }^{5}$ O．Biquard，Désingularisation de métriques d＇Einstein．I，方程（13）、Theorem 3．1、Lemma 4．1，https： ／／arxiv．org／pdf／1105．4904。
${ }^{6}$ I．Şuvaina，The Yamabe invariant of a class of symplectic 4－manifolds，第2、4节，https：／／arxiv．org／ht ml／1410．1236v1。
}

最后一式的无穷远首项由 TT 通量 $\int_{S_{R}} T(\nu, x)=\int_{B_{R}}(\operatorname{div} T)(x)+\operatorname{tr} T=0$ 消去。必须在同心截断下取极限，不能声称该单独积分绝对可积。Biquard 原文提供带有限维障碍的第二方程，额外第二分量消项属于本会话的特定计算。 ${ }^{7}$

规范同步不可省略：普通测地二次项满足 $B_{e} H^{\mathrm{geo}}=-2 \sigma x^{b} / 3$ ，应取 $X=-\sigma r^{2} x / 18$ ，将 $H_{2}$ 改为 $H^{\text {geo }}+\mathcal{L}_{X} e$ ，并同步更新 $H_{4}$ 。径向三次梯度场不改变一阶标架旋转。又由$B_{g} \operatorname{Ric}_{g}=0 、 B_{g} g=0$ 的 Taylor 展开，$B_{k}\left(\sigma k_{2}-\operatorname{Ric}^{(2)}\left(k_{2}, k_{2}\right)\right)=0$ ，所以真实方程与Bianchi 条件相容。

命题2．2（明确以四次延拓为输入的误差提升）。若指定 Wahl／KE 数据具有上述 $k_{2}, k_{4}$及逐阶尾界，内度量 $a^{2}\left(k+a^{2} k_{2}+a^{4} k_{4}\right)$ 在 $b=a^{2 / 5}$ 处普通截到外部 $e+H_{2}+H_{4}+O\left(r^{6}\right)$ ，则
$$\delta_{-}\left(g_{a}\right) \leq C a^{8 / 5} .$$
证明．物理内残差为 $O\left(w^{4}\right)$ 。截断残差为
$$C\left[b^{4}+a^{4} b^{-6}+a^{4-\epsilon} b^{-4+\epsilon}+a^{4-\epsilon} b^{-2+\epsilon}\right]$$
取 $\epsilon=1 / 2$ ，四项依次为 $a^{8 / 5}, a^{8 / 5}, a^{21 / 10}, a^{29 / 10}$ 。 \(\square\)

该命题把可靠的尺度推导与更深的第二内端消项分开，便于独立审查；两个有限阶局部方程可解并不证明完整全局 Einstein 方程可解。

\section*{2.6 常标量修正：权重端点与可用的局部替代}

\section*{2．6．1 三种尺度的加权逆}

在前述构造上令 $w_{a}$ 为光滑尺度函数：核上 $w_{a} \asymp a(1+\rho)$ ，中间圈与物理半径可比，远处为固定正量。记 $C_{\mu}^{k, \alpha}$ 为局部尺度不变 Hölder 范数再乘 $w_{a}^{-\mu}$ 的加权空间。每块核固定一点 $p_{i}$ 与固定物理半径截断 $\zeta_{i}$ ，设
$$\|v\|_{X_{a, \mu}}=\sum_{i}\left|v\left(p_{i}\right)\right|+\left\|v-\sum_{i} v\left(p_{i}\right) \zeta_{i}\right\|_{C_{\mu}^{2, \alpha}}, \quad Y_{a, \mu}=C_{\mu-2}^{0, \alpha}, \quad 0<\mu<2 .$$
若外轨形标量算子 $P_{\sigma, 0}=-6 \Delta-8 \sigma$ 在所选函数空间无核，则
$$\|v\|_{X_{a, \mu}} \leq C_{\mu}\left\|P_{\sigma, a} v\right\|_{Y_{a, \mu}} .$$
反证法按最大值所在尺度分为固定外域、ALE 核、平坦商锥三种极限。前者由外部无核排除；后两者先减去每核一个点值常数，再用次二次调和函数 Liouville 性质排除。ALE 证明可直接用 $\Delta_{e} H=O\left(\rho^{\mu-6}\right)$ 的 Newton 势减去 $O\left(\rho^{-2}\right)$ 尾，得到整个欧氏空间上的次二次 affine 函数；群无不变线性方向排除一次项，完整 ALE 最大值原理排除衰减余项。每个固定 $a$ 的 Fredholm 指数为零，故该单射估计给真正的逆。

\footnotetext{
${ }^{7}$ O．Biquard，Désingularisation de métriques d＇Einstein II，第 3 节，https：／／arxiv．org／html／1311．0956v1； T．Ozuch，Higher order obstructions to the desingularization of Einstein metrics，https：／／arxiv．org／html／2 012．13316v3。
}

负分支的外算子 $-6 \Delta+8$ 自动无核。正 $A_{1}$ 情形的可能核经 Bochner 等号刚性仅出现在圆球及足球商：含奇点时为 $S^{4} / \mathbb{Z}_{2}$ ，核由高度函数给出。选交换两极并使整个构造不变的对合，将标量方程限制在偶函数空间，核即消失。一般循环球面悬挂的同一反射处理也成立；这里没有给任意正 ALE 轨形免费消核。

令 $f_{a}=s\left(g_{a}\right)-4 \sigma$ ，四维共形公式使
$$u=1+v, \quad P_{\sigma, a} v=-f_{a}(1+v)+12 \sigma v^{2}+4 \sigma v^{3}$$
等价于 $s\left(u^{2} g_{a}\right)=4 \sigma$ 。旧对数方案有 $\left|\nabla^{j} f_{a}\right| \leq C_{j} w_{a}^{2-j}$ 、支撑半径 $R=a^{1 / 4}$ ；这是因为（2．4）的主项无迹。于是
$$\left\|f_{a}\right\|_{Y_{a, \mu}} \leq C R^{4-\mu}, \quad\left\|\nabla^{2} v\right\|_{\infty} \leq C a^{\mu-2} R^{4-\mu} .$$
取 $4 / 3<\mu<2$ 得 Hessian 小量，收缩映射和 Ricci 共形公式遂保留 $\delta_{\sigma}\left(u^{2} g_{a}\right)=$ $O\left(|\log a|^{-1}\right)$ ，而标量曲率精确恒定。新完整核方案应改用
$$\left\|f_{a}\right\|_{Y_{a, \mu}} \leq C_{\mu}\left(R^{4-\mu}+a^{4} b^{-\mu-2}+a^{4} R^{-\mu-4}\right) .$$
取 $b=a^{\gamma}, R=a^{\kappa}$ 时，Hessian 趋零的一组充分条件是
$$\frac{2-\mu}{4-\mu}<\kappa<\frac{\mu+2}{\mu+4}, \quad \kappa<\gamma<1 .$$
旧尺度最终指数不能未经重算搬到新尺度。

\section*{2．6．2 为什么 $\mu=2$ 的全局估计确实失败}

EH 上 $H=\rho^{2} \cos \theta$ 是光滑非恒定调和函数。将 $a^{2}(H-H(p))$ 在对数环带截断至零，得到 $v_{a}$ ：
$$\left\|v_{a}\right\|_{X_{a, 2}} \geq c>0, \quad\left\|P_{\sigma, a} v_{a}\right\|_{C_{0}^{0, \alpha}} \leq C\left(R^{2}+L^{-1}\right) \rightarrow 0 .$$
这是实际近核，排除了直接把（2．7）改成 $\mu=2$ 。它不排除特殊源或局部齐次解的无损失 Hessian 估计。

引理2．3（EH 上可扰动的局部 Hessian 端点）。设 $k$ 为固定 EH 度量，$h$ 满足 $\left|\nabla_{k}^{j} h\right| \leq$ $C_{j} \rho^{2-j} 、 0 \leq j \leq 3$ ；记 $k_{\varepsilon}=k+\varepsilon h$ 。若 $R \geq 16 、 \varepsilon R^{2}$ 足够小，且 $\Delta_{k_{\varepsilon}} u=\frac{4}{3} \varepsilon u$ 于 $D_{R}=\{\rho<R\}$ ，则
$$\sup _{D_{R / 2}}\left|\nabla_{k_{\varepsilon}}^{2} u\right| \leq C R^{-2}\|u\|_{L^{\infty}\left(D_{R}\right)} .$$
常数允许依赖固定 $h$ 的尺度范数；不要求 $h$ 具有对称性。
关键证明。EH 的标量球谐次数为偶数 $l$ ，Hopf 权为 $m$ ；正则径向解满足
$$\left(p F^{\prime}\right)^{\prime}-q F=0, \quad p=\rho^{3}\left(1-\rho^{-4}\right), \quad q=l(l+2) \rho+4 m^{2} \rho\left(\left(1-\rho^{-4}\right)^{-1}-1\right) .$$
对 $l \geq 2$ 取 $z=\rho^{l}$ ，相同算子作用于 $z$ 非正，Wronskian $p\left(z F^{\prime}-z^{\prime} F\right)$ 从bolt处的零值单调增加，故
$$\frac{F_{l, m}(\rho)}{F_{l, m}(R)} \leq(\rho / R)^{l} \leq(\rho / R)^{2} .$$

先对全部角模作 $L^{2}$ 正交估计，再用比例环带 Schauder，可得精确 EH 上的 Hessian界，常数不随角频变化。 ${ }^{8}$

对 Poisson 源，常数项由 $\Delta_{k} \rho^{2}=8$ 精确求解；尺度幅度为 $A \rho^{p} 、 p>0$ 的其余源按dyadic 圈分割。每圈零边界解先由径向障板得 $\left\|v_{t}\right\|_{\infty} \leq C t^{2}\left\|F_{t}\right\|_{\infty}$ ，再由刚才的全角模估计控制圈内侧 Hessian。几何级数给 $Q_{T}(v) \leq C_{p}\left(\left|F_{0}\right|+A T^{p}\right)$ ，其中 $Q_{T}$ 为 Hessian及尺度 Hölder 范数。

固定 EH 核上梯度可由 Hessian 控制，否则会产生非零平行一形式，并使 Ricci－flat 四维开集局部平坦，与 EH 非平坦矛盾。沿径向路径积分后，$|d u| \leq C \rho Q_{T}(u)$ 、$|u-u(p)| \leq C \rho^{2} Q_{T}(u)$ 。扰动差算子源因此为 $O\left(\varepsilon \rho^{2} Q_{T}(u)\right)$ 。势项 $\varepsilon u$ 必须拆成常数点值和同阶余项，应用上面的 $p=2$ Poisson 界得到
$$Q_{T}(u) \leq C T^{-2}\|u\|_{\infty}+C \varepsilon\|u\|_{\infty}+C \varepsilon T^{2} Q_{T}(u) .$$
吸收最后一项完成证明。边界 $C^{2, \alpha}$ 先由更大比例环带取得，未把内部估计误作边界估计。 \(\square\)

\section*{2．6．3 负常标量修正保留实际幂次}

对固定 Wahl 填入，若标量源具有尺度幅度 $w^{p} 、 p>0$ ，支撑半径为 $b$ ，正算子热半群与一致 Sobolev 界给
$$\|u-1\|_{\infty}=O\left(b^{p+2}\right), \quad\|u-1\|_{1}=O\left(b^{p+4}\right) .$$
证明将 $\int_{0}^{\infty} e^{-t(-6 \Delta+8)} f d t$ 在 $t=b^{2}$ ， 1 分割，使用短时 $L^{\infty}$ 收缩、 $L^{1} \rightarrow L^{\infty}$ 的 $t^{-2}$界及长时指数衰减，再吸收已存在小解的非线性项。引理2．3与逐圈源分解进一步给$\left\|\nabla^{2}(u-1)\right\|_{\infty}=O\left(b^{p}\right)$ 。因此二次匹配 $p=2, b=a^{1 / 2}$ 在精确 $s=-4$ 后仍保留 $O(a)$的 Ricci 误差；四次匹配 $p=4, b=a^{2 / 5}$ 保留 $O\left(a^{8 / 5}\right)$ 。这取代了早期加权估计所得的$O\left(a^{7 / 8}\right)$ 较弱结果。

命题2．4（常标量体积变分的抵消）。设上述平滑标记的负常标量修正族 $\widehat{g}_{a}=u_{a}^{2} g_{a}$ 满足
$$\left\|E_{\widehat{g}_{a}}\right\|_{2}=O\left(a^{p}\right), \quad\left\|\partial_{a} g_{a}\right\|_{2}=O\left(a^{q}\right), \quad p+q>-1,$$
且体积有极限 $V_{0}$ 。则
$$\left|\operatorname{Vol}\left(\widehat{g}_{a}\right)-V_{0}\right|=O\left(a^{p+q+1}\right) .$$
证明．由 $s_{\widehat{g}_{a}} \equiv-4$ 的一阶变分，
$$V^{\prime}(a)=\frac{1}{2} \int\left\langle E_{\widehat{g}_{a}}, \partial_{a} \widehat{g}_{a}\right\rangle d V$$
$\partial_{a} \widehat{g}_{a}=2 u_{a}\left(\partial_{a} u_{a}\right) g_{a}+u_{a}^{2} \partial_{a} g_{a}$ 中第一项纯迹，与 $E$ 点态正交，故无须估计 $\partial_{a} u_{a}$ 。应用Cauchy－Schwarz 后积分即得。标记的 Lie 导数也与散度为零的 $E$ 积分正交。 \(\square\)

\footnotetext{
${ }^{8}$ A．Malmendier，The eigenvalue equation on the Eguchi－Hanson space，第2节的分离变量方程，https： ／／arxiv．org／pdf／math／0210081。
}

具体匹配族的 $\left\|\partial_{a} g_{a}\right\|_{2}=O(a)$ 来自固定核相对速度 $O\left(a^{-1}\right)$ 与体积 $O\left(a^{4}\right)$ ，以及尾项的逐阶参数链式求导；不能对一个未给参数控制的 $O(\cdot)$ 直接求导。二次匹配给$\|E\|_{2}=O\left(a^{2}\right)$ ，四次匹配给 $O\left(a^{12 / 5}\right)$ ，故分别有
$$0<\operatorname{Vol}\left(\widehat{g}_{a}\right)-2 \pi^{2} \leq C a^{4}, \quad 0<\operatorname{Vol}\left(\widehat{g}_{a}\right)-2 \pi^{2} \leq C a^{22 / 5} .$$
严格正号另用指定 $N$ 的 SW 等号刚性与非复性，后章给其拓扑输入。体积速率只依赖$L^{2}$ 论证，不依赖点态 Hessian 端点，二者证明依赖应分开。

\section*{2.7 对数阶为何不能任意改进：无规范的通量}

命题2．5（允许任意角向变化的线性通量）。令 $n \geq 4, \Gamma \subset O(n)$ 在球面自由作用， $A=\{b<r<R\} / \Gamma 、 L=\log (R / b)$ 。设非零二次齐次 $\Gamma$－不变张量 $K$ 满足 $\operatorname{tr} K=$ $\operatorname{div} K=\Delta K=0 、 K(x, \cdot)=0$ ，并置
$$o=r^{-n-2} K, \quad I_{K}=\int_{S^{n-1} / \Gamma}|K|_{\mathrm{HS}}^{2}, \quad J_{K}=\int_{S^{n-1} / \Gamma}\|K\|_{*} .$$
若光滑张量 $u$ 在内外边界邻域分别等于 $0, K$ ，则
$$\int_{A}\left\langle D \operatorname{Ric}_{e} u, o\right\rangle=-\frac{n+2}{2} I_{K}, \quad\left\|D \operatorname{Ric}_{e} u\right\|_{\mathrm{op}, \infty} \geq \frac{(n+2) I_{K}}{2 L J_{K}} .$$
证明。 $o$ 无迹、无散度、调和且 $o(\nu, \cdot)=0$ ，所以真实 Ricci 线性化中的全部规范项经分部积分消失。Green 边界配对只留下外边界，$\partial_{r} K=2 K / r 、 \partial_{r} o=-n o / r$ ，给常数。另一方面 $\int_{A}\|o\|_{*}=L J_{K}$ ，算子范数与核范数对偶即得下界。 \(\square\)

非线性推广无需内部 $D^{2} q$ 界。若 $g=e+q 、|q| \leq B r^{2},|D q| \leq B r, B R^{2} \leq 1 / 2$ ，端点为 $e+H_{1}, e+H_{0} 、 K=H_{0}-H_{1} 、 D \operatorname{Ric}_{e} H_{i}=\sigma e$ ，则
$$\delta_{\sigma}(g) \geq \frac{(n+2) I_{K} / 2-C_{K}\left(B^{2}+B\right) R^{2}}{J_{K}\left(L+C B R^{2}\right)} .$$
因为精确余项的最高阶部分为 $A(q) * D^{2} q$ ，对其与 $o$ 的配对只需积分分部一次；体积和边界余项均为 $O\left(\left(B^{2}+B\right) R^{2}\right)$ 。端点允许一阶相对误差 $\epsilon_{ \pm}$，分子另减 $C_{K}\left(\epsilon_{-}+\epsilon_{+}\right)$。

更弱的内部条件是固定小 $C^{0}$ 界与 $\mathcal{E}(q)=\int_{A} r^{-n}|D q|^{2}$ 。加权 Hardy 估计
$$\int_{A} r^{-n-2}|q|^{2} \leq 2 \mathcal{E}+C b^{2}, \quad \int_{A} r^{-n}|q| \leq C R(\sqrt{\mathcal{E}}+b)$$
给
$$\delta_{\sigma}(g) \geq \frac{(n+2) I_{K} / 2-C\left(\epsilon+\mathcal{E}+R \sqrt{\mathcal{E}}+R^{2}\right)}{J_{K} L+C R(\sqrt{\mathcal{E}}+R)} .$$
所以 $\mathcal{E} \rightarrow 0 、 R, \epsilon \rightarrow 0$ 时，同一首项仍成立。
若中间坐标确为 $g$－调和坐标，且 $|q| \leq A r^{1+\alpha} 、 \alpha>0$ ，端圈保留固定二次一阶模型，则 Caccioppoli 给
$$\mathcal{E} \leq C R^{2}+C_{\alpha}\left(A^{2} R^{2 \alpha}+A R^{1+\alpha}\right) \rightarrow 0 .$$

临界 $\alpha=0$ 时多出 $A^{2} L$ ，不能无代价取端点。规范条件也不能删：对支撑在 $s<r<2 s$的小球，取
$$\Phi_{s}(x)=x+s^{9 / 4} \chi(x / s) \sin \left(s^{-5 / 4} x_{1}\right) e_{1} .$$
它在端点恒等且 $D \Phi_{s}-I=O(s)$ 。对一个标准近 Einstein 插值作拉回后，Ricci 最大误差不变，$C^{0}, W^{1,4}, W^{2,2}$ 的坐标扰动均趋零，但 $\mathcal{E}\left(\Phi_{s}^{*} g-e\right) \geq c s^{-1 / 2} \rightarrow \infty$ 。该例改变的是坐标，精确揭示无权小范数不能替代所需加权规范控制；它没有改变度量几何或突破通量下界。

\section*{2．7．1 球面模型的锐系数与常标量代价}

球面外项和（2．3）的内项之差满足
$$Q:=K / r^{2}, \quad \operatorname{spec}(Q)=(0,-\sigma / 18, \sigma / 36, \sigma / 36) .$$
若 $v_{\Gamma}=\operatorname{Vol}\left(S^{3} / \Gamma\right)$ ，则 $I_{K}=v_{\Gamma} / 216, J_{K}=v_{\Gamma} / 9$ 。因此无标量约束的首项是 $1 /(8 L)$ 。它可由
$$q=H_{1}+\eta K+\frac{\sigma}{144} \eta^{\prime} r^{2} e, \quad t=\log (r / b),$$
达到：主残差矩阵 $-3 Q-\sigma e / 24$ 的算子范数恰为 $1 / 8$ ，选择长度 $\sqrt{L}$ 的两端缓变平台使 $\eta^{\prime}=L^{-1}+O\left(L^{-3 / 2}\right)$ 。

若标量曲率精确为 $4 \sigma$ ，残差 $T=\operatorname{Ric}-\sigma g$ 精确无迹、无散度。取 $\varphi=r^{-2}$ ，利用
$$r^{-4}\left(e-4 P_{r}\right)=-\frac{1}{2} \operatorname{Hess}_{e}\left(r^{-2}\right), \quad Q-\frac{\sigma}{144}\left(e-4 P_{r}\right)-\frac{\sigma}{48} e=-\frac{\sigma}{12} P_{J}$$
消去迹与 Hessian 测试项，得到更强的
$$\liminf L \delta_{\sigma}(g) \geq \frac{1}{6}$$
纯 Weyl 插值达到此首项。非线性及一阶端点误差的稳健版本分母为 $v_{\Gamma} L / 12+O(1+$ $B R^{2}$ ），分子为 $v_{\Gamma} / 72-O\left(\epsilon_{-}+\epsilon_{+}+\left(B^{2}+B\right) R^{2}\right)$ 。以 EH 而非欧氏度量作背景时，仅新增 $O\left((a / b)^{4}\right)$ 误差。改变内端其余 Weyl 分量而保持 $\mathcal{R}_{\mathrm{in},+} \xi=0$ ，不会消去该测试通量：球面矩阵平均保证与固定 $K$ 的配对仍为 $I_{K}$ 。

在 $U(2)$ 与两极反射不变的足球双消解中，径向公式
$$v^{\prime}(t)=J_{a}(t)^{-1} \int_{0}^{t} J_{a}(s) \Delta v(s) d s$$
直接给无最小尺度损失的 Hessian 界。取 $T_{a}=|\log a|, b=a T_{a}, R=T_{a}^{-1}$ ，则 $L / T_{a} \rightarrow 1$ 、标量源为 $O\left(T_{a}^{-2}\right)$ 。常标量小解的 Hessian 亦为 $O\left(T_{a}^{-2}\right)$ ，从而该明确模型满足
$$s_{\widehat{g}_{a}}=4, \quad|\log a| \delta_{+}\left(\widehat{g}_{a}\right) \longrightarrow \frac{1}{6} .$$
无常标量约束的对应构造则为1／8。这两个常数衡量指定退化方案的效率；误差本身趋零，绝非原题的普遍正间隙。一般无核 $A_{1}$ 情形还可通过固定权重和固定幂次族的对角选择达到 $1 / 6$ ，不需要令端点逆的常数一致。

\section*{2.8 临界导数能量：三阶可小，四阶不自动小}

对旧纯 Weyl 对数构造，残差 $T_{a}=\operatorname{Ric}\left(g_{a}\right)-\sigma g_{a}$ 满足
$$\left\|\nabla^{k} T_{a}\right\|_{L^{4 / k}} \leq C_{k}\left(L^{k / 4-1}+a+R^{2}\right) \rightarrow 0, \quad k=1,2,3 .$$
关键积分为 $\int L^{-4 / k} r^{-4} r^{3} d r$ ，其 $k / 4$ 次幂恰为 $L^{k / 4-1}$ ；核与普通截断部分按物理尺度计算。于是完整 $W^{1,4}, W^{2,2}, W^{3,4 / 3}$ 范数均趋零，仍无 Ricci 导数最大范数控制。

若至少一处 $K \neq 0$ ，固定截断 $\psi$ 下四阶有精确下界
$$\int_{\log \text { annulus }}\left|\nabla^{4} T_{a}\right| d V \longrightarrow 3\left(\int_{0}^{1}\left|\psi^{\prime}\right|\right) \int_{S^{3} /\{ \pm 1\}}\left|D^{4}\left(K / r^{2}\right)\right|_{r=1} d \omega>0$$
所有导数落在截断系数上的额外项多出 $L^{-1}$ ，非线性与连接差积分为 $o(1)$ 。若角张量的四阶导数为零，则其零次齐次分量为常数，正规条件 $K(x, \cdot)=0$ 又迫使 $K=0$ ，矛盾。合适 $4 / 3<\mu<2$ 的常标量修正不会消除该下界。该结论针对所分析的构造，并非所有近 Einstein 序列的四阶障碍。

\section*{2.9 标准光滑模型：几何构造与拓扑识别须分别证明}

命题2．6（球面悬挂消解的标准光滑类型）。令 $r \geq 1 、 p=r+1, \Gamma=\mathbb{Z}_{p} \subset S U(2)$ 作用为 $\left(z_{1}, z_{2}\right) \mapsto\left(\zeta z_{1}, \zeta^{-1} z_{2}\right)$ 。它在 $S^{4} \subset \mathbb{R} \oplus \mathbb{C}^{2}$ 上的商只有两个 $A_{r}$ 点。在南北两极采用反射 $(t, z) \mapsto(-t, z)$ 兼容的标准 ALE 标记，所得光滑流形为
$$M_{r} \cong \# r\left(S^{2} \times S^{2}\right) .$$
以本章 ADE 延拓及反射不变的标量修正为输人，构造稿给出
$$\begin{aligned}
& \operatorname{Ric}_{g_{r, a}}-g_{r, a} \longrightarrow 0 \quad \text { 于最大算子范数, } \quad s_{g_{r, a}}=4, \\
& \left(M_{r}, g_{r, a}\right) \longrightarrow S^{4} / \mathbb{Z}_{r+1}, \quad \operatorname{Vol}\left(M_{r}, g_{r, a}\right) \longrightarrow \frac{24 \pi^{2}}{r+1} .
\end{aligned}$$
几何断言继承前述构造稿的待独立审查状态；拓扑识别不依赖该分析构造。
证明。设 $W$ 是 framing 全为 -2 的 $A_{r}$ 链 plumbing。去掉两个锥邻域后的外部是$\left(S^{3} / \Gamma\right) \times I$ 。反射在截面标记中为恒等，故消解是标准双倍 $D(W)=W \cup_{\text {id }}(-W)$ ，没有任意 lens space 粘接映射。 $W$ 单连通、spin，$D(W)$ 是 $W \times I$ 的光滑化边界，因而也单连通、spin，且 $b_{2}(D(W))=2 r 、 \tau(D(W))=0$ 。标准 toric 作用沿恒等边界粘接延拓。Orlik－Raymond 的光滑环面作用分类遂给上述微分同胚；仅用交叉形式分类不足以得到此结论。 ${ }^{9}$ 几何结论由两个兼容 ALE 核和偶反射标量逆得到；归一化 Ric $=g$的圆球体积为 $24 \pi^{2}$ 。 \(\square\)

\footnotetext{
${ }^{9}$ P．Orlik，F．Raymond，Actions of the torus on 4－manifolds．I，https：／／webhomes．maths．ed．ac．uk／～v1ran ick／papers／orlikraymond1．pdf，§5。
}

每个固定 $r$ 的常数可以依赖 $r$ 。对角选择 $r_{j} \rightarrow \infty$ 、再取足够小的 $a_{j}$ ，仍可令
$$\delta_{+}\left(g_{r_{j}, a_{j}}\right) \leq j^{-1}, \quad b_{2}\left(M_{r_{j}}\right) \rightarrow \infty, \quad \operatorname{Vol}\left(g_{r_{j}, a_{j}}\right) \rightarrow 0 .$$
Myers 定理同时给统一直径上界。这一条件性后果说明，纯正 Ricci 近似条件不能在这条构造成立时再提供统一体积下界或 $b_{2}$ 上界；它并未排除这些流形上的其他 Einstein度量。

另一个固定输入是 $\mathcal{O}=\left(S^{2} \times S^{2}\right) /\left\langle\left(r_{\pi}, r_{\pi}\right)\right\rangle$ ，其中每个球面的曲率为 $1, r_{\pi}$ 是旋转 $\pi$ 。它有四个 $A_{1}$ 点，体积 $8 \pi^{2}$ 。有效环面格为
$$L=\mathbb{Z}^{2}+\mathbb{Z}(1 / 2,1 / 2), \quad u=(1,0), v=(0,1), p=(1 / 2,1 / 2), m=(1 / 2,-1 / 2) .$$
每个角的负、正 EH 填入分别插入特征直线 $(a+b) / 2 、(a-b) / 2$ ，相邻格行列式绝对值均为1，所以两种方向均允许标准环面作用延拓。全负方向的新直线依次为 $p, m, p, m$ ；翻转一个核交换该处 $p, m$ 。对八边形 quasitoric 流形，$w_{2}=0$ 当且仅当存在 $\ell: L \rightarrow \mathbb{F}_{2}$ ，对所有特征向量取值1。由于 $m=u-p$ ，这等价于新直线全为 $p$ 或全为 $m$ ，即恰在两个相对角翻转。这是 Davis－Januszkiewicz 上同调公式的直接应用。 ${ }^{10}$ 令 $k$ 为正 EH核数；$\chi=8 、 \tau=2 k-4$ ，结合光滑环面分类得到

\begin{tabular}[t]{|l|l|}
\hline 选择 & 有向微分同胚类型 \\
\hline $k=0$ & $\mathbb{C P}^{2} \# 5 \overline{\mathbb{C P}}^{2}$ \\
\hline $k=1$ & $2 \mathbb{C} \mathbb{P}^{2} \# 4 \overline{\mathbb{C P}}^{2}$ \\
\hline $k=2$ ，相邻 & $3 \mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$ \\
\hline $k=2$ ，相对 & $\# 3\left(S^{2} \times S^{2}\right)$ \\
\hline $k=3$ & $4 \mathbb{C P}^{2} \# 2 \overline{\mathbb{C P}}^{2}$ \\
\hline $k=4$ & $5 \mathbb{C P}^{2} \# \overline{\mathbb{C P}}^{2}$ ． \\
\hline
\end{tabular}
在给定定向分支内标准正交粘接相差 $S O(4)$ 中的路径，边界同痕延拓到领圈，故不会改变这些光滑类型。这不涉及任意抽象边界微分同胚。上述模型继承 $A_{1}$ 构造稿的近Einstein 结论，但没有相应的全局 Einstein 不存在性证书。

还可对来源作一项独立筛选。若正 Kähler－Einstein 轨形只有 $N$ 个 $A_{1}$ 点，最小复消解为 $\mathbb{C P}^{2} \# m \overline{\mathbb{C P}}^{2} 、 0 \leq m \leq 8$ ，则
$$c_{1}^{2}=9-m, \quad c_{2}^{\mathrm{orb}}=m+3-\frac{3}{2} N, \quad 3 c_{2}^{\mathrm{orb}}-c_{1}^{2}=\frac{3}{8 \pi^{2}} \int\left|W^{-}\right|^{2} \geq 0 .$$
因此 $N \leq 8 m / 9 \leq m-1$（存在奇点时）。任意翻转 $k \leq N$ 个核后仍有 $b^{-}=m-k \geq 1$ ，所以这个来源不能产生正定交叉形式的新模型。若最小消解为 $S^{2} \times S^{2}$ ，同式给 $N=0$ 。这是 Chern－Weil 公式的推论，范围限于这里明确假设的正 KE 来源。

\subsection*{2.10 某条修正路线无解，与流形无解是不同结论}

命题2．7（保留球面开集的共形修正不可能 Einstein 化）。设 $M^{4}$ 闭、连通、单连通，$b_{2}(M)>0$ ，而 $g$ 在某个非空开集 $U$ 上局部共形平坦。则不存在全局 Einstein 度量 $h$ ，使 $\left.h\right|_{U}$ 与 $\left.g\right|_{U}$ 共形。特别地，$[g]$ 不含任何符号的 Einstein 度量。

\footnotetext{
${ }^{10}$ M．Davis，T．Januszkiewicz，Convex polytopes，Coxeter orbifolds and torus actions，https：／／people．math．osu．edu／davis．12／old＿papers／DJ＿toric．dmj．pdf，Corollary 3．9、Theorem 4．14、Corollary 6．8。
}

证明。共形不变性给 $\left.W_{h}\right|_{U}=0$ 。Einstein 度量的调和坐标实解析性使 $W_{h} \equiv 0$ ，故 $h$ 是常截面曲率度量；闭且单连通迫使其为圆球，与 $b_{2}>0$ 矛盾。 ${ }^{11}$ \(\square\)

球面悬挂构造保留一个圆球开集，任意后续共形常标量修正不改变此排除。 $r=1$时底层 $S^{2} \times S^{2}$ 明明承载乘积 Einstein 度量，说明不能把共形类内无解升级为所有度量无解。

Huang－Ozuch 的固定 Ricci 常数四维球面／双曲轨形 GH 隔离定理还给另一种局部排除。 ${ }^{12}$ 对每个固定 $p \geq 2$ ，存在 $\eta_{p}>0$ ，使任意光滑 $\operatorname{Ric}_{h}=h$ 的四维流形 $(N, h)$满足 $d_{G H}\left((N, h), S^{4} / \mathbb{Z}_{p}\right) \geq \eta_{p}$ 。因此对上述趋于该轨形的构造，当 $a$ 足够小时，
$$\inf _{(N, h): \operatorname{Ric}_{h}=h} d_{G H}\left(\left(M_{p-1}, g_{a}\right),(N, h)\right) \geq \eta_{p} / 2 .$$
若 $e^{-t} g_{a} \leq \phi^{*} h \leq e^{t} g_{a}$ 且 $\operatorname{diam}\left(g_{a}\right) \leq D$ ，恒等对应关系给 $d_{G H} \leq \frac{1}{2}\left(e^{t / 2}-1\right) D$ ，于是
$$t \geq 2 \log \left(1+\eta_{p} / D\right) .$$
常数依赖固定轨形；这一结论固定归一化正 Einstein 常数，并不排除远处或其他尺度的 Einstein 度量。

命题2．8（近正 Einstein 度量的 Yamabe 两侧估计）。对闭连通四维 $g$ ，若 $\delta_{+}(g) \leq \delta<1$ ，$V=\operatorname{Vol}(g)$ ，则
$$4(1-\delta) \sqrt{V} \leq Y(M,[g]) \leq 4(1+\delta) \sqrt{V} .$$
若 $s_{g}=4$ ，右端可换为 $4 \sqrt{V}$ 。
证明．以 $d \nu=d V / V$ 归一化，Ricci 下界 Ric $\geq \kappa g 、 \kappa=1-\delta$ ，给
$$\|u\|_{4, \nu}^{2} \leq\|u\|_{2, \nu}^{2}+\frac{3}{2 \kappa}\|\nabla u\|_{2, \nu}^{2} .$$
这是 Ilias 的锐 Sobolev 不等式；系数 $3 /(2 \kappa)$ 对本归一化至关重要。 ${ }^{13}$ 用 $s \geq 4 \kappa$ 代人Yamabe 商的分子 $\int\left(6|\nabla u|^{2}+s u^{2}\right)$ ，得到下界；常数函数给上界。 \(\square\)

对 $M_{r}$ 构造的条件性应用为
$$Y\left(M_{r},\left[g_{r, a}\right]\right) \longrightarrow 8 \pi \sqrt{\frac{6}{r+1}} .$$
另一方面，乘积 $S^{2} \times S^{2}$ 的 Yamabe 常数为 $16 \pi$ ，正 Yamabe 连通和不等式给全局不变量 $Y\left(M_{r}\right) \geq 16 \pi 。{ }^{14}$ 故这些共形类与全局变分上确界的比值至多趋于 $\sqrt{3 /(2(r+1))}$ ，并可对角趋零。这提供变分分离，而非 Einstein 不存在性。

\footnotetext{
${ }^{11}$ D．DeTurck，J．Kazdan，Some regularity theorems in Riemannian geometry，Theorem 5．2，https：／／www．nu mdam．org／article／ASENS＿1981＿4＿14＿3＿249＿0．pdf。
${ }^{12}$ Y．Huang，T．Ozuch，Regularity of Einstein 5－manifolds via 4－dimensional gap theorems，Theorem 1．1， https：／／arxiv．org／html／2512．21317v2。
${ }^{13}$ S．Ilias，https：／／www．numdam．org／item／10．5802／aif．921．pdf；另一完整证明见 L．Dupaigne，I．Gentil，S． Zugmeyer，Sobolev＇s inequality under a curvature－dimension condition，Theorem A，https：／／afst．centre－m ersenne．org／item／10．5802／afst．1731．pdf。
${ }^{14} \mathrm{O}$ ．Kobayashi，Scalar curvature of a metric with unit volume，https：／／doi．org／10．1007／BF01461722；相关手术不等式的证明与归一化见 B．Ammann，M．Dahl，E．Humbert，Smooth Yamabe invariant and surgery， https：／／ammann．app．uni－regensburg．de／preprints／sigmaana／sigmaana．pdf。
}

\subsection*{2.11 负分支候选：必须辨认光滑结构与边界 spin 数据}

取超椭圆曲线 $C_{g}, C_{h}, g, h \geq 2$ ，并令 $\mathcal{O}_{g, h}=\left(C_{g} \times C_{h}\right) /\left\langle\iota_{g} \times \iota_{h}\right\rangle$ 。它具有 $4(g+1)(h+1)$个 $A_{1}$ 点和负乘积 Einstein 轨形度量。全部沿复方向作标准－2 消解所得 $M_{0}$ 已经承载负 Einstein 度量。证明可完全给出：在 $B=\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ 上，商为
$$w^{2}=f(x) q(z), \quad w \in L=\mathcal{O}(g+1, h+1) .$$
取一般 $F \in H^{0}\left(B, L^{2}\right)$ ，则 $w^{2}=f q+t F$ 的一般小非零纤维 $X_{t}$ 光滑。节点局部写为$u v-z^{2}=t$ ，令 $t=-s^{2}$ ，并引入
$$u \alpha=(z-s) \beta, \quad(z+s) \alpha=v \beta, \quad[\alpha: \beta] \in \mathbb{C P}^{1} .$$
两张仿射图直接显示总空间光滑、到 $s$ 的投影为 submersion；中心纤维为 -2 消解，非零纤维为原光滑纤维。整体粘合及 Ehresmann 定理给 $M_{0} \cong X_{t}$ 。这是普通二重点同时消解的经典计算。 ${ }^{15}$ 最后 $K_{X_{t}}=\pi^{*} \mathcal{O}(g-1, h-1)$ ample，Aubin－Yau 定理给负 KE。所以原消解复结构上的－2 曲线不能排除另一复结构的 Einstein 度量。

例如 $(g, h)=(2,5)$ 得 $\chi=116 、 \tau=-72$ ，恰与无 Einstein 的六次曲面八次吹起相同；它们甚至同胚，却不微分同胚。前述构造落在承载 Einstein 度量的那个光滑结构上。 ${ }^{16}$ 局部可平滑也不保证整体可平滑；此处整体方程 $w^{2}=f q+t F$ 是不可省的输入。

混合＋2、－2 核还存在真正的边界兼容问题。每个 $\mathbb{R P}^{3}$ 边界有两个 spin 结构；两种定向的偶 disk bundle 各自诱导一个，且二者不同。否则将两核沿同一 spin 结构粘合会得到闭 spin 四维流形而签名为 $\pm 2$ ，违反 Rokhlin 定理。固定外部 $W$ 若有 spin结构，允许改变的边界选择构成仿射子空间
$$\operatorname{im}\left(H^{1}\left(W ; \mathbb{Z}_{2}\right) \longrightarrow H^{1}\left(\partial W ; \mathbb{Z}_{2}\right)\right) .$$
因此逐点翻转不能被当作彼此独立的全局 spin 自由度。
规范理论的适用范围也必须核对。非挠的正自交球面使通常的伴随不等式无法与非零 SW 或相应稳定同伦不变量共存；混合核在两种定向上都出现此类球面，有限覆盖中的每个球面仍逐份提升，故这些标准证书往往同时失效。这里仅指满足各自 $b^{+}$、局部系数及非零不变量假设的具体伴随定理，不能说所有可能的扭曲 monopole 障碍都已被排除。 ${ }^{17}$ 保留下来的方法是：先验证不存在性证书能跨所选核与边界数据，再尝试最大 Ricci 误差构造。

\footnotetext{
${ }^{15} \mathrm{M}$ ．Atiyah，On analytic surfaces with double points，https：／／doi．org／10．1098／rspa．1958．0181；局部同时消解见 M．Reid，https：／／mreid．warwick．ac．uk／surf／more／DuVal．pdf。
${ }^{16} \mathrm{C}$ ．LeBrun，Curvature and smooth topology in dimension four，https：／／emis．de／ft／47117，文中明确比较这两个光滑类型。
${ }^{17}$ 局部系数版本须逐项使用 N．Nakamura， Pin $^{-}(2)$－monopole invariants，Theorem 1．15、Remark 1．17，https：／／arxiv．org／abs／1303．4870。
}

\section*{第三章 局部灵活性的限度与带边界连接障碍}

\section*{3.1 固定宽度的负 Ricci 灵活性不能代替紧夹逼}

Lohkamp 的原始公告确实给出双边夹逼：对每个 $n \geq 3$ ，存在 $a(n)>b(n)>0$ ，使每个 $n$ 维流形承载完备度量，满足 $-a(n) g<\operatorname{Ric}_{g}<-b(n) g 。{ }^{1}$ 其 Hausdorff 稠密性与保留闭集附近数据的延拓性质，也没有把 $a(n) / b(n)$ 变成可趋于1的自由参数。所以准确差别是固定宽度与任意紧宽度，不能误说该理论完全没有双边控制。

若 $m, M$ 是 $-g^{-1} \operatorname{Ric}_{g}$ 的全局最小、最大特征值， $0<m \leq M$ ，则
$$\inf _{c>0} \delta_{-}(c g)=\frac{M-m}{M+m}, \quad c_{\mathrm{opt}}=\frac{M+m}{2} .$$
这来自两个端点误差的最小最大优化，故缩放不改变本质比值 $M / m$ 。在 $S^{1} \times S^{3}$ 上，严格 Hitchin－Thorpe 端点已迫使每个同号负 Ricci 度量满足 $M / m>3$ 。因此任何对所有四维流形适用、使用上述严格双边不等式的普遍常数，必有
$$a(4) / b(4)>3 .$$
同一流形没有任何 Einstein 度量：$\chi=0$ 使 Einstein Gauss－Bonnet 被积函数 $|W|^{2}+ s^{2} / 24$ 恒零，故度量平坦；但其普适覆盖 $\mathbb{R} \times S^{3}$ 并非 $\mathbb{R}^{4}$ 。这否定了在所有闭四维流形上普遍实现任意紧负夹逼的设想，没有排除经过拓扑筛选后的特定流形族。

更细的点态筛选来自共形公式。令 $g_{u}=e^{2 u(t)}\left(d t^{2}+\sum d x_{\alpha}^{2}\right)$ ，假设 $u^{\prime \prime}>0$ 。负 Ricci的相对特征值为
$$\mu_{t}=e^{-2 u}(n-1) u^{\prime \prime}, \quad \mu_{\perp}=e^{-2 u}\left(u^{\prime \prime}+(n-2)\left(u^{\prime}\right)^{2}\right) .$$
设 $\nu=\left(u^{\prime}\right)^{2} / u^{\prime \prime}$ 。即使在每个点允许一个独立正数作最有利的代数幅度归一化，形状缺陷仍恰为
$$d_{\text {shape }}=\frac{(n-2)|1-\nu|}{n+(n-2) \nu} .$$
这里并未把该点态数当作空间依赖的度量缩放；后者会重新改变 Ricci。若 $0 \leq \nu \leq \eta<1$ ，形状缺陷有固定正下界。特别地，平坦界面截断 $u(t)=a e^{-d / t} 、 t>0$ ，满足
$$\nu(t)=\frac{a d}{d-2 t} e^{-d / t} \rightarrow 0, \quad d_{\text {shape }} \rightarrow \frac{n-2}{n} .$$
完整跨界面度量还有 Ric → 0的幅度问题；任意固定缩放后的最大归一化误差至少为1 。反之 $d_{\text {shape }}=0$ 等价于 $u^{\prime \prime}=\left(u^{\prime}\right)^{2}$ ，其非平坦解 $u=-\log \left|t-t_{0}\right|+C$ 就是局部双曲度量，不能从 $u^{\prime}=0$ 的平坦初值平滑启动。

\footnotetext{
${ }^{1}$ J．Lohkamp，Negatively Ricci Curved Manifolds，Theorems 1、3、4，https：／／arxiv．org／pdf／math／9210223；完整论文出版页：https：／／annals．math．princeton．edu／1994／140－3／p04。
}

该形状障碍在一般背景上稳定：若
$$\nabla^{2} f=H v^{b} \otimes v^{b}+R, \quad\left|\operatorname{Ric}_{g_{0}}\right|+|R|+|d f|^{2}=o(H), \quad H>0,$$
则 $-\widetilde{g}^{-1} \operatorname{Ric}_{\widetilde{g}} 、 \widetilde{g}=e^{2 f} g_{0}$ ，除以 $e^{-2 f} H$ 后的谱趋于 $(n-1,1, \ldots, 1)$ 。这是把上述假设代入完整共形 Ricci 公式的结果。它只排除单方向 Hessian 压倒其他项的策略；多个方向同时精确匹配不满足此假设。预设 Ricci 方程 $\operatorname{Ric}_{g}=-h_{0}$ 也不能代替自洽条件：还需控制 $g^{-1}\left(g-h_{0}\right)$ ，把 $h_{0}$ 设为未知 $g$ 则回到了 Einstein 方程。

\section*{3.2 去核、正分支障碍与高频误差}

令 $L_{g}=\frac{1}{2}\left(\nabla^{*} \nabla-2 \stackrel{\circ}{R}\right)$ 为归一化 Einstein 背景的 Bianchi 规范线性化。固定两个亏格至少二的曲面，在 $S$ 上固定双曲度量 $a$ ，在 $T$ 上把一条分离测地线压短得到 $b_{j}$ 。则 $g_{j}=a \oplus b_{j}$ 拓扑、体积固定， $\operatorname{Ric}=-g_{j} 、 \sec \in[-1,0]$ ，且所有正阶曲率导数为零。但 $T$ 上 $\Delta f_{j}=\lambda_{j} f_{j}$ 可取 $\lambda_{j} \downarrow 0$ ：分离领圈中近阶跃函数的能量为 $O\left(\ell_{j}\right)$ ，减均值后的$L^{2}$ 范数有统一正下界。取 $S$ 上非零 TT 核元 $q$ ，便有
$$L_{g_{j}}\left(f_{j} q\right)=\frac{1}{2} \lambda_{j} f_{j} q, \quad f_{j} q \perp \operatorname{ker} L_{g_{j}}, \quad\left\|\left(\left.L_{g_{j}}\right|_{\mathrm{ker}^{p} \text { erp }}\right)^{-1}\right\|_{2 \rightarrow 2} \geq 2 / \lambda_{j} \rightarrow \infty .$$
乘积算子与该谱机制的详细版本见 6．43、6．42 节。其经典依据是双曲曲面形变理论及乘积谱公式。 ${ }^{2}$ 这连去掉整个真实核后的普通统一逆也排除了，但输入本来就是精确Einstein，故不是原题反例。Jäckel 的严格负截面曲率与薄部假设如何进入其特定反演估计，在全局分析章节单独说明。

正分支有另一个必须分开的现象。对 $\mathbb{C P}^{2} \times \mathbb{C P}^{1}$ ，将两个因子都归一化为 Ric $=g$ ，取第一因子上 $\Delta f=2 f$ 的非零函数，则
$$H=\operatorname{Hess} f+f a-f b$$
为非零 TT 核元：总迹为 $-2 f+4 f-2 f=0, \delta \operatorname{Hess} f=d f 、 \delta(f a)=-d f 、 \delta(f b)=0$ ，而 Hessian 交换公式给 $L_{g} H=0$ 。Koiso 的经典例子说明这里所有非零无穷小 Einstein形变均遇到二阶障碍，不能用＂把核当作参数＂自动取得精确解族。 ${ }^{3}$ 本例实维六；没有据此声称四维正分支也存在上述同型非可积核，也没有证明正分支去核后的正谱隙能像负分支一样趋零。

命题3．1（Ricci 最大误差不控制 Ricci 导数）。在任意固定闭 Einstein 背景 $\left(M^{n}, g_{0}\right)$ 、$n \geq 2 、 \operatorname{Ric}_{g_{0}}=\sigma g_{0}$ 上，存在 $\widehat{g}_{k} \rightarrow g_{0}$ 于 $C^{2}$ ，使
$$\delta_{\sigma}\left(\widehat{g}_{k}\right)=O\left(k^{-1 / 2}\right) \rightarrow 0, \quad\left\|\nabla^{\widehat{g}_{k}} \operatorname{Ric}_{\widehat{g}_{k}}\right\|_{\infty} \geq c k^{1 / 2} \rightarrow \infty .$$
证明。在坐标球取紧支撑截断 $\chi$ ，于较小球恒为一，设 $u_{k}=k^{-5 / 2} \chi \cos \left(k x^{1}\right) 、 \widehat{g}_{k}=e^{2 u_{k}} g_{0}$ 。共形 Ricci 公式含 $-(n-2) \nabla^{2} u_{k}-\left(\operatorname{tr} \nabla^{2} u_{k}\right) g_{0}$ 和较低阶项，所以误差为 $O\left(k^{-1 / 2}\right)$ 。在$\chi=1 、 \sin \left(k x^{1}\right)= \pm 1$ 的点，三阶主项是 $k^{1 / 2}$ 乘一个非零张量 $d x^{1} \otimes\left((n-2) d x^{1} \otimes d x^{1}+\right. \left|d x^{1}\right|^{2} g_{0}$ ）；其余项低阶，给导数下界。 \(\square\)

\footnotetext{
${ }^{2}$ L．Andersson，V．Moncrief，Einstein spaces as attractors for the Einstein flow，§§2．5．2、3，https：／／arxiv． org／pdf／0908．0784；该文 Einstein 算子为这里的 $2 L$ 。
${ }^{3}$ S．J．Hall，On the Rigidity of $\mathbb{C P}^{2 n} \times \mathbb{C P}^{1}$ ，Proposition 2.3 及 Koiso 障碍的重证，https：／／arxiv．org／html ／2408．16689v1。
}

这个例子仍有原背景精确解，故只是输入正则性路线的反例。负分支另有 $L^{\infty}$ 与绝对 $L^{2}$ 小量的区别：有限 $d$ 重覆盖保持最大误差，却将固定误差的 $L^{2}$ 范数乘以 $\sqrt{d}$ 。正分支的统一 Bishop 体积上界消除了这一特定问题，不能顺带消除核与高阶障碍。

\section*{3.3 平坦及 Heisenberg 颈：可复核的最大误差下界}

若 $g=d t^{2}+G_{i j}(t) d x^{i} d x^{j}$ ，叶片为内蕴平坦环面，$G(t)$ 可为任意正定矩阵。记$A=\frac{1}{2} G^{-1} G^{\prime} 、 H=\operatorname{tr} A$ 。在内部 $H=0$ 的叶片，Gauss 公式给
$$\delta_{-}(g) \geq \frac{n-2+|A|^{2}}{n} \geq \frac{n-2}{n} .$$
因此允许剪切或非对角矩阵并不能改善此类颈。常数在非紧模型中达到：令 $m=n-1$ 、$\beta=2 \sqrt{m} / n$ ，则
$$g=d t^{2}+a_{0}^{2} \cosh (\beta t)^{n / m} h_{\text {flat }}$$
的径向、切向 Ricci 特征值分别为 $-1-(n-2) \operatorname{sech}^{2}(\beta t) / n 、-1+(n-2) \operatorname{sech}^{2}(\beta t) / n$ 。四维时，若 $\operatorname{Vol}\left(T^{3}, h_{0}\right)=V_{0}$ ，其误差 $\rho$ 满足
$$\int_{\mathbb{R} \times T^{3}} \rho^{2} d V=\frac{a^{3} V_{0}}{\sqrt{3}} \rightarrow 0, \quad \sup \rho=\frac{1}{2}$$
这是积分误差消失而最大误差不消失的精确局部模型。
命题3．2（一般左不变 Heisenberg 颈）。设 $N$ 是三维 Heisenberg 群紧商，固定标架满足 $\left[X_{1}, X_{2}\right]=Z$ 。在紧区间 $I$ 取 $g=d t^{2}+G_{i j}(t) \eta^{i} \eta^{j}$ ，其中 $G(t)>0$ 任意，并定义
$$A=\frac{1}{2} G^{-1} G^{\prime}, \quad H=\operatorname{tr} A, \quad z=Z /|Z|_{G}, \quad c=\frac{G(Z, Z)}{\sqrt{\operatorname{det} G}} .$$
若内部有 $H\left(t_{0}\right)=0$ ，则有如下带边界结论：
$$\begin{array}{c|c}
\text { 两端假设 } & \delta=\delta_{-}(g) \text { 的必要下界 } \\
\hline c^{2} \leq 4 / 3 & \delta \geq 1 / 3 \\
c^{2} \leq 2 / 3 & \delta \geq 1 / 3+\left|A\left(t_{0}\right)\right|^{2} / 5 \\
c^{2} \leq 1 & \delta>4 / 11 .
\end{array}$$
最后的常数未声称最佳，且不能移用于仅有第一行边界假设的情形。
证明．叶片的 Ricci 算子为 $-c^{2} I / 2+c^{2} P_{z}$ 。设 $E=\operatorname{Ric}+g 、 w=\log c 、 k=\langle A z, z\rangle$ 、$q=|A z|^{2}-k^{2} \geq 0$ 。由 $w^{\prime}=2 k-H 、 \nabla_{t} z=A z-k z$ 及切向 Ricci 公式得到
$$w^{\prime \prime}+H w^{\prime}=-1+\frac{3}{2} c^{2}+\operatorname{tr} E_{\tan }-2 E_{z z}+4 q .$$
内部最大值原理给 $\sup c^{2} \leq \max \left\{\sup _{\partial I} c^{2}, 2 / 3+2 \delta\right\}$ ，而在 $t_{0}$ ，Gauss 约束给 $c^{2} \geq 4-8 \delta+2|A|^{2}$ 。合并即得前两行。

第三行保留误差分量之间的关系。完整 Gauss 与法向方程为
$$c^{2}=4-2 \operatorname{tr} E_{\tan }+2 E_{00}-2 H^{2}+2|A|^{2}, \quad H^{\prime}=1-E_{00}-|A|^{2} .$$

代人前式得 $w^{\prime \prime}+H w^{\prime} \geq 1+c^{2}-3 \delta-H^{2}$ 。反设 $\delta \leq 4 / 11$ ，前两估计给
$$c^{2} \leq 46 / 33, \quad c\left(t_{0}\right)^{2} \geq 12 / 11>1, \quad 16 / 33-H^{2} \leq H^{\prime} \leq 15 / 11 .$$
令 $t_{0}=0$ ，必要时反转参数使 $w^{\prime}(0) \geq 0$ ，则 $0 \leq H(t) \leq k t 、 k=15 / 11$ 。只要 $w \geq w(0)$ ，在 $0 \leq t \leq b=2 / 3$ 上有 $w^{\prime \prime}+H w^{\prime} \geq 1-k^{2} t^{2}>0$ ，积分因子闭合该条件。因边界$c^{2} \leq 1$ ，区间不能提前终止。于是
$$w(b)-w(0) \geq \frac{626}{3267} e^{-10 / 33}>\frac{5}{36}>\frac{1}{2} \log (23 / 18),$$
而 $c^{2}$ 的上下界给相反不等式。严格数值可用 $e^{-10 / 33}>8 / 11$ 与 $626 \cdot 8 /(3267 \cdot 11)-5 / 36=$67／143748＞ 0 核验。 \(\square\)

归一化复双曲尖端的 $c^{2}=2 / 3$ ，故其左不变双端连接受这些下界限制。混合 Ricci分量不必为零；证明只使用完整误差在单位向量上的界。一般空间依赖的非齐次颈不在该命题内。

\section*{3.4 一般最小截面没有同样的局部间隙}

任意双侧最小超曲面 $\Sigma^{n-1}$ 只满足
$$R_{\Sigma}+\left|A_{\Sigma}\right|^{2}=R_{M}-2 \operatorname{Ric}(\nu, \nu) \leq-(n-2)+n \delta_{-} .$$
四维 $\delta_{-}<1 / 2$ 要求 $R_{\Sigma}<0$ ，但环面或球面拓扑都不排除处处负标量曲率。下面的精确 Einstein 局部带进一步说明，稳定性也不能补出一般颈部间隙。

在周期为 $2 \pi$ 的 $T^{3}$ 上，取
$$h_{0}=d z^{2}+e^{2 \sin z} d x^{2}+e^{-2 \sin z} d y^{2}, \quad s_{h_{0}}=-2 \cos ^{2} z .$$
在周期 $H^{1}$ 函数上极小化 $\int\left(2\left|u^{\prime}\right|^{2}-\frac{1}{2} \cos ^{2} z u^{2}+u^{6} / 6\right) d z$ 。一维紧嵌入给极小元，小非零常数给负能量，故极小元非零；取绝对值及 ODE 唯一性给正解析解
$$-4 u^{\prime \prime}-\cos ^{2} z u+u^{5}=0, \quad h=u^{4} h_{0}, \quad s_{h}=-2 .$$
解析初值 $(h, A=0)$ 满足 $\operatorname{div} A-d H=0 、 s_{h}+|A|^{2}-H^{2}=-2$ 。Koiso 的解析 Einstein Cauchy 定理因此产生整个紧 $T^{3}$ 上的局部带
$$g=d t^{2}+h_{t}, \quad|t|<\varepsilon, \quad \operatorname{Ric}_{g}=-g, \quad h_{0}^{\prime}=0 .$$
该定理只用于解析初值，不能擅自推广到任意光滑初值。 ${ }^{4}$ 中央环面的第二变分为$\int\left(|\nabla \phi|^{2}+\phi^{2}\right)>0$ 。反射唯一性及 $H^{\prime}=1-|A|^{2}$ 给
$$H=t+O\left(t^{3}\right), \quad d V_{h_{t}} / d V_{h}=1+t^{2} / 2+O\left(t^{4}\right) \geq 1 .$$

\footnotetext{
${ }^{4}$ B．Ammann，A．Moroianu，S．Moroianu，The Cauchy problems for Einstein metrics and parallel spinors， Theorem 2．1、Corollary 2．2，https：／／arxiv．org／pdf／1106．2066。
}

因此投影拉回的闭形式 $\pi^{*} d V_{h}$ 的 comass 至多为一，校准中央环面；它在足够薄的带中同调面积极小且由乘积结构不可压缩。这完全兼容齐次颈下界，因为此中央叶片非平坦。该带没有指定两端外部，也没有任何完备或闭的延拓结论。

对一般全测地三球初值，尚有有用的必要各向异性。写 $g=d t^{2}+h_{t} 、 h_{0}^{\prime}=0$ ，并令 $A_{0}^{\prime}=\alpha I+T 、 \operatorname{tr} T=0$ 。若中央整张三球上 $\delta_{-} \leq \delta<1 / 5$ ，则
$$\sup _{S^{3}}\|T\|_{\mathrm{op}}>\frac{1-5 \delta}{3} .$$
因为 $\alpha \leq(1+\delta) / 3$ ，任意切向正交标架上三维曲率公式给
$$K_{h_{0}}\left(e_{1}, e_{2}\right) \leq \frac{-1+5 \delta}{3}+\|T\|_{\mathrm{op}} .$$
若上述严格下界失败，整张三球非正截面曲率，与 Cartan－Hadamard 定理矛盾。故对任意固定截面度量 $h$ 的 $d t^{2}+f(t)^{2} h$ ，只要 $f^{\prime}$ 有零点，就必有 $\delta_{-}>1 / 5$ ，包括非圆截面及球面空间形式。圆截面更有 $\delta_{-} \geq 1 / 2+3 /\left(2 f^{2}\right)$ 。这些结论要求全测地切片或明确的单一 warped product 形式，不能仅由 $H=0$ 推出。

\section*{3．5 Berger 小核：局部精确可行，指定延拓不可行}

固定 $S U(2)$ 标架 $\left[X_{i}, X_{j}\right]=2 X_{k}$ ，对偶形式记 $\sigma_{i}$ 。Berger 度量 $h_{q}=q \sigma_{1}^{2}+\sigma_{2}^{2}+\sigma_{3}^{2}$的 Ricci 谱为
$$(2 q, 4-2 q, 4-2 q), \quad s_{h_{q}}=8-2 q .$$
取 $q=5 、 A=0$ ，上一节解析定理给 Ric $=-g$ 的局部三球领圈；中央三球严格稳定，$A_{0}^{\prime}=\operatorname{diag}(11,-5,-5)$ 。更一般地，对 $0<a \leq 1$ 令
$$h_{a}=a^{2}\left(\left(4+a^{2}\right) \sigma_{1}^{2}+\sigma_{2}^{2}+\sigma_{3}^{2}\right), \quad s_{h_{a}}=-2 .$$
在放大坐标中求 Einstein 常数 $-a^{2}$ 的齐次 ODE，参数 $a \in[0,1]$ 的初始正定矩阵处于紧集，故有统一存在区间 $|s|<c$ 。缩回 $t=a s$ 后得到
$$\operatorname{Ric}_{G_{a}}=-G_{a}, \quad|t|<c a, \quad \operatorname{diam}=O(a), \quad \operatorname{Vol}_{4}=O\left(a^{4}\right), \quad\|\operatorname{Rm}\|_{\infty}=O\left(a^{-2}\right) .$$
因此＂小核必然产生非零最大 Ricci 误差＂本身不成立；问题在于其端点和完整延拓。
命题3．3（上述小核的显式双轴延拓）。取初值 $u(0)=a \sqrt{4+a^{2}} 、 v(0)=a 、 u^{\prime}(0)=$ $v^{\prime}(0)=0$ ，并要求 $G=d t^{2}+u^{2} \sigma_{1}^{2}+v^{2}\left(\sigma_{2}^{2}+\sigma_{3}^{2}\right)$ 、 $\operatorname{Ric}_{G}=-G$ 。其双轴解在坐标 $-a<r<a$中为
$$\begin{gathered}
G_{a}=\frac{d r^{2}}{F_{a}(r)}+a^{2} F_{a}(r) \sigma_{1}^{2}+\left(a^{2}-r^{2}\right)\left(\sigma_{2}^{2}+\sigma_{3}^{2}\right) \\
F_{a}(r)=\frac{a^{4}+4 a^{2}+\left(2 a^{2}+4\right) r^{2}-r^{4} / 3}{a^{2}-r^{2}}
\end{gathered}$$
两个端点均为有限测地距离的曲率奇点；正向距离 $T_{a}<a / \sqrt{4+a^{2}}<a / 2$ 。

证明。令 $p=u^{\prime} / u 、 q=v^{\prime} / v$ 。完整 Ricci 特征值为
$$\begin{aligned}
R_{00} & =-u^{\prime \prime} / u-2 v^{\prime \prime} / v \\
R_{11} & =2 u^{2} / v^{4}-u^{\prime \prime} / u-2 p q, \\
R_{22}=R_{33} & =4 / v^{2}-2 u^{2} / v^{4}-v^{\prime \prime} / v-p q-q^{2} .
\end{aligned}$$
由 $R_{00}=R_{11}$ 得 $\left(v^{\prime} / u\right)^{\prime}=-u / v^{3}$ ，积分并用初值得 $\left(v^{\prime} / u\right)^{2}=v^{-2}-a^{-2}$ 。令 $v^{2}=a^{2}-r^{2}$ 、 $r^{\prime}=u / a>0 、 F=\left(r^{\prime}\right)^{2}$ ，Gauss 约束化为
$$r\left(a^{2}-r^{2}\right) F^{\prime}-\left(a^{2}+r^{2}\right) F=-\left(a^{2}-r^{2}\right)^{2}-4\left(a^{2}-r^{2}\right) .$$
偶初值消去线性积分常数，得到所写 $F_{a}$ 。令 $w=a^{2}-r^{2} 、 C_{a}=8 a^{2}\left(1+a^{2} / 3\right)$ ，可写 $F_{a}=r^{2} / 3-5 a^{2} / 3-4+C_{a} / w$ 。代人上面三个 Ricci 式可逐项核验 $R_{i i}=-1$ 。 $F_{a}(r)>F_{a}(0)=4+a^{2}$ 给距离界；而
$$K_{01}=-F_{a}^{\prime \prime} / 2=-\frac{1}{3}-\frac{C_{a}\left(a^{2}+3 r^{2}\right)}{\left(a^{2}-r^{2}\right)^{3}} \longrightarrow-\infty .$$
故端点不是坐标奇点，也不能补成光滑 nut 或 bolt。 \(\square\)

该公式属于经典 Taub 家族的代数分支，不能套用通常正定外部分支的填充定理。${ }^{5}$ 沿正向区间 $u^{\prime}>0 、 v^{\prime}<0$ ，轴比不断增大，形算子始终不定。因此这些切片不能直接匹配双曲测地球的圆诱导度量及定号形算子。

同初值的近 Einstein 双轴度量也有定量障碍。若 $\delta_{-}<1+4 / a^{2}$ ，首次离开论证在速度边界给 $u^{\prime \prime} / u \geq 8 / a^{2}+3-\delta>0 、 v^{\prime \prime} / v \leq-4 / a^{2}-1+\delta<0$ ，故 $u^{\prime}>0 、 v^{\prime}<0$ 始终成立。令 $x=v^{\prime} / u<0$ ，完整误差 $R_{i i}=-1+e_{i}$ 给
$$x^{\prime} \leq-\kappa \frac{u}{v^{3}}, \quad \kappa=1-\frac{\delta a^{2}}{4+a^{2}}>0 .$$
把 $v$ 作为变量并注意积分方向，得到 $x^{2} \geq \kappa\left(v^{-2}-a^{-2}\right)$ ，于是 $z=\sqrt{a^{2}-v^{2}}$ 满足$z^{\prime} \geq \sqrt{4+a^{2}-\delta a^{2}}$ 。所以保持正定、双轴形式及误差条件的单侧时间至多为
$$T_{\max } \leq \frac{a}{\sqrt{4+a^{2}-\delta a^{2}}}$$
若要到达圆三球或 $v^{\prime}>0$ 的截面，必有 $\delta_{-} \geq 1+4 / a^{2}$ 。这是指定初值与指定对称类中的结论，不是一般局部手术障碍。

命题3．4（固定标架三轴变化仍不能完成该连接）。对 $0<A \leq 1$ ，取
$$G=d t^{2}+\sum_{i=1}^{3} a_{i}(t)^{2} \sigma_{i}^{2}, \quad\left(a_{1}, a_{2}, a_{3}\right)(0)=\left(A \sqrt{4+A^{2}}, A, A\right), \quad a_{i}^{\prime}(0)=0 .$$
这里同一个固定左不变标架对所有 $t$ 都使度量对角。若正向整个领圈 $0 \leq t<L$ 上$\delta_{-}(G) \leq 1$ ，则
$$a_{1}^{\prime}>0, \quad a_{2}^{\prime}, a_{3}^{\prime}<0, \quad \frac{a_{1}}{a_{2}}, \frac{a_{1}}{a_{3}}>\sqrt{4+A^{2}} \quad(t>0), \quad L<11 A / 5 .$$

\footnotetext{
${ }^{5}$ M．M．Akbar 的 Taub－NUT－AdS 公式，§2，https：／／arxiv．org／pdf／gr－qc／0301007。在其变量中取$\rho=r / 2 、 L=a / 2 、 M=0 、 \Lambda=1$ ，于 $|\rho|<L$ 的负定表达式整体乘－1，得到这里的正定内部分支；本稿以直接方程核验为依据。
}

证明．设 $x_{i}=a_{i}^{\prime} / a_{i} 、 H=\sum x_{i}$ ，截面 Ricci 为
$$r_{i}=\frac{2\left(a_{i}^{4}-\left(a_{j}^{2}-a_{k}^{2}\right)^{2}\right)}{a_{1}^{2} a_{2}^{2} a_{3}^{2}}, \quad x_{i}^{\prime}=r_{i}+1-H x_{i}-e_{i}, \quad H^{\prime}=1-e_{0}-\sum x_{i}^{2} .$$
在区域 $a_{1}^{2} \geq\left(4+A^{2}\right) A^{2} 、 a_{2}^{2}, a_{3}^{2} \leq A^{2}$ 上，$r_{1}>0$ ，且 $-r_{2} \geq\left(4+2 A^{2}\right) / a_{2}^{2} 、-r_{3} \geq$ $\left(4+2 A^{2}\right) / a_{3}^{2}$ 。例如前一式等价于 $X^{2}-q_{0} X Z+Z^{2}-Y^{2} \geq 0$ ，其中 $q_{0}=4+A^{2} 、 X=a_{1}^{2}$ 、 $Y=a_{2}^{2} 、 Z=a_{3}^{2}$ ，而左端至少为 $\left(A^{2}-Z\right)\left(q_{0}^{2} A^{2}-A^{2}-Z\right) \geq 0$ 。速度边界处耦合项 $-H x_{i}$ 恰为零，因此三个速度分别严格指向 $x_{1}>0 、 x_{2}, x_{3}<0$ ，首次离开不可能。

法向方程给 $H^{\prime} \leq 2-H^{2} / 3 、 H(0)=0$ ，故 $H<\sqrt{6}$ 。记 $a=a_{2} 、 v=-a^{\prime} \geq 0$ ，则
$$v^{\prime} \geq \frac{4-v^{2}}{a}-\sqrt{6} v .$$
当 $v \leq 1 / 2$ 时，$a \leq A \leq 1$ 给 $v^{\prime}>5 /(2 A)$ 。所以除非提前终止，$v$ 在时间 $\tau<A / 5$ 达到 $1 / 2$ ，之后不能向下越过该值；再过小于 $2 A$ 就有 $a \leq 0$ ，与正定性矛盾。 \(\square\)

它允许两个短轴不等，但不涵盖随 $t$ 旋转主轴或非齐次截面。双轴子类的形状量$u=\log (b / a) 、 q=e^{2 u}$ 还满足
$$u^{\prime \prime}+H u^{\prime}=4(q-1) / a^{2}+\eta, \quad|\eta| \leq 2 \delta .$$
故＂把变化放慢＂保留内禀各向异性源，不能自动得到 $O\left(L^{-1}\right)$ 误差。若从 $q_{0}>1$ 开始增长后在 $u^{\prime}=0$ 处转向，必须有 $a^{2} \geq 2\left(q_{0}-1\right) / \delta$ ；上述特定初值却迫使 $a$ 一直收缩。

\section*{3.6 普通点短把手的覆盖体积障碍}

设完备 $\left(M^{n}, g\right) 、 n \geq 3$ ，满足 Ric $\geq-(n-1) k^{2} g$ 。记曲率 $-k^{2}$ 的模型球体积为
$$V_{k}(r)=\left|S^{n-1}\right| \int_{0}^{r} s_{k}(t)^{n-1} d t, \quad s_{k}(t)=\sinh (k t) / k$$
（ $k=0$ 时取 $s_{0}(t)=t$ ）。Bishop－Gromov 给 $\operatorname{Vol} B(p, r) \leq V_{k}(r)$ 。若有两份互不相交、等距于曲率 $-k_{0}^{2}$ 的完整球环带 $b<r<R$ ，且某点 $p$ 到两个内边界每一点的距离均至多 $D$ ，则径向通达性给
$$2\left[V_{k_{0}}(R)-V_{k_{0}}(b)\right] \leq V_{k}(D+R-b) .$$
在 $k, k_{0}$ 有界、 $R_{j} \rightarrow 0 、 b_{j}=o\left(R_{j}\right)$ 下，必有
$$\liminf D_{j} / R_{j} \geq 2^{1 / n}-1 .$$
两份外部环带必须真的不相交；不能把背景中重叠的体积算两次。
只保留一份外环带，也可用普适覆盖得到同样障碍。若其内边界点 $q$ 上有长度至多 $\ell$ 、在 $\pi_{1}(M, q)$ 中非平凡的闭曲线，则
$$2\left[V_{k_{0}}(R)-V_{k_{0}}(b)\right] \leq V_{k}\left(\ell / 2+\pi s_{k_{0}}(b)+R-b\right) .$$

证明是把该环提升到 $\widetilde{q}$ 与非平凡 deck 像之间，取最短线中点。因 $n \geq 3$ ，球环带单连通，两份提升分量互不相交且等距于原环带。中点到两份内边界的距离至多 $\ell / 2+\pi s_{k_{0}}(b)$ ，再作球体积比较。不需要基本群无挠。因此在相同小尺度条件下
$$\liminf \ell_{j} / R_{j} \geq 2\left(2^{1 / n}-1\right) .$$

若手术核心 $U$ 的 $\pi_{1}(U) \rightarrow \pi_{1}(M)$ 像非平凡，以 $D_{U}$ 记只在核心内行走的内蕴直径，则（3．1）中 $\ell / 2$ 可换为 $D_{U}$ 。确实，将任意像非平凡的环分成 $\varepsilon$ 小段，再把分点以长至多 $D_{U}+\varepsilon$ 的路径接回基点，原环是长度至多 $2 D_{U}+3 \varepsilon$ 的小环乘积；至少一个像非平凡。令 $\varepsilon \downarrow 0$ 即得 $\liminf D_{U_{j}} / R_{j} \geq 2^{1 / n}-1$ 。对 $\left(S^{1} \times S^{3}\right) \backslash B^{4}$ 核，van Kampen使其 $\mathbb{Z}$ 成为闭连通和基本群的自由因子，正满足此条件。

论证只用外部体积下界和径向长度上界。若外环带在固定标记中满足（1－$\left.\eta_{j}\right) g_{\mathrm{Euc}} \leq g_{j} \leq\left(1+\eta_{j}\right) g_{\mathrm{Euc}} 、 \eta_{j} \rightarrow 0$ ，其极限常数仍不变。它不要求 Weyl 界或任何光滑泡极限，却确实要求保留这样完整的普通点外部。长而细、体积小但内蕴直径大的区域不被排除。

不能用未经证明的＂两端 Ricci－flat 泡＂替代此直接论证。若已经得到完整光滑、Ric $\geq 0$ 、具有两个端的极限，Cheeger－Gromoll 分裂使其为 $\mathbb{R} \times N 、 N$ 紧，从而不可能同时有欧氏体积增长。 ${ }^{6}$ 但有限领圈的两个边界不是完整空间的两个端；原 Ricci 误差控制不会自动给完整光滑收敛或在一个极限中保留两个端。

\section*{3.7 任意内部几何也无法跨越的平均曲率阈值}

命题3．5（有限边界的距离指数形式）。设 $W^{m+1}$ 紧致连通，有两个非空边界分量 $\Sigma_{0}, \Sigma_{1}$ ，$\operatorname{Ric}_{W} \geq-m k^{2} g 、 k>0$ 。采用从 $W$ 指向外部的法向，令 $H_{\Sigma_{i}} \geq h_{i}$ ，平均曲率不除以$m$ 。若两边界距离为 $L$ ，则
$$h_{0}+h_{1} \leq 2 m k \tanh (k L / 2)<2 m k .$$
证明．取实现距离的单位速正交测地线 $\gamma:[0, L] \rightarrow W$ ，沿其平行移送正交法标架 $E_{i}$ 。对 $V_{i}=f E_{i} 、 f(0)=f(L)=1$ ，端点可在边界移动的第二变分给
$$0 \leq \sum I\left(V_{i}, V_{i}\right)=\int_{0}^{L}\left\{m\left(f^{\prime}\right)^{2}-f^{2} \operatorname{Ric}\left(\gamma^{\prime}, \gamma^{\prime}\right)\right\} d t-H_{0}-H_{1}$$
两个边界项均为负号，这是外法向约定的结果。选 $f(t)=\cosh (k(t-L / 2)) / \cosh (k L / 2)$ ，则 $\int\left(\left(f^{\prime}\right)^{2}+k^{2} f^{2}\right)=\left[f f^{\prime}\right]_{0}^{L}=2 k \tanh (k L / 2)$ ，结论随即成立。 \(\square\)

这是经典第二变分方法的有限边界版本，未把无穷远的渐近双曲定理套到有限接口。 ${ }^{7}$

命题3．6（单球面边界核心的拓扑约束）。设紧致连通 $U^{m+1}$ 只有一个边界 $\Sigma \cong S^{m}$ ，$m \geq 2$ ，且 $\pi_{1}(U) \neq 0$ 。若 $\operatorname{Ric}_{U} \geq-m k^{2} g 、 H_{\Sigma} \geq h$ ，则 $h<m k$ 。

\footnotetext{
${ }^{6} \mathrm{M}$ ．Anderson，A survey of Einstein metrics on 4－manifolds，§5，https：／／arxiv．org／pdf／0810．4830。
${ }^{7}$ M．Cai，G．Galloway，Boundaries of zero scalar curvature in the AdS／CFT correspondence，Proposition 2与覆盖论证，https：／／arxiv．org／pdf／hep－th／0003046。
}

证明．普适覆盖的边界至少有两个分量，每个都等距于紧的 $\Sigma$ 。提升的带边界长度空间完备且 proper；紧原空间的正宽度领圈给不同提升边界统一正间距。固定一个分量后，到其余分量的最小距离可在一个分量上取得。最短线开段若先碰第三个边界，就得到更短距离，矛盾。在这条线应用上一命题，得到 $2 h<2 m k$ 。 \(\square\)

它不需要把手生成元短或核心直径小。
对四维归一化双曲外部 Ric $=-g$ ，半径 $R$ 的球面，相对于从球心向外的法向具有$H_{R}=\sqrt{3} \operatorname{coth}(R / \sqrt{3})$ 。考虑以任意紧致连通桥连接两个被删球面，或用 $\left(S^{1} \times S^{3}\right) \backslash B^{4}$核替换一个球。若新度量在接口处匹配外部的诱导度量和第二基本形式，则相对于核心的外法向，接口平均曲率均为正的 $H_{R}$ 。令 $\delta=\delta_{-}(g)$ ，在两种情形均有
$$\sqrt{3} \operatorname{coth}(R / \sqrt{3})<\sqrt{3(1+\delta)}, \quad \delta>\operatorname{csch}^{2}(R / \sqrt{3}) .$$
因此
$$R>\sqrt{3} \operatorname{arsinh}\left(\delta^{-1 / 2}\right)=\frac{\sqrt{3}}{2} \log (1 / \delta)+\sqrt{3} \log 2+o(1) .$$
这是无对称假设、不限制长度或 Weyl 的接口障碍。固定半径不能得到误差趋零；缩小半径时下界反而为3／$R^{2}$ 阶。两个相同球面的桥还必须满足
$$L \geq 2 \sqrt{\frac{3}{1+\delta}} \operatorname{artanh}\left(\frac{\operatorname{coth}(R / \sqrt{3})}{\sqrt{1+\delta}}\right) .$$
若只知道接口 $H_{i} \geq H_{R}-\eta>0$ ，同样得到稳定版本
$$\delta>(\operatorname{coth}(R / \sqrt{3})-\eta / \sqrt{3})^{2}-1 .$$
仅有诱导边界度量接近，并不能代替所需的平均曲率接近。

\section*{3.8 变化拓扑熵候选：不存在性已知，近似输入尚缺}

令 $X$ 为闭定向实双曲四流形，$X_{d} \rightarrow X$ 为次数趋于无穷的有限连通覆盖子序列。这类序列可由双曲流形群的剩余有限性取得；不要求每个整数次数均出现。记 $c_{d}= \chi\left(X_{d}\right)=d \chi(X)$ 。取固定闭定向 $Q$ ，假设其基本群分类映射可压入分类空间三维骨架，即 $Q$ 为 nonessential，且
$$t_{Q}=2-\chi(Q)+\frac{3}{2}|\tau(Q)|>0, \quad M_{d}=X_{d} \# Q .$$
Brunnbauer－Ishida－Suárez－Serrato 的连通和定理给 $\lambda\left(M_{d}\right)=\lambda\left(X_{d}\right)$ 。 $^{8}$ 对前文定义的$A=\chi-3|\tau| / 2 、 B=\lambda^{4} /\left(108 \pi^{2}\right)$ ，双曲刚性及 Gauss－Bonnet 给
$$A\left(M_{d}\right)=c_{d}-t_{Q}, \quad B\left(M_{d}\right)=c_{d} .$$

\footnotetext{
${ }^{8}$ M．Brunnbauer，M．Ishida，P．Suárez－Serrato，An essential relation between Einstein metrics，volume entropy， and exotic smooth structures，Theorem 1．1，https：／／arxiv．org／pdf／0807．1187。
}

Kotschick 的全符号 Einstein 必要条件 $A \geq B$ 遂排除每个 $M_{d}$ 上的全部 Einstein 度量。${ }^{9}$ 例如 $Q=S^{1} \times S^{3}$ 时 $t_{Q}=2, Q=\mathbb{C P}^{2}$ 或反向时 $t_{Q}=1 / 2$ 。这些是已发表不存在性理论的应用，不能声称为新发现的无 Einstein 流形。

前文精确误差不等式在 $0 \leq \delta \leq 1 / 3$ 给 $A \geq((1-\delta) /(1+\delta))^{2} B$ 。对 $c_{d} \geq 4 t_{Q} / 3$ ，反解落在此区间，于是对 $M_{d}$ 上所有度量均有
$$\delta_{-}(g) \geq \frac{1-\sqrt{1-t_{Q} / c_{d}}}{1+\sqrt{1-t_{Q} / c_{d}}}=\frac{t_{Q}}{4 c_{d}}+O\left(c_{d}^{-2}\right) .$$
若实际误差大于 $1 / 3$ ，此下界自动成立。下界趋零不等于下确界趋零：本稿没有在这些$M_{d}$ 上构造最大误差趋零的度量。这也不同于对固定候选作有限覆盖；这里先扩大双曲部分，再只接上一个固定 $Q$ ，使亏损 $t_{Q}$ 不随 $d$ 增长。

若 $\delta \leq 1 / 3$ ，任何潜在输入还须满足
$$\begin{gathered}
\frac{12 \pi^{2} c_{d}}{(1+\delta)^{2}} \leq \operatorname{Vol}\left(M_{d}, g\right) \leq \frac{12 \pi^{2}\left(c_{d}-t_{Q}\right)}{(1-\delta)^{2}} \\
\operatorname{diam}\left(M_{d}, g\right) \geq \frac{\log c_{d}}{\sqrt{3(1+\delta)}}-C
\end{gathered}$$
体积下界由熵与 Bishop 上界给出，上界来自曲率积分；直径式来自模型球的指数体积增长。故假如取得 $\delta_{d}=O\left(c_{d}^{-1}\right)$ ，其体积必须为 $12 \pi^{2} c_{d}+O(1)$ ，直径必发散。

带边界结果进一步量化了精确保留双曲外部的手术代价。归一化双曲四球体积为
$$V_{\mathbb{H}}(R)=6 \pi^{2}\left(z^{3}-3 z+2\right), \quad z=\cosh (R / \sqrt{3}) .$$
若从 $X_{d}$ 删除两个互不相交的半径 $R$ 球再接桥，则 $2 V_{\mathbb{H}}(R) \leq 12 \pi^{2} c_{d}$ ，而上一节给$z>\sqrt{1+\delta^{-1}}$ 。因此
$$c_{d}>\left(1+\delta^{-1}\right)^{3 / 2}-3\left(1+\delta^{-1}\right)^{1 / 2}+2, \quad \liminf c_{d} \delta^{3 / 2} \geq 1 .$$
单球填入把手核心时系数相应为1／2。这强于该家族的全局熵下界所要求的 $c_{d} \gtrsim \delta^{-1}$ ，却仍允许覆盖任意增大。它要求替换半径和移除的原双曲体积一起增长，排除了＂把手术放在越来越小普通点区域内＂的这类实现方式。没有由此排除大范围改变外部几何、改变接口，或完全不同的全局构造。

\footnotetext{
${ }^{9}$ D．Kotschick，Entropies，Volumes，and Einstein Metrics，Theorem 1、Corollary 3，https：／／arxiv．org／pd f／math／0410215。
}

\section*{第四章 高度四椭圆曲面：全局典范关系与复形变障碍}

本章保留代数支线中能够分别审核的三个对象：指定的光滑四维候选、显式的典范完全交模型、该模型的形变理论。复结构不存在、全局 $\mathbb{Q}$－Gorenstein 平滑不存在、实 Einstein 度量不存在，是三个不同断言。本章不认证原创性、发表优先权或同行评审完成；涉及全模栈下降及实际 Einstein 退化的结论，单独保留其前提。

\section*{4.1 候选对象与数值等号分类}

取文献指定的椭圆曲面 $E(4)$ ，沿一个自交数 -4 的截面作有理吹降，记所得光滑流形为 $N=W_{4,1}=Y_{4}$ 。它指指定手术的光滑型，不能仅按特征数选择同胚流形代替。已有文献给出单连通、极小辛性质及
$$\chi(N)=47, \quad \tau(N)=-31, \quad b_{+}(N)=7, \quad b_{-}(N)=38, \quad 2 \chi(N)+3 \tau(N)=1 .$$
Lee 明确讨论单截面有理吹降不承载复结构的结论；同时吹降多个截面的正面构造不能套用到单截面。Şuvaina 提供相关负 Kähler－Einstein 轨形与 Yamabe 背景。 ${ }^{1}$

数值上的非复障碍很具体：若给定定向下 $N$ 有复结构，单连通性给 $b_{1}=0$ ，故为 Kähler；结合极小性得到一般型极小曲面 $p_{g}=3, K^{2}=1$ ，违反 Noether 不等式$K^{2} \geq 2 p_{g}-4=2$ 。反向定向有 $(\chi-\tau) / 4=78 / 4 \notin \mathbb{Z}$ ，连 almost－complex 结构所需的整数条件也不满足。这些结论不排除非 Kähler 的实 Einstein 度量。

命题4．1（已发表等号分类的应用）。设 $X$ 为正规射影曲面，只有商奇点，且 $K_{X}$ ample、$K_{X}^{2}=1 、 p_{g}(X)=3$ 。则其最小消解 $M$ 为带截面的相对极小椭圆曲面 $f: M \rightarrow \mathbb{P}^{1}$ ，满足
$$K_{M} \sim 2 F, \quad C^{2}=-4 .$$
映射 $M \rightarrow X$ 收缩 $C$ 为唯一非典范奇点 $\frac{1}{4}(1,1)$ ；其余被收缩曲线为纤维中不交 $C$ 的全部 ADE 配置。

该分类核心归于 Tsunoda－Zhang。 ${ }^{2}$ 其适用性核查如下。写 $\pi^{*} K_{X}=K_{M}+B$ ，$B=\sum b_{i} E_{i}, D=\sum E_{i}$ 。最小商奇点消解给 $0 \leq b_{i}<1$ ，而 $K_{M}+D=\pi^{*} K_{X}+(D-B)$ 为Zariski 分解。正部平方为一，且原文的对数几何亏格公式给 $h^{0}\left(K_{M}+D\right)=h^{0}\left(K_{M}\right)=3$ 。若系统不由 pencil 给出，原文不等式给 $3 \leq \frac{1}{2}+2$ ，矛盾。pencil 情形的界
$$\bar{p}_{g} \leq \frac{P^{2}+\sqrt{\left(P^{2}\right)^{2}+8 P^{2}}}{2}+1$$

\footnotetext{
${ }^{1} \mathrm{Y}$ ．Lee，Complex structure on the rational blowdown of sections in $E$（4），https：／／arxiv．org／pdf／0905．3705； I．Şuvaina，The Yamabe invariant of a class of symplectic 4－manifolds，https：／／arxiv．org／abs／1410．1236。
${ }^{2}$ S．Tsunoda and D．－Q．Zhang，Noether＇s Inequality for Non－complete Algebraic Surfaces of General Type， Publ．RIMS 28 （1992），21－38，Theorems 1．3、2．10（3），Propositions 1．6－1．7：https：／／ems．press／content／se rial－article－files／40427？nt＝1。
}

恰取等号，已发表等号分类给 $B=C / 2 、 K_{M} \sim 2 F 、 C^{2}=-4$ 。对其余异常曲线 $E$ ，$0=\left(K_{M}+C / 2\right) \cdot E$ 的非负项同时为零；伴随公式给 $E^{2}=-2 、 F \cdot E=C \cdot E=0$ ，得到 ADE 部分。 $K_{X}$ ample 迫使所有不交截面的纤维分量都被收缩。

说明 4．2。这是纯代数分类。实际 Einstein 序列是否产生非塌缩轨形极限、是否 Kähler、射影、且具有上述数值，须由分析部分独立证明。本章不从 Ricci 误差趋零直接推出这些条件。

\section*{4.2 消解、自然轨形与典范覆盖栈}

令 $Y \rightarrow \mathbb{P}^{1}$ 为高度四最小 Weierstrass 曲面，截面 $C$ 位于光滑部分，$C^{2}=-4$ ，允许 ADE 总空间奇点。方程为
$$y^{2}=x^{3}+A_{16}(u, v) x+B_{24}(u, v),$$
下标为二元齐次次数；最小性要求不存在一点同时满足 $\operatorname{ord} A \geq 4$ ，ord $B \geq 6$ 。收缩截面得 $X$ 。Wahl 点附近须区分

\begin{tabular}[t]{|l|l|}
\hline 对象 & 局部模型 \\
\hline 粗曲面 & $\mathbb{C}^{2} / \mu_{4}$ \\
\hline 自然光滑商轨形 & $\left[\mathbb{C}^{2} / \mu_{4}\right]$ \\
\hline 典范覆盖栈 & $\left[\left\{a c-b^{2}=0\right\} / \mu_{2}\right]$. \\
\hline
\end{tabular}
$\mu_{4}$ 标量作用；$\mu_{2}$ 同时翻转 $(a, b, c)$ 。指标一覆盖是奇异 $A_{1}$ ，不是光滑 $\mathbb{C}^{2}$ 。ADE 点的自然商轨形光滑，而典范覆盖栈是原奇异 scheme。自然轨形的 Dolbeault 复形与典范覆盖的余切复形不可互换。 ${ }^{3}$

命题4．3（指定模型的典范环）。有
$$\begin{gathered}
R\left(X, K_{X}\right)=\frac{\mathbb{C}[a, b, c, x, y]}{\left(a c-b^{2}, y^{2}-x^{3}-A_{8}(a, b, c) x-B_{12}(a, b, c)\right)} \\
\operatorname{deg}(a, b, c, x, y)=(1,1,1,4,6)
\end{gathered}$$
对应的加权完全交栈为 $X$ 的典范覆盖栈。
证明．ADE 消解 crepant，截面收缩 discrepancy 为 $-1 / 2$ 。故
$$H^{0}\left(X, \omega_{X}^{[m]}\right)=H^{0}\left(M, \mathcal{O}_{M}(2 m F+\lfloor m / 2\rfloor C)\right) .$$
Weierstrass 函数 $x, y$ 沿截面极阶为 2,3 ；单项式取 $x^{i} y^{j}, i \geq 0 、 j=0,1$ ，其系数次数为 $2 m-8 i-12 j$ ，极阶条件恰为 $4 i+6 j \leq m 。 a=u^{2}, b=u v, c=v^{2}$ 生成低次偶数环，关系为 $a c-b^{2}$ ；另一关系来自原 Weierstrass 方程。

记 $\mathcal{P}=\mathbb{P}(1,1,1,4,6) 、 \mathfrak{X}=V\left(q, F_{12}\right)$ 。两式为正则序列，伴随给 $\omega_{\mathfrak{X}}=\mathcal{O}(2+12- 13)=\mathcal{O}(1)$ 。权重一坐标不全为零处稳定子平凡。轴上 $y^{2}=x^{3}$ 给唯一轨道，$x, y \neq 0$ ，

\footnotetext{
${ }^{3}$ P．Hacking，Compact moduli of plane curves，Proposition 3．7、Theorem 3．9：https：／／paulhacking．gith ub．io／planecurves．pdf 。D．Abramovich and B．Hassett，Stable varieties with a twist，§5．3：https：／／arxiv． org／pdf／0904．2797，提供 Kollár 条件、典范覆盖与极化线丛的接口。
}

稳定子 $\mu_{2}$ ；étale 图上消去 $y$ 得 $\left[A_{1} / \mu_{2}\right]$ ，稳定子在典范线上作用忠实。因此没有额外gerbe。 \(\square\)

原始模型 $X_{24} \subset \mathbb{P}(1,1,8,12)$ 的 $K_{X}=\mathcal{O}_{X}(2)$ ，其 $\mathcal{O}(1)$ 不是典范层。必须取偶数Veronese 才得到（4．3）。这是对象识别的必要校正。

\section*{4.3 低次典范乘法控制全部 Artin 平滑参数}

引理4．4（非退化二次典范关系）。设 $X$ 正常 KSB 稳定，$p$ 为 $\frac{1}{4}(1,1)$ 点，$V=H^{0}\left(\omega_{X}\right)$ 、$W=H^{0}\left(\omega_{X}^{[2]}\right)$ 。假设：
\begin{itemize}
\item[1．] $H^{1}\left(\omega_{X}\right)=H^{1}\left(\omega_{X}^{[2]}\right)=0$ ；
\item[2．] $\operatorname{dim} V=3 、 \operatorname{dim} W=5$ ；
\item[3．] $\operatorname{Sym}^{2} V \rightarrow W$ 满射，核由秩三二次型 $q$ 生成；
\item[4．] 在指标一覆盖 $B_{0}=\mathbb{C}[[u, v, w]] /\left(u v-w^{2}\right)$ 上，$V$ 的某基对应三个反不变函数，其像组成 $\mathfrak{m}_{B_{0}} / \mathfrak{m}_{B_{0}}^{2}$ 的基。
\end{itemize}

则每个局部 Artin 复代数 $A$ 上的 KSB／QG 形变，在 $p$ 处的典范覆盖形式局部为
$$\left[\operatorname{Spf} A[[u, v, w]] /\left(u v-w^{2}\right) / \mu_{2}\right] .$$
同构可尊重中心标记，局部 Wahl 平滑参数在每个 Artin 层恒为零。
证明．Kollár 条件给平坦典范覆盖 $\mathfrak{X}_{A}$ 和可逆层 $L_{A}$ 。小扩张 $A^{\prime} \rightarrow A$ 的核 $J$ 满足$\mathfrak{m}_{A^{\prime}} J=0$ 。中心 $H^{1}\left(L^{k}\right)=0, k=1,2$ ，给
$$0 \rightarrow H^{0}\left(L^{k}\right) \otimes J \rightarrow H^{0}\left(L_{A^{\prime}}^{k}\right) \rightarrow H^{0}\left(L_{A}^{k}\right) \rightarrow 0 .$$
逐层归纳，$V_{A}, W_{A}$ 为自由模，秩为3，5，与基变换相容。乘法由 Nakayama 保持满射；其核是秩一自由直和项，生成元记为 $q_{A}$ 。中心非退化使判别式为单位。特征零下可作约化为恒等的线性变换，恢复固定 $u v-w^{2}$ ：矩阵线性化 $T \mapsto T^{\top} Q+Q T$ 对可逆对称$Q$ 满射，取 $T=Q^{-1} D / 2$ 消去任意对称小扰动，逐层归纳即可。

实际相对指标覆盖的完备局部环记为 $B_{A}$ 。三个提升截面在同一等变标架下为反不变函数 $f_{i, A}$ ，满足真实关系 $q_{A}\left(f_{1, A}, f_{2, A}, f_{3, A}\right)=0$ 。条件四与形式 Nakayama 给满射
$$C_{A}=A\left[\left[z_{1}, z_{2}, z_{3}\right]\right] /\left(q_{A}\right) \rightarrow B_{A} .$$
中心是同构：中心三函数为嵌入坐标，核为包含不可约 $q$ 的高度一素理想，故恰为 $(q)$ 。设满射核为 $K$ 。 $B_{A}$ 对 $A$ 平坦，张量剩余域后 $K / \mathfrak{m}_{A} K$ 单射到 $C_{0}$ 。中心映射同构，故该模为零； $\mathfrak{m}_{A}$ 幂零，反复代入 $K=\mathfrak{m}_{A} K$ 得 $K=0$ 。
$\mu_{2}$ 在三个坐标上取负，线性正规化与之交换。两局部平凡化之差的中心恒等部分可取有限对数，写成取值于 $\mathfrak{m}_{A}$ 的等变导子；逐系数提升后取有限指数，便可尊重小扩张前已给的标记。 \(\square\)
$d t=0$ 不排除 $t=s^{2}$ 或纯幂零参数。这里使用每个 Artin 基上的真实关系、平坦性及幂零 Nakayama，因此控制高阶。只有 $p_{g}=3, P_{2}=5$ 不够；乘法满射、关系非退化和局部坐标生成性均不可删。对于（4．3），$R_{1}=\langle a, b, c\rangle$ 、 $\operatorname{dim} R_{2}=5$ ，二次关系为$a c-b^{2}$ ，三函数正是覆盖嵌入坐标；所需 $H^{1}$ 消失由下一节给出。

\section*{4.4 完整 QG 计算：三十八维与无穷小厚化}

命题4．5（显式模型的完整形变计算）。设 $X$ 为命题4．3的正常稳定模型， $\mathfrak{X}$ 为典范覆盖栈，采用满足 Kollár 条件的 KSB／QG 形变。则
$$\operatorname{dim} \operatorname{Ext}^{1}\left(L_{\mathfrak{X}}, \mathcal{O}_{\mathfrak{X}}\right)=38, \quad \operatorname{Ext}^{2}\left(L_{\mathfrak{X}}, \mathcal{O}_{\mathfrak{X}}\right)=0 .$$
带中心标记的半通用基形式光滑。每个 Artin 形变的典范环仍有五个同权重生成元、两条同次数关系，且 Wahl 点形式局部平凡。

证明．完全交环 Krull 维数三，Cohen－Macaulay。Koszul 分解及 Serre 对偶给
$$H^{1}(\mathfrak{X}, \mathcal{O}(k))=0, \quad H^{2}(\mathcal{O}(k))=H^{0}(\mathcal{O}(1-k))^{*} \quad(k \in \mathbb{Z}) .$$
这里对偶用于 proper Gorenstein 栈，无需栈光滑。限制加权 Euler 序列：
$$0 \rightarrow \mathcal{O} \rightarrow \mathcal{O}(1)^{3} \oplus \mathcal{O}(4) \oplus \mathcal{O}(6) \rightarrow E \rightarrow 0, \quad E=\left.T_{\mathcal{P}}\right|_{\mathfrak{X}}$$
高阶映射 $H^{2}(\mathcal{O}) \rightarrow H^{2}(\mathcal{O}(1))^{3}$ 的对偶是
$$\mathbb{C}^{3} \rightarrow R_{1}, \quad(\alpha, \beta, \gamma) \mapsto \alpha a+\beta b+\gamma c,$$
为同构，所以 $H^{1}(E)=H^{2}(E)=0$ 。余切复形对偶为 $[E \rightarrow \mathcal{N}]$ ，位于次数 0,1 ，其中$\mathcal{N}=\mathcal{O}(2) \oplus \mathcal{O}(12)$ 。总次数二的 $H^{2}(E), H^{1}(\mathcal{N})$ 都为零，故 $\operatorname{Ext}^{2}=0$ 。Hilbert 级数
$$\frac{\left(1-z^{2}\right)\left(1-z^{12}\right)}{(1-z)^{3}\left(1-z^{4}\right)\left(1-z^{6}\right)}$$
在次数0，1，2，4，6，12的系数依次为1，3，5，10，19，70。因此
$$h^{0}(E)=3 \cdot 3+10+19-1=37, \quad h^{0}(\mathcal{N})=75 .$$
稳定性在特征零下排除无穷小自同构，故 $\operatorname{dim} \operatorname{Ext}^{1}=38$ 。这不等于 $H^{2}\left(\Theta_{X}\right)$ 消失。
从任意 Artin KSB 形变出发，典范覆盖自带线丛 $L_{A}$ 。（4．7）使各次截面模 $\left(R_{A}\right)_{k}=H^{0}\left(\mathfrak{X}_{A}, L_{A}^{k}\right)$ 自由，且与基变换相容。提升五个中心生成元，逐次数Nakayama 给 $A[a, b, c, x, y] \rightarrow R_{A}$ 。核 $I_{A}$ 各次与中心基变换相容，可提升中心关系为$q_{A} \in\left(I_{A}\right)_{2}, F_{A} \in\left(I_{A}\right)_{12}$ 。有限模 $\left(I_{A} /\left(q_{A}, F_{A}\right)\right)_{k}$ 的中心为零，Nakayama 给
$$R_{A}=A[a, b, c, x, y] /\left(q_{A}, F_{A}\right) .$$
这排除了高阶新增生成元与额外关系。充分高偶次典范幂相对 ample，Proj 恢复 $X_{A}$ ；统一化极化线丛的 stack Proj 恢复典范覆盖。权重使 $q_{A}$ 只含 $a, b, c$ ，可恢复为 $a c-b^{2}$ 。轴上 $F_{A}$ 只剩单位系数的 $y^{2}, x^{3}$ ，消去 $y$ 后仍为 $\left[A_{1} / \mu_{2}\right]$ 平凡族。亦可用引理4．4。 □

\section*{4．4．1 从显式模型到整个模栈的条件接口}

计算不要求 ADE 奇点一般位置。若正常、积分纤维的 lc Weierstrass 总空间已建立同一典范环，计算仍适用；但严格 lc 情形须在 Weierstrass 总空间本身使用 $K_{Y} \sim 2 F$ ，不能搬到非 crepant 消解。

命题4．6（条件性的开浸入结论）。设截面收缩态射由正常高度四 Weierstrass 模栈到KSB 模栈，局部有限表示，在几何点及其自同构上为单态；并且每个 Wahl 点局部平凡的 Artin KSB 形变都能按给定标记、同构及基变换，相容地恢复为带截面的 Weierstrass家族。则命题4．5使该态射在上述模型开集上为 étale monomorphism，因而是开浸入；该开集模栈光滑、维数三十八。

局部恢复可具体计算：恢复 $q$ 后，对 $F_{A}$ 完成平方消去 $y$ 一次项，再平移 $x$ 消去二次项，得 $y^{2}=x^{3}+A_{8}(a, b, c) x+B_{12}(a, b, c)$ 。二次曲线 $a c-b^{2}=0$ 在局部 Artin 复基上为 $\mathbb{P}_{A}^{1}$ ，其 $\mathcal{O}(1)$ 对应 $\mathcal{O}_{\mathbb{P}_{A}^{1}}(2)$ ，从而恢复次数16，24的 Weierstrass 系数。整个模栈的下降、Brauer－Severi 基底及自同构相容性，仍属于上命题明列的接口。

Bejleri 等公开 v2的 Remarks 1．6、5．6 留下高度四环境分支的泛点非约化问题。本章计算与该问题直接相关，不能归为该文已证结果，也不能直接宣称整个紧化边界约化。 ${ }^{4}$

\section*{4.5 自然形变障碍空间：一维并非普遍成立}

仍只允许 Wahl 与 ADE 奇点。令 $\pi: M \rightarrow X$ 为最小消解，$f: M \rightarrow \mathbb{P}^{1}$ 为椭圆纤维化。

命题4．7（反射张量与普通一形式）。有自然同构
$$H^{2}\left(X, \Theta_{X}\right)^{*} \cong H^{0}\left(M, \Omega_{M}^{1} \otimes K_{M}\right) .$$
证明．正规曲面 Cohen－Macaulay，顶次 Serre 对偶给
$$H^{2}\left(X, \Theta_{X}\right)^{*}=\operatorname{Hom}_{X}\left(\Theta_{X}, \omega_{X}\right)=H^{0}\left(X, j_{*}\left(\Omega_{X_{\mathrm{reg}}}^{1} \otimes K_{X_{\mathrm{reg}}}\right)\right) .$$
Hom 层为反射层，无需 $\Theta_{X}$ 局部自由。ADE 处典范层 Cartier、消解 crepant；除去局部典范生成元后用 klt 一形式延拓，可知扭曲张量正则拉回。 ${ }^{5}$

Wahl 点光滑覆盖坐标为 $(u, v)$ ，不变张量写成 $\sigma=(a d u+b d v) \otimes(d u \wedge d v)$ 。系数次数为 $1 \bmod 4$ 。在 $v=z u, s=u^{4}$ 消解图，写 $a=u A(s, z), b=u B(s, z)$ ，直接算得
$$\pi^{*} \sigma=\left(\frac{A+z B}{16} \frac{d s}{s}+\frac{B}{4} d z\right) \otimes(d s \wedge d z) .$$

\footnotetext{
${ }^{4}$ D．Bejleri，J．Foster，A．Fernandez Herrero，G．Inchiostro，S．Makarova and J．Zhao，Moduli of elliptic surfaces of Kodaira dimension one fibered over rational curves，arXiv：2407．05539v2， 2025 年 12 月 5 日：https： ／／arxiv．org／html／2407．05539v2。本章核查此版本，不声称已核对期刊终稿或完成全面优先权检索。
${ }^{5}$ D．Greb，S．Kebekus，S．J．Kovács and T．Peternell，Differential forms on log canonical spaces，klt 正则延拓：https：／／arxiv．org／abs／1003．2913。这里先去掉可逆典范因子，不把一般张量积直接套入一形式定理。
}

故至多有沿 $C$ 的单对数极。一般光滑椭圆纤维上 $\left.K_{M}\right|_{F}$ 平凡，将张量作用于 $T F$ 得紧曲线的亚纯一形式；唯一可能极点为 $F \cap C$ ，至多单极。留数和为零，故唯一留数为零。它恰为（4．10）沿 $C$ 的对数留数，在稠密集为零遂处处为零。留数正合列给正则拉回。反方向由限制到正则部和反射延拓得到，两者在稠密集互逆。 \(\square\)

\section*{4．5．1 非等模的一维结论}

若 $j_{f}$ 非常数，一般光滑纤维上的序列
$$\left.0 \rightarrow \mathcal{O}_{F} \rightarrow \Omega_{M}^{1}\right|_{F} \rightarrow \mathcal{O}_{F} \rightarrow 0$$
具有非零 Kodaira－Spencer 扩张类。连接 $H^{0}\left(\mathcal{O}_{F}\right) \rightarrow H^{1}\left(\mathcal{O}_{F}\right)$ 是同构，所以其全部截面水平。又 $f^{*} \Omega_{\mathbb{P}^{1}}^{1} \otimes K_{M} \simeq \mathcal{O}_{M}$ ，每个全局扭曲一形式在稠密集为 $h \sigma_{\mathrm{hor}}$ 。纤维紧性使$h$ 来自基底亚纯函数；沿截面 $d f$ 处处非零，排除其极点。因此 $h$ 为常数，得到
$$h^{2}\left(X, \Theta_{X}\right)=1 \quad \text { ( } j_{f} \text { 非常数). }$$
这一论证不依赖 QG 无障碍性。

\section*{4．5．2 等模：每个奇异纤维贡献一个基底零点}

设 $j_{f}$ 常数，$D$ 为基底上奇异纤维的约化除子，$k=\operatorname{deg} D, L=\mathcal{O}_{\mathbb{P}^{1}}(4)$ 。
命题4．8。在最小 Weierstrass、仅 ADE 总空间奇点的范围内，
$$0 \rightarrow \Omega_{\mathbb{P}^{1}}^{1} \rightarrow f_{*} \Omega_{M}^{1} \rightarrow L(-D) \rightarrow 0, \quad h^{2}\left(X, \Theta_{X}\right)=1+\max (0,7-k) .$$
证明。 $\Omega_{M}^{1}$ 正则映到 $\omega_{M / \mathbb{P}^{1}}$ ，故相对像系数正则。一般纤维上为零的形式必为 $p(z) d z$ ；沿截面排除极点，确定核为基底余切层。

等模 Weierstrass 方程的系数满足 $A^{\prime}=2 c A, B^{\prime}=3 c B$ 。分别可取 $c=B^{\prime} /(3 B)$ 、 $A^{\prime} /(2 A)$ ，或在 $A=\alpha P^{2}, B=\beta P^{3}$ 时取 $P^{\prime} / P$ 。定义
$$\eta=\frac{d x-c x d z}{y}=\frac{2 d y-3 c y d z}{3 x^{2}+A} .$$
两式在普通支点互补。截面处令 $w=x / y$ ，有 $x=w^{-2}+O\left(w^{2}\right), y=w^{-3}+O(w)$ ，故 $d x / y$正则，且 $\eta$ 拉回截面为零。奇异基底点 $z=0$ 处，最小等模模型给 $c=\kappa / z+$ 正则项， $\kappa \neq 0$ ，于是 $z \eta$ 在总空间光滑处正则。唯一另需检查的光滑原点为 $y^{2}=x^{3}+z$ ，此时$z \eta=y d x-\frac{2}{3} x d y$ 。其他原点为 ADE，由一形式延拓定理正则拉回。

反之，写正则形式 $\alpha=h(z) \eta+p(z) d z$ 。相对正则性先给 $h$ 正则，沿截面再给 $p$正则。 $\eta$ 在奇异纤维一般点的极部为 $-\kappa(x / y) d z / z$ ，并非恒零，不能由只依赖基底的 $p$抵消，所以 $h(0)=0$ 。每个奇异纤维恰贡献一次基底零点，得到短正合列。张量 $\mathcal{O}(2)$后为
$$0 \rightarrow \mathcal{O} \rightarrow f_{*}\left(\Omega_{M}^{1} \otimes K_{M}\right) \rightarrow \mathcal{O}(6-k) \rightarrow 0 .$$
$H^{1}\left(\mathbb{P}^{1}, \mathcal{O}\right)=0$ ，结合（4．9）得维数公式。 \(\square\)

由最小性得到完整表：

\begin{tabular}[t]{|l|l|l|}
\hline 类型 & 根数限制 & $h^{2}\left(\Theta_{X}\right)$ \\
\hline $j$ 非常数 & 无此参数 & 1 \\
\hline $j=0, A=0, \operatorname{deg} B=24$ & $k \geq 5$ & $1+\max (0,7-k)$ \\
\hline $j=1728, B=0, \operatorname{deg} A=16$ & $k \geq 6$ & $1+\max (0,7-k)$ \\
\hline $j \notin\{0,1728, \infty\}$ 常数 & $k=8$ & 1 \\
\hline
\end{tabular}
两个特殊等模分支的根重数分别不超过 5,3 ；其余常 $j$ 写作 $A=\alpha P_{8}^{2}, B=\beta P_{8}^{3}, P_{8}$ 无重根。因此 $h^{2}$ 确可为二或三，不能保留整族恒为一维的早期说法。

\section*{4．6 Wahl 商与 ADE 插值：障碍空间不等于实际障碍}

记 $T_{\mathrm{ADE}}^{1}$ 为全部 ADE 局部形变空间，$T_{W}^{1}=\mathbb{C}$ 为 Wahl 局部 QG 平滑方向。由标准局部到全局谱序列及（4．6），
$$0 \rightarrow H^{1}\left(\Theta_{X}\right) \rightarrow T_{\mathrm{QG}}^{1} \rightarrow T_{\mathrm{ADE}}^{1} \oplus \mathbb{C} \xrightarrow{d_{2}} H^{2}\left(\Theta_{X}\right) \rightarrow 0 .$$
全局切空间到 Wahl 因子的投影为零，故
$$H^{2}\left(\Theta_{X}\right) / d_{2}\left(T_{\mathrm{ADE}}^{1}\right) \cong \mathbb{C}$$
这是一维障碍商，而不是整个 $H^{2}$ 一维。商泛函可归一化为 $\ell\left(d_{2}(e, w)\right)=w$ 。

\section*{4．6．1 局部代数与全局 jet 插值}
$j=0$ 的根重数 $m$ 处，方程 $y^{2}-x^{3}-z^{m}=0$ 的 Jacobian 商为
$$\mathbb{C}\{x, z\} /\left(x^{2}, z^{m-1}\right) .$$
常数和 $x$ 两块各长 $m-1$ ，由 $\dot{B}, \dot{A}$ 控制。所有根的总块长为 $24-k$ 。多点限制$H^{0}\left(\mathbb{P}^{1}, \mathcal{O}(d)\right) \rightarrow H^{0}\left(\mathcal{O}_{Z}\right)$ 秩为 $\min (d+1, \operatorname{deg} Z)$ ，故 $\operatorname{ADE}$ 余核为 $\max (0,7-k)$ 。
$j=1728$ 时，局部商为
$$\mathbb{C}\{x, z\} /\left(3 x^{2}+z^{m}, z^{m-1} x\right),$$
基取 $1, z, \ldots, z^{2 m-2}$ 和 $x, x z, \ldots, x z^{m-2}$ ，两块长 $2 m-1, m-1$ 。 $m=1$ 时仍有一维第一块，给 $A_{1}$ ，不是光滑点。全局 $\dot{B}, \dot{A}$ 的插值再给相同余核。它与普通微分形式的独立计算一致，但这种秩比较本身不控制高阶 Artin 障碍。

\section*{4．6．2 自然形变消障的完整条件}

命题4．9（自然形变的条件性无障碍结论）。对上述 Wahl／ADE 模型，另保留两个形变接口：
\begin{itemize}
\item[1．] 自然光滑商轨形的小扩张提升障碍，等于局部 QG 提升差异经（4．14）的 $d_{2}$ 所得类；
\end{itemize}

2．Wahl 局部平凡 QG 形变的 Weierstrass 恢复尊重中心标记及同构。
则自然局部平凡形变的所有实际 Artin 障碍消失。
证明。先设 $h^{2}=1$ 。给定 $A$ 上自然形变，QG 形式光滑性给 $A^{\prime}$ 上一个全局 QG 提升。将其局部图改为预先指定的平凡提升，差异为 $\left(\tau_{\mathrm{ADE}}, \tau_{W}\right)$ 。全部 Artin Wahl 局部平凡性给 $\tau_{W}=0$ ；平凡化标记可用有限对数的导子提升调整。比较接口给 $O_{\mathrm{lt}}= \pm d_{2}\left(\tau_{\mathrm{ADE}}, 0\right)$ 。由（4．15）与 $h^{2}=1, d_{2}\left(T_{\mathrm{ADE}}^{1}\right)=0$ ，所以 $o_{\mathrm{lt}}=0$ 。

高维障碍空间只有三种：$j=0, k=5 ; j=0, k=6 ; j=1728, k=6$ 。设 ADE 总Tjurina 数为 $\tau_{\mathrm{ADE}}$ ，则 $h^{1}=37-\tau_{\mathrm{ADE}}+h^{2}$ 。 $j=0$ 时 $\tau_{\mathrm{ADE}}=48-2 k ; j=1728, k=6$时 $\tau_{\mathrm{ADE}}=36$ 。三者均得 $h^{1}=k-3$ 。

写 $B=b \prod\left(z-p_{i}\right)^{m_{i}}$ 或 $A=a \prod\left(z-p_{i}\right)^{m_{i}}$ 。固定三个不同根，移动其余 $k-3$个根，保持重数和首项系数。参数空间光滑。根附近单位因子可取 $m_{i}$ 次根吸入基底坐标，故 ADE 图确为解析局部产品，而非仅保持类型名称。Wahl 局部平凡性由前述Artin 结论给出。

若根运动的 Kodaira－Spencer 类为零，恢复接口使它来自无穷小射影基底变换$\xi(z) \partial_{z}(\operatorname{deg} \xi \leq 2)$ 和常值纤维缩放。对 $\dot{B} / B$ 或 $\dot{A} / A$ 在各根取留数，得到 $\dot{p}_{i}=-\xi\left(p_{i}\right)$ ，整体符号无关紧要。三个固定根迫使 $\xi=0$ ，全部根速度为零；故 Kodaira－Spencer 映射为同构。

设 Kuranishi 底环为 $\mathbb{C}\left[\left[t_{1}, \ldots, t_{d}\right]\right] / I, d=h^{1}$ 。实际光滑 $d$ 维家族给到 $\mathbb{C}\left[\left[s_{1}, \ldots, s_{d}\right]\right]$的映射，其线性部分可逆。形式逆函数定理使复合幂级数映射为同构，而 $I$ 在其核中，故 $I=0$ 。这控制完整非约化底环。 \(\square\)

将比较接口明列为条件，是为避免从 QG 无障碍性直接跳到另一形变函子。分析应用不能只引用三十八维这一数字。严格 lc 非商点也不能替换成自然光滑有限商轨形。

\section*{4．6．3 障碍泛函的解析冗余：可供分析使用的形式}

在同一小扩张比较接口下，不要求 $h^{2}=1$ ，已有 $o_{\mathrm{lt}} \in d_{2}\left(T_{\mathrm{ADE}}^{1}\right)$ ，因此 $\ell$ 杀掉每个实际障碍。对收敛 Kuranishi 映射 $f: H^{1} \rightarrow H^{2}$ ，记 $S=\mathbb{C}\left\{t_{1}, \ldots, t_{d}\right\} 、 \mathfrak{m}=(t)$ 、 $I=\left(f_{1}, \ldots, f_{r}\right)$ 。若采用该映射给出的通用小扩张障碍理论，则得到
$$\ell f \in \mathfrak{m} I, \quad \ell f(t)=a(t) f(t), \quad a(0)=0 .$$
其机制是：以 $S /\left(\mathfrak{m} I+\mathfrak{m}^{N+1}\right) \rightarrow S /\left(I+\mathfrak{m}^{N+1}\right)$ 为小扩张，$\ell$ 杀掉通用障碍，得到每个$N$ 上的理想包含；再由 Noether 局部环的 Krull 交定理恢复收敛理想关系。这比只在零点集合上消失更强。这里保留通用障碍识别前提，不宣称任意无限维非线性映射都有同样除法性质。

\section*{4.7 一般高度的对照计算与高度四的特殊性}

为说明该方法的结构，考虑同类光滑 Weierstrass 总空间，截面自交为 $-n, n \geq 3$ ，只收缩截面且 $K_{X}$ ample。其原始加权方程在 $\mathbb{P}(1,1,2 n, 3 n)$ 中次数为 $6 n$ 。

若 $n$ 奇数，该超曲面栈就是典范覆盖，典范线为 $\mathcal{O}(n-2)$ ，在 $\mu_{n}$ 上忠实。若$n=2 m$ 偶数，则典范覆盖为
$$V\left(a c-b^{2}, F_{6 m}\right) \subset \mathbb{P}(1,1,1,2 m, 3 m), \quad \omega=\mathcal{O}(m-1) .$$
局部为 $\left[A_{1} / \mu_{m}\right]$ 。局部平滑 $a c-b^{2}=t$ 在 $\mu_{m}$ 下不变，当且仅当 $m \mid 2 。 n \geq 3$ 中仅$n=4$ 允许这一方向。因此高度四的特点是局部允许 QG 平滑，而全局低次关系禁止它。

在上述完整模型假设下，同样的 Euler 与余切复形计算给
$$\operatorname{dim} T_{\mathrm{QG}}^{1}=10 n-2, \quad \operatorname{dim} T_{\mathrm{QG}}^{2}= \begin{cases}0, & n=3,4 \\ n-3, & n \geq 5\end{cases}$$
偶数 $n=2 m \geq 6$ 时不能只作维数相减。关键对偶映射为
$$H^{0} \mathcal{O}(m-3) \longrightarrow H^{2}(E)^{*}, \quad h \longmapsto h(c,-2 b, a) .$$
它落在 Euler 乘法的核中，因为 $a c h-2 b^{2} h+c a h=2 q h=0$ ；在 $\mathbb{C}[a, b, c] /(q)$ 整环中单射。故 $H^{2}(E) \rightarrow H^{2}(\mathcal{N})$ 满射，合法得到差值 $n-3$ 。奇数时差值直接为 $2(n-2)-(n-1)=$ $n-3$ 。

同次数方程可以逐小扩张提升，给平坦完全交族，故这个指定开集仍可形式光滑，即使自然完整障碍空间 $T^{2}$ 非零。这再次说明非零障碍空间本身不等于存在实际不可消去的障碍。式（4．17）不声称处理全部非正常或可约 KSB 紧化边界。

\section*{4.8 与实 Einstein 问题之间尚未建立的桥梁}

本支线值得保留的方法是：用完整典范分次找对覆盖栈；用最低次数的全局关系限制局部平滑；用普通一形式、唯一留数消去和 jet 插值独立计算障碍维数；用真实根运动与形式逆函数定理控制高阶底环。这些方法构成一个相对集中的代数几何研究方向。

但尚无定理说明：一个可能非 Kähler 的实 Einstein 度量，必定诱导本章所禁止的全局复平滑。即使排除趋向指定轨形的 Einstein 平滑，也不排除原流形上具有其他体积、其他极限或不参与该退化的度量。

固定负 Kähler－Einstein 外轨形的线性化也不能无条件假定可逆。光滑 Weierstrass、仅一个 Wahl 点的模型自然形变维数为三十八；标准负 Kähler－Einstein anti－Hermitian对应提示七十六个实核方向。把这变成紧轨形上的核维数及可积性结论，须在自然自伴定义域、等变 Dolbeault 理论与 KE 形变理论中落实。负 Ricci 排除 Killing 场并不排除 Einstein 形变核。本章不以这项标准对应的简称替代完整轨形分析证明。

全局复障碍、局部核以及随退化一致的逆估计，是不同的数学输入。任何一个维数计算或消失结论都不能单独结束原始 Ricci 夹逼问题。

\section*{第五章 规范理论饱和、临界分析与泡上的周期约束}

本章集中整理一条特定四维路线：从 Seiberg－Witten 曲率下界的近等号，提取负Kähler－Einstein 轨形极限及其非零全纯首项，再用曲率泡的周期检验这个首项。该路线研究的输入通常已经是精确 Einstein 度量；它与原问题中任意近 Einstein 输入的量词不同。全文把可以直接证明的恒等式、带明示前提的分析命题，以及尚待统一核验的应用接口分开陈述。档案中的＂独立复核＂不构成额外数学假设，也不代替证明。

\section*{5.1 固定对象、规范与两类不同的极限}

记 $N=Y(4)=W_{4,1}$ 为从椭圆曲面 $E(4)$ 沿一条自交数－4的截面作有理吹降所得的指定光滑流形。以下使用它的拓扑输入
$$\chi(N)=47, \quad \tau(N)=-31, \quad b_{1}(N)=0, \quad b_{+}(N)=7, \quad 2 \chi(N)+3 \tau(N)=1 .$$
该光滑型单连通、辛且不承载复结构；有平方为1的 monopole 类 $K$ ，其非零 Seiberg－Witten 基本类为 $\pm K$ 。这里＂基本类只有两个＂和＂全部 ordinary monopole 类只有两个＂不是同一陈述，后者需要下面的额外论证。 ${ }^{1}$

始终使用复定向，$W^{+}$作为 $\Lambda^{+}$上对称无迹算子的 Hilbert－Schmidt 范数；标量Laplacian 为 $\Delta=d^{*} d \geq 0$ 。若
$$\operatorname{Ric}\left(g_{j}\right)=-g_{j}, \quad d_{j}=\operatorname{Vol}\left(g_{j}\right)-2 \pi^{2} \longrightarrow 0, \quad \operatorname{diam}\left(g_{j}\right) \leq D,$$
则记 $s_{j}=\sqrt{d_{j}}$ 。此处 $s_{j}$ 是体积缺陷的平方根，绝不是 Ricci 方程误差；（5．2）的 Ricci误差精确为零。

本章还使用另一种输入：常标量曲率 -4 的显式逼近族，它在固定紧核上趋向某个指定负 KE 轨形，并以有理同调球填补唯一 Wahl 点。这种输入用于全部 monopole类的识别，不要求该逼近族是 Einstein。不能混用两种序列的已知性质。

\section*{5．2 Seiberg－Witten 缺陷与全部普通单极类}

\section*{5．2．1 精确缺陷恒等式与无规范极限}

取未扰动 Seiberg—Witten 解 $(A, \Phi)$ ，设 $y=|\Phi|^{2}$ ，采用
$$\left|F_{A}^{+}\right|^{2}=\frac{y^{2}}{8}, \quad 4 \int\left|\nabla_{A} \Phi\right|^{2}=\int\left(4 y-y^{2}\right), \quad 0 \leq y \leq 4 .$$
若行列式第一 Chern 类平方为1，Chern－Weil 公式给
$$\int y^{2}=32 \pi^{2}+8 \int\left|F_{A}^{-}\right|^{2}$$

\footnotetext{
${ }^{1}$ R．Fintushel and R．Stern，Six Lectures on Four 4－Manifolds，Lecture 4，§3，https：／／arxiv．org／pdf／math／0610700。该来源确认指定有理吹降光滑型及其 Seiberg－Witten 数据，不证明本章的体积间隙。
}

展开 $(4-y)^{2}$ ，得到
$$16\left(\operatorname{Vol}(g)-2 \pi^{2}\right)=\int(4-y)^{2}+8 \int\left|\nabla_{A} \Phi\right|^{2}+8 \int\left|F_{A}^{-}\right|^{2}$$
三个系数必须同时保留；这个等式只需标量曲率为－4。 ${ }^{2}$
命题5．1（SW饱和给出的 KE 极限）。设 $g_{j}$ 满足（5．2），并在有限点外光滑收敛到紧Einstein 轨形 $X$ ，总体积收敛至 $2 \pi^{2}$ 。则 $X$ 承载与极限定向相容的平行自对偶二形式，长度平方为2；因而该极限是负 KE 轨形。

证明。令 $\beta_{j}=-i F_{A_{j}}^{+}$；改变全套 Chern 符号只同时改变其正负。它是普通全局二形式，且
$$\left|\beta_{j}\right| \leq \sqrt{2}, \quad \int\left|\nabla \beta_{j}\right|^{2} \leq C d_{j}, \quad \int\left(\left|\beta_{j}\right|-\sqrt{2}\right)^{2} \leq 2 d_{j} .$$
第二条来自 SW二次型的微分界 $\left|\nabla \beta_{j}\right| \leq C\left|\Phi_{j}\right|\left|\nabla_{A_{j}} \Phi_{j}\right|$ 。在任意固定正则核心上，Rel－ lich 紧性给强 $L^{2}$ 子列；度量光滑收敛使极限满足分布方程 $\nabla \beta_{\infty}=0$ 。椭圆正则性及长度收敛给光滑、平行、长度 $\sqrt{2}$ 的自对偶形式。

在轨形覆盖球上，它有界且在穿孔球平行。半径 $r$ 的截断一阶误差至多 $C r^{-1} r^{4}= C r^{3}$ ，故平行方程延拓穿过中心。平行二形式定义平行正交复结构，因而可积。这个证明不需要比较全局旋量规范或跨颈拼接酉过渡函数。 \(\square\)

\section*{5．2．2 全部 ordinary monopole 类的饱和识别}

命题5．2（带固定外部收敛输入的全部类识别）。设 $N$ 单连通，$K^{2}=1, \pm K$ 是 ordinary monopole 类。另设存在常标量度量列 $g_{j}$ ，满足
$$\operatorname{Scal}\left(g_{j}\right)=-4, \quad V_{j} \rightarrow 2 \pi^{2}, \quad g_{j} \rightarrow g_{0} \text { 于 } C_{\text {loc }}^{\infty}\left(X_{\text {reg }}\right),$$
其中 $g_{0}$ 是固定负 KE 轨形。删去唯一Wahl点的邻域得紧核 $C$ ，要求
$$H^{2}(N ; \mathbb{R}) \stackrel{\cong}{\rightarrow} H^{2}(C ; \mathbb{R}),\left.\quad K\right|_{C}=\left[\omega_{0} /(2 \pi)\right] .$$
则全部 ordinary monopole 类恰为 $\{K,-K\}$ 。
证明。固定任意 ordinary 类 $a$ ，在同一 $g_{j}$ 上同时取 $a 、 K$ 的 SW 解。写实曲率 $f_{a, j}=$ $i F_{a, j} 、 f_{K, j}=i F_{K, j}$ ，使其除以 $2 \pi$ 代表相应类。最大值原理给 $\left|f^{+}\right| \leq \sqrt{2}$ ，而
$$\left\|f_{a, j}^{-}\right\|_{2}^{2}=\left\|f_{a, j}^{+}\right\|_{2}^{2}-4 \pi^{2} a^{2} \leq 2 V_{j}-4 \pi^{2} a^{2}=O_{a}(1) .$$
即使 $a^{2}<0$ ，仍有这个完整曲率 $L^{2}$ 界。另一方面（5．4）给 $\left\|f_{K, j}^{-}\right\|_{2} \rightarrow 0$ 。因此交叉配对
$$4 \pi^{2} a \cdot K=\int\left\langle f_{a, j}^{+}, f_{K, j}^{+}\right\rangle-\int\left\langle f_{a, j}^{-}, f_{K, j}^{-}\right\rangle$$

\footnotetext{
${ }^{2}$ C．LeBrun，Four－Manifolds，Curvature Bounds，and Convex Geometry，§3，https：／／arxiv．org／pdf／math ／0611450。（5．4）是标准 SW 规范下的直接重排。
}

推出 $|a \cdot K| \leq 1$ 。两个类均为特征类且 $H^{2}(N ; \mathbb{Z})$ 无挠，故 $a-K=2 x, a \cdot K$ 为奇整数。改变 $a$ 的符号后可设 $a \cdot K=1$ 。

记 $D_{j}=2-\left\langle f_{a, j}^{+}, f_{K, j}^{+}\right\rangle \geq 0$ 。上式饱和给 $\int D_{j} \rightarrow 0$ ，且
$$\left|f_{a, j}^{+}-f_{K, j}^{+}\right|^{2} \leq 2 D_{j}, \quad D_{j} \geq \frac{4-\left|\Phi_{a, j}\right|^{2}}{2} .$$
故 $\left|\Phi_{a, j}\right|^{2} \rightarrow 4$ 于 $L^{2}$ ，由 Weitzenböck 方程又有 $\left\|\nabla_{A_{a, j}} \Phi_{a, j}\right\|_{2} \rightarrow 0$ 。
还必须识别完整外部曲率，而不只其自对偶部分。在固定可缩正则球上，阿贝尔Coulomb 规范和曲率 $L^{2}$ 界给联络 $W^{1,2}$ 界；旋量点态界与协变导数界给普通 $W^{1,2}$ 界。联络强 $L^{3}$ 与旋量强 $L^{6}$ 收玫足以通过乘积项。极限旋量非零、平行，其二次型与 $K$ 的极限同向。

在 KE 球上，把这个局部 Spin ${ }^{c}$ 结构写成典范结构扭曲一条线丛。平行旋量落在度零或顶次线中，其平行性使行列式曲率分别等于自然典范曲率或其负；二次型方向固定了相同符号。故
$$f_{a, j}-f_{K, j} \rightharpoonup 0 \quad \text { 于 } L_{\mathrm{loc}}^{2}\left(X_{\mathrm{reg}}\right) .$$
也可先由局部 $d^{*} \oplus d^{+}$及 Dirac 方程作椭圆正则化，得到光滑极限后再作此识别。
与任意紧支撑于 $\operatorname{int} C$ 的闭二形式配对，得到 $\left.(a-K)\right|_{C}=0$ 。Poincaré－Lefschetz对偶及（5．5）给 $a=K$ 于实上同调；无挠性给整数类相等。恢复符号即得结论。 \(\square\)

该命题不用形式维数非负来排除负平方类。它真正需要固定外部 KE 收敛与紧核同调同构；仅知道 Yamabe 数值或标量曲率下确界不能替代这些输入。 ${ }^{3}$

\section*{5．2．3 体积窗及其不足}

SW 标量不等式与非复性给 $V>2 \pi^{2}$ 。Einstein Chern－Weil 公式给
$$\int_{N}\left|W^{+}\right|^{2}=2 \pi^{2}-\frac{V}{3}, \quad 2 \pi^{2}<V \leq 6 \pi^{2} .$$
识别全部 ordinary 类并不进一步缩窄这个区间。若 $x=V /\left(2 \pi^{2}\right) 、 q=-\left(K_{g}^{-}\right)^{2}$ ，LeBrun曲率不等式与 Cauchy—Schwarz 给
$$1+q \leq \frac{7 x+3+4 \sqrt{2 x(3-x)}}{18}, \quad 1<x \leq 3 .$$
其右边在整个允许区间均至少为 1，所以 $q=0$ 始终相容，不能迫使 $x \rightarrow 1$ 。
更精确地，单个正类的投影控制不能使整个 Hodge 正平面紧致。在交叉形式的正交基 $K, e_{1}, \ldots, e_{6}, f_{1}, \ldots, f_{38}$ 中，令
$$H_{t}=\operatorname{span}\left\{K, \cosh t e_{1}+\sinh t f_{1}, e_{2}, \ldots, e_{6}\right\} .$$
则 $K_{H_{t}}^{-}=0$ ，但 $\left\|e_{1}\right\|_{H_{t}}^{2}=\cosh (2 t) \rightarrow \infty$ 。这是有限维二次空间上的阻碍检验，不声称每个 $H_{t}$ 都由 Einstein 度量实现。

\footnotetext{
${ }^{3}$ ordinary 与 special monopole 类的区分见 D．Kotschick，Monopole classes and Einstein metrics，Definitions 1 and 3，https：／／arxiv．org／pdf／math／0306022。
}

\section*{5.3 自对偶曲率的全局控制：为何允许另一半曲率集中}

在（5．2）下，Bishop－Gromov 比较由正体积下界和直径界给统一局部非塌缩及
$$\|u\|_{4}^{2} \leq S(D)\left(\|d u\|_{2}^{2}+\|u\|_{2}^{2}\right) .$$
固定拓扑和 Einstein Gauss－Bonnet 公式给完整曲率 $L^{2}$ 界。四维 Einstein 紧性给有限孤立奇点的紧轨形极限。 ${ }^{4}$

命题5．1给极限 KE，故其 $W^{+}$特征值为（－2／3，1／3，1／3）。（5．6）与极限体积相结合得到
$$\lim _{j} \int_{N}\left|W_{g_{j}}^{+}\right|^{2}=\frac{4 \pi^{2}}{3}=\int_{X}\left|W_{g_{0}}^{+}\right|^{2}$$
正则核心已耗尽全部 $W^{+}$能量，所以没有自对偶能量落入奇点。
引理5．3（闭合的半曲率方程及一阶升级）。对上述序列，在去掉有限个初始项后有
$$\left\|W_{j}^{+}\right\|_{\infty} \leq C, \quad\left\|\nabla W_{j}^{+}\right\|_{\infty} \rightarrow 0, \quad \operatorname{spec}\left(W_{j}^{+}\right) \rightarrow(-2 / 3,1 / 3,1 / 3) \quad \text { 一致. }$$
这些估计允许 $W_{j}^{-}$无界。
证明．Einstein Weyl 方程闭合为
$$\nabla^{*} \nabla W^{+}=2 W^{+}+6\left(W^{+}\right)^{2}-2\left|W^{+}\right|^{2} I .$$
Kato 与（5．8）的局部 Moser 估计表明，小 $L^{2}$ 自对偶能量球上有 $\sup \left|W^{+}\right| \leq C\left(r^{-2}+\right.$ $1)\left\|W^{+}\right\|_{2}$ 。无原子能量极限及小球体积上界允许选固定半径覆盖，给全局 $W^{+}$界。积分（5．9）得
$$\int\left|\nabla W^{+}\right|^{2}=2 \int\left|W^{+}\right|^{2}+18 \int \operatorname{det} W^{+} \rightarrow 0 .$$
最后一个极限使用已经得到的点态界来排除三次积分的浓缩。
把 $W^{+}$当作 $\operatorname{Sym}_{0}^{2} \Lambda^{+}$的零形式，记 $U_{k}=\nabla_{k} W^{+}$。取 $\mathcal{D}=\nabla^{i} \nabla_{i}$ ，首次交换为
$$\mathcal{D} U_{k}=\nabla_{k} \mathcal{D} W^{+}+\operatorname{Ric}_{k}{ }^{\ell} U_{\ell}+2 F_{i k}^{E} U_{i}+\left(\nabla^{i} F_{i k}^{E}\right) W^{+} .$$
新出现的唯一底空间协变指标经收缩只给 Ricci。 $\Lambda^{+}$联络曲率只含 $W^{+}$＋Scal I／12； Einstein 条件使它自对偶，Bianchi 因而给 Yang－Mills 方程。于是 $\left|\nabla^{*} \nabla U\right| \leq C|U|$ ，全局 Moser 给 $\|U\|_{\infty} \leq C\|U\|_{2} \rightarrow 0$ 。沿长度至多 $D$ 的曲线与一个正则基点比较，得到全局谱收敛。 \(\square\)

上述简化只适用于第一次交换。继续对多协变指标张量求导，不能再默认完整 Rie－ mann 曲率消失。 ${ }^{5}$

最低特征线有统一谱隙；单连通性使其可定向。取全局 $\omega_{j}$ 满足 $\left|\omega_{j}\right|^{2}=2$ ，记相应近复结构为 $J_{j}$ 。此时 $\left\|\nabla \omega_{j}\right\|_{\infty} \rightarrow 0$ 。所有非平坦曲率泡均 Ricci－flat 且 $W^{+}=0$ ，这是自对偶能量账本的后果，不是预设泡型。

\footnotetext{
${ }^{4}$ M．Anderson，A Survey of Einstein Metrics on 4－Manifolds，Theorem 5.3 and §5，https：／／arxiv．org／pdf／0810．4830。此处使用的是非塌缩 Einstein 轨形紧性，不是一般有界 Ricci 序列的光滑紧性。
${ }^{5}$ Weyl 方程及精确谱刚性阈值可参见 X．Li and Y．Zhang，Kählerity of Einstein Four－Manifolds，§2，https：／／arxiv．org／pdf／2206．04870。本章不把 $\lambda_{2} \rightarrow 1 / 3$ 替换为其刚性定理要求的逐点 $\lambda_{2} \geq 1 / 3$ 。
}

\section*{5.4 闭典范形式、Hodge 投影与精确体积账本}

\section*{5．4．1 无需二形式谱隙的 Hodge 修正}

局部补全 quaternionic 标架 $\left(\omega_{1}, \omega_{2}, \omega_{3}\right), \omega_{1}=\omega$ ，各长度平方为2。写
$$\nabla \omega_{1}=b \otimes \omega_{2}+c \otimes \omega_{3}, \quad \nabla \omega_{2}=-b \otimes \omega_{1}+a \otimes \omega_{3}, \quad \nabla \omega_{3}=-c \otimes \omega_{1}-a \otimes \omega_{2} .$$
投影典范线联络的曲率给全局闭形式
$$\Omega=d a=(1+q) \omega-b \wedge c, \quad[\Omega /(2 \pi)]=K_{J}, \quad\left|\Omega^{-}\right| \leq \frac{1}{4}|\nabla \omega|^{2},$$
其中最低特征值写为 $\lambda_{1}=-2 / 3-q$ 。局部 $d a$ 不意味着全局 exact ；此处 $a$ 只是局部联络一形式。 $\Omega$ 一致接近 $\omega$ ，因而最终是驯服 $J$ 的真实辛形式。

写 Hodge 分解 $\Omega=\alpha+d \xi$ ，令 $\psi=\alpha^{+}$。Stokes 与正交性给
$$\left\|(d \xi)^{+}\right\|_{2}=\left\|(d \xi)^{-}\right\|_{2}, \quad\left\|\psi-\Omega^{+}\right\|_{2} \leq\left\|\Omega^{-}\right\|_{2}, \quad\left\|\alpha^{-}\right\|_{2} \leq\left\|\Omega^{-}\right\|_{2} .$$
这里没有使用二形式 Laplacian 的正谱下界。对 $\psi$ 的 Weitzenböck 方程与一次交换给点态及一阶控制，结合直径界把 $L^{2}$ 接近提升为一致接近。因此 $\psi$ 无零点，
$$u=|\psi|_{g} / \sqrt{2}, \quad \widehat{g}=u g$$
使 $(\widehat{g}, \psi)$ 为 almost－Kähler，且 $u \rightarrow 1$ 一致。 $\psi$ 一般不代表整个 $2 \pi K_{J}$ ，整类的代表是$\alpha$ ；后面的公式保留 $\alpha^{-}$。

命题5．4（四项体积缺陷恒等式）。设 $\operatorname{Scal}(g)=-4, K^{2}=1, \alpha$ 为 $2 \pi K$ 的调和代表， $\psi=\alpha^{+}$无零点，且其诱导近复结构的典范类为 $K$ 。定义 $u=|\psi|_{g} / \sqrt{2} 、 \widehat{g}=u g$ 。则
$$V-2 \pi^{2}=\|u-1\|_{2}^{2}+3\|d \sqrt{u}\|_{2}^{2}+\frac{1}{4} \int|\widehat{\nabla} \psi|_{\widehat{g}}^{2} d V_{\widehat{g}}+\frac{1}{2}\left\|\alpha^{-}\right\|_{2}^{2}$$
右边未标明的范数相对于 $g$ 。
证明．记 $U_{1}=\int u 、 U_{2}=\int u^{2} 、 R=\left\|\alpha^{-}\right\|_{2}^{2} 、 H=\|d \sqrt{u}\|_{2}^{2} 、 T=\int|\widehat{\nabla} \psi|^{2}$ 。Hodge 交叉形式给 $2 U_{2}-R=4 \pi^{2}$ 。almost－Kähler 典范联络的积分公式及 $c_{1}(T N)=-K$ 给
$$\int\left(\operatorname{Scal}(\widehat{g})+\frac{1}{2}|\widehat{\nabla} \psi|^{2}\right) d V_{\widehat{g}}=-4 U_{2}$$
共形标量公式则为 $\int \operatorname{Scal}(\widehat{g}) d V_{\widehat{g}}=6 H-4 U_{1}$ ，故 $U_{1}-U_{2}=3 H / 2+T / 8$ 。代人 $\int(u-1)^{2}=$ $U_{2}-2 U_{1}+V$ 即得结论。 \(\square\)

\section*{5．4．2 负 Weyl 符号允许的能量平衡}

在 $\widehat{g}$ 下相对于 $\psi$ 分块写
$$W^{+}=\left(\begin{array}{cc}
a & v^{\top} \\
v & -a I / 2+\widehat{B}
\end{array}\right), \quad \operatorname{tr} \widehat{B}=0, \quad w=W^{+}(\psi, \psi)=2 a, \quad t=|\widehat{\nabla} \psi|^{2} .$$

Einstein 共形类的加权 Weyl 恒等式与 $w-\widehat{\mathrm{Scal}} / 3=t / 2$ 给
$$\int\left(|v|^{2}+|\widehat{B}|^{2}\right) u^{-1 / 2} d V_{\widehat{g}}=-\frac{3}{16} \int w t u^{-1 / 2} d V_{\widehat{g}}$$
其共形权重是 $u^{-1 / 2}$ 。在当前 $w \rightarrow-4 / 3$ 的符号下，右端允许正能量；不能用于直接消灭扭率。 ${ }^{6}$

命题5．5（近下端 Einstein 序列的首阶能量比例）。在（5．2）、（5．1）及以上全局谱和Hodge 构造下，写
$$\lambda_{1}=-\frac{2}{3}-q, \quad \lambda_{2}=\frac{1}{3}+\frac{q}{2}-b, \quad \lambda_{3}=\frac{1}{3}+\frac{q}{2}+b, \quad b \geq 0 .$$
则
$$\frac{\int b_{j}^{2}}{d_{j}} \rightarrow \frac{1}{2}, \quad \frac{\int\left|\nabla W_{j}^{+}\right|^{2}}{d_{j}} \rightarrow 10, \quad \frac{\int\left|\nabla \omega_{j}\right|^{2}}{d_{j}} \rightarrow 4, \quad \frac{\int\left|d \omega_{j}\right|^{2}}{d_{j}} \rightarrow 0,$$
且
$$\left\|q_{j}\right\|_{\infty} \leq C d_{j}, \quad\left\|b_{j}\right\|_{\infty}+\left\|\nabla W_{j}^{+}\right\|_{\infty}+\left\|\nabla \omega_{j}\right\|_{\infty} \leq C \sqrt{d_{j}} .$$
证明．令 $B_{2}=\int b^{2} 、 Q=\int q^{2} 、 G=\int\left|\nabla W^{+}\right|^{2}$ 。（5．13）先给 $\widehat{T} \leq 4 d$ ；（5．14）再给$B_{2} \leq C d$ 。拓扑公式及 Weyl 方程精确为
$$\begin{aligned}
2 \int q & =-d-\frac{3}{2} Q-2 B_{2} \\
G & =d+\frac{9}{2} \int(1+q)\left(4 b^{2}-q^{2}\right)
\end{aligned}$$
所以 $G \leq C d$ 。引理 5.3 的一阶估计和谱间隙给导数 $O(\sqrt{d})$ ；结合直径界及 $B_{2} \leq C d$得 $\|b\|_{\infty}=O(\sqrt{d})$ 。

令 $\nu=\omega / \sqrt{2}$ 。最低特征值的二阶微分公式给
$$(\Delta+2) q=4 b^{2}-3 q^{2}-2 \sum_{k=2,3}\left(\lambda_{k}-\lambda_{1}\right)\left|(\nabla \nu)_{k}\right|^{2}$$
对 $\Delta+2$ 用最大值估计，借助已知 $q \rightarrow 0$ 吸收平方项，得 $\|q\|_{\infty}=O(d)$ 。这里的正质量只属于径向变量，不能扩展到全部横向模式。
（5．11）－（5．12）于是给 $\left\|\alpha^{-}\right\|_{2}+\|u-1\|_{2}=O(d)$ ，$\psi$ 与最低轴夹角的 $L^{2}$ 范数也是$O(d)$ 。其 Weitzenböck 方程及首次交换给 $\|\nabla \psi\|_{\infty}=O(\sqrt{d})$ ；夹角一致为 $O(\sqrt{d})$ 。设$\mu=\left\langle W^{+} \psi, \psi\right\rangle /|\psi|^{2}$ ，则 $\mu+2 / 3=O(d)$ ，且
$$2 u \Delta u=4 u^{2}(\mu+2 / 3)-|\nabla \psi|^{2}+2|d u|^{2} .$$
故 $\|\Delta u\|_{\infty}=O(d)$ ，分部积分给 $\int|d u|^{2}=\int(u-1) \Delta u=O\left(d^{2}\right)$ 。四项体积公式成为$\widehat{T}=4 d+O\left(d^{2}\right)$ 。

\footnotetext{
${ }^{6}$ C．LeBrun，Einstein Metrics，Harmonic Forms，and Symplectic Four－Manifolds，equation（3），https： ／／arxiv．org／pdf／1408．1078。分块中 $|W|^{2}=3 a^{2} / 2+2|v|^{2}+|\widehat{B}|^{2},\left|W(\psi)^{\perp}\right|^{2}=2|v|^{2}$ ，代人即得系数 $-3 / 16$ 。
}

分块式中 $\int|v|^{2}=O\left(d^{2}\right), \int|\widehat{B}|^{2}=2 B_{2}+O\left(d^{2}\right)$ ；（5．14）因而给 $B_{2}=d / 2+o(d)$ 。代入（5．18）给 $G=10 d+o(d)$ 。积分（5．19）并用（5．17），得到
$$2 \int \sum_{k>1}\left(\lambda_{k}-\lambda_{1}\right)\left|(\nabla \nu)_{k}\right|^{2}=d+6 B_{2}-\frac{3}{2} Q .$$
谱间隙趋于1，故 $\int|\nabla \omega|^{2}=4 d+o(d)$ 。最后对自对偶 $\omega$ 的 Hodge－Weitzenböck 公式给精确式
$$d+\|d \omega\|_{2}^{2}+\frac{3}{2} Q+2 B_{2}=\frac{1}{2}\|\nabla \omega\|_{2}^{2},$$
于是 $\|d \omega\|_{2}^{2}=o(d)$ 。所有步骤按上述顺序进行，不预先使用待证比例。 \(\square\)

这些正能量比例本身完全相容，不构成矛盾。它们的作用是约束任何实际匹配首项；例如 $\int b^{2}=o(d)$ 与这条特定序列的必要条件不相容。

\section*{5.5 从非平行性提取非零全纯张量}

记 $A_{j}=\nabla \omega_{j} / s_{j}$ 。（5．16）给全局点态界，在固定正则核心上的齐次方程给全部局部导数界。奇点小球体积 $O\left(r^{4}\right)$ ，所以归一化能量不会藏入泡。取极限得
$$\int_{X}\left|A_{\infty}\right|^{2}=4, \quad \text { Alt } A_{\infty}=0, \quad A_{\infty} \in T^{*} X \otimes \omega_{0}^{\perp} .$$
在复维2，交替化 $\Lambda^{0,1} \otimes \Lambda^{2,0} \rightarrow \Lambda^{2,1}$ 是同构，因而
$$A_{\infty}=\sigma+\bar{\sigma}, \quad \sigma \in \Omega^{1,0} \otimes K_{X} .$$
Einstein 条件与最低特征线给实际精确恒等式
$$R_{g_{j}}^{\Lambda^{+}}(Z, \bar{U}) \omega_{j}=0 .$$
右端在除以 $s_{j}$ 前已经为零。将 $d_{\nabla} \nabla \omega=R^{\Lambda^{+}} \omega$ 传极限，按 $\Lambda^{2,0}$ 和 $\Lambda^{0,2}$ 类型分别比较，得到 $\nabla^{0,1} \sigma=0$ 。在轨形覆盖中用 Hartogs 延拓。

若把正旋量的极限分块写为 $\left(\begin{array}{cc}0 & b_{1} \\ -b_{1}^{*} & 0\end{array}\right)$ ，并固定 $|\nabla \omega|^{2}=8|b|^{2}$ 的规范，则得到
$$b_{1} \in \mathcal{H}_{X}:=H_{\mathrm{orb}}^{0}\left(X, \Omega^{1} \otimes K_{X}\right), \quad\left\|b_{1}\right\|_{2}^{2}=\frac{1}{2} .$$
外部横向 $W^{+}$首项与 $\partial_{K} b_{1}$ 通过固定非零表示同构对应。判断消失时不需要选取这个表示的数值常数。

说明5．6。（5．21）对一般近 Einstein 度量会出现 $O\left(\left|\mathrm{Ric}_{0}\right|\right)$ 源；除以 $s_{j}$ 后不必消失。因此不能把本节的全纯首项定理直接应用于原题任意 Ricci 夹逼序列。至少需要另证误差相对于体积缺陷的速率以及其余紧性输入。

\section*{5.6 可重复使用的临界分析工具}

\section*{5．6．1 有界曲率西丛的梯度估计：把系数导数放回散度}

命题5．7。设闭四流形满足（5．8），$E$ 带西联络，且 $\|\operatorname{Ric}\|_{\infty} \leq K_{R} 、\left\|F^{E}\right\|_{\infty} \leq K_{F}$ 。若$\nabla^{*} \nabla u=H$ ，则
$$\|\nabla u\|_{\infty} \leq C\left(S, K_{R}, K_{F}\right)\left(\|\nabla u\|_{2}+\|H\|_{\infty}+K_{F}\|u\|_{\infty}\right) .$$
不需要 $\nabla H 、 \nabla F^{E}$ 或完整 Riemann 曲率的一致界。
证明．令 $U=\nabla u$ 。首次交换可整理为
$$\nabla^{*} \nabla U=\nabla^{*} T+A U, \quad T_{i j}=-g_{i j} H+F_{i j}^{E} u, \quad(A U)_{j}=-\operatorname{Ric}_{j}{ }^{k} U_{k}-F_{i j}^{E} U^{i} .$$
因此 $A$ 有界而 $|T| \leq C\left(|H|+K_{F}|u|\right)$ 。系数导数只出现在散度里。
对一般度量联络丛上的这个方程，令 $w=|U| 、 v=(w-k)_{+}$，在 $\{w>k\}$ 写$U=w e 、|e|=1$ 。以 $(v / w) U$ 测试，主项精确为
$$|d v|^{2}+\frac{v}{w} w^{2}|\nabla e|^{2} .$$
散度源的角向项自带 $v / w$ ，可由第二个非负项吸收，没有 $w / v$ 损失。得到
$$\left\|(w-k)_{+}\right\|_{4}^{2} \leq C \int_{\{w>k\}}\left(|T|^{2}+w^{2}\right)$$
对分布函数作 dyadic 求和并吸收足够小的固定体积尾，得到
$$\|U\|_{\infty} \leq C\left(S,\|A\|_{\infty}\right)\left(\|U\|_{2}+\|T\|_{L^{4,1}}\right) .$$
更局部的重排项为 $\int_{0}^{t_{0}} r^{-3 / 4}|T|^{*}(r) d r$ ；对有界 $T$ 不超过 $4 t_{0}^{1 / 4}\|T\|_{\infty}$ 。这给（5．23），不要求总体积上界。应用于 $T^{*} M \otimes E$ 时无需控制该新丛的曲率，因为测试证明不再作曲率交换。 \(\square\)

\section*{5．6．2 完整有限泡树上的 Hessian 临界指数}

若在固定有限非塌缩 Einstein 泡树上，已知 $\left\|\nabla W_{j}^{+}\right\|_{\infty} \leq C s_{j}$ 、最低轴谱隙统一，且第一次交换后为有界系数齐次方程，则每个物理正则尺度 $r$ 的块上
$$\left|\nabla^{2} J_{j}\right| \leq C s_{j} / r .$$
在累积物理尺度 $a_{v, j}$ 的节点核心上，$p$ 次积分代价为 $C_{p} s_{j}^{p} a_{v, j}^{4-p}$ ；在颈上是 $C_{p} s_{j}^{p} \sum_{k} r_{k}^{4-p}$ 。因此
$$\left\|\nabla^{2} J_{j}\right\|_{L^{p}} \leq C_{p} s_{j} \quad(1 \leq p<4), \quad\left\|\nabla^{2} J_{j}\right\|_{L^{4, \infty}} \leq C s_{j} .$$
常数依赖固定有限树和模型。强 $L^{4}$ 估计一般只能由这项计算得到
$$\left\|\nabla^{2} J_{j}\right\|_{4}^{4} \leq C s_{j}^{4}\left(1+\sum_{u \rightarrow v} \log \frac{a_{u, j}}{a_{v, j}}\right) .$$
它没有给强 $L^{4,1}$ ，也没有证明实际例子一定达到对数增长。节点尺度必须使用累积物理尺度，不能以父子相对尺度替代。 ${ }^{7}$

\footnotetext{
${ }^{7}$ 低能量颈的受控缩放图和实际非塌缩 Einstein 退化框架见 T．Ozuch，Noncollapsed degeneration of Einstein4－manifolds I，§2，https：／／arxiv．org／pdf／1909．12957v2。（5．25）的尺度求和在本文显示。
}

\section*{5．6．3 固定复轨形上的 Lorentz－Kuranishi 回缩}

在固定紧光滑复二维轨形上，令 $D=\bar{\partial} 、 H_{q}$ 为 Dolbeault 调和投影、 $G_{q}$ 为其 Green算子，设
$$\mathcal{B}=W^{1,(4,1)}\left(\Lambda^{0,1} \otimes T^{1,0}\right), \quad \mathcal{Y}=L^{4,1}\left(\Lambda^{0,2} \otimes T^{1,0}\right), \quad F(\mu)=D \mu+\frac{1}{2}[\mu, \mu] .$$
临界嵌人 $\mathcal{B} \hookrightarrow C^{0} 、 B=D^{*} G_{2}: \mathcal{Y} \rightarrow \mathcal{B}$ 的有界性及
$$\|[u, v]\|_{\mathcal{Y}} \leq C\|u\|_{\mathcal{B}}\|v\|_{\mathcal{B}}$$
使 $\mathcal{K}(\mu)=\mu+\frac{1}{2} B[\mu, \mu]$ 在原点附近解析可逆。这里所有常数属于固定背景，不是退化族的一致常数。 ${ }^{8}$

命题5．8（条件性的缺陷投影与可积回缩）。若光滑 Kuranishi 障碍映射 $f: H^{1} \rightarrow H^{2}$满足某个固定泛函的解析冗余 $\ell f(h)=a(h) f(h) 、 a(0)=0$ ，则对小 $\mu \in \mathcal{B}$ 且 $D^{*} \mu=0$ ，有
$$\left|\ell H_{2} F(\mu)\right| \leq C\|\mu\|_{\mathcal{B}}\|F(\mu)\|_{\mathcal{Y}} .$$
若更强地，光滑 Dolbeault 形变问题在全部 Artin 小扩张上的实际障碍均为零，则不要求 $\mu$ 处于 Coulomb 规范：存在 $F(\nu)=0$ ，使
$$\|\nu\|_{\mathcal{B}} \leq C\|\mu\|_{\mathcal{B}}, \quad\|\mu-\nu\|_{\mathcal{B}} \leq C\|F(\mu)\|_{\mathcal{Y}}, \quad D^{*}(\mu-\nu)=0 .$$
光滑输入给光滑 $\nu$ ；不声称其高阶范数一致。
证明。复维2给 $D B=1-H_{2}$ 。若 $D^{*} \mu=0$ ，Hodge 分解为 $\mathcal{K}(\mu)=H_{1} \mu+B F(\mu)$ 。与$\nu=\mathcal{K}^{-1}\left(H_{1} \mu\right)$ 比较，逆映射 Lipschitz 界给 $\|\mu-\nu\|_{\mathcal{B}} \leq C\|F(\mu)\|_{\mathcal{Y}} 。 H_{2} D=0$ 和二次括号差估计，再加解析冗余，给（5．26）。

无障碍情形取闭方向投影 $P_{Z}=H_{1}+D G_{0} D^{*}$ ，则 $\mathcal{K}(\mu)=P_{Z} \mu+B F(\mu)$ 。对光滑闭 $v, F\left(\mathcal{K}^{-1}(t v)\right)$ 是调和值解析函数。若低于 $n$ 阶系数均为零，第 $n$ 阶系数就是一个Artin 小扩张的实际障碍，故为零。归纳及解析性给整个函数为零；再以光滑稠密性推广到 $\mathcal{B}$ 。取 $\nu=\mathcal{K}^{-1}\left(P_{Z} \mu\right)$ 即得误差界。 $D^{*} B=0$ 且 $D^{*} P_{Z}=D^{*}$ 给残差自动 Coulomb。

若输入光滑，方程 $\nu+B\left(\frac{1}{2}[\nu, \nu]\right)=P_{Z} \mu$ 可先在固定 $W^{1,4}$ 与 $W^{1,16}$ 中冻结小的连续系数并用 Neumann 反演，取得 $\nu \in W^{1,16}$ 。系统 $\left(D \nu+\frac{1}{2}[\nu, \nu], D^{*} \nu\right)=\left(0, D^{*} \mu\right)$ 是小扰动的一阶椭圆系统；Schauder 迭代给光滑性。 \(\square\)

自然光滑商轨形的 Dolbeault 复形与 QG 形变所用的奇异典范覆盖栈不是同一对象。上述 Artin 输入必须由代数章节提供准确映射，不能由＂某个 Wahl参数不可平滑＂直接替代。 ${ }^{9}$

\footnotetext{
${ }^{8}$ 端点嵌入见 A．Alberico，A．Cianchi，L．Pick and L．Slavíková，Sharp Sobolev type embeddings on the entire Euclidean space，Corollary 3．2，https：／／arxiv．org／pdf／1711．11549。Green 算子界来自固定背景椭圆估计的实插值。
${ }^{9}$ Artin 障碍的 Maurer－Cartan 描述见 M．Manetti，Lectures on deformations of complex manifolds，Chapters IV－V，https：／／arxiv．org／pdf／math／0507286。
}

若一个零截断延拓 $\widetilde{\mu}_{j}$ 满足 $e_{j}=\left\|\widetilde{\mu}_{j}\right\|_{\mathcal{B}} \rightarrow 0$ ，外部与在 Wahl 点线性消失的对偶测试的配对为 $A s_{j}+o\left(s_{j}\right), A \neq 0$ ，则 Lorentz 对偶给
$$\left\|F\left(\widetilde{\mu}_{j}\right)\right\|_{\mathcal{Y}} \geq \frac{c s_{j}}{e_{j}+r_{j}^{4}} .$$
如果截断计算另给该缺陷不超过 $C\left(s_{j}+m_{j}\right)$ ，则 $m_{j} \geq c s_{j} /\left(e_{j}+r_{j}^{4}\right)$ 。这说明环带振幅不能为 $O\left(s_{j}\right)$ ，但 $m_{j} \rightarrow 0$ 与 $m_{j} / s_{j} \rightarrow \infty$ 可以同时成立；它不自动确定物理泡参数。

\section*{5．6．4 低次典范 Dirac 谱隙与近似乘法}

固定 Levi－Civita 的 $U(2)$ 投影 $\nabla^{U}=\nabla-\frac{1}{2} J(\nabla J)$ ，在
$$S_{m}=\Lambda^{0, *} \otimes K^{m}, \quad L_{m}=K^{2 m-1}$$
上使用其诱导行列式联络和 Levi－Civita Clifford 联络。它与度数保持联络的差只升降两个次数，大小为 $O(|\nabla J|)$ 。投影曲率恒等式为
$$F^{K}=-\operatorname{Tr}\left\{P_{10} R^{T M} P_{10}+P_{10}\left(\nabla P_{10} \wedge \nabla P_{10}\right) P_{10}\right\}, \quad P_{10}=(I-i J) / 2 .$$
没有独立的 $\nabla^{2} J$ 项。Einstein 最低轴条件及（5．16）给 $i F^{K}=\omega+O\left(s_{j}^{2}\right)$ ，正旋量完整联络曲率有界，Lichnerowicz 势的跨度数部分为 $O\left(s_{j}^{2}\right)$ 。不能把这个完整曲率结论推广到负旋量，因为后者看见 $W^{-}$。 ${ }^{10}$

假设固定极限满足 $H^{0,1}\left(K_{X}^{m}\right)=0, m=1,2$ 。若奇 Dirac 算子没有一致谱隙，取单位低特征旋量。Lichnerowicz 有界势和统一Sobolev 常数给点态界，因而其质量不落入体积趋零的奇点邻域。正则核心极限及可去奇性产生非零元素 $H^{0,1}\left(K_{X}^{m}\right)$ ，矛盾。故存在 $\lambda_{m}>0$ ，使
$$\left\|\mathcal{D}_{m, j}^{-} \psi\right\|_{2}^{2} \geq \lambda_{m}\|\psi\|_{2}^{2} .$$
它依赖指定极限，绝非维数统一谱隙。指标
$$\operatorname{ind} \mathcal{D}_{m, j}^{+}=\frac{(2 m-1)^{2}-\tau(N)}{8}=4+\frac{m(m-1)}{2}$$
因而给偶核维数4，5。第一数是旋量核维数，不能写成三个典范截面的维数。 $m=1$ 时顶次线 $\bar{K} \otimes K$ 有自然平行投影截面 $\tau$ ；对顶次平均取核后，才能分离三维近似典范截面空间。

在同一个低次核、自然乘积法则和极限典范乘法输入下，可选三个截面 $\alpha_{i, j}$ 及秩3 二次型 $q_{j} \rightarrow q_{0}$ ，使
$$\left\|\bar{\partial}_{J} \alpha_{i, j}\right\|_{2}=O\left(s_{j}\right), \quad\left\|q_{j}\left(\alpha_{j}\right)\right\|_{W^{1,2}}+\left\|q_{j}\left(\alpha_{j}\right)\right\|_{4}=O\left(s_{j}\right) .$$
使用命题5．7、被收缩的迹方程及核正交逆，可进一步控制顶次分量 $\beta_{i}$ 及关系 $r=q_{j}\left(\alpha_{j}\right)$的点态和全梯度为 $O\left(s_{j}\right)$ 。这些升级要求实际源方程，不从投影的有限维性自动得出。

\footnotetext{
${ }^{10}$ 指定联络及 Clifford 次数分解可对照 X．Ma and G．Marinescu，The Spin ${ }^{c}$ Dirac operator on high tensor powers of a line bundle，§2，https：／／arxiv．org／pdf／math／0111138。本节不使用其高幂谱定理来代替低次幂论证。
}

该方法没有使关系误差变为 $O\left(s_{j}^{2}\right)$ 。在正旋量块 $\nabla^{S_{1}^{+}}=\left(\begin{array}{cc}\nabla^{K} & b \\ -b^{*} & d\end{array}\right)$ 中，$|b|=O\left(s_{j}\right)$ ，迹方程可给 $\left(\nabla^{K}\right)^{*} b=O\left(s_{j}^{2}\right)$ ，但完整 $\nabla b$ 不一定二阶小。归一化后仍留下 $\Delta B_{i}=-2 b_{1}^{*} \cdot \nabla A_{i}$的一阶响应，这正是（5．35）的来源。核正交让逆可用，不会把残差平方；局部源变小也不控制核心常数模。主链的周期证明后来绕开了实际三截面匹配，但这些固定低次核与响应工具仍有独立用途。

\section*{5.7 外部 Green－Jacobi 模式与真正能量的边界}

这一部分保留了长期局部匹配研究中有独立内容的线性构造。固定一个负 KE 轨形 $X$ ，Wahl 点光滑覆盖为 $\mathbb{C}^{2} / \mu_{4}$ ，作用 $(u, v) \mapsto(i u, i v), g=e+O\left(r^{2}\right)$ 。置 $R=|u|^{2}+|v|^{2}$ ，定义
$$A_{Q}=R^{-3}\left(\begin{array}{cc}
-\bar{v}^{2} & \bar{u} \bar{v} \\
\bar{u} \bar{v} & -\bar{u}^{2}
\end{array}\right) \in \Omega^{0,1}\left(T^{1,0}\right) .$$
其大小为 $r^{-4}$ ；在平坦穿孔模型上对称、 $\bar{\partial}$ 闭且 $\bar{\partial}^{*}$ 闭。取截断 $\chi$ ，令 $F=\bar{\partial}\left(\chi A_{Q}\right)$ 。 $F$支撑在固定环带，光滑延拓，设它的调和投影 $\eta=H_{2} F \neq 0$ 。 $\eta$ 与 Wahl QG 障碍的识别是独立代数输入，不包含在下面的解析构造中。

命题5．9（给定非零连接类的奇异外部延拓）。上述输入下，可构造穿孔 $X$ 上的张量$\alpha_{Q}$ ，满足
$$\alpha_{Q}=A_{Q}+O\left(r^{-2}\right), \quad \bar{\partial} \alpha_{Q}=\eta, \quad \bar{\partial}^{*} \alpha_{Q}=0, \quad \Delta_{\bar{\partial}, T} \alpha_{Q}=0 .$$
降低向量指标后它对称，因而对应真实 anti－Hermitian、TT 的 Jacobi 张量。有限的是
$$\int_{X \backslash\{p\}}\left(\left|\bar{\partial} \alpha_{Q}\right|^{2}+\left|\bar{\partial}^{*} \alpha_{Q}\right|^{2}\right)=\|\eta\|_{2}^{2}>0$$
$\alpha_{Q}$ 本身不属于 $L^{2}$ 。
证明．令 $B=\bar{\partial}^{*} G_{2}$ 。顶次 Hodge 分解给 $\bar{\partial}\left(\chi A_{Q}-B F\right)=\eta$ 。实际余闭源 $s_{0}=\bar{\partial}_{g}^{*}\left(\chi A_{Q}\right)$在奇点附近为 $O\left(r^{-3}\right)$ ，属于 $L^{p}, 1<p<4 / 3$ 。负 KE 紧轨形没有全纯向量场，故$\Delta_{\bar{\partial}, T}^{(0)} u=s_{0}$ 有唯一 $W^{2, p}$ 解。Green 核大小 $O\left(d^{-2}\right)$ 、导数 $O\left(d^{-3}\right)$ 给 $u=O\left(r^{-1}\right)$ 、$\nabla u=O\left(r^{-2}\right)$ 。定义
$$\alpha_{Q}=\chi A_{Q}-B F-\bar{\partial} u .$$
利用 $\bar{\partial}^{2}=\left(\bar{\partial}^{*}\right)^{2}=0$ 即得（5．32）。
对称性需要单独检查。令 $\mathcal{A} \alpha$ 为降低向量指标后的反对称部分。KE 背景的局部转置恒等式为
$$\mathcal{A} \Delta_{\bar{\partial}, T} \alpha=\left(\Delta_{\bar{\partial},(0,2)}-\lambda\right) \mathcal{A} \alpha, \quad \text { Ric }=\lambda g .$$
它通过一次复协变导数交换得到，不需要 $\bar{\partial} \alpha=0$ 。因此 $\varphi=\mathcal{A} \alpha_{Q}$ 满足 $\left(\Delta_{\bar{\partial}}+1\right) \varphi=0$且 $\varphi=O\left(r^{-2}\right)$ 。其分布点源至多是 $c \delta_{p}$ ；导数型点源与此增长阶不相容。 $\mu_{4}$ 在 $\Lambda_{p}^{0,2}$ 上作用为 -1 ，故无不变 $c$ 。可去奇后积分正算子得 $\varphi=0$ 。

Kähler－Einstein 上的 anti－Hermitian 张量与对称 Beltrami 张量算子对应，将 Dol－ beault 方程转为 $P_{g} h=0$ ，其中 $P_{g}=\frac{1}{2} \nabla^{*} \nabla-\stackrel{\circ}{R}$ ；余闭性给散度零，anti－Hermitian 性给迹零。最后（5．33）直接来自已显示的一阶方程。 \(\square\)

11
若 EH 复周期 $w$ 的完整首项在同一规范下是 $\alpha_{w}=\frac{1}{2} w^{2} \alpha_{Q}-\frac{1}{2}|w|^{2} \alpha_{0}$ ，其中 $\alpha_{0}$ 的Dolbeault 缺陷为零，则
$$\mathcal{E}_{\bar{\partial}}\left(\alpha_{w}\right)=\frac{|w|^{4}}{4}\|\eta\|_{2}^{2} .$$
$|w| \asymp a^{2}$ 时该项尺度为 $a^{8}$ 。它是固定外部的线性缺陷能量；完整拼接作用量还含内端、边界、规范和非线性项，不能以（5．34）代替。

\section*{5．7．1 允许的正权重与共振}

四维 ALE 标量 Laplacian 的锥端齐次根为 $\delta=\ell$ 和 $\delta=-2-\ell$ ，其中 $\ell$ 是球面谐和次数。只有 $\Gamma$ 不变模式参与相应权空间。正权重下的核不只常数；例如标量 $\mu_{4}$ 作用保留二次不变调和模式。源与齐次根共振会产生 $r^{\delta} \log r$ ，不能把它纳入不含对数的同阶余项。

局部曲率源具有光滑原像，也不意味着它匹配指定紧外部的全部高阶 jet。固定外部极限、膨胀内域极限和参数求导是三个不同操作；对正尺度成立的光滑参数化不自动控制零尺度导数。

\section*{5.8 双典范残值：明确可计算的固定背景响应}

本节仅在高度4 Weierstrass－Wahl 轨形上工作。代数章节给自然光滑轨形上的线丛 $L 、 L^{2} \cong K$ ，及 $H^{0}(L)=\langle U, V\rangle$ 。置
$$\left(A_{0}, A_{1}, A_{2}\right)=\left(U^{2}, U V, V^{2}\right), \quad q(A)=A_{0} A_{2}-A_{1}^{2}=0, \quad \eta=U \nabla^{L} V-V \nabla^{L} U .$$
连接项在 $\eta$ 中相消。所需上同调输入是 $H^{1}(K)=H^{1}\left(K^{2}\right)=H^{2}\left(K^{2}\right)=0, h^{2}(L)=2$ 。
令 $b \in \mathcal{H}_{X}=H^{0}\left(\Omega^{1} \otimes K\right), \tau$ 为 $\Omega^{0,2}(K)$ 的平行单位截面。定义核正交响应
$$\Delta B_{i}=-2 b^{*} \cdot \nabla^{K} A_{i}, \quad \int B_{i}=0, \quad \bar{\partial} R_{b}=-2 \sum_{i, j} Q_{i j} A_{i} \bar{\partial}_{K}^{*}\left(B_{j} \tau\right)$$
其中 $q(z)=\sum Q_{i j} z_{i} z_{j}$ 。源的可解性和这些方程属于固定背景的响应定义；不能从一个任意近 Einstein 输入直接调用它们。

\section*{5．8．1 两步分辨率与秩一泛函}

记 $\mathcal{J}=(U, V)^{2}$ 的轨形理想层，则
$$0 \longrightarrow L^{\oplus 2} \xrightarrow{M} K^{\oplus 3} \xrightarrow{D} \mathcal{J} K^{2} \longrightarrow 0, \quad D=\left(U^{2}, U V, V^{2}\right), \quad M=\left(\begin{array}{cc}
-V & 0 \\
U & -V \\
0 & U
\end{array}\right) .$$

\footnotetext{
${ }^{11}$ 实张量－Dolbeault 算子对应的来源为 X．Dai，X．Wang and G．Wei，On the Variational Stability of Kähler－Einstein Metrics，相关 Kähler 分解见作者稿§3，https：／／web．math．ucsb．edu／～dai／paper／dww3．pdf。本节把它用于明确构造的穿孔张量，不对非 $L^{2}$ 张量直接使用闭流形积分正性。
}

在 Wahl 覆盖上 $\mathcal{J}=(u, v)^{2}$ ；商的 $\mu_{4}$ 不变部分在 $K^{2}$ 权下只有常数项，因而点值连接$K_{p}^{2} \cong H^{1}\left(\mathcal{J} K^{2}\right)$ 是同构。Serre 对偶下 $H^{2}(M)$ 的对偶映射为
$$\left(c_{0}, c_{1}, c_{2}\right) \longmapsto\left(-V c_{0}+U c_{1},-V c_{1}+U c_{2}\right) .$$
$(U, V)$ 不在其像中，因此给出一维核上的非零泛函。
对（5．35）取
$$P=\left(-\bar{\partial}_{K}^{*}\left(B_{2} \tau\right), 2 \bar{\partial}_{K}^{*}\left(B_{1} \tau\right),-\bar{\partial}_{K}^{*}\left(B_{0} \tau\right)\right), \quad H=\left(-2 b^{*} \cdot \nabla^{L} V, 2 b^{*} \cdot \nabla^{L} U\right) \tau .$$
直接乘积微分给 $\bar{\partial} R_{b}=D P 、 \bar{\partial} P=M H$ 。局部 Dolbeault 提升证明这个闭数据确代表$R_{b}(p)$ 的点商类；不能仅凭一个光滑形式在点上消失来识别全纯理想层类。与 $(U, V)$ 配对得到
$$\mathcal{L}_{p}(b):=R_{b}(p)=c_{p}\langle\eta, b\rangle_{L^{2}}, \quad c_{p} \neq 0 .$$
内积对第一变量线性，所以 $\mathcal{L}_{p}$ 对 $b$ 共轭线性，复像维数为 1 ，核是 $\eta$ 的 $L^{2}$ 正交补。

\section*{5．8．2 精确常数与相位}

若 $U=u \ell 、 V=v \ell 、 \Omega=\ell^{2}=k(u, v) d u \wedge d v, k_{0}=k(0), e=\Omega(p)^{2}$ ，且 $\tau=\zeta \tau_{0}$ 、$|\zeta|=1$ ，则同一 Dolbeault 方程和原始积分型 Serre 配对给
$$\mathcal{L}_{p}(b)=-\frac{\zeta}{\pi^{2} k_{0}}\langle\eta, b\rangle_{L^{2}} e$$
常数可用紧支撑径向提升核查：$\rho=|u|^{2}+|v|^{2}$ ，取 $f(0)=1$ 、外侧 $f=0$ ，点值 $e$ 的提升给
$$H^{\mathrm{loc}}=-\frac{2 f^{\prime}(\rho)}{\rho^{2}}\binom{\bar{u}}{\bar{v}} \ell d \bar{u} \wedge d \bar{v}$$
用 $d u \wedge d v \wedge d \bar{u} \wedge d \bar{v}=4 d V_{\text {Euc }}$ 、径向积分，再除以覆盖度4，得到 $\int\left(U H_{1}^{\mathrm{loc}}+V H_{2}^{\mathrm{loc}}\right)=2 \pi^{2} k_{0}$ 。实际源的配对是 $-2 \zeta\langle\eta, b\rangle$ ，二者比较即得公式。 ${ }^{12}$

若保持全局基 $(U, V)$ 不变，不能同时免费规定 $k_{0}=1$ 与 $|e|=1$ 。把基变换$(U, V)^{\top} \mapsto G(U, V)^{\top} 、 d=\operatorname{det} G$ 纳人规范时，
$$\eta \mapsto d \eta, \quad k_{0} \mapsto k_{0} / d, \quad \mathcal{L}_{p} \mapsto d^{2} \mathcal{L}_{p} .$$
局部标架 $\ell \mapsto f \ell$ 则使 $k_{0}, e$ 同乘 $f(0)^{4}$ 。相位 $\tau \mapsto \xi \tau$ 必须伴随 $b \mapsto \xi b$ ；这些同步变化使（5．38）协变。其负号不能单独构成不存在性矛盾。

纤维反演的奇空间是 $\mathbb{C} \eta$ ，偶空间记为 $\mathcal{H}_{+}$。它在 Wahl 覆盖上的提升是标量 $e^{\pi i / 4}$ ，在 $K_{p}^{2}$ 上作用为－1，故
$$\left(\partial_{K} b_{+}\right)(p)=0, \quad b_{+}=O\left(r^{5}\right), \quad\left(\partial_{K} \eta\right)(p)=\frac{2}{k_{0}} e$$

\footnotetext{
${ }^{12}$ Dolbeault 双复形及积分型 Serre 对偶的标准背景见 J．－P．Demailly，Complex Analytic and Differential Geom－ etry，Chapters V－VI，https：／／www－fourier．univ－grenoble－alpes．fr／～demailly／manuscripts／agbook．pdf。显示的残值常数来自本节的特定分辨率计算。
}

消去 $\eta$ 分量，得到不依赖点标架相位的模长关系
$$\left|\left(\partial_{K} b\right)(p)\right|=\frac{2 \pi^{2}}{\|\eta\|_{2}^{2}}\left|\mathcal{L}_{p}(b)\right| .$$
线性和共轭线性不同，未经选取实化不能把二者写成一个复线性比例。

\section*{5．8．3 四次闭性缺陷的零集}

固定 KE 背景，设 $C=\partial_{K} b 、 f=|b|^{2} 、 H=i b \wedge b^{*}$ ，定义
$$Q=(\Delta+2)^{-1}\left(4|C|^{2}-8 f\right), \quad T(b)=d(Q \omega+2 H), \quad \mathcal{D}(b)=\|T(b)\|_{2}^{2} .$$
$C$ 一般不是全纯： $\bar{\partial}_{K} C=F_{K} \wedge b$ 。Kähler 恒等式给 $\int|C|^{2}=\int|b|^{2}$ 。令 $L_{\omega} \alpha=\alpha \wedge \omega$ ，这是实一形式到三形式的平行等距同构。定义 $\beta \wedge \omega=-2 d H 、 \xi=d Q-\beta$ ，则局部复微分给
$$d^{*} \beta=4|C|^{2}-4 f, \quad d^{*} \xi=-2(Q+2 f) .$$
由 $* H=f \omega-H$ ，可得
$$\mathcal{D}(b)=0 \quad \Longleftrightarrow \quad d^{*} H=0 .$$
事实上若 $\xi=0,(5.41)$ 给 $Q=-2 f$ ，故 $T=-2 d(* H)=0$ ；逆向由 $d^{*} H=0$ 得$\beta=-2 d f$ ，再由 $\Delta+2$ 的唯一可解性得同一结论。

在 Wahl 点，一阶数据为 $b=A\left(z^{1} d z^{2}-z^{2} d z^{1}\right) \otimes e+O\left(r^{2}\right)$ ，因此 $\Delta f(p)=-|C(p)|^{2}$ 。置 $G=Q+2 f$ ，有 $((\Delta+2) G)(p)=2|C(p)|^{2}$ 。若 $C(p) \neq 0, \mathcal{D}(b)>0$ 。更进一步，$\mathcal{V}=\operatorname{span}_{\mathbb{R}}\left\{T(b): b \in \mathcal{H}_{X}\right\}$ 是固定有限维空间。在其上三阶点评价
$$\ell(T)=-\left[(\Delta+2) d^{*} L_{\omega}^{-1} T\right](p)$$
有有限 $L^{2}$ 算子范数 $M_{X}$ ，且 $\ell(T(b))=4|C(p)|^{2}$ 。于是
$$\mathcal{D}(b) \geq \frac{16}{M_{X}^{2}}|C(p)|^{4} \geq c_{X}\left|\mathcal{L}_{p}(b)\right|^{4}, \quad c_{X}>0 .$$
这里的点控制合法是因为空间固定且有限维；不存在一般无限维 $L^{2}$ 点评价估计。该四次正量与（5．15）的 $\left\|d \omega_{j}\right\|_{2}^{2}=o\left(s_{j}^{2}\right)$ 相容，并不强迫矛盾。把它识别为实际序列的 $s_{j}^{4}$ 首项仍需要二阶极限的完整一致控制。

\section*{5.9 精确局部 KE 参考与三阶净通量的抵消}

这项构造用于检验＂局部正源就是正障碍＂的错误推理。在光滑 quadric $Z_{1}^{2}+Z_{2}^{2}+$ $Z_{3}^{2}=1$ 上令 $v=\sqrt{1+\sum\left|Z_{i}\right|^{2}}, q=\sqrt{2}$ ，取 EH 势 $F_{0}(v)=2 c v$ 。自由对合 $Z \mapsto-Z$给 Wahl 泡商。径向势的行列式密度为
$$\mathcal{D}(F)=\frac{1}{16 v} \frac{d}{d v}\left(\left(v^{2}-2\right)\left(F^{\prime}\right)^{2}\right) .$$

因此 $\log \left(\omega_{F}^{2} / \omega_{0}^{2}\right)=t F$ 等价于
$$F^{\prime}(v)=2 c \sqrt{\frac{2}{v^{2}-2} \int_{q}^{v} u e^{t F(u)} d u}, \quad F(q)=A(t), \quad A(0)=2 c q$$
在每个固定 $q \leq v \leq V$ 上，根号内在端点光滑延拓；其关于 $F$ 的微分含因子 $t$ 。解析隐函数定理给小 $t$ 的精确光滑族，满足 $\operatorname{Ric}(g(t))=-t g(t)$ 。允许参数区间依赖 $V$ ，所以这不是完整非紧泡上统一参数区间的完备 KE 族。

写 $F=2 c v+t \phi_{1}+t^{2} \phi_{2}+t^{3} \phi_{3}+\cdots$ ，径向线性算子为
$$L \phi=\frac{\left(v^{2}-2\right) \phi^{\prime \prime}+2 v \phi^{\prime}}{2 c v} .$$
前两阶及三阶源可直接递推：
$$\begin{aligned}
\phi_{1} & =\frac{2 c^{2}}{3} v^{2}+\frac{8 c^{2}}{3} \log (v+\sqrt{2}) \\
A & =\frac{\phi_{1}^{\prime}}{2 c}, \quad B=L \phi_{1}-A, \quad S_{2}=\phi_{1}+\frac{A^{2}+B^{2}}{2}, \\
S_{3} & =\phi_{2}+B S_{2}+(A-B) \frac{\phi_{2}^{\prime}}{2 c}-\frac{A^{3}+B^{3}}{3}, \\
\phi_{m}(v) & =C_{m}+\int_{q}^{v} \frac{\int_{q}^{u} 2 c w S_{m}(w) d w}{u^{2}-2} d u \quad(m=2,3) .
\end{aligned}$$
特别地，三阶保留了
$$\begin{gathered}
S_{3}=c^{3}\left(\frac{40}{27} v^{3}+\frac{16}{3} v \log v-\frac{32}{9} v\right)+O(\log v) \\
\phi_{3}=c^{4}\left(\frac{4}{27} v^{4}+\frac{16}{9} v^{2} \log v-\frac{56}{27} v^{2}\right)+O(v \log v)
\end{gathered}$$
若泡径向距离为 $R$ ，则 $v \asymp R^{2}$ ；三阶度量项含 $R^{6} 、 R^{2} \log R$ 与 $R^{2}$ 层，不能删掉临界对数项。

若三阶 Ricci 方程写作 $D \operatorname{Ric}_{k}\left(h_{6}\right)+\mathbf{S}_{3}=0$ ，对任意 TT、 $L^{2}$ Jacobi 核 $o$ ，在有限泡域精确有
$$\begin{aligned}
0= & \int_{B_{R}}\left\langle\mathbf{S}_{3}, o\right\rangle+\frac{1}{2} \int_{\partial B_{R}}\left(\left\langle h_{6}, \nabla_{\nu} o\right\rangle-\left\langle\nabla_{\nu} h_{6}, o\right\rangle\right) \\
& -\int_{\partial B_{R}}\left(\mathcal{B}_{k} h_{6}\right)\left(o(\nu, \cdot)^{\sharp}\right),
\end{aligned}$$
其中 $\mathcal{B}_{k}=\delta+\frac{1}{2} d \operatorname{tr}$ 。最后一项是势规范的边界项；转到 Bianchi 规范时所有系数必须同步变化。由于显示的 $\phi_{3}$ 已给光滑原像，总和在每个有限 $R$ 精确为零。 $40 / 27$ 的正号因而不能被称为 Einstein 障碍的正号。

同样，若约化泛函采用固定 Hilbert 梯度和正交投影 $P_{p}, u_{p} \perp \operatorname{im} P_{p}$ 且（1－ $\left.P_{p}\right) \nabla I\left(G_{p}+u_{p}\right)=0$ ，令 $w_{p}=\nabla I\left(G_{p}+u_{p}\right)$ ，则精确包络恒等式为
$$\frac{d}{d p} I\left(G_{p}+u_{p}\right)=\left\langle w_{p}, \partial_{p} G_{p}-\left(\partial_{p} P_{p}\right) u_{p}\right\rangle$$

它消去了 $\partial_{p} u_{p}$ ，但要求实际约化真是同一个固定梯度及投影。一般 Einstein 模障碍约化和参考梯度之间的 Riesz 转换误差仍可能乘以 $\partial_{p} u_{p}$ ，不能省略。经典脱奇结果不能直接升级为本模型三阶净障碍定号。 ${ }^{13}$

\subsection*{5.10 泡上的 Stokes 约束与全奇点评价}

\section*{5．10．1 一个无需尺度比较的局部命题}

命题5．10（保留径向项的周期约束）。设 $g_{j}$ 为 Einstein 度量， $\operatorname{Ric}\left(g_{j}\right)=-g_{j}$ ，在物理尺度 $a_{j} \rightarrow 0$ 的固定核心上有光滑收敛 $a_{j}^{-2} \Phi_{j}^{*} g_{j} \rightarrow k$ 。允许先拉回有限覆盖；要求该固定核心属于非平坦 hyperKähler ALE，$H^{1}=0$ ，且包含一条闭二周期。写
$$W_{j}^{+}=\left(-2 / 3-q_{j}\right) P_{j}+\left(1 / 3+q_{j} / 2\right)\left(I-P_{j}\right)+B_{j},\left.\quad B_{j}\right|_{P_{j}^{\perp}} \in \operatorname{Sym}_{0}^{2}\left(P_{j}^{\perp}\right) .$$
设 $q_{j} \rightarrow 0 、 \delta_{j}=\left\|\nabla \omega_{j}\right\|_{\infty} \rightarrow 0$ ，并记
$$Q_{j}=\left\|q_{j}\right\|_{\infty}, \quad M_{j}=\left\|B_{j}\right\|_{\infty}, \quad G_{j}=\left\|\nabla B_{j}\right\|_{\infty}+\left\|d q_{j}\right\|_{\infty}, \quad K_{j}=1+Q_{j}+\delta_{j}^{2} .$$
若该周期的横向极限周期向量 $\zeta_{0} \neq 0$ ，则固定较小核心上
$$\left|\left|B_{j}\right|_{\mathrm{op}}-\frac{\left|q_{j}\right|}{2}\right| \leq C\left(a_{j} G_{j}+a_{j} \delta_{j} K_{j}+a_{j}^{2} K_{j} M_{j}\right) .$$
特别地，若 $M_{j}+G_{j}+\delta_{j}=O\left(s_{j}\right)$ 且 $Q_{j}=O\left(s_{j}^{2}\right)$ ，则
$$\sup \left|B_{j}\right| \leq C\left(a_{j} s_{j}+s_{j}^{2}\right)=o\left(s_{j}\right) .$$
证明。最低轴在单位泡核心上趋于平行。其正交平面丛与极限常平面同伦，因而平凡；它不是周期曲面的切丛。取全局自对偶标架，记旋转横向平面的联络为 $\alpha_{1}$ ，另两分量为 $\alpha_{2}, \alpha_{3}$ 。单位泡尺度下 $\left|\alpha_{2}\right|+\left|\alpha_{3}\right| \leq C a_{j} \delta_{j}$ 。实际曲率公式为
$$\begin{aligned}
F_{1} & =d \alpha_{1}+\alpha_{2} \wedge \alpha_{3}=a_{j}^{2}\left(1+q_{j}\right) \omega_{1} \\
\binom{F_{2}}{F_{3}} & =\binom{d \alpha_{2}+\alpha_{3} \wedge \alpha_{1}}{d \alpha_{3}+\alpha_{1} \wedge \alpha_{2}}=-a_{j}^{2}\left(B_{j}+q_{j} I / 2\right)\binom{\omega_{2}}{\omega_{3}} .
\end{aligned}$$
所以 $d \alpha_{1}=O\left(a_{j}^{2} K_{j}\right)$ 。 $H^{1}=0$ 的固定域上选 $\operatorname{SO}(2)$ Coulomb 规范，Hodge 估计给$\alpha_{1}=O\left(a_{j}^{2} K_{j}\right)$ ；使用的是闭的 $d \alpha_{1}$ ，不是把可能不闭的 $F_{1}$ 当成阿贝尔曲率。

第一行在周期上积分后除以 $a_{j}^{2}$ ，给极限最低轴周期为零。另两行 Stokes 给
$$\left|\left(B_{j}\left(x_{*}\right)+q_{j}\left(x_{*}\right) I / 2\right) \zeta_{j}\right| \leq C\left(a_{j} G_{j}+a_{j} \delta_{j} K_{j}+a_{j}^{2} K_{j} M_{j}\right) .$$
将系数从积分中移出时，物理协变导数经缩放乘 $a_{j}$ ，标架旋转误差是 $\left[\alpha_{1}, B_{j}\right]$ ；纯迹与旋转交换。

对实对称无迹 2 × 2 矩阵，$B^{2}=|B|_{\mathrm{op}}^{2} I$ 。利用 $\left|\zeta_{j}\right| \geq c>0$ 和反三角不等式得到（5．52）。代入各项速率即得（5．53）。 \(\square\)

\footnotetext{
${ }^{13}$ Biquard，Désingularisation de métriques d＇Einstein II，§1 and §3，https：／／arxiv．org／abs／1311．0956； Ozuch，Integrability of Einstein deformations and desingularizations，Theorem 4．6，https：／／arxiv．org／abs／2105．13193。这里的具体径向递推和有限域抵消是直接计算；文献并未给出本章所需的全部高阶匹配结论。
}

径向小量不能删掉。若仅有 $q_{j}=O\left(s_{j}\right)$ ，矩阵 $B_{*}=\operatorname{diag}\left(-q_{*} / 2, q_{*} / 2\right)$ 可满足 $\left(B_{*}+q_{*} I / 2\right)(1,0)^{\top}=0$ ，却并非零矩阵。因此周期独自只约束完整横向矩阵；真正消除抵消的是 $q_{j}=o\left(s_{j}\right)$ 。若有两条横向周期构成可逆 2 × 2 矩阵，则可同时控制 $B_{j}, q_{j}$ ，但不能仅凭 $b_{2} \geq 2$ 断言周期秩为 2 。

\section*{5．10．2 每个真实轨形奇点都可以选一个光滑泡}

对（5．2）的任一真实奇点 $p$ ，在隔离邻域内部取最大曲率点 $x_{j}$ ，邻域边界落在光滑收敛外环带。若内部曲率也有界，非塌缩与 Einstein 正则性会使极限点光滑，矛盾。故 $Q_{j}=|\operatorname{Rm}|\left(x_{j}\right) \rightarrow \infty$ ，且 $x_{j} \rightarrow p$ 。取 $\rho_{j}=Q_{j}^{-1 / 2}$ ，最大点到外边界距离在原尺度有正下界。于是任意固定缩放球上曲率至多为1、基点曲率为1，非塌缩保留。可得完整光滑非平坦 Ricci－flat 极限，有限总曲率与欧氏体积增长使其 ALE；全局 $W^{+}$界使它ASD。

非平坦 ASD Ricci－flat ALE 四流形有有限单连通 hyperKähler 覆盖。其三个平行形式不可能全部在所有二周期上取零，这是 hyperKähler ALE 周期分类的非退化性。第一行 Stokes 已使最低轴的全部周期为零，故可选一条横向非零周期。 ${ }^{14}$
（5．16）满足命题5．10的速率。利用全局 $\left\|\nabla\left(B_{j} / s_{j}\right)\right\|_{\infty} \leq C$ ，只传递标量模长，无需跨颈同步相位。先与距 $p$ 为固定 $r$ 的外部点比较，再令 $j \rightarrow \infty 、 r \downarrow 0$ ，得到
$$B_{1}(p)=0, \quad\left(\partial_{K} b_{1}\right)(p)=0 \quad \text { 对每个真实轨形奇点 } p .$$
这一机制不要求根泡光滑，不比较各层泡尺度，不依赖实际双典范残值匹配，也不需要 $s_{j} \asymp a_{j}^{4}$ 。

\subsection*{5.11 有界直径体积间隙：保留完整逻辑接口}

本章的分析部分产生非零 $b_{1}$ 及全奇点零评价。把它转成矛盾还需要准确的代数几何输人。为便于独立检查，先写成逻辑完整的条件命题。

命题5．11（非零首项与有限点评价的组合）。假设对固定 $N$ 的每条（5．2），存在子列极限 $X$ ，使本章的非零全纯首项和全奇点零评价成立。另假设每个这样的 $X$ 都有一组奇点 $S_{X}$ ，使
$$\operatorname{Ev}_{X}:\left.\mathcal{H}_{X} \longrightarrow \bigoplus_{p \in S_{X}} K_{X}^{2}\right|_{p}, \quad b \longmapsto\left(\left(\partial_{K} b\right)(p)\right)_{p \in S_{X}}$$
单射。则对每个有限 $D$ 存在 $\varepsilon_{N}(D)>0$ ，使
$$\operatorname{Ric}(g)=-g, \quad \operatorname{diam}(g) \leq D \quad \Longrightarrow \quad \operatorname{Vol}(g) \geq 2 \pi^{2}+\varepsilon_{N}(D) .$$
证明．若结论失败，逐个选取体积差小于 $1 / j$ 、直径不超过同一个 $D$ 的 Einstein 度量。极限给 $\left\|b_{1}\right\|_{2}^{2}=1 / 2$ ，但（5．55）使其落入（5．56）的核，矛盾。只需在抽取后的一个固定 $X$ 上单射，不需跨复模空间一致的评价常数，也不需要 Einstein 体积谱离散或有限。 \(\square\)

\footnotetext{
${ }^{14}$ E．P．Wright，Quotients of gravitational instantons，Theorem A and §2－3，https：／／arxiv．org／pdf／1102
。2442。单连通情形使用 Kronheimer 的 hyperKähler ALE 周期分类；非单连通情形由有限覆盖回到该框架。
}

档案把所有极限识别为 $K_{X}^{2}=1, p_{g}(X)=3$ 的高度4 Weierstrass 截面收缩族，允许附加 ADE 点。分析入口如下：全局 $W^{+}$界使七个自对偶调和形式一致有界，奇点小球不能吸走其 Gram 矩阵，因此 $b_{+}(X) \geq 7$ ；球面商边界实 $H^{1}, H^{2}$ 消失使核心内部支撑代表可延拓回 $N$ ，给反向不等式和 $b_{1}(X)=0$ 。KE 典范形式给 $K_{X}^{2}=V /\left(2 \pi^{2}\right)=1$以及射影性，随后需要应用 $\log$ Noether 等号分类。 ${ }^{15}$

有限点评价部分的结构是：Wahl 点检测奇截面 $\eta$ ；一般族的偶空间为零，少数等模族的偶截面由次数至多 1 的基底参数 $Q$ 控制。适当 ADE 点的微分评价为 $Q$ 在该点的非零倍数。因此 Wahl 点加至多两个 ADE 点可以检测全空间。这个结论必须覆盖所有等模例外，并采用自然轨形上的 $\partial_{K}$ ，不能删掉附加 ADE 分支。

本整理保留（5．57）为显式接口命题；其对指定 $N$ 的无条件应用，需要代数章节的全部极限分类与有限点评价证明和本章统一使用相同轨形、定向、典范线性化。它不是一般 Ricci 夹逼定理。即使全部接口通过，也只推出精确 Einstein 度量接近该特殊体积下端时直径必须趋于无穷，仍允许体积远离下端的 Einstein 度量。

\section*{5．11．1 为什么直径不能由普通饱和条件补出}

固定单连通光滑五次曲面族可退化为平面与四次曲面沿一条光滑四次曲线横截相交：
$$\mathcal{X}_{t}=\left\{L Q_{4}+t Q_{5}=0\right\} \subset \mathbb{P}^{3} .$$
一般 $t \neq 0$ 的光滑纤维有 $K^{2}=5$ 。其归一化负 KE 度量满足 $V=10 \pi^{2}$ ，精确达到 SW标量下界；稳定退化的完整 KE 极限却具有沿双曲线移至无穷远的非紧分量，故直径发散。 ${ }^{16}$

因此单连通、固定拓扑、固定负 Einstein 常数、固定体积和 SW 完全饱和合起来仍不保证直径界。要排除 $N$ 的无界直径分支，必须使用新的、针对该光滑型的控制。

\subsection*{5.12 本章留下的可执行数学接口}

已经清楚分离的对象有四类：SW 给出的体积与旋量缺陷、最低 Weyl 轴给出的扭率首项、固定轨形上的 Dolbeault／双典范响应、实际泡核心上的周期。它们分别具有不同的范数和尺度，不能因都出现一个非零数就直接相等。
\begin{itemize}
\item[] －对局部残值路线，非零 $\mathcal{L}_{p}(b)$ 与正四次缺陷并不构成矛盾；还须证明实际方程迫使相应缺陷为零，或计算包含内外及规范项的完整净通量。
\item[] －对周期路线，局部 Stokes 证明已绕开 $s \asymp a^{4}$ 和残值匹配。不能绕开的输入是全局
- 阶速率、径向 $o(s)$ 、非零首项、全部极限分类和有限点评价单射。
\item[-] 对一般 Ricci 夹逼问题，当前分析没有从原始假设推出直径界、体积接近 $2 \pi^{2}$ 、自对偶谱隙或 $\operatorname{Ric}_{0}=o(s)$ 。这些是范围界线，不是已知可按顺序完成的待办引理。
\end{itemize}

\footnotetext{
${ }^{15}$ S．Tsunoda and D．－Q．Zhang，Noether＇s inequality for non－complete algebraic surfaces of general type， Theorem 2.10 与相关等号分类，https：／／ems．press／content／serial－article－files／40427？nt＝1。本章把其适用范围核验交给代数章节；不能把 $p_{g}=3, K^{2}=1$ 的数值本身当成已经完成的分类证明。
${ }^{16}$ J．Song，Degeneration of Kähler－Einstein manifolds of negative scalar curvature，Theorem 1．2，https： ／／arxiv．org／pdf／1706．01518。该例的作用是检验一般紧性推理，既不是 $N$ 上的度量，也不是原题反例。
}

\section*{第六章 固定曲面丛上的全局逼近、修正与退化}

本章围绕一个固定的光滑闭四维流形展开：纤维与基底均为高亏格曲面，单值变换由一次非分离 Dehn twist 生成。已经完成的核心构造是：在同一个流形上，全局最大 Ricci 误差可以趋于零，且完整曲率及任意固定阶导数可以保持有界。这并不是原问题的反例，因为尚未排除这个流形的所有 Einstein 度量。随后建立的三阶修正、全局配对、共形障碍和谱计算，各自说明了特定修正机制的能力与边界。

以下固定纤维亏格 $p \geq 2$ 、基底亏格 $q \geq 2$ 。归一化目标始终是 Ric $=-g$ ，并记
$$\Phi(g)=\operatorname{Ric}_{g}+g, \quad \delta(g)=\sup _{M}\left|g^{-1} \Phi(g)\right|_{\mathrm{op}}, \quad V_{0}=16 \pi^{2}(p-1)(q-1) .$$
张量的 $C^{k}$ 范数指相应背景下 0 至 $k$ 阶协变导数的上确界之和；$|\cdot|$ 无特别说明时为Hilbert－Schmidt 范数。对称矩阵的核范数 $|Q|_{*}$ 指绝对特征值之和，它是算子范数配对所需的对偶范数。所有渐近常数允许依赖固定的曲面、轮廓和导数阶数，不能改称仅依赖维数的常数。

\section*{6.1 不退化纤维的慢插值：一个完整的闭流形构造}

\section*{6．1．1 拓扑先固定，度量再变化}

在闭双曲纤维 $\left(F, h_{0}\right)$ 上固定非分离简单闭测地线及其子领圈
$$\left[-R_{0}, R_{0}\right] \times \mathbb{R} / \mathbb{Z}, \quad h_{0}=d u^{2}+a(u)^{2} d s^{2}, \quad a(u)=a_{0} \cosh u$$
这里 $a_{0}, R_{0}, h_{0}$ 完全固定。取光滑 $\zeta$ ，在领圈左、右端邻域分别恒为0，1。映射
$$D(u, s)=(u, s+\zeta(u))$$
在领圈两端均为恒等，故零延拓为纤维上的 Dehn twist。定义
$$h_{z}=d u^{2}+a^{2}\left(d s+z \zeta^{\prime} d u\right)^{2} \quad(0 \leq z \leq 1), \quad h_{z}=h_{0} \quad \text { 在领圈外. }$$
每个 $z$ 对应的局部代换 $s^{\prime}=s+z \zeta(u)$ 给出
$$K_{h_{z}}=-1, \quad d A_{h_{z}}=d A_{h_{0}}, \quad h_{1}=D^{*} h_{0} .$$
非整数 $z$ 的坐标代换不必延拓成闭纤维的微分同胚；已经匹配边界的是度量本身。这避免了把非平凡映射类错误地同痕化。

在闭基底 $B$ 上固定非分离曲线 $c$ 。沿它切开，取补集上的平凡纤维丛；将连接领圈的两端分别用恒等和 $D$ 粘接。得到固定闭流形 $E_{D}$ 。其单值变换表示通过
$$\pi_{1}(B) \longrightarrow \mathbb{Z} \longrightarrow \operatorname{Mod}(F), \quad 1 \longmapsto[D] .$$

令基底双曲度量中的 $c$ 长度为 $\ell \downarrow 0$ ，其余 Fenchel－Nielsen 参数固定。标准领圈半宽为
$$w(x)=\operatorname{arsinh} \frac{1}{\sinh (x / 2)}, \quad L=\frac{1}{2} w(\ell), \quad g_{B}=d t^{2}+\ell^{2} \cosh ^{2} t d \theta^{2} \quad(|t| \leq L)$$
领圈公式与单曲线尖点退化是经典输入。 ${ }^{1}$ 取固定端部常值轮廓 $\eta:[-1,1] \rightarrow[0,1]$ ，置$z(t)=\eta(t / L)$ ，并定义
$$G_{\ell}=d t^{2}+\ell^{2} \cosh ^{2} t d \theta^{2}+h_{z(t)} \text { 在基底领圈内; } \quad G_{\ell}=g_{B}+h_{0} \quad \text { 在外部. }$$
右端内侧度量是 $D^{*} h_{0}$ ，等于外部度量的粘接拉回；$z$ 在端部常值，所有横向导数都匹配。因此这是整个固定 $E_{D}$ 上的光滑正定度量。

\section*{6．1．2 全部 Ricci 块，而非仅对角估计}

记
$$b=\ell \cosh t, \quad j=\tanh u, \quad k=\tanh t, \quad Q=a \zeta^{\prime}, \quad v=Q z^{\prime} .$$
采用正交余标架
$$\left(e^{0}, e^{1}, e^{2}, e^{3}\right)=\left(d t, b d \theta, d u, a\left(d s+z \zeta^{\prime} d u\right)\right) .$$
其非零结构方程为
$$d e^{1}=k e^{0} \wedge e^{1}, \quad d e^{3}=j e^{2} \wedge e^{3}+v e^{0} \wedge e^{2} .$$
纤维在 $t$ 方向的形状算子及其协变导数为
$$S=\frac{1}{2}\left(\begin{array}{cc}
0 & v \\
v & 0
\end{array}\right), \quad \operatorname{tr} S=0, \quad D_{t} S=\left(\begin{array}{cc}
v^{2} / 2 & v_{t} / 2 \\
v_{t} / 2 & -v^{2} / 2
\end{array}\right), \quad \operatorname{div}_{h_{z}} S=\frac{v_{u}+2 j v}{2} e^{3} .$$
$D_{t} S$ 中的二次对角项来自标架旋转，不能用矩阵条目的普通导数代替。切片 Gauss－Codazzi 公式给出完整矩阵
$$\Phi\left(G_{\ell}\right)_{\mathrm{ON}}=\left(\begin{array}{cccc}
-v^{2} / 2 & 0 & 0 & \left(v_{u}+2 j v\right) / 2 \\
0 & 0 & 0 & 0 \\
0 & 0 & -v^{2} / 2 & -\left(v_{t}+k v\right) / 2 \\
\left(v_{u}+2 j v\right) / 2 & 0 & -\left(v_{t}+k v\right) / 2 & v^{2} / 2
\end{array}\right) .$$
亦可把 $e^{3}$ 看成圆周连接：圆周长度函数为 $a$ ，连接曲率为 $(v / a) d t \wedge d u$ 。水平曲率平方项给两个 $-v^{2} / 2$ ，圆周块给 $+v^{2} / 2$ ，连接曲率散度给两个混合项，得到相同公式。

令
$$A_{0}=\|Q\|_{\infty}, \quad A_{1}=\left\|Q^{\prime}+2 j Q\right\|_{\infty}, \quad M_{i}=\left\|\eta^{(i)}\right\|_{\infty}(i=1,2) .$$

\footnotetext{
${ }^{1}$ M．Rupflin and P．Topping，Horizontal curves of hyperbolic metrics，Appendix A，Lemma A． 1 与 Theorem A．4：https：／／arxiv．org／pdf／1605．06691．本章使用它们提供的双曲领圈和厚部收敛；Ricci 矩阵与修正均在下文计算。
}

矩阵的非对角部分只有两条独立边，其算子范数为对应条目平方和的平方根。因此
$$\delta\left(G_{\ell}\right) \leq \frac{A_{0}^{2} M_{1}^{2}}{2 L^{2}}+\frac{1}{2 L} \sqrt{\left(A_{1} M_{1}\right)^{2}+A_{0}^{2}\left(M_{1}+M_{2} / L\right)^{2}} \longrightarrow 0 .$$
领圈交叉区域外只要 $Q=0$ 或 $z^{\prime}=0$ ，误差就严格为零；故这是全局最大误差估计。
短基底圆周没有引入隐藏的 $\ell^{-1}$ ：系数与 $\theta$ 无关，联络只含 $b^{\prime} / b=\tanh t$ 。固定纤维的有限坐标覆盖与固定路径给任意固定阶导数界。对结构方程逐次协变微分得到
$$\begin{aligned}
\operatorname{Vol}\left(G_{\ell}\right) & =V_{0}, & s_{G_{\ell}} & =-4-v^{2} / 2, \\
\left\|\nabla^{m} \operatorname{Rm}_{G_{\ell}}\right\|_{\infty} & \leq C_{m}, & \left\|\nabla^{m} \Phi\left(G_{\ell}\right)\right\|_{\infty} & \leq C_{m} / L
\end{aligned}$$
这些高阶估计是显式构造的性质，不是一般 Ricci 夹逼的推论。

\section*{6．1．3 实际退化与构造内部的障碍}

矩阵（6．7）对应的联络还给
$$K\left(e_{0}, e_{3}\right)=v^{2} / 4>0 \text { 当 } v \neq 0 \text {. }$$
因此本构造并不满足严格负截面曲率。基底中央的非平凡短圆周给 $\mathrm{inj}_{\text {min }} \leq \ell / 2$ ，而投影不增加长度，故直径发散。插值区域体积为
$$8 \pi(p-1) \ell \sinh L=O(\sqrt{\ell}) \longrightarrow 0 .$$
厚部光滑极限是 $\Sigma_{p} \times \Sigma_{q-1,2}$ ，体积仍为 $V_{0}$ 。非平凡粘接被送向越来越远的细颈；最大误差趋零的依据仍是（6．8），不能用小体积替代。

若（6．5）本身为任意常数的 Einstein 度量，$e_{1}$ 分量先迫使 Einstein 常数为 $-1, e_{0}$分量再迫使 $v=0$ ，与两个非平凡轮廓矛盾。这只排除了该分层形式内的精确解。

同一机制适用于标准几何自由商。若曲面群生成元满足
$$\rho\left(a_{i}\right)=1, \quad \rho\left(b_{i}\right)=\left[\phi_{i}\right] \quad(1 \leq i \leq q),$$
则可沿互不相交的 $a_{i}$ 领圈独立插值，$\left[\phi_{i}\right]$ 无需交换。先取从 $h_{0}$ 到 $\left(\phi_{i}^{0}\right)^{*} h_{0}$ 的端部常值双曲路径 $k_{i, z}$ 。其面积形式 $\mu_{i, z}$ 的导数正合，选择 $d \alpha_{i, z}=\partial_{z} \mu_{i, z}$ ，以
$$\iota_{X_{i, z}} \mu_{i, z}=-\alpha_{i, z}, \quad \partial_{z} \psi_{i, z}=X_{i, z} \circ \psi_{i, z}$$
定义流，则 $h_{i, z}=\psi_{i, z}^{*} k_{i, z}$ 具有共同面积形式。终点是 $\left(\phi_{i}^{0} \circ \psi_{i, 1}\right)^{*} h_{0}$ ，映射类未变，丛总空间可用领圈内的同痕逐块识别。完整切片公式为
$$\Phi_{t t}=-\operatorname{tr} S_{i}^{2}, \quad \Phi_{\theta \theta}^{\mathrm{ON}}=0, \quad \Phi_{F F}^{\sharp}=-D_{t} S_{i}-k S_{i}, \quad \Phi_{t F}=\operatorname{div}_{h_{i}} S_{i} .$$
有限条固定路径仍给（6．9）。表示经自由群延拓到把体，丛定向地界一个五维曲面丛，因而签名为零；非交换单值变换没有在此机制中产生非零签名。

\section*{6．1．4 指数积分误差与非零签名的结构限制}

若慢轮廓的变化支撑在 $|t| \leq \alpha L$ ，固定 $0<\alpha<1$ ，则 $\ell=4 e^{-2 L}+O\left(e^{-6 L}\right)$ ，误差支持体积为 $O\left(e^{-(2-\alpha) L}\right)$ 。对每个有限 $r \geq 1$ ，
$$\left\|\Phi\left(G_{L}\right)\right\|_{L^{r}} \leq C_{r} L^{-1} e^{-(2-\alpha) L / r}, \quad\left\|s_{G_{L}}+4\right\|_{L^{r}} \leq C_{r} L^{-2} e^{-(2-\alpha) L / r} .$$
记 $q_{L}=|S|^{2} 、 A_{L}=\int q_{L} 、 B_{L}=\int q_{L}^{2}$ ，则 $A_{L}=O\left(L^{-2} e^{-(2-\alpha) L}\right) 、 B_{L} \leq C L^{-2} A_{L}$ 。由$s=-4-q_{L}$ 与 Yamabe 商的 Hölder 下界、常数函数上界，
$$-\sqrt{16 V_{0}+8 A_{L}+B_{L}} \leq Y\left(\left[G_{L}\right]\right) \leq-4 \sqrt{V_{0}}-A_{L} / \sqrt{V_{0}} .$$
一旦使用本章拓扑部分证明的 $Y\left(E_{D}\right)=-4 \sqrt{V_{0}}$ ，即得
$$Y\left(E_{D}\right)-Y\left(\left[G_{L}\right]\right)=\frac{A_{L}}{\sqrt{V_{0}}}\left[1+O\left(L^{-2}\right)\right] \quad\left(A_{L}>0\right) .$$
这量化逼近而不宣称上确界实现。
对任意高亏格曲面丛 $E \rightarrow B$ ，取单值变换等变的纤维模参数映射 $F: \widetilde{B} \rightarrow \mathcal{T}_{p}$ 。采用 $\left[\omega_{\mathrm{WP}}\right]=2 \pi^{2} \kappa_{1}$ 的规范，签名公式给
$$\int_{B} F^{*} \omega_{\mathrm{WP}}=6 \pi^{2} \tau(E), \quad \frac{1}{2} \int_{B}|d F|^{2} d A \geq 6 \pi^{2}|\tau(E)| .$$
第一式由 $\kappa_{1}=\pi_{*}\left(e\left(T_{v} E\right)^{2}\right)$ 与 $3 \tau=\left\langle p_{1}(T E),[E]\right\rangle$ 得到；第二式由 Kähler 形式的面积不等式得到。 ${ }^{2}$ 当 $K_{B}=-1$ 时，
$$\sup _{B}|d F|^{2} \geq \frac{3 \pi|\tau(E)|}{q-1} .$$
所以非零签名的固定亏格丛不能保持基底曲率 -1 ，同时令所有方向的模参数速度一致趋零。自由商构造的每个领圈只沿一个变量变化，故 $F^{*} \omega_{\mathrm{WP}}=0$ ；其签名为零是结构事实。这个能量限制不排除一般非下沉度量中的曲率抵消。

\section*{6.2 双领圈平衡：全局二阶误差及精确首系数}

现在改变构造本身：纤维短测地线长度为 $\varepsilon \downarrow 0$ ，基底短长度为 $\beta=\varepsilon^{2}$ ，其余模参数固定。置
$$R=w(\varepsilon)-2, \quad L=w(\beta)-2, \quad a=\varepsilon \cosh u, \quad b=\beta \cosh t .$$
取固定截断 $\rho$ ，在 $x \leq 1 / 4$ 为零，在 $x \geq 1$ 为一，令
$$\chi_{R}(u)=\rho(R-|u|), \quad \chi_{L}(t)=\rho(L-|t|), \quad I_{R}=\int \chi_{R} \operatorname{sech}^{3} u d u, \quad J_{L}=\int \chi_{L} \operatorname{sech} t d t .$$

\footnotetext{
${ }^{2}$ S．Wolpert，Chern forms and the Riemann tensor for the moduli space of curves，特征形式规范见印刷第120页及第5章：https：／／www．math．umd．edu／～swolpert／preprints／Chern＿forms．pdf．使用等变映射或先取无挠有限覆盖，避免粗模空间遗漏单值变换信息。
}

取积分从左端开始并归一化的轮廓
$$\zeta^{\prime}=I_{R}^{-1} \chi_{R} \operatorname{sech}^{3} u, \quad \tau^{\prime}=J_{L}^{-1} \chi_{L} \operatorname{sech} t$$
它们端点差均为一。使用（6．2）和同一粘接，得到固定 $E_{D}$ 上的闭度量
$$G_{\varepsilon}=d t^{2}+b^{2} d \theta^{2}+d u^{2}+a^{2}\left(d s+\tau \zeta^{\prime} d u\right)^{2}$$
改变参数时 Dehn twist 的具体代表可能变，但映射类固定；以丛微分同胚拉回固定总空间即可。

仍使用完整矩阵（6．7），此时
$$v=\frac{\varepsilon}{I_{R} J_{L}} \chi_{R} \chi_{L} \operatorname{sech}^{2} u \operatorname{sech} t$$
两个线性项变成
$$v_{u}+2 \tanh u v=\frac{\varepsilon \chi_{R}^{\prime} \chi_{L}}{I_{R} J_{L}} \operatorname{sech}^{2} u \operatorname{sech} t, \quad v_{t}+\tanh t v=\frac{\varepsilon \chi_{R} \chi_{L}^{\prime}}{I_{R} J_{L}} \operatorname{sech}^{2} u \operatorname{sech} t .$$
在核心它们精确消失。在截断带，分别受 $C \varepsilon e^{-2 R}$ 与 $C \varepsilon e^{-L}$ 控制，均为 $O\left(\varepsilon^{3}\right)$ ；该带内$v=O\left(\varepsilon^{3}\right)$ 。其余区域为对角残差 $v^{2} / 2$ 。中心 $t=u=0$ 达到最大值，而截断带误差比中心二阶项小，故对充分小 $\varepsilon$ ，严格有
$$\delta\left(G_{\varepsilon}\right)=\frac{\varepsilon^{2}}{2 I_{R}^{2} J_{L}^{2}}=\frac{2}{\pi^{4}} \varepsilon^{2}+O\left(\varepsilon^{4}\right) .$$
这里 $I_{R}=\pi / 2+O\left(\varepsilon^{3}\right) 、 J_{L}=\pi+O\left(\varepsilon^{2}\right)$ 。体积仍恰为 $V_{0}$ ，标量曲率仍为 $-4-v^{2} / 2$ ，完整曲率及固定阶导数一致有界。

该改善不违反固定端点慢插值的下界。对一般面积规范领圈，$S=\frac{1}{2} h^{-1} \partial_{t} h$ 满足
$$|S|^{2} \leq \delta, \quad\left\|D_{t} S+\tanh t S\right\|_{\mathrm{op}} \leq \delta .$$
沿平行标架解一阶不等式得
$$\|S(t)\|_{\mathrm{op}} \leq \sqrt{\delta / 2} \operatorname{sech} t+\delta \mid \tanh t .$$
因此端点 Teichmüller 距离 $d$ 必须满足
$$d \leq \pi \sqrt{\delta / 2}+2 \delta \log \cosh L, \quad d>0 \text { 固定时 } \liminf L \delta \geq d / 2 \text {. }$$
双领圈中端点本身退化，恒等标记的剪切伸缩只给
$$d_{\varepsilon} \leq \operatorname{arsinh} \frac{\varepsilon}{2 I_{R}}=\frac{\varepsilon}{\pi}+O\left(\varepsilon^{3}\right) .$$
这是上界而非匹配渐近等式；固定 $d>0$ 的假设已经不成立。

\section*{6.3 一次真实的二阶校正：最大误差降至三阶}

\section*{6．3．1 张量方程的可解分解}

展开短角坐标 $x=\varepsilon s 、 y=\beta \theta$ ，使用完整双曲圆柱乘积
$$g_{0}=g_{1}+g_{2}, \quad g_{1}=d t^{2}+\cosh ^{2} t d y^{2}, \quad g_{2}=d u^{2}+\cosh ^{2} u d x^{2} .$$
令 $c_{0}=2 / \pi^{2} 、 f=\operatorname{sech}^{2} t 、 r=\operatorname{sech}^{2} u, T_{1}=d t^{2}-\cosh ^{2} t d y^{2} 、 T_{2}=d u^{2}-\cosh ^{2} u d x^{2}$ 、 $q_{1}=f T_{1}$ 。在背景标架中
$$\Phi\left(G_{\varepsilon}\right)=\varepsilon^{2} D+O_{C^{k}}\left(\varepsilon^{3}\right), \quad D=\frac{c_{0}^{2} f r^{2}}{2} \operatorname{diag}(-1,0,-1,1) .$$
取 $\mathfrak{b} h=-\operatorname{div} h+\frac{1}{2} d \operatorname{tr} h$ 。直接微分给 $\mathfrak{b} D=0$ 。在 Einstein 背景的 Bianchi 规范下，
$$D \Phi_{g_{0}} h=\mathcal{L} h, \quad \mathcal{L}=\frac{1}{2}\left(\nabla^{*} \nabla-2 \stackrel{\circ}{R}\right) .$$
此处 $\stackrel{\circ}{R} g=$ Ric，粗 Laplacian 非负。 ${ }^{3}$ 寻找 $K=A g_{1}+B q_{1}+C T_{2}$ 。令
$$P_{t}=\partial_{t}^{2}+\tanh t \partial_{t}, \quad P_{u}=\partial_{u}^{2}+\tanh u \partial_{u}$$
则 $\mathcal{L} K=-D$ 等价于
$$\begin{aligned}
H_{A} A & =\frac{c_{0}^{2}}{2} f r^{2}, \quad H_{A}=-P_{t}-P_{u}+2, \\
-P_{u} B & =\frac{c_{0}^{2}}{2} r^{2}, \\
H_{C} C & =c_{0}^{2} f r^{2}, \quad H_{C}=-P_{t}-P_{u}+2-4 r .
\end{aligned}$$
中间方程具有两端趋零的闭式解
$$B(u)=\frac{c_{0}^{2}}{8}\left[\operatorname{sech}^{2} u+\frac{\pi^{2}}{4}-(\arctan \sinh u)^{2}\right] .$$
对 $A, C$ 使用测度 $d \mu_{0}=\cosh t \cosh u d t d u$ 下的 Friedrichs 实现。酉共轭和地态变换给
$$-P_{t} \simeq-\partial_{t}^{2}+\frac{1}{4}+\frac{1}{4} \operatorname{sech}^{2} t \geq \frac{1}{4}, \quad-P_{u}+2-4 r \geq 0,$$
后一个不等式来自
$$\int\left(\left|a^{\prime}\right|^{2}+(2-4 r) a^{2}\right) \cosh u d u=\int r^{2}\left|(a / r)^{\prime}\right|^{2} \cosh u d u$$
故 $H_{A} \geq 5 / 2 、 H_{C} \geq 1 / 4$ ，右端属于 $L^{2}\left(d \mu_{0}\right)$ ，唯一光滑解可明确写为
$$A=\frac{c_{0}^{2}}{2} \int_{0}^{\infty} e^{-s H_{A}}\left(f r^{2}\right) d s, \quad C=c_{0}^{2} \int_{0}^{\infty} e^{-s H_{C}}\left(f r^{2}\right) d s$$
这已定义实际解，不是尚待证明的可逆性假设。

\footnotetext{
${ }^{3}$ 标准规范线性化见 M．Anderson，Dehn filling and Einstein metrics in higher dimensions，§2．3：https：／／arxiv．org／pdf／math／0303260．这里采用 Einstein 常数－1；以下三个径向算子由乘积连接直接计算。
}

\section*{6．3．2 Bianchi 条件、衰减和闭流形粘接}

设 $D_{u}=\partial_{u}+2 \tanh u 、 H_{1}=-P_{t}-P_{u}+2-r$ 。交换恒等式
$$D_{u} H_{C}=H_{1} D_{u}, \quad \partial_{u} H_{A}=H_{1} \partial_{u}$$
使 $Z=C_{u}+2 \tanh u C-A_{u}$ 满足 $H_{1} Z=0$ 。它属于加权 $L^{2}$ ，而 $H_{1} \geq 3 / 2$ ，所以
$$\mathfrak{b} K=\left(A_{u}-C_{u}-2 \tanh u C\right) d u=0, \quad D \Phi_{g_{0}} K=-D .$$

正函数
$$T(t)=\frac{1}{2}\left[\frac{\pi^{2}}{4}-(\arctan \sinh t)^{2}\right], \quad-P_{t} T=f,$$
给 $H_{A}(T r) \geq f r^{2} 、 H_{C}(T r) \geq f r^{2}$ 。正 Green 算子比较与局部椭圆估计于是给
$$0 \leq A \leq \frac{c_{0}^{2}}{2} \operatorname{Tr}, \quad 0 \leq C \leq c_{0}^{2} \operatorname{Tr}, \quad\left|\nabla^{j} K\right| \leq C_{j}\left(e^{-|t|-2|u|}+e^{-2|t|-|u|}\right) .$$
$H_{C}$ 的零阶势可以为负；比较使用正谱隙与正部分测试，并未假定势处处非负。
取固定宽度截断 $\Psi_{\varepsilon}=\psi_{R}(u) \psi_{L}(t)$ ，在子领圈端点邻域为零、核心为一。将
$$\widetilde{G}_{\varepsilon}=G_{\varepsilon}+\varepsilon^{2} \Psi_{\varepsilon} K$$
零延拓到闭流形。校正及全部导数在边界匹配，且 $K$ 一致有界，故小参数下正定。核心二阶源由（6．20）消去；纤维截断带上 $K=O\left(e^{-R}\right)=O(\varepsilon)$ ，基底截断带上 $K=O\left(e^{-L}\right)= O\left(\varepsilon^{2}\right)$ ，因此交换子分别贡献 $O\left(\varepsilon^{3}\right) 、 O\left(\varepsilon^{4}\right)$ 。背景替换 $G_{\varepsilon}-g_{0}=O_{C^{k}}(\varepsilon)$ 与二阶 Taylor余项分别贡献 $O\left(\varepsilon^{3}\right) 、 O\left(\varepsilon^{4}\right)$ 。于是
$$\left\|\Phi\left(\widetilde{G}_{\varepsilon}\right)\right\|_{C^{k}\left(\widetilde{G}_{\varepsilon}\right)} \leq C_{k} \varepsilon^{3} \quad \text { 每个固定 } k .$$
校正的水平系数依赖纤维位置，原投影一般已不是黎曼下沉；原来的固定体积与自然almost Kähler 恒等式也不能沿用。

\section*{6．3．3 非零通量如何消除一个假的二阶障碍}

由（6．19）有
$$\left[\cosh u B^{\prime}\right]_{-\infty}^{+\infty}=-c_{0}^{2} \pi / 4, \quad B(u)=\frac{c_{0}^{2} \pi}{4} e^{-|u|}+O\left(e^{-3|u|}\right) .$$
故该模式不能用紧支解精确修正。另令
$$M(t)=\int C(t, u) r(u) \cosh u d u$$
纤维方向积分合法且无边界项，给
$$-P_{t} M=\frac{3 \pi c_{0}^{2}}{8} f, \quad M=\frac{3 \pi c_{0}^{2}}{8} T, \quad-\left[\cosh t M^{\prime}\right]_{-\infty}^{+\infty}=\frac{3}{2 \pi^{2}} .$$
恢复实际校正幅度与两个短角周期，这项通量为 $3 \varepsilon^{3} \beta /\left(2 \pi^{2}\right)$ ，恰补偿源 $\varepsilon^{2} D$ 与纤维形式零模 $r T_{2}$ 的负配对。 $r T_{2}$ 沿整个基底圆柱不衰减，并不属于完整双端模型的 $L^{2}$ 伴随核。逐点衰减不等于加权通量消失；此处不存在 Fredholm 矛盾。

\section*{6.4 真正的全局测试张量与三阶下界}

\section*{6．4．1 从领圈长度模到闭基底的全纯 TT 张量}

在基底子领圈中令 $q_{0}=f(t)\left(d t^{2}-b^{2} d \theta^{2}\right)$ 。单节点退化的全纯二次微分集中定理提供全局实 TT 张量 $q_{\beta}$ ，满足
$$q_{\beta}=q_{0}+O_{C^{2}}\left(\beta^{2}\right) \text { 在剪切子领圈, } q_{\beta}=O_{C^{2}}\left(\beta^{2}\right) \text { 在其外. }$$
具体地，以角周期 $2 \pi$ 的共形坐标 $z$ 写，$q_{0}=\frac{\beta^{2}}{4 \pi^{2}} \operatorname{Re}\left(d z^{2}\right)$ ；若集中全纯二次微分 $\Omega_{\beta}$ 的主系数为 $b_{0} \asymp \beta^{3 / 2}$ ，取 $q_{\beta}=\operatorname{Re}\left(\frac{\beta^{2}}{4 \pi^{2} b_{0}} \Omega_{\beta}\right)$ 即得。其非主项与外部项的范数为 $O\left(\beta^{3 / 2}\right)$ ；乘归一化因子后成为 $O\left(\beta^{2}\right)$ 。 ${ }^{4}$

令 $\mathcal{Q}_{\varepsilon}=\pi^{*} q_{\beta}$ 。原度量 $G_{\varepsilon}$ 的水平叶全测地、纤维极小，所以
$$\operatorname{tr}_{G_{\varepsilon}} \mathcal{Q}_{\varepsilon}=0, \quad \operatorname{div}_{G_{\varepsilon}} \mathcal{Q}_{\varepsilon}=0 .$$
这是背景度量的性质，不要求扰动后仍为下沉。面积固定与 $\left|q_{0}\right|_{*}=2 f$ 给
$$\begin{aligned}
\int\left|\mathcal{Q}_{\varepsilon}\right|_{*} d V & =8 \pi^{2}(p-1) \beta+O\left(\beta^{2}\right) \\
\left\|\mathcal{Q}_{\varepsilon}\right\|_{2}^{2} & =4 \pi^{2}(p-1) \beta+O\left(\beta^{2}\right) \\
\int\left\langle\Phi\left(G_{\varepsilon}\right), \mathcal{Q}_{\varepsilon}\right\rangle d V & =-\frac{\varepsilon^{3} \beta}{2 \pi^{2}}(1+o(1))
\end{aligned}$$
最后一式由水平块（ $-v^{2} / 2,0$ ）直接积分；两个径向积分均为 $\int \operatorname{sech}^{3}=\pi / 2$ 。

\section*{6．4．2 保留伴随缺陷后仍得到非线性下界}

一般背景上应使用
$$J_{g} h=\frac{1}{2}\left(\nabla^{*} \nabla h-2 \stackrel{\circ}{R} h\right)+\frac{1}{2}(\Phi(g) \circ h+h \circ \Phi(g)), \quad D \Phi_{g} h=J_{g} h-\delta_{g}^{*} \mathfrak{b}_{g} h .$$
$J_{g}$ 自伴；非 Einstein 背景的 $\Phi(g)$ 项不可省略。 $\mathcal{Q}_{\varepsilon}$ 并不是精确伴随核。剪切大小及前两阶导数为 $O(\varepsilon r(u))$ ，因此
$$\left|J_{G} \mathcal{Q}_{\varepsilon}\right| \leq C \varepsilon r(u)\left(f(t)+\beta^{2}\right), \quad\left\|J_{G} \mathcal{Q}_{\varepsilon}\right\|_{1} \leq C \varepsilon^{2} \beta .$$
点态缺陷可以是一阶；额外小因子来自实际纤维体积权重。闭流形分部积分给
$$\int\left\langle D \Phi_{G} h, \mathcal{Q}_{\varepsilon}\right\rangle=\int\left\langle h, J_{G} \mathcal{Q}_{\varepsilon}\right\rangle .$$
对任意全局光滑对称张量 $h_{\varepsilon}$ ，令 $a_{\varepsilon}=\left\|h_{\varepsilon}\right\|_{C^{2}\left(G_{\varepsilon}\right)}, g_{\varepsilon}=G_{\varepsilon}+h_{\varepsilon}$ 。固定小邻域内，局部展开给 $\left|\Phi(G+h)-\Phi(G)-D \Phi_{G} h\right| \leq C a_{\varepsilon}^{2}$ 。结合（6．25）得到
$$c \varepsilon^{3} \leq C \delta\left(g_{\varepsilon}\right)+C \varepsilon^{2} a_{\varepsilon}+C a_{\varepsilon}^{2} .$$

\footnotetext{
${ }^{4}$ M．Rupflin and P．Topping，Teichmüller harmonic map flow into nonpositively curved targets，Lemma 4．4， （4．17）－（4．22）：https：／／arxiv．org／pdf／1403．3195．本章只需该特定单节点族的集中二次微分。 $C^{2}$ 估计另由全纯方程在固定半径双曲覆盖上的内部估计得到；不以注入半径正下界为前提。
}

特别地，任意全局 $O_{C^{2}}\left(\varepsilon^{2}\right)$ 校正都满足
$$\liminf _{\varepsilon \rightarrow 0} \frac{\delta\left(g_{\varepsilon}\right)}{\varepsilon^{3}} \geq \frac{1}{16 \pi^{4}(p-1)}$$
与（6．23）合起来，已经构造的 $\widetilde{G}_{\varepsilon}$ 具有 $\delta=\Theta\left(\varepsilon^{3}\right)$ 。若要使 $\delta=o\left(\varepsilon^{3}\right)$ 且 $a_{\varepsilon} \rightarrow 0$ ，必要条件为
$$a_{\varepsilon} \geq c \varepsilon^{3 / 2} .$$
允许任意张量分量、任意支撑、任意角向依赖；但这是指定近似族附近的尺度限制，其下界仍趋零。

若仅要求校正紧支于基底领圈，则同一证明直接用局部 $q_{0}$ 和乘积线性化完成，不需全局二次微分。该版本允许任意 $\beta(\varepsilon) \rightarrow 0$ ，首系数仍为（6．28）。若支撑进一步限于两个子领圈之积，则核范数质量较小，首系数提高为 $e^{2} /\left(16 \pi^{3}\right)$ ；这个 $e^{2}$ 来自安全边距$R=w(\varepsilon)-2$ ，不具有维数普适意义。

同一配对还有明确的线性后果：若 $J_{G} h=\mathcal{Q}_{\varepsilon}$ 可解，则 $\|h\|_{\infty} \geq c \varepsilon^{-2}$ ；若 $J_{G} h=$ $-\Phi(G)$ 可解，则 $\|h\|_{\infty} \geq c \varepsilon$ 。前者用 $\|\mathcal{Q}\|_{2}^{2}$ ，后者用源配对，均保留 $\left\|J_{G} \mathcal{Q}\right\|_{1}$ 。不能将这些线性幅度下界替换为更强的非线性不存在结论。

\section*{6.5 整个共形类的控制与一个真实的临界抵消}

\section*{6．5．1 共形变换可以消去一个投影，却破坏其他方程}

对任意实光滑函数 $w$ ，四维共形公式及 $\mathcal{Q}$ 的 TT 性给精确恒等式
$$\int\left\langle\Phi\left(e^{2 w} G\right), \mathcal{Q}\right\rangle d V_{G}=I_{\varepsilon}+2 \int \mathcal{Q}(\nabla w, \nabla w) d V_{G}, \quad I_{\varepsilon}=-\frac{\varepsilon^{3} \beta}{2 \pi^{2}}(1+o(1))$$
Hessian 项由闭流形分部积分消失，纯迹项逐点消失。取固定非负 $\psi \in C_{c}^{\infty}(-1,1)$ 、 $\max \psi=1$ ，从基底领圈拉回，令
$$B_{\varepsilon}=\int \mathcal{Q}(d \psi, d \psi) d V_{G}=4 \pi(p-1) \beta\left(\int \operatorname{sech} t\left(\psi^{\prime}\right)^{2} d t+O\left(\beta^{2}\right)\right)>0$$
取 $w_{\varepsilon}=\sqrt{-I_{\varepsilon} /\left(2 B_{\varepsilon}\right)} \psi$ ，其大小为 $\Theta\left(\varepsilon^{3 / 2}\right)$ ，（6．30）恰为零。但在 $w$ 的最大点，$d w=0$ 、 $\Delta w \leq 0$ ，由
$$s_{e^{2 w} G}=e^{-2 w}\left(-4-v^{2} / 2-6 \Delta w-6|d w|^{2}\right)$$
得到 $s+4 \geq c \varepsilon^{3 / 2}$ ，因此这个实际闭度量的完整误差为 $\Theta\left(\varepsilon^{3 / 2}\right)$ 。它证明二次投影不能预先取有利符号，并未构造更好的近似解。

\section*{6．5．2 任意大小的共形因子都会被小残差重新限制}

设 $g=u^{2} G_{\varepsilon}, u>0$ 任意，$\delta(g)$ 足够小。写 $e=s_{g}+4 、 V_{\varepsilon}=v^{2} / 2$ ，则
$$-6 \Delta_{G} u-\left(4+V_{\varepsilon}\right) u=(-4+e) u^{3}, \quad|e| \leq 4 \delta(g) .$$

最大值原理给
$$\frac{4}{4+4 \delta(g)} \leq(\min u)^{2} \leq(\max u)^{2} \leq \frac{4+\left\|V_{\varepsilon}\right\|_{\infty}}{4-4 \delta(g)} .$$
故 $\|u-1\|_{\infty}+\|\Delta u\|_{\infty} \leq C\left(\varepsilon^{2}+\delta(g)\right)$ 。在固定半径局部覆盖上作 $W^{2, r}$ 内部估计（ $r>4$ ），得到一阶导数界；再将完整共形 Ricci 公式
$$\Phi\left(u^{2} G\right)=\Phi(G)+\left(u^{2}-1\right) G-2 u^{-1} \nabla^{2} u+4 u^{-2} d u \otimes d u-\left(u^{-1} \Delta u+u^{-2}|d u|^{2}\right) G$$
中的 Hessian 单独移项，得到
$$\left\|u^{2} G_{\varepsilon}-G_{\varepsilon}\right\|_{C^{2}\left(G_{\varepsilon}\right)} \leq C\left(\varepsilon^{2}+\delta(g)\right) .$$
这个 Hessian 步骤必须使用完整 Ricci 方程，不能由 $\|\Delta u\|_{\infty}$ 直接推出。代入（6．27），对所有正光滑 $u$ 得 $\delta\left(u^{2} G_{\varepsilon}\right) \geq c \varepsilon^{3}$ ，任意序列仍满足（6．28）的首系数。换用 $\widetilde{G}_{\varepsilon}$ 为背景，则标量误差为三阶；同一证明给
$$\inf _{u>0} \delta\left(u^{2} \widetilde{G}_{\varepsilon}\right)=\Theta\left(\varepsilon^{3}\right) .$$
不声称下确界达到。原始 $G_{\varepsilon}$ 的共形类只得三阶下界；三阶张量校正通常不在这个共形类内，故不能把它的上界算作原共形类的达到性。

\section*{6．5．3 保留乘积开集还可排除共形类中任意常数的 Einstein 度量}

设闭连通 $M$ 不承载非正截面曲率度量，而 $G$ 在非空开集上为两个 $K=-1$ 曲面的局部积。若 $\widehat{G}=f^{-2} G$ 为 Einstein，共形 Ricci 公式的无迹部分给 $\nabla^{2} f=\psi G$ 。积坐标内的混合 Hessian 为零，故 $f=f_{1}(x)+f_{2}(y)$ ；两个对角方程迫使 $\psi$ 为常数。取散度，再用两个因子的 Ric $=-g$ ，得到 $d f_{1}=d f_{2}=0$ 。因此 $\widehat{G}$ 在该开集为常数倍局部对称乘积。

Einstein 度量在调和坐标中实解析，所以解析张量 $\widehat{\nabla} \operatorname{Rm}_{\widehat{G}}$ 从这个开集延拓为全局零。 ${ }^{5}$ 平行移动保持曲率张量，便将乘积的非正截面曲率传播到整个 $M$ ，矛盾。 $E_{D}$ 的无非正截面曲率性质在本章拓扑部分说明；$G_{\varepsilon} 、 \widetilde{G}_{\varepsilon}$ 均保留非空精确乘积开集，故各自整个共形类不含任何 Einstein 度量。这仍允许其他共形类中的 Einstein 度量。

\section*{6.6 精确标量归一化与五阶体积首项}

对于任意闭四维度量 $g$ ，若 $s_{g}=-4-Q 、\|Q\|_{\infty}<1$ ，负常标量方程为
$$-6 \Delta_{g} u-(4+Q) u+4 u^{3}=0 .$$
常数 $\sqrt{1-\|Q\|_{\infty} / 4}$ 与 $\sqrt{1+\|Q\|_{\infty} / 4}$ 是下、上解，单调迭代给正光滑解。两个解之比的最大值原理给唯一性和 $\|u-1\|_{\infty} \leq C\|Q\|_{\infty}$ 。对显式族的统一局部覆盖，源的固定

\footnotetext{
${ }^{5}$ D．DeTurck and J．Kazdan，Some regularity theorems in Riemannian geometry，Theorem 5．2：https：／／www．numdam．org／item／10．24033／asens．1405．pdf．这里只用 Einstein 解析性，不使用另需单连通假设的全局度量比较结论。
}

阶导数也小，椭圆提升给相同阶的 $C^{k+2}$ 控制。因此原始二阶族和三阶族均可共形归一化为 $s \equiv-4$ ，并保持各自的 Ricci 误差阶数；这一步没有解决无迹 Ricci 方程。

对于原始双领圈族，$Q=v^{2} / 2 \geq 0$ 且 $\mathcal{A}_{\varepsilon}=\int Q=\varepsilon^{5} / \pi^{2}+O\left(\varepsilon^{7}\right)$ 。唯一归一化因子满足 $1 \leq u \leq \sqrt{1+\|Q\|_{\infty} / 4}$ 。积分 $w=u-1$ 的方程先给 $\int w=\mathcal{A}_{\varepsilon} / 8+O\left(\|Q\|_{\infty} \mathcal{A}_{\varepsilon}\right)$ ，于是
$$\operatorname{Vol}\left(u^{2} G_{\varepsilon}\right)=V_{0}+\frac{\varepsilon^{5}}{2 \pi^{2}}+O\left(\varepsilon^{7}\right)$$
此处余项比张量三阶校正后的对应公式更强；两个不同族不可混用。
三阶族的体积需要重新计算。为 $A$ 增加超解 $f B$ ：由（6．18）有
$$H_{A}(f B)=\frac{c_{0}^{2}}{2} f r^{2}+4 f^{2} B, \quad 0 \leq A \leq f B .$$
结合（6．21），
$$A \leq C \min \left(e^{-|t|-2|u|}, e^{-2|t|-|u|}\right), \quad \int A d \mu_{0}=\frac{1}{2 \pi^{2}}$$
积分常数来自对 $H_{A} A$ 积分：两个方向的通量消失， $2 \int A=\left(c_{0}^{2} / 2\right)(\pi)(\pi / 2)$ 。 $A$ 的尾积分为 $O\left((R+1) e^{-R}+(L+1) e^{-L}\right)$ 。仅有 $A \leq C T r$ 尚不足以证明这个加权 $L^{1}$ 性质。

在背景纤维标架中，$G_{\varepsilon}$ 的剪切矩阵为 $\left(\begin{array}{cc}1+m^{2} & m \\ m & 1\end{array}\right)$ ，其中 $m=\varepsilon \tau \chi_{R} r / I_{R}$ 。所以真正的迹为 $\operatorname{tr}_{G_{\varepsilon}} K=2 A-C m^{2}$ 。行列式展开与角向体积因子 $\varepsilon \beta=\varepsilon^{3}$ 给
$$\operatorname{Vol}\left(\widetilde{G}_{\varepsilon}\right)=V_{0}+\frac{\varepsilon^{5}}{2 \pi^{2}}+O\left(\varepsilon^{6} \log (1 / \varepsilon)\right) .$$
其中 $\int|K|^{2} d V=O\left(\varepsilon^{3}\right), C m^{2}$ 项至多贡献 $O\left(\varepsilon^{7}(1+L)\right)$ 。体积从上方趋近 $V_{0}$ ，并未越过允许端点制造矛盾。

令 $\mathcal{S}(g)=\operatorname{Vol}(g)^{-1 / 2} \int s_{g} d V_{g}$ 。原始族中直接积分得 $\int v^{2} d V=2 \varepsilon^{5} / \pi^{2}+O\left(\varepsilon^{7}\right)$ 。二阶校正的 $H^{1}$ 质量及曲率界使泛函的一、二次变分改变均为 $O\left(\varepsilon^{7}\right)$ ，故
$$\mathcal{S}\left(\widetilde{G}_{\varepsilon}\right)=-4 \sqrt{V_{0}}-\frac{\varepsilon^{5}}{\pi^{2} \sqrt{V_{0}}}+O\left(\varepsilon^{7}\right), \quad \int\left(s_{\widetilde{G}_{\varepsilon}}+4\right) d V=O\left(\varepsilon^{6} \log (1 / \varepsilon)\right)$$
固定轮廓及 $\partial_{\log \varepsilon} R, \partial_{\log \varepsilon} L=O(1)$ 允许对这些实际积分求导，给
$$\partial_{\log \varepsilon} \mathcal{S}=-\frac{5 \varepsilon^{5}}{\pi^{2} \sqrt{V_{0}}}+O\left(\varepsilon^{7}\right)<0$$
这是从参数表达式证明的余项导数控制，不是任意大 $O$ 的形式求导。故此明确三阶族没有偶然的 Einstein 成员。

对 $\widetilde{G}_{\varepsilon}$ 作唯一的标量—4共形归一化，写 $u=1+w$ 。积分
$$(-6 \Delta+8) w=Q+Q w-12 w^{2}-4 w^{3}$$
得 $8 \int w=\int Q+O\left(\varepsilon^{6}\right)$ 。结合（6．34），归一化体积仍满足（6．33），且
$$Y\left(\left[\widetilde{G}_{\varepsilon}\right]\right)=-4 \sqrt{V_{0}}-\frac{\varepsilon^{5}}{\pi^{2} \sqrt{V_{0}}}+O\left(\varepsilon^{6} \log (1 / \varepsilon)\right) .$$

这是单个共形类的 Yamabe 值，不能与所有共形类的上确界混同。对于任意标量 -4的背景 $\widehat{g}$ ，将 $z>0$ 常数重标度至 $\int z^{4} d V=V$ 后，还有精确共形能量差
$$\mathcal{S}\left(z^{2} \widehat{g}\right)-\mathcal{S}(\widehat{g})=\frac{6 \int|d z|^{2}+2 \int\left(z^{2}-1\right)^{2}}{\sqrt{V}} \geq 0$$
等号只在 $z=1$ 达到；该恒等式只控制共形方向。

\section*{6.7 原始与修正背景的谱：不能借小距离转移符号}

在原始 $G_{\varepsilon}$ 上，基底全纯 TT 张量的拉回空间 $\mathcal{B}_{\varepsilon}$ 维数为 $6 q-6$ 。其每个元素$Q$ 都为全空间 TT。固定纤维度量、只变基底 $b \mapsto b+s q$ 时，坐标型水平 Ricci 为$\operatorname{Ric}_{i j}=\operatorname{Ric}_{b, i j}-\operatorname{tr}\left(S_{i} S_{j}\right)$ ；TT 变分使 $D \operatorname{Ric}_{b}(q)=-q$ 。混合块也不变。因此 $J_{G} Q$ 只有垂直块，并有精确式
$$\left(J_{G} Q\right)_{F F}=q\left(\partial_{t}, \partial_{t}\right)\left(\begin{array}{cc}
v^{2} / 2 & \left(v_{t}-k v\right) / 2 \\
\left(v_{t}-k v\right) / 2 & -v^{2} / 2
\end{array}\right)_{\mathrm{ON}} .$$
故 $\left\langle J_{G} Q_{1}, Q_{2}\right\rangle=0$ 逐点成立。若 $J_{G} Q=0$ ，剪切开集上必有 $q_{t t}=0$ 。领圈共形坐标中相应全纯系数于是为纯虚常数。若常数非零，提升到上半平面后全纯二次微分在开集上为常数倍 $(d w / w)^{2}$ ，解析延拓使其处处无零，与闭曲面上零点总次数 $4 q-4>0$ 矛盾。因此 $\left.J_{G}\right|_{\mathcal{B}_{\varepsilon}}$ 单射。

将 $L^{2}$ 分解为负谱、核与正谱。若 $Q \in \mathcal{B}_{\varepsilon}$ 的负谱投影为零，由 $\left\langle J_{G} Q, Q\right\rangle=0$ 得 $Q$在核中，进而 $Q=0$ 。所以
$$\operatorname{index} \_\left(J_{G_{\varepsilon}}\right) \geq 6 q-6 \text {. }$$
这是非 Einstein 背景 Jacobian 的负指数，不是某个精确 Einstein 解的不稳定性结论。
对集中主模式 $Q=\mathcal{Q}_{\varepsilon}$ ，令 $Z=J_{G} Q$ 。从（6．35）与 $v=\varepsilon c_{0} r \operatorname{sech} t+o(\varepsilon)$ 得
$$\|Z\|_{2}^{2} \sim \frac{\varepsilon^{3} \beta}{4 \pi^{2}}, \quad \frac{\left\langle J_{G} Z, Z\right\rangle}{\|Z\|_{2}^{2}} \rightarrow 2, \quad \frac{\|Z\|_{2}^{2}}{\|Q\|_{2}^{2}} \sim \frac{\varepsilon^{3}}{16 \pi^{4}(p-1)} .$$
其中极限张量是
$$-c_{0} r \tanh t \operatorname{sech}^{3} t\left(e^{2} \otimes e^{3}+e^{3} \otimes e^{2}\right) .$$
其 Rayleigh 商为 $\frac{1}{2} \int\left(\varphi^{\prime}\right)^{2} \cosh t / \int \varphi^{2} \cosh t=2$ 。单位化 $\{Q, Z\}$ 压缩矩阵为 $\left(\begin{array}{cc}0 & s_{\varepsilon} \\ s_{\varepsilon} & d_{\varepsilon}\end{array}\right)$ ， $d_{\varepsilon} \rightarrow 2$ ，因此
$$\limsup \frac{\lambda_{\min }\left(J_{G_{\varepsilon}}\right)}{\varepsilon^{3}} \leq-\frac{1}{32 \pi^{4}(p-1)} .$$
没有匹配下界，也没有证明所有负特征值具有该尺度。
三阶校正背景 $\widetilde{G}_{\varepsilon}$ 需要重新计算。对 $g_{0}+\eta K$ 和 $Q_{0}=f T_{1}$ ，水平曲率变分及 $\operatorname{tr}_{g_{2}}\left(C T_{2}\right)=0$ 给
$$\left.\partial_{\eta}\right|_{0}\left\langle J_{g_{0}+\eta K} Q_{0}, Q_{0}\right\rangle=\int\left(2 A-P_{t} A\right) f^{2} d \mu_{0}$$

令 $\bar{A}(t)=\int A \cosh u d u$ ，则 $\left(-P_{t}+2\right) \bar{A}=f / \pi^{3}$ 。因此该积分恰为 $3 /\left(8 \pi^{2}\right)$ 。剪切、全局 TT 非主项和固定宽度截断均贡献低阶，得到
$$\left\langle J_{\widetilde{G}} Q, Q\right\rangle=\frac{3 \varepsilon^{3} \beta}{8 \pi^{2}}+o\left(\varepsilon^{3} \beta\right) .$$
原来的二维压缩现在正定，其较小 Ritz 值为
$$\frac{\varepsilon^{3}}{16 \pi^{4}(p-1)}+o\left(\varepsilon^{3}\right)>0 .$$
这不证明整个算子正定或可逆。 $O\left(\varepsilon^{2}\right)$ 度量接近大于这里的 $\varepsilon^{3}$ 谱尺度，故不能靠未经定量的连续性传递负谱。

在更大但仍明确的垂直响应类 $F=\varphi(t) r(u) M$ 中，$M=e^{2} \otimes e^{3}+e^{3} \otimes e^{2}$ ，令
$$W=-c_{0} r \tanh t \operatorname{sech}^{3} t M, \quad Y=-\frac{c_{0}}{2} r \tanh t \operatorname{sech} t M .$$
有 $J_{0} Y=W 、\langle W, Y\rangle=1 /\left(4 \pi^{2}\right)$ ，且
$$\frac{\left\langle J_{\widetilde{G}}(Q+\varepsilon \Psi F), Q+\varepsilon \Psi F\right\rangle}{\varepsilon^{3} \beta} \longrightarrow \frac{1}{8 \pi^{2}}+\left\langle J_{0}(F+Y), F+Y\right\rangle .$$
该类的最优首项仍为正，由 $F=-Y$ 达到，相应试探 Rayleigh 商为 $\varepsilon^{3} /\left[32 \pi^{4}(p-1)\right]+$ $o\left(\varepsilon^{3}\right)$ 。这里没有优化整个正交补，也没有无条件使用 Schur 补逆。

\section*{6.8 精确线性模型：良好的 $L^{2}$ 谱并不控制最大范数逆}

\section*{6．8．1 允许全部张量分量的领圈 TT 投影}

在精确背景 $d t^{2}+\ell^{2} \cosh ^{2} t d \theta^{2}+h_{0}$ 上，固定闭纤维 TT 核张量 $q_{F}, \int\left|q_{F}\right|^{2}=1$ 。对任意对称张量 $h$ ，取其垂直块与 $q_{F}$ 的纤维配对并作圆周平均，记结果 $a_{h}(t)$ 。乘积连接保持张量类型，纤维算子自伴，圆周平均消去角向 Laplacian，因此
$$\Pi_{q_{F}}(\mathcal{L} h)=\frac{1}{2} \mathcal{A}_{L} a_{h}, \quad \mathcal{A}_{L} a=-a^{\prime \prime}-\tanh t a^{\prime}=-\frac{1}{\cosh t}\left(\cosh t a^{\prime}\right)^{\prime} .$$
纯水平、混合张量及纯规范项都不能在线性阶贡献此投影。
记 $J(t)=\int_{0}^{t} \operatorname{sech} s d s 、 I_{L}=J(L)-J(-L)$ 。给定端点 $0, d$ ，齐次解为 $a_{\mathrm{harm}}=d[J(t)- J(-L)] / I_{L}$ ，导数集中在固定宽度核心。Dirichlet 逆则由 $m_{L}=\log \cosh L-\log \cosh t$ 、 $\mathcal{A}_{L} m_{L}=1$ 精确给出
$$\left\|\mathcal{A}_{L, D}^{-1}\right\|_{\infty \rightarrow \infty}=\log \cosh L$$
另一方面，乘 $\sqrt{\cosh t}$ 共轭后的势为 $1 / 4+\operatorname{sech}^{2} t / 4$ ，故 Dirichlet $L^{2}(\cosh t d t)$ 逆范数至多 4。

对慢路径 $a_{L}=d \eta(t / L)$ ，残差为 $O(|d| / L)$ ；零端点的唯一第一次校正是 $a_{\mathrm{harm}}-a_{L}$ 。在 $t= \pm \sqrt{L}$ 取极限得
$$\liminf \left\|a_{\text {harm }}-a_{L}\right\|_{\infty} \geq|d| / 2 .$$

若 $a$ 在端部常值，$r=\frac{1}{2} \mathcal{A}_{L} a$ ，Green 配对还给
$$\int \cosh t r d t=0, \quad \int J(t) \cosh t r d t=d / 2$$
真实体积权重包含 $\ell$ ；提取固定 $d$ 的检验函数必须是 $J / \ell$ ，其最大范数发散。不能忽略此因子制造假矛盾。

\section*{6．8．2 闭乘积的全部核与精确正谱隙}

对于闭双曲曲面 $F, B$ ，取 $\Delta_{E}=\nabla^{*} \nabla-2 \stackrel{\circ}{R}$ 。一形式 Bochner 公式是 $\Delta_{H}=\nabla^{*} \nabla-I$ 。故整个混合块满足
$$\left.\Delta_{E}\right|_{T^{*} F \odot T^{*} B}=\Delta_{H, F}^{(1)}+\Delta_{H, B}^{(1)}+2 I .$$
两因子的谐和一形式对称积是 TT，Einstein 特征值恰为2，归一化方程线性化特征值为 1 ；它们虽属于通常 $\Delta_{L}=\Delta_{E}-2 I$ 的核，却不属于 $D(\operatorname{Ric}+g)$ 的核。

在单个闭双曲曲面上，令
$$(P \alpha)_{i j}=\frac{1}{2}\left(\nabla_{i} \alpha_{j}+\nabla_{j} \alpha_{i}\right)+\frac{1}{2}(\delta \alpha) g_{i j} .$$
交换导数给 $\delta P=\frac{1}{2}\left(\Delta_{H}+2\right) 、 \Delta_{E}(P \alpha)=P\left(\Delta_{H}+2\right) \alpha 、 \Delta_{E}(f g)=(\Delta f+2 f) g$ 。全体对称张量正交分解成纯迹、 $\operatorname{im} P$ 和全纯 TT 部分。后者是核，其余谱至少为 2 。乘积三个平行张量块的谱和于是给
$$\begin{aligned}
\operatorname{ker} \Delta_{E} & =\pi_{F}^{*} \mathcal{T}_{F} \oplus \pi_{B}^{*} \mathcal{T}_{B}=: \mathcal{K}, \\
\operatorname{dim} \mathcal{K} & =6 p+6 q-12, \\
\operatorname{infspec}\left(\left.\Delta_{E}\right|_{\mathrm{TT} \cap \mathcal{K}^{\perp}}\right) & =\min \left\{2, \lambda_{1}(F), \lambda_{1}(B)\right\} .
\end{aligned}$$
三个可能最小值由 $g_{F}-g_{B} 、 \varphi_{B} k_{F} 、 \varphi_{F} k_{B}$ 这些 TT 张量达到。乘积核及因子可积性还表明：固定闭乘积附近，模微分同胚的全部归一化 Einstein 度量均来自两个因子的Teichmüller 形变。 ${ }^{6}$

只捏缩一条非分离曲线且其他模参数固定时，$\lambda_{1}\left(B_{\ell}\right) \geq c>0$ 。 一个直接证明是：领圈零边界函数由共轭公式满足 $\|v\|_{2}^{2} \leq 4\|d v\|_{2}^{2}$ ；去掉中央长领圈后的厚核心连通且几何不退化，故有统一 Neumann Poincaré 常数。对 $\chi\left(f-\bar{f}_{\text {core }}\right)$ 使用领圈估计，再在过渡带使用核心估计，得到整个闭曲面的统一 Poincaré 不等式。非分离性保证只需减去一个核心常数。

若捏缩的是分离曲线，两个核心常数之差可在中央面积 $O(\ell)$ 的带内过渡，得到$\lambda_{1}\left(B_{\ell}\right) \leq C \ell$ ；由 $\varphi_{B} k_{F}$ ，完整 Einstein 正谱也趋零。这两种退化不能混用。

\footnotetext{
${ }^{6}$ L．Andersson and V．Moncrief，Einstein spaces as attractors for the Einstein flow，§2．5．2、Lemma 3．2、 Proposition 3．3、Corollary 3．4：https：／／arxiv．org／pdf／0908．0784．乘积谱公式亦见 K．Kröncke，On infinites－ imal Einstein deformations，Proposition 4．1：https：／／arxiv．org／html／1508．00721v1．这些是既有理论在闭曲面积上的应用，不是 $E_{D}$ 的全局刚性。
}

\section*{6．8．3 闭流形、去掉全部真实核后仍有对数最大范数损失}

取固定 $F$ 与上述单非分离退化 $B_{\ell}$ ，度量 $G_{\ell}=g_{F}+g_{B_{\ell}}$ 本身就是 Einstein。令完整领圈半宽为 $w_{\ell}$ ，取端部截断 $\chi$ ，定义
$$m_{\ell}=\log \cosh w_{\ell}-\log \cosh t, \quad v_{\ell}=\chi\left(w_{\ell}-|t|\right) m_{\ell}, \quad a_{\ell}=v_{\ell}-\frac{1}{\operatorname{Area}\left(B_{\ell}\right)} \int_{B_{\ell}} v_{\ell} d A$$
在领圈外零延拓 $v_{\ell}$ ，它全局光滑。核心 $\Delta v_{\ell}=1$ ，端部保留使 $\int \Delta v_{\ell}=0$ 的负源；任意固定阶 $\left\|\Delta v_{\ell}\right\|_{C^{r}}$ 一致有界。令 $x=w_{\ell}-|t|$ ，则 $m_{\ell} \leq x 、 \ell \cosh \left(w_{\ell}-x\right) \leq C\left(e^{-x}+\ell\right)$ ，故每个有限 $r$ 都有 $\left\|v_{\ell}\right\|_{L^{r}} \leq C_{r}$ ，均值有界，而 $\left\|a_{\ell}\right\|_{\infty} \geq \log \cosh w_{\ell}-C$ 。

固定 $\left\|k_{F}\right\|_{\infty}=1$ 的纤维 Teichmüller 核张量，置 $h_{\ell}=a_{\ell} k_{F}$ 。它是 TT； $\int a_{\ell}=0$使它正交于纤维核，与基底核则逐点正交。因此 $h_{\ell} \in \mathcal{K}_{\ell}^{\perp}$ ，且
$$J_{\ell} h_{\ell}=\frac{1}{2}\left(\Delta_{B_{\ell}} v_{\ell}\right) k_{F}, \quad\left\|h_{\ell}\right\|_{\infty} \geq c \log (1 / \ell)-C, \quad\left\|J_{\ell} h_{\ell}\right\|_{C^{r}} \leq C_{r} .$$
故真实去核逆的 $C^{r} \rightarrow C^{0}$ 范数至少对数增长，虽然（6．42）在该族上给统一正 $L^{2}$ 谱隙。归一化 $h_{\ell} /\left\|h_{\ell}\right\|_{\infty}$ 的任意有限 $L^{r}$ 范数趋零，故它不是反驳 $L^{2}$ 谱隙的归一化近核序列。

以上模型已去掉边界与真实核两种借口，却仍发生最大范数逆损失；但背景自身就是精确 Einstein 度量。它诊断的是一种无效的统一存在性推断，不能作为原问题的反例。

\section*{6.9 曲面丛候选的拓扑、精确全局不变量与 Einstein 必要条件}

本节固定一个确已具有任意紧负 Ricci 夹逼序列的闭四维候选，并把它的拓扑结论、变分结论和精确 Einstein 方程的条件结论分开。这些材料的共同限制是：尚未排除该流形上的所有 Einstein 度量。以下组合推导经过本次公式与前提复查；除明确标注的经典定理外，不声称已经完成文献首创性认证。

\section*{6．9．1 固定对象与拓扑识别}

令 $F=\Sigma_{p} 、 B=\Sigma_{q}, p, q \geq 2$ 。在 $F$ 上取非分离简单闭曲线 $\alpha$ ，令 $D$ 为其正 Dehn twist；选择支集外的固定基点。令 $u: \pi_{1}(B) \rightarrow \mathbb{Z}$ 为本原满同态。本文的 $E_{D}$ 是单值变换
$$\rho(\gamma)=[D]^{u(\gamma)}$$
所定义的光滑定向曲面丛。记
$$G=\pi_{1}\left(E_{D}\right)=\Pi_{p} \rtimes_{D_{*}^{u(\cdot)}} \Pi_{q}, \quad \Pi_{r}=\pi_{1}\left(\Sigma_{r}\right), \quad c=\chi\left(E_{D}\right), \quad V_{0}=4 \pi^{2} c .$$
支集外固定点给出截面，从而半直积写法有实际几何依据。纤维、基底均非球面，纤维丛同伦正合列使 $E_{D}$ 也是 $K(G, 1)$ 。直接计算得到
$$\chi\left(E_{D}\right)=4(p-1)(q-1), \quad \tau\left(E_{D}\right)=0, \quad H_{1}\left(E_{D^{k}} ; \mathbb{Z}\right) \cong \mathbb{Z}^{2 p+2 q-1} \oplus \mathbb{Z} /|k| \mathbb{Z} \quad(k \neq 0) .$$
这里 $b_{1}\left(E_{D}\right)=2 p+2 q-1$ 为奇数，两个取向上的 $b_{+}$均大于1。

签名计算不依赖对手术图的猜测。将 $E_{D}$ 写成三维映射环面 $T_{D} \rightarrow S^{1}$ 沿 $B \rightarrow S^{1}$的拉回。若 $V$ 是垂直切丛，则 $e(V)^{2}$ 从三维空间拉回，故为零。再用
$$T E_{D} \cong V \oplus \pi^{*} T B, \quad p_{1}\left(T E_{D}\right)=e(V)^{2}+\pi^{*} e(T B)^{2}$$
和签名定理即得 $\tau=0$ 。 一阶同调则由分裂群扩张的交换化给出：$H_{1}\left(E_{D^{k}}\right)=H_{1}(B) \oplus \operatorname{coker}\left(D_{*}^{k}-I\right)$ ，非分离扭转的同调作用是秩一 transvection。

面积保持的单值代表给两个取向上的辛形式 $\omega_{ \pm}=\mu_{F} \pm \mu_{B}$ 。相应典范类可选为
$$a_{+}=-e_{V}-e_{B}, \quad a_{-}=-e_{V}+e_{B}, \quad e_{V}=e(V), \quad e_{B}=\pi^{*} e(T B) .$$
它们的平方在各自取向下均为 $2 c$ ；由 Taubes 非消失，它们分别是各取向的实际monopole 类。反取向类不能并入原取向的 monopole 类集合。

经典手术识别。取乘积 $F \times B$ 中的 Lagrangian 环面 $T=\alpha \times \gamma$ ，其中 $\gamma$ 是 $u$ 的 Poincaré对偶曲线。在乘积 framing 中记经向为 $a, b$ 、meridian 为 $\mu$ 。将新填充盘的边界指定为$\mu+k a$ 的 $1 / k$ Luttinger 填充，局部等价于沿基底割线重新粘接 $(s, v) \mapsto(s+k \zeta(v), v)$ ，故所得流形为 $E_{D^{ \pm k}}$ 。正负号由 meridian 与 twist 取向约定决定。这是局部手术模型的识别；不能把流形的拓扑类型当作新发现。Baldridge－Kirk 的 Lemma 2 提供这一机制的经典先例，但该引理的逐字陈述处理的是其文中的环面例子，当前高亏格识别仍由上述局部模型支撑。 ${ }^{7}$

适用范围的拓扑筛选。 任意 surface－by－surface 群中的可解子群 $S$ 满足
$$1 \longrightarrow A \longrightarrow S \longrightarrow B^{\prime} \longrightarrow 1, \quad A, B^{\prime} \in\{1, \mathbb{Z}\} .$$
因为闭高亏格曲面群的可解子群至多循环。因此 $S$ 虚阿贝尔、Hirsch 秩至多2：尤其$G$ 不含 $\mathbb{Z}^{3}$ 、非阿贝尔离散 Heisenberg 群或 Sol 三维格点群。这排除了将具有这些单射外围子群的图流形核心直接认作 $E_{D}$ 的可能。在商群里发现 Heisenberg 结构不等于原群含有该子群。

Sung 的乘积环面纤维和定理不能仅凭手术名称直接移用。其 meridian 粘接为$\mu_{1} \mapsto-\mu_{2}$ ，不同于上述 Luttinger 斜率。从同一 $F \times B$ 出发，只与 $S^{1} \times X_{j}$ 作该定理允许的外部纤维和，且手术圆在 $H_{1}\left(X_{j} ; \mathbb{Q}\right)$ 中非零时，Mayer－Vietoris 给
$$b_{1}(\widetilde{M})=2 p+2 q+\sum_{j}\left(b_{1}\left(X_{j}\right)-1\right) \geq 2 p+2 q$$
故不能得到单 twist 的 $E_{D}$ 。只作非空内部纤维和时，乘积环面补空间的边界 $\mathbb{Z}^{3}$ 在基本群上单射，HNN 正规形使其在粘接后保留，也不能得到高亏格曲面丛。这两项排除不覆盖任意混合手术序列。 ${ }^{8}$

\footnotetext{
${ }^{7}$ https：／／arxiv．org／pdf／math／0703065，Baldridge－Kirk，Constructions of small symplectic 4－manifolds using Luttinger surgery，§2．1、Lemma 2。
${ }^{8}$ https：／／arxiv．org／pdf／0710．2375，Sung，Surgery，Yamabe invariant，and Seiberg－Witten theory， Theorem 1．5。该定理不是任意 Luttinger 手术保持 Yamabe 值的声明。
}

还有一个不依赖单值形式的刚性筛选：
$$\Sigma_{p} \longrightarrow E \longrightarrow \Sigma_{q}, \quad E \simeq \Sigma_{r} \times \Sigma_{s} \quad \Longrightarrow \quad E \cong \mathfrak{d}_{\text {diff }} \Sigma_{r} \times \Sigma_{s} .$$
证明中，纤维正规群 $N$ 位于 $A \times C=\Pi_{r} \times \Pi_{s}$ 。 $N \cap A$ 与 $N \cap C$ 是 $N$ 中逐点交换的正规子群；曲面群中非平凡正规子群的中心化子平凡，故至少一者为1。不妨 $N \cap A=1$ 。与 $A$ 取交换子便得 $N \subset C$ ；商群 $A \times(C / N)$ 是曲面群，因而 $C / N=1$ 。所以纤维群为整个乘积因子，单值化平凡。最后由 $\operatorname{Diff}_{0}^{+}\left(\Sigma_{p}\right)$ 可缩，光滑曲面丛分类给出光滑乘积。 ${ }^{9}$ 因此不能在保持此光滑曲面丛条件的同时，自由换入一个假想的 exotic 乘积光滑结构。

保持已证明输入范围的两种拓扑操作。 对于单值表示通过标准几何自由群商的更广构造族，若全部生成元在纤维的小圆盘上恒等，可沿法向丛平凡的截面作逐纤维连接和。从纤维亏格 $p_{1}, p_{2}$ 得
$$p_{\text {new }}=p_{1}+p_{2}, \quad \chi\left(E_{\text {new }}\right)=4\left(p_{1}+p_{2}-1\right)(q-1), \quad \tau\left(E_{\text {new }}\right)=0 .$$
新的单值仍通过同一自由群商，故可重新应用慢插值构造。
若给定连通 $d$ 重纤维循环分歧覆盖，分歧点共 $r$ 个且完全分歧，并另外假设每个单值生成元都可提升，则新纤维亏格 $P$ 满足
$$P-1=d(p-1)+\frac{r(d-1)}{2}, \quad \chi(\widehat{E})=4(P-1)(q-1), \quad \tau(\widehat{E})=0 .$$
自由群关系使各提升可以分别选择，新总空间仍在已证明输入范围内。必须在新光滑丛上重新构造度量；分歧映射的直接度量拉回会退化，不能使用。这两种操作扩展候选范围，但仍不产生非零签名或异常球。

相反，依靠非平凡吹胀得到的无 Einstein 证书不能直接移入这个范围：aspherical曲面丛没有非零同调的异常二球。同样，即使另一构造实现相同基本群，仍需核对总空间的同伦型和光滑丛结构。对于实际为 Kodaira 纤维化的复几何分歧覆盖，负 Kähler－Einstein 存在性也不能被单值复杂性否定。这些是保持输入的构造操作与排错条件，没有组成完整反例。

\section*{6．9．2 有限覆盖上的复结构与非正曲率障碍}

任意有限覆盖均无复结构。设 $H \leq G$ 有限指数，$N=\Pi_{p}, K=H \cap N, Q^{\prime}$ 为 $H$ 在$\Pi_{q}$ 中的像。若 $a=[N: K] 、 b=\left[\Pi_{q}: Q^{\prime}\right]$ ，则覆盖度为 $d=a b$ 。对应覆盖仍是连通光滑曲面丛
$$\Sigma_{p^{\prime}} \longrightarrow \widehat{E} \longrightarrow \Sigma_{q^{\prime}}, \quad p^{\prime}=1+a(p-1), \quad q^{\prime}=1+b(q-1), \quad \tau(\widehat{E})=0 .$$
具体地，原投影提升为到 $Q^{\prime}$ 对应基底覆盖的 proper submersion；基本群满射保证纤维连通，Ehresmann 定理给出上述丛结构。

\footnotetext{
${ }^{9}$ https：／／doi．org／10．4310／jdg／1214428816，Earle－Eells，A fibre bundle description of Teichmüller theory。
}

覆盖的单值像仍无限。取 $\gamma \in H$ ，使其基底像的 $u$－值 $n \neq 0$ ；共轭作用 $\alpha \in$ $\operatorname{Aut}(N)$ 保持 $K$ ，其外作用为 $D^{n}$ 。若覆盖单值像有限，则存在 $m \geq 1, k \in K$ ，使 $\left.\alpha^{m}\right|_{K}=\left.\operatorname{Inn}(k)\right|_{K}$ 。曲面群具有唯一根性质，而每个 $x \in N$ 的某个正幂属于 $K$ ，故
$$\left.\beta\right|_{K}=\mathrm{id}, \quad \beta=\operatorname{Inn}\left(k^{-1}\right) \alpha^{m} \quad \Longrightarrow \quad \beta(x)^{r}=x^{r} \Longrightarrow \beta(x)=x .$$
于是 $\alpha^{m}$ 在 $N$ 上内，矛盾于非分离 twist 的非平凡同调作用 $x \mapsto x \pm n m(x \cdot[\alpha])[\alpha]$ 。
Kotschick 的定理准确断言：高亏格曲面丛承载复结构且签名为零，当且仅当其给定单值表示的像有限；无需预先假设原投影全纯。 ${ }^{10}$ 因此

每个连通有限覆盖 $\widehat{E} \rightarrow E_{D}$ 都不承载可积复结构，两个取向均如此。

更强的群论结论及其独立证明。 不能直接从四维无复结构推出群不是 Kähler 群。这里另有严格的覆盖构造：
$$\forall H \leq_{\text {f.i. }} G, \quad \exists H^{\prime} \leq_{\text {f.i. }} H, \quad b_{1}\left(H^{\prime}\right) \text { 为奇数. }$$
令 $N_{0} \triangleleft G$ 是 $H$ 的有限指数正规核心，置 $K_{0}=N_{0} \cap \Pi_{p} 、 B_{0}=N_{0} \cap \Pi_{q}$ 。二者有限指数，且 $K_{0} \rtimes B_{0} \leq N_{0} \leq H$ 。正规性使 $K_{0}$ 在 $D_{*}$ 下不变；取提升 twist 的适当正幂，并把 $B_{0}$ 再限制到 $u^{-1}(m \mathbb{Z})$ ，便使提升单值为 $\Phi=\prod_{i} T_{\gamma_{i}}^{a_{i}}$ ，其中 $\gamma_{i}$ 不交、 $a_{i}>0$ ，且在切割块上恒等。设切割对偶图为 $\Gamma, r=b_{1}(\Gamma)$ 。非分离曲线 $\alpha$ 的交数同态 $\Pi_{p} \rightarrow \mathbb{Z}$ 在有限指数 $K_{0}$ 上仍非零；它在各切割块上为零，故通过对偶图因子化，证明 $r \geq 1$ 。同调作用为
$$\Phi_{*}=I+A, \quad A(x)=\sum_{i} a_{i}\left\langle x,\left[\gamma_{i}\right]\right\rangle\left[\gamma_{i}\right], \quad A^{2}=0, \quad \operatorname{rank} A=r .$$
最后一个秩等式依赖所有系数同号：若 $C$ 的列为 $\left[\gamma_{i}\right]$ ，则 $A=C D C^{\top} J, D>0$ ，故其秩为曲线同调张成空间的维数；曲面切割正合列又把该维数识别为 $r$ 。对应分裂扩张的 $b_{1}=2 p_{1}+2 q_{1}-r$ 。若 $r$ 偶且非零，取 $\Gamma$ 的连通二重覆盖，沿曲面到对偶图的压缩映射拉回。多扭转在该图上恒等，故相容提升；新图的第一 Betti 数为 $2 r-1$ ，于是得到奇数 $b_{1}$ 的更深覆盖。若 $r$ 原本为奇数，无需最后一步。

紧 Kähler 流形及其有限覆盖的 $b_{1}$ 均为偶数，故
$$G \text { 的任何有限指数子群都不是任何复维数的紧 Kähler 群. }$$
注意量词是＂每个覆盖有更深的奇数 $b_{1}$ 覆盖＂，不是＂所有覆盖本身均有奇数 $b_{1}$＂。

非正截面曲率障碍是经典结果。 Kapovich－Leeb 已在同一个单 twist 循环单值构造上证明，$G$ 无忠实、proper 且半单的 CAT（0）等距作用，且相应离散半单作用的存在性对有限指数变换保持。这里 proper 是对群元素计数的适当性，不把平凡作用误算成允

\footnotetext{
${ }^{10}$ https：／／arxiv．org／pdf／math／9911255，Kotschick，On regularly fibered complex surfaces，Proposition 1、 Theorem 4。
}

许的离散作用。因此所有有限覆盖都无 $\sec \leq 0$ 度量。 ${ }^{11}$ 其单 twist 机制可直接看出。映射环面子群有关系
$$z a z^{-1}=a, \quad z b z^{-1}=b a, \quad z c_{i} z^{-1}=c_{i}, \quad z d_{i} z^{-1}=d_{i}, \quad[a, b] \prod_{i \geq 2}\left[c_{i}, d_{i}\right]=1$$
置 $v=b a b^{-1}$ ，则 $a, v, c_{i}, d_{i}$ 均与 $z$ 交换。在假设存在的半单 CAT（0）作用中， $\operatorname{Min}(z)= Y \times \mathbb{R}$ 给中心化子的共同平移同态 $\tau$ 。曲面关系给 $\tau(a)=\tau(v)$ ，而 $a z$ 与 $v^{-1} z$ 均与 $z$共轭。在两个相应 flat torus 上计算长度，得到
$$\tau(a)=-\frac{\ell(a)^{2}}{2 \ell(z)}<0, \quad \tau(v)=\frac{\ell(v)^{2}}{2 \ell(z)}>0,$$
矛盾。两个欧氏平面可以不同，关键是它们使用同一个 $\tau$ 。
更一般的循环单值族 $E_{\phi}$ 中，
$$E_{\phi} \text { 有 } \sec \leq 0 \text { 度量 } \Longleftrightarrow[\phi] \text { 有限阶. }$$
无限阶方向由 surface－by－surface CAT（0）群的单值单射定理；有限阶方向由 Nielsen realization 选不变双曲纤维度量，其与基底双曲度量的乘积下降为 Ric $=-g$ 的度量。${ }^{12}$ 无非正截面曲率、无复结构和非虚 Kähler，均未构成一般负 Einstein 不存在性定理。

\section*{6．9．3 从显式逼近确定的全局变分量}

本小节使用构造部分已经逐块验证的输入
$$\operatorname{Vol}\left(E_{D}, G_{j}\right)=V_{0}, \quad \delta_{j}=\left\|\operatorname{Ric}_{G_{j}}+G_{j}\right\|_{\mathrm{op}, \infty, G_{j}} \rightarrow 0, \quad s_{G_{j}} \rightarrow-4 \text { 一致. }$$
固定 $d$ 重连通覆盖 $\widehat{E} \rightarrow E_{D}$ ，记 $V_{*}=d V_{0}$ 。提升序列保留同样的最大误差，体积为 $V_{*}$ 。结合两个取向上的典范 monopole 类、标量曲率估计及其等号刚性，有
$$\begin{aligned}
Y(\widehat{E}) & =-4 \sqrt{V_{*}}=-8 \pi \sqrt{d c} \\
\inf _{g} \int_{\widehat{E}}\left|\operatorname{Ric}_{g}\right|_{\mathrm{HS}}^{2} d V_{g} & =4 V_{*}=16 \pi^{2} d c \\
\inf _{s_{g} \geq-4} \operatorname{Vol}(g) & =\inf _{\operatorname{Ric}_{g} \geq-g} \operatorname{Vol}(g)=V_{*} \\
\inf _{\left\|g^{-1} \operatorname{Ric}_{g}\right\|_{\mathrm{op}, \infty} \leq 1} \operatorname{Vol}(g) & =V_{*}
\end{aligned}$$
Yamabe 上确界、Ricci 能量下确界和这三种体积下确界均不取到：相应等号会给出Kähler 度量，与（6．48）矛盾。经典曲率估计、monopole 定义与等号情形见 LeBrun。 ${ }^{13}$

\footnotetext{
${ }^{11}$ https：／／www．math．ucdavis．edu／～kapovich／EPR／KL＿1996．pdf，Kapovich－Leeb，Actions of discrete groups on nonpositively curved spaces，Theorems 2．3、4．5。Theorem 4.5 的证明正是循环 Dehn twist 曲面丛。
${ }^{12}$ https：／／arxiv．org／pdf／2001．03694，Llosa Isenrich－Py，Theorem 3。有限阶的 realization 见 https： ／／annals．math．princeton．edu／1983／117－2／p02，Kerckhoff 的原定理。
${ }^{13}$ https：／／arxiv．org／pdf／math／0611450，LeBrun，Four－Manifolds，Curvature Bounds，and Convex Geom－ etry，Proposition 3．2、Theorems A、5．3、Definition 5．6。这里的不变量计算是这些经典估计与（6．51）的组合推导。
}

各等式的两侧来源应保留。Yamabe 下界由 $Y\left(\left[G_{j}\right]\right) \geq \min s_{G_{j}} \operatorname{Vol}\left(G_{j}\right)^{1 / 2}$ ；上界对任意共形类的负常标量曲率 Yamabe 代表使用 $\int s^{2} \geq 32 \pi^{2} a^{2}$ 。Ricci 平方下界来自经典 monopole 估计，上界来自（6．51）。体积下界可以直接由 SW 自旋子最大值原理得到，见下小节；上界取 $\left(1+\delta_{j}\right) G_{j}$ ，它满足 Ric $\geq-g$ ，体积为 $\left(1+\delta_{j}\right)^{2} V_{0} \rightarrow V_{0}$ 。极值不取到只排除极值实现者，不能把所有 Einstein 临界点都当作极值实现者。

完整曲率能量的达到性尤其不同。采用 $|\mathrm{Rm}|^{2}=R_{i j k l} R^{i j k l}$ 的完整张量范数， Gauss－Bonnet 直接等价于
$$\int|\operatorname{Rm}|^{2}=32 \pi^{2} \chi(\widehat{E})+4 \int\left|\operatorname{Ric}-\frac{s}{4} g\right|^{2} .$$
逼近序列给三个精确下确界
$$\inf _{g} \int s_{g}^{2}=16 V_{*}, \quad \inf _{g} \int\left|\operatorname{Ric}_{g}\right|^{2}=4 V_{*}, \quad \inf _{g} \int\left|\operatorname{Rm}_{g}\right|^{2}=8 V_{*} .$$
前两者的等号会达到 monopole 标量估计的等号，故不取到；第三者则满足严格等价
$$\exists g: \int\left|\mathrm{Rm}_{g}\right|^{2}=8 V_{*} \quad \Longleftrightarrow \quad \widehat{E} \text { 承载 Einstein 度量. }$$
由（6．55），取等当且仅当无迹 Ricci 为零；收缩 Bianchi 恒等式再迫使比例系数为常数。因此第三种下确界的达到性仍未知。不能将前两种泛函的不取到性传递给第三种。 ${ }^{14}$

全部 monopole 类与共同极化已经同时饱和。 对某一取向的全部 monopole 类集 $\mathcal{C}$ ，定义
$$\beta^{2}=\max _{a \in \operatorname{Hull} \mathcal{C}} a^{2}, \quad \alpha^{2}=\inf _{H \in \operatorname{Gr}_{b_{+}}^{+}} \max _{a \in \mathcal{C}}\left(a_{H}^{+}\right)^{2}$$
典范类给 $2 d c \leq \beta^{2} \leq \alpha^{2}$ ，提升逼近序列与标量估计给相反上界。故在每个有限覆盖和两个取向上都有
$$\alpha_{+}^{2}=\beta_{+}^{2}=\alpha_{-}^{2}=\beta_{-}^{2}=2 d c .$$
不需先列出所有基本类，也不假设覆盖中新类都由原流形拉回。
保留两个取向必须共享同一Hodge 极化的约束后，结论仍成立。对原取向交形式$Q$ 的极大正子空间 $H$ ，记
$$P_{+}(H)=\max _{a \in \mathcal{C}_{+}} Q\left(\pi_{H} a, \pi_{H} a\right), \quad P_{-}(H)=\max _{b \in \mathcal{C}_{-}}\left[-Q\left(\pi_{H^{\perp}} b, \pi_{H^{\perp}} b\right)\right] .$$
每个 $H$ 都有 $P_{ \pm}(H) \geq 2 d c$ ，而同一个提升序列满足
$$2 c \leq \frac{1}{d} P_{ \pm}\left(H_{\pi^{*} G_{j}}^{+}\right) \leq 2 c\left(1+\delta_{j}\right)^{2} .$$
特别地，对任意 $r, s \geq 0$ ，
$$\begin{aligned}
\inf _{g}\left\{r P_{+}\left(H_{g}^{+}\right)+s P_{-}\left(H_{g}^{+}\right)\right\} & =2 d c(r+s) \\
\inf _{g} \max \left\{r P_{+}\left(H_{g}^{+}\right), s P_{-}\left(H_{g}^{+}\right)\right\} & =2 d c \max \{r, s\} .
\end{aligned}$$

\footnotetext{
${ }^{14}$ https：／／arxiv．org／pdf／math／0003068，LeBrun，Ricci Curvature，Minimal Volumes，and Seiberg－Witten Theory，引言、§4 提供曲率泛函与规范理论的经典背景。
}

误差界甚至同时独立于覆盖度数。因此收集更多 monopole 类、有限覆盖、非负加权或共同极化的上述数值组合，不能制造遗漏的严格间隙。这不排除完整 SW 方程或实际Einstein 极化的更精细信息。

标准熵与曲率积分障碍为何仍有余量。 若 $\lambda(E)^{4}=\inf _{g} h(g)^{4} \operatorname{Vol}(g)$ 为最小体积熵，则 Bishop 比较与（6．51）给
$$\lambda\left(E_{D}\right)^{4} \leq 36 \pi^{2} c .$$
经典 Einstein 必要条件 $c \geq \frac{3}{2}|\tau|+\lambda\left(E_{D}\right)^{4} /\left(108 \pi^{2}\right)$ 的右侧至多为 $c / 3$ 。同样，$\frac{2}{3}\left\|E_{D}\right\| \leq \lambda\left(E_{D}\right)^{4}$ 使对应单纯体积障碍仍有这个量级的余量。若 $f: E_{D} \rightarrow X$ 映向闭实双曲四流形，则映射度熵估计给
$$|\operatorname{deg} f| \chi(X) \leq c / 3 .$$
例如 $p=q=2$ 时 $c=4$ ，实双曲四流形的正偶数 Euler 示性数使所有这种映射的度数为零。 ${ }^{15}$ 若 $p \geq 3$ ，将包含扭转曲线的一孔环面压成一点，还得到度一映射$E_{D} \rightarrow \Sigma_{p-1} \times \Sigma_{q}$ 。乘积目标的熵刚性只给 $\operatorname{Vol}(g) \geq \frac{4}{9} \frac{p-2}{p-1} V_{0}$（在 Ric $\geq-g$ 下），弱于（6．54）。 ${ }^{16}$

更完整的数值检查可写成如下形式。假想 $\operatorname{Ric}_{g}=-g 、 \operatorname{Vol}(g)=x V_{*}, 1<x<3$时，
$$\int\left|W^{+}\right|^{2}=\int\left|W^{-}\right|^{2}=V_{*}(1-x / 3), \quad \int s^{2}=16 x V_{*}$$
LeBrun 混合估计的左侧在固定这些积分后，其代数上界为
$$V_{*} B(x), \quad B(x)=(4 \sqrt{x}+\sqrt{6-2 x})^{2}>36 .$$
由（6．59）可选共同极化使两组 monopole 标量与混合估计同时有严格余量。这是数值松弛的可行性，并非构造一个具有这些数据的 Einstein 度量；它说明单靠这组积分数值不能排空 $1<x<3$ 。

非零签名与固定乘积体积不能同时保留。对一般闭四流形 $E$ ，明确假设两取向均有辛结构、 $b_{2}^{ \pm}>1$ ，且 $\chi(E)>0$ 。选择平方较大的典范 monopole 类，其平方为 $2 \chi+3|\tau|$ 。若 $\delta=\left\|\operatorname{Ric}_{g}+g\right\|_{\mathrm{op}, \infty, g}<1$ ，则 $\left|s_{g}\right| \leq 4(1+\delta)$ ，从经典标量估计得
$$\operatorname{Vol}(E, g) \geq \frac{4 \pi^{2} \chi(E)+6 \pi^{2}|\tau(E)|}{(1+\delta)^{2}} .$$
如果另坚持 $\operatorname{Vol}(E, g)=4 \pi^{2} \chi(E)$ ，便有
$$\delta \geq \sqrt{1+\frac{3|\tau(E)|}{2 \chi(E)}}-1 .$$
此式约束任意度量，但保留指定体积与 monopole 前提；它不是仅由拓扑签名给出的任意体积 Ricci 误差间隙。

\footnotetext{
${ }^{15}$ https：／／arxiv．org／pdf／math／0410215，Kotschick，Entropies，Volumes，and Einstein Metrics，Theorem
1、Corollary 2、 §2 的体积熵与映射度估计。
${ }^{16}$ https：／／arxiv．org／pdf／1406．4428，Merlin，Theorem 1、Corollary 12。
}

\section*{6．9．4 SW 缺陷分解：近极小体积究竟控制什么}

这一部分适用于任意闭定向四流形 $M$ ，只要求一个实际 monopole 类 $a$ 满足 $a^{2}>$ 0 。设 $V_{a}=2 \pi^{2} a^{2}$ ，使用规范
$$\begin{gathered}
D_{A} \Phi=0, \quad-i F_{A}^{+}=\sigma(\Phi), \quad|\sigma(\Phi)|^{2}=|\Phi|^{4} / 8 \\
t=|\Phi|^{2}, \quad \mathcal{G}=\int\left|\nabla_{A} \Phi\right|^{2}, \quad \mathcal{B}=\int\left|F_{A}^{-}\right|^{2}
\end{gathered}$$
SW 的积分 Weitzenböck 公式与 Chern－Weil 等式为
$$4 \mathcal{G}+\int s t+\int t^{2}=0, \quad \int t^{2}=16 V_{a}+8 \mathcal{B}$$
所有未注明的积分均按当前度量的体积形式。将 $s=s_{+}-s_{-}$代人并展开平方，得到精确恒等式
$$\int s_{-}^{2}-16 V_{a}=8 \mathcal{G}+8 \mathcal{B}+\int\left(t-s_{-}\right)^{2}+2 \int s_{+} t$$
右侧全部非负；这是经典方程的误差项重排，不另作普遍新定理宣称。
若 $s \geq-4$ ，令 $e=\operatorname{Vol}(g)-V_{a} 、 \xi=s+4 \geq 0$ ，则另一种等价且有用的重排是
$$16 e=8 \mathcal{G}+8 \mathcal{B}+\int(4-t)^{2}+2 \int \xi t$$
这里各项之间均为加号。最大值原理给 $0 \leq t \leq 4$ ；（6．63）立即给 $e \geq 0$ 。取等时自旋子平行且非零，从而产生 Kähler 结构。

为了不丢失误差分布，定义
$$\mathcal{H}(z)=16-(4-z)_{+}^{2}= \begin{cases}8 z-z^{2}, & 0 \leq z \leq 4 \\ 16, & z \geq 4\end{cases}$$
则（6．64）精确等价于
$$16 e=\int \mathcal{H}(\xi)+8 \mathcal{G}+8 \mathcal{B}+\int\left(t-s_{-}\right)^{2}+2 \int s_{+} t .$$
所以 $\operatorname{Vol}\{s \geq 0\} \leq e$ 。若进一步 $\operatorname{Ric} \geq-g$ ，记 $q_{g}=\|\operatorname{Ric}+g\|_{\mathrm{op}, g}$ ；半正定性给 $0 \leq q_{g} \leq \xi$ ，故
$$\int \mathcal{H}\left(q_{g}\right)=\int_{0}^{4}(8-2 z) \operatorname{Vol}\left\{q_{g}>z\right\} d z \leq 16 e, \quad \operatorname{Vol}\left\{q_{g} \geq \eta\right\} \leq \frac{16 e}{\mathcal{H}(\eta)}$$
这是一项有界截断分布预算，不是 $L^{\infty}$ 估计，也不是由凸 Young 函数定义的 Orlicz 范数估计。

若另有 $q_{g} \leq K$ ，则对所有 $r \geq 1$
$$\int q_{g}^{r} \leq \frac{16 K^{r}}{\mathcal{H}(K)} e \quad(K>0) .$$

若还假设统一的连续模与局部体积下界
$$\left|q_{g}(x)-q_{g}(y)\right| \leq L d_{g}(x, y)^{\alpha}, \quad \operatorname{Vol} B_{g}(x, r) \geq v r^{4} \quad\left(0<r \leq r_{0}\right), \quad 0<\alpha \leq 1,$$
最大点周围 $q_{g} \geq \frac{1}{2} \max q_{g}$ 的球与（6．67）给出，充分小的 $e$ 下，
$$\left\|q_{g}\right\|_{\infty} \leq\left(\frac{16(2 L)^{4 / \alpha}}{3 v} e\right)^{\alpha /(4+\alpha)}$$
这是明确附加条件下的充分估计；原始 Ricci 夹逼并未提供这些条件。

不额外假设直径的注入半径退化。 若固定 $M$ 具有上述实际类且 $b_{1}(M)$ 奇，
$$\operatorname{Ric}_{g_{j}} \geq-g_{j}, \quad\left\|\operatorname{Ric}_{g_{j}}+g_{j}\right\|_{\mathrm{op}, \infty} \leq K, \quad \operatorname{Vol}\left(g_{j}\right) \rightarrow V_{a},$$
则
$$\min _{M} \operatorname{inj}_{g_{j}} \longrightarrow 0 .$$
否则双侧 Ricci 界与全局注入半径下界给统一调和坐标和小球体积下界。在最短测地线上打包不交小球，利用总体积上界得到直径上界。调和坐标紧致性再给同一闭流形上的 $C^{1, \alpha}$ 子列；（6．68）使 Ricci 误差在有限 $L^{r}$ 中消失。调和坐标下的弱 Ricci 方程与粗圆正则性产生光滑 $\operatorname{Ric}_{g_{\infty}}=-g_{\infty}$ 、体积 $V_{a}$ 的极限，与等号给 Kähler、 $b_{1}$ 奇相矛盾。${ }^{17}$ 该结论不给维数统一的体积间隙，且不把输入序列宣称为 $C^{\infty}$ 收玫。

\section*{6．9．5 任何假想 Einstein 度量必须满足的全局条件}

在 $E_{D}$ 或其 $d$ 重有限覆盖上，正或零 Einstein 常数被正平方实际 monopole 类排除。负常数可以统一归一化为 $\mathrm{Ric}_{g}=-g$ 。设 $V_{*}=d V_{0}$ ，则任何这样的度量都必须满足
$$V_{*}<\operatorname{Vol}(g)<3 V_{*} .$$
左端来自（6．54）的不取到性。右端由 Einstein Gauss－Bonnet
$$8 \pi^{2} d c=\int\left(\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}\right)+\frac{2}{3} \operatorname{Vol}(g)$$
给出；等号意味着 Weyl 为零，即常截面曲率 $-1 / 3$ 。但 $G$ 含 $\mathbb{Z}^{2}$ ，其每个有限指数子群亦然，与闭负实空间形式的群性质矛盾。Weyl 范数在这里统一取其作用于 $\Lambda^{ \pm}$的Hilbert－Schmidt 范数。

由经典非 Hadamard 障碍，这个假想度量还必须有正截面曲率平面。这与负 Ricci并不矛盾。更强的、覆盖全部体积区间的谱约束是
$$W^{+} \text {与 } W^{-} \text {在一个共同开稠密集上各有三个互异特征值。 }$$

\footnotetext{
${ }^{17}$ https：／／doi．org／10．1007／BF01233434，Anderson，Convergence and rigidity of manifolds under Ricci curvature bounds 。
}

证明先用签名为零排除一半 Weyl 恒零，否则两半均零，又落入上段的实双曲矛盾。若一半 Weyl 处处至多有两个特征值，Derdziński 的 Proposition 5（iv）保证它处处非零，且 Proposition 5（i）的共形度量
$$\bar{g}=\left(24\left|W^{ \pm}\right|^{2}\right)^{1 / 3} g$$
局部 Kähler。简单特征线的定向覆盖至多二重，局部 Kähler 形式仅差正负号，因而在该覆盖上拼成全局 Kähler 结构，违反（6．48）。 ${ }^{18}$ 最后，对无迹自伴三阶算子设
$$\mathfrak{D}(A)=\frac{1}{2}\left(\operatorname{tr} A^{2}\right)^{3}-3\left(\operatorname{tr} A^{3}\right)^{2}=\prod_{i<j}\left(\lambda_{i}-\lambda_{j}\right)^{2}$$
Einstein 度量的实解析性使 $\mathfrak{D}\left(W^{ \pm}\right)$解析且不恒零，故其零集无内点，证明（6．72）。 ${ }^{19}$因此假想度量也不能在任何非空开集上局部共形 Kähler。该结论允许一般三特征值Einstein 几何，未排除所有度量。

连通精确 Einstein 路径的体积恒定。 若 $g(a)$ 是固定闭四流形上、在整个连通参数区间定义的 $C^{1}$ 精确路径， $\operatorname{Ric}_{g(a)}=-g(a)$ ，令 $h=\partial_{a} g 、 V=\operatorname{Vol}(g)$ 。总标量曲率第一变分给
$$-4 V^{\prime}=\frac{d}{d a} \int s d V=\int\left(-\langle\text { Ric }, h\rangle+\frac{s}{2} \operatorname{tr} h\right) d V=-\int \operatorname{tr} h d V=-2 V^{\prime}$$
故 $V^{\prime}=0$ 。因此，若某近似度量族 $G_{\varepsilon}$ 的体积趋于 $V_{0}$ ，不可能在整个区间 $0<\varepsilon<\varepsilon_{0}$找到 $C^{1}$ 的 $\operatorname{Ric}_{\widehat{G}_{\varepsilon}}=-\widehat{G}_{\varepsilon}$ 路径，且
$$\left\|G_{\varepsilon}^{-1}\left(\widehat{G}_{\varepsilon}-G_{\varepsilon}\right)\right\|_{\mathrm{op}, \infty} \rightarrow 0 .$$
相对 $C^{0}$ 接近使该精确路径体积趋 $V_{0}$ ，恒定性则迫使它等于 $V_{0}$ ，违反（6．71）。该结论不排除位于不同模空间分支的离散 Einstein 序列，也不排除与输入不接近的精确度量。固定非零 Einstein 常数是体积恒定的必要前提。 ${ }^{20}$

固定构造辛形式时的更窄条件。这是一项有额外相容性假设的结果，不能并入任意Einstein 结论。固定构造中的辛形式 $\omega$ ，满足 $\operatorname{Vol}_{\omega}=V_{0} 、 4 \pi c_{1} \cdot[\omega]=-4 V_{0}$ 。若其相容almost－Kähler 度量满足 $\operatorname{Ric}_{g}=-x g$ ，记 $u_{J}=|\nabla J|^{2}$ ，则 Blair 公式给
$$x=1+\frac{1}{16 V_{0}} \int u_{J}>1 .$$
把 $W^{+}$对 $\Lambda^{+}=\mathbb{R}(\omega / \sqrt{2}) \oplus \omega^{\perp}$ 分块，记其在 $\omega^{\perp}$ 压缩后的无迹部分为 $C$ 。在 $\delta W^{+}=0$下，经典积分恒等式保留平方余项后给
$$\int\left(\frac{s^{2}}{24}-\left|W^{+}\right|^{2}\right)=\frac{3}{128} \int u_{J}^{2}+\int|C|^{2} .$$

\footnotetext{
${ }^{18}$ https：／／www．numdam．org／article／CM＿1983＿＿49＿3＿405＿0．pdf，Derdziński，Self－dual Kähler manifolds and Einstein manifolds of dimension four，Proposition 5（i）、（iv）。
${ }^{19}$ https：／／www．numdam．org／article／ASENS＿1981＿4＿14＿3＿249＿0．pdf，DeTurck－Kazdan，Some regularity theorems in Riemannian geometry，Theorem 5．2。
${ }^{20}$ https：／／arxiv．org／pdf／1311．6749，Kröncke，引言、§2 的 Einstein－Hilbert 第一变分背景。上述体积恒定等式是直接计算。
}

由此有
$$V_{0}(x-1)(7-5 x)=\frac{3}{128} \int\left(u_{J}-16(x-1)\right)^{2}+\int|C|^{2}, \quad 1<x<\frac{7}{5} .$$
端点 $x=7 / 5$ 会迫使 $u_{J}$ 为正常数，与闭 almost－Kähler Einstein 四流形必有 $u_{J}=0$ 的点相矛盾。 ${ }^{21}$ 对任意归一化 almost－Kähler Einstein 三元组，不再固定 $\omega$ ，相应等式为
$$\operatorname{Vol}(g)-V_{0}=\frac{3}{128} \int|\nabla J|^{4}+\int|C|^{2} .$$
$x g$ 的体积为 $x^{2} V_{0}$ ，同时相容辛形式变为 $x \omega$ ；不能用缩放删除固定 $\omega$ 的尺度限制。

\section*{6．9．6 体积趋下端时：精确 Einstein 序列的条件退化定理}

本小节假设的是尚未证明存在的精确序列
$$\operatorname{Ric}_{g_{j}}=-g_{j}, \quad \operatorname{Vol}\left(E_{D}, g_{j}\right) \longrightarrow V_{0} .$$
它不能与（6．51）的已有近似序列混同。结论为：选取厚点和子列后，必出现一个完整、非紧、有限体积的局部 $\mathbb{H}^{2}(-1) \times \mathbb{H}^{2}(-1)$ 光滑极限；对当前 $E_{D}$ ，该格点商必须可约。下面给出这条推论链所需的分析与拓扑输入。

从体积缺陷得到局部曲率能量控制。 省略下标，令 $d_{V}=V-V_{0}>0$ 。Gauss－Bonnet与签名公式给
$$\int\left|W^{+}\right|^{2}=\int\left|W^{-}\right|^{2}=V_{0}-\frac{V}{3} .$$
对两取向应用经典混合估计 $\int\left(4+\sqrt{6}\left|W^{ \pm}\right|\right)^{2} \geq 36 V_{0}$ ，展开并整理得到
$$\int\left(\left|W^{ \pm}\right|-\sqrt{\frac{2}{3}}\right)^{2} \leq \frac{3}{2} d_{V}$$
完整 $(0,4)$ 曲率张量范数与此处 Weyl 算子范数的转换为
$$|\operatorname{Rm}|_{(0,4)}^{2}=4\left(\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}\right)+\frac{8}{3} .$$
因此对任意可测集 $U$
$$\int_{U}|\operatorname{Rm}|_{(0,4)}^{2} \leq 24 d_{V}+\frac{40}{3} \operatorname{Vol}(U) .$$
Bishop 比较给每个固定半径球的体积上界。先将半径统一选小，再令 $d_{V}$ 小，（6．77）使所有球同时达到 Cheeger－Tian 四维 Einstein 的小能量阈值。该定理使用未经体积归一化的 $L^{2}$ 曲率积分，不要求球体积或注入半径下界。故存在普适 $d_{*}, K_{*}>0$ ，使
$$0<d_{V} \leq d_{*} \quad \Longrightarrow \quad\left\|\mathrm{Rm}_{g}\right\|_{\infty} \leq K_{*} .$$

\footnotetext{
${ }^{21}$ https：／／arxiv．org／pdf／1408．1078，LeBrun，Equation（3）；https：／／arxiv．org／pdf／math／0409290， Proposition 2.4 中使用的 Armstrong 定理。
}

这里不可把＂精确 Einstein＂替换成＂小 Ricci 误差＂。 ${ }^{22}$
有界曲率的精确 Einstein 度量通过显式 Ricci 流 $g(t)=(1+2 t) g$ 与 Shi 估计还具有统一曲率导数界。若全流形的注入半径均充分小，有界截面曲率塌缩理论会给全局正秩 $F$－结构，从而 $\chi\left(E_{D}\right)=0$ ，矛盾。所以存在统一的厚点 $p_{j}, \operatorname{inj}_{g_{j}}\left(p_{j}\right) \geq i_{*}>0$ 。这一步使用正 Euler 示性数和塌缩拓扑，不是直接从总体积下界猜出厚点。 ${ }^{23}$ 厚点的小球非塌缩经 Bishop－Gromov 比较传播到每个固定距离范围；结合曲率界和导数界，给出完整的带基点光滑极限 $X$ 。

平行方向来自两个 SW 方程，不能由 Weyl 范数猜出。 在每一取向上各取实际类的SW 解。（6．65）在 $s=-4$ 时化为
$$16 d_{V}=8 \mathcal{G}+8 \mathcal{B}+\int(4-t)^{2}$$
令 $\varphi=\sigma(\Phi)$ ，二次映射的微分估计给
$$|\nabla \varphi|^{2} \leq \frac{t}{2}\left|\nabla_{A} \Phi\right|^{2}, \quad|\varphi|=\frac{t}{2 \sqrt{2}} \leq \sqrt{2} .$$
因此
$$\int|\nabla \varphi|^{2} \leq 4 d_{V}, \quad \int(|\varphi|-\sqrt{2})^{2} \leq 2 d_{V}, \quad \int|\varphi|^{2} \geq 2 V_{0} .$$
对两取向的普通二形式在极限紧集上同时取 Rellich 子列，得到全局平行的
$$\varphi_{\infty}^{+} \in \Lambda^{+}, \quad \varphi_{\infty}^{-} \in \Lambda^{-}, \quad\left|\varphi_{\infty}^{ \pm}\right| \equiv \sqrt{2} .$$
无需在变化的流形上识别 spin－c 结构或建立统一规范。二形式定义的正交平行复结构 $J_{+}, J_{-}$彼此交换，$-J_{+} J_{-}$是迹为零的平行对称对合，其正负特征分布均为秩2。deRham 分解与 Ric $=-g$ 遂给
$$X=\Lambda \backslash\left(\mathbb{H}^{2}(-1) \times \mathbb{H}^{2}(-1)\right), \quad \Lambda<\operatorname{PSL}_{2}(\mathbb{R})^{2} \text { 为无挠格点. }$$
两套平行结构保证甲板变换分别保存两个有向分布，所以这里没有未经说明的因子交换。紧集体积极限给 $0<\operatorname{Vol}(X) \leq V_{0}$ 。若 $X$ 紧，光滑收敛最终给整个 $X$ 到 $E_{D}$ 的同维嵌入，其像开且闭，故为微分同胚，与 $E_{D}$ 无复结构矛盾。因此 $X$ 非紧。

同样的 SW 测试形式对任意假想精确 Einstein 度量给出
$$0<\lambda_{0}^{ \pm}\left(\nabla^{*} \nabla\right) \leq \frac{2\left(V-V_{0}\right)}{V_{0}} .$$
这里是 $\Lambda^{ \pm}$上的粗 Laplacian；若其最低特征值为零，会产生非零平行二形式并给 Kähler结构。式（6．82）不涉及本来就有调和零模的 Hodge Laplacian。

\footnotetext{
${ }^{22}$ 原定理：https：／／doi．org／10．1090／S0894－0347－05－00511－4，Cheeger－Tian。完整接口见 https：／／arxiv．org／pdf／1707．05511，Ge－Jiang，Theorem 1．1：四维 Einstein、 $|\lambda| \leq 3 、 r \leq 1 、 \int_{B_{r}}|\operatorname{Rm}|^{2} \leq \varepsilon$ 蕴含半球上的 $C r^{-2}$ 曲率界。
${ }^{23}$ https：／／arxiv．org／pdf／2103．05659，Song，Essential minimal volume of Einstein 4－manifolds，§1．2、Lemma 2 所用的 Cheeger－Gromov 正秩 $F$－结构与 Euler 消失。
}

为使用整数周期，可以将 SW 曲率换为固定上同调类的完整调和代表。按 $\left[i F_{A}\right]=$ $2 \pi a$ 的曲率约定，取 $Q=i F_{A}^{+}$，令 $H=2 \pi a_{g}^{+}$为固定类 $2 \pi a$ 的自对偶调和部分；它也是 $Q$ 的 $L^{2}$ 调和投影。这里 $Q$ 通常不闭，不能谈它自己的同调类。则
$$16 d_{V}=\int(4-t)^{2}+8 \mathcal{G}+8\|Q-H\|_{2}^{2}+32 \pi^{2}\left\|a_{g}^{-}\right\|_{2}^{2}$$
相应 Hodge 投影不需全局谱隙；它给 $\int(|H|-\sqrt{2})^{2} \leq 4 d_{V}$ ，结合曲率界与二形式Weitzenböck 公式给 $\|\nabla H\|_{2}^{2} \leq C d_{V}$ 。完整调和代表 $\alpha_{j}^{ \pm}$满足 $\left[\alpha_{j}^{ \pm}\right]=2 \pi a_{ \pm}$，在光滑极限紧集上经调和椭圆正则性收敛到 $\pm\left(\omega_{1}+\omega_{2}\right)$ 与 $\pm\left(\omega_{1}-\omega_{2}\right)$ 。必须使用完整代表才能读取固定整数周期，不能用随度量改变的自对偶投影替代固定类。

不可约分支的纯拓扑排除。 无挠不可约非一致格点 $\Lambda<\operatorname{PSL}_{2}(\mathbb{R})^{2}$ 到任何闭高亏格曲面群的同态均平凡。确实，Margulis 正规子群定理使非平凡核必为有限指数；另一方面 $\Lambda$ 的尖点么幂群含 $\mathbb{Z}^{2}$ ，所以不可能单射到曲面群。曲面群无挠，有限像只能平凡。依次向 $G \rightarrow \Pi_{q}$ 和核 $\Pi_{p}$ 投影，得
$$\operatorname{Hom}(\Lambda, G)=\{1\} .$$
该论证使用高秩正规子群定理，没有声称 $\operatorname{PSL}_{2}(\mathbb{R})^{2}$ 或其格点具有性质 $(T)$ 。 ${ }^{24}$
不可约非一致商的 Baily－Borel 紧化是仅增添有限个尖点的射影曲面。选避开这些点的一般光滑超平面截面 $C$ ，则 $C \subset X$ 紧且
$$C \cdot C=\left.\operatorname{deg} \mathcal{O}(1)\right|_{C}>0 .$$
所以任意包含 $C$ 及其管状邻域的紧核心 $N$ 都不能嵌入 $E_{D}$ ：若 $i: N \hookrightarrow E_{D}$ ，（6．83）与$E_{D}=K(G, 1)$ 使 $i$ 零伦，故 $i_{*}[C]=0$ ；但同维嵌入保存法丛，自交数为 $\pm C \cdot C \neq 0$ ，矛盾。该论证绕过了＂紧核心是否基本群单射＂的未证假设。 ${ }^{25}$ 光滑收敛恰会给任何固定紧核心的嵌入，故（6．81）不可约分支被排除。

剩余可约极限及其量子化。 可约格点的有限指数积子群给有限 Riemannian 覆盖
$$S_{1} \times S_{2} \longrightarrow X$$
，$S_{i}$ 是完整有限面积定向双曲曲面，至少一个非紧。若覆盖度为 $D_{0} 、 k_{i}=-\chi\left(S_{i}\right)>0$ ，则
$$\operatorname{Vol}(X)=\frac{4 \pi^{2} k_{1} k_{2}}{D_{0}}=4 \pi^{2} \chi(X), \quad 1 \leq \chi(X) \leq c$$
对有限组在原序列中基点距离两两趋无穷的厚部极限，$\sum_{\ell} \chi\left(X_{\ell}\right) \leq c$ 。没有证明抽取出的极限捕获全部体积，也不能重复计数同一分支的不同基点。

\footnotetext{
${ }^{24}$ Margulis 的正规子群与算术性定理见 Discrete Subgroups of Semisimple Lie Groups；可核对陈述：https： ／／arxiv．org／pdf／math／0106063，Theorem 17．1．1。尖点么幂 $\mathbb{Z}^{2}$ 见 https：／／arxiv．org／pdf／0706．3580， McReynolds，§2．1。
${ }^{25}$ https：／／annals．math．princeton．edu／1966／84－3／p11，Baily－Borel，Compactification of arithmetic quotients of bounded symmetric domains。Hilbert modular 曲面的具体紧化见 https：／／arxiv．org／pdf／1108．5 305，Funke－Millson，§2．2．3。
}

\section*{6．9．7 可约核心的整数周期、闭因子单射与可实现模型}

仍以（6．75）为前提。将可约极限有限覆盖的紧核心记为 $N_{1} \times N_{2}$ 。收敛映射与有限覆盖复合，给到 $E_{D}$ 的光滑局部嵌入 $f_{j}$ ；它未必整体单射。完整整数类 $a_{ \pm}$的周期收敛给
$$f_{j}^{*} a_{ \pm}=0 \quad \text { 于 } H^{2}\left(N_{1} \times N_{2} ; \mathbb{Z}\right)$$
，当两个因子均非紧；因为交叉环面上的极限周期为零，而整数序列收敛到零后最终为零。若 $S_{1}=\Sigma_{r}$ 闭，则在闭切片 $C=\Sigma_{r} \times\{z\}$ 上
$$\left|\left\langle a_{+}, f_{j *}[C]\right\rangle\right|=\left|\left\langle a_{-}, f_{j *}[C]\right\rangle\right|=2 r-2 \quad(j \text { 充分大 }) .$$
Künneth 分解给整个核心的类限制：闭因子情形 $f_{j}^{*} a_{ \pm}$是 $\pm \operatorname{pr}_{1}^{*}\left[-e\left(T \Sigma_{r}\right)\right]$ ，两个符号可分别选择；非紧核心无 $H^{2}$ ，交叉环面周期最终为零。

令 $m=2 r-2, v=\left\langle e_{V}, f_{j *}[C]\right\rangle, b=\left\langle e_{B}, f_{j *}[C]\right\rangle$ 。由（6．46）与（6．85），
$$|v+b|=|v-b|=m \quad \Longrightarrow \quad(v, b) \in\{( \pm m, 0),(0, \pm m)\} .$$
恰有一个 Euler 类达到闭曲面圆周作用的最大值。
基底 Euler 类来自 $\Pi_{q}$ 在 $\partial \mathbb{H}^{2}$ 上的标准作用。垂直 Euler 类也来自实际的圆周作用：对正规纤维群共轭，再作用于其 Gromov 边界，
$$G \longrightarrow \operatorname{Aut}^{+}\left(\Pi_{p}\right) \longrightarrow \operatorname{Homeo}^{+}\left(S^{1}\right), \quad e\left(\rho_{V}\right)=e_{V} .$$
这一 Euler 类识别可由带对角截面的拉回曲面丛核验：在每个纤维将截面点吹起为切方向圆，并加上普适覆盖的无穷远圆，得到环带丛；内外边界分别为 $S(V)$ 与 Nielsen边界圆丛，所以 Euler 类相同。使用的是有向单位切向量圆，没有遗漏射影化的因子2。 ${ }^{26}$

最大 Euler 数圆周作用半共轭于忠实 Fuchsian 作用；半共轭的满射性使原作用本身忠实。故（6．86）的任一分支都迫使
$$\left(\left.f_{j}\right|_{C}\right)_{*}: \pi_{1}\left(\Sigma_{r}\right) \longrightarrow \pi_{1}\left(E_{D}\right) \text { 单射. }$$
这里没有推出非紧因子或整个核心的基本群单射。 ${ }^{27}$
闭因子亏格还满足两种可检查的整除：
$$\left\{\begin{array}{ll}
r-1=d(q-1), & \text { 基底最大 Euler 分支, } \\
r-1=d(p-1), & \text { 垂直最大 Euler 分支, }
\end{array} \quad d \in \mathbb{N}\right. \text {. }$$
第一行的闭曲面群单射进入 $\Pi_{q}$ ，其像必须有限指数；无限指数覆盖曲面的基本群为自由群，不能为闭曲面群。

\footnotetext{
${ }^{26}$ https：／／arxiv．org／pdf／0905．2360，Bestvina－Church－Souto，§3 的环带紧化；https：／／arxiv．org／pdf／1105．4444，Bowden，§3 的垂直 Euler 类。
${ }^{27}$ 最大 Euler 数刚性为 Matsumoto 的经典定理；其准确陈述和推广见 https：／／arxiv．org／pdf／2207．08411， Adachi－Matsuda－Nozawa，Corollary 1．2、Theorem 1．3。
}

第二行不需要先证明像落在原纤维群。利用 $P: E_{D} \rightarrow T_{D}$ 和映射环面的 Wang 序列：
$$0 \rightarrow \mathbb{Z}[F] \rightarrow H_{2}\left(T_{D} ; \mathbb{Z}\right) \rightarrow \operatorname{ker}\left(D_{*}-I: H_{1}(F ; \mathbb{Z}) \rightarrow H_{1}(F ; \mathbb{Z})\right) \rightarrow 0 .$$
不变量核由 twist 支集外的曲线类生成；这些曲线与映射环面方向的乘积环面上，垂直切丛有非零截面，Euler 评价为零；在纤维上的评价为 $2-2 p$ 。因此
$$\left\langle e_{V}, z\right\rangle \in(2-2 p) \mathbb{Z} \quad \text { 对所有 } z \in H_{2}\left(E_{D} ; \mathbb{Z}\right) \text {, }$$
结合 $|v|=2 r-2$ 得第二行。若另一个开因子的 $-\chi=k$ ，积覆盖度为 $D_{0}$ ，体积约束进一步给 $d k \leq 2 D_{0}(p-1)$（基底分支），或 $d k \leq 2 D_{0}(q-1)$（垂直分支）。垂直分支中的$d$ 只是 Euler 评价确定的整数，未经额外论证不能称为原纤维群中的指数。

若该闭切片本身在 $E_{D}$ 中嵌入，其法丛由另一因子平凡化，自交为零；（6．85）使两取向 adjunction 不等式取等，所以它在所代表的非挠同调类中亏格最小。有限覆盖后仅局部嵌入的切片不能直接套用嵌入版 adjunction。 ${ }^{28}$

这些必要条件与候选拓扑确实相容。 令 $P_{B}=B \backslash \nu(\gamma) \cong \Sigma_{q-1,2}, P_{F}=F \backslash \nu(\alpha) \cong$ $\Sigma_{p-1,2}$ ，其中删去包含 twist 支集的开环带。分别有基本群单射的实际嵌入
$$F \times P_{B} \hookrightarrow E_{D}, \quad P_{F} \times B \hookrightarrow E_{D} .$$
第一个利用 $\left.u\right|_{\pi_{1} P_{B}}=0$ ，第二个利用 $\left.D\right|_{P_{F}}=\mathrm{id}$ 。两个核心分别实现垂直、基底最大Euler 分支，且各自 $\chi=c$ ，其补集 Euler 示性数为零。它们彼此重叠，不能将 Euler数或体积相加。此外
$$C_{G}\left(\Pi_{p}\right)=\{(1, b): u(b)=0\} \cong \operatorname{ker} u,$$
该中心化子含大的自由子群；所以＂闭曲面群不能与非阿贝尔自由群交换＂在这里是错误推法。

已有近似度量还实现这些可约模型。仅捏缩基底 $\gamma$ ，固定其余 Fenchel－Nielsen 参数与纤维双曲度量，在宽度 $L_{\ell}=\frac{1}{2} w(\ell)$ 的中央领圈慢插值：
$$w(\ell)=\operatorname{arsinh}(1 / \sinh (\ell / 2)) .$$
中央区域体积为 $8 \pi(p-1) \ell \sinh L_{\ell}=O(\sqrt{\ell})$ ，固定极限紧集上最终为精确乘积，故
$$\left(E_{D}, G_{\ell}, p_{\ell}\right) \longrightarrow\left(F, h_{0}\right) \times S_{q-1,2}, \quad \operatorname{Vol}\left(F \times S_{q-1,2}\right)=V_{0} .$$
若同时只捏缩纤维与基底中指定的非分离曲线，其余模参数固定，双领圈构造还给$S_{p-1,2} \times S_{q-1,2}$ 的全体积极限。这些是 $\|$ Ric $+g \|_{\infty} \rightarrow 0$ 的实际序列，不是精确 Ein－ stein 序列。 ${ }^{29}$

\footnotetext{
${ }^{28}$ https：／／arxiv．org／pdf／math／0005268，Ozsváth－Szabó，Higher Type Adjunction Inequalities in Seiberg－Witten Theory，Theorem 1.3 的基本情形。
${ }^{29}$ https：／／arxiv．org／pdf／1605．06691，Rupflin－Topping，Lemma A．1、Theorem A．4：双曲领圈与单曲线退化。
}

两个开曲面的面积形式在普通 de Rham 上同调中正合，其乘积不含紧复曲线；不可约分支使用的正自交曲线机制在此确实不适用。尽管平行面积形式正合，其原函数仍不能有界：若 $d \eta=\omega_{S}$ ，在面积趋向正总面积的尖点截断核心上，Stokes 给
$$\sup _{\partial S_{T}}|\eta| \geq \frac{\operatorname{Area}\left(S_{T}\right)}{\operatorname{Length}\left(\partial S_{T}\right)} \asymp e^{T} .$$
这说明普通上同调为零不等于存在可供全局估计的有界原函数。

条件退化定理的准确边界。（6．75）推出有界曲率、厚点、可约有限体积积商、整数周期及闭因子单射等必要条件。它未证明精确序列存在，未保证极限捕获全部体积，未证明核心整体基本群单射，也未控制两套近乎平行形式在原流形全部薄部处处非零。Einstein Dehn 填充中的外围元素可以被杀掉，所以不能把＂极限核心嵌入＂自动升级为基本群单射。 ${ }^{30}$ 即使日后排除了体积趋 $V_{0}$ 的精确序列，也只得到依赖流形的正体积间隙；（6．71）中更大体积的 Einstein 度量仍需另外处理。

\footnotetext{
${ }^{30}$ https：／／arxiv．org／pdf／math／0303260，Anderson，Dehn filling and Einstein metrics in higher dimensions。这只是对无条件核心单射推法的反证先例，并不是当前固定 $E_{D}$ 上精确 Einstein 序列的构造。
}

\section*{第七章 Weyl 特征线、谐和压缩与不能删除的源项}

本章讨论的是四维曲率方程本身。核心区分有三个：最大的简单特征值与最小的简单特征值；精确调和 Weyl 与散度很小；固定光滑背景上的有限维核与退化族上的统一可逆性。以下局部恒等式和有限维推导保留全部几何假设，不附带文献首创性声明。

\section*{7.1 最大特征值刚性恰在乘积模型处退化}

令 $\alpha \geq \beta \geq \gamma$ 为一个半 Weyl 算子的特征值。Catino－Dameno 的预印本证明：闭Einstein 四流形若 $W^{+} \not \equiv 0$ 且存在同一个 $\rho_{0}<1$ 使 $\beta \leq \rho_{0} \alpha$ ，则在至多二重覆盖上共形 Kähler，原 Einstein 度量具有正标量曲率。因此其非正标量推论为
$$s \leq 0, \quad W^{+} \not \equiv 0 \quad \Longrightarrow \quad \sup _{\left\{W^{+} \neq 0\right\}} \frac{\beta}{\alpha}=1 .$$
这里采用论文所查版本的结论，不能把预印本的存在误写成已经完成独立同行复核。 ${ }^{1}$
对两个曲率为 -1 的曲面积，两个半 Weyl 的谱都是
$$(-2 / 3,1 / 3,1 / 3) .$$
最大根重合，最小根简单。这已经否定了从 Ric $+g$ 很小推出最大根一致简单的普遍命题，因为此处 Ricci 缺陷严格为零。对本稿的 Dehn twist 曲面丛，$\tau=0$ 与 $\mathbb{Z}^{2} \subset \pi_{1}$ 又保证任意假想负 Einstein 度量的两半 Weyl 都不恒零：一半为零会由签名公式迫使另一半为零，继而得到与 Preissmann 定理矛盾的负常曲率。因此（7．1）适用于两种取向。

等价的不变量条件为
$$\inf _{\left\{W^{ \pm} \neq 0\right\}} \frac{\operatorname{det} W^{ \pm}}{\left|W^{ \pm}\right|^{3}}=-\frac{1}{3 \sqrt{6}} .$$
上确界可能沿 Weyl 零点取得极限；没有证明存在非零的重根点。两种取向的相关点也不必相同。

\section*{7.2 负最小特征线的精确平衡}

设 $(M, h)$ 闭、定向，$\delta_{h} W_{h}^{+}=0$ ，最小特征值 $\lambda_{h}<\mu_{h} \leq \nu_{h}$ 处处简单。在必要的特征线定向二重覆盖上，定义
$$g=\left(-\lambda_{h}\right)^{2 / 3} h, \quad f=-\left(-\lambda_{h}\right)^{-1 / 3}, \quad A=f W_{g}^{+}, \quad A \omega=\omega, \quad|\omega|_{g}^{2}=2 .$$
下文 $\lambda, \mu, \nu$ 指 $g$ 下特征值；$f \lambda=1$ ，并记
$$\rho=\mu / \lambda \in[-1 / 2,1), \quad \eta=\rho+1 / 2 \in[0,3 / 2) .$$

\footnotetext{
${ }^{1}$ G．Catino，D．Dameno，Conformal Kähler Rigidity of Einstein Four－Manifolds，arXiv：2607．21538v1，Theo－ rem 1．4、Corollary 1．7，https：／／arxiv．org／html／2607．21538v1。
}

对正权 $-f$ 使用共形协变公式后整体乘负号，合法得到
$$\delta_{g} A=0, \quad \nabla^{*} \nabla A+\frac{s_{g}}{2} A-\frac{6}{f} A^{2}+\frac{2}{f}|A|^{2} I=0 .$$
这没有把 $-W$ 当成另一取向的 Weyl 张量。
命题7．1（负分支的平衡与闭合缺陷）。在上述条件下，令 $N=|\nabla \omega|^{2} 、 D=|d \omega|^{2}$ ，则
$$\begin{aligned}
D & =R(\eta) N, & R(\eta) & =\frac{4 \eta^{2}}{9+4 \eta^{2}} \\
\int_{M} Q(\eta) N d V_{g} & =8 \int_{M}|\lambda| \eta^{2} d V_{g}, & Q(\eta) & =\frac{3\left(9-4 \eta^{2}\right)}{2\left(9+4 \eta^{2}\right)}
\end{aligned}$$
积分在上述闭覆盖上进行。两个较大特征值重合时，各式按连续性仍成立。
证明．在局部长度为 $\sqrt{2}$ 的特征标架中写 $\nabla \omega=a \otimes \omega_{2}-c \otimes \omega_{3}$ 。由 $\delta A=0$ ，令 $k=(1-\rho) /(2+\rho)$ ，得到
$$D=(1-k)^{2}|a|^{2}, \quad N=2\left(1+k^{2}\right)|a|^{2}, \quad T:=W^{+}(\nabla \omega, \nabla \omega)=2 \lambda\left\{\rho-(1+\rho) k^{2}\right\}|a|^{2} .$$
这些一阶关系可由特征方程微分与散度缩并直接重建；本章后面的带源计算也给出其无源版本。将（7．3）与 $\omega \otimes \omega$ 收缩，使用 $A \omega=\omega$ ，得
$$0=2 N-\frac{2}{\lambda} T+s_{g}-12 \lambda+\frac{4}{\lambda}\left|W^{+}\right|^{2} .$$
二形式 Weitzenböck 公式给 $\left\langle\omega, \Delta_{d} \omega\right\rangle=N-4 \lambda+2 s_{g} / 3$ 。消去 $s_{g}$ 并积分，利用自对偶性 $\int\left\langle\omega, \Delta_{d} \omega\right\rangle=2 \int D$ ，可得
$$0=\int_{M}\left(3 D+\frac{1}{2} N-\frac{2}{\lambda} T+8 \lambda \eta^{2}\right) d V_{g}$$
代入局部关系，前三项恰为 $Q N$ ，而 $\lambda<0$ ，遂得结论。 \(\square\)

负分支给出两个非负量相等，未迫使任一消失。若再有 $0 \leq \eta \leq \varepsilon<3 / 2 、|\lambda| \leq \Lambda$ ，则
$$\frac{1}{\operatorname{Vol}_{g}(M)} \int_{M}|d \omega|^{2} d V_{g} \leq \frac{64 \Lambda \varepsilon^{4}}{3\left(9-4 \varepsilon^{2}\right)}$$
这里四阶指范数的平方。参数 $\varepsilon$ 衡量 Weyl 上部谱分裂，不能与 Ricci 误差混同。
命题7．2（严格闭性条件下的局部刚性）。上述规范可只在开集上定义。若在该开集上$d \omega \equiv 0$ ，则 $\eta=0$ 且 $\nabla^{g} \omega=0$ ，所以 $g$ 局部 Kähler，$s_{g}=6 \lambda<0$ 。

证明．自对偶性给 $\Delta_{d} \omega=0$ 。前一证明的点态式变为 $0=Q N+8 \lambda \eta^{2}$ ，同时 $D=R N=0$ 。在 $\eta>0$ 处，$R>0$ 强迫 $N=0$ ，与 $\lambda \eta^{2}<0$ 矛盾；故 $\eta=0$ ，再由 $Q=3 / 2$ 得 $N=0$ 。 \(\square\)

若只在 $U=M \backslash S$ 上有简单性，则闭流形积分不能直接照搬。一个充分的截断条件是 $Q N,|\lambda| \eta^{2} \in L^{1}(U, g)$ ，并有 $0 \leq \chi_{j} \leq 1 、 \chi_{j} \rightarrow 1 、 \operatorname{supp} \chi_{j} \Subset U$ 满足
$$\int_{U} Q^{-1}\left|d \chi_{j}\right|_{g}^{2} d V_{g} \longrightarrow 0$$
这是含逆谱隙权重的容量条件。仅知道 $S$ 有小 Hausdorff 维数，不足以控制该加权积分。

\section*{7.3 谐和核不能由近乎闭性删除}

在固定闭负 Kähler－Einstein 曲面积 $\left(M, g_{0}\right)$ 上，取一个非零实全纯二形式 $\psi$ ，它自对偶、谐和，且逐点正交于 Kähler 形式 $\omega_{0}$ 。写 $F=|\psi|^{2}$ ，则
$$\omega_{t}=\left(1+t^{2} F / 2\right)^{-1 / 2}\left(\omega_{0}+t \psi\right)$$
具有恒定长度 $\sqrt{2}$ ，并满足
$$d \omega_{t}=O\left(t^{2}\right), \quad \nabla \omega_{t}=t \nabla \psi+O\left(t^{2}\right)$$
$\nabla \psi \not \equiv 0$ ：由负 Kähler－Einstein 的二形式 Weitzenböck 公式，非零的这类谐和形式不可能平行。因此近乎闭性和一个固定 Hodge 正谱隙仍允许一阶非平行谐和模。这个形式族没有满足真实 Weyl 特征方程；它精确排除的是只靠单位长度与 Hodge 估计实现刚性的证明捷径。

完整几何方程能提供更细的有限维量。令 $H$ 为 $\mathcal{H}_{g}^{+}$的 $L^{2}$ 正交投影，并置
$$P=I-A \succeq 0, \quad \operatorname{spec} P=(0,3 / 2-\eta, 3 / 2+\eta), \quad \mathcal{C}=\left.H P H\right|_{\mathcal{H}_{g}^{+}} .$$
当 $b^{+}>0$ 时，记 $\kappa=\lambda_{\text {min }}(\mathcal{C}) 、 z=(I-H) \omega$ 。因为 $P \omega=0$ ，有精确等式
$$\int\langle P H \omega, H \omega\rangle=\int\langle P z, z\rangle .$$
若 $\lambda_{1}^{+}(g)>0$ 是去核 Hodge 谱隙，则 $\|z\|_{2}^{2} \leq 2\|d \omega\|_{2}^{2} / \lambda_{1}^{+}$。结合 $\|H \omega\|_{2}^{2}+\|z\|_{2}^{2}=$ $2 \operatorname{Vol}_{g}(M)$ ，得到
$$\lambda_{1}^{+}(g) \frac{\kappa}{\kappa+3 / 2+\varepsilon} \leq \frac{1}{\operatorname{Vol}_{g}(M)} \int|d \omega|^{2} \leq \frac{64 \Lambda \varepsilon^{4}}{3\left(9-4 \varepsilon^{2}\right)} .$$
因此在 Hodge 谱隙有统一正下界、且曲率有统一上界的光滑族中，$\kappa=O\left(\varepsilon^{4}\right)$ 。它迫使压缩谱退化，没有证明压缩谱在有限参数处等于零。

命题7．3（压缩核的精确结构）。在连通闭流形上， $\operatorname{dim} \operatorname{ker} \mathcal{C} \leq 1$ 。非零核元素必为 $u \omega$ ，其中 $u$ 处处不为零。改号令 $u>0, v=\log u$ ，则
$$\Delta_{d} v=\frac{Q}{3}|\nabla \omega|^{2}-\frac{8}{3}|\lambda| \eta^{2}, \quad \operatorname{argmax} u \subset\{\eta=0\} .$$
证明。核元素 $\psi$ 满足非负积分 $\int\langle P \psi, \psi\rangle=0$ ，故逐点属于 $\mathbb{R} \omega$ 。由 $d \omega=\theta \wedge \omega$ 及 $d(u \omega)=$ 0 ，得 $d u=-u \theta$ ；沿路径的线性常微分方程给出不消失性和一维性。将 $\Delta_{d}(u \omega)=0$ 与$\omega$ 配对，得 $\left\langle\omega, \Delta_{d} \omega\right\rangle=-2 \Delta_{d} u / u$ 。再用点态平衡和 $|d \omega|^{2}=|d v|^{2}$ ，便得（7．9）。若 $v$ 的最大点有 $\eta>0$ ，则 $d v=0$ 与（7．4）迫使 $N=0$ ，使右端严格负，而非负 Laplacian 在最大点非负，矛盾。 \(\square\)

核元素是 $u \omega$ 闭合，不是 $\omega$ 闭合；故不能据此套用命题7．2。

对任意谐和自对偶形式 $\psi, \phi$ ，完整二阶方程还给出
$$\begin{aligned}
0=\int_{M} & {\left[\sum_{i}\left\langle A \nabla_{e_{i}} \psi, \nabla_{e_{i}} \phi\right\rangle+\frac{s_{g}}{12}\langle A \psi, \phi\rangle\right.} \\
& \left.+\frac{1}{f}\left\langle A^{2} \psi, \phi\right\rangle-\frac{|A|^{2}}{f}\langle\psi, \phi\rangle\right] d V_{g}
\end{aligned}$$
其证明是将 $\nabla^{*} \nabla A$ 整体分部积分到 $\psi \otimes \phi$ ，再用谐和二形式的 Weitzenböck 方程；不能把变权 $f$ 提出拉普拉斯。这些等式在负 Kähler－Einstein 起点容许非平行谐和二形式，并非自动的消失定理。

对真正的闭光滑几何族，在固定束的等距识别下，设起点 Kähler，$w_{1}=\dot{\omega}_{0} 、 P_{1}=\dot{P}_{0}$ ，则
$$w_{1}=-\frac{2}{3} P_{1} \omega_{0} .$$
选随度量光滑变化的标准正交谐和基，使压缩矩阵 $C(0)=\operatorname{diag}\left(0, \frac{3}{2} I\right)$ 。由（7．6）得 $\lambda_{\text {min }} C(t)=O\left(t^{4}\right)$ ，二阶 Schur 补给出必要相容条件
$$C_{00}^{\prime \prime}(0)=\frac{4}{3} \sum_{a>0}\left|C_{a 0}^{\prime}(0)\right|^{2}$$
所有导数包含度量、体积、共形权及谐和空间的变化。这只是二阶必要条件，容许四阶正的小特征值；不构成真实变形的存在性定理。

\section*{7.4 带源的一阶恒等式}

暂不假设 $\delta A=0$ 。仍在长度为 $\sqrt{2}$ 的局部特征标架中，设 $\operatorname{spec} A=(1, \rho,-1-\rho)$ ， $\nabla \omega_{1}=a \otimes \omega_{2}-c \otimes \omega_{3}$ 。以裸指标约定定义
$$A_{a b c d}=\frac{1}{2} \sum_{r} \sigma_{r}\left(\omega_{r}\right)_{a b}\left(\omega_{r}\right)_{c d}, \quad q_{b}=\frac{1}{2}\left(\nabla^{a} A_{a b c d}\right)\left(\omega_{1}\right)_{c d} .$$
这个 $q$ 是正缩并的散度投影；若采用 $\delta=-\nabla^{a}$ ，相差一个负号。令 $U=\iota_{a^{\sharp}} \omega_{2} 、 V=\iota_{c^{\sharp}} \omega_{3}$ 、 $\ell_{1}=U-V=* d \omega_{1} 、 H_{1}=U+V$ ，微分 $A \omega_{1}=\omega_{1}$ 即得
$$q=(1-\rho) U-(2+\rho) V=\frac{3}{2} \ell_{1}-\eta H_{1} .$$
因为 $D=\left|\ell_{1}\right|^{2} 、 N=\left|\ell_{1}\right|^{2}+\left|H_{1}\right|^{2}$ ，平方得到
$$\left(9+4 \eta^{2}\right) D-4 \eta^{2} N=4|q|^{2}+8 \eta\left\langle q, H_{1}\right\rangle .$$
其中交叉项没有预定符号。恢复 $\sqrt{D}=O(\eta \sqrt{N})$ 所需且充分的相对尺度为
$$|q|=O(\eta \sqrt{N}),$$
两个方向允许不同的统一常数。只知道 $q \rightarrow 0$ 不够。

\section*{7.5 在慢插值构造中，源项确实占据首阶}

本节沿用曲面丛章的固定纤维慢插值，另以 $\vartheta$ 表示轮廓，避免与谱参数 $\eta$ 混淆。局部正交余标架为
$$\left(e^{0}, e^{1}, e^{2}, e^{3}\right)=\left(d t, b d \theta, d u, a\left(d s+z \zeta^{\prime} d u\right)\right), \quad b=\ell \cosh t, \quad a=a_{0} \cosh u, \quad z=\vartheta(t / L)$$
令 $j=\tanh u 、 k=\tanh t 、 Q_{0}=a \zeta^{\prime} 、 v=Q_{0} z^{\prime}$ ，并置
$$A_{0}=\frac{v_{u}+2 j v}{4}, \quad C_{0}=\frac{k v-v_{t}}{4} .$$
在标准的自对偶、反自对偶基中，直接由 Koszul 公式与曲率分解得到
$$W^{ \pm}=\left(\begin{array}{ccc}
-2 / 3+v^{2} / 6 & \mp A_{0} & 0 \\
\mp A_{0} & 1 / 3-v^{2} / 3 & C_{0} \\
0 & C_{0} & 1 / 3+v^{2} / 6
\end{array}\right) .$$
两者等谱，最小谱隙为 $1-O\left(L^{-1}\right)$ 。全局闭形式 $\Omega_{ \pm}=e^{01} \pm e^{23}$ 的最小谱投影处处非零，故两条最小特征线全局可定向。若 $d_{0}, e_{0}, f_{0}$ 为矩阵的三个对角元，最小特征值为$\lambda$ ，则
$$x=\frac{A_{0}}{e_{0}-\lambda-C_{0}^{2} /\left(f_{0}-\lambda\right)}, \quad y=-\frac{C_{0} x}{f_{0}-\lambda}$$
给出
$$\omega_{+}=\frac{\Omega_{+}+x\left(e^{02}-e^{13}\right)+y\left(e^{03}+e^{12}\right)}{\sqrt{1+x^{2}+y^{2}}} .$$
另一取向按矩阵共轭相应改号。Schur 补展开为
$$\lambda=-\frac{2}{3}+\frac{v^{2}}{6}-A_{0}^{2}+O\left(L^{-4}\right), \quad x=A_{0}+O\left(L^{-3}\right), \quad y=-C_{0} A_{0}+O\left(L^{-4}\right) .$$
在任意固定阶标架导数下余项一致，且
$$d \omega_{ \pm}=-\left(A_{0, t}+k A_{0}\right) e^{013}+\left(A_{0, u}+j A_{0}\right) e^{123}+O\left(L^{-2}\right) .$$
对固定非平凡轮廓，取 $t=\gamma L 、 \gamma \neq 0$ 且 $\vartheta^{\prime}(\gamma) \neq 0$ ，并取 $Q_{0}^{\prime}+2 j Q_{0} \neq 0$ 的纤维点，便有 $\left\|d \omega_{ \pm}\right\|_{\infty} \asymp L^{-1}$ 。这种纤维点必存在，否则 $Q_{0}=c \operatorname{sech}^{2} u$ ，结合端部支撑条件将迫使 twist 平凡。

令 $\mathrm{P}=\frac{1}{2}($ Ric $-s g / 6)$ 为 Schouten 张量， $\mathrm{C}_{i, j k}=\nabla_{k} \mathrm{P}_{i j}-\nabla_{j} \mathrm{P}_{i k}$ 。本模型的精确分量为
$$\mathrm{P}_{03}=A_{0}, \quad \mathrm{C}_{1,13}=-k A_{0}, \quad \mathrm{C}_{1,02}=0 .$$
故两种取向均有 $\left\|\delta W^{ \pm}\right\|_{\infty} \asymp L^{-1}$ 。另一方面误差支集体积为 $O\left(e^{-L}\right)$ ，所以相应平方积分至多为 $C e^{-L} / L^{2}$ 。指数小的积分没有使任何有限参数下的 Cotton 张量消失。

还可检验无源闭合关系在首阶上的失败。记 $r=Q_{0}^{\prime}+2 j Q_{0}$ ，选 $Q_{0} r \neq 0$ 的点，$B=\vartheta^{\prime}(\gamma) \neq 0, c_{*}=(2 / 3)^{2 / 3}$ 。经（7．2）共形归一化后，有
$$\begin{aligned}
D_{L} & =\frac{c_{*}^{-1} B^{2}}{16 L^{2}}\left\{r^{2}+\left(r^{\prime}+j r\right)^{2}\right\}+O\left(L^{-3}\right) \\
N_{L} & =\frac{c_{*}^{-1} B^{2}}{8 L^{2}}\left\{r^{2}+\left(r^{\prime}+2 Q_{0}\right)^{2}+\left(j r-2 Q_{0}\right)^{2}\right\}+O\left(L^{-3}\right), \\
\eta_{L} & =\frac{3\left|Q_{0} B\right|}{8 L}+O\left(L^{-2}\right) .
\end{aligned}$$

于是 $D_{L} / N_{L}$ 趋于一个严格正的常数，而误用无源式将预言 $O\left(L^{-2}\right)$ 。式（7．12）给 $|q| \asymp L^{-1}$ ，其平方正好提供（7．13）的 $L^{-2}$ 首项；所需相对量 $\eta \sqrt{N}$ 仅为 $O\left(L^{-2}\right)$ 。这是具体的一阶尺度缺失，不是符号上可以忽略的误差。

\section*{7.6 最大正截面处的必要谱分裂}

设闭 Einstein 四流形满足 Ric $=-g$ ，并且最大截面曲率 $\kappa>0$ 。对曲面丛候选及其有限覆盖，群论的非 Hadamard 障碍保证这一正号。令 $x_{0}$ 为 $a+c=\lambda_{\text {max }}\left(W^{+}\right)+$ $\lambda_{\text {max }}\left(W^{-}\right)$的最大点，在该点记 $d=a-\lambda_{2}\left(W^{+}\right) 、 e=c-\lambda_{2}\left(W^{-}\right)$。则
$$12(a d+c e)-4\left(d^{2}+e^{2}\right) \geq 4 \kappa+12 \kappa^{2}+3(a-c)^{2}, \quad \max (d, e)>\kappa / 2 .$$
证明使用精确等式 $K_{\text {max }}(x)=-1 / 3+(a+c) / 2$ 以及 Einstein Weyl 方程
$$\Delta^{\nabla} W^{ \pm}=-2 W^{ \pm}-6\left(W^{ \pm}\right)^{2}+2\left|W^{ \pm}\right|^{2} I .$$
在 $x_{0}$ 延拓单位最大特征向量为一阶平行的局部单位截面，其两个 Rayleigh 商之和从下方支撑 $a+c$ ，故在该点拉普拉斯非正。所得 $0 \geq-2(a+c)-6\left(a^{2}+c^{2}\right)+2\left(\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}\right)$ ，代人谱 $(a, a-d,-2 a+d)$ 及 $(c, c-e,-2 c+e)$ 即得（7．16）。这样处理不要求重特征值可微。

不等式允许 $\kappa \downarrow 0$ 时谱隙同步消失；乘积模型恰在其零端点。因此本章产生的是可检验的必要条件与精确源项账目，没有排除任意负 Einstein 度量。

\section*{第八章 适应曲面纤维化的 Einstein 方程与条件刚性}

本章研究一个可完整写出方程的结构类：给定曲面丛投影，相对于所研究的度量，它已经是黎曼下沉。其价值是能够区分实际方程、可证明的刚性和仍然自由的几何量。光滑流形具有曲面丛结构，不意味着它的任意 Einstein 度量都属于这个结构类。下列结论不能据此升级为底层流形不承载任何 Einstein 度量。

\section*{8.1 统一约定与全部相关曲率块}

除另行说明，设
$$\pi:\left(E^{4}, G\right) \longrightarrow\left(B^{2}, g_{B}\right)$$
为闭、连通、定向流形间的黎曼下沉，纤维 $F_{b}$ 闭、连通、定向，亏格 $p \geq 2$ 。记 $\mathcal{V}=\operatorname{ker} d \pi$ 、 $\mathcal{H}=\mathcal{V}^{\perp}$ ，纤维度量为 $h$ ，纤维高斯曲率为 $K$ 。标量 Laplacian 取 $\Delta=\operatorname{div} \nabla$ ，因而在闭流形上谱非正。

取基底正交标架 $e_{a}$ 的基本水平提升 $X_{a}$ 。对垂直向量场定义水平输运导数 $D_{a} U=$ $\left[X_{a}, U\right]$ ；作用在带基底指标的量上时，同时加入基底 Levi－Civita 联络修正。定义
$$\begin{array}{cl}
2 h\left(S_{a} U, V\right)=\mathcal{L}_{X_{a}} h(U, V), & H_{a}=\operatorname{tr} S_{a}, \quad N=-H^{\sharp}, \\
P_{a}=S_{a}-\frac{1}{2} H_{a} I, & M_{a b}=\operatorname{tr}\left(P_{a} P_{b}\right), \\
\Omega_{a b}=\left[X_{a}, X_{b}\right]^{\mathcal{V}}, \quad \Omega=\Omega_{12}, & Q=\frac{1}{2}|\Omega|_{h}^{2}=\sum_{a, b}\left|A_{X_{a}} X_{b}\right|^{2} .
\end{array}$$
$N$ 是不除以纤维维数的纤维平均曲率向量。 $\left|S_{a}\right|^{2}=\operatorname{tr}\left(S_{a}^{2}\right)$ 为Hilbert－Schmidt 范数。 $D$不是垂直丛的度量联络；后者在水平方向为 $\nabla_{X_{a}}^{\mathcal{V}}=D_{a}+S_{a}$ 。特别地，不能把两种导数混写而保留相同的零阶项。

命题8．1（连接公式及曲率块）。在上述约定下，Koszul 公式给出
$$\begin{aligned}
\nabla_{X_{a}} X_{b} & =\left(\nabla_{e_{a}}^{B} e_{b}\right)^{\mathcal{H}}+\frac{1}{2} \Omega_{a b} \\
\nabla_{X_{a}} U & =D_{a} U+S_{a} U-\frac{1}{2} \sum_{b} h\left(\Omega_{a b}, U\right) X_{b} \\
\nabla_{U} X_{a} & =S_{a} U-\frac{1}{2} \sum_{b} h\left(\Omega_{a b}, U\right) X_{b} \\
\nabla_{U} V & =\nabla_{U}^{F} V-\sum_{a}^{b} h\left(S_{a} U, V\right) X_{a}
\end{aligned}$$
令
$$J_{a}=\frac{1}{2} \sum_{b} h\left(\left(D_{b} \Omega\right)_{a b}+2 S_{b} \Omega_{a b}+H_{b} \Omega_{a b}, \cdot\right) .$$

则相关完整收缩为
$$\begin{aligned}
\operatorname{Ric}_{G}\left(X_{a}, X_{b}\right) & =\left(K_{B}-Q\right) \delta_{a b}-\operatorname{tr}\left(S_{a} S_{b}\right)-\frac{1}{2}\left(D_{a} H_{b}+D_{b} H_{a}\right) \\
\left.\operatorname{Ric}_{G}\left(X_{a}, \cdot\right)\right|_{\mathcal{V}} & =\operatorname{div}_{F}\left(h S_{a}\right)-d_{F} H_{a}-J_{a} \\
\operatorname{tr}_{\mathcal{V}} \operatorname{Ric}_{G} & =2 K+Q-\operatorname{div}_{\mathcal{H}} H-|H|^{2}
\end{aligned}$$
若水平分布可积，则 $\Omega=0$ ，局部水平平凡化中 $G=g_{B}+h_{y}$ ，并有完整的垂直端同态公式
$$h^{-1} \operatorname{Ric}_{V V}=K I-\nabla_{B}^{a} S_{a}-H^{a} S_{a} .$$
式（8．5）适用于任意基底维数、二维纤维。
证明。式（8．2）直接计算度量和括号即可。垂直 Gauss 方程与全部混合截面收缩分别为
$$2 K_{G}\left(V_{1}, V_{2}\right)=2 K-|H|^{2}+|S|^{2}, \quad \sum_{a, i} K_{G}\left(X_{a}, V_{i}\right)=-\operatorname{div}_{\mathcal{H}} H+Q-|S|^{2}$$
相加消去 $|S|^{2}$ ，得到垂直迹。单位水平方向的 Ricci 收缩中，水平截面贡献为 $K_{B}- 3|\Omega|^{2} / 4$ ，混合贡献为 $-D_{X} H_{X}-\left|S_{X}\right|^{2}+|\Omega|^{2} / 4$ ；极化给水平块。混合块可先用垂直度量联络计算，再代入 $\nabla^{\mathcal{V}}=D+S$ ，得到（8．3）中的 $2 S_{b} \Omega_{a b}$ ；该项不能遗漏。

可积时令 $L_{a}=h S_{a}=\frac{1}{2} \partial_{a} h$ 。垂直双线性式含 $-\nabla_{B}^{a} L_{a}-H^{a} L_{a}+2 g^{a b} L_{a} h^{-1} L_{b}$ ；升指标时 $h^{-1} \partial_{a} L_{b}=\partial_{a} S_{b}+2 S_{a} S_{b}$ ，二次项恰好抵消，得到（8．5）。 ${ }^{1}$ \(\square\)

对于一般残差 $R=\operatorname{Ric}_{G}-\lambda G$ ，令 $r_{a}=\left.R\left(X_{a}, \cdot\right)\right|_{\mathcal{V}} 、 t_{V}=\operatorname{tr}{ }_{\mathcal{V}} R$ ，并令 $\mathcal{C}_{a}=\operatorname{div}_{F}\left(J_{a}+\right.$ $\left.r_{a}\right)^{\sharp}$ 。二维曲率变分和面积第一变分给
$$\begin{gathered}
d_{\mathcal{H}} K=-K H+\mathcal{C}, \quad \mathcal{L}_{X_{a}}\left(K d A_{h}\right)=\mathcal{C}_{a} d A_{h}, \\
\operatorname{div}_{G} H^{\sharp}=\operatorname{div}_{\mathcal{H}} H+|H|^{2}=2(K-\lambda)+Q-t_{V}, \\
\left(d_{\mathcal{H}} H\right)_{a b}=\operatorname{div}_{F} \Omega_{a b} .
\end{gathered}$$
第一式中的源项在每条闭纤维上积分为零，但没有逐点符号。其推导使用 $2 X_{a} K=$ $-2 K H_{a}+2 \operatorname{div}_{F} \operatorname{div}_{F}\left(h S_{a}\right)-2 \Delta_{F} H_{a}$ 。此外，$X_{a}\left(\operatorname{div}_{F} U\right)=\operatorname{div}_{F}\left(D_{a} U\right)+U\left(H_{a}\right)$ ，所以水平导数不能与纤维散度无条件交换。

在 $K \neq 0$ 的区域令 $w=K^{-1}$ ，还可保留一种有用的源项形式：
$$\Delta_{\mathcal{H}} w+3 w\left\langle\mathcal{C}, d_{\mathcal{H}} w\right\rangle=2(1-\lambda w)+w\left(Q-t_{V}\right)-w^{2} \operatorname{div}_{\mathcal{H}} \mathcal{C}-w^{3}|\mathcal{C}|^{2} .$$
它揭示了可积性或精确 Einstein 性被放宽后出现的导数项。本章后续刚性证明直接使用 $K$ 的全局最小值，避免要求 $1 / K$ 全局存在。

\footnotetext{
${ }^{1}$ 基本曲率方程来源：B．O＇Neill，The fundamental equations of a submersion（1966），https：／／doi．org／10．1 307／mmj／1028999604。相关曲率公式的公开研究性重述见 Huber－Javaloyes，Corollaries 5、8，https：／／arxiv．org／pdf／2208．04839。本章把所需收缩和范数约定明确写出。
}

\section*{8.2 两种可完整证明的乘积刚性}

定理8．2（可积水平分布的刚性）。设 $\pi:\left(E^{m+2}, G\right) \rightarrow\left(B^{m}, g_{B}\right)$ 为闭连通流形间的黎曼下沉，纤维为闭连通定向高亏格曲面。若 $G$ 为 Einstein 且水平分布可积，则 Einstein常数 $\lambda<0$ ，纤维全测地且高斯曲率恒为 $\lambda$ ，基底满足 $\operatorname{Ric}_{g_{B}}=\lambda g_{B}$ 。该下沉局部为乘积；某个有限基底覆盖上的拉回度量为全局等距乘积。

证明。此时 $Q=J=R=0$ ，式（8．6）给
$$d_{\mathcal{H}} K=-K H, \quad \operatorname{div}_{G} H^{\sharp}=2(K-\lambda), \quad \Delta_{\mathcal{H}} K=2 K\left(|H|^{2}-K+\lambda\right) .$$
Gauss－Bonnet 保证总空间上 $K$ 的全局最小值 $k_{0}<0$ 。在最小点，第一式使 $H=0$ ，故$0 \leq \Delta_{\mathcal{H}} K=-2 k_{0}\left(k_{0}-\lambda\right)$ ，即 $K \geq k_{0} \geq \lambda$ 。这里仅用 Hessian 在最小点半正定，不需要水平算子严格椭圆或水平叶闭合。再对全空间散度积分，得到 $0=2 \int_{E}(K-\lambda) d V_{G}$ ，因而 $K \equiv \lambda<0, ~ H=0$ 。

固定 $b$ 和 $v \in T_{b} B$ 。混合方程使 $h\left(S_{v} \cdot, \cdot\right)$ 为纤维 TT 张量，水平块使 $\left|S_{v}\right|^{2}= \operatorname{Ric}_{B}(v, v)-\lambda|v|^{2}$ 沿纤维恒定。二维 TT 张量是全纯二次微分的实部，非零者在高亏格闭曲面上必有零点，故 $S_{v}=0$ 。也可仅用下面的 Euler 丛论证完成此步。于是两分布平行。水平 holonomy 落在固定闭双曲纤维的有限等距群；取其核对应的有限基底覆盖，得到全局乘积。 \(\square\)

证明中并未预设纤维曲率符号、纤维极小性或 $H$ 沿纤维恒定。较早依赖 $K<0$的倒数曲率证明已被这个版本包含，不再作为另一个结果重复列出。

引理8．3（纤维 Euler 障碍）。在闭定向曲面 $F$ 上，若 $\chi(F) \neq 0$ ，则实秩二丛 $\operatorname{Sym}_{0}^{2} T^{*} F$不承载无零点光滑截面。设 $P: T_{b} B \rightarrow \operatorname{Sym}_{0}(T F)$ 为线性映射场， $\operatorname{dim} B=2$ ，令$M(v, w)=\operatorname{tr}\left(P_{v} P_{w}\right)$ 。若 $M^{0}$ 沿整条纤维恒定，则 $M^{0}=0$ 。

证明。纤维正交标架旋转 $\theta$ 时，无迹对称矩阵的两分量旋转 $2 \theta$ ，故该丛 Euler 数的绝对值为 $2|\chi(F)|$ 。若恒定的 $D=M^{0}$ 有正特征值 $d>0$ ，取相应固定单位方向 $v$ 。写$M=t(x) I+D$ ，由 $M \geq 0$ 得 $t \geq d$ ，于是 $\left|P_{v}\right|^{2} \geq 2 d>0$ ，与非零 Euler 数矛盾。 \(\square\)

定理 8.4 （基本平均曲率的刚性）。在本章四维闭下沉设定中，假设 $\operatorname{Ric}_{G}=\lambda G 、 \lambda<0$ 。若平均曲率 $H$ 为 basic，即为基底一形式的拉回，则 $H=0$ ，且 $A=T=0$ 。结论同样是局部同曲率双曲乘积和有限基底覆盖上的全局乘积。

证明。令 $a(b)=\operatorname{Area}\left(F_{b}\right)$ 。面积第一变分给 $H=\pi^{*} d \log a$ ，因此这里的 basic 一形式全局正合。置 $f=\log a 、 u=\sqrt{a}$ 。水平 Einstein 块成为
$$M+\nabla_{B}^{2} f+\frac{1}{2} d f \otimes d f=\left(K_{B}-\lambda-Q\right) g_{B}$$
取无迹部分，$M^{0}=-2 u^{-1}\left(\nabla_{B}^{2} u\right)^{0}$ 沿纤维恒定。引理8．3使 $\left(\nabla_{B}^{2} u\right)^{0}=0$ 。
闭负 Einstein 四流形的 Gauss－Bonnet 公式给 $\chi(E)>0$ ；由 $\chi(E)=\chi(F) \chi(B)$ 得$\chi(B)<0$ 。纯迹 Hessian 使 $\nabla u$ 为共形向量场，而闭高亏格曲面不存在非零共形向量场，故 $u$ 为常数、 $H=0$ 。

到二维目标的极小黎曼下沉是无临界点调和态射。Wood 的 Einstein 四维定理给与原度量正交且使映射全纯的可积复结构，必要时反转源定向。LeBrun 的紧负 Einstein Hermitian 刚性使原度量 Kähler。 ${ }^{2}$ 此 $J$ 保持 $\mathcal{H}, \mathcal{V}$ ，而 $A_{X}(J X)=J A_{X} X=0$ 。水平二维即给 $A=0$ ，再接定理8．2。 \(\square\)

对无限 Dehn twist 单值变换的候选丛 $E_{D}$ ，两定理都排除相应结构类中的 Einstein度量；所用矛盾是有限等距 holonomy 与无限外单值变换冲突。它们没有排除不适应原投影的度量。

另一个需要区分的操作是用纤维体积将 basic 平均曲率消去。一般 $r$ 维闭纤维下，若其体积为 $a$ ，则 $N^{b}=-d \log a$ 。改成 $a^{-2 / r} G_{\mathcal{V}}+G_{\mathcal{H}}$ ，或者作总共形改变 $\widetilde{G}=a^{-2 / r} G$ ，确实可令新度量的纤维极小；但通常破坏 Einstein 条件。闭负 Einstein 度量的两个共形 Einstein 代表只能相差常数：令 $\widetilde{G}=e^{2 u} G 、 w=e^{-u}$ ，无迹共形 Ricci 方程使 $\left(\nabla^{2} w\right)^{0}=0$ ，而积分 Bochner 式为
$$0=\frac{n-1}{n} \int(\Delta w)^{2} d V_{G}-\lambda \int|d w|^{2} d V_{G}$$
$\lambda<0$ 迫使 $d w=0$ 。因此不能把原度量的 Einstein 性与修改后度量的调和态射性组合调用 Wood 定理。

\section*{8.3 纤维面积方程、等号刚性和残差界}

命题8．5（非 basic 面积方程）。允许 $A \neq 0$ 和非 basic 平均曲率，设 $\operatorname{Ric}_{G}=-\ell G+R$ 、 $\ell>0 、\|R\|_{\mathrm{op}, \infty} \leq \varepsilon<\ell$ 。置
$$A_{F}=-2 \pi \chi(F)>0, \quad a_{*}=A_{F} / \ell, \quad \bar{Z}=a^{-1} \int_{F_{b}} Z d A_{h}, \quad q_{\mathrm{av}}=\sup _{B} \bar{Q}$$
则
$$\Delta_{B} a=4 \pi \chi(F)+2 \ell a+a \bar{Q}-a \overline{t_{V}},$$
并有
$$\frac{A_{F}}{\ell+\varepsilon+q_{\mathrm{av}} / 2} \leq a(b) \leq \frac{A_{F}}{\ell-\varepsilon}, \quad \frac{a_{\max }}{a_{\min }} \leq \frac{\ell+\varepsilon+q_{\mathrm{av}} / 2}{\ell-\varepsilon} .$$
特别地，上侧面积界仅需 Ricci 零阶残差。
证明．水平流满足 $\mathcal{L}_{X_{a}} d A_{h}=H_{a} d A_{h}$ ，故
$$X_{a} a=\int_{F} H_{a} d A_{h}, \quad \Delta_{B} a=\int_{F}\left(\operatorname{div}_{\mathcal{H}} H+|H|^{2}\right) d A_{h}$$
第二次变分中必须保留 $|H|^{2}$ 的纤维平均，不能换成平均 $H$ 的平方。代入（8．6）和 Gauss－Bonnet 即得方程。面积最大点和最小点的比较，加上 $\left|t_{V}\right| \leq 2 \varepsilon$ ，给全部界。 \(\square\)

\footnotetext{
${ }^{2}$ Wood 原始来源：https：／／doi．org／10．1142／S0129167X92000187。本整理实际核对的是 Baird－Pantilie 对其无临界点定理的研究性重述，https：／／arxiv．org／pdf／0709．0672；未取得 Wood 出版社全文，不声称逐页复查其证明。LeBrun，Proposition 1，https：／／arxiv．org／pdf／1010．0238 明确给非 Kähler 紧 Einstein Hermitian四流形的 Einstein 常数为正。
}

若 $A=0$ ，则 $q_{\mathrm{av}}=0$ ，并且
$$\frac{a_{*}}{1+\varepsilon / \ell} \leq a \leq \frac{a_{*}}{1-\varepsilon / \ell}, \quad|\bar{K}+\ell| \leq \varepsilon .$$
两端由曲率分别为 $-\ell$ 与 $-\ell \pm \varepsilon$ 的闭曲面乘积达到，因此这个结构类中的面积常数是尖锐的；平均曲率界不能去掉平均号。

面积上界还保留明确的等号信息。令 $U=A_{F} /(\ell-\varepsilon) 、 w=U-a \geq 0$ ，则
$$\left[-\Delta_{B}+2(\ell-\varepsilon)\right] w=a\left(\bar{Q}+2 \varepsilon-\overline{t_{V}}\right) \geq 0 .$$
若一条纤维 $a=U$ ，强最大值原理给 $w=0$ ，从而 $Q=0 、 t_{V}=2 \varepsilon$ 处处；垂直残差块等于 $\varepsilon h$ 。当 $\varepsilon>0$ 时尚不能推出 $T=0$ 。

精确负 Einstein 情形 $\varepsilon=0$ 中，以下四条件等价：
$$A=0 \quad \Longleftrightarrow \quad \text { 该下沉局部为同曲率乘积 } \quad \Longleftrightarrow \quad K \geq-\ell \quad \Longleftrightarrow \quad \exists b: a(b)=a_{*} \text {. }$$
这里 $K \geq-\ell$ 与 Gauss－Bonnet 使 $a \geq a_{*}$ ，再用上界即可。若不满足这些条件，则每条纤维都有 $a<a_{*} 、 \bar{K}<-\ell$ ，因而包含 $K<-\ell$ 的点；不能再推出 $A$ 在每条纤维都非零。

\section*{8．3．1 曲率最低值的定量估计，以及无法省去的导数}

假定水平可积，记 $r_{a}=\left.R\left(X_{a}, \cdot\right)\right|_{\mathcal{V}} 、 \mathcal{C}_{a}=\operatorname{div}_{F} r_{a}^{\sharp} 、 \mathfrak{d}=\operatorname{div}_{\mathcal{H}} \mathcal{C} 、 d_{+}=\|\max (\mathfrak{d}, 0)\|_{\infty}$ 。由（8．6），在 $K$ 的负全局最小值 $-x$ 处有
$$0 \leq 2 x(\ell+\varepsilon-x)+d_{+} .$$
其中舍去的项是 $|\mathcal{C}|^{2} / K \leq 0$ ；不用另估计 $\|\mathcal{C}\|_{\infty}$ 。所以
$$K \geq-\frac{\ell+\varepsilon+\sqrt{(\ell+\varepsilon)^{2}+2 d_{+}}}{2} .$$
若把右侧负数写为 $-\ell-\zeta$ ，则
$$\zeta \leq \varepsilon+\frac{d_{+}}{2(\ell+\varepsilon)}, \quad \overline{|K+\ell|} \leq \varepsilon+2 \zeta .$$
这改进了要求 $1 / K$ 全局有界的估计，但 $\mathfrak{d}$ 包含混合 Ricci 残差的两次导数；不是原始零阶残差。

这个区别可由真实闭几何检验。固定曲率 -1 的 $\left(B, g_{B}\right) 、\left(F, h_{0}\right)$ ，选坐标截断，在其恒一的中心令
$$u_{N}=-N^{-5 / 2} \chi_{B} \chi_{F} \cos (N s) \cos (N z), \quad G_{N}=g_{B}+e^{2 u_{N}} h_{0} .$$
这是全局光滑、水平可积的下沉族。全部残差块为
$$\begin{aligned}
R_{a b} & =-2\left(\nabla_{B}^{2} u_{N}\right)_{a b}-2\left(u_{N}\right)_{a}\left(u_{N}\right)_{b}, \\
r_{a} & =-d_{F}\left(u_{N}\right)_{a} \\
h^{-1} R_{V V} & =\left\{e^{-2 u_{N}}\left(-1-\Delta_{h_{0}} u_{N}\right)+1-\Delta_{B} u_{N}-2\left|d_{B} u_{N}\right|^{2}\right\} I .
\end{aligned}$$

因此 $\|R\|_{\infty}=O\left(N^{-1 / 2}\right) \rightarrow 0$ ，但
$$\mathfrak{d}=-e^{-2 u_{N}} \Delta_{B} \Delta_{h_{0}} u_{N}+2 e^{-2 u_{N}}\left\langle d_{B} u_{N}, d_{B} \Delta_{h_{0}} u_{N}\right\rangle$$
在中心等于 $e^{2 N^{-5 / 2}} N^{3 / 2} \rightarrow+\infty 。 \mathcal{C}$ 的最大范数也可达到 $c N^{1 / 2}$ 。该例只证明上述导数控制不能由 Ricci 零阶误差直接取得；其纤维曲率仍接近 -1 ，底层乘积流形承载Einstein 度量。

若改为假设 $H$ basic，而不要求 $A=0$ ，水平无迹块和引理8．3给另一种真正只用零阶残差的结论：
$$\left\|\left(\nabla_{B}^{2} \sqrt{a}\right)^{0}\right\|_{\mathrm{op}} \leq \frac{1}{2} \varepsilon \sqrt{a} .$$
证明是在 $-2 a^{-1 / 2}\left(\nabla^{2} \sqrt{a}\right)^{0}$ 的正特征值大于 $\varepsilon$ 时，利用水平残差无迹部分的算子范数至多 $\varepsilon$ ，构造纤维上无零点的 $P_{v}$ 。从这个过定椭圆估计到 $a$ 近常数，仍需要依赖基底几何的逆估计。

\section*{8.4 非基本平均曲率：测度变分、四次矩与条件控制}

令
$$\begin{aligned}
& f=\log a, \quad d \mu_{b}=a^{-1} d A_{h}, \quad \eta=H-\pi^{*} d f, \\
& C=\overline{\eta \otimes \eta}, \quad \mathcal{E}=M+Q g_{B}, \quad \mathcal{R}=\left.R\right|_{\mathcal{H} \times \mathcal{H}}
\end{aligned}$$
$\bar{\eta}=0$ ，但 $\eta$ 未知是否为零。准确的密度变分是
$$\mathcal{L}_{X_{a}} \mu_{b}=\eta_{a} \mu_{b}, \quad \nabla_{a} \bar{Z}=\overline{D_{a} Z}+\overline{Z \eta_{a}}, \quad \overline{D_{a} \eta_{b}}=-C_{a b} .$$
对于带基底指标的 $Z$ ，两边使用基底协变导数。遗漏这里的第二项，会同时改变后续协方差符号和三、四次矩系数。

平均水平块给
$$\operatorname{Ric}_{B}=(-\ell+\bar{Q}) g_{B}+2 a^{-1 / 2} \nabla_{B}^{2} \sqrt{a}+\bar{M}-\frac{1}{2} C+\overline{\mathcal{R}} .$$
令 $D_{0}=-2 a^{-1 / 2}\left(\nabla_{B}^{2} \sqrt{a}\right)^{0}$ ，并定义
$$\mathcal{B}_{\eta}=\left[\operatorname{sym} D \eta+d f \odot \eta+\frac{1}{2} \eta \otimes \eta\right]^{0}, \quad \alpha \odot \beta=\frac{1}{2}(\alpha \otimes \beta+\beta \otimes \alpha) .$$
点态水平块与 Euler 引理给
$$M^{0}=D_{0}-\mathcal{B}_{\eta}-\mathcal{R}^{0}, \quad\left\|D_{0}(b)\right\|_{\mathrm{op}} \leq \sup _{F_{b}}\left\|\mathcal{B}_{\eta}+\mathcal{R}^{0}\right\|_{\mathrm{op}} .$$
所以非 basic 波动及其水平导数正是基本平均曲率证明的实际误差源。
命题8．6（中心化 Riccati 方程和四次矩恒等式）。对于单位基底测地线方向 $v$ 及其水平提升，写 $\eta_{v}=\eta(v) 、 C_{v}=C(v, v) 、 \mathcal{E}_{v}=\mathcal{E}(v, v) 、 r_{v}=\mathcal{R}(v, v)$ 。则
$$\begin{aligned}
D_{v} H_{v} & =K_{B}+\ell-\mathcal{E}_{v}-r_{v}-\frac{1}{2} H_{v}^{2}, \\
D_{v} \eta_{v}+d f(v) \eta_{v} & =-\left[\left(\mathcal{E}_{v}+r_{v}\right)-\overline{\mathcal{E}_{v}+r_{v}}\right]-\frac{1}{2}\left(\eta_{v}^{2}+C_{v}\right), \\
\left(\nabla_{v} C\right)(v, v)+2 d f(v) C_{v} & =-2 \overline{\eta_{v}\left(\mathcal{E}_{v}+r_{v}\right)} .
\end{aligned}$$

在 $T^{1} B$ 上取 Liouville 测度 $d L$ ，其圆周角度因子总质量为一，则
$$\int_{T^{1} B} a^{3}\left(\overline{\eta_{v}^{4}}+3 C_{v}^{2}\right) d L=-6 \int_{T^{1} B} a^{3} \operatorname{Cov}_{\mu_{b}}\left(\eta_{v}^{2}, \mathcal{E}_{v}+r_{v}\right) d L$$
证明．第一式是水平块，减去其纤维平均并使用（8．17）得第二式；对 $C_{v}$ 求导时密度变分贡献 $\overline{\eta_{v}^{3}}$ ，与第二式产生的三次项恰好抵消，得到第三式。

在闭流形 $\mathcal{N}=E \times{ }_{B} T^{1} B$ 上令 $\mathcal{X}$ 为水平测地流，$d \nu=d \mu_{b} d L$ 。由密度变分
$$\operatorname{div}_{\nu} \mathcal{X}=\eta_{v}, \quad \operatorname{div}_{a^{3} \nu} \mathcal{X}=\eta_{v}+3 d f(v) .$$
将中心化方程乘 $3 \eta_{v}^{2}$ 并积分，与 $\int a^{3} \mathcal{X}\left(\eta_{v}^{3}\right) d \nu=-\int a^{3}\left(\eta_{v}^{4}+3 d f(v) \eta_{v}^{3}\right) d \nu$ 比较；三次漂移消去，且 $\overline{C_{v} \eta_{v}^{2}}=C_{v}^{2}$ ，得结论。 \(\square\)

命题 8.7 （单侧能量振荡控制）。设
$$d_{\mathcal{E}}=\sup _{b, x \in F_{b},|v|=1}\left(\overline{\mathcal{E}_{v}}-\mathcal{E}_{v}\right)_{+} .$$
则有
$$\|\eta\|_{\infty} \leq \frac{a_{\max }}{a_{\min }} \sqrt{2 d_{\mathcal{E}}+4 \varepsilon},$$
以及不含面积比的加权界
$$\frac{\int_{B} a^{3} \overline{|\eta|^{2}} d A_{B}}{\int_{B} a^{3} d A_{B}} \leq \frac{3}{2}\left(d_{\mathcal{E}}+\sqrt{d_{\mathcal{E}}^{2}+4 \varepsilon^{2}}\right)$$
证明．置 $z=a \eta_{v}$ 。由（8．20）， $\mathcal{X} z \leq a\left(d_{\mathcal{E}}+2 \varepsilon\right)-z^{2} /(2 a)$ 。在紧致 $\mathcal{N}$ 上分别取 $z$ 的最大点、最小点，得到（8．22）。

对概率测度 $a^{3} d L / \int a^{3} d L$ 记平均为 $\langle\cdot\rangle_{w}$ ，置 $A_{4}=\left\langle\overline{\eta_{v}^{4}}\right\rangle_{w} 、 B_{2}=\left\langle C_{v}^{2}\right\rangle_{w} 、 m=\left\langle C_{v}\right\rangle_{w}$ 。有 $A_{4} \geq B_{2} \geq m^{2}$ 。单侧振荡控制能量协方差；残差满足 $\operatorname{Var}\left(r_{v}\right) \leq \varepsilon^{2}$ 。式（8．21）因而给
$$A_{4}+3 B_{2} \leq 6 d_{\mathcal{E}} m+6 \varepsilon \sqrt{A_{4}-B_{2}} .$$
令 $y=\sqrt{A_{4}-B_{2}}$ ，用 $6 \varepsilon y-y^{2} \leq 9 \varepsilon^{2}$ ，得 $4 m^{2} \leq 6 d_{\mathcal{E}} m+9 \varepsilon^{2}$ 。解二次不等式，再用角度平均 $\int C(v, v) d \theta=\frac{1}{2} \operatorname{tr} C$ ，即得加权界。 \(\square\)

精确 Einstein 情形中， $\mathcal{E}$ basic 推出 $d_{\mathcal{E}}=0$ ，因而 $H$ basic，最终得到乘积。一般情形 $d_{\mathcal{E}}$ 是独立几何输入，不能把它重命名为 Ricci 残差。 $a^{3}$ 权重也不能未经比较换成总空间体积权重 $a$ 。

还有一个更直接的条件估计。记 $\delta_{B}=\sup _{B}\left(K_{B}+\ell\right)_{+}$，在 $H_{v}$ 的全局两端使用第一条 Riccati 方程，得到
$$\|H\|_{\infty}^{2} \leq 2\left(\delta_{B}+\varepsilon\right), \quad \frac{1}{\operatorname{Vol}(E)} \int_{E}(\operatorname{tr} M+2 Q) d V_{G} \leq 3\left(\delta_{B}+\varepsilon\right)$$
第二式由水平迹积分和第一式得到。若精确 Einstein 且 $K_{B} \leq-\ell$ ，则直接有 $H=M=$ $Q=0 、 K_{B}=-\ell$ ，无需再调用 Wood－LeBrun。但 $\delta_{B}$ 同样不是原题已知量。

\section*{8．4．1 哪些操作没有增加新的约束}

对基底函数 $\phi$ ，置 $L_{a}=\Delta_{B}+\langle d f, d \cdot\rangle$ 、 $v=\nabla^{B} \phi$ 。完整公式为
$$\begin{aligned}
\Delta_{G}(\phi \circ \pi) & =\left(L_{a} \phi\right) \circ \pi+\eta(v) \\
\left|\nabla_{G}^{2}(\phi \circ \pi)\right|^{2} & =\left|\nabla_{B}^{2} \phi\right|^{2}+M(v, v)+\frac{1}{2} H_{v}^{2}+Q|v|^{2}
\end{aligned}$$
因此 $\Delta_{G}$ 保持全部基本函数当且仅当 $\eta=0$ 。将两式代人总空间 Bochner 恒等式，恰好还原（8．18）的加权版本，并没有额外得到 $\int C \leq 0$ 。 Lott 的相应下沉比较定理要求纤维测度在水平输运下保持到比例常数；在本设定中这正是 $\eta=0$ ，不能作为证明 $\eta=0$的前提。 ${ }^{3}$

混合块还给实际的纤维椭圆方程（此处 $R=0)$ ：
$$\begin{aligned}
\operatorname{div}_{F}\left(h P_{a}\right)-\frac{1}{2} d_{F} \eta_{a} & =J_{a}, \quad \Delta_{F} \eta_{a}=2 \operatorname{div}_{F} \operatorname{div}_{F}\left(h P_{a}\right)-2 \operatorname{div}_{F} J_{a} \\
\frac{1}{2} \int_{F}\left|d_{F} \eta_{a}\right|^{2} d A_{h} & =-\int_{F}\left\langle h P_{a},\left(\nabla_{F}^{2} \eta_{a}\right)^{0}\right\rangle d A_{h}-\int_{F}\left\langle J_{a}, d_{F} \eta_{a}\right\rangle d A_{h}
\end{aligned}$$
零均值排除了常数核，却没有消除右侧的无定号源项；$P_{a}$ 尚非 TT，纤维谱隙也未获统一下界。

固定原映射和原源度量，仅把目标换成任意 $k$ ，则
$$\tau_{k}(\pi)=\tau\left(\mathrm{id}:\left(B, g_{B}\right) \rightarrow(B, k)\right) \circ \pi+d \pi\left(H^{\sharp}\right) .$$
所以存在目标使固定投影调和，必先使 $H$ basic，进而已经是乘积；改变映射本身则是下一章的另一问题。

\section*{8．5 Gram 各向同性与局部复结构}

令 $J_{H}, J_{V}$ 分别为水平和垂直定向二维平面的正四分之一旋转，定义全局正交几乎复结构 $J_{s}=J_{H} \oplus s J_{V}, s= \pm 1$ 。若 $X_{2}=J_{H} X_{1}$ ，从 $h\left(J_{V} U, V\right)=d A_{h}(U, V)$ 的变分得到
$$D_{a} J_{V}=J_{V} S_{a}-S_{a} J_{V}=2 J_{V} P_{a} .$$
采用 $N_{J}(Y, Z)=[J Y, J Z]-J[J Y, Z]-J[Y, J Z]-[Y, Z]$ ，完整混合分量为
$$N_{J_{s}}\left(X_{1}, U\right)=2\left(P_{1}+s J_{V} P_{2}\right) U .$$
其余分量由二维 $J_{s}$－不变平面及 $N_{J}(J Y, Z)=-J N_{J}(Y, Z)$ 确定；这里没有遗漏 $H$ 或$\Omega$ 项。令 $F_{s}=P_{1}+s J_{V} P_{2}$ ，则
$$M^{0}=0 \Longleftrightarrow F_{+}=0 \text { 或 } F_{-}=0, \quad\left|F_{+}\right|^{2}\left|F_{-}\right|^{2}=4\left\|M^{0}\right\|_{\text {op }}^{2} .$$
在 $P_{1} \neq 0$ 的连通区域符号唯一且恒定；零点上不能无证明地拼成一个全局可积 $J_{s}$ 。若$M^{0}$ 在某非空开集恒零，则其中必有较小非空开集上一个固定 $J_{s}$ 可积。

\footnotetext{
${ }^{3}$ J．Lott，Some Geometric Properties of the Bakry－Émery－Ricci Tensor，Theorem 2，https：／／arxiv．org／pd f／math／0211065。
}

结合本汇编拓扑与谱部分对候选 $E_{D}$ 建立的＂任意假想 Einstein 度量没有 Hermi－ $\operatorname{tian}$ 开集＂条件，得到：
$$\mathcal{Z}=\left\{M^{0}=0\right\} \text { 闭且无内点, } \mathcal{Z} \cap F_{b} \neq \varnothing \text { 对所有 } b \text {. }$$
第二项不需要 Einstein：固定纤维上的 $F_{+}, F_{-}$都是 $\operatorname{Sym}_{0}^{2} T^{*} F$ 的截面，各有零点。第一项使用 Einstein Hermitian 的局部半 Weyl 重谱条件。 ${ }^{4}$ 这两种零集性质相容；穿过每条纤维不意味着包含开集。

\section*{8.6 协方差的局部精确反例与闭延拓门槛}

\section*{8．6．1 垂直迹增加了哪些信息}

在精确 Einstein 情形，水平迹减垂直迹给
$$\operatorname{tr} \mathcal{E}=2\left(K_{B}-K\right)-Q+\frac{1}{2}|H|^{2} .$$
因此完整方程不允许独立任意指定 $K, M, Q, H$ 。令 $s=|\eta|^{2} 、 b=d \log a 、 Z=\eta \otimes \eta-C$ ，对（8．21）作二维角度平均并代入（8．31），得到
$$\begin{aligned}
& \int_{B} a^{3}\left[3 \overline{s^{2}}-(\operatorname{tr} C)^{2}+2|C|^{2}\right] d A_{B} \\
& \quad=\int_{B} a^{3}\left[8 \operatorname{Cov}(s, K)+4 \operatorname{Cov}(s, Q)-4 \overline{Z: M^{0}}-4\langle b, \overline{s \eta}\rangle\right] d A_{B}
\end{aligned}$$
左侧至少为 $3 \int a^{3} \overline{\left.\eta\right|^{4}}$ 。Gauss－Bonnet 固定 $\int K$ ，不固定 $\operatorname{Cov}(s, K) ; Q \geq 0$ 也不决定其协方差符号。下述实际局部几何进一步证明，不能仅靠完整局部 Einstein 方程推出逐纤维协方差非负。

命题8．8（常负截面曲率下的负协方差模型）。任给闭定向亏格 $p \geq 2$ 曲面 $F$ ，存在开矩形 $B$ 上的光滑黎曼下沉 $\pi:(B \times F, G) \rightarrow\left(B, g_{B}\right)$ ，其所有纤维闭，水平分布可积，且 $\sec _{G}=-1$ 。某基底点 $b_{0}$ 和方向 $v$ 满足
$$\operatorname{Cov}_{\mu_{b_{0}}}\left(\eta_{v}^{2}, \mathcal{E}_{v}\right)<0,$$
角度平均协方差也严格为负。
证明．固定闭双曲 $\left(F, h_{0}\right)$ 和非零全纯二次微分的实部 $q$ 。小参数 $\rho>0$ 下，求
$$h=e^{2 u} h_{0}, \quad A=\rho h^{-1} q, \quad \Delta_{h_{0}} u-e^{2 u}+1-\frac{1}{2} \rho^{2} e^{-2 u}|q|_{h_{0}}^{2}=0 .$$
在 $(u, \rho)=(0,0)$ 的线性化 $\Delta_{h_{0}}-2$ 可逆，隐函数定理给光滑解。 $h, A$ 满足曲率 -1 的Gauss－Codazzi 方程且 $\operatorname{tr} A=0$ 。令 $\rho$ 足够小使 $|A|^{2}<1$ ，则
$$g_{3}=d r^{2}+h((\cosh r I+\sinh r A) \cdot,(\cosh r I+\sinh r A) \cdot)$$

\footnotetext{
${ }^{4}$ 局部 Riemannian Goldberg－Sachs 结论见 Gover－Hill－Nurowski，Theorems 1．2、2．1，https：／／arxiv．org／pd f／0911．3364。本处候选无 Hermitian 开集的全局拓扑及解析性前提由本汇编相应章节提供，不从点态 Nijenhuis零点推出。
}

在闭 $F$ 的统一管状邻域内具有截面曲率 -1 。这是经典极小曲面正常模型。 ${ }^{5}$
记 $k=|A|^{2} 、 m=\bar{k}>0$ 。二次微分有零点，因此有非空开集 $U$ 满足 $k<m / 2$ 。取支撑于 $U$ 的非零 $\phi$ ，使 $\bar{\phi}=0$ ，则 $\overline{\phi^{2}(k-m)}<0$ 。形算子取 $A=\nabla \nu$ ；平均曲率Jacobi 算子为 $L=-\Delta_{h}+2-|A|^{2}>0$ 。令 $\psi=L^{-1} \phi$ ，作小正常图 $F_{\delta}$ 。其平均曲率和无迹形算子满足
$$H_{\delta}=\delta \phi+O\left(\delta^{2}\right), \quad P_{\delta}=A+O(\delta), \quad \eta_{\delta}=\delta \phi+O\left(\delta^{2}\right) .$$
归一化面积测度光滑变化，故
$$\operatorname{Cov}_{\mu_{\delta}}\left(\eta_{\delta}^{2},\left|P_{\delta}\right|^{2}\right)=\delta^{2} \overline{\phi^{2}(k-m)}+O\left(\delta^{3}\right)<0 .$$

用 $F_{\delta}$ 的法向距离重写 $g_{3}=d r^{2}+h_{\delta, r}$ ，并置
$$G=d t^{2}+\cosh ^{2} t\left(d r^{2}+h_{\delta, r}\right), \quad g_{B}=d t^{2}+\cosh ^{2} t d r^{2}$$
Warped product 公式使全部截面曲率恰为 -1 ，因此所有 Ricci 块同时精确满足 $\operatorname{Ric}_{G}=$ $-3 G$ 。在 $(t, r)=(0,0), S_{1}=0 、 S_{2}=A_{\delta} 、 \eta_{1}=0 、 \eta_{2}=\eta_{\delta} 、 \mathcal{E}=\left|P_{\delta}\right|^{2} e^{2} \otimes e^{2}$ 。方向 $e_{2}$的协方差为（8．33），角度平均为它的3／8倍。 \(\square\)

基底是开矩形，水平流存在边界通量，不能在该模型上使用无边界的四次矩积分恒等式。它也不能保留原样延拓为任意紧夹逼的闭下沉：

命题 8.9 （保留指定纤维的闭延拓门槛）。令上述指定 $F_{\delta}$ 的主曲率绝对值不超过 $\kappa<1$ 。任何保留其诱导纤维度量、并成为闭四维曲面黎曼下沉的延拓 $\widetilde{G}$ ，均满足
$$\left\|\operatorname{Ric}_{\widetilde{G}}+3 \widetilde{G}\right\|_{\mathrm{op}, \infty} \geq 2-\kappa^{2}$$
归一化 $\widehat{G}=3 \widetilde{G}$ 后，下界为 $\left(2-\kappa^{2}\right) / 3>1 / 3$ 。
证明．指定纤维上 $K=-1+\operatorname{det} A_{\delta} \geq-1-\kappa^{2}$ ，故其面积至少为 $A_{F} /\left(1+\kappa^{2}\right)$ 。若残差$\varepsilon<3$ ，闭面积上界（8．9）给其面积至多 $A_{F} /(3-\varepsilon)$ 。比较即得 $\varepsilon \geq 2-\kappa^{2} ; \varepsilon \geq 3$ 时当然成立。论证允许延拓在其他区域有 $A \neq 0$ 。 \(\square\)

这个门槛只限制指定纤维内禀度量和下沉结构都被保留的闭合方式，不是原题的维数统一间隙；改变纤维几何或不再要求下沉的方案不受此结论排除。

\section*{8.7 反向检验：高频形变与未适应投影的源项}

若 $H$ basic，水平块中除残差外各项都沿纤维恒定，故
$$\overline{\mathcal{E}_{v}}-\mathcal{E}_{v}=r_{v}-\bar{r}_{v}, \quad d_{\mathcal{E}} \leq 2 \varepsilon .$$

\footnotetext{
${ }^{5}$ Huang－Lucia，Minimal immersions of closed surfaces in hyperbolic three－manifolds，§§2．2－2．3，https：／／arxiv．org／pdf／1011．1313；其中小参数极小曲面存在性归于 Uhlenbeck。Huang－Wang，Lemma 2．2，https：／／arxiv．org／pdf／1001．4217 给相同等距曲面公式。本构造不声称这些经典步骤原创。
}

一般非 basic 情形则有精确恒等式
$$\overline{\mathcal{E}_{v}}-\mathcal{E}_{v}=(\operatorname{sym} D \eta)(v, v)+d f(v) \eta_{v}+\frac{1}{2}\left(\eta_{v}^{2}+C_{v}\right)+r_{v}-\bar{r}_{v} .$$
因而 $d_{\mathcal{E}} \leq\|\operatorname{sym} D \eta\|_{\infty}+\|d f\|_{\infty}\|\eta\|_{\infty}+\|\eta\|_{\infty}^{2}+2 \varepsilon$ 。这精确指出了把 $\eta$ 小转成能量振荡小时仍需控制的导数。

为检验最直接的高频构造，固定双曲乘积，选纤维上的光滑无迹自伴端同态 $Z$ ，非零且支撑于真开子集。令 $b_{N}=\chi \sin (N s)$ ，并设
$$h_{N}(U, V)=h_{0}\left(e^{\tau_{N} b_{N} Z} U, V\right), \quad G_{N}=g_{B}+h_{N} .$$
$\operatorname{det} e^{\tau_{N} b_{N} Z}=1$ 使纤维面积形式固定，$H=A=0$ ；而
$$P_{v}=\frac{\tau_{N}}{2} d b_{N}(v) Z, \quad d_{\mathcal{E}, N}=\frac{\tau_{N}^{2}}{4}\left\|d b_{N}\right\|_{\infty}^{2} \frac{\int_{F} \operatorname{tr}\left(Z^{2}\right) d A_{h_{0}}}{\operatorname{Area}\left(F, h_{0}\right)} .$$
只看水平残差会得到 $O\left(\tau_{N}^{2} N^{2}\right)$ ，但完整垂直无迹块为
$$\left(h_{N}^{-1}\left(\operatorname{Ric}_{V V}+h_{N}\right)\right)^{0}=-\frac{\tau_{N}}{2}\left(\Delta_{B} b_{N}\right) Z .$$
混合块为 $O\left(\tau_{N} N\right)$ ，垂直纯迹内禀误差为 $O\left(\tau_{N}\right)$ ，于是固定背景下
$$\varepsilon_{N} \asymp \tau_{N} N^{2}, \quad d_{\mathcal{E}, N} \asymp \tau_{N}^{2} N^{2} .$$
取 $\tau_{N}=N^{-2-\alpha} 、 \alpha>0$ ，有 $\varepsilon_{N} \asymp N^{-\alpha}$ ，而 $d_{\mathcal{E}, N} / \varepsilon_{N} \asymp N^{-2-\alpha} \rightarrow 0$ 。所以该真实闭高频族没有制造能量振荡相对 Ricci 残差的放大。

最后，给定投影不为黎曼下沉时还会出现本章方程没有包含的自由度。取两个双曲曲面 $(F, h)$ 和 $(B, k)$ ，令
$$G=h+f(x)^{2} k, \quad f=e^{u}>0 .$$
研究投影到 $B$ 时，水平尺度随纤维点变化，因此投影通常不是黎曼下沉。对任一纤维TT 张量 $q$ ，翘曲乘积公式给
$$\begin{aligned}
\int_{F}\left\langle\left.\left(\operatorname{Ric}_{G}+G\right)\right|_{T F}, q\right\rangle_{h} d A_{h} & =-2 \int_{F}\langle d u \otimes d u, q\rangle_{h} d A_{h} \\
\int_{F} f^{2}\left\langle\left.\left(\operatorname{Ric}_{G}+G\right)\right|_{T F}, q\right\rangle_{h} d A_{h} & =2 \int_{F}\langle d f \otimes d f, q\rangle_{h} d A_{h}
\end{aligned}$$
两种权重不可混用。沿 $q$ 的正或负特征方向选局部高频截断函数，可使两种二次配对分别具有任一符号，即使纤维 Teichmüller 参数恒定。它证明未经推导删去水平尺度，就不能把垂直 TT 方程称为无源 WP 调和方程。这族一般度量不是 Einstein 反例；在这一简单 warped 形式内，精确 Einstein 已迫使 $f$ 常数。

\section*{8.8 固定双曲乘积排除另一类下沉反例}

定理8．10（乘积源上的任意曲面下沉）。设 $(E, G)=\left(\Sigma_{p}, g_{p}\right) \times\left(\Sigma_{q}, g_{q}\right), p, q \geq 2$ ，两因子曲率同为 $-c<0$ 。其到闭定向曲面的任意黎曼下沉，若纤维连通、定向且亏格至少二，则交换因子后等于一个因子投影复合基底等距映射。

证明。Euler 数乘法性使基底也为高亏格曲面，记其群为 $\Gamma_{r}$ 。纤维丛给 $1 \rightarrow \Gamma_{F} \rightarrow \Gamma_{p} \times \Gamma_{q} \xrightarrow{\rho} \Gamma_{r} \rightarrow 1$ 。两个因子的像逐元素交换；闭高亏格曲面群中非阿贝尔子群的中心化子平凡。因此交换因子后 $\rho(\gamma, \delta)=\rho_{1}(\gamma)$ ，且 $\Gamma_{F}=\operatorname{ker} \rho_{1} \times \Gamma_{q}$ 。再次使用中心化子性质使 ker $\rho_{1}=1$ ，故 $p=r$ 。每个切片映射 $f_{y}: \Sigma_{p} \rightarrow B$ 诱导群同构，因此度数为$\pm 1$ 。

乘积任意截面曲率至少 $-c$ ，O＇Neill 水平公式给 $K_{B} \geq-c$ ，故 Gauss－Bonnet 给$\operatorname{Area}(B) \geq \operatorname{Area}\left(\Sigma_{p}\right)$ 。另一方面，黎曼下沉不增加长度，所以每个 $f_{y}$ 的两个奇异值至多一；结合其度数，面积公式给反向不等式。全部取等号使两个奇异值处处为一，切片切空间因而等于水平空间。投影沿第二因子恒定，第一因子到基底为度数绝对值一的局部等距，即全局等距。

有同曲率双曲乘积有限等距覆盖的源，也得到局部结论：先将拉回下沉的纤维连通分支取商，形成有限基底覆盖，再应用定理。这里不能把明确的有限乘积覆盖条件改成一般局部乘积商。

这也说明，非等模 Kodaira 全纯纤维化不能直接提供相反例子：若其负 Kähler－Einstein 度量使同一全纯投影成为真正的黎曼下沉，复纤维极小且 $\nabla J=0$ 给 $A=0$ ，于是上述刚性使其局部乘积。全纯性没有自动提供水平度量沿纤维下降的条件。

\section*{8.9 与 Teichmüller 有效方程的接口}

全局章节的式（10．8）已证明：非零 Dehn twist 幂的光滑内部等变 WP 映射若满足带权强迫方程，则强迫项在长度梯度方向的投影必须抵消严格正的长度 Hessian 能量。本章（8．3）的连接源项和（8．38）的水平尺度源项，说明不能把完整四维 Einstein 方程未经推导写成无源 WP 方程。非 TT 形变、纤维共形因子、随参数变化的投影及规范项也必须同时处理。

因此，加权 collar 曲线能量及其端点位移泛函是可分析的有效模型；要用于排除四维 Einstein 度量，仍需严格证明完整方程的投影，并在同一权重和同一退化尺度下控制有符号源项。本文没有建立这一约化等价性。

\section*{第九章 面向任意源度量的谐和代表、Hodge 缺陷与最优目标}

上一章的精确方程需要指定投影为黎曼下沉。本章改变分析对象：固定投影的同伦类，针对每一个未知源度量重新求谐和代表。这样可以处理不适应原纤维化的度量，但付出的代价是水平非共形性、二阶导数与临界点；它们必须出现在方程中，不能由＂谐和＂一词隐去。

\section*{9.1 唯一谐和代表与无 Weyl 的 Bochner 缺陷}

设 $M$ 闭连通，$\pi: M \rightarrow B=\Sigma_{q}, q \geq 2$ ，且 $\pi_{*}: \pi_{1}(M) \rightarrow \pi_{1}(B)$ 满射。对任意源度量 $G$ 和双曲目标 $h\left(K_{h}=-1\right)$ ，负曲率目标的经典理论给同伦于 $\pi$ 的唯一谐和映射
$$f_{h}:(M, G) \longrightarrow(B, h), \quad \tau\left(f_{h}\right)=0 .$$
其秩二集开且稠密：若某开集秩一，则 Sampson 的秩一定理使整个像落在闭测地线中；若某开集秩零，唯一延拓使映射常值，两者都与非循环群满射冲突。 ${ }^{1}$ 这不排除临界点；秩二开稠密不能改成处处下沉。

现在设 $\operatorname{dim} M=4 、 \operatorname{Ric}_{G}=-c G 、 c>0$ 。记
$$B_{f}=\nabla d f, \quad t=|d f|^{2}=s_{1}^{2}+s_{2}^{2}, \quad \alpha=f^{*} \omega_{h}, \quad J=|\alpha|=s_{1} s_{2},$$
其中 $s_{1} \geq s_{2} \geq 0$ 为 $d f$ 的两个目标奇异值。 $t$ 和 $J^{2}$ 在临界点也光滑。二形式范数取$|\alpha|^{2}=\sum_{i<j} \alpha\left(e_{i}, e_{j}\right)^{2}$ 。

命题 9.1 （精确积分缺陷及等号）。有
$$\frac{1}{2} \Delta_{G} t=\left|B_{f}\right|^{2}-c t+2 J^{2}, \quad \int_{M}\left|B_{f}\right|^{2} d V_{G}+2 \int_{M} J^{2} d V_{G}=c \int_{M} t d V_{G} .$$
因而
$$0<\mathcal{R}(G, h):=\frac{2 \int J^{2} d V_{G}}{c \int t d V_{G}} \leq 1, \quad 1-\mathcal{R}=\frac{\int|\nabla d f|^{2} d V_{G}}{c \int|d f|^{2} d V_{G}}$$
若 $\mathcal{R}=1$ ，则 $d f$ 平行，$G$ 局部为两个曲率 $-c$ 的曲面乘积；$f:(M, G) \rightarrow(B, h / c)$ 是局部乘积的黎曼下沉。

证明．在奇异值标架中，目标曲率的有序指标 $(1,2) 、(2,1)$ 各贡献 $s_{1}^{2} s_{2}^{2}$ ，故 Bochner 目标项是 $2 J^{2}$ 。积分后得到公式。等号使 $\nabla d f=0$ ；由已有秩二点，$d f$ 处处秩二，其核与正交补均平行。源 Einstein 使两个局部因子曲率同为 $-c$ 。水平叶上的 $f^{*} h$ 是正定平行张量，非零常曲率曲面上只能为标量倍数 $a G_{\mathcal{H}}$ ；比较曲率得 $a=c$ 。 \(\square\)

\footnotetext{
${ }^{1}$ Eells－Sampson，Harmonic mappings of Riemannian manifolds（1964），https：／／doi．org／10．2307／2373037； Sampson，Some properties and applications of harmonic mappings（1978），Theorems 1、3、4、11，https： ／／www．numdam．org／article／ASENS＿1978＿4＿11＿2＿211＿0．pdf。
}

对于候选 $E_{D}$ 及 $f \simeq \pi$ ，等号会使 $f$ 成为闭纤维丛。群满射使纤维连通，群核仍为原曲面群。平行输运保持负曲率纤维度量，外单值变换有限，与原无限 Dehn twist外作用矛盾。因此每个假想 Einstein 度量都满足
$$0<\mathcal{R}(G, h)<1, \quad \text { 某个正则点有 } \frac{2 s_{1}^{2} s_{2}^{2}}{s_{1}^{2}+s_{2}^{2}}<c \text {. }$$
第二项由积分严格缺陷及正则集稠密得到。严格不等式尚不是统一正间隙。
水平非共形缺陷另为
$$t^{2}-4 J^{2}=\left(s_{1}^{2}-s_{2}^{2}\right)^{2} \geq 0, \quad \int\left(t^{2}-4 J^{2}\right)=\int t^{2}+2 \int\left|B_{f}\right|^{2}-2 c \int t$$
Bochner 恒等式不迫使它为零。一般谐和下沉在正则集只满足 $d f(N)=\operatorname{tr}_{\mathcal{H}} \nabla d f$ ；只有二维目标下的水平共形性才使右侧自动为零，从而纤维极小。

\section*{9.2 拉回面积形式：真实缺陷和条件平行性}

目标二维使
$$d \alpha=0, \quad \alpha \wedge \alpha=0 .$$
这些恒等式不包含余闭性。 $\nabla^{h} \omega_{h}=0$ 给
$$\begin{aligned}
\left(\nabla_{X} \alpha\right)(Y, Z) & =\omega_{h}\left(B_{f}(X, Y), d f(Z)\right)+\omega_{h}\left(d f(Y), B_{f}(X, Z)\right) \\
(\delta \alpha)(Y) & =-\omega_{h}(\tau(f), d f(Y))-\sum_{i} \omega_{h}\left(d f\left(e_{i}\right), B_{f}\left(e_{i}, Y\right)\right)
\end{aligned}$$
谐和性仅消去第二行第一项。逐项 Cauchy－Schwarz 给 $|\nabla \alpha|^{2} \leq t\left|B_{f}\right|^{2} 、|\delta \alpha|^{2} \leq t\left|B_{f}\right|^{2}$ ，并未令误差消失。

命题9．2（闭 Einstein 乘积中的非余闭拉回）。存在闭负 Einstein 四流形上的谐和下沉，诱导基本群满射、具有闭曲面群核，但其拉回目标面积形式既非余闭也非常长度。

证明．取 $(M, G)=\left(\Sigma_{q}, g_{0}\right) \times\left(\Sigma_{p}, k\right)$ ，两因子曲率均为 -1 。在第一曲面取与 $g_{0}$ 不同的标记双曲结构 $h$ 。恒等同伦类的谐和映射 $u:\left(\Sigma_{q}, g_{0}\right) \rightarrow\left(\Sigma_{q}, h\right)$ 是保向微分同胚，且不共形。令 $f=u \circ \mathrm{pr}_{1}$ ，则
$$\alpha=J_{u} \operatorname{pr}_{1}^{*} \omega_{g_{0}}, \quad \delta_{G} \alpha=-\iota_{\nabla J_{u}} \operatorname{pr}_{1}^{*} \omega_{g_{0}} .$$
若 $J_{u}$ 常数，由相等双曲面积得 $J_{u}=1$ 。对曲面谐和映射写全纯、反全纯能量密度 $\mathcal{H}, \mathcal{L}$ ，有 $J_{u}=\mathcal{H}-\mathcal{L} 、 \Delta_{g_{0}} \log \mathcal{H}=2\left(J_{u}-1\right)$ 。所以 $\mathcal{H}, \mathcal{L}$ 都常数。Hopf 二次微分的范数平方为 $\mathcal{H} \mathcal{L}$ ；非零二次微分必有零点，故 $\mathcal{L}=0$ ，矛盾。因此 $J_{u}$ 非常数。 \(\square\)

例子可以通过另选 $h=g_{0}$ 变成共形投影，所以它只排除任意给定目标下的自动共形或自动余闭推论；候选 $E_{D}$ 的无限外单值变换也未被保留。

取非负 Hodge Laplacian $\Delta_{d}=d \delta+\delta d$ ，Einstein 四维二形式的 Weitzenböck 公式为
$$\Delta_{d} \alpha=\nabla^{*} \nabla \alpha-\frac{4 c}{3} \alpha-2 W(\alpha), \quad \int|\delta \alpha|^{2}=\int\left(|\nabla \alpha|^{2}-\frac{4 c}{3} J^{2}-2 W(\alpha, \alpha)\right) .$$
$W$ 在这里是 $\Lambda^{2}$ 上的曲率算子。正则集若水平截面曲率为 $K_{\mathcal{H}}$ ，则 $W(\alpha, \alpha)=\left(K_{\mathcal{H}}+\right.$ $c / 3) J^{2}$ ，积分被积项可写为 $|\nabla \alpha|^{2}-2\left(c+K_{\mathcal{H}}\right) J^{2}$ 。因此从 $d f$ 转向面积形式重新引入了源 Weyl 控制。

也没有仅由谐和二阶数据得到的严格吸收系数。取点态数据 $d f\left(e_{1}\right)=u_{1} 、 d f\left(e_{2}\right)=$ $u_{2}$ 、其余为零，$B_{f}^{1}=0 、 B_{f}^{2}=\operatorname{diag}(3,-1,-1,-1)$ 。虽然 $\operatorname{tr} B_{f}=0$ ，却有 $|\delta \alpha|^{2}=9$ 、 $|\nabla \alpha|^{2}=3$ 。这是局部 jet 的代数反例，未声称实现为某闭 Einstein 映射；足以排除仅凭该点态代数推出 $|\delta \alpha|^{2} \leq \theta|\nabla \alpha|^{2} 、 \theta<1$ 。

命题 $\mathbf{9 . 3}$（余闭性与方向 Weyl 条件）。若 $f$ 有秩二点，且 $\delta \alpha=0 、 W(\alpha, \alpha) \leq-2 c|\alpha|^{2} / 3$处处成立，则 $\alpha$ 平行、无零点，$G$ 局部为两曲面乘积。若 $f_{*}$ 满射且群核为闭高亏格曲面群，则该纤维丛的外单值变换有限。

证明。式（9．6）右侧为非负项之和，故 $\nabla \alpha=0$ 。其非零秩处处保持，核与正交补平行，结论随即成立。由适当下沉与群满射得到连通纤维，水平度量下降为目标上的某个度量，平行输运属于纤维有限等距群。 \(\square\)

单独余闭只使正则集上 $\operatorname{ker} \alpha$ 与 $\operatorname{ker}(* \alpha)$ 都可积。以 $N_{\mathcal{V}}$ 和 $N_{\mathcal{H}}$ 表示两分布的未归一化平均曲率，则
$$N_{\mathcal{V}}=\nabla_{\mathcal{H}} \log J, \quad N_{\mathcal{H}}=\nabla_{\mathcal{V}} \log J .$$
进一步 $J$ 为正常数时，$(\alpha \pm * \alpha) / J$ 为常长度闭二形式，给相反定向的 almost－Kähler结构；尚未得到可积复结构，也未得到水平度量下降。对 $E_{D}$ ，若 $\delta \alpha=0$ ，上述平行性判据要求某正则点 $K_{\mathcal{H}}>-c$ ，否则与无限外单值变换矛盾。

\section*{9．3 Hodge 投影、Euler 配对与杯积的准确作用}

\section*{9．3．1 Hodge 投影不保持逐点可分解性}

下面给出闭 Einstein 几何上的明确例子，而不只用上同调平方为零的逻辑区分。在双曲乘积上，取两因子的非零谐和一形式 $\eta_{i}$ ，置 $\theta_{i}=* \eta_{i} 、 m_{i}=\operatorname{Area}\left(\Sigma_{i}\right)^{-1} \int\left|\eta_{i}\right|^{2}$ 。省略拉回记号，令
$$\begin{aligned}
& \beta=\left(\eta_{1}-m_{1} \theta_{2}\right) \wedge\left(\theta_{1} / m_{1}+\eta_{2}\right), \\
& \gamma=\omega_{1}+m_{1} m_{2} \omega_{2}+\eta_{1} \wedge \eta_{2}+\theta_{1} \wedge \theta_{2} .
\end{aligned}$$
$\beta$ 闭且简单，而其 Hodge 投影恰为 $\gamma$ ：各因子顶维项的投影把系数取平均，混合项已经谐和。然而
$$\gamma \wedge \gamma=2\left(m_{1} m_{2}-\left|\eta_{1}\right|^{2}\left|\eta_{2}\right|^{2}\right) d V_{G}$$
积分为零，却不处处为零，因为高亏格曲面的非零谐和一形式有零点。这个例子允许$\beta$ 有零点，也未将其指认为候选投影的面积拉回；它精准展示的是 Hodge 投影这一操作不保留简单性。

\section*{9．3．2 候选 Euler 配对看不见正合误差}

对原候选丛 $\pi: E_{D} \rightarrow B$ ，固定 $V=\operatorname{ker} d \pi$ ，不能在另一个映射的临界点把它改成$\operatorname{ker} d f$ 。取 $u_{B} \in H^{2}(B ; \mathbb{R})$ 使积分为一，令 $b=\pi^{*} u_{B}$ ，则
$$b^{2}=0, \quad\left\langle b \smile e(V),\left[E_{D}\right]\right\rangle=\chi(F) \neq 0 .$$
对任意 $G$ ，记 $\beta=\mathrm{H}_{G} b 、 \xi=\mathrm{H}_{G} e(V)$ 。若 $f \simeq \pi$ ，令 $A_{h}=\operatorname{Area}(B, h)$ ，则
$$\alpha=A_{h} \beta+d \nu, \quad \int \alpha \wedge \xi=A_{h} \chi(F), \quad \delta \alpha=\delta d \nu, \quad\|\beta\|_{2}\|\xi\|_{2} \geq|\chi(F)| .$$
正合项在配对中消失，所以精确 Euler 配对并不控制 $\delta d \nu$ 。
这种缺口还能在同一个候选拓扑上实现，但须放弃 Einstein 条件：取保持纤维面积形式 $\mu$ 的 Dehn twist 代表；在原平坦丛的局部基底圆盘上，把水平提升改为 $X_{1}=\partial_{s}$ 、 $X_{2}=\partial_{t}+\rho(s, t) Y$ ，其中 $Y$ 为保持 $\mu$ 的垂直 Hamiltonian 场，$\rho$ 紧支撑。给垂直度量选固定面积形式 $\mu$ ，取连接度量。此时 $H=0$ ，投影为谐和黎曼下沉；但
$$\Omega=\left(\partial_{s} \rho\right) Y, \quad *_{G} \pi^{*} \omega_{h}=\mu_{\mathcal{V}}, \quad d \mu_{\mathcal{V}}\left(X_{1}, X_{2}, U\right)=-\mu(\Omega, U) .$$
所以在 $\Omega \neq 0$ 处 $\delta \pi^{*} \omega_{h} \neq 0$ ，而 Euler 配对仍成立。

\section*{9．3．3 基底杯积子代数的定量非谐和乘积}

取 $H^{1}(B ; \mathbb{R})$ 的辛基 $v_{1}, \ldots, v_{2 q}$ ，使 $v_{i} \smile v_{j}=J_{i j} u_{B}$ ，其中 $J$ 由 $q$ 个标准 $2 \times 2$ 反对称块组成。令 $\theta_{i}=\mathrm{H}_{G}\left(\pi^{*} v_{i}\right) 、 R_{i j}=\theta_{i} \wedge \theta_{j}-J_{i j} \beta$ 。每个 $R_{i j}$ 闭且正合，并有
$$\sum_{i<j}\left|R_{i j}\right|^{2} \geq(q-1)|\beta|^{2} .$$
证明只需固定源二平面：令 $x_{i}=\theta_{i}\left(e_{\mu}\right) 、 y_{i}=\theta_{i}\left(e_{\nu}\right)$ ，则 $z=x \wedge y$ 简单；标准辛形式 $J$的平方范数为 $q$ 、comass 为一，所以对 $r=\beta\left(e_{\mu}, e_{\nu}\right),|z-r J|^{2} \geq(|z|-|r|)^{2}+(q-1) r^{2}$ 。对源各二平面求和即得。

令 $\lambda_{\mathrm{ex}, 2}(G)>0$ 为非零正合二形式上的首个 Hodge 特征值，便有
$$\sum_{i<j}\left\|\delta\left(\theta_{i} \wedge \theta_{j}\right)\right\|_{2}^{2} \geq(q-1) \lambda_{\mathrm{ex}, 2}(G)\|\beta\|_{2}^{2} \geq \frac{(q-1) \lambda_{\mathrm{ex}, 2}(G) \chi(F)^{2}}{\|\xi\|_{2}^{2}}>0 .$$
它量化了谐和代表不能逐点实现整个基底杯积代数的程度。该不等式也成立于真正的负 Einstein 曲面乘积，所以它不是 Einstein 不存在性障碍；Einstein 不要求谐和形式的楔积仍谐和。几何形式性的经典背景见 Kotschick。 ${ }^{2}$

\section*{9.4 谐和一形式完整测试：共形缺陷与盲点}

对谐和 $f:(M, G) \rightarrow(B, h)$ ，定义目标上的对称逆变张量
$$C_{f}=\sum_{i} d f\left(e_{i}\right) \otimes d f\left(e_{i}\right), \quad S_{f}=C_{f}-\frac{1}{2}\left(\operatorname{tr}_{h} C_{f}\right) h^{-1} .$$
$\left|S_{f}\right|^{2}=\left(s_{1}^{2}-s_{2}^{2}\right)^{2} / 2 ; S_{f}=0$ 正是水平弱共形。

\footnotetext{
${ }^{2}$ D．Kotschick，On products of harmonic forms，https：／／arxiv．org／pdf／math／0004009。式（9．9）的证明已在正文独立给出，不据此认定首创性。
}

命题 9.4 （一对共轭一形式的精确测试）。对目标非零实谐和一形式 $\vartheta$ ，有
$$\begin{aligned}
& \delta_{G} f^{*} \vartheta=-\left\langle\nabla^{h} \vartheta, S_{f}\right\rangle \\
& D_{\vartheta}(f):=\left|\delta_{G} f^{*} \vartheta\right|^{2}+\left|\delta_{G} f^{*}\left({ }^{*} h \vartheta\right)\right|^{2}=\left(\left|\nabla^{h} \vartheta\right|^{2} \circ f\right)\left|S_{f}\right|^{2} .
\end{aligned}$$
若 $f$ 的秩二集稠密，则这两个拉回形式同时谐和当且仅当 $S_{f} \equiv 0$ 。
证明．$\nabla \vartheta$ 因闭且余闭而为无迹对称二张量；链式求导给第一式。其与 $\nabla(* \vartheta)$ 在目标二维无迹对称张量空间中等范数、正交，故给第二式。非零 $\vartheta$ 的 $\nabla \vartheta$ 不可能在开集恒零，否则负曲率使平行一形式为零，再由唯一延拓全局为零。于是其非零集开稠密；用$f$ 正则集上的开映射性，再连续延拓，得到最后断言。 \(\square\)

对候选假想 Einstein 度量，若 $D_{\vartheta}$ 在某开集为零，缩小到正则子开集可得水平共形，从而 Wood 给局部正交可积复结构，与候选的无 Hermitian 开集条件冲突。故
$$\left\{D_{\vartheta}=0\right\} \text { 闭且无内点, } \quad \int_{E_{D}} D_{\vartheta} d V_{G}>0 \quad(\vartheta \neq 0) \text {. }$$
对固定的源度量、目标度量及映射，这个积分定义目标谐和空间上的正定二次型，其最小特征值为正。该有限维结论没有给出统一于未知源度量的常数。

\section*{9．4．1 所有测试的公共零点恰是超椭圆分歧点}

取 $L^{2}(h)$ 正交单位基 $\vartheta_{1}, \ldots, \vartheta_{2 q}$ ，定义
$$W_{h}(y)=\sum_{j=1}^{2 q}\left|\nabla^{h} \vartheta_{j}(y)\right|^{2}, \quad \mathcal{D}_{h}(f)=\sum_{j} D_{\vartheta_{j}}(f)=\left(W_{h} \circ f\right)\left|S_{f}\right|^{2} .$$
$W_{h}$ 与所选正交基无关；这里的 $W_{h}$ 是目标测试权重，不是源 Weyl 张量。
命题9．5（公共零点的分类与阶数）。 $W_{h}(y)=0$ 当且仅当 $B$ 是超椭圆黎曼曲面，且 $y$是其二重球面映射的分歧点。超椭圆时共 $2 q+2$ 个零点，并且在每个零点 $y_{0}$ 附近
$$c_{h} d_{h}\left(y, y_{0}\right)^{2} \leq W_{h}(y) \leq C_{h} d_{h}\left(y, y_{0}\right)^{2} .$$
证明。超椭圆对合 $\iota$ 是 $h$ 的等距变换，在谐和一形式上作用为 $-I$ ；否则不变全纯一形式会下降到球面。在固定点 $d \iota=-I$ ，二阶协变张量的拉回却作用为 $+I$ ，故 $\nabla \vartheta=0$ 。

反之，若所有 $\nabla \vartheta(y)=0$ ，则任何在 $y$ 消失的全纯一形式至少有二阶零点，即$H^{0}\left(K_{B}-y\right)=H^{0}\left(K_{B}-2 y\right)$ 。因 $q \geq 2, h^{0}(y)=1$ ；Riemann－Roch 给 $q-1=q-3+h^{0}(2 y)$ ，故 $h^{0}(2 y)=2$ 。存在仅在 $y$ 有二阶极点的非恒定亚纯函数，它给次数二球面映射，$y$ 为分歧点。

上界由全部梯度在 $y_{0}$ 消失及光滑性得到。下界使用超椭圆模型 $v^{2}=\prod_{k=1}^{2 q+2}\left(x-a_{k}\right)$ ，使所考察分歧点在有限值 $a_{1}$ 上。全纯一形式 $\alpha=\left(x-a_{1}\right) d x / v$ 在该点恰有二阶零点。用 $x-a_{1}=z^{2}$ ，有 $\alpha=\left(b z^{2}+O\left(z^{4}\right)\right) d z 、 b \neq 0$ ，因而 $\nabla \alpha=\left(2 b z+O\left(|z|^{2}\right)\right) d z \otimes d z$ 。将其真实部展开到正交基并用 Cauchy－Schwarz，即得下界。 ${ }^{3}$ \(\square\)

\footnotetext{
${ }^{3}$ Riemann－Roch、超椭圆模型及其全纯一形式的基础证明可核对 McMullen 的作者讲义 Riemann Surfaces， §§9、11、13，https：／／people．math．harvard．edu／～ctm／math213b／home／course／course．pdf。这里列出完整推导，不把经典曲面工具记为新的 Einstein 理论。
}

固定非超椭圆目标时 $\kappa_{h}=\min _{B} W_{h}>0$ ，故
$$\int_{M}\left|S_{f}\right|^{2} d V_{G} \leq \kappa_{h}^{-1} \int_{M} \mathcal{D}_{h}(f) d V_{G}$$
亏格 $q \geq 3$ 可选这样的目标；亏格二的所有结构均超椭圆，在六个分歧点有公共盲点。即使目标有统一注入半径下界，也不自动有统一 $\kappa_{h}$ ：取光滑非超椭圆族 $h_{t}$ 趋近光滑超椭圆 $h_{0}$ ，则谐和正交基可光滑选取，$W_{h_{t}} \rightarrow W_{h_{0}}$ ，在一个极限分歧点有 $0<\kappa_{h_{t}} \leq W_{h_{t}}\left(y_{0}\right) \rightarrow 0$ 。这里没有夹断闭测地线。

\section*{9．4．2 精确 Einstein 几何上的正定缺陷也能趋零}

固定双曲目标 $(B, h)$ 与纤维 $(F, k)$ ，取 $g_{t} \rightarrow h$ 的光滑双曲族，非零参数时标记Teichmüller 类不同。令 $G_{t}=g_{t} \oplus k$ ，则 $\operatorname{Ric}_{G_{t}}=-G_{t}$ 。恒等映射处的谐和 Jacobi 二次型为 $\int_{B}\left(|\nabla V|^{2}+|V|^{2}\right) d A_{h}$ ，无核。隐函数定理给谐和微分同胚 $u_{t}:\left(B, g_{t}\right) \rightarrow(B, h)$ ，且 $u_{t} \rightarrow \mathrm{id}$ 光滑。取 $f_{t}=u_{t} \circ \mathrm{pr}_{B}$ ，定义 $Q_{t}(\vartheta)=\int D_{\vartheta}\left(f_{t}\right) d V_{G_{t}}$ 。非零 $t$ 下 $u_{t}$ 不共形，式（9．11）与目标梯度非零集稠密给 $Q_{t}$ 正定；但 $S_{f_{t}} \rightarrow 0$ ，因此
$$0<\min _{\|\vartheta\|_{L^{2}(h)}=1} Q_{t}(\vartheta) \leq \max _{\|\vartheta\|_{L^{2}(h)}=1} Q_{t}(\vartheta) \longrightarrow 0 .$$
该族源拓扑、Einstein 常数、体积都固定，曲率有界、注入半径正、直径有界，且光滑收敛。这排除＂正定缺陷加一般 Einstein 紧性必有统一间隙＂的通用推论。它不保留$E_{D}$ 的拓扑；候选特有紧性或零极限排除仍需另证。

源一形式 Bochner 公式没有补上缺口。对闭拉回 $\beta=f^{*} \vartheta$ ，Hodge 分解为 $\beta=$ $\gamma+d u, \gamma$ 谐和， $\int u=0$ 。在 $\operatorname{Ric}_{G}=-c G$ 下，交叉项消失，得到
$$\|\delta \beta\|_{2}^{2}=\left\|\Delta_{0} u\right\|_{2}^{2}=\|\nabla d u\|_{2}^{2}-c\|d u\|_{2}^{2} \geq \lambda_{1}(G)\|d u\|_{2}^{2}, \quad \Delta_{0}=\delta d \geq 0 .$$
它只度量拉回形式与其谐和代表之间的正合误差，不强迫 $d u=0$ 。

\section*{9.5 最优目标确实存在，但最优不等于共形}

\section*{9．5．1 经典最优目标定理及可检查的 proper 性证明}

定理9．6（固定源的唯一最优标记目标；经典结果）。对任意固定闭连通黎曼源（ $M, G$ ）及基本群满射 $\pi: M \rightarrow \Sigma_{q}, q \geq 2$ ，谐和能量
$$\mathcal{E}_{G}([h])=\frac{1}{2} \int_{M}\left|d f_{h}\right|_{G, h}^{2} d V_{G}$$
在标记 Teichmüller 空间上 proper，达到唯一极小点。
这是 Yamada 的 proper 性和 WP 严格凸性理论；严格凸性采用 Kim－Wan－Zhang的修正证明。 ${ }^{4}$ 较早记录中＂最优目标可能未取得＂的缺口在固定源层面据此删除，不能继续作为未知问题保留。

\footnotetext{
${ }^{4}$ Yamada，Weil－Petersson convexity of the energy functional on classical and universal Teichmüller spaces， JDG 51 （1999），https：／／doi．org／10．4310／jdg／1214425025。本整理未取得其全文。实际读取 Kim－Wan－Zhang， Corollary 0．4、Theorem 0．8、§3，https：／／arxiv．org／pdf／1809．00255；该文指出早期凸性证明中的 Schwarz 不等式系数问题，并给修正证明。
}

下面记录一个直接核验 proper 性的方法。固定 $K \geq 0$ 使 $\operatorname{Ric}_{G} \geq-K G$ ，对 $t_{h}=$ $\left|d f_{h}\right|^{2}$ ，Bochner 给 $\Delta_{G} t_{h} \geq-2 K t_{h}$ 。令 $P_{s}=e^{s \Delta_{G}}$ ，固定源热核为 $p_{s}^{G}$ ，则 $\partial_{s}\left(e^{2 K s} P_{s} t_{h}\right) \geq 0$ 。取 $s=1$ ，得到
$$\left\|d f_{h}\right\|_{\infty}^{2} \leq 2 e^{2 K}\left\|p_{1}^{G}\right\|_{\infty} \mathcal{E}_{G}([h])=: C_{G} \mathcal{E}_{G}([h]) .$$
$C_{G}$ 与目标退化无关，但依赖源几何。
取有限组填充目标曲线 $\gamma_{a}$ 。由基本群满射，可选固定源环路 $c_{a}$ 映到相应自由同伦类。于是
$$\ell_{h}\left(\gamma_{a}\right) \leq \operatorname{Length}_{G}\left(c_{a}\right) \sqrt{C_{G} \mathcal{E}_{G}([h])} .$$
填充曲线长度和在标记 Teichmüller 空间上 proper：裤曲线及横截曲线的长度上界给裤长上下界及扭转有界。不能先模去映射类群，将无界扭转消失于记号中。

谐和映射 Jacobi 二次型为
$$Q_{h}(V)=\int_{M}\left[|\nabla V|^{2}+\sum_{i}\left(\left|d f_{h}\left(e_{i}\right)\right|^{2}|V|^{2}-\left\langle d f_{h}\left(e_{i}\right), V\right\rangle^{2}\right)\right] d V_{G} .$$
零核以外的 $V$ 若使它为零，则 $V$ 平行且所有 $d f_{h}\left(e_{i}\right)$ 共线，像落在双曲测地线中，与群满射冲突。因此 Jacobi 无核，隐函数定理给能量光滑。能量次水平集由填充长度控制落在紧集，又是闭的，故 proper。达到极小之后，经典 WP 严格凸性及内部测地线连通性给唯一性。

极小的一阶条件仅为
$$\frac{1}{2} \int_{M} \operatorname{tr}_{G} f_{h}^{*} q d V_{G}=0 \quad \text { 对全部目标 } \mathrm{TT} \text { 张量 } q \text {. }$$
在映射为下沉时，余面积公式使它等于 $\frac{1}{2} \int_{B}\left\langle q, \int_{f^{-1}(b)}\left(d f d f^{*}\right) / J d A_{G}\right\rangle_{h} d A_{h}$ 。这是纤维积分后、再作有限维 TT 测试的约束，不是逐点纯迹方程。

\section*{9．5．2 真实闭近 Einstein 族：目标唯一最优而投影不共形}

命题9．7（最优目标的几何反向检验）。存在闭四维光滑度量族 $G_{t} \rightarrow G_{0}, G_{0}$ 为负 Einstein 曲面乘积，且 $\left\|\operatorname{Ric}_{G_{t}}+G_{t}\right\|_{\mathrm{op}, \infty}=O(|t|)$ 。对所有充分小非零 $t$ ，投影同伦类的唯一最优目标谐和代表处处秩二，却不水平共形；$G_{t}$ 本身不是 Einstein。

证明．固定曲率 -1 的 $(B, h),(F, k)$ ，取非零特征函数 $-\Delta_{h} \psi=\lambda \psi 、 \lambda>0$ 。令
$$u_{t}=1+t \psi, \quad T_{t}=\nabla_{h}^{2} u_{t}-\left(\Delta_{h} u_{t}-u_{t}\right) h, \quad L_{t}=h^{-1} T_{t} .$$
因 $\operatorname{Ric}_{h}=-h$ ，
$$\operatorname{div}_{h} T_{t}=0, \quad \operatorname{tr}_{h} T_{t}=\left(2-\Delta_{h}\right) u_{t}, \quad T_{t}^{0}=t\left(\nabla_{h}^{2} \psi\right)^{0} .$$
对于任何 TT 张量 $q$ ，分部积分给 $\int_{B}\left\langle T_{t}, q\right\rangle_{h}=0$ 。 $T_{0}=h$ ，故小参数下 $L_{t}$ 正定。置
$$a_{t}=\sqrt{\operatorname{det} L_{t}}, \quad b_{t}(X, Y)=h\left(a_{t} L_{t}^{-1} X, Y\right), \quad G_{t}=b_{t} \oplus a_{t} k .$$

二维行列式给 $\operatorname{det}\left(h^{-1} b_{t}\right)=1 、 a_{t} b_{t}^{i j}=T_{t}^{i j} 、 d V_{G_{t}}=a_{t} d A_{h} d A_{k}$ 。因此投影到目标 $h$ 的张力为
$$\tau_{G_{t}, h}(\pi)^{j}=a_{t}^{-1} \nabla_{i}^{h}\left(a_{t} b_{t}^{i j}\right)=a_{t}^{-1} \nabla_{i}^{h} T_{t}^{i j}=0 .$$
纤维体积变化已进入因子 $a_{t}$ 。它是唯一谐和代表，且
$$\left.d \mathcal{E}_{G_{t}}\right|_{[h]}(q)=\frac{1}{2} \operatorname{Area}(F, k) \int_{B}\left\langle T_{t}, q\right\rangle_{h} d A_{h}=0$$
由定理9．6，$[h]$ 是唯一全局极小标记目标。
若投影水平共形，则 $b_{t}$ 为 $h$ 的标量倍数，即 $T_{t}^{0}=0$ 。这会使 $\nabla_{h} \psi$ 成为闭高亏格曲面的共形向量场，迫使 $\psi$ 常数，矛盾。

构造光滑依赖参数，所以完整 Ricci 最大残差为 $O(|t|)$ 。又 $a_{t}=1+\frac{1}{2}(\lambda+2) t \psi+$ $O\left(t^{2}\right)$ ，对小非零参数非常数。若 $G_{t}$ Einstein，将其写作 $b_{t}+w_{t}^{2} k 、 w_{t}=\sqrt{a_{t}}$ ，水平无迹 Ricci 方程给 $\left(\nabla_{b_{t}}^{2} w_{t}\right)^{0}=0$ 。同样的共形向量场论证迫使 $a_{t}$ 常数，矛盾。 \(\square\)

此构造同时实现了正定推前张量、散度约束、所有 TT 驻点条件、真正谐和映射和真正全局最优目标，故比抽象的积分抵消矩阵例子更强。它的边界同样明确：非零参数的源不精确 Einstein，且底层乘积流形承载 $G_{0}$ ；不能据此否定＂精确 Einstein 加候选特有拓扑＂可能带来的额外刚性。

\section*{9.6 现有工具之间的实际接口}

这套方法已为任意假想源 Einstein 度量提供唯一谐和代表，以及唯一最优标记目标。它们消除了＂是否必须先把原投影改成黎曼下沉＂的入门障碍，但没有消除共形缺陷 $S_{f}$ 、面积拉回余闭缺陷 $\delta f^{*} \omega_{h}$ 或临界点。

能够完成的条件接口是：$\nabla d f=0$ 给乘积；余闭面积形式加明确方向 Weyl 不等式给平行性；一对共轭目标谐和一形式的拉回同时谐和给水平弱共形。候选拓扑则要求这些缺陷不能在某些开集中消失。尚未建立的是一条源自完整 Einstein 方程、适用于候选上全部度量的反向估计，使这种必要非零性与独立上界发生矛盾。各处固定几何的正定性、目标的最优性和局部闭合公式，都不能替代这个接口。

\section*{第十章 全局候选的定量约束与有效方程的边界}

曲面丛路线已经有全局最大范数近似构造，但尚未排除所有 Einstein 度量。扩展图流形路线具有相反优势：已有完整的 Einstein 不存在性定理，却尚缺所需的 Ricci 最大误差趋零构造。把这两类候选的长处直接拼接，并不会自动产生一个同时具有两种性质的流形。

\section*{10.1 扩展图四流形：已知不存在性与未知近似性}

本节取闭、连通、定向的 Frigerio－Lafont－Sisto 型扩展图四流形 $M$ ，有非平凡尖点环面粘接，且含至少一个纯实双曲四维块。Di Cerbo 的结果给出
$$\tau(M)=0, \quad \chi(M)>0, \quad \mathbb{Z}^{2} \subset \pi_{1}(M), \quad V_{*}:=\inf _{\operatorname{Ric}_{g} \geq-g} \operatorname{Vol}_{g}(M)=12 \pi^{2} \chi(M),$$
并排除 $M$ 上的所有 Einstein 度量。 ${ }^{1}$
命题10．1（任意近似输入的体积与 Weyl 分布）。对上述固定 $M$ ，若某度量满足 $\delta=$ $\|\operatorname{Ric}+g\|_{\mathrm{op}, \infty}<1 / 3$ ，则
$$\begin{aligned}
\frac{V_{*}}{(1+\delta)^{2}} \leq V:=\operatorname{Vol}_{g}(M) & \leq \frac{V_{*}}{(1-\delta)^{2}} \\
\frac{1}{V} \int_{M}|W|^{2} d V_{g} & \leq \frac{8}{3} \delta \\
\|W\|_{\infty} & \geq \frac{1-3 \delta}{\sqrt{3}}
\end{aligned}$$
这里 $|W|^{2}=\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}$ 为曲率算子范数。
证明．因为 $\operatorname{Ric}_{g} \geq-(1+\delta) g$ ，度量 $(1+\delta) g$ 可用于（10．1）的下确界，给出左侧体积界。四维 Chern－Gauss－Bonnet 公式和命题1．1后的点态箱体最小值给
$$8 \pi^{2} \chi(M)=\int_{M}\left(|W|^{2}+\frac{s^{2}}{24}-\frac{|E|^{2}}{2}\right) d V_{g} \geq \int_{M}|W|^{2} d V_{g}+\frac{2}{3}(1-\delta)^{2} V$$
用 $8 \pi^{2} \chi=2 V_{*} / 3$ ，先得右侧体积界，再以 $V_{*} \leq(1+\delta)^{2} V$ 得（10．3）。
对于任意二维平面 $\Pi$ ，曲率分解及四维无迹算子的最大特征值估计给
$$K_{g}(\Pi) \leq-\frac{1}{3}+\delta+\frac{|W|}{\sqrt{3}} .$$
Ricci 缺陷对这个表达式的贡献至多为 $\delta$ ：在适应 $\Pi$ 的标架中，它是四个对角缺陷按系数（1／3，1／3，－1／6，－1／6）的线性组合。若（10．4）失败，所有截面曲率严格负，与$\mathbb{Z}^{2} \subset \pi_{1}(M)$ 及 Preissmann 定理矛盾。 \(\square\)

\footnotetext{
${ }^{1}$ L．F．Di Cerbo，Extended Graph 4－Manifolds，and Einstein Metrics，arXiv：2106．13279，Lemmas 8－9、Theo－ rem 12，https：／／arxiv．org／pdf／2106．13279。原文的最小 Ricci 体积采用 Ric $\geq-3 g$ ；换到本稿 Ric $\geq-g$ 后，四维体积乘以 9 。纯双曲闭流形没有上述非平凡粘接，不在本节候选范围内。
}

以上常数不依赖块数或 Euler 示性数，因而也适用于维数固定而拓扑变化的序列。拓扑变化时只能直接断言归一平均趋零；固定 $M$ 时，体积窗口才进一步给总 Weyl 能量趋零。

这个结论同时要求平均 Weyl 能量趋零和最大 Weyl 幅度保持正下界。它把任何可能的反例构造限制为必然有曲率集中的形式，却没有排除曲率集中。对任意 $t>0$ ，Chebyshev 不等式给
$$\frac{\operatorname{Vol}_{g}\{|W| \geq t\}}{V} \leq \frac{8 \delta}{3 t^{2}} .$$
当 $\delta<1 / 6$ 时，集合 $\{|W| \geq 1 /(2 \sqrt{3})\}$ 非空，其相对体积至多为 $32 \delta$ 。这里是非空集合的体积上界，不是其体积正下界。

命题10．2（附加导数控制下的直径代价）。若另有 $\delta<1 / 6 、\|\nabla W\|_{\infty} \leq L 、 \operatorname{diam}_{g} M \leq$ $D$ ，令
$$r=\min \left\{D, 1,(4 \sqrt{3} L)^{-1}\right\},$$
其中 $L=0$ 时最后一项取 $+\infty$ 。记 $v_{-7 / 18}(r)$ 为四维常截面曲率 $-7 / 18$ 模型的半径 $r$球体积，则
$$\delta \geq \frac{1}{128} \frac{v_{-7 / 18}(r)}{v_{-7 / 18}(D)} .$$
特别地，对固定 $L$ ，任何这样的 $\delta \rightarrow 0$ 序列必须满足
$$\operatorname{diam}_{g} M \geq \sqrt{\frac{2}{7}} \log \frac{1}{\delta}-C_{L}$$
（在 $\delta$ 充分小时）。
证明．在 $|W| \geq 1 /(2 \sqrt{3})$ 的点，以梯度界传播到半径 $r$ 的球，球内有 $|W| \geq 1 /(4 \sqrt{3})$ 。又 Ric $\geq-7 g / 6$ ，Bishop－Gromov 比较给
$$\frac{\operatorname{Vol} B(x, r)}{V} \geq \frac{v_{-7 / 18}(r)}{v_{-7 / 18}(D)} .$$
如果直径恰为 $D$ ，先用 $D+\epsilon$ 再取极限即可。与（10．3）合并，得到 $8 \delta / 3 \geq$ $\operatorname{Vol} B(x, r) /(48 V)$ ，即（10．5）。四维该模型球体积至多按 $e^{\sqrt{7 / 2} D}$ 增长；固定 $L$ 后先由（10．5）排除有界 $D$ ，再取固定 $r=\min \left\{1,(4 \sqrt{3} L)^{-1}\right\}$ ，得到（10．6）。 \(\square\)

没有注入半径假设进入这个论证，但 $\nabla W$ 的界是新增条件，不能从 Ricci 最大范数夹逼直接获得。已有有界截面曲率塌缩或最小体积逼近序列，也不自动具有$\|$ Ric $+g \|_{\infty} \rightarrow 0{ }^{2}$

\footnotetext{
${ }^{2}$ C．Connell，P．Suárez－Serrato，On higher graph manifolds，https：／／arxiv．org／abs／1208．4876，用于本节经典最小体积输入的来源链；此处未将其构造改称为 Ricci 最大范数近 Einstein 构造。
}

\section*{10．2 WP 长度下降排除无强迫的有效模型}

设 $(B, b)$ 闭、连通，$F$ 为亏格至少二的闭曲面，等变表示满足 $\operatorname{im} \rho=\left\langle D_{\alpha}^{k}\right\rangle, k \neq 0$ 。在 Teichmüller 空间内部，令 $f=\ell_{\alpha}$ 为被扭曲曲线的双曲长度。经典输入为 $f \circ D_{\alpha}^{k}=f$且其 Weil－Petersson Hessian 处处正定。 ${ }^{3}$

对光滑等变映射 $u: \widetilde{B} \rightarrow \mathcal{T}(F)$ 、基底正权 $w$ ，记
$$\tau_{w}(u)=\tau(u)+d u(\nabla \log w), \quad H_{u}=\sum_{i} \operatorname{Hess}_{\mathrm{WP}} f\left(d u\left(e_{i}\right), d u\left(e_{i}\right)\right) .$$
不变函数 $v=f \circ u$ 下降到 $B$ ，链式法则给
$$\operatorname{div}_{b}(w \nabla v)=w\left\{H_{u}+d f_{u}\left(\tau_{w}(u)\right)\right\} .$$
若 $\tau_{w}(u)=0$ ，在闭基底积分迫使 $H_{u}=0$ ，从而 $u$ 常值。但非零 Dehn twist 幂没有内部固定点，故这种映射不存在。目标不完备不影响这段局部微分与闭基底积分论证。

更精确地，$-\nabla f$ 的局部流给合法的等变变分，且
$$\left.\frac{d}{d s}\right|_{0} \frac{1}{2} \int_{B} w\left|d u_{s}\right|^{2} d V_{b}=-\int_{B} w H_{u} d V_{b}<0$$
每个内部映射都有严格下降方向。对位移函数 $F_{T}(x)=\frac{1}{2} d_{\mathrm{WP}}(x, T x)^{2}, T=D_{\alpha}^{k}$ ，沿连接 $x$ 与 $T x$ 的常速内部测地线 $\gamma$ ，同样有
$$d F_{T}(-\nabla f)=-\int_{0}^{1} \operatorname{Hess}_{\mathrm{WP}} f(\dot{\gamma}, \dot{\gamma}) d t<0$$
这里使用 WP 内部测地凸性的经典结果，而非在不完备空间上直接套用 Cartan－Hadamard 定理。

若真实有效方程是 $\tau_{w}(u)=R$ ，必要条件却变为
$$\int_{B} w d f_{u}(R) d V_{b}=-\int_{B} w H_{u} d V_{b}<0 .$$
这要求有符号的相对控制。例如若能证明 $d f_{u}(R) \geq-(1-\epsilon) H_{u}$ ，同一个 $\epsilon>0$ ，才会产生矛盾。一个绝对很小的源项仍可能抵消同步趋零的右端。任意四维 Einstein 度量尚未被证明能放人这个受控约化，水平与混合分量、非极小纤维及规范变化也会产生 $R$ 。因此无强迫模型的无解性，不能替代全局 Einstein 不存在性。

\footnotetext{
${ }^{3}$ M．Wolf，The Weil－Petersson Hessian of Length on Teichmüller Space，Theorem 1.1 及第1．2节，https： ／／arxiv．org／pdf／0902．0203；长度凸性的先行结果归于 Wolpert。
}

\section*{10.3 现有存在性定理的准确距离}

Jäckel 的有效稳定性定理已使阈值摆脱直径、体积上界和注入半径下界。所查第二版的 Theorem 1.1 在 $n \geq 4$ 下仍要求
$$\|\operatorname{Ric}(\bar{g})+(n-1) \bar{g}\|_{C^{0}},\|\operatorname{Ric}(\bar{g})+(n-1) \bar{g}\|_{L^{2}} \leq \epsilon,$$
以及 $\sec \leq-K<0$ 、薄部截面曲率严格等于 $-1 、\|\nabla \operatorname{Ric}\|_{\infty} \leq \Lambda$ 。阈值依赖 $n, \alpha, K, \Lambda$ ，结论是存在近旁负 Einstein 度量。 ${ }^{4}$ 该证明在薄部使用覆盖空间的局部原像计数与混合范数逆估计。它提供的是有明确附加结构的统一可解性机制；当前 Ricci 夹逼假设既没有给出这些结构，也没有给出替代控制。

本稿各路线最终指向同一解析要求：应在真正退化的几何中比较残差、逆算子、非线性项及障碍投影的相对尺度。但这个共同要求不是已经存在的一般定理。局部可修正性、特定构造族的失败或一个端点的体积间隙，都仍需额外论证才能触及原问题的全称量词。

\footnotetext{
${ }^{4}$ F．Jäckel，Effective stability of negatively curved Einstein metrics in dimensions at least 4， arXiv：2502．16692v2，Theorem 1．1，https：／／arxiv．org／html／2502．16692v2。本稿核查版本修订于2025年12 月29 日。
}
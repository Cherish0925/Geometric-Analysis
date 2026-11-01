---
source_file: 03_A03_全局拓扑兼容与反例闭合.pdf
converter: mathpix
format: mmd
---

\title{
主线三：近 Einstein 构造与全局拓扑的闭合
}

S0910A03｜图流形、曲面丛、全局存在性与 Yau26 的决定性接口

\author{
Qiushi Engine 科学续接稿
}

2026 年 9 月 16 日

\begin{abstract}
摘要
本主线不是第三项已经完成的重大突破，而是连接两条已有成果主线与原题的全局研究线。它同时保留两类互补对象：已知无 Einstein 但尚未构造任意紧 Ricci 夹逼的 extended graph 流形；记录已有近负 Einstein 输入但尚未排除全部 Einstein 度量的曲面丛与其他固定解消。第100步的相对 Chern－Gauss－Bonnet 预算、完整矩阵连接器、周边格点与长颈参数联动是直接起点。本稿将其整理为明确的全局定理目标，并由文献中的最小 Ricci 体积重新推导图流形近夹逼序列必须满足的体积和 Weyl 能量饱和条件。
\end{abstract}

\section*{目录}
1 原题、量词与成功标准 ..... 2
2 材料边界与使用方式 ..... 3
3 本主线的任务：让两个性质作用于同一光滑对象 ..... 3
4 图流形的外部基线与一项直接可推导的饱和约束 ..... 4
5 第100步留下的真正全局预算：相对 Chern－Gauss－Bonnet ..... 5
6 连接器方程：只保留完整的几何问题 ..... 5
7 长颈、周边格点与荷：不能只优化一个变量 ..... 6
8 曲面丛：已有输入之后，怎样研究一般 Einstein 存在性 ..... 7
9 全局变分方法：保留下确界，撤掉非达到性的过强推断 ..... 8
10 不能遗漏的正分支与高维问题 ..... 8
11其他高价值路线的保留方式，而非重新从零铺开 ..... 8
12 本会话应优先裁决的三个具体问题 ..... 9
13 Prior－art 边界与论文可能的核心 ..... 9
14 接续入口与不能丢失的原始资产 ..... 10
15 结果交付与论文标准 ..... 11

\section*{1 原题、量词与成功标准}

本会话组的工作命题保持为：对每个维数 $n \geq 2$ ，是否存在只依赖 $n$ 的实常数 $c_{n}<C_{n}$ ，使任意闭、连通、光滑实流形 $M^{n}$ 只要承载一个度量 $g$ 满足
$$c_{n} g \leq \operatorname{Ric}_{g} \leq C_{n} g,$$
就承载某个光滑 Einstein 度量 $h$ ，即 $\operatorname{Ric}_{h}=\lambda h, \lambda \in \mathbb{R}$ ？不要求 $h$ 接近 $g$ ，不要求 $h$ 与 $g$ 的 Ricci符号相同；结论针对同一光滑流形，不是仅同胚类型。

历史归属为 Yau 1982 年 Problem Section 的第 26 题［1］。当前归档没有附上原始题页的完整可核对影像；上式是三个会话反复确认的工作表述，而不是本文件宣称已经逐字认证的历史引文。续接时应在当前工作区核对原始任务书与题页，若发现实质差异，单列差异并调整对应推论，不把相邻的稳定性问题替换成原题。

定义
$$\delta_{\sigma}(g)=\left\|g^{-1} \operatorname{Ric}_{g}-\sigma \mathrm{Id}\right\|_{L^{\infty}, \mathrm{op}}, \quad e_{\sigma}(M)=\inf _{g \in \operatorname{Met}(M)} \delta_{\sigma}(g), \quad \sigma \in\{+1,-1\} .$$
$P_{n}^{\sigma}$ 表示存在仅依赖 $n$ 的 $\varepsilon_{n}>0$ ，使 $\delta_{\sigma}(g)<\varepsilon_{n}$ 推出 $M$ 承载某个 Einstein 度量。工作命题满足
$$Q_{n} \Longleftrightarrow P_{n}^{+} \vee P_{n}^{-} .$$
证明只用缩放：$\widehat{g}=a g$ 时，作为 $(0,2)$ 张量的 Ricci 不变，Ricci 端同态变为 $a^{-1} g^{-1} \operatorname{Ric}_{g}$ 。任一非退化区间都有一个非零内点 $\mu$ 及同号小邻域；将 $\operatorname{Ric} \approx \operatorname{sign}(\mu) g$ 的度量按 $1 /|\mu|$ 缩放即可进人该邻域。反向直接取以 $\pm 1$ 为中心的小区间。

因此，一个固定维数的证明只需要完成其中一个符号分支；完整反驳要在同一维数击败两个符号分支，可以使用不同流形。每个流形都必须排除任意符号的全部 Einstein 度量。构造 $e_{\sigma}(M)=0$本身是一项独立结论，但它只有与该 $M$ 的全部 Einstein 不存在性相结合，才构成分支反例。

二维由一致化、三维正分支由 Hamilton 的正 Ricci 结果提供经典基线；不得把这些作为本项目的新成果。四维的专门工具不会自动推广到 $n \geq 5$ 。本文件允许严谨的强中间结果独立成文，但不把它们改称原题的完整解决。

\section*{1.1 统一范数，避免四倍因子再次混入}

下列 $W^{ \pm}$与签名公式在定向四维范畴内使用；非定向情形须另行处理定向双覆盖及等变下降，不能由覆盖的 Einstein 存在直接推出原流形结论。四维设 $s=\operatorname{tr}_{g} \operatorname{Ric} 、 E=\operatorname{Ric}-\frac{s}{4} g$ 。本文件的$W^{ \pm}$使用在 $\Lambda_{ \pm}^{2}$ 上的曲率算子范数；$E$ 和 Ricci 使用张量范数。于是
$$\begin{aligned}
8 \pi^{2} \chi(M) & =\int_{M}\left(\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}+\frac{s^{2}}{24}-\frac{|E|^{2}}{2}\right) d \mu_{g} \\
12 \pi^{2} \tau(M) & =\int_{M}\left(\left|W^{+}\right|^{2}-\left|W^{-}\right|^{2}\right) d \mu_{g} \\
\left|\operatorname{Rm}_{\text {full }}\right|^{2} & =4\left(\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}\right)+2|E|^{2}+\frac{s^{2}}{6}
\end{aligned}$$
若写 $\mathcal{R}$ 表示完整曲率算子，则 $\left|\operatorname{Rm}_{\text {full }}\right|^{2}=4|\mathcal{R}|^{2}$ 。精确 Einstein 时分别有 $\int|\mathcal{R}|^{2}=8 \pi^{2} \chi$ 和 $\int\left|\operatorname{Rm}_{\text {full }}\right|^{2}=32 \pi^{2} \chi$ 。Eguchi－Hanson 的 $12 \pi^{2}$ 能量采用前一种规范；后一种为 $48 \pi^{2}$ 。
$$\delta_{\sigma} \leq \delta \text { 给出 } \quad|s-4 \sigma| \leq 4 \delta, \quad|E|^{2} \leq 4 \delta^{2}, \quad \mid \text { Ric }-\left.\sigma g\right|^{2} \leq 4 \delta^{2} .$$
全文不把小 $L^{p}$ 积分、小加权范数、局部精确解，替换成原题要求的全域无权 Ricci 端同态上确界。

\section*{2 材料边界与使用方式}

本文件是供原会话从 Step101 继续研究的科学续接稿，不是以整理文字替代原始证明的投稿稿。依据包括：2026－09－15 进展包、2026－09－16 逐步归档、S0910A01／A02／A03 各 100 步的完整meta－trace，以及用户提供的 Codex 对原稿的逐段审读报告。外部文献核对日期为 2026－09－16。两个 ZIP 含摘要、公式、分级和原稿路径，但不含所有被引用的原始 TeX、证明笔记和程序字节。

下列标签只用于区分证据，不对数学内容按平台打分：【文献】表示本轮核对到的外部定理或明确引用；【原稿审读】表示原稿被 Codex 实质审读、未发现缺口的报告；【轨迹】表示会话记载的推导或内部核验；【本稿重算】表示下文完整展示的代数或逻辑推导；【待证】表示仍需新证明的目标。已撤回结论只作为边界保存，不进入定理依赖。

精确 Einstein 的统一拓扑间隙已有原稿审读支持，不能再因一般 near－Einstein 平滑接口未闭合而降回＂只有摘要的想法＂。一般 near－Einstein 的统一 Ricci 夹逼间隙仍未完成，不能因前一项成立就自动升级。固定 $A_{1}$ 近 Einstein 构造与全局 Einstein 不存在性也是两个命题。

第一次接续应读取本会话当前任务书、工作区最近修正及下文列出的原稿，记录版本；不重启已经做完的 300 步，也不把审读报告当成原稿全文。三份文件彼此独立可编译；没有要求安装新应用或改变系统基础架构。缺失来源的恢复应服务于一个具体定理，不应演变为无期限重复检索。

\section*{3 本主线的任务：让两个性质作用于同一光滑对象}

对一个明确指定的 $M$ ，反例所需的两部分是
$$\mathrm{P}_{\sigma}(M): e_{\sigma}(M)=0, \quad \mathrm{~N}(M): M \text { 不承载任何 Einstein 度量. }$$
本会话的科学目标是严格建立某个 $\mathrm{P}_{\sigma}(M) \wedge \mathrm{N}(M)$ ，或者证明关键候选的 $e_{\sigma}$ 有正下界，或者反向构造该候选上的 Einstein 度量。三种结论都推进原题，但逻辑作用不同。

\begin{tabular}[t]{|l|l|l|}
\hline 对象 & 当前可以继承的内容 & 真正尚未完成的内容 \\
\hline 指定一般型吹起族 & A01 持有精确拓扑间隙及必要退化的审读支持 & 近似方程的无额外几何假设间隙，或同一无 Einstein 拓扑上的输入构造 \\
\hline 固定 A1 解消 & A02 持有 $e_{\sigma}(M)=0$ 的构造链 & 识别准确 smooth type，证明全部 Einstein 不存在，或证明某个 Einstein 存在 \\
\hline Dehn－twist 曲面丛 $E_{D}$ & 累积稿与 A03 第 68－69 步报告全局近负 Einstein 输入 & 输入原稿核准；非适配、非 Kähler的一般 Einstein 存在性判断 \\
\hline 含纯双曲块的 extended graph 流形 & 在 Di Cerbo 精确范畴内有全部 Einstein 不存在性 & 全 Ricci 缺陷趋零的闭合连接器与全局度量 \\
\hline
\end{tabular}

曲面丛的 $\mathrm{P}_{-}$与图流形的 N 属于不同对象，不能相加。一个图流形局部 free－$T^{2}$ 区域也不意味着整个闭流形具有自由环面作用。第三主线应保留这些差异，而不是用同一个＂长颈＂名称将不同拓扑合并。

\section*{4 图流形的外部基线与一项直接可推导的饱和约束}

\section*{4.1 先固定 Di Cerbo 范畴，不能只用名称}

采用 Di Cerbo 文中定义的闭、定向 extended graph 四流形，检查真实双曲块、非纯块、边界仿射粘合及周边子群的条件［2］。不能把任意有图式分解的流形都包含进去，也不能将无非平凡拼接的闭双曲流形当成无 Einstein 例。

对于含至少一个纯实双曲四维块的相应对象，记各块截面曲率 -1 的体积和为
$$V_{0}=\sum_{j} \operatorname{Vol}_{-1}\left(P_{j}\right)>0 .$$
该文 Lemmas 8－9 给出 $\tau(M)=0 、 \chi(M)=3 V_{0} /\left(4 \pi^{2}\right)$ ，以及 Ric $\geq-3 g$ 规范下的最小 Ricci 体积为 $V_{0}$ 。它们与全局不存在性证明共同构成可靠基线。没有纯块的 $\chi=\tau=0$ 情形本来就受紧夹逼的 Chern－Weil 障碍限制，不应作为本路线的主要候选。

\section*{4.2 近负 Einstein 序列必须同时饱和体积与 Weyl 预算}

以下为【本稿重算】的文献推论，不宣称文献首次。改用原题的 Ric $\approx-g$ 归一化，令
$$V_{*}=9 V_{0}=12 \pi^{2} \chi(M) .$$
若 $\delta=\delta_{-}(g) \leq 1 / 3$ ，则
$$\frac{V_{*}}{(1+\delta)^{2}} \leq \operatorname{Vol}_{g} M \leq \frac{V_{*}}{(1-\delta)^{2}}$$
左界来自最小 Ricci 体积： $\operatorname{Ric}_{g} \geq-(1+\delta) g$ ，缩放 $h=(1+\delta) g$ 后 $\operatorname{Ric}_{h} \geq-h$ ，其四维体积为$(1+\delta)^{2} \mathrm{Vol}_{g} M$ 。右界来自 CGB 与下述点态估计。

对四个 Ricci 特征值处于 $[-1-\delta,-1+\delta]$ ，记 $\lambda_{i}$ ，则
$$\frac{s^{2}}{24}-\frac{|E|^{2}}{2}=\frac{\left(\sum_{i} \lambda_{i}\right)^{2}}{6}-\frac{1}{2} \sum_{i} \lambda_{i}^{2} \geq \frac{2}{3}(1-\delta)^{2}, \quad \delta \leq 1 / 3 .$$
可逐变量利用该二次式的凹性把最小化归到区间端点；按高端点数目 $j=0, \ldots, 4$ 检查五个值即可。结合式（1．4）和 $8 \pi^{2} \chi=\frac{2}{3} V_{*}$ ，得到式（4．1），并进一步得到
$$0 \leq \int_{M}|W|^{2} d \mu_{g} \leq 8 \pi^{2} \chi(M)\left[1-\left(\frac{1-\delta}{1+\delta}\right)^{2}\right]$$
所以固定图流形若存在 $\delta_{i} \rightarrow 0$ ，必须有 $\operatorname{Vol}_{g_{i}} M \rightarrow V_{*} 、 \int|W|^{2} \rightarrow 0$ ；变化拓扑时则是相对 $\chi\left(M_{i}\right)$的 Weyl 能量趋零。另有 $\int|E|^{2} \leq 4 \delta_{i}^{2} \operatorname{Vol} M_{i}$ 。

这个约束比＂有可能通过塌缩逃走＂具体得多。但它不是矛盾：局部极限可以是真双曲几何，而真双曲 Einstein 局部片本来存在。不能把 A01 的禁止校准谱论证照搬到这里。图流形的难点是，非双曲的粘合拓扑能否被藏进很小的 Weyl 能量与受控 Ricci 缺陷中。

研究目标 4.1 （图流形的二择一结论）。在一个完整核准的上述图流形或明确序列上，构造 $\delta_{-}\left(g_{i}\right) \rightarrow$0；或者建立阻止式（4．1）－（4．2）同时逼近的统一几何代价。固定流形正间隙、固定拓扑族正间隙和仅依维数的正间隙必须分别陈述。

若只证明模型对称类内的正间隙，不能说所有图流形度量已被排除；若真的构造成功，因为外部全部 Einstein 不存在性已核准，将得到负分支反例，但完整 $Q_{4}$ 的否定仍需正分支。

\section*{5 第100步留下的真正全局预算：相对 Chern－Gauss－Bonnet}

在本节临时使用双曲截面曲率 $-1 、 \operatorname{Ric}=-3 g$ 的规范，记物理缺陷 $\mathrm{E}=\operatorname{Ric}+3 g 、 e=\operatorname{tr} \mathrm{E}$ 。转回原题取 $h=3 g$ ，则 $\delta_{-}(h)=(1 / 3)\left\|g^{-1} \mathrm{E}\right\|_{\infty}$ ，不要混用数值阈值。

设 $N$ 是替换双曲 cusp 尾部的全部区域，删除尾部总体积为 $V_{\mathrm{rem}}, V_{N}=\operatorname{Vol} N$ 。假设补集保持原精确双曲度量，且拓扑 Euler 预算对应原块总和。全局 CGB 减去补集后有
$$2 \int_{N}|W|^{2}+12\left(V_{N}-V_{\text {rem }}\right)=\int_{N}\left(\left|\mathrm{E}^{\circ}\right|^{2}+2 e-\frac{e^{2}}{12}\right) .$$
这里必须是匹配后的光滑闭度量；若只对尚有边界的试验域使用，则应保留对应边界转移项。
若端同态误差特征值 $x_{i} \in[-\epsilon, \epsilon]$ ，二次部分为
$$\sum_{i} x_{i}^{2}-\frac{1}{3}\left(\sum_{i} x_{i}\right)^{2}$$
其绝对值不超过 $4 \epsilon^{2}$ ，而 $|2 e| \leq 8 \epsilon$ 。所以
$$\left.\left|2 \int_{N}\right| W\right|^{2}+12\left(V_{N}-V_{\text {rem }}\right) \mid \leq\left(8 \epsilon+4 \epsilon^{2}\right) V_{N} .$$
近零缺陷必满足
$$V_{\mathrm{rem}}-V_{N}=\frac{1}{6} \int_{N}|W|^{2}+o\left(V_{N}\right) .$$
来源与状态：A03 第100步修正后的相对 CGB 关系；本稿重新检查规范与代数。它取代第99步错误地将局部 free－$T^{2}$ 连接器当成整个闭 $\chi=0$ 流形的论证。

它是一条相容条件，不是自动不可能性。 $V_{N}$ 可以小于 $V_{\text {rem }}$ ；体积差可以支付 Weyl 能量。满足该条件也没有解决水平、形状、混合和荷方程。第 99 步将目标改成固定缺陷约 1.098 的主张已撤回：任一有限正缺陷都不能反驳允许任意窄区间的原题，该数值也没有被证明几何最优。

\section*{6 连接器方程：只保留完整的几何问题}

\section*{6．1 Gaussian 表示与全部 Ricci 分量}

令 $g=d r^{2}+q(r), K=\frac{1}{2} \partial_{r} q 、 S=q^{-1} K 、 H=\operatorname{tr} S$ 。在 Ric $\approx-3 g$ 规范下，残差的全部分量为
$$\begin{aligned}
& \mathrm{E}_{r r}=3-\operatorname{tr}\left(q^{-1} K_{r}\right)+\operatorname{tr}\left(S^{2}\right) \\
& \mathrm{E}_{r i}=q^{j k} \nabla_{j} K_{k i}-\partial_{i} H \\
& \mathrm{E}_{i j}=\operatorname{Ric}(q)_{i j}+3 q_{i j}-\left(K_{r}\right)_{i j}-H K_{i j}+2\left(K q^{-1} K\right)_{i j}
\end{aligned}$$
等价的法向方程是
$$H^{\prime}=3-|S|^{2}-\mathrm{E}_{r r} .$$
混合 Codazzi 块不能省略。计算范数需通过 $g=L L^{\top}$ 的 Cholesky 分解，使用 $L^{-1} \mathrm{E} L^{-\top}$ 的谱，而不是坐标分量最大值。

中心 Cauchy 数据 $\left(q_{0}, K_{0}\right)$ 应满足标量与动量约束。精确 Einstein 规范的标量约束为
$$R_{q_{0}}=-6+H_{0}^{2}-\left|S_{0}\right|^{2} .$$
全测地中心 $K_{0}=0$ 要求 $R_{q_{0}}=-6$ ；最小中心 $H_{0}=0$ 并不要求 $K_{0}=0$ 。不能把 charged 中心擅自替换成全测地中心。

\section*{6.2 正定矩阵表示不意味着方程已解}

第98步保留了全部轨道矩阵和混合方向。令 $B=q_{0}^{1 / 2}, A=B^{-1} K_{0} B^{-1}, \widehat{R}=B^{-1} \operatorname{Ric}\left(q_{0}\right) B^{-1}$ ，写
$$q=B \exp (X) B .$$
在 $H_{0}=0$ 的中心，两侧满足
$$X(0)=0, \quad X_{r}(0)= \pm 2 A, \quad X_{r r}(0)=2(\widehat{R}+3 I) .$$
因 $\left.\frac{d^{2}}{d r^{2}} e^{X}\right|_{X=0}=X_{r r}+X_{r}^{2}$ ，无须假设矩阵交换，就恢复正确二阶 Einstein 中心数据。指数表示保证正定，却不控制全 Ricci 残差，也不证明可延拓到远端。

数值参数化必须解析地固定端点一、二阶导数。若只是评估时覆盖端点导数数组，优化结果并不对应实际光滑度量。第 98 步粗网格中心 Codazzi 误差曾被误当最终缺陷；其随 Fourier 分辨率下降说明这是离散误差，不是几何下界。一次拟合下降、未保存系数、未去混叠的非线性乘积，不构成存在证据。

\section*{6.3 平切片障碍与 Koiso 局部可解性分别说明什么}

若所有切片平坦，$R_{q}=0$ ，标量约束迫使
$$H^{2}-|S|^{2}=6+O(\epsilon), \quad H^{2} \geq 9-6 \epsilon .$$
足够小误差时无法穿过 $H=0$ 。这只排除平切片模型，不排除曲切片、twist 或非对角补偿。
另一方面，取非恒定解析周期 $f$ ，
$$h_{0}=d \theta^{2}+e^{2 f(\theta)} d x^{2}+e^{-2 f(\theta)} d y^{2}, \quad R\left(h_{0}\right)=-2\left(f^{\prime}\right)^{2}$$
负 Yamabe 类的归一化代表 $h=\psi^{4} h_{0}$ 可满足 $R(h)=-6$ ，对应
$$-8 \psi^{\prime \prime}-2\left(f^{\prime}\right)^{2} \psi=-6 \psi^{5} .$$
它提供 Koiso 式解析局部 Einstein Cauchy 数据，说明不能用一个失败的有限参数中心模型排除所有局部中心。它不提供双端 cusp 匹配、共同长时间延拓或全局闭度量。

\section*{7 长颈、周边格点与荷：不能只优化一个变量}

\section*{7.1 半长与误差的共同极限}

在最小中心 $H(0)=0$ 与扩张端 $H(R)=3$ 的受限 Gaussian 模型中，Raychaudhuri 比较给出
$$1 \leq k \tanh (k R), \quad k=\sqrt{1+\epsilon / 3} .$$
若 $\epsilon \rightarrow 0$ ，必须 $R \rightarrow \infty$ ；展开相应必要代价为 $\epsilon \gtrsim 12 e^{-2 R}$ 。这是该端点条件下的法向必要条件，不是全连接器的充分误差率。增加 $R$ 后切向与混合残差可能更坏，不能只展示法向块衰减。

精确外部基准 $q=e^{2 r} q_{0}$ 的残差为切向 $\operatorname{Ric}\left(q_{0}\right)$ ，物理大小随 $e^{-2 r}$ 衰减；最大值仍可能在腰部。$q=\cosh ^{2}(r) q_{0}$ 也不能保留一般 charged 中心的 Weingarten 数据。因此外部 redshift 不能自动修复内过渡。

\section*{7.2 周边覆盖的正确作用}

轨迹第69、100步使用周边格点（ $N, 1,1$ ），经 cusp 深度约 $\log N$ 后得到长度尺度（ $1, N^{-1}, N^{-1}$ ），与 rank－two 商塌缩中心匹配。商操作在局部保留度量与 Ricci 端同态，却把体积与缺陷积分同时缩小；它不直接减小点态缺陷。

第100步提出一个24－cell 双曲块的具体候选及一cusp 循环覆盖。该 census 标签、周边同调像、覆盖连通性、cusp 类型和 Di Cerbo 假设都要回到原构造或可复核的三角剖分核准；本稿不将轨迹中的 census 数值当成外部已认证输入。原始周边字符非零并不自动意味着任意度数覆盖都只有一个 cusp，应检查相应指数与互素条件。

对固定无量纲连接器轮廓，体积、Weyl 能量与所有缺陷积分可共同按 $N^{-2}$ 缩放，式（5．1）除以体积后仍不变。真正近零缺陷时 $R$ 也要增长，匹配深度变为
$$T=\log N-R+O(1), \quad N \gg e^{R}$$
所以需要同时控制 $R, N$ 与依 $R$ 变化的轮廓体积和谱常数。把 $N \rightarrow \infty$ 当成一切误差自动消失的极限是错误的。

\section*{7.3 荷与 Bochner 的抵消必须保留}

第95步的有效工具可抽象为一条带边界项的代数恒等式。对对称矩阵 $A$ 、向量荷 $q$ 、密度$d \mu_{\sigma}$ ，设 $Q=\frac{1}{2} q^{\top} A q 、 m_{q}(X)=q^{\top} A X q$ ，则
$$\int m_{q}(X) d \mu_{\sigma}=\int_{\partial \Omega} Q\langle X, \nu\rangle d \mu_{\sigma, \partial}-\frac{1}{2} \int q^{\top}\left\{X(A)+\left(\operatorname{div}_{\sigma} X\right) A\right\} q d \mu_{\sigma}$$
它由 $X Q=\frac{1}{2} q^{\top} X(A) q+m_{q}(X)$ 分部积分得到。应用于连接器时应恢复原稿 $A=e^{-3 \sigma} M^{-1}$ 的变量字典和边界通量。

原稿曾试图把 drift 曲率的 $+Q|d U|^{2}$ 当成有利项，直接沿用无 twist 上界；实际张力项产生$-Q|d U|^{2}$ 抵消，剩余含面积梯度与形状梯度的相关项，没有固定符号。这个抵消保留了 twist 参与过渡的可能性。不能再使用已撤回的 scalar－charge ceiling，也不能因为＂有荷可能补偿＂就认定全局解存在。

\section*{8 曲面丛：已有输入之后，怎样研究一般 Einstein 存在性}

累积稿第6章及A03第68步记录了一类 Dehn－twist 曲面丛 $E_{D}$ 的最大范数近负 Einstein 输入构造，使用慢变度量、显式 Ricci 块、全局修正与长颈估计。当前归档没有完整给出所有种数、单值化映射与系数；续接须取回原定义，不以一个同名抽象曲面丛替代。首先确认是固定 smooth type 上的 $e_{-}\left(E_{D}\right)=0$ ，还是随 $D$ 变化的序列，这影响原题量词。

适配某个纤维化、水平可积或基本平均曲率的 Einstein 刚性结果，可以限制适配度量，却不能限制任意 Einstein 度量。曲面丛拓扑本身不要求未知 Einstein 度量尊重原纤维结构。

对基面 NPC 目标的能量极小调和映射，不自动是调和态射或水平共形。将两个双曲曲面的乘积投向另一个标记的双曲曲面，便可产生 Einstein 源上的调和映射而缺少所需共形性。优化目标Teichmüller 结构给出的通常是积分 TT 平稳条件，不是逐点 Hopf 微分消失。欲获得全局障碍，应从具体无限 Dehn－twist 单值化、谱退化或共形缺陷找到新的强制量。

可以考察以下有数学裁决力的方向：是否某个任意 Einstein 度量都诱导特定可控的调和映射结构；是否可由单值化推出一个与 Einstein 方程不相容的积分恒等式；或是否存在不同复结构／不同构造实际上给该 smooth type 一个 Einstein 度量。每一方向都需要完整假设，而不是＂曲面丛没有复结构所以没有 Einstein＂。

\section*{9 全局变分方法：保留下确界，撤掉非达到性的过强推断}

四维有
$$\mathcal{F}(g)=\int_{M}\left(|W|^{2}+s^{2} / 24\right) d \mu_{g}=8 \pi^{2} \chi(M)+\frac{1}{2} \int_{M}|E|^{2} d \mu_{g}$$
如果某个固定流形的输入构造还给出体积控制，使 $\int|E|^{2} \rightarrow 0$ ，则其下确界为 $8 \pi^{2} \chi$ 。若光滑度量达到这个下确界，则 $E=0$ ，由收缩 Bianchi 在 $n>2$ 得标量常数，从而是 Einstein 度量，符号不限。

但展示一列退化极小化序列，只证明一条极小化路径不紧，不证明不存在另一光滑极小值点。近 Einstein 的 $L^{p}$ 残差也不是四阶变分 Euler－Lagrange 残差。Ekeland、Palais－Smale 或＂泛函非负＂不能未经估计填平此差距。每次调用必须说明固定范畴、紧性、规范、允许退化和最终 smoothtype 的恢复。

一个真正有影响的结果可以是：在这些已构造输入的流形上证明全局达到性，产生 Einstein；或者证明所有可能达到情形都被一个严格障碍排除，得到全部 Einstein 不存在性。任一方向都要覆盖全部候选极小值，而不是只覆盖选定 orbifold 附近的一支。

\section*{10 不能遗漏的正分支与高维问题}

本会话不重复 A02 的有限维计算，但应维护全局覆盖范围。Ric $\approx+g$ 给 Myers 直径界、Bishop体积上界和有限基本群，不给统一体积下界或基本群阶上界。精确 Einstein 商可以塌缩；正确目标不是排除所有塌缩，而是理解其是否仍与 Einstein 存在性兼容。

四维在固定非塌缩条件下可用有界 Ricci 有限型与正则片理论［3］。有限多个微分同胚型本身不构造 Einstein 度量，也不使极限光滑；曲率集中与 smooth－type 恢复仍需研究。对两两不同的高拓扑复杂度输入，体积塌缩可能被迫出现。此处的四维曲率能量约束与 A01 的 SW 近等号密度不同，不能强行套同一禁止谱。

若在一个非塌缩覆盖上产生了 Einstein 度量，仍要证明它对原甲板群等变，才能下降；覆盖存在 Einstein 并不自动意味着商的指定光滑结构存在所需度量。

对于 $n \geq 5$ ，四维的 $\Lambda_{ \pm}^{2}$ 、SW／Bauer－Furuta 和 CGB 二次能量机制没有直接同构替代。高维路线可以寻找拓扑驱动的临界 $L^{n / 2}$ 预算、特定特殊结构下的禁止曲率模式、沿余维四奇异层的ALE 束障碍或新的全部 Einstein 不存在性。但若加入特殊 holonomy、对称性、体积或完整曲率假设，只得到该范畴定理，不是原题。

四维输入与同符号 Einstein 因子相乘，端同态误差是两因子误差的最大值，因而可传播某些输入；它不传播全部 Einstein 不存在性，因为产品上的任意 Einstein 度量不必分裂。正 Einstein球因子维数至少 2 ，这种乘积也跳过五维。项目尚无可直接调用的高维全部 Einstein 障碍，不等于数学上不存在，也不构成停止探索的理由。

\section*{11 其他高价值路线的保留方式，而非重新从零铺开}

双曲连通和与 BCG／Sambusetti 熵路线在轨迹中已有目标依赖的障碍信息；不足处是没有与之匹配的任意紧 Ricci 夹逼构造，且常数可能依赖目标。其正确延伸是研究近等号熵映射能否保留周边同伦信息、能否给出固定拓扑损失的定量代价，而不是再次把经典熵不等式本身列为新突破。使用前恢复 A01 第91步的实际命题与源文献，不能把某个目标的界推广为维数统一界。

精确 Poincaré－Einstein 或 AH／cusp 模型显示切向与法向非线性补偿并非不可能，这是反对简单局部无解结论的真实依据。但一个自对偶模型未必提供可反射的全测地 $T^{3}$ 中心：若解析 Einstein

邻域中有反射，该反射逆转取向并交换 $W^{+}, W^{-}$，自对偶与反射相容会迫使二者同时消失；中心因而不能是所设想的紧致负常曲率三环面。这只限制该反射应用，不否定其他非对称中心。

已有负 Einstein Dehn filling 思路可以帮助研究边界与逆算子，但填充改变周边拓扑；得到另一个流形上的 Einstein 度量，不能成为 Di Cerbo 图流形上的存在反证。有限维的 free－$T^{2}$ 、对角、orthogonally transitive 或反射对称类也不穷尽所有图流形度量。保留这些路线的价值在于给主攻问题提供精确对照，而不是用局部范畴的失败宣布原题已经偏向真或假。

\section*{12 本会话应优先裁决的三个具体问题}

\section*{12.1 问题 G：真实双端连接器的连续极限是否存在}

固定完整 Di Cerbo 图流形候选、周边粘合和中心约束，构造保持两侧端点全部 jets 的完整矩阵场。数值上要求系数保存、精细网格独立验证、非线性去混叠、正定性下界、所有 Ricci 块和尺度依赖误差；再寻求解析或区间后验估计。若线性化逆范数为 $B$ 、二次非线性常数为 $C$ 、残差为$\varepsilon$ ，校正可行性至少要控制相应 $B^{2} C \varepsilon$ ，而不是只让离散残差变小；余核与自由参数需另外解决。

若始终失败，寻找在分辨率和端点参数变化下仍存在的连续伴随障碍，而不是把一次优化停滞当成不存在性。有效障碍须对真实方程与允许自由度配对，并能排除所有足够小缺陷，而非只排除某个五次插值。

\section*{12.2 问题 S：曲面丛或固定解消的全局 Einstein 判断}

优先挑一个输入已经最清楚的具体 smooth type，恢复全部拓扑数据和构造证明。对正、零、负 Einstein 常数逐项列出可用证书，剩余的某个符号不能用未经证明的 Ricci－flat 分类消掉。尽可能把问题转成一个具实际约束的调和映射、能量达到性或全局模空间命题。

如果证明了 Einstein 存在，应明确是新存在性结果而非反例失败的废弃产物。若只证明附近无解，保留为局部定理，并说明何种额外全局覆盖才能得到全部不存在性。

\section*{12.3 问题 R：图流形的 Weyl 小量是否有全局拓扑代价}

式（4．2）使假想序列具有归一化 Weyl 小量。研究这种全局近双曲状态能否强迫相容的几何／拓扑结构，或允许非双曲周边 $\mathbb{Z}^{3}$ 在极小能量区域存活。不能把 $L^{2}$ 小量直接升为全域点态 Weyl 小量；A02 的尖峰是必要测试。

若能构造一个新的定量拓扑稳定性定理，可能直接排除整类负分支反例；若找到能保留周边群的严格构造，可能完成问题 G。它与 A01 有共同的＂小缺陷到局部结构＂技术，但这里的局部双曲模式不是被禁止的模式，最后必须有全局步骤。

\section*{13 Prior－art 边界与论文可能的核心}

Di Cerbo 的全部 Einstein 不存在性和最小 Ricci 体积不是本项目成果［2］。由它们结合 CGB得到式（4．1）－（4．2）是本文件重算的直接推论，可用作严格筛选条件，不以一个代数推论单独宣称重大突破。Koiso 局部解析存在、Yamabe 归一化和负曲率调和映射理论也是背景；真正新增要落在全局匹配、近零缺陷的共同参数控制或无额外适配假设的 Einstein 判断上。

当前不承诺这条主线已经有一篇完成的主论文。可独立成文的强结果应当是：一个全局负分支反例；一个无对称性限制的连接器／图流形夹逼间隙；一个此前未知 smooth type 的 Einstein 存在

性；或一个显著更一般、可用于多个候选的全局稳定性／非达到性定理。仅若某受限模型定理本身具有独立新意与用途，才考虑将其单独写出。

\section*{14 接续入口与不能丢失的原始资产}

第100步相对 CGB 与全局预算 Sessions／S0910A03／workspace／notes／step100＿relative ＿cgb＿graph＿budget．md
全矩阵匹配压力测试 Sessions／S0910A03／workspace／notes／step98＿full＿matrix＿matching＿ pressure＿test．md
荷与 Bochner 抵消 Sessions／S0910A03／workspace／notes／step95＿KX＿and＿bochner＿cancel lation．md

周边格点与各向异性匹配 Sessions／S0910A03／workspace／notes／step69＿anisotropic＿cusp＿ compensation．md

局部 Koiso 中心数据 Sessions／S0910A03／workspace／scripts／step69＿collapsed＿koiso＿c enter．py

完整矩阵残差程序 Sessions／S0910A03／workspace／scripts／step98＿full＿matrix＿joint＿tra nsition．py

独立分辨率检查 Sessions／S0910A03／workspace／scripts／step98＿center＿residual＿resol ution．py
曲面丛、全局 TT 与单值化章节 Skills／qiushi－yau26／references／research／20260912．tex双曲熵障碍的已有路线 Sessions／S0910A01／workspace／notes／step91＿sambusetti＿bcg＿quan titative＿route．md

同伴固定 A1 输入 Sessions／S0910A02／workspace／notes／step83＿near＿pinched＿construc tion＿and＿frontier＿reduction．md

同伴精确拓扑间隙 Sessions／S0910A03／workspace／briefing／Yau26＿uniform＿gap．tex
第99步笔记与 JSON 应带第100步修正，不作为当前反例目标。第98步的端点数组覆盖、粗网格最大值与未保存系数不得用于严格构造。第 95 步 charged ceiling 已撤回，但式（7．2）及真实抵消应保留。第68－69步曲面丛调和态射缺口、非适配 Einstein 自由度与周边匹配问题不得被后续摘要省略。

\section*{14.1 从 Step101 开始的合理顺序}

先读取当前工作区与上述最终笔记，冻结一个真正满足外部不存在性假设的图流形候选及其完整周边数据；同时核准曲面丛输入的准确版本。用相对 CGB、全矩阵残差与 $(R, N)$ 联动重算候选的全局预算，然后在问题 G、S、R 中选择一个有最强证据的目标深入。

A03 不接管 A01 已经审读的精确间隙主证明，也不复制 A02 十维 Weyl 核计算。需要调用时传递完整条件与版本。若发现新的更有效全局机制，允许转向；但必须说明它改变了 $\mathrm{P}_{\sigma}$ 或 N 的哪一部分，不能仅增添一组相关术语。

这一安排保留 300 步中的有价值内容，又把后续计算约束在原题真正需要的闭合处：同一光滑对象、同一归一化、全部方程、全部 Einstein 符号和明确常数依赖。

\section*{15 结果交付与论文标准}

研究结论以具体命题和证明为单位，而不是以 Agent 数量、步数或平台认可次数为单位。同一公式在多个会话复算，可以提高证据质量，不产生多项独立新发现。

可完成的结果应及时冻结成可独立阅读的数学稿：准确的假设与量词，新增结论相对最接近文献的差别，所有分析接口及常数依赖，完整证明，必要时附有限计算及独立复算说明。假设增多或结论缩小必须在主定理中显式反映。无需等到整个 Yau26 解决才允许发表严谨的中间结果，也不把一个证明链拆成若干缺乏独立贡献的论文。

Annals、Inventiones、JAMS、Acta 可以作为高质量写作与结果强度的目标，但任何文件都不预设已达到其录用标准。完整性、首创性、重要性和选刊是四项判断。用经典工具证明新的重要定理可以完全原创；出现一个新名称、搜不到同名词或构造了＂框架＂，并不能确认首创性。按精确命题及假设进行查新，并记录最近定理、包含关系及真正新增的证明步骤。

无论本轮选择论文收束还是进一步探索，结束时只需留下四类必要材料：更新后的主定理与证明；当前最小未闭合命题；确切被否定的模型及原因；可供同伴直接使用的来源、版本和计算。除非出现新的反证或新缺口，不再次从零争论已审读的同一结果。反过来，发现具体错误就修正所有依赖它的结论，而不是只新增一份不被后续读取的纠错说明。

\section*{参考文献}
\begin{itemize}
\item[] ［1］S．－T．Yau，Problem Section，in Seminar on Differential Geometry，Annals of Mathematics Studies 102，Princeton University Press，1982，pp．669－706．历史题页仍需在工作区逐字核对；本稿采用任务书中的区间命题。
\item[] ［2］L．F．Di Cerbo，Extended graph 4－manifolds，and Einstein metrics，arXiv：2106．13279．https： ／／arxiv．org／abs／2106．13279．本轮核对其 extended graph 定义、Lemmas 8－9 和 Einstein不存在性证明；不推广到所有称为＂图流形＂的空间。
\item[] ［3］J．Cheeger and A．Naber，Regularity of Einstein manifolds and the codimension 4 conjecture， arXiv：1406．6534．https：／／arxiv．org／abs／1406．6534．引用须区分有界 Ricci 的非塌缩正则片与精确 Einstein 的更强正则性。
\item[] ［4］A．Naber and R．Zhang，Topology and $\epsilon$－regularity theorems on collapsed manifolds with Ricci curvature bounds，Geom．Topol． 20 （2016），2575－2664．https：／／doi．org／10．2140／gt． 201 6．20．2575．最大纤维化幂零秩、模型几何等输入不能省去；本稿不宣称这些输入已由夹逼推出。
\item[] ［5］W．Jiang，L．Kong and S．Xu，Convergence of Ricci－limit spaces under bounded Ricci curvature and local covering geometry I，arXiv：2205．00373．https：／／arxiv．org／abs／2205．00373．local covering geometry 是额外结构；具体使用前核对版本与定理。
\item[] ［6］M．T．Anderson，Ricci curvature bounds and Einstein metrics on compact manifolds，J．Amer． Math．Soc． 2 （1989），455－490．https：／／doi．org／10．1090／S0894－0347－1989－0999661－1．本轮确认文献身份，未取得所需 Corollary B（4）的完整原文；不得据二手概述填写其假设或用它排除输入曲率尖峰。
\item[] ［7］H．Ge and W．Jiang，є－regularity for shrinking Ricci solitons and Ricci flows，arXiv：1707．05511． https：／／arxiv．org／abs／1707．05511．本轮核对 Theorem 1．1、Theorem 3．4；后者为有界Ricci 的尺度选择，不是一般有界 Ricci 的点态曲率结论。
\end{itemize}
\begin{itemize}
\item[] ［8］T．Ozuch，Noncollapsed degeneration of Einstein 4－manifolds，II，arXiv：1909．12960v2；Geom． Topol． 26 （2022）．https：／／arxiv．org／abs／1909．12960．本轮重点核对§7．3、Corollary 15、Remarks 50－51 及明确的 $L^{\infty}$ 问题；编号以该 arXiv 版本为准。
\item[] ［9］C．LeBrun，Ricci curvature，minimal volumes，and Seiberg－Witten theory，Invent．Math． 145 （2001），279－316．https：／／arxiv．org／abs／math／0003068．本轮核对 Theorem 2.3 的证明及式（11）、Proposition 3．1－3．2、Corollary 3．4；不把 $1 / 3$ 说成已证明最优的 Einstein 拓扑阈值。
\item[] ［10］Qiushi Engine 项目资料：2026－09－15 进展包、2026－09－16 逐步归档，S0910A01／A02／A03 各100步 meta－trace；源文件名与本地工作区定位见正文。原稿、脚本与摘要须分别识别，不能把记录中的成功标签视作外部定理。
\item[] ［11］用户在本会话提供的 Codex 原稿审读报告（截至2026－09－16）：Sessions／S0910A03／worksp ace／briefing／Yau26＿uniform＿gap．tex，重点位置原稿约第277行；另核查 A02 第83步构造笔记。结论为在所审读依赖链中未发现实质缺口，且精确拓扑间隙不依赖（SC）。本引用是审读报告的来源定位，不声称原稿全文已包含于归档。
\end{itemize}
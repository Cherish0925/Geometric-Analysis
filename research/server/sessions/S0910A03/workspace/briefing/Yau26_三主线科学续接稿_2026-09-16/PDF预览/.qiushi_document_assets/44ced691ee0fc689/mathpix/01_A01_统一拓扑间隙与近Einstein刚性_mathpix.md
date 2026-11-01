---
source_file: 01_A01_统一拓扑间隙与近Einstein刚性.pdf
converter: mathpix
format: mmd
---

\title{
主线一：Einstein 统一拓扑间隙与近等号刚性
}

S0910A01｜从已审读的精确定理走向无额外几何假设的 Ricci 夹逼结论

\author{
Qiushi Engine 科学续接稿
}

2026 年 9 月 16 日

\begin{abstract}
摘要
本主线承接 300 步中的 Seiberg－Witten／Chern－Weil 近等号分析、局部禁止曲率模式、平均缺陷传输与允许塌缩的正则性。已审读的主要结果是指定复曲面吹起族上精确 Einstein 的统一拓扑间隙，配套结果为近临界近 Einstein 序列的必要退化。后续的核心问题不是重复包装精确定理，而是判断这种刚性是否对任意塌缩的近似 Einstein 方程稳定。本稿保留可独立成文的已获结果、尚未完成的局部流接口和反例可能性；给出一组可直接复算的粗常数缺陷估计，供续接时与原稿对照。
\end{abstract}

\section*{目录}
1 原题、量词与成功标准 ..... 2
2 材料边界与使用方式 ..... 3
3 已经取得的主结果及其逻辑位置 ..... 3
4 精确主定理的证明机制：必须保留的五个环节 ..... 4
5 把代数缺陷写完整：一组可直接复算的连接估计 ..... 6
6 从精确方程到近似方程：三个可竞争的证明方向 ..... 7
7 必须保留的300步技术积累及其当前边界 ..... 8
8 Prior－art 审计：要回答的不是名称是否出现 ..... 9
9 从 Step101 继续：三种合理的科研终点 ..... 9
10 跨会话接口与原稿定位 ..... 9
11 结果交付与论文标准 ..... 10

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

\section*{3 已经取得的主结果及其逻辑位置}

\section*{3.1 精确 Einstein 的统一拓扑间隙}

定理3．1（原稿审读支持的主定理）。设 $X$ 是闭极小一般型复曲面，$b_{+}(X)>1, A=c_{1}^{2}(X)>0$ ，并令
$$M=X \# k \overline{\mathbb{C P}}^{2}, \quad k \in \mathbb{Z}_{\geq 0}$$
存在与 $X, k$ 无关的 $\gamma \in(0,1 / 3)$ ，使
$$k \geq(1 / 3-\gamma) A \quad \Longrightarrow \quad M \text { 不承载任何 Einstein 度量. }$$
来源与状态：2026－09－15 进展包第1节；Codex 对 Yau26＿uniform＿gap．tex 的逐段审读报告［12，13］。报告明确主证明不依赖（SC），并检查了能量规范、覆盖重数与族统一常数。本文沿用这一审读支持状态，不将其降为＂没有证明的猜想＂；完整投稿证明须取自原稿，不能仅引用本文概述。

最接近的已核对外部基线是 LeBrun Corollary 3.4 的 $k \geq A / 3$ 不存在性［2］。新命题的增量是跨越 $X, k$ 变化仍不消失的正宽度，不是 $1 / 3$ 本身。经典逐个严格不等式 $k / A<1 / 3$ 并不排除$k_{i} / A_{i} \uparrow 1 / 3$ ；整数性在 $A_{i} \rightarrow \infty$ 时也不给统一宽度。首创性应围绕这一精确增量查新，不能从尚未查到同式就宣布全球首次。

这是指定无限流形族上的全局不存在性定理。证明使用局部极限不使其变成局部结论；但它仍不是 $P_{4}^{-}$，也不是对所有四维流形的存在性定理。

\section*{3.2 近临界序列的必要退化}

定理3．2（进展包与审读报告中的配套结论）。在上述吹起族中，若 $M_{i}=X_{i} \# k_{i} \overline{\mathbb{C P}}^{2}$ ，
$$\delta_{i}=\delta_{-}\left(g_{i}\right) \longrightarrow 0, \quad d_{i}=\left(\frac{1}{3}-\frac{k_{i}}{A_{i}}\right)_{+} \longrightarrow 0,$$

则对任意固定 $r, v>0$ ，
$$\frac{\operatorname{Vol}_{g_{i}}\left\{p: \operatorname{Vol}_{g_{i}} B_{r}(p) \geq v\right\}}{\operatorname{Vol}_{g_{i}} M_{i}} \longrightarrow 0, \quad \operatorname{diam}\left(M_{i}, g_{i}\right) \longrightarrow \infty .$$
有界直径版本为：$\delta_{-} \leq 1 / 4 、 \operatorname{diam} \leq D$ 时，
$$\delta_{-}^{2}+\left(\frac{1}{3}-\frac{k}{A}\right)_{+} \geq c(D)>0 .$$
来源与状态：进展包第1、3节与 Codex 审读；A03第3－8步提供其临界族前身。变化拓扑时只能断言测度比例塌缩，不能擅自升级为 $\sup _{p} \operatorname{Vol} B_{r}(p) \rightarrow 0$ 。固定拓扑临界族的更强版本应保留其原始额外条件。

定理3．1扩展＂无 Einstein＂的拓扑范围；定理3．2直接限制原题允许的近似输入。这两项互相关联，却不是彼此自动推出。尤其 $d_{i} \rightarrow 0$ 是沿原1／3边界的条件，不能把它照搬到新禁止带内部每个固定比值。

\section*{4 精确主定理的证明机制：必须保留的五个环节}

\section*{4.1 统一平均能量，而非总量紧致性}

假设存在 Einstein 度量。monopole 条件排除非负 Einstein 常数后，归一化为 Ric $=-g$ 。标量曲率估计和式（1．4）给出
$$\operatorname{Vol}_{g} M \geq 2 \pi^{2} A, \quad \int_{M}\left|\operatorname{Rm}_{\text {full }}\right|^{2} d \mu_{g} \leq 16 \frac{\chi(M)}{A} .$$
这里允许 $\operatorname{Vol} M$ 、总曲率能量和直径全部无界。需要统一的是 $\chi / A$ ，而不是 $\chi$ 本身。
Codex 检查的 Noether 输人为 $\chi(X) \leq 5 A+36$ 。其数值可由 $A \geq 2 p_{g}-4 、 \chi(X)=12(1-$ $\left.q+p_{g}\right)-A 、 q \geq 0$ 得到。再用已有的 Einstein 必要条件 $k \leq A / 3$ 及正整数 $A \geq 1$ ，
$$\frac{\chi(M)}{A} \leq 5+\frac{36}{A}+\frac{1}{3} \leq \frac{124}{3}<42 .$$
所以可统一取 $L=42$ 。这一步没有循环使用新 $\gamma$ 定理。若改为其他 monopole 流形族，首先要重新证明相应的 $\chi / A$ 界。

\section*{4.2 同时选择低能量与低平均缺陷的固定尺度中心}

设 $H \geq 0$ ，并令 $\mathcal{A}_{r} H(x)=\operatorname{Vol}\left(B_{r}(x)\right)^{-1} \int_{B_{r}(x)} H$ 。在统一 Ricci 下界及固定有界尺度下， Bishop－Gromov 局部倍增和 Fubini 给出
$$\int_{M} \mathcal{A}_{r} H(x) d \mu(x) \leq C_{\mathrm{BG}} \int_{M} H d \mu$$
证明时用 $y \in B_{r}(x)$ 导致 $\operatorname{Vol} B_{r}(x)$ 与 $\operatorname{Vol} B_{r}(y)$ 在统一倍增常数内可比，再交换积分。无需绝对体积下界。

由 Markov 不等式，平均全曲率不超过固定倍数 $C_{0}$ 的中心占据固定正比例；对非负近等号密度也可同时选择局部均值很小的中心。将两个坏集比例各压到 $1 / 4$ ，交集仍有至少 $1 / 2$ 的体积比例。Ricci 下界又给 $\operatorname{Vol} B_{r} \leq V_{-1}(r)$ ，故选取仅依赖 $C_{0}$ 的小固定 $r$ ，可将局部绝对 $L^{2}$ 能量压入下述正则性阈值。

这是 $r=r(L)>0$ ，不是依序列变化的 $r_{i} \rightarrow 0$ 。保留原尺度使后续极限仍有非零 Einstein 常数，避免放大后只得到 Ricci－flat 而丢失局部矛盾。

\section*{4.3 允许塌缩的正则性究竟给了什么}

Cheeger－Tian 的四维精确 Einstein 小能量估计，经 Ge－Jiang Theorem 1.1 明确重述：Ric＝ $\lambda g 、|\lambda| \leq 3$ ，在 $r \leq 1$ 的球上 $\int|\mathrm{Rm}|^{2} \leq \varepsilon$ ，则内球 $\sup |\operatorname{Rm}| \leq C r^{-2} ; \varepsilon, C$ 不依赖球体积下界$[3,4]$ 。范数换算只改变固定常数。

它给固定尺度曲率有界，并不说随着绝对能量趋零，塌缩球上的曲率必趋零。也不直接给底空间注入半径下界。接下来需要在足够小的无共轭半径内拉回度量，获得受控的局部展开片。

\section*{4.4 展开不必单射：小平均缺陷如何传输}

引理4．1（缓冲局部等距映射的重数传输）。设 $\pi:(\widetilde{U}, \widetilde{g}) \rightarrow(U, g)$ 是局部等距映射。给定中心及半径 $s$ ，假设需要的长度不超过 $2 s$ 的路径均可从 $\widetilde{B}_{s}$ 内原像提升，且提升留在 $\widetilde{B}_{3 s} \Subset \widetilde{U}$ 。对 $x, y \in B_{s}$ ，假设它们可由上述路径连接；记 $n_{s}(x)$ 为 $x$ 在 $\widetilde{B}_{s}$ 的原像数，并假设面积公式适用。则对 $F \geq 0$ ，
$$\int_{\widetilde{B}_{s}} \pi^{*} F \leq \frac{\operatorname{Vol}\left(\widetilde{B}_{3 s}\right)}{\operatorname{Vol}\left(\widetilde{B}_{s}\right)} \int_{B_{s}} F .$$
证明。从 $x$ 的每个小球原像提升同一条 $x$ 到 $y$ 的路径。唯一提升及反向提升保证这些终点互异，故 $n_{s}(x) \leq n_{3 s}(y)$ 。对 $y \in B_{s}$ 积分，得到
$$n_{s}(x) \operatorname{Vol} B_{s} \leq \int_{B_{s}} n_{3 s}(y) d \mu(y) \leq \operatorname{Vol} \widetilde{B}_{3 s}$$
于是 $\int_{\widetilde{B}_{s}} \pi^{*} F=\int_{B_{s}} F n_{s} \leq\left(\operatorname{Vol} \widetilde{B}_{3 s} / \operatorname{Vol} B_{s}\right) \int_{B_{s}} F$ ，除以 $\operatorname{Vol} \widetilde{B}_{s}$ 即得。实际指数展开中需另外检查定义域、缓冲及局部等距拉回；本证明没有假设全局单射或正规覆盖。 \(\square\)

来源与状态：这是 Codex 所述重数机制的显式化。原稿中的球选择与缓冲条件仍应逐项对应；不能将本引理用于不具有路径提升空间的抽象多值参数化。

受控展开片上的体积比有统一界，故底空间的小平均密度能传到展开片。仅知道底空间绝对积分小则不够：$U \times S_{\ell}^{1}$ 的固定密度积分可随 $\ell \rightarrow 0$ 消失，展开后密度却不变。

\section*{4.5 禁止的是开集 Einstein 模式，而不是单点代数数据}

临界近等号迫使展开后的光滑极限具有
$$\operatorname{Ric}=-g, \quad s=-4, \quad \operatorname{Spec}\left(W^{+}\right)=(-1 / 6,1 / 12,1 / 12) .$$
设简单本征形式为定长 $\omega$ ，常数谱给 $W^{+}=\mu \mathrm{Id}+(\lambda-\mu) P_{\omega}$ 。由 Einstein 条件 $\operatorname{div} W^{+}=0$ ，展开乘积法则后先与 $\omega$ 收缩得 $\operatorname{div} \omega=0$ ，再由非零自对偶二形式在四维的非退化性得 $\nabla \omega=0$ 。于是$\nabla W^{+}=0$ 。这也与 Derdziński Proposition 5 一致［5］。

但式（4．5）给 $\left|W^{+}\right|^{2}=1 / 24$ 、 $\operatorname{det} W^{+}=-1 / 864$ 。代入 Einstein－Weyl 恒等式
$$\Delta\left|W^{+}\right|^{2}=2\left|\nabla W^{+}\right|^{2}+s\left|W^{+}\right|^{2}-36 \operatorname{det} W^{+}$$
要求 $\left|\nabla W^{+}\right|^{2}=1 / 16$ ，矛盾。等价地，局部 Kähler－Einstein 谱应为 $(-2 / 3,1 / 3,1 / 3)$ 。这个论证针对开集上持续成立的模式；它不排除某点的代数曲率恰好取同样数值。

\section*{5 把代数缺陷写完整：一组可直接复算的连接估计}

这一节为【本稿重算】，用于接续与交叉校验，不替代原稿中定义不同的密度及109、436、675等常数，也不声明这些代数组合在文献中首次出现。

取适用 LeBrun 估计的 monopole 类 $a$ ，使 $\left(a^{+}\right)^{2} \geq A$ 。此处正投影范数不是类的拓扑自交数$a^{2}=A-k$ 。令 $\omega=\left|W^{+}\right|, w=\lambda_{\text {min }}\left(W^{+}\right)$，
$$\begin{aligned}
I & =\frac{1}{4 \pi^{2}} \int_{M}\left(s^{2} / 24+2 \omega^{2}\right) d \mu_{g}, & J & =\frac{1}{8 \pi^{2}} \int_{M}|E|^{2} d \mu_{g} \\
D_{a} & =I-\frac{2}{3}\left(a^{+}\right)^{2} \geq 0, & q & =k-A / 3, \quad d=(-q / A)_{+}
\end{aligned}$$
Chern－Weil 给 $I-J=A-k$ ，从而
$$D_{a}=J-q-\frac{2}{3}\left(\left(a^{+}\right)^{2}-A\right) \leq J+A d .$$
LeBrun Theorem 2.3 及其证明式（11）分别支持
$$\begin{aligned}
\int(s-\sqrt{6} \omega)^{2} d \mu_{g} & \geq 72 \pi^{2}\left(a^{+}\right)^{2} \\
\int\left(\frac{2}{3} s+2 w\right)_{-}^{2} d \mu_{g} & \geq 32 \pi^{2}\left(a^{+}\right)^{2}
\end{aligned}$$
其中 $u_{-}=\min (u, 0)$ ；全部 monopole 与极化假设必须同时成立［2］。
逐点配方恒等式是
$$27\left(s^{2} / 24+2 \omega^{2}\right)-(s-\sqrt{6} \omega)^{2}=\frac{1}{8}(s+8 \sqrt{6} \omega)^{2} .$$
因此 $\int(s+8 \sqrt{6} \omega)^{2} \leq 864 \pi^{2} D_{a}$ 。设
$$f=\frac{2}{3} s-2 \sqrt{2 / 3} \omega, \quad a_{*}=\frac{2}{3} s+2 w, \quad \mathcal{G}=f^{2}-\left(a_{*,-}\right)^{2} .$$
$w \geq-\sqrt{2 / 3} \omega$ 给 $a_{*} \geq f$ ，所以 $\mathcal{G} \geq 0$ ；又 $\int f^{2} \leq 48 \pi^{2} I$ ，故
$$\int \mathcal{G} d \mu_{g} \leq 48 \pi^{2} D_{a}$$
令 $Q(g)=\int \mid$ Ric $+\left.g\right|^{2} d \mu_{g}$ ，并另外定义密度
$$\Phi_{*}:=|\operatorname{Ric}+g|^{2}+(s+4)^{2}+(s+8 \sqrt{6} \omega)^{2}+\mathcal{G} .$$
因为 $\int(s+4)^{2} \leq 4 Q 、 J \leq Q /\left(8 \pi^{2}\right)$ ，有
$$\int_{M} \Phi_{*} d \mu_{g} \leq 119 Q+912 \pi^{2} A d$$
特别是 $q \geq 0$ 时恢复一个 $119 Q$ 型终端重新校准界；精确 $\operatorname{Ric}=-g$ 时则只有 $912 \pi^{2} A d$ 。
若 $\delta_{-} \leq 1 / 4$ ，标量曲率 monopole 界给 $\mathrm{Vol} \geq 2 \pi^{2} A /\left(1+\delta_{-}\right)^{2}$ 。于是
$$\int_{M} \Phi_{*} \leq 476 \delta_{-}^{2}+456\left(1+\delta_{-}\right)^{2} d \leq 713\left(\delta_{-}^{2}+d\right) .$$
零密度的光滑极限满足式（4．5）：前两项给 Ric $=-g 、 s=-4$ ，第三项给 $\omega=1 /(2 \sqrt{6})$ ，最后一项迫使最小本征值达到迹零对称算子的极值，另外两个本征值相等。

这说明从小 Ricci 缺陷到小平均校准缺陷的代数环节已经可以明确写出。尚未解决的不是＂再找一个平方恒等式＂，而是在任意塌缩的近似方程上取得足以传递这个密度的正则区域。

\section*{6 从精确方程到近似方程：三个可竞争的证明方向}

研究目标6．1（主攻联合间隙）。在指定吹起族内，证明或严格否定存在统一 $c_{*}>0$ ，使所有度量在$\delta_{-} \leq 1 / 4$ 时满足
$$\delta_{-}^{2}+\left(\frac{1}{3}-\frac{k}{A}\right)_{+} \geq c_{*} .$$
不得额外默认有界直径、非塌缩或全曲率上确界。若只能得到带这些条件的版本，则准确记录它加强了哪个已有定理。

\section*{6.1 方向 A：正体积比例的局部展开可达性}

目标不必是＂处处正则＂，而是至少在一组固定正比例、局部平均 $\Phi_{*}$ 趋零的中心上，产生固定尺度受控展开。已知有界 Ricci 的尺度选择［4，Theorem 3．4］可以把小绝对能量转成某个可比尺度上的小归一化能量，但不自动给点态曲率界。Naber－Zhang 与 Jiang—Kong—Xu 需要额外的纤维化秩、模型或局部覆盖几何［7，8］。

真正要证明的是这些额外结构能否由本问题的小校准密度和能量预算获得；或者秩下降、不可展开区域是否必消耗固定正比例的校准缺陷。若构造出同时满足全部预算而不可展开的反模型，就限定这一方向，不重复把覆盖结构当成一般有界 Ricci 的免费结论。

\section*{6.2 方向 B：弱测试张量与直接定量刚性}

寻找不先要求全曲率点态界的估计：将 Ric $+g$ 的导数通过分部积分移到受控测试张量上，用$\mathcal{G}$ 、谱间隔和 Hodge 缺陷控制局部几何。 $\|$ Ric $+g \|_{\infty} \rightarrow 0$ 不控制 $\nabla$ Ric；不能把 Bianchi 恒等式写成点态 $\operatorname{div} W=O(\delta)$ 。

有价值的结果应是明确的＂密度小则有一个禁止模式可被传递的片＂定理，或者一个给定测试空间中的反例。使用有限 $W^{2, p}$ 强收敛往往足够传递二次曲率量，不必强求输入序列 $C^{\infty}$ 收敛。需要说明 $p$ 、规范、边界缓冲及系数紧性的实际来源。

\section*{6.3 方向 C：有控制的局部平滑与终端重新校准}

如果采用局部流，最小需求是得到一个定义在原闭流形上的终端度量，使正比例支撑区上曲率受控，并且 $Q(T) / A \rightarrow 0$ ；再对终端度量重新应用式（5．9）或原稿对应密度。无需分别运输所有初始SW 形式的缺陷。

但这一简化不解决流的共同存在时间、支撑过渡区域和退化系数问题。必须从实际初始数据证明，而不是因为权重代数通过检查就宣称流存在。若该接口的复杂性长期超过直接弱刚性路线，应保存有效引理后调整路线，而不是以＂已经投入几十步＂为理由继续同一闭合循环。

\section*{6.4 同等允许的反向结果}

若在已由定理3．1排除 Einstein 的拓扑上构造 $\delta_{-} \rightarrow 0$ ，则得到真正负分支反例。构造应满足所有临界密度和能量约束；只展示一个塌缩局部模型或某种负 Ricci 度量不够。新禁止带内部的固定$k / A<1 / 3$ 不受 $d \rightarrow 0$ 的同一必要退化结论直接覆盖，可以重新检查，但不能因此预先认定那里容易构造。

\section*{6.5 一个足够完成矛盾、但不要求输入曲率处处有界的接口}

命题6．2（受控谐和片上的密度传递准则）。设假想序列满足 $\delta_{-}\left(g_{i}\right)^{2}+d_{i} \rightarrow 0$ 。假设可选定固定半径的局部展开片及谐和坐标，将其识别到同一个欧氏球 $B_{2}$ ，使拉回度量 $\widetilde{g}_{i}$ 一致正定、具有统一$C^{1, \alpha}$ 控制，且拉回的 $\Phi_{*}$ 在该球的平均值趋零。则这样的序列不可能存在。

证明．先取 $C^{1, \beta}$ 收玫子列，$\beta<\alpha$ 。谐和坐标中的 Ricci 方程主部为 $-\frac{1}{2} g^{a b} \partial_{a} \partial_{b} g_{j k}$ ，其余项只含度量的一阶导数。 $\operatorname{Ric}_{\widetilde{g}_{i}}+\widetilde{g}_{i} \rightarrow 0$ 一致成立，因此分布极限满足 $\operatorname{Ric}_{g_{\infty}}=-g_{\infty}$ 。内点椭圆估计先给任意有限 $p$ 的 $W^{2, p}$ 控制，随后极限的 Einstein 方程给光滑性。对差分方程再次应用统一椭圆估计，在更小球上得到强 $W^{2, p}$ 收玫；取 $p>4$ 即足够传递本文全部二次曲率密度。于是 $\Phi_{*}\left(g_{\infty}\right)=0$ ，得到被式（4．5）排除的 Einstein 开集。 \(\square\)

该命题的分析含义是：最终需要的是一个小密度受控片，不是把所有输入度量变成有界曲率。真正待证的是这样的片能否在任意塌缩序列中找到，以及底空间平均值能否传到同一片。它不与A02 的尖峰构造矛盾，因为尖峰例并不满足本主线的趋零禁止谱密度。

\section*{7 必须保留的300步技术积累及其当前边界}

\section*{7．1 旧 IL 连接和族与新吹起族不能混成一个范畴}

旧研究还处理 $M=\left(\#_{j=1}^{m} X_{j}\right) \# N, m=2,3$ ，使用
$$A=\sum_{j} c_{1}^{2}\left(X_{j}\right), \quad D=4 m-(2 \chi+3 \tau)(N), \quad 2 \chi(M)+3 \tau(M)=A-D .$$
相应临界参数是 $D / A$ ，某些具体例子中 $D=k+4$ 或 $k+8$ ，不是一律 $k / A$ 。Bauer－Furuta 给出全符号类的条件须从 Ishida－LeBrun 原文逐项恢复［11］。

临界近等号记录包括 $\operatorname{Vol} / A \rightarrow 32 \pi^{2} / 9 、 \int\left|W^{+}\right|^{2} /\left(\pi^{2} A\right) \rightarrow 4 / 27$ 、正负投影收敛及多形式空间相分离。这些是有用的几何约束。一般符号平均应写为实际投影范数的和；不能把 $\left(K_{X}^{+}\right)^{2}$ 无理由等同于 $A$ 。固定 $A$ 的绝对误差趋零与变化 $A_{i}$ 时的 $o\left(A_{i}\right)$ 必须区分。

\section*{7.2 选择支撑、加权 Moser 与共同时间}

用 $a=\zeta^{2}$ 表示截断权重，避免与 Euler 数 $\chi(M)$ 混淆。旧路线的有效代数骨架是
$$K_{p}=\int a^{p-2} \mathcal{K}^{p}, \quad Z_{p}=a^{(p-1) / 2} \mathcal{K}^{p / 2}, \quad K_{3 p / 2} \leq K_{p}^{1 / 2} K_{2 p}^{1 / 2} .$$
它来自精确 Cauchy－Schwarz 配权，而不是将 $\left\|Z_{p}\right\|_{3}^{3}$ 错当成 $K_{3 p / 2}$ 。梯度耗散含 $a^{p-1} \mathcal{K}^{p-2}|\nabla \mathcal{K}|^{2}$ 。实指数的 Kato 正则化与主系数 $a \mapsto a+\varepsilon$ 是不同操作；每一步极限都需统一估计。

归一化 Sobolev 常数与小能量的乘积可以在选择支撑上抵消塌缩体积因子，但不能据此宣布全局无权 Sobolev 常数统一。有界 $a E$ 只在 $a=1$ 的平台给无权控制；过渡区仍可能是最难部分。每个数据存在 $T_{i}>0$ 不等于存在统一 $T_{0}>0$ 。全阶导数分配脚本仅验证列举与代数，不证明 PDE的存在、延拓和极限。

\section*{7.3 终端几何与全局闭性}

多个中心不能各自演化后被当成同一个终端闭度量。需要一个由不交支撑／着色构造的全局权重及一套共同流。Ricci 流没有有限传播速度；区域远离初始坏点不足以使该区域自动不受影响。SW／Chern－Weil 的终端应用要求同一闭流形与规范一致的度量，不能只在若干片上重新定义。

\section*{8 Prior－art 审计：要回答的不是名称是否出现}

\begin{tabular}[t]{|l|l|l|}
\hline 最近来源 & 已有内容 & 本项目需要确认的增量 \\
\hline LeBrun［2］ & $1 / 3$ 不存在性与 SW 曲率估计 & 指定无限族的统一 $\gamma$ 是否已有等价定理或直接推论；不把尖锐积分式等同于尖锐 Einstein 阈值。 \\
\hline Cheeger－Tian［3］ & 精确4维 Einstein、无体积下界的小能量正则性 & 与近饱和缺陷及展开重数传输组合后，是否产生此前未有的族一致结论。 \\
\hline Derdziński［5］ & harmonic $W^{+}$的两本征值局部结构 & 禁止谱本身是经典机制；新增重点应在量化强迫和跨退化传递。 \\
\hline Ge－Jiang［4］ & 精确定理复述、有界 Ricci 尺度选择 & 不重新命名已有尺度选择；真正新增接口是近似方程下的正则／密度传递。 \\
\hline Anderson、 Naber－Zhang［9，7］ & 不同附加假设下的紧性与正则性 & 逐项核对附加条件，不能从题名推断可解决本题；核查既有推论是否覆盖统一间隙。 \\
\hline
\end{tabular}

按定理相互蕴含关系查新：保持同一范畴、同一归一化、同一常数依赖；检索拓扑近饱和、monopole 退化、局部密度、Einstein 塌缩及最小体积文献的交叉，而不是仅搜索＂uniform topologygap＂。未获得全文的文章标为来源待核，不替它补写定理。

\section*{9 从 Step101 继续：三种合理的科研终点}

第一次接续先核对主原稿、Codex 审读对应版本和最近会话修正，冻结定理3．1的真实陈述与依赖图。若原稿已有本文件概述中缺省的细节，不重复造证明；若发现具体缺口，写清楚失效位置和受影响结论。接着将式（5．9）－（5．10）与原密度逐项比对，选择更简洁、适用范围更清楚的版本。

若精确结果和必要退化完整且查新支持，第一种终点是完成一篇以统一拓扑间隙及定量近等号退化为核心的投稿稿。不能把第一稿的价值取决于尚未解决的式（6．1）；也不为追求期刊名人为添上未经证明的广泛推广。

第二种终点是实质加强式（6．1）：在三个竞争方向中选择一个最小分析接口，先证明真实输入上的统一版本，再推广范畴。可先获得覆盖可达的正比例定理、受控秩下降代价或保留密度的平滑定理；这些要明确说明排除了哪些先前仍开放的序列。

第三种终点是构造满足全部预算的逃逸模型，并与 A03 的全局拓扑机制拼接。模型失败时，只排除该模型，不宣布一般塌缩不存在。A02 提供的曲率尖峰必须作为正则性压力测试保留，但它的底层本来有 Einstein 度量，不能误当此处的拓扑反例。

每次路线分叉用一条可判真的命题决定，而非预先耗满 100 步。论文整理、证明推进和新方向探索允许切换；切换应由证据触发，禁止重复宣布＂只差一个标准技术步骤＂而未展示该步骤。

\section*{10 跨会话接口与原稿定位}

A01 持有本主线主定理与密度；A02 持有近似构造和正则性反例；A03持有同一光滑拓扑的全局存在／不存在性。交接只需要准确的输入、输出、常数依赖与可用版本，不能传递＂同伴已突

破＂的评价替代数学。
主原稿（优先读取）qiushi＿engine＿v08／users／user2／Sessions／S0910A03／workspace／brie fing／Yau26＿uniform＿gap．tex

累积研究稿 Skills／qiushi－yau26／references／research／20260912．tex
旧 IL 组装（逐模块核对状态）Sessions／S0910A01／workspace／notes／step68＿restricted＿ IL＿canonical＿assembly．md
终端重新校准 Sessions／S0910A01／workspace／notes／step67＿terminal＿recalibration＿re covery．md

选支撑的独立模块 Sessions／S0910A01／workspace／notes／step70＿selected＿support＿lemma． md

实指数缺陷 Moser Sessions／S0910A01／workspace／notes／step70＿defect＿moser＿real＿exp onent．md

共同 bootstrap Sessions／S0910A01／workspace／notes／step55＿joint＿bootstrap＿backgro und＿continuation＿repair．md

局部禁止谱与退化 Sessions／S0910A03／workspace／notes／step6＿local＿projector＿obstruct ion＿and＿collapse＿reduction．tex

平均传输的修正版 Sessions／S0910A03／workspace／notes／step8＿cover＿mean＿transport＿and ＿model＿scope＿corrections．md

以上为轨迹提供的工作区定位，不表示这些原稿字节已经收进本交付包。A03第31－60步的加权估计、选择支撑、正则化与延拓笔记保留为条件性技术储备；使用时以最后修正为准，不从早期＂完成＂标签倒推证明状态。

\section*{10.1 必须继承的纠错}

纯 $W^{+}$独立下界的早期推导已撤回；不丢弃符号不利的梯度项，不把 $F_{A}^{+}$当成调和形式。compact Armstrong 定理不直接用于非紧正则片。平均缺陷传输要保留重数。Noether 比例界不等于全局体积界。正 Ricci 给体积上界，不给体积下界。旧的 $A^{-1 / 2}$ 界仅限制特定旧链，不能否定新精确统一间隙。Min－Oo 旧论证的来源争议没有解决前，不把其存在性当作本主线依赖［10］。

\section*{11 结果交付与论文标准}

研究结论以具体命题和证明为单位，而不是以 Agent 数量、步数或平台认可次数为单位。同一公式在多个会话复算，可以提高证据质量，不产生多项独立新发现。

可完成的结果应及时冻结成可独立阅读的数学稿：准确的假设与量词，新增结论相对最接近文献的差别，所有分析接口及常数依赖，完整证明，必要时附有限计算及独立复算说明。假设增多或结论缩小必须在主定理中显式反映。无需等到整个 Yau26 解决才允许发表严谨的中间结果，也不把一个证明链拆成若干缺乏独立贡献的论文。

Annals、Inventiones、JAMS、Acta 可以作为高质量写作与结果强度的目标，但任何文件都不预设已达到其录用标准。完整性、首创性、重要性和选刊是四项判断。用经典工具证明新的重要定理可以完全原创；出现一个新名称、搜不到同名词或构造了＂框架＂，并不能确认首创性。按精确命题及假设进行查新，并记录最近定理、包含关系及真正新增的证明步骤。

无论本轮选择论文收束还是进一步探索，结束时只需留下四类必要材料：更新后的主定理与证

明；当前最小未闭合命题；确切被否定的模型及原因；可供同伴直接使用的来源、版本和计算。除非出现新的反证或新缺口，不再次从零争论已审读的同一结果。反过来，发现具体错误就修正所有依赖它的结论，而不是只新增一份不被后续读取的纠错说明。

\section*{参考文献}
\begin{itemize}
\item[] ［1］S．－T．Yau，Problem Section，in Seminar on Differential Geometry，Annals of Mathematics Studies 102，Princeton University Press，1982，pp．669－706．历史题页仍需在工作区逐字核对；本稿采用任务书中的区间命题。
\item[] ［2］C．LeBrun，Ricci curvature，minimal volumes，and Seiberg－Witten theory，Invent．Math． 145 （2001），279－316．https：／／arxiv．org／abs／math／0003068．本轮核对 Theorem 2.3 的证明及式（11）、Proposition 3．1－3．2、Corollary 3．4；不把 $1 / 3$ 说成已证明最优的 Einstein 拓扑阈值。
\item[] ［3］J．Cheeger and G．Tian，Curvature and injectivity radius estimates for Einstein 4－manifolds， J．Amer．Math．Soc． 19 （2006），487－525．DOI：https：／／doi．org／10．1090／S0894－0347－05－00511－4．本稿所用精确 Einstein 小能量版本同时由 Ge－Jiang Theorem 1.1 核对。
\item[] ［4］H．Ge and W．Jiang，є－regularity for shrinking Ricci solitons and Ricci flows，arXiv：1707．05511． https：／／arxiv．org／abs／1707．05511．本轮核对 Theorem 1．1、Theorem 3．4；后者为有界Ricci 的尺度选择，不是一般有界 Ricci 的点态曲率结论。
\item[] ［5］A．Derdziński，Self－dual Kähler manifolds and Einstein manifolds of dimension four，Compo－ sitio Math． 49 （1983），405－433，Proposition 5．https：／／www．numdam．org／item／CM＿1983＿＿49＿3＿405＿0／．局部两本征值与恒模长结构；本稿另给出对应一阶投影证明。
\item[] ［6］J．Cheeger and A．Naber，Regularity of Einstein manifolds and the codimension 4 conjecture， arXiv：1406．6534．https：／／arxiv．org／abs／1406．6534．引用须区分有界 Ricci 的非塌缩正则片与精确 Einstein 的更强正则性。
\item[] ［7］A．Naber and R．Zhang，Topology and $\epsilon$－regularity theorems on collapsed manifolds with Ricci curvature bounds，Geom．Topol． 20 （2016），2575－2664．https：／／doi．org／10．2140／gt． 2016．20．2575．最大纤维化幂零秩、模型几何等输入不能省去；本稿不宣称这些输入已由夹逼推出。
\item[] ［8］W．Jiang，L．Kong and S．Xu，Convergence of Ricci－limit spaces under bounded Ricci curvature and local covering geometry I，arXiv：2205．00373．https：／／arxiv．org／abs／2205．00373．localcovering geometry 是额外结构；具体使用前核对版本与定理。
\item[] ［9］M．T．Anderson，Ricci curvature bounds and Einstein metrics on compact manifolds，J．Amer． Math．Soc． 2 （1989），455－490．https：／／doi．org／10．1090／S0894－0347－1989－0999661－1．本轮确认文献身份，未取得所需 Corollary B（4）的完整原文；不得据二手概述填写其假设或用它排除输人曲率尖峰。
\item[] ［10］R．Ye，Ricci flow，Einstein metrics and space forms，Trans．Amer．Math．Soc． 338 （1993）， 871－896．https：／／doi．org／10．1090／S0002－9947－1993－1108615－3．项目记录提示其对Min－Oo 投影论证的修正；本稿不据尚未核准的旧存在性陈述建立结论。
\end{itemize}
\begin{itemize}
\item[] ［11］M．Ishida and C．LeBrun，Spin manifolds，Einstein metrics，and differential topology， arXiv：math／0107111．https：／／arxiv．org／abs／math／0107111．Proposition 4 与 Theo－rem 7 为旧 IL 连接和路线来源；实际应用前逐项核对 Bauer－Furuta／模 4 等原始假设，不能只保留拓扑比值。
\item[] ［12］Qiushi Engine 项目资料：2026－09－15 进展包、2026－09－16 逐步归档，S0910A01／A02／A03 各100步 meta－trace；源文件名与本地工作区定位见正文。原稿、脚本与摘要须分别识别，不能把记录中的成功标签视作外部定理。
\item[] ［13］用户在本会话提供的 Codex 原稿审读报告（截至2026－09－16）：Sessions／S0910A03／worksp ace／briefing／Yau26＿uniform＿gap．tex，重点位置原稿约第277行；另核查 A02 第83步构造笔记。结论为在所审读依赖链中未发现实质缺口，且精确拓扑间隙不依赖（SC）。本引用是审读报告的来源定位，不声称原稿全文已包含于归档。
\end{itemize}
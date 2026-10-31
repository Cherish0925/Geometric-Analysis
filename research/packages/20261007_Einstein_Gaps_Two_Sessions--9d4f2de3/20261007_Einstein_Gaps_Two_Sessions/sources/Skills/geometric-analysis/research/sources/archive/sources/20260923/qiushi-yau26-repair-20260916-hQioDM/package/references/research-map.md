# Ricci 夹逼研究地图

这份地图把问题、证明和来源对应起来。十二个主题是阅读入口，不是全部成果或全部缺口的计数。正文中的条件定理、局部反例和未完成构造均有研究价值；没有重新进行文献查新，不等于撤回已有数学，也不构成首创性认证。

记 $\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{\infty,\mathrm{op}}$。工作命题在固定维数为 $Q_n\Longleftrightarrow P_n^+\lor P_n^-$，输出允许同一光滑流形上的任意 Einstein 度量。完整否定只须在一个固定维数同时否定两分支，两序列可用不同流形；单支反例不够。原始历史题文与本文明确采用的工作表述仍须区分。

下文状态描述保留内容的范围：**完整正文**（full）指列明假设下的陈述与论证俱在；**合并**（merged）指重复或较弱版本并入明确的新版本；**模型内**（model-only）指结论只针对所写几何、代数或数值模型；**已撤回**（withdrawn）指来源中某个明确错误的推论已被后文替代；**未给出**（missing）指所需数学尚未出现，不把研究目标当成证明。完整正文不表示所有应用接口、发表检验或整个 Yau 26 已完成。

## 本地正文与来源版本

| 简称 | 本地完整材料 | 主要来源与版本 |
| --- | --- | --- |
| F | [问题与研究基础](../research/20260910.tex) | 量词、经典方法和条件边界的综合稿 |
| L | [长篇构造与分析](../research/20260912.tex) | 上传 `Yau26_source_package/Yau26_synthesis.tex`；SHA-256 前缀 `1bfb842faab5f56f`；不是三条续接稿的摘要 |
| U | [统一拓扑间隙](../research/20260916_uniform_gap.tex) | 上传 `Yau26_uniform_gap.tex`；源哈希前缀 `bf171ca3deeb712a` |
| R | [刚性与退化](../research/20260916_rigidity.tex) | 2026-09-16 三主线稿 `01_A01_统一拓扑间隙与近Einstein刚性.tex`，源哈希前缀 `7aebf229b5b1dd2f`，及三 Session 原始推导 |
| C | [近 Einstein 构造](../research/20260916_construction.tex) | 同组 `02_A02_点态近Einstein解消与Weyl匹配.tex`，源哈希前缀 `76b6f8bf6ae162c1`，及 A01/A02 后期原始推导 |
| G | [全局几何与拓扑](../research/20260916_global.tex) | 同组 `03_A03_全局拓扑兼容与反例闭合.tex`，源哈希前缀 `9f8b92323d732589`，及 A03 Step 63–100 |

TeX 定位采用原有 `\label{...}` 或完整节名，便于全文搜索，不依赖会随编辑移动的行号。A01、A02、A03 分别指 `S0910A01`、`S0910A02`、`S0910A03`；其 `Step k` 是各自独立的原始 Step，不能混成同一时间轴。网页累计记录的 §1–322 则是章节号，不能等同于任一个 Session 的 Step。

上传源均来自 A03 的 `workspace/briefing/`。2026-09-15 `Yau26_parallel_progress`、2026-09-16 `Yau26_full_research_archive_2026-09-16` 的逐步日志与分类表用于追踪版本，不替代正文证明。L 的源附带 `CURATION.md` 明确了累计章节到数学专题的对应；这里沿用这个来源定位，并对重要证明块直接对照正文。

## 1. 精确 Einstein 的统一拓扑间隙

完整正文：U `thm:intro-exact`、`thm:exact`；R `thm:topgap` 为合并陈述。对极小一般型复曲面 $X$、$b_+(X)>1$、$A=c_1^2(X)>0$，存在与 $X,k$ 无关的非显式 $\gamma>0$，使 $k\ge(1/3-\gamma)A$ 时 $X\#k\overline{\mathbb{CP}}^2$ 无任何 Einstein 度量。

证明的可复用环节均在 U：`eq:budget-general` 的校准预算；`lem:fubini` 的选点；`lem:transfer` 的带缓冲局部等距展开及重数传输；精确 Einstein 小能量正则性；`lem:forbidden` 的局部禁谱。一般形式在 $\mathrm{MP}(A)$、$\chi\le LA$ 下给 $(2\chi+3\tau)/A\ge2/3+\eta(L)$。Noether 不等式先给 $L=42$，再得统一 $\gamma$，并非逐个 $X$ 的严格性。

来源：U 上传独立证明稿；A01 Step 4–14、A03 Step 3–12 的近等号与展开研究提供相关背景。U 的**精确定理不依赖 (SC)**；`prop:conditional` 才假设任意塌缩有界 Ricci 度量具有统一的原度量弱调和片。把 (SC) 的未证性倒灌成精确 $\gamma$ 定理缺口，或由精确定理宣称所有近 Einstein 输入都有统一 Ricci 间隙，都是不同命题间的误用。

## 2. 固定 A1 解消上的 log-Weyl 构造

完整正文：L `FND:A1construction`、`FND:Hstar`、`FND:logoperator`；C `thm:A1` 及“完整构造的数学结构”。固定闭 Einstein 四轨形、节点、取向、端部标记和 EH 填充后，核心修正解 $D\operatorname{Ric}_{g_{EH}}\widetilde h=g_{EH}$；共同径向规范下二次项之差 $K$ 是 Ricci 核中的 Weyl 方向，且

$$D\operatorname{Ric}_e[\eta(\log r)K]=-\frac{\eta''+6\eta'}{2r^2}K.$$

内核、对数环带、外截断的完整非线性误差推出固定光滑解消上的 $\delta_\sigma(g_a)\le C/|\log a|\to0$，并有外部 GH 极限及放大 EH 核极限。这是无权点态端同态范数，不是有限 $L^p$ 残差。

来源：上传长稿累计早期及 §55–85 的局部构造；三主线 A02 稿；原 A02 Step 60–70、83 的共振通量与近夹逼构造。ADE、type T、Wahl 和四次延拓是不同扩展，见后面的“进一步的独立子结果”。未给出：任意指定解消的 all-sign Einstein 不存在性；精确障碍只排除某个渐近匹配族，不能替代它。

## 3. 固定 Dehn-twist 曲面丛 $E_D$

完整正文在 L `BUN:chapter`，不是只有 G 的概述。来源为上传累计 §223–270、274–275、279–280、282、288–289；对应长稿的整块构造、TT 配对和共形证明保留。主要层次如下。

- `BUN:slow`、`BUN:ricci-matrix`、`BUN:slow-bound`：先固定总空间，$h_1=D^*h_0$，在基底长领圈慢插值；全部 Ricci 块给 $\delta_-(G_\ell)=O(L^{-1})$、固定体积。混合分量没有被忽略。
- `BUN:double`、`BUN:balanced-profiles`、`BUN:exact-second`：纤维参数 $\varepsilon$ 与基底参数 $\beta=\varepsilon^2$ 平衡，$I_R\to\pi/2$、$J_L\to\pi$，精确首项为 $\delta_-(G_\varepsilon)=2\varepsilon^2/\pi^4+O(\varepsilon^4)$。
- `BUN:three-equations`、`BUN:B-solution`、`BUN:bianchi`、`BUN:decay`：把真实二阶源拆成三个标量方程，两个强制势算子有正下界，第三个显式求解；验证 Bianchi、尾项与闭流形截断，得到 `BUN:third-bound` 的 $O(\varepsilon^3)$。
- `BUN:global-pairings`、`BUN:nonlinear-obstruction`：使用闭基底的真实 TT 张量，并保留非 Einstein 背景的伴随缺陷。`BUN:whole-conformal-third` 配合任意正共形因子的 bootstrap 给指定校正背景整个共形类的 $\inf_u\delta_-(u^2\widetilde G_\varepsilon)=\Theta(\varepsilon^3)$。
- `BUN:fifth-volume` 保留五阶体积首项；`BUN:negative-ritz` 与 `BUN:corrected-ritz` 区分原始、校正背景谱；`BUN:exact-product-gap`、`BUN:closed-log-loss` 给闭乘积去全核后的真实 $L^\infty$ 逆损失，不能以好的 $L^2$ 谱隙取代。

模型内而非 all-metrics：`BUN:conformal` 还利用未改动的乘积开集排除这些共形类中任意符号的 Einstein 度量。其他共形类没有被排除。L `BUNTOP:Einstein-necessary` 的体积窗、正截面和 Weyl 谱必要条件也不是全部不存在性证明。G“曲面丛上的近Einstein构造与全局问题”只是导航与综合。

## 4. 近等号 Weyl 轮廓、禁谱与必要退化

完整正文：U `eq:density`、`eq:calibration`、`lem:forbidden`、`thm:local`、`thm:proportion`、`cor:diam`；R“Seiberg--Witten近等号的解析分解”。$\mathcal D=0$ 强迫 $\operatorname{Ric}=-g$ 与 $\operatorname{spec}W^+=(-1/6,1/12,1/12)$；散度零使简单特征线平行，局部 Kähler 曲率范数与该谱矛盾。这是开集上的微分刚性，不是说该点态代数谱本身不存在。

U 的具体预算为 $\fint\mathcal D\le436\delta^2+675d$，$d=(1/3-k/A)_+$。相应近边界序列必须在归一化体积测度意义下塌缩，且直径趋无穷；不宣称每点一致塌缩或序列已经构造。R `eq:109`、`eq:436675` 与 `eq:119` 分别保留不同联合密度的常数，不能混换定义。

来源：A01 Step 4–14、A03 Step 3–12；U 独立稿及上传归档“04_详细推导_IL临界分支与校准”。R 另保留旋量缺陷、两次 Hölder、调和投影、Walsh 极化及空间相分离（`eq:spinor-deficit` 至 `eq:walsh`）。未给出：任意塌缩输入上的统一正密度；低能量球可选不等于统一弱调和片已建立。

## 5. 固定超临界比例的负夹逼下界

完整正文：L `FND:SWgap`。设 $K=k+4\ell$、$c=c_1^2(X)$、$r=K/c-1/3$，保留所引 LeBrun 定理的极化和 monopole 假设，在 $c/3\le K<c$ 得

$$\delta_-(g)\ge\Phi(r)=\begin{cases}\sqrt{r/2},&r\le2(2-\sqrt3)^2,\\2\sqrt r/(\sqrt6+\sqrt r),&2(2-\sqrt3)^2\le r<2/3.\end{cases}$$

证明保留 Ricci 特征值箱体顶点优化以及 $\int|\operatorname{Ric}^\circ|^2$ 与 Chern--Weil 预算。因此固定 $p=K/c>1/3$ 不能给负缺陷趋零；变化比例接近 $1/3$ 时此下界趋零，不产生上界或度量。小缺陷还给 $K/c\le1/3+2\delta^2$ 和超临界整数性限制。

来源：上传长稿早期一般筛选及累计 §115、212；A01/A03 初期临界预算。较弱的旧分式界在其 $1/3<p<1$、$\delta<1$ 范围内可用，现合并进精确箱体版本；不把它延长到使分母失去符号的参数区。这个结果与主题 1 的非显式、低于 $1/3$ 的精确 Einstein 统一间隙不同。

## 6. ALE 首障碍、无规范通量与临界尺度

完整正文／模型内：C `eq:firstobs` 给 refined 家族 $g_t=t(g_{cal}+th)$ 的物理首项 $\lambda h_t^{-1}o+o(1)$。非零首障碍在固定核心留下阶一端同态误差，不能把核心缩小就消掉。它约束固定渐近匹配，不约束主题 2 的跨对数尺度 Weyl 漂移。

C `sec:ellflux` 及 `eq:ellfluxbound` 对平锥上全部角向扰动证明无规范 Wronskian 配对。对齐次次数 $\ell\ge2$，对偶质量为 $J_{K_\ell}\int_b^Rr^{1-\ell}dr$：仅二次模给无权 $1/\log(R/b)$，高次模给幂律。`eq:nonlinearflux`、`eq:energyflux` 保留一次分部积分后的非线性与加权能量误差；固定球面失配的锐系数另有完整推导。

来源：L `FND:flux`、`FND:nonlinearflux`、`FND:energyflux`；A02 Step 34、42、46–50、59–74；上传归档“05”和“07”。已撤回的是从 $|\mathcal O_i|\le C\delta_i\log(1/t_i)+o(1)$ 无条件推出 $\mathcal O_i\to0$；还须控制乘积 $\delta_i\log(1/t_i)$。C `sec:c0pairing` 的质量 $O(t_i)$ 测试张量是明确的待证替代，不是任意泡树已有的投影定理。

## 7. Calderón--Zygmund 型全曲率尖峰

完整正文：C“小Ricci缺陷与全曲率尖峰”、`eq:CZ`；A02 Step 11 的解析构造。紧支撑的反向双翘曲使基底 Ricci 的 Hessian 相消，垂直 Ricci 只见 $\Delta u$ 与一阶项，而混合 Riemann 分量仍见 $u_{xy}$。取
$w_\sigma=-XY\log(X^2+Y^2+\sigma^2)/2$、$u_j=\Lambda_j^{-2/3}\psi w_{e^{-\Lambda_j}}$，得到 $\delta_+=O(\Lambda_j^{-2/3})$ 与中心 $|\operatorname{Rm}|\gtrsim\Lambda_j^{1/3}$，全局度量仍光滑正定。

来源与复算：[step11_cz_spike_analytical.py](computations.md#step11_cz_spike_analytical-py)；数值变体仅辅助。应保留的修正是：固定区域内**扰动曲率的** $L^2$ 范数趋零，总曲率能量趋于非零乘积背景能量。先缩小背景区域可得到小局部总能量，不能声称固定球或整个闭流形总能量沿该序列趋零。底层 $S^2\times S^2$ 本有 Einstein 度量；反驳的是过强的输入正则性推断，不是 Yau 26，也不是塌缩例。

## 8. BCGP 的 $\mathbb Z_4^2$、$K^2=2$ 六节点例

完整正文：R“产品商面的平滑与Einstein存在性”，特别 `eq:reflexive`、`eq:qg-obstruction`、`eq:H2zero`；C“一个乘积商的全局平滑与Einstein度量”。原 A01 Step 49 的存在性机制在 Step 50 保留条件，Step 51 `step51_reflexive_bridge_einstein_existence_proof.md` 补反射切层桥；Step 52 扩展特征标比较。

具体分支数据给 $g(C_1)=g(C_2)=3$、六个 A1 点、$K_{X_0}^2=2$。证明包括准 étale 商上的 $T_{X_0}=(\pi_*T_Y)^G$、有限映射与不变量的上同调交换、等变 Serre/Künneth 及列明特征标，得到 $H^2(X_0,T_{X_0})=0$；不是误用 $H^2(T_S)=0$。Lee--Park 的局部到全局 QG 平滑打开全部节点，典范丛下降与丰沛性开放给平滑纤维 $K$ ample；Aubin--Yau 给负 KE，ADE 同时解消及 Ehresmann 把它放回标准复方向最小解消的同一 smooth type。

结论允许改变复结构：原解消复曲面上的 $(-2)$ 曲线仍说明其原 $K$ 不 ample。不能推广到任意混合手性光滑填充。$S_5,K^2=4$ 四节点比较、$H^2$ 的二维值及 $\beta:\mathbb C^4\to\mathbb C^2$ 的核只是一阶信息，尚不保证全坐标非零或高阶提升；其他扫描行也不是完整 BCGP 分类。有限群计算见 [step51_reflexive_bridge_verify.py](computations.md#step51_reflexive_bridge_verify-py)，几何桥由正文承担。

## 9. 正曲率乘积商的手性、$q_{diag}$ 与四节点

完整正文中的模型恒等式：C `sec:fullkernel`、`sec:greenjet`、`sec:chiralitytable`、`eq:samechiralityblocks`。A01 Step 94 修正 AA/BB 张量模，95–97 区分规范、源锥和核平面，99 核对真实电／磁模的遗漏 jet，100 `step100_chirality_cancellation_proof.md` 给逐谱层有限代数证明。对规定的不同节点 AA/BB 传输，$B_{++}=B_{--}=0$；该结论不依赖已求和的谱尾，但不包含自作用或完整 AB 源桥。

A02 Step 96、99–100 进入同一模型的四接收端方程。C“对角张量消去与四节点互易窗”保留 $q_{diag}=0$ 的配对消去；$c_{adj}\simeq0.06288499$、$c_{diag}\simeq-0.03545352$、$q_{adj}\simeq0.00800500$ 仍为谱截断数值。相邻平衡行必须 $|c_{adj}+c_{diag}|\le q_{adj}$，其他所列混合行必须 $|c_{adj}|\le q_{adj}$；严格否定还须有小于显示裕量的谱尾界。

五行按保持邻接关系的方形节点置换分类，是一行相容加四行混合；固定背景下未把整体手性反转当成几何等价，`----` 没有列入。旧“全五行混合”“任意互易集合有交则含 1”以及用迹方向零响应检验无迹方向的说法已被准确版本替代。

未给出：C `eq:LS` 的完整 $F^{self}+F^{deform}+F^{inter}+F^{complement}+\mathcal R$、所需 $o(t^3)$ 或全部同阶项、退化比例和方向控制。即使完整局部无零点也只排除该退化邻域。复算见 [A01 的代数证明程序](computations.md#step100_chirality_cancellation_proof-py)、[A02 四节点程序](computations.md#step100_four_node_closure_and_q_diag-py)；存档数值成功标签不替代上述界。

## 10. 正分支有限型与条件 orbifold/ALE 极限

完整正文：C `sec:coveramplifier` 的经典有限型推论。固定 $\delta_0<1$、$\operatorname{Vol}\ge v>0$ 后，Myers、体积比较及四维非塌缩有限性给有限多个微分同胚型。另一个命题以单连通族的统一体积下界为**假设**，用普适覆盖有限型和 $\chi(\widetilde M)=|\pi_1M|\chi(M)$ 放大到一般族；Myers/Bishop 自身不提供该体积下界。

来源：A02 Step 9–10、24–31、73–85；F `sec:frontier` 和 R“近似方程的三个分析问题”保留正则性边界。非塌缩 orbifold/ALE 描述、从实际输入传输核投影、泡树结构和精确 Einstein 极限各需其具体假设。有限型不产生 Einstein 度量，覆盖上的 Einstein 度量也未证明对甲板群不变。精确解消障碍和一般近 Einstein 度量不能未经桥梁直接互换。

## 11. 图流形、环面／圆塌缩、Koiso 芽与双端连接器

本主题含多项独立完整结果，而不是一个已闭合的构造定理。

- G `eq:graphvol`、`eq:graphW`、`eq:graphconcentration`：指定 Di Cerbo 纯双曲块图流形范畴已有 all-sign 无 Einstein 输入；假想近负序列必须体积近饱和、$\fint|W|^2\le8\delta/3$ 而 $\|W\|_\infty\ge(1-3\delta)/\sqrt3$。`eq:graphdiameter` 另需导数控制。L `GLB:graphpinch`、`GLB:diam` 保留网页累计 §317、320–321 的详细推导。
- G `eq:bcg-threshold`：双曲连接和的度二 BCG/CGB 给依赖目标 $\chi$ 的显式正间隙；该下界随 $\chi\to\infty$ 趋零不构造近似输入，也不是维数统一界。
- G `eq:fullRic` 保留 Gaussian 表示的法向、切向、混合全部 Ricci 块；平切片、固定螺旋标架 `prop:helical`、完整双外扩端且自由等距 OT-$T^2$ 的 `thm:OT` 各有证明。它们不涵盖带 twist、奇异轨道、非对称或任意连接器。R `app:reduction` 保留 Nil 正确单调号、实际 Einstein cusp 及圆约化；消去绝对纤维周期不等于控制基底重构。
- G `eq:separator-jacobi`、`eq:separator-schrodinger`、`eq:separator-Q-bound` 把分隔面稳定性、容量与带权 Maxwell 源结合，得到长度无关的分隔面荷上界，不是整个底面的荷趋零。全稳定精确 Koiso 芽及法向能量尖峰说明稳定性不提供所需的法向输运控制；局部解析解的存在时间可依赖数据。
- G `eq:charged-dictionary`、`eq:physical-charge-source`、`eq:charged-taylor`、`eq:charged-logQ`、`eq:charged-noether`、`eq:charged-pairing`：保留非零荷稳定中心、物理荷与坐标荷的区别、正确强迫号、Noether 配对和 Bochner 项抵消。$L\log Q=-18-4Q+e_\perp$ 不产生先前声称的最大原理上界；标量红移反模型也不是完整 Einstein 解。
- G“局部恒等式与共享参数的双端匹配算子”：完整变量的主符号检验、共同中心参数、两侧 Dirichlet-to-Neumann 返回、轨道 holonomy 均保留。符号单射不是 Fredholm 定理、余核刻画或统一逆估计；固定荷局部 $K_X$ 恒等式为运动学恒等式，不是额外闭合方程。
- G `eq:relative`、`eq:relativebound` 是 A03 Step 100 的相对 CGB：$2\int_N|W|^2+12(V_N-V_{rem})=\int_N(|E^\circ|^2+2e-e^2/12)$，此处 $E=\operatorname{Ric}+3g$。近似外部还须保留有符号外部曲率及体积差。`eq:peripheral-rank`、`eq:cusp-tail`、`eq:cusp-cover-scale` 补回具体 `24cdc1.1` 的周边正秩、$V_{tail}=A/3$ 和共同 $N^{-2}$ 缩放；`eq:RN` 要求真正长颈时 $T=\log N-R+O(1)$、$N\gg e^R$。

来源：A03 Step 63–78 连接器、79–87 OT、88–97 带荷稳定性与联合匹配、98–100 全矩阵与全局预算；另见上传归档“08”。Step 99 把闭 $\chi\le0$ 的约 $1.098$ 下界当成有边界连接器目标，已由 Step 100 撤回；局部环面作用不强迫完成图流形 $\chi=0$。保留的下一问题仍是 $\delta\to0$ 的同一参数族、严格伴随障碍或新的全局存在性，而非寻找一个固定有限误差例。

## 12. 低维经典归约与高维开放问题

完整经典归约见 F“低维与特殊结构的边界”：二维用一致化；三维正 Ricci 用 Hamilton，负分支在充分小误差下由 $K_{ij}=(r_i+r_j-r_k)/2<0$ 及几何化得到双曲类型。它们不外推成高维定理。

G“正分支、覆盖与高维乘积”、C“乘积传播只保留输入夹逼”保留 $\delta$ 的乘积最大值公式。正 Einstein 球因子至少二维，直接乘积跳过五维；输入误差的传播不传播 all-sign 无 Einstein，因为未知度量不必分裂。来源：A02 Step 5、24、70–74、94 及上传归档“09_高维_nge5_与乘积传播”。旧“只四维尚待决定”“所有高维已消障”的概括没有相应普遍证明，不作为现行结论。

未给出的是 $n\ge5$ 的一般统一存在机制，而不是禁止高维研究。临界 $L^{n/2}$ 预算、ALE 束、特殊 holonomy 或新拓扑障碍都可继续发展，各自保留条件。高维开放只阻止全维肯定证明；某个固定维数的两分支反例若完成，已足以否定工作命题，不需要另做所有高维。

## 十二主题之外仍有独立内容的证明块

这些内容不能被“局部构造／全局拓扑／解析接口”三个词吸收后只留标题。下表给出实际保留的证明位置以及准确边界。

| 内容 | 本地证明定位与当前范围 | 来源版本 |
| --- | --- | --- |
| 严格 Hitchin--Thorpe 端点与复／辛正分支 | L `FND:HT`、`FND:positive`：Ricci 比值 3 的端点、等号线丛和指定几何类别归约；不称为一般存在性的最优阈值 | 累计早期一般筛选 |
| ADE 全余核、type T、Wahl | L“共线周期的 ADE 核”“零 Kähler 周期与 type T 平滑”，处理完整 $3b_2$ 核；Wahl 自由商给 $T^*\mathbb{RP}^2$ 和最低阶构造；`FND:quarticbound` 的增强另以四次延拓为输入 | 累计 §55–85；C 相应合并节 |
| 标量逆、局部 Hessian 端点、变分通量 | L `FND:weightedscalar`、`FND:Hessian`、`FND:volumevariation`：$0<\mu<2$ 的加权逆，真实近核排除全局 $\mu=2$；局部端点仍保留实际误差幂次及常标量体积抵消 | 上传长稿完整块，不以摘要替代 |
| 普通点短把手与不要求内部对称的边界障碍 | L `FND:short-handle`、`FND:covervolume`、`FND:boundarymean`；长薄把手不由短把手结论排除，平均曲率阈值须保留既定外端 jets 与拓扑条件 | 累计 §213–222 |
| Berger 精确小核与失败延拓 | L `FND:berger`：局部精确负 Einstein 核、指定双轴延拓的有限距离奇异及部分三轴限制；局部灵活性与特定延拓失败同时成立 | 累计 §213–222；A03 局部中心研究 |
| 高度四的典范环、全 Artin 参数和 QG 维数 | L `ALG:quadratic`、`ALG:allartinlocal`、`ALG:QG`、`ALG:ext38`、`ALG:allartinring` 保留显式模型的关系与 38/0 计算；`ALG:moduliconditional` 的全模栈下降仍有独立假设 | 累计 §58、61、70、73–74、79、90、99、102–104、112–120、133、135、139、144 |
| 自然形变障碍与等模例外 | L `ALG:noniso`、`ALG:isotrivial`、`ALG:localglobal`、`ALG:wahlquotient`、`ALG:redundancy`、`ALG:heightn`；整族 $h^2=1$ 已被等模的 2、3 维例外替代；`ALG:naturalconditional` 的比较与重构不是由典范覆盖 Ext² 自动推出 | 同一代数支线，较弱／错误版本并入后期准确版本 |
| SW 饱和、全部普通 monopole 类和体积账本 | L `GAU:SW-to-KE`、`GAU:ordinary`、`GAU:four-term`、`GAU:ratios`；全类识别保留实际固定外部收敛及核心同调前提 | 累计 §85–211 的规范分析 |
| 临界分析与外部响应 | L `GAU:bundle-gradient`、`GAU:Hessian-critical`、`GAU:Kuranishi`、`GAU:Dirac-gap`、`GAU:external-Jacobi`、`GAU:residue-constant`；有限泡树与固定背景等条件保留，核正交不会把一阶残差平方 | 同一规范支线；Lorentz--Kuranishi 回缩为条件命题 |
| 局部 KE 抵消、泡周期及全奇点评价 | L `GAU:local-KE`、`GAU:net-flux`、`GAU:period-local`、`GAU:all-point-zero`；`GAU:gap-conditional` 还需全部极限分类及有限点评价单射，不等于任意 Einstein 度量不存在 | 累计规范支线的后期版本 |
| 退化局部流的有效分析 | R `app:flow`：选支撑、相对 Sobolev、完整张量变分、三组弱能量、精确缺陷齐次性、实指数 Moser、端点体积抵消、最高截断 jet 与背景连接；`eq:H2energy`、`eq:H3energy`、`eq:Qenergy`、`eq:realp`、`eq:weighted-endpoint` 是具体论证位置 | A01 Step 15–48、54–70；A03 Step 13–61；上传归档“06” |
| 局部流的真正剩余部分 | R“共同时间问题与终端校准”、U (SC)：逐数据光滑解、形式能量估计或固定阶正则化不能自行给退化族共同时间和所需终端原度量片。旧无条件封闭说法被替代，完整张量估计没有因此删除 | A01 Step 30、40、55–67 与 A03 Step 40、50、60–61 的修订链 |
| $E_D$ 拓扑与精确全局变分值 | L `BUNTOP:covers`、`BUNTOP:global-values`、`BUNTOP:all-monopoles`、`BUNTOP:SW-four`、`BUNTOP:endpoint`、`BUNTOP:reducible-core`：有限覆盖障碍、Yamabe／能量下确界、条件端点退化及可实现闭乘积核心；一个退化极小化序列不排除别处达到极小值 | 累计曲面丛后期全局块 |
| Weyl 负特征线、谐和压缩核和源项 | L `WYL:balance`、`WYL:closed`、`WYL:kernel`、`WYL:source`、`WYL:nonclosed`；闭性下有刚性，带源时只有平衡；慢插值 Cotton 源确占首阶，绝对趋零不能换成所需相对小量 | 累计 §271、276–278、281、283–286 |
| 适应下沉的结构定理 | L `SUB:blocks`、`SUB:integrable`、`SUB:basic`、`SUB:area`、`SUB:quartic`、`SUB:oscillation`、`SUB:all-product-submersions`：完整曲率块、两种乘积刚性、非 basic 面积与矩恒等式；不是任意 Einstein 度量自动适应给定投影 | 累计 §287、293–301、304–305、309–310、313–314 |
| 协方差与高频反向检验 | L `SUB:negative-covariance`、`SUB:extension-gap`、`SUB:frequency-scaling`、`SUB:TT-source`：精确常负曲率的局部负协方差模型与保留纤维的闭延拓阈值；局部模型不等于闭反例 | 同一下沉支线 |
| 谐和代表、Hodge／杯积边界与最优目标 | L `SUB:harmonic-bochner`、`SUB:area-counterexample`、`SUB:area-parallel`、`SUB:cup-product-bound`、`SUB:one-form-test`、`SUB:hyperelliptic`、`SUB:optimal-target`、`SUB:optimal-nonconformal`：固定源最优目标取得是经典结果；最优并不迫使共形，Hodge 投影也不保逐点可分解性 | 累计 §302、306、311、315、318–319；不是仍待证明“固定源最优目标存在” |
| WP 有效方程 | L `GLB:WPsource`、`GLB:WPbalance`：无强迫长度下降障碍及带源有符号平衡；真实四维强迫与误差尚需从同一几何推导 | 累计 §290 |

## 三个 Session 的实际末端与可继续研究的对象

这里记录来源的末端，不重新分配 Session、不改变其目标、不把 Step 100 倒退成较早的宏观计划。

- A01 Step 100：`step100_chirality_cancellation_proof.md`（源哈希前缀 `936dd3348f91facd`）。保留 AA/BB 同手性消去的有限代数证明。实际末端交接要求在三类资产之间重新比较，而非锁定乘积商：逐估计检查 Step 68 的受限 IL 汇总及 Step 65、67 的流／终端论证，研究双曲 BCG 路线缺的近夹逼输入，或选择五维、AB 结构证明和其他新方法。若继续乘积商，则完整物理源／AB 桥、自作用、补空间和余项仍待建立。统一 $\gamma$ 与近等号分析是已保留的另一成果，不因此删除或宣称全局混合解消已完成。
- A02 Step 100：`step100_four_node_closure_and_structural_vanishing.md`（`2d2ebf49b88bc773`）。保留 $q_{diag}=0$ 与四接收端互易窗。实际交接要求独立核对手性枚举、交换对称、物理对角耦合及 $O(t^{5/2})$ 对 $t^3$ 的压倒关系，并比较严格余项、负镜像系数、局部到全局不存在性或新的直接存在路线；有限代数／谱认证与完整曲率的 Lean 层也分开。现稿修正了“五种混合”用语，没有把这次交接改成全局无解结论。标准复方向负 KE 平滑是另一个问题，不能用来裁决混合填充。
- A03 Step 100：`step100_relative_cgb_graph_budget.md`（`96884dd3d911f364`）。保留相对 CGB、具体周边正秩与共同缩放；继续对象是同一个 $(N,T,R,\text{中心数据},\text{仿射粘合})$ 下的完整矩阵连接器、Weyl 能量、全部 Ricci 块和外部修正，或能覆盖其允许自由度的连续障碍。Step 98 粗网格试验未保存可信连续场与全部真实端点 jets，单一五次插值的停滞不是不存在性。

2026-09-16 三主线上传稿保留更宽的数学组织方式，与上述最后一步并存；它不是把 A01/A02/A03 重新启动为三个固定角色的指令。“三个未闭合接口”只是某次综合的主题归并，不是整包独立数学缺口总数。代数下降、评价单射、任意塌缩正则性、完整混合约化、两端匹配及 all-metrics Einstein 问题各有不同量词。

## 三百步与维护覆盖的对应

下面的区间只压缩研究沿革；一段可含多条并行支线。每个 Session 的 Step 1–100 均已有 canonical relay，逐步索引保留记录哈希、状态和来源，不用重复放入此地图。

| 来源 | 全部 Step 区间与主要数学位置 |
| --- | --- |
| A01 | 1–14：近等号／局部展开（U、R）；15–48：加权局部流及修订（R `app:flow`）；49–53：QG 平滑及特征标（R 产品商面节）；54–70：延拓／Moser／终端校准（R）；71–75：图颈与中心比较（G）；76–100：乘积商、核、Green 响应、手性（C） |
| A02 | 1–10：正分支、非塌缩与障碍范围（F、C）；11–29：CZ、toric/circle 模型和塌缩困难（C、R、计算附录）；30–59：泡树／投影与定向、负支校准（C、R）；60–75：共振通量、对数尺度、高阶模式与乘积（C）；76–100：多节点、源锥、ALE 拓扑预算及最终四节点（C，部分有限实验仅在附录） |
| A03 | 1–12：拓扑预算、Weyl、展开和圆约化（R）；13–61：退化流完整估计及多次延拓修订（R `app:flow`）；62–70：图流形、中心和端点（G）；71–87：各向异性、螺旋及 OT 障碍（G）；88–97：带荷稳定性、Koiso 与联合匹配（G）；98–100：完整矩阵试验、量词纠正和相对 CGB（G、计算附录） |

维护批次 `qiushi-yau26-flat-20260916-6fHNZy` 在 Skill 外保存四份详细来源表：

- `step-index-provenance.json`：三组各 100 条，步号恰为 1–100，总计 300；三份 relay 源哈希前缀依次为 `7db048a11db5007b`、`1ee6ec0bcba16c6b`、`16cc760f30aeb5aa`。
- `embedded-sources.json`：1990 个来源记录，A01 为 612、A02 为 626、A03 为 752，含 300 条 relay 和 49 条网页材料记录；有重复镜像和综合材料，不能解释为 1990 个独立证明。
- `computational-coverage.json`：1014 个计算来源条目，1004 个直接嵌入位置加 10 个同内容引用；实际对应 589 个程序块和 415 个输出块，分别在 [计算方法](computations.md) 与 [实验结果](experiments.md)。
- `omitted-derivatives.json`：79 个明确处置条目，包括 37 个二进制／图像／非文本派生物、1 个可由保留生成器重建的大型规则网格、41 个第三方或生成依赖。不能把“未原样嵌入”全部等同于数学丢失，也不能只凭这些计数声称所有原始论证语义零遗漏。

详细索引是维护证据，不是使用本文数学的隐藏前提。这里的“完整正文”由所定位的实际论证承担；仅留在计算附录的试验、重复版本及明确撤回的推论没有自动升级为定理。若发现尚未由正文覆盖的有价值推导，应按其原始假设补正文，而不是改写来源记录或用关键词命中宣布完成。

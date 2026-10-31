# 点态逼近、全局构造与精确 Einstein 实现

积分间隙、曲率极小化和精确存在性在同一个几何问题中相遇：固定光滑流形上的曲率方程能否实现，能否任意逼近，逼近序列怎样退化。本文保存早期构造与实现研究的完整位置，使它们与后来的 [积分间隙](GAPS_AND_ENDPOINTS.md)、[曲率变分](CURVATURE_VARIATION.md)、[几乎 Kähler 刚性](GOLDBERG.md) 连续衔接。

主要来源是 [9月29日整合数学稿](../archive/originals/2026-09-29/27b3cef6-aeed-442c-9e66-fef1a757828e.tex)，以下以该稿章节标题或 `sec:` 标签定位；早期独立分卷的入口列于文末。这里记录原稿中的命题、构造和证明关系，原始细节仍由对应正文承载。

## 1. 点态问题的原始量词与积分理论的连接

对闭连通光滑 $n$-维流形，记

$$

\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{L^\infty,\mathrm{op}},
\qquad \sigma\in\{-1,1\}.

$$

早期工作命题问：是否存在只依赖维数的非退化 Ricci 区间，使任意承载该区间内度量的流形都承载某个 Einstein 度量。输出要求是同一光滑流形上的存在性，不要求接近输入，也不预设输出 Einstein 常数的符号。

设 $P_n^\sigma$ 表示某个维数常数 $\epsilon_n^\sigma>0$ 使 $\delta_\sigma<\epsilon_n^\sigma$ 推出 Einstein 存在。缩放归约为

$$

Q_n\quad\Longleftrightarrow\quad P_n^+\ \text{或}\ P_n^-.

$$

因此证明一个符号分支便足以建立这一工作命题；否定它则须在同一维数排除两个符号分支。单独构造负号逼近并不自动完成全部量词。

四维中，本文与积分理论直接相连：

$$

\mathcal E(g)\le\fint|\operatorname{Ric}_g-\sigma g|^2\le4\delta_\sigma(g)^2.

$$

所以全度量积分正间隙排除相应点态逼近；反向推理不成立。小积分残差允许小支撑高曲率扰动，不能直接作为点态构造或强紧性输入。

来源：整合稿 “Normalization and the underlying Einstein existence problem”（`sec:normalized-existence`）；[早期点态构造分卷](../archive/originals/2026-09-16/02_A02_点态近Einstein解消与Weyl匹配.tex) §1。

## 2. Ricci 夹逼的拓扑边界与谱限制

早期点态结果保留四个 Ricci 特征值之间的相关性。若 $\sigma\operatorname{Ric}>0$，并且每点

$$

\lambda_{\max}(\sigma g^{-1}\operatorname{Ric})\le3\lambda_{\min}(\sigma g^{-1}\operatorname{Ric}),

$$

则

$$

2\chi(M)>3|\tau(M)|.

$$

特别地，$\delta_\sigma\le1/2$ 足够。代数端点的密度非负来自

$$

\frac{s^2}{24}-\frac{|\operatorname{Ric}^{\circ}|^2}{2}
=\frac{(\sum r_i)^2-3\sum r_i^2}{6}\ge0.

$$

等号只能有特征值 $(3a,a,a,a)$。简单特征线、Euler 数与半 Weyl 消失进一步排除闭流形的等号。这是严格拓扑边界，而非 Einstein 存在定理。

后续 harmonic-Weyl 谱排除识别某些不相容曲率轨道；它们为实际场校准提供背景，但单个标量乘子并不能覆盖整个 Weyl 空间。允许的 Kähler–Einstein 轨道必须保留。

来源：整合稿 “Pointwise Ricci pinching and spectral exclusion”（`sec:early-pointwise-rigidity`）。曲率算子范数与四指标张量范数相差四倍；精确 Einstein 时分别有 $\int|\operatorname{Rm}_{\rm op}|^2=8\pi^2\chi$、$\int|\operatorname{Rm}_{(0,4)}|^2=32\pi^2\chi$。

## 3. 固定轨形解消：让点态 Ricci 残差趋零

固定闭 Einstein 四维轨形 $(M_0,g_0)$，$\operatorname{Ric}_{g_0}=\sigma g_0$，有限个 $A_1$ 点，并固定等变坐标、Eguchi–Hanson 取向和实际光滑填充。原稿构造平滑核心修正

$$

D\operatorname{Ric}_{g_{\rm EH}}\widetilde h=g_{\rm EH},\qquad
\widetilde h=H_*+O_2(\rho^{-2}),

$$

在共同径向规范中与外部二次项匹配，得到同一个标记解消 $M$ 上

$$

\delta_\sigma(g_a)\le C/|\log a|\longrightarrow0.

$$

同时保留轨形 GH 极限与重标度 EH 核心极限。

核心修正不可省略：裸 $a^2g_{\rm EH}$ 的端同态残差为 $-\sigma I$，缩小体积不能消除它。原稿利用精确双轴 Einstein 核心族的参数微分，获得原尺度所需的 Ricci 补偿。

内外二次项之差在共同规范中为纯 Weyl 张量

$$

K_{ij}=-\tfrac13C_{ikjl}x^kx^l,

$$

其全部十维 Weyl 方向满足精确截断恒等式

$$

D\operatorname{Ric}_{e}[\eta(\log r)K]
=-\frac{\eta_{tt}+6\eta_t}{2r^2}K.

$$

宽对数环带使导数为 $O(|\log a|^{-1})$，再配合核心、ALE 尾部和外部正规余项控制得到全域无权估计。

这解释了局部精确解消障碍与点态任意逼近为何能够并存。ADE、type-T、Wahl 等扩展还涉及完整周期余核、商下降及标记；不能从一个 $A_1$ 模型直接推广到任意 ALE 填充。某一匹配邻域没有精确解，也不排除该光滑流形上远离当前构造的 Einstein 度量。

来源：[9月21日构造分卷](../archive/originals/2026-09-21/02_近Einstein构造_闭拓扑与全模态修正_20260921.tex) §§3–4；[原核心证明](../archive/originals/2026-09-17/20260916_construction.tex)。

## 4. 固定曲面丛与一般剪切闭构造

### 固定 Dehn twist 丛

取 $F=\Sigma_p,B=\Sigma_q$，$p,q\ge2$，固定非分离 Dehn twist $D$ 和满射 $u:\pi_1(B)\to\mathbb Z$，定义

$$

E_D=(\widetilde B\times F)/\pi_1(B),\qquad
\gamma(x,y)=(\gamma x,D^{u(\gamma)}y).

$$

其拓扑与归一化量为

$$

\chi=4(p-1)(q-1),\quad\tau=0,\quad b_1=2p+2q-1,
\quad V_0=4\pi^2\chi.

$$

两取向都具有实际辛规范类。构造在固定纤维上选取同面积双曲路径 $h_z$，满足 $h_1=D^*h_0$，在退化基底长领口上缓慢变化：

$$

G_\ell=dt^2+\ell^2\cosh^2t\,d\theta^2+h_{\eta(t/L_\ell)}.

$$

完整 Ricci 矩阵而非仅对角分量给出

$$

V(G_\ell)=V_0,\qquad\delta_-(G_\ell)\to0,\qquad
\|\nabla^m\operatorname{Rm}\|_\infty\le C_m.

$$

注入半径趋零、直径趋于无穷；两端真实 Dehn twist 匹配使光滑总空间不随参数改变。双领口平衡和后续校正提高指定构造的误差阶，但没有转化成对全部竞争度量的非存在性结论。

### 多块、整数剪切与非交换映射类

更一般的固定闭图块粘合使用

$$

\Psi_e(\phi,x)=(-\phi+u_e(x),f_e(x)).

$$

长领口吸收双曲纤维路径的映射类变化；另一支撑区的塌缩圆使非零整数剪切保持拓扑效应而 Ricci 残差趋零。原稿得到

$$

\|G_\ell^{-1}\operatorname{Ric}_{G_\ell}+3I\|_\infty
\le C(|\log\ell|^{-1}+\ell),\qquad
V(G_\ell)=4\pi^2\chi/9.

$$

缩放 $3G_\ell$ 后即为 $\operatorname{Ric}\simeq-g$ 规范。有限固定路径、全部混合 Ricci 项和边界导数匹配构成闭构造的关键。

来源：整合稿 “A fixed surface bundle with arbitrarily small pointwise Einstein defect”（`sec:fixed-bundle-geometry`）、“Fixed multitwist bundles…”；9月21日构造分卷 §§4、7。

## 5. 固定对象的变分值已算出，全部 Einstein 存在性仍独立

对原稿所列非零剪切、无虚 Kähler 结构的固定闭流形 $M$，两取向实际类与上述构造共同给出

$$

\sigma(M)=-8\pi\sqrt\chi,\quad
\inf_{\operatorname{Ric}\ge-g}V=4\pi^2\chi,

$$


$$

\inf\int s^2=64\pi^2\chi,\quad
\inf\int|\operatorname{Ric}|^2=16\pi^2\chi,\quad
\inf\int|\operatorname{Rm}_{(0,4)}|^2=32\pi^2\chi.

$$

前四个相应极值不取得；最后的全曲率极值取得当且仅当存在某个 Einstein 度量，原稿未决定。不能用 Yamabe 上确界或 Ricci 能量不取得，排除别的体积处存在精确 Einstein。

亏格均为 2 的 $E_D$ 具有 $\chi=4,\tau=0,b_1=7$，点态逼近序列体积为 $16\pi^2$。保留的精确负 Einstein 候选窗口为

$$

16\pi^2<V(h)<48\pi^2,\qquad\operatorname{Ric}_h=-h.

$$

它是固定光滑对象上的独立全局存在性问题。已有群论限制还迫使相关剪切流形上的任意 Einstein 输出没有非零局部 Killing 场；这一条件允许完全非对称输出，不能替代不存在证明。

来源：整合稿 `sec:shear-variational`、`sec:shear-global`、`sec:shear-symmetry`；[9月26日研究方案](../archive/originals/2026-09-26/Qiushi_Einstein_研究主线深化与证明方案_20260926.md) §9。

## 6. 周期、实际场和慢 Teichmüller 模态

多实际类的共同饱和产生联合约束，而不只是一组逐类标量不等式。在相应投影预算与饱和条件下，归一化交叉矩阵接近符号相关多面体

$$

\mathcal C_m=\operatorname{conv}\{zz^T:z\in\{-1,1\}^m\}.

$$

额外标量谱控制将可测符号提升到常符号，从而使正周期矩阵接近秩一，并控制交叉形式的第二个正特征值。完整周期平面的紧性仍需要充分多方向的控制：双曲曲面乘积即使精确 Einstein、所有实际 special 类已饱和，周期平面也可逃向无穷。

这种失败由实际慢场进一步量化。对固定面积形式、水平单位速率双曲路径 $h_v$，令 $G=\gamma+h_{v(x)}$，$k_v=\partial_vh_v$、$N_v=\partial_vk_v-k_vh_v^{-1}k_v$。完整误差为

$$

E_{HH}=(K_\gamma+1)\gamma-\tfrac14|k_v|^2dv\otimes dv,
\quad E_{HV}=0,
\quad E_{VV}=\tfrac12k_v\Delta v-\tfrac12N_v|dv|^2.

$$

基底双曲时，精确能量式为

$$

\int|\operatorname{Ric}_G+G|^2
=\tfrac14\int_B(\Delta v)^2+\int_B\Xi(v)|dv|^4,
\quad\Xi(v)\ge(16V_F)^{-1}.

$$

没有只依赖幅度的势项，因为每个常参数都给精确乘积。循环覆盖上的固定幅度 $v_m=a\cos(2\pi z/m)$ 满足 $\delta_-=\Theta(m^{-2})$、未归一化残差能量 $\Theta(m^{-3})$，但模参数振幅不趋零。

同一族的两个实际规范缺陷精确等于

$$

q_+=q_-=\frac9{4V}\int_B|dv|^2+\frac92\fint|\operatorname{Ric}+G|^2.

$$

因此实际周期完全正确、非零恒长谐和形式、很小的局部误差仍不能强迫标记纤维结构全局恒定。到保纤维产品类的距离可保持正值；没有由此得到到全部 Einstein 度量的正距离，因为这些流形本身已经承载精确乘积度量。

来源：整合稿 `sec:period-inertia`、`sec:periods`、`sec:positive-planes`、`sec:slow-moduli`、`sec:moduli-gauge`。完整慢场、连接变量、基底核及法向逆的统一非线性约化仍是比单参数恒等式更强的任务。

## 7. 精确非紧模型、连接器与完整修正方程

早期稿还有实际完整非紧 Einstein 八参数族，建立在两个双曲柱面、固定角周期和已标记边界数据上。参考族残差在紧化方形四边消失，乘积因子分解使其进入加权反演空间；移动参考规范、全非线性修正和 Bianchi 恢复共同给 $\operatorname{Ric}=-g$。八参数是边界与核参数，不等于已分类八个互不等距模参数。

另一项精确结论是：在所述光滑共形紧、完整负 Einstein 范畴，全紧化上的自由等距圆作用迫使共形边界连通。原稿保留非平凡圆丛和扭转，使用辅助 Lorentz 约化的非负零向 Ricci 或相应 Riemannian 论证。显式双端 Kottler 型近似族却可使残差趋零，说明精确无解不能自动推出统一正间隙。

闭修正需要同时求解补空间方程和全部低模方程。Schur 补必须保留外部响应，不能只检查局部核心的投影；任意小但非零的非对称模态也不能当作规范自由度删去。后验收缩准则只有在完整函数空间逆界、正定性、边界和规范恢复均验证后，才给精确 Einstein 输出。

来源：9月21日 [构造分卷](../archive/originals/2026-09-21/02_近Einstein构造_闭拓扑与全模态修正_20260921.tex) §§5、8–11；[全局判定分卷](../archive/originals/2026-09-21/03_全局Einstein判定_对称破缺与原题闭合_20260921.tex) §§6–7。

## 8. 已形成的受控精确实现链

整合稿从有界直径、体积正下界、单手性超临界 Weyl 控制与拓扑排泡出发，建立调和坐标紧性和同一光滑类型的 Einstein 输出。后续 “Bounded-geometry realization without gauge saturation or Weyl bounds” 进一步陈述：

$$

\pi_2(M)=0,\quad\operatorname{diam}g\le D,\quad V_g\ge v,
\quad\delta_\sigma(g)<\epsilon(D,v)
\Longrightarrow\exists h\text{ on }M:\operatorname{Ric}_h=\sigma h.

$$

该版本的核心是完整 Ricci-flat ALE 核心嵌入障碍，不再需要单手性 Weyl 界。正分支的直径可由 Bonnet–Myers 给出；负分支的实际正投影预算可提供体积下界。直径与非塌缩在此仍是实质输入。

实际场近饱和还给更特殊的输出：

| 输入范畴 | 小量 | 同一光滑流形上的结论 |
|---|---|---|
| aspherical，直径有界，单侧实际共形供给及正投影预算 | $\delta_-+\mathfrak D_2/V$ | 负 Kähler–Einstein |
| 两取向实际共形供给，直径有界，至少一侧统一正投影 | $\delta_-+q_++q_-$ | 局部为 $\mathbb H^2\times\mathbb H^2$，两全局平行复结构 |
| $T_+=3T_->0$，实际供给 $p\ge T_+$，直径有界 | $\delta_-$ | 复双曲度量 |

在陈数边界，数值关系自动强迫饱和和另一手性曲率小，不需另加几何同伦或 Weyl 假设。相应有限覆盖版本把能量先下降，在底空间完成紧性；它不依赖覆盖度数，也不要求覆盖上的复结构直接下降。输出可仅是底空间的局部对称 Riemannian 度量。

来源：整合稿 `sec:compact-realization`、`sec:ale-boundary`、`sec:gauge-ke`、`sec:bilateral`、`sec:chern-boundary`、`sec:virtual-realization`。这些近似到精确的命题与无直径积分间隙互补，不应互相替换输入。

## 9. 当前连接的边界与共同研究问题

去直径的双圆盘实现不能直接从受控定理推出：固定剪切逼近族已显示相应退化可能保留非 Kähler 拓扑。复双曲陈数边界 $\chi=3\tau>0$ 是另一个精确问题，现有剪切族不属于它；删除直径仍需处理有限体积长颈、塌缩和填充。

轨形平滑方向必须恢复整个核心的相对标记及实际场跨尺度信息。只分类末端 ALE 泡，或只有全局缺陷趋零，均不足以推出核心尺度上的非零场与正确 Milnor 填充。原稿的尺度比条件是一个已证充分条件；其自动成立已被特定退化例否定。

与后期研究的关系是明确的：积分 gap 给不可逼近区域；低成本构造改变全度量极值的候选答案；周期与慢模态解释某些紧性为何失效；受控实现把允许的极限几何变成同一光滑对象上的精确解；Goldberg 则在已经满足 Einstein 方程时研究相容辛结构的可积性。它们共享曲率相容性与全局结构，但不存在“解决一个便自动解决其余”的推论。

续接时应保留这些已经形成的不同结论：$E_D$ 的全部负 Einstein 存在性、一般退化下的精确实现、全度量最优曲率值和闭负 Goldberg 仍分别需要自己的决定性证明连接。

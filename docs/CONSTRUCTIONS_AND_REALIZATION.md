# 点态逼近、全局构造与精确 Einstein 实现

本文研究固定光滑流形上的 Einstein 方程、点态逼近及其退化。构造与精确实现同 [积分间隙](GAPS_AND_ENDPOINTS.md)、[曲率变分](CURVATURE_VARIATION.md)、[几乎 Kähler 刚性](GOLDBERG.md) 通过实际场和曲率方程相联系。

主要来源是 [9月29日整合数学稿](../archive/originals/2026-09-29/27b3cef6-aeed-442c-9e66-fef1a757828e.tex)，以下以章节标题或 `sec:` 标签定位，并在相应章节链接独立分卷。

## 1. 点态问题的原始量词与积分理论的连接

对闭连通光滑 $n$-维流形，记

$$
\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{L^\infty,\mathrm{op}},
\qquad \sigma\in\{-1,1\}.
$$

记 $Q_n$ 为如下命题：存在只依赖维数的实数 $a_n<b_n$，使任意承载 $a_ng\le\operatorname{Ric}_g\le b_ng$ 的闭光滑 $M^n$ 都承载某个 $\operatorname{Ric}_h=\lambda h$。这里 $h$ 位于同一光滑流形，$\lambda\in\mathbb R$；$h$ 与输入 $g$ 的距离和 Einstein 常数符号均不受指定。

设 $P_n^\sigma$ 表示某个维数常数 $\epsilon_n^\sigma>0$ 使 $\delta_\sigma<\epsilon_n^\sigma$ 推出 Einstein 存在。缩放归约为

$$
Q_n\quad\Longleftrightarrow\quad P_n^+\ \text{或}\ P_n^-.
$$

因此任一符号分支成立即蕴含 $Q_n$；反例须在同一维数分别否定两个分支。每个分支的反例均要求逼近流形不承载任何 Einstein 度量。

四维中，记 $V=\operatorname{Vol}(M,g)$、$s=\operatorname{tr}_g\operatorname{Ric}$，定义

$$
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|^2dV_g}{\lambda^2V}.
$$

取 $\lambda=\sigma$ 得

$$
\mathcal E(g)\le\fint|\operatorname{Ric}_g-\sigma g|^2\le4\delta_\sigma(g)^2.
$$

这里 $\fint=V^{-1}\int$。Ricci 使用张量范数，$W^\pm$ 使用其在自对偶或反自对偶二形式上的算子范数。全度量积分正间隙因此排除相应点态逼近。小积分残差则容许小支撑高曲率扰动，给出的几何控制较弱。

来源：整合稿 “Normalization and the underlying Einstein existence problem”（`sec:normalized-existence`）；[早期点态构造分卷](../archive/originals/2026-09-16/02_A02_点态近Einstein解消与Weyl匹配.tex) §1。

## 2. Ricci 夹逼的拓扑边界与谱限制

令 $\chi(M)$、$\tau(M)$ 分别为 Euler 数与签名。若 $\sigma\operatorname{Ric}>0$，并且每点

$$
\lambda_{\max}(\sigma g^{-1}\operatorname{Ric})\le3\lambda_{\min}(\sigma g^{-1}\operatorname{Ric}),
$$

则

$$
2\chi(M)>3|\tau(M)|.
$$

特别地，$\delta_\sigma\le1/2$ 足够。记 $r_i>0$ 为 $\sigma g^{-1}\operatorname{Ric}$ 的四个特征值，$\operatorname{Ric}^{\circ}=\operatorname{Ric}-sg/4$，则密度非负来自

$$
\frac{s^2}{24}-\frac{|\operatorname{Ric}^{\circ}|^2}{2}
=\frac{(\sum r_i)^2-3\sum r_i^2}{6}\ge0.
$$

等号只能有特征值 $(3a,a,a,a)$，其中 $a=\min_i r_i>0$。简单特征线、Euler 数与半 Weyl 消失进一步排除闭流形的等号。由此得到所述严格拓扑必要条件。

调和 Weyl 方程还给出特定曲率谱区域的排除结果，并用于后续实际场校准。其范围由相应谱条件确定；Kähler–Einstein 谱构成相容的等号模型。

来源：整合稿 “Pointwise Ricci pinching and spectral exclusion”（`sec:early-pointwise-rigidity`）。曲率算子范数平方与四指标张量范数平方相差四倍；精确 Einstein 时分别有 $\int|\operatorname{Rm}_{\rm op}|^2=8\pi^2\chi$、$\int|\operatorname{Rm}_{(0,4)}|^2=32\pi^2\chi$。

## 3. 固定轨形解消：让点态 Ricci 残差趋零

固定闭 Einstein 四维轨形 $(M_0,g_0)$，$\operatorname{Ric}_{g_0}=\sigma g_0$，有限个 $A_1$ 点，并固定等变坐标、Eguchi–Hanson 取向和光滑填充标记。原稿构造平滑核心修正

$$
D\operatorname{Ric}_{g_{\rm EH}}\widetilde h=g_{\rm EH},\qquad
\widetilde h=H_*+O_2(\rho^{-2}),
$$

在共同径向规范中与外部二次项匹配，得到同一个标记解消 $M$ 上

$$
\delta_\sigma(g_a)\le C/|\log a|\longrightarrow0.
$$

该族以 Gromov–Hausdorff 意义趋于原轨形，核心重标度后趋于 Eguchi–Hanson（EH）度量。$O_2$ 表示包括前两阶导数的渐近控制。

裸 $a^2g_{\rm EH}$ 的端同态残差为 $-\sigma I$。精确双轴 Einstein 核心族的参数微分提供相应线性修正，使原尺度 Ricci 残差趋零。

内外二次项之差在共同规范中为纯 Weyl 张量

$$
K_{ij}=-\tfrac13C_{ikjl}x^kx^l,
$$

其中 $C$ 为 Weyl 代数曲率张量、$e$ 为欧氏度量。令 $t=\log r$，则全部十维 Weyl 方向满足截断恒等式

$$
D\operatorname{Ric}_{e}[\eta(\log r)K]
=-\frac{\eta_{tt}+6\eta_t}{2r^2}K.
$$

宽对数环带使导数为 $O(|\log a|^{-1})$，再配合核心、ALE 尾部和外部正规余项控制得到全域无权估计。

局部精确解消障碍与上述点态逼近使用不同的匹配条件。向 ADE、type-T、Wahl 填充推广时，还需分别处理周期余核、有限商下降和边界标记。光滑流形上任意 Einstein 度量的存在性则是独立的全局问题。

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

两取向上的辛结构提供实际 Seiberg–Witten 类。构造在固定纤维上选取同面积双曲路径 $h_z$，满足 $h_1=D^*h_0$，在退化基底长领口上缓慢变化：

$$
G_\ell=dt^2+\ell^2\cosh^2t\,d\theta^2+h_{\eta(t/L_\ell)}.
$$

包括混合分量的 Ricci 计算给出

$$
V(G_\ell)=V_0,\qquad\delta_-(G_\ell)\to0,\qquad
\|\nabla^m\operatorname{Rm}\|_\infty\le C_m.
$$

注入半径趋零、直径趋于无穷；两端 Dehn twist 匹配使光滑总空间不随参数改变。双领口平衡和后续校正还提高了该构造的误差阶。该流形上的全部 Einstein 存在性见第5节。

### 多块、整数剪切与非交换映射类

对有限个曲面乘积块，沿连通图粘合其边界，采用固定映射

$$
\Psi_e(\phi,x)=(-\phi+u_e(x),f_e(x)).
$$

其中 $u_e$ 为圆值映射，$f_e$ 为保定向微分同胚。长领口上的双曲路径实现映射类变化；另一支撑区中的圆方向塌缩使固定整数剪切的 Ricci 残差趋零。原稿得到

$$
\|G_\ell^{-1}\operatorname{Ric}_{G_\ell}+3I\|_\infty
\le C(|\log\ell|^{-1}+\ell),\qquad
V(G_\ell)=4\pi^2\chi/9.
$$

缩放 $3G_\ell$ 后即为 $\operatorname{Ric}\simeq-g$ 规范。估计常数依赖有限的固定路径和粘合数据；两端度量及各阶导数匹配。

来源：整合稿 “A fixed surface bundle with arbitrarily small pointwise Einstein defect”（`sec:fixed-bundle-geometry`）、“Fixed multitwist bundles…”；9月21日构造分卷 §§4、7。

## 5. 固定剪切流形的变分值与 Einstein 存在性

对原稿所列非零剪切固定闭流形 $M$，每个有限覆盖均无 Kähler 结构。记 $\sigma(M)$ 为 Yamabe 不变量，与前文符号参数 $\sigma\in\{-1,1\}$ 区别。两取向实际类与构造给出

$$
\sigma(M)=-8\pi\sqrt\chi,\quad
\inf_{\operatorname{Ric}\ge-g}V=4\pi^2\chi,
$$

$$
\inf\int s^2=64\pi^2\chi,\quad
\inf\int|\operatorname{Ric}|^2=16\pi^2\chi,\quad
\inf\int|\operatorname{Rm}_{(0,4)}|^2=32\pi^2\chi.
$$

Yamabe、约束体积、标量平方积分和 Ricci 平方积分这四个极值均不取得。全曲率极值取得当且仅当存在某个 Einstein 度量；这一存在性仍待决定。

亏格均为 2 的 $E_D$ 具有 $\chi=4,\tau=0,b_1=7$，点态逼近序列体积为 $16\pi^2$。任意归一化精确负 Einstein 候选满足

$$
16\pi^2<V(h)<48\pi^2,\qquad\operatorname{Ric}_h=-h.
$$

群论还限制相关剪切流形上的 Einstein 度量：其局部 Killing 场芽空间处处为零。因此剩余候选属于非 Kähler、完全非局部齐性的负 Einstein 几何。

来源：整合稿 `sec:shear-variational`、`sec:shear-global`、`sec:shear-symmetry`；[9月26日研究方案](../archive/originals/2026-09-26/Qiushi_Einstein_研究主线深化与证明方案_20260926.md) §9。

## 6. 周期、实际场和慢 Teichmüller 模态

多个实际类的共同饱和约束其相互交叉配对。在相应投影平方估计与饱和条件下，归一化交叉矩阵接近符号相关多面体

$$
\mathcal C_m=\operatorname{conv}\{zz^T:z\in\{-1,1\}^m\}.
$$

额外标量谱控制将可测符号提升到常符号，从而使正周期矩阵接近秩一，并控制交叉形式的第二个正特征值。完整周期平面的紧性仍需要充分多方向的控制：双曲曲面乘积即使精确 Einstein、所有实际 special 类已饱和，周期平面也可逃向无穷。

慢模态给出另一组显式退化。设 $\gamma$ 为闭基底曲面 $B$ 上的度量，$h_v$ 为闭纤维 $F$ 上固定面积形式、水平且纤维 $L^2$ 单位速率的双曲路径。令 $G=\gamma+h_{v(x)}$、$k_v=\partial_vh_v$、$N_v=\partial_vk_v-k_vh_v^{-1}k_v$。以 $H,V$ 下标表示水平和垂直分量，$E=\operatorname{Ric}_G+G$ 满足

$$
E_{HH}=(K_\gamma+1)\gamma-\tfrac14|k_v|^2dv\otimes dv,
\quad E_{HV}=0,
\quad E_{VV}=\tfrac12k_v\Delta v-\tfrac12N_v|dv|^2.
$$

这里 $K_\gamma$ 为基底 Gaussian 曲率，$\Delta=-\operatorname{div}\nabla$。记 $V_F=\operatorname{Area}(F,h_v)$ 和

$$
\Xi(v)=\frac1{16}\int_F|k_v|^4dA_F+\frac14\int_F|N_v|^2dA_F.
$$

基底双曲时，精确能量式为

$$
\int|\operatorname{Ric}_G+G|^2
=\tfrac14\int_B(\Delta v)^2+\int_B\Xi(v)|dv|^4,
\quad\Xi(v)\ge(16V_F)^{-1}.
$$

每个常参数给精确 Einstein 乘积，因此能量式只含模参数的导数。循环覆盖上的固定幅度 $v_m=a\cos(2\pi z/m)$ 满足 $\delta_-=\Theta(m^{-2})$、未归一化残差能量 $\Theta(m^{-3})$，但模参数振幅不趋零。

在各自取向中，令 $a_\pm$ 为实际规范类，$p_\pm$ 为其正 Hodge 投影能量，定义

$$
q_\pm=\frac1V\left[\frac32\int(s^2+12|W^\pm|^2)-72\pi^2p_\pm\right].
$$

同一族满足

$$
q_+=q_-=\frac9{4V}\int_B|dv|^2+\frac92\fint|\operatorname{Ric}+G|^2.
$$

该族的周期精确固定、谐和代表恒长非零，局部误差趋零，而标记纤维结构保持非零振幅。其到保纤维产品类的距离有正下界。流形本身承载精确产品度量；关于全部 Einstein 度量及任意微分同胚的距离是另一问题。

来源：整合稿 `sec:period-inertia`、`sec:periods`、`sec:positive-planes`、`sec:slow-moduli`、`sec:moduli-gauge`。覆盖次数一致的非线性约化还需同时处理完整慢场、连接变量、基底核和法向逆。

## 7. 完备非紧精确模型、连接器与完整修正方程

早期稿构造了完备非紧 Einstein 八参数族，建立在两个双曲柱面、固定角周期和已标记边界数据上。参考族残差在紧化方形四边消失，乘积因子分解使其进入加权反演空间；移动参考规范、全非线性修正和 Bianchi 恢复共同给 $\operatorname{Ric}=-g$。八参数记录已标记的边界数据和核方向。

另一项精确结论是：在所述光滑共形紧、完备负 Einstein 范畴，全紧化上的自由等距圆作用迫使共形边界连通。原稿保留非平凡圆丛和扭转，使用辅助 Lorentz 约化的非负零向 Ricci 或相应 Riemannian 论证。同一类边界条件下，显式双端 Kottler 型近似族的残差下确界为零，展示了非取得的端点行为。

闭修正的非线性约化同时求解补空间方程与低模方程。Schur 补包含外部响应，低模空间包含实际非对称方向。后验收缩准则使用函数空间逆界、非线性余项界、正定性、边界条件和规范恢复，提供精确 Einstein 解的充分条件。

来源：9月21日 [构造分卷](../archive/originals/2026-09-21/02_近Einstein构造_闭拓扑与全模态修正_20260921.tex) §§5、8–11；[全局判定分卷](../archive/originals/2026-09-21/03_全局Einstein判定_对称破缺与原题闭合_20260921.tex) §§6–7。

## 8. 有界几何与精确实现

整合稿从有界直径、体积正下界、单手性超临界 Weyl 控制与拓扑排泡出发，建立调和坐标紧性和同一光滑类型的 Einstein 输出。后续 “Bounded-geometry realization without gauge saturation or Weyl bounds” 进一步陈述：

$$
\pi_2(M)=0,\quad\operatorname{diam}g\le D,\quad V_g\ge v,
\quad\delta_\sigma(g)<\epsilon(D,v)
\Longrightarrow\exists h\text{ on }M:\operatorname{Ric}_h=\sigma h.
$$

该版本通过完备 Ricci-flat ALE 核心的嵌入障碍获得调和坐标紧性，替代了此前的单手性 Weyl 条件。正分支的直径可由 Bonnet–Myers 给出；负分支的实际类的正投影下界可提供体积下界。直径与非塌缩在此仍是实质输入。

对实际共形单极子输入，令 $p=(a_g^+)^2$，定义

$$
\mathfrak D_2=\frac32\int(s^2+12|W^+|^2)-72\pi^2p,
\qquad T_\pm=2\chi\pm3\tau.
$$

这里 $a$ 为该 Spin$^c$ 结构的实第一 Chern 类。实际共形输入指固定 Spin$^c$ 结构的未扰动方程在输入共形类内处处可解。下表前两行的小量阈值依赖直径上界 $D$ 与正投影下界 $A_0>0$，第三行只依赖 $D$。

| 输入范畴 | 小量 | 同一光滑流形上的结论 |
|---|---|---|
| aspherical，直径有界，单侧逐共形类的单极子解存在性条件及 $p\ge A_0$ | $\delta_-+\mathfrak D_2/V$ | 负 Kähler–Einstein |
| 两取向逐共形类的单极子解存在性条件，$p_+,p_->0$，至少一侧 $p_\pm\ge A_0$，直径有界 | $\delta_-+q_++q_-$ | 局部为 $\mathbb H^2\times\mathbb H^2$，两全局平行复结构 |
| $T_+=3T_->0$，单极子解存在性条件 $p\ge T_+$，直径有界 | $\delta_-$ | 复双曲度量 |

在陈数边界，数值关系与单极子解存在性条件强迫饱和和另一手性曲率小。有限覆盖版本将积分估计按度数归一化后下降，并在底空间完成紧性；阈值依赖底空间直径和归一化正投影下界，与覆盖度数无关。其结论是底空间的局部对称 Riemannian 度量，覆盖上的复结构可不下降。

来源：整合稿 `sec:compact-realization`、`sec:ale-boundary`、`sec:gauge-ke`、`sec:bilateral`、`sec:chern-boundary`、`sec:virtual-realization`。这些实现定理保留各自的全局几何条件，与无直径积分障碍具有不同的适用范畴。

## 9. 退化情形中的实现问题

固定剪切逼近族表明，删除直径后，双圆盘近饱和可以伴随非 Kähler 拓扑。复双曲陈数边界 $\chi=3\tau>0$ 则位于该剪切族之外；其无直径实现涉及有限体积长颈、塌缩与填充，仍待解决。

轨形平滑的已证充分条件保留整个核心的相对标记、实际场的跨尺度信息以及缺陷与核心尺度的比值。特定退化例显示，全局缺陷趋零与该尺度比条件可以分离；一般情形仍需建立核心尺度的非零场和 Milnor 填充对应。

积分 gap 描述不可逼近区域，构造给出曲率极值的上界，周期与慢模态刻画退化，有界几何实现定理则产生同一光滑对象上的精确解。Goldberg 问题在 Einstein 方程已成立的前提下，进一步研究相容辛结构的可积性。这些问题通过实际场与曲率的相容性相连，各自保留独立的存在性或刚性要求。

尚未解决的全局目标包括 $E_D$ 的负 Einstein 存在性、一般退化下的精确实现、目标流形的全度量最优曲率值以及闭负 Goldberg 问题。

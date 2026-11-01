# 点态逼近、全局构造与精确 Einstein 实现

Shuxing Yang, Junyao Wu, Rui Zhao, Hongsheng Chen, Yihao Yang  
Qiushi Engine Team, Zhejiang University · [作者与通讯信息](../AUTHORS.md)

本文研究固定光滑流形上的近 Einstein 度量及其退化，并讨论近似解何时可变形为同一流形上的 Einstein 度量。相关的积分障碍、曲率极值和相容辛结构分别见[积分间隙](GAPS_AND_ENDPOINTS.md)、[曲率变分](CURVATURE_VARIATION.md)与[几乎 Kähler 刚性](GOLDBERG.md)。

主要证明见[Einstein 几何研究总稿](../archive/originals/2026-09-29/27b3cef6-aeed-442c-9e66-fef1a757828e.tex)，各节列出相应章节及独立证明。

## 1. Ricci 夹逼与 Einstein 度量存在性

对闭连通光滑 $`n`$-维流形，记

```math
\delta_\sigma(g)=\|g^{-1}\mathop{\mathrm{Ric}}\nolimits_g-\sigma I\|_{L^\infty,\mathrm{op}},
\qquad \sigma\in\{-1,1\}.
```

记 $`Q_n`$ 为如下命题：存在只依赖维数的实数 $`a_n<b_n`$，使任意承载 $`a_ng\le\mathop{\mathrm{Ric}}\nolimits_g\le b_ng`$ 的闭光滑 $`M^n`$ 都承载某个 $`\mathop{\mathrm{Ric}}\nolimits_h=\lambda h`$。这里 $`h`$ 位于同一光滑流形，$`\lambda\in\mathbb R`$；$`h`$ 与输入 $`g`$ 的距离和 Einstein 常数符号均不受指定。

设 $`P_n^\sigma`$ 表示某个维数常数 $`\epsilon_n^\sigma>0`$ 使 $`\delta_\sigma<\epsilon_n^\sigma`$ 推出 Einstein 存在。缩放归约为

```math
Q_n\quad\Longleftrightarrow\quad P_n^+\ \text{或}\ P_n^-.
```

因此任一符号分支成立即蕴含 $`Q_n`$；反例须在同一维数分别否定两个分支。每个分支的反例均要求逼近流形不承载任何 Einstein 度量。

四维中，记 $`V=\mathop{\mathrm{Vol}}\nolimits(M,g)`$、$`s=\mathop{\mathrm{tr}}\nolimits_g\mathop{\mathrm{Ric}}\nolimits`$，定义

```math
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int_M|\mathop{\mathrm{Ric}}\nolimits_g-\lambda g|^2dV_g}{\lambda^2V}.
```

取 $`\lambda=\sigma`$ 得

```math
\mathcal E(g)\le\mathop{\rlap{-}\int}\nolimits|\mathop{\mathrm{Ric}}\nolimits_g-\sigma g|^2\le4\delta_\sigma(g)^2.
```

这里 $`\mathop{\rlap{-}\int}\nolimits=V^{-1}\int`$。Ricci 使用张量范数，$`W^\pm`$ 使用其作为自对偶或反自对偶二形式上算子的 Hilbert–Schmidt 范数。全度量积分正间隙因此排除相应点态逼近。小积分残差则容许小支撑高曲率扰动，给出的几何控制较弱。

来源：整合稿 “Normalization and the underlying Einstein existence problem”（`sec:normalized-existence`）；[早期点态构造分卷](../archive/originals/2026-09-16/02_A02_点态近Einstein解消与Weyl匹配.tex) §1。

## 2. Ricci 夹逼的拓扑边界与谱限制

令 $`\chi(M)`$、$`\tau(M)`$ 分别为 Euler 数与签名。若 $`\sigma\mathop{\mathrm{Ric}}\nolimits>0`$，并且每点

```math
\lambda_{\max}(\sigma g^{-1}\mathop{\mathrm{Ric}}\nolimits)\le3\lambda_{\min}(\sigma g^{-1}\mathop{\mathrm{Ric}}\nolimits),
```

则

```math
2\chi(M)>3|\tau(M)|.
```

特别地，$`\delta_\sigma\le1/2`$ 足够。记 $`r_i>0`$ 为 $`\sigma g^{-1}\mathop{\mathrm{Ric}}\nolimits`$ 的四个特征值，$`\mathop{\mathrm{Ric}}\nolimits^{\circ}=\mathop{\mathrm{Ric}}\nolimits-sg/4`$，则密度非负来自

```math
\frac{s^2}{24}-\frac{|\mathop{\mathrm{Ric}}\nolimits^{\circ}|^2}{2}
=\frac{(\sum r_i)^2-3\sum r_i^2}{6}\ge0.
```

等号只能有特征值 $`(3a,a,a,a)`$，其中 $`a=\min_i r_i>0`$。简单特征线、Euler 数与半 Weyl 消失进一步排除闭流形的等号。由此得到所述严格拓扑必要条件。

调和 Weyl 方程还给出特定曲率谱区域的排除结果，并用于后续实际场校准。其范围由相应谱条件确定；Kähler–Einstein 谱构成相容的等号模型。

来源：整合稿 “Pointwise Ricci pinching and spectral exclusion”（`sec:early-pointwise-rigidity`）。曲率算子的 Hilbert–Schmidt 范数平方与四指标张量范数平方相差四倍；精确 Einstein 时分别有 $`\int|\mathop{\mathrm{Rm}}\nolimits_{\rm op}|^2=8\pi^2\chi`$、$`\int|\mathop{\mathrm{Rm}}\nolimits_{(0,4)}|^2=32\pi^2\chi`$。

## 3. 固定轨形解消上的一致点态逼近

固定闭 Einstein 四维轨形 $`(M_0,g_0)`$，$`\mathop{\mathrm{Ric}}\nolimits_{g_0}=\sigma g_0`$，有限个 $`A_1`$ 点，并固定等变坐标、Eguchi–Hanson 取向和光滑填充标记。构造中的核心修正满足

```math
D\mathop{\mathrm{Ric}}\nolimits_{g_{\rm EH}}\widetilde h=g_{\rm EH},\qquad
\widetilde h=H_*+O_2(\rho^{-2}),
```

在共同径向规范中与外部二次项匹配，得到同一个标记解消 $`M`$ 上

```math
\delta_\sigma(g_a)\le C/|\log a|\longrightarrow0.
```

该族以 Gromov–Hausdorff 意义趋于原轨形，核心重标度后趋于 Eguchi–Hanson（EH）度量。$`O_2`$ 表示包括前两阶导数的渐近控制。

未经修正的 $`a^2g_{\rm EH}`$ 的端同态残差为 $`-\sigma I`$。精确双轴 Einstein 核心族的参数微分提供相应线性修正，使原尺度 Ricci 残差趋零。

内外二次项之差在共同规范中为纯 Weyl 张量

```math
K_{ij}=-\tfrac13C_{ikjl}x^kx^l,
```

其中 $`C`$ 为 Weyl 代数曲率张量、$`e`$ 为欧氏度量。令 $`t=\log r`$，则全部十维 Weyl 方向满足截断恒等式

```math
D\mathop{\mathrm{Ric}}\nolimits_{e}[\eta(\log r)K]
=-\frac{\eta_{tt}+6\eta_t}{2r^2}K.
```

宽对数环带使导数为 $`O(|\log a|^{-1})`$，再配合核心、ALE 尾部和外部正规余项控制得到全域无权估计。

局部精确解消障碍与上述点态逼近使用不同的匹配条件。向 ADE、type-T、Wahl 填充推广时，还需分别处理周期余核、有限商下降和边界标记。光滑流形上任意 Einstein 度量的存在性则是独立的全局问题。

来源：[近 Einstein 度量的解消与匹配](../archive/originals/2026-09-21/02_近Einstein构造_闭拓扑与全模态修正_20260921.tex) §§3–4；[核心修正的证明](../archive/originals/2026-09-17/20260916_construction.tex)。

## 4. 固定曲面丛与剪切流形上的逼近

### 固定 Dehn twist 丛

取 $`F=\Sigma_p,B=\Sigma_q`$，$`p,q\ge2`$，固定非分离 Dehn twist $`D`$ 和满射 $`u:\pi_1(B)\to\mathbb Z`$，定义

```math
E_D=(\widetilde B\times F)/\pi_1(B),\qquad
\gamma(x,y)=(\gamma x,D^{u(\gamma)}y).
```

其拓扑与归一化量为

```math
\chi=4(p-1)(q-1),\quad\tau=0,\quad b_1=2p+2q-1,
\quad V_0=4\pi^2\chi.
```

两取向上的辛结构提供实际 Seiberg–Witten 类。构造在固定纤维上选取同面积双曲路径 $`h_z`$，满足 $`h_1=D^*h_0`$，在退化基底长领口上缓慢变化：

```math
G_\ell=dt^2+\ell^2\cosh^2t\,d\theta^2+h_{\eta(t/L_\ell)}.
```

包括混合分量的 Ricci 计算给出

```math
V(G_\ell)=V_0,\qquad\delta_-(G_\ell)\to0,\qquad
\|\nabla^m\mathop{\mathrm{Rm}}\nolimits\|_\infty\le C_m.
```

注入半径趋零、直径趋于无穷；两端 Dehn twist 匹配使光滑总空间不随参数改变。双领口平衡和后续校正还提高了该构造的误差阶。该流形上的全部 Einstein 存在性见第5节。

### 多块、整数剪切与非交换映射类

对有限个曲面乘积块，沿连通图粘合其边界，采用固定映射

```math
\Psi_e(\phi,x)=(-\phi+u_e(x),f_e(x)).
```

其中 $`u_e`$ 为圆值映射，$`f_e`$ 为保定向微分同胚。长领口上的双曲路径实现映射类变化；另一支撑区中的圆方向塌缩使固定整数剪切的 Ricci 残差趋零。所得度量满足

```math
\|G_\ell^{-1}\mathop{\mathrm{Ric}}\nolimits_{G_\ell}+3I\|_\infty
\le C(|\log\ell|^{-1}+\ell),\qquad
V(G_\ell)=4\pi^2\chi/9.
```

缩放 $`3G_\ell`$ 后即为 $`\mathop{\mathrm{Ric}}\nolimits\simeq-g`$ 规范。估计常数依赖有限的固定路径和粘合数据；两端度量及各阶导数匹配。

来源：整合稿 “A fixed surface bundle with arbitrarily small pointwise Einstein defect”（`sec:fixed-bundle-geometry`）、“Fixed multitwist bundles…”；近 Einstein 度量构造分卷 §§4、7。

## 5. 固定剪切流形的变分值与 Einstein 存在性

对原稿所列非零剪切固定闭流形 $`M`$，每个有限覆盖均无 Kähler 结构。记 $`\sigma(M)`$ 为 Yamabe 不变量，与前文符号参数 $`\sigma\in\{-1,1\}`$ 区别。两取向实际类与构造给出

```math
\sigma(M)=-8\pi\sqrt\chi,\quad
\inf_{\mathop{\mathrm{Ric}}\nolimits\ge-g}V=4\pi^2\chi,
```

```math
\inf\int s^2=64\pi^2\chi,\quad
\inf\int|\mathop{\mathrm{Ric}}\nolimits|^2=16\pi^2\chi,\quad
\inf\int|\mathop{\mathrm{Rm}}\nolimits_{(0,4)}|^2=32\pi^2\chi.
```

Yamabe、约束体积、标量平方积分和 Ricci 平方积分这四个极值均不取得。全曲率极值取得当且仅当存在某个 Einstein 度量；这一存在性仍待决定。

亏格均为 2 的 $`E_D`$ 具有 $`\chi=4,\tau=0,b_1=7`$，点态逼近序列体积为 $`16\pi^2`$。任意归一化精确负 Einstein 候选满足

```math
16\pi^2<V(h)<48\pi^2,\qquad\mathop{\mathrm{Ric}}\nolimits_h=-h.
```

群论还限制相关剪切流形上的 Einstein 度量：其局部 Killing 场芽空间处处为零。因此剩余候选属于非 Kähler、完全非局部齐性的负 Einstein 几何。

来源：整合稿 `sec:shear-variational`、`sec:shear-global`、`sec:shear-symmetry`；[固定剪切流形的存在性问题](../archive/originals/2026-09-26/Qiushi_Einstein_研究主线深化与证明方案_20260926.md) §9。

## 6. 周期与 Teichmüller 模态

多个实际类的共同饱和约束其相互交叉配对。在相应投影平方估计与饱和条件下，归一化交叉矩阵接近符号相关多面体

```math
\mathcal C_m=\mathop{\mathrm{conv}}\nolimits\{zz^T:z\in\{-1,1\}^m\}.
```

额外标量谱控制将可测符号提升到常符号，从而使正周期矩阵接近秩一，并控制交叉形式的第二个正特征值。完整周期平面的紧性仍需要充分多方向的控制：双曲曲面乘积即使精确 Einstein、所有实际 special 类已饱和，周期平面也可逃向无穷。

慢模态给出另一组显式退化。设 $`\gamma`$ 为闭基底曲面 $`B`$ 上的度量，$`h_v`$ 为闭纤维 $`F`$ 上固定面积形式、水平且纤维 $`L^2`$ 单位速率的双曲路径。令 $`G=\gamma+h_{v(x)}`$、$`k_v=\partial_vh_v`$、$`N_v=\partial_vk_v-k_vh_v^{-1}k_v`$。以 $`H,V`$ 下标表示水平和垂直分量，$`E=\mathop{\mathrm{Ric}}\nolimits_G+G`$ 满足

```math
E_{HH}=(K_\gamma+1)\gamma-\tfrac14|k_v|^2dv\otimes dv,
\quad E_{HV}=0,
\quad E_{VV}=\tfrac12k_v\Delta v-\tfrac12N_v|dv|^2.
```

这里 $`K_\gamma`$ 为基底 Gaussian 曲率，$`\Delta=-\mathop{\mathrm{div}}\nolimits\nabla`$。记 $`V_F=\mathop{\mathrm{Area}}\nolimits(F,h_v)`$ 和

```math
\Xi(v)=\frac1{16}\int_F|k_v|^4dA_F+\frac14\int_F|N_v|^2dA_F.
```

基底双曲时，精确能量式为

```math
\int|\mathop{\mathrm{Ric}}\nolimits_G+G|^2
=\tfrac14\int_B(\Delta v)^2+\int_B\Xi(v)|dv|^4,
\quad\Xi(v)\ge(16V_F)^{-1}.
```

每个常参数给精确 Einstein 乘积，因此能量式只含模参数的导数。循环覆盖上的固定幅度 $`v_m=a\cos(2\pi z/m)`$ 满足 $`\delta_-=\Theta(m^{-2})`$、未归一化残差能量 $`\Theta(m^{-3})`$，但模参数振幅不趋零。

在各自取向中，令 $`a_\pm`$ 为实际规范类，$`p_\pm`$ 为其正 Hodge 投影能量，定义

```math
q_\pm=\frac1V\left[\frac32\int(s^2+12|W^\pm|^2)-72\pi^2p_\pm\right].
```

同一族满足

```math
q_+=q_-=\frac9{4V}\int_B|dv|^2+\frac92\mathop{\rlap{-}\int}\nolimits|\mathop{\mathrm{Ric}}\nolimits+G|^2.
```

该族的周期精确固定、谐和代表恒长非零，局部误差趋零，而标记纤维结构保持非零振幅。其到保纤维产品类的距离有正下界。流形本身承载精确产品度量；关于全部 Einstein 度量及任意微分同胚的距离是另一问题。

来源：整合稿 `sec:period-inertia`、`sec:periods`、`sec:positive-planes`、`sec:slow-moduli`、`sec:moduli-gauge`。下述循环覆盖定理完成了指定乘积范畴中的完整核修复。一般纤维变化仍需同时处理慢场、连接变量和法向方程。

### 保留线性化核的非线性修正与最佳估计阶

固定双曲曲面 $`(B,b)`$、$`(F,f)`$ 和 $`\pi_1(B)\twoheadrightarrow\mathbb Z`$。令 $`B_m`$ 为 $`m`$ 重循环覆盖，$`h_m=b_m+f`$。使用提升的统一局部坐标，置

```math
X_m=C^{3,\alpha}_{\mathrm{uloc}},\qquad
Y_m=C^{1,\alpha}_{\mathrm{uloc}}.
```

在相对于 $`h_m`$ 的调和映射规范中，Einstein 算子的线性化为

```math
L_m=\tfrac12\nabla^*\nabla-\mathring R,\qquad
K_m=\ker L_m=T_{B_m}\oplus T_F,
```

其中 $`T_\Sigma`$ 是曲面上的横截无迹张量空间。全部核由两因子的 Teichmüller 变形积分为精确 Einstein 族

```math
H_m(k)=h_m+k+R_m(k),\quad
\Pi_mR_m(k)=0,\quad
\|R_m(k)\|_{X_m}\le C\|k\|_{X_m}^2.
```

常数不依赖 $`m`$，虽然 $`\dim K_m`$ 随覆盖增长。

在核补空间上，

```math
\|u\|_{X_m}\le Cm^2\|L_mu\|_{Y_m},\qquad \Pi_mu=0.
```

其唯一增长来源是基底上的低频标量模态；迹、混合及共形 Killing 分量具有固定正势。TT 投影由
$`P_Ts=s-D(\delta D)^{-1}\delta s`$ 表示，正势逆与局部椭圆估计给其统一有界性，所以增长的核维数不再引入损失。

因此，对已在调和规范中且 $`\|g-h_m\|_{X_m}<cm^{-2}`$ 的度量，

```math
\boxed{\;
\|g-H_m(\Pi_m(g-h_m))\|_{X_m}
\le Cm^2\|\mathop{\mathrm{Ric}}\nolimits_g+g\|_{Y_m}.
\;}
```

证明是在核补上反演并吸收二次余项；完整精确族使剩余核方程恒等消失。它同时分类该邻域中的全部精确解。

这个二次损失由实际度量达到。取无限循环覆盖上的调和坐标 $`z`$、$`z(\tau x)=z(x)+1`$，则

```math
v_m=\cos(2\pi z/m),\qquad
\Delta v_m=\frac{4\pi^2}{m^2}|dz|^2v_m.
```

对非零 $`q\in T_F`$，张量 $`v_mq`$ 与整个核正交。以幅度 $`\theta m^{-2}`$ 扰动并作二次阶规范修正，得到

```math
\|\mathop{\mathrm{Ric}}\nolimits_{g_m}+g_m\|_{Y_m}\le Cm^{-4},
\qquad
\mathop{\mathrm{dist}}\nolimits_{X_m}(g_m,\{\mathop{\mathrm{Ric}}\nolimits_h=-h\})\ge cm^{-2}.
```

任意靠近的 Einstein 度量均可用统一的调和映射逆放入上述规范，故距离下界包括所有微分同胚拉回的 Einstein 度量。由此排除残差到距离的统一 $`\theta`$ 次估计中 $`\theta>1/2`$ 的情形。每个 $`M_m`$ 本身仍承载 $`h_m`$。

完整证明见[可积核与循环覆盖修复](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/continuation/20260924_integrable_kernel_cyclic_repair.md)。

### 闭路变形与单值表示

对实际曲面丛 $`\pi:M\to B`$，用输入度量的正交 Ehresmann 联络沿闭路 $`\gamma`$ 搬运纤维度量，得到同一纤维上的 $`h_t`$。定义

```math
\mathscr C_g(\gamma)
=\frac12\int_0^1\sup_F\|(h_t^{-1}\dot h_t)^\circ\|_{\rm op}\,dt.
```

若 $`x_0`$ 为起点纤维的 Teichmüller 点，$`\rho`$ 为映射类单值表示，则

```math
d_T(x_0,\rho(\gamma)x_0)\le\mathscr C_g(\gamma).
```

证明对两切向量的长度比求导并积分，直接控制返回映射的拟共形伸缩，无须矩阵同时对角化。

固定纤维亏格和其双曲代表的 systole 正下界后，Teichmüller 厚部模映射类群紧，群作用适当。故存在统一阈值，使同一起点的一组生成闭路全部满足 $`\mathscr C_g<\epsilon`$ 时，单值群包含在一个有限稳定子中。Nielsen 实现及高亏格曲面 $`\mathrm{Diff}_0`$ 的可缩性随后给出原光滑丛

```math
M\cong(\widehat B\times F)/G,
```

并赋予精确双曲乘积商度量。因此原曲面丛承载一个精确 Einstein 度量。

厚度和沿完整闭路的累计量都参与证明。固定 Dehn twist 可以沿越来越长的领口缓慢实现，其局部导数趋零而单值性不变；纤维自身退化时，Dehn twist 的 Teichmüller 位移也可趋零。两种构造分别说明为何局部小量与单值性结论之间不能略去这些条件。

证明及最小纤维黎曼下沉的 Ricci 应用见[闭路变形与单值性](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/continuation/20260924_cycle_holonomy_realization.md)。

## 7. 完备非紧 Einstein 度量与拼接方程

构造得到完备非紧 Einstein 八参数族，建立在两个双曲柱面、固定角周期和已标记边界数据上。参考族残差在紧化方形四边消失，乘积因子分解使其进入加权反演空间；移动参考规范、全非线性修正和 Bianchi 恢复共同给 $`\mathop{\mathrm{Ric}}\nolimits=-g`$。八参数记录已标记的边界数据和核方向。

另一项精确结论是：在所述光滑共形紧、完备负 Einstein 范畴，全紧化上的自由等距圆作用迫使共形边界连通。原稿保留非平凡圆丛和扭转，使用辅助 Lorentz 约化的非负零向 Ricci 或相应 Riemannian 论证。同一类边界条件下，显式双端 Kottler 型近似族的残差下确界为零，展示了非取得的端点行为。

闭流形上 Einstein 方程的非线性约化同时求解补空间方程与低模方程。Schur 补包含外部响应，低模空间包含实际非对称方向。收缩映射定理使用函数空间逆界、非线性余项界、正定性、边界条件和规范恢复，提供精确 Einstein 解的充分条件。

来源：[近 Einstein 度量构造](../archive/originals/2026-09-21/02_近Einstein构造_闭拓扑与全模态修正_20260921.tex) §§5、8–11；[全局判定分卷](../archive/originals/2026-09-21/03_全局Einstein判定_对称破缺与原题闭合_20260921.tex) §§6–7。

### 有限长度连接区域的 Ricci 残差下界

在 Gaussian 坐标中写 $`g=dr^2+q(r)`$，令 $`B=\tfrac12q^{-1}\partial_rq`$、$`H=\mathop{\mathrm{tr}}\nolimitsB`$、$`E=\mathop{\mathrm{Ric}}\nolimits+3g`$。Ricci 的法向方程为

```math
H'+\frac{H^2}{3}+|B^\circ|^2=3-E_{rr}.
```

对连接最小截面 $`H(0)=0`$ 与双曲扩张端 $`H(R)=3`$ 的区域，置 $`u=H-3\tanh r`$，则

```math
\int_0^R\cosh^2r(-E_{rr})\,dr
=3\cosh^2R(1-\tanh R)
+\int_0^R\cosh^2r\left(|B^\circ|^2+\frac{u^2}{3}\right)dr.
```

这个恒等式保留了形算子的全部无迹分量。若 $`\|E\|_{\mathrm{op}}\le\delta`$，标量 Riccati 比较给出必要条件

```math
1\le k\tanh(kR),\qquad k=\sqrt{1+\delta/3}.
```

其最小允许误差在 $`R\to\infty`$ 时为 $`12e^{-2R}(1+o(1))`$。因而有限长度不能精确完成这组边界数据；误差趋零必须允许长度增长。这个法向条件仍须与切向、混合 Ricci 方程和端部匹配共同满足。

### 双曲拼接中的相对曲率与体积恒等式

设闭四流形由有限体积、截面曲率 $`-1`$ 的双曲块截断后拼接而成。令 $`N`$ 为替换区域，外部保留精确双曲度量；$`V_{\rm rem}`$ 是被移去的完整尖点尾部体积。假定拼接保持这些双曲块 Euler 数之和。记 $`V_N=\mathop{\mathrm{Vol}}\nolimits(N)`$、$`e=\mathop{\mathrm{tr}}\nolimitsE`$。对参考双曲块和实际闭度量分别使用 Chern–Gauss–Bonnet，再减去共同外部，得到

```math
\boxed{\;
2\int_N|W|^2+12(V_N-V_{\rm rem})
=\int_N\left(|E^\circ|^2+2e-\frac{e^2}{12}\right).
\;}
```

证明只需代入 $`s=-12+e`$ 与
$`8\pi^2\chi=\int(|W|^2+s^2/24-|E^\circ|^2/2)`$。
若 $`\|E\|_{\mathrm{op}}\le\delta`$，四个特征值均在 $`[-\delta,\delta]`$，所以

```math
\left|2\int_N|W|^2+12(V_N-V_{\rm rem})\right|
\le(8\delta+4\delta^2)V_N.
```

特别地，近 Einstein 替换必须满足

```math
V_{\rm rem}-V_N=\frac16\int_N|W|^2+O(\delta V_N).
```

Weyl 能量可以由移去和插入体积之差抵偿。故仅有 Weyl 非负性不能推出连接区域的统一正能量下界。

对尖点 $`dt^2+e^{-2t}q_*`$，横截面体积 $`A(T)`$ 与尾部体积满足 $`V_{\rm tail}(T)=A(T)/3`$。在一个尖点的 $`N`$ 重循环覆盖中取截断深度 $`T_N=\log N+T_0`$，两者均按 $`N^{-2}`$ 缩小；匹配的二维格商连接区域的体积、Weyl 能量和残差积分也具有同一因子。因此塌缩参数本身不能改变上述无量纲相容关系。外部若仅近似双曲，其曲率积分与参考体积的差必须保留。

两项证明及矩阵值拼接模型的来源分别见[法向 Riccati 比较](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/archive/sources/20260923/v08_S0910A03/workspace/notes/step99_raychaudhuri_cgb_and_cost_structure.md) §1 和[相对 Chern–Gauss–Bonnet 证明](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/archive/sources/20260923/v08_S0910A03/workspace/notes/step100_relative_cgb_graph_budget.md) §§2–5。局部自由环面作用并不使完成后的闭流形 Euler 数为零；相对 Chern–Gauss–Bonnet 公式中的 Euler 数项须按实际闭流形计算。

### 四节点乘积模型的手性相消

在 $`(S^2\times S^2)/\mathbb Z_2`$ 的四个 $`A_1`$ 点上，线性化的张量–标量谱分解提供一个可精确计算的相互作用模型。令 $`D=\mathop{\mathrm{diag}}\nolimits(1,-1)`$、$`O=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)`$。接收端与源端的同手性双线性映射满足

```math
\begin{aligned}
R_+(D,D)&=-D/2,&R_+(O,O)&=D/2,&R_+(D,O)&=R_+(O,D)=-O/2,\\
S_+(D,D)&=-D/4,&S_+(O,O)&=D/4,&S_+(D,O)&=S_+(O,D)=-O/4.
\end{aligned}
```

与单位矩阵的混合输入为零。电、磁张量极化在节点分别为 $`D,O,O,-D`$。若张量因子的源点和接收点对跖，极化项逐对抵消；若该因子同点而标量因子对跖，则

```math
\mathop{\mathrm{Block}}\nolimits_D=\mathop{\mathrm{Block}}\nolimits_O
=\tfrac14(D\otimes D+O\otimes O),
```

而标量 $`\cos2\varphi`$、$`\sin2\varphi`$ 的相对节点符号相反，再次抵消。因此在 AA、BB 两个张量–标量扇区，每个固定谱次数的不同节点同手性块均为零。

交叉手性改变 $`S_-(O,D)`$ 的符号，使两标量块互为相反数，原有节点符号遂使贡献相加。这个有限维恒等式说明手性如何改变传递，但完整 Einstein 障碍还包括一形式扇区、自作用、补空间 Schur 项、投影变化和非线性余项。现有计算不能省去这些项，直接推出闭流形不承载 Einstein 度量。

来源：[节点极化与逐次数相消证明](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/archive/sources/20260923/v08_S0910A01/workspace/notes/step100_chirality_cancellation_proof.md)。四节点交换关系与其数值首阶模型见[四节点相互作用方程](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/archive/sources/20260923/v08_S0910A02/workspace/notes/step100_four_node_closure_and_structural_vanishing.md)；后者只计算首阶模型，尚未估计完整非线性余项。

## 8. 有界几何与精确实现

整合稿从有界直径、体积正下界、单手性超临界 Weyl 控制与 ALE 气泡的拓扑排除出发，建立调和坐标紧性和同一光滑类型的 Einstein 度量。后续 “Bounded-geometry realization without gauge saturation or Weyl bounds” 进一步陈述：

```math
\pi_2(M)=0,\quad\mathop{\mathrm{diam}}\nolimitsg\le D,\quad V_g\ge v,
\quad\delta_\sigma(g)<\epsilon(D,v)
\Longrightarrow\exists h\text{ on }M:\mathop{\mathrm{Ric}}\nolimits_h=\sigma h.
```

该版本通过完备 Ricci-flat ALE 核心的嵌入障碍获得调和坐标紧性，替代了此前的单手性 Weyl 条件。正分支的直径可由 Bonnet–Myers 给出；负分支的实际类的正投影下界可提供体积下界。直径与非塌缩在此仍是实质输入。

对实际共形单极子输入，令 $`p=(a_g^+)^2`$，定义

```math
\mathfrak D_2=\frac32\int(s^2+12|W^+|^2)-72\pi^2p,
\qquad T_\pm=2\chi\pm3\tau.
```

这里 $`a`$ 为该 Spin$`^c`$ 结构的实第一 Chern 类。实际共形输入指固定 Spin$`^c`$ 结构的未扰动方程在输入共形类内处处可解。下表前两行的小量阈值依赖直径上界 $`D`$ 与正投影下界 $`A_0>0`$，第三行只依赖 $`D`$。

| 输入范畴 | 小量 | 同一光滑流形上的结论 |
|---|---|---|
| aspherical，直径有界，单侧逐共形类的单极子解存在性条件及 $`p\ge A_0`$ | $`\delta_-+\mathfrak D_2/V`$ | 负 Kähler–Einstein |
| 两取向逐共形类的单极子解存在性条件，$`p_+,p_->0`$，至少一侧 $`p_\pm\ge A_0`$，直径有界 | $`\delta_-+q_++q_-`$ | 局部为 $`\mathbb H^2\times\mathbb H^2`$，两全局平行复结构 |
| $`T_+=3T_->0`$，单极子解存在性条件 $`p\ge T_+`$，直径有界 | $`\delta_-`$ | 复双曲度量 |

在陈数边界，数值关系与单极子解存在性条件强迫饱和和另一手性曲率小。有限覆盖版本将积分估计按度数归一化后下降，并在底空间完成紧性；阈值依赖底空间直径和归一化正投影下界，与覆盖度数无关。其结论是底空间的局部对称 Riemannian 度量，覆盖上的复结构可不下降。

来源：整合稿 `sec:compact-realization`、`sec:ale-boundary`、`sec:gauge-ke`、`sec:bilateral`、`sec:chern-boundary`、`sec:virtual-realization`。这些实现定理保留各自的全局几何条件，与无直径积分障碍具有不同的适用范畴。

### 体积增长条件下的局部一致 Einstein 修正

正定性与体积增长条件也给出 Einstein 度量的存在定理。设闭 $`n`$ 维流形（$`n\ge3`$）具有统一 $`C^{2,\alpha}`$ 调和坐标，完整 Bianchi 规范线性化

```math
L_g=\tfrac12\nabla^*\nabla+V_g
```

在**全部**对称二张量上满足 $`\langle L_gu,u\rangle_{L^2}\ge\lambda\|u\|_2^2`$。假设实际流形的每个球满足

```math
\mathop{\mathrm{Vol}}\nolimitsB_R(x)\le C_G(1+R)^d e^{HR},\qquad H^2<8\lambda.
```

选择 $`H/2<a<\sqrt{2\lambda}`$、$`\phi_x=e^{-a d(x,\cdot)}`$。二次型恒等式为

```math
\langle L_g(\phi_xu),\phi_xu\rangle_{L^2}
=\int\phi_x^2\langle L_gu,u\rangle
+\frac12\int|d\phi_x|^2|u|^2.
```

因此，$`L_gu=f`$ 时

```math
\|\phi_xu\|_2\le(\lambda-a^2/2)^{-1}\|\phi_xf\|_2,
\qquad
\int\phi_x^2\le C_Ge^H\sum_{m\ge0}(m+2)^d e^{-(2a-H)m}<\infty.
```

加上局部 Moser 与 Schauder 估计，得到与总量、直径无关的逆估计

```math
\|L_g^{-1}f\|_{C^{2,\alpha}_{\rm uloc}}
\le C\|f\|_{C^{0,\alpha}_{\rm uloc}}.
```

局部一致范数取所有坐标球的上确界。非线性二次余项的收缩与 Bianchi 恢复于是给出

```math
\|\mathop{\mathrm{Ric}}\nolimits_g+g\|_{C^{0,\alpha}_{\rm uloc}}<\epsilon
\Longrightarrow
\mathop{\mathrm{Ric}}\nolimits_h=-h,\quad
\|h-g\|_{C^{2,\alpha}_{\rm uloc}}
\le C\|\mathop{\mathrm{Ric}}\nolimits_g+g\|_{C^{0,\alpha}_{\rm uloc}}.
```

若另有 $`\|\nabla\mathop{\mathrm{Ric}}\nolimits\|_\infty\le K_1`$，插值将右侧控制为 $`C\delta_-^{1-\alpha}`$。

固定实双曲流形的循环覆盖提供直径、体积皆趋于无穷的实例。无限循环覆盖由 $`\mathbb Z`$ 余紧作用，基本域计数给有限循环商的统一线性球体积增长。每个基本域中的独立小扰动可使全局 $`L^2`$ 残差按 $`\sqrt m`$ 增长，而上述局部一致修复仍成立。双曲曲面乘积的线性化具有 Teichmüller 核，不满足这里的正强制条件，须使用第6节的完整核修复。

来源：[四维局部一致修复](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/continuation/20260924_uniformly_local_repair.md)、[任意维数版本](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/continuation/20260924_higher_dimensional_local_repair.md)。条件 $`H^2<8\lambda`$ 是该加权证明的充分条件；这里要求二次型正定，而不只是谱与零点分离。

### 剪切流形上谱退化所迫使的直径逃逸

对第5节中具有非零整数剪切的指定自粘合族，已有非球面性、$`\tau=0`$、所有有限覆盖非 Kähler、$`\mathbb Z^2\subset\pi_1`$ 及实际类平方 $`2\chi>0`$。设 $`\mathop{\mathrm{Ric}}\nolimits_g=-g`$，按递增顺序排列 $`W^+`$ 的特征值，记

```math
t=-\tfrac34\lambda_1(W^+),\qquad b=\lambda_3(W^+)-\lambda_2(W^+).
```

对固定 $`0\le\theta<1/\sqrt3`$，若 $`b\le4\theta t`$，则任意直径上界 $`D`$ 都给统一分离

```math
\mathop{\mathrm{diam}}\nolimitsg\le D\quad\Longrightarrow\quad
\mathop{\rlap{-}\int}\nolimits b^2\ge\epsilon(D,\theta)>0.
```

这里允许 $`W^+`$ 的零点。最大值原理先给 $`t\le[2(1-3\theta^2)]^{-1}`$；单极子标量曲率积分下界给 $`V\ge4\pi^2\chi`$，与直径比较合用控制体积和 Euler 数。若完整曲率失控，最大曲率处放大产生非平坦 Ricci-flat 反自对偶 ALE 核心，其嵌入被该非球面拓扑排除。因而有光滑紧性。

若 $`\mathop{\rlap{-}\int}\nolimits b^2\to0`$，极限具有至多两个自对偶 Weyl 特征值。其非零分支给至多二重覆盖上的 Kähler 结构；零分支结合 $`\tau=0`$ 给实双曲度量。前者与非虚 Kähler 性矛盾，后者与基本群中的 $`\mathbb Z^2`$ 矛盾。所以在这一谱区域，分裂能量趋零必使直径趋于无穷，无须另列反手性 Weyl 爆破的可能。

完整证明及指定拓扑族见[非球面核心排除与谱逃逸](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/mathematics/current/line1_aspherical_no_bubbles.md) §§2–3。该定理保留相对谱夹逼，不排除区域外的精确 Einstein 度量。

## 9. 谐和形式的零点、完整填充与退化尺度

固定剪切逼近族表明，删除直径后，双圆盘近饱和可以伴随非 Kähler 拓扑。复双曲陈数边界 $`\chi=3\tau>0`$ 则位于该剪切族之外；其无直径实现涉及有限体积长颈、塌缩与填充，仍待解决。

### 谐和形式零点附近的模长缺陷

若在半径 $`\rho`$ 的坐标邻域中，$`\rho^{-2}g`$ 具有统一椭圆性与 $`C^{1,\alpha}`$ 控制，调和二形式 $`\Omega`$ 满足 $`\Omega(x)=0`$，则

```math
\int_{U_{x,\rho}}(|\Omega|-\sqrt2)^2\,dV_g\ge c\rho^4.
```

缩放到单位球后，小幅度缺陷给出 $`\Omega`$ 的 $`L^2`$ 上界；对一阶 Hodge–Dirac 方程逐次使用 $`W^{1,p}`$ 内部估计，得到统一 Hölder 控制。零点附近一个固定比例小球上模长保持小，从而产生固定正的幅度缺陷；缩放恢复 $`\rho^4`$。

由逐共形类的单极子解得到的谐和代表 $`\Omega=-2\pi H_a`$ 满足

```math
\int(|\Omega|-\sqrt2)^2\le818\kappa V,\qquad
\kappa=\mathop{\rlap{-}\int}\nolimits|\mathop{\mathrm{Ric}}\nolimits+g|^2+D_2/V,
```

这里取相应小缺陷范围。因此

```math
H_a(x)=0\quad\Longrightarrow\quad
r_{\alpha,Q}(x)^4\le C\kappa V,
```

其中 $`r_{\alpha,Q}`$ 是具有上述固定坐标控制的最大尺度。

对直径有界且 Hodge 投影平方具有正下界的近饱和序列，若轨形极限的每个**完整填充**内都有坐标尺度下界 $`\rho_j`$，且

```math
\kappa_jV_j<c_0\rho_j^4,
```

便可排除填充中的谐和零点。在极限奇点为 $`A_1`$ 且填充 $`b_2=1`$，或填充为有理同调球的指定范畴，接触填充分类和相对标记给出 Milnor 纤维对应。再满足全局射影 $`\mathbb Q`$-Gorenstein 平滑条件时，原光滑流形取得负 Kähler–Einstein 度量。局部填充对应与全局复平滑是此证明中两个独立输入。

零点附近模长缺陷的四次尺度不能由平均量取代。在 Kähler 曲面的一个 Darboux 球中插入缩小的 near-symplectic 零圈模型，可保持上同调类及外部形式，并选择使之自对偶的度量；所得形式就是全闭流形上该类的调和代表。幅度缺陷为 $`O(\rho^4)`$，一阶导数能量为 $`O(\rho^2)`$，零圈仍存在。该模型的点态 Ricci 缺陷可增长为 $`\rho^{-2}`$，所以它只说明周期与平均形式误差不足以保证非零性，并非近 Einstein 反例。

完整局部估计、相对填充与零圈构造见[谐和零点的尺度与几何实现](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/continuation/20260924_harmonic_zero_scale.md)。

### Wahl 退化中的实际场

将 Wahl 有理球收缩为 $`\frac1{n^2}(1,n-1)`$ 点时，恢复族的统一标量界使实际旋量有界，缩小填充内的四次质量趋零。阿贝尔可去奇点与实上同调平方不变，将解、联络能量和旋量导数能量传到轨形。该转移保留

```math
a^2,\quad T_+,\quad\mathop{\mathrm{ind}}\nolimitsD,
```

而

```math
T_-^{\rm orb}=T_-(M)-4\sum_\nu(1-n_\nu^{-2}).
```

两手性的变化因此必须分别处理。

在指定典范标记下，一些可延拓字符强迫 $`\Phi(p)=\nabla_A\Phi(p)=0`$；对同时具有单极子解的符号类求平均，仍可在强迫零点子族中保留 Hodge 投影平方正下界。这推出逐度量的严格标量不等式。它若要成为统一 Einstein 障碍，还须控制零点的几何尺度以及同一场的 Weyl 和调和投影缺陷。

逐阶 Taylor 展开不能单独给出上述尺度控制。对任意固定允许的等变度量展开，辅助 SW 系统的平坦主算子在齐次多项式上满射，故允许的 Dirac 首项可以逐阶完成。这里的形式解尚不决定全局解：形式级数的收敛、全局幅度和退化尺度尚未由形式递归决定。

上述场转移、指标公式、首项次数和形式延拓的连续证明见[Wahl 退化中的实际规范场](../research/notes/Wahl_Fields_and_Formal_Completion.md)。

## 10. 未解的存在性问题

积分间隙描述不可逼近区域，构造给出曲率极值的上界，周期与慢模态刻画退化，有界几何实现定理产生同一光滑对象上的精确解。上述存在性定理分别依赖低频分量的逆估计、闭路单值表示、填充中的非零场与边界标记，以及平滑或变形方程。

这里还须区分两个尺度不变量。体积塌缩构造若使 $`P\to0`$，只决定 $`P_*=0`$；它并不自动使 $`\alpha=\inf\mathcal E`$ 为零。例如 $`\chi=\tau=0`$ 时，长圆柱上界与 Chern–Weil 下界给 $`\alpha=1`$。由非零 Einstein 主体取得 $`\alpha=0`$，还需控制标量平均、方差和完整恢复积分，见[曲率变分](CURVATURE_VARIATION.md)。

尚未解决的全局目标包括 $`E_D`$ 的负 Einstein 存在性、一般退化下的精确实现、目标流形的全度量最优曲率值以及闭负 Goldberg 问题。

# 负 Einstein 几乎 Kähler 四维流形：构造与刚性

Shuxing Yang, Junyao Wu, Rui Zhao, Hongsheng Chen, Yihao Yang  
Qiushi Engine Team, Zhejiang University · [作者与通讯信息](../AUTHORS.md)

## 问题与符号约定

设 $`(M^4,g,J,\Omega)`$ 为闭、连通的几乎 Kähler 四维流形，

```math
\Omega(X,Y)=g(JX,Y),\qquad d\Omega=0,\qquad
\mathop{\mathrm{Ric}}\nolimits_g=-ag,\quad a>0.
```

取向由 $`\Omega^2`$ 决定，故 $`*\Omega=\Omega`$、$`|\Omega|^2=2`$，标量曲率为 $`s=-4a`$。负 Goldberg 问题是：上述条件是否蕴含 $`\nabla\Omega=0`$？等价地，是否存在闭的非 Kähler 几乎 Kähler–Einstein 四维流形，且 Einstein 常数为负？

下文采用非负 Laplace 算子 $`\Delta=-\mathop{\mathrm{div}}\nolimits\nabla`$ 与 $`\nabla^*\nabla`$。曲率算子作用在二形式上，Weyl 算子的范数为 Hilbert–Schmidt 范数。令

```math
q=|\nabla\Omega|^2,\qquad n=\Omega/\sqrt2,\qquad
Z=\{x\in M:q(x)=0\}.
```

相对于 $`\Lambda^+=\mathbb Rn\oplus n^\perp`$，写成

```math
W^+=\begin{pmatrix}t&v^*\\v&-tI/2+B\end{pmatrix},\qquad
t=\frac{s}{6}+\frac q4,\qquad \mathop{\mathrm{tr}}\nolimits B=0,
```

其中

```math
\eta=W^+\Omega-t\Omega\in\Lambda_J^-,\qquad v=\eta/\sqrt2.
```

这里 $`\Lambda_J^-`$ 是实 $`J`$-反不变二形式丛，$`B`$ 是 $`n^\perp`$ 上的无迹对称块，通常记为 $`W_3^+`$。闭情形的共同约束是扭率、Weyl 曲率和归一化 Einstein 作用量之间的恒等式；非紧构造则说明这些局部方程允许怎样的严格非可积几何。

## 完备非紧构造与 Fino 的存在性问题

[显式构造](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex)给出微分同胚于 $`\mathbb R^4`$ 的完备度量与相容二形式，满足

```math
\mathop{\mathrm{Ric}}\nolimits=-3g,\qquad W^-=0,\qquad d\Omega=0,\qquad
|\Omega|^2=2,\qquad |\nabla\Omega|^2>0.
```

构造使用 $`\mathrm{SL}(2,\mathbb R)`$ 上的左不变余标架

```math
d\sigma_1=-2\sigma_2\wedge\sigma_3,\qquad
d\sigma_2=2\sigma_3\wedge\sigma_1,\qquad
d\sigma_3=2\sigma_1\wedge\sigma_2.
```

令 $`D=1+3x^2`$。对 $`1/3\lt x\lt 1`$，取

```math
\begin{aligned}
G&=\frac{4D}{(1-x^2)^2(9x^2-1)},\\
A_1&=\frac{4(3x-1)D}{3(1-x)(1+x)^2},&
A_2&=\frac{4(3x+1)D}{3(1-x)^2(1+x)},\\
A_3&=\frac{64x^2}{(1-x^2)D},&
X_1&=\frac{(1-x)^3(3x+1)}{16x^3},\quad
X_2=\frac{(1+x)^3(3x-1)}{16x^3}.
\end{aligned}
```

定义

```math
g=G\,dx^2+\sum_{i=1}^3A_i\sigma_i^2,\qquad
e^0=\sqrt G\,dx,\quad e^i=\sqrt{A_i}\sigma_i,
```

```math
\omega_i=e^0\wedge e^i+e^j\wedge e^k,\qquad
\Omega=\sqrt{X_1}\,\omega_1+\sqrt{X_2}\,\omega_2,
```

其中 $`(i,j,k)`$ 循环排列。$`X_1+X_2=1`$ 给出 $`|\Omega|^2=2`$。令 $`dr=\sqrt G\,dx`$、$`h_i=d\log\sqrt{A_i}/dr`$，并按上述结构方程写 $`de^i=h_i e^{0i}+2w_i e^{jk}`$，则

```math
d(f_i\omega_i)
=\bigl(f_i'+(h_j+h_k-2w_i)f_i\bigr)e^{0jk}=0,
\qquad f_i=\sqrt{X_i}.
```

这直接验证闭性。由同一标架的 Koszul 公式计算，曲率算子的混合块为零，$`\mathcal R^-=-I`$，$`\mathop{\mathrm{tr}}\nolimits\mathcal R^+=-3`$，从而 $`\mathop{\mathrm{Ric}}\nolimits=-3g`$、$`W^-=0`$。

该结构光滑延拓到平面丛

```math
\mathrm{SL}(2,\mathbb R)\times_{\mathrm{SO}(2)}\mathbb R^2
\longrightarrow\mathbb H^2.
```

总空间微分同胚于 $`\mathbb R^4`$，且

```math
|\nabla\Omega|^2=\frac{36(1-x^2)^3}{(1+3x^2)^3}.
```

**光滑性与完备性。** 将 $`r=0`$ 置于 $`x=1/3`$，有

```math
x-\tfrac13=\tfrac29r^2+O(r^4),\qquad
A_1=r^2+O(r^4),\qquad A_2=A_3=6+7r^2+O(r^4),
```

```math
A_2-A_3=\tfrac{10}{3}r^4+O(r^6),\qquad X_2=\tfrac83r^2+O(r^4).
```

圆周参数取周期 $`2\pi`$。在局部纤维坐标 $`z=re^{i\psi}`$ 下，法向度量首项为 $`|dz+iz\beta|^2`$；水平余标架的权为二，其权四非等向项由 $`r^4`$ 的消失阶保证光滑。$`\Omega`$ 的混合项分别写成 $`zF(r^2)`$ 和 $`z^3H(r^2)`$ 乘以光滑形式，因而也穿过零截面。此处 $`q=32/3`$。

当 $`x\uparrow1`$，$`G\sim[2(1-x)^2]^{-1}`$，所以 $`r\to\infty`$。在每个有界径向区间，$`A_2,A_3`$ 有正下界，故

```math
g\ge dr^2+c_R\pi^*g_{\mathbb H^2}\quad(0\le r\le R).
```

有限长度曲线同时具有有界径向坐标和有界底空间距离，不能逃离紧集。双曲平面可缩，平面丛平凡，故总空间为 $`\mathbb R^4`$，并且度量完备。

**非齐性。** 曲率不变量 $`|W^+|^2`$ 在零截面等于 $`2/3`$，在无穷端趋于 $`6`$，因而度量本身非齐性。此外

```math
\left|\mathop{\mathrm{pr}}\nolimits_{n^\perp}(W^+n)\right|^2
=\frac{9(1-x^2)^3(9x^2-1)}{(1+3x^2)^4}>0
```

在正则区域成立：相容形式不是 Weyl 特征形式。完整曲率表达式与光滑延拓见[构造正文](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex)，其[精确代数程序](../archive/originals/2026-10-08/Q4_independent_cartan.py)从标架括号计算全部曲率分量。

Fino 的 *Almost Kähler 4-dimensional Lie groups with $`J`$-invariant Ricci tensor*（2005）在 Corollary 2.1 之后询问：实四维 Lie 群上是否存在非不变、非 Ricci 平坦的严格几乎 Kähler–Einstein 度量。将上述结构拉回 $`(\mathbb R^4,+)`$，即得到该存在性问题的一个完备例子。该例非紧且体积无限；闭流形上的负 Goldberg 猜想另要求紧致性。

## 对称局部解与紧致延拓的限制

### 正则 nut 点的刚性

设一个光滑 Einstein–几乎 Kähler 对 $`(g,\Omega)`$ 在一个孤立固定点附近同时具有完整的 $`\mathrm{SU}(2)`$ 不变性，正则轨道为三维球面，固定点为光滑 nut。取 $`\mathop{\mathrm{Ric}}\nolimits=-3g`$，并取在 nut 处允许非零不变自对偶二形式的手性，则该局部对只能是复双曲 Kähler 对。

首先，无须预先假定度量对角。沿法向测地线写

```math
g=dt^2+H_{ij}(t)\sigma_i\sigma_j,\qquad
 d\sigma_i=2\sigma_j\wedge\sigma_k.
```

在某一正则轨道上对角化 $`H=\mathop{\mathrm{diag}}\nolimits(a_i^2)`$，混合 Einstein 方程为

```math
(n_k-n_j)K_{jk}=0,\qquad
K_{jk}=\frac{H'_{jk}}{2a_ja_k},\qquad
n_i=-\frac{2a_i}{a_ja_k}.
```

故 $`[H,H']=0`$。用一个常数 $`\mathrm{SO}(3)`$ 变换同时对角化 $`H,H'`$ 后，空间 Einstein 方程的唯一性将这个固定标架保持为对角标架；重特征值及其交叉不增加新的自由度。

令 $`u=t^2`$、$`a_i=tf_i(u)`$，并定义

```math
H_i=1+2u\frac{f_i'}{f_i},\qquad
Z_i=\frac{f_i}{f_jf_k}.
```

正则 nut 的 Einstein 方程与约束为

```math
2uH_i'-H_i+H_i\sum_jH_j
-2\bigl[Z_i^2-(Z_j-Z_k)^2\bigr]-3u=0,
```

```math
\sum_{i\lt j}H_iH_j+\sum_i Z_i^2-2\sum_{i\lt j}Z_iZ_j-3u=0.
```

初项为 $`f_i=1+(1/6+d_i)u+\cdots`$、$`\sum_i d_i=0`$。写 $`\Omega=\sum_i x_i\omega_i`$、$`X_i=x_i^2`$，闭性及常长度条件恰为

```math
uX_i'=(2Z_i-H_j-H_k)X_i,\qquad
\sum_iX_i=1,\qquad R_i:=X_i(0)\ge0.
```

由上式递推所得的前五个正次长度系数为有理多项式。其共同零集在 $`\sum R_i=1`$、$`\sum d_i=0`$ 下为三条直线，即

```math
(d_1,d_2,d_3)=(1/6,-1/12,-1/12),\qquad
(R_1,R_2,R_3)=(1,r,-r)
```

及其置换。这里允许复系数的代数消元尚保留参数 $`r`$；非负条件 $`R_i\ge0`$ 强迫 $`r=0`$。[精确代数程序](../research/computations/bianchi_ix_nut.py)由上述 ODE 生成前五阶约束，并检验它们的根理想恰为这三条直线的交理想。程序只需 SymPy 与 Singular；全阶结论还使用下面的唯一性论证。

在每阶 $`u^n`$、$`n\ge2`$，新的三个度量系数在 Einstein 递推中的特征值分别为

```math
4(n+2)(n-1)\quad\text{（无迹部分）},\qquad
2(n+2)(2n+1)\quad\text{（迹部分）}.
```

它们均非零，闭形式的传输也唯一；因此有限代数约束已经确定全部 Taylor 系数。相应的解析解为

```math
a_1=\frac{\sinh(\sqrt2t)}{\sqrt2},\qquad
a_2=a_3=\sqrt2\sinh(t/\sqrt2),\qquad
\Omega=\pm\omega_1.
```

Einstein 度量及其调和形式的解析正则性将形式唯一性提升为光滑局部唯一性。这排除了完整 $`\mathrm{SU}(2)`$ 对称的严格非可积 nut；不变度量上的非不变形式、较小对称群及一般局部解仍是不同的问题。

### 双曲固定曲面的紧致延拓

上述 Fino 模型可以对双曲底空间取紧商，但将两个双曲 bolt 用三维轨道领口连接，不能得到闭 Einstein 度量。更一般地，若光滑闭四流形由曲面 $`\Sigma_i`$ 上的二维圆盘丛及乘积领口组成，则

```math
\chi(M)=\sum_i\chi(\Sigma_i).
```

所有 bolt 的亏格均大于一时，右端为负，与 Einstein 的 Gauss–Bonnet 公式矛盾。没有 bolt 而轨道空间为圆周时，$`\chi=0`$，同一公式迫使度量平坦。这仅处理所述光滑圆盘丛拼接；不同外部、轨形端点及不能按此分解的闭几何需要各自的匹配分析。

## 严格低于标准插入能量的辛构造与共形归一化

[曲率变分中的严格上界构造](CURVATURE_VARIATION.md)还具有一个结构性质：无迹 Ricci 能量严格低于标准吹起能量的度量，可以同时承载与外部形式精确匹配的无零自对偶闭二形式。本节记 $`P(g)=\int|\mathop{\mathrm{Ric}}\nolimits^{\circ}|^2`$、$`S(g)=\int s^2`$。

以 $`\mathop{\mathrm{Ric}}\nolimits_{\mathrm{CH}}=-6g`$ 归一化，固定一个精确复双曲领口的光滑 $`\mathcal O(-1)`$ 单元 $`g_*`$，使

```math
J_6(g_*):=\int|\mathop{\mathrm{Ric}}\nolimits_{g_*}+6g_*|^2\lt 8\pi^2.
```

其从外领口向内传输的自对偶闭形式在 bolt 上为零。取单调截断 $`\chi`$，在 bolt 邻域等于一，在外领口等于零，并在塌缩方向与纤维方向的平面内旋转轨道度量：

```math
H_\epsilon=R(\epsilon\chi)H_*R(\epsilon\chi)^T.
```

bolt 附近的常旋转是固定右平移的拉回，外部旋转为恒等，故度量的光滑性、拓扑标记和外领口不变。由未改变的外部 Kähler 形式积分闭自对偶方程，所得形式 $`\Omega_\epsilon`$ 的异常周期 $`p=\int_E\Omega_\epsilon`$ 满足

```math
p'(0)=-\pi\int\chi'(r)\Phi(r)\,dr>0,
\qquad \Phi=\psi_+(0)\frac{\phi_f}{\psi_+}>0.
```

这里 $`\psi_+`$ 为正的齐次传输解，$`\phi_f`$ 为原零周期解的非零纤维系数；旋转方向取上述符号。闭自对偶一阶系统的唯一性排除正则轨道上的共同零点，非零 $`p`$ 则排除 bolt 上的零点。因此充分小的 $`\epsilon\ne0`$ 给出辛形式，而平滑二阶连续性保留 $`J_6(g_\epsilon)\lt 8\pi^2`$。

在紧复双曲商的互不相交精确球领口内插入这些单元，得到纯吹起上的整体共形几乎 Kähler 竞争度量。一般仅接近复双曲的背景还需要同时延拓度量与闭形式；已有单独的度量匹配不能替代这一要求。

### 异常周期趋零时的标量曲率集中

记 $`p`$ 为小异常周期，$`r`$ 为到 bolt 的法向距离，bolt 面积为 $`\pi b^2`$。设

```math
f_p=|\Omega_p|_{g_p}/\sqrt2,\qquad
\widehat g_p=f_pg_p=v_p^2g_p,\qquad v_p=\sqrt{f_p}.
```

光滑 bolt 展开中，周期分量与原形式的一阶法向分量正交，因而

```math
f_p^2=a_0^2p^2+\kappa^2r^2+O(p^2r^2+r^4),\qquad
a_0=(\pi b^2)^{-1},\quad\kappa>0.
```

故归一化层的尺度为 $`r\asymp|p|`$。在这一层，若 $`\mathscr D=\mathop{\mathrm{div}}\nolimits\nabla=-\Delta`$，则

```math
\frac{\mathscr Dv_p}{v_p}
=\frac{\kappa^2(4a_0^2p^2+\kappa^2r^2)}
{4(a_0^2p^2+\kappa^2r^2)^2}+O(1),
```

```math
S(\widehat g_p)
=\int\left(s_{g_p}-6\frac{\mathscr Dv_p}{v_p}\right)^2dV_{g_p}
\sim\frac{C_E}{p^2},\qquad
C_E=36(2\pi^2b^2)\frac{7\kappa^2}{32a_0^2}>0.
```

常数来自 $`dV_{g_p}=2\pi^2b^2r\,dr+O(r^3)dr`$ 及

```math
\int_0^\infty
\left[\frac{\kappa^2(4a_0^2p^2+\kappa^2r^2)}
{4(a_0^2p^2+\kappa^2r^2)^2}\right]^2r\,dr
=\frac{7\kappa^2}{32a_0^2p^2}.
```

总体积具有正极限，标量积分保持有界，因此标量方差具有同一首项。在闭插入度量上，共形 Chern–Weil 恒等式精确给出

```math
P(\widehat g_p)-P(g_p)
=\frac{S(\widehat g_p)-S(g_p)}{12}
\sim\frac{C_E}{12p^2}.
```

原度量 $`g_p`$ 光滑收敛并保持严格能量上界；发散发生在将相容形式归一到常长度的代表上。因此，共形 Kähler 类的能量下界不能推广为共形几乎 Kähler 类的同一下界。

整体周期也随之变化。在外部 $`\mathop{\mathrm{Ric}}\nolimits=-g`$ 归一化下，令 $`A=K_X^2>0`$，用拉回的主体典范类 $`K_X`$ 写

```math
[\psi]=\pm2\pi K_X-\sum_i s_i\mathop{\mathrm{PD}}\nolimits(E_i),\qquad
[\psi]^2=4\pi^2A-\sum_i s_i^2.
```

与主体类的归一化配对为

```math
\frac{|2\pi K_X\cdot[\psi]|}{\sqrt{4\pi^2A[\psi]^2}}
=\left(1-\frac{\sum_i s_i^2}{4\pi^2A}\right)^{-1/2}.
```

这是二次周期效应；若改与吹起后相容结构的典范类配对，则还出现异常分量的一次项。

## 扭率零点及零曲线

局部选取与 $`\Omega`$ 正交、长度为 $`\sqrt2`$ 的二形式 $`\phi,J\phi`$，写成

```math
\nabla\Omega=\vartheta\otimes\phi-J\vartheta\otimes J\phi,
\qquad q=4|\vartheta|^2,
```

其中 $`(J\vartheta)(X)=-\vartheta(JX)`$。$`\vartheta`$ 的零点与 Nijenhuis 张量 $`N_J`$ 的零点一致。在零点处，$`L=(\nabla\vartheta)^\sharp`$ 的秩、实行列式和零化性质与局部标架选择无关。

[零点结构原稿](../archive/originals/2026-10-09/Q4_Torsion_Zero_Structure.tex)证明，在适配的复正交标架中，

```math
L(z)=cz+Q\bar z,\qquad c\in\mathbb C,\quad Q\in M_2(\mathbb C),
\qquad \mathop{\mathrm{tr}}\nolimits(Q\bar Q)=-8|c|^2,
```

```math
\det_{\mathbb R}L=9|c|^4+|\det_{\mathbb C}Q|^2\ge0.
```

$`\bar Q`$ 表示逐项共轭。横截零点的局部指数为 $`+1`$；非横截零点的导数实秩为 $`0`$ 或 $`2`$。在 $`Z`$ 上还有精确恒等式

```math
\boxed{|\nabla^2\Omega|^2=4|B|^2-6|\eta|^2.}
```

Armstrong 的经典拓扑论证将 $`N_J`$ 视为复秩二丛

```math
\mathcal N=T^{1,0}M\otimes\bar K,\qquad K=\Lambda^{2,0}T^*M
```

的截面，并给出

```math
c_2(\mathcal N)[M]=5\chi(M)+6\tau(M).
```

对闭、非零标量 Einstein 度量，Chern–Weil 公式保证该数为正，因而 $`Z\ne\varnothing`$。若全部零点横截，则

```math
\#Z=5\chi+6\tau.
```

这一计数与正局部指数相容。

在 $`Z`$ 上，$`\langle W^+n,n\rangle=s/6`$，从而

```math
\lambda_{\min}(W^+)\le s/6,\qquad |W^+|^2\ge s^2/24.
```

因此闭负 Einstein 度量若处处满足 $`\lambda_{\min}(W^+)>s/6`$，就不能携带该取向的相容几乎 Kähler 形式。特别地，$`W^+=0`$ 的负 Einstein 度量被排除。该结论将非零扭率丛的总陈数限制在上述曲率区域；它本身没有给出该区域的体积或能量下界。完备 Fino 模型在每个有限点满足严格的相反曲率界，并仅在无穷远趋近 Kähler 值，说明这里确实使用了闭性。

[零曲线分析](../archive/originals/2026-10-15/Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex)进一步证明：当 $`s\ne0`$ 时，不存在紧致无边界嵌入曲面 $`C\subset Z`$ 满足

```math
\ker(DN_J)_x=T_xC\qquad\text{对所有 }x\in C.
```

对于闭光滑 $`J`$-全纯零曲线，若 $`DN_J`$ 的秩二点在曲线上稠密，则 $`C`$ 全测地。其法向扭率导数为线丛

```math
\mathop{\mathrm{Hom}}\nolimits_{\mathbb C}
(\bar\nu_C,T^{1,0}C\otimes\bar K|_C)
\simeq\bar K^{\otimes2}|_C
```

的截面 $`\xi`$，其中 $`\nu_C`$ 是复法丛。该线丛的度数为

```math
\deg(\bar K^{\otimes2}|_C)
=\frac{s}{4\pi}\mathop{\mathrm{Area}}\nolimits_g(C)\lt 0.
```

故 $`\xi`$ 必有零点。其[切向微分方程](../archive/originals/2026-10-15/Goldberg_Global_Connections_20261015.tex)为

```math
D^{1,0}\xi=r,\qquad D^{1,0}r=0,
```

其中 $`D`$ 为诱导的典范 Hermitian 联络，$`r`$ 是横向曲率分量的法向导数。方程保留这一非齐次项，容许秩下降及负指数。

### 高阶零点的首项

若扭率一形式 $`\vartheta`$ 在一点的第一非零 Taylor 项为次数 $`m\ge2`$ 的齐次多项式，则在适配的复正交标架中必有

```math
\boxed{f_m(z)=\kappa(\bar z_2)^m e_1.}
\tag{Z}
```

这一必要条件与标量曲率的符号无关。它限制首项的方向和类型，并不保证该多项式能延拓为实际解。

证明从 Einstein–几乎 Kähler 方程的主部开始。半扭子方程先给出

```math
f_m=z\,h(\bar z)+g(\bar z),\qquad
\deg h=m-1,\quad\deg g=m.
```

令 $`w=\bar z`$、$`C=z\otimes D_wh+D_wg`$，并将 $`C`$ 分为转置对称部分 $`C_s`$ 和转置反对称部分 $`C_a`$。对 $`q`$ 应用调和形式方程与完整 Weyl 方程，在次数 $`2m-2`$ 比较系数，得到

```math
\|C_a\|^2-\|C_s\|^2-8|h|^2
-6\mathop{\mathrm{Re}}\nolimits\sum_j\overline{f_{m,j}}\,\partial_{w_j}h=0.
```

最后一项来自 $`\nabla W^+`$ 与 $`\nabla\Omega`$ 的乘积，不能删去。Euler 齐次公式将其改写为

```math
\mathop{\mathrm{tr}}\nolimits(\overline{Dg}Dg)+(m+1)(m+3)|h|^2
+2(m+3)\mathop{\mathrm{Re}}\nolimits\sum_j\overline{g_j}\,\partial_{w_j}h=0.
```

前两项与最后一对共轭项具有不同复双次数，故分别为零。若 $`g_1,g_2`$ 作为多项式线性独立，则 $`Dh=0`$；若 $`g=vG`$ 取值于固定复直线，则
$`\mathop{\mathrm{tr}}\nolimits(\overline{Dg}Dg)=|\sum\bar v_i\partial_{w_i}G|^2\ge0`$，同样得到 $`h=0`$。

在矩阵空间上，Hermitian 形式
$`\mathcal H(U,V)=\mathop{\mathrm{tr}}\nolimits(\bar U V)`$ 的符号为 $`(3,1)`$。恒等式 $`\mathcal H(Dg,Dg)=0`$ 表明 $`Dg`$ 的各多项式系数张成全迷向子空间，故维数至多一。写 $`Dg=M p(w)`$，混合偏导相等迫使 $`M=v\otimes\ell`$ 为秩一，$`p`$ 为 $`(\ell\cdot w)^{m-1}`$ 的倍数；迷向性又给出 $`\ell\cdot\bar v=0`$。一次相容的酉标架变换即得式 (Z)。

沿零曲线，这个首项使异常点处横向 Weyl 截面的切向一次项消失，却不决定绕数。例如 $`z|z|^2`$ 与 $`\bar z|z|^2`$ 都没有一次项，绕数分别为 $`+1`$ 和 $`-1`$。上述非齐次传输方程仍保留法向源 $`r`$；仅对标量恒等式继续微分，尚不能将 $`r`$ 写成对 $`\xi,\bar\xi`$ 的有界零阶作用。

### 有限阶相容模型

有限阶模型说明上述正指数与 Einstein 方程的低阶相容条件并不矛盾。在 Darboux 坐标中固定 $`\Omega_0=dx_1\wedge dx_2+dx_3\wedge dx_4`$，取对称矩阵多项式 $`H=H_2+H_4+H_6`$，使 $`H\Omega_0+\Omega_0H=0`$，并令 $`g=e^H`$。则 $`g\Omega_0g=\Omega_0`$，所以正定性和几乎 Kähler 相容性精确成立。所给有理系数满足

```math
\mathop{\mathrm{Ric}}\nolimits(g)+g=O(|x|^6),\qquad
\vartheta(x)=(x_1-x_4,-x_2-x_3,x_2/2,x_1/2)+O(|x|^3),
```

故 $`\det D\vartheta(0)=1/4>0`$。完整系数及计算见[零点与 Weyl 方程正文](../archive/originals/2026-10-15/Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex) §3。更高阶的浮点重构保留了非退化零点，但未给出精确的全阶形式解。已成立的结论是显示 Taylor 阶内的相容性，不能由此推出精确 Einstein 局部解或闭流形上的实现。

## Darboux 表示下的线性相容结构

固定平坦 $`\mathbb C^2`$ 的标准辛形式，以反 $`J`$ 不变对称张量 $`h`$ 表示相容度量的线性变化。令 $`\mathcal P_n`$ 为四个实变量的次数 $`n`$ 齐次多项式空间，$`\Delta_0=-\sum\partial_i^2`$。线性 Ricci 算子为

```math
L_nh=\frac12\left(\partial_k\partial_i h_{kj}
+\partial_k\partial_jh_{ki}+\Delta_0h_{ij}\right),\qquad
h\in\mathcal P_{n+2}\otimes\mathop{\mathrm{Sym}}\nolimits^2_{\mathrm{anti}\text{-}J}.
```

除了线性收缩 Bianchi 方程，还恰好有一个标量微分相容式：

```math
\mathscr B(E)_j=\partial_iE_{ij}-\frac12\partial_j\mathop{\mathrm{tr}}\nolimits E,
\qquad
\mathscr P(E)=J_{ia}J_{jb}\partial_a\partial_bE_{ij}
+\frac12\Delta_0\mathop{\mathrm{tr}}\nolimits E.
```

对所有 $`n\ge0`$，有齐次多项式空间上的正合关系

```math
\boxed{\mathop{\mathrm{im}}\nolimits L_n
=\ker(\mathscr B,\mathscr P),\qquad
\dim\mathop{\mathrm{coker}}\nolimits L_n
=4\binom{n+2}{3}+\binom{n+1}{3}.}
\tag{F}
```

负次数空间及相应二项式系数取零。这一结论同时给出常系数算法：给定次数 $`n`$ 的源，先计算其 Bianchi 四分量与标量 $`\mathscr P`$；两者消失时，线性度量修正存在。

**证明结构。** 反 $`J`$ 不变性给出 $`\mathop{\mathrm{tr}}\nolimits h=0`$、$`J^ThJ=-h`$。代入 $`L_n`$ 可直接验证 $`\mathscr B L_n=\mathscr P L_n=0`$。为证明没有遗漏相容条件，写

```math
h=\mu_{ab}\,dz_a dz_b+\nu_{ab}\,d\bar z_a d\bar z_b,
\qquad \mu=\bar\nu,
\qquad v_a=\partial_{\bar z_1}\nu_{a2}-\partial_{\bar z_2}\nu_{a1}.
```

在 $`\ker L_n`$ 上，$`\partial_{z_b}v_a=\delta_{ab}h_0(\bar z)`$，因此主扭率像为

```math
\mathsf T_n(\ker L_n)
=\{z h_0(\bar z)+g_0(\bar z):
\deg h_0=n,\ \deg g_0=n+1\}.
```

这个像的实维数为 $`6n+10`$。反全纯对称 $`\nu`$ 及多项式 Poincaré 引理产生全部 $`g_0`$；对 $`h_0=w_1^n`$，显式提升为

```math
\nu_{11}=-w_1^nw_2z_1-\frac n2w_1^{n-1}w_2^2z_2,
\qquad \nu_{12}=-w_1^nw_2z_2,
\qquad \nu_{22}=0.
```

$`n=0`$ 时第二项取零。直接代入得到 $`L_nh=0`$、$`v=zw_1^n`$；酉群作用张成全部次数 $`n`$ 的 $`h_0`$。

若 $`v=0`$，则 $`\nu=\bar\partial\bar\partial\phi`$，剩余方程为 $`\partial\bar\partial(\sum\partial_z\partial_{\bar z}\mathop{\mathrm{Re}}\nolimits\phi)=0`$。虚部给出 Hamiltonian 规范方向；扣除势的冗余后得到

```math
\dim\ker L_n=\binom{n+7}{3}+(n+5)^2+2n-10,
```

```math
\dim\bigl((\ker L_n\cap\ker\mathsf T_n)/
\text{Hamiltonian 规范}\bigr)=(n+1)(n+5).
```

特别在 $`n=0`$，后一个空间的五维是实际的 $`W^-`$ 曲率自由度，不能一并当作规范删除。另一方面，Fischer 内积将 $`(\mathscr B,\mathscr P)`$ 的伴随变成符号矩阵的乘法；该矩阵在任意非零实余向量上秩为五，故伴随在相应多项式次数上单射。由此两类相容条件独立且维数正好等于上述余核，得到 (F)。

非线性 Einstein 方程的每阶源还依赖此前选择的曲率与扭率系数。式 (F) 确定线性相容条件，不证明整个非线性 Taylor 塔可解；数值上某一截断的满秩也不替代全阶形式解或解析收敛。尤其固定一个较低阶提升后得到的“障碍”，必须再对所有允许的较高阶修正取商，才能解释为与提升选择无关的几何限制。

## 行列式与 Green 势刚性

定义自对偶曲率块、其相反数及第二初等对称函数：

```math
\mathcal R_+=W^+-\frac a3I,\qquad A=-\mathcal R_+,
\qquad U=\sigma_2(A)=\frac{a^2}{3}-\frac12|W^+|^2.
```

经典 Einstein Weyl–Weitzenböck 方程为

```math
\nabla^*\nabla W^++\frac s2W^+-6(W^+)^2+2|W^+|^2I=0.
```

与 $`W^+`$ 配对并平移曲率算子，得到

```math
(\Delta+2a)U=|\nabla A|^2-18\det\mathcal R_+.
```

闭流形上的 $`L_a=\Delta+2a`$ 可逆。记其正 Green 核为 $`G_a(x,y)`$，并令

```math
\Psi=L_a^{-1}(\det\mathcal R_+),\qquad
\mathcal D=L_a^{-1}(|\nabla A|^2).
```

于是 $`U=\mathcal D-18\Psi`$、$`\mathcal D\ge0`$。结合零点恒等式，[合并原稿](../research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)得到：对每个 $`p\in Z`$，

```math
\boxed{18\Psi(p)=\mathcal D(p)
+\frac18|\nabla^2\Omega(p)|^2+\frac54|\eta(p)|^2.}
```

若存在 $`p\in Z`$ 使 $`\Psi(p)\le0`$，右端各项均为零。Green 核的严格正性推出 $`\nabla A\equiv0`$，进而

```math
A=a\,n\otimes n,\qquad \nabla\Omega=0.
```

这给出[Green 势刚性定理](../archive/originals/2026-10-14/Q4_Green_Potential_Rigidity.tex)。全局条件 $`\det\mathcal R_+\le0`$ 通过正性保持蕴含 $`\Psi\le0`$，从而包含较早的[行列式符号刚性定理](../archive/originals/2026-10-13/Q4_Determinant_Sign_Rigidity.tex)。

将 $`W^+`$ 的特征值记为 $`\lambda_1\ge\lambda_2\ge\lambda_3`$，令

```math
\Sigma=\{x:\lambda_1(W^+)=\lambda_2(W^+)\}.
```

则零点结构进一步给出

```math
Z\cap\Sigma=\{p:\nabla\Omega(p)=0,\ \nabla^2\Omega(p)=0\}.
```

上述闭光滑零曲线必经过 $`Z\cap\Sigma`$。在交点处，恒等式化为

```math
18\Psi(p)=\int_MG_a(p,y)|\nabla A(y)|^2\,dV_y.
```

右端记录全流形的曲率变化。任何闭非 Kähler 候选必须在每个扭率零点满足 $`\Psi>0`$，并在某个开集满足 $`\det\mathcal R_+>0`$。

## 典范联络的正交关系、调和形式乘积与变分

### 典范联络的正交关系

典范曲率公式与 Bonthrone–Zhang 的典范因子定理给出：对每个闭实 $`J`$-反不变二形式 $`\alpha`$，

```math
\int_M\langle\eta,\alpha\rangle\,dV_g=0.
```

因此，若存在全局光滑 $`f>0`$ 使 $`d(f\eta)=0`$，则 $`\eta=0`$。Apostolov–Armstrong–Drăghici 的紧致第三 Gray 定理随后推出 $`\nabla\Omega=0`$。

在 $`\{\eta\ne0\}`$ 上定义 Lee 形式 $`\vartheta_\eta`$：

```math
d\eta=\vartheta_\eta\wedge\eta.
```

积分因子方程等价于 $`d\log f=-\vartheta_\eta`$。其局部可解性要求 $`d\vartheta_\eta=0`$，全局可解性还涉及周期及跨零集延拓。[典范联络正交关系的证明](../archive/originals/2026-10-12/Q4_Canonical_Orthogonality.tex)计算了上述非紧例的 $`d\vartheta_\eta\ne0`$，给出局部积分因子存在性的明确障碍。

### 调和乘积

对固定闭定向度量，取平均正交规范的自对偶调和基 $`\psi_1,\ldots,\psi_m`$，其中 $`m=b_2^+(M)`$。令

```math
G_{ij}(x)=\langle\psi_i(x),\psi_j(x)\rangle,
\qquad B_g(x)=G(x)-I,
\qquad
H_{ij}=\mathop{\rlap{-}\int}\nolimits_M\langle\nabla\psi_i,\nabla\psi_j\rangle\,dV_g,
```

并在实对称矩阵空间上定义

```math
\mathsf C_g(X)=\mathop{\rlap{-}\int}\nolimits_M\langle B_g(x),X\rangle B_g(x)\,dV_g.
```

相容几乎 Kähler 形式（模去符号）精确对应

```math
X\in\ker\mathsf C_g,\qquad X\succeq0,\qquad
\mathop{\mathrm{tr}}\nolimits X=1,\qquad\mathop{\mathrm{rank}}\nolimits X=1.
```

这里 $`X=uu^T`$、$`|u|=1`$ 对应 $`\Omega=\sqrt2\sum_i u_i\psi_i`$。因为

```math
\langle\mathsf C_g(X),X\rangle
=\mathop{\rlap{-}\int}\nolimits\langle B_g(x),X\rangle^2,
```

核条件恰好表示 $`|\Omega|^2\equiv2`$；闭性来自各 $`\psi_i`$ 的调和性。并且

```math
\mathop{\rlap{-}\int}\nolimits|\nabla\Omega|^2=2\mathop{\mathrm{tr}}\nolimits(HX),
```

所以相应形式平行当且仅当 $`\mathop{\mathrm{tr}}\nolimits(HX)=0`$。若 $`\ker H\ne0`$ 且度量负 Einstein，di Scala–Nagy 的唯一性定理保证全部相容形式平行。

[调和乘积原稿](../archive/originals/2026-10-13/Q4_Harmonic_Product_Reduction.tex)还计算了 Kähler 方向附近的范数方差：沿非平行调和方向，其阶为四阶，而导数能量为二阶。一般负 Einstein 度量的剩余问题是确定其调和乘积核中的秩一正矩阵是否均来自平行形式。

### 负 Kähler–Einstein 背景上的长度缺陷

固定紧负 Kähler–Einstein 曲面或紧轨形 $`(V,g,J,\omega)`$，则

```math
H_g^+=\mathbb R\omega\oplus\mathop{\mathrm{Re}}\nolimits H^{2,0}(V).
```

对 $`\beta\in\mathop{\mathrm{Re}}\nolimits H^{2,0}(V)`$，有精确的点态分解

```math
|b\omega+\beta|^2=2b^2+|\beta|^2.
```

若 $`\beta=\mathop{\mathrm{Re}}\nolimits\theta`$ 具有非零常模长，则全纯典范形式 $`\theta`$ 无零点，因而平凡化 $`K_V`$；这与 $`c_1(V)=[\rho/(2\pi)]\ne0`$ 矛盾。故常模长自对偶调和形式只能是 $`\omega`$ 的常数倍。

令 $`Q_0(\beta)=|\beta|^2-\mathop{\rlap{-}\int}\nolimits|\beta|^2`$。有限维空间 $`\mathop{\mathrm{Re}}\nolimits H^{2,0}(V)`$ 的 $`L^2`$ 单位球面紧，且 $`Q_0`$ 在其上无零点，因此存在依赖该背景的 $`c_V>0`$，使

```math
\|Q_0(\beta)\|_{L^2}\ge c_V\|\beta\|_{L^2}^2.
\tag{L}
```

长度缺陷是二次的，其平方为四次；导数能量则仍为二次。这解释了为什么在 Kähler 方向附近，范数方差与扭率能量不能直接用同阶常数互相控制。

### Kähler 背景的反取向结构

同取向的长度论证对任意紧 Kähler 曲面同样成立：相容自对偶调和形式写为 $`b\omega_I+\mathop{\mathrm{Re}}\nolimits\theta`$，常长度迫使典范形式 $`\theta`$ 具有常模长，从而平行；非 Ricci 平坦时只能是 $`\pm\omega_I`$。

反取向则出现不同的几何。两个正交复结构 $`I,J`$ 此时交换，$`-IJ`$ 为对称对合，给出正交的 $`I`$-不变二平面丛 $`D_+\oplus D_-`$。若

```math
\omega_I=\omega_++\omega_-,\qquad
\Omega_J=\omega_+-\omega_-,
```

则 $`d\omega_\pm=0`$，故它们的核为可积平面分布，叶为极小复曲线。两组叶都全测地恰好等价于 $`\nabla J=0`$。这些是光滑复线分布，不能自动当作全纯线子丛；正交投影若全纯，Hermitian 自伴性已经迫使它平行。

当 $`g`$ 为 KE、$`\mathop{\mathrm{Ric}}\nolimits=Eg`$ 时，按两个分布作常数伸缩

```math
g_{a,b}=a\,g|_{D_+}+b\,g|_{D_-},\qquad a,b>0,
```

仍是 $`I`$-Kähler，其 Ricci 形式不变，Ricci 特征值为 $`E/a,E/b`$。这是 Apostolov–Drăghici–Moroianu 的[常 Ricci 特征值分裂表述](https://arxiv.org/abs/math/0007122)。负特征值时，是否必为平行分裂仍需额外结论。

若 $`x=c_1(D_+^{1,0})`$、$`y=c_1(D_-^{1,0})`$，则 $`xy=\chi`$、$`x^2+y^2=3\tau`$，但两个取向的典范类之间的交叉积为 $`x^2-y^2`$，并未由这些特征数确定。因此，反取向实际类存在本身不能恢复曲面丛中的固定交叉配对证明。对标准局部 $`\mathbb H^2\times\mathbb H^2`$ 度量，两种取向都已有平行 Kähler 形式，故上述同取向论证排除该度量的严格几乎 Kähler 相容形式。

### 联络变分

对于 $`\Lambda^+=\mathbb Rn\oplus n^\perp`$ 上的 Levi-Civita 联络，写 $`\mathcal A=D_0+C`$，其中 $`D_0`$ 保持分裂，$`C`$ 为非对角部分。固定丛上的联络路径 $`\mathcal A_t=D_0+tC`$ 满足

```math
\mathop{\mathrm{YM}}\nolimits(\mathcal A_t)
=\mathop{\mathrm{YM}}\nolimits(\mathcal A)
+2(1-t^2)^2\|F_{D_0}^-\|_2^2.
```

这是固定丛上的联络变分公式。用于度量极值时，还须证明所选联络路径确实由度量的 Levi-Civita 联络诱导；单独改变分裂联络不提供度量下降方向。推导见[整体联系正文](../archive/originals/2026-10-15/Goldberg_Global_Connections_20261015.tex)。

## Einstein 作用量、扭率能量与模空间

对闭定向 Einstein 四维流形定义

```math
\widehat S(g)=V_g^{-1/2}\int_Ms_g\,dV_g,\qquad
D_W(g)=\int_M\left(\frac{s_g^2}{24}-|W_g^+|^2\right)dV_g.
```

Chern–Weil 恒等式给出

```math
D_W(g)=\frac{\widehat S(g)^2}{16}-2\pi^2T_+(M),
\qquad T_+(M)=2\chi(M)+3\tau(M).
\tag{A}
```

若另有相容几乎 Kähler 形式，Sekigawa 型积分恒等式给出

```math
D_W(g)=\mathcal T(g,\Omega),\qquad
\mathcal T(g,\Omega):=\int_M\left(|B|^2+\frac{3q^2}{32}\right)dV_g\ge0.
\tag{T}
```

等号恰好表示 $`\nabla\Omega=0`$。因而

```math
\widehat S(g)^2
=32\pi^2T_+(M)+16\mathcal T(g,\Omega).
```

这将非可积性写成可由度量本身计算的作用量超额。它同时说明，$`D_W`$ 的非负性依赖实际相容闭形式；一般 Einstein 度量不必具有该符号。恒等式的局部计算见[整体联系正文](../archive/originals/2026-10-15/Goldberg_Global_Connections_20261015.tex)。

**命题：作用量在光滑 Einstein 模空间上局部常数。** 取保取向微分同胚和正缩放的商。$`\widehat S`$ 在该模空间的每个连通分支上为常数，并在每个紧子集上只有有限多个值。

证明中须处理模空间的奇点，不能只考虑预先给定的光滑路径。Einstein 度量恰为 $`\widehat S`$ 的临界点。由 Koiso 的局部形变理论，在规范切片中 Einstein 解集是有限维实解析集；缩小邻域后，每一点可由有限段可微的次解析路径连接到基点。沿每一段，$`d\widehat S/dt=0`$，故 $`\widehat S`$ 局部常数。该结论下降到商空间；连通性和紧性分别给出上述两个推论。这里使用的是解析临界集的局部结构，无须假定所有无穷小 Einstein 形变可积。参见 Koiso 的[形变理论](https://www.i-repository.net/contents/osakacu/sugaku/111F0000002-01903-9.pdf)及 Besse，*Einstein Manifolds*，§12.G。

若一个分支含有同取向负 Kähler–Einstein 度量，则该分支上 $`D_W=0`$；其中任何相容几乎 Kähler 结构均由式 (T) 得到可积性。若相容形式诱导相反取向，则同一分支上的扭率能量被固定为

```math
\mathcal T_-=12\pi^2\tau(M).
```

因此 $`\tau\lt 0`$ 时不存在这样的反取向结构，$`\tau=0`$ 时它必为 Kähler；$`\tau>0`$ 时等式只规定扭率能量，尚不给出矛盾。这是固定分支的结论，不把整个 Einstein 模空间假定为连通。

## 典范曲线与扭率能量的积分下界

设 $`\gamma`$ 为第一典范 Hermitian 联络的实曲率形式，$`[\gamma]=2\pi c_1(M,J)`$。对任意单位 $`J`$-复二平面 $`\Pi`$，典范曲率公式给出

```math
\gamma(\Pi)=\frac s4+|\vartheta_{\Pi^\perp}|^2.
\tag{K1}
```

证明使用 $`\gamma=\rho^*-\tfrac12\phi_T`$：$`J`$-反不变曲率分量在 $`\Pi`$ 上为零，$`\rho^*(\Pi)=(s+q)/4`$，而 $`\tfrac12\phi_T(\Pi)=|\vartheta_\Pi|^2`$。由 $`q=4|\vartheta|^2`$ 即得 (K1)。这一典范联络及曲线估计的经典来源是 LeBrun，[*Einstein Metrics, Symplectic Minimality, and Pseudo-Holomorphic Curves*](https://arxiv.org/abs/math/0409290)，§3。

由于 $`s`$ 为常数，

```math
\beta=\gamma-\frac s4\Omega
```

是闭二形式，且在每个 $`J`$-复二平面上非负。故 $`\beta(C)\ge0`$ 对所有 $`J`$-全纯流 $`C`$ 成立；同时 $`\Omega+t\beta`$ 对每个 $`t\ge0`$ 均驯服同一个 $`J`$。因而典范曲率在 $`J`$-全纯曲线生成的锥上满足同一非负性。

令 $`K=-c_1(M,J)`$。只要 $`\mathop{\mathrm{PD}}\nolimits(K)`$ 由 $`J`$-全纯流 $`C_K`$ 表示，就有精确等式

```math
\boxed{\mathcal T-\int_M|v|^2
=2\pi\int_{C_K}|\vartheta^\perp|^2\,dA\ge0.}
\tag{K2}
```

为核对常数，记 $`Q_\vartheta=\int q`$。Weyl 块分解与式 (T) 给出

```math
\frac{|s|}{16}Q_\vartheta=\mathcal T+\int|v|^2,
\qquad
2\pi c_1\cdot[\Omega]=\frac{sV}{2}+\frac{Q_\vartheta}{4}.
```

于是

```math
2\pi[\beta]\cdot K
=-4\pi^2c_1^2+\frac{s^2V}{8}+\frac{sQ_\vartheta}{16}
=\mathcal T-\int|v|^2,
```

再用 (K1) 即得 (K2)。$`v`$ 是本文的单位自对偶标架分量，即 $`|v|^2=|\eta|^2/2`$。这里要求相应类具有 $`J`$-全纯流代表：$`b^+>1`$ 时可使用相应 Taubes 理论；$`b^+=1`$ 时须另核对 chamber 和所用类。

进一步设 $`b^+>1`$、$`K=K_0+\sum_{i=1}^r e_i`$ 为已确定的吹起典范类分解，$`e_i\cdot e_j=-\delta_{ij}`$、$`K_0\cdot e_i=0`$，并且 $`\mathop{\mathrm{PD}}\nolimits(K_0)`$ 及每个异常类 $`E_i=\mathop{\mathrm{PD}}\nolimits(e_i)`$ 都具有相对于这个 $`J`$ 的全纯流代表。在适用的非有理、非直纹曲面吹起范畴中，可由经典带符号基本类及 Taubes 理论得到这些代表。由

```math
[\beta]\cdot K_0\ge0,\qquad
\beta(E_i)=2\pi+\frac{|s|}{4}\int_{E_i}\Omega
```

得到

```math
\boxed{\mathcal T-\int|v|^2
\ge4\pi^2r+\frac{\pi|s|}{2}\sum_i\int_{E_i}\Omega,}
\tag{K3}
```

```math
s^2V\ge32\pi^2K_0^2+32\pi^2r
+8\pi|s|\sum_i\int_{E_i}\Omega.
```

这里对曲线的积分包含各分量重数；奇异流也可按正则部分积分。对任一满足 $`c_1\cdot C=d>0`$ 的 $`J`$-全纯流，还直接有

```math
\int_Cq\,dA\ge8\pi d+|s|\int_C\Omega.
```

因此异常曲线周围不能存在扭率恒为零的邻域。这些积分下界适用于存在上述异常曲线的非极小候选；$`r=0`$ 时仍需其他约束。

另一项经典刚性结论适用于 $`b^-=0`$，见 Kim 的 [harmonic Weyl 结果](https://doi.org/10.1016/j.difgeo.2024.102141)。由 (T) 和签名公式，

```math
8\pi^2(\chi-3\tau)=\mathcal T+3\int|W^-|^2.
```

而 $`b^-=0`$、$`b^+\ge1`$ 给出 $`\chi-3\tau=2-2b_1-2b^+\le0`$，故 $`\mathcal T=0`$，几乎 Kähler 结构可积。一般严格候选必须同时满足 $`b^-\ge1`$ 与 $`\chi>3\tau`$。

## 非塌缩退化中的能量传递

固定闭定向光滑四流形 $`M`$。设 $`g_j`$ 为 Einstein 度量，标量曲率统一为 $`s_0\lt 0`$，体积有正下界、直径有上界。取一个收敛子列，其极限为具有有限奇点集 $`S`$ 的紧 Einstein 轨形 $`(V,g_V)`$，并在 $`V\setminus S`$ 上光滑收敛。这是四维 Einstein 轨形紧性所给的情形；几何背景见 [Ozuch 的非塌缩退化研究](https://arxiv.org/abs/1909.12957)。

记 $`m_+\ge0`$ 为奇点处集中的自对偶 Weyl 总能量。它包括所有核心和颈部，无须先把集中分解为完整气泡树。标量固定和体积收敛给出

```math
D_W(V)=\lim_jD_W(g_j)+m_+.
\tag{D}
```

这里轨形的拓扑量采用曲率定义

```math
T_+^{\mathrm{curv}}(V)
=\frac1{4\pi^2}\int_V\left(2|W^+|^2+\frac{s_0^2}{24}\right)dV,
```

所以

```math
T_+(M)=T_+^{\mathrm{curv}}(V)+\frac{m_+}{2\pi^2}.
```

$`T_+^{\mathrm{curv}}`$ 不应替换成轨形底空间的 $`2\chi+3\tau`$。

### 自对偶 Weyl 与扭率不集中

**定理。** 若每个 $`g_j`$ 还携带同取向相容几乎 Kähler 形式 $`\Omega_j`$，则极限携带光滑轨形几乎 Kähler 形式 $`\Omega_V`$，且

```math
\boxed{m_+=0,\qquad
\mathcal T(g_j,\Omega_j)\longrightarrow\mathcal T(g_V,\Omega_V).}
\tag{NC}
```

证明有两个环节。首先，$`d\Omega_j=d^*\Omega_j=0`$ 和 $`|\Omega_j|^2=2`$ 使椭圆估计可在正则部分使用，得到光滑极限。提升到轨形奇点的穿孔四球后，用截断函数检验 $`d+d^*`$：因形式有界，截止误差由 $`\|d\chi_\epsilon\|_{L^1}=O(\epsilon^3)`$ 控制而趋零。弱方程因此穿过原点，椭圆正则性给出群不变的光滑延拓。闭性、自对偶性和常模长随之保留。

其次，设 $`m_{\mathcal T}\ge0`$ 为扭率密度 $`|B|^2+3q^2/32`$ 的集中质量。两种密度的总质量有界：$`B`$ 是 $`W^+`$ 的块，而 $`q=4t-2s_0/3`$。在光滑流形与极限轨形上分别使用式 (T)，再与式 (D) 比较，得到

```math
\mathcal T(V)+m_{\mathcal T}
=\lim_j\mathcal T(g_j)
=\lim_jD_W(g_j)
=D_W(V)-m_+
=\mathcal T(V)-m_+.
```

两项集中质量非负，故同时为零。这个证明依赖实际闭形式的可去奇点性质，以及两种集中质量在同一恒等式中的相反符号。

在任意光滑曲率尺度极限上，缩放后的 Einstein 常数趋零；由 (NC) 其 $`W^+`$ 为零。相容形式的缩放极限仍闭、自对偶且长为 $`\sqrt2`$，Weitzenböck 公式进一步给出它平行。因此，实际出现的 ALE 核心在继承取向下为 Ricci-flat Kähler。反自对偶 Weyl 能量仍可集中；结论没有排除 Ricci-flat 气泡，也没有给出塌缩序列的紧性。

### Kähler 轨形端点与小扭率序列

设 $`\mathcal C`$ 是光滑 Einstein 模空间的连通子集，并有上述类型的序列趋于同取向 Kähler–Einstein 轨形。式 (A) 与作用量局部常数使 $`D_W`$ 在 $`\mathcal C`$ 上恒定，而式 (D) 给出

```math
D_W|_{\mathcal C}=-m_+\le0.
```

于是 $`\mathcal C`$ 中每个几乎 Kähler–Einstein 度量必为 Kähler；若其中存在此类度量，则还必有 $`m_+=0`$。这是对一个具有指定端点的整个连通分支的限制。

若严格几乎 Kähler–Einstein 度量序列满足 $`\mathcal T_j\to0`$，它必须离开光滑 Einstein 模空间的每个紧子集。若同时满足上述非塌缩和直径条件，则极限为 Kähler–Einstein 轨形，且至少有一个奇点。不同成员可能处于不同连通分支；作用量局部常数本身不排除这种序列。若能另证该轨形的充分小邻域只含有限个 Einstein 连通分支，则各分支的常作用量与极限连续性相结合，才排除严格正的扭率趋零。

相同传递公式也限制一般型吹起流形的 Einstein 极限。对 $`M=X\#k\overline{\mathbb{CP}}^{\,2}`$、$`A=c_1^2(X)>0`$，经典 Ricci 积分下界给出

```math
\widehat S(g)^2\ge32\pi^2(A+k),\qquad D_W(g)\ge4\pi^2k.
```

故在上述非塌缩 Einstein 退化中

```math
D_W(V)\ge4\pi^2k+m_+.
```

当 $`k>0`$ 时，极限主体不能是继承取向下的 Kähler 轨形。这限制了可能的退化几何；它不排除所有小吹起上的 Einstein 度量。

## 负 Kähler–Einstein 端点附近的耦合形变

### 二阶长度障碍

设 $`\mathop{\mathrm{Ric}}\nolimits_g=Eg`$、$`E\lt 0`$，考虑满足耦合 Einstein、闭性、自对偶与常长度方程至二阶的形式展开

```math
g^{-1}g_t=I+tH_1+\frac{t^2}{2}H_2+O(t^3),\qquad
\omega_t=\omega+t\beta_1+\frac{t^2}{2}\beta_2+O(t^3).
```

在同时作用于度量与形式的规范变换后，$`H_1`$ 为反 $`J`$ 不变的 Kodaira–Spencer 方向，$`\beta_1\in\mathop{\mathrm{Re}}\nolimits H^{2,0}`$。负 KE 的二阶 Einstein 正规形给出 $`H_2^+=H_1^2`$；这里上标 $`+`$ 表示 $`J`$-不变部分，而非 Hodge 自对偶部分。该输入及二阶 Einstein 可解性见 [Nagy，Theorem 1.6](https://arxiv.org/html/2603.09028)。

形式与度量混合项可用全纯二形式的一级运输处理。若 $`\beta_1=\mathop{\mathrm{Re}}\nolimits\theta`$，则 Kodaira–Spencer 闭性及 $`\partial\bar\partial`$ 引理产生一个闭形式变分 $`\beta'`$，满足

```math
(\beta')^-=-DP_g^-[H_1]\beta_1,\qquad
\langle\omega,\beta'\rangle=0.
```

因此，二阶闭性与自对偶方程的全部解为 $`\beta_2=2\beta'+\gamma`$，其中 $`\gamma\in H_g^+`$。反 $`J`$ 不变张量与 $`\omega,\beta_1`$ 的交叉收缩为零，度量二阶项又由 $`H_2^+=H_1^2`$ 抵消。长度方程遂化为

```math
|\beta_1|^2+\langle\omega,\gamma\rangle=0.
```

后项为常数，所以唯一剩余的函数障碍是

```math
\mathop{\mathrm{Ob}}\nolimits_2(H_1,\beta_1)
=|\beta_1|^2-\mathop{\rlap{-}\int}\nolimits|\beta_1|^2=Q_0(\beta_1).
```

由式 (L)，它只能在 $`\beta_1=0`$ 时消失。故单独旋转相容形式或加入混合的一阶形变，不能产生严格几乎 Kähler 的二阶方向。纯度量方向仍需研究更高阶 Einstein 方程；二阶结论并未证明所有邻近 Einstein 度量都属于同一个 Kähler 族。

### 自对偶调和形式的颈部迹

对一个既定的轨形—ALE 退化，进一步假设每个核心为渐近 $`\mathbb C^2/\Gamma`$、$`\Gamma\subset\mathrm{SU}(2)`$ 的 Ricci-flat Kähler ALE 空间，且在继承取向下 $`\Lambda^+`$ 有全局平行标架。假设各颈部在共同平行标架中为平坦圆锥加误差 $`e_j`$，满足

```math
r^k|\nabla^ke_j|\le\delta_jw_j(r),\qquad
\int_{\mathrm{neck}}w_j(r)\frac{dr}{r}\le C,\qquad\delta_j\to0.
\tag{N}
```

在 $`A_1`$ 圆锥上，闭自对偶齐次二形式的次数为

```math
\{\ldots,-6,-4\}\cup\{0\}\cup\{2,4,\ldots\}.
```

次数零是孤立常模态。将闭自对偶方程投影到这一模态后，其穿越颈部的变化由 $`C\delta_j\int w_j\,dr/r`$ 控制，故同一常形式连接外部的 $`\omega_V(p)`$ 与核心无穷远的平行形式。核心上有界自对偶调和形式的系数是有界调和函数，由 Ricci 非负的 Liouville 定理为常数。由最大值点的吹起论证还得到

```math
\|\omega\|_{L^\infty(g_j)}\le C\|\omega\|_{L^2(g_j)},\qquad
H^+_{g_j}\longrightarrow H^+_{g_V}.
```

ALE 的 $`L^2`$ 上同调在反自对偶侧，故不增加自对偶调和维数。该估计使 (L) 的常数在这样的 KE 退化中保持正下界。若出现多个尺度，需要在每条颈部验证 (N)；扭率能量不集中本身并不提供这个带导数的匹配条件。

### 常标量 Kähler 比较族的二次法向能量

设光滑化中的消失类 $`\delta`$ 满足 $`\delta^2=-2`$、$`c_1\cdot\delta=0`$。对标量曲率 $`s=4E\lt 0`$ 的 Kähler 比较度量，令 $`\rho`$ 为 Ricci 形式，$`\rho_0=\rho-E\omega`$。它闭、原始且反自对偶，因而调和，并有

```math
P(g)=2\|\rho_0\|_2^2
=-2\bigl(2\pi c_1-E[\omega]\bigr)^2,\qquad
\int_\delta\rho_0=-E\zeta_r,\quad \zeta_r:=\int_\delta\omega.
\tag{C}
```

若 $`\theta=\delta^{1,1}`$、$`\theta^2\to-2`$，且比较类写成
$`[\omega]=\lambda(2\pi c_1/E+\epsilon\theta)`$，由常标量归一化求出 $`\lambda`$ 后，得到

```math
\frac{P(g)}{E^2\zeta_r^2}
=-\frac2{\theta^2}-\frac{E^2\epsilon^2}{2\pi^2c_1^2}\longrightarrow1.
```

这给出上述比较度量族的二次法向能量。对谐和原始 $`(1,1)`$ 形式 $`\theta`$，对应 Hermitian 无迹无散张量满足 $`\Delta_EH_\theta=-2EH_\theta`$；若线性化取 $`\tfrac12\Delta_E`$，相应特征值为 $`-E`$。该正下界只属于 Hermitian 扇区，不能代替反 Hermitian 核补空间的统一谱估计。

要由 (C) 排除节点端点附近的所有非 Kähler Einstein 度量，还须在同一个有限维约化中建立：统一的补空间逆；所有可实现的局部周期方向上的比较族；比较度量与约化度量之间的加权 $`o(|\zeta_r|)`$ 误差；以及覆盖全部约化参数的相对 $`C^0`$ 匹配。满足这些条件时，单位 $`L^2`$ 法向测试下的约化障碍为

```math
\Lambda_I=E\zeta_r+o(|\zeta_r|).
```

拓扑度保证比较族覆盖目标参数，Einstein 方程 $`\Lambda_I=0`$ 随即强迫 $`\zeta_r=0`$，再由 $`[\rho_0]=0`$ 和调和性得到 KE。一般多尺度节点、局部周期不能独立实现或补空间估计退化时，尚未建立这条全覆盖连接。公式 (C) 是精确结论；邻域内所有 Einstein 解的分类仍以这些匹配条件为前提。

## Weyl 耦合方程与闭流形上的可积性问题

令 $`D`$ 为保持 $`\mathbb Rn\oplus n^\perp`$ 的投影联络，写

```math
\nabla=D+C,\qquad
C_i=\begin{pmatrix}0&-p_i^T\\p_i&0\end{pmatrix}.
```

几乎 Kähler 类型关系与调和性给出

```math
\sum_i p_i p_i^T=\frac q4I_{n^\perp},\qquad D^*p=2v.
```

Einstein Weyl 方程的无迹横向块为

```math
D^*DB+\left(\frac{3s}{2}+2q\right)B
=2\sum_i[p_i(D_iv)^T+(D_iv)p_i^T]_0
+2(vv^T)_0,
```

其中 $`[\cdot]_0`$ 表示二维块的无迹部分。该方程光滑穿过扭率零集。与 $`B`$ 配对并分部积分，得到

```math
\int_M\left[|DB|^2+\left(\frac{3s}{2}+2q\right)|B|^2
+4\sum_i\langle(D_iB)p_i,v\rangle-10\langle Bv,v\rangle\right]dV=0.
```

在扭率零点，零阶系数 $`3s/2`$ 为负，源项仍耦合 $`v`$ 及其导数，因而这个恒等式并不具有直接迫使 $`B=0`$ 的正性。推导见[完整 Weyl 方程正文](../archive/originals/2026-10-15/Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex) §5。

上述结果尚未解决闭负 Goldberg 的一般情形。严格非 Kähler 候选须同时具有非空扭率零集、零点处严格为正的行列式 Green 势、正的作用量超额，以及满足上述微分方程的横向 Weyl 分量。它所属的 Einstein 连通分支不含同取向 KE 度量，也不能以同取向 KE 轨形为非塌缩端点。不同分支之间的极限、塌缩与直径发散仍可能发生。

沿 Green 势方法，需由原始 Einstein–几乎 Kähler 系统进一步控制零点处的整体曲率配对；沿调和乘积方法，需限制负 Einstein 度量所实现的秩一核；构造方向则需得到闭的精确 Einstein 相容结构。上述条件分别给出闭负 Goldberg 问题的充分条件与可能的构造途径。

零点、Green 势与完整 Weyl 方程的连续证明见[合并正文](../research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)。Armstrong 的零点存在性、Derdziński 的 Weyl 方程、Sekigawa 恒等式、第三 Gray 定理、di Scala–Nagy 唯一性及 Watson 的浸没刚性作为经典输入保留各自出处。

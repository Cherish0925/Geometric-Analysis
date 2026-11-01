# 曲率极值、几何构造与退化

Shuxing Yang, Junyao Wu, Rui Zhao, Hongsheng Chen, Yihao Yang  
Qiushi Engine Team, Zhejiang University · [作者与通讯信息](../AUTHORS.md)

本文研究闭四维流形上无迹 Ricci 曲率平方积分的下确界、极小值取得性及极小化序列的退化。规范理论给出下界，曲率插入构造给出上界，变分与极限分析描述可能的极值几何。讨论分别涉及光滑流形、具有指定奇点的轨形和完备有限体积 Einstein 流形。

## 1. 泛函与共形归约

设 $`M`$ 为闭连通定向光滑四维流形。Ricci 使用张量范数；Weyl 和完整曲率作为二形式上的自伴算子，使用 Hilbert–Schmidt 范数。记

```math
P=\int_M|\mathop{\mathrm{Ric}}\nolimits^{\circ}|^2,\quad S=\int_Ms^2,\quad
I_\pm=\int_M|W^\pm|^2,\quad W=I_++I_-,\quad
R=\int_M|\mathop{\mathrm{Ric}}\nolimits|^2=P+S/4,
```

```math
V=\mathop{\mathrm{Vol}}\nolimits(M,g),\quad T_s=\int_Ms,\quad
L_s=S-T_s^2/V,\quad T_\pm=2\chi(M)\pm3\tau(M).
```

所有积分取 $`dV_g`$。定义

```math
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int|\mathop{\mathrm{Ric}}\nolimits_g-\lambda g|^2}{\lambda^2V},\qquad
P_*(M)=\inf_gP(g),\qquad\alpha(M)=\inf_g\mathcal E(g).
```

当 $`R>0`$ 时，$`\mathcal J=4P/R`$，直接对 $`1/\lambda`$ 极小化得

```math
\mathcal E=4-\frac{T_s^2}{VR}=\mathcal J+\frac{L_s}{R}.
\tag{1.1}
```

Ricci-flat 度量满足 $`\mathcal E=4`$，此时 $`\mathcal J`$ 不定义。四维整体缩放保持 $`P,S,I_\pm`$ 不变。Chern–Weil 恒等式为

```math
4\pi^2T_\pm=\frac S{24}+2I_\pm-\frac P2,
\qquad
\int|\mathop{\mathrm{Rm}}\nolimits_{\rm op}|^2=8\pi^2\chi+P.
\tag{1.2}
```

因此全曲率极小化与 $`P`$ 极小化等价；$`\alpha`$ 还取决于分母和标量方差，不能通过相减两个独立下确界求得。

### 1.1 负 Yamabe 代表与两种极值的比较

同一负 Yamabe 共形类中，令 $`\widehat g`$ 为常标量代表，$`\delta=S(g)-S(\widehat g)\ge0`$。共形不变的 Weyl 能量和 (1.2) 给出

```math
P(g)=P(\widehat g)+\delta/12,\qquad
R(g)=R(\widehat g)+\delta/3,
```

```math
\mathcal J(g)=
\frac{R(\widehat g)}{R(\widehat g)+\delta/3}\mathcal J(\widehat g)
+\frac{\delta/3}{R(\widehat g)+\delta/3}.
\tag{1.3}
```

特别地，$`\mathcal J(g)\lt 1`$ 时 $`\mathcal E(\widehat g)=\mathcal J(\widehat g)\le\mathcal J(g)`$。若每个共形类均为负类且 $`\inf\mathcal E\lt 1`$，便有 $`\inf\mathcal E=\inf\mathcal J`$。

设每个共形类均为负 Yamabe 类，全度量标量下界为 $`S\ge32\pi^2A>0`$，且 $`T_+>0`$。写 $`p_*=P_*/(8\pi^2)`$。对 $`P`$ 极小化序列作负 Yamabe 替换，并用 $`I_+\ge0`$，得到

```math
\frac{p_*}{p_*+3T_+/4}
\le\alpha(M)\le\frac{4p_*}{A+p_*}.
\tag{1.4}
```

左式来自 $`R\le4P+24\pi^2T_+`$；右式使用 $`R\ge P+8\pi^2A`$。在这些假设下，$`P_*=0`$ 与 $`\alpha=0`$ 等价。精确的常标量公式是

```math
\mathcal E(\widehat g)=\frac{16P(\widehat g)}{4P(\widehat g)+Y([g])^2},
\tag{1.5}
```

其中 $`Y([g])`$ 为 Yamabe 常数。省去分母的 $`4P`$ 只给出一个上界，不能用于精确归一化。

### 1.2 全局 Weyl–Yamabe 极值公式

令 $`d([g])=8\pi^2\chi-W(g)`$。由 Gauss–Bonnet，

```math
P=S/12-2d,\quad R=S/3-2d,\quad
\mathcal E-1=\frac{L_s-6d}{R}.
\tag{1.6}
```

在 $`d>0`$ 的共形类中，$`Y\ne0`$，且 $`S\ge Y^2`$；常标量 Yamabe 代表达到这个最小值。因 $`1-6d/(S/3-2d)`$ 随 $`S`$ 递增，(1.1) 给出类内最小值。全局于是满足

```math
\boxed{\displaystyle
\alpha(M)=1-6\sup\left(\{0\}\cup
\left\{\frac{d([g])}{Y([g])^2/3-2d([g])}:d([g])>0\right\}\right).}
\tag{1.7}
```

公式中的上界 $`\alpha\le1`$ 可独立构造：在一个正规点插入长度 $`L`$ 的单位圆柱 $`S^3\times[0,L]`$，两端采用固定过渡。圆柱上 $`s=6`$、$`|\mathop{\mathrm{Ric}}\nolimits|^2=12`$、$`|\mathop{\mathrm{Ric}}\nolimits^{\circ}|^2=3`$，故 $`4P,R`$ 均为 $`24\pi^2L+O(1)`$，而 $`L_s=O(1)`$。于是 $`\mathcal E\to1`$。同一构造适用于有孤立奇点的紧轨形的正规点。

因此

```math
\alpha(M)\lt 1\quad\Longleftrightarrow\quad
W_*(M):=\inf_gW(g)\lt 8\pi^2\chi(M).
\tag{1.8}
```

签名不等式 $`W\ge12\pi^2|\tau|`$ 又给出

```math
2\chi\le3|\tau|\quad\Longrightarrow\quad\alpha=1.
\tag{1.9}
```

严格小于时不取得；等号时，取得要求相应手性的 Weyl 张量消失且标量为非零常数。例如 $`\mathop{\mathrm{MinVol}}\nolimits(M)=0`$ 给出 $`P_*=0`$，同时 $`\chi=\tau=0`$，所以 $`\alpha=1`$。零绝对能量下确界与零相对缺陷下确界在没有 (1.4) 的输入时可以完全不同。

连通和的 Weyl 恢复给 $`W_*(M\#N)\le W_*(M)+W_*(N)`$。若 $`d_*=8\pi^2\chi-W_*`$，则

```math
d_*(M\#N)\ge d_*(M)+d_*(N)-16\pi^2.
```

例如 $`\#n\overline{\mathbb{CP}}^{\,2}`$ 满足 $`W_*=12n\pi^2`$、$`d_*=4\pi^2(4-n)`$，故 $`n\le3`$ 时 $`\alpha\lt 1`$，$`n\ge4`$ 时 $`\alpha=1`$。

来源：[相对缺陷与联合共形极值](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §§1、5–6。

### 1.3 绝对 Ricci 能量的全部近极小序列

设 $`T_+=A-d`$，$`A>0,d\ge0`$；对所考虑的每个共形类，单极子解的存在性保证经典标量及混合曲率估计，且所选投影平方 $`p\ge A`$。令

```math
C=8\pi^2A,\qquad H=8\pi^2d,\qquad j=R-C-H.
```

则对每个这样的度量，

```math
j\ge0,\qquad H-\sqrt{j(C+j)}\le P\le H+j.
\tag{1.10}
```

这一选择结论适用于所有接近经典 Ricci 能量下界的度量。证明令

```math
D=\frac1{4\pi^2}\int\left(\frac{s^2}{24}+\frac{|W^+|^2}{2}\right)-\frac p2\ge0,
\qquad B_p=S-32\pi^2p\ge0.
```

Chern–Weil 给 $`j=16\pi^2(p-A)+32\pi^2D`$。再写 $`q=-s+\sqrt6|W^+|`$、$`t=s+2\sqrt6|W^+|`$，有

```math
144\pi^2D=\left(\int q^2-72\pi^2p\right)+\tfrac12\int t^2,
\qquad s=(t-2q)/3.
```

括号内非负；展开 $`S`$ 并对 $`\int qt`$ 使用 Cauchy–Schwarz，得到
$`0\le B_p\le2j+4\sqrt{j(C+j)}`$。代入
$`P=H+j-8\pi^2(p-A)-B_p/4`$ 即得 (1.10)。因此固定 $`A,d`$ 时，$`j_i\to0`$ 强迫

```math
P_i\to H,\quad S_i\to4C,\quad
\mathcal E(g_i)=\frac{4H}{C+H}+\frac{L_s(g_i)}{C+H}+o(1).
\tag{1.11}
```

标量方差是原度量上独立的余项；负 Yamabe 替换使它消失并保持 $`0\le\widehat j\le j`$。若 $`P=0`$，则 (1.10) 还给
$`j\ge(\sqrt{C^2+4H^2}-C)/2`$：任何 Einstein 候选必须偏离该绝对 Ricci 能量极小值。这里没有将两个独立下确界相减。

来源：[Ricci 能量选择及完整证明](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/mathematics/current/line1_energy_selection.md) §§2–5。

## 2. 曲率插入构造与严格上界

### 2.1 固定复双曲领口内的吹起构造

区间积分给出有限尺度光滑单元的严格上界。解析构造进一步证明：每个固定半径 $`R_0>0`$ 的复双曲领口内，都存在普通负单吹起单元，在外部精确等于 $`\mathop{\mathrm{Ric}}\nolimits=-6g`$，并满足

```math
\frac{P(g_\epsilon)}{8\pi^2}
=1-9\epsilon^2\log(1/\epsilon)+O_{R_0}(\epsilon^2),
\qquad
\frac{J_6(g_\epsilon)}{8\pi^2}
=1-9\epsilon^2\log(1/\epsilon)+O_{R_0}(\epsilon^2),
```

其中 $`J_6(g)=\int|\mathop{\mathrm{Ric}}\nolimits_g+6g|^2`$。两式均包括 Burns 核心、颈部和外过渡；内外过渡的总误差为 $`O_{R_0}(\epsilon^2)`$。因此充分小的正 $`\epsilon`$ 给出 $`P,J_6\lt 8\pi^2`$。

来源：[固定复双曲领口内的对数渐近展开](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) §§0–6。颈部推导及符号计算程序见该文 §8。

### 2.2 覆盖量词和极限次序

设 $`X_0`$ 为固定紧复双曲曲面，$`X_j\to X_0`$ 为度数趋于无穷的有限非分歧覆盖，$`A_j=c_1^2(X_j)`$。令

```math
M_j=X_j\#k_j\overline{\mathbb{CP}}^{\,2}\#\ell_j(S^1\times S^3).
```

考察满足下列比例的手术族：

```math
Q_j=k_j+4\ell_j\to\infty,\quad h_j=Q_j/A_j\to0,\quad
k_j/Q_j\to2/9,\quad\ell_j/Q_j\to7/36
```

在这些比例下，适合基底小嵌入球的固定单元可复制至 $`M_j`$，得到

```math
\limsup_j\frac{\alpha(M_j)}{h_j}
\le4-\frac89\delta_{X_0}\lt 4.
```

其中 $`\delta_{X_0}>0`$ 是固定单元相对于 $`8\pi^2`$ 的归一化能量下降量，可依赖 $`X_0`$。极限次序为：固定领口和一个足够小的正插入参数，再令覆盖度数趋于无穷。

另一路使用一个已有固定半径单元：对于事先给定、嵌套且子群交集平凡的残余覆盖塔，某一级以后具有正比例的该单元安放位置。此结论也适用于非正规塔，仅使用固定球在某一级的嵌入。在该量词下，区间计算与共形尾部恢复给出

```math
\limsup_j\alpha(M_j)/h_j\le3.9961446513521015108\ldots\lt 4.
```

区间计算给出特定单元的显式上界；任意固定小领口的构造扩大了覆盖序列的适用范围。

来源：[有限覆盖上的曲率插入与恢复序列](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §§3–5；任意固定基底覆盖序列的扩展见 [固定复双曲领口内的对数渐近展开](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) §6。

令 $`\mathfrak P_{8n,7n}`$ 为具有 $`8n`$ 个吹起、$`7n`$ 个柄及固定完整外部标记的混合单元 $`P`$ 能量下确界。次可加性给出

```math
\gamma_{\rm bal}=\lim_{n\to\infty}
\frac{\mathfrak P_{8n,7n}}{72\pi^2n}
=\inf_n\frac{\mathfrak P_{8n,7n}}{72\pi^2n},
\qquad \limsup_j\alpha(M_j)/h_j\le\gamma_{\rm bal}.
```

反向不等式需要将一般竞争度量局部化至该单元范畴，或建立相应全局下界。

### 2.3 一般背景的张量机制

在一般负 Kähler–Einstein 背景上，节省量由插入方向与背景曲率的耦合决定。写 $`R^+=W^++sI/12`$，表示自对偶曲率块，与积分量 $`R`$ 采用不同记号。首先，对任意固定光滑背景、任意点 $`p`$ 和单位方向 $`\zeta\in\Lambda_p^+`$，以 $`x^{1/5}`$ 为截断半径插入异常面积为 $`\pi x`$ 的 Burns 核心，得到

```math
P(g_x)=P(g)+8\pi^2\bigl(1-xR^+_p(\zeta,\zeta)\bigr)+O(x^{6/5}).
```

证明由标量平坦、自对偶平坦的 Burns 尾部及其球面 transgression 给出；其中标量通量为 $`4\pi^2x`$，自对偶通量为 $`\pi^2\zeta\otimes\zeta`$。在负 KE 背景上，$`\omega^\perp`$ 是一阶响应的核；实双曲背景则 $`R^+=sI/12\lt 0`$，每个方向的一阶能量变化均为正。这个任意背景的一阶结论不要求 $`P`$-临界性。

若背景在插入支撑邻域内为 $`P`$-临界，再选择角修正，可进一步展开为

```math
P(g_\epsilon)=P(g)+8\pi^2-8\pi^2\epsilon R^+_p(\zeta,\zeta)
 +4\pi^2\Phi\epsilon^2\log(1/\epsilon)+O(\epsilon^2).
```

当 $`\mathop{\mathrm{Ric}}\nolimits^{\circ}_p=0`$、$`R^+\zeta=\mu\zeta`$ 时，优化系数为

```math
\Phi=-\mu(\mu-s/8)-|T|^2,\qquad
T=(R^+|_{\zeta^\perp})^{\circ}.
```

角修正使反手性 Weyl 二阶背景项在目标曲率组合 $`(2W^+,s/\sqrt{12})`$ 中消去。核方向上的负对数项为 $`-4\pi^2|T|^2\epsilon^2\log(1/\epsilon)`$。在负 KE 背景的垂直方向，$`|T|^2=s^2/32`$，故固定 $`k`$ 个点的构造满足

```math
\frac{P(\widetilde g_\epsilon)}{8\pi^2}
=k-\frac{ks^2}{64}\epsilon^2\log(1/\epsilon)+O(\epsilon^2)\lt k.
```

这里 $`T`$ 是 $`\zeta^\perp`$ 上限制算子的无迹部分；$`\Phi`$ 为插入角修正所确定的二阶对数系数。系数公式适用于所列特征向量方向；一般方向还含旋转零模。其非正性在核方向成立，在整个 $`R^+\le0`$ 锥上则不成立。余项常数依赖固定光滑背景和插入数据。

来源：[一般背景的曲率插入展开](../archive/originals/2026-10-08/01_Research_Synthesis.tex) §3。

展开中的对数项可以由三个区域区分出来。取 Burns 尾部 $`A_0=\partial\bar\partial_\zeta\log r^2`$，在固定背景的正规坐标中插入 $`\epsilon A_0`$ 和零次齐次角修正。内区 $`r\asymp\sqrt\epsilon`$ 的误差是 $`O(\epsilon^2)`$；外过渡的一阶变分由背景的局部 $`P`$-临界性消去，余项也是 $`O(\epsilon^2)`$。中间区以 $`\sigma=\epsilon/r^2`$ 展开，其径向密度具有形式

```math
\epsilon r\,\gamma_1(r)
+\frac{\epsilon^2}{r}\gamma_2(r)
+\frac{\epsilon^3}{r^3}\gamma_3(r,\sigma),\qquad
\gamma_2(0)=8\pi^2\Phi.
```

积分区间下端为 $`O(\sqrt\epsilon)`$，故第二项产生 $`4\pi^2\Phi\epsilon^2\log(1/\epsilon)`$。背景三阶及更高阶项均只进入可积余项。反手性消去必须同时计入 Hodge 投影随度量的变化。

这证明对每个固定极小一般型曲面 $`X`$ 和每个 $`k\ge1`$，

```math
\boxed{P_*(X\#k\overline{\mathbb{CP}}^{\,2})\lt 8\pi^2k.}
\tag{2.1}
```

若典范模型有 ADE 奇点，先在正规部固定插入点和一个正的能量下降量，再令 Ricci-flat 解消尺度趋零；不能将这两个选择顺序倒置。常数依赖背景，对任意共同退化背景的一致性不由此得到。

### 2.4 归一化上界与不相交插入区域

设一个固定复双曲单元的完整 $`P`$ 能量为 $`8\pi^2p_c`$，$`p_c\lt 1`$。在复双曲覆盖中能安放 $`8n`$ 个该单元和 $`7n`$ 个独立柄单元时，令 $`Q=36n`$、$`h=Q/A`$、

```math
C_c=\frac{28}{9}+\frac89p_c.
```

柄单元来自 $`S^1\times S^3`$ 的标量平坦、共形平坦 Green 构造，$`P`$ 能量为 $`32\pi^2`$。其尺度取 $`\delta`$、拼接半径取 $`\sqrt\delta`$，过渡能量和尾部误差均为 $`O(\delta^2)`$。因此 (1.4) 给出有限参数上界

```math
\boxed{\frac{\alpha(M)}h\le\frac{C_c}{1+C_ch/4}.}
\tag{2.2}
```

已构造的单元满足 $`p_c\lt 0.995662732772`$，从而 $`C_c\lt 3.996144651353`$。这里不需要先令 $`h\to0`$；假设是所需完整单元确实能同时安放。选择一个具有足够大整体注入半径的有限正规覆盖后，其所有进一步有限覆盖继承这些位置。对任意固定基底覆盖序列，则使用 §2.1 的小领口单元，节省常数允许依赖基底。

一般固定负 KE 背景也可取局部单元的固定能量下降量 $`\eta_X>0`$。若吹起占 $`Q=k+4\ell`$ 的比例为 $`\vartheta=k/Q`$，相应构造给

```math
\frac{\alpha(M)}h\le
\frac{4(1-\vartheta\eta_X)}{1+h(1-\vartheta\eta_X)}.
\tag{2.3}
```

这不自动把上述平衡手术族的线性下界推广到所有 KE 背景。非复双曲背景的 $`3c_2-c_1^2`$ 在有限覆盖下同比例增长，其原有 Weyl 余量可能使指定的平衡小 $`h`$ 条件无法实现。

允许主体自身变化时，可以明确计算这一余量的作用。设负 KE 主体 $`X_j`$ 有 $`A_j=c_1^2(X_j)`$、$`\Delta_j=3c_2(X_j)-A_j\ge0`$，并有足够多彼此分离、在 $`C^2`$ 中趋近固定复双曲模型球的插入位置。取

```math
Q_j=k_j+4\ell_j=o(A_j),\quad h_j=Q_j/A_j,\quad
\vartheta_j=k_j/Q_j\to\vartheta,\quad r_j=\Delta_j/Q_j\to r,
\quad\sigma=4r+18\vartheta.
```

在逐共形类的单极子解存在性及类平方条件下，已有线性强制常数 $`c_0>0`$ 给出

```math
\liminf_j\frac{\alpha(M_j)}{h_j}
\ge\max\left\{\frac43(3-\sigma)_+,\frac{18}{19}(4+c_0-\sigma)_+\right\},
\qquad
\limsup_j\frac{\alpha(M_j)}{h_j}\le4(1-\eta\vartheta),
\tag{2.3a}
```

其中 $`8\pi^2(1-\eta)`$ 是插入单元的完整残差能量。下界来自精确式
$`3T_-/A=1+(\sigma_j-3)h_j`$ 及

```math
P=\frac{S-32\pi^2A}{12}+4I_-+\frac{8\pi^2Q}{3}(3-\sigma_j).
```

上界的 KE 主体残差为零，故只含吹起比例 $`\vartheta`$。分歧 Picard 覆盖构造满足 $`A_n\asymp p^{8n}`$、$`\Delta_n\asymp p^{6n}`$，且提供所需的正比例模型位置：对 $`r>0`$ 取 $`Q_n\sim\Delta_n/r`$，对 $`r=0`$ 取 $`Q_n\sim p^n\Delta_n`$，均有 $`h_n\to0`$。这实现了上述两参数范围内的几何族。

主体的反手性能量恰为 $`I_-^{\rm KE}=8\pi^2\Delta/3`$。若某竞争族保留它至 $`o(Q)`$，同一恒等式给 $`\mathcal E\ge4h(1-6\vartheta)+o(h)`$；要突破此界，必须改变主体的反手性能量。在环面上的精确 cusp-closing 模型

```math
g=t(dx^2+dy^2)+\frac{dt^2}{\Theta(t)}+\Theta(t)\eta^2,
\quad d\eta=dx\wedge dy,\quad
\Theta(t)=\tfrac23t^2-c/t,
```

有 $`s=-4`$、$`|W^+|^2=2/3`$、$`|W^-|^2=6c^2/t^6`$。在平滑闭合截面 $`t_0=(3c/2)^{1/3}`$ 取所需圆周期，若该截面的自交为 $`-e`$，直接积分得 $`I_-=8\pi^2e/3`$。这明确了该构造中反手性余量的几何位置。

来源：[分歧 KE 族的两参数曲率律](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md) §§0–4。

### 2.5 Weyl 能量上界与吹起数的范围

固定外领口的复双曲单元满足相对恒等式

```math
p_c-1=\frac{\Delta I_+}{2\pi^2}+\frac{\Delta S}{96\pi^2}.
```

若 $`\eta=-\Delta I_+/(2\pi^2)>0`$，在 $`Y`$ 的 $`N`$ 个不相交固定球中选 $`n\le\min(k,N)`$ 个使用该单元，其余吹起采用小尺度经典恢复，则

```math
d_*(Y\#k\overline{\mathbb{CP}}^{\,2})
\ge4\pi^2\left(A/3-k+\eta n\right).
\tag{2.4}
```

所以 $`k\lt A/3+\eta n`$ 已保证 $`\alpha\lt 1`$。这改善了只由 Kähler 恢复看到的 $`k\lt A/3`$ 区域。

该结论取决于能够同时选取的不相交插入球的数目。在 $`\mathop{\mathrm{Ric}}\nolimits=-g`$ 的复双曲归一化中，令 $`X_R=\sinh^2(R/\sqrt6)`$。若整体注入半径大于 $`2R`$，最大不相交 $`R`$-球族满足

```math
\frac{1}{9[4X_R(1+X_R)]^2}\le\frac NA\le\frac1{9X_R^2}.
```

上述球数估计给出了 $`k\lt A/3`$ 之外的适用区间。插入球的尺度和数目共同决定全局能量下降量。式 (2.2)–(2.4) 给出上界；与之匹配的下界仍待确定。

### 2.6 无对称限制的完整单元共形归约

令完整光滑单元在紧集外精确等于 $`\mathop{\mathrm{Ric}}\nolimits=-6g`$ 的复双曲端，并固定端部识别。存在唯一正函数 $`u\to1`$ 满足

```math
-6\Delta_gu+s_gu+24u^3=0,\qquad \widehat g=u^2g,\quad s_{\widehat g}=-24,
```

其中 $`\Delta=\mathop{\mathrm{div}}\nolimits\nabla`$。不要求原度量的标量处处为负，也不要求任何对称性。证明在精确端上用 $`1-e^{-a(r-R)}`$ 与 $`1+(M-1)e^{-a(r-R)}`$ 作上下屏障，在核心内分别延为零和足够大的常数，随后作穷竭并使用强最大值原理。线性化 $`-6\Delta+48`$ 给出

```math
|\nabla^j(u-1)|=O(e^{-mr}),\qquad 4\lt m\lt 2+2\sqrt3,
```

对每个固定 $`j`$ 成立。这个衰减快于端的体积增长，故共形 transgression 的线性边界项消失，得到精确能量差

```math
P(g)-P(\widehat g)
=24\int|\nabla u|^2+3\int(\Delta u/u)^2,
\tag{2.5}
```

```math
J_6(g)-J_6(\widehat g)
=P(g)-P(\widehat g)+\frac14\int(s_g+24)^2.
```

因而，在同一标记单元上，精确复双曲端的 $`P`$ 与 $`J_6`$ 下确界相等，也等于常标量 $`-24`$、渐近速率 $`\mu`$ 满足 $`2\lt \mu\lt 2+2\sqrt3`$ 的单元的 $`P`$ 下确界。逆向证明将渐近端在单位环带上截回精确端，附加平方残差为 $`O(e^{(4-2\mu)R})`$。这一步给下确界归约，不给取得性。

若单元有 $`k`$ 个吹起和 $`\ell`$ 个柄，相对模型球的 Weyl 差为 $`\Delta I_+`$，则

```math
P(\widehat g)-8\pi^2(k+4\ell)=4\Delta I_++48\mathop{\mathrm{RV}}\nolimits(\widehat g).
\tag{2.6}
```

相对体积 $`\mathop{\mathrm{RV}}\nolimits`$ 包含匹配截面的原体积差及完整单元上的 $`\int(u^4-1)dV_g`$。改变截面但保持端部识别不改变它。Weyl 能量的减少必须与这同一个常标量代表的相对体积共同计算；单独一个负 Weyl 差不能给出 $`P`$ 的最优值。

来源：[完整复双曲端的共形归约与证明](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md)；[相对曲率恒等式](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md) §1。

### 2.7 领口的约束分解与标准端截断

对一般 Gaussian 领口 $`g=dt^2+h_t`$，令 $`K=\frac12\partial_th_t`$、$`\Theta=\mathop{\mathrm{tr}}\nolimits_{h_t}K`$。Gauss–Codazzi 及切向演化方程把无迹 Ricci 分为

```math
\mathcal C=\tfrac12(\Theta^2-|K|^2-R_h)+s/4,
\quad\mathcal M=\mathop{\mathrm{div}}\nolimits_hK-d\Theta,
\quad\mathcal S=(\mathop{\mathrm{Ric}}\nolimits^{h_t}-\partial_tK-\Theta K+2K^2)^{\circ_h},
```

并给精确正交恒等式

```math
|\mathop{\mathrm{Ric}}\nolimits^{\circ}|^2=\frac43\mathcal C^2+2|\mathcal M|^2+|\mathcal S|^2.
\tag{2.17}
```

因此任一满足下式的输运恒等式
$`\mathcal A_b-\mathcal A_a-\mathcal F=\int_C(f\mathcal C+\langle X,\mathcal M\rangle+\langle T,\mathcal S\rangle)`$
都给

```math
P(C)\ge\frac{|\mathcal A_b-\mathcal A_a-\mathcal F|^2}
{\int_C(\frac34f^2+\frac12|X|^2+|T|^2)}.
\tag{2.18}
```

$`\mathcal F`$ 是参考几何自身的演化，不能省去。不同输运量若使用相同残差分量，其下界一般只能取最大值；只有支撑或正交分量分离时才能相加。式 (2.17) 也没有单独控制 $`K`$、$`R_h`$ 或领口半径，因而不替代领口的提取定理。

在 $`g=dt^2+\sum_{i=f,g,h}a_i^2\sigma_i^2`$、$`d\sigma_i=2\sigma_j\wedge\sigma_k`$ 的对角领口，置
$`y_i=a_i'/a_i`$、$`\mathcal V=a_fa_ga_h`$、$`\kappa=a_f/(a_ga_h)`$、$`q=\log(a_g/a_h)`$、$`\zeta=1/(a_ga_h)`$。CR 形变可由

```math
\Phi=q+\frac{y_g-y_h}{4}-\zeta\sinh q
```

追踪，其精确方程为

```math
\Phi'=F-\frac14(\mathop{\mathrm{Ric}}\nolimits^{\circ}_{gg}-\mathop{\mathrm{Ric}}\nolimits^{\circ}_{hh}),
\tag{2.19}
```

```math
F=(y_g-y_h)\left(1-\frac{y_f+y_g+y_h}{4}-\zeta\cosh q\right)
+\zeta\sinh q\,(y_g+y_h-2)
+\frac{2\zeta^2}{\kappa^2}\sinh(2q).
```

于是

```math
\left|\Delta\Phi-\int_I F\,dt\right|
\le\left(\frac{P(I)}{16\pi^2}\right)^{1/2}
\left(\int_I\frac{dt}{\mathcal V}\right)^{1/2}.
\tag{2.20}
```

在规定的小渐近复双曲块内，横向变量为 $`O(\zeta)`$，从而 $`F=\zeta^2G`$、$`G`$ 有界；这项估计不对任意对角几何成立。若 $`\mathcal V\ge ce^{4t}/16`$，将漂移尾积分记作 $`\delta_T`$，则将无穷远 CR 数据恢复为标准值所需的能量满足
$`P([T,\infty))/(8\pi^2)\ge(c/2)e^{4T}(|\Phi(T)|-\delta_T)_+^2`$。
系数 $`1/2`$ 是标准端线性问题的最优值。因此在已经展开的大体积非标准 CR 端，恢复标准无穷远具有正的能量下界。

反之，若完整对角端始终处于一个充分小的标准渐近复双曲块，$`s=-24`$、$`P\lt \infty`$ 且 $`\Phi(t)\to0`$，则存在保持任意给定内部紧集、外部精确复双曲的 $`g_R`$，满足

```math
P(g_R)\longrightarrow P(g).
\tag{2.21}
```

证明需先匹配径向相位。在状态 $`(y_f,y_g,y_h,\kappa,q,\zeta)`$ 中，线性速率为 $`2,0,-2,-4,-6,-8`$；$`-2`$ 模态正是精确复双曲曲线

```math
H(z)=\left(\sqrt{1+z}+\frac1{\sqrt{1+z}},\sqrt{1+z},\sqrt{1+z},\sqrt{1+z},0,z\right)
```

的切向。扣除同 $`\zeta`$ 的 $`H`$ 后，$`P\lt \infty`$ 给加权残差 $`e^{2t}e\in L^2`$，其中 $`e_i=\mathop{\mathrm{Ric}}\nolimits_{ii}+6`$。稳定方向用 Duhamel 公式，出射方向用有界终端条件，零速率方向用 (2.20)；余项吸收遂给所有物理偏差 $`o(e^{-2t})`$。将相位匹配后的 $`D_i=\log a_i-\log a_i^{\rm CH}`$ 在 $`[R,R+1]`$ 截断，附加能量不超过

```math
C\int_R^{R+1}\mathcal V|e|^2dt
+C\mathcal V(R)\sup_{[R,R+1]}(|D|+|D'|)^2=o(1).
```

同法对 $`J_6\lt \infty`$ 给 $`J_6`$ 的截断收敛。若完整标准端类的下确界为零，仍需取得性才能得到 Einstein 填充；(2.21) 本身仅连接两个极值域。

来源：[无对称约束分解](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step34_characteristic_constraint_calculus_and_N_probe.md) §2；[CR 输运与标准端截断](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step26_truncation_flux_and_branch_completeness.md) §§1–2。

非标准 Rossi 无穷远的 $`\mathcal O(-1)`$ Einstein 填充分支尚未完成：其目标是对角方程 $`\mathop{\mathrm{Ric}}\nolimits=-6g`$、光滑 bolt 与非标准 CR 端。现有解析级数、区间输运和末端块将问题缩到初始包围与后续输运的衔接；[初始 Fuchs 程序](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/scripts/ach_bolt_fuchs.py) 的状态次序 $`(\sigma,\delta,\gamma,D\sigma,D\delta,D\gamma)`$ 与按 $`(\sigma,D\sigma,\delta,D\delta,\gamma,D\gamma)`$ 分配的余项半径没有一致置换。因此尚缺有效的分量余项界及其向输运初始盒的包含；同起始盒上的 Weyl 判别也依赖这一步。上述领口恒等式与截断结论不依赖这项填充存在性。已成立的完整 $`\mathbb R^4`$ almost-Kähler Einstein 构造见 [Goldberg 专题](GOLDBERG.md)，两者的拓扑与边界问题不同。

## 3. 全度量曲率估计与近极小序列的变分

### 3.1 全局共形 Kähler 类的能量下界

设 $`X`$ 为极小一般型曲面，$`A=c_1^2(X)>0`$，$`M=X\#k\overline{\mathbb{CP}}^{\,2}`$。对原取向上任意复结构的 Kähler 度量 $`h`$ 及 $`g=u^2h`$，全度量标量曲率平方积分下界和 $`I_+(h)=S(h)/24`$ 给

```math
P(g)-8\pi^2k
=\frac{S(g)-32\pi^2A}{12}
+\frac{S(h)-32\pi^2A}{6}\ge0.
\tag{3.1}
```

结合 (2.1)，$`P`$ 的极小化序列不可能始终位于全局共形 Kähler 类中。$`\tau(M)\ge0`$ 时，相反取向的共形 Kähler 度量也受相应比较限制。

共形 almost-Kähler 类中存在 $`P\lt 8\pi^2k`$ 的度量：精确复双曲领口中的旋转单元具有无零闭自对偶二形式，其 almost-Kähler 归一化伴随一个随异常周期趋零而发散的标量平方层。这并不增加原度量的 $`P`$。构造及两种泛函的换算见 [低能量插入单元的辛形式与共形归一化](GOLDBERG.md#严格低于标准插入能量的辛构造与共形归一化)。

对固定吹起复结构，还可以看出下界的严格性。写 Kähler 类为 $`\pi^*a-\sum e_iE_i`$，$`e_i>0`$，令 $`q=K_X\cdot a`$。Hodge 指标定理给 $`q^2\ge Aa^2`$，故

```math
\frac{(c_1\cdot[\omega])^2}{[\omega]^2}
=\frac{(q+\sum e_i)^2}{a^2-\sum e_i^2}>A.
```

于是 $`S>32\pi^2A`$，$`P=S/4-8\pi^2(A-k)>8\pi^2k`$；缩小全部吹起面积给其 Kähler 下确界恰为 $`8\pi^2k`$，但不取得。这里区分了原复结构中的极值与所有 Riemannian 度量中的极值。

来源：[共形 Kähler 分离与 Einstein 候选区域](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §§2–3。

### 3.2 Weyl 能量与标量曲率积分的联合约束

在负 Yamabe 代表上定义

```math
\kappa=\frac A2-\frac{3I_+}{8\pi^2},\quad
\upsilon=\frac{Y([g])^2}{32\pi^2}-A\ge0,\quad
p=\frac P{8\pi^2}.
```

这里 $`\kappa`$ 是 Weyl 缺额，与端点估计的参数缺陷不同。(1.2) 精确给出

```math
p=k-\frac43\kappa+\frac13\upsilon.
\tag{3.2}
```

经典混合曲率不等式将 $`0\le\kappa\le A/2`$ 的区域限制为

```math
p\ge k-\kappa+
\frac{A-\kappa-\sqrt{A^2-2A\kappa}}2.
\tag{3.3}
```

若 $`\kappa\lt 0`$，则 $`p\ge k-4\kappa/3`$。Einstein 候选在 $`0\lt k\lt A/3`$ 时必须满足

```math
\kappa\ge k+
\frac{k^2}{A(1+\sqrt{1-3k/A})^2}>k.
\tag{3.4}
```

因而 $`\kappa\le k`$ 若能对所有竞争度量成立，会产生严格正下界；但这项不等式尚未建立。它的具体后果是

```math
p_*\ge p_{\rm flat}:=\frac{A-k-\sqrt{A^2-2Ak}}2
\sim\frac{k^2}{4A},\qquad 0\lt k\lt A/2.
\tag{3.5}
```

再结合反自对偶 Weyl 能量估计，便有条件性估计

```math
\alpha\ge\min\left\{1,\frac{4p_{\rm flat}}{4p_{\rm flat}+A+k}\right\}
\sim(k/A)^2.
```

式 (3.5) 以全度量不等式 $`\kappa\le k`$ 为前提。$`p/k\to0`$ 并不强迫 $`\kappa/k\to1`$，因为 (3.2) 允许 $`\kappa`$ 与 $`\upsilon`$ 同时增长并抵消。实际需要确定的是全部可实现二元数据 $`(\kappa,\upsilon)`$；单独优化 Weyl 能量无法决定 $`P_*`$。例如设 $`\Theta_*(M)=\sup_{[g]}2\kappa/A`$，则 (1.8) 给 $`\alpha\lt 1\iff\Theta_*>(3k/A-1)/2`$，但 $`\Theta_*`$ 本身还不足以计算正间隙。

### 3.3 近极小、近驻点和近稳定的统一选择

在上述平衡手术族中设 $`h_j=Q_j/A_j\to0`$。选择 $`P`$ 近极小序列使

```math
0\le P(g_j)-P_*(M_j)\le\delta_j,
\qquad \delta_j=o(Q_j^3/A_j^2),
```

并作负 Yamabe 替换、归一化至 $`s=-4`$。在该族已有的全曲率积分上界 $`\int|\mathop{\mathrm{Rm}}\nolimits|^2\le KA_j`$ 下，考虑所有满足

```math
\|H\|_\infty\le1,\qquad
\int\bigl(|\nabla^2H|^2+|\nabla H|^4\bigr)\le A_j
\tag{3.6}
```

的光滑对称张量。对 $`F(t)=P(g_j+tH)`$，曲率变换公式和 Cauchy–Schwarz 给固定小区间内 $`|F''|+|F'''|\le C_KA_j`$。由下确界的定义 $`F(t)\ge F(0)-\delta_j`$，分别作二阶、三阶 Taylor 比较，得到

```math
|DP_{g_j}[H]|\le C_K\sqrt{A_j\delta_j}=o(Q_j),\qquad
D^2P_{g_j}[H,H]\ge-C_KA_j^{2/3}\delta_j^{1/3}=-o(Q_j).
\tag{3.7}
```

估计对 (3.6) 的全部测试同时成立；对不相交支撑测试，也可控制其一阶绝对值之和及二阶负部之和。它不要求统一 Sobolev 常数。常标量下，$`DS[H]=8\int\langle\mathop{\mathrm{Ric}}\nolimits^{\circ},H\rangle`$，所以

```math
4DI_+[H]+\frac23\int\langle\mathop{\mathrm{Ric}}\nolimits^{\circ},H\rangle=o(Q_j).
```

这些变分估计在所选极小化序列上达到 $`o(Q_j)`$ 精度。颈部收敛、气泡能量恒等式和光滑取得性需要进一步的几何控制。

来源：[全局近极小序列的变分选择](../archive/originals/2026-09-29/02_O11_Variational_Selection.md)。

另一种选择使用加权负梯度流。令 $`Q_g`$ 为 $`P`$ 的 $`L^2`$ 梯度，固定光滑正权 $`w`$，在流实际存在的区间上，$`\partial_tg=-wQ_g`$（模微分同胚）满足

```math
\frac{d}{dt}P(g_t)=-\int w|Q_{g_t}|^2.
```

因此某个时刻的加权残差不超过 $`2(P(g_0)-P_*)/T`$。这提供了带尺度权重的 Palais–Smale 选择。它不保证从任意初始能量界出发，流都能存在足够长时间；曲率集中半径与局部 Sobolev 控制也仍须分别建立。仅有自身尺度的 $`L^2`$ 梯度残差不能推出点态曲率有界。

### 3.4 单极子场的能量分解

设完整符号类族 $`a_\varepsilon=c+\sum\varepsilon_iE_i`$ 的各个结构在同一度量下均有单极子解。曲率、标量余量和旋量导数满足

```math
8\pi^2Q-P=\mathcal N-\mathcal B,\qquad\mathcal B\ge0,
\tag{3.8}
```

其中 $`\mathcal N`$ 是按符号类平均的加权非可积能量：在实际场给出的单位方向 $`n`$ 和幅度 $`\rho`$ 上，取 $`\nabla n`$ 的 $`W_2`$ 分量，积分 $`\rho^2|(\nabla n)_{W_2}|^2/2`$。各权重、零集处理及非负余项见[同场分解](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md)。

因此 $`P\lt 8\pi^2Q`$ 要求 $`\mathcal N>\mathcal B`$。若另有全局强制 $`P\ge c\mathcal N`$，才会得到 $`P\ge8\pi^2Qc/(1+c)`$；(3.8) 本身没有提供这个新不等式。

单个符号翻转的相对曲率 $`h=(f-f')/2`$ 满足

```math
\|h^-\|_2^2-\|h^+\|_2^2=4\pi^2.
```

异常类的固定配对因此可以主要由反自对偶曲率承担。相对线丛的第一 Chern 类是 $`(a-a')/2=\pm E_i`$；旋量内积为零也可能只表示正交，不能据此给每个异常类指定一个独立的正涡旋能量下界。全局下界需要控制这些单极子场之间的关系；局部模型的能量不能直接相加。

在实际 almost-Kähler 结构上，还可保留扭率的完整积分轮廓。设 $`|\omega|^2=2`$，$`\delta=|\nabla\omega|^2=s^*-s`$，$`\ell=8\pi K_\omega\cdot[\omega]>0`$，$`\theta=\int\delta/\ell`$，并令

```math
C_+=\frac{I_+}{2\pi^2}+\frac{S}{96\pi^2},\qquad
\varphi=\frac{\mathop{\mathrm{Vol}}\nolimits\{s^*\ge0\}}V\lt 1.
```

Blair 恒等式给 $`\int(-2s-\delta)=\ell`$，而
$`W^+(\omega/\sqrt2,\omega/\sqrt2)=s/6+\delta/4`$。无迹性及两区域 Jensen 不等式因此给

```math
C_+\ge\frac{\ell^2}{128\pi^2V}
\left[3\theta^2-2\theta+1+
\frac{\varphi}{1-\varphi}(1-\theta)_+^2\right]
\ge\frac{\ell^2}{128\pi^2V}\frac2{3-2\varphi}.
\tag{3.8a}
```

具体地，写 $`\sigma=-s`$，点态下界为
$`G(\sigma,\delta)=[2\sigma^2+(3\delta-2\sigma)^2]/(192\pi^2)`$。
整体均值为 $`\bar\sigma=(1+\theta)\ell/(2V)`$、$`\bar\delta=\theta\ell/V`$；将 $`\{\delta\ge\sigma\}`$ 与补集分别取均值，附加项由
$`\min_{y-x=D}[2x^2+(3y-2x)^2]=6D^2`$ 算出。这也解释了为何出现 $`\varphi/(1-\varphi)`$。

把 $`\ell`$ 改写成异常周期需要额外拓扑信息。若主体的全部基本类恰为 $`\pm K_X`$，Taubes 的符号翻转论证给
$`K_\omega\cdot[\omega]=|K_X\cdot[\omega]|+\sum_i|E_i\cdot[\omega]|`$，且每个异常周期严格为正。不过 $`b^+>1`$ 时，$`|K_X\cdot[\omega]|^2\ge A[\omega]^2`$ 并非一般成立；这一 Hodge 指标型条件必须另行提供。式 (3.8a) 保留 $`\ell`$ 时不需要它。与 §2.3 合并，沿 $`\omega`$ 方向的 Burns 首项节省发生于 $`s^*>0`$ 区域，而 (3.8a) 给出该区域对曲率积分下界的贡献。

来源：[almost-Kähler 扭率轮廓](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md) §§1–2；[正星标量区域的估计](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md) §3。

### 3.5 Yamabe 常数与 Weyl 谱的余项估计

仍假设完整符号类族的各个结构均有单极子解，取 $`s=-4`$ 的 Yamabe 代表。令

```math
\Delta V=V-2\pi^2A=\frac{Y([g])^2-32\pi^2A}{16},\qquad
D_W=\int(2/3-|W^+|^2).
```

Chern–Weil 给 $`8\pi^2k-P=4D_W-4\Delta V`$。将同场 Weyl 分解按实际幅度 $`0\le r\le2`$ 和单位方向 $`n`$ 优化，其点态密度为

```math
f(W,r,n)=-r^2W(n,n)-4|W|^2-r^3+\frac73r^2-\frac43.
```

写 $`x=-\lambda_{\min}(W)\ge0`$，对 $`n,r`$ 的最大值为 $`\varphi(x)-4|W|^2`$，其中

```math
\varphi(x)=
\begin{cases}
\frac12[(6x+14)/9]^3-\frac43,&0\le x\le2/3,\\
4x,&x\ge2/3.
\end{cases}
```

令 $`\mathcal K`$ 为谱 $`(-2/3,1/3,1/3)`$ 的 Kähler Weyl 轨道，$`\Psi(W)=4/3+2|W|^2-\varphi(x)`$。若谱写为 $`(-x,x/2-\sigma,x/2+\sigma)`$，则

```math
\Psi=\frac53(2/3-x)^2+\frac4{27}(2/3-x)^3+4\sigma^2\quad(x\le2/3),
```

```math
\Psi=3(x-2/3)^2+4\sigma^2\quad(x\ge2/3).
```

所以 $`\Psi\ge(10/9)\mathop{\mathrm{dist}}\nolimits(W,\mathcal K)^2`$。将这一点态界代回实际场等式，保留非正余项，再用 $`4D_W-4\Delta V`$ 消去 $`D_W`$，得

```math
\boxed{8\pi^2k-P(g)\le
4\Delta V-2\int\Psi(W^+_{\widehat g})
\le4\Delta V-\frac{20}{9}\int\mathop{\mathrm{dist}}\nolimits(W^+_{\widehat g},\mathcal K)^2.}
\tag{3.9}
```

因此 $`P(g)\le8\pi^2ck`$ 要求 $`Y([g])^2\ge32\pi^2(A+(1-c)k)`$，且还须满足谱偏离项所给出的更强限制。经典混合估计给出首项 $`8\pi^2k-P\le4\Delta V`$；本式进一步保留了重特征值分裂的非负余项。其限制仍由 (3.2) 表达：尚无全局估计将 $`D_W-\Delta V`$ 压到匹配构造的最佳值。

完整符号类族还给出一个关于周期的线性下界。令
$`\Pi_g=\max_\varepsilon(a_\varepsilon^+)^2-A`$。
对任意正平方的自对偶谐和类 $`c`$，投影到 $`\mathbb Rc`$ 并逐项选择符号，给

```math
\Pi_g\ge\frac{(|K\cdot c|+\sum_i|E_i\cdot c|)^2}{c^2}-A.
\tag{3.9a}
```

取 $`c=K^+`$、$`e_i=E_i\cdot K^+`$，则
$`\Pi_g\ge|K^-|^2+2\sum|e_i|+(\sum|e_i|)^2/(K^+)^2`$。
另按符号平均有 $`\Pi_g\ge|K^-|^2+\sum|E_i^+|^2`$；两者应取较大者，前者不在所有度量上支配后者。
经典混合估计在 $`s=-4`$ 代表上精确写为

```math
8\pi^2k-P\le4\Delta V-\frac49\int(\sqrt6|W^+|-2)^2-16\pi^2\Pi_g,
\qquad\Delta V\ge2\pi^2\Pi_g.
```

因此扣除周期强迫的体积超额，置
$`\Delta V_{\rm free}=\Delta V-2\pi^2\Pi_g\ge0`$，便有

```math
\boxed{P(g)\ge8\pi^2\left(k+2\sum_i|e_i|\right)
-4\Delta V_{\rm free}+\frac49\int(\sqrt6|W^+|-2)^2,
\quad\Delta V\ge4\pi^2\sum_i|e_i|.}
\tag{3.9b}
```

若实际自对偶类写成 $`c=K-\sum\sigma_iE_i`$，则直接用 (3.9a) 得

```math
\Pi_g\ge\frac{(A+\|\sigma\|_1)^2}{A-\|\sigma\|_2^2}-A
\ge2\|\sigma\|_1+\|\sigma\|_2^2.
```

这保留了旋转单元的周期信息，无须假设 $`\|e\|_1\ge\|\sigma\|_1`$。因而使 $`P`$ 低于标准插入能量所需的体积超额还须满足这些周期约束。

这里使用的经典标量及混合曲率估计见 [统一间隙专题](GAPS_AND_ENDPOINTS.md)；(3.9a)–(3.9b) 保留了对全部实际符号类取最大值所产生的周期项。

### 3.6 靠近复双曲主体时的局部化

在 $`\mathop{\mathrm{Ric}}\nolimits_{g_0}=-6g_0`$ 的紧复双曲商上，Bianchi 规范下的 Einstein 线性化为

```math
L=\tfrac12(\nabla^*\nabla-2\mathring R).
```

Koiso 恒等式在无迹横截张量上给 $`L\ge1`$；规范与迹部分由 Hodge Laplacian 和标量 Laplacian 的非负性给 $`L\ge6`$。这不使用覆盖的第一特征值下界。若 $`|d\phi|\le a\lt \sqrt2`$，加权分部积分进一步给

```math
\|e^\phi L^{-1}e^{-\phi}\|_{2\to2}\le(1-a^2/2)^{-1}.
```

设外部区域的常标量度量已处于该规范，且相对 $`g_0`$ 在一致局部 $`C^{2,\gamma}`$ 范数内充分接近。对离核心距离 $`T`$ 以外的区域，截断、加权逆估计和非线性余项吸收给

```math
\|g-g_0\|_{H^2(d\ge T)}
\le C\left(\|\mathop{\mathrm{Ric}}\nolimits^{\circ}_g\|_{L^2(d\ge1)}+e^{-aT}\Lambda\right),
\qquad \Lambda=\|g-g_0\|_{H^1(1\le d\le2)}.
\tag{3.10}
```

常数只依赖模型和接近程度。标量约束使主体体积的一阶变化成为界面通量，其余为 $`O(\|g-g_0\|_{H^2}^2)`$。将通量计入核心相对体积 $`\Delta V_U`$，(3.9) 因而给

```math
P(g)\ge\frac{8\pi^2k-4\Delta V_U-C\Lambda^2}{1+C}.
\tag{3.11}
```

这说明在明确的近复双曲范围内，固定比例的能量下降要求核心相对体积超额或界面误差具有相应下界。一般极小化序列是否具有这样的主体、规范和小邻域仍未建立；四维 $`H^2`$ 控制本身不能替代所需的 $`C^{2,\gamma}`$ 假设。

在同一小邻域内，可以同时控制实际规范场，而不限于度量。对任意紧复双曲商 $`(X_\Gamma,g_\Gamma)`$，取 $`\mathop{\mathrm{Ric}}\nolimits=-6g`$ 的典范 Seiberg–Witten 解 $`(A_0,\Phi_0)`$，满足 $`\nabla_{A_0}\Phi_0=0`$、$`|\Phi_0|^2=24`$。其规范固定线性化 $`\mathcal L`$ 的正规算子精确分裂为

```math
\mathcal L^*\mathcal L
=B_1\oplus(\Delta+12)\oplus(\Delta+6)\oplus\nabla^*\nabla_{K^{-1}},
\qquad B_1=dd^*+\tfrac12d^*d+6
=\tfrac12\nabla^*\nabla+3+\tfrac12dd^*.
\tag{3.12}
```

这一算子具有与商群无关的一致局部 Hölder 逆估计。关键是万有覆盖上的 Green 核及所需一阶导数可积。正质量标量块由 Kato 控制；$`K^{-1}`$ 块在径向规范下的方程为

```math
-f''-(3\coth r+\tanh r)f'+9\tanh^2r\,f=0.
```

零能量衰减解为 $`O(e^{-(2+\sqrt{13})r})`$，快于体积壳的 $`e^{4r}`$ 增长；原点处 Green 核和导数分别为 $`O(r^{-2})`$、$`O(r^{-3})`$，也可积。一形式块则有

```math
B_1^{-1}=2(\nabla^*\nabla+6)^{-1}
-\frac16d\bigl[(\Delta+6)^{-1}-(\Delta+12)^{-1}\bigr]d^*.
\tag{3.13}
```

两个标量核的主奇性相消，混合二阶导数仅为 $`O(r^{-2})`$，尾部仍可积。绝对收敛的周期化于是给所有紧商同一个 $`L^\infty`$ 界；万有覆盖单位球上的内点估计提升到一致局部 $`C^{2,\gamma}`$。这里没有使用商空间的单射半径下界。

因此存在模型常数 $`\varepsilon_0,C>0`$：若经一次整体缩放与微分同胚后，$`g`$ 与 $`g_\Gamma`$ 的一致局部 $`C^{2,\gamma}`$ 距离不超过 $`\varepsilon_0`$，则其负 Yamabe 代表 $`\widehat g`$ 有唯一邻近的典范解分支（模规范），场方向 $`n`$ 满足

```math
\int|\nabla n|^2\le C P(\widehat g)\le C P(g).
\tag{3.14}
```

证明先以 $`6(\Delta+8)`$ 求 Yamabe 修正，以 $`\nabla^*\nabla+6`$ 固定 DeTurck 规范，再用 Koiso 估计及二次余项吸收得到 $`\|g'-g_\Gamma\|_{H^2}^2\le CP(\widehat g)`$。式 (3.12) 的逆和双线性非线性项给典范解的收缩映射；其 $`H^1`$ 估计控制 $`\nabla n`$，得到 (3.14)。该结果只控制邻近的典范分支；吹起外部的符号类解是否属于这个分支，仍须单独证明。

### 3.7 正耦合曲率作用与耦合场

共同强制估计还有不依赖极小值取得性的直接应用。设 $`T_+=A(1-h)`$、$`h>0`$，并在每个所考虑共形类中，固定 Spin$`^c`$ 结构的单极子方程处处可解，满足 $`p\ge A>0`$、$`a^2\ge T_+`$。记

```math
D_2=\frac32S+18I_+-72\pi^2p\ge0,
\quad\Sigma=S-32\pi^2p\ge0,
\quad\Sigma\le C(P+D_2).
```

对任意 $`u,v>0`$，作用量
$`\mathscr I_{u,v}=uP+v(\frac32S+18I_+)`$ 满足

```math
\boxed{\mathscr I_{u,v}-72\pi^2vA
\ge\frac{36\pi^2\min(u,v)}{\frac92+\frac98C}\,Ah.}
\tag{3.15}
```

事实上 Chern–Weil 给
$`36\pi^2(p-T_+)=\frac92P+\frac98\Sigma-D_2`$，
故右侧不超过 $`(\frac92+\frac98C)(P+D_2)`$；而作用量超额至少为 $`\min(u,v)(P+D_2)`$。签名公式又将同一作用写成
$`uP+\frac32vS+9vW+108\pi^2v\tau`$。这使线性强制进入一族正耦合二次曲率作用，未声称其常数最优。

若某流形已有全度量 $`P\ge p_0>0`$，则曲率算子的混合块满足 $`4\int|B|^2=P\ge p_0`$。对实际满足
$`\mathop{\mathrm{Ric}}\nolimits-\frac12sg+\Lambda g=\varkappa T`$
的度量与场，取无迹部分给

```math
\int|T^\circ|^2\ge\frac{p_0}{\varkappa^2}.
\tag{3.16}
```

对四维 Euclidean Maxwell 张量
$`T_{ij}=F_{ik}F_j{}^k-\frac14g_{ij}F_{kl}F^{kl}`$，二形式范数下有
$`|T|^2=4|F^+|^2|F^-|^2`$，从而
$`\int|F^+|^2|F^-|^2\ge p_0/(4\varkappa^2)`$。
这是耦合方程解的自对偶与反自对偶场分量所须满足的重叠积分下界。

来源：[二次曲率作用与耦合场](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/paper/sections/quadratic_and_matter.tex)。

## 4. 光滑全局极小元与临界点

本节研究闭光滑流形上是否存在非 Bach-flat 的光滑全局 $`P`$ 极小元。两种明确候选为：Horikawa 单吹起和 Godeaux 单吹起，均具有

```math
16\pi^2/3\le P_*\lt 8\pi^2.
```

经典曲率下界已排除 Einstein 度量；若取得，则负 Yamabe 性、$`P`$-临界性和变分关系保证极小元非 Bach-flat。尚缺的是光滑取得性本身。

来源：[共形 Kähler 分离与 Horikawa 吹起](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §4 的 Horikawa 例；[Godeaux 吹起的极小化与退化](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) §1 的 Fermat 商 Godeaux 例。两种候选具有各自的光滑拓扑。

### 4.1 谐和通量与下降方向

[谐和通量分解与曲率变分](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §3 中，令 $`B:\Lambda^+\to\Lambda^-`$ 为混合曲率块，$`a`$ 为给定第一 Chern 类，$`h`$ 为单位 $`L^2`$ 范数的非零谐和反自对偶形式，$`q=(a_g^-,h)_{L^2}>0`$。定义

```math
p=P/(8\pi^2),\qquad\mathfrak F_h=\sqrt2\int|B^*h|,
\qquad\delta=1-\mathfrak F_h/(2\pi q),
\qquad L=(P/2-\mathfrak F_h^2)/(4\pi^2).
```

则

```math
p=q^2(1-\delta)^2+L,\qquad L\ge0,
```

其中 $`L`$ 分为混合曲率块的秩偏离与幅度方差两项。数值 $`p=0,\delta=1,L=0`$ 也满足该等式。

对真实度量变分有如下公式。在闭 almost-Kähler 结构 $`(g,J,\Omega)`$、Ricci 为 $`J`$-不变的类别，

```math
DP_g[\mathop{\mathrm{Ric}}\nolimits^{\circ}]
=\frac18\int|ds|^2-\frac12\int s|\mathop{\mathrm{Ric}}\nolimits^{\circ}|^2.
```

常非零标量时，每个非 Einstein 度量均有保体积形式的下降方向。负标量下进一步的精确谐和秩对齐条件
$`\mathop{\mathrm{im}}\nolimitsB_x\subset\mathbb Rh_x`$
给出局部化下降，无须对零集上的商另加有界假设。因此负标量 Einstein–Maxwell 非 Einstein 度量也不可能成为 $`P`$-临界点。

来源：[曲率通量等号与下降方向](../archive/originals/2026-10-08/Q3_Descent_and_Flux_Equality.tex) §§2–3；[谐和方向约束下的下降变分](../archive/originals/2026-10-08/Q3_Harmonic_Alignment_Descent.tex) §§2–5；[谐和秩条件与刚性](../archive/originals/2026-10-08/Q3_Harmonic_Rank_Rigidity.tex) §§1、4。完整点态方程允许两个幅度同时变化。

因此非 Einstein、负标量的光滑极小元若存在，对每个非零谐和反自对偶形式均有严格正的对齐余项；这一正数允许依赖度量。

上述通量分解还区分了常标量 Kähler 几何的驻定性与稳定性。令 $`a=c_1(J_0)`$，随度量取 $`h=a_g^-/|a_g^-|`$，并写

```math
\mathscr D_a(g)=\frac{P(g)}{8\pi^2}-|a_g^-|^2
=L-2q_g^2\delta+q_g^2\delta^2.
\tag{4.1a}
```

每个常标量 Kähler 度量均满足 $`D\mathscr D_a=0`$；非 Einstein 情形还满足 $`D\delta=DL=0`$。证明是对任意双向变分 $`g_t`$ 正交化原复结构，使内蕴扭率为 $`O(t)`$，从而通量的扭率误差给 $`\delta(g_t)\le Ct^2`$。双向可微性迫使 $`D\delta=0`$；$`L\ge0`$ 且 $`L(g_0)=0`$ 给 $`DL=0`$。Kähler–Einstein 情形的 $`P`$ 和 $`|a^-|^2`$ 均在零处取极小值，仍给 $`D\mathscr D_a=0`$。这里驻定的泛函是 $`\mathscr D_a`$；非 Einstein 的常标量 Kähler 度量通常不使 $`P`$ 驻定。

局部强制需要保留变化中的谐和方向及其周期。设 $`a_{g_0}^-`$ 无零点，在 Bianchi 规范和线性常标量空间
$`\mathcal S=\{k:\beta_{g_0}k=0,\ s'_0(k)\text{ 为常数}\}`$ 上，令 $`d_2,\ell_2`$ 为 $`\delta(g_0+tk),L(g_0+tk)`$ 的二次系数。则

```math
(\mathscr D_a)_2=\ell_2-2q_0^2d_2,
\qquad c_K=\inf_{d_2(k)>0}\frac{\ell_2(k)}{q_0^2d_2(k)}.
\tag{4.1b}
```

若 $`k\in\ker\ell_2`$，对齐方程必须微分为
$`B'_0=\dot\Phi\otimes h_0+\Phi_0\otimes\dot h`$，而非固定 $`h_0`$。线性化 Bianchi 恒等式和幅度条件使相应 $`\Omega_t`$ 满足 $`d\Omega_t=O(t^2)`$、$`(\mathop{\mathrm{Ric}}\nolimits'')'_0=0`$。能否将它与一阶 Kähler 变分比较，还取决于周期障碍

```math
\Xi(k)=[\dot\Omega_k]^{0,2}\pmod{\mathop{\mathrm{im}}\nolimits\mathcal P_\omega},
\qquad
\mathcal P_\omega:H^{0,1}(T^{1,0}M)\longrightarrow H^{0,2}(M),
\quad[\mu]\longmapsto[\mu\mathbin{\lrcorner}\omega].
\tag{4.1c}
```

增广对齐、标量和 Bianchi 系统的主符号是单射：其核满足
$`k^\circ=\sigma\circ h_0`$、$`\sigma\perp\omega`$、$`\mathop{\mathrm{tr}}\nolimitsk=0`$、$`(\sigma\circ h_0)\xi=0`$，而相反手性的二形式给
$`(\sigma\circ h_0)^2=|\sigma|^2|h_0|^2I/4`$。因此 $`K=\ker\ell_2\cap\mathcal S`$ 有限维，且
$`\ell_2(k)\ge c\|k-\pi_Kk\|_{H^2}^2`$。若另有 $`\Xi|_K=0`$，先扣除同周期的一阶 Kähler 变分，再用 Moser 修正消去恰当部分；固定辛形式下的 Blair–Ianus 恒等式
$`\mathop{\mathrm{Hess}}\nolimits\int|\nabla\omega|^2=2\|(\nabla\omega)'\|_2^2`$
遂将 $`K`$ 放入 $`d_2`$ 的根空间。由 $`d_2\le C\ell_2`$ 得 $`c_K>0`$，并对 $`0\lt c\lt c_K`$ 有

```math
L(g_0+k)\ge c q_0^2\delta(g_0+k)-C\|k\|_{C^{2,\gamma}}^3,
\qquad k\in\mathcal S.
\tag{4.1d}
```

这是带周期前提的局部结论。一般的 $`\Xi|_K=0`$ 尚未证明，$`\mathcal S`$ 也只是线性切片；不能据此断言所有常标量 Kähler 度量都是局部极小元。

曲面乘积给出一个显式鞍点机制。取 $`M=\Sigma_1(K_1)\times\Sigma_2(K_2)`$，$`K_1\lt K_2\lt 0`$，令 $`Q`$ 为第一因子的非零全纯二次微分的实部，$`\Delta_2f=\mu f`$、$`\mu>0`$。实际度量族

```math
g_t=g_1(e^{tf g_1^{-1}Q}\,\cdot,\cdot)\oplus g_2
```

保持两个面积形式，故 $`q_t^2=|c_1^-|_{g_t}^2`$ 不变；其切向量 $`k=fQ`$ 横截无迹且 $`s'_0=0`$。直接计算两个 Ricci 块，若 $`G_t`$ 为第一块、$`K_t`$ 为其纤维 Gaussian 曲率，则

```math
\mathop{\mathrm{Ric}}\nolimits_V=K_tG_t+\frac{t\mu f}{2}G_tg_1^{-1}Q,
\qquad
\mathop{\mathrm{Ric}}\nolimits_H=K_2g_2-\frac{t^2}{4}|Q|^2df\otimes df,
```

混合块没有一阶项。Gauss–Bonnet 与面积不变消去 $`K_t-K_1`$ 的积分二次贡献，$`\int|df|^2=\mu\int f^2`$ 因而给

```math
\boxed{8\pi^2(\mathscr D_a)_2=
\frac\mu4(\mu+K_1-K_2)\|fQ\|_2^2.}
\tag{4.1e}
```

$`0\lt \mu\lt K_2-K_1`$ 时存在严格下降。由于 $`s_0\lt 0`$，$`6\Delta-2s_0`$ 可逆，可作 $`O(t^2)`$ 共形修正使标量精确为常数；(4.1a) 的驻定性保持二次系数，二形式的 Hodge 分解也不变。分开的通量系数为

```math
\ell_2=\frac{\mu^2}{32\pi^2}\|k\|_2^2,
\qquad q_0^2d_2=\frac{(K_2-K_1)\mu}{64\pi^2}\|k\|_2^2,
\qquad c_K\le\frac{2\lambda_1(\Sigma_2)}{K_2-K_1}.
\tag{4.1f}
```

夹缩分离闭测地线可令 $`\lambda_1(\Sigma_2)\to0`$，所以即使拓扑和两个曲率尺度固定，也没有跨背景的统一正 $`c_K`$。这些模式满足 $`\ell_2>0`$，未决定核上的周期障碍；而低于 $`|c_1^-|^2`$ 也不等于低于归一化吹起能量 $`k`$，后者另有 $`|c_1^-|^2=k+\Pi`$ 的投影超额。

完整推导见 [常标量驻定、周期障碍与乘积 Hessian](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §3。

### 4.2 低于标准插入能量的子水平集与退化

[Godeaux 吹起的极小化与退化](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) §§2–5 构造一个显式节点 Godeaux 退化，配合固定严格插入得到 $`P\lt 8\pi^2`$ 的退化序列，其缩放核心为 Ricci-flat Eguchi–Hanson。因此次 $`8\pi^2`$ 子水平集可非紧。该构造未确定退化序列是否极小，光滑取得性仍为独立问题。

同稿的带标记整体分裂估计保留规范类在主体和各渐近局部欧氏（ALE）核心的分量；相对特征数项相加抵消后，某些核心被排除，但规范类在嵌入 $`(-2)`$-球上的限制可为零；Ricci-flat 核心具有非平凡二循环而 $`P=0`$。

### 4.3 非球面背景中的 ALE 核心与替换

[标量曲率与全局极小值取得性](../archive/originals/2026-10-12/Scalar_Curvature_and_Global_Attainment_20261012.tex) §§2–3：闭 aspherical 四维环境中，若嵌入紧域的边界连通且边界基本群有限，且该域有 $`s\ge0`$、严格向外平均凸度量，则包含映射零伦。由此对所列单端光滑 ALE 核心得 $`\chi=1,\tau=0`$ 及边界群限制；非平凡端群时

```math
P\ge4\pi^2+S/12,
```

满足这些嵌入条件的 Ricci-flat ALE 核心只能平坦。Aspherical 指环境流形的万有覆盖可缩。

[渐近欧氏气泡的替换](../archive/originals/2026-10-15/AE_Bubble_Replacement_20261015.tex) §§2–3 处理平凡端群：对满足原稿微分衰减条件、$`s\ge0,\chi=1,P\lt 16\pi^2`$ 的完备单端渐近欧氏（AE）流形，利用经典 Chang–Gursky–Yang 球定理证明紧核心为标准光滑球；若它作为完整核心以 $`C^2`$ 缩放收敛出现在 $`P`$ 极小化序列中，正能量可由平坦填充和小能量过渡严格降低，因此不可能保留这样的气泡。

替换定理以完整核心的光滑缩放收敛为输入。一般极小化序列的轨形、中间尺度、多端及塌缩分支仍待分析；边界为 $`S^3/Q_8`$ 的正能量核心属于非平凡端群分支。

[标量曲率与全局取得性](../archive/originals/2026-10-12/Scalar_Curvature_and_Global_Attainment_20261012.tex) §4 的双曲尖点加倍例说明另一个独立现象：可有闭 aspherical 流形上 $`P_* =0`$ 而不取得，曲率一致有界、退化来自塌缩环面颈。取得性因而同时涉及曲率集中和塌缩退化。

对紧复双曲主体还可在明确的气泡分解范围内限制异常拓扑的去向。设 $`b^+(X)\ge3`$，$`M_k=X\#k\overline{\mathbb{CP}}^{\,2}`$，且一个 $`P`$ 极小化序列具有有限主体—气泡图分解：所有锥群平凡，缩放气泡标量平坦、完整 AE，并有使边界 Chern–Weil 项收敛的导数衰减；各分离尺度的能量满足下半连续性。则每个加帽气泡 $`\widehat N_i`$ 的 $`b^+`$ 为零，并且

```math
\sum_i\bigl[4(e_i-1)+4b_1(\widehat N_i)+b_2(\widehat N_i)\bigr]\lt k,
\tag{4.3}
```

其中 $`e_i`$ 为气泡端数。

证明先确定承载基本群的主体。$`\Gamma=\pi_1X`$ 是单端、自由不可分解的四维 Poincaré 对偶群；连通和图因而只有一个顶点 $`Y`$ 承载 $`\Gamma`$，其余顶点单连通且图没有环。吹降的分类映射经 $`Y`$ 分解并有度一，故 $`b^+(Y)\ge b^+(X)`$。$`Y`$ 不可能是气泡帽：标量平坦 AE 的各端共形紧化给正标量曲率，而有度一映射到闭负截面曲率流形的必要流形不能承载正标量曲率。于是每个气泡补集都含有 $`b^+\ge3`$ 的 $`Y`$；Seiberg–Witten 连通和消失与实际非零不变量迫使每个气泡帽 $`b^+=0`$。

对这类 AE 气泡，边界曲率恒等式给
$`P(N_i)\ge8\pi^2[4(e_i-1)+4b_1+b_2]`$。
再用插入构造给出的 $`P_*(M_k)\lt 8\pi^2k`$ 和下半连续性即得 (4.3)。因此异常拓扑不能全部逃入光滑 AE 气泡。特别 $`k=1`$ 时每个气泡单端且帽为同伦四维球面，主体连通，并有 $`M_1\cong V\#\Sigma`$，$`\Sigma`$ 为同伦球面，故 $`V`$ 与 $`M_1`$ 同胚。

若再有能量恒等式、平凡锥点的光滑可去性及极限的局部极小性，则主体达到 $`P_*(V)`$。其标量是负常数：正标量由上述必要性排除；零标量连同无正标量度量会迫使 Ricci-flat，从而基本群虚交换，与 $`\Gamma`$ 矛盾。常非零标量的 Bach-flat $`P`$-临界点必为 Einstein，所以主体极小元或者 Einstein，或者给出非 Bach-flat 全局极小元。在本节更强的完整核心替换条件下，还可删除正能量的平凡端群气泡。一般极小化序列是否进入这些分解与可去性假设，仍是这项条件性取得结论的前提。

### 4.4 实双曲吹起：一个取决于 Yamabe 值的精确问题

设 $`Y`$ 为闭实双曲四维流形，$`M_k=Y\#k\overline{\mathbb{CP}}^{\,2}`$，$`Y_{\rm hyp}\lt 0`$ 为双曲共形类的 Yamabe 常数。其全度量恒等式为

```math
P(g)=8\pi^2k+4I_+(g)+\frac{S(g)-Y_{\rm hyp}^2}{12},
\qquad Y_{\rm hyp}^2=192\pi^2\chi(Y).
\tag{4.1}
```

若另有 Yamabe 不变量等式 $`\mathcal Y(M_k)=Y_{\rm hyp}`$，则 $`S\ge Y_{\rm hyp}^2`$，故 $`P\ge8\pi^2k`$；Burns 恢复给相反不等式。若达到这个下界，同时达到负 Yamabe 不变量的度量必为 Einstein，与 $`P>0`$ 矛盾。因此

```math
P_*(M_k)=8\pi^2k\quad\text{且不取得}.
```

同一恒等式和 §1.2 的圆柱上界给

```math
\alpha(M_k)=\min\left\{1,\frac{4k}{k+6\chi(Y)}\right\}.
\tag{4.2}
```

$`k\lt 2\chi(Y)`$ 时不取得；$`k>2\chi(Y)`$ 时 $`\alpha=1`$ 及不取得不需要上述 Yamabe 假设。临界 $`k=2\chi(Y)`$ 的取得要求常非零标量的相应半共形平坦度量。

式 (4.1) 是无条件恒等式，(4.2) 的非平凡小 $`k`$ 分支则依赖尚未证明的 Yamabe 值。对任意极小化序列只能由等式推得其趋于半共形平坦及 Yamabe 极值；把每份 $`8\pi^2`$ 分配给单个异常类仅在指定的 Burns 恢复序列中成立。

来源：[实双曲吹起与 Yamabe 问题](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md) §3。

## 5. 成对 $`A_1`$ 奇点轨形的精确极值

固定奇点类型后的变分问题有时可以完整求解，并由此排除一类光滑极小化极限。设 $`X`$ 为紧复双曲曲面，取复取向，

```math
A=c_1^2(X),\qquad\chi(X)=A/3,\qquad\tau(X)=A/9.
```

令 $`O=S^4/\mathbb Z_2`$，其中对合在 $`S^4\subset\mathbb R\times\mathbb C^2`$ 上为 $`(t,w)\mapsto(t,-w)`$；它有两个 $`A_1`$ 点。在正规点作连通和，置

```math
V_m=X\#mO,\qquad k=2m>0.
```

以下下确界取遍这一固定轨形上的全部光滑轨形度量。其精确值为

```math
\boxed{P_{*,\mathrm{orb}}(V_m)=8\pi^2k,\qquad
\alpha_{\mathrm{orb}}(V_m)=\min\left\{1,\frac{4k}{A+k}\right\}.}
\tag{5.1}
```

而每个单独度量都满足 $`P(g)>8\pi^2k`$，所以 $`V_m`$ 不承载 Einstein 轨形度量。

### 5.1 光滑解消与下界转移

两个奇点由复取向的 Eguchi–Hanson 空间解消后，$`O`$ 的光滑解消微分同胚于 $`\overline{\mathbb{CP}}^{\,2}\#\overline{\mathbb{CP}}^{\,2}`$。证明需要光滑拓扑：原有 $`T^2`$ 作用延拓过两个 $`\mathcal O(-2)`$ 核心；解消单连通，交形式为 $`-I_2`$，轨道空间是四边形圆盘。Orlik–Raymond 的光滑环面作用分类给出上述微分同胚。单独知道交形式不足以替代这一步。所用光滑分类见 Orlik–Raymond，[Actions of the torus on 4-manifolds I](https://www.ams.org/tran/1970-152-02/S0002-9947-1970-0268911-3/)，§§4–5。

因此 $`V_m`$ 解消为 $`M_k=X\#k\overline{\mathbb{CP}}^{\,2}`$。对任意轨形度量，用缩小的 Eguchi–Hanson 核心解消，在其平坦端与轨形正规坐标间选取能量趋零的过渡环带，得到

```math
S(g_\epsilon)\to S(g),\qquad P(g_\epsilon)\to P(g),\qquad
\int(s^-_{g_\epsilon})^2\to\int(s^-_g)^2.
```

经典一般型吹起曲面的 Yamabe 估计于是转移为 $`\int(s^-)^2\ge32\pi^2A`$。这里包含 $`b^+=1`$ 的情形；使用的是每个光滑度量上的曲率估计，不需要先构造轨形上的极限单极子。经典输入见 LeBrun，[Kodaira dimension and the Yamabe problem](https://doi.org/10.4310/cag.1999.v7.n1.a5)；混合曲率估计及极化类选择见 [Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory](https://doi.org/10.1007/s002220100148)。

该轨形的特征数为

```math
\chi_{\mathrm{orb}}=A/3-m,\qquad\tau_{\mathrm{orb}}=A/9.
```

$`A_1`$ 链接的签名 eta 项为零。令 $`\sigma=S-32\pi^2A\ge0`$、$`w=W-4\pi^2A/3=2I_-\ge0`$，轨形 Chern–Weil 公式给出

```math
P=8\pi^2k+\sigma/12+2w,
\qquad R=8\pi^2(A+k)+\sigma/3+2w.
\tag{5.2}
```

故 $`\mathcal J`$ 是 $`4k/(A+k)`$、$`1`$、$`4`$ 的加权平均，其权重依次为 $`8\pi^2(A+k)`$、$`\sigma/3`$、$`2w`$。这证明 (5.1) 的两个下界。

### 5.2 显式恢复序列

在 $`\mathbb R^4\setminus\{0\}`$ 上取

```math
h=(1+r^{-2})^2\delta.
```

它标量平坦、共形平坦，且直接积分得

```math
P(h)=32\pi^2,\qquad
\int_{r>L}|\mathop{\mathrm{Ric}}\nolimits^{\circ}_h|^2
=\frac{\pi^2(96L^2+32)}{(1+L^2)^3}.
```

等距对合

```math
\iota(x)=\mathop{\mathrm{diag}}\nolimits(-1,-1,-1,1)x/|x|^2
```

交换两端，在 $`\pm e_4`$ 的微分均为 $`-I`$。商空间有两个 $`A_1`$ 点和一个普通 AE 端，$`P`$ 能量恰为 $`16\pi^2`$。

在 $`X`$ 的 $`m`$ 个不同点插入尺度为 $`\epsilon`$ 的商空间，拼接半径取 $`\rho=\sqrt\epsilon`$。背景与欧氏度量的差为 $`O(\rho^2)`$，缩放端与欧氏度量的差为 $`O(\epsilon^2\rho^{-2})`$；连同两阶导数可知过渡曲率有界，过渡体积为 $`O(\epsilon^2)`$。被截去的端能量也为 $`O((\epsilon/\rho)^4)=O(\epsilon^2)`$。所以

```math
P\to8\pi^2k,\qquad S\to32\pi^2A,\qquad
W\to4\pi^2A/3,\qquad L_s\to0,
```

从而 $`\mathcal E\to4k/(A+k)`$。与 §1.2 的长圆柱序列合并即得全部上界。

### 5.3 不取得性与光滑极小化序列的排除

若某度量达到 $`P=8\pi^2k`$，则 (5.2) 强迫 $`\sigma=w=0`$，并达到全度量的 $`S`$ 下界。对 $`S`$ 作共形变分得到 $`\Delta s=0`$；负标量曲率积分下界使 $`s`$ 为非零常数。再作无迹变分，

```math
DS[H]=-2s\int\langle\mathop{\mathrm{Ric}}\nolimits^{\circ},H\rangle=0
```

强迫 $`\mathop{\mathrm{Ric}}\nolimits^{\circ}=0`$，与 $`P=8\pi^2k>0`$ 矛盾。

令 $`q=4k/(A+k)`$、$`B=8\pi^2(A+k)`$，有

```math
\mathcal E-q=\frac{(1-q)\sigma/3+2(4-q)w+L_s}{R},
\qquad
\mathcal E-1=\frac{(q-1)B+6w+L_s}{R}.
```

故 $`k\lt A/3`$ 和 $`k>A/3`$ 时 $`\alpha_{\mathrm{orb}}`$ 均不取得。在边界 $`k=A/3`$，取得等价于 $`W^-=0`$ 且标量为负常数；还必须有 $`\sigma>0`$。这一边界上的存在性没有由上述公式决定。

另一方面，光滑解消满足 (2.1) 的 $`P_*(M_k)\lt 8\pi^2k`$。若其极小化序列在正规部 $`C^2_{\rm loc}`$ 收敛到 $`V_m`$ 上的光滑轨形度量，则非负性与下半连续性已给

```math
\liminf_iP(g_i)\ge P(V_m)>8\pi^2k>P_*(M_k),
```

矛盾。这里不需要额外假设气泡能量恒等式。固定轨形的精确下界排除了这一极限形态，却不成为其全部光滑解消度量的下界；有限尺度构造恰能降低这一奇异极限的能量。

## 6. ALE 解消中的混合曲率转移

### 6.1 解消时相对缺陷的连续性

设紧轨形主体 $`g`$ 满足 $`R(g)>0`$，解消采用 Ricci-flat ALE 空间，端误差及其前两阶导数为 $`O(r^{-\tau})`$，$`\tau>0`$。插入尺度 $`\epsilon`$，拼接半径取 $`\rho=\epsilon^{\tau/(\tau+2)}`$。环带上的尺度化度量误差为 $`O(\rho^2+(\epsilon/\rho)^\tau)=O(\rho^2)`$，故 Ricci 曲率有界、环带体积为 $`O(\rho^4)`$；核心 Ricci 为零。因此

```math
(V,T_s,S,P,R,L_s)(g_\epsilon)\longrightarrow(V,T_s,S,P,R,L_s)(g),
\qquad\mathcal E(g_\epsilon)\to\mathcal E(g).
\tag{6.1}
```

于是非零 Einstein 轨形的这种解消满足 $`P_*=\alpha=0`$，不必另外假设标量方差消失。若主体 Ricci-flat，则只能直接推出 $`P_*=0`$；上述简单截断族反而 $`\mathcal E\to4`$，因为标量仅支撑在体积趋零的过渡区，$`T_s^2\le4\mathop{\mathrm{Vol}}\nolimits(\mathop{\mathrm{supp}}\nolimitss)R`$。

若填充仅标量平坦，令 $`Q=\sum_jP(N_j)`$，同一计算给

```math
\mathcal E(g_\epsilon)\longrightarrow
\frac{4P(g)+L_s(g)+4Q}{R(g)+Q},\qquad R(g)+Q>0.
\tag{6.2}
```

正能量核心将相对缺陷推向 $`4`$，而有限尺度 Burns 节省来自这个极限式未保留的相互作用。式 (6.1)–(6.2) 针对实际拼接族，并非任意退化序列的能量恒等式。另须注意，$`P`$ 在度数 $`d`$ 的有限覆盖下乘以 $`d`$，$`\mathcal E`$ 则保持不变。

### 6.2 同时保留标量与手性 Weyl 能量

设紧轨形 $`V`$ 的孤立奇点由有足够二阶渐近衰减的标量平坦 ALE 空间 $`N_j`$ 解消为 $`M=X\#k\overline{\mathbb{CP}}^{\,2}`$，$`A=c_1^2(X)>0`$。取与 $`M`$ 一致的取向，令 $`\Gamma_j`$ 为端群，$`\eta_{\Gamma_j}`$ 使用定向签名公式的约定。定义

```math
a_\pm(N)=\frac2{|\Gamma|}-2\chi(N)\mp3\tau(N)\mp3\eta_\Gamma.
```

非紧 Chern–Weil 公式为

```math
P(N)=4I_\pm(N)+S(N)/12+8\pi^2a_\pm(N).
\tag{6.3}
```

若 $`N`$ Ricci-flat，则 $`a_\pm\le0`$；若还为复取向 Kähler，则

```math
a_+=0,\qquad a_-=-4\left(\chi(N)-|\Gamma|^{-1}\right).
\tag{6.4}
```

对光滑解消度量使用经典混合估计，再令解消尺度趋零，得到

```math
\boxed{\int_V(s-\sqrt6|W^+|)^2
+6\sum_jI_+(N_j)\ge72\pi^2A.}
\tag{6.5}
```

证明只需展开被积式：核心上 $`s=0`$，所以核心的贡献恰为 $`6I_+`$；过渡环带的总曲率平方积分趋零；主体上的积分收敛。每个光滑度量可选择对应的单极子类，整个转移不要求这些类收敛到某个预先指定的轨形类。对 Ricci-flat 解消，记 $`A_\pm=\sum_ja_\pm(N_j)`$，式 (6.5) 化为

```math
\int_V(s-\sqrt6|W^+|)^2\ge72\pi^2A+12\pi^2A_+.
```

因此复取向 Ricci-flat Kähler 解消无损转移该不等式；反取向解消则有明确的手性修正项。标量平坦但非 Ricci-flat 的核心还贡献其正 $`P`$ 能量。

### 6.3 Einstein 主体的有限参数可行区

假设主体度量 Einstein。标量估计迫使其标量为负。设 $`x=S(V)/(96\pi^2)`$。特征数加法给

```math
T_+^{\rm orb}=A-k+A_+,
\qquad T_-^{\rm orb}=4c_2(X)-A+5k+A_-.
```

由标量曲率积分下界、$`I_\pm\ge0`$ 和 (6.5)，

```math
\frac A3\le x\le\min(T_+^{\rm orb},T_-^{\rm orb}),\qquad
\left(\sqrt{8x}+\sqrt{T_+^{\rm orb}-x}\right)^2\ge6A+A_+.
\tag{6.6}
```

左侧是关于 $`x`$ 的凹函数，最大值在 $`x=8T_+^{\rm orb}/9`$；在允许区间上取这个点或最近端点，即可精确决定这些数值条件是否相容。还有不含渐近余项的必要条件

```math
\boxed{9A_-+2A_++42k+12(3c_2(X)-A)\ge0.}
\tag{6.7}
```

其证明是恒等式

```math
9x+3T-\left(\sqrt{8x}+\sqrt{T-x}\right)^2
=2\left(\sqrt{T-x}-\sqrt{2x}\right)^2\ge0,
```

再使用 $`x\le T_-^{\rm orb}`$。它比只保留标量曲率积分下界更强，且保留主体偏离复双曲的 $`3c_2-A`$ 项。

对复双曲背景及全部复取向 Ricci-flat Kähler 核心，$`A_+=0`$。式 (6.6) 强迫 $`k\le A/3`$，并给

```math
x_{\min}=\frac A{27}\left(4-\sqrt{1-3k/A}\right)^2,
\qquad
\sum_j\left(\chi(N_j)-\frac1{|\Gamma_j|}\right)
\le\frac{A/3+5k-x_{\min}}4.
\tag{6.8}
```

若这些核心全部为 Kronheimer 空间、承载总秩 $`k-k_b`$，令 $`y=\sqrt{1-3k/A}`$，则

```math
\sum_j\left(1-\frac1{|\Gamma_j|}\right)
\le k_b+\beta(k,A),\qquad
\beta(k,A)=\frac{k(5y+1)}{18(1+y)}\lt \frac k6.
\tag{6.9}
```

$`k_b`$ 仅表示没有被这些核心吸收的秩，不能据此把每个剩余异常类分配到某个几何区域。有限 $`A`$ 的严格修正为 $`\beta/k=1/6-k/(12A)+O((k/A)^2)`$；只保留 $`k/6`$ 会漏掉临界配置的排除。

### 6.4 对角交形式中的完整根系

当 $`X`$ aspherical 时，吹下映射 $`M\to X`$ 将每个嵌入球面送到零同伦类，因而其同调类落在异常对角格 $`-\mathbb Z^k`$。一个 $`(-2)`$-球必为 $`\pm E_i\pm E_j`$，即 $`D_k`$ 根。因此，嵌入的 ADE 配置需要作为根系嵌入 $`D_k`$；仅匹配行列式远远不够。

这一限制可直接分类。将根的两个非零坐标连成带符号边；对每个连通坐标分量作坐标变号，使一棵生成树全为差根。其反射生成坐标置换。若没有和根，所生成根系为 $`A_{v-1}`$；若存在和根，则为 $`D_v`$。因此 $`E_6,E_7,E_8`$ 不能作为这种根系嵌入任意对角格。若全部异常秩由根配置吸收，只有

```math
D_{a_1}\oplus\cdots\oplus D_{a_q},\qquad a_i\ge2,\quad\sum a_i=k,
```

其中 $`D_2=A_1\oplus A_1`$、$`D_3=A_3`$。该子格在对应对角格中的指数为 $`2^q`$，通常不是本原子格。

将 (6.9) 用于这些实际 Kronheimer 核心，其端群修正项为

```math
c(D_2)=1,\qquad c(D_3)=3/4,\qquad
c(D_a)=1-\frac1{4(a-2)}\quad(a\ge4).
```

这些修正项之和必须不超过 $`\beta(k,A)`$。秩至多五的每个分量的修正项均大于其秩的六分之一，故完整吸收需要至少一个 $`D_a`$ 分量满足 $`a\ge6`$，特别有 $`k\ge6`$。$`k=6`$ 时唯一通过根型限制的候选是 $`D_6`$；其修正项为 $`15/16`$，精确解 (6.9) 得

```math
A\ge\frac{3675}{64}.
```

复双曲曲面的 $`A\in9\mathbb Z`$，第一个数值允许值因而是 $`A=63`$。这些是拓扑与能量的必要条件；仍须有实际嵌入、正确边界识别以及负 Einstein 主体。通过数值条件没有构造这些对象。

### 6.5 Eguchi–Hanson 障碍与逼近速率

ALE 解消的首项还可精确到一个局部二次能量项。设 Einstein 轨形 $`(V,g_V)`$ 在 $`p`$ 有 $`\mathbb R^4/\mathbb Z_2`$ 奇点，$`\mathop{\mathrm{Ric}}\nolimits=\Lambda g`$，$`\mathbf R^+=W^++\frac{s}{12}I`$。用尺度 $`a`$、方向 $`\zeta\in\Lambda_p^+`$、$`|\zeta|=1`$ 的 Eguchi–Hanson 空间解消。其三个 $`L^2`$ 余核张量为 $`o_i=\Omega\circ\omega_i`$，其中 $`\omega_i`$ 为平行超 Kähler 形式，$`\Omega`$ 为相反手性的调和二形式。外部可写 $`\Omega=-\frac14d(\sigma_3/r^2)`$，但其 bolt 周期非零，故这不是全局恰当形式。范数为

```math
\langle o_i,o_j\rangle=\frac{4\delta_{ij}}{r^8},
\qquad
\|o_i\|_2^2=\pi^2\int_a^\infty\frac4{r^5}\,dr
=\frac{\pi^2}{a^4}.
\tag{6.10}
```

将轨形的二次度量 jet $`h_2`$ 延拓到单位 Eguchi–Hanson 空间，线性化 Ricci 与余核的配对是无穷远通量，精确为

```math
\int\langle D\mathop{\mathrm{Ric}}\nolimits_{\rm EH}[\widehat h_2],o_i\rangle
=\pi^2(\mathbf R_p^+\zeta)_i.
\tag{6.11}
```

角向配对与余核范数的精确核算见 [Eguchi–Hanson 配对程序](../research/computations/eguchi_hanson_pairing.py)。重标 $`y=x/a`$ 后，配对乘以 $`a^2`$。若度量在 jet 延拓的解消中心 $`\widetilde g_a`$ 的加权 $`C^2`$ 邻域内，即

```math
|\nabla^j(a^{-2}g-a^{-2}\widetilde g_a)|
\le\delta a^2(1+|y|)^{w-j},
\quad 0\le j\le2,\quad0\le w\lt 2,
\tag{6.12}
```

并在固定外部半径处具有相应界，则对固定有界 $`\delta`$ 有

```math
P(g)\ge\pi^2a^4\bigl(|\mathbf R_p^+\zeta|-\varepsilon_w(a,\delta)\bigr)_+^2,
\qquad\varepsilon_w(a,\delta)\longrightarrow0.
\tag{6.13}
```

取截断的 $`\sum_i(\mathbf R^+\zeta)_io_i`$ 作测试，Cauchy–Schwarz 和 (6.10)–(6.11) 给主项。背景的 Einstein jet 方程消去原本不衰减的二次余项；余核衰减 $`r^{-4}`$、$`w\lt 2`$ 使扰动通量和非线性项均为 $`o(a^2)`$。因此此处限制的是规定解消邻域中的逼近速率，并非尺度无关的正间隙。

若背景全局 Einstein，Biquard–Ozuch 的模余核线性解给适配的解消度量

```math
P(g_a^*)=\pi^2a^4|\mathbf R_p^+\zeta|^2+O(a^6).
\tag{6.14}
```

取包含该一阶修正的邻域，(6.13) 与 (6.14) 匹配；不能要求它位于任意缩小的原始中心邻域。若 $`\mathbf R^+\zeta=0`$，同一构造给 $`P(g_a^*)=O(a^8\log(1/a))`$，但该阶的最优系数尚未决定。若背景只在奇点附近 Einstein，上界须另加 $`P(g_V)`$。近等号时 Cauchy–Schwarz 还迫使无迹 Ricci 的主要部分集中于三个余核方向。

这里的经典输入为 Ozuch，[Higher order obstructions to the desingularization of Einstein metrics](https://arxiv.org/abs/2012.13316v3)，Lemma 2.3 及 §2.1。该文在相应稳定性与可积性条件下给出一阶障碍消失后的二阶分量 $`C\det(\mathbf R^+|_{\zeta^\perp})`$。若其余两个特征值为 $`u,v`$、$`u+v=\Lambda`$，§2.3 的优化 Burns 二阶系数同时满足

```math
\Phi_{\rm opt}=-\frac{(u-v)^2}{2}
=-\frac{\Lambda^2}{2}+2\det(\mathbf R^+|_{\zeta^\perp}).
\tag{6.15}
```

于是两种 ALE 插入读取相同的局部不变量：一阶看 $`\mathbf R^+`$ 的核，二阶看其余二维空间的行列式。该关系没有把 Ozuch 的二阶障碍转成无条件充分条件，也没有使任意近极小序列自动满足 (6.12)。

## 7. 完备有限体积 Einstein 域与塌缩补域

ALE 轨形解消不是所有退化的统一模型。完备有限体积 Einstein 域可能留下塌缩或尖点补域；这些区域的可见曲率量由边界特征数决定。

### 7.1 边界恒等式与极限曲率积分

对带边界紧域 $`D`$ 定义

```math
\mathscr C_\pm(g;D)=\frac1{2\pi^2}\int_D|W^\pm|^2
+\frac1{96\pi^2}\int_Ds^2,\qquad
\widehat P(g;D)=\frac{P(g;D)}{8\pi^2}.
```

将 Euler 边界项记为 $`\mathscr E`$，签名 eta 项及 transgression 之和记为 $`\mathscr H`$，采用

```math
\chi(D)=\int_De+\mathscr E,\qquad
\int_DL=\tau(D)+\mathscr H.
```

则

```math
\widehat P=\mathscr C_\pm-(2\chi\pm3\tau)(D)+\mathscr Q_\pm(\partial D),
\quad \mathscr Q_\pm=2\mathscr E\mp3\mathscr H.
\tag{7.1}
```

共同边界的两侧取向相反，边界项随之反号。

设 $`M=X\#k\overline{\mathbb{CP}}^{\,2}`$ 上一列度量具有下列实际极限：

- 在开集 $`\Omega`$ 上，经微分同胚后 $`C^2_{\rm loc}`$ 收敛到完备有限体积、标量常数 $`s_\infty\lt 0`$ 的 Einstein 度量；
- $`P(g_i)\to0`$、$`L_s(g_i)\to0`$、$`\bar s_i\to s_\infty`$，且总体积收敛到 $`\mathop{\mathrm{Vol}}\nolimits(\Omega,g_\infty)`$；
- $`\Omega_\rho\uparrow\Omega`$ 是嵌套紧穷竭，其补域各连通分支 $`C_j^{(\rho)}`$ 的拓扑和所接端的集合固定。

则各补域有非负极限曲率积分

```math
q_j=\lim_{\rho\to0}\lim_{i\to\infty}\mathscr C_+(g_i;C_j^{(\rho)})\ge0,
```

满足

```math
q_j=(2\chi+3\tau)(C_j)
+\lim_{\rho\to0}\sum_{L\text{ 接于 }C_j}\mathscr Q_+(L;g_\infty),
\qquad
\mathscr C_+(g_\infty;\Omega)=A-k-\sum_jq_j.
\tag{7.2}
```

这里链接取 $`\partial\Omega_\rho`$ 的取向。多端补域给出的是边界项之和的极限；单独各端的极限还需其渐近结构。

证明在每个固定 $`\rho`$ 上使用 (7.1)、局部收敛和 $`P(C_j)\to0`$，再由非负密度和嵌套性取得外层极限。标量部分消失的关键为

```math
\int_{C_j}s_i^2\le2L_s(g_i)+2\bar s_i^2\mathop{\mathrm{Vol}}\nolimits(C_j,g_i).
```

无体积损失使全部补域体积的上极限不超过 Einstein 域的尾部体积，后者随 $`\rho\to0`$ 趋零。因此补域的 Weyl 极限为 $`\int_{C_j}|W^+|^2\to2\pi^2q_j`$，但并不要求该能量为零。

### 7.2 全局混合不等式限制补域

若全部光滑度量满足 LeBrun 混合曲率下界，则

```math
\boxed{9k+8\sum_jq_j\le3A.}
\tag{7.3}
```

在主体上写 $`x=S/(96\pi^2)`$、$`y=I_+/(2\pi^2)`$，有

```math
\int_\Omega(s-\sqrt6|W^+|)^2
\le12\pi^2(\sqrt{8x}+\sqrt y)^2
\le108\pi^2(x+y).
```

而 $`x+y=A-k-\sum q_j`$。补域的标量平方积分趋零，但其混合积分趋于 $`12\pi^2q_j`$。相加便得

```math
72\pi^2A\le108\pi^2(A-k-\sum q_j)+12\pi^2\sum q_j,
```

即 (7.3)。所以 $`q_j>0`$ 的补域必须集中正手性 Weyl 能量，不能把它等同于曲率有界的纯体积塌缩。

### 7.3 圆纤维尖点的相对特征数

若端部满足 Dai–Wei 的圆纤维尖点渐近，链接作为 $`\partial\overline\Omega`$ 的 Euler 数为 $`e`$，其边界公式为

```math
\mathscr Q_+^\infty=-e+3\mathop{\mathrm{sign}}\nolimitse,\qquad
\mathscr Q_-^\infty=e-3\mathop{\mathrm{sign}}\nolimitse.
```

所用渐近条件及绝热 eta 公式见 Dai–Wei，[Hitchin–Thorpe inequality for noncompact Einstein 4-manifolds](https://web.math.ucsb.edu/~dai/paper/dwAIM.pdf)，Theorems 3.5、5.1。

对作为补域边界的 $`e_{\rm out}=-e`$，

```math
q_+=(2\chi+3\tau)(C)+e_{\rm out}-3\mathop{\mathrm{sign}}\nolimitse_{\rm out}.
\tag{7.4}
```

设 $`\partial C=S^3`$、$`b_1=b_3=b_2^+=0`$、$`b_2^-=r\ge1`$。则 $`2\chi+3\tau=2-r`$，两种 Hopf 取向分别给 $`q_+=4-r`$ 和 $`q_+=-r`$。非负性排除后一取向，并强迫可行补域最多携带四个异常秩。

若全部异常拓扑分布在 $`N`$ 个这样的补域中，$`\sum r_j=k`$，另有 $`B`$ 个 $`q_+=4`$ 的球补域，则 (7.3) 等价于

```math
\boxed{k+32N+32B\le3A.}
\tag{7.5}
```

特别地，每个异常类各占一个补域时，$`k\le A/11`$。若四个类成组、$`N=k/4`$ 且 $`B=0`$，只恢复 $`k\le A/3`$，没有排除这一形态。四秩补域的 $`q_+=0`$，但反取向公式给 $`q_-=20`$，即

```math
\int_C|W^-|^2\longrightarrow40\pi^2.
```

它对混合自对偶曲率估计不可见，却仍具有固定全曲率。相符的拓扑组合是秩四 $`D_4`$ ALF 核心与穿孔 $`\mathbb{RP}^2`$ 二维实向量丛，其同调包含指数二扩张 $`-D_4\subset-I_4`$；相对光滑识别及匹配的低能量过渡尚未构造。

这一拓扑组合可说得更精确。令 $`N`$ 为秩四 $`D_4`$ ALF 核心，$`\partial N=S^3/Q_8`$、$`\pi_1N=1`$、$`(\chi,\tau)=(5,-4)`$；令 $`W`$ 为边界取相反取向的 $`\mathbb{RP}^2`$ 实二维圆盘丛，$`\pi_1W=\mathbb Z_2`$。由于 $`Q_8\to\mathbb Z_2`$ 满射，$`N\cup W`$ 单连通，具有 $`\chi=6,\tau=-4`$。Donaldson 与 Freedman 定理分别给交形式 $`-I_4`$ 和到 $`\#4\overline{\mathbb{CP}}^{\,2}`$ 的同胚；微分同胚及边界相对识别仍未确定。$`W\cup c(S^3/Q_8)`$ 的底空间单连通、$`H_2=\mathbb Z_2`$，故只是有理同调四维球面。过渡域 $`W\setminus B^4`$ 的 $`\chi=\tau=0`$，两种手性的边界特征数项均相消；这允许曲率能量趋零，却尚未给出这样的度量。

这些结论以本节明确的 Einstein 域收敛和无体积损失为前提。一般极小化序列尚未自动产生这些条件。紧复双曲基本群不含 $`\mathbb Z^2`$，只能排除尖点链接群的某些单射；若链接到主体的映射有核，就不能据此排除尖点或塌缩。

### 7.4 Einstein 方程进一步限制尖点

边界特征数项允许的补域还须匹配真实 Einstein 端。考虑圆纤维束 $`Y\to B`$ 上的固定基底模型

```math
g_0=dr^2+\pi^*g_B+e^{-2\kappa r}f^2\eta^2,
\qquad \kappa>0,\quad f>0,
\tag{7.6}
```

其中 $`B`$ 为闭曲面或轨形曲面，$`\eta`$ 为联络。若 $`\mathop{\mathrm{Ric}}\nolimits_g=\lambda g`$，且在 $`g_0`$ 正交标架中
$`g-g_0=o(1)`$、$`\mathop{\mathrm{Ric}}\nolimits_g-\mathop{\mathrm{Ric}}\nolimits_{g_0}=o(1)`$，则

```math
\boxed{\lambda=-\kappa^2,\qquad df=0,\qquad K_B=\lambda\lt 0.}
\tag{7.7}
```

证明直接来自径向和混合 Ricci 分量：
$`\mathop{\mathrm{Ric}}\nolimits_{g_0}(\partial_r,\partial_r)=-\kappa^2`$，
$`\mathop{\mathrm{Ric}}\nolimits_{g_0}(\partial_r,\widehat Y)=\kappa Y(f)/f`$。
于是 Einstein 方程先给 $`\lambda=-\kappa^2`$、$`df=0`$；联络曲率的 O'Neill 项为 $`O(e^{-2\kappa r})`$，水平分量遂给 $`K_B=\lambda`$，最后 Gauss–Bonnet 给 $`\chi^{\rm orb}(B)\lt 0`$。

相对 $`C^2`$ 收敛足以保证这里的两个收敛条件；仅有纤维尖点重标切丛上的光滑延拓并不足够。例如扰动 $`xq(\theta)dy^2`$ 沿单位竖直向量 $`x^{-1}\partial_\theta`$ 的导数不趋零。因此 (7.7) 排除的是所述相对渐近范围内的 $`S^2`$ 或 $`T^2`$ 固定基底端；实、复双曲的缩小基底尖点不在此模型中。

对尚允许的光滑基底 $`\Sigma_g`$，$`g\ge2`$，单个圆盘丛补域 $`C=D_e(\Sigma_g)`$ 的 (7.4) 化为

```math
q_+(C)=4-4g+e.
\tag{7.8}
```

非负性要求 $`e\ge4g-4`$。若嵌入的零截面具有相应 Seiberg–Witten 基本类条件（$`b^+>1`$，或另给适用的腔室数据），伴随不等式又给 $`2g-2\ge e+|L\cdot\Sigma_g|\ge e`$，两式矛盾。故这种单曲面圆盘丛补域被排除；多类补域及轨形基底仍须分别研究。§7.3 的 Hopf 边界项与 $`A/11`$ 阈值是正确的条件性计算，但其 $`S^2`$ 固定基底 Einstein 端已经被 (7.7) 排除。

另有不依赖指定尖点剖面的排除。设端部的球面提升为双轴形式

```math
g=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)+c(t)^2\sigma_3^2,
\quad t\in[t_0,\infty),\quad
d\sigma_i=2\sigma_j\wedge\sigma_k,
\tag{7.9}
```

并可下降至 $`S^3/\Gamma`$，其中 $`\Gamma\subset SU(2)`$ 有限。若 $`|\mathop{\mathrm{Rm}}\nolimits|`$ 有界，且 Einstein 张量满足
$`G(\partial_t,\partial_t)\ge0`$（特别是 Einstein 常数 $`\lambda\le0`$），则该端的体积必为无穷。

为证明，先对一般对角形式置 $`a_i'/a_i=\lambda_i`$、$`x_i=a_i^2`$。径向 Riccati 方程
$`\lambda_i'=-\lambda_i^2-K(\partial_t,e_i)`$
与端部完整性使 $`|\lambda_i|`$ 有界。截面的内蕴 Ricci 满足

```math
r_i=\frac{2[x_i^2-(x_j-x_k)^2]}{x_1x_2x_3},
\qquad r_i+r_j=\frac{4(x_i+x_j-x_k)}{x_ix_j}.
\tag{7.10}
```

Gauss 方程给 $`r_i`$ 有界；排序 $`x_1\ge x_2\ge x_3`$ 后，$`r_1+r_2\ge4/x_2`$，所以第二大尺度有正下界。若双轴端体积有限，有界对数体积导数使 $`v=a^2c\to0`$，继而 $`a\ge b_0`$、$`c\to0`$。Hamilton 约束却给

```math
\lambda_a(\lambda_a+2\lambda_c)
=\tfrac12s_\Sigma+G(\partial_t,\partial_t)
\ge\frac4{a^2}-\frac{c^2}{a^4}>0.
\tag{7.11}
```

因此 $`\lambda_a`$ 最终符号固定。正号使
$`(\log v)'=\frac32\lambda_a+\frac12(\lambda_a+2\lambda_c)>0`$，与 $`v\to0`$ 矛盾；负号使 $`a`$ 递减，(7.11) 的右端继而有正下界，故 $`\lambda_a`$ 一致为负，迫使 $`a\to0`$，又与 $`a\ge b_0`$ 矛盾。此证明覆盖所有双轴剖面；有限商不正规时，只需球面提升的双轴性质，不要求全局 $`U(2)`$ 作用下降。

一般三轴端也可在 $`\liminf\sigma_2>0`$ 下排除有限体积，其中 $`\sigma_2=\sum_{i\lt j}\lambda_i\lambda_j`$。因为 $`H^2\ge3\sigma_2`$，体积收缩分支具有 $`H\lt 0`$；任意对和 $`u=\lambda_i+\lambda_j\ge0`$ 会给 $`\sigma_2\le Hu-3u^2/4\le0`$，故所有对和都一致为负，使所有 $`a_ia_j\to0`$，违反第二大尺度的正下界。对 $`\mathop{\mathrm{Ric}}\nolimits=-3g`$，一个充分条件为

```math
\liminf s_\Sigma>-6,
\qquad\text{例如}\quad
\limsup\frac{(a_1^2-a_2^2)^2}{a_1^2a_2^2a_3^2}\lt 3
\quad(a_3\text{ 为最小尺度}).
\tag{7.12}
```

这些端部约束使用完整的 Einstein 方程，因而比补域特征数条件更强。没有固定基底渐近、双轴提升或 (7.12) 的一般塌缩端仍未被排除；也尚未从任意极小化序列提取本节所需的端部结构。

## 8. 未解的极值与取得性问题

上述结果决定了固定成对 $`A_1`$ 轨形的两个极值，在一般型吹起曲面上构造了严格低于标准插入能量的度量，并排除了若干可能的光滑极小化极限。它们也给出全部竞争度量必须满足的共形关系、近极小变分关系及实际场结构。

| 变分问题 | 已有结论 | 尚未决定的内容 |
|---|---|---|
| 平衡手术族 | 渐近系数严格小于 $`4`$ 的构造、有限参数归一化、覆盖与安放条件 | 匹配的全度量下界及最佳首项 |
| 一般型纯吹起曲面 | $`P_*\lt 8\pi^2k`$；共形 Kähler 分离；联合 $`(\kappa,\upsilon)`$ 可行区 | $`P_*`$ 的精确值和小 $`k/A`$ 时的真实尺度 |
| 非 Bach-flat 光滑极小元 | 明确正能量候选、下降方向、退化例和部分气泡替换 | 至少一个符合全部条件的光滑取得实例 |
| 固定成对 $`A_1`$ 轨形 | 精确下确界及除临界参数外的不取得性 | 临界参数 $`k=A/3`$ 时的常负标量自对偶度量是否存在 |
| Ricci-flat ALE 解消的 Einstein 主体 | 标量、混合曲率和根格的有限参数必要条件 | 相容的实际嵌入、Einstein 主体与完整拼接 |
| 有限体积 Einstein 域 | 补域曲率积分的非负性、$`9k+8\sum q_j\le3A`$；固定基底与双轴端的限制 | 一般序列的结构提取及未排除补域的几何实现 |

不存在精确 Einstein 度量、$`P_*>0`$、$`\alpha>0`$ 和极小值能否光滑取得是不同断言。Ricci-flat 核心可有非零二阶拓扑而 $`P`$ 仍可为零；塌缩也可使下确界不取得。因此，严格插入构造降低标准模型能量以后，决定全局最优值的关键在于实际竞争几何如何同时实现主体、核心、边界配对与规范场，而不在于继续把标准核心能量独立相加。

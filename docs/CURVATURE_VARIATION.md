# 曲率极值、几何构造与退化

无迹 Ricci 能量研究一个光滑流形能否在积分意义下逼近 Einstein 方程。全局下界限制所有竞争度量；插入和恢复构造给出可实现的上界；取得性则要求理解极小化序列的集中、塌缩和光滑极限。以下统一这些问题的泛函、构造和变分关系，并分别处理光滑流形、固定轨形及完备 Einstein 域。

## 1. 泛函与共形归约

设 $M$ 为闭连通定向光滑四维流形。Ricci 使用张量范数，Weyl 和完整曲率使用曲率算子范数。记

$$
P=\int_M|\operatorname{Ric}^{\circ}|^2,\quad S=\int_Ms^2,\quad
I_\pm=\int_M|W^\pm|^2,\quad W=I_++I_-,\quad
R=\int_M|\operatorname{Ric}|^2=P+S/4,
$$

$$
V=\operatorname{Vol}(M,g),\quad T_s=\int_Ms,\quad
L_s=S-T_s^2/V,\quad T_\pm=2\chi(M)\pm3\tau(M).
$$

所有积分取 $dV_g$。定义

$$
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}_g-\lambda g|^2}{\lambda^2V},\qquad
P_*(M)=\inf_gP(g),\qquad\alpha(M)=\inf_g\mathcal E(g).
$$

当 $R>0$ 时，$\mathcal J=4P/R$，直接对 $1/\lambda$ 极小化得

$$
\mathcal E=4-\frac{T_s^2}{VR}=\mathcal J+\frac{L_s}{R}.
\tag{1.1}
$$

Ricci-flat 度量满足 $\mathcal E=4$，此时 $\mathcal J$ 不定义。四维整体缩放保持 $P,S,I_\pm$ 不变。Chern–Weil 恒等式为

$$
4\pi^2T_\pm=\frac S{24}+2I_\pm-\frac P2,
\qquad
\int|\operatorname{Rm}_{\rm op}|^2=8\pi^2\chi+P.
\tag{1.2}
$$

因此全曲率极小化与 $P$ 极小化等价；$\alpha$ 还取决于分母和标量方差，不能通过相减两个独立下确界求得。

### 1.1 负 Yamabe 代表与两种极值的比较

同一负 Yamabe 共形类中，令 $\widehat g$ 为常标量代表，$\delta=S(g)-S(\widehat g)\ge0$。共形不变的 Weyl 能量和 (1.2) 给出

$$
P(g)=P(\widehat g)+\delta/12,\qquad
R(g)=R(\widehat g)+\delta/3,
$$

$$
\mathcal J(g)=
\frac{R(\widehat g)}{R(\widehat g)+\delta/3}\mathcal J(\widehat g)
+\frac{\delta/3}{R(\widehat g)+\delta/3}.
\tag{1.3}
$$

特别地，$\mathcal J(g)<1$ 时 $\mathcal E(\widehat g)=\mathcal J(\widehat g)\le\mathcal J(g)$。若每个共形类均为负类且 $\inf\mathcal E<1$，便有 $\inf\mathcal E=\inf\mathcal J$。

设每个共形类均为负 Yamabe 类，全度量标量下界为 $S\ge32\pi^2A>0$，且 $T_+>0$。写 $p_*=P_*/(8\pi^2)$。对 $P$ 极小化序列作负 Yamabe 替换，并用 $I_+\ge0$，得到

$$
\frac{p_*}{p_*+3T_+/4}
\le\alpha(M)\le\frac{4p_*}{A+p_*}.
\tag{1.4}
$$

左式来自 $R\le4P+24\pi^2T_+$；右式使用 $R\ge P+8\pi^2A$。在这些假设下，$P_*=0$ 与 $\alpha=0$ 等价。精确的常标量公式是

$$
\mathcal E(\widehat g)=\frac{16P(\widehat g)}{4P(\widehat g)+Y([g])^2},
\tag{1.5}
$$

其中 $Y([g])$ 为 Yamabe 常数。省去分母的 $4P$ 只给出一个上界，不能用于精确归一化。

### 1.2 全局 Weyl–Yamabe 极值公式

令 $d([g])=8\pi^2\chi-W(g)$。由 Gauss–Bonnet，

$$
P=S/12-2d,\quad R=S/3-2d,\quad
\mathcal E-1=\frac{L_s-6d}{R}.
\tag{1.6}
$$

在 $d>0$ 的共形类中，$Y\ne0$，且 $S\ge Y^2$；常标量 Yamabe 代表达到这个最小值。因 $1-6d/(S/3-2d)$ 随 $S$ 递增，(1.1) 给出类内最小值。全局于是满足

$$
\boxed{\displaystyle
\alpha(M)=1-6\sup\left(\{0\}\cup
\left\{\frac{d([g])}{Y([g])^2/3-2d([g])}:d([g])>0\right\}\right).}
\tag{1.7}
$$

公式中的上界 $\alpha\le1$ 可独立构造：在一个正规点插入长度 $L$ 的单位圆柱 $S^3\times[0,L]$，两端采用固定过渡。圆柱上 $s=6$、$|\operatorname{Ric}|^2=12$、$|\operatorname{Ric}^{\circ}|^2=3$，故 $4P,R$ 均为 $24\pi^2L+O(1)$，而 $L_s=O(1)$。于是 $\mathcal E\to1$。同一构造适用于有孤立奇点的紧轨形的正规点。

因此

$$
\alpha(M)<1\quad\Longleftrightarrow\quad
W_*(M):=\inf_gW(g)<8\pi^2\chi(M).
\tag{1.8}
$$

签名不等式 $W\ge12\pi^2|\tau|$ 又给出

$$
2\chi\le3|\tau|\quad\Longrightarrow\quad\alpha=1.
\tag{1.9}
$$

严格小于时不取得；等号时，取得要求相应手性的 Weyl 张量消失且标量为非零常数。例如 $\operatorname{MinVol}(M)=0$ 给出 $P_*=0$，同时 $\chi=\tau=0$，所以 $\alpha=1$。零绝对能量下确界与零相对缺陷下确界在没有 (1.4) 的输入时可以完全不同。

连通和的 Weyl 恢复给 $W_*(M\#N)\le W_*(M)+W_*(N)$。若 $d_*=8\pi^2\chi-W_*$，则

$$
d_*(M\#N)\ge d_*(M)+d_*(N)-16\pi^2.
$$

例如 $\#n\overline{\mathbb{CP}}^{,2}$ 满足 $W_*=12n\pi^2$、$d_*=4\pi^2(4-n)$，故 $n\le3$ 时 $\alpha<1$，$n\ge4$ 时 $\alpha=1$。

来源：[相对缺陷与联合共形极值](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §§1、5–6。

## 2. 低成本手术与真实上界

### 2.1 从有限尺度证书到任意固定复双曲领口

区间积分给出有限尺度光滑单元的严格上界。解析构造进一步证明：每个固定半径 $R_0>0$ 的复双曲领口内，都存在普通负单吹起单元，在外部精确等于 $\operatorname{Ric}=-6g$，并满足

$$
\frac{P(g_\epsilon)}{8\pi^2}
=1-9\epsilon^2\log(1/\epsilon)+O_{R_0}(\epsilon^2),
\qquad
\frac{J_6(g_\epsilon)}{8\pi^2}
=1-9\epsilon^2\log(1/\epsilon)+O_{R_0}(\epsilon^2),
$$

其中 $J_6(g)=\int|\operatorname{Ric}_g+6g|^2$。两式均包括 Burns 核心、颈部和外过渡；内外过渡的总误差为 $O_{R_0}(\epsilon^2)$。因此充分小的正 $\epsilon$ 给出 $P,J_6<8\pi^2$。

来源：[O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) §§0–6。完整颈部推导及符号程序的入口见该文 §8。

### 2.2 覆盖量词和极限次序

设 $X_0$ 为固定紧复双曲曲面，$X_j\to X_0$ 为度数趋于无穷的有限非分歧覆盖，$A_j=c_1^2(X_j)$。令

$$
M_j=X_j\#k_j\overline{\mathbb{CP}}^{\,2}\#\ell_j(S^1\times S^3).
$$

原平衡比例为

$$
Q_j=k_j+4\ell_j\to\infty,\quad h_j=Q_j/A_j\to0,\quad
k_j/Q_j\to2/9,\quad\ell_j/Q_j\to7/36
$$

在这些比例下，适合基底小嵌入球的固定单元可复制至 $M_j$，得到

$$
\limsup_j\frac{\alpha(M_j)}{h_j}
\le4-\frac89\delta_{X_0}<4.
$$

其中 $\delta_{X_0}>0$ 是固定单元相对于 $8\pi^2$ 的归一化节省，可依赖 $X_0$。极限次序为：固定领口和一个足够小的正插入参数，再令覆盖度数趋于无穷。

另一路使用一个已有固定半径单元：对于事先给定、嵌套且子群交集平凡的残余覆盖塔，某一级以后具有正比例的该单元安放位置。此结论也适用于非正规塔，仅使用固定球在某一级的嵌入。在该量词下，既有区间证书与共形尾部恢复给出

$$
\limsup_j\alpha(M_j)/h_j\le3.9961446513521015108\ldots<4.
$$

数值证书给出特定单元的显式上界；任意固定小领口的构造扩大了覆盖序列的适用范围。

来源：[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §§3–5；任意固定基底覆盖序列的扩展见 [O11_Arbitrary_Collar_Logarithmic_Construction.md](../archive/originals/2026-10-07/O11_Arbitrary_Collar_Logarithmic_Construction.md) §6。

令 $\mathfrak P_{8n,7n}$ 为具有 $8n$ 个吹起、$7n$ 个柄及固定完整外部标记的混合单元 $P$ 能量下确界。次可加性给出

$$
\gamma_{\rm bal}=\lim_{n\to\infty}
\frac{\mathfrak P_{8n,7n}}{72\pi^2n}
=\inf_n\frac{\mathfrak P_{8n,7n}}{72\pi^2n},
\qquad \limsup_j\alpha(M_j)/h_j\le\gamma_{\rm bal}.
$$

反向不等式需要将一般竞争度量局部化至该单元范畴，或建立相应全局下界。

### 2.3 一般背景的张量机制

在一般负 Kähler–Einstein 背景上，节省量由插入方向与背景曲率的耦合决定。写 $R^+=W^++sI/12$，表示自对偶曲率块，与积分量 $R$ 采用不同记号。首先，对任意固定光滑背景、任意点 $p$ 和单位方向 $\zeta\in\Lambda_p^+$，以 $x^{1/5}$ 为截断半径插入异常面积为 $\pi x$ 的 Burns 核心，得到

$$
P(g_x)=P(g)+8\pi^2\bigl(1-xR^+_p(\zeta,\zeta)\bigr)+O(x^{6/5}).
$$

证明由标量平坦、自对偶平坦的 Burns 尾部及其球面 transgression 给出；其中标量通量为 $4\pi^2x$，自对偶通量为 $\pi^2\zeta\otimes\zeta$。在负 KE 背景上，$\omega^\perp$ 是一阶响应的核；实双曲背景则 $R^+=sI/12<0$，每个方向都增加一阶成本。这个任意背景的一阶结论不要求 $P$-临界性。

若背景在插入支撑邻域内为 $P$-临界，再选择角修正，可进一步展开为

$$
P(g_\epsilon)=P(g)+8\pi^2-8\pi^2\epsilon R^+_p(\zeta,\zeta)
 +4\pi^2\Phi\epsilon^2\log(1/\epsilon)+O(\epsilon^2).
$$

当 $\operatorname{Ric}^{\circ}_p=0$、$R^+\zeta=\mu\zeta$ 时，优化系数为

$$
\Phi=-\mu(\mu-s/8)-|T|^2,\qquad
T=(R^+|_{\zeta^\perp})^{\circ}.
$$

角修正使反手性 Weyl 二阶背景项在目标曲率组合 $(2W^+,s/\sqrt{12})$ 中消去。核方向上的负对数项为 $-4\pi^2|T|^2\epsilon^2\log(1/\epsilon)$。在负 KE 背景的垂直方向，$|T|^2=s^2/32$，故固定 $k$ 个点的构造满足

$$
\frac{P(\widetilde g_\epsilon)}{8\pi^2}
=k-\frac{ks^2}{64}\epsilon^2\log(1/\epsilon)+O(\epsilon^2)<k.
$$

这里 $T$ 是 $\zeta^\perp$ 上限制算子的无迹部分；$\Phi$ 为插入角修正所确定的二阶对数系数。系数公式适用于所列特征向量方向；一般方向还含旋转零模。其非正性在核方向成立，在整个 $R^+\le0$ 锥上则不成立。余项常数依赖固定光滑背景和插入数据。

来源：[一般背景的曲率插入展开](../archive/originals/2026-10-08/01_Research_Synthesis.tex) §3。


展开中的对数项可以由三个区域区分出来。取 Burns 尾部 $A_0=\partial\bar\partial_\zeta\log r^2$，在固定背景的正规坐标中插入 $\epsilon A_0$ 和零次齐次角修正。内区 $r\asymp\sqrt\epsilon$ 的误差是 $O(\epsilon^2)$；外过渡的一阶变分由背景的局部 $P$-临界性消去，余项也是 $O(\epsilon^2)$。中间区以 $\sigma=\epsilon/r^2$ 展开，其径向密度具有形式

$$
\epsilon r\,\gamma_1(r)
+\frac{\epsilon^2}{r}\gamma_2(r)
+\frac{\epsilon^3}{r^3}\gamma_3(r,\sigma),\qquad
\gamma_2(0)=8\pi^2\Phi.
$$

积分区间下端为 $O(\sqrt\epsilon)$，故第二项产生 $4\pi^2\Phi\epsilon^2\log(1/\epsilon)$。背景三阶及更高阶项均只进入可积余项。反手性消去必须同时计入 Hodge 投影随度量的变化。

这证明对每个固定极小一般型曲面 $X$ 和每个 $k\ge1$，

$$
\boxed{P_*(X\#k\overline{\mathbb{CP}}^{,2})<8\pi^2k.}
\tag{2.1}
$$

若典范模型有 ADE 奇点，先在正规部固定插入点和一个严格节省量，再令 Ricci-flat 解消尺度趋零；不能将这两个选择顺序倒置。常数依赖背景，对任意共同退化背景的一致性不由此得到。

### 2.4 有限参数归一化与安放容量

设一个固定复双曲单元的完整 $P$ 成本为 $8\pi^2p_c$，$p_c<1$。在复双曲覆盖中能安放 $8n$ 个该单元和 $7n$ 个独立柄单元时，令 $Q=36n$、$h=Q/A$、

$$
C_c=\frac{28}{9}+\frac89p_c.
$$

柄单元来自 $S^1\times S^3$ 的标量平坦、共形平坦 Green 构造，成本为 $32\pi^2$。其尺度取 $\delta$、拼接半径取 $\sqrt\delta$，过渡能量和尾部误差均为 $O(\delta^2)$。因此 (1.4) 给出有限参数上界

$$
\boxed{\frac{\alpha(M)}h\le\frac{C_c}{1+C_ch/4}.}
\tag{2.2}
$$

已有单元 $p_c<0.995662732772$ 给 $C_c<3.996144651353$。这里不需要先令 $h\to0$；假设是所需完整单元确实能同时安放。选择一个具有足够大整体注入半径的有限正规覆盖后，其所有进一步有限覆盖继承这些位置。对任意固定基底覆盖序列，则使用 §2.1 的小领口单元，节省常数允许依赖基底。

一般固定负 KE 背景也可取局部单元的固定节省 $\eta_X>0$。若吹起占 $Q=k+4\ell$ 的比例为 $\vartheta=k/Q$，相应构造给

$$
\frac{\alpha(M)}h\le
\frac{4(1-\vartheta\eta_X)}{1+h(1-\vartheta\eta_X)}.
\tag{2.3}
$$

这不自动把原平衡族的线性下界推广到所有 KE 背景。非复双曲背景的 $3c_2-c_1^2$ 在有限覆盖下同比例增长，其原有 Weyl 余量可能使指定的平衡小 $h$ 条件无法实现。

### 2.5 Weyl 上界越过三分之一边界

固定外领口的复双曲单元满足相对恒等式

$$
p_c-1=\frac{\Delta I_+}{2\pi^2}+\frac{\Delta S}{96\pi^2}.
$$

若 $\eta=-\Delta I_+/(2\pi^2)>0$，在 $Y$ 的 $N$ 个不相交固定球中选 $n\le\min(k,N)$ 个使用该单元，其余吹起采用小尺度经典恢复，则

$$
d_*(Y\#k\overline{\mathbb{CP}}^{,2})
\ge4\pi^2\left(A/3-k+\eta n\right).
\tag{2.4}
$$

所以 $k<A/3+\eta n$ 已保证 $\alpha<1$。这改善了只由 Kähler 恢复看到的 $k<A/3$ 区域。

安放比例是这条结论的实际限制。在 $\operatorname{Ric}=-g$ 的复双曲归一化中，令 $X_R=\sinh^2(R/\sqrt6)$。若整体注入半径大于 $2R$，最大不相交 $R$-球族满足

$$
\frac{1}{9[4X_R(1+X_R)]^2}\le\frac NA\le\frac1{9X_R^2}.
$$

因此可以得到一个明确但较小的边界扩大；不能把单元本身的节省率当作所有吹起都能以同一尺寸实现的节省率。式 (2.2)–(2.4) 都是全局构造上界，未决定最终极小值。

### 2.6 无对称限制的完整单元共形归约

令完整光滑单元在紧集外精确等于 $\operatorname{Ric}=-6g$ 的复双曲端，并固定端部识别。存在唯一正函数 $u\to1$ 满足

$$
-6\Delta_gu+s_gu+24u^3=0,\qquad \widehat g=u^2g,\quad s_{\widehat g}=-24,
$$

其中 $\Delta=\operatorname{div}\nabla$。不要求原度量的标量处处为负，也不要求任何对称性。证明在精确端上用 $1-e^{-a(r-R)}$ 与 $1+(M-1)e^{-a(r-R)}$ 作上下屏障，在核心内分别延为零和足够大的常数，随后作穷竭并使用强最大值原理。线性化 $-6\Delta+48$ 给出

$$
|\nabla^j(u-1)|=O(e^{-mr}),\qquad 4<m<2+2\sqrt3,
$$

对每个固定 $j$ 成立。这个衰减快于端的体积增长，故共形 transgression 的线性边界项消失，得到精确能量差

$$
P(g)-P(\widehat g)
=24\int|\nabla u|^2+3\int(\Delta u/u)^2,
\tag{2.5}
$$

$$
J_6(g)-J_6(\widehat g)
=P(g)-P(\widehat g)+\frac14\int(s_g+24)^2.
$$

因而，在同一标记单元上，精确复双曲端的 $P$ 与 $J_6$ 下确界相等，也等于常标量 $-24$、渐近速率 $\mu$ 满足 $2<\mu<2+2\sqrt3$ 的单元的 $P$ 下确界。逆向证明将渐近端在单位环带上截回精确端，附加平方残差为 $O(e^{(4-2\mu)R})$。这一步给下确界归约，不给取得性。

若单元有 $k$ 个吹起和 $\ell$ 个柄，相对模型球的 Weyl 差为 $\Delta I_+$，则

$$
P(\widehat g)-8\pi^2(k+4\ell)=4\Delta I_++48\operatorname{RV}(\widehat g).
\tag{2.6}
$$

相对体积 $\operatorname{RV}$ 包含匹配截面的原体积差及完整单元上的 $\int(u^4-1)dV_g$。改变截面但保持端部识别不改变它。Weyl 能量的减少必须与这同一个常标量代表的相对体积共同计算；单独一个负 Weyl 差不能给出 $P$ 的最优值。

来源：[完整复双曲端的共形归约与证明](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md)；[相对曲率恒等式](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md) §1。

## 3. 全部竞争者上的约束与近极小变分

### 3.1 Kähler 类与低成本竞争者分离

设 $X$ 为极小一般型曲面，$A=c_1^2(X)>0$，$M=X\#k\overline{\mathbb{CP}}^{,2}$。对原取向上任意复结构的 Kähler 度量 $h$ 及 $g=u^2h$，全度量标量预算和 $I_+(h)=S(h)/24$ 给

$$
P(g)-8\pi^2k
=\frac{S(g)-32\pi^2A}{12}
+\frac{S(h)-32\pi^2A}{6}\ge0.
\tag{3.1}
$$

结合 (2.1)，全局共形 Kähler 类不能包含 $P$ 的极小化序列。$\tau(M)\ge0$ 时，相反取向的共形 Kähler 度量也受相应比较限制。

对固定吹起复结构，还可以看出下界的严格性。写 Kähler 类为 $\pi^*a-\sum e_iE_i$，$e_i>0$，令 $q=K_X\cdot a$。Hodge 指标定理给 $q^2\ge Aa^2$，故

$$
\frac{(c_1\cdot[\omega])^2}{[\omega]^2}
=\frac{(q+\sum e_i)^2}{a^2-\sum e_i^2}>A.
$$

于是 $S>32\pi^2A$，$P=S/4-8\pi^2(A-k)>8\pi^2k$；缩小全部吹起面积给其 Kähler 下确界恰为 $8\pi^2k$，但不取得。这里区分了原复结构中的极值与所有 Riemannian 度量中的极值。

来源：[共形 Kähler 分离与 Einstein 候选区域](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §§2–3。

### 3.2 Weyl 缺额和标量超额必须共同实现

在负 Yamabe 代表上定义

$$
\kappa=\frac A2-\frac{3I_+}{8\pi^2},\quad
\upsilon=\frac{Y([g])^2}{32\pi^2}-A\ge0,\quad
p=\frac P{8\pi^2}.
$$

这里 $\kappa$ 是 Weyl 缺额，与端点估计的参数缺陷不同。(1.2) 精确给出

$$
p=k-\frac43\kappa+\frac13\upsilon.
\tag{3.2}
$$

经典混合曲率不等式将 $0\le\kappa\le A/2$ 的区域限制为

$$
p\ge k-\kappa+
\frac{A-\kappa-\sqrt{A^2-2A\kappa}}2.
\tag{3.3}
$$

若 $\kappa<0$，则 $p\ge k-4\kappa/3$。Einstein 候选在 $0<k<A/3$ 时必须满足

$$
\kappa\ge k+
\frac{k^2}{A(1+\sqrt{1-3k/A})^2}>k.
\tag{3.4}
$$

因而 $\kappa\le k$ 若能对所有竞争度量成立，会产生严格正下界；但这项不等式尚未建立。它的具体后果是

$$
p_*\ge p_{\rm flat}:=\frac{A-k-\sqrt{A^2-2Ak}}2
\sim\frac{k^2}{4A},\qquad 0<k<A/2.
\tag{3.5}
$$

再结合反手性预算，便有条件性估计

$$
\alpha\ge\min\left\{1,\frac{4p_{\rm flat}}{4p_{\rm flat}+A+k}\right\}
\sim(k/A)^2.
$$

式 (3.5) 是一个尚缺全局前提的尺度候选。$p/k\to0$ 并不强迫 $\kappa/k\to1$，因为 (3.2) 允许 $\kappa$ 与 $\upsilon$ 同时增长并抵消。实际需要确定的是全部可实现二元数据 $(\kappa,\upsilon)$；单独优化 Weyl 能量无法决定 $P_*$。例如设 $\Theta_*(M)=\sup_{[g]}2\kappa/A$，则 (1.8) 给 $\alpha<1\iff\Theta_*>(3k/A-1)/2$，但 $\Theta_*$ 本身还不足以计算正间隙。

### 3.3 近极小、近驻点和近稳定的统一选择

在原平衡族中设 $h_j=Q_j/A_j\to0$。选择 $P$ 近极小序列使

$$
0\le P(g_j)-P_*(M_j)\le\delta_j,
\qquad \delta_j=o(Q_j^3/A_j^2),
$$

并作负 Yamabe 替换、归一化至 $s=-4$。在该族已有的全曲率预算 $\int|\operatorname{Rm}|^2\le KA_j$ 下，考虑所有满足

$$
\|H\|_\infty\le1,\qquad
\int\bigl(|\nabla^2H|^2+|\nabla H|^4\bigr)\le A_j
\tag{3.6}
$$

的光滑对称张量。对 $F(t)=P(g_j+tH)$，曲率变换公式和 Cauchy–Schwarz 给固定小区间内 $|F''|+|F'''|\le C_KA_j$。由真正的全局极小值 $F(t)\ge F(0)-\delta_j$，分别作二阶、三阶 Taylor 比较，得到

$$
|DP_{g_j}[H]|\le C_K\sqrt{A_j\delta_j}=o(Q_j),\qquad
D^2P_{g_j}[H,H]\ge-C_KA_j^{2/3}\delta_j^{1/3}=-o(Q_j).
\tag{3.7}
$$

估计对 (3.6) 的全部测试同时成立；对不相交支撑测试，也可控制其一阶绝对值之和及二阶负部之和。它不要求统一 Sobolev 常数。常标量下，$DS[H]=8\int\langle\operatorname{Ric}^{\circ},H\rangle$，所以

$$
4DI_+[H]+\frac23\int\langle\operatorname{Ric}^{\circ},H\rangle=o(Q_j).
$$

这给出 $Q_j$ 尺度上的真实变分信息，适用于选出的极小化序列。它没有使任意低能量度量自动近驻点，也没有自动提供强颈部收敛、气泡能量恒等式或光滑取得性。

来源：[全局近极小序列的变分选择](../archive/originals/2026-09-29/02_O11_Variational_Selection.md)。

另一种选择使用加权负梯度流。令 $Q_g$ 为 $P$ 的 $L^2$ 梯度，固定光滑正权 $w$，在流实际存在的区间上，$\partial_tg=-wQ_g$（模微分同胚）满足

$$
\frac{d}{dt}P(g_t)=-\int w|Q_{g_t}|^2.
$$

因此某个时刻的加权残差不超过 $2(P(g_0)-P_*)/T$。这提供了带尺度权重的 Palais–Smale 选择。它不保证从任意初始能量预算出发，流都能存在足够长时间；曲率集中半径与局部 Sobolev 控制也仍须分别建立。仅有自身尺度的 $L^2$ 梯度残差不能推出点态曲率有界。

### 3.4 实际场分解中的节省机制

对具有同度量实际解供给的完整符号类族 $a_\varepsilon=c+\sum\varepsilon_iE_i$，曲率、标量余量和旋量导数可整理为

$$
8\pi^2Q-P=\mathcal N-\mathcal B,\qquad\mathcal B\ge0,
\tag{3.8}
$$

其中 $\mathcal N$ 是按符号类平均的加权非可积能量：在实际场给出的单位方向 $n$ 和幅度 $\rho$ 上，取 $\nabla n$ 的 $W_2$ 分量，积分 $\rho^2|(\nabla n)_{W_2}|^2/2$。各权重、零集处理及非负余项见[同场分解](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md)。

于是严格低成本要求 $\mathcal N$ 支付实际节省。若另有全局强制 $P\ge c\mathcal N$，才会得到 $P\ge8\pi^2Qc/(1+c)$；(3.8) 本身没有提供这个新不等式。

单个符号翻转的相对曲率 $h=(f-f')/2$ 满足

$$
\|h^-\|_2^2-\|h^+\|_2^2=4\pi^2.
$$

异常类的固定配对因此可以主要由反自对偶曲率承担。相对线丛的第一 Chern 类是 $(a-a')/2=\pm E_i$；旋量内积为零也可能只表示正交，不能据此给每个异常类指定一个独立正涡旋费用。全局最优性必须控制这些场的联合实现，而非只把局部标准费用相加。

### 3.5 节省量的 Yamabe 代价与 Weyl 谱余项

仍假设完整符号类族的实际供给，取 $s=-4$ 的 Yamabe 代表。令

$$
\Delta V=V-2\pi^2A=\frac{Y([g])^2-32\pi^2A}{16},\qquad
D_W=\int(2/3-|W^+|^2).
$$

Chern–Weil 给 $8\pi^2k-P=4D_W-4\Delta V$。将同场 Weyl 分解按实际幅度 $0\le r\le2$ 和单位方向 $n$ 优化，其点态密度为

$$
f(W,r,n)=-r^2W(n,n)-4|W|^2-r^3+\frac73r^2-\frac43.
$$

写 $x=-\lambda_{\min}(W)\ge0$，对 $n,r$ 的最大值为 $\varphi(x)-4|W|^2$，其中

$$
\varphi(x)=
\begin{cases}
\frac12[(6x+14)/9]^3-\frac43,&0\le x\le2/3,\\
4x,&x\ge2/3.
\end{cases}
$$

令 $\mathcal K$ 为谱 $(-2/3,1/3,1/3)$ 的 Kähler Weyl 轨道，$\Psi(W)=4/3+2|W|^2-\varphi(x)$。若谱写为 $(-x,x/2-\sigma,x/2+\sigma)$，则

$$
\Psi=\frac53(2/3-x)^2+\frac4{27}(2/3-x)^3+4\sigma^2\quad(x\le2/3),
$$

$$
\Psi=3(x-2/3)^2+4\sigma^2\quad(x\ge2/3).
$$

所以 $\Psi\ge(10/9)\operatorname{dist}(W,\mathcal K)^2$。将这一点态界代回实际场等式，保留非正余项，再用 $4D_W-4\Delta V$ 消去 $D_W$，得

$$
\boxed{8\pi^2k-P(g)\le
4\Delta V-2\int\Psi(W^+_{\widehat g})
\le4\Delta V-\frac{20}{9}\int\operatorname{dist}(W^+_{\widehat g},\mathcal K)^2.}
\tag{3.9}
$$

因此 $P(g)\le8\pi^2ck$ 要求 $Y([g])^2\ge32\pi^2(A+(1-c)k)$，并支付额外的谱偏离项。经典混合估计已经给出“节省至多为四倍 Yamabe 体积超额”的首项；本式另外控制重特征值的分裂。两者可同时使用，不能把首项重新计为独立结果。其限制仍由 (3.2) 表达：尚无全局估计将 $D_W-\Delta V$ 压到匹配构造的最佳值。

### 3.6 靠近复双曲主体时的局部化

在 $\operatorname{Ric}_{g_0}=-6g_0$ 的紧复双曲商上，Bianchi 规范下的 Einstein 线性化为

$$
L=\tfrac12(\nabla^*\nabla-2\mathring R).
$$

Koiso 恒等式在无迹横截张量上给 $L\ge1$；规范与迹部分由 Hodge Laplacian 和标量 Laplacian 的非负性给 $L\ge6$。这不使用覆盖的第一特征值下界。若 $|d\phi|\le a<\sqrt2$，加权分部积分进一步给

$$
\|e^\phi L^{-1}e^{-\phi}\|_{2\to2}\le(1-a^2/2)^{-1}.
$$

设外部区域的常标量度量已处于该规范，且相对 $g_0$ 在一致局部 $C^{2,\gamma}$ 范数内充分接近。对离核心距离 $T$ 以外的区域，截断、加权逆估计和非线性余项吸收给

$$
\|g-g_0\|_{H^2(d\ge T)}
\le C\left(\|\operatorname{Ric}^{\circ}_g\|_{L^2(d\ge1)}+e^{-aT}\Lambda\right),
\qquad \Lambda=\|g-g_0\|_{H^1(1\le d\le2)}.
\tag{3.10}
$$

常数只依赖模型和接近程度。标量约束使主体体积的一阶变化成为界面通量，其余为 $O(\|g-g_0\|_{H^2}^2)$。将通量计入核心相对体积 $\Delta V_U$，(3.9) 因而给

$$
P(g)\ge\frac{8\pi^2k-4\Delta V_U-C\Lambda^2}{1+C}.
\tag{3.11}
$$

这说明在明确的近复双曲范围内，固定比例节省需要核心相对体积超额或界面误差承担相应规模。一般极小化序列是否具有这样的主体、规范和小邻域仍未建立；四维 $H^2$ 控制本身不能替代所需的 $C^{2,\gamma}$ 假设。

## 4. 光滑全局极小元与临界点

Q3 询问闭光滑流形上的全局 $P$ 极小值是否可由非 Bach-flat 光滑度量取得。两种明确候选为：Horikawa 单吹起和 Godeaux 单吹起，均具有

$$
16\pi^2/3\le P_*<8\pi^2.
$$

经典曲率下界已排除 Einstein 度量；若取得，则负 Yamabe 性、$P$-临界性和变分关系保证极小元非 Bach-flat。尚缺的是光滑取得性本身。

来源：[Four_Problems_Direct_Connections.tex](../archive/originals/2026-10-08/Four_Problems_Direct_Connections.tex) §4 的 Horikawa 例；[Q3_Global_Attainment.tex](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) §1 的 Fermat 商 Godeaux 例。两种候选具有各自的光滑拓扑。

### 4.1 谐和通量与下降方向

[03_Subsequent_Mathematical_Developments(1).tex](../archive/originals/2026-10-08/03_Subsequent_Mathematical_Developments.tex) §3 中，令 $B:\Lambda^+\to\Lambda^-$ 为混合曲率块，$a$ 为给定第一 Chern 类，$h$ 为单位 $L^2$ 范数的非零谐和反自对偶形式，$q=(a_g^-,h)_{L^2}>0$。定义

$$
p=P/(8\pi^2),\qquad\mathfrak F_h=\sqrt2\int|B^*h|,
\qquad\delta=1-\mathfrak F_h/(2\pi q),
\qquad L=(P/2-\mathfrak F_h^2)/(4\pi^2).
$$

则

$$
p=q^2(1-\delta)^2+L,\qquad L\ge0,
$$

其中 $L$ 明确分成混合曲率块的秩偏离和幅度方差。这个等式自身仍容许 $p=0,\delta=1,L=0$。

对真实度量变分有如下公式。在闭 almost-Kähler 结构 $(g,J,\Omega)$、Ricci 为 $J$-不变的类别，

$$
DP_g[\operatorname{Ric}^{\circ}]
=\frac18\int|ds|^2-\frac12\int s|\operatorname{Ric}^{\circ}|^2.
$$

常非零标量时，每个非 Einstein 度量均有保体积形式的下降方向。负标量下进一步的精确谐和秩对齐条件
$\operatorname{im}B_x\subset\mathbb Rh_x$
给出局部化下降，无须对零集上的商另加有界假设。因此负标量 Einstein–Maxwell 非 Einstein 度量也不可能成为 $P$-临界点。

来源：[Q3_Descent_and_Flux_Equality.tex](../archive/originals/2026-10-08/Q3_Descent_and_Flux_Equality.tex) §§2–3；[Q3_Harmonic_Alignment_Descent.tex](../archive/originals/2026-10-08/Q3_Harmonic_Alignment_Descent.tex) §§2–5；[Q3_Harmonic_Rank_Rigidity.tex](../archive/originals/2026-10-08/Q3_Harmonic_Rank_Rigidity.tex) §§1、4。完整点态方程允许两个幅度同时变化。

因此非 Einstein、负标量的光滑极小元若存在，对每个非零谐和反自对偶形式均有严格正的对齐余项；这一正数允许依赖度量。

### 4.2 次标准能量子水平集中的退化

[Q3_Global_Attainment.tex](../archive/originals/2026-10-08/Q3_Global_Attainment.tex) §§2–5 构造一个显式节点 Godeaux 退化，配合固定严格插入得到 $P<8\pi^2$ 的退化序列，其缩放核心为 Ricci-flat Eguchi–Hanson。因此次 $8\pi^2$ 子水平集可非紧。该构造未确定退化序列是否极小，光滑取得性仍为独立问题。

同稿的带标记整体分裂估计保留规范类在主体和各渐近局部欧氏（ALE）核心的分量；相对特征数项相加抵消后，某些核心被排除，但规范类在嵌入 $(-2)$-球上的限制可为零；Ricci-flat 核心具有非平凡二循环而 $P=0$。

### 4.3 非球面背景中的 ALE 核心与替换

[Scalar_Curvature_and_Global_Attainment_20261012.tex](../archive/originals/2026-10-12/Scalar_Curvature_and_Global_Attainment_20261012.tex) §§2–3：闭 aspherical 四维环境中，若嵌入紧域的边界连通且边界基本群有限，且该域有 $s\ge0$、严格向外平均凸度量，则包含映射零伦。由此对所列单端光滑 ALE 核心得 $\chi=1,\tau=0$ 及边界群限制；非平凡端群时

$$
P\ge4\pi^2+S/12,
$$

满足这些嵌入条件的 Ricci-flat ALE 核心只能平坦。Aspherical 指环境流形的万有覆盖可缩。

[AE_Bubble_Replacement_20261015.tex](../archive/originals/2026-10-15/AE_Bubble_Replacement_20261015.tex) §§2–3 处理平凡端群：对满足原稿微分衰减条件、$s\ge0,\chi=1,P<16\pi^2$ 的完备单端渐近欧氏（AE）流形，利用经典 Chang–Gursky–Yang 球定理证明紧核心为标准光滑球；若它作为完整核心以 $C^2$ 缩放收敛出现在 $P$ 极小化序列中，正能量可由平坦填充和小能量过渡严格降低，因此不可能保留这样的气泡。

替换定理以完整核心的光滑缩放收敛为输入。一般极小化序列的轨形、中间尺度、多端及塌缩分支仍待分析；边界为 $S^3/Q_8$ 的正能量核心属于非平凡端群分支。

[标量曲率与全局取得性](../archive/originals/2026-10-12/Scalar_Curvature_and_Global_Attainment_20261012.tex) §4 的双曲尖点加倍例说明另一个独立现象：可有闭 aspherical 流形上 $P_* =0$ 而不取得，曲率一致有界、退化来自塌缩环面颈。取得性因而同时涉及曲率集中和塌缩退化。

### 4.4 实双曲吹起：一个取决于 Yamabe 值的精确问题

设 $Y$ 为闭实双曲四维流形，$M_k=Y\#k\overline{\mathbb{CP}}^{,2}$，$Y_{\rm hyp}<0$ 为双曲共形类的 Yamabe 常数。其全度量恒等式为

$$
P(g)=8\pi^2k+4I_+(g)+\frac{S(g)-Y_{\rm hyp}^2}{12},
\qquad Y_{\rm hyp}^2=192\pi^2\chi(Y).
\tag{4.1}
$$

若另有 Yamabe 不变量等式 $\mathcal Y(M_k)=Y_{\rm hyp}$，则 $S\ge Y_{\rm hyp}^2$，故 $P\ge8\pi^2k$；Burns 恢复给相反不等式。若达到这个下界，同时达到负 Yamabe 不变量的度量必为 Einstein，与 $P>0$ 矛盾。因此

$$
P_*(M_k)=8\pi^2k\quad\text{且不取得}.
$$

同一恒等式和 §1.2 的圆柱上界给

$$
\alpha(M_k)=\min\left\{1,\frac{4k}{k+6\chi(Y)}\right\}.
\tag{4.2}
$$

$k<2\chi(Y)$ 时不取得；$k>2\chi(Y)$ 时 $\alpha=1$ 及不取得不需要上述 Yamabe 假设。临界 $k=2\chi(Y)$ 的取得要求常非零标量的相应半共形平坦度量。

式 (4.1) 是无条件恒等式，(4.2) 的非平凡小 $k$ 分支则依赖尚未证明的 Yamabe 值。对任意极小化序列只能由等式推得其趋于半共形平坦及 Yamabe 极值；把每份 $8\pi^2$ 分配给单个异常类仅在指定的 Burns 恢复序列中成立。

来源：[实双曲吹起与 Yamabe 问题](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md) §3。

## 5. 成对 $A_1$ 奇点轨形的精确极值

固定奇点类型后的变分问题有时可以完整求解，并由此排除一类光滑极小化极限。设 $X$ 为紧复双曲曲面，取复取向，

$$
A=c_1^2(X),\qquad\chi(X)=A/3,\qquad\tau(X)=A/9.
$$

令 $O=S^4/\mathbb Z_2$，其中对合在 $S^4\subset\mathbb R\times\mathbb C^2$ 上为 $(t,w)\mapsto(t,-w)$；它有两个 $A_1$ 点。在正规点作连通和，置

$$
V_m=X\#mO,\qquad k=2m>0.
$$

以下下确界取遍这一固定轨形上的全部光滑轨形度量。其精确值为

$$
\boxed{P_{*,\mathrm{orb}}(V_m)=8\pi^2k,qquad
\alpha_{\mathrm{orb}}(V_m)=\min\left\{1,\frac{4k}{A+k}\right\}.}
\tag{5.1}
$$

而每个单独度量都满足 $P(g)>8\pi^2k$，所以 $V_m$ 不承载 Einstein 轨形度量。

### 5.1 光滑解消与下界转移

两个奇点由复取向的 Eguchi–Hanson 空间解消后，$O$ 的光滑解消微分同胚于 $\overline{\mathbb{CP}}^{,2}\#\overline{\mathbb{CP}}^{,2}$。证明需要光滑拓扑：原有 $T^2$ 作用延拓过两个 $\mathcal O(-2)$ 核心；解消单连通，交形式为 $-I_2$，轨道空间是四边形圆盘。Orlik–Raymond 的光滑环面作用分类给出上述微分同胚。单独知道交形式不足以替代这一步。所用光滑分类见 Orlik–Raymond，[Actions of the torus on 4-manifolds I](https://www.ams.org/tran/1970-152-02/S0002-9947-1970-0268911-3/)，§§4–5。

因此 $V_m$ 解消为 $M_k=X\#k\overline{\mathbb{CP}}^{,2}$。对任意轨形度量，用缩小的 Eguchi–Hanson 核心解消，在其平坦端与轨形正规坐标间选取能量趋零的过渡环带，得到

$$
S(g_\epsilon)\to S(g),\qquad P(g_\epsilon)\to P(g),\qquad
\int(s^-_{g_\epsilon})^2\to\int(s^-_g)^2.
$$

经典一般型吹起曲面的 Yamabe 估计于是转移为 $\int(s^-)^2\ge32\pi^2A$。这里包含 $b^+=1$ 的情形；使用的是每个光滑度量上的曲率估计，不需要先构造轨形上的极限单极子。经典输入见 LeBrun，[Kodaira dimension and the Yamabe problem](https://doi.org/10.4310/cag.1999.v7.n1.a5)；混合曲率估计及极化类选择见 [Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory](https://doi.org/10.1007/s002220100148)。

该轨形的特征数为

$$
\chi_{\mathrm{orb}}=A/3-m,\qquad\tau_{\mathrm{orb}}=A/9.
$$

$A_1$ 链接的签名 eta 项为零。令 $\sigma=S-32\pi^2A\ge0$、$w=W-4\pi^2A/3=2I_-\ge0$，轨形 Chern–Weil 公式给出

$$
P=8\pi^2k+\sigma/12+2w,
\qquad R=8\pi^2(A+k)+\sigma/3+2w.
\tag{5.2}
$$

故 $\mathcal J$ 是 $4k/(A+k)$、$1$、$4$ 的加权平均，其权重依次为 $8\pi^2(A+k)$、$\sigma/3$、$2w$。这证明 (5.1) 的两个下界。

### 5.2 显式恢复序列

在 $\mathbb R^4\setminus\{0\}$ 上取

$$
h=(1+r^{-2})^2\delta.
$$

它标量平坦、共形平坦，且直接积分得

$$
P(h)=32\pi^2,\qquad
\int_{r>L}|\operatorname{Ric}^{\circ}_h|^2
=\frac{\pi^2(96L^2+32)}{(1+L^2)^3}.
$$

等距对合

$$
\iota(x)=\operatorname{diag}(-1,-1,-1,1)x/|x|^2
$$

交换两端，在 $\pm e_4$ 的微分均为 $-I$。商空间有两个 $A_1$ 点和一个普通 AE 端，成本恰为 $16\pi^2$。

在 $X$ 的 $m$ 个不同点插入尺度为 $\epsilon$ 的商空间，拼接半径取 $\rho=\sqrt\epsilon$。背景与欧氏度量的差为 $O(\rho^2)$，缩放端与欧氏度量的差为 $O(\epsilon^2\rho^{-2})$；连同两阶导数可知过渡曲率有界，过渡体积为 $O(\epsilon^2)$。被截去的端能量也为 $O((\epsilon/\rho)^4)=O(\epsilon^2)$。所以

$$
P\to8\pi^2k,\qquad S\to32\pi^2A,\qquad
W\to4\pi^2A/3,\qquad L_s\to0,
$$

从而 $\mathcal E\to4k/(A+k)$。与 §1.2 的长圆柱序列合并即得全部上界。

### 5.3 不取得性与光滑极小化序列的排除

若某度量达到 $P=8\pi^2k$，则 (5.2) 强迫 $\sigma=w=0$，并达到全度量的 $S$ 下界。对 $S$ 作共形变分得到 $\Delta s=0$；负标量预算使 $s$ 为非零常数。再作无迹变分，

$$
DS[H]=-2s\int\langle\operatorname{Ric}^{\circ},H\rangle=0
$$

强迫 $\operatorname{Ric}^{\circ}=0$，与 $P=8\pi^2k>0$ 矛盾。

令 $q=4k/(A+k)$、$B=8\pi^2(A+k)$，有

$$
\mathcal E-q=\frac{(1-q)\sigma/3+2(4-q)w+L_s}{R},
\qquad
\mathcal E-1=\frac{(q-1)B+6w+L_s}{R}.
$$

故 $k<A/3$ 和 $k>A/3$ 时 $\alpha_{\mathrm{orb}}$ 均不取得。在边界 $k=A/3$，取得等价于 $W^-=0$ 且标量为负常数；还必须有 $\sigma>0$。这一边界上的存在性没有由上述公式决定。

另一方面，光滑解消满足 (2.1) 的 $P_*(M_k)<8\pi^2k$。若其极小化序列在正规部 $C^2_{\rm loc}$ 收敛到 $V_m$ 上的光滑轨形度量，则非负性与下半连续性已给

$$
\liminf_iP(g_i)\ge P(V_m)>8\pi^2k>P_*(M_k),
$$

矛盾。这里不需要额外假设气泡能量恒等式。固定轨形的精确下界排除了这一极限形态，却不成为其全部光滑解消度量的下界；有限尺度构造恰能降低这一奇异极限的成本。

## 6. ALE 解消中的混合曲率转移

### 6.1 解消时相对缺陷的连续性

设紧轨形主体 $g$ 满足 $R(g)>0$，解消采用 Ricci-flat ALE 空间，端误差及其前两阶导数为 $O(r^{-\tau})$，$\tau>0$。插入尺度 $\epsilon$，拼接半径取 $\rho=\epsilon^{\tau/(\tau+2)}$。环带上的尺度化度量误差为 $O(\rho^2+(\epsilon/\rho)^\tau)=O(\rho^2)$，故 Ricci 曲率有界、环带体积为 $O(\rho^4)$；核心 Ricci 为零。因此

$$
(V,T_s,S,P,R,L_s)(g_\epsilon)\longrightarrow(V,T_s,S,P,R,L_s)(g),
\qquad\mathcal E(g_\epsilon)\to\mathcal E(g).
\tag{6.1}
$$

于是非零 Einstein 轨形的这种解消满足 $P_*=\alpha=0$，不必另外假设标量方差消失。若主体 Ricci-flat，则只能直接推出 $P_*=0$；上述简单截断族反而 $\mathcal E\to4$，因为标量仅支撑在体积趋零的过渡区，$T_s^2\le4\operatorname{Vol}(\operatorname{supp}s)R$。

若填充仅标量平坦，令 $Q=\sum_jP(N_j)$，同一计算给

$$
\mathcal E(g_\epsilon)\longrightarrow
\frac{4P(g)+L_s(g)+4Q}{R(g)+Q},\qquad R(g)+Q>0.
\tag{6.2}
$$

正能量核心将相对缺陷推向 $4$，而有限尺度 Burns 节省来自这个极限式未保留的相互作用。式 (6.1)–(6.2) 针对实际拼接族，并非任意退化序列的能量恒等式。另须注意，$P$ 在度数 $d$ 的有限覆盖下乘以 $d$，$\mathcal E$ 则保持不变。

### 6.2 同时保留标量与手性 Weyl 能量

设紧轨形 $V$ 的孤立奇点由有足够二阶渐近衰减的标量平坦 ALE 空间 $N_j$ 解消为 $M=X\#k\overline{\mathbb{CP}}^{,2}$，$A=c_1^2(X)>0$。取与 $M$ 一致的取向，令 $\Gamma_j$ 为端群，$\eta_{\Gamma_j}$ 使用定向签名公式的约定。定义

$$
a_\pm(N)=\frac2{|\Gamma|}-2\chi(N)\mp3\tau(N)\mp3\eta_\Gamma.
$$

非紧 Chern–Weil 公式为

$$
P(N)=4I_\pm(N)+S(N)/12+8\pi^2a_\pm(N).
\tag{6.3}
$$

若 $N$ Ricci-flat，则 $a_\pm\le0$；若还为复取向 Kähler，则

$$
a_+=0,\qquad a_-=-4\left(\chi(N)-|\Gamma|^{-1}\right).
\tag{6.4}
$$

对光滑解消度量使用经典混合估计，再令解消尺度趋零，得到

$$
\boxed{\int_V(s-\sqrt6|W^+|)^2
+6\sum_jI_+(N_j)\ge72\pi^2A.}
\tag{6.5}
$$

证明只需展开被积式：核心上 $s=0$，所以核心的贡献恰为 $6I_+$；过渡环带的总曲率平方积分趋零；主体上的积分收敛。每个光滑度量可选择自身所供给的实际类，整个转移不要求这些类收敛到某个预先指定的轨形类。对 Ricci-flat 解消，记 $A_\pm=\sum_ja_\pm(N_j)$，式 (6.5) 化为

$$
\int_V(s-\sqrt6|W^+|)^2\ge72\pi^2A+12\pi^2A_+.
$$

因此复取向 Ricci-flat Kähler 解消无损转移该不等式；反取向解消则有明确的手性代价。标量平坦但非 Ricci-flat 的核心还支付其正 $P$ 能量。

### 6.3 Einstein 主体的有限参数可行区

假设主体度量 Einstein。标量估计迫使其标量为负。设 $x=S(V)/(96\pi^2)$。特征数加法给

$$
T_+^{\rm orb}=A-k+A_+,
\qquad T_-^{\rm orb}=4c_2(X)-A+5k+A_-.
$$

由标量预算、$I_\pm\ge0$ 和 (6.5)，

$$
\frac A3\le x\le\min(T_+^{\rm orb},T_-^{\rm orb}),\qquad
\left(\sqrt{8x}+\sqrt{T_+^{\rm orb}-x}\right)^2\ge6A+A_+.
\tag{6.6}
$$

左侧是关于 $x$ 的凹函数，最大值在 $x=8T_+^{\rm orb}/9$；在允许区间上取这个点或最近端点，即可精确决定这些数值条件是否相容。还有不含渐近余项的必要条件

$$
\boxed{9A_-+2A_++42k+12(3c_2(X)-A)\ge0.}
\tag{6.7}
$$

其证明是恒等式

$$
9x+3T-\left(\sqrt{8x}+\sqrt{T-x}\right)^2
=2\left(\sqrt{T-x}-\sqrt{2x}\right)^2\ge0,
$$

再使用 $x\le T_-^{\rm orb}$。它比只保留标量预算更强，且保留主体偏离复双曲的 $3c_2-A$ 项。

对复双曲背景及全部复取向 Ricci-flat Kähler 核心，$A_+=0$。式 (6.6) 强迫 $k\le A/3$，并给

$$
x_{\min}=\frac A{27}\left(4-\sqrt{1-3k/A}\right)^2,
\qquad
\sum_j\left(\chi(N_j)-\frac1{|\Gamma_j|}\right)
\le\frac{A/3+5k-x_{\min}}4.
\tag{6.8}
$$

若这些核心全部为 Kronheimer 空间、承载总秩 $k-k_b$，令 $y=\sqrt{1-3k/A}$，则

$$
\sum_j\left(1-\frac1{|\Gamma_j|}\right)
\le k_b+\beta(k,A),\qquad
\beta(k,A)=\frac{k(5y+1)}{18(1+y)}<\frac k6.
\tag{6.9}
$$

$k_b$ 仅表示没有被这些核心吸收的秩，不能据此把每个剩余异常类分配到某个几何区域。有限 $A$ 的严格修正为 $\beta/k=1/6-k/(12A)+O((k/A)^2)$；只保留 $k/6$ 会漏掉临界配置的排除。

### 6.4 对角交形式中的完整根系

当 $X$ aspherical 时，吹下映射 $M\to X$ 将每个嵌入球面送到零同伦类，因而其同调类落在异常对角格 $-\mathbb Z^k$。一个 $(-2)$-球必为 $\pm E_i\pm E_j$，即 $D_k$ 根。因此，嵌入的 ADE 配置需要作为根系嵌入 $D_k$；仅匹配行列式远远不够。

这一限制可直接分类。将根的两个非零坐标连成带符号边；对每个连通坐标分量作坐标变号，使一棵生成树全为差根。其反射生成坐标置换。若没有和根，所生成根系为 $A_{v-1}$；若存在和根，则为 $D_v$。因此 $E_6,E_7,E_8$ 不能作为这种根系嵌入任意对角格。若全部异常秩由根配置吸收，只有

$$
D_{a_1}\oplus\cdots\oplus D_{a_q},\qquad a_i\ge2,\quad\sum a_i=k,
$$

其中 $D_2=A_1\oplus A_1$、$D_3=A_3$。该子格在对应对角格中的指数为 $2^q$，通常不是本原子格。

将 (6.9) 用于这些实际 Kronheimer 核心，其边界成本为

$$
c(D_2)=1,\qquad c(D_3)=3/4,\qquad
c(D_a)=1-\frac1{4(a-2)}\quad(a\ge4).
$$

总成本必须不超过 $\beta(k,A)$。秩至多五的每个分量成本均大于其秩的六分之一，故完整吸收需要至少一个 $D_a$ 分量满足 $a\ge6$，特别有 $k\ge6$。$k=6$ 时唯一通过根型限制的候选是 $D_6$；其成本为 $15/16$，精确解 (6.9) 得

$$
A\ge\frac{3675}{64}.
$$

复双曲曲面的 $A\in9\mathbb Z$，第一个数值允许值因而是 $A=63$。这些是拓扑与能量的必要条件；仍须有实际嵌入、正确边界识别以及负 Einstein 主体。通过数值条件没有构造这些对象。

## 7. 完备有限体积 Einstein 域与塌缩补域

ALE 轨形解消不是所有退化的统一模型。完备有限体积 Einstein 域可能留下塌缩或尖点补域；这些区域的可见曲率量由边界特征数决定。

### 7.1 边界恒等式与极限电荷

对带边界紧域 $D$ 定义

$$
\mathscr C_\pm(g;D)=\frac1{2\pi^2}\int_D|W^\pm|^2
+\frac1{96\pi^2}\int_Ds^2,\qquad
\widehat P(g;D)=\frac{P(g;D)}{8\pi^2}.
$$

将 Euler 边界项记为 $\mathscr E$，签名 eta 项及 transgression 之和记为 $\mathscr H$，采用

$$
\chi(D)=\int_De+\mathscr E,\qquad
\int_DL=\tau(D)+\mathscr H.
$$

则

$$
\widehat P=\mathscr C_\pm-(2\chi\pm3\tau)(D)+\mathscr Q_\pm(\partial D),
\quad \mathscr Q_\pm=2\mathscr E\mp3\mathscr H.
\tag{7.1}
$$

共同边界的两侧取向相反，边界项随之反号。

设 $M=X\#k\overline{\mathbb{CP}}^{,2}$ 上一列度量具有下列实际极限：

- 在开集 $\Omega$ 上，经微分同胚后 $C^2_{\rm loc}$ 收敛到完备有限体积、标量常数 $s_\infty<0$ 的 Einstein 度量；
- $P(g_i)\to0$、$L_s(g_i)\to0$、$\bar s_i\to s_\infty$，且总体积收敛到 $\operatorname{Vol}(\Omega,g_\infty)$；
- $\Omega_\rho\uparrow\Omega$ 是嵌套紧穷竭，其补域各连通分支 $C_j^{(\rho)}$ 的拓扑和所接端的集合固定。

则各补域有非负极限电荷

$$
q_j=\lim_{\rho\to0}\lim_{i\to\infty}\mathscr C_+(g_i;C_j^{(\rho)})\ge0,
$$

满足

$$
q_j=(2\chi+3\tau)(C_j)
+\lim_{\rho\to0}\sum_{L\text{ 接于 }C_j}\mathscr Q_+(L;g_\infty),
\qquad
\mathscr C_+(g_\infty;\Omega)=A-k-\sum_jq_j.
\tag{7.2}
$$

这里链接取 $\partial\Omega_\rho$ 的取向。多端补域给出的是边界项之和的极限；单独各端的极限还需其渐近结构。

证明在每个固定 $\rho$ 上使用 (7.1)、局部收敛和 $P(C_j)\to0$，再由非负密度和嵌套性取得外层极限。标量部分消失的关键为

$$
\int_{C_j}s_i^2\le2L_s(g_i)+2\bar s_i^2\operatorname{Vol}(C_j,g_i).
$$

无体积损失使全部补域体积的上极限不超过 Einstein 域的尾部体积，后者随 $\rho\to0$ 趋零。因此补域的 Weyl 极限为 $\int_{C_j}|W^+|^2\to2\pi^2q_j$，但并不要求该能量为零。

### 7.2 全局混合不等式限制补域

若全部光滑度量满足 LeBrun 混合曲率下界，则

$$
\boxed{9k+8\sum_jq_j\le3A.}
\tag{7.3}
$$

在主体上写 $x=S/(96\pi^2)$、$y=I_+/(2\pi^2)$，有

$$
\int_\Omega(s-\sqrt6|W^+|)^2
\le12\pi^2(\sqrt{8x}+\sqrt y)^2
\le108\pi^2(x+y).
$$

而 $x+y=A-k-\sum q_j$。补域的标量平方积分趋零，但其混合积分趋于 $12\pi^2q_j$。相加便得

$$
72\pi^2A\le108\pi^2(A-k-\sum q_j)+12\pi^2\sum q_j,
$$

即 (7.3)。所以正电荷补域必须集中正手性 Weyl 能量，不能把它等同于曲率有界的纯体积塌缩。

### 7.3 圆纤维尖点的拓扑代价

若端部满足 Dai–Wei 的圆纤维尖点渐近，链接作为 $\partial\overline\Omega$ 的 Euler 数为 $e$，其边界公式为

$$
\mathscr Q_+^\infty=-e+3\operatorname{sign}e,\qquad
\mathscr Q_-^\infty=e-3\operatorname{sign}e.
$$

所用渐近条件及绝热 eta 公式见 Dai–Wei，[Hitchin–Thorpe inequality for noncompact Einstein 4-manifolds](https://web.math.ucsb.edu/~dai/paper/dwAIM.pdf)，Theorems 3.5、5.1。

对作为补域边界的 $e_{\rm out}=-e$，

$$
q_+=(2\chi+3\tau)(C)+e_{\rm out}-3\operatorname{sign}e_{\rm out}.
\tag{7.4}
$$

设 $\partial C=S^3$、$b_1=b_3=b_2^+=0$、$b_2^-=r\ge1$。则 $2\chi+3\tau=2-r$，两种 Hopf 取向分别给 $q_+=4-r$ 和 $q_+=-r$。非负性排除后一取向，并强迫可行补域最多携带四个异常秩。

若全部异常拓扑分布在 $N$ 个这样的补域中，$\sum r_j=k$，另有 $B$ 个电荷为四的球补域，则 (7.3) 等价于

$$
\boxed{k+32N+32B\le3A.}
\tag{7.5}
$$

特别地，每个异常类各占一个补域时，$k\le A/11$。若四个类成组、$N=k/4$ 且 $B=0$，只恢复 $k\le A/3$，没有排除这一形态。四秩补域的 $q_+=0$，但反取向公式给 $q_-=20$，即

$$
\int_C|W^-|^2\longrightarrow40\pi^2.
$$

它对混合正手性预算不可见，却仍具有固定全曲率。相符的拓扑组合是秩四 $D_4$ ALF 核心与穿孔 $\mathbb{RP}^2$ 二维实向量丛，其同调包含指数二扩张 $-D_4\subset-I_4$；相对光滑识别及匹配的低能量过渡尚未构造。

这些结论以本节明确的 Einstein 域收敛和无体积损失为前提。一般极小化序列尚未自动产生这些条件。紧复双曲基本群不含 $\mathbb Z^2$，只能排除尖点链接群的某些单射；若链接到主体的映射有核，就不能据此排除尖点或塌缩。

## 8. 极值与取得性分别还需要什么

上述结果决定了固定成对 $A_1$ 轨形的两个极值，建立了一般型吹起曲面的严格次标准上界，并排除了若干可能的光滑极小化极限。它们也给出全部竞争度量必须满足的共形关系、近极小变分关系及实际场结构。

| 变分问题 | 已有结论 | 尚未决定的内容 |
|---|---|---|
| 原平衡手术族 | 严格次四构造、有限参数归一化、覆盖与安放条件 | 匹配的全度量下界及最佳首项 |
| 一般型纯吹起曲面 | $P_*<8\pi^2k$；共形 Kähler 分离；联合 $(\kappa,\upsilon)$ 可行区 | $P_*$ 的精确值和小 $k/A$ 时的真实尺度 |
| 非 Bach-flat 光滑极小元 | 明确正能量候选、下降方向、退化例和部分气泡替换 | 至少一个符合全部条件的光滑取得实例 |
| 固定成对 $A_1$ 轨形 | 精确下确界及除临界壁外的不取得性 | $k=A/3$ 壁上的常负标量自对偶度量是否存在 |
| Ricci-flat ALE 解消的 Einstein 主体 | 标量、混合曲率和根格的有限参数必要条件 | 相容的实际嵌入、Einstein 主体与完整拼接 |
| 有限体积 Einstein 域 | 非负补域电荷、$9k+8\sum q_j\le3A$、Hopf 拓扑代价 | 一般序列的结构提取及未排除补域的几何实现 |

不存在精确 Einstein 度量、$P_*>0$、$\alpha>0$ 和极小值能否光滑取得是不同断言。Ricci-flat 核心可有非零二阶拓扑而不支付 $P$；塌缩也可使下确界不取得。因此，构造越过标准局部费用以后，决定全局最优值的关键在于实际竞争几何如何同时实现主体、核心、边界配对与规范场，而不在于继续把标准核心费用独立相加。

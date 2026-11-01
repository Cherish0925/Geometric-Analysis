# 积分 Einstein 间隙、端点与双取向应用

下文陈述本项目研究稿中的积分障碍、端点估计及双取向应用，并列出各命题的输入和证明依赖。N1、I40、I41、I51、O10、O11 是项目原稿的编号；经典非消失定理与本项目的分析命题分别标注来源。

## 1. 共同对象与实际输入

设 $M$ 为闭、连通、定向光滑四流形，$g$ 为光滑黎曼度量。记 $\chi(M)$ 为 Euler 示性数，$\tau(M)$ 为签名，$s_g$ 为标量曲率，$\operatorname{Ric}^{\circ}_g=\operatorname{Ric}_g-s_gg/4$，$V_g=\operatorname{Vol}_g(M)$。省略测度的积分均相对于 $dV_g$，$x_+=\max\{x,0\}$，$\fint f=V_g^{-1}\int_M f\,dV_g$。定义

$$
T_+=2\chi(M)+3\tau(M),\quad
P(g)=\int_M|\operatorname{Ric}^{\circ}_g|^2,\quad
R(g)=\int_M|\operatorname{Ric}_g|^2,
$$

$$
\mathcal J(g)=\frac{4P(g)}{R(g)},\qquad
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|^2}
{\lambda^2\operatorname{Vol}_g(M)}.
$$

$W^+$、$W^-$ 分别为自对偶和反自对偶 Weyl 曲率，采用其在二形式空间上作用的 Hilbert–Schmidt 范数；Ricci 使用二张量范数。下文所有曲率常数均采用这一约定。

假设共形类 $[g]$ 的 Yamabe 常数为负。令 $\widehat g\in[g]$ 为 $s_{\widehat g}=-4$ 的常标量代表，$V=V_{\widehat g}$。要求某个 Spin$^c$ 结构在 $\widehat g$ 上有未扰动 Seiberg–Witten 解；若 $\mathcal A$ 是其行列式线丛 $L$ 的酉联络、$\Phi$ 是正旋量，则采用原稿规范

$$
D_{\mathcal A}\Phi=0,\qquad F_{\mathcal A}^+=2i\sigma(\Phi).
$$

其中 $D_{\mathcal A}$ 是 Dirac 算子，$\sigma$ 是原稿固定归一化的旋量二次映射。记 $a=c_1(L)$，$a_g^+$ 为其自对偶调和投影，并假设

$$
p=(a_g^+)^2=(a_{\widehat g}^+)^2\ge A>0.
$$

此处 $A$ 是正实数下界，与联络 $\mathcal A$ 区别。逐度量命题只使用该共形类的上述输入；要得到对 $M$ 全部光滑度量成立的结论，须逐共形类满足这些条件，并使用同一个 $A$。不同共形类可选择不同 Spin$^c$ 结构。

若一个结构的未扰动方程在整个共形类均可解，且 $p>0$，则 SW–Weitzenböck 恒等式排除该类中的非负常标量代表。普通单极子类、Kotschick 的 special monopole 类、Bauer–Furuta（BF）及 Pin$^{-}(2)$ 非消失定理分别提供可解性条件。Pin$^{-}(2)$ 分支将底空间度量和扭曲解提升到双覆盖上的普通 SW 系统；积分与类平方均乘以覆盖次数，$\mathcal J$、$\mathcal E$ 和 $T_+/A$ 不变。该论证仅对底空间度量的提升使用覆盖上的方程。

在 $R>0$ 时有 $\mathcal E\ge\mathcal J$。Ricci 平坦度量满足 $R=0$，故 $\mathcal J$ 不定义，而上述 $\mathcal E$ 定义给出 $4$。全度量应用中的正投影下界另给 $\int s_-^2\ge32\pi^2A>0$，其中 $s_-=\max\{-s,0\}$，由此排除 Ricci 平坦度量。

入口：[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§1、4；较早版本为 [Qiushi_Line1_Unified_Gap_20260928.md](../archive/originals/2026-09-28/Qiushi_Line1_Unified_Gap_20260928.md)。后续继承稿 §5 另证明了类平方短缺版本，见下文。

## 2. 原积分障碍、N1 与 I40/I41 的连续关系

### 2.1 单解参数估计推出 N1

对 $\beta\ge2$ 定义参数泛函

$$
D_\beta=(1+\beta^{-1})\int s^2
 +6(\beta+1)\int|W^+|^2-72\pi^2p.
$$

在上述单解输入及 $a^2\ge T_+$ 下，I51 有限参数估计给出

$$
\frac{P(\widehat g)}V+\frac{D_\beta(\widehat g)}{\beta V}
\ge c_0\frac{(\beta-2)^2}{\beta^4}.
$$

将 $\beta=8$ 代入并使用 Chern–Weil 恒等式，得到

$$
D_8=108\pi^2(T_+-2p/3)+\frac{27}{2}P.
$$

由 $\int s^2\ge32\pi^2p$ 和下列共形比较，继承稿推出

$$
\boxed{\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+
\ge\varepsilon_N>0.}
\tag{N1}
$$

这里 $c_0>0$ 为 I51 的普适常数，可取 $\varepsilon_N=\min\{1,c_0/768\}$。

对上述负 Yamabe 代表，记

$$
\Delta S=\int_gs_g^2-\int_{\widehat g}s_{\widehat g}^2\ge0,
$$

则 $P(g)=P(\widehat g)+\Delta S/12$、$R(g)=R(\widehat g)+\Delta S/3$，故 $\mathcal J(g)$ 是 $\mathcal J(\widehat g)$ 与 $1$ 的加权平均，特别

$$
\mathcal J(g)\ge\min\{\mathcal J(\widehat g),1\}.
$$

$\mathcal E\ge\mathcal J$ 随即恢复旧的

$$
\mathcal E(g)+\left(\frac{T_+}{A}-\frac23\right)_+\ge\varepsilon_N.
$$

N1 因而蕴含原 $\mathcal E$ 障碍。对四类经典应用，先由相应非消失定理验证可解性、$p\ge A>0$ 与类平方条件，再代入 N1；非消失定理不是 N1 的结论。

### 2.2 类平方短缺版本

[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §5 使用 I51 中含 $(-a^2)_+/V$ 的估计，允许 $a^2<T_+$。令

$$
y=\frac{(T_+-a^2)_+}{A}.
$$

得到

$$
\boxed{\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+
\ge\frac{c}{1+y}.}
\tag{N1-Y}
$$

该命题要求负 Yamabe 代表上有上述同一实际解且 $p\ge A>0$。对任意固定 $L_0\ge0$，条件 $y\le L_0$ 给出统一下界 $c/(1+L_0)$；原稿未确定最优的 $y$ 依赖，也未得到与无界 $y$ 无关的正常数。

### 2.3 I40/I41 的强制估计与线性下界

置

$$
\Sigma=\int s^2-32\pi^2p,\quad
\Pi=P+D_2,\quad Y=(T_+-a^2)_+.
$$

原稿的强制估计为

$$
\Sigma\le C\{\Pi+\sqrt{\Pi Y}\},\qquad
(p-T_+)_+\le C_T\{\Pi+\sqrt{\Pi Y}\}.
\tag{I41}
$$

证明使用相容背景作用的消去、有界截面的协变 Hessian 估计、联络能量与同场弱 Bianchi 恒等式。$Y=0$ 时 $\Sigma\le C\Pi$；因此对任意尺度 $Q_j>0$，若 $\Sigma_j\ge c_1Q_j$，则 $\Pi_j\ge(c_1/C)Q_j$。

令 $T_-=2\chi-3\tau$、$h=1-T_+/A$、$U=3\min(T_+,T_-)/A$。在 $p\ge A>0$、$a^2\ge T_+$ 和 $0<h\le1/3$ 下，结合另一手性的 Chern–Weil 关系，得到

$$
\mathcal J+(U-1-h)_+\ge ch.
$$

对 $U_j=1+h_j+O(h_j^2)$、$h_j\downarrow0$ 的原平衡族，这给出 $\inf_g\mathcal J(g)\ge c_2h_j$。允许类平方短缺时，右侧相应变为 $ch^2/(h+y)$。N1 研究 $T_+/A=2/3$ 附近的分离；这条线性结论研究 $T_+/A=1-h$ 且双手性约束接近等号的范围。

原稿定位：[00_Line1_Research_Atlas_20260928.md](../archive/originals/2026-09-28/00_Line1_Research_Atlas_20260928.md) §§1、3.1–3.4；[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§2–6；[Yau26_Line1_External_Review_20260927.md](../archive/originals/2026-09-27/Yau26_Line1_External_Review_20260927.md)；旧卷定位见上述继承稿末节。

## 3. O10：从有限参数到任意固定有限密度

O10 研究下列参数缺陷；其中 $V_g=\operatorname{Vol}_g(M)$：

$$
\kappa_\beta(g)=\fint_M|\operatorname{Ric}_g+g|^2
 +\frac{D_\beta(g)}{V_g}.
$$

它不同于前节有限参数估计的 $P/V+D_\beta/(\beta V)$。在 $s=-4$ 代表上，第一项才化为 $P/V$。

### 3.1 现有有限密度结论

[O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md) §§1–4 的命题为：在原逐共形类的单极子解存在性条件、$p\ge A>0$、$a^2\ge T_+$ 下，任意固定有限 $B$ 存在 $c_{\rm FD}(B)>0$，使

$$
\boxed{\frac{\chi(M)}A\le B\quad\Longrightarrow\quad
\kappa_\beta(g)\ge c_{\rm FD}(B)
\frac{(\beta-2)^2}{\beta^2},\qquad\beta\ge2.}
\tag{FD}
$$

该结论不另加点态 Ricci、直径、非塌缩、注入半径或统一 Sobolev 控制。[O10_Finite_Density_Complete_Proof.tex](../archive/originals/2026-09-29/O10_Finite_Density_Complete_Proof.tex) 汇集主证明与直接前置，适合沿完整依赖阅读。

### 3.2 有限密度证明的依赖

**实际正旋量的强收敛估计。** [O10_Strong_Current_Prerequisite.md](../archive/originals/2026-09-29/O10_Strong_Current_Prerequisite.md) 证明：沿假想端点序列，$|\nabla\Phi|^4$ 对归一化体积测度一致可积；三次扭率 $\mathfrak t\in S^-\otimes L$ 及其 Dirac 残差、曲率拟合和类型投影因而具有原稿所列强收敛。这里 $S^-$ 是负旋量丛，$\mathfrak t$ 对应源稿的扭率记号 $\tau$，与签名 $\tau(M)$ 区别。此步不使用 Euler 密度上界。

**同丛有界辅助截面。** [O10_Direct_Resolvent_Prerequisite.md](../archive/originals/2026-09-29/O10_Direct_Resolvent_Prerequisite.md) 取光滑有界径向截断 $\mathcal T$，在包含极限模长的区间恒等，并解

$$
(4+\nabla^*\nabla)v=6\mathcal T(\mathfrak t)
$$

得到 $|v|+|\nabla^*\nabla v|\le C$、$v-\mathfrak t\to0$ 于 $H^1(dV/V)$，以及 $(\nabla^*\nabla-2)v\to0$ 于 $L^2(dV/V)$。辅助截面 $v$ 仅由该线性方程定义。

**有限密度导数估计。** $b=\fint|W^-|^2\le C_B$ 给 $\|\nabla v\|_4+\|\nabla^2v\|_2\le C_B$。模长、相位与 Dirac 方程的约化只留下一个复导数分量；协方差测试给 $q=|\nabla v|^2\to2m_*$ 于测度，$m_*=128/81$。见 [O10_Weak_Bianchi.md](../archive/originals/2026-09-29/O10_Weak_Bianchi.md)。这条直接证明避免了早期 Nijenhuis 括号的伴随测试，保留早期 [O10_Resolvent_Prolongation.md](../archive/originals/2026-09-29/O10_Resolvent_Prolongation.md) 作为另一条推导记录。

**第五幂线丛。** 构造

$$
\sigma=\Phi\wedge t(v)\in\Gamma(L^5),\qquad
|\sigma|^2\to4\rho_*m_*^3>0,\quad\rho_*=4/3.
$$

其中 $t(v)$ 为源稿定义的一阶三次旋量表达式，$|\Phi|^2\to\rho_*$、$|v|^2\to m_*$；并有 $\fint|\nabla\sigma|^2\le C_B$。线丛次数来自 $t(v)\in S^+\otimes L^4$ 和 $\det S^+=L$。

**全局矛盾。** 线丛的对数预解算子正则化与 Chern–Weil 转移公式给

$$
c_1(L^5)^2[M]/V\to0,
$$

而同一实际场的曲率估计给

$$
c_1(L^5)^2[M]/V=25a^2[M]/V\to25/(6\pi^2)>0.
$$

线丛引理及更一般闭二形式配对见 [O10_Topological_Escape.md](../archive/originals/2026-09-29/O10_Topological_Escape.md)；实际应用见 [O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md) §§2–3。

另一证明保留相位项，取得 $L^5$ 上的弱 Cauchy–Riemann 型方程，并以正算子 $\nabla^*\nabla+10/3$ 的预解方程作对偶测试，见 [O10_Finite_Density_Fifth_Line.md](../archive/originals/2026-09-29/O10_Finite_Density_Fifth_Line.md)。两条证明使用相同的实际场强收敛前置。

有限参数估计排除有界 $\beta$ 的反例子列；原稿共形比较

$$
\widehat\kappa_\beta\le
\frac{\kappa_\beta}{1-\sqrt{\kappa_\beta}-\kappa_\beta/16}
$$

将小缺陷反例转到 $s=-4$ 代表，从而接回全部原允许度量。

### 3.3 密度范围与常数依赖

| 原稿阶段 | 获得内容 | 后续使用 |
|---|---|---|
| [O10_Critical_Density.md](../archive/originals/2026-09-29/O10_Critical_Density.md) | $\chi/A<3/8$ 的较短端点论证 | 该范围现包含于 FD |
| [O10_Strengthened_Endpoint.md](../archive/originals/2026-09-29/O10_Strengthened_Endpoint.md) | 谱超额、$39/4$ 临界密度及正宽度 | 该范围现包含于 FD |
| [O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md) | 每个固定有限 $B$ 的 FD | 对每个有限 $B$ 的端点估计 |
| [O10_Quantitative_Escape_and_O11_Boundary.md](../archive/originals/2026-09-29/O10_Quantitative_Escape_and_O11_Boundary.md) | 增长能量的对数陈数约束及指数型密度依赖 | 保留独立引理与速率推导 |
| [O10_Primitive_Rate_Audit.md](../archive/originals/2026-09-29/O10_Primitive_Rate_Audit.md) | 原始缺陷与实际误差之间的幂次转接，结合第五线丛正势排除给多项式依赖 | 依赖强流估计及第五线丛排除 |

最后一稿令 $x=\kappa_\beta+\beta^{-2}$。设 $0<\epsilon_0\le1$ 为慢梯度截断中的固定指数，$\gamma=\epsilon_0/(1+\epsilon_0)$。以 $\mathfrak e_D$ 表示该稿所列实际场误差之和，包括辅助截面与扭率的 $H^1$、$L^4$ 差，则

$$
\mathfrak e_D\le Cx^{\gamma/16}.
$$

结合 [O10_Alternative_Global.md](../archive/originals/2026-09-29/O10_Alternative_Global.md) 的

$$
\mathfrak e_D(1+b)^{3/2}\to0\quad\Longrightarrow\quad
\text{不存在该端点序列},
$$

得到 $x\ge c(1+b)^{-24/\gamma}$，进而得到某个普适有限指数 $N$ 的

$$
c_{\rm FD}(B)\ge c_0(1+B)^{-N}.
$$

此结论依赖慢梯度估计和上述第五线丛排除；$x$ 是原始曲率缺陷，$\mathfrak e_D$ 是其导出的场误差，二者通过显示的幂次估计联系。

## 4. 地理条件下的统一端点

[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §2（亦见 [04_Uniform_Endpoints_and_Tower_Recovery.tex](../archive/originals/2026-10-07/04_Uniform_Endpoints_and_Tower_Recovery.tex)）证明以下分区推论。

若原允许对象构成的族满足

$$
Q:=A-T_+\ge0,\qquad \chi(M)\le CA+Q,
$$

其中 $C<\infty$ 固定，则

$$
\kappa_\beta\ge c_{\rm geo}(C)\frac{(\beta-2)^2}{\beta^2},\quad
c_{\rm geo}(C)=\min\{\varepsilon_N,c_{\rm FD}(C+1/3)\}>0.
\tag{GEO}
$$

证明分区：$Q/A\ge1/3$ 时 N1 直接给正间隙；$Q/A<1/3$ 时只需固定密度 $C+1/3$ 的 FD。该结论允许族内 $\chi/A$ 无界，统一常数依赖固定的地理常数 $C$。

对满足所列单极子可解性条件的光滑极小复一般型曲面 $X$，$A=c_1^2(X)>0$，Noether 估计给 $\chi(X)\le35A$。因此

$$
M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),\quad
Q=k+4\ell,\quad \chi(M)\le35A+Q
$$

有与主体、手术数、度量、参数无关的常数

$$
c_* =\min\{\varepsilon_N,c_{\rm FD}(106/3)\}.
$$

对于 $r$ 个正平方极小复一般型曲面的连通和，令 $A=\sum_{i=1}^r c_1^2(X_i)$、$Q=k+4\ell+4(r-1)$。若相应普通或 BF 理论提供 $p\ge A$、$a^2=A-k$ 的实际类，则同一估计成立。其可解性范围由相应连通和非消失定理决定；上述 Noether 估计使用复一般型及各 $c_1^2(X_i)>0$。

原平衡族满足 $\chi/A\le1/3+h$，故 FD 已给出其统一端点估计。GEO 进一步允许所列手术数无界；一般 O10 不包含 GEO 的地理假设。

## 5. 无密度 O10：低幅度估计与集中问题

一般目标仍是原全部实际输入下，存在不依赖 $\chi/A$ 的绝对 $c>0$。FD、速率排除和 GEO 没有共同覆盖所有允许对象。

### 5.1 不依赖反手性 Weyl 上界的估计

[O10_Unbounded_Density.md](../archive/originals/2026-09-29/O10_Unbounded_Density.md) 与 [O10_Double_Weighted_Test.md](../archive/originals/2026-09-29/O10_Double_Weighted_Test.md) 处理原正旋量低幅度区、容量和合法带权测试。[O10_Low_Amplitude_Energy_and_O11_Scope.md](../archive/originals/2026-09-29/O10_Low_Amplitude_Energy_and_O11_Scope.md) 证明以下估计。令 $d\mu_j=dV_j/V_j$、$\mathscr L_j=\nabla_j^*\nabla_j$；假设 $|v_j|+|\mathscr L_jv_j|\le C$、$m_j=|v_j|^2\to m_*$ 于 $L^2(d\mu_j)$、$(\mathscr L_j-2)v_j\to0$ 于 $L^2(d\mu_j)$。另假设区域 $G_j$ 上的一个正交复类型投影 $\mathsf P_j$ 满足 $\int_{G_j}|\mathsf P_j\nabla v_j|^2d\mu_j\to0$，且 $\int_{M_j\setminus G_j}|\nabla v_j|^2d\mu_j\to0$。记 $q_j=|\nabla v_j|^2$，则对固定 $0<\theta<1$、$\varepsilon>0$ 有

$$
\limsup_j\fint\frac{q_j}{(m_j+\varepsilon)^\theta}
\le\frac{2m_*}{(1-\theta)(m_*+\varepsilon)^\theta},
$$

$$
\limsup_j\fint_{\{m_j\le t\}}q_j
\le2\mathrm e\,t\log(m_*/t),\qquad0<t<m_*/\mathrm e.
$$

这里 $\mathrm e=\exp(1)$。因此 $\lim_{t\downarrow0}\limsup_j\fint_{\{m_j\le t\}}q_j=0$。估计不要求 $\fint|W^-|^2$ 有统一上界；极限次序为先固定 $\theta,\varepsilon$，再令 $j\to\infty$。

### 5.2 中间幅度集中

上述估计仍容许固定中间幅度层 $0<u_0<m_j<u_1<m_*$ 在体积趋零时保留非零径向能量。无密度证明所需的两个结论——第五线丛截面经固定截断后的正 $L^2$ 质量，以及该截面满足相应弱曲率方程——尚未同时得到。

[O10_Alternative_Global.md](../archive/originals/2026-09-29/O10_Alternative_Global.md) §8 保留完整径向项后给出

$$
\mathfrak b=d\,\theta_1+c\,\theta_2,\qquad
d=-\frac{m_3+i m_4}{2m},
$$

这里 $\mathfrak b$ 是局部旋量联络的非对角一形式，$\theta_1=e^1-ie^2$、$\theta_2=e^3-ie^4$ 来自适配正交余标架，$m_i=e_i(m)$，$c,d$ 为复系数。正手性非对角曲率中的径向项精确相消。标量矩恒等式与定义在 $[0,m_*]$ 上的形式能量测度 $d\nu_q=2dt$、$d\nu_R=4t\,dt$ 相容；这些测度也满足逆幅度矩估计。尚无使这些形式测度由完整闭流形场方程实现的构造。

[O10_Local_Model_And_Prolongation_Audit.md](../archive/originals/2026-09-29/O10_Local_Model_And_Prolongation_Audit.md) 指出：由 Armstrong 的局部结果，不存在同时满足 $\operatorname{Ric}=-g$、$W^+=0$、$d\omega=0$、$|\omega|^2=2$ 的几乎 Kähler 局部解，其中取向由 $\omega$ 决定。源稿在缩小双曲球上构造的实际 SW 解并不提供常模长闭相容形式，因而属于另一类局部对象；其闭流形延拓仍需验证全部过渡条件。

开放问题是证明完整径向、相位和曲率方程排除上述集中，或构造满足全部原假设的闭流形端点序列。FD 的量词为 $\forall B<\infty\ \exists c(B)>0$；一般 O10 要求 $\exists c>0$ 对全部允许对象成立。

## 6. 双取向、Kodaira 斜率与后续配对推广

### 6.1 固定密度前置 FD2

[Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md)（2026-10-07）与 [06_Two_Orientation_Global_Gap.tex](../archive/originals/2026-10-07/06_Two_Orientation_Global_Gap.tex) 调用 FD 在固定 $B=2$ 的特例，记为 **FD2**。其同一实际类 $c$ 必须满足

$$
(c^+)^2\ge A_c>0,\quad c^2\ge T_+,\quad\chi/A_c\le2.
$$

双取向推论以 FD2 为假设；FD2 的强流、辅助截面和线丛证明见 §3。

### 6.2 全曲面丛范畴的间隙

对光滑定向曲面丛 $\Sigma_f\to M\xrightarrow{\pi}\Sigma_b$，$f,b\ge2$，原稿在 FD2 前置下证明

$$
\boxed{\mathcal J(g)+\left(1-\frac{3|\tau(M)|}{\chi(M)}\right)_+
\ge\varepsilon_{\rm SB},\qquad
\varepsilon_{\rm SB}=\left(\frac{\min\{1,c_{\rm FD}(2)\}}{200}\right)^2.}
\tag{SB}
$$

该常数独立于基底和纤维的亏格、丛的单值表示、总空间以及度量。

取总空间取向使 $\tau\ge0$，并记 $e=\chi(M)$。令 $e(E)$ 表示定向实平面丛 $E$ 的 Euler 类。取 $x=e(\pi^*T\Sigma_b)$、$y=e(T_{\rm vert}M)$，则

$$
x^2=0,\quad xy=e,\quad y^2=3\tau,
\quad a=x+y,\quad b=x-y,
$$

$$
a^2=2e+3\tau,\quad b^2[M]=-2e+3\tau,\quad ab=-3\tau.
$$

Thurston 的辛构造与 Taubes 的非消失定理提供这些类。原稿在 $0<d<1/256$ 的分支验证反取向的正交叉形式指数 $b_2^+>1$；其中 $d=\mathcal J(\widehat g)+(1-3\tau/e)_+$。以 $\bar\kappa_\beta$ 表示 $\widehat g$ 上使用类 $b$ 和反取向 $\bar M$ 定义的参数缺陷。同一 Hodge 分解中的交叉配对给出

$$
A_-=e(2-3\tau/e)>0,\quad e/A_-<2,\quad
\bar\kappa_{d^{-1/2}}<100\sqrt d.
$$

FD2 给同一量至少为 $\min\{1,c_{\rm FD}(2)\}/2$。$d\ge1/256$ 时 SB 直接成立；$d=0$ 时原稿给出对每个有限 $\beta\ge2$ 均成立的 $\bar\kappa_\beta\le16/\beta$，与 FD2 矛盾。因此三种情形均得到 SB。

Einstein 情形给 $3|\tau|\le(1-\varepsilon_{\rm SB})\chi$。对具有经典负 KE 度量的光滑 Kodaira 纤维化，$c_1^2=2\chi+3\tau$、$c_2=\chi$，得到

$$
\boxed{c_1^2/c_2\le3-\varepsilon_{\rm SB}.}
$$

此命题在 FD2 前提下给出统一斜率上界 $3-\varepsilon_{\rm SB}$；最优上确界未在该稿中确定。经典背景及问题出处在原稿末节：Kotschick `math/9911255`、LeBrun `math/0005195`、Catanese–Rollenske `math/0611428`；[00_All_Recent_Research.tex](../archive/originals/2026-10-07/00_All_Recent_Research.tex) 的相关章另列 Catanese `1611.06617` §1.3 与 Polizzi `2002.01363` Remark 4.10。

### 6.3 10 月 8 日一般双取向配对定理

[00_Results_and_Proof.md](../archive/originals/2026-10-08/00_Results_and_Proof.md) §1 与 [Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) 将 SB 推广到一般闭四流形。令 $e=\chi>0$，选取 $\tau\ge0$。设 $\mathcal C_+$ 是正取向有限组全度量单极子类，

$$
a\in\operatorname{Hull}(\mathcal C_+),\quad a^2\ge T_+;
$$

反取向有实际单极子类 $b$，满足 $b^2[\bar M]\ge T_-=2e-3\tau$。记 $t=3\tau/e$、$z=|ab|/e$。在 FD2 前置下，

$$
\boxed{\mathcal J(g)+(1-t)_++(t-z)_+\ge\varepsilon_{\rm pair},}
$$

其中 $\varepsilon_{\rm pair}=\varepsilon_{\rm SB}$。正取向一侧仅通过凸性使用标量曲率估计，不需凸组合本身有 SW 解；FD2 始终作用于实际反取向类 $b$。

若反取向类也取自有限集合，可在满足平方条件的配对中最大化 $|ab|/e$。对于辛形式对诱导的定向平面丛分裂 $TM=E_1\oplus E_2$，若其两个典范类满足上述可解性条件，原稿将配对短缺项控制为

$$
\frac{2}{e}\bigl(\min\{e(E_1)^2,e(E_2)^2\}\bigr)_+.
$$

该推广的输入是双取向可解性及混合交叉积。应用于具体吹起流形时，须另行验证这些输入。

## 7. 原稿索引与问题范围

| 阅读目的 | 原始文件及定位 |
|---|---|
| 原 gap、N1、单解与短缺继承 | [03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§1–6；[00_Line1_Research_Atlas_20260928.md](../archive/originals/2026-09-28/00_Line1_Research_Atlas_20260928.md) §3 |
| I40/I41 与旧卷来源 | [Yau26_Line1_External_Review_20260927.md](../archive/originals/2026-09-27/Yau26_Line1_External_Review_20260927.md)；上述 Atlas 及继承稿的精确卷、Source、节号 |
| 强流前置 | [01_O10_Strong_Current.md](../archive/originals/2026-09-29/01_O10_Strong_Current.md)；[O10_Strong_Current_Prerequisite.md](../archive/originals/2026-09-29/O10_Strong_Current_Prerequisite.md) |
| 同丛预解算子的有界截面 | [O10_Direct_Resolvent_Prerequisite.md](../archive/originals/2026-09-29/O10_Direct_Resolvent_Prerequisite.md) |
| 质量、相位、Dirac 与第五幂截面 | [O10_Weak_Bianchi.md](../archive/originals/2026-09-29/O10_Weak_Bianchi.md)；历史第一延拓 [O10_Resolvent_Prolongation.md](../archive/originals/2026-09-29/O10_Resolvent_Prolongation.md) |
| 有限密度主证明及附录 | [O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md)；[O10_Finite_Density_Complete_Proof.tex](../archive/originals/2026-09-29/O10_Finite_Density_Complete_Proof.tex) |
| 第五线正势路线 | [O10_Finite_Density_Fifth_Line.md](../archive/originals/2026-09-29/O10_Finite_Density_Fifth_Line.md)；[O10_Alternative_Global.md](../archive/originals/2026-09-29/O10_Alternative_Global.md) |
| 对数陈数与原误差速率 | [O10_Topological_Escape.md](../archive/originals/2026-09-29/O10_Topological_Escape.md)；[O10_Quantitative_Escape_and_O11_Boundary.md](../archive/originals/2026-09-29/O10_Quantitative_Escape_and_O11_Boundary.md)；[O10_Primitive_Rate_Audit.md](../archive/originals/2026-09-29/O10_Primitive_Rate_Audit.md) |
| 无密度集中与有效更正 | [O10_Unbounded_Density.md](../archive/originals/2026-09-29/O10_Unbounded_Density.md)；[O10_Double_Weighted_Test.md](../archive/originals/2026-09-29/O10_Double_Weighted_Test.md)；[O10_Low_Amplitude_Energy_and_O11_Scope.md](../archive/originals/2026-09-29/O10_Low_Amplitude_Energy_and_O11_Scope.md)；[O10_Local_Model_And_Prolongation_Audit.md](../archive/originals/2026-09-29/O10_Local_Model_And_Prolongation_Audit.md) |
| 地理分区与统一手术族 | [Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §2；[04_Uniform_Endpoints_and_Tower_Recovery.tex](../archive/originals/2026-10-07/04_Uniform_Endpoints_and_Tower_Recovery.tex) |
| 双取向与 Kodaira | [Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md)；[06_Two_Orientation_Global_Gap.tex](../archive/originals/2026-10-07/06_Two_Orientation_Global_Gap.tex) |
| 一侧凸包、配对短缺及辛形式对推广 | [00_Results_and_Proof.md](../archive/originals/2026-10-08/00_Results_and_Proof.md) §1；[Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) |
| 连续汇编入口 | [00_Collected_Research.tex](../archive/originals/2026-10-07/00_Collected_Research.tex)；[00_All_Recent_Research.tex](../archive/originals/2026-10-07/00_All_Recent_Research.tex) 及其同名版本 |

N1 与 I40/I41 使用单解参数分析；FD 另使用端点的强流及线丛分析；GEO 由 N1 和 FD 分区推出；SB 及一般配对定理由 FD2 与双取向交叉关系推出。各命题的条件和输出不同。

BF 应用族的完整凸包估计需要控制全部单极子类；已知符号类的优化与普通手术族的计算分别针对所列类集合。O11 的后续构造已在其所列族上将标准系数 $4$ 严格降低，所余问题是实际最优首项及匹配下界。一般无密度 O10 与精确 Einstein 存在性仍各有独立假设和待证结论。

服务器中的连续解析工程见[Codex主稿与原始证明](../research/server/codex/README.md)。后续[实际Taub–NUT载体与第五线投影](../research/server/sessions/S1003A01/README.md)给出局部场、尾部和平均预算的具体模型，尚未把它们接成一般无密度O10的闭反例或统一估计。两项公开问题的数学证明与文献比较见[10月31日记录](../research/server/codex/project/continuation/20261031_Kodaira_Fino_Literature_and_Proof_Status.md)。

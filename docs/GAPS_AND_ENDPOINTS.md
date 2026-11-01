# 积分 Einstein 间隙、端点与双取向应用

整体交叉形式限制曲率积分；一个实际规范场还把曲率与同一度量下的协变导数联系起来。以下先建立共同的归一化和相容性估计，再推导临界间隙、线性强制、有限密度端点及双取向应用。N1、I40/I41、FD 等标签沿用证明原稿的编号。

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

### 1.1 缺陷泛函与精确共形比较

写 $S=\int s^2$、$I=\int s$、$W_\pm=\int|W^\pm|^2$。四维 Chern–Weil 恒等式为

$$
R=P+S/4,\qquad
4\pi^2T_\pm=S/24+2W_\pm-P/2,
\qquad T_\pm=2\chi\pm3\tau.
\tag{1}
$$

对 $R>0$，将 $1/\lambda$ 配方得到

$$
\mathcal E=4-\frac{I^2}{V_gR}
=\mathcal J+\frac{S-I^2/V_g}{R}\ge\mathcal J.
\tag{2}
$$

$I=0$ 时此式仍给下确界，但有限 $\lambda$ 不取得它。Ricci-flat 度量满足 $R=0$，此时 $\mathcal J$ 不定义而 $\mathcal E=4$。在全度量正预算应用中，实际单极子估计另给 $\int s_-^2\ge32\pi^2A>0$，从而排除 Ricci-flat；这里 $s_-=\max\{-s,0\}$。

对 $g=u^2\widehat g$，取非负 Laplace 算子 $\Delta=d^*d$。标量变换式 $s_gu^3=6\Delta_{\widehat g}u-4u$ 给

$$
\delta:=S(g)-S(\widehat g)
=48\int_{\widehat g}u^{-2}|du|^2
 +36\int_{\widehat g}(u^{-1}\Delta u)^2\ge0.
\tag{3}
$$

Weyl 能量共形不变，故

$$
P(g)=P(\widehat g)+\delta/12,\qquad
R(g)=R(\widehat g)+\delta/3,
$$
$$
\mathcal J(g)=
\frac{R(\widehat g)\mathcal J(\widehat g)+\delta/3}
 {R(\widehat g)+\delta/3}.
\tag{4}
$$

因此 $\mathcal J(g)$ 是 $\mathcal J(\widehat g)$ 与 $1$ 的加权平均；若 $\mathcal J(g)<1$，则

$$
\mathcal E(\widehat g)=\mathcal J(\widehat g)
\le\mathcal J(g)\le\mathcal E(g).
\tag{5}
$$

这还决定负 Yamabe 共形类内的下确界：$\inf_{g\in[g_0]}\mathcal J(g)=\min\{\mathcal J(\widehat g),1\}$。当 $\mathcal J(\widehat g)>1$，取局部支撑的正共形因子 $u_n=1+\epsilon\chi\sin(nx^1)$，固定小 $\epsilon>0$，式 (3) 中的 Laplace 平方项趋于无穷；式 (4) 遂趋于 $1$，而有限 $\delta$ 不取得该值。若 $\mathcal J(\widehat g)<1$，极小值恰由常数缩放的 Yamabe 代表取得；等于 $1$ 时整个共形类均有 $\mathcal J=1$。

对在 Yamabe 替换下封闭、且每个共形类均为负的竞争度量集合，只要 $\inf\mathcal J<1$，便有

$$
\inf_g\mathcal E(g)=\inf_g\mathcal J(g).
\tag{6}
$$

证明只需对 $\mathcal J$ 的极小化序列逐项使用 (5)，再结合 $\mathcal J\le\mathcal E$。标量方差因而不构成低缺陷极值问题中的独立代价；这不涉及极小值的光滑取得性。

证明来源：[共形分离与线性强制](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/continuation/20260927_conformal_separation_and_zero_end.md) Part I §§1、3；[单解继承](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§1、4。

### 1.2 点态近 Einstein 输入的共形归约

共形比较还保留一个不使用规范场的定量结论。若闭四维度量满足
$$
\delta_-(g):=\|g^{-1}\operatorname{Ric}_g+I\|_{\infty,\mathrm{op}}
\le\epsilon\le\tfrac14,
$$
则唯一的 $s_{\widehat g}=-4$ 代表 $\widehat g=u^2g$ 满足
$$
1-\epsilon\le u^2\le1+\epsilon,\qquad
\|du\|_\infty\le4\epsilon,
$$
$$
\int_g\bigl((u-1)^2+|du|^2+|\nabla^2u|^2\bigr)
\le\tfrac38\int_g(s_g+4)^2\le6\epsilon^2V_g,
$$
$$
\int_{\widehat g}|\operatorname{Ric}_{\widehat g}+\widehat g|^2
\le P(g)\le4\epsilon^2V_g.
$$
右侧的导数和测度属于输入 $g$；最后一式左侧属于 $\widehat g$。这些常数不依赖直径、注入半径或标量谱隙。

令 $e=s_g+4$、$v=u-1$，标量方程写成
$$
6\Delta_gv+4u(u+1)v=-eu.
$$
最大值原理先控制 $u$；与 $v$ 配对、再用积分 Bochner 式，分别控制 $v,dv,\nabla^2v$。为得到最大梯度界，将方程改写为
$$
(\Delta_g+4/3)v=F,\qquad \|F\|_\infty\le2\epsilon.
$$
在 $\operatorname{Ric}\ge-Kg$ 下，热半群给
$$
\|\nabla(\Delta_g+m)^{-1}f\|_\infty
\le\left(\frac{\sqrt K}{m}+\sqrt{\frac{\pi}{2m}}\right)\|f\|_\infty.
$$
取 $K=5/4,m=4/3$ 即得所述常数。曲率积分界则由 $P(\widehat g)\le P(g)$ 和 $s_{\widehat g}=-4$ 得出。

该归约不能保持点态 Ricci 小量。固定双曲曲面乘积 $(\Sigma_1\times\Sigma_2,h_1+h_2)$，在第一因子的等温坐标圆盘取截断函数 $\chi$，令
$$
v_L=-\frac{\log L}{2L}\chi(x,y)\,xy
\log(x^2+y^2+e^{-2L}),\qquad
g_L=e^{2v_L}h_1+h_2.
$$
直接微分给
$$
\|v_L\|_{C^1}+\|\Delta_{h_1}v_L\|_\infty
=O((\log L)/L),\qquad
\nabla^2v_L(0)=(\log L)(dx\otimes dy+dy\otimes dx).
$$
二维 Ricci 仅由 Gaussian 曲率决定，故 $\delta_-(g_L)=O((\log L)/L)\to0$。对实际 Yamabe 因子作代换 $u_L=e^{-v_L/3}w_L$，标量方程中的 $\Delta v_L$ 精确消去；固定曲面上的隐函数定理给 $w_L\to1$ 于 $C^{2,\alpha}$。四维共形 Ricci 公式遂给
$$
\liminf_{L\to\infty}
\frac{\delta_-(u_L^2g_L)}{\log L}\ge\tfrac23.
$$
输入仍具有统一截面曲率界、直径上界、正注入半径和标量谱隙。因而从积分结论返回点态问题时，不能把 Yamabe 替换当作保持 $L^\infty$ Ricci 残差的操作。

完整估计和反例见[负 Yamabe 归约](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/mathematics/current/line1_yamabe_endpoint.md)。

### 1.3 标量方差需要全局连通信息

对原度量的标量方差，实际规范预算也不能替代全局控制。固定 $M=\Sigma_g\times\Sigma_h$，在第一因子沿分离测地线取长度 $\ell\to0$ 的双曲度量，得到精确负 Einstein 乘积 $g_\ell$。在长领口两侧把度量分别乘以不同常数 $c_-^2,c_+^2$，并在固定长度的中央领口光滑过渡，记所得度量为 $\widetilde g_\ell$。过渡区体积为 $O(\ell)$，其曲率及任意固定阶导数有统一界；适当选择过渡后，标量曲率保持在固定负区间。

同一个实际典范类 $a$ 在这族上满足 $p=a^2=T_+=A$。令
$$
B_\ell=S(\widetilde g_\ell)-32\pi^2A,\qquad
D=\frac1{4\pi^2}\left(\frac S{24}+\frac{W_+}{2}\right)-\frac p2.
$$
共形变换及 Chern–Weil 精确给出
$$
B_\ell=O(\ell),\qquad D(\widetilde g_\ell)=\frac{B_\ell}{96\pi^2},
\qquad P(\widetilde g_\ell)=\frac{B_\ell}{12}\to0.
$$
记两侧未缩放体积为 $V_-,V_+>0$，并置
$$
H_0=V_-+V_+,\quad H_2=V_-c_-^2+V_+c_+^2,\quad
H_4=V_-c_-^4+V_+c_+^4.
$$
由于过渡体积趋零，
$$
S-I^2/V\longrightarrow16\left(H_0-\frac{H_2^2}{H_4}\right)>0,
\qquad
\mathcal E(\widetilde g_\ell)\longrightarrow
4\left(1-\frac{H_2^2}{H_0H_4}\right)>0.
$$
例如 $V_-=V_+$、$c_-=1,c_+=\sqrt2$ 时，最后极限为 $2/5$。该族的标量谱隙趋零：两侧不同的标量尺度通过越来越细的领口相接。它证明原度量上的小规范缺陷、小 $P$ 和固定负标量区间不能强迫 $\mathcal E\to0$。逐共形类取 Yamabe 代表仍给 §1.1 的正确极值归约。

构造、实际类和精确能量式见[共形长颈与标量方差](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/mathematics/current/line1_conformal_neck.md) §§2–6。

## 2. 从经典预算到同场微分相容性

### 2.1 经典估计的归一化后果

在经典单极子或共形可解性条件下，曲率估计给出

$$
S\ge32\pi^2p,\qquad
\sqrt S+\sqrt{6W_+}\ge6\sqrt2\,\pi\sqrt p.
$$

加权 Cauchy–Schwarz 因而对每个 $\beta>0$ 给

$$
D_\beta=(1+\beta^{-1})S+6(\beta+1)W_+-72\pi^2p\ge0.
\tag{7}
$$

代入 (1)，

$$
D_\beta=(\beta+1)
\left[\frac{8-\beta}{8\beta}S+\frac32P+12\pi^2T_+\right]
 -72\pi^2p.
\tag{8}
$$

若 $t=T_+/A\in(0,2/3)$，取 $\beta+1=6/t$，则 $\beta>8$。由 $p\ge A$，式 (8) 中的拓扑项非正，所以

$$
\frac PS\ge\frac{\beta-8}{12\beta},\qquad
\boxed{\mathcal J\ge\frac{2-3t}{2-t}.}
\tag{9}
$$

$T_+\le0$ 时由 (1) 直接有 $P\ge S/12$，从而 $\mathcal J\ge1$。这些是经典预算的代数推论。式 (9) 在 $t=2/3$ 退化为零；排除每个度量取得等号，并不能排除一列退化度量趋近等号。

证明及经典原始文献见[经典曲率界与定量间隙](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/supplements/20261004_classical_and_quantitative_gaps.tex) §§1–3。

### 2.2 有界二形式：与规范供给分离的分析命题

设 $\psi$ 是闭四流形上的光滑自对偶二形式，$\|\psi\|_\infty\le K$。令

$$
q=|\psi|^2,\qquad
A_\psi=\frac q{24}I-\frac18\psi\otimes\psi,
$$
$$
d=\fint\bigl(|\operatorname{Ric}+g|^2+|W^+-A_\psi|^2+(q-2)^2\bigr),
\qquad B=\fint|\Delta_H\psi|^2.
$$

有界二形式定理给出

$$
\boxed{(1+B)d\ge c(K)>0.}
\tag{10}
$$

这里 $\Delta_H$ 是非负 Hodge Laplacian。定理只要求上述有界性和源项预算；它排除的是指定 Ricci、Weyl 与二形式模长的共同逼近。

其证明包含两个互相作用的估计。首先，度量丛截面 $u$ 满足协变插值
$\|\nabla u\|_4^2\le4\|u\|_\infty\|\nabla^2u\|_2$。先交换 Hessian 两槽、再积分分部得到

$$
\begin{aligned}
\int|\nabla^2u|^2={}&\int|\operatorname{tr}\nabla^2u|^2
-\int\operatorname{Ric}_{ij}\langle\nabla_i u,\nabla_j u\rangle\\
&+\sum_{ij}\int\langle F_{ij}\nabla_j u,\nabla_i u\rangle
+\frac12\sum_{ij}\int|F_{ij}u|^2.
\end{aligned}
\tag{11}
$$

$F$ 为丛联络曲率。式中没有曲率导数。对 $\Lambda^+$ 联络，$F$ 只涉及 $W^+$、标量曲率和无迹 Ricci；$W^-$ 不作用于此丛。由 (11) 和 Hodge–Weitzenböck 公式，若 $d\le1$，则

$$
\fint\bigl(|\nabla^2\psi|^2+|\nabla\psi|^4
+|\nabla^2A_\psi|^2+|\Delta q|^2\bigr)
\le C_K(1+B+d),
$$
$$
\fint|dq|^2\le C_K\sqrt{d(1+B+d)}.
\tag{12}
$$

其次，令 $J_\psi=\operatorname{div}W(A_\psi)$，其中 $W(A_\psi)$ 是对应的代数 Weyl 四张量。弱 Bianchi 恒等式在同一 $J_\psi$ 上测试给

$$
\fint|J_\psi|^2\le C_K\sqrt{d(1+B+d)}.
\tag{13}
$$

另一方面，对 $q\psi$ 作 Hodge 测试并完整收缩 $\nabla A_\psi$，得到

$$
\begin{aligned}
\int|J_\psi|^2=\int\Bigl(&-\frac{s q^2}{192}-\frac{q^3}{384}
+\frac{q\langle(W^+-A_\psi)\psi,\psi\rangle}{32}
+\frac{q|d\psi|^2}{16}-\frac{5|dq|^2}{384}\\
&+\frac{\langle\iota_{\nabla q}\psi,*d\psi\rangle}{16}\Bigr).
\end{aligned}
\tag{14}
$$

$s=-4,q=2,W^+=A_\psi$ 时代数项等于 $1/16$；交叉项由正的 $q|d\psi|^2$ 与 (12) 控制。因此 $\fint|J_\psi|^2\ge1/16-C_K\sqrt{d(1+B+d)}$，与 (13) 合并即得 (10)。全式对 $\psi$ 为多项式，跨零点无需除以模长。

证明见[有界自对偶二形式定理](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/mathematics/current/round21_analytic.md) §§1–3。将该定理用于新几何对象时，需实际提供有界二形式及 Hodge 源项预算；单有上同调类不提供这些条件。

### 2.3 同一单解的精确校准与有限参数估计

在 $s=-4$ 的代表上，取第 1 节规范的一个实际解，置

$$
\rho=|\Phi|^2\in[0,2],\quad
\psi=2\sqrt2\sigma(\Phi),\quad
\zeta=\langle\Phi,\nabla_{\mathcal A}\Phi\rangle,
\quad J_F=\|F_{\mathcal A}^+-(F_{\mathcal A}^+)_H\|_2^2.
$$

对 $\beta\ge2$，定义

$$
c_\beta=\frac{4(\beta+1)}{3\beta},\quad
C_\beta(\rho)=\rho+\frac{c_\beta}{2}
 -\frac{(\rho+c_\beta)^2}{2c_\beta(\beta+1)},
$$
$$
W_0=\frac{9\beta}{8(\beta+1)^2}
\left(\frac{\rho^2}{3}I-\psi\otimes\psi\right).
$$

旋量、Hodge 与 Hopf 恒等式给出四项分解

$$
\boxed{\frac{D_\beta}{18}
=J_F+\frac4{c_\beta}\int|\zeta|^2
+\frac{\beta+1}{3}\int|W^+-W_0|^2
+\frac1{c_\beta}\int C_\beta(\rho)(\rho-c_\beta)^2.}
\tag{15}
$$

由于 $C_\beta(0)=2/3$ 且 $C_\beta'>0$ 于 $[0,2]$，各项非负。它同时控制模长、完整 Weyl 拟合、非调和曲率和 Maxwell 残差：若 $H_{\mathcal A}$ 是同一曲率类的调和代表，则

$$
\|F_{\mathcal A}-H_{\mathcal A}\|_2^2=2J_F\le D_\beta/9,
\qquad \|\delta F_{\mathcal A}\|_2^2\le D_\beta/9.
\tag{16}
$$

第一式利用恰当二形式的两手性能量相等。式 (16) 是 Hodge 图范数控制；由它取得完整协变导数控制还需处理 $W^-$ 的作用。

令 $r=P/V$、$b_a=(-a^2)_+/V$。对 (15) 选定的同一场进行 Hessian 与弱 Bianchi 测试，得到有限参数估计

$$
\boxed{(1+b_a)\left(r+\frac{D_\beta}{\beta V}\right)
\ge c_{\rm raw}\frac{(\beta-2)^2}{\beta^4}.}
\tag{17}
$$

其参数依赖来自如下计算。置 $t=1/\beta$、$d_\beta=D_\beta/V$、$\omega=\sqrt2\psi/c_\beta$，则
$W_0=t(|\omega|^2I/3-\omega\otimes\omega)$。若 $J_t=\operatorname{div}W(W_0)$、$X=\fint|J_t|^2$，同场测试给

$$
X\le Ct\sqrt{(r+td_\beta)(1+r+d_\beta+b_a)}.
$$

Hodge 收缩的主项为 $(16/3)t^2(1-2t)$；其余项由 (15) 控制为
$Ct^2(\sqrt{d_\beta}+d_\beta+\sqrt{td_\beta})$。比较上下界，并分别处理 $r,d_\beta\le1$ 与其补集，即得 (17)。$a^2\ge T_+$ 时，Chern–Weil 给 $b_a\le r/(8\pi^2)$；分别处理小、大 $r$，可将右侧常数减为普适 $c_0>0$ 并去掉成本因子。

证明见[常权单解的校准与参数估计](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/continuation/20260927_constant_weight_and_global_fit.md) §§2–2.3。将类的存在来源与这个分析步骤分开，使普通、极化、BF 和实际 Pin$^{-}(2)$ 输入能够使用同一估计。

### 2.4 临界比例的统一分离

令 $d=(T_+/A-2/3)_+$。$\beta=8$ 将参数组合与拓扑组合精确对齐：

$$
D_8=108\pi^2(T_+-2p/3)+\frac{27}{2}P.
\tag{18}
$$

$s=-4$ 与标量预算给 $A/V\le1/(2\pi^2)$，故

$$
r+\frac{D_8}{8V}\le\frac{43}{16}r+\frac{27}{4}d.
$$

在 $a^2\ge T_+$ 下，式 (17) 去成本后给左端至少为
$c_8=9c_0/1024$。若原度量 $\mathcal J(g)<1$，式 (4) 及
$\mathcal J(\widehat g)=4r/(r+4)$ 给 $r\le4\mathcal J(g)/3$；于是

$$
c_8\le\frac{43}{12}\mathcal J(g)+\frac{27}{4}d
\le\frac{27}{4}(\mathcal J(g)+d).
$$

$\mathcal J(g)\ge1$ 分支直接成立。因此

$$
\boxed{\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+
\ge\varepsilon_N,\qquad
\varepsilon_N=\min\{1,c_0/768\}.}
\tag{N1}
$$

该式把经典预算退化的临界比例推进为统一正分离。在
$(T_+/A-2/3)_+<\varepsilon_N$ 的范围内，它给出正的无迹 Ricci 下界
$\varepsilon_N-(T_+/A-2/3)_+$。

例如 $M=X\#k\overline{\mathbb{CP}}^{\,2}$，$X$ 为提供所需实际类的一般型极小复曲面，$A=c_1^2(X)>0$，则

$$
\mathcal J(g)+\left(\frac13-\frac kA\right)_+\ge\varepsilon_N.
$$

所以 $k/A>1/3-\varepsilon_N$ 排除非零 Einstein 度量；正标量预算另排除 Ricci-flat。对高次光滑超曲面 $X_d\subset\mathbb{CP}^3$，$A_d=d(d-4)^2\to\infty$，取 $k_d=\lceil A_d/3\rceil-1$，便在经典三分之一阈值以下得到实际的额外排除区间。

完整推导见[单解临界间隙](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§2–4。

### 2.5 类平方成本的两种定量形式

不要求 $a^2\ge T_+$，保留 (17) 在 $\beta=8$ 时的常数 $c_{8,\mathrm{raw}}>0$。设

$$
\nu=\frac{(-a^2)_+}{A},\qquad
 y=\frac{(T_+-a^2)_+}{A}.
$$

由 $b_a\le\nu/(2\pi^2)$ 和上一节同一上界，立即有

$$
\boxed{\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+
\ge\frac{c_*}{1+\nu/(2\pi^2)},\qquad
c_*=\min\{1,4c_{8,\mathrm{raw}}/27\}.}
\tag{N1-\nu}
$$

因此 $a^2\ge0$ 已足以使这条临界间隙不损失常数，包括 $0\le a^2<T_+$ 的情形。

若要以相对于 $T_+$ 的短缺表示，则 (1) 给

$$
\frac{(-T_+)_+}{V}\le\frac r{8\pi^2},\qquad
b_a\le\frac r{8\pi^2}+\frac y{2\pi^2}.
$$

在 $\mathcal J(g)<1$ 分支，$r<4/3$，故

$$
\left(1+\frac1{6\pi^2}+\frac y{2\pi^2}\right)
\left[\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+\right]
\ge\frac{4c_{8,\mathrm{raw}}}{27}.
$$

缩小常数并包含 $\mathcal J(g)\ge1$ 分支，得到

$$
\boxed{\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+
\ge\frac{c}{1+y}.}
\tag{N1-Y}
$$

两个形式控制不同的量：$\nu$ 直接记录行列式曲率预算的负类平方成本，$y$ 便于与线性强制中的拓扑短缺比较。若逐共形类有 $y\le L$，则
$\mathcal J\ge c/(1+L)-(T_+/A-2/3)_+$；只有右端为正时才能排除 Einstein 度量。最优短缺依赖未由这些估计确定。

依据为[单解继承](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §5 的保留成本式；$\nu$ 形式由同一成本式直接推出。

### 2.6 标量超额的线性强制

I40/I41 的校准背景论证也能由 §2.3 的同一个常权解驱动。因此本节及其下能量边界只需第 1 节的负 Yamabe 单解输入。

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

以下给出单解接入的关键等式。先在 $s=-4$ 代表上取 (15) 的 $\beta=2$，此时

$$
\frac{D_2}{18}=J_F+2\int|\zeta|^2+\int|W^+-W_0|^2
+\frac12\int C_2(\rho)(\rho-2)^2,
\qquad C_2(\rho)\ge\frac23.
$$

作常数重标 $\Psi=(2/\sqrt6)^{1/2}\Phi$，置
$\eta=|\Psi|^2$、$\eta_0=4/\sqrt6$、$U_0=-4+\sqrt6\eta$、
$K=\int|\nabla_{\mathcal A}\Psi|^2$。联络和曲率模型保持不变，方程为
$4\nabla^*\nabla\Psi+U_0\Psi=0$。上述分解控制
$\int(|\eta-\eta_0|^2+|U_0|^2+|d\eta|^2+|\operatorname{Im}\langle\Psi,\nabla\Psi\rangle|^2+|W^+-W_0|^2)+J_F\le CD_2$。

以固定低模长截断乘 $\Psi$ 测试方程，得到
$\int_{\{\eta\le1\}}|\nabla\Psi|^2\le CD_2$。积分旋量方程和调和投影又给

$$
4K-4\int\eta+\sqrt6\int\eta^2=0,\qquad
6\int\eta^2=32\pi^2p+8J_F,
$$
$$
\boxed{\Sigma=8\sqrt6K+\int|U_0|^2+8J_F.}
$$

这使同一解具备校准背景论证需要的全部误差控制。Kähler–Einstein 曲率模型作用于校准旋量时精确消失；行列式负手性曲率满足
$\|F_{\mathcal A}^-\|_2^2=4\pi^2(p-a^2)+J_F\le\sqrt6K+C\Pi+4\pi^2Y$。
式 (11) 因而给

$$
\|\nabla^2\Psi\|_2^2+\|\nabla\Psi\|_4^4
\le C(K+\Pi+Y).
$$

同场弱 Bianchi 测试与低模长控制随后给

$$
K\le C\Pi+C\sqrt{\Pi(K+\Pi+Y)}
\le C'\bigl(\Pi+\sqrt{\Pi Y}\bigr).
$$

末步吸收 $\sqrt{\Pi K}$，并由精确超额式控制 $\Sigma$。它避免以背景体积 $V$ 代替 $K$ 而丢失线性阶。该论证用于 $\Pi/V\le1$；补集直接由 $0\le\Sigma\le16V<16\Pi$ 处理。负 Yamabe 代表上的估计经 (3) 转回原度量：

$$
\Sigma=\widehat\Sigma+\delta,\qquad
\Pi=\widehat\Pi+\frac{19}{12}\delta.
$$

再用精确关系

$$
36\pi^2(p-T_+)=\frac92P+\frac98\Sigma-D_2
$$

便同时取得 (I41) 的两个结论。$Y=0$ 时 $\Sigma\le C\Pi$，所以任意尺度 $Q_j>0$ 上的 $\Sigma_j\ge c_1Q_j$ 都强迫 $\Pi_j\ge(c_1/C)Q_j$。

令 $T_-=2\chi-3\tau$、$h=1-T_+/A$、$U=3\min(T_+,T_-)/A$。在 $p\ge A>0$、$a^2\ge T_+$ 和 $0<h\le1/3$ 下，结合另一手性的 Chern–Weil 关系，得到

$$
\mathcal J+(U-1-h)_+\ge ch.
$$

对 $U_j=1+h_j+O(h_j^2)$、$h_j\downarrow0$ 的原平衡族，这给出 $\inf_g\mathcal J(g)\ge c_2h_j$。允许类平方短缺时，右侧相应变为 $ch^2/(h+y)$。N1 研究 $T_+/A=2/3$ 附近的分离；这条线性结论研究 $T_+/A=1-h$ 且双手性约束接近等号的范围。

单解证明见[单个 Yamabe 单极子的线性强制](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/paper/sections/single_solution_coercivity.tex)。校准背景的 Hessian 与弱 Bianchi 推导见[线性强制正文](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/paper/sections/linear_coercivity.tex)。

### 2.7 两手性之间的能量限制

令 $T_+=A(1-h)$、$e=R/(8\pi^2A)$、$z=p/A-1\ge0$。精确代数归约为

$$
D_2/A=36\pi^2(e-1-h-2z),\qquad
P/A=2\pi^2e\mathcal J.
$$

由 (I41)，在 $Y=0$ 时存在普适 $c_0'>0$ 使

$$
e(1+\mathcal J/18)\ge1+(1+c_0')h+(2+c_0')z.
\tag{19}
$$

有短缺 $y=Y/A$ 时，附加正量相应为
$c_s(h+z)^2/(h+z+y)$。另一方面，两个 Chern–Weil 恒等式给

$$
e(1-\mathcal J)\le U,\qquad
U=3\min(T_+,T_-)/A.
$$

若 $L_h=1+(1+c_0')h$、$U>0$，消去 $e$ 得到

$$
\mathcal J\ge\frac{(L_h-U)_+}{L_h+U/18}.
\tag{20}
$$

当 $U\le0$，已有 $\mathcal J\ge1$。式 (20) 说明线性间隙来自两项共同作用：实际场要求 Ricci 能量超出经典最低值，另一手性又限制接近 Einstein 时可容许的总能量。

还有一个不同参数区间的上能量边界。设 $1/4<h<1/3$，定义

$$
G(h)=\frac{(4+\sqrt{1-3h})^2}{9},\qquad
 t_* =\frac{1-2\sqrt{1-3h}}{8+2\sqrt{1-3h}}.
$$

在全度量实际供给与 $a^2\ge T_+$ 下，紧化参数 $P_t=tD_{1/t}$ 的精确 Chern–Weil 式及 (17) 给

$$
\mathcal E(g)+(G(h)-e)_+
\ge c_*'t_*^2(1-2t_*)^2.
\tag{21}
$$

$t_*\downarrow0$ 时右端为 $\frac49c_*'(h-1/4)^2+O((h-1/4)^3)$。这条结论记录紧化端点的二次余量；其正性区间与 (N1) 的临界比例、式 (20) 的小 $h$ 线性窗口不同。

证明见[共形分离](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/continuation/20260927_conformal_separation_and_zero_end.md) Part I §§2–3 及[常权参数分析](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/sources/continuation/20260927_constant_weight_and_global_fit.md) §2.4。

### 2.8 经典数值预算为何不足以给出线性阶

下面的形式数据将微分强制与积分代数清楚地区分。对 $0<h\le1/4$，取

$$
\begin{gathered}
p=A,\quad T_+=A(1-h),\quad T_-=A(1+h)/3,\\
P=8\pi^2Ah^2,\quad S=32\pi^2A(1+h+2h^2),\\
W_-=\frac23\pi^2Ah^2,\qquad
W_+=\frac43\pi^2A(1-2h)+\frac23\pi^2Ah^2.
\end{gathered}
$$

它们满足两手性 Chern–Weil 恒等式、$W_\pm>0$、标量预算及全部 $D_\beta>0$。后一项可令
$X=2\sqrt{1+h+2h^2}$、$Z=\sqrt{1-2h+h^2/2}$ 后写成

$$
\frac{D_\beta}{8\pi^2A}
=\left(\frac X{\sqrt\beta}-\sqrt\beta Z\right)^2+(X+Z)^2-9.
$$

在该区间 $9-X^2-Z^2>0$，且

$$
4X^2Z^2-(9-X^2-Z^2)^2
=\frac94h^2(32-40h-25h^2)>0,
$$

故 $X+Z>3$。然而

$$
\mathcal J=\frac{4h^2}{1+h+3h^2}=o(h),\qquad
D_2=108\pi^2Ah^2,
\quad \Sigma=32\pi^2A(h+2h^2).
$$

因此在 $Y=0$ 时，这组数据不满足 $\Sigma\le C(P+D_2)$。这没有构造实际度量；它证明经典的上述全部数值约束仍容许二次阶缺陷，而同场微分相容性排除这种行为。详细代数见[经典比较](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/supplements/20261004_classical_and_quantitative_gaps.tex) §5。

### 2.9 已供给 BF 类的完整符号预算

在满足相应稳定上同伦非消失条件的 $r=2,3$ 个辛主体连通和中，设
$c_i^2=A_i>0$、$A=\sum_iA_i$，异常类为 $E_j$。交叉形式满足
$c_i\cdot c_j=\delta_{ij}A_i$、$c_i\cdot E_j=0$、$E_i\cdot E_j=-\delta_{ij}$，且非消失定理供给全部类

$$
\mathcal C_0=\left\{\sum_i\epsilon_ic_i+\sum_j\eta_jE_j:
\epsilon_i,\eta_j\in\{\pm1\}\right\}.
$$

对这组实际类，经典凸包预算和正子空间优化预算都恰为 $A$：

$$
\max_{v\in\operatorname{conv}(\mathcal C_0)}v^2
=\inf_H\max_{a\in\mathcal C_0}(a_H^+)^2=A,
$$

其中 $H$ 遍历交叉形式的极大正子空间。第一式由
$v=\sum t_ic_i+\sum u_jE_j$、$|t_i|,|u_j|\le1$ 及
$v^2=\sum A_it_i^2-\sum u_j^2\le A$ 得到，平均异常符号即取得 $\sum_i c_i$。
第二式的下界来自对全部独立符号平均投影平方；上界取包含所有 $c_i$、正交于所有 $E_j$ 的极大正子空间即可。这里优化抽象正子空间，不要求该最优子空间由某个度量实现。

若全部单极子类给出更大的预算 $B=A(1+\delta)$，经典 Ricci 估计
$R\ge8\pi^2(2p-T_+)$ 与 Einstein 的另一手性约束共同要求

$$
1+h+2\delta\le U.
$$

因此在 $U-1-h=O(h)$ 的平衡族上，未知类增加的 $O(Ah)$ 预算可能改变经典比较。已供给符号类的预算精确等于 $A$，不等于全部单极子类已被列尽；若要排除额外预算的一阶影响，还需例如 $B-A=o(Ah)$。本章的强制估计只调用实际选定类，不依赖这个尚未得到的上控。

证明及非消失条件见[BF 类的两种预算](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/paper/sections/bf_budget_comparison.tex)。

## 3. 任意固定有限 Euler 密度的端点

端点问题研究下列参数缺陷；其中 $V_g=\operatorname{Vol}_g(M)$：

$$
\kappa_\beta(g)=\fint_M|\operatorname{Ric}_g+g|^2
 +\frac{D_\beta(g)}{V_g}.
$$

它不同于前节有限参数估计的 $P/V+D_\beta/(\beta V)$。在 $s=-4$ 代表上，第一项才化为 $P/V$。

### 3.1 有限密度定理

[O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md) §§1–4 的命题为：在原逐共形类的单极子解存在性条件、$p\ge A>0$、$a^2\ge T_+$ 下，任意固定有限 $B$ 存在 $c_{\rm FD}(B)>0$，使

$$
\boxed{\frac{\chi(M)}A\le B\quad\Longrightarrow\quad
\kappa_\beta(g)\ge c_{\rm FD}(B)
\frac{(\beta-2)^2}{\beta^2},\qquad\beta\ge2.}
\tag{FD}
$$

该结论不另加点态 Ricci、直径、非塌缩、注入半径或统一 Sobolev 控制。[O10_Finite_Density_Complete_Proof.tex](../archive/originals/2026-09-29/O10_Finite_Density_Complete_Proof.tex) 汇集主证明与直接前置，适合沿完整依赖阅读。

### 3.2 证明：实际扭率、第五线丛与 Chern 配对

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

其中三次旋量表达式有不依赖局部标架的定义

$$
t(v)=\sum_{i=1}^4c^-(e^i)v\otimes(v\wedge\nabla_i v)
\in S^+\otimes L^4.
$$

$c^-$ 是负到正手性的 Clifford 乘法；$|\Phi|^2\to\rho_*$、$|v|^2\to m_*$。由于 $|\sigma|\le C|\nabla v|$，以及
$|\nabla\sigma|\le C(|\nabla^2v|+|\nabla v|^2+|\nabla\Phi||\nabla v|)$，有限密度估计给 $\fint|\nabla\sigma|^2\le C_B$。线丛次数来自 $\det S^+=L$，而非把一个局部系数当成全局标量。

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

### 3.3 对数预解尺度为何能检测陈数

上一证明使用的线丛引理具有独立的分析意义。设 $K_j$ 为闭四流形上的 Hermitian 线丛，实曲率为 $F_j$；全部范数采用 $dV_j/V_j$。假设

$$
\|\operatorname{Ric}_{g_j}\|_2+\|F_j\|_2+\|\nabla\sigma_j\|_2\le C,
\qquad |\sigma_j|\longrightarrow\ell>0\quad\text{依测度},
$$

并有闭二形式 $\omega_j=\omega_{0,j}+e_j$，其中
$\|\omega_{0,j}\|_\infty\le C$、$\|e_j\|_2\to0$。则
$V_j^{-1}\int F_j\wedge\omega_j\to0$。不要求有界模型 $\omega_{0,j}$ 自身闭合。

对 $\sigma_j$ 作有界等变径向截断，得 $s_j$，其模长仍趋于 $\ell$，且
$\|\nabla s_j\|_2^2\le E_0$。置 $\mathscr L_j=\nabla_j^*\nabla_j$、
$u_{j,\epsilon}=(I+\epsilon\mathscr L_j)^{-1}s_j$。最大值原理与谱分解给

$$
|u_{j,\epsilon}|\le C,\qquad
\|u_{j,\epsilon}-s_j\|_2^2\le\epsilon E_0,\qquad
\int_0^\infty\|\mathscr L_ju_{j,\epsilon}\|_2^2\,d\epsilon\le E_0.
$$

取 $\delta_j=\||s_j|-\ell\|_2^2+\|e_j\|_2^2+j^{-1}$。
在 $[\delta_j^{1/2},\delta_j^{1/4}]$ 上按 $d\epsilon/\epsilon$ 平均，能选择 $\epsilon_j$ 使

$$
\epsilon_j\|\mathscr L_ju_j\|_2^2\le\frac{4E_0}{|\log\delta_j|}\to0,
\qquad \|e_j\|_2^2/\epsilon_j\to0.
$$

式 (11) 的线丛版本给
$\fint(|\nabla^2u_j|^2+|\nabla u_j|^4)\le C(1+\|\mathscr L_ju_j\|_2^2)$。
对固定 $0<\ell_0<\ell_1<\ell$，低模长集 $Z_j=\{|u_j|\le\ell_1\}$ 的测度为 $O(\epsilon_j)$。因此

$$
\fint_{Z_j}|\nabla u_j|^2\to0,
\qquad \|e_j\|_2\left(\fint|\nabla u_j|^4\right)^{1/2}\to0.
$$

在 $u_j\ne0$ 处，单位截面 $u_j/|u_j|$ 给实联络形式 $\alpha_j$，满足
$d\alpha_j=F_j$、$|\alpha_j|\le C|\nabla u_j|/|u_j|$。
令 $\chi_j=\chi(|u_j|)$ 从 $\ell_0$ 以下的 $0$ 过渡到 $\ell_1$ 以上的 $1$。则 $\chi_j\alpha_j$ 光滑延拓到全流形，Stokes 公式给

$$
\fint F_j\wedge\omega_j
=\fint(1-\chi_j)F_j\wedge\omega_j
-\fint d\chi_j\wedge\alpha_j\wedge\omega_j\longrightarrow0.
$$

第一项由 $Z_j$ 的小测度、$F_j$ 的 $L^2$ 界和 $e_j\to0$ 控制；第二项由刚取得的两条导数估计控制。取 $\omega_j=F_j$ 就得到第五线丛所需的陈数矛盾。关键是选择使 $\epsilon_j\|\mathscr L_ju_j\|_2^2=o(1)$ 的尺度；任意平滑尺度通常只能给 $O(1)$，不足以消去过渡能量。

完整推导见[有限密度连续证明](../research/packages/20261007_Einstein_Gaps_Two_Sessions--9d4f2de3/20261007_Einstein_Gaps_Two_Sessions/sources/Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex)，其中亦给出实际扭率、模长—相位约化及协方差测试的公式。

### 3.4 密度范围与常数依赖

有限密度定理的量词是对每个固定 $B<\infty$ 取得 $c_{\rm FD}(B)>0$。其证明进一步给出关于 $B$ 的定量下控。线丛的对数陈数估计与第五线丛正势估计分别产生指数型和多项式型控制；两者均保留实际场误差与原曲率缺陷的联系。

令 $x=\kappa_\beta+\beta^{-2}$。设 $0<\epsilon_0\le1$ 为慢梯度截断中的固定指数，$\gamma=\epsilon_0/(1+\epsilon_0)$。以 $\mathfrak e_D$ 表示该稿所列实际场误差之和，包括辅助截面与扭率的 $H^1$、$L^4$ 差，则

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

## 4. 不需要 Euler 密度上界的两个范围

### 4.1 固定拓扑比例低于四分之三

设同一 Spin$^c$ 结构在整个共形类均有实际未扰动解，且

$$
p\ge A>0,\qquad a^2\ge T_+,\qquad T_+/A\le\theta<3/4.
$$

则存在只依赖 $\theta$ 的 $c_L(\theta)>0$，使该共形类内所有度量和所有有限 $\beta\ge2$ 满足

$$
\boxed{\kappa_\beta(g)\ge c_L(\theta).}
\tag{L}
$$

该结论使用整个共形类的实际供给；在全度量应用中，各共形类可以选择不同结构，但须共用 $A,\theta$。

证明把经典预算有效的区域和有限参数估计有效的区域接合。置
$Q_s=\int(s+4)^2/4$。由 Chern–Weil，

$$
V_g\kappa_\beta=(13/12+1/\beta)S+(6\beta+10)W_+
+Q_s-8\pi^2T_+-72\pi^2p.
$$

若 $T_+>0$，在经典式 (7) 中取辅助参数
$\gamma=(9\beta-\theta+6)/(9+\theta)$，恰消去 $W_+$ 项，得到

$$
V_g\kappa_\beta\ge a(\theta,\beta)S+Q_s,
\quad
 a(\theta,\beta)=\frac{N_\theta(\beta)}{\beta(9\beta-\theta+6)},
$$
$$
N_\theta(\beta)
=(3/4-\theta)\beta^2+(1/2-11\theta/4)\beta+6-\theta.
$$

$a>0$ 时，逐点最小化 $as^2+(s+4)^2/4$ 给
$\kappa_\beta\ge16a/(1+4a)$。多项式满足

$$
\operatorname{disc}N_\theta
=\frac{57}{16}(\theta-2/3)(\theta+142/19),
\quad N_{2/3}(\beta)=\frac{(\beta-8)^2}{12},
\quad \lim_{\beta\to\infty}a=\frac1{12}-\frac\theta9.
$$

所以 $\theta<2/3$ 时该下界直接统一为正；$2/3\le\theta<3/4$ 时，可能非正的参数落在一个有界区间，并远离 $\beta=2$。该区间内 $a^2\ge T_+>0$，式 (17) 的负平方成本为零，有限参数估计给正下界；在 $\beta=2$ 的邻域仍用 $N_\theta(2)=10-21\theta/2>0$。最后由 §3 的共形转移接回原度量。$T_+\le0$ 分支直接取 $\theta=0$，得到 $\kappa_\beta\ge1$。

三个数 $2/3,8,3/4$ 因而分别来自同一个多项式的判别式零点、双根和最高次系数消失。$\theta\uparrow3/4$ 时这条证明的常数退化，尚不能据此断言统一常数不存在。

上述证明仅使用经典不等式 (7)、有限参数估计 (17) 和 §3 的共形转移。$\kappa_\beta$ 包含场拟合缺陷，不能从 (L) 删除 $D_\beta/V_g$ 后声称同范围内的所有度量具有纯 Einstein 正间隙。

### 4.2 地理关系把无界手术数归入固定密度窗口

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

对满足所列单极子可解性条件的光滑极小复一般型曲面 $X$，$A=c_1^2(X)>0$。Noether 不等式与公式给

$$
p_g\le A/2+2,\qquad \chi(X)=12(1-q_{\rm hol}+p_g)-A.
$$

$A=1$ 时整数性给 $p_g\le2$，从而 $\chi(X)\le35$；$A\ge2$ 时 $\chi(X)\le5A+36\le23A$。所以统一有 $\chi(X)\le35A$，这里不要求常数最佳。因此

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

一般目标仍是原全部实际输入下，存在不依赖 $\chi/A$ 的绝对 $c>0$。FD、速率排除和 GEO 没有共同覆盖所有允许对象。本节截面范数均采用归一化体积测度。

### 5.1 不依赖反手性 Weyl 上界的估计

[双重带权测试](../archive/originals/2026-09-29/O10_Double_Weighted_Test.md) 给出一个不含曲率的估计。若 $|v|+|\nabla^*\nabla v|\le C_v$，对任意实 $e\in H^1$，用 $e^2v$ 测试方程并积分分部，得

$$
\int e^2|\nabla v|^2
=\operatorname{Re}\int e^2\langle\nabla^*\nabla v,v\rangle
-2\operatorname{Re}\int e\langle de\otimes v,\nabla v\rangle.
$$

吸收最后一项并用 Kato 不等式，可分别对标量和张量误差取得

$$
\|e\nabla v\|_2\le C(C_v)\|e\|_{H^1},\qquad
\||E|\nabla v\|_2\le C(C_v)\|E\|_{H^1}.
$$

若另有 $|w|+|\nabla^*\nabla w|\le C$，且 $\nabla w,\nabla^2w,\nabla\Phi,\nabla^2\Phi$ 的 $L^2$ 范数有界，重复使用该估计便控制 $\||\nabla v||\nabla w|\|_2$ 与 $\||\nabla\Phi||\nabla w|\|_2$。因此，对全局定义的光滑收缩张量 $\mathcal C$，若
$|\mathcal C|\le C$、$|\nabla\mathcal C|\le C(1+|\nabla\Phi|+|\nabla v|)$，则

$$
\left|\fint\zeta*\mathcal C*(\nabla^2v)*(\nabla w)\right|
\le C\|\zeta\|_{H^1}.
$$

证明只把 Hessian 的一个导数移到另外三个因子，不交换协变导数；常数不依赖 $\|\nabla^2v\|_2$ 或 $\fint|W^-|^2$。固定模长截断所产生的张量须满足上述全局性和导数条件。它控制的是明确的一类弱配对，不能把仅有界的径向系数变成小量。

[低幅度能量估计](../archive/originals/2026-09-29/O10_Low_Amplitude_Energy_and_O11_Scope.md) 进一步给出如下结论。令 $d\mu_j=dV_j/V_j$、$\mathscr L_j=\nabla_j^*\nabla_j$；假设 $|v_j|+|\mathscr L_jv_j|\le C$、$m_j=|v_j|^2\to m_*$ 于 $L^2(d\mu_j)$、$(\mathscr L_j-2)v_j\to0$ 于 $L^2(d\mu_j)$。另假设区域 $G_j$ 上的一个正交复类型投影 $\mathsf P_j$ 满足 $\int_{G_j}|\mathsf P_j\nabla v_j|^2d\mu_j\to0$，且 $\int_{M_j\setminus G_j}|\nabla v_j|^2d\mu_j\to0$。记 $q_j=|\nabla v_j|^2$，则对固定 $0<\theta<1$、$\varepsilon>0$ 有

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

### 5.3 一阶场的稳定子与线丛选择

能否直接从一阶正旋量数据得到模长非零的线丛截面，取决于一个代数约束。理想端点的一阶数据 $(\Phi,P)$ 满足

$$
|\Phi|^2=4/3,\quad \langle\Phi,P_i\rangle=0,
\quad\sum_i c(e^i)P_i=0,\quad |P|^2=4/9.
$$

这是一条 $\operatorname{Spin}^c(4)$ 轨道。固定 $\Phi\parallel e_1$ 后，$P_i=\theta_i e_2$；Dirac 关系使 $\theta$ 具有形式 $e_2\otimes s^-$，且 $|s^-|$ 固定。$SU(2)_-$ 对该球传递作用，故轨道实维数为 $3+3=6$。其圆稳定子可写为

$$
\left[\operatorname{diag}(\bar\lambda,\lambda),
\operatorname{diag}(\bar\lambda^3,\lambda^3),\lambda\right],
\qquad |\lambda|=1,
$$

作用于 $L$ 的权为 $\lambda^2$。因此任何连续等变的 $L^m$ 值一阶构造，$m\ne0$，在理想轨道上满足
$F(\Phi,P)=\lambda^{2m}F(\Phi,P)$，只能为零。若实际一阶数据依测度趋近该紧轨道，这些构造也依测度趋零。加入由同一理想数据等变决定的零阶曲率量不会改变此结论。

有限密度证明取得的 $\nabla v$ 多提供一个非零权五分量，正是 $\Phi\wedge t(v)$ 所提取的方向。这个表示论结论解释了为何单靠一阶自然线丛截面不能替代第五线丛；它不排除非局部构造或某个投影微分方程的额外消去。

秩二也不能直接复制秩一引理。对 $E=S^-\otimes L$，
$c_2(E)=(9a^2+T_-)/4$；但四维中的点零度数可由有限 $H^1$ 能量承载。在固定秩二丛的点外单位截面上，度数一角向场有 $|\nabla s|=O(r^{-1})$，在半径 $\epsilon$ 内截成零只需 $O(\epsilon^2)$ 能量。因此“近乎处处非零且 $H^1$ 有界”本身不推出 $c_2(E)/V\to0$。

### 5.4 Taub–NUT 载体：平均控制与实际匹配的区别

负旋量的失控尺度可以由一个精确模型展示。在超 Kähler Taub–NUT 度量
$g=Hdx^2+H^{-1}\eta^2$、$H=1+\ell/r$ 上，取平行正旋量标架和
$\Phi_\ell=\sqrt{4/3}\,e_1+(\sqrt2/3)\bar f e_2$，$f=x_1+ix_2$。其三次扭率为

$$
v=\sqrt{m_*/2}\,d\bar f,\qquad
|v|^2=\frac{m_*r}{r+\ell},\qquad
|\nabla v|^2=\frac{m_*\ell^2}{(r+\ell)^4}.
$$

有 $\int|\nabla v|^2=8\pi^2m_*\ell^2$，而
$\int|\nabla v|^4=(8\pi^2/15)m_*^2$、
$\int|\nabla^2v|^2=(16\pi^2/5)m_*$。对体积量级 $\ell^2$ 的块，二次能量平均有界，后两项却增长为 $\ell^{-2}$。

第五线投影又有精确偶极式

$$
\Phi_\ell\wedge t(v)
=C_\sigma\frac{\ell\bar f}{(r+\ell)^3},\qquad
C_\sigma=2^{11}\sqrt6/3^7.
$$

其模长导数能量为 $(8\pi^2/21)C_\sigma^2>0$，独立于核尺度；在上述块上截面本身却依测度趋零。这同时说明正模长与导数预算是有限密度证明的两项实际要求。该场只是在 Ricci-flat 切模型中的 Dirac–扭率构造，尚未满足物理块及闭流形的完整单极子系统。

恢复标量曲率 $-4$ 和行列式曲率后，Weitzenböck 式中的物理曲率作用必须保留；裸切模型的 $-2v$ 不能直接计为残差代价。相邻块还必须匹配同一个正旋量一阶场、行列式联络与边界通量。上述精确公式、模长能量积分以及一阶数据的 Hermite 匹配估计见[Taub–NUT 端点场](../research/notes/taub_nut_endpoint_fields.md)。它们缩小了可行的集中机制，尚未给出无密度端点的证明或闭反例。

## 6. 双取向、Kodaira 斜率与后续配对推广

### 6.1 固定密度前置 FD2

使用 FD 在固定 $B=2$ 的特例，记为 **FD2**。其同一实际类 $c$ 必须满足

$$
(c^+)^2\ge A_c>0,\quad c^2\ge T_+,\quad\chi/A_c\le2.
$$

FD2 的实际扭率、辅助截面与线丛证明见 §3；下面给出从这个定理到双取向间隙的推导。

### 6.2 全曲面丛范畴的间隙

对光滑定向曲面丛 $\Sigma_f\to M\xrightarrow{\pi}\Sigma_b$，$f,b\ge2$，由 FD2 得

$$
\boxed{\mathcal J(g)+\left(1-\frac{3|\tau(M)|}{\chi(M)}\right)_+
\ge\varepsilon_{\rm SB},\qquad
\varepsilon_{\rm SB}=\left(\frac{\min\{1,c_{\rm FD}(2)\}}{200}\right)^2.}
\tag{SB}
$$

该常数独立于基底和纤维的亏格、丛的单值表示、总空间以及度量。

**证明。** 取总空间取向使 $\tau\ge0$，记 $e=\chi(M)>0$。定向平面丛分裂
$TM=T_{\mathrm{vert}}M\oplus\pi^*T\Sigma_b$ 的 Euler 类记为 $y,x$，则

$$
x^2=0,\quad xy=e,\quad y^2=3\tau,
\qquad a=x+y,\quad b=x-y,
$$
$$
a^2=2e+3\tau,\qquad b^2[M]=-2e+3\tau,
\qquad a\cdot b=-3\tau.
\tag{22}
$$

Thurston 的曲面丛辛构造与 Taubes 非消失定理分别提供两取向的类；典范类的整体符号不影响平方和绝对配对。$b_1(M)\ge2b\ge4$，故正取向 $b_2^+>1$，而 $a^2>0$ 保证每个共形类均负。

仅需考虑 $\mathcal J(g)<1$，在同一负 Yamabe 代表上置

$$
j=\mathcal J(\widehat g)\le\mathcal J(g),\quad
 t=3\tau/e,\quad u=V/(2\pi^2e),\quad
 r=P/V=4j/(4-j),\quad w=W_-/V.
$$

正取向实际标量预算和反手性 Chern–Weil 给

$$
2+t\le U:=(a^+)^2/e\le u,\qquad
w=\frac{2-t}{u}-\frac13+\frac{j}{4-j}\ge0.
\tag{23}
$$

因此 $t<2$，并有

$$
u\le\frac{3(4-j)}{4(1-j)}(2-t),\qquad
 t\le1+\frac{9j}{16-7j}\le1+j.
$$

$t<2$ 又推出 $b_2^-(M)>e/6+b_1-1>1$，所以反取向类 $b$ 也具有所需全度量供给。令

$$
Z=\|b^-\|_2^2/e,\quad X=\|a^-\|_2^2/e=U-(2+t),
\quad Y=\|b^+\|_2^2/e=Z-(2-t).
$$

负投影范数均取正值。反取向标量预算给 $2-t\le Z\le u$；同一度量的 Hodge 正交与 (22) 给关键的混合约束

$$
\boxed{t\le\sqrt{UY}+\sqrt{XZ}.}
\tag{24}
$$

令 $d=j+(1-t)_+$。若 $0<d\le1/256$，由 (23) 可得

$$
1-d\le t\le1+d,\quad3-d\le u\le3+5d<4,
\quad X\le4d,\quad w\le d,\quad r\le4d/3.
$$

将 $\sqrt{XZ}\le4\sqrt d$ 代入 (24)，保留同一场的投影预算，得到

$$
\frac Zu\ge\frac{2-t}{u}
 +\frac{(t-4\sqrt d)^2}{u^2}
\ge\frac49-2\sqrt d.
\tag{25}
$$

取反取向预算 $A_-=e(2-t)=b^2[\bar M]>0$。此时

$$
p_b=eZ\ge A_-,\qquad
\frac{\chi(\bar M)}{A_-}=\frac1{2-t}<2.
$$

反取向参数缺陷为

$$
\bar\kappa_\beta
=r+16(1+\beta^{-1})+6(\beta+1)w-36Z/u.
$$

取有限 $\beta=d^{-1/2}\ge16$，式 (25) 给

$$
\bar\kappa_\beta<100\sqrt d,
$$

而 FD2 给 $\bar\kappa_\beta\ge c(1-2\sqrt d)^2\ge c/2$，其中
$c=\min\{1,c_{\rm FD}(2)\}$。所以 $d\ge(c/200)^2$。$d\ge1/256$ 分支直接满足同一下界；$d=0$ 时有 $t=1,u=3,X=0,w=0,Z\ge4/3$，从而每个有限 $\beta$ 都满足 $\bar\kappa_\beta\le16/\beta$，与 FD2 矛盾。再由 (4) 回到原度量，得到 (SB)。

### 6.3 Kodaira 斜率：反证序列自动具有固定密度

对承载 Einstein 度量的曲面丛，$\mathcal J=0$，所以

$$
3|\tau|\le(1-\varepsilon_{\rm SB})\chi.
$$

光滑 Kodaira 纤维化具有 ample 典范丛，经典 Aubin–Yau 定理给负 Kähler–Einstein 度量。代入 $c_1^2=2\chi+3\tau$、$c_2=\chi$ 即得

$$
\boxed{c_1^2/c_2\le3-\varepsilon_{\rm SB}.}
\tag{26}
$$

这条推论由 FD2 及上述供给、配对证明，覆盖全部所述 Kodaira 纤维化。它回答斜率能否统一远离 $3$ 的问题；其常数不是最佳斜率的计算，也不判断是否存在斜率大于 $8/3$ 的实例。

在 Kähler–Einstein 代表上还可直接看出为何无需一般无密度端点。设 $r_K=c_1^2/e$，归一化 $s=-4$。反取向类 $b$ 是原复结构的 $(1,1)$ 类，故其自对偶部分在 Kähler 方向上；结合 (22) 得

$$
p_b=\frac{4e^2}{c_1^2},\qquad
V=2\pi^2c_1^2,\qquad
\frac{W_-}{V}=\frac{4(3-r_K)}{3r_K}.
$$

因而

$$
\bar\kappa_\beta
=16(1+\beta^{-1})
+8(\beta+1)\frac{3-r_K}{r_K}
-\frac{144}{r_K^2}.
\tag{27}
$$

若有 $r_K\uparrow3$ 的序列，取 $\beta=(3-r_K)^{-1/2}$，右侧趋于零；但
$A_-=e(4-r_K)$，所以 $\chi/A_-=1/(4-r_K)\le1$，FD 始终使用同一个有限密度常数，产生矛盾。这里起作用的是反取向的实际场在同一 Kähler–Einstein 度量上的精确投影，而非仅分别使用两个类平方。

完整证明见[双取向统一间隙](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md) §§2–7。公开问题及经典严格不等式的来源为 Kotschick, *On regularly fibered complex surfaces*；LeBrun, *Diffeomorphisms, symplectic forms and Kodaira fibrations*；Catanese–Rollenske, *Double Kodaira fibrations*；Catanese 的综述 §1.3，相关文献条目保存在[连续数学稿](../archive/originals/2026-10-07/00_All_Recent_Research.tex)。

### 6.4 一侧凸包与配对短缺

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

## 7. 正间隙的 Ricci 流后果

设闭四流形满足全度量 $P(g)\ge p_0>0$ 和 $\mathcal Y(M)<0$。例如，若 $\mathcal J\ge j_0>0$、$S\ge32\pi^2A$，则由 $P=\mathcal JR/4\ge\mathcal JS/16$ 可取 $p_0=2\pi^2Aj_0$。这里只使用单独的 $P$ 正下界。

考虑体积保持的 Ricci 流

$$
\partial_tg=-2\operatorname{Ric}+\tfrac12\bar s\,g,
\qquad \bar s=\fint s,\qquad V=\operatorname{Vol}(g(0)).
$$

取 $a>0$ 使 $\mathcal Y(M)\le-a\sqrt V$，并记
$m(t)=\min s_{g(t)}$、$b_0=-m(0)>0$。Yamabe 变分原理给 $m(t)\le-a$。采用 $\Delta=\operatorname{div}\nabla$ 写流方程，有

$$
\partial_ts=\Delta s+2|\operatorname{Ric}^{\circ}|^2
+\tfrac12s(s-\bar s),
$$
$$
m'\ge\tfrac{-m}{2}(\bar s-m)\ge0,
\qquad
\bar s'=\frac{2P}{V}-\frac12\operatorname{Var}(s).
\tag{28}
$$

前式在 $m$ 几乎处处可微时成立。若 $s\le K$ 于光滑时间区间 $[0,t]$，$K\ge0$，点态 $(s-m)(K-s)\ge0$ 给

$$
\operatorname{Var}(s)\le(K-m)(\bar s-m),
\qquad
\frac12\operatorname{Var}(s)
\le\left(1+\frac K{-m}\right)m'.
$$

积分 (28) 得到

$$
\boxed{\frac{2p_0}{V}t
\le K\left(1+\log\frac{b_0}{a}\right)
-\bar s(0)+b_0-a.}
\tag{29}
$$

因此永生流的历史正标量峰值
$K(t)=\max\{0,\sup_{0\le u\le t}\max_Ms_{g(u)}\}$ 满足

$$
K(t)\ge
\frac{(2p_0/V)t+\bar s(0)-b_0+a}{1+\log(b_0/a)}.
\tag{30}
$$

式 (29)–(30) 只依赖显示的静态输入与流的演化式。

若另引用四维未归一化 Ricci 流“有限时间内标量绝对值有界则光滑延拓”的外部定理，则对任意 $K>\max\{0,\max s_{g(0)}\}$，首次达到时间 $\tau_K$ 必在最大光滑时间内发生，且

$$
\tau_K\le\frac{V}{2p_0}
\left[K\left(1+\log\frac{b_0}{a}\right)
-\bar s(0)+b_0-a\right].
\tag{31}
$$

原因是：若有限时间前未达到 $K$，则 $m(0)\le s\le K$；解除体积归一化的比例因子有正上下界，外部定理允许延拓。若流永生且未达到 $K$，则与 (29) 矛盾。在 $s(0)=-4$、$V\le CA$、$j_0\ge ch$ 的平衡族中，(31) 给 $\tau_K\le C_K/h$。

证明及外部定理的指定版本见[全度量 Ricci 间隙的定量动态后果](../archive/originals/2026-10-07/03_Quantitative_Ricci_Flow.tex) §§1–4。这里控制历史峰值和首次达到时间，不断言流必有限时间奇异，也不给出奇异率。

## 8. 适用范围与继续研究的数学连接

上述论证具有四个不同层次：实际规范供给确保场存在；同场微分相容性产生比特征数预算更强的曲率约束；有限密度和拓扑分区处理退化参数；两取向的交叉配对将整个几何族的边界行为送入固定端点。

一般无密度端点尚需控制 §5 的中间模长集中，或构造满足完整闭流形方程的反例。多个实际类的配对提供另一种信息：若 $a_1,\ldots,a_m$ 在同一度量下具有实际供给，则交叉矩阵满足 $Q=G^+-G^-$，其中 $G^\pm$ 是正半定 Hodge Gram 矩阵。现有双取向定理使用其中一个混合配对；任意多场矩阵的统一锐利估计尚未建立。

曲率最优值则还要把这些全度量下界与实际恢复构造匹配。严格低于标准手术费用的构造已表明首项 $4$ 在所列族上不最优；其精确极值与光滑取得性见[曲率变分](CURVATURE_VARIATION.md)。同一研究中的点态逼近、周期与精确实现见[构造与实现](CONSTRUCTIONS_AND_REALIZATION.md)。

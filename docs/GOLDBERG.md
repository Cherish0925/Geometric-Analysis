# 负 Einstein 几乎 Kähler 四维几何

## 问题与规范

设 $(M^4,g,J,\Omega)$ 为闭、连通的几乎 Kähler 四维流形，

$$
\Omega(X,Y)=g(JX,Y),\qquad d\Omega=0,\qquad
\operatorname{Ric}_g=-ag,\quad a>0.
$$

取向由 $\Omega^2$ 决定，故 $*\Omega=\Omega$、$|\Omega|^2=2$，标量曲率为 $s=-4a$。负 Goldberg 问题是：上述条件是否蕴含 $\nabla\Omega=0$？等价地，是否存在闭的非 Kähler 几乎 Kähler–Einstein 四维流形，且 Einstein 常数为负？

下文采用非负 Laplace 算子 $\Delta=-\operatorname{div}\nabla$ 与 $\nabla^*\nabla$。曲率算子作用在二形式上，Weyl 算子的范数为 Hilbert–Schmidt 范数。令

$$
q=|\nabla\Omega|^2,\qquad n=\Omega/\sqrt2,\qquad
Z=\{x\in M:q(x)=0\}.
$$

相对于 $\Lambda^+=\mathbb Rn\oplus n^\perp$，写成

$$
W^+=\begin{pmatrix}t&v^*\\v&-tI/2+B\end{pmatrix},\qquad
t=\frac{s}{6}+\frac q4,\qquad \operatorname{tr}B=0,
$$

其中

$$
\eta=W^+\Omega-t\Omega\in\Lambda_J^-,\qquad v=\eta/\sqrt2.
$$

这里 $\Lambda_J^-$ 是实 $J$-反不变二形式丛，$B$ 是 $n^\perp$ 上的无迹对称块，通常记为 $W_3^+$。以下内容按完备非紧构造、扭率零集、曲率刚性和整体约束组织；每一结论均附证明原稿。

## 完备非紧构造与 Fino 的存在性问题

[显式构造与验证](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex)给出微分同胚于 $\mathbb R^4$ 的完备度量与相容二形式，满足

$$
\operatorname{Ric}=-3g,\qquad W^-=0,\qquad d\Omega=0,\qquad
|\Omega|^2=2,\qquad |\nabla\Omega|^2>0.
$$

构造使用 $\mathrm{SL}(2,\mathbb R)$ 上的左不变余标架

$$
d\sigma_1=-2\sigma_2\wedge\sigma_3,\qquad
d\sigma_2=2\sigma_3\wedge\sigma_1,\qquad
d\sigma_3=2\sigma_1\wedge\sigma_2.
$$

在 $1/3<x<1$ 上定义的显式系数光滑延拓到平面丛

$$
\mathrm{SL}(2,\mathbb R)\times_{\mathrm{SO}(2)}\mathbb R^2
\longrightarrow\mathbb H^2.
$$

总空间微分同胚于 $\mathbb R^4$，且

$$
|\nabla\Omega|^2=\frac{36(1-x^2)^3}{(1+3x^2)^3}.
$$

零截面处该值为 $32/3$；$x\to1$ 时径向距离趋于无穷。原稿分别证明零截面的光滑性、度量完备性及曲率不变量的非恒定性，因此所得度量非齐性。全部曲率计算另附[精确代数程序](../archive/originals/2026-10-08/Q4_independent_cartan.py)。构造的来源为研究系统 A01；对应原稿补充曲率计算、完备延拓和文献联系。

Fino 的 *Almost Kähler 4-dimensional Lie groups with $J$-invariant Ricci tensor*（2005）在 Corollary 2.1 之后询问：实四维 Lie 群上是否存在非不变、非 Ricci 平坦的严格几乎 Kähler–Einstein 度量。将上述结构拉回 $(\mathbb R^4,+)$，即给出这一存在性问句的肯定例子，并具有完备性。原稿对该问句的回答与历史优先权作分别处理。该例非紧且体积无限；闭负 Goldberg 研究所需的进一步条件来自整体紧致几何。

## 扭率零点及零曲线

局部选取与 $\Omega$ 正交、长度为 $\sqrt2$ 的二形式 $\phi,J\phi$，写成

$$
\nabla\Omega=\vartheta\otimes\phi-J\vartheta\otimes J\phi,
\qquad q=4|\vartheta|^2,
$$

其中 $(J\vartheta)(X)=-\vartheta(JX)$。$\vartheta$ 的零点与 Nijenhuis 张量 $N_J$ 的零点一致。在零点处，$L=(\nabla\vartheta)^\sharp$ 的秩、实行列式和零化性质与局部标架选择无关。

[零点结构原稿](../archive/originals/2026-10-09/Q4_Torsion_Zero_Structure.tex)证明，在适配的复正交标架中，

$$
L(z)=cz+Q\bar z,\qquad c\in\mathbb C,\quad Q\in M_2(\mathbb C),
\qquad \operatorname{tr}(Q\bar Q)=-8|c|^2,
$$

$$
\det_{\mathbb R}L=9|c|^4+|\det_{\mathbb C}Q|^2\ge0.
$$

$\bar Q$ 表示逐项共轭。横截零点的局部指数为 $+1$；非横截零点的导数实秩为 $0$ 或 $2$。在 $Z$ 上还有精确恒等式

$$
\boxed{|\nabla^2\Omega|^2=4|B|^2-6|\eta|^2.}
$$

Armstrong 的经典拓扑论证将 $N_J$ 视为复秩二丛

$$
\mathcal N=T^{1,0}M\otimes\bar K,\qquad K=\Lambda^{2,0}T^*M
$$

的截面，并给出

$$
c_2(\mathcal N)[M]=5\chi(M)+6\tau(M).
$$

对闭、非零标量 Einstein 度量，Chern–Weil 公式保证该数为正，因而 $Z\ne\varnothing$。若全部零点横截，则

$$
\#Z=5\chi+6\tau.
$$

这一计数与正局部指数相容。

[零曲线分析](../archive/originals/2026-10-15/Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex)进一步证明：当 $s\ne0$ 时，不存在紧致无边界嵌入曲面 $C\subset Z$ 满足

$$
\ker(DN_J)_x=T_xC\qquad\text{对所有 }x\in C.
$$

对于闭光滑 $J$-全纯零曲线，若 $DN_J$ 的秩二点在曲线上稠密，则 $C$ 全测地。其法向扭率导数为线丛

$$
\operatorname{Hom}_{\mathbb C}
(\bar\nu_C,T^{1,0}C\otimes\bar K|_C)
\simeq\bar K^{\otimes2}|_C
$$

的截面 $\xi$，其中 $\nu_C$ 是复法丛。该线丛的度数为

$$
\deg(\bar K^{\otimes2}|_C)
=\frac{s}{4\pi}\operatorname{Area}_g(C)<0.
$$

故 $\xi$ 必有零点。其[切向微分方程](../archive/originals/2026-10-15/Goldberg_Global_Connections_20261015.tex)为

$$
D^{1,0}\xi=r,\qquad D^{1,0}r=0,
$$

其中 $D$ 为诱导的典范 Hermitian 联络，$r$ 是横向曲率分量的法向导数。方程保留这一非齐次项，容许秩下降及负指数。

同一批原稿还构造了实解析相容度量的有限阶模型，满足 $\operatorname{Ric}+g=O(|x|^6)$，且扭率具有孤立横截零点。该计算确立所列 Taylor 阶的相容性；精确 Einstein 局部解的存在性仍是独立问题。

## 行列式与 Green 势刚性

定义自对偶曲率块、其相反数及第二初等对称函数：

$$
\mathcal R_+=W^+-\frac a3I,\qquad A=-\mathcal R_+,
\qquad U=\sigma_2(A)=\frac{a^2}{3}-\frac12|W^+|^2.
$$

经典 Einstein Weyl–Weitzenböck 方程为

$$
\nabla^*\nabla W^++\frac s2W^+-6(W^+)^2+2|W^+|^2I=0.
$$

与 $W^+$ 配对并平移曲率算子，得到

$$
(\Delta+2a)U=|\nabla A|^2-18\det\mathcal R_+.
$$

闭流形上的 $L_a=\Delta+2a$ 可逆。记其正 Green 核为 $G_a(x,y)$，并令

$$
\Psi=L_a^{-1}(\det\mathcal R_+),\qquad
\mathcal D=L_a^{-1}(|\nabla A|^2).
$$

于是 $U=\mathcal D-18\Psi$、$\mathcal D\ge0$。结合零点恒等式，[合并原稿](../research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)得到：对每个 $p\in Z$，

$$
\boxed{18\Psi(p)=\mathcal D(p)
+\frac18|\nabla^2\Omega(p)|^2+\frac54|\eta(p)|^2.}
$$

若存在 $p\in Z$ 使 $\Psi(p)\le0$，右端各项均为零。Green 核的严格正性推出 $\nabla A\equiv0$，进而

$$
A=a\,n\otimes n,\qquad \nabla\Omega=0.
$$

这给出[Green 势刚性定理](../archive/originals/2026-10-14/Q4_Green_Potential_Rigidity.tex)。全局条件 $\det\mathcal R_+\le0$ 通过正性保持蕴含 $\Psi\le0$，从而包含较早的[行列式符号刚性定理](../archive/originals/2026-10-13/Q4_Determinant_Sign_Rigidity.tex)。

将 $W^+$ 的特征值记为 $\lambda_1\ge\lambda_2\ge\lambda_3$，令

$$
\Sigma=\{x:\lambda_1(W^+)=\lambda_2(W^+)\}.
$$

则零点结构进一步给出

$$
Z\cap\Sigma=\{p:\nabla\Omega(p)=0,\ \nabla^2\Omega(p)=0\}.
$$

上述闭光滑零曲线必经过 $Z\cap\Sigma$。在交点处，恒等式化为

$$
18\Psi(p)=\int_MG_a(p,y)|\nabla A(y)|^2\,dV_y.
$$

右端记录全流形的曲率变化。任何闭非 Kähler 候选必须在每个扭率零点满足 $\Psi>0$，并在某个开集满足 $\det\mathcal R_+>0$。

## 规范正交、调和乘积与变分

### 规范正交

典范曲率公式与 Bonthrone–Zhang 的典范因子定理给出：对每个闭实 $J$-反不变二形式 $\alpha$，

$$
\int_M\langle\eta,\alpha\rangle\,dV_g=0.
$$

因此，若存在全局光滑 $f>0$ 使 $d(f\eta)=0$，则 $\eta=0$。Apostolov–Armstrong–Drăghici 的紧致第三 Gray 定理随后推出 $\nabla\Omega=0$。

在 $\{\eta\ne0\}$ 上定义 Lee 形式 $\vartheta_\eta$：

$$
d\eta=\vartheta_\eta\wedge\eta.
$$

积分因子方程等价于 $d\log f=-\vartheta_\eta$。其局部可解性要求 $d\vartheta_\eta=0$，全局可解性还涉及周期及跨零集延拓。[规范正交原稿](../archive/originals/2026-10-12/Q4_Canonical_Orthogonality.tex)计算了上述非紧例的 $d\vartheta_\eta\ne0$，给出局部积分因子存在性的明确障碍。

### 调和乘积

对固定闭定向度量，取平均正交规范的自对偶调和基 $\psi_1,\ldots,\psi_m$，其中 $m=b_2^+(M)$。令

$$
G_{ij}(x)=\langle\psi_i(x),\psi_j(x)\rangle,
\qquad B_g(x)=G(x)-I,
\qquad
H_{ij}=\fint_M\langle\nabla\psi_i,\nabla\psi_j\rangle\,dV_g,
$$

并在实对称矩阵空间上定义

$$
\mathsf C_g(X)=\fint_M\langle B_g(x),X\rangle B_g(x)\,dV_g.
$$

相容几乎 Kähler 形式（模去符号）精确对应

$$
X\in\ker\mathsf C_g,\qquad X\succeq0,\qquad
\operatorname{tr}X=1,\qquad\operatorname{rank}X=1.
$$

相应形式平行当且仅当 $\operatorname{tr}(HX)=0$。若 $\ker H\ne0$ 且度量负 Einstein，di Scala–Nagy 的唯一性定理保证全部相容形式平行。

[调和乘积原稿](../archive/originals/2026-10-13/Q4_Harmonic_Product_Reduction.tex)还计算了 Kähler 方向附近的范数方差：沿非平行调和方向，其阶为四阶，而导数能量为二阶。一般负 Einstein 度量的剩余问题是确定其调和乘积核中的秩一正矩阵是否均来自平行形式。

### Einstein 路径与联络变分

由 Sekigawa 恒等式和 Chern–Weil 公式，闭几乎 Kähler–Einstein 四维流形满足

$$
s^2\operatorname{Vol}_g(M)-32\pi^2(2\chi+3\tau)
=\frac32\int_Mq^2\,dV_g+16\int_M|B|^2\,dV_g.
$$

沿归一化为 $\operatorname{Ric}=-g$ 的光滑 Einstein 路径，体积不变。若路径起点为同取向 Kähler–Einstein 度量，则路径中每个承载相容几乎 Kähler 结构的成员均为 Kähler。

对于 $\Lambda^+=\mathbb Rn\oplus n^\perp$ 上的 Levi-Civita 联络，写 $\mathcal A=D_0+C$，其中 $D_0$ 保持分裂，$C$ 为非对角部分。固定丛上的联络路径 $\mathcal A_t=D_0+tC$ 满足

$$
\operatorname{YM}(\mathcal A_t)
=\operatorname{YM}(\mathcal A)
+2(1-t^2)^2\|F_{D_0}^-\|_2^2.
$$

这是联络变分公式；度量变分还要求路径中的联络由相应度量的 Levi-Civita 联络诱导。两项结论的推导见[整体联系原稿](../archive/originals/2026-10-15/Goldberg_Global_Connections_20261015.tex)。

## 完整 Weyl 耦合与开放部分

令 $D$ 为保持 $\mathbb Rn\oplus n^\perp$ 的投影联络，写

$$
\nabla=D+C,\qquad
C_i=\begin{pmatrix}0&-p_i^T\\p_i&0\end{pmatrix}.
$$

几乎 Kähler 类型关系与调和性给出

$$
\sum_i p_i p_i^T=\frac q4I_{n^\perp},\qquad D^*p=2v.
$$

Einstein Weyl 方程的无迹横向块为

$$
D^*DB+\left(\frac{3s}{2}+2q\right)B
=2\sum_i[p_i(D_iv)^T+(D_iv)p_i^T]_0
+2(vv^T)_0,
$$

其中 $[\cdot]_0$ 表示二维块的无迹部分。该方程光滑穿过扭率零集，并保留 $B$、$v$ 与几乎复结构导数之间的耦合；证明见[完整 Weyl 方程原稿](../archive/originals/2026-10-15/Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex) §5。

闭负 Goldberg 的一般情形仍开放于这些原稿。当前条件刚性定理说明，非 Kähler 候选须同时具有非空扭率零集、零点处严格为正的行列式 Green 势，以及符合上述微分方程的横向 Weyl 分量。零曲线的秩下降和孤立零点仍属于待处理的几何情形。

沿 Green 势方法，需由原始 Einstein–几乎 Kähler 系统进一步控制零点处的整体曲率配对；沿调和乘积方法，需限制负 Einstein 度量所实现的秩一核；构造方向则需得到闭的精确 Einstein 相容结构。这些是同一闭问题的不同表述与研究入口。

最新的公式衔接与来源对应见[10 月 15 日合并稿](../research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)。Armstrong 的零点存在性、Derdziński 的 Weyl 方程、Sekigawa 恒等式、第三 Gray 定理、di Scala–Nagy 唯一性及 Watson 的浸没刚性在各原稿中保留为经典输入。

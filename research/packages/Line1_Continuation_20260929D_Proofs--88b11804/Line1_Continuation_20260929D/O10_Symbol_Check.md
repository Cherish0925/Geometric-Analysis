# O10 第五线丛论证：独立符号核验与正手性捷径检验

核验对象：`upload/O10_Finite_Density_Fifth_Line(1).md` 第 2—5 节。日期：2026-09-29。

结论：附件所用 Clifford 矩阵、两个相位流、三次式的线丛次数、Cartan 式、自对偶投影、加权符号以及线丛 Bochner 正势彼此一致。没有发现将正势改为负势的符号错误。这里核验有限代数与积分恒等式，不代替弱测试及截断收敛的分析证明。

随附纯 Python 脚本 `verify_fifth_line_symbols.py` 不依赖外部数学包。所有矩阵计算使用能被二进制精确表示的 Gaussian dyadic 数；最终势常数使用有理数 Fraction。脚本逐项检查全部 15 个实连接变量的基方向，而非随机数检验。

## 1. 三次式确实落在第五行列式幂

令原 Spin-c 束为 $S^\pm$，$L=\det S^+$，而 $E=S^-\otimes L$。则

\[
\det E=L^3,\qquad c^-(e^i)v\in S^+\otimes L,
\qquad v\wedge\nabla_i v\in L^3.
\]

因此

\[
t(v)\in S^+\otimes L^4,\qquad \Phi\wedge t(v)\in L^5.
\]

在附件规范的局部帧 $v=\sqrt m(1,0)$ 中，用反向 Clifford 矩阵 $-C_i^*$ 直接计算得

\[
t(v)=m^{3/2}(-b_1+ib_2,-b_3-ib_4).
\]

故

\[
-\frac{\Phi\wedge t(v)}{2\sqrt\rho\,m^{3/2}}
=\frac{b_3+ib_4}{2}=c_0.
\]

这同时确定了原附件负号和 $D_5=d+5i\mathfrak a$，无需通过猜测 gauge 权重确定。

## 2. 保留两个相位流的 Cartan 式

以

\[
\Omega_{+,LC}=\begin{pmatrix}i(p-\mathfrak a/2)&-\bar\eta\\
\eta&i(\mathfrak a/2-p)\end{pmatrix},\quad
\Omega_{-,LC}=\begin{pmatrix}i(q-3\mathfrak a/2)&-\bar b\\
b&i(3\mathfrak a/2-q)\end{pmatrix}
\]

代入

\[
\Omega_{-,LC}C_j-C_j\Omega_{+,LC}=\Gamma^i{}_j C_i,
\qquad de^i=-\Gamma^i{}_j\wedge e^j.
\]

令 $\theta_1=e^1-ie^2$、$\theta_2=e^3-ie^4$，并置
$\eta=\kappa\theta_1$、$b=c\theta_2$，得到两个精确恒等式：

\[
\boxed{d\theta_2=i(2\mathfrak a-p-q)\wedge\theta_2
-\bar c\,\Xi_-,}
\]

\[
\boxed{d\theta_1=-i(\mathfrak a+p-q)\wedge\theta_1
+\kappa\,\Xi_+,}
\]

其中

\[
\Xi_-=e^{13}+e^{24}+i(e^{14}-e^{23}),\quad
\Xi_+=e^{13}-e^{24}+i(e^{14}+e^{23}).
\]

第一式的 $\kappa$ 项抵消，第二式的 $c$ 项抵消。
两式已在 $\mathfrak a,p,q$ 的 12 个实分量、$\kappa,\Re c,\Im c$ 共 15 个实基方向上逐项核对。按原取向，$*\Xi_-=-\Xi_-$、$*\Xi_+=\Xi_+$。

于是附件负手性 off-diagonal 曲率的主项确为

\[
(F^E)_{21}=D_5c\wedge\theta_2-|c|^2\Xi_-
-i(p+3q)\wedge c\theta_2
\]

（再加真实误差项）。自对偶投影精确消除 $|c|^2\Xi_-$。

### 新检验：不能通过正手性 off-diagonal 曲率直接消去 $c$

若改看正手性联络，则

\[
(F^{S^+})_{21}=d\eta+i(\mathfrak a-2p)\wedge\eta
=d\kappa\wedge\theta_1+i\kappa(q-3p)\wedge\theta_1
+\kappa^2\Xi_+.
\]

因此，即使 $p=q=0$ 且 $\kappa$ 为常数，所得也只有
$\kappa^2\Xi_+$，不含剩余分量 $c$。这排除了“用已控制的正手性曲率直接控制 $c$，从而立刻删除 $W^-$ 预算”这一特定捷径。

## 3. 加权符号没有丢失因子 2

设 $\mathcal L(\alpha)=(\alpha\wedge\theta_2)^+$。在附件的自对偶基

\[
\Psi_1=e^{12}+e^{34},\quad\Psi_2=e^{13}-e^{24},\quad
\Psi_3=e^{14}+e^{23}
\]

中，基向量范数平方是 2，矩阵为

\[
L=\frac12\begin{pmatrix}0&0&-i&-1\\1&i&0&0\\-i&1&0&0\end{pmatrix},
\qquad D=\operatorname{diag}(2,1,1).
\]

在 $\Omega_-=e^{12}-e^{34}$、$\Omega(X,Y)=g(JX,Y)$ 以及
$(J\alpha)(X)=-\alpha(JX)$ 的约定下，

\[
J=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}.
\]

精确矩阵等式为

\[
2L^\dagger DL=I-iJ.
\]

左边的 2 来自目标基的内积，故作为几何算子的表达正是
$\mathcal L^*\mathcal D\mathcal L=I-iJ$。若把坐标基错误地当作正交归一基，则会少掉这个因子；原附件没有此错误。

## 4. Bochner 配对的正负号

明确采用对第一槽共轭线性的 Hermitian 内积，并令 $D^*D=\Delta$ 非负。
对实二形式 $\Omega$，$J$ 对一形式的矩阵满足 $J_{ji}=\Omega_{ij}$。
因此 skew 配对为

\[
\langle-iJDc,Dw\rangle
=i\Omega_{ij}\overline{D_i c}\,D_jw.
\]

闭流形上分部积分：

\[
\int i\Omega_{ij}\overline{D_i c}\,D_jw
=\int\bar c\left[-i\Omega_{ij}D_iD_jw
-i(\nabla_i\Omega_{ij})D_jw\right].
\]

由于

\[
\Omega_{ij}D_iD_j=\frac12\Omega_{ij}[D_i,D_j]
=\langle F,\Omega\rangle,
\qquad (\delta\Omega)_j=-\nabla_i\Omega_{ij},
\]

得到

\[
\Re\int\langle Dc-iJDc,Dw\rangle
=\Re\int\left\langle c,
\Delta w-i\langle F,\Omega\rangle w
+i\delta\Omega\cdot Dw\right\rangle.
\]

这里没有使用 $d\Omega=0$ 或 $J^2=-I$。

取 $F=5F_A$、$f=-iF_A^-$、
$\bar\Omega=-4Q_v/m_*$，前置拟合为
$f=-27Q_v/32+o_{L^2}(1)$，且 $|Q_v|^2=m^2/8$。
故

\[
-i\langle5F_A,\bar\Omega\rangle
=5\langle f,\bar\Omega\rangle
\longrightarrow
5\frac{27}{32}\frac4{m_*}\frac{m_*^2}{8}
=\frac{135m_*}{64}=\frac{10}{3}.
\]

两个负系数相乘为正；再经分部积分，势项确实为
$\Delta_{5A}+10/3$。不能将它改成 $\Delta_{5A}-10/3$，也不能将另一三次旋量的 Lichnerowicz 势 $-7$ 移植到此线丛算子。

## 5. 此核验对无界密度问题的准确意义

符号成立意味着新的弱 CR 路线具有真实的正强制算子。它不自动证明所有误差在无界 $W^-$ 预算下仍趋零。具体来说：

* 曲率误差分部积分后包含 $\epsilon_b\,\nabla v\,D_5w$；当前使用的小 $L^2$、有界 $L^4$、有界 $L^4$ 配对依赖 $\nabla v$ 的 $L^4$ 界。
* $D_5c$ 的 $L^2$ 控制依赖 $\nabla^2v$ 和 $|\nabla v|^2$ 的预算。
* 固定幅度截断的最终质量下界 $1-C_B/M^2$ 依赖 $c$ 的 $L^4$ 界。如果这些界随 $B$ 发散，固定 $M$ 的测试不能排除质量向越来越高幅度集中。

以上是分析输入所在的准确位置，不是符号障碍。要删除密度条件，需要对这些项提供独立于 $W^-$ 总预算的新估计或新的测试机制；已控制的正手性 off-diagonal 曲率不直接提供这种估计，因为第 2 节所示的 $c$ 项恰好抵消。

## 6. 保留质量梯度后的径向分量：正曲率中的再次精确抵消

本节检验尝试删除密度界时的一个新短路，并不把理想方程当作近似序列的已证强收敛。

设局部 $v=\sqrt m(1,0)$，令

\[
u=\frac{dm}{2m},\qquad
\nabla_i v=\sqrt m\,(u_i+iq_i,b_i).
\]

取 $Z_1=(e_1-ie_2)/2$、$Z_2=(e_3-ie_4)/2$。在理想条件
$\nabla_{Z_1}v=\nabla_{Z_2}v=D^-v=0$ 下，第一分量给

\[
q=(u_2,-u_1,u_4,-u_3)=-J_+u.
\]

第二分量给 $b_2=-ib_1$、$b_4=-ib_3$，而 Dirac 的第二分量进一步给

\[
\boxed{b=d\theta_1+c\theta_2,\qquad d=-(u_3+iu_4).}
\]

所以，尚未控制 $dm$ 时不能把 $b$ 简化成 $c\theta_2$。
保留此项，且先取正旋量质量 $\rho$ 常数、$p=0$，两条 Cartan 式变成

\[
\boxed{
d\theta_1=-i(\mathfrak a-q)\wedge\theta_1+
\kappa\Xi_+-d\,\theta_1\wedge\theta_2,}
\]

\[
\boxed{
d\theta_2=i(2\mathfrak a-q)\wedge\theta_2-
\bar c\,\Xi_--2i\bar d\,e^{12}.}
\]

这里 $d$ 是一个复系数，微分仍写作 $d\theta_i$；
$\theta_1\wedge\theta_2=\bar\Xi_+$。

因为 $\kappa=\sqrt m/(2\rho^{3/2})$，此时
$d\kappa=\kappa u$。又有

\[
u+iq=(u_1+iu_2)\theta_1+(u_3+iu_4)\theta_2,
\]

从而

\[
(d\kappa+i\kappa q)\wedge\theta_1
=\kappa d\,\theta_1\wedge\theta_2.
\]

代入正联络 off-diagonal 曲率，得到

\[
\begin{aligned}
(F^{S^+})_{21}
&=d\kappa\wedge\theta_1+
\kappa\,d\theta_1+i\mathfrak a\wedge\kappa\theta_1\\
&=(d\kappa+i\kappa q)\wedge\theta_1+
\kappa^2\Xi_+-\kappa d\,\theta_1\wedge\theta_2\\
&=\boxed{\kappa^2\Xi_+.}
\end{aligned}
\]

径向质量梯度贡献与新增的 $d\theta_1$ 联络分量**精确抵消**。
因此，不能先通过这一正手性曲率方程断言第二复平面的 $dm$ 小，再用
$J_+dm=J_-dm$ 把所有漂移吸收到 $m^{-3/2}c$ 中。这会遗漏 Dirac 方程强迫保留的径向分量。

新增脚本已验证两条径向 Cartan 恒等式，并独立验证四个质量梯度基方向上的双线性曲率抵消。此结果与无密度路线的独立计算一致。

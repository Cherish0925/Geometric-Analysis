# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step26_truncation_flux_and_branch_completeness.md",
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md",
    "Sessions/S1003A02/workspace/scripts/ach_projected.py",
    "Sessions/S1003A01/workspace/scripts/perp_cartan_verify.py",
    "Sessions/S1003A02/trace/ttcs/results/step26_ttcs01_generator1_integration.md"
  ]
}
```

## Task

Formulate the b-independent scale-one saturation problem for diagonal Bianchi-IX metrics suggested by the small-b Taub-bolt/Λ-Taub-NUT/ACH transition. The inner limiting state is a Hopf-collapsed Berger/Taub-bolt neck; the terminal condition is the rho=1 standard-CR ACH stable set. Use the complete trace-free Ricci controls H,E,D with cost ∫ r^3(3H^2/16+E^2/6+D^2/8)dt, not D alone. Derive a mathematically executable state-control boundary-value problem, identify symmetries/scalings and the correct b-free entry/exit conditions, and explain how to distinguish a positive saturation payment from arbitrarily cheap steering. Ground the derivation in the provided exact diagonal equations and accumulated notes; do not invent numerical results.

## Output

## 一、几何槽位与完整控制系统

取未来 ACH 端的 Reeb 方向为 \(F=a_f\)，两个接触方向为 \(G=a_g\)、\(C=a_h\)。小 bolt 极限的内端构型是

\[
F\simeq G=A,\qquad C\ll A,
\]

其中 \(C\) 是 Taub-bolt/Λ-Taub-NUT 颈中的 Hopf 小圆；标准 CH 端则满足

\[
G/C\longrightarrow 1,\qquad F/(GC)\longrightarrow 1.
\]

因此这一转变不是单独改变 \(q=\log(G/C)\)，而是从形状空间中的塌缩射线

\[
(\beta,q)\sim \left(\frac q2,q\right),\qquad q\to+\infty
\]

转向标准 CH 射线

\[
q\to0,\qquad \beta\to+\infty .
\]

令

\[
F=re^{2\beta/3},\qquad
G=re^{-\beta/3+q/2},\qquad
C=re^{-\beta/3-q/2},\qquad h=\log r.
\]

记

\[
u=h',\qquad v=\beta',\qquad w=q'.
\]

已有精确公式可写为

\[
\begin{aligned}
D&=-q''-3h'q'+e^{-2h}\mathcal V_D(\beta,q),\\
E&=-\beta''-3h'\beta'+e^{-2h}\mathcal V_E(\beta,q),\\
H&=-2h''-\frac23(\beta')^2-\frac12(q')^2
    +e^{-2h}\mathcal V_H(\beta,q),
\end{aligned}
\]

其中

\[
\begin{aligned}
\mathcal V_D&=
8\left(e^{-4\beta/3}\sinh 2q-e^{2\beta/3}\sinh q\right),\\
\mathcal V_E&=
4e^{8\beta/3}-4e^{2\beta/3}\cosh q
-8e^{-4\beta/3}\sinh^2q,\\
\mathcal V_H&=
\frac23e^{8\beta/3}-\frac83e^{2\beta/3}\cosh q
+\frac83e^{-4\beta/3}\sinh^2q.
\end{aligned}
\]

于是完整状态控制方程为

\[
\begin{aligned}
h'&=u,&
\beta'&=v,&
q'&=w,\\
u'&=-\frac12H-\frac13v^2-\frac14w^2+\frac12e^{-2h}\mathcal V_H,\\
v'&=-3uv+e^{-2h}\mathcal V_E-E,\\
w'&=-3uw+e^{-2h}\mathcal V_D-D.
\end{aligned}
\tag{1}
\]

精确作用量是

\[
\widehat P
=
\int r^3\left(
\frac3{16}H^2+\frac16E^2+\frac18D^2
\right)\,dt.
\tag{2}
\]

这里 \(D\) 控制两个未来接触方向的差异，\(E\) 控制未来 Reeb 方向相对于接触平面的形状，而 \(H\) 控制径向方向与轨道平均方向之间的差异。只保留 \(D\) 会遗漏塌缩槽位重新排列所必需的两个通道。

---

## 二、消去整体尺度后的 \(b\)-无关系统

引入尺度不变时间和动量

\[
d\tau=\frac{dt}{r},\qquad
p=rh',\qquad
\xi=r\beta',\qquad
\eta=rq',
\]

以及尺度不变控制

\[
\bar H=r^2H,\qquad
\bar E=r^2E,\qquad
\bar D=r^2D.
\]

以点表示 \(d/d\tau\)，则形状状态

\[
Y=(\beta,q,p,\xi,\eta)
\]

满足自主系统

\[
\boxed{
\begin{aligned}
\dot\beta&=\xi,\\
\dot q&=\eta,\\
\dot p&=
p^2-\frac13\xi^2-\frac14\eta^2
+\frac12\mathcal V_H-\frac12\bar H,\\
\dot\xi&=-2p\xi+\mathcal V_E-\bar E,\\
\dot\eta&=-2p\eta+\mathcal V_D-\bar D.
\end{aligned}}
\tag{3}
\]

同时

\[
\boxed{
\widehat P=
\int
\left(
\frac3{16}\bar H^2+
\frac16\bar E^2+
\frac18\bar D^2
\right)d\tau .
}
\tag{4}
\]

方程 (3)–(4) 不含 \(h\)、bolt 半径 \(b\) 或任何绝对长度。这正是所需的尺度一饱和问题。

整体伸缩

\[
t\mapsto \lambda t,\qquad
(F,G,C)\mapsto\lambda(F,G,C)
\]

只改变 \(h\mapsto h+\log\lambda\)，而 \(Y,\tau,\bar H,\bar E,\bar D\) 及作用量均不变。另有：

* \(\tau\)-平移对称性；
* 交换 \(G,C\) 时
  \[
  q\mapsto-q,\quad \eta\mapsto-\eta,\quad \bar D\mapsto-\bar D;
  \]
* 三个轨道槽位的循环置换，但 \(O(-1)\) bolt 槽位与未来 Reeb 槽位一旦选定，就对应不同的几何扇区。

---

## 三、正确的 Hopf 塌缩入端

设内端 Λ-Taub-NUT 颈写成

\[
F=G=A,\qquad C=\varepsilon A,\qquad \varepsilon\downarrow0.
\]

记尺度不变的一阶数据

\[
U=A',\qquad V=A\,\frac{C'}{C}.
\]

则

\[
q=\log\frac1\varepsilon,\qquad
\beta=\frac12\log\frac1\varepsilon
\]

以及

\[
\boxed{
\begin{aligned}
p&=\varepsilon^{1/3}\frac{2U+V}{3},\\
\xi&=\varepsilon^{1/3}\frac{U-V}{2},\\
\eta&=\varepsilon^{1/3}(U-V).
\end{aligned}}
\tag{5}
\]

所以入端族为

\[
I_\varepsilon(A)=
\left(
\frac12\log\varepsilon^{-1},
\log\varepsilon^{-1},
\varepsilon^{1/3}\frac{2U(A)+V(A)}3,
\varepsilon^{1/3}\frac{U(A)-V(A)}2,
\varepsilon^{1/3}(U(A)-V(A))
\right).
\tag{6}
\]

在已有 Λ-Taub-NUT 匹配中，

\[
A(s)=\frac{\sinh(\sqrt2s)}{\sqrt2},\qquad
U(A)=\sqrt{1+2A^2},\qquad
V(A)=\frac{2A^2}{\sqrt{1+2A^2}}.
\tag{7}
\]

且

\[
\varepsilon_b(A)
=
\frac{C}{A}
=
\frac{2b}{\sqrt3}\frac{U(A)}A+o(b).
\tag{8}
\]

因此对任意固定 \(0<A_-<A<A_+<\infty\)，令 \(b\to0\) 等价于令 \(\varepsilon\to0\)；方程和作用量中已无 \(b\)。

入端并非任意 Hopf 塌缩 Berger 数据。它还必须满足

\[
F/G\to1,\qquad
\frac{\xi-\eta/2}{\varepsilon^{1/3}}\to0,
\]

以及 (5) 给出的 Taub-bolt/Λ-Taub-NUT 一阶射线。若把所有有界 Berger 一阶数据都放进入端，所得变分值会混入并非来自小 bolt 匹配的几何。

### 塌缩射线的正则化

令

\[
x=\beta-\frac q2=\log(F/G),\qquad
z=e^{-q/3}=\varepsilon^{1/3}.
\]

则入端为

\[
z\to0,\qquad x\to0,\qquad
(p,\xi,\eta)=
z\left(\frac{2U+V}{3},\frac{U-V}{2},U-V\right).
\]

沿 \(x=0\)，

\[
\begin{aligned}
\mathcal V_D&=4(z^2-z^8),\\
\mathcal V_E&=2(z^2-z^8),\\
\mathcal V_H&=-\frac83z^2+\frac23z^8.
\end{aligned}
\tag{9}
\]

这些精确消去说明 Hopf 塌缩射线本身是正则的。真正的快速不稳定方向是 \(x=\log(F/G)\)。若

\[
\chi=\xi-\frac{\eta}{2},
\]

则

\[
\dot x=\chi,
\]

且

\[
\dot\chi
=
-2p\chi+\mathcal V_x-\bar E+\frac12\bar D,
\tag{10}
\]

其中

\[
\boxed{
\mathcal V_x=
4z^{-4}
\left(e^{8x/3}-e^{-4x/3}\right)
+
4z^2
\left(e^{-4x/3}-e^{2x/3}\right).
}
\tag{11}
\]

因此

\[
\mathcal V_x=16z^{-4}x+O(z^{-4}x^2+z^2x).
\]

这正是塌缩颈中增长率 \(4/C\) 的尺度无关形式。它也显示，驱动未来 Reeb 槽位形成的控制是

\[
-\bar E+\frac12\bar D,
\]

而不是 \(\bar D\) 单独一个分量。对固定的有效输入

\[
a=-\bar E+\frac12\bar D,
\]

在

\[
\frac16\bar E^2+\frac18\bar D^2
\]

下的最小代价为

\[
\frac18a^2,
\]

由

\[
\bar E=-\frac34a,\qquad
\bar D=\frac12a
\]

实现。即使这两个形状通道达到最优配比，\(\bar H\) 仍需处理相伴随的体积加速度。

---

## 四、标准 CR 出端的精确表达

固定一个足够小的 ACH 截面 \(\zeta=\zeta_*>0\)。由

\[
\zeta=\frac1{GC}=e^{-2h+2\beta/3}
\]

可消去 \(h\)：

\[
h=\frac{\beta}{3}-\frac12\log\zeta_*.
\]

尺度状态 \(Y\) 在该截面对应于紧化 ACH 状态

\[
\mathcal A_{\zeta_*}(Y)=
(y_f,y_g,y_h,\kappa,q,\zeta_*),
\]

其中

\[
\boxed{
\begin{aligned}
y_f&=\sqrt{\zeta_*}\,e^{-\beta/3}
\left(p+\frac23\xi\right),\\
y_g&=\sqrt{\zeta_*}\,e^{-\beta/3}
\left(p-\frac13\xi+\frac12\eta\right),\\
y_h&=\sqrt{\zeta_*}\,e^{-\beta/3}
\left(p-\frac13\xi-\frac12\eta\right),\\
\kappa&=\sqrt{\zeta_*}\,e^\beta .
\end{aligned}}
\tag{12}
\]

令 \(\Sigma_{\mathrm{std}}(\zeta_*)\) 为归一化 \(\operatorname{Ric}=-6g\) 紧化 Einstein 流在该截面上的标准 CR 稳定集：

\[
W\in\Sigma_{\mathrm{std}}(\zeta_*)
\]

当且仅当：

1. \(W\) 满足 Einstein Hamilton 关系；
2. 从 \(W\) 向外积分无控制紧化方程；
3. 轨道趋于
   \[
   E(0)=(2,1,1,1,0,0).
   \]

第三项等价于非线性极限量

\[
\Phi_\infty=0,\qquad \rho_\infty=1.
\]

有限 \(\zeta_*\) 处只设

\[
\widetilde\Phi
=
q+\frac14(y_g-y_h)-\zeta\sinh q=0
\]

并不充分，因为仍有 \(O(\zeta_*^2)\) 的自由漂移。可执行实现应使用三个精确残量：

\[
\mathcal R(W)=
\bigl(
\mathcal U_+(W),\,
\Phi_\infty(W),\,
\mathcal C(W)
\bigr),
\tag{13}
\]

其中 \(\mathcal U_+\) 是非线性外出模系数，\(\mathcal C\) 是 Einstein Hamilton 量。于是尺度商上的出端集合为

\[
\boxed{
\overline\Sigma_{\mathrm{std}}(\zeta_*)
=
\left\{
Y:\mathcal R(\mathcal A_{\zeta_*}(Y))=0
\right\}.
}
\tag{14}
\]

它可由 \(E(0)\) 的 \(-2,-4,-6\) 模向内参数化；固定 \(\zeta_*\) 后，径向相位被消去，通常留下二维稳定片。

若要求直接接到精确 CH，而不是一般标准 CR Einstein 尾部，可把 (14) 换成精确 CH 状态

\[
H(\zeta_*)=
\left(
\sqrt{1+\zeta_*}+\frac1{\sqrt{1+\zeta_*}},
\sqrt{1+\zeta_*},
\sqrt{1+\zeta_*},
\sqrt{1+\zeta_*},
0,\zeta_*
\right).
\tag{15}
\]

前一种表述与 Theorem T 配合：标准 CR Einstein 尾部可在越来越远处截成精确 CH，附加作用量趋于零。

---

## 五、尺度一饱和值

固定尺度一相位区间

\[
K=[A_-,A_+]\Subset(0,\infty).
\]

定义

\[
\boxed{
\begin{aligned}
\mathcal V_{\mathrm{sat}}(K)
=
\liminf_{\varepsilon\downarrow0}
\inf\Bigg\{&
\int_0^T
\left(
\frac3{16}\bar H^2+
\frac16\bar E^2+
\frac18\bar D^2
\right)d\tau:\\
&
Y(0)=I_\varepsilon(A),\quad A\in K,\quad
Y(T)\in\overline\Sigma_{\mathrm{std}}(\zeta_*),\quad T>0,\\
&
Y\ \text{满足}\ (3)
\Bigg\}.
\end{aligned}}
\tag{16}
\]

这一定义包含三个必要特征：

* 小 bolt 只通过 \(\varepsilon\to0\) 出现；
* 饱和相位 \(A\) 保留为有限参数；
* 从 Hopf 塌缩槽位到标准 CR 稳定集的全部 \(H,E,D\) 支付均计入。

实际小 bolt Einstein 分支在入端带有指数微小的 \(F/G-1\)。在有限 \(\varepsilon\) 问题中，可加入对应符号的 \(o(1)\) 初始扰动。由于塌缩不稳定模会放大极小种子，不能预先把任意 \(O(1)\) 饱和状态免费加入 \(I_\varepsilon\)。正确的放松入端应由有限 \(\varepsilon\) 最优值的极限，或由塌缩区线性二次可达分析推导。

---

## 六、可直接计算的极值方程

写无控制漂移为 \(F(Y)\)，控制矩阵为

\[
B=
\begin{pmatrix}
0&0&0\\
0&0&0\\
-\frac12&0&0\\
0&-1&0\\
0&0&-1
\end{pmatrix},
\qquad
R=\operatorname{diag}\left(\frac3{16},\frac16,\frac18\right).
\]

Pontryagin Hamilton 量取为

\[
\mathcal H
=
\lambda\cdot(F(Y)+B\bar u)+\bar u^{T}R\bar u,
\qquad
\bar u=(\bar H,\bar E,\bar D).
\]

逐点极小化给出

\[
\boxed{
\bar H=\frac43\lambda_p,\qquad
\bar E=3\lambda_\xi,\qquad
\bar D=4\lambda_\eta .
}
\tag{17}
\]

将其代回后得到十维状态—协态双端系统。自由时长给出 \(\mathcal H=0\)；入端相位 \(A\) 自由时，协态与 \(\partial_A I_\varepsilon\) 正交；出端协态位于 \(\overline\Sigma_{\mathrm{std}}\) 的法方向。由此可采用多重射击、配点或区间 Taylor 模型。

数值实现宜使用

\[
x=\beta-\frac q2,\qquad z=e^{-q/3}
\]

及式 (9)、(11) 的因式分解形式，避免 \(z^{-4}\) 大项之间的浮点消去。

---

## 七、正饱和支付与任意廉价转向如何分开

### 1. 零作用量轨道

若存在无控制轨道

\[
\bar H=\bar E=\bar D=0
\]

从塌缩入端的适当外出芽连接到
\(\overline\Sigma_{\mathrm{std}}\)，则

\[
\mathcal V_{\mathrm{sat}}(K)=0.
\]

这就是小 bolt 极限中标准 CR Einstein 连接的尺度商表达。

但不存在一条精确连接仍不足以推出正值，因为轨道可能停留越来越久，或借助塌缩不稳定模用越来越小的控制改变外出相位。

### 2. 塌缩区线性二次可达量

沿一条无控制参考轨道 \(\bar Y\)，线性化为

\[
\delta\dot Y=A(\tau)\delta Y+B\,\delta\bar u.
\]

其加权 Gram 矩阵为

\[
\mathcal G_T=
\int_0^T
\Psi(T,s)\,
B R^{-1}B^T\,
\Psi(T,s)^T\,ds,
\tag{18}
\]

其中

\[
BR^{-1}B^T
=
\operatorname{diag}_{(p,\xi,\eta)}
\left(\frac43,6,8\right).
\]

把 \(\mathcal G_T\) 投影到标准稳定集的三个法方向，即外出模、\(\Phi_\infty\) 和 Hamilton 量方向：

* 若相应 Gram 特征值随 \(\varepsilon\to0\) 发散，固定的端点偏移可能由趋零作用量实现；这会产生显式廉价控制族。
* 若投影 Gram 矩阵保持有限，而无控制外出族与标准稳定集之间保持非零分离，则线性化支付为正。非线性正下界还需控制离开参考管状区的轨道。

这一步尤其会决定“指数微小种子免费选择饱和相位”的程度，而不会把任意饱和状态直接假定为免费。

### 3. Hamilton–Jacobi 下界

设 \(S(Y)\) 是一个 \(C^1\) 函数。若在所有相关状态上

\[
\boxed{
F(Y)\cdot\nabla S
+\frac13S_p^2
+\frac32S_\xi^2
+2S_\eta^2
\le0,
}
\tag{19}
\]

则对任意控制轨道都有

\[
\widehat P\ge S(Y(T))-S(Y(0)).
\tag{20}
\]

因此若

\[
\inf_{\overline\Sigma_{\mathrm{std}}}S
-
\sup_{\mathcal I_{\mathrm{col}}}S
=c>0,
\]

便得到

\[
\mathcal V_{\mathrm{sat}}(K)\ge c.
\]

式 (19) 已经把三个控制通道逐点消去，适合用低阶多项式、分片有理函数和区间算术构造。

### 4. 显式廉价族

要证明任意廉价转向，最直接的对象是一族

\[
(h_\varepsilon,\beta_\varepsilon,q_\varepsilon)
\]

满足正确入端与标准稳定出端，并由精确公式计算

\[
H_\varepsilon,\ E_\varepsilon,\ D_\varepsilon,
\]

使得

\[
\int r_\varepsilon^3
\left(
\frac3{16}H_\varepsilon^2+
\frac16E_\varepsilon^2+
\frac18D_\varepsilon^2
\right)dt\longrightarrow0.
\tag{21}
\]

仅证明 \(D_\varepsilon\) 的积分趋零没有决定性，因为快速形状旋转通常把代价转移到 \(E_\varepsilon\)，相伴随的径向加速度又进入 \(H_\varepsilon\)。

### 5. 手征通量的辅助作用

Hopf 塌缩入端具有

\[
(\mathfrak b_+,\mathfrak b_-)\longrightarrow(-2,2).
\]

对任意中间轨道，手征 transgression 给出

\[
\widehat P\ge
\mathfrak b_\pm(T)-\mathfrak b_\pm(0).
\]

它会立即排除先开成近圆球、再进入 CH 的普通解塌缩路径。高剪切路径可以令手征通量下降，因此该通量适合把状态压入一个高剪切区域，而区域内部的支付由 (19) 或完整最优控制系统处理。

---

由此，小 \(b\) 问题被压缩成一个明确的 \(b\)-无关对象：从 compactified Hopf 塌缩 Taub-bolt/Λ-Taub-NUT 入端 \(I_\varepsilon(A)\) 出发，在完整三控制系统 (3) 中到达投影后的 \(\rho=1\) ACH Einstein 稳定集，并计算极限值 (16)。正支付对应一个严格正的动态规划值；任意廉价转向则必须表现为无控制连接、塌缩 Gram 增益发散，或一族满足 (21) 的完整三分量构造。
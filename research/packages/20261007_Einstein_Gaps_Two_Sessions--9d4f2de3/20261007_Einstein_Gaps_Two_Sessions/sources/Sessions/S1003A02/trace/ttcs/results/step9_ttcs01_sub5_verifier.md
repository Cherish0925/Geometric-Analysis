# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step6_perpendicular_dual_cost_and_relative_calibration.md",
    "Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md",
    "Sessions/S1003A02/workspace/data/o11perp/profile_perp_smooth_x0.03.csv",
    "Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md"
  ]
}
```

## Task

Analyze the exact relative calibration and transgression results from peer Session S1003A01 together with the perpendicular cell profile and the active Einstein-gap goal. Explain whether the decomposition P/(8π²)-1 = three nonnegative squares + ∫2u1u2u3/λ2 can plausibly yield a general lower bound in the perpendicular SU(2)-invariant sector, what matrix Hardy/Riccati inequality would be needed, and how the first-order cancellation R^+ζ=0 enters. Compare its mathematical value to brute-force Hessian computations. Identify a concrete inequality or transformed variable that could control the cubic term by the endpoint data and squares without losing an O(x0) term.

## Output

## 科学核验备忘录

### 1. 精确相对校准确实把问题压缩到了一个临界的积分不等式

记
\[
\begin{aligned}
E_1&=\dot u_1+\frac{2u_1+u_2u_3}{\lambda_1},\\
E_2&=\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2},\\
E_3&=\dot u_3+\frac{2u_3+u_1u_2}{\lambda_3}.
\end{aligned}
\]
Step 6 的恒等式是
\[
\boxed{
\frac{P}{8\pi^2}-1
=
\int\left(
\frac{\lambda_1}{4}E_1^2+
\frac{\lambda_2}{4}E_2^2+
\frac{\lambda_3}{4}E_3^2+
\frac{2u_1u_2u_3}{\lambda_2}
\right)dt .}
\tag{1}
\]
这里的常数 \(1\) 来自相对校准
\[
\Phi=C-u_2^2,\qquad
\Phi_{\rm bolt}=1,\quad \Phi_{\rm CH}=0,
\]
而不是人为插入的估计常数。因此，只要控制最后的三次项，就会得到精确阈值
\[
P\ge 8\pi^2.
\]

这不是逐点正性问题。\(x_0=.01\) 的近极值剖分给出
\[
\mathcal S_1+\mathcal S_2+\mathcal S_3
=0.003428047,\qquad
\mathcal C_3=-0.00143166,
\]
所以三次项抵消了平方和约 \(41.8\%\)，剩余
\[
0.0019963874=\frac{P}{8\pi^2}-1.
\]
因此，任何把三次项当作“小误差”的论证都没有反映实际近极值机制。

相对校准的几何设置也与给出的 \(x_0=.03\) 剖面一致。CSV 首行满足
\[
G=F=h_{11}=0,\qquad h_{22}=h_{33}=x_0,
\]
且
\[
G'(x_0)F'(x_0)
=
0.9675596867\cdot1.0335279712
\approx1,
\]
这是光滑 bolt 的锥角关系；同时 \(h_{33}'(x_0)=1\)，故
\(h_{33}-x=O((x-x_0)^2)\)，符合 `wpow=2`。在 \(x=1\) 处，
\[
G=2,\ G'=3,\ G''=2,\qquad
(h_{11},h_{22},h_{33})=(1,1,2),
\]
及其一、二阶导数都与 CH 数据吻合。因而循环重标
\[
(a,b,c)=(\sqrt{x},\sqrt{xe^w},\sqrt F)
\]
确实消除了旧坐标在 bolt 处的表观奇性，并给出
\[
u_{\rm bolt}=(0,0,-1),\qquad u_{\rm CH}=(0,3X,0).
\]

同一批数值中，\(x_0=.03\) 的电荷最低值约为
\(\mathcal T/(8\pi^2)=0.11848\)，所以这里没有强制零电荷切片。相对校准的价值正在于：它不需要零电荷穿越，而是追踪从 \(u_3\) 轴到 \(u_2\) 轴的电荷转移。

---

### 2. 所需的矩阵 Hardy/Riccati 结构

把
\[
\eta=\binom{u_1}{u_3},\qquad
A=\frac14
\begin{pmatrix}
\lambda_1&0\\
0&\lambda_3
\end{pmatrix},
\]
并定义
\[
K=
\begin{pmatrix}
2/\lambda_1&u_2/\lambda_1\\
u_2/\lambda_3&2/\lambda_3
\end{pmatrix},
\qquad
N=\frac{u_2}{\lambda_2}
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
则第一、第三平方连同三次项恰好组成
\[
\boxed{
\mathcal Q_\perp[\eta]
=
\int\left[
(\dot\eta+K\eta)^TA(\dot\eta+K\eta)
+\eta^TN\eta
\right]dt .}
\tag{2}
\]
因为
\[
\eta^TN\eta=\frac{2u_1u_2u_3}{\lambda_2},
\]
所以
\[
\frac{P}{8\pi^2}-1
=
\mathcal Q_\perp[\eta]
+\int\frac{\lambda_2}{4}E_2^2dt.
\tag{3}
\]

最干净、略强于所需结论的矩阵 Hardy 命题是
\[
\boxed{\mathcal Q_\perp[\eta]\ge0}
\tag{4}
\]
对所有光滑 bolt—CH 数据成立。若 (4) 太强，精确所需形式只是
\[
\mathcal Q_\perp[\eta]
\ge
-\int\frac{\lambda_2}{4}E_2^2dt.
\tag{5}
\]

一个足以推出 (4) 的 Riccati 完平方如下。若存在对称矩阵
\(\Gamma(t)\)，使
\[
\boxed{
\mathfrak R_\Gamma:=
N-\dot\Gamma+K^T\Gamma+\Gamma K-\Gamma A^{-1}\Gamma
\succeq0,}
\tag{6}
\]
则有精确恒等式
\[
\begin{aligned}
\mathcal Q_\perp[\eta]
={}&
\int
\bigl(\dot\eta+K\eta-A^{-1}\Gamma\eta\bigr)^T
A
\bigl(\dot\eta+K\eta-A^{-1}\Gamma\eta\bigr)\,dt\\
&+\int\eta^T\mathfrak R_\Gamma\eta\,dt
+\bigl[\eta^T\Gamma\eta\bigr]_{\rm bolt}^{\rm collar}.
\end{aligned}
\tag{7}
\]
CH 端有 \(\eta=0\)，bolt 端有 \(\eta=(0,-1)\)，故端点项等于
\[
-\Gamma_{33}({\rm bolt}).
\]
于是
\[
\Gamma_{33}({\rm bolt})\le0
\tag{8}
\]
与 (6) 一起便给出 \(\mathcal Q_\perp\ge0\)。在 bolt 处
\(A\) 退化，(6) 应按光滑 bolt 展开取极限；CSV 中的
\(G'F'=1\) 和 \(w=O((x-x_0)^2)\) 正好提供所需的正则渐近。

把 (2) 展开为通常的 Sturm 形式也很有用。由于
\[
B=AK=\frac14
\begin{pmatrix}
2&u_2\\
u_2&2
\end{pmatrix},
\]
有
\[
\mathcal Q_\perp
=
\bigl[\eta^TB\eta\bigr]_{\rm bolt}^{\rm collar}
+\int\left(\dot\eta^TA\dot\eta+\eta^TV\eta\right)dt,
\tag{9}
\]
其中
\[
V=K^TAK-\dot B+N,
\]
即
\[
V=
\begin{pmatrix}
\displaystyle \frac1{\lambda_1}+\frac{u_2^2}{4\lambda_3}
&
\displaystyle
\frac{u_2}{2}\!\left(\frac1{\lambda_1}+\frac1{\lambda_3}\right)
+\frac{u_2}{\lambda_2}-\frac{\dot u_2}{4}
\\[2mm]
\displaystyle
\frac{u_2}{2}\!\left(\frac1{\lambda_1}+\frac1{\lambda_3}\right)
+\frac{u_2}{\lambda_2}-\frac{\dot u_2}{4}
&
\displaystyle \frac1{\lambda_3}+\frac{u_2^2}{4\lambda_1}
\end{pmatrix}.
\tag{10}
\]
若 \(R=\Gamma-B\)，则 (6) 等价于
\[
\boxed{V-\dot R-RA^{-1}R\succeq0.}
\tag{11}
\]

更几何地，设 \(Y\) 是矩阵 Jacobi 方程
\[
-(A\dot Y)^{\cdot}+VY=0
\tag{12}
\]
的可逆 Lagrangian 基解，并令
\[
R=A\dot YY^{-1}.
\]
则
\[
\dot R+RA^{-1}R=V,
\tag{13}
\]
且在 \(\eta=Yz\) 下，
\[
\boxed{
\mathcal Q_\perp
=
\int \dot z^T\,Y^TAY\,\dot z\,dt
+\bigl[\eta^T(B+R)\eta\bigr]_{\rm bolt}^{\rm collar}.}
\tag{14}
\]
因此真正的解析对象是一个从正则 bolt 数据延伸到 CH 数据而始终可逆的矩阵 Jacobi 场，或一个满足 (6) 的显式矩阵函数。仅数值积分出某条剖面的 \(R\) 仍只对应那条剖面；一般下界需要从 \(a_i,u_i\) 的结构推出 (6) 和端点符号。

Step 6 的修正项
\[
\psi=-\frac{a_2^2}{a_1a_3}u_1u_3
\]
正是矩阵语言中的一个非对角二次型：
\[
\psi=\eta^T
\begin{pmatrix}
0&-\frac{a_2^2}{2a_1a_3}\\[1mm]
-\frac{a_2^2}{2a_1a_3}&0
\end{pmatrix}\eta.
\]
其剩余式含混合二、三、四次项，说明单独调节一个非对角系数不够；完整的 \(2\times2\) Riccati 矩阵允许两个对角系数与一个非对角系数共同演化，正好是自然的下一层结构。

---

### 3. CH 段上的标量 ground-state 变换可以完全处理变号势

在精确 CH 段，
\[
\lambda_1=\lambda_3,\qquad u_2=3x,
\]
以
\[
v_\pm=u_1\pm u_3
\]
对角化后得到
\[
\mathcal Q_\pm[v]
=
\int\left[p(x)(v')^2+V_\pm(x)v^2\right]dx,
\qquad
p(x)=\frac{x(1+x)}4,
\]
其中
\[
V_+=\frac{4+18x+15x^2}{16x(1+x)},\qquad
V_-=\frac{4-18x+3x^2}{16x(1+x)}.
\]
\(V_-\) 在
\[
x=\frac{9-\sqrt{69}}3\approx0.231
\]
之后改变符号，所以逐点势能估计确实不可行。

但两个 Sturm 方程都有显式正解：
\[
y_+(x)=x(1+x)^{1/2},\qquad
y_-(x)=x(1+x)^{-5/2},
\]
并且
\[
-(py_\pm')'+V_\pm y_\pm=0.
\]
因此有精确分解
\[
\boxed{
\mathcal Q_\pm[v]
=
\int p\,y_\pm^2
\left[\left(\frac{v}{y_\pm}\right)'\right]^2dx
+
\left[p\frac{y_\pm'}{y_\pm}v^2\right]_{\rm in}^{\rm out}.}
\tag{15}
\]
这里
\[
p\frac{y_+'}{y_+}=\frac{2+3x}{8},\qquad
p\frac{y_-'}{y_-}=\frac{2-3x}{8}.
\]

特别地，定义
\[
\boxed{
z_+=\frac{v_+}{x\sqrt{1+x}},\qquad
z_-=\frac{(1+x)^{5/2}}{x}\,v_-,
}
\tag{16}
\]
则
\[
\boxed{
\mathcal Q_+
=
\int\frac{x^3(1+x)^2}{4}(z_+')^2dx
+
\left[\frac{2+3x}{8}v_+^2\right]_{\rm in}^{\rm out},
}
\tag{17}
\]
\[
\boxed{
\mathcal Q_-
=
\int\frac{x^3}{4(1+x)^4}(z_-')^2dx
+
\left[\frac{2-3x}{8}v_-^2\right]_{\rm in}^{\rm out}.
}
\tag{18}
\]

这是一个具体且不损失一阶信息的答案：三次相互作用已经包含在
\(\mathcal Q_-\) 的变号势中，而 (18) 把它精确转化为一个平方与端点通量。没有使用
\[
|u_1u_3|\le \tfrac12(u_1^2+u_3^2)
\]
之类会抹去自旋方向信息的估计。

若精确 CH 段从 \(x=a\) 开始，并且外端 \(v_\pm=0\)，则
\[
\mathcal Q_+
=
\int_a^{x_{\rm out}}\frac{x^3(1+x)^2}{4}(z_+')^2dx
-\frac{2+3a}{8}v_+^2(a),
\tag{19}
\]
\[
\mathcal Q_-
=
\int_a^{x_{\rm out}}\frac{x^3}{4(1+x)^4}(z_-')^2dx
-\frac{2-3a}{8}v_-^2(a).
\tag{20}
\]
所以一个非常具体的内区迹不等式是
\[
\boxed{
\mathcal E_{\rm inner}(a)
\ge
\frac{2+3a}{8}v_+^2(a)
+
\frac{2-3a}{8}v_-^2(a),
}
\tag{21}
\]
其中保留 \(\lambda_2E_2^2/4\) 项。矩阵形式就是：内区的 Dirichlet-to-Neumann 二次型支配 CH 的 Riccati 端点矩阵
\[
\operatorname{diag}\!\left(\frac{2+3a}{8},\frac{2-3a}{8}\right)
\]
于 \(v_\pm\) 基底中。式 (21) 的一阶等号方向应当正是 perpendicular 通道，而二阶差值决定有限 \(x_0\) 的阈值余量。

---

### 4. 第三个平方本身不能解决三次项

由 \(E_2\) 的定义，
\[
u_1u_3=2u_2-\lambda_2\dot u_2+\lambda_2E_2.
\]
于是
\[
\boxed{
\frac{\lambda_2}{4}E_2^2
+\frac{2u_1u_2u_3}{\lambda_2}
=
\frac{\lambda_2}{4}
\left(
\dot u_2+\frac{2u_2+u_1u_3}{\lambda_2}
\right)^2
-\frac{d}{dt}(u_2^2).
}
\tag{22}
\]
积分后，端点给出
\[
-[u_2^2]_{\rm bolt}^{\rm CH}=-9X^2.
\]
这正是 outgoing CH 电荷。式 (22) 说明：仅把三次项和 \(E_2\) 平方重组，会退回绝对电荷问题，并产生一个阶数为 \(1\) 的端点量；相对校准 \(C-u_2^2\) 的选择不可替换。真正的小量来自横向 \(v_\pm\) 的 Dirichlet-to-Neumann 匹配，而不是从 \(u_2\) 通道单独获得。

---

### 5. \(R^+\zeta=0\) 在这里表现为临界 Jacobi 通道

Step 8 的一阶律为
\[
\frac{P}{8\pi^2}
=
1-x_0R^+(\zeta,\zeta)+O(x_0^2),
\]
而 CH 上
\[
R^+=W^++\frac{s}{12}
=\operatorname{diag}(-6,0,0)
\]
于 \((\omega_{\rm CH},\omega_2,\omega_3)\) 基底中。因此
\[
-x_0R^+(\zeta,\zeta)=6x_0\cos^2\theta.
\]
当 \(\zeta\perp\omega_{\rm CH}\) 时，
\[
R^+\zeta=0,
\qquad
\frac{P}{8\pi^2}-1=O(x_0^2).
\]

在 Riccati/Sturm 语言中，这意味着最低横向通道是临界的：内区 Riccati 通量与 CH 的 \(v_-\) 通量在 \(O(x_0)\) 阶必须完全匹配。显式函数
\[
y_-(x)=\frac{x}{(1+x)^{5/2}}
\]
是该 CH 通道的正 Jacobi 解；它不必单独满足两个端点条件，但给出了精确的 ground-state 权函数和对数导数
\[
\frac{y_-'}{y_-}
=
\frac{2-3x}{2x(1+x)}.
\]
因而 \(R^+\zeta=0\) 不是三次项偶然变小，而是矩阵 Hardy 二次型出现临界方向。任何要求
\[
\mathcal E_{\rm inner}
\ge
\mathcal E_{\rm CH}+c\,x_0
\]
且 \(c>0\) 与 perpendicular 方向无关的估计，都会与这个 Jacobi 匹配及数值尺度冲突。

数值也符合这一点：
\[
\begin{array}{c|c}
x_0 & P/(8\pi^2)-1\\ \hline
0.003 & 1.21\times10^{-4}\\
0.01 & 1.94\text{--}2.00\times10^{-3}\\
0.03 & 1.79\text{--}1.90\times10^{-2}
\end{array}
\]
这些值约为 \(10\text{--}20\,x_0^2\)，虽然现有数据尚不能区分
\(x_0^2\) 与 \(x_0^2\log(1/x_0)\)。

---

### 6. 相对校准与 brute-force Hessian 的数学价值不同

1. **相对校准是全振幅恒等式。**  
   式 (1) 对整个 fixed-slot 对角 Bianchi-IX 路径成立，不依赖某个有限维多项式参数化，也不依赖局部驻点。

2. **它保留拓扑阈值。**  
   bolt 的相对值为 \(1\)，CH 的相对值为 \(0\)，故 \(8\pi^2\) 系数直接来自 transgression。若证明矩阵 Hardy 不等式，就得到该扇区所有剖面的 \(P\ge8\pi^2\)，继而由
   \[
   J=P+\frac14\int(s+24)^2dV
   \]
   得到 \(J\ge8\pi^2\)。

3. **Hessian 对参数化非常敏感。**  
   Step 8 已经展示：diabatic ansatz 强制
   \(h_{13}=\phi(F-x)=0\) 于特征值交叉点，因而制造了 \(O(x_0)\) 的旋转代价；fixed-slot 剖面移除了这个约束，并恢复 \(R^+\zeta=0\) 的一阶消失。局部 Hessian 的系数若脱离正确的特征线延拓，可以反映 ansatz 伪效应。

4. **Hessian 仍有明确用途。**  
   在 fixed-slot 类中，谱 Hessian 可以近似矩阵 Sturm 算子的最低特征值、定位接近共轭点的位置，并数值生成 Riccati 权函数。它适合测量二阶系数与测试候选 \(\Gamma\)，但单独不能覆盖远离驻点的非线性路径。

5. **校准揭示了真正需要证明的对象。**  
   不是“所有点上三次项符号有利”，而是矩阵 Jacobi 场在 bolt—CH 传输中保持可逆，并且其端点二次型满足 (8) 或等价的迹估计 (21)。

---

### 7. 综合判断

这套分解很有希望给出 perpendicular fixed-slot 对角 SU(2) 类中的一般下界，但其合理形式是一个**临界半正定 Hardy 定理**，不是带统一线性余量的估计。最具体的可用结构是：

- CH 上的精确变量
  \[
  z_-=\frac{(1+x)^{5/2}}{x}(u_1-u_3),
  \]
  以及恒等式 (18)；
- 过渡区上的矩阵 Riccati 不等式 (6)；
- 或等价的内区迹比较 (21)，并要求 perpendicular 通道在一阶达到等号。

尚缺的数学对象是一个满足 bolt 正则渐近、穿过整个过渡区且不产生 Riccati 极点的显式 \(2\times2\) 矩阵权，或一个直接证明内区 Dirichlet-to-Neumann 形式支配 CH 形式的比较定理。现有剖面、平方分解和 CH ground-state 因子化都与该结构相容；它们同时解释了为何粗糙 Young 估计会虚构 \(O(x_0)\) 代价，以及为何 \(R^+\zeta=0\) 必须作为精确零模信息保留。
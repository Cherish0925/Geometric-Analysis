# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step40_harmonic_class_compatibility_and_period_stiffness.md",
    "Sessions/S1003A01/workspace/scripts/step40_harmonic_class_period.py",
    "Sessions/S1003A01/workspace/data/step40/harmonic_class_period.json",
    "Sessions/S1003A01/workspace/scripts/su2_offdiag_hessian.py",
    "Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md",
    "Sessions/S1003A01/workspace/notes/step39_actual_harmonic_zero_test_and_route_comparison.md",
    "Sessions/S1003A01/workspace/scripts/step39_harmonic_zero_profile.py"
  ]
}
```

## Task

Verify the mathematics and numerics of the Step-40 note on harmonic-class compatibility of SU(2)-invariant cell variations for the perpendicular complex-hyperbolic blow-up cell. Check carefully: (a) the self-duality ODE d_t phi = (2/sqrt(det H)) H phi for invariant closed forms d(sum phi_i sigma_i) on g=dt^2+H_ij sigma_i sigma_j with d sigma_i = 2 sigma_j^sigma_k, including orientation and the factor 2; (b) the bolt exponents (0,2,2) for SD and (0,-2,-2) for ASD at a perpendicular bolt H~diag(t^2,b^2,b^2), smoothness conditions for the potential components, and the period formula int_E d(phi_1 sigma_1)=2 pi phi_1(0); (c) the SU(2)-averaging argument that for invariant variations supported in the cell the b^- solvability conditions int<h0, Omega o beta> = 0 collapse to a single exceptional condition, and the claims that the host period angle eta does not move at first order while j>=1 isotypic variations do not move exceptional periods at first order; (d) the Klein-group character localization of the obstruction in the h13 block and the decoupling from diagonal modes (including the exterior mass-null mode); (e) the rotation formula delta phi_1(0)=int theta' Phi dt and the gauge identity; (f) whether the period-stiffness computation DeltaJ = t^2/(2 L^T H^{-1} L) is correctly assembled from the Step-21 Hessians (note the Hessians were computed with a bolt rotation psi*(chi-1) while the period functional uses the isometric psi*chi form; check that this does not change the Hessian or the period functional), and what exactly it establishes (Ritz upper value at second order within the invariant block, floating). (g) Section 1: conformal invariance of the pair class and the claimed extension of inf P = inf J6 to pair classes defined by conditions on Omega. Also judge the interpretation in Section 3: positive exceptional areas available at quadratic cost near the perpendicular cell versus linear Kahler tariff, and what it does and does not imply for Taubes/AKGamma-type lower bounds and for the unrestricted blow-up tariff. Point out any error, missing hypothesis, or overstatement, and give the corrected statement.

## Output

# Step 40 科学核验备忘录

## 总结

Step 40 的局部微分几何骨架基本正确：

- 在取向 \(dt\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3>0\) 下，自对偶方程确为
  \[
  \dot\phi=\frac{2}{\sqrt{\det H}}H\phi,
  \]
  反自对偶方程取相反号。
- 垂直 bolt 的指标 \((0,2,2)\) 与 \((0,-2,-2)\) 正确；bolt 正则的 invariant ASD 解空间是一维。
- invariant 变化的固定上同调类相容性确实压缩成每个 cell 一个标量条件。
- 在基准形式沿 slot \(3\)、异常方向沿 slot \(1\) 时，直接局部周期通道位于 \(h_{13}\)。
- 旋转公式、gauge 恒等式及数值 ODE 实现彼此吻合。
- 刚度公式
  \[
  \Delta J=\frac{t^2}{2L^TH^{-1}L}
  \]
  作为有限维二阶 Ritz 计算是正确的。

但有一个影响全部周期数值的明确归一化错误：

> Step 39 的几何形式是  
> \[
> \Omega=\frac12d(\phi_i\sigma_i),
> \]
> 而 Step 40 的脚本把 \(t=2\pi\phi_1(0)\)。几何周期实际应为  
> \[
> t=\int_E\Omega=\pi\phi_1(0).
> \]

因此文件中的 \(K\simeq8.09\) 对应的是 \(\widetilde t=2t\)，不是 Step 39 的几何周期 \(t\)。以真正的 \(\Omega\) 周期表示，应有
\[
K_{\Omega}=4K_{\rm file}\simeq32.34,\qquad
\Delta J\simeq16.17\,t^2.
\]
相应地，Ricci \(=-g\) 尺度下的系数约为 \(0.4492\,t_g^2\)，不是 \(0.1123\,t_g^2\)。

此外，非平凡 SU(2) isotype “绝不会在一阶改变异常周期”只在孤立 cell、SU(2)-等变端值响应中成立；对一般闭流形的全局 period map，异常类的全局 ASD 调和代表可在 cell 内含非 invariant 分量，因此还不能作这一全局断言。

---

## 1. invariant 自对偶 ODE

令
\[
\eta_1=\sigma_2\wedge\sigma_3,\quad
\eta_2=\sigma_3\wedge\sigma_1,\quad
\eta_3=\sigma_1\wedge\sigma_2.
\]
在 regular orbit 区域写
\[
F=d\!\left(\sum_i p_i(t)\sigma_i\right)
  =dt\wedge p_i'\sigma_i+2p_i\eta_i.
\]
三维 orbit 度量为 \(H_{ij}\sigma_i\sigma_j\)，于是
\[
*_3\sigma_i=\sqrt{\det H}\,(H^{-1})_{ij}\eta_j.
\]
采用取向 \(dt\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3>0\)，有
\[
*_4(dt\wedge\alpha)=*_3\alpha.
\]
故 \(F=*F\) 等价于
\[
2p=\sqrt{\det H}\,H^{-1}p',
\]
即
\[
\boxed{p'=\frac{2}{\sqrt{\det H}}Hp.}
\]
同理，\(F=-*F\) 给出
\[
\boxed{p'=-\frac{2}{\sqrt{\det H}}Hp.}
\]

因此式 (2.2) 中的矩阵位置与因子 \(2\) 都正确。反转四维取向会交换 SD 与 ASD。

需要补充一处几何表述：当 \(p_1(0)\ne0\) 时，\(p_1\sigma_1\) 不是跨越 bolt 的全局光滑一形式；上式是 regular orbit 区域上的局部势表示。二形式本身可以光滑，并具有非零异常周期。因此“每个 invariant 闭二形式全局等于 \(d(\sum p_i\sigma_i)\)”并不成立；正确说法是它在主轨道区有这一表示，势在 bolt 处允许连接形式型奇性。

---

## 2. bolt 指标、光滑性与周期

在垂直 bolt 处，
\[
H=\operatorname{diag}(t^2,b^2,b^2)+O(t^2)
\]
并且
\[
\sqrt{\det H}=tb^2(1+O(t^2)).
\]
SD 方程的主部为
\[
p_1'=\frac{2t}{b^2}p_1,\qquad
p_2'=\frac2t p_2,\qquad
p_3'=\frac2t p_3.
\]
所以
\[
p_1=c_1+O(t^2),\qquad
p_2=t^2(c_2+O(t^2)),\qquad
p_3=t^2(c_3+O(t^2)).
\]
指标确为
\[
(0,2,2).
\]
在通常的 bolt parity 条件下，这三类二形式都光滑。这里 \(p_1\sigma_1\) 本身可不光滑，但
\[
d(p_1\sigma_1)
\]
光滑。

ASD 主部为
\[
q_1'=-\frac{2t}{b^2}q_1,\qquad
q_2'=-\frac2tq_2,\qquad
q_3'=-\frac2tq_3,
\]
所以指标为
\[
(0,-2,-2).
\]
只有 \(q_1=c+O(t^2)\) 给出 bolt 正则 invariant ASD 二形式；另两支除非系数为零，否则具有 \(t^{-2}\) 奇性。因此局部正则 invariant ASD 空间确为一维。

### 周期

给定
\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2
\]
及 collapsing circle 周期 \(2\pi\)，有
\[
\int_E\sigma_2\wedge\sigma_3=\pi
\]
（整体符号依赖 \(E\) 的取向）。于是
\[
\int_Ed(p_1\sigma_1)
 =\int_E2p_1(0)\sigma_2\wedge\sigma_3
 =2\pi p_1(0).
\]
因此任务中所列的
\[
\int_Ed(\phi_1\sigma_1)=2\pi\phi_1(0)
\]
本身正确。

但是 Step 39 的规范是
\[
\Omega=\frac12d(\phi_i\sigma_i).
\]
在这一规范中，
\[
\boxed{\int_E\Omega=\pi\phi_1(0).}
\]
Step 40 脚本使用 collar 值 \(\phi_f(X)=X\)，这正是 Step 39 中括号内的 profile potential，而不是 \(d(\cdot)\) 势的系数 \(X/2\)。因此脚本中的周期少了外部的 \(1/2\)。

这一点也可由精确 CH collar 直接看出：
\[
\omega_{CH}=\frac12d(x\sigma_f)
           =\frac12dx\wedge\sigma_f+x\,\sigma_g\wedge\sigma_h.
\]
若改用 \(d(x\sigma_f)\)，得到的是 \(2\omega_{CH}\)。

---

## 3. 固定上同调类相容性与 SU(2) averaging

设闭流形上 \(\Omega\) 为 SD 调和形式，度量变化为 \(h\)，固定上同调类意味着
\[
\dot\Omega=da.
\]
微分 \(*\Omega=\Omega\) 得
\[
\dot *\,\Omega+*da=da,
\]
从而
\[
(da)^-=\frac12\dot *\,\Omega.
\]
算子
\[
d^-:\Omega^1\longrightarrow\Omega^-
\]
的余核是 ASD 调和二形式，所以可解性要求
\[
\int_M\langle \dot *\,\Omega,\beta\rangle\,dV=0
\qquad
\forall\beta\in\mathcal H^-.
\]
中间维数 Hodge star 的变分只依赖 \(h^\circ\)，并且在无关紧要的非零常数与符号之外，
\[
\langle\dot *\,\Omega,\beta\rangle
\sim \langle h^\circ,\Omega\circ\beta\rangle.
\]
因此式 (2.1) 的零条件正确。

### invariant 变化为何只给一个标量

若 \(h\) 与 \(\Omega\) 在 cell \(U\) 中均为 invariant，则
\[
\int_U\langle h^\circ,\Omega\circ\beta\rangle
=
\int_U\langle h^\circ,\Omega\circ\bar\beta\rangle,
\]
其中 \(\bar\beta\) 是 \(\beta|_U\) 的 SU(2) 平均。由于 \(d\)、\(*\) 与平均交换，\(\bar\beta\) 仍是闭 ASD 二形式；bolt 正则性迫使
\[
\bar\beta=c(\beta)\beta_E.
\]
若规范为 \(\int_E\beta_E=2\pi\)，则
\[
c(\beta)=\frac{\int_E\beta}{2\pi}.
\]
故全部 \(b^-\) 个方程都变为同一 cell 泛函乘以 \(\int_E\beta\)。

这一泛函并非恒零。若所有 ASD 类均与 \(E\) 正交，则 \(PD(E)\) 会完全落在 \(H^+\) 中，进而
\[
E^2=\|E\|^2>0,
\]
与 \(E^2=-1\) 矛盾。因此单 cell 确实得到一个非平凡标量条件。

对多个互不相交的异常球 \(E_i\)，相应的 \(E_i^-\) 线性无关：若
\[
\sum_i a_iE_i^-=0,
\]
则 \(\sum_i a_iE_i\) 为 SD 类，但其平方为
\[
-\sum_i a_i^2,
\]
只能在所有 \(a_i=0\) 时成立。因此每个 cell 一个独立条件的说法在这一设置中成立。

### \(\eta\) 的一阶变化

对 invariant \(h\)，period-map 的位移方向由 \(E^-\) 控制。对基准 Kähler ray \(K_X\)，
\[
K_X\cdot E=0,
\]
且 \(H^+\perp H^-\)。因此以 \(K_X\) 为基点的归一化夹角 \(\eta\) 的一阶导数为零；变化首先出现在二阶。这一结论适用于该 Kähler ray。

“只有异常面积移动”若理解为“period map 的 invariant 局部泛函是 rank-one exceptional channel”，是正确的；若理解为所有 host cycle 周期在一般 \(b^+>1\) 情形下一阶均不动，则还需要更多全局 Hodge 分解信息。

### 非平凡 isotype 的陈述需要收窄

对孤立 invariant cell，并固定 invariant collar 数据，线性响应算子按 SU(2) 类型分解。非平凡类型的响应在 \(E\) 上积分为零，所以没有直接的局部异常周期源。

但在一般闭流形上，全局异常类的 ASD 调和代表 \(E^-\) 在 cell 中不必是纯 invariant；其非 invariant 分量可与同类型的 \(h\) 配对：
\[
\int_U\langle h_j^\circ,\Omega\circ(E^-)_{j}\rangle
\]
不必为零。因此可严格写成：

> \(j\ne0\) 变化与局部 invariant 模式 \(\beta_E\) 的配对为零，并且在 SU(2)-等变 cell 端值问题中不产生一阶异常周期；对一般闭流形的全局 period map，还需知道全局 ASD 调和代表在 cell 内的全部 isotype 分量。

这也说明 host-period stiffness 与异常周期之间的全局耦合不能仅由局部 averaging 完全分离。

---

## 4. Klein 群、\(h_{13}\) 通道与旋转公式

三条 off-diagonal 通道 \(h_{12},h_{13},h_{23}\) 在
\[
(\sigma_1,\sigma_2,\sigma_3)\mapsto
(\varepsilon_1\sigma_1,\varepsilon_2\sigma_2,\varepsilon_3\sigma_3),
\qquad
\varepsilon_1\varepsilon_2\varepsilon_3=1,
\]
下携带不同角色。对角变化属于平凡角色。因此任何 Klein-invariant 二次泛函的 Hessian 都满足：

- 三个 off-diagonal block 互不耦合；
- 每个 off-diagonal block与所有对角模式互不耦合。

外部 mass-null 模式是对角模式，所以与 \(h_{13}\) 的 Hessian 交叉项为零。这个结论来自离散对称性，不依赖其是否为严格零模。

对基准
\[
\phi=(0,0,\phi_f)
\]
线性化
\[
\phi'=\frac{2}{\sqrt{\det H}}H\phi.
\]
off-diagonal 变化的一阶行列式变化为零，而第一分量只接收 \(\delta H_{13}\phi_f\)。若
\[
\psi_+'=\frac{2H_{11}}{\sqrt{\det H}}\psi_+,\qquad
\psi_+(t_c)=1,
\]
并固定 collar 端值 \(\delta\phi_1(t_c)=0\)，则
\[
\boxed{
\delta\phi_1(0)
=-\psi_+(0)\int_0^{t_c}
\frac{2\,\delta H_{13}\phi_f}
{\sqrt{\det H}\,\psi_+}\,dt.
}
\]
式 (2.3) 正确。

### 旋转公式的符号

按脚本的旋转矩阵约定，
\[
\delta H_{13}=\theta(H_{11}-H_{33}).
\]
定义
\[
\Phi=\psi_+(0)\frac{\phi_f}{\psi_+}.
\]
则
\[
\Phi'
=\frac{2(H_{33}-H_{11})}{\sqrt{\det H}}\Phi.
\]
代入上式得到
\[
\delta\phi_1(0)=\int_0^{t_c}\theta\,\Phi'\,dt.
\]
若 \(\theta(t_c)=0\) 且 \(\Phi(0)=0\)，则
\[
\boxed{
\delta\phi_1(0)
=-\int_0^{t_c}\theta'(t)\Phi(t)\,dt.
}
\]
因此按文中已经固定的 \(\delta H_{13}\) 约定，显示公式前应为减号。若同时反转 \(E\) 或周期取向，则最终周期符号随之改变；刚度不受影响。

### gauge 恒等式

由
\[
\left(\frac{\phi_f}{\psi_+}\right)'
=
\frac{2(H_{33}-H_{11})}{\sqrt{\det H}}
\frac{\phi_f}{\psi_+}
\]
立刻得到
\[
\int_0^{t_c}
\frac{2(H_{11}-H_{33})\phi_f}
{\sqrt{\det H}\psi_+}\,dt
=
-\left[\frac{\phi_f}{\psi_+}\right]_0^{t_c}
=-X.
\]
`harmonic_class_period.json` 给出的相对误差 \(1.1\times10^{-10}\) 与此完全一致。

“常数旋转是 gauge”还需同时旋转 collar 上的形式端值。若只旋转度量而仍把 collar potential 固定在 slot \(3\)，常数旋转会产生表观周期；将 \(\Omega\) 与 gluing identification 一同拉回后，该项恰由 collar 端值抵消。

---

## 5. Hessian 中的 \(\chi-1\) 与周期代码中的 \(\chi\)

`su2_offdiag_hessian.py` 使用
\[
\theta_{\rm Hess}=\psi(\chi-1),
\]
而周期代码使用物理相对旋转
\[
\theta_{\rm per}=\psi\chi,
\qquad \chi(t_c)=0,\quad\chi(0)=1.
\]
二者相差全局常数旋转 \(-\psi\)。若同时拉回度量、形式、异常球与 collar identification，则它们描述同一个几何族。因此：

- 纯 \(\psi^2\) 代价完全相同；
- 几何异常周期的一阶导数完全相同；
- 在真正的临界度量处，diffeomorphism-invariant Hessian 在商空间上定义良好，整个二次型也相同。

对 mixed \(\psi c_m\) 项还有一个技术点：脚本在旋转后以固定 frame 加入 \(k_{13}\)，而精确的全局拉回会同时旋转该 bump。二者在原点具有相同一阶切向量，但二阶坐标变化可产生一个对角变化项。若基准度量对该对角方向的一阶变分为零，则 mixed Hessian 相同；若只知道有限维近似驻定，则需要比较两种参数化或计算这一诱导对角项。当前材料没有给出这项的独立数值。

因此，纯旋转部分与周期协变性没有问题；全矩阵 \(K\) 的几何解释应写为“在采用脚本商空间参数化并把基准视为驻定点时的浮点二阶 Ritz 值”。

---

## 6. 刚度公式与归一化修正

若
\[
J(c)=J_0+\frac12c^THc+o(|c|^2),\qquad
t(c)=L^Tc+o(|c|),
\]
且 \(H\) 在该有限维空间中正定，则拉格朗日乘子给出
\[
c_*=\frac{H^{-1}L}{L^TH^{-1}L}\,t
\]
以及
\[
\boxed{
\Delta J_{\min}
=\frac{t^2}{2L^TH^{-1}L}.
}
\]
脚本的线性代数组装正确。

`schur_bolt_rotation` 的含义应改写为
\[
H_{\psi\psi}-H_{\psi m}H_{mm}^{-1}H_{m\psi}.
\]
它是“固定旋转幅度、允许 Chebyshev bump 松弛后的旋转代价”，不是未松弛的纯旋转代价。

### 周期因子修正

脚本使用
\[
L_{\rm file}=2\pi\,\frac{\partial\phi_1(0)}{\partial c}.
\]
对 Step 39 的
\[
\Omega=\frac12d(\phi_i\sigma_i)
\]
应使用
\[
L_\Omega=\pi\,\frac{\partial\phi_1(0)}{\partial c}
=\frac12L_{\rm file}.
\]
所以
\[
L_\Omega^TH^{-1}L_\Omega
=\frac14L_{\rm file}^TH^{-1}L_{\rm file},
\qquad
K_\Omega=4K_{\rm file}.
\]

修正后的表为：

\[
\begin{array}{c|ccc}
 &K_{\rm file}&K_\Omega&
\Delta J/t^2=K_\Omega/2\\ \hline
X=128,\ n=16&8.08848&32.35391&16.17695\\
X=512,\ n=10&8.09442&32.37766&16.18883\\
X=512,\ n=16&8.08628&32.34513&16.17256\\
X=512,\ n=24&8.08611&32.34442&16.17221
\end{array}
\]

因此几何周期版本是
\[
\boxed{
\Delta J
\simeq16.17\,t^2,
\qquad
t=\int_E\Omega.
}
\]

在 \(\bar g=6g,\ \psi=6\Omega\) 下，
\[
t_g=\int_E\psi=6t,
\]
故
\[
\boxed{
\Delta J
\simeq\frac{K_\Omega}{72}t_g^2
\simeq0.4492\,t_g^2.
}
\]

若坚持保留文件中的 \(K\simeq8.09\)，则必须把文件变量重命名为
\[
\widetilde t=2t=\int_E2\Omega.
\]
此时
\[
t_g=3\widetilde t,
\]
而不是文件所写的 \(t_g=6\widetilde t\)。

### 数值证据实际支持的内容

数据支持：

1. gauge 恒等式达到约 \(10^{-10}\) 相对误差；
2. 单一旋转和第一个 Chebyshev bump 的非线性 ODE 响应与线性泛函在 \(10^{-4}\)–\(10^{-3}\) 幅度下吻合；
3. \(K_{\rm file}\) 在 \(X=128\to512\) 及 \(n=10,16,24\) 下稳定到约 \(10^{-3}\)；
4. 所有显示的有限矩阵及其 fixed-period 子空间矩阵为正定。

这些结果给出有限维 invariant \(h_{13}\) 空间中的浮点二阶 Ritz 上值。它们尚未给出无限维 invariant 问题的严格最优系数，也没有直接测试最优组合 \(c_*\) 的有限幅度 \(J(t)\)。普通 coefficient-space 最小特征值随 \(n\) 改变不具规范不变意义；Step 21 的 generalized spectrum 更适合表达函数空间 coercivity。

---

## 7. conformal pair 与 \(\inf P=\inf J_6\)

四维中二形式上的 Hodge star 在
\[
\widehat g=u^2g
\]
下不变。因此若 \(\Omega\) 闭且 \(g\)-SD，则它仍是 \(\widehat g\)-SD，因而仍调和。保持同一个 \(\Omega\) 时：

- 上同调类不变；
- 所有周期不变；
- 零集及其拓扑不变；
- \(L^2\) 二形式范数也保持 conformal invariant。

这一部分正确。

需要修正一句表述：若 \(g\) 在 CH collar 上为 Kähler 且 \(\Omega=\omega_{CH}\)，则对 \(\widehat g=u^2g\)，同一复结构的 fundamental form 是
\[
\widehat\omega=u^2\Omega.
\]
所以 \(\Omega\) 并不是 \(\widehat g\) 的 Kähler form；它只是
\[
\Omega=u^{-2}\widehat\omega
\]
并渐近于原 CH Kähler form。cutoff conformal factor 在外端恢复为 \(1\) 后，才重新得到精确 CH collar 与精确匹配的 \(\Omega\)。

若对每个竞争 pair 都存在所述正 Yamabe factor，且其衰减足以令 cutoff 代价趋零，则
\[
J_6(g)\ge P(g)
\]
以及
\[
J_6(u^2g)=P(u^2g)\le P(g)
\]
给出
\[
\inf_{\text{pair class}}P
=
\inf_{\text{pair class}}J_6.
\]
这一推导适用于由 \(\Omega\) 本身决定的条件，例如：

- 固定实上同调类；
- 固定异常周期；
- 固定零集拓扑；
- 非消失性或指定零面。

若 pair 条件还包含 \(|\Omega|_g=\sqrt2\)、almost-Kähler 归一化或其他显式依赖 \(g\) 的等式，则 conformal 变化一般不保持这些条件。

对 \(m\) 个 core，把总 collar 恢复代价安排成 \(o(m)\) 还需要几何构造容许每个恢复半径随序列增大而互不干涉；在高密度放置中这不是仅由单 cell 衰减自动得到的。

此外，\(\inf P=\inf J_6\) 是下确界等式。它说明构造上界时可在事后做 scalar normalization 而不增大代价；但当前 \(K\) 来自 \(J_6\) Hessian，它不自动等于 period-resolved \(P\) Hessian。后者可能因 conformal 松弛而更小。

---

## 8. 对 Section 3 几何解释的修正

### 可以推出的内容

在有限维 invariant 模型中，period map 在垂直 cell 处具有非零导数，而 \(J\) 的一阶导数因 Klein 角色对称性消失。因此局部存在以异常周期为参数的分支，并有
\[
J(t)\le J_0+16.17\,t^2+o(t^2)
\]
，其中 \(t=\int_E\Omega\) 是 Step 39 的几何周期。若用文件变量 \(\widetilde t=2t\)，则原来的
\[
J(\widetilde t)\le J_0+4.043\,\widetilde t^2+o(\widetilde t^2)
\]
保持成立。

这确实表明：Kähler aligned cell 的线性 \(6t/\pi\) 规律不是所有非 Kähler cell 的局部 period law；垂直分支在 \(t=0\) 的一阶导数为零。

### 阈值与交点

用 \(J_0=0.9952879\) 及修正后的二次系数，纯二次截断给出
\[
t_{\rm threshold}
\approx
\sqrt{\frac{1-J_0}{16.17695}}
\approx0.01707,
\]
而不是 \(0.034\)。Ricci \(=-g\) 尺度下
\[
t_g\approx0.1024,
\]
而不是 \(0.20\)。

与 Kähler 线性增量比较，
\[
16.17t^2=\frac6\pi t
\]
给出
\[
t\approx0.1181.
\]
若把 \(J_0-1\) 的常数差也计入，总量截断的交点约为 \(0.1205\)。原文的 \(0.472\) 是以 \(\widetilde t=2t\) 计算出的增量交点。由于 \(0.12\) 已远大于真正受小参数展开直接控制的邻域，这一交点只能作为二阶截断的数值指示，不能据此确认两条完整非线性分支在那里相交。

即使不使用截断半径，连续性与 \(J_0<1\) 仍说明存在某个足够小的非零周期区间使 \(J<1\)；具体 \(0.017\) 需要三阶及更高阶余项的定量控制。

### Taubes 与 AKΓ

非零周期意味着 \(\Omega\) 不可能在整个 \(E\) 上恒为零。对 invariant 分支，\(\Omega|_E\) 实际是常数倍面积形式。然而这还不说明 \(\Omega\) 在闭流形上处处非零。只有闭、SD 且处处非零时，
\[
\Omega\wedge\Omega=|\Omega|^2dV>0
\]
才给出 symplectic form。

因此二次 period cost 提供的是成为 symplectic pair 的一个必要局部通道，而不是 Taubes 前提的实现。零集消失、全局 cohomology 选择、spin\(^c\) 类以及 host-period 耦合仍需单独处理。

同样，AKΓ 型估计中的线性 exceptional contribution 可以由下列任何一项承担：

- 零集消除所需的全局几何代价；
- 非 invariant host-period 通道；
- \(\eta\) 的高阶变化；
- 调和代表的全局重组；
- Weyl、振幅或导数能量；
- collar/interface flux。

局部 \(J_6\) Hessian 没有计算这些全部量，所以它不与 AKΓ 型估计冲突。

### 对 unrestricted blow-up tariff 的含义

当前结果说明 Kähler cell 的线性 period payment 不是非 Kähler 局部 cell 的普遍规律。它没有显示正周期会降低垂直 cell 代价；这里的二阶系数为正，故 \(t=0\) 仍是该 invariant block 的局部最小点。

它也未单独确定 unrestricted blow-up tariff，因为还缺少：

- 闭流形上的多 cell 同时实现；
- 全局 harmonic/self-dual 方向的 period-map 耦合；
- 非 SU(2) 模式；
- 非线性 \(j(t)\)；
- 若要求 symplectic 或 monopole 来源时的相应场方程。

---

## 建议采用的修正版核心陈述

可将 Step 40 的主要数值结论改写为：

> 对 Step 39 规范
> \[
> \Omega=\frac12d(\phi_i\sigma_i),\qquad t=\int_E\Omega=\pi\phi_1(0),
> \]
> \(x_0=0.038\) 的垂直 stationary cell 在有限维 SU(2)-invariant \(h_{13}\) Ritz 空间中具有
> \[
> J(t)=J_0+\frac12K_\Omega t^2+o(t^2),
> \qquad
> K_\Omega\simeq32.34,
> \]
> 即
> \[
> \Delta J\simeq16.17t^2.
> \]
> 在 Ricci \(=-g\) 规范、\(t_g=\int_E6\Omega=6t\) 下，
> \[
> \Delta J\simeq0.4492\,t_g^2.
> \]
> 这是固定 collar、SU(2)-invariant \(h_{13}\) 通道中的浮点二阶 Ritz 上值；它表明垂直非 Kähler cell 的异常周期在 \(t=0\) 附近按二次量增加代价，而不是 Kähler aligned 分支的线性规律。该计算本身不说明调和形式已处处非零，也不确定闭流形 unrestricted tariff。

这是与 Step 39 的形式规范、aligned slope \(6/\pi\)、以及 \(\bar g=6g,\ \psi=6\Omega\) 全部一致的版本。
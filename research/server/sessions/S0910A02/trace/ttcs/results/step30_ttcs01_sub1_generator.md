# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step30_route_reassessment_noncollapsed_bubble_variational.md",
    "Sessions/S0910A02/workspace/data/step30_noncollapsed_bubble_variational_audit.json",
    "Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md"
  ]
}
```

## Task

Develop sharper mathematical construction routes for the Step-30 variational Pohozaev/Komar bridge. We need ideas that could turn C^0 Ricci pinching in a noncollapsed four-dimensional ALE/orbifold bubble annulus into the Ozuch/Biquard first-obstruction projection R_+ v=0, ideally using minimizers of int |L_Z g|^2 or related divergence-free pairings rather than full curvature smoothing. Propose concrete lemmas, model problems, scale choices, and falsifying tests that Agent2/Agent3 can execute next. Preserve the exact Yau-26 target and do not claim final success.

## Output

### 一、把变分对象从 Killing 能量改成共形 Killing 能量

设泡的长度尺度为 \(\varepsilon_i\to0\)，并写

\[
\bar g_i=\varepsilon_i^{-2}g_i .
\]

若原度量满足

\[
\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op},g_i}\le \delta_i,
\qquad \delta_i\to0,
\]

则缩放后

\[
\left\|\operatorname{Ric}_{\bar g_i}-\varepsilon_i^2\bar g_i
\right\|_{\mathrm{op},\bar g_i}
\le \delta_i\varepsilon_i^2 ,
\]

从而

\[
\left|\operatorname{Ric}_{\bar g_i}^{\circ}\right|_{\bar g_i}
\le C\delta_i\varepsilon_i^2. \tag{1}
\]

径向场 \(r\partial_r\) 在平锥上是共形 Killing 场而不是 Killing 场；因此

\[
\int |\mathcal L_Zg|^2
\]

对径向 Ozuch 场具有 \(R^4\) 级的无用主项。更合适的是四维共形 Killing 算子

\[
\mathcal K_g Z:=(\mathcal L_Zg)^\circ
=\mathcal L_Zg-\frac12(\operatorname{div}_gZ)g
\]

以及能量

\[
J_R(Z)=\int_{\Omega_R}|\mathcal K_gZ|^2\,d\mu_g. \tag{2}
\]

固定外截面 \(\Sigma_R=\partial\Omega_R\) 上的迹后，极小场满足

\[
\delta_g\mathcal K_gZ=0. \tag{3}
\]

故

\[
o_Z:=\mathcal K_gZ
\]

同时无迹且无散。它正是适合与 \(\operatorname{Ric}^{\circ}\) 配对的 TT 测试张量。

在 Eguchi–Hanson 空间 \((N,g_b)\) 上，Ozuch 给出的标准场形成三个相关方向：

\[
X_b\sim r\partial_r,\qquad
Y'_{2}\sim Y^+_2,\qquad Y'_3\sim Y^+_3.
\]

相应张量满足

\[
o_0=(\mathcal L_{X_b}g_b)^\circ
=-2H^4+O(r^{-5}),
\]

\[
o_a=\mathcal L_{Y'_a}g_b
=\mathcal L_{Y_a^+}H^4+O(r^{-5}),
\qquad a=2,3, \tag{4}
\]

并且 \(|o_a|=O(r^{-4})\)、\(o_a\in L^2\)。这三个方向分别读取
\(R^+_{11},R^+_{12},R^+_{13}\)，共同读取

\[
R_+\omega_1^+.
\]

因此 Step 30 的径向场应使用 \(J_R^\circ=\int|\mathcal KZ|^2\)，旋转场也可统一使用同一泛函。

---

## 二、第一项核心引理：导数不落在 Ricci 误差上的 TT 投影

定义带宇宙常数的 Einstein 张量

\[
\mathcal G_{\bar g,\varepsilon^2}
=
\operatorname{Ric}_{\bar g}
-\frac12s_{\bar g}\bar g
+\varepsilon^2\bar g.
\]

它严格无散，且由 (1)

\[
|\mathcal G_{\bar g_i,\varepsilon_i^2}|
\le C\delta_i\varepsilon_i^2.
\]

若 \(Z_{a,i,R}\) 是 (2) 的极小场，令

\[
o_{a,i,R}:=\mathcal K_{\bar g_i}Z_{a,i,R}.
\]

由于 \(o_{a,i,R}\) 无迹，

\[
\mathcal P_{a,i}(R):=
\int_{\Omega_R}
\left\langle\mathcal G_{\bar g_i,\varepsilon_i^2},
o_{a,i,R}\right\rangle d\mu_{\bar g_i}
=
\int_{\Omega_R}
\left\langle\operatorname{Ric}_{\bar g_i}^{\circ},
o_{a,i,R}\right\rangle d\mu_{\bar g_i}. \tag{5}
\]

于是

\[
|\mathcal P_{a,i}(R)|
\le
C\delta_i\varepsilon_i^2
\|o_{a,i,R}\|_{L^1(\Omega_R)}. \tag{6}
\]

这个式子只使用 Ricci 的逐点大小，不含 \(\nabla\operatorname{Ric}\)。

### 可证明的粗估计

若 \(J_R(Z_{a,i,R})\le C\)，则由 Cauchy–Schwarz 和四维体积增长，

\[
\|o_{a,i,R}\|_{L^1}
\le C R^2J_R(Z_{a,i,R})^{1/2}
\le CR^2,
\]

故

\[
\varepsilon_i^{-2}|\mathcal P_{a,i}(R)|
\le C\delta_iR^2. \tag{7}
\]

在得到 \(r^{-4}\) 衰减后还能改进为

\[
\|o_{a,i,R}\|_{L^1}\le C(1+\log R),
\qquad
\varepsilon_i^{-2}|\mathcal P_{a,i}(R)|
\le C\delta_i(1+\log R), \tag{8}
\]

但 (7) 已足以处理任意无预设关系的 \(\delta_i,\varepsilon_i\)。

### 极小能量的竞争场估计

若在 \(\Omega_R\) 上，\(\bar g_i\) 与某个经过尺度和方向调制的 EH 度量 \(g_{b,i}\) 的尺度化 \(C^1\) 距离为 \(\eta_i(R)\)，则把 \(X_b,Y'_2,Y'_3\) 截取为竞争场给出

\[
J_R(Z_{a,i,R})
\le
C\Bigl(
1+\eta_i(R)^2R^4+\varepsilon_i^4R^8
\Bigr). \tag{9}
\]

最后一项来自外部潮汐项
\(\varepsilon_i^2H_2\)，因为

\[
|\mathcal K(\varepsilon_i^2H_2)|\sim \varepsilon_i^2r^2.
\]

因此一种无需比较 \(\delta_i\) 与 \(\varepsilon_i\) 的单尺度选择是

\[
R_i=
\min\left\{
\delta_i^{-1/4},
\varepsilon_i^{-1/4},
R_i^{\mathrm{geom}}
\right\}, \tag{10}
\]

其中 \(R_i^{\mathrm{geom}}\to\infty\) 选得足够慢，使

\[
\eta_i(R_i)R_i^2\to0.
\]

于是

\[
R_i\to\infty,\qquad
\delta_iR_i^2\to0,\qquad
\varepsilon_iR_i\to0,\qquad
\varepsilon_i^4R_i^8\to0. \tag{11}
\]

若坚持使用未经无迹化的 Komar 表达式，径向场会额外产生
\(C\delta_i\varepsilon_i^2R_i^4\)；此时可把
\(\delta_i^{-1/4}\) 攈成 \(\delta_i^{-1/8}\)。TT 投影 (5) 避开了这个体积项。

---

## 三、第二项核心引理：EH Green 表达式把 TT 投影变成 \(R_+\omega_1^+\)

令

\[
\mathcal L_b=(D\operatorname{Ric}^{\circ})_{g_b}
\]

在 Bianchi 规范下作用于对称二张量。对 EH Jacobi 张量 \(o_a\)，有

\[
\mathcal L_b o_a=0,\qquad
\delta_{g_b}o_a=0,\qquad
\operatorname{tr}_{g_b}o_a=0.
\]

存在 Green 截面双线性型 \(\mathfrak B_R(k,o_a)\)，使

\[
\int_{\Omega_R}
\bigl(
\langle\mathcal L_bk,o_a\rangle
-
\langle k,\mathcal L_bo_a\rangle
\bigr)d\mu_{g_b}
=
\mathfrak B_R(k,o_a). \tag{12}
\]

其主项具有通常形式

\[
\mathfrak B_R(k,o_a)
=
\int_{\Sigma_R}
\left(
\langle\nabla_\nu k,o_a\rangle
-\langle k,\nabla_\nu o_a\rangle
+\text{Bianchi gauge terms}
\right)dA. \tag{13}
\]

若

\[
k=H_2+O(r^{-2})
\]

且 \(o_a\) 具有 (4) 的渐近展开，则功率计数给出有限极限：

\[
\mathfrak B_\infty(H_2,o_0)
=c_0R^+_{11},
\]

\[
\mathfrak B_\infty(H_2,o_2)
=c_2R^+_{12},\qquad
\mathfrak B_\infty(H_2,o_3)
=c_3R^+_{13}, \tag{14}
\]

其中 \(c_a\ne0\)。这就是 Ozuch Theorem 4.6 和 Corollary 4.10 的 Green 型版本。三个式子同时消失等价于

\[
R_+\omega_1^+=0. \tag{15}
\]

这里 \(O(r^{-2})\) 项对 (14) 没有贡献；其截面配对衰减为零。因此无需先证明 Ozuch 特殊坐标中的 \(H_2^4=0\)，只需排除比 \(r^2\) 更快增长并能进入 (14) 的模式。

### 定量桥接引理的理想形式

若调制和规范固定后

\[
\bar g_i=g_{b,i}+\varepsilon_i^2k_i+q_i,
\]

并且在 \(\Omega_{R_i}\)

\[
k_i=H_2+O(r^{-2})+\text{小误差},
\]

那么 (5)、(12) 应给出

\[
|R_+\omega_1^+|
\le
C\left[
\delta_iR_i^2
+R_i^{-1}
+\varepsilon_iR_i
+\varepsilon_i^2R_i^2
+\rho_i(R_i)
\right]. \tag{16}
\]

各项来源分别是：

* \(\delta_iR_i^2\)：由 (7)；
* \(R_i^{-1}\)：EH 的 \(O(r^{-5})\) 尾项；
* \(\varepsilon_iR_i\)：orbifold 展开中的三次项；
* \(\varepsilon_i^2R_i^2\)：Einstein 算子的二次余项；
* \(\rho_i(R_i)\)：归一化颈区展开和调制误差。

选择 (10) 并证明 \(\rho_i(R_i)\to0\) 后，(16) 导出 (15)。

更干净的版本采用迭代极限：先固定 \(R\)，令 \(i\to\infty\)；再令 \(R\to\infty\)。这样 Ricci 误差项在第一步直接趋零，不需要任何 \(\delta_i\log\varepsilon_i^{-1}\) 型关系。

---

## 四、真正关键的解析对象：EH 速率刚性与调制

变分投影本身已能处理 \(C^0\) Ricci 数据。剩余实质是证明

\[
\bar g_i-g_{b,i}=O(\varepsilon_i^2)
\quad\text{在每个固定 EH 紭集上}, \tag{17}
\]

而不是仅有 \(\bar g_i\to g_b\)。

一个合适的引理形状是：

> **EH 速率刚性引理。**  
> 经过 Bianchi–harmonic 微分同胚、EH 尺度调制、渐近 \(SO(4)\) 框架调制以及对 EH 的 \(L^2\) Jacobi 方向作正交化后，对每个固定 \(A\) 和 \(p>4\)，
> \[
> \|\bar g_i-g_{b,i}\|_{W^{2,p}(\Omega_A)}
> \le C_A\varepsilon_i^2.
> \]
> 因而
> \[
> k_i:=\varepsilon_i^{-2}(\bar g_i-g_{b,i})
> \]
> 在紧集上收敛到 \(k\)，且
> \[
> (D\operatorname{Ric})_{g_b}k=g_b,
> \qquad
> (D\operatorname{Ric}^{\circ})_{g_b}k=0.
> \]

其反证归一化机制很明确。若存在幅度
\(a_i\gg\varepsilon_i^2\)，则

\[
u_i=a_i^{-1}(\bar g_i-g_{b,i})
\]

趋于 EH 上的 Jacobi 张量。尺度、方向、微分同胚和 \(L^2\) 模式均已由调制消去；orbifold 端又把真正的 \(r^2\) 潮汐系数固定为 \(\varepsilon_i^2H_2\)。因此所需的核心分类是：

\[
\text{EH 上所有次二次增长 Jacobi 张量}
=
\text{调制模式}+\text{纯规范模式}. \tag{18}
\]

在平锥 \(\mathbb R^4/\mathbb Z_2\) 上，还需明确处理 \(r^{-2}\)、\(r^0\) 等齐次模式。若 \(r^{-2}\) 模式是体积规范或尺度规范，它可被调制消去；若存在一个非规范、非 \(L^2\)、次二次增长模式，(17) 的上述形式就不成立，必须把该模式加入有限维参数空间。

这一部分不需要 Ricci 流。谐和坐标中的方程是

\[
-\frac12g^{ab}\partial_a\partial_b g_{ij}
+Q_{ij}(g^{-1},\partial g)
=
\operatorname{Ric}_{ij}. \tag{19}
\]

一旦颈区已有 \(C^{1,\alpha}\) 谐和坐标，右端的 \(L^\infty\) 控制直接给出局部 \(W^{2,p}\) 控制；差分方程和 (18) 可用于提升收敛速率。所需文献对象很具体：

* Eguchi–Hanson 上加权 Lichnerowicz 核及其 indicial roots；
* Biquard 的 EH Jacobi 张量分类；
* Ozuch 的加权 Bianchi 规范与 EH 调制；
* ALE 椭圆算子的加权 Fredholm 理论。

---

## 五、若 (17) 不能直接得到：Ozuch–Kuranishi 双投影路线

允许存在

\[
v_i\to0,\qquad \|v_i\|\gg\varepsilon_i^2,
\]

其中 \(v_i\) 属于 EH 的有限维 Jacobi 空间。写成

\[
\bar g_i
=
g_{v_i}
+\varepsilon_i^2h_i
+w_i,
\]

并令

\[
p_i:=\Pi_{\mathbf O(g_b)}\Phi_{g_b}(g_{v_i})
\]

为 Kuranishi 余项。

第一种投影沿 \(p_i/\|p_i\|\) 给出

\[
\|p_i\|
\le
C\varepsilon_i^2
\bigl(1+\delta_iR_i^2\bigr)
+o(\varepsilon_i^2). \tag{20}
\]

第二种投影沿 \(o_0,o_2,o_3\)。Ozuch Proposition 0.12 的关键内容是

\[
\bigl|
\langle\Phi(g_{v_i}),o_a\rangle
\bigr|
\le
C\|v_i\|\,\|p_i\|. \tag{21}
\]

因 \(\|v_i\|\to0\)，(20)–(21) 导出

\[
\varepsilon_i^{-2}
\langle\Phi(g_{v_i}),o_a\rangle
\to0.
\]

于是主项仍为

\[
\varepsilon_i^2\mathfrak B_\infty(H_2,o_a),
\]

从而得到 (15)。这一双投影结构比直接要求
\(\bar g_i-g_b=O(\varepsilon_i^2)\) 更强：较大的 EH 模量漂移不会污染对称 Pohozaev 分量。

对 EH 而言，还可把可积的 \(v_i\) 吸收到实际 EH 参数
\(g_{b,i}\) 中。尺度由曲率或 bolt 面积固定，方向由渐近框架固定；最终的 \(\omega_{1,i}^+\) 正是泡所选择的方向。

---

## 六、最有区分力的模型计算

### 1. 精确 EH 共形 Killing 极小场

在截断 EH 空间上分别给定 \(r\partial_r,Y_2^+,Y_3^+\) 的外迹，求解

\[
\delta\mathcal KZ=0.
\]

应核验：

\[
\int_{\Omega_R}|\mathcal KZ|^2=O(1),
\qquad
\int_{\Omega_R}|\mathcal KZ|=O(\log R),
\]

以及

\[
\mathcal KZ_0=-2H^4+O(r^{-5}),\qquad
\mathcal KZ_a=\mathcal L_{Y_a^+}H^4+O(r^{-5}).
\]

同一计算若改用 \(\int|\mathcal L_Zg|^2\)，径向能量应呈 \(R^4\) 主项。这一对照直接区分两个泛函。

EH 的 \(SU(2)\) 对称性可把径向部分化成 ODE；旋转部分可用有限个球谐模式化简。数值有限元只需用来观察能量增长和模式混合，解析证明仍来自椭圆方程。

### 2. \(3\times3\) 障碍矩阵的显式球面积分

由 Ozuch 的公式，

\[
\operatorname{Ric}^{(2)}_e(H^4,H_2)
=
C\sum_{j=1}^3
R^+_{1j}
\frac{\theta_1^-\circ\omega_j^+}{r^4}.
\]

分别与 \(r\partial_r,Y_2^+,Y_3^+\) 配对，并使用

\[
\int_{S^3}x_ax_b\,dA
=
\frac{|S^3|}{4}\delta_{ab},
\]

即可得到 (14)。这一计算能确定所有符号和非零常数，并可把最后的线性代数写成小型 Lean 定理：

\[
\mathfrak B_0=\mathfrak B_2=\mathfrak B_3=0
\iff
R_+\omega_1^+=0.
\]

### 3. 平锥强迫项压力测试

在线性模型

\[
\mathcal L_eu=f,\qquad
\|f\|_\infty\le\delta
\]

中，用 \(r^{-4}\) Jacobi 张量 \(o\) 配对：

\[
\left|\int_{A(1,R)}\langle f,o\rangle\right|
\le C\delta\log R.
\]

取 \(f\) 在若干壳层上近似对齐 \(o/|o|\)，可使该数量达到同一量级。这说明在自然匹配尺度上不能预设
\(\delta\log\varepsilon^{-1}\to0\)；慢对角尺度或先 \(i\to\infty\)、再 \(R\to\infty\) 是实质性的。

### 4. 平锥齐次模式枚举

在 \(\mathbb R^4/\mathbb Z_2\) 上分解 Bianchi 规范对称二张量的齐次解，记录所有增长率与 \(-4,-2,0,2\) 相邻的模式，并计算它们与 \(o_0,o_2,o_3\) 的 Green 配对。

最关键的区分观察是：是否存在一个非规范、非 EH 模量、次二次增长模式。若存在，它必须进入 Kuranishi 参数；若不存在，(18) 给出速率提升。

### 5. EH 模量漂移测试

考虑一列精确 EH 度量，其尺度或方向漂移量满足

\[
\varepsilon_i^2\ll |v_i|\to0.
\]

固定 \(g_b\) 的测试张量会看到伪主项；随 \(g_{b,i}\) 调制的测试张量应消除它。这个例子直接检验“先调制、再除以 \(\varepsilon_i^2\)”是否被正确实现。

### 6. 非线性环域模型

取

\[
g_{\mathrm{app}}
=
e+H^4+\varepsilon^2H_2+u
\]

并在 Bianchi 规范下求使
\(\|\operatorname{Ric}^{\circ}\|_\infty\) 最小的 \(u\)。当
\(R_+\omega_1^+\ne0\) 时，TT 投影预言归一化 Ricci 各向异性不能同时趋零；当
\(R_+\omega_1^+=0\) 时，一阶投影消失。该模型可揭示遗漏的尺度因子、规范项和旋转分量。

---

## 七、这条桥最终应呈现的定理形状

对形成单个 \(\mathbb R^4/\mathbb Z_2\)–Eguchi–Hanson 泡的非塌缩序列，若能建立：

1. EH 参数调制与速率刚性，或 Kuranishi 双投影分解；
2. 共形 Killing 极小场的统一能量估计；
3. 归一化颈区误差 \(\rho_i(R_i)\to0\)；
4. Green 截面型与 Ozuch 球面积分的一致性；

则 \(C^0\) Ricci 夹逼本身会迫使

\[
R_+(p)\,v_{\mathrm{EH}}=0.
\]

这里无需逐点控制 \(Rm\)，也无需 Ricci 流；Ricci 误差始终只以 \(L^\infty\)-与 TT 张量的积分配对出现。

这一结论只处理四维正归一化、非塌缩、EH 型泡的一阶相容性。原 Yau 第 26 题还包含塌缩几何、一般 ALE 泡树、全部解奇化方程、原光滑拓扑上的 Einstein 度量构造以及所有维数。即使得到 \(R_+v=0\)，更高阶 Ozuch 障碍与全局粘合仍需独立数学结构。
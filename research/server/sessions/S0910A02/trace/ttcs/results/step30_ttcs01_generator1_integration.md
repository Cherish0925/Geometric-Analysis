# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 30,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step30_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step30_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop sharper mathematical construction routes for the Step-30 variational Pohozaev/Komar bridge. We need ideas that could turn C^0 Ricci pinching in a noncollapsed four-dimensional ALE/orbifold bubble annulus into the Ozuch/Biquard first-obstruction projection R_+ v=0, ideally using minimizers of int |L_Z g|^2 or related divergence-free pairings rather than full curvature smoothing. Propose concrete lemmas, model problems, scale choices, and falsifying tests that Agent2/Agent3 can execute next. Preserve the exact Yau-26 target and do not claim final success.

## Integrated Scientific Memo

# Step‑30 变分 Pohozaev/Komar 桥：校正后的构造方案

## 1. 首要校正：单靠 \(\int |\mathcal L_Zg|^2\) 不适合径向障碍

旋转场 \(Y\) 在平锥上是 Killing 场，可用
\[
J(Z)=\int_\Omega |\mathcal L_Zg|^2.
\]
但径向场 \(r\partial_r\) 是共形 Killing 场，平锥上
\[
\mathcal L_{r\partial_r}e=2e,
\]
故普通 Killing 能量本身有 \(R^4\) 级体积主项，不能有效检测 \(H^4\)。

四维应统一采用共形 Killing 箔子
\[
\mathcal K_gZ:=(\mathcal L_Zg)^\circ
=\mathcal L_Zg-\frac12(\operatorname{div}_gZ)g
\]
及
\[
J^\circ_\Omega(Z)=\int_\Omega |\mathcal K_gZ|^2\,d\mu_g.
\]
固定边界迹后，极小场满足
\[
\delta_g\mathcal K_gZ=0.
\]
因此
\[
o_Z:=\mathcal K_gZ
\]
无迹且无散。它是比原始 Komar 向量通量更自然的测试张量，尤其适合 \(C^0\) Ricci 夹逼，因为
\[
\langle \operatorname{Ric}^\circ,o_Z\rangle
\]
不包含标量曲率误差，也不需要 \(\nabla\operatorname{Ric}\)。

在 Eguchi–Hanson（EH）模型上，Ozuch 的谐和延拓给出三个关键方向：
\[
X_b\sim r\partial_r,\qquad Y'_2\sim Y^+_2,\qquad Y'_3\sim Y^+_3,
\]
且
\[
(\mathcal L_{X_b}g_b)^\circ=-2H^4+o(r^{-4}),
\qquad
\mathcal L_{Y'_a}g_b=\mathcal L_{Y_a^+}H^4+o(r^{-4}).
\]
这三个 TT 张量分别读取 \(R^+_{11},R^+_{12},R^+_{13}\)，共同读取
\[
R_+\omega_1^+.
\]

需要注意：Ozuch 的 \(X_b\) 满足向量粗 Laplace 方程，而 \(\delta\mathcal KX=0\) 的具体符号和 Ricci 项依约定而异；二者在 Ricci-flat EH 上可以对应，但不能未经 Weitzenböck 计算直接认作同一个方程。

---

## 2. \(C^0\)-Ricci 安全的两个互补恒等式

设泡的长度尺度为 \(\varepsilon_i\)，并缩放
\[
\bar g_i=\varepsilon_i^{-2}g_i.
\]
若
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op},g_i}\le\delta_i,
\]
则
\[
\|\operatorname{Ric}_{\bar g_i}-\varepsilon_i^2\bar g_i\|_{\mathrm{op},\bar g_i}
\le \delta_i\varepsilon_i^2,
\qquad
|\operatorname{Ric}_{\bar g_i}^\circ|\le C\delta_i\varepsilon_i^2.
\]

### 2.1 精确非线性边界通量

四维定义
\[
\mathcal E_i
=
\operatorname{Ric}_{\bar g_i}
-\frac12s_{\bar g_i}\bar g_i
+\varepsilon_i^2\bar g_i.
\]
则
\[
\delta_{\bar g_i}\mathcal E_i=0,
\qquad
|\mathcal E_i|\le C\delta_i\varepsilon_i^2.
\]
对任意 \(Z\)，Ozuch Lemma 1.4 给出精确恒等式
\[
\int_{\partial\Omega}\mathcal E_i(Z,\nu)
=
\frac12\int_\Omega
\langle\mathcal E_i,\mathcal L_Z\bar g_i\rangle.
\tag{2.1}
\]
若 \(o_Z=\mathcal K_{\bar g_i}Z\)，因 \(o_Z\) 无迹，
\[
\int_\Omega\langle\mathcal E_i,o_Z\rangle
=
\int_\Omega\langle\operatorname{Ric}_{\bar g_i}^\circ,o_Z\rangle,
\tag{2.2}
\]
从而
\[
\left|
\varepsilon_i^{-2}
\int_\Omega\langle\operatorname{Ric}_{\bar g_i}^\circ,o_Z\rangle
\right|
\le
C\delta_i\|o_Z\|_{L^1(\Omega)}.
\tag{2.3}
\]
这是最干净的 \(C^0\)-安全投影：Ricci 缺陷不被微分。

若仅知
\[
J^\circ_\Omega(Z)\le C,
\]
且 \(\Omega\subset B_R\) 有四维体积增长，则
\[
\|o_Z\|_{L^1}\le CR^2,
\]
故误差为 \(C\delta_iR^2\)。若进一步证明 \(o_Z=O(r^{-4})\)，则
\[
\|o_Z\|_{L^1(A(1,R))}\le C(1+\log R).
\]

### 2.2 EH 自伴 Green 投影

令
\[
L_b=(D\operatorname{Ric}^\circ)_{g_b}
\]
取 Bianchi 规范。对于 EH 的 TT Jacobi 张量 \(o_a\)，
\[
L_bo_a=0.
\]
若 \(k\) 是待检测的潮汐扰动，则
\[
\int_{\Omega_R}
\bigl(\langle L_bk,o_a\rangle-\langle k,L_bo_a\rangle\bigr)
=
\mathfrak B_R(k,o_a),
\tag{2.4}
\]
其中 \(\mathfrak B_R\) 是含 Bianchi 修正项的边界双线性型。

对
\[
k=H_2+O(r^{-2})
\]
和 EH 渐近张量，有
\[
\mathfrak B_\infty(H_2,o_0)=c_0R^+_{11},\quad
\mathfrak B_\infty(H_2,o_2)=c_2R^+_{12},\quad
\mathfrak B_\infty(H_2,o_3)=c_3R^+_{13},
\tag{2.5}
\]
其中 \(c_a\neq0\)。这正是 Ozuch Theorem 4.6、Corollary 4.10 的 Green 形式。因此三个投影消失等价于
\[
R_+\omega_1^+=0.
\tag{2.6}
\]

最有希望的桥不是仅使用向量边界通量，也不是仅使用线性 Green 公式，而是：

1. 用非线性 \(\mathcal E_i\) 恒等式控制原始 \(C^0\) Ricci 缺陷；
2. 用 EH Green 型识别归一化投影极限；
3. 用变分场保证测试张量是规范稳定且能量最小的。

---

## 3. 建议证明的定量桥接引理

### 引理 A：变分 TT 场

在截断 EH 域 \(\Omega_R\) 上，对外边界分别指定
\[
r\partial_r,\quad Y_2^+,\quad Y_3^+
\]
的迹，并在内核施加正则边界条件。则 \(J^\circ\) 极小解 \(Z_{a,R}\) 满足
\[
\delta\mathcal K Z_{a,R}=0,
\qquad
J^\circ(Z_{a,R})\le C,
\tag{3.1}
\]
常数独立于 \(R\)，并且
\[
\mathcal KZ_{0,R}\to(\mathcal L_{X_b}g_b)^\circ,\qquad
\mathcal KZ_{a,R}\to\mathcal L_{Y'_a}g_b
\]
在固定紧集上收敛。

边界条件必须消除真正的共形 Killing 核，否则极小解不唯一。需要显式证明 Korn 型 coercivity，而不能只援引 Ozuch 的对称二张量 Fredholm 估计；源文 Lemma B.2 针对的是规范固定 Einstein 算子，不直接等于向量算子 \(\delta\mathcal K\)。

### 引理 B：双极限投影

假设调制后的泡尺度度量满足：固定 \(R\) 上
\[
\bar g_i\to g_b
\quad\text{于 }C^{1,\alpha}\cap W^{2,p},\quad p>4,
\]
且测试场 \(Z_{a,i,R}\) 收敛到引理 A 的 EH 场。则
\[
\lim_{R\to\infty}\lim_{i\to\infty}
\varepsilon_i^{-2}
\int_{\Omega_R}
\langle\operatorname{Ric}_{\bar g_i}^{\circ},
\mathcal K_{\bar g_i}Z_{a,i,R}\rangle
=
c_a(R_+\omega_1^+)_a,
\tag{3.2}
\]
前提是已识别 \(\varepsilon_i^2\) 阶潮汐项 \(H_2\)，或通过下述 Kuranishi 双投影排除了更大的 Jacobi 漂移。

另一方面，由 (2.3)，固定 \(R\) 后
\[
\left|
\varepsilon_i^{-2}
\int_{\Omega_R}
\langle\operatorname{Ric}_{\bar g_i}^{\circ},
\mathcal KZ_{a,i,R}\rangle
\right|
\le C_R\delta_i\to0.
\]
于是再令 \(R\to\infty\) 即得到 (2.6)。此迭代极限避免任何未经给定的
\(\delta_i\log\varepsilon_i^{-1}\to0\) 关系。

### 引理 C：单尺度版本

若需要一个随 \(i\) 增长的环域，可取
\[
R_i=\min\{\delta_i^{-1/4},\varepsilon_i^{-1/4},
R_i^{\rm geom}\},
\tag{3.3}
\]
其中 \(R_i^{\rm geom}\to\infty\) 足够慢，使几何误差满足所需加权小量。预期得到
\[
|R_+\omega_1^+|
\le C\bigl(
\delta_iR_i^2+R_i^{-1}
+\varepsilon_iR_i+\varepsilon_i^2R_i^2
+\rho_i(R_i)
\bigr).
\tag{3.4}
\]
来源依次是 Ricci 缺陷、EH \(O(r^{-5})\) 尾项、orbifold 三次项、非线性余项及规范/调制误差。式 (3.4) 目前是待证目标，不是已有结论。

---

## 4. 真正瓶颈：不是通量恒等式，而是二阶尺度识别

固定尺度上的 EH 收敛
\[
\bar g_i\to g_b
\]
不足以识别
\[
\varepsilon_i^{-2}(\bar g_i-g_b).
\]
需要以下两条路线之一。

### 4.1 速率刚性

经过 Bianchi–harmonic 微分同胚、EH 尺度和渐近框架调制，并消去 \(L^2\) Jacobi 模式后，证明
\[
\|\bar g_i-g_{b,i}\|_{W^{2,p}(\Omega_A)}
\le C_A\varepsilon_i^2.
\tag{4.1}
\]
其反证归约要求分类 EH 上所有次二次增长的 Lichnerowicz Jacobi 张量：
\[
\{\text{次二次增长 Jacobi 模式}\}
=
\{\text{尺度、方向、可积模量、纯规范}\}.
\tag{4.2}
\]
尤其必须枚举平锥上的 indicial rates \(-4,-2,0,2\) 附近模式；若存在非规范、非模量的次二次增长模式，就必须纳入有限维调制参数，(4.1) 的简单形式将失败。

谐和坐标方程
\[
-\frac12g^{ab}\partial_a\partial_b g_{ij}
+Q(g^{-1},\partial g)=\operatorname{Ric}_{ij}
\]
说明 \(L^\infty\) Ricci 可以提供局部 \(W^{2,p}\) 控制，但不能自动提供所需的 \(\varepsilon_i^2\) 收敛速率；速率提升依赖 Jacobi 分类和边界匹配。

### 4.2 Kuranishi 双投影

允许较大 EH 模量漂移
\[
\|v_i\|\gg\varepsilon_i^2,\qquad v_i\to0,
\]
写成
\[
\bar g_i=g_{v_i}+\varepsilon_i^2h_i+w_i.
\]
令
\[
p_i=\Pi_{\mathbf O(g_b)}\Phi_{g_b}(g_{v_i}).
\]
首先沿 \(p_i/\|p_i\|\) 投影，目标是证明
\[
\|p_i\|=O(\varepsilon_i^2)+o(\varepsilon_i^2).
\tag{4.3}
\]
再沿对称方向 \(o_0,o_2,o_3\) 投影。Ozuch Proposition 0.12 支持
\[
|\langle\Phi(g_{v_i}),o_a\rangle|
\le C\|v_i\|\,\|p_i\|,
\tag{4.4}
\]
因此该项除以 \(\varepsilon_i^2\) 后消失，剩下的主项正是
\(\mathfrak B_\infty(H_2,o_a)\)。

这条路线比直接证明 (4.1) 更稳健，因为它允许可积或非可积 Jacobi 漂移，但其应用仍要求建立 pinched 序列的分解和余项估计；Ozuch 的原定理只处理精确 Einstein 退化。

---

## 5. 径向 reduced-volume 路线的正确定位

径向障碍还可写成
\[
\Lambda\mathcal V(g_b)
+Q(W_b^+,W_o^-)+Q(W_b^-,W_o^+)=0.
\tag{5.1}
\]
这对近共形平坦的正 Einstein orbifold 点非常有力，因为非平坦 ALE 有
\(\mathcal V(g_b)<0\)，而 \(\Lambda>0\)。但不能据现有材料断言：

1. \(|\mathcal V(g_b)|\) 由泡的量子化 \(L^2\) 能量统一下界；
2. 对一般 ALE 类型，Weyl 交叉项一定较小；
3. 径向一个标量障碍足以推出完整 \(R_+v=0\)。

EH 情形必须保留两个旋转投影；径向加两旋转才给出三分量向量方程。径向路线适合做强排除测试和 spherical/conformally-flat 模型，不应替代 tensorial EH 投影。

此外，直接把非线性边界通量
\[
\int_{\Sigma_r}\mathcal E_g(Z,\nu)
\]
宣称为 Ozuch 的二阶平台是不充分的：\(\mathcal E_g=O(\delta)\) 只给出小通量，而 Ozuch 障碍来自归一化的 \(\varepsilon_i^2\) 阶交叉项。必须通过二阶尺度识别或 Green/Kuranishi 分解证明两者的极限一致。

---

## 6. 最有区分力的下一批模型与证伪测试

### 6.1 EH 共形 Killing 极小场

在截断 EH 上求解
\[
\delta\mathcal KZ=0
\]
并验证
\[
\int_{\Omega_R}|\mathcal KZ|^2=O(1),\qquad
\int_{\Omega_R}|\mathcal KZ|=O(\log R),
\]
以及三个渐近式。对照普通能量
\(\int|\mathcal L_Zg|^2\)：径向方向应出现 \(R^4\) 主项。若 \(J^\circ\) 极小能量仍随 \(R\) 多项式增长，则单尺度桥很可能失败，但双极限仍可能存活。

### 6.2 显式 \(3\times3\) 球面积分

从
\[
H^4=-\frac{\theta_1^-\circ\omega_1^+}{2r^4},
\qquad
\operatorname{Ric}^{(2)}_e(H^4,H_2)
=
C\sum_jR^+_{1j}
\frac{\theta_1^-\circ\omega_j^+}{r^4}
\]
分别与
\[
r\partial_r,\quad Y_2^+,\quad Y_3^+
\]
配对，确定全部符号和非零常数。最终线性代数应形式化为
\[
B_0=B_2=B_3=0
\iff R_+\omega_1^+=0.
\]

### 6.3 平锥 forcing 饱和测试

在线性模型
\[
L_eu=f,\qquad \|f\|_\infty\le\delta
\]
中与 \(r^{-4}\) 模式配对。选择 \(f\) 在各壳层与该模式同向，可达到
\[
\left|\int_{A(1,R)}\langle f,o\rangle\right|
\asymp\delta\log R.
\]
这会证伪任何不加条件便在自然匹配尺度 \(R\sim\varepsilon^{-1}\) 使用通量的论证，并说明双极限或慢对角尺度是必要的。

### 6.4 齐次 Jacobi 模式枚举

在 \(\mathbb R^4/\mathbb Z_2\) 上完整列出 Bianchi 规范对称二张量的齐次解及其 Green 配对。关键证伪对象是：

> 是否存在非规范、非 EH 模量、增长率小于 \(2\) 的模式，并对 \(o_0,o_2,o_3\) 有非零配对？

若存在，必须扩充 Kuranishi 参数；若不存在，速率刚性路线获得关键支撑。

### 6.5 EH 模量漂移

取精确 EH 度量序列，尺度或方向漂移满足
\[
\varepsilon_i^2\ll |v_i|\to0.
\]
固定背景测试会产生伪主项；随 \(g_{b,i}\) 调制的测试必须将其消除。这是检验“先调制、后除以 \(\varepsilon_i^2\)”的最低成本反例测试。

### 6.6 非线性环域模型

令
\[
g_{\rm app}=e+H^4+\varepsilon^2H_2+u
\]
并在 Bianchi 规范下优化 \(u\)，使
\(\|\operatorname{Ric}^\circ\|_\infty\) 最小。比较：

- \(R_+\omega_1^+\neq0\)：归一化 TT 投影是否保持非零；
- \(R_+\omega_1^+=0\)：一阶投影是否消失；
- 仅径向障碍消失但旋转障碍非零：验证标量路线不足。

---

## 7. 可实际追求的桥定理

对形成单个 \(\mathbb R^4/\mathbb Z_2\)-EH 泡的非塌缩四维序列，若建立：

1. EH 参数调制及速率刚性，或 Kuranishi 双投影分解；
2. 共形 Killing 极小场的统一 coercivity 与渐近；
3. 归一化颈区误差 \(\rho_i(R)\) 的控制；
4. 非线性 \(\mathcal E_i\) 投影与 EH Green 边界型的一致性；

则 \(C^0\) Ricci 夹逼可望推出
\[
R_+(p)v_{\rm EH}=0.
\]

这只解决四维正归一化、非塌缩、EH 型单泡的一阶相容性。它不处理一般 ALE 泡树、塌缩、高阶 Ozuch 障碍、全局解奇化及原光滑拓扑上的 Einstein 度量构造，更不解决全维 Yau 第26题。
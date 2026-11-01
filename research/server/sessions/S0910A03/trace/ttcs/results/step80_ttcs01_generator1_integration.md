# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 80,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step80_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step80_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Using the invariant orthogonally-transitive equations and the Step 80 numerical evidence, develop a mathematically concrete construction or obstruction focused on the first O(1) physical layer after a reflected scalar-minus-six T^3 center. The central issue is whether the base metric and orbit area can compensate the positive-semidefinite H^2 orbit-map stress while the full Ricci defect tends to zero and the shape reverses from forced contraction toward expansion. Propose a minimal but genuinely coupled ansatz or rescaling that is not a frozen cusp and not merely Step 73's tail; derive its equations or leading asymptotics, specify boundary/jet data consistent with reflection and R(q0)=-6, and identify a decisive calculation that could distinguish a real vanishing-defect mechanism from a surviving sign obstruction. Respect that common lattice scaling leaves U unchanged and that physical forcing uses rho dvol(gamma_B), e^{3r} on the cusp.

## Integrated Scientific Memo

## 第一物理层的具体模型：反射中心的“角滑移—面积泵”系统

Step 80 的关键信息不是长尾失败，而是一个稳定的入口层失配：当 \(R=4,6\) 时，最大缺陷始终约为 \(15\)，定位在 \(r\simeq0.2\)；远端的 \(S-I\)、内蕴 Ricci 和 \(v_r\) 却已趋零。联合调整基底只能降低 RMS，不能降低该 \(C^0\) 峰值。因此必须精确处理反射中心后的 \(O(1)\) 层，而不能继续依赖冻结 cusp 或 Step 73 尾部。

### 1. 完整 OT 系统

取
\[
g=e^{2\lambda(r,z)}(dr^2+dz^2)+e^{\sigma(r,z)}
U_{ab}(r,z)d\xi^a d\xi^b,\qquad \det U=1,
\]
其中 \(U:B\to\mathbb H^2=SL(2,\mathbb R)/SO(2)\)。记
\[
e_{ij}=\langle U_i,U_j\rangle_{\mathbb H^2},\qquad \rho=e^\sigma .
\]
精确的 \(\operatorname{Ric}=-3g\) 方程为
\[
\Delta\sigma+|\nabla\sigma|^2=6e^{2\lambda},
\tag{1}
\]
\[
\nabla_r(\rho U_r)+\nabla_z(\rho U_z)=0,
\tag{2}
\]
\[
\Delta\lambda=\frac14\bigl(|\nabla\sigma|^2-e_{rr}-e_{zz}\bigr),
\tag{3}
\]
以及共形规范约束
\[
\sigma_{rr}-\sigma_{zz}
-2\lambda_r\sigma_r+2\lambda_z\sigma_z
+\frac12(\sigma_r^2-\sigma_z^2)
+\frac12(e_{rr}-e_{zz})=0,
\tag{4}
\]
\[
\sigma_{rz}-\lambda_z\sigma_r-\lambda_r\sigma_z
+\frac12\sigma_r\sigma_z+\frac12e_{rz}=0.
\tag{5}
\]

有缺陷 \(E=\operatorname{Ric}+3g\) 时，轨道方程具有形式
\[
\nabla_i(\rho U_i)=\rho e^{2\lambda}\mathcal E_U^\circ .
\tag{6}
\]
因此物理源以
\[
\rho\,d\operatorname{vol}(\gamma_B)
\]
积分；在 cusp 上该权重为 \(e^{3r}\,dr\,dz\)。共同格点缩放
\[
G\mapsto N^{-2}G
\]
只给 \(\sigma\) 加常数，不改变 \(U\) 或其归一化能量，因而不能减弱入口层机制。

---

### 2. 反射中心及其精确二阶 jet

在 \(r=0\) 施加
\[
\lambda_r=\sigma_r=U_r=0.
\tag{7}
\]
令
\[
\lambda(0,z)=\ell(z),\quad \sigma(0,z)=s(z),\quad U(0,z)=U_0(z).
\]
中心三维度量是
\[
q_0=e^{2\ell}dz^2+e^sU_0.
\]
条件 \(R(q_0)=-6\) 等价于
\[
2(s_{zz}-\ell_zs_z)+\frac32s_z^2
+\frac12|U_{0,z}|_{\mathbb H^2}^2
=6e^{2\ell}.
\tag{8}
\]

由 (1)–(5) 得到必需的二阶 jet：
\[
\sigma_{rr}
=6e^{2\ell}-s_{zz}-s_z^2
=s_{zz}-2\ell_zs_z+\frac12s_z^2+\frac12|U_{0,z}|^2,
\tag{9}
\]
\[
\lambda_{rr}
=\frac14(s_z^2-|U_{0,z}|^2)-\ell_{zz},
\tag{10}
\]
\[
\nabla_rU_r
=-\bigl(\nabla_zU_{0,z}+s_zU_{0,z}\bigr).
\tag{11}
\]

特别地，在 \(s_z=\ell_z=0\)、\(|U_{0,z}|^2=12\) 的均匀中心，
\[
\sigma_{rr}=6,\qquad \lambda_{rr}=-3.
\tag{12}
\]
所以同一个 \(H^2\) 应力同时推动轨道面积增长，却首先使基底 \(z\) 方向收缩。所需的形状反转只能来自随后增长的 \(\sigma_r^2\) 在 (3) 中超过轨道能量。

积分形式也显示中心负担不可由格点缩放消除。用 \(d\tau=e^\ell dz\)，在对角情形
\[
q_0=d\tau^2+e^\sigma(e^d dx^2+e^{-d}dy^2)
\]
中，
\[
R(q_0)=-2\sigma_{\tau\tau}-\frac32\sigma_\tau^2-\frac12d_\tau^2=-6
\]
推出
\[
\boxed{\;
\langle d_\tau^2\rangle_\rho
=12+\langle\sigma_\tau^2\rangle_\rho\ge12.
\;}
\tag{13}
\]
对一般 \(U\)，这是相应的矩阵 \(H^1\) 能量下界。

---

### 3. 最小但真正耦合的 ansatz

单纯对角 \(U=\operatorname{diag}(e^d,e^{-d})\) 的二维模型确实比 Step 73 更耦合，但它没有测试完整 \(H^2\) 目标中的角向松弛。要直接打破 Step 78 的固定螺旋反馈，最小模型应保留极坐标
\[
ds_{\mathbb H^2}^2=dd^2+\sinh^2d\,d\psi^2 .
\]

先取均匀旋转中心
\[
\ell=0,\qquad s=s_*,\qquad d(0,z)=d_*,
\qquad \psi(0,z)=mz,
\tag{14}
\]
其中
\[
m^2\sinh^2d_*=12.
\tag{15}
\]
反射给出全部径向一阶导数为零；中心二阶导数为
\[
\sigma_{rr}=6,\qquad \lambda_{rr}=-3,
\qquad d_{rr}=12\coth d_*,\qquad \psi_{rr}=0.
\tag{16}
\]
若不加入额外 \(z\)-依赖，这正是 Step 78 型固定角速度反馈：\(d\) 增大，角向应力也增大。

加入最少的角滑移模式：
\[
d=d_0(r)+a(r)\cos kz+O(a^2),
\tag{17}
\]
\[
\psi=mz+b(r)\sin kz+O(a^2),
\tag{18}
\]
\[
\sigma=s_0(r)+p(r)\cos kz+q(r)\cos2kz+O(a^3),
\tag{19}
\]
\[
\lambda=\ell_0(r)+\alpha(r)\cos kz+\beta(r)\cos2kz+O(a^3).
\tag{20}
\]
所有振幅在 \(r=0\) 取偶反射数据，即一阶径向导数为零。

为使中心的一阶 \(H^2\) 应力不变，可取
\[
p(0)=\alpha(0)=0,\qquad
b(0)=-\frac{m}{k}\coth d_*\,a(0).
\tag{21}
\]
这正是“角滑移”：径向距离扰动与局部角速度扰动互相抵消，使 \(R(q_0)=-6\) 在一阶仍成立。二阶产生的零模和 \(2k\) 模必须由 \(q(0),\beta(0)\) 通过 (8) 精确确定，不能忽略。

线性化轨道方程给出
\[
a''+s_0'a'-k^2a
=m^2\cosh(2d_*)a
+2mk\sinh d_*\cosh d_*\,b,
\tag{22}
\]
\[
b''+s_0'b'-k^2b-mkp
-2mk\coth d_*\,a=0.
\tag{23}
\]
代入 (21)，中心处得到关键符号
\[
\boxed{\;a''(0)=(k^2-m^2)a(0).\;}
\tag{24}
\]
因此 \(k<m\) 时，扰动在第一非平凡阶向减小 \(d\) 的方向弯曲，而中心一阶应力保持不变。这是固定 VII\(_0\) 螺旋中不存在的最小松弛机制。

零模的主要耦合为
\[
s_0''+(s_0')^2=6e^{2\ell_0}+O(a^2),
\tag{25}
\]
\[
\ell_0''=\frac14\left((s_0')^2-\overline{e_U}\right)+O(a^2).
\tag{26}
\]
最初 \(\ell_0'\sim-3r\)，而 \(s_0'\sim6r\)。若角滑移使
\(\overline{e_U}\) 不再增长，\((s_0')^2\) 可在 \(O(1)\) 距离内改变
\(\ell_0''\) 的符号，从而允许基底由收缩转向扩张。若
\(\overline{e_U}\) 仍随 \(d\) 增长，则 Step 78 的障碍继续存在。

---

### 4. Step 80 对该模型的约束

数值资料支持如下定位：

* 最大残差对 \(R\) 基本不变，且锁定于 \(r\simeq0.2\)；
* 远端误差随 \(R\) 显著下降；
* 入口峰主要由 \(E_{zz}\) 控制；
* 联合基底响应降低 RMS，却没有降低 supremum 峰；
* 峰值与 \(\frac12|dU|^2\) 的量级相同。

因此不能断言该峰只是“冻结 \(\sigma,\lambda\)”的数值假象：Step 80 已包含 joint base response，而其 \(C^0\) 峰仍存。更准确的解释是：所用有限维基底响应没有满足 (8)–(11) 所规定的完整中心 jet，特别是没有加入角滑移及其二阶零模/\(2k\) 反作用。只有在直接求解全部 (1)–(5) 后峰仍稳定存在，才可把它升级为真正障碍。

---

### 5. 决定性计算：二阶 Galerkin 兼容性加凸矩估计

首先把 (17)–(20) 代入完整系统，保留到 \(O(a_0^2)\)，并：

1. 用 (8) 精确消去中心零模和 \(2k\) 模；
2. 强制满足全部二阶 jet (9)–(11)；
3. 演化零、\(k\)、\(2k\) 模至固定 \(L=O(1)\)；
4. 计算完整残差
   \[
   (\mathcal A,\mathcal T_U,\mathcal L,\mathcal C_1,\mathcal C_2)
   \]
   和零模形状
   \[
   \ell_0'(L)
   =-3L+3L^3+a_0^2\mathcal Q_{m,k,d_*}(L)+O(a_0^3).
   \tag{27}
   \]

若某个 \(k<m\) 使所有模方程相容、完整 \(C^0\) 残差趋零，同时
\(\ell_0'\) 转向正值，则得到真实的第一层反转机制。若在
\(E_{zz}\)、Hamilton 组合或 \(2k\) 约束中留下不可调的同号
\(O(a_0^2)\) 项，则这是 Step 80 峰的解析来源。

同时应以不变量形式检查所需缺陷矩。令
\[
F_P(U)=\frac12d_{\mathbb H^2}(U,P)^2.
\]
由于 \(\mathbb H^2\) 曲率为 \(-1\)，
\[
\operatorname{Hess}F_P\ge g_{\mathbb H^2}.
\]
由受迫轨道方程得到
\[
\operatorname{div}\!\bigl(\rho\nabla(F_P\circ U)\bigr)
\ge
\rho|dU|^2+
\bigl\langle\nabla F_P,\rho e^{2\lambda}\mathcal E_U^\circ\bigr\rangle .
\tag{28}
\]
反射边界的径向通量为零，故
\[
\int_{C_L}\rho\,\partial_r(F_P\circ U)\,dz
\ge
\int_0^L\!\!\int\rho|dU|^2\,dr\,dz
+
\int_0^L\!\!\int
\langle\nabla F_P,\rho e^{2\lambda}\mathcal E_U^\circ\rangle\,dr\,dz .
\tag{29}
\]

这给出清晰的二分判据：

* **真实机制：** 角滑移产生足够的出口凸距离通量，基底零模转向扩张，且完整缺陷趋零。
* **符号障碍：** 第一层轨道能量保持 \(O(1)\)，出口通量不足；因第一层物理体积仅为 \(O(1)\)，点态 \(o(1)\) 的缺陷无法支付 (29)，故必有 \(O(1)\) 的轨道或基底缺陷残留。

长扩张区则不同：其权重为 \(e^{3r}\)，所以点态很小的缺陷可积累为有限受迫矩。这正是为什么第一 \(O(1)\) 层与长尾必须分开检验，也解释了共同格点缩放不能解决入口峰。

最后，有限边界上把 \(U\) 强制成常值会触发凸距离刚性；无限 PE/cusp 端则未必如此。但这不能替代当前有限第一层计算：首先必须证明中心能量能够穿过该 \(O(1)\) 层而不留下固定的 \(C^0\) Ricci 缺陷。上述二阶模相容性及 (29) 的通量账本正是区分两种情形的最小决定性计算。
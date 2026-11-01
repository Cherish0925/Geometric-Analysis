# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 83,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step83_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step83_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Given the K-production framework for the OT graph-manifold connector, where K'=-2⟨τ,b⟩+2⟨vc⟩+Cov(v-u,k)-2xK with K(0)=12, K''(0)≥72, and a successful connector requires K≤6+2δ: investigate whether any known monotone or convex functional excludes the K-drop in the full coupled (γ_B, σ, M) OT system. Consider: (a) The total orbit energy E=∫ρ e_{H²} dz — does the full area/base evolution preserve E monotonicity? (b) The orbit-volume-weighted squared distance F=∫ρ d²_{H²}(U,P) dz for an appropriate reference P — does the coupled base response preserve its monotonicity? (c) The matrix Noether current Q=∫ρ M⁻¹M_r dz — can its vanishing be used in combination with other quantities? (d) Is there an energy/entropy functional combining K, x, y, ⟨|b|²⟩, ⟨h²⟩ that is monotone along the coupled Einstein evolution? Look for a differential inequality of the form d/dr(F)≥c·F or a Lyapunov argument. If no monotone quantity exists, identify which coupled mechanism breaks each candidate's monotonicity and what the resulting freedom is.

## Integrated Scientific Memo

## 结论

现有恒等式**不能排除**完整耦合 OT 系统中的 \(K\)-下降
\[
K:12\longrightarrow 6+2\delta .
\]
目前唯一稳健的凸性工具，是 \(\mathbb H^2\) 上距离函数产生的**二维加权散度恒等式**。它能排除“精确 Einstein、反射内边界、有限外边界处 \(U\) 恰为常值”的连接器，但它不是关于径向切片量 \(K\)、轨道能量或距离矩的 Lyapunov 律。

关键障碍是完整系统允许以下符号不定的交换：

- 空间张力与径向速度的相位交换 \(\langle\tau,b\rangle\)；
- 轨道能量在 \(U_s\) 与 \(U_r\) 间转移；
- 面积梯度 \(h^2\) 对 \(K=\langle |U_s|^2-h^2\rangle\) 的直接扣除；
- 演化权重 \(\rho\,ds\) 引起的空间重分布；
- \(u,v,k,h,b\) 的协方差；
- 满足矩阵 Noether 零均值的高频径向运动。

因此，VII\(_0\) 的标量正反馈并未延伸为完整 OT 系统的已知单调量。

---

## 1. 轨道能量没有径向单调性

采用物理规范
\[
e=|U_s|_{\mathbb H^2}^2,\qquad b=U_r,\qquad
\tau=D_sU_s+hU_s,\qquad H=u+v,\qquad d\mu=\rho\,ds .
\]
精确方程为
\[
D_rb+Hb+\tau=0.
\]
令
\[
\mathcal E_s=\int e\,d\mu,\qquad
\mathcal B=\int |b|^2\,d\mu .
\]
直接微分得
\[
\boxed{\mathcal E_s'
=-2\int\langle\tau,b\rangle\,d\mu
+\int(v-u)e\,d\mu,}
\]
并由轨道方程等价写成
\[
\boxed{\mathcal E_s'
=\mathcal B'
+\int H|b|^2\,d\mu+\int(v-u)e\,d\mu.}
\]
这里每个交换项都可变号。因此，固定膨胀尾部背景上的“阻尼能量”并不在动态基底中保留：基底和面积响应正是通过这些项向轨道场注入或抽取能量。

在共形基底规范下也只有应力平衡，而非能量单调性。若
\[
E_z=\int\rho |U_z|^2dz,\qquad E_r=\int\rho |U_r|^2dz,
\]
则源自由方程给出
\[
\boxed{(E_z-E_r)'=
\int\rho_r\bigl(|U_z|^2+|U_r|^2\bigr)\,dz.}
\]
\(\Delta\rho=6e^{2\lambda}\rho\) 只控制 \(\rho\) 的二维 Laplacian，并不固定逐切片的 \(\rho_r\) 符号；同时
\[
\Delta\lambda=\frac{|\nabla\sigma|^2-e_{\mathbb H^2}}4
\]
把轨道能量反馈回基底。故右端无固定符号。

即使 \(\int\rho e\) 增长，也不能阻止 \(K\) 下降，因为
\[
K=\langle e-h^2\rangle
\]
还可通过 \(h^2\) 增长或权重向低 \(e-h^2\) 区域迁移而降低。

---

## 2. 距离凸性保留的是通量单调，而不是切片距离单调

固定 \(P\in\mathbb H^2\)，设
\[
\phi(U)=\frac12d_{\mathbb H^2}(U,P)^2 .
\]
由于 \(\mathbb H^2\) 曲率为 \(-1\)，
\[
\operatorname{Hess}\phi\ge g_{\mathbb H^2}.
\]
精确加权调和映射满足
\[
\boxed{
\operatorname{div}\!\bigl(\rho\nabla(\phi\circ U)\bigr)
=\rho\,\operatorname{Hess}\phi(dU,dU)
\ge \rho|dU|^2.}
\]
因此
\[
\Psi(r):=\int_{S^1}\rho\,\partial_r(\phi\circ U)\,dz
\]
满足 \(\Psi'(r)\ge0\)。反射边界给出 \(\Psi(0)=0\)。这正是排除精确有限常值出口的凸性机制，而且任意正权重 \(\rho\) 都不会破坏它。

但题目中的切片量
\[
\mathcal F_P(r)=\int\phi(U)\,d\mu
\]
没有单调性：
\[
\boxed{
\mathcal F_P'
=\int\bigl(\langle\nabla\phi,b\rangle+H\phi\bigr)\,d\mu .}
\]
两个项都无固定符号。尤其反射中心处 \(b=H=0\)，故
\[
\mathcal F_P'(0)=0.
\]
若 \(\mathcal F_P(0)>0\)，则从中心开始不可能有
\[
\mathcal F_P'\ge c\,\mathcal F_P,\qquad c>0.
\]

二阶式进一步显示基底耦合：
\[
\boxed{
\mathcal F_P''
=\int\!\left[
\operatorname{Hess}\phi(b,b)
+\operatorname{Hess}\phi(U_s,U_s)
+(H'+H^2)\phi
+H\langle\nabla\phi,b\rangle
\right]d\mu .}
\]
前两项非负，但
\[
H'+H^2=3+H^2-|S|^2
\]
并不定号，最后的相关项也不定号。因此二维凸性不能转换成径向 Lyapunov 律。

若存在轨道缺陷源 \(\mathcal R_0\)，散度式增加
\[
\rho\langle\nabla\phi,\mathcal R_0\rangle .
\]
即使点态缺陷为 \(O(\delta)\)，长而膨胀的连接器中其加权累积仍可能是 \(O(1)\)。仅由现有资料不能严格推出 \(d_{\max}\gtrsim\delta^{-1}\)：这种估计还需要统一控制出口通量、物理/共形权重以及 \(|\nabla\phi|=d(U,P)\)，目前并未闭合。

选择移动参考点 \(P(r)\) 或加权重心只会消除一个零模，同时引入 \(P'\) 项；它仍不控制 \(U_s\)、\(h\) 及其相关性。

---

## 3. Noether 流只消除有限维零模

精确 OT 方程给出
\[
\mathcal Q(r)=\int_{S^1}\rho\,M^{-1}M_r\,dz
=\text{常数},
\]
反射性使
\[
\boxed{\mathcal Q\equiv0.}
\]
这只是 \(\mathfrak{sl}(2,\mathbb R)\) 中的有限维一阶矩约束，并不控制
\[
\int\rho\,|M^{-1}M_r|^2dz
\asymp \int |b|^2\,d\mu .
\]
大幅振荡的 \(b\) 可以具有零矩阵平均，却有任意大的 \(L^2\) 范数及显著的 \(\langle\tau,b\rangle\)。

更直接地，对常面积闭环 \(U(s)\)，任一目标 Killing 场 \(X\) 满足
\[
\int\langle X(U),D_sU_s\rangle ds=0.
\]
故 \(b=\varepsilon\tau\) 与 \(b=-\varepsilon\tau\) 都可满足 Noether 零均值，而它们使
\[
-2\langle\tau,b\rangle
\]
取相反符号。于是 \(\mathcal Q=0\) 不可能决定 \(K'\) 的符号。

若企图将 \(\mathcal Q=0\) 升级为能量控制，还需关于权重 \(\rho\) 的统一加权 Poincaré 常数；现有面积方程不排除 \(\rho\) 的 \(z\)-集中，因此没有这种已知统一估计。

---

## 4. 有限矩组合不闭合

令
\[
A=\langle h^2\rangle,\qquad B=\langle|b|^2\rangle .
\]
精确系统中
\[
\boxed{
B'=-2\langle\tau,b\rangle
-\langle H|b|^2\rangle-(x+y)B,}
\]
以及
\[
\boxed{
A'=\operatorname{Cov}(u,h^2)-yA
-\langle h\langle U_s,b\rangle\rangle .}
\]
已有的核心生产律为
\[
\boxed{
K'=-2\langle\tau,b\rangle+2\langle vc\rangle
+\operatorname{Cov}(v-u,k)-2xK,}
\]
且 Codazzi 给出
\[
\boxed{
2\langle vc\rangle
=-2\langle h^2u\rangle+\langle h^2v\rangle
+\langle h\langle U_s,b\rangle\rangle .}
\]

组合 \(K-B\) 确实消掉最明显的张力—速度项：
\[
\boxed{
(K-B)'=
2\langle vc\rangle+\operatorname{Cov}(v-u,k)-2xK
+\langle H|b|^2\rangle+(x+y)B.}
\]
但它引入了局部相关量 \(\langle H|b|^2\rangle\)。加入 \(A\) 可以消去一部分
\(\langle h\langle U_s,b\rangle\rangle\)，却仍留下
\[
\operatorname{Cov}(v-u,k),\quad
\operatorname{Cov}(u,h^2),\quad
\langle H|b|^2\rangle
\]
等不由 \((K,x,y,A,B)\) 决定的量。

因此，对任意仅依赖有限矩
\[
\mathcal L=\Phi(K,x,y,A,B)
\]
的候选量，现有平衡式不能导出
\[
\mathcal L'\ge0
\quad\text{或}\quad
\mathcal L'\ge c\mathcal L.
\]
这不是说不存在任何更复杂的非局部泛函，而是说明所列有限矩族不闭合；新的泛函必须记录至少：

1. \(\tau\) 与 \(b\) 的相位；
2. \(H,u,v\) 与 \(|b|^2,k,h^2\) 的空间相关；
3. 权重 \(\rho\) 的集中程度；
4. \(U_s\) 与 \(U_r\) 的二维应力交换。

---

## 5. Bochner 路线尚未形成障碍

加权调和映射的 Bochner 公式包含
\[
\operatorname{Ric}^{\sigma}_{B}
=\operatorname{Ric}_{B}+\operatorname{Hess}\sigma
\]
及因目标负曲率产生的非负项。若能证明沿整个连接器
\[
\operatorname{Ric}^{\sigma}_{B}\ge-\kappa g_B
\]
且负部足够小，则可能得到能量最大值原理或增长控制。

但现有方程只给
\[
\Delta\sigma=6e^{2\lambda}-|\nabla\sigma|^2,
\]
即 Hessian 的迹；其无迹部分由基底约束和轨道应力耦合，未有半正性。故“\(\operatorname{Hess}\sigma\ge0\)”不能作为已知事实，Bochner 公式目前仍含不可控的符号不定项。需要解决的精确对象是：

\[
\boxed{\text{在曲率缺陷受控时，能否从完整基底约束推出 }
(\operatorname{Ric}_B+\operatorname{Hess}\sigma)_-
\text{ 的定量上界？}}
\]

若不能，则负的漂移 Ricci/Hessian 区域正可允许轨道能量集中，而非产生 Lyapunov 障碍。

---

## 6. \(K\)-下降仍可利用的动态自由度

中心处
\[
K(0)=12,\qquad K'(0)=0,\qquad K''(0)\ge72,
\]
所以任何成功连接器都必须先经历 \(K\) 上升，再发生非线性翻转。返回前 \(x<0\)，故
\[
-2xK>0
\]
也反对下降。要使 \(K'<0\)，其余项必须以足够负的总量压过这一项。现有系统允许的机制为：

- **相位翻转：** 后期 \(b\) 与 \(\tau\) 同向，使
  \(-2\langle\tau,b\rangle<0\)；
- **面积梯度增长：** 增大 \(\langle h^2\rangle\)，即使 \(\langle e\rangle\) 不降也可降低 \(K\)；
- **权重重分布：** \(\rho\,ds\) 向较低 \(k=e-h^2\) 区域集中；
- **协方差工程：** 使 \(\operatorname{Cov}(v-u,k)\) 或 \(\langle vc\rangle\) 为负；
- **Noether-compatible 振荡：** 以零矩阵平均但大 \(L^2\) 的 \(b\) 实现上述相位交换；
- **径向/切向能量交换：** 将 \(U_s\) 能量转入 \(U_r\)，而不违反总二维调和映射结构。

综上，现有单调、凸性和守恒结构只给出精确常值出口的二维刚性，以及若干通量和零模约束；它们均不足以阻止完整耦合系统把 \(K\) 从 \(12\) 降至 \(6+2\delta\)。真正尚未解决的对象是一个能同时控制张力—速度相位、局部面积响应和协方差的非局部应力/Bochner 不等式；若不存在这种控制，上述空间重分布与相位自由度就是逃逸机制。
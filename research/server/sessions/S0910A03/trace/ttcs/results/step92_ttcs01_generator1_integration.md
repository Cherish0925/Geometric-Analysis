# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 92,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step92_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step92_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

The active Yau-26 subproblem is a free T^2-invariant two-ended approximately negative-Einstein connector. At its invariant minimizing separator C, let rho=e^sigma, s be base arclength, V=|II|^2=kappa^2+h_nu^2/2+e_nu/2+Q, h=sigma_s, and e_s=|U_s|^2. The verified formulas are: (i) for every smooth periodic phi, ∫rho V phi^2 <= ∫rho[(phi_s)^2+(3-E_nunu)phi^2]; (ii) R_q=-2h_s-(3/2)h^2-e_s/2; (iii) minimal Gauss R_q=-6+D-V, |D|<=4delta; (iv) Maxwell dq=±2rho * E_mix, with normalized |b|<=2sqrt(2)delta, and Q=(1/2)e^{-3sigma}q^T M^{-1}q; (v) orbit equation tau_sigma(U)=-grad Q+Z, |Z|<=2delta. Develop the strongest mathematically valid interaction among the full Jacobi form, scalar identity, Maxwell transport, and orbit equation. Look especially for a new nonlocal inequality that controls concentration of Q or e_nu on C, or else give an explicit formal/local-data mechanism showing why these equations still permit concentration. Keep all hypotheses and identify exact missing bridge; do not infer a pointwise bound from stability.

## Integrated Scientific Memo

## 1. 精确的 Jacobi–标量曲率融合

在 \(C\) 上令
\[
E_{\nu\nu}=E(\nu,\nu),\qquad
D=E(T,T)+E(V_1,V_1)+E(V_2,V_2)-E_{\nu\nu}.
\]
由
\[
-2h_s-\frac32h^2-\frac12e_s=-6+D-V
\]
得到逐点恒等式
\[
\boxed{
h_s=3-\frac D2+\frac V2-\frac34h^2-\frac14e_s.}
\tag{1}
\]

在完整稳定性形式中取
\[
\phi=\rho^{-1/2}y=e^{-\sigma/2}y.
\]
周期性积分分部给出
\[
\int_C\rho\,\phi_s^2ds
=\int_C\left(y_s^2+\frac12h_sy^2+\frac14h^2y^2\right)ds.
\]
代入 (1)，可得无权 Schrödinger 形式
\[
\boxed{
\int_C\left[
y_s^2+
\left(
\frac92-E_{\nu\nu}-\frac D4
-\frac34V-\frac18(h^2+e_s)
\right)y^2
\right]ds\ge0.}
\tag{2}
\]
记
\[
\mathcal W:=\frac34V+\frac18(h^2+e_s).
\]
因为
\[
\frac92-E_{\nu\nu}-\frac D4
=\frac92-\frac14T_E-\frac34E_{\nu\nu}
\le a_\delta:=\frac92+\frac32\delta,
\]
其中 \(T_E=E(T,T)+E(V_1,V_1)+E(V_2,V_2)\)，故
\[
\boxed{
\int_C\mathcal W y^2ds
\le\int_C(y_s^2+a_\delta y^2)ds
\quad\forall\,y\in C^\infty_{\rm per}(C).}
\tag{3}
\]

这是目前最干净的、完全由稳定性和两个标量曲率公式推出的非局部结论。特别要注意：它仍是容量控制，不是逐点控制。

---

## 2. Birman–Schwinger 型非局部浓度约束

设
\[
H_\delta=-\partial_s^2+a_\delta
\]
作用在长度 \(L_C\) 的周期圆上，其 Green 核为
\[
G_\delta(s,t)=
\frac{\cosh\!\big(\sqrt{a_\delta}(L_C/2-d_C(s,t))\big)}
{2\sqrt{a_\delta}\sinh(\sqrt{a_\delta}L_C/2)}.
\]
形式不等式 (3) 等价于
\[
\left\|\mathcal W^{1/2}H_\delta^{-1}\mathcal W^{1/2}\right\|\le1.
\tag{4}
\]
以 \(\mathcal W^{1/2}\) 为测试函数可得
\[
\boxed{
\iint G_\delta(s,t)\mathcal W(s)\mathcal W(t)\,dsdt
\le\int_C\mathcal W\,ds.}
\tag{5}
\]

由于
\[
\mathcal W\ge\frac34Q,\qquad
\mathcal W\ge\frac38e_\nu,
\]
分别有
\[
\boxed{
\iint G_\delta QQ\le\frac43\int_CQ\,ds,}
\qquad
\boxed{
\iint G_\delta e_\nu e_\nu\le\frac83\int_Ce_\nu\,ds.}
\tag{6}
\]
这里双重积分中的两个函数分别取值于 \(s,t\)。

若 \(Q_jds\rightharpoonup m\delta_{s_0}\)，则 (5) 给出原子质量上界
\[
\boxed{
m\le
\frac{8\sqrt{a_\delta}}3
\tanh\!\left(\frac{\sqrt{a_\delta}L_C}{2}\right).}
\tag{7}
\]
因此 Jacobi 形式禁止任意大的集中质量，但允许高度 \(\sim\ell^{-1}\)、宽度 \(\ell\to0\) 的尖峰。

用帐篷函数还可得到：对任意半径 \(r\le L_C/2\) 的内弧 \(I_r\)，
\[
\boxed{
\int_{I_r}\mathcal W\,ds
\le \frac8r+\frac83a_\delta r.}
\tag{8}
\]
右端在 \(r\downarrow0\) 时发散，准确体现了一维容量尺度。

---

## 3. Maxwell 传输确实进一步排除 \(Q|_C\) 的任意高度集中

令
\[
w=\sqrt{2Q}.
\]
将 Maxwell 传输限制到 \(C\) 的切向，得到
\[
\boxed{
\left|w_s+\frac32hw\right|
\le\frac12w\sqrt{e_s}+B_\delta,
\qquad B_\delta=2\sqrt2\,\delta.}
\tag{9}
\]
于是
\[
|w_s|\le c(s)w+B_\delta,\qquad
c=\frac32|h|+\frac12\sqrt{e_s},
\]
且
\[
c^2\le\frac52(h^2+e_s).
\tag{10}
\]

关键点是同一个 Jacobi 势 \(\mathcal W\) 同时控制 \(Q\) 的局部质量和传输成本 \(h^2+e_s\)。这消除了 Branch 2 所担心的 \(\rho\)-振荡障碍：使用无权共轭形式 (3)，不必在 \(\rho\) 与 \(\rho^{-3}\) 两种权之间转换。

例如，当 \(L_C\ge2/\sqrt{a_\delta}\) 时，在 \(Q\) 的最大点周围取
\[
r=a_\delta^{-1/2}.
\]
由 (8)，
\[
M_\delta(r):=\frac8r+\frac83a_\delta r
=\frac{32}{3}\sqrt{a_\delta}.
\]
中央弧内存在一点 \(s_0\) 满足
\[
Q(s_0)\le\frac{128}{9}a_\delta.
\]
同时，由 (8)、(10) 和 Cauchy–Schwarz，
\[
\int_{s_0}^{s_{\max}}c\,ds
\le \sqrt{\frac{320}{3}}.
\]
对 (9) 直接使用 Grönwall（不除以 \(w\)，故允许 \(Q=0\)），得到
\[
\boxed{
\sup_CQ
\le
\frac12
\exp\!\left(2\sqrt{\frac{320}{3}}\right)
\left(
\frac{16}{3}\sqrt{a_\delta}
+\frac{\sqrt2\,\delta}{\sqrt{a_\delta}}
\right)^2.}
\tag{11}
\]

若 \(L_C<2/\sqrt{a_\delta}\)，由 (3) 的常数测试及沿较短圆弧的传输，
\[
\boxed{
\sup_CQ
\le
\frac12e^{4\sqrt{10}}
\left(
\sqrt{\frac{8a_\delta}{3}}
+\frac{2\sqrt2\,\delta}{\sqrt{a_\delta}}
\right)^2.}
\tag{12}
\]

所以，在已给五条关系及 Maxwell 不变量范数公式成立的规范下，
\[
\boxed{\sup_CQ\le C(\delta)}
\tag{13}
\]
确实成立，且常数与 \(C\) 的长度及 \(\rho\) 的振荡无关。常数极粗，但结论是实质性的：**稳定性单独只控制容量；稳定性经过标量恒等式与 Maxwell 切向传输耦合后，排除了 \(Q\) 在 separator 上的任意高度集中。**

Branch 2 提出的 \(\rho^{-2}\) 测试也正确，并给出
\[
\int_C\rho^{-3}\left(\frac72h^2+\frac12e_s\right)ds
\le(9+5\delta)\int_C\rho^{-3}ds,
\tag{14}
\]
但它不是闭合 \(Q|_C\) 所必需的最强路线；无权共轭 (2) 避免了其交叉权重问题。其声称 \(Q_{\max}\to0\) 如 \(\ell^2/\log^2(1/\delta)\) 的结论并未由现有假设严格推出，应删除。

---

## 4. \(e_\nu\) 仍可在给定方程层面任意集中

不能由“\(Q\) 有界”加 orbit equation 直接推出 \(e_\nu\) 的逐点界。方程
\[
\tau_\sigma(U)=-\nabla Q+Z
\tag{15}
\]
只控制 \(U\) 的加权二阶迹；在单条曲线上的数据中，它可以通过选择 \(\nabla_\nu U_\nu\) 吸收任意大的第一法向导数 \(U_\nu\)。因此 Branch 2 所称“有界 tension 经椭圆估计控制 \(e_\nu\)”缺少区域几何、边界数据和椭圆正则性尺度，不能成立于当前假设下。

一个明确的形式局部数据族如下。固定长度 \(L\)，令
\[
m_*:=2\sqrt3\tanh\!\left(\frac{\sqrt3L}{2}\right),
\]
取 \(0<m<m_*\)，并令
\[
P_\ell(s)=\frac m\ell\chi(s/\ell),
\qquad \chi\ge0,\quad\int\chi=1
\]
为光滑周期尖峰。对充分小的 \(\ell\)，
\[
-\partial_s^2+3-P_\ell\ge0
\tag{16}
\]
作为二次型成立；极限是强度 \(m\) 的周期点相互作用，其零能阈值即 \(m_*\)。

在 \(C\) 上指定
\[
\rho=1,\quad h=0,\quad D=E_{\nu\nu}=0,
\]
\[
q=Q=b=0,\qquad \kappa=h_\nu=0,
\]
以及
\[
\boxed{
e_\nu=2P_\ell,\qquad
V=P_\ell,\qquad
e_s=12+2P_\ell.}
\tag{17}
\]
则
\[
R_q=-\frac12e_s=-6-P_\ell=-6+D-V,
\]
Jacobi 形式恰为
\[
\int P_\ell\phi^2\le\int(\phi_s^2+3\phi^2),
\]
而 Maxwell 方程平凡成立。

目标映射的 jets 也可形式实现：选取 \(\mathbb H^2\) 中闭合浸入曲线，使
\[
|U_s|^2=12+2P_\ell,
\qquad |U_\nu|^2=2P_\ell,
\]
再指定二阶法向 jet
\[
\nabla_\nu U_\nu=-\nabla_sU_s
\]
以实现 \(\tau_\sigma(U)=0\)。于是
\[
\sup_Ce_\nu\sim\ell^{-1}\to\infty,
\qquad
\int_Ce_\nu ds\to2m.
\tag{18}
\]

这严格说明：**在题给 Jacobi、标量、Gauss、Maxwell 和 orbit trace 方程的局部 jet 层面，\(e_\nu\) 可任意高地集中。** 它不是完整管状邻域解，因为尚未施加其余水平约化方程、Codazzi–Bianchi 相容性以及两端全局条件。

---

## 5. 精确未闭合桥梁

目前得到的是
\[
\sup_CQ\le C(\delta),
\]
而旧 resolvent 比较所需的是
\[
Q_+=\sup_BQ.
\]
沿法向 Maxwell 传输为
\[
\left|\partial_\nu w+\frac32h_\nu w\right|
\le\frac12w\sqrt{e_\nu}+B_\delta.
\tag{19}
\]
从 \(C\) 向基底内部传播 \(Q\) 的界，需要控制每条法向弧上的
\[
\boxed{
\int\bigl(|h_\nu|+\sqrt{e_\nu}\bigr)\,dn.}
\tag{20}
\]
separator Jacobi 形式只控制 \(n=0\) 截面上的切向容量，并不提供 (20)。orbit equation 只控制二阶导数的迹，不能单独控制 \(U_\nu\)；而 Maxwell 假设仅给 \(|b|\le2\sqrt2\delta\)，没有 \(Db\) 控制，故也不能合法地构造具有受控右端的二阶 \(Q\)-方程。

因此精确剩余对象是一个**管状 collar 正则性/传输估计**，例如以下任一足够强的结果：

\[
\sup_{\text{collar}}e
\quad\text{或}\quad
\int_{\text{normal arc}}\sqrt e,
\quad\text{或}\quad
\int_{\text{collar}}|DdU|^2
\]
由 separator 数据和 \(\delta\) 一致控制；并须兼容剩余水平方程及 Codazzi–Bianchi 关系。缺少这一桥梁时，不能把 \(Q|_C\) 的新界提升为 \(Q_+\) 界，也不能排除 \(e_\nu\) 的 separator-jet 尖峰，更不能恢复带 twist 的全局 resolvent 矛盾。
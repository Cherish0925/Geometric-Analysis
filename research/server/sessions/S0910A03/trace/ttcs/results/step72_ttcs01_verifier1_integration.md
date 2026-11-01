# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 72,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step72_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step72_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following structural properties of the T²-invariant Einstein system in conformal gauge on [0,R]×S¹.

Metric: g = e^{2φ}(dt²+dz²) + e^{2b}dx² + e^{2c}dy², where (t,z) is the base 2D plane (z periodic), and x,y are T² quotient directions.

Claim 1 (Anisotropy drift-Laplacian): For exact Ric+3g=0, the difference δ=b-c satisfies Δδ + ∇σ·∇δ = 0 where σ=b+c and Δ,∇ are the flat 2D operators on (t,z). This follows from subtracting the xx and yy Einstein equations.

Claim 2 (Maximum principle): On the domain [0,R]×S¹ with reflection conditions δ_t(0,z)=0, the strong maximum principle and Hopf lemma force: either δ is constant, or max_z δ(R,z) ≥ max_z δ(0,z) and min_z δ(R,z) ≤ min_z δ(0,z). The oscillation of the T² anisotropy at the outer boundary is at least as large as at the center.

Claim 3 (Orbit-area equation): Setting ρ=e^{b+c}, the orbit area satisfies Δ_flat(ρ) = (6e^{2φ} - |∇δ|²)·ρ. For isotropic solutions (δ=0), ρ is strictly subharmonic.

Claim 4 (Isotropic impossibility): For isotropic g=dt²+f²h on T³ (3D fiber), the normal Einstein equation gives s'+s²=1 while the tangential gives s'+3s²=3, where s=f'/f. These are algebraically inconsistent with s(0)=0.

Claim 5 (Forced compatibility): For approximate Einstein with |Ric+3g|_op ≤ δ on T³ outer boundary in flat conformal class, the Gauss equation forces δ ≥ (9-H²)/6 where H is mean curvature. Combined with the interior weighted identity (δ ≥ Ce^{-2R} from the normal balance), the constraints are compatible: take H=3-ε, δ~ε, R~(1/2)log(6/ε).

For each claim: (a) verify the derivation, (b) check whether the maximum principle argument is correct for the Neumann boundary at t=0, (c) identify whether the anisotropy preservation BLOCKS cusp matching or merely CONSTRAINS it.

Key question: Does the drift-Laplacian δ equation prevent the construction of approximate Einstein metrics on graph manifolds with Koiso centers? Or does the anisotropy propagation to the boundary merely require matching to an anisotropic cusp (which is what the lattice quotient construction provides)?

## Integrated Scientific Memo

## 核验结论

记
\[
d:=b-c,\qquad \sigma:=b+c,\qquad \rho:=e^\sigma,
\]
并用 \(\eta\) 表示近似 Einstein 误差：
\[
\mathcal E:=\operatorname{Ric}_g+3g,\qquad
\|\mathcal E\|_{\mathrm{op}}\le \eta .
\]

总体结论：

- **Claim 1 正确。**
- **Claim 2 正确；对非恒定精确解可加强为严格不等式。**
- **Claim 3 的公式错误。** 正确公式不含 \(-|\nabla d|^2\)：
  \[
  \Delta_{\rm flat}\rho=6e^{2\phi}\rho .
  \]
- **Claim 4 正确**，但须补充：切向 Einstein 方程先迫使三维纤维 \(h\) 为 Einstein，因而在 \(T^3\) 上平坦。
- **Claim 5 作为“必要条件彼此兼容”的陈述基本正确**，但长度估计需区分 \(H(R)=3\) 与 \(H(R)=3-\varepsilon\)，并区分 Gaussian 距离和 conformal-gauge 坐标 \(t\)。
- 漂移 Laplace 方程对**精确、有限距离、平坦 cusp 匹配**形成真实障碍；但它**不排除近似 Einstein 构造**。不过，“换成各向异性的平坦格点 cusp”只能改变 \(d\) 的常数部分，不能吸收 Koiso 中心的 \(z\)-振荡。因此“lattice quotient 已经解决 anisotropy”这一较强说法不成立。

---

## 1. 各向异性方程

由所给 \(xx,yy\) 混合分量，
\[
\mathcal E_x
=3-e^{-2\phi}\bigl(\Delta b+\nabla\sigma\cdot\nabla b\bigr),
\]
\[
\mathcal E_y
=3-e^{-2\phi}\bigl(\Delta c+\nabla\sigma\cdot\nabla c\bigr),
\]
其中 \(\Delta,\nabla\) 是 \((t,z)\) 上的平坦算子。相减得到
\[
\mathcal E_x-\mathcal E_y
=-e^{-2\phi}\left(\Delta d+\nabla\sigma\cdot\nabla d\right).
\]

因此精确 Einstein 情形满足
\[
\boxed{\Delta d+\nabla\sigma\cdot\nabla d=0,}
\]
等价地
\[
\boxed{\operatorname{div}(e^\sigma\nabla d)=0.}
\]

Claim 1 正确。

近似 Einstein 情形则为
\[
\boxed{
\Delta d+\nabla\sigma\cdot\nabla d
=-e^{2\phi}(\mathcal E_x-\mathcal E_y),
}
\]
故
\[
\left|\Delta d+\nabla\sigma\cdot\nabla d\right|
\le 2\eta e^{2\phi}.
\]
只有误差的 \(x/y\) 差分分量能够改变这一模式。

---

## 2. Neumann 反射边界与最大值原理

算子
\[
L_\sigma=\Delta+\nabla\sigma\cdot\nabla
=e^{-\sigma}\operatorname{div}(e^\sigma\nabla\,\cdot)
\]
在紧圆柱上均匀椭圆。若 \(d\) 非恒定：

1. 强最大值原理排除内部全局极值；
2. 在 \(t=0\) 上，外法向为 \(-\partial_t\)；
3. 若非恒定解在该边界达到全局最大值，Hopf 引理要求外法向导数非零；
4. 反射条件
   \[
   d_t(0,z)=0
   \]
   与此矛盾。

对 \(-d\) 同理。因此全局最大、最小必须在 \(t=R\) 上取得，并且
\[
\boxed{
\max_z d(R,z)>\max_z d(0,z),\qquad
\min_z d(R,z)<\min_z d(0,z)
}
\]
对每个非恒定精确解成立。于是
\[
\boxed{\operatorname{osc}_{t=R}d>
\operatorname{osc}_{t=0}d.}
\]

Claim 2 的弱不等式正确，且可加强为严格不等式。

还有一个直接的刚性结论：若外边界
\[
d(R,z)\equiv D
\]
为常数，则令 \(u=d-D\)，利用 \(u(R,\cdot)=0\)、\(u_t(0,\cdot)=0\)，有
\[
0=\int u\,\operatorname{div}(e^\sigma\nabla u)
=-\int e^\sigma|\nabla u|^2,
\]
从而
\[
\boxed{d\equiv D.}
\]
所以精确反射解若在有限距离匹配固定形状的平坦 cusp，则 \(x/y\) 长度比必须在整个 core 上恒定。

---

## 3. 轨道面积公式：Claim 3 必须修正

相加 \(xx,yy\) 方程得到
\[
\mathcal E_x+\mathcal E_y
=
6-e^{-2\phi}\left(\Delta\sigma+|\nabla\sigma|^2\right).
\]
又因为
\[
\frac{\Delta\rho}{\rho}
=\Delta\sigma+|\nabla\sigma|^2,
\]
精确方程是
\[
\boxed{\Delta_{\rm flat}\rho=6e^{2\phi}\rho.}
\]

不存在 \(-|\nabla d|^2\rho\) 项。原因是所有二次项恰好组合为
\[
|\nabla b|^2+2\nabla b\cdot\nabla c+|\nabla c|^2
=|\nabla(b+c)|^2.
\]

因此正确结论更强：
\[
\boxed{\Delta\rho>0}
\]
对所有精确解成立，而不只对 \(d=0\) 成立。

近似情形为
\[
\boxed{
\Delta\rho=e^{2\phi}
\bigl(6-\mathcal E_x-\mathcal E_y\bigr)\rho.
}
\]
由 \(|\mathcal E_x|,|\mathcal E_y|\le\eta\)，当 \(\eta<3\) 时仍严格次调和。

配合反射条件 \(\rho_t(0,z)=0\)，积分可得
\[
\int_{S^1}\rho_t(R,z)\,dz
=
6\int_0^R\!\!\int_{S^1}e^{2\phi}\rho\,dz\,dt>0
\]
（精确情形）。

---

## 4. 各向同性 warped-product 不可能性

设
\[
g=dt^2+f(t)^2h,\qquad s=f'/f,
\]
其中 \(h\) 是 \(T^3\) 上固定度量。

法向方程：
\[
\operatorname{Ric}_{tt}=-3\frac{f''}{f}=-3
\]
给出
\[
\boxed{s'+s^2=1.}
\]

切向方程为
\[
\operatorname{Ric}_g|_{T^3}
=
\operatorname{Ric}_h-
\bigl(ff''+2(f')^2\bigr)h.
\]
若四维度量在区间上 Einstein，则该张量方程迫使 \(h\) 为 Einstein。三维 Einstein 度量具有常截面曲率，而 \(T^3\) 上只能是平坦情形。因此
\[
\frac{f''}{f}+2s^2=3,
\]
即
\[
\boxed{s'+3s^2=3.}
\]

相减得到
\[
s^2=1,
\]
与反射中心条件 \(s(0)=0\) 矛盾。更直接地，在 \(t=0\) 两式分别要求
\[
s'(0)=1,\qquad s'(0)=3.
\]

故 Claim 4 正确。Step 70 笔记中的
\[
s=\tanh(\sqrt3\,t)
\]
不正确；仅解法向方程时应为
\[
s=\tanh t,\qquad H=3\tanh t,
\]
但此解不满足切向 Einstein 方程。

进一步，任何仅依赖 \(t\) 的对角平坦 \(T^3\) 纤维 ansatz
\[
g=dt^2+\sum_{i=1}^3e^{2\psi_i(t)}dx_i^2
\]
也不可能具有全测地中心。切向方程给
\[
\psi_i''+\psi_i'\sum_j\psi_j'=3.
\]
在 \(\psi_i'(0)=0\) 时，每个 \(\psi_i''(0)=3\)，故总和为 \(9\)；法向方程却要求总和为 \(3\)。因此成功的 core 必须真正依赖 \(z\)。

---

## 5. Gauss 约束和法向加权恒等式

### 5.1 平坦外边界的 Gauss 约束

令外边界 \(\Sigma^3\) 本征平坦，第二基本形式为 \(A\)，平均曲率为 \(H\)，法向为 \(\nu\)。Gauss 标量方程：
\[
0=R_\Sigma
=R_g-2\operatorname{Ric}_g(\nu,\nu)+H^2-|A|^2.
\]
写
\[
\operatorname{Ric}_g=-3g+\mathcal E,
\]
则
\[
0=-6+\operatorname{tr}_\Sigma\mathcal E
-\mathcal E_{\nu\nu}+H^2-|A|^2.
\]
因为
\[
\bigl|\operatorname{tr}_\Sigma\mathcal E
-\mathcal E_{\nu\nu}\bigr|\le4\eta,
\qquad
|A|^2\ge H^2/3,
\]
所以
\[
6\le4\eta+\frac23H^2,
\]
即
\[
\boxed{\eta\ge\frac{9-H^2}{6}.}
\]

若
\[
H=3-\varepsilon,
\]
则
\[
\boxed{\eta\ge
\varepsilon-\frac{\varepsilon^2}{6}.}
\]

该点态结论需要外边界本征平坦。若仅与平坦度量共形，则一般只能直接得到积分版本。

### 5.2 法向平衡的正确符号和端点依赖

在 Gaussian 距离 \(r\) 中写
\[
g=dr^2+h_r,\qquad A=\tfrac12h_r',\qquad A(0)=0,
\]
并令
\[
B=A-I,\qquad \beta=H-3.
\]
则
\[
\mathcal E_{\nu\nu}=-H'-|A|^2+3
\]
给出
\[
\boxed{\beta'+2\beta+|B|^2=-\mathcal E_{\nu\nu}.}
\]
由 \(\beta(0)=-3\)，
\[
\boxed{
e^{2R}\beta(R)
=-3-\int_0^Re^{2r}|B|^2\,dr
-\int_0^Re^{2r}\mathcal E_{\nu\nu}\,dr.
}
\]
Step 70 笔记最后一项的符号与
\(\mathcal E=\operatorname{Ric}+3g\) 的定义不一致；绝对值估计不受影响。

若 \(H(R)=3\)，则
\[
\boxed{\eta\ge\frac{6}{e^{2R}-1}.}
\]
若 \(H(R)=3-\varepsilon\)，正确必要关系是
\[
\boxed{
3e^{-2R}
\le
\varepsilon+\frac{\eta}{2}(1-e^{-2R}).
}
\]
因此当端点有曲率亏损 \(\varepsilon\) 时，不能把法向恒等式单独表述为纯粹的 \(\eta\gtrsim e^{-2R}\)；亏损本身可以承担初始不平衡的一部分。

结合 Gauss 约束，尺度
\[
\eta\asymp\varepsilon,\qquad
e^{-2R}\asymp\varepsilon,
\]
即
\[
R\sim\frac12\log\frac6\varepsilon
\]
确实相容。但这只证明必要条件相容，并不建立近似 core 的存在性。

此外，这里的 \(R\) 是 Gaussian 法向距离。原 conformal gauge 中 \(e^{2\phi}(dt^2+dz^2)\) 的 \(t\) 一般不是 Gaussian 距离，除非另有坐标转换或双边弧长控制。

---

## 6. 漂移方程究竟阻断还是约束 cusp 匹配？

必须区分三种各向异性：

1. \(d=b-c\)：\(x/y\) 轨道内部的形状比；
2. 平坦 cusp 格点的常数矩形比例；
3. 第二基本形式 \(A\) 的外在膨胀各向异性。

\(H\to3\)、\(A\to I\) 与非正方形平坦格点完全相容，因为格点矩形比例只是 \(d\) 的常数部分。

但对 Step 69 的显式 Koiso 中心，
\[
q_N=u^4\left(
dz^2+e^{2f(z)}\frac{dx^2}{N^2}
+e^{-2f(z)}\frac{dy^2}{N^2}
\right),
\]
有
\[
d_N=2f(z),
\]
其振荡与 \(N\) 无关。平坦 translational cusp 在适配仿射坐标中只有
\[
d=\text{常数}.
\]
改变 \(x,y\) 周期只给 \(d\) 加常数，不改变
\[
\operatorname{osc} d.
\]

因此：

- 对**精确 Einstein 解**，非恒定 Koiso 中心的 \(d(z)\) 不可能在有限距离直接匹配任何固定平坦 cusp，包括矩形、非正方形 cusp；
- rank-two lattice quotient 解决的是总体尺度以及 \(z\) 方向相对于 \(x,y\) 方向的格点类型，不会消除 \(x/y\) 振荡模式；
- 对**近似 Einstein 解**，方程有源，因此没有绝对 no-go：
  \[
  \operatorname{div}(e^\sigma\nabla d)
  =-e^{\sigma+2\phi}(\mathcal E_x-\mathcal E_y).
  \]
  所需振荡衰减必须由误差差分、权重退化、足够长的过渡区，或不同的中心数据承担。

在固定长度、且 \(\phi,\sigma\) 一致受控的圆柱上，若外边界 \(d\) 为常数，则能量与 Poincaré/椭圆估计会迫使中心振荡随 \(\eta\to0\) 消失。因此仅令格点参数 \(N\to\infty\) 并不足以使误差自动趋零；必须展示相关权重或长度如何使有源转移在定量上可行。

## 最终判断

漂移 Laplace 方程：

- **阻断**非恒定 Koiso 各向异性到固定平坦 cusp 的有限距离**精确**匹配；
- 仅仅“改用 anisotropic lattice cusp”并不能解除该阻断，因为它只提供常数各向异性；
- **不阻断一般的近似 Einstein 构造**，但施加了一个明确的定量任务：必须控制
  \[
  \mathcal E_x-\mathcal E_y
  \]
  如何消除中心的 \(z\)-振荡，同时满足 \(R\sim\frac12\log(1/\eta)\) 的法向尺度及 Gauss 边界约束。

目前真正未解决的科学对象是：构造并估计一个 \(z\)-非齐次的椭圆边值解或近似解，使其从全测地 Koiso 中心出发，在长 collar 上把非恒定 \(d\) 转化为常数 cusp 数据，同时 Einstein 缺陷一致趋零。
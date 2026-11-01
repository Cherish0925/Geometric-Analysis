# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 85,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step85_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step85_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following Bochner comparison theorem for the OT orbit-map energy density and its application to reflected Einstein connectors.

SETUP: Consider a 4D Einstein metric g with Ric = -3g having T² symmetry, in orthogonally transitive form g = e^{2λ}(dr² + dz²) + e^σ M_{ab}dξ^a dξ^b where M ∈ SL(2)/SO(2) ≅ H². The orbit map U: (B², γ_B) → (H², g_{H²}) satisfies the σ-weighted harmonic map equation div(e^σ M⁻¹dM) = 0, equivalently τ_σ(U) = 0 where L = Δ_{γ_B} + ⟨∇σ,∇·⟩ = ρ⁻¹div(ρ∇) with ρ = e^σ.

CLAIM 1 (Bochner formula): For e = |dU|²_{γ_B}, the exact σ-harmonic case gives
½Le = |DdU|² + ½|dU(∇σ)|² + Q(A) - 3e
where A is the Gram matrix A_{ij} = h(dU(e_i), dU(e_j)), and the Einstein base equation Ric_B - Hess σ = -3γ_B + ½dσ⊗dσ + ½U*h_{H²} + E_B has been used with E_B = 0.

CLAIM 2 (Q bound): Q(A) = ½tr(A²) + 2det(A) ≥ ½(tr A)² = ½e², with equality iff det A = 0 (rank-one dU).

CLAIM 3 (Maximum principle): ½Le ≥ ½e(e-6), so at any interior maximum Le ≤ 0 implies e ≤ 6. On a reflected connector [0,R]×S¹, reflection removes the center boundary, giving sup e ≤ max{6, sup_{exit} e}.

CLAIM 4 (Center identity): At a reflected center (r=0) with scalar curvature -6 on the T³ slice, U_r(0,z) = 0 by reflection, so e(0,z) = |U_s|²(0,z) where s is the physical z-arclength. The Step 82 identity K(0) = ⟨|U_s|² - H²⟩(0) = 12, with H(0) = 0, gives ⟨e(0,·)⟩_μ = 12.

CLAIM 5 (Contradiction): If sup_{exit} e < 12, then sup e < 12, but ⟨e(0,·)⟩_μ = 12 > sup e. This is impossible since ⟨e⟩ ≤ sup e for any positive measure. So every exact reflected OT Einstein connector must have sup_{exit} e ≥ 12.

CLAIM 6 (Forced case identity): For τ_σ = F ≠ 0, the identity ⟨dU, Dτ_σ⟩ = div_σ(V) - |τ_σ|² holds where V(·) = ⟨dU(·), τ_σ⟩. This converts the forced Bochner formula to ½Le = |DdU|² + div_σ(V) - |F|² + Q - 3e + nonneg + E_B·A.

Verify each claim independently. Check all coefficients, signs, the H² curvature term (K = -1), the drift curvature convention, the conformal gauge identification e(0,z) = |U_s|²(0,z), and whether the maximum principle applies to the operator L on a compact reflected domain. Identify any gap or coefficient error.

## Integrated Scientific Memo

# 核验结论

在题设的 \(\mathbb H^2\) 归一化（截面曲率 \(-1\)）和基底方程
\[
\operatorname{Ric}_B-\nabla^2\sigma
=-3\gamma_B+\frac12d\sigma\otimes d\sigma
+\frac12U^*h_{\mathbb H^2}+E_B
\]
下，Claims 1、2、3、5、6 正确。Claim 4 混淆了两个不同变量，等式
\(\langle e(0)\rangle_\mu=12\) 一般不成立；正确结论是
\[
\boxed{\langle e(0,\cdot)\rangle_\mu
=12+\big\langle |(\log\rho)_s|^2\big\rangle_\mu\ge12.}
\]
这一修正反而加强 Claim 5。

---

## 1. Bochner 公式

令
\[
e=|dU|^2,\qquad U_i=dU(e_i),\qquad
A_{ij}=\langle U_i,U_j\rangle.
\]
对
\[
L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle,
\qquad
\tau_\sigma=\tau+dU(\nabla\sigma),
\]
加权 Bochner 公式为
\[
\frac12Le
=
|DdU|^2+\langle dU,D\tau_\sigma\rangle
+(\operatorname{Ric}_B-\nabla^2\sigma):A
-\sum_{i,j}\langle R^{\mathbb H^2}(U_i,U_j)U_j,U_i\rangle .
\]

### 漂移曲率符号

这里确实是
\[
\boxed{\operatorname{Ric}_B-\nabla^2\sigma},
\]
不是加号。圆 cusp 检验
\[
\gamma_B=dr^2+e^{2r}dz^2,\qquad \sigma=2r
\]
给出正交标架下
\[
\operatorname{Ric}_B-\nabla^2\sigma
=\operatorname{diag}(-1,-3)
=-3I+\tfrac12d\sigma\otimes d\sigma,
\]
与所用基底方程一致。

### 目标曲率项

当 \(K_{\mathbb H^2}=-1\) 时，
\[
-\sum_{i,j}\langle R(U_i,U_j)U_j,U_i\rangle
=2\det A.
\]
另一方面，
\[
\left(\tfrac12U^*h\right):A=\tfrac12\operatorname{tr}(A^2),
\qquad
\left(\tfrac12d\sigma\otimes d\sigma\right):A
=\tfrac12|dU(\nabla\sigma)|^2.
\]
因此在 \(E_B=0\)、\(\tau_\sigma=0\) 时，
\[
\boxed{
\frac12Le
=
|DdU|^2+\frac12|dU(\nabla\sigma)|^2
+\frac12\operatorname{tr}(A^2)+2\det A-3e.
}
\]
所以 Claim 1 的所有系数和符号正确。

---

## 2. \(Q(A)\) 的估计

定义
\[
Q(A)=\frac12\operatorname{tr}(A^2)+2\det A.
\]
对 \(2\times2\) 矩阵，
\[
\operatorname{tr}(A^2)=(\operatorname{tr}A)^2-2\det A,
\]
故
\[
Q(A)
=\frac12(\operatorname{tr}A)^2+\det A.
\]
由于 \(A\) 是 Gram 矩阵，\(A\ge0\)，从而
\[
\boxed{Q(A)\ge\frac12(\operatorname{tr}A)^2=\frac12e^2.}
\]
等号当且仅当
\[
\det A=0\iff \operatorname{rank}dU\le1.
\]
严格说应写“秩至多一”；零映射也属于等号情形。非零时才是 rank one。Claim 2 除此措辞外正确。

---

## 3. 最大值原理

由上述公式舍去非负项可得
\[
\boxed{\frac12Le\ge\frac12e(e-6).}
\]
在内点最大值处，
\[
\nabla e=0,\qquad \Delta e\le0,
\]
因而漂移项消失且 \(Le\le0\)，于是
\[
e(e-6)\le0.
\]
又 \(e\ge0\)，故内点最大值满足 \(e\le6\)。

若 \(r=0\) 的“反射”是光滑等距反射，则可沿中心将所有数据光滑加倍；\(r=0\) 成为加倍柱面内部的圆，\(L\) 仍是光滑、严格椭圆的漂移算子。紧致性保证最大值达到，因此
\[
\boxed{
\sup_\Omega e\le
\max\left\{6,\sup_{\{r=R\}}e\right\}.
}
\]
所以 Claim 3 正确，但必须明确假设是**光滑反射延拓**，而不只是形式上的 Neumann 条件。

---

## 4. 中心恒等式：Claim 4 的变量错误

在共形基底上，
\[
n=e^{-\lambda}\partial_r,\qquad
\partial_s=e^{-\lambda}\partial_z.
\]
因此
\[
e=e^{-2\lambda}\bigl(|U_r|^2+|U_z|^2\bigr)
=|U_n|^2+|U_s|^2.
\]
反射给出 \(U_r(0,z)=0\)，所以
\[
\boxed{e(0,z)=|U_s(0,z)|^2.}
\]
这一共形规范识别正确。

错误发生在 Step 82 的 \(K\) 被改写成含径向平均曲率 \(H\)。Step 82 实际定义的是
\[
K=\left\langle |U_s|^2-h^2\right\rangle_\mu,
\qquad
h=(\log\rho)_s,
\]
其中 \(h\) 是中心切片上的**切向 orbit-area 导数**。它不是径向平均曲率
\[
H_{\rm rad}=u+v.
\]
反射确实给出 \(H_{\rm rad}(0)=0\)，但并不推出 \(h(0,z)=0\)。

切片标量曲率公式是
\[
R(q_0)
=-2h_s-\frac32h^2-\frac12|U_s|^2.
\]
对 \(d\mu=\rho\,ds\) 积分，并使用
\[
\int \rho h_s\,ds=-\int\rho h^2\,ds,
\]
得到
\[
\langle R(q_0)\rangle_\mu
=-\frac12\left\langle |U_s|^2-h^2\right\rangle_\mu
=-\frac12K.
\]
反射固定切片全测地，而
\[
R(g)=-12,\qquad \operatorname{Ric}(n,n)=-3,
\]
故 Gauss 公式给出点态
\[
R(q_0)=-12-2(-3)=-6.
\]
于是
\[
K(0)=12,
\]
但真正的能量平均为
\[
\boxed{
\langle e(0,\cdot)\rangle_\mu
=\langle|U_s|^2\rangle_\mu
=12+\langle h^2\rangle_\mu\ge12.
}
\]
仅当 \(\rho\) 沿中心圆恒定，即 \(h\equiv0\) 时，才有
\(\langle e(0)\rangle_\mu=12\)。

---

## 5. 出口能量阻碍

令
\[
m_0=\langle e(0,\cdot)\rangle_\mu
=12+\langle h^2\rangle_\mu.
\]
正测度平均满足
\[
m_0\le\sup_\Omega e.
\]
结合最大值估计，
\[
12+\langle h^2\rangle_\mu
\le
\max\left\{6,\sup_{\rm exit}e\right\}.
\]
左侧严格大于 \(6\)，所以必有
\[
\boxed{
\sup_{\rm exit}e
\ge12+\langle h^2\rangle_\mu
\ge12.
}
\]
因此 Claim 5 的结论正确，且可加强如上。

题设所写“若 \(\sup_{\rm exit}e<12\)，则 \(\sup e<12\)”可以成立，因为
\[
\sup e\le\max\{6,\sup_{\rm exit}e\}<12.
\]
与中心平均至少为 \(12\) 矛盾。应将其中的中心等式改为不等式。

---

## 6. 强迫情形

设
\[
\tau_\sigma(U)=F,
\qquad
V(X)=\langle dU(X),F\rangle .
\]
则
\[
\begin{aligned}
\operatorname{div}_\sigma V
&=\langle\tau+dU(\nabla\sigma),F\rangle
 +\langle dU,DF\rangle\\
&=|F|^2+\langle dU,D\tau_\sigma\rangle .
\end{aligned}
\]
所以
\[
\boxed{
\langle dU,D\tau_\sigma\rangle
=\operatorname{div}_\sigma V-|F|^2.
}
\]
代入带 \(E_B\) 的 Bochner 公式得
\[
\boxed{
\frac12Le
=
|DdU|^2+\operatorname{div}_\sigma V-|F|^2
+Q(A)-3e
+\frac12|dU(\nabla\sigma)|^2
+E_B:A.
}
\]
Claim 6 的系数、符号均正确。

不过该恒等式不能仅凭 \(|F|\) 的点态控制直接重复最大值原理，因为
\(\operatorname{div}_\sigma V\) 含 \(DF\)。加权分部积分给出
\[
\int_\Omega \eta^2\rho\,\operatorname{div}_\sigma V
=
-2\int_\Omega \eta\rho\,
\langle dU(\nabla\eta),F\rangle
+\int_{\partial\Omega}\eta^2\rho\,V(\nu),
\]
所以在无边界通量或明确控制边界通量时，可以消除 \(DF\)。但由此得到长度和几何一致的 \(L^\infty\) 估计，还需要统一的加权 Sobolev/Moser 常数；现有材料没有证明这一点。

---

## 最终判定表

| Claim | 判定 | 修正或条件 |
|---|---|---|
| 1 | 正确 | 漂移曲率为 \(\operatorname{Ric}_B-\nabla^2\sigma\)；\(K_{\mathbb H^2}=-1\) 给 \(+2\det A\) |
| 2 | 正确 | 等号条件应写 \(\operatorname{rank}dU\le1\) |
| 3 | 正确 | 需要中心处存在光滑反射加倍，且域紧致 |
| 4 | 部分错误 | \(e(0)=|U_s|^2\) 正确；一般应为 \(\langle e(0)\rangle=12+\langle h^2\rangle\ge12\) |
| 5 | 正确且可加强 | \(\sup_{\rm exit}e\ge12+\langle h^2\rangle\ge12\) |
| 6 | 正确 | 点态式含 \(DF\)；积分式另有边界通量，统一 Moser 估计尚未建立 |

因此，精确反射 OT Einstein connector 的出口能量阻碍是严格成立的；唯一实质性错误是 Claim 4 将切向 \(h=(\log\rho)_s\) 与径向 \(H=u+v\) 混淆。
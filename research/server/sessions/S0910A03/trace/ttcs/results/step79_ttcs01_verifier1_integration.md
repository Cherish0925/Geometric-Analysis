# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 79,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step79_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step79_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following structural reduction for orthogonally transitive T²-invariant 4D Einstein metrics with Ric = -3g.

Metric: g = e^{2λ}(dr²+dz²) + G_{ab}(r,z)dξ^a dξ^b with G = e^σ M, det M = 1.

1. AREA EQUATION: σ_rr + σ_zz + σ_r² + σ_z² = 6 e^{2λ}. Check the coefficient 6.

2. ORBIT MAP EQUATION: div(e^σ M^{-1}dM) = 0 (weighted harmonic map to H² = SL(2)/SO(2)).
  In H² polar coords: d-eq: (e^σ d_r)_r + (e^σ d_z)_z = e^σ sinh(d)cosh(d)|∇ψ|²
  Conservation: div(e^σ sinh²(d) ∇ψ) = 0

3. BASE CONFORMAL: Δλ = (|∇σ|² - e_{H²})/4 where e_{H²} = H²-energy of orbit map.

4. TWIST VANISHING: For commuting Killing fields on Ric=-3g, twist scalars are constant. Reflection reverses orientation ⟹ twist = 0 on exact reflected cores.

5. VII_0 SPECIALIZATION: Setting ψ=kz, d=d(r), the d-equation becomes (e^σ d')' = e^σ sinh(d)cosh(d)k², whose RHS is always positive. This is the VII_0 barrier mechanism.

6. STEP 73 RECOVERY: On the cusp background with diagonal orbit (α=v, β=0), the orbit equation gives v_rr + 3v_r + e^{-2r}v_zz = 0, recovering Step 73.

Verify each component. Check whether the coefficient in the area equation is 6 (not 3). Check whether the orbit equation is exactly a weighted harmonic map. Check the conservation law. Does the mechanism analysis correctly identify that general 2-variable H² maps can break the VII_0 barrier through angular momentum absorption by the growing weight e^σ? Are there additional conservation laws or monotonicity constraints in the coupled system that could prevent this?

## Integrated Scientific Memo

## 核验结论

令
\[
\rho=e^\sigma=\sqrt{\det G},\qquad
A_i=G^{-1}\partial_iG=\sigma_iI+B_i,\qquad
B_i=M^{-1}\partial_iM,
\]
其中 \(i=r,z\)，且 \(\operatorname{tr}B_i=0\)。轨道块 Ricci 端同态为
\[
(\operatorname{Ric}_g)^a{}_b
=-\frac{e^{-2\lambda}}{2\rho}\,
\partial_i(\rho A_i)^a{}_b.
\]
因此 \(\operatorname{Ric}=-3g\) 给出
\[
\partial_i(\rho A_i)=6e^{2\lambda}\rho I. \tag{1}
\]

### 1. 面积方程：系数确为 \(6\)

对 (1) 取迹：
\[
\operatorname{tr}A_i=2\sigma_i,\qquad
\partial_i(\rho\sigma_i)=\Delta\rho,
\]
故
\[
\boxed{\Delta\rho=6e^{2\lambda}\rho},
\]
即
\[
\boxed{\Delta\sigma+|\nabla\sigma|^2=6e^{2\lambda}}.
\]
所以系数是 **\(6\)，不是 \(3\)**。一般地，若
\(\operatorname{Ric}=\Lambda g\)，右端系数为 \(-2\Lambda\)。

---

### 2. 轨道方程确为加权 \(H^2\) 调和映射方程

取 (1) 的无迹部分：
\[
\boxed{\partial_i\bigl(\rho M^{-1}\partial_iM\bigr)=0}. \tag{2}
\]
二维共形规范下，基底共形因子在散度中消去，因此这是泛函
\[
\frac12\int \rho\,|dM|_{H^2}^2\,dr\,dz
\]
的 Euler–Lagrange 方程，其中
\[
H^2=SL(2,\mathbb R)/SO(2),\qquad
\langle V,W\rangle_M
=\frac12\operatorname{tr}(M^{-1}VM^{-1}W).
\]

在极坐标
\[
ds_{H^2}^2=dd^2+\sinh^2d\,d\psi^2
\]
中，方程正是
\[
\boxed{
\partial_r(\rho d_r)+\partial_z(\rho d_z)
=\rho\sinh d\cosh d\,(\psi_r^2+\psi_z^2)
}, \tag{3}
\]
以及
\[
\boxed{
\partial_r(\rho\sinh^2d\,\psi_r)
+\partial_z(\rho\sinh^2d\,\psi_z)=0.
} \tag{4}
\]
故所给角动量流
\[
J_i=\rho\sinh^2d\,\psi_i
\]
确实满足 \(\operatorname{div}J=0\)。

但源笔记中的 Iwasawa 方程 (4.6) 有一个符号错误。若
\[
ds_{H^2}^2=d\alpha^2+e^{-2\alpha}d\beta^2,
\]
正确方程是
\[
\boxed{
\operatorname{div}(\rho\nabla\alpha)
=-\rho e^{-2\alpha}|\nabla\beta|^2,
}
\]
\[
\boxed{
\operatorname{div}(\rho e^{-2\alpha}\nabla\beta)=0.
}
\]
因此 (4.6) 右端必须由正号改成负号。对角情形 \(\beta=0\) 不受影响。

---

### 3. 基底共形因子方程正确

定义
\[
q_{ij}
=\frac12\operatorname{tr}(B_iB_j),\qquad
e_{H^2}=q_{rr}+q_{zz}.
\]
基底 Ricci 分量为
\[
\operatorname{Ric}_{ij}
=-\Delta\lambda\,\delta_{ij}
-\nabla_i^h\nabla_j^h\sigma
-\frac12\sigma_i\sigma_j-\frac12q_{ij}.
\]
取平坦迹并代入面积方程，得到
\[
\boxed{
\Delta\lambda
=\frac{|\nabla\sigma|^2-e_{H^2}}4.
}
\]
这里
\[
e_{H^2}
=|\nabla d|^2+\sinh^2d\,|\nabla\psi|^2
=|\nabla\alpha|^2+e^{-2\alpha}|\nabla\beta|^2.
\]

交叉约束也正确：
\[
\boxed{
\sigma_{rz}
=\lambda_z\sigma_r+\lambda_r\sigma_z
-\frac12\sigma_r\sigma_z-\frac12q_{rz}.
}
\]
源笔记中的 \(e_{H^2,rz}\) 应理解为 \(q_{rz}\)，而不是能量密度的偏导数。

---

### 4. 反射对称核心上的 twist 消失

对 Killing 场 \(X\)，令
\[
\omega_X=*(X^\flat\wedge dX^\flat).
\]
Killing 恒等式给出
\[
d\omega_X
=2*(X^\flat\wedge\operatorname{Ric}(X)^\flat)=0,
\]
因为 \(\operatorname{Ric}(X)^\flat=-3X^\flat\)。

若 \(X,Y\) 交换，则
\[
c_X=\iota_Y\omega_X
=*(X^\flat\wedge Y^\flat\wedge dX^\flat)
\]
满足
\[
dc_X=\mathcal L_Y\omega_X-\iota_Yd\omega_X=0.
\]
同理 \(dc_Y=0\)。

若反射等距映射保持两个 \(T^2\) 生成元并反转四维定向，则它反转 Hodge 星号，故在固定超曲面上
\[
c_X=-c_X,\qquad c_Y=-c_Y.
\]
于是 \(c_X=c_Y=0\)，再由常值性扩展至整个连通核心。在 Killing 场线性无关处，这正给出正交传递性。

因此第 4 项正确，但需明确反射必须保持相应 \(T^2\) 作用。轨道矩阵的非对角项不是 twist。

---

### 5. VII\(_0\) 特化及频率约定

对抽象极坐标 ansatz
\[
d=d(r),\qquad \psi=kz,\qquad \sigma=\sigma(r),
\]
(3) 化为
\[
\boxed{
(e^\sigma d')'
=e^\sigma k^2\sinh d\cosh d.
} \tag{5}
\]
若 \(k\neq0\)、\(d>0\)，右端严格为正。由反射初值 \(d'(0)=0\) 可得
\[
e^\sigma d'>0,\qquad d'>0
\]
于正向区间成立。这确实是 VII\(_0\) 的单向势垒机制。

不过和 Step 78 的旋转共架参数比较时有一个二倍角约定。若
\[
M=R(kz)
\begin{pmatrix}e^d&0\\0&e^{-d}\end{pmatrix}
R(kz)^T,
\]
则标准 \(H^2\) 极角是
\[
\psi=2kz.
\]
因此若 \(k\) 沿用 Step 78 的共架频率，(5) 的右端应为
\[
4e^\sigma k^2\sinh d\cosh d.
\]
这只影响频率归一化，不影响正性或势垒结论。

---

### 6. Step 73 的恢复正确，但必须显式换成共形坐标

Step 73 基底
\[
dr^2+e^{2r}dz^2
\]
在 \((r,z)\) 中不是共形规范。令
\[
t=-e^{-r},
\]
则
\[
dr^2+e^{2r}dz^2=e^{2r}(dt^2+dz^2).
\]
取
\[
\rho=N^{-2}e^{2r}=N^{-2}t^{-2},\qquad
M=\operatorname{diag}(e^v,e^{-v}),
\]
轨道方程为
\[
\partial_t(\rho v_t)+\partial_z(\rho v_z)=0.
\]
利用 \(\partial_t=e^r\partial_r\)，得到
\[
\boxed{
v_{rr}+3v_r+e^{-2r}v_{zz}=0.
}
\]
因此 Step 73 恢复成立。若错误地直接在非共形的 \((r,z)\) 坐标代入平坦散度式，会得到错误的
\(v_{rr}+2v_r+v_{zz}=0\)。

---

## 一般二维映射是否通过增长权重“吸收角动量”？

需要修正源笔记中的强说法。

方程
\[
\partial_rJ_r+\partial_zJ_z=0
\]
只推出周期圆上的径向流守恒：
\[
\frac d{dr}\int_{S^1}J_r\,dz=0.
\]
反射条件 \(M_r(0,z)=0\) 给出该径向流为零。它**不**推出
\(\psi_z\) 随 \(\rho=e^\sigma\) 增长而衰减，也不控制
\(\int J_z\,dz\)。

事实上 helicoidal 解本身满足
\[
J_r=0,\qquad
J_z=\rho\sinh^2d\,k,
\]
无论 \(J_z\) 如何随 \(r\) 变化，仍有
\(\partial_rJ_r+\partial_zJ_z=0\)。源笔记 §6.2 中关于
\(\frac d{dr}\int J_z\,dz\) 的公式并非由守恒律推出，应删除。

因此严格结论只是：

* 一般二维 \(H^2\) 映射不受 \(\psi_z=k\) 的冻结约束，因而 Step 78 的点态 invariant-region 证明不再适用；
* 它们在原则上可以重新分配角向能量并使 \(|\nabla\psi|\) 变小；
* 但“增长的 \(e^\sigma\) 必然吸收角动量并使 \(\psi_z\to0\)”没有得到证明。

---

## 耦合系统中确有额外约束

### 1. 完整矩阵 Noether 流

(2) 给出
\[
\mathcal Q(r)
=\int_{S^1}\rho M^{-1}M_r\,dz,
\qquad
\mathcal Q'(r)=0.
\]
反射数据 \(M_r(0,z)=0\) 因而推出
\[
\boxed{\mathcal Q(r)\equiv0.}
\]
角流只是这一 \(SL(2,\mathbb R)\) 矩阵守恒律的一个分量。

### 2. 凸距离最大值原理

固定 \(P\in H^2\)，令
\[
F(U)=\frac12d_{H^2}(U,P)^2.
\]
由于 \(H^2\) 曲率为 \(-1\)，
\[
\operatorname{Hess}F\ge g_{H^2}.
\]
对加权调和映射 \(U\) 有
\[
\boxed{
\operatorname{div}(\rho\nabla(F\circ U))
\ge \rho|dU|^2.
} \tag{6}
\]
在有限周期柱面上，若内边界为反射 Neumann 条件 \(U_r=0\)，则
\[
\sup_{\text{柱面}}F
\le \sup_{\text{外边界}}F.
\]
特别地，若外边界轨道映射恰为常值 \(P\)，则
\[
\boxed{U\equiv P.}
\]
故一个**精确 Einstein、精确反射**的有限核心，不能把中心处阶一的轨道位移松弛到外边界的精确常值映射。这是对所提机制的实质性限制。

### 3. 加权应力平衡

令
\[
T_{ij}=q_{ij}-\frac12\delta_{ij}e_{H^2}.
\]
则
\[
\boxed{
\partial_i(\rho T_{ij})
=-\frac12e_{H^2}\,\partial_j\rho.
} \tag{7}
\]
若还能证明 \(\rho_r\ge0\) 点态，则
\[
\frac d{dr}\int_{S^1}\rho T_{rr}\,dz
=-\frac12\int_{S^1}\rho_r e_{H^2}\,dz\le0.
\]
但面积方程目前只给出平均通量增长：
\[
\boxed{
\frac d{dr}\int_{S^1}\rho_r\,dz
=6\int_{S^1}e^{2\lambda}\rho\,dz>0,
} \tag{8}
\]
并不保证 \(\rho_r\ge0\) 点态。因此 (7) 尚未形成无条件单调量。

---

## 对近似 Einstein 连接器的最终判断

若
\[
E=\operatorname{Ric}+3g,
\]
轨道方程变成
\[
\boxed{
\partial_i(\rho B_i)
=-2e^{2\lambda}\rho\,E_{\rm orbit}^{\circ}.
} \tag{9}
\]
即使 \(\|E\|_\infty\to0\)，长扩张连接器上的权重
\(e^{2\lambda}\rho\) 仍可能使总强迫量保持阶一。因此精确系统的最大值原理不能仅凭点态小缺陷直接推广。

综上：

1. 面积系数 \(6\)、加权调和映射结构、极坐标守恒律、共形因子方程、twist 消失及 Step 73 方程均得到核验。
2. Iwasawa \(\alpha\) 方程必须改为负号；Step 73 必须注明共形坐标变换；VII\(_0\) 与极角频率相差因子 \(2\)。
3. 一般二维映射确实逃离固定 helicoid 的 ODE 势垒，但“增长权重吸收角动量”目前仅是可能机制，不是守恒律的推论。
4. 精确反射问题受到矩阵流守恒、凸距离最大值原理、面积通量和应力平衡的额外约束。特别是精确常值外边界迫使整个轨道映射常值。
5. 尚未解决的精确对象是：是否存在一列长的近似 Einstein 连接器，使 (9) 的加权强迫累积为阶一，同时 \(\|E\|_\infty\to0\) 并满足全部基底约束与出口条件。决定这一点需要控制加权源，而非仅控制点态 Ricci 缺陷。
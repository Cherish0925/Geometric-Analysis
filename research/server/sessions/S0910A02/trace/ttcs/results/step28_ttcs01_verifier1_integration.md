# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 28,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step28_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step28_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Bochner center bound theorem package for the positive-collapse route of Yau Problem 26. The key claims to check:

1. THEOREM A (Bochner center bound): For Z Killing on closed (M,g) with Ric ≤ (Λ+δ)g, the standard Bochner identity ∫|∇Z|² = ∫Ric(Z,Z) combined with the fiber gradient lower bound |∇Z|² ≥ (b²/2)|Z|² (for Heisenberg center bracket b) gives ⟨b²⟩ ≤ 2(Λ+δ). Check that the fiber gradient lower bound is correct for a general submersion with possibly nonzero T and A tensors (not just the totally geodesic case). The claim is that T and A terms add non-negatively to |∇Z|².

2. THEOREM B: For Λ+δ < 0 on a closed manifold, the Bochner identity implies Z=0. Check sign conventions.

3. ALMOST-KILLING CORRECTION: The exact Weitzenböck formula gives ∫|∇Z|² = ∫Ric(Z,Z) + (1/2)∫|σ|² - (1/4)∫(tr σ)² where σ = L_Z g. Check that the 2-form norm convention (|dω|² = 2|A|² vs 4|A|²) is consistent with the derivation. Also check the collapse-scale analysis: for fiber scale ε, average |Z|² ~ ε², and τ = ||L_Z g||, the correction is τ²Vol/∫|Z|². When does this give abelian forcing?

4. INDUCTION ARCHITECTURE: Bound center bracket, quotient by central circle, apply Kaluza-Klein relation to get two-sided Ricci control on quotient, repeat. Check whether the constant degradation is O(2^k Λ) and whether the central quotient preserves the manifold structure needed for the next Bochner step.

5. The H3 model verification: |∇Z|² = c²(2k₃² + b²/2) where Z=c·e₃, verified by explicit Koszul formula. The Bochner identity integrand c²(3k₃² + 2k₁k₃ + k₃') vanishes after IBP. Check this.

Be precise about sign/convention issues, especially in the Weitzenböck formula. Flag any gaps in the induction architecture.

## Integrated Scientific Memo

# Bochner 中心括号包核验结论

记
\[
K:=\Lambda+\delta.
\]

## 1. Theorem A：Bochner 恒等式正确，但原文算子符号有误

若采用非负粗 Laplace 算子
\[
\nabla^*\nabla=-\operatorname{tr}\nabla^2,
\]
则 Killing 场满足
\[
\nabla^*\nabla Z=\operatorname{Ric}^{\sharp}(Z),
\]
而不是原文写的
\[
\nabla^*\nabla Z+\operatorname{Ric}^{\sharp}(Z)=0.
\]
后一个公式只有在采用迹型算子 \(\nabla^i\nabla_i\) 时才应写成
\[
\nabla^i\nabla_i Z+\operatorname{Ric}^{\sharp}(Z)=0.
\]

不过积分结论完全正确：
\[
\int_M|\nabla Z|^2\,dV
=\int_M\operatorname{Ric}(Z,Z)\,dV
\le K\int_M|Z|^2\,dV.
\]

### 一般子沉浸中 \(T,A\) 是否可能抵消？

不能。设 \(\pi:M\to B\) 是 Riemannian 子沉浸，\(\{U_a\}\) 和 \(\{X_i\}\) 分别为垂直、水平正交标架，\(Z\) 为垂直场。则
\[
\nabla_{U_a}Z=\widehat\nabla_{U_a}Z+T_{U_a}Z,
\]
其中两项分别垂直、水平，因而正交；同样
\[
\nabla_{X_i}Z=\mathcal V\nabla_{X_i}Z+A_{X_i}Z
\]
也是正交分解。因此
\[
\begin{aligned}
|\nabla Z|^2
={}&\sum_a\Bigl(
|\widehat\nabla_{U_a}Z|^2+|T_{U_a}Z|^2
\Bigr)\\
&+\sum_i\Bigl(
|\mathcal V\nabla_{X_i}Z|^2+|A_{X_i}Z|^2
\Bigr)
\ge |\widehat\nabla Z|^2.
\end{aligned}
\]
所以原文“\(T,A\) 只增加非负平方项”的核心判断正确。

若纤维上有正交标架
\[
[e_1,e_2]=bz,\qquad z=Z/|Z|,
\]
并且中心场长度沿纤维恒定，则纤维 Koszul 公式给出
\[
\widehat\nabla_{e_1}Z=-\frac b2|Z|e_2,\qquad
\widehat\nabla_{e_2}Z=\frac b2|Z|e_1,\qquad
\widehat\nabla_zZ=0.
\]
故
\[
|\widehat\nabla Z|^2=\frac{b^2}{2}|Z|^2,
\]
从而
\[
\boxed{\;
\frac{\int_Mb^2|Z|^2\,dV}{\int_M|Z|^2\,dV}
\le 2K.
\;}
\]

更一般地，对中心单位向量 \(z\)，令
\[
\langle J_zX,Y\rangle=\langle z,[X,Y]\rangle.
\]
则
\[
|\widehat\nabla Z|^2
=\frac{|Z|^2}{4}\|J_z\|_{\mathrm{HS}}^2.
\]
这是高维中心括号的正确推广。

### 必须修正的全局假设

“闭流形上存在非交换连通幂零群的自由等距作用”这一表述实际上没有非交换实例：

- 闭流形的等距群是紧 Lie 群；
- 紧 Lie 代数中的幂零子代数必为交换：每个 \(\operatorname{ad}_X\) 同时斜对称且幂零，因此为零。

所以 Corollary A1 应改写为：

1. \(M\) 具有相应的 Heisenberg/幂零纤维结构；
2. 纤维度量逐纤维具有所用的左不变结构；
3. 某个中心方向单独产生全局 Killing 场。

紧 Heisenberg 幂零流形的典型情形正是整个 \(H_3\) 并非全局等距群，而中心圆可以是全局 Killing 流。

此外，该结论只是 \(|Z|^2\)-加权 \(L^2\) 控制，不是 \(b\) 的逐点上界；它允许大括号集中在小测度或 \(|Z|\) 很小的区域。

---

## 2. Theorem B：符号和结论正确

若 \(K<0\)，则对 Killing 场
\[
0\le\int|\nabla Z|^2
=\int\operatorname{Ric}(Z,Z)
\le K\int|Z|^2.
\]
若 \(Z\not\equiv0\)，最右端严格为负，矛盾。因此
\[
\boxed{Z\equiv0.}
\]

这要求的是严格负的 Ricci **上界** \(\operatorname{Ric}\le Kg\)，而不是通常 Bochner 调和一形式定理中的正 Ricci 下界。CH\(^2\) horosphere 数据位于非紧空间，其分部积分有无穷远通量，因此不构成反例。

---

## 3. Almost-Killing 修正：系数正确，但只能作为积分恒等式使用

令
\[
\omega=Z^\flat,\qquad
\sigma=\mathcal L_Zg,\qquad
\nabla Z=A+S,
\]
其中
\[
A=\frac{\nabla Z-(\nabla Z)^T}{2},\qquad S=\frac{\sigma}{2}.
\]
采用张量 Frobenius 范数以及标准二形式范数
\[
|\alpha|^2=\frac12\sum_{ij}\alpha_{ij}^2,
\]
有
\[
|\nabla Z|^2=|A|^2+\frac14|\sigma|^2.
\]
又因
\[
(d\omega)_{ij}=2A_{ij},
\]
故
\[
|d\omega|^2
=\frac12\sum_{ij}(2A_{ij})^2
=2|A|^2,
\]
而不是 \(4|A|^2\)。同时
\[
\delta\omega=-\operatorname{div}Z
=-\frac12\operatorname{tr}\sigma.
\]
积分 Weitzenböck 公式遂给出
\[
\boxed{
\int_M|\nabla Z|^2
=
\int_M\operatorname{Ric}(Z,Z)
+\frac12\int_M|\sigma|^2
-\frac14\int_M(\operatorname{tr}\sigma)^2.
}
\]

因此
\[
\int|\nabla Z|^2
\le K\int|Z|^2+\frac12\int|\sigma|^2
\]
以及
\[
\boxed{
\langle b^2\rangle_{|Z|^2}
\le
2K+\frac{\int|\mathcal L_Zg|^2}{\int|Z|^2}.
}
\]
若 \(\|\mathcal L_Zg\|_\infty\le\tau\)，则最后一项至多为
\[
\frac{\tau^2\operatorname{Vol}(M)}{\int|Z|^2}.
\]

原材料中“解出 \(|A|^2\)”的无积分表达不能理解成逐点恒等式；点态 Weitzenböck 公式还含散度项。正确命题是上述积分恒等式。另需修正 JSON 中“误差 \(O(\tau)\)”的说法：在这里误差是二次量 \(O(\tau^2)\)。

### 坍缩尺度阈值

若
\[
\frac1{\operatorname{Vol}(M)}\int|Z|^2\asymp\varepsilon^2,
\]
则修正项规模为
\[
O\!\left(\frac{\tau^2}{\varepsilon^2}\right).
\]

应区分三个结论：

- 若 \(\tau=O(\varepsilon)\)，则环境尺度括号的加权平均仍为 \(O(1)\)；
- 若 \(\tau=o(\varepsilon)\)，则修正项本身趋于零，恢复精确 Killing 情形的渐近常数；
- 对第一坍缩尺度归一化括号 \(\varepsilon b\)，
  \[
  \langle(\varepsilon b)^2\rangle_{|Z|^2}
  \le 2K\varepsilon^2+
  \varepsilon^2\frac{\int|\sigma|^2}{\int|Z|^2}.
  \]
  在上述长度可比假设下，仅需 \(\tau\to0\) 即可得到加权 \(L^2\) 意义的
  \(\varepsilon b\to0\)；若只要求修正比值有界，则 \(\tau=O(\varepsilon)\) 已足够。

因此原文要求 \(\tau=o(\varepsilon)\) 对“归一化括号消失”过强；它只在要求修正比值趋零时必要。若中心方向实际处于更小的分级尺度，应保留不变量
\[
R_Z:=\frac{\int|\mathcal L_Zg|^2}{\int|Z|^2}
\]
并检验相应归一化尺度的 \(\varepsilon^2R_Z\to0\)，不能机械使用
\(\int|Z|^2\asymp\varepsilon^2\operatorname{Vol}\)。

---

## 4. 中心商归纳：目前不是已证定理

在非常特殊的“自由、常长度、光滑圆商塔”中，若
\[
c\,g_M\le\operatorname{Ric}_M\le C\,g_M,
\]
且按所用约定
\[
\operatorname{Ric}_M(U,U)=\frac12|\phi|^2,\qquad
\operatorname{Ric}_B(X,X)
=\operatorname{Ric}_M(X,X)+\frac12|i_X\phi|^2,
\]
则
\[
|\phi|^2\le2C,\qquad
c\,g_B\le\operatorname{Ric}_B\le2C\,g_B.
\]
在这一强化情形，经过 \(r\) 次圆商可有
\[
C_r\le2^rC.
\]

但原文的普遍 \(O(2^k\Lambda)\) 归纳存在以下缺口：

1. **变长度问题。** 一般中心 Killing 场长度不是常数。商公式出现
   \[
   f^{-1}\operatorname{Hess}f,\qquad f^{-1}\Delta f
   \]
   等项，Bochner 加权积分估计不控制这些逐点项。

2. **纤维括号与水平曲率不同。** Theorem A 控制的是纤维内在中心括号；商空间 Ricci 的上界还需控制连接曲率 \(\phi\) 或 \(A\)。在一般 pinched、非 Einstein 情形，不能直接援引
   \(|\phi|^2=2\Lambda\)。该等式属于额外的精确 Einstein/常长度方程。

3. **平均控制不足。** \(\langle b^2\rangle_{|Z|^2}\) 的积分上界不能直接给出下一层所需的逐点 Ricci 上界。

4. **圆商次数不等于 nilpotency step。** 二步群可能有多维交换子中心，需要多个圆商。因此指数应由实际圆商塔长度 \(r\) 控制，而非仅由幂零步数 \(k\) 控制。

5. **商未必是光滑流形。** 中心流需要闭轨道且作用自由、proper。零点、有限稳定子或稠密轨道会分别导致分层空间、orbifold 或非良性商。

6. **全局中心圆未必存在。** 幂零流形束的单值变换可能作用于中心晶格；即使第一层中心场全局 Killing，商后的下一层中心场也未必是全局 Killing。

因此目前可核准的说法是：

> \(O(2^rC)\) 只在具有逐层自由、常长度、光滑、并保留所需 Killing 结构的圆商塔中成立；它没有由 Theorem A 推出为一般 N-structure 或一般 Ricci-pinched 坍缩定理。

---

## 5. \(H_3\) 模型：Koszul 和分部积分均正确

对
\[
g=dt^2+a^2(\theta_1^2+\theta_2^2)+c^2\theta_3^2,
\qquad
b=\frac c{a^2},\qquad
k_3=\frac{c'}c,\qquad
Z=ce_3,
\]
连接公式给出
\[
\begin{aligned}
\nabla_{e_0}Z&=ck_3e_3,\\
\nabla_{e_1}Z&=-\frac{cb}{2}e_2,\\
\nabla_{e_2}Z&=\frac{cb}{2}e_1,\\
\nabla_{e_3}Z&=-ck_3e_0.
\end{aligned}
\]
故
\[
\boxed{
|\nabla Z|^2
=c^2\left(2k_3^2+\frac{b^2}{2}\right).
}
\]

由
\[
\operatorname{Ric}_{33}
=\frac{b^2}{2}-k_3'-(2k_1+k_3)k_3
\]
得到
\[
|\nabla Z|^2-\operatorname{Ric}(Z,Z)
=c^2(3k_3^2+2k_1k_3+k_3').
\]

体积权为 \(w=a^2c\)，故完整积分权为
\[
W=c^2w=a^2c^3,\qquad
\frac{W'}W=2k_1+3k_3.
\]
于是精确地
\[
\int W(3k_3^2+2k_1k_3+k_3')\,dt
=[Wk_3]_{\partial}.
\]
周期情形中端点项相消；标准光滑中心圆闭合时
\[
Wk_3=a^2c^2c'\longrightarrow0.
\]
因此 Bochner 积分核验成立。原文把分部积分后结果直接写成零时，应显式注明这一端点通量条件；对其他奇异闭合必须单独验证。

## 最终判定

可以保留并使用：

- Killing 场的全局 Bochner 上界；
- 一般 Riemannian 子沉浸中 \(T,A\) 不会破坏纤维梯度下界；
- Heisenberg 中心括号的 \(|Z|^2\)-加权 \(L^2\) 控制；
- 严格负 Ricci 上界下 Killing 场消失；
- exact almost-Killing 积分修正公式；
- \(H_3\) 模型计算。

不能作为已证结果使用：

- 非交换连通幂零群在闭流形上的自由全局等距作用这一原始设定；
- 由平均中心括号界推出逐点或一致的“abelian forcing”；
- 对一般 pinched 坍缩迭代中心商并得到 \(O(2^k\Lambda)\)；
- 未建立的 N-structure almost-Killing 桥及商后 Killing 结构。

真正剩余的负载点是：在实际局部 N-structure 中建立尺度正确的
\[
\frac{\int|\mathcal L_Zg|^2}{\int|Z|^2}
\]
控制，并同时获得逐层商所需的连接曲率、长度 Hessian、自由闭轨道及商后对称性控制。
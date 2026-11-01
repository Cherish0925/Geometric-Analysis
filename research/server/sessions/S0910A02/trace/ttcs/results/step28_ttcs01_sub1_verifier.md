# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step28_bochner_center_bound_and_abelian_forcing.md",
    "Sessions/S0910A02/workspace/data/step28_bochner_killing_center_bound.json",
    "Sessions/S0910A02/workspace/data/step28_almost_killing_correction.json",
    "Sessions/S0910A02/workspace/notes/step27_preceptor_h3_positive_monotonicity_review.md",
    "Sessions/S0910A02/workspace/notes/step26_nilpotent_abelian_forcing_audit.md"
  ]
}
```

## Task

Verify the Bochner center bound theorem package for the positive-collapse route of Yau Problem 26. The key claims to check:

1. THEOREM A (Bochner center bound): For Z Killing on closed (M,g) with Ric ≤ (Λ+δ)g, the standard Bochner identity ∫|∇Z|² = ∫Ric(Z,Z) combined with the fiber gradient lower bound |∇Z|² ≥ (b²/2)|Z|² (for Heisenberg center bracket b) gives ⟨b²⟩ ≤ 2(Λ+δ). Check that the fiber gradient lower bound is correct for a general submersion with possibly nonzero T and A tensors (not just the totally geodesic case). The claim is that T and A terms add non-negatively to |∇Z|².

2. THEOREM B: For Λ+δ < 0 on a closed manifold, the Bochner identity implies Z=0. Check sign conventions.

3. ALMOST-KILLING CORRECTION: The exact Weitzenböck formula gives ∫|∇Z|² = ∫Ric(Z,Z) + (1/2)∫|σ|² - (1/4)∫(tr σ)² where σ = L_Z g. Check that the 2-form norm convention (|dω|² = 2|A|² vs 4|A|²) is consistent with the derivation. Also check the collapse-scale analysis: for fiber scale ε, average |Z|² ~ ε², and τ = ||L_Z g||, the correction is τ²Vol/∫|Z|². When does this give abelian forcing?

4. INDUCTION ARCHITECTURE: Bound center bracket, quotient by central circle, apply Kaluza-Klein relation to get two-sided Ricci control on quotient, repeat. Check whether the constant degradation is O(2^k Λ) and whether the central quotient preserves the manifold structure needed for the next Bochner step.

5. The H3 model verification: |∇Z|² = c²(2k₃² + b²/2) where Z=c·e₃, verified by explicit Koszul formula. The Bochner identity integrand c²(3k₃² + 2k₁k₃ + k₃') vanishes after IBP. Check this.

Be precise about sign/convention issues, especially in the Weitzenböck formula. Flag any gaps in the induction architecture.

## Output

# 科学核验备忘录

## 总结

- Theorem A 的全局 Bochner 恒等式成立，但文中的粗 Laplace 算子符号需要改写。
- Heisenberg 中心方向的纤维梯度估计成立；非零 \(T,A\) 不会产生抵消。不过它需要真实的 Riemannian 子沉浸、纤维左不变结构和全局中心 Killing 场。
- “闭流形上由连通非交换幂零群自由等距作用”这一假设组合实际上为空：闭流形的等距群是紧 Lie 群，而紧 Lie 代数中的幂零子代数必为交换。因此 Corollary A1 必须改成“中心圆作用等距，较大的幂零结构仅为纤维结构”，H\(_3\) 模型正属于这种情形。
- Theorem B 的符号和结论正确。
- almost-Killing 公式在标准微分形式范数下完全正确，但它是积分恒等式，不是逐点恒等式。对于归一化括号 \(\varepsilon b\to0\)，所需条件弱于文中写出的 \(\|\mathcal L_Zg\|=o(|Z|)\)。
- 中心商归纳目前尚未形成一般定理。\(O(2^k\Lambda)\) 只在一串自由、常长度、光滑圆商等额外条件下可推出，而且指数应由圆商次数控制，不一定等于幂零步数。
- H\(_3\) 模型的 Koszul 计算和分部积分均正确；坐标证明须保留端点通量 \([a^2c^3k_3]\)。

---

## 1. Bochner 恒等式与纤维梯度估计

### 1.1 Laplace 算子符号

若采用通常的非负连接 Laplace 算子
\[
\nabla^*\nabla=-\operatorname{tr}\nabla^2,
\]
则 Killing 场满足
\[
\nabla^*\nabla Z=\operatorname{Ric}^{\sharp}(Z).
\]
等价地，采用迹型、非正的算子 \(\nabla^i\nabla_i\) 时，
\[
\nabla^i\nabla_i Z+\operatorname{Ric}^{\sharp}(Z)=0.
\]
因此文件中的
\[
\nabla^*\nabla Z+\operatorname{Ric}(Z)=0
\]
与通常的 \(\nabla^*\nabla\) 记号不相容，但随后使用的积分式是正确的：
\[
\int_M|\nabla Z|^2\,dV
=\int_M\operatorname{Ric}(Z,Z)\,dV.
\]
于是若 \(\operatorname{Ric}\le K g\)，
\[
\int_M|\nabla Z|^2\le K\int_M|Z|^2,
\qquad K=\Lambda+\delta.
\]

### 1.2 非全测地纤维不会破坏下界

设 \(\pi:M\to B\) 是 Riemannian 子沉浸，\(\{U_a\}\) 为垂直正交标架，\(\{X_i\}\) 为水平正交标架。对垂直场 \(Z\)，Gauss–O’Neill 分解给出
\[
\begin{aligned}
|\nabla Z|^2
={}&\sum_a\left(
|\widehat\nabla_{U_a}Z|^2+|T_{U_a}Z|^2\right)\\
&+\sum_i\left(
|\mathcal V\nabla_{X_i}Z|^2+|A_{X_i}Z|^2\right).
\end{aligned}
\]
这里 \(\widehat\nabla\) 是纤维的内蕴 Levi–Civita 连接。所有项均为平方，因此
\[
|\nabla Z|^2\ge |\widehat\nabla Z|^2.
\]
所以非零 \(T\)、非零 \(A\) 的确不会抵消纤维内蕴项。文中的核心不等式在这一点上成立。

### 1.3 Heisenberg 中心计算

在每条纤维上令 \(z=Z/|Z|\)，并以正交标架满足
\[
[e_1,e_2]=b z.
\]
中心性及纤维齐性保证 \(|Z|\) 沿纤维不变。Koszul 公式给出
\[
\widehat\nabla_{e_1}Z=-\frac{b}{2}|Z|e_2,\qquad
\widehat\nabla_{e_2}Z=\frac{b}{2}|Z|e_1,\qquad
\widehat\nabla_zZ=0.
\]
故
\[
|\widehat\nabla Z|^2=\frac{b^2}{2}|Z|^2.
\]
结合上一分解，
\[
|\nabla Z|^2\ge \frac{b^2}{2}|Z|^2.
\]
积分后得到
\[
\frac{\int_M b^2|Z|^2}{\int_M|Z|^2}
\le 2K.
\]

更一般地，对中心单位向量 \(z\)，定义
\[
\langle J_zX,Y\rangle=\langle z,[X,Y]\rangle.
\]
则
\[
\widehat\nabla_XZ=-\frac{|Z|}{2}J_zX,\qquad
|\widehat\nabla Z|^2=\frac{|Z|^2}{4}\|J_z\|_{\mathrm{HS}}^2.
\]
H\(_3\) 情形中 \(\|J_z\|_{\mathrm{HS}}^2=2b^2\)。这也是推广到高维中心括号时更自然的表达。

需要注意，不能直接用归一化场 \(Z/|Z|\) 代替 \(Z\) 进入 Bochner 恒等式；若 \(|Z|\) 横向变化，归一化场通常不再是 Killing 场。

### 1.4 全群等距作用的结构问题

Corollary A1 写成“闭 \(M\) 上存在步数至少二的连通幂零群自由等距作用”时没有非交换实例。理由是：

1. \(\operatorname{Isom}(M,g)\) 对闭 \(M\) 是紧 Lie 群；
2. 自由作用必为有效作用，因而诱导 Lie 代数单射；
3. 紧 Lie 代数带有 \(\operatorname{Ad}\)-不变内积；幂零子代数中每个 \(\operatorname{ad}_X\) 同时是斜对称算子和幂零算子，因此只能为零；
4. 所以该幂零子代数必须交换。

H\(_3\) 紧幂零流形上的左不变度量并不使整个 H\(_3\) 成为全局等距群；通常只有中心圆流是全局 Killing 流。因而非空版本应假设：

- 存在 Heisenberg 或幂零纤维结构；
- 纤维垂直度量逐纤维左不变；
- 某个中心方向产生全局 Killing 场。

在这些条件下，上述积分估计成立，但它仍是加权 \(L^2\) 估计，不能直接推出 \(b\) 的逐点上界。

---

## 2. 负 Ricci 上界与 Killing 场消失

令 \(K=\Lambda+\delta<0\)。若 \(Z\not\equiv0\)，则
\[
0\le\int_M|\nabla Z|^2
=\int_M\operatorname{Ric}(Z,Z)
\le K\int_M|Z|^2<0,
\]
矛盾。因此 \(Z\equiv0\)。

所以 Theorem B 正确。它说明具有严格负定 Ricci 上界的闭流形没有非零连续等距生成元。CH\(^2\) horosphere 数据处于非紧环境，Bochner 分部积分带有无穷远通量，因而不与此结论冲突。

---

## 3. Almost-Killing 修正项

令
\[
B_{ij}=\nabla_iZ_j,\qquad
A=\frac{B-B^T}{2},\qquad
S=\frac{B+B^T}{2}=\frac{\sigma}{2},
\quad \sigma=\mathcal L_Zg.
\]
采用张量范数 \(|A|^2=\sum_{ij}A_{ij}^2\) 以及标准二形式范数
\[
|\alpha|^2=\frac12\sum_{ij}\alpha_{ij}^2,
\]
有
\[
|\nabla Z|^2=|A|^2+\frac14|\sigma|^2.
\]
又因 \(d\omega_{ij}=2A_{ij}\)，
\[
|d\omega|^2
=\frac12\sum_{ij}(2A_{ij})^2
=2|A|^2,
\]
且
\[
|\delta\omega|^2=\frac14(\operatorname{tr}\sigma)^2.
\]
积分 Weitzenböck 公式
\[
\int(|d\omega|^2+|\delta\omega|^2)
=\int(|\nabla\omega|^2+\operatorname{Ric}(Z,Z))
\]
因此给出
\[
\boxed{
\int|\nabla Z|^2
=
\int\operatorname{Ric}(Z,Z)
+\frac12\int|\sigma|^2
-\frac14\int(\operatorname{tr}\sigma)^2 }.
\]
系数正确。若把二形式范数写成 \(\sum_{ij}\alpha_{ij}^2\)，中间会出现 \(4|A|^2\)，但那不是 Hodge 能量通常采用的范数。

此公式只能作为积分恒等式使用；文件中无积分号的“solved for \(A\)”表达不成立为逐点公式，因为点态 Weitzenböck 公式还含散度项。

由此得到
\[
\langle b^2\rangle_{|Z|^2}
\le
2K+\frac{\int|\sigma|^2}{\int|Z|^2}.
\]
若 \(\int|Z|^2\asymp\varepsilon^2\operatorname{Vol}(M)\) 且
\(\|\sigma\|_\infty\le\tau\)，则修正比值为
\[
O\!\left(\frac{\tau^2}{\varepsilon^2}\right).
\]

三个不同强度应当区分：

1. \(\tau=O(\varepsilon)\)：环境尺度下的加权括号仍为 \(O(1)\)。
2. \(\tau=o(\varepsilon)\)：修正比值趋于零，恢复精确 Killing 场的渐近常数。
3. 对归一化括号，
   \[
   \langle(\varepsilon b)^2\rangle
   \le 2K\varepsilon^2+
   \varepsilon^2\frac{\int|\sigma|^2}{\int|Z|^2}.
   \]
   在上述长度可比条件下，右端为 \(O(\varepsilon^2+\tau^2)\)。因此仅需
   \(\tau\to0\) 就足以得到加权 \(L^2\) 意义下的
   \(\varepsilon b\to0\)；并不需要 \(\tau=o(\varepsilon)\)。

若中心方向比第一坍缩尺度更短，例如分级 H\(_3\) 坍缩中 \(|Z|\sim\varepsilon^2\)，则 \(\int|Z|^2\sim\varepsilon^2\operatorname{Vol}\) 不再成立。此时应保留不变量
\[
R_Z=\frac{\int|\mathcal L_Zg|^2}{\int|Z|^2}
\]
并直接研究 \(\varepsilon^2R_Z\)。

另有一处文本不统一：`step28_bochner_killing_center_bound.json` 说误差为 \(O(\tau)\)，而精确公式和 `step28_almost_killing_correction.json` 给出的是二次量 \(O(\tau^2)\)。

---

## 4. 中心商归纳

在自由、常长度圆作用这一强化情形，倍增估计确实可计算。设 \(U\) 为单位垂直场，\(\phi\) 为按文件约定归一化的连接曲率，则
\[
\operatorname{Ric}_M(U,U)=\frac12|\phi|^2,
\]
\[
\operatorname{Ric}_B(X,X)
=
\operatorname{Ric}_M(X,X)
+\frac12|i_X\phi|^2.
\]
若
\[
c\,g_M\le\operatorname{Ric}_M\le C\,g_M,
\]
则
\[
|\phi|^2\le2C,\qquad
c\,g_B\le\operatorname{Ric}_B\le2C\,g_B.
\]
所以经过 \(r\) 个满足同样条件的圆商，可得
\[
C_r\le2^rC.
\]

但当前归纳叙述缺少以下数学材料：

- 一般中心 Killing 场的长度只是商空间上的函数。变长度 Kaluza–Klein 公式含
  \[
  f^{-1}\operatorname{Hess}f,\qquad f^{-1}\Delta f,
  \]
  而 Bochner 的加权积分估计不控制这些逐点项。
- 中心括号估计只有加权积分形式，不能提供下一层商度量所需的逐点 Ricci 上界。
- 一条中心圆商未必降低幂零步数。例如 \(H_3^m\) 的步数为二，但需要处理 \(m\) 个独立交换子中心方向，或一次商掉整个中心环面。因此指数由实际圆商次数控制，不由步数 \(k\) 单独控制。
- 中心流必须有闭轨道且作用自由、适当，商才是光滑流形。有零点、有限稳定子或稠密轨道时，所得对象分别可能是分层空间、orbifold 或非 Hausdorff 商。
- 在幂零流形束中，中心晶格方向可能被单值变换置换；一个全局原始中心圆未必自动存在。
- 即使第一层中心场是全局 Killing 场，商后的新中心方向也未必仍产生全局 Killing 场。

因此 \(O(2^k\Lambda)\) 目前只对“自由常长度圆塔”成立；它尚未由 Theorem A 推出，也尚未覆盖一般 N-structure。

---

## 5. H\(_3\) 模型

对
\[
g=dt^2+a^2(\theta_1^2+\theta_2^2)+c^2\theta_3^2,
\quad b=\frac c{a^2},\quad k_3=\frac{c'}c,
\quad Z=c\,e_3,
\]
给出的连接公式产生
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
|\nabla Z|^2
=c^2\left(2k_3^2+\frac{b^2}{2}\right),
\]
与数据文件一致。

又
\[
\operatorname{Ric}_{33}
=\frac{b^2}{2}-k_3'-(2k_1+k_3)k_3,
\]
从而
\[
|\nabla Z|^2-\operatorname{Ric}(Z,Z)
=c^2(3k_3^2+2k_1k_3+k_3').
\]
体积权为 \(w=a^2c\)，令
\[
W=c^2w=a^2c^3,\qquad
\frac{W'}W=2k_1+3k_3.
\]
于是
\[
\int W(3k_3^2+2k_1k_3+k_3')\,dt
=[Wk_3]_{\mathrm{endpoints}}.
\]
周期情形中该通量为零；标准光滑中心圆闭合中
\(Wk_3=a^2c^2c'\to0\)，也为零。因此模型 Bochner 核验正确。若采用其他奇异闭合方式，坐标计算仍需单独确认这一端点通量，尽管全局光滑闭流形上的 Bochner 恒等式本身已经保证总散度积分为零。

总体上，可靠的新结果是“全局中心 Killing 场给出中心括号的加权积分控制”，以及 H\(_3\) 模型中的精确实现。一般幂零坍缩的迭代商过程还需要自由闭中心轨道、长度控制、逐点 Kaluza–Klein 估计和商后 Killing 结构。
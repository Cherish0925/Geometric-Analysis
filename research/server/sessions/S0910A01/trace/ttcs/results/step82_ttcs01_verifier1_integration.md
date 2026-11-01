# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 82,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step82_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step82_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following existence claim for Einstein desingularization of (S²×S²)/⟨(r_π,r_π)⟩:

CLAIM: Within the A+J+L equivariant family (insertion direction ω₂ fixed by J, equal scales by A+L symmetry, diagonal chirality pattern), ALL finite-dimensional obstructions tracked by Ozuch's O(t^{5/2}) error estimate vanish:
- λ_k = 0 for k=1,2,3 at each node (in-kernel insertion, ζ ∈ ker R⁺)
- μ₁ = 0 at each node (rank-one determinant: det R|_{ζ⊥} = 0)
- μ₂ = μ₃ = 0 at each node (J-parity: J acts as diag(-1,+1,-1) on adapted basis)
- ν_l = 0 (product orbifold has O(g_o) = {0}, no orbifold deformation parameters)

The combined Ozuch equation t·λ + t²·μ = O(t^{5/2}) becomes 0 = O(t^{5/2}), trivially satisfied.

CONSEQUENCE CLAIM: Under these conditions, Biquard's IFT ([Biq13] Theorem 14.3) produces an actual Einstein metric on the smooth resolution #₃(S²×S²) for sufficiently small t > 0.

SPECIFIC QUESTIONS TO CHECK:
1. Is the obstruction vanishing complete, or are there additional finite-dimensional conditions beyond λ, μ, ν that Ozuch tracks?
2. Does Biquard's IFT actually handle the case when ALL obstructions vanish identically (not just when they can be solved by parameter adjustment)? Is the map F(φ,v,t) = 0 being identically satisfied a degenerate or non-degenerate situation for the IFT?
3. The operator P on the product orbifold has a negative mode g₁-g₂ with eigenvalue -Λ. On the approximate desingularization, this mode survives (modified by O(t²)). Does this prevent the IFT contraction from closing? The eigenvalue is bounded away from zero, so the inverse norm should be O(1).
4. The orbifold deformation space O(g_o): is it truly trivial for (S²×S²)/Z₂? The round product has no TT kernel for P, but are there non-TT modes in O(g_o)?
5. The integrability condition: Ozuch requires 'integrable Einstein deformations' of both the orbifold and the ALE space. For the EH metric, are all deformations integrable? For the product orbifold with O(g_o) = {0}, is integrability vacuously satisfied?
6. The topology: with diagonal chirality (2 nodes +, 2 nodes -), the resolution has χ = 8, τ = 0, giving #₃(S²×S²). Is this correct?
7. Is there precedent in the literature for Einstein metrics on #₃(S²×S²)? This would be a new result if correct.

## Integrated Scientific Memo

# 核验结论

**存在性后果不成立。** 当前材料只证明了 Ozuch 的 \(O(t^{5/2})\) 公式中显式可见的低阶系数被消去；它没有证明完整有限维约化映射恒等为零。仍有一个 \(J\)-偶的径向障碍方向，其首个未知项预计在 \(t^3\)（可能伴随 \(\log t\)）阶，因此正好被 \(O(t^{5/2})\) 余项掩盖。

准确结论是：

\[
\boxed{\text{已知必要障碍不排除该解消，但现有论证不能产生 Einstein 度量。}}
\]

---

## 一、实际消去的障碍

在每个节点，取适应基
\[
(\phi_{(1)},\phi_{(2)},\phi_{(3)})
=(\omega _2,\omega _1,\omega _3),
\qquad
R^\pm=\operatorname{diag}(\Lambda,0,0).
\]

则：

1. **一阶局部障碍**
   \[
   \lambda_k=0,\qquad k=1,2,3,
   \]
   因为 \(R^\pm\omega _2=0\)。

2. **二阶径向系数**
   \[
   \mu_1=0,
   \]
   因为 Ozuch Lemma 2.14 给出
   \[
   \mu_1=C\det\!\left(R^\pm|_{\omega_2^\perp}\right),
   \]
   而适应基下该 \(2\times2\) 块为
   \(\operatorname{diag}(\Lambda,0)\)。

3. **横向投影**
   \[
   \mu_2=\mu_3=0,
   \]
   且更强地，所有已构造阶数上的横向投影恒等为零。原因是
   \[
   J^*|_{\Lambda^\pm}=\operatorname{diag}(-1,+1,-1),
   \]
   插入方向 \(\omega_2\) 为偶，而 \(\omega_1,\omega_3\) 为奇。若图、截断、DeTurck 参考度量和补空间修正均取 \(J\)-等变，则完整残差为 \(J\)-偶，与奇余核张量的配对为零。

4. **全局投影 \(\nu_l\)** 在 \(A\)-不变族中为零，但理由不是
   \(\mathbf O(g_o)=0\)，而是 \(A\)-奇偶性。

因此
\[
t\lambda+t^2\mu=O(t^{5/2})
\]
确实退化为
\[
0=O(t^{5/2}),
\]
但这只是一个无信息的低精度必要关系。

---

## 二、关键错误：完整径向映射并未消失

Ozuch Proposition 2.19 的逻辑方向是

\[
\text{存在精确 Einstein 度量}
\Longrightarrow
\begin{cases}
t_j\lambda_k^j+t_j^2\mu_k^j=O(t_{\max}^{5/2}),\\
\nu_l=O(t_{\max}^{5/2}).
\end{cases}
\]

它不是充分性定理。反过来从低阶系数消失推出存在性，是无效的。

在 \(A+J\) 对称后，四个节点的四个径向方程由 \(A\) 降为两个。单因子反足对称 \(L\) 给出
\[
F_2(t_1,t_2)=F_1(t_2,t_1),
\]
但不使它们消失。首个候选层为
\[
F_i(t_1,t_2)
=t_i\sum_jB_{ij}t_j^2+\cdots,
\qquad
B=
\begin{pmatrix}
a&b\\
b&a
\end{pmatrix}.
\]

在所声称的等尺度线上，
\[
F_1(t,t)=F_2(t,t)=(a+b)t^3+\cdots.
\]
因此正尺度解至少要求
\[
a+b=0
\]
或更高阶的特殊分支机制。对称性本身不蕴含这个等式。

简单模型已经说明问题：
\[
F(t)=t^3
\]
满足 \(F(t)=O(t^{5/2})\)，但在 \(t>0\) 没有小零点。Ozuch Remark 2.11 还允许精细展开出现对数项，真实首项可能是 \(t^3\log t\)。

所以：

* Ozuch 当前参数空间之外未发现额外种类的余核方向；
* 但同一个 \(J\)-偶径向方向中仍有未计算的高阶有限维条件；
* “全部有限维障碍消失”是错误表述。

---

## 三、Biquard IFT 不能直接给出所声称的存在性

Lyapunov–Schmidt 分解为
\[
\Pi^\perp\Phi(g^A+x)=0,\qquad
\Pi\Phi(g^A+x)=0.
\]

补空间 IFT 或压缩映射至多先求得 \(x=x(t)\)，满足第一式。随后必须精确求解有限维映射
\[
\mathcal F(t):=\Pi\Phi(g^A+x(t))=0.
\]

需要区分两种情形：

* 若由某个精确恒等式证明**完整函数**
  \(\mathcal F(t)\equiv0\)，则无需对尺度方向要求非退化，补空间求解足以产生解；
* 当前只证明了 \(\mathcal F\) 的若干低阶系数为零。这使尺度零点更退化，而不是自动满足方程。

此外，所引 [Biq13] 的具体解消定理处于渐近双曲背景；Ozuch 明确强调该背景可利用共形无穷远参数，而紧致问题具有不同的有限维平衡。现有材料没有给出一个可直接应用于此紧致四节点构造、并以 \(\lambda=\mu=\nu=0\) 为充分条件的 Biquard 定理。

---

## 四、\(\mathbf O(g_o)\) 并不平凡

Ozuch 定义的是全体对称二张量上的
\[
\mathbf O(g_o)
=
\ker_{L^2}\!\left(\frac12\nabla^*\nabla-\mathring R\right),
\]
而不是 TT 核。

令 \(u_1,u_2\) 为两个球因子的轴向一次球谐函数；它们在半转下不变并下降到商。由
\[
\Delta u_i=2\Lambda u_i,
\qquad
\mathring R(u_i g_j)=\Lambda u_i g_j,
\]
得到
\[
P(u_i g_j)=0.
\]
故存在四维核
\[
\operatorname{span}
\{u_1g_1,u_1g_2,u_2g_1,u_2g_2\}.
\]

这不与 TT 核为零矛盾。相对形状模态满足
\[
P(g_1-g_2)=-\Lambda(g_1-g_2),
\]
也不是零模态。

不过 \(A\) 对每个 \(u_i\) 取负号而保持 \(g_j\)，故这四个核张量全为 \(A\)-奇；在 \(A\)-不变构造中，残差与其配对严格为零。因此正确说法是：

\[
\boxed{\mathbf O(g_o)\neq0,\quad
\text{但其 }A\text{-不变部分为零，故 }\nu_l=0.}
\]

这要求在 \(A\)-不变 Banach 空间中重新陈述椭圆/IFT 论证；不能把 published full-space hypothesis 简单替换成“核为零”。

---

## 五、可积性

### Eguchi–Hanson 端

EH 的三个 \(L^2\) 核方向由显式族
\[
\zeta\longmapsto \mathrm{eh}_{\zeta^\pm}
\]
微分得到，因此都是可积的 Ricci-flat ALE 变形。

### 乘积 orbifold 端

在全对称二张量空间里，可积性并非由 “TT 核为零” 自动推出，因为上述四个非 TT 核方向仍存在。至少 \(u_1g_1,u_2g_2\) 是 Lie 导数方向；交叉方向的完整可积性没有由现有来源建立。因而不能逐字应用 Ozuch 2020 的“所有 \(\mathbf O(g_o)\) 方向可积”假设。

在 \(A\)-不变子空间中这些方向全部消失，所以可积性可视为真空成立，但需要一版明确的等变限制论证。

Ozuch 2021 Proposition A.2 只解释特定 Taub/一阶解消障碍的消失；该文明确说它没有恢复 Ozuch 2020 的高阶障碍，故不能消去当前剩余径向映射。

---

## 六、负模态 \(g_1-g_2\)

该模态本身不是障碍：
\[
P(g_1-g_2)=-\Lambda(g_1-g_2),
\]
其特征值与零有固定距离。算子不定不妨碍 IFT；所需的是可逆性而非正定性。

若对应近似模态在拼接后具有
\[
-\Lambda+o(1)
\]
的特征值，则它的逆贡献确实为 \(O(1)\)。但这一个模态的估计不等于完整的一致逆估计：仍须排除颈区或其他补空间方向产生趋零特征值。因此它**不构成反证**，也**不能代替**完整 weighted inverse estimate。

---

## 七、拓扑

由固定点公式，
\[
\chi\!\left((S^2\times S^2)/\mathbb Z_2\right)
=\frac{4+4}{2}=4.
\]
每个 \(A_1\) 解消以例外 \(S^2\) 替换一点，使 Euler 数增加 \(1\)，故
\[
\chi(M)=8.
\]
两正、两负手征使
\[
\tau(M)=0.
\]

但 \((\chi,\tau)=(8,0)\) 本身不能区分奇、偶交叉形式。根据 Step 77 的拓扑表，**两正节点位于相对角的对角手征图案**对应偶形式
\[
3H,
\]
因而为
\[
\#_3(S^2\times S^2).
\]
相邻的两正节点则对应奇形式
\[
3\langle1\rangle\oplus3\langle-1\rangle
\]
及 \(3\mathbb{CP}^2\#3\overline{\mathbb{CP}}^{\,2}\)。二者不能称为通过 “wall-crossing” 等价。

---

## 八、文献先例

所给来源没有构造 \(\#_3(S^2\times S^2)\) 上的 Einstein 度量，也不足以支持全局性的“文献中此前未知”断言。可以严格说：

> 该度量若由此方法构造出来，将不是所给 Ozuch/Biquard 材料中已有的结果；是否为全局文献中的首次结果，需要额外系统检索。

---

## 对七个问题的简答

1. **障碍消失不完整。** 横向塔消失，已知二阶径向系数消失；高阶 \(J\)-偶径向条件仍在。
2. **IFT 只有在完整约化映射恒等为零时才自动闭合。** 当前只有低阶 Taylor 数据为零，属于退化情况。
3. **\(-\Lambda\) 模态本身无害。** 但完整的 uniform inverse estimate 尚未证明。
4. **\(\mathbf O(g_o)\neq0\)。** 有四个非 TT 核模态；其投影因 \(A\)-奇偶性消失。
5. **EH 变形可积。** 全 orbifold 核的可积性不是空条件；在 \(A\)-不变子空间中才真空成立。
6. **\(\chi=8,\tau=0\) 正确。** 对角相对角图案根据给定拓扑表给出 \(\#_3(S^2\times S^2)\)，需要偶交叉形式而不仅是 \(\chi,\tau\)。
7. **所给文献无先例，也无存在性证明。**

决定性未解对象是完整的等变径向约化函数，特别是
\[
F_i=t_i\sum_jB_{ij}t_j^2+\cdots
\]
中的 \(a+b\)、可能的对数项，以及随后的一致补空间逆估计。
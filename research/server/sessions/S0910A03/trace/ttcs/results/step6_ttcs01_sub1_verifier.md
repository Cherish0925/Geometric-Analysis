# TTCS Independent Branch Record

```json
{
  "step_id": 6,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step5_regular_patch_and_derdzinski_boundary.tex",
    "Knowledge/objects/papers/Conformal-Kähler-rigidity-of-Einstein-four-manifolds--ee41ec8c511e--4518ab125268/object.md",
    "Sessions/S0910A03/trace/ttcs/results/step5_ttcs01_verifier1_integration.md",
    "Sessions/S0910A01/workspace/notes/step7_local_vs_global_rigidity.md"
  ]
}
```

## Task

Independently test the proposed first-order projector argument on an oriented Einstein four-manifold. Assume W+ as a symmetric endomorphism of Λ+ has two constant distinct eigenvalues, one simple and one double: W+=μ I+(λ−μ)P where P is the orthogonal rank-one projection determined by a local normalized self-dual eigenform ω. Starting from δW+=0 (equivalently ∇^a W^+_{ab cd}=0, with all tensor symmetries and normalization factors handled), derive the exact first-order equations for ∇ω. Decide whether they force ∇ω=0 for either sign of λ−μ. Explicitly check the tempting projection step ω_ab∇^aω_cd=0: identify every surviving term, especially derivatives of the first ω factor/divergence terms, and use self-dual nondegeneracy correctly. Cross-check against the supplied Derdziński-style eigenframe equations. Then combine the answer with the Einstein–Weyl Weitzenböck identity at spectrum (−1/6,1/12,1/12), s=−4, and state whether this local calibrated system is inconsistent. Provide a direct mathematical memo, not a general literature summary.

## Output

# 数学核验备忘录

## 1. 投影算子的张量归一化

采用
\[
\langle\alpha,\beta\rangle=\frac12\alpha_{ab}\beta^{ab},
\qquad
(A\alpha)_{ab}=\frac12A_{ab}{}^{cd}\alpha_{cd}.
\]
取局部自对偶本征形式 \(\omega\)，归一化为
\[
|\omega|^2=2.
\]
则简单本征线上的正交投影为
\[
P(\alpha)=\frac{\langle\alpha,\omega\rangle}{2}\,\omega,
\qquad
P_{ab\,cd}=\frac12\omega_{ab}\omega_{cd}.
\]
因此，令 \(\kappa=\lambda-\mu\neq0\)，有
\[
W^+_{ab\,cd}
=\mu\,(\mathbb I^+)_{ab\,cd}
+\frac{\kappa}{2}\omega_{ab}\omega_{cd},
\tag{1}
\]
其中 \(\mathbb I^+\) 是 \(\Lambda^+\) 上的恒等算子；迹零还给出
\[
\lambda+2\mu=0.
\]

由于 \(\lambda,\mu\) 都是常数，且 \(\nabla\mathbb I^+=0\)，Einstein 条件给出的
\(\nabla^aW^+_{ab\,cd}=0\) 等价于
\[
(\nabla^a\omega_{ab})\omega_{cd}
+\omega_{ab}\nabla^a\omega_{cd}=0.
\tag{2}
\]
这里第一项绝不能直接丢去。记
\[
\xi_b:=\nabla^a\omega_{ab}.
\]
则完整方程是
\[
\xi_b\omega_{cd}+\omega_{ab}\nabla^a\omega_{cd}=0.
\tag{3}
\]

## 2. 沿 \(\omega\) 与 \(\omega^\perp\) 分解

固定长度意味着
\[
\omega^{cd}\nabla_a\omega_{cd}
=\frac12\nabla_a(\omega^{cd}\omega_{cd})=0,
\tag{4}
\]
所以 \(\nabla_a\omega\in\omega^\perp\)。

将 (3) 的 \(cd\) 槽投影到 \(\mathbb R\omega\)，第二项消失，得到
\[
\xi_b=0.
\tag{5}
\]
等价地，直接与 \(\omega^{cd}\) 收缩：
\[
0=4\xi_b+
\omega_{ab}(\nabla^a\omega_{cd})\omega^{cd}
=4\xi_b.
\]

再投影到 \(\omega^\perp\)，第一项消失，得到
\[
\omega_{ab}\nabla^a\omega_{cd}=0.
\tag{6}
\]
因此这个“投影步骤”最终是成立的，但成立原因是两个正交分量分别消失，而不是因为对第一因子求导的项不存在。

归一化自对偶二形式满足
\[
\omega_a{}^c\omega_c{}^b=-\delta_a{}^b,
\tag{7}
\]
也可由
\[
\omega\wedge\omega=|\omega|^2\,dV=2\,dV
\]
看出其逐点非退化性。于是 (6) 中作用在导数指标上的矩阵
\(\omega^a{}_b\) 可逆，故
\[
\boxed{\nabla\omega=0.}
\tag{8}
\]
进而
\[
\boxed{\nabla P=0,\qquad \nabla W^+=0.}
\tag{9}
\]
推导只使用 \(\kappa\neq0\)，所以对 \(\lambda-\mu\) 的两种符号完全相同。

## 3. 与 Derdziński 本征标架方程的对应

取所给标架
\[
\omega_1=e^{12}+e^{34},\quad
\omega_2=e^{13}-e^{24},\quad
\omega_3=e^{14}+e^{23},
\]
并令简单本征形式为 \(\omega_1=\omega\)，写成
\[
\nabla\omega_1=a\otimes\omega_2-c\otimes\omega_3.
\tag{10}
\]
代入 (3) 后，完整的一阶方程为
\[
\begin{aligned}
0={}&
\bigl(\iota_{a^\sharp}\omega_2-\iota_{c^\sharp}\omega_3\bigr)_b
(\omega_1)_{cd}\\
&+\bigl(\iota_{a^\sharp}\omega_1\bigr)_b(\omega_2)_{cd}
-\bigl(\iota_{c^\sharp}\omega_1\bigr)_b(\omega_3)_{cd}.
\end{aligned}
\tag{11}
\]
由于 \(\omega_1,\omega_2,\omega_3\) 线性无关，
\[
\iota_{a^\sharp}\omega_1=0,\qquad
\iota_{c^\sharp}\omega_1=0,\qquad
\iota_{a^\sharp}\omega_2-\iota_{c^\sharp}\omega_3=0.
\tag{12}
\]
\(\omega_1\) 非退化，前两式立即给出
\[
a=c=0,
\]
与 (8) 一致。

所给 Derdziński 型公式在重标记后为
\[
d\lambda
=(\lambda-\mu)\bigl(
\iota_{a^\sharp}\omega_3+\iota_{c^\sharp}\omega_2
\bigr).
\tag{13}
\]
当本征值都是常数时，它只给出
\[
\iota_{a^\sharp}\omega_3+\iota_{c^\sharp}\omega_2=0.
\tag{14}
\]
这是 \(\delta W^+=0\) 的一个收缩结果，不是完整张量方程。

例如取 \(a=e^1,\ c=e^2\)，则
\[
\iota_{e_1}\omega_3+\iota_{e_2}\omega_2=e^4-e^4=0,
\]
甚至
\[
\iota_{e_1}\omega_2-\iota_{e_2}\omega_3=0,
\]
但 (11) 的其余部分为
\[
e^2\otimes\omega_2+e^1\otimes\omega_3\neq0.
\]
因此仅使用 (13) 会遗漏正交于简单本征线的两个张量分量；完整投影方程把 \(a,c\) 都消去。

## 4. 校准谱与 Einstein–Weyl 恒等式

在当前本征值约定下，所给 Einstein–Weyl 公式为
\[
0=\nabla^*\nabla W^+
+\frac{s}{2}W^+
-6(W^+)^2
+2|W^+|^2\mathbb I^+.
\tag{15}
\]
令 \(\Delta=\nabla^a\nabla_a\)，收缩得到
\[
\frac12\Delta|W^+|^2
=
|\nabla W^+|^2
+\frac{s}{2}|W^+|^2
-18\det W^+.
\tag{16}
\]

对
\[
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right),
\qquad s=-4,
\]
有
\[
|W^+|^2=\frac1{24},
\qquad
\det W^+=-\frac1{864}.
\]
本征值为常数，故左端为零，于是
\[
0
=|\nabla W^+|^2-\frac1{12}+\frac1{48}
=|\nabla W^+|^2-\frac1{16}.
\]
所以
\[
\boxed{|\nabla W^+|^2=\frac1{16}.}
\tag{17}
\]
这与投影方程给出的 \(\nabla W^+=0\) 直接矛盾。所给另一份笔记中的 \(1/24\) 来自系数为 \(s/3\) 与 \(-4\operatorname{tr}(W^3)\) 的公式；它不对应这里的 Weyl 端同态约定及所给 Lemma 2.5。当前约定下数值是 \(1/16\)。

还有一个独立印证：由 \(\nabla\omega=0\)，度量局部为 Kähler；当 \(s=-4\) 时，Kähler 曲面的自对偶 Weyl 谱必须是
\[
\left(-\frac23,\frac13,\frac13\right),
\]
而不是校准谱。

## 结论

\[
\boxed{\text{具有上述恒定校准谱且 }\operatorname{Ric}=-g
\text{ 的局部 Einstein 系统不存在。}}
\]

局部正函数方程 \(\Delta f=-f/2\) 本身虽有解，但它只处理标量曲率的共形变换，并未包含 (2) 的完整一阶 harmonic-Weyl 方程。Derdziński 的典范共形乘子由简单本征值的固定幂确定；简单本征值为常数时，该乘子也是常数，因此不能产生所述非平行局部模型。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 6,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step6_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step6_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently test the proposed first-order projector argument on an oriented Einstein four-manifold. Assume W+ as a symmetric endomorphism of Λ+ has two constant distinct eigenvalues, one simple and one double: W+=μ I+(λ−μ)P where P is the orthogonal rank-one projection determined by a local normalized self-dual eigenform ω. Starting from δW+=0 (equivalently ∇^a W^+_{ab cd}=0, with all tensor symmetries and normalization factors handled), derive the exact first-order equations for ∇ω. Decide whether they force ∇ω=0 for either sign of λ−μ. Explicitly check the tempting projection step ω_ab∇^aω_cd=0: identify every surviving term, especially derivatives of the first ω factor/divergence terms, and use self-dual nondegeneracy correctly. Cross-check against the supplied Derdziński-style eigenframe equations. Then combine the answer with the Einstein–Weyl Weitzenböck identity at spectrum (−1/6,1/12,1/12), s=−4, and state whether this local calibrated system is inconsistent. Provide a direct mathematical memo, not a general literature summary.

## Integrated Scientific Memo

# 数学核验备忘录

设 \((M^4,g)\) 为定向 Einstein 流形，因而
\[
\delta W^+=0.
\]
假设 \(W^+:\Lambda^+\to\Lambda^+\) 有两个处处常且不同的本征值：简单本征值 \(\lambda\) 与二重本征值 \(\mu\)。取局部简单本征形式 \(\omega\)，采用
\[
\langle\alpha,\beta\rangle=\frac12\alpha_{ab}\beta^{ab},
\qquad |\omega|^2=2.
\]
令 \(P\) 为 \(\mathbb R\omega\) 上的正交投影，则
\[
P(\alpha)=\frac{\langle\alpha,\omega\rangle}{2}\omega,
\qquad
P_{ab\,cd}=\frac14\omega_{ab}\omega_{cd}
\]
作为作用律
\[
(P\alpha)_{ab}=\frac12P_{ab}{}^{cd}\alpha_{cd}
\]
下的四阶张量。因此
\[
W^+_{ab\,cd}
=\mu I^+_{ab\,cd}
+\frac{\lambda-\mu}{4}\omega_{ab}\omega_{cd}.
\tag{1}
\]
若不用四阶张量的额外 \(1/2\) 作用约定，而直接把 \(P\) 写作双线性核，则相应系数为 \(1/2\)；以下散度方程不受这个总体非零常数影响。

## 1. 完整的一阶投影方程

因为 \(\lambda,\mu\) 常且 \(\nabla I^+=0\)，由 \(\lambda-\mu\ne0\) 及 \(\nabla^aW^+_{ab\,cd}=0\) 得
\[
(\nabla^a\omega_{ab})\omega_{cd}
+\omega_{ab}\nabla^a\omega_{cd}=0.
\tag{2}
\]
记
\[
\xi_b:=\nabla^a\omega_{ab}.
\]
则
\[
\xi_b\omega_{cd}+\omega_{ab}\nabla^a\omega_{cd}=0.
\tag{3}
\]

固定长度给出
\[
\omega^{cd}\nabla_a\omega_{cd}=0.
\tag{4}
\]
将 (3) 与 \(\omega^{cd}\) 收缩：
\[
0=(\omega_{cd}\omega^{cd})\xi_b
+\omega_{ab}\omega^{cd}\nabla^a\omega_{cd}
=4\xi_b,
\]
故
\[
\boxed{\xi_b=\nabla^a\omega_{ab}=0.}
\tag{5}
\]
代回 (3)：
\[
\boxed{\omega_{ab}\nabla^a\omega_{cd}=0.}
\tag{6}
\]

所以这个“诱人的投影步骤”结论确实成立，但不能从一开始删去对第一因子求导所得的散度项。严格顺序是：

1. 展开 \(\nabla(\omega\otimes\omega)\)，保留两个乘积法则项；
2. 向 \(\mathbb R\omega\) 投影，得到 \(\operatorname{div}\omega=0\)；
3. 再向 \(\omega^\perp\) 投影，得到 (6)。

归一化非零自对偶二形式满足
\[
\omega_a{}^c\omega_c{}^b=-\delta_a{}^b,
\tag{7}
\]
故它作为 \(TM\to T^*M\) 的映射可逆。于是 (6) 对每个固定 \(c,d\) 都意味着
\[
\boxed{\nabla_a\omega_{cd}=0.}
\tag{8}
\]
因此
\[
\boxed{\nabla P=0,\qquad \nabla W^+=0.}
\tag{9}
\]
这里只用到 \(\lambda-\mu\neq0\)，所以对其正负号没有区别。

## 2. Derdziński 本征标架交叉核验

取标准局部正交标架
\[
\omega_1=e^{12}+e^{34},\quad
\omega_2=e^{13}-e^{24},\quad
\omega_3=e^{14}+e^{23},
\]
令 \(\omega_1=\omega\)，并写
\[
\nabla\omega_1=a\otimes\omega_2-c\otimes\omega_3.
\tag{10}
\]
则
\[
\xi
=\iota_{a^\sharp}\omega_2-\iota_{c^\sharp}\omega_3,
\]
而
\[
\omega_{1\,ab}\nabla^a\omega_{1\,cd}
=
(\iota_{a^\sharp}\omega_1)_b(\omega_2)_{cd}
-(\iota_{c^\sharp}\omega_1)_b(\omega_3)_{cd}.
\]
完整散度方程即
\[
\begin{aligned}
0={}&
\bigl(\iota_{a^\sharp}\omega_2-\iota_{c^\sharp}\omega_3\bigr)\otimes\omega_1\\
&+\iota_{a^\sharp}\omega_1\otimes\omega_2
-\iota_{c^\sharp}\omega_1\otimes\omega_3.
\end{aligned}
\tag{11}
\]
按 \(\omega_1,\omega_2,\omega_3\) 分量分别比较：
\[
\iota_{a^\sharp}\omega_1=0,\qquad
\iota_{c^\sharp}\omega_1=0,\qquad
\iota_{a^\sharp}\omega_2-\iota_{c^\sharp}\omega_3=0.
\tag{12}
\]
由 \(\omega_1\) 非退化，
\[
a=c=0,
\]
从而再次得到 \(\nabla\omega_1=0\)。

这并不与供应材料中的 Derdziński 型本征值方程矛盾。该材料给出的
\[
d\mu_1=(\mu_1-\mu_2)\iota_{a^\sharp}\omega_3
      +(\mu_1-\mu_3)\iota_{c^\sharp}\omega_2
\tag{13}
\]
只是完整 \(\delta W^+=0\) 系统的一个特定收缩。当前 \(\mu_2=\mu_3=\mu\)、\(d\mu_1=0\) 时，它仅给出
\[
\iota_{a^\sharp}\omega_3+\iota_{c^\sharp}\omega_2=0,
\tag{14}
\]
本身不足以推出 \(a=c=0\)。遗漏的是 (11) 中沿 \(\omega_2,\omega_3\) 的两个独立分量。换言之，Derdziński 收缩公式与完整方程相容，但不能替代完整方程。

## 3. 校准谱的 Weitzenböck 检验

采用供应论文 Lemma 2.5 的端同态约定，Einstein 情形满足
\[
0=\nabla^*\nabla W^+
+\frac{s}{2}W^+
-6(W^+)^2
+2|W^+|^2I.
\tag{15}
\]
相应标量恒等式可写为
\[
\Delta |W^+|^2
=
2|\nabla W^+|^2+s|W^+|^2-36\det W^+,
\tag{16}
\]
其中 \(\Delta=\operatorname{div}\nabla\)；等价地，
\[
\frac12\Delta|W^+|^2
=
|\nabla W^+|^2+\frac{s}{2}|W^+|^2-18\det W^+.
\tag{17}
\]

在谱
\[
\left(-\frac16,\frac1{12},\frac1{12}\right),
\qquad s=-4
\]
处，
\[
|W^+|^2=\frac1{24},\qquad
\det W^+=-\frac1{864}.
\]
谱常数意味着 \(|W^+|^2\) 常数，故 (17) 给出
\[
0
=
|\nabla W^+|^2-\frac1{12}+\frac1{48},
\]
即
\[
\boxed{|\nabla W^+|^2=\frac1{16}.}
\tag{18}
\]
这与完整一阶方程所得
\[
\nabla W^+=0
\]
直接矛盾。

数值 \(1/24\) 来自另一套不相容的标量 Bochner 系数；它虽在 Kähler–Einstein 测试上偶然也可抵消，但不对应这里由 (15) 导出的端同态约定。对本题应使用 \(1/16\)。

另有独立检查：\(\nabla\omega=0\) 使 \(g\) 局部 Kähler；若 \(s=-4\)，其 \(W^+\) 谱必为
\[
\left(-\frac23,\frac13,\frac13\right)
\]
（按排序可能重排），而非校准谱。

## 结论

\[
\boxed{
\text{常本征值谱 }
(-1/6,1/12,1/12),\ s=-4,\ \delta W^+=0
\text{ 的局部校准系统不相容。}}
\]

先前“局部共形 Kähler 且共形因子满足 \(\Delta f=-f/2\)，所以局部可行”的论证遗漏了完整的 projector 散度方程。Derdziński 的一般两本征值模型允许本征值变化；但在本题额外假设两个本征值均为常数时，完整一阶系统强迫简单本征线平行，随后与 Einstein–Weyl 恒等式冲突。
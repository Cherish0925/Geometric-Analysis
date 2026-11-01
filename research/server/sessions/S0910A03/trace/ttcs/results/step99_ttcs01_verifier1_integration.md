# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 99,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step99_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step99_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following Raychaudhuri normal-cost analysis and assess whether a tangential cost floor exists.

For a Gaussian 4-metric g = dr² + q(r,s) with H = tr(q⁻¹q_r/2), W° = W - (H/3)I, and E = Ric + 3g:

(1) The Raychaudhuri identity H' + H²/3 + |W°|² = 3 - E_rr gives, with u = H - 3tanh r and integration against cosh²(r):
   ∫₀ᴿ cosh²(r)(-E_rr)dr = 3cosh²(R)(1-tanh R) + ∫₀ᴿ cosh²(r)[|W°|²+u²/3]dr
for any trial with H(0)=0 (minimal center), H(R)=3 (expanding). This identity was numerically verified with residual 3.4×10⁻³.

(2) The comparison ODE h'=(3+δ)-h²/3, h(0)=0, h(R)=3 forces 1≤k tanh(kR) where k=√(1+δ/3). At R=1: δ_min≈1.318. Asymptotically: δ_min~12e^{-2R}.

(3) For the conformal expansion q = cosh²(r)q₀(s) of a charged Koiso separator (scalar curvature -7, winding 2, S=1, Qmax=0.5):
   E_rr = E_ri = 0 exactly
   E_T = Ric(q₀) + 2q₀, with operator norm 9.94 at r=0, decaying as sech²(r)
   The metric has H(0)=0 and K(0)=0, so it does NOT match the charged Koiso Weingarten.

(4) For the quintic jet-preserving transition on [0,1] matching the charged center jets to expanding exterior:
   E_T dominates: peak 28.7 at r≈0.28, while Enn peaks at 10.7
   The dominant E_T term is Ric(q): the quintic creates intermediate metrics with spatial curvature up to 21.4

QUESTION: Is there a tangential-block analog of the Raychaudhuri floor? Specifically, must ‖E_T‖_op exceed some positive lower bound on [0,R] for any metric with H(0)=0 matching the charged Koiso center and H(R)=3? Or could the exact Einstein continuation (if it exists) achieve E_T=0 throughout, with the actual transition cost depending only on where the germ domain ends?

The conformal expansion suggests the tangential cost is 9.94·sech²(r_transition), which goes to zero as the transition point moves to larger r. This would mean the tangential cost has no floor — it depends on how far the exact Einstein germ extends.

## Integrated Scientific Memo

## 核验结论

### 1. Raychaudhuri 加权恒等式正确，但须保留下端边界项

令
\[
K=\frac12q_r,\qquad W=q^{-1}K,\qquad H=\operatorname{tr}W .
\]
则
\[
\operatorname{Ric}_{rr}=-H'-\operatorname{tr}(W^2)
=-H'-\frac{H^2}{3}-|W^\circ|^2,
\]
所以
\[
H'+\frac{H^2}{3}+|W^\circ|^2=3-E_{rr}.
\]

置 \(u=H-3\tanh r\)。因为
\[
(3\tanh r)'+\frac{(3\tanh r)^2}{3}=3,
\]
有
\[
u'+2\tanh r\,u+\frac{u^2}{3}+|W^\circ|^2=-E_{rr}.
\]
乘以 \(\cosh^2r\) 后：
\[
\bigl(\cosh^2r\,u\bigr)'
+\cosh^2r\left(\frac{u^2}{3}+|W^\circ|^2\right)
=\cosh^2r(-E_{rr}).
\]
故一般形式为
\[
\int_0^R\cosh^2r(-E_{rr})\,dr
=
\cosh^2R\,u(R)-u(0)
+\int_0^R\cosh^2r
\left(\frac{u^2}{3}+|W^\circ|^2\right)dr.
\]
当 \(H(0)=0,\ H(R)=3\) 时，恰得题述公式。

数值上
\[
1.7030029+0.9641074+1.7295474-4.3932304
=0.0034274,
\]
与记录一致，约为左侧的 \(7.8\times10^{-4}\)。

`hyperbolic_validation` 中约 \(3.000112\) 的“残差”不是恒等式失效，而是该测试满足 \(H(0)=3\)，却漏掉了 \(-u(0)=-3\)。补回后误差约 \(1.12\times10^{-4}\)。

该恒等式逐个 \(s\) 成立；固定坐标测度的 \(s\)-平均仍成立，而随 \(r\) 变化的切片体积平均会产生额外项。

---

### 2. 正常块的点态下界正确

若全区间
\[
E_{rr}\ge-\delta,
\]
则
\[
H'\le 3+\delta-\frac{H^2}{3}.
\]
比较方程
\[
h'=3+\delta-\frac{h^2}{3},\qquad h(0)=0
\]
的解是
\[
h(r)=3k\tanh(kr),\qquad k=\sqrt{1+\frac{\delta}{3}}.
\]
由 \(H(R)=3\) 必须有
\[
1\le k\tanh(kR).
\]
因此
\[
\sup_{[0,R]}(-E_{rr})\ge\delta_*(R),
\qquad
\delta_*(R)=3(k_R^2-1),
\quad k_R\tanh(k_RR)=1.
\]
在 \(R=1\)：
\[
\delta_*(1)=1.317686519\ldots
\]
且
\[
\delta_*(R)=12e^{-2R}+O(Re^{-4R}).
\]

应区分两个量：

* 点态下界 \(\delta_*(R)\to0\)；
* 加权积分边界项
  \[
  3\cosh^2R(1-\tanh R)\longrightarrow\frac32.
  \]

因此正常块存在每个固定 \(R\) 的点态 floor，但不存在由此推得的、在 \(R\to\infty\) 后仍为正的统一点态 floor。

---

### 3. 共形模型计算正确，但不能证明 charged connector 无切向 floor

对
\[
q(r)=\cosh^2r\,q_0
\]
有
\[
W=\tanh r\,I,\qquad H=3\tanh r,
\]
以及
\[
E_{rr}=E_{ri}=0,\qquad
E_T=\operatorname{Ric}(q_0)+2q_0.
\]
后一个等式是协变张量等式；其相对于 \(q(r)\) 的算子为
\[
E_T^\sharp
=\operatorname{sech}^2r\,
q_0^{-1}\bigl(\operatorname{Ric}(q_0)+2q_0\bigr),
\]
故
\[
\|E_T\|_{\mathrm{op}}
=9.9372539\,\operatorname{sech}^2r.
\]

但该模型有两个决定性失配：

\[
K(0)=0,\qquad W^\circ\equiv0,
\]
而 charged Koiso 中心具有非零无迹 Weingarten 数据。事实上由中心约束
\[
\operatorname{tr}_qE_T-E_{rr}
=R(q)+6-H^2+|W|^2
\]
以及 \(R(q_0)=-7,\ H=0,\ E=0\)，可得 charged 中心
\[
|W^\circ(0)|^2=1.
\]

此外，共形模型在有限 \(R\) 只有
\[
H(R)=3\tanh R<3,
\]
并不满足题设末端条件。因此
\[
9.94\,\operatorname{sech}^2(r_{\rm transition})
\]
只是该剪切为零的特定 ansatz 的缺陷衰减，并不是从 charged 中心出发的连接代价，也不能证明相关 infimum 为零。

忠实的 charged 中心二阶 jet 反而满足
\[
E_T(0)=0.
\]
所以中心非零剪切本身不是切向缺陷；真正 Einstein 度量完全可以携带剪切。

---

## 切向块是否存在 Raychaudhuri 型 floor？

### 没有已知的直接切向类比

切向迹满足
\[
\operatorname{tr}_qE_T=R(q)+9-H'-H^2,
\]
其中切片标量曲率 \(R(q)\) 没有可用的固定符号。无迹部分可写成剪切演化方程
\[
(W^\circ)'+H W^\circ
=\bigl[\operatorname{Ric}(q)^\sharp\bigr]^\circ-E_T^\circ.
\]
这里不存在类似
\[
|W^\circ|^2+\frac{u^2}{3}\ge0
\]
的标量正定被积项，因而 Raychaudhuri 比较论证不能推出
\[
\sup\|E_T\|_{\mathrm{op}}\ge c>0.
\]

### \(E_T\equiv0\) 的精确陈述

令
\[
C=E_{rr},\qquad J_i=E_{ri}.
\]
由 contracted Bianchi identity，在 \(E_T=0\) 时得到约束传播系统
\[
\partial_r C=-2D^iJ_i-2HC,\qquad
\partial_rJ_i=\frac12D_iC-HJ_i.
\]
若 charged 中心满足 \(C(0)=J(0)=0\)，则在具有相应唯一性的光滑/解析延拓区间内，
\[
C=J=0.
\]
因此在那里 \(E_T=0\) 实际上意味着 \(E=0\)：这是完整 Einstein 延拓，而不只是切向 Einstein。

这种精确 Einstein 延拓可以在自身 germ 区间上满足 \(E_T\equiv0\)，但它不可能一直延至有限的 \(H(R)=3\) 端点。因为若 \(E=0\)，则加权恒等式右侧为
\[
3\cosh^2R(1-\tanh R)
+\int_0^R\cosh^2r
\left(|W^\circ|^2+\frac{u^2}{3}\right)dr>0,
\]
与左侧零矛盾。等价地，
\[
H(r)\le3\tanh r<3.
\]

所以可以严格断言：

1. exact Einstein germ 上可以有 \(E_T\equiv0\)；
2. 它不可能在有限区间内同时到达 \(H(R)=3\)；
3. 每个这样的有限 connector 必有某处 \(E_T\ne0\)；
4. 但这不推出所有 connector 的
   \[
   \sup_{[0,R]}\|E_T\|_{\mathrm{op}}
   \]
   具有共同正下界。

最后一步失败的原因是 Bianchi 系统涉及 \(E_T\) 的导数：小的 \(C^0\) 切向残差可伴随很大的径向或空间导数。除非额外给出统一椭圆估计、非退化性和 \(C^{2,\alpha}\) 预紧性，精确零解的唯一性不能转化成定量的 \(C^0\) floor。在这种额外紧性假设下，才可由“无 \(E_T=0\) connector”推出一个依赖 \(R\)、端点数据及几何控制常数的正下界。

---

## 外部匹配导致的条件性 floor

若末端被固定为特定的非平坦外部
\[
q(R)=e^{2R}q_0,\qquad K(R)=q(R),\qquad K_r(R)=2q(R),
\]
则端点本身满足
\[
E_T(R)=\operatorname{Ric}(q_0)
\]
（协变形式），因而
\[
\sup_{[0,R]}\|E_T\|_{\mathrm{op}}
\ge
e^{-2R}
\left\|q_0^{-1/2}\operatorname{Ric}(q_0)q_0^{-1/2}\right\|_{\mathrm{op}}.
\]
数据中的 \(R=1\) 值 \(1.0741905\) 和 \(R=2.5\) 值 \(0.0534808\) 的比值恰为 \(e^{-3}\)。这是由所选外部强制的固定-\(R\) floor；换成精确平坦切片 cusp 末端后，该特定 floor 消失。

---

## 五次插值数据的正确解释

数据支持
\[
\sup\|E_T\|_{\mathrm{op}}=28.6631,\qquad
\sup\|\operatorname{Ric}(q)\|_{\mathrm{op}}=21.4219.
\]
但其他径向项也不小：
\[
\sup\|K_r\|_{\mathrm{op}}=11.94,\quad
\sup\|HK\|_{\mathrm{op}}=9.79,\quad
\sup\|2Kq^{-1}K\|_{\mathrm{op}}=9.64.
\]
因此空间 Ricci 是最大的单项，却不是唯一来源；总峰值来自多项相互作用。采样表中 \(\operatorname{Ric}(q)\) 约在 \(r=0.28\) 达峰，而 \(E_T\) 的显示峰值更接近 \(r=0.36\)，二者不应混同。所称 \(E_{rr}\) 峰值 \(10.7\) 不在当前两个 JSON 中，无法由所给数据独立核验。

## 最终判断

**正常块 floor 已严格成立并经数据支持。切向块在当前假设下没有已证明的 Raychaudhuri 型正下界。**

更准确地说：

* \(E_T\equiv0\) 的完整 finite-\(R\) connector 不可能存在；
* 但“每个 connector 均非零”不等于“其 \(C^0\) 范数有统一正下界”；
* 共形衰减模型因中心剪切和末端 \(H\) 均失配，不能证明 tangential infimum 为零；
* 切向代价不能只由 Einstein germ 结束的径向位置决定，还依赖结束处的 \(q,W^\circ\)、切片曲率以及所选外部匹配数据；
* 是否可随 germ 延长构造
  \[
  \sup\|E_T\|_{\mathrm{op}}\to0
  \]
  的忠实 charged、jet-preserving connector，仍是当前材料未解决的精确科学对象。
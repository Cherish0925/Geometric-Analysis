# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 7,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step7_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step7_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Investigate whether the full Einstein system Ric(g) = -g can have solutions on a 4-manifold with nil³ (Heisenberg) fiber structure over a 1D base.

The setup: total metric g = ds² + G_IJ(s)(dx^I + A^I(s))(dx^J + A^J(s)) where {e₁,e₂,e₃} generate the Heisenberg algebra [e₁,e₂] = e₃.

For abelian (torus) fibers over 1D base with Ric = -g, Lott's orbit-volume equation gives v'' = 3v (where v = √det G), which has no periodic solutions (contradicts ∫v'' = 0 on a circle). This cleanly excludes abelian collapse.

For nil³: the Heisenberg structure constant contributes negative fiber Ricci curvature R_fiber = -a₃²/(2a₁²a₂²), which partially compensates the positive mass term. The question is whether the full Einstein ODE system has:
(a) ANY periodic solution on a circle base
(b) ANY solution on an interval with controlled behavior at endpoints
(c) A generalized orbit-volume equation with positive coefficient

Key constraint: Ric(∂s,∂s) = -1 gives a₁''/a₁ + a₂''/a₂ + a₃''/a₃ = 1. The cross terms in v''/v = 1 + 2Σ_{i<j}(a_i'/a_i)(a_j'/a_j) can be negative, so the argument doesn't immediately extend from abelian.

Please determine whether a positive-coefficient orbit-volume inequality holds for nil³ with λ = -1, or construct/identify a mechanism that could allow nil³ negative Einstein solutions.

## Integrated Scientific Memo

## 结论

对 Heisenberg \( \mathrm{nil}^3 \) 轨道的一维余维 Einstein 系统，存在精确的非阿贝尔轨道体积方程，但其系数**并不普遍为正**：

\[
\boxed{\quad v''=\left(3-\frac{\rho}{2}\right)v,\qquad
\rho=\lvert[\cdot,\cdot]\rvert_{h_s}^{\,2}
=\frac{a_3^2}{a_1^2a_2^2}.\quad}
\]

因此：

- 不存在只由 \(\operatorname{Ric}(g)=-g\) 推出的统一点态不等式 \(v''\ge c\,v\)（\(c>0\)）。
- 尽管如此，完整 Einstein 系统对 \(\rho\) 有额外最大值原理，足以严格排除圆周基底上的周期解。
- 区间或射线上的 nil\(^3\) 负 Einstein 解确实存在；标准机制是复双曲 \(\mathbb CH^2\) 的 horospherical nil-cusp。
- 对有限区间，若两端的 bracket ratio 均保持 \(<6\)，尤其是两端均为光滑中心圆塌缩，则不存在两端闭合解；若要逃避此结论，至少一端必须进入 \(\rho\to\infty\) 的曲率爆破区，或形成非紧 cusp 端。

---

## 1. 完整共形一维 Einstein 方程

局部消去一维基底上的 shift 后写成

\[
g=ds^2+h_s.
\]

令

\[
L=\frac12h_s^{-1}\dot h_s,\qquad
H=\operatorname{tr}L=\frac{v'}v,\qquad
v=\sqrt{\det h_s}.
\]

超曲面 Ricci 公式为

\[
\operatorname{Ric}_{ss}=-H'-\operatorname{tr}(L^2),
\]

\[
\operatorname{Ric}^{\#}_{T}
=\operatorname{Ric}^{\#}_{h_s}-L'-HL.
\]

故 \(\operatorname{Ric}_g=-g\) 等价于

\[
H'+\operatorname{tr}(L^2)=1,
\]

\[
L'+HL=\operatorname{Ric}^{\#}_{h_s}+I.
\]

切向取迹得到

\[
H'+H^2=3+\operatorname{Scal}(h_s).
\]

由于 \(v'/v=H\)，有

\[
\frac{v''}{v}=H'+H^2
=3+\operatorname{Scal}(h_s).
\]

对 Heisenberg 代数，在正交标架中令

\[
[E_1,E_2]=mE_3,\qquad \rho=m^2.
\]

其纤维 Ricci 特征值是

\[
-\frac{\rho}{2},\qquad
-\frac{\rho}{2},\qquad
+\frac{\rho}{2},
\]

因而

\[
\operatorname{Scal}(h_s)=-\frac{\rho}{2}.
\]

这给出精确方程

\[
\boxed{v''=\left(3-\frac{\rho}{2}\right)v.}
\]

这也纠正了源脚本中尚未完成的猜测：nil 曲率项不是非负的“有效 \(F\)”项，而是通过负纤维标量曲率从 \(+3\) 中减去 \(\rho/2\)。

---

## 2. 对角情形的 Einstein ODE 与约束

取

\[
h_s=a_1^2(\theta^1)^2+a_2^2(\theta^2)^2+a_3^2(\theta^3)^2,
\qquad
d\theta^3=\theta^1\wedge\theta^2,
\]

并定义

\[
k_i=\frac{a_i'}{a_i},\qquad
H=k_1+k_2+k_3,\qquad
\rho=\frac{a_3^2}{a_1^2a_2^2}.
\]

则

\[
\begin{aligned}
k_1'+Hk_1&=1-\frac{\rho}{2},\\
k_2'+Hk_2&=1-\frac{\rho}{2},\\
k_3'+Hk_3&=1+\frac{\rho}{2},\\
H'+k_1^2+k_2^2+k_3^2&=1,
\end{aligned}
\]

以及

\[
\rho'=2\rho(k_3-k_1-k_2).
\]

Hamiltonian 约束为

\[
\boxed{
H^2-\sum_i k_i^2=2-\frac{\rho}{2}
}
\]

或等价地

\[
2\sum_{i<j}k_ik_j=2-\frac{\rho}{2}.
\]

因此源脚本所指出的交叉项并非完整系统中的自由量：

\[
\frac{v''}{v}
=1+2\sum_{i<j}k_ik_j
=3-\frac{\rho}{2}.
\]

---

## 3. 不存在普遍的正系数体积不等式

只有在附加控制

\[
\rho\le 6-\varepsilon
\]

时，才能得到

\[
v''\ge\frac{\varepsilon}{2}v.
\]

完整 ODE 确实允许局部数据满足 \(\rho>6\)。例如在一点取

\[
H=0,\qquad k_3=0,\qquad k_2=-k_1.
\]

Hamiltonian 约束化为

\[
-2k_1^2=2-\frac{\rho}{2},
\]

当 \(\rho>4\) 时有实解；取 \(\rho>6\)，便有

\[
v''=\left(3-\frac{\rho}{2}\right)v<0.
\]

标准 ODE 局部存在性随即给出局部 Einstein 解。因此任何无附加假设的 \(v''\ge c v\)、\(c>0\) 均为假。

---

## 4. 圆周基底：所有周期解均不存在

令中心方向上的 \(L\)-迹为 \(z\)，商空间
\(\mathfrak n/Z\) 上的迹为 \(a\)，并置

\[
D=z-a,\qquad H=a+z.
\]

由于 Heisenberg bracket 从
\(\Lambda^2(\mathfrak n/Z)\) 映至 \(Z\)，有

\[
\rho'=2\rho D.
\]

中心和水平切向 Einstein 方程分别给出

\[
z'+Hz=1+\frac{\rho}{2},
\qquad
a'+Ha=2-\rho.
\]

故闭合的标量子系统是

\[
\boxed{
\begin{aligned}
H'&=3-\frac{\rho}{2}-H^2,\\
D'&=-1+\frac{3\rho}{2}-HD,\\
\rho'&=2\rho D.
\end{aligned}}
\]

若 \(\rho\) 在内点取极值，则 \(D=0\)，并且

\[
\rho''=2\rho D'
=\rho(3\rho-2).
\]

所以：

- 内点局部最大值必满足 \(\rho\le 2/3\)；
- 内点局部最小值必满足 \(\rho\ge 2/3\)。

在圆周上 \(\rho\) 达到全局最大值，因此处处

\[
\rho\le\frac23.
\]

于是

\[
v''=\left(3-\frac{\rho}{2}\right)v
\ge\frac83v>0.
\]

轨道体积在 nilmanifold mapping torus 上是周期标量：返回映射为 lattice-preserving nilmanifold 微分同胚，保持 Haar 协体积。积分得到

\[
0=\int_{S^1}v''\,ds
\ge\frac83\int_{S^1}v\,ds>0,
\]

矛盾。因此

\[
\boxed{\text{不存在以 }S^1\text{ 为基底、}\mathrm{nil}^3
\text{ 为纤维且 }\operatorname{Ric}=-g\text{ 的解。}}
\]

即使允许水平 shear，此论证仍可保持：混合 Einstein 方程迫使 \(L\) 保持中心线，而水平无迹部分满足独立线性方程；上面的 \(H,D,\rho\) 系统不变。

---

## 5. 区间端点所能得到的严格结论

极值判据说明，若端点数据满足

\[
\limsup_{s\to\partial I}\rho(s)\le R<6,
\]

则 \(\rho\) 在整个有限区间内不超过 \(\max(R,2/3)<6\)。理由是任何更高的内部全局最大值都必须不超过 \(2/3\)。因此存在 \(c>0\) 使

\[
v''\ge cv.
\]

特别地，若有限区间两端均有 \(v\to0\)，则不可能存在正解：正的严格凸函数不能在有限区间两个端点同时趋于零。

光滑中心圆塌缩属于此情形。若 \(a_3\to0\)，而 \(a_1,a_2\) 保持正且有限，则

\[
\rho=\frac{a_3^2}{a_1^2a_2^2}\longrightarrow0.
\]

相容的形式展开为

\[
a_1(s)=a_1(0)\left(1+\frac{s^2}{4}+O(s^4)\right),
\]

\[
a_2(s)=a_2(0)\left(1+\frac{s^2}{4}+O(s^4)\right),
\]

\[
a_3(s)=s+O(s^5),
\]

从而

\[
\rho(s)=\frac{s^2}{a_1(0)^2a_2(0)^2}+O(s^4),
\qquad
v(s)=a_1(0)a_2(0)s+O(s^3).
\]

所以单个光滑中心塌缩端局部上与 Einstein ODE 相容，但两个这样的有限端不能连接。

不能仅凭现有标量系统断言所有区间解必然趋于复双曲 fixed point 或 \(\rho\to\infty\)；完整的全局相图分类尚未给出。严格成立的是：若区间解进入 \(\rho\ge6\) 区域以抵消体积凸性，由于内部高峰不可能出现，这种高 bracket norm 必须由端点方向输入。

---

## 6. nil\(^3\) 负 Einstein 解的真实存在机制

令

\[
\alpha=\frac1{\sqrt6},
\]

并取

\[
\boxed{
g=ds^2
+e^{2\alpha s}\bigl((\theta^1)^2+(\theta^2)^2\bigr)
+\frac23e^{4\alpha s}(\theta^3)^2,
\qquad
d\theta^3=\theta^1\wedge\theta^2.
}
\]

此时

\[
k_1=k_2=\alpha,\qquad k_3=2\alpha,\qquad
H=4\alpha,\qquad \rho=\frac23.
\]

代入可得

\[
Hk_1=\frac23=1-\frac{\rho}{2},
\qquad
Hk_3=\frac43=1+\frac{\rho}{2},
\]

以及

\[
k_1^2+k_2^2+k_3^2=1.
\]

故

\[
\operatorname{Ric}_g=-g.
\]

这就是适当归一化的复双曲平面 \(\mathbb CH^2\) 的 horospherical 表示。其轨道体积满足

\[
v''=\frac83v,
\qquad
v\asymp e^{4s/\sqrt6}.
\]

对 Heisenberg 纤维取 lattice 商，可在 \(s\to-\infty\) 得到完整的有限体积 nil cusp。它不能闭合为圆周 mapping torus，因为所需返回映射是 Heisenberg dilation，改变 Haar 协体积，而非保持 lattice 的体积保持自同构。

---

## 最终分类性答案

\[
\boxed{
\begin{array}{c|c}
\text{问题} & \text{结论}\\ \hline
\text{普遍正系数轨道体积不等式} &
\text{不存在； }v''=(3-\rho/2)v\\[1mm]
\text{圆周基底上的周期解} &
\text{不存在}\\[1mm]
\text{有限区间，两端 }\rho<6\text{ 且 }v\to0 &
\text{不存在}\\[1mm]
\text{单个光滑中心塌缩端} &
\text{局部相容}\\[1mm]
\text{射线／cusp 解} &
\text{存在，标准模型为 }\mathbb CH^2\\[1mm]
\text{高 }\rho\text{ 端点或曲率爆破端的完整分类} &
\text{现有材料尚未解决}
\end{array}}
\]

因此 nil\(^3\) 情形既不能沿用阿贝尔的全局点态次调和性，也不能被局部排除；正确结构是“符号不定的精确体积方程 + bracket-norm 最大值屏障”。该屏障完全排除圆周情形，而复双曲 cusp 则证明区间／射线上的 nil\(^3\) 负 Einstein 机制真实存在。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 29,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step29_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step29_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the complete conditional chain for the four-dimensional negative-branch Yau Problem 26 argument on the Ishida-LeBrun no-Einstein family. The chain has three layers: (1) TOPOLOGICAL: For above-critical manifolds (sigma = D - A/3 > 0), CGB + Hirzebruch + SW monopole inequality give R >= sigma >= delta^2 Vol/(2pi^2), hence delta >= c sqrt(sigma/A) with no PDE. (2) ANALYTIC: For the critical boundary (sigma = 0), a buffered cutoff flow partial_t g = -2 chi^2(Ric+g) on selected maximal-function good supports produces: H_2 persistence -> S^2Y <= C beta^3/t -> ||aF||_inf <= C beta/t (three-factor Moser) -> J_6 persistence -> ||aE||_inf <= C delta(r^2/t)^{1/3} -> integrable velocity V(T) <= C delta theta^{2/3} r^2 -> metric comparison closes bootstrap. The shifted curvature T = Rm + G, U = aT gives continuation via Wang's theorem. (3) GEOMETRIC DOWNSTREAM: terminal recalibration gives int mathfrak_D <= 119 Q(T) = o(A); exponential pullback on fixed-volume plateau selects centers with vanishing pulled-back defect; Rauch tangent-space noncollapse; harmonic-coordinate compactness; smooth Einstein limit with calibrated Weyl spectrum (-1/6, 1/12, 1/12); Derdzinski contradiction (locally conformally Kahler but |W+|^2 = 1/24 != 2/3). KEY CLAIM: K_0 = Vol^{-1} int |Rm|^2 is uniformly bounded by 9 + O(1/A) + O(delta^2) across the IL family, making the critical product beta = S * H_2^{1/2} = C r^2 K_0^{1/2} a universal constant, hence the gap delta_0 is universal. Check: (a) Is the above-critical algebraic gap correct? (b) Is the bootstrap dependency graph non-circular? (c) Does the volume cancellation in beta hold exactly? (d) Is the Moser time exponent (1+n/2)/p_0 correct for the parabolic iteration? (e) Is the Derdzinski contradiction valid at the calibrated spectrum? (f) Are there any hidden gaps in the conditional chain?

## Integrated Scientific Memo

# 核验结论：该四维负分支链条尚未闭合

## 总判定

现有材料足以确认：

- 上临界拓扑障碍的核心代数成立，但题目摘要中的一个不等号方向写反；
- Sobolev–局部能量中的体积因子确实消去；
- Moser 时间指数 \((1+n/2)/p_0\) 正确；
- 终端 \(119Q(T)\) 重标定和 Derdziński 的模长矛盾成立。

但目前不能确认完整条件链。至少有三个实质性断点：

1. 所写加权 Moser 递推存在半次 cutoff 权重缺口；
2. \(K_0\le 9+O(A^{-1})+O(\delta^2)\) 没有由给定材料证明，且使用的 CGB 系数有误；
3. 退化 cutoff flow 的张量级能量公式和 shifted-curvature 延拓仍是示意性的。

因此，“\(\beta\) 为普适常数，故得到普适 gap \(\delta_0\)”目前不成立。

---

## (a) 上临界代数

令
\[
E=\operatorname{Ric}+g,\qquad
R=\frac1{8\pi^2}\int_M|\operatorname{Ric}^{\circ}|^2\,d\mu .
\]
若 \(\|g^{-1}E\|_{\rm op}\le\delta\)，则在四维
\[
|\operatorname{Ric}^{\circ}|^2=|E^\circ|^2\le |E|^2\le4\delta^2,
\]
所以
\[
R\le \frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g).
\]

另一方面，
\[
I-R=\frac{2A}{3}-\sigma,\qquad I\ge\frac{2A}{3}
\]
推出
\[
R\ge\sigma.
\]
故正确链条是
\[
\boxed{\sigma\le R\le
\frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g),}
\]
而不是任务摘要中的
\[
R\ge\sigma\ge\frac{\delta^2\operatorname{Vol}}{2\pi^2}.
\]

体积上界也可直接闭合。由 \(|s+4|\le4\delta\)，
\[
I\ge \frac{(1-\delta)^2}{6\pi^2}\operatorname{Vol}.
\]
再用 \(I=2A/3-\sigma+R\le2A/3+R\) 及上述 \(R\) 上界，得到
\[
\frac{1-2\delta-2\delta^2}{6\pi^2}\operatorname{Vol}
\le \frac{2A}{3}.
\]
例如 \(\delta\le1/4\) 时，
\[
\operatorname{Vol}\le \frac{32\pi^2}{3}A,
\qquad
\delta^2\ge\frac{3}{16}\frac{\sigma}{A}.
\]
无先验小性时，一个全局正确的写法是
\[
\boxed{\delta\ge
\min\!\left\{\frac14,\frac{\sqrt3}{4}\sqrt{\frac{\sigma}{A}}\right\}.}
\]

所以固定上临界流形确有无需 PDE 的 gap。若要无截断地写成
\(c\sqrt{\sigma/A}\)，还需控制 \(\sigma/A\)，或允许常数依赖具体拓扑。

---

## (b) Bootstrap 是否非循环

预期依赖顺序
\[
H_2\to Y\to\|aF\|_\infty\to J_6
\to\|aE\|_\infty\to V\to \text{metric/Sobolev}
\]
在概念上是三角形的。

但 `step29_simultaneous_support_theorem.md` 所定义的 first-exit 集只提到 B1–B4，而 Step A 已使用
\[
\beta_a(t)=S(t)\|F(t)\|_{L^2}\le4\beta_0.
\]
这并不能仅由曲率点态界 \(C/t\) 或度量比较推出，尤其在 \(t=0\) 附近。

需要把至少
\[
H_2(t)\le4H_2(0),\qquad S(t)\le4S(0)
\]
显式纳入 simultaneous first-exit 条件。如此 Step A 才能改善预设的 \(H_2\) 界，后续步骤才真正单向。

此外，支持构造中还有两项必须修正：

- 弱型估计不能一般假定 doubling constant \(C_D\le2\)；阈值应取 \(c\,C_DK_0\)。
- \(r/5\)-分离并不使 \(B_{2r/3}\) 支持不交；必须使用有界度着色，并保留一个固定体积分数的颜色类。

因此依赖图可修成非循环，但当前写法不完整。

---

## (c) \(\beta\) 的体积消去与 \(K_0\) 主张

在同一支持体积 \(V_\Omega\) 上，
\[
S\le C_{\rm Sob}\frac{r^2}{V_\Omega^{1/2}},
\qquad
H_2(0)\le M V_\Omega,\qquad M=1+K_0,
\]
所以
\[
\boxed{\beta_0=S\,H_2(0)^{1/2}
\le C_{\rm Sob}r^2\sqrt{1+K_0}.}
\]
体积因子严格消去；若 Sobolev 域和能量域不同，则只多一个由
Bishop–Gromov 控制的固定体积比。

若取
\[
r=c(1+K_0)^{-1/4},
\]
则
\[
\beta_0\le C_{\rm Sob}c^2.
\]
因此可以通过维数无关的无量纲因子 \(c\) 令临界吸收参数变小。单就此消去而言，并不需要 \(K_0\) 有统一上界。

但终端固定半径 Einstein germ 需要 \(r\) 不退化，所以仍需 \(K_0\) 的统一上界。

### \(K_0\le9+O(A^{-1})+O(\delta^2)\) 未被证明

给定分解约定
\[
|\operatorname{Rm}|^2
=|W|^2+2|\operatorname{Ric}^{\circ}|^2+\frac{s^2}{6},
\]
CGB 推出的是
\[
\boxed{
\int|\operatorname{Rm}|^2
=32\pi^2\chi(M)+4\int|\operatorname{Ric}^{\circ}|^2,}
\]
不是来源笔记中的系数 \(6\)。

故
\[
K_0
\le\frac{32\pi^2\chi(M)}{\operatorname{Vol}}
+16\delta^2.
\]
若使用 \(\operatorname{Vol}/A\to32\pi^2/9\)，只能得到
\[
K_0=9\,\frac{\chi(M)}{A}+o(1)+O(\delta^2).
\]
要推出数值 \(9+O(A^{-1})\)，还必须证明
\[
\chi(M)=A+O(1).
\]
给定材料中没有该关系；仅有 \(2\chi+3\tau=A-D\) 不够。若能证明较弱的
\(\chi(M)\le CA\)，则足以给出统一 \(K_0\) 上界，但不能得到常数 \(9\)。

此外，A03 的半径有内部矛盾：
\[
r_*=c(A/K_0)^{1/4}
\quad\text{与}\quad
r_*=cK_0^{-1/4}.
\]
因为 \(K_0\) 是平均曲率能量，后者才与其余估计相容。

---

## (d) Moser 时间指数与实际递推

时间指数正确：
\[
\boxed{t^{-(1+n/2)/p_0}}.
\]
这是维数 \(n\) 的标准抛物尺度指数，也等于
\[
\sum_{k\ge0}\frac1{p_k}
=\frac{n+2}{2p_0},
\qquad p_{k+1}=\left(1+\frac2n\right)p_k.
\]

在 \(n=4\)：

- \(p_0=3\)：指数 \(1\)，得到曲率的 \(t^{-1}\)；
- \(p_0=6\)：指数 \(1/2\)，再乘 seed 的 \(t^{1/6}\)，得到 \(t^{-1/3}\)。

Sobolev 幂
\[
S^{n/(2p_0)}
\]
也正确，分别为 \(S^{2/3}\) 和 \(S^{1/3}\)。

### 但所写加权递推不成立

来源定义
\[
H_p=\int a^{p-2}f^p,\qquad
z_p=a^{(p-1)/2}f^{p/2}.
\]
四维抛物 Sobolev 步控制
\[
\int z_p^3
=\int a^{\frac32(p-1)}f^{3p/2}.
\]
而下一指数的能量是
\[
H_{3p/2}
=\int a^{3p/2-2}f^{3p/2}.
\]
前一 integrand 等于后一 integrand 乘 \(a^{1/2}\)。由于 transition 区
\(a\to0\)，前者不能统一控制后者。cutoff 无限平坦也不会提供
\(a^{-1/2}\) 的有界性。

所以 Step 27 的递推式 (4.4) 并未从其定义推出。必须另证：

- cutoff 指数随 \(p\) 演化的加权 Moser 引理；或
- 改用 \(U=aF\)、\(aE\) 的一致能量体系；或
- 重新设计权重，使 Sobolev 输出恰好成为下一层能量。

多项式 \(p^4\) 损失本身是无害的，但不能修复这个半次权重缺口。这是当前分析层最明确的阻断点。

---

## (e) Derdziński 矛盾

给定光滑 Einstein 极限及终端缺陷消失，
\[
s=-4,\qquad |W^+|^2=\frac1{24},
\qquad
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
谱确实无迹，且平方和为 \(1/24\)。

Einstein 条件给出 \(\delta W^+=0\)。Derdziński 定理使
\[
(24|W^+|^2)^{1/3}g
\]
局部 Kähler。此处因 \(|W^+|\) 为常数且 \(24|W^+|^2=1\)，原度量自身局部 Kähler。四维 Kähler 度量满足
\[
\operatorname{Spec}(W^+)
=\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right),
\qquad
|W^+|^2=\frac{s^2}{24}.
\]
当 \(s=-4\) 时，
\[
|W^+|^2=\frac23,
\]
与 \(1/24\) 矛盾。因此该下游矛盾有效。

不应使用“常特征值强迫 \(\nabla W^+=0\)”作为替代证明；特征框架仍可能旋转。可靠证明是上述局部共形 Kähler 加模长冲突。

---

## (f) 其余隐藏缺口

1. **退化流短时存在与延拓。**  
   \(\partial_tg=-2\chi^2(\operatorname{Ric}+g)\) 在 \(\chi=0\) 处退化。说明 \(-2\chi^2g\) 是低阶项并不能解决主部退化。对
   \[
   U=a\!\left(\operatorname{Rm}+\frac{g\owedge g}{2(n-1)}\right)
   \]
   的 Wang 型导数归纳、成组分部积分及 staggered Hölder 仍未展开，因此 continuation 目前是条件假设。

2. **张量级 power-energy 公式。**  
   moving norm、moving volume、Lichnerowicz 反应项、\(\nabla^2a\) 分部积分、Kato 正则化及其多项式 \(p\)-依赖都只有示意推导。

3. **\(J_6\) 与全局 \(Q\) 的同时保持。**  
   必须在同一多支持流、同一终止时刻、同一 bootstrap 中证明；不能仅把各自局部估计并列。

4. **固定尺度 plateau regularity。**  
   终端 \(|\sec|\le K\) 只给 \(C^{1,\alpha}\)/harmonic-coordinate 基础控制。光滑极限还需在更小 buffer 和正时间区间上获得统一曲率导数估计。

5. **pullback 平均所需统一常数。**  
   必须真正得到
   \[
   \operatorname{Vol}(P_i)\ge\alpha A_i,\quad
   \rho\ge\rho_0>0,\quad K\le K_0',\quad
   K\rho^2<\pi^2/4.
   \]
   这些不能依赖 \(i\)。

6. **吸收阈值与固定 germ 尺度。**  
   即使修复 \(K_0\)，\(\beta=O(1)\) 只说明普适有界，不说明低于吸收阈值。可以通过
   \(r=cK_0^{-1/4}\) 取小 \(c\) 来减小 \(\beta\)，但同时 \(\rho\sim r\) 变小。需要显式证明存在一个固定 \(c>0\)，既满足所有吸收和 Gronwall 条件，又保留固定正半径及 Rauch 条件。现有材料没有常数级验证。

7. **终端部分的正确范围。**  
   \[
   \int\mathfrak D\le119Q(T)
   \]
   的算术成立，指数映射平均也可绕过 base injectivity collapse；但它们都依赖上游提供统一 plateau 族和 \(Q(T)/A\to0\)。

---

## 最终核验表

| 问题 | 结论 |
|---|---|
| (a) 上临界 gap | 核心正确，但应为 \(\sigma\le R\le\delta^2\mathrm{Vol}/(2\pi^2)\)；一般写成 \(c\min\{1,\sqrt{\sigma/A}\}\)。 |
| (b) 非循环性 | 可修成三角形；当前 first-exit 集遗漏 \(H_2,S\)。 |
| (c) \(\beta\) 体积消去 | 严格成立；但 \(K_0=9+O(A^{-1})+O(\delta^2)\) 未证且 CGB 系数写错。 |
| (d) Moser 指数 | 时间指数正确；所写加权递推有 \(a^{1/2}\) 缺口。 |
| (e) Derdziński | 通过局部共形 Kähler 与 \(1/24\neq2/3\) 的模长冲突成立。 |
| (f) 完整链 | 尚未闭合；核心缺口是兼容权重的 Moser 定理、张量级能量不等式、退化流延拓及统一固定尺度常数。 |

因此，该方案目前是一条有价值但仍属条件性的四维负分支架构，尚不是 Ishida–LeBrun 全族统一 gap 的完整证明。
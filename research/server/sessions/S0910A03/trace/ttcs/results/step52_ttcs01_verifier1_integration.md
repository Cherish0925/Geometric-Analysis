# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 52,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step52_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step52_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the new Step 52 normalized local-flow start. The scientific question is whether Guoyi Xu's detailed fixed-point proof for the degenerate local Ricci-DeTurck equation remains valid after adding the algebraic metric reaction -2 chi^2 g. Reconstruct the exact changes to Xu's frozen strictly parabolic map, positivity/eigenvalue estimates, high-Sobolev invariant ball, contraction estimate, epsilon-uniform compactness, and DeTurck pullback. Look specifically for hidden derivative loss, epsilon dependence, boundary/interface mismatch, wrong sign, or a failure to recover the exact geometric normalized flow. Also verify that the flat-torus test really falsifies Step 51's homogeneous critical-energy closure. Give a direct mathematical judgment and any exact repairs needed.

## Integrated Scientific Memo

# Step 52 核验结论

## 结论

Step 52 对 Xu 固定系数抛物型映射的修改在分析层面基本正确：

\[
-2\chi^2V
\]

确实只是一个与 \(\varepsilon\) 无关的零阶线性项。它不引入导数损失、不产生 \(\varepsilon^{-1}\)，并且 Xu 的正定性估计、高阶 Sobolev 不变球、压缩估计及 \(\varepsilon\to0\) 紧性均可在缩短依赖于单个初值的时间后保持。

但是，Step 52 的 **DeTurck 回拉是错误的**。一般而言

\[
\varphi^*(\chi^2 g)
=(\chi^2\circ\varphi)\,\varphi^*g,
\]

而不是 \(\chi^2\varphi^*g\)。因此 Xu 的“固定 Eulerian 截断函数”的纯度量映射，回拉后至多给出带运输截断系数的方程，不能直接得到要求的固定截断几何流

\[
\partial_t h=-2\chi^2(\Ric_h+h).
\]

故 Step 52 的 Proposition 3.1 **尚未由其所写证明建立**。要修复，必须加入运输系数作为未知量，或完整采用 Yang 的运输对系统；代数反应本身仍然无害，但 Xu 的 metric-only fixed point 不足以完成最终回拉。

平坦四维环面的检验完全正确，并严格否定 Step 51 所声称的无源齐次临界能量闭合。

---

## 1. 冻结严格抛物映射

令 \(a=\chi^2\)。规范固定后的目标度量方程为

\[
\partial_tg
=a\,g^{-1}*\widetilde\nabla^2g
+D(g,g)+B(g,\widetilde\nabla g)-2ag.
\]

Xu 的正确冻结正则化映射是

\[
\boxed{
\partial_tV
=(a+\varepsilon)U^{-1}*\widetilde\nabla^2V
+D(U,V)+B(U,\widetilde\nabla U)-2aV.
}
\]

在固定点 \(U=V=g_\varepsilon\) 后，令 \(\varepsilon\downarrow0\) 正好恢复上述规范固定方程。选用 \(-2aV\) 而不是 \(-2aU\) 还有两个优点：它直接进入线性方程的零阶系数，并且两次映射之差仅产生 \(-2a(V-\widetilde V)\)。

该修改：

- 不含 \(V\) 的空间导数；
- 不改变主符号；
- 与 \(\varepsilon\) 无关；
- 在 \(\{a=0\}\) 上消失；
- 在 Xu 的有边界版本中，由于 \(\chi\in C_c^\infty(\Omega)\)，在边界领圈中也消失，因此不产生新的边界兼容性条件。

---

## 2. 正定性与特征值估计

相对于 \(\widetilde g\) 对角化 \(V\)，记特征值为 \(\lambda_i\)，并定义

\[
\phi_m=\sum_i\lambda_i^{-m},
\qquad
\psi_m=\sum_i\lambda_i^m .
\]

反应项单独满足

\[
\dot V=-2aV,\qquad \dot V^{-1}=2aV^{-1},
\]

故

\[
(\partial_t\phi_m)_{\rm react}=2ma\phi_m,
\qquad
(\partial_t\psi_m)_{\rm react}=-2ma\psi_m.
\]

Step 52 的符号和系数均正确。下特征值估计所用的 \(\phi_m\) 获得一个不利但有界的 \(2m\|a\|_\infty\phi_m\)；上特征值估计的新增项则有利。Xu 的最大值原理 ODE 因而只需缩短时间，不出现 \(a^{-1}\) 或 \(\varepsilon^{-1}\)。

---

## 3. 高阶 Sobolev 不变球

对固定背景能量

\[
E_m(V)=\sum_{|\alpha|\le m}
\|\widetilde\nabla^\alpha V\|_{L^2(\widetilde g)}^2,
\]

新增贡献为

\[
-4\sum_{|\alpha|\le m}
\int
\left\langle\widetilde\nabla^\alpha V,
\widetilde\nabla^\alpha(aV)\right\rangle d\mu_{\widetilde g}.
\]

Leibniz 展开给出

\[
\left|E_m'(V)\right|_{\rm react}
\le C_m\|a\|_{W^{m,\infty}}E_m(V)
\le C_m\|\chi\|_{C^m}^2E_m(V).
\]

最高阶同阶项实际上是有利的

\[
-4\int a|\widetilde\nabla^mV|^2,
\]

其余项只含至多 \(m\) 阶的 \(V\)。因此：

- 不产生 \(\widetilde\nabla^{m+1}V\)；
- 不与主部耗散竞争；
- Xu 的 (2.22) 只增加 \(CE_m\)；
- Propositions 2.5、2.7 在较短时间上保持成立。

原有主系数处理仍然一致地满足

\[
\frac{|\widetilde\nabla a|^2}{a+\varepsilon}
=
\frac{4\chi^2|\widetilde\nabla\chi|^2}
{\chi^2+\varepsilon}
\le 4|\widetilde\nabla\chi|^2,
\]

所以没有隐藏的 \(\varepsilon\)-依赖。

---

## 4. 压缩估计

若

\[
V=\Phi_\varepsilon^N(U),\qquad
\widetilde V=\Phi_\varepsilon^N(\widetilde U),\qquad
W=V-\widetilde V,
\]

则新增差分项恰为

\[
-2aW.
\]

它不进入由 \(U-\widetilde U\) 驱动的非齐次项。对 Xu 的低阶压缩范数，

\[
\left|
\sum_{|\alpha|\le \widetilde p}
\left\langle
\widetilde\nabla^\alpha W,
\widetilde\nabla^\alpha(-2aW)
\right\rangle
\right|
\le C_a\|W\|_{H^{\widetilde p}}^2.
\]

因此 Xu 的 (2.49) 改为

\[
\frac d{dt}\|W\|_{H^{\widetilde p}}^2
\le (C_1+C_a)\|W\|_{H^{\widetilde p}}^2
+C_2\|U-\widetilde U\|_{H^{\widetilde p}}^2.
\]

由于 \(W(0)=0\)，

\[
\|W\|_{T,\widetilde p}^2
\le C_2Te^{(C_1+C_a)T}
\|U-\widetilde U\|_{T,\widetilde p}^2.
\]

缩短 \(T\) 后仍得到同样的压缩。无新增导数损失或正则化损失。

---

## 5. \(\varepsilon\)-一致紧性及零集界面

反应项不妨碍紧性，但 Step 52 需要补写一个细节：仅凭

- \(\{\chi>0\}\) 内部的严格抛物正则性；
- \(\operatorname{int}\{\chi=0\}\) 上的静止性，

不足以自动得到跨越一般零集界面的光滑性。

正确修复是：在已经取得固定点及低阶双 Lipschitz/Sobolev 控制后，对每个 \(m\) 在**同一个固定时间区间**上重做 Xu 的固定点方程能量估计：

\[
\frac d{dt}E_m(g_\varepsilon)
\le C_m\bigl(1+E_m(g_\varepsilon)\bigr),
\]

其中 \(C_m\) 可依赖于光滑初值、背景度量和 \(\chi\)，但不依赖于 \(\varepsilon\)。方程还给出

\[
\|\partial_tg_\varepsilon\|_{H^{m-2}}\le C_m.
\]

逐阶取对角子列即可在全域得到 \(C^\infty\) 极限，包括 \(\partial\{\chi>0\}\) 上的点。这正是应该替代单纯“两区域内部正则性”论述的全局 Sobolev 论证。

在闭流形上可直接去掉边界，使用包含低阶项的全局 Sobolev 不等式；这不会改变上述结构。

---

## 6. 决定性问题：DeTurck 回拉改变截断函数

设规范固定度量满足

\[
\partial_t\widehat g
=-2a(\Ric_{\widehat g}+\widehat g)
+\mathcal L_{aW}\widehat g,
\qquad a=\chi^2,
\]

并采用标准 DeTurck ODE

\[
\partial_t\varphi=-(aW)\circ\varphi.
\]

令 \(h=\varphi^*\widehat g\)，则

\[
\begin{aligned}
\partial_t h
&=\varphi^*
\left(\partial_t\widehat g+\mathcal L_{-aW}\widehat g\right)\\
&=-2\varphi^*\!\left(a(\Ric_{\widehat g}+\widehat g)\right)\\
&=\boxed{-2(a\circ\varphi)(\Ric_h+h)}.
\end{aligned}
\]

Step 52 使用的恒等式

\[
\varphi^*(\chi^2\widehat g)
=\chi^2\varphi^*\widehat g
\]

一般是假的。两个 \(\chi^2\)-乘自然张量“变换类型相同”，只能说明它们都获得同一个复合因子 \(\chi^2\circ\varphi\)，不能把该因子变回固定的 \(\chi^2\)。

若将 Xu 文本中的

\[
\partial_t\varphi_t(p)=-a(p)W(\varphi_t(p),t)
\]

按字面理解，其 Eulerian 生成元为
\(- (a\circ\varphi^{-1})W\)，甚至不能完全抵消 \(\mathcal L_{aW}\widehat g\)。因此无论采用标准解释还是字面解释，Step 52 的一行回拉都不足以得到固定截断方程。

### 精确修复形式

引入运输系数 \(\widehat a\)，求解耦合系统

\[
\begin{cases}
\partial_t\widehat g
=-2\widehat a(\Ric_{\widehat g}+\widehat g)
+\mathcal L_{\widehat aW}\widehat g,\\[1mm]
\partial_t\widehat a
=\widehat a\,W(\widehat a),\\
\widehat a(0)=a,
\end{cases}
\]

并令

\[
\partial_t\varphi=-(\widehat aW)\circ\varphi.
\]

则

\[
\frac d{dt}(\widehat a\circ\varphi)=0,
\qquad
\widehat a\circ\varphi=a,
\]

从而

\[
\partial_t(\varphi^*\widehat g)
=-2a\bigl(\Ric_{\varphi^*\widehat g}+\varphi^*\widehat g\bigr).
\]

但此时不再是 Xu 的 metric-only 映射。标量方程含 \(W(\widehat a)\)，差分方程也出现

\[
(\widehat a-\widetilde{\widehat a})\,\widetilde V
\]

等耦合项；必须另证运输方程与度量方程的联合不变球和压缩/光滑-tame 估计。Step 50 中的 Yang 运输对框架正是可能的修复方向，但现有 Step 52 没有完成这一点。

因此可严格确认的是：

> \(-2\chi^2V\) 对 Xu 的规范固定纯度量方程是完全可容许的零阶扰动；但由此得到固定截断的几何归一化流仍缺少运输系数的耦合证明。

只有在 \(a\) 为常数，或演化中偶然始终满足 \(W(a)=0\) 时，原回拉才直接成立。

---

## 7. 平坦环面检验

在平坦

\[
T^4=(\mathbb R/2\pi\mathbb Z)^4
\]

上取

\[
\chi(x_1)=\frac{1+\cos x_1}{2},\qquad a=\chi^2.
\]

初始时 \(\Ric=0\)，故

\[
\dot g=-2ag,\qquad
\dot{\Rm}=g\owedge\Hess a.
\]

直接计算

\[
a''(x_1)=-\frac{\cos x_1+\cos2x_1}{2}.
\]

\(\Hess a\) 只有 \(11\) 分量，且在四维

\[
|g\owedge\Hess a|^2=12(a'')^2.
\]

又有

\[
\int_0^{2\pi}(a'')^2\,dx_1=\frac{\pi}{2},
\]

所以

\[
\begin{aligned}
E(t)
&=\int_{T^4}|\Rm(g(t))|^2\,d\mu_{g(t)}\\
&=12\cdot\frac{\pi}{2}\cdot(2\pi)^3t^2+O(t^3)\\
&=\boxed{48\pi^4t^2+O(t^3)}.
\end{aligned}
\]

脚本和 JSON 的系数均正确。于是

\[
\frac{E'(t)}{E(t)}=\frac2t+O(1).
\]

因此不存在近 \(t=0\) 的有界 \(C\) 使

\[
E'(t)\le CE(t).
\]

更直接地，若该齐次不等式成立且 \(E(0)=0\)，Gronwall 将推出 \(E\equiv0\)，与上述展开矛盾。

临界指数处的常数同伦反应消去

\[
(2p-n)\int a|\Rm|^p=0,\qquad p=n/2,
\]

本身仍然正确；错误在于把空间强迫

\[
g\owedge\nabla^2a
\]

也视作已消除。一次分部积分后吸收留下的是

\[
C\int \frac{|da|^2}{a}F^{p-2},
\]

而不是 \(C\int F^p\)。在 \(n=4,p=2\) 时这是实际的零次/体积强迫。再次分部积分则重新出现

\[
\Delta_g a
=g^{ij}\bigl(\partial_i\partial_j a-\Gamma(g)^k{}_{ij}\partial_ka\bigr),
\]

其控制不能从单纯的度量双 Lipschitz 比较得到。

需要精确区分：该例否定无源齐次闭合 \(E'\le CE\)，但不否定带加性体积项的粗估计 \(E'\le CE+C_0\)；后者与 \(E(t)=O(t^2)\) 相容，却不能支持 Step 51 所声称的齐次临界能量论证。

---

## 最终判定

1. **冻结映射、正定性、Sobolev 球、压缩及 \(\varepsilon\)-一致估计：通过。**
2. **界面光滑性：可修复；须明确使用同一时间区间上的全阶全局 Sobolev 估计。**
3. **边界兼容性：Xu 的紧支撑设置中无新增问题；闭流形版本更直接。**
4. **DeTurck 回拉：不通过。** 固定 Eulerian 截断函数回拉为 \(a\circ\varphi\)，Step 52 的 Proposition 3.1 尚未证明。
5. **所需精确修复：** 建立运输系数—度量耦合系统的固定点或 tame inverse；仅加入代数项 \(-2aV\) 不够。
6. **平坦环面检验：通过。** 系数 \(48\pi^4\) 正确，并严格推翻 Step 51 的齐次临界能量闭合。
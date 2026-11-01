# TTCS Independent Branch Record

```json
{
  "step_id": 15,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step15_cutoff_smoothing_architecture.md",
    "Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md",
    "Sessions/S0910A01/workspace/notes/step14_smoothing_vs_reduction_route.md",
    "Sessions/S0910A01/workspace/notes/step11_chart_accessibility_and_energy.md"
  ]
}
```

## Task

Verify the cutoff-smoothing accessibility architecture for the negative branch of Yau Problem 26 in dimension 4. The architecture claims: (A) For a sequence of closed 4-manifolds (M_i, g_i) with Ric_{g_i}+g_i -> 0 in C^0 and no Einstein metric, a normalized cutoff flow d_t g = -2 chi^2(Ric+g) on the closed manifold produces bounded curvature on a definite volume proportion while preserving global near-Einstein. (B) Calibration recovery: the LeBrun mixed SW estimate and Chern-Gauss-Bonnet applied to the smoothed metric g_i(t) give the SAME near-saturation profile because topology and near-Einstein are preserved. (C) The Li all-centers condition is satisfied at all covering centers inside the good set because the comparable-ball Bishop-Gromov ratio V_{-1}(13r*/2)/V_{-1}(r*) is bounded (~1785 in 4D), making r*^4 * C_BG * K_0 small for small r*, regardless of collapse. Verify each component and identify any gaps or errors: (1) Is the calibration recovery correct? Are there any subtleties about Seiberg-Witten invariants changing under the flow? (2) Is the BG transfer chain correct? The maximal function at p gives fint_{B_{4r*}(p)} |Rm|^2 <= K_0; for y within 5r*/2 of p, B_{r*}(y) subset B_{4r*}(p), so int_{B_{r*}(y)} <= K_0 Vol(B_{4r*}(p)); BG gives Vol(B_{4r*}(p))/Vol(B_{r*}(y)) <= C_BG. (3) Does the cutoff flow actually have short-time existence (degenerate parabolicity where chi=0)? (4) Does bounded curvature + collapse give CFG chart accessibility for the forbidden-germ argument? (5) Is the volume contradiction valid: definite proportion of accessible points vs vanishing proportion from calibrated defect?

## Output

# 科学核验备忘：四维 cutoff–smoothing accessibility 架构

## 总体结论

- **(C) 可比球 Bishop–Gromov 转移是正确的。** 它确实消除了塌缩体积因子，并允许在固定的小尺度 \(r_*>0\) 上满足 Li 的初始无量纲 \(L^2\) 条件。文中半径参数 \(\rho,r_*\) 需要统一。
- **(B) 拓扑重新校准是正确机制。** 只要平滑后闭度量在全流形上仍满足 \(\|\operatorname{Ric}+g\|_\infty=o(1)\)，LeBrun–SW 与 Chern–Gauss–Bonnet 可以直接对新度量重做；不需要沿流输运 \(W^+\)。但必须重做完整的等号余项，而不只是文中显示的一个标量平方项。
- **(A) 尚未由现有材料证明。** 每个固定 \(i\) 的局部 Ricci 流存在性可由 Yang 型理论支持，但统一时间 \(T\asymp r_*^2\)、过渡环带中的全局 Einstein 误差传播，以及精确的局部 Li 能量闭合都仍缺少证明。正规化近似本身也不能替代退化流的统一估计。
- 有界全曲率是进入 CFG 理论的正确输入，但“局部正规覆盖自动无塌缩，从而所有平台点均可访问”在笔记中没有形成带统一常数的定理。
- 最后的体积矛盾在上述分析与几何输入成立后是逻辑完备的。

---

## 1. 平滑后重新校准

令
\[
h_i=g_i(t_0),\qquad
\eta_i=\|\operatorname{Ric}_{h_i}+h_i\|_\infty\longrightarrow0,
\qquad V_i=\operatorname{Vol}(M_i,h_i).
\]
设
\[
I_i=\frac1{4\pi^2}\int\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu,
\qquad
J_i=\frac1{4\pi^2}\int\frac{|\mathring{\operatorname{Ric}}|^2}{2}\,d\mu.
\]
Chern–Gauss–Bonnet 与签名公式对任意光滑度量给出
\[
I_i-J_i=2\chi(M_i)+3\tau(M_i)=A_i-k_i.
\]
由 \(\operatorname{Ric}_{h_i}=-h_i+O(\eta_i)\)，
\[
s_{h_i}=-4+O(\eta_i),\qquad J_i\le C\eta_i^2V_i.
\]
同时，标量曲率项给出
\[
I_i\ge cV_i
\]
（\(i\) 足够大时 \(s^2\ge 8\)，例如）。因而
\[
cV_i\le A_i-k_i+C\eta_i^2V_i,
\]
吸收最后一项后得到 \(V_i=O(A_i)\)，继而
\[
J_i=o(A_i),\qquad
I_i=A_i-k_i+J_i=\frac23A_i+o(A_i).
\]

### SW 类与度量变化

对每个度量分别选取吹起基本类
\[
a_\varepsilon=c_1(X_i)+\sum_{j=1}^{k_i}\varepsilon_jE_j .
\]
符号平均给出
\[
2^{-k_i}\sum_{\varepsilon}|a_\varepsilon^+|^2
=
|c_1(X_i)^+|^2+\sum_j|E_j^+|^2
\ge |c_1(X_i)^+|^2
\ge c_1^2(X_i)=A_i.
\]
所以某个符号选择满足 \((a_i^+)^2\ge A_i\)。这里 \(a_i\) 可以随 \(h_i\) 攻变；无需沿流固定同一个符号选择。

在当前 \(A_i\to\infty\) 的曲面序列中，BMY 给出
\[
A_i\le9\chi_{\mathrm{hol}}(X_i)\le9(1+p_g(X_i)),
\]
故 \(p_g(X_i)\to\infty\)，而
\[
b^+(X_i)=1+2p_g(X_i)>1
\]
对尾部序列成立。吹起不改变 \(b^+\)。因此尾部序列的 SW 基本类不受度量路径影响，不出现 \(b^+=1\) 的 chamber 现象。流只改变度量，不改变光滑结构、交叉形式、取向或 Spin\(^c\) 结构。

LeBrun 不等式给出
\[
D_{a,i}:=I_i-\frac23(a_i^+)^2\ge0,
\]
并且
\[
D_{a,i}
\le \frac{A_i}{3}-k_i+J_i
\le \left|k_i-\frac{A_i}{3}\right|+J_i=o(A_i).
\]
所以原有等号分析可以完全重做。

### 必须保留完整余项

文中仅显示
\[
\int (s+8\sqrt6\,|W^+|)^2=o(A_i).
\]
它只确定
\[
s\to-4,\qquad |W^+|^2\to\frac1{24}
\]
的平均关系，**单独并不能确定**
\[
\operatorname{Spec}(W^+)\to
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
要得到两个相等特征值，还必须重新引入 Step 8/11 中的特征值余项，例如
\[
\mathcal G=f^2-(a_-)^2
\]
或等价的投影张量余项，并证明其积分也是 \(o(A_i)\)。只要这些余项本来就是由 \(D_{a,i}\) 控制的非零平方和，重新校准便成立。

上述标量余项还恢复体积常数。由 \(s=-4+o(1)\) 和
\[
|W^+|=\frac1{2\sqrt6}+o_{L^2}(1),
\]
可得
\[
I_i=\frac{3}{16\pi^2}V_i+o(A_i).
\]
结合 \(I_i=\frac23A_i+o(A_i)\)，
\[
\frac{V_i}{A_i}\longrightarrow\frac{32}{9}\pi^2.
\]
因此重新校准确实是拓扑与终端 near-Einstein 性质的结果，不依赖 \(W^+\) 沿时间的比较。

---

## 2. Bishop–Gromov 转移链

若
\[
d(p,y)\le\frac52r_*,
\]
则
\[
B_{r_*}(y)\subset B_{\frac72r_*}(p)\subset B_{4r_*}(p).
\]
由最大函数条件，
\[
\int_{B_{r_*}(y)}|\operatorname{Rm}|^2
\le K_0\,\operatorname{Vol}B_{4r_*}(p).
\]
反过来，
\[
B_{4r_*}(p)\subset B_{\frac{13}{2}r_*}(y).
\]
在 \(\operatorname{Ric}\ge-3g\) 下，
\[
\frac{\operatorname{Vol}B_{4r_*}(p)}
     {\operatorname{Vol}B_{r_*}(y)}
\le
\frac{\operatorname{Vol}B_{\frac{13}{2}r_*}(y)}
     {\operatorname{Vol}B_{r_*}(y)}
\le
\frac{V_{-1}(\frac{13}{2}r_*)}{V_{-1}(r_*)}.
\]
故
\[
r_*^4\fint_{B_{r_*}(y)}|\operatorname{Rm}|^2
\le
r_*^4K_0
\frac{V_{-1}(\frac{13}{2}r_*)}{V_{-1}(r_*)}.
\]

当 \(r_*\downarrow0\) 时，
\[
\frac{V_{-1}(\frac{13}{2}r_*)}{V_{-1}(r_*)}
\longrightarrow
\left(\frac{13}{2}\right)^4
=1785.0625.
\]
在正的 \(r_*\) 上该比值略大于 \(1785\)，所以“约 \(1785\)”只能理解为小尺度渐近值。可先固定很小的 \(r_0\)，令该比值在 \(0<r\le r_0\) 上由某个常数 \(C_0\) 控制，再取
\[
r_*\le
\min\left\{r_0,\left(\frac{\varepsilon_{\mathrm{Li}}}
{2C_0K_0}\right)^{1/4}\right\}.
\]
此处完全不需要球体积的绝对下界，塌缩因子确实消失。

相同消去也出现在 Sobolev–能量乘积：
\[
C_S(B_{r_*})\|\operatorname{Rm}\|_{L^2(B_{r_*})}
\le
C r_*^2
\left(\fint_{B_{r_*}}|\operatorname{Rm}|^2\right)^{1/2}.
\]
因此 (C) 的核心计算成立。

### 半径记号需要统一

Section 2.4 的具体计算只直接控制 \(B_{r_*}(p)\) 内目标点及其覆盖中心，而 Proposition A 写成了整个 \(B_{\rho/4}(p)\) 上的 all-centres 条件。一个一致选择是
\[
\rho=8r_*,
\]
使
\[
B_{\rho/8}(p)=B_{r_*}(p),\qquad
B_{\rho/4}(p)=B_{2r_*}(p),\qquad
B_{\rho/2}(p)=B_{4r_*}(p).
\]
若局部延拓使用 \(B_{2r_*}(p)\) 内所有中心，还会出现稍大的可比球常数；最大函数在 \(p\) 控制所有半径，所以仍可处理，但常数不再恰好是 \(13/2\) 那一个。

---

## 3. cutoff 流存在性与全局 Einstein 误差

令 \(a=\chi^2\)。方程
\[
\partial_tg=-2a(\operatorname{Ric}+g)
\]
在 \(a=0\) 处不是一致抛物型，故不能直接套用标准 DeTurck 短时理论。

### 每个固定 \(i\)

Yang 型 local Ricci flow 理论确实为
\[
\partial_tg=-2\chi^2\operatorname{Ric}
\]
提供退化局部流构造；闭流形上的初始光滑度量具有有限的全曲率上界，正规化的低阶项 \(-2\chi^2g\) 不改变主要结构。因此，每个固定 \(i\) 的某个正时间解有可靠文献依据。

但这并不产生与 \(i\) 无关的时间
\[
T=c\,r_*^2.
\]
普通存在时间可能依赖 \(\sup|\operatorname{Rm}_{g_i}|\)、cutoff 的高阶导数以及过渡环带的几何，而这些量在序列中没有统一控制。统一的 \(T\) 正是局部 \(L^2\) 能量延拓所需证明的一部分。

用
\[
a_\varepsilon=\chi^2+\varepsilon^2
\]
正规化可得到一致抛物方程，但令 \(\varepsilon\to0\) 需要与 \(\varepsilon\) 无关的估计。文中的“外部只以 \(O(\varepsilon^2\delta_i)\) 速度移动”仅在已经知道 \(E(t)=O(\delta_i)\) 时成立，不能独立推出该估计。

还有一个几何细节：仅从 Ricci 下界不能自动构造
\[
|\nabla^2\chi_i|\le C\rho^{-2}
\]
的统一光滑 cutoff。统一一阶 Lipschitz 控制较容易；二阶控制通常需要更多局部几何。A03 的积分恒等式通过分部积分消除了 \(\nabla^2a\)，这有助于能量法，但基本存在理论和曲率方程仍需与所选 cutoff 正确衔接。

### “同次性”不足以推出全局 \(C^0\) 传播

A03 验证的公式
\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)
\]
是重要的，其中
\[
\mathcal C_a(E)
=(da)*\nabla E+(\nabla^2a)*E+\cdots
\]
每项均含 \(E\) 或其导数。因此 \(E\equiv0\) 时流静止，这是正确的。

但从 \(\|E(0)\|_\infty\le\delta_i\) 不能仅凭同次性得到
\[
\|E(t)\|_\infty\le C\delta_i.
\]
过渡环带中存在 \(da*\nabla E\)，而初始条件没有给出 \(\nabla E\) 控制。Step 15 中
\[
O(|d\chi|^2\delta_i^2t)
\]
的环带曲率变化估计没有推导依据。实际上
\[
|\partial_tg|=2a|E|,
\]
而
\[
\partial_t\operatorname{Rm}
\sim\nabla^2(aE)+\operatorname{Rm}*aE
\]
包含
\[
da*\nabla E,\qquad \nabla^2a*E.
\]
它们既不是自动的 \(O(\delta_i^2)\)，也不由初始 \(C^0\) 误差控制。

Li Corollary 3.5 在 \(\chi=1\) 的内部平台可给出
\[
|E(x,t)|\le
C\delta_i\left(\frac{r_*^2}{t}\right)^{2/3},
\]
但它不处理过渡环带。开放的 \(\chi=0\) 区域确实完全冻结；在 \(\{\chi=0\}\) 与 \(\{\chi>0\}\) 的接口处，曲率仍可能受空间二阶导数影响。

因此，当前最主要的分析空缺是：

\[
\boxed{
\text{统一时间的局部 cutoff 曲率能量闭合}
\;+\;
\text{过渡环带上的全局 }E\text{ 传播}.
}
\]

A03 的积分型 \(E\)-能量公式说明该问题具有可行的乘法结构，但尚未形成 \(L^\infty\) 结论。

---

## 4. 有界曲率、塌缩与 CFG 可访问性

若在一个带缓冲的球上已有
\[
|\operatorname{Rm}|\le\Lambda,
\]
并且某个正规覆盖上的单位尺度体积有统一下界，则 Cheeger–Gromov–Taylor 与 harmonic-coordinate 理论确实给出统一注入半径和 harmonic radius。这个部分没有问题。

困难在于从“基球上有界全曲率”直接跳到“局部正规覆盖无塌缩”。CFG 理论通常先给出 N-structure、局部 infranil 纤维和正则分层；要得到 Step 11 所定义的 \((h,v)\)-chart accessibility，还要形成如下定量陈述：

> 在 \(|\sec|\le\Lambda\) 的固定缓冲球内，存在仅依赖于维数、\(\Lambda\) 和缓冲尺度的 \(h,v>0\)，并在一个具有确定体积比例的内部子集上存在正规覆盖，使提升球体积至少为 \(vh^4\)，且 harmonic radius 至少为 \(ch\)。

笔记没有给出这一精确 CFG 定理，也没有说明奇异纤维、可收缩短轨道与正则 N-structure 部分的体积如何分配。Naber–Zhang Proposition 6.4 需要 residual dimension 和 maximal fibered nilpotency rank；这些条件在 Section 6.2 中没有验证。

若 Proposition A 在正时间还给出内部 Shi 导数估计，则应用 CFG 会更标准，但正规覆盖无塌缩及确定体积比例仍需明确的局部覆盖定理。单纯的指数映射图不足以替代正规覆盖，因为 Step 11 的缺陷平均输运依赖 deck 作用和正规覆盖的重数控制。

所以“有界全曲率是正确入口”成立，而“平台自动全部成为可访问点”尚未由提供的文本推出。

---

## 5. 体积矛盾

在半径统一后，初始 packing 给出
\[
\sum_j\operatorname{Vol}_{g_i}
B_{\rho/8}(p_j)
\ge c\sum_j\operatorname{Vol}_{g_i}B_\rho(p_j)
\ge c'\operatorname{Vol}(M_i,g_i),
\]
其中第一步也是同中心 Bishop–Gromov 比较。取更小的内部球可为 CFG 图表保留固定缓冲。

若平台上的 Corollary 3.5 估计成立，则这些内部集合在 \(t_0\) 时的体积与初始体积相差 \(1+o(1)\)。若全局终端 near-Einstein 估计也成立，前述拓扑重新校准给出
\[
\operatorname{Vol}(M_i,g_i(t_0))
\sim \frac{32}{9}\pi^2A_i
\sim\operatorname{Vol}(M_i,g_i).
\]
因此平台仍占 \(g_i(t_0)\) 总体积的固定比例。

若 CFG 层再提供统一的 \(h,v\)，则
\[
\frac{\operatorname{Vol}\mathcal A_i(h,v)}
{\operatorname{Vol}(M_i,g_i(t_0))}\ge c_0>0.
\]
另一方面，完整校准缺陷满足
\[
\fint_{M_i}F_{g_i(t_0)}\,d\mu_{t_0}\to0,
\]
全局 near-Einstein 给出统一 Ricci 下界，Step 11 的最大函数选点、正规覆盖平均输运和 Derdziński forbidden-germ 论证于是给出
\[
\frac{\operatorname{Vol}\mathcal A_i(h,v)}
{\operatorname{Vol}(M_i,g_i(t_0))}\to0.
\]
两式确实矛盾。

因此最后的体积论证本身成立；其前提依赖三个尚未闭合的对象：

1. 固定时间的局部 cutoff–Li 曲率能量估计；
2. 过渡环带上的全局 Einstein 误差估计；
3. 从平台有界全曲率到固定 \(h,v\) 正规覆盖可访问集的定量 CFG 结果。

这三个对象中，第一个与第二个是当前架构的主要分析内容；第三个是独立的塌缩几何内容。
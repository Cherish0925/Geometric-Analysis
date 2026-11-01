# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 26,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step26_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step26_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 26 correction to the buffered selected-support cutoff-flow route for Yau Problem 26. Focus on: (1) whether the Step 25 plateau-only metric-displacement argument is indeed insufficient and whether support-wide integral control of ||aE||_infty is the right metric-comparability target; (2) whether the fixed-p defect energy J_p=int eta^2 a^(p-2)|E|^p, especially p=6, has the claimed weights, Hessian/cutoff remainders, curvature potential F z_p^2, and initial bound from pointwise Ricci pinching without curvature high integrability; (3) whether the proposed p=6 positive-time weighted velocity estimate ||aE||_infty <= C delta (r^2/t)^(1/3) is a plausible next Moser target or hides a Hardy/degenerate-parabolic obstruction; (4) whether the reading of Yang local Ricci flow source correctly handles DeTurck transported coefficient and shows that short-time existence is only a starting point while uniform continuation to theta r^2 requires weighted curvature/velocity estimates; (5) identify any exact missing hypotheses or wrong weights. Do not decide the overall Yau problem; give a scientific verification memo for the analytic route.

## Integrated Scientific Memo

# Step 26 分析路线核验备忘

## 结论

Step 26 对 Step 25 的修正是必要且正确的：

\[
V(t):=\int_0^t\|aE(s)\|_{L^\infty(\operatorname{supp}\chi,g(s))}\,ds,
\qquad a=\chi^2,\quad E=\operatorname{Ric}+g,
\]

而不是仅控制平台区 \(\{a=1\}\) 上的 \(E\)，才是传递整个活动支撑上度量比较、Sobolev 常数、体积元及 cutoff 梯度界的正确目标。

固定指数能量

\[
J_p=\int \eta^2a^{p-2}|E|^p
\]

的权重账本基本正确。特别是 \(p=6\) 时，

\[
J_6=\int\eta^2\chi^8|E|^6
\]

与 Yang 附录 A 的四维加权 Moser 起始权重
\(\chi^{2p_0-n}\) 在 \(p_0=6,n=4\) 时完全吻合。因此

\[
\|aE(t)\|_\infty
\lesssim \delta\left(\frac{r^2}{t}\right)^{1/3}
\]

并非只有量纲依据；它是 Yang 型退化局部热流估计的自然专门化。没有发现必然的 Hardy 障碍。尚未完成的关键环节是：

1. 将缺陷张量方程严格化为 Yang 所需的标量/Kato 不等式；
2. 证明并输入正时间的加权 \(L^3\) 曲率势界；
3. 写出归一化局部流及 Wang 延拓论证的逐项适配。

---

## 1. 度量比较：Step 25 的平台论证确实不足

对任一固定非零切向量 \(v\)，

\[
\frac d{dt}\log g_t(v,v)
=-2a\,\frac{E_t(v,v)}{g_t(v,v)},
\]

故

\[
\left|\frac d{dt}\log g_t(v,v)\right|
\le 2|aE|_{g(t)}.
\]

于是

\[
e^{-2V(t)}g_0\le g(t)\le e^{2V(t)}g_0.
\]

这是一条逐点、全活动支撑的结论。平台区上的曲率或缺陷控制无法约束过渡带：完全可能有

\[
a(x)\ll1,\qquad |E(x,t)|\sim a(x)^{-1},
\]

使 \(a|E|\sim1\)。光滑性并不提供可用于 first-exit 的统一定量过渡估计。

因此，为了在 \(\operatorname{supp}\chi\) 上传递：

- 当前 Sobolev 不等式；
- \(|d\chi|_{g(t)}\lesssim r^{-1}\)；
- 体积和 \(L^2\) 范数比较；
- \(\beta_a(t)=A(t)^2\|F(t)\|_{L^2(\operatorname{supp}\chi)}\) 的小性，

所需目标确为

\[
\boxed{\int_0^{\theta r^2}
\|aE(t)\|_{L^\infty(\operatorname{supp}\chi)}\,dt
\le\varepsilon_{\rm met}.}
\]

在 \(\{a=0\}\) 上流静止，故无需扩大到活动支撑之外。

---

## 2. 固定 \(p\) 缺陷能量的权重核验

设

\[
J_p=\int\eta^2a^{p-2}|E|^p,
\]

\[
Z_p=\int\eta^2a^{p-1}|E|^{p-2}|\nabla E|^2,
\qquad
z_p=\eta a^{(p-1)/2}|E|^{p/2}.
\]

以 \(\eta^2a^{p-2}|E|^{p-2}E\) 测试

\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)
\]

产生下列正确权重。

### 主耗散

方程中的 \(a\) 与测试权重 \(a^{p-2}\) 相乘，故耗散为

\[
Z_p=\int\eta^2a^{p-1}|E|^{p-2}|\nabla E|^2.
\]

### cutoff 与 Hessian-\(a\) 余项

主项分部积分、直接的 \((da)*\nabla E\) 项以及 Hessian-\(a\) 项分部积分后，典型交叉项为

\[
a^{p-2}|da|\,|E|^{p-1}|\nabla E|.
\]

Young 不等式给出

\[
\varepsilon a^{p-1}|E|^{p-2}|\nabla E|^2
+C_{\varepsilon,p}a^{p-3}|da|^2|E|^p.
\]

因为 \(a=\chi^2\)，

\[
|da|^2=4a|d\chi|^2,
\]

故

\[
a^{p-3}|da|^2|E|^p
=4|d\chi|^2a^{p-2}|E|^p
\le Cr^{-2}a^{p-2}|E|^p.
\]

这说明并未留下 \(a^{-1}\) 型 Hardy 势。

这里必须保留严格的缓冲假设

\[
\operatorname{supp}d\eta\subset\{a=0\}^{\circ},
\]

而不仅是“\(\eta=1\) 于平台”。该假设使分部积分中所有 \(d\eta\) 项因同时带有 \(a\) 或 \(da\) 而消失。

### 曲率势

Lichnerowicz 反应、移动范数及移动体积元可统一估计为

\[
C_p\int\eta^2a^{p-1}F|E|^p,
\qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

而

\[
\eta^2a^{p-1}F|E|^p=Fz_p^2.
\]

此外，

\[
\|\nabla z_p\|_2^2
\le C_pZ_p+C_pr^{-2}J_p,
\]

且

\[
\|z_p\|_2^2
=\int\eta^2a^{p-1}|E|^p\le J_p.
\]

因此四维当前度量下的相对 Sobolev 不等式给出

\[
\int Fz_p^2
\le C_pA(t)^2\|F\|_2\,
   (Z_p+r^{-2}J_p)
=C_p\beta_a(t)(Z_p+r^{-2}J_p).
\]

若

\[
C_p\beta_a(t)<\frac{c_p}{2},
\]

则

\[
J_p'+c_p'Z_p\le C_pr^{-2}J_p,
\qquad
J_p(t)\le e^{C_pt/r^2}J_p(0).
\]

因此 Step 26 的 \(a\)-幂次、势权重和余项权重均正确。

---

## 3. 初值究竟需要什么

所需假设不是一般意义上的任意 Ricci 双边夹逼，而是当前负 Einstein 分支中的定量缺陷小性：

\[
\boxed{\|E(0)\|_{L^\infty}
=\|\operatorname{Ric}_{g_0}+g_0\|_{L^\infty}
\le C\delta.}
\]

于是

\[
J_p(0)\le C\delta^p
\operatorname{Vol}(\Omega_\eta,g_0),
\]

无需初始超临界 Riemann 曲率积分界。

但必须区分：

- \(J_p(0)\) 只使用点态 Ricci 缺陷小性；
- 演化中的势吸收仍使用局部临界曲率小性
  \(\beta_a=A^2\|F\|_{L^2}\ll1\)。

所以“无需高次曲率可积性”正确；“完全无需曲率积分控制”则不正确。

另外，“缩小 \(r\)”本身不自动使 \(\beta_a\) 小：在曲率集中点，四维 \(L^2\) 能量是尺度临界的。小性必须来自已选定的 good support/maximal-function 条件，再结合常数部分贡献 \(A^2\sqrt{\operatorname{Vol}}\sim r^2\)。

---

## 4. \(p=6\) 目标与 Yang Moser 结构的匹配

Yang 附录 A 的退化局部热流迭代，其时空输入权重为

\[
\chi^{2p_0-n}f^{p_0}.
\]

取

\[
n=4,\qquad p_0=6,\qquad f=|E|,
\]

得到

\[
\chi^{2p_0-n}=\chi^8=a^4,
\]

恰是 \(J_6\) 的权重。其输出为 \(\chi^2f=a|E|\)。

势函数条件在 \(q=6\) 时为

\[
\left(\int\chi^{q-n}F^{q/2}\right)^{2/q}
=
\left(\int\chi^2F^3\right)^{1/3}
\le \mu t^{-1/3}.
\]

若曲率链已证明

\[
S^2Y(t)
=S^2\int\chi^2F^3
\le \frac{C\beta^3}{t},
\qquad S=A^2,
\]

则

\[
\mu\lesssim \beta S^{-2/3},
\qquad
\mu S^{2/3}\lesssim\beta,
\]

正好落在 Yang 的临界势控制形式中。

由 Yang 型估计及 \(J_6(s)\le C\delta^6V\) 可得

\[
\|aE(t)\|_\infty
\lesssim
\delta\,S^{1/3}V^{1/6}t^{-1/3}.
\]

若同一支撑体积 \(V\) 与 Sobolev 系数满足

\[
S\lesssim r^2V^{-1/2},
\]

则体积消去：

\[
S^{1/3}V^{1/6}\lesssim r^{2/3},
\]

从而

\[
\boxed{
\|aE(t)\|_\infty
\le C\delta r^{2/3}t^{-1/3}
=C\delta(r^2/t)^{1/3}.}
\]

时间积分为

\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le \frac32C\delta\,\theta^{2/3}r^2.
\]

更一般地，固定 \(p>2\) 给出 \(t^{-2/p}\)，在零时刻可积。

### Hardy/退化抛物障碍的判定

没有发现不可克服的 Hardy 障碍。关键原因是每次 cutoff 微分均满足

\[
a^{q-3}|da|^2
=4a^{q-2}|d\chi|^2,
\]

余项始终回到当前加权能量，而不会生成 \(\chi^{-2}\) 势。此前的 Hardy 失败针对的是丢弃 cutoff 权重后进行的非加权 Nash/Moser 尝试，不适用于 Yang 的加权框架。

不过上述结论仍需两个实质性补件：

1. **张量到标量的 Kato 归约。**  
   必须由精确 \(E\) 方程推出 \(f=|E|\) 满足 Yang 型不等式，其中 \((da)*\nabla E\) 对应允许的一阶项，而 Hessian-\(a\) 项经处理后对应
   \(C(|d\chi|^2-\chi\Delta\chi)f\) 或等价弱形式。固定 \(J_6\) 能量本身并不自动给出 \(L^\infty\)。

2. **曲率势的正时间控制。**  
   \(\int\chi^2F^3\lesssim t^{-1}\) 必须对迭代所用的整个时间区间成立，而非仅某个终端切片。first-exit 的逻辑顺序应为：
   \[
   q=2,3\text{ 曲率能量}
   \Longrightarrow \text{正时间加权 }L^3\text{ 曲率势}
   \Longrightarrow J_6\text{ 的 Yang Moser}
   \Longrightarrow \|aE\|_\infty.
   \]

因此该目标已有明确的来源模板，但尚不能把脚本的尺度核验当作 PDE 证明。

---

## 5. \(p=6\) 的正则化细节

\(a^4=\chi^8\) 是光滑权重，因此选择 \(p=6\) 避免了一般实数 \(p\) 在 \(\chi=0\) 处的权重光滑性问题。

但脚本中“\(z_6=\chi^5|E|^3\) 光滑”的说法不准确：\(|E|^3\) 在 \(E=0\) 处通常不是 \(C^\infty\)。所需结论是它属于适当的 \(W^{1,2}\) 类，且

\[
|\nabla |E|^3|\le3|E|^2|\nabla E|.
\]

严格证明可采用

\[
(|E|^2+\varepsilon)^{3/2}
\]

正则化后令 \(\varepsilon\downarrow0\)。一般 \(p\)-能量也应以同样方式处理 \(|E|^{p-2}\)。

---

## 6. Yang/Wang 来源读取

### DeTurck 中的系数运输

Yang §8 在 hatted 方程中使用

\[
\hat a=(\chi\circ\varphi_t^{-1})^2,
\]

最终取

\[
g=\varphi_t^*\hat g.
\]

因此

\[
\varphi_t^*\hat a=\chi^2,
\]

拉回后确实恢复固定空间 cutoff 的流，而不是另一条时间搬运 cutoff 的方程。Step 26 对此读取正确。

归一化项应在 hatted 方程中写为

\[
-2\hat a\,\hat g,
\]

拉回后成为 \(-2\chi^2g\)。它不改变主符号，只改变零阶反应和 Gronwall 常数；但必须明确写入，不能未经适配直接引用未归一化定理。

### 短时间存在只是起点

Yang Theorem 8.2 仅给每个光滑初值某个短时间解，其长度可依赖未控制的高阶初始几何。它不能独立给出统一的 \(\theta r^2\)。

Yang Theorem 9.2 的统一时间结论本身使用最大区间/first-exit，携带：

- Sobolev 不等式；
- 全支撑度量比较；
- 临界曲率积分控制；
- 加权点态曲率界。

因此 Step 26 关于“短时间存在只是启动器”的判断正确。

### 延拓条件

Wang Theorem 4.1 给出：若有限终止时间前

\[
\|\chi^2\operatorname{Rm}\|_\infty
\]

一致有界，则局部 Ricci 流可光滑延拓。故 uniform continuation 需要全支撑加权曲率界；平台上的无权曲率界不够用于这一延拓定理。

应明确采用 Wang 的高阶 \(L^p\) 归纳，而不要依赖 Yang Theorem 9.2 末尾直接声称的全阶 \(L^2\) 曲率导数控制；Wang 正是为修补该处而给出 Lemmas 4.4–4.14 的归纳论证。

还应区分两种估计的角色：

- \(\|\chi^2\operatorname{Rm}\|_\infty\)：用于光滑延拓；
- \(\int\|\chi^2E\|_\infty dt\)：用于度量、Sobolev 常数及 cutoff 梯度的稳定。

二者在 simultaneous first-exit 中耦合，但不能互相替代。

---

## 7. 精确缺失假设与待修正表述

1. 必须明确
   \[
   0\le\chi,\eta\le1,\quad
   \eta\equiv1\text{ 于 }\operatorname{supp}\chi\text{ 的邻域},\quad
   \operatorname{supp}d\eta\subset\{a=0\}^{\circ}.
   \]

2. 当前度量下需有
   \[
   |d\chi|_{g(t)}\le Cr^{-1},
   \]
   该界由全支撑双 Lipschitz 比较从 \(g_0\) 传递。

3. 相对 Sobolev 系数与体积的尺度关系
   \[
   A^2\lesssim r^2V^{-1/2}
   \]
   必须由选定支撑的 isoperimetric/Sobolev 构造证明；脚本只验证在此假设下的体积消去。

4. \(J_p(0)\) 的小性要求
   \[
   \|\operatorname{Ric}_{g_0}+g_0\|_\infty\lesssim\delta,
   \]
   而不是任意固定宽度的 Ricci 夹逼。

5. \(C_p\beta_a<c_p/2\) 的小性来自 good-support 的临界曲率选择，不是单纯缩小 \(r\)。

6. 平台上的 \(|\operatorname{Rm}|\lesssim t^{-1}\) 需要某个前向时间柱（如 \([t/2,t]\)）上的空间 \(L^3\) 控制和嵌套平台球；单时刻 \(L^3\) 值不能直接推出点态界，且 Shi 估计只能在已有点态曲率后用于导数。

7. `step26_*ledger.py` 只核验单项式权重和尺度；完整证明仍需处理移动范数、移动体积、张量收缩、Kato 正则化及时间 cutoff。

8. 早先 Step 24 对归一化项产生“净能量阻尼”的说法已被其 supersession 否定。Step 26 的能量不等式没有使用该阻尼，故不受影响；应继续把所有相关代数反应作为
   \(C\int aF^3\)、\(C\int a^2F^4\) 等项处理。

---

## 最终判定

- **Step 25 平台位移论证：不充分。**
- **全支撑 \(\int\|aE\|_\infty\)：正确的度量比较目标。**
- **\(J_p\)、特别是 \(J_6\) 的权重：正确。**
- **初始数据无需高次 Riemann 曲率可积性：正确，但演化吸收仍需临界 \(L^2\) 曲率小性。**
- **\(p=6\) 的 \(t^{-1/3}\) 加权速度目标：与 Yang 加权 Moser 精确匹配，没有已显示的 Hardy 障碍。**
- **Yang 的 transported-coefficient 读取及“短时间存在仅为起点”的判断：正确。**
- **统一延拓：仍依赖全支撑加权曲率、加权速度、当前 Sobolev 和临界势控制的同步闭合。**

当前最集中的未决分析对象不是权重或尺度，而是：严格建立缺陷方程的 Yang 型标量/Kato 不等式，并以整段正时间加权 \(L^3\) 曲率界作为势，完成 \(J_6\to\|aE\|_\infty\) 的实例化；同时写出归一化 Wang 延拓的零阶修正。
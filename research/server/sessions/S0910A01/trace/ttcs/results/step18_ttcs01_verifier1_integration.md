# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 18,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step18_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step18_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 18 refined cutoff-flow analysis for the four-dimensional negative LeBrun route. Please read the corrected Step 18 note, the patched Step 17 support-scale note, the A03 Step 17 cutoff-flow note, Li's source theorem passages, and the Step 18 scripts. Check: (1) the weighted scalar identity for f=a|Rm| and the conclusion that the quadratic reaction is f^2 rather than f^2/a; (2) whether the integrated principal energy can avoid pointwise Hessian cutoff assumptions at least in the scalar model and what remains tensorially; (3) whether the coupled L2 layer is legitimately separated from the remaining pointwise smoothing problem; (4) whether unweighted Q(t) is correctly kept distinct from weighted aE; (5) whether the model computations support but do not prove degenerate epsilon-regularity. Give a direct scientific memo with corrections or a sharper theorem target; do not turn this into final-route control.

## Integrated Scientific Memo

# Step 18 科学核验备忘录

## 结论

Step 18 的核心代数修正是正确的：

\[
f=a|\Rm|,\qquad a=\chi^2
\]

所满足的二次反应项是 \(cf^2\)，不是 \(cf^2/a\)。标量主部的积分能量恒等式也确实可通过一次分部积分消去 \(\Delta a\)，因而该层不需要逐点 Hessian cutoff 控制。

但当前材料尚未证明完整的张量 \(L^2\) 系统，更未证明退化区间上的 \(\varepsilon\)-正则性。合理的状态应为：

- **标量代数、尺度抵消和候选能量结构：已核验；**
- **耦合 \(L^2\) 层：在光滑解、度量可比和沿流 Sobolev 控制的 bootstrap 区间内有可信闭合机制，但完整张量推导尚缺；**
- **从临界能量到 \(|a\Rm|\le C/t\)：仍是开放核心；**
- **\(Q(t)=\int|E|^2\) 必须直接作无权控制，不能由 \(aE\) 推出。**

此外有三个具体修正：退化热核脚本漂移符号反了；A03 将 \(C/t\) 称为从 \(0\) 可积是错误的；现有 good-set 半径并未自动控制整个 \(B_{5r_*}\) 支撑区。

---

## 1. \(f=a|\Rm|\) 的加权恒等式

在 \(\{a>0\}\) 上写 \(K=|\Rm|=f/a\)。由

\[
K_t\le a\Delta K+caK^2+T
\]

以及 \(a_t=0\)，得到

\[
f_t\le a^2\Delta(f/a)+ca^2K^2+aT.
\]

商法则给出

\[
a^2\Delta(f/a)
=a\Delta f-2\langle\nabla a,\nabla f\rangle
+\left(\frac{2|\nabla a|^2}{a}-\Delta a\right)f,
\]

故

\[
\boxed{
f_t\le a\Delta f-2\langle\nabla a,\nabla f\rangle
+\left(\frac{2|\nabla a|^2}{a}-\Delta a\right)f
+cf^2+aT .
}
\]

因为

\[
a^2K^2=(aK)^2=f^2,
\]

反应项确为 \(cf^2\)，绝非 \(cf^2/a\)。对 \(a=\chi^2\)，

\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2,
\qquad
\frac{2|\nabla a|^2}{a}-\Delta a
=6|\nabla\chi|^2-2\chi\Delta\chi .
\]

因此不存在逆 \(\chi\) 奇性，但逐点方程仍含 \(\chi\Delta\chi\)。

`step18_weighted_cutoff_algebra.py` 正确核验了这一乘积法则；它没有核验真实曲率张量演化中 \(T\) 的组成。严格处理 \(K=|\Rm|\) 在 \(\Rm=0\) 处的不可微性时，应使用

\[
K_\varepsilon=(|\Rm|^2+\varepsilon^2)^{1/2}
\]

后令 \(\varepsilon\downarrow0\)，或直接从张量方程结合 Kato 不等式导出。

---

## 2. 标量积分主能量确实不需要逐点 \(\nabla^2a\)

令

\[
L_af=a\Delta f-2\langle\nabla a,\nabla f\rangle
+\left(2|\nabla a|^2/a-\Delta a\right)f.
\]

固定时刻以 \(\eta^2f\) 测试并对 \(-\Delta a\) 项分部积分，可得

\[
\begin{aligned}
\int \eta^2fL_af
={}&-\int a\eta^2|\nabla f|^2
-2\int a\eta f\langle\nabla\eta,\nabla f\rangle\\
&-\int\eta^2f\langle\nabla a,\nabla f\rangle
+2\int\eta f^2\langle\nabla\eta,\nabla a\rangle\\
&+2\int\eta^2f^2\frac{|\nabla a|^2}{a}.
\end{aligned}
\]

Young 不等式于是给出

\[
\int\eta^2fL_af
\le
-c\int a\eta^2|\nabla f|^2
+C\int
\left(
a|\nabla\eta|^2
+\eta^2\frac{|\nabla a|^2}{a}
\right)f^2 .
\]

所以标量主部只需要一阶 cutoff 控制。脚本在这一有限意义上正确；它未包括随时间变化的体积元、张量范数和其他耦合项。

### 张量层剩余对象

真实曲率能量中会出现例如

\[
\int\eta^2\langle \Rm,(\nabla^2a)*E\rangle,
\qquad
\int\eta^2(\nabla^2a)*\Rm*\Rm .
\]

一次分部积分可把它们变成

\[
\nabla a*\nabla E*\Rm,\qquad
\nabla a*E*\nabla\Rm,\qquad
\nabla a*\nabla\Rm*\Rm
\]

以及 localization-gradient 项。利用

\[
|\nabla a|=2\sqrt a\,|\nabla\chi|,
\qquad |\nabla\chi|\lesssim r^{-1},
\]

这些项预期满足

\[
\varepsilon\int a|\nabla\Rm|^2
+\varepsilon\int a|\nabla E|^2
+Cr^{-2}\int (|\Rm|^2+|E|^2).
\]

因此在**弱张量 \(L^2\) 能量层**避免点态 Hessian 假设很可能成立，但供应材料尚未给出完整指标推导，尤其需检查：

- 所有 \(\nabla^2a\) 收缩；
- 度量逆、范数及体积元变分；
- Bianchi 交换与局部化边界项；
- 加权耗散是否与每个 Young 配对完全匹配。

点态最大值原理则是另一回事：其中直接出现 \(|\nabla^2_{g(t)}a|\)。仅有 \(C^0\) 度量可比不能统一控制 Christoffel 差，从而不能统一控制该 Hessian。若要避免这一假设，应以弱 Moser/能量方法取代该点态论证。

---

## 3. 耦合 \(L^2\) 层与点态平滑应区分，但当前不能称为无条件定理

四维吸收尺度是正确的。若

\[
R_U=\frac{r^4}{V_U}\int_U|\Rm|^2,\qquad
A_U\lesssim \frac{r^2}{V_U^{1/2}},
\]

则

\[
A_U\|\Rm\|_{L^2(U)}
\lesssim
\frac{r^2}{V_U^{1/2}}
\frac{R_U^{1/2}V_U^{1/2}}{r^2}
\lesssim R_U^{1/2}.
\]

因而

\[
\begin{aligned}
\int \eta^2a|\Rm||E|^2
&\le \|\Rm\|_2\|\eta\chi E\|_4^2\\
&\lesssim A_U\|\Rm\|_2
\left[
\int\eta^2a|\nabla E|^2+
\int(a|\nabla\eta|^2+\eta^2|\nabla\chi|^2)|E|^2
\right],
\end{aligned}
\]

在 \(R_U\) 足够小时可吸收。曲率三次项通过 \(\eta\chi|\Rm|\) 有同样机制。脚本正确验证了

\[
A_U\|\Rm\|_2\sim \sqrt{K_0}\,r^2
\]

且塌缩体积消失。

这支持候选系统

\[
\begin{aligned}
\dot R_\alpha+cX_\alpha
&\le Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta)
+\varepsilon Y_\alpha,\\
\dot P_\alpha+cY_\alpha
&\le Cr^{-2}\sum_{\beta\sim\alpha}P_\beta .
\end{aligned}
\]

但应表述为：

> 在已有光滑解、度量可比、沿流相对 Sobolev 不等式及全支撑初始临界能量小性的 bootstrap 区间内，完整张量计算预期给出该闭合系统。

A03 所称“无条件已证明的 \(L^2\) 传播”过强。因为沿流 Sobolev 常数和球体积比较依赖度量可比；度量可比又需控制

\[
\int_0^t\|aE(s)\|_\infty\,ds,
\]

而该控制尚与退化点态正则性耦合。故可靠结构是“联合 continuation package”，不是一个完全独立的已证明底层加单一开放顶层。

即使上述 \(L^2\) 系统闭合，它也只传播临界能量，不能推出退化平均值不等式，更不能自动推出

\[
|a\Rm|\le C/t.
\]

Li 的 Theorem 3.4/3.6 使用非退化 Laplacian，并对所有相关中心的局部能量 supremum 作 bootstrap；有限 plateau 的半径包含关系不等价于其全中心动态假设。

### 支撑尺度遗漏

当前 Step 17 由以 \(p\) 为中心、半径至 \(4r_*\) 的 maximal function 控制初始数据，但活动支撑达到 \(B_{5r_*}(p)\)。这不自动控制过渡外环中所有半径 \(r_*\) 的局部能量。一个直接修补是把 maximal-function 截断半径至少扩至 \(6r_*\)：若 \(y\in B_{5r_*}(p)\)，则

\[
B_{r_*}(y)\subset B_{6r_*}(p),
\]

再以 Bishop–Gromov 比较转换为 shifted-center 归一化小能量。

---

## 4. \(Q(t)\) 与 \(aE\) 的区分正确且必要

度量速度由

\[
|\partial_tg|=2|aE|
\]

控制，故度量漂移需要的是加权点态量，例如

\[
\int_0^T\|aE(t)\|_\infty\,dt.
\]

而 LeBrun 拓扑重新校准需要

\[
Q(t)=\int_M|E(t)|^2\,d\mu_{g(t)}
\]

这一**无权全局量**。在 \(a\to0\) 处，\(aE\) 不提供 \(E\) 的控制，因此二者绝不能替换。

更有希望的 \(Q\)-路线是直接把无权缺陷能量中的

\[
\int a|\Rm||E|^2
\]

用上述四维 Sobolev–\(L^2\) 吸收处理，从而得到 support-summed 不等式

\[
Q'(t)\lesssim r^{-2}Q(t)
\]

并推出 \(Q(t)\le CQ(0)\)。这避免依赖点态 \(\|\Rm\|_\infty\)，也比 A03 以 transition pointwise curvature 为输入的论证更不循环。

### A03 最大值原理中的错误

由

\[
|a\Rm|\le C/t
\]

不能直接从 \(t=0\) 对最大值原理积分，因为

\[
\int_0^T\frac{dt}{t}=\infty.
\]

因此“\(C/t\) 可积，仅产生对数增长”的陈述错误。若从 \(t_0>0\) 开始，常数会依赖 \(t_0\)，不能据此得到统一的 \(|E(t)|\le C\delta\)。

真正可用于度量漂移的目标应是具有可积时间奇性的加权缺陷估计，例如

\[
\|aE(t)\|_\infty
\le C_p\delta\left(\frac{r^2}{t}\right)^{2/p},
\qquad p>2,
\]

因为

\[
\int_0^{\theta r^2}t^{-2/p}\,dt<\infty.
\]

---

## 5. 模型计算只提供一致性证据

### 常扩散系数模型

若 \(a\) 局部为常数，\(p=n/2\) 时

\[
\|K(t)\|_\infty\lesssim(at)^{-1}\|K_0\|_{L^{n/2}},
\]

故

\[
\|aK(t)\|_\infty\lesssim t^{-1}\|K_0\|_{L^{n/2}}.
\]

这正确说明 \(aK\) 是自然目标，但没有处理 \(\nabla a\)、非线性或张量耦合。

### \(a=x^2\) 模型的脚本修正

令 \(y=\log x\)，则

\[
K_t=x^2K_{xx}
\quad\Longleftrightarrow\quad
u_t=u_{yy}-u_y.
\]

相应正确热核为

\[
G(y,z,t)
=(4\pi t)^{-1/2}
\exp\!\left[-\frac{(y-z-t)^2}{4t}\right].
\]

脚本使用了 \(y-z+t\)，即反向漂移。修正后，小时间 \(L^2(dx)\to L^\infty\) 加权范数的 \(t^{-1/4}\) 幂次和“靠近退化边界的归一化尖峰产生更小加权输出”的定性结论仍保持，但数值表应重新生成。

此外：

- 脚本没有指定 \(y=0\) 的半直线边界条件；
- 光滑紧支撑 cutoff 在与冻结区相接处通常是平坦的，\(\chi=x\) 并非该边缘的真实局部型；
- 模型遗漏切向变量、\(f^2\) 反应、张量 cutoff 项及 \(E\) 耦合。

故这些计算只说明未发现简单的一维尺度障碍，绝非退化 \(\varepsilon\)-正则性证明。

---

## 更精确的定理目标

应把目标写成一个联合 bootstrap 定理。假设已有光滑 cutoff-flow 解，并在全活动支撑的所有相关 Whitney/固定尺度球上具有归一化临界能量小性，证明同时成立：

1. 沿流度量可比、相对 Sobolev 不等式和有限重叠覆盖保持；
2. 仅用一阶 cutoff 控制的完整张量耦合能量不等式；
3. \(\sup_\alpha(R_\alpha+\kappa P_\alpha)\) 的短时保持；
4. 无权缺陷控制
   \[
   Q(t)\le CQ(0);
   \]
5. 退化加权正则性
   \[
   \sup a|\Rm(t)|\le C/t;
   \]
6. 可积的加权缺陷估计
   \[
   \sup a|E(t)|
   \le C_p\delta(r^2/t)^{2/p},\qquad p>2.
   \]

其中真正尚缺的点态机制是第 5 项，同时第 2 项尚需完整张量审计。一个可能的局部几何框架是 Whitney 尺度：

\[
|\nabla\chi|\lesssim r^{-1}
\quad\Longrightarrow\quad
\chi\asymp\chi(x)
\ \text{于}\ 
B_{cr\chi(x)}(x),
\]

而扩散长度

\[
\sqrt{a(x)t}=\chi(x)\sqrt t
\]

在 \(t\le\theta r^2\) 时位于该球内。于是可在每个 \(a(x)>0\) 点把方程按其自然退化尺度重标为统一抛物型；剩余任务是把这一 Whitney-scale 观察提升为具有张量耦合、弱 cutoff 正则性和塌缩无关常数的 Moser/mean-value 定理。
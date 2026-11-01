# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 19,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step19_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step19_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the proposed first-exit closure for the 4D normalized cutoff flow. The claim is that Wang's Theorem 6.3 can be localized to a finite-neighbor system of balls on a closed 4-manifold under the normalized cutoff flow ∂_tg = -2χ²(Ric+g), yielding the volume-independent curvature decay |χ²Rm| ≤ C√ε/t.

Specific points to check:

1. VOLUME-INDEPENDENT BETA: On a ball B_r with Ric ≥ -3g, the relative Sobolev constant is A ~ C·r·V^{-1/4}. The maximal-function selection gives ∫_{B_r}|Rm|² ≤ K₀·V. Therefore β = A²·||Rm||_{L²} = C²r²V^{-1/2}·√(K₀V) = C²r²√K₀. With the Li radius r_* = (ε/K₀)^{1/4}, this gives β = C²√ε. Does this volume cancellation hold exactly in 4D? Does it fail in other dimensions?

2. LOCALIZATION OF WANG/YANG: Wang's proof (Theorem 6.3, see context_files) uses a global Sobolev inequality and global L^{n/2} curvature energy. The localized version replaces these with relative Sobolev on each ball and local energies R_α per ball. The Moser iteration (Li Theorem 2.5) runs on each individual ball B_r(x) with nested sub-balls. The energy persistence comes from the coupled L² system dH_α/dt ≤ Cr^{-2}Σ_{β~α}H_β. Does this localization introduce any new terms or require additional hypotheses beyond the coupled energy control?

3. NORMALIZED FLOW CORRECTION: Under ∂_tg = -2χ²(Ric+g) = -2χ²Ric - 2χ²g, the curvature evolution gains additional terms from h₂ = -2χ²g. These are ∂_tRm|_{h₂} ~ Hess(χ²)·g + χ²·Rm (from the metric variation formula). In the L^{n/2} energy equation, these contribute O(r^{-2})∫|Rm|^{n/2} (lower order) and ∫χ²|Rm|^{n/2} (absorbed). Is this correct? Are there any higher-order terms from the normalization that could affect the Moser absorption?

4. FIRST-EXIT CLOSURE LOGIC: Given β small → |χ²Rm|≤Cβ/t → curvature potential for Li → |χ²E|≤C_pδ(r²/t)^{2/p} → weighted Bernstein |χ∇(χ²E)|≤C_pδt^{-1/2}(r²/t)^{2/p} → for p>4: metric drift O(δθ^{1-2/p}r²), connection drift O(δθ^{1/2-2/p}), Hessian drift O(δθ^{1/2-2/p}/r) → all provisional first-exit bounds improved for small δ. Is there any circular dependency? Does the Bernstein estimate actually follow from the weighted parabolic structure?

## Integrated Scientific Memo

# 核验结论

所提“first-exit closure”目前**不能成立为已证明定理**。可靠成立的是：

- 四维中 \(\beta\) 的塌缩体积消去；
- 固定有限邻接系统上的临界 \(L^2\) 能量传播框架；
- 归一化项不产生超过 \(\nabla^2(\chi^2)\) 的新导数；
- 假设加权点值与梯度估计后，\(p>2\) 和 \(p>4\) 的漂移可积阈值。

尚未由 Wang、Li 或现有笔记证明的两个核心 PDE 命题是：

\[
R_\alpha(t)\ll1
 \Longrightarrow
 \|\chi^2\Rm(t)\|_\infty\le C\beta/t
\]

在**退化、局部、有限邻接**系统中的版本，以及

\[
\|\chi\nabla(\chi^2E)(t)\|_\infty
 \le C_p\delta\,t^{-1/2}(r^2/t)^{2/p}.
\]

因此该闭合链是一个合理的**条件性方案**，而不是现有来源的推论。

---

## 1. \(\beta\) 的体积消去

令 \(V_\alpha=\Vol(U_\alpha)\)，并在扩大球 \(\widetilde U_\alpha\) 上使用曲率能量。相对 Sobolev 不等式写成

\[
\|v\|_4
 \le A_\alpha\bigl(\|\nabla v\|_2+r^{-1}\|v\|_2\bigr),
 \qquad
 A_\alpha\le C_SrV_\alpha^{-1/4}.
\]

若

\[
\int_{\widetilde U_\alpha}|\Rm|^2
 \le K_0\Vol(\widetilde U_\alpha),
\qquad
\Vol(\widetilde U_\alpha)\le C_VV_\alpha,
\]

则 Wang 型小参数满足

\[
\begin{aligned}
\beta_\alpha
&=A_\alpha^2
  \|\Rm\|_{L^2(\widetilde U_\alpha)}\\
&\le C_S^2 C_V^{1/2} r^2\sqrt{K_0}.
\end{aligned}
\]

所以 \(V_\alpha^{-1/2}\) 与曲率范数中的 \(V_\alpha^{1/2}\) **恰好消去**。取

\[
r_*^4K_0=\varepsilon
\]

即得

\[
\beta_\alpha\le C_S^2C_V^{1/2}\sqrt{\varepsilon}.
\]

严格地说，这是带固定 Sobolev、扩大球体积比较和邻接度常数的不等式，不是无常数的等式。若扩大球由有限多个邻球覆盖，更准确的是

\[
A_\alpha^2\|\Rm\|_{L^2(\widetilde U_\alpha)}
 \lesssim
 \left(\sum_{\beta\sim\alpha}R_\beta\right)^{1/2}.
\]

因此 Wang 的阈值还须吸收有限邻接度。

### 是否只在四维成立？

体积消去本身并非四维独有。一般维数中，若掌握临界平均能量

\[
\fint_{B_r}|\Rm|^{n/2}\le K_{n/2},
\]

则

\[
A^2\sim r^2V^{-2/n},\qquad
\|\Rm\|_{L^{n/2}}\le K_{n/2}^{2/n}V^{2/n},
\]

从而

\[
A^2\|\Rm\|_{L^{n/2}}
 \lesssim r^2K_{n/2}^{2/n}.
\]

四维特殊之处在于 \(n/2=2\)：现有 \(L^2\) 曲率能量正好是临界能量，并且 Li 的塌缩无关机制及相关拓扑控制本质上是四维输入。对 \(n>4\)，仅有平均 \(L^2\) 控制不能推出临界 \(L^{n/2}\) 控制。

---

## 2. Wang/Yang 不能直接逐球套用

Wang 定理 6.3 假定：

\[
\|f\|_{\frac{2n}{n-2}}\le A_0\|\nabla f\|_2,
\qquad
A_0^2\|\Rm\|_{L^{n/2}(M)}\le\beta,
\]

以及全局 \(L^p\) Ricci 控制。所需版本则使用逐球相对 Sobolev、局部能量和退化算子 \(\partial_t-\chi^2\Delta\)。这不是简单的“限制到球上”。

引入独立局部化函数 \(\eta_\alpha\) 后，能量计算至少增加

\[
a|d\eta|^2F^q,\qquad
\frac{|da|^2}{a}\eta^2F^q,\qquad
|da||d\eta|F^q,
\qquad a=\chi^2,
\]

以及相对 Sobolev 的零阶项

\[
Cr^{-2}\int\eta^2F^q.
\]

其中

\[
\frac{|da|^2}{a}=4|d\chi|^2
\]

是正则的。扩大支撑还导致邻接能量

\[
A_\alpha^2\|\Rm\|_{L^2(\widetilde U_\alpha)}
 \lesssim
 \left(\sum_{\beta\sim\alpha}R_\beta\right)^{1/2}.
\]

因此

\[
\dot H_\alpha
 \le Cr^{-2}\sum_{\beta\sim\alpha}H_\beta
\]

能够提供临界能量持续性，但并非局部 Moser 迭代的唯一输入。还需要：

- 暂定度量等价；
- 随时间一致的相对 Sobolev 常数；
- 邻球体积比较与有界邻接度；
- \(d\chi,d\eta\) 控制；
- 嵌套支撑位于有缓冲的好区域；
- 演化测度项控制。

归一化流下

\[
\partial_td\mu=-\tr(aE)\,d\mu,
\]

所以 Moser 能量还出现

\[
\int |\tr(aE)|\,\eta^2F^q.
\]

它可望由固定超临界 \(L^p\) 缺陷估计经插值处理，但必须写入证明。

此外，Step 18 已正确指出不能在所有 Moser 指数上反复使用临界小能量吸收：反应系数通常按 \(q\sqrt{\varepsilon_*}\) 增长。正确结构应为：

1. 在一个固定 \(p_0>2\) 上传播 \(aE\)；
2. 另行证明加权曲率势估计；
3. 再按 Li 定理 2.5 的“时间依赖势”机制迭代到 \(L^\infty\)。

Li 的局部迭代是非退化的，Wang 的加权退化迭代是全局的；所需“局部且退化”的混合版本仍需独立证明。

---

## 3. 归一化项的精确影响

对一般度量变分 \(h\)，

\[
D\Rm_g(h)=\nabla^2h\ \text{的曲率对称化}+\Rm*h.
\]

取

\[
h_2=-2ag,\qquad a=\chi^2,
\]

由于 \(\nabla g=0\)，

\[
D\Rm_g(h_2)
 =-(\nabla^2a)\owedge g+a\,\mathcal R(\Rm)
\]

至多差约定相关常数。因此：

- 不出现高于 \(\nabla^2a\) 的导数；
- \(a\Rm\) 是乘法型低阶项；
- \((\nabla^2a)\owedge g\) 是与 \(\Rm\) 无关的加性源。

在 \(q=n/2\) 曲率能量中，Hessian 项实际为

\[
\int\eta^2|\Rm|^{q-2}
 \left\langle\Rm,(\nabla^2a)\owedge g\right\rangle,
\]

其大小是

\[
\int\eta^2|\nabla^2a|\,|\Rm|^{q-1},
\]

并不能直接写成

\[
Cr^{-2}\int|\Rm|^q.
\]

积分分部一次后会产生

\[
|da|\,|\Rm|^{q-2}|\nabla\Rm|,
\]

Young 不等式留下较低曲率次幂。两个可行修正是：

### 修正 A：使用 \(F=(1+|\Rm|^2)^{1/2}\)

所有较低次幂均由 \(F^q\) 控制。初始参数变成

\[
A^2\|F\|_2
 \lesssim \beta+r^2.
\]

在近 \(\Ric=-g\) 的情形，\(|\Rm|\) 有维数性非零基线，故 \(K_0\ge c>0\)，从而

\[
r^2\lesssim r^2\sqrt{K_0}\asymp\beta,
\]

于是仍可保持 \(O(\beta)\) 量级。

### 修正 B：合并完整速度 \(-2aE\)

不要单独估计 \(-2ag\)，而是先将 Ricci 部分与 metric 部分合并。这样源项可改写为

\[
\nabla^2a*E+da*\nabla E,
\]

反映 \(E=0\) 时完整流静止，但代价是曲率估计与缺陷能量耦合。

所以“归一化只增加可吸收的
\(O(r^{-2})\int|\Rm|^{n/2}\)”并不严格；但“归一化不增加更高阶导数，不改变主 Moser 阶数结构”是正确的。

---

## 4. 从曲率点值估计到曲率势

若局部化 Wang 估计已经证明：

\[
\|a\Rm(t)\|_\infty\le \frac{C\beta}{t},
\qquad
\|\Rm\|_2\le \frac{\beta}{A^2},
\]

则 Step 18 所需的三次势满足

\[
\begin{aligned}
K_3(t)
&=\int a|\Rm|^3\\
&\le \|a\Rm\|_\infty\int|\Rm|^2\\
&\le \frac{C\beta^3}{A^4t}.
\end{aligned}
\]

因此

\[
K_3(t)\le \frac{C}{A^4t}
\]

确实随之成立，且小 \(\beta\) 时更强。这一环没有额外体积问题。

但前提——局部、退化、有限邻接版本的

\[
\|a\Rm\|_\infty\le C\beta/t
\]

——正是尚未证明的核心命题，而不能直接引用 Wang 定理 6.3。

---

## 5. First-exit 漂移与真正缺口

设已知

\[
U=aE,\qquad
\|U(t)\|_\infty
 \le C_p\delta(r^2/t)^{2/p}.
\]

则

\[
\int_0^{\theta r^2}\|U(t)\|_\infty\,dt
 \le C_p\frac{p}{p-2}
 \delta\,\theta^{1-2/p}r^2.
\]

故度量漂移的精确可积阈值是 \(p>2\)。

若进一步已知

\[
\|\chi\nabla U(t)\|_\infty
 \le C_p\delta\,t^{-1/2}(r^2/t)^{2/p},
\]

则

\[
\int_0^{\theta r^2}\|\chi\nabla U(t)\|_\infty\,dt
 \le C_p\frac{2p}{p-4}
 \delta\,\theta^{1/2-2/p}r.
\]

故加权一阶漂移阈值是 \(p>4\)，\(p=4\) 为对数端点。

### Hessian 漂移

因为固定函数 \(a\) 的 Hessian 仅通过联络变化，

\[
\partial_t(\nabla^2a)_{ij}
 =-(\partial_t\Gamma^k_{ij})a_k,
\qquad
\partial_t\Gamma=\nabla U,
\]

并且 \(da=2\chi\,d\chi\)，所以

\[
|\partial_t\nabla^2a|
 \le C|d\chi|\,|\chi\nabla U|.
\]

若 \(|d\chi|\le C/r\)，则

\[
\|\nabla^2a(t)-\nabla^2a(0)\|_\infty
 \le C_p\frac{2p}{p-4}
 \delta\,\theta^{1/2-2/p}.
\]

因此所给脚本和原链中的 \(O(\delta/r)\) Hessian 漂移并非由其显示的 Bernstein 估计推出；时间积分带来的 \(r\) 与 \(|d\chi|\sim r^{-1}\) 抵消。

### 加权联络不等于完整联络

精确地，

\[
|\Gamma(t)-\Gamma(0)|
 \lesssim\int_0^t|\nabla U|\,ds.
\]

\(\chi\nabla U\) 的估计不能在 \(\chi\to0\) 处控制完整 \(\nabla U\)。它只直接控制：

- 加权联络差 \(\chi(\Gamma(t)-\Gamma(0))\)，或
- 与 \(da\) 收缩的联络差，因而足够控制 \(\nabla^2a\)。

若 first-exit 条件要求全局无权联络差，则必须另证 \(\nabla U\) 的无权估计，或将退出量改成真正被方程控制的加权量。

---

## 6. Bernstein 估计没有从现有材料推出

标量模型

\[
u_t=\chi^2\Delta u
\]

确实提示局部扩散长度为 \(\chi\sqrt t\)，从而形式上

\[
\chi|\nabla u|\lesssim t^{-1/2}\|u\|_\infty.
\]

但对

\[
\partial_tU=a(\Delta_LU-2U)+\mathcal B_a(U)
\]

直接微分会产生

\[
\nabla a*\nabla^2U,\quad
a\nabla\Rm*U,\quad
a\Rm*\nabla U,\quad
\nabla^3a*U,\quad
\nabla^2a*\nabla U.
\]

仅有 \(a\Rm\le C/t\) 并不控制 \(a\nabla\Rm\)。Li 定理 2.5 是函数值 Moser 估计，不是导数估计；Wang 的延拓部分提供的是在额外高阶 \(L^q\) 与 cutoff 导数控制下的定性正则性，也没有给出序列一致、对 \(\delta\) 线性且具有

\[
t^{-1/2-2/p}
\]

精确速率的估计。

因此 Bernstein 步骤不是已证推论。需要证明的精确对象是一个局部加权

\[
L^p\longrightarrow W^{1,\infty}
\]

估计，其常数只依赖于暂定 Sobolev 几何、有限邻接度、曲率势 \(K_3\) 和受控 cutoff 系数，而不依赖塌缩体积。

---

## 最终判定

所提闭合逻辑没有形式上的恶性循环：它可组织为同时 first-exit 论证，并在所有关键估计已建立时严格改善退出量。但目前它依赖两个未证输入：

1. **局部退化曲率正则化**
   \[
   \sup_\alpha R_\alpha\ll1
   \Longrightarrow
   \|\chi^2\Rm(t)\|_\infty\le C\beta/t;
   \]

2. **局部退化加权张量梯度估计**
   \[
   \|\chi\nabla(\chi^2E)(t)\|_\infty
   \le C_p\delta\,t^{-1/2}(r^2/t)^{2/p}.
   \]

此外必须修正：

- 归一化 Hessian 项是加性低阶源，不能未经处理直接视为
  \(r^{-2}\int|\Rm|^{n/2}\)；
- \(\chi\nabla U\) 只控制加权联络或与 \(da\) 收缩的联络，不控制完整联络；
- Hessian 漂移的所示 \(r\)-尺度应按上式重算；
- 若退出系统包含全局无权
  \(\int|E|^2\)，加权 \(aE\) 估计在 \(a=0\) 区域不能自动传播它，仍需单独的全局能量论证。

故当前最强可靠结论是：**体积消去和漂移指数成立；Wang/Yang 的有限邻接局部化及 Bernstein 步骤尚未闭合，因而声称已得到体积无关曲率衰减并完成 first-exit closure，证据不足。**
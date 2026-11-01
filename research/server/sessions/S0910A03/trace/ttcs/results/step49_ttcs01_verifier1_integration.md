# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 49,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step49_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step49_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematical correctness of the normalized cutoff Ricci flow existence and extension theorem in step49_normalized_flow_existence_and_extension.md. The flow equation is ∂_t g = -2χ²(Ric(g) + g), which differs from Yang's equation ∂_t g = -2χ²Ric by the zeroth-order term -2χ²g. The note claims:

1. The extra Christoffel variation from h = -2bg is -(δ^k_j ∂_i b + δ^k_i ∂_j b - g_ij ∇^k b) using ∇g=0. The curvature variation is -2bRm - g∧∇²b (Kulkarni-Nomizu product). Verify these formulas.

2. In the L^p energy evolution, the extra terms contribute: a dissipative -2p∫b|Rm|^p (favorable) and a source bounded by Cp·||∇²a||_∞·(∫|Rm|^p + Vol). The Grönwall coefficient is therefore ε-independent since ∇^k b_ε = ∇^k a for k≥1. Verify this is correct.

3. The coefficient-regularized existence (b_ε = χ²+ε² with ε>0) gives uniformly parabolic equations, and the ε-independent energy bounds give a common existence time T₀. The ε→0 passage uses interior C^k estimates on {χ>0}, vanishing drift on {χ=0}, and weighted estimates for regularity at ∂supp(χ). Verify this argument.

4. The extension criterion: bounded |χ²Rm| on [0,T*) implies smooth extension past T*, by adapting Wang's staggered induction. The normalization adds bounded lower-order terms at each level. Verify compatibility with Wang's framework.

5. The positive-time slab argument: if T* is a finite maximal time, the Moser endpoint |χ²Rm| ≤ Cγ/t is finite on [T*/2,T*), giving bounded |χ²Rm| there, so the extension criterion applies — contradiction. This resolves the issue that γ/t diverges at t=0 without needing a uniform bound on [0,T]. Verify this argument is sound.

Check for hidden assumptions, circular reasoning, or gaps. The note explicitly does NOT claim uniqueness, sequence-uniform estimates, or any result about Yau Problem 26.

## Integrated Scientific Memo

# 核验结论

`step49_normalized_flow_existence_and_extension.md` **目前不能视为已经证明了其存在与延拓定理**。归一化项确实不改变主符号，并在正确建立 cutoff-jet 控制后与 Yang/Wang 的框架结构兼容；但文中存在一个曲率符号错误、一个重要的能量符号误判，以及 \(\varepsilon\to0\) 极限和任意阶延拓中的实质缺口。

## 1. Christoffel 与曲率变分

令 \(h=-2bg\)。连接变分为
\[
\dot\Gamma^k_{ij}
=\frac12g^{k\ell}(\nabla_i h_{j\ell}+\nabla_jh_{i\ell}-\nabla_\ell h_{ij})
=-(\delta^k_j b_i+\delta^k_i b_j-g_{ij}b^k),
\]
故 (1.1) 正确。

采用笔记明确写出的约定
\[
\dot R^k{}_{\ell ij}
=\nabla_i\dot\Gamma^k_{j\ell}-\nabla_j\dot\Gamma^k_{i\ell},
\]
直接计算得到
\[
\dot R_{k\ell ij}
=-2bR_{k\ell ij}
+g_{ki}H_{j\ell}+g_{j\ell}H_{ik}
-g_{kj}H_{i\ell}-g_{i\ell}H_{jk},
\qquad H=\nabla^2b.
\]
因此，在通常的 Kulkarni–Nomizu 约定下，
\[
\boxed{\dot{\mathrm{Rm}}\big|_N
=-2b\,\mathrm{Rm}+g\owedge\nabla^2b.}
\]
所以 (1.2)–(1.3) 中 Hessian 项的符号应为 **正号**。这一错误不影响后续只使用绝对值的源项估计。

另有两个结构性修正：

- (2.1) 中 cutoff 展开应出现
  \[
  \nabla^2b*\operatorname{Ric},\qquad
  \nabla b*\nabla\operatorname{Ric},
  \]
  而不是 \(\nabla^2b*\nabla\operatorname{Ric}\)。
- 对 \(m\ge1\)，不能写成
  \[
  \partial_t\nabla^m\mathrm{Rm}
  =\nabla^m\partial_t\mathrm{Rm}.
  \]
  还需加入
  \[
  \sum_{r=0}^{m-1}\nabla^r\dot\Gamma_N*
  \nabla^{m-1-r}\mathrm{Rm},
  \qquad \dot\Gamma_N\sim\nabla a.
  \]
  它们是低阶项，但必须纳入 staggered induction。

## 2. \(L^p\) 能量：上界结构可行，但“耗散”结论错误

笔记计算的
\[
-2p\int b|\mathrm{Rm}|^p
\]
只是 covariant \((0,4)\)-曲率张量反应项本身的贡献，并不是完整的 norm evolution。

因为
\[
\dot g^{-1}=2b\,g^{-1},
\]
\(|\mathrm{Rm}|^2\) 中四个逆度量因子合计贡献
\(8b|\mathrm{Rm}|^2\)，而张量变分贡献
\(-4b|\mathrm{Rm}|^2\)。故
\[
\partial_t|\mathrm{Rm}|^p\big|_N
=2pb|\mathrm{Rm}|^p
+p|\mathrm{Rm}|^{p-2}
 \langle \mathrm{Rm},g\owedge\nabla^2b\rangle .
\]
再结合
\[
\dot d\mu=-nb\,d\mu,
\]
得到完整归一化贡献
\[
\boxed{
\frac d{dt}\int|\mathrm{Rm}|^p\,d\mu\Big|_N
=(2p-n)\int b|\mathrm{Rm}|^p\,d\mu
+p\int|\mathrm{Rm}|^{p-2}
 \langle\mathrm{Rm},g\owedge\nabla^2b\rangle\,d\mu .
}
\]
因此当 \(p>n/2\) 时净 reaction 一般是正的，而非耗散。不过由于
\(0\le b_\varepsilon\le2\)，它仍只是一个有界的 Grönwall 项。

若已经知道
\[
\sup_{\varepsilon,t}\|\nabla^2_{g_\varepsilon}a\|_\infty<\infty,
\]
则
\[
\left|
p\int|\mathrm{Rm}|^{p-2}
\langle\mathrm{Rm},g\owedge\nabla^2a\rangle
\right|
\le C(n)p\|\nabla^2a\|_\infty(E_p+\operatorname{Vol}),
\]
所以 (2.2) 的最终“附加项为 \(\varepsilon\)-独立 Grönwall 项”的结构是合理的。

但
\[
\nabla^k_{g_\varepsilon}b_\varepsilon
=\nabla^k_{g_\varepsilon}a
\]
只说明常数 \(\varepsilon^2\) 的导数消失，**并不自动给出一致有界性**。例如
\[
\nabla^2_ga=\partial^2a-\Gamma(g)*\partial a
\]
依赖于演化连接。因此必须通过 cutoff-jet/connection 的耦合估计证明其一致界，不能把 \(\nabla^ka\) 当作与演化度量无关的固定有界张量。

## 3. 系数正则化与 \(\varepsilon\to0\)：当前论证不成立

### 固定 \(\varepsilon>0\)

在正确的 DeTurck gauge 和 transported coefficient 系统中，
\[
b_\varepsilon=a+\varepsilon^2\ge\varepsilon^2
\]
使主部严格抛物；\(-2b_\varepsilon g\) 是零阶项，不改变主符号。这一部分正确。

### 共同存在时间不能仅由 (2.2) 推出

当 \(\varepsilon\to0\) 时椭圆性常数退化。单个 \(L^p\) 曲率 Grönwall 不足以给出统一的固定坐标 \(C^{2,\alpha}\) 控制或共同存在时间。完整证明至少需要 Yang 型的：

- metric equivalence；
- cutoff jets；
- weighted curvature derivatives；
- connection difference 或 DeTurck coordinate bounds；

并需检查归一化项在整个系统中的影响，而不仅是零阶曲率能量。

### (4.4) 含有不可积项

文中使用
\[
\int_0^t \frac C{s}\,ds,
\]
该积分发散，不能推出短时间 metric equivalence，也不能推出随后声称的 \(C\sqrt t\) 初值连续性。“logarithmic integral”并不会趋于零。

需要另行建立在 \(t=0\) 附近可积的统一估计，例如
\[
\|b_\varepsilon\operatorname{Ric}\|_\infty
\le Cs^{-\alpha},\qquad \alpha<1,
\]
或直接由光滑初值获得统一短时界。文中未给出。

### 零集上的 \(O(\varepsilon^2)\) drift 不成立

在 \(\{\chi=0\}\) 上 \(b_\varepsilon=\varepsilon^2\)，而 weighted Moser 界只给出
\[
\varepsilon^2|\mathrm{Rm}_\varepsilon|\le C/t.
\]
于是
\[
\varepsilon^2|\operatorname{Ric}_\varepsilon|\le C/t,
\]
并非 \(C\varepsilon^2/t\)。因此无法由该估计推出
\[
|g_\varepsilon(t)-g_0|=O(\varepsilon^2).
\]

### weighted regularity 不推出界面光滑性

从
\[
\nabla^m(a\mathrm{Rm})\in L^p\quad\forall m,p,
\qquad g=g_0\text{ on }\{a=0\}
\]
不能推出 \(g\) 跨越 \(\partial\operatorname{supp}\chi\) 光滑。退化系数可以隐藏未加权导数的不匹配。例如平坦函数
\[
a(x)=
\begin{cases}
e^{-1/x^2},&x>0,\\
0,&x\le0,
\end{cases}
\qquad u=x_+
\]
满足 \(au\) 光滑，而 \(u\) 非 \(C^1\)。

故必须证明统一固定坐标导数界、connection jets 的匹配，或直接采用已完整证明的 degenerate DeTurck 构造。当前 §4.4 的 interior diagonal argument 只得到
\[
C^\infty_{\mathrm{loc}}(\{\chi>0\}\times(0,T]),
\]
不能处理零集边界。因此 Theorem 4.1 尚未证明。

## 4. bounded \(|\chi^2\mathrm{Rm}|\) 延拓

若已有 exact smooth solution 且
\[
|a\mathrm{Rm}|\le K,
\]
则 metric equivalence 可直接由
\[
|\partial_tg|_g
\le 2|a\operatorname{Ric}|_g+2|ag|_g
\le C_nK+2\sqrt n
\]
得到：
\[
e^{-C(K+1)t}g_0\le g(t)\le e^{C(K+1)t}g_0.
\]
无需在 \(\{\chi\ge\varepsilon_0\}\) 上除以 \(\chi^2\)。

归一化项在结构上与 Wang 框架兼容：

\[
\dot\Gamma_N\sim\nabla a,\qquad
\dot{\mathrm{Rm}}_N=-2a\mathrm{Rm}+g\owedge\nabla^2a,
\]
其高阶导数只产生当前阶线性反应、低阶曲率项以及 cutoff jets。因此归一化不产生新的最高阶空间导数。

但当前文本尚未完成：

1. 所有 \(\partial_t\nabla^m\) 的 connection commutators；
2. \(a\,\nabla^{m+2}a\) 等项与 cutoff-jet 层级的闭合；
3. 从 covariant \(L^p/C^k\) 控制到固定坐标下 endpoint metric 的光滑极限；
4. 跨 \(\partial\operatorname{supp}\chi\) 的 jet matching。

而 `step49_corrected_restricted_theorem_statement.md` §6.1 本身也明确承认任意阶 staggered induction 尚未完整写出。因此准确结论是：

> 归一化项与 Wang 的延拓机制结构兼容，但 `step49` 尚未证明 Theorem 5.1。

## 5. 正时间 slab 论证

这一逻辑本身正确，但以延拓定理和 Moser 界在整个 \((0,T^*)\) 上有效为前提。

若
\[
|a\mathrm{Rm}(t)|\le C\gamma/t,
\qquad 0<t<T^*,
\]
则在后半区间
\[
\sup_{[T^*/2,T^*)}|a\mathrm{Rm}|
\le \frac{2C\gamma}{T^*}<\infty.
\]
由于解在紧区间 \([0,T^*/2]\) 上光滑，
\[
\sup_{[0,T^*/2]}|a\mathrm{Rm}|<\infty.
\]
合并即得到 \([0,T^*)\) 上的统一有限界，可应用延拓准则。故 \(C\gamma/t\) 在 \(t=0\) 发散并非障碍，且这里没有内在循环论证。

不过，如果该 Moser 界来自 first-exit bootstrap，则必须确认其 bootstrap 假设对所有 \(t<T^*\) 保持成立；相关任意阶闭合在伴随材料中仍标为未完成。因此 slab deduction 是正确的**条件性结论**。

## 最终判定

1. **Christoffel 公式正确；曲率 Hessian 项符号应改为 \(+\)。**
2. **完整 \(L^p\) reaction 是 \((2p-n)\int b|\mathrm{Rm}|^p\)，不能称为耗散。**  
   但在 cutoff-jet 一致控制成立后，归一化仍只增加 \(\varepsilon\)-独立的 Grönwall 项。
3. **\(\varepsilon\)-regularized 方程逐个严格抛物，但共同存在时间及光滑 \(\varepsilon\to0\) 极限未由本文证明。** (4.4)、零集 drift 和界面光滑性推断均有实质错误。
4. **归一化与 Wang staggered framework 兼容，但任意阶延拓证明尚未闭合。**
5. **正时间 slab 论证正确，但依赖尚未建立的延拓准则和 Moser 前提。**

因此该笔记可以保留为“归一化项结构兼容性分析”，不能标记为已经建立 per-datum existence、smooth interface passage 或 extension theorem。
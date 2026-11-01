# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step37_base_pair_continuation.md",
    "Sessions/S0910A03/trace/ttcs/results/step37_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Read the actual Step 38 note, the corrected Step 37 base-pair file, the Step 37 TTCS integration, the shifted-curvature evolution source notes, A01's index-level curvature tensor derivation, and Wang's printed Section 4 source. Verify the new scientific assertion at the tensor-energy level: (i) a signed term J=∫χ ∇_i∇_jχ B^{ij}(V), with |B|≤C_p|V|^p and |∇B|≤C_p|V|^{p-1}|∇V|, is controlled by weighted diffusion plus ||dχ||∞²||V||_p^p; (ii) the actual m=2 term χ∇²χ*∇²U in the differentiated U equation really has this signed contraction structure after testing, so an evolving Hessian norm is unnecessary for this term; (iii) identify precisely which remaining general-m top-cutoff/lower-curvature contractions are not covered by this lemma and what finite-exponent induction would be needed. Check whether the repaired finite-Lp base estimate is valid without hidden L-infinity or division-by-a assumptions. Give explicit corrections rather than treating the extension theorem as established.

## Output

# 科学核验备忘录

## 总结

1. Step 38 的 signed Hessian-cutoff 引理在 \(p\ge 2\) 时成立。对
   \[
   J=\int_M\chi\,\nabla_i\nabla_j\chi\,B^{ij}(V)\,d\mu
   \]
   作一次分部积分，确实只需加权耗散
   \[
   D_{V,p}:=\int_M\chi^2|\nabla V|^2|V|^{p-2}\,d\mu
   \]
   和 \(\|d\chi\|_\infty^2\|V\|_p^p\)，不需要 \(\nabla^2\chi\) 的任何范数，也不需要除以 \(a=\chi^2\)。

2. 在 \(m=2\) 的 \(\nabla^2U\) 能量中，当前阶项
   \[
   \chi\nabla^2\chi*\nabla^2U
   \]
   经测试后确实是该 signed 形式。这里 \(B^{ij}\) 是
   \(|V|^{p-2}V\otimes V\) 的平行度量收缩，\(V=\nabla^2U\)。因此这个特定项不需要演化中的 Hessian 范数。相同机制其实适用于任意 \(m\) 的
   \(\chi\nabla^2\chi*\nabla^mU\) 当前阶项。

3. 修正后的 Step 37 给出的有限 \(L^p\) base-pair 估计成立，但须明确使用已独立取得的
   \[
   \sup_{t<T}\|T(t)\|_{L^p}<\infty .
   \]
   除题设中的 \(\|U\|_\infty\) 外，不出现 \(\|T\|_\infty\)、\(\|a\nabla\operatorname{Rm}\|_\infty\)、\(\|\nabla^2\chi\|_\infty\) 或除以 \(a\) 的步骤。

4. 该引理没有处理一般 \(m\) 中的最高 cutoff jet
   \(\nabla^{m+1}\chi,\nabla^{m+2}\chi\) 与低阶曲率因子的耦合。所需的当前阶组合是
   \[
   \bigl(\nabla^mU,\nabla^{m+1}\chi\bigr),
   \]
   随后再估计 \(\nabla^mT\)。Step 38 尚未给出这一组合在任意 \(m\) 下的逐项证明；Wang Section 4 的印刷论证也没有展示其中关键的 \(\nabla^{m+1}\chi\)-项如何处理。

---

## 1. signed Hessian-cutoff 引理

在固定时刻，闭流形上的散度积分为零，因此
\[
\begin{aligned}
J
&=\int_M\chi\,\nabla_i\nabla_j\chi\,B^{ij}\,d\mu\\
&=-\int_M\nabla_i\chi\,\nabla_j\chi\,B^{ij}\,d\mu
  -\int_M\chi\,\nabla_j\chi\,\nabla_iB^{ij}\,d\mu .
\end{aligned}
\]

由题设的两个点态估计，
\[
\begin{aligned}
|J|
&\le C_p\|d\chi\|_\infty^2\int|V|^p\\
&\quad+C_p\int|\chi|\,|d\chi|\,|V|^{p-1}|\nabla V|.
\end{aligned}
\]
第二项具有精确分解
\[
|\chi|\,|d\chi|\,|V|^{p-1}|\nabla V|
=
\bigl(|\chi||\nabla V||V|^{(p-2)/2}\bigr)
\bigl(|d\chi||V|^{p/2}\bigr).
\]
由于 \(|\chi|=\sqrt a\)，Young 不等式给出
\[
\boxed{
|J|
\le \varepsilon D_{V,p}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p.}
\]

这一步在 \(\{\chi=0\}\) 上仍是逐点成立的乘积估计，没有出现 \(\chi^2/a\)。

### 零集上的正则化

当 \(p\) 非偶数或 \(V\) 有零点时，可令
\[
\rho_\delta=(|V|^2+\delta^2)^{1/2},\qquad
P_\delta(V)=\rho_\delta^{p-2}V,
\]
并以 \(B_\delta=P_\delta(V)*V\) 代替 \(B\)。此时
\[
|B_\delta|\le C_p\rho_\delta^p,\qquad
|\nabla B_\delta|\le C_p\rho_\delta^{p-1}|\nabla V|.
\]
所得估计为
\[
|J_\delta|
\le\varepsilon\int\chi^2\rho_\delta^{p-2}|\nabla V|^2
+C_{p,\varepsilon}\|d\chi\|_\infty^2\int\rho_\delta^p,
\]
随后令 \(\delta\downarrow0\)。这补足了 Step 38 所称“标准 tensor-norm regularization”的细节。

若能量另含 \(\eta^2\)，分部积分还会产生
\[
-2\int\eta\,(\nabla_i\eta)\chi\,(\nabla_j\chi)B^{ij}.
\]
Step 38 的 stationary collar 假设使 \(\chi=0\) 于 \(\operatorname{supp}d\eta\)，因此该项消失；没有这一支撑关系时必须另行估计。

---

## 2. \(m=2\) 当前阶 Hessian 项的真实结构

`weighted_moser_and_continuation_repair.md` (2.6) 给出
\[
(\partial_t-a\Delta)U
=da*\nabla U+\nabla^2a*U+d\chi*d\chi*U
 +U*U+aG*U.
\]
对它取两次协变导数。令
\[
V=\nabla^2U.
\]
由前两项的乘积法则，包含当前阶 \(V\) 且 cutoff 总阶数为二的部分为有限个
\[
(\nabla^2a)*V.
\]
又因为
\[
\nabla_i\nabla_j a
=2\chi\,\nabla_i\nabla_j\chi
 +2\nabla_i\chi\,\nabla_j\chi,
\]
当前阶部分正是
\[
\chi\nabla^2\chi*V,\qquad d\chi*d\chi*V.
\]
这与 Step 27 (3.2)、Codex `shifted_curvature_continuation.md` (4.1) 中
\[
\alpha+\beta+\gamma=4,\qquad\gamma=2
\]
的分配完全一致。

设 \(\mathcal L^{ij}\) 是相应的平行代数收缩，则每一项经
\(P(V)=|V|^{p-2}V\) 测试后可写成
\[
\int\chi\,\nabla_i\nabla_j\chi\,
\underbrace{\langle P(V),\mathcal L^{ij}V\rangle}_{B^{ij}(V)}\,d\mu .
\]
由于 \(\nabla g=0\)，
\[
|B|\le C_p|V|^p,\qquad
|\nabla B|\le C_p|V|^{p-1}|\nabla V|.
\]
因此 Step 38 (2.6) 对这个当前阶项成立。

相邻两个当前阶项也按预期处理：
\[
\int P(V)*(d\chi*d\chi*V)
\le C\|d\chi\|_\infty^2\|V\|_p^p,
\]
以及
\[
\int P(V)*(\chi d\chi*\nabla V)
\le\varepsilon D_{2,p}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p.
\]

### 这里没有处理的 \(m=2\) 项

Step 38 (2.3) 应理解为“包含当前阶 \(V\) 的 high-cutoff 部分”，而不是完整的 \(m=2\) 方程。后者还包含例如
\[
\chi\nabla^4\chi*U,\qquad
d\chi*\nabla^3\chi*U,\qquad
\chi\nabla^3\chi*\nabla U,
\]
以及由
\[
\nabla^i a*\nabla^jU*\nabla^kT
\]
产生的
\[
\chi\nabla^2\chi*U*T.
\]
这些项的测试因子只有 \(|V|^{p-1}\)，或者含有额外的 \(U,T,\nabla U\)；它们不满足引理中只依赖 \(V\) 的两条 \(B\)-估计。它们需要低阶 \(U,T\) 和 cutoff jet 的有限指数估计。

A01 `step35_tensor_variation_and_hessian_a.md` (3.3)–(3.9) 提供了独立的同类张量机制：
\[
B_{\mathrm{curv}}^{pq}
=R^p{}_j{}^q{}_lE^{jl},\qquad
|\nabla B_{\mathrm{curv}}|
\le CF|\nabla\operatorname{Rm}|.
\]
这验证了“先保留 Hessian 的两个指标，再分部积分”的方法。\(m=2\) 的 \(U\)-能量结构则直接来自上述 \(U\) 方程，而不是仅由 A01 的曲率标量计算推出。

---

## 3. 修正后的 Step 37 base-pair

令
\[
W=\nabla U,\qquad \Theta=\nabla^2\chi,\qquad
D_{1,p}=\int\chi^2|\nabla W|^2|W|^{p-2}.
\]
Step 37 中 \(I_{1c}\) 和 \(I_3\) 经第二次分部积分后均满足
\[
|I_{1c}|+|I_3|
\le\varepsilon D_{1,p}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|W\|_p^p.
\]
其余混合项为
\[
K^2\|\Theta\|_p^2\|W\|_p^{p-2},
\qquad
K\|\Theta\|_p\|W\|_p^{p-1},
\]
并由 Young 转换为
\[
C_p(1+K^p)
\bigl(\|\Theta\|_p^p+\|W\|_p^p\bigr).
\]

由
\[
aT=U,\qquad
a\nabla T=W-da*T,\qquad
a\operatorname{Rm}=U-aG,
\]
涉及未加权曲率的项至多给出
\[
C K|W|+CK|d\chi||T|+C,
\]
所以在积分中只需 \(\|T\|_p\)，不需要其点态范数。

### cutoff Hessian 的精确演化

Step 37 §4 对 \(CK|\Theta|\) 来源的文字需要修正。固定标量 \(\chi\) 满足
\[
\partial_t\Theta_{ij}
=-(\partial_t\Gamma)^k{}_{ij}\nabla_k\chi.
\]
又因
\[
\partial_tg=-2\operatorname{Ric}(U),
\]
有
\[
\partial_t\Gamma
=g^{-1}*\nabla\operatorname{Ric}(U)
=g^{-1}*\operatorname{Ric}(W),
\]
从而
\[
|\partial_t\Theta|\le C|W||d\chi|.
\]
空间协变导数中不存在额外的 \(U*\Gamma\) 项。能量中的
\(CK\|\Theta\|_p^p\) 来自演化度量下的张量范数和体积元，因为
\[
|\partial_tg|\le C_nK.
\]
因此
\[
\frac d{dt}\|\Theta\|_p^p
\le C_pK\|\Theta\|_p^p
+C_p\|d\chi\|_\infty
  \|W\|_p\|\Theta\|_p^{p-1}.
\]

合并得到
\[
\frac d{dt}
\left(\|W\|_p^p+\|\Theta\|_p^p\right)
\le C_{p,K,g_0,\chi,T}
\left(
1+\|W\|_p^p+\|\Theta\|_p^p+\|T\|_p^p
\right).
\]
若 Step 27/Codex §6 的
\[
\sup_{t<T}\|T(t)\|_p<\infty
\]
已经独立取得，Grönwall 即给出修正后的 Step 37 结论。

这里使用的点态量只有题设中的 \(\|U\|_\infty\) 和由度量比较得到的
\(\|d\chi\|_\infty\)。所有有限 \(L^p\) 估计本身仍不能直接产生点态导数估计；后者需要下一空间阶的未加权 \(L^p\) 控制。

---

## 4. 一般 \(m\) 中尚未被引理处理的结构

记
\[
W_m=\nabla^mU,\qquad C_r=\nabla^r\chi,\qquad
P_m=|W_m|^{p-2}W_m.
\]
最高 cutoff 部分为
\[
\Gamma_1=\chi C_{m+2}*U,\quad
\Gamma_2=C_1C_{m+1}*U,\quad
\Gamma_3=\chi C_{m+1}*\nabla U,\quad
\Gamma_4=\chi C_1*\nabla W_m.
\]

\(\Gamma_4\) 由耗散吸收。引理只处理当前阶分配中的
\[
\chi C_2*W_m.
\]
它不处理下列结构。

### 4.1 \(\Gamma_1\) 留下的当前 cutoff jet

对 \(\Gamma_1\) 分部积分一次：
\[
\begin{aligned}
\int P_m*\Gamma_1
={}&-\int\nabla P_m*\chi C_{m+1}*U\\
&-\int P_m*C_1C_{m+1}*U\\
&-\int P_m*\chi C_{m+1}*\nabla U .
\end{aligned}
\]
前两项分别需要
\[
\varepsilon D_{m,p}
+C K^2\|C_{m+1}\|_p^2\|W_m\|_p^{p-2},
\]
和
\[
CK\|C_1\|_\infty
\|C_{m+1}\|_p\|W_m\|_p^{p-1}.
\]
因此 \(C_{m+1}\) 与 \(W_m\) 必须在同一指数 \(p\) 下组合估计。signed Hessian 引理不能降低这里的 \(m+1\) 阶 cutoff jet。

这也是 Wang Proposition 4.14 印刷论证中没有写出的项：其 \(\Gamma_1\) 分部积分必然产生
\[
\nabla P_m*\chi C_{m+1}*U.
\]
仅说明最后剩下 \(C_2C_mU\) 并不足以消去该项，除非另有逐指标抵消恒等式；所给来源没有展示这样的恒等式。

### 4.2 \(\Gamma_3\) 与第三个 descendant

将
\[
\int P_m*\chi C_{m+1}*\nabla U
\]
和 \(\Gamma_3\) 合并，再从 \(C_{m+1}\) 移去一个导数，得到
\[
\begin{aligned}
&-\int\nabla P_m*\chi C_m*\nabla U,\\
&-\int P_m*C_1C_m*\nabla U,\\
&-\int P_m*\chi C_m*\nabla^2U,
\end{aligned}
\]
外加协变导数换序产生的曲率收缩。

第一项满足
\[
\varepsilon D_{m,p}
+C\int|C_m|^2|\nabla U|^2|W_m|^{p-2}.
\]
第三项按 \(m\) 分三种情形：

- \(m=1\)：\(\nabla^2U=\nabla W_1\)，由耗散吸收；
- \(m=2\)：\(\nabla^2U=W_2\)，正是
  \(\chi\nabla^2\chi*W_2\) 的 signed Hessian 项；
- \(m\ge3\)：\(\nabla^2U\) 属于已有的较低空间阶，可用有限指数 Hölder 估计。

换序项含 \(\operatorname{Rm}=T-G\) 与较低 cutoff、\(U\) 导数。空间度量收缩本身不会产生导数，因为 \(\nabla g=0\)。

### 4.3 其余低阶曲率乘积

分化后的非线性部分包含
\[
\nabla^ia*\nabla^jU*\nabla^kT,
\qquad i+j+k=m,\quad k\le m-1.
\]
当 \(j=m\) 时，
\[
aW_m*T=W_m*U
\]
由 \(\|U\|_\infty\) 控制。其余情形都需要
\[
\nabla^jU\ (j<m),\qquad
\nabla^kT\ (k\le m-1),\qquad
C_r\ (r\le m)
\]
在充分大的有限指数中有界。这些不是 signed Hessian 引理的对象。

---

## 5. 所需有限指数组合

供应文件中的结构支持如下递推框架。

假设在第 \(m\) 阶之前，所有
\[
\nabla^jU\ (j<m),\qquad
C_r\ (r\le m),\qquad
\nabla^jT\ (j\le m-1)
\]
在每个有限 \(L^q\) 中已有界，并有 \(\|U\|_\infty\le K\)。

对固定 \(p\)：

1. 同时估计 \(W_m\) 与 \(C_{m+1}\)。cutoff 方程的唯一当前阶乘积是
   \[
   \partial_tC_{m+1}
   =W_m*C_1+\text{较低空间阶乘积}.
   \]
   与上面的两类
   \(C_{m+1}\)-项相配，Young 后得到
   \[
   \frac d{dt}
   \bigl(\|W_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
   \le C_{m,p}
   \bigl(1+\|W_m\|_p^p+\|C_{m+1}\|_p^p\bigr).
   \]

2. 以前一空间阶因子在 \(L^{4p}\) 或 \(L^{8p}\) 中的界处理乘积。例如
   \[
   \int |C_m|^2|\nabla U|^2|W_m|^{p-2}
   \]
   可由
   \[
   \|C_m\|_{4p}^2\|\nabla U\|_{4p}^2
   \|W_m\|_p^{p-2}\operatorname{Vol}(M)^{1/p}
   \]
   控制。含至多四个较低空间阶因子的项可将每个因子放入
   \(L^{8p}\)，无需使用它们的点态范数。

3. 得到 \(W_m,C_{m+1}\) 后，再估计 \(\nabla^mT\)。其代表性项为
   \[
   \int|C_{m+1}|^2|T|^2|\nabla^mT|^{p-2},
   \]
   和
   \[
   \int|W_m||T||\nabla^mT|^{p-1}.
   \]
   前者使用 \(C_{m+1},T\in L^{4p}\)，后者使用
   \(W_m,T\in L^{2p}\)。

这一指数安排解释了为何不需要较低空间阶的点态范数，也解释了为何估计顺序必须先组合
\((\nabla^mU,\nabla^{m+1}\chi)\)，再处理 \(\nabla^mT\)。

目前 Step 38 只写出了这一机制的关键局部修补和 \(m=2\) 当前阶项。任意 \(m\) 的完整结果还缺少：对分化后的每个收缩验证上述导数阶数、证明换序项只含 \(\nabla^jT\) 且 \(j\le m-1\)、以及从这些逐项估计推出统一的组合微分不等式。因此，signed Hessian 修补强化了 continuation 方案，但供应文件尚未从它推出完整的终端延拓定理。Step 38 的 K2–Y–Moser 结论仍应按其文字理解为光滑 first-exit 时间段上的条件性结果。
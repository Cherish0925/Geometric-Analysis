# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 38,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step38_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step38_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the actual Step 38 note, the corrected Step 37 base-pair file, the Step 37 TTCS integration, the shifted-curvature evolution source notes, A01's index-level curvature tensor derivation, and Wang's printed Section 4 source. Verify the new scientific assertion at the tensor-energy level: (i) a signed term J=∫χ ∇_i∇_jχ B^{ij}(V), with |B|≤C_p|V|^p and |∇B|≤C_p|V|^{p-1}|∇V|, is controlled by weighted diffusion plus ||dχ||∞²||V||_p^p; (ii) the actual m=2 term χ∇²χ*∇²U in the differentiated U equation really has this signed contraction structure after testing, so an evolving Hessian norm is unnecessary for this term; (iii) identify precisely which remaining general-m top-cutoff/lower-curvature contractions are not covered by this lemma and what finite-exponent induction would be needed. Check whether the repaired finite-Lp base estimate is valid without hidden L-infinity or division-by-a assumptions. Give explicit corrections rather than treating the extension theorem as established.

## Integrated Scientific Memo

# Tensor-energy 核验结论

## 1. Signed Hessian-cutoff 引理成立

设 \(p\ge 2\)，
\[
J=\int_M \chi\,\nabla_i\nabla_j\chi\,B^{ij}(V)\,d\mu,
\]
且
\[
|B(V)|\le C_p|V|^p,\qquad
|\nabla B(V)|\le C_p|V|^{p-1}|\nabla V|.
\]
在闭流形上，对向量场
\[
X^i=\chi\,\nabla_j\chi\,B^{ij}
\]
使用散度定理，精确得到
\[
J=-\int \nabla_i\chi\,\nabla_j\chi\,B^{ij}
  -\int\chi\,\nabla_j\chi\,\nabla_iB^{ij}.
\]
这里没有曲率交换子。于是
\[
\begin{aligned}
|J|
&\le C_p\|d\chi\|_\infty^2\int |V|^p\\
&\quad+C_p\int |\chi|\,|d\chi|\,|V|^{p-1}|\nabla V|.
\end{aligned}
\]
利用
\[
|\chi|\,|d\chi|\,|V|^{p-1}|\nabla V|
=
\bigl(|\chi||\nabla V||V|^{(p-2)/2}\bigr)
\bigl(|d\chi||V|^{p/2}\bigr)
\]
和 Young 不等式，
\[
\boxed{
|J|\le
\varepsilon\int\chi^2|\nabla V|^2|V|^{p-2}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\int |V|^p.}
\]

此证明不使用 \(\nabla^2\chi\) 的范数，也不形成 \(1/a\)。当 \(V=0\) 或 \(p\) 非偶数时，可用
\[
\rho_\delta=(|V|^2+\delta^2)^{1/2},\qquad
B_\delta=\rho_\delta^{p-2}V*V
\]
正则化，再令 \(\delta\downarrow0\)。

若积分另带辅助 cutoff \(\eta^2\)，分部积分会额外产生
\[
-2\int \eta\,\nabla_i\eta\,\chi\nabla_j\chi\,B^{ij}.
\]
只有在 \(\chi=0\) 于 \(\operatorname{supp}d\eta\) 的 stationary collar 设置下该项自动消失；否则必须单独估计。

---

## 2. \(m=2\) 的当前阶 Hessian 项确有该 signed 结构

由
\[
(\partial_t-a\Delta)U
=da*\nabla U+\nabla^2a*U+d\chi*d\chi*U
 +U*U+aG*U,
\qquad a=\chi^2,
\]
取两次协变导数，令
\[
V=\nabla^2U.
\]
包含当前阶 \(V\) 且 cutoff 总阶为二的部分为
\[
(\nabla^2a)*V
=
2\chi\nabla^2\chi*V+2d\chi*d\chi*V.
\]
此外主算子及一阶 cutoff 项产生
\[
\chi\,d\chi*\nabla V.
\]

对 \(\chi\nabla^2\chi*V\) 用
\[
P(V)=|V|^{p-2}V
\]
测试后，每个通用收缩都可写成
\[
\int\chi\,\nabla_i\nabla_j\chi\,B^{ij}(V),
\qquad
B^{ij}(V)=\langle P(V),\mathcal L^{ij}V\rangle,
\]
其中 \(\mathcal L^{ij}\) 是由平行度量组成的代数收缩。因 \(\nabla g=0\)，
\[
|B|\le C_p|V|^p,\qquad
|\nabla B|\le C_p|V|^{p-1}|\nabla V|.
\]
因此
\[
\boxed{
\left|\int |V|^{p-2}V*(\chi\nabla^2\chi*V)\right|
\le \varepsilon D_{2,p}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p,}
\]
其中
\[
D_{2,p}=\int\chi^2|\nabla V|^2|V|^{p-2}.
\]
故这个特定项不需要演化中的 \(\|\nabla^2\chi\|_4\) 或其他 Hessian 范数。

相邻两项分别满足
\[
\int P(V)*(d\chi*d\chi*V)
\le C\|d\chi\|_\infty^2\|V\|_p^p,
\]
及
\[
\int P(V)*(\chi d\chi*\nabla V)
\le \varepsilon D_{2,p}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p.
\]

A01 的指标计算
\[
B_{\rm curv}^{pq}=R^p{}_j{}^q{}_lE^{jl},\qquad
|\nabla B_{\rm curv}|\le CF|\nabla\operatorname{Rm}|
\]
独立验证了“保留 Hessian 两个指标后再分部积分”的机制，但 \(m=2\) 的上述结论本身应从 \(U\)-方程推出，而不能仅由该标量曲率计算推断。

### 必须限定结论范围

上述三项只是 \(m=2\) 方程中“含当前阶 \(V\)”的 high-cutoff 部分；完整 \(m=2\) 方程还含
\[
\chi\nabla^4\chi*U,\qquad
d\chi*\nabla^3\chi*U,\qquad
\chi\nabla^3\chi*\nabla U,
\]
以及含低阶 \(T,U\) 因子的非线性收缩。单-Hessian 引理并不控制这些项。

---

## 3. 修正后的 Step 37 finite-\(L^p\) base pair 有效

令
\[
W=\nabla U,\qquad \Theta=\nabla^2\chi,\qquad
D_{1,p}=\int\chi^2|\nabla W|^2|W|^{p-2}.
\]
Step 37 原始版本对 \(I_{1c}\) 和 \(I_3\) 的绝对值估计有幂次错误：两者原始大小都是
\[
\int |\chi|\,|\Theta|\,|W|^p,
\]
而非总次数为 \(p\) 的普通 Hölder 乘积。修正方法是保留指标收缩，将两者均写成
\[
\int\chi\,\nabla_i\nabla_j\chi\,B^{ij}(W)
\]
并应用上述引理：
\[
|I_{1c}|+|I_3|
\le \varepsilon D_{1,p}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|W\|_p^p.
\]

其余真正的耦合项为
\[
K^2\|\Theta\|_p^2\|W\|_p^{p-2},
\qquad
K\|\Theta\|_p\|W\|_p^{p-1},
\]
而 Young 不等式分别给出
\[
K^2\|\Theta\|_p^2\|W\|_p^{p-2}
\le CK^p\|\Theta\|_p^p+C\|W\|_p^p,
\]
\[
K\|\Theta\|_p\|W\|_p^{p-1}
\le CK^p\|\Theta\|_p^p+C\|W\|_p^p.
\]

未加权曲率项可由
\[
a\nabla T=W-da*T,\qquad
a\operatorname{Rm}=U-aG
\]
改写，故只出现有限 \(L^p\) 源 \(\|T\|_p^p\)，不需要
\[
\|T\|_\infty
\quad\text{或}\quad
\|a\nabla\operatorname{Rm}\|_\infty
\]
作为 Grönwall 系数。

### cutoff Hessian 演化的文字修正

固定标量 \(\chi\) 满足
\[
\partial_t(\nabla_i\nabla_j\chi)
=-(\partial_t\Gamma)^k{}_{ij}\nabla_k\chi.
\]
由
\[
\partial_tg=-2\operatorname{Ric}(U)
\]
及度量相容性，
\[
\partial_t\Gamma
=g^{-1}*\nabla\operatorname{Ric}(U)
=g^{-1}*\operatorname{Ric}(\nabla U),
\]
所以
\[
|\partial_t\Theta|\le C|W||d\chi|.
\]
Step 37 中所称空间项 \(U*\Gamma\) 不是正确来源。能量中的
\[
CK\|\Theta\|_p^p
\]
来自演化度量下的张量范数及体积元变化，因为
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

合并后
\[
\frac d{dt}
\bigl(\|W\|_p^p+\|\Theta\|_p^p\bigr)
\le C_{p,K,g_0,\chi,T}
\bigl(1+\|W\|_p^p+\|\Theta\|_p^p+\|T\|_p^p\bigr).
\]

### \(\|T\|_p\) 输入本身无隐藏假设

测试
\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T)
\]
时，唯一表面需要 Hessian 控制的项可分部积分为
\[
C\int |\nabla a|\,|\nabla T|\,|T|^{p-1}.
\]
使用处处成立的
\[
|\nabla a|=2|\chi||d\chi|
\]
直接 Young：
\[
\le \varepsilon\int\chi^2|\nabla T|^2|T|^{p-2}
+C_\varepsilon\|d\chi\|_\infty^2\int|T|^p.
\]
反应项由 \(a|T|=|U|\le K\) 控制。因此
\[
\sup_{t<T}\|T(t)\|_p<\infty
\]
对每个固定有限 \(p\) 确实可从 \(\|U\|_\infty\) 推出，不需要 \(\|T\|_\infty\)。

故修正后的结论是：
\[
\boxed{
\sup_{t<T}
\left(\|\nabla U(t)\|_{L^p}
+\|\nabla^2\chi(t)\|_{L^p}\right)<\infty
\quad (p\ge2).}
\]
较小正指数可由高指数界及有限体积推出。

这只是 finite-\(L^p\) base estimate。退化耗散仅控制
\[
\chi\nabla |W|^{p/2},
\]
不能由“所有有限 \(L^p\) 界”直接升级到 \(L^\infty\)。

---

## 4. 一般 \(m\) 尚未由该引理覆盖的项

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

- \(\Gamma_4\) 由扩散直接吸收。
- 引理处理的是当前阶分配
  \[
  \chi C_2*W_m,
  \]
  而不是任意最高 cutoff jet。

### 4.1 \(\Gamma_1\) 产生不可消去的 \(C_{m+1}\)

一次分部积分给出
\[
\begin{aligned}
\int P_m*\Gamma_1
={}&-\int\nabla P_m*\chi C_{m+1}*U\\
&-\int P_m*C_1C_{m+1}*U\\
&-\int P_m*\chi C_{m+1}*\nabla U.
\end{aligned}
\]
前两项分别留下
\[
\varepsilon D_{m,p}
+CK^2\|C_{m+1}\|_p^2\|W_m\|_p^{p-2},
\]
以及
\[
CK\|C_1\|_\infty
\|C_{m+1}\|_p\|W_m\|_p^{p-1}.
\]
因此 \(\nabla^{m+1}\chi\) 必须与 \(\nabla^mU\) 在当前层共同估计。

这正是 Wang Proposition 4.14 印刷论证中没有展示的项。其文字只列出最终 residual
\[
\nabla^2\chi*\nabla^m\chi*U,
\]
但直接对 \(\Gamma_1\) 分部积分必然产生
\[
\nabla P_m*\chi\nabla^{m+1}\chi*U.
\]
除非另有逐指标抵消恒等式，而给定来源没有提供该恒等式，否则不能声称 \(U_m\) 只依赖 cutoff jets 至 \(m\) 阶。

### 4.2 \(\Gamma_3\) 的 descendants

从 \(C_{m+1}\) 再移去一个导数，会产生
\[
\begin{aligned}
&-\int\nabla P_m*\chi C_m*\nabla U,\\
&-\int P_m*C_1C_m*\nabla U,\\
&-\int P_m*\chi C_m*\nabla^2U,
\end{aligned}
\]
以及协变换序项。

第一项留下
\[
\varepsilon D_{m,p}
+C\int |C_m|^2|\nabla U|^2|W_m|^{p-2}.
\]
第三项按阶数区分：

- \(m=1\)：\(\nabla^2U=\nabla W_1\)，由耗散吸收；
- \(m=2\)：\(\nabla^2U=W_2\)，正是本次已修复的 signed Hessian 项；
- \(m\ge3\)：\(\nabla^2U\) 是较低空间阶，但仍需有限高指数 Hölder 控制。

换序项含低阶 \(T\)-导数，不属于单-Hessian 引理。

### 4.3 非线性低阶曲率收缩

一般还有
\[
\nabla^ia*\nabla^jU*\nabla^kT,
\qquad i+j+k=m,\quad k\le m-1.
\]
当 \(j=m\) 时可用
\[
aW_m*T=W_m*U
\]
和 \(\|U\|_\infty\) 控制；其余情况需要
\[
\nabla^jU\ (j<m),\quad
\nabla^kT\ (k\le m-1),\quad
C_r\ (r\le m)
\]
的有限高指数界。这些均不由 signed Hessian 引理处理。

---

## 5. 所需的 finite-exponent induction

可行的依赖顺序应是
\[
\boxed{
(\nabla^mU,\nabla^{m+1}\chi)\ \text{先作当前阶组合估计},
\qquad
\nabla^mT\ \text{随后估计}.}
\]

假设所有较低空间阶 \(U,T,\chi\) 已在每个有限 \(L^q\) 中有界。对固定 \(p\)：

1. **组合当前阶。** cutoff 方程中唯一当前阶项是
   \[
   \partial_tC_{m+1}=W_m*C_1+\text{lower terms}.
   \]
   使用正则化变量
   \[
   \mathcal X_{m,p}
   =(\varepsilon+\|W_m\|_p^p)^{2/p},\qquad
   \mathcal Z_{m+1,p}
   =(\varepsilon+\|C_{m+1}\|_p^p)^{2/p},
   \]
   上述二次、双线性项转化为
   \[
   C\mathcal Z,\qquad
   C\mathcal X^{1/2}\mathcal Z^{1/2}
   \le C(\mathcal X+\mathcal Z).
   \]
   目标不等式是
   \[
   (\mathcal X_{m,p}+\mathcal Z_{m+1,p})'
   \le C_{m,p}(1+\mathcal X_{m,p}+\mathcal Z_{m+1,p}).
   \]

2. **较低阶乘积的指数安排。** 例如
   \[
   \int |C_m|^2|\nabla U|^2|W_m|^{p-2}
   \]
   可用 \(C_m,\nabla U\in L^{4p}\) 控制；含至多四个较低阶因子的项，可将每个置于 \(L^{8p}\)。这不形成当前阶的无限指数链，因为归纳假设已给出较低空间阶的所有有限指数。

3. **随后估计 \(T_m=\nabla^mT\)。** 代表性最坏项为
   \[
   \int |C_{m+1}|^2|T|^2|T_m|^{p-2},
   \]
   使用 \(C_{m+1},T\in L^{4p}\)；以及
   \[
   \int |W_m||T||T_m|^{p-1},
   \]
   使用 \(W_m,T\in L^{2p}\)，因为
   \[
   \frac1{2p}+\frac1{2p}+\frac{p-1}{p}=1.
   \]

该框架与来源中的导数计数相容，但供应文件尚未逐一验证任意 \(m\) 下所有收缩、换序项和 \(G\)-项均满足这些模板。因此它目前是可信的 induction blueprint，不是已完成的 extension theorem。

---

## 6. 必须写入后续版本的明确修正

1. 删除所有在 \(\{a=0\}\) 上书写
   \[
   \chi^2/a=1,\qquad |\nabla a|^2/a=4|d\chi|^2
   \]
   的点态表达；统一改用
   \[
   |\chi|=\sqrt a,\qquad |\nabla a|=2|\chi||d\chi|
   \]
   的无除法 Young 分解。

2. 修正 \(\Theta=\nabla^2\chi\) 演化中 \(CK|\Theta|\) 的来源：它来自演化范数和体积，不来自不存在的空间 \(U*\Gamma\) 项。

3. 将 Step 38 的 \(m=2\) 结论限定为当前阶
   \[
   \chi\nabla^2\chi*\nabla^2U
   \]
   项；不能据此声称完整 \(m=2\) 层已闭合。

4. 修正 Wang 式依赖图：\(U_m\) 确实需要 \(C_{m+1}\)，故应采用同阶 pair，而非声称 cutoff 只需至 \(m\) 阶。

5. 不得把 Step 27、Step 38 或现有 Codex memo 引为完整延拓定理。尚缺的精确数学对象是：
   - 任意 \(m\) 的逐收缩组合能量不等式；
   - 所有协变换序项的低阶 \(T\)-导数审计；
   - 先 \((U_m,C_{m+1})\)、后 \(T_m\) 的完整 finite-exponent induction；
   - 终端 transported-coefficient DeTurck restart 的独立存在性验证。

**最终判定：** 断言 (i)、(ii) 成立；修正后的 Step 37 finite-\(L^p\) base estimate 成立，且无隐藏的曲率 \(L^\infty\) 或除以 \(a\) 假设。断言 (iii) 只能给出上述明确的剩余项与归纳框架，现有材料尚不足以宣布完整 smooth extension theorem。
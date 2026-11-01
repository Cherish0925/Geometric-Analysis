# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 37,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step37_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step37_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 37 base-pair continuation estimate for (∇U, ∇²χ) in the normalized cutoff flow ∂_tg = -2a(Ric+g), a=χ², with U=a(Rm+G). The note claims that assuming sup|U|<∞ on [0,T), the four dangerous terms R_1=χ∇³χ*U, R_2=∇χ*∇²χ*U, R_3=χ∇²χ*∇U, R_4=χ∇χ*∇²U can be handled in the L^p energy of W=∇U by: (i) integrating by parts on R_1 to produce three terms I_{1a}, I_{1b}, I_{1c}, using the χ factor to match diffusion a=χ²; (ii) absorbing I_{1a} via Young with the identity χ²/a=1; (iii) treating R_4 via χ≤√a and Young; (iv) coupling to the Θ=∇²χ evolution via the cutoff-jet equation ∂_tΘ ~ K|Θ| + |W||∇χ|; (v) closing by Gronwall for Y_1=||W||_p^p+||Θ||_p^p with only the known inhomogeneity ||T||_p^p from Step 27 §5. Check whether: (a) the IBP in eq (3.3)-(3.4) correctly produces all three product-rule terms; (b) the χ²/a=1 identity is valid at a=0 (where both vanish); (c) the R_4 estimate does not lose a derivative; (d) the Young conversion from mixed powers in (3.15) to (3.16) is valid; (e) no hidden ||T||_∞ or ||a∇Rm||_∞ coefficient appears; (f) the Gronwall constant C_1(p,K,g_0,χ,T) is indeed finite for each fixed smooth datum.

## Integrated Scientific Memo

# Step 37 核验结论

**结论：Step 37 按现文不能成立。**  
其目标——对每个固定 \(p\ge2\) 得到
\[
\sup_{t<T}\bigl(\|\nabla U(t)\|_{L^p}+\|\nabla^2\chi(t)\|_{L^p}\bigr)<\infty
\]
——可以通过局部修补得到，但 (3.9)、(3.11) 对 \(I_{1c}\)、\(I_3\) 的幂次计算错误，因而现文的 (3.15) 并未由前文推出。正确修补是对这两个 \(\chi\nabla^2\chi\)-型项再作一次分部积分。

以下令
\[
W=\nabla U,\qquad \Theta=\nabla^2\chi,\qquad
P(W)=|W|^{p-2}W,
\]
并记
\[
D_p=\int_M a|\nabla W|^2|W|^{p-2}\,d\mu,\qquad a=\chi^2.
\]

## 1. \(R_1\) 的第一次分部积分

对
\[
I_1=\int_M P(W)*\chi U*\nabla\Theta\,d\mu
\]
在闭流形上分部积分，导数恰好落在三个因子上：
\[
\begin{aligned}
I_1={}&-\int \Theta*\chi U*\nabla P(W)\\
&-\int \Theta*d\chi*U*P(W)\\
&-\int \Theta*\chi W*P(W).
\end{aligned}
\]
因此 (3.3)–(3.4) 的三个乘积法则项 \(I_{1a},I_{1b},I_{1c}\) 是完整的；这里没有遗漏第四项，也不因这一次散度运算产生曲率交换子。

前两个估计为
\[
|I_{1a}|
\le \varepsilon D_p+
C_{p,\varepsilon}K^2\int |\Theta|^2|W|^{p-2},
\]
以及
\[
|I_{1b}|
\le CK\|d\chi\|_\infty
\|\Theta\|_p\|W\|_p^{p-1}.
\]
并且
\[
\int |\Theta|^2|W|^{p-2}
\le \|\Theta\|_p^2\|W\|_p^{p-2}.
\]

## 2. 不应在 \(a=0\) 处书写 \(\chi^2/a=1\)

\(\chi^2/a\) 在 \(\{a=0\}\) 上字面上未定义。正确且更强的论证完全不需要除以 \(a\)：
\[
\begin{aligned}
&K|\chi||\Theta||W|^{p-2}|\nabla W|\\
&\quad =
K\bigl(\sqrt a|\nabla W||W|^{(p-2)/2}\bigr)
 \bigl(|\Theta||W|^{(p-2)/2}\bigr)\\
&\quad\le
\varepsilon a|\nabla W|^2|W|^{p-2}
+C_\varepsilon K^2|\Theta|^2|W|^{p-2}.
\end{aligned}
\]
这在所有点都成立，包括 \(a=0\)。

对每个 \(t<T\)，由光滑性也确有
\[
W=\nabla(aT)=da*T+a\nabla T=0
\quad\text{于 }\{\chi=0\},
\]
因为 \(a=da=0\)；但该事实并非上述 Young 估计所需，且不能使未定义的商本身成为点态恒等式。

## 3. 现文的关键幂次错误

### \(I_{1c}\)

因为 \(\nabla U=W\)，
\[
|P(W)|\,|\nabla U|=|W|^{p-1}|W|=|W|^p.
\]
故正确的原始项是
\[
|I_{1c}|\le C\int |\chi|\,|\Theta|\,|W|^p,
\]
而不是 (3.9) 的
\(\|\Theta\|_p\|W\|_p^{p-1}\)。

### \(I_3\)

同样，
\[
R_3=\chi\Theta*W
\]
在能量中给出
\[
|I_3|\le C\int |\chi|\,|\Theta|\,|W|^p.
\]
(3.11) 所写的
\[
\int |\Theta||W|^p
\le \|\Theta\|_p\|W\|_p^p
\]
是错误的；Hölder 实际给出
\[
\|\Theta\|_p\,
\|W\|_{p^2/(p-1)}^p.
\]
若保留该原始估计，就会出现总次数 \(p+1\) 的超线性项，不能推出线性 Grönwall 不等式。因此现文的 (3.15) 与 (3.9)、(3.11) 不一致。

## 4. 对 \(I_{1c}\) 和 \(I_3\) 的统一修补

两项均可写成有限个如下形式的收缩：
\[
J=\int_M \chi\,\nabla_i\nabla_j\chi\,
B^{ij}(W)\,d\mu,
\]
其中经过标准的
\((|W|^2+\delta)^{(p-2)/2}\) 正则化后，
\[
|B(W)|\le C_p|W|^p,\qquad
|\nabla B(W)|\le C_p|W|^{p-1}|\nabla W|.
\]
从 Hessian 上移去一个导数：
\[
J
=-\int \nabla_i\chi\nabla_j\chi\,B^{ij}(W)
-\int \chi\nabla_j\chi\,\nabla_iB^{ij}(W).
\]
于是
\[
\begin{aligned}
|J|
&\le C_p\|d\chi\|_\infty^2\int |W|^p\\
&\quad+C_p\int |\chi||d\chi|
|W|^{p-1}|\nabla W|\\
&\le \varepsilon D_p+
C_{p,\varepsilon}\|d\chi\|_\infty^2\int |W|^p.
\end{aligned}
\]
故 \(I_{1c}\) 和 \(I_3\) 都应如此处理，而不是直接用
\(\|\Theta\|_p\) 做 Hölder。该修补不引入新的 Hessian 范数。

## 5. \(R_4\) 不丢失导数

由于 \(W=\nabla U\)，按固定导数次序可将
\[
\nabla^2U=\nabla W.
\]
因此
\[
\begin{aligned}
|I_4|
&\le C\int |\chi||d\chi||\nabla W||W|^{p-1}\\
&\le \varepsilon D_p+
C_{p,\varepsilon}\|d\chi\|_\infty^2\int |W|^p.
\end{aligned}
\]
二阶导数被加权耗散吸收，没有留下未控制的 \(\nabla^2U\)。

若为统一指标次序而交换协变导数，交换子是
\(\operatorname{Rm}*U\)。其中已有的 \(a\)-因子可用
\[
a\operatorname{Rm}=U-aG
\]
处理，或者剩余项作为 \(K|T|\) 的有限 \(L^p\) 源处理；无需
\(\|T\|_\infty\)。

## 6. 修正后的 \(W\)-能量

在上述处理后，真正得到的是
\[
\begin{aligned}
\frac d{dt}\|W\|_p^p
\le{}&
C_pK^2\|\Theta\|_p^2\|W\|_p^{p-2}\\
&+C_pK\|\Theta\|_p\|W\|_p^{p-1}\\
&+C_p(1+K^p)\|W\|_p^p
+C_p(1+K^p)\|T\|_p^p+C_p .
\end{aligned}
\]
这里第二行的真正耦合项来自 \(I_{1b}\)、\(R_2\) 等；\(I_{1c}\) 和 \(I_3\) 已变成耗散项与 \(\|W\|_p^p\)。

Young 转换是正确的：
\[
K^2\|\Theta\|_p^2\|W\|_p^{p-2}
\le C K^p\|\Theta\|_p^p+C\|W\|_p^p,
\]
对应指数 \(p/2,p/(p-2)\)，以及
\[
K\|\Theta\|_p\|W\|_p^{p-1}
\le CK^p\|\Theta\|_p^p+C\|W\|_p^p,
\]
对应指数 \(p,p/(p-1)\)。因此修正后确有
\[
\frac d{dt}\|W\|_p^p
\le C_p(1+K^p)
\bigl(1+\|W\|_p^p+\|\Theta\|_p^p+\|T\|_p^p\bigr).
\]

## 7. cutoff jet 方程

精确恒等式是
\[
\partial_t\Gamma
=g^{-1}*\nabla\operatorname{Ric}(U)
=g^{-1}*\operatorname{Ric}(W),
\]
因为 Ricci 收缩使用的度量对当前联络平行。因此对固定标量 \(\chi\)，
\[
|\partial_t\Theta|\le C|W||d\chi|.
\]
演化范数和体积元产生由
\(|\partial_tg|\le CK\) 控制的项，故
\[
\frac d{dt}\|\Theta\|_p^p
\le C_pK\|\Theta\|_p^p
+C_p\|d\chi\|_\infty
\|W\|_p\|\Theta\|_p^{p-1},
\]
进而
\[
\frac d{dt}\|\Theta\|_p^p
\le C_p(1+K)
\bigl(\|\Theta\|_p^p+\|W\|_p^p\bigr).
\]

Step 37 §4 所称的“\(U*\Gamma\)”并非正确来源：\(\nabla\operatorname{Ric}(U)\) 没有这种额外空间低阶修正。\(CK\|\Theta\|_p^p\) 实际来自演化度量下的范数和体积变化。

## 8. 不出现隐藏的点态曲率系数

关键代数恒等式为
\[
a\nabla T=W-da*T,
\]
且 \(\nabla T=\nabla\operatorname{Rm}\)。所以
\[
a\nabla\operatorname{Rm}*U
=(W-da*T)*U,
\]
其大小由
\[
K|W|+CK|d\chi||T|
\]
控制。类似地，
\[
a\operatorname{Rm}*W=(U-aG)*W,\qquad
(\partial_t\Gamma)*U=W*U.
\]
因此能量估计中只需：

- \(|U|\le K\)；
- \(\|d\chi\|_\infty<\infty\)；
- Step 27 (5.4) 的有限 \(\|T\|_{L^p}\)；

不需要
\[
\|T\|_\infty
\quad\text{或}\quad
\|a\nabla\operatorname{Rm}\|_\infty
\]
作为 Grönwall 系数。

## 9. Grönwall 与常数的有限性

令
\[
Y_1=\|W\|_p^p+\|\Theta\|_p^p.
\]
修正后
\[
Y_1'(t)
\le C_1\bigl(1+Y_1(t)+\|T(t)\|_p^p\bigr).
\]
因此
\[
Y_1(t)\le e^{C_1t}
\left[
Y_1(0)+C_1\int_0^t
\bigl(1+\|T(s)\|_p^p\bigr)\,ds
\right].
\]

对每个固定光滑 datum：

- \(|\partial_tg|_g\le C_nK\) 在有限时间上给出统一度量与体积比较；
- 因而 \(\|d\chi\|_{\infty,g(t)}\) 有界；
- \(Y_1(0)<\infty\)；
- 若 Step 27 (5.4) 已独立成立，则
  \(\sup_{t<T}\|T(t)\|_p<\infty\)。

所以 \(C_1(p,K,g_0,\chi,T)\) 及非齐次时间积分均有限。直接能量论证覆盖 \(p\ge2\)；更小的有限指数可由任一更高 \(L^q\) 界和统一体积界推出。

## 最终判定

对题中六点：

1. **(a)** 第一次 IBP 的三个乘积项完整正确。  
2. **(b)** \(\chi^2/a=1\) 不能在 \(a=0\) 处作为字面恒等式；应改用 \(|\chi|=\sqrt a\) 的无除法 Young 分解。  
3. **(c)** \(R_4\) 不丢失导数。  
4. **(d)** (3.15)\(\to\)(3.16) 的 Young 指数本身正确，但现文的 (3.15) 因错误处理 \(I_{1c},I_3\) 而未被推出；经第二次 IBP 后成立。  
5. **(e)** 展开上述恒等式后，不出现隐藏的 \(\|T\|_\infty\) 或 \(\|a\nabla\operatorname{Rm}\|_\infty\)。  
6. **(f)** 在 Step 27 (5.4) 已成立的条件下，每个固定光滑 datum 的 Grönwall 常数和非齐次项均有限。

另需删除 Step 37 §6 中“仅由所有有限 \(L^p\) 界和 \(p>n\) 即得 \(L^\infty\)”的陈述：Sobolev 嵌入需要 \(W^{1,p}\) 控制，而当前仅有 \(L^p\) 与时间积分的退化加权梯度耗散。修正后的 Step 37 严格证明的是**有限 \(L^p\) base-pair 估计**；点态升级及完整延拓仍依赖后续高阶 induction 的独立验证。
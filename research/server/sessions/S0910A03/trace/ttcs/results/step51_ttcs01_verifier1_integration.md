# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 51,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step51_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step51_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the precise L^p curvature energy estimate for the normalized cutoff flow ∂_tg = -2χ²(Ric+g). The note claims three specific things: (1) The conformal variation of |Rm|²_g under h₂ = -2ag gives +4a|Rm|² - 2⟨Rm, g∧∇²a⟩, where the +4a comes from the metric-inverse variation (4 factors of g^{-1}, each contributing +2a, minus 4a from the tensor inner product -2a|Rm|²). (2) Combined with the volume evolution ∂_t dμ = -a(s+n)dμ, the net normalization addition to d/dt ∫|Rm|^p is (2p-n)∫a|Rm|^p + bounded source. (3) At the critical exponent p=n/2, the reaction coefficient (2·n/2 - n) = 0 vanishes exactly. Check the sign conventions, count the g^{-1} factors, verify the Kulkarni-Nomizu trace, and confirm that Yang's Theorem A.7 Moser iteration is structurally compatible with the modified inequality (bounded Grönwall coefficient at supercritical p, bounded source from g∧∇²a). Read Yang's Theorem A.7 display and the conformal variation formula.

## Integrated Scientific Memo

## 核验结论

三项核心代数结论中：

1. \(+4a|\mathrm{Rm}|^{2}\) 的反应项正确；
2. 归一化相对于 Yang 非归一化流给出的净 \(L^{p}\) 反应系数确为 \(2p-n\)；
3. 在 \(p=n/2\) 时该系数严格消失。

但原笔记有两个符号错误，并且把 Yang 的齐次 Moser 迭代直接推广到含加性 Hessian 源的情形尚未证明。因此，笔记的核心恒等式成立，而其 Theorem 5.1 目前不能由所写论证推出。

### 1. 共形变分及逆度量计数

只考虑
\[
\dot g=h_2=-2ag,\qquad a=\chi^2.
\]
写成 \(\dot g=2\dot u\,g\)，则 \(\dot u=-a\)。在 Yang/Hamilton 的曲率约定下，完全降指标曲率满足
\[
\dot R_{ijkl}
=
2\dot u\,R_{ijkl}
-(g\owedge\nabla^2\dot u)_{ijkl},
\]
故
\[
\boxed{
\dot R_{ijkl}\big|_{h_2}
=
-2aR_{ijkl}+(g\owedge\nabla^2a)_{ijkl}.}
\]
因此笔记 (1.2) 中 Hessian 项的负号应改为正号。平坦二维检验可固定此符号：若
\[
g(t)=e^{-2ta}(dx^2+dy^2),
\]
则
\[
\dot R_{1212}=\Delta a
=(g\owedge\nabla^2a)_{1212}.
\]

另一方面，
\[
|\mathrm{Rm}|^2
=
g^{ia}g^{jb}g^{kc}g^{ld}R_{ijkl}R_{abcd},
\qquad
\dot g^{ij}=2ag^{ij}.
\]
四个 \(g^{-1}\) 因子共贡献
\[
4(2a)|\mathrm{Rm}|^2=8a|\mathrm{Rm}|^2.
\]
两个曲率张量的变分贡献
\[
2\langle\mathrm{Rm},-2a\mathrm{Rm}\rangle
=-4a|\mathrm{Rm}|^2.
\]
所以
\[
\boxed{
\partial_t|\mathrm{Rm}|^2\big|_{h_2}
=
4a|\mathrm{Rm}|^2
+
2\langle\mathrm{Rm},g\owedge\nabla^2a\rangle.}
\]
原笔记的 \(+4a|\mathrm{Rm}|^2\) 完全正确，但 (1.4) 中 Hessian 配对的符号应为正。后续若只取绝对值，该符号不影响估计。

### 2. Kulkarni–Nomizu 缩并

采用笔记中的定义
\[
(g\owedge H)_{ijkl}
=g_{ik}H_{jl}-g_{il}H_{jk}-g_{jk}H_{il}+g_{jl}H_{ik},
\]
直接缩并得到
\[
g^{ik}(g\owedge H)_{ijkl}
=(n-2)H_{jl}+(\operatorname{tr}H)g_{jl}.
\]
利用 Riemann 张量的对称性，
\[
\boxed{
\langle\mathrm{Rm},g\owedge H\rangle
=4\langle\mathrm{Ric},H\rangle.}
\]
因此
\[
2\langle\mathrm{Rm},g\owedge\nabla^2a\rangle
=8\langle\mathrm{Ric},\nabla^2a\rangle,
\]
且
\[
|\langle\mathrm{Rm},g\owedge\nabla^2a\rangle|
\le C_n|\mathrm{Rm}|\,|\nabla^2a|.
\]

同一缩并还给出
\[
\dot{\mathrm{Ric}}\big|_{h_2}
=(n-2)\nabla^2a+(\Delta a)g.
\]
特别地，当 \(a\) 空间常数时，\((0,2)\)-Ricci 张量不变，而其范数因两个逆度量而满足
\[
\partial_t|\mathrm{Ric}|=2a|\mathrm{Ric}|.
\]
所以笔记 §4.1 所称的“归一化增加 \(-2a|\mathrm{Ric}|\)，具有耗散性”符号相反；正确的是有界的 \(+2a|\mathrm{Ric}|\) 零阶项。它仍可作为 Corollary A.10 中的有界系数处理，但并非耗散项。

### 3. 体积变分与精确 \(L^p\) 系数

标准公式为
\[
\partial_t d\mu
=\frac12\operatorname{tr}_g(\dot g)\,d\mu.
\]
对完整流
\[
\dot g=-2a(\mathrm{Ric}+g)
\]
有
\[
\boxed{
\partial_t d\mu=-a(s+n)d\mu.}
\]
故笔记 (1.5) 的符号错误；§2.3 后来的重新计算使用了正确符号。相对于 Yang 的流 \(-2a\mathrm{Ric}\)，归一化的体积增量恰为
\[
-na\,d\mu.
\]

设 \(F=|\mathrm{Rm}|\)、\(E_p=\int F^p\,d\mu\)。归一化部分精确给出
\[
\begin{aligned}
\dot E_p\big|_{\mathrm{norm}}
&=
\frac p2\int F^{p-2}
\left(4aF^2+
2\langle\mathrm{Rm},g\owedge\nabla^2a\rangle\right)d\mu\\
&\qquad-n\int aF^p\,d\mu\\
&=
\boxed{
(2p-n)\int aF^p\,d\mu
+
p\int F^{p-2}
\langle\mathrm{Rm},g\owedge\nabla^2a\rangle\,d\mu.}
\end{aligned}
\]
若采用相反的 Riemann 符号约定，最后的源项符号会反转，但 \(2p-n\) 不变。

常数 \(a\) 给出独立检验：
\[
g(t)=e^{-2at}g(0),\qquad
F(t)^p\,d\mu_{g(t)}
=e^{(2p-n)at}F(0)^p\,d\mu_{g(0)}.
\]
因此
\[
\boxed{p=n/2\quad\Longrightarrow\quad 2p-n=0.}
\]
这是临界曲率能量在常数缩放下的共形尺度不变性。

### 4. Hessian 源的正确能量控制

源项满足
\[
\left|
p\int F^{p-2}
\langle\mathrm{Rm},g\owedge\nabla^2a\rangle
\right|
\le C_{n,p}\int |\nabla^2a|F^{p-1}.
\]
逐点 Young 不等式给出
\[
C_{n,p}|\nabla^2a|F^{p-1}
\le
\varepsilon F^p+
C_{n,p,\varepsilon}|\nabla^2a|^p.
\]
临界层因此至多满足
\[
\frac d{dt}E_{n/2}
\le CE_{n/2}
+C_\varepsilon\int|\nabla^2a|^{n/2}\,d\mu,
\]
从而
\[
E_{n/2}(t)
\le e^{Ct}\left[
E_{n/2}(0)+
C_\varepsilon
\int_0^t\!\!\int|\nabla^2a|^{n/2}\,d\mu\,ds
\right].
\]

把最后一项写成 \(C_\varepsilon\operatorname{Vol}\,t\) 需要关于演化度量下
\(\nabla^2_{g(t)}a\) 的统一 \(L^\infty\) 控制。仅有双 Lipschitz 控制并不足以推出这一点，因为
\[
\nabla^2_{g(t)}a=\partial^2a-\Gamma(g(t))*\partial a
\]
还依赖演化联络。初始 cutoff 的坐标二阶导数有界不自动给出演化协变 Hessian 的统一界。

### 5. 与 Yang Theorem A.7 的兼容范围

Yang 的 A.7 假设的是齐次标量不等式
\[
\partial_t f
\le
\chi^2(\Delta f+c_0f^2)
+2A\chi|\nabla\chi||\nabla f|
+B(|\nabla\chi|^2-\chi\Delta\chi)f,
\]
以及
\[
\partial_t d\mu\le c\chi^2f\,d\mu.
\]

体积条件仍兼容，因为
\[
-a(s+n)\le a|s|\le C_n aF.
\]

超临界反应项也兼容：
\[
(2p-n)\int aF^p\le (2p-n)\int F^p.
\]
其系数对 \(p\) 仅线性增长；在 \(p_k\) 几何增长的 Moser 迭代中，这类多项式增长在取 \(p_k\)-次根后可由收敛的指数和吸收。因此“超临界反应是有界 Grönwall 扰动”是正确的。

真正未闭合的是加性 Hessian 强迫：
\[
C\int |\nabla^2a|F^{p_k-1}.
\]
Yang 的 A.7 及 Lemmas A.5–A.6 是齐次递推，不含该项。粗暴使用 Young 会产生
\[
C_{p_k}\int|\nabla^2a|^{p_k},
\]
或在 \(L^\infty\) 控制下产生类似 \(C^{p_k}\operatorname{Vol}\) 的加性项。取 \(p_k\)-次根后它趋于一个固定强迫尺度，而不是趋于零；当原曲率能量很小时，它反而可能主导。因此笔记 §3.2 所说“相对于
\(H(p_k)^{1+2/n}\) 是次线性的，故可吸收”并不成立，至少尚无所需估计。

可行的严格版本必须证明以下二者之一：

- 一个非齐次 Moser 迭代引理，显式保留由
  \(\|\nabla^2a\|\) 产生的加性点态界，并跟踪其 cutoff、体积及时间依赖；
- 改用移位曲率
  \[
  T=\mathrm{Rm}+\mathcal G,\qquad
  \mathcal G=\frac1{2(n-1)}g\owedge g,
  \]
  因为 \(\mathrm{Ric}(\mathcal G)=g\)，故
  \[
  \partial_tg=-2a\,\mathrm{Ric}(T),
  \]
  从而寻求关于 \(T\) 的齐次演化。不过相应临界假设自然涉及
  \(\int|T|^{n/2}\)，不能无说明地替换原来的
  \(\int|\mathrm{Rm}|^{n/2}\)。

此外，Yang Appendix A 使用 \(2n/(n-2)\) Sobolev 不等式及 \(p>1\) 的 Lemma A.3，直接支持的是 \(n\ge3\)；\(n=2\) 需要独立的二维 Moser 论证。

## 最终判定

- **已严格核准：**
  \[
  \partial_t|\mathrm{Rm}|^2\big|_{h_2}
  =4a|\mathrm{Rm}|^2+
  2\langle\mathrm{Rm},g\owedge\nabla^2a\rangle,
  \]
  \[
  \dot E_p\big|_{\mathrm{norm}}
  =(2p-n)\int a|\mathrm{Rm}|^p+\text{Hessian source},
  \]
  以及 \(p=n/2\) 时反应系数严格为零。

- **应修正：**笔记 (1.2)、(1.4) 的 Hessian 符号；(1.5) 的体积符号；§4.1 的 Ricci“耗散”符号。

- **尚未核准：**由这些恒等式直接推出笔记 Theorem 5.1。缺失的精确科学对象是：带加性强迫
  \(C|\nabla^2a|\) 的非齐次 Yang–Moser 递推及其统一 cutoff-dependent 估计。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 57,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step57_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step57_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the H₂ evolution derivation in §§2-7 of this note for the exact normalized cutoff flow ∂_tg = -2χ²(Ric+g) using the shifted curvature T = Rm + g∧g/(2(n-1)). The main claims to check:

1. The identity |∇T|² = |∇Rm|² because ∇G = 0 (G is built from the metric). Does this hold exactly, including under the evolving metric g(t)? The covariant derivative ∇ = ∇_{g(t)} is time-dependent; is ∇_{g(t)}G(g(t)) still zero?

2. The Bochner pair integration §3: the cross term 2ηa(∇η)·∇|T|² vanishes because a = 0 on supp(∇η). The extra shifted-curvature term ∫η²a⟨ΔRm, G⟩ reduces by IBP to εD₂ + C/(εr²)·Vol using ∇G = 0 and the buffer collar. Check the IBP steps explicitly.

3. The Type (C) Hessian-of-a term §5: after one IBP, ∫η²(∇²a)·𝒯 = -∫η²(∇a)·∇𝒯 with the cross term killed by a∇η = 0. Then Young gives ε''D₂ + C/(ε''r²)H₂. Is this correct for 𝒯 involving E·T (a product of two curvature-type tensors)?

4. The normalization cancellation §6: under pure conformal h = -2ag in n = 4, ∫|Rm|²dμ is exactly constant (the 4D conformal invariance). For T = Rm + G, the extra G-dependent terms are bounded by CaF_T. Verify this dimension-specific cancellation.

5. The W^{1,p} → L^∞ bridge (Proposition 9.1): the base pair gives T ∈ L^q and ∇T ∈ L^q for all q on [τ,T*]. For p > 4, Kato + Sobolev gives ‖T‖_∞ < ∞. Is the Sobolev embedding valid on a closed manifold with bilipschitz-controlled geometry? Does the per-datum Sobolev constant depend on collapse? Check whether this really eliminates the need for the infinite staggered hierarchy.

## Integrated Scientific Memo

# 核验结论

§§2–7 的目标型 \(H_2\) 不等式基本成立，但原笔记存在三个必须修正的精确性问题：

1. \(G\) 的分量归一化及 \(\partial_tG\) 系数相差一个因子 \(2\)；
2. Bochner 块目前有重复计数 shifted term 的风险；
3. §6 所谓“共形不变性”只能解释为**零阶共形缩放项在 \(n=4\) 的抵消**；当 \(a(x)\) 非常数时，仍有 \(\nabla^2a\) 项，并非任意局部共形变化下 \(\int|{\rm Rm}|^2\) 不变。

修正这些后，可得所需能量估计。命题 9.1 的 \(W^{1,p}\to L^\infty\) 步骤也成立，但只给出逐个初始数据的曲率上界；完整光滑延拓仍需要另行证明高阶正则性/延拓定理。

## 1. \(G\) 的平行性与归一化

每个固定时刻 \(t\)，Levi-Civita 联络满足
\[
\nabla_{g(t)}g(t)=0.
\]
因此由 \(g(t)\) 代数构造的
\[
G(g(t))=\frac{g(t)\owedge g(t)}{2(n-1)}
\]
满足
\[
\nabla_{g(t)}G(g(t))=0.
\]
联络随时间变化不影响这一逐时刻空间恒等式。故
\[
\nabla T=\nabla{\rm Rm},\qquad
|\nabla T|_{g(t)}^2=|\nabla{\rm Rm}|_{g(t)}^2
\]
完全精确，因而两个 \(D_2\) 定义相同。

必须固定 Kulkarni–Nomizu 约定。若
\[
(g\owedge g)_{ijkl}
=2(g_{ik}g_{jl}-g_{il}g_{jk}),
\]
则
\[
G_{ijkl}
=\frac{g_{ik}g_{jl}-g_{il}g_{jk}}{n-1},
\qquad
{\rm Ric}(G)=g.
\]
因此 §2.8 中分母 \(2(n-1)\) 的分量公式错误；它只给出
\({\rm Ric}(G)=\frac12g\)。

同一约定下，因 \(h=\partial_tg=-2aE\)，
\[
\partial_tG
=\frac{h\owedge g+g\owedge h}{2(n-1)}
=-\frac{2a}{n-1}(E\owedge g),
\]
而不是 §2.8 的 \(-a(E\owedge g)/(n-1)\)。这些因子不改变后续估计的阶，但必须修正，否则
\({\rm Ric}(T)=E\) 的精确恒等式失效。

## 2. Bochner 块

缓冲区条件给出
\[
a\,d\eta=0,\qquad da=0
\quad\text{于 }\operatorname{supp}d\eta,
\]
故
\[
\int 2\eta a\,\nabla\eta\cdot\nabla|T|^2\,d\mu=0.
\]

若单独处理 shifted term，
\[
I_G=\int\eta^2a\langle\Delta{\rm Rm},G\rangle\,d\mu,
\]
则在闭流形上
\[
\begin{aligned}
I_G
&=-\int\left\langle\nabla{\rm Rm},
\nabla(\eta^2aG)\right\rangle\,d\mu\\
&=-\int\eta^2\,da\cdot
\langle\nabla{\rm Rm},G\rangle\,d\mu.
\end{aligned}
\]
这里 \(2\eta a\,d\eta\otimes G\) 由 \(a\,d\eta=0\) 消失，
\(\eta^2a\nabla G\) 由 \(\nabla G=0\) 消失。于是
\[
|I_G|
\le
\varepsilon D_2+
\frac{C_n}{\varepsilon r^2}
\operatorname{Vol}(\operatorname{supp}\eta,g(t)),
\]
因为
\[
\frac{|da|^2}{a}=4|d\chi|^2\le Cr^{-2}.
\]

但应避免重复计数。正确写法有两种：

- 直接利用 \(\Delta T=\Delta{\rm Rm}\)：
  \[
  2a\langle T,\Delta{\rm Rm}\rangle
  =2a\langle T,\Delta T\rangle
  =a\Delta|T|^2-2a|\nabla T|^2,
  \]
  此时没有额外 \(I_G\)；
- 或先对 \({\rm Rm}\) 使用 Bochner，再显式保留
  \(2a\langle G,\Delta{\rm Rm}\rangle\)。

§3 不能同时使用第一种完整 \(T\)-Bochner 恒等式又另加一次 shifted term。附加的 \(Cr^{-2}\operatorname{Vol}\) 上界虽无害，却不应作为重复推导的结果。

另需统一 \(\Delta_L\) 与 rough Laplacian \(\Delta\)：Bochner 恒等式用于 \(\Delta\)，而
\(\Delta_L-\Delta\) 是曲率代数项，应归入 cubic reaction。

## 3. Hessian-\(a\) 项

精确指标形式为
\[
I_C=\int\eta^2(\nabla_i\nabla_j a)\,\mathcal T^{ij}\,d\mu.
\]
一次分部积分得到
\[
I_C
=-\int\eta^2(\nabla_i a)\nabla_j\mathcal T^{ij}\,d\mu
-2\int\eta(\nabla_i a)(\nabla_j\eta)\mathcal T^{ij}\,d\mu.
\]
第二项因 \(da=0\) 于 \(\operatorname{supp}d\eta\) 而消失。这里真正需要的是
\(da\,d\eta=0\)，仅有 \(a\,d\eta=0\) 还不够。

若 \(\mathcal T\) 由 \(E*T\) 及平行的度量因子构成，则
\[
|\nabla\mathcal T|
\le C\bigl(|\nabla E||T|+|E||\nabla T|\bigr)
\le C F_T|\nabla T|,
\]
因为
\[
|\nabla E|\le C|\nabla{\rm Rm}|=C|\nabla T|,
\qquad |E|+|T|\le C F_T.
\]
所以
\[
\begin{aligned}
|I_C|
&\le C\int\eta^2|da|F_T|\nabla T|\,d\mu\\
&\le \varepsilon''D_2+
\frac{C}{\varepsilon''r^2}H_2.
\end{aligned}
\]
该步骤正确，并且确实消除了对
\(\|\nabla^2\chi\|_\infty\) 的直接依赖。

## 4. \(n=4\) 的 normalization cancellation

对零阶纯共形部分 \(h=-2ag\)，先把 \(a\) 当作点处的缩放系数；\(\nabla^2a\) 项另归 Type (C)。降指标曲率张量的代数变化贡献
\[
2\langle{\rm Rm},-2a{\rm Rm}\rangle
=-4a|{\rm Rm}|^2.
\]
四个逆度量贡献
\[
+8a|{\rm Rm}|^2,
\]
故
\[
(\partial_t|{\rm Rm}|^2)_{\rm alg}
=4a|{\rm Rm}|^2.
\]
体积变化为
\[
\partial_td\mu=-na\,d\mu.
\]
因而
\[
\partial_t\bigl(|{\rm Rm}|^2d\mu\bigr)_{\rm alg}
=(4-n)a|{\rm Rm}|^2d\mu,
\]
恰在 \(n=4\) 消失。

这不是说对空间变系数 \(a(x)\)，
\(\int|{\rm Rm}|^2d\mu\) 在完整局部共形演化下不变：
\(\nabla^2a\) 项仍存在并已由 Type (C) 控制。严格说，四维一般共形不变量是
\(\int|W|^2\)，而非任意局部共形变化下的
\(\int|{\rm Rm}|^2\)。

对 \(F^2=1+|{\rm Rm}|^2\)，常数 \(1\) 产生
\[
-4\int\eta^2a\,d\mu,
\]
这是有界源项。

对 \(T={\rm Rm}+G\)，零阶附加项只含
\[
a\langle{\rm Rm},G\rangle,\quad a|G|^2,\quad a,
\]
可由 \(CaF_T\) 控制；同时
\[
|2\langle T,\partial_tG\rangle|
\le Ca|T||E|
\le CaF_T^2
\le CaF_T^3.
\]
因此这些项可纳入
\[
C\int\eta^2aF_T^3\,d\mu+C_0.
\]

原 §6 中“纯共形逆度量变化为
\(+8a|E||{\rm Rm}|^2\)”的表述应改为
\(+8a|{\rm Rm}|^2\)；\(|E|\)-加权三次项属于完整
\(-2aE\) 变化，不属于纯共形精确抵消。

## 5. 修正后的 \(H_2\) 结论

在选择一种不重复计数的 Bochner 分解、修正 \(G\) 归一化并把
\(\Delta_L-\Delta\) 归入代数反应后，支持
\[
\boxed{
\frac d{dt}H_2+(2-\delta_0)D_2
\le
C_1\int\eta^2aF_T^3\,d\mu
+\frac{C_2}{r^2}H_2+C_0 .
}
\]
若使用直接 \(T\)-Bochner 写法，额外的
\(r^{-2}\operatorname{Vol}\) shifted source 并非必要；若使用拆分写法，则它可合法出现并吸收到 \(C_0\)。

另有一个记号错误：
\[
\operatorname{tr}E={\rm scal}+n.
\]
§2.2 中“\(s=\operatorname{tr}E-n={\rm scal}+n\)”不一致；若
\(s={\rm scal}\)，应直接写 \(\operatorname{tr}E=s+n\)。

## 6. \(W^{1,p}\to L^\infty\) 桥

假设 Step 56 的三个微分不等式及
\[
\|aF_T(t)\|_\infty\le C\gamma/t
\]
在 \((0,T^*)\) 成立。固定 \(\tau>0\)。则
\[
|\partial_tg|=2a|E|\le CaF_T\le C\gamma/\tau
\]
给出 \(g(t)\) 与 \(g(\tau)\) 在
\([\tau,T^*)\) 上的一致双 Lipschitz 等价。

由 base-pair 链得到，对任意有限 \(q\)，
\[
T,\ \nabla U,\ \nabla^2\chi,\ \nabla T
\in L^\infty([\tau,T^*];L^q).
\]
取 \(p>4\)。Kato 不等式
\[
|d|T||\le|\nabla T|
\]
给出 \(|T|\in W^{1,p}\)。固定闭光滑流形
\((M,g(\tau))\) 上 Morrey–Sobolev 嵌入成立：
\[
W^{1,p}(M,g(\tau))\hookrightarrow L^\infty(M),\qquad p>4.
\]
双 Lipschitz 等价把各时刻 \(g(t)\) 的 \(L^p\) 与梯度范数统一比较到
\(g(\tau)\)，故
\[
\sup_{t\in[\tau,T^*)}\|T(t)\|_\infty
\le C_{p,\tau}
\sup_{t\in[\tau,T^*)}
\bigl(\|T(t)\|_p+\|\nabla T(t)\|_p\bigr)<\infty.
\]

该 Sobolev 常数确实可能依赖塌缩，例如依赖
\((M,g(\tau))\) 的逐数据几何；双 Lipschitz 控制只保证它在给定流的终端时间片上一致，不给出跨塌缩序列的一致常数。这不妨碍逐数据 continuation，但不能进入 sequence-uniform first-exit 估计。

因此有限阶桥确实消除了“为了先得到
\(\|{\rm Rm}\|_\infty\)”而运行无限 staggered hierarchy 的需要。它没有单独完成光滑延拓：从有界曲率到 \(t=T^*\) 的光滑极限及 restart，仍需一个经证明的高阶退化 Shi 型估计、完整 staggered bootstrap，或适用于该 cutoff flow 的明确 continuation theorem。§9.2(a) 目前只是对此的概述；§9.2(b) 的
\(\Gamma\) 的 \(L^p\) 收敛加曲率有界本身不足以推出终点度量光滑。

最后，整个命题 9.1 依赖未在这些文件中重证的 weighted Moser 输入
\(\|aF_T\|_\infty\le C\gamma/t\)。因此核验结果是：

- §§2–7 的 \(H_2\) 不等式经上述修正后成立；
- \(W^{1,p}\to L^\infty\) 曲率桥成立，且 Sobolev 常数仅逐数据有限；
- “由此自动平滑越过 \(T^*\)”尚需独立的高阶延拓论证，不能仅由有限阶桥本身宣告。
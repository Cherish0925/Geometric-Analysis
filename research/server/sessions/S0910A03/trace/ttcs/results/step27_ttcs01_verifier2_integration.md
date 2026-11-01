# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 27,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step27_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step27_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the logical interface between a normalized local-flow extension theorem and the existing Step 26 first-exit chain. Determine whether a terminal-time assumption sup|a Rm|<∞ really supplies all hypotheses needed for the shifted-curvature Wang induction on a closed manifold, with constants allowed to depend on the individual smooth initial metric/cutoff, and whether bounds for all ∇^m(a(Rm+G)) suffice for smooth extension. Identify any overlooked issue involving zeros of a, unweighted L^p curvature, evolving contraction Ric(aT)=a Ric(T), transported DeTurck coefficient, or support collar. Also assess whether the claimed whole-support Moser bound is strong enough near a terminal time despite its C/t form.

## Integrated Scientific Memo

## 核验结论

设
\[
a=\chi^2,\qquad E=\Ric_g+g,\qquad 
\widetilde R=\Rm+G,\qquad U=a\widetilde R,
\]
其中
\[
G_{ijkl}=\frac1{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}),
\qquad \Ric(G)=g.
\]

对闭流形上的归一化局部流
\[
\partial_t g=-2aE
\]
而言，终止时刻假设
\[
\sup_{M\times[0,T)}|a\Rm|<\infty,\qquad T<\infty
\]
确实提供了 Wang 型高阶归纳所需的全部**基础假设**；零点集、外部静止 collar、归一化项和 \(C/t\) 型 Moser 界都不会额外破坏接口。但目前 Step 27 只建立了正确的结构框架，尚未完成 Wang Lemma 4.11、Propositions 4.13–4.14 的逐项归一化版本，因此还不能把延拓定理视为已经证明。

---

## 1. 终端加权曲率界给出的基础控制

因为 \(|G|_g\) 仅依赖维数且 \(0\le a\le1\)，
\[
|U|=|a(\Rm+G)|\le |a\Rm|+C_n.
\]
并且有精确恒等式
\[
\Ric(U)=a\Ric(\widetilde R)=a(\Ric+g)=aE.
\]
故
\[
\partial_tg=-2\Ric(U),\qquad |\partial_tg|_g\le C_n|U|.
\]
于是有限时间内
\[
e^{-CT}g_0\le g(t)\le e^{CT}g_0.
\]
这给出：

- 体积形式的一致比较；
- 相对于固定闭流形 \((M,g_0)\) 的一致非齐次 Sobolev 常数；
- \(|d\chi|_{g(t)}\) 的一致界；
- 所有初始 cutoff jets 的有限性。

常数允许依赖单个 \((g_0,\chi,T)\)，因此不需要任何序列一致的高阶 cutoff 界；高阶 \(\nabla^r\chi\) 正是由 Wang 的耦合归纳传播。

---

## 2. \(a\) 的零点不会导致缺失的未加权曲率控制

\(|U|\) 在 \(a\) 很小时不能逐点控制 \(\widetilde R\)，所以 Wang 归纳所需的未加权
\[
\|\widetilde R\|_{L^p}
\]
必须单独证明，而不能从加权 \(L^\infty\) 界直接推出。

对
\[
Y_p(t)=\int_M(1+|\widetilde R|^2)^{p/2}\,d\mu_t
\]
使用移位曲率方程测试。将
\[
(\nabla^2a)*\Ric(\widetilde R)
\]
积分分部一次后，关键项满足
\[
a|\widetilde R|^{p+1}
=|a\widetilde R|\,|\widetilde R|^p
\le \|U\|_\infty |\widetilde R|^p,
\]
以及
\[
|da|\,|\nabla\widetilde R|\,|\widetilde R|^{p-1}
\le \varepsilon a|\nabla\widetilde R|^2|\widetilde R|^{p-2}
+C_\varepsilon\frac{|da|^2}{a}|\widetilde R|^p.
\]
由于 \(a=\chi^2\)，真正出现的配对张量为
\[
\frac{da\otimes da}{a}=4\,d\chi\otimes d\chi
\]
并可光滑延拓到 \(\{\chi=0\}\)。因此
\[
Y_p'\le C_p(1+Y_p),
\]
从而对每个有限 \(p\)，
\[
\sup_{t<T}\|\widetilde R(t)\|_{L^p}<\infty.
\]

必须注意：可控的是 \(da\otimes da/a\) 或 \(|da|^2/a\)，不能把证明改写成单独使用可能奇异的 \(da/a\)。

---

## 3. 收缩恒等式没有所谓“空间低阶误差”

固定时刻有
\[
\nabla g^{-1}=0,
\]
所以
\[
\nabla^m(aE)
=\nabla^m\Ric(U)
=\Ric(\nabla^mU)
\]
是精确恒等式，不含“由 evolving contraction convention 产生的低阶项”。这种代数项只会在对收缩作**时间微分**时出现。

同样，
\[
\partial_t\Gamma
=g^{-1}*\nabla(aE)
=g^{-1}*\nabla\Ric(U).
\]
故 cutoff 导数演化中的最高输入恰为 \(\nabla^{r-1}U\)，与 Wang Lemma 4.6 的依赖三角完全一致。严格书写点态范数演化时，宜使用 \(|\nabla^r\chi|^2\) 或正则化范数，以避开范数在零点不可微的问题。

---

## 4. 归一化并未引入新的高阶未知量，但完整归纳尚缺

移位后 \(\nabla G=0\)，且
\[
\partial_tG=\Ric(U)*g
\]
仅为代数项。因此归一化产生的项仍只涉及：

- \(U\) 及其导数；
- 未加权 \(\widetilde R\) 及其导数；
- \(\chi\) 的导数；
- 已由维数控制的 \(G\)。

最高 cutoff 项仍是
\[
\chi\nabla^{m+2}\chi*U,\qquad
\nabla\chi*\nabla^{m+1}\chi*U,\qquad
\chi\nabla^{m+1}\chi*\nabla U.
\]
这些项必须像 Wang Proposition 4.14 那样积分分部，不能在点态上直接声称受控。

特别需要核对的项是由联络变化产生的
\[
\Ric(\nabla^mU)*\widetilde R.
\]
其中 \(\widetilde R\) 通常只有任意有限 \(L^q\) 界，而非未加权 \(L^\infty\) 界。它应通过 Hölder、足够大的指数、Sobolev 和加权扩散落入 Wang 的未加权曲率族，但这一吸收尚未逐项写出。

因此当前可以确认的是：

\[
U\in L^\infty,\quad
\widetilde R\in L^p\ \forall p<\infty,\quad
|d\chi|\in L^\infty,
\]
加上统一度量/Sobolev 比较和有限初始 jets，确实是归纳所需的正确输入。仍缺的是归一化版的：

1. Lemma 4.11：先同时控制 \(\nabla U\) 与 \(\nabla^2\chi\)；
2. Proposition 4.13：由 cutoff jets 控制未加权 \(\nabla^m\widetilde R\)；
3. Proposition 4.14：闭合 \(\nabla^mU\) 与 \(\nabla^{m+1}\chi\) 的循环。

其核心应形成 Wang Lemma 4.8 型耦合不等式
\[
y_m'(t)\le A_m\int_0^t y_m(s)\,ds+B_my_m(t)+C_m,
\]
其中 \(y_m\) 同时包含相应的 \(\|\nabla^mU\|_{L^p}\) 和最高 cutoff 范数。

另一个小的代数修正是：若将移位反应项写成 \(\mathcal Q_G(\widetilde R)\)，应有
\[
\mathcal Q_G(0)=0.
\]
因为 \(\widetilde R=0\) 意味着 \(E=0\)，流速为零；故任何表面上的常数项必须在精确公式中抵消。粗略估计
\[
|\mathcal Q_G(S)|\le C(1+|S|+|S|^2)
\]
可用于能量估计，但不反映这一精确消去。

---

## 5. 所有 \(\nabla^mU\) 有界确实足以光滑延拓

若对每个 \(m\ge0\)，
\[
\sup_{M\times[0,T)}|\nabla^mU|<\infty,
\]
则
\[
\sup|\nabla^m(aE)|\le C_{n,m}\sup|\nabla^mU|.
\]
令
\[
A(t)=\nabla^{g(t)}-\nabla^{g_0}.
\]
由
\[
\partial_tA=g^{-1}*\nabla(\partial_tg)
=g^{-1}*\nabla\Ric(U),
\]
先控制 \(A\)，再相对于固定联络 \(\nabla^{g_0}\) 逐阶微分，可归纳控制所有 \(\nabla_{g_0}^kA\)。于是
\[
\partial_tg=-2\Ric(U)
\]
的所有固定坐标空间导数一致有界，并在有限时间上可积。故 \(g(t)\) 在 \(C^\infty\) 中收敛到光滑正定度量 \(g(T)\)，再由同一固定标量 \(a\) 的短时存在性向后延拓。

因此，在已经获得全部 \(U\)-jets 后，不需要额外的未加权逐点曲率界。

---

## 6. DeTurck 系数必须随微分同胚输运

hatted 系统中的系数必须是
\[
\widehat a=a\circ\varphi_t^{-1},
\qquad \varphi_t^*\widehat a=a.
\]
若在 hatted 坐标中错误地固定 \(\widehat a=a\)，拉回后一般不会得到原方程。加入
\[
-2\widehat a\,\widehat g
\]
只是关于度量的零阶项，不改变 Yang 正则化系统的主部；只需保持 Lie 导数项与微分同胚方程的符号配对，使拉回时二者消去。

---

## 7. support collar 不需要小性或序列一致控制

在 \(a=0\) 的外部开集上，
\[
\partial_tg=0,\qquad U=0.
\]
该区域的未加权曲率及其导数只是初始度量的固定有限量。它们可能在某个度量序列中不一致，但终端延拓定理允许常数依赖单个 \((g_0,\chi)\)，所以不构成缺失假设。

Step 26 的活跃区能量与外部 collar 常量应继续分开；不能从 collar 的未加权曲率推导任何统一小性，但延拓本身也不需要这种小性。

---

## 8. \(C/t\) 的全 support Moser 界足够处理正的终止时刻

若最大存在时间 \(T_*>0\) 且
\[
\|a\Rm(t)\|_\infty\le \frac{C\bar\beta}{t},
\qquad 0<t<T_*,
\]
则在后半段
\[
\sup_{t\in[T_*/2,T_*)}\|a\Rm(t)\|_\infty
\le \frac{2C\bar\beta}{T_*}<\infty.
\]
在 \([0,T_*/2]\) 上，加权曲率由光滑短时解及紧性自动有界。因此
\[
\sup_{M\times[0,T_*)}|a\Rm|<\infty.
\]
由于 \(a=0\) 于活跃 support 外，全 support 估计已经是全流形的加权曲率估计。\(t\downarrow0\) 时的形式发散不妨碍正终止时刻的延拓。

---

## 9. 与 first-exit 链的正确逻辑顺序

必须在最大光滑存在区间
\[
[0,T_{\max})
\]
上运行 Step 26 的能量、Moser 和 first-exit 估计，而不能预先假设解已存在到目标时间。若假设
\[
T_{\max}<\theta r^2,
\]
则 first-exit 改进及 \(C/t\) 界给出
\[
\sup_{M\times[0,T_{\max})}|a\Rm|<\infty.
\]
归一化延拓定理随后迫使解跨过 \(T_{\max}\)，产生矛盾。因此得到
\[
T_{\max}\ge\theta r^2.
\]

这个排列消除了“first-exit 假设目标时间存在，而延拓又依赖 first-exit”的循环。

---

## 最终判定

- **接口层面：成立。** 终端假设 \(\sup|a\Rm|<\infty\) 给出了移位 Wang 归纳所需的全部基础输入。
- **延拓判据层面：成立。** 全部 \(\nabla^m(a(\Rm+G))\) 有界足以得到 \(C^\infty\) 终端极限并延拓。
- **潜在问题均可消除：** \(a\) 的零点、未加权 \(L^p\) 曲率、空间收缩、DeTurck 输运、静止 collar 和 \(C/t\) 终端行为都没有制造新假设。
- **尚未完成的唯一实质性证明对象：** 将 \(\mathcal L_{G,m}\) 完全展开，并逐项完成归一化版 Wang Lemma 4.11 与 Propositions 4.13–4.14，尤其验证 \(\Ric(\nabla^mU)*\widetilde R\) 和最高 cutoff 项在耦合 \(L^p\) 不等式中的吸收。
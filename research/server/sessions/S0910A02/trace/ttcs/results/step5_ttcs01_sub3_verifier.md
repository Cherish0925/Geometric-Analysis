# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step5_positive_branch_all_dimensions.md",
    "Sessions/S0910A02/workspace/notes/step4_preceptor_energy_accounting_and_route_review.md",
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md"
  ]
}
```

## Task

Verify the noncollapsed positive convergence theorem (Theorem 2) stated in the Step 5 note for Yau Problem 26. The theorem claims: for each n≥2 and v>0, there exists ε(n,v)>0 such that any closed connected smooth Riemannian n-manifold with δ_+(g)≤ε and Vol(M,g)≥v admits an Einstein metric. The proof uses: (1) two-sided Ricci bounds from δ_+(g)≤δ giving (1-δ)g≤Ric≤(1+δ)g; (2) Myers diameter bound giving diam≤D(n,δ); (3) harmonic radius lower bound r_h(n,Λ,D,v)>0 from Ricci bounds + noncollapse + bounded diameter; (4) C^{1,α} Arzelà-Ascoli convergence in harmonic coordinate atlases; (5) passing Ric→g to the limit in distributional sense; (6) elliptic regularity bootstrapping from C^{1,α} Einstein to C^∞; (7) diffeomorphism M_i≅M_∞ for large i from global C^{1,α} convergence. Check: are all steps valid? Are there gaps in the argument (e.g., does step 3 require Anderson's specific theorem or can it be derived from elementary Ricci bounds? Is the elliptic regularity in step 6 standard? Does the global convergence in step 7 really give diffeomorphism?). Is the constant dependence ε=ε(n,v) correct, or does ε also depend on other geometric data? Does the theorem correctly identify that the gap to P_n^+ is exactly the volume dependence?

## Output

# 科学复核备忘

## 总评

Theorem 2 的现有证明在 \(n\ge 4\) 时没有成立。核心断点是 Step 2.1：

\[
|\operatorname{Ric}|\le \Lambda,\qquad
\operatorname{diam}\le D,\qquad
\operatorname{Vol}\ge v
\]

不能推出统一的 \(C^{1,\alpha}\) harmonic radius 下界。全局体积非塌缩确实推出所有小球的体积下界，但不排除 Weyl 曲率集中、orbifold 奇点和 ALE 冒泡。后续 Step 2.2–2.5 在另加统一 harmonic radius 下界时基本正确；仅凭本文三项几何数据则无法启动。

这说明现有论证没有证明 \(n\ge4\) 的 Theorem 2，但也没有证明其反命题。其真值仍涉及非塌缩奇性形成与底层光滑拓扑能否承载 Einstein 度量。

---

## 1. Ricci、直径和局部体积控制：正确

取反证序列 \(\delta_i\to0\)。对充分大的 \(i\)，可令 \(\delta_i\le \frac12\)，于是

\[
\frac12 g_i\le \operatorname{Ric}_{g_i}\le \frac32 g_i,
\qquad
\operatorname{diam}(M_i,g_i)
\le \pi\sqrt{2(n-1)}=:D_n .
\]

若 \(|\operatorname{Ric}|\) 指 Hilbert–Schmidt 范数，则应写

\[
|\operatorname{Ric}_{g_i}|\le \frac32\sqrt n,
\]

而不是 \(\Lambda=2\)；若指 Ricci endomorphism 的算子范数，则 \(\Lambda=2\) 可以使用。由于 \(n\) 固定，这只改变维数常数。

全局体积下界确实给出逐点、逐尺度的体积非塌缩。利用 \(\operatorname{Ric}\ge0\) 和 Bishop–Gromov，对 \(0<r\le D_n\)，

\[
\frac{\operatorname{Vol}B_{g_i}(x,r)}{r^n}
\ge
\frac{\operatorname{Vol}B_{g_i}(x,D_n)}{D_n^n}
=
\frac{\operatorname{Vol}(M_i,g_i)}{D_n^n}
\ge \frac{v}{D_n^n}.
\]

所以 Step 2.1 中“小球体积下界”的部分成立。

---

## 2. harmonic radius 推论不成立

从上述小球体积下界不能得到

\[
r_h(M_i,g_i)\ge r_0(n,\Lambda,D,v)>0.
\]

原因可从曲率分解直接看出。对 \(n\ge4\)，

\[
\operatorname{Rm}
=
W+\frac1{n-2}\mathring{\operatorname{Ric}}\owedge g
+\frac{s}{2n(n-1)}g\owedge g .
\]

条件 \(\operatorname{Ric}\simeq g\) 控制后两项，却完全不控制 \(W\)。因此即使 Ricci 张量、直径和所有小球的体积比都有统一控制，仍可能有全曲率集中。

Step 2.1 中的 harmonic-coordinate PDE

\[
-\frac12 g^{ab}\partial_a\partial_b g_{ij}
+Q_{ij}(g,\partial g)=R_{ij}
\]

本身不能产生一个定长的 harmonic chart。使用这条方程以前，已经需要该坐标球上的度量椭圆性和坐标正则性；这正是 harmonic radius 要表达的内容。因此“有界 Ricci 右端项 \(\Rightarrow\) 定长 harmonic chart”在这里是循环推理。

标准 harmonic-radius 定理通常还使用以下一种信息：

- \(\operatorname{inj}(M,g)\ge i_0>0\)；
- 某个尺度上的体积比接近欧氏值，而不仅是大于任意固定正数；
- 全曲率控制；
- 直接假设 harmonic radius 下界；
- 足以排除局部曲率集中的积分信息。

Step 4 的来源摘要也与此一致：非塌缩、Ricci 有界的四维 Einstein 序列，其自然紧性输出允许 Einstein orbifold、孤立奇点和 Ricci-flat ALE bubbles，而不是必然得到全局光滑流形。该摘要中的四维结果还使用 \(L^2\) 曲率控制；Theorem 2 的假设甚至没有统一的 \(L^2\) 全曲率上界，因为 \(\chi(M_i)\) 可以变化。

四维 CGB 公式也不能修复此处：

\[
8\pi^2\chi
=
\int_M\left(
|W|^2+\frac{s^2}{24}
-\frac{|\mathring{\operatorname{Ric}}|^2}{2}
\right)d\mu .
\]

体积下界只给 Weyl 总能量与拓扑量之间的差值，并不给每个小球上的能量小量，也不给 \(W\) 的点态上界。

---

## 3. 后续步骤在统一 harmonic radius 假设下成立

### 全局 \(C^{1,\alpha}\) 紧性

若另有

\[
r_h^{1,\alpha}(M_i,g_i)\ge r_0>0,
\]

则由直径上界、总体积上界和局部体积下界，可用统一有限数量的 harmonic charts 覆盖 \(M_i\)。标准 Cheeger–Gromov 紧性随后给出一个紧致 \(C^{1,\alpha}\) 流形 \((M_\infty,g_\infty)\)，并在取子列后给出微分同胚

\[
\varphi_i:M_\infty\longrightarrow M_i
\]

以及 \(C^{1,\beta}\) 收敛，其中通常取 \(\beta<\alpha\)。

仅有 GH 收敛，或仅在正则部分上的坐标收敛，不产生这些全局微分同胚。因而 Step 2.4 只有在已经得到全局 Cheeger–Gromov \(C^{1,\alpha}\) 收敛时才正确。

### Einstein 方程传到极限

在上述全局收敛成立时，这一步正确。由

\[
\|\operatorname{Ric}_{g_i}-g_i\|_{g_i}\le\delta_i\to0
\]

及 \(g_i\to g_\infty\) 的 \(C^{1,\beta}\) 收敛，可得该张量差在固定坐标中一致趋于零。Ricci 的坐标公式是 Christoffel 符号的一阶导数加二次项；Christoffel 符号在 \(C^0\) 中收敛，所以其导数在分布意义下收敛。因此

\[
\operatorname{Ric}_{g_\infty}=g_\infty
\]

作为分布方程成立。

### 从 \(C^{1,\alpha}\) 到光滑

这是标准的 Einstein 正则性。极限 harmonic coordinates 仍是 \(g_\infty\)-harmonic，方程成为一致椭圆系统

\[
-\frac12 g_\infty^{ab}
\partial_a\partial_b(g_\infty)_{ij}
=
(g_\infty)_{ij}
-Q_{ij}(g_\infty,\partial g_\infty).
\]

右端属于 \(C^{0,\alpha}\)。先用弱解的椭圆正则性，再用 Schauder 估计得到 \(C^{2,\alpha}\)，随后反复微分得到 \(C^\infty\)；事实上 Einstein 度量在 harmonic coordinates 中为实解析。这里不需要 Einstein 算子的非退化性，因为不是把 \(g_i\) 扰动成 Einstein 度量，而是把极限 Einstein 度量经微分同胚搬回 \(M_i\)。

---

## 4. 常数依赖

若统一 harmonic radius 下界真的能由 \((n,v)\) 推出，则反证紧性论证确实会给出某个非显式

\[
\varepsilon=\varepsilon(n,v).
\]

理由是当 \(\delta\le\frac12\) 时，Ricci 上界和 Myers 直径上界都只依赖 \(n\)。

但目前所引 harmonic-radius 推论不存在。因此可验证的修正版需要额外几何参数，例如：

\[
\varepsilon=\varepsilon(n,v,r_0,\alpha)
\]

在假设 \(r_h^{1,\alpha}\ge r_0\) 时；或相应地写成

\[
\varepsilon(n,v,i_0),\qquad
\varepsilon(n,v,K)
\]

分别对应 injectivity radius 下界或 \(|\operatorname{Rm}|\le K\)。

在 \(n=2,3\) 时情况不同：二维中 Ricci 决定 Gauss 曲率，三维中 Weyl 张量恒为零而 \(\operatorname{Rm}\) 由 Ricci 代数决定。因此 Ricci 夹逼给出全曲率控制，结合局部体积下界可得到 injectivity/harmonic-radius 控制。并且 Step 5 已分别用 uniformization 和 Hamilton 定理独立得到结论。

---

## 5. 与 \(P_n^+\) 的关系

“距 \(P_n^+\) 只差体积下界”并不准确。现有推导还没有处理非塌缩但 harmonic radius 趋于零的序列。可靠的序列性表述是：

若 \(P_n^+\) 不成立，可选取

\[
\delta_+(g_i)\to0,\qquad \mathcal E(M_i)=\varnothing.
\]

取子列后至少出现以下一种现象：

\[
\operatorname{Vol}(M_i,g_i)\to0,
\]

或存在 \(v>0\) 使体积保持在 \(v\) 以上，但 harmonic radius 趋于零，从而产生全曲率集中或奇性极限。现有材料没有排除第二种现象。

即使 Theorem 2 将来成立，“\(P_n^+\) 当且仅当紧夹逼阻止体积塌缩”仍不对。Step 5 自己给出的三维圆 lens spaces 满足

\[
\delta_+(h_m)=0,\qquad
\operatorname{Vol}(h_m)\to0,
\]

而 \(P_3^+\) 由 Hamilton 定理成立。正确含义只能是：若 Theorem 2 成立，则任何由无 Einstein 拓扑组成、且 \(\delta_+\to0\) 的序列必须体积趋零；它并不要求所有容许输入度量都具有统一体积下界。

另有一处相邻文本不一致：Theorem 1(d) 中仅依赖 \((n,\delta)\) 的 \(|\pi_1|\) 上界被 lens spaces 直接否定。Myers 只给出 \(\pi_1\) 有限。加入 \(\operatorname{Vol}(M,g)\ge v\) 后才有

\[
|\pi_1(M)|
=\frac{\operatorname{Vol}(\widetilde M)}
       {\operatorname{Vol}(M)}
\le \frac{V_n(\delta)}{v}.
\]

这项修正仍不能控制 Weyl 曲率或 harmonic radius。
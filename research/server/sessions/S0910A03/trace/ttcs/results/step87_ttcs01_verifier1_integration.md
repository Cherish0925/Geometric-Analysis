# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 87,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step87_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step87_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following forced reflected OT connector obstruction theorem. The setting: a complete 2D smooth weighted base (B², γ_B, dμ = e^σ dA) with σ-harmonic map U: B → H² (hyperbolic plane), orbit energy e = |dU|²_{H²}, weighted tension F = τ_σ(U), and the Einstein base equation gives Ric_f^4 = Ric_B - Hess σ - ½dσ⊗dσ ≥ -(3+δ)γ_B (finite-dimensional CD condition with N=4).

The argument chain:

1. FORCED BOCHNER (from Steps 85-86): ½Le ≥ |DdU|² + div_σ V - |F|² + ½e² - (3+δ)e, where V(X) = ⟨dU(X), F⟩, |V| ≤ |F|√e ≤ 2δ√e. Drop |DdU|² ≥ 0.

2. MASSIVE COMPARISON: With κ = 6+2δ = 2(3+δ), rearrange to get (-L+κ)e ≤ κ² + 2(2δ)² - 2div_σ V. Key step: 2κe - e² ≤ κ² (completing the square).

3. LI-YAU FISHER INFORMATION: On a complete smooth weighted manifold with CD(-K,N) [Ric_f^N ≥ -K], the heat kernel p_t of L satisfies the Li-Yau gradient estimate, hence I(t) := ∫ p_t |∇_y log p_t|² dμ ≤ N/(2t) + NK/2. By Cauchy-Schwarz and heat conservation ∫p_t dμ = 1: ∫|∇_y p_t(x,y)| dμ(y) ≤ √I(t) ≤ √(N/(2t) + NK/2).

4. RESOLVENT ESTIMATE: C_κ = sup_x ∫|∇_y G_κ(x,y)| dμ(y) ≤ ∫_0^∞ e^{-κt} √(N/(2t)+NK/2) dt = √(2πN/(2κ)) + √(NK/2)/κ. With N=4, K=3+δ: C_κ ≤ √(2π/κ) + √(2(3+δ))/κ.

5. COMPARISON PRINCIPLE: Since -L+κ has strictly positive potential (κ>0) on a complete manifold, if (-L+κ)(ψ-e) ≥ 0 and ψ-e is bounded below, then ψ-e ≥ 0 (Omori-Yau). Define ψ by (-L+κ)ψ = κ²+8δ²-2div_σ V. Then ψ = (κ²+8δ²)/κ + ψ_2 where |ψ_2| ≤ 2C_κ·2δ·√B (B=sup e). So B ≤ κ+8δ²/κ + 4δC_κ√B.

6. QUADRATIC CLOSURE: B ≤ α + β√B with α = κ+8δ²/κ, β = 4δC_κ. Solution: B ≤ (β/2+√(β²/4+α))². CENTER FLOOR: ⟨e(0,·)⟩_μ ≥ 12-8δ (from reflected center Gauss equation with defect). For δ < δ₀ ≈ 0.249, the ceiling B(δ) < 12-8δ = floor. Contradiction.

Verify each step. Particular attention to: (a) Is the Li-Yau Fisher information bound I(t) ≤ N/(2t)+NK/2 correct under CD(-K,N) with N > dim M? What is the standard reference? (b) Is stochastic completeness (∫p_t dμ = 1) guaranteed under CD(-(3+δ),4) on our complete weighted manifold? (c) Is the integration by parts for R_κ[div_σ V] justified when V vanishes at infinity? (d) Does the Omori-Yau maximum principle apply to -L+κ on this specific complete manifold (exponential weighted volume growth)? (e) Is the center floor 12-8δ correctly derived from the Gauss equation? Check all sign conventions.

## Integrated Scientific Memo

# 核验结论

该论证链的核心可以成立，但原 Step 3 的 Fisher 信息估计错误，因此原宣称的阈值  
\(\delta_0\simeq0.24885\) **不能由所写论证推出**。将其替换为正确的有限维 \(CD(-K,N)\) 熵耗散估计后，得到严格的通用 resolvent 常数

\[
C_\kappa\le \frac{2}{\sqrt{3+\delta}},
\]

并产生修正后的障碍阈值

\[
\boxed{\delta_* \simeq 0.24625.}
\]

因此，在完整列明以下假设时，forced reflected OT connector obstruction 是成立的：

- 完备、无边界的光滑加权延拓；
- 全局 \(CD(-(3+\delta),4)\)；
- 全四维 Ricci 缺陷满足 \(\|E\|_{\mathrm{op}}\le\delta\)；
- \(e=|dU|^2\) 有界（例如 \(e\to0\) 于所有端）；
- 反射中心光滑且全测地；
- 中心 Gauss 恒等式所需的自由、正交传递 \(T^2\) 结构成立。

---

## 1. Forced Bochner 与 massive comparison：正确

令 \(f=-\sigma\)，则

\[
L=\Delta-\langle\nabla f,\nabla\cdot\rangle
 =\Delta+\langle\nabla\sigma,\nabla\cdot\rangle .
\]

有限维 Bakry–Émery 张量为

\[
\operatorname{Ric}^{4}_{f}
=\operatorname{Ric}_B-\operatorname{Hess}\sigma
-\frac12d\sigma\otimes d\sigma .
\]

由基底 Einstein 方程，

\[
\operatorname{Ric}^{4}_{f}
=-3\gamma_B+\frac12U^*h_{\mathbb H^2}+E_B
\ge -(3+\delta)\gamma_B.
\]

注意 round-cusp benchmark 中该张量是 \(-3\gamma_B\)，不是
\(\operatorname{diag}(-1,-3)\)；后者是尚未减去
\(\frac12d\sigma^2\) 的 \(\operatorname{Ric}_B-\operatorname{Hess}\sigma\)。

令

\[
V(X)=\langle dU(X),F\rangle .
\]

则符号正确地满足

\[
\langle dU,DF\rangle
=\operatorname{div}_\sigma V-|F|^2.
\]

双曲目标曲率项满足

\[
Q(A)=\frac12e^2+\det A\ge\frac12e^2.
\]

结合 \(E_B:A\ge-\delta e\)，得到

\[
\boxed{
\frac12Le\ge |DdU|^2+\operatorname{div}_\sigma V-|F|^2
+\frac12e^2-(3+\delta)e.}
\]

由垂直 Ricci 缺陷方程，

\[
|F|\le2\delta,\qquad |V|\le2\delta\sqrt e.
\]

置

\[
K=3+\delta,\qquad \kappa=2K=6+2\delta,
\]

丢掉 \(|DdU|^2\) 后，

\[
(-L+\kappa)e
\le 2\kappa e-e^2+2|F|^2-2\operatorname{div}_\sigma V.
\]

利用

\[
2\kappa e-e^2=\kappa^2-(e-\kappa)^2\le\kappa^2
\]

及 \(2|F|^2\le8\delta^2\)，得到

\[
\boxed{
(-L+\kappa)e
\le \kappa^2+8\delta^2-2\operatorname{div}_\sigma V.}
\]

Steps 1–2 因而成立。

---

## 2. 原 Fisher 信息估计不成立

原式

\[
I(t)\le\frac{N}{2t}+\frac{NK}{2}
\tag{2.1}
\]

并不是一般 \(CD(-K,N)\) 下的有效全时间估计；它只是正确表达式的小时间展开的前两项。

一个直接反例是 supplied round cusp：

\[
\gamma_B=dr^2+e^{2r}dz^2,\qquad \sigma=2r,
\]

其径向算子为

\[
L_{\rm rad}=\partial_{rr}+3\partial_r.
\]

径向热核相对于 \(e^{3r}dr\) 的 Fisher 信息为

\[
9+\frac1{2t}.
\]

全热核 Fisher 信息不小于其径向边缘的 Fisher 信息。因此在 \(N=4,K=3\) 时，原式给出的

\[
I(t)\le\frac2t+6
\]

在 \(t>1/2\) 时与上述下界冲突。

---

## 3. 正确的 \(CD(-K,N)\) Fisher 估计

定义

\[
I(t)=\int p_t|\nabla\log p_t|^2\,d\mu.
\]

在保守热半群下，de Bruijn–\(\Gamma_2\) 恒等式给出

\[
I'(t)=-2\int p_t\,\Gamma_2(\log p_t)\,d\mu.
\]

由

\[
\Gamma_2(\phi)\ge -K\Gamma(\phi)+\frac1N(L\phi)^2
\]

以及

\[
\int p_tL\log p_t\,d\mu=-I(t),
\]

Jensen 不等式给出

\[
\int p_t(L\log p_t)^2d\mu\ge I(t)^2.
\]

因此

\[
I'(t)\le2KI(t)-\frac2N I(t)^2.
\]

与具有 \(I(0+)=+\infty\) 的 Riccati 解比较，得到

\[
\boxed{
I(t)\le\frac{NK}{1-e^{-2Kt}}
=\frac{NK}{2}\bigl(\coth(Kt)+1\bigr).}
\tag{3.1}
\]

其展开为

\[
\frac{NK}{1-e^{-2Kt}}
=\frac{N}{2t}+\frac{NK}{2}+O(t),
\]

解释了原错误公式的来源。

这是标准有限维 Bakry–Émery 半群计算；可核对 Bakry–Qian 的有限维 Li–Yau 型理论，或 Bakry–Gentil–Ledoux 的 Markov diffusion monograph。这里真正使用的是上述可直接复验的 \(\Gamma_2\)-Riccati 推导。

---

## 4. 随机完备性：在全局完备延拓假设下成立

对于完备光滑加权流形，有限 \(N>n\) 且

\[
\operatorname{Ric}^{N}_{f}\ge-Kg
\]

时，加权体积比较给出至多指数增长：

\[
\mu(B_R(x))\le C_x e^{cR}.
\]

于是 Grigor’yan 体积判据

\[
\int^\infty\frac{R}{\log\mu(B_R(x))}\,dR=\infty
\]

成立，从而最小热核保守：

\[
\boxed{\int p_t(x,y)\,d\mu(y)=1.}
\]

因此问题 (b) 的答案是“是”，但仅针对题设所要求的**全局完备且全局满足 CD 下界的延拓**。一个有限 connector 自身带 exit 边界时，随机完备性并非自动结论；必须先平滑接到完整端，并保持相同曲率维数界。

---

## 5. 修正后的 resolvent 梯度估计

由 Cauchy–Schwarz 和热守恒，

\[
\int|\nabla_y p_t(x,y)|\,d\mu(y)
\le\sqrt{I(t)}.
\]

结合 (3.1)，

\[
\begin{aligned}
C_\kappa
&:=\sup_x\int|\nabla_yG_\kappa(x,y)|\,d\mu(y)\\
&\le
\int_0^\infty e^{-\kappa t}
\sqrt{\frac{NK}{1-e^{-2Kt}}}\,dt\\
&=
\frac{\sqrt{NK}}{2K}
B\!\left(\frac{\kappa}{2K},\frac12\right).
\end{aligned}
\]

本问题恰有 \(\kappa=2K\)，故

\[
B(1,\tfrac12)=2
\]

并得到简洁的通用界

\[
\boxed{
C_\kappa\le\sqrt{\frac NK}
=\frac{2}{\sqrt{3+\delta}}.}
\tag{5.1}
\]

原 Step 4 还有一个次要书写问题：即使原 Fisher 界成立，也只能用

\[
\sqrt{a+b}\le\sqrt a+\sqrt b,
\]

而不是等号；且

\[
\int_0^\infty e^{-\kappa t}\sqrt{\frac{N}{2t}}\,dt
=\sqrt{\frac{\pi N}{2\kappa}}.
\]

JSON 中的 \(1.13518\) 是积分错误 Fisher 上界所得，不能作为通用常数。较粗的 \(1.43157\) 型系数大于修正后的严格系数，所以基于它得到的保守阈值约 \(0.214212\) 仍然有效。

---

## 6. Resolvent 分部积分：可以严格化

利用 cutoff \(\chi_R\)，有

\[
\begin{aligned}
\int \chi_RG_\kappa\,\operatorname{div}_\sigma V\,d\mu
={}&-\int\chi_R\langle\nabla G_\kappa,V\rangle\,d\mu\\
&-\int G_\kappa\langle\nabla\chi_R,V\rangle\,d\mu.
\end{aligned}
\]

取 \(|\nabla\chi_R|\le C/R\)，并使用

\[
\int G_\kappa(x,y)\,d\mu(y)=\frac1\kappa,
\]

第二项趋于零。第一项因

\[
\int|\nabla G_\kappa|\,|V|\,d\mu
\le C_\kappa\|V\|_\infty
\]

绝对可积。因此

\[
\boxed{
R_\kappa[\operatorname{div}_\sigma V](x)
=-\int\langle\nabla_yG_\kappa(x,y),V(y)\rangle\,d\mu(y).}
\]

若 \(e\to0\)，则 \(e\) 和 \(V\) 有界，且 \(V\to0\)。事实上对 cutoff 极限而言，有界性已足够；“vanishes at infinity”是更强但方便的条件。

所以问题 (c) 的答案是肯定的。

---

## 7. 比较原理：成立；半群证明最干净

加权 Omori–Yau 原理可由有限维 \(CD(-K,N)\) 的加权 Laplacian comparison 推出；指数加权体积增长不是障碍。更直接地，若 \(e\) 有界且

\[
(-L+\kappa)e\le S,
\]

则 Duhamel 公式给出

\[
e\le e^{-\kappa T}P_Te+
\int_0^T e^{-\kappa t}P_tS\,dt.
\]

令 \(T\to\infty\)，因 \(\kappa>0\) 且 \(e\) 有界，

\[
e\le R_\kappa S.
\]

应用于

\[
S=\kappa^2+8\delta^2-2\operatorname{div}_\sigma V,
\]

并用 (5.1) 及 \(|V|\le2\delta\sqrt B\)，得到

\[
\boxed{
B:=\sup e
\le\kappa+\frac{8\delta^2}{\kappa}
+4\delta C_\kappa\sqrt B.}
\tag{7.1}
\]

因此问题 (d) 的答案也是肯定的；严格证明可完全绕开对经典点态 Omori–Yau 版本的依赖。

---

## 8. 二次闭合：正确

设

\[
\alpha=\kappa+\frac{8\delta^2}{\kappa},\qquad
\beta=4\delta C_\kappa.
\]

从 \(B\le\alpha+\beta\sqrt B\)，令 \(x=\sqrt B\)，解

\[
x^2-\beta x-\alpha\le0
\]

得到

\[
\boxed{
B\le
\left(\frac\beta2+
\sqrt{\frac{\beta^2}{4}+\alpha}\right)^2.}
\]

代入严格界 \(C_\kappa\le2/\sqrt{3+\delta}\)，有

\[
\alpha=2(3+\delta)+\frac{4\delta^2}{3+\delta},
\qquad
\beta=\frac{8\delta}{\sqrt{3+\delta}}.
\]

所以

\[
\boxed{
B\le\mathcal B(\delta):=
\left[
\frac{4\delta}{\sqrt{3+\delta}}
+
\sqrt{
2(3+\delta)+\frac{20\delta^2}{3+\delta}
}
\right]^2.}
\tag{8.1}
\]

---

## 9. 中心下界 \(12-8\delta\)：符号和系数正确

令中心三维超曲面为 \(\Sigma\)，其为全测地，单位法向为 \(\nu\)。写

\[
E=\operatorname{Ric}_g+3g,\qquad \|E\|_{\mathrm{op}}\le\delta.
\]

四维标量曲率为

\[
R_g=-12+\operatorname{tr}E,
\]

且

\[
\operatorname{Ric}_g(\nu,\nu)=-3+E(\nu,\nu).
\]

全测地 Gauss 方程因此给出

\[
R_\Sigma
=R_g-2\operatorname{Ric}_g(\nu,\nu)
=-6+D,
\]

其中

\[
D=\operatorname{tr}E-2E(\nu,\nu)
=\sum_{a=1}^3E(e_a,e_a)-E(\nu,\nu),
\]

故

\[
|D|\le4\delta.
\]

在中心写

\[
q=ds^2+G_{ab}(s)d\xi^ad\xi^b,\qquad
G=e^\sigma M,\qquad \rho=e^\sigma,
\]

并令

\[
h=\sigma_s=(\log\rho)_s.
\]

相应三维标量曲率恒等式为

\[
R_\Sigma=-2h_s-\frac32h^2-\frac12e.
\]

由于 \(\rho_s=\rho h\)，对中心圆按 \(d\mu=\rho\,ds\) 加权积分：

\[
\int -2h_s\rho\,ds
=2\int h\rho_s\,ds
=2\int h^2\rho\,ds.
\]

所以

\[
\langle R_\Sigma\rangle_\mu
=\frac12\langle h^2-e\rangle_\mu.
\]

结合 \(R_\Sigma=-6+D\)，得

\[
\langle e\rangle_\mu
=12-2\langle D\rangle_\mu+\langle h^2\rangle_\mu
\ge12-8\delta.
\]

因此

\[
\boxed{\langle e(0,\cdot)\rangle_\mu\ge12-8\delta}
\]

完全正确。这里 \(h=\sigma_s\)；源文件中某处写成 \(h=\sigma_s/2\) 是记号误写。该中心下界依赖完整四维 Gauss 方程及 \(\|E\|_{\mathrm{op}}\le\delta\)，不能仅由抽象 \(CD\) 下界推出。

---

## 10. 修正后的最终障碍

比较 (8.1) 与中心 floor。方程

\[
\mathcal B(\delta)=12-8\delta
\]

可化为

\[
9-12\delta-7\delta^2
=
8\delta\sqrt{(3+\delta)(3-2\delta)}.
\]

其第一个正根约为

\[
\boxed{\delta_*=0.24625.}
\]

故严格结论是：

> 对完整、自由 \(T^2\)、正交传递、光滑反射且具有完整 cusp 型延拓的 connector，若  
> \[
> \|E\|_{\mathrm{op}}\le\delta,\qquad e\to0
> \]
> 于所有端，并且上述耦合方程与全局 \(CD(-(3+\delta),4)\) 成立，则
> \[
> 0\le\delta<0.24625
> \]
> 时不存在这样的 connector。

原 \(\delta_0\simeq0.24885\) 应删除；它来自错误的 Fisher 上界。较保守的 \(\delta<0.214212\) 仍由更粗但足够大的 resolvent 常数保证。

该结论只覆盖 reflected、free-\(T^2\)、OT、完整 cusp 延拓这一类；不覆盖 approximate twist、奇异轨道、非 OT graph metric、仅有限长 approximate tail，或 \(N\#N\) 的 \(S^3\) neck。
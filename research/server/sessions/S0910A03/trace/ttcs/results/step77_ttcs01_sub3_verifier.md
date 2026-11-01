# TTCS Independent Branch Record

```json
{
  "step_id": 77,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step77_pe_scattering_correction.md",
    "Sessions/S0910A03/workspace/data/step77_pe_expansion.json",
    "Sessions/S0910A03/workspace/notes/step76_center_energy_transport_and_scattering.md",
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md"
  ]
}
```

## Task

Verify the following claims about reflected Einstein cores on [0,∞) × T³ with Ric = -3g and S(0) = 0 (totally geodesic T³ center).

1. FEFFERMAN-GRAHAM EXPANSION: In the geodesic defining function gauge with ρ = e^{-r}, the PE expansion g_ρ = γ - Sch(γ)ρ² + g₃ρ³ + O(ρ⁴) (n=3 boundary dimension) gives the shape operator:
   S = I + Sch(γ)♯ e^{-2r} - (3/2)γ⁻¹g₃ e^{-3r} + O(e^{-4r})
with Sch(γ) = Ric_γ - (R_γ/4)γ in dim 3, and g₃ transverse-traceless. Check the signs and coefficients.

2. MEAN CURVATURE: H = 3 + (R_γ/4)e^{-2r} + O(e^{-4r}), so e^{2R}(3-H(R)) → -R_γ/4.

3. NORMAL IDENTITY: From H' = -|S|² + 3 (Riccati for Ric=-3g), d/dr[e^{2r}(3-H)] = e^{2r}|S-I|², hence e^{2R}(3-H(R)) = 3 + ∫₀^R e^{2r}|S-I|²dr. Check whether the Riccati equation H' = -|S|² + 3 is correct for Ric=-3g in dim 4.

4. R_γ < -12: Combining: -R_γ/4 = 3 + ∫₀^∞ e^{2r}|S-I|²dr ≥ 3, so R_γ ≤ -12. Strict inequality because |S(0)-I|² = 3 > 0. Equality requires g = dr² + e^{2r}q₀ with Ric(q₀) = 0 (flat on T³), contradicting R(q₀) = -6.

5. ASD OBSTRUCTION: For an ASD Einstein 4-manifold with Ric=-3g, reflection across a totally geodesic T³ reverses orientation, forcing W⁺ → W⁻. By analyticity, both vanish near T³, giving W=0 and constant sectional curvature -1. T³ cannot embed totally geodesically in H⁴ (Preissmann). Check whether the analyticity argument is correct.

6. THREE-OBJECT DISTINCTION: The center metric q₀ (at S=0, R(q₀)=-6) and conformal infinity γ (at r→∞, R_γ<-12) are at opposite ends. Imposing R(γ)=-6 as done in Step 76 Section 9 is not a necessary condition. The nonlocal datum g₃ (not γ) carries filling information.

Check each claim independently. Identify any sign errors, coefficient errors, or logical gaps.

## Output

# 科学复核备忘

以下采用
\[
g=dr^2+q_r=\rho^{-2}(d\rho^2+g_\rho),\qquad \rho=e^{-r},
\]
并约定法向指向 \(r\) 增大方向，
\[
S=\frac12q_r^{-1}\partial_rq_r .
\]
还需假设同一个高斯坐标 \(r\) 从 \(r=0\) 的全测地 \(T^3\) 一直延伸到 PE 无穷远。所有涉及 \(R_\gamma\) 的公式均逐点成立，积分沿固定法向射线进行。

## 1. Fefferman–Graham 展开

由
\[
q_r=e^{2r}g_\rho
\]
可得
\[
S=I+\frac12g_\rho^{-1}\partial_rg_\rho
  =I-\frac{\rho}{2}g_\rho^{-1}\partial_\rho g_\rho.
\]
写成
\[
g_\rho=\gamma+g_2\rho^2+g_3\rho^3+O(\rho^4),
\qquad g_2=-\operatorname{Sch}(\gamma),
\]
则
\[
S
=I-g_2^\sharp\rho^2-\frac32g_3^\sharp\rho^3+O(\rho^4),
\]
所以
\[
\boxed{
S=I+\operatorname{Sch}(\gamma)^\sharp e^{-2r}
-\frac32\gamma^{-1}g_3e^{-3r}+O(e^{-4r}).
}
\]

在三维，
\[
\operatorname{Sch}(\gamma)
=\operatorname{Ric}_\gamma-\frac{R_\gamma}{4}\gamma.
\]
对于光滑 PE Einstein 四维度量，
\[
\operatorname{tr}_\gamma g_3=0,\qquad
\operatorname{div}_\gamma g_3=0.
\]

因此符号及 \(-3/2\) 系数均正确。`step77_pe_expansion.json` 中的记法
\(B_2=\gamma^{-1}g_2=-\operatorname{Sch}^\sharp\) 与
\(S-I=-B_2e^{-2r}-\frac32B_3e^{-3r}\) 也是一致的。若改用相反法向定义 \(S\)，所有相关符号会同时改变；当前约定与后面的 Riccati 方程相容。

## 2. 平均曲率

取迹得到
\[
H
=3+\operatorname{tr}_\gamma\operatorname{Sch}(\gamma)e^{-2r}
-\frac32\operatorname{tr}_\gamma(g_3)e^{-3r}
+O(e^{-4r}).
\]
因为
\[
\operatorname{tr}_\gamma\operatorname{Sch}(\gamma)
=R_\gamma-\frac34R_\gamma=\frac14R_\gamma
\]
且 \(g_3\) 无迹，
\[
\boxed{
H=3+\frac{R_\gamma}{4}e^{-2r}+O(e^{-4r}).
}
\]
因此逐点有
\[
\boxed{
\lim_{R\to\infty}e^{2R}(3-H(R))
=-\frac14R_\gamma.
}
\]
这里 \(R_\gamma\) 一般是 \(T^3\) 上的函数，并非自动为常数。

## 3. 法向恒等式

高斯坐标中的法向 Ricci 分量为
\[
\operatorname{Ric}(\partial_r,\partial_r)
=-H'-|S|^2.
\]
由 \(\operatorname{Ric}=-3g\) 得
\[
\boxed{H'=3-|S|^2.}
\]
令 \(B=S-I\)。在三维截面上，
\[
|S|^2=|B|^2+2(H-3)+3,
\]
故
\[
(H-3)'+2(H-3)+|S-I|^2=0.
\]
等价地，
\[
\boxed{
\frac{d}{dr}\bigl[e^{2r}(3-H)\bigr]
=e^{2r}|S-I|^2.
}
\]
中心处 \(S(0)=0\)，所以 \(H(0)=0\)，积分给出
\[
\boxed{
e^{2R}(3-H(R))
=3+\int_0^R e^{2r}|S-I|^2\,dr.
}
\]
Riccati 方程及其符号均正确。

## 4. \(R_\gamma<-12\)

PE 展开给出 \(|S-I|=O(e^{-2r})\)，所以加权被积函数为
\(O(e^{-2r})\)，积分收敛。结合前两节，
\[
\boxed{
-\frac14R_\gamma(x)
=3+\int_0^\infty e^{2r}|S-I|^2(r,x)\,dr,
}
\]
即
\[
\boxed{
R_\gamma(x)
=-12-4\int_0^\infty e^{2r}|S-I|^2(r,x)\,dr<-12.
}
\]
严格性直接来自
\[
|S(0)-I|^2=|-I|^2=3.
\]
由连续性，每条法向射线上都有一个正长度区间使被积函数为正。

中心标量曲率也确实满足
\[
R(q_0)
=R(g)-2\operatorname{Ric}(n,n)+H^2-|S|^2
=-12+6=-6.
\]

若积分为零，则光滑性会给出 \(S\equiv I\)，这已经与 \(S(0)=0\) 矛盾。脱离中心条件单独考虑 \(S\equiv I\) 时，
\[
q_r=e^{2r}q_*
\]
且 Einstein 方程要求 \(\operatorname{Ric}(q_*)=0\)；三维 \(T^3\) 上这意味着平坦。因而笔记中的 warped-product 说明是正确的，但严格性并不需要它。

### 代表元归一化问题

数值阈值 \(-12\) 只适用于由“中心在 \(r=0\)、\(\rho=e^{-r}\)”选出的代表元，不适用于 \([\gamma]\) 中的任意代表元。若
\[
\widetilde\rho=a\rho,\qquad
\widetilde r=r-\log a,\qquad
\widetilde\gamma=a^2\gamma,
\]
则中心位于 \(\widetilde r_0=-\log a\)，相应公式变成
\[
-\frac14R_{\widetilde\gamma}
=3e^{2\widetilde r_0}
+\int_{\widetilde r_0}^\infty
e^{2\widetilde r}|S-I|^2\,d\widetilde r.
\]
这与 \(R_{\widetilde\gamma}=a^{-2}R_\gamma\) 相容。若仅说“conformal infinity \([\gamma]\) 满足 \(R_\gamma<-12\)”而不指定代表元，则表述不成立。

## 5. ASD 排除论证

结论成立，但反射步骤需要补足。

对于一般光滑度量，“全测地”本身并不自动产生局部等距反射。这里可利用 Einstein 方程：在高斯坐标中，中心数据为
\[
q(0)=q_0,\qquad q'(0)=0.
\]
Einstein 演化方程在 \(r\mapsto-r\) 下不变，且所有奇数阶法向 jet 由方程递推为零。等价地，可调用 Einstein Cauchy 数据的局部唯一性。由此偶延拓产生光滑 Einstein 双面邻域，映射
\[
\iota(r,x)=(-r,x)
\]
才成为反向定向的局部等距映射。

在双面邻域上选定定向。若原侧 \(W^+=0\)，则：

1. Einstein 度量在调和坐标中实解析，所以 \(W^+=0\) 从一个开集解析延拓到邻域；
2. \(\iota\) 反向定向，交换 \(\Lambda^2_+\) 与 \(\Lambda^2_-\)，故在反射侧有 \(W^-=0\)；
3. 因而邻域内 \(W^+=W^-=0\)，即 \(W=0\)。

Einstein 条件 \(\operatorname{Ric}=-3g\) 随即给出截面曲率恒为 \(-1\)。全测地中心继承截面曲率 \(-1\)，但紧 \(T^3\) 不可能承载严格负截面曲率度量：Preissmann 定理与
\(\pi_1(T^3)=\mathbb Z^3\) 矛盾。

因此 ASD Einstein 四维度量不能含有这样的紧全测地 \(T^3\)。

符号
\[
\operatorname{Rm}=-g\owedge g
\]
取决于 Kulkarni–Nomizu 乘积约定。若
\[
(g\owedge g)_{ijkl}
=2(g_{ik}g_{jl}-g_{il}g_{jk}),
\]
则应写成
\[
\operatorname{Rm}=-\frac12g\owedge g.
\]
几何上无歧义的陈述是“截面曲率恒为 \(-1\)”。

## 6. 三个对象及 \(g_3\)

三者确实不同：

- \(q_0\)：中心 \(r=0\) 的实际诱导度量，满足 \(R(q_0)=-6\)；
- \(\gamma\)：由中心归一化高斯坐标选出的无穷远代表元，满足逐点 \(R_\gamma<-12\)；
- \(g_3\)：固定 \(\gamma\) 后的 TT 系数，是 PE 展开中未由局部曲率公式决定的 Neumann 型数据。

所以在 Step 76 §9 中要求 \(R(\gamma)=-6\) 确实混淆了两个不同位置的度量；它既不是产生全测地中心所需的方程，在中心归一化代表元下还与 \(R_\gamma<-12\) 相冲突。

更准确地说，\(\gamma\) 给出 Dirichlet 数据及局部系数 \(g_2\)，而 \(g_3\) 给出相对于固定 \(\gamma\) 的附加非局域响应。FG 递推表明 \((\gamma,g_3)\) 决定完整形式展开，但仅凭该递推不能推出每个 TT 张量都可由整体 filling 实现，也不能推出整体 filling 与 \(g_3\) 之间自动双射。

相应的有限量是
\[
\boxed{
e^{3r}\left[
S^\circ-\operatorname{Sch}(\gamma)^{\circ\sharp}e^{-2r}
\right]
\longrightarrow
-\frac32\gamma^{-1}g_3.
}
\]
笔记中另有两处需要同步修正：
\[
e^{3r}S^\circ
=e^r\operatorname{Sch}(\gamma)^{\circ\sharp}
-\frac32\gamma^{-1}g_3+O(e^{-r}),
\]
故未减去局部 Schouten 项时，\(e^{3r}S^\circ\) 一般不有界。Step 77 §3 所说的“\(e^{3a}P\) 趋于有限值”以及 §6 所说的“\(e^{3r}S^\circ\) 有界”，仅在
\(\operatorname{Sch}(\gamma)^\circ=0\) 等特殊情形成立；一般情形必须使用上面的重整化表达式。

## 总结

1–3 的符号和系数正确。第4项对中心归一化的无穷远代表元逐点成立，但不能直接表述为整个共形类的固定数值性质。第5项结论正确，证明中必须先建立 Einstein 偶延拓和局部等距反射；解析性随后才能交换并消去 \(W^\pm\)。第6项的几何区分正确，但“\(g_3\) 携带全部 filling 信息”应理解为固定 \(\gamma\) 后的形式 Neumann 数据；未重整化的 \(e^{3r}S^\circ\) 一般会发散。
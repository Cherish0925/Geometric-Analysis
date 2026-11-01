# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 77,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step77_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step77_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

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

## Integrated Scientific Memo

# 核验结论

固定约定
\[
g=dr^2+q_r=\rho^{-2}(d\rho^2+g_\rho),\qquad \rho=e^{-r},
\]
法向指向 \(r\to+\infty\)，并定义
\[
S=\frac12q_r^{-1}\partial_rq_r,\qquad H=\operatorname{tr}S.
\]
还必须假设该高斯距离坐标从中心 \(r=0\) 无焦点地延伸到 PE 端。以下关于 \(R_\gamma\) 的等式均是沿法向射线的逐点等式。

## 1. Fefferman–Graham 展开：正确

由 \(q_r=e^{2r}g_\rho\)，
\[
S=I+\frac12g_\rho^{-1}\partial_rg_\rho
  =I-\frac{\rho}{2}g_\rho^{-1}\partial_\rho g_\rho.
\]
代入
\[
g_\rho=\gamma-\operatorname{Sch}(\gamma)\rho^2+g_3\rho^3+O(\rho^4)
\]
得到
\[
\boxed{
S=I+\operatorname{Sch}(\gamma)^\sharp e^{-2r}
-\frac32\gamma^{-1}g_3e^{-3r}+O(e^{-4r}).
}
\]
符号与 \(-3/2\) 系数均正确。三维边界上
\[
\operatorname{Sch}(\gamma)
=\operatorname{Ric}_\gamma-\frac{R_\gamma}{4}\gamma,
\]
而光滑四维 PE Einstein 度量满足
\[
\operatorname{tr}_\gamma g_3=0,\qquad
\operatorname{div}_\gamma g_3=0.
\]

相反法向约定会同时改变 \(S\) 及 Riccati 公式中的相关符号；上述约定与后续恒等式一致。

## 2. 平均曲率：正确

取迹并使用 \(g_3\) 无迹：
\[
\operatorname{tr}_\gamma\operatorname{Sch}(\gamma)
=R_\gamma-\frac34R_\gamma=\frac14R_\gamma,
\]
故
\[
\boxed{
H=3+\frac{R_\gamma}{4}e^{-2r}+O(e^{-4r}),
}
\]
从而
\[
\boxed{
\lim_{R\to\infty}e^{2R}(3-H(R))
=-\frac14R_\gamma.
}
\]
这里 \(R_\gamma\) 一般是 \(T^3\) 上的函数，不必为常数。

## 3. 法向 Riccati 恒等式：正确

高斯坐标下
\[
\operatorname{Ric}(\partial_r,\partial_r)=-H'-|S|^2.
\]
由于 \(\operatorname{Ric}=-3g\)，
\[
\boxed{H'=3-|S|^2.}
\]
又因切片维数为 \(3\)，
\[
|S-I|^2=|S|^2-2H+3,
\]
所以
\[
\boxed{
\frac d{dr}\bigl[e^{2r}(3-H)\bigr]
=e^{2r}|S-I|^2.
}
\]
中心满足 \(S(0)=0\)、\(H(0)=0\)，于是
\[
\boxed{
e^{2R}(3-H(R))
=3+\int_0^R e^{2r}|S-I|^2\,dr.
}
\]

## 4. \(R_\gamma<-12\)：对中心归一化代表元正确

由 FG 展开 \(S-I=O(e^{-2r})\)，故加权积分收敛。令 \(R\to\infty\) 得到逐点公式
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
|S(0)-I|^2=3;
\]
连续性保证每条法线上积分严格为正，无需额外 equality 分类。

中心标量曲率确为
\[
R(q_0)=R(g)-2\operatorname{Ric}(n,n)=-12+6=-6.
\]

“等号迫使 \(S\equiv I\)”的辅助论证也成立：此时
\[
g=dr^2+e^{2r}q_*
\]
且 Einstein 方程迫使 \(\operatorname{Ric}(q_*)=0\)，三维下因而平坦。但它与 \(S(0)=0\) 已直接矛盾。

### 必要的归一化限定

阈值 \(-12\) 不是整个共形类的共形不变量，只适用于由中心锚定的
\[
r(0)=0,\qquad \rho=e^{-r}
\]
所选出的代表元 \(\gamma\)。若 \(\widetilde\rho=a\rho\)，则
\(\widetilde\gamma=a^2\gamma\)，中心在
\(\widetilde r_0=-\log a\)，相应公式变为
\[
-\frac14R_{\widetilde\gamma}
=3e^{2\widetilde r_0}
+\int_{\widetilde r_0}^{\infty}
e^{2\widetilde r}|S-I|^2\,d\widetilde r.
\]
因此不应无条件写成“共形无穷远 \([\gamma]\) 的任意代表元满足 \(R<-12\)”。

## 5. ASD 排除：结论正确，但原证明缺少反射延拓引理

单凭“一条超曲面全测地”并不对任意光滑度量自动产生局部等距反射。这里须先利用 Einstein 方程建立偶延拓：

\[
q(0)=q_0,\qquad q'(0)=0.
\]
方程在 \(r\mapsto-r\) 下不变；通过 Einstein Cauchy 数据的局部唯一性，或在适当规范下递推所有奇数阶法向 jet 为零，可将度量光滑地加倍，使
\[
\iota(r,x)=(-r,x)
\]
成为反定向局部等距映射。

在该 Einstein 双面邻域上：

1. 原侧 ASD，故某定向下 \(W^+=0\)；
2. 反定向等距映射交换 \(\Lambda^2_+\) 与 \(\Lambda^2_-\)，因此反射侧 \(W^-=0\)；
3. Einstein 度量在调和坐标中实解析。由两个条件分别在开集上成立，解析唯一延拓给出整个连通邻域内
   \[
   W^+=W^-=0.
   \]

所以 \(W=0\)。再结合 \(\operatorname{Ric}=-3g\)，得到截面曲率恒为 \(-1\)。全测地中心由 Gauss 方程继承截面曲率 \(-1\)，但紧 \(T^3\) 不可能承载严格负截面曲率度量，因为 Preissmann 定理与
\[
\pi_1(T^3)=\mathbb Z^3
\]
矛盾。

因此 ASD Einstein 四维流形不能含这种紧全测地 \(T^3\)；同理，任何候选反射核既不能 ASD，也不能 SD。

笔记中的
\[
\operatorname{Rm}=-g\owedge g
\]
依赖 Kulkarni–Nomizu 规范。若
\[
(g\owedge g)_{ijkl}
=2(g_{ik}g_{jl}-g_{il}g_{jk}),
\]
则正确系数是 \(-\tfrac12g\owedge g\)。无歧义陈述应为“截面曲率恒为 \(-1\)”。

## 6. \(q_0,\gamma,g_3\) 的区分：正确，但需限制对 \(g_3\) 的表述

三个对象确实不同：

- \(q_0\)：中心的实际诱导度量，满足 \(R(q_0)=-6\)；
- \(\gamma\)：PE 无穷远的一个代表元；在中心锚定规范中逐点满足 \(R_\gamma<-12\)；
- \(g_3\)：固定 \(\gamma\) 后，FG 展开中未由局部边界曲率递推决定的 TT、Neumann 型数据。

因此 Step 76 §9 把 \(R(q_0)=-6\) 强加给无穷远代表元是对象混淆，不是全测地中心的必要条件。若其 \(q_\partial\) 甚至不是中心锚定的代表元，则也不能仅凭数值 \(-6\) 与 \(-12\) 比较；真正错误仍是把中心条件施加于无穷远数据。

更精确地说，\(g_3\) 是固定 \(\gamma\) 后的形式非局域响应数据。FG 递推说明 \((\gamma,g_3)\) 决定形式渐近展开，但不能据此断言：

- 每个 TT 张量都由某个全局 filling 实现；
- \(g_3\) 与全局 filling 自动一一对应；
- 不同全局 filling 必然由 \(g_3\) 唯一区分。

正确的重整化极限是
\[
\boxed{
e^{3r}\left[
S^\circ-\operatorname{Sch}(\gamma)^{\circ\sharp}e^{-2r}
\right]
\longrightarrow-\frac32\gamma^{-1}g_3.
}
\]

这同时纠正 Step 77 的另一处陈述：一般而言
\[
e^{3r}S^\circ
=e^r\operatorname{Sch}(\gamma)^{\circ\sharp}
-\frac32\gamma^{-1}g_3+O(e^{-r}),
\]
所以未经减去 Schouten 项的 \(e^{3r}S^\circ\) 通常发散。只有当
\(\operatorname{Sch}(\gamma)^\circ=0\) 等特殊条件成立时，它才可能有界。因而 Step 77 §3 的“\(e^{3a}P\) 趋于有限极限”及 §6 的“\(e^{3r}S^\circ\) 有界”不能作为一般结论；应使用上述重整化应力。

## 附带发现的局部展开问题

Step 77 §7B 中
\[
|S-I|^2=3-6r+\frac{27}{2}r^2+\cdots
\]
不成立为已证下界。实际二阶系数含有
\[
|S'(0)|^2-\operatorname{tr}S''(0),
\]
而笔记遗漏了 \(-\operatorname{tr}S''(0)\)。即使中心定理给出
\(|S'(0)|^2\ge27\)，若无 \(\operatorname{tr}S''(0)\) 的符号控制，也不能推出所写二阶下界。

另外，即使只用
\[
|S-I|^2=3-6r+O(r^2),
\]
乘上 \(e^{2r}\) 后线性项抵消，因此相应积分不是笔记写的
\(3\varepsilon-3\varepsilon^2+O(\varepsilon^3)\)，而是
\[
3\varepsilon+O(\varepsilon^3).
\]
这不影响积分严格为正或 \(R_\gamma<-12\)。

**总判定：** 第 1–4 项在指定规范下正确；第 5 项结论正确但必须补上 Einstein 偶延拓/局部反射论证；第 6 项的对象区分正确，但 \(R_\gamma<-12\) 只属于中心归一化代表元，而 \(g_3\) 应称为形式 Neumann 数据，不能未经全局唯一性定理提升为 filling 的完整分类数据。
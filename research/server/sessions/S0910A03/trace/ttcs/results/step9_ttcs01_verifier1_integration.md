# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 9,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step9_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step9_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify or refute the following regularity claim and identify the precise obstruction if false:

CLAIM (the regularity question): On a 4-dimensional Riemannian ball (B_1(p), g) with Ric ≥ -3g that arises as the local universal cover of a collapsed near-Einstein ball, suppose:
(a) fint_{B_r(p)} |Rm|² ≤ K for all 0 < r ≤ 1/3 (controlled maximal curvature function)
(b) Ric ≥ -(1+δ)(n-1)g with δ small

Does (a)+(b) force Vol(B_{r*}(p)) ≥ c(K)r*⁴ for some fixed r*(K) > 0?

Consider:
1. Known ε-regularity theorems (Anderson, Cheeger-Naber) and whether they apply without noncollapse as input
2. Whether the 4D conformal invariance of ∫|Rm|² adds structure
3. Whether a countermodel exists: a collapsed ball with Ric ≥ -3g, controlled normalized curvature mean at every scale, and Vol → 0
4. The distinction between 'local universal cover' and 'arbitrary ball' - the cover has no short loops
5. Whether Naber-Zhang Prop 6.4 hypotheses (GH model, maximal rank, model noncollapsing) follow from (a)+(b)

Give a precise mathematical assessment, not a survey.

## Integrated Scientific Memo

## 结论

该正则性断言为 **假**。事实上，即使把条件加强为

\[
\operatorname{Ric}_g=-g
\]

且在所考察区域有一致的点态曲率界，也不能推出局部普适覆盖在某个固定尺度上的四维非塌缩。

精确障碍不是曲率集中，而是：

\[
\boxed{\text{塌缩纤维在较大的覆盖域内可缩，因而局部普适覆盖不会将其解开。}}
\]

换言之，普适覆盖只解开在覆盖域基本群中非平凡的短环；它不能消除短的 **可缩** 纤维。对应于 Naber–Zhang 的语言，这正是纤维化基本群的秩下降，而非最大秩。

---

## 一个满足精确 near-Einstein 背景的反例

取 \(\ell=\sqrt3\)，\(\nu>0\)，令

\[
F_\nu(r)=
\frac{r-\nu}{r+\nu}
\left(1+\frac{(r-\nu)(r+3\nu)}{\ell^2}\right),
\qquad r\geq \nu ,
\]

并考虑 Taub–NUT–AdS 度量

\[
g_\nu=
\frac{dr^2}{F_\nu(r)}
+(r^2-\nu^2)(d\theta^2+\sin^2\theta\,d\phi^2)
+4\nu^2F_\nu(r)(d\psi+\cos\theta\,d\phi)^2,
\tag{1}
\]

其中 \(\phi\) 周期为 \(2\pi\)，\(\psi\) 周期为 \(4\pi\)。该标准规范化满足

\[
\operatorname{Ric}_{g_\nu}
=-\frac3{\ell^2}g_\nu=-g_\nu.
\tag{2}
\]

因此它同时满足题中的两个 Ricci 下界，包括
\(\operatorname{Ric}\ge -3g\) 和
\(\operatorname{Ric}\ge-3(1+\delta)g\)，甚至 \(\delta=0\)。

在 \(r=\nu\) 处令

\[
r=\nu+\frac{\rho^2}{8\nu}.
\]

由于

\[
F_\nu(r)=\frac{\rho^2}{16\nu^2}+O(\rho^4),
\]

(1) 在该点展开为

\[
d\rho^2+\frac{\rho^2}{4}
\left[d\theta^2+\sin^2\theta\,d\phi^2+
(d\psi+\cos\theta\,d\phi)^2\right]+O(\rho^4),
\]

故 \(r=\nu\) 是光滑的 nut，不是奇点。

设

\[
t_\nu(r)=\int_\nu^rF_\nu(u)^{-1/2}\,du
\]

为到 nut 的径向距离，并选中心 \(p_\nu\) 使

\[
d(p_\nu,\mathrm{nut})=\frac12.
\]

若 \(q\in B_{1/3}(p_\nu)\)，则

\[
\frac16<d(q,\mathrm{nut})<\frac56.
\tag{3}
\]

因此这些球全部处于与 nut 一致分离的固定尺度环带。在这个环带上，随 \(\nu\to0\) 的曲率张量一致有界；于是存在与 \(\nu\) 无关的 \(K_0<\infty\)，使

\[
\sup_{B_{1/3}(p_\nu)}|\operatorname{Rm}_{g_\nu}|^2\le K_0.
\tag{4}
\]

从而对全部 \(0<r\le1/3\),

\[
\fint_{B_r(p_\nu)}|\operatorname{Rm}_{g_\nu}|^2\le K_0.
\tag{5}
\]

这比条件 (a) 更强。

另一方面，体积形式为

\[
d\mu_{g_\nu}
=
2\nu(r^2-\nu^2)\sin\theta\,
dr\,d\theta\,d\phi\,d\psi .
\tag{6}
\]

对每个固定 \(s\le1/3\)，球 \(B_s(p_\nu)\) 所在的径向区间保持在固定紧集内，故

\[
\operatorname{Vol}_{g_\nu}(B_s(p_\nu))\le C_s\nu,
\tag{7}
\]

于是

\[
\frac{\operatorname{Vol}_{g_\nu}(B_s(p_\nu))}{s^4}\longrightarrow0.
\tag{8}
\]

---

## 为什么局部普适覆盖仍然塌缩

令

\[
U_\nu=B_1(p_\nu).
\]

通过 \(p_\nu\) 的短 \(\psi\)-轨道长度为 \(O(\nu)\)。它可以沿径向扫到 nut；由于 nut 距 \(p_\nu\) 为 \(1/2\)，该收缩圆盘完整包含在 \(U_\nu\) 内。因此短纤维在

\[
\pi_1(U_\nu)
\]

中是平凡元素。

取包含 \(B_{1/3}(p_\nu)\) 的环带子域 \(W_\nu\Subset U_\nu\)。它在该环带内是一个以短 \(\psi\)-圆为纤维的圆丛，并可选其底域为可缩域，所以

\[
\pi_1(W_\nu)\cong\mathbb Z.
\]

但包含映射诱导的同态

\[
\pi_1(W_\nu)\longrightarrow\pi_1(U_\nu)
\]

为零，因为生成元通过 nut 收缩。故 \(W_\nu\) 在 \(U_\nu\) 的普适覆盖中的每个连通提升都一一映到 \(W_\nu\)，而不是把短圆展开为直线。

因此若 \(\tilde p_\nu\) 是 \(p_\nu\) 的一个提升，则对每个固定
\(s\le1/3\),

\[
B_s(\tilde p_\nu)\cong B_s(p_\nu)
\]

（至少位于上述一一提升的环带分支内），从而

\[
\operatorname{Vol}(B_s(\tilde p_\nu))
\le C_s\nu\longrightarrow0.
\tag{9}
\]

所以不存在仅依赖 \(K_0\) 的固定 \(r_*(K_0)>0\) 和 \(c(K_0)>0\)，使所有此类覆盖球满足

\[
\operatorname{Vol}(B_{r_*}(\tilde p_\nu))
\ge c(K_0)r_*^4.
\]

这里应将 \(r_*\) 理解为位于已控制的内部尺度（例如 \(r_*\le1/3\)）；这正是所需正则性桥梁的尺度范围。

---

## 五个指定问题的精确判定

### 1. Anderson、Cheeger–Naber 不能补上非塌缩

这些定理以非塌缩为输入，而不是由小曲率能量产生非塌缩。

本例中甚至有

\[
\int_{B_s(p_\nu)}|\operatorname{Rm}|^2
\le K_0\,\operatorname{Vol}(B_s(p_\nu))
=O(\nu)\to0,
\]

但体积比仍趋于零。因此，即使绝对 \(L^2\) 曲率能量趋零，也不能在没有体积比或 Sobolev 常数下推出 harmonic radius 下界。

Cheeger–Naber 的有界 Ricci、余维四正则性同样建立在定量非塌缩假设上，不能倒用来证明该假设。

### 2. 四维 \(\int|\mathrm{Rm}|^2\) 的尺度不变性无济于事

该不变性针对整体同尺度缩放。此处是各向异性塌缩：圆方向长度为 \(O(\nu)\)，底部三维几何保持固定尺度。因此球体积和绝对曲率能量都为 \(O(\nu)\)，而归一化曲率均值保持有界。

故四维临界性不提供体积比、Sobolev 常数或注入半径下界。

### 3. 反模型确实存在

上述 Taub–NUT–AdS 环带同时具有：

\[
\operatorname{Ric}=-g,\qquad
\sup|\mathrm{Rm}|\le C,\qquad
\fint_{B_r}|\mathrm{Rm}|^2\le K_0
\]

以及

\[
\operatorname{Vol}(B_s)\to0
\]

对任意固定 \(s\le1/3\)。因此它比题目所要求的反模型更强。

### 4. “局部普适覆盖没有短环”这一说法不正确

正确说法是：普适覆盖没有代表覆盖域基本群非平凡元素的闭环。它仍可包含任意短的可缩闭曲线。

本例的短圆在测试环带内看似为纤维生成元，但在更大的单位球内经 nut 收缩，因此提升并不展开它。这正说明“local universal cover”不能替代最大秩条件。

### 5. Naber–Zhang Proposition 6.4 的假设不由 (a)+(b) 推出

本例的环带 GH 收敛到一个固定尺度的非塌缩三维模型；事实上极限底度量为

\[
h_0=\frac{dr^2}{1+r^2/3}+r^2d\Omega_2^2,
\]

即截面曲率 \(-1/3\) 的双曲三空间。因此 GH 模型和模型非塌缩尺度都不是问题。

极限维数 \(k=3\)，所以最大纤维化幂零秩应为

\[
4-k=1.
\]

但短圆生成元在 \(U_\nu=B_1(p_\nu)\) 中可缩，故相应纤维化基本群的秩为 \(0\)。恰好是

\[
0<4-k.
\]

因此失败的 Naber–Zhang 假设是 **最大秩**。条件 (a)+(b) 对短纤维在缓冲域基本群中是否存活完全没有控制。

---

## 对两类简化反例的说明

Berger 球面乘直线也可直接反驳只写出的 Ricci 下界版本：

\[
(S^3,g_\varepsilon)\times\mathbb R,
\qquad
g_\varepsilon=\varepsilon^2\sigma_1^2+\sigma_2^2+\sigma_3^2.
\]

它可满足 \(\operatorname{Ric}\ge0\)、一致点态曲率界，并沿可缩 Hopf 圆塌缩；空间本身甚至单连通。不过它不是 \(\operatorname{Ric}\approx-g\)，所以单独使用时不能完全回应“collapsed near-Einstein ball”的背景限定。Taub–NUT–AdS 反例消除了这一歧义，因为它精确满足 \(\operatorname{Ric}=-g\)。

---

## 最终数学判定

\[
\boxed{(a)+(b)\ \text{不推出任何固定尺度的四维体积下界。}}
\]

更强的点态曲率界、绝对 \(L^2\) 曲率小性乃至精确负 Einstein 方程都不足以排除这一现象。缺失的拓扑—几何信息是：

\[
\boxed{\text{短塌缩纤维必须在缓冲域基本群中存活，亦即纤维化基本群达到最大秩。}}
\]

这正是 Naber–Zhang 作为独立假设加入、而不能从曲率均值和 Ricci 下界导出的内容。
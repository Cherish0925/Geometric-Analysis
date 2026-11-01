# TTCS Independent Branch Record

```json
{
  "step_id": 17,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step17_normalized_cutoff_flow_theorem.md",
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A01/workspace/notes/step17_support_scale_li_bootstrap.md"
  ]
}
```

## Task

The normalized cutoff flow ∂_t g = -2χ²(Ric+g) has the property that |E| = |Ric+g| satisfies a maximum principle with bounded Gronwall factor. A01's Step 17 note identifies the transition-inclusive continuation theorem as the single remaining bridge. The maximum principle breaks the metric-comparability circle (their TTCS correction (c)). Given this, investigate whether the FULL coupled system (curvature energy + defect energy on the transition region) can be closed self-consistently. The specific question: A01's Section 5.5 argues that the 4D Sobolev-energy product C_S·||Rm||_{L²} = O(r*²) absorbs the dangerous ∫|Rm||E|² term in the defect energy inequality. If the maximum principle gives |E(t)| ≤ √2·δ independently, does this eliminate the need for a separate transition curvature bootstrap? Consider: (a) On the transition, the metric barely drifts (O(δr²)), so Sobolev constants and ball volumes are preserved. (b) The curvature evolution on the transition has the extra terms ∇²(χ²)·E and ∇(χ²)·∇E, but both are O(δ/r²) and O(|∇E|/r). (c) For the integrated curvature energy on the transition, the ∇(χ²)·∇E·Rm cross term can be absorbed by the defect gradient dissipation from the coupled system. Determine whether the full continuation package (a)-(e) from A01 Section 9 follows from the maximum principle + Sobolev-energy cancellation, or whether a genuinely new analytical input is still needed.

## Output

### 核心结论

即使把
\[
\|E(t)\|_\infty\le \sqrt2\,\delta
\]
作为一个外加的、在统一时间段内成立的估计，四维 Sobolev–曲率能量消去确实足以闭合**过渡环带上的耦合 \(L^2\) 能量系统**。它可给出 A01 中 (e) 的局部临界曲率能量保持，并同时控制缺陷梯度耗散。

但它不能单独推出过渡环带上的
\[
|\chi^2\Rm|\le C/t,
\]
也不能保证光滑解存在到统一时间 \(\theta r_*^2\)。更关键的是，所述 \(\|E(t)\|_\infty\) maximum principle 本身并不独立于当前曲率：其 Gronwall 系数含有 \(\|\chi^2\Rm(t)\|_\infty\)。因此，实际初始资料下仍需一个新的加权抛物正则性与延拓定理。最大值估计并未真正移除过渡环带的曲率问题。

## 1. 缺陷 maximum principle 仍含当前 Weyl 曲率

先看平台区 \(a=\chi^2=1\)。按笔记中的 \(\Delta_L\) 约定，
\[
\partial_tE=\Delta_LE-2E.
\]
计算 \(|E|^2\) 时还必须加入逆度量变化
\[
\partial_tg^{-1}=2E^\sharp,
\qquad
(\partial_t|E|^2)_{\text{norm}}=4\operatorname{tr}(E^3).
\]
它恰好消去 Step 17 中残留的三次项，得到更简洁但更关键的恒等式
\[
\boxed{
(\partial_t-\Delta)|E|^2
=-2|\nabla E|^2+4R_{ikjl}E_{ij}E_{kl}.
}
\tag{1}
\]
所以 pointwise 反应项不是 \(O(\delta)|E|^2\)，而是
\[
4\Rm(E,E)\le 4|\Rm|\,|E|^2.
\]
Ricci 接近 \(-g\) 并不控制 Weyl 张量；在代数曲率层面，固定 Ricci 部分时 Weyl 算子的模可以任意大，并可令 \(E^\circ\) 对准其大特征方向。

对一般 \(a=\chi^2\)，schematic maximum-principle 形式为
\[
(\partial_t-a\Delta)|E|^2
\le
-c\,a|\nabla E|^2
+C\left(
a|\Rm|+1+\frac{|\nabla a|^2}{a}+|\nabla_g^2a|
\right)|E|^2.
\tag{2}
\]
由于
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le Cr^{-2},
\]
一阶 cutoff 项没有 \(1/\chi\) 奇性；但 \(a|\Rm|\) 仍在。于是
\[
\|E(t)\|_\infty^2
\le
\|E(0)\|_\infty^2
\exp\!\left[
C\int_0^t
\bigl(1+r^{-2}+\|a\Rm(s)\|_\infty
+\|\nabla_g^2a(s)\|_\infty\bigr)\,ds
\right].
\tag{3}
\]

初始 \(K_0=\|\Rm(g_0)\|_\infty\) 不能替代式 (3) 中的当前曲率。度量的 \(C^0\) 小漂移不控制其二阶导数，彼此任意接近的度量可以有完全不同的曲率。同样，
\[
\nabla_g^2a-\nabla_{g_0}^2a
=(\Gamma(g_0)-\Gamma(g))*da,
\]
所以双 Lipschitz 等价只保持 \(|da|\)，并不保持 \(|\nabla_g^2a|\)。事实上
\[
\partial_t\Gamma=g^{-1}*\nabla(aE)
\]
又引入 \(a\nabla E\)。

因此 Step 17 Proposition 1 中“初始曲率因度量小漂移而基本保持”的环节不成立。若已有
\[
\|a\Rm(t)\|_\infty\le C/t,
\]
直接放入 (3) 还会产生 \(t=0\) 处的对数；以初始 \(K_0\) 截断后，因子通常含 \(\log(K_0r^2)\)，对变化拓扑的序列并不统一。

## 2. 假设独立的 \(\|E\|_\infty\) 估计后，耦合 \(L^2\) 系统可以闭合

设暂时外加以下两件事：

1. 光滑解已存在于 \([0,T]\)；
2. \(\|E(t)\|_\infty\le C\delta\) 在该时间段统一成立。

那么
\[
|\partial_tg|_g\le C\delta
\]
立刻给出
\[
e^{-C\delta t}g_0\le g(t)\le e^{C\delta t}g_0.
\tag{4}
\]
固定的覆盖、体积比、有限邻接数以及相对 Sobolev 不等式因此保持到可控常数。

在半径 \(r\) 的固定覆盖上，相对 Sobolev 形式是
\[
\|f\|_4^2
\le
S_\alpha
\left(\|\nabla f\|_2^2+r^{-2}\|f\|_2^2\right),
\qquad
S_\alpha\asymp \frac{r^2}{V_\alpha^{1/2}}.
\tag{5}
\]
塌缩时 \(S_\alpha\) 本身通常并不有界；真正保持统一的是
\[
S_\alpha\|\Rm\|_{L^2(U_\alpha)}
\le
C\left(
\frac{r^4}{V_\alpha}
\int_{U_\alpha}|\Rm|^2
\right)^{1/2}
=C\,R_{U_\alpha}^{1/2}.
\tag{6}
\]

若相邻局部能量满足 \(R_\beta\le\varepsilon_*\)，则危险项分别满足

\[
\begin{aligned}
\int \eta_\alpha^2a|\Rm||E|^2
&\le
\|\Rm\|_{2,U_\alpha}
\|\eta_\alpha\sqrt a\,E\|_4^2\\
&\le
C\sqrt{\varepsilon_*}
\left(
Y_\alpha+r^{-2}\sum_{\beta\sim\alpha}P_\beta
\right),
\end{aligned}
\tag{7}
\]

以及

\[
\int \eta_\alpha^2a|\Rm|^3
\le
C\sqrt{\varepsilon_*}
\left(
X_\alpha+r^{-2}\sum_{\beta\sim\alpha}R_\beta
\right).
\tag{8}
\]

过渡项利用
\[
|\nabla a|\le Cr^{-1}\sqrt a
\]
给出
\[
\int |\nabla a|\,|\nabla E|\,|\Rm|
\le
\epsilon Y_\alpha
+C_\epsilon r^{-2}\sum_{\beta\sim\alpha}R_\beta.
\tag{9}
\]

\(\nabla_g^2a*E*\Rm\) 不必用 pointwise Hessian 估计。积分分部后，
\[
\int\eta^2\nabla^2a*E*\Rm
=
-\int\nabla a*\nabla(\eta^2E*\Rm),
\]
由此产生 \(\nabla a*\nabla E*\Rm\)、\(\nabla a*E*\nabla\Rm\) 和 \(d\eta\) 项，最终可估为
\[
\epsilon(X_\alpha+Y_\alpha)
+C_\epsilon r^{-2}
\sum_{\beta\sim\alpha}(R_\beta+P_\beta).
\tag{10}
\]

取 \(\varepsilon_*\) 足够小后，式 (7)、(8) 的主梯度项被耗散吸收，得到
\[
\begin{aligned}
\dot R_\alpha+cX_\alpha
&\le
Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta)
+\epsilon_1Y_\alpha,\\
\dot P_\alpha+cY_\alpha
&\le
Cr^{-2}\sum_{\beta\sim\alpha}P_\beta.
\end{aligned}
\tag{11}
\]
令 \(H_\alpha=R_\alpha+\kappa P_\alpha\)，选择固定 \(\kappa\) 吸收 \(\epsilon_1Y_\alpha\)，则
\[
\dot H_\alpha+c'(X_\alpha+Y_\alpha)
\le
Cr^{-2}\sum_{\beta\sim\alpha}H_\beta.
\tag{12}
\]
若覆盖邻接数为 \(N\)，
\[
H_*(t):=\sup_\alpha H_\alpha(t)
\le
e^{CNt/r^2}H_*(0).
\tag{13}
\]
因此在 \(t\le\theta r^2\)、\(\theta\) 足够小时，
\[
\sup_\alpha R_\alpha(t)\le 2\varepsilon_*
\]
可由首次达到 \(2\varepsilon_*\) 的时刻反证闭合。初始
\[
P_\alpha(0)\le \delta^2r^4
\]
在 \(\delta\to0\) 时不会扰动曲率阈值。

所以，**耦合能量层面确实可以自洽闭合**。最大值估计若外加成立，还会直接给出全局
\[
Q(t)\le C\delta^2\Vol(g(t)),
\]
甚至不必借助全局 \(P\)-能量来完成终端拓扑校准；不过 \(Y_\alpha\) 仍对吸收式 (9) 至关重要。

## 3. 对 A01 (a)–(e) 的逐项含义

在“统一光滑存在时间 + 独立 \(\|E\|_\infty\) 估计”这一外加前提下：

- **(a) metric comparability：成立。** 直接来自式 (4)。
- **(b) relative Sobolev preservation：成立。** 双 Lipschitz 等价保持固定覆盖上的 Sobolev、体积与有限重数。
- **(d) weighted defect：成立且更强。** 因 \(a\le1\)，
  \[
  \|aE(t)\|_\infty\le C\delta
  \le
  C_p\delta(r^2/t)^{2/p},
  \qquad t\le\theta r^2,\ p>2.
  \]
- **(e) local critical curvature energy：耦合能量论证可给出。** 式 (11)–(13) 是所需核心。
- **(c) weighted pointwise curvature：不能由这些能量不等式直接得到。**

从
\[
R_\alpha(t)\le 2\varepsilon_*,\qquad
\int_0^T(X_\alpha+Y_\alpha)\,dt<\infty
\]
到
\[
\sup_{\Omega}a|\Rm(t)|\le C/t
\tag{14}
\]
需要 parabolic \(\varepsilon\)-regularity 或加权 Moser 迭代。四维 \(W^{1,2}\to L^4\) 只给有限指数控制，并不直接给 \(L^\infty\)。此外，\(a\) 在零集附近退化，标准统一抛物估计不能原样使用；\(\nabla E\) 与 evolving Hessian of \(a\) 又进入曲率方程。

在平台的更小内球上，\(a=1\)，且所有 Li covering balls 都位于平台内部时，标准 Li 局部迭代可产生
\[
|\Rm|\le C/t
\]
及 Shi 型导数估计。这里不需要过渡环带的 pointwise 曲率。可是要使整个 cutoff flow 到达固定终端时间，仍需控制过渡环带中的高阶几何；\(C^0\) 度量等价和临界 \(L^2\) 能量本身并不是经典解的延拓估计。

## 4. 真正需要的分析定理

实际路线需要联合证明，而不是预先假设，
\[
\begin{gathered}
\sup_\alpha R_\alpha(t)\le C\varepsilon_*,\\
\|a\Rm(t)\|_\infty\le C/t,\\
\|aE(t)\|_\infty
\le C_p\delta(r^2/t)^{2/p},
\qquad p>2,\\
e^{-C\delta r^2}g_0\le g(t)\le e^{C\delta r^2}g_0,
\end{gathered}
\tag{15}
\]
并由此延拓至 \(t=\theta r^2\)。其中 \(p>2\) 给出
\[
\int_0^{\theta r^2}t^{-2/p}\,dt<\infty,
\]
这才是真正适合闭合度量漂移的估计。它不能由式 (3) 的 pointwise Gronwall 自动产生。

最贴近现有材料的定理形状是：

1. 先以式 (11)–(13)保持局部临界能量；
2. 对 \(a\Rm\) 建立退化系数下的加权 Moser 估计；
3. 把 \(\Rm\) 作为临界 \(L^2\) 势，对缺陷方程建立 \(L^p\to L^\infty\) 平滑；
4. 用可积的 \(aE\) 估计改善 metric comparability；
5. 由 weighted curvature 与局部高阶估计延拓光滑解。

相关资料搜索主题应精确聚焦于：

- local Ricci flow 的 \(\chi^2\Rm\) weighted estimates；
- relative Sobolev balls 上的 critical \(L^{n/2}\) curvature smoothing；
- quadratically vanishing coefficient 的 Ricci–DeTurck flow；
- small \(L^{n/2}\) potential 的 endpoint parabolic regularity；
- Wang–Yang local Ricci flow 延拓机制中 cutoff Hessian 与 weighted curvature 的耦合。

因此，Sobolev–能量消去已经足以处理**积分层面的过渡耦合**，但不能取代**加权 pointwise 正则性与统一时间延拓**。而当前所用的缺陷 maximum principle 又依赖后者中的 \(a\Rm\) 控制，所以实际所需的桥梁仍然存在，只是其核心已可缩小为式 (15) 所示的加权抛物定理。
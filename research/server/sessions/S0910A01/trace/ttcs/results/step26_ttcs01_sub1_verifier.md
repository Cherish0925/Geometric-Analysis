# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step26_weighted_velocity_and_local_flow.md",
    "Sessions/S0910A01/workspace/scripts/step26_fixed_p_defect_velocity.py",
    "Sessions/S0910A01/workspace/scripts/step26_p6_defect_energy_ledger.py",
    "Sessions/S0910A01/workspace/notes/step25_first_exit_formulation.md",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Sessions/S0910A03/workspace/notes/step24_corrected_evolution_and_conditional_gap.md"
  ]
}
```

## Task

Verify the Step 26 correction to the buffered selected-support cutoff-flow route for Yau Problem 26. Focus on: (1) whether the Step 25 plateau-only metric-displacement argument is indeed insufficient and whether support-wide integral control of ||aE||_infty is the right metric-comparability target; (2) whether the fixed-p defect energy J_p=int eta^2 a^(p-2)|E|^p, especially p=6, has the claimed weights, Hessian/cutoff remainders, curvature potential F z_p^2, and initial bound from pointwise Ricci pinching without curvature high integrability; (3) whether the proposed p=6 positive-time weighted velocity estimate ||aE||_infty <= C delta (r^2/t)^(1/3) is a plausible next Moser target or hides a Hardy/degenerate-parabolic obstruction; (4) whether the reading of Yang local Ricci flow source correctly handles DeTurck transported coefficient and shows that short-time existence is only a starting point while uniform continuation to theta r^2 requires weighted curvature/velocity estimates; (5) identify any exact missing hypotheses or wrong weights. Do not decide the overall Yau problem; give a scientific verification memo for the analytic route.

## Output

# 科学核验备忘：Step 26 加权速度与局部 Ricci 流

## 总结

Step 26 对 Step 25 的修正确实必要。平台区上的曲率或缺陷估计不能控制过渡带中的度量变化；当前支撑上真正相关的量是

\[
V(t)=\int_0^t\|aE(s)\|_{L^\infty(\operatorname{supp}\chi,g(s))}\,ds,
\qquad a=\chi^2 .
\]

固定 \(p\) 的缺陷能量

\[
J_p=\int \eta^2a^{p-2}|E|^p
\]

具有正确的主耗散权重、过渡带余项和曲率势。特别是 \(p=6\) 与 Yang 附录 A 的加权 Moser 幂次精确匹配：在四维中，起始权重正是

\[
\chi^{2p_0-n}=\chi^8=a^4.
\]

因此

\[
\|aE(t)\|_\infty\lesssim
\delta(r^2/t)^{1/3}
\]

不只是量纲上的猜测；它与 Yang 的 \(p_0=q=6\) 迭代结构一致。尚缺的是把 Einstein 缺陷张量方程逐项嵌入该张量型加权迭代，并同时使用正时间的加权 \(L^3\) 曲率估计。

---

## 1. 整个活动支撑上的 \(aE\) 控制确实是正确目标

对固定切向量 \(v\neq0\)，

\[
\frac d{dt}\log g_t(v,v)
=-2a\,\frac{E_t(v,v)}{g_t(v,v)} ,
\]

故

\[
\left|\frac d{dt}\log g_t(v,v)\right|
\le 2|aE|_{\mathrm{op}}
\le 2|aE|.
\]

积分即得

\[
e^{-2V(t)}g_0\le g(t)\le e^{2V(t)}g_0.
\]

这个推导逐点成立，因而要传递整个选定支撑上的 Sobolev 常数、体积元和 \(|d\chi|_{g(t)}\)，就需要在整个 \(\operatorname{supp}\chi\) 上控制 \(aE\)。在 \(\{a=0\}\) 上度量不动，所以活动支撑以外无需额外估计。

平台信息不能推出过渡带信息。仅从代数上看，过渡带允许出现

\[
a(x)=\varepsilon,\qquad |E(x,t)|\simeq \varepsilon^{-1},
\]

此时 \(a|E|\simeq1\)，即使平台上的 \(E\) 很小也无影响。光滑性本身不会给出平台与过渡带之间的定量联系。因而 Step 25 中“\(a<1\) 自动减小位移”的推理不成立，Step 26 的替换是正确的。

---

## 2. \(J_p\) 的权重计算

采用已给出的精确缺陷方程

\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E).
\]

令

\[
J_p=\int\eta^2a^{p-2}|E|^p,\qquad
Z_p=\int\eta^2a^{p-1}|E|^{p-2}|\nabla E|^2.
\]

### 2.1 主项与过渡带余项

扩散系数 \(a\) 与测试权重 \(a^{p-2}\) 相乘，给出耗散权重 \(a^{p-1}\)。主项分部积分、\((da)*\nabla E\) 项以及 Hessian-\(a\) 项分部积分后，典型交叉项均为

\[
a^{p-2}|da|\,|E|^{p-1}|\nabla E|.
\]

Young 不等式给出

\[
\begin{aligned}
&a^{p-2}|da|\,|E|^{p-1}|\nabla E|\\
&\quad\le
\varepsilon a^{p-1}|E|^{p-2}|\nabla E|^2
+C_\varepsilon a^{p-3}|da|^2|E|^p.
\end{aligned}
\]

由于 \(a=\chi^2\)，

\[
|da|^2=4a|d\chi|^2,
\]

所以

\[
a^{p-3}|da|^2|E|^p
=4|d\chi|^2a^{p-2}|E|^p
\le Cr^{-2}a^{p-2}|E|^p.
\]

这验证了 Step 26 的关键权重。它没有留下 \(a^{-1}\) 型奇异势。

\(\operatorname{supp}d\eta\subset\{a=0\}^{\circ}\) 使所有含 \(d\eta\) 的扩散项及 Hessian 分部积分项消失；这里需要该驻定领圈假设，而不仅是 \(\eta=1\) 于平台。

### 2.2 曲率势

Lichnerowicz 反应、逆度量变化和体积元变化均可估为

\[
C_pa^{p-1}F|E|^p,
\qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

定义

\[
z_p=\eta a^{(p-1)/2}|E|^{p/2},
\]

则恰有

\[
\eta^2a^{p-1}F|E|^p=Fz_p^2.
\]

而且

\[
\|\nabla z_p\|_2^2
\le C_pZ_p+C_pr^{-2}J_p,
\]

因为 \(a\)-导数项仍化为
\(4|d\chi|^2a^{p-2}|E|^p\)，且

\[
\|z_p\|_2^2
=\int\eta^2a^{p-1}|E|^p\le J_p.
\]

因此当前度量下的 Sobolev 不等式给出

\[
\int Fz_p^2
\le C_p\beta_a(t)(Z_p+r^{-2}J_p),
\qquad
\beta_a=A(t)^2\|F\|_{L^2(\operatorname{supp}\chi)}.
\]

在 \(C_p\beta_a<c_p/2\) 时，得到

\[
J_p'+c_p'Z_p\le C_pr^{-2}J_p.
\]

这些权重与 `step26_fixed_p_defect_velocity.py` 和
`step26_p6_defect_energy_ledger.py` 一致；两个脚本只验证单项式和尺度，不验证张量收缩、移动体积元及 Young 常数。

### 2.3 初值

所需的精确初始假设是

\[
\|E(0)\|_{L^\infty}
=\|\operatorname{Ric}_{g_0}+g_0\|_{L^\infty}
\le C\delta.
\]

由此

\[
J_p(0)\le C\delta^p\operatorname{Vol}(\operatorname{supp}\chi,g_0),
\]

无需任何初始 \(L^p\) Riemann 曲率估计。这里“Ricci 夹逼”必须具体给出上述近 \(-g_0\) 的估计；一般的
\(c_4g\le\operatorname{Ric}\le C_4g\) 本身不产生小参数 \(\delta\)。

缺陷能量虽不使用高次 Riemann 曲率初值，其势项吸收仍依赖当前的临界 \(L^2\) 曲率控制。

### 2.4 \(p=6\) 的正则性细节

\[
J_6=\int\eta^2\chi^8|E|^6
\]

是光滑多项式型能量。脚本中“\(z_6=\chi^5|E|^3\) 光滑”的表述不精确：\(|E|^3\) 在 \(E=0\) 处并非 \(C^\infty\)。它属于所需的 \(W^{1,2}\) 类，且

\[
|\nabla |E|^3|\le3|E|^2|\nabla E|.
\]

严格推导可使用 \((|E|^2+\varepsilon)^{3/2}\) 后令
\(\varepsilon\downarrow0\)。Moser 中出现的非整数幂也需要类似正则化，或者选取仅在外缘平坦消失的标准光滑 cutoff。

---

## 3. \(p=6\) 加权 Moser 目标与 Yang 附录的精确匹配

令 Sobolev 系数记为 \(S=A^2\)：

\[
\|u\|_4^2\le
S\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr).
\]

Yang 附录 A.1 的起始参数在这里可取

\[
n=4,\qquad p_0=6,\qquad q=6.
\]

其起始空间权重为

\[
\chi^{\,2p_0-n}=\chi^8=a^4,
\]

正好是 \(J_6\) 的权重；输出量则是 \(\chi^2f=a f\)。

此外，Yang 对势 \(u\) 的条件是

\[
\left(\int\chi^{q-n}u^{q/2}\right)^{2/q}
\le\mu t^{-(q-n)/q}.
\]

取 \(u=CF\) 后变成

\[
\left(\int\chi^2F^3\right)^{1/3}
\le\mu t^{-1/3}.
\]

若曲率能量已经给出

\[
S^2Y(t)=S^2\int\chi^2F^3
\le \frac{C\beta^3}{t},
\]

则可取

\[
\mu=C\beta S^{-2/3},
\qquad \mu S^{2/3}=C\beta.
\]

因此 Yang 的幂次结构给出

\[
\|aE(t)\|_\infty
\lesssim
S^{1/3}
\bigl[r^{-2}+t^{-1}(1+\beta^3)\bigr]^{1/2}
\left(\int_0^tJ_6(s)\,ds\right)^{1/6}.
\]

利用 \(t\le r^2\) 和 \(J_6(s)\le C\delta^6V\)，

\[
\|aE(t)\|_\infty
\le C\delta S^{1/3}V^{1/6}t^{-1/3}.
\]

若同一支撑体积 \(V\) 满足选定的相对 Sobolev估计

\[
S\le Cr^2V^{-1/2},
\]

便得到

\[
\boxed{
\|aE(t)\|_\infty
\le C\delta r^{2/3}t^{-1/3}
=C\delta(r^2/t)^{1/3}.}
\]

所以体积消去和时间指数均正确。

这里没有显现 Hardy 型奇异项：每次 cutoff 导数产生的是

\[
a^{q-3}|da|^2=4a^{q-2}|d\chi|^2,
\]

与当前 \(J_q\) 权重相同。真正需要补足的是以下两点：

1. \(E\) 方程中的 \((da)*\nabla E\) 是张量收缩，不能仅靠
   \(|\nabla|E||\le|\nabla E|\) 全部改写为标量漂移项；需要 Yang 所述的张量型 Moser 版本，或直接对每个迭代指数建立加权能量式。
2. 有限多个 \(L^q\) 空间估计本身不能推出 \(L^\infty\)。需要指数趋于无穷的 Moser 过程，或一个已经封装该过程的加权均值定理。

因此该估计是有明确文献模板的下一段分析，而非仅由脚本得到。

---

## 4. Yang/Wang 文献读取

### 4.1 固定空间系数

Yang 第 8 节令

\[
\hat a=(\chi\circ\varphi_t^{-1})^2
\]

出现在 DeTurck 方程中，并最终取

\[
g(t)=\varphi_t^*\hat g(t).
\]

于是

\[
\varphi_t^*\hat a=\chi^2,
\]

拉回后确实恢复固定的原始 cutoff，而不是随时间搬运的另一条流。Step 26 对这一点的读取正确。

归一化项可在 hatted 方程中写成

\[
-2\hat a\,\hat g.
\]

拉回后正是 \(-2\chi^2g\)。它不改变主符号，但会进入体积元、反应项和高阶延拓估计，因而仍需逐项写入。

### 4.2 短时间存在与一致时间

Yang Theorem 8.2 只给每个光滑初值某个正的存在时间；其长度可以依赖初始高阶几何。它不能单独产生统一的 \(\theta r^2\)。

Yang Theorem 9.2 已给出了相应的一致时间原型：小的临界 Riemann 曲率、Sobolev 常数及 \(L^p\) Ricci 控制共同产生

\[
|\chi^2\operatorname{Rm}|\lesssim t^{-1},
\qquad
|\chi^2\operatorname{Ric}|\lesssim t^{-n/(2p)}.
\]

当前初值满足 \(\operatorname{Ric}=-g+E\)，故具有任意有限 \(p\) 的初始 Ricci 控制。直接使用该估计可给出可积的加权 Ricci 速度；但其系数一般为 \(O(1)\)，不带 \(\delta\)。缺陷方程的齐次结构才产生 Step 26 所需的 \(\delta\) 因子。

Wang Theorem 4.1 明确说明：若终止时刻以前

\[
\|\chi^2\operatorname{Rm}\|_\infty
\]

一致有界，则局部 Ricci 流可光滑延拓。估计 \(C/t\) 在任意正的终止时刻都是有限的。归一化项的相应版本还需把 \(-2\chi^2g\) 加入高阶归纳，但它是零阶项。

要区分两种作用：

- 加权曲率控制服务于光滑延拓；
- 加权速度积分服务于度量、Sobolev 常数和 cutoff 梯度的传递。

二者在当前第一退出论证中相互依赖，但在 Wang 的延拓定理里，直接假设的是加权曲率。

---

## 5. 尚需明确写入的数学内容

1. 当前度量下的
   \(|d\chi|\le Cr^{-1}\)、相对 Sobolev 不等式及其系数 \(S(t)\)。
2. 初始条件必须明确为
   \(\|\operatorname{Ric}+g\|_\infty\le C\delta\)。
3. \(C_6\beta_a<c_6/2\) 来自选定良好支撑的临界曲率小量；“缩小 \(r\)”一句本身不足以排除曲率集中点。
4. Moser 中使用的体积 \(V\) 必须与
   \(S\le Cr^2V^{-1/2}\) 中的支撑体积相同，或已有统一体积比。
5. \(Y(s)\lesssim s^{-1}\) 需要对整个 \(0<s\le t\) 成立，而不只是终端切片。
6. 平台上的 \(|\operatorname{Rm}|\lesssim t^{-1}\) 需要前一时间段（例如 \([t/2,t]\)）上的空间 \(L^3\) 控制和嵌套平台球；单个时刻的 \(L^3\) 值不直接给出点值。
7. `step26_*ledger.py` 中验证的是幂次与缩放；完整 PDE 证明仍需包含移动范数、移动体积元、张量 Hessian-\(a\) 收缩以及非整数幂正则化。

总体而言，Step 26 修正了 Step 25 的核心度量传播问题；\(J_6\) 权重正确，并与 Yang 的四维 \(p_0=q=6\) 加权 Moser 结构高度吻合。当前最集中的数学缺口是该张量型 Moser 实例化及归一化 Yang/Wang 延拓论证。
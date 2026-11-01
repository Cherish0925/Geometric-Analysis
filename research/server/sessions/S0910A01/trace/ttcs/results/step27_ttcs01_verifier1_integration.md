# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 27,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step27_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step27_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the normalized cutoff-flow continuation theorem and the full conditional gap chain for the four-dimensional negative Yau-26 laboratory. The claim is that the three theorems in the continuation note (short-time existence, extension under weighted curvature, uniform time via first-exit bootstrap) close the last analytic obstacle, and that the full chain from initial Ricci pinching to the Derdziński forbidden germ is logically complete (conditional on the general-p inequality and Maheux-Saloff-Coste Sobolev).

Specific points to check:
1. In Theorem 1.1 (short-time existence via ε-regularization): Does the lower-order -2χ²g term genuinely not affect the parabolic existence? The ε-independent energy bound (1.3) gains O(Vol) terms from normalization—is this absorbed by Gronwall for short time?
2. In Theorem 2.1 (extension): Wang's induction uses ∇^m(χ²Rm). The normalization adds ∇^m(χ²g) terms. Since g itself evolves, ∇^m g involves m-th derivatives of Christoffel symbols, hence ∇^{m-1}Rm. Does the induction order remain correct (i.e., does controlling ∇^{m-1}(χ²Rm) suffice to control ∇^m(χ²g))?
3. In Theorem 3.1 (uniform time): The first-exit argument uses the weighted curvature bound ||aRm|| ≤ Cβ/t, which diverges at t=0. But Theorem 2.1 requires bounded |χ²Rm| on [0,T). Is the argument correct that short-time existence gives [0,T₁), and then for any t₀ ∈ (0,T₁), |aRm(t₀)| < ∞ by the Moser bound, so extension applies from t₀ onward?
4. Does the three-factor Moser iteration (unified note) correctly supply both ||aF|| ≤ Cβ/t and ||aE|| ≤ Cδ(r²/t)^{1/3} with the stated volume cancellations? The key algebraic identity is the three-factor Hölder decomposition a^{p-1}Ff^p = (aF³)^{1/3}(a^{p-2}f^p)^{1/3}z_p^{4/3}.
5. Is there any logical gap between the positive-time bounded curvature on plateaux and the Derdziński contradiction? Specifically: the calibrated Weyl spectrum from Steps 5-8 was derived for the initial metric; after flowing, do the nonnegative deficit densities transfer to the terminal metric under metric comparability and Q/A → 0?

## Integrated Scientific Memo

# 核验结论

当前材料**不能证明**“三条 continuation 定理已经闭合最后解析障碍”，也不能证明从初始 Ricci 夹逼到 Derdziński forbidden germ 的完整条件链已经逻辑闭合。准确结论是：

- 归一化项 \(-2\chi^2g\)确实不改变主抛物结构，且其能量中的 \(O(\mathrm{Vol})\) 项可由短时间 Gronwall 吸收；
- 但 Theorem 1.1 所写的 \(\varepsilon\)-正则化极限论证无效；
- Theorem 2.1 的结论在结构上可信，但所写高阶归纳遗漏了演化 cutoff 的高阶协变导数，尚不是证明；
- \(C\beta/t\) 在 \(t=0\) 发散不妨碍 first-exit continuation，只需显式拼接初始光滑区间；
- 三因子 Hölder 恒等式及两个体积消去正确；Moser 输出仍依赖尚未完全核验的 general-\(p\) 能量不等式，并且统一笔记中有一个迭代指数记账错误；
- 初始 Weyl deficit 不能靠 \(C^0\) 度量比较传到终端度量；必须对终端度量重新使用拓扑/SW 不等式。更严重的是，从可能坍缩的有界曲率 plateaux 提取四维光滑 Einstein germ 的非坍缩或局部覆盖论证未给出。

下面逐点给出可保留的结论及精确缺口。

---

## 1. 短时存在：归一化项无害，但所写 \(\varepsilon\)-极限不成立

令 \(a=\chi^2\)。在 DeTurck 规范下，

\[
D_g(-2ag)[h]=-2ah
\]

是零阶项，因此不改变主符号。对每个固定 \(\varepsilon>0\)，正则化方程

\[
\partial_tg_\varepsilon=-2(\varepsilon^2+a)(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon)
\]

仍是严格抛物的。运输 \(a\circ\varphi^{-1}\) 并回拉后也确实恢复固定空间 cutoff \(a\)。所以归一化本身不构成短时存在障碍。

归一化导致的能量源项也可处理。若

\[
\mathcal E_\varepsilon'
 \le C\mathcal E_\varepsilon+C\,\operatorname{Vol}_{g_\varepsilon(t)}(M),
\]

且在预备短区间内体积受控，则

\[
\mathcal E_\varepsilon(t)
 \le e^{Ct}\left(\mathcal E_\varepsilon(0)
 +C\int_0^t e^{-Cs}\operatorname{Vol}_{g_\varepsilon(s)}(M)\,ds\right).
\]

故 \(O(\mathrm{Vol})\) 项确实可由 Gronwall 吸收。这回答了问题 1 中关于归一化项的局部疑问。

但 continuation note 随后的推论不成立：

\[
\sup_t\int |\operatorname{Rm}_{g_\varepsilon}|^{n/2}<\infty
\quad\not\Longrightarrow\quad
\sup_t\|g_\varepsilon\|_{C^k}<\infty .
\]

尤其在四维，\(L^2\)-曲率是临界量，不能直接给出点态曲率或 \(C^k\) 控制。并且正则化系统的椭圆常数下界是 \(\varepsilon^2\)，普通抛物估计常数可在 \(\varepsilon\to0\) 时退化。因此材料没有证明：

\[
T_\varepsilon\ge T_0>0\ \text{一致于 }\varepsilon,
\qquad
\|g_\varepsilon\|_{C^k([0,T_0])}\le C_k.
\]

Arzelà–Ascoli 极限和“标准抛物唯一性”也随之没有依据。

**可行修复**是直接采用 Yang 的退化 cutoff-flow 短时存在/Nash–Moser 构造，并验证加入的映射 \(g\mapsto-2ag\) 是 tame 的零阶扰动。这个结论很可能正确，但 supplied note 尚未写成完整适配证明。因此 Theorem 1.1 的命题可恢复，现有证明不可接受。

---

## 2. Extension：\(\nabla g=0\) 消除了题设担忧，但笔记仍漏掉 cutoff 高阶导数

对当前 Levi-Civita 联络恒有

\[
\nabla g=0,
\qquad
\nabla^m(ag)=(\nabla^m a)\otimes g.
\]

因此不能把 \(\nabla^m g\) 当作坐标偏导，并声称其中出现 Christoffel 的 \(m\) 阶导数。题设中的这一具体担忧由 metric compatibility 完全消除：控制 \(\nabla^m(ag)\) 并不直接要求控制 \(\nabla^{m-1}\operatorname{Rm}\)。

然而 continuation note 的替代理由“\(\nabla^i\chi\) time-independent，且由 metric equivalence 控制”是错误的。函数 \(\chi\) 固定，但当 \(i\ge2\) 时，\(\nabla^i\chi\) 依赖演化联络。归一化曲率变化包含

\[
a*\operatorname{Rm}+(\nabla^2a)*g.
\]

施加 \(\nabla^m\) 后会产生

\[
\sum_{i+j=m}\nabla^ia*\nabla^j\operatorname{Rm},
\qquad
(\nabla^{m+2}a)*g,
\]

而 note 所列归一化项只到 \(\nabla^m a\)，遗漏了 \(\nabla^{m+2}a\)。

同时

\[
\partial_t\Gamma=g^{-1}*\nabla(aE)
\]

导致

\[
\partial_t(\nabla^q a)
 =\sum \nabla^r(\partial_t\Gamma)*\nabla^{q-r-1}a.
\]

最高曲率导数阶数是三角型的：控制 \(\nabla^q a\) 通常只牵涉低一阶的 weighted curvature derivatives。因此 Wang 式联合归纳很可能仍闭合；原 local-flow 归纳本来也必须处理 coefficient \(a\) 的高阶演化协变导数。正确层级应同时估计，例如

\[
\{\nabla^j(a\operatorname{Rm})\}_{j\le m},
\qquad
\{\nabla^q a\}_{q\le m+2},
\]

并逐项验证时间交换子和空间交换子的阶数。

以下 \(C^0\) 部分是正确的：

\[
|\partial_tg|
 =2a|\operatorname{Ric}+g|
 \le C(|a\operatorname{Rm}|+a)
 \le C(K+1),
\]

故有限时间内度量一致等价。但 metric equivalence 单独不能控制 \(\nabla^qa\), \(q\ge2\)。

所以对问题 2 的精确回答是：

- 不存在“\(\nabla^mg\) 导致同阶失控”；
- 归纳阶数在正确的联合层级中应保持三角性；
- 但 Theorem 2.1 当前文字遗漏 \(\nabla^{m+2}a\) 及 cutoff-derivative evolution，尚未构成完整 extension 证明。

---

## 3. \(C\beta/t\) 在零时刻的发散：first-exit 逻辑可严格修复

设可能的终端 first-exit time 为 \(T_*>0\)，取

\[
0<t_0<\min\{T_1,T_*\}.
\]

初始短时光滑性给出

\[
K_0=\sup_{0\le t\le t_0}
 \|a\operatorname{Rm}(t)\|_\infty<\infty .
\]

而 Moser 估计在正时间给出

\[
\sup_{t_0\le t<T_*}
 \|a\operatorname{Rm}(t)\|_\infty
 \le \frac{C\beta}{t_0}.
\]

故

\[
\sup_{0\le t<T_*}\|a\operatorname{Rm}(t)\|_\infty
\le
\max\left\{K_0,\frac{C\beta}{t_0}\right\}<\infty .
\]

这才是将 extension theorem 用在终端时间 \(T_*\) 所需的估计。仅说“对每个 \(t<T_*\) 都能向后延拓一点”不自动排除在 \(T_*\) 处崩溃；必须写出上述直至 \(T_*\) 的统一界。

因此问题 3 的机制是正确的，但 Theorem 3.1 应以这段拼接估计替换当前第 6 项的表述，并且它仍以完整证明 Theorem 1.1、2.1 为前提。

---

## 4. 三因子 Moser：核心代数和体积消去正确，迭代记账需修正

令

\[
H_p=\int a^{p-2}f^p,\qquad
Y=\int aF^3,\qquad
z_p=a^{(p-1)/2}f^{p/2}.
\]

恒等式

\[
a^{p-1}Ff^p
=(aF^3)^{1/3}(a^{p-2}f^p)^{1/3}z_p^{4/3}
\]

完全正确，因为 \(a\) 的指数为

\[
\frac13+\frac{p-2}{3}+\frac{2(p-1)}3=p-1.
\]

Hölder \((3,3,3)\) 给出

\[
R_p
\le Y^{1/3}H_p^{1/3}\|z_p\|_4^{4/3}.
\]

再结合

\[
\|z_p\|_4^2
\le C_pS(D_p+r^{-2}H_p)
\]

和 Young 不等式，可得

\[
C_pR_p
\le \varepsilon D_p+
Cp^N\bigl(r^{-2}+S^2Y\bigr)H_p
\]

对某固定有限 \(N\)。只要 \(p\)-依赖是多项式，Moser 乘积可收敛。

在时间片 \(s\in[t/2,t]\) 上应使用点态系数界

\[
S^2Y(s)\le \frac{C\beta^3}{s}
\le \frac{2C\beta^3}{t}.
\]

这比只记录 \(\int_{t/2}^tS^2Y\) 更安全；若对带 \(p^N\) 的系数直接使用 Gronwall，可能产生不利的 \(e^{Cp^N}\)。

两个终端消去均正确：

### 曲率，\(p_0=3\)

\[
\int_{t/2}^tH_3(s)\,ds
\le C\frac{\beta^3}{S^2},
\]

故

\[
\|aF(t)\|_\infty
\le CS^{2/3}t^{-1}
\left(\frac{\beta^3}{S^2}\right)^{1/3}
=\frac{C\beta}{t}.
\]

### 缺陷，\(p_0=6\)

若 \(V=\operatorname{Vol}(\Omega)\) 且

\[
\int_{t/2}^tJ_6(s)\,ds\le C\delta^6Vt,
\]

则

\[
\begin{aligned}
\|aE(t)\|_\infty
&\le CS^{1/3}t^{-1/2}(\delta^6Vt)^{1/6}\\
&=C\delta\,S^{1/3}V^{1/6}t^{-1/3}\\
&=C\delta\,r^{2/3}t^{-1/3}
=C\delta\left(\frac{r^2}{t}\right)^{1/3},
\end{aligned}
\]

因为 \(S\asymp r^2V^{-1/2}\)。于是

\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le \frac32C\delta\theta^{2/3}r^2.
\]

### 需要改正的 Moser 指数

若 \(p_k=p_0\kappa^k\), \(\kappa=1+2/n\)，则

\[
\sum_{k\ge0}\frac1{p_k}
=\frac{n+2}{2p_0},
\]

不是 unified note 所写的 \(n/(2p_0)\)。最终 Sobolev 幂仍为

\[
\frac1\kappa\sum_k\frac1{p_k}
=\frac{n}{2p_0},
\]

因为每步真正贡献的是 \(S^{1/(\kappa p_k)}\)。所以最终 \(S^{2/3}\) 和 \(S^{1/3}\) 正确，但 §4 的逐步因子和求和公式必须修正。

此外，curvature power-energy inequality 中出现的 \(C_0(p)\operatorname{Vol}\) 源项不能在后续迭代中无声消失。需要证明它实际上满足

\[
\mathrm{source}_p\le Cp^Nr^{-2}H_p
\]

（利用 \(F\ge1\) 及 active-region 支撑），或使用 A03 所声称的 source-free 版本并给出完整推导。

因此问题 4 的结论是：代数恒等式、Young 吸收和体积消去成立；完整 \(L^p\to L^\infty\) 定理仍条件依赖于严格的 general-\(p\) 不等式、源项处理和正确的时间片迭代。

---

## 5. 终端 Weyl 校准不能由 metric comparability 运输

初始度量的 Weyl 特征值或 deficit 密度不由

\[
e^{-\varepsilon}g_0\le g(T)\le e^\varepsilon g_0
\]

传递到 \(g(T)\)。曲率依赖二阶导数，而这里仅有 \(C^0\) 双 Lipschitz 比较。

正确机制是：对终端闭度量 \(g(T)\) **重新应用**拓扑、Seiberg–Witten 和 tensor-gap 不等式。所需结论必须形如

\[
0\le \frac1A\int_M\mathcal D_j(g(T))\,d\mu_{g(T)}
\le C\frac{Q_{\mathrm{global}}(T)}A+o(1),
\]

其中 \(\mathcal D_j\ge0\) 是各个校准 deficit。若此前确已证明

\[
Q_{\mathrm{global}}(T)
\le e^{C\theta}Q_{\mathrm{global}}(0),
\qquad
Q_{\mathrm{global}}(0)/A\to0,
\]

则可推出终端积分 deficit 消失。这一步不依赖 metric comparability，而依赖 Steps 5–8 的不等式确实对任意终端度量成立。相关公式不在本输入内，故无法独立核验。

即使终端积分校准成立，仍有两个缺口：

1. **plateau 占比。** 必须证明所选 \(a=1\) 区域具有序列一致的正归一化体积，或提供另一种从全局 deficit 选出良好 plateau 的定量论证。
2. **坍缩 compactness。** 有界曲率和 Shi 导数界本身不产生统一四维 harmonic radius。若 plateaux 可坍缩，则普通 harmonic-chart compactness 不能直接给出非退化四维 Einstein limit。需要：
   - plateau 上局部非坍缩/注入半径下界；或
   - 在适当局部覆盖、指数图或 equivariant collapsed limit 上建立光滑 germ，并证明 Weyl 校准和 Derdziński 论证仍适用。

另外，从积分 deficit 到开放集上的精确谱结构，还需要借助导数界和相对体积比较，把小平均值升级为较小球上的一致小值；随后确认极限中

\[
E=0,\qquad \delta W^+=0,
\]

且 \(W^+\neq0\) 并具有所需两特征值结构。所给文件没有完成这一步。

---

## 最终核验状态

目前严格可支持的是以下**条件命题**：

> 假设 Yang 型归一化退化短时存在、完整 Wang 型联合 extension 归纳、具有多项式 \(p\)-常数和正确源项处理的 general-\(p\) 能量不等式，以及 Maheux–Saloff-Coste 相对 Sobolev 不等式均成立，则三因子 Moser 方法给出
> \[
> \|aF(t)\|_\infty\le C\beta/t,\qquad
> \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3},
> \]
> 且第二个估计闭合 metric/Sobolev first-exit bootstrap；将正时间曲率界与初始光滑区间拼接后，可将流延拓到统一时间 \(\theta r^2\)。

尚未闭合的精确数学对象是：

1. Yang 退化构造加入 \(-2ag\) 后的完整短时存在与唯一性证明；
2. Wang extension 中 \(\nabla^{m+2}a\) 和演化 cutoff 高阶导数的联合归纳；
3. general-\(p\) 不等式的完整 index-level 推导、源项处理及一致 Moser 常数；
4. 终端度量的 deficit 重校准公式；
5. plateau 正占比，以及坍缩情形下提取四维光滑 Einstein–Derdziński germ 的 compactness/local-cover 论证。

因此，“三条 theorem 已闭合最后解析障碍”及“完整条件 gap chain 已逻辑完备”这两个主张，按现有材料均应判定为**尚未证成**。
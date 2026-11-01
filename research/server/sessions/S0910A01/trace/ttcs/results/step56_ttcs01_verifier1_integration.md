# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 56,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step56_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step56_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the common observation time and terminal compactness theorem in the attached note for the restricted IL cutoff flow ∂_t g = -2χ²(Ric+g) in dimension 4.

Key claims to check:

1. §2.5 Smooth convergence at T*: The argument uses H^7 bounds → Sobolev embedding H^7(M^4) ↪ C^{4,α} → Schauder bootstrap on the DeTurck system to get C^∞ convergence. Is H^7 → C^{4,α} correct for n=4? Does the Schauder bootstrap work for the degenerate equation (the coefficient χ² vanishes)? The note says 'in the DeTurck gauge, the system is strictly parabolic after ε-regularization.' Is this sufficient?

2. §2.6 Restart and uniqueness: The pasting argument uses: both solutions arise as ε→0 limits of the unique strictly parabolic ε-regularized DeTurck system, so they agree on the overlap. Is this logically sound? Does it require the ε-regularized solutions to converge uniformly, or is there a subtlety?

3. §4 Terminal compactness: The note claims that bounded curvature K on pullback balls, Rauch noncollapse v₀, and vanishing defect ∫Φ/A→0 suffice for strong W^{2,q}_loc convergence through harmonic coordinates without sequence-uniform derivative bounds. Is this the correct compactness mechanism? Does the upgrade from C^{1,α} harmonic to W^{2,q} to C^∞ on the Einstein limit work?

4. §5 A-cancellation: The global contradiction uses ∫Φ ≤ 119 Q(T) ≤ C δ² A and Vol(P^in) ≥ c₀ A to get mean(Φ) ≤ Cδ²/c₀. Does the A factor cancel correctly? Is the Liouville averaging from Step 53 §7.2 (unit tangent bundle, geodesic flow invariance) correctly invoked for pullback balls under collapse?

5. §2.7 Separation of roles: Verify that no per-datum constant from §2 leaks into the sequence-uniform estimates in §3-§5. In particular, check that the terminal curvature K in §3.1 comes from the first-exit bootstrap (sequence-uniform Γ and θr²), not from the per-datum H^{s₀} continuation.

## Integrated Scientific Memo

# 核验结论

该 note 的 **终端紧性、\(A\)-消去和常数角色分离基本正确，但需要若干技术改写**；而 **公共观测时间的延拓证明目前不完整**。关键缺口集中在 §2.5–§2.6：\(\varepsilon\)-正则化后的严格抛物性，不能自动给出精确退化流的统一 Schauder 提升或唯一性。

## 1. §2.5：\(H^7\) 嵌入正确；退化 Schauder 论证不足

在闭四维流形上，
\[
H^s\hookrightarrow C^{k,\alpha}
\quad\Longleftrightarrow\quad
s>k+\alpha+\frac n2 .
\]
取 \(s=7,n=4,k=4\)，需要
\[
7>6+\alpha ,
\]
故
\[
H^7(M^4)\hookrightarrow C^{4,\alpha}(M),\qquad 0<\alpha<1.
\]
因此嵌入结论正确，但 note 所写的理由“\(7>n/2+2=4\)”不是推出 \(C^{4,\alpha}\) 的正确阈值；正确阈值是 \(7>n/2+4+\alpha\)。

此外，一致 \(H^7\) 有界本身只给子列紧性，不直接给 \(t\uparrow T_*\) 时整条曲线收敛。可用 current-pair 层级补足：若 \(U_j\) 和固定背景连接差 \(A\) 的估计严格建立到所需阶，则
\[
\sup_{t<T_*}\|\partial_tg(t)\|_{H^7(\bar g)}<\infty,
\]
从而
\[
\|g(t_2)-g(t_1)\|_{H^7}
 \le C_\tau |t_2-t_1|,
\]
得到强 \(H^7\)，继而强 \(C^{4,\alpha}\) 终端极限。这个时间 Cauchy 步骤应显式加入。

但
\[
(\chi^2+\varepsilon)g^{ab}\partial_a\partial_b
\]
只对固定 \(\varepsilon>0\) 一致抛物。其 Schauder 常数一般随 \(\varepsilon\downarrow0\) 发散。因此逐个 \(\varepsilon\) 的
\[
C^{4,\alpha}\to C^{6,\alpha}\to\cdots
\]
不能在没有 \(\varepsilon\)-一致高阶估计时传给精确退化流。

- 在 \(\{\chi\ge c>0\}\) 上可用局部严格抛物正则性；
- 在 \(\operatorname{int}\{\chi=0\}\) 上有 \(\partial_tg=0\)；
- 真正未处理的是 \(\chi\to0\) 的退化界面。

所以“正则化后严格抛物”不足以证明全局 \(C^\infty\) 终端收敛。需要以下任一项：

1. 精确退化系统所有阶的加权 current-pair 估计；
2. 对 \(\varepsilon\) 一致的高阶估计；
3. 一个直接以 \(H^7\) 或 \(C^{4,\alpha}\) 数据为初值、寿命仅依赖相应有限范数的退化系统局部适定性/延拓定理。

Step 55 目前只明确核验了下一层交换，并承认一般阶张量展开仍是示意性的，故不能视作完整有限阶证明。

## 2. §2.6：正则化唯一性不能直接传给精确极限

“两个精确解都是唯一正则化解的 \(\varepsilon\to0\) 极限，因此相等”在逻辑上不充分。

从 \(g(\tau)\) 演化到 \(T_*\) 的正则化终端数据是
\[
S_\varepsilon(T_*-\tau)g(\tau),
\]
而重启正则化流直接以 \(g(T_*)\) 为数据。对固定 \(\varepsilon\)，二者通常并不相同。即使初值差趋于零，也需要 \(\varepsilon\)-一致稳定性，例如
\[
\sup_{0\le s\le s_0}
\|S_\varepsilon(s)u_\varepsilon-S_\varepsilon(s)v_\varepsilon\|_{H^7}
\le C\|u_\varepsilon-v_\varepsilon\|_{H^7},
\]
其中 \(C\) 不依赖 \(\varepsilon\)。note 未提供这种估计。

正确替代是：

- 证明精确退化 DeTurck 系统在相应 \(H^7\) 类中的直接能量唯一性；或
- 证明正则化半群的统一稳定性和统一收敛。

若已取得足够正则的终端极限及从该数据出发的局部解，前后两段可在 \(T_*\) 直接连接；由于两侧都满足
\[
\partial_tg=-2\chi^2(\operatorname{Ric}+g)
\]
并有相同空间二阶终端数据，一阶时间导数也相合。此时不需要虚构一个非平凡“重叠区”。但若要比较两个从同一终端数据出发的延拓，仍需精确系统唯一性。

因此公共观测时间证明截至现有材料尚未闭合。

## 3. §4：终端紧性机制成立，但收敛表述需修正

### 3.1 拉回球与半径

在所有相关径向测地线均留在平台、且
\[
\rho\le \min\{r/2,\rho_0(K),\rho_{\rm buffer}\}
\]
时，Rauch/Jacobi 比较给出指数拉回球
\[
(\mathcal B_\rho(p),(\exp_p)^*g)
\]
的统一体积上下界。底流形上的 \(\exp_p\) 可以折叠或多对一，不影响拉回球非坍缩。

故 Proposition 1.2 中“任意 \(\rho\le r/2\)”过强；还需加入曲率尺度和 buffer 限制。

### 3.2 正确的紧性链条

曲率上界和拉回球非坍缩给出统一 harmonic radius。取子列和 harmonic 坐标后，
\[
g_i\to g_\infty \quad\text{强于 }C^{1,\alpha'}_{\rm loc},
\qquad
g_i\rightharpoonup g_\infty \quad\text{弱于 }W^{2,q}_{\rm loc}.
\]

若所选中心满足
\[
\mathcal A_\rho\Phi(p_i)\to0,
\]
则由 \(\Phi\ge |E_i|^2\) 得
\[
\|E_i\|_{L^2(\mathcal B_\rho)}\to0.
\]
又因曲率统一有界，\(E_i\) 在 \(L^\infty\) 中一致有界，所以插值得
\[
E_i\to0\quad\text{强于 }L^q_{\rm loc}
\]
对每个有限 \(q\) 成立。

在 harmonic 坐标中，
\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=2(g_i)_{jk}-2(E_i)_{jk}
+Q_{jk}(g_i^{-1},\partial g_i).
\]
利用 \(C^{1,\alpha'}\) 强收敛、\(E_i\to0\) 的强 \(L^q\) 收敛及内点椭圆估计，可推出
\[
g_i\to g_\infty\quad\text{强于 }W^{2,q}_{\rm loc}.
\]

因此 note 的核心紧性结论正确，但以下两句应删除或更正：

- 不是“\(E_i\) 的 \(W^{2,q}\) 弱极限”；\(W^{2,q}\) 控制属于 \(g_i\)；
- 不能由 Rellich 直接推出 \(E_i\) 强 \(L^2\) 收敛。该收敛直接来自缺陷积分趋零。

### 3.3 极限光滑，不代表原序列 \(C^\infty\) 收敛

极限弱满足
\[
\operatorname{Ric}_{g_\infty}=-g_\infty.
\]
harmonic-coordinate 椭圆 bootstrap 给出 \(g_\infty\in C^\infty\)。

但现有数据不足以推出
\[
g_i\to g_\infty\quad\text{于 }C^\infty_{\rm loc},
\]
因为没有 \(E_i\) 的统一高阶导数估计。局部矛盾不需要这一结论：强 \(W^{2,q}\) 已足以传递二阶曲率代数密度；也可用弱收敛和平方项的下半连续性得到极限上的校准关系。

谱计算一致：
\[
\left(-\frac16\right)^2
+2\left(\frac1{12}\right)^2=\frac1{24},
\]
而 \(\operatorname{Ric}=-g\) 的四维 Kähler–Einstein germ 有
\[
\operatorname{spec}(W^+)
=\left(-\frac23,\frac13,\frac13\right),
\qquad |W^+|^2=\frac23,
\]
故与校准谱矛盾。这里 \(\mathcal G=0\Rightarrow\) 局部 Kähler 的 Derdziński 输入来自未附上的 Step 45，仍是一个上游依赖。

## 4. §5：\(A\)-消去和坍缩下 Liouville 平均正确

接受上游估计后，
\[
Q(T)\le C Q(0)
\le C\delta^2\operatorname{Vol}(M)
\le C\delta^2 A,
\]
以及
\[
\operatorname{Vol}(P^{\rm in})\ge c_0A
\]
给出
\[
\fint_{P^{\rm in}}\mathcal A_\rho\Phi(p)\,d\mu(p)
\le \frac{C\delta^2 A}{c_0A}
=\frac{C\delta^2}{c_0}.
\]
所以 \(A\) 完全消去。若 \(\delta\) 是 \(g^{-1}E\) 的算子范数，四维中严格写法为
\[
Q(0)\le4\delta^2\operatorname{Vol}(M),
\]
维数因子吸收入 \(C\)。

Liouville 平均在底空间坍缩时仍成立。积分是在单位切丛/切球上完成，测地流保持 Liouville 测度；指数映射多对一只导致按切向量重数计数，不要求 injectivity radius 下界。所需条件是所有长度不超过 \(\rho\) 的相关测地线处于统一曲率控制区，正是 buffer 条件。

传播常数宜写为
\[
Q(T)\le C(\theta,V_*)Q(0)
\]
或保留完整指数；除非预先将固定的 \(V_*\) 吸收到 \(C\)，不应机械写成 \(e^{C\theta}\)。

## 5. §2.7：常数角色分离成立

平台上的终端曲率直接来自第一退出端点：
\[
\|aF_T(T)\|_\infty
\le \frac{C\Gamma}{T},
\qquad T=\theta r^2,\quad a=1,
\]
故
\[
|\operatorname{Rm}(T)|
\le \frac{C\gamma_*}{\theta r^2}+C_4
=:K(\gamma_*,\theta,r).
\]
这里不含 §2 的 \(K_\tau\)、固定背景 Sobolev 常数或高阶 current-pair 常数。

同样，§3–§5 使用的双 Lipschitz 常数、\(Q(T)/A\)、Rauch 非坍缩和 harmonic compactness 常数只依赖第一退出参数及固定 geography 数据。唯一依赖 §2 的是逻辑上的“解确实存在到 \(T\)”，而非数值常数泄漏。

若保留“原序列 \(C^\infty\) 收敛”，则会重新引入未证明的统一高阶需求；改成“原序列强 \(W^{2,q}_{\rm loc}\) 收敛，极限光滑”后，角色分离成立。

## 最终判定

- **Claim 1：部分正确。** \(H^7\hookrightarrow C^{4,\alpha}\) 正确；退化方程的 \(C^\infty\) Schauder bootstrap 未证明。
- **Claim 2：不成立。** 正则化唯一性本身不能推出精确极限唯一性；需要统一稳定性或精确退化系统唯一性。
- **Claim 3：经修正成立。** 有界曲率、拉回非坍缩和缺陷趋零足以得到强 \(W^{2,q}_{\rm loc}\) 与光滑 Einstein 极限，但不足以得到原序列 \(C^\infty\) 收敛。
- **Claim 4：成立。** \(A\) 正确消去；Liouville 平均适用于坍缩情形。
- **Claim 5：成立。** 终端 \(K\) 来自统一第一退出 bootstrap，而不是逐个初值的延拓常数。

因此，§3–§5 可通过上述改写形成严密的终端紧性模块；§2 的公共观测时间仍需要补齐有限阶 current-pair 展开、终端时间 Cauchy 性，以及精确退化流的有限正则局部适定性/唯一性。
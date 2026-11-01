# TTCS Independent Branch Record

```json
{
  "step_id": 56,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md",
    "Sessions/S0910A01/workspace/data/step56_common_time_terminal_verify.json"
  ]
}
```

## Task

Verify the common observation time and terminal compactness theorem in the attached note for the restricted IL cutoff flow ∂_t g = -2χ²(Ric+g) in dimension 4.

Key claims to check:

1. §2.5 Smooth convergence at T*: The argument uses H^7 bounds → Sobolev embedding H^7(M^4) ↪ C^{4,α} → Schauder bootstrap on the DeTurck system to get C^∞ convergence. Is H^7 → C^{4,α} correct for n=4? Does the Schauder bootstrap work for the degenerate equation (the coefficient χ² vanishes)? The note says 'in the DeTurck gauge, the system is strictly parabolic after ε-regularization.' Is this sufficient?

2. §2.6 Restart and uniqueness: The pasting argument uses: both solutions arise as ε→0 limits of the unique strictly parabolic ε-regularized DeTurck system, so they agree on the overlap. Is this logically sound? Does it require the ε-regularized solutions to converge uniformly, or is there a subtlety?

3. §4 Terminal compactness: The note claims that bounded curvature K on pullback balls, Rauch noncollapse v₀, and vanishing defect ∫Φ/A→0 suffice for strong W^{2,q}_loc convergence through harmonic coordinates without sequence-uniform derivative bounds. Is this the correct compactness mechanism? Does the upgrade from C^{1,α} harmonic to W^{2,q} to C^∞ on the Einstein limit work?

4. §5 A-cancellation: The global contradiction uses ∫Φ ≤ 119 Q(T) ≤ C δ² A and Vol(P^in) ≥ c₀ A to get mean(Φ) ≤ Cδ²/c₀. Does the A factor cancel correctly? Is the Liouville averaging from Step 53 §7.2 (unit tangent bundle, geodesic flow invariance) correctly invoked for pullback balls under collapse?

5. §2.7 Separation of roles: Verify that no per-datum constant from §2 leaks into the sequence-uniform estimates in §3-§5. In particular, check that the terminal curvature K in §3.1 comes from the first-exit bootstrap (sequence-uniform Γ and θr²), not from the per-datum H^{s₀} continuation.

## Output

# 科学核验备忘录

## 总体结论

- \(H^7(M^4)\hookrightarrow C^{4,\alpha}\) 对每个 \(0<\alpha<1\) 成立，但文中据此直接推出 \(C^\infty\) 终端度量的论证并不成立。主要问题是精确方程在 \(\chi=0\) 处退化，而 \(\varepsilon\)-正则化方程的 Schauder 常数一般随 \(\varepsilon\downarrow0\) 发散。
- “正则化方程唯一，因此两个精确极限相同”的拼接论证也不充分；需要精确退化系统自身的唯一性，或对正则化半群给出与 \(\varepsilon\) 无关的稳定估计。
- 终端紧性机制的核心是可行的：曲率有界、指数拉回球非坍缩、局部 \(\Phi\)-积分趋零足以得到 \(C^{1,\alpha'}\) 及强 \(W^{2,q}_{\mathrm{loc}}\) 收敛，并得到光滑 Einstein 极限。文中“由 Rellich 得 \(E_i\) 强 \(L^2\) 收敛”和“原序列升级为 \(C^\infty\) 收敛”两句不成立，也不是局部矛盾所必需的。
- \(A\)-因子的消去是正确的；指数映射多对一不会破坏单位切丛上的 Liouville 平均。
- 去掉原序列 \(C^\infty\) 收敛这一步后，§3–§5 的常数确实不依赖 §2 的逐个初值高阶常数。终端曲率直接来自统一的第一退出估计。
- 截至所给材料，公共观测时间仍未形成完整证明：除上述终端光滑性与唯一性问题外，Step 55 自己也说明一般阶的 current-pair 张量展开仍是示意公式，尚未逐项推导。

---

## 1. \(H^7\) 嵌入与终端光滑性

### 1.1 Sobolev 嵌入本身正确

在四维固定光滑背景上，
\[
H^s\hookrightarrow C^{k,\alpha}
\quad\text{若}\quad
s>k+\alpha+\frac n2.
\]
取 \(s=7,n=4,k=4\)，条件成为
\[
7>4+\alpha+2,
\]
即对每个 \(\alpha<1\) 成立。因此
\[
H^7(M^4)\hookrightarrow C^{4,\alpha}(M)
\]
是正确的；\(\alpha=1\) 不包含在内。

文中“\(7>n/2+2=4\)，所以嵌入 \(C^{4,\alpha}\)”给出的数值理由不对。真正使用的是
\[
7>\frac n2+4+\alpha=6+\alpha.
\]

### 1.2 一致 \(H^7\) 有界并不自动给出整条时间曲线收敛

式 (2.6) 只给
\[
\sup_{t<T_*}\|g(t)\|_{H^7(\bar g)}<\infty.
\]
这只能先给出子列紧性，不能单独推出 \(g(t)\) 在 \(t\uparrow T_*\) 时有唯一极限。

现有 current-pair 数据事实上可能补上时间 Cauchy 性。因为
\[
\partial_tg=-2aE,
\]
而 \(\bar\nabla^j(aE)\) 可由 \(U_j=\nabla^j(aT)\) 与
\(\bar\nabla^\ell A,\ \ell\le j-1\) 表示，所以若 (2.3)、(2.5) 已严格建立到 \(U_7\)，则
\[
\sup_{\tau\le t<T_*}\|\partial_tg(t)\|_{H^7(\bar g)}<\infty.
\]
于是
\[
\|g(t_2)-g(t_1)\|_{H^7}
 \le \int_{t_1}^{t_2}\|\partial_tg(s)\|_{H^7}\,ds
 \le C_\tau |t_2-t_1|,
\]
从而得到强 \(H^7\) 极限，再由 Sobolev 嵌入得到强 \(C^{4,\alpha}\) 极限。这个时间导数步骤在 Step 56 §2.4–§2.5 中没有写出。

### 1.3 \(\varepsilon\)-Schauder 不能推出精确退化极限光滑

对固定 \(\varepsilon>0\)，DeTurck 系统的主系数为
\[
(\beta^2+\varepsilon)g^{ab},
\]
确实严格抛物。但其椭圆性常数至少含有 \(\varepsilon\)，因此高阶 Schauder 常数通常含 \(\varepsilon^{-1}\) 的幂。逐个 \(\varepsilon\) 的
\[
C^{4,\alpha}\to C^{6,\alpha}\to\cdots
\]
不能在没有 \(\varepsilon\)-一致高阶估计时传递到 \(\varepsilon\to0\) 的精确流。

对精确系统：

- 在 \(\{\chi>0\}\) 的紧子区域，局部严格抛物，可作局部正则化；
- 在 \(\chi\equiv0\) 的开集，度量保持不动；
- 在 \(\chi\) 从正值退化到零的交界处，上述两种论证都不能直接给出全局 \(C^\infty\) 控制。

因此 §2.5 的 \(C^\infty\) 终端收敛没有由现有推导支持。数学上可替代这一环节的对象是：与 \(\varepsilon\) 无关的所有阶加权估计，或者一个以统一 \(H^7\) 范数为寿命参数的退化系统局部适定性定理。所附材料没有给出其中任一完整定理。

---

## 2. §2.6 的重启与唯一性

“两个解都是唯一的 \(\varepsilon\)-正则化系统的极限，所以二者一致”这一推理不成立。

设 \(S_\varepsilon(t)\) 为正则化半群。旧分支从 \(g(\tau)\) 出发，其正则化终端数据是
\[
S_\varepsilon(T_*-\tau)g(\tau),
\]
它通常只在 \(\varepsilon\to0\) 后趋于 \(g(T_*)\)。重启分支的正则化系统则直接从 \(g(T_*)\) 出发。对固定 \(\varepsilon\)，这两组初值并不相同，所以正则化方程的唯一性不能把它们等同起来。

即使两组初值之差趋零，还需要类似
\[
\sup_{0\le s\le s_0}
\|S_\varepsilon(s)u_\varepsilon-S_\varepsilon(s)v_\varepsilon\|_{H^7}
\le C\|u_\varepsilon-v_\varepsilon\|_{H^7},
\]
且 \(C\) 与 \(\varepsilon\) 无关，才能把唯一性传给极限。文中没有这样的稳定估计。另一种充分数学内容是精确退化 DeTurck 系统在 \(H^7\) 中的直接能量唯一性；这也没有在所给文件中出现。

严格说，若已经有足够光滑的终端数据，并有从该数据出发的精确解，简单连接前后两段通常不需要“重叠区唯一性”。当前真正缺少的是终端光滑性或 \(H^7\) 层级的局部延拓定理，而不是形式上的拼接。

---

## 3. 终端拉回球紧性

### 3.1 拉回球非坍缩成立，但 \(\rho\) 必须处于曲率尺度内

若
\[
|\operatorname{Rm}|\le K
\]
沿所有相关径向测地线成立，并且
\[
\rho<cK^{-1/2}
\]
（更精确地，可取小于相应共轭半径），Rauch 比较给出
\[
c(K,\rho)t^3\le J_p(t,u)\le C(K,\rho)t^3.
\]
因此指数拉回度量在切空间球上非退化，并有
\[
c(K,\rho)\rho^4
\le \operatorname{Vol}_{(\exp_p)^*g}(\mathcal B_\rho)
\le C(K,\rho)\rho^4.
\]

指数映射在底流形上可以多对一；这不影响拉回球本身的体积估计。

Proposition 1.2 写成“任意 \(0<\rho\le r/2\)”过强。§4.1 实际又加入了 \(\rho\le\rho_0(K)\)。正确半径应满足
\[
\rho\le \min\{r/2,\rho_0(K),\rho_{\mathrm{buffer}}\}.
\]
固定一个这样的正半径已足够支持后面的局部矛盾。

### 3.2 \(C^{1,\alpha}\) 与 \(W^{2,q}\) 紧性可由终端数据得到

在较小拉回球上，曲率上界和上述体积下界给出统一 harmonic radius。经过 harmonic 坐标变换，可取子列使
\[
g_i\to g_\infty\quad\text{于 }C^{1,\alpha'}_{\mathrm{loc}},
\]
并且
\[
g_i\rightharpoonup g_\infty\quad\text{于 }W^{2,q}_{\mathrm{loc}}
\]
对所有有限 \(q\) 成立。

文中写“\(E_\infty\) 是 \(E_i\) 的 \(W^{2,q}\) 弱极限”不准确。具有 \(W^{2,q}\) 控制的是 \(g_i\)；\(E_i=\operatorname{Ric}_{g_i}+g_i\) 先只有 \(L^q\) 控制。

### 3.3 强 \(W^{2,q}\) 收敛的正确来源

若选出的中心满足
\[
\mathcal A_\rho\Phi(p_i)\to0,
\]
则由于 \(\Phi\ge |E_i|^2\) 且拉回球体积一致有界，
\[
\|E_i\|_{L^2(\mathcal B_\rho)}\to0.
\]
曲率上界还给出 \(\|E_i\|_{L^\infty}\le C(K)\)，所以插值得到
\[
E_i\to0\quad\text{强于 }L^q_{\mathrm{loc}}
\]
对每个有限 \(q\) 成立。

在 harmonic 坐标中，
\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=2(g_i)_{jk}-2(E_i)_{jk}
 +Q_{jk}(g_i^{-1},\partial g_i).
\]
由于 \(g_i\to g_\infty\) 强于 \(C^{1,\alpha'}\)，且 \(E_i\to0\) 强于 \(L^q\)，内点椭圆估计给出
\[
g_i\to g_\infty
\quad\text{强于 }W^{2,q}_{\mathrm{loc}}.
\]
这才是强 \(W^{2,q}\) 的依据。

文中的 Rellich 句子不对：Rellich 可把 \(W^{2,q}\) 紧化到较低阶空间，但不能直接使包含二阶导数的 \(E_i\) 强 \(L^2\) 收敛。

### 3.4 极限光滑，但原序列不必 \(C^\infty\) 收敛

极限满足
\[
\operatorname{Ric}_{g_\infty}=-g_\infty
\]
的弱形式。取 \(q>4\)，Einstein 方程的 harmonic-coordinate 椭圆正则性依次给出
\[
W^{2,q}\to C^{1,\alpha}\to C^{2,\alpha}\to C^\infty.
\]
因此 \(g_\infty\) 是光滑 Einstein 度量。

不过，仅有 \(E_i\to0\) 于 \(L^q\) 并不给出 \(E_i\) 的高阶导数控制，所以不能推出
\[
g_i\to g_\infty\quad\text{于 }C^\infty_{\mathrm{loc}}.
\]
后续只需强 \(W^{2,q}\)：曲率是二阶导数加一阶导数的二次项，故曲率强 \(L^q\) 收敛足以传递文中代数型的 Weyl 密度和谱关系。Derdziński 定理只作用于已经光滑的极限。

谱计算本身一致：
\[
\left(-\frac16\right)^2
+2\left(\frac1{12}\right)^2=\frac1{24},
\]
而四维 Kähler–Einstein 度量 \(\operatorname{Ric}=-g\) 有
\[
\operatorname{spec}(W^+)
=\left(-\frac23,\frac13,\frac13\right),
\qquad |W^+|^2=\frac23,
\]
与校准谱不相容。

---

## 4. \(A\)-因子消去与 Liouville 平均

接受 Step 45 的
\[
\int_M\Phi\,d\mu\le119Q(T)
\]
以及 Step 53 的平均公式后，代数是正确的：
\[
Q(T)\le C Q(0)
\le C\delta^2\operatorname{Vol}(M)
\le C\delta^2A,
\]
并且
\[
\operatorname{Vol}(P^{\rm in})\ge c_0A.
\]
于是
\[
\frac1{\operatorname{Vol}(P^{\rm in})}
\int_{P^{\rm in}}\mathcal A_\rho\Phi(p)\,d\mu(p)
\le \frac{C\delta^2A}{c_0A}
=\frac{C\delta^2}{c_0}.
\]
因此存在中心 \(p\) 具有相同上界，\(A\) 完全消去。

若 \(\delta\) 是 \(g^{-1}E\) 的算子范数，而 \(Q=\int|E|_{\mathrm{HS}}^2\)，则四维中应写
\[
Q(0)\le4\delta^2\operatorname{Vol}(M),
\]
只是把维数常数吸收到 \(C\) 中。

Liouville 平均在坍缩情形仍有效。拉回球的分子可写成
\[
\int_{S_pM}\int_0^\rho
\Phi\bigl(\pi\varphi_t(p,u)\bigr)
J_p(t,u)\,dt\,d\sigma_p(u),
\]
其中 \(J_p(t,u)\le C(K,\rho)t^3\)。积分中心从
\(P^{\rm in}\) 扩大到 \(M\)，再利用测地流 \(\varphi_t\) 保持 Liouville 测度，得到
\[
\int_{P^{\rm in}}\mathcal A_\rho\Phi(p)\,d\mu(p)
\le C(K,\rho)\int_M\Phi\,d\mu.
\]
多条切向量映到同一底流形点只会按切丛测度计数，不要求指数映射单射。

一个小的常数记号问题是，(3.3) 实际给出
\[
Q(T)\le
e^{\,2C_H\theta+C_VV_*}Q(0),
\]
不能无附加关系直接写成 \(e^{C\theta}Q(0)\)。写成
\(C(\theta,V_*)Q(0)\) 即可，且不影响 \(A\)-消去。

---

## 5. 逐个初值常数与统一终端常数

§3.1 的终端曲率来自
\[
\|aF_T(T)\|_\infty
\le \frac{C\Gamma}{T},
\qquad T=\theta r^2.
\]
在平台 \(a=1\) 上，
\[
|\operatorname{Rm}|
\le |T|+|G|
\le \frac{C\gamma_*}{\theta r^2}+C_4.
\]
因此
\[
K=K(\gamma_*,\theta,r)
\]
不含 §2 中的 \(K_\tau\)、固定背景 Sobolev 常数或高阶 current-pair 常数。

同样：

- 双 Lipschitz 常数只由 \(V_*\) 控制；
- \(Q(T)/A\) 只用统一传播式；
- 拉回球体积只由 \(K,\rho\) 控制；
- harmonic-coordinate 紧性只用 \(K,\rho,v_0\)；
- 局部 \(\eta\) 来自上述统一局部类及校准 Einstein germ 的不存在性。

所以 §3–§5 的核心估计没有从 §2 泄入逐个初值常数。§4.4 所写的原序列 \(C^\infty\) 收敛若保留，则会要求额外的统一高阶信息；改为“极限光滑、原序列强 \(W^{2,q}_{\mathrm{loc}}\) 收敛”后，这一分离是成立的。

最后，所附 JSON 的 21 项测试确实验证了指数、谱范数、层级计数和代数消去，但文件自身也注明这些只是结构与代数验证。它没有覆盖退化 Schauder、精确极限唯一性或一般阶张量展开。因此，终端紧性与 \(A\)-消去具有可修正的严密证明框架，而公共观测时间中的光滑延拓仍依赖尚未给出的退化系统适定性和高阶 current-pair 推导。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 1,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step1_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step1_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Read the active Yau26 target and the Step 1 route/scaling package. Produce a mathematically ambitious but target-faithful memo proposing genuinely different routes toward either proving or refuting the exact proposition Q_n (closed connected smooth real manifolds; pure dimension-only Ricci quadratic-form pinching; output any Einstein metric on the same smooth manifold). Do not change the target, and do not treat restricted stability, ansatz nonexistence, or weighted/Lp estimates as a solution. Focus on routes that could cross the central gap: pure Ricci pinching without noncollapse/full-curvature/spectral assumptions. For each promising route, state the mechanism, why it might be strong, what would distinguish it early, and its likely failure mode. Pay special attention to dimensions n>=4, negative-branch uniform stability versus counterexamples, positive-branch topological obstructions, collapse, orbifold desingularization, Lohkamp/prescribed-Ricci flexibility, and possible new invariants or compactness alternatives.

## Integrated Scientific Memo

# Yau 第26题：跨越“纯 Ricci 夹逼”核心缺口的路线备忘录

固定维数 \(n\)，记
\[
\delta_\sigma(g)=\sup_M\|g^{-1}\Ric_g-\sigma I\|_{\mathrm{op}},
\qquad \sigma\in\{+1,-1\},
\]
以及
\[
\Gamma_n^\sigma=\inf_{\Ein(M)=\varnothing}\inf_g\delta_\sigma(g).
\]
则
\[
P_n^\sigma\iff \Gamma_n^\sigma>0,\qquad
Q_n\iff P_n^+\vee P_n^-.
\]
因此证明 \(Q_n\) 只需证明一个符号分支；但在某固定维数反驳 \(Q_n\)，必须同时构造
\[
\Gamma_n^+=\Gamma_n^-=0.
\]
这使“只攻击负分支”的反例计划在逻辑上不足，而正分支可能成为整个命题的保护壳。

低维基线是 \(Q_2\) 成立，且现有材料强烈支持 \(Q_3\) 的两支均成立；真正困难从 \(n\ge4\) 开始。

---

## 一、最值得优先辨别的总分岔

纯 Ricci 夹逼不能控制 \(n\ge4\) 的 Weyl 曲率，因此任何一般证明必须处理四种逃逸：

1. 曲率集中与 ALE 泡；
2. 塌缩；
3. 负分支的无界直径、长颈和低谱；
4. Einstein 线性化的近核及有限维阻碍。

反例则必须同时完成：

1. 无权、逐点、相对于输入度量的 \(\delta_\sigma(g_j)\to0\)；
2. 固定维数；
3. 底层流形上排除任意符号、任意位置的全部 Einstein 度量；
4. 若要否定 \(Q_n\)，在同一维数击败两个符号分支。

最关键的早期分岔不是“用流还是用拼接”，而是：

> **紧 Ricci 各向同性是否仍允许任意拓扑的局部插入？**

若允许，则 Lohkamp 型柔性、长颈或消解可成为反例机器；若不允许，则应存在某种 Ricci-only 的结构紧性或“无小把手”定理。

---

# 二、证明方向

## 1. 负分支：把 Min-Oo 的全局 Sobolev 步骤改造成多尺度局部衰减

### 机制

Min-Oo 对
\[
h=\Ric-\frac rn g,\qquad r<0
\]
沿归一化 Ricci 流得到本质上的反应—扩散不等式
\[
\frac d{dt}\|h\|_{L^2}^2
\le \frac rn\|h\|_{L^2}^2
+C(n)\|h\|_\infty\|h\|_{L^2}^2.
\]
当 \(\Ric\approx-g\) 时，\(r/n\approx-1\)，这是只依赖维数的真正阻尼。现有证明使用直径与完整截面曲率尺度界来：

- 保证短时完整曲率控制；
- 控制 Sobolev 常数；
- 将 \(L^2\) 衰减提升为 \(L^\infty\) 衰减。

准确的附加尺度量约为
\[
\diam(g)^2\max |\sec_g|<\Lambda^2,
\]
而不是注入半径假设。因而任何反例序列若落在该定理的归一化内，必须使这一量失控。

新的目标应是局部化上述论证。设
\[
\Ric=-g+E,\qquad \|E\|_{L^\infty}\le\varepsilon.
\]
在每个 Ricci 尺度球上建立热核或 Moser 型估计，再通过覆盖空间和厚薄分解传播阻尼，而不使用全局 Sobolev 常数。危险低频部分应单独投影为几何模参数，而不是粗暴估计。

### 为什么可能足够强

负 Einstein 常数提供正分支没有的零阶耗散。若局部阻尼能够跨越长几何和塌缩，则可直接得到 \(P_n^-\)，从而得到 \(Q_n\)。

### 早期判别

检验闭双曲曲面乘积及其高亏格序列。适当归一化后它们满足 \(\Ric=-g\)，但直径可趋于无穷，且存在零混合截面曲率。若对其小的 \(\delta_-\)-扰动仍能获得统一局部衰减，说明 Min-Oo 的 \(\Lambda\) 很可能只是证明工具的产物。

另一个判别对象是长颈上的最小线性化特征值。需区分：

- 小特征值来自真正 Einstein 模空间，可由参数吸收；
- 小特征值产生非零余核阻碍，可能导向反例。

### 主要失败方式

- 初始 Weyl 曲率可在任意小尺度爆破，导致流的短时常数失控；
- 长颈使 Poincaré 常数退化，局部阻尼无法形成全局收敛；
- 解沿流逃向轨形、尖点或塌缩极限，而没有同一光滑流形上的平滑极限。

---

## 2. Ricci-only 紧化：先分类所有近 Einstein 逃逸，再逐类恢复存在性

### 机制

先证明一个“带源项的 Einstein 紧化定理”：
\[
\Ric_{g_i}=\sigma g_i+E_i,\qquad \|E_i\|_{L^\infty}\to0.
\]
在四维、非塌缩和有界直径情形，期望得到：

- 除有限点外光滑收敛到 Einstein 轨形；
- 曲率集中处出现 Ricci-flat ALE 泡树；
- 颈区具有 Ozuch 型加权坐标控制；
- \(E_i\) 在吹起尺度上成为低阶源项。

四维 Chern–Weil 还给出
\[
\int |\Ric^0_{g_i}|^2\to0,
\]
而完整曲率能量由拓扑量和小误差控制。这个路线不假装已有工具覆盖塌缩；其目标是将一般失败分解为明确的“非塌缩泡树、塌缩、长直径、近核”四类。

### 为什么可能足够强

它把不可见的 Weyl 爆破转换为有限局部模型，继而可使用消解阻碍、有限维约化和拓扑信息。如果证明每种极限拓扑都已承载某个 Einstein 度量，则无需让输出接近输入。

### 早期判别

证明局部定理：在体积非塌缩球上，若 \(|\Ric|\le C\) 且 \(\|\Ric-\sigma g\|_\infty\to0\)，则任何曲率集中吹起均为 Ricci-flat ALE，且近似 Einstein 源项不会破坏颈衰减。

### 主要失败方式

紧化本身不解决：

- 塌缩；
- 负分支无界直径；
- 轨形消解的阻碍；
- 同一拓扑上可能存在远离该极限的 Einstein 度量。

所以它应作为结构归约，而非独立解答。

---

## 3. 正分支：建立“塌缩必为 Einstein-preserving 塌缩”的结构定理

### 机制

若
\[
\delta_+(g)\le\varepsilon<1,
\]
则
\[
\Ric\ge(1-\varepsilon)g,\qquad
\diam M\le \pi\sqrt{\frac{n-1}{1-\varepsilon}},
\]
且 \(\pi_1(M)\) 有限。仍无体积或注入半径下界；精确正 Einstein 商空间本身即可塌缩。因此正确结论不能是“不塌缩”，而应是：

> 足够小的正 Ricci 各向异性只允许有限商、局部齐性商或某些总空间本已承载 Einstein 度量的有组织塌缩。

在局部纤维模型中，利用 O’Neill 公式比较水平、垂直及混合 Ricci。真正缩小纤维时，纤维曲率、第二基本形式及 \(A,T\)-张量通常在不同方向产生不同阶的 Ricci 贡献。目标是证明非商型塌缩必有
\[
\lambda_{\max}(g^{-1}\Ric)-\lambda_{\min}(g^{-1}\Ric)\ge \eta_n>0.
\]

### 为什么可能足够强

正分支已有统一直径和有限基本群。若排除“坏塌缩”，非塌缩部分可进入轨形紧化；证明 \(P_n^+\) 本身就足以证明 \(Q_n\)，无须解决负分支。

### 早期判别

在 Berger 球、齐性纤维化和一般 Riemannian submersion 上严格计算上述谱宽。Berger 型 Hopf 塌缩中，Ricci 主值随纤维缩小明显分离，说明普通纤维塌缩与紧各向同性不相容；但球面空间形式的有限商保持精确 Einstein，必须被结构定理允许。

### 主要失败方式

双边 Ricci 有界下的塌缩远比截面曲率有界塌缩复杂；高 Weyl 区域可能没有经典 \(F\)-结构。即使得到拓扑纤维化，也未必能在总空间上构造 Einstein 度量。

---

## 4. 正分支的“不存在微小拓扑把手”原理

### 机制

反例最自然的构造是把无 Einstein 拓扑藏进小体积区域。可先在旋转或双重 warped 模型中寻找尺度无关缺陷下界。例如
\[
g=dt^2+a(t)^2g_{S^p}+b(t)^2g_{S^q}
\]
的三个 Ricci 特征值是
\[
r_t=-p\frac{a''}{a}-q\frac{b''}{b},
\]
\[
r_p=(p-1)\frac{1-(a')^2}{a^2}-\frac{a''}{a}
-q\frac{a'b'}{ab},
\]
\[
r_q=(q-1)\frac{1-(b')^2}{b^2}-\frac{b''}{b}
-p\frac{a'b'}{ab}.
\]
寻找满足光滑帽端或连通和端点条件的积分恒等式，证明任何拓扑改变颈都满足
\[
\sup_t\max\{|r_t-1|,|r_p-1|,|r_q-1|\}\ge\eta_{p,q}>0.
\]

最终需要把该 ODE 现象提升为不依赖对称性的焦点、指数映射或稳定超曲面定理。

### 为什么可能足够强

它直接阻止最可能的正分支反例机制，而不要求分类所有正 Ricci 流形。

### 早期判别

使用区间算术严格求解上述变分问题；若最优缺陷随颈长仍有正下界，则存在真正的局部刚性信号。若缺陷可按 \(L^{-1}\) 衰减，则长颈可能成为反例引擎。

### 主要失败方式

Weyl 自由度可能让非对称高维颈绕过 warped-product 下界；族内证书不能自动推广到全部度量。

---

## 5. 全局椭圆度或模二计数：把近核当成参数而非病态常数

### 机制

固定 Bianchi 规范后考虑
\[
\mathcal F_\sigma(g)=\Ric_g-\sigma g+\delta_g^*B_{\bar g}g.
\]
近 Einstein 度量是 \(\mathcal F_\sigma\) 的近零点。在线性近核上作 Lyapunov–Schmidt 分解，将 ALE 尺度、轨形变形、颈模量和覆盖参数纳入有限维变量。目标不是统一控制整个 \(L^{-1}\)，而是：

1. 对近核正交补建立维数控制；
2. 对约化映射定义度数或模二交数；
3. 证明所有泡树边界贡献抵消或具有已知奇偶性。

Ozuch 的工作说明：在非塌缩四维 Einstein 退化中，靠近轨形的精确 Einstein 度量确实受拼接模型控制。这为定义局部边界贡献提供了基础。

### 早期判别

在 Eguchi–Hanson/Calabi 单泡模型上计算约化阻碍穿过零壁时的局部度数。若简单零具有非零局部度，可能形成全局计数；若壁两侧贡献成对消失，则该不变量无效。

### 主要失败方式

纯 Ricci 夹逼并不给 Einstein 模空间的适当性；塌缩、长颈和符号变化可能引入无穷多个边界分量，使全局度无法定义。

---

# 三、反例方向

## 6. Lohkamp／prescribed-Ricci 的“紧各向同性柔性”测试

### 机制

普通结论“每个高维闭流形承载 \(\Ric<0\) 度量”远远不够。决定负分支的是更强量
\[
\Phi_n^-(M)=\inf_g\delta_-(g).
\]
若能证明某固定维数中的丰富流形族满足
\[
\Phi_n^-(M)=0,
\]
再与排除全部 Einstein 度量的拓扑或光滑结构障碍结合，即可否定 \(P_n^-\)。

可尝试：

- 定量 prescribed-Ricci 局部块；
- 长尺度手柄，使过渡导数按 \(L^{-1}\) 衰减；
- 通过高频局部修正点态各向同性，而非只控制平均 Ricci；
- 将 Bianchi 兼容条件作为辅助未知量共同求解。

### 为什么可能足够强

负标量曲率没有正标量曲率那样的直接拓扑阻碍，因此负 Ricci 柔性最可能接近任意拓扑。

### 早期判别

在可实现手柄的 cohomogeneity-one 或 slowly varying 横截面模型上，直接估计
\[
\inf \sup \|g^{-1}\Ric+I\|_{\mathrm{op}}
\]
是否随颈长趋零。单 warped 模型中，精确方程 \(\Ric=-g\) 强迫双曲型 ODE，显示明显刚性；真正问题是慢变、非对称横截面能否绕过它。

### 主要失败方式

传统负 Ricci 手术只保持符号，过渡区通常有阶一各向异性。Bianchi 恒等式和 Levi-Civita 兼容性可能形成紧 pinching 的 \(h\)-principle 障碍。

即使成功否定 \(P_n^-\)，仍需在同一维数独立否定 \(P_n^+\)。

---

## 7. 轨形消解反例：必须消去无权核心阻碍，而不是依赖加权小量

### 正确缩放

在 Morteza–Viaclovsky 的 Calabi 核心，紧致消解度量满足
\[
g_t\sim t g_{\rm cal},
\]
且
\[
\Ric_{g_t}-\Lambda g_t-t\lambda\chi_t o
=O_{g_{\rm cal}}(t^2\rho^2).
\]
相对于 \(g_t\) 的 \((0,2)\)-张量算子范数多出 \(t^{-1}\)，所以余项变成
\[
O_{g_t}(t\rho^2).
\]
核心中为 \(O(t)\)，过渡尺度 \(\rho\sim t^{-1/4}\) 时为 \(O(t^{1/2})\)，均可趋零。

但阻碍项满足
\[
\|t\lambda o\|_{g_t,\mathrm{op}}
\sim |\lambda|\,\|o\|_{g_{\rm cal},\mathrm{op}},
\]
若 \(\lambda\ne0\)，核心处保持阶一。因此已知“首阻碍非零，附近无 Einstein”的例子并不产生 Yau26 所需的无权 \(C^0\) pinching。

### 真正可行的改进

必须找到：

1. 首阻碍恰为零；
2. 或轨形族的阻碍系数 \(\lambda_j\to0\)；
3. 或由合法局部/全局参数消去首阻碍；
4. 但高阶或全局阻碍仍不为零；
5. 且消解流形上不存在任何远处、任意符号的 Einstein 度量。

若 \(\lambda_j\to0\)，可再选 \(t_j\to0\)，使核心缺陷 \(O(\lambda_j)\) 与过渡缺陷 \(O(t_j^{1/2})\) 同时消失。

### 为什么可能足够强

它能够在体积趋零的区域插入光滑拓扑，同时外部保持精确 Einstein，是最具体的点态 pinching 反例框架。

### 早期判别

计算候选紧 Einstein 轨形的首阻碍
\[
n\langle\mathcal R(\omega),\omega\rangle
+2(n-2)R.
\]
非零 Einstein 常数的 Kähler–Einstein 轨形通常给出非零量，因此不适合直接构造。应搜索非 Kähler 轨形族、多个奇点间的耦合参数，或首阶相消但高阶不相消的情形。

### 主要失败方式

首阻碍消失往往正是 Einstein 消解存在的条件；反之，高阶阻碍可能只排除同一退化邻域，而不能排除底层流形上的其他 Einstein 度量。

Ozuch 的例子只有
\[
\|\Ric-3g\|_{L^p}\to0,\qquad \Ric\ge3g,
\]
以及不存在具有指定 GH 极限的 Einstein 序列；这既不是 \(\delta_+\to0\)，也不是全局无 Einstein。

---

## 8. 为点态缺陷设计 Pohozaev／通量不变量

### 机制

设 \(\eta\) 是 ALE 线性化核张量，试图建立
\[
\int_\Omega
\langle \Ric_g-\sigma g,\eta\rangle\,dV
=
\int_{\partial\Omega}\mathcal U(g,\eta)
+\text{受控规范项}.
\]
若
\[
\|\Ric_g-\sigma g\|_{g,\mathrm{op}}\le\varepsilon,
\]
且 \(\eta\) 有适当归一化，则左侧受
\[
C\varepsilon\,\Vol(\Omega)
\]
控制；右侧可能收敛到由 ALE 端、轨形曲率或泡拓扑决定的非零量。这会直接给出
\[
\delta_\sigma(g)\ge \eta_0
\]
或刻画首个必须消失的局部量。

应继续寻找高阶、多泡版本，并检查其是否与 Euler、signature、边界 \(\eta\)-量或重整化体积相联系。

### 为什么可能足够强

它把加权拼接阻碍翻译成原题需要的无权 \(C^0\) 缺陷下界，也可解释哪些局部拓扑根本无法被紧 pinching 隐藏。

### 早期判别

用该通量公式重新推导 Calabi 首阻碍，并准确恢复上述阶一核心项。若公式只能给出 \(L^p\) 或加权控制，它不能跨越中央缺口。

### 主要失败方式

通量通常只限制靠近指定轨形退化的度量。除非另有紧性定理迫使候选拓扑上的所有 Einstein 度量进入该退化类，否则它不能证明全局无 Einstein。

---

## 9. 四维正分支：寻找兼容正标量曲率的新型全 Einstein 障碍

### 已有硬约束

若闭定向四流形满足
\[
\delta_\sigma(g)\le\varepsilon<
\frac1{1+\sqrt3},
\]
则
\[
2\chi(M)>3|\tau(M)|.
\]
因此违反或达到 Hitchin–Thorpe 边界的流形不可能成为任意紧的正或负分支反例。

对于正分支，输入本身有正标量曲率。故任何同时阻碍正标量曲率的 Dirac 或 monopole 工具也会排除输入，而不能制造反例。必须寻找满足以下三项的新不变量：

1. 允许正 Ricci 或至少正标量曲率；
2. 满足严格 Hitchin–Thorpe；
3. 排除任意符号的全部 Riemannian Einstein 度量。

### 为什么可能足够强

若能与局部正 pinched 拓扑插入结合，它将补齐反驳 \(Q_4\) 最困难的一半。

### 早期判别

对每个已知“正 Ricci 但无已知 Einstein”的四流形，区分：

- 已严格证明无全部 Einstein；
- 只证明无 Kähler–Einstein；
- 只证明某 ansatz 无解；
- 事实上已有非 Kähler Einstein 度量。

尤其不能把某复结构的 K-不稳定性当成底层光滑流形无 Einstein。

### 主要失败方式

可能根本不存在这样的障碍：紧正 Ricci 各向同性也许已经强迫底层拓扑属于某个 Einstein-admitting 类。若如此，正分支更可能为真。

---

## 10. 熵与体积刚性：阻止“在双曲底上藏小拓扑”

### 机制

若候选负分支反例由双曲流形 \(N\) 经连通和或局部手术得到，并有度一映射 \(M\to N\)，则在适当归一化下熵—体积不等式可约束
\[
h(g)^n\Vol(M,g).
\]
若手术声称在体积趋零的区域加入拓扑，同时总体积逼近双曲体积，刚性可能迫使其回到双曲结构，从而给出缺陷下界。

### 为什么可能有用

它针对最常见的反例原型，而无需控制 Weyl 曲率。

### 早期判别

对每个负 pinched 手术模型计算其体积超额和熵。若拓扑改变而体积仍逼近刚性下界，应期待某处存在不可消去的 Ricci 各向异性。

### 主要失败方式

原题没有体积限制；反例可以让总体积趋于无穷。因此该路线只能否定特定构造，不会单独证明 \(P_n^-\)。

---

# 四、需要纠正的两项路线判断

## 1. 正分支并不因“正标量曲率杀死 SW”而自动接近解决

正标量曲率确实排除了许多 monopole-class 候选，Chern–Weil 也排除了 Hitchin–Thorpe 违反者；但这只说明常用四维反例库不足，不能推出所有无 Einstein 障碍都已消失，更不能推出高维拓扑分类。正分支仍面对：

- 不受控 Weyl；
- 允许的 Einstein 商塌缩；
- 轨形阻碍；
- 不存在统一局部线性逆的可能性。

因此“优先研究正分支”有逻辑吸引力，但尚无证据证明它比负分支更接近完成。

## 2. Ricci 下界或 RCD 理论不能直接给出接近球面

\(\Ric\approx+g\) 给出 Myers 直径上界，但没有接近最大直径、接近 Obata 第一特征值或体积接近球面的条件。故现有 Ricci 下界的 almost-rigidity 不能仅由 \(\delta_+\ll1\) 自动调用。若要使用合成几何，必须先从双边 Ricci 各向同性推出新的非塌缩、谱或密度结论；这正是待证核心，而不是现成工具。

---

# 五、最有区分力的具体研究对象

以下对象能以较低成本改变核心判断：

### A. 正分支纤维塌缩谱宽
对一般齐性 submersion 和可控 infranil 纤维模型，证明或否定
\[
\lambda_{\max}(g^{-1}\Ric)-\lambda_{\min}(g^{-1}\Ric)
\ge\eta_n
\]
在非商型塌缩中的统一下界。需同时保留精确 Einstein 商作为反例校准。

### B. 负分支长颈最优缺陷
在满足真实光滑端点条件的多 warped 模型中求
\[
\inf \sup_t \|g^{-1}\Ric+I\|_{\mathrm{op}}
\]
随颈长的渐近。若趋零，紧负 Ricci 手术具有可信度；若有正下界，支持统一稳定性。

### C. Calabi 消解的全区域无权误差
对每个候选族明确写出
\[
\delta_\sigma(g_t)
\le
C\bigl(|\lambda|+t^{1/2}+\text{外部匹配误差}\bigr),
\]
而不是只给加权 Hölder 或 \(L^p\) 估计。首阻碍非零即淘汰该候选。

### D. \(H^2\times H^2\) 及长直径负 Einstein 背景
研究线性化近核、局部热核衰减和覆盖空间估计是否与亏格、直径无关。这直接判断 Min-Oo 的全局依赖是否本质。

### E. 四维候选数据库的兼容性筛选
同时记录：

- 是否严格满足 \(2\chi>3|\tau|\)；
- 是否承载正标量或正 Ricci；
- 无 Einstein 结论是否排除所有符号和全部度量；
- 是否可能具有 \(c_1<0\)、Calabi–Yau 或其他已知 Einstein 结构；
- 已知障碍能否反过来给出 \(\delta_\sigma\) 正下界。

---

# 六、综合判断

目前最完整的证明架构是：

\[
\text{Ricci-only 退化分类}
+\text{坏塌缩排除}
+\text{近核参数化}
+\text{各退化类上的拓扑存在性}.
\]

其中负分支可利用 Min-Oo 的负反应阻尼，正分支可利用 Myers 的直径控制；两者优势互补，但都尚缺纯 Ricci 条件下对 Weyl、塌缩和近核的统一处理。

最可信的反例架构则是：

\[
\text{紧各向同性柔性或首阻碍消去的消解}
+\text{无权 }C^0\text{ 缺陷趋零}
+\text{全局无 Einstein 障碍}.
\]
四维负分支可能由 Lohkamp 型柔性与 LeBrun 型障碍结合；正分支明显更困难，因为紧 pinching 已排除 Hitchin–Thorpe 反例，而许多规范理论障碍又与正标量输入冲突。任何对 \(Q_n\) 的反驳都必须解决这一正分支瓶颈，而不能以负分支成功替代。

当前最精确的未决科学对象可以压缩为两个量：

\[
\inf_{\Ein(M)=\varnothing}\inf_g\delta_- (g),
\qquad
\inf_{\Ein(M)=\varnothing}\inf_g\delta_+ (g),
\]
以及导致这些下确界可能为零的全部几何逃逸。首要突破将是证明其中某一量具有维数统一正下界，或在同一固定维数为两者分别构造趋零序列。
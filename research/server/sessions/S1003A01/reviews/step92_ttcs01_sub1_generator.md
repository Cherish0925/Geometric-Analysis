# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step91_dense_carrier_consistency_and_wahl_cone_withdrawal.md",
    "Sessions/S1003A01/workspace/notes/spirit_step91_global_reduction_and_carrier_scope.md",
    "Sessions/S1003A02/workspace/notes/step102_wahl_orbifold_realization_and_K2_invariance.md",
    "Sessions/S1003A02/workspace/notes/step105_cusp_channel_restored_and_cap_charge_theorem.md",
    "Sessions/S1003A01/workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md",
    "Sessions/S1003A01/workspace/notes/step85_coupled_center_theorem_neck_trace_and_endpoint_reduction.md",
    "Sessions/S1003A01/workspace/notes/step87_csck_calibration_and_nodal_endpoint_rigidity.md"
  ]
}
```

## Task

The active goal is the unrestricted Einstein-gap programme on four-manifolds. Recent work produced three concrete global entrances for Q1 and one for Q4, but several proposed reductions were corrected. Read the supplied route synthesis, the realized Wahl-orbifold theorem, the corrected cap-charge theorem, and the established AKE endpoint results. Develop at most three mathematically serious next routes, each centered on a new implication that would materially advance Q1/Q2/Q4 rather than repackage known integral bounds. In particular compare: (i) a fixed supplied Seiberg–Witten field limit across shrinking Wahl rational-ball fillers, including what class-sensitive Einstein identity could become available after the limit; (ii) entropy/degree rigidity from the realized degree-one map to a compact complex-hyperbolic surface, noting that BCG’s direct sharp theorem is real-hyperbolic while the source may be non-Kähler; (iii) the zero-charge four-class Hopf-collapse cap and whether odd intersection form, w2, spin bordism, eta/Dirac, or F-structure theory can obstruct or construct it; (iv) a closed Goldberg route combining normalized action, no-concentration, and second-order center results. For each proposed route, state a precise theorem target, derive the key equations or topological invariant, identify one cheapest decisive calculation/source theorem, and explain what result would genuinely change the global programme. Do not assume compactness, supplied orbifold character, or exhaustive degeneration alternatives that the files do not prove.

## Output

下面三条路线分别对应 Wahl 场论输入、零电荷塌缩帽、Goldberg 端点闭合。它们都引入了现有整体曲率积分之外的新信息。复双曲熵—次数入口单独放在末尾比较：按现有常数，它尚未产生第四条独立路线。

## 一、固定 Seiberg–Witten 场穿过 Wahl 有理球收缩

### 定理目标

设 \(V\) 是带 Wahl 点 \(p_\nu\) 的紧致 Einstein 轨形，\(s_g=-\lambda<0\)。以缩放后的 Ricci-flat Kähler ALE 有理球填入 \(p_\nu\)，得到 \(M\) 上的光滑度量 \(g_\varepsilon\)，并假设每个曲率尺度极限不是 ALE 填充就是平坦锥颈。

从有限个 blow-up 基本类中，对每个 \(g_\varepsilon\) 选取满足
\[
(a_\varepsilon^+)^2\ge A
\]
的一个供应类及其未扰动 SW 解 \((A_\varepsilon,\Phi_\varepsilon)\)。有限性允许取子列使 \(a_\varepsilon=a\) 固定。目标是证明：

1. \((A_\varepsilon,\Phi_\varepsilon)\) 在 \(V\setminus\{p_\nu\}\) 上收敛到非零有限能量解 \((\bar A,\bar\Phi)\)；
2. 该解跨越各 \(p_\nu\) 延拓为某个轨形 spin\(^c\) 结构；
3. 其局部特征由光滑结构在实际 lens 端截面上的限制决定，而不是预先指定的 \(j=0\) 或任意猜测公式。

这会把“填充转移得到一个不等式”提升为“Wahl Einstein 轨形上存在一个已识别拓扑类的真实单极场”。

### 核心估计与无自旋子冒泡

取
\[
U_\varepsilon=|\Phi_\varepsilon|^2,\qquad
F_{A_\varepsilon}^+=q(\Phi_\varepsilon),\qquad
|F_{A_\varepsilon}^+|^2=\frac{U_\varepsilon^2}{8}.
\]
SW Weitzenböck 恒等式为
\[
0=\int_M\left(4|\nabla_{A_\varepsilon}\Phi_\varepsilon|^2
+s_{g_\varepsilon}U_\varepsilon+U_\varepsilon^2\right).
\]
由 harmonic projection，
\[
\int_M U_\varepsilon^2
=8\int_M|F_{A_\varepsilon}^+|^2
\ge 32\pi^2(a^+_\varepsilon)^2
\ge 32\pi^2A.
\]
另一方面，固定 \(c_1(a)^2\) 与 Chern–Weil 给出全曲率的统一 \(L^2\) 控制。

关键点是：缩放到 Ricci-flat ALE 填充或平坦锥颈后，任何有限能量极限都满足
\[
0=\int\left(4|\nabla_A\Phi|^2+|\Phi|^4\right),
\]
故 \(\Phi\equiv0\)。因此 \(L^4\) 自旋子质量不能全部落入收缩区；上面的正下界迫使 \(\bar\Phi\not\equiv0\)。有限 \(L^2\) 的 \(U(1)\) 联络随后给出局部 holonomy 表示
\[
\Gamma_{p_\nu}\longrightarrow U(1),
\]
它正是待识别的轨形特征。所需分析来源是有限能量 \(U(1)\) 联络与 Dirac 自旋子在 \((B^4\setminus0)/\Gamma\) 上的可去奇点理论。

### 极限后出现的类敏感 Einstein–SW 恒等式

令 \(\mathcal F=iF_{\bar A}\) 为实二形式，写 Hodge 分解
\[
\mathcal F=2\pi h_a+d\alpha ,
\]
其中 \(h_a\) 是固定轨形 de Rham 类 \(a\) 的 harmonic 代表。由于
\[
\|(d\alpha)^+\|_2^2=\|(d\alpha)^-\|_2^2,
\]
得到精确恒等式
\[
\boxed{
\frac18\int_V U^2-4\pi^2\|a_g^+\|^2
=
\int_V|F_{\bar A}^-|^2-4\pi^2\|a_g^-\|^2
=
\frac12\|d\alpha\|_2^2 .
}
\]
这比仅使用 \(\max(a^+)^2\ge A\) 多保留了实际供应类及其极化信息。Einstein 条件又给出
\[
0\le U\le\lambda,\qquad
4\int_V|\nabla_{\bar A}\bar\Phi|^2
=\int_VU(\lambda-U).
\]
若右端为零且 \(\bar\Phi\neq0\)，则场平行并诱导 Kähler 结构；对已知非 Kähler 候选，这迫使至少一个场能量项严格为正。

局部 torsion 特征不进入 de Rham 平方，因此还需 Kawasaki 指数：
\[
\operatorname{ind}_{\rm orb}D_{\bar A}
=
\int_V\widehat A(TV)e^{c_1(\bar L)/2}
+\sum_\nu\kappa_{p_\nu}(\mathfrak s),
\]
其中
\[
\kappa_{p}(\mathfrak s)
=
\frac1{|\Gamma_p|}
\sum_{\gamma\neq1}
\frac{\operatorname{tr}\sigma_{D,\mathfrak s}(\gamma)}
{\det(1-\gamma|T_pV)} .
\]
这里必须使用实际 spin\(^c\) 提升；仅知道 determinant 特征还需处理二倍扭转。

### 最便宜的决定性计算

对一个已实现的 \(k=4\) Wahl 嵌入做一次完整 Kirby/Smith 正规形计算：

\[
H^2(M)\longrightarrow H^2(W)
\longrightarrow H^2(L(n^2,n-1)),
\]
对每个真实 blow-up 基本类计算 determinant 特征，同时保留 spin\(^c\) 扭转的因子二；随后精确求 \(\kappa_n(r)\)。这会立即区分三种情形：

- 实际特征与非零极限场相容；
- 局部表示迫使特定消失阶；
- 再配合某个 cokernel Weitzenböck 消去后，指数与非零核不相容。

第一种情形会给 Q1/Q2 一个真正类敏感的轨形单极输入；后两种情形会排除相应已实现 Wahl Einstein 轨形，从而移除一条具体零间隙构造入口。

---

## 二、四类零电荷 Hopf 帽：\(D_4\) ALF 载体与奇格的 torsion 过渡

### 精确拓扑与能量匹配

令
\[
C_4=\#4\,\overline{\mathbb{CP}}^{\,2}\setminus B^4.
\]
则
\[
\chi(C_4)=5,\qquad \tau(C_4)=-4.
\]
在可容许的 Hopf 手性 \(e_{\rm out}=-1\) 下，
\[
c_+(C_4)
=(2\chi+3\tau)+e_{\rm out}-3\operatorname{sign}(e_{\rm out})
=0,
\]
而另一手性电荷为
\[
c_-(C_4)
=(2\chi-3\tau)-e_{\rm out}+3\operatorname{sign}(e_{\rm out})
=20.
\]

这与 \(D_4\) ALF hyperkähler 空间恰好匹配。若其复定向满足 \(W^+=0\)，并且 \(\chi=5\)，则 fibred-end Gauss–Bonnet 给出
\[
\frac1{8\pi^2}\int |W^-|^2=5,
\qquad
\boxed{\frac1{2\pi^2}\int|W^-|^2=20.}
\]
因此它能携带帽的全部 \(c_-\) 电荷，同时不产生任何 \(c_+\) 电荷。这比 ALE \(D_4\) 更吻合：ALE 端的群阶修正会留下一个非整数差额，而 ALF 端没有该 Euler 差额。

### 奇交叉形式如何进入

在标准奇格 \(-I_4\) 中，
\[
D_4=\left\{x\in\mathbb Z^4:\sum_i x_i\equiv0\pmod2\right\},
\qquad [I_4:D_4]=2.
\]
商群由 \(e_1+D_4\) 生成，其二次值为
\[
q(e_1)=-1\pmod{2\mathbb Z}.
\]
所以 \(D_4\) 载体只看到偶格；从 \(-D_4\) 扩张到 \(-I_4\) 的奇性必须由一个 \(\mathbb Z_2\) torsion 过渡区携带。单独使用 \(w_2\) 或 spin bordism 不会自动排除这种机制：

- \(D_4\subset I_4\) 已给出所需的指数二奇扩张；
- \(\Omega_3^{\rm Spin}=0\)，三维 spin bordism 本身不给出非零类。

真正敏感的是该 \(\mathbb Z_2\) 类上的 spin\(^c\) 二次精化及 adiabatic eta。

### 定理目标

证明下列构造定理，或由 eta 不相容排除它：

1. \(C_4\) 含有一个 \(D_4\) plumbing \(P_{D_4}\)，其补区
   \[
   R=C_4\setminus\operatorname{int}P_{D_4}
   \]
   是从 \(D_4\) prism 端截面到 \(S^3\) Hopf 端截面的有理同调 cobordism；
2. \(R\) 的相对同调中有
   \[
   H_2(R,Y_{D_4})_{\rm tors}\cong\mathbb Z_2,
   \]
   正好实现 \(D_4\subset I_4\) 的 glue coset；
3. \(R\) 携带与两端圆纤维相容的 polarized F-structure，因而存在
   \[
   \operatorname{Vol}(R,h_\ell)\to0,\qquad
   |\operatorname{Rm}_{h_\ell}|\le C;
   \]
4. 将缩放后的 \(D_4\) ALF 度量粘入后得到
   \[
   \int_{C_4}\left(|\operatorname{Ric}^\circ|^2+s^2+|W^+|^2\right)\to0,
   \qquad
   \frac1{2\pi^2}\int_{C_4}|W^-|^2\to20.
   \]

若第 3 项成立，这就是零电荷四类 Hopf 帽的真实几何模型。

### eta/Dirac 的决定性等式

在 \(R\) 上，若曲率有界而体积趋零，则 Euler 与 Pontryagin 体积分趋零。因此两端的 adiabatic 修正必须满足
\[
\mathcal E_{\rm ad}(Y_{D_4})
=\mathcal E_{\rm ad}(S^3_{\rm Hopf}),
\qquad
\mathcal H_{\rm ad}(Y_{D_4})
=\mathcal H_{\rm ad}(S^3_{\rm Hopf}),
\]
因为 \(\chi(R)=\tau(R)=0\)。

对承载奇扩张的 torsion spin\(^c\) 结构，APS 公式进一步要求
\[
\operatorname{ind}D_R^+
=
-\frac12\Big[
(\eta_D+h)_{\rm out}-(\eta_D+h)_{\rm in}
\Big],
\]
右端必须为整数，并与 \(\mathbb Z_2\) glue 类的二次精化一致。若该整数条件不成立，则任何过渡区都必须保留非零曲率积分，因而 \(c_+=0\) 模型不能实现。

### 最便宜的决定性计算

一次 Kirby–Seifert–eta 联合计算足够：

- 用根
  \[
  e_1-e_2,\ e_2-e_3,\ e_3-e_4,\ e_3+e_4
  \]
  写出 \(D_4\) plumbing 在 \(\#4\overline{\mathbb{CP}}^2\) 中的标记；
- 求补区 \(R\) 的基本群、torsion 同调与两端 Seifert 斜率；
- 用 Dai 的 adiabatic 公式和 lens/prism Dedekind 和计算 signature 与 spin\(^c\) Dirac eta。

若数值完全匹配，构造方向获得一个精确载体；若不匹配，四类零电荷帽在有界曲率 F-structure 模型中被排除。两种结果都会实质改变 Q1：前者给出非达到零间隙序列的核心局部块，后者消去目前最强的不可见塌缩机制。

---

## 三、Goldberg：把无集中、中心二阶阻碍与 Einstein 作用量离散化连接起来

### 局部端点定理目标

设 \((V,g_V,\omega_V)\) 是紧致 \(s<0\) Kähler–Einstein 轨形，\(M\) 是由同定向 Ricci-flat Kähler ALE 树平滑得到的四流形。目标是证明：

> 存在 \(V\) 的 Gromov–Hausdorff 邻域，使其中每个 almost-Kähler Einstein 平滑度量都是 Kähler–Einstein。

一个更强的形式是：附近所有 Einstein 度量都满足
\[
\widehat S(g)=\widehat S(g_V).
\]

### 三个已有结构如何闭合

对 AKE Einstein 度量，
\[
D(g):=\int\left(\frac{s^2}{24}-|W^+|^2\right)
=\frac{\widehat S(g)^2}{16}-2\pi^2T_+(M)
=T_{\rm AK}(g)\ge0.
\]
在同定向 Kähler ALE 树中，所有 bubble 都有 \(W^+=0\)，所以
\[
T_+(M)=T_+^{\rm curv}(V),\qquad D(g_V)=0.
\]

若 \(T_{\rm AK}(g_i)\to0\) 且出现非塌缩有界直径收敛，则无集中定理给出：

- 极限是 Kähler–Einstein 轨形；
- \(W^+\) 与 torsion 能量均无原子；
- 所有 bubble 都是同定向 Ricci-flat Kähler；
- \(\widehat S(g_i)\to\widehat S(g_V)\)。

在 KE 中心，任意 harmonic self-dual 形式写成
\[
\omega'=a\omega_V+\beta,\qquad
\beta\in\operatorname{Re}H^{2,0}(V),
\]
并满足
\[
|\omega'|^2=2a^2+|\beta|^2,
\qquad
\|\,|\beta|^2-\fint|\beta|^2\,\|_2
\ge c_V\|\beta\|_2^2.
\]
二阶耦合方程的唯一形式方向阻碍正是
\[
Q_0(\beta)=|\beta|^2-\fint|\beta|^2.
\]
颈部通量定理使这个常数在 Kähler ALE 退化中保持正下界。因此形式旋转不能产生独立的小 AKE 分支；剩余问题纯粹位于 Einstein 度量的有限维约化空间。

### 真正缺少的有限维结论

令
\[
\mathcal Z\subset [0,\varepsilon)\times P
\]
为 Einstein 约化方程的零集，第一坐标是 gluing 尺度。若 \(\mathcal Z\) 在 \(t=0\) 的实 blow-up 上是 subanalytic，或更一般地可由有限个幂—对数展开定义，则：

1. 每个积聚到 \(t=0\) 的连通 germ 含有一条趋向 KE 端点的分段 \(C^1\) 曲线；
2. \(\widehat S\) 在 Einstein 集上局部常值；
3. 连续性给出该 germ 上
   \[
   \widehat S=\widehat S(g_V);
   \]
4. 因而任何 AKE 成员满足
   \[
   T_{\rm AK}=D=0,
   \]
   所以它是 Kähler。

这条路线不需要证明所有附近 Einstein 度量都是 Kähler；只需证明 compactified Einstein 零集没有无限个彼此分离、作用量值趋向端点的孤立分支。

### 最便宜的决定性计算

一节点 quintic 模型已经把所需分析压缩到一个正规化 harmonic 缺陷。精确上同调式为
\[
\frac{[\rho_0]}{\zeta_r}
=
-\frac{E}{T}\theta
+\frac{E^2\varepsilon}{2\pi C}c_1 .
\]
最短的实质推进是证明其 harmonic 代表在 Ozuch 的源范数中满足
\[
\frac{\rho_0}{\zeta_r}
\longrightarrow
\frac E2\,\theta_{\rm EH}
\quad\text{in }r_D^{-2}C^\alpha_\beta,
\]
并同时控制 gauge modulation 与 obstruction test tensor 的变化。它会闭合 CSCK secant 与同一个 Einstein 约化图之间的比较，从而得到第一个完整的 KE 轨形邻域刚性定理。

更一般的来源应是 Einstein 锥退化约化映射的 polyhomogeneous gluing 定理，再结合幂—对数函数的 o-minimal 准备定理。若这一层成立，则当 \(T_+(M)>0\) 时，小 torsion 严格 AKE 序列只能进入直径发散或体积分裂几何；有界直径的全部 KE 端点通道都会被关闭。

---

## 复双曲熵—次数入口的定量比较

这里不能直接把实双曲靶的 Besson–Courtois–Gallot sharp 定理用于复双曲靶；还需核对“任意 Riemannian 源到紧致 \(\mathbb{CH}^2\) 靶”的精确秩一版本以及轨形源版本。源度量非 Kähler 也使 Siu 型 harmonic-map 刚性不能直接使用。

更重要的是，即便暂时把理想的熵—体积不等式
\[
h(g)^4\operatorname{Vol}(g)
\ge h(g_X)^4\operatorname{Vol}(g_X)
\]
作为输入，它的常数仍然太弱。归一化
\[
\operatorname{Ric}_g=-3g.
\]
对 \(\mathbb{CH}^2\)，由 holomorphic sectional curvature \(-4\) 模型缩放得到
\[
h(g_X)=2\sqrt2,\qquad
\operatorname{Vol}(X)=\frac{2\pi^2A}{9}.
\]
Bishop 熵上界给出 \(h(g)\le3\)，故至多得到
\[
\operatorname{Vol}(g)\ge\frac{64}{81}\operatorname{Vol}(X),
\qquad
u:=\frac{\int s^2}{32\pi^2}\ge\frac{64}{81}A.
\]
而现有 SW 标量估计已经给出
\[
u\ge A.
\]
因此标准熵输入不会改善硬区间中的 Q1 估计。

真正能改变全局问题的复双曲次数定理必须是 Einstein 特有的，例如对 degree-one harmonic map
\[
f:(V,g)\to(X,g_X)
\]
控制
\[
S_f=f^*g_X-\frac{|df|^2}{4}g
\]
并从 Einstein Bochner 公式推出 \(S_f\equiv0\)，或推出足以与
\[
u\le3(A-k)
\]
冲突的定量体积下界。这样的定理会直接迫使 \(V\) 局部复双曲，从而与 Wahl 点或 blow-up 拓扑不相容。现有实双曲 BCG 常数本身尚未提供这一新 implication。
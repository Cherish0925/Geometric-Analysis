# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step39_actual_harmonic_zero_test_and_route_comparison.md",
    "Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md",
    "Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md",
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md",
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md",
    "Skills/geometric-analysis/references/results-and-questions.md"
  ]
}
```

## Task

Develop a mathematically concrete proof/construction framework for the localized-to-diffuse transition of the actual harmonic-zero configuration described in Step 39. The first target is a pure blow-up tower of compact complex-hyperbolic hosts, outside the inherited linear window. Use one realizable closed metric and its glued harmonic form, not a formal nowhere-zero zero-period field. Give: a precise domain decomposition (host-like bulk, zero/bolt cores, interfaces), candidate quadratic forms or Dirichlet-to-Neumann maps including full metric first jets and harmonic-form flux, the role of cover-uniform CH coercivity and its field-selection caveat, possible collective low modes/compliance scaling with A and k, and a cheapest discriminating calculation or theorem that can tell whether O(k) core cost can become o(k). Keep lower estimates distinct from upper constructions and keep eta/exceptional periods/zero sets separate. Relate any proposed route back to P and the normalized Einstein defect. Do not assume the cap route or density-free O10 is the same problem.

## Output

# 实际调和零点构型的局域—弥散框架

## 1. 几何对象与分解

取紧复双曲曲面
\[
(X_j,g_{\mathrm{CH}},\omega_{\mathrm{CH}}),\qquad
\operatorname{Ric}(g_{\mathrm{CH}})=-g_{\mathrm{CH}},
\]
并记
\[
A_j=K_{X_j}^2,\qquad \operatorname{Vol}(X_j)=2\pi^2A_j.
\]
纯吹起塔的首个清晰参数序列可取
\[
M_j=X_j\# k_j\overline{\mathbb{CP}}^{\,2},\qquad
k_j\to\infty,\qquad h_j=\frac{k_j}{A_j}\to0.
\]
尽管 \(h_j\to0\)，纯吹起情形的 \(\sigma=18\)，因而不落入已有线性定理的参数区间。与此同时
\[
\frac{\chi(M_j)}{A_j}=\frac13+\frac{k_j}{A_j}
\]
仍然有界，因此这里研究的不是 O10。

在每个选定点嵌入 Step 39 的实际垂直单元。每个单元含三个区域：

\[
U_i^{\mathrm{core}}=\{\text{bolt}\le x\le \rho\},\qquad
T_i=\{\rho\le x\le X\},\qquad
Y_i=\{x=X\},
\]
其中 \(\rho\approx5\) 或 \(10\) 已进入 CH 线性尾部，\(Y_i\) 位于完全相同的 CH collar 内。闭流形分解为
\[
M_j=B_j\cup\bigcup_{i=1}^{k_j}(U_i^{\mathrm{core}}\cup T_i),
\]
其中
\[
B_j=X_j\setminus\bigcup_i B_i
\]
连同各外 collar 组成 host-like bulk。内部截面
\[
\Sigma_i=\{x=\rho\}
\]
用来接入透明的 CH 尾部响应；外接口 \(Y_i\) 用来实现精确光滑拼接。

基准对 \((g_0,\Omega_0)\) 具有：

* \(g_0=g_{\mathrm{CH}}\)、\(\Omega_0=\omega_{\mathrm{CH}}\) 于 \(B_j\) 及各外 collar；
* \(d\Omega_0=0\)、\(*_{g_0}\Omega_0=\Omega_0\)，故 \(\Omega_0\) 是真实调和自对偶形式；
* \([\Omega_0]=\pi^*[\omega_{\mathrm{CH}}]\)，所以
  \[
  \int_{E_i}\Omega_0=0,\qquad \eta=1;
  \]
* \(\Omega_0\) 沿每个 bolt 消失，而不是一个无零点、零 exceptional period 的形式；
* 单元体积与被切除 CH 区域体积相等，因此基准闭构造仍有
  \[
  V_0=2\pi^2A_j.
  \]

这个分解保留了非线性核心、线性 CH 尾部和全局 bulk 三种不同尺度，且不会把 Step 29 的 Chern/interface flux 与原始 Ricci 作用量重复相加。

---

## 2. 实际调和形式的耦合线性化

固定 pullback 上同调类。写
\[
g_t=g_0+t h+O(t^2),\qquad
\Omega_t=\Omega_0+t\,da+O(t^2).
\]
由
\[
*_{g_t}\Omega_t=\Omega_t
\]
得到
\[
(da)^-=\frac12\dot *_{h}\Omega_0.
\]
配合规范
\[
d^*a=0,
\]
bulk 上的形式方程是椭圆系统
\[
\boxed{\;
\mathcal S_{\Omega_0}(h,a)
=
\left(d^-a-\frac12\dot *_{h}\Omega_0,\ d^*a\right)=0.
\;}
\]
这个表示从不除以 \(|\Omega_0|\)，所以在 bolt 零点处仍然有意义。固定上同调类还排除了添加全局调和自对偶形式；闭一形式造成的 \(a\)-非唯一性则取商处理。

在接口 \(Y\) 上，自对偶形式的自然数据为
\[
\tau=i^*\Omega\in\Omega^2(Y),\qquad
\beta=\iota_n\Omega\in\Omega^1(Y),
\]
并满足
\[
\tau=*_{Y}\beta.
\]
\(\beta\) 是应保留的调和形式通量。线性化时，\(\dot *_Y\) 与 \(h|_Y\) 同时进入，因此不能只传递标量 \(q=|\Omega|^2\)。对应的 Green 辛形式是
\[
\mathfrak s_Y\bigl((\tau,\beta),(\tau',\beta')\bigr)
=
\int_Y(\tau\wedge\beta'-\tau'\wedge\beta).
\]
这使核心 Calderón 空间与 bulk Calderón 空间可以直接匹配。

对度量，在 Bianchi–York 规范和固定总体尺度后，以
\[
\gamma_g h=\bigl(h|_Y,\nabla_nh|_Y\bigr)
\]
作为完整一阶接口数据。这里应保留所有切向、混合和法向分量；只传递诱导三维度量会漏掉 Ricci 作用量所需的二阶信息。

因此每个接口的状态向量可写成
\[
z_i=
\left(
h|_{Y_i},\nabla_nh|_{Y_i};
a_T|_{Y_i}\bmod d_YC^\infty,\,
\beta_i
\right),
\]
另附 exceptional periods 和可能的 host 上同调漂移系数。固定 pullback 分支中这些附加系数分别为 \(0\) 和 \(0\)。

---

## 3. Ricci 二次型与 DtN 算子

令
\[
P(g)=\int_M|\operatorname{Ric}^\circ_g|^2\,d\mu_g.
\]
在 CH bulk 上，若 \(h=h_{\mathrm{TT}}+2fg\)，则二次主部为
\[
Q_{\mathrm{CH}}(h)
=
\frac14\int|L_Eh_{\mathrm{TT}}|^2
+
4\int|(\nabla^2f)^\circ|^2.
\]
TT 与 conformal 通道在 CH 背景上正交。Step 44 的点态 Bochner 间隙给出统一于有限覆盖的估计
\[
Q_{\mathrm{CH}}(h)\ge
\kappa\left(
\|h_{\mathrm{TT}}\|_{H^2}^2+\|df\|_{H^1}^2
\right).
\]

因为 \(Q_{\mathrm{CH}}\) 的 Euler 算子是四阶算子
\[
\mathcal A^*\mathcal A,\qquad
\mathcal A=D\operatorname{Ric}^\circ,
\]
Green 公式产生两组 metric momenta：
\[
Q_{\mathrm{CH}}(h,v)
=
\int_B\langle\mathcal A^*\mathcal A h,v\rangle
+\sum_i
\left[
\langle\pi_0(h),v|_{Y_i}\rangle
+
\langle\pi_1(h),\nabla_nv|_{Y_i}\rangle
\right].
\]
由此定义 bulk 的度量 DtN 算子
\[
\Lambda_B^g:
(h|_Y,\nabla_nh|_Y)\longmapsto(\pi_0,\pi_1).
\]

将调和形式约束 \(\mathcal S_{\Omega_0}(h,a)=0\) 一并消元，得到真正相关的耦合算子
\[
\Lambda_B^{\mathrm{eff}}
=
\begin{pmatrix}
\Lambda_{gg}&\Lambda_{g\Omega}\\
\Lambda_{\Omega g}&\Lambda_{\Omega\Omega}
\end{pmatrix},
\]
或等价地，对固定 periods 取 Schur 补
\[
\Lambda_{g,\mathrm{fixed\ class}}
=
\Lambda_{gg}
-\Lambda_{g\Omega}\Lambda_{\Omega\Omega}^{\dagger}\Lambda_{\Omega g}.
\]
这里的伪逆只作用在除去规范核和固定上同调类之后的空间。这个算子同时记录 metric first jet、调和通量及 Hodge 投影的非局域响应。

核心端定义非线性相对作用量
\[
\mathfrak C_i(z_i)
=
\inf\left\{
P(g;U_i):
\begin{array}{l}
(g,\Omega)\text{ 光滑延伸至 bolt},\\
d\Omega=0,\ *\Omega=\Omega,\\
\int_{E_i}\Omega=0,\\
\gamma(g,\Omega)=z_i
\end{array}
\right\}.
\]
在实际单元附近，
\[
\mathfrak C_i(z_i)
=
P_{\mathrm{core}}
+2\langle f_{\mathrm{core}},z_i-z_i^0\rangle
+\langle z_i-z_i^0,\Lambda_C(z_i-z_i^0)\rangle
+O(\|z_i-z_i^0\|^3).
\]
于是闭构造的二次近似为
\[
P(g_0+h)
=
kP_{\mathrm{core}}
+2\langle f,z\rangle
+\langle z,(\Lambda_C^{\oplus k}+\Lambda_B^{\mathrm{eff}})z\rangle
+Q_\perp+O(\|z\|^3).
\]
若记
\[
\mathcal K_{j,k}=\Lambda_C^{\oplus k}+\Lambda_B^{\mathrm{eff}},
\]
则局部优化给出
\[
P_{\min}^{(2)}
=
kP_{\mathrm{core}}
-\langle f,\mathcal K_{j,k}^{\dagger}f\rangle.
\]
因此真正区分局域与集体响应的量不是某个单独尾部积分，而是
\[
\boxed{\quad
\mathfrak C_{j,k}
=
\langle f,\mathcal K_{j,k}^{\dagger}f\rangle.
\quad}
\]

### 已知径向块作为实现校准

在反对称 CH 尾部，
\[
z^-=(w_0,\Theta),\qquad
E_{\mathrm{ext}}=
\frac{\delta^2}{I(\rho)},
\]
\[
\delta=-2K(\rho)\Theta-w_0G(\rho),\qquad
K(\rho)=\left(\frac{\rho}{1+\rho}\right)^2.
\]
\(\delta=0\) 是 Einstein mass 零模。任何数值或解析 DtN 实现都必须精确复现这个核。

若改用 AK 分解，则应同时加入 Step 29 的
\[
B=b_+-3\mathcal F-9\mathcal P^2-6Wuu'
\]
接口转换。原始 \(E_{\mathrm{ext}}\) 与 AK 尾部积分不能同时作为两个正项使用。定理级 profile 在 \(x=10\) 后的原始尾部仅约
\[
1.15\times10^{-4}\,(8\pi^2),
\]
而单元总作用量约为 \(0.99567(8\pi^2)\)。因此只重调远尾或 mass 零模至多改变很小部分；若出现 \(o(k)\)，它必须重构核心或形成 host 尺度的新分支。

---

## 4. CH 强制性与场分支选择问题

对去掉若干核心后的 bulk，截断论证给出应有的局部形式
\[
Q_{\mathrm{CH}}(h;B_j)
\ge
\kappa\|h\|_{H^2(B_j') }^2
-
C\sum_i\|\gamma_gh\|_{\mathcal T(Y_i)}^2,
\]
其中 \(B_j'\) 与接口保持固定距离，常数仅依赖 CH 模型及注入半径下限。接口项不是误差垃圾；它正是 \(\Lambda_B^g\) 所吸收的量。

对于相距趋于无穷的核心，局域 Green 响应具有：

* 每个紧支撑接口源的 \(L^2\) 大小为 \(O(1)\)；
* \(k\) 个互不相交源的总 \(L^2\) 平方为 \(O(k)\)；
* CH Einstein 算子的覆盖统一间隙排除了随 \(A\) 增长的光滑 metric compliance；
* 若 Green 核的远距和可积，则异地相互作用为 \(o(k)\)。

一个振幅为 \(t\) 的真正 host 尺度 metric 模式具有 bulk 刚度
\[
Q_{\mathrm{bulk}}\sim A\,t^2,
\]
而 \(k\) 个核心与它的线性耦合为 \(k t\)。优化后只能产生
\[
\Delta P_{\mathrm{coh}}\sim-\frac{k^2}{A}.
\]
当 \(k=o(A)\) 时，这不足以改变一个严格正的单核心线性系数。它可以解释次阶 collective correction，却不能由小扰动把 \(ck\) 自动变成 \(o(k)\)。

这一结论只适用于 metric 和固定 actual-form 分支。若用 Seiberg–Witten 场建立所有度量上的下界，则还需区分 canonical bulk branch 与 depletion/vortex branch。Step 44 的覆盖统一结论作用于整个闭 CH 主体的绝对 \(H^2\) 邻域；当前 \(k\)-核心构造的总体 \(H^2\) 大小约为 \(\sqrt{k}\)，并不属于该邻域。所需局部场估计应具有
\[
R(B_j')
\le
C\,P(B_j)
+
C\sum_i\|\xi_i\|_{\mathrm{field},Y_i}^2
+
C\,\mathfrak V(B_j),
\]
其中 \(\xi_i\) 是 monopole 的接口 Cauchy 数据，\(\mathfrak V\) 明确计量其偏离 canonical branch 的 amplitude depletion 和相位旋转。若不保留 \(\mathfrak V\)，bulk metric 接近 CH 并不能推出场接近 canonical 解。

上界构造不需要这一选择：拼接的 \(\Omega\) 本身就是闭、光滑、调和且自对偶的真实形式。但它也不能自动当作 monopole bilinear 使用。

---

## 5. 可能的集体低模及其尺度

### 5.1 局域 CH 尾部模

这些模由单核心 DtN 吸收，代价为 \(O(k)\)。已知 mass 零模只消去特定尾部组合
\[
-2K(\rho)\Theta-w_0G(\rho),
\]
不消去 bolt 的 marked charge 或核心 Ricci 作用量。

### 5.2 host 尺度的 metric 模

如上所述，CH 间隙给出 \(A t^2\) 刚度和 \(k t\) 耦合，因此只产生 \(k^2/A\) 修正。若一个计算显示 compliance 随 \(A\) 线性增长，则必有未除去的规范模、尺度模、上同调漂移，或接口源正好投影到另一个零模。

### 5.3 Hodge 正子空间漂移

若允许
\[
[\Omega]=\pi^*[\omega_{\mathrm{CH}}]+\xi,\qquad
\xi\in H^+(X_j),
\]
则 \(\xi\) 是 bulk 的真正全局低模。它不由 \(d\Omega=0\) 的局部能量定价，并可能使 \(\eta\) 从 \(1\) 降低。此时应把 \(\xi\) 作为独立有限维变量加入 DtN 系统，并显式计算 period Gram matrix。由此产生的低代价属于 period-angle 漂移，不属于固定 pullback 类中的零点扩散。

### 5.4 exceptional periods

若
\[
e_i=\int_{E_i}\Omega\ne0,
\]
则进入正面积、aligned sphere 和 \(s^*>0\) pocket 路线。相应核心作用量应写成
\[
\mathfrak C_i(z_i;e_i),
\]
而不是把 \(e_i\to0\) 与 \(e_i=0\) 混同。固定实际 harmonic-zero 分支始终取 \(e_i=0\)。

### 5.5 零集的集体重组

\(e_i=0\) 保证无处为零的 symplectic 形式不可能存在，但不保证每个 \(E_i\) 都对应不同的零集分支。一个零集分量可能同时服务多个 exceptional classes。更一般的扰动还可把 bolt 上二维零集裂解成 near-symplectic 型低维零集。

因此需要记录三项彼此独立的数据：
\[
\eta,\qquad (e_1,\dots,e_k),\qquad
Z(\Omega)\ \text{及其 vanishing order}.
\]
仅凭零集分量数不能得到每吹起常数代价。薄零管的单纯一阶 Dirichlet 能甚至可呈临界容量行为；真正可能保留 \(O(1)\) 代价的是闭性、自对偶性、harmonic flux、metric 二阶响应和 Chern/interface charge 的联合系统。

### 5.6 弥散 common mode

若存在一条远离 CH 小邻域的实际分支，使总旋转量
\[
R\sim k
\]
分布在体积 \(A\) 上，并且 \(\operatorname{Ric}^\circ\) 只在旋转的一阶项消去后以二次量出现，则量纲上
\[
|\operatorname{Ric}^\circ|\sim \frac{k}{A},\qquad
P\sim A\left(\frac{k}{A}\right)^2=\frac{k^2}{A}.
\]
这正是弥散二次尺度。它要求同时实现：

\[
d\Omega=0,\quad *\Omega=\Omega,\quad
[\Omega]=\pi^*[\omega_{\mathrm{CH}}],\quad
\int_{E_i}\Omega=0,
\]
以及核心 metric charge 的消散。只在固定 Einstein host 上缓慢旋转一个形式并不满足这些条件。

---

## 6. 多核心相对作用量：局域—弥散转变的精确对象

令 \(\mathcal A_m(R)\) 为以下实际 pair 的集合：

* 底层是一个 CH 球内的 \(m\) 点吹起，exceptional intersection form 为 \(-I_m\)；
* 在外 collar 上
  \[
  g=g_{\mathrm{CH}},\qquad \Omega=\omega_{\mathrm{CH}};
  \]
* 在内部
  \[
  d\Omega=0,\qquad *_{g}\Omega=\Omega,\qquad
  \int_{E_i}\Omega=0;
  \]
* \(g,\Omega\) 在 bolts 和零集处均光滑。

定义两个相对 tariff：
\[
T_m^P
=
\inf_{R>0}\inf_{(g,\Omega)\in\mathcal A_m(R)}
\int|\operatorname{Ric}^\circ|^2,
\]
\[
T_m^{\mathcal R}
=
\inf_{R>0}\inf_{(g,\Omega)\in\mathcal A_m(R)}
\int|\operatorname{Ric}+g|^2.
\]
第二个量满足
\[
\mathcal R(g)
=
P(g)+\frac14\int(s+4)^2,
\]
所以更直接服务于归一化 Einstein defect 的上构造。再定义
\[
\tau_\infty^P=\inf_{m\ge1}\frac{T_m^P}{m},
\qquad
\tau_\infty^{\mathcal R}=\inf_{m\ge1}\frac{T_m^{\mathcal R}}{m}.
\]

这两个数把问题分成两个数学上明确的方向。

### 下界定理的目标形状

若能证明统一 marked-cluster 估计
\[
T_m^P\ge c\,m\qquad\text{对所有 }m,
\]
并将 CH bulk DtN 与各 cluster 的 full first jet、harmonic flux 精确匹配，则稀疏塔上应得到
\[
P(g)\ge
\tau_\infty^P k
-C\frac{k^2}{A}
-o(k).
\]
因 \(k=o(A)\)，若 \(\tau_\infty^P>0\)，则
\[
P(g)\ge c'k.
\]
对固定 pullback actual-form 分支，这正是“核心作用量不能弥散掉”的定量表述。若要推广到所有度量，还需加入上一节的 monopole field-selection/depletion 项。

### 上构造的精确形式

若存在
\[
m_\nu\to\infty,\qquad
\frac{T_{m_\nu}^{\mathcal R}}{m_\nu}\to0,
\]
则每个近极小 cluster 在外 collar 上与 CH pair 完全一致，可以直接嵌入具有足够大嵌入球的复双曲有限覆盖。取互不相交的 clusters 后，
\[
\mathcal R(g_{\mathrm{closed}})
=
\sum_\alpha T_{m_\alpha}^{\mathcal R},
\]
而拼接后的 \(\Omega\) 仍然是实际闭、光滑、自对偶调和形式。于是
\[
\mathcal R=o(k),\qquad P=o(k).
\]
这是从 \(O(k)\) 到 \(o(k)\) 的真实闭构造，不依赖形式上的无零点零周期场。

若只有 \(T_m^P/m\to0\)，还需同时控制
\[
\int(s+4)^2=o(m)
\]
或给出覆盖统一的 conformal scalar repair；否则 \(P\) 的小量尚未转化成 \(\mathcal R\) 的小量。

---

## 7. 成本最低而区分力最强的计算

最便宜的计算不是再扩大固定 cap shell 基，而是计算实际单元的**耦合接口 Hessian**。

### 7.1 单核心 full-trace Hessian

在 \(\Sigma=\{x=\rho\}\) 选取：

1. metric 的全部低阶 \(SU(2)\) 表示，包括已知反对称径向通道和产生 weight-four 相互作用的最低非径向通道；
2. harmonic potential \(a_T\) 及通量 \(\beta\) 的对应表示；
3. 固定 exceptional period、固定 pullback class。

数值对象是
\[
\mathcal K_\ell
=
\Lambda_{C,\ell}
+
\Lambda_{\mathrm{CH},\ell}^{\mathrm{eff}}
\]
以及核心 load \(f_\ell\)。高角频块由四阶椭圆主符号提供正增长，只需精确处理有限多个低模。径向块必须复现
\[
E_{\mathrm{ext}}=\delta^2/I
\]
和 mass 零模；AK 表示必须复现 Step 29 的 \(B\)-flux 转换。

相应的局域优化系数为
\[
e_{\mathrm{loc}}
=
P_{\mathrm{cell}}
-\sum_{\ell\le\ell_0}
\langle f_\ell,\mathcal K_\ell^\dagger f_\ell\rangle.
\]
若区间算术给出
\[
e_{\mathrm{loc}}>0
\]
且所有非规范低模远离零，则实际单元附近没有通往 \(o(k)\) 的小振幅分支。若某块出现趋零特征值，其特征向量直接给出应延拓的 metric/form diffuse ansatz。

### 7.2 多点 Green 矩阵

对放置点 \(p_i\) 计算
\[
\mathcal K_{ij}
=
\delta_{ij}\Lambda_C+
G_{\mathrm{CH}}(p_i,p_j),
\]
其中 \(G_{\mathrm{CH}}\) 是耦合 Einstein–Hodge 接口 Green 核。观察两个量：
\[
\lambda_{\min}(\mathcal K),\qquad
\langle f,\mathcal K^\dagger f\rangle.
\]
在稀疏放置中：

* 若异地块和为 \(o(k)\)，则每核心系数趋向 \(e_{\mathrm{loc}}\)；
* 若 coherent block 的刚度为 \(A\)，则只产生 \(k^2/A\) 修正；
* 若 compliance 显著快于 \(k\) 增长，则其特征向量会指出 Hodge drift、field depletion 或新的非线性 collective mode。

所需外部来源族很明确：\(SU(2,1)\) 齐性算子的球函数 Green 核、四阶 Einstein Hessian 的 Calderón 投影，以及 \(d^-\oplus d^*\) 的接口投影。Step 44 的 Lemma M 是其中 spinorial 块的对应问题。

### 7.3 最终决定性的定理对象

单核心 Hessian只能区分实际单元附近的分支。能够彻底区分 \(O(k)\) 与 \(o(k)\) 的对象是
\[
\tau_\infty^P
\quad\text{或}\quad
\tau_\infty^{\mathcal R}.
\]
证明 \(\tau_\infty^P>0\) 给出多核心线性 tariff；构造 \(T_m^{\mathcal R}=o(m)\) 给出实际闭弥散序列。二者都允许核心改变 bolt 面积、零集几何和完整 jets，因此不会把固定 cap 家族的数值性质误当成全体构型的性质。

---

## 8. 与 \(P\) 和归一化 Einstein defect 的换算

在 \(\operatorname{Ric}=-g\) 标度下，
\[
\mathcal R(g)=\int|\operatorname{Ric}+g|^2
=
P(g)+\frac14\int(s+4)^2.
\]
基准 volume-pinned 构造满足 \(V=2\pi^2A\)，故
\[
\frac{\mathcal R(g)}{V}
=
4\,\frac{\mathcal R(g)/(8\pi^2)}{A}.
\]
特别地，在 \(s=-4\) 代表上，
\[
\frac{\mathcal R}{V}
=
\frac{P}{V}
=
4\,\frac{P/(8\pi^2)}{A}.
\]
因此：

\[
P=\Theta(k)
\quad\Longrightarrow\quad
\mathscr D=\Theta(k/A),
\]
而
\[
P=O(k^2/A)
\quad\Longrightarrow\quad
\mathscr D=O(k^2/A^2),
\]
前提是 scalar 通道也处于相同尺度。Step 39 的
\[
4.08167\,(2\pi^2)
\]
每单元数值是含 Weyl-model 与 amplitude 项的 augmented branch defect；它说明当前实际 harmonic-zero 对位于线性 surgery-density 尺度，但既不是 \(P\) 的下界，也不是弥散上构造。

最后，\(\eta\)、exceptional periods 与零集应始终分别记录。固定 pullback 分支有
\[
\eta=1,\qquad e_i=0,
\]
其低代价若存在，只能来自零集和 metric/form 的集体重组。允许 \(\eta\) 漂移或 \(e_i>0\) 会进入不同的 Hodge 或 aligned-pocket 机制。固定 cap 优化只探索某个核心子族；O10 又要求 \(\chi/A\to\infty\)。这两者都不等同于上述纯吹起塔的 localized-to-diffuse tariff。
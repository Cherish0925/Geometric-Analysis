# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 39,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step39_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step39_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop a mathematically concrete proof/construction framework for the localized-to-diffuse transition of the actual harmonic-zero configuration described in Step 39. The first target is a pure blow-up tower of compact complex-hyperbolic hosts, outside the inherited linear window. Use one realizable closed metric and its glued harmonic form, not a formal nowhere-zero zero-period field. Give: a precise domain decomposition (host-like bulk, zero/bolt cores, interfaces), candidate quadratic forms or Dirichlet-to-Neumann maps including full metric first jets and harmonic-form flux, the role of cover-uniform CH coercivity and its field-selection caveat, possible collective low modes/compliance scaling with A and k, and a cheapest discriminating calculation or theorem that can tell whether O(k) core cost can become o(k). Keep lower estimates distinct from upper constructions and keep eta/exceptional periods/zero sets separate. Relate any proposed route back to P and the normalized Einstein defect. Do not assume the cap route or density-free O10 is the same problem.

## Integrated Scientific Memo

# 实际 harmonic-zero 构型的局域—弥散框架

## 1. 首个测试族与必须固定的对象

取紧复双曲覆盖塔
\[
(X_j,g_{\rm CH},\omega_{\rm CH}),\qquad \Ric(g_{\rm CH})=-g_{\rm CH},
\]
并令
\[
A_j=K_{X_j}^2,\qquad \Vol(X_j)=2\pi^2A_j,\qquad
M_j=X_j\#k_j\overline{\CP}^{\,2}.
\]
最干净的稀疏极限是
\[
k_j\to\infty,\qquad h_j:=k_j/A_j\to0.
\]
纯吹起有 \(Q=k,\ r=0,\theta=1,\sigma=18\)，故不受现有 \(\sigma<4+c_0\) 线性窗口约束；但
\[
\chi(M_j)/A_j=1/3+k_j/A_j
\]
仍有界，因此这不是 density-free O10。

基准必须是 Step 39 的真实闭 pair \((g_0,\Omega_0)\)，而非形式上的 nowhere-zero、零 exceptional-period 场：

\[
d\Omega_0=0,\qquad *_{{g_0}}\Omega_0=\Omega_0,\qquad
[\Omega_0]=\pi^*[\omega_{\rm CH}],
\]
\[
\int_{E_i}\Omega_0=0,\qquad \eta=1,
\]
且 \(\Omega_0\) 沿每个 bolt 消失。它在精确 CH collar 和 untouched host 上等于 \(\omega_{\rm CH}\)，因而闭合拼接后仍是光滑调和自对偶形式。

这里始终应分别记录：

\[
\boxed{\eta,\qquad e_i:=\int_{E_i}\Omega,\qquad Z(\Omega)}
\]

而不能互相替代。固定 pullback harmonic-zero 分支是
\[
\eta=1,\qquad e_i=0,\qquad Z(\Omega)\neq\varnothing.
\]
若允许 \(\eta\) 漂移，就是 host 正上同调方向的 escape；若 \(e_i>0\)，则进入 aligned exceptional-area/\(s^*>0\) pocket 路线，不再是当前 perpendicular zero-period 问题。

---

## 2. 精确区域分解

在每个吹起点选两个截面：

* \(\Sigma_i=\{x=\rho\}\)，其中 \(\rho\approx5\) 或 \(10\)，已进入可线性化的 CH 尾部；
* \(Y_i=\{x=X\}\)，位于 metric 和 form 都已精确等于 CH/Kähler 数据的 collar。

定义

\[
C_i=\{\text{bolt}\le x\le \rho\}
\]
为完整 zero/bolt core，

\[
T_i=\{\rho\le x\le X\}
\]
为接口尾部，

\[
B_j=M_j\setminus\bigcup_i(C_i\cup T_i)
\]
为 host-like bulk。于是
\[
M_j=B_j\cup\bigcup_{i=1}^{k_j}(T_i\cup C_i).
\]

这一区分有两个作用。

1. \(C_i\) 保留 bolt 光滑性、零点消失阶、marked topology 和全部非线性核心作用。
2. \(T_i\) 可由 Step 19 的精确 CH response 替代，但不能同时再把 Step 29 的 AK 尾积分当作第二个正代价。

特别是，在反对称径向通道
\[
E_{\rm ext}(\rho;w_0,\Theta)
=\frac{\delta^2}{I(\rho)},\qquad
\delta=-2K(\rho)\Theta-w_0G(\rho),
\]
其中
\[
K(\rho)=\left(\frac{\rho}{1+\rho}\right)^2.
\]
\(\delta=0\) 是 Einstein mass null line。若改用 AK 表示，必须加入
\[
B=b_+-3\mathcal F-9\mathcal P^2-6Wuu'
\]
的边界转换；raw \(E_{\rm ext}\) 与 AK tail 不可重复计价。定理级 profile 在 \(x=10\) 后的 raw tail 仅约
\[
1.146\times10^{-4}(8\pi^2),
\]
远小于总单元作用量约 \(0.99567(8\pi^2)\)。因此只利用远尾 mass mode 不可能把整个 \(O(k)\) 核心成本变成 \(o(k)\)。

---

## 3. 接口变量：metric full first jet 与 harmonic flux

### 3.1 度量数据

对四阶 Hessian functional \(P=\int|\Ric^\circ|^2\)，接口不能只传递诱导三维度量。Bianchi–York 规范并固定整体尺度后，应保留
\[
\gamma_g h=\bigl(h|_\Sigma,\nabla_nh|_\Sigma\bigr),
\]
等价地保留诱导度量与第二基本形式的全部线性化，包括切向、混合和法向分量。

若
\[
\mathcal A=D\Ric^\circ_{g_{\rm CH}},
\]
则 CH bulk 的二次型可写为
\[
Q_{\rm CH}(h)=\|\mathcal Ah\|_{L^2(B)}^2.
\]
其 Green 公式产生两个共轭 momenta：
\[
Q_{\rm CH}(h,v)
=
\int_B\langle\mathcal A^*\mathcal Ah,v\rangle
+\int_{\partial B}
\bigl[
\langle\pi_0(h),v\rangle+
\langle\pi_1(h),\nabla_nv\rangle
\bigr].
\]
因此 metric DtN 是
\[
\Lambda_B^g:
(h|_\Sigma,\nabla_nh|_\Sigma)\mapsto(\pi_0,\pi_1).
\]

### 3.2 调和形式数据

固定 pullback 上同调类，写
\[
g_t=g_0+th+O(t^2),\qquad
\Omega_t=\Omega_0+t\,da+O(t^2).
\]
自对偶条件的线性化是
\[
(da)^-=\frac12\dot *_{h}\Omega_0,
\]
配以
\[
d^*a=0.
\]
故自然耦合系统为
\[
\boxed{
\mathcal S_{\Omega_0}(h,a)=
\left(d^-a-\frac12\dot *_{h}\Omega_0,\ d^*a\right)=0.
}
\]
它不除以 \(|\Omega_0|\)，所以穿过 bolt 零点仍然正则；这是使用真实 harmonic-zero pair 的关键优点。

在三维接口 \(Y\) 上设
\[
\tau=i^*\Omega,\qquad \beta=\iota_n\Omega.
\]
自对偶性给出
\[
\tau=*_{Y}\beta.
\]
\(\beta\) 是必须保留的 harmonic flux；线性化时 \(\dot *_Y\) 又与 metric first jet 耦合。相应边界辛形式为
\[
\mathfrak s_Y((\tau,\beta),(\tau',\beta'))
=
\int_Y(\tau\wedge\beta'-\tau'\wedge\beta).
\]
因此只传递 \(q=|\Omega|^2\)、或只传递一个径向 amplitude，是不充分的。

一个完整接口状态可取
\[
z_i=
\left(
h|_{\Sigma_i},\nabla_nh|_{\Sigma_i};
a_T|_{\Sigma_i}\bmod d_{\Sigma_i}C^\infty,\,
\beta_i
\right),
\]
并另列全局正调和方向及 exceptional periods。固定目标分支把这些附加量约束为
\[
[\Omega]=\pi^*[\omega_{\rm CH}],\qquad e_i=0.
\]

---

## 4. 耦合 DtN 与相对核心作用量

在消去 bulk 内部变量并固定 cohomology 后，得到耦合 Calderón/DtN 算子
\[
\Lambda_B^{\rm eff}
=
\begin{pmatrix}
\Lambda_{gg}&\Lambda_{g\Omega}\\
\Lambda_{\Omega g}&\Lambda_{\Omega\Omega}
\end{pmatrix}.
\]
若先消去 form 变量，则 metric 的有效算子是 Schur 补
\[
\Lambda_{g,\mathrm{fixed\ class}}
=
\Lambda_{gg}
-\Lambda_{g\Omega}\Lambda_{\Omega\Omega}^{\dagger}
 \Lambda_{\Omega g},
\]
其中伪逆仅在除去 gauge kernel 和固定上同调核后使用。

每个核心定义真实非线性相对作用量
\[
\mathfrak C_i(z_i)=
\inf\left\{
\int_{C_i}|\Ric^\circ_g|^2:
\begin{array}{l}
(g,\Omega)\text{ 光滑延伸至 bolt},\\
d\Omega=0,\quad *_g\Omega=\Omega,\\
\int_{E_i}\Omega=0,\\
\gamma(g,\Omega)=z_i
\end{array}
\right\}.
\]
在 Step 39 单元附近，
\[
\mathfrak C_i(z_i)
=
P_{\rm core}
+2\langle f_i,z_i-z_i^0\rangle
+\langle z_i-z_i^0,\Lambda_C(z_i-z_i^0)\rangle
+O(\|z_i-z_i^0\|^3).
\]

于是多核心二次问题为
\[
P
=
kP_{\rm core}
+2\langle f,z\rangle
+\langle z,\mathcal K_{j,k}z\rangle
+Q_\perp+O(\|z\|^3),
\]
其中
\[
\mathcal K_{j,k}
=
\Lambda_C^{\oplus k}+\Lambda_B^{\rm eff}.
\]
局部优化给出
\[
P_{\min}^{(2)}
=
kP_{\rm core}
-\langle f,\mathcal K_{j,k}^{\dagger}f\rangle.
\]
因此局域—弥散转变的准确 compliance 是
\[
\boxed{
\mathfrak C_{j,k}
=\langle f,\mathcal K_{j,k}^{\dagger}f\rangle,
}
\]
而不是某个孤立 tail integral，也不是形式上的 torsion common mode。

任何实现都必须通过两个校准：

1. 在径向反对称块精确复现 \(E_{\rm ext}=\delta^2/I\) 及 mass null line；
2. 在 AK 表示中精确复现 Step 29 的 \(B\)-flux 转换，不能给 Einstein mass mode 虚构正成本。

---

## 5. 覆盖一致 CH 强制性及其边界

在 CH bulk 上，写
\[
h=h_{\rm TT}+2fg.
\]
二次主部为
\[
Q_{\rm CH}(h)
=
\frac14\|L_Eh_{\rm TT}\|_2^2
+4\|(\nabla^2f)^\circ\|_2^2,
\]
且两个通道在背景上正交。Step 44 给出沿有限覆盖塔一致的估计
\[
Q_{\rm CH}(h)
\ge
\kappa\left(
\|h_{\rm TT}\|_{H^2}^2+\|df\|_{H^1}^2
\right).
\]
一致性来自 CH 曲率的点态 Bochner potential 和固定注入半径下限，而不是可能沿塔退化的普通谱隙。

局部化后的正确形状是
\[
Q_{\rm CH}(h;B_j)
\ge
\kappa\|h\|_{H^2(B_j')}^2
-C\sum_i\|\gamma_gh\|_{\mathcal T(\Sigma_i)}^2.
\]
负的 boundary term 不是可丢弃误差；它恰由 coupled DtN 与核心 response 吸收。

### 场选择 caveat

上述 metric coercivity 不自动给出 monopole field 的 canonical selection。Step 44 的 \(R\le CP\) 只对：

* 完整 CH quotient 的绝对全局 \(H^2\) 小邻域；
* canonical Seiberg–Witten branch

成立。含 \(k\) 个 unit cores 的总 \(H^2\) 距离通常为 \(O(\sqrt{k})\)，并不在该邻域。

即使 bulk metric 局部接近 CH，实际 monopole 仍可在 bulk 发生 amplitude depletion/vortex，因而正确的局部估计必须是
\[
R(B_j')
\le
C\,P(B_j)
+C\sum_i\|\xi_i\|_{\rm field,\Sigma_i}^2
+C\,\mathfrak V(B_j),
\]
其中 \(\xi_i\) 为场的接口 Cauchy 数据，\(\mathfrak V\) 明确计量偏离 canonical branch 的 depletion、phase 和 Lee/Nijenhuis 成分。没有 \(\mathfrak V\) 的 localized selection 尚未证明。

这一区分只影响“所有度量”的下界。上界构造可直接使用 glued \(\Omega\)，因为它已经是实际闭、光滑、调和、自对偶形式；但不能把它无条件认作 monopole bilinear。

---

## 6. 集体低模及 \(A,k\) 标度

### 6.1 局部 tail 与 mass mode

每个核心的 CH tail 模由单核 DtN 定价。mass null direction 只消去
\[
-2K(\rho)\Theta-w_0G(\rho)
\]
这一特定组合，不消去 bolt marked charge 或整个 core action。已知 tail 只占当前单元成本的极小部分，所以它至多产生小系数修正。

### 6.2 host 尺度 metric mode

若一个全局模式的幅度为 \(t\)，覆盖一致 CH coercivity 给出
\[
P_{\rm bulk}\sim A\,t^2.
\]
若每个核心与之线性耦合 \(O(t)\)，总耦合为
\[
-k\,\lambda t.
\]
优化后
\[
t_{\rm opt}\sim k/A,\qquad
\Delta P_{\rm collective}\sim-\frac{k^2}{A}.
\]
故当 \(k=o(A)\) 时，任何仍在 perturbative CH 分支内的 collective mode 只能给次阶修正，不能把严格正的 \(ck\) 变成 \(o(k)\)。

不能据此声称任意点源相互作用必为指数小，或写出未经计算的阈值距离：四阶张量 Green 核及相关 \(L^1\) resolvent 尚未完整求出，Step 44 的 Lemma M 正是相应未决问题。安全结论仅是整体 coercive mode 的 \(A t^2\) 刚度及由此产生的 \(k^2/A\) compliance 标度。

### 6.3 Hodge 正方向

若允许
\[
[\Omega]=\pi^*[\omega_{\rm CH}]+\xi,\qquad \xi\in H^+(X_j),
\]
则 \(\xi\) 是不由局部 \(d^-\oplus d^*\) 能量定价的全局有限维低模，并可改变 \(\eta\)。它必须作为独立变量连同 period Gram matrix 加入系统。由此产生的低成本属于 period-angle drift，不是固定 pullback harmonic-zero 的扩散。

### 6.4 真正非微扰 diffuse mode

若存在远离 CH 小邻域的闭 pair，使总旋转/重排量 \(R\sim k\) 分散于体积 \(A\)，而一阶 Ricci 响应被抵消，则量纲允许
\[
|\Ric^\circ|\sim k/A,\qquad
P\sim k^2/A.
\]
这正是 Cotton/Cauchy–Schwarz 路线可能给出的二次尺度。但它要求同时解决：

\[
d\Omega=0,\quad *_g\Omega=\Omega,\quad
[\Omega]=\pi^*[\omega_{\rm CH}],\quad
e_i=0,
\]
以及零集与完整核心 charge 的重组。仅在固定 Einstein host 上“缓慢旋转方向”不是构造。

---

## 7. 零集不能单独提供现成线性下界

Taubes period 论证只给出：若某个 \(e_i=0\)，则 self-dual harmonic form 不能处处非零。它没有给出：

* 每个 exceptional class 对应一个不同零集分量；
* \(Z(\Omega)\) 的面积 \(\gtrsim k\)；
* \(\int|\nabla\Omega|^2\gtrsim k\)；
* 零集是通常 near-symplectic 的二维曲面。

事实上，四维横截 near-symplectic self-dual harmonic form 的一般零集通常是一维，而当前对称单元的 bolt 是非泛型二维零面。因此“codimension-two vortex logarithmic energy”及“每个 \(E_i\) 强制一个面积单位”的说法没有来源支持，不能作为下界框架。

零集路线若要成立，必须证明一个真正的 relative theorem，例如：在固定 bounded-geometry/flux 假设下，完整 harmonic Calderón 数据与 \(k\) 个 null periods 强制某个可加的 zero-set/Chern charge。不能只用零集分量数或面积猜测；薄零管可能具有退化容量，而一个零集分量也可能服务多个 exceptional constraints。

---

## 8. 决定 \(O(k)\) 能否降为 \(o(k)\) 的非线性对象

单核心 Hessian只能排除 Step 39 单元附近的小振幅逃逸。完整问题应由多核心相对 tariff 表述。

令 \(\mathcal A_m(R)\) 为一个 CH 球内 \(m\) 点吹起上的 pair 集合，满足：

\[
(g,\Omega)=(g_{\rm CH},\omega_{\rm CH})
\quad\text{于外 collar},
\]
\[
d\Omega=0,\qquad *_g\Omega=\Omega,\qquad
\int_{E_i}\Omega=0,
\]
并在全部 bolts 和零集处光滑。定义
\[
T_m^P
=
\inf_{R>0}\inf_{(g,\Omega)\in\mathcal A_m(R)}
\int|\Ric^\circ_g|^2,
\]
以及
\[
T_m^{\mathcal R}
=
\inf_{R>0}\inf_{(g,\Omega)\in\mathcal A_m(R)}
\int|\Ric_g+g|^2.
\]
在 \(\Ric=-g\) 归一化下，
\[
\mathcal R(g):=\int|\Ric+g|^2
=
P(g)+\frac14\int(s+4)^2.
\]

定义渐近每点 tariff
\[
\tau_\infty^P=\inf_{m\ge1}\frac{T_m^P}{m},
\qquad
\tau_\infty^{\mathcal R}
=\inf_{m\ge1}\frac{T_m^{\mathcal R}}m.
\]

这给出清楚的两侧判据。

### 下界侧

若证明
\[
T_m^P\ge c\,m\qquad\forall m,
\]
并将 cluster DtN 与 CH bulk 的 full metric jet、harmonic flux 正确匹配，则稀疏塔上预期得到
\[
P\ge \tau_\infty^P k
-C\frac{k^2}{A}
-o(k).
\]
当 \(k=o(A)\) 且 \(\tau_\infty^P>0\) 时，
\[
P\ge c'k.
\]
要推广为所有度量的 theorem，还需补上 field-selection/depletion 控制。

### 上构造侧

若构造
\[
m_\nu\to\infty,\qquad
T_{m_\nu}^{\mathcal R}=o(m_\nu),
\]
则每个 cluster 在外 collar 上精确匹配 CH pair，可嵌入足够大的有限覆盖，拼接后仍得到真实闭 harmonic-zero pair，并有
\[
\mathcal R=o(k),\qquad P=o(k).
\]
若只有 \(T_m^P=o(m)\)，还不能推出归一化 Einstein defect 小；必须另外证明
\[
\int(s+4)^2=o(m)
\]
或进行具有同阶控制的 scalar repair。

因此，真正决定 \(O(k)\to o(k)\) 的数学对象是 \(\tau_\infty^P\) 或 \(\tau_\infty^{\mathcal R}\)，而不是固定 cap 路线、单尾响应或形式 common mode。

---

## 9. 最便宜且最有区分力的计算

### 第一阶段：实际单元的 coupled full-trace Hessian

这是现有基础设施上成本最低的判别。

在 \(\Sigma=\{x=\rho\}\) 上选取：

1. metric 的全部低阶 \(SU(2)\) 表示，包括已知反对称径向块及最低非径向块；
2. harmonic potential \(a_T\) 与 flux \(\beta\) 的对应表示；
3. 固定 pullback class 与 \(e=0\)。

逐块计算
\[
\mathcal K_\ell
=
\Lambda_{C,\ell}
+\Lambda_{{\rm CH},\ell}^{\rm eff}
\]
及核心 load \(f_\ell\)，并验证：

\[
E_{\rm ext}=\delta^2/I,\qquad
\ker E_{\rm ext}=\{\delta=0\},
\]
以及 Step 29 的 \(B\)-flux cancellation。

得到局部最优系数
\[
e_{\rm loc}
=
P_{\rm cell}
-\sum_{\ell\le\ell_0}
\langle f_\ell,\mathcal K_\ell^\dagger f_\ell\rangle.
\]

* 若区间算术证明 \(e_{\rm loc}>0\)，且除 gauge、scale、mass 及固定 cohomology 核外所有低特征值一致离零，则 Step 39 单元附近不存在通向 \(o(k)\) 的小振幅分支。
* 若出现趋零特征值，其 eigenvector 直接给出下一步应延拓的 coupled metric/form diffuse ansatz。
* 高角频块可由四阶椭圆主符号统一控制，因此数值上只需处理有限多个低模。

只改变一个 far-tail 标量 \(w(X)\) 的计算可作为初步校验，但不足以判别全问题，因为当前成本主要位于 \(x\lesssim5\) 的非线性核心，而不是 far tail。

### 第二阶段：多点 Green/Calderón 矩阵

对放置点 \(p_i\) 计算
\[
\mathcal K_{ij}
=
\delta_{ij}\Lambda_C
+G_{\rm CH}(p_i,p_j),
\]
其中 \(G_{\rm CH}\) 是 coupled Einstein–Hodge 接口 Green kernel。监测
\[
\lambda_{\min}(\mathcal K),\qquad
\langle f,\mathcal K^\dagger f\rangle.
\]

* 若非对角块总贡献为 \(o(k)\)，则每核系数趋向 \(e_{\rm loc}\)；
* 若唯一 collective compliance 的刚度为 \(A\)，则修正为 \(O(k^2/A)\)；
* 若 compliance 超线性增长，则其 eigenvector 会辨认出真正的 Hodge drift、field depletion 或非线性 collective branch。

### 最终决定性 theorem/calculation

计算有限 \(m\) 的
\[
T_m^P/m,\qquad T_m^{\mathcal R}/m
\]
并寻找随 \(m\) 的趋势，是最直接的 nonlinear cluster test。统一正下界证明线性 tariff；趋零的 realizable cluster 序列直接给出 \(o(k)\) 上构造。

---

## 10. 与 \(P\) 及归一化 Einstein defect 的关系

在体积锁定 \(V=2\pi^2A\) 下，
\[
\frac{\mathcal R(g)}{V}
=
4\,\frac{\mathcal R(g)/(8\pi^2)}{A}.
\]
若 \(s=-4\)，则 \(\mathcal R=P\)，故
\[
P=\Theta(k)
\quad\Longrightarrow\quad
\mathscr D=\Theta(k/A),
\]
而
\[
P=O(k^2/A)
\quad\Longrightarrow\quad
\mathscr D=O(k^2/A^2).
\]
若未固定 \(s=-4\)，必须把
\[
\frac14\int(s+4)^2
\]
与 \(P\) 同时控制。

Step 39 的每单元
\[
4.08167\,(2\pi^2)
\]
是包含 \(|\Ric+g|^2\)、Weyl-model 误差和 amplitude defect 的 augmented branch numerator；它证明当前真实 harmonic-zero pair 位于线性 surgery-density 尺度，但既不是 \(P\) 的下界，也不是弥散二次尺度的上构造。

结论上，当前有严格支持的是：

* perturbative CH collective compliance 只能给 \(O(k^2/A)\) 修正；
* \(O(k)\to o(k)\) 若发生，必来自核心的非微扰集体重构、非 canonical field/depletion，或明确分离的 Hodge/period escape；
* 最便宜的可靠判别是 coupled core–bulk Hessian，而完整判别对象是多核心相对 tariff \(\tau_\infty^P,\tau_\infty^{\mathcal R}\)；
* cap 路线、aligned pockets、\(\eta\)-drift、零 exceptional periods 和 O10 是不同问题，不能互相充当证据。
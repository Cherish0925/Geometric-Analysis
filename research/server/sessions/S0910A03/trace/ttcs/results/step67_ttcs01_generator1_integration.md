# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 67,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step67_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step67_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Starting from the verified Gaussian Einstein equations and Koiso local germ in Step 67, derive a mathematically useful formulation of the global two-ended matching problem to flat hyperbolic cusp data on T^3. Analyze the linearization about an exact flat cusp and about a reflection-symmetric W=0 central slice. Seek explicit mode decompositions, conserved/monotone quantities, stable/unstable dimensions, or a boundary map whose surjectivity/obstruction could decide whether a constant-scalar -6 central torus can connect to flat cusp ends with exact or uniformly small Ric+3g defect. Propose the cheapest decisive calculation or theorem, and stress-test it against exact cusps and Koiso germs. Do not infer nonexistence from elliptic ill-posedness or finite numerical failure, and do not invent literature.

## Integrated Scientific Memo

## 全局双端匹配问题的可用表述

采用
\[
G=dt^2+g_t,\qquad S=\frac12g_t^{-1}\dot g_t=-W,\qquad H=\operatorname{tr}S,
\]
并记 Einstein 缺陷
\[
E:=\operatorname{Ric}_G+3G.
\]
由已核验的 Gaussian 公式可得
\[
\begin{aligned}
\dot g&=2gS,\\
\dot S&=\operatorname{Ric}_{g}^{\#}+3I-HS-E_T^\#,\\
\dot H&=3-|S|^2-E_{00},\\
\operatorname{div}S-dH&=E_{0\cdot},\\
R_g+|S|^2-H^2&=-6+\operatorname{tr}_gE_T-E_{00}.
\end{aligned}
\tag{1}
\]
最后两式分别是动量约束和 Hamilton 约束；它们不能被只求解切向演化方程所替代。

对反射对称颈，只需研究半边 \(t\in[0,L]\)。中心条件是
\[
S(0)=0,\qquad R_{g_0}=-6,
\tag{2}
\]
其中 \(g_0\) 为解析度量时，Koiso 定理给出唯一局部解析 Einstein germ。终端要求在某个邻域内成为精确平坦 cusp：
\[
g_t=e^{2(t-L)}a^2F,\qquad F\ \text{flat on }T^3,
\tag{3}
\]
故 \(S=I,\ H=3,\ E=0\)。一个完整的量化对象是
\[
\varepsilon(L,F):=
\inf\left\{\|E\|_{L^\infty([0,L]\times T^3)}:
(1)\text{--}(3)\text{成立}\right\}.
\tag{4}
\]
反射产生另一端。问题分为：

* 是否存在某个 \(L\) 使 \(\varepsilon(L,F)=0\)；
* 更重要地，是否
  \[
  \inf_{L,F}\varepsilon(L,F)=0?
  \tag{5}
  \]

这一区分至关重要：精确匹配不可能，并不推出一致小缺陷匹配不可能。

---

## 1. 精确 Einstein 情形的点态单调量

分解
\[
S=\frac H3I+A,\qquad \operatorname{tr}A=0.
\]
当 \(E=0\) 时，
\[
H'=3-\frac{H^2}{3}-|A|^2,\qquad
A'=\operatorname{Ric}_{g}^{\circ}-HA.
\tag{6}
\]
由 \(H(0)=0\) 与标量比较，
\[
H(t)\le 3\tanh t<3
\tag{7}
\]
只要解存在。因此从 totally geodesic 中心出发的精确 Einstein 解不可能在有限 \(L\) 达到精确 cusp 数据 \(H(L)=3\)。

在 \(-3<H<3\) 区域定义
\[
Q(t,x)=e^{2t}\frac{3-H(t,x)}{3+H(t,x)}.
\tag{8}
\]
直接计算得到
\[
\boxed{\frac d{dt}\log Q
=\frac{6|A|^2}{9-H^2}\ge0.}
\tag{9}
\]
因为 \(Q(0)=1\)，任一精确延拓均有 \(Q\ge1\)。这既允许 Koiso 局部反转，也排除了有限距离精确 cusp 匹配；二者没有矛盾。

### 三个必要校验

1. **精确 cusp**：\(S=I,H=3,A=0\)。此时 \(Q=0\)，但该解没有 \(S=0\) 中心叶，故不受 \(Q(0)=1\) 的结论约束。

2. **形式 cosh 模型**：
   \[
   g_t=\cosh^2t\,q,\qquad \operatorname{Ric}_q=-2q,
   \]
   给出 \(H=3\tanh t,A=0,Q\equiv1\)。这种 \(q\) 不可能存在于 \(T^3\)，但它是正确的符号和常数校验。

3. **Koiso germ**：若 \(R_q=-6,\ S(0)=0\)，则
   \[
   g_t=q+t^2(\operatorname{Ric}_q+3q)+O(t^4),
   \tag{10}
   \]
   \[
   A=t\,\operatorname{Ric}_q^\circ+O(t^3),
   \]
   \[
   H=3t-\left(1+\frac13|\operatorname{Ric}_q^\circ|^2\right)t^3+O(t^5),
   \tag{11}
   \]
   \[
   Q=1+\frac29|\operatorname{Ric}_q^\circ|^2t^3+O(t^5).
   \tag{12}
   \]
   这与 (9) 一致。特别地，单调量没有错误地禁止已严格存在的局部反转 germ。

---

## 2. 对共形紧 Einstein 端的精确障碍

若该 germ 延拓为共形紧端，令 \(r=e^{-t}\)，写
\[
G=r^{-2}(dr^2+\gamma_r).
\]
在四维 ambient 情形，若采用标准 geodesic compactification 展开
\[
\gamma_r=\gamma_0-r^2P_{\gamma_0}+r^3\gamma_3+O(r^4),
\qquad
\operatorname{tr}_{\gamma_0}\gamma_3
=\operatorname{div}_{\gamma_0}\gamma_3=0,
\tag{13}
\]
则
\[
H=3+\frac14R_{\gamma_0}e^{-2t}+O(e^{-3t}).
\tag{14}
\]
结合 (9) 得到
\[
\boxed{
-\frac{R_{\gamma_0}(x)}{24}
=
\exp\!\left[
\int_0^\infty
\frac{6|A(t,x)|^2}{9-H(t,x)^2}\,dt
\right]\ge1.}
\tag{15}
\]
因而在由中心距离选定的共形代表中，
\[
\boxed{R_{\gamma_0}(x)\le-24.}
\tag{16}
\]

所以：

* totally geodesic 中心不能精确连接到平坦共形无穷远；
* 障碍落在 \(e^{-2t}\) 的 mean-curvature 模，而不是自由的 TT 系数 \(\gamma_3\)；
* 这不排除共形边界为某个负标量曲率 \(T^3\) 度量的 Einstein core。

式 (13)–(16) 依赖共形紧光滑展开这一额外假设；Koiso 的局部定理本身并不保证全局延拓或该渐近结构。

---

## 3. 平坦 cusp 附近的线性模

在线性化背景
\[
\bar g_t=e^{2t}F,\qquad \bar S=I
\]
上，令
\[
h=\bar g^{-1}\delta g,\qquad s=\delta S.
\]
则
\[
\dot h=2s,\qquad
\dot s=e^{-2t}\mathcal R_Fh-3s-(\operatorname{tr}s)I,
\tag{17}
\]
其中
\[
(\mathcal R_Fh)_{ij}
=\frac12\bigl(
\partial^k\partial_i h_{kj}
+\partial^k\partial_j h_{ki}
-\Delta h_{ij}
-\partial_i\partial_j\operatorname{tr}h
\bigr).
\tag{18}
\]
线性化约束为
\[
e^{-2t}\bigl(
\partial^i\partial^jh_{ij}
-\Delta\operatorname{tr}h
\bigr)-4\operatorname{tr}s=0,
\tag{19}
\]
\[
\partial^js_{ji}-\partial_i\operatorname{tr}s=0.
\tag{20}
\]

对非零 Fourier 波矢 \(k\)，在 TT 扇区
\[
k^jh_{ij}=0,\qquad \operatorname{tr}h=0
\]
中，每个 \(k\) 有两个偏振，并满足
\[
h''+3h'-|k|_F^2e^{-2t}h=0.
\tag{21}
\]
令 \(z=|k|_Fe^{-t}\)，两个显式解为
\[
f_+(z)=(1+z)e^{-z},\qquad
f_-(z)=(1-z)e^z,
\tag{22}
\]
且
\[
f_\pm(z)=1-\frac12z^2\pm\frac13z^3+O(z^4).
\tag{23}
\]
因此每个非零 TT 模在无穷远有：

* 一个中心模 \(h_0\)：改变边界共形度量；
* 一个稳定模 \(h_3e^{-3t}\)：改变 TT 响应张量。

固定边界共形度量后，每个 \(k\ne0\) 剩两个稳定偏振。反向从 cusp 做 Cauchy 延拓时，稳定组合一般包含 \(e^z\) 分量，说明数值上极度不稳定；这只是病态性，不是非存在性证据。

对 \(k=0\)，
\[
h=h_0+h_3e^{-3t},
\tag{24}
\]
其中 \(h_0\) 是六维平坦模量方向，\(h_3\) 是五维无迹稳定方向。

TT 方程还具有守恒 Wronskian
\[
\Omega_t(h_1,h_2)
=e^{3t}\bigl(
\langle h_1,\dot h_2\rangle
-\langle\dot h_1,h_2\rangle
\bigr),
\tag{25}
\]
其无穷远值正比于
\[
\langle h_0^{(1)},h_3^{(2)}\rangle
-\langle h_3^{(1)},h_0^{(2)}\rangle.
\tag{26}
\]
这提示完整 Einstein 边界映射的线性化具有自然辛结构；它可用于证明 Dirichlet-to-Neumann 映射的对称性，但不能单独强迫 \(\gamma_3=0\)。

---

## 4. \(W=0\) 中心叶附近的线性化

设中心度量为 \(q\)，满足
\[
R_q=-6,\qquad S(0)=0.
\]
保持中心约束的变分 \(K=\delta q\) 必须满足
\[
DR_q(K)
=-\Delta_q\operatorname{tr}K
+\operatorname{div}_q\operatorname{div}_qK
-\langle\operatorname{Ric}_q,K\rangle=0.
\tag{27}
\]
反射条件给出
\[
K'(0)=0,
\tag{28}
\]
而由 Einstein 演化式
\[
K''(0)=2D\operatorname{Ric}_q(K)+6K.
\tag{29}
\]

主符号层面，每个非零余切方向有：

* 6 个对称二张量分量；
* 减去 3 个切向微分同胚规范方向；
* 减去 1 个标量约束；

留下 2 个物理自由度，恰与 cusp 端每个非零 \(k\) 的两个 TT 稳定偏振匹配。因此没有局部维数不匹配；真正的障碍只能是全局核、余核或非线性失配。

可定义中心到无穷远的边界映射
\[
\mathcal B:q\longmapsto(\gamma_0,\gamma_3)
\tag{30}
\]
（模切向微分同胚），定义域限于确实延拓为共形紧 Einstein 端的常标量曲率中心度量。式 (15) 给出其像的一个显式非线性约束。决定局部满射性的对象是规范固定后
\[
D\mathcal B_q
\]
的核与余核，而不是未经规范处理的椭圆 Cauchy 问题。

---

## 5. 小缺陷为何可能绕开精确障碍

当 \(E\ne0\) 时，(9) 变为
\[
\boxed{
\frac d{dt}\log Q
=
\frac{6(|A|^2+E_{00})}{9-H^2}.}
\tag{31}
\]
所以它不再无条件单调；符号可由 \(E_{00}\) 改变，而且在 \(H\to3\) 时被放大。

令 \(\eta=3-H\)，则
\[
\eta'+2\eta
=
|A|^2+E_{00}+\frac{\eta^2}{3}.
\tag{32}
\]
精确中心端通常具有 \(\eta\sim Ce^{-2t}\)。在距离 \(L\) 把它修正为 \(\eta=0\)，正常分量所需缺陷仅为 \(O(e^{-2L})\)。标量比较也只给出渐近下界
\[
\varepsilon\gtrsim12e^{-2L},
\tag{33}
\]
并无与长度无关的正间隙。

更关键的是共形度量存在慢中心模。写
\[
g_t=e^{2t}\gamma_t,\qquad S=I+B,\qquad b=\operatorname{tr}B.
\]
则
\[
\gamma'=2\gamma B,
\tag{34}
\]
\[
B'
=e^{-2t}\operatorname{Ric}_{\gamma}^{\#}
-bI-3B-bB-E_T^\#.
\tag{35}
\]
若 \(\gamma(u)\), \(u\in[0,1]\)，是任意端点附近常值的光滑度量路径，并在区间 \(T\le t\le T+K\) 取
\[
u=\frac{t-T}{K},\qquad
G=dt^2+e^{2t}\gamma(u),
\tag{36}
\]
则
\[
B=\frac1{2K}\gamma^{-1}\partial_u\gamma
\]
且直接代入得到
\[
\begin{aligned}
E_{00}&=-2b-|B|^2-b',\\
E_T^\#&=
e^{-2t}\operatorname{Ric}_{\gamma}^{\#}
-bI-3B-bB-B',\\
E_{0\cdot}&=\operatorname{div}_{\gamma}B-db.
\end{aligned}
\tag{37}
\]
在固定光滑路径及一致椭圆性假设下，
\[
\boxed{
\|E\|_{L^\infty}
\le C_\gamma\left(K^{-1}+e^{-2T}\right).}
\tag{38}
\]
因此只要存在一个反射对称、共形紧的精确 Einstein core
\[
\begin{cases}
\operatorname{Ric}_G=-3G,\\
S(0)=0,\quad R_{g_0}=-6,\\
G\text{ 在 }t\to\infty\text{ 共形紧},
\end{cases}
\tag{39}
\]
即使其边界度量不是平坦的，也可：

1. 在大 \(T\) 截断精确端；
2. 用长 \(K\) 的绝热层把边界代表缓慢变为某个平坦 \(F\)；
3. 接上精确平坦 cusp；
4. 关于中心反射。

总缺陷为
\[
O(e^{-2T})+O(K^{-1})\to0.
\tag{40}
\]

这说明精确 flat-end 障碍 (15) **不能**产生一致 \(L^\infty\) 缺陷下界。任何真正的 gap 定理都必须排除 Einstein core (39)，或证明所有中心演化在进入 cusp 慢流形前保持定量距离；匹配层本身不能提供这样的 gap。

---

## 6. 最便宜且真正决定性的计算

最有价值的有限计算不是继续扩大 Step 66 的旧 Fourier 优化，而是计算一个规范固定的混合边值算子的最小奇异值：

1. 选取解析 \(q\) 满足 \(R_q=-6\)；
2. 由 Koiso 展开初始化 \(S(0)=0\) 的精确 germ；
3. 在紧化半柱上使用 Einstein–DeTurck 方程；
4. 内边界施加 totally geodesic 条件；
5. 外边界施加选定的负标量曲率共形度量；
6. 同时监控 DeTurck 向量、Hamilton/动量约束和恒等式 (9)/(15)。

其线性化应在去规范后呈 index-zero 的 TT 主符号结构。一个严格可复核的非退化解将建立 core (39)，随后 (36)–(40) 给出小缺陷平坦 cusp 颈。相反，只有对整个允许中心数据类证明统一余核障碍或先验 blow-up/compactness 排除，才能得到非存在性；单次求解失败或极小奇异值都不够。

### 必须满足的压力测试

任何候选计算或定理均应同时通过：

* 精确 cusp：\(S=I,H=3,E=0\)；
* Koiso germ 的展开 (10)–(12)；
* cusp TT 显式模 (22)–(23)；
* Hamilton 与动量约束，而非仅切向方程；
* Einstein–DeTurck 向量为零；
* 若声称精确共形紧 core，则检验点态公式 (15)。

---

## 核心结论

目前可严格得到：

1. totally geodesic 常标量曲率 \(-6\) 中心叶存在局部精确 Einstein 反转 germ；
2. 它不能在有限距离精确匹配平坦 cusp；
3. 若其精确延拓共形紧，则中心选定的边界代表满足 \(R_{\gamma_0}\le-24\)，故不能平坦；
4. 中心与 cusp 的线性物理自由度在主符号层面匹配，没有显然的维数障碍；
5. 共形度量是慢中心模，长绝热层可用 \(O(K^{-1})\) 缺陷完成非平坦到平坦的变化；
6. 因而一致小缺陷问题等价地集中到 Einstein core (39) 的存在/非存在，而非精确 flat-cusp 匹配本身。

精确未决对象是：是否存在某个解析 \(T^3\) 度量 \(q\) 满足 \(R_q=-6\)，使其 \(S=0\) Koiso germ 全局延拓为共形紧负 Einstein 半柱。这个对象一旦存在，绝热匹配即给出两端平坦 cusp 的一致小缺陷颈；若不存在，则需要一个适用于全部此类 \(q\) 的全局障碍，而非椭圆 Cauchy 病态性或有限数值失败。
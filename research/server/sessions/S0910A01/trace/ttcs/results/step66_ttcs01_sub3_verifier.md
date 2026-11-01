# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step66_route_reorientation_after_IL_bridge.md",
    "Sessions/S0910A01/workspace/notes/step65_per_datum_existence_theorem.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

Read the Step 66 route reorientation note and related context. Check the mathematical logic and scope: the correction to Step65's family-uniform C^k wording; exclusion of #5CP2 by tight-pinching Hitchin--Thorpe; asymmetric interpretation of A02's Green-operator desingularization computation; and the claimed flow-transfer principle from sign-general cutoff flow plus calibration density to a branch gap. Identify any overstatement, missing assumption, or stronger route suggested by the same evidence. Keep the answer scientific and concrete.

## Output

# 数学核验备忘录

## 总体结论

Step 66 的四项核心判断中：

1. **撤回“族上一致 \(C^k\) 高阶估计”是正确的。**延拓单个解只需该解在假定的有限终止时刻具有光滑正定端点；但这仍依赖当前张量层级确实给出所有阶的固定背景估计与时间收敛。所给文件尚未完整展示这一层级。
2. **\(\#_5\mathbb{CP}^2\) 的排除完全成立。**同一计算还排除了 \(\#_4\mathbb{CP}^2\) 的任意紧 \(\pm1\)-Ricci 夹逼，故在这组连通和中只有 \(m\le3\) 仍可能进入紧夹逼研究。
3. **Green 算子计算的非对称解释方向正确，但“计算成功即构造精确 Einstein 度量”仍过强。**首阶阻碍消失通常只是相容性；精确存在还需完整非线性拼接。
4. **flow-transfer 思想是有价值的抽象框架，但 Step 65 只提供各符号、各维数的局部存在。**Steps 55–63 的平滑和紧性模块是四维、\(\sigma=-1\) 结构，不能仅凭 Step 65 直接移植到 \(\sigma=+1\) 或 \(n\ge5\)。此外，局部 Einstein germ 只能与局部不可能性配合；“刚性类别与拓扑不相容”需要额外的全局延拓或全局紧性定理。

---

## 1. Step 65 一致性措辞的修正

### 1.1 每个 datum 的延拓确实不需要族上一致高阶估计

把几何方程写成固定微分算子
\[
\partial_t g=F_{\chi,\sigma}(g)
:=-2\chi^2(\operatorname{Ric}_g-\sigma g).
\]
若旧解在 \(t=T\) 具有 \(C^\infty\) 正定极限 \(g_T\)，新解从同一个 \((g_T,\chi,\sigma)\) 出发，则两侧一阶时间导数均为 \(F_{\chi,\sigma}(g_T)\)。继续对方程求时间导数可见，每个
\[
\partial_t^k g(T)
\]
都是 \(g_T,\chi\) 的有限阶空间 jet 所决定的通用微分表达式。因此所有时间 jet 自动相同；这里不需要几何方程的唯一性。Step 66 所说“不需要单个贯穿全程的 DeTurck gauge”也是正确的。

但这一论证需要的不只是
\[
|aE|,\quad |a\operatorname{Rm}|
\]
的低阶有界性。必须得到：

- 对所有 \(m\)，固定背景下 \(g(t)\) 的 \(W^{m,p}\) 一致有界；
- \(\partial_t g=-2aE\) 在相应 \(W^{m,p}\) 中可积；
- \(t\uparrow T\) 时存在唯一的 \(C^\infty\) 极限，而不只是若干子列极限；
- 极限度量保持正定。

Step 55 的 (2.9)–(2.14) 给出了正确的三角结构，但其表述明确以“当前张量估计已完成到所需各阶”为前提。该文件 §4 仍把全阶 current-pair 层级列为尚缺内容。Step 65 又把关键的一致 tame estimate (4.3) 主要委托给未随本任务提供的 A03 Step 56；§4.5 在所给文本中还缺失标记为 (4.9) 的具体式子。因此，“延拓逻辑不需族上一致 \(C^k\)”成立，但“所有端点正则性已经由所给文件独立证明”尚无法从这些文件本身复核。

### 1.2 序列紧性仍需族上一致的低阶几何量

不需要族上一致的所有 \(C^k\) 估计，不等于完全不需要族上一致估计。IL 的局部极限至少需要：

\[
|\operatorname{Rm}_{g_i(T)}|\le K
\]
在统一大小的平台缓冲区成立，以及
\[
\|\operatorname{Ric}_{g_i(T)}+g_i(T)\|_{L^\infty}\to0.
\]

在指数映射拉回球上，还需统一半径低于共轭半径，并有足够的体积与 harmonic-radius 控制。对 Step 8 中仅含代数曲率的密度，有限 \(W^{2,p}\)、\(p>2\)，已经足够传递 \(W^+\)、标量曲率和特征值密度，不需要近似度量的族上一致 \(C^\infty\) 控制。这正好支持 Step 66 的修正，但应明确区分：

- **延拓单个流：**每个 datum 的全阶端点控制；
- **抽取 Einstein germ：**族上一致曲率、非塌缩拉回球和有限 \(W^{2,p}\) 控制。

### 1.3 Step 65 §7 的 gauge 初值有一处内部不一致

若在原几何坐标中从 \((g(T),\chi)\) 重新启动，并让新的 DeTurck 微分同胚从恒等映射开始，则新的 transported cutoff 满足
\[
\widetilde\beta(0)=\chi.
\]
Step 65 §7 随后写成
\[
\widetilde\beta(0)=\chi\circ\varphi_T^{-1},
\]
这是沿用旧 transported 坐标时的表达。后者对应的初值应是旧坐标中的 \((G(T),\beta(T))\)，而不是几何坐标中的 \((g(T),\chi)\)。Step 66 放弃拼接单一 DeTurck gauge 后，这个混淆可以完全避开：只在几何变量中拼接即可。

---

## 2. \(\#_5\mathbb{CP}^2\) 与 Hitchin–Thorpe

计算无误：
\[
\chi(\#_m\mathbb{CP}^2)=m+2,\qquad
\tau(\#_m\mathbb{CP}^2)=m,
\]
所以
\[
2\chi-3|\tau|=4-m.
\]
对 \(\delta_\sigma(g)\le\varepsilon\)，写 Ricci 特征值为 \(\sigma+e_i\)，其中 \(|e_i|\le\varepsilon\)。则
\[
|s|\ge4(1-\varepsilon),\qquad
|E|^2\le4\varepsilon^2.
\]
代入四维 Chern–Weil 公式得
\[
2\chi\pm3\tau
\ge \frac{\operatorname{Vol}(M,g)}{4\pi^2}
\left[\frac23(1-\varepsilon)^2-2\varepsilon^2\right].
\]
当
\[
\varepsilon<\varepsilon_{\mathrm{HT}}
:=\frac1{1+\sqrt3}
\]
时右侧严格为正。因此任意满足
\[
2\chi\le3|\tau|
\]
的定向四维流形都具有统一的 \(\pm1\)-Ricci 缺陷下界 \(\varepsilon_{\mathrm{HT}}\)。

由此不仅有：

- \(m=5\)：严格违反 Hitchin–Thorpe，既无 Einstein 度量，也无任意紧的 \(\pm1\) 夹逼；
- \(m>5\)：同样被排除；

还包括：

- \(m=4\)：虽然是等号情形，仍不可能有 \(\delta_\sigma\to0\)。

因此在 \(\#_m\mathbb{CP}^2\) 这一组中，紧正支候选实际上只剩 \(m\le3\)。Step 66 的“严格 Hitchin–Thorpe 类型”定位是必要条件，但还不是足够信息：仍需同时知道底层流形没有任何 Einstein 度量，并真正构造 \(\delta_+\to0\)。所给 dossier 只把 \(\#_3\mathbb{CP}^2\) 的 Einstein 存在状态列为待核实问题，不能把它直接当作已知无解类型。

还应保留一个符号区别：正 Ricci 输入并不强迫假想输出 Einstein 度量具有正 Einstein 常数。因此对候选流形的全局无解论证必须处理 \(\lambda>0,\lambda=0,\lambda<0\) 三种情形。

---

## 3. A02 Green 算子计算的含义

Step 66 对“局部去奇点信息不能替代全局无 Einstein”的说明正确，但开头“该计算可以决定某个轨形退化能否去奇点”为双向表述，强于通常的 Green 算子计算。

典型的逻辑层次是：

1. Green 算子或相互作用矩阵给出首阶匹配项；
2. 非零余核投影在一个已证明的必要性定理下，可排除指定轨形、指定 ALE 泡、指定尺度与定向模式的 Einstein 退化；
3. 首阶投影为零只表示首阶相容，尚需处理高阶项、核与余核、尺度和旋转参数、多个奇点的耦合、规范固定、反算子估计及非线性余项；
4. 只有完成这些分析并得到精确解，才能断定所得光滑类型承载 Einstein 度量。

即使首阶阻碍非零，也必须确认所有可调参数都已纳入；单个矩阵元非零不排除由尺度向量、轨形 Einstein 变形或不同泡定向产生的抵消。

反过来，完整非线性拼接若成立，确实立即证明该光滑类型存在 Einstein 度量。局部阻碍则只排除所研究的退化通道。要从它推出该光滑类型无任何 Einstein 度量，需要一个覆盖所有 Einstein 度量的全局紧性或分类结果，并分别处理非零 Einstein 常数的两种归一化以及 Ricci-flat 情形。仅覆盖正 Einstein 序列仍不足以排除其他符号。

---

## 4. flow-transfer 原理的精确形态

Step 66 的三点描述抓住了机制，但还需要展开成下列假设组。设固定 \(n,\sigma\)，并考虑某个流形族。若存在
\[
\delta_\sigma(g_i)\to0
\]
的序列，需统一得到：

### 4.1 局部流的可运行条件

存在固定尺度 \(r,\theta\)、cutoff \(\chi_i\) 及平台缓冲区，使初始局部 Sobolev–临界曲率量满足
\[
\mathcal S_i(0)\,H_i(0)^{1/2}<\gamma_*
\]
（四维情形），cutoff 各阶导数也具有所需控制。单纯存在“全局曲率预算”并不自动给出这一小量条件。

### 4.2 到共同观察时刻的估计

在 \(T=\theta r^2\) 有
\[
V_i(T)=\int_0^T\|\chi_i^2E_{\sigma,i}(t)\|_\infty\,dt\to0,
\]
并在平台上得到统一的完整曲率上界及
\[
\|E_{\sigma,i}(T)\|_\infty\to0.
\]
各 datum 的全阶固定背景估计负责延拓；族上一致的低阶估计负责局部紧性。

### 4.3 校准密度必须在终端时刻仍然趋零

需要一个自然、非负的密度 \(\Phi_\sigma(g)\)，以及明确的拓扑恒等式、规范理论不等式或流中误差估计，推出某些终端拉回球满足
\[
\fint_{\mathcal B_\rho(p_i)}
(\exp_{p_i})^*\Phi_\sigma(g_i(T))\,d\mu\longrightarrow0.
\]
“支持集占据固定体积比例”只是实现这一步的一种方法；还需处理指数映射的多重覆盖、平台缓冲和 Liouville 平均。

### 4.4 极限正则性必须足以传递密度

在拉回球上应有统一 harmonic radius 或等价的有限 \(W^{2,p}\) 紧性，使极限满足
\[
\operatorname{Ric}_{g_\infty}=\sigma g_\infty
\]
并能把 \(\Phi_\sigma\) 传递到极限。由非负性和局部平均趋零，才可推出
\[
\Phi_\sigma(g_\infty)\equiv0
\]
于一个开球。

### 4.5 最后一步有两种不同形式

- **局部型：**不存在满足 \(\operatorname{Ric}=\sigma g\) 且 \(\Phi_\sigma=0\) 的光滑 germ。IL 的 Derdziński 谱矛盾属于这一型。
- **全局型：**\(\Phi_\sigma=0\) 只产生一个合法的局部 Einstein 模型，但其完整延拓与某种全局拓扑不相容。此时局部紧性本身不够，还需解析延拓、完备化、单值性或全局收敛定理。

Step 66 把这两型并列在同一句中，容易掩盖第二型所需的额外全局论证。

当以上常数对整个流形族统一时，反证序列法才给出该族的正缺陷间隙。这个间隙一般依赖校准、cutoff、Sobolev 小量和拓扑族；只有这些量最终都仅依赖 \(n\)，才能得到原题要求的维数常数。

---

## 5. 符号与维数的可迁移程度

Step 65 的局部存在定理确实对所有 \(\sigma\in\mathbb R\) 和 \(n\ge2\) 表述。但 Steps 55–63 的关键能量是四维的：
\[
L^2\text{ 曲率},\qquad
H^{1}\hookrightarrow L^4,\qquad
\mathcal S H^{1/2}.
\]
在 \(n\ge5\) 时应改为临界 \(L^{n/2}\) 曲率及相应 Sobolev 指数，现有四维估计不能直接视为已完成的高维版本。

符号也需重新计算。按 Step 65 的规范
\[
G_0=\frac{g\owedge g}{2(n-1)},\qquad \operatorname{Ric}(G_0)=-g,
\]
与
\[
E_\sigma=\operatorname{Ric}-\sigma g
\]
相配的 shifted curvature 是
\[
T_\sigma=\operatorname{Rm}+\sigma G_0,
\qquad
\operatorname{Ric}(T_\sigma)=E_\sigma.
\]
因此：

- \(\sigma=-1\)：\(T_{-1}=\operatorname{Rm}-G_0\)；
- \(\sigma=+1\)：\(T_{+1}=\operatorname{Rm}+G_0\)。

Step 55 的
\[
T=\operatorname{Rm}+G
\]
与 \(E=\operatorname{Ric}+g\) 在新的规范下不相容。最终 IL 证明不能只替换一个显示公式；所有涉及 \(U_m=\nabla^m(aT)\)、Ricci 收缩、曲率势项和终端密度的式子都需按 \(T_{-1}\) 重新核算。

---

## 6. IL 子族结果目前最坚实的部分

Step 8 的局部终结机制是具体且有力的。终端极限若满足
\[
\operatorname{Ric}=-g,\qquad
\operatorname{spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right),
\]
则 Derdziński 因子
\[
(24|W^+|^2)^{1/3}=1
\]
迫使极限度量局部 Kähler；但 Kähler–Einstein 四维度量在该归一化下应有
\[
\operatorname{spec}(W^+)
=\left(-\frac23,\frac13,\frac13\right).
\]
这是局部 germ 层面的直接矛盾，不依赖全局拓扑分类，因而非常适合 flow-transfer。

不过，从所给文件尚不能单独推出一个对全部所述 IL geography 一致的 \(\varepsilon_{IL}\)。还需在统一量词下连接：

\[
\delta_i\to0
\Longrightarrow
D_i/A_i\to0,\quad
\operatorname{Vol}_i/A_i\asymp1,
\]
并覆盖 \(A_i\) 有界与 \(A_i\to\infty\) 两种序列，同时证明 support 选择、first-exit 常数、终端平均和延拓层级均不依赖相关 geography 参数。Step 8 验证了校准零集与局部矛盾；Step 55 验证了延拓的三角结构；Step 65 给出各 datum 的局部存在框架。三者之间的统一常数链仍是最终子族定理中必须逐式呈现的内容。

同一证据还给出一个更锋利的路线整理：四维 \(\#_m\mathbb{CP}^2\) 中 \(m\ge4\) 已由显式常数 \(\varepsilon_{\mathrm{HT}}\) 全部排除；Green 算子结果应分为“首阶相容”“特定退化受阻”“完整非线性存在”三种数学产物；flow-transfer 则应拆成“局部 germ 矛盾型”和“全局刚性型”两个独立命题。这样可避免局部去奇点信息、局部 Einstein 极限与底层全局存在性之间的逻辑混合。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 3,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step3_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step3_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Consider the boundary behavior at k/A = 1/3 for Yau Problem 26 (negative branch). At this ratio, the mixed SW bound δ ≥ 0 becomes degenerate. The question is whether there exists a sequence of no-Einstein manifolds M_j = X_j#k_j CP̄² with k_j/A_j → 1/3⁺ carrying metrics with δ_-(g_j) → 0, or whether additional obstructions create a uniform gap. Key considerations: (1) Below k/A = 1/3, Aubin-Yau gives negative Kähler-Einstein metrics on X, and blow-ups may carry KE metrics for small k; (2) At k/A ≈ 1/3, the energy budget forces near-ASD (|W₊|² → 0); (3) The blow-up points create topological changes that must be accommodated geometrically; (4) Stability and deformation theory of KE metrics under blow-up; (5) Whether the 'broken' KE metric just above k/A = 1/3 might still have small δ; (6) Connections to Tian's alpha-invariant, K-stability, and the Yau-Tian-Donaldson conjecture for negative KE. Generate concrete mathematical mechanisms that could determine whether the transition at k/A = 1/3 is continuous or discontinuous in the Ricci-pinching sense.

## Integrated Scientific Memo

## 边界 \(k/A=1/3\) 的机制性结论

设
\[
M=X\#k\,\overline{\mathbb{CP}}^{\,2},\qquad
A=c_1^2(X),\qquad p=\frac{k}{A}=\frac13+\alpha,
\]
并令
\[
\delta=\delta_-(g)=\sup_M\|g^{-1}\Ric_g+I\|_{\rm op}.
\]
现有证据既没有构造出 \(\alpha\downarrow0,\delta\downarrow0\) 的无 Einstein 度量序列，也没有给出边界处统一正间隙；但可以把问题压缩为几个相当具体的数学对象。

### 1. 必须满足的精确尺度律

记
\[
S=\frac1{4\pi^2A}\int\frac{s^2}{24},\quad
W=\frac1{4\pi^2A}\int2|W_+|^2,\quad
T=\frac1{4\pi^2A}\int\frac{|E|^2}{2},\quad
v=\frac{\Vol(g)}{4\pi^2A}.
\]
Chern–Gauss–Bonnet 与混合 SW 估计给出
\[
S+W-T=1-p=\frac23-\alpha,\qquad S+W\ge\frac23,
\]
从而
\[
T\ge\alpha.
\]
结合点态 Ricci 夹逼与体积上界，已有严格估计为
\[
\boxed{\ \frac{\delta}{1-\delta}\ge \sqrt{\frac{\alpha}{2}}\ }.
\]
因此任何连续过渡都必须满足
\[
\alpha=O(\delta^2).
\]
特别是自然的整数取整序列
\[
k=\left\lceil\frac A3\right\rceil,\qquad \alpha=O(A^{-1})
\]
至多允许
\[
\delta\asymp A^{-1/2}.
\]
这表明边界问题不是“固定一个额外 blow-up 后缩小其几何尺度”，而是一个 \(A,k\to\infty\) 的广延极限。

还需纠正“Ricci 夹逼自动迫使 near-ASD”的过强表述。恒等式
\[
W=(T-\alpha)+\left(\frac23-S\right)
\]
说明 \(W\to0\) 需要额外饱和：
\[
T-\alpha\to0,\qquad S\to\frac23,
\]
或等价地在适当归一化下体积也逼近相应 Chern–Weil 上界。仅有 \(\delta\to0\) 与 \(\alpha\to0\) 尚不能单独排除广延的 \(W_+\)-能量。

---

## 2. 普通复 blow-up 的 Kähler 路径被点态符号直接排除

对普通复 blow-up \(\widetilde X\to X\) 的例外曲线 \(E_i\)，有
\[
c_1(T\widetilde X)\cdot E_i=1.
\]
任意 Kähler 度量的 Ricci 形式满足
\[
[\rho]=2\pi c_1(T\widetilde X),\qquad
\int_{E_i}\rho=2\pi.
\]
若同时 \(\delta<1\)，则 \(\Ric_g\le -(1-\delta)g\)，故在 \(E_i\) 的复切平面上
\[
\rho(u,Ju)=\Ric(u,u)\le -(1-\delta)g(u,u),
\]
于是
\[
2\pi=\int_{E_i}\rho
\le -(1-\delta)\Area_g(E_i)<0,
\]
矛盾。

因此：

\[
\boxed{\text{普通 blow-up 复结构上的任何 Kähler 度量都不可能满足 }\delta_-<1.}
\]

所以所谓“越过 \(1/3\) 后的破裂 KE 度量”不能仍是该 blow-up 复结构上的光滑 Kähler 度量。Arezzo–Pacard 型小 Kähler blow-up 也不能产生所需序列：其缩放的 Burns 型核心至多有小积分体积，却不能有小的无权 \(C^0\) Ricci 缺陷。

这也限定了 Tian \(\alpha\)-不变量、K-稳定性和 YTD 的作用。对于 \(K_X\) ample 的负 KE 基底，Aubin–Yau 已解决存在性；普通 blow-up 的障碍首先是上述例外曲线的上同调符号，而不是 Fano 情形那种精细 K-不稳定。Log/K-稳定性仍可用于研究“收缩例外曲线—奇异 KE/电流—再平滑”的路线，但必须另证平滑后
\[
\|\Ric+g\|_{\rm op}\to0
\]
这一远强于弱收敛或积分残差的性质。

---

## 3. 小 ALE 泡不能给出连续过渡

将一个 Ricci-flat ALE 核心缩小并插入背景，核心上始终有
\[
\|\Ric+g\|_{\rm op}=1
\]
（按目标归一化 \(\Ric=-g\)），所以缩小体积只改善积分范数，绝不改善 \(\delta_-\)。非 Ricci-flat 的 Burns 核心更糟：缩放后其 Ricci 端同态通常按逆平方尺度增长。

因此连续过渡所需的局部模型不是“小 Ricci-flat bubble”，而应是一个在自然 \(\Ric=-g\) 尺度上有非退化大小的负 Ricci 曲率 cap、长管或其他纯 Riemannian 区域。

曲率爆破后，若存在非塌缩光滑 blow-up 极限，则重标后的 Ricci 曲率趋零，因此极限确为 Ricci-flat。ALE Ricci-flat 四维泡的 ADE vanishing-cycle 格是偶的、由 \((-2)\)-类生成，不能由单个 \((-1)\)-类局部实现。这为集中路线提供了重要障碍。

但不能据此声称已经排除了所有集中序列。尚缺：

1. 由纯 Ricci 夹逼得到足够的非塌缩与泡树紧性；
2. 处理塌缩的 ALF/ALG/ALH 或更一般局部模型；
3. 证明原流形的每个例外 \((-1)\)-类必须注入泡的紧支撑同调；
4. 排除奇数格通过 neck、regular body 与多个尺度共同承载；
5. 处理 \(A_j,k_j\to\infty\) 时 regular body 本身拓扑也变化的事实。

故“Ricci-flat 泡都是偶格，所以整个序列不可能”目前只是条件性机制，不是定理。

---

## 4. 真正的局部判别对象：负 Einstein 型 \(\overline{\mathbb{CP}}^{\,2}\)-cap

定义
\[
P=\overline{\mathbb{CP}}^{\,2}\setminus B^4
\]
及带外边界 Cauchy 数据 \(\mathcal C=(\gamma,\mathrm{II})\) 的填充缺陷
\[
\Delta(P;\mathcal C)
=\inf_g\sup_P\|\Ric_g+g\|_{\rm op}.
\]
这里 \(g\) 还应满足与 \(\mathcal C\) 的规定匹配，并控制边界 collar、曲率和体积。

这给出清楚的二分：

* 若存在与基底 collar 相容的 \(\mathcal C_j\)，使
  \[
  \Delta(P;\mathcal C_j)\to0,
  \]
  则连续过渡具有局部构造基础；
* 若对所有可匹配数据均有
  \[
  \Delta(P;\mathcal C)\ge c>0,
  \]
  则每个 \((-1)\)-手柄有不可消除的 \(C^0\) Ricci 成本，从而产生间隙机制。

可计算的第一模型是 \(U(2)\)-不变 Bianchi IX ansatz
\[
g=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)+b(t)^2\sigma_3^2,
\]
在 bolt 处施加完整光滑条件，在外边界匹配 \((\gamma,\mathrm{II})\)，并研究
\[
\inf_{a,b}\sup_t\max_i|r_i(t)+1|.
\]
该 ansatz 内无解只能排除对称 cap，不能排除一般 cap；但若能严格构造缺陷趋零的解，则会提供实质性的连续性证据。

每个 cap 还满足带边界的 Chern–Weil 转gression：
\[
2\chi(P)\pm3\tau(P)
=
\frac1{4\pi^2}\int_P
\left(2|W^\pm|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)
+\operatorname{CS}_\pm(\partial P).
\]
因此 ODE 或 PDE 搜索必须同时记录边界 Chern–Simons 项；只优化 Ricci 特征值而不核对拓扑能量是不充分的。

---

## 5. 多 monopole 类可能提供缺失的统一间隙

对所有 blow-up monopole 类
\[
a_\varepsilon=c_1(X)+\sum_{i=1}^k\varepsilon_iE_i,
\qquad \varepsilon_i=\pm1,
\]
有精确平均恒等式
\[
2^{-k}\sum_\varepsilon(a_\varepsilon^+)^2
=(c_1(X)^+)^2+\sum_i(E_i^+)^2.
\]
因而
\[
\max_\varepsilon(a_\varepsilon^+)^2
\ge A+\sum_i(E_i^+)^2,
\]
并得到加强的混合估计
\[
\frac1{4\pi^2}\int
\left(\frac{s^2}{24}+2|W_+|^2\right)
\ge
\frac23\left(A+\sum_i(E_i^+)^2\right).
\]
与 Chern–Gauss–Bonnet 比较即给出
\[
\boxed{\ 
\frac1{4\pi^2}\int\frac{|E|^2}{2}
\ge
k-\frac A3+\frac23\sum_i(E_i^+)^2 .
\ }
\]

因此连续序列不仅要求 \(\alpha\to0\)，还要求
\[
\frac1A\sum_i(E_i^+)^2\to0.
\]
也就是说，约 \(A/3\) 个互相正交的 \((-1)\)-类必须同时几乎完全落入负自对偶 Hodge 子空间。

决定间隙的核心不等式是：能否从 \(\delta_-\ll1\) 推出
\[
\sum_i(E_i^+)^2\ge cA
\]
或任何足以与体积 \(O(A)\) 比较的正下界。若成立，便产生统一 Ricci 间隙；若不成立，则候选构造必须实现大量例外类近乎 ASD。

自然工具是 harmonic ASD 形式的 Weitzenböck 公式
\[
0=\int\left(
|\nabla\eta|^2+
\left\langle\left(\frac{s}{3}I-2W_-\right)\eta,\eta\right\rangle
\right),
\]
但 Ricci 夹逼并不控制 \(W_-\)，所以单靠此式尚不能关闭问题。它把缺口精确转化成 \(\Lambda^-\) 曲率算子的谱密度问题：能否在 \(\Ric\approx-g\) 下容纳 \(k\sim A/3\) 个近 ASD 的整数上同调方向。

---

## 6. SW 近等号刚性是另一种可能的间隙机制

定义
\[
D_a(g)=
\frac1{4\pi^2}\int
\left(\frac{s^2}{24}+2|W_+|^2\right)
-\frac23(a^+)^2.
\]
若候选序列还处于近 ASD、近体积极值、近最小 \(E\)-能量的饱和扇区，则应有
\[
D_{a_j}(g_j)=o(A_j).
\]
混合 SW 估计源于 SW 方程及 Weitzenböck 恒等式。因此一个定量近等号定理可能产生自对偶二形式 \(\omega_j\)，满足例如
\[
A_j^{-1}\|\nabla\omega_j\|_{L^2}^2\to0,\qquad
A_j^{-1}\||\omega_j|-c_j\|_{L^2}^2\to0,
\]
并控制其与 \(W_+\) 特征方向的对齐。

若进一步能把该控制提升为足以使用 adjunction/Taubes 机制的 almost-Kähler 结构，则例外类可能出现为 almost-holomorphic \((-1)\)-曲线；普通 Kähler 情形的 Ricci 形式符号矛盾或许能以定量误差形式恢复，从而产生统一 gap。

关键是不能把“SW 近等号应当 almost-Kähler”当成已知事实。所需的是一个随 \(A,k\) 一致的定量稳定性定理，包括：

* spinor 不消失和归一化；
* 从 \(L^2\) 到足够强局部控制的提升；
* 对 \(O(A)\) 个例外类同时有效；
* 在曲率集中或塌缩区仍保持常数。

---

## 7. 奇异极限与有限维 obstruction 决定缺陷的阶

若边界由某个 Einstein/ASD-Einstein 轨形表示，平滑参数 \(t\) 下可写
\[
F(g_t)=\Ric_{g_t}+g_t=r_t,
\]
规范固定后
\[
F(g_t+h)=r_t+L_th+Q_t(h).
\]
当 \(L_t\) 有小特征值或余核时，关键不是总残差，而是有限维投影
\[
\Pi_t r_t+\Pi_tQ_t(h)=0.
\]
需要计算 \(\Pi_t r_t\) 如何依赖
\[
\alpha=\frac{k}{A}-\frac13.
\]

两种渐近律分别对应两种相变：

\[
|\Pi_t r_t|\sim C\alpha
\]
与 SW 的退化相容，可能允许 \(\delta\sim\sqrt\alpha\)；

\[
|\Pi_t r_t|\ge c>0
\]
则意味着增加一个过临界例外分量就产生局部 \(C^0\) 成本，从而形成跳跃。

这里应计算的是 Pohozaev 通量、ALE 质量、轨形点曲率与高阶匹配项，而不只是“能否修正成精确 Einstein”。精确修正被 SW 阻止是已知拓扑事实；开放问题是未经修正的最小无权 Ricci 残差能否仍趋零。

---

## 8. 体积与几何逃逸方式

在归一化 \(\Ric=-g\) 的最小负 KE 基底上，
\[
\Vol(X)=2\pi^2A.
\]
若过临界候选还满足 \(W/A\to0\) 和上述全面饱和，则
\[
\Vol(M)\sim4\pi^2A.
\]
于是对 \(k\sim A/3\)，新增体积的平均量级约为每个例外分量
\[
\frac{2\pi^2A}{A/3}\sim6\pi^2.
\]
因此 near-ASD 连续过渡不是在固定 KE 背景上加入体积趋零的小泡；其拓扑必须由自然尺度的 caps、广延 Weyl 包或长薄区域承载。若体积没有这一增长，则必须由非忽略的 \(W_+\) 或额外 \(E\)-能量补偿。

此外，Min-Oo 型稳定性意味着任何成功的无 Einstein 序列必须逃离有界几何类：
\[
\diam(g_j)^2\max|\Rm(g_j)|\to\infty.
\]
可能表现为：

1. Weyl 曲率爆破；
2. 直径增长而曲率有界；
3. 二者同时发生。

其中曲率爆破路线受到 Ricci-flat 泡与奇偶格问题的约束；最未受控制的是**有界曲率、体积和直径随 \(A\) 增长的非 Kähler 路线**。它可由许多自然尺度 cap 或长 tube 构成，并不被当前积分不等式排除。

---

## 最小决定性问题集

边界连续性最终可由以下对象决定：

1. **Cap 缺陷**
   \[
   \inf_{\mathcal C\ {\rm compatible}}\Delta(P;\mathcal C)
   \stackrel{?}{=}0.
   \]
   正值支持跳跃；零值提供连续构造的局部模块。

2. **多 monopole 投影间隙**
   \[
   \delta_-\ll1\quad\stackrel{?}{\Longrightarrow}\quad
   \sum_i(E_i^+)^2\ge cA.
   \]
   若成立则混合 SW 估计不再退化。

3. **SW 近等号稳定性**：小 \(D_a/A\) 是否一致地强迫足够强的 almost-Kähler 结构，并使例外类可被 adjunction 检测。

4. **泡树奇偶定理**：在纯 Ricci 夹逼允许的所有塌缩与非塌缩极限中，\((-1)\)-同调是否必然承担不可忽略的 Ricci 缺陷。

5. **轨形 obstruction 的阶**
   \[
   \Pi_t r_t=O(\alpha)\quad\text{还是}\quad
   |\Pi_t r_t|\ge c.
   \]

现阶段最稳妥的科学判断是：普通 Kähler blow-up、小 ALE bubble 和固定比例 \(p>1/3\) 都已被排除；尚存的连续机制必须是广延、非 Kähler、带大 \(W_-\) 自由度并逃离有界几何稳定性范围的构造。是否存在统一 gap，精确取决于上述 cap、multiclass 与近等号刚性问题，现有材料尚不能在连续与不连续之间作严格裁决。
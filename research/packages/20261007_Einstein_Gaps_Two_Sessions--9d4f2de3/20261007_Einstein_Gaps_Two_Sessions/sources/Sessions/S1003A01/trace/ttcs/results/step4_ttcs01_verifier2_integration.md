# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 4,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step4_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step4_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Analyze and strengthen the fixed-exterior part of the O11 cell programme in light of this precise issue. Suppose a true J-minimizing sequence converges in C^2 on compact regular regions while the CH exterior is fixed. Explain exactly how comparison minimality transfers compactly supported local stationarity/stability to the limit; what is still needed to control an interface stress at the free-interior/fixed-collar interface and justify unique continuation to a locally CH base; and prove the quantitative recovered-volume implication from F=((s+3)^2/3)+1+4|W+|^2>=0: how a deficit delta forces at least delta/4 of background CH volume to be unrecovered. Also assess whether the developing-map extension argument applies unchanged to real-hyperbolic negative Einstein / W+-flat bases relevant to the peer O10 route, making all necessary constant-curvature and completeness hypotheses explicit.

## Integrated Scientific Memo

# 固定外部 O11：极小性传递、界面应力、恢复体积与实双曲推广

设 \(C\) 为 cell，\(U_c\subset C\) 为逐点固定成 \(g_{\mathrm{CH}}\) 的开 collar，\(\Omega=C\setminus\overline{U_c}\) 为自由内部，\(\Sigma=\partial\Omega\)。记

\[
J(g)=\int_C |\operatorname{Ric}_g+g|^2\,dV_g,\qquad
J_*=\inf_{\mathcal A}J,
\]

其中 \(\mathcal A\) 是所有在 \(U_c\) 上等于 \(g_{\mathrm{CH}}\) 的光滑度量。设 \(g_i\in\mathcal A\) 是真实极小序列：

\[
J(g_i)\to J_*,
\]

并在极限 regular 区的每个紧集上，经单值标记嵌入 \(\Phi_i\) 有

\[
\Phi_i^*g_i\to g_\infty\qquad\text{in }C^2.
\]

以下结论区分了已经闭合的部分与尚缺的界面输入。

---

## 1. 比较极小性如何传递局部 stationarity 与 stability

取

\[
K\Subset\Omega_\infty^{\rm reg}\setminus\Sigma
\]

及 \(h\in C_c^\infty(S^2T^*K)\)。对小 \(t\)，令

\[
g_\infty(t)=g_\infty+th.
\]

把 \(h\) 经 \(\Phi_i\) 推回原 cell，得 \(h_i\)，并令

\[
g_i(t)=g_i+t h_i.
\]

由于扰动支集远离固定 collar，\(g_i(t)\) 仍可允许；集中区、拓扑与外部标记均不变。极小性给出

\[
J(g_i(t))-J(g_i)\ge J_*-J(g_i)=o(1).
\]

而 \(J\) 的密度仅依赖度量的二阶 jet，故支集邻域上的 \(C^2\) 收敛给出

\[
J(g_i(t))-J(g_i)
\longrightarrow
J_K(g_\infty+th)-J_K(g_\infty).
\]

因此，对每个固定的小 \(t\),

\[
J_K(g_\infty+th)\ge J_K(g_\infty).
\]

同时使用 \(t\) 与 \(-t\)，得到

\[
DJ_{g_\infty}(h)=0,\qquad
D^2J_{g_\infty}(h,h)\ge0.
\]

所以真实比较极小性传递的不只是 Palais–Smale 意义的 stationarity，而是每个紧 regular 自由区上的完整局部极小性与 stability。集中在 \(K\) 外的能量在差分中精确消去，无需全局能量恒等式或 Ekeland 修正。

严格所需条件是：

1. regular 收敛带有单值标记，使扰动可推回原 cell；
2. 收敛在扰动支集的邻域上为 \(C^2\)；
3. 支集远离固定外部、奇点与多重覆盖区；
4. 若要把弱方程提升为经典四阶方程，还需 harmonic gauge 下的局部椭圆正则性。

这一步只产生**自由区内部方程**，不产生跨 \(\Sigma\) 的自然边界条件。

---

## 2. 标量方程可闭合，但张量唯一延拓留下界面应力

### 2.1 标量部分

紧支共形变分 \(\dot g=2fg\) 给出

\[
\dot J=4\int f(\Delta_+s+s+4)\,dV,
\]

故在 regular 自由区

\[
(\Delta_++1)u=0,\qquad u=s+4. \tag{2.1}
\]

如果 \(g_\infty\) 在固定坐标中 \(C^2\) 接到 CH collar，则

\[
u|_\Sigma=0.
\]

在自由区是有界光滑域、且所有缺失 orbifold 点对 (2.1) 可去或无标量通量的条件下，可用 \(u\) 本身测试：

\[
0=\int_\Omega u(\Delta_++1)u
 =\int_\Omega\bigl(|du|^2+u^2\bigr),
\]

因此

\[
s\equiv-4. \tag{2.2}
\]

等价地可用最大值原理。这里真正还需说明的是奇点可去性或足够的 \(H^1\) 控制；若存在非-orbifold 缺失集，不能未经证明排除其携带分布标量通量。

### 2.2 张量方程

令

\[
E=\operatorname{Ric}+g.
\]

在 \(s=-4\) 后，内部 Euler–Lagrange 方程化为

\[
\Delta_-E=-2\operatorname{Rm}(E)+\frac12|E|^2g. \tag{2.3}
\]

在任一 regular 紧集上，右端可写成有界系数线性作用于 \(E\)，故

\[
|\Delta_-E|\le C|E|. \tag{2.4}
\]

\(C^2\) 接合只给出

\[
E|_\Sigma=0,
\]

这不足以推出 \(E=0\)：二阶椭圆系统可有非零的零 Dirichlet 解。

将自由侧 \(E\) 在固定 CH 侧延拓为零，记为 \(\widehat E\)。分布意义下，

\[
(\Delta_-\widehat E-A_E\widehat E)_{\mathrm{dist}}
 =
\pm(\nabla_\nu E)_{\mathrm{free}}\,\delta_\Sigma. \tag{2.5}
\]

若 \(E\) 本身有跳跃，还会有 \(\nabla\delta_\Sigma\) 项；\(C^2\) 度量接合已经排除了这一项。因而剩余障碍正是自由侧的法向一阶迹，即度量三阶 jet 所决定的**界面应力**。

若自由侧足够 \(C^3\)，又利用

\[
\operatorname{tr}E=0,\qquad \operatorname{div}E=0,
\]

以及 \(E|_\Sigma=0\) 导致其切向导数为零，可知法向或含法向指标的部分受约束；剩余独立数据可表示为

\[
\sigma=(\nabla_\nu E)^{TT}_{T\Sigma}
\in\Gamma(\operatorname{Sym}^2_0T^*\Sigma),
\]

在三维界面上是五分量的切向无迹对称张量。把整个 \(\nabla_\nu E\) 称为应力更不依赖正则性分解。

### 2.3 为什么内部极小性不自动消除它

所有可允许光滑变分在固定开 collar 上恒零，因此在 \(\Sigma\) 上具有全阶零 jet。支撑于 \(\Sigma\) 的有限阶分布不被这些变分探测。因此，紧支 stationarity/stability 本身不能推出

\[
\nabla_\nu E|_\Sigma=0. \tag{2.6}
\]

这正是“regular base stationary，所以从固定 CH collar 唯一延拓”这一推论中的缺口。固定外部问题是带强 Dirichlet 约束的四阶变分问题；自然边界应力可作为约束的 Lagrange multiplier 留下。

足以消除该项的输入包括：

1. **跨界面更高阶收敛：**固定坐标中至少 \(C^3\) 收敛。由于每个 \(g_i\) 在 collar 上完全 CH，便有 \(E_i=\nabla E_i=0\)，极限满足 (2.6)。
2. **全 regular 基底上的光滑弱方程：**证明 Euler–Lagrange 方程跨 \(\Sigma\) 分布成立且无 \(\delta_\Sigma\) 项；由 (2.5) 得 (2.6)。
3. **自由侧内部已有 CH 开集：**若 CH 开集位于允许紧支变分的区域内，则无需穿越固定/自由界面，可直接在同一 PDE 区域中唯一延拓。
4. **独立的 Dirichlet 张量强制性：**若能证明未知极限上的 Dirichlet TT 算子
   \[
   \nabla^*\nabla-2\mathring{\operatorname{Rm}}
   \]
   具有严格正下界，则 \(E|_\Sigma=0\) 和方程本身可迫使 \(E=0\)。这需要额外曲率控制或对 CH 的定量接近，不能由 \(C^2_{\rm loc}\) 极小性自动得到。

一旦界面应力消失，零延拓成为跨 \(\Sigma\) 的弱解。由 Aronszajn 型唯一延拓，

\[
E\equiv0
\]

于相连 regular 基底。因此 \(g_\infty\) 满足 \(\operatorname{Ric}=-g\)。Einstein 度量在 harmonic 坐标中实解析；它在固定开集上是 CH，所以 CH 曲率型通过解析延拓传播，regular 基底局部 CH。若存在 orbifold 点，该论证需提升到有限统一化图，并另行提供可去性。

故正确逻辑是

\[
\text{比较极小性}
\Longrightarrow
\text{自由区内部 stationarity/stability},
\]

\[
\text{奇点可去性 + 无界面应力}
\Longrightarrow
\operatorname{Ric}=-g,
\]

\[
\text{Einstein 解析性 + CH 开 germ}
\Longrightarrow
\text{局部 CH}.
\]

---

## 3. 从 \(F\ge0\) 得到精确的未恢复体积下界

相对恒等式为

\[
J(g_i)-8\pi^2q
=
\int_C F(g_i)\,dV_{g_i}-4d, \tag{3.1}
\]

其中

\[
F(g)=\frac{(s+3)^2}{3}+1+4|W^+|^2\ge0. \tag{3.2}
\]

在归一化 \(\operatorname{Ric}=-g\) 的 CH 度量上，

\[
s=-4,\qquad |W^+|^2=\frac23,
\]

所以

\[
F(g_{\mathrm{CH}})=4. \tag{3.3}
\]

假设存在绝对缺口

\[
\limsup_iJ(g_i)\le 8\pi^2q-\delta,\qquad \delta>0. \tag{3.4}
\]

令 \(\mathcal R\subset D\) 为通过单值标记、以 \(C^2_{\rm loc}\) 恢复成原 CH 度量的背景区域。对任意 \(K\Subset\mathcal R\),

\[
\int_{\Phi_i(K)}F(g_i)\,dV_{g_i}
\longrightarrow 4\,\operatorname{Vol}_{\mathrm{CH}}(K).
\]

由 \(F\ge0\)，遗漏的 neck、bubble 和未恢复区不能贡献负量，故

\[
4\,\operatorname{Vol}_{\mathrm{CH}}(K)
\le
\liminf_i\int_CF(g_i)\,dV_{g_i}.
\]

另一方面，由 (3.1)–(3.4),

\[
\limsup_i\int_CF(g_i)\,dV_{g_i}\le4d-\delta.
\]

令 \(K\uparrow\mathcal R\)，得到

\[
4\,\operatorname{Vol}_{\mathrm{CH}}(\mathcal R)
\le4d-\delta,
\]

即

\[
\boxed{
d-\operatorname{Vol}_{\mathrm{CH}}(\mathcal R)
\ge\frac{\delta}{4}.
} \tag{3.5}
\]

这里左端是背景 CH 球中未被恢复的体积，而不是 replacement 区在 \(g_i\) 下的实际体积。

对于单 blowup 的归一化

\[
j_i=\frac{J(g_i)}{2\pi^2}\le4-\varepsilon,
\]

有 \(\delta=2\pi^2\varepsilon\)，从而

\[
\boxed{
d-\operatorname{Vol}_{\mathrm{CH}}(\mathcal R)
\ge\frac{\pi^2}{2}\varepsilon.
} \tag{3.6}
\]

因此若 regular 基底恢复了 \(D\) 除有限点之外的全部 CH 度量，则恢复体积仍为 \(d\)，(3.5) 排除任何正缺口。有限点 bubbling 本身不能产生阈值以下的 \(J\)；亚阈值序列必须失去正背景体积的 CH 恢复，或逃离单值 regular convergence/orbifold completion 这一框架。

注意这里只需 \(F\ge0\)，不能把 \(F\ge1\) 用来直接增强背景“未恢复体积”结论，因为未恢复背景体积与 replacement 的实际 \(g_i\)-体积并不相同。若另有相应体积收敛或区域对应，才可增加实际 replacement-volume 项。

---

## 4. Developing-map 刚性对实双曲基底何时成立

令

\[
X=\mathbb H^4_\kappa/\Gamma
\]

为闭光滑实双曲四流形，\(\Gamma\) 无挠余紧。若采用 \(\operatorname{Ric}=-g\) 归一化，则

\[
3\kappa=-1,\qquad \kappa=-\frac13. \tag{4.1}
\]

从 \(X\) 删除有限个互不相交的嵌入闭四球，设连通外部为 \(U\)。假设：

1. \(\mathcal O\) 是连通、有效、无边界、**完备**的局部常曲率 \(\kappa\) orbifold；
2. 有光滑单射局部等距映射
   \[
   \iota:U\to\mathcal O_{\rm reg};
   \]
3. 映射保留与原外部相同的尺度；不是只给一个局部 collar germ。

则 developing-map 论证与 CH 情形相同，并且紧致性可由完备性代替。

完备局部实双曲 orbifold 可写为

\[
\mathcal O=\mathbb H^4_\kappa/\Gamma'
\]

其中 \(\Gamma'\) 离散。四维中删除有限个球不改变基本群，所以

\[
\pi_1(U)=\Gamma.
\]

局部等距的 developing map 是 \(\mathbb H^4_\kappa\) 中开集间的局部等距；常曲率刚性使其延拓为整体等距。共轭后得到

\[
\Gamma<\Gamma'.
\]

令 \(\widetilde U\) 为 \(U\) 在 \(\mathbb H^4_\kappa\) 中的提升。它连通、无界，而其补集的每个连通分量是一个有界 lifted ball。若存在 \(\gamma'\in\Gamma'\setminus\Gamma\)，\(\iota\) 的单射性迫使

\[
\gamma'\widetilde U\cap\widetilde U=\varnothing.
\]

于是连通无界集 \(\gamma'\widetilde U\) 必须包含在某个有界补集分量中，矛盾。因此

\[
\Gamma'=\Gamma.
\]

由于 \(\Gamma\) 无挠，\(\mathcal O\) 实际光滑，并与 \(X\) 全局等距，且该等距延拓给定的外部映射。

### 关键限制：Einstein 且 \(W^+=0\) 并不等于实双曲

在四维、\(\operatorname{Ric}=-g\) 时，曲率算子为

\[
\mathcal R=
\begin{pmatrix}
W^+-\frac13I&0\\
0&W^--\frac13I
\end{pmatrix}. \tag{4.2}
\]

因此 \(W^+=0\) 只固定 \(\Lambda^+\) 块。常截面曲率 \(-1/3\) 还要求

\[
W^-=0. \tag{4.3}
\]

所以 developing-map 论证**不能**原样用于仅知“负 Einstein 且 \(W^+=0\)”的 O10 基底；这样的基底未必局部实双曲，因而没有 \((\operatorname{Isom}(\mathbb H^4),\mathbb H^4)\)-结构可供上述群论论证使用。

它在以下任一条件下适用：

- 已直接证明 regular 基底局部常截面曲率 \(-1/3\)；
- 或已证明基底 Einstein，并含有与固定实双曲外部相连的实双曲开集，同时已经消除界面应力。Einstein 解析性随后把 \(W^-=0\) 从该开集传播到整个相连 regular 基底；此时 \(W^+=0\) 甚至是冗余的。

另外必须保留：

- orbifold 完备性或能推出完整 quotient developing structure 的等价条件；
- 外部映射是光滑、单射的局部等距；
- 使用整个 \(U=X\setminus\bigcup D_a^\circ\)，而非只知道一个 collar germ；
- regular completion 确为有效 orbifold，而非多层、非 Hausdorff 或非 orbifold completion。

### 实双曲背景的密度常数不同

对同一个 \(F\)，归一化实双曲背景满足

\[
s=-4,\qquad W^+=0,
\]

因而

\[
F_{\mathrm{RH}}=\frac13+1=\frac43,
\]

而 CH 上 \(F_{\mathrm{CH}}=4\)。所以 CH 的 \(\delta/4\) 恢复体积系数不能机械移植到 O10。若 O10 的相对恒等式确为

\[
J-J_{\rm top}
=
\int_C F-\frac43d,
\]

同样论证给出的背景未恢复体积下界是

\[
d-\operatorname{Vol}_{\rm RH}(\mathcal R)
\ge \frac{\delta}{4/3}
=\frac{3\delta}{4}.
\]

但其拓扑常数 \(J_{\rm top}\) 必须由 O10 自身的相对 Chern–Weil 恒等式核定，不能预设仍是 O11 的 \(8\pi^2q\)。

---

## 结论

固定外部路线中已经严格成立的是：

\[
\text{真实比较极小性}
\Rightarrow
\text{每个紧 regular 自由区上的局部极小性、stationarity、stability}.
\]

尚不能从 \(C^2\) 收敛推出的是跨固定/自由界面的张量唯一延拓。缺失对象精确为

\[
(\nabla_\nu(\operatorname{Ric}+g))_{\rm free}\,\delta_\Sigma,
\]

或其独立切向无迹部分 \(\sigma\)。需要 \(C^3\) jet 控制、无界面测度的全局弱方程、自由侧内部 CH 开集，或独立 Dirichlet 强制性中的至少一种。

与此独立地，非负相对密度已经给出完全定量的结论：

\[
J_i\le8\pi^2q-\delta
\quad\Longrightarrow\quad
\text{至少 }\delta/4\text{ 的背景 CH 体积未恢复}.
\]

因此，只要 regular 极限恢复除零测集外的整个 CH 球，就自动有

\[
\liminf_iJ(g_i)\ge8\pi^2q,
\]

无需对 bubble tree 作 APS 电荷分类。Developing-map 刚性则可原样推广到**完备局部实双曲**基底，但不能仅由“负 Einstein、\(W^+=0\)”启动；必须再得到 \(W^-=0\)，即真正的常截面曲率。
# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step82_goldberg_levelset_SW_and_symmetric_closures.md",
    "Sessions/S1003A01/workspace/notes/step81_normalized_sections_and_ddc_canonical_pairing.md",
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Sessions/S1003A01/workspace/notes/step79_second_tier_dWplus_kodaira_and_log_torsion_identity.md",
    "Sessions/S1003A01/workspace/notes/step77_goldberg_first_tier_collapse_and_canonical_curve_identity.md"
  ]
}
```

## Task

The research programme is attacking the closed negative-scalar Goldberg problem in dimension four: prove that a closed almost-Kähler Einstein 4-manifold (M,g,ω) with s<0 is Kähler, or construct a closed strictly almost-Kähler Einstein counterexample.

The attached notes record the established state.
- A complete noncompact strict AKE model exists (Bianchi VIII, W⁻=0, q>0 at finite points, ACH-type end). It satisfies every integral identity built from decaying local densities: the AAD balance, Kodaira identities, the W⁺ Bochner identity and the regularized identities. It also satisfies the Seiberg–Witten Weyl integrand estimate, with a large margin.
- Torsion zeros are forced on a closed candidate, carrying c₂(E)=5χ+6τ. Nondegenerate zeros have index +1. Finite-order jets give no local obstruction.
- The amplitude-level flux identity reduces to the coarea densities of |Y|² and |η|², and the remaining freedom is the trace-free ∇Y driven by ∂_Dv.
- Symmetric (cohomogeneity-one) closures are excluded.

Produce two or three genuinely different, mathematically concrete global arguments, or a constructive route, that could change the closed-manifold conclusion. These must not be another local integral identity or rewriting of the known balance. Each should exploit something the model provably lacks: finite volume, compactness of the zero set, the Euler class, harmonic ASD classes (b⁻≥1 is forced), canonical J-currents, or the twistor or harmonic-section viewpoint (η is the tension of J as a section of the twistor bundle). Spectral or unique-continuation input is also admissible.

For each argument:
- state the precise conjectural statement;
- explain why the model does not already satisfy its premises, or why it uses compactness essentially;
- identify the first decisive calculation, with the exact objects and formulas;
- say what result would kill it.

Partial theorems of real value, such as Goldberg under a natural weak hypothesis not covered by Sekigawa, Apostolov–Armstrong–Drăghici (W₂⁺=0, Gray conditions) or Kim (b⁻=0), are welcome if precisely formulated with a proof route. Do not invent literature; name a precise knowledge_request if a source is needed.

## Output

下面三条路线使用彼此不同的全局结构：Hodge–Hopf 拓扑、完整 Seiberg–Witten 单极子、以及 Einstein 模空间紧性。它们都不是现有积分恒等式的线性组合。

## 一、Hodge–Hopf 刚性：把扭率零点的 Euler 荷转化为调和 ASD 二形式不可能携带的 Hopf 荷

记 \(H\) 为二形式的调和投影。Kim 公式给出
\[
|\gamma^-|^2=\frac{q^2}{32},
\qquad
\|H\gamma^-\|_2^2=4\pi^2\|c_1^-\|^2,
\]
因而有精确正交分解
\[
\boxed{\;
\frac1{32}\int_Mq^2-4\pi^2\|c_1^-\|^2
=\|\gamma^--H\gamma^-\|_2^2 .
\;} \tag{H}
\]

### 精确猜想

**Hodge–Hopf 猜想。** 若闭 AKE Einstein 四流形满足 \(s<0\)、\(\gamma^-\) 调和，且扭率零点均为具有孤立齐次主部的有限阶零点，则 \(q\equiv0\)。

一个立即有价值的特例是：所有扭率零点非退化时，\(\gamma^-\) 调和应当推出 Kähler。这一假设既不是 \(W_2^+=0\)，也不是 Gray 型条件或 \(b^-=0\)。

### 核心机制

在 \(M\setminus Z\) 上定义单位 ASD 二形式
\[
n_\alpha=\frac{4\sqrt2}{q}\gamma^- \in S(\Lambda^-).
\]
在适配酉标架中，\(n_\alpha\) 正是单位扭率
\[
\widehat\alpha=\frac{\alpha}{|\alpha|}\in S(E)\cong S^3
\]
经过标准 Hopf 映射 \(S^3\to S^2\) 的像。若 \(p\) 是非退化扭率零点，则
\[
\operatorname{Hopf}\!\left(n_\alpha|_{S^3_\rho(p)}\right)
=\operatorname{ind}_p(\alpha)=+1.
\]
总 Hopf 荷因此等于
\[
\sum_p\operatorname{ind}_p(\alpha)=c_2(E)=5\chi+6\tau.
\]

若 \(\gamma^-\) 调和，则在 \(p\) 附近的首个非零齐次项
\[
P_k=\sum_{j=1}^3P_{k,j}(x)\,\Omega_j^-
\]
必须满足平坦首阶方程
\[
dP_k=0,\qquad d^*P_k=0.
\]
另一方面，\(P_k\) 不是任意 Maxwell 多项式，而具有特殊二次复合形式
\[
P_k=Q(A_m),
\]
其中 \(A_m\) 是 \(\alpha\) 的首个齐次项，\(Q:\mathbb C^2\to\mathbb R^3\) 是 Hopf 二次映射，且 \(k=2m\)。

第一个决定性计算就是有限维代数问题：

\[
\boxed{\;
d\,Q(A_m)=0,\quad
Q(A_m)^{-1}(0)=\{0\},\quad
\deg(\widehat A_m)>0
\;}
\tag{MH}
\]
是否存在非零解？

对非退化零点只需处理 \(m=1\)：把 Step 62 的全部允许线性锥
\[
A_1(x)=Bx+c\bar x
\]
代入 \(dQ(A_1)=0\)，比较所有一次多项式系数。这是一个精确的符号线性系统，随后只需与锥约束及 \(\det_{\mathbb R}A_1>0\) 联立。若无解，便得到上述非退化零点版本。高阶情形是同一个表示论问题在 \(\operatorname{Sym}^m(\mathbb R^4)^*\otimes\mathbb C^2\) 上的推广。

### 为什么完整模型不参与

Bianchi–VIII 模型在每个有限点都有 \(q>0\)，没有小三球上的 Hopf 荷；它也没有闭流形上的 \(c_2(E)\) 总荷和调和投影公式 (H)。其端部可以吸收二级 Chern–Simons 量。

### 推翻方式

任意一个显式多项式
\[
P=Q(A_m),\qquad dP=0,
\]
若具有孤立零点且 \(P/|P|:S^3\to S^2\) 的 Hopf 数为正，就会推翻核心局部命题。更直接的是构造一支调和 ASD 二形式，其孤立零点正好具有这种 Hopf 型首项。

尚需的资料主题是：

`knowledge_request: local zero topology of harmonic self-dual or anti-self-dual two-forms in four dimensions; homogeneous polynomial solutions of dφ=0 with *φ=-φ; Hopf invariants of isolated zeros of Maxwell fields.`

---

## 二、保留完整 Taubes 单极子：寻求反向 Hodge 不等式，而不是继续使用标量 Weyl 估计

设 \(b^+>1\)，\(T\) 为典范 Taubes 流。已有精确公式
\[
D_K:=T_{\rm AK}-\int_M|\eta|^2
=2\pi\int_T|a^\perp|^2\,dA\ge0.
\]

### 精确猜想

存在普适常数 \(c_{\rm SW}>0\)，使每个闭 AKE Einstein 四流形满足
\[
\boxed{\;
4\pi^2\|c_1^-\|^2-\frac1{32}\int_Mq^2
\ge c_{\rm SW}D_K .
\;} \tag{SW-H}
\]

但由 (H)，左侧恰为
\[
-\|\gamma^--H\gamma^-\|_2^2\le0.
\]
因此 (SW-H) 会同时给出
\[
D_K=0,\qquad \gamma^-=H\gamma^-.
\]
再与第一条路线的 Hodge–Hopf 刚性结合，即得到 \(q=0\)。在 \(b^+=1\) 情形，同一陈述可放在存在典范 chamber 单极子或实际典范流的前提下。

### 第一个决定性计算

使用由 \(J\) 给出的 Spin\(^c\) 分解
\[
S^+=\Lambda^{0,0}\oplus\Lambda^{0,2},
\]
令 \(\Psi_0=(1,0)\) 为单位典范旋量。其投影类对应 \(u=\omega/\sqrt2\)。Hopf 微分给出精确关系
\[
\left|\Pi_{\Psi_0^\perp}\nabla_{A_c}\Psi_0\right|^2
=\frac14|\nabla u|^2=\frac q8. \tag{P}
\]

对 Taubes 的大参数解 \((A_r,\Psi_r)\)，令
\[
\widehat\Psi_r=\frac{\Psi_r}{|\Psi_r|},\qquad
a_{B,r}=-\operatorname{Im}
\langle\widehat\Psi_r,\nabla_{A_r}\widehat\Psi_r\rangle .
\]
Berry 曲率恒等式为
\[
da_{B,r}
=
-\operatorname{Im}
\langle\Pi^\perp\nabla_{A_r}\widehat\Psi_r
\wedge
\Pi^\perp\nabla_{A_r}\widehat\Psi_r\rangle
-\operatorname{Im}
\langle\widehat\Psi_r,R^{S^+}_{A_r}\widehat\Psi_r\rangle .
\tag{B}
\]
同时 Dirac–Weitzenböck 公式是
\[
0=\int_M\left(
|\nabla_{A_r}\Psi_r|^2+\frac s4|\Psi_r|^2
+\frac12\langle\rho(F_{A_r}^+)\Psi_r,\Psi_r\rangle
\right)dV. \tag{W}
\]

计算的实质是把 (B)、(W) 与 Taubes 曲率方程联立，并减去由 (P) 产生的体项 \(q|\Psi_r|^2/8\)。在 \(r\to\infty\) 时：

* 远离 \(T\)，投影旋量趋向 \([\Psi_0]\)，体项按 (P) 精确抵消；
* 管状层中的曲率收敛到 \(2\pi[T]\)；
* 与 \(\beta=\gamma-\frac s4\omega\) 的配对应产生
  \[
  2\pi\int_T|a^\perp|^2=D_K;
  \]
* ASD 曲率的 Hodge 极小化产生
  \[
  \|\gamma^--H\gamma^-\|_2^2.
  \]

所需的关键结果，是有限项中 \(D_K\) 具有严格正系数，而其余项是平方或可由 Einstein 方程消去。标量 SW Weyl 估计在推导中丢掉了投影旋量能量，因而看不到这一项。

### 为什么完整模型不参与

该模型没有闭流形上的典范基本类、Taubes 单极子序列、典范流 \(T\) 或 \(c_1^-\) 的 Hodge 极小化。其满足标量 Weyl 估计并不涉及 (B) 中的 Berry 曲率量子化。

### 推翻方式

若大参数展开表明 \(D_K\) 的有限项系数为零或符号相反，或者最终仍留下可取两种符号的 \(\bar\partial_Dv\)、\(\eta^TV\eta\) 项，那么 (SW-H) 不成立。一个局部 Taubes 涡旋剖面若已经产生这种符号，也足以终止这条机制。

所需资料主题是：

`knowledge_request: first correction in the Taubes large-r expansion on an almost-Kähler four-manifold; Berry curvature of the canonical spinor line; equality terms discarded in LeBrun's monopole curvature estimates.`

---

## 三、小缺陷紧性与非 Kähler 分岔：既给出间隙定理，也提供闭反例的构造入口

归一化 \(s=-12\)。固定 \(M\) 及 almost-complex 同伦类，并写
\[
T_i=T_{\rm AK}(g_i,\omega_i).
\]

### 精确陈述

设一列闭 AKE Einstein 结构满足

\[
\operatorname{Vol}_{g_i}B_r(x)\ge\nu r^4
\quad(0<r\le1),\qquad
\operatorname{diam}(M,g_i)\le D.
\]

再假设所有可能出现的 Kähler–Einstein orbifold 极限，在 Einstein–调和自对偶形式耦合变形复形中没有非 Kähler 法向 Jacobi 场。则存在
\[
\varepsilon=\varepsilon(M,\nu,D)>0
\]
使
\[
T_{\rm AK}<\varepsilon\quad\Longrightarrow\quad q\equiv0.
\tag{G}
\]

这给出一个不依赖点态 Weyl 夹逼的小缺陷间隙。反过来，若某个紧 Kähler–Einstein orbifold 存在可积的非 Kähler 法向 Jacobi 场，则 Lyapunov–Schmidt 分岔可能产生无对称性的闭严格 AKE Einstein 结构。

### 紧性计算

由
\[
T_i=\int\left(\operatorname{tr}V_i^2+\frac3{32}q_i^2\right)
\]
立刻得到
\[
\int q_i^2\le\frac{32}{3}T_i,\qquad
\int\operatorname{tr}V_i^2\le T_i.
\]
拓扑恒等式
\[
144V_i=32\pi^2c_1^2+16T_i
\]
给出统一体积。于是
\[
Q_i\le V_i^{1/2}\|q_i\|_2\longrightarrow0,
\]
再由
\[
\frac{12}{16}Q_i=\int|\eta_i|^2+T_i
\]
可得
\[
\|\eta_i\|_2\longrightarrow0.
\]

固定拓扑下，Einstein Gauss–Bonnet 公式控制 \(\int|{\rm Rm}|^2\)。非塌缩和直径条件给出 orbifold 紧性。极限之外的每个曲率泡经缩放后仍带有闭、单位长度、自对偶二形式；而
\[
\int q_i^2\to0
\]
在每个泡上迫使该二形式平行。因此所有泡都是标量平坦 Kähler 泡，主极限也是 Kähler–Einstein orbifold。严格几何只能来自该极限附近的耦合分岔。

### 第一个决定性计算：耦合线性化

在光滑 Kähler–Einstein 点 \((g_0,\omega_0)\) 处，对变分 \((h,\sigma)\)，Bianchi 规范下的线性系统是
\[
L_Eh=0,\qquad B_{g_0}h=0,
\]
\[
d\sigma=0,
\]
\[
(1-*_{g_0})\sigma=\dot *_{h}\omega_0,
\]
\[
2\langle\sigma,\omega_0\rangle
-\langle h,\omega_0\circ\omega_0\rangle=0.
\tag{L}
\]
这里 \(L_E\) 是 \(\operatorname{Ric}+3g\) 的规范固定线性化。解空间中由复结构与 Kähler 类变形产生的部分仍满足 \(\nabla\omega=0\)；真正构造闭严格结构所需的是一个与这些方向正交的解 \((h,\sigma)\)。

若 (L) 的法向核为空，解析隐函数理论给出局部 Kähler 刚性。若法向核非零，则二阶 Kuranishi 映射
\[
\mathcal K_2(h,\sigma)
\]
成为首个构造计算；其投影到 Einstein 算子余核和常长度方程余核必须同时为零。这个计算可在具体 Kähler–Einstein 曲面或 orbifold 上用 Laplace 谱与张量分解完成，不需要任何 cohomogeneity-one 假设。

### 为什么完整模型不参与

Bianchi–VIII 模型体积无穷、直径无穷，也不收敛到紧 Kähler–Einstein orbifold。其低扭率区域沿 ACH 端部扩张，正是上述紧性机制所排除的现象。

### 推翻方式与构造信号

* 若存在 \(T_i\to0\) 的闭严格序列，其几何沿长颈塌缩而无法形成上述 orbifold 图景，则无附加几何输入的普适小缺陷间隙不成立。
* 若 (L) 出现非 Kähler 法向核，且全部有限维 Kuranishi 阻碍消失，它会直接给出最可信的无对称闭反例构造路线。
* 若所有 \(s<0\) 的紧 Kähler–Einstein 极限都只有 Kähler 型 Jacobi 场，则闭反例不能从小缺陷分岔产生；任何严格例子必须保持 \(T_{\rm AK}\) 远离零并进入强曲率区域。

所需资料主题是：

`knowledge_request: Einstein orbifold compactness in dimension four under noncollapse and L2 curvature control; Koiso-type decomposition of infinitesimal Einstein deformations for Kähler–Einstein surfaces with s<0; coupled variation of a constant-length harmonic self-dual form; orbifold Kuranishi theory for this coupled system.`

这三条路线之间有明确连接：第二条若给出反向 Hodge 估计，便把问题送入第一条的 Hopf 零点刚性；第三条则处理 \(T_{\rm AK}\to0\) 的整个退化区，并把闭反例问题压缩为一个可计算的耦合谱分岔问题。
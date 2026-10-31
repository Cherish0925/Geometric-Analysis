# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step2_blowup_cell_problem_O11.md",
    "Sessions/S1003A02/workspace/notes/step1_field_compatibility_and_route_portfolio.md",
    "Skills/geometric-analysis/references/results-and-questions.md",
    "Skills/geometric-analysis/references/conventions-and-literature.md",
    "Skills/geometric-analysis/research/paper/sections/variational_geometry.tex"
  ]
}
```

## Task

Goal: decide the balanced first-order Einstein-gap coefficient (O11): is inf_g P = 8 pi^2 Q + o(Q) on X_j # k CP2bar # l (S^1 x S^3) over complex-hyperbolic covers X_j, where P = int |Ric0|^2? The note reduces this exactly to the functional 4(W_+ - (4/3)pi^2 A) + (S-32pi^2A)/12 and to a local cell problem P(U) = 8pi^2 + 4 Delta W_+ + Delta S/12; U(2)-invariant cells numerically always cost more than 8pi^2, with first-order penalty 8pi^2*6x0 (x0 = exceptional area/pi, Ric=-6g). Generate the strongest mathematical routes to (a) a proof, without symmetry, that every small perturbation of a scaled Burns bubble glued into a complex-hyperbolic (or Kahler-Einstein) background pays P >= 8pi^2(1 + c x0) - o(x0) with c>0 — identify the exact boundary pairing (Kahler mass of Burns times background curvature), the function spaces, and whether the Seiberg-Witten/Kahler-calibration structure gives the local inequality Delta W_+ >= 0; (b) genuinely different competitor cells that could beat 8pi^2 non-perturbatively: toric/T^2 multi-blowup clusters, LeBrun hyperbolic-ansatz scalar-flat metrics, non-Kahler ASD-like bubbles adapted to a negatively curved background, cells containing necks, and cells combining a blowup with a handle (relevant since the balanced family has k/Q=2/9, l/Q=7/36 and its lower bound uses the opposite chirality through U=3min(T+,T-)/A). For each, give a concrete computable test (ansatz, reduced functional, expected signal) and what result would refute coefficient 4. Also say whether the local inequality Delta W_+ >= 0 for all cells could be FALSE, and propose the cheapest construction testing it. Do not invent literature; name precise knowledge requests if needed.

## Output

设一个复合胞腔 \(U\) 携带 \(k_U\) 个 blow-up 与 \(\ell_U\) 个 handle，并与复双曲球 \(B\) 在外沿邻域完全一致。记
\[
q_U=k_U+4\ell_U,\qquad
\mathfrak e(U):=P(U)-8\pi^2q_U.
\]
相对 Chern–Weil 恒等式给出
\[
\boxed{\mathfrak e(U)
 =4\left[\int_U|W^+|^2-\int_B|W^+|^2\right]
 +\frac1{12}\left[\int_Us^2-\int_Bs^2\right].}
\]
因此任何固定胞腔满足 \(\mathfrak e(U)<0\)，都足以推翻系数 \(4\)：在固定球商的高阶覆盖中，一个嵌入球的所有提升彼此分离，而 \(Q_j=o(A_j)\)，所以可在 \(O(Q_j)\) 个位置复制同一胞腔。若胞腔的 \((k_U,\ell_U)\) 比例不等于平衡比例，可同标准胞腔混合。反过来，小 Burns 泡附近的正一阶项只控制恢复邻域；要覆盖所有度量，还需要全局同场不等式，或证明低 \(P\) 近极值度量自动分解为复双曲主体和有限能量胞腔。

## 一、小 Burns 泡的无对称扰动：应有的精确展开

令 \(t=x_0=\operatorname{Area}(E)/\pi\)，背景为 Kähler–Einstein 四流形
\[
\operatorname{Ric}_{g_0}=\lambda g_0,\qquad \lambda<0.
\]
在复双曲归一化 \(\lambda=-6\) 下，数值结果对应
\[
P(U_t)=8\pi^2+48\pi^2t+o(t)
      =8\pi^2(1+6t)+o(t).
\]

### 1. 界面配对的精确值

把单位 Burns 度量写在 \(Z=\operatorname{Bl}_0\mathbb C^2\) 上，其无穷远展开为
\[
g_B=\delta+H_{-2}+O(r^{-4}),\qquad H_{-2}=O(r^{-2}),
\]
并用
\[
m_K:=\frac{\operatorname{Area}(E)}{\pi}
\]
定义 Kähler 质量归一化。背景在 \(p\) 点的正规坐标二阶项为
\[
(Q_2)_{ij}(y)=-\frac13R_{ikjl}(p)y^ky^l.
\]
缩放 \(x=\sqrt t\,y\) 后，背景在泡尺度上成为
\[
g_0(\sqrt t\,y)=\delta+tQ_2(y)+O(t^{3/2}|y|^3).
\]
决定一阶能量的正是 \(H_{-2}\) 与 \(Q_2\) 的 Green 配对。

令
\[
\mathcal D h=
\left(2(DW^+)_{g_B}h,\frac1{\sqrt{12}}(Ds)_{g_B}h\right)
\]
并在 Bianchi 切片
\[
\beta_{g_B}h=0
\]
上工作。由
\[
\int_{\Omega_R}\left(
 \langle \mathcal Dh,\mathcal Dk\rangle
 -\langle h,\mathcal D^*\mathcal Dk\rangle\right)
 =\int_{S_R}\mathbf G_{\mathcal D}(h,k)
\]
定义 Green 三形式 \(\mathbf G_{\mathcal D}\)。Burns–背景配对为
\[
\mathfrak B_p(H_{-2},Q_2)
 :=\lim_{R\to\infty}\int_{S_R}
       \mathbf G_{\mathcal D}(H_{-2},Q_2),
\]
其中还应加入相对 Chern–Weil transgression 的同一归一化；两者合并后的不变量值是
\[
\boxed{
\mathfrak B_p
 =-8\pi^2\lambda\,m_K
 =-2\pi^2s_{g_0}(p)m_K
 =-2\pi s_{g_0}(p)\operatorname{Area}(E).
}
\]
对 \(\lambda=-6\) 和 \(m_K=t\)，这正是 \(48\pi^2t\)。

这个值可由两步严格确定：

1. \(H_{-2}\) 是 \(U(2)\)-不变质量模，故其与 Kähler–Einstein 曲率二阶项的线性配对只能取背景标量曲率分量；反自对偶 Bochner 曲率与无迹 Ricci 分量在表示分解下不贡献。
2. 常数由已完成的 \(U(2)\) Kähler 计算校准。因该配对只依赖两端的渐近系数，而不依赖插值方式，校准得到的常数适用于无对称匹配。

等价地，对于任意 Kähler–Einstein 背景，
\[
P(U_t)=8\pi^2-8\pi^2\lambda t+o(t).
\]
在 Kähler 子类中还可分解为
\[
\Delta S=-32\pi^2\lambda t+o(t),\qquad
\Delta W_+=-\frac43\pi^2\lambda t+o(t),
\]
因为 \(|W^+|^2=s^2/24\)。当 \(\lambda=-6\) 时，
\[
\frac{\Delta S}{12}=16\pi^2t,\qquad
4\Delta W_+=32\pi^2t.
\]

### 2. 合适的加权空间与核分解

在固定 Burns 空间上可采用
\[
\|h\|_{C^{2,\alpha}_\delta}
 =\sum_{j=0}^2\sup_Z
   \langle r\rangle^{j-\delta}|\nabla^jh|
 +[\langle r\rangle^{2+\alpha-\delta}\nabla^2h]_\alpha,
\]
以及尺度不变的加权能量范数
\[
\|h\|_{H^2_\delta}^2
 =\sum_{j=0}^2
  \int_Z\langle r\rangle^{2(j-\delta)-4}
             |\nabla^jh|^2\,d\mu_{g_B}.
\]
权重取
\[
-2<\delta<0
\]
并避开 \(\mathcal D^*\mathcal D\) 的 indicial 集。质量模 \(r^{-2}\) 由固定 \(\operatorname{Area}(E)\) 单独处理；泡中心、欧氏转动和坐标变化通过标记点及 Bianchi 切片固定。背景增长模 \(tQ_2\) 不放入衰减空间，而作为显式匹配项分离。

自然二次型为
\[
\mathcal Q_B(v)
 =\int_Z\left(
 4|(DW^+)_{g_B}v|^2+\frac1{12}|(Ds)_{g_B}v|^2
 \right)d\mu_{g_B}.
\]
因 Burns 满足 \(W^+=s=0\)，这就是
\[
\int(4|W^+|^2+s^2/12)
\]
在 Burns 点的 Hessian 二次型。所需谱结论是：在 Bianchi 切片上，固定面积、中心和渐近标架之后，
\[
\mathcal Q_B(v)\ge c_0\|v\|_{H^2_\delta}^2
\]
对所有与有限维 Jacobi 核正交的 \(v\) 成立。若还存在非平凡的 scalar-flat ASD Jacobi 模，则须作 Lyapunov–Schmidt 化约，并计算质量映射在该模空间上的变化；仅有二次型半正性还不够。

最关键的源资料需求是：

- Burns 度量上 \((DW^+,Ds,\beta)\) 加权形变复形的核与余核；
- 权重 \((-2,0)\) 内所有 Jacobi 模的几何来源；
- 固定 exceptional area 后，附近 scalar-flat ASD ALE 度量是否只有坐标、中心和尺度模；
- Burns Kähler 质量在这些模上的一阶变化。

### 3. 预期的完整能量展开

把一般近 Burns 胞腔在调制后写成
\[
g_t=g_t^{\mathrm{app}}+v.
\]
应建立
\[
\mathfrak e(U_t)
 =t\mathfrak B_p+\mathcal Q_B(v_\perp)
   +t\mathcal L_p(v_\perp)+\mathcal R_t(v),
\]
并有
\[
|\mathcal L_p(v_\perp)|
 \le C\,\mathcal Q_B(v_\perp)^{1/2},
\]
\[
|\mathcal R_t(v)|
 \le \eta\,\mathcal Q_B(v_\perp)+o(t)+Ct^2.
\]
完成平方后，
\[
\mathcal Q_B+t\mathcal L_p\ge-Ct^2,
\]
从而
\[
\boxed{
P(U_t)\ge
8\pi^2-8\pi^2\lambda t-o(t).
}
\]
在 \(\lambda=-6\) 时即
\[
P(U_t)\ge8\pi^2(1+6t)-o(t).
\]

若利用 Kähler 正规坐标的奇偶性、Burns 的 polyhomogeneous 展开以及匹配半径 \(r\sim t^{1/4}\)，更精细的余项形态很可能是
\[
O(t^2|\log t|),
\]
但这一阶数要从各个 \(r^{-4}\)、背景四阶项和 cutoff 交叉项逐项推出，不能只由尺度分析断定。

### 4. Seiberg–Witten 与 Kähler 校准实际能给什么

若胞腔与复双曲球在外沿邻域一致，把它与 \(X\setminus B\) 拼接得到 \(X\#\overline{\mathbb{CP}}^2\)。全局实际 monopole 类给出
\[
S(g)\ge32\pi^2A=S(g_X),
\]
故对这种可植入胞腔有精确结论
\[
\boxed{\Delta S\ge0.}
\]
在 Kähler 胞腔中，
\[
4\Delta W_++\frac{\Delta S}{12}
 =\frac{\Delta S}{4},
\]
Hodge 指标估计进一步产生上面的正质量一阶项。因此 Kähler、toric Kähler、scalar-flat Kähler core 加 Kähler 插值都不能降低 \(8\pi^2\)。

但一般胞腔的
\[
\Delta W_+\ge0
\]
并不成立。供应材料中的 Malchiodi–Malizia 严格 Weyl 降低已经给出强烈且几乎直接的反例机制。设
\[
\delta\mathcal W_{\mathrm{op}}
 :=(W_++W_-)_{\#}-
   (W_++W_-)_{X}-(W_++W_-)_{\overline{\mathbb{CP}}^2}<0.
\]
signature 可加性给出
\[
\delta(W_+-W_-)=0,
\]
因而
\[
\boxed{
\delta W_+=\delta W_-=
\frac12\delta\mathcal W_{\mathrm{op}}<0.
}
\]
反向 Fubini–Study 因子的 \(W^+\) 为零，所以连接和度量的 \(W^+\) 严格低于复双曲因子。只要原构造的改动可收纳在一个接合邻域内，这就是 \(\Delta W_+<0\) 的胞腔。平滑逼近保留严格符号。

因此真正可能成立的局部式不是 \(\Delta W_+\ge0\)，而是联合补偿
\[
\boxed{\Delta S+48\Delta W_+\ge0,}
\]
或其小泡定量版本。Seiberg–Witten 标量式给出第一项的符号，Burns Hessian 给出近泡联合补偿；现有全局 Weyl–标量平方估计本身不足以推出该式。

测试 \(\Delta W_+\ge0\) 最省成本的两种方式是：

1. 直接从严格总 Weyl 接合值利用 signature 恒等式取一半，无需另算两种手征曲率；
2. 在现有 \(U(2)\) 代码中把目标从 \(P\) 攓为 \(W_+\)，或等价地最小化 \(W_-\)，因为一 blow-up 胞腔满足
   \[
   \Delta W_+=\Delta W_--12\pi^2.
   \]
   找到 \(W_-(U)<W_-(B)+12\pi^2\) 即得到 \(\Delta W_+<0\)。这并不自动降低 \(P\)，还要比较标量代价。

## 二、最有区分力的非微扰胞腔

### A. 严格 Weyl 接合作为联合 \(P\) 测试

这是离现有材料最近的非 \(U(2)\) 竞争者。设接合参数为 \(a\)，定义
\[
\Theta(a)
 =4\Delta W_+(a)+\frac{\Delta S(a)}{12}.
\]
决定性信号是
\[
\Theta(a)<0.
\]
即使 \(\Theta(a)\) 只比零小 \(10^{-10}\)，只要选定一个固定 \(a>0\) 并可在覆盖中重复，该固定每点节省仍会改变一阶系数。

Weyl 项已知严格为负；未知量是同一度量上的标量项。一个非常便宜而又精确的改进是固定接合度量 \(g_a\)，只在胞腔内部改变共形因子。对
\[
\widetilde g=u^2g_a,\qquad u\equiv1
\]
于外沿邻域，有
\[
W_+(\widetilde g)=W_+(g_a),
\]
而
\[
S(u^2g_a)
 =\int u^{-2}(6\Delta_{g_a}u+s_{g_a}u)^2\,d\mu_{g_a}.
\]
因此可最小化这个单一四阶泛函。其 Euler 方程为
\[
(6\Delta+s)\left[
 u^{-2}(6\Delta u+su)\right]
-u^{-3}(6\Delta u+su)^2=0,
\]
配以 \(u=1\) 于一条外沿 collar，并保持 \(u>0\)。若最小值满足
\[
\Delta S_{\min}(a)<-48\Delta W_+(a),
\]
则得到真实的 \(P(U)<8\pi^2\) 胞腔。若小 \(a\) 展开总是
\[
\Theta(a)=48\pi^2t(a)+o(t(a))>0,
\]
则它与 Burns 配对完全一致，Weyl 节省被标量项以更大的一阶量抵消。

所需源资料是 2025 接合中 \(a^4\) 相互作用常数、两种手征的方向约定、度量在接合邻域外是否与原度量完全一致，以及其标量曲率在同一坐标展开中的首项。

### B. \(T^2\)-不变多 blow-up 簇

Kähler toric 类本身不会取胜。若
\[
g=u_{ij}\,d\mu_i d\mu_j+u^{ij}\,d\theta_i d\theta_j
\]
来自 symplectic potential \(u\)，则 Abreu 公式给出
\[
s=-\partial_i\partial_j u^{ij},\qquad
|W^+|^2=\frac{s^2}{24},
\]
于是
\[
\mathfrak e(U)=\frac{\Delta S}{4}\ge0.
\]

真正的新自由度来自一般正交可迁 \(T^2\) 度量
\[
g=G_{ab}(y)\,dy^ady^b+
H_{ij}(y)\bigl(d\theta^i+A^i_a\,dy^a\bigr)
          \bigl(d\theta^j+A^j_b\,dy^b\bigr),
\]
其中 \(G,H\) 是独立正定矩阵场。rod vectors 和新增的 \((-1)\)-facets 编码多个 exceptional sphere；外沿 collar 固定为复双曲球的 toric 数据。若角变量周期为 \(2\pi\)，约化泛函为
\[
P=(2\pi)^2\int_{\mathcal P}
 |\operatorname{Ric}^\circ(G,H,A)|^2
 \sqrt{\det G\,\det H}\,d^2y.
\]

首个有价值的模型是两个相邻 \((-1)\)-facet，变量包括：

- 两 exceptional areas；
- 两中心间距；
- facet 夹角及 rod 数据；
- 非 Kähler 模 \(H-G^{-1}\)；
- 连接曲率 \(dA\)。

小尺寸簇的一阶配对只看到总 Kähler 质量，因复双曲曲率在 \(U(2)\) 下各向同性，故预期仍为
\[
-8\pi^2\lambda\sum_i t_i>0.
\]
真正可能的新现象出现在簇直径与背景曲率半径同阶，或非 Kähler 模使有效质量张量脱离正标量模。决定性信号是
\[
\frac{P(U_m)}{8\pi^2m}<1
\]
且差值在网格加密、外沿 collar 加宽后保持。任意固定 \(m\) 的严格下降即可在平衡族中复制。

### C. LeBrun 双曲 ansatz

可采用双曲 monopole 表示
\[
V=1+\sum_{\alpha=1}^mG_{p_\alpha},\qquad
d\theta=*_{H^3}dV,
\]
以及文献中的精确共形因子，把
\[
Vg_{H^3}+V^{-1}\theta^2
\]
变成 scalar-flat Kähler 或自对偶度量。monopole 位置 \(p_\alpha\) 控制 exceptional 配置和无穷远多极矩。

这里有三个独立计算：

1. 从圆作用固定点和交矩阵确定所得紧致片段在选定定向下确实携带 \(m\) 个 \((-1)\)-类；
2. 计算无穷远 \(r^{-2}\) 质量项和 \(r^{-3},r^{-4}\) 多极项；
3. 截断后用非 Kähler collar 与复双曲球匹配，再计算
   \[
   \mathfrak e=4\Delta W_++\Delta S/12.
   \]

若整个胞腔保持 Kähler，前述 \(\Delta S/4\) 机制排除节省。因此 LeBrun 度量的价值主要是提供显式 scalar-flat ASD 核心，而最优化自由度放在外部非 Kähler collar。共线 monopoles 给出 \(U(1)^2\) 约化，三维积分可进一步降为二维数值积分。

决定性信号不是核心的 \(W^+=s=0\)，而是匹配完成后
\[
\mathfrak e(U_m)<0.
\]
小簇若只有正的总质量，仍会支付 Burns 型正一阶项；更有希望的是可调多极矩在有限尺寸产生强相互作用。

需要精确检索：

- LeBrun 双曲 monopole 度量的定向、紧致化拓扑和交矩阵；
- scalar-flat Kähler 版本的共形因子；
- 无穷远质量及多极展开；
- 多中心参数退化时的 orbifold 与光滑解析。

### D. 非 Kähler、ASD-like 泡

从泛函结构看，理想核心满足
\[
s=0,\qquad W^+=0,
\]
因为此时
\[
4|W^+|^2+s^2/12
\]
在核心完全消失。Burns 只是其中的 Kähler 点。若存在同一拓扑上的非 Kähler scalar-flat ASD ALE 族，其质量张量可与背景曲率形成不同符号的配对。

最便宜的线性测试是在 Burns 上求解
\[
(DW^+)h=0,\qquad (Ds)h=0,\qquad \beta h=0
\]
并读取 \(h\) 的 \(r^{-2}\) 系数。若固定 exceptional area 后存在真实非规范模，定义其有效质量
\[
m_{\mathrm{eff}}(h)
\]
使一阶相互作用为
\[
-8\pi^2\lambda m_{\mathrm{eff}}.
\]
若某个可积模给出 \(m_{\mathrm{eff}}<0\)，则 \(\lambda<0\) 时小尺度相互作用立刻朝低于 \(8\pi^2\) 的方向移动。若所有可积模都满足 \(m_{\mathrm{eff}}>0\)，Burns 一阶正项具有更强普适性。

另一条计算路线是先取一个 \(\Delta W_+<0\) 的 ASD-like 种子，再用上面的共形四阶问题最小化标量能量。共形变化保持 \(W_+\) 能量不变，因此这能把“Weyl 降低”与“标量是否足够便宜”完全分开。

这里需要的源资料是 O\((-1)\) 上 scalar-flat ASD ALE 度量的局部模空间，以及非 Kähler ALE 质量的正性定理究竟需要哪些复结构、标量符号和 spin 假设。

### E. 含内部 neck 的单 blow-up 胞腔

现有 \(x=b^2\) 参数化排除了 \(b\) 非单调。完整 biaxial Bianchi IX 形式
\[
g=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)
     +c(t)^2\sigma_3^2
\]
允许 \(a'\) 改变符号、多个喉部和长 Einstein-like 段。bolt 光滑条件由
\[
c(0)=0,\qquad a(0)>0,\qquad a'(0)=0
\]
及圆纤维周期决定；外端固定到复双曲球的二阶 jet。目标泛函是
\[
P=2\pi^2\int a^2c\,|\operatorname{Ric}^\circ(a,c)|^2\,dt.
\]
它是一个两函数四阶变分问题，可直接用 automatic differentiation 和谱基求解，不再使用 \(x=a^2\) 作全局坐标。

可能的节省机制是：过渡不在单一 annulus 中完成，而由两个曲率较小的过渡和一段近 Einstein neck 分担。四维曲率能量尺度不变，所以单纯拉长圆柱通常不便宜；真正需要的是
\[
\operatorname{Ric}_{tt}\approx
\operatorname{Ric}_{\sigma_1}\approx
\operatorname{Ric}_{\sigma_3}
\]
在 neck 主体同时成立。

决定性信号是一个满足 bolt 与外端匹配的解具有
\[
P<8\pi^2.
\]
若所有非单调分支都回到 \(P>8\pi^2\)，则会显著加强单 blow-up 胞腔的非微扰证据。

### F. blow-up 与 handle 的复合胞腔

平衡比例满足
\[
\frac{k}{\ell}\longrightarrow\frac87.
\]
因此自然的基本超胞腔携带
\[
(k_U,\ell_U)=(8,7),\qquad q_U=36.
\]
更小的探索单元可先取一个 blow-up 与一个 handle；七个这种单元再加一个单 blow-up，正好给出 \((8,7)\)。

handle 可由在同一复双曲球内部挖去两个小球并接入 warped bridge 构造。对
\[
g=dt^2+a(t)^2g_{S^3}
\]
有
\[
|\operatorname{Ric}^\circ|^2
 =3\frac{\bigl((a')^2-1-aa''\bigr)^2}{a^4},
\]
从而
\[
\boxed{
P_{\mathrm{bridge}}
 =6\pi^2\int
 \frac{\bigl((a')^2-1-aa''\bigr)^2}{a}\,dt.
}
\]
这个一维泛函可与 Burns/Bianchi IX 核心通过共同的 \(S^3\) jet 耦合。纯 handle 的全局结果表明标准每个 handle 代价为 \(32\pi^2\)，但 blow-up 与 handle 共居一个胞腔时，两个过渡区可共享曲率，且 handle 的 signature 为零，可能同时改变 \(W_+\) 与 \(W_-\)。

对携带 \((k_U,\ell_U)\) 的复合胞腔应同时记录
\[
\Delta(W_+-W_-)=-12\pi^2k_U.
\]
因此
\[
\Delta W_+=\Delta W_--12\pi^2k_U.
\]
handle 可能通过降低 blow-up 所需的 \(W_-\) 代价来间接降低 \(W_+\)，这正与平衡族中 opposite chirality 的作用相呼应。

决定性信号分别是
\[
P(U_{1,1})<40\pi^2
\]
或更直接地
\[
P(U_{8,7})<8\pi^2\cdot36.
\]
若
\[
P(U_{1,1})=8\pi^2(5-\delta),
\]
则七个复合单元加一个标准 blow-up 给出每个平衡超胞腔节省
\[
7\delta\cdot8\pi^2,
\]
足以改变 O11 的一阶常数。

## 三、从局部结果到完整 O11 的两种数学形态

小 Burns 定理若完成，将给出：

\[
P(U_t)\ge8\pi^2(1+|\lambda|t)-o(t)
\]
对所有加权 \(C^{2,\alpha}\)-邻近胞腔成立。这说明恢复序列只有在 exceptional areas 趋零时才逼近 \(8\pi^2\)，并排除所有小尺度无对称改形。

完整 O11 还需要下列两种结构之一。

### 1. 全局同场补偿

在 scalar \(-4\) 代表上，以供应给每个度量的同一个 monopole 解为基础，直接建立
\[
S-32\pi^2A+48\left(W_+-\frac43\pi^2A\right)
 \ge-o(Q).
\]
这正等价于
\[
P\ge8\pi^2Q-o(Q).
\]
由于严格 Weyl 接合可使第二项为负，证明必须追踪产生该下降的同一几何区域内的 spinor 梯度、标量增加和 determinant-curvature 偏差，而不能分别估计两个下确界。

### 2. 近极值胞腔分解

对满足 \(P=O(Q)\) 的近极值序列，若能由曲率泛函的近驻定性、Seiberg–Witten 同场恒等式和四维 \(\varepsilon\)-正则性推出：

- 除去总拓扑荷 \(Q\) 所在的若干区域后，主体趋于复双曲几何；
- 每个集中区域在适当缩放后产生完整胞腔；
- 总 \(P\) 等于各胞腔能量之和加 \(o(Q)\)；

那么任意通用胞腔不等式
\[
P(U)\ge8\pi^2(k_U+4\ell_U)
\]
便给出 O11。相反，任一固定胞腔的严格下降都直接产生系数小于 \(4\) 的闭流形序列。

当前最有信息量的计算组合是：

\[
\boxed{
\text{Malchiodi–Malizia 一颈 Weyl 项}
\;+\;
\text{同一度量上的共形标量最小化}
}
\]
因为它直接测试
\[
4\Delta W_++\Delta S/12
\]
而不是单独测试 Weyl 能量。最有信息量的解析组合则是：

\[
\boxed{
\text{Burns 加权 Hessian 的核分类}
\;+\;
\mathfrak B_p=-8\pi^2\lambda m_K
}
\]
它可把数值观察的 \(c=6\) 提升为无对称的一阶定理，并明确说明任何低于 \(8\pi^2\) 的胞腔都必须离开小 Burns 邻域，进入真正的有限尺寸、复合拓扑或新 ALE 质量机制。
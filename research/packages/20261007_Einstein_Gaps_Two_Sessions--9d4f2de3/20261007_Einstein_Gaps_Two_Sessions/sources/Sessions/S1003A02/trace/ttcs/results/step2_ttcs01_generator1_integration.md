# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 2,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Goal: decide the balanced first-order Einstein-gap coefficient (O11): is inf_g P = 8 pi^2 Q + o(Q) on X_j # k CP2bar # l (S^1 x S^3) over complex-hyperbolic covers X_j, where P = int |Ric0|^2? The note reduces this exactly to the functional 4(W_+ - (4/3)pi^2 A) + (S-32pi^2A)/12 and to a local cell problem P(U) = 8pi^2 + 4 Delta W_+ + Delta S/12; U(2)-invariant cells numerically always cost more than 8pi^2, with first-order penalty 8pi^2*6x0 (x0 = exceptional area/pi, Ric=-6g). Generate the strongest mathematical routes to (a) a proof, without symmetry, that every small perturbation of a scaled Burns bubble glued into a complex-hyperbolic (or Kahler-Einstein) background pays P >= 8pi^2(1 + c x0) - o(x0) with c>0 — identify the exact boundary pairing (Kahler mass of Burns times background curvature), the function spaces, and whether the Seiberg-Witten/Kahler-calibration structure gives the local inequality Delta W_+ >= 0; (b) genuinely different competitor cells that could beat 8pi^2 non-perturbatively: toric/T^2 multi-blowup clusters, LeBrun hyperbolic-ansatz scalar-flat metrics, non-Kahler ASD-like bubbles adapted to a negatively curved background, cells containing necks, and cells combining a blowup with a handle (relevant since the balanced family has k/Q=2/9, l/Q=7/36 and its lower bound uses the opposite chirality through U=3min(T+,T-)/A). For each, give a concrete computable test (ansatz, reduced functional, expected signal) and what result would refute coefficient 4. Also say whether the local inequality Delta W_+ >= 0 for all cells could be FALSE, and propose the cheapest construction testing it. Do not invent literature; name precise knowledge requests if needed.

## Integrated Scientific Memo

# O11：结论、局部定理路线与反例搜索方案

## 1. 当前能决定什么

尚不能由现有材料判定
\[
\inf_gP(g)=8\pi^2Q+o(Q),
\qquad
P=\int|\Ric^\circ|^2.
\]
已严格成立的是
\[
P-8\pi^2Q
=
4\left(W_+-\frac43\pi^2A\right)
+\frac{S-32\pi^2A}{12},
\]
以及对替换一个复双曲球、并在边界 collar 上完全匹配的单 blow-up 胞腔
\[
P(U)-8\pi^2
=
4\Delta W_++\frac{\Delta S}{12}.
\]
全局 monopole 标量估计在这种可植入胞腔上确实给出
\[
\Delta S\ge0.
\]
但它不控制 \(\Delta W_+\) 的符号；现有一般 Weyl–标量估计也不足以推出联合不等式
\[
\Delta S+48\Delta W_+\ge0.
\]

因此，系数 \(4\) 的问题有两个相互独立的缺口：

1. **局部扰动缺口：**证明所有非对称、近 Burns 的小胞腔仍支付正的一阶背景相互作用；
2. **非微扰缺口：**排除固定尺度、复合拓扑或带 neck 的胞腔满足
   \[
   P(U)<8\pi^2(k_U+4\ell_U).
   \]

任一固定胞腔若有上述严格下降，便可在高阶覆盖中复制 \(O(Q_j)\) 次；若其 \((k_U,\ell_U)\) 比例与平衡比例不同，可与标准胞腔混合。因此它会真正把一阶系数降到 \(4\) 以下，而非只产生 \(o(Q)\) 修正。

---

## 2. 无对称小 Burns 泡：应证明的精确定理

令背景 \(g_0\) 为 Kähler–Einstein，
\[
\Ric(g_0)=\lambda g_0,\qquad \lambda<0,
\]
并令
\[
t=\frac{\Area(E)}{\pi}.
\]
复双曲计算采用 \(\lambda=-6\)。预期的无对称结论是
\[
\boxed{
P(U_t)\ge 8\pi^2-8\pi^2\lambda t-o(t).
}
\]
特别地，
\[
\boxed{
P(U_t)\ge8\pi^2(1+6t)-o(t)
}
\qquad(\lambda=-6).
\]
这不仅说明正系数 \(c>0\)，而且预言最优一阶常数为 \(c=6\)。

### 2.1 边界配对

在固定 Burns 空间 \(Z=\Bl_0\mathbb C^2\) 上写
\[
g_B=\delta+H_{-2}+O(r^{-4}),\qquad H_{-2}=O(r^{-2}),
\]
背景正规坐标展开为
\[
(g_0)_{ij}(x)
=
\delta_{ij}-\frac13R_{ikjl}(p)x^kx^l+O(|x|^3).
\]
在泡尺度 \(x=\sqrt t\,y\) 上，
\[
g_0(\sqrt t\,y)=\delta+tQ_2(y)+O(t^{3/2}|y|^3),
\quad
(Q_2)_{ij}=-\frac13R_{ikjl}(p)y^ky^l.
\]

取
\[
\mathcal D h=
\left(2(DW^+)_{g_B}h,\frac1{\sqrt{12}}(Ds)_{g_B}h\right)
\]
并施加 Bianchi gauge
\[
\beta_{g_B}h=0.
\]
其 Green 配对定义为
\[
\mathfrak B_p(H_{-2},Q_2)
=
\lim_{R\to\infty}\int_{S_R}
\mathbf G_{\mathcal D}(H_{-2},Q_2),
\]
但要与相对 Chern–Weil transgression 一起归一化；单独写 \(\mathcal D\) 的边界项可能漏掉拓扑常数。以
\[
m_K=\frac{\Area(E)}{\pi}
\]
归一化 Burns 的 Kähler mass，预期总配对为
\[
\boxed{
\mathfrak B_p=-8\pi^2\lambda m_K
=-2\pi^2s_{g_0}(p)m_K
=-2\pi s_{g_0}(p)\Area(E).
}
\]
当 \(\lambda=-6\)、\(m_K=t\) 时，它等于 \(48\pi^2t\)。

这个常数不是现有来源中已经证明的无对称公式；严谨路线是：

1. 先证明边界双线性型仅依赖 \(H_{-2}\) 和背景二阶 jet，而与 cutoff 无关；
2. 将 Burns mass mode 分解到 \(U(2)\) 不可约表示。对 Kähler–Einstein 背景，只有标量曲率分量能与该不变 mode 配对；
3. 用已完成的 \(U(2)\) Kähler 计算校正常数，得到 \(-8\pi^2\lambda\)。

对于 Kähler 匹配，该分解与数值完全一致：
\[
\Delta S=-32\pi^2\lambda t+o(t),\qquad
\Delta W_+=-\frac43\pi^2\lambda t+o(t),
\]
所以在 \(\lambda=-6\) 时
\[
\frac{\Delta S}{12}=16\pi^2t,\qquad
4\Delta W_+=32\pi^2t.
\]

### 2.2 加权空间和核问题

可用
\[
C^{2,\alpha}_\delta,\qquad H^2_\delta,\qquad -2<\delta<0,
\]
避开 \(\mathcal D^*\mathcal D\) 的 indicial roots。例如
\[
\|h\|_{C^{2,\alpha}_\delta}
=
\sum_{j=0}^2\sup_Z\langle r\rangle^{j-\delta}|\nabla^jh|
+
[\langle r\rangle^{2+\alpha-\delta}\nabla^2h]_\alpha,
\]
以及
\[
\|h\|_{H^2_\delta}^2
=
\sum_{j=0}^2
\int_Z
\langle r\rangle^{2(j-\delta)-4}|\nabla^jh|^2\,d\mu_{g_B}.
\]

必须显式移除或调制：

- \(r^{-2}\) mass/scale mode，用固定 \(\Area(E)\) 处理；
- 泡中心和平移参数；
- 无穷远 Euclidean rotation/frame；
- 纯微分同胚方向；
- 任何真正的 scalar-flat ASD Jacobi mode。

背景增长项 \(tQ_2\) 不属于衰减空间，应作为显式匹配数据保留。

Burns 满足 \(W^+=s=0\)，故二阶型为
\[
\mathcal Q_B(v)
=
\int_Z\left[
4|(DW^+)v|^2+\frac1{12}|Ds(v)|^2
\right]d\mu_{g_B}.
\]
关键解析命题不是无条件严格正性，而是固定参数并投影有限维核后
\[
\mathcal Q_B(v_\perp)
\ge c_0\|v_\perp\|_{H^2_\delta}^2.
\]
若存在非几何 Jacobi 核，则必须做 Lyapunov–Schmidt 化约，并计算其可积性和 mass map；仅有 \(\mathcal Q_B\ge0\) 不够。

### 2.3 所需展开

对调制后的
\[
g_t=g_t^{\rm app}+v
\]
应建立
\[
P(U_t)-8\pi^2
=
t\mathfrak B_p
+\mathcal Q_B(v_\perp)
+t\mathcal L_p(v_\perp)
+\mathcal R_t(v),
\]
其中
\[
|\mathcal L_p(v_\perp)|
\le C\mathcal Q_B(v_\perp)^{1/2},
\]
且在所选近邻内
\[
|\mathcal R_t(v)|
\le \eta\mathcal Q_B(v_\perp)+o(t)+Ct^2.
\]
完成平方给出
\[
\mathcal Q_B+t\mathcal L_p\ge-Ct^2
\]
以及目标下界。更强的
\[
O(t^2|\log t|)
\]
余项是合理候选，但必须由 polyhomogeneous 展开、匹配半径和每个 cutoff 交叉项实际推导，不能仅凭尺度计数宣称。

### 2.4 最精确的知识请求

需要核实或建立：

1. Burns 上
   \[
   (DW^+,Ds,\beta)
   \]
   的加权核、余核和 indicial roots；
2. \(-2<\delta<0\) 中所有 Jacobi fields 的几何来源；
3. 固定 exceptional area 与 asymptotic frame 后，附近 scalar-flat ASD ALE 度量是否局部刚性；
4. 若不刚性，ALE mass tensor/Kähler mass 沿这些模的微分；
5. 相对 Chern–Weil transgression 与上述 Green pairing 的精确符号和常数。

---

## 3. Seiberg–Witten/Kähler 结构能否给 \(\Delta W_+\ge0\)？

### 能严格得到的部分

把胞腔植入 \(X\setminus B\) 后，全局标量估计给出
\[
S(g)\ge32\pi^2A=S(g_X),
\]
故
\[
\boxed{\Delta S\ge0.}
\]
如果整个闭合度量仍是 Kähler，则
\[
W_+=S/24,
\]
并且
\[
P(U)-8\pi^2=\frac{\Delta S}{4}\ge0.
\]
因此，纯 Kähler toric 胞腔、scalar-flat Kähler core 配 Kähler collar，均不可能击败 \(8\pi^2\)。

### \(\Delta W_+\ge0\) 很可能是假的

严格总 Weyl 降低的 connected-sum 构造给出了直接的反例机制。设同一接合度量满足
\[
\delta(W_++W_-)<0
\]
（这里均为 operator norm 能量）。signature 的拓扑不变性给出
\[
\delta(W_+-W_-)=0,
\]
所以
\[
\delta W_+=\delta W_-=
\frac12\delta(W_++W_-)<0.
\]
对反向 Fubini–Study 因子，其相关 \(W^+\) 为零。因此，只要该接合改动能局限于一个胞腔并保持外 collar 完全固定，就产生
\[
\Delta W_+<0.
\]

故不能把 \(\Delta W_+\ge0\) 当作可信的普遍局部原理。真正可能成立的是联合补偿
\[
\boxed{\Delta S+48\Delta W_+\ge0,}
\]
即 \(P(U)\ge8\pi^2\)，或仅在小 Burns 邻域成立的定量版本。

### 最便宜的检验

最低成本不是重新优化全部胞腔，而是：

1. 从严格总 Weyl 接合的已知数值/展开，用 signature 恒等式直接取一半得到 \(\Delta W_+\)；
2. 检查接合是否在外 collar 与背景精确一致；
3. 在同一度量上计算 scalar energy，而不是比较独立下确界。

若不直接使用该接合，也可在现有 \(U(2)\) 代码中把目标改成 \(W_+\)。单 blow-up 相对 signature 给出
\[
\Delta W_+=\Delta W_--12\pi^2
\]
（背景项按同一相对约定计入）。寻找
\[
\Delta W_+<0
\]
只需把 \(W_-\) 压到相应阈值以下；但这本身不意味着 \(P<8\pi^2\)。

---

## 4. 最直接的非微扰竞争者：严格 Weyl 接合加共形标量最小化

对已知严格 Weyl 接合度量 \(g_a\)，定义
\[
\Theta(a)=4\Delta W_+(a)+\frac{\Delta S(a)}{12}.
\]
决定系数的信号是
\[
\boxed{\Theta(a)<0.}
\]

Weyl 部分已有负方向；缺失的是同一度量的 scalar cost。由于四维 Weyl 能量共形不变，可固定 \(g_a\) 并只在胞腔内部求
\[
\widetilde g=u^2g_a,\qquad u\equiv1
\]
于外 collar。目标为
\[
S(u^2g_a)
=
\int_Uu^{-2}(6\Delta_{g_a}u+s_{g_a}u)^2\,d\mu_{g_a}.
\]
因此这是一个标量四阶边值最优化，而不是再次优化完整度量。其形式 Euler 方程为
\[
(6\Delta+s)\!\left[u^{-2}(6\Delta u+su)\right]
-u^{-3}(6\Delta u+su)^2=0,
\]
并需取保证 collar 固定的边界数据，例如在 collar 上直接规定 \(u=1\)，而不是只给单一 Dirichlet 条件。

若
\[
\Delta S_{\min}(a)<-48\Delta W_+(a),
\]
则得到真实的
\[
P(U)<8\pi^2.
\]
任何固定 \(a>0\) 的严格节省都能复制并改变一阶系数。反之，若节省仅为 \(O(a^4)\) 且闭流形构造迫使 \(a=a_j\to0\)，总节省只是 \(o(Q_j)\)，不能改变系数。

需要从接合原始构造中提取：

- Weyl \(a^4\) 相互作用的精确常数和 chirality 约定；
- 接合度量是否在紧致区域外精确等于原度量；
- 同一插值坐标中的 scalar-curvature 首项；
- \(W^{2,\infty}\) 度量平滑化后的 Weyl 与 scalar 误差；
- scalar-flat Green-function blow-up 是否保留负 Weyl interaction。

这是目前最便宜、最有判别力的反例测试。

---

## 5. 其他真正不同的胞腔

### 5.1 一般 \(T^2\)-不变多 blow-up 簇

纯 toric Kähler 情形不能赢：用 symplectic potential \(u\)，
\[
g=u_{ij}d\mu_i d\mu_j+u^{ij}d\theta_i d\theta_j,\qquad
s=-\partial_i\partial_j u^{ij},
\]
且
\[
|W^+|^2=s^2/24,
\]
故联合超额为 \(\Delta S/4\ge0\)。

真正应算的是一般 orthogonally transitive \(T^2\) ansatz：
\[
g=G_{ab}(y)dy^ady^b
+
H_{ij}(y)(d\theta^i+A^i_a\,dy^a)
(d\theta^j+A^j_b\,dy^b).
\]
rod/facet 数据编码 exceptional spheres，外 collar 固定为复双曲球。约化泛函为
\[
P=(2\pi)^2\int_{\mathcal P}
|\Ric^\circ(G,H,A)|^2
\sqrt{\det G\,\det H}\,d^2y.
\]

首个计算应取两个相邻 \((-1)\)-facets，优化：

- 两个 exceptional areas；
- 中心间距；
- rod/facet 几何；
- 非 Kähler 模 \(H-G^{-1}\)；
- connection curvature \(dA\)。

小簇的一阶项预计只见总 mass，
\[
-8\pi^2\lambda(t_1+t_2)>0,
\]
故真正可能获益的是有限尺度簇或非 Kähler mass tensor。反驳系数 \(4\) 的信号是
\[
\boxed{P(U_m)<8\pi^2m}
\]
并在网格加密及 collar 加宽后保持固定严格差。

### 5.2 LeBrun hyperbolic ansatz

可从
\[
V=1+\sum_{\alpha=1}^mG_{p_\alpha},\qquad
d\theta=*_{H^3}dV
\]
构造圆对称多中心核心，再取相应共形因子得到 scalar-flat Kähler 或自对偶候选。

必须先核实：

- 选定定向下的紧致化拓扑和交矩阵；
- 固定点是否确实给出 \(m\) 个所需 \((-1)\)-类；
- asymptotic \(r^{-2}\) mass 以及 \(r^{-3},r^{-4}\) multipoles；
- 多中心碰撞时的 orbifold/光滑条件。

如果胞腔始终 Kähler，它不能获胜；真正自由度必须放在非 Kähler collar。应计算
\[
4\Delta W_++\frac{\Delta S}{12},
\]
而非仅注意核心满足 \(s=W^+=0\)。决定性信号仍是
\[
P(U_m)<8\pi^2m.
\]

### 5.3 非 Kähler scalar-flat ASD-like 泡

最便宜的线性测试是在 Burns 上求
\[
DW^+(h)=0,\qquad Ds(h)=0,\qquad \beta h=0,
\]
并读取其 \(r^{-2}\) asymptotic tensor。

- 若固定面积后没有非规范可积模，则 Burns 一阶相互作用具局部普适性；
- 若存在可积模，应计算背景曲率与其 effective mass tensor 的配对；
- 若该配对能转负，则小尺度非 Kähler 泡可能直接逃离 \(+6t\) 规律。

这里不能预先把相互作用写成单一标量 mass；非 \(U(2)\) 模可能与背景 Bochner/Weyl 分量配对。只有在表示分解证明这些分量消失后，才可化为
\[
-8\pi^2\lambda m_{\rm eff}.
\]

需要精确知识：\(O(-1)\) 上 scalar-flat ASD ALE 模空间、可积性，以及适用于非 Kähler ALE 度量的质量正性条件。

### 5.4 含内部 neck 的单 blow-up 胞腔

现有 \(x=b^2\) 参数化排除了 orbit radius 非单调。改用完整 biaxial Bianchi IX：
\[
g=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)+c(t)^2\sigma_3^2.
\]
bolt 条件为
\[
c(0)=0,\qquad a(0)>0,\qquad a'(0)=0,
\]
再按圆纤维周期固定 \(c'(0)\)。外端匹配复双曲二阶 jet。

约化泛函
\[
P=2\pi^2\int a^2c\,|\Ric^\circ(a,c)|^2dt
\]
是两函数高阶变分问题，可直接用自动微分和谱配置优化。应允许：

- \(a'\) 改变符号；
- 多个 throat；
- 长近 Einstein 段；
- 多段 transition。

单纯拉长 cylinder 不会因尺度不变性自动便宜；需要 neck 主体近似满足各 Ricci 特征值相等。反驳信号：
\[
\boxed{P<8\pi^2.}
\]

### 5.5 blow-up 与 handle 的复合胞腔

平衡比例为
\[
\frac{k}{Q}\to\frac29,\qquad
\frac{\ell}{Q}\to\frac7{36},
\]
即
\[
\frac{k}{\ell}\to\frac87.
\]
自然超胞腔是
\[
(k_U,\ell_U)=(8,7),\qquad q_U=36.
\]

handle bridge 可先用
\[
g=dt^2+a(t)^2g_{S^3}.
\]
在给定归一化下，
\[
|\Ric^\circ|^2
=
3\frac{\big((a')^2-1-aa''\big)^2}{a^4},
\]
所以
\[
P_{\rm bridge}
=
6\pi^2\int
\frac{\big((a')^2-1-aa''\big)^2}{a}\,dt.
\]
将 bridge 与 Burns/Bianchi IX 核心通过共同 \(S^3\) jet 联合优化，可测试 transition sharing 是否降低总成本。

相对 signature 给出
\[
\Delta(W_+-W_-)=-12\pi^2k_U.
\]
handle 本身不改 signature，却可能改变为承载 blow-up 拓扑所需的两种手征能量分配。这正是平衡族中 opposite chirality 不能忽略的原因。

最小测试可先取 \((1,1)\)：
\[
\boxed{P(U_{1,1})<40\pi^2.}
\]
若得到
\[
P(U_{1,1})=8\pi^2(5-\delta),
\]
则七个 \((1,1)\) 胞腔加一个标准 blow-up 构成 \((8,7)\)，总节省为
\[
7\delta\cdot8\pi^2.
\]
更直接的最终测试是
\[
\boxed{P(U_{8,7})<8\pi^2\cdot36.}
\]

---

## 6. 各类测试的判据汇总

| 候选 | 可计算对象 | 支持系数 \(4\) 的信号 | 反驳系数 \(4\) 的信号 |
|---|---|---|---|
| 近 Burns 非对称扰动 | 加权 Hessian、mass–curvature 边界配对 | \(P\ge8\pi^2(1+6t)-o(t)\) | 固定面积 Jacobi 模给出负的一阶配对 |
| 严格 Weyl neck | \(\Theta=4\Delta W_++\Delta S/12\) | scalar cost 抵消 Weyl gain | 固定尺度 \(\Theta<0\) |
| 一般 toric/\(T^2\) cluster | 二维约化 \(P[G,H,A]\) | \(P(U_m)\ge8\pi^2m\) | \(P(U_m)<8\pi^2m\) |
| LeBrun 多中心核心 | mass/multipoles + 非 Kähler collar | 总 mass 正且 collar 无节省 | 完整匹配后联合超额为负 |
| 非 Kähler ASD-like ALE | Jacobi 核及 mass tensor | 固定面积局部刚性或正配对 | 可积模产生负背景配对 |
| 内部 neck | Bianchi IX 两函数泛函 | 所有分支 \(P\ge8\pi^2\) | 单 blow-up \(P<8\pi^2\) |
| blow-up–handle cell | 联合 bridge/core 泛函 | \(P\ge8\pi^2(k+4\ell)\) | \(P_{1,1}<40\pi^2\) 或 \(P_{8,7}<288\pi^2\) |

---

## 7. 从胞腔结论到完整 O11

近 Burns 定理只证明恢复邻域中的系数 \(4\)，不能排除完全不同的全局几何。完整结论还需下列两种数学机制之一。

### 全局同场补偿

在供应给每个度量的同一个 monopole 解上证明
\[
S-32\pi^2A
+
48\left(W_+-\frac43\pi^2A\right)
\ge-o(Q).
\]
这与
\[
P\ge8\pi^2Q-o(Q)
\]
完全等价。由于 \(\Delta W_+\) 很可能可为负，证明必须把该 Weyl 下降与同一区域中的 scalar excess、spinor gradient、determinant-curvature mismatch 联合起来，不能分别取下界。

### 近极值胞腔分解

对 \(P=O(Q)\) 的近极值序列证明：

1. 拓扑集中区之外趋近复双曲主体；
2. 每个集中区缩放后产生完整标记胞腔；
3. 拓扑荷满足
   \[
   \sum_i(k_i+4\ell_i)=Q+o(Q);
   \]
4. 能量无损分裂：
   \[
   P(g_j)=\sum_iP(U_i)+o(Q_j).
   \]

若再有所有完整胞腔的普遍不等式
\[
P(U)\ge8\pi^2(k_U+4\ell_U),
\]
即可推出 O11。反之，一个固定严格低成本胞腔即可复制，直接否定系数 \(4\)。

最先应解决的两个具体数学对象因此是：

\[
\boxed{
\text{Burns 加权形变复形的核分类}
+
\text{边界配对 }-8\pi^2\lambda m_K
}
\]
和
\[
\boxed{
\text{严格 Weyl 一颈接合}
+
\text{同一胞腔内的共形 scalar-energy 最小化}.
}
\]

前者把数值观察的 \(6t\) 提升为无对称局部定理；后者以最低成本检验 \(\Delta W_+\ge0\) 的失败是否能进一步成为真正的 \(P<8\pi^2\) 反例。
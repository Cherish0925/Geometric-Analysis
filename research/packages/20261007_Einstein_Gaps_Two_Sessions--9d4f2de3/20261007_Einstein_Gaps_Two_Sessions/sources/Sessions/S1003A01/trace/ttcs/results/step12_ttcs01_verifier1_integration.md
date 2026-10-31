# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 12,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step12_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step12_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check and strengthen the proposed next cost theory after the certified subthreshold single-blow-up cell. Verify the exact subadditivity statements for the cell infima J_{k,l}, including J_{8,7}≤7J_{1,1}+J_{1,0} and J_{8,7}≤4J_{2,0}+224π², and derive precisely what inequalities would improve the currently certified balanced upper coefficient. Then compare three routes—two blow-up interaction, blow-up–handle interaction, and the complete large-collar single-cell limit—using the inherited pure-handle rigidity, actual-field lower results, the certified cell mechanism, and relevant curvature-functional gluing literature. Identify which route gives the best combination of mathematical leverage and faithful connection to the full Einstein-gap goal. Pay special attention to whether a reduced exterior interaction for J must use the fourth-order normal equation A* A rather than the second-order linearized Einstein equation, and to any gauge or boundary-data issue that could invalidate a naive Dirichlet-to-Neumann experiment.

## Integrated Scientific Memo

# 核验结论：认证单爆破 cell 之后的代价理论

## 1. 定义、随 collar 半径的单调性与精确次可加性

在 \(\operatorname{Ric}=-g\) 归一化下，令
\[
j_{k,\ell}(R)
=
\inf_{g}
\int_{C_{k,\ell}(R)}|\operatorname{Ric}_g+g|^2\,dV_g,
\]
其中
\[
C_{k,\ell}(R)\cong
B_R^{\mathbb{CH}^2}\#
k\overline{\mathbb{CP}}^{\,2}\#
\ell(S^1\times S^3),
\]
且 \(g\) 在外侧开 collar 上与复双曲度量完全一致。允许 \(R\) 变化的 cell 下确界记为
\[
\mathfrak J_{k,\ell}:=\inf_R j_{k,\ell}(R).
\]

若 \(R_2>R_1\)，可在 \(R_1\)-cell 外接一段零 defect 的 CH 环域，故
\[
j_{k,\ell}(R_2)\le j_{k,\ell}(R_1),
\qquad
\boxed{\mathfrak J_{k,\ell}
=\lim_{R\to\infty}j_{k,\ell}(R).}
\]
这只是能量下确界的精确极限公式；不自动给出完整极限度量、紧性或下确界达到。

### 次可加性定理

对任意 \(k_i,\ell_i\ge0\)，
\[
\boxed{
\mathfrak J_{k_1+k_2,\ell_1+\ell_2}
\le
\mathfrak J_{k_1,\ell_1}
+
\mathfrak J_{k_2,\ell_2}.}
\]

证明：在足够大的 CH 球中取两个不交子球，将它们分别替换为两个近极值 cell。由于各 cell 在完整开 collar 上精确等于 CH，拼接光滑，子球之间区域满足 \(\operatorname{Ric}+g=0\)，所以总代价严格等于两局部代价之和。令近极值误差趋零即得结论。这里不需要任一 infimum 被达到。

纯 handle 刚性给出
\[
\boxed{\mathfrak J_{0,\ell}=32\pi^2\ell.}
\]
\(\ell>0\) 时该值由 shrinking-handle 序列逼近而不由固定光滑 cell 达到，但这不影响下确界层面的次可加不等式。因此
\[
\boxed{\mathfrak J_{8,7}
\le 7\mathfrak J_{1,1}+\mathfrak J_{1,0},}
\]
因为 \((8,7)=7(1,1)+(1,0)\)，以及
\[
\boxed{\mathfrak J_{8,7}
\le4\mathfrak J_{2,0}+224\pi^2,}
\]
因为 \((8,7)=4(2,0)+(0,7)\) 且
\(\mathfrak J_{0,7}=224\pi^2\).

同理，
\[
\mathfrak J_{2,0}\le2\mathfrak J_{1,0},
\qquad
\mathfrak J_{1,1}\le\mathfrak J_{1,0}+32\pi^2,
\]
从而恢复当前分离构造
\[
\boxed{\mathfrak J_{8,7}
\le8\mathfrak J_{1,0}+224\pi^2.}
\]

严格不等式
\[
\mathfrak J_{2,0}<2\mathfrak J_{1,0}
\quad\text{或}\quad
\mathfrak J_{1,1}<\mathfrak J_{1,0}+32\pi^2
\]
都不是次可加性的形式推论；它们正是需要证明的相互作用节省。

### 稳定 balanced block

令 \(a_n=\mathfrak J_{8n,7n}\)。由次可加性，Fekete 引理给出
\[
\lim_{n\to\infty}\frac{\mathfrak J_{8n,7n}}n
=
\inf_{n\ge1}\frac{\mathfrak J_{8n,7n}}n.
\]
因此 fixed-cell 构造中真正稳定的 balanced 系数是
\[
\boxed{
c_{\rm cell}^{\rm st}
=
\frac1{72\pi^2}
\inf_{n\ge1}\frac{\mathfrak J_{8n,7n}}n,}
\]
它可能严格小于单块值
\(\mathfrak J_{8,7}/(72\pi^2)\)。

若 \(c_{\rm inh}>0\) 是继承的 actual-field 全度量下界，则每个可转移的 cell 构造必须满足
\[
c_{\rm inh}
\le c_{\rm cell}^{\rm st}
\le \frac{\mathfrak J_{8,7}}{72\pi^2}.
\]
这是局部代价理论与全局 Einstein-gap 正下界之间的重要一致性约束。

---

## 2. 改进当前认证 balanced 系数所需的精确不等式

令
\[
\overline J_{10}
\]
表示实际采用的光滑单爆破 cell 上界。canonical strict \(X=8\) Arb 证书给出未平滑 profile
\[
\frac{J_6}{8\pi^2}
\in
[0.999116243135324311\pm2.24\times10^{-19}],
\]
通过 smoothing width 对角趋零，可把 \(\overline J_{10}\) 任意逼近该值。因此当前认证渐近系数是
\[
c_{\rm cert}
=
\frac{28}{9}+\frac{\overline J_{10}}{9\pi^2}
=
\frac{224\pi^2+8\overline J_{10}}{72\pi^2},
\]
在极限意义下
\[
c_{\rm cert}<3.999214438342511.
\]

材料中的 \(X=16\) 数值更低，但 canonical pure-Arb strict 输出明确属于 \(X=8\)；除非 \(X=16\) 也用修正后的 pure-Arb tail 实现重新认证，否则严谨比较应以 \(X=8\) 为基准。

### 2.1 完整 \((8,7)\) mixed cell

新的 \((8,7)\)-cell 上界 \(J_{87}\) 改进当前证书，当且仅当
\[
\boxed{
J_{87}<224\pi^2+8\overline J_{10}.}
\]
若
\[
\Delta_{87}
=
224\pi^2+8\overline J_{10}-J_{87}>0,
\]
则
\[
\boxed{
c_{\rm new}
\le c_{\rm cert}-\frac{\Delta_{87}}{72\pi^2}.}
\]

若比较的是未知的最优分离代价，而非当前数值证书，则严格 mixed 非可加性为
\[
\boxed{
\mathfrak J_{8,7}
<
8\mathfrak J_{1,0}+224\pi^2.}
\]

要突破所有“单爆破 + 独立 handles”构造共有的绝对底项 \(28/9\)，必须有更强的
\[
\boxed{\mathfrak J_{8,7}<224\pi^2.}
\]

### 2.2 两爆破相互作用

由
\[
\mathfrak J_{8,7}\le4\mathfrak J_{2,0}+224\pi^2
\]
得到
\[
c\le\frac{28}{9}+\frac{\mathfrak J_{2,0}}{18\pi^2}.
\]
因此相对于当前认证值，精确条件是
\[
\boxed{\mathfrak J_{2,0}<2\overline J_{10}.}
\]
若构造出
\[
J_{20}=2\overline J_{10}-\Delta_{20},
\qquad \Delta_{20}>0,
\]
则
\[
\boxed{
c_{\rm new}\le
c_{\rm cert}-\frac{\Delta_{20}}{18\pi^2}.}
\]

相对于真正最优单爆破 cell 的内在严格次可加条件是
\[
\boxed{\mathfrak J_{2,0}<2\mathfrak J_{1,0}.}
\]

### 2.3 爆破–handle 相互作用

由
\[
\mathfrak J_{8,7}
\le7\mathfrak J_{1,1}+\mathfrak J_{1,0}
\]
得到
\[
c\le
\frac{7\mathfrak J_{1,1}+\mathfrak J_{1,0}}{72\pi^2}.
\]

相对于最优分离理论，正确的 mixed 非可加条件是
\[
\boxed{
\mathfrak J_{1,1}
<
\mathfrak J_{1,0}+32\pi^2.}
\]

若余下的 \((1,0)\)-block 仍取认证 cell，则一个直接可验证的充分条件是
\[
\boxed{
J_{11}<\overline J_{10}+32\pi^2.}
\]
写成
\[
J_{11}
=
\overline J_{10}+32\pi^2-\Delta_{11},
\]
即有
\[
\boxed{
c_{\rm new}
\le c_{\rm cert}
-\frac{7\Delta_{11}}{72\pi^2}.}
\]

更一般地，相对于当前认证系数的精确代数条件是
\[
\boxed{
7\mathfrak J_{1,1}+\mathfrak J_{1,0}
<
224\pi^2+8\overline J_{10}.}
\]

### 2.4 单爆破 large-collar 改进

若新的单 cell 给出
\[
J_{10}^{\rm new}
=
\overline J_{10}-\Delta_{10},
\]
则
\[
\boxed{
c_{\rm new}
\le c_{\rm cert}
-\frac{\Delta_{10}}{9\pi^2}.}
\]
但只要 handles 仍由纯 handle shrinking cores 独立处理，这条路线永远保留 \(28/9\) 项。

---

## 3. 三条路线的比较

### A. 两爆破相互作用：最佳综合杠杆

目标是
\[
\mathfrak J_{2,0}<2\mathfrak J_{1,0},
\]
或对当前证书更直接地，
\[
J_{20}<2\overline J_{10}.
\]

优势：

1. **比较基准是真实光滑度量。**  
   两个认证单爆破 cell 经足够窄 smoothing 后可任意接近 \(2\overline J_{10}\)，无需围绕未达到的 handle infimum 做微妙比较。

2. **任意严格节省都改善 balanced 系数。**  
   四个双爆破 cell 加七个 pure-handle shrinking cores 已精确符合 \((8,7)\) 比例。

3. **与已知曲率泛函 gluing 的机制最接近。**  
   Malchiodi–Malizia 的 Weyl-energy gluing 用 biharmonic interpolation，并由相对框架旋转控制 Weyl 交叉项；Gursky–Viaclovsky 的四阶 gauge-fixed 拼接中，Kuranishi 首项同样含
   \[
   W(z_0)\circledast W(y_0)
   \]
   及 scalar/mass 项。这些结果不直接证明 \(J\) 的严格次可加性，但明确支持“第四阶外部响应 + 相对位置/旋转交叉项”这一机制。

4. **认证 cell 的已知非 Kähler、\(\omega^\perp\) 模式可继续使用。**

限制：即使成功，它仍保留 \(224\pi^2\) 的独立 handle 代价，因此不能单独突破 \(28/9\)。

### B. 爆破–handle 相互作用：与完整 mixed Einstein-gap 问题最直接

纯 handle 已完全刚性：
\[
\mathfrak J_{0,\ell}=32\pi^2\ell,
\]
故“改进孤立 handle cell”已被排除。

相对恒等式
\[
J-8\pi^2q
=
\frac{S_C-16d}{12}
+\frac14\int_C(s+4)^2
-4\left(\frac{2d}{3}-W_C\right),
\]
配合
\[
\frac{2d}{3}-W_C=12\pi^2k-B_C\le12\pi^2k,
\]
说明 handles 增加拓扑代价 \(q=k+4\ell\)，却不提供独立的 self-dual Weyl-depletion budget；该预算来自 blow-ups。因而 mixed 节省若存在，必须是 handle 几何改变了 blow-up 所资助的 Weyl depletion、scalar compensation 和 Ricci defect 的共同分配。

这条路线最忠实地接近完整目标，因为它可能重新组织甚至削弱 \(28/9\) handle 项。但近期解析风险最大：pure-handle infimum 仅由退化序列实现。若
\[
J(H_\rho)=32\pi^2+e(\rho),\qquad e(\rho)\to0,
\]
mixed 构造需证明相互作用节省 \(I(\rho)\) 满足
\[
I(\rho)>e(\rho)+o(I(\rho))
\]
在某一尺度成立。仅发现一个固定尺度负交叉项并不足够。

### C. 完整 large-collar 单 cell 极限：最清晰、最可认证的控制问题

由
\[
\mathfrak J_{1,0}=\lim_{R\to\infty}j_{1,0}(R),
\]
large collar 是单爆破下确界的精确能量实现，而非仅数值技巧。现有 Bianchi-IX 曲率公式、bolt 消奇异化和 Arb 积分可以直接复用；\(X=8\) 到 \(X=16\) 的数值下降提供了真实信号。

它可确定：

- \(\mathfrak J_{1,0}\) 的更优上界及可能渐近值；
- defect 是留在 bolt、向外漂移，还是形成完整渐近 CH 极限；
- 认证 \(\omega^\perp\) 模式的尾部结构；
- fixed-collar 无临界点定理所预示的非达到/退化机制。

但不能从有限的 \(X=8,16\) 数据推出极限趋势，更不能推断代价可能趋零。关于“essential spectrum 从零开始”或“\(\eta_\infty\to1\)”的说法在所给材料中没有依据。还应注意：fixed-collar 问题无光滑内部临界点意味着 large-collar 极限很可能通过退化或逃逸实现，而非收敛到普通固定边界极小度量。

### 综合判断

- **近期最好的数学杠杆与完整目标之间的平衡：两爆破相互作用。**  
  它已有严格光滑基准、任何节省都能立即转移到 balanced family，并且最接近现有第四阶曲率 gluing 技术。

- **若目标是理解或突破 \(28/9\) handle 项：爆破–handle 相互作用不可替代。**  
  它是最终 mixed-cost 问题的核心，但目前缺少控制 shrinking-handle 误差与交叉项相对阶数的机制。

- **large-collar 单 cell 是最可靠的数值/退化控制实验。**  
  它可继续提高已认证系数并为多核相互作用提供尾部边界数据，但其结构覆盖面窄于 mixed routes。

---

## 4. Reduced exterior interaction 必须使用 \(A^*A\)，而不是 \(A\)

令
\[
\Phi(g)=\operatorname{Ric}_g+g,
\qquad
g_0=g_{\mathbb{CH}^2},
\qquad
\Phi(g_0)=0,
\]
并令
\[
A=D\Phi_{g_0}.
\]
对 \(g_\varepsilon=g_0+\varepsilon h\)，
\[
\Phi(g_\varepsilon)
=
\varepsilon Ah+O(\varepsilon^2),
\]
所以外部区域 \(\Omega\) 上
\[
J_\Omega(g_\varepsilon)
=
\varepsilon^2\int_\Omega|Ah|^2\,dV_{g_0}
+O(\varepsilon^3).
\]

二次能量
\[
Q(h)=\int_\Omega|Ah|^2
\]
的 normal equation 是
\[
\boxed{A^*Ah=0,}
\]
不是
\[
Ah=0.
\]

\(Ah=0\) 描述 infinitesimal Einstein deformation；\(A^*Ah=0\) 才描述在给定接口数据下最小化 squared Einstein defect 的外部响应。即使在 Bianchi gauge 中 \(A\) 成为形式自伴的二阶 Laplace 型算子，正确方程仍是四阶 \(A^2h=0\)。

这也解释了为何 Weyl-energy 文献采用 biharmonic interpolation，以及 Gursky–Viaclovsky 必须使用四阶 gauge-fixed 算子。那些文献给出方法论和交叉项模板，但不能直接搬用其符号结论到 \(J\)：\(J\) 非共形不变，CH 背景非平坦，scalar/volume 项会改变总能量平衡。

还需区分两个层次：

- 在**精确 CH 外部**，\(A^*A\) 是正确的二次 normal operator；
- 若在线性化点包含认证 cell 的非 Einstein 核心，则 \(J\) 的一阶变分一般不消失，二次算子还含由背景 defect 产生的低阶项，不能把整个 cell 变分简化为纯 \(A^*A\)。

---

## 5. naive Dirichlet-to-Neumann 实验的致命问题

### 5.1 四阶问题需要两组边界迹

对
\[
Q(h)=\int_\Omega|Ah|^2
\]
作分部积分，边界配对同时涉及
\[
\delta h|_\Sigma
\quad\text{和}\quad
\nabla_\nu\delta h|_\Sigma.
\]
因此自然的 Calderón 数据是
\[
(h,\nabla_\nu h)
\longmapsto
\text{与 }Ah,\nabla_\nu Ah\text{ 相关的共轭数据},
\]
而不是二阶方程的
\[
h\longmapsto\nabla_\nu h.
\]

几何上应固定/匹配诱导度量与第二基本形式，加上 gauge-compatible 的法向数据。只固定诱导三维度量不足以保证 \(C^1\) 乃至 \(W^{2,2}\) 可接受的 gluing；法向导数不匹配会产生奇异曲率，破坏能量计算。反之，对二阶方程 \(Ah=0\) 同时强制 metric 与 normal derivative 通常过定。

### 5.2 微分同胚 gauge 零模

由自然性，
\[
A(\mathcal L_Xg_0)
=
\mathcal L_X\Phi(g_0)=0.
\]
未经 gauge fixing 的 \(Q\) 在纯 gauge 方向退化。若 \(X\) 不在接口处固定，它可改变坐标形式的 Dirichlet/Neumann 数据而不改变几何，制造伪交叉节省。

可靠设置至少需要：

- 统一的 Bianchi slice 或等价 elliptic gauge；
- 只模掉在外 collar/接口标记上恒等的微分同胚；
- 核心与外部使用同一 boundary marking；
- 单独处理 residual Killing/conformal-Killing kernel 与有限维 cokernel；
- 不把 trace/scaling 模式误当作纯 gauge，因为 cosmological constant 已固定。

### 5.3 必须固定完整 metric germ

cell 定义要求在开 collar 上整个 metric germ 精确等于 CH，而非只给定边界内蕴度量。来源材料中的 chiral cap 结果已说明：相同的圆边界度量可能对应任意大的 full-collar Weyl 代价，因为法向 germ 和 Pontryagin transgression 仍携带信息。这里同样不能用 intrinsic Dirichlet data 替代完整 collar 匹配。

### 5.4 严格相加与真正交互的区别

若两个认证 cell 保留各自完整 exact-CH collar，并嵌入不交子球，则 defect 支持不交，代价严格相加；不存在相互作用。要测试
\[
\mathfrak J_{2,0}<2\mathfrak J_{1,0},
\]
必须更内侧截取两个核心，让它们共享同一个 CH 外部响应区。在线性层面，
\[
Q(h_1+h_2)
=
Q(h_1)+Q(h_2)
+
2\int_\Omega\langle Ah_1,Ah_2\rangle.
\]
相对位置与框架旋转可改变最后一项，但只有在共同 gauge、完整四阶边界数据和同一 boundary marking 下，该交叉项才有几何意义。

---

## 6. 需要纠正的两点

1. **复双曲平面不是“两种 Weyl 手性都非零”。**  
   以其复取向，\(\mathbb{CH}^2\) 是 Kähler–Einstein，并在本文约定下满足 \(W^-=0\)、\(W^+\neq0\)。因此不能据 Malchiodi–Malizia 的一般非同手性假设，直接断言某个 CH–cell 交叉项必非零或必有利；必须核对 orientation reversal、核心尾部手性和实际张量收缩。

2. **fixed-collar 无临界点定理并不说明极小点会满足 \(E\neq0\) 且 \(A^*E=0\)。**  
   该定理恰恰说明 \(q>0\) 时不存在任何光滑 unrestricted stationary cell。下确界可能不达到。\(A^*A h=0\) 是 CH 外部的线性二次响应方程，不是一个已存在全局 cell 极小点的方程。

---

## 最终科学判断

已核实的下一层代价框架是：

\[
\boxed{
\mathfrak J_{k_1+k_2,\ell_1+\ell_2}
\le
\mathfrak J_{k_1,\ell_1}
+\mathfrak J_{k_2,\ell_2}}
\]
及其特例
\[
\boxed{\mathfrak J_{8,7}\le7\mathfrak J_{1,1}+\mathfrak J_{1,0}},
\qquad
\boxed{\mathfrak J_{8,7}\le4\mathfrak J_{2,0}+224\pi^2}.
\]

当前认证 balanced 系数的三个严格改进判据分别是
\[
\boxed{\mathfrak J_{2,0}<2\overline J_{10}},
\]
\[
\boxed{
7\mathfrak J_{1,1}+\mathfrak J_{1,0}
<
224\pi^2+8\overline J_{10}},
\]
以及
\[
\boxed{\mathfrak J_{8,7}<224\pi^2+8\overline J_{10}}.
\]

在数学可实施性、立即改善系数的能力以及与全局 Einstein-gap 目标的联系三者之间，**两爆破共享外部相互作用目前最均衡**；其 reduced exterior problem 必须是 gauge-fixed 的四阶 \(A^*A\) 问题。**爆破–handle 相互作用则是突破独立 handle 项的唯一直接路线**，其决定性未知量是 shrinking-handle excess 与 mixed interaction 的相对渐近阶。**large-collar 单 cell 极限最适合继续严格认证与研究退化，但不能替代 mixed-cost 理论。**
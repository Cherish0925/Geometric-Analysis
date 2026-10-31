# TTCS Independent Branch Record

```json
{
  "step_id": 12,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md",
    "Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260927_covering_geometry_and_sharp_subfamilies.md",
    "Knowledge/objects/papers/Weyl-energy-and-connected-sums-of-four-manifolds--aac98700a100--c47de95b9e22/object.md",
    "Knowledge/objects/papers/1303.0827-Critical-metrics-on-connected-sums-of-Einstein-four-manifolds--711e2a97c44e--5258e72d2de1/object.md"
  ]
}
```

## Task

Check and strengthen the proposed next cost theory after the certified subthreshold single-blow-up cell. Verify the exact subadditivity statements for the cell infima J_{k,l}, including J_{8,7}≤7J_{1,1}+J_{1,0} and J_{8,7}≤4J_{2,0}+224π², and derive precisely what inequalities would improve the currently certified balanced upper coefficient. Then compare three routes—two blow-up interaction, blow-up–handle interaction, and the complete large-collar single-cell limit—using the inherited pure-handle rigidity, actual-field lower results, the certified cell mechanism, and relevant curvature-functional gluing literature. Identify which route gives the best combination of mathematical leverage and faithful connection to the full Einstein-gap goal. Pay special attention to whether a reduced exterior interaction for J must use the fourth-order normal equation A* A rather than the second-order linearized Einstein equation, and to any gauge or boundary-data issue that could invalidate a naive Dirichlet-to-Neumann experiment.

## Output

# 科学核验备忘录：认证单爆破 cell 之后的代价理论

## 1. Cell 代价的精确定义与次可加性

在 \(\operatorname{Ric}=-g\) 归一化下，令  
\[
\mathcal C_{k,\ell}(R)
\]
表示定义在
\[
B_R^{\mathbb{CH}^2}\#k\overline{\mathbb{CP}}^{\,2}
\#\ell(S^1\times S^3)
\]
上的光滑度量，并要求它在外周一个开 collar 上与复双曲度量完全相同。记
\[
j_{k,\ell}(R)=\inf_{g\in\mathcal C_{k,\ell}(R)}
\int |\operatorname{Ric}_g+g|^2\,dV_g,
\qquad
\mathfrak J_{k,\ell}=\inf_R j_{k,\ell}(R).
\]

### 1.1 大 collar 极限本身就是 cell 下确界

若 \(R_2>R_1\)，任意 \(R_1\)-cell 都可在外面接上零代价的复双曲环区，成为 \(R_2\)-cell。因此
\[
j_{k,\ell}(R_2)\le j_{k,\ell}(R_1),
\]
从而
\[
\boxed{\mathfrak J_{k,\ell}
=\lim_{R\to\infty}j_{k,\ell}(R).}
\]

这是能量层面的精确陈述。它并不自动产生一个完整极限度量；几何收敛、曲率集中和无穷远渐近仍是额外内容。

### 1.2 精确次可加性

对任意非负整数 \(k_i,\ell_i\)，有
\[
\boxed{
\mathfrak J_{k_1+k_2,\ell_1+\ell_2}
\le
\mathfrak J_{k_1,\ell_1}
+
\mathfrak J_{k_2,\ell_2}.}
\]

证明是几何上完全精确的。给定两个近极值 cell，在一个足够大的复双曲球中取两个互不相交的等距子球，把各子球替换为相应 cell。由于两个度量在开 collar 上与复双曲度量一致，拼接是光滑的；在剩余区域
\(\operatorname{Ric}+g=0\)，故总代价恰为两个局部代价之和。令近极值误差趋于零即得上式。

由 Step 11 §3 的纯 handle 结果，
\[
\boxed{\mathfrak J_{0,\ell}=32\pi^2\ell,}
\]
其中 \(\ell>0\) 时下确界由 shrinking-core 序列逼近，但没有固定光滑 cell 取得它。因此
\[
\mathfrak J_{2,0}\le 2\mathfrak J_{1,0},
\qquad
\mathfrak J_{1,1}\le \mathfrak J_{1,0}+32\pi^2,
\]
以及
\[
\boxed{
\mathfrak J_{8,7}
\le 7\mathfrak J_{1,1}+\mathfrak J_{1,0},}
\]
\[
\boxed{
\mathfrak J_{8,7}
\le 4\mathfrak J_{2,0}+224\pi^2.}
\]

第二式中 \(224\pi^2=7\cdot32\pi^2\)。尽管没有代价恰为 \(224\pi^2\) 的固定七-handle 光滑 cell，先取其代价小于 \(224\pi^2+\varepsilon\)，再令 \(\varepsilon\to0\)，所得下确界不等式仍是精确的。

特别地，
\[
\boxed{
\mathfrak J_{8,7}
\le 8\mathfrak J_{1,0}+224\pi^2,}
\]
这就是当前分离构造的 cell 形式。

### 1.3 稳定大块代价

次可加性还给出一个比单个 \((8,7)\) block 更自然的对象。令
\[
a_n=\mathfrak J_{8n,7n}.
\]
则 \(a_{m+n}\le a_m+a_n\)，故 Fekete 引理给出
\[
\lim_{n\to\infty}\frac{\mathfrak J_{8n,7n}}n
=
\inf_{n\ge1}\frac{\mathfrak J_{8n,7n}}n.
\]
相应的稳定 cell 系数是
\[
\boxed{
c_{\mathrm{cell}}^{\mathrm{st}}
=
\frac1{72\pi^2}
\inf_{n\ge1}\frac{\mathfrak J_{8n,7n}}n.}
\]

因此单块 \(\mathfrak J_{8,7}\) 仍可能高于大块平均代价。结合 inherited actual-field 正下界和固定 cell 的全局转移，
\[
\boxed{
c_{\rm inh}\le c_*
\le c_{\mathrm{cell}}^{\mathrm{st}}
\le \frac{\mathfrak J_{8,7}}{72\pi^2}.}
\]
特别地，
\[
\mathfrak J_{8,7}\ge72\pi^2c_{\rm inh},
\]
并且
\[
7\mathfrak J_{1,1}+\mathfrak J_{1,0}\ge72\pi^2c_{\rm inh},
\qquad
4\mathfrak J_{2,0}+224\pi^2\ge72\pi^2c_{\rm inh}.
\]
这些不等式把局部 cell 理论与全局 actual-field 理论直接连接起来。

---

## 2. 改进当前认证系数所需的精确不等式

令
\[
\overline J_{10}=8\pi^2\bar\kappa
\]
表示所采用的认证单爆破上界。Step 11 的独立复核给出
\[
\bar\kappa_8
=0.999116243135324311+O(10^{-19}),
\]
于是当前 canonical 系数为
\[
c_8
=
\frac{28}{9}+\frac{\overline J_{10}}{9\pi^2}
=
4-\frac89(1-\bar\kappa_8)
<3.999214438342511.
\]

Step 10 还记录了 \(X=16\) 的较小数值
\(\bar\kappa_{16}\simeq0.99890294372\)，对应
\(3.99902484\)；但所给材料中纯 Arb 半径修正后的 canonical strict 输出是 \(X=8\)。若 \(X=16\) 也以同一修正版重新生成 strict 输出，以下所有公式只需将 \(\overline J_{10}\) 换成该值。

### 2.1 直接 \((8,7)\) cell

直接 mixed block 给出
\[
c\le \frac{\mathfrak J_{8,7}}{72\pi^2}.
\]
它优于当前认证值当且仅当
\[
\boxed{
\mathfrak J_{8,7}
<
224\pi^2+8\overline J_{10}.}
\]
对 \(X=8\) 参考值，右端约为
\[
287.943439560661\,\pi^2.
\]

若定义节省量
\[
\Delta_{87}
=
224\pi^2+8\overline J_{10}-J_{87}^{\rm new}>0,
\]
则新系数为
\[
c\le c_8-\frac{\Delta_{87}}{72\pi^2}.
\]

### 2.2 两爆破相互作用

由
\[
\mathfrak J_{8,7}\le4\mathfrak J_{2,0}+224\pi^2
\]
得到
\[
c\le \frac{28}{9}+\frac{\mathfrak J_{2,0}}{18\pi^2}.
\]
因此，改进当前认证值的精确条件是
\[
\boxed{\mathfrak J_{2,0}<2\overline J_{10}.}
\]
等价地，
\[
\frac{\mathfrak J_{2,0}}{16\pi^2}<\bar\kappa_8.
\]

若一个实际双爆破 cell 满足
\[
J_{20}^{\rm new}=2\overline J_{10}-\Delta_{20},
\qquad \Delta_{20}>0,
\]
则
\[
\boxed{
c\le c_8-\frac{\Delta_{20}}{18\pi^2}.}
\]

若目标是优于“最佳分离单爆破代价”而非当前数值证书，则所需的更内在不等式是
\[
\boxed{
\mathfrak J_{2,0}<2\mathfrak J_{1,0}.}
\]

### 2.3 爆破–handle 相互作用

七个 \((1,1)\) block 加一个 \((1,0)\) block 给出
\[
c\le
\frac{7\mathfrak J_{1,1}+\mathfrak J_{1,0}}{72\pi^2}.
\]
它优于最佳分离 cell 理论当且仅当
\[
\boxed{
\mathfrak J_{1,1}
<
\mathfrak J_{1,0}+32\pi^2.}
\]
这是 mixed 非可加性的自然严格形式。

若用同一个认证单爆破 cell 作为余下的 \((1,0)\) block，一个易于直接验证的充分条件是存在光滑 \((1,1)\) cell 满足
\[
\boxed{
J_{11}^{\rm new}<\overline J_{10}+32\pi^2.}
\]
写成
\[
J_{11}^{\rm new}
=\overline J_{10}+32\pi^2-\Delta_{11},
\qquad \Delta_{11}>0,
\]
则
\[
\boxed{
c\le c_8-\frac{7\Delta_{11}}{72\pi^2}.}
\]

更一般地，相对于当前认证值的充要代数条件是
\[
\boxed{
7\mathfrak J_{1,1}+\mathfrak J_{1,0}
<
224\pi^2+8\overline J_{10}.}
\]

### 2.4 继续降低单爆破代价

若大 collar 计算产生
\[
J_{10}^{\rm new}
=\overline J_{10}-\Delta_{10},
\qquad \Delta_{10}>0,
\]
则
\[
\boxed{
c\le c_8-\frac{\Delta_{10}}{9\pi^2}.}
\]

这条路线只能改进
\[
\frac{28}{9}+\frac{\mathfrak J_{1,0}}{9\pi^2};
\]
只要所有 handles 仍由纯 handle shrinking cores 处理，\(28/9\) 项不会消失。相比之下，mixed cell 有可能重新组织这部分代价。

---

## 3. 三条路线的科学比较

### 3.1 两爆破相互作用：最强的近期数学杠杆

这条路线的目标
\[
J_{20}<2\overline J_{10}
\]
非常敏感：相对于两个经过平滑的认证单爆破 cell，任意严格节省都能降低当前 balanced 系数。它有三个明显优势。

1. **基准是实际光滑度量。**  
   两个认证单爆破 cell 可各自选取足够窄的平滑区，使总代价任意接近 \(2\overline J_{10}\)。因此相互作用不必围绕一个不存在的极值 handle cell 展开。

2. **认证机制仍然可见。**  
   Step 10 将单 cell 节省归因于复双曲 Kähler–Einstein 背景中 \(R^+\) 的 \(\omega^\perp\) 模式、一次临界和二次补偿。两个爆破核可通过相对位置及 \(SU(2)\) 框架旋转调节这些模式在共享外部区域中的交叉项。这与曲率泛函拼接文献中的 Weyl 张量取向参数高度一致。

3. **它立即传递到真实 balanced 家族。**  
   四个双爆破 cell 加七个 pure-handle shrinking cores 给出同一 \((8,7)\) 比例，不需要改变全局拓扑窗口。

它不能把系数压到 \(28/9\) 以下，因为该分解始终保留 \(224\pi^2\) 的纯 handle 项；但它既测试真正的多爆破非可加性，又直接改善已认证系数。

### 3.2 爆破–handle 相互作用：与最终 mixed 问题联系最直接

Step 11 §4 的相对恒等式
\[
J-8\pi^2q
=
\frac{S_C-16d}{12}
+\frac14\int_C(s+4)^2
-4\left(\frac{2d}{3}-W_C\right),
\]
以及
\[
\frac{2d}{3}-W_C=12\pi^2k-B_C\le12\pi^2k
\]
表明：handles 增加 \(q\)，但没有独立的 self-dual Weyl depletion 预算；这一预算来自 blow-ups。因而
\[
\mathfrak J_{1,1}<\mathfrak J_{1,0}+32\pi^2
\]
若成立，必须来自 handle 几何改变了同一个 blow-up 模式如何使用 Weyl depletion、标量补偿和 Ricci 代价，而不是一个更便宜的孤立 handle。

这一点与完整 Einstein-gap 目标最接近，因为七个 \((1,1)\) block 已经把所有 handles 纳入 coupled cells；足够强的 mixed 节省甚至可能突破分离构造的 \(28/9\) 项。

主要解析困难是 pure-handle 下确界不由固定光滑 cell 取得。若 \(H_\rho\) 是 shrinking handle，
\[
J(H_\rho)=32\pi^2+e(\rho),\qquad e(\rho)\to0,
\]
那么一个 joint cell 的比较必须形如
\[
J_{11}(\rho)
=
\overline J_{10}+32\pi^2+e(\rho)
-I(\rho)+\text{高阶项}.
\]
只有当
\[
I(\rho)>e(\rho)+\text{高阶项}
\]
在某个尺度成立时，才得到严格 mixed 节省。单独计算一个固定尺度的交叉项还不够；相互作用随 \(\rho\to0\) 的衰减速率是核心量。

### 3.3 完整大 collar 单 cell 极限：最清晰的数值与退化实验

由于
\[
\mathfrak J_{1,0}=\lim_{R\to\infty}j_{1,0}(R),
\]
大 collar 不是辅助参数，而是单爆破下确界的精确能量表述。它还可直接复用现有 Bianchi-IX 一维曲率公式、bolt 消奇异化和 Arb 积分代码。\(X=8\) 到 \(X=16\) 的数值下降显示该方向确有可测信号。

这一方向的主要科学产出包括：

- \(\mathfrak J_{1,0}\) 的更强上界或渐近值；
- 极小序列是在 bolt 附近集中、向无穷远漂移，还是趋向完整渐近 CH 填充；
- 认证 cell 的 \(\omega^\perp\) 补偿是否具有有限极限；
- Step 8 的 response law 是否可转化为可证明的尾部展开。

但它仍只改变单爆破项。`20260928_relative_cell_cost.md` §8 已证明 \(q>0\) 的固定-collar 问题没有光滑内部临界度量，所以大 collar 极限很可能涉及非取得或几何退化，而不是收敛到一个普通固定-collar 极小点。

---

## 4. 外部相互作用的正确方程是 \(A^*A\)

令
\[
\Phi(g)=\operatorname{Ric}_g+g,
\qquad
g_0=g_{\mathbb{CH}^2},
\qquad
\Phi(g_0)=0,
\]
并记
\[
A=D\Phi_{g_0}.
\]
对 \(g_\varepsilon=g_0+\varepsilon h\)，有
\[
\Phi(g_\varepsilon)
=
\varepsilon Ah+O(\varepsilon^2),
\]
故在一个复双曲外部区域 \(\Omega\) 上
\[
J_\Omega(g_\varepsilon)
=
\varepsilon^2\int_\Omega |Ah|^2\,dV_{g_0}
+O(\varepsilon^3).
\]

因此二次近似的欧拉方程是
\[
\boxed{A^*Ah=0,}
\]
而不是
\[
Ah=0.
\]

后者描述线性化 Einstein 变形；前者描述在给定接口迹数据下最小化平方 Ricci defect 的外部响应。即使在 Bianchi gauge 中 \(A\) 成为形式自伴的二阶 Laplace 型算子，正确方程仍是四阶的 \(A^2h=0\)。

这与两份相关文献的结构吻合：

- Malchiodi–Malizia 对 Weyl 能量采用 biharmonic interpolation；其严格节省来自四阶 Hessian 和 Weyl 张量交叉项。
- Gursky–Viaclovsky 的 \(B^t\) 拼接使用四阶 gauge-fixed 算子，其 Kuranishi 首项包含
  \[
  W(z_0)\circledast W(y_0)+\text{scalar/mass 项}.
  \]

这些结果提供了四阶插值、相对旋转和交叉项组织方式，但不能直接推出 \(\mathfrak J_{2,0}<2\mathfrak J_{1,0}\)：Weyl 能量与 \(J\) 不同，标量及体积项仍会改变总符号；而且 Malchiodi–Malizia 的同手性例外也必须核对。复双曲背景在本文取向下满足 \(W^-=0\)，不能仅凭其闭流形定理断言这里存在严格节省。

还有一个重要区别：\(A^*A\) 只是在复双曲外部区域上的精确二次 normal equation。若直接在线性化点取认证 cell 的非 Einstein 核心，\(J\) 的一次变分一般不为零，Hessian 还含有由原始 defect 产生的低阶项；此时不能把整个 cell 的变分简化为纯 \(A^*A\)。

---

## 5. Dirichlet–Neumann 实验必须保留的接口结构

一个直接把二阶线性化 Einstein 方程送入数值 Dirichlet–Neumann 求解器的实验，会遗漏以下数学结构。

### 5.1 四阶迹数据

平滑拼接核心与外部区域时，固定的不只是 \(h|_\Sigma\)，还包括一阶法向迹；等价的几何数据是诱导度量、第二基本形式以及坐标固定信息。对
\[
Q(h)=\int_\Omega |Ah|^2
\]
作变分后，Green 公式的接口项同时含有 \(\delta h\) 与
\(\nabla_\nu\delta h\)。因此响应算子应当是四阶 Calderón 型映射
\[
(h,\nabla_\nu h)
\longmapsto
(\text{与 }Ah,\nabla_\nu Ah\text{ 有关的共轭数据}),
\]
而不是二阶映射 \(h\mapsto\nabla_\nu h\)。

用二阶方程 \(Ah=0\) 同时匹配度量和一阶法向迹通常成为过定问题；只匹配度量又不足以产生所需的光滑 cell。

### 5.2 微分同胚零模

由于 \(\Phi\) 是自然张量，
\[
A(\mathcal L_Xg_0)
=
\mathcal L_X\Phi(g_0)=0.
\]
所以未经处理的 \(Q\) 在纯 gauge 方向上退化。若 \(X\) 在接口处不固定，它会改变坐标表达下的 Dirichlet 与 Neumann 数据，而不改变几何代价。由此得到的交叉节省可能只是接口重标记。

可用的设置是：

- 选取相对于 \(g_0\) 的 Bianchi slice；
- 只允许在外 collar 上恒等的微分同胚；
- 核心和外部区域使用同一接口标记；
- 将 trace scaling 与 gauge 区分开，因为固定宇宙常数下 \(h=cg_0\) 不是纯 gauge 模式。

### 5.3 完整 metric germ，而非仅诱导三维度量

Cell 定义要求外 collar 上整个度量 germ 与 CH 相同。仅固定接口上的诱导三维度量，不能控制法向导数、第二基本形式和相对 Chern–Weil transgression。`20260927_covering_geometry_and_sharp_subfamilies.md` §6.1–6.2 已给出同类现象：相同的内禀圆度并不决定填充的 chiral Weyl 代价，法向 germ 可以携带任意大的能量信息。

### 5.4 共享外部尾部才会产生交叉项

若两个认证 cell 保留各自完整的 exact-CH collar，并被放在互不相交的子球中，则 defect 支持不相交，总代价严格相加，没有交叉项。两爆破实验必须在更内侧截取两个核心，让它们共享同一个复双曲外部响应。在线性层面，若 \(h_1,h_2\) 是共享外部解，
\[
Q(h_1+h_2)
=
Q(h_1)+Q(h_2)
+2\int_\Omega\langle Ah_1,Ah_2\rangle.
\]
相对位置和框架旋转可改变最后一项的符号；但它必须由 gauge-compatible 四阶响应算子计算。

---

## 6. 综合判断

三条路线承担的数学任务不同：

| 路线 | 改进当前认证值的目标 | 对完整问题的作用 |
|---|---:|---|
| 两爆破相互作用 | \(J_{20}<2\overline J_{10}\) | 直接改善 balanced 系数；测试多爆破非可加性；仍保留 \(28/9\) handle 项 |
| 爆破–handle 相互作用 | \(J_{11}<\overline J_{10}+32\pi^2\) | 直接测试 mixed 非可加性；有机会重新组织 handle 项 |
| 大 collar 单 cell | \(J_{10}^{\rm new}<\overline J_{10}\) | 最易复用现有认证工具；精确研究 \(\mathfrak J_{1,0}\) 与退化，但不触及 mixed handle 机制 |

**综合数学杠杆与对完整 Einstein-gap 问题的实际映射，两爆破相互作用是目前最均衡的路线。** 它有实际光滑认证 cell 作为比较基准，任何严格节省都会产生新的 balanced 上界；四阶曲率泛函拼接文献也提供了最接近的交叉项框架。正确的 reduced problem 是 gauge-fixed \(A^*A\) 外部响应，而不是二阶线性化 Einstein Dirichlet–Neumann 问题。

**若核心问题进一步转为能否突破绝对 \(28/9\) 项，则爆破–handle 相互作用不可替代。** 两爆破和单 cell 路线即使充分成功，也只能降低 blow-up 部分；mixed cell 才能改变 handle 与 blow-up 的共同支付方式。其关键未知量是 shrinking handle 误差 \(e(\rho)\) 与 mixed 交叉节省 \(I(\rho)\) 的相对渐近阶。

大 collar 单 cell 极限则是最清晰的数值控制实验和退化模型，并可为两爆破共享外部问题提供经过认证的单核迹数据、尾部模式和尺度选择。
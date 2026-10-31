# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 3,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step3_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step3_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the proposed fixed-exterior orbifold rigidity lemma in Section 7 of the note. Exact setting: X=CH^2/Γ is a closed smooth complex-hyperbolic surface; D is an embedded metric ball with Vol(D)<Vol(X)/2; U=X\D° isometrically embeds as the unchanged open exterior of a compact connected locally CH orbifold base O arising from a stationary fixed-collar degeneration. The argument says O=CH^2/Γ', equality of the exterior germ yields Γ<Γ', volumes give Vol(O)=Vol(X)/[Γ':Γ], while Vol(O)>=Vol(U)>Vol(X)/2, so the index is one and O=X smoothly. Verify each topological, holonomy, developability, completeness, volume, and unique-continuation step; identify and repair any hidden issue, especially whether an isometric embedding of U really gives the lattice inclusion and whether orbifold points or nontrivial developing maps can evade it. Then state the strongest rigorously supportable lemma and what it actually removes from the bubble-tree problem.

## Integrated Scientific Memo

# 固定外部 orbifold 刚性：核验、修正与最强结论

## 1. 结论概览

Section 7 的核心“格点包含—体积—指数”论证是正确的，但必须补出以下关键点：

1. \(\mathcal O\) 必须是紧致、连通、有效、无边界的光滑 Riemannian orbifold；仅有正则极限的度量完成还不够。
2. \(U\to\mathcal O\) 必须是同维光滑单射局部等距，并落在 \(\mathcal O_{\rm reg}\)；抽象的距离保持子集映射不足以产生 holonomy 包含。
3. 真正携带 \(\Gamma\) 的是完整外部 \(U=X\setminus D^\circ\)，不是一小段 collar germ。
4. 格点包含来自 developing-map 等变性：
   \[
   A\Gamma A^{-1}\subset\Gamma',
   \]
   不能只写“外部 germ 相同，故 \(\Gamma<\Gamma'\)”。
5. 紧致性给出 orbifold 完备性，完备性才排除 developing image 是 \(\mathbb{CH}^2\) 真开子集的可能。
6. 体积应解释为 orbifold Riemannian 体积。

在这些假设下，Section 7 原有的 \(d<\operatorname{Vol}(X)/2\) 论证完全成立。事实上，利用外部嵌入的单射性还可加强：对一个或有限多个互不相交嵌入球，**不需要任何体积小于一半的假设**，即可推出 \(\Gamma'=\Gamma\)。

此外，在这种有限点、非塌缩、stationary orbifold-base 退化中，相对 Chern–Weil 恒等式与 Fatou 下半连续性已经直接给出
\[
\liminf J\ge 8\pi^2(k+4\ell).
\]
因此，whole-tree APS charge theorem 对这一退化类别的**阈值下界**并非必需；它仍可能用于等号、近等号及拓扑在树中的精细分布。

---

## 2. Stationarity 到局部复双曲：所需的精确论证

令
\[
J(g)=\int |\operatorname{Ric}_g+g|^2\,dV_g.
\]
必须假设 stationarity 已经传递到 orbifold 正则部分；这不是任意最小化序列自动拥有的性质。若有 \(C^{2,\alpha}_{\mathrm{loc}}\) 收敛且序列为真正最小化序列，可用紧支撑变分移植论证传递 stationarity，但相关 compactness 与正则性本身仍是额外分析输入。

### 2.1 标量方程

紧支撑共形变分给出
\[
(\Delta_++1)(s+4)=0
\]
于正则部分。设 \(Y\) 是包含固定外部的正则连通分支。由于 \(s=-4\) 于其中一个非空 CH 开集，唯一延拓给出
\[
s\equiv-4\qquad\text{于 }Y.
\]

若方程已经在整个紧致 orbifold 上逐图成立，也可直接积分：
\[
0=\int_{\mathcal O}(s+4)(\Delta_+(s+4)+(s+4))
 =\int_{\mathcal O}\bigl(|\nabla(s+4)|^2+(s+4)^2\bigr).
\]
但在一般 bubble-tree 极限中，较稳妥的是先限制到包含 collar 的正则分支。

### 2.2 张量方程

令
\[
E=\operatorname{Ric}+g.
\]
在 \(s=-4\) 后，Euler–Lagrange 方程化为
\[
\Delta_-E=-2\operatorname{Rm}(E)+\frac12|E|^2g.
\]
对这个已固定的解，右侧可以写成光滑零阶线性算子作用于 \(E\)：
\[
\Delta_-E=\mathcal A(x)E,\qquad
\mathcal A_x(T)=-2\operatorname{Rm}_x(T)
 +\frac12\langle E_x,T\rangle g_x.
\]
该系统主符号为标量，局部系数有界。因为 \(E=0\) 于 CH 外部开集，椭圆唯一延拓给出
\[
E\equiv0\qquad\text{于 }Y.
\]

### 2.3 Einstein 到局部 CH

Einstein 度量在调和坐标中实解析。固定外部上
\[
\nabla\operatorname{Rm}=0
\]
且曲率张量具有复双曲代数型，解析延拓给出同样结论于 \(Y\)。在 orbifold chart 中提升度量；正则点稠密，故 \(E=0\) 与复双曲曲率型连续延伸到 chart 中心。于是相关 orbifold 完成局部复双曲。

这里有两个不能省略的条件：

- \(Y\) 的度量完成确实是具有有限局部群的光滑 orbifold；唯一延拓本身不证明这一点。
- 若极限允许 multi-fold points，应先分离含固定外部的 sheet，再对其 orbifold 完成应用论证。

---

## 3. 完备性、developability 与全局商

设现在 \(\mathcal O\) 是紧致、连通、有效、无边界的局部 CH Riemannian orbifold。紧致性蕴含测地完备性。

局部 CH charts 赋予它一个
\[
(\operatorname{Isom}(\mathbb{CH}^2),\mathbb{CH}^2)
\]
orbifold 结构。orbifold universal cover 上的 developing map
\[
\operatorname{dev}:\widetilde{\mathcal O}_{\rm orb}
 \longrightarrow\mathbb{CH}^2
\]
是局部等距。完备性保证它为覆盖；因 \(\mathbb{CH}^2\) 单连通，developing map 是全局等距。因此
\[
\mathcal O=\mathbb{CH}^2/\Gamma',
\]
其中 \(\Gamma'<\operatorname{Isom}(\mathbb{CH}^2)\) 离散、余紧，可能含 torsion。

这一步排除了两种潜在规避：

- developing image 只是 \(\mathbb{CH}^2\) 的真开子集；
- “非平凡 developing map”产生不同的局部模型。

developing map 的选择只差一个全局 \(A\in\operatorname{Isom}(\mathbb{CH}^2)\)。

---

## 4. 外部嵌入为什么确实给出格点包含

令
\[
X=\mathbb{CH}^2/\Gamma,\qquad
U=X\setminus D^\circ.
\]
这里可取闭球补或其带边界版本；如需开流形 holonomy，可略缩球并使用
\(X\setminus\overline D\)。由于 \(D\) 是四球且接口为 \(S^3\)，van Kampen 给出
\[
\pi_1(U)\cong\pi_1(X)=\Gamma.
\]

### 4.1 嵌入像必须位于正则部分

若
\[
\iota:U\longrightarrow\mathcal O
\]
是同维光滑单射局部等距，则其像不能通过有效 orbifold 奇异点。奇异点 \(p\) 的小球体积密度为
\[
\lim_{r\downarrow0}
 \frac{\operatorname{Vol}B(p,r)}{\omega_4r^4}
 =\frac1{|G_p|},
\]
而光滑源点密度为 \(1\)。局部等距保持这一密度，故 \(G_p=1\)。因此
\[
\iota(U)\subset\mathcal O_{\rm reg}.
\]

若所谓“等距嵌入”仅是度量空间意义的距离保持映射，则上述平滑 lifting 和 holonomy 论证并不自动成立；固定外部的 Cheeger–Gromov 嵌入应明确包含光滑局部等距性质。

### 4.2 Developing-map 等变性

取 \(U\) 的 CH developing map 与 \(\mathcal O\) 的 developing map。提升 \(\iota\) 后，二者在连通域上相差一个全局等距 \(A\)：
\[
\operatorname{dev}_{\mathcal O}\circ\widetilde\iota
 =A\circ\operatorname{dev}_{U}.
\]
因此对每个 \(\gamma\in\pi_1(U)\)，
\[
\rho_{\mathcal O}(\iota_*\gamma)
 =A\rho_U(\gamma)A^{-1}.
\]
由于 \(\rho_U\) 是原闭 CH 流形的忠实 holonomy，像为 \(\Gamma\)，遂得
\[
A\Gamma A^{-1}\subset\Gamma'.
\]

这也直接说明 \(\iota_*\) 到 orbifold fundamental group 是单射。故 orbifold points 或不同 developing-map 选择都不能规避格点包含。

---

## 5. 原体积论证的严格版本

记
\[
H=A\Gamma A^{-1}\subset\Gamma'.
\]
因为 \(H\) 是余紧格点而 \(\Gamma'\) 离散，指数
\[
n=[\Gamma':H]
\]
有限。等价地，
\[
\mathbb{CH}^2/H\longrightarrow\mathbb{CH}^2/\Gamma'
\]
是有限 orbifold covering。于是 orbifold 体积满足
\[
\operatorname{Vol}(\mathcal O)
 =\frac{\operatorname{Vol}(\mathbb{CH}^2/H)}{n}
 =\frac{V}{n}.
\]
另一方面，\(\iota\) 单射且体积保持，所以
\[
\operatorname{Vol}(\mathcal O)
 \ge\operatorname{Vol}(U)=V-d.
\]
若 \(d<V/2\)，则
\[
\frac Vn\ge V-d>\frac V2,
\]
故 \(n<2\)，从而 \(n=1\)。因此
\[
\Gamma'=A\Gamma A^{-1}.
\]
由于 \(\Gamma\) 无 torsion，\(\Gamma'\) 也无 torsion，故 \(\mathcal O\) 实际光滑，并与 \(X\) 全局等距。

此外，全局等距与给定 \(\iota\) 在一个外部 germ 上具有相同提升 \(A\)，由连通性及局部等距的唯一延拓，它在整个 \(U\) 上等于 \(\iota\)。

---

## 6. 加强：体积小于一半并非必要

可进一步证明，只要删去的是一个或有限多个互不相交嵌入四球，就不需要 \(d<V/2\)。

共轭后设
\[
\Gamma\subset\Gamma',\qquad
q|_{\widetilde U}=\iota\circ\pi|_{\widetilde U},
\]
其中
\[
\widetilde U=\pi^{-1}(U)\subset\mathbb{CH}^2.
\]

取 \(g\in\Gamma'\setminus\Gamma\)。若
\[
g\widetilde U\cap\widetilde U\ne\varnothing,
\]
则存在 \(x,gx\in\widetilde U\)。因为
\[
q(x)=q(gx)
\]
且 \(\iota\) 单射，存在 \(\gamma\in\Gamma\) 使
\[
gx=\gamma x.
\]
但 \(x\) 位于 \(\mathcal O_{\rm reg}\) 的提升中，其 \(\Gamma'\)-稳定子群平凡，所以 \(g=\gamma\)，矛盾。因此
\[
g\widetilde U\cap\widetilde U=\varnothing.
\]
故
\[
g\widetilde U\subset
\mathbb{CH}^2\setminus\widetilde U=\pi^{-1}(D^\circ).
\]
右侧是互不相交的有界提升球之并。由于 \(g\widetilde U\) 连通，它必须包含于其中一个有界球。但 \(\widetilde U\) 是 \(\Gamma\)-不变且无界，故其等距像 \(g\widetilde U\) 也无界，矛盾。

因此不存在 \(g\in\Gamma'\setminus\Gamma\)，即
\[
\Gamma'=\Gamma.
\]

同一证明适用于有限多个互不相交球，只要外部连通。这一加强对多 cell 构造尤其有用。

---

## 7. 最强可严格支持的刚性引理

### 固定外部 orbifold 刚性引理

设
\[
X=\mathbb{CH}^2/\Gamma
\]
为闭光滑复双曲曲面，\(\Gamma\) 为无 torsion 余紧格点。设 \(D\subset X\) 是一个闭嵌入四球，或有限个互不相交闭嵌入四球之并，并假设
\[
U=X\setminus D^\circ
\]
连通。

设 \((\mathcal O,g)\) 是紧致、连通、有效、无边界的局部复双曲 Riemannian orbifold，且存在光滑单射局部等距
\[
\iota:(U,g_X)\longrightarrow(\mathcal O,g).
\]
则存在 \(A\in\operatorname{Isom}(\mathbb{CH}^2)\) 使
\[
\mathcal O\cong
\mathbb{CH}^2/(A\Gamma A^{-1})\cong X.
\]
特别地，\(\mathcal O\) 没有 orbifold 奇异点，且该全局等距在 \(U\) 上等于 \(\iota\)。不需要体积小于一半的假设。

“局部复双曲”可替换为以下分析假设：

- \(g\) 是光滑 orbifold metric；
- 在固定外部与 \(g_X\) 完全相同；
- 包含该外部的正则分支对 \(J\) 的所有紧支撑 metric variations 为 stationary；
- Euler–Lagrange 方程与 orbifold completion 已由极限理论合法取得。

若允许 ineffective orbifolds，度量只能检测 effective reduction；严格结论应表述为 effective reduction 与 \(X\) 等距。

---

## 8. 对 bubble-tree 下界的进一步后果

对
\[
C=D\#k\overline{\mathbb{CP}}^{\,2}
 \#\ell(S^1\times S^3),\qquad q=k+4\ell,
\]
源材料给出每个光滑 fixed-collar metric 的精确恒等式
\[
J-8\pi^2q
 =
\int_C\left[
\frac{(s+3)^2}{3}+1+4|W^+|^2
\right]\,dV-4d.
\tag{8.1}
\]
记其中密度为 \(F(g)\)。它处处满足
\[
F(g)\ge1,
\]
而 CH metric 上
\[
s=-4,\qquad |W^+|^2=\frac23,
\]
故
\[
F(g_{\rm CH})=4.
\]

若一列 fixed-collar metrics 在有限集合外 \(C^2_{\rm loc}\) 收敛到上述 stationary orbifold base，则刚性引理说明 base 正是原 CH 球。取
\[
K\Subset D\setminus S
\]
并令 \(K\uparrow D\setminus S\)。由局部 \(C^2\) 收敛，
\[
\int_{\Phi_i(K)}F(g_i)\,dV_{g_i}
 \longrightarrow 4\,\operatorname{Vol}(K).
\]
在补集上只使用 \(F\ge1\)，甚至直接丢弃其非负积分，即得
\[
\liminf_i(J(g_i)-8\pi^2q)
 \ge4\operatorname{Vol}(K)-4d.
\]
令 \(\operatorname{Vol}(K)\uparrow d\)，得到
\[
\boxed{\liminf_i J(g_i)\ge8\pi^2q.}
\]

因此，在“有限点集中 + 非塌缩 orbifold completion + stationary base + 足够局部收敛”的情形下：

- quotient-ended ALE levels；
- 各内部接口的 \(1/|\Lambda|\) 与 APS \(\eta\)-项；
- 标记类如何分布于各 bubble；

都不能使总能量降到 \(8\pi^2q\) 以下。阈值下界已由全 cell 的相对恒等式得到，无需逐层分配 charge。

不过不应过度强化等号结论：由上述 Fatou 论证本身只能得到相应积分余量趋零的约束；若没有额外 non-collapsing、volume convergence 或 energy identity，不能自动断言所有 neck 和 bubble 在每一尺度都具有完整的 scalar-flat、\(W^+=0\) 分类。

---

## 9. 它实际从 bubble-tree 问题中移除了什么

严格移除的是：

1. **残余 CH superquotient base：**  
   不可能出现不同格点、较小体积或带 torsion 的
   \(\mathbb{CH}^2/\Gamma'\)。

2. **base orbifold singularities：**  
   包含固定外部的 base component 必为原光滑 \(X\)。

3. **root quotient group：**  
   base 中被替换区域是普通 CH 球，因而每棵相应 rooted tree 的外接口是 \(S^3\)，不是 \(S^3/\Lambda\)。

4. **该退化类别的 whole-tree 阈值证明：**  
   对有限点 stationary orbifold-base 退化，(8.1) 已直接给出
   \(\liminf J\ge8\pi^2q\)。

仍未解决的是：

- 任意近极小序列的 \(\varepsilon\)-正则性和 orbifold compactness；
- stationarity 向极限的传递；
- collapse、非有限点集中、codimension \(1\) 或 \(2\) 退化；
- non-orbifold completion 或 multi-fold 现象的排除；
- 非退化光滑 cell 的耦合 coercivity 问题；
- 阈值等号和近等号时内部 bubble/neck 的完整分类与标记拓扑分解。

所以最准确的结论是：**固定外部刚性彻底排除了 stationary、非塌缩、有限点 orbifold-base 退化作为 subthreshold 机制；剩余危险必须来自 compactness 假设失效、非 stationary 极限、塌缩或真正的非退化 cell coercivity 失败。**
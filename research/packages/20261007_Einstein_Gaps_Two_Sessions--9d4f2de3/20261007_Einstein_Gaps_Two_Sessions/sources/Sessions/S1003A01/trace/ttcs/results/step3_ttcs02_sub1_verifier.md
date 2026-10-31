# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Check the proposed fixed-exterior orbifold rigidity lemma in Section 7 of the note. Exact setting: X=CH^2/Γ is a closed smooth complex-hyperbolic surface; D is an embedded metric ball with Vol(D)<Vol(X)/2; U=X\D° isometrically embeds as the unchanged open exterior of a compact connected locally CH orbifold base O arising from a stationary fixed-collar degeneration. The argument says O=CH^2/Γ', equality of the exterior germ yields Γ<Γ', volumes give Vol(O)=Vol(X)/[Γ':Γ], while Vol(O)>=Vol(U)>Vol(X)/2, so the index is one and O=X smoothly. Verify each topological, holonomy, developability, completeness, volume, and unique-continuation step; identify and repair any hidden issue, especially whether an isometric embedding of U really gives the lattice inclusion and whether orbifold points or nontrivial developing maps can evade it. Then state the strongest rigorously supportable lemma and what it actually removes from the bubble-tree problem.

## Output

# 固定外部 orbifold 刚性：核验备忘录

## 1. 核心结论

指数—体积论证在适当补全假设后成立。关键群论步骤不能只写成“外部 germ 相同，所以 \(\Gamma<\Gamma'\)”；严密论证需要：

1. \(\mathcal O\) 是紧致、连通、有效、闭的光滑 Riemannian orbifold，因此其局部 CH 度量完备；
2. “\(U\) 等距嵌入”是同维数的光滑单射局部等距映射，而不只是某个子集上的距离保持；
3. 使用整个外部
   \[
   U_0=X\setminus\overline D,
   \]
   而不仅是一小段 collar，因为 \(\pi_1(U_0)\cong\pi_1(X)=\Gamma\)；
4. 通过 developing map 的等变性得到
   \[
   A\Gamma A^{-1}\subset\Gamma',
   \]
   其中 \(A\in\operatorname{Isom}(\mathbb{CH}^2)\)；
5. 体积一律取 orbifold Riemannian 体积。

在这些假设下，
\[
[\Gamma':A\Gamma A^{-1}]=1,
\]
故 \(\mathcal O\) 是光滑的，并与 \(X\) 全局等距；给定的外部嵌入还是该全局等距映射在 \(U_0\) 上的限制。

---

## 2. Stationarity 确实推出局部 CH

这一部分使用 I54 的 (8.1)、(8.2)，但要说明方程如何从正则部分延伸到 orbifold 图。

令
\[
\mathscr J(g)=\int_{\mathcal O}|\operatorname{Ric}_g+g|^2\,dV_g.
\]
在可变区域内，对紧支撑共形变分 \(\dot g=2fg\)，有
\[
\dot{\mathscr J}
 =4\int_{\mathcal O}f(\Delta_+s+s+4)\,dV.
\]
固定外部本身是 CH，故那里 \(s=-4\)，相同方程自动成立。由于 metric germ 在 overlap 上完全相同，没有接口型分布项。因此正则部分上处处有
\[
(\Delta_++1)(s+4)=0. \tag{2.1}
\]

设 \(u=s+4\)。局部唯一延拓可直接用于 (2.1)：在 orbifold 图上提升后，它是普通光滑椭圆方程，而 \(u\) 在 CH 外部开集上为零。对于紧致 orbifold 还有更直接的积分论证：
\[
0=\int_{\mathcal O}u(\Delta_+u+u)
 =\int_{\mathcal O}\bigl(|\nabla u|^2+u^2\bigr),
\]
所以
\[
s\equiv-4. \tag{2.2}
\]

令
\[
E=\operatorname{Ric}+g.
\]
全张量变分及 \(s=-4\) 给出 I54 的方程
\[
\Delta_-E=-2\operatorname{Rm}(E)+\frac12|E|^2g. \tag{2.3}
\]
对这个已给定的解，可以把右端写成线性零阶算子作用于 \(E\)：
\[
\mathcal A_x(T)
 =-2\operatorname{Rm}_x(T)+\frac12\langle E_x,T\rangle g_x,
\qquad
\Delta_-E=\mathcal A(x)E.
\]
局部系数光滑且有界。由于 \(E=0\) 于 CH 外部开集，Aronszajn 型唯一延拓给出
\[
E\equiv0
\]
于连通正则部分。由定向光滑四维序列产生的有效 orbifold，其局部群位于 \(SO(4)\)，奇异层余维至少二，正则部分连通。提升到各 orbifold 图后，\(E\) 由连续性在图中心也为零。因此
\[
\operatorname{Ric}_{\mathcal O}=-g_{\mathcal O}. \tag{2.4}
\]

DeTurck–Kazdan 的 Einstein 解析性可逐图应用。张量 \(\nabla\operatorname{Rm}\) 在 CH 外部开集上为零，解析延拓给出
\[
\nabla\operatorname{Rm}\equiv0.
\]
曲率张量在外部具有复双曲型；平行移动保持其代数型，因此每一点都有 CH 邻域。orbifold 图中的提升也具有相同性质。于是 stationary base 的确是局部复双曲 orbifold。

这一推导依赖正则极限具有光滑 orbifold 延拓，并且 stationarity 能传递到正则部分。仅有一个任意最小化序列并不会自动提供这些方程。

---

## 3. 完备局部 CH orbifold 必为全局商

设此时 \(\mathcal O\) 已是紧致、连通、有效、闭的局部 CH orbifold。紧致性给出 orbifold 测地完备性。

局部 CH 图赋予 \(\mathcal O\) 一个
\[
\bigl(\operatorname{Isom}(\mathbb{CH}^2),\mathbb{CH}^2\bigr)
\]
结构。其 orbifold universal cover 上有 developing map
\[
\operatorname{dev}:\widetilde{\mathcal O}_{\mathrm{orb}}
 \longrightarrow\mathbb{CH}^2.
\]
完备局部等距结构的标准完备化定理，等价地 orbifold Cartan–Hadamard 定理，说明：

- universal orbifold cover 实际是流形；
- \(\operatorname{dev}\) 是完备局部等距；
- 测地线提升使其满射；
- 因 \(\mathbb{CH}^2\) 单连通，\(\operatorname{dev}\) 是全局等距。

所以
\[
\mathcal O=\mathbb{CH}^2/\Gamma',
\]
其中
\[
\Gamma'<\operatorname{Isom}(\mathbb{CH}^2)
\]
是离散余紧群，可以含有限阶元素。使用全等距群可以同时容纳 holomorphic 与 antiholomorphic 局部等距。

因此，完备性排除了 developing image 只是 \(\mathbb{CH}^2\) 的真开子集这一可能。若手中只有删除了集中点的正则空间，而尚未得到紧致 orbifold 完成，则这一步不能使用。

---

## 4. 外部嵌入如何真正产生格点包含

### 4.1 外部携带全部基本群

令 \(D\) 为光滑嵌入的四球，并取
\[
U_0=X\setminus\overline D.
\]
由 van Kampen，
\[
\pi_1(U_0)\xrightarrow{\cong}\pi_1(X)=\Gamma,
\]
因为球及其球面 collar 的相关基本群均平凡。这里四维性很重要：接口是 \(S^3\)。

\(X\) 的 CH developing map 限制到 \(U_0\)，其 holonomy 为
\[
\rho_U:\pi_1(U_0)\longrightarrow\operatorname{Isom}(\mathbb{CH}^2),
\qquad
\rho_U(\pi_1(U_0))=\Gamma,
\]
而且 \(\rho_U\) 忠实。

### 4.2 嵌入像位于正则部分

若
\[
f:U_0\longrightarrow\mathcal O
\]
是同维数光滑单射局部等距，则其像不能穿过有效 orbifold 奇异点。事实上，若 \(q\) 的局部稳定群为 \(K_q\)，则小球体积密度为
\[
\lim_{r\downarrow0}
\frac{\operatorname{Vol}B(q,r)}{\omega_4r^4}
=\frac1{|K_q|}.
\]
光滑源点的密度为 \(1\)，局部等距保持该密度，所以 \(|K_q|=1\)。因此
\[
f(U_0)\subset\mathcal O_{\mathrm{reg}}.
\]

这也说明“等距嵌入”应理解为 Cheeger–Gromov 收敛中产生的光滑局部等距嵌入。若只给一个抽象子集上的距离保持映射，下面的 holonomy 推导没有足够结构。

### 4.3 Holonomy 等变性

选取 \(\mathcal O=\mathbb{CH}^2/\Gamma'\) 的 developing 坐标。局部提升 \(f\) 后，两个 CH developing map 相差某个全局等距
\[
A\in\operatorname{Isom}(\mathbb{CH}^2):
\qquad
\operatorname{dev}_{\mathcal O}\circ\widetilde f
 =A\circ\operatorname{dev}_{U}.
\]
对每个 \(\gamma\in\pi_1(U_0)\)，等变性给出
\[
\rho_{\mathcal O}(f_*\gamma)
 =A\rho_U(\gamma)A^{-1}
 =A\gamma A^{-1}. \tag{4.1}
\]
因此
\[
H:=A\Gamma A^{-1}\subset\Gamma'. \tag{4.2}
\]

这同时证明 \(f_*\) 到 orbifold 基本群是单射：若 \(f_*\gamma=1\)，则 (4.1) 给出 \(A\gamma A^{-1}=1\)，从而 \(\gamma=1\)。

所以真正产生格点包含的是：

- 完整外部 \(U_0\) 携带 \(\Gamma\)；
- 局部等距的 developing-map 等变性；
- \(\mathcal O\) 的完备商表示。

单独一小段 collar germ 只确定局部等距 \(A\)，并不携带足够的基本群信息。

---

## 5. 有限指数与体积

由于 \(H=A\Gamma A^{-1}\) 是余紧格点而 \(\Gamma'\) 离散，包含
\[
H\subset\Gamma'
\]
必为有限指数。等价地，自然 orbifold covering
\[
\mathbb{CH}^2/H\longrightarrow\mathbb{CH}^2/\Gamma'
\]
的源是紧致空间，其离散纤维只能有限。记
\[
n=[\Gamma':H]\in\mathbb N.
\]
对 orbifold Riemannian 体积，
\[
\operatorname{Vol}(\mathcal O)
 =\frac{\operatorname{Vol}(\mathbb{CH}^2/H)}{n}
 =\frac{V}{n}. \tag{5.1}
\]
有限稳定群所在集合测度为零，故这一覆盖度—体积公式即使 \(\Gamma'\) 含 torsion 也成立。

另一方面，\(f\) 在正则部分体积保持且单射，所以
\[
\operatorname{Vol}(\mathcal O)
 \ge \operatorname{Vol}(U_0)
 =V-d. \tag{5.2}
\]
结合 \(d<V/2\)，得到
\[
\frac{V}{n}\ge V-d>\frac V2,
\qquad n<2.
\]
因此
\[
n=1,\qquad \Gamma'=A\Gamma A^{-1}. \tag{5.3}
\]

由于 \(\Gamma\) 无 torsion，\(\Gamma'\) 也无 torsion，故 \(\mathcal O\) 没有 orbifold 奇异点。映射
\[
F:X\longrightarrow\mathcal O,\qquad
F([x]_\Gamma)=[Ax]_{\Gamma'}
\]
是全局等距。它与 \(f\) 在一个 germ 上有同一提升 \(A\)，而 \(U_0\) 连通，所以
\[
f=F|_{U_0}. \tag{5.4}
\]
因此嵌入外部的补集正是全局等距像下的原 CH 球。

---

## 6. 最强可严格支持的引理

**固定外部 orbifold 刚性引理。**  
设
\[
X=\mathbb{CH}^2/\Gamma
\]
为闭光滑复双曲曲面，\(\Gamma\) 为无 torsion 余紧格点，\(V=\operatorname{Vol}(X)\)。设 \(D\subset X\) 为光滑嵌入的 metric \(4\)-ball，\(d=\operatorname{Vol}(D)<V/2\)，并令 \(U_0=X\setminus\overline D\)。

设 \((\mathcal O,g_{\mathcal O})\) 为紧致、连通、有效、闭的局部复双曲 Riemannian \(4\)-orbifold，并存在光滑单射局部等距
\[
f:(U_0,g_X)\longrightarrow(\mathcal O,g_{\mathcal O}).
\]
则存在
\[
A\in\operatorname{Isom}(\mathbb{CH}^2)
\]
使
\[
\mathcal O\cong
\mathbb{CH}^2/(A\Gamma A^{-1})
\cong X
\]
作为 Riemannian orbifold；事实上 \(\mathcal O\) 是光滑流形，且 \(f\) 是一个全局等距映射在 \(U_0\) 上的限制。

其中“局部复双曲”可以由以下分析输入推出：\(g_{\mathcal O}\) 是光滑 orbifold metric，在固定外部与 \(g_X\) 完全相同，并且在可变区域对所有紧支撑 metric variations 为 \(\mathscr J\)-stationary，且相应 Euler–Lagrange 方程已传递到正则极限。

若允许 ineffective orbifold，度量只能识别其 effective reduction；此时严格结论是 effective reduction 与 \(X\) 等距。几何收敛中通常采用 effective orbifold。

---

## 7. 对 bubble tree 的实际作用

在标准非塌缩 orbifold bubble-tree 情形中，上述引理给出：

1. **紧致 base 不是新的 CH superquotient。**  
   不会留下具有 torsion、较小体积或不同格点的
   \(\mathbb{CH}^2/\Gamma'\)。

2. **base metric 和 topology 都是原来的 \(X\)。**  
   固定外部的嵌入由全局 CH 等距延伸，其补集是标准 CH 球。

3. **base 上没有 orbifold 奇异点。**  
   因而每棵聚集树的整体外接口是普通 \(S^3\)，其外端群为平凡群。在通常的树匹配中，这正是 root 端的群。

4. **更深层仍可出现 \(S^3/\Lambda\)。**  
   某个 bubble 自身的奇异点、下一层 ALE 空间以及内部 neck 仍可携带 \(\Lambda\neq1\)。相应 APS \(\eta\)-项属于树内部接口的配对记账；base 接口不再产生非平凡 quotient 项。

5. **仍需 whole-tree 拓扑与能量公式。**  
   引理本身没有给出每棵带标记树的 \(8\pi^2q\) 代价，也没有给出 orbifold compactness、energy identity、stationarity 的极限传递、塌缩区域的拓扑承载或标记相对类的分解。它精确移除了“残余局部 CH orbifold base”这一几何可能性，并把剩余问题收束为外接口为 \(S^3\) 的完整 rooted filling。
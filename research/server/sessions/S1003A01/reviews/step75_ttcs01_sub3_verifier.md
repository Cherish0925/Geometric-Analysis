# TTCS Independent Branch Record

```json
{
  "step_id": 75,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Sessions/S1003A01/workspace/notes/spirit_step74_attainment_and_root_lattice.md",
    "Knowledge/objects/papers/Torus-Actions-on-Alexandrov-4-Spaces--16a56ecf5468--b4037224a666/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Skills/geometric-analysis/research/sources/mathematics/current/round13_chamber.md"
  ]
}
```

## Task

Critically review the load-bearing topology and supply hypotheses of Theorem 74.A. Check whether the T^2/Orlik-Raymond reasoning as written really yields a diffeomorphism (not merely homeomorphism) between the oriented two-Eguchi-Hanson resolution of S^4/Z2 and CPbar^2#CPbar^2; if the argument needs explicit orbit weights or a smooth-classification statement, say exactly what remains and whether a Kirby/lattice shortcut is valid. Also check the metricwise scalar bound S>=32pi^2 A on X#k CPbar^2 for b+=1 from LeBrun's polarized argument, and whether any fake-projective-plane exception remains. Conclude the precise theorem scope that is presently supported.

## Output

# 科学核验备忘录：Theorem 74.A 的光滑拓扑输入与 \(b^+=1\) 曲率供给

## 结论摘要

1. **两端 Eguchi–Hanson 解消的现有论证严格得到**
   \[
   \pi_1(N)=0,\qquad Q_N\cong-I_2,\qquad
   N\ \text{定向同胚于}\ 
   \overline{\mathbb{CP}}^{\,2}\#\overline{\mathbb{CP}}^{\,2}.
   \]
   但所给 `Torus Actions on Alexandrov 4-Spaces` 文献中的 Theorems 2.9–2.10 使用的是“equivariantly homeomorphic”。因此，Step 74 目前写出的 Orlik–Raymond 引用**尚未在文字层面给出定向微分同胚**。

2. 这个光滑识别可以由经典 Orlik–Raymond 的**光滑 \(T^2\)-作用分类定理**补足。需要引用的内容必须明确说：闭、单连通、光滑、带有效光滑 \(T^2\)-作用的定向四维流形，在光滑等变意义下分解为标准块的等变连通和。仅引用当前注册文献中的同胚版本并不够。

3. 若改用完整的加权轨道空间分类，必须记录南北两端不同的定向数据。有效环面的格为
   \[
   \Lambda=\mathbb Z^2+\frac12(1,1)\mathbb Z,
   \]
   四条循环轨道弧的本原向量可取
   \[
   e_1,\quad \frac{e_1+e_2}{2},\quad e_2,\quad
   \frac{e_1-e_2}{2}.
   \]
   南端出现反对角向量，是因为 \(S^4\) 的诱导定向在南极与 \(w=(w_1,w_2)\) 的标准复定向相反；定向匹配的复坐标可取 \((w_1,\bar w_2)\)。若两端都机械地插入 \((e_1+e_2)/2\)，会得到另一组光滑特征数据，不能表达两个定向匹配的 \((-2)\)-球。

4. **交叉形式或 Freedman 理论本身不能把同胚提升为微分同胚。** Donaldson 对定交叉形式的对角化也不完成这一提升。一个真正的 Kirby 证明当然可行，但必须给出 \(\mathbb{RP}^3\) 两端之间的实际粘合映射和完整的把手滑动；仅写 \(Q_N=-I_2\) 不是 Kirby 证明。

5. LeBrun 的极化论证确实给出所有
   \[
   M_k=X\#k\overline{\mathbb{CP}}^{\,2}
   \]
   上逐度量成立的
   \[
   \int_{M_k}s_g^2\,d\mu_g\ge32\pi^2A,
   \qquad A=c_1^2(X),
   \]
   **包括 \(b^+(X)=1\)**。这里使用的是随极化 \(H_g\) 选择的 spin-\(c\) 结构，而不是一个对所有度量固定不变的全局 monopole class。

6. 对紧复双曲曲面，\(b^+=1\) 恰好导出 \(p_g=q=0\) 和 \(A=9\)，即 fake projective plane 情形。LeBrun 的极化、分腔和吹起公式同样适用，因此**没有遗留的 fake-projective-plane 例外**。

---

## 1. 两端解消的纯拓扑计算

记
\[
O=S^4/\langle w\mapsto-w\rangle ,
\]
并从两个奇点各去掉一个锥邻域。中间部分为
\[
C\cong \mathbb{RP}^3\times[0,1].
\]
每个截断的 Eguchi–Hanson 填充在光滑拓扑上是复线丛
\[
E=\mathcal O_{\mathbb{CP}^1}(-2)
\]
的圆盘丛，其三维端面为 \(L(2,1)=\mathbb{RP}^3\)。解消后的闭流形可写为
\[
N=E_+\cup C\cup E_-.
\]

### 基本群

\[
\pi_1(C)=\mathbb Z/2,\qquad \pi_1(E_\pm)=0.
\]
两个 \(\mathbb{RP}^3\) 到 \(C\) 的包含在基本群上都是同构，而到 \(E_\pm\) 后生成元被消去。Van Kampen 因而给出
\[
\pi_1(N)=0.
\]

仅写“\(\pi_1(\mathcal O(-2))=1\)”还不完整；中间部分的 \(\mathbb Z/2\) 以及端面包含映射需要如上说明。

### 二阶同调与指数二子格

Mayer–Vietoris 给出
\[
0\longrightarrow
\mathbb Z\langle C_+\rangle\oplus\mathbb Z\langle C_-\rangle
\longrightarrow H_2(N;\mathbb Z)
\longrightarrow
\ker\!\left[(\mathbb Z/2)^2\longrightarrow\mathbb Z/2\right]
\longrightarrow0.
\]
最后的映射由两个端面到 \(\mathbb{RP}^3\times I\) 的包含给出，其核为 \(\mathbb Z/2\)。因此两个异常球生成 \(H_2(N)\) 中指数二的子格。

在定向匹配的复定向下，
\[
C_+^2=C_-^2=-2,\qquad C_+\cdot C_-=0.
\]
于是这个指数二子格的矩阵是
\[
\begin{pmatrix}-2&0\\0&-2\end{pmatrix}.
\]
因为 \(N\) 单连通且闭，\(H_2(N;\mathbb Z)\) 无挠并带幺模交叉形式。它秩为二，而上面的有限指数子格已经显示整个实交叉形式为负定，故
\[
Q_N\cong-I_2.
\]
Freedman 理论由此给出
\[
N\approx_{\rm homeo}
\overline{\mathbb{CP}}^{\,2}\#
\overline{\mathbb{CP}}^{\,2}
\]
作为定向同胚。

这部分计算是完整的，但终点是同胚。

---

## 2. \(T^2\) 数据中缺少的定向信息

原 \(T^2\) 在商空间上的核为
\[
K=\{(1,1),(-1,-1)\}.
\]
故有效环面 \(T'=T^2/K\) 的一参数子群格为
\[
\Lambda=\mathbb Z^2+\frac12(1,1)\mathbb Z.
\]
设原两条坐标圆的向量为 \(e_1,e_2\)。

北极附近，\(S^4\) 的定向与 \(w=(w_1,w_2)\) 的复定向一致。\(A_1\) 锥的两个射线是 \(e_1,e_2\)，最小解消插入
\[
v_+=\frac{e_1+e_2}{2}.
\]

南极附近，\(w\) 的标准复定向与 \(S^4\) 的诱导定向相反。为使 Eguchi–Hanson 的复定向与全局定向一致，可使用
\[
(w_1,\bar w_2),
\]
其环面权为 \(e_1,-e_2\)。此处应插入
\[
v_-=\frac{e_1-e_2}{2}.
\]

因此循环向量为
\[
e_1,\quad v_+,\quad e_2,\quad v_-.
\]
取格基
\[
p=e_1,\qquad q=v_+,
\]
则该序列成为
\[
(1,0),\quad(0,1),\quad(-1,2),\quad(1,-1).
\]
相邻行列式的绝对值都为 \(1\)，所以解消后的作用在四个角点处是光滑局部标准作用。北端满足
\[
e_1+e_2=2v_+,
\]
南端在定向匹配的局部复格中也给出自交数 \(-2\)。这与前述两个不交 \((-2)\)-球一致。

这些向量提供了使用加权轨道空间分类所需的具体输入。它们也说明 Step 74 中“两个复定向 EH 填充”需要区分南北局部复坐标；仅说 EH 是 \(U(2)\)-不变还没有记录这一点。

---

## 3. Orlik–Raymond 路线目前到达哪一步

所给现代文献在引言中说经典 Orlik–Raymond 理论把连续作用平滑化，但其 Theorems 2.9–2.10 的明确表述是：

- 按加权轨道空间进行 **equivariant homeomorphism** 分类；
- 单连通情形等变同胚于标准四维流形的等变连通和。

这不自动产生现有两个光滑流形之间的微分同胚。一个作用可等变同胚于某个光滑模型，并不等于所给等变同胚已经是光滑映射。

完成光滑识别有两种独立方式：

### 方式 A：经典光滑 \(T^2\)-分类

需要一个明确的经典定理，其结论是：闭、单连通、光滑、定向、带有效光滑 \(T^2\)-作用的四维流形，在**等变微分同胚**意义下是标准块的等变连通和。对本例：

- \(N\) 单连通；
- 解消作用是有效光滑 \(T^2\)-作用；
- 轨道空间为四条轨道弧围成的圆盘；
- 不存在额外有限稳定子轨道；
- \(Q_N=-I_2\)。

于是标准块分解只能给出
\[
N\cong_{\rm diff}^{+}
\overline{\mathbb{CP}}^{\,2}\#
\overline{\mathbb{CP}}^{\,2}.
\]

在引用这样一个光滑版本后，交叉形式足以从标准块列表中选出正确流形；此时不必再逐项比较轨道权。

### 方式 B：完整的加权光滑分类

若使用“加权轨道空间决定等变光滑类型”的版本，则前一节的四个向量必须写入，并与
\(\overline{\mathbb{CP}}^{\,2}\#\overline{\mathbb{CP}}^{\,2}\)
上的标准作用比较。这里需要的结论仍必须是等变微分同胚，而不能只是等变同胚。

### Kirby 与格的区别

由
\[
\pi_1(N)=0,\qquad Q_N=-I_2
\]
直接推导微分同胚是无效的。Freedman 给出同胚，Donaldson 给出定交叉形式的对角化；二者都不识别光滑结构。两个 \((-2)\)-球的同调类也不会自动产生两个可吹下的嵌入 \((-1)\)-球。

Kirby 方法可以独立完成任务，但必须包含：

- 两个 \(\mathcal O(-2)\) 圆盘丛之间通过 \(\mathbb{RP}^3\times I\) 的实际粘合；
- 该粘合在 Kirby 图中的表示；
- 把手滑动、消去以及最终标准图。

现有文本没有这些图或滑动，所以“Kirby/lattice shortcut”中的 lattice 部分只到同胚，Kirby 部分尚未实际出现。

---

## 4. \(b^+=1\) 时的逐度量标量曲率下界

令
\[
M_k=X\#k\overline{\mathbb{CP}}^{\,2},\qquad c^2=A,
\]
其中 \(c\) 可取 \(X\) 的实典范基本类，符号不影响平方。对任意光滑度量 \(g\)，令
\[
H=H_g^+\subset H^2(M_k;\mathbb R)
\]
为其自对偶极化。

按照 LeBrun `Ricci curvature, minimal volumes, and Seiberg-Witten theory` 中 Definition 1 与 Proposition 3.2 的证明，以及 `round13_chamber.md` §§2a–3：

1. 逐一选择异常类 \(E_i\) 的符号，使
   \[
   c_H^+\cdot E_i\le0.
   \]

2. 吹起公式给出一个在该极化相容小扰动腔中非零的 spin-\(c\) 结构，其实 Chern 类为
   \[
   a_H=c-\sum_{i=1}^kE_i.
   \]

3. 它是 \((M_k,H)\) 的 polarized monopole：未扰动 Seiberg–Witten 方程对所有 \(H\)-adapted 度量可解。特别地，它适用于 \(g\) 及其整个共形类。

4. 自对偶投影满足
   \[
   \begin{aligned}
   (a_H^+)^2
   &=
   \left(c_H^+-\sum_iE_{i,H}^+\right)^2\\
   &=
   (c_H^+)^2
   -2\sum_i c_H^+\cdot E_i
   +\left(\sum_iE_{i,H}^+\right)^2\\
   &\ge(c_H^+)^2\ge c^2=A.
   \end{aligned}
   \]

5. LeBrun 的 Weitzenböck 估计给出
   \[
   \int_{M_k}s_g^2\,d\mu_g
   \ge32\pi^2(a_H^+)^2
   \ge32\pi^2A.
   \]

这一推导允许 \(a_H\) 随 \(H\)、因而随测试度量改变。Theorem 74.A 的解消序列中每个 \(g_\varepsilon\) 可分别选择自己的 \(a_{H_\varepsilon}\)；不需要这些类收敛，也不需要一个固定类同时服务于全部度量。

因此 Step 74 的 “Supply hypothesis (SW)” 最精确的表述不是“存在一个固定的全度量 monopole class”，而是：

> 对每个度量 \(g\)，存在一个相对于 \(H_g\) 的 polarized monopole \(a_g\)，满足 \((a_g^+)^2\ge A\)。

这已经足以推出标量曲率估计，也足以把 LeBrun 的混合 \(s\)–\(W^+\) 不等式逐度量用于粘合度量。

---

## 5. fake projective plane 情形

对复双曲曲面，
\[
c_1^2(X)=A,\qquad c_2(X)=\frac A3,\qquad
\chi(\mathcal O_X)=\frac{c_1^2+c_2}{12}=\frac A9.
\]
同时
\[
b^+(X)=1+2p_g.
\]
若 \(b^+=1\)，则 \(p_g=0\)，于是
\[
\frac A9=\chi(\mathcal O_X)=1-q.
\]
因为 \(A>0\) 且 \(q\ge0\)，必有
\[
q=0,\qquad A=9.
\]
这正是 fake projective plane 的数值情形。

这里 \(c^2=A>0\)，所以对任意极化 \(H\)，
\[
c_H^+\ne0;
\]
否则 \(c\) 完全反自对偶，会推出 \(c^2\le0\)。因此基底典范类在小扰动腔中的极化延拓不会穿过 \(c_H^+=0\) 的墙。吹起后的符号选择由上述公式逐极化完成。

所以“\(b^+=1\) 的腔问题只出现在 fake projective plane”只能理解为：这是复双曲族中唯一需要显式使用极化版本的子族；它并不是尚未覆盖的子族。

---

## 6. 当前材料支持的精确定理表述

令 \(X\) 为任意紧复双曲曲面，包括 fake projective planes，令
\[
V_m=X\#m(S^4/\mathbb Z_2),\qquad k=2m.
\]

### 已完整支持的曲率供给

对标准光滑吹起
\[
M_k=X\#k\overline{\mathbb{CP}}^{\,2}
\]
及其任意光滑度量，
\[
\int s^2\ge32\pi^2A,
\]
并且相应的 LeBrun 混合不等式也可逐度量使用。这里无需额外排除 \(b^+=1\)。

### 仍依赖光滑识别的部分

Theorem 74.A 从解消度量 \(g_\varepsilon\) 调用上述估计时，需要
\[
\operatorname{Res}(V_m)
\cong_{\rm diff}^{+}
M_{2m}.
\]
当前写出的拓扑计算和已注册的现代 \(T^2\) 文献只直接给出
\[
\operatorname{Res}(V_m)
\approx_{\rm homeo}^{+}
M_{2m}.
\]
因而，以现有文件为依据，Theorem 74.A 的下界、所有 \(m\) 的 Einstein 排除、\(\inf P\) 和 \(\alpha_{\rm orb}\) 的精确值，应读作以该定向光滑识别为输入的定理。

一旦加入经典 Orlik–Raymond 光滑分类的准确出处，或加入完成的 Kirby 计算，局部块即满足
\[
N\cong_{\rm diff}^{+}
\overline{\mathbb{CP}}^{\,2}\#
\overline{\mathbb{CP}}^{\,2},
\]
从而 Theorem 74.A 适用于：

\[
\boxed{\text{所有紧复双曲曲面 }X,\ \text{所有 }m\ge1,\ \text{包括所有 fake projective planes}.}
\]

真正尚缺的是一个光滑拓扑引用或等价的把手证明，而不是 Seiberg–Witten 标量曲率供给。
# TTCS Independent Branch Record

```json
{
  "step_id": 1,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/briefing/aligned_research_goal.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

Independently check the dossier's central reduction Q_n iff P_n^+ or P_n^- and search for hidden quantifier, scaling, sign, or vacuity issues. Then critically assess what low-dimensional cases are already settled and what a full refutation actually requires. Check especially whether arbitrary intervals can be vacuous, how homothetic rescaling acts on Ricci as a (0,2)-tensor and on the Ricci endomorphism, and whether n=2,3 yield complete positive results under the stated smooth closed connected conventions.

## Output

# 科学核验备忘

## 1. \(Q_n\Longleftrightarrow P_n^+\vee P_n^-\) 的推导成立

记 \(E(M)\) 为“\(M\) 承载某个 Einstein 度量”。工作命题是

\[
Q_n:\quad \exists a<b\;\forall M^n\;\forall g,\qquad
ag\leq \operatorname{Ric}_g\leq bg\Longrightarrow E(M).
\]

由于 \(E(M)\) 与输入度量 \(g\) 无关，对每个固定 \(M\) 有逻辑等价

\[
\forall g\,[B(M,g)\Rightarrow E(M)]
\iff
[(\exists g\,B(M,g))\Rightarrow E(M)].
\]

因此，把题文理解成“任意满足夹逼的输入度量”或“流形上存在一个满足夹逼的输入度量”，在此结论形式下没有量词差异。

### 1.1 常数倍缩放

若 \(\widetilde g=cg\)，其中 \(c>0\) 为常数，则 Christoffel 符号不变，因而

\[
\nabla^{\widetilde g}=\nabla^g,\qquad
\operatorname{Ric}_{\widetilde g}=\operatorname{Ric}_g
\]

成立于 \((0,2)\)-张量层面。Ricci 端同态则满足

\[
A_{\widetilde g}
=\widetilde g^{-1}\operatorname{Ric}_{\widetilde g}
=c^{-1}A_g.
\]

相应地，

\[
ag\leq\operatorname{Ric}_g\leq bg
\iff
\frac ac\,\widetilde g
\leq\operatorname{Ric}_{\widetilde g}
\leq\frac bc\,\widetilde g.
\]

若 \(\operatorname{Ric}_g=\lambda g\)，则

\[
\operatorname{Ric}_{cg}=\frac{\lambda}{c}(cg).
\]

所以 Einstein 常数除以 \(c\)，符号不变。

对固定端同态 \(T\)，有
\(\|T\|_{\mathrm{op},cg}=\|T\|_{\mathrm{op},g}\)，但由于 \(A_{cg}=c^{-1}A_g\)，

\[
\delta_\sigma(cg)
=\sup_M\|c^{-1}A_g-\sigma I\|_{\mathrm{op},g},
\]

一般并不等于 \(c^{-1}\delta_\sigma(g)\)。底稿的分支推导使用特征值区间，没有犯这一常见缩放错误。

### 1.2 从 \(P_n^\sigma\) 到 \(Q_n\)

若某个 \(\varepsilon\in(0,1)\) 满足 \(P_n^\sigma\)，自伴随端同态的谱刻画给出

\[
\delta_\sigma(g)\leq\varepsilon
\iff
(\sigma-\varepsilon)g\leq\operatorname{Ric}_g
\leq(\sigma+\varepsilon)g.
\]

取

\[
a=\sigma-\varepsilon,\qquad b=\sigma+\varepsilon
\]

即可。特别是负分支正确写成

\[
(-1-\varepsilon)g
\leq\operatorname{Ric}_g
\leq(-1+\varepsilon)g.
\]

### 1.3 从 \(Q_n\) 到一个符号分支

任意非退化实区间 \([a,b]\) 都含有同号非退化闭子区间

\[
[u,v]\subset[a,b],\qquad uv>0.
\]

令

\[
\mu=\frac{u+v}{2},\qquad
\sigma=\operatorname{sign}\mu,\qquad
\varepsilon=\frac{v-u}{|u+v|}.
\]

当 \(0<u<v\) 或 \(u<v<0\) 时，都有 \(0<\varepsilon<1\)。并且

\[
|\mu|(\sigma-\varepsilon)=u,\qquad
|\mu|(\sigma+\varepsilon)=v.
\]

若 \(\delta_\sigma(h)\leq\varepsilon\)，置

\[
g=\frac{h}{|\mu|}.
\]

由 \(\operatorname{Ric}_g=\operatorname{Ric}_h\) 以及 \(h=|\mu|g\)，得到

\[
ug\leq\operatorname{Ric}_g\leq vg,
\]

从而也满足原来的 \([a,b]\) 夹逼。应用 \(Q_n\) 即得 \(E(M)\)。因此

\[
Q_n\iff P_n^+\vee P_n^-.
\]

符号可以随维数改变；整体命题是

\[
\forall n\geq2\;(P_n^+\vee P_n^-),
\]

而不是要求同一个符号对所有维数成立。

---

## 2. 区间不会在所有输入上形成空前提

对每个固定 \(n\geq2\) 和每个 \(a<b\)，可取非零 \(t\in(a,b)\)。

* 若 \(t>0\)，将圆球度量缩放，使
  \[
  \operatorname{Ric}_g=tg.
  \]
* 若 \(t<0\)，利用闭实双曲 \(n\)-流形并缩放，同样可得
  \[
  \operatorname{Ric}_g=tg.
  \]
* 若区间包含 \(0\)，平坦环面还给出 \(A_g=0\)。

因此任意非退化区间在固定维数中至少有一个闭光滑输入实例，不能通过选择一个“完全无人满足”的区间使 \(Q_n\) 自动成立。

不过，对某个特定流形 \(M\)，可能没有任何度量满足所选区间；此时该 \(M\) 对应的蕴含式确实自动为真。这正是 \(Q_n\) 的数学内容：只有承载夹逼输入的流形才须承载 Einstein 度量。

另一个符号细节是：

* 当 \(a<0<b\) 时，任取闭流形上的度量 \(g\)，充分放大 \(cg\) 后，\(A_{cg}=c^{-1}A_g\) 的全部特征值都进入 \([a,b]\)。
* 当 \(0\) 只是端点时，这个论证不成立，因为缩放使特征值趋近零，却不会改变其符号。

命题 \(Q_n\iff P_n^+\vee P_n^-\) 不依赖端点情形的直接缩放；它通过区间内部的同号子区间处理 \([0,b]\)、\([a,0]\) 和跨零区间。

底稿中的间隙量

\[
\Gamma_n^\sigma=
\inf_{\mathcal E(M)=\varnothing}\inf_g\delta_\sigma(g)
\]

也确实满足

\[
P_n^\sigma\iff\Gamma_n^\sigma>0.
\]

若 \(P_n^\sigma\) 对阈值 \(\varepsilon\) 成立，则所有无 Einstein 度量的流形均有 \(\delta_\sigma(g)>\varepsilon\)，所以 \(\Gamma_n^\sigma\geq\varepsilon\)。反向取小于 \(\Gamma_n^\sigma\) 的正数即可。

---

## 3. 低维情形在当前约定下已经得到完整正结果

### 3.1 二维

每个闭、连通、光滑曲面都承载常高斯曲率度量：

* \(S^2,\mathbb{RP}^2\)：正曲率；
* \(T^2\) 和 Klein 瓶：平坦；
* 其余闭曲面：负曲率。

非定向曲面也包含在上述均匀化结论中。在二维，

\[
\operatorname{Ric}_h=K_hh,
\]

所以常高斯曲率正是这里定义的 Einstein 条件。于是每个这样的 \(M^2\) 都有 \(\mathcal E(M)\neq\varnothing\)，输入 \(g\) 完全无关。因此：

\[
P_2^+\ \text{和}\ P_2^-
\]

对任意 \(\varepsilon\in(0,1)\) 都成立，\(Q_2\) 甚至可由任意 \(a<b\) 见证。例如可明确取

\[
c_2=-1,\qquad C_2=1.
\]

### 3.2 三维正分支

若

\[
\delta_+(g)\leq\varepsilon<1,
\]

则

\[
\operatorname{Ric}_g\geq(1-\varepsilon)g>0.
\]

Hamilton 1982 年定理表明，闭三维流形承载正 Ricci 度量时，归一化 Ricci 流产生常正截面曲率度量。因此 \(P_3^+\) 对每个 \(\varepsilon\in(0,1)\) 都成立。一个显式的 \(Q_3\) 见证是

\[
c_3=\frac12,\qquad C_3=\frac32.
\]

只此正分支已经完整解决三维原命题。

### 3.3 三维负分支

设 Ricci 端同态在正交特征标架中的特征值为 \(r_1,r_2,r_3\)。三维曲率张量由 Ricci 张量决定，且

\[
K_{ij}=\frac{r_i+r_j-r_k}{2},
\qquad\{i,j,k\}=\{1,2,3\}.
\]

若

\[
r_i\in[-1-\varepsilon,-1+\varepsilon],
\]

则

\[
K_{ij}
\leq\frac{2(-1+\varepsilon)-(-1-\varepsilon)}2
=\frac{-1+3\varepsilon}{2}.
\]

故 \(\varepsilon<1/3\) 时所有截面曲率严格为负。

从这里到双曲度量还需要三维拓扑：严格负截面曲率给出非球面性、不可约性及无 \(\mathbb Z^2\) 子群等性质；结合三维几何化并排除 Seifert 情形，可知 \(M\) 承载双曲度量。非定向情形需要引用相应形式的几何化，或在定向双覆盖上作等变论证。三维光滑结构唯一性保证所得双曲度量位于同一光滑流形上。

因此

\[
P_3^-
\]

至少对任意 \(\varepsilon<1/3\) 也成立。底稿中的截面曲率计算正确，但从负截面曲率到同一光滑流形上的双曲度量这一段应写出上述拓扑链条；它不影响 \(Q_3\)，因为 Hamilton 的正分支已经足够。

---

## 4. 完整否定所需的精确量词

由于 \(Q_2,Q_3\) 已成立，整体命题若不成立，相关维数必为某个固定的 \(n\geq4\)。必须同时有

\[
\forall\varepsilon\in(0,1)\ \exists M_\varepsilon^+,g_\varepsilon^+:
\quad
\delta_+(g_\varepsilon^+)\leq\varepsilon,\qquad
\mathcal E(M_\varepsilon^+)=\varnothing,
\]

以及

\[
\forall\varepsilon\in(0,1)\ \exists M_\varepsilon^-,g_\varepsilon^-:
\quad
\delta_-(g_\varepsilon^-)\leq\varepsilon,\qquad
\mathcal E(M_\varepsilon^-)=\varnothing.
\]

两族流形可以不同，也可随 \(\varepsilon\) 改变，但维数必须相同。等价地，可构造两列

\[
\delta_\pm(g_j^\pm)\longrightarrow0,\qquad
\mathcal E(M_j^\pm)=\varnothing.
\]

其中 \(\mathcal E(M)=\varnothing\) 必须排除所有光滑度量及所有 \(\lambda\in\mathbb R\)，而不只是：

* 与输入度量邻近的 Einstein 解；
* 与输入 Ricci 符号相同的 Einstein 解；
* 具有指定对称性、复结构或某个 ansatz 的解；
* 某一个固定小误差下的解。

为什么两支足以直接处理任意 \([a,b]\)：在其中选取同号子区间 \([u,v]\)，令

\[
\varepsilon_0=\frac{v-u}{|u+v|}.
\]

使用相应符号的无 Einstein 实例 \(h\)，再置 \(g=h/|\mu|\)，便得到

\[
ug\leq\operatorname{Ric}_g\leq vg
\]

且 \(\mathcal E(M)=\varnothing\)。于是原来的 \([a,b]\) 也不能充当 \(Q_n\) 的常数对。

特别地，在维数 \(n_1\) 只构造正分支序列、在另一维数 \(n_2\) 只构造负分支序列，并不能否定整体命题；两支必须汇聚在同一个固定维数。

## 总结

底稿的核心归约、缩放方向、负分支符号和量词结构均正确。任意非退化区间在固定维数中都有实际输入实例，所以不存在全局空前提。二维由曲面均匀化完全解决；三维由 Hamilton 的正 Ricci 定理完全解决，负分支在 \(\varepsilon<1/3\) 时也可经截面曲率计算与几何化得到。整体命题的完整否定必须发生在某个固定 \(n\geq4\)，并在该维数中同时给出趋近 \(+I\) 与趋近 \(-I\) 的两族无任何 Einstein 度量的流形。
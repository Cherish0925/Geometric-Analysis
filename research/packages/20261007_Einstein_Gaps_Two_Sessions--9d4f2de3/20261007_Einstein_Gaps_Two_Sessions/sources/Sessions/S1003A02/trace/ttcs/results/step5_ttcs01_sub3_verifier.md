# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step4_O10_localization_and_orbifold_test.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md",
    "Skills/geometric-analysis/research/paper/sections/variational_geometry.tex",
    "Skills/geometric-analysis/references/conventions-and-literature.md"
  ]
}
```

## Task

Check the proposed h=0 Einstein-gap theorem for minimal Kähler surfaces of general type: alpha=inf E should be zero by orbifold/ALE approximation; alpha is attained exactly when the underlying smooth four-manifold admits some Einstein metric, not necessarily Kähler; if K is ample Aubin-Yau supplies a negative Kähler-Einstein metric, while if K is nef nonample Kähler-Einstein attainment is impossible but non-Kähler Einstein existence may remain. Read the Step 4 Y-test and the actual Ozuch higher-order source. Determine precisely what Ozuch's first and second compact obstructions say for A1/Eguchi-Hanson resolution of a negative Kähler-Einstein orbifold. In particular, check whether the rank-one Kähler-Einstein curvature block automatically satisfies not just det R+=0 but also Ozuch's stronger second obstruction, and hence whether that source excludes or leaves open nearby non-Kähler Einstein metrics. Give a theorem with exact hypotheses and a corrected status of the unresolved part.

## Output

## 科学核验备忘录

### 一、\(h=0\) 情形的零下确界与达到问题

#### 定理 1（极小一般型 Kähler 曲面的 Einstein 泛函）

设 \((X,J)\) 是紧致极小一般型 Kähler 曲面，\(M\) 为其底层定向光滑四维流形，并令  
\[
\mathcal E(g)=\inf_{\lambda\neq0}
 \frac{\int_M|\Ric_g-\lambda g|^2\,d\mu_g}
      {\lambda^2\Vol(g)},\qquad
\alpha(M)=\inf_g\mathcal E(g).
\]
则：

1. **零下确界**
   \[
   \alpha(M)=0.
   \]

2. **达到的精确含义**  
   \(\alpha(M)\) 由某个光滑度量达到，当且仅当 \(M\) 上存在
   \[
   \Ric_g=\lambda g,\qquad \lambda\neq0.
   \]
   极小一般型曲面的标准 Seiberg–Witten/Yamabe 结果排除非负常标量曲率 Einstein 度量，因此这里也可等价表述为：底层光滑流形承载某个 \(\lambda<0\) 的 Einstein 度量。

3. **\(K_X\) ample**  
   Aubin–Yau 定理给出与 \(J\) 相容的 \(\lambda<0\) Kähler–Einstein 度量，所以 \(\alpha(M)=0\) 被达到。

4. **\(K_X\) nef 但非 ample**  
   不存在与原复结构 \(J\) 相容的 Kähler–Einstein 度量；但这并不排除底层光滑流形承载不与 \(J\) 相容的 Einstein 度量。因此此时 \(\alpha(M)=0\) 已确定，而是否达到仍等价于一个光滑 Einstein 存在问题。

#### 证明要点

一般型曲面的典范模型
\[
\pi:X\longrightarrow X_{\rm can}
\]
收缩所有 \((-2)\)-曲线。\(X_{\rm can}\) 只有 ADE 型 Du Val 奇点，\(K_{X_{\rm can}}\) ample，并承载一个 orbifold Kähler–Einstein 度量 \(g_0\)，可归一化为
\[
\Ric(g_0)=-g_0.
\]

在每个奇点处插入相应的 Kronheimer Ricci-flat hyperkähler ALE 度量。局部覆盖坐标中
\[
g_0=e+O(r^2),\qquad
g_{{\rm ALE},\varepsilon}=e+O(\varepsilon^4r^{-4}).
\]
例如在 \(r\asymp\varepsilon^{1/2}\) 上截断时，过渡区曲率保持有界，而其体积为 \(O(\varepsilon^2)\)；ALE 插入区的体积同样趋于零。外部区域满足 \(\Ric+g=0\)，ALE 区满足 \(\Ric=0\)，故
\[
\Vol(g_\varepsilon)\longrightarrow\Vol(g_0)>0,\qquad
\int_X|\Ric(g_\varepsilon)+g_\varepsilon|^2\,d\mu_{g_\varepsilon}
 \longrightarrow0.
\]
取 \(\lambda=-1\) 即得
\[
0\leq \mathcal E(g_\varepsilon)
 \leq\frac1{\Vol(g_\varepsilon)}
 \int_X|\Ric(g_\varepsilon)+g_\varepsilon|^2\,d\mu_{g_\varepsilon}
 \longrightarrow0.
\]

另一方面，`variational_geometry.tex` 的式
\[
\mathcal E(g)=4-\frac{I^2}{VR}
=\frac{4P+L_s}{R}
\]
表明，当 \(R>0\) 时，
\[
\mathcal E(g)=0
\iff P=0,\quad L_s=0
\iff \Ric_g^\circ=0,\quad s_g\ \text{为非零常数}.
\]
这正是 \(\Ric_g=\lambda g\)、\(\lambda\neq0\)。Ricci-flat 度量的 \(\mathcal E\) 等于 \(4\)，不是零。

若 \(g\) 与 \(J\) 相容且 Kähler–Einstein，则
\[
[\rho_g]=2\pi c_1(X)=-2\pi c_1(K_X),\qquad \rho_g=\lambda\omega_g.
\]
当 \(\lambda<0\) 时，
\[
c_1(K_X)=\frac{-\lambda}{2\pi}[\omega_g]
\]
是 Kähler 类，因此 \(K_X\) ample。故 \(K_X\) nef 非 ample 时，原复结构下的 Kähler–Einstein 度量不存在。

---

### 二、Ozuch 在 \(A_1\)/Eguchi–Hanson 解消中的两个局部 obstruction

以下是 `Higher order obstructions to the desingularization of Einstein metrics` 中实际得到的结论。

设 \((X_0,g_0)\) 是紧致 Einstein 四维 orbifold，
\[
\Ric(g_0)=\Lambda g_0,
\]
所有奇点均为 \(\mathbb R^4/\mathbb Z_2\)，且 \(g_0\) 的无穷小 Einstein 变形可积。设光滑流形 \(M\) 由在这些奇点插入 Eguchi–Hanson 空间得到，并假设存在光滑 Einstein 度量序列在 Gromov–Hausdorff 意义下趋于 \((X_0,g_0)\)。

记 \(\sigma=+\) 或 \(-\) 为该 EH 插入所对应的手性，\(\phi\in\Lambda^\sigma_p\) 为归一化的 EH gluing/period 向量。

#### 1. 第一阶条件：必须有一个零曲率方向

Ozuch §2.1.1 中的系数为
\[
\lambda_k
 =c\,\big\langle \mathbf R^\sigma_{g_0}(p)\phi,\phi_k\big\rangle,
 \qquad c>0,
\]
其中 \((\phi,\phi_2,\phi_3)\) 是 \(\Lambda^\sigma_p\) 的正交基。所有 \(\lambda_k\) 消失等价于
\[
\boxed{\mathbf R^\sigma_{g_0}(p)\phi=0.}
\]
因而方向无关的较弱写法是
\[
\boxed{\det\mathbf R^\sigma_{g_0}(p)=0.}
\]

这里必须区分两个表述：行列式为零只说明存在可用的核方向；对一个已经指定的 EH gluing 向量，真正的方程是
\(\mathbf R^\sigma\phi=0\)。

#### 2. 第二阶紧致条件：核至少为二维

在第一阶系数消失后，取基使 \(\phi=e_1\)，则
\[
\mathbf R^\sigma_{g_0}(p)=
\begin{pmatrix}
0&0&0\\
0&R_{22}&R_{23}\\
0&R_{23}&R_{33}
\end{pmatrix}.
\]
Ozuch §2.1.4 给出的下一系数满足
\[
\mu_1
 =C\det
 \begin{pmatrix}
 R_{22}&R_{23}\\
 R_{23}&R_{33}
 \end{pmatrix},
 \qquad C>0.
\]
因此 \(\mu_1=0\) 意味着该 \(2\times2\) 块还有一个零特征值。又因为
\[
\operatorname{tr}\mathbf R^\sigma
 =\operatorname{tr}\!\left(W^\sigma+\frac{s}{12}I\right)
 =\frac s4=\Lambda,
\]
所以最终形式为
\[
\boxed{\mathbf R^\sigma_{g_0}(p)
       =\operatorname{diag}(0,0,\Lambda)}
\]
（允许置换基向量）。

这就是论文 Theorem 0.2 和 Proposition 0.4 中的较强结论。

#### 3. 较强结论所需的附加前提

在上述可积性及 \(A_1\) 设置下，论文在以下任一情形得到
\(\operatorname{diag}(0,0,\Lambda)\)：

- Einstein 解消序列是 transverse；
- \(\Lambda=0\)，且序列是 nondegenerate；
- orbifold 只有一个奇点，且序列是 nondegenerate；
- 存在趋于该 orbifold 的 stable Ricci-flat 序列；
- orbifold 只有一个奇点且 Einstein-rigid。

论文中的尺度定义是：若 \(t_{\min},t_{\max}\) 是 EH 尺度而 \(v_n\) 是 orbifold Einstein 变形参数，则两种情形都要求
\[
\frac{t_{\min}}{t_{\max}}\not\longrightarrow0;
\]
transverse 还要求
\[
\frac{\|v_n\|}{t_{\min}}\longrightarrow0,
\]
nondegenerate 要求
\[
\frac{\|v_n\|^2}{t_{\min}}\longrightarrow0.
\]

对于 \(\Lambda<0\) 的 Kähler–Einstein orbifold，直接相关的是 transverse 分支，以及单奇点的 nondegenerate 或 rigid 分支；Ricci-flat 分支不适用。

---

### 三、专门代入 \(\Lambda<0\) 的 Kähler–Einstein orbifold

在复定向下，Kähler–Einstein 四维 orbifold 的自对偶 Weyl 块为
\[
W^+
 =\operatorname{diag}\left(\frac s6,-\frac s{12},-\frac s{12}\right).
\]
因此完整曲率算子在 \(\Lambda^+\) 上的块是
\[
\mathbf R^+
 =W^++\frac s{12}I
 =\operatorname{diag}\left(\frac s4,0,0\right)
 =\operatorname{diag}(\Lambda,0,0).
\]
第一特征方向是 Kähler 形式 \(\omega/\sqrt2\)，另两个方向构成 primitive self-dual 平面。于是
\[
\det\mathbf R^+=0,\qquad
\dim\ker\mathbf R^+=2.
\]

所以答案是：

\[
\boxed{\text{Kähler–Einstein 的 rank-one } \mathbf R^+
\text{ 不仅满足 }\det\mathbf R^+=0，
\text{也自动满足 Ozuch 的第二阶条件。}}
\]

更具体地，若 EH gluing 向量
\[
\phi\in\ker\mathbf R^+=\omega^\perp,
\]
则第一阶方程成立；在 \(\phi^\perp\) 上，\(\mathbf R^+\) 的特征值为
\(\Lambda\) 和 \(0\)，故
\[
\mu_1=C(\Lambda\cdot0)=0.
\]
置换基后正是 Ozuch 的
\[
\operatorname{diag}(0,0,\Lambda).
\]

相反，在 Kronheimer 的周期参数中，保持原复结构的 crepant Kähler 插入取 gluing 向量平行于 Kähler 形式：
\[
\phi\parallel\omega.
\]
此时
\[
\mathbf R^+\phi=\Lambda\phi\neq0.
\]
因此 Step 4 中“\(\det\mathbf R^+=0\)，所以 leading obstruction 已满足”需要加入方向信息：

- 对允许旋转 EH hyperkähler 参数的方向无关问题，行列式条件确实满足；
- 对保持原复结构的 Kähler ALE 恢复序列，指定的 gluing 向量不在核中，方向分辨的第一阶方程不成立；
- 核中的 gluing 向量对应旋转后的、通常不保持原复结构的候选解消。

这也解释了为什么复几何恢复序列可以使
\[
\int|\Ric+g|^2\to0
\]
却不能直接被修正成同一复结构下的精确 Kähler–Einstein 度量。

---

### 四、修正后的未解决状态

Ozuch 的高阶论文没有排除从核方向进行的非 \(J\)-Kähler Einstein 解消：

1. \(\Lambda<0\) Kähler–Einstein orbifold 的 \(\mathbf R^+\) 已具有论文要求的 rank-one 形式；
2. 因此第一阶行列式关系和第二阶 rank-one 关系都不能排除旋转后的 EH gluing；
3. 该论文给出的是必要方程，不提供 Einstein 解消的存在构造；
4. 多奇点时还可能出现 orbifold 变形、不同 bubble 尺度及全局相互作用；单奇点时仍可能有更高阶项和线性化可解性问题。

故精确结论是：

> 对 \(K_X\) nef 非 ample 的极小一般型曲面，ALE/orbifold 构造严格证明 \(\alpha(M)=0\)。与原复结构相容的 Kähler–Einstein 达到不可能。Ozuch 的第一、第二个紧致 obstruction 都不排除沿 \(\ker\mathbf R^+\) 的旋转 EH 方向出现邻近的非 \(J\)-Kähler Einstein 度量，但该文也没有构造这种度量。因此 \(\alpha(M)\) 是否达到，仍等价于底层光滑四维流形是否承载某个 \(\lambda<0\) Einstein 度量；邻近 orbifold 的非 Kähler 解消只是其中一个尚未决定的实现机制。
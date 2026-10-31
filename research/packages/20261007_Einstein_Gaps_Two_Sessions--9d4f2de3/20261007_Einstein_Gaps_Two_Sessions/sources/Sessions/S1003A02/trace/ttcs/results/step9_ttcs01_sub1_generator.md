# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md",
    "Sessions/S1003A02/workspace/scripts/o11_general_bulk_cell.py",
    "Sessions/S1003A02/workspace/notes/step6_theorems_and_O11_rotation.md"
  ]
}
```

## Task

Develop a mathematically precise proof route for the universal first-order Burns cell law suggested by the attached note and computations. Let an oriented smooth Einstein or general curved 4-manifold have curvature operator self-dual block R^+=W^++s/12 at p, and insert a small Burns O(-1) cell whose Kähler form at infinity is ζ∈Λ^+_p. The proposed expansion in the session normalization is ∫cell |Ric°|²/(8π²)=1-a² R^+(ζ,ζ)+O(a^4) (equivalently the separate first variations are -a²W^+(ζ,ζ) and -a²s/12). Give the strongest derivation you can: identify the ALE boundary term/renormalized Chern-Weil or matched-asymptotic calculation that fixes the coefficient and sign, state gauge and matching hypotheses, and distinguish what is actually proved from what still needs an explicit calculation. Explain the relation to Ozuch/Biquard desingularization obstruction R^+ζ=0 and to the Fubini–Study/complex-hyperbolic sign reversal in the provided computational result. Do not invent literature; reason from the supplied artifacts.

## Output

下面给出一个可直接转化为严格定理的证明框架。核心不是对 \(|\operatorname{Ric}^{\circ}|^{2}\) 逐项展开，而是先用 Chern–Weil 把问题化为自对偶曲率算子能量，再计算 Burns \(r^{-2}\) 尾项在无穷远球面产生的秩一曲率矩。这个计算同时确定系数与符号。

## 1. 精确的相对表述

取
\[
P(g)=\int_M|\operatorname{Ric}^{\circ}_g|^2\,d\mu_g,\qquad
I_+(g)=\int_M|R_g^+|^2\,d\mu_g,
\]
其中
\[
R^+=W^++\frac{s}{12}\operatorname{Id}_{\Lambda^+}.
\]
在本文约定下，
\[
P(g)=4I_+(g)-8\pi^2T_+(M).
\]

设 \(\widehat M=M\#\overline{\mathbf{CP}}^{\,2}\)，在 \(p\in M\) 处插入尺度 \(a\) 的 Burns 块，并记所得度量为 \(g_a\)。由于
\[
T_+(\widehat M)=T_+(M)-1,
\]
有完全精确的恒等式
\[
P(g_a)-P(g)
=
8\pi^2+4\bigl(I_+(g_a)-I_+(g)\bigr).
\tag{1}
\]
因此所需公式等价于
\[
I_+(g_a)-I_+(g)
=
-2\pi^2a^2R_p^+(\zeta,\zeta)+o(a^2).
\tag{2}
\]

对于一般背景，最自然的“cell 能量”是上述全局相对量；若背景 Einstein，则 \(P(g)=0\)，它就是插入后产生的全部 trace-free Ricci 能量。

---

## 2. Burns 尾项及其规范

在与 \(\zeta\) 对应的正交复结构 \(J_\zeta\) 下，使用会话脚本中的尺度约定
\[
K=x-a^2,\qquad x=r^2.
\]
Burns 度量写为
\[
g_{B,a}
=
\frac{r^2}{r^2-a^2}\,dr^2
+r^2(\sigma_1^2+\sigma_2^2)
+(r^2-a^2)\sigma_3^2.
\]
若 \(g_0=dr^2+r^2(\sigma_1^2+\sigma_2^2+\sigma_3^2)\)，且
\(J_\zeta dr=r\sigma_3\)，则
\[
g_{B,a}
=
g_0+a^2H_\zeta+O(a^4r^{-4}),
\]
其中
\[
H_\zeta
=
r^{-2}\Bigl(dr\otimes dr-(J_\zeta dr)\otimes(J_\zeta dr)\Bigr).
\tag{3}
\]

这里 \(a\) 已由 bolt 条件 \(K(a^2)=0\)、\(K'(a^2)=1\) 固定；若重新定义尺度，公式中的系数也随之重标定。

计算系数时使用径向 Kähler 规范。余项可置于相对于欧氏度量或拼接背景的 Bianchi 规范，并与平移、转动、尺度及微分同胚模态正交。允许的规范变换必须保持式 (3) 的 \(r^{-2}\) 系数及其球面通量；例如由 \(X=o(r^{-1})\) 产生的变换不会改变下面的曲率矩。

---

## 3. 决定常数与符号的球面通量计算

令 \(n=x/r\)，\(m=J_\zeta n\)。则
\[
(H_\zeta)_{ij}
=
r^{-2}(n_in_j-m_im_j).
\]
直接微分得到
\[
\operatorname{tr}_{g_0}H_\zeta=0,\qquad
\partial_j(H_\zeta)_{ij}=2r^{-3}n_i.
\tag{4}
\]
采用
\[
D s_{g_0}(h)=\partial_i\partial_jh_{ij}
-\Delta\operatorname{tr}h
\]
的符号约定，式 (4) 给出
\[
D s_{g_0}(H_\zeta)=0\qquad (r>0),
\]
同时
\[
\int_{S_r}
\left(\operatorname{div}H_\zeta-d\operatorname{tr}H_\zeta\right)(n)\,dA
=
2r^{-3}\operatorname{Area}(S_r^3)
=
4\pi^2.
\tag{5}
\]

换言之，若把 \(H_\zeta\) 视为 \(\mathbf R^4\) 上的奇异张量，其分布曲率源满足
\[
D s_{g_0}(H_\zeta)=4\pi^2\delta_0.
\tag{6}
\]
真实 Burns 核心是光滑的且标量曲率为零，所以当 Burns 尾项从内侧向外侧关闭时，拼接环带必须携带相反的通量：
\[
\int_{\mathrm{transition}}\delta s\,d\mu
=
-4\pi^2a^2+o(a^2).
\tag{7}
\]

现在使用四维 Kähler 曲率的秩一结构。若
\(\zeta=\omega/\sqrt2\) 是单位 Kähler 形式，则
\[
R^+
=
\frac{s}{4}\,\zeta\otimes\zeta.
\tag{8}
\]
径向关闭 Burns 尾项可在 Calabi–\(U(2)\) Kähler族内完成，所以在线性阶，
\[
D R^+_{g_0}(H_\zeta)
=
\frac14D s_{g_0}(H_\zeta)\,
\zeta\otimes\zeta.
\]
结合式 (7)，得到关键的 ALE 曲率矩：
\[
\boxed{
\int_{\mathrm{transition}}\delta R^+\,d\mu
=
-\pi^2a^2\,\zeta\otimes\zeta+o(a^2).
}
\tag{9}
\]

式 (9) 是全部系数的来源。它也可以看成 Burns 无穷远 Chern–Weil transgression 的秩一版本。符号来自一个简单事实：奇异尾项本身在原点带 \(+\pi^2\zeta\otimes\zeta\) 的分布源，而光滑 Burns 核心没有 \(R^+\)；因此外侧关闭尾项的环带必须给出相反通量。

---

## 4. 从曲率矩得到一阶定律

在 \(p\) 处取定向正交正规坐标，并用径向平行移动识别附近的 \(\Lambda^+\)。于是
\[
R_g^+(x)=R_p^++O(r).
\]
记插入产生的自对偶曲率变化为 \(K_a\)。良好匹配时，
\[
\int K_a\,d\mu
=
-\pi^2a^2\zeta\otimes\zeta+o(a^2),
\qquad
\int|K_a|^2\,d\mu=o(a^2).
\tag{10}
\]
于是
\[
\begin{aligned}
I_+(g_a)-I_+(g)
&=
2\int\langle R_g^+,K_a\rangle\,d\mu
+\int|K_a|^2\,d\mu+o(a^2)\\
&=
-2\pi^2a^2R_p^+(\zeta,\zeta)+o(a^2).
\end{aligned}
\]
代入式 (1)，得到
\[
\boxed{
\frac{P(g_a)-P(g)}{8\pi^2}
=
1-a^2R_p^+(\zeta,\zeta)+o(a^2).
}
\tag{11}
\]

这同时说明为何一般背景中的 \(W^-\) 与 \(\operatorname{Ric}^{\circ}\) 不在线性项出现：拓扑恒等式把相对能量完全写成 \(R^+\) 的能量变化，而 Burns 通量是 \(\Lambda^+\) 上的秩一矩。

---

## 5. Weyl 与标量两部分的独立系数

由式 (9) 取迹，
\[
\int\delta s\,d\mu
=
4\operatorname{tr}\int\delta R^+\,d\mu
=
-4\pi^2a^2.
\]
再由
\[
\delta W^+
=
\delta R^+-\frac{\delta s}{12}\operatorname{Id},
\]
得到
\[
\int\delta W^+\,d\mu
=
-\pi^2a^2
\left(
\zeta\otimes\zeta-\frac13\operatorname{Id}
\right)+o(a^2).
\tag{12}
\]

若
\[
\mathcal W_+(g)=\int|W_g^+|^2d\mu_g,\qquad
\mathcal S(g)=\int s_g^2d\mu_g,
\]
则
\[
\Delta\mathcal W_+
=
-2\pi^2a^2W_p^+(\zeta,\zeta)+o(a^2),
\tag{13}
\]
以及
\[
\Delta\mathcal S
=
-8\pi^2a^2s(p)+o(a^2).
\tag{14}
\]
所以
\[
4\Delta\mathcal W_+
=
-8\pi^2a^2W_p^+(\zeta,\zeta)+o(a^2),
\]
\[
\frac1{12}\Delta\mathcal S
=
-8\pi^2a^2\frac{s(p)}{12}+o(a^2),
\]
正好给出会话笔记中的两个分量。

特别值得强调：Weyl 系数和标量系数并不是两个独立的数值拟合；它们都由式 (9) 的单个秩一矩强制确定。

---

## 6. 匹配条件与可严格化的误差估计

一个足以推出式 (11) 的构造可采用尺度 \(\delta_a\)，满足
\[
a\ll \sqrt a\ll\delta_a\ll1
\]
——这里已把背景曲率长度归一为一。更不依赖单位的写法是
\[
\frac{a}{\delta_a}\to0,\qquad
\frac{a^2}{\delta_a^4}\to0,\qquad
\delta_a\to0.
\]

所需匹配结构为：

1. 在固定内尺度 \(r=a\rho\) 上，
   \[
   a^{-2}g_a\longrightarrow g_{B,1}
   \]
   于紧集上光滑收敛；下一项包含背景的二次正规坐标 jet，而不是把整个小球粗略替换成纯 Burns 度量。

2. 在 \(a\ll r\ll\delta_a\) 上，
   \[
   g_a=g+a^2H_\zeta+q_a,
   \]
   其中 \(q_a\) 的加权二阶导数对曲率能量的贡献为 \(o(a^2)\)。

3. 在 \(r\sim\delta_a\) 上，通过径向 Kähler 插值关闭 \(a^2H_\zeta\)。该环带的曲率量级为
   \[
   O(a^2\delta_a^{-4}),
   \]
   因而其纯平方能量为
   \[
   O(a^4\delta_a^{-4})=o(a^2).
   \]

4. 背景曲率在环带上冻结为 \(R_p^+\) 所产生的误差是
   \[
   O(a^2\delta_a)=o(a^2)
   \]
   或在中心对称匹配下更小。

对于非 Einstein 背景，拼接必须收缩到 \(p\)，否则一个固定大小区域内的光滑度量扰动还会带来依赖该区域的普通一阶变分。对于 Einstein 背景，\(P(g)=0\)，故任意光滑紧支扰动在 \(g\) 处的一阶变分本来就是零，局部性的来源更直接。

这些估计足以给出 \(o(a^2)\) 余项。会话材料尚未包含把它们逐项写成一个完整加权 Hölder 或 Sobolev 拼接证明的文本，但决定一阶系数的式 (5)–(9) 已是显式计算，而非数值推断。

---

## 7. 为什么这是极小 cell 的一阶值，而不是每个插值的值

任意插值都可以在 crossover 区域加入额外的非 Kähler 模态；这样的模态可能贡献正的 \(O(a^2)\) 曲率能量。早先 diabatic ansatz 所产生的额外代价正属于这一现象。

把 crossover 变量取为
\[
r=\sqrt a\,y,
\]
则背景二次 jet 与 Burns 尾项都以 \(a\) 阶进入缩放后的度量。在线性化层面，预期的二次泛函为
\[
a^{-2}\bigl(P(g_a)-P(g)-8\pi^2\bigr)
=
-8\pi^2R_p^+(\zeta,\zeta)
+
4\int_{\mathbf R^4\setminus\{0\}}
|D R_0^+(v)|^2\,dy
+o(1),
\tag{15}
\]
其中 \(v\) 是除固定 Burns 源以外的 source-free 匹配模态。常曲率张量与 \(D R_0^+(v)\) 的交叉积分经分部积分消失；剩下的是非负平方。把 Burns 尾项的关闭位置送到 \(y=\infty\)，该关闭层的平方能量趋于零，而式 (9) 的通量保持不变。

因此式 (15) 给出极小值
\[
-8\pi^2R_p^+(\zeta,\zeta),
\]
也解释了为何绝热匹配得到笔记中的 \(6\cos^2\theta\)，而强迫 eigenvalue crossing 的插值会额外付出 \(O(a^2)\)。

把这一点做成所有 admissible cell 上的严格下界，需要一个 crossover 的 Γ-收敛定理：在 Bianchi 规范下取得加权紧性，分离微分同胚、尺度、中心和转动模态，并证明任何有限的一阶能量序列都收敛到式 (15) 的线性化模型。 supplied computations 已给出强烈的数值结构，但这个加权紧性与模态分解尚未写出。

---

## 8. \(O(a^4)\) 余项还需要什么

球面通量直接给出的是
\[
1-a^2R^+(\zeta,\zeta)+o(a^2).
\]
若要把余项提升为统一的 \(O(a^4)\)，还需完成二阶 matched expansion：

\[
g_a
=
g_B+a^2q_2(R_p)+a^3q_3(\nabla R_p)
+a^4q_4(R_p^2,\nabla^2R_p)+\cdots
\]
并求解 Burns 上相应的线性化曲率方程。

中心反演对称性应使 \(a^3\) 标量项消失，但四维临界缩放可能产生
\[
a^4\log a
\]
项；必须通过显式二阶方程或 indicial-root 计算确认其系数为零。还需处理 Burns Jacobi 模态与外侧 jet 的正交条件。因此，会话中的 \(O(a^4)\) 目前应读作数值所支持的二阶行为；一阶系数和符号则已有上面的解析通量计算。

---

## 9. 与 Ozuch–Biquard 张量 \(R^+\zeta\) 的关系

一阶相互作用势可写为
\[
\mathcal V(t,\zeta)
=
-t\,\langle R_p^+\zeta,\zeta\rangle,
\qquad t=a^2.
\]
其尺度导数为
\[
\partial_t\mathcal V
=
-\langle R_p^+\zeta,\zeta\rangle,
\]
而在单位球 \(S(\Lambda^+)\) 上的方向导数为
\[
\nabla_\zeta\mathcal V
=
-2t\,\Pi_{\zeta^\perp}(R_p^+\zeta).
\]
因此：

- 尺度方向检测 \(R^+(\zeta,\zeta)\)；
- 转动方向检测 \(R^+\zeta\) 在 \(\zeta^\perp\) 上的分量；
- 两者同时为零恰好给出
  \[
  R_p^+\zeta=0.
  \]

这说明 Burns 能量的一阶相互作用是 Ozuch/Biquard Einstein 拼接张量的标量势。二者不是同一个方程：能量只取了一个标量收缩，而 Einstein 方程投影到全部 ALE Jacobi 模态后产生向量条件。若 \(R^+\) 半定，则
\[
R^+(\zeta,\zeta)=0
\quad\Longleftrightarrow\quad
R^+\zeta=0;
\]
若 \(R^+\) 不定，标量收缩为零仍可能有 \(R^+\zeta\neq0\)。

---

## 10. 复双曲与 Fubini–Study 的符号反转

对 Kähler 四维度量，以单位 Kähler 形式 \(\omega\) 为第一基向量，
\[
R^+=\operatorname{diag}\left(\frac{s}{4},0,0\right).
\]
脚本采用
\[
K_{\mathrm{bulk}}=x+\kappa x^2,\qquad s=-24\kappa,
\]
故
\[
R^+=-6\kappa\,\omega\otimes\omega.
\]
若
\[
\langle\zeta,\omega\rangle=\cos\theta,
\]
则
\[
-R^+(\zeta,\zeta)
=
6\kappa\cos^2\theta.
\tag{16}
\]

于是：

- 复双曲号 \(\kappa=+1\)：
  \[
  \frac{P_{\rm cell}}{8\pi^2}
  =
  1+6a^2\cos^2\theta+o(a^2);
  \]
- Fubini–Study 号 \(\kappa=-1\)：
  \[
  \frac{P_{\rm cell}}{8\pi^2}
  =
  1-6a^2\cos^2\theta+o(a^2).
  \]

在复双曲情形 \(s=-24\) 时，
\[
-\frac{s}{12}=2,
\]
而
\[
-W^+(\zeta,\zeta)
=
2(3\cos^2\theta-1).
\]
两者相加正好是
\[
2+2(3\cos^2\theta-1)=6\cos^2\theta.
\]
当 \(\theta=\pi/2\) 时，Weyl 的 \(-2a^2\) 与标量的 \(+2a^2\) 精确抵消；这就是数值表中一阶项消失、只剩二阶效应的解析原因。Fubini–Study 情形所有这些符号同时反转，正好对应 `o11_general_bulk_cell.py` 中的预测斜率 \(6\kappa\)。

综上，最稳固的解析结论是：在会话尺度与定向约定下，Burns \(r^{-2}\) 尾项具有
\[
\int\delta R^+=-\pi^2a^2\zeta\otimes\zeta
\]
这一普适秩一曲率矩；Chern–Weil 恒等式随后强制给出
\[
\frac{P_{\rm cell}}{8\pi^2}
=
1-a^2R_p^+(\zeta,\zeta)+o(a^2).
\]
严格的 \(O(a^4)\) 余项以及对全部 cell 极小化的完整定理，还取决于二阶 Burns 匹配方程与 crossover 加权紧性分析。
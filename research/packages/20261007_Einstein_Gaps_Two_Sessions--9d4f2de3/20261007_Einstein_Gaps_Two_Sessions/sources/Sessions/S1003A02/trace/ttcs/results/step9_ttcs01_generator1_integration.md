# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 9,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step9_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step9_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop a mathematically precise proof route for the universal first-order Burns cell law suggested by the attached note and computations. Let an oriented smooth Einstein or general curved 4-manifold have curvature operator self-dual block R^+=W^++s/12 at p, and insert a small Burns O(-1) cell whose Kähler form at infinity is ζ∈Λ^+_p. The proposed expansion in the session normalization is ∫cell |Ric°|²/(8π²)=1-a² R^+(ζ,ζ)+O(a^4) (equivalently the separate first variations are -a²W^+(ζ,ζ) and -a²s/12). Give the strongest derivation you can: identify the ALE boundary term/renormalized Chern-Weil or matched-asymptotic calculation that fixes the coefficient and sign, state gauge and matching hypotheses, and distinguish what is actually proved from what still needs an explicit calculation. Explain the relation to Ozuch/Biquard desingularization obstruction R^+ζ=0 and to the Fubini–Study/complex-hyperbolic sign reversal in the provided computational result. Do not invent literature; reason from the supplied artifacts.

## Integrated Scientific Memo

## Burns 一阶 cell law：可证明部分、形式推导与尚缺计算

记
\[
P(g)=\int |\Ric_g^\circ|^2\,d\mu_g,\qquad
I_+(g)=\int |R_g^+|^2\,d\mu_g,\qquad
R^+=W^++\frac{s}{12}\Id_{\Lambda^+}.
\]
尺度参数采用脚本约定 \(x_0=a^2\)，即 Burns 径向函数 \(K=x-a^2\)、\(x=r^2\)。单位自对偶形式 \(\zeta\in\Lambda_p^+\) 表示 Burns Kähler 方向。

核心结论应分成两层：

1. **拓扑恒等式、允许的张量形式以及 CH/FS 符号反转是严格的；**
2. **系数恰为 \(-1\) 的证明可归结为一个显式 Burns 无穷远 transgression 计算，但现有材料尚未真正完成该计算。**  
   因而目前最稳妥的解析结论是一个有明确待验边界常数的公式；数值结果强烈表明该常数取所需值。

---

### 1. Chern–Weil 的精确归约

在会话规范下，
\[
P=4\int |W^+|^2+\frac1{12}\int s^2-8\pi^2T_+
   =4I_+-8\pi^2T_+ .
\tag{1}
\]
一次反向 blow-up 使
\[
T_+(M\#\overline{\CP}^{\,2})=T_+(M)-1.
\]
因此，对在 \(p\) 附近插入一个 Burns 块所得 \(g_a\)，有精确相对恒等式
\[
P(g_a)-P(g)
=
8\pi^2+4\bigl(I_+(g_a)-I_+(g)\bigr).
\tag{2}
\]
所以目标 cell law
\[
\frac{P(g_a)-P(g)}{8\pi^2}
=1-a^2R_p^+(\zeta,\zeta)+O(a^4)
\tag{3}
\]
等价于
\[
I_+(g_a)-I_+(g)
=-2\pi^2a^2R_p^+(\zeta,\zeta)+O(a^4).
\tag{4}
\]

这一步还说明：一阶项中不需要独立出现 \(W^-\) 或背景 \(\Ric^\circ\)。相对能量已由 \(R^+\) 与拓扑跳跃完全控制。对一般非 Einstein 背景，式 (3) 应理解为相对于被删除背景小球的局部相对量；若背景 Einstein，则 \(P(g)=0\)，解释最直接。

---

### 2. 对称性先把未知压缩到两个常数

在正规坐标和平行标架下，背景曲率在第一阶可冻结为 \(R_p^+\)。Burns 数据除尺度外只给出单位向量 \(\zeta\in\Lambda^+\)。因此 \(SO(3)_+\)-等变性迫使一阶响应具有形式
\[
-a^2\left(c_W\,W_p^+(\zeta,\zeta)+c_s\,s(p)\right),
\tag{5}
\]
或等价地，其积分曲率矩必须形如
\[
\int \delta R^+
=-C\,a^2\,\zeta\otimes\zeta
-C_0a^2\,\Id .
\tag{6}
\]
Burns 尾项的 Kähler/rank-one 结构预期排除额外的独立 \(\Id\) 项，并给出
\[
\int\delta R^+
=-\pi^2a^2\,\zeta\otimes\zeta.
\tag{7}
\]
若 (7) 成立，则 Weyl 和 scalar 系数不再独立，二者自动都等于目标值。现有 CH 数值把这两个分量分别测得为
\[
-a^2W^+(\zeta,\zeta),\qquad -a^2\frac{s}{12},
\]
误差约在百分之几内；但数值不能代替 (7) 的解析边界计算。

---

### 3. Burns 尾项与候选边界通量

在 \(\zeta\) 所确定的正交复结构 \(J_\zeta\) 下，Burns 度量可写为
\[
g_{B,a}
=
\frac{r^2}{r^2-a^2}\,dr^2
+r^2(\sigma_1^2+\sigma_2^2)
+(r^2-a^2)\sigma_3^2 .
\]
相对于欧氏度量，
\[
g_{B,a}=g_0+a^2H_\zeta+O(a^4r^{-4}),
\tag{8}
\]
其中
\[
H_\zeta
=r^{-2}\left(dr\otimes dr-(J_\zeta dr)\otimes(J_\zeta dr)\right).
\tag{9}
\]
令 \(n=x/r\)、\(m=J_\zeta n\)，则
\[
(H_\zeta)_{ij}=r^{-2}(n_in_j-m_im_j),
\]
并可直接验证
\[
\tr H_\zeta=0,\qquad
\partial_j(H_\zeta)_{ij}=2r^{-3}n_i.
\tag{10}
\]
于是标量曲率线性化的球面通量为
\[
\int_{S_r}
\bigl(\div H_\zeta-d\tr H_\zeta\bigr)(n)\,dA
=4\pi^2.
\tag{11}
\]

式 (11) 是正确的候选 renormalized boundary charge，也是固定尺度和符号的关键。但需要谨慎：

- 由 (11) 可以严格得到标量线性化的分布通量；
- **不能仅凭标量通量就断言完整的矩阵恒等式 (7)**；
- 要得到 (7)，必须显式计算 \(DR^+_{g_0}(H_\zeta)\) 的 Chern–Simons/transgression 边界积分，或证明所选 Kähler 匹配使其严格保持 rank-one 形式。

形式上，若匹配环带在与 \(J_\zeta\) 相容的径向 Kähler 类内完成，则四维 Kähler 曲率满足
\[
R^+=\frac{s}{4}\,\zeta\otimes\zeta
\tag{12}
\]
（\(\zeta\) 为单位 Kähler 方向），于是内外边界方向约定给出
\[
\int_{\rm annulus}\delta s=-4\pi^2a^2,
\qquad
\int_{\rm annulus}\delta R^+
=-\pi^2a^2\zeta\otimes\zeta.
\tag{13}
\]
负号来自：奇异尾项在被移除的原点具有正的外向通量，而光滑 scalar-flat Burns 核不含对应分布源，因此将尾项向外关闭的 transition annulus 携带相反通量。

这给出非常具体的待完成计算：

\[
\boxed{
\lim_{R\to\infty}
\int_{S_R/\Gamma}
\mathcal T_{R^+}(H_\zeta)
=-\pi^2\,\zeta\otimes\zeta
}
\tag{14}
\]
其中 \(\mathcal T_{R^+}\) 是 \(R^+\) 线性化分部积分产生的矩阵值 transgression 3-form，方向应按“Burns 核向外、被删背景球向内”统一。直接在 (9) 上计算 (14)，才是固定系数与符号的决定性 ALE 边界步骤。

---

### 4. 假设曲率矩后，一阶定律的推导

设匹配后自对偶曲率变化为 \(K_a\)，并满足
\[
\int K_a\,d\mu
=-\pi^2a^2\zeta\otimes\zeta+o(a^2),
\tag{15}
\]
以及
\[
\int |K_a|^2\,d\mu=o(a^2).
\tag{16}
\]
在正规标架中
\[
R_g^+(x)=R_p^++O(r).
\]
因此
\[
\begin{aligned}
I_+(g_a)-I_+(g)
&=2\int\langle R_g^+,K_a\rangle\,d\mu
  +\int |K_a|^2\,d\mu+o(a^2)\\
&=-2\pi^2a^2R_p^+(\zeta,\zeta)+o(a^2).
\end{aligned}
\tag{17}
\]
代入 (2) 得
\[
\boxed{
\frac{P(g_a)-P(g)}{8\pi^2}
=1-a^2R_p^+(\zeta,\zeta)+o(a^2).
}
\tag{18}
\]

由 (13) 取迹，
\[
\int\delta s=-4\pi^2a^2,
\tag{19}
\]
并且
\[
\int\delta W^+
=-\pi^2a^2
\left(\zeta\otimes\zeta-\frac13\Id\right).
\tag{20}
\]
故与冻结背景的交叉项分别给出
\[
\Delta\!\int|W^+|^2
=-2\pi^2a^2W_p^+(\zeta,\zeta)+o(a^2),
\tag{21}
\]
\[
\Delta\!\int s^2
=-8\pi^2a^2s(p)+o(a^2).
\tag{22}
\]
利用 (1)，即
\[
\frac{4\Delta\int|W^+|^2}{8\pi^2}
=-a^2W_p^+(\zeta,\zeta)+o(a^2),
\]
\[
\frac{\Delta\int s^2/12}{8\pi^2}
=-a^2\frac{s(p)}{12}+o(a^2).
\tag{23}
\]
这正是所要求的两个独立第一变分。

---

### 5. 规范和 matched-asymptotic 假设

一个足以证明 \(o(a^2)\) 版本的框架如下。

#### 外侧规范

在 \(p\) 处用定向正规坐标，并由径向平行移动识别 \(\Lambda^+\)。背景展开为
\[
g_{ij}=\delta_{ij}-\frac13R_{ikjl}(p)x^kx^l+O(r^3).
\tag{24}
\]

#### 内侧规范

在 \(r=a\rho\) 下，
\[
a^{-2}g_a\longrightarrow g_{B,1}
\]
于 Burns 紧集上光滑收敛。尺度由 bolt 条件固定，避免尺度 Jacobi 模态改变 \(a\) 的定义。

#### Bianchi 规范和零模态

余项应置于欧氏或 Burns 背景的 Bianchi 规范，并与以下模态正交：

- 平移；
- 尺度；
- 整体转动；
- 由衰减向量场产生的纯微分同胚模态。

允许的 gauge transformation 必须保持 \(r^{-2}\) 首项及其边界通量；例如 \(X=o(r^{-1})\) 的变换不会改变 (14)。

#### 中间区

取拼接半径 \(\delta_a\) 满足
\[
\delta_a\to0,\qquad
\frac a{\delta_a}\to0,\qquad
\frac{a^2}{\delta_a^4}\to0.
\tag{25}
\]
在 \(a\ll r\ll\delta_a\) 中要求
\[
g_a=g+a^2H_\zeta+q_a,
\tag{26}
\]
其中 \(q_a\) 的加权 \(C^2\) 或 \(W^{2,2}\) 范数足以使其曲率能量为 \(o(a^2)\)。

关闭 \(a^2H_\zeta\) 的环带中，
\[
|\Rm_{\rm transition}|\sim O(a^2\delta_a^{-4}),
\]
故纯平方贡献为
\[
O(a^4\delta_a^{-4})=o(a^2).
\tag{27}
\]
冻结背景曲率的误差为 \(O(a^2\delta_a)=o(a^2)\)，在中心对称匹配下还可更小。

这些假设足以把系数问题集中到 (14)。

---

### 6. \(O(a^4)\) 目前不能由现有材料宣布为已证

上述边界矩方法自然给出
\[
1-a^2R^+(\zeta,\zeta)+o(a^2).
\]
要升级为题设的
\[
1-a^2R^+(\zeta,\zeta)+O(a^4),
\tag{28}
\]
必须完成二阶 matched expansion，例如
\[
g_a=g_B+a^2q_2(R_p)+a^3q_3(\nabla R_p)
+a^4q_4(R_p^2,\nabla^2R_p)+\cdots
\tag{29}
\]
并分析 Burns 线性化算子的 indicial roots、Jacobi 模态和 solvability 条件。

特别需要排除：

- \(a^3\nabla R\) 项；中心对称性预期使相应标量贡献消失，但需证明；
- 四维临界尺度可能产生的 \(a^4\log a\)；
- crossover 中非 Kähler 模态的额外 \(O(a^2)\) 平方能量。

因此，现有证据支持 \(O(a^4)\)，但严格可安全声称的是 \(o(a^2)\)，除非补上二阶 ALE 匹配计算。

同样，公式对一个精心构造的绝热匹配给出上界；若要证明它是**所有 admissible cells 的一阶极小值**，还需要 crossover 的加权紧性或 \(\Gamma\)-收敛。旧的 diabatic ansatz 强迫塌缩方向与外侧 fibre 在特征值交叉处错误相接，产生额外 \(O(a^2)\) 代价；Step 8 的 fixed-slot/adiabatic 计算正是对此伪影的修正。

---

### 7. 与 Ozuch–Biquard 障碍的精确关系

一阶相互作用势为
\[
\mathcal V(t,\zeta)
=-t\,\langle R_p^+\zeta,\zeta\rangle,
\qquad t=a^2.
\tag{30}
\]
其尺度导数和单位球 \(S(\Lambda^+)\) 上的方向导数分别是
\[
\partial_t\mathcal V=-\langle R_p^+\zeta,\zeta\rangle,
\tag{31}
\]
\[
\nabla_\zeta\mathcal V
=-2t\,\Pi_{\zeta^\perp}(R_p^+\zeta).
\tag{32}
\]
二者同时消失当且仅当
\[
R_p^+\zeta=0.
\tag{33}
\]

因此：

- cell 能量的一阶尺度响应检测标量收缩 \(R^+(\zeta,\zeta)\)；
- 旋转模态检测 \(R^+\zeta\) 的正交分量；
- Einstein desingularization 投影到全部 ALE Jacobi 模态后得到向量障碍 \(R^+\zeta=0\)。

所以 cell law 是 Ozuch/Biquard 障碍的标量势，而不是与向量障碍逐字相同。若 \(R^+\) 半定，则
\[
R^+(\zeta,\zeta)=0\iff R^+\zeta=0.
\]
若 \(R^+\) 不定，则二次型可在非核方向为零，不能从 cell 一阶成本为零推出 Einstein 障碍消失。

---

### 8. 复双曲与 Fubini–Study 的符号反转

对 Kähler 四维度量，以单位 Kähler 方向 \(\omega\) 为第一基向量，
\[
R^+=\diag\left(\frac s4,0,0\right).
\tag{34}
\]
脚本采用
\[
K_{\rm bulk}=x+\kappa x^2,\qquad s=-24\kappa,
\]
故
\[
R^+=-6\kappa\,\omega\otimes\omega.
\tag{35}
\]
若
\[
\langle\zeta,\omega\rangle=\cos\theta,
\]
则
\[
-R^+(\zeta,\zeta)=6\kappa\cos^2\theta.
\tag{36}
\]

于是 CH 号 \(\kappa=+1\) 给出
\[
\frac{P_{\rm cell}}{8\pi^2}
=1+6a^2\cos^2\theta+o(a^2),
\tag{37}
\]
而 FS 号 \(\kappa=-1\) 给出
\[
\frac{P_{\rm cell}}{8\pi^2}
=1-6a^2\cos^2\theta+o(a^2).
\tag{38}
\]
这正对应 `o11_general_bulk_cell.py` 的 predicted slope \(6\kappa\)。

在 CH 情形 \(s=-24\)：
\[
-\frac{s}{12}=2,
\qquad
-W^+(\zeta,\zeta)=2(3\cos^2\theta-1),
\]
故
\[
2+2(3\cos^2\theta-1)=6\cos^2\theta.
\tag{39}
\]
当 \(\theta=\pi/2\) 时，scalar 的 \(+2a^2\) 与 Weyl 的 \(-2a^2\) 精确抵消，一阶项为零；这解释了计算中只剩正的 \(O(a^4)\)-量级余项，也与
\[
\ker R^+=\omega^\perp
\]
上的 Ozuch/Biquard 第一障碍消失完全一致。FS 中背景曲率整体换号，因此两部分以及总 slope 同时反转。

---

## 最终证明状态

目前材料支持的最强严谨路线是：

\[
\boxed{
\text{Chern--Weil 拓扑跳跃}
+\text{Burns 的矩阵值 ALE transgression}
\Longrightarrow
\frac{P_{\rm cell}}{8\pi^2}
=1-a^2R_p^+(\zeta,\zeta)+o(a^2).
}
\]

其中已明确并可直接验证的是：

- Chern–Weil 归约 (1)–(2)；
- Burns \(r^{-2}\) 尾项 (8)–(9)；
- scalar 边界通量 \(4\pi^2\)；
- 若矩阵值曲率矩 (13) 成立，则所有系数、符号、Weyl/scalar 分裂、CH/FS 反转及 Ozuch/Biquard 联系都随之严格推出。

仍需显式完成的核心对象只有
\[
\int_{S^3_\infty}\mathcal T_{R^+}(H_\zeta)
\]
的矩阵值计算，确认它恰为 \(-\pi^2\zeta\otimes\zeta\)（按拼接边界方向）；而 \(O(a^4)\) 余项及“对全部 cells 的极小律”还分别需要二阶 matched expansion 和 crossover 的加权紧性/\(\Gamma\)-收敛分析。
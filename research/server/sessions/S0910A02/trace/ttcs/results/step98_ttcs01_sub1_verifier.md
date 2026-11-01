# TTCS Independent Branch Record

```json
{
  "step_id": 98,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step96_corrected_selection_and_determinantal.md",
    "Sessions/S0910A02/workspace/notes/step94_three_gates_and_highdim_theorem.md",
    "Sessions/S0910A02/workspace/data/step97_gradient_quartic_audit.json",
    "Sessions/S0910A01/workspace/notes/step97_ab_physical_cone_interpretation.md",
    "Knowledge/objects/papers/Smoothing-singular-extremal-Kähler-surfaces-and-minimal-Lagrangians--76bcf086d1fb--80cf6934cc4e/object.md",
    "Knowledge/objects/papers/COMPACT-MODULI-SPACES-OF-DEL-PEZZO-SURFACES--3cb2439eac00--b970fe5e4bdb/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Critically verify the revised positive Gate-3 calibration for the Yau 26 project. The claim to assess is: for the four-A1 quotient (P^1 x P^1)/Z2 in the degree-4 del Pezzo KE compactification, the compatible Kähler smoothing directions correspond to Eguchi-Hanson periods in the kernel planes orthogonal to the local Kähler form, while the excluded holomorphic resolution direction is the Kähler exceptional-curve direction. Therefore the full Lyapunov-Schmidt reduced Einstein obstruction, viewed as the gradient of a normalized Einstein-Hilbert/scalar-curvature functional after solving the complement in a suitable slice, should have its leading quartic f4 vanish on the compatible KE smoothing locus. In particular, same-chirality self and pair coefficients should vanish in the full calibrated LS potential; partial raw spectral sectors such as the AB coefficient need not vanish alone but must cancel after all sectors and coordinate/complement/global corrections. Please check what is actually supported by the supplied sources, what assumptions about gauge/slice/coordinates/automorphisms are needed, and what should not be claimed. Also judge whether the old Gate-3 criterion |q_diag| versus |2q_adj+q_diag| must be replaced by a calibrated real quartic on physical scale/phase/global-deformation variables, and whether local obstruction can or cannot imply global no-Einstein for Yau 26.

## Output

# 科学复核备忘

## 总结

1. **局部 Kähler 几何解释成立。** 对 \(A_1\) Kronheimer 模型，固定复结构 \(I_1\) 后，
   \[
   \zeta=(\zeta_r,\zeta_c),\qquad \zeta_c=\zeta_2+i\zeta_3,
   \]
   其中 \(\zeta_r\) 是 Kähler 类在消失球上的周期，\(\zeta_c\) 是复平滑参数。因而 \(\zeta_r=0,\ \zeta_c\ne0\) 是 Kähler 平滑方向，而 \(\zeta_c=0,\ \zeta_r\ne0\) 给出带全纯 \((-2)\)-球的消解方向。对等曲率的 \(S^2\times S^2\)，后者正是局部 Kähler 形式所在的曲率特征线，前者是其正交二维核平面。

2. **精确 KE 分支确实迫使首个四次势在其切锥上满足**
   \[
   df_4=0,\qquad f_4=0.
   \]
   但这需要真正的变分型 Lyapunov–Schmidt 构造、固定体积、微分同胚切片、稳定子群商以及与 Kronheimer 周期相容的坐标。现有材料没有直接构造这个 \(f_4\)。

3. **“同手征自项和配对项的系数分别为零”不能由 KE 分支推出。** 正确结论只是：所有局部、配对、补空间、投影运动和全局耦合项的总和，在实际 KE 分支上给出零梯度。非零系数完全可以通过平衡方程组合成一个在 KE 子流形上为零的势。

4. 旧的
   \[
   |q_{\rm diag}|\quad\hbox{与}\quad |2q_{\rm adj}+q_{\rm diag}|
   \]
   比较式不能决定混合分支。除遗漏变量与相位外，它还包含一个直接的线性代数错误：对
   \[
   L(z)=Pz+Q\bar z
   \]
   而言，只有 \(|P|=|Q|\) 时才有非零核；\(|P|<|Q|\) 与 \(|P|>|Q|\) 时都可逆。

5. 即使混合配置的局部四次方程严格排除邻近 Einstein 退化，它也只涉及该特定 Gromov–Hausdorff 退化附近的度量，不能推出同一光滑流形完全不承载 Einstein 度量，更不能单独解决 Yau 第 26 题中的全称量词。

---

## 1. Kronheimer 周期与曲率核平面的对应

Biquard–Rollin §2.2 的 Kronheimer 参数满足：

- \(H^2(Y_\zeta,\mathbb R)\simeq\mathfrak h\)，三条 Kähler 形式的上同调类分别是 \(\zeta_1,\zeta_2,\zeta_3\)；
- 固定 \(I_1\) 后写作
  \[
  \zeta_r=\zeta_1,\qquad \zeta_c=\zeta_2+i\zeta_3;
  \]
- Lemma 6 表明：\(\theta(\zeta_r)=0\) 时根类 \(\theta\) 是 Lagrangian 类；\(\theta(\zeta_c)=0\) 时它由全纯曲线表示。

对 \(A_1\)，\(\mathfrak h\simeq\mathbb R\)，所以：

\[
\begin{array}{c|c}
(\zeta_r,\zeta_c)&\text{固定 }I_1\text{ 下的几何}\\ \hline
(0,\zeta_c\ne0)&\text{复平滑，消失球为 Lagrangian}\\
(\zeta_r\ne0,0)&\text{消解，全纯 }(-2)\text{-球的面积由 }|\zeta_r|\text{给出}
\end{array}
\]

同时，对两个 Gauss 曲率均为 \(\kappa\) 的球面乘积，若
\[
\omega_1^\pm=\frac{e^{12}\pm e^{34}}{\sqrt2},
\]
则曲率算子满足
\[
R^\pm\omega_1^\pm=\kappa\omega_1^\pm,\qquad
R^\pm\omega_2^\pm=R^\pm\omega_3^\pm=0.
\]
因此
\[
R^\pm=\operatorname{diag}(\kappa,0,0).
\]
局部 Kähler 形式给出第一条特征线，而
\[
K^\pm=(\omega_1^\pm)^\perp
\]
正是复平滑周期 \((\zeta_2,\zeta_3)\) 所在平面。这也与 Ozuch 的首阶公式
\[
\lambda_k(\zeta^\pm)
 =c\langle R^\pm\zeta^\pm,\zeta_{(k)}^\pm\rangle
\]
一致：\(\zeta\in K^\pm\) 时首阶项消失，Kähler 消解方向 \(\zeta\parallel\omega_1^\pm\) 则不消失。

Ozuch 的二阶径向公式也与此相容：在适配基下，余下 \(2\times2\) 曲率块仍含一个零方向，所以其行列式为零。所附 \(T^2\) 权重论证还能排除 \(K\to K\) 的齐次二次等变映射；这一步要求 Bianchi 切片、投影和补空间均取为 \(T^2\)-等变，可通过对紧群平均实现。它排除的是原始局部二次自响应，并不排除消去全局模式后重新出现的 \(|\xi_j|^4\) 有效项。

---

## 2. KE 紧化资料实际给出的信息

Odaka–Spotti–Sun 的 Theorems 4.1–4.2 给出：

- 四节点曲面
  \[
  X_{4T}\simeq (\mathbb P^1\times\mathbb P^1)/\mathbb Z_2
  \]
  是唯一的四 \(A_1\) 多重节点曲面；
- 它是 degree-4 KE 模空间中的点；
- 光滑 degree-4 del Pezzo 曲面构成稠密开集并承载 KE 度量。

所以确有光滑 KE 序列趋于 \(X_{4T}\)。Biquard–Rollin §7.1 也明确讨论该四 \(A_1\) 商空间及其 KE 平滑。

但两篇来源尚未直接给出以下更精细的识别：

- 任意四个原始局部平滑参数与某个固定 Einstein 切片中的 EH 周期 \(\xi_j\) 一一相同；
- 所有节点可任意独立取尺度和相位；
- 存在来源中已经构造好的等尺度分支；
- 等尺度分支直接产生
  \[
  |2c_{\rm adj}+c_{\rm diag}|=|q_{\rm diag}|
  \]
  这一系数恒等式。

这里自动同构尤其重要。\(X_{4T}\) 至少有 \((\mathbb C^*)^2\) 连通自动同构群，其紧子群正是选择规则中使用的 \(T^2\)。Biquard–Rollin 主定理的“无非平凡全纯向量场”假设并不直接适用于 \(X_{4T}\)；文中采用的是对称子空间中的等变版本。OSS 的局部对象则是
\[
\operatorname{Def}(X_{4T})//\operatorname{Aut}(X_{4T}),
\]
而不是未取商的四个节点参数空间。因此 KE 模空间中的一个点对应自动同构轨道，而固定 Einstein 切片通常只取该轨道的平衡代表。原始局部参数中的系数不能直接当作切片坐标中的有效四次系数。

---

## 3. 四次势为零的严格含义

设在固定体积的 Ebin–Bianchi 切片中，对归一化总标量曲率泛函
\[
\mathscr S(g)
 =\operatorname{Vol}(g)^{(2-n)/n}\int R_g\,dV_g
\]
做变分型 Lyapunov–Schmidt 约化。若补空间方程已解为 \(w=w(x)\)，定义
\[
\varphi(x)=\mathscr S(G(x)+w(x)).
\]
则
\[
d\varphi_x(\dot x)
 =\big\langle \operatorname{Grad}\mathscr S,\,
 D_x(G+w)\dot x\big\rangle.
\]
有限维 obstruction 向量是 \(d\varphi\) 经参数切向量 Gram 矩阵转换后的表示，不一定是原始 \(\zeta\) 坐标中的普通 Euclidean 梯度。

若
\[
\varphi(x)=\varphi(0)+f_4(x)+o(|x|^4),\qquad
d\varphi=df_4+o(|x|^3),
\]
且有精确 KE 分支
\[
x(s)=sa+O(s^2),
\]
那么
\[
0=d\varphi(x(s))
  =s^3df_4(a)+o(s^3),
\]
故
\[
df_4(a)=0.
\]
由 Euler 恒等式，
\[
4f_4(a)=df_4(a)[a]=0.
\]

因此正确的校准对象是 **KE 分支切锥上的零临界集**，不只是 \(f_4=0\) 的零值集。反过来，单有 \(f_4(a)=0\) 并不推出 \(df_4(a)=0\)。

上述推导还需要：

- 通过 \(A_1\) Weyl 商的分歧覆盖，以 lifted period \(\xi_j\) 为光滑变量；\(\xi_j\sim-\xi_j\)；
- 固定体积并除去整体缩放；
- 除去微分同胚方向并对 \(T^2\) 稳定子作等变约化；
- 用统一局部标架和统一 \(L^2\) 归一化；
- 将投影运动、标架运动、补空间解和全局变形的同阶贡献全部并入；
- 给出对四次展开及其一阶导数均一致的余项估计。

Ozuch 的
\[
\Phi_{g_0}(g)=\operatorname{Ric}(g)-\Lambda g+\delta_g^*B_{g_0}g
\]
是规范固定算子。其原始 \(\lambda,\mu,\nu\) 系数并未在来源中被证明为 lifted period 坐标下某个实多项式的普通梯度。

---

## 4. 为何不能逐项置零

一个典型实四次势可写成
\[
f_4=
 \sum_i a_i|\xi_i|^4
 +\sum_{i<j}c_{ij}|\xi_i|^2|\xi_j|^2
 +\operatorname{Re}\sum_{i<j}q_{ij}\xi_i^2\bar\xi_j^2
 +f_{4,\mathrm{glob}}.
\]
真正的变分结构在统一标架下要求
\[
c_{ij}\in\mathbb R,\qquad c_{ij}=c_{ji},\qquad
q_{ji}=\overline{q_{ij}},
\]
并允许消去全局模式产生 Schur 补型四次项。

KE 子流形上 \(f_4=df_4=0\) 并不迫使 \(a_i,c_{ij},q_{ij}\) 分别消失。例如
\[
f_4(z_1,z_2)=\bigl(|z_1|^2-|z_2|^2\bigr)^2
\]
在 \(|z_1|=|z_2|\) 上同时满足 \(f_4=0\) 与 \(df_4=0\)，但自项和配对项的系数均非零。这正是自动同构平衡或 moment-map 型结构可能产生的形式。

此外，所附修正选择规则已经表明：角向 \(Q\) 通道取决于节点量
\[
\sigma_j=\varepsilon_js_A^js_B^j,
\]
而不是单由手征决定。因此“同手征配对系数应为零”本身也不是正确的表示论分类。

所附 Step 97 JSON 数据进一步说明：

- AB 邻接贡献为
  \[
  c_{\rm adj}^{AB}=-0.03144249732,
  \]
  对角贡献为
  \[
  c_{\rm diag}^{AB}=0.017726760721,
  \]
  所以兼容行的 AB 部分
  \[
  P^{AB}=2c_{\rm adj}^{AB}+c_{\rm diag}^{AB}
  =-0.045158233919
  \]
  并不为零；
- 检查到的 tensor-odd 邻接角向量级约为
  \[
  |q_{\rm adj}|=0.004002498659
  \]
  ，但这只是一个张量子扇区；
- 旧数值 \(-0.035444995979\) 实际是 AB 径向值与固定角度下一个张量角向值之和，不是纯 \(P\) 系数；
- 两个邻接 \(Q\) 项的相位可使其和的模遍历
  \[
  [0,\ 0.008004997318],
  \]
  所以固定写成 \(2q_{\rm adj}\) 需要额外对称相位假设。

这些数值只表明现有扇区尚未组成完整约化梯度；它们既没有给出精确 KE 抵消，也没有与 KE 存在性冲突。

---

## 5. 旧的模长比较为何不成立

对实线性映射
\[
L(z)=Pz+Q\bar z,
\]
其行列式为
\[
\det_{\mathbb R}L=|P|^2-|Q|^2.
\]
所以
\[
\ker L\ne\{0\}
\quad\Longleftrightarrow\quad
|P|=|Q|.
\]
特别地，\(P=0,\ Q\ne0\) 时 \(L(z)=Q\bar z\) 仍然可逆。因而“\(|Q|>|P|\) 时出现一维核”是错误的；行列式符号只记录实线性映射的取向。

即使某个接收节点满足 \(|P_j|=|Q_j|\)，也只得到该节点、该固定源配置下的非零方向。完整问题要求同时求解所有节点的

\[
\partial_{r_j}f_4=0,\qquad
\partial_{\theta_j}f_4=0,
\]
以及全局变形变量方程，并在
\[
M_j=\xi_j\xi_j^T,\qquad \operatorname{rank}M_j=1,\quad
\operatorname{tr}M_j>0
\]
这一物理 EH 锥上求解。允许任意有符号的 \(\operatorname{Sym}^2(K_j)\) 会引入不对应任何 bubble 的方向。

因此首个有意义的有限维对象是经完整校准的实四次势及其梯度，而不是单节点的两个模长。若该四次势在兼容 KE 子流形上高度退化，混合分支还需更高阶展开。

---

## 6. 与 Yau 第 26 题的关系

Ozuch 的定理研究的是：一列 Einstein 度量是否能以指定 EH bubble 配置趋于某个给定 orbifold。即使混合手征四次势没有非零临界点，所得结论也只是：

> 该光滑拓扑上不存在以所选 bubble 配置、尺度关系和 orbifold 极限出现的邻近 Einstein 分支。

它没有涉及：

- 远离 \(X_{4T}\) 的 Einstein 度量；
- 另一种退化图景；
- 不同 bubble 树；
- 任意符号的 Einstein 常数；
- Yau 第 26 题中任意候选维数常数 \(c_n<C_n\) 所对应的 Ricci 夹逼量词。

所以局部四次 obstruction 可以成为一个严格的局部非存在定理，也可用于识别混合分支；它本身不能推出同一光滑流形全局不存在 Einstein 度量。完整的 Yau-26 证伪还需要独立的全局拓扑或几何机制，以及与通用 Ricci 夹逼常数相匹配的度量构造。
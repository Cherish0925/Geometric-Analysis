# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 98,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step98_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step98_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Critically verify the revised positive Gate-3 calibration for the Yau 26 project. The claim to assess is: for the four-A1 quotient (P^1 x P^1)/Z2 in the degree-4 del Pezzo KE compactification, the compatible Kähler smoothing directions correspond to Eguchi-Hanson periods in the kernel planes orthogonal to the local Kähler form, while the excluded holomorphic resolution direction is the Kähler exceptional-curve direction. Therefore the full Lyapunov-Schmidt reduced Einstein obstruction, viewed as the gradient of a normalized Einstein-Hilbert/scalar-curvature functional after solving the complement in a suitable slice, should have its leading quartic f4 vanish on the compatible KE smoothing locus. In particular, same-chirality self and pair coefficients should vanish in the full calibrated LS potential; partial raw spectral sectors such as the AB coefficient need not vanish alone but must cancel after all sectors and coordinate/complement/global corrections. Please check what is actually supported by the supplied sources, what assumptions about gauge/slice/coordinates/automorphisms are needed, and what should not be claimed. Also judge whether the old Gate-3 criterion |q_diag| versus |2q_adj+q_diag| must be replaced by a calibrated real quartic on physical scale/phase/global-deformation variables, and whether local obstruction can or cannot imply global no-Einstein for Yau 26.

## Integrated Scientific Memo

# Gate‑3 校准复核结论

## 1. 可确认的局部几何

对 \(A_1\) Kronheimer/Eguchi–Hanson 模型，固定复结构 \(I_1\) 后可写
\[
\zeta=(\zeta_r,\zeta_c),\qquad
\zeta_r=\zeta_1,\quad \zeta_c=\zeta_2+i\zeta_3 .
\]
Biquard–Rollin 的 Kronheimer 参数解释给出：

- \(\zeta_r=0,\ \zeta_c\neq0\)：复平滑方向；消失球对 \(I_1\)-Kähler 形式是 Lagrangian；
- \(\zeta_c=0,\ \zeta_r\neq0\)：全纯消解方向；根类由全纯 \((-2)\)-球表示，其 Kähler 面积由 \(\zeta_r\) 控制。

在等曲率 \(S^2\times S^2\) 的节点处，适当归一化后
\[
R^\pm=\operatorname{diag}(\Lambda,0,0),
\]
其中非零特征线由局部 Kähler 形式给出。因此兼容 Kähler 平滑周期位于
\[
K^\pm=(\omega_{\mathrm K}^{\pm})^\perp=\ker R^\pm,
\]
而被排除的全纯消解参数位于 Kähler 特征线。这个核心解释受来源支持。

但须区分：

- EH 的几何手征 \(\pm\)；
- 节点局部标架及极点符号；
- 选择规则中的
  \[
  \sigma_j=\varepsilon_j s_A^j s_B^j.
  \]

角向耦合由 \(\sigma_i=\sigma_j\) 决定，而不是简单由“同手征/异手征”决定。因此任何按手征直接判定 pair coefficient 为零的说法均不可靠。

---

## 2. KE 紧化实际蕴含什么

OSS 确认
\[
X_{4T}\cong(\mathbb P^1\times\mathbb P^1)/\mathbb Z_2
\]
是唯一四 \(A_1\) 的 degree‑4 多项式稳定边界点，并承载 KE orbifold metric；光滑 degree‑4 del Pezzo KE 曲面可以趋于该点。Biquard–Rollin 也明确讨论这一四节点商空间的 KE 平滑。

因此，若在合适切片中完成一个真正变分型的 Lyapunov–Schmidt 约化，得到实约化势
\[
\varphi(x)=\varphi(0)+f_4(x)+o(|x|^4),
\qquad
d\varphi=df_4+o(|x|^3),
\]
而某条精确 KE 分支满足
\[
x(s)=sa+O(s^2),
\]
则必有
\[
df_4(a)=0.
\]
由四次齐次 Euler 恒等式，
\[
4f_4(a)=df_4(a)[a]=0,
\]
故也有
\[
f_4(a)=0.
\]

所以可支持的校准陈述是：

> **完整、变分一致、坐标一致的约化四次势，在兼容 KE 分支的切锥上具有零临界点，因而其值也为零。**

这不是来源中已经显式算出的四次多项式，而是建立完整 LS 构造后由 KE 分支推出的必要条件。

---

## 3. 不应声称个别 self/pair 系数消失

“同手征 self 和 pair 系数在完整校准势中分别为零”并不成立，也不能由 KE 分支推出。KE 存在只要求所有贡献的**总约化梯度**在兼容分支上消失。

例如
\[
f_4(z_1,z_2)=\bigl(|z_1|^2-|z_2|^2\bigr)^2
\]
在 \(|z_1|=|z_2|\) 上同时满足
\[
f_4=0,\qquad df_4=0,
\]
但自项和交叉项系数都非零。因此自动同构平衡、全局变量或补空间 Schur 补完全可能通过非平凡系数组合产生 KE 零集。

Step‑97 的原始扇区数据正说明这一点：

\[
c_{\rm adj}^{AB}=-0.03144249732,\qquad
c_{\rm diag}^{AB}=0.017726760721,
\]
从而兼容行的 AB 部分为
\[
P^{AB}=2c_{\rm adj}^{AB}+c_{\rm diag}^{AB}
      =-0.045158233919\neq0.
\]
这不是与 KE 存在矛盾，而只说明 AB 是未完成的径向 \(P\)-扇区。AA/BB-even、self/opposite-corner、标架与投影运动、补空间解及全局变形必须在同一坐标和规范下共同装配。

同理，已有 tensor-odd 数字只是一个子扇区，不能单独视为完整 \(q_{\rm adj}\)。

---

## 4. 旧 Gate‑3 模长判据必须废弃

旧比较
\[
|q_{\rm diag}|
\quad\text{与}\quad
|2q_{\rm adj}+q_{\rm diag}|
\]
至多是等尺度、固定对称相位、冻结全局变量后的特殊截面，不是一般物理判据。

而且旧 outcome logic 含一个线性代数错误。对
\[
L(z)=Pz+Q\bar z
\]
作为 \(\mathbb R^2\) 上的实线性映射，
\[
\det_{\mathbb R}L=|P|^2-|Q|^2,
\]
故
\[
\ker L\neq0
\iff |P|=|Q|.
\]
无论 \(|P|>|Q|\) 还是 \(|P|<|Q|\)，映射都可逆；行列式符号只改变取向，不能把 \(|Q|>|P|\) 解释为“存在一维核”。

此外，两个邻接角向项具有独立相位。现有数据表明其和的模可在近似区间
\[
[0,\,0.008004997318]
\]
内变化，不能无条件压缩成固定的 \(2q_{\rm adj}\)。

正确的 Gate‑3 对象应为完整实四次势，例如
\[
f_4=
\sum_i a_i|\xi_i|^4
+\sum_{i<j}c_{ij}|\xi_i|^2|\xi_j|^2
+\operatorname{Re}\sum_{i<j}q_{ij}\xi_i^2\bar\xi_j^2
+f_{4,\mathrm{global}},
\]
并在真实变量上求
\[
df_4=0:
\]

- 各节点尺度 \(t_j>0\)；
- 各 kernel-plane 相位 \(\theta_j\)；
- 产品比例等全局 Einstein deformation；
- 除去总体缩放后的固定体积变量；
- 自动同构商后的平衡代表。

等价的物理源是
\[
M_j=t_j^2u_ju_j^T,
\qquad \operatorname{rank}M_j=1,\quad
\operatorname{tr}M_j=t_j^2>0.
\]
在无约束 \(\operatorname{Sym}^2(K_j)\) 上发现的核，未必落在这个正秩一锥上。

---

## 5. 必需的规范、切片与坐标假设

“约化 obstruction 是实势的梯度”需要额外建立，不能直接从 Ozuch 的规范固定算子推出。Ozuch 使用
\[
\Phi_{g_0}(g)
=\operatorname{Ric}(g)-\Lambda g+\delta_g^*B_{g_0}g,
\]
它本身不是所选坐标中的普通 Euclidean 梯度。严谨校准至少需要：

1. **固定体积**，去掉整体尺度方向；
2. **Ebin/Bianchi 型微分同胚切片**；
3. **\(T^2\)-等变投影和补空间**，必要时对紧群平均；
4. 处理 \(X_{4T}\) 的正维自动同构群，在稳定子群商或 Luna/Kuranishi 切片中约化；
5. 通过 \(A_1\) Weyl 分歧覆盖使用光滑 lifted period，注意 \(\xi_j\sim-\xi_j\)；
6. 所有节点采用统一 EH 归一化和统一正交标架运输；
7. 将补空间解、Gram 矩阵、投影/标架运动和全局 deformation 同阶项全部纳入；
8. 对势及其一阶导数均有足够一致的余项控制。

若完整约化确为实梯度，则统一标架下必须满足一致性条件
\[
c_{ij}\in\mathbb R,\qquad c_{ij}=c_{ji},\qquad
q_{ji}=\overline{q_{ij}}.
\]
违反这些条件应优先解释为规范、运输或归一化错误，而不是新的 obstruction。

兼容 KE 校准也应表述为
\[
df_4=0
\]
在实际 KE 轨道或其商像上成立；不能仅用某个等尺度代表导出未经证明的逐系数恒等式。尤其 OSS 给出的是局部 deformation space 的自动同构商，而不是四个节点参数的任意独立直积。

---

## 6. 局部 obstruction 对 Yau 第 26 题的限度

即使完整校准后的混合配置四次势在物理锥上没有非零临界点，结论也仅是：

> 不存在以指定 orbifold 极限、EH 手征配置、尺度渐近和 bubble tree 出现的邻近 Einstein 分支。

它不能排除：

- 远离该边界点的 Einstein metric；
- 其他退化或 bubble tree；
- 不同 Einstein 常数符号；
- 同一光滑流形上完全不同的 Einstein 几何。

本例尤其不能产生“全局无 Einstein”反例，因为相关光滑 degree‑4 del Pezzo 本身已经承载正 Kähler–Einstein metric。因此这一 Gate‑3 计算无论结果如何，都不能单独证伪 Yau 26，也不能提供所需的“满足 Ricci 夹逼但不承载任何 Einstein metric”的流形。

## 最终判定

- **支持**：兼容 Kähler 平滑周期位于局部 Kähler 形式的正交 kernel plane；全纯消解方向是 Kähler exceptional-curve 方向。
- **有条件支持**：完整变分型 LS 四次势必须在兼容 KE 切锥上满足
  \[
  df_4=f_4=0.
  \]
- **不支持**：同手征 self 或 pair 系数应逐项消失。
- **支持替换**：旧模长比较必须改为在真实尺度、相位、自动同构商和全局 deformation 变量上的完整实四次临界点问题。
- **明确否定**：该局部 obstruction 不能推出同一流形全局无 Einstein，更不能单独解决 Yau 第 26 题。
# TTCS Independent Branch Record

```json
{
  "step_id": 96,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step96_source_compatible_kernel_map.md",
    "Sessions/S0910A01/workspace/data/step96_source_receiver_decomposition.json",
    "Sessions/S0910A01/workspace/data/step96_kernel_plane_ab_map.json",
    "Sessions/S0910A01/workspace/scripts/step96_source_receiver_decomposition.py",
    "Sessions/S0910A01/workspace/scripts/step96_kernel_plane_ab_map.py",
    "Sessions/S0910A01/workspace/notes/step95_gauge_obstruction_and_kernel_plane.md",
    "Sessions/S0910A01/workspace/notes/step89_correction_and_relative_green.md",
    "Sessions/S0910A02/workspace/notes/step93_ttcs_audit_of_kernel_plane_and_A01_step95.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 96 product-orbifold source-compatible kernel-plane reconstruction. Please read the files and give a mathematical memo on: (i) whether the Ozuch H^4 boundary source is correctly treated as a quadratic Sym^2(K) source rather than a scalar receiver adjoint; (ii) whether the scripts' conclusion that the Step89 odd adjoint identity holds for diagonal entries but fails for the off-diagonal/double-angle entry is consistent with the formulas; (iii) whether the AB-sector propagated map is a valid restricted sample and recovers the old K_adj only as one entry; (iv) what assumptions or missing components still prevent an obstruction/existence theorem. Do not decide the whole session; focus on correctness, source compatibility, and mathematical limitations of this Step 96 artifact.

## Output

## 数学核验备忘

### 总评

Step 96 的核心重构方向是正确的：Eguchi–Hanson 的 \(H^4(\zeta)\) 对插入参数 \(\zeta\) 是二次的，因此节点间响应天然是
\[
\operatorname{Sym}^2(K_{\rm src})\longrightarrow \operatorname{Sym}^2(K_{\rm rec})
\]
的线性映射，而不是一个由单个接收泛函决定的标量系数。它也正确撤回了 Step 95 中由一个相邻节点系数推导完整混合手性方程的论证。

但 `step96_source_receiver_decomposition.py` 对非对角项使用了**有序矩阵系数** \(S_{23}\)，没有先取 \((23,32)\) 对称部分。物理二次源只看到该对称部分。因此，“奇源的对角恒等式成立、非对角恒等式不成立”这一结论与 \(\operatorname{Sym}^2(K)\) 的实际极化不一致。这个问题不影响当前显示的 AB 秩一矩阵，因为该矩阵的两个非对角源列本来就是零；但它改变了 Step 96 对奇源双角分量的解释。

---

## 1. \(H^4\) 源确实是 \(\operatorname{Sym}^2(K)\) 源

Ozuch Proposition 1.16 给出
\[
H^4(\zeta^+)=-\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4}.
\]
由于 \(\rho_x(\zeta)\) 对 \(\zeta\) 线性，\(H^4(\zeta)\) 对 \(\zeta\) 二次，并且在 \(\zeta\mapsto-\zeta\) 下不变。

设
\[
V_2(x)=\frac12H_{ijpq}x_px_q,\qquad
C_{\zeta b}=\sum_a\zeta_aC_{ab}.
\]
利用
\[
\int_{\mathbb{RP}^3}x_rx_sx_px_q\,d\sigma
=\frac{\pi^2}{24}
\bigl(\delta_{rs}\delta_{pq}+\delta_{rp}\delta_{sq}+\delta_{rq}\delta_{sp}\bigr)
\]
以及 \(C_{ab}\) 无迹，可得
\[
3\int_{\mathbb{RP}^3}\langle H^4(\zeta^+),V_2\rangle
=-\frac{\pi^2}{16}
\sum_b(C_{\zeta b})_{ij}(C_{\zeta b})_{pq}H_{ijpq}.
\]
这正是脚本中的
\[
S^+(\zeta,\zeta)/\pi^2
=-\frac1{16}\sum_b(C_{\zeta b})_{ij}(C_{\zeta b})_{pq}H_{ijpq},
\]
而另一手性由 \(C_{b\zeta}\) 替换。系数 \(-1/16\)、\(V_2\) 中的 \(1/2\) 以及 \(\mathbb{RP}^3\) 体积因子彼此一致。

因此 Step 96 将标量 \(K_{\rm adj}\) 替换为二次源映射，是源公式本身要求的，而非仅仅一种更宽泛的参数化。

---

## 2. 非对角奇源比较少了一次对称化

脚本定义的有序系数是
\[
Q^+_{ac}(H)
=-\frac1{16}\sum_b
(C_{ab})_{ij}(C_{cb})_{pq}H_{ijpq}.
\]
一般 Hessian 只满足
\[
H_{ijpq}=H_{jipq}=H_{ijqp},
\]
并不满足 \(H_{ijpq}=H_{pqij}\)，所以 \(Q_{ac}\) 不必为对称矩阵。实际二次源为
\[
S^+_H(\zeta)=\zeta_a\zeta_cQ^+_{ac}(H)
=\zeta^T\frac{Q^++(Q^+)^T}{2}\zeta.
\]
故真正的 \(\operatorname{Sym}^2(K)\) 系数是
\[
\widehat Q^+_{ac}
=\frac12(Q^+_{ac}+Q^+_{ca}).
\]
特别地，双角项应使用
\[
\widehat Q_{23}=\frac12(Q_{23}+Q_{32}),
\]
而不是单独的 \(Q_{23}\)。

`step96_source_receiver_decomposition.py` 中

```python
ENTRIES = [(0,0), (1,1), (0,1)]
```

只读取 `source_matrix(...)[0,1]`，没有与 `[1,0]` 平均。数据文件本身已经显示这种非对称性：同一最坏基向量上，
\[
S_{\rm odd,23}/\pi^2=-0.125,\qquad
S_{\rm odd,32}/\pi^2=+0.125,
\]
而对应接收项为零。这一对数值在物理极化中恰好相消。

更结构化地，令
\[
F_H(\zeta)
=S_{\rm odd,H}(\zeta)/\pi^2-\frac12R_{\rm odd,H}(\zeta).
\]
Step 89 的恒等式对任意 Hessian 成立；乘积背景的节点等距群可以在保持乘积分解的同时把 \(K\) 中任意单位向量旋转到 \(e_2\)。因此
\[
F_H(\zeta)=0\qquad(\zeta\in K).
\]
两边都是 \(\zeta\) 的齐次二次式，极化后得到
\[
\boxed{\;
\widehat S_{\rm odd,ac}
=\frac12R_{\rm odd,ac},
\qquad a,c\in\{2,3\}.
\;}
\]
所以物理的奇源恒等式不只覆盖 \(22,33\)，也覆盖对称化后的 \(23\) 项。脚本报告的 \(1/\sqrt2\) 残量属于有序表示中的反对称冗余，不是 \(\operatorname{Sym}^2(K)\) 的额外双角源。

一个直接的复核量是
\[
\max_H\left|
\frac{S_{\rm odd,23}(H)+S_{\rm odd,32}(H)}2
-\frac12R_{\rm odd,23}(H)
\right|,
\]
按上述协变性应落在浮点舍入量级。

这并不使完整 \(H^4\) 源等于稀疏接收泛函的伴随。数据中的偶源对角项没有有序/对称化歧义，而
\[
S_{\rm even,22},\quad S_{\rm even,33}
\]
对全部接收项张成空间仍有明确非零残量，最大系数差达到 \(0.25\)。因此“单个奇接收泛函不能代表完整 plus/minus 源”仍然成立；需要修正的是把奇源的物理 \(23\) 项也列为额外残量。

此外，JSON 中的相对 \(L^2\) 数字依赖所选 100 个坐标基向量的缩放方式。精确为零与非零最大系数具有代数意义，而 \(0.7527\)、\(1/\sqrt2\) 不应解释为坐标无关的几何大小。

---

## 3. AB 扇区计算是有效的受限样本

脚本中的 AB 谱数据在乘积几何上相互一致：

1. 对单位二球上的一形式本征模，若 Hodge 本征值为
   \[
   \mu_\ell=\ell(\ell+1),
   \]
   则粗 Laplace 本征值为 \(\mu_\ell-1\)。交叉张量上的曲率作用为零，故
   \[
   P=\frac12(\mu_{\ell_A}+\mu_{\ell_B})-1,
   \]
   与代码一致，且最小值为 \(1\)，所以 AB 扇区没有零模投影问题。

2. 代码的交叉张量在覆盖空间上满足
   \[
   \|h\|^2=2\mu_{\ell_A}\mu_{\ell_B}.
   \]
   \(\mathbb Z_2\) 商使总体积减半，于是下降模在商空间上的范数为
   \[
   \mu_{\ell_A}\mu_{\ell_B},
   \]
   正好解释了代码中的 `norm_quot = muA*muB`。保留的 \(m=0,2\) 模在同步半转下下降到商空间；\(m=1\) 模虽可成对下降，但其相关一形式在极点的一阶导数为零，不贡献脚本所取的 AB 混合二阶 jet。

3. 原始手性矩阵中只有 plus/minus 与 minus/plus 块非零。取半和、半差后自然得到
   \[
   B_{\rm even,even}^{AB}=+a
   \begin{pmatrix}
   1&1&0\\
   1&1&0\\
   0&0&0
   \end{pmatrix},
   \quad
   B_{\rm odd,odd}^{AB}=-a
   \begin{pmatrix}
   1&1&0\\
   1&1&0\\
   0&0&0
   \end{pmatrix}.
   \]
   这表示
   \[
   M\longmapsto a\,\operatorname{tr}(M)\,I_K,
   \]
   即 AB 扇区只传播源的标量二次分量，不传播双角分量。

4. 因而旧数值确实只是
   \[
   K_{\rm adj}^{AB}
   =
   \bigl[B_{\rm odd,odd}^{AB}\bigr]_
   {R_{22}\leftarrow\zeta_2^2}
   =-0.03144249732
   \]
   这一项。相同矩阵中还同时存在
   \(R_{22}\leftarrow\zeta_3^2\)、
   \(R_{33}\leftarrow\zeta_2^2\)、
   \(R_{33}\leftarrow\zeta_3^2\)，所以旧标量不能确定完整响应。

非对角源未对称化的问题在当前显示矩阵中不改变数值，因为所有 \(23\) 源列和 \(R_{23}\) 输出行都是零。热正则阶梯在四组 \((\tau,L_{\max})\) 上稳定到显示精度，且固定 \(\tau\) 的尾壳极小；这提供了很强的数值复现性。不过文件没有区间算术或 \(\tau\downarrow0\) 的显式误差估计，因此非零常数目前仍是高稳定度数值结果，而非解析非零证明。

---

## 4. 尚未纳入定理推导的数学项

1. **AA/BB 及其完整 jet。** 偶源对角残量已经证明 AB 接收项不能代表全部源。AA、BB、标量、迹自由张量以及可能与规范分解耦合的模式均须进入同一谱逆。

2. **自节点有限部分。** 当前脚本只计算分离节点 NS、SN、SS。自节点处的二阶点源与二阶接收同时作用，需采用与 Ozuch 构造一致的匹配延拓和有限部分；不能由异节点热核直接替代。

3. **全局投影与形变。** AB 扇区因 \(P\ge1\) 而无需额外投影，但其他扇区含 \(Pq=-q\) 的平行形状模，也可能含全局核及 orbifold Einstein 形变。Ozuch Proposition 2.10 中的 \(\nu_l\) 方程和正交归一化需要一起处理。

4. **节点框架运输。** 四个节点的 \(K_j\) 基、南极取向、两种手性及节点置换尚未组成显式运输矩阵。当前 NS 与 SN 数值相同是在脚本局部框架约定中得到的，尚不能直接作为完整行方程中的同号项相加。

5. **同阶局部项。** 接收投影线、框架、图坐标、补空间解、非线性修正及自节点正规项都会改变三阶投影系数。已知 Kähler–Einstein 配置只约束这些项的完整总和，不能推出某个相邻偶块等于某个相邻奇块的相反数。

6. **其余 Ozuch 方程。** \(\mu_1\) 可由行列式公式分析，但 \(\mu_2,\mu_3\)、全部 \(\nu_l\) 以及可能的 orbifold 形变变量尚未形成闭合有限维系统。

7. **误差阶。** 异节点响应在径向方程中为 \(t_jt_i^2\)，等尺度时是 \(t^3\)。Ozuch Proposition 2.19 当前给出的误差为 \(O(t_{\max}^{5/2})\)，其量级大于 \(t^3\)。需要形如
   \[
   \Pi_{K_j}\mathfrak F_j=t^3\mathcal C_j+o(t^3)
   \]
   的展开，或明确写出可能的 \(t^3\log t\) 项。Ozuch §3.3 的 Proposition 3.14 与 Corollary 3.25 提供了可参照的高阶构造模板，但尚未被移植到这一乘积背景。

8. **局部残量的分布属性。** 100 维 jet 线性代数说明两个局部泛函不同，却没有单独证明其差对应哪一种规范固定的点分布，也没有证明该差在投影谱空间中必然产生非零接收响应。“TT 残量”这一措辞需要分布延拓、Bianchi 恒等式及全局投影公式支持。

### 结论

Step 96 成功把研究对象从单个 \(K_{\rm adj}\) 改写为源相容的有限维映射，并给出了可信的 AB 扇区样本。最重要的修正是：`Sodd_23` 的残量来自未对称化的有序系数；物理极化后的奇源 \(23\) 项仍满足 Step 89 的半倍接收恒等式。完整 plus/minus 源仍含接收泛函张成空间之外的偶源成分，因此 Step 95 的混合手性推导依然不能恢复。当前 AB 数值适合作为完整计算的校准项，而不是完整节点方程。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 96,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step96_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step96_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 96 product-orbifold source-compatible kernel-plane reconstruction. Please read the files and give a mathematical memo on: (i) whether the Ozuch H^4 boundary source is correctly treated as a quadratic Sym^2(K) source rather than a scalar receiver adjoint; (ii) whether the scripts' conclusion that the Step89 odd adjoint identity holds for diagonal entries but fails for the off-diagonal/double-angle entry is consistent with the formulas; (iii) whether the AB-sector propagated map is a valid restricted sample and recovers the old K_adj only as one entry; (iv) what assumptions or missing components still prevent an obstruction/existence theorem. Do not decide the whole session; focus on correctness, source compatibility, and mathematical limitations of this Step 96 artifact.

## Integrated Scientific Memo

# Step 96 数学核验备忘

## 结论摘要

Step 96 的主要结构修正是正确的：Ozuch 的 \(H^4(\zeta)\) 是关于插入方向 \(\zeta\) 的二次源，因此节点间对象应是
\[
\operatorname{Sym}^2(K_i)\longrightarrow \operatorname{Sym}^2(K_j),
\qquad K_j=\ker R^{\epsilon_j},
\]
而不是单个标量 \(K_{\rm adj}\)。

但 Step 96 关于奇源非对角项的结论有一个实质性错误：脚本比较的是有序矩阵系数 \(S_{23}\)，未取物理二次型所需的 \((23,32)\) 对称部分。数据自身显示该“残量”在对称化后抵消。因此正确结论是：

\[
S_{\rm odd}|_{\operatorname{Sym}^2(K)}
   =\frac12R_{\rm odd}|_{\operatorname{Sym}^2(K)}
\]
不仅对 \(22,33\) 成立，也对物理的双角 \(23\) 分量成立。完整的 plus/minus 源仍不等于稀疏接收泛函的伴随，因为偶源部分具有明确非零残量；所以 Step 95 的标量障碍论证仍然必须撤回。

AB 扇区计算是可信的受限样本，并且旧 \(K_{\rm adj}^{AB}\) 确实只是矩阵的一项，而非完整物理映射。

---

## 1. \(H^4\) 必须作为二次 \(\operatorname{Sym}^2(K)\) 源处理

Ozuch Proposition 1.16 给出
\[
H^4(\zeta^+)
=-\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4}.
\]
其中 \(\rho_x(\zeta)\) 与 \(\zeta^+\) 都线性依赖 \(\zeta\)，故 \(H^4\) 对 \(\zeta\) 是齐次二次的，并在 \(\zeta\mapsto-\zeta\) 下不变。对
\[
V_2(x)=\frac12H_{ijpq}x_px_q
\]
的边界配对因此具有形式
\[
\frac{S^+_H(\zeta)}{\pi^2}
=-\frac1{16}\sum_b
 (C_{\zeta b})_{ij}(C_{\zeta b})_{pq}H_{ijpq},
\]
负手性则使用 \(C_{b\zeta}\)。这与脚本的 `SCOEFF` 定义及 Step 89 的 \(H\)-相对-\(V_2\) 因子一致。

所以正确的源不是“接收标量的伴随”，而是一个关于源方向的二次泛函；极化后属于 \(\operatorname{Sym}^2(K_i)^*\)。接收端第一障碍同样读出 \(K_j\) 上的二次曲率块，故节点间有限维对象是
\[
B_{ji}\in
\operatorname{Hom}\!\left(\operatorname{Sym}^2(K_i),
                           \operatorname{Sym}^2(K_j)\right).
\]

这一点也符合 Ozuch Proposition 2.10 的角色：边界配对给出全局核投影及构造 \(\bar h^4\) 的源数据，并不直接等于某个标量接收系数。真正的节点块还需经过全局投影求解并在接收节点取正规二阶 jet。

---

## 2. 奇源非对角“失败”是未对称化伪影

### 2.1 脚本实际计算了什么

脚本定义有序系数
\[
Q^+_{ac}(H)
=-\frac1{16}\sum_b
(C_{ab})_{ij}(C_{cb})_{pq}H_{ijpq}.
\]
一般 Hessian 只满足
\[
H_{ijpq}=H_{jipq}=H_{ijqp},
\]
不必满足 \(H_{ijpq}=H_{pqij}\)，因此作为数组的 \(Q_{ac}\) 不必对称。

但物理源是
\[
S_H(\zeta)=\sum_{a,c}\zeta_a\zeta_cQ_{ac}(H),
\]
它只依赖
\[
\widehat Q_{ac}
=\frac12(Q_{ac}+Q_{ca}).
\]
因此物理双角系数应当比较
\[
\widehat S_{\rm odd,23}
=\frac12\bigl(S_{\rm odd,23}+S_{\rm odd,32}\bigr),
\]
而不是单独的 `source_matrix[0,1]`。

`step96_source_receiver_decomposition.py` 的

```python
ENTRIES = [(0,0), (1,1), (0,1)]
```

只抽取 \(23\) 有序项，没有与 \(32\) 平均。

### 2.2 数据已经暴露了该问题

`step96_kernel_plane_ab_map.json` 对同一最坏 Hessian 基向量记录
\[
S_{\rm odd,23}/\pi^2=-0.125,\qquad
S_{\rm odd,32}/\pi^2=+0.125,
\]
而接收项为零。因此产生“最大误差 \(0.125\)”的部分在物理对称化后恰好抵消。

更一般地，Step 89 的恒等式对任意选定的单位插入方向成立；乘积节点的稳定子在 \(K=\operatorname{span}\{e_2,e_3\}\) 上旋转。故对任意 \(\zeta\in K\)，
\[
\frac{S_{\rm odd,H}(\zeta)}{\pi^2}
=\frac12R_{\rm odd,H}(\zeta).
\]
两边都是 \(\zeta\) 的齐次二次多项式，极化给出
\[
\boxed{
\widehat S_{\rm odd,ac}
=\frac12R_{\rm odd,ac},
\qquad a,c\in\{2,3\}.
}
\]

因此：

- \(22\)、\(33\) 恒等式正确；
- “物理 \(23\)/double-angle 奇源恒等式失败”不正确；
- JSON 中该项的 \(1/\sqrt2\) 残量来自有序表示的反对称冗余，不属于 \(\operatorname{Sym}^2(K)\)。

应直接修改脚本，检查
\[
\max_H\left|
\frac{S_{\rm odd,23}(H)+S_{\rm odd,32}(H)}2
-\frac12R_{\rm odd,23}(H)
\right|,
\]
预期仅为浮点误差。

### 2.3 这并不恢复 Step 95 的标量模型

完整 H\(^4\) 源仍不能化为稀疏奇接收泛函的伴随。特别是 \(22,33\) 偶源没有上述有序/对称化歧义，而数据给出相对于全部简单接收项张成空间的明显非零残量：
\[
\|T_{\rm even,22}\|/\|S_{\rm even,22}\|
\approx0.75277,
\]
且最大坐标残量为 \(0.25\)；\(33\) 同样如此。单独 plus/minus 源也有较大残量。

所以正确的分解应是：

- 奇源在物理 \(\operatorname{Sym}^2(K)\) 上满足 Step 89 型伴随恒等式；
- 偶源及单独手性源包含额外成分 \(T\)；
- gauge 恒等式
  \[
  R_{\rm odd}(\mathcal L_Xg_0)=0
  \]
  只保证奇接收值对平滑纯规范变化不变，不能消去这些额外物理源。

此外，JSON 中的相对 \(L^2\) 数值依赖所选 100 个坐标基的缩放；“精确为零/非零”和最大坐标残量有直接代数意义，但 \(0.75277\)、\(1/\sqrt2\) 不应视为坐标不变量。

---

## 3. AB 扇区是有效的受限样本

该计算在其声明范围内是自洽的。

对二球一形式模，若 Hodge 本征值为
\[
\mu_\ell=\ell(\ell+1),
\]
则 AB 交叉张量上的算子本征值采用
\[
P=\frac12(\mu_{\ell_A}+\mu_{\ell_B})-1.
\]
由于 \(\ell_A,\ell_B\ge1\)，有 \(P\ge1\)，所以 AB 扇区没有零模逆问题；平行形状张量 \(q=g_A-g_B\) 属于同因子张量扇区，也不在这里。

计算得到相邻节点
\[
B^{AB}_{\rm even,even}
=+a
\begin{pmatrix}
1&1&0\\
1&1&0\\
0&0&0
\end{pmatrix},
\qquad
B^{AB}_{\rm odd,odd}
=-a
\begin{pmatrix}
1&1&0\\
1&1&0\\
0&0&0
\end{pmatrix},
\]
其中
\[
a=0.03144249732,
\]
混合 even–odd 块为零。这个矩阵表示
\[
M\longmapsto a\,\operatorname{tr}(M)\,I_K
\]
（奇奇块多一个负号）：AB 扇区只传播源的标量部分，既无 \(R_{23}\) 输出，也不响应无迹双角源。

旧值
\[
K_{\rm adj}^{AB}=-0.03144249732
\]
恰好是
\[
B^{AB}_{\rm odd,odd}
(R_{22}\leftarrow\zeta_2^2)
\]
这一项。同一矩阵还有另外三个相等的对角源—接收项，因此旧 \(K_{\rm adj}\) 不能代表完整映射。

当前未对称化错误不改变已显示的 AB 矩阵，因为其 \(23\) 源列和 \(R_{23}\) 行本来全为零。需要注意脚本中 \(23\) 列是矩阵元素 \(M_{23}\)，实际评价二次型时要乘 \(2\zeta_2\zeta_3\)。

热阶梯在各 \((\tau,L_{\max})\) 下稳定至所示精度，说明谱截断可靠；但文件没有给出区间误差或严格的 \(\tau\downarrow0\) 极限证明，所以数值非零性仍是高可信数值结论，而非解析定理。

---

## 4. 尚不足以推出障碍或存在性的原因

1. **完整谱扇区缺失。**  
   尚未计算 AA/BB、迹自由张量及其他同因子扇区。AB 的秩一结构不能外推到完整 Green 响应；偶源残量很可能正通过这些扇区传播。

2. **真正的全局节点块尚未构造。**  
   必须固定延拓、Bianchi slice、核投影和正规化，求解全局
   \[
   P_{g_o}\bar h_i^4=\text{源}+\text{核投影},
   \]
   然后在节点 \(j\) 抽取正规二阶 jet。局部边界配对或受限谱和本身不等于完整 \(Q_{ji}\)。

3. **自节点有限部分缺失。**  
   当前仅有分离节点 NS、SN、SS。自节点 quadrupole—receiver 配对是奇异的，需要与 Ozuch 匹配构造一致的有限部分，不能由异节点热核替代。

4. **节点框架运输尚未明确。**  
   四节点、南北极取向、两种手性及节点置换之间的
   \[
   U_{ji}:K_i\to K_j
   \]
   尚未显式建立。局部框架中 NS 与 SN 数值相同，不自动意味着它们在全局行方程中同号相加。

5. **投影和框架会在同阶移动。**  
   正规 jet 会改变秩一像线及 \(K_j\) 投影；这些修正与目标三阶系数同阶，不能事后忽略。

6. **有限维方程尚未闭合。**  
   仍需处理 \(\mu_2,\mu_3\)、全部 \(\nu_l\)、orbifold Einstein 形变 \(v_2\)，以及 complement solution、chart、非线性和自节点项。已知全同手性 Kähler–Einstein 配置只校准完整总和，不能推出某个相邻偶块等于某个奇块的负值。

7. **误差阶尚不够。**  
   异节点项在等尺度时为
   \[
   t_jt_i^2=O(t^3),
   \]
   而 Ozuch Proposition 2.19 的现有必要估计仅有
   \[
   O(t_{\max}^{5/2}),
   \]
   后者大于 \(t^3\)。因此即使算出非零三阶系数，也不能据此排除解。需要
   \[
   \Pi_{K_j}\mathfrak F_j
   =t^3\mathcal C_j+o(t^3),
   \]
   或显式纳入 \(t^3\log t\) 项。Ozuch §3.3 的高阶 jet 构造提供模板，但必须针对正曲率乘积背景重新建立。

8. **“残量是 TT 分布”的措辞尚未证明。**  
   jet 空间中两个泛函不相等，只证明存在局部代数残量。要称其为规范固定的 TT 点分布，并断言其投影传播非零，还需分布延拓、Bianchi 恒等式及全局投影证明。

## 最终判断

Step 96 正确完成了最重要的概念修正：研究对象是源相容的
\[
\operatorname{Sym}^2(K_i)\to\operatorname{Sym}^2(K_j)
\]
映射，AB 结果只是其中一个受限校准块，旧 \(K_{\rm adj}^{AB}\) 只是一个矩阵元素。

必须修正的地方是：奇源 \(23\) 项的所谓失败来自遗漏 \((23,32)\) 对称化。物理 \(\operatorname{Sym}^2(K)\) 上的奇源恒等式应覆盖整个 \(22,33,23\) 块。尽管如此，偶源及单独手性源的真实残量仍足以否定 Step 95 的标量伴随模型。当前材料既未给出完整障碍，也未给出存在性结论。
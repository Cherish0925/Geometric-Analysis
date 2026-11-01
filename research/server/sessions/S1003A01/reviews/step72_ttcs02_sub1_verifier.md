# TTCS Independent Branch Record

```json
{
  "step_id": 72,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step72_H2_curvature_factorization.md",
    "Sessions/S1003A01/workspace/notes/step71_flat_exactness_and_fibre_structure.md",
    "Sessions/S1003A01/workspace/scripts/step72_vary_H2_free.py",
    "Sessions/S1003A01/workspace/scripts/step72_lift_quotient.py",
    "Sessions/S1003A01/workspace/scripts/step72_curvature_identification.py",
    "Sessions/S1003A01/workspace/data/step72/vary_H2_free_K6.json",
    "Sessions/S1003A01/workspace/data/step72/vary_H2_free_K8.json",
    "Sessions/S1003A01/workspace/data/step72/lift_quotient_K6.json",
    "Sessions/S1003A01/workspace/data/step72/lift_quotient_K8.json",
    "Sessions/S1003A01/workspace/data/step72/curvature_identification.json"
  ]
}
```

## Task

Verify the final Step-72 local conclusion after the correction-independent lift quotient was computed. Read the note, all three central scripts, and outputs. Check: (1) the identification of ker(dE0,dN1)/quartic-Hamiltonian gauge with the five-dimensional W^-(0) block; (2) the linear-algebra statement that a chosen W^- lift changes P_K(E_K), but its class modulo J_h ker A_h vanishes at K=6 and K=8 because B has full target rank; (3) whether the explicit radial conclusions and cancellation norms are interpreted correctly; (4) why the attempted fixing of coordinate N3,N5,N7 does not yet define covariant fixed torsion, and what its nonzero residual actually establishes; and (5) whether the revised note withdraws all stronger unsupported Step-71 inferences. Give a concise theorem-quality formulation, name any remaining computational flaw or normalization issue, and distinguish exact structural facts from floating evidence.

## Output

# 科学核验备忘录

## 一、定理式表述

固定所给的 \(\lambda=-5\)、gen5 偶次 Darboux 喷流，并使用脚本中的系数欧氏内积。令  
\[
V_2=\{\text{二次 anti-}J\text{ 度量系数}\},\qquad \dim V_2=6\binom53=60,
\]
\[
A_2=(dE_0,dN_1)|_{V_2},\qquad \mathcal G_2=\{\text{四次 Hamiltonian 生成的二次度量变化}\}.
\]
对 \(K=6,8\)，再写
\[
A=[A_p\ A_h]=d(E_0,E_2,\ldots,E_{K-2}),\qquad
J=[J_p\ J_h]=P_KdE_K,
\]
其中 \(p=H_2\)，\(h=(H_4,\ldots,H_K)\)。

**有限喷流命题。** 若采用输出中给出的秩等式，则：

1.  
   \[
   \dim \ker A_2=40,\qquad \dim\mathcal G_2=35,\qquad
   \dim(\ker A_2/\mathcal G_2)=5.
   \]
   在脚本规定的标准定向下，线性化曲率映射在该商空间上满足
   \[
   \bar{\mathcal R}_+=0,\qquad
   \bar{\mathcal R}_-:
   \ker A_2/\mathcal G_2\longrightarrow S^2_0(\Lambda^-)
   \]
   为同构。因此这五个方向正是 \(W^-(0)\) 的五个分量。

2. 对任一五维基 \(X\) 及任一满足
   \[
   A_hH_0=-A_pX
   \]
   的提升，所有其他提升为 \(H_0+N_hC\)，其中
   \[
   N_h=\ker A_h.
   \]
   相应的下一阶标量响应
   \[
   Y=J_pX+J_hH_0
   \]
   只确定商类
   \[
   [Y]\in \mathcal P_K/\operatorname{im}(J_hN_h).
   \]
   输出给出
   \[
   \operatorname{rank}(J_hN_h)=\dim\mathcal P_K
   =
   \begin{cases}
   35,&K=6,\\
   84,&K=8.
   \end{cases}
   \]
   因而该商空间为零，五个 \(W^-\) 方向在这两阶均没有产生与提升选择无关的标量兼容类。

3. 对径向泛函 \(\ell_K\) 同样有
   \[
   \ell_K^T[Y]=0
   \quad\text{于}\quad
   \mathcal P_K/\operatorname{im}(J_hN_h).
   \]
   所以所选最小系数范数提升的径向响应并非 \(W^-\) 的内禀响应。

这是一个**一阶、有限阶、固定数值基点**的陈述；它本身不提供非线性解族、全阶形式解或收敛形式喷流。

---

## 二、五维商空间与 \(W^-\) 的识别

### 结构上成立的部分

四次齐次 Hamiltonian 的空间维数为 \(\binom73=35\)。其 Hamiltonian 向量场为三次，作用在平坦零阶度量上产生二次纯坐标变化。若该度量变化为零，则相应三次向量场是 Euclidean Killing 场；齐次三次 Killing 场只能为零，因此该映射为单射，故 \(\dim\mathcal G_2=35\)。

由张量自然性，四次 Hamiltonian 拉回不改变当前所考察的 \(E_0\) 和 \(N_1\) 系数；线性化平坦曲率也在这些纯坐标方向上为零。因此
\[
\mathcal G_2\subseteq\ker A_2,\qquad
\mathcal R_\pm|_{\mathcal G_2}=0
\]
具有明确的几何来源。输出中的
\[
\|A_2G_2\|=7.99\times10^{-15},
\]
以及两种曲率块在 \(G_2\) 上约 \(10^{-15}\) 的范数，与这些恒等式一致。

### 浮点运算给出的部分

脚本以相对阈值提取
\[
\operatorname{rank}A_2=20,\qquad \dim\ker A_2=40.
\]
将 \(\ker A_2\) 正交投影到 \(\mathcal G_2^\perp\) 后，奇异值为五个 \(1+O(10^{-14})\)，其余约 \(2.2\times10^{-15}\)。这非常清楚地支持五维商空间。

在该五维空间上：

- \(W^+\) 块范数为 \(1.61\times10^{-15}\)；
- \(W^-\) 块的五个奇异值为
  \[
  1.9365,\ 1.9365,\ 1.8974,\ 1.6733,\ 1.6330.
  \]

因此数值矩阵确实给出 \(Q\simeq S^2_0(\Lambda^-)\)。定向约定也一致：脚本使用
\[
\Lambda^\pm=\operatorname{span}\{e^{01}\pm e^{23},
e^{02}\pm e^{31},e^{03}\pm e^{12}\}.
\]

不过，现有文件没有给出符号矩阵、非零子式或完整的 \(U(2)\)-模分解证明。因此“数值上识别为 \(W^-\)”有充分依据；“表示论上已经严格证明”尚缺一段明确材料。严格证书可以是 \(A_2\)、Hamiltonian 映射与曲率映射的精确矩阵秩，或证明商空间是唯一的五维不可约模并验证 \(\mathcal R_-\) 非零。

---

## 三、提升商与径向分量

所用商构造在数学上完全正确。只要 \(A_hH_0=-A_pX\) 可解，提升集合就是
\[
H_0+\ker A_h,
\]
而 \(J\) 的变化正是
\[
Y+\operatorname{im}(J_h\ker A_h).
\]
因此 \(B=J_hN_h\) 满行秩立即推出商类为零；此时 \([B,Y]\) 的联合秩不再提供额外信息。

数值结果为：

| 数量 | \(K=6\) | \(K=8\) |
|---|---:|---:|
| \(\dim\ker A_h\) | 361 | 735 |
| \(\operatorname{rank}B\) | 35/35 | 84/84 |
| 报告的最小 \(B\) 奇异值 | \(0.2515\) | \(0.004984\) |
| \(\|(I-\Pi_B)Y\|\) | \(8.05\times10^{-11}\) | \(4.18\times10^{-10}\) |
| \(\|\ell^TB\|\) | \(7.2487\) | \(0.92593\) |
| \(\|\ell^TY\|\) | \(165.576\) | \(522.637\) |
| \(\|\ell^T(I-\Pi_B)Y\|\) | \(1.59\times10^{-12}\) | \(2.01\times10^{-11}\) |
| \(\|Y+BC\|\) | \(1.83\times10^{-11}\) | \(5.31\times10^{-9}\) |

所选最小范数提升的 \(Y\) 在五维空间上确有秩五，奇异值分别为给出的 \(2.3\times10^3\!-\!5.8\times10^3\) 和 \(4.2\times10^4\!-\!2.1\times10^5\)。这说明该特定截面强烈响应于 \(W^-\)，但满秩 \(B\) 又说明整个响应都能由固定 \(H_2\) 的高阶修正改变。Step 72 对这一点的解释是正确的。

径向向量的公式也正确：若 \(K-2=2m\)，则
\[
\Delta^m x^\alpha\big|_0
=
m!\prod_i\frac{\alpha_i!}{(\alpha_i/2)!}
\]
当所有 \(\alpha_i\) 为偶数，否则为零。脚本随后把该系数向量归一为单位欧氏范数。因此径向零商类有意义，而 \(165.6\)、\(522.6\) 等数值依赖系数基、单位范数约定和 `P_matrix/2` 的整体因子，并不是几何常数。

一个具体的数值缺口是：`Nh` 由截断 SVD 构造，但输出没有记录
\[
\|A_hN_h\|,\qquad \|A_hN_hC\|.
\]
特别是 \(K=8\) 的消去修正范数为 \(8.14\times10^4\)，可能放大数值零空间中的残余。故“\(B\) 满秩，所以抽象商为零”是当前最强的结果；显式修正同时保持低阶方程的精度，还需要上述两个量。另一个相关现象是 Step 71 给出 \(K=8\) 的相关核维数 \(736\)，而 Step 72 给出 \(735\)，很可能来自 \(10^{-8}\) 与 \(10^{-10}\) 相对阈值之间的一条小奇异方向。当前 JSON 没有保存 \(A_h\) 截断处的奇异值。

---

## 四、固定 \(N_3,N_5,N_7\) 的含义

这些是固定 Darboux 坐标中的 Taylor 系数，不是 Hamiltonian 拉回下的协变喷流。

若四次 Hamiltonian 产生三次向量场 \(X_3\)，则
\[
\delta N=\mathcal L_{X_3}N.
\]
当
\[
N=N_1+N_3+\cdots
\]
时，三次项包含
\[
(\mathcal L_{X_3}N_1)_3.
\]
同时
\[
\delta g_2=\mathcal L_{X_3}g_0,\qquad
\delta g_4\supset \mathcal L_{X_3}g_2,
\]
而 \(g=\exp H\) 的参数化还会把这些作用耦合到更高 \(H_d\)。因此一个真实 Hamiltonian 拉回会同时改变 \(H_2,H_4,\ldots\) 与 \(N_3,N_5,\ldots\)；逐项要求坐标系数 \(dN_q=0\) 会排除几何上等价的变化。

协变对象应由 \(\nabla^rN\) 及其随度量连接的变化构成，并同时除去真实 Hamiltonian 拉回产生的 Lie 导数。现有增广矩阵没有实现这一对象。

关于非零残余：

- \(K=6\) 的增广最小二乘残余为
  \[
  47.8135,\qquad
  \frac{47.8135}{12870.46}=3.715\times10^{-3},
  \]
  而不加坐标 \(N_q\) 条件时残余约 \(10^{-11}\)。这支持如下具体事实：在当前坐标、当前方程权重和当前五列 \(X\) 下，低阶 Einstein 线性方程与全部 \(dN_3=dN_5=0\) 不能同时达到数值精度。

- 该 Frobenius 残余是五列合并量，没有给出残余矩阵的五个奇异值。因此它至少表明某个 \(W^-\) 组合不能如此延拓，但尚不能据此说每个非零 \(W^-\) 方向都必然改变这些坐标系数。

- \(K=8\) 只记录绝对残余 \(9301.93\)。所给 JSON 缺少当前脚本本应写出的 `rhs_norm` 和相对残余，且 Einstein 行与 Nijenhuis 行没有做协变尺度平衡。因此该数字显示明显的不相容迹象，却不能量化其条件状态。

由于增广仿射方程本身没有被精确满足，该分支随后得到的 \(4.26\times10^{14}\)、\(4.35\times10^{16}\) 修正范数确实不承载数学含义。Step 72 对这两个巨大数值的处理是正确的。

---

## 五、Step 71 推论的撤回情况与文件一致性

修订文本已经明确撤回以下较强解释：

- 径向层级是唯一可能的局部—整体载体；
- 径向行只依赖扭率而与 \(W^-\) 无关；
- 所选提升的非零径向响应定义了内禀 \(W^-\!\to\)兼容映射；
- 固定坐标 Nijenhuis 系数刻画了完整的协变扭率纤维。

Step 72 §4 明确指出前两种相反解释都把一个所选截面误当成提升商；§6 也恢复了 \(W^-\) 经由连接、谐投影和 ASD Weitzenböck 方程进入整体输运的作用。Step 71 文件自身也已把 §7.1–§7.4 标成受固定 \(H_2\) 与坐标条件影响的历史计算。

仍需精确阅读两处措辞：

1. “物理 \(H_2\) 方向迫使高阶坐标扭率变化”目前只由合并残余支持；现有输出没有证明五维空间中每个非零方向都有此性质。
2. “非退化 \(+1\) 零点在所测阶局部可行”应理解为：在这一个 \(\lambda=-5\)、gen5 数值基点，至 \(K=8\) 的线性化标量行可由高阶修正覆盖。它并不等同于任意非退化一阶喷流的结论，也不产生非线性或全阶形式解。

另有轻微文件版本差异：Step 72 正文在 \(K=6\) 写出 \(8.55\times10^{-11}\)、\(5.93\times10^{-11}\)、\(1.81\times10^{-12}\)、\(1.52\times10^{-11}\)，而当前 JSON 分别为 \(8.045\times10^{-11}\)、\(5.315\times10^{-11}\)、\(1.592\times10^{-12}\)、\(1.826\times10^{-11}\)。这些差异不改变秩与商空间结论，但正文应与选定的数据文件同步。

**总评：** 修正后的核心线性代数结论正确：所选 \(W^-\) 提升会显著改变 \(P_K(E_K)\)，但在 \(K=6,8\) 时，固定 \(H_2\) 的高阶低方程核已映满整个标量目标，所以没有留下提升无关的径向或非径向兼容类。其严格数学地位目前是由双精度秩计算强力支持的有限喷流命题；精确秩证书、数值零空间残余以及协变扭率喷流仍是尚缺的证明材料。
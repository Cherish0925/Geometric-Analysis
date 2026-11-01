# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 52,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step52_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step52_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 52 holomorphic Lefschetz computation and interpretation for BCGP product-quotient rows in the Yau 26 session. Please read the script, data, source excerpts, Step 51 proof note, and Step 52 note. Check: (i) the Lefschetz trace formulas and fixed-point/multiplier reconstruction from branch stabilizers; (ii) whether the tensor-character average correctly computes H^0(C1,2K)⊗H^0(C2,K) plus H^0(C1,K)⊗H^0(C2,2K) invariants; (iii) whether the numerical conclusions d=0 only for the K^2=2 Z4^2 row among the scanned BCGP rows are plausible from the supplied data; (iv) whether the interpretation is appropriately limited: d=0 supplies a sufficient global Q-Gorenstein smoothing route via Step 51, while d>0 is not a no-smoothing/no-Einstein theorem. Identify any load-bearing errors, convention risks, or source-assumption gaps that should be repaired before this result is used.

## Integrated Scientific Memo

# Step 52 核验结论

## 总结

Step 52 的核心数学方法是正确的：

\[
d=\dim H^0(C_1\times C_2,\Omega_Y^1\otimes K_Y)^G
\]

确实由脚本中的 holomorphic Lefschetz 迹和张量特征标平均计算；结合 Step 51 的反身层桥梁，它等于

\[
\dim H^2(X,T_X^0).
\]

在所实际扫描的 20 个条目中，即 §6.7 与 §6.9–§6.27，现有数据可信地支持：

\[
d=0
\quad\Longleftrightarrow\quad
\text{BCGP §6.7， }K^2=2,\ G=\mathbb Z_4^2.
\]

但必须把结论限定为“在所扫描条目中”。其余 \(K^2=2\) 条目 §6.1–§6.6、§6.8 并未扫描，因此不能写成“全部 BCGP rows 中唯一”。

没有发现破坏 §6.7 的 \(d=0\) 结论或张量平均方法的承重性错误。正式使用前主要需补强：分支系统验证、非阿贝尔局部旋转数约定、精确 cyclotomic 运算，以及 Lee–Park 定理原文依赖。

---

## 1. Lefschetz 公式

设 \(u\ne1\) 是曲线 \(C\) 的有限阶自同构，\(\lambda_p\) 是其在固定点 \(p\) 处的切向乘子。Holomorphic Lefschetz 公式给出

\[
\sum_q(-1)^q\operatorname{Tr}\bigl(u\mid H^q(C,L)\bigr)
=
\sum_{p\in\operatorname{Fix}(u)}
\frac{\operatorname{Tr}(u\mid L_p)}{1-\lambda_p}.
\]

取 \(L=K_C\) 时，纤维作用为 \(\lambda_p\)，且

\[
H^1(C,K_C)\cong H^0(C,\mathcal O_C)^\vee
\]

上的迹为 \(1\)，故

\[
\operatorname{Tr}(u\mid H^0(C,K_C))
=
1+\sum_p\frac{\lambda_p}{1-\lambda_p}.
\]

取 \(L=2K_C\) 时，纤维作用为 \(\lambda_p^2\)，而 \(H^1(C,2K_C)=0\)，故

\[
\operatorname{Tr}(u\mid H^0(C,2K_C))
=
\sum_p\frac{\lambda_p^2}{1-\lambda_p}.
\]

恒等元处

\[
\chi_K(1)=g,\qquad \chi_{2K}(1)=3g-3.
\]

脚本中的公式完全正确。一个敏感检验是 genus-\(g\) 超椭圆对合：它有 \(2g+2\) 个固定点且 \(\lambda=-1\)，上式给出

\[
1+(2g+2)\frac{-1}{2}=-g,
\]

正好对应其在 \(H^0(K)\) 上的 \(-1\) 作用。

---

## 2. 从分支稳定子重建固定点和乘子

对正则 \(G\)-覆盖 \(C\to\mathbb P^1\)，第 \(i\) 个分支点的惯性群为

\[
H_i=\langle e_i\rangle,\qquad |e_i|=r_i.
\]

该分支点上方的点由左陪集 \(aH_i\) 参数化，其稳定子为

\[
aH_i a^{-1}.
\]

因此 \(u\) 固定 \(aH_i\) 当且仅当

\[
a^{-1}ua=e_i^k\ne1.
\]

若生成元 \(e_i\) 的局部作用取为 \(\zeta_{r_i}\)，则此固定点处 \(u\) 的乘子为

\[
\lambda=\zeta_{r_i}^k.
\]

脚本依次通过：

- `left_coset_reps(H)` 枚举 \(aH\)；
- `conjugate_by(a,u)` 计算 \(a^{-1}ua\)；
- `power_index` 恢复指数 \(k\)；

正确实现了这一计数。重复出现的分支元素代表不同的分支值，因而应重复计数，脚本亦如此。

把所有局部生成元的取向同时反转，会将特征标变成

\[
\chi(u)\longmapsto \chi(u^{-1}).
\]

由于群平均可作变量替换 \(u\mapsto u^{-1}\)，总不变量维数不变。因此 `tangent_sign=-1` 检验是正确的一致性检验，但不是独立复算。尤其，它不能检测比全局取逆更一般的局部旋转数误配。

---

## 3. 张量特征标平均

Step 51 的 Künneth 分解为

\[
H^0(Y,\Omega_Y^1\otimes K_Y)
=
H^0(2K_{C_1})\otimes H^0(K_{C_2})
\oplus
H^0(K_{C_1})\otimes H^0(2K_{C_2}).
\]

对有限群表示 \(V\)，

\[
\dim V^G=\frac1{|G|}\sum_{u\in G}\chi_V(u),
\]

而

\[
\chi_{A\otimes B}(u)=\chi_A(u)\chi_B(u).
\]

故脚本计算的

\[
\frac1{|G|}\sum_{u\in G}
\left[
\chi_{2K,C_1}(u)\chi_{K,C_2}(u)
+
\chi_{K,C_1}(u)\chi_{2K,C_2}(u)
\right]
\]

正是两个不变量空间维数之和。这里不应加入复共轭：加入复共轭计算的是相应 Hom 型配对，而非对角张量表示的不变量。

同一个群元 \(u\) 同时作用于两个因子也正确，因为 BCGP 使用的是同一个已识别群 \(G\) 的对角作用，而不是第二因子上的逆作用。

---

## 4. 数值结论的可信度

### 4.1 三个阿贝尔条目可由 JSON 精确复核

Fourier 分解直接给出：

\[
\begin{array}{c|ccc}
\text{row} & d_{21}&d_{12}&d\\ \hline
§6.7,\ \mathbb Z_4^2&0&0&0\\
§6.18,\ \mathbb Z_4\times\mathbb Z_2&2&2&4\\
§6.19,\ \mathbb Z_2^3&3&3&6
\end{array}
\]

其中 §6.7 的字符列表与 Step 51 的独立字符计算一致；Step 52 没有使用

\[
\operatorname{Sym}^2H^0(K)\cong H^0(2K),
\]

所以它确实构成对该 \(d=0\) 结论的有意义交叉验证。

### 4.2 非阿贝尔条目至少有一项可精确复核

对 §6.9、\(G=S_5\)，按共轭类进行精确 Lefschetz 求和可得

\[
d_{21}=1,\qquad d_{12}=1,\qquad d=2,
\]

与 JSON 完全一致。这明显提高了非阿贝尔实现的可信度。

### 4.3 其余条目的内部检查

其余数值同时满足：

- 生成的置换群阶与预期相同；
- Riemann–Hurwitz 给出源中列出的 genus；
- \(\frac1{|G|}\sum\chi_K=0\)，符合 \(C_i/G\simeq\mathbb P^1\)；
- 结果在浮点误差约 \(10^{-15}\) 内为整数；
- 正负乘子约定给出同一总维数；
- note 与 JSON 逐项一致。

因此“所有已扫描的 \(K^2=4,6\) 条目均有 \(d>0\)”是可信的。

不过 `expected_d` 字典只是回归断言，不能算独立证据；它显然是由同一轮结果填入的。

---

## 5. 必须修正或补强的风险

### A. 扫描范围表述

脚本实际覆盖：

\[
§6.7,\quad §6.9\text{--}§6.27.
\]

它没有覆盖其他七个 \(K^2=2\) 条目：

\[
§6.1\text{--}§6.6,\quad §6.8.
\]

所以严格结论应写为：

> 在 Step 52 所扫描的 20 个条目中，只有 §6.7 的 \(d\) 为零。

不能写成“全部 BCGP product-quotient rows 中只有该条目”。

### B. 分支系统条件没有由脚本直接验证

算法预设每个 branch list 是真正的球面生成系统：

\[
\prod_i e_i=1,\qquad
\langle e_1,\dots,e_r\rangle=G,
\]

且元素阶与源 signature 一致。BCGP §6 确实将这些列表作为 spherical generators 给出，但脚本只用 `S1 + S2` 生成群；它没有断言每个 \(S_i\) 单独生成 \(G\)，也没有检查有序乘积为恒等元。

应增加每一行、每一个曲线的断言：

```python
assert ordered_product(branch) == G.identity
assert subgroup_generated(branch) == set(G.elements)
assert [G.order(e) for e in branch] == source_signature
```

否则保留群阶和 genus 的抄录错误仍可能漏过检查。

### C. 非阿贝尔局部旋转数约定

脚本假定源中的球面生成元 \(e_i\) 对应标准正向小环，其局部作用为

\[
z\mapsto e^{2\pi i/r_i}z.
\]

这是通常的 Riemann existence/spherical-generator 约定，并且阿贝尔 §6.7 的独立字符表及 §6.9 的共轭类复算支持该实现。但“统一取逆”测试只检查

\[
\lambda\leftrightarrow\lambda^{-1},
\]

不能排除某些分支点被独立换成另一 primitive power 的转录错误。对全部非阿贝尔表格作定理级使用时，宜附上源中该约定，或用普通特征标表/精确 Chevalley–Weil 再复算至少每类群的代表。

### D. 浮点而非精确 cyclotomic 运算

当前使用 `cmath.exp`，最后通过容差投影到整数。所得误差很小，数值上没有异常，但严格有限计算应改为：

- cyclotomic field 中的精确根单位；
- 共轭类求和；
- 最终符号化化简为整数。

这尤其适合最终可独立验证的证明记录。现有浮点计算足以支持“可信扫描”，但不宜单独承担形式化定理证明。

### E. 置换解析约定

所列 BCGP branch elements 的复循环基本都是互不相交循环，因此当前 parser 没有实际歧义。但代码声明非互不相交循环按自定的 left-to-right 规则处理。加入球面乘积和单独生成性检查会显著降低未来转录或扩表时的风险。

### F. Step 51 的来源依赖

从 \(d=0\) 到实际 simultaneous \(\mathbb Q\)-Gorenstein smoothing，依赖 Step 51 所引用的 Lee–Park Proposition 2.4(2)。该原文不在本次材料中，因此目前只能核验为“Step 51 对外部定理的明确引用”，不能由这里独立确认其全部假设及“实际圆盘族而非仅一阶提升”的结论。

最终证明记录应附上原命题并逐项核对：

- normal projective surface；
- quotient/T-singularities；
- \(H^2(T_X^0)=0\)；
- 局部 \(\mathbb Q\)-Gorenstein deformation的全局化；
- simultaneous smoothing 的实际 family-level 结论。

---

## 6. 解释边界

在 Step 51 桥梁成立的前提下，

\[
d=\dim H^2(X,T_X^0).
\]

因此 \(d=0\) 给出一个充分机制：所有局部 \(A_1\) 平滑参数可全局化，得到 simultaneous \(\mathbb Q\)-Gorenstein smoothing；再结合 canonical ampleness、Aubin–Yau 和 ADE simultaneous resolution，可为最小解消的底层光滑流形构造负 Einstein 度量。

反之，\(d>0\) 只表示

\[
H^2(X,T_X^0)\ne0
\]

以及“由该群消失直接推出所有局部平滑全局化”的简单路线不可用。它并不决定局部到整体映射

\[
H^0(\widetilde T_X^1)\longrightarrow H^2(T_X^0)
\]

的秩或核；其核仍可能包含所有节点坐标均非零的平滑方向。更不排除其他复结构、其他平滑族或非 Kähler Einstein 度量。

---

## 最终核验意见

- Lefschetz 迹公式：**正确**。
- 从 branch stabilizers 重建固定点与乘子：**正确，受标准 spherical-generator 局部旋转约定约束**。
- 张量特征标平均：**正确**。
- §6.7 的 \(d=0\)：**有独立且较强的交叉验证**。
- 所扫描 \(K^2=4,6\) 条目的 \(d>0\)：**数值与结构上可信；其中 §6.9 亦可精确复核**。
- 解释“\(d=0\) 是充分平滑路线，\(d>0\) 非否定定理”：**准确**。
- 使用时必须改成“在所扫描的 20 个条目中唯一”，并补上分支系统断言、精确 cyclotomic 复算及 Lee–Park 原文核对。
# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step26_nilpotent_abelian_forcing_audit.md",
    "Sessions/S0910A02/workspace/data/step26_nilpotent_submersion_balance.json",
    "Sessions/S0910A02/workspace/data/step26_heisenberg_moving_frame_ricci.json",
    "Sessions/S0910A02/workspace/notes/step25_structural_resolution_landscape.md",
    "Sessions/S0910A02/workspace/notes/step24_all_dim_positive_collapse_architecture.md",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Knowledge/objects/papers/2211.09998-Collapsed-Manifolds-with-local-Ricci-bounded-Covering-Geometr--4e46d62a6fcb--f76980c4eb0a/object.md",
    "Knowledge/objects/papers/Ricci-positive-metrics-on-connected-sums-of-projective-spaces--17bdbf22f9bb--cb9ce73e65bd/object.md"
  ]
}
```

## Task

Verify the Step-26 nilpotent abelian-forcing audit for the Yau-26 positive branch. Focus on mathematical correctness and theorem-shaping consequences: (i) the Heisenberg intrinsic Ricci/anistropy pattern; (ii) the twist-only rank/center bound and whether it is narrow; (iii) the cohomogeneity-one diagonal H3 moving-frame Ricci formulas and the claim that T-active local exact Ric=+1 data with large bracket are algebraically possible; (iv) whether this really defeats a pointwise Milnor-only abelian-forcing theorem and supports a graded/relative-rate theorem instead; (v) source-scope claims about Kapovitch--Wilking/Naber--Zhang/Rong. Do not invent external facts; if exact O'Neill formulas are needed but not in the files, state the missing source need precisely. Please give a direct scientific memo: corrections, confirmed parts, and what theorem statement remains viable.

## Output

# 科学核验备忘录

## 总评

Step-26 的三个核心计算均成立：

1. \(H_3\) 的内禀 Ricci 特征值及中心—生成元各向异性正确；
2. \(T=0\) 时中心方向给出的 \(b\) 上界及 twist 秩估计正确，但只使用了垂直 Ricci 方程，是很窄的必要条件；
3. 对角余维一 \(H_3\) 模型的移动标架 Ricci 公式正确，而且任意大的 \(b\) 确实可嵌入局部光滑的 \(\operatorname{Ric}=g\) 解中。

因此，单凭 Milnor 纤维 Ricci 在一点上迫使可见坍缩阿贝尔化的论证不成立。另一方面，当前材料并未证明一般非交换坍缩一定呈分级结构，更没有证明同尺度非交换坍缩在闭流形上不可能。严格成立的内容是：在验证过的 \(H_3\) 模型中，大 bracket 必然伴随同阶的第二基本形式以及 \(O(b^2)\) 的 bracket 变化率。

---

## 1. Heisenberg 内禀 Ricci：确认

设正交标架满足
\[
[e_1,e_2]=b e_3.
\]
Koszul 计算给出截面曲率
\[
K_{12}=-\frac34b^2,\qquad
K_{13}=K_{23}=\frac14b^2.
\]
故
\[
\operatorname{Ric}^F
=\operatorname{diag}\left(-\frac12b^2,-\frac12b^2,\frac12b^2\right),
\]
以及
\[
\operatorname{scal}_F=-\frac12b^2.
\]
中心方向与任一生成元方向的差为
\[
\operatorname{Ric}^F(e_3,e_3)-\operatorname{Ric}^F(e_1,e_1)=b^2.
\]

这与 `step26_nilpotent_submersion_balance.json` 完全一致。

---

## 2. \(T=0\) 的 twist 估计：成立，但只给必要条件

在纤维全测地的 Riemannian submersion 中，垂直方向满足
\[
\operatorname{Ric}_M(U,U)
=
\operatorname{Ric}_F(U,U)
+\sum_i|A_{X_i}U|^2.
\]
记
\[
Q(U,U)=\sum_i|A_{X_i}U|^2\ge0.
\]
若 \(\omega_{ij}=A_{X_i}X_j\)，则在通常的 O’Neill 约定下
\[
Q(U,U)=2\sum_{i<j}\langle U,\omega_{ij}\rangle^2;
\]
系数会随 \(A\) 的定义改变，但半正定性和
\[
\operatorname{rank}Q\le \binom d2
\]
不受影响。

对 \(H_3\)，若要求垂直 Ricci 精确等于单位阵，则
\[
Q=I-\operatorname{Ric}^F
=
\operatorname{diag}\left(
1+\frac12b^2,\,
1+\frac12b^2,\,
1-\frac12b^2
\right).
\]

由此：

- 若总 Ricci 满足 \(\operatorname{Ric}_M\le(1+\delta)g\)，中心方向给出
  \[
  \frac12b^2\le 1+\delta.
  \]
- \(0<b<\sqrt2\) 时，所需 \(Q\) 的秩为 \(3\)；
- \(b=\sqrt2\) 时，所需 \(Q\) 的秩为 \(2\)；
- 二维底空间只有一个独立的 \(\omega_{12}\)，故 \(\operatorname{rank}Q\le1\)，两种情形均不能实现；
- \(d\ge3\) 只通过秩测试，并不保证水平 Ricci、混合 Ricci、曲率形式闭合性及整体几何同时成立。

所以这里得到的是可靠的 \(T=0\) 代数阻碍，不是一般坍缩定理。

---

## 3. 余维一对角 \(H_3\) 模型：公式和局部大-\(b\) 解均成立

考虑
\[
g=dt^2+a(t)^2(\theta_1^2+\theta_2^2)+c(t)^2\theta_3^2,
\]
并定义
\[
k_1=\frac{a'}a,\qquad k_3=\frac{c'}c,\qquad
H=2k_1+k_3,\qquad b=\frac{c}{a^2}.
\]
正交标架的非零括号为
\[
[e_0,e_1]=-k_1e_1,\quad
[e_0,e_2]=-k_1e_2,\quad
[e_0,e_3]=-k_3e_3,\quad
[e_1,e_2]=be_3.
\]
因此
\[
\begin{aligned}
\operatorname{Ric}_{00}
&=-2(k_1'+k_1^2)-(k_3'+k_3^2),\\
\operatorname{Ric}_{11}
=\operatorname{Ric}_{22}
&=-\frac{b^2}{2}-k_1'-Hk_1,\\
\operatorname{Ric}_{33}
&=\frac{b^2}{2}-k_3'-Hk_3.
\end{aligned}
\]
`step26_heisenberg_moving_frame_ricci.json` 的符号计算与这些公式一致。

令垂直三个分量等于 \(1\)，得到
\[
k_1'=-1-\frac12b^2-Hk_1,\qquad
k_3'=-1+\frac12b^2-Hk_3,
\]
同时几何恒等式
\[
\frac{b'}b=k_3-2k_1.
\]
余下的 \(\operatorname{Ric}_{00}=1\) 等价于
\[
C:=4k_1^2+8k_1k_3+b^2+4=0.
\]

一个很有用的补充计算是
\[
C'=-2HC.
\]
因此只要初值满足 \(C=0\)，约束就由 ODE 精确保持。这比数值残差本身更强：光滑 ODE 的局部存在性，加上取正初值 \(a(0),c(0)\) 并解
\[
a'=k_1a,\qquad c'=k_3c,
\]
即可重建真正的局部光滑 Einstein 度量。

对任意 \(B>0\)，可取
\[
b(0)=B,\qquad
k_1(0)=\frac B2,\qquad
k_3(0)=-\frac B2-\frac1B.
\]
它精确满足 \(C=0\)。当 \(B=20\) 时即为文件中的
\[
k_1=10,\qquad k_3=-10.05.
\]
此时
\[
b'(0)=-\frac32B^2-1,
\]
所以文件中的 \(b'=-601\) 也正确。

数值积分所得 \(10^{-13}\) 量级残差主要反映 ODE 与约束保持；它不是与 ODE 无关的第二次曲率计算。真正独立的支撑来自移动标架符号推导。

---

## 4. 可进一步强化的大-\(b\) 定量关系

令
\[
|T|^2=2k_1^2+k_3^2.
\]
由约束
\[
4k_1^2+8k_1k_3=-(b^2+4)
\]
及恒等式
\[
4k_1^2+8k_1k_3+2|T|^2
=2(2k_1+k_3)^2\ge0
\]
可得
\[
|T|^2\ge\frac{b^2+4}{2}.
\]
所以“大 bracket 伴随 \(|T|\sim b\)”并非只由样本观察，而是该精确 Einstein 模型中的点态定理。

同样，由
\[
4k_1^2+8k_1k_3+\frac45(k_3-2k_1)^2
=\frac45(3k_1+k_3)^2\ge0
\]
得到
\[
\left|\frac{b'}b\right|^2
=(k_3-2k_1)^2
\ge\frac54(b^2+4).
\]
故
\[
|b'|\gtrsim b^2
\]
也是强制关系，而非特定初值的偶然现象。

这一估计还能推广到
\[
1-\delta\le \operatorname{Ric}_{ii}\le1+\delta
\]
的同一模型。记 \(\rho_i=\operatorname{Ric}_{ii}\)，消去 \(k_1',k_3'\) 可得
\[
4k_1^2+8k_1k_3
=
2\rho_0-4\rho_1-2\rho_3-b^2.
\]
因而当 \(\delta<1/2\) 时，
\[
|T|^2\ge\frac{b^2+4-8\delta}{2},
\]
以及
\[
\left|\frac{b'}b\right|^2
\ge\frac54\bigl(b^2+4-8\delta\bigr).
\]
这给出了 Step-26 “相对变化率”解释的严格模型版本。

---

## 5. 对阿贝尔化叙述的实际含义

该局部解确实排除了以下点态推理：

> 总 Ricci 接近 \(g\)，而 nilpotent 纤维的 Milnor Ricci 含有 \(\pm b^2/2\)，所以 \(b\) 必须小。

原因是总 Ricci 还含有 \(T\)、平均曲率及其导数；这些项能精确抵消 Milnor 各向异性。

而且取
\[
a(0)=c(0)=B^{-1}
\]
时，初始纤维在三个方向上同尺度，直径约 \(B^{-1}\)，同时
\[
b(0)=B.
\]
所以同尺度的非交换几何在单个局部切片上也可与 \(\operatorname{Ric}=g\) 共存，代价是
\[
|T|\asymp B,\qquad |b'|\asymp B^2.
\]
因此，“同尺度非交换坍缩已被排除”不能从现有计算推出。成立的是条件式表述：

> 若控制产生于 \(T\)、平均曲率及其横向导数的全部 O’Neill 项，使它们在总曲率尺度上保持 \(O(1)\)，则大 bracket 无法由这些项抵消；在该额外假设下，第一可见尺度的 bracket 才会趋于零。

分级图景与计算相容：
\[
a=\varepsilon^\alpha,\qquad c=\varepsilon^\gamma,\qquad
b=\varepsilon^{\gamma-2\alpha}.
\]
特别是 \(\gamma=2\alpha\) 时 \(b=O(1)\)，但在直径尺度重标后 bracket 为
\[
\varepsilon^\alpha b\longrightarrow0.
\]
这说明交换子方向可落入更小尺度。不过，一般非交换坍缩必然如此分解，尚需全套 O’Neill 方程、尺度一致的张量估计和奇异轨道通量分析。

---

## 6. 标量积分提供的信息

本模型中
\[
\operatorname{scal}_M
=
-\frac12b^2-2H'-H^2-|T|^2,
\qquad
w=a^2c,\quad \frac{w'}w=H.
\]
若所有函数周期，则
\[
\int \operatorname{scal}_M\,w\,dt
=
\int\left(-\frac12b^2+H^2-|T|^2\right)w\,dt.
\]
这里出现 \(+H^2\)，所以仅有标量积分通常不能直接控制 bracket；平均曲率仍可承担补偿。

在精确 \(\operatorname{Ric}=g\) 模型中，约束进一步给出
\[
-\frac12b^2+H^2-|T|^2=-b^2-2,
\]
与 \(\operatorname{scal}=4\) 的周期积分不相容。因此这些局部解不能直接拼成周期型闭模型。若通过奇异轨道闭合，则端点通量必须单独计算。

---

## 7. 文献内容与其实际给出的结构

### Kapovitch–Wilking / Naber–Zhang

所引内容基本准确：

- Naber–Zhang Theorem 2.26 转述 KW：在
  \[
  \operatorname{Ric}\ge-(n-1)
  \]
  下，短环像群是 \((w(n),n)\)-nilpotent。
- Theorem 2.27：若球 GH 接近一个 \(k\) 维 Ricci 极限球，则精细群为
  \[
  (w_0,n-k)\text{-nilpotent},\qquad
  \operatorname{rank}\le n-k.
  \]
  常数依赖于极限球的非坍缩尺度。
- Theorem 1.1、5.1 和 Proposition 6.4：在 GH 近似及最大秩等假设下，局部覆盖获得非坍缩和调和半径下界。
- 曲率张量上界还需要 Einstein 或 \(|\nabla\operatorname{Ric}|\) 上界；单纯两侧 Ricci 夹逼没有提供这一导数信息。

这些定理给出群论结构及覆盖正则性，并不自动生成对原度量具有定量 \(A,T,N\) 控制的 Riemannian submersion。

### Rong

Rong 的 Theorem B 确实要求：

- Ricci 下界；
- 局部 rewinding volume 下界；
- GH 接近较低维、非坍缩的光滑流形；
- 对底空间有截面曲率及 injectivity radius 控制。

所得是光滑纤维丛、infra-nil 纤维、仿射结构群及 GHA。与其文中经典有界截面曲率定理相比，Theorem B 的陈述没有给出原度量下的 \(\varepsilon\)-Riemannian submersion 估计，也没有给出纤维第二基本形式的统一估计。因此它解决了纤维拓扑识别，但尚未提供 Step-26 所需的 O’Neill 张量控制。

---

## 8. 仍可严格表述的定理形态

目前最坚实的版本是模型定理：

> 对余维一对角 \(H_3\) 度量，若 \(\operatorname{Ric}=g\)，则任意点都有
> \[
> |T|^2\ge\frac{b^2+4}{2},\qquad
> |\partial_t\log b|^2\ge\frac54(b^2+4).
> \]
> 对 \([1-\delta,1+\delta]\)-夹逼有相应的 \(8\delta\) 修正。

一般 regular infranil-submersion 的可行陈述应明确加入：

- 原度量与纤维丛结构之间的定量相容性；
- \(A,T,N\) 以及进入垂直 Ricci 的横向导数项的尺度一致上界；
- nilpotent 内禀标量与 bracket 范数之间的固定归一化公式；
- 奇异轨道或端点通量的处理。

当前文件中的 Burdick Lemma 2.5只处理由全测地 submersion 出发的特殊 doubly warped 度量，不能替代一般 \(T\neq0\) 的 O’Neill 公式。一般定理需要一份固定约定的直接来源，明确给出垂直 Ricci、混合 Ricci、标量迹、平均曲率散度项及积分测度。没有这组公式，Step-26 的一般分级定理仍是结构设想；其 \(H_3\) 局部模型部分则已得到完整代数验证。
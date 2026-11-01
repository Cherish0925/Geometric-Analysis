# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step63_SU2_nut_and_clean_zero_surface.md",
    "Sessions/S1003A01/workspace/scripts/step63_bianchiIX_nut_series.py",
    "Sessions/S1003A01/workspace/scripts/step63_nut_component.py",
    "Sessions/S1003A01/workspace/scripts/step63_nut_q.py",
    "Sessions/S1003A01/workspace/data/step63/bix_nut_series_order5.json",
    "Sessions/S1003A01/workspace/data/step63/bix_nut_component.out",
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md"
  ]
}
```

## Task

Independently check the Step-63 diagonal Bianchi-IX regular-nut calculation and its mathematical interpretation for the closed negative-scalar Goldberg problem. Read the note and exact scripts/data. Verify: (i) the u=t^2 Einstein and closure equations and regular-nut parameter count; (ii) whether the exact L1,...,L5 ideal and Singular localization really exclude all interior three-weight, genuinely triaxial branches through this order; (iii) whether the three associated components are exactly permutations of the stated complex-hyperbolic Kähler branch, including the closed-form sinh identification and q=0; (iv) what is proved versus only suggested about all-order formal or analytic branches. Identify any normalization, smoothness, ideal-theoretic, or overinterpretation errors and give corrected theorem wording.

## Output

# 科学核验备忘录

## 总结

Step 63 的核心计算在固定归一化下是正确的：

1. \(u=t^{2}\) 形式的 Einstein 方程、Hamilton 约束和不变自对偶闭形式方程均可直接从 Bianchi IX 曲率公式推出。
2. `bix_nut_component.out` 中的 Rabinowitsch 计算确实给出单位理想，因此 \(L_{1},\dots,L_{5}\) 不存在三个 \(R_i\) 都非零且 \(d_i\) 两两不同的复代数解。
3. 极小素理想在几何可行集 \(R_i\ge0,\ \sum R_i=1\) 上确实只留下三个轴向点；它们对应同一个复双曲 Kähler 模型的三个排列。
4. 两处文字需要修正：
   - 完整理想在真正的四个变量 \((R_1,R_2,d_1,d_2)\) 中维数是 \(1\)，不是 \(2\)；输出中的额外一维来自未参与完整理想的 Rabinowitsch 变量 \(z\)。
   - 三个代数组件本身是直线，不是三个点；只有与 \(R_i\ge0\) 相交后才各缩成一个点。
5. 脚本本身只算到 \(u^{5}\)，但补上一般阶递推矩阵后，可以得到更强的全阶结论：每个实的、正则的、对角 SU(2)-不变形式分支都必为排列后的复双曲 Kähler 分支。这个全阶结论不能仅靠“前五阶与闭式相符”来表达，所需的递推唯一性如下已经给出。

---

## 1. Einstein 方程、闭形式方程与 nut 参数

取标准归一化
\[
d\sigma_i=2\,\sigma_j\wedge\sigma_k
\]
（循环指标），使 \(\sum_i\sigma_i^2\) 为单位圆三球度量。设
\[
g=dt^2+\sum_{i=1}^3a_i(t)^2\sigma_i^2,\qquad
h_i=\frac{\dot a_i}{a_i}.
\]
正交方向上的 Ricci 分量为
\[
\operatorname{Ric}_{ii}
=-\frac{\ddot a_i}{a_i}-h_i(h_j+h_k)
+2\,\frac{a_i^4-(a_j^2-a_k^2)^2}{a_i^2a_j^2a_k^2}.
\]
令
\[
u=t^2,\qquad a_i=t f_i(u),\qquad
H_i=t h_i=1+2u\frac{f_i'}{f_i},\qquad
Z_i=t\frac{a_i}{a_ja_k}=\frac{f_i}{f_jf_k},
\]
其中此处撇号表示 \(d/du\)。将 \(\operatorname{Ric}_{ii}=\lambda\) 乘以 \(t^2\)，得到
\[
2uH_i'-H_i+H_i\sum_\ell H_\ell
-2\left[Z_i^2-(Z_j-Z_k)^2\right]+\lambda u=0.
\]
Gauss–Hamilton 方程为
\[
\sum_{i<j}H_iH_j+\sum_iZ_i^2
-2\sum_{i<j}Z_iZ_j+\lambda u=0.
\]
所以 `step63_bianchiIX_nut_series.py` 中 \(\lambda=-3\) 时的两个方程符号和系数正确；此时标量曲率为 \(s=-12\)。

### 正则 nut 展开

光滑 nut 要求
\[
a_i=t\bigl(1+A_i u+O(u^2)\bigr).
\]
代入任一 Einstein 方程的 \(u^1\) 项，得到
\[
6(A_1+A_2+A_3)+\lambda=0.
\]
因此 \(\lambda=-3\) 时
\[
A_i=\frac16+d_i,\qquad d_1+d_2+d_3=0.
\]
所以正则对角 Einstein nut 在最低自由阶恰有两个连续参数。这与脚本的参数化一致。

更进一步，若在 \(f_i\) 的 \(u^n\) 系数中加入 \(b_i u^n\)，令 \(B=b_1+b_2+b_3\)，则 Einstein 方程 \(u^n\) 项中新系数的线性部分为
\[
\delta E_i\big|_{u^n}
=2(n+2)\left(2(n-1)b_i+B\right).
\]
其迹零子空间上的特征值为
\[
4(n+2)(n-1),
\]
迹方向上的特征值为
\[
2(n+2)(2n+1).
\]
两者在所有 \(n\ge2\) 时均非零。因此给定 \((d_1,d_2,d_3)\) 后，全部高阶 \(f_i\) 系数唯一确定。脚本对 \(n=2,\dots,5\) 的求解是这个一般递推的前五步。

### 闭形式输运

取单位正交自对偶基
\[
\omega_i=dt\wedge(a_i\sigma_i)+a_ja_k\,\sigma_j\wedge\sigma_k,
\qquad |\omega_i|^2=2.
\]
对
\[
\Omega=\sum_i x_i\omega_i
\]
计算外微分，得到
\[
d\Omega=0
\quad\Longleftrightarrow\quad
(x_i a_ja_k)'_t=2x_i a_i.
\]
等价地，
\[
2u\frac{dx_i}{du}=M_i x_i,\qquad
M_i=2Z_i-H_j-H_k.
\]
令 \(X_i=x_i^2\)，便得到脚本中的
\[
uX_i'=M_iX_i.
\]
由于 \(M_i(0)=0\)，该方程在除去显式的 \(u\) 后是正则递推。初值
\[
r_i=x_i(0),\qquad R_i=r_i^2,\qquad \sum_iR_i=1
\]
给出一个 \(S^2\) 上的初始形式方向；使用 \(R_i\) 只丢掉离散符号，不影响长度条件。

还有一个重要事实：若 \(R_i=0\)，则 \(x_i(0)=0\)，而上述一阶方程的唯一形式解为
\[
x_i\equiv0.
\]
所以“轴向初值”不仅是 nut 上的轴向值，对应分量在整个局部解中都恒为零。

---

## 2. \(L_1,\dots,L_5\) 的理想计算

`step63_nut_component.py` 先置
\[
R_3=1-R_1-R_2
\]
并取 \(L_1,\dots,L_5\) 的分子。数据中的分母全是非零有理常数，因此清除分母不会改变零点集。

令
\[
P=R_1R_2R_3(d_1-d_2)(2d_1+d_2)(d_1+2d_2).
\]
Rabinowitsch 理想
\[
J=I+\langle1-zP\rangle
\]
的标准基在 `bix_nut_component.out` 中是 \(1\)。因此在代数闭包上也不存在满足
\[
R_1R_2R_3\ne0,\qquad
(d_1-d_2)(d_1-d_3)(d_2-d_3)\ne0
\]
的共同零点。这里
\[
d_3=-d_1-d_2,
\]
所以脚本中的后三个因子正是三个特征值差。由此，关于“三个权重均非零且最低曲率数据真正三轴”的排除是精确的。

### 极小素理想的正确读法

输出的三个极小素理想化简后给出下列三条直线：

\[
(d_1,d_2,d_3)
=\left(-\frac1{12},\frac16,-\frac1{12}\right),
\qquad
(R_1,R_2,R_3)=(r,1,-r);
\]

\[
(d_1,d_2,d_3)
=\left(-\frac1{12},-\frac1{12},\frac16\right),
\qquad
(R_1,R_2,R_3)=(r,-r,1);
\]

\[
(d_1,d_2,d_3)
=\left(\frac16,-\frac1{12},-\frac1{12}\right),
\qquad
(R_1,R_2,R_3)=(1,r,-r).
\]

例如输出中的第三个素理想含有 \(12d_2+1\)；代入 \(d_2=-1/12\) 后，其余两个多项式分别化为
\[
1728d_1-288,\qquad 432R_1-432,
\]
所以确实得到 \(d_1=1/6,\ R_1=1\)，而 \(R_2\) 保持自由，且 \(R_3=-R_2\)。

因此，代数几何上这三个组件不是三个孤立点。它们成为直线的原因很清楚：两个重复方向具有相同的输运因子，取相反的形式权重会在 \(\sum X_i\) 中逐阶抵消。

但在真实 almost-Kähler 几何中
\[
R_i=x_i(0)^2\ge0.
\]
于是每条直线都只能取 \(r=0\)。真实归一化零点集恰好是
\[
(R_1,R_2,R_3)=(1,0,0),(0,1,0),(0,0,1),
\]
并配上相应的
\[
(d_i,d_j,d_k)=\left(\frac16,-\frac1{12},-\frac1{12}\right).
\]

### 维数修正

Singular 的环为
\[
\mathbb Q[R_1,R_2,d_1,d_2,z].
\]
完整理想 \(I\) 不含 \(z\)，所以输出的 `dim full=2` 包含一个无关的自由 \(z\) 方向。去掉这个人工变量后，实际归一化理想在四个几何变量中的维数为 \(1\)，与上面三条直线一致。

因此，笔记中“理想维数二”以及“极小伴随素理想就是三个点”都应按上述方式改写。其真实几何结论仍然成立，而且比单纯的 Rabinowitsch 结论更强：在 \(R_i\ge0\) 上，前五个长度方程只允许三个轴向点。

关于“119 个最小二乘解”的具体收敛轨迹，所给文件没有列出参数序列；精确代数结果足以说明它们不是 119 个互异精确零点，但不能单凭当前输出重建每条数值轨迹。

---

## 3. 复双曲分支和 \(q=0\)

选取第一轴。理想计算给出
\[
d_1=\frac16,\qquad d_2=d_3=-\frac1{12},
\]
所以
\[
A_1=\frac13,\qquad A_2=A_3=\frac1{12}.
\]
脚本算出的级数正好是
\[
a_1(t)=\frac{\sinh(\sqrt2\,t)}{\sqrt2},
\qquad
a_2(t)=a_3(t)=\sqrt2\,\sinh\!\left(\frac{t}{\sqrt2}\right).
\]
其展开分别为
\[
\frac{a_1}{t}
=1+\frac{u}{3}+\frac{u^2}{30}+\frac{u^3}{630}
+\frac{u^4}{22680}+\frac{u^5}{1247400}+\cdots,
\]
\[
\frac{a_2}{t}
=1+\frac{u}{12}+\frac{u^2}{480}+\frac{u^3}{40320}
+\frac{u^4}{5806080}+\frac{u^5}{1277337600}+\cdots.
\]
这与 JSON 中全部五阶系数逐项一致。

令
\[
\rho=\frac{t}{\sqrt2}.
\]
则
\[
a_1=\sqrt2\sinh\rho\cosh\rho,\qquad
a_2=a_3=\sqrt2\sinh\rho,
\]
并且
\[
g=2\left[d\rho^2+\sinh^2\rho\,
\bigl(\sigma_2^2+\sigma_3^2+\cosh^2\rho\,\sigma_1^2\bigr)\right].
\]
在上述 \(\sigma_i\) 归一化下，这是复双曲二空间的极坐标表达，且
\[
\operatorname{Ric}=-3g.
\]

精确的 \(H_i,Z_i\) 为
\[
H_1=\rho(\coth\rho+\tanh\rho),\qquad
H_2=H_3=\rho\coth\rho,
\]
\[
Z_1=\rho\coth\rho,\qquad
Z_2=Z_3=\frac{\rho}{\sinh\rho\cosh\rho}
=\rho(\coth\rho-\tanh\rho).
\]
对于 \(\Omega=\pm\omega_1\)，有
\[
M_1=2Z_1-H_2-H_3=0.
\]
同时 `step63_nut_q.py` 中进入 \(q\) 的两个横向联络组合满足
\[
b_2=H_2-Z_1+Z_2-Z_3=0,\qquad
b_3=H_3-Z_1-Z_2+Z_3=0.
\]
因此
\[
q=|\nabla\Omega|^2=0
\]
是精确恒等式，不只是前五阶消失。等价地，
\[
(a_2a_3)'=2a_1
\]
说明 \(\omega_1\) 闭，而上述联络恒等式说明它平行。

需要注意，`step63_nut_q.py` 内部调用了有限阶 `series(...,0,5)`；脚本自身只验证截断消失。精确的 \(q=0\) 来自这里的闭式计算。

---

## 4. 全阶形式分支与解析分支

脚本直接提供的是：

- Einstein 系数到 \(u^5\)；
- 长度条件 \(L_1,\dots,L_5\)；
- 这五个多项式的精确代数零点结构。

单凭“五阶级数与 \(\sinh\) 相同”还不足以推出所有高阶系数相同。但第 1 节给出的递推矩阵补齐了这一步：

1. 任意全阶形式解必满足 \(L_1=\cdots=L_5=0\)。
2. \(R_i\ge0\) 迫使其最低数据成为三个轴向点之一。
3. 给定对应的 \(d_i\)，Einstein 系数在每个 \(n\ge2\) 唯一。
4. 闭式复双曲度量具有同一最低数据并精确满足 Einstein 方程，所以其级数就是唯一形式级数。
5. 其余两个 \(x_i\) 初值为零，闭形式输运唯一性给出 \(x_i\equiv0\)；活跃分量由常长度得到 \(x_1=\pm1\)。

因此可将结果表述为：

> **定理（对角 Bianchi IX 正则 nut）。**  
> 设 \(d\sigma_i=2\sigma_j\wedge\sigma_k\)，并设
> \[
> g=dt^2+\sum_i a_i(t)^2\sigma_i^2,\qquad
> a_i=t f_i(t^2),\quad f_i(0)=1,
> \]
> 是满足 \(\operatorname{Ric}=-3g\) 的实形式幂级数正则 nut。设
> \[
> \Omega=\sum_i x_i(t^2)\omega_i
> \]
> 是实的 SU(2)-不变自对偶形式，满足
> \[
> d\Omega=0,\qquad |\Omega|^2=2.
> \]
> 则经指标排列后，
> \[
> a_1=\frac{\sinh(\sqrt2\,t)}{\sqrt2},\qquad
> a_2=a_3=\sqrt2\sinh(t/\sqrt2),
> \]
> 且
> \[
> (x_1,x_2,x_3)=(\pm1,0,0).
> \]
> 因而 \(\Omega\) 平行，\(q=0\)，该形式解是复双曲 Kähler 解。相同结论适用于解析正则 nut。

对于光滑 Einstein 解，还可结合 Einstein 度量在调和坐标中的实解析性，排除具有相同全部 Taylor 系数但不等于该解析模型的平坦扰动。

所以，在所述对角且全 SU(2)-不变的类中，全阶排除可以成立；笔记中需要加入一般阶递推矩阵，而不是只写“前五个条件传播为 Kähler 分支”。

---

## 5. 对闭 \(s<0\) Goldberg 问题的含义

这个结果排除了一个具体的高对称构造：正则 nut 不能在该对角不变类中实现 Step 62 的非退化孤立 torsion 零点。唯一留下的模型在整个邻域内都是 Kähler，因而 nut 不是孤立 torsion 零点。

它本身不能推出闭 Einstein almost-Kähler 四流形必为 Kähler。所给推导没有处理：

- 不要求 \(\Omega\) 全 SU(2)-不变的局部解；
- 具有 \(t\)-依赖非对角轨道矩阵的系统；
- 一般无对称解析 germ；
- Step 62 中已经通过有限阶方程的普通 cone jets；
- 闭流形上的全局拼接和紧性机制。

关于笔记中的 torsion 零曲面结论：若闭光滑曲面 \(C\subset\{T=0\}\) 上 \(\nabla T\) 处处秩二，则由
\[
\det_{\mathbb R}Df=9|c|^4+|\det(S+A)|^2
\]
确实得到 \(c=0\)，且 \(TC=\ker DT\) 是 \(J\)-复直线。此时 \(\eta=0\)、\(W_3^+\ne0\)，而
\[
2\pi c_1(M,J)[C]=\frac{s}{4}\operatorname{Area}(C)
\]
与 \(W_3^+|_C\) 对 \(K_J^{-2}|_C\) 的平凡化矛盾。因此“处处秩二的闭零曲面不存在”这一部分成立。

若秩二点只稠密，则仍有
\[
\deg(K_J^{-2}|_C)=\frac{s\,\operatorname{Area}(C)}{4\pi}<0.
\]
但把这个次数写成若干 exceptional points 的局部绕数之和，还需要 \(W_3^+|_C\) 的零点离散。稠密秩二本身不保证 exceptional 集是有限点集；它也可能是更复杂的闭集。此处应增加“零点孤立”或使用横截扰动后的 Euler 类表述。

综合而言，Step 63 精确排除了所提出的对角 SU(2) nut 构造，并且在补入一般阶递推后可提升为该类中的全阶 Kähler 刚性；它尚未提供闭 \(s<0\) Goldberg 问题的一般局部排除或全局结论。
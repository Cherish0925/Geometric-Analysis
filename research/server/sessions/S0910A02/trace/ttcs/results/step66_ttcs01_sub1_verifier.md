# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step66_kahler_reduction_and_operator_audit.md",
    "Sessions/S0910A02/workspace/notes/step65_metric_export_findings.md",
    "Sessions/S0910A02/workspace/data/step66_kahler_substitute_step65.json",
    "Sessions/S0910A02/workspace/data/step66_operator_audit_profiles.json",
    "Sessions/S0910A02/workspace/data/step66_nonlinear_radial_audit.json",
    "Sessions/S0910A02/workspace/data/step66_ode_matrix_extract.json",
    "Sessions/S0910A02/workspace/data/step66_ode_compatibility.json",
    "Sessions/S0910A02/workspace/data/step66_least_squares_h_profile.json",
    "Sessions/S0910A02/workspace/data/step66_ls_profile_nonlinear_audit.json",
    "Sessions/S0910A02/workspace/data/source_text/biquard_1105_4904_pdftotext.txt"
  ]
}
```

## Task

Verify the Step-66 mathematical/computational conclusions about the Eguchi-Hanson correction export for the Yau-26 positive-branch experiment. Read the supplied note/data. Check specifically: (1) whether the Kähler-potential identity and its limitation by the EH bolt cohomology/obstruction term are stated correctly in the session conventions; (2) whether the solver-agnostic operator-norm audit results justify decoupling the refined small-defect certificate from BVP convergence and from the naive-start flow experiment; (3) whether the ODE compatibility extraction (rank-two highest-derivative system plus lower-order constraint) is a legitimate correction to the Step-65 handoff; (4) whether the LS-profile and nonlinear audit should be interpreted only as diagnostic, not as a near-pinched metric certificate; and (5) what concrete mathematical/computational next step would most reduce uncertainty without overclaiming. Please identify any sign/factor/cohomology/gauge caveats that could materially change the next work.

## Output

# 科学核验备忘录

## 总体结论

Step-66 的 Kähler 径向恒等式、原始 EH 插入具有 \(O(1)\) Ricci 端态残差、以及最高阶系数矩阵在 \(r>1\) 时秩为二，这三项均得到所给符号数据的支持。需要作三处实质修正：

1. Biquard 的方程中是  
   \[
   d_{eh}\operatorname{Ric}(h)=\Lambda eh+\sum_{j=1}^3\lambda_j o_j,
   \]
   不是 \(\frac13\sum_j\lambda_j o_j\)；原文排版中的上下求和指标被误读成了 \(1/3\)。

2. \(o_j\) 不是紧支撑张量。它们是 EH 上光滑、\(L^2\)、以 \(r^{-4}\) 衰减的全局核张量；紧支撑对象是拼接时的 \(\chi_t o_j\)。

3. ODE 相容关系不会通过选择 \(f_1'\) 来传播。把所给 \(f_2'',f_3''\) 代回相容关系并求导，\(f_1'\) 完全消去；剩余自由度是径向微分同胚规范，必须由 Bianchi 规范或另一规范方程固定。

此外，对 \((S^2\times S^2)/\mathbb Z_2\) 的实际二次项 \(H\)，三函数 \(U(2)\)-不变径向模型很可能不能完成渐近匹配。这个问题比当前数值 BVP 的收敛性更根本。

---

## 1. Kähler 势恒等式与 bolt 上的上同调

令本会话中的算子记为 \(\mathcal D=i\partial\bar\partial\)，并经复结构把 \((1,1)\)-形式识别为对称张量。给定
\[
h_\phi=A_\phi(e_0^2+e_3^2)+B_\phi(e_1^2+e_2^2),
\]
有
\[
S:=A_\phi+B_\phi
=(1-r^{-4})q'+\frac{3q}{r}+\frac{q}{r^5}.
\]
这里 \(S\) 是复迹，而实迹为 \(2S\)。

所给精确代入数据中，只有因子 \(-1/2\) 使三个独立框架分量同时恒等为零，因此在本会话归一化下
\[
d\operatorname{Ric}_{EH}(h_\phi)
=-\frac12\,\mathcal D S
\]
是正确的径向恒等式。这个 \(-1/2\) 与常见复坐标归一化不同，但与会话内部计算一致：在平坦渐近区，
\[
\mathcal D(r^2)\longrightarrow4\omega,
\]
而常见的另一种归一化给出 \(2\omega\)。后续若从文献导入公式，必须先统一这个二倍因子。

对
\[
q=\frac{2r^5}{r^4-1},\qquad
\phi=r^2+\frac12\log\frac{r^2-1}{r^2+1},
\]
直接代入确有 \(A_\phi=B_\phi=4\)，故
\[
\mathcal D\phi=4\omega.
\]
在 \(r=1\) 附近，\(q\sim[2(r-1)]^{-1}\)，所以对数奇性是真实的。又因
\[
\omega|_{S^2_{\rm bolt}}=e_1\wedge e_2,
\qquad
\int_{S^2_{\rm bolt}}\omega\ne0,
\]
而光滑全局标量 \(u\) 的 \(\mathcal D u\) 是恰当形式，在 bolt 上积分为零，故不存在光滑全局势表示 \(\omega\)。因此，纯光滑 Kähler 势模型不能解
\[
-\frac12\mathcal D S=\Lambda\omega,\qquad \Lambda\ne0.
\]

还有一个有用的内部一致性：
\[
\mathcal D(r^2)
=4\omega+4r^{-4}(e_0\wedge e_3-e_1\wedge e_2).
\]
第二项具有 EH 的 \(L^2\) 反自对偶谐和形式形状，解释了为什么 \(\mathcal D(r^2)\) 与 \(4\omega\) 的差异落在 EH 核方向中；同时两者对应的线性化 Ricci 都为零。

不过，上同调解释只直接覆盖固定复结构下的径向 Hermitian 通道。Biquard 的三维空间
\[
o_j(x,y)=\Omega(I_jx,y)
\]
是规范固定后的 Fredholm 余核，由同一个 \(L^2\) 谐和二形式 \(\Omega\) 与三个超 Kähler 复结构生成。非 Kähler 变化、复结构变化以及一般角向模式都不归约为一个标量势。因此，“bolt 上同调正好等同于全部三个 obstruction 张量”并不准确；它精确说明其中一个 Kähler 通道为何不能由光滑势完成。

---

## 2. Ricci 端态残差评估与流实验的分离

对物理插入
\[
g_\varepsilon=\varepsilon\widehat g_\varepsilon,
\qquad
\widehat g_\varepsilon=eh+\varepsilon h,
\]
正确的 Ricci 端态残差是
\[
E_\varepsilon
=g_\varepsilon^{-1}
\bigl(\operatorname{Ric}_{g_\varepsilon}-\Lambda g_\varepsilon\bigr)
=
\varepsilon^{-1}\widehat g_\varepsilon^{-1}
\operatorname{Ric}_{\widehat g_\varepsilon}
-\Lambda I.
\]
在固定 \(r\) 处展开得到
\[
E_\varepsilon
=eh^{-1}\bigl(d\operatorname{Ric}(h)-\Lambda eh\bigr)
+O(\varepsilon).
\]
这说明：直接评估候选张量的 Ricci 端态残差，在逻辑上不依赖生成该张量的 BVP 求解器是否报告收敛。

数据与这一公式一致：

- 原始 EH：一阶与非线性全区残差均为 \(1\)，这是精确的
  \(\operatorname{Ric}_{eh}=0\) 后果。
- \(h=r^2eh\)：一阶最大值约 \(8.92\)，非线性值随
  \(\varepsilon\to0\) 接近同一量级，正确捕捉了完整线性化 Ricci 与单纯 Lichnerowicz 算子的差别。
- \(h=4eh\)：线性化 Ricci 为零，因此残差仍为 \(1\)。
- 标量截断模型：远离 bolt 截断区时，一阶中位残差约
  \(3\times10^{-6}\)，但全区最大值为 \(5.0\)–\(11.6\)；非线性全区最大值也保持 \(5\)–\(12\)。远区最大值从
  \(0.0946\) 降至 \(0.0156\)，与过渡区预期的 \(O(\sqrt\varepsilon)\) 相符，但核心截断项没有消失。

因此，当前评估器已经可靠地区分了“局部消去源项”和“全局算子范数变小”这两件事。它还不是完整的近夹逼证明材料：实际对象需要包含完整角变量、外部 orbifold 区、拼接截断及所有 bubble，并需要对插值误差、网格细化和浮点误差给出可复验界。当前一阶脚本是候选 \(h\) 的线性残差评估器；非线性径向数据则是局部数值复核。

Biquard 原文 Remark 4.3 的朴素拼接
\[
g^0_{t,\varphi}=\chi_t\,t\,eh+(1-\chi_t)\varphi^*g_0
\]
在 \(t\) 足够小时是光滑正定度量，所以可以作为 Ricci–DeTurck 或变分计算的初值，不需要先有小残差。该流若不接近 Einstein 度量，不能推出同一光滑流形不承载其他 Einstein 度量；若流达到定态，还需分别计算 DeTurck 向量和
\(\operatorname{Ric}-\lambda g\)，以排除得到非 Einstein Ricci soliton 的可能。所述 \(r=0\) 已知模型作为算法对照，因而具有明确解释价值。

---

## 3. ODE 最高阶秩与规范自由度

所给矩阵在 \(r>1\) 时确有
\[
\operatorname{rank}M=2,
\qquad
(-1,2,1)M=0.
\]
在 \(r=1\) 处秩进一步降为 \(1\)，这与 bolt 坐标退化一致。相容关系为
\[
\begin{aligned}
C={}&\Lambda r^6-(3r^4+1)f_1
+2(r^4+1)f_2+2r^5 f_2'\\
&+(r^4-1)f_3+r(r^4-1)f_3'=0.
\end{aligned}
\]

关键修正是：利用数据中显示的 \(f_2''\) 和 \(f_3''\) 公式直接求导，可精确化简为
\[
C'=-\frac{4}{r(r^4-1)}\,C.
\]
其中所有 \(f_1'\) 项完全抵消。因此：

- 若一个初始截面上 \(C=0\)，则它由两条二阶方程自动保持；
- \(f_1'\) 不能由“保持相容关系”确定；
- 未确定的 \(f_1\) 对应径向微分同胚规范。

这正符合 Biquard Proposition 2.2 中“解在规范与核方向模去后确定”的陈述。以
\[
B h=\delta h+\frac12d\operatorname{tr}h,\qquad
\delta=-\operatorname{tr}\nabla
\]
为约定，三函数模型的径向 Bianchi 方程应为
\[
-\frac12 f_1'+f_2'+\frac12f_3'
-\frac{2}{r}(f_1-f_2)
-\frac{r^4+1}{r(r^4-1)}(f_1-f_3)=0.
\]
它才会关闭 \(f_1'\) 的自由度。该公式也显示 bolt 光滑性至少要求
\[
f_1-f_3=O(r-1).
\]
在适当距离坐标 \(s\) 中有 \(r-1\sim s^2\)；光滑系数是 \(s^2\) 的光滑函数，且极坐标平面要求 \(f_1(1)=f_3(1)\)。简单地在 \(r\) 坐标施加三个 Neumann 条件并不等价于 bolt 光滑性。

还有一个更重要的角向问题。若 ambient 模型确为等曲率
\(S^2\times S^2\)，取正交标架使 \(e_{12},e_{34}\) 为两个因子的面积形式，则曲率算子满足
\[
R(e_{12})=\kappa e_{12},\qquad
R(e_{34})=\kappa e_{34},
\]
混合二形式上的作用为零，所以
\[
R^+\sim\operatorname{diag}(\kappa,0,0),
\qquad
R^-\sim\operatorname{diag}(\kappa,0,0).
\]
选择 EH 复方向进入 \(\ker R^+\) 可以消去 Biquard 的首阶系数，但该曲率张量并不在这一复结构的 \(U(2)\) 下不变：对应的 \(U(2)\) 在另一半二形式上作用为完整 \(SO(3)\)，而秩一的 \(R^-\) 不是标量。故一般二次项 \(H\) 含非径向角模式，不能仅由
\((f_1,f_2,f_3)\) 匹配。商掉 \(\mathbb Z_2\) 不改变奇点处的局部曲率张量。

---

## 4. LS 张量与非线性数据的含义

LS 数据只能作为数值探索材料：

- LSQR 达到 \(20000\) 次迭代上限，估计条件数约
  \(1.02\times10^7\)。
- 线性残差中位数约 \(5.0\times10^{-4}\)，但全区最大值约
  \(4684\)；小的内部中位数不能控制算子范数上确界。
- 两端值由启发式惩罚产生，没有 ambient \(H\) 匹配，也没有 bolt 的 Frobenius 光滑展开。
- 非线性全区最大值在
  \(\varepsilon=10^{-2},3\times10^{-3},10^{-3},3\times10^{-4}\)
  时约为 \(18.7,19.9,20.3,20.4\)，没有趋零。
- 即使删去 \(r\le1.2\)，最大值仍约
  \(0.688,0.667,0.652,0.646\)。
- \(\varepsilon=10^{-4}\) 时自然拼接半径为 \(10\)，但张量数据只到 \(R=8\)；外端插值产生了约 \(10^4\) 的尖峰。
- 采样点上正定因子接近 \(1\)，只能说明所采样的矩阵尚为正定，不能替代 Ricci 端态上确界估计。

所以该 LS 张量不能作为近夹逼度量材料，也不能用于多 bubble 的全局常数计算。

---

## 5. 最能减少当前不确定性的具体数学对象

价值最高的下一项可复验产物是：**实际 ambient 二次项 \(H\) 在 EH 复方向下的精确 \(U(2)\)-模态分解**。其内容应包括

\[
H_{ij}(x)=-\frac13R_{ikjl}(p_0)x^kx^l
\]
在与 Biquard 曲率号数一致的正规坐标中的表达；把 EH Kähler 方向旋转到 \(\ker R^\pm\)；用齐次三次向量场把 \(H\) 放入欧氏 Bianchi 规范；随后分解其径向与非径向张量谐波。

这个计算会立即回答三函数 ODE 是否能匹配真实 \(H\)。对等曲率乘积，上述曲率算子已经预示必有非径向模式。若确实如此，正确数值对象是有限个角谐波的 Bianchi-规范径向 ODE 系统，而不是继续优化当前三函数 LS 模型。

符号实现还可用两个精确制造解校准号数与因子：

1. 任意径向向量场 \(X\) 的 \(h=\mathcal L_Xeh\) 必须满足
   \(d\operatorname{Ric}(h)=0\)；
2. Biquard Proposition 1.1 的显式 \(k_i\) 必须满足
   \(d\operatorname{Ric}(k_i)=o_i\)。

这两项连同 \(C'=-4C/[r(r^4-1)]\) 可同时验证完整线性化 Ricci、Bianchi 规范、obstruction 归一化以及 bolt 展开。
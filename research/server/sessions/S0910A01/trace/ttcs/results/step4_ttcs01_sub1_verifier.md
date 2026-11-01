# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step4_near_equality_and_boundary_calibration.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Knowledge/objects/papers/math-0111228-Curvature-Connected-Sums-and-Seiberg-Witten-Theory--84e6ef833958--5b74c8864d85/object.md",
    "Knowledge/objects/papers/Classical-boundary-value-problem-in-Riemannian-quantum-gravity-and-Taub--f07b76fb28c1--60f59311428a/object.md",
    "Knowledge/objects/papers/1712.08861-Partition-functions-on-3d-circle-bundles-and-their-gravity-du--7a54cfd2f253--29a9259ebb8d/object.md",
    "Sessions/S0910A01/workspace/data/step4_taub_bolt_ads_summary.json",
    "Sessions/S0910A01/workspace/scripts/step4_taub_bolt_boundary_probe.py"
  ]
}
```

## Task

Check the Step 4 mathematical correction and route reorientation for Yau Problem 26. Ground your answer in the provided files. In particular: (1) verify or correct the derivation D_a=I-(2/3)(a^+)^2 <= J-q with I-J=A-k and q=k-A/3, and the conclusion D_a/A->0 when delta_->0 and k/A->1/3; (2) verify the source-based equality mechanism of LeBrun's mixed Seiberg-Witten estimate (almost-Kähler structure, lowest W_+ eigenspace, s+s* constant, exact blow-up equality obstruction), distinguishing it from the withdrawn Weyl-only/harmonic-F_A+ argument; (3) check the corrected interpretation of bare ALE cores versus corrected gluing; (4) assess whether the Taub-Bolt-AdS boundary sampler supports only the stated conclusion that exact zero-defect fillings exist for attained boundary Cauchy data, not a general cap lower bound. Give a direct scientific memo identifying any mistakes, missing assumptions, and the most consequential next mathematical/computational test.

## Output

# 科学复核备忘录

## 总体结论

Step 4 的四项核心修正基本成立：

1. \(D_a\le J-q\) 的代数完全正确；由 \(\delta_-\to0\) 推出 \(D_a/A\to0\) 还需要明确写入 \(\operatorname{Vol}(M,g)/A=O(1)\)，在一般型复曲面吹起族中可由四维 Chern–Gauss–Bonnet 与 Noether 不等式得到。
2. LeBrun 2001 给出的等号机制确实是特殊 almost-Kähler 结构，而不是 \(F_A^+\) 调和或单独的 \(W_+\) 估计。吹起后的等号排除也与原文 Proposition 3.2 一致。
3. 裸 Ricci-flat ALE 核的无尺度缺陷计算正确；\(O(t^2)\) 的相对 \(C^2\) 修正原则上能产生阶一 Ricci 端同态，但这只是尺度分析，实际存在性取决于线性化 Einstein 方程、规范固定、余核投影及界面匹配。
4. Taub–Bolt–AdS 采样只支持“对其自身实现的截面 Cauchy 数据存在精确 \(\operatorname{Ric}=-g\) 填充”。它不能给出任意预设 Cauchy 数据上的填充，也不能产生一般 cap 残差的正下界。

---

## 1. \(D_a\) 计算与近等号结论

由所给定义
\[
I-J=A-k,\qquad q=k-\frac A3,
\]
可得精确恒等式
\[
\begin{aligned}
D_a
&=I-\frac23(a^+)^2\\
&=J+A-k-\frac23(a^+)^2\\
&=J-q-\frac23\bigl((a^+)^2-A\bigr).
\end{aligned}
\]
对 LeBrun 符号选择得到的 monopole class，\((a^+)^2\ge A\)，所以
\[
0\le D_a\le J-q.
\]
这里左端非负来自 LeBrun Proposition 3.1 的混合曲率估计。因而该推导正确，而且还给出
\[
J\ge q.
\]

### 从 Ricci 夹逼估计 \(J\)

把负支归一化明确写成
\[
\delta=\sup_M\bigl\|g^{-1}(\operatorname{Ric}+g)\bigr\|_{\rm op}.
\]
若 \(e_1,\dots,e_4\in[-\delta,\delta]\) 是 \(\operatorname{Ric}+g\) 的特征值，则
\[
s=-4+\sum_i e_i,\qquad
|\mathring r|^2=\sum_i(e_i-\bar e)^2\le \sum_i e_i^2\le4\delta^2.
\]
因此
\[
J=\frac1{8\pi^2}\int_M|\mathring r|^2\,d\mu
\le \frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g).
\]

体积估计可由完整的 Euler 型公式得到：
\[
8\pi^2\chi_{\rm top}(M)
=\int_M\left(|W|^2+\frac{s^2}{24}-\frac{|\mathring r|^2}{2}\right)d\mu.
\]
当 \(\delta<1\) 时，\(|s|\ge4(1-\delta)\)，故
\[
8\pi^2\chi_{\rm top}(M)
\ge
\left[\frac23(1-\delta)^2-2\delta^2\right]\operatorname{Vol}(M,g).
\]
记
\[
c(\delta)=\frac23(1-\delta)^2-2\delta^2;
\]
对充分小的 \(\delta\)，\(c(\delta)>0\)，从而
\[
\frac JA\le
\frac{4\delta^2}{c(\delta)}
\frac{\chi_{\rm top}(M)}A.
\]

因此文中 \(J/A=O(\delta^2)\) 需要
\[
\frac{\chi_{\rm top}(M)}A=O(1).
\]
对 \(M=X\#k\overline{\mathbb{CP}}^{\,2}\)、\(X\) 为最小一般型复曲面，这一点成立。Noether 不等式给出
\[
A=c_1^2(X)\ge2\chi_{\rm hol}(X)-6,
\]
于是
\[
c_2(X)=12\chi_{\rm hol}(X)-A\le5A+36,
\]
并且
\[
\chi_{\rm top}(M)=c_2(X)+k.
\]
当 \(k/A\to1/3\) 时，\(\chi_{\rm top}(M)/A\) 一致有界。

由此
\[
\frac JA\to0,\qquad \frac qA\to0,
\]
再用
\[
0\le\frac{D_a}{A}\le\frac JA-\frac qA
\]
便得到
\[
\boxed{\frac{D_a}{A}\to0.}
\]

若 \(X\) 只是任意具有 Seiberg–Witten 类的四流形而没有 \(\chi_{\rm top}(M)/A\) 控制，则 \(\delta\to0\) 本身不足以推出 \(J/A\to0\)。Step 4 中“加上 CGB 体积上界”这一短语应扩展为上面的完整条件链。

### 全符号平均公式

若所有
\[
a_\varepsilon=c_1(X)+\sum_j\varepsilon_jE_j
\]
均为可用 monopole classes，则
\[
2^{-k}\sum_\varepsilon(a_\varepsilon^+)^2
=(c_1(X)^+)^2+\sum_j(E_j^+)^2.
\]
选择平方最大的符号并用 \((c_1(X)^+)^2\ge A\)，得到
\[
I\ge\frac23\left(A+\sum_j(E_j^+)^2\right).
\]
结合 \(I=J+A-k\)，确有
\[
\boxed{
J\ge q+\frac23\sum_j(E_j^+)^2.
}
\]
所以
\[
\frac1A\sum_j(E_j^+)^2\to0
\]
是实际 Ricci 夹逼度量的推论，而不是单纯由交叉形式得出的结论。

---

## 2. LeBrun 等号机制

所附 LeBrun 2001 文本支持 Step 4 的来源修正。

### 实际证明链

Proposition 2.1 对 Seiberg–Witten 解 \((A,\Phi)\) 使用：

- spinor Weitzenböck 公式；
- 任意自对偶二形式的 Weitzenböck 公式；
- \(\varphi=\sigma(\Phi)=-iF_A^+\)；
- 导数估计
  \[
  |\nabla\varphi|^2\le\frac12|\Phi|^2|\nabla\Phi|^2;
  \]
- \(W_+\) 最小特征值 \(w\)；
- Hölder 不等式。

随后 Lemma 2.2 在共形类中构造 \(s+3w\) 为非正常数的度量，Theorem 2.3 得到
\[
\int_M
\left(
\frac23s-2\sqrt{\frac23}|W_+|
\right)^2d\mu
\ge32\pi^2(a^+)^2.
\]
这等价于 Ishida–LeBrun 所引述的
\[
\int_M(s-\sqrt6|W_+|)^2d\mu
\ge72\pi^2(a^+)^2.
\]

Proposition 3.1 再通过三角不等式与二维欧氏空间中的 Cauchy–Schwarz 得到
\[
\frac1{4\pi^2}\int_M
\left(\frac{s^2}{24}+2|W_+|^2\right)d\mu
\ge\frac23(a^+)^2.
\]

### \(F_A^+\) 并非一般调和

Seiberg–Witten 方程只给出
\[
F_A^+=i\sigma(\Phi).
\]
虽然 \(F_A\) 满足 Bianchi 恒等式 \(dF_A=0\)，但通常
\[
dF_A^+\ne0;
\]
因此 \(F_A^+\) 通常不是调和自对偶二形式。原文使用的是：

\[
-2\pi a^+
\quad\text{是}\quad
\sigma(\Phi)
\quad\text{的调和投影}.
\]

只有在等号成立时，Proposition 2.4 才推出 \(\sigma(\Phi)\) 本身等于相应调和代表。这正是撤回的“\(F_A^+\) 一开始就是调和的”论证与正确证明之间的关键差异。所附来源也没有给出足以替代混合估计的单独 \(W_+\) 下界。

### 精确等号的几何内容

LeBrun Proposition 2.4 表明等号强迫：

- \(g\) 为 almost-Kähler；
- almost-Kähler 形式 \(\omega\) 点态属于 \(W_+\) 的最低特征子空间；
- 
  \[
  s+s^*
  \]
  为非正常数，其中
  \[
  s^*=\frac s3+2W_+(\omega,\omega);
  \]
- 相关 almost-complex 第一 Chern 类与 spin\(^c\) 第一 Chern 类一致；
- 对产生 Proposition 3.1 的较强后继估计，\(W_+\) 还必须在 almost-complex 结构下不变。

若饱和度量同时 Einstein，Corollary 2.5 借助 Armstrong 的结果推出其为 Kähler–Einstein。Step 4 对这部分的陈述准确。

### 吹起后的精确等号排除

LeBrun Proposition 3.2 的论证也与 Step 4 一致。若 \(k>0\) 而等号成立，则：

1. almost-Kähler 类 \([\omega]\) 与选定 \(a^+\) 成比例；
2. 符号选择中的等号迫使
   \[
   [\omega]\cdot E_j=0;
   \]
3. 相邻的 Seiberg–Witten 类与 Taubes 理论给出异常类的伪全纯球代表；
4. 该球的辛面积必须严格为正，却又等于 \([\omega]\cdot E_j=0\)。

因此 \(k>0\) 时精确等号不可能出现。

这里并没有自动产生与 \(k\) 成比例的定量间隔。异常球面积可以趋于零；Taub–Bolt 小 \(L\) 模型甚至展示了在精确 \(\operatorname{Ric}=-g\) 的局部填充中，bolt 二球可缩至任意小。因此近等号路线真正需要的是 Seiberg–Witten spinor、共形极小化因子及 Weyl 集中的定量紧性，而不是单独的异常球面积下界。

### \(D_a/A\to0\) 能控制到哪一层

令
\[
\mathcal E^2=\int_M(s^2+48|W_+|^2)d\mu,\qquad
K=4\sqrt2\pi|a^+|.
\]
由定义直接算得
\[
\left(\frac{\mathcal E}{\sqrt2}\right)^2-K^2
=48\pi^2D_a.
\]
在当前情形中
\[
\frac IA\to\frac23,\qquad
\frac{(a^+)^2}{A}\to1.
\]
因此 \(D_a=o(A)\) 确实迫使 Proposition 3.1 中三角不等式、二维 Cauchy–Schwarz 及 Theorem 2.3 的数值差额均为 \(o(A)\)。但数值差额趋零尚不能直接给出 almost-Kähler 极限；塌缩、共形因子退化、spinor 零集和 Weyl 能量集中都可能破坏几何收敛。这正是 Step 4 所指出的核心分析问题。

---

## 3. 裸 ALE 核与修正 gluing

设 \(h\) 为 Ricci-flat ALE 度量，\(g_t=t^2h\)。常数缩放不改变 Ricci 张量作为 \((0,2)\)-张量，而 \(\operatorname{Ric}_h=0\)，故
\[
g_t^{-1}\bigl(\operatorname{Ric}_{g_t}+g_t\bigr)
=(t^2h)^{-1}(t^2h)=I.
\]
所以裸核的归一化算子范数缺陷恒为 \(1\)，与 \(t\) 无关。Step 4 对旧解释的修正正确。

另一方面，若在固定 ALE 坐标中写
\[
g_t=t^2(h+t^2k),
\]
并且 \(t^2k\) 是相对于 \(h\) 的 \(C^2\) 小量，则
\[
\operatorname{Ric}(g_t)
=\operatorname{Ric}(h+t^2k)
=t^2D\operatorname{Ric}_h(k)+O(t^4),
\]
从而
\[
g_t^{-1}\bigl(\operatorname{Ric}(g_t)+g_t\bigr)
=
h^{-1}\bigl(D\operatorname{Ric}_h(k)+h\bigr)+O(t^2).
\]
因此 \(O(t^2)\) 的相对 \(C^2\) 修正确能改变阶一的 Ricci 端同态。要在首阶实现 \(\operatorname{Ric}=-g\)，需要解
\[
D\operatorname{Ric}_h(k)=-h
\]
并同时处理微分同胚规范、余核投影、增长条件和外部 Cauchy 数据。

这里“相对 \(O(t^2)\)”必须指经过缩放后的 \(C^2\) 控制；仅有 \(C^0\) 小量无法控制 Ricci 张量。首个余核投影非零时会留下阶一端同态残差；该投影为零只消除了首阶障碍，并不自动产生完整非线性解。Step 4 把高阶修正 gluing 保留下来，在尺度分析上是正确的。

---

## 4. Taub–Bolt–AdS 采样所支持的内容

Akbar 给出的度量在 \(\Lambda=-1\) 约定下满足
\[
\operatorname{Ric}=-g.
\]
所附脚本使用的
\[
\Delta(\rho)=\rho^2-2M\rho+L^2-
\left(L^4+2L^2\rho^2-\frac{\rho^4}{3}\right)
\]
以及
\[
0<L^2\le\frac{2-\sqrt3}{4},
\qquad
\rho_b=\frac{1\pm\sqrt{1+16L^4-16L^2}}{4L}
\]
都与 Akbar 文本一致。由 \(\Delta(\rho_b)=0\) 解出的 \(M\) 公式也正确。

有限截面上的诱导 Berger 数据
\[
a^2=\rho^2-L^2,\qquad
b^2=\frac{4L^2\Delta}{\rho^2-L^2}
\]
正确。令 \(t\) 为向外测地距离，则
\[
\frac{d\rho}{dt}=\frac{\sqrt\Delta}{a},
\]
脚本中的
\[
\alpha=\frac1a\frac{da}{dt},\qquad
\beta=\frac1b\frac{db}{dt}
\]
公式亦正确。

一个有用的独立一致性关系来自 Einstein Hamilton 约束。按脚本的左不变形式归一化，
\[
R_\gamma=\frac2{a^2}-\frac{b^2}{2a^4},
\]
而 \(K\) 的特征值为 \((\alpha,\alpha,\beta)\)。由于内部满足 \(\operatorname{Ric}=-g\)，应有
\[
\boxed{
R_\gamma-2\alpha^2-4\alpha\beta=-2.
}
\]
对 `step4_taub_bolt_ads_summary.json` 中 \(b/a\simeq0.25\) 的样本，
\[
R_\gamma\simeq0.00412,\quad
\alpha\simeq0.578786,\quad
\beta\simeq0.576265,
\]
代入后左端约为 \(-2.0000\)。这为导数和法向约定提供了良好交叉验证。

### 采样结果的精确含义

- 对每个满足正定性并来自正则 bolt 参数的样本，内部度量解析上满足 \(\operatorname{Ric}=-g\)。
- \(p=1\) 的截断内部具有 \(\mathcal O(-1)\to S^2\) 的圆盘丛拓扑；按标准复定向可读作 \(\overline{\mathbb{CP}}^{\,2}\) 去掉一个球，Akbar 的 \(CP^2\) 表述涉及定向约定。
- 因而，不预先固定截面 Cauchy 数据、只在此拓扑上的 \(U(2)\)-不变 cap 中取 Ricci 残差下确界时，下确界已经是零。

但当前采样不能推出：

- 任意指定 \((a,b,\alpha,\beta)\) 都能实现；
- 任意外部 collar 都能与这些 cap 匹配；
- 在平滑过渡区仍可保持小的无权 Ricci 端同态误差；
- 某个固定 Cauchy 数据问题存在统一正下界。

正则 Taub–Bolt 族只有参数 \((L,\rho_{\rm cut})\)，而同质 Cauchy 数据由
\[
(a,b,\alpha,\beta)
\]
描述，并受一个 Hamilton 关系约束。故该族至多给出允许 Cauchy 数据空间中的低维子集。拼接时若两侧都采用各自向外法向，还必须满足
\[
K_{\rm cap}+K_{\rm ext}=0,
\]
而不仅是第一基本形式相等。

另外，JSON 中的 `ricci_defect_sup: 0.0` 是由解析 Einstein 公式直接写入的标记，并非脚本对 Ricci 分量所作的数值求值。样本数量和 \(b/a\) 数值区间也只对应脚本选取的有限 \((L,\rho)\) 网格，不能视为完整参数像。Akbar 文本还陈述了任意 Berger Dirichlet 数据的填充结果，但当前脚本没有独立重现其七次多项式论证；Step 4 不依赖这一更强陈述是合适的。

---

## 5. 最有信息量的下一项数学—计算检验

最关键的具体对象是**受约束的 Cauchy 匹配与线性余核投影**，而不是继续统计自由 cap 的 Ricci 残差。

对 Taub–Bolt cap 定义
\[
\mathcal C_{\rm cap}(L,\rho)
=(a,b,\alpha,\beta),
\]
对一个实际候选外部 collar 定义相应
\[
\mathcal C_{\rm ext}(\theta)
=(a_{\rm ext},b_{\rm ext},
\alpha_{\rm ext},\beta_{\rm ext}).
\]
采用两侧向外法向时，一个直接的无量纲失配量为
\[
\mathfrak m=
\max\left\{
\left|\log\frac a{a_{\rm ext}}\right|,
\left|\log\frac b{b_{\rm ext}}\right|,
|\alpha+\alpha_{\rm ext}|,
|\beta+\beta_{\rm ext}|
\right\}.
\]
该量应与 gauge-fixed 线性 Einstein 算子的余核投影一起记录。仅有 \(\mathfrak m\to0\) 尚不足以控制过渡区的二阶导数；还需检验修正解是否使
\[
\sup\left\|g^{-1}(\operatorname{Ric}+g)\right\|_{\rm op}\to0
\]
贯穿整个 collar。

这一检验直接区分两种机制：

- bolt Cauchy 数据能沿 \(L\to0\) 或其他退化参数逼近真实外部数据，并且首阶余核投影同时趋零；
- exact cap 虽存在，但其第二基本形式始终无法接近外部所需数据，或线性余核投影保持阶一。

对全局近等号路线，相应缺失的数学内容是一个针对 LeBrun 证明链的 concentration–compactness 定理：从
\[
\delta_i\to0,\qquad D_{a_i}/A_i\to0
\]
构造受控的 almost-Kähler 形式，明确描述 spinor 零集、共形因子和 Weyl 集中，并追踪异常类是否进入 Taub–Bolt/ALE 型泡中。没有这一层分析，精确等号下的 Taubes 面积矛盾还不能直接转化为近等号矛盾。
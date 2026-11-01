# TTCS Independent Branch Record

```json
{
  "step_id": 57,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step60_all_order_continuation_and_terminal_chart.md",
    "Sessions/S0910A03/workspace/scripts/step60_family_enumeration_verify.py",
    "Sessions/S0910A03/workspace/data/step60_family_enumeration_verify.json",
    "Sessions/S0910A01/workspace/notes/step57_preceptor_deTurck_uniqueness_and_scope_review.md",
    "Sessions/S0910A01/workspace/notes/step45_consolidated_IL_negative_gap_proof.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md"
  ]
}
```

## Task

Verify A03 Step60's all-order continuation and terminal pullback-chart repair as a potential component of the restricted Ishida--LeBrun negative-gap route. Focus on mathematical substance: (1) Are the exact coordinate-time families T1--T6 and U1--U7 plausibly exhaustive from the base equations, time-connection commutators, and spatial commutators? (2) Do the two key conversions (B1*B1)T=4(C1*C1)U and a T_m=U_m-sum B_q*T_{m-q} remove the dangerous unweighted current terms without hiding a new same-level derivative? (3) Does the all-order tower legitimately give C^infty convergence to a positive terminal metric and permit uniqueness-free splice by autonomous time-jet matching? (4) Is the terminal Liouville pullback selection and W^{2,q}->L^1 density convergence enough for the Derdzinski forbidden-germ contradiction? Note any errors, hidden assumptions, or proof details still required. Keep the conclusion restricted to the four-dimensional negative IL class and not the full Yau 26 statement.

## Output

# 科学复核备忘录

## 总评

Step60 的末端 Liouville 选择、指数映射拉回、\(W^{2,q}\) 强收敛以及 Derdziński 局部矛盾，数学结构基本成立。任意阶延拓部分的最高阶分配和三角结构也很可信，但目前更准确地说是“主导导数族加低阶余项的闭合框架”，尚不是逐项写出的精确张量恒等式。另有两个需要明确修正之处：

1. (1.5) 中的独立 \(a\cdot1\) 和 (1.6) 中的独立 \(a^2\) 不可能是实际非零项。
2. (3.4)–(3.7) 对最低层 \(m=1\) 有循环依赖；任意阶归纳应以先前模块给出的
   \[
   T_1,\ U_1,\ C_2\in L^q\qquad(\forall q<\infty)
   \]
   为起点，再从 \(m=2\) 向上推进。

在这两点修正并补全低阶余项估计后，该延拓与末端图表模块可以用于四维 \(\operatorname{Ric}\approx-g\) 的 Ishida–LeBrun 路线。

---

## 1. T1–T6 与 U1–U7 的穷尽性

### 1.1 主导导数分配是正确的

从
\[
\partial_tT
=a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T+\cdots)
\]
出发，施加 \(\nabla^m\) 后：

- 对 \(a\Delta T\)、\(B_1\nabla T\)、\(B_2T\) 使用 Leibniz 公式，确实统一产生
  \[
  B_r*T_{m+2-r},\qquad 1\le r\le m+2.
  \]
- 二次反应项产生
  \[
  B_r*T_i*T_j,\qquad r+i+j=m.
  \]
- 空间交换子产生
  \[
  a*\nabla^r\operatorname{Rm}*T_s,\qquad r+s=m.
  \]
- 时间连接交换子产生主项
  \[
  U_{r+1}*T_s,\qquad r+s=m-1,
  \]
  因为
  \[
  \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)=g^{-1}*U_1.
  \]

同理，先把 \((B_1*B_1)*T\) 改写为 \(C_1*C_1*U\)，再对 \(U\) 方程求导，U2–U7 的最高阶分配与 Leibniz、空间交换子和时间交换子一致。代码核验了 1 到 64 阶共 160,864 个整数分配，没有记录索引矛盾；这确实支持三角结构。

### 1.2 “精确恒等式”的表述需要修正

取 \(T=0\)。由于
\[
T=\operatorname{Rm}+\frac{g\owedge g}{2(n-1)},
\]
这对应常截面曲率 \(-1/(n-1)\)，且
\[
U=aT=0,\qquad \partial_tg=-2\operatorname{Ric}(U)=0.
\]
因此必有 \(\partial_tT=\partial_tU=0\)。所以：

- (1.5) 中若 \(a\cdot1\) 是真正独立的非零项，就与该平稳解矛盾；
- (1.6) 中若 \(a^2\) 是真正独立的非零项，也有同样矛盾。

保持移位曲率的代数消去后，合理的结构应为
\[
\partial_tT
=a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T),
\]
\[
\partial_tU
=a\Delta U+B_1*\nabla U+B_2*U
 +(C_1*C_1)*U+U*U+aU,
\]
允许不同的普适收缩系数，但没有独立于 \(T,U\) 的强迫项。Step60 多列出的 \(B_m\) 与 \(\nabla^m(a^2)\) 对能量估计无害，却不能作为实际非零张量项使用。

### 1.3 时间重排余项未被 T1–T6、U1–U7 逐项覆盖

把 \(\nabla^r(\partial_t\Gamma)\) 改成固定导数顺序时，会出现例如
\[
(\nabla^q\operatorname{Rm})*U_{r-q}*T_s,
\qquad q\le r-1,\quad r+s=m-1,
\]
以及在 \(U_m\) 方程中的
\[
(\nabla^q\operatorname{Rm})*U_{r-q}*U_s.
\]
这些并不字面属于 T1–T6 或 U1–U7。它们的确是先前层量：\(q\le m-2\)，相应的 \(U\) 阶数也不超过 \(m-1\)，所以不会破坏归纳，但应明确放入一个余项多项式，并写出所有导数分配不等式。

因此，现有脚本验证的是已列族的整数分配性质，不能验证张量演算中是否遗漏了一个低阶乘积族。一个可直接引用的证明版本需要把上述时间重排项、Ricci 重排项以及 \(C_{m+1}\) 方程中的类似项统一写成 \(\mathcal P_m,\mathcal R_m,\mathcal S_m\)。

---

## 2. 两个关键转换

### 2.1 \((B_1*B_1)*T=4(C_1*C_1)*U\)

由于
\[
B_1=\nabla a=2\chi\nabla\chi=2\chi C_1,
\]
每一个具体收缩都满足
\[
(B_1*B_1)*T
=4\chi^2(C_1*C_1)*T
=4(C_1*C_1)*U.
\]
这是逐项精确的代数转换，不涉及除以 \(a\)，在 \(\chi=0\) 处也没有奇性。

对其求 \(m\) 阶导数后，极端分配只有
\[
C_1*C_1*U_m,\qquad C_{m+1}*C_1*U_0,
\]
以及先前层乘积。最高 cutoff 导数是 \(C_{m+1}\)，没有重新出现未加权的 \(T_m\)。

### 2.2 \(aT_m\) 的转换

Leibniz 公式给出
\[
U_m=\nabla^m(aT)
=aT_m+\sum_{q=1}^m B_q*T_{m-q},
\]
其中星号包含导数位置的置换与组合系数。因此
\[
aT_m
=U_m-\sum_{q=1}^m B_q*T_{m-q}.
\]
右侧没有 \(T_m\)；所有 \(T\) 因子最高为 \(T_{m-1}\)。此外 \(B_m\) 只含最高 \(C_m\)，而当前 cutoff 伙伴是 \(C_{m+1}\)，所以这里也没有隐藏的新同阶导数。

这正好处理 U5 的极端项
\[
a\nabla^m\operatorname{Rm}*U_0.
\]
因为 \(m\ge1\) 时 \(\nabla^mG=0\)，有 \(\nabla^m\operatorname{Rm}=T_m\)，继而得到
\[
U_m*U_0+\text{先前层项}.
\]
该转换是有效的。

---

## 3. 任意阶能量与平滑截止时刻

### 3.1 \(m\ge2\) 的耦合闭合可信

最高 cutoff 项
\[
2\chi C_{m+2}*U_0
\]
积分一次后，导数落在 \(U_0\) 上产生
\[
I_m=\int\chi |C_{m+1}|\,|U_1|\,|U_m|^{p-1}.
\]
令 \(V=U_m\)、\(Z=C_{m+1}\)、\(f=\chi|V|^{p/2}\)，四维 Sobolev 嵌入给出
\[
\|f\|_4^2
\le C\bigl(p^2D^U_{m,p}+\|V\|_p^p\bigr).
\]
当 \(m\ge2\) 时，\(U_1\) 已是先前层量，其 \(L^4\) 范数可以放入常数；随后 Young 不等式确实产生
\[
\varepsilon D^U_{m,p}
+C\bigl(1+\|Z\|_p^p+\|V\|_p^p\bigr).
\]
当前 Hessian 项 \(B_2*V\) 也可以通过一次分部积分和
\[
\frac{|\nabla a|^2}{a}=4|C_1|^2
\]
吸收到加权耗散中。

### 3.2 最低层 \(m=1\) 尚未由该论证推出

当 \(m=1\) 时，\(V=U_1\)，所以残余项变成
\[
I_1=\int\chi |C_2|\,|U_1|^p.
\]
此时 (3.4) 中的 \(\|U_1\|_4\) 不是先前层常数，而是当前未知量。直接使用该式会产生类似
\[
\|C_2\|_p^2\,\|U_1\|_p^p
\]
的乘积，不能化为 (3.7) 的线性 Gronwall 右端。

\(T_1\) 层也有类似现象：最高 cutoff 项积分后可产生
\[
\int \chi |C_2|\,|T_1|^p.
\]

因此 Step60 的任意阶模块应从先前文档已经列出的基础输入
\[
T_1,U_1,C_2\in L^q,\qquad \forall q<\infty,
\]
开始。以此为基础，\(m=2,3,\ldots\) 的归纳结构是合理的。若要保留
\[
T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
\]
这一最初箭头，还需要一个独立的低阶估计或额外消去机制。

### 3.3 固定背景连接转换需要写成一个实际归纳

在所有 \(T_j,U_j,C_{j+1}\) 的有限 \(L^p\) 范数均有时间一致控制后，令
\[
A=\nabla^{g(t)}-\bar\nabla,\qquad \bar g=g(\tau).
\]
基本公式是
\[
\partial_tA=g^{-1}*\nabla^g\operatorname{Ric}(U)=g^{-1}*U_1.
\]
对其施加 \(\bar\nabla^m\) 后，最高源项是 \(U_{m+1}\)，其余是
\(A_{\le m-1}\)、\(U_{\le m}\) 和 \(g^{-1}\) 的乘积。取 \(p>4\)，利用四维 Sobolev 乘法和逐阶 Gronwall，可以得到所有固定背景 \(H^s\) 控制。Step60 的 (5.2) 目前是示意式，但没有明显的导数损失。

由
\[
\sup_{t<T_*}\|\partial_tg(t)\|_{H^s(\bar g)}<\infty
\]
可得
\[
\|g(t)-g(t')\|_{H^s(\bar g)}
\le C_s|t-t'|,
\]
于是 \(g(t)\) 在每个 \(H^s\) 中有极限，兼容后得到 \(C^\infty\) 收敛。

正定性可由已有双 Lipschitz 控制直接得到；等价地，若
\[
\|\partial_tg\|_{g,\mathrm{op}}
\le2\|aE\|_{g,\mathrm{op}}
\]
的时间积分有限，则
\[
e^{-2\int\|aE\|}\,g(\tau)
\le g(t)\le
e^{2\int\|aE\|}\,g(\tau),
\]
故极限 \(g_*\) 仍正定。

### 3.4 无需唯一性的拼接成立

设
\[
\mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g).
\]
对旧分支，
\[
\partial_t^\ell g(t)=\mathcal F_\ell(g(t)),
\]
而 \(\mathcal F_\ell\) 是依赖有限空间 jet 的光滑微分算子。\(g(t)\to g_*\) 的 \(C^\infty\) 收敛给出
\[
\partial_t^\ell g(t)\to\mathcal F_\ell(g_*).
\]
任何从 \(g_*\) 出发、使用同一固定 \(\chi\) 的局部解也满足相同的初始时间 jet。故所有
\(\partial_x^\alpha\partial_t^\ell g\) 在拼接时刻一致，分段解是光滑解。

这一步只依赖从任意光滑正定数据出发的逐数据局部存在构造。Step60 §4 的主符号计算也正确说明了为何不应使用原先的 ungauged \(L^2\) 度量差估计。

---

## 4. Liouville 选择与拉回图表

### 4.1 平均选择正确消除了拓扑尺度

若
\[
\operatorname{Vol}(P_i)\ge c_0A_i,\qquad
\int_{M_i}\mathfrak D_i\le C_0\delta_i^2A_i,
\]
并且径向 Jacobi 行列式满足
\[
c\,t^3\le j_i(p,u,t)\le C\,t^3,
\]
则
\[
\int_{P_i}\mathcal A_\rho\mathfrak D_i(p)\,d\mu_i(p)
\le C(K,\rho)\int_{M_i}\mathfrak D_i\,d\mu_i.
\]
这是 Liouville 测度在测地流下不变性的直接结果。即使 \(\exp_p\) 在基流形上多对一，积分是在初始单位切向量上完成的，不会产生不可控的重数。

于是存在 \(p_i\in P_i\) 满足
\[
\mathcal A_\rho\mathfrak D_i(p_i)
\le C\,\delta_i^2.
\]
\(A_i\) 在这里确实完全消去。

### 4.2 拉回球提供了所需的局部几何

必须同时使用两项假设：

1. 所有长度不超过 \(\rho\) 的径向测地线均留在 \(|\operatorname{Rm}|\le K\) 的 plateau 中；
2. \(\rho<cK^{-1/2}\)，从而没有共轭点。

在
\[
\bigl(B_\rho(0)\subset T_{p_i}M_i,\;(\exp_{p_i})^*g_i\bigr)
\]
上，原点的指数映射就是径向恒等映射，因此原点具有一致的 injectivity radius。基流形中的不同径向线可以汇合，但在拉回球中仍是不同点。由曲率控制和原点 injectivity radius，在固定更小球上可取一致 harmonic coordinates，并得到
\[
C^{1,\alpha}\cap W^{2,q}\qquad(\forall q<\infty)
\]
控制。

### 4.3 \(W^{2,q}\) 强收敛足以传递密度

小平均给出
\[
E_i=\operatorname{Ric}_{g_i}+g_i\to0
\quad\text{于 }L^2_{\mathrm{loc}}.
\]
曲率一致有界使其进一步在所有有限 \(L^q\) 中趋零。harmonic-coordinate Ricci 方程随后给出平滑 Einstein 极限
\[
\operatorname{Ric}_{g_\infty}=-g_\infty.
\]
对差方程使用内部椭圆估计，可将弱 \(W^{2,q}\) 收敛提升为
\[
g_i\to g_\infty
\quad\text{强收敛于 }W^{2,q}_{\mathrm{loc}},
\]
故曲率在有限 \(L^q\) 中强收敛。

Step60 的密度项 \(G_i\) 与 §1 中的移位曲率 \(G\) 符号冲突。这里应明确写成 Step8 的
\[
\mathcal G=f^2-(a_-)^2.
\]
\(\mathcal G\) 由标量曲率、\(|W^+|\)、\(W^+\) 的最小特征值和截断函数代数组合而成。最小特征值对对称矩阵是 Lipschitz 函数，因此强曲率 \(L^q\) 收敛和一致曲率控制足以推出
\[
\mathfrak D_i\to\mathfrak D_\infty
\quad\text{于 }L^1_{\mathrm{loc}}.
\]
于是
\[
\int_{U'}\mathfrak D_\infty=0.
\]
极限密度非负且连续，故在局部恒为零。

### 4.4 Derdziński 矛盾成立

密度为零给出
\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\qquad
\operatorname{Spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right),
\qquad |W_\infty^+|^2=\frac1{24}.
\]
Einstein 条件给出 \(\delta W_\infty^+=0\)。Derdziński 1983 Proposition 5 随后说明
\[
(24|W^+|^2)^{1/3}g_\infty=g_\infty
\]
局部 Kähler。但四维 Kähler–Einstein 度量满足
\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
与 \(1/24\) 矛盾。

等价地，常特征值投影引理给出 \(\nabla W^+=0\)，而
\[
0=\Delta|W^+|^2
=2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]
在上述数值下给出
\[
|\nabla W^+|^2=\frac1{16}.
\]
末端局部矛盾因此充分成立，不需要逼近度量的点态曲率收敛。

---

## 5. 适用于四维 IL 路线的结论

Step60 可以作为四维 \(\operatorname{Ric}\approx-g\) 的 Ishida–LeBrun 间隙论证中的有效组件，但其任意阶部分依赖以下已明确的数学输入：

- 精确流的逐数据局部存在；
- \(T_1,U_1,C_2\) 的所有有限 \(L^q\) 基础估计；
- 把时间重排产生的低阶三重乘积写入正式余项；
- 固定背景连接的逐阶 Sobolev 归纳；
- 终时刻的全局密度积分估计、\(A_i\)-比例中心集、统一 \(K,\rho,c_0\)。

拓扑尺度 \(A_i\) 在 Liouville 选择中确实消去，但所得常数仍依赖 \(K,\rho,c_0\)、流估计和具体 IL 几何输入。该组件并未产生仅依赖维数的 Ricci 夹逼常数，也未处理正号情形、任意四维拓扑或 \(n\ge5\)。
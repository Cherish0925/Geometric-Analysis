# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 57,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step57_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step57_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify A03 Step60's all-order continuation and terminal pullback-chart repair as a potential component of the restricted Ishida--LeBrun negative-gap route. Focus on mathematical substance: (1) Are the exact coordinate-time families T1--T6 and U1--U7 plausibly exhaustive from the base equations, time-connection commutators, and spatial commutators? (2) Do the two key conversions (B1*B1)T=4(C1*C1)U and a T_m=U_m-sum B_q*T_{m-q} remove the dangerous unweighted current terms without hiding a new same-level derivative? (3) Does the all-order tower legitimately give C^infty convergence to a positive terminal metric and permit uniqueness-free splice by autonomous time-jet matching? (4) Is the terminal Liouville pullback selection and W^{2,q}->L^1 density convergence enough for the Derdzinski forbidden-germ contradiction? Note any errors, hidden assumptions, or proof details still required. Keep the conclusion restricted to the four-dimensional negative IL class and not the full Yau 26 statement.

## Integrated Scientific Memo

# Step 60 核验结论

## 总结判断

Step 60 的两个核心代数转换、终端 Liouville 选择、指数映射拉回图表、\(W^{2,q}\) 椭圆升级，以及 Derdziński 禁止芽矛盾，原则上成立。

任意阶延拓的最高阶三角结构也很可信，但当前文本尚不能算作完整的逐项证明：T1–T6、U1–U7 应理解为**主导导数族**，还需把时间连接重排和 Ricci 交换产生的低阶多因子项明确收入余项多项式。此外有两个实质性修正：

1. (1.5) 中独立的 \(a\cdot1\) 与 (1.6) 中独立的 \(a^2\) 不应存在；
2. (3.3)–(3.7) 对 \(m=1\) 存在循环，归纳应以既有基础估计
   \[
   T_1,\ U_1,\ C_2\in L^q,\qquad q<\infty
   \]
   为起点，从 \(m=2\) 推进。

因此，该模块可作为四维负号 Ishida–LeBrun 路线的**条件性组件**，但尚需补齐所列证明依赖。

---

## 1. T1–T6、U1–U7 是否穷尽？

### 1.1 最高阶分配基本正确

由
\[
\partial_tT
 =a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T)
\]
施加 \(\nabla^m\)，Leibniz、空间交换子和时间连接交换子分别产生：

\[
B_r*T_{m+2-r},\qquad
B_r*T_i*T_j,
\]
\[
a*\nabla^r\operatorname{Rm}*T_s,\qquad
U_{r+1}*T_s,
\]
以及线性低阶项。这正对应 T2–T6；T1 是主扩散项。

把 \(U=aT\) 的方程先用
\[
(B_1*B_1)*T=4(C_1*C_1)*U
\]
改写后，同样得到 U2–U7 的最高阶分配。脚本对 1–64 阶共 160,864 个整数分配的检查，确实验证了这些**已列族内部**的三角性。

但脚本不证明穷尽性：它没有从张量 PDE 自动生成所有项，只检查预先写入的族。因此 64 阶零失败是有价值的一致性检验，不是全阶张量恒等式的证明。

### 1.2 时间重排产生额外低阶多因子项

将 \(\nabla^r(\partial_t\Gamma)\) 重排成固定协变导数顺序，会出现例如
\[
(\nabla^q\operatorname{Rm})*U_{r-q}*T_s,
\qquad q\le r-1,\quad r+s=m-1,
\]
以及 \(U_m\) 方程中的
\[
(\nabla^q\operatorname{Rm})*U_{r-q}*U_s.
\]
这些并不逐字属于 T1–T6 或 U1–U7。它们不破坏三角性，因为
\[
q\le r-1\le m-2
\]
且其余加权导数也不超过当前层，但应正式写入
\(\mathcal P_m,\mathcal R_m,\mathcal S_m\)，并列明所有阶数约束。

因此，“exactly the following universal contraction families”表述过强；更准确的是：

> T1–T6、U1–U7 穷尽主导分配，所有导数重排余项均为严格低阶多项式。

完整证明仍需一份索引级或严格不变量级的 commutator lemma。

### 1.3 基础方程中的常数强迫项有误

令
\[
T=\operatorname{Rm}+\frac{g\owedge g}{2(n-1)}.
\]
若 \(T=0\)，则度量具有截面曲率 \(-1/(n-1)\)，从而
\[
U=aT=0,\qquad \partial_tg=-2\operatorname{Ric}(U)=0.
\]
于是必有
\[
\partial_tT=\partial_tU=0.
\]
因此 (1.5) 的独立 \(a\cdot1\) 和 (1.6) 的独立 \(a^2\) 若为非零普适项，会直接与该平稳解冲突。

结构方程应改为
\[
\partial_tT
 =a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T),
\]
\[
\partial_tU
 =a\Delta U+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+aU,
\]
允许星号中的普适系数和收缩变化，但无独立常数强迫。相应地，T6 中裸 \(B_m\) 及 U7 中来自 \(\nabla^m(a^2)\) 的部分只是无害的过度包络，不应作为实际非零项引用。

---

## 2. 两个关键转换是否真正消除危险项？

### 2.1 \( (B_1*B_1)T \) 转换完全有效

因为
\[
B_1=\nabla(\chi^2)=2\chi C_1,
\]
每个具体收缩都满足
\[
(B_1*B_1)*T
 =4\chi^2(C_1*C_1)*T
 =4(C_1*C_1)*U.
\]
没有除以 \(a\)，所以在 \(\chi=0\) 处同样成立。

求 \(m\) 阶导数后，极端分配为
\[
C_1*C_1*U_m,
\qquad
C_{m+1}*C_1*U_0,
\]
其余均为较低层。不会重新产生裸 \(T_m\)，也没有 \(C_{m+2}\)。

### 2.2 \(aT_m\) 转换也没有隐藏同阶导数

Leibniz 公式严格给出
\[
U_m=\nabla^m(aT)
 =aT_m+\sum_{q=1}^{m}\binom mq B_q*T_{m-q},
\]
故
\[
aT_m
 =U_m-\sum_{q=1}^{m}\binom mq B_q*T_{m-q}.
\]
Step 60 的星号记号可吸收二项式系数，但正式陈述最好保留其存在。

右端所有未加权 \(T\) 均至多为 \(T_{m-1}\)。最高 \(B_m\) 仅含至多 \(C_m\)，而当前 cutoff 伙伴是 \(C_{m+1}\)。应用于 U5 的极端项时，
\[
a\nabla^m\operatorname{Rm}*U_0
 =aT_m*U_0
 =U_m*U_0+\text{严格低阶项},
\]
这里使用 \(m\ge1\) 时 \(\nabla^mG=0\)。所以此转换也是干净的。

---

## 3. 任意阶塔、终端极限与无唯一性拼接

### 3.1 \(m\ge2\) 的耦合能量机制成立

最高 cutoff 项
\[
2\chi C_{m+2}*U_0
\]
分部积分一次后，关键残项为
\[
I_m=\int\chi |C_{m+1}|\,|U_1|\,|U_m|^{p-1}.
\]
令
\[
V=U_m,\quad Z=C_{m+1},\quad f=\chi|V|^{p/2}.
\]
四维中
\[
\|f\|_4^2
 \le C_S\left(p^2D^U_{m,p}+C\|V\|_p^p\right),
\]
并且 Hölder 指数
\[
\frac14+\frac1p+\frac14+\frac{p-2}{2p}=1
\]
匹配。若 \(m\ge2\)，则 \(U_1\) 是既有低阶量，Young 不等式确实给出
\[
I_m\le\varepsilon D^U_{m,p}
 +C\bigl(1+\|Z\|_p^p+\|V\|_p^p\bigr).
\]

\(B_1*U_{m+1}\) 由
\[
\frac{|B_1|^2}{a}=4|C_1|^2
\]
吸收；\(B_2*U_m\) 的 signed-Hessian 分部积分结构也可闭合，但其所需张量收缩估计是从早先 Step 35 引入的依赖，Step 60 本身没有重证。

### 3.2 \(m=1\) 不能由同一估计直接推出

当 \(m=1\) 时，
\[
V=U_1,\qquad
I_1=\int\chi |C_2|\,|U_1|^p.
\]
此时 (3.4) 中的 \(\|U_1\|_4\) 不再是低阶已知常数，而是当前未知量。直接 Young 会产生类似
\[
\|C_2\|_p^2\|U_1\|_p^p
\]
的非线性当前层乘积，不能得到 (3.7) 所写的线性 Gronwall 形式。\(T_1\) 层有相同问题。

因此归纳应明确写为：

- 基础模块提供
  \[
  T_1,U_1,C_2\in L^q\quad(\forall q<\infty);
  \]
- Step 60 的统一任意阶论证从 \(m=2\) 开始：
  \[
  (U_2,C_3)\to T_2\to(U_3,C_4)\to T_3\to\cdots.
  \]

若要保留
\[
T_0\to(U_1,C_2)\to T_1
\]
作为本模块自身的结论，则必须另写低阶估计。

### 3.3 从协变塔到固定背景 \(H^s\) 仍需正式归纳

设
\[
A=\nabla^{g(t)}-\bar\nabla,\qquad \bar g=g(\tau).
\]
基本演化是
\[
\partial_tA=g^{-1}*\nabla^g\operatorname{Ric}(U)
           =g^{-1}*U_1.
\]
对 \(\bar\nabla^m\) 求导，最高源项是 \(U_{m+1}\)，其余为
\(A_{<m}\)、\(U_{\le m}\)、\(g^{-1}\) 的乘积。取足够大的有限 \(p>4\)，利用四维 Sobolev 乘法并逐阶 Gronwall，可得到所有固定背景导数。

Step 60 的 (5.2) 体现了正确结构，没有明显导数损失，但还不是完整证明；应写出：

1. \(\nabla^g\) 与 \(\bar\nabla\) 的逐阶转换公式；
2. 每阶所需的 \(p\)；
3. 乘积估计；
4. \(A\) 和 \(g\) 的同步归纳。

完成后，
\[
\sup_{t<T_*}\|\partial_tg(t)\|_{H^s(\bar g)}<\infty
\]
给出
\[
\|g(t)-g(t')\|_{H^s}\le C_s|t-t'|,
\]
所以 \(g(t)\) 在每个 \(H^s\) 中收敛，兼容性和 Sobolev 嵌入给出
\[
g(t)\to g_*\quad\text{于 }C^\infty.
\]

### 3.4 正定性与拼接

\(g_*\) 的正定性需要保留到 \(T_*\) 的双 Lipschitz 控制，或使用
\[
\|\partial_tg\|_{g,\mathrm{op}}\le2\|aE\|_{g,\mathrm{op}}
\]
和有限时间积分得到
\[
e^{-2\int\|aE\|}\,g(\tau)
\le g(t)\le
e^{2\int\|aE\|}\,g(\tau).
\]
这不是仅由 \(C^\infty\) 收敛自动推出的。

一旦 \(g_*\) 光滑正定，并且逐数据局部存在适用于 \(g_*\)，无唯一性拼接是正确的。令
\[
\mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g),
\qquad
\mathcal F_{\ell+1}=D\mathcal F_\ell[\mathcal F].
\]
旧分支和任意从 \(g_*\) 出发的新分支均满足
\[
\partial_t^\ell g=\mathcal F_\ell(g).
\]
因此所有单侧时空 jets 在 \(T_*\) 匹配，分段解为光滑解。无需在重叠区比较两个分支，也无需使用错误的 ungauged \(L^2\) 唯一性估计。

此结论是条件性的：它依赖逐数据局部存在，以及在 \([\tau,T_*)\) 上保持 \(\|U\|_\infty\)、双 Lipschitz 和 Sobolev 常数等零阶条件。

---

## 4. 终端 Liouville 选择与 Derdziński 矛盾

### 4.1 Liouville 选择成立

由
\[
\operatorname{Vol}(P_i)\ge c_0A_i,
\qquad
\int_{M_i}\mathfrak D_i\le C_0\delta_i^2A_i,
\]
以及径向 Jacobi 比较
\[
c_Rt^3\le j_i(p,u,t)\le C_Rt^3,
\]
Fubini 和测地流的 Liouville 测度不变性给出
\[
\int_{P_i}\mathcal A_\rho\mathfrak D_i(p)\,d\mu_i(p)
 \le C(K,\rho)\int_{M_i}\mathfrak D_i\,d\mu_i.
\]
于是存在 \(p_i\in P_i\) 使
\[
\mathcal A_\rho\mathfrak D_i(p_i)
 \le C\,\delta_i^2.
\]
拓扑尺度 \(A_i\) 确实完全消去。由于积分在初始单位切向量上完成，\(\exp_p\) 在基流形上的折叠或多对一不会引入重数损失。

### 4.2 拉回球的非塌缩需要共轭半径条件

必须明确使用：

- 所有长度 \(\le\rho\) 的径向测地线留在 \(|\operatorname{Rm}|\le K\) 的 plateau；
- \(\rho<cK^{-1/2}\)，从而无共轭点。

在
\[
(B_\rho(0)\subset T_{p_i}M_i,(\exp_{p_i})^*g_i)
\]
中，基流形上相交的径向线在拉回域内仍是不同点；中心具有统一 injectivity radius。故在固定较小球上可取一致 harmonic coordinates，获得
\[
C^{1,\alpha}\cap W^{2,q},\qquad q<\infty,
\]
控制。

### 4.3 强 \(W^{2,q}\) 足以传递密度

小平均和 \(\mathfrak D_i\ge|E_i|^2\) 给出
\[
E_i\to0\quad\text{于 }L^2_{\rm loc}.
\]
曲率一致有界使其在所有有限 \(L^q\) 中趋零。harmonic-coordinate Ricci 方程给出弱 Einstein 极限，并通过内部差方程估计升级为
\[
\widetilde g_i\to g_\infty
\quad\text{强 }W^{2,q}_{\rm loc}.
\]
于是曲率强 \(L^q\) 收敛。标量曲率、\(|W^+|\) 及 \(W^+\) 最小特征值都是有界曲率范围内的 Lipschitz 代数量，因此显式 LeBrun gap
\[
\mathcal G=f^2-(a_-)^2
\]
也在 \(L^1_{\rm loc}\) 中收敛。

这里应把 Step 60 §6 的 \(G_i\) 政名为 \(\mathcal G_i\)，以免和移位曲率
\[
G=\frac{g\owedge g}{2(n-1)}
\]
混淆。

由非负性和
\[
\int_{U'}\mathfrak D_\infty=0
\]
得到
\[
\mathfrak D_\infty\equiv0.
\]
不需要近似度量曲率逐点收敛。

### 4.4 禁止芽矛盾成立

密度为零推出
\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\qquad
|W_\infty^+|^2=\frac1{24},\qquad
\operatorname{Spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Einstein 条件给出 \(\delta W_\infty^+=0\)。Derdziński Proposition 5 说明
\[
(24|W^+|^2)^{1/3}g_\infty=g_\infty
\]
局部 Kähler；但四维 Kähler–Einstein、\(\operatorname{Ric}=-g\) 时
\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
与 \(1/24\) 矛盾。

等价地，常两特征值投影结论给出 \(\nabla W^+=0\)，而 Einstein–Weyl 恒等式在上述谱值下给出
\[
|\nabla W^+|^2=\frac1{16}.
\]
所以终端局部矛盾充分成立。

---

## 最终核验状态

Step 60 的有效内容是：

- 两个危险项转换严格正确，且没有隐藏同阶导数；
- \(m\ge2\) 的当前对三角闭合机制可信；
- 在补全固定背景归纳后，任意阶控制可给出正定光滑终端度量；
- 自治方程的全时间 jet 匹配提供真正无需唯一性的拼接；
- Liouville 选择、拉回非塌缩、强 \(W^{2,q}\to L^1\) 密度传递和 Derdziński 禁止芽矛盾均成立。

仍需补齐或显式引用：

1. 修正去掉 (1.5)、(1.6) 的独立常数强迫项；
2. 从 \(T_1,U_1,C_2\) 基础层开始归纳，或另证 \(m=1\)；
3. 索引级基础曲率演化及 T/U 族穷尽性；
4. 时间重排低阶多因子余项的正式定义；
5. signed-Hessian 收缩估计；
6. 固定背景 Sobolev 归纳；
7. 逐数据局部存在、零阶第一退出控制及终端全局密度/中心集输入。

在这些条件下，它是四维负号 Ishida–LeBrun 间隙路线的可用组件；它不产生仅依赖维数的 Ricci 夹逼常数，也不处理正号、一般四维拓扑或 \(n\ge5\)，因而不解决完整 Yau 第26题。
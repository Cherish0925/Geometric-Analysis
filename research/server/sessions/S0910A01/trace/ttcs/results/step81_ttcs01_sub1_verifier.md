# TTCS Independent Branch Record

```json
{
  "step_id": 81,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step81_L_exchange_and_radial_ledger.md",
    "Sessions/S0910A01/workspace/data/step81_L_symmetry_scale_ledger.json",
    "Sessions/S0910A01/workspace/data/step81_L_H4_transport.json",
    "Sessions/S0910A01/workspace/notes/step80_J_equivariant_all_order_reduction.md",
    "Sessions/S0910A01/trace/ttcs/results/step80_ttcs01_verifier1_integration.md",
    "Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 81 refinement of the positive mixed-row product-orbifold construction. User goal is Yau Problem 26; this is only a local positive-Einstein desingularization test. Read the notes/data and check: (1) the single-factor antipodal L(x,y)=(-x,y) really descends to the quotient, exchanges the two A-orbits, reverses 4D orientation, and swaps the plus/minus EH chiralities compatibly with the diagonal mixed assignment; (2) L transports the J-fixed radial direction omega2 with the stated sign and is compatible with the full angular H^4/rho_x formula, not a frozen-rho shortcut; (3) the surviving radial finite-dimensional response should be recorded as F_i=t_i sum_j B_ij t_j^2+R_i rather than sum_j B_ij t_j^3; (4) L symmetry constrains the candidate B matrix to [[a,b],[b,a]] only after fixing transported radial normalizations and does not force positive-scale balance; (5) identify any missing sign, normalization, order, self/cross-response, logarithmic, gauge, or shape-mode issue that must be handled before a real coefficient calculation can support or obstruct an Einstein desingularization.

## Output

# Step 81 科学核验备忘录

## 总结

Step 81 的两个核心修正成立：

1. 单因子反足映射 \(L(x,y)=(-x,y)\) 确实把对角节点轨道与非对角节点轨道互换，同时反转四维定向，因此把正、反自对偶空间互换；在所取基下，它把 \(J\)-偶径向方向 \(\omega _2^+\) 送到 \(+\omega _2^-\)。
2. 若节点 \(j\) 的 EH 远场产生 \(t_j^2H^4(\phi_j)\)，其在接收节点 \(i\) 诱导的曲率二次射流进入 Ozuch 第一投影后还要乘接收尺度 \(t_i\)。所以交互项是
   \[
   t_it_j^2,
   \]
   而不是 \(t_j^3\)。

不过，矩阵
\[
B=\begin{pmatrix}a&b\\ b&a\end{pmatrix}
\]
目前仍只是候选三次齐次部分。Ozuch 现有的 \(O(t_{\max}^{5/2})\) 估计不能分辨三次项，且其 Remark 2.11 明确允许空间对数项。另有一处线性代数可加强：在上述交换对称性下，非零 \(B\) 的正尺度核不可能具有不等尺度比；正核必要求 \(a+b=0\)，并且在 \(B\ne0\) 时必有 \(t_1=t_2\)。

---

## 1. \(L\) 的商作用、节点作用与手征交换

商作用为
\[
\sigma=(r_\pi,r_\pi).
\]
反足映射与每个球面上的半转动对易，因此
\[
L\sigma=\sigma L,\qquad L^2=\mathrm{id}.
\]
故 \(L\) 下降为
\[
(S^2\times S^2)/\langle\sigma\rangle
\]
上的 orbifold 等距变换。局部群作用为 \(-I_4\)，它也与 \(DL\) 对易。

在源、靶节点的相容定向积框架中可以取
\[
q:=DL=\operatorname{diag}(1,-1,1,1),\qquad \det q=-1.
\]
这是合理的：\(S^2\) 的反足映射反转二维定向，第二因子恒等，故乘积四维定向被反转。

节点作用为
\[
NN\mapsto SN,\quad SS\mapsto NS,\quad
NS\mapsto SS,\quad SN\mapsto NN.
\]
所以
\[
\{NN,SS\}\longleftrightarrow\{NS,SN\}.
\]
对角混合赋值
\[
\epsilon(s_1,s_2)=s_1s_2
\]
满足
\[
\epsilon(L(s_1,s_2))=-\epsilon(s_1,s_2).
\]
这与 \(q\) 交换 \(\Lambda^+\) 和 \(\Lambda^-\) 完全一致，而不是仅交换节点标签。

采用 Step 80 中的标准基，
\[
q_*:
\begin{cases}
\omega_1^+\mapsto-\omega_1^-,\\
\omega_2^+\mapsto+\omega_2^-,\\
\omega_3^+\mapsto+\omega_3^-,
\end{cases}
\qquad
q_*:
\begin{cases}
\omega_1^-\mapsto-\omega_1^+,\\
\omega_2^-\mapsto+\omega_2^+,\\
\omega_3^-\mapsto+\omega_3^+.
\end{cases}
\]
这是直接的二形式计算。例如
\[
\omega_2^+=e^{13}-e^{24}
\mapsto e^{13}+e^{24}=\omega_2^-.
\]
令
\[
S=\operatorname{diag}(-1,1,1),
\]
则曲率块按
\[
R^-_{\mathrm{target}}=S R^+_{\mathrm{source}}S^T
\]
运输。因此
\[
\operatorname{diag}(1,0,0)\mapsto\operatorname{diag}(1,0,0).
\]

更重要的是，径向 EH 核张量的符号也为正，而不只是二形式的符号。由 EH 参数族的协变性，
\[
L^*\operatorname{eh}_{t\omega_2^-}
=\operatorname{eh}_{t\omega_2^+}.
\]
对 \(t\) 微分可得
\[
L^*\mathbf o_{\mathrm{rad}}^-=\mathbf o_{\mathrm{rad}}^+.
\]
因此以 \(L\)-运输的 Ozuch 径向核张量作投影时，没有额外负号。四维定向反转也不会给 \(L^2\) 投影增加符号，因为积分使用 Riemannian 体积密度。

---

## 2. 完整角变量 \(\rho_x\) 的运输

这里必须使用 Ozuch Definition 1.14 的点态角映射，而不能把 \(\rho_x\) 换成常向量。

对源节点的正手征插入 \(\omega_2^+\)，角向反自对偶形式为
\[
\Theta^-(x)=\sum_j\rho^-_j(x)\omega_j^-.
\]
由于 \(q\omega_j^-=s_j\omega_j^+\)，其中
\[
(s_1,s_2,s_3)=(-1,1,1),
\]
自然性给出
\[
q_*\Theta^-(x)=\Theta^+(qx),
\]
即
\[
\rho^+(qx)=S\rho^-(x).
\]
于是利用 \(r(qx)=r(x)\) 以及
\[
q_*(A\circ B)=(q_*A)\circ(q_*B),
\]
得到逐点恒等式
\[
q_*H_+^4(x)=H_-^4(qx),
\]
等价地
\[
L^*H_-^4=H_+^4.
\]

因此 Step 81 的角向运输结论是精确代数恒等式。JSON 中 20,000 个样本的零误差与此一致，但数学依据是上述二形式运输和 \(\rho_x\) 的协变性；采样本身不替代该推导。

---

## 3. 接收尺度 \(t_i\) 必须保留

Ozuch 的参数写作
\[
\zeta_j=t_j\phi_j,\qquad t_j=|\zeta_j|.
\]
由 Proposition 1.16 的 EH 渐近式，
\[
H^4(t_j\phi_j)=t_j^2H^4(\phi_j),
\]
因为 \(\rho_x\) 对 \(\zeta\) 线性，而 \(H^4\) 对两个 \(\zeta\) 因子二次齐次。

节点 \(j\) 的奇异源经过投影伪逆和奇异部分扣除后，在另一节点 \(i\) 产生正则二次射流，量级为 \(t_j^2\)。Ozuch 第一投影对接收节点曲率变化线性，而有限维方程本身具有
\[
t_i\lambda_i+t_i^2\mu_i
\]
的尺度结构。因此该正则射流给出
\[
t_i\,\delta\lambda_i
=t_it_j^2\,\mathcal I_{ij}.
\]

所以候选三次项应写成
\[
F_i(t_1,t_2)
=t_i\sum_jB_{ij}t_j^2+R_i.
\]
写成 \(\sum_jB_{ij}t_j^3\) 在 \(i\ne j\) 时漏掉了接收泡尺度。两尺度恰好相等时二者都呈现 \(t^3\)，所以只有多尺度记账才能看出差异。

这仍未证明三次项是首个非零径向项。Ozuch 当前给出的
\[
t_i\lambda_i+t_i^2\mu_i=O(t_{\max}^{5/2})
\]
在可比尺度下比 \(t^3\) 大：
\[
t^{5/2}/t^3=t^{-1/2}\to\infty.
\]
故该估计无法提取 \(B\)。

---

## 4. \(L\) 对 \(B\) 的约束及正尺度核

若近似度量、补空间修正和投影均按 \(L\) 等变方式构造，则完整约化映射满足
\[
F_2(t_1,t_2)=F_1(t_2,t_1).
\]
若三次部分存在且写作
\[
F_1=t_1(at_1^2+bt_2^2)+o\!\left(t_1(t_1^2+t_2^2)\right),
\]
则
\[
F_2=t_2(bt_1^2+at_2^2)+o\!\left(t_2(t_1^2+t_2^2)\right),
\]
从而
\[
B=\begin{pmatrix}a&b\\ b&a\end{pmatrix}.
\]

若另一轨道的径向投影改乘固定非零常数 \(\kappa\)，矩阵字面形式会改变；把第二方程除以 \(\kappa\) 后，零点问题仍回到上述交换矩阵。以 \(L\)-运输的核张量和相同 \(L^2\) 归一化时，\(\kappa=1\)。

令
\[
x=t_1^2>0,\qquad y=t_2^2>0.
\]
首项方程为
\[
ax+by=0,\qquad bx+ay=0.
\]
相加得到
\[
(a+b)(x+y)=0.
\]
因为 \(x+y>0\)，正尺度首项零点必有
\[
a+b=0.
\]
若 \(a=-b\ne0\)，两式进一步给出
\[
x=y,\qquad t_1=t_2.
\]
若 \(a=b=0\)，整个三次矩阵消失。

因此，在 \(L\) 的参数交换协变性已经固定后，不存在额外的“不等正尺度比符号问题”：非零 \(B\) 的正核只能是等尺度方向。Step 81 中关于一般两尺度正核比例的句子只适用于尚未使用 \(L\) 关系的一般 \(2\times2\) 矩阵。

若所需小余项估计成立，则还可得到：

- \(a+b\ne0\)：没有足够小的正尺度零点，而不仅是没有等尺度零点；
- \(a+b=0,\ a\ne0\)：任何候选正尺度分支都必须渐近满足 \(t_1/t_2\to1\)；
- \(a=b=0\)：需计算下一齐次层。

---

## 5. 数值系数 \(a,b\) 成为几何量前尚缺的内容

### 5.1 同轨道项不只是局部自响应

以接收节点 \(NN\) 为例，\(a\) 至少包含：

- \(NN\) 本节点的局部下一径向响应；
- 同一 \(A\)-轨道伙伴 \(SS\) 的正则 Green 响应；
- 两个轨道一源共同激发的全局补空间响应。

而 \(b\) 包含来自 \(NS,SN\) 两个节点的响应。若 \(F_i\) 定义为轨道内两个节点投影之和，还会出现统一的轨道重数因子。计算文件必须明确 \(F_i\) 是单节点投影、轨道平均还是轨道总和。

### 5.2 对数项可能先于常系数矩阵出现

Ozuch Remark 2.11 明确指出 \(H_4^4\) 通常含有 \(\log r\)。匹配尺度依赖 \(t_i,t_j\) 时，空间对数可能产生
\[
t_it_j^2\log t_j,\qquad
t_i^3\log t_i
\]
等项。这些项的绝对值大于纯 \(t^3\) 项。因而需要先确定实际的多齐次—对数展开；若对数投影不消失，首个径向对象将是依赖 \(\log t\) 的交换矩阵，而不是常数 \(B\)。

### 5.3 shape 模态进入同一三次层

Step 77 已给出
\[
P(g_1-g_2)=-\Lambda(g_1-g_2).
\]
该模态为 \(A,J,L\)-偶，虽然不是核，却可被二次 EH 源以 \(O(t_j^2)\) 激发。解补空间方程所得的 shape 响应会改变各节点曲率二次射流，再经接收因子 \(t_i\) 进入 \(B\)。整体尺度、迹模态以及 Einstein 常数的归一化响应也需在同一切片中处理。

### 5.4 规范分解只对总系数有意义

局部 EH 下一项、奇异扣除后的 Green 自响应、DeTurck 修正和截断匹配项可以随坐标及参数化重新分配。真正稳定的对象是完整 Lyapunov–Schmidt 投影的总系数。Step 77 已展示过一个具体先例：原始正规坐标中的 \(-\pi^2/18\) 标量配对被 Bianchi 坐标修正精确抵消。

### 5.5 等变补空间求解

要使
\[
F_2(t_1,t_2)=F_1(t_2,t_1)
\]
成为完整约化映射的恒等式，以下数据需同时保持 \(L\)：

- EH 坐标与径向截断；
- DeTurck 参考度量；
- 核、余核及补空间投影；
- 补空间逆算子的选择；
- 两轨道径向核张量的归一化。

有限群平均可产生这样的等变选择。否则原始坐标系中的系数可能不呈现交换形式，尽管几何零点集仍具有交换协变性。

### 5.6 尺度域需明确

余项
\[
o\!\left(t_i(t_1^2+t_2^2)\right)
\]
最自然地先在可比尺度域
\[
\eta\le t_1/t_2\le\eta^{-1}
\]
上统一建立。若 \(t_1/t_2\to0\) 或 \(\infty\)，接收泡退化速度与源泡不同，需要另行给出多尺度展开，不能直接由 \(O(t_{\max}^{5/2})\) 推出。

---

## 与 Yau 第 26 题的关系

这一计算研究的是一个特定正 Einstein orbifold 附近、具有 \(A,J,L\) 对称性的混合手征 EH 退化。

- 若得到 \(a+b\ne0\) 并建立上述余项估计，它排除的是这一局部等变、可比尺度退化机制，不能排除同一光滑流形上远离该 orbifold 的 Einstein 度量。
- 若得到 \(a+b=0\)，只说明等尺度方向通过这一阶方程，仍需下一径向项、补空间一致逆估计和非线性闭合。
- 即使最终构造出该四维流形上的正 Einstein 度量，也只是一个具体存在结果，并未处理 Yau 第 26 题中的任意闭流形及仅依赖维数的 Ricci 夹逼常数。
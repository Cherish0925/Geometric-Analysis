# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 81,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step81_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step81_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 81 refinement of the positive mixed-row product-orbifold construction. User goal is Yau Problem 26; this is only a local positive-Einstein desingularization test. Read the notes/data and check: (1) the single-factor antipodal L(x,y)=(-x,y) really descends to the quotient, exchanges the two A-orbits, reverses 4D orientation, and swaps the plus/minus EH chiralities compatibly with the diagonal mixed assignment; (2) L transports the J-fixed radial direction omega2 with the stated sign and is compatible with the full angular H^4/rho_x formula, not a frozen-rho shortcut; (3) the surviving radial finite-dimensional response should be recorded as F_i=t_i sum_j B_ij t_j^2+R_i rather than sum_j B_ij t_j^3; (4) L symmetry constrains the candidate B matrix to [[a,b],[b,a]] only after fixing transported radial normalizations and does not force positive-scale balance; (5) identify any missing sign, normalization, order, self/cross-response, logarithmic, gauge, or shape-mode issue that must be handled before a real coefficient calculation can support or obstruct an Einstein desingularization.

## Integrated Scientific Memo

# Step 81 核验结论

Step 81 的主体修正成立，但需补强两点：

1. \(L\)-交换对称性不仅要求运输 \(\omega _2\)，还必须运输并同范数归一化完整的 EH 径向核/余核张量及投影泛函；
2. 在
   \[
   B=\begin{pmatrix}a&b\\ b&a\end{pmatrix}
   \]
   已成立后，非零 \(B\) 的正尺度核只能是等尺度方向。Step 81 所说的“一般正比例符号问题”不再存在。

---

## 1. \(L\) 的下降、轨道交换和手征运输

令
\[
\mathcal O=(S^2\times S^2)/\langle\sigma\rangle,\qquad
\sigma=(r_\pi,r_\pi),
\]
并令 \(L=(\ell,\mathrm{id})\)，其中 \(\ell\) 是第一球面上交换 \(N,S\) 的反足等距变换。因为 \(\ell r_\pi=r_\pi\ell\)，故
\[
L\sigma=\sigma L,
\]
所以 \(L\) 确实下降为 \(\mathcal O\) 的 orbifold 等距变换；局部群 \(-I_4\) 也与 \(DL\) 对易。

节点作用为
\[
NN\mapsto SN,\quad SS\mapsto NS,\quad
NS\mapsto SS,\quad SN\mapsto NN,
\]
因而
\[
\{NN,SS\}\longleftrightarrow\{NS,SN\}.
\]
对角混合赋值
\[
\epsilon(s_1,s_2)=s_1s_2
\]
满足 \(\epsilon(Lp)=-\epsilon(p)\)，即 \(L\) 同时交换两个 \(A\)-轨道和 EH 手征。

在源、靶节点的相容定向积框架中可写
\[
DL=q=\operatorname{diag}(1,-1,1,1),\qquad \det q=-1.
\]
因此 \(L\) 反转四维定向，并交换 \(\Lambda^+\) 与 \(\Lambda^-\)。直接计算给出
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
故 \(S=\operatorname{diag}(-1,1,1)\) 是 \(\Lambda^\pm\) 间的基变换矩阵，并且
\[
S\operatorname{diag}(1,0,0)S^T=\operatorname{diag}(1,0,0).
\]
这证明秩一曲率块和混合手征赋值相容。

径向插入方向的二形式符号确为
\[
\omega_2^+\mapsto+\omega_2^-.
\]
为了固定约化方程的投影符号，还应使用 EH 参数族自然性
\[
L^*\operatorname{eh}_{t\omega_2^-}
=\operatorname{eh}_{t\omega_2^+}
\]
并对 \(t\) 微分，从而得到
\[
L^*\mathbf o_{\rm rad}^-=\mathbf o_{\rm rad}^+.
\]
这才将正号从插入二形式提升到完整径向核张量。若两端采用相同 \(L^2\) 或同一 flux 归一化，则投影运输因子为 \(+1\)。仅验证 \(\omega _2\) 本身不足以固定任意独立选择的余核归一化。

---

## 2. 完整角向 \(H^4\) 运输成立

必须使用 Ozuch Definition 1.14 的完整角映射，而不是冻结 \(\rho\)。设
\[
\Theta^-(x)=\sum_j\rho_j^-(x)\omega_j^- .
\]
由二形式的自然运输，
\[
q_*\Theta^-(x)=\Theta^+(qx),
\]
所以
\[
\rho^+(qx)=S\rho^-(x),\qquad
S=\operatorname{diag}(-1,1,1).
\]
又因为 \(r(qx)=r(x)\) 且
\[
q_*(\alpha\circ\beta)=(q_*\alpha)\circ(q_*\beta),
\]
可逐点推出
\[
q_*H_+^4(x)=H_-^4(qx),
\]
等价于
\[
L^*H_-^4=H_+^4.
\]

因此 JSON 中的零采样误差与一个精确代数恒等式一致；真正的证明是上述协变性，而不是随机采样。Step 81 没有重犯冻结 \(\rho\) 的错误。

---

## 3. 正确的尺度账本

Ozuch 的有限维方程具有
\[
t_i\lambda_i+t_i^2\mu_i
\]
的接收节点尺度结构。另一方面，EH 远场满足
\[
H^4(t_j\phi_j)=t_j^2H^4(\phi_j).
\]
节点 \(j\) 的 \(H^4\) 源经投影伪逆、奇异部分扣除及 Green 运输，在节点 \(i\) 产生量级 \(t_j^2\) 的正则二次射流；它修正接收节点的一阶曲率障碍，因此贡献为
\[
t_i\,\delta\lambda_i=t_it_j^2\mathcal I_{ij}.
\]
所以候选三次层必须写成
\[
\boxed{
F_i(t_1,t_2)
=t_i\sum_jB_{ij}t_j^2+R_i
}
\]
而不是
\[
\sum_jB_{ij}t_j^3.
\]
后者在交叉项中漏掉接收尺度；只有在 \(t_1=t_2\) 时二者才偶然都呈 \(t^3\)。

目前仍不能断言这就是首个真实非零层。源文只给出
\[
t_i\lambda_i+t_i^2\mu_i=O(t_{\max}^{5/2}),
\]
而在可比尺度下 \(t^{5/2}\gg t^3\)，故该估计无法提取任何三次系数。

---

## 4. \(L\) 对 \(B\) 的约束及正尺度结论

在完整拼接、DeTurck 规范、补空间逆和径向投影均 \(L\)-等变，且两轨道采用 \(L\)-运输归一化时，
\[
F_2(t_1,t_2)=F_1(t_2,t_1).
\]
若纯三次主部存在，则
\[
F_1=t_1(at_1^2+bt_2^2)+\cdots,\qquad
F_2=t_2(bt_1^2+at_2^2)+\cdots,
\]
故
\[
\boxed{
B=\begin{pmatrix}a&b\\ b&a\end{pmatrix}.
}
\]
若第二轨道的径向泛函另乘固定常数，这一字面矩阵形式会相应改变；重新按 \(L\) 运输归一化后才恢复上述形式。

对 \(t_i>0\)，令 \(x=t_1^2>0,\ y=t_2^2>0\)。主部方程是
\[
ax+by=0,\qquad bx+ay=0.
\]
相加得
\[
(a+b)(x+y)=0.
\]
所以任何正尺度主部零点都要求
\[
a+b=0.
\]
进一步：

- 若 \(a+b\ne0\)，没有正尺度主部核；
- 若 \(a=-b\ne0\)，必有 \(x=y\)，即 \(t_1=t_2\)；
- 若 \(a=b=0\)，整个候选三次矩阵消失，必须计算下一层。

因此，Step 81 中关于一般两尺度正核比例的表述应修正：一旦 \(L\) 已把矩阵约束为交换形式，非零 \(B\) 不存在不等正尺度核。对称性本身仍然既不推出 \(a+b=0\)，也不推出 Einstein 解。

若进一步证明统一余项
\[
R_i=o\!\left(t_i(t_1^2+t_2^2)\right)
\]
（至少在可比尺度锥上），则 \(a+b\ne0\) 将排除所有充分小的正尺度零点，而不只是等尺度零点；若 \(a=-b\ne0\)，任何候选分支必须满足 \(t_1/t_2\to1\)。

---

## 5. 真正计算 \(a,b\) 前必须解决的事项

### (a) 轨道和自/交响应定义

必须说明 \(F_i\) 是单节点投影、轨道平均还是轨道总和。以轨道 \(\{NN,SS\}\) 为例，“自系数” \(a\) 不只是同一节点的局部响应，还包括：

- 本节点局部下一径向项；
- 同轨道另一节点的正则 Green 响应；
- 两个节点共同激发的全局补空间响应。

\(b\) 则汇总另一轨道两个节点的交叉响应。轨道重数和平均因子必须统一进入 \(a,b\)。

### (b) 对数项和真实渐近次序

Ozuch Remark 2.11 明确指出 \(H_4^4\) 通常含 \(\log r\)。匹配尺度代入后可能出现
\[
t_i^3\log t_i,\qquad t_it_j^2\log t_j
\]
或混合对数项，它们比纯 \(t^3\) 更大。必须先建立多齐次—对数展开；若对数投影不消失，首要对象不是常数矩阵 \(B\)，而是依赖 \(\log t\) 的交换响应矩阵。

### (c) shape 模态

\[
P(g_1-g_2)=-\Lambda(g_1-g_2)
\]
且该模态为 \(A,J,L\)-偶。它不是障碍核，但可被 \(O(t_j^2)\) 源激发，其补空间解会改变节点曲率二次射流，因而在乘以接收尺度后直接进入 \(a,b\)。同时它使不变补空间上的算子不定；需要一致可逆性，不能依赖正定性。

### (d) 标量核、规范与归一化

四个 \(u_i g_j\) 模态属于 Ozuch 的完整 \(L^2\) 核。\(A\)-奇性可使等变残差对它们的完整投影恒为零，但这要求完整拼接和规范精确 \(A\)-等变，而不只是局部二阶配对消失。Step 77 已显示原始正规坐标中的 \(-\pi^2/18\) 配对被 Bianchi 修正抵消；因此局部、Green、cutoff 和 gauge 部分本身不具不变量意义，只有完整 Lyapunov–Schmidt 投影的总系数才可作为 \(a,b\)。

整体尺度、迹方向和 Einstein 常数的归一化也必须在同一切片中固定，否则会改变径向方程的代表。

### (e) 完整等变性

要得到精确恒等式
\[
F_2(t_1,t_2)=F_1(t_2,t_1),
\]
以下选择都必须同时保持 \(A,J,L\)：

- EH 坐标与截断函数；
- DeTurck 参考度量；
- 核、余核和补空间投影；
- 补空间逆算子的选择；
- 两轨道径向核张量及 flux/\(L^2\) 归一化。

尤其 \(L\) 交换正负 EH 手征，需实际构造这种跨手征等变拼接，而不能只验证节点线性模型。

### (f) Green 相互作用

交叉系数不是 \(H^4\) 的点值，也不是两个 \(S^2\) 静态 Green 函数的乘积。需要计算的是切片后的 multipole-to-curvature 映射
\[
\mathcal C_{ij}^{\epsilon}
=
D R_{p_i}^{\epsilon}
\!\left[
G_P^\perp(I-\Pi_{\mathbf O})\mathcal S_{j,\phi_j}
\right],
\]
使用完整乘积算子的伪逆及其加性谱分母。奇异扣除发生在源/自节点；不同接收节点处是正则射流评价。

### (g) 余项和多尺度域

至少应在
\[
\eta\le t_1/t_2\le\eta^{-1}
\]
上证明统一的
\[
F_i=t_i\sum_jB_{ij}t_j^2+
o\!\left(t_i(t_1^2+t_2^2)\right),
\]
或给出真实的幂—对数替代式。若 \(t_1/t_2\to0\) 或 \(\infty\)，需要单独的多尺度分析，不能从当前 \(O(t_{\max}^{5/2})\) 估计外推。

---

## 最终判定

Step 81 对事项 (1)–(4) 的核心结论正确：

- \(L\) 确实下降、交换两个 \(A\)-轨道、反转四维定向并交换手征；
- \(\omega _2\) 以正号运输，完整角向 \(\rho_x/H^4\) 也精确协变；
- 正确账本是 \(t_i\sum_jB_{ij}t_j^2\)；
- 在运输归一化后 \(B=[[a,b],[b,a]]\)，但对称性不迫使 \(a+b=0\)。

必要修正是：完整径向核张量和投影归一化的正号仍须显式写入证明；而在交换矩阵形式成立后，非零 \(B\) 的正核只能是等尺度方向。当前最精确的未决对象是：在完整等变切片和足够尖锐的幂—对数展开中，首个非零等尺度径向投影系数究竟是纯三次的 \(a+b\)、三次对数系数，还是因进一步抵消而出现在更高阶。
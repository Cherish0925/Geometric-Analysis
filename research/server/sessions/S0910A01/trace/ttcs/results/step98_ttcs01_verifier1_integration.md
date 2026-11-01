# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 98,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step98_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step98_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematical content and logical soundness of the Step 98 trace obstruction theorem for the product-orbifold Ozuch desingularization. The key claims to verify are:

1. SAME-CHIRALITY VANISHING: B_{++} = B_{--} = 0 for all spectral sectors and pairs. The argument is that B_ee = -B_oo exactly (verified computationally) and cross-parity blocks vanish by K-symmetry. Is this a structural identity or a numerical coincidence? Is there a representation-theoretic reason that same-chirality pairs should give zero response?

2. TRACE OBSTRUCTION: The AB sector gives cross-chirality trace c0 = 4a ≈ 0.1258 for adjacent pairs. For the mixed pattern, this sums to 0.503 t^2 at equal scales. The argument that this is a genuine obstruction relies on: (a) self-terms are pattern-independent, (b) all-same has zero inter-node trace (by B_same=0), (c) KE existence implies self-trace is solvable independently. Does this argument work? Are there loopholes?

3. TRACE VS P/Q: The claim that the trace channel is independent of the P/Q (traceless) channel and that the trace obstruction alone suffices. Is this correct in the Ozuch framework?

4. The P/Q channel structure: NN←NS has pure Q (anti-holomorphic from AA tensor on factor A), while NN←SN has pure P (holomorphic from BB tensor on factor B). Is this consistent with the product structure and chirality conventions?

## Integrated Scientific Memo

# Step 98 核验结论

## 总判断

现有材料**没有证明**所声称的 “Step 98 trace obstruction theorem”。它可靠地给出了一个有限谱模型中的、混合手性相对全同手性的**节点间响应计算**；其中 AB 部分为正的各向同性响应，AA/BB 部分为较小的无迹响应。但从该计算到 Ozuch 反解奇点不存在性，仍缺少结构恒等式、完整模态、完整约化方程及余项控制。

此外，Step 98 §5 的迹系数有明确的二倍计数错误：

\[
\operatorname{tr}A_{\rm NN}^{\rm inter}=8a\,t^2
 \approx0.25154\,t^2,
\]

而不是 \(0.50308\,t^2\)。定理 §6(b) 中的符号系数 \(8a\) 才与前述定义一致。

---

## 1. \(B_{++}=B_{--}=0\)：目前是数值现象，不是已证明的结构恒等式

由脚本采用的 Hadamard 变换，

\[
\begin{aligned}
B_{ee}&=\tfrac14(B_{++}+B_{+-}+B_{-+}+B_{--}),\\
B_{eo}&=\tfrac14(B_{++}-B_{+-}+B_{-+}-B_{--}),\\
B_{oe}&=\tfrac14(B_{++}+B_{+-}-B_{-+}-B_{--}),\\
B_{oo}&=\tfrac14(B_{++}-B_{+-}-B_{-+}+B_{--}).
\end{aligned}
\]

若 \(B_{eo}=B_{oe}=0\)，则

\[
B_{++}=B_{--}=B_{ee}+B_{oo},\qquad
B_{+-}=B_{-+}=B_{ee}-B_{oo}.
\]

因此 \(B_{ee}=-B_{oo}\) 与 \(B_{++}=B_{--}=0\) 在此条件下是**等价命题**，不是后者的独立解释。\(K\)-对称性至多解释交叉奇偶块消失；它本身并不迫使 \(B_{ee}=-B_{oo}\)。

通常的乘积等变性允许非零映射，例如

\[
M\longmapsto \operatorname{tr}(M)I_K
\]

以及 \(\operatorname{Sym}^2_0(K)\) 上的 spin-2 映射，故没有一般表示论原则禁止同手性响应。要把数值零提升为恒等式，必须给出额外的手性反演对称，或逐模态证明

\[
B_{++}^{(\ell_t,\ell_s,\mathrm{polarization})}=0.
\]

### 计算覆盖范围也不足以支持 “所有谱扇区”

`step98_full_chirality_tensor_maps.py` 对 AA/BB 只构造了

\[
H_{abmn}=T_{ab}\,(\nabla^2 f)_{mn}
\]

这一类稀疏 tensor–scalar Hessian 数据。Step 96 自己明确指出，完整 electric/magnetic tensor jets、低模、变形模、投影器与标架运动尚未纳入。因此“AB、AA、BB 所有谱扇区”的说法过强。

此外：

- 计算是浮点热正则化谱和；
- \(\tau\) 与 \(L_{\max}\) 同时变化；
- 没有 \(\tau\to0\)、\(L_{\max}\to\infty\) 的误差界；
- 脚本没有直接记录未经舍入的 \(\|B_{ee}+B_{oo}\|\) 或 \(\|B_{++}\|\) 证书。

故当前最准确的表述是：

> 在已实现的 AB/AA/BB 截断模型及所测试参数下，观察到同手性块为机器精度零；尚无结构证明或完备谱证明。

---

## 2. AB 迹归一化与 Step 98 的二倍错误

Step 96 给出相邻节点 AB 块

\[
B^{AB}_{ee}=aJ,\qquad B^{AB}_{oo}=-aJ,
\qquad J(M)=\operatorname{tr}(M)I_K,
\]

其中 \(a\simeq0.0314425\)。于是交叉手性块为

\[
B^{AB}_{+-}=B_{ee}-B_{oo}=2aJ.
\]

对物理源

\[
M_j=t_j^2u_ju_j^T,\qquad \operatorname{tr}M_j=t_j^2,
\]

有

\[
A^{AB}_{ij}=2a\,t_j^2I_K,
\qquad
\operatorname{tr}A^{AB}_{ij}=4a\,t_j^2.
\]

NN 的两个相邻交叉手性源因此贡献

\[
\operatorname{tr}A_{\rm NN}^{\rm inter}
=4a(t_{\rm NS}^2+t_{\rm SN}^2).
\]

等尺度时：

\[
\boxed{\operatorname{tr}A_{\rm NN}^{\rm inter}
=8a\,t^2\approx0.25154\,t^2.}
\]

Step 98 §5 将表中的 \(c_0=4a\) 又乘了一个矩阵迹因子 \(2\)，得到 \(16a\,t^2\)，属于重复计数。

这也与 Step 97 的物理径向量一致。单个相邻源给出

\[
u_i^TA_{ij}^{AB}u_i=2a\,t_j^2,
\]

两个等尺度相邻源给出 \(4a\,t^2\)；若 Ozuch obstruction one-form 还带接收端因子 \(t_i\)，则最终为

\[
4a\,t^3\simeq0.12577\,t^3.
\]

因此 \(t^2\) 是矩阵 \(A_i\) 的量级，\(t^3\) 是乘入接收泡尺度后的投影方程量级；最终定理必须明确使用哪一个对象，并据此比较余项。

---

## 3. “KE 存在 \(\Rightarrow\) 自项可独立解掉”不成立

完整首阶方程应至少具有形式

\[
F_i^\varepsilon(p)
=
F_i^{\rm self}(p)
+F_i^{\rm deform,\varepsilon}(p)
+\sum_{j\ne i}B_{ij}^{\varepsilon_i\varepsilon_j}(M_j)
+R_i^\varepsilon(p),
\]

其中 \(p\) 包含尺度、方向、背景变形、标架及修正参数。

即使接受全同手性节点间项为零，某个全同手性 KE 退化族也只会给出

\[
F_i^{\rm self}(p_{\rm KE})
+F_i^{\rm deform,+}(p_{\rm KE})
+R_i^+(p_{\rm KE})=0
\]

在该特定参数族上成立。它不推出：

1. 自相互作用单独为零；
2. 自项与变形项对所有尺度恒等为零；
3. 混合手性解必须使用相同参数；
4. 变形项投影到 \(R^+\) 与 \(R^-\) 后仍与手性无关。

而且给定资料没有证明已知的 \(\mathrm{Bl}_5\mathbb P^2\) KE 度量确实构成退化到这个特定乘积 orbifold、并匹配当前 Ozuch 参数化的族。仅知道同一光滑流形上存在某个 KE 度量，不足以校准这套局部胶合方程。

所以当前差分计算最多证明：

> 在同一组尺度、方向和背景参数处，混合模式相对于全同模式增加了所计算的节点间矩阵。

它不能排除在另一组尺度或变形参数处由自项/背景项抵消。

要获得真正 obstruction，至少需要证明下列之一：

\[
\operatorname{tr}\bigl(F_i^{\rm self}+F_i^{\rm deform}\bigr)
\equiv0
\]

在相关阶上恒等成立；或者证明迹方向属于**完整调整算子的余核**，因而所有允许的尺度、背景和投影器变化都不能生成相反迹项。

---

## 4. 迹与 \(P/Q\)：表示分解独立，但物理方程并不逐分量独立

作为表示空间，

\[
\operatorname{Sym}^2(K)
=
\mathbb RI_K\oplus \operatorname{Sym}^2_0(K)
\]

确实分解为一维迹表示和二维 spin-2 表示。AB 为纯迹、AA/BB 为无迹，属于有意义的代数观察。

但 Step 97 指出实际接收方程是

\[
A_i u_i=0,
\]

等价于径向和角向投影，而不一定要求整个矩阵 \(A_i=0\)。若

\[
A=\frac X2I+
\frac12
\begin{pmatrix}
Y&Z\\
Z&-Y
\end{pmatrix},
\qquad u=(\cos\theta,\sin\theta),
\]

则

\[
u^TAu
=
\frac12\bigl(X+Y\cos2\theta+Z\sin2\theta\bigr).
\]

因此无迹 \(P/Q\) 项可以在**径向方程**中抵消迹项。非零迹足以排除 \(A=0\)，但不能单独排除 \(Au=0\)；非零迹矩阵完全可能有核。

### 现有数值实际上支持一个更强、也更合适的相对结论

按照 Step 98 报告的系数，相邻块可写成

\[
A_{\rm NS}=2a\,t_{\rm NS}^2I+T_Q,\qquad
A_{\rm SN}=2a\,t_{\rm SN}^2I+T_P,
\]

并且

\[
\|T_Q\|=|Q|t_{\rm NS}^2,\qquad
\|T_P\|=|P|t_{\rm SN}^2.
\]

取

\[
2a\simeq0.062885,\qquad |P|=|Q|\simeq0.00800,
\]

则对任意源角和接收角，

\[
u^TA_{\rm inter}u
\ge
(2a-|Q|)t_{\rm NS}^2+
(2a-|P|)t_{\rm SN}^2>0.
\]

等尺度时下界约为

\[
0.10977\,t^2.
\]

所以，在已计算的节点间模型中，混合模式的相对矩阵其实是**一致正定**的；这比“迹非零”更适合物理方程 \(A_iu_i=0\)。但它仍可能被未计算的自项、背景变形项或其他谱块抵消，故尚不是完整 obstruction。

附带地，实线性映射

\[
\xi\mapsto P\xi+Q\bar\xi
\]

的行列式确为

\[
|P|^2-|Q|^2,
\]

非零核当且仅当 \(|P|=|Q|\)。因此 Step 98 对 A02 的该项修正是正确的。

---

## 5. AA/BB 的 \(P/Q\) 结构

以下支持模式与乘积分离相容：

- AA 只在 \(NN\leftarrow NS\) 非零，即源与接收端共享 A 因子极点；
- BB 只在 \(NN\leftarrow SN\) 非零，即共享 B 因子极点；
- \(NN\leftarrow SS\) 在所选 tensor–scalar 模态中没有 AA/BB 响应；
- 两个非零系数绝对值相同，符合 A/B 因子交换对称。

但“AA 必为 \(Q\)、BB 必为 \(P\)”不是当前资料中的不变量结论。若核平面标架作保向旋转，\(P,Q\) 仅改变相位；若源端或接收端标架含反射，则全纯和反全纯标签会互换。Step 97 明确说节点标架传输尚未固定，而 Step 98 脚本没有实现 \(U_{ij}\) 传输。

故目前可确认的是：

> 一个相邻方向出现一个纯 spin-2 通道，另一个因子交换方向出现其共轭对应通道，绝对值均约 \(0.008\)。

绝对命名 “AA=\(Q\)、BB=\(P\)” 仍依赖未固定的方向、复结构和手性约定。

---

## 可成立的修正版结论

现有证据支持如下受限陈述：

> 在脚本所包含的热正则化 AB/AA/BB 模态模型中，同手性节点间块数值上为零。对棋盘式混合手性，两个相邻节点产生 AB 各向同性正响应，并伴随较小的 AA/BB 无迹响应。报告系数下，其相对节点间矩阵对所有角度正定；等尺度矩阵迹为
> \[
> 8a\,t^2\approx0.25154\,t^2.
> \]
> 这是一项有力的候选首阶相对 obstruction，但尚未证明为完整 Ozuch obstruction。

将其升级为定理所缺的精确对象是：

1. \(B_{++}=0\) 的逐模态或对称性恒等式；
2. 完整 tensor jets、低模、变形模、投影器和标架运动；
3. 显式节点标架传输；
4. 热正则化谱和的极限与误差界；
5. 包含自项及所有调整参数的完整首阶投影方程；
6. 迹/正定方向属于完整调整算子余核的证明；
7. \(t^2\) 矩阵与 \(t^3\) 物理 obstruction 的统一归一化；
8. 严格小于首项的 Ozuch/Biquard 余项估计。

因此 Step 98 当前应视为**数值发现的正定相对节点间机制**，而不是已核验的反解奇点阻碍定理。
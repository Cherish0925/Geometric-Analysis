# O11阈值TT恒等式的独立核验及无TT投影的扩展

## 1. 核验结论

`O11_Threshold_Variation.md` 的(4.1)正确。Weyl系数为−4，非Einstein项E:H²的系数为−8，有序Cotton范数前为2。沿仿射路径g+tH求导时，必须保留逆度量配对的导数；该项正是产生正确E:H²系数所需的一部分。

## 2. 对所有无迹H的精确公式

设闭四流形s=-4，E=Ric+g，H是任意光滑对称无迹二张量，不要求div H=0。定义
\[
b_i=\nabla^jH_{ij},\quad \phi=\langle E,H\rangle,
\quad \psi=\nabla^ib_i-\phi=Ds_g[H],
\quad C(H)_{ijk}=\nabla_kH_{ij}-\nabla_jH_{ik}.
\]
则沿仿射路径g+tH有
\[
\boxed{D^2S[H,H]
=2\int\psi^2+2\int|C(H)|^2-4\int|b|^2
+\frac83\int|H|^2-4\int W(H,H)-8\int E:H^2.}\tag{T1}
\]

**证明。** 记I=∫s，V=Vol，\(\mathcal H=I+2V\)。在s=-4处
\[
D^2S[H,H]=2\int(Ds[H])^2-8D^2\mathcal H[H,H].
\]
\(\mathcal H\)的协变梯度为−Ric+(s/2+1)g=−E。微分梯度、逆度量收缩和体积（最后一项因tr H=0消失），得
\[
D^2\mathcal H
=-\int\langle D Ric[H],H\rangle-\int|H|^2+2\int E:H^2.
\]
Ricci线性化在无迹张量上为
\[
D Ric[H]=\tfrac12(\nabla^*\nabla H+Ric\circ H+H\circ Ric-2Rm(H))
+\operatorname{sym}\nabla b.
\]
因此
\[
D^2\mathcal H=-\tfrac12\int|\nabla H|^2+
\int Rm(H,H)+\int|b|^2+\int E:H^2.
\]
一次交换协变导数给出一般化Cotton恒等式
\[
\tfrac12\int|C(H)|^2
=\int|\nabla H|^2-\int|b|^2-\int Rm(H,H)+\int Ric:H^2.
\]
再使用
\[
Rm(H,H)=W(H,H)+\tfrac13|H|^2-E:H^2
\]
可得
\[
D^2\mathcal H=-\tfrac14\|C(H)\|_2^2+\tfrac12\|b\|_2^2
+\tfrac12\int W(H,H)-\tfrac13\|H\|_2^2+\int E:H^2.
\]
乘−8并加2∥ψ∥²₂即(T1)。令b=0恢复原稿TT公式。

## 3. 独立背景检验

### 实双曲四维背景

常曲率−1/3时E=W=0。TT公式成为
\[
D^2S=2\|C(H)\|_2^2+\tfrac83\|H\|_2^2.
\]
这与负Einstein的TT变分吻合。

### 两个曲率−1曲面的乘积

在一个因子的Teichmüller方向上，H是TT且Codazzi，E=0，W(H,H)=2|H|²/3，故D²S=0。

取另一方向H=g_1−g_2，则H平行TT，|H|²=4，Rm(H,H)=−4，W(H,H)=−16/3。公式给D²S=32V。直接计算
\[
s(g+tH)=-4/(1-t^2),\quad dV_{g+tH}=(1-t^2)dV_g,
\quad S(g+tH)=16V/(1-t^2)
\]
同样得32V。

### 非Einstein常标量乘积：检查−8 E:H²

令两因子曲率κ_1+κ_2=−2，且κ_1≠κ_2。E在第一因子为a g_1，a=κ_1+1。取第一因子的Teichmüller方向H，仍有C(H)=0和W(H,H)=2|H|²/3。因此公式给
\[
D^2S[H,H]=-8a\|H\|_2^2.
\]
也可沿保持该因子曲率和面积的非线性Teichmüller路径直接检验：S沿该路径恒定，面积二阶约束给∫tr(g_1'')=∫|H|²，DS=8∫⟨E,\cdot⟩，故仿射Hessian恰为−8a∥H∥²。此检验独立确认了容易漏掉的非Einstein系数。

## 4. 直接绕过TT投影

在实际平衡族上，设ξ=(w_3^++w_3^-−1/3)_+，已有∫ξ²=O(Q)。于是(T1)给
\[
D^2S\ge2\|\psi\|_2^2+2\|C(H)\|_2^2+\tfrac43\|H\|_2^2
-4\|\operatorname{div}H\|_2^2-\int(4\xi+8|E|)|H|^2.
\]
使用阈值泛函F=P−γS的弱稳定性，得到
\[
\boxed{D^2P[H,H]\ge
\gamma\{2\|Ds[H]\|_2^2+2\|C(H)\|_2^2+\tfrac43\|H\|_2^2
-4\|\operatorname{div}H\|_2^2\}
-C(\varepsilon+\sqrt h)Q.}\tag{T2}
\]
对满足幅度和临界预算的任意无迹H成立。

只要\(\|\operatorname{div}H\|_2^2=o(A)\)，其额外散度惩罚乘γ=O(h)就是o(Q)。因此无须实际求解可能失控的TT投影，就可在这类试验上保留原TT结论的一阶尺度内容。

## 5. 与自适应resolvent的关系

`O11_Descent_or_Recovery.md` 的自适应试验满足
\[
\|H\|_2^2+\|\nabla H\|_2^2+\|\nabla^*\nabla H\|_2^2=O(Q),
\quad\|H\|_\infty\le C.
\]
因此散度项是O(Q)，当然是o(A)。进一步结合实际Weyl预算，该文件新增推论(A3+)给出全部临界导数预算O(Q)。所以
\[
|D^2S[H,H]|=O(Q),\qquad\gamma D^2S[H,H]=o(Q).
\]
这使其成为无需TT投影的合法非共形试验，却同时说明：阈值泛函相对于P的二阶修正，在这类局部化试验上不是新的Q主项。

一般bulk TT方向可以有∥H∥²或导数预算为O(A)，其γD²S可以是O(Q)。两者的规模不同，没有矛盾。

现阶段未证明任何具体自适应H使DF出现Q尺度的非零量或D²F出现Q尺度负量。已解决“是否可构造合法非共形试验且绕过TT投影”，尚未解决“该试验必然给出下降”。不把两个结论混同。

# O11：阈值泛函的二阶修正与手术尺度上的TT稳定性

2026-09-29。直接依据新附件 `O10_O11_Direct_Work_20260929(1).md` 第2–5节、整合稿的两手性预算、实际 Weyl 偏离预算和Cotton恒等式。本文件给出新的二阶推导，不声称已决定O11最佳系数。

## 1. 两种近极小序列不是同一个变分问题

记
\[
 p_j=\inf_gP(g),\quad \alpha_j=\inf_g\mathcal E(g),\quad
 F_j(g)=R(g)-\frac{S(g)}{4-\alpha_j},\quad
 k_j=\frac{\alpha_j}{4(4-\alpha_j)}.
\]
这里的 \(k_j\) **仅在本文件表示泛函系数，不表示吹起个数**。为避免与原族的手术记号混淆，以下改记此系数为
\[
 \gamma_j:=\frac{\alpha_j}{4(4-\alpha_j)}=O(h_j).
\]
因为 \(R=P+S/4\)，精确关系是
\[
 \boxed{F_j=P-\gamma_jS.}\tag{1.1}
\]

上一轮选择的是任意精度的 \(P\)-近极小度量。本附件选择的是任意精度的 \(\mathcal E\)-近极小度量；在其负Yamabe代表上，\(F_j\ge0\) 且其值接近零。后一列只满足
\[
 P(g_j)-p_j=O(A_jh_j^2),
\]
不能把它自动当作达到上一轮任意更小 \(P\)-误差的同一列。

下文的 \(g_j\) 一律是新附件的阈值泛函选择，均为 \(s=-4\)，并满足
\[
 R=8\pi^2A_j+O(Q_j),\quad V=2\pi^2A_j+O(Q_j),
 \quad P=O(Q_j),\quad Q_j=A_jh_j.
\tag{1.2}
\]

## 2. 四阶Taylor选择可以在更大的临界测试类上一致成立

使用集合
\[
 \mathcal T_j=\left\{H:\ \|H\|_{\infty,g_j}\le1,
 \quad \int\bigl(|\nabla^2H|^2+|\nabla H|^4\bigr)\le A_j\right\}.
\tag{2.1}
\]
它比新附件中的临界范数单位球大，能容纳在正体积比例区域中同时进行的变化，以及许多微观区域的合并测试。

对于 \(g_t=g_j+tH\)，\(|t|\le1/4\)，联络差的精确公式是
\[
 (\nabla^{g_t}-\nabla^{g_j})^k{}_{ab}
 =\frac t2(g_t)^{kc}
 (\nabla_aH_{bc}+\nabla_bH_{ac}-\nabla_cH_{ab}).
\]
求 \(t\) 导数不会增加 \(H\) 的空间微分阶数。\(F_j\) 的二、四阶导数均由
\[
 C\int\left(|\operatorname{Ric}_{g_j}|^2+
                 |\nabla^2H|^2+|\nabla H|^4\right)
\]
控制，因而对 \(H\in\mathcal T_j\) 一致为 \(O(A_j)\)。可以直接使用Ricci差式，不必控制 \(\nabla\operatorname{Rm}\)。

由 \(F_j\ge0\) 和可任意精确选择
\[
 \mathcal E(g_j)-\alpha_j\le\varepsilon_j^2h_j^2,
 \qquad\varepsilon_j\downarrow0,
\]
可得 \(F_j(g_j)\le CA_j\varepsilon_j^2h_j^2\)。新附件的两侧Taylor计算于是对整个 \(\mathcal T_j\) 仍成立：
\[
 \boxed{|DF_j[H]|\le C\varepsilon_jQ_j,\qquad
 D^2F_j[H,H]\ge-C\varepsilon_jQ_j.}\tag{2.2}
\]
第二式使用对称四阶余项与 \(t=\sqrt{\varepsilon_jh_j}\)。这不是把原范数右侧形式地删掉，而是重新用总临界预算 \(A_j\) 控制Taylor余项。

## 3. 一阶修正确实是低阶；二阶修正一般不是

令 \(E=\operatorname{Ric}+g=\operatorname{Ric}^{\circ}\)，因为 \(s=-4\)。闭流形上的标量平方一阶变分是
\[
 DS_g[H]=8\int\langle E,H\rangle.
\]
故由(1.1)与(2.2)，对 \(H\in\mathcal T_j\)，
\[
 |DP[H]|
 \le C\varepsilon_jQ_j+8\gamma_j\sqrt P\,\|H\|_2
 \le C(\varepsilon_j+\sqrt{h_j})Q_j=o(Q_j).
\tag{3.1}
\]
这里用 \(\|H\|_2\le\sqrt V\)、\(P=O(Q_j)\)。

但二阶精确关系是
\[
 \boxed{D^2P[H,H]=D^2F_j[H,H]+\gamma_jD^2S[H,H].}\tag{3.2}
\]
在(2.1)的测试类中只能先得到 \(|D^2S|=O(A_j)\)，所以修正可以是 \(O(Q_j)\)。若把它无条件写成 \(o(Q_j)\)，会丢掉正是O11研究的一阶尺度。

以下在真实TT测试方向上控制其符号，并保留可能的正贡献。

## 4. 常负标量度量上标量平方Hessian的精确TT恒等式

设 \(g\) 是任意闭四流形上的 \(s=-4\) 度量，\(H\) 是真实TT张量：
\[
 \operatorname{tr}_gH=0,\qquad\nabla^iH_{ij}=0.
\]
定义
\[
 C(H)_{ijk}=\nabla_kH_{ij}-\nabla_jH_{ik},\quad
 \phi=\langle E,H\rangle,
 \quad E:H^2=E_{ij}H^i{}_kH^{kj}.
\]
Cotton型张量采用全部有序指标的张量范数。曲率收缩为
\(\operatorname{Rm}(H,H)=R_{ikjl}H^{ij}H^{kl}\)，Weyl同样约定。

**命题。** 沿仿射路径 \(g+tH\)，有
\[
 \boxed{
 D^2S_g[H,H]
 =2\int\phi^2+2\int|C(H)|^2
  +\frac83\int|H|^2
  -4\int W(H,H)-8\int E:H^2.
 }\tag{4.1}
\]
不要求 \(g\) 是Einstein或任何泛函的临界点。

**证明。** 令
\[
 I(g)=\int s_g,\qquad\mathcal H(g)=I(g)+2V(g).
\]
对所有度量有
\[
 S(g)=\int(s_g+4)^2\,dV_g-8\mathcal H(g).
\]
在 \(s=-4\) 处，TT条件给 \(Ds[H]=-\phi\)，因此
\[
 D^2S[H,H]=2\int\phi^2-8D^2\mathcal H[H,H].\tag{4.2}
\]
\(\mathcal H\) 的协变张量梯度为
\(-\operatorname{Ric}+(s/2+1)g\)，在当前度量等于 \(-E\)。对该梯度、逆度量收缩和体积因子同时微分，TT条件给出
\[
 D^2\mathcal H[H,H]
 =-\int\langle D\operatorname{Ric}[H],H\rangle
       -\int|H|^2+2\int E:H^2.
\]
取 \(\nabla^*\nabla\) 为正的粗糙Laplacian，TT上的Ricci线性化是
\[
 D\operatorname{Ric}[H]
 =\tfrac12\{\nabla^*\nabla H+\operatorname{Ric}\circ H
             +H\circ\operatorname{Ric}-2\operatorname{Rm}(H)\}.
\]
故
\[
 D^2\mathcal H[H,H]
 =-\tfrac12\int|\nabla H|^2
                 +\int\operatorname{Rm}(H,H)+\int E:H^2.
\tag{4.3}
\]
积分分部、交换一次协变导数并用 \(\operatorname{div}H=0\)，得到
\[
 \tfrac12\int|C(H)|^2
 =\int|\nabla H|^2-\int\operatorname{Rm}(H,H)
                              +\int\operatorname{Ric}:H^2.
\tag{4.4}
\]
四维曲率分解在无迹 \(H\) 上给
\[
 \operatorname{Rm}(H,H)
       =W(H,H)+\tfrac13|H|^2-E:H^2.
\tag{4.5}
\]
将(4.4)代入(4.3)，再代入(4.5)，得到
\[
 D^2\mathcal H[H,H]
 =-\tfrac14\int|C(H)|^2+\tfrac12\int W(H,H)
                   -\tfrac13\int|H|^2+\int E:H^2.
\]
与(4.2)合并即(4.1)。证毕。

常曲率 \(-1/3\) 时该式为
\(D^2S=2\|C(H)\|_2^2+(8/3)\|H\|_2^2\)，与负Einstein的TT二阶计算一致。两个曲率 \(-1\) 曲面的乘积上，因子上的Teichmüller核满足 \(C(H)=0\)、\(W(H,H)=(2/3)|H|^2\)，式中各项相消为零；这也核对了Weyl系数与有序Cotton范数。

## 5. 实际两手性预算将不定项降为 \(o(Q)\)

记 \(w_3^\pm\) 为两个Weyl算子的最大特征值，令
\[
 \xi=(w_3^++w_3^- -1/3)_+.
\]
标准四维代数识别 \(S_0^2T^*\cong\Lambda^+\otimes\Lambda^-\) 给
\[
 W(H,H)\le(w_3^++w_3^-)|H|^2
                   \le(1/3+\xi)|H|^2.
\tag{5.1}
\]
原平衡族的同一实际解预算已经给出
\[
 \int\xi^2\le\frac89\mathcal B_j,
 \qquad
 \mathcal B_j=P+2\pi^2A_j\{U_j-1-h_j-2(p/A_j-1)\}
 \le P+O(A_jh_j^2)=O(Q_j).
\tag{5.2}
\]
这里 \(p\ge A_j\) 是实际类的自对偶投影平方；\(\mathcal B_j\) 对应整合稿中的 \(D_2/18+3\int|W^-|^2\)，避免与测试张量 \(H\) 混淆。

把(5.1)代入(4.1)，得
\[
 D^2S[H,H]\ge
 2\|\phi\|_2^2+2\|C(H)\|_2^2+\frac43\|H\|_2^2
       -\int(4\xi+8|E|)|H|^2.
\tag{5.3}
\]
若 \(\|H\|_\infty\le1\)，则(1.2)、(5.2)给出
\[
 \int(4\xi+8|E|)|H|^2
 \le(4\|\xi\|_2+8\|E\|_2)\|H\|_4^2
 \le C\sqrt{A_jQ_j}.
\tag{5.4}
\]
这是 \(S\) Hessian的误差；它未必是 \(o(Q)\)。但乘以 \(\gamma_j=O(h_j)\) 后，
\[
 \gamma_j\sqrt{A_jQ_j}=O(Q_j\sqrt{h_j})=o(Q_j).
\]

将(5.3)–(5.4)与(2.2)、(3.2)合并，得到本轮新增结论：

**阈值选择的TT二阶强制。** 对所有 \(H\in\mathcal T_j\) 且为TT的测试，统一成立
\[
 \boxed{
 D^2P_{g_j}[H,H]\ge
 \gamma_j\left\{2\|\langle E,H\rangle\|_2^2
            +2\|C(H)\|_2^2+\frac43\|H\|_2^2\right\}
       -C(\varepsilon_j+\sqrt{h_j})Q_j.
 }\tag{5.5}
\]
这保留了 \(O(Q)\) 的正二阶支付，没有把 \(\gamma_jD^2S\) 错当成消失项。所需Weyl信息来自实际场与双手性预算，而不是对一般曲率张量假设点态复双曲夹逼。

## 6. 最佳首项进入了一个新的必要谱约束，但尚未被决定

沿子列设
\[
 \alpha_j/h_j\to c\in(0,4].
\]
则 \(\gamma_j/h_j\to c/16\)。由(5.5)，对上述允许TT测试有
\[
 \frac{D^2P[H,H]}{Q_j}\ge
 \left(\frac c8+o(1)\right)
       \frac{\|C(H)\|_2^2+\|\langle E,H\rangle\|_2^2}{A_j}
 +\left(\frac c{12}+o(1)\right)\frac{\|H\|_2^2}{A_j}
 -o(1).
\tag{6.1}
\]
因为测试幅度及临界预算可保证各右侧范数比有界，这个重写保留了统一误差。特别是，在一个正体积比例上有非零幅度的允许TT变化，不能在 \(P\) 的二阶变分中完全没有手术尺度的支付。

这个方向的信息不能自行推出 \(c\ge4\)：较小的 \(c\) 要求的支付也较小。若要用它决定最佳首项，需要从实际拓扑或场结构构造一个具体允许TT方向，并计算其二阶变分与右侧支付的差，使其出现严格负的 \(Q\) 量；或得到足够强的反向结构约束。目前没有构造出这样的方向。

## 7. 当前结论与仍缺少的关键步骤

本轮已经证明：

- \(F\)-选择与任意精度 \(P\)-选择的区别；一阶差是 \(o(Q)\)，二阶差必须保留。
- 新附件的四阶Taylor选择可以扩到总临界预算 \(A_j\) 的测试集。
- 任意负常标量度量上精确的TT标量平方Hessian恒等式。
- 借助已证实际Weyl预算，阈值近稳定性强迫(5.5)的正二阶支付，误差为 \(O((\varepsilon_j+\sqrt h_j)Q_j)\)。

仍未证明O11最佳首项；没有把(5.5)登记为最优系数定理。下一段实质缺口已经具体化：须得到满足临界预算的真实非共形TT测试，并使它违反该二阶支付或产生一阶下降。实际 \(E=\operatorname{Ric}^{\circ}\) 虽然在常标量情况下为TT，但其点态幅度及临界二阶导数预算尚无统一控制，因此不能直接将 \(H=E\) 代入后宣布矛盾。

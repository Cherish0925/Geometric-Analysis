# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 90,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step90_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step90_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the K-symmetry argument for the product orbifold (S^2 x S^2)/Z_2 desingularization. K(z,w) = (bar(z), w) is complex conjugation on the first sphere, identity on the second. The central claims to verify are:

1. K fixes all four A_1 nodes (NN, NS, SN, SS), has tangent DK = diag(1,-1,1,1), det = -1, and commutes with sigma, A, J.

2. K^* maps omega_2^+ to omega_2^- with sign +1, hence exchanges the positive and negative Eguchi-Hanson models at each node.

3. Cross-parity vanishing: if S_j^1 = (S_j^+ - S_j^-)/2 is K-odd and L_i^0 is K-even, then L_i^0 G_tau S_j^1 = 0 for ALL node pairs (i,j), including diagonal. This eliminates all even-odd and odd-even interactions.

4. Geometric annihilation: q = g_A - g_B is K-even (because K preserves both metrics), hence K-parity orthogonality gives <S_j^1, q> = 0 at the full geometric level, not just the flat V_2 level. Similarly for the four scalar Ozuch zero modes.

5. The relative mixed-minus-all-same interaction reduces to off-diagonal odd-odd terms only. Diagonal odd-odd terms vanish by epsilon_i^2 - 1 = 0. No singular self-subtraction is needed.

Critically examine: (a) whether the Bianchi correction and gauge terms in the Ozuch construction respect K-equivariance, (b) whether there could be additional negative TT modes in the K-odd sector beyond the known K-even mode q, (c) the exact mechanism by which K acts on the linearized curvature functional (receiver).

## Integrated Scientific Memo

# K-对称性核验结论

## 1. 基础几何与手征交换

令
\[
K(z,w)=(\bar z,w).
\]
复共轭固定 \(\mathbb{CP}^1\) 的 \(0,\infty\)，故 \(K\) 逐点固定四个节点
\[
NN,\ NS,\ SN,\ SS.
\]
在每个节点取适配正交标架，可写
\[
DK=\operatorname{diag}(1,-1,1,1),\qquad \det DK=-1.
\]
因此 \(K\) 反转四维乘积定向，并交换 \(\Lambda^2_+\) 与 \(\Lambda^2_-\)。它与给定的 \(\sigma,J\) 对易；与 \(A\) 的对易性在数据中通过计算记录，若采用分支中所写的对角 antipodal 定义也可直接验证，但正式文本应明确 \(A\) 的定义。

取
\[
\begin{aligned}
\omega_1^\pm&=e^{01}\pm e^{23},\\
\omega_2^\pm&=e^{02}\mp e^{13},\\
\omega_3^\pm&=e^{03}\pm e^{12},
\end{aligned}
\]
则
\[
K^*\omega_1^+=-\omega_1^-,
\qquad
K^*\omega_2^+=\omega_2^-,
\qquad
K^*\omega_3^+=\omega_3^-.
\]
故 SD 到 ASD 的传输矩阵为
\[
\operatorname{diag}(-1,1,1),
\]
特别是
\[
K^*\omega_2^+=\omega_2^-
\]
确实具有正号。

对已给出的 \(H^4\) 公式，数值采样并非主要证据；矩阵恒等式已经给出严格代数证明。若
\[
K C_{2j}K=t_jC_{j2},\qquad(t_1,t_2,t_3)=(-1,1,1),
\]
则必须同时变换自变量和张量：
\[
\begin{aligned}
(K^*H_+^4)(x)
&=K H_+^4(Kx)K\\
&=-\frac12\sum_j
  (x^TKC_{2j}Kx)\,KC_{2j}K\\
&=-\frac12\sum_j t_j^2
  (x^TC_{j2}x)C_{j2}
 =H_-^4(x).
\end{aligned}
\]
同样的数据支持 \(K^*O_1^+=O_1^-\)。

这严格证明了首个 ALE 多极项和核模式的交换。要把它提升为“完整 Eguchi–Hanson 度量的交换”，还需明确相容的 ALE 标记与提升 \(\widetilde K\)，并验证
\[
\widetilde K^*\operatorname{eh}_{\omega_2^+}
=\operatorname{eh}_{\omega_2^-}.
\]
标准 \(O(4)\)-自然标记下该式应成立，但现有材料只显式验证了 \(H^4,O_1\)，没有展示完整标记图。

---

## 2. receiver 的精确变换机制

令 \(U=K^*\)，并记
\[
A_2=\Lambda^2(DK_{p_i}).
\]
因为曲率及其线性化是自然算子，且背景度量 \(\bar g\) 为 \(K\)-不变，
\[
D\mathcal R_{\bar g}[Uh]
=A_2^{-1}D\mathcal R_{\bar g}[h]A_2.
\]
定义节点 \(p_i\) 的径向 receiver
\[
L_i^\pm(h)
=
\frac{\langle\omega_2^\pm,
D\mathcal R_{\bar g}[h]\omega_2^\pm\rangle}
{|\omega_2^\pm|^2}.
\]
由 \(A_2\omega_2^+=\omega_2^-\) 得
\[
L_i^+(Uh)=L_i^-(h),\qquad
L_i^-(Uh)=L_i^+(h).
\]
因此
\[
L_i^0=\frac{L_i^++L_i^-}{2},\qquad
L_i^1=\frac{L_i^+-L_i^-}{2}
\]
满足
\[
L_i^0U=L_i^0,\qquad L_i^1U=-L_i^1.
\]
这就是 receiver 奇偶性的非循环证明：它来自线性化曲率的自然性和 \(\omega_2^+\leftrightarrow\omega_2^-\)，不是预设的“内积奇偶性”。

即使在其他相容标架中 \(\omega_2^+\) 的传输带负号，该符号在二次曲率收缩中出现两次，也不会改变 \(L^+\leftrightarrow L^-\) 的结论。

---

## 3. 所有节点对的交叉奇偶消失

Ozuch 源满足
\[
S_j^+(Uh)=S_j^-(h),\qquad
S_j^-(Uh)=S_j^+(h),
\]
其中边界配对使用的是 Riemann 密度，故不会因 \(K\) 反定向而额外产生符号。于是
\[
US_j^0=S_j^0,\qquad US_j^1=-S_j^1.
\]

背景 Lichnerowicz 算子 \(P\) 与 \(U\) 对易。若
\[
G_\tau=f_\tau(P)(I-\Pi_{\ker P})
\]
是热核或谱正则化，且核补空间取 \(K\)-不变正交补，则
\[
UG_\tau=G_\tau U.
\]
因此，对任意有序节点对 \((i,j)\)，
\[
\begin{aligned}
L_i^0G_\tau S_j^1
&=L_i^0UG_\tau S_j^1
 =L_i^0G_\tau US_j^1\\
&=-L_i^0G_\tau S_j^1=0,
\end{aligned}
\]
同理
\[
L_i^1G_\tau S_j^0=0.
\]

由于 \(K\) 固定每个节点而非置换节点，这个结论适用于所有 \(i,j\)，特别包括 \(i=j\)。对角交叉项在每个 \(\tau>0\) 时已经恒为零，不涉及取极限，也无需局部奇异自项消减。

这里的精确适用对象是由 \(K\)-不变奇异 orbifold 背景构造的线性 pairwise Green 问题。固定手征向量 \(\epsilon\) 的完整粘合度量通常并不为 \(K\)-不变；实际上
\[
K^*\widetilde g_\epsilon=\widetilde g_{-\epsilon}.
\]
故高阶非线性、多源乘积项必须另行作奇偶分解，不能无条件归入单节点公式 \(S_j^0+\epsilon_jS_j^1\)。

---

## 4. Bianchi 修正与 gauge：自然性成立，但具体实现尚未完全核验

在 \(K\)-不变背景上，自然算子满足
\[
\mathcal B_{\bar g}(Uh)=U\mathcal B_{\bar g}(h),\qquad
\delta_{\bar g}^*(U\alpha)=U\delta_{\bar g}^*\alpha.
\]
所以
\[
(\mathcal B_{\bar g}\delta_{\bar g}^*)U
=U(\mathcal B_{\bar g}\delta_{\bar g}^*).
\]
由节点距离构造的径向 cutoff
\[
\chi(d_{\bar g}(p_i,\cdot))
\]
也为 \(K\)-不变。谱逆、正交投影和相对于 \(K\)-不变背景唯一归一化的 Bianchi/DeTurck 解均保持 \(K\)-等变。

但若要宣称特定 Ozuch/Biquard 实现的“完整几何源”已被核验，还缺少以下显式兼容性：

1. 局部标记图满足
   \[
   K\circ\Phi_i^+=\Phi_i^-\circ\widetilde K;
   \]
2. 核补空间、中心固定和 frame normalization 为 \(K\)-不变；
3. \(H_2^4\)、\(V_{l,0},V_{l,2}\)、frame correction 及 gauge vector field 均按上述规则交换。

现有材料严格覆盖 \(H^4,O_1\)，但没有展示这些后续对象。若第一 obstruction 消失并按 Ozuch 选择 \(H_2^4=0\)，该缺口在对应零模边界项中缩小；它仍不能替代完整 chart/gauge 核验。

因此：

- **orbifold-reference 线性层面的交叉奇偶消失是成立的；**
- **对完整 Ozuch 几何源的同一结论是以这些自然、等变选择为条件成立，现有工件尚未完全落实该条件。**

---

## 5. \(q\) 与四个标量零模的几何消失

因为 \(K\) 分别保持两个因子度量，
\[
K^*q=K^*(g_A-g_B)=q.
\]
高度函数 \(Z_A,Z_B\) 也为 \(K\)-不变，故
\[
Z_Ag_A,\quad Z_Ag_B,\quad Z_Bg_A,\quad Z_Bg_B
\]
全部为 \(K\)-偶。

只要完整源确实满足 \(US_j^1=-S_j^1\)，则对任意上述偶模 \(\psi\)，
\[
\langle S_j^1,\psi\rangle
=\langle US_j^1,U\psi\rangle
=-\langle S_j^1,\psi\rangle=0.
\]
因此它们的配对在完整几何层面消失，而不仅是平坦 \(V_2\) 主部。

不过应严格区分两层结论：

- 平坦主部消失已由完整 100 维 Hessian 基计算验证；
- 完整几何消失依赖上一节尚待落实的全构造 \(K\)-等变性。

---

## 6. \(K\)-奇 TT 扇区是否还有非正模

分支给出了一个可将“开放问题”实质关闭的乘积谱分解。将 upstairs 对称张量写为
\[
h=f g_A+k_A+m+\ell g_B+k_B,
\]
其中 \(k_A,k_B\) 是各自因子块内无迹张量，\(m\) 为混合块。在单位球乘积上，给定约定
\[
P=\frac12\nabla^*\nabla-\mathring R
\]
下有
\[
\begin{aligned}
P(fg_A)&=\left(\frac12\Delta f-f\right)g_A,\\
Pk_A&=\frac12\nabla^*\nabla k_A+k_A,\\
Pm&=\frac12\nabla^*\nabla m,
\end{aligned}
\]
另一个因子同理。

由此可见负谱只能来自常数 scalar-block 系数；在 TT 子空间中唯一对应方向为
\[
q=g_A-g_B,\qquad Pq=-q,
\]
而 \(q\) 为 \(K\)-偶。商空间中标量本征值 \(2\) 的下降函数为 \(Z_A,Z_B\)，它们也是 \(K\)-偶，并产生所列四个零模。

在 \(K\)-奇、商空间下降的扇区：

- scalar-block 系数的允许标量本征值至少为 \(4\)，故 \(P\ge1\)；
- 无迹因子块满足 \(P\ge1\)；
- 混合块的 rough-Laplacian 本征值至少为 \(2\)，故同样 \(P\ge1\)。

因而在这些乘积谱公式和商下降条件下，
\[
\boxed{P|_{\text{\(K\)-odd quotient tensors}}\ge1,}
\]
特别地 \(K\)-奇 TT 扇区没有额外的负模或零模；轴向 Killing–Killing 模以本征值 \(1\) 达到下界。

这一加强结论需要在正式证明中补入球面标量、1-form 与无迹 2-tensor 的低谱下界及 \(\sigma\)-下降奇偶条件，不能仅引用模式 census。即便 \(P\ge1\)，它也**不能**决定离对角 Green 值或最终相对和的符号。

---

## 7. 相对作用确实只剩离对角奇–奇项

原响应分解为
\[
\mathcal R_\epsilon(\tau)=
\sum_{i,j}a_ib_j
\left(
K_{ij}^{00}+\epsilon_jK_{ij}^{01}
+\epsilon_iK_{ij}^{10}
+\epsilon_i\epsilon_jK_{ij}^{11}
\right),
\]
其中
\[
a_i=t_i,\qquad b_j=t_j^2.
\]
减去 all-plus 配置并利用
\[
K_{ij}^{01}=K_{ij}^{10}=0
\]
后，
\[
\Delta_\epsilon(\tau)
=\sum_{i,j}a_ib_j(\epsilon_i\epsilon_j-1)
K_{ij}^{11}(\tau).
\]
对 \(i=j\)，
\[
\epsilon_i^2-1=0,
\]
所以
\[
\boxed{
\Delta_\epsilon(\tau)
=\sum_{i\ne j}a_ib_j(\epsilon_i\epsilon_j-1)
K_{ij}^{11}(\tau).
}
\]
每个 receiver 节点与 source 节点分离，故相应 Green 解在 receiver 附近平滑。以同一正则化先形成相对量后取 \(\tau\downarrow0\)，不需要奇异自项 subtraction。

这只适用于当前线性 pairwise \(O(t_i t_j^2)\) 层。完整非线性高阶项可能具有 \(\epsilon_j\epsilon_k\) 等新手征结构，须另行分析。

最后，\(P\) 在奇扇区正定并不赋予上述离对角和确定符号：去掉对角后的 Green 矩阵一般不是正半定，且权重 \(t_i t_j^2\) 非对称。现有轴向 \(\lambda=1\) 通道给出正的特定贡献，但不能控制全部奇谱通道。

## 最终判定

中心命题 1–3 及 5 在 \(K\)-不变 orbifold-reference 线性构造中成立；receiver 奇偶性由线性化曲率自然性严格推出。命题 4 在完整几何层面成立的逻辑也是正确的，但仍以特定 Ozuch/Biquard chart、Bianchi 归一化及高阶径向数据的 \(K\)-等变实现为待核验输入。乘积谱分解进一步表明 \(K\)-奇 TT 扇区没有额外非正模，实际有 \(P\ge1\)；然而这不决定最终离对角相互作用的符号。
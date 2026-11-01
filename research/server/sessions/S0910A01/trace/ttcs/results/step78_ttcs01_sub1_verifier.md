# TTCS Independent Branch Record

```json
{
  "step_id": 78,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step78_equivariant_diagonal_reduction.md",
    "Sessions/S0910A01/workspace/data/step78_equivariant_construction.json",
    "Sessions/S0910A01/workspace/data/step78_rank_one_orthogonality.json",
    "Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md"
  ]
}
```

## Task

Verify the three structural theorems for the A-equivariant diagonal reduction of the Einstein desingularization of (S^2 x S^2)/Z_2, and check the order analysis.

1. SCALAR KERNEL ELIMINATION: The simultaneous antipodal A(x,y)=(-x,-y) is orientation-preserving, commutes with sigma, and acts on product harmonics as (-1)^{l1+l2}. The four scalar P-kernel modes u_i*g_j have l_total=1 (odd), so are A-odd. An A-invariant residual is orthogonal to them. Check this carefully: is it really true that A is orientation-preserving in 4D? That it commutes with sigma? That l1+l2=1 for the kernel modes?

2. SCALAR DECOUPLING: For in-kernel zeta in span{omega_2,omega_3}, compute omega_k^+ circ omega_l^- for k,l in {2,3} in the standard product frame. Verify they all have zero trace on each S^2 factor. Therefore H^4(zeta) has zero scalar-sector coupling. Note the contrast: omega_1^+ circ omega_1^- = -(g1-g2), which IS scalar. So only in-kernel directions decouple from scalars.

3. ORDER ANALYSIS: The Ozuch necessary conditions give t^2*mu_k = O(t^{5/2}), so mu_k -> 0. The inter-node Green response contributes at O(t^3). Since 5/2 < 3, we have t^{5/2} >> t^3 for small t. Check: is this comparison correct? Does it really mean the inter-node term is BELOW the remainder? If so, the leading reduced equation is simply mu_k(alpha) = 0 at each orbit, with no inter-node coupling.

4. RANK-ONE ORTHOGONALITY: R^- = diag(Lambda,0,0) and rho(zeta)^- = (0,cos alpha,sin alpha) for in-kernel zeta. Verify R^- * rho(zeta)^- = 0. Verify the curvature modification dR^- is block-diagonal (entries (1,2) and (1,3) are zero). Does this suggest all mu_k vanish? What caveats apply?

Be precise about any errors in the reasoning.

## Output

# 独立核验备忘

## 总结

1. **\(A\)-对称消去四个标量核投影是成立的。**  
   \(A\) 在每个 \(S^2\) 上反转取向，在四维乘积上保持取向；它与 \(\sigma\) 交换。四个核张量确实分别具有次数 \((1,0)\) 或 \((0,1)\)，因而都是 \(A\)-奇。只要近似度量、规范选择和节点粘合数据确实按 \(A\) 配对，其 Einstein 残差与这四个核张量严格正交。

2. **\(H^4\) 与 \(f g_1,f g_2\) 的直接耦合为零，但 Step 78 的证明需要修正。**  
   所列二形式复合的分因子迹均为零。事实上，即使 \(\rho(\zeta)^-\) 含有 \(\omega_1^-\) 分量，只要 \(\zeta^+\in\operatorname{span}\{\omega_2^+,\omega_3^+\}\)，分因子迹仍然为零。因此结论比笔记中的计算更稳固，但等式
   \[
   \rho(\zeta)^-=c\omega_2^-+s\omega_3^-
   \]
   本身未由给出的文件证明，并且若 \(\rho\) 是通常依赖径向方向的映射，则一般不能这样固定其分量。

3. **阶数比较正确。**  
   对可比较尺度，\(t_i^2\mu_{i,k}=O(t_{\max}^{5/2})\) 给出 \(\mu_{i,k}=O(t_{\max}^{1/2})\)。交互项 \(t_i t_j^2\mathcal I_{ij,k}\) 是 \(O(t_{\max}^3)=o(t_{\max}^{5/2})\)，所以现有 Ozuch 估计看不到它。由此只能得到二阶系数方程 \(\mu_{i,k}=0\)；不能由此断言三阶交互在实际方程中不存在。

4. **秩一代数恒等式在指定前提下成立，但不能推出所有 \(\mu_k\) 都为零。**  
   若固定基底中确有 \(\rho(\zeta)^-=(0,c,s)\)，则 \(R^-\rho(\zeta)^-=0\)，且所写 \(dR^-\) 严格分块。然而 \(dR^-\rho(\zeta)^-=8\rho(\zeta)^-/r^6\neq0\)，并且 \(R^-dR^-\neq0\)。因此只有显式含 \(R^-\rho(\zeta)^-\) 的项自动消失；\(\mu_2,\mu_3\) 仍需完整公式。

---

## 1. \(A\)-对称与标量核

### 四维取向

在偶维球面 \(S^2\) 上，反足映射的次数为
\[
\deg(-\mathrm{id}_{S^2})=(-1)^{2+1}=-1.
\]
因此它在每个因子上反转取向。乘积映射
\[
A=(-\mathrm{id}_{S^2})\times(-\mathrm{id}_{S^2})
\]
的次数为
\[
\deg A=(-1)(-1)=+1.
\]
所以 \(A\) 在 \(S^2\times S^2\) 上保持四维乘积取向。

这里不能只看切空间中的形式矩阵 \(-I_2\) 的行列式；\(T_xS^2\) 与 \(T_{-x}S^2\) 的取向由相反的外法向量定义，这正是单个反足映射取向反转的来源。

### 与 \(\sigma\) 交换

将
\[
r_\pi=\operatorname{diag}(-1,-1,1)\in SO(3),\qquad
A_{S^2}=-I_3
\]
视为 \(\mathbb R^3\) 中的线性映射，则
\[
(-I_3)r_\pi=r_\pi(-I_3).
\]
故
\[
A\sigma=\sigma A.
\]
因此 \(A\) 降到商 orbifold 上。由于 \(A\) 保持四维取向，它也保持 \(\Lambda^+\oplus\Lambda^-\) 分解，故不会交换 EH 手性。

### 谐波次数与核张量

球谐函数满足
\[
A_{S^2}^*Y_{l,m}=(-1)^lY_{l,m}.
\]
故乘积谐波满足
\[
A^*(Y_{l_1,m_1}Y_{l_2,m_2})
=(-1)^{l_1+l_2}Y_{l_1,m_1}Y_{l_2,m_2}.
\]

轴向一次谐波 \(u_1\) 只依赖第一个因子，所以次数是 \((1,0)\)；\(u_2\) 的次数是 \((0,1)\)。由于 \(A^*g_j=g_j\)，
\[
A^*(u_i g_j)=-u_i g_j.
\]
因此四个张量
\[
u_1g_1,\quad u_1g_2,\quad u_2g_1,\quad u_2g_2
\]
确实都是 \(A\)-奇。

若残差 \(E\) 为 \(A\)-不变张量，而 \(K\) 是其中任一核张量，则 \(A\) 是保体积的等距映射，故
\[
\langle E,K\rangle_{L^2}
=\langle A^*E,A^*K\rangle_{L^2}
=\langle E,-K\rangle_{L^2}
=-\langle E,K\rangle_{L^2}.
\]
所以
\[
\langle E,K\rangle_{L^2}=0.
\]

这里“两个配对节点使用同一角度”应理解为
\[
\zeta_{A(p)}=A_*\zeta_p.
\]
若两个节点使用各自任意选取的局部框架，相同的数值 \(\alpha\) 未必自动表达这个传输关系。

---

## 2. \(H^4\) 的分因子无迹性

取乘积正交标架 \((e_1,e_2,e_3,e_4)\)，前两个方向属于第一个球面。采用未归一化基底
\[
\begin{aligned}
\omega_1^+&=e^{12}+e^{34},&
\omega_1^-&=e^{12}-e^{34},\\
\omega_2^+&=e^{13}-e^{24},&
\omega_2^-&=e^{13}+e^{24},\\
\omega_3^+&=e^{14}+e^{23},&
\omega_3^-&=e^{14}-e^{23}.
\end{aligned}
\]
把二形式视为斜对称端同态。自对偶和反自对偶端同态彼此交换，其乘积是对称端同态。直接乘法给出
\[
\omega_2^+\circ\omega_2^-
=
\operatorname{diag}(-1,1,-1,1),
\]
\[
\omega_3^+\circ\omega_3^-
=
\operatorname{diag}(-1,1,1,-1),
\]
以及
\[
\omega_2^+\circ\omega_3^-=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&0&-1\\
0&0&-1&0
\end{pmatrix},
\]
\[
\omega_3^+\circ\omega_2^-=
\begin{pmatrix}
0&-1&0&0\\
-1&0&0&0\\
0&0&0&-1\\
0&0&-1&0
\end{pmatrix}.
\]
因此每个矩阵都满足
\[
T_{11}+T_{22}=0,\qquad T_{33}+T_{44}=0.
\]
归一化二形式只会为这些矩阵加入统一常数因子。

作为对照，
\[
\omega_1^+\circ\omega_1^-
=\operatorname{diag}(-1,-1,1,1)
=-(g_1-g_2),
\]
所以 \(\omega_1\) 方向确实含有乘积形状张量。

### 对 \(\rho\) 的修正

Step 78 使用了
\[
\rho(\zeta)^-=c\omega_2^-+s\omega_3^-.
\]
这一等式并非证明分因子无迹性所必需。事实上，直接计算也给出
\[
\operatorname{tr}_{g_1}(\omega_a^+\circ\omega_1^-)
=
\operatorname{tr}_{g_2}(\omega_a^+\circ\omega_1^-)=0,
\qquad a=2,3.
\]
所以对任意 \(\eta^-\in\Lambda^-\)，都有
\[
\operatorname{tr}_{g_1}(\eta^-\circ\zeta^+)
=
\operatorname{tr}_{g_2}(\eta^-\circ\zeta^+)=0
\]
只要
\[
\zeta^+\in\operatorname{span}\{\omega_2^+,\omega_3^+\}.
\]
因此即便 \(\rho_{\hat x}(\zeta)^-\) 随角变量 \(\hat x\) 转动并出现 \(\omega_1^-\) 分量，\(H^4\) 的这一分因子无迹结论仍成立。

于是，在平坦乘积模型中，
\[
\langle H^4,f g_k\rangle
=f\,\operatorname{tr}_{g_k}H^4=0,\qquad k=1,2,
\]
这是逐点恒等式，不仅是球面平均为零。

这里应精确区分两种表述：

- 对所有纯迹乘积张量 \(f g_1,f g_2\)，直接耦合确实为零；
- 若“标量扇区”还包括由 Hessian 生成的无迹张量，则上述迹计算本身没有涵盖那些张量；
- 截断、移植和 Bianchi 修正后的完整残差也不等于裸的 \(H^4\)，但四个 \(A\)-奇核投影仍由第一部分的对称性严格消去。

### 谱隙数值的一处修正

“非标量扇区谱隙至少为 \(3\Lambda/2\)”并不成立。取两个球面上的一次谐波一形式 \(\alpha,\beta\)，并令
\[
h=\alpha\odot\beta
\]
为混合张量。Bochner 公式给出
\[
\nabla^*\nabla\alpha=\Lambda\alpha,\qquad
\nabla^*\nabla\beta=\Lambda\beta.
\]
乘积曲率在混合块上的作用为零，因此
\[
P h=\frac12(2\Lambda)h=\Lambda h.
\]
可以选择两个在 \(r_\pi\) 下同时变号的一次模式，使 \(h\) 在 \(\sigma\) 下不变；两个一次模式都为 \(A\)-奇，所以 \(h\) 为 \(A\)-偶。因此该扇区存在本征值 \(\Lambda\)，整体正谱隙至多为 \(\Lambda\)，而 \(3\Lambda/2\) 只适用于所列因子无迹二阶张量子扇区。

---

## 3. 阶数比较

令 \(t=t_{\max}\)，并假设接收节点尺度满足 \(t_i\asymp t\)。当一阶系数 \(\lambda_{i,k}=0\) 时，
\[
t_i^2\mu_{i,k}=O(t^{5/2}),
\]
所以
\[
\mu_{i,k}=O\!\left(\frac{t^{5/2}}{t_i^2}\right)
=O(t^{1/2}).
\]
因此沿 \(t\to0\) 的解序列，如果 \(\alpha_i(t)\to\alpha_i^*\)，则连续性给出
\[
\mu_{i,k}(\alpha_i^*)=0.
\]
这是二阶系数方程；对某个固定的非零 \(t\)，原估计本身并不等价于精确方程 \(\mu_{i,k}=0\)。

交互源在节点 \(j\) 的振幅是 \(t_j^2\)，接收节点的一阶阻碍还带有 \(t_i\)，故
\[
F^{\mathrm{inter}}_{i,k}
=t_it_j^2\mathcal I_{ij,k}.
\]
若交互算子一致有界，则一般已有
\[
|t_it_j^2|\le t_{\max}^3,
\]
不必要求尺度可比较。并且
\[
\frac{t^3}{t^{5/2}}=t^{1/2}\longrightarrow0.
\]
所以
\[
t^3=o(t^{5/2}).
\]
这正表示三阶交互被包含在当前 \(O(t^{5/2})\) 误差中，Ozuch 的这一估计无法提取其系数。

因而可精确表述为：

- 在 \(t^2\) 阶，每个节点轨道的必要系数方程是
  \[
  \mu_{i,k}(\alpha_i)=0;
  \]
- 这一阶没有节点间项；
- 若这些 \(\mu_{i,k}\) 全部消失，则下一层方程可能含有交互项、自节点正规 Green 部分及其他三阶项；
- 现有 \(O(t^{5/2})\) 估计不足以比较这些三阶系数。

在尺度很不相等时，交互项可以与较小节点的自项同阶。例如
\[
t_2^2\sim t_2t_1^2
\quad\Longleftrightarrow\quad
t_2\sim t_1^2.
\]
但这两个量此时都远小于以 \(t_{\max}=t_1\) 表示的 \(O(t_1^{5/2})\) 误差，所以当前必要条件仍无法分辨这种平衡。

---

## 4. 秩一正交代数与 \(\mu_2,\mu_3\)

令
\[
R^-=\operatorname{diag}(\Lambda,0,0),\qquad
v=\rho(\zeta)^-=(0,c,s),\qquad c^2+s^2=1.
\]
则
\[
R^-v=0
\]
是直接的矩阵乘法。

若
\[
dR^-=12\left(vv^T-\frac13I\right)\frac1{r^6},
\]
则
\[
dR^-=
\frac1{r^6}
\begin{pmatrix}
-4&0&0\\
0&12c^2-4&12cs\\
0&12cs&12s^2-4
\end{pmatrix}.
\]
所以 \((1,2)\) 与 \((1,3)\) 元确实严格为零。右下角块的行列式为
\[
(12c^2-4)(12s^2-4)-(12cs)^2=-32.
\]
其沿 \((c,s)\) 的本征值为 \(8\)，沿正交方向的本征值为 \(-4\)。

但是同一矩阵也给出
\[
dR^-v=\frac8{r^6}v\neq0
\]
以及
\[
R^-dR^-=dR^-R^-
=\frac1{r^6}\operatorname{diag}(-4\Lambda,0,0)\neq0.
\]
`step78_rank_one_orthogonality.json` 中的 `R_dR_norm = 4` 正好记录了后一事实。因此“背景曲率消去 \(v\)”只适用于直接出现 \(R^-v\) 的表达式，不能推广到所有二阶曲率收缩。

还有一个重要前提：若 EH 公式中的 \(\rho=\rho_{\hat x}\) 随径向方向变化，则一般可写
\[
\rho_{\hat x}(\zeta)^-=(a(\hat x),b(\hat x),d(\hat x)).
\]
此时
\[
dR^-_{12}=12ab/r^6,\qquad
dR^-_{13}=12ad/r^6,
\]
只有在 \(a(\hat x)=0\) 时才保持上述分块。给出的 JSON 只对假设 \(a=0\) 后的 \(\alpha\)-多项式取样，没有检验 \(\rho_{\hat x}\) 的空间方向依赖。若这里的 \(\rho\) 是某个固定且特意选择的粘合识别，则分块计算成立；若它是标准径向旋转映射，则需要在固定背景曲率基底中重新计算角变量。

因此目前能得到的是：

- \(R^-v=0\) 和分块 \(dR^-\) 在指定固定分量前提下成立；
- \(\nabla R=0\) 也成立，因为圆球乘积局部对称；
- 这些事实会消去含背景曲率导数或直接含 \(R^-v\) 的项；
- 非零的 \(dR^-v\)、\(R^-dR^-\)、右下角块，以及规范与 Green 修正仍可能进入 \(\mu_2,\mu_3\)。

所以，现有代数对 \(\mu_2=\mu_3=0\) 提供了结构动机，但并未形成推导。完整 Biq16/Ozuch 分量公式及其中 \(\rho\) 的确切定义，才会决定这两个系数。
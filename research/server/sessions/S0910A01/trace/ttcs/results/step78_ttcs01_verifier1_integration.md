# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 78,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step78_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step78_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the three structural theorems for the A-equivariant diagonal reduction of the Einstein desingularization of (S^2 x S^2)/Z_2, and check the order analysis.

1. SCALAR KERNEL ELIMINATION: The simultaneous antipodal A(x,y)=(-x,-y) is orientation-preserving, commutes with sigma, and acts on product harmonics as (-1)^{l1+l2}. The four scalar P-kernel modes u_i*g_j have l_total=1 (odd), so are A-odd. An A-invariant residual is orthogonal to them. Check this carefully: is it really true that A is orientation-preserving in 4D? That it commutes with sigma? That l1+l2=1 for the kernel modes?

2. SCALAR DECOUPLING: For in-kernel zeta in span{omega_2,omega_3}, compute omega_k^+ circ omega_l^- for k,l in {2,3} in the standard product frame. Verify they all have zero trace on each S^2 factor. Therefore H^4(zeta) has zero scalar-sector coupling. Note the contrast: omega_1^+ circ omega_1^- = -(g1-g2), which IS scalar. So only in-kernel directions decouple from scalars.

3. ORDER ANALYSIS: The Ozuch necessary conditions give t^2*mu_k = O(t^{5/2}), so mu_k -> 0. The inter-node Green response contributes at O(t^3). Since 5/2 < 3, we have t^{5/2} >> t^3 for small t. Check: is this comparison correct? Does it really mean the inter-node term is BELOW the remainder? If so, the leading reduced equation is simply mu_k(alpha) = 0 at each orbit, with no inter-node coupling.

4. RANK-ONE ORTHOGONALITY: R^- = diag(Lambda,0,0) and rho(zeta)^- = (0,cos alpha,sin alpha) for in-kernel zeta. Verify R^- * rho(zeta)^- = 0. Verify the curvature modification dR^- is block-diagonal (entries (1,2) and (1,3) are zero). Does this suggest all mu_k vanish? What caveats apply?

Be precise about any errors in the reasoning.

## Integrated Scientific Memo

# 核验结论

四项中：

- **标量核消去成立**，但前提是整个粘合数据与规范选择均严格 \(A\)-等变。
- **裸 \(H^4\) 对 \(f g_1,f g_2\) 的直接耦合为零**；Step 78 对 \(\rho\) 的固定分量假设并非必要，且可能没有被证明。
- **阶数比较正确**：三阶节点相互作用低于现有 \(O(t_{\max}^{5/2})\) 精度，因而该估计无法识别它；这不表示三阶方程中不存在相互作用。
- **秩一正交恒等式成立，但绝不能据此断言所有 \(\mu_k\) 消失**。目前严格得到的只有 \(\mu_1=0\)；\(\mu_2,\mu_3\) 仍需完整公式。

---

## 1. \(A\)-对称确实消去四个标量核投影

令 \(a(x)=-x\) 为 \(S^2\) 的反足映射。其次数为
\[
\deg a=(-1)^{2+1}=-1,
\]
所以单个 \(S^2\) 上反转取向。于是
\[
A=a\times a:S^2\times S^2\longrightarrow S^2\times S^2
\]
的乘积次数为
\[
\deg A=(-1)(-1)=+1.
\]
因此 \(A\) **保持四维乘积取向**，从而保持 \(\Lambda^+\oplus\Lambda^-\) 分解。这里不能仅以切空间中的 \(-I_2\) 行列式判断单球面的取向，因为源点和像点的球面取向还涉及相反的外法向量。

若
\[
r_\pi=\operatorname{diag}(-1,-1,1)\in SO(3),
\]
则反足映射来自 \(-I_3\)，故
\[
(-I_3)r_\pi=r_\pi(-I_3).
\]
因此
\[
A\sigma=\sigma A,
\]
所以 \(A\) 降到商 orbifold 上。

球谐函数满足
\[
a^*Y_{\ell m}=(-1)^\ell Y_{\ell m}.
\]
其中 \(u_1\) 的乘积次数为 \((1,0)\)，\(u_2\) 为 \((0,1)\)，而 \(A^*g_j=g_j\)。故
\[
A^*(u_i g_j)=-u_i g_j,\qquad i,j\in\{1,2\}.
\]
所以四个 Ozuch 全张量核模式
\[
u_1g_1,\quad u_1g_2,\quad u_2g_1,\quad u_2g_2
\]
确实全部 \(A\)-奇。

若残差 \(E\) 为 \(A\)-不变，则因 \(A\) 是保体积等距映射，
\[
\langle E,K\rangle_{L^2}
=\langle A^*E,A^*K\rangle_{L^2}
=-\langle E,K\rangle_{L^2},
\]
故 \(\langle E,K\rangle=0\)。因此四个 \(\nu_l\) 投影严格消失。

### 必要限定

这要求近似度量、截断、规范修正及 EH 数据整体 \(A\)-等变。节点参数必须满足
\[
\zeta_{A(p)}=A_*\zeta_p.
\]
在任意独立选择的局部标架中，“两个节点使用相同数值角度 \(\alpha\)”未必自动等价于该传输条件。

另外，\(A\) 在 \(S^2\times S^2\) 上实际上是自由的；“固定 equator\(\times\)equator”这一支输出中的附带说法是错误的，因为 \(x=-x\) 在球面上无解。

---

## 2. 标量直接耦合消失，但应缩窄并修正陈述

取乘积正交标架 \((e_1,e_2,e_3,e_4)\)，其中前两维属于第一个因子，并采用
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
把二形式视为斜对称端同态；自对偶和反自对偶端同态交换，其复合为对称端同态。直接计算得到
\[
\omega_2^+\circ\omega_2^-
=\operatorname{diag}(-1,1,-1,1),
\]
\[
\omega_3^+\circ\omega_3^-
=\operatorname{diag}(-1,1,1,-1),
\]
而两个交叉复合可写为
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
\end{pmatrix},
\]
具体交叉项符号可随二形式约定改变，但分因子迹不变。上述每个张量都满足
\[
T_{11}+T_{22}=0,\qquad T_{33}+T_{44}=0.
\]
所以对于
\[
\zeta^+\in\operatorname{span}\{\omega_2^+,\omega_3^+\},
\]
由这些复合构成的 \(H^4\) 对两个因子均无迹，从而逐点有
\[
\langle H^4,f g_1\rangle
=f\,\operatorname{tr}_{g_1}H^4=0,
\qquad
\langle H^4,f g_2\rangle
=f\,\operatorname{tr}_{g_2}H^4=0.
\]

事实上，直接计算还表明
\[
\operatorname{tr}_{g_i}(\omega_a^+\circ\omega_1^-)=0,
\qquad a=2,3,\quad i=1,2.
\]
因此只要自对偶输入 \(\zeta^+\) 位于 \(\omega_2^+,\omega_3^+\) 平面，对任意
\(\eta^-\in\Lambda^-\)，张量 \(\eta^-\circ\zeta^+\) 都具有分因子无迹性。由此：

- Step 78 所用
  \[
  \rho(\zeta)^-=c\omega_2^-+s\omega_3^-
  \]
  并非标量解耦所必需；
- 给出的文件也没有建立 \(\rho\) 在固定背景基底中确实恒有这种形式；若 \(\rho=\rho_{\hat x}\) 随径向方向转动，该固定分量式可能不成立；
- 但上述更强的代数事实仍足以证明裸 \(H^4\) 对 \(f g_1,f g_2\) 的直接耦合为零。

对照地，
\[
\omega_1^+\circ\omega_1^-
=\operatorname{diag}(-1,-1,1,1)
=-(g_1-g_2),
\]
所以出核方向 \(\omega_1\) 确实产生标量形状张量。

### 陈述范围

“对全部标量扇区解耦”若仅指纯迹乘积张量 \(f g_1,f g_2\)，则成立。若该术语还包含 Hessian 生成的无迹标量型张量，则上述分因子迹计算不足以覆盖它们。截断、移植和 Bianchi 修正后的完整残差也不等于裸 \(H^4\)；不过四个 \(A\)-奇零模投影仍由第 1 节的对称性严格消去。

Step 78 进一步声称整个非标量扇区谱隙至少为 \(3\Lambda/2\)，这不成立。若 \(\alpha,\beta\) 是两个因子上的一次谐波一形式，则混合张量
\[
h=\alpha\odot\beta
\]
满足
\[
\nabla^*\nabla\alpha=\Lambda\alpha,\qquad
\nabla^*\nabla\beta=\Lambda\beta,\qquad
\mathring Rh=0,
\]
从而
\[
Ph=\Lambda h.
\]
可选取使 \(h\) 同时 \(\sigma\)-不变和 \(A\)-偶的模式。因此全非标量正谱隙至多为 \(\Lambda\)；\(3\Lambda/2\) 只适用于笔记列出的特定 TT\(\times\)scalar 子扇区。

---

## 3. 阶数比较正确，但“领先方程”是渐近必要条件

令 \(t=t_{\max}\)。在入核方向上 \(\lambda_{i,k}=0\)，Ozuch 条件为
\[
t_i^2\mu_{i,k}=O(t^{5/2}).
\]
若 \(t_i\asymp t\)，则
\[
\mu_{i,k}=O(t^{1/2}).
\]
所以沿 \(t\to0\) 的解序列，若 \(\alpha_i(t)\to\alpha_i^*\)，则由连续性
\[
\mu_{i,k}(\alpha_i^*)=0.
\]
因此 \(\mu=0\) 是二阶系数的极限必要方程，而不是对每个固定小 \(t\) 从该余项估计推出的精确方程。

节点 \(j\) 的源振幅为 \(t_j^2\)，在节点 \(i\) 的第一阻碍中再乘 \(t_i\)，故
\[
F_{i,k}^{\mathrm{inter}}
=t_i t_j^2\mathcal I_{ij,k}.
\]
若交互算子一致有界，则一般已有
\[
t_i t_j^2=O(t_{\max}^3),
\]
不必假定尺度可比较。且
\[
\frac{t^3}{t^{5/2}}=t^{1/2}\to0,
\]
即
\[
t^3=o(t^{5/2}).
\]

在可比较尺度下，层级为
\[
t^2\gg t^{5/2}\gg t^3.
\]
故现有精度下：

1. 二阶局部系数方程是
   \[
   \mu_{i,k}(\alpha_i)=0;
   \]
2. 该二阶方程在不同节点轨道之间解耦；
3. 三阶节点间项被包含在 \(O(t^{5/2})\) 余项中，Ozuch 的这一估计无法提取其系数。

“inter-node term is below the remainder”是正确的数量级表述，但不意味着该项在真实三阶展开中不存在。若所有 \(\mu_{i,k}\) 消失，则下一阶可能同时包含节点间 Green 响应、自节点 Green 正则部分及其他三阶项；需要优于 \(o(t^3)\) 的展开才能比较它们。

尺度极不相等时，较小节点的自项和交互项可以同阶，例如
\[
t_2^2\sim t_2t_1^2
\quad\Longleftrightarrow\quad
t_2\sim t_1^2.
\]
但二者此时都可能低于以 \(t_{\max}=t_1\) 表示的 \(O(t_1^{5/2})\) 误差，因此当前必要条件仍无法解析这种平衡。Step 78 关于“不等尺度时交互可以竞争”的直觉成立，但不能从现有余项精度获得可验证的平衡方程。

---

## 4. 秩一正交成立，但不足以推出 \(\mu_2=\mu_3=0\)

在固定基底并假设
\[
R^-=\operatorname{diag}(\Lambda,0,0),
\qquad
v=\rho(\zeta)^-=(0,c,s),
\qquad c^2+s^2=1
\]
时，
\[
R^-v=0.
\]

若
\[
dR^-=12\left(vv^T-\frac13I\right)\frac1{r^6},
\]
则
\[
dR^-=\frac1{r^6}
\begin{pmatrix}
-4&0&0\\
0&12c^2-4&12cs\\
0&12cs&12s^2-4
\end{pmatrix}.
\]
所以 \((1,2)\) 和 \((1,3)\) 元确实为零。右下块满足
\[
\det
\begin{pmatrix}
12c^2-4&12cs\\
12cs&12s^2-4
\end{pmatrix}
=-32.
\]
其沿 \((c,s)\) 的本征值为 \(8\)，沿垂直方向的本征值为 \(-4\)。

但同一计算同时表明
\[
dR^-v=\frac8{r^6}v\neq0,
\]
以及
\[
R^-dR^-=dR^-R^-
=\frac1{r^6}\operatorname{diag}(-4\Lambda,0,0)\neq0.
\]
JSON 中的 `R_dR_norm = 4` 正记录了后一非零事实。因此只可断言：

- 直接含 \(R^-v\) 的项消失；
- \(\nabla R=0\) 消去背景曲率导数项；
- 固定分量假设下，\(dR^-\) 不混合 \(\omega_1^-\) 与核平面。

不能断言所有二阶曲率收缩均消失。非零的 \(dR^-v\)、\(R^-dR^-\) 和核平面内的非退化块都可能进入 \(\mu_2,\mu_3\)。

此外，如果实际公式中的
\[
\rho_{\hat x}(\zeta)^-=(a(\hat x),b(\hat x),d(\hat x))
\]
依赖球面方向，那么
\[
(dR^-)_{12}=12ab/r^6,\qquad
(dR^-)_{13}=12ad/r^6.
\]
故分块性要求在所采用的固定背景基底中 \(a(\hat x)\equiv0\)。现有 JSON 只验证了先假定 \(a=0\) 后的矩阵代数，没有验证 \(\rho_{\hat x}\) 的定义确实保证这一点。

因此当前严格状态是：

\[
\boxed{\mu_1=0}
\]
由已引用的秩一行列式公式得到；而
\[
\boxed{\mu_2,\mu_3\ \text{尚未确定}.}
\]

每个轨道的领先自由方向只有一个角度 \(\alpha\)，却有两个未决条件
\[
\mu_2(\alpha)=\mu_3(\alpha)=0.
\]
除非二者因 \(SO(2)\) 协变性降为一个标量条件，或恒等消失，否则一参数通常不能同时满足两个独立方程。决定性对象是完整 Biq16/Ozuch 公式中 \((\mu_2,\mu_3)\) 的适配基底计算，包括：

1. \(\rho\) 的确切、可能依赖方向的定义；
2. 非零 \(dR^-\) 核块的贡献；
3. Bianchi/坐标规范修正；
4. 奇性扣除后的自节点 Green 正则项；
5. 若相应阶次允许，核坐标 \(v\) 的影响。

故“rank-one orthogonality suggests all \(\mu_k\) vanish”最多是未经证明的猜想；“曲率没有产生非零二阶阻碍的机制”则是过强且与已计算的非零 \(dR^-\) 结构不相容的表述。
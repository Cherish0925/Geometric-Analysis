# TTCS Independent Branch Record

```json
{
  "step_id": 77,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md",
    "Sessions/S0910A01/workspace/data/step77_scalar_kernel_and_pairing.json",
    "Sessions/S0910A01/workspace/data/step77_slice_decomposition_verify.json",
    "Sessions/S0910A02/workspace/notes/step68_spectral_symmetry_and_multipole_gate.md",
    "Sessions/S0910A02/workspace/data/step68_orbifold_kernel_full_vs_tt.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 77 repair of the mixed-row product-orbifold obstruction problem. Please check the mathematical substance, not prose style: (i) Ozuch Definition 1.8 full L2 kernel versus TT kernel distinction; (ii) the calculation that axial first harmonics u1,u2 on S^2 descend under the half-turn and give P(u_i g_j)=0 for Ozuch P=1/2∇*∇-R°; (iii) the Bianchi/pure-gauge slice interpretation and whether it is enough to remove or must be incorporated into the finite-dimensional equations; (iv) the local raw normal-coordinate projection prototype in step77_scalar_kernel_and_pairing.json, especially whether the -pi^2/18 coefficient should be treated only as a unit test before slice/Green transport; (v) the separation of lambda, mu_1, mu_2,3, projected equations, full residual/inverse estimates, and the topology/Ozuch-Q0.8 scope corrections. Identify any remaining mathematical errors or the most useful next executable computation for the singular-subtracted Green response H_ij,2.

## Output

# 科学核验备忘录

## 总体结论

Step 77 对 Ozuch 全 \(L^2\) 核与 TT 核的区分是正确且必要的；四个标量扇区零模也确实存在，并且完整核恰为四维。Bianchi 条件加微分同胚商能够消去这些方向，但这需要在算子、投影和有限维映射中同时实现，不能只依据 TT 核为零删除 \(\nu_l\)。

有两个重要的进一步修正：

1. JSON 中的 \(-\pi^2/18\) 原始系数可以独立复算出来，但把 Riemann 正规坐标改成 Ozuch 所要求的 \(B_{\mathbf e}g_o=0\) 坐标后，规范修正恰好给出 \(+\pi^2/18\)。因此这四个标量模的这一阶局部配对在标准 Bianchi 坐标中逐点相消，而不只是四节点等尺度求和相消。
2. 节点间 Green 二阶喷流 \(H_{ij,2}\) 在可比尺度下进入 \(t_i t_j^2=O(t^3)\) 项，不属于式
   \[
   t_i\lambda_i+t_i^2\mu_i
   \]
   中的局部 \(\mu_i\)。裸 \(\mu_{2,3}\) 与节点间 Green 响应应分开计算。

---

## 1. 全核恰为四维，TT 核为零

Ozuch Definition 1.8 明确定义
\[
\mathbf O(g)=\ker_{L^2}\left(\frac12\nabla^*\nabla-\mathring R\right)
\]
作用于所有对称二张量，并未加入无迹或散度为零的条件。Step 77 在这一点上与原文一致。

设两个球面的截面曲率均为 \(\Lambda\)。在覆盖空间 \(S^2\times S^2\) 上，把张量分成两个纯因子块和混合块。对
\[
h=Y_\ell(x)Y_m(y)\,g_1
\]
有
\[
P h=
\left[
\frac{\Lambda}{2}\bigl(\ell(\ell+1)+m(m+1)\bigr)-\Lambda
\right]h.
\]
零特征值只可能满足
\[
\ell(\ell+1)+m(m+1)=2,
\]
即 \((\ell,m)=(1,0)\) 或 \((0,1)\)。对 \(g_2\) 块同样成立。

因子内无迹张量满足
\[
\mathring R h=-\Lambda h,\qquad
\langle Ph,h\rangle
=\frac12\|\nabla h\|^2+\Lambda\|h\|^2,
\]
故不产生零模。混合一形式块上 \(\mathring R=0\)，而两个球面都没有平行一形式，故也无零模。

半转 \(r_\pi\) 在每个球面的 \(\ell=1\) 空间上作用为
\[
(x,y,z)\longmapsto(-x,-y,z),
\]
不变子空间由轴向谐波 \(u=z\) 张成。因此商空间上的完整核确为
\[
\mathbf O(g_o)
=\operatorname{span}
\{u_1g_1,u_1g_2,u_2g_1,u_2g_2\}.
\]
这不仅证明“包含四个模”，也排除了其他零模。

相对缩放张量满足
\[
P(g_1-g_2)=-\Lambda(g_1-g_2),
\]
所以不在核中。

---

## 2. Bianchi 条件与微分同胚方向

对
\[
h=a\,u_1g_1+b\,u_1g_2+c\,u_2g_1+d\,u_2g_2
\]
直接计算得到
\[
B h=b\,du_1+c\,du_2.
\]
因此 Bianchi 条件留下
\[
u_1g_1,\qquad u_2g_2.
\]
又因为
\[
\mathcal L_{\nabla u_1}g
=2\nabla^2u_1=-2\Lambda u_1g_1,
\qquad
\mathcal L_{\nabla u_2}g
=-2\Lambda u_2g_2,
\]
这两个剩余方向都是商空间上良定义的微分同胚方向。加入无迹条件后它们也被消去，所以
\[
\ker(P|_{\mathrm{TT}})=0.
\]

这足以说明几何模空间在该线性层次没有非平凡方向，但不足以在 Ozuch 原有公式中直接删掉四个投影。原因有二：

- Bianchi 条件只消去两个交叉模，另外两个需要额外固定残余微分同胚；
- 这些微分同胚会改变节点处线性坐标、EH 尺度和角参数的表示，因而有限维映射也随切片改变。

此外，Ozuch 后续论证采用 Definition 1.10 的“完整核可积”前提。当前材料没有证明上述四个全核方向都形成其所需的 \(\mathbf g_v\) Einstein 族；两个交叉方向尤其没有这样的构造。因此，原 Ozuch \(v\)-参数体系若原样使用，还需要相应的 Kuranishi 项。采用定制 Bianchi/微分同胚切片则可以避开这一前提，但算子和投影公式必须同步重写。

---

## 3. \(-\pi^2/18\) 原始系数及其 Bianchi 修正

### 3.1 原始正规坐标计算正确

取 \(\Lambda=1\)、\(\phi=\omega_2^+\)，在 \(S^3\) 上使用
\[
\mathbb E[x_a^4]=\frac18,\qquad
\mathbb E[x_a^2x_b^2]=\frac1{24}\quad(a\ne b).
\]
把
\[
H^4=-\frac12\sum_{\alpha=1}^3
(x^TA_\alpha x)A_\alpha
\]
与 \(u_1g_1\) 的二次正规坐标项收缩，可得
\[
\mathbb E_{S^3}\langle H^4,V_2(u_1g_1)\rangle=-\frac1{18}.
\]
其他三个模给出同值；核平面内角度只通过 \(c^2+s^2\) 出现。由于
\[
\operatorname{Area}(S^3/\mathbb Z_2)=\pi^2,
\]
原始积分确为
\[
-\frac{\pi^2}{18}.
\]
南极处 \(u_i\) 与其二次 Taylor 项同时变号，故 JSON 中四节点符号表也正确。反向手性由固定节点的定向反转等距映射给出同一数值。

### 3.2 Ozuch 的 Bianchi 坐标产生精确抵消

Riemann 正规坐标中的产品度量二次项 \(H_2^{\rm rn}\) 满足
\[
B_{\mathbf e}H_2^{\rm rn}
=-\frac{2\Lambda}{3}\sum_{a=1}^4x_a\,dx_a,
\]
所以它不是 Ozuch 使用的 \(B_{\mathbf e}g_o=0\) 坐标。

令
\[
X=-\frac{\Lambda}{18}r^2x^a\partial_a.
\]
因为
\[
B_{\mathbf e}(\mathcal L_X\mathbf e)=-\Delta X^\flat
=\frac{2\Lambda}{3}x^\flat,
\]
故
\[
H_2^B=H_2^{\rm rn}+\mathcal L_X\mathbf e
\]
满足二次阶 Bianchi 条件。相应地，
\[
V_2^B(u_i g_j)
=V_2^{\rm rn}(u_i g_j)
+\operatorname{sgn}(u_i(p))\,\mathcal L_XG_j,
\]
其中 \(G_j\) 是第 \(j\) 个因子的常值投影度量。

采用与 JSON 相同的 \(H^4\) 号数和 \(\omega^\pm\) 基底，球面矩计算给出
\[
\int_{S^3/\mathbb Z_2}
\langle H^4,\mathcal L_XG_j\rangle\,d\sigma
=+\frac{\pi^2}{18}.
\]
因此
\[
\int_{S^3/\mathbb Z_2}
\langle H^4,V_2^B(u_i g_j)\rangle\,d\sigma=0
\]
对四个模、四个节点和两种手性均成立。

所以 \(-\pi^2/18\) 很适合作为正规坐标代数的 unit test，但它不能支持“尺度不等时首阶标量投影一般非零”的推断。标准 Bianchi 坐标下，该阶配对逐节点为零。Ozuch 公式另有因子
\[
\nu_l=3\int\langle H^4,V_{l,2}\rangle,
\]
以及全局 \(L^2\) 归一化；这些都应在更新后的脚本中明确体现。

---

## 4. \(\lambda,\mu\) 与 Green 响应的阶数分离

下列分离是正确的：

- 若 \(\phi_i\in\ker R^{\epsilon_i}\)，则
  \[
  \lambda_k^i(\phi_i,0)=0
  \quad(k=1,2,3).
  \]
- 对
  \[
  R^\pm=\operatorname{diag}(\Lambda,0,0)
  \]
  和核平面中的 \(\phi_i\)，适配基底下余下 \(2\times2\) 块秩为一，因此 Ozuch/Biquard 的公式给出
  \[
  \mu_1^i=0.
  \]
- 该行列式公式没有给出 \(\mu_2^i,\mu_3^i\)。它们需要实际的 Biquard 二阶公式。

横向平衡还可进一步细化。若
\[
\phi=(0,\cos\alpha,\sin\alpha),
\]
则离开核平面的角扰动 \(a e_1\) 使一个横向 \(\lambda\) 分量在线性阶变化，因而能平衡对应的 \(t^2\mu\)；核平面内的切向分量在线性阶不改变 \(R\phi=0\)。所以两个横向 \(\mu\) 分量并不自动都能靠任意角扰动消去。尺度比主要通过全局 \(\nu\) 方程及更高阶节点耦合进入。

需要改正的是 Green 项的归属。由于
\[
H^4(t_j\phi_j)=t_j^2H^4(\phi_j),
\]
节点 \(j\) 在节点 \(i\) 产生的正规二次喷流满足
\[
H_{ij,2}=O(t_j^2).
\]
它改变节点 \(i\) 的首 obstruction 后，有限维方程中的量级是
\[
t_i\,O(t_j^2).
\]
可比尺度下这是 \(O(t^3)\)，而不是 \(t_i^2\mu_i\) 的 \(O(t^2)\) 项。Ozuch 当前
\[
O(t_{\max}^{5/2})
\]
精度看不到这一系数，因为 \(t^3=o(t^{5/2})\)。因此裸 \(\mu_{2,3}\)、\(v=O(t)\) 引起的局部修正、以及 \(H_{ij,2}\) 应按不同阶次处理。

Step 77 关于投影方程与完整残差的区分是正确的：这些方程是精确 Einstein 度量必须满足的有限维投影关系；存在性还需要补空间上的统一逆估计、投影后残差估计和非线性余项控制。

---

## 5. 拓扑表与 Ozuch Question 0.8

表中所有行满足
\[
b_2=6,\qquad
(b_2^+,b_2^-)=(k+1,5-k),
\]
并且 \(k\leftrightarrow4-k\) 与定向反转一致。\(k=2\) 时两行同为 \((3,3)\)，相邻型为奇交叉形式、对置型为偶交叉形式，这与
\[
3\mathbb{CP}^2\#3\overline{\mathbb{CP}}{}^2,
\qquad
\#_3(S^2\times S^2)
\]
的区分一致。

当前提供的文件没有包含所引用的 `20260912.tex` 或 Kirby 图，因此这些不变量可独立确认，但精确光滑微分同胚类型仍需该手柄计算或等价的显式构造支撑。

Ozuch Question 0.8 的原文确实以 Ricci-flat orbifold 和 Kähler Ricci-flat ALE 树为背景，询问极限及平滑度量是否为 hyperkähler 商。它不是关于该正 Einstein 产品 orbifold 的充分性陈述。Step 77 对此的修正正确。

---

## 6. 最有信息量的 Green 可执行对象

比原始
\[
\frac12D^2_{p_i}G_P^\perp(H^4)
\]
更稳定的对象是直接计算目标节点的线性化曲率响应
\[
\mathcal C_{ij}^{\epsilon}(\phi)
=
D_{g_o}R^\epsilon_{p_i}
\left[
G_P^\perp (I-\Pi_{\mathbf O})\,\mathcal S_{j,\phi}
\right].
\]
这里局部四极源可由小球面通量定义；对光滑测试张量
\[
q=Q_0+Q_2+O(r^4)
\]
其归一化可固定为
\[
\mathcal S_{j,\phi}(q)
=
3\int_{S^3/\mathbb Z_2}
\langle H^4(\phi),Q_2\rangle\,d\sigma.
\]
采用上面的 Bianchi 坐标修正后，该泛函应消去四个完整核模。

若 \(\Psi_\alpha\) 是商空间上 \(P\) 的正交本征张量，
\[
P\Psi_\alpha=p_\alpha\Psi_\alpha,
\]
则不同节点间的响应形式上为
\[
\mathcal C_{ij}^{\epsilon}(\phi)
=
\sum_{p_\alpha\ne0}
\frac{
D R^\epsilon(\Psi_\alpha)(p_i)\,
\mathcal S_{j,\phi}(\Psi_\alpha)
}{p_\alpha}.
\]
这比裸 \(D^2\) 更合适，因为 \(D R\) 自动包含二阶协变导数、常值项 \(H_{ij,0}\) 导致的正交框架修正以及背景曲率与张量的代数收缩。

产品张量球谐基底可以显式实现该和式；核中四模应精确剔除，并用热核或 Abel 正则处理高频和。自伴性给出可复现的互易恒等式
\[
\langle\mathcal S_{i,\psi},
G_P^\perp\mathcal S_{j,\phi}\rangle
=
\langle\mathcal S_{j,\phi},
G_P^\perp\mathcal S_{i,\psi}\rangle.
\]
四节点对称性只留下相邻与对置两类响应；由于 \(H^4(\phi)\) 对 \(\phi\) 二次，核平面内取
\[
\phi=e_2,\quad e_3,\quad \frac{e_2+e_3}{\sqrt2}
\]
即可重建全部角依赖。

这一计算最终进入三阶耦合项
\[
t_i\sum_{j\ne i}t_j^2\,
\left\langle
\mathcal C_{ij}^{\epsilon_j}(\phi_j)\phi_i,
\phi_{i,k}
\right\rangle,
\]
它才是混合行尺度比和节点间相互作用的直接有限维系数。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 77,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step77_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step77_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 77 repair of the mixed-row product-orbifold obstruction problem. Please check the mathematical substance, not prose style: (i) Ozuch Definition 1.8 full L2 kernel versus TT kernel distinction; (ii) the calculation that axial first harmonics u1,u2 on S^2 descend under the half-turn and give P(u_i g_j)=0 for Ozuch P=1/2∇*∇-R°; (iii) the Bianchi/pure-gauge slice interpretation and whether it is enough to remove or must be incorporated into the finite-dimensional equations; (iv) the local raw normal-coordinate projection prototype in step77_scalar_kernel_and_pairing.json, especially whether the -pi^2/18 coefficient should be treated only as a unit test before slice/Green transport; (v) the separation of lambda, mu_1, mu_2,3, projected equations, full residual/inverse estimates, and the topology/Ozuch-Q0.8 scope corrections. Identify any remaining mathematical errors or the most useful next executable computation for the singular-subtracted Green response H_ij,2.

## Integrated Scientific Memo

# Step 77 数学核验结论

## 1. Ozuch 全 \(L^2\) 核与 TT 核

Step 77 的核心修复正确。Ozuch Definition 1.8 定义的是
\[
\mathbf O(g)=\ker_{L^2}P_g,\qquad
P_g=\frac12\nabla^*\nabla-\mathring R,
\]
作用于全部对称二张量，不是 \(P|_{\mathrm{TT}}\) 的核。因此不能由 TT 核为零直接删除 \(\nu_l\) 投影。

在覆盖空间 \(S^2(\Lambda)\times S^2(\Lambda)\) 上，对第一球面的轴向一阶谐波 \(u_1\)，
\[
\Delta u_1=2\Lambda u_1,\qquad \nabla^2u_1=-\Lambda u_1g_1.
\]
又因 \(g_j\) 平行且
\[
\mathring R(u_1g_j)=\Lambda u_1g_j,
\]
所以
\[
P(u_1g_j)=0,\qquad j=1,2.
\]
\(u_2g_j\) 同理。半转在每个球面的 \(\ell=1\) 空间上作用为
\[
(x,y,z)\mapsto(-x,-y,z),
\]
故只有轴向谐波下降到商空间，得到
\[
\mathbf O(g_o)
=\operatorname{span}\{u_1g_1,u_1g_2,u_2g_1,u_2g_2\}.
\]
通过纯因子无迹块、混合一形式块和标量谱分解还可排除其他零模，故完整核确为四维，而非仅“至少四维”。

另一方面，
\[
\ker(P|_{\mathrm{TT}})=0,
\qquad
P(g_1-g_2)=-\Lambda(g_1-g_2).
\]
相对尺度模是有界离零的负特征模，不是零模。

---

## 2. Bianchi／纯规范解释

对
\[
h=a\,u_1g_1+b\,u_1g_2+c\,u_2g_1+d\,u_2g_2
\]
及 \(B=\delta+\frac12d\operatorname{tr}\)，有
\[
Bh=b\,du_1+c\,du_2.
\]
因此 Bianchi 条件留下 \(u_1g_1,u_2g_2\)，而
\[
\mathcal L_{\nabla u_1}g=-2\Lambda u_1g_1,\qquad
\mathcal L_{\nabla u_2}g=-2\Lambda u_2g_2,
\]
说明这两个剩余方向是纯微分同胚方向。于是恰当的 Bianchi 加残余微分同胚归一化切片中没有真实线性 Einstein 模。

但这不能在 Ozuch 原体系内直接删除四个 \(\nu_l\)：

* Bianchi 条件本身仅排除两个交叉模；
* 消除剩余纯规范模会改变局部坐标、EH 参数及投影映射；
* Definition 1.10 还假设完整核可积。现有材料没有证明交叉／共形型核方向按该定义积分为 Einstein 族。

因此只有两种严谨方案：

1. 保留四个全核变量及相应 Kuranishi／投影方程；或
2. 从头构造定制切片，并同步重写算子、Green 逆、节点参数和有限维映射。

Step 77 关于“必须纳入方程或显式切片，不能静默删除”的判断正确；“这些都不是几何模”只应理解为线性模微分同胚后的结论，不能自动替代 Kuranishi 分析。

---

## 3. \(-\pi^2/18\) 只能作为原始坐标单元测试

JSON 的计算属于未切片的 Riemann 正规坐标原型。按其基底和归一化，球面矩确给出
\[
\mathbb E_{S^3}\langle H^4,V_2\rangle=-\frac1{18},
\qquad
\int_{S^3/\mathbb Z_2}\langle H^4,V_2\rangle
=-\frac{\pi^2}{18}.
\]
四个模式数值相同、核平面角度仅通过 \(c^2+s^2\) 出现，以及节点轴向谐波符号表，均可作为代数回归测试。

然而该数值不是 Ozuch 的最终 \(\nu_l\) 系数。更强地说，Riemann 正规坐标的产品二次项并不满足 \(B_{\mathbf e}H_2=0\)。令
\[
X=-\frac{\Lambda}{18}r^2x^a\partial_a;
\]
则
\[
B_{\mathbf e}(\mathcal L_X\mathbf e)
=\frac{2\Lambda}{3}x^\flat
\]
恰好修正正规坐标二次项的 Bianchi 缺陷。在与 JSON 相同的符号约定下，该坐标修正的配对为
\[
\int_{S^3/\mathbb Z_2}
\langle H^4,\mathcal L_XG_j\rangle\,d\sigma
=+\frac{\pi^2}{18},
\]
从而标准二次阶 Bianchi 坐标中
\[
\int_{S^3/\mathbb Z_2}
\langle H^4,V_{l,2}^{B}\rangle\,d\sigma=0
\]
对这四个全核模逐节点相消。

因此 Step 77 中“等尺度四节点求和相消，但不等尺度时原始标量投影可能非零”的推断不能作为物理结论保留。正确表述是：

* \(-\pi^2/18\) 验证原始正规坐标张量代数；
* 经过所需的 Bianchi 坐标修正后，该局部阶次的四个核配对消失；
* 更高阶、完整切片或 Green 传输是否重新产生核方程，仍须另算；
* Ozuch 公式还有
  \[
  \nu_l=3\int\langle H^4,V_{l,2}\rangle
  \]
  及全局 \(L^2\) 归一化，JSON 数值未包含这些。

这是 Step 77 尚需写入的主要数学修正。

---

## 4. \(\lambda,\mu\)、节点耦合和分析估计的分离

下列分离正确：

\[
\phi_i\in\ker R^{\epsilon_i}
\quad\Longrightarrow\quad
\lambda_k^i(\phi_i,0)=0,\quad k=1,2,3.
\]

对于
\[
R^\pm=\operatorname{diag}(\Lambda,0,0),
\]
在以 \(\phi_i\) 开头的适配基底中，Ozuch/Biquard 的行列式公式只推出
\[
\mu_1^i
=C\det
\begin{pmatrix}
R_{22}&R_{23}\\
R_{32}&R_{33}
\end{pmatrix}
=0.
\]
它不推出 \(\mu_2^i=\mu_3^i=0\)。后二者须用实际 Biq16 二阶公式计算；角扰动也不必能独立平衡两个横向分量。

还应进一步纠正 Green 响应的阶数归属。因为
\[
H^4(t_j\phi_j)=t_j^2H^4(\phi_j),
\]
源节点 \(j\) 在目标节点 \(i\) 产生
\[
H_{ij,2}=O(t_j^2).
\]
它改变目标节点的首 obstruction 后进入
\[
t_i\,O(t_j^2).
\]
可比尺度下这是 \(O(t^3)\)，不是局部
\[
t_i^2\mu_i=O(t^2)
\]
的一部分，而且低于 Ozuch 当前 \(O(t_{\max}^{5/2})\) 精度所能分辨的阶次。因此必须分别计算：

1. 裸局部 \(\mu_{1,2,3}\)；
2. \(v\)-或 Kuranishi 变量引起的局部曲率修正；
3. 三阶节点间 Green 耦合
   \[
   t_i\sum_{j\ne i}t_j^2(\cdots).
   \]

Step 77 正确区分了有限维必要投影方程与完整存在性证明。即使所有投影消失，仍需：

* 投影后完整加权残差估计；
* 补空间上的一致右逆；
* 非线性余项和参数依赖控制；
* 最终有限维零点的非退化性或适当度数论证。

---

## 5. 拓扑和适用范围

以下修正成立：

* 四节点解消均有 \(b_2=6\)；
* \(k\) 个正向 EH 时签名为 \(\tau=2k-4\)；
* \(k=2\) 的相邻型与对置型分别对应奇、偶交叉形式候选：
  \[
  3\mathbb{CP}^2\#3\overline{\mathbb{CP}}{}^2,
  \qquad
  \#_3(S^2\times S^2).
  \]

但所给材料没有包含声称支持精确光滑微分同胚类型的 Kirby／手柄证明，因此 \(b_2\)、签名和奇偶性可核验，完整光滑分类仍依赖该缺失构造。

Ozuch Question 0.8 确实是 Ricci-flat orbifold 及 Kähler Ricci-flat ALE 树是否必为 hyperkähler 商的问题，不是正 Einstein 产品商的充分性猜想。平坦 \(T^4/\mathbb Z_2\) 计算只能作为控制模型，除非给出到正曲率产品情形的传递论证。任何局部退化阻碍也只排除靠近该 orbifold 的 Einstein 序列，不解决 Yau–26 的全局命题。

---

## 6. 最有用的下一项可执行 Green 计算

比直接记录坐标二阶导数更稳定的目标是目标节点的线性化曲率响应
\[
\mathcal C_{ij}^{\epsilon}(\phi)
=
D_{g_o}R^\epsilon_{p_i}
\left[
G_P^\perp (I-\Pi_{\mathbf O})\mathcal S_{j,\phi}
\right],
\]
其中四极源泛函以边界通量归一化：
\[
\mathcal S_{j,\phi}(Q)
=
3\int_{S^3/\mathbb Z_2}
\langle H^4(\phi),Q_2^B\rangle\,d\sigma .
\]
这里必须使用刚才的 Bianchi 二次喷流 \(Q_2^B\)，并验证它对四个全核模为零。

若
\[
P\Psi_\alpha=p_\alpha\Psi_\alpha
\]
是商空间上的张量球谐谱，则
\[
\mathcal C_{ij}^{\epsilon}(\phi)
=
\sum_{p_\alpha\ne0}
\frac{
D R^\epsilon(\Psi_\alpha)(p_i)\,
\mathcal S_{j,\phi}(\Psi_\alpha)
}{p_\alpha}.
\]
实现时应同时检查：

* 四个零模被精确投影掉；
* \(P(g_1-g_2)=-\Lambda(g_1-g_2)\)；
* 自伴互易关系
  \[
  \langle\mathcal S_{i,\psi},G_P^\perp\mathcal S_{j,\phi}\rangle
  =
  \langle\mathcal S_{j,\phi},G_P^\perp\mathcal S_{i,\psi}\rangle;
  \]
* 四节点对称性只留下相邻与对置两类传输；
* 取
  \[
  \phi=e_2,\quad e_3,\quad \frac{e_2+e_3}{\sqrt2}
  \]
  即可重建核平面中的二次角依赖。

最终应形成三阶耦合系数
\[
t_i\sum_{j\ne i}t_j^2
\left\langle
\mathcal C_{ij}^{\epsilon_j}(\phi_j)\phi_i,
\phi_{i,k}
\right\rangle,
\]
而不是把 \(H_{ij,2}\) 混入裸 \(\mu_i\)。

## 最终判定

Step 77 的主修复——全核／TT 核区分、四维标量核、切片不能静默删除投影、只证明 \(\mu_1=0\)、投影方程不等于完整存在性、拓扑及 Q0.8 范围修正——均正确。

仍需修正的关键点有两个：

1. \(-\pi^2/18\) 经二次阶 Bianchi 坐标修正后恰好抵消，不能用于声称不等尺度时该阶标量投影一般非零；
2. 节点间 \(H_{ij,2}\) 是可比尺度下的三阶 \(t_it_j^2\) 响应，不属于二阶局部 \(\mu_i\)。

此外，若继续原样使用 Ozuch Definition 1.10，还必须解决四维全核的可积性/Kuranishi 问题；采用定制切片则须完整重建对应的有限维系统。
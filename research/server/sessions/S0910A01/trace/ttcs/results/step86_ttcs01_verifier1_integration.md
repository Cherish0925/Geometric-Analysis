# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 86,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step86_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step86_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

I am computing the exact inter-node obstruction coefficient for mixed-chirality Einstein desingularization of the product orbifold O=(S^2xS^2)/Z_2 with four A_1 (R^4/Z_2) nodes, following Ozuch's higher-order obstruction theory. The decisive structural finding of this step is that the correct inter-node coefficient is NOT a bulk product-Lichnerowicz spectral sum (which produced frame-sensitive proxy numbers -1.22, +0.41, -0.53 in prior work), but Ozuch's exact BOUNDARY PAIRING formula from Proposition 2.10 and Corollary 2.12 of arXiv:2105.13193 (file: Knowledge/objects/papers/Higher-order-obstructions...object.md, lines 606-666). Specifically:
(a) Prop 2.10 line 616: nu_l = 3 * integral over S^3/Z_2 of <H^4, V_{l,2}>_e, valid when lambda_k=0, where H^4=H^4(zeta_j^pm) is the ALE bubble's r^{-4} multipole at source node j, and V_{l,2} is the r^{+2}-growing homogeneous component of the orbifold obstruction/Einstein-deformation basis mode v_l = O(g_o) evaluated near the singular point.
(b) Cor 2.12 line 660: sum_j |zeta_j| lambda_1^j(zeta,v) = C sum_l <v,v_l> nu_l(zeta,0) + O(...), linking bubble first-obstruction variation to orbifold nu_l.
(c) H^4(zeta^+) = -rho(zeta)^- o zeta^+ /(2r^4) and H^4(zeta^-) = -zeta^- o rho(zeta)^+/(2r^4) are DIFFERENT symmetric 2-tensors depending on chirality (established in prior Step 84 with tr(C_ab C_cd)=4 delta_ac delta_bd).

MY CLAIM TO VERIFY: The mixed-row chirality coefficient c_opp - c_same reduces to the difference of boundary pairings nu_l(+) - nu_l(-) = 3 integral over S^3/Z_2 of <H^4(zeta^+) - H^4(zeta^-), V_{l,2}> where V_{l,2} is chirality-independent (it is a property of the orbifold Einstein deformation, common to all fillings), and only the source multipole H^4 carries the chirality. This is a clean r^{-4} source against r^{+2} receiver spherical boundary integral, so ONLY the degree-2 (in the R^4 harmonic sense) part of the receiver V_{l,2} survives against the degree-2 source multipole H^4, by orthogonality of RP^3 Laplacian eigenspaces (line 574, 636). 

QUESTIONS: (1) Is this reduction faithful to Ozuch's Prop 2.10 / Cor 2.12, i.e. is the inter-node coefficient genuinely the boundary integral 3*int<H^4, V_{l,2}> rather than a bulk resolvent, and does the chirality dependence enter only through H^4 with V_{l,2} chirality-independent? (2) What exactly is V_{l,2} for the product orbifold O=(S^2xS^2)/Z_2 -- is it the r^2-Taylor coefficient of the orbifold's Einstein-deformation obstruction modes O(g_o) at the node, and is the relevant space here the H_2-type quadratic tensor with P_e H_2 = Lambda e (line 476)? (3) Does the requirement lambda_k=0 (first obstruction vanishing, which prior steps established via EH-direction-in-kernel choice) legitimately hold at the leading order so that the Prop 2.10 formula applies, or does the mixed-chirality assignment spoil lambda_k=0? (4) Is there a genuine risk that nu_l is a per-NODE quantity (each node contributes its own bar-h^4_j, summed in line 641) so that the 'inter-node' language must be interpreted as: node j's source H^4(zeta_j) pairs with the GLOBAL orbifold mode v_l which is delocalized over all four nodes -- meaning the coupling between distinct nodes is mediated by the global obstruction mode v_l, not by a direct node-to-node Green function? Please read the source lines 449-666 carefully and give a precise mathematical assessment of whether the boundary-pairing reduction is correct and what V_{l,2} and v_l concretely are for this product orbifold.

## Integrated Scientific Memo

## 核验结论

你的边界配对公式对 **Ozuch 的 \(\nu_l\) 核投影系数**完全正确，但把它直接认作一般的混合手征、逐节点系数
\[
c_{ij}=L_iG_P^\perp S_j
\]
则不正确。二者是不同的数学对象：

\[
\boxed{\nu_l^{(j)}
 =3\int_{\Sigma_j}\langle H_j^4,V^{(j)}_{l,2}\rangle_e\,d\sigma_e}
\]
是源节点 \(j\) 对全局零模 \(v_l\in\ker P_{g_o}\) 的 Fredholm 投影；而真正从 \(j\) 传播到另一节点 \(i\) 的曲率二阶 jet，通常仍需 \(P_{g_o}\) 在核正交补上的全局解算。

---

## 1. Proposition 2.10 实际给出的内容

固定节点 \(p_j\) 以及
\[
v_l\in\mathbf O(g_o)=\ker_{L^2}P_{g_o},\qquad
v_l=V^{(j)}_{l,0}+V^{(j)}_{l,2}+O(r_j^4).
\]
Ozuch 构造
\[
P_{g_o}\bar h_j^4
 =\sum_l\nu_l^{(j)}v_l+\sum_k\lambda_k^j\bar o_{j,k}^4,
\qquad
\bar h_j^4\sim H_j^4+H_{j,2}^4
\]
并通过分部积分得到一般式
\[
\nu_l^{(j)}
=
3\int_{\Sigma_j}\langle H_j^4,V^{(j)}_{l,2}\rangle_e
+\int_{\Sigma_j}\langle H_{j,2}^4,V^{(j)}_{l,0}\rangle_e .
\]
当全部 \(\lambda_k^j=0\) 时，Lemma 2.3 给出 \(H_{j,2}^4=0\)，因此
\[
\boxed{
\nu_l^{(j)}
 =3\int_{\Sigma_j}
 \langle H_j^4,V^{(j)}_{l,2}\rangle_e\,d\sigma_e .
}
\]

因而，在同一个定向 orbifold chart 中比较两种填充时，
\[
\boxed{
\nu_l^{(j,+)}-\nu_l^{(j,-)}
=
3\int_{\Sigma_j}
\langle H_j^4(\zeta_j^+)-H_j^4(\zeta_j^-),
V^{(j)}_{l,2}\rangle_e\,d\sigma_e .
}
\]
这里 \(v_l\) 及其 jet \(V_{l,2}^{(j)}\) 完全由 orbifold 决定，与节点填入 \(+\) 或 \(-\) Eguchi–Hanson 无关；该公式中的手征依赖确实只在
\[
H^4(\zeta^+)
=-\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4},
\qquad
H^4(\zeta^-)
=-\frac{\zeta^-\circ\rho(\zeta)^+}{2r^4}
\]
中。

系数 \(3\) 也正是边界 Wronskian 的径向次数给出的：
\[
\frac12\bigl((-4)-2\bigr)=-3
\]
再结合内边界法向约定得到命题中的正号。

### 角向正交性

\(H^4\) 的笛卡尔张量分量属于 \(S^3/\mathbb Z_2\) 上的标量二次谐波，即球谐次数 \(2\)。一般齐次二次张量 \(V_{l,2}\) 的系数可含次数 \(0\) 与次数 \(2\) 部分；只有后者参与配对。因此准确说法是：

\[
\int_{\Sigma_j}\langle H^4,V_{l,2}\rangle
=
\int_{\Sigma_j}
\langle H^4,\Pi_{\mathcal H_2}V_{l,2}\rangle .
\]

---

## 2. 这不等于一般的逐节点 Green 响应

由节点 \(j\) 的源所确定的全局奇异解满足
\[
P_{g_o}\bar h_j^4=\sum_l\nu_l^{(j)}v_l,
\qquad
\bar h_j^4\sim H_j^4\quad (p_j\text{ 附近}).
\]
在另一节点 \(p_i\neq p_j\) 附近，它是光滑的：
\[
\bar h_j^4=A_{ij,0}+A_{ij,2}+O(r_i^4).
\]
接收节点的第一障碍变化取决于 \(A_{ij,2}\) 的曲率 jet，并还包含 \(A_{ij,0}\) 引起的线性坐标修正：
\[
\delta_j\lambda_k^i
=
c\left\langle
\delta R^\pm_i(A_{ij,0},A_{ij,2})\,\zeta_i^\pm,
\zeta_{i,(k)}^\pm
\right\rangle .
\]
从 \(H_j^4\) 求 \(A_{ij,2}\) 一般需要求解
\[
P_{g_o}\bar h_j^4
\]
在核正交补上的部分，即投影 Green 算子。数值 \(\nu_l^{(j)}\) 只记录核方向投影，并不确定该正交补解在 \(p_i\) 的二阶 jet。

因此：

* 若你的 \(c_{\rm opp}-c_{\rm same}\) **按定义就是某个全局核模的 Fredholm 投影差**，则边界公式正确；
* 若它是 Step 85 所写的真正接收节点响应
  \[
  c_{ij}=L_iG_P^\perp S_j,
  \]
  则不能用 \(\nu_l^{(j)}\) 取代它。

Corollary 2.12 也没有消除这一区别。它给出
\[
\sum_j|\zeta_j|\lambda_1^j(\zeta,v)
=
C\sum_l\langle v,v_l\rangle\nu_l(\zeta,0)
+O(\|v\|^2|\zeta|^2),
\]
其中 \(v\) 是全局 infinitesimal Einstein deformation。该式是一个伴随互易关系，只有对节点求和后的接收量，没有独立的 \(i,j\) 两个指标，也没有给出 \(A_{ij,2}\)。

一个直接的来源内证是平坦 \(\mathbb T^4/\mathbb Z_2\)：全局核模是常张量，故 \(V_{l,2}=0\)、相应 \(\nu_l=0\)；但论文第 3–4 节仍存在由周期化 \(H^4\) 场 \(B_{j-i}^L\) 产生的非零泡间曲率相互作用。故“核投影”和“节点间传播”严格不同。

---

## 3. \(V_{l,2}\) 究竟是什么

它是
\[
v_l\in\mathbf O(g_o),\qquad P_{g_o}v_l=0
\]
在节点的二次 Taylor 项：
\[
v_l=V_{l,0}+V_{l,2}+O(r^4).
\]
它不是背景度量展开
\[
g_o=e+H_2+O(r^4)
\]
中的 \(H_2\)。

二者满足不同方程：

\[
P_eH_2=\Lambda e,
\]
而 \(V_{l,2}\) 来自展开 \(P_{g_o}v_l=0\)，其方程含有背景曲率 jet \(H_2\) 对常数项 \(V_{l,0}\) 的作用。符号上是
\[
P_eV_{l,2}
=
-\bigl(DP\bigr)_{H_2}V_{l,0},
\]
而不是 \(P_eV_{l,2}=\Lambda e\)。

所以问题中“相关空间是否就是满足 \(P_eH_2=\Lambda e\) 的 \(H_2\)-型二次张量”应回答：

\[
\boxed{\text{同为齐次二次张量层级，但不是同一个仿射方程或同一个对象。}}
\]

---

## 4. 产品 orbifold 的核：必须区分完整 Bianchi 核与 TT 模空间

对单位半径乘积
\[
g_o=g_A+g_B,\qquad \operatorname{Ric}(g_o)=g_o,
\]
提供的 sector ledger 确实在完整算子
\[
P=\frac12\nabla^*\nabla-\mathring R
\]
中给出四个形式零模：
\[
u_Ag_A,\quad u_Ag_B,\quad u_Bg_A,\quad u_Bg_B,
\]
其中 \(u_A,u_B\) 是两因子的 \(\ell=1\) 高度函数。

但这不能直接称为四维 TT infinitesimal Einstein deformation space：

\[
\mathcal L_{\nabla u_A}g_o=-2u_Ag_A,\qquad
\mathcal L_{\nabla u_B}g_o=-2u_Bg_B,
\]
故其中至少两个是纯微分同胚方向。另两个 cross modes 是否通过 Ozuch 使用的 gauge、是否为可积 Einstein deformation，需要单独的 Bianchi/Kuranishi 核验。另一方面
\[
g_A-g_B
\]
是 TT，但 ledger 给出 \(P=-1\)，是负模而不是零模。

因此两个分支中“\(\mathbf O(g_o)\) 明确四维”和“强烈预计 \(\mathbf O(g_o)=0\)”都超出了当前材料能严格支持的范围。精确结论是：

* 完整未约化 \(P\)-核有上述候选零模；
* 真正进入 Definition 1.8、Proposition 2.10 和 Corollary 2.12 的 gauge-fixed/integrable 空间尚须约化；
* 负的 shape mode 绝不会成为 \(v_l\)，但会参与真正的 \(G_P^\perp\) 响应。

### 候选零模的局部二次 jet

在节点 \(p_{\sigma,\tau}\) 附近取两因子的测地/立体型局部坐标
\(x,y\in\mathbb R^2\)，使
\[
u_A=\sigma\left(1-\frac12|x|^2\right)+O(r^4),\qquad
u_B=\tau\left(1-\frac12|y|^2\right)+O(r^4),
\]
以及
\[
g_A=E_A-\frac12|x|^2E_A+O(r^4),\qquad
g_B=E_B-\frac12|y|^2E_B+O(r^4).
\]
则相应二次项为
\[
\begin{aligned}
V_2(u_Ag_A)&=-\sigma |x|^2E_A,\\
V_2(u_Ag_B)&=-\frac{\sigma}{2}(|x|^2+|y|^2)E_B,\\
V_2(u_Bg_A)&=-\frac{\tau}{2}(|x|^2+|y|^2)E_A,\\
V_2(u_Bg_B)&=-\tau |y|^2E_B,
\end{aligned}
\]
再乘所选 \(L^2\) 归一化常数。这些公式可用于任何最终确认为真实 \(v_l\) 的线性组合。

---

## 5. 产品情形下这些候选配对事实上为零

取适应乘积分解的二形式基，使
\[
\omega_1^+=\operatorname{vol}_A+\operatorname{vol}_B,\qquad
\omega_1^-=\operatorname{vol}_A-\operatorname{vol}_B.
\]
乘积曲率算子为
\[
R^+=\operatorname{diag}(1,0,0),\qquad
R^-=\operatorname{diag}(1,0,0).
\]
故满足第一障碍消失的 EH 方向分别为
\[
\zeta^+\in\operatorname{span}\{\omega_2^+,\omega_3^+\},
\qquad
\zeta^-\in\operatorname{span}\{\omega_2^-,\omega_3^-\}.
\]

上述候选 \(V_{l,2}\) 都是标量函数乘 \(E_A\) 或 \(E_B\)。其 trace-free 矩阵部分沿
\[
E_A-E_B\propto C_{11}
=\omega_1^+\circ\omega_1^-.
\]
而若 \(\zeta^+\) 位于 \(R^+\) 的核，则
\[
H^4(\zeta^+)\in
\operatorname{span}\{C_{ab}:a=2,3\};
\]
若 \(\zeta^-\) 位于 \(R^-\) 的核，则
\[
H^4(\zeta^-)\in
\operatorname{span}\{C_{ab}:b=2,3\}.
\]
利用
\[
\operatorname{tr}(C_{ab}C_{cd})
=4\delta_{ac}\delta_{bd},
\]
两者均与 \(C_{11}\) 正交；\(H^4\) 又是 trace-free，因此 \(V_{l,2}\) 的纯迹部分也不贡献。于是，对上述完整零模候选空间，
\[
\boxed{
\int_{\Sigma_j}\langle H^4(\zeta^\pm),V_{l,2}\rangle_e=0.
}
\]

所以无论约化后这些候选保留多少，曲率核方向上都有
\[
\nu_l^{(j,+)}=\nu_l^{(j,-)}=0.
\]
这直接否定了“非零 \(c_{\rm opp}-c_{\rm same}\) 就等于
\(\nu_l(+)-\nu_l(-)\)”这一识别。若所求混合行系数非零，它必须来自：

1. \(H_j^4\) 经核正交补全局传播后在 \(p_i\) 的 \(A_{ij,2}\)；
2. 相应曲率/第二障碍变化；
3. 或更高阶非线性项；

而不是这些 \(\nu_l\) 配对。

---

## 6. \(\lambda_k=0\) 与混合手征

在未受其他泡正则场扰动的产品背景上，
\[
\lambda_k^j
=c\left\langle R^\pm\zeta_j^\pm,\zeta_{j,(k)}^\pm\right\rangle .
\]
由于两种手征都有二维曲率核，每个节点独立选择
\[
\zeta_j^\pm\in\ker R^\pm
\]
即可使三个 \(\lambda_k^j\) 全部精确为零。因此混合 \(+/-\) 指派本身不破坏 Proposition 2.10 的假设。

但其他节点的泡产生正则场后，接收节点曲率发生变化，新的
\[
\delta\lambda_k^i
\]
正是待求的节点间响应。因此应区分：

\[
\lambda_k^j(\zeta,0)=0
\quad\text{与}\quad
\lambda_k^j(\zeta,\text{全局泡响应后})=0.
\]

前者足以在领先源问题中应用 Proposition 2.10；后者不是自动成立的。

---

## 7. 多节点含义

自然定义每个源节点的贡献
\[
\nu_l^{(j)}
=
3\int_{\Sigma_j}
\langle H_j^4,V^{(j)}_{l,2}\rangle,
\]
总障碍为
\[
\nu_l^{\rm tot}=\sum_j\nu_l^{(j)}.
\]
每个积分都发生在同一个节点 \(j\)：源 \(H_j^4\) 与全局模式 \(v_l\) 在该节点的局部 jet 配对。节点之间可因共享同一个 delocalized \(v_l\) 而在有限维约化方程中耦合，但这不是直接的 \(j\to i\) Green 传播。

故“inter-node”至少有两种必须分开的含义：

\[
\begin{array}{ll}
\text{全局零模介导：}&
H_j^4\mapsto \nu_l^{(j)}
\mapsto\text{有限维全局参数};\\[1mm]
\text{直接正交补传播：}&
H_j^4\mapsto\bar h_j^4
\mapsto A_{ij,2}
\mapsto\delta\lambda_k^i.
\end{array}
\]

你的边界配对正确描述第一种；Step 85 的 \(L_iG_P^\perp S_j\) 描述第二种。对于当前产品 orbifold 的曲率核 EH 方向，第一种候选配对全部为零，故真正的混合手征系数仍应在第二种机制中计算。
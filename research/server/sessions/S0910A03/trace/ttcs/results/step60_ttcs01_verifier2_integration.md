# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 60,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step60_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step60_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Audit the terminal chart argument for the restricted four-dimensional Ishida–LeBrun route. Starting from Vol_T(P)≥cA, ∫𝔇_T≤Cδ²A (q_top≥0), uniform curvature on buffered plateau regions, and exponential-pullback ball averaging, verify the exact selection-and-limit chain: Liouville/Fubini inequality over p∈P, a selected pullback ball with mean density O(δ²), Rauch noncollapse and harmonic coordinates, strong W^{2,q}_loc convergence, and passage of the nonnegative density to zero on the whole limiting ball, sufficient for the calibrated-spectrum projector contradiction. Flag any flaw in claiming curvature convergence or pointwise vanishing from W^{2,q}; propose the minimal rigorous replacement if necessary. Also verify that A cancels and the resulting restricted conclusion is exclusion of sufficiently negative-pinched input metrics on a family already known to admit no Einstein metric—not merely exclusion of λ=-1 output metrics.

## Integrated Scientific Memo

# 终端图表论证核验

## 结论

在以下上游输入成立的前提下：

\[
\operatorname{Vol}_{g_i(T)}(P_i)\ge c_0A_i,\qquad
\int_{M_i}\mathfrak D_i\,d\mu_i\le C_0\delta_i^2A_i,
\]
\(P_i\) 具有统一 plateau 缓冲，且该缓冲内
\[
|\operatorname{Rm}_{g_i(T)}|\le K,
\]
终端链条可以严格闭合：

\[
\text{Liouville/Fubini 平均}
\Longrightarrow
\text{选取均值 }O(\delta_i^2)\text{ 的 pullback 球}
\]
\[
\Longrightarrow
\text{Rauch 控制与中心调和图}
\Longrightarrow
g_i\to g_\infty\text{ 强 }W^{2,q}_{\rm loc}
\]
\[
\Longrightarrow
\mathfrak D_\infty\equiv0
\Longrightarrow
\operatorname{Spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right)
\Longrightarrow\text{矛盾}.
\]

需要修正两处表述：

1. pullback 球的总体积下界本身不足以直接引用通常的全球调和半径定理；最稳妥的输入是 pullback 球中心的统一单射半径，或等价地直接构造中心调和图。
2. 强 \(W^{2,q}\) 收敛不给出逐点曲率收敛。正确替代是强 \(L^q\) 曲率收敛、密度的强 \(L^1\) 收敛，再借助极限 Einstein 度量的光滑性把几乎处处为零提升为处处为零。

---

## 1. Liouville–Fubini 选择与 \(A\) 的消去

令终端非负密度为

\[
\mathfrak D_i=
|E_i|^2+(s_i+4)^2+
(s_i+8\sqrt6|W_i^+|)^2+G_i,
\qquad E_i=\operatorname{Ric}_{g_i(T)}+g_i(T),
\]
其中 \(G_i\ge0\)。在 \(q_{\rm top}\ge0\) 时，Step 43 给出

\[
\int_{M_i}\mathfrak D_i\le119\,Q_i(T)
\le C\delta_i^2A_i.
\tag{1}
\]

必须由同一个中心集合 \(P_i\) 同时承担：

\[
\operatorname{Vol}(P_i)\ge c_0A_i
\tag{2}
\]
以及每个 \(p\in P_i\) 的长度不超过 \(\rho\) 的径向测地线均位于曲率受控 plateau 中。仅在大集合上有体积下界、而只在更小且无体积控制的集合上有缓冲，并不足够。Step 56 的 \(P^{\rm in}\) 记号若确实满足两者，则接口一致。

定义

\[
\mathcal B_\rho(p)=\{v\in T_pM_i:|v|<\rho\},\qquad
\widetilde g_{i,p}=(\exp_p)^*g_i(T),
\]
以及

\[
\mathcal A_\rho\mathfrak D_i(p)
=
\frac{\int_{\mathcal B_\rho(p)}
(\exp_p)^*\mathfrak D_i\,d\mu_{\widetilde g_{i,p}}}
{\operatorname{Vol}_{\widetilde g_{i,p}}(\mathcal B_\rho(p))}.
\]

取 \(\rho\le c\min\{r,K^{-1/2}\}\)。径向 Jacobian 比较给出

\[
c_Rt^3\le j_i(p,u,t)\le C_Rt^3,\qquad
c_v\rho^4\le\operatorname{Vol}_{\widetilde g_{i,p}}
(\mathcal B_\rho(p))\le C_v\rho^4.
\tag{3}
\]

以 \(\varphi_t\) 表示单位切丛上的测地流、\(dL\) 表示 Liouville 测度，则

\[
\begin{aligned}
\int_{P_i}\mathcal A_\rho\mathfrak D_i(p)\,d\mu_i(p)
&\le
\frac C{\rho^4}\int_0^\rho t^3
\int_{SP_i}\mathfrak D_i(\pi\varphi_tz)\,dL(z)\,dt\\
&\le C_L(K,\rho)\int_{M_i}\mathfrak D_i\,d\mu_i .
\end{aligned}
\tag{4}
\]

第二步使用 \(\varphi_t^*dL=dL\) 及 \(\mathfrak D_i\ge0\)。指数映射可以折叠或多重覆盖，但这不会产生额外重数：积分是在单位切丛上按初始方向计算，而测地流是其上的微分同胚。

由 (1)、(2)、(4)，存在 \(p_i\in P_i\) 使

\[
\mathcal A_\rho\mathfrak D_i(p_i)
\le
\frac{C_LC_0\delta_i^2A_i}{c_0A_i}
=
\frac{C_LC_0}{c_0}\delta_i^2.
\tag{5}
\]

因此 \(A_i\) 完全消去。结合 (3)，

\[
\int_{\mathcal B_\rho(p_i)}
(\exp_{p_i})^*\mathfrak D_i\,d\mu_{\widetilde g_i}
\longrightarrow0.
\tag{6}
\]

这里的常数仍可依赖固定 IL 地理参数、\(K,\rho,c_0\)，故所得间隙不是仅依赖维数的常数。

---

## 2. Pullback 几何与调和坐标

曲率界拉回为

\[
|\operatorname{Rm}_{\widetilde g_i}|\le K
\quad\text{于 }\mathcal B_\rho(p_i).
\tag{7}
\]

Rauch 比较给出 (3)，但“整个 pullback 球有体积下界”不应被直接等同于“任意内点都有统一调和半径”。最小而稳妥的修正是只在中心建立图表：

* 径向曲线 \(t\mapsto tv\) 是 pullback 度量从 \(0\) 出发的测地线；
* 在该 pullback 域内，不同径向射线不会在切空间中相交；
* Rauch 给出统一共轭半径下界。

因而

\[
\operatorname{inj}_{\widetilde g_i}(0)
\ge c(K,\rho)>0.
\tag{8}
\]

由中心单射半径与曲率界，可在一个固定较小球 \(U\Subset\mathcal B_\rho\) 上取得调和坐标，使

\[
\lambda^{-1}\delta\le\widetilde g_i\le\lambda\delta,\qquad
\|\widetilde g_i\|_{C^{1,\alpha}(U)}
+\|\widetilde g_i\|_{W^{2,q}(U)}\le C_q.
\tag{9}
\]

这里不需要 base-manifold 图像球 \(B(p_i,\rho)\) 非塌缩；局部解包正是 pullback 构造的目的。

取子列后，

\[
\widetilde g_i\to g_\infty
\quad\text{强 }C^{1,\beta}_{\rm loc},
\qquad
\widetilde g_i\rightharpoonup g_\infty
\quad\text{弱 }W^{2,q}_{\rm loc}.
\tag{10}
\]

---

## 3. Einstein 极限与强 \(W^{2,q}\) 收敛

由 (6) 中的 \(|E_i|^2\) 项，

\[
\|E_i\|_{L^2(U)}\to0.
\tag{11}
\]

统一曲率界给出 \(\|E_i\|_{L^\infty}\le C(K)\)，故插值推出

\[
E_i\to0\quad\text{强 }L^q_{\rm loc}
\quad\text{对每个有限 }q.
\tag{12}
\]

调和坐标中的 Ricci 方程为

\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=
2(g_i)_{jk}-2(E_i)_{jk}
+Q_{jk}(g_i^{-1},\partial g_i).
\tag{13}
\]

由 \(C^{1,\beta}\) 收敛和 (12)，可传到极限，得到

\[
\operatorname{Ric}_{g_\infty}=-g_\infty
\tag{14}
\]
的弱解。调和坐标中的 Einstein 椭圆系统随即将 \(g_\infty\) 提升为光滑度量。

再令 \(h_i=g_i-g_\infty\)。差分方程可写为

\[
L_i h_i
=
2h_i-2E_i+(Q_i-Q_\infty)
+(L_\infty-L_i)g_\infty.
\tag{15}
\]

右端强收敛到零于 \(L^q_{\rm loc}\)，内点椭圆估计给出

\[
\boxed{
g_i\to g_\infty\quad\text{强 }W^{2,q}_{\rm loc}
}
\tag{16}
\]
对每个有限 \(q\) 成立。边界不需要处理，只在固定缩小球上使用内点估计。

---

## 4. 必须修正的曲率与密度表述

不能从 (16) 声称：

\[
\operatorname{Rm}_{g_i}(x)\to\operatorname{Rm}_{g_\infty}(x)
\quad\text{对每一点 }x.
\]

正确结论是

\[
\operatorname{Rm}_{g_i}\to\operatorname{Rm}_{g_\infty}
\quad\text{强 }L^q_{\rm loc},
\tag{17}
\]
并可另取子列得到几乎处处收敛。原因是曲率由度量二阶导数的线性项与一阶导数的二次项组成。

对密度也不应直接声称逐点收敛。这里最小严谨替代如下：

1. 取 \(q>2\)。由 (17)、统一曲率界以及 \(W^+\) 特征值对对称矩阵的 Lipschitz 依赖，
   \[
   \mathfrak D_i\to\mathfrak D_\infty
   \quad\text{强 }L^1_{\rm loc}.
   \tag{18}
   \]
   特别地，\(G=f^2-(b_-)^2\) 的截断及最小特征值不会破坏这一结论。

2. 对每个 \(K'\Subset U\)，由 (6)、(18) 和非负性，
   \[
   \int_{K'}\mathfrak D_\infty\,d\mu_{g_\infty}=0.
   \tag{19}
   \]
   因而 \(\mathfrak D_\infty=0\) 几乎处处。

3. \(g_\infty\) 已光滑，所以 \(\mathfrak D_\infty\) 连续。于是
   \[
   \boxed{\mathfrak D_\infty\equiv0\quad\text{在整个内球 }U.}
   \tag{20}
   \]

因此，处处消失来自“非负密度的零积分 + 光滑极限的连续性”，而不是来自 \(W^{2,q}\) 下的逐点曲率收敛。

---

## 5. 校准谱投影子矛盾

由 (14)、(20)，

\[
s_\infty=-4,\qquad
s_\infty+8\sqrt6|W_\infty^+|=0,
\]
故

\[
|W_\infty^+|^2=\frac1{24}.
\tag{21}
\]

再由 \(G_\infty=0\) 与 Step 43 的谱确定引理，

\[
\operatorname{Spec}(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right)
\tag{22}
\]
在整个内球上成立。注意：\(G=0\) 单独不足以得到该谱，必须同时使用 \(s=-4\) 和 \(|W^+|^2=1/24\)。

Einstein 条件给出 \(\delta W_\infty^+=0\)。常谱投影子引理因此推出

\[
\nabla W_\infty^+=0.
\tag{23}
\]

另一方面，Einstein–Weyl 恒等式

\[
\Delta|W^+|^2
=
2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]
结合

\[
s=-4,\qquad |W^+|^2=\frac1{24},\qquad
\det W^+=-\frac1{864}
\]
给出

\[
|\nabla W_\infty^+|^2=\frac1{16},
\tag{24}
\]
与 (23) 矛盾。故不存在平均密度趋于零的受控 pullback 球序列。由反证紧性，存在

\[
\eta=\eta(K,\rho)>0
\]
使所有此类中心均满足

\[
\mathcal A_\rho\mathfrak D(p)\ge\eta.
\tag{25}
\]

与 (5) 比较，当

\[
\delta<
\left(\frac{c_0\eta}{C_LC_0}\right)^{1/2}
\]
时即得矛盾。

---

## 6. 严格得到的受限结论

在 \(q_{\rm top}\ge0\)、终端流与体积选择等上游模块成立的 IL 地理族中，存在依赖该地理族的 \(\varepsilon_{\mathcal F}>0\)，使

\[
\left\|g^{-1}(\operatorname{Ric}_g+g)\right\|_{L^\infty,\mathrm{op}}
\ge\varepsilon_{\mathcal F}
\tag{26}
\]
对该族上的所有候选输入度量成立。等价地，不存在任意紧的归一化负 Ricci 夹逼

\[
-(1+\varepsilon_{\mathcal F})g
\le\operatorname{Ric}_g
\le-(1-\varepsilon_{\mathcal F})g.
\tag{27}
\]

这是对**输入度量**的定量负 Einstein 间隙，不只是排除某个输出度量满足 \(\operatorname{Ric}_h=-h\)。若所选 IL 成员已由独立拓扑或规范论结果排除所有 Einstein 度量，则本论证是在这些已知无 Einstein 度量的流形上进一步排除充分接近 \(-g\) 的 Ricci 夹逼输入。

但 \(\varepsilon_{\mathcal F}\) 依赖地理族，不只依赖维数；而且 (27) 是围绕 \(-1\) 的窄夹逼。因此该受限结果本身既不证明也不证伪 Yau 第 26 题的维数一致宽夹逼命题。
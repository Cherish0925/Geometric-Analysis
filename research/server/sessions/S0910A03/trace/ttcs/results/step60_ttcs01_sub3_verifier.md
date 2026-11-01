# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A03/workspace/notes/step43_terminal_density_G_lemma.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A01/workspace/notes/step54_first_exit_continuation_derivation.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md"
  ]
}
```

## Task

Audit the terminal chart argument for the restricted four-dimensional Ishida–LeBrun route. Starting from Vol_T(P)≥cA, ∫𝔇_T≤Cδ²A (q_top≥0), uniform curvature on buffered plateau regions, and exponential-pullback ball averaging, verify the exact selection-and-limit chain: Liouville/Fubini inequality over p∈P, a selected pullback ball with mean density O(δ²), Rauch noncollapse and harmonic coordinates, strong W^{2,q}_loc convergence, and passage of the nonnegative density to zero on the whole limiting ball, sufficient for the calibrated-spectrum projector contradiction. Flag any flaw in claiming curvature convergence or pointwise vanishing from W^{2,q}; propose the minimal rigorous replacement if necessary. Also verify that A cancels and the resulting restricted conclusion is exclusion of sufficiently negative-pinched input metrics on a family already known to admit no Einstein metric—not merely exclusion of λ=-1 output metrics.

## Output

# 终端图表链的科学核验备忘录

## 1. 终端数据必须落在同一个缓冲集合上

令
\[
E_i=\operatorname{Ric}_{g_i(T)}+g_i(T),
\]
并采用 `step43_terminal_density_G_lemma.md` §5 的密度
\[
\mathfrak D_i
=
|E_i|^2+(s_i+4)^2
+(s_i+8\sqrt6\,|W_i^+|)^2+G_i ,
\qquad G_i\ge 0.
\]
终端论证需要同一个集合 \(P_i\) 同时满足：

\[
\operatorname{Vol}_{g_i(T)}(P_i)\ge c_0A_i,
\qquad
\int_{M_i}\mathfrak D_i\,d\mu_i\le C_0\delta_i^2A_i,
\tag{1}
\]
并且每个 \(p\in P_i\) 发出的长度不超过固定 \(\rho\) 的测地线都留在曲率受控的 plateau 内。

这里有一个集合层面的要点：若体积下界只对较大的中心集合成立，而测地缓冲只对其较小子集成立，就不能保证平均法选出的点具有所需图表。`step56_common_time_and_terminal_compactness.md` 使用 \(P^{\rm in}\) 同时承担这两项性质，因此在该记号下是连贯的。由终端双 Lipschitz 控制，初始 \(B_r\subset B_{5r}\) 的距离余量可以转化为终端余量；固定取
\[
0<\rho\le c\,r,\qquad K\rho^2\le c_{\rm R}
\tag{2}
\]
即可。

---

## 2. Liouville–Fubini 平均不等式

在
\[
\mathcal B_\rho(p)=\{v\in T_pM_i:|v|_{g_i(T)}<\rho\},
\qquad
\widetilde g_{i,p}=(\exp_p)^*g_i(T)
\]
上定义
\[
\mathscr A_\rho\mathfrak D_i(p)
=
\frac{\displaystyle\int_{\mathcal B_\rho(p)}
(\exp_p)^*\mathfrak D_i\,d\mu_{\widetilde g_{i,p}}}
{\displaystyle\operatorname{Vol}_{\widetilde g_{i,p}}
(\mathcal B_\rho(p))}.
\tag{3}
\]

设 \(j_i(p,u,t)\) 是指数映射的径向 Jacobian。由于所有相关径向测地线均留在 \(|\mathrm{Rm}|\le K\) 的区域，Rauch 比较在 \(0<t<\rho\) 上给出
\[
c_Rt^3\le j_i(p,u,t)\le C_Rt^3.
\tag{4}
\]
特别地，
\[
c_v\rho^4\le
\operatorname{Vol}_{\widetilde g_{i,p}}(\mathcal B_\rho(p))
\le C_v\rho^4.
\tag{5}
\]

记 \(SP_i=\{(p,u)\in SM_i:p\in P_i\}\)，\(\varphi_t\) 为测地流，\(dL\) 为 Liouville 测度。由 (4)–(5)，
\[
\begin{aligned}
\int_{P_i}\mathscr A_\rho\mathfrak D_i(p)\,d\mu_i(p)
&\le
\frac{C}{\rho^4}
\int_0^\rho t^3
\int_{SP_i}
\mathfrak D_i(\pi\varphi_tz)\,dL(z)\,dt.
\end{aligned}
\tag{6}
\]
测地流保持 \(dL\)，并且 \(\mathfrak D_i\ge0\)，故
\[
\begin{aligned}
\int_{SP_i}\mathfrak D_i(\pi\varphi_tz)\,dL(z)
&=
\int_{\varphi_t(SP_i)}\mathfrak D_i(\pi z)\,dL(z)\\
&\le
\int_{SM_i}\mathfrak D_i(\pi z)\,dL(z)
=
|S^3|\int_{M_i}\mathfrak D_i\,d\mu_i .
\end{aligned}
\tag{7}
\]
代回并积分 \(t^3\)，得到
\[
\boxed{
\int_{P_i}\mathscr A_\rho\mathfrak D_i\,d\mu_i
\le C_L(K,\rho)\int_{M_i}\mathfrak D_i\,d\mu_i .
}
\tag{8}
\]

这正是指数映射可以多重覆盖时所需的形式：积分按初始单位切向量计数，\(\varphi_t\) 是 \(SM_i\) 上的微分同胚，因此没有额外的覆盖重数。

由 (1) 和 (8)，存在 \(p_i\in P_i\) 满足
\[
\mathscr A_\rho\mathfrak D_i(p_i)
\le
\frac{C_LC_0\delta_i^2A_i}{c_0A_i}
=
\frac{C_LC_0}{c_0}\delta_i^2.
\tag{9}
\]
所以拓扑规模 \(A_i\) 完全消去。这里消去的只是增长因子 \(A_i\)；\(c_0,C_0,K,\rho\) 仍可依赖该 IL 地理族的参数。

结合 (5)，所选 pullback 球还满足
\[
\int_{\mathcal B_\rho(p_i)}
(\exp_{p_i})^*\mathfrak D_i\,d\mu_{\widetilde g_i}
\le C\delta_i^2\rho^4\longrightarrow0.
\tag{10}
\]

---

## 3. Rauch 几何与调和坐标紧性

由 \(K\rho^2\) 足够小，径向 Jacobi 场在 \(\mathcal B_\rho(p_i)\) 内没有共轭退化，故 \(\widetilde g_i=(\exp_{p_i})^*g_i(T)\) 是光滑正定度量。指数映射可以不单射，但这不影响 pullback 度量。

两侧截面曲率界、(5) 的体积下界以及向内缩小到固定球 \(\mathcal B_{\rho_1}\)，例如 \(\rho_1=\rho/4\)，给出统一调和半径。于是可在共同欧氏坐标域 \(U\) 上写成
\[
\lambda^{-1}\delta\le \widetilde g_i\le\lambda\delta,
\qquad
\|\widetilde g_i\|_{C^{1,\alpha}(U)}
+\|\widetilde g_i\|_{W^{2,q}(U)}
\le C_q
\tag{11}
\]
对每个有限 \(q\) 成立。取子列后，
\[
\widetilde g_i\to g_\infty
\quad\text{于 }C^{1,\beta}_{\rm loc},
\qquad
\widetilde g_i\rightharpoonup g_\infty
\quad\text{于 }W^{2,q}_{\rm loc}.
\tag{12}
\]

由 (10)，
\[
\|E_i\|_{L^2(U)}\to0.
\tag{13}
\]
曲率界给出 \(\|E_i\|_{L^\infty}\le C(K)\)，因此插值后
\[
E_i\to0\quad\text{于 }L^q_{\rm loc}
\quad\text{对每个有限 }q.
\tag{14}
\]

调和坐标中的 Ricci 方程是
\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=
-2(\operatorname{Ric}_{g_i})_{jk}
+Q_{jk}(g_i^{-1},\partial g_i)
=
2(g_i)_{jk}-2(E_i)_{jk}+Q_{i,jk}.
\tag{15}
\]
由 (12)、(14) 可传到极限：
\[
\operatorname{Ric}_{g_\infty}=-g_\infty
\tag{16}
\]
以弱方程意义成立。调和坐标椭圆正则性随后给出 \(g_\infty\in C^\infty\)。

强 \(W^{2,q}_{\rm loc}\) 收敛也能从同一方程得到。令 \(h_i=g_i-g_\infty\)，则
\[
L_i h_i
=
2h_i-2E_i+(Q_i-Q_\infty)
+(L_\infty-L_i)g_\infty .
\tag{17}
\]
右端在 \(L^q_{\rm loc}\) 中趋于零：\(E_i\to0\)，一阶度量收敛使 \(Q_i\to Q_\infty\)，系数收敛使最后一项趋于零。内点椭圆估计遂给出
\[
\boxed{
g_i\to g_\infty
\quad\text{强 }W^{2,q}_{\rm loc}
}
\tag{18}
\]
对每个有限 \(q\) 成立。

---

## 4. 曲率收敛与密度消失的严谨表述

有限 \(q\) 的强 \(W^{2,q}\) 收敛并不自动给出曲率在每一点收敛，也不产生 \(C^2\) 收敛。`step56_common_time_and_terminal_compactness.md` §4.4 中“曲率代数量在 \(W^{2,q}\) 下收敛”应精确写成：

\[
\operatorname{Rm}_{g_i}\to\operatorname{Rm}_{g_\infty}
\quad\text{强 }L^q_{\rm loc};
\tag{19}
\]
再取子列后，可得几乎处处收敛。

这是因为曲率等于度量二阶导数的线性项加上一阶导数的二次项。对 \(q>4\)，(18) 足以使前者强 \(L^q\) 收敛，后者由 \(C^{1,\beta}\) 收敛处理。

此外，\(W^+\) 的最小特征值是对称 \(3\times3\) 矩阵的 Lipschitz 函数；在统一曲率界下，
\[
G_i=f_i^2-(b_{i,-})^2
\]
也是曲率变量的统一局部 Lipschitz 函数。因此
\[
\mathfrak D_i\to\mathfrak D_\infty
\quad\text{于 }L^1_{\rm loc}.
\tag{20}
\]

对每个 \(K'\Subset U\)，由 (10) 和 (20)，
\[
0\le
\int_{K'}\mathfrak D_\infty\,d\mu_{g_\infty}
=
\lim_{i\to\infty}
\int_{K'}\mathfrak D_i\,d\mu_{g_i}
=0.
\tag{21}
\]
所以 \(\mathfrak D_\infty=0\) 几乎处处。极限度量已经光滑，\(\mathfrak D_\infty\) 是连续函数，故
\[
\mathfrak D_\infty\equiv0
\quad\text{在整个固定内球 }U.
\tag{22}
\]

因此最小严谨替代不是“曲率逐点收敛”，而是：

> 强 \(W^{2,q}_{\rm loc}\) 产生强 \(L^q_{\rm loc}\) 曲率收敛；密度在 \(L^1_{\rm loc}\) 中收敛；极限密度先几乎处处为零，再由极限度量的光滑性推广到内球每一点。

局部紧性只涉及固定缩小球，不需要讨论原始 pullback 球的外层球面。

---

## 5. 校准谱与投影子矛盾

由 (22)，极限上同时有
\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\qquad
s_\infty=-4,
\tag{23}
\]
\[
s_\infty+8\sqrt6|W_\infty^+|=0
\quad\Longrightarrow\quad
|W_\infty^+|^2=\frac1{24},
\tag{24}
\]
以及 \(G_\infty=0\)。`step43_terminal_density_G_lemma.md` Lemma 1.2 遂给出
\[
\operatorname{Spec}(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right)
\tag{25}
\]
在整个内球成立。注意 \(G=0\) 单独并不足够；必须与 (23)–(24) 同时使用。

Einstein 方程给出 \(\delta W_\infty^+=0\)。`step6_local_projector_obstruction_and_collapse_reduction.tex` 的常谱投影子引理于是推出
\[
\nabla W_\infty^+=0.
\tag{26}
\]
另一方面，同一文件中的 Einstein–Weyl 标量恒等式在
\[
s=-4,\quad |W^+|^2=\frac1{24},\quad
\det W^+=-\frac1{864}
\]
处给出
\[
|\nabla W^+|^2=\frac1{16},
\tag{27}
\]
与 (26) 不相容。因此不存在上述零密度极限球。

紧性反证于是产生固定常数
\[
\eta=\eta(K,\rho)>0
\]
使每个受控 pullback 球均满足
\[
\mathscr A_\rho\mathfrak D(p)\ge\eta.
\tag{28}
\]
与 (9) 比较，只要
\[
\delta<
\left(\frac{c_0\eta}{C_LC_0}\right)^{1/2},
\tag{29}
\]
终端选择点便不可能存在。

---

## 6. 得到的特定 IL 族结论

在 \(q_{\rm top}\ge0\) 时，`step43_terminal_density_G_lemma.md` 给出
\[
\int\mathfrak D_T\le119\,Q(T),
\]
没有额外拓扑项。结合 \(Q(T)\le C Q(0)\)、\(Q(0)\le C\delta^2\operatorname{Vol}(M)\) 以及 \(\operatorname{Vol}(M)\le CA\)，上述链条得到
\[
\boxed{
\inf_g
\left\|g^{-1}(\operatorname{Ric}_g+g)\right\|_{L^\infty,\mathrm{op}}
\ge \varepsilon_{\mathcal F}>0
}
\tag{30}
\]
其中 \(\varepsilon_{\mathcal F}\) 可依赖所选 Ishida–LeBrun 地理族，但不随 \(A_i\) 增长。

等价地，该族上不存在任意紧的
\[
-(1+\varepsilon_{\mathcal F})g
\le \operatorname{Ric}_g
\le -(1-\varepsilon_{\mathcal F})g
\tag{31}
\]
型输入度量。

这里的 \(\operatorname{Ric}_{g_\infty}=-g_\infty\) 只是终端 pullback 图表的局部极限方程，不是原问题所要求的全局输出度量。对题设中已经由 Ishida–LeBrun 理论排除所有 Einstein 常数 \(\lambda\) 的那些连通和成员，任意符号的 Einstein 输出都另已不存在；本论证新增的是输入端的归一化 Ricci 间隙，而不是仅仅排除 \(\lambda=-1\) 的输出。它也没有构造满足原始夹逼前提而不承载 Einstein 度量的流形，因此单凭这一特定族结论不能证伪 Yau 第 26 题。
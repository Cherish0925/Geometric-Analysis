# TTCS Independent Branch Record

```json
{
  "step_id": 46,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step42_uniform_gap_weight_terminal_repairs.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A01/workspace/notes/step16_exponential_pullback_averaging_review.md",
    "Sessions/S0910A03/workspace/notes/step43_terminal_density_G_lemma.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step45_preceptor_verdict_and_next_interface.md"
  ]
}
```

## Task

Independently verify the theorem statement, topological normalization, and terminal geometric passage in the assembled restricted Ishida–LeBrun negative-gap argument. Check the family-uniform contradiction split for bounded/unbounded A and q>=0; the O(A) curvature/volume input needed for support selection; terminal density constants and use of monopole classes at the flowed metric; retention of A-proportional inner-center volume; conversion of the normalized plateau flow to ordinary Ricci flow; local Shi estimates with a real spacetime buffer; exponential-pullback Liouville–Rauch averaging without base injectivity; strong convergence sufficient to pass G and Weyl eigenvalues; and the Derdzinski/projector contradiction. Attack any hidden assumption such as base noncollapse, unsupported smooth cutoffs, weak-to-strong curvature passage, or a mismatch between the density average and the pulled-back chart. Give exact repairs and state the strongest theorem actually supported, without treating it as a solution of full Yau Problem 26.

## Output

# 科学核验备忘录：Ishida–LeBrun 的 \(\operatorname{Ric}\approx-g\) 一致间隙

## 1. 总结

拓扑归一化
\[
(2\chi+3\tau)(M)=\frac{2A}{3}-q
\]
是正确的；\(q\ge0\) 序列的有界 \(A\)/无界 \(A\) 分拆也成立。经下述公式和构造修正后，支撑选取、终端密度、指数映射拉回、强曲率收敛以及 Derdziński/投影算子矛盾构成一条完整的终端链。

当前材料严格支撑的是：

> **经核验的归约定理。** 对指定的 Ishida–LeBrun 流形族，若同一个正则化极限流同时给出固定时间 \(T>0\)、\(Q_i(T)/A_i\to0\)、体积至少为 \(\alpha A_i\) 的平台中心集、平台上的真实时空曲率控制以及趋于恒等的双 Lipschitz 比较，则不存在
> \[
> \|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_{\infty,\mathrm{op}}\to0
> \]
> 的序列。因此该统一流命题蕴含一个与 \(A,N,q\) 无关的 \(\varepsilon_{\rm IL}>0\)。

所给文件尚未把所有一阶退出量——移动 Sobolev 常数、\(K_2,Y,J_6\)、全 \(p\) 缺陷估计、全局 \(Q\)、支撑几何和正则化极限——写成同一条自足定理并在同一解上联合证明。Step 45 给出了每个初值的构造途径，但每个初值的延拓本身不产生族上一致的观测时间。因而，从这些摘录本身尚不能推出无附加解析假设的 \(\varepsilon_{\rm IL}\) 定理。

---

## 2. 拓扑归一化与 \(A\) 的两种情形

设
\[
M=(\#_{j=1}^mX_j)\#N,\qquad m\in\{2,3\},
\]
并令
\[
A=\sum_jc_1^2(X_j),\qquad
D=4m-(2\chi+3\tau)(N),\qquad q=D-\frac A3.
\]
连通和公式给出
\[
(2\chi+3\tau)(M)=A-D=\frac{2A}{3}-q.
\]
若
\[
I=\frac1{4\pi^2}\int\left(\frac{s^2}{24}+2|W^+|^2\right),\qquad
J=\frac1{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2,
\]
则
\[
I-J=\frac{2A}{3}-q. \tag{2.1}
\]

需要把“Ishida–LeBrun 单极子族”写成明确的上同调假设。足够的形式是：存在对每个光滑度量均适用的单极子类
\[
\kappa_\varepsilon=C+\sum_\ell\varepsilon_\ell e_\ell,
\qquad \varepsilon_\ell=\pm1,
\qquad C^2=A,
\]
且符号平均消去交叉项。于是
\[
\operatorname{avg}_\varepsilon(\kappa_\varepsilon^+)^2
=(C^+)^2+\sum_\ell(e_\ell^+)^2
\ge A+\sum_\ell(e_\ell^+)^2.
\]
仅写 \(b_+(N)=0\) 并不足以自动产生这些类；定理陈述中“承载相应单极子族”是实质性假设。

定义
\[
\Delta_{\rm av}
=I-\frac{2A}{3}-\frac23\sum_\ell(e_\ell^+)^2.
\]
由混合 Seiberg–Witten 不等式和 (2.1)，
\[
\boxed{\;
\Delta_{\rm av}
=J-q-\frac23\sum_\ell(e_\ell^+)^2\ge0.
\;} \tag{2.2}
\]
因此在 \(q\ge0\) 时
\[
q+\frac23\sum_\ell(e_\ell^+)^2\le J. \tag{2.3}
\]

若
\[
\delta=\|g^{-1}(\operatorname{Ric}+g)\|_{\infty,\mathrm{op}},
\]
则
\[
|s+4|\le4\delta,\qquad
J\le\frac{\delta^2}{2\pi^2}\operatorname{Vol}(g).
\]
又因 \(|s|\ge4(1-\delta)\)，
\[
I\ge\frac{(1-\delta)^2}{6\pi^2}\operatorname{Vol}(g).
\]
结合 \(I\le2A/3+J\)，得到
\[
\bigl(1-2\delta-2\delta^2\bigr)\operatorname{Vol}(g)
\le4\pi^2A. \tag{2.4}
\]
故对充分小的 \(\delta\)，
\[
\operatorname{Vol}(g)=O(A),\qquad
\frac qA=O(\delta^2),\qquad \frac JA=O(\delta^2). \tag{2.5}
\]

这直接验证了序列分拆：

* 若 \(A_i\to\infty\)，所有归一化为 \(A_i^{-1}\) 的估计保持有效。
* 若 \(A_i\) 有界，则 \(A_i,D_i\in\mathbb Z\)，所以
  \[
  q_i=D_i-\frac{A_i}{3}\in\frac13\mathbb Z.
  \]
  由 \(q_i/A_i\to0\) 和 \(q_i\ge0\)，最终必有 \(q_i=0\)。无须事先假设 \(A_i\to\infty\)。

对 \(q>0\)，精确 Einstein 度量已由 \(q\le J=0\) 排除。\(q=0\) 的等号情形需要后面的局部曲率矛盾，不能只称作标准拓扑障碍。

---

## 3. 体积渐近与 \(O(A)\) 曲率能量

由 Step 43 使用的代数恒等式和单极子类 \(p=(\kappa^+)^2\ge A\)，
\[
\int(s+8\sqrt6|W^+|)^2
\le864\pi^2(J-q)=o(A). \tag{3.1}
\]
连同 \(s+4\to0\) 的 \(A^{-1}L^2\) 意义，可得
\[
4\pi^2I=\frac34\operatorname{Vol}(g)+o(A).
\]
而 \(I/A\to2/3\)，故
\[
\boxed{\quad
\frac{\operatorname{Vol}(g)}A\longrightarrow\frac{32\pi^2}{9}.
\quad} \tag{3.2}
\]

支撑选取还需要
\[
\int_M|\operatorname{Rm}|^2\le C A. \tag{3.3}
\]
这一点可以从给定几何推出，但 Step 41 没有展示其拓扑来源：

* 对最小一般型复曲面，
  \[
  c_2(X)=12\chi_h(X)-c_1^2(X),
  \]
  而 Noether 不等式给出
  \[
  c_1^2(X)\ge2p_g(X)-4,\qquad
  \chi_h(X)\le1+p_g(X),
  \]
  从而
  \[
  c_2(X)\le5c_1^2(X)+36.
  \]
  因 \(m\le3\) 且每个 \(c_1^2(X_j)\ge1\)，总和为 \(O(A)\)。

* 因 \(b_+(N)=0\)，
  \[
  (2\chi+3\tau)(N)=4-4b_1(N)-b_2(N),
  \]
  所以
  \[
  D=4m-4+4b_1(N)+b_2(N)=\frac A3+q=O(A).
  \]
  因此 \(|\chi(N)|=O(A)\)，进而 \(|\chi(M)|=O(A)\)。

* Gauss–Bonnet、\(\int|\operatorname{Ric}^{\circ}|^2=O(A)\) 和
  \(\int s^2=O(A)\) 给出 \(\int|W|^2=O(A)\)，从而得到 (3.3)。

这里没有使用任意小球的体积下界。

---

## 4. 支撑选取中的两处必要修正

### 4.1 临界能量阈值

若最大函数好点满足
\[
\fint_{B_{7r}(x)}|\operatorname{Rm}|^2
\le \frac{\eta^2}{C_{\rm BG}r^4},
\]
则 Bishop–Gromov 上体积估计给出
\[
\int_{B_{7r}(x)}|\operatorname{Rm}|^2\le\eta^2.
\]
Step 41 §2.5 中“缩小 \(r\) 即可使常数小于一”并不成立，因为
\[
\frac{V_{-2}(7r)}{r^4}\longrightarrow \omega_4\,7^4,
\]
而不是趋于零。正确做法是预先把最大函数阈值除以固定的
\(C_{\rm BG}\)。

弱型最大函数估计随后给出
\[
\operatorname{Vol}(\text{坏点集})
\le C\frac{r^4}{\eta^2}\int|\operatorname{Rm}|^2
\le C'\frac{r^4}{\eta^2}A.
\]
结合 (3.2)，固定足够小的 \(r\) 后，好点集体积至少为 \(cA\)。

### 4.2 平滑截断与着色

距离函数复合得到的截断只有 Lipschitz 正则性。一个严格构造是：先取光滑函数 \(\rho_x\) 满足
\[
|\rho_x-d(x,\cdot)|<r/10,\qquad |d\rho_x|\le2,
\]
再令固定光滑函数 \(\psi\) 在 \((-\infty,5.2r]\) 上等于 \(1\)，在
\([6.8r,\infty)\) 上等于 \(0\)，并置
\[
\chi_x=\psi(\rho_x).
\]
于是
\[
\chi_x=1\ \text{于 }B_{5r}(x),\qquad
\operatorname{supp}\chi_x\subset B_{7r}(x),\qquad
|d\chi_x|\le C/r.
\]
高阶导数对每个单独度量有限；不需要族上一致。

在 Ricci 下界下，小尺度度量空间具有统一倍增常数。因此一个
\(r\)-分离网在任意 \(14r\)-球中的点数有统一上界，其冲突图可用固定数目的颜色着色。由于所有 \(B_r(x)\) 覆盖好点集，至少一个颜色类满足
\[
\operatorname{Vol}\!\left(\bigcup_{\alpha}B_r(x_\alpha)\right)\ge\alpha A,
\]
同时该颜色类的 \(B_{7r}(x_\alpha)\) 两两不交。这验证了
\(A\)-比例的平台中心体积，无需基流形小球体积下界。

若
\[
\Lambda_i=\int_0^T\|a_i(\operatorname{Ric}+g)\|_{\infty,\mathrm{op}}\,dt
\longrightarrow0,
\]
则
\[
e^{-2\Lambda_i}g_i(0)\le g_i(t)\le e^{2\Lambda_i}g_i(0)
\]
以及
\[
\operatorname{Vol}_{g_i(T)}(P_i)
\ge e^{-4\Lambda_i}\operatorname{Vol}_{g_i(0)}(P_i)
\ge\frac{\alpha}{2}A_i.
\tag{4.1}
\]

---

## 5. 终端密度与常数

光滑流不改变流形、定向或单极子类集合。终端时刻可重新选择一个符号类，使
\[
p_i=(\kappa_i^+(T))^2\ge A_i.
\]
因此所有 LeBrun 不等式都可直接用于 \(g_i(T)\)，不需要沿流运输调和代表。

令
\[
E=\operatorname{Ric}+g,\qquad Q=\int|E|^2,\qquad
R=\frac1{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2.
\]
则
\[
R\le\frac{Q}{8\pi^2},\qquad
\int(s+4)^2\le4Q. \tag{5.1}
\]
由
\[
27\left(\frac{s^2}{24}+2|W^+|^2\right)
-(s-\sqrt6|W^+|)^2
=\frac18(s+8\sqrt6|W^+|)^2
\]
和 \(p\ge A\)，
\[
\int(s+8\sqrt6|W^+|)^2
\le864\pi^2(R-q)\le108Q. \tag{5.2}
\]

Step 43 所用的另一个实质输入应明确写为
\[
\int\left[\left(\frac23s+2w\right)_-\right]^2
\ge32\pi^2p, \tag{5.3}
\]
即 LeBrun 的广义 Yamabe 谱估计。设
\[
f=\frac23s-2\sqrt{\frac23}|W^+|,\qquad
b=\frac23s+2w,\qquad
G=f^2-(b_-)^2.
\]
点态有 \(G\ge0\)，而 (5.3) 给出
\[
\int G\le6Q\qquad(q\ge0). \tag{5.4}
\]

因此应统一定义
\[
\boxed{\;
\mathfrak D
=|E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+G,
\qquad
\int\mathfrak D\le119Q.
\;} \tag{5.5}
\]

Step 41 §7.4 把密度写成带 \(1/(4\pi^2)\) 的另一种缩放、遗漏
\(|E|^2\)，却继续使用常数 \(119\)；这两种写法不相容。后续选择和收敛应统一使用 (5.5)。

Step 41 §7.2 的第二个等式也应改为
\[
\Delta_{\rm av}(T)
=J(T)-q-\frac23\sum_\ell(e_\ell^+(T))^2,
\]
不能写成带 \((\sum(e_\ell^+)^2-A)\) 的表达式。

---

## 6. 平台流、普通 Ricci 流与真实时空缓冲

在固定开集 \(\{a=1\}\) 上，
\[
\partial_tg=-2(\operatorname{Ric}+g).
\]
置
\[
\bar g(\tau)=e^{2t}g(t),\qquad
\tau=\frac{e^{2t}-1}{2},
\]
则
\[
\partial_\tau\bar g=-2\operatorname{Ric}_{\bar g}. \tag{6.1}
\]
因此平台内部确实是普通 Ricci 流的时空重参数化，而不只是终端切片上的形式相似。

要使用局部 Shi 估计，必须有一个时空缓冲，而不仅是终端曲率界。固定
\[
P_i\subset\bigcup B_r(x_\alpha),\qquad
\{a=1\}\supset\bigcup B_{5r}(x_\alpha).
\]
由 (4.1)，对所有 \(t\in[0,T]\)，从 \(p\in P_i\) 出发、长度至多
\(4\rho\) 的 \(g_i(t)\)-曲线仍位于 \(B_{3r}^{g_i(0)}(x_\alpha)\)，只要取固定
\[
\rho<r/4
\]
并令 \(i\) 充分大。若 Moser 估计在
\([T/2,T]\) 给出平台上的 \(|\operatorname{Rm}|\le K\)，则普通局部 Shi 定理给出
\[
\sup_{B_\rho^{g_i(T)}(p)}
|\nabla^k\operatorname{Rm}_{g_i(T)}|
\le C_k(K,T^{-1},\rho^{-1}). \tag{6.2}
\]
这些估计不使用基流形的注入半径。对正则化系数
\(b_\varepsilon=1+\varepsilon^2\)，同样结论由常数时间重参数化得到，且
\(b_\varepsilon\) 保持在固定紧区间内。

---

## 7. 指数映射拉回与强收敛

选择
\[
\rho<\min\left\{\frac r4,\frac{\pi}{2\sqrt K}\right\}.
\]
对 \(p\in P_i\)，长度不超过 \(\rho\) 的终端径向测地线均留在平台时空缓冲的终端切片。由
\(-K\le\sec\le K\)，Rauch 比较给出
\[
s_K(t)^3\le J_p(t,\xi)\le s_{-K}(t)^3.
\]
对任何 \(F\ge0\)，Step 16 的 Liouville 计算严格给出
\[
\int_{P_i}A_\rho F(p)\,d\mu(p)
\le C(K,\rho)\int_MF\,d\mu.
\tag{7.1}
\]
指数映射可多次覆盖同一基点；Liouville 测度本来就按这些访问次数积分，因此无需基流形注入半径。

取 \(F=\mathfrak D_i\)，由 (4.1)、(5.5) 和 \(Q_i(T)/A_i\to0\)，存在
\(p_i\in P_i\) 使
\[
A_\rho\mathfrak D_i(p_i)\to0. \tag{7.2}
\]
若
\[
\widehat g_i=(\exp_{p_i}^{g_i(T)})^*g_i(T)
\]
定义在 \(B_\rho(0)\subset T_{p_i}M_i\)，则 (7.2) 的分子恰是
\[
\int_{B_\rho(0)}
(\exp_{p_i})^*\mathfrak D_i\,d\mu_{\widehat g_i}. \tag{7.3}
\]
这消除了“密度平均是否与拉回图一致”的疑问。缩到任意固定
\(B_{\rho'}(0)\)，其积分仍趋于零，而 Rauch 给出统一的体积下界。

由 (6.2) 可在选取正交标架识别 \(T_{p_i}M_i\simeq\mathbb R^4\) 后取得光滑局部收敛。若只使用调和坐标，则必须先获得
\[
\widehat g_i\to g_\infty
\quad\text{强收敛于 }W_{\mathrm{loc}}^{2,p},\quad p>4.
\]
单纯的弱 \(W^{2,p}\) 收敛不足以传递二次量 \(G\)。可由调和坐标 Ricci 方程的差分估计获得强收敛；平台 Shi 估计则直接给出更强的光滑收敛。

Weyl 特征值对对称矩阵系数是 Lipschitz 连续的，故强曲率收敛足以传递
\(|W^+|\)、最小特征值 \(w\) 和 \(G\)。由 (7.3) 及各项均 \(\ge0\)，极限满足
\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\qquad
s_\infty=-4,\qquad
|W_\infty^+|^2=\frac1{24},\qquad
G_\infty=0. \tag{7.4}
\]

---

## 8. Derdziński 与投影算子矛盾

在 (7.4) 中
\[
f=-3,\qquad
\xi=w+\sqrt{\frac23}|W^+|\ge0,\qquad b=f+2\xi.
\]
由 \(G=f^2-(b_-)^2=0\) 可得 \(\xi=0\)，因此
\[
w=-\frac16.
\]
迹为零和范数平方 \(1/24\) 随即给出
\[
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right). \tag{8.1}
\]

Einstein 方程蕴含 \(\delta W^+=0\)。Derdziński 命题于是说明
\[
(24|W^+|^2)^{1/3}g_\infty
\]
局部 Kähler；这里因 \(|W^+|^2=1/24\)，共形因子恒为 \(1\)，故
\(g_\infty\) 本身局部 Kähler。但 Kähler 四维度量满足
\[
|W^+|^2=\frac{s^2}{24},
\]
而 \(s=-4\) 给出 \(2/3\)，与 \(1/24\) 矛盾。

Step 6 的投影算子计算提供独立验证。写
\[
W^+=\mu I+(\lambda-\mu)P_\omega
\]
，其中 \(\omega\) 张成单特征线。常特征值和 \(\delta W^+=0\) 给出
\[
(\nabla^a\omega_{ab})\omega_{cd}
+\omega_{ab}\nabla^a\omega_{cd}=0.
\]
与 \(\omega^{cd}\) 收缩后得到 \(\nabla^a\omega_{ab}=0\)，再代回并利用自对偶二形式的非退化性，得到 \(\nabla\omega=0\)。因此 \(\omega\) 定义局部平行 Kähler 结构，同样与 (8.1) 不相容。

---

## 9. 当前材料支撑的精确强度

拓扑代数、\(A\)-归一化体积、\(O(A)\) 曲率能量、塌缩兼容的支撑选取、终端常数 \(108,6,119\)、终端重新选择单极子类、平台体积保留、普通 Ricci 流转换、局部 Shi 正则性、Liouville–Rauch 选择、强曲率传递以及局部曲率矛盾，在上述修正后相互一致。

尚需由统一流命题提供的具体数据是
\[
T,r,\alpha,K>0
\]
与 \(i\) 无关，并且在同一个光滑极限流上同时满足
\[
\frac{Q_i(T)}{A_i}\to0,\qquad
\operatorname{Vol}_{g_i(T)}(P_i)\ge\alpha A_i,
\]
\[
\{a_i=1\}\text{ 含有固定宽度的时空缓冲},\qquad
|\operatorname{Rm}|\le K\text{ 于该缓冲的 }[T/2,T],
\]
以及
\[
\int_0^T\|a_i(\operatorname{Ric}+g)\|_\infty\,dt\to0.
\]
这些数据一旦联合成立，族上一致的 \(\varepsilon_{\rm IL}\) 由序列反证立即得到。

该结果只涉及四维特定 Ishida–LeBrun 流形族和 \(\operatorname{Ric}\approx-g\) 的归一化，不给出一般四流形、其他维数或完整 Yau 第 26 题所需的维数常数与 Lean 4 形式证明。
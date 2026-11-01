# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 46,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step46_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step46_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the theorem statement, topological normalization, and terminal geometric passage in the assembled restricted Ishida–LeBrun negative-gap argument. Check the family-uniform contradiction split for bounded/unbounded A and q>=0; the O(A) curvature/volume input needed for support selection; terminal density constants and use of monopole classes at the flowed metric; retention of A-proportional inner-center volume; conversion of the normalized plateau flow to ordinary Ricci flow; local Shi estimates with a real spacetime buffer; exponential-pullback Liouville–Rauch averaging without base injectivity; strong convergence sufficient to pass G and Weyl eigenvalues; and the Derdzinski/projector contradiction. Attack any hidden assumption such as base noncollapse, unsupported smooth cutoffs, weak-to-strong curvature passage, or a mismatch between the density average and the pulled-back chart. Give exact repairs and state the strongest theorem actually supported, without treating it as a solution of full Yau Problem 26.

## Integrated Scientific Memo

# 核验结论：受限 Ishida–LeBrun 负间隙论证

## 1. 最强可支持结论

现有材料完整支持的是一个**终端几何归约定理**，尚不足以无条件证明族上一致的负 Ricci 间隙。

> **经核验的条件归约。**  
> 设 \(M_i\) 属于指定的四维 Ishida–LeBrun 流形族，\(q_i\ge0\)，且
> \[
> \|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_{\infty,\mathrm{op}}\to0.
> \]
> 若同一个正则化极限流在统一时间 \(T>0\) 产生终端度量 \(g_i(T)\)，并同时满足：
> \[
> Q_i(T)/A_i\to0,\qquad Q_i(T)=\int|\operatorname{Ric}_{g_i(T)}+g_i(T)|^2,
> \]
> 存在中心集 \(P_i\) 及统一常数 \(\alpha,\rho,K>0\)，使
> \[
> \operatorname{Vol}_{g_i(T)}P_i\ge\alpha A_i,
> \]
> 且每个 \(p\in P_i\) 的半径 \(\rho\) 指数拉回域位于一个真实的正时间平台缓冲中，其上
> \[
> |\operatorname{Rm}|\le K,
> \]
> 那么终端密度、Liouville–Rauch 平均和局部 Derdziński 矛盾排除该序列。
>
> 因而，一个同时给出上述输出的**族上一致 first-exit/平滑流定理**将推出某个与 \(A,D,q,N\) 无关的 \(\varepsilon_{\rm IL}>0\)。

所给文件没有把移动 Sobolev 控制、\(K_2,Y,J_6\)、全 \(p\) 缺陷阶梯、全局 \(Q\)、支撑几何及正则化极限在**同一个解和同一个统一时间区间**上联合证明。因此目前不能把无条件的 \(\varepsilon_{\rm IL}\) 间隙定理视为已完成。

这即使完成，也只是四维、负归一化、特定 Ishida–LeBrun geography 的结果，不是 Yau 第 26 题的完整解答。

---

## 2. 拓扑归一化与有界/无界 \(A\) 分拆

令
\[
M=(\#_{j=1}^{m}X_j)\#N,\qquad m\in\{2,3\},
\]
\[
A=\sum_jc_1^2(X_j),\qquad
D=4m-(2\chi+3\tau)(N),\qquad
q=D-\frac A3.
\]
连通和公式严格给出
\[
(2\chi+3\tau)(M)=A-D=\frac{2A}{3}-q. \tag{2.1}
\]
因此，若
\[
I=\frac1{4\pi^2}\int\left(\frac{s^2}{24}+2|W^+|^2\right),\qquad
J=\frac1{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2,
\]
则
\[
I-J=\frac{2A}{3}-q. \tag{2.2}
\]

必须把“承载 Ishida–LeBrun monopole family”保留为实质假设；仅有 \(b_+(N)=0\) 不自动给出所需全部单极子类。若
\[
\kappa_\varepsilon=C+\sum_\ell\varepsilon_\ell e_\ell,\qquad C^2=A,
\]
是对每个光滑度量均有效的单极子类族，则符号平均给出
\[
I\ge \frac23\left(A+\sum_\ell(e_\ell^+)^2\right).
\]
故正确的平均缺陷为
\[
\boxed{
\Delta_{\rm av}
=I-\frac{2A}{3}-\frac23\sum_\ell(e_\ell^+)^2
=J-q-\frac23\sum_\ell(e_\ell^+)^2\ge0.
} \tag{2.3}
\]
Step 41 §7.2 中带
\(\sum(e_\ell^+)^2-A\) 的终端表达式是错误的，应改为 (2.3)。

当 \(q\ge0\) 时，
\[
q+\frac23\sum_\ell(e_\ell^+)^2\le J. \tag{2.4}
\]
近 Einstein 条件以及校准体积给出
\[
\frac JA\to0,\qquad \frac qA\to0,\qquad
\frac{\Delta_{\rm av}}A\to0.
\]

族上一致反证中的两种情形均成立：

* \(A_i\to\infty\)：使用所有 \(A_i^{-1}\)-归一化估计；
* \(A_i\) 有界：取子列令 \(A_i=A_0\)。由于
  \[
  q_i=D_i-\frac{A_i}{3}\in\frac13\mathbb Z,\qquad q_i\ge0,
  \]
  且 \(q_i/A_i\to0\)，最终 \(q_i=0\)。

但第二种情形并非由固定拓扑的 collapse reduction 自动闭合；它仍需同一个终端流模块。

---

## 3. \(O(A)\) 体积和曲率输入

校准恒等式与单极子估计给出
\[
\frac{\operatorname{Vol}(g_i)}{A_i}\longrightarrow
\frac{32\pi^2}{9}. \tag{3.1}
\]
因此初始总体积既是 \(O(A)\)，又有正的 \(A\)-比例下界。

支撑选取还需要
\[
\int_M|\operatorname{Rm}|^2\le C A. \tag{3.2}
\]
这可以由现有拓扑和 Chern–Weil 数据推出：

* \(m\le3\)，一般型曲面的 Euler 数总和为 \(O(A)\)；
* \(b_+(N)=0\) 时
  \[
  (2\chi+3\tau)(N)=4-4b_1(N)-b_2(N),
  \]
  而 \(D=A/3+q=O(A)\)，故相关 Betti/Euler 数为 \(O(A)\)；
* \(\int s^2=O(A)\)、\(\int|\operatorname{Ric}^{\circ}|^2=O(A)\)，再由 Gauss–Bonnet 和 signature 控制 Weyl 能量。

该推导不需要基流形的局部非塌缩。

---

## 4. 支撑选取的精确修复

### 4.1 临界能量阈值

Step 41 中“通过缩小 \(r\) 将归一化小能量变成所需的非归一化小能量”并不正确，因为四维中
\[
\frac{V_{-2}(7r)}{r^4}\to \omega_4\,7^4,
\]
不会趋于零。

正确做法是从一开始选择较强的最大函数阈值：
\[
\fint_{B_{7r}(x)}|\operatorname{Rm}|^2
\le \frac{\eta^2}{C_{\rm BG}r^4}, \tag{4.1}
\]
其中 \(C_{\rm BG}\) 吸收 Bishop–Gromov 上体积常数。于是
\[
\int_{B_{7r}(x)}|\operatorname{Rm}|^2\le\eta^2. \tag{4.2}
\]
弱型最大函数估计则给出
\[
\operatorname{Vol}(\mathrm{bad})
\le C\frac{r^4}{\eta^2}\int|\operatorname{Rm}|^2
\le C'\frac{r^4}{\eta^2}A. \tag{4.3}
\]
固定充分小的 \(r\) 后，good set 具有 \(cA\) 体积。

### 4.2 平滑截断不能直接由距离函数得到

\(\varphi(d(x,\cdot)/r)\) 只有 Lipschitz 正则性。“mollify while preserving everything”需要明确实现。可取平滑距离近似 \(\rho_x\)：
\[
|\rho_x-d(x,\cdot)|<r/10,\qquad |d\rho_x|\le2,
\]
再令
\[
\chi_x=\psi(\rho_x),
\]
其中 \(\psi=1\) 于 \((-\infty,5.2r]\)，\(\psi=0\) 于
\([6.8r,\infty)\)。于是
\[
\chi_x=1\text{ 于 }B_{5r}(x),\quad
\operatorname{supp}\chi_x\subset B_{7r}(x),\quad
|d\chi_x|\le C/r.
\]
高阶导数只需对每个单独初值有限；材料没有也不应声称它们族上一致。

### 4.3 着色与内中心体积

Ricci 下界给出固定尺度倍增和统一冲突图度数。对 \(r\)-分离网作有限着色后，可取一个颜色类使 \(B_{7r}\) 两两不交且
\[
\operatorname{Vol}\left(\bigcup_\alpha B_r(x_\alpha)\right)
\ge \alpha A. \tag{4.4}
\]
Bishop–Gromov 比例还可由 \(B_{5r}\) 平台体积推出 \(B_r\) 内中心体积的同阶下界。

若
\[
\Lambda_i=\int_0^T\|a_i(\operatorname{Ric}+g)\|_{\infty,\mathrm{op}}\,dt
\to0,
\]
则
\[
e^{-2\Lambda_i}g_i(0)\le g_i(t)\le e^{2\Lambda_i}g_i(0),
\]
所以终端仍有
\[
\operatorname{Vol}_{g_i(T)}P_i\ge \frac{\alpha}{2}A_i. \tag{4.5}
\]

---

## 5. 终端密度：正确归一化与常数

流保持底层光滑流形和定向。终端时刻应按 \(g_i(T)\) 的 Hodge 分解**重新选择**符号单极子类，使
\[
p_i=(\kappa_i^+(T))^2\ge A_i.
\]
无须沿流运输某个调和代表。

记
\[
E=\operatorname{Ric}+g,\qquad Q=\int|E|^2,\qquad
R=\frac1{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2.
\]
则
\[
R\le \frac{Q}{8\pi^2},\qquad
\int(s+4)^2\le4Q. \tag{5.1}
\]
代数恒等式和 monopole 下界给出
\[
\int(s+8\sqrt6|W^+|)^2
\le864\pi^2(R-q)
\le108Q\qquad(q\ge0). \tag{5.2}
\]

设
\[
f=\frac23s-2\sqrt{\frac23}|W^+|,\qquad
b=\frac23s+2w,\qquad
G=f^2-(b_-)^2.
\]
点态 \(G\ge0\)。终端谱缺陷估计使用的关键外部输入是
\[
\int(b_-)^2\ge32\pi^2p, \tag{5.3}
\]
即 LeBrun 广义 Yamabe 谱估计；在其适用于任意终端光滑度量的准确版本下，
\[
\int G\le6Q\qquad(q\ge0). \tag{5.4}
\]

因此应统一使用
\[
\boxed{
\mathfrak D
=|E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+G,
\qquad
\int\mathfrak D\le119Q.
} \tag{5.5}
\]
其中
\[
119=1+4+108+6.
\]

Step 41 §7.4 中带 \(1/(4\pi^2)\)、给第二项加 \(1/16\)、并遗漏
\(|E|^2\) 的定义与常数 \(119\) 不相容，必须删除或重新缩放，不能与 (5.5) 混用。

谱估计 (5.3) 在给定文件中仍是引用性输入，而非自足证明。要将终端模块完全内部闭合，需要核准其原始定理陈述、适用对象及常数 \(32\pi^2\)。

---

## 6. 平台上的普通 Ricci 流及真实时空缓冲

在固定开集 \(\{a=1\}\) 上，
\[
\partial_tg=-2(\operatorname{Ric}+g). \tag{6.1}
\]
令
\[
\bar g(\tau)=e^{2t}g(t),\qquad
\tau=\frac{e^{2t}-1}{2},
\]
则
\[
\partial_\tau\bar g=-2\operatorname{Ric}_{\bar g}. \tag{6.2}
\]
因此平台内部确实是普通 Ricci 流的缩放和时间重参数化。

局部 Shi 估计不能只从终端切片的曲率界推出；需要一个真实时空缓冲。取
\[
P_i\subset\bigcup B_r^{g_i(0)}(x_\alpha),\qquad
\{a=1\}\supset\bigcup B_{5r}^{g_i(0)}(x_\alpha).
\]
利用整个 \([0,T]\) 上的双 Lipschitz 比较，选固定 \(\rho<r/4\)，使从
\(P_i\) 出发的相关 \(g_i(t)\)-球在所有 \(t\in[T/2,T]\) 都位于
\(B_{5r}^{g_i(0)}\) 平台内。若 first-exit/Moser 输出给出
\[
|\operatorname{Rm}|\le K
\quad\text{于该缓冲的 }[T/2,T],
\]
则局部 Shi 估计给出
\[
\sup_{B_\rho^{g_i(T)}(p)}
|\nabla^k\operatorname{Rm}_{g_i(T)}|
\le C_k(K,T^{-1},\rho^{-1}). \tag{6.3}
\]
该步骤不要求基流形注入半径下界，但它严格依赖尚待联合证明的统一平台曲率输出。

---

## 7. Liouville–Rauch 平均与拉回图完全一致

取
\[
\rho<\min\left\{\frac r4,\frac{\pi}{2\sqrt K}\right\}.
\]
若每条长度不超过 \(\rho\) 的径向测地线都位于 \(|\sec|\le K\) 的缓冲内，则
\[
s_K(t)^3\le J_p(t,\xi)\le s_{-K}(t)^3.
\]
对于任何 \(F\ge0\)，Liouville 不变性严格给出
\[
\int_{P_i}A_\rho F(p)\,d\mu(p)
\le C(K,\rho)\int_{M_i}F\,d\mu. \tag{7.1}
\]
指数映射的多重覆盖只是在 Liouville 积分中多次计数；因 \(F\ge0\)，不会造成问题。无需基流形的 cut-locus 分解、注入半径或 deck group 控制。

应用于 \(F=\mathfrak D_i\)，由
\[
\operatorname{Vol}P_i\ge\alpha A_i,\qquad
\int\mathfrak D_i/A_i\to0,
\]
可选 \(p_i\in P_i\) 使
\[
A_\rho\mathfrak D_i(p_i)\to0. \tag{7.2}
\]

令
\[
\widehat g_i=(\exp_{p_i}^{g_i(T)})^*g_i(T)
\quad\text{于 }B_\rho(0)\subset T_{p_i}M_i.
\]
由于指数映射在该范围是局部等距浸入，
\[
A_\rho\mathfrak D_i(p_i)
=
\frac{\displaystyle\int_{B_\rho(0)}
(\exp_{p_i})^*\mathfrak D_i\,d\mu_{\widehat g_i}}
{\displaystyle\operatorname{Vol}_{\widehat g_i}B_\rho(0)}. \tag{7.3}
\]
所以不存在“Liouville 平均的密度与紧性所用拉回图不匹配”的问题。

Rauch 给出拉回域中心球的统一正体积下界，即使基流形完全塌缩也成立。

---

## 8. 强收敛及曲率谱的传递

仅有弱 \(W^{2,p}\) 收敛不足以传递二次曲率密度 \(G\)。可采用两种严格路径：

1. 用 §6 的局部 Shi 导数界直接取得较小拉回球上的光滑收敛；
2. 或用有界曲率和 Rauch 非塌缩取得 harmonic radius，再由
   \[
   g_i^{ab}\partial_a\partial_b(g_i)_{jk}
   =-2(\operatorname{Ric}_{g_i})_{jk}
   +Q_{jk}(g_i^{-1},\partial g_i)
   \]
   的差分椭圆估计取得
   \[
   \widehat g_i\to g_\infty
   \quad\text{强收敛于 }W_{\mathrm{loc}}^{2,p},\qquad p>4. \tag{8.1}
   \]

平台上的统一曲率界和 \(\int|E_i|^2\to0\) 还给出所有有限 \(p\) 的
\[
\|E_i\|_{L^p_{\rm loc}}\to0
\]
（通过有界性插值）。因此极限弱满足
\[
\operatorname{Ric}_{g_\infty}=-g_\infty,
\]
再由 harmonic-coordinate Einstein 方程自举为光滑。

强 \(W^{2,p}\) 收敛给出曲率的强 \(L^p\) 收敛。对称矩阵最小特征值关于矩阵系数是 Lipschitz 的，故可以传递
\[
|W^+|,\qquad w=\lambda_{\min}(W^+),\qquad G.
\]
于是终端密度趋零推出
\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\qquad
s_\infty=-4,\qquad
|W_\infty^+|^2=\frac1{24},\qquad
G_\infty=0. \tag{8.2}
\]

此前从 \(C^0\)-小 Einstein 缺陷直接声称 \(W^{4,p}\) 的步骤不成立，且完全不需要。

---

## 9. Derdziński／投影算子矛盾

在 (8.2) 下，
\[
f=-3,\qquad
\xi=w+\sqrt{\frac23}|W^+|\ge0,\qquad
b=f+2\xi.
\]
此时
\[
G=4\xi(3-\xi).
\]
由 \(G=0\) 及允许范围可得 \(\xi=0\)，故
\[
w=-\frac16.
\]
再由迹为零和 \(|W^+|^2=1/24\)，得到
\[
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right). \tag{9.1}
\]

Einstein 方程蕴含
\[
\delta W^+=0.
\]
Derdziński 定理说明
\[
(24|W^+|^2)^{1/3}g_\infty
\]
局部 Kähler。因 \(24|W^+|^2=1\)，\(g_\infty\) 本身局部 Kähler。但 Kähler 四维度量满足
\[
|W^+|^2=\frac{s^2}{24},
\]
故 \(s=-4\) 时应为 \(2/3\)，与 \(1/24\) 矛盾。

投影算子计算给出独立核验：常双特征值分解
\[
W^+=\mu I+(\lambda-\mu)P_\omega
\]
结合 \(\delta W^+=0\) 先推出 \(\delta\omega=0\)，继而由自对偶二形式的非退化性推出
\(\nabla\omega=0\)，故 \(\nabla W^+=0\)。另一方面该常谱代入 Einstein–Weyl Weitzenböck 恒等式要求
\[
|\nabla W^+|^2=\frac1{16},
\]
再次矛盾。

---

## 10. 尚未闭合的精确对象

剩余问题不是终端几何，而是一个联合、塌缩稳健的流定理：

\[
\boxed{\text{同一正则化极限流上的统一 first-exit package}}
\]

它必须在统一 \(T,r>0\) 上同时证明：

\[
Q_i(T)/A_i\to0,
\qquad
\operatorname{Vol}_{g_i(T)}P_i\ge\alpha A_i,
\]
\[
|\operatorname{Rm}|\le K
\quad\text{于固定宽度平台缓冲的 }[T/2,T],
\]
\[
\int_0^T\|a_i(\operatorname{Ric}+g)\|_\infty\,dt\to0,
\]
并联合保持所用移动 Sobolev 不等式、\(K_2,Y,J_6\)、全 \(p\) 缺陷阶梯和全局 \(Q\)。

Step 45 修复了若干高阶权重结构并给出 per-datum 正则化构造路线，但：

* per-datum 延拓不自动给出族上一致时间；
* 标量 partition 脚本不等于完整 tensor/PDE 证明；
* 尚缺上述所有 first-exit 量在同一个极限解上的联合闭合；
* 终端 \(G\) 界仍需把 LeBrun 谱下界 (5.3) 的精确原始定理和适用条件核准为正式依赖。

因此，当前严格状态是：**拓扑归一化、支撑选择的修正版以及整个终端几何链成立；族上一致受限负间隙仍是条件性的。**
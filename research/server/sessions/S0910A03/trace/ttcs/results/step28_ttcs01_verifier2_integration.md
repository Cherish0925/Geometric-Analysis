# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 28,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step28_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step28_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the downstream geometric passage from the terminal cutoff-flow metrics to the forbidden calibrated Einstein germ. Focus on whether the good-support/Vitali construction truly supplies a positive-volume set with a fixed terminal-metric geodesic buffer; whether the exponential-pullback averaging inequality supplies a noncollapsed smooth chart despite collapse and sheet multiplicity; whether global terminal L2 defect can be converted, after rebuilding the Seiberg-Witten objects for that same terminal metric, into one joint nonnegative density whose pullback limit has nonzero harmonic self-dual form in the lowest W+ eigenspace; and whether the Step 6 projector/Einstein-Weyl contradiction then follows. Distinguish fixed topology from varying topology. Identify every load-bearing statement still asserted rather than proved, and formulate the shortest rigorous bridge that would close it if possible.

## Integrated Scientific Memo

# 下游几何链条核验：终端截断流度量到禁戒校准 Einstein germ

## 结论

在**固定的临界 Ishida–LeBrun 四流形、负归一化分支**上，下游链条可以严格表述为一个条件性定理：

> 若截断归一化 Ricci 流在统一正时间产生一个占总体积固定比例、具有固定终端测地缓冲并带全部曲率导数界的平台，同时终端全局 Ricci 缺陷满足  
> \[
> Q_i:=\int_{M}|\,\Ric_{\bar g_i}+\bar g_i\,|^2\,d\mu_{\bar g_i}\to0,
> \]
> 则指数拉回平均选出固定半径的非塌缩光滑图；在**同一个终端度量**上重建 Seiberg–Witten 数据后，联合非负密度选出非零定长的自对偶调和二形式，位于 \(W^+\) 的最低特征线；极限 Einstein germ 具有
> \[
> s=-4,\qquad
> \Spec(W^+)=\left(-\frac16,\frac1{12},\frac1{12}\right),
> \]
> 与 Step 6 的 projector/Einstein–Weyl 恒等式矛盾。

指数平均、联合密度、谱确定和 Step 6 矛盾本身没有发现新的几何障碍。未闭合的核心仍是产生该终端平台的塌缩一致抛物定理；此外，正部 rescaled monopole 到同一个 \(H_i\) 的书面化引理尚需补齐。

---

## 1. 正体积平台与终端测地缓冲

Step 23 所称“稀疏后支撑互不相交且内球仍占固定体积比例”不能仅由 Vitali 一句话推出；需要以下定量版本。

设初始好点集 \(G_i\) 满足
\[
\Vol_{g_i(0)}G_i\ge \alpha\,\Vol_{g_i(0)}M_i,
\]
并有统一 Ricci 下界。取 \(G_i\) 中极大的 \(12r\)-分离集 \(\{p_{ij}\}\)。则
\[
B_{6r}(p_{ij})\ \text{两两不交},\qquad
G_i\subset\bigcup_jB_{12r}(p_{ij}).
\]
Bishop–Gromov 比较给出
\[
\Vol B_{12r}(p_{ij})
 \le D(n,\Lambda,r)\Vol B_{2r}(p_{ij}),
\]
故
\[
P_i^0:=\bigcup_j B_{2r}^{g_i(0)}(p_{ij})
\]
满足
\[
\Vol_{g_i(0)}P_i^0
 \ge \frac{\alpha}{D}\Vol_{g_i(0)}M_i. \tag{1}
\]

若终端度量 \(\bar g_i=g_i(T_0)\) 与初始度量统一双 Lipschitz：
\[
L^{-1}g_i(0)\le \bar g_i\le Lg_i(0), \tag{2}
\]
则
\[
\Vol_{\bar g_i}P_i^0\ge c(n,\alpha,D,L)\Vol_{\bar g_i}M_i. \tag{3}
\]

对 \(p\in B_{2r}^{g_i(0)}(p_{ij})\)，任一长度不超过 \(\rho\) 的 \(\bar g_i\)-测地线满足
\[
d_{g_i(0)}(p_{ij},\gamma(t))
 \le 2r+\sqrt L\,\rho.
\]
取 \(\rho\le r/\sqrt L\)，整条测地线均留在 \(B_{3r}^{g_i(0)}(p_{ij})\)，因而处于 plateau 内。

因此，**Vitali/Bishop–Gromov 加终端双 Lipschitz 漂移确实给出正体积与固定终端测地缓冲**。但这些假设尚未在所给材料中被一个完整流定理同时证明。特别地，Step 23 只在 provisional bilipschitz/Sobolev 区间内建立积分估计；Step 27 只处理已有 \(\|a\Rm\|_\infty\) 后的延拓。

---

## 2. 指数拉回平均确实消除塌缩与片层数

令 \(h_{i,p}=\exp_p^*\bar g_i\) 定义在 \(B_\rho(0)\subset T_pM\)。若从 \(P_i\) 出发、长度至多 \(\rho\) 的测地线均处于 \(|\sec|\le K\) 区域，且
\[
\rho<\frac{\pi}{2\sqrt K},
\]
则 Rauch 比较和测地流的 Liouville 测度不变性给出
\[
\int_{P_i}\fint_{B_\rho(0),h_{i,p}}
 F(\exp_pv)\,d\mu_{h_{i,p}}\,d\mu_{\bar g_i}(p)
 \le C(n,K,\rho)\int_MF\,d\mu_{\bar g_i}. \tag{4}
\]

关键点如下。

1. 拉回球体积有固定下界：
   \[
   \Vol_{h_{i,p}}B_\rho(0)
   \ge \omega_{n-1}\int_0^\rho s_K(t)^{n-1}\,dt>0.
   \]
   因而拉回图自身非塌缩，即使底流形球完全塌缩。

2. 指数映射可有任意多片层；(4) 不出现片层数，因为测地流保留方向变量和 Liouville 测度。

3. \(\rho<\pi/(2\sqrt K)\) 排除径向共轭点，故 \(h_{i,p}\) 是光滑正定度量；在该拉回度量中，从原点出发的指数映射就是 \(v\mapsto v\)。

但 \(|\sec|\le K\) **不足以**得到 \(C^\infty\) 紧致性。还需要稍大缓冲区上的
\[
\sup|\nabla^m\Rm_{\bar g_i}|\le K_m,\qquad m\ge0. \tag{5}
\]
一旦 plateau 上已有正时间曲率界，普通 normalized Ricci-flow 内点估计可在更小平台上提供 (5)。随后正常坐标/Jacobi 估计给出拉回度量的 \(C^\infty_{\rm loc}\) 子列收敛。

---

## 3. 终端度量上的联合非负密度

所有对象必须针对同一个终端度量 \(\bar g_i\) 重建。不能把初始 harmonic representative、spinor 或 Hodge 投影沿截断流搬运。

定义
\[
E_i=\Ric_{\bar g_i}+\bar g_i,\qquad
q_i=\sqrt6\,|W_i^+|-s_i,\qquad r_i=q_i^+.
\]
这里必须注意两处公式修正：

- 正确的是 \(q_i=\sqrt6|W_i^+|-s_i\)，不是
  \(\sqrt6|W_i^+|-|s_i|\)；
- 有限 \(i\) 时正确的半正定算子是
  \[
  \mathcal A_i
  =W_i^++\sqrt{\frac23}|W_i^+|I_{\Lambda^+}\succeq0, \tag{6}
  \]
  不能预先写成 \(W_i^++\frac16I\)。后者只在极限已知
  \(|W_\infty^+|=1/(2\sqrt6)\) 后成立。

### 3.1 终端 \(L^2\) 缺陷足以驱动校准链

不需要终端时刻仍有点态近 Einstein 夹逼。由
\[
|\Ric^\circ|^2
=|E|^2-\frac14(\tr E)^2\le |E|^2
\]
可得拓扑归一化量
\[
R_i\le\frac{Q_i}{8\pi^2},\qquad Q_i=\int|E_i|^2.
\]
Chern–Gauss–Bonnet、临界拓扑恒等式、符号平均以及标量–Weyl 恒等式给出某个终端符号 monopole 类满足
\[
0\le \Delta_i
:=\int r_i^2-72\pi^2(a_i^+)^2
\le C Q_i. \tag{7}
\]
这一步在固定拓扑下给出绝对 \(\Delta_i\to0\)。

对该类在 \(\bar g_i\) 下的 harmonic self-dual representative 记为 \(H_i\)。正部正则化的 rescaled monopole 分解应给出
\[
\int\left(r_i-\frac92\right)^2\le CQ_i, \tag{8}
\]
\[
\int\left(
 |2\pi H_i|-\frac{r_i}{3\sqrt2}
\right)^2\le CQ_i, \tag{9}
\]
以及在有界曲率平台 \(\Omega_i\) 上
\[
\int_{\Omega_i}
 \langle\mathcal A_iH_i,H_i\rangle
 \le C(K)Q_i. \tag{10}
\]

因此可定义单一逐点非负密度
\[
\boxed{
\begin{aligned}
\mathcal D_i={}&|E_i|^2+
 \left(r_i-\frac92\right)^2+
 \left(|2\pi H_i|-\frac{r_i}{3\sqrt2}\right)^2\\
&+2\langle\mathcal A_iH_i,H_i\rangle .
\end{aligned}}
\tag{11}
\]
若 \(Q_i\to0\)，则
\[
\int_{\Omega_i}\mathcal D_i\to0. \tag{12}
\]

这里仍有一个实际书面缺口：现有材料和脚本支持正部代数，但尚未完整证明一个统一引理，将

- 平滑正权 \(f_{ik}^2\to r_i+\varepsilon_i\)；
- 每个正权对应的 rescaled SW 解；
- 与正则化参数无关的同一个 harmonic representative \(H_i\)；
- spinor eigenline defect 到 (10) 的传递

连续组织起来。该引理是短而必要的，不应以“代数脚本通过”代替。

---

## 4. 图选择、Hodge 极限及谱确定

由正体积比例 (3)、平均不等式 (4) 和 (12)，可选择 \(p_i\in P_i\)，使
\[
\fint_{B_\rho(0),h_i}
 \mathcal D_i(\exp_{p_i}v)\,d\mu_{h_i}\to0,
\qquad h_i=\exp_{p_i}^*\bar g_i. \tag{13}
\]
在 (5) 下，缩小半径后
\[
h_i\to h_\infty\quad\text{于 }C^\infty_{\rm loc}. \tag{14}
\]

由 (9) 和平台曲率界，拉回 \(H_i\) 有统一局部 \(L^2\) 界。方程
\[
dH_i=0,\qquad d_{h_i}^*H_i=0,\qquad *_iH_i=H_i
\]
的内点椭圆估计给出子列
\[
H_i\to H_\infty\quad\text{于 }C^\infty_{\rm loc}. \tag{15}
\]
从 (13) 及非负性得到
\[
\Ric_{h_\infty}=-h_\infty,\qquad s_\infty=-4, \tag{16}
\]
\[
r_\infty=\frac92,\qquad
|W_\infty^+|=\frac1{2\sqrt6}, \tag{17}
\]
\[
|H_\infty|=\frac{3}{4\sqrt2\pi}>0,\qquad
\mathcal A_\infty H_\infty=0. \tag{18}
\]

对于无迹对称 \(3\times3\) 算子，
\[
\lambda_{\min}(W)\ge-\sqrt{\frac23}|W|,
\]
等号当且仅当其余两个特征值相等。因此 (17)–(18) 给出整个开图上的
\[
\Spec(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right). \tag{19}
\]

仅有 \(|W^+|=1/(2\sqrt6)\) 不能确定谱；非零 \(H_\infty\) 的最低特征线信息不可省略。

---

## 5. Step 6 的局部矛盾成立

Einstein 四维度量满足 \(\delta W^+=0\)。若
\[
W^+=\mu I+(\lambda-\mu)P_\omega
\]
具有常数单特征值和常数双特征值，展开 \(\delta W^+=0\) 并与定长特征形式 \(\omega\) 收缩，依次得到
\[
\nabla^a\omega_{ab}=0,\qquad
\omega_{ab}\nabla^a\omega_{cd}=0.
\]
非零自对偶二形式在四维非退化，故
\[
\nabla\omega=0,\qquad \nabla W^+=0. \tag{20}
\]

另一方面，Einstein–Weyl 标量恒等式
\[
\Delta|W^+|^2
=2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]
在
\[
s=-4,\quad |W^+|^2=\frac1{24},\quad
\det W^+=-\frac1{864}
\]
下给出
\[
|\nabla W^+|^2=\frac1{16}, \tag{21}
\]
与 (20) 矛盾。因此禁戒 calibrated Einstein germ 确实不存在。

---

## 6. 尚未证明的承重命题

### 核心缺口：塌缩一致的终端平台定理

现有材料尚未证明截断流
\[
\partial_tg=-2a(\Ric+g),\qquad a=\sum_j\chi_j^2
\]
在统一时间 \([0,\theta r^2]\) 上同时产生：

1. 统一 metric comparability；
2. relative Sobolev 常数保持；
3. 局部曲率能量、缺陷能量及全局 \(Q\) 保持；
4. 加权曲率估计
   \[
   \|a\Rm(t)\|_\infty\le C\gamma/t; \tag{22}
   \]
5. 可积的加权缺陷估计
   \[
   \|aE(t)\|_\infty
   \le C_p\delta(r^2/t)^{2/p},\qquad p>2; \tag{23}
   \]
6. 从这些估计严格改进 first-exit 条件，非循环地闭合 metric/Sobolev bootstrap。

Step 23 已在 provisional interval 上建立 \(q=2,3\) 积分层级、终端 \(H_3\)、全局 \(Q\) 增长界和 \(J_6\) 保持；但从这些积分界到 (22)–(23) 的 Moser/Nash 超收缩仍未展示。Step 27 证明的是：**假设** (22) 已有，则可光滑延拓；它不产生 (22)。

### 支撑性但仍应书面证明的命题

- 塌缩球上的 relative Sobolev 常数及
  \[
  A_0^2\|\Rm\|_{L^2}\sim C\sqrt{\varepsilon_{\rm Li}}
  \]
  的体积抵消；
- 好集经过分离/Vitali 后仍保留固定体积比例；
- terminal platform 的双 Lipschitz 比较、固定缓冲与内点导数界在同一命题中成立；
- Step 27 中 Wang staggered-exponent 高阶归纳的逐项正规化转移；
- 正部 rescaled monopole 的终端联合密度引理，尤其是 (10)。

---

## 7. 固定拓扑与变拓扑

### 固定拓扑

临界拓扑量 \(A\) 固定，因此：

- 初始曲率总能量和总体积一致有界；
- Li 工作尺度有统一正下界 \(r\ge r_0>0\)；
- \(T_0=\theta r^2\) 为统一正时间；
- \(Q_i\to0\) 和 \(\int\mathcal D_i\to0\) 是绝对收敛；
- 符号类集合有限，可在需要时取固定类子列；
- 若核心平台定理成立，上述下游矛盾闭合。

### 变拓扑

通常只有
\[
Q_i=o(V_i),\qquad
\int\mathcal D_i=o(V_i),
\]
而非绝对 \(o(1)\)。指数平均仍可工作，但必须同时有
\[
\Vol P_i\ge cV_i,\qquad r_i\ge r_0>0,\qquad
\sup|\nabla^m\Rm|\le C_m. \tag{24}
\]
一般族中这些条件尚无保证。若 \(r_i\to0\)，按 \(r_i^{-2}\) 放大后 Einstein 常数趋于零，校准 Weyl 尺度也趋零，Step 6 的固定负 Einstein germ 不再出现。

此外，拓扑变化时符号立方体维数增长；平均 deficit 小不能推出每个符号顶点都饱和。可逐度量选择一个最大投影类，但不能得到所有类的统一结论。

---

## 最短闭合桥梁

下游部分可封装为：

> **终端平台—禁戒 germ 引理。**  
> 若临界 Ishida–LeBrun 度量序列存在 \(P_i\Subset\Omega_i\) 及固定 \(c,\rho,K_m>0\)，满足
> \[
> \Vol(P_i)\ge c\,\Vol(M_i),
> \]
> 从 \(P_i\) 发出的长度至多 \(2\rho\) 的测地线留在 \(\Omega_i\)，
> \[
> \sup_{\Omega_i}|\nabla^m\Rm|\le K_m,
> \qquad
> \frac{\int|\Ric+g_i|^2}{\Vol(M_i)}\to0,
> \]
> 且终端正部 rescaled monopole 分解给出 (8)–(10)，则指数平均产生固定半径光滑极限，满足 (16)–(19)，从而与 (20)–(21) 矛盾。

因此真正最短的上游桥是：

1. 证明 whole-support 加权曲率 Moser/Nash 估计 (22)；
2. 证明 \(p>2\) 的加权缺陷估计 (23)，从而积分控制 metric drift；
3. 以 first-exit 论证同时闭合 metric comparability 与 relative Sobolev persistence；
4. 用 Step 27 延拓并在 plateau 上应用普通内点导数估计；
5. 单独写出终端正部 monopole 联合密度引理。

这将闭合固定临界四维负分支的“终端截断流度量 \(\Rightarrow\) 禁戒 calibrated Einstein germ”链条，但不覆盖变拓扑一般族、正分支、\(n\ge5\) 或 Yau 第 26 题的维数统一命题。
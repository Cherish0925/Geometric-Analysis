# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 99,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step99_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step99_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Given the cost structure of the free-T² connector for Yau Problem 26:

1. Normal cost: bounded below by Raychaudhuri floor δ_min(R) ~ 12e^{-2R}
2. Tangential cost: conformal expansion gives 9.94·sech²(r) for the charged separator orbit shape
3. The exact Einstein germ (Koiso) has zero cost but is only defined locally

The critical unknown is the continuation domain of the exact Einstein germ from the charged Koiso center. If it extends to r = r₁, the best trial metric could achieve operator norm ~ max(δ_min(R), 9.94·sech²(r₁)) for a total cylinder of length R.

PROPOSE concrete mathematical strategies for either:
(A) Establishing that the Koiso germ has finite maximal continuation radius r_max, and estimating r_max from the data (S=1, Qmax=0.5, scalar curvature -7, orbit energy concentrated with von Mises parameter 800).
(B) Proving that the tangential cost cannot be made arbitrarily small by any trial (i.e., a genuine tangential obstruction).
(C) A completely different construction strategy that bypasses the Koiso center + expanding exterior framework.

The context includes the full development history of the free-T² connector problem over 96+ steps, including the Bochner/resolvent obstruction for exact OT connectors, the flat-slice barrier, and the charged Koiso separator construction.

## Integrated Scientific Memo

## 结论性判断

现有数据支持两个不同的潜在延拓尺度，但尚不能证明 Koiso germ 的最大实延拓半径有限：

\[
r_{\mathrm{focus}}\sim 0.7\!-\!0.8,
\qquad
r_{\mathrm{hf}}\sim \kappa^{-1/2}\sim 0.035
\quad(\kappa=800).
\]

前者来自基圆方向的低模聚焦，后者来自椭圆 Cauchy 问题的高频放大。必须用完整的 \(s\)-依赖 \(3\times3\) 系统区分二者；任何径向替代都会重新落入 flat-slice barrier，因而不检验真正的 charged Koiso 机制。

另一方面，若试验度量最终定义在**闭的自由 \(T^2\)-流形**上，则 Chern–Gauss–Bonnet 确实给出一个与 Koiso 延拓无关的全局 Ricci 误差下界。这是目前最接近严格方案 (B) 的结果，但它不能解释局部开圆柱上的数值常数 \(9.94\)，也不能单独证明该具体 tangential profile 的逐点最优性。

---

# A. 证明或估计有限 \(r_{\max}\)

## A1. 可直接实施的高阶、区间验证延拓

采用完整 Einstein Cauchy 系统

\[
\partial_rq=2K,\qquad
\partial_rK=\operatorname{Ric}(q)+3q-HK+2Kq^{-1}K,
\]

并保留所有 \(s\)-Fourier 模及混合 connection block。展开

\[
q(r,s)=\sum_{m\ge0}q_m(s)r^m,\qquad
K(r,s)=\sum_{m\ge0}K_m(s)r^m.
\]

由冻结的 Step 94/96 中心数据递归生成系数，而不是重新生成径向数据。需要区间验证的几何量是

\[
a^2=q_{ss}-q_{sA}G^{AB}q_{Bs},\qquad
\lambda_{\min}(q),\qquad \lambda_{\min}(G),\qquad
|\mathrm{Rm}| ,
\]

以及 Hamiltonian、momentum constraints。

严格的有限半径结论可以来自：

1. 在某个实 \(r_*\) 上区间证明 \(a^2(r_*,s_*)\le0\)；
2. 区间证明 \(\lambda_{\min}q(r_*,s_*)\le0\)；
3. 在保持正定时证明某个曲率不变量沿实轴无界。

Padé 极点或 Taylor 系数比

\[
\frac{\|q_m\|}{\|q_{m+1}\|},\qquad
\frac{\|K_m\|}{\|K_{m+1}\|}
\]

只能定位候选复解析奇点；除非与实轴上的正定性丧失或曲率发散结合，否则不能证明 \(r_{\max}<\infty\)。

由于 von Mises 参数为 \(800\)，建议至少使用 \(N_s=96,128,192,256\)，并做 \(3/2\) 或 \(2\) 倍 padding；Step 96 的 \(N=48,64\) 只足以验证 \(r=0.02\) 的局部 Taylor 行为。

## A2. 两个可区分的预测尺度

中心精确数据为

\[
H_r=2,\qquad a_{rr}=-(4+Q),\qquad \sigma_{rr}=6+Q.
\]

在 \(Q_{\max}=0.5\) 处，二阶近似给出

\[
a(r)\approx1-\frac{4.5}{2}r^2,
\qquad r_{\rm zero}\approx\sqrt{\frac2{4.5}}=0.667.
\]

若以恒定有效曲率 Jacobi 模型代替，

\[
a(r)\approx\cos(\sqrt{4+Q}\,r),
\]

则

\[
r_{\rm focus}\approx \frac{\pi}{2\sqrt{4.5}}=0.740.
\]

在 \(Q\approx0\) 区域相应为 \(0.706\) 和 \(0.785\)。这些只是中心外推，不是 Sturm 定理，因为尚未证明法向–基圆截面曲率在整个 collar 中维持正下界。

若真实 \(r_{\max}\lesssim0.8\)，则

\[
9.94\,\sech^2(r_{\max})\gtrsim 5.5,
\]

而要使此项低于 \(10^{-2}\) 必须达到约

\[
r_1>4.14.
\]

因此证明 \(r_{\max}<1\) 已足以排除“长精确 germ 显著降低 tangential cost”的设想。

## A3. 高频延拓尺度

椭圆 Cauchy 主部对 Fourier 模 \(k\) 产生大致

\[
e^{\mu |k|r}
\]

的增长，其中 \(\mu\) 必须从完整线性化主符号求出。对

\[
B_\kappa(s)=\frac{e^{\kappa\cos s}}{I_0(\kappa)}
\]

有主频区近似

\[
|\widehat B_\kappa(k)|\sim e^{-k^2/(2\kappa)}.
\]

传播后包络为

\[
\exp\!\left(\mu |k|r-\frac{k^2}{2\kappa}\right),
\]

最大模约为

\[
k_*(r)=\mu\kappa r,
\]

总放大约为

\[
\exp\!\left(\frac{\mu^2\kappa r^2}{2}\right).
\]

当 \(\kappa=800,\mu=1\) 时：

\[
r=0.02:\ e^{0.16}\approx1.17,\qquad
r=0.10:\ e^4\approx54.6,\qquad
r=0.20:\ e^{16}\approx8.9\times10^6.
\]

这解释了为什么 \(r=0.02\) 的短程数值收敛不能支持 order-one 延拓。

但高频增长本身也不等于有限的实几何延拓半径：椭圆 Cauchy 不稳定性可能只意味着数值求解病态。决定性计算是把实际中心 Fourier 数据投影到完整主符号的增长特征子空间。如果投影幅值为 \(A\)，候选非线性尺度为

\[
r_{\rm hf}\approx
\sqrt{\frac{2\log A^{-1}}{\mu^2\kappa}}.
\]

例如 \(\mu=1\) 时：

\[
A=10^{-1}\Rightarrow r_{\rm hf}\approx0.076,\qquad
A=10^{-2}\Rightarrow r_{\rm hf}\approx0.107.
\]

因此最有区分力的输出不是一次长时间 marching，而是：

- 增长 eigenspace 上的实际 Fourier 投影；
- 随 Taylor 阶数稳定的实轴正定性界；
- 危险模 \(k_*(r)\) 是否随 \(\kappa r\) 漂移。

## A4. 将低模聚焦升级为定理

令

\[
\theta_s=\partial_r\log a.
\]

在适当水平框架中，其 Riccati 方程具有形式

\[
\partial_r\theta_s+\theta_s^2+
|W_{s\perp}|^2
=-\sec(\nu,e_s).
\]

中心上

\[
\theta_s(0)=0,\qquad
\theta_s'(0)=-(4+Q),
\]

故

\[
\sec(\nu,e_s)\big|_{r=0}=4+Q.
\]

若能在首次退化前证明

\[
\sec(\nu,e_s)\ge k_*>0,
\]

则

\[
\theta_s'\le-\theta_s^2-k_*,
\]

从而

\[
\theta_s(r)\le-\sqrt{k_*}\tan(\sqrt{k_*}r),
\qquad
r_{\max}\le\frac{\pi}{2\sqrt{k_*}}.
\]

真正缺失的对象正是沿 germ 的截面曲率下界；中心二阶系数不能替代它。可尝试从 quotient 方程构造控制量

\[
\mathcal F(r)=
\int_{S^1}\left[
\theta_s^2+|U_r|^2+\frac{|U_s|^2}{a^2}+Q
\right]a e^\sigma ds
\]

并证明短程 coercive 微分不等式，阻止正截面曲率迅速变号。

还需区分两种 \(a\to0\)：

- 若 period/holonomy 满足精确 bolt 光滑条件，则是非自由 \(T^2\) 的平滑封口；
- 否则是锥奇点、正定性丧失或曲率爆炸。

前一种不是通向自由 expanding end 的 continuation。

> 修正：Step 96 在 \(r=0.02\) 报告的 \(\lambda_{\min}(q)=0.127455\) 不能据此称为“从 \(O(1)\) 快速降到 \(0.127\)”；中心最小特征值未在材料中给出，该数值可能主要来自中心 orbit matrix 的各向异性。

---

# B. 真正的 tangential obstruction

## B1. 闭自由 \(T^2\) 流形上的严格拓扑下界

若闭定向四流形承载自由 \(T^2\)-作用，则

\[
\chi(M)=0.
\]

Chern–Gauss–Bonnet 给出

\[
0=\frac1{8\pi^2}
\int_M
\left(
|W|^2+\frac{s^2}{24}
-\frac12|\Ric^\circ|^2
\right)dV,
\]

即

\[
\int_M|\Ric^\circ|^2\,dV
=
2\int_M|W|^2\,dV
+\frac1{12}\int_Ms^2\,dV.
\tag{B.1}
\]

这立即排除任意接近非零 Einstein 常数的 Ricci tensor。若

\[
\|\Ric+3g\|_{\rm op}\le\delta<3,
\]

则 Ricci 特征值属于 \([-3-\delta,-3+\delta]\)，故

\[
|s|\ge 12-4\delta=4(3-\delta).
\]

同时，对四个均落在长度 \(2\delta\) 区间的特征值，最优方差界是

\[
|\Ric^\circ|^2\le4\delta^2.
\]

由 (B.1)：

\[
4\delta^2\Vol(M)
\ge
\frac1{12}\,16(3-\delta)^2\Vol(M),
\]

所以

\[
\delta\ge\frac{3-\delta}{\sqrt3},
\qquad
\boxed{\delta\ge\frac{3}{1+\sqrt3}\approx1.098.}
\tag{B.2}
\]

更一般地，若 Ricci 特征值位于负区间 \([c,C]\)，\(c<C<0\)，则利用区间方差的最优估计

\[
|\Ric^\circ|^2\le (C-c)^2
\]

可得更强的

\[
\boxed{C-c\ge \frac{2|C|}{\sqrt3}.}
\tag{B.3}
\]

分支中使用了较粗的 \(4(C-c)^2\)，只得到 \((C-c)\ge |C|/\sqrt3\)；(B.3) 是同一路线的严格改进。

这是真正的“任何 trial 都不能任意小”的逐点 operator-norm 障碍，因为一个逐点上界会导致积分矛盾。它适用于闭自由 \(T^2\) 流形上的最终度量，而不直接适用于带边界或非紧 connector cylinder；有边界时必须加入 Gauss–Bonnet 边界项。

它也不能从现有数据推出数值 \(5\) 或 \(9.94\)。\(\int|W|^2\) 虽是非负附加项，但没有体积归一化下界时，不能声称它“必然把常数提高到数个单位”。

## B2. 对具体 connector 的 adjoint obstruction

对完整 reduced residual

\[
F(V)=(H,T,Z,\mathcal B)
\]

寻找满足齐次伴随方程的全局场 \(\Psi\)，则

\[
\|F(V)\|_\infty
\ge
\frac{|\langle\Psi,F(V)\rangle|}
{\|\Psi\|_{L^1}}.
\]

积分分部后，分子应只含：

- 中心与两端的 Hopf/TT moments；
- 三个 \(\mathbb H^2\) Killing currents；
- shared center/end 参数的有限维导数；
- charge/holonomy 边界数据。

将这些参数方向投影掉后，若仍有中心局域的伴随场满足

\[
\inf_{R\to\infty}
\frac{|\langle\Psi_R,F\rangle|}
{\|\Psi_R\|_{L^1}}>0,
\]

即得到真正的 tangential sup-norm floor。

Step 96 已证明 compactly supported 的局部 \(X\) 不可能完成此事，因为固定 charge germ 上

\[
\frac12c^TK_Xc
=
\operatorname{div}_\sigma(QX)-m_c(X),
\qquad m_c=0,
\]

积分恒为零。因此必须解跨越中心和两端的伴随边值问题。

最具体的判据是 compactified Fourier–Chebyshev 线性化的最小奇异值及左奇异场：

- 奇异值趋于正数，左场保持中心局域，并与 residual 非零配对：真实障碍；
- 奇异值指数衰减，左场向 charge-taper 端逃逸：redshift near-kernel；
- 随网格漂移或集中于 cutoff 尺度：离散伪模。

Hopf moment 的中心能量尺度很大：在标准 determinant-one block 中，

\[
R(q_\Sigma)=-\frac12|U_s|^2=-7
\quad\Rightarrow\quad |U_s|^2=14.
\]

但把它直接识别为数值系数 \(9.94\) 尚无依据；必须包括 charge forcing、水平方程以及所有 shared parameter directions 后再计算有限维 cokernel。

## B3. 紧性–Liouville 路线

反设存在 \(R_j\to\infty\) 的 trials，满足

\[
\|F(V_j)\|_\infty\to0
\]

且中心 trace 收敛到 charged Koiso 数据。若能建立统一 gauge-fixed 局部椭圆估计和非退化性，则子列收敛到完整的、双端 expanding 的精确 free-\(T^2\) Einstein 解。

因此一般 tangential obstruction 等价于一个精确 Liouville 定理：

\[
\text{不存在携带该 charged Koiso 中心数据的完整双端解。}
\]

证明所需的候选守恒量正是 Hopf/TT flux、target Killing currents、Hamiltonian/Raychaudhuri identities。单独的 Pohozaev 积分通常只给总量下界；若 transition 可以随 \(R\) 展宽，它不能推出 sup floor。因此必须再证明 end indicial mass gap 或得到中心局域伴随模。

---

# C. 绕开 Koiso 中心与 expanding exterior

## C1. 允许 \(T^2\) 作用退化

自由作用使 coordinate charge 必须沿 cylinder 输运。若允许一个 primitive circle 在 codimension-two fixed set 上平滑塌缩，则 charge/holonomy 可通过拓扑 rod data 终止，而非通过 \(dq\neq0\) 的长 taper 消除。

应建立带 rod vectors 的 toric BVP，并检查：

\[
\text{塌缩圆周期条件},\quad
\text{holonomy jump},\quad
\text{bolt 光滑性},\quad
\sup\|\Ric+3g\|_{\rm op}.
\]

这会脱离 free-\(T^2\) 类别，也避开 flat-slice barrier 和固定 charge transport。

## C2. 微结构 orbit-shape connector

令 orbit map 为小振幅高频模式：

\[
U(r,s)\sim \varepsilon A(r)(\cos ks,\sin ks),
\qquad
\varepsilon k\sim\sqrt{14}.
\]

则中心所需

\[
|U_s|^2\sim14
\]

可以由 \(\varepsilon=O(k^{-1})\) 实现，故 orbit-shape 总位移很小。困难是

\[
U_{ss}=O(k),
\]

必须用 \(r\)-依赖相位/振幅及 \(\sigma,\varphi,A\) correctors 消去。自然选择为边界层形式

\[
A(r)\sim e^{-k|r|}.
\]

需做两尺度展开并逐块验证

\[
(H,T,Z,\mathcal B)
\]

的 \(O(k)\)、\(O(1)\) 项是否全部可消；只有剩余达到 \(O(k^{-1})\) 才形成真正的新构造。这个方案用高频 intrinsic curvature 替代长精确 germ，但也可能因非线性平均应力留下不可消的 \(O(1)\) tensor。

## C3. 完全离开 \(T^2\) connector：直接寻找“近 Einstein 但无 Einstein”的闭流形

可研究具有截面曲率

\[
-1-\varepsilon\le\sec\le-1+\varepsilon
\]

且拓扑上不承载 Einstein 度量的闭四流形；此时自动有

\[
\|\Ric+3g\|_{\rm op}\le3\varepsilon.
\]

候选机制包括 branched-cover/hyperbolization 与独立的光滑拓扑 Einstein 障碍。但必须同时核验：

1. pinched metric 与拓扑构造发生在同一光滑流形；
2. Einstein obstruction 排除所有符号的 Einstein 度量；
3. 拓扑公式和曲率 pinching 可同时量化。

仅违反 Hitchin–Thorpe 的流形不适合极窄 pinching，因为 Gauss–Bonnet/signature 本身会阻止其接近非零 Einstein。

## C4. 定量 Ricci-flexibility 或有限维 cohomogeneity-one 方案

另一条路线是用双 warped-product/handle blocks 直接控制所有 Ricci 特征值，例如

\[
g=dt^2+f(t)^2g_{S^p}+h(t)^2g_{S^q},
\]

\[
\Ric_{tt}
=-p\frac{f''}{f}-q\frac{h''}{h},
\]

并对两个 orbit blocks 建立显式微分不等式，使整个 surgery 始终落在固定 Ricci 区间内。相比椭圆 Cauchy continuation，这可转化为有限维 ODE 或 interval-arithmetic BVP。

---

## 当前最精确的未决对象

1. **\(r_{\max}\)**：需要完整 Fourier–Taylor 系统的实轴区间证书，或沿 germ 的正截面曲率下界；中心 Taylor 数据只能给 \(0.7\!-\!0.8\) 的候选聚焦尺度。
2. **高频是否真实限制几何延拓**：需要实际中心数据在增长主符号 eigenspaces 上的投影；数值病态本身不是奇点。
3. **具体 tangential floor**：闭自由 \(T^2\) 类已有严格普适下界
   \[
   \|\Ric+3g\|_{\rm op}\ge \frac{3}{1+\sqrt3},
   \]
   但数值 \(9.94\) 是否代表更强的中心局域 obstruction，取决于完整伴随 matching operator 的中心 cokernel 与 end indicial spectrum。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 21,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step21_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step21_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following mathematical chain for the 4D negative-branch cutoff-flow program on a critical Ishida-LeBrun manifold M.

(1) NORMALIZATION LOWER-ORDER: Under dt g = -2 chi^2 (Ric+g), the normalization -2 chi^2 g changes the curvature evolution by: (a) volume form -a(s+4)dmu with |s+4| ≤ 4 delta; (b) curvature: -(nabla^2 a) ☐ g + O(|nabla a||Rm|), which is lower order than the critical cubic reaction a|Rm|^2 in H_q. Verify that the critical parameter beta = A_0^2 ||Rm||_2 is unchanged, and that the normalization contributes only an exponential Gronwall factor e^{CT_0}.

(2) INTERIOR REGULARITY ON PLATEAU: After the first-exit gives |chi^2 Rm| ≤ C gamma/t uniformly on [0, T_0], on the plateau {chi=1} the flow becomes dt g = -2(Ric+g), a normalized Ricci flow. Since a=1 there, |Rm| ≤ C gamma/t. Standard Shi interior estimates on [T_0/2, T_0] x B_{rho/32}(p) should give |nabla^k Rm| ≤ C_k (T_0/2)^{-k/2}. Verify: (a) Does the normalized Ricci flow (with the -2g term) satisfy standard Shi estimates? (b) Are the Shi constants independent of the sequence index? (c) Does this give smooth compactness on the exponential chart?

(3) EXPONENTIAL CHART TO CONTRADICTION: For the limit h_inf on B_{R/2}(0) from Arzela-Ascoli: (a) Does |E_i(T_0)| → 0 follow from |chi^2 E| ≤ C delta_i (r^2/T_0)^{1/3}? (b) Does the 7/24 calibration inequality transfer through the flow and chart, giving |W+| = 1/(2sqrt6) on the limit? (c) Is the projector obstruction (simple eigenform → parallel → nabla W+ = 0 vs |nabla W+|^2 = 1/16) correctly stated?

(4) POTENTIAL GAPS: Are there any gaps in the chain from the first-exit output to the projector contradiction? In particular: does metric comparability correctly transfer the global Q control through the exponential chart? Does the good-center selection correctly provide nontrivial monopole data on the limit? Does the chart pullback preserve the all-derivative bounds from Shi?

## Integrated Scientific Memo

# 核验结论

该链条目前只能成立为**条件性框架**。由一阶退出输出到正时间平台正则性这一段基本正确；但从全局校准到指数图中的谱饱和，仍缺少定量选点和非零 monopole 极限数据。此外，一阶退出本身的 \(U1\)–\(U3\) 尚未证明，且 Step 21 的退出条件中存在曲率能量与缺陷能量混用。

## 1. 归一化项

令
\[
E=\Ric+g,\qquad a=\chi^2,\qquad \partial_tg=-2aE.
\]

### 1.1 体积元

精确公式是
\[
\partial_t d\mu=-a(s+4)d\mu=-a\,\tr E\,d\mu.
\]

若仅已知初始时刻 \(|E(0)|\le\delta\)，则
\[
|s(0)+4|\le 2\delta
\]
（采用 Hilbert–Schmidt 范数；\(4\delta\) 是较松的界）。但不能据此断言整个流区间都有 \(|s+4|\le4\delta\)。在得到缺陷 Moser 估计后，只能直接推出
\[
|a(s+4)|\le C|aE|
 \le C\delta (r^2/t)^{1/3},
\]
其时间奇性可积。在先做曲率迭代时，演化测度项应作为
\[
|a\,\tr E|\lesssim aF,\qquad
F=(1+|\Rm|^2)^{1/2},
\]
并入曲率反应项，不能循环使用尚未得到的缺陷点态界。

### 1.2 曲率演化和 Grönwall 因子

把 \(-2ag\) 单独看作变分时，对全协变曲率张量有示意公式
\[
D\Rm[-2ag]=-2a\,\Rm+\mathcal K(\nabla^2a),
\]
符号依曲率约定而定。孤立的变分公式中不必存在本征的
\(|\nabla a||\Rm|\) 项；一阶 \(a\)-导数主要在对 Hessian 项分部积分、改变指标或高阶方程中出现。

在 \(H_q\) 能量计算中，利用
\[
\frac{|da|^2}{a}=4|d\chi|^2
\]
并以 Young 不等式吸收耗散，归一化项产生
\[
\varepsilon D_q+
C_{\varepsilon,q}(r^{-2}+1)H_q
\]
一类低阶项。使用 \(F\ge1\) 时，表面上的常数源也可纳入 \(H_q\)；若直接使用 \(|\Rm|\)，则会保留显式体积源。

因此自然的放大因子是
\[
\exp\!\left(C_q(T_0/r^2+T_0)\right),
\]
而不是未经说明的 \(e^{CT_0}\)。当 \(T_0=\theta r^2\) 时为
\[
e^{C_q(\theta+\theta r^2)}.
\]
它不引入新的临界 Sobolev 小量条件，但需要选取 \(\theta\) 足够小。

Step 21 中的 \(C\,\Vol/r^{2q}\) 也没有由现有分部积分计算支持；其精确尺度应从完整 \(H_q\) 推导重新计算。关键结论仍是：这些项比临界三次反应低阶，由耗散和 Grönwall 处理，而非改变临界吸收阈值。

### 1.3 临界参数

初始量
\[
\beta=A_0^2\|\Rm(g_0)\|_{L^2}
\]
当然不因随后选择归一化或非归一化流而改变。但它不是动态不变量；流中的 Sobolev 常数和局部 \(L^2\) 曲率仍须由退出体系控制。

实际正则化层使用
\[
\gamma=A_0^2\|F\|_2,\qquad
\gamma\le\beta+Cr^2.
\]
故准确结论是：归一化不改变临界吸收机制，而不是说所有演化中的临界量自动保持不变。

---

## 2. 平台上的 Shi 正则性

### 2.1 归一化流是否适用 Shi 估计

是。在 \(\chi=1\) 的固定开集上，
\[
\partial_tg=-2(\Ric+g).
\]
令
\[
\widehat g(\tau)=e^{2t}g(t),\qquad
\tau=\frac{e^{2t}-1}{2},
\]
则
\[
\partial_\tau\widehat g=-2\Ric_{\widehat g}.
\]
因此普通局部 Shi 估计经有限时间的缩放直接转移；也可从带线性低阶项的归一化曲率方程直接证明。

这不使用有限传播速度。所需条件只是整个稍大的抛物柱始终位于固定平台 \(\{\chi=1\}\)，并在那里有曲率上界。

### 2.2 估计的正确形式及序列一致性

在 \([T_0/2,T_0]\) 上，
\[
|\Rm|\le K:=\frac{2C\gamma}{T_0}.
\]
若点 \(p\) 距平台边界至少 \(d>0\)，则局部估计形如
\[
|\nabla^k\Rm|(p,T_0)
\le C(n,k,T_0)\,
K\bigl(K^{k/2}+(T_0/2)^{-k/2}+d^{-k}\bigr).
\]
因此 Step 21 的
\[
C_k(T_0/2)^{-k/2}
\]
只能理解为已将 \(K\)、缓冲宽度和时间尺度吸收到 \(C_k\) 中。

这些常数对序列指标 \(i\) 一致，需要一致控制：

\[
T_{0,i}>0,\qquad \gamma_i/T_{0,i},\qquad
d_i^{-1},
\]
以及平台柱内的度量可比性。特别地，如果工作尺度 \(r_i\to0\)，则
\[
T_{0,i}=\theta r_i^2,\qquad
(T_{0,i}/2)^{-k/2}\sim r_i^{-k}
\]
会发散。全局 Chern–Weil 总能量界本身并不能推出统一的局部曲率密度界或 \(r_i\ge r_*>0\)。因此“由 Chern–Weil 自动得到序列一致的全部导数界”没有被现有材料证明。

一个可能的替代是按尺度重标度指数图；但那会改变 Einstein 常数和校准常数，必须重新设计极限矛盾，不能直接代入当前固定尺度论证。

### 2.3 指数图紧致性

若上述全部协变导数界和固定正半径 \(R\) 已统一获得，取
\[
R<\min\{c\,d,\pi/(2\sqrt K)\},
\qquad h_i=(\exp_{p_i}^{g_i(T_0)})^*g_i(T_0).
\]
在无共轭点范围内，指数映射是局部等距，故
\[
\nabla_{h_i}^k\Rm_{h_i}
=(\exp_{p_i})^*\nabla_{g_i(T_0)}^k\Rm_{g_i(T_0)}
\]
精确成立。多重覆盖或小整体单射半径不会破坏这一点。

但“协变曲率导数有界”到“指数坐标中度量系数 \(C^\infty\) 有界”还需 Jacobi 方程：Rauch 给出统一椭圆性，曲率全部导数控制给出度量系数全部坐标导数控制。随后才能在缩小球 \(B_{R/2}\) 上应用 Arzelà–Ascoli。仅有指数图体积下界不足以推出光滑紧致性。

---

## 3. 从指数图到矛盾

### 3.1 Einstein 极限

在平台上 \(a=1\)，故
\[
|E_i(T_0)|
\le C\delta_i(r_i^2/T_{0,i})^{1/3}
=C\theta^{-1/3}\delta_i\to0.
\]
这一结论与 \(r_i\) 无关，并在指数拉回下保持。因此一旦已有 \(C^\infty\) 图极限，
\[
\Ric_{h_\infty}=-h_\infty.
\]

### 3.2 \(7/24\) 校准不能自动转移到任意指数图

校准不等式是在终端度量上重新应用：
\[
\int_M\left(|W^+|-\frac1{2\sqrt6}\right)^2d\mu
\le\frac7{24}Q_i(T_0).
\]
要使右侧趋零，需独立证明
\[
Q_i(T_0)\le C Q_i(0),
\qquad Q_i(0)\le\delta_i^2\Vol(g_i(0)).
\]
度量可比性只比较体积元和同一张量的范数，不能控制 \(E(T_0)\) 相对 \(E(0)\)；所需输入是齐次缺陷方程的三角能量估计。固定拓扑上还需体积上界，现有 Chern–Weil 代数在 \(s=-4+O(\delta_i)\)、无迹 Ricci \(=O(\delta_i)\) 时可给出这一点。

即使全局积分趋零，也不能直接断言多重指数图上的积分趋零。必须使用 Step 16 的指数图平均引理，并满足
\[
\frac{\int_M\mathcal D_i\,d\mu_i}
     {\Vol(P_i,g_i(T_0))}\longrightarrow0,
\]
其中 \(P_i\) 是允许选中心的缓冲平台，\(\mathcal D_i\) 是联合非负密度。因而还需证明平台体积不相对于全局误差过快退化，例如
\[
\Vol(P_i)\ge c\,\Vol(M,g_i)
\]
或其他足以使上述比值趋零的估计。Step 21 没有提供这一条件。

### 3.3 Weyl 模长不足以确定谱

由
\[
\Ric=-g,\qquad |W^+|=\frac1{2\sqrt6}
\]
不能单独推出
\[
\Spec(W^+)=(-1/6,1/12,1/12).
\]
例如
\[
\left(-\frac1{4\sqrt3},0,\frac1{4\sqrt3}\right)
\]
同样无迹且平方范数为 \(1/24\)。

必须在终端度量上重新构造 monopole/Hodge 数据，并通过联合密度选出非零极限自对偶调和形式 \(H_\infty\)，满足
\[
|H_\infty|=\frac{3}{4\sqrt2\pi}>0,\qquad
\mathscr A_\infty H_\infty=0,
\]
其中
\[
\mathscr A=W^++\sqrt{\frac23}|W^+|I\ge0.
\]
由于
\[
\sqrt{\frac23}|W^+|=\frac16,
\]
这给出特征值 \(-1/6\)。再由无迹和
\[
|W^+|^2=\frac1{24}
\]
才推出另外两个特征值均为 \(1/12\)。

所以“good center”必须针对 Step 16 的完整联合密度 \(\mathcal D_i\)，而不能只针对 \(7/24\) 校准密度；初始度量的调和代表也不能简单运输到终端度量。

### 3.4 Projector 矛盾

一旦谱
\[
(-1/6,1/12,1/12)
\]
和其恒定重数已建立，局部 projector 论证是正确的。写成
\[
W^+=\frac1{12}I-\frac14P,
\]
其中 \(P\) 是秩一谱投影。Einstein 条件给出 \(\delta W^+=0\)；结合恒定特征值的 Derdziński/projector 计算得到
\[
\nabla P=0,\qquad \nabla W^+=0.
\]

另一方面，采用材料中的 Einstein–Weyl 恒等式
\[
\frac12\Delta|W^+|^2
=|\nabla W^+|^2+\frac{s}{2}|W^+|^2-18\det W^+,
\]
并代入
\[
s=-4,\quad |W^+|^2=\frac1{24},\quad
\det W^+=-\frac1{864},
\]
由于模长常数，有
\[
0=|\nabla W^+|^2-\frac1{12}+\frac1{48},
\]
故
\[
|\nabla W^+|^2=\frac1{16},
\]
与 \(\nabla W^+=0\) 矛盾。该数值在给定恒等式约定下是可直接复核的。

---

## 4. 当前链条中的具体断点

1. **\(U1\)–\(U3\) 尚未证明。**  
   加权曲率 Moser、缺陷 Moser，以及有限邻域三角 \(Q\) 系统仍缺完整的时间—空间递推、演化测度处理和 \(a=0\) 正则化。脚本只验证指数乘积与样例数值，不证明这些 PDE 结论。

2. **退出条件混用了两种能量。**  
   Step 21 的 (F3) 是曲率能量 \(H_2\)，但 Step V 引用的 (4.1) 控制的是缺陷能量 \(Q_\alpha\)。后者不能改进前者。必须分别证明：
   \[
   H_{2,\alpha}(t)\le 2H_{2,\alpha}(0)
   \]
   的曲率有限邻域估计，以及
   \[
   Q(t)\le C Q(0)
   \]
   的缺陷三角估计；或重写退出体系，使两个量均为独立条件。

3. **统一工作尺度未建立。**  
   若 \(r_i\to0\)，正时间 Shi 导数界在未缩放图中并不统一。需要统一局部 \(L^2\) 曲率密度、统一正体积好区域，或一个能兼容校准常数的重标度方案。

4. **全局 \(Q\) 到图上的传递不是度量可比性的结果。**  
   先由三角能量系统得到终端全局 \(Q\to0\)，再用联合密度的指数平均引理选中心；还需控制允许中心集的体积分母。

5. **非零 monopole 极限尚未完成。**  
   Step 16 给出了合适的正部修正和联合密度框架，但仍需终端度量上的 monopole 存在、缺陷估计，以及指数图上的 Hodge 椭圆紧致性。没有 \(H_\infty\neq0\)，谱结论和 projector 矛盾都不能启动。

6. **拉回本身不损失导数界。**  
   在统一无共轭半径内，所有内禀协变导数界由局部等距精确保留；真正未解决的是这些界及图半径能否对序列统一，而不是拉回操作。

因此，可靠的条件性结论是：
\[
\boxed{
\begin{gathered}
\text{若能证明 }U1\text{--}U3,\ \text{统一平台尺度/体积分母，}\\
\text{并以联合 monopole 密度选取好中心，}\\
\text{则平台 Shi 正则性 }\Rightarrow
\text{光滑指数图极限 }\Rightarrow
\text{谱饱和 }\Rightarrow
\text{projector 矛盾。}
\end{gathered}}
\]
现有材料尚不足以推出所声称的固定拓扑 Ricci-pinching gap。
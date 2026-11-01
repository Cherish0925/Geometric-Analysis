# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md",
    "Sessions/S0910A02/workspace/notes/step4_preceptor_energy_accounting_and_route_review.md",
    "Sessions/S0910A02/workspace/notes/step3_stable_integral_obstruction_principle.md",
    "Sessions/S0910A02/workspace/notes/step3_corrections_lebrun_and_collapse.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md",
    "Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md"
  ]
}
```

## Task

Check the Step-4 Preceptor note for Yau Problem 26. Focus on the four-dimensional full-Weyl Chern--Gauss--Bonnet accounting and the route judgment. Verify the constants and inequalities: 8π²χ = ∫(|W|²+s²/24-|E|²/2), b(δ)=(2/3)(1-δ)²-2δ², volume ceiling, equivalence between volume lower bound and Weyl-energy deficit up to δ-dependent constants, and the claim that tight pinching plus bounded |Rm| forbids 4D collapse. Also check the target-fidelity/refutation logic: p→1/3+ negative LeBrun boundary alone cannot refute Q_4, positive branch obstruction statements are not overclaimed, and Anderson/Ye source gaps are stated at their real scope. Identify corrections or sharper formulations that would materially affect the next research step.

## Output

# 科学复核备忘录：Step 4 四维 CGB 计量与路线逻辑

## 1. 四维全 Weyl 计量

令 Ricci 端同态的特征值为
\[
\sigma+e_i,\qquad \sigma\in\{\pm1\},\qquad |e_i|\le \delta<1,
\]
并令 \(E=\operatorname{Ric}-\frac{s}{4}g\)。则
\[
s=4\sigma+\sum_i e_i,\qquad
|E|^2=\sum_i(e_i-\bar e)^2
      =\sum_i e_i^2-4\bar e^2\le 4\delta^2.
\]
又因 \(s\) 与 \(\sigma\) 同号，
\[
|s|\ge 4(1-\delta).
\]

在 Step 4 所采用的 Weyl 范数约定下，
\[
8\pi^2\chi(M)
=\int_M\left(|W|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)d\mu
\]
是正确的；这里 \(|W|^2=|W^+|^2+|W^-|^2\)。设
\[
B:=\frac{s^2}{24}-\frac{|E|^2}{2}.
\]
上述粗估计给出
\[
B\ge \frac23(1-\delta)^2-2\delta^2
=:b(\delta),
\]
其中
\[
b(\delta)=\frac23-\frac43\delta-\frac43\delta^2
         =\frac23(1-2\delta-2\delta^2).
\]
因此
\[
\int_M|W|^2\,d\mu+b(\delta)V\le 8\pi^2\chi(M).
\]
所有系数均正确，而且
\[
b(\delta)>0
\iff
\delta<\frac{\sqrt3-1}{2}
=\frac1{1+\sqrt3}.
\]

相应体积上界为
\[
V\le \frac{8\pi^2\chi}{b(\delta)}
=\frac{12\pi^2\chi}{1-2\delta-2\delta^2}.
\]
在 \(\delta=0\) 时退化为
\[
V\le12\pi^2\chi,
\]
正是 \(\operatorname{Ric}=\pm g\) 时由 CGB 得到的上界。

### 更强的最优点态下界

\(b(\delta)\) 正确但并非最优。取 \(\sigma=+1\)，记
\[
S=\sum_i e_i,\qquad Q=\sum_i e_i^2.
\]
直接展开得
\[
B=\frac23+\frac S3+\frac{S^2}{6}-\frac Q2.
\]
固定其余三个 \(e_j\) 后，该式关于第四个 \(e_i\) 是凹二次函数，故在立方体 \([-\delta,\delta]^4\) 上的最小值出现在顶点。枚举顶点可得最优统一下界
\[
B\ge\beta(\delta):=
\begin{cases}
\displaystyle \frac23(1-\delta)^2,
&0\le\delta\le\frac13,\\[2mm]
\displaystyle \frac23-\frac23\delta-\frac43\delta^2
=\frac23(1+\delta)(1-2\delta),
&\frac13\le\delta<1.
\end{cases}
\]
\(\sigma=-1\) 通过 \(e_i\mapsto-e_i\) 得到相同结果。因而真正的点态正性区间扩展到
\[
\beta(\delta)>0\iff \delta<\frac12.
\]
所以 Step 4 的全部结论在其写出的 \(\delta<1/(1+\sqrt3)\) 区间成立，并且可统一加强到 \(\delta<1/2\)，把 \(b\) 替换为 \(\beta\)。

## 2. Weyl 能量亏量与体积

Step 4 的上界
\[
B\le a(\delta):=\frac23(1+\delta)^2
\]
也正确，因为
\[
B\le\frac{s^2}{24}\le\frac23(1+\delta)^2.
\]

定义
\[
D_W:=8\pi^2\chi-\int_M|W|^2\,d\mu=\int_M B\,d\mu.
\]
在 \(b(\delta)>0\) 时有精确夹估
\[
b(\delta)V\le D_W\le a(\delta)V.
\]
采用最优下界则为
\[
\beta(\delta)V\le D_W\le a(\delta)V
\qquad(\delta<1/2).
\]

因此：

* 若 \(V\ge v\)，则
  \[
  \int|W|^2\le8\pi^2\chi-\beta(\delta)v.
  \]
* 若
  \[
  \int|W|^2\le8\pi^2\chi-\eta,
  \]
  则
  \[
  V\ge\frac{\eta}{a(\delta)}.
  \]

故“体积正下界”和“Weyl 能量与 \(8\pi^2\chi\) 之间存在正亏量”确实可相互转化，常数只依赖 \(\delta\)。

这里的“塌缩”应精确表述为总体积 \(V_i\to0\)。对 \(\delta_i\) 一致小于 \(1/2\) 的序列，
\[
V_i\to0\iff D_{W,i}\to0.
\]
这条等价关系本身不控制局部注入半径。正号支路中 Myers 给出直径上界，因此总体积正下界连同 Ricci 下界可转化为单位球体积正下界；负号支路没有自动直径控制，故总体积计量不能单独排除局部细部区域。

## 3. 有界全曲率与塌缩

若同一范数约定下
\[
|\operatorname{Rm}|\le K,
\]
则 Weyl 是曲率分解中的正交分量，故 \(|W|\le|\operatorname{Rm}|\)。由 CGB 和 \(B\le a(\delta)\)，
\[
8\pi^2\chi
\le (K^2+a(\delta))V.
\]
另一方面，\(\beta(\delta)>0\) 强制 \(\chi>0\)，所以闭连通四维流形满足 \(\chi\ge1\)，从而
\[
V\ge\frac{8\pi^2}{K^2+a(\delta)}
\qquad(\delta<1/2).
\]
若正号支路且可定向，则 Bochner 与 Poincaré 对偶给出
\[
b_1=b_3=0,\qquad \chi=2+b_2\ge2,
\]
于是分子可加强为 \(16\pi^2\)。

所以 Step 4 的计算确实排除了在统一 \(|\operatorname{Rm}|\) 上界下的总体积趋零。更定量地，
\[
\|W\|_\infty^2
\ge\frac{8\pi^2\chi}{V}-a(\delta)
\ge\frac{8\pi^2}{V}-a(\delta).
\]
因此任何 \(V_i\to0\) 的紧夹逼序列都必有
\[
\|W_{g_i}\|_\infty\to\infty.
\]

### 可进一步提炼出的紧致性定理

设
\[
\delta_i\to0,\qquad
\|\operatorname{Ric}_{g_i}-\sigma g_i\|_{\mathrm{op}}\le\delta_i,
\qquad
|\operatorname{Rm}_{g_i}|\le K,
\]
并且直径一致有界。上述 CGB 估计给出统一体积正下界；Ricci 下界、直径上界和 Bishop–Gromov 比较继而给出局部球体积正下界，曲率上界再给出注入半径控制。谐和坐标中的方程
\[
-\frac12g^{ab}\partial_a\partial_b g_{ij}
+Q_{ij}(g,\partial g)=\operatorname{Ric}_{ij}
\]
允许取 \(C^{1,\alpha}\cap W^{2,p}\) 极限，并把
\(\operatorname{Ric}_{g_i}-\sigma g_i\to0\) 传递为
\[
\operatorname{Ric}_{g_\infty}=\sigma g_\infty.
\]
椭圆正则性使极限光滑，且最终的流形与极限流形微分同胚。因此这些流形本身承载 Einstein 度量。

对正号支路，Myers 自动提供直径上界。由此得到一个比 Step 4 更强的结论：

> 四维正号紧夹逼、但底层流形不承载 Einstein 度量的序列，若 \(\delta_i\to0\)，则其全曲率上确界必趋于无穷。

负号支路中，相同推论需要额外直径上界；否则还存在直径发散这一种几何机制。

## 4. 曲率范数约定

Step 4 第 5 点的“全曲率能量趋于 \(8\pi^2\chi\)”需要明确 \(\operatorname{Rm}\) 的范数。若采用曲率算子 \(\mathcal R:\Lambda^2\to\Lambda^2\) 的 Hilbert–Schmidt 范数，则
\[
|\mathcal R|^2
=|W|^2+\frac{|E|^2}{2}+\frac{s^2}{24},
\]
故
\[
\int|\mathcal R|^2
=8\pi^2\chi+\int|E|^2.
\]
结合
\[
\int|E|^2
\le4\delta^2V
\le\frac{32\pi^2\delta^2}{\beta(\delta)}\chi
\]
可得
\[
\int|\mathcal R|^2
=8\pi^2\chi+O(\delta^2\chi).
\]

若 \(|\operatorname{Rm}|\) 表示完整 \((0,4)\)-张量范数，则会出现整体因子 \(4\)。Step 3 曾出现因子错误，因此在后续 TeX 中固定这一约定很重要。

## 5. 拓扑与两条符号支路

目标逻辑正确。若正号稳定命题对某个 \(\delta_0>0\) 成立，则直接取
\[
c_4=1-\delta_0,\qquad C_4=1+\delta_0
\]
即可得到原始区间命题；负号同理。反过来，若原始区间命题不成立，则它尤其对任意小的
\[
[1-\delta,1+\delta]
\quad\text{和}\quad
[-1-\delta,-1+\delta]
\]
都不成立。因此同一维数中两种符号都必须出现不承载 Einstein 度量的紧夹逼序列。

所以 \(p=k/A\to1/3^+\) 的 LeBrun 负号临界序列，即使能够构造，也只处理其中一条符号支路，不能单独否定四维原命题。Step 4 对此的逻辑完全正确。

由
\[
4\pi^2(2\chi\pm3\tau)
=\int\left(2|W^\pm|^2+B\right)d\mu
\]
以及 \(\beta(\delta)>0\)，还可加强为
\[
2\chi\pm3\tau>0,\qquad
2\chi>3|\tau|
\qquad(\delta<1/2).
\]
因此由 Hitchin–Thorpe 数值关系排除 Einstein 度量的拓扑，也不能承载任意紧的任一符号 Ricci 夹逼。

对
\[
M=\#_k\mathbb{CP}^2,
\qquad
\chi=k+2,\quad \tau=k,
\]
有
\[
2\chi-3\tau=4-k.
\]
故这一论证直接覆盖 \(k=4\) 的等号情形和 \(k\ge5\) 的严格反向情形；\(k=2,3\) 并不由该数值关系处理。Step 4 中“connected sums of \(\mathbb{CP}^2\)”最好附上这一 \(k\) 值说明。

## 6. Seiberg–Witten 正号表述

若所用类是对每个度量都有效的非平凡 monopole class，或处于 \(b_2^+>1\) 且非零 SW 不变量给出这种度量无关输入的情形，则
\[
\delta_+<1
\Longrightarrow
\operatorname{Ric}>0
\Longrightarrow
s>0
\]
与 monopole 方程的 Weitzenböck 论证不相容。因此这类 LeBrun 流形确实不能提供正号输入度量。

但“nonzero SW”本身在 \(b_2^+=1\) 时涉及 chamber 依赖，不能无条件替代“对所有度量有效的 monopole class”。Step 4 前部已经列出“relevant polarization/monopole-class input”，后部的正号句子也需要保留同样的适用条件。当前提供的源文摘要不足以把该句扩展到所有未注明 \(b_2^+\) 的一般型曲面爆破。

## 7. Anderson、Cheeger–Naber、Ozuch、Min-Oo 与 Ye

Step 4 对现有源文的区分是准确的：

* Ozuch 的 Theorem 0.1 从**精确 Einstein** 四维流形、体积正下界、直径上界和 \(L^2\) 曲率控制出发，得到 Einstein orbifold 与 Ricci-flat ALE bubble。
* Ozuch 的 Theorem 0.2 仍假设输入度量本身 Einstein；它描述接近 orbifold 时的 gluing–perturbation 结构，不从一般 \(\|\operatorname{Ric}-\lambda g\|\ll1\) 推出 Einstein 度量。
* Cheeger–Naber 的 Theorems 1.12、1.13 给出非塌缩、双侧 Ricci 有界四维流形的有限微分同胚型和局部 \(L^2\) 全曲率估计；这些不是 Einstein 存在定理。
* Min-Oo 原文定理明确要求 \(n>3\)、负平均标量曲率，并带有直径—截面曲率尺度参数 \(\Lambda\)。它不能产生只依赖维数的 Ricci 夹逼常数。
* 当前文件中没有 Ye 1993 的定理正文。仅凭二手稳定性引用，不能把 Ye 当成从任意全局 Ricci 紧夹逼度量产生 Einstein 度量的依据。
* Anderson 1989 在现有材料中只由 Ozuch 用于精确 Einstein 紧化。其 Corollary B(4) 的准确假设尚未出现在提供的源文中，因此 Step 4 暂不赋予它更强用途是有根据的。

## 总结

Step 4 的核心 CGB 等式、\(b(\delta)\)、体积上界、Weyl 亏量—体积夹估以及统一全曲率上界排除总体积趋零，全部数学成立。最有实质意义的增强有四项：

1. 点态下界可由 \(b(\delta)\) 提升为最优的 \(\beta(\delta)\)，正性延伸到 \(\delta<1/2\)。
2. “塌缩”在该计量中应解释为总体积趋零；负号支路的局部细部几何还需要直径或局部球体积信息。
3. 正号支路结合 Myers，可把“有界全曲率时体积不趋零”提升为“有界全曲率的 \(\delta_i\to0\) 序列最终具有 Einstein 微分拓扑”。
4. LeBrun/SW 正号排除必须明确 metric-independent monopole class 或相应 \(b_2^+>1\) 条件；普通 chamber-dependent SW 信息不足以支撑无条件表述。
# Yau Problem Set 研究基线与 AI 攻关路线
## ——本会话完整整理：问题状态、数学本质、AI 适配性、Yau 19/23/26 路线与 Qiushi Engine 研究方法

**整理日期：2026-09-15**  
**用途：下一会话研究交接与长期研究基线。**

---

## 0. 核心结论

本会话形成的最重要判断不是“挑最著名的问题”，而是区分：

\[
\boxed{\text{数学价值/难度}}
\qquad\text{与}\qquad
\boxed{\text{当前 AI/LLM 的可攻性}}
\]

二者不是同一个排序。

对于 Yau 1982 年 `Problem Section` 中的 Problem 18–32：

- 原题已经解决或原猜想已被否定：**18、21、24、30、31、32**。
- 按“原题一般形式仍未彻底解决或只部分解决”计算，应包括：  
  **19、20、22、23、25、26、27、28、29**。
- 之前会话中常用的“仍真正开放：19、20、22、23、25、26、28”是一个较窄的筛选，不应误解为 18–32 中全部尚未完成的问题；**27、29 的一般形式也仍未完全解决**。

若目标是“让当前 LLM/Agent 系统最大化产生原创、严格数学进展的概率”，本会话的综合排序是：

\[
\boxed{
23_{\text{explicit K3}}
>
19_{\text{concrete realization/obstruction}}
>
22_{\text{concrete subgroup/geometry}}
\gg
26
>
20
>
25,28
}
\]

若把 27、29 也纳入，则它们其实非常值得考虑，尤其：

\[
\boxed{
29_{n=6},\quad 27_{\text{剩余三维非紧分类}}
}
\]

它们具有“已有强前沿 + 明确断点 + 下一步可裁决”的良好 AI 研究结构。

对于 Qiushi Engine 当前最值得押注的两个方向：

1. **主线：Yau 23 的显式 K3 Ricci-flat metric 分支**  
   不是随机搜 metric，而是攻击 Kummer 构造中最后的无限维修正项，寻找其可压缩、精确、可证明的表示。

2. **副线：Yau 19 的 \(n=4,k=1\) 局部 realization / obstruction**  
   研究
   \[
   g\mapsto p_1(\nabla^g)
   \]
   的线性化、主符号、局部像与余核；优先裁决局部可实现性，而不是一开始直接做任意维数、任意 Pontryagin 类。

这两个方向分别测试两种 AI 科研能力：

- Yau 23：**数值发现 → 结构压缩 → 符号化 → exactification → 严格 PDE 证明**；
- Yau 19：**几何算子分析 → 不变量/表示论 → 局部定理或新障碍 → 全局拼接**。

---

# 1. Yau Problem 18–32：完整状态地图

原始来源：

> Shing-Tung Yau, *Problem Section*, in *Seminar on Differential Geometry*, Annals of Mathematics Studies 102, Princeton University Press, 1982, pp. 669–706.

这一组主要位于曲率、Ricci 曲率、Einstein 度量和标量曲率方向。

| Problem | 原问题核心 | 当前总体状态 | 对当前 AI 的意义 |
|---|---|---|---|
| 18 | 完备非紧 \(K\ge0\)，若一点严格正曲率，是否微分同胚于 \(\mathbb R^N\) | 已解决；Perelman 的 soul conjecture 工作 | 不作为开放主线 |
| **19** | 给定 Pontryagin 类的闭形式代表，何时能成为某个 Riemannian metric 的 Levi-Civita Chern–Weil 曲率形式 | **开放** | **强 AI 候选** |
| **20** | 刻画哪些对称张量 \(T_{ij}\) 可成为某个 metric 的 Einstein tensor | **全局问题开放** | 难；PDE + gauge + topology |
| 21 | 完备正 Ricci 流形是否总有有限拓扑型/可视为紧流形带边界内部 | 一般陈述为假 | 不作为原题开放线 |
| **22** | 刻画完备正 Ricci 流形的基本群 | **一般形式开放** | 中等适合；可切具体群/维数/增长条件 |
| **23** | K3 上构造显式 Ricci-flat metric；以及四维 Ricci-flat manifold 分类 | **开放** | **显式 K3 分支最适合当前 AI** |
| 24 | 每个 \(n\ge3\) 光滑流形是否有负 Ricci metric | 已解决；Lohkamp 等 | 不作为原题开放线 |
| **25** | 分类紧致四维负 Einstein manifold；\(S^4\) 是否可有负 Einstein metric | **开放** | 极难；不宜作为当前 AI 首攻 |
| **26** | 是否存在只依赖维数的 Ricci pinching 常数，迫使流形存在 Einstein metric | **一般形式开放** | 数学重要，但当前 LLM 适配较差 |
| **27** | 分类完备三维 \(R\ge0\) 流形 | **部分解决，一般非紧情形未完全完成** | **较适合 AI 推进具体剩余边界** |
| **28** | 分类紧致四维正标量曲率 Einstein manifolds | **开放** | 极难；分类空间太大 |
| **29** | compact \(K(\pi,1)\) + \(R\ge0\) 是否必 flat | **低维强进展，一般高维开放** | **很适合攻下一维/明确断点** |
| 30 | 紧三维单连通流形是否为 \(S^3\) | 已解决；Perelman | 不作为开放主线 |
| 31 | 欧氏空间中紧嵌入常标量曲率超曲面是否为球面 | 原嵌入问题已解决；Ros | 不作为开放主线 |
| 32 | compact Yamabe problem | 已解决；Yamabe–Trudinger–Aubin–Schoen | 不作为开放主线 |

---

# 2. 什么样的数学问题“适合当前 LLM/Agent”

不能只看问题是否著名。真正适合 AI 的问题通常同时具有以下结构：

\[
\boxed{
\text{前沿边界明确}
+
\text{候选对象可生成}
+
\text{中间反馈丰富}
+
\text{失败可证伪}
+
\text{最终结果可严格验证}
}
\]

当前 LLM/Agent 最有优势的工作包括：

- 文献和定理假设的系统梳理；
- 大规模候选生成与反例攻击；
- 符号推导、张量代数、表示论计算；
- 有限组合搜索；
- 数值 PDE、高精度计算、自动微分；
- 模式发现、整数关系、特殊函数猜测；
- 将数值候选 exactify；
- 区间算术、SAT/SMT、CAS、Lean 等严格验证；
- 多路线并行后收敛到一个决定性障碍。

当前 LLM 最危险的场景是：

\[
\text{一个巨大开放命题}
\rightarrow
\text{连续几十页“似乎合理”的推导}
\rightarrow
\text{中间偷偷引入未证明的全局性质}
\]

因此应避免把“长推理”误认为“研究进展”。

---

# 3. Yau 26：数学本质与为什么它不适合当前 LLM 首攻

## 3.1 数学领域

Yau 26 本质属于：

\[
\boxed{
\text{Global Riemannian Geometry}
+
\text{Geometric Analysis}
+
\text{Nonlinear PDE}
+
\text{Global Analysis}
+
\text{Topology}
}
\]

Einstein metric 满足

\[
\operatorname{Ric}(g)=\lambda g.
\]

经过 gauge fixing 后，Einstein 方程可以视为一个非线性椭圆 PDE 系统。

Problem 26 的核心不是“算一个 Ricci tensor”，而是：

> 仅凭给定 metric 的 Ricci tensor 足够夹逼，能否推出**底层流形上存在某个 Einstein metric**？

原始形式可概括为寻找只依赖维数 \(N\) 的常数 \(c_N<C_N\)，使适当 Ricci 双边夹逼能够推出 Einstein metric 的存在。

## 3.2 真正的困难

高维中：

\[
\operatorname{Ric}
\]

只是完整 Riemann curvature 的缩并。它并不直接控制：

- Weyl curvature；
- collapse；
- injectivity radius；
- bubbling / degeneration；
- Einstein/Lichnerowicz operator 的谱隙；
- 全局拓扑；
- perturbation 所需的非退化性。

LLM 很容易无意中使用：

\[
\text{Ricci pinching}
\Rightarrow
\text{compactness}
\Rightarrow
\text{curvature control}
\Rightarrow
\text{spectral gap}
\Rightarrow
\text{Einstein}
\]

但其中每个箭头都可能正是开放问题。

真正可能决定 Yau 26 的机制应接近：

\[
\boxed{
\text{Ricci pinching}
\Longrightarrow
\text{某种统一的 noncollapse/curvature/spectral control}
}
\]

或者反方向：

\[
\boxed{
\text{构造任意强 Ricci pinching}
\quad+\quad
\text{底层流形仍不存在任何 Einstein metric}
}
\]

这要求发明新的**全局几何机制**，而不是算力堆积。

## 3.3 已知研究线的正确理解

与该问题相关的重要方向包括：

- Michael T. Anderson：Ricci bounds、紧性、almost-Einstein 与 Einstein metrics；
- Maung Min-Oo：负 Ricci almost-Einstein 路线；
- Dale Skinner：三维负 pinching / hyperbolic metric 的修正性结果；
- Frieder Jäckel、Ursula Hamenstädt：负曲率 Einstein stability / effective hyperbolization；
- Joel Fine、Bruno Premoselli：近似 Einstein 构造经严格扰动得到 Einstein metric；
- Jiang–Naber：Ricci 控制下的曲率能量与奇异结构；
- Tian–Wang：almost-Einstein limits；
- Ozuch、LeBrun、Biquard、Kröncke：Einstein deformation、obstruction、stability；
- Bamler：Dehn filling / Einstein 构造；
- Böhm–Wilking、Brendle–Schoen：更强 curvature operator / sectional pinching 下的 Ricci flow 与 rigidity。

关键区分：

\[
\boxed{
\text{“某个近似 Einstein metric 可以被修正”}
\neq
\text{“纯 Ricci pinching 自动保证存在 Einstein metric”}
}
\]

Jäckel 的近期稳定性定理仍需要额外的负 sectional curvature、薄部结构、Ricci 导数与 \(C^0/L^2\) 误差控制；因此不能等同于 Yau 26 的一般结论。

## 3.4 AI 对 Yau 26 最合理的用法

不是直接要求“证明 Yau 26”，而是固定一个决定性子问题，例如：

- 纯 Ricci pinching 是否能推出 uniform spectral gap？
- 能否构造 Ricci pinching 很强但 Weyl curvature 爆炸的序列？
- 哪一个 Anderson/Jäckel 型额外条件是不可删除的？
- 是否存在拓扑族能同时满足任意强 Ricci pinching而排除 Einstein metric？

每次只攻击一个硬障碍，直到证明、反例或精确边界出现。

---

# 4. 为什么“开一万台计算机随机搜索”不能直接解决 Yau 19/23

这两个问题都不是有限集合搜索问题。

一个 metric 是

\[
g\in C^\infty(S^2T^*M),
\]

即整个流形上的光滑对称二阶张量场。搜索空间是无限维连续函数空间。

随机搜索一个候选 metric，要求：

\[
\operatorname{Ric}(g)\equiv0
\]

不是“数值很小”，而是**全局精确恒等式**。

即便得到

\[
\|\operatorname{Ric}(g)\|=10^{-30},
\]

仍然只是近似解。

而且必须同时证明：

- \(g\) 正定；
- 全局光滑；
- 坐标图之间正确拼接；
- 没有隐藏奇点；
- 对象确实定义在目标 K3/流形上；
- PDE 精确成立。

## 4.1 表示瓶颈比算力瓶颈更重要

若只搜索有限参数族

\[
g(a_1,\dots,a_m),
\]

真正解可能根本不在这个 ansatz 中。

此时：

\[
10^4\text{ computers}
\quad\text{或}\quad
10^{10}\text{ computers}
\]

都没有本质帮助。

真正重要的是发现：

\[
\boxed{
\text{一个正确的表示/ansatz/隐藏结构}
}
\]

使原本无限维的问题降维为有限或高度结构化的问题。

因此数学研究中最关键的常常不是：

> 搜得多快？

而是：

> **到底应该在什么空间里搜？**

## 4.2 “almost solution” 到 exact solution 的鸿沟

计算机天然擅长：

\[
\|F(x)\|\ll1.
\]

数学需要：

\[
F(x)=0.
\]

若存在稳定性定理：

\[
\|F(x)\|<\varepsilon
\Longrightarrow
\exists x^*,\;F(x^*)=0,
\]

那么数值搜索非常有价值。

但证明这种稳定性通常要求：

- \(DF_x\) 可逆；
- uniform inverse bound；
- spectral gap；
- nondegeneracy；
- compactness；
- error control。

这些条件往往本身就是开放问题最难的部分。

因此正确流水线应是：

\[
\boxed{
\text{结构发现}
\rightarrow
\text{有限化/压缩}
\rightarrow
\text{计算搜索}
\rightarrow
\text{候选}
\rightarrow
\text{exactification}
\rightarrow
\text{严格证明}
}
\]

而不是随机枚举公式。

---

# 5. Yau 23：为什么是当前最值得押注的主线

## 5.1 原题分成两个难度完全不同的部分

Problem 23 包含：

1. 在 K3 surface 上构造一个**显式 Ricci-flat metric**；
2. 更广泛地理解/分类四维 compact Ricci-flat manifolds。

这两个目标必须分开。

第二个“完整分类”非常深，不适合当前 LLM 直接全攻。

第一部分：

\[
\boxed{\text{explicit Ricci-flat metric on compact K3}}
\]

更适合 AI，因为：

- 解的存在性已经由 Yau 的 Calabi conjecture 定理保证；
- 有成熟数值和渐近构造可提供“目标信号”；
- 可以计算 Ricci/Monge–Ampère residual；
- 可以寻找隐藏的特殊函数/谱/格点结构；
- 候选最终可通过严格 PDE/级数收敛验证。

因此这是一个：

\[
\text{已知存在}
\rightarrow
\text{未知结构}
\]

的问题，而不是“甚至不知道真假”的命题。

## 5.2 与 Millennium Problems 的关系

不能说 Yau 23 比千禧年七大问题更难。

更合理的判断是：

- **显式 K3 metric 分支**通常比多数仍未解决的 Millennium Problems 更窄、更具体、更可计算；
- **四维 Ricci-flat 完整分类**则极深，不能轻率比较；
- “更适合 AI”不等于“更难”或“价值更高”。

显式 K3 分支适合 AI 的关键，是存在：

\[
\text{候选}
\rightarrow
\text{数值残差}
\rightarrow
\text{结构发现}
\rightarrow
\text{严格验证}
\]

这样的反馈环。

---

# 6. Yau 23：最值得突破的具体路线

## 6.1 不要随机搜索 \(g\)，而要攻击 Kummer 构造的最后修正项

Kummer 路线从：

\[
T^4/\{\pm1\}
\]

开始。

这个 orbifold 在 16 个固定点有奇点。局部可用显式 Eguchi–Hanson Ricci-flat 模型解析这些奇点，形成一个非常精确的近似 Kähler metric。

然后真正的 Ricci-flat metric 可写成：

\[
\omega
=
\omega_0+i\partial\bar\partial u,
\]

其中：

- \(\omega_0\)：显式/高度可控的近似拼接 Kähler form；
- \(u\)：全局修正势函数。

\(u\) 满足复 Monge–Ampère 方程：

\[
(\omega_0+i\partial\bar\partial u)^2
=
c\,\Omega\wedge\bar\Omega.
\]

因此“显式 K3 metric”的核心未知量实际上高度集中在：

\[
\boxed{u}
\]

而不是整个 \(g\)。

这给出一个比“随机 metric 搜索”强得多的表示。

## 6.2 不要寄希望于简单连续对称性降成 ODE

一个重要结构事实：

在 compact Ricci-flat manifold 上，Killing vector field 受 Bochner 公式强约束；在 K3 上 \(b_1=0\)，因此不存在非零平行向量场，Ricci-flat K3 不具有非平凡连续等距群的恒等分支。

这意味着：

\[
\boxed{
\text{不要期待靠 cohomogeneity-one 连续对称性把整个 K3 PDE 神奇降成 ODE}
}
\]

真正可利用的是：

- 离散对称性；
- lattice / torus 结构；
- Kummer involution；
- 局部 Eguchi–Hanson 精确模型；
- 全局谱表示；
- degeneration / gluing scale。

## 6.3 最有希望的表示：局部显式 + 全局谱

建议构造三个互补表示层：

### Bulk

远离 exceptional divisors 的区域接近平坦 torus quotient，可使用：

\[
\text{Fourier / lattice modes}.
\]

### Bubble

16 个 resolution 区域使用：

\[
\text{Eguchi–Hanson adapted modes/eigenfunctions}.
\]

### Matching

拼接环带使用：

\[
\text{overlap / transition modes}.
\]

于是把修正项表示成：

\[
u
=
\sum_\alpha c_\alpha\phi_\alpha.
\]

AI 的任务不是仅仅把 residual 降低，而是分析系数：

\[
c_\alpha(\varepsilon)
\]

是否显示出精确结构，例如：

- theta functions；
- modular/automorphic structure；
- lattice sums；
- Green kernels；
- 特殊函数；
- 可递推的代数/解析系数；
- 极度稀疏的谱结构。

## 6.4 正确的 AI 闭环

### 阶段 A：得到高精度 target

用成熟的：

- 数值 Monge–Ampère；
- balanced metrics；
- neural Calabi–Yau approximation；
- spectral/PDE solvers；

得到多个 Kähler 参数、多个 gluing scale 下的高精度 \(u\)。

### 阶段 B：结构发现

不直接接受神经网络。

从数值解中提取：

- Fourier/EH 模态系数；
- asymptotic scaling law；
- 整数关系；
- recurrence；
- symmetry selection rules；
- theta/lattice patterns。

使用：

- PSLQ；
- symbolic regression；
- exact rational/algebraic reconstruction；
- high-precision consistency checks。

### 阶段 C：猜精确表示

目标不是“拟合函数”，而是形成：

\[
u=\sum_{m=0}^{\infty}u_m
\]

或某种特殊函数/格点和表达式。

### 阶段 D：反向代入 PDE

证明：

\[
(\omega_0+i\partial\bar\partial u)^2
=
c\Omega\wedge\bar\Omega,
\]

并证明：

\[
\omega_0+i\partial\bar\partial u>0.
\]

### 阶段 E：严格收敛

例如证明：

\[
\sum_m \|u_m\|_{C^{2,\alpha}}<\infty
\]

或更适合该表示的函数空间估计。

### 阶段 F：显式性的标准

必须事先定义清楚什么算“explicit”：

- 有限闭式特殊函数表达；
- 全局可计算且系数精确递推的收敛级数；
- 有限算法表示 + 严格收敛证书；
- 仅通过“存在唯一 PDE 解”隐式定义，通常不能算完成原始显式目标。

“可计算”与“显式”不能混为一谈。

## 6.5 第一决定性关口

Yau 23 不应同时开 100 条路线。

第一关只问：

\[
\boxed{
\text{Kummer 修正 }u
\text{ 是否存在跨尺度稳定、极度可压缩的精确谱/特殊函数结构？}
}
\]

若答案 NO，就尽快否掉这条 exactification 路线。

若答案 YES，再集中全部资源证明它。

---

# 7. Yau 19：数学本质

原问题：

给定 compact manifold \(M\) 上代表某个 Pontryagin class 的闭 \(4k\)-form

\[
\Omega,
\]

能否找到 Riemannian metric \(g\)，使 \(\Omega\) 正好等于该 metric 的 Levi-Civita curvature 通过 Chern–Weil 构造得到的 Pontryagin form？

形式化地定义：

\[
\mathcal P_k:
\operatorname{Met}(M)
\longrightarrow
\Omega^{4k}(M),
\]

\[
\mathcal P_k(g)=p_k(\nabla^g).
\]

问题本质是：

\[
\boxed{
\operatorname{Im}\mathcal P_k = ?
}
\]

已知：

\[
[\mathcal P_k(g)]
=
p_k(M)
\]

是拓扑不变量，因此不同 metric 改变的是同一 cohomology class 中的**精确部分**。

真正困难之处：

> 任意 connection 的 Chern–Weil representability 与 Levi-Civita connection 的 representability 完全不同。

Levi-Civita curvature 必须同时满足：

- torsion-free；
- metric compatibility；
- Riemann curvature 的代数对称性；
- Bianchi identities；
- curvature 来自某个 metric 的二阶 jet；
- 全局拼接与正定性。

因此不能把一般 connection 的自由度直接移植过来。

---

# 8. Yau 19：最有希望的路线

## 8.1 不从任意 \(n,k\) 开始

第一模型固定：

\[
\boxed{
n=4,\qquad k=1.
}
\]

研究：

\[
\mathcal P_1(g)=p_1(\nabla^g)\in\Omega^4(M).
\]

四维的好处：

- \(p_1\) 已经是 top-degree form；
- 与 signature density / self-dual–anti-self-dual curvature 紧密相关；
- Weyl decomposition、conformal geometry 结构丰富；
- tensor algebra 规模仍能被 CAS/representation theory 精确处理。

## 8.2 研究线性化

考虑：

\[
D\mathcal P_1|_g(h).
\]

Chern–Weil transgression 告诉我们：

\[
\frac{d}{dt}p_1(\nabla^{g_t})
\]

是 exact form。

这与原问题高度匹配，因为同一个 Pontryagin class 中两个代表之差本来就是 exact。

第一任务：

\[
\boxed{
\text{计算并理解 }D\mathcal P_1
\text{ 的 principal symbol、像与余核}
}
\]

特别注意：

- \(p_1\) 对 curvature 是二次的；
- 在过度退化的背景（例如平坦背景）上线性化可能丢失信息；
- 应优先在**generic curved background**上研究，而不是仅在线性化最方便但最退化的点上工作。

## 8.3 第一个真正值得证明/否定的局部命题

可设定局部 realization 问题：

> 对 generic metric \(g\)，给定一个足够小、支撑在坐标球内的 exact 4-form \(\eta\)，是否存在局部 metric perturbation \(h\)，使
> \[
> p_1(g+h)=p_1(g)+\eta
> \]
> （精确或通过可控的非线性校正实现）？

这不是预设为真，而是**第一决定性裁决题**。

两种结果都有价值：

### 若局部 surjectivity 成立

则可尝试：

\[
\Omega-p_1(g_0)=d\alpha
\]

并利用 fragmentation / partition of unity 分解为局部修正：

\[
d\alpha=\eta_1+\cdots+\eta_N,
\]

逐块调整 metric：

\[
g_0\to g_1\to\cdots\to g_N.
\]

真正困难将转移到：

- 局部修改是否互不破坏；
- 非线性误差如何迭代；
- metric 正定性；
- 全局 gauge/compatibility；
- 是否存在 loss of derivatives；
- 是否需要 Nash–Moser 而非普通 implicit function theorem。

### 若局部 surjectivity 失败

研究：

\[
\operatorname{coker}D\mathcal P_1
\]

可能直接暴露新的 differential obstruction。

这可能正是 Yau 原问题中“应该存在的额外拓扑/微分障碍”的一部分。

因此这是一个非常好的双向研究：

\[
\boxed{
\text{surjective}
\Rightarrow
\text{存在性路线}
}
\]

\[
\boxed{
\text{not surjective}
\Rightarrow
\text{新 obstruction 路线}
}
\]

## 8.4 Qiushi 在这里的具体工具价值

特别适合自动化：

- Riemann tensor symmetry reduction；
- Bianchi identities；
- jet-space parameterization；
- tensor invariant enumeration；
- representation decomposition；
- symbol matrix exact rank；
- rational random specialization；
- Gröbner basis；
- exact linear algebra；
- SMT/SAT 搜索特殊 algebraic curvature models；
- CAS 验证；
- 最终将关键恒等式形式化。

重要原则：

> 数值 random rank 只能用于发现 generic rank；最终必须给出 exact symbolic/rational certificate。

## 8.5 第一决定性关口

Yau 19 第一阶段只做：

\[
\boxed{
D(g\mapsto p_1(g))
\text{ 在四维 generic metric 上的局部像究竟是什么？}
}
\]

不要先写几十页全局 proof。

先把这一个问题彻底裁决。

---

# 9. Yau 23 与 Yau 19：为什么不是“没人研究的简单问题”

两者都已有几十年的大量相关研究。

## Yau 23 的研究传统

包括：

- Yau：Calabi conjecture / Ricci-flat Kähler metric existence；
- Kummer construction；
- Gross–Wilson：elliptic K3 collapsing；
- Donaldson：numerical/balanced Calabi–Yau metrics；
- Foscolo：collapsing hyperkähler K3 / gluing；
- Hein–Sun–Viaclovsky–Zhang：collapse、bubbling、nilpotent structures；
- Chen–Viaclovsky–Zhang：elliptic K3 collapsing Ricci-flat metrics；
- Thomas Jiang：Kummer construction 的新分析；
- 2026 年 Shackleton：Kummer surface 上新的 Calabi–Yau metric gluing formulation；
- numerical / machine-learning Calabi–Yau metric work。

“仍没有简单闭式公式”不是因为没人算，而是因为全局非线性修正具有深结构。

## Yau 19 的研究传统

属于：

- Chern–Weil theory；
- characteristic classes；
- curvature prescription；
- prescribed Ricci / geometric PDE；
- connection representability；
- Hermitian Chern–Weil representability；
- Levi-Civita curvature constraints。

难点不是生成 Chern–Weil form，而是：

\[
\boxed{
\text{哪些形式能够来自 Levi-Civita connection？}
}
\]

这是高度受约束的非线性微分几何问题。

---

# 10. 为什么 Yau 25/28 不应作为当前 AI 主战场

Yau 25：

\[
\text{classify compact 4D negative Einstein manifolds}
\]

Yau 28：

\[
\text{classify compact 4D positive Einstein manifolds}
\]

“分类”意味着研究：

\[
\{\text{smooth 4-manifolds}\}
\times
\{\text{Einstein metrics}\}
/(\mathrm{Diff}\times\mathrm{scale}).
\]

涉及：

- smooth 4-manifold topology；
- gauge theory；
- Seiberg–Witten；
- nonlinear Einstein PDE；
- moduli；
- degeneration；
- compactness；
- topology/geometry geography；
- existence / uniqueness / stability / connected components。

这类问题不是缺算力，而是缺一个足够统一的新理论结构。

当前 LLM 很容易生成大量“相关路线”，但缺乏决定性反馈，因此不适合作为第一旗舰。

---

# 11. Problem 20 与 22 的位置

## Problem 20

Einstein tensor prescription：

\[
R_{ij}-\frac12Rg_{ij}=T_{ij}.
\]

难点：

- \(T\) 的 divergence-free 条件依赖未知 metric；
- gauge freedom；
- 全局 nonlinear PDE；
- topology；
- boundary conditions；
- necessary-and-sufficient characterization 的目标过强。

局部 prescribed Ricci / perturbative results 与全局原题差距大。

因此适合研究小的局部/边界/非退化子问题，不适合当前直接全解。

## Problem 22

正 Ricci 完备流形的基本群：

\[
\pi_1(M),\qquad \operatorname{Ric}>0.
\]

相对更适合 AI，因为可以切成：

- 指定 group 是否可 realization；
- 指定维数；
- warped product / surgery construction；
- volume growth；
- nilpotent / polycyclic / finite constraints；
- geometry at infinity。

但必须严格区分：

\[
\operatorname{Ric}>0
\quad\text{与}\quad
\operatorname{Ric}\ge0.
\]

非负 Ricci 的反例或群结构不能无条件升级到严格正 Ricci。

---

# 12. Problem 27 与 29：此前筛选中被低估的两个 AI 候选

## Problem 27

目标：

\[
\text{classify complete 3-manifolds with }R\ge0.
\]

compact 情形与 uniformly positive 等大量子情形已有强结果，但完全一般的 noncompact \(R\ge0\) 分类仍存在边界问题。

它适合 AI 的原因：

- 只有 3 维；
- 现代工具很明确：\(\mu\)-bubbles、minimal surfaces、harmonic functions、ends、inverse mean curvature flow；
- 近年仍持续有“明确推进一步即可形成新定理”的空间；
- 可以把未知边界分成可裁决的小类。

## Problem 29

目标：

\[
M\text{ compact }K(\pi,1),\quad R\ge0
\Rightarrow
M\text{ flat?}
\]

低维已经有强结果，一般高维仍开放。

最合理的 AI 策略不是“一步证明所有维数”，而是：

\[
\boxed{\text{找到当前定理的第一未覆盖维数/第一技术断点}}
\]

例如系统分析：

- minimal hypersurface regularity；
- \(\mu\)-bubble descent；
- slice-and-dice；
- topology control；
- dimension-dependent singularity。

这种：

\[
\text{已有 proof}
+
\text{唯一明确断点}
+
\text{下一维}
\]

通常比 Yau 26 的“缺一个未知全局机制”更适合 AI。

---

# 13. Qiushi Engine 为什么仍值得攻 Yau 19/23

不是因为“LLM 很聪明”或“GPU 很多”。

真正的系统优势应该来自：

## 13.1 长期状态

保存：

- 已否定 ansatz；
- 已知 obstruction；
- 所有 lemma 依赖；
- 数值数据；
- exact certificate；
- 路线失败原因。

避免每次会话重新开始。

## 13.2 异构工具闭环

\[
\text{LLM hypothesis}
\rightarrow
\text{CAS}
\rightarrow
\text{numerical solver}
\rightarrow
\text{counterexample search}
\rightarrow
\text{exact algebra}
\rightarrow
\text{formal verification}
\]

## 13.3 并行不是“随机发散”

Agent 并行应承担不同角色：

- constructor；
- skeptic / counterexample hunter；
- exactifier；
- literature auditor；
- proof verifier。

不是让 100 个 Agent 各自产生 100 个故事。

## 13.4 研究单位应是“决定性障碍”

错误方式：

\[
\text{Agent Step 1–500：不断换想法}
\]

正确方式：

\[
\boxed{
\text{一个关键命题}
\rightarrow
\text{连续几十/几百步攻到真/假/边界清楚}
}
\]

---

# 14. 两条主线的资源配置建议

## 主线 A：Yau 23 Kummer exactification

建议资源：**约 70%**

唯一第一目标：

\[
\boxed{
\text{Kummer 修正势 }u
\text{ 是否存在高度可压缩、跨尺度稳定的精确表示？}
}
\]

工作包：

1. 建立权威 Kummer 几何与坐标实现；
2. 高精度求解多个参数点；
3. 构造 bulk/bubble/matching basis；
4. 提取谱系数；
5. 搜索递推、格点和、theta/automorphic 结构；
6. 交叉参数验证；
7. exact reconstruction；
8. 反向代入 Monge–Ampère；
9. 收敛和正定证明；
10. 独立 verifier。

## 副线 B：Yau 19 \(n=4,k=1\)

建议资源：**约 30%**

唯一第一目标：

\[
\boxed{
D\mathcal P_1|_g
\text{ 在 generic 4D metric 上的局部像/余核}
}
\]

工作包：

1. 固定 conventions；
2. 推导 \(p_1\) 与其 variation；
3. gauge/diffeomorphism directions 分离；
4. generic algebraic curvature background；
5. principal symbol exact computation；
6. representation decomposition；
7. generic rank certificate；
8. 若满秩：局部 nonlinear inversion；
9. 若不满秩：提取 invariant obstruction；
10. 再决定是否进入 global patching。

---

# 15. 研究品味：本会话最重要的方法论

## 15.1 不要把“熟悉”当“容易”

LLM 对：

- Ricci flow；
- Einstein metric；
- Kähler geometry；
- Chern–Weil；
- PDE；

训练知识很多。

但：

\[
\boxed{\text{知识密度高}\neq\text{开放问题突破概率高}}
\]

Yau 26 就是典型例子。

## 15.2 不要把“近似很好”当“定理快完成”

\[
10^{-30}\neq0.
\]

必须问：

> 有什么 theorem 能把近似解 exactify？

如果没有，就仍然停留在 numerical evidence。

## 15.3 优先寻找可证伪路线

好的路线应该能在有限时间被判：

- 真；
- 假；
- 缺哪个条件。

而不是永远“还可以继续优化”。

## 15.4 表示优先于算力

世界级数学问题中：

\[
\boxed{
\text{找到正确 representation}
>
\text{增加 10000 倍 brute-force compute}
}
\]

算力应在正确的压缩空间里使用。

## 15.5 先找决定性 lemma，而不是先写论文

论文结构应来自已闭合的数学结果。

不要先构造 narrative，再让证明适配 narrative。

## 15.6 失败结果要永久保留

一个被严格否定的强 ansatz 很有价值，因为它缩小真实搜索空间。

Qiushi 应把：

\[
\text{失败}
\rightarrow
\text{结构性原因}
\rightarrow
\text{下一次不再重复}
\]

变成系统长期能力。

## 15.7 原题必须忠实

任何进展都必须明确属于：

- full solution；
- special case；
- conditional theorem；
- obstruction；
- numerical evidence；
- conjectural mechanism。

不能把“非常接近”包装成“已解决”。

---

# 16. 两题的成功标准

## Yau 23

### 最强成功

给出 compact K3 上真正显式、全局、光滑、正定的 Ricci-flat metric，并严格证明：

\[
\operatorname{Ric}(g)=0.
\]

### 强中间结果

- 新的全局精确级数表示；
- 系数显式递推且证明收敛；
- 新的特殊函数/自动形式表达；
- 将此前隐式 correction 显著 exactify；
- 对某个高度对称 K3 给出前所未有的解析表示。

### 不算解决

- neural network approximation；
- residual 很小；
- 有限精度网格；
- 仅依赖“唯一 PDE 解存在”的隐式定义而没有新的显式结构。

## Yau 19

### 最强成功

给出 Pontryagin form Levi-Civita representability 的一般 necessary-and-sufficient criterion。

### 强中间结果

- \(n=4,k=1\) 的局部 realization theorem；
- generic submersion / local openness；
- 新 differential obstruction；
- 特定 manifold class 上完整 characterization；
- 可拼接的局部到全局 theorem。

### 不算解决

- 随机 metric 样本的大量数值统计；
- 只证明某几个代表可实现；
- 任意 connection 的 representability；
- 忽略 Levi-Civita 约束。

---

# 17. 下一会话应直接从哪里开始

不要重新讨论“Yau 问题到底难不难”。

直接建立两个项目。

---

## Project A — Yau 23 / K3 Explicit Ricci-flat Metric

### 最高目标

在一个明确指定的 compact Kummer K3 上，将已知 Ricci-flat Kähler metric 的隐式 PDE 修正转化为新的精确、可压缩、可严格验证的解析表示；最终目标是达到足以合理称为 explicit metric 的标准。

### 第一裁决题

\[
\boxed{
u
\text{ 的高精度谱系数是否具有稳定的精确结构？}
}
\]

### 第一阶段输出

- 坐标/normalization 完整规范；
- Kummer approximate metric；
- 多尺度高精度 \(u\)；
- bulk/bubble/matching coefficient dataset；
- symmetry/selection rules；
- candidate exact patterns；
- negative results ledger。

---

## Project B — Yau 19 / \(p_1\) Local Realization

### 最高目标

理解四维中 Levi-Civita Pontryagin-form map

\[
\mathcal P_1:g\mapsto p_1(\nabla^g)
\]

的局部像，并据此建立局部 realization theorem 或发现新的 differential obstruction。

### 第一裁决题

\[
\boxed{
D\mathcal P_1|_g
\text{ 在 generic curved background 上的 principal symbol/局部像是什么？}
}
\]

### 第一阶段输出

- exact variation formula；
- gauge kernel；
- principal symbol；
- exact generic-rank certificate；
- image/cokernel representation decomposition；
- 局部 surjectivity yes/no；
- 下一步 nonlinear theorem 的精确前提。

---

# 18. 最终研究判断

如果目标是“让 Qiushi + LLM 真正取得原创数学突破”，最重要的不是一次性宣称解决 Yau 原题，而是选择一个问题，使系统能够形成：

\[
\boxed{
\text{发现}
\rightarrow
\text{证伪}
\rightarrow
\text{压缩}
\rightarrow
\text{exactify}
\rightarrow
\text{证明}
}
\]

的真实科学闭环。

在本会话讨论的 Yau 问题中：

\[
\boxed{
\text{Yau 23 显式 K3 分支}
}
\]

最适合作为第一旗舰。

\[
\boxed{
\text{Yau 19 的 4D }p_1\text{ realization/obstruction}
}
\]

最适合作为第二理论旗舰。

Yau 26 仍然重要，但它更像一个检验系统是否已经具备“发明新的全局几何机制”的长期问题，而不是当前最容易形成严格突破的目标。

真正值得追求的不是“让更多 Agent 思考更久”，而是：

\[
\boxed{
\text{把无限、模糊、不可搜索的开放问题}
\longrightarrow
\text{压缩成一个决定性的结构问题}
\longrightarrow
\text{持续攻击直到真伪闭合}
}
\]

这应当成为 Qiushi Engine 处理世界级数学问题的核心研究范式。

---

# 19. 关键文献与人物索引（供下一会话起步）

## 原始问题集
- Shing-Tung Yau, *Problem Section*, Seminar on Differential Geometry, Annals of Mathematics Studies 102, 1982.

## Yau 23 / K3 / Ricci-flat
- S.-T. Yau — Calabi conjecture / Ricci-flat Kähler existence.
- Gross–Wilson — collapsing K3 metrics.
- Donaldson — numerical / balanced Calabi–Yau metrics.
- Foscolo — hyperkähler gluing/collapse on K3.
- Hein–Sun–Viaclovsky–Zhang — degeneration/bubbling structures.
- Chen–Viaclovsky–Zhang — elliptic K3 collapsing Ricci-flat metrics.
- Thomas Jiang — modern analytic Kummer constructions.
- B. Shackleton (2026) — *A Calabi–Yau Metric on the Kummer Surface*.
- Numerical / machine-learning Calabi–Yau metric literature — 用于生成高精度 target，但不能代替 exact proof.

## Yau 19 / Chern–Weil representability
- S.-S. Chern — Chern–Weil curvature forms.
- Narasimhan–Ramanan — universal connections（注意：一般 connection 不等于 Levi-Civita）。
- Dennis DeTurck — local prescribed Ricci curvature，作为 curvature prescription 的比较模型。
- V. P. Pingali — Chern–Weil form representability in Hermitian/vector-bundle settings；不等于解决 Levi-Civita Pontryagin prescription.

## Yau 26 / Einstein stability
- Michael T. Anderson.
- Maung Min-Oo.
- Dale Skinner.
- Ursula Hamenstädt.
- Frieder Jäckel.
- Joel Fine.
- Bruno Premoselli.
- Jiang–Naber.
- Tian–Wang.
- Tristan Ozuch.
- Claude LeBrun.
- Olivier Biquard.
- Klaus Kröncke.
- Richard Bamler.
- Böhm–Wilking.
- Brendle–Schoen.

## Yau 29 / scalar curvature & aspherical geometry
- Schoen–Yau.
- Gromov–Lawson.
- Chodosh–Li.
- Gromov.
- minimal hypersurface / \(\mu\)-bubble / higher-index literature.

---

## 一句话交接

> **下一会话不要重新泛谈 Yau Problems。直接把 Yau 23 的 Kummer correction exactification 作为主线，把 Yau 19 的四维 \(p_1\) local image/obstruction 作为副线；所有研究都围绕“一个决定性关口 → 计算/反例/严格证明 → 真伪闭合”推进。**

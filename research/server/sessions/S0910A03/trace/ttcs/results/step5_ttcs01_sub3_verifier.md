# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step7_local_vs_global_rigidity.md",
    "Sessions/S0910A03/workspace/notes/step4_compactness_synthesis.tex",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md",
    "Knowledge/objects/papers/Orbifold-compactness-for-spaces-of-Riemannian-metrics-and-applications--30aa929b9159--a0e9497fbde6/object.md",
    "Sessions/S0910A03/staging/acquired/2609_01464__Removability_of_non-isolated_singularities_for_Eins_32e2d5864ee030ed/part_001.md"
  ]
}
```

## Task

Check the compactness extraction argument under only |Ric+g|_{L∞}->0 on noncollapsed four-dimensional balls. Using Cheeger–Naber harmonic-radius measure estimates, determine what positive-measure regular patches can be selected, what local convergence follows, whether uniform convergence of the Ricci defect is enough to bootstrap a C^{1,alpha}/W^{2,p} harmonic-chart limit to a smooth Einstein metric, and how an integral deficit O(delta^2) passes to that patch. Explicitly separate noncollapse at one ball, typical-point selection, curvature concentration, collapsing regions, and topology recovery. State exact missing assumptions if the argument fails.

## Output

# 科学核验备忘录：非塌缩四维球上的近 Einstein 紧致性提取

记
\[
\varepsilon_i:=\|\operatorname{Ric}_{g_i}+g_i\|_{L^\infty(g_i)}\longrightarrow0,
\qquad \operatorname{Vol}_{g_i}B_1(p_i)\ge v>0 .
\]
以下假定 \(M_i\) 闭，因而 Cheeger–Naber 的完备性假设自动满足。若只研究局部球，则需在一个更大球上拥有同样的 Ricci 控制，并把所有坐标估计放在严格缩小后的球上。

## 1. 单个非塌缩球确实给出正测度的固定尺度正则片

当 \(i\) 充分大时，
\[
|\operatorname{Ric}_{g_i}|\le 3,\qquad \operatorname{Ric}_{g_i}\ge-3g_i.
\]
Bishop–Gromov 比较由 \(\operatorname{Vol}B_1(p_i)\ge v\) 给出
\[
\operatorname{Vol}B_{1/2}(p_i)\ge b(v)>0.
\]

Cheeger–Naber Theorem 1.13 与 Remark 1.11 在四维给出
\[
\operatorname{Vol}\!\left(
T_r\{x\in B_1(p_i):r_h(x)\le r\}
\right)\le C(v)r^4.
\]
这里仅使用双边 Ricci 有界；Einstein 方程不是这一步的输入。

取固定的 \(\rho=\rho(v)>0\)，使
\[
C(v)(2\rho)^4<\frac12 b(v),\qquad \rho<\frac18,
\]
并定义
\[
\mathcal G_i=
B_{1/2}(p_i)\setminus
T_{2\rho}\{x\in B_1(p_i):r_h(x)\le2\rho\}.
\]
于是
\[
\operatorname{Vol}(\mathcal G_i)\ge \frac12b(v)>0.
\]
每个 \(x_i\in\mathcal G_i\) 都满足：

* \(r_h(x_i)>2\rho\)；
* 对所有 \(y\in B_\rho(x_i)\)，均有 \(r_h(y)>2\rho\)；
* \(B_\rho(x_i)\) 的体积有仅依赖 \(v,\rho\) 的正下界。

所以可选择的不只是一个正则点，而是一族正测度的中心；每个中心都承载固定尺度的谐和坐标片。该结论不表示 \(B_1(p_i)\) 上处处都有统一谐和半径。

## 2. 谐和坐标中的正确局部收敛

选 \(x_i\in\mathcal G_i\)，令
\[
\Phi_i:B_{2\rho}(0)\longrightarrow M_i
\]
为谐和坐标，并记
\[
\widetilde g_i=\Phi_i^*g_i.
\]
由 harmonic radius 的定义及有界 Ricci 的椭圆正则性，对任意有限 \(p\) 和任意 \(\alpha<1\)，在缩小后的欧氏球上有
\[
\|\widetilde g_i\|_{C^{1,\alpha}}
+\|\widetilde g_i\|_{W^{2,p}}\le C(v,\rho,p,\alpha).
\]
因而可取子列，使得对 \(\beta<\alpha\)
\[
\widetilde g_i\to g_\infty
\quad\text{强收敛于 }C^{1,\beta},
\qquad
\widetilde g_i\rightharpoonup g_\infty
\quad\text{弱收敛于 }W^{2,p}.
\]

在谐和坐标中，
\[
(\operatorname{Ric}_{g_i})_{\mu\nu}
=-\frac12 \widetilde g_i^{ab}
\partial_a\partial_b(\widetilde g_i)_{\mu\nu}
+Q_{\mu\nu}(\widetilde g_i,\partial\widetilde g_i).
\]
写
\[
e_i:=\operatorname{Ric}_{g_i}+g_i,
\qquad \|e_i\|_{L^\infty}\to0.
\]
强 \(C^{1,\beta}\) 收敛使 \(Q(\widetilde g_i,\partial\widetilde g_i)\) 强收敛；二阶导数的弱收敛则足以把方程传到极限，得到分布意义下
\[
\operatorname{Ric}_{g_\infty}=-g_\infty.
\]
极限方程本身是谐和坐标中的一致椭圆拟线性系统。由于
\(g_\infty\in C^{1,\beta}\cap W^{2,p}\)，对极限方程应用 Schauder 正则性并迭代可得
\[
g_\infty\in C^\infty,\qquad \operatorname{Ric}_{g_\infty}=-g_\infty.
\]

因此，\(L^\infty\) Ricci defect 趋零足以产生光滑的局部 Einstein 极限。

### 需要修正的 Schauder 步骤

由
\[
\|e_i\|_{L^\infty}\to0
\]
不能推出 \(e_i\to0\) 于 \(C^\alpha\)；其振荡频率可能增长。因此，原笔记中“方程右端在 \(C^\alpha\) 收敛，所以直接得到 \(C^{2,\alpha}\) 收敛”这一行没有相应估计支撑。

正确结果是：

1. 先以弱 \(W^{2,p}\) 收敛得到 Einstein 极限；
2. 先证明极限光滑；
3. 再对 \(w_i=\widetilde g_i-g_\infty\) 使用内点 \(W^{2,p}\) 估计。

事实上，在更小球上，
\[
L_iw_i=
(\widetilde g_\infty^{ab}-\widetilde g_i^{ab})
\partial_{ab}g_\infty
+2w_i-2e_i
+\bigl(P(\widetilde g_i,\partial\widetilde g_i)
-P(g_\infty,\partial g_\infty)\bigr),
\]
右端强趋于零于每个有限 \(L^p\)。于是
\[
\widetilde g_i\to g_\infty
\quad\text{强收敛于 }W^{2,p}_{\mathrm{loc}}
\quad\text{对所有有限 }p.
\]
相应地，
\[
\operatorname{Rm}_{g_i}\to\operatorname{Rm}_{g_\infty}
\quad\text{强收敛于 }L^p_{\mathrm{loc}}.
\]
但仅由 \(L^\infty\) Ricci defect 不能得到度量序列的 \(C^{2,\alpha}\) 或光滑收敛；这类结论需要 defect 的 Hölder 或更高导数控制，或者每个 \(g_i\) 已满足精确的 Einstein 方程。

## 3. 积分 deficit 如何传到正则片

设正则片 \(U_i\subset B_\rho(x_i)\) 上有
\[
\int_{U_i}|\Psi(g_i,\operatorname{Rm}_{g_i})|^2\,dV_{g_i}
\le C\varepsilon_i^2,
\]
其中 \(\Psi\) 是度量和曲率的连续代数表达式。强 \(W^{2,p}\) 收敛给出曲率的强 \(L^p\) 收敛；取 \(p\ge2\) 后，
\[
\Psi(g_i,\operatorname{Rm}_{g_i})
\longrightarrow
\Psi(g_\infty,\operatorname{Rm}_{g_\infty})
\quad\text{于 }L^2_{\mathrm{loc}}.
\]
因此
\[
\Psi(g_\infty,\operatorname{Rm}_{g_\infty})=0
\quad\text{几乎处处}.
\]
极限度量光滑，所以该恒等式实际上处处成立。

例如，若固定了取向并且谐和坐标保持取向，
\[
\int_{U_i}
\bigl(s_i+8\sqrt6\,|W_i^+|\bigr)^2\,dV_{g_i}\to0,
\]
则
\[
s_\infty+8\sqrt6\,|W_\infty^+|=0.
\]
由 \(\operatorname{Ric}_{g_\infty}=-g_\infty\) 得 \(s_\infty=-4\)，故
\[
|W_\infty^+|=\frac1{2\sqrt6}
\]
在整个极限片上成立。这里不需要 \(W_i^+\) 的 \(C^0\) 收敛；强 \(L^2\) 收敛和极限光滑性已经足够。

若 deficit 含有 \(\nabla W\) 或更高导数，仅有上述度量紧致性还不能传递它，因为这需要三阶或更高阶度量控制。

另外，固定 \(|W_\infty^+|\) 并不推出 \(W_\infty^+\) 只有两个特征值。对 \(\Lambda^+\) 上的无迹对称算子，三特征值都不同仍可具有同一固定范数。二重特征值还需一个额外代数等号，例如控制
\[
\frac1{\sqrt6}|W^+|^3-
\bigl|\operatorname{tr}(W^+)^3\bigr|
\]
趋于零；该等号情形才对应两个特征值。

## 4. 局部 deficit 与全局归一化 deficit 是两种不同输入

### 4.1 已知非塌缩球上的局部积分趋零

若已经有
\[
\int_{B_1(p_i)}\mathfrak d_i\,dV_{g_i}\to0,
\qquad \mathfrak d_i\ge0,
\]
那么任意上述正则片 \(U_i\subset B_1(p_i)\) 都满足
\[
\int_{U_i}\mathfrak d_i\to0.
\]
此时正则片的选择与 deficit 的选择无需再次协调。

### 4.2 只有全局归一化积分

若仅有
\[
\frac1{\operatorname{Vol}(M_i)}
\int_{M_i}\mathfrak d_i\,dV_{g_i}
=O(\varepsilon_i^2),
\]
则对均匀随机点 \(p\in M_i\)，Fubini 给出
\[
\mathbb E_p\!\left[\int_{B_R(p)}\mathfrak d_i\,dV\right]
=
\frac1{\operatorname{Vol}(M_i)}
\int_{M_i}\mathfrak d_i(x)\,
\operatorname{Vol}(B_R(x))\,dV(x).
\]
Ricci 下界给出固定 \(R\) 时
\[
\operatorname{Vol}(B_R(x))\le C(R),
\]
故
\[
\mathbb E_p\!\left[\int_{B_R(p)}\mathfrak d_i\right]
=O(\varepsilon_i^2).
\]
这确实选出局部 deficit 很小的典型球，但典型点可能位于塌缩区。

若定义
\[
A_i(v)=\{p:\operatorname{Vol}B_1(p)\ge v\}
\]
并且另有
\[
\operatorname{Vol}A_i(v)\ge\tau\,\operatorname{Vol}(M_i)
\]
，其中 \(\tau>0\) 固定，则
\[
\frac1{\operatorname{Vol}A_i(v)}
\int_{A_i(v)}
\left(\int_{B_R(p)}\mathfrak d_i\right)dV(p)
\le C(R)\tau^{-1}O(\varepsilon_i^2).
\]
于是可同时选到：

* \(B_1(p_i)\) 非塌缩；
* \(\int_{B_R(p_i)}\mathfrak d_i=O(\varepsilon_i^2)\)。

再在此球内应用 Cheeger–Naber，即得到同时具有固定谐和尺度和小 deficit 的片。

仅知道一个非塌缩球，而 \(\operatorname{Vol}(M_i)\to\infty\) 时，全局归一化积分不能控制该指定球。若另有
\[
\operatorname{Vol}(M_i)\le V<\infty,
\]
则一个非塌缩内球已经占有固定体积比例，上述联合选择成立。更强地，归一化 \(O(\varepsilon_i^2)\) 此时直接给出全局未归一化积分 \(O(\varepsilon_i^2)\)。

## 5. 曲率集中与塌缩必须分开

### 5.1 曲率集中

Cheeger–Naber 还给出局部
\[
\fint_{B_1(p_i)}|\operatorname{Rm}_{g_i}|^2\le C(v),
\]
但这允许 \(L^2\) 曲率集中在半径趋零的区域。弱 \(r_h\) 估计只说明这类区域的管状体积为 \(O(r^4)\)，并不产生
\[
\inf_{B_{3/4}(p_i)}r_h>0.
\]

因此：

* 可以提取避开集中点的光滑 Einstein 片；
* 不能由此得到整个 \(B_1(p_i)\) 的光滑收敛；
* 四维极限仍可出现孤立 orbifold 点及 ALE bubbles；
* 只控制 \(W^+\) 的 deficit 时，\(W^-\) 仍可集中并携带 Chern–Gauss–Bonnet 能量。

要得到整球光滑收敛，需要例如
\[
\inf_{B_{3/4}(p_i)}r_h\ge r_0>0,
\]
或者一个逐球的小曲率输入，使每个潜在集中球都进入 \(\varepsilon\)-正则性结论。

### 5.2 塌缩区域

单个非塌缩球会向任意固定距离传播非塌缩。若
\(d(x,p_i)\le R\)，则
\[
B_1(p_i)\subset B_{R+1}(x),
\]
结合 Bishop–Gromov 得
\[
\operatorname{Vol}B_1(x)\ge c(v,R)>0.
\]
所以在以 \(p_i\) 为中心的任意固定 \(R\)-球内，不会发生单位尺度塌缩。

但 \(c(v,R)\) 随 \(R\) 退化；若直径趋于无穷，塌缩区可向无穷远移动。双曲曲面乘积的退化度量提供了直接模型：
\[
\operatorname{Ric}_{h_i\oplus k}=-(h_i\oplus k),
\]
厚部存在非塌缩球，而短闭测地线附近单位球体积趋零。故精确 Einstein 方程本身也不能把单球非塌缩提升为全流形非塌缩。

该乘积模型的 \(W^+\) 范数与校准值不同，因而可被特定 Weyl profile 排除；但这只排除了这一模型，并没有给出一般塌缩结构与该 profile 不相容的定理。

## 6. 局部 Einstein 片不恢复原流形拓扑

谐和坐标提取产生的是一个开球上的 Einstein 度量，或者在对半径作对角提取后得到一个可能非紧的正则部分。它没有提供：

* 原 \(M_i\) 上的全局 Einstein 度量；
* 极限与 \(M_i\) 的全局微分同胚；
* 逃向远处的薄部；
* 集中点处的 bubbles 及其同调信息。

即使所有 \(M_i\) 是同一个光滑流形，拓扑仍可储存在越来越细的颈区和 bubble 中，而正则片只看到局部欧氏拓扑。

要得到同一流形上的全局光滑 Einstein 极限，通常需同时拥有：

1. 全流形逐点单位球体积下界；
2. 直径上界，或等价的统一有限坐标覆盖输入；
3. 全流形谐和半径正下界，或排除所有曲率集中点；
4. 坐标拼接给出的全局微分同胚。

若允许 orbifold 极限，则还需逐个处理 orbifold 点并记录 bubble-tree 的颈部粘接。所给 2026 年 removability 定理也不能自动消去 Cheeger–Naber 的 orbifold 点：该定理预设奇异集外的 Einstein 度量已作为一个闭拓扑流形上的 \(L^\infty\) 度量延拓；一般的圆锥 \(C(S^3/\Gamma)\) 并不自动提供这种流形结构。

## 7. 核验后的精确结论

目前材料严格支持
\[
\boxed{
\begin{aligned}
&\text{一个非塌缩四维球}
+\|\operatorname{Ric}+g\|_{L^\infty}\to0\\
&\quad\Longrightarrow
\text{正测度的一族固定尺度谐和片}\\
&\quad\Longrightarrow
\text{子列在片上收敛到光滑 }\operatorname{Ric}=-g\text{ 度量}.
\end{aligned}}
\]

若该球邻域上的代数曲率 deficit 积分趋零，则相应等号传到极限片。这里正确的收敛工具是先取得光滑极限，再获得强 \(W^{2,p}\) 与强 \(L^p\) 曲率收敛，而不是直接使用 \(C^{2,\alpha}\) Schauder 收敛。

从这一局部结论到全流形 Einstein 度量之间仍缺少全局非塌缩、直径或有限覆盖控制、曲率集中点的消除，以及全局拓扑识别。全局归一化 deficit 与单个非塌缩球同时使用时，还需总量上界、非塌缩点的正体积比例，或该指定球上的局部 deficit 估计。
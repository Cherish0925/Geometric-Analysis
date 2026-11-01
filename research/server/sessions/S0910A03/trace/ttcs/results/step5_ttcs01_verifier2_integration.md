# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 5,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step5_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step5_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the compactness extraction argument under only |Ric+g|_{L∞}->0 on noncollapsed four-dimensional balls. Using Cheeger–Naber harmonic-radius measure estimates, determine what positive-measure regular patches can be selected, what local convergence follows, whether uniform convergence of the Ricci defect is enough to bootstrap a C^{1,alpha}/W^{2,p} harmonic-chart limit to a smooth Einstein metric, and how an integral deficit O(delta^2) passes to that patch. Explicitly separate noncollapse at one ball, typical-point selection, curvature concentration, collapsing regions, and topology recovery. State exact missing assumptions if the argument fails.

## Integrated Scientific Memo

# 核验结论：单个非塌缩四维球只能给出局部正则 Einstein 片

设
\[
\varepsilon_i:=\|\Ric_{g_i}+g_i\|_{L^\infty}\to0,
\qquad \Vol_{g_i}B_1(p_i)\ge v>0 .
\]
为避免边界问题，若 \(M_i\) 不完备，应假设同样的 Ricci 控制成立于更大的相对紧球上，并只在严格缩小的内球提取。以下所有结论均为局部结论。

## 1. Cheeger–Naber 实际允许选择什么正则片

充分大时 \(|\Ric_{g_i}|\le3\)。Cheeger–Naber Theorem 1.13 与 Remark 1.11 在四维给出
\[
\Vol\!\left(
T_r\{x\in B_1(p_i):r_h(x)\le r\}
\right)\le C(v)r^4 .
\]
这里只控制**谐和半径**，不是曲率正则尺度；把 \(r_h\) 换成 \(r_x\) 需要精确 Einstein 方程或 \(\nabla\Ric\) 控制。

由 Bishop–Gromov，
\[
\Vol B_{1/2}(p_i)\ge b(v)>0.
\]
选固定 \(\rho=\rho(v)<1/8\)，使
\[
C(v)(2\rho)^4<\tfrac12 b(v),
\]
并令
\[
G_i:=B_{1/2}(p_i)\setminus
T_{2\rho}\{r_h\le2\rho\}.
\]
则
\[
\Vol(G_i)\ge \tfrac12b(v)>0.
\]
对任意 \(x_i\in G_i\)，有 \(r_h(x_i)>2\rho\)，且
\[
y\in B_\rho(x_i)\Longrightarrow r_h(y)>2\rho.
\]
因此可选择的是一族具有统一正体积、统一谐和尺度的局部正则片；并不能推出整个 \(B_1(p_i)\) 上谐和半径一致有下界。

## 2. 正确的局部收敛与 bootstrap

在这些片的谐和坐标中，对每个有限 \(p\) 及 \(\alpha<1\)，
\[
\|g_i\|_{C^{1,\alpha}}+\|g_i\|_{W^{2,p}}\le C(v,\rho,p,\alpha).
\]
缩小定义域并取子列后，
\[
g_i\to g_\infty\quad\text{强于 }C^{1,\beta},
\qquad
g_i\rightharpoonup g_\infty\quad\text{弱于 }W^{2,p},
\]
其中 \(\beta<\alpha\)。

谐和坐标方程为
\[
\Ric_{ij}(g_i)
=-\frac12g_i^{ab}\partial_a\partial_b(g_i)_{ij}
+Q_{ij}(g_i,\partial g_i),
\]
亦即令 \(E_i=\Ric(g_i)+g_i\)，
\[
-\frac12g_i^{ab}\partial_a\partial_b(g_i)_{ij}
=-g_{i,ij}-Q_{ij}(g_i,\partial g_i)+E_{i,ij}.
\]
由 \(E_i\to0\) 于 \(L^\infty\)、\(C^{1,\beta}\) 强收敛及 \(W^{2,p}\) 弱收敛，可将方程传到极限：
\[
\Ric(g_\infty)=-g_\infty
\]
在分布意义成立。对这个无 defect 的极限方程应用椭圆正则性，得到
\[
g_\infty\in C^\infty,\qquad \Ric(g_\infty)=-g_\infty.
\]

### 必须修正的错误

仅由 \(E_i\to0\) 于 \(L^\infty\) 不能推出 \(E_i\to0\) 于 \(C^\alpha\)，故不能直接声称右端在 \(C^\alpha\) 收敛，也不能直接得到 \(g_i\to g_\infty\) 于 \(C^{2,\alpha}\) 或光滑收敛。

在先证明极限光滑后，对 \(w_i=g_i-g_\infty\) 使用内点 \(W^{2,p}\) 估计，可得到
\[
g_i\to g_\infty\quad\text{强于 }W^{2,p}_{\mathrm{loc}}
\quad(\forall p<\infty),
\]
从而
\[
\Rm(g_i)\to\Rm(g_\infty)
\quad\text{强于 }L^p_{\mathrm{loc}}.
\]
这足以传递代数曲率 deficit，但仍不蕴含序列的 \(C^{2,\alpha}\) 收敛。

## 3. \(O(\delta^2)\) deficit 如何传到片上

须区分三个层次。

### 指定非塌缩球上的局部 deficit

若非负密度 \(\mathfrak d_i\) 已满足
\[
\int_{B_1(p_i)}\mathfrak d_i\,dV_{g_i}=O(\varepsilon_i^2),
\]
则任意上述正则片 \(U_i\subset B_1(p_i)\) 自动满足同一上界。

若
\[
\mathfrak d_i=|\Psi(g_i,\Rm(g_i))|^2
\]
且 \(\Psi\) 是度量与曲率的连续代数表达式，则强 \(W^{2,p}\) 收敛（取 \(p\ge2\)）给出
\[
\Psi(g_i,\Rm(g_i))\to\Psi(g_\infty,\Rm(g_\infty))
\quad\text{于 }L^2_{\rm loc}.
\]
因此 \(\Psi(g_\infty,\Rm(g_\infty))=0\) 几乎处处；由极限光滑性，等式处处成立。

例如若
\[
\int_{U_i}(s_i+8\sqrt6\,|W_i^+|)^2\,dV_{g_i}\to0,
\]
并固定一致取向，则
\[
s_\infty+8\sqrt6\,|W_\infty^+|=0.
\]
由于 \(\Ric(g_\infty)=-g_\infty\)，有 \(s_\infty=-4\)，故
\[
|W_\infty^+|=\frac1{2\sqrt6}.
\]
这里不需要 \(W_i^+\) 的一致收敛。

若 deficit 涉及 \(\nabla W\) 或更高导数，上述紧致性不足以传递它。

此外，固定 \(|W_\infty^+|\) **不**蕴含 \(W_\infty^+\) 有二重特征值；还需例如 \(\tr((W^+)^3)\) 的尖锐代数等号。

### 只有全局总积分

若
\[
\int_{M_i}\mathfrak d_i=O(\varepsilon_i^2),
\]
则它当然控制任何指定局部片。

### 只有全局归一化积分

若仅有
\[
\frac1{\Vol(M_i)}\int_{M_i}\mathfrak d_i
=O(\varepsilon_i^2),
\]
则体积随机基点满足
\[
\mathbb E_p\!\left[\int_{B_R(p)}\mathfrak d_i\right]
=
\frac1{\Vol(M_i)}
\int_{M_i}\mathfrak d_i(x)\Vol(B_R(x))\,dV(x)
=O(\varepsilon_i^2),
\]
其中使用 Ricci 下界给出的 \(\Vol(B_R(x))\le C(R)\)。这只能选出**体积典型的小 deficit 球**，不能保证它非塌缩。

要同时选择非塌缩且小 deficit 的球，至少需要下列之一：

* 指定非塌缩球本身有局部 deficit 控制；
* 非塌缩点集占固定体积比例：
  \[
  \Vol\{p:\Vol B_1(p)\ge v\}\ge\tau\Vol(M_i);
  \]
* 或总量上界 \(\Vol(M_i)\le V\)，使一个固定体积的非塌缩内球占有统一正比例。

单个非塌缩球加上归一化全局 deficit，在 \(\Vol(M_i)\to\infty\) 时不足以控制该球。

还须注意：由 \(\|\Ric+g\|_\infty\le\varepsilon_i\) 自动得到的 \(O(\varepsilon_i^2)\) 仅包括
\[
|E_i|^2,\qquad (s_i+4)^2.
\]
任何 \(W^+\) deficit 的小量性均需额外的 Chern–Weil、LeBrun 或近等号输入，不能由 Ricci defect 推出。

## 4. 曲率集中不等于塌缩

### 曲率集中

在一个非塌缩球上，Cheeger–Naber 给出四维局部 \(L^2\) 曲率控制及坏谐和半径集合的弱型估计，但允许能量集中于半径趋零的区域。因此可以提取避开集中集合的光滑 Einstein 片，却不能推出整球光滑收敛。

四维非塌缩极限可有孤立 orbifold 点及 Ricci-flat ALE bubbles。特别地，只控制 \(W^+\) deficit 时，\(W^-\) 仍可集中并携带拓扑能量。要消除这些点，需额外的逐球小曲率/能量隙条件，或直接假设统一谐和半径下界。

Antonelli–Székelyhidi 的可去奇点定理不能自动消去一般 orbifold 锥点：它预设 Einstein 度量已作为闭光滑流形上的 \(L^\infty\) 度量延拓；\(\mathbb R^4/\Gamma\) 的非平凡锥点通常不满足此前提。

### 塌缩区域

由一个非塌缩球和 Ricci 下界，对任意固定 \(R\)，可将非塌缩传播到 \(B_R(p_i)\)：
\[
d(x,p_i)\le R\Longrightarrow \Vol B_1(x)\ge c(v,R)>0.
\]
但 \(c(v,R)\) 随 \(R\) 退化；当直径无界时，塌缩区可逃向无穷远。

退化双曲曲面乘积满足精确 \(\Ric=-g\)，厚部有非塌缩球，而短测地线附近塌缩。因此单球非塌缩和精确 Einstein 方程都不能推出全流形非塌缩。特定 Weyl profile 可排除这一具体模型的宏观主体，但没有给出排除所有塌缩模型的一般定理。

## 5. 拓扑恢复完全未由局部提取解决

局部谐和坐标极限只产生一个开集上的光滑 Einstein 度量。它不提供：

* \(M_i\) 上的全局 Einstein 度量；
* 极限与原流形的全局微分同胚；
* 薄部、颈区和逃向无穷远的区域；
* orbifold 点及 ALE bubble 所携带的同调信息。

在负 Einstein 常数情形没有 Myers 直径上界。若要从局部片恢复整个固定流形，至少还需：

1. 全流形统一单位球非塌缩；
2. 直径上界或统一有限坐标覆盖；
3. 排除所有曲率集中点，或完整控制 orbifold/bubble tree；
4. 全局坐标拼接及微分同胚识别。

即使局部极限满足额外 Weyl 等号，所得 pointed limit 通常非紧；依赖 Stokes 的紧致 Derdziński/共形 Kähler 矛盾不能在该局部极限上执行。

## 最终判定

严格成立的是
\[
\boxed{
\begin{aligned}
&\Vol B_1(p_i)\ge v,\quad
\|\Ric_{g_i}+g_i\|_{L^\infty}\to0\\
&\Longrightarrow
\text{在 }B_1(p_i)\text{ 中存在正测度、固定谐和尺度的正则片}\\
&\Longrightarrow
\text{子列在这些片上以 }C^{1,\alpha}
\text{ 及强 }W^{2,p}_{\rm loc}\text{ 收敛}\\
&\Longrightarrow
\text{光滑局部极限满足 }\Ric(g_\infty)=-g_\infty.
\end{aligned}}
\]

局部代数曲率 deficit 若在所选球上趋零，则传到极限片。仅有全局归一化 deficit 时，还需非塌缩点的固定体积比例、总量上界或指定球局部控制。该论证不能排除曲率集中、远处塌缩或 topology loss，也不能据此构造原流形上的全局 Einstein 度量。
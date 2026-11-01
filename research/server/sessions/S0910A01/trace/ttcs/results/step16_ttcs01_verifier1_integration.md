# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 16,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step16_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step16_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the corrected smoothing-route files and assess the transition-inclusive cutoff-flow stability problem as mathematics. The goal is not final approval; determine whether the proposed weighted energy route can plausibly yield, on a support of radius comparable to the Li scale, (i) persistence of local normalized L2 curvature energy and interior |Rm|<=C/t, and (ii) global or support-summed Einstein-defect control Q(t0)/A->0 for the near-Einstein LeBrun critical sequence. Explicitly account for Ricci flow having no finite propagation speed, for Li's supremum/covering quantifiers, for cutoff transition terms in the E equation, for the difference between pointwise E control and the weaker normalized L2 target, and for what existing Li/Yang/Wang statements actually supply. Give a direct scientific memo: viable proof skeleton, obstruction terms, exact hypotheses still needed, and whether any part of Step 15's completed-chain wording survives after Step 16.

## Integrated Scientific Memo

# 科学复核备忘录：含过渡区的 cutoff-flow 稳定性

## 结论

把每个活动支撑取成 Li 尺度 \(r_*\) 的固定倍数后，weighted-energy 路线在四维的尺度与符号上是相容的，因而**值得继续**；但现有 Li、Yang、Wang 结果均不能直接闭合它。

当前应区分两个层次：

1. **条件于支撑上的曲率能量持续小，Einstein 缺陷的归一化 \(L^2\) 控制很可能可闭合。**  
   过渡项在积分后保持齐次于 \(E=\operatorname{Ric}+g\)，临界曲率势项可由四维 Sobolev–能量消去吸收。这应给出
   \[
   Q_i(t_0):=\int_{M_i}|E_i(t_0)|^2\le C Q_i(0),
   \qquad \frac{Q_i(t_0)}{A_i}\to0.
   \]
   这一目标不需要在过渡环证明逐点 \(|E|=O(\delta_i)\)。

2. **真正未证的是支撑整体上的曲率 bootstrap。**  
   必须证明 cutoff 过渡项参与的、坍缩一致的局部归一化 \(L^2\) 曲率能量保持，并排除能量在流中重新集中；然后才能在内平台推出
   \[
   |\operatorname{Rm}(t)|\le C(t^{-1}+r_*^{-2})\le C_\theta/t.
   \]
   单纯控制整个支撑的总曲率能量并不足以保证每个 \(r_*\)-球仍低于临界吸收阈值。

因此 Step 15 的“完整链条”结论不成立；保留下来的是若干可靠组件和一个条件性证明架构。

---

## 1. 先修复静态尺度与量词

应统一采用固定比例的嵌套区域，例如
\[
B_{4r}(p_j)\subset B_{8r}(p_j)\subset
\{\chi_j=1\}\cup\text{buffer}
\subset\operatorname{supp}\chi_j\subset B_{16r}(p_j),
\qquad r=r_*.
\]
选取支撑彼此不交或至少有统一有界重叠，并令
\[
|d\chi_j|\le Cr^{-1}.
\]

若
\[
\mathcal M_{R_0}(|\operatorname{Rm}|^2)(p_j)\le K_0,
\qquad (L+1)r\le R_0,
\]
则任意 \(y\in B_{Lr}(p_j)\) 满足
\[
\int_{B_r(y)}|\operatorname{Rm}|^2
 \le K_0\,\operatorname{Vol}(B_{(L+1)r}(p_j)).
\]
利用球包含与 Ricci 下界下的 Bishop–Gromov 比较，
\[
r^4\fint_{B_r(y)}|\operatorname{Rm}|^2
\le C(L)K_0r^4.
\]
取固定小 \(r\) 即得到整个支撑所需中心的初始 Li 小量。这修复了 Step 15 中 \(r_*\ll\rho\) 时从一个好点错误推至整个宏观 \(B_{\rho/4}\) 的问题。

Vitali 选择仍可使内平台占总体积的固定比例，因为所有半径现在都是 \(r\) 的固定倍数。

---

## 2. 不存在有限传播；平台上的方程相同并不意味着解局部独立

在 \(\{\chi=1\}\) 上，
\[
\partial_tg=-2(\operatorname{Ric}+g)
\]
确实是标准归一化 Ricci flow 的局部微分方程，但抛物方程在任意正时间即受外部影响。冻结 \(\{\chi=0\}\) 只意味着该处度量不动，并不使过渡环对平台不可见。

Li 的 Theorem 3.4 明确采用
\[
e_0(t)=\sup_{x\in M}
\left(\int_{B_r(x)}f^2\right)^{1/2}
\]
的全中心 supremum。估计一个 \(B_r(x)\) 时，需要以邻近中心覆盖 \(B_{2r}(x)\)。若 supremum 仅取内平台，邻近中心会落入更外层；反复加 buffer 最终必到达过渡环。这不是有限加几层即可消除的技术细节，而是量词不闭合以及抛物无限传播的具体表现。

因此正确对象不是“把 Li 的全局证明限制到平台”，而是**直接在整个活动支撑上保留 cutoff 权重与过渡项的能量定理**。

---

## 3. 曲率部分：可行骨架与核心障碍

设
\[
a=\chi_j^2,\qquad
F_j(t)=\int \zeta_j^2|\operatorname{Rm}|^2\,d\mu_t,
\]
其中 \(\zeta_j\) 是独立的外层测试 cutoff。相对 Sobolev 不等式为
\[
\|u\|_4^2\le
S_j\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\qquad
S_j\lesssim
\frac{r^2}{\operatorname{Vol}(B_{16r}(p_j))^{1/2}}.
\]
初始时
\[
S_jF_j(0)^{1/2}\lesssim r^2K_0^{1/2}.
\]
这是四维坍缩消去：体积因子完全抵消。

### 所需曲率能量不等式

归一化 cutoff flow 的曲率变分含有
\[
a\Delta\operatorname{Rm},\quad
a\,\operatorname{Rm}*\operatorname{Rm},\quad
da*\nabla E,\quad
\nabla^2a*E
\]
及低阶归一化项。所需的是把 Hessian-cutoff 项全部分部积分，得到类似
\[
\begin{aligned}
\frac d{dt}F_j
+c\int\zeta_j^2a|\nabla\operatorname{Rm}|^2
\le {}&
Cr^{-2}(F_j+q_j)\\
&+C\int\zeta_j^2a|\operatorname{Rm}|^3,
\end{aligned}
\tag{3.1}
\]
其中
\[
q_j(t)=\int\zeta_j^2|E|^2.
\]
在只有 Ricci 控制的初始数据下，不能默认存在统一
\(\|\nabla^2\chi\|_\infty\lesssim r^{-2}\)；故 (3.1) 必须只依赖一阶 cutoff 控制，不能把 Hessian 项粗略逐点估计。

临界三次项可按
\[
\begin{aligned}
\int\zeta_j^2a|\operatorname{Rm}|^3
&\le F_{j,\mathrm{loc}}^{1/2}
  \|\zeta_j\chi_j\operatorname{Rm}\|_4^2\\
&\le S_jF_{j,\mathrm{loc}}^{1/2}
\left[
C\int\zeta_j^2a|\nabla\operatorname{Rm}|^2
+Cr^{-2}F_j
\right]
\end{aligned}
\]
吸收，只要每个相关局部球在动态中仍满足
\[
S_{j,y}
\|\operatorname{Rm}\|_{L^2(B_r(y),t)}
\le\varepsilon_0.
\tag{3.2}
\]

### 真正障碍：总能量保持不等于局部无集中

Wang 的模型不等式
\[
\frac d{dt}\int|\operatorname{Rm}|^2+
c\int|\nabla(\chi|\operatorname{Rm}|)|^2
\le C|d\chi|_\infty^2\int|\operatorname{Rm}|^2
\]
说明过渡区可通过 weighted energy 而非有限传播处理。然而它主要控制活动域总能量。即使
\[
F_j(t)\le C F_j(0),
\]
能量仍可能集中到某个 \(r\)-球，使 (3.2) 失效。因此仅有 (3.1) 的粗略总支撑版本尚不足以推出局部 persistence。

需要额外构造以下之一：

- 带边缘衰减的局部能量 supremum，例如
  \[
  \sup_y w(y)^2\int_{B_r(y)}|\operatorname{Rm}|^2,
  \]
  其中 \(w\) 向支撑边缘消失，并证明邻球覆盖、过渡项与临界吸收都在该权重下闭合；或
- 一套支撑覆盖上的耦合局部能量系统，证明其演化矩阵有统一可控的有界重叠结构，并阻止局部集中。

第一种设想结构上合理，但应注意：若取 \(w=\chi^k\)，\(|dw|/w\) 可能在 \(\chi\to0\) 时奇异；必须在积分结构中证明只有诸如
\[
|da|^2/a=4|d\chi|^2
\]
这样的非奇异组合出现。此处尚无现成证明。

一旦 (3.2) 的动态版本成立，内平台上可用 Li 的临界 Moser 机制，得到
\[
|\operatorname{Rm}|(x,t)
\le C(t^{-1}+r^{-2}),
\qquad x\in B_{4r}(p_j),\quad
0<t\le\theta r^2.
\]

---

## 4. Einstein 缺陷 \(L^2\) 控制：条件性闭合较强

对
\[
E=\operatorname{Ric}+g,\qquad a=\chi^2,
\]
A03 的计算给出
\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E),
\]
其中 \(\mathcal C_a(E)\) 每项均含 \(E,\nabla E\) 或其迹。因此 \(E=0\) 时无过渡区加性源。

积分后，
\[
\begin{aligned}
\frac d{dt}q_j+
c\int\zeta_j^2a|\nabla E|^2
\le{}&
Cr^{-2}q_j\\
&+C\int\zeta_j^2a|\operatorname{Rm}|\,|E|^2.
\end{aligned}
\tag{4.1}
\]
这里 \(\nabla^2a\) 已分部积分消去，并利用
\[
|da|^2/a=4|d\chi|^2.
\]

若曲率 persistence 提供局部小量 (3.2)，则
\[
\begin{aligned}
\int\zeta_j^2a|\operatorname{Rm}|\,|E|^2
&\le
\|\operatorname{Rm}\|_{L^2(\mathrm{relevant\ ball})}
\|\zeta_j\chi_jE\|_4^2\\
&\le
\varepsilon_0
\left[
C\int\zeta_j^2a|\nabla E|^2
+Cr^{-2}q_j
\right].
\end{aligned}
\]
吸收后
\[
q_j'(t)\le Cr^{-2}q_j(t),
\qquad
q_j(t)\le e^{Ct/r^2}q_j(0).
\tag{4.2}
\]

初始逐点近 Einstein 条件给出
\[
q_j(0)\le
\delta_i^2\operatorname{Vol}(\operatorname{supp}\zeta_j).
\]
对不交或有界重叠的支撑求和，并加上完全冻结的外部，得到
\[
Q_i(t_0)\le
C\delta_i^2\operatorname{Vol}(M_i,g_i)
\]
（还需流中度量/体积统一可比）。在 LeBrun 临界序列
\(\operatorname{Vol}(M_i)/A_i=O(1)\) 下，
\[
\boxed{\frac{Q_i(t_0)}{A_i}\to0.}
\]
并且
\[
\mathring{\operatorname{Ric}}=E^\circ,\qquad
J_i(t_0)
=\frac1{8\pi^2}\int|\mathring{\operatorname{Ric}}|^2
\le\frac{Q_i(t_0)}{8\pi^2},
\]
故 \(J_i(t_0)/A_i\to0\)。这正足以在终端闭流形度量上重做 Chern–Weil/Seiberg–Witten 标定，无需沿流输运 \(W^+\)。

---

## 5. 逐点 \(E\) 与归一化 \(L^2\) 目标不可混同

Li Corollary 3.5 在普通 Ricci flow 的完整动态包成立时，可导出
\[
|E(x,t)|
\lesssim
\delta_i\left(\frac{r^2}{t}\right)^{2/3}
\]
以及可积的时间奇性。但这不能直接用于过渡环：

- cutoff 方程含退化主系数 \(a=\chi^2\)；
- 还含 \(d\chi\)-耦合项；
- Corollary 3.5 印刷中的未定义 \(\phi^2\) 与其调用的 Theorem 2.5 不一致，最合理的 source reading 是它服务于普通热方程，而不是一个已证明的 cutoff-transition Moser 定理。

因此该推论最多可在已经控制好的 \(\chi=1\) 内区使用，不能据此宣称全局逐点
\(|E|=O(\delta_i)\)。

对拓扑重标定，较弱的 \(Q/A\to0\) 已足够，且其能量证明更自然。另一方面，只有 \(Q\) 控制尚不能保证度量一致，因为
\[
\partial_tg=-2aE
\]
的点态速度需要时间可积的 \(L^\infty\) 控制。可尝试用 Wang 型 weighted Ricci 估计获得不带 \(\delta_i\) 的可积界，以维持 metric equivalence；但将其从
\(-2\chi^2\operatorname{Ric}\) 改为
\(-2\chi^2(\operatorname{Ric}+g)\)，并使常数对坍缩与支撑数目一致，仍需证明。

---

## 6. 现有来源究竟给了什么

### Li

Li Theorems 3.1、3.4、3.6 提供：

- 全中心初始小能量条件；
- 全流形 supremum 与覆盖 continuation；
- 四维相对 Sobolev–局部归一化能量的坍缩消去；
- 动态能量成立后的 \(C/t\) Moser 提升；
- 普通 Ricci flow 下的曲率势 subsolution 估计。

它们不提供：

- cutoff flow；
- 过渡项估计；
- 仅在平台中心上的闭合 supremum；
- 从一个 maximal-function 好点控制任意宏观支撑。

### Yang/Wang

Yang/Wang 提供：

- \(\partial_tg=-2\chi^2\operatorname{Ric}\) 的 local Ricci flow 框架；
- 含 cutoff 的曲率能量计算；
- 在全局 Sobolev 常数、活动域整体临界能量小及 \(L^p\)-Ricci 假设下的 weighted curvature/Ricci 估计。

它们不直接提供：

- 当前归一化 defect flow；
- 多个坍缩支撑上的相对球 Sobolev/局部归一化能量版本；
- 动态逐球无集中结论；
- 支撑求和的 \(Q/A\) 定理。

尤其 Wang Proposition 3.12/Thm 6.3 的 Sobolev 与整体能量假设不能仅凭“体积最终会消去”就自动满足；必须把局部覆盖与相对系数写进证明。

---

## 7. 精确所需的新定理

足以完成 smoothing bridge 的解析定理至少应断言：

1. 对固定比例嵌套支撑和 \(|d\chi|\le Cr^{-1}\)，退化归一化 cutoff flow 存在至 \(T\ge\theta r^2\)；
2. 流中度量、固定初始球、Dirichlet Sobolev 常数统一可比；
3. 每个支撑内所有相关 \(r\)-球的局部归一化曲率能量持续低于临界阈值，而非仅支撑总能量有界；
4. 所有 cutoff-transition 曲率项经分部积分后只产生可控的 \(r^{-2}\) 低阶项；
5. 内平台满足 \(|\operatorname{Rm}|\le C/t\)；
6. defect 能量满足 \(q_j(t)\le Cq_j(0)\)，常数独立于坍缩体积和支撑数；
7. 有足够的时间可积 weighted \(L^\infty\) 速度估计以保证 metric equivalence。

其中第 3–4 项是主要未证对象；正则化 \(\chi_\varepsilon\ge\varepsilon\) 不会自动解决它，因为外部高曲率区域此时也参与扩散，必须先有对 \(\varepsilon\) 一致的 weighted estimates。

---

## 8. Step 15 在 Step 16 后仍成立与不成立的部分

### 仍成立

- 支撑尺度改为 \(O(r_*)\) 后的 comparable-ball 初始小能量；
- 四维 Sobolev–能量体积消去；
- cutoff defect 方程在 \(E\) 中的齐次性；
- 条件于 \(Q(t_0)/A\to0\) 的拓扑重标定；
- 条件于受控 cover/chart 极限的 Step 8 Derdziński 局部矛盾。

### 不成立或仍待证

- 以有限传播或“\(\sqrt t\) 尚未到边界”为依据忽略过渡环；
- 直接把 Li 的全中心 supremum 限制到内平台；
- 由冻结外部推出全局逐点 \(|E|=O(\delta_i)\)；
- 由支撑总曲率能量保持推出每球临界小量保持；
- 由有界曲率自动得到所需 buffered normal covers；
- 四维负支 LeBrun 临界反证链已经完成。

即使解析 weighted-flow 定理完成，有界曲率到正常覆盖可达性的几何重构仍是独立缺口：需统一 lifted noncollapse、harmonic radius、deck-averaging buffer，并处理 rank drop、奇异层和短可缩轨道。现有材料未证明这一层。

最终，完整的 weighted theorem 加 cover reconstruction 至多排除当前 LeBrun/Ishida–LeBrun 临界实验族，不能据此宣称解决一般四维负支或 \(n\ge5\) 的 Yau 第 26 题。
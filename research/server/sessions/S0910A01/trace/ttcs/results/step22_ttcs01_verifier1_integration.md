# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 22,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step22_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step22_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 22 repair to the cutoff-flow smoothing argument for Yau Problem 26's four-dimensional negative LeBrun/Ishida-LeBrun laboratory. Read the corrected notes and scripts. The scientific questions: (1) Does the correction correctly distinguish component energy int_U F^2 <= M Vol(U) from the false Whitney-volume-normal bound int_W F^2 <= C M Vol(W)? (2) Does the retained scale-invariant Whitney estimate ell^4 average_W F^2 and the Sobolev product A_W^2||F||_2 <= C r^2 sqrt(M) follow with the right powers? (3) Is the current component first-exit formulation Gamma(t)=sup A_alpha^2 H_2,alpha(t)^{1/2} the right way to prove energy persistence and cubic potential A^4 H_3 <= C Gamma^3/t? (4) Does the weak nested moment estimate use the correct weights H_q=int eta^2 a^(q-2)F^q and v_q=eta a^((q-1)/2)F^(q/2), and are the Holder/Sobolev exponents, finite-neighbor terms, and endpoint scalings scientifically consistent? Identify any remaining mathematical gaps or wrong inferences, especially about transition curvature closeness, metric displacement, unweighted defect Q, and plateau bounded-curvature needs. Do not decide the whole research route; give a mathematical verification memo.

## Integrated Scientific Memo

# Step 22 数学核验备忘录

## 总体结论

Step 22 **正确修复了核心能量归一化错误**：

\[
\int_UF^2\le M\operatorname{Vol}(U)
\]

不能推出任意 Whitney 球 \(W\subset U\) 上的

\[
\int_WF^2\le CM\operatorname{Vol}(W).
\]

四维中真正保留下来的是

\[
\ell^4\fint_WF^2\le CMr^4,
\qquad
A_W^2\|F\|_{L^2(W)}\le Cr^2\sqrt M.
\]

加权矩体系的 \(a,F\) 次数、Hölder–Sobolev–Young 指数以及两个终点尺度也基本正确。然而，当前笔记尚不是闭合证明：内外 cutoff、邻域耗散吸收、时间柱嵌套和图传播都有必须修正的实质细节；精确张量不等式、未加权缺陷 \(Q\) 的三角估计以及 cutoff flow 的存在延拓仍未证明。

---

## 1. 分量能量与 Whitney 能量

由 \(W\subset U\) 只能得到

\[
\int_WF^2\le \int_UF^2\le M\operatorname{Vol}(U).
\]

能量可以集中在 \(W\)，故不能把右端换成 \(CM\operatorname{Vol}(W)\)。

体积比较的幂正确，但 (1.3) 的非同心球论证应写严谨。若
\(U=B_{5r}(p)\)、\(y\in B_{4r}(p)\)，则

\[
U\subset B_{9r}(y).
\]

因此在初始度量的 Ricci 下界/体积倍增假设下，

\[
\operatorname{Vol}(B_\ell(y))
 \ge c\left(\frac{\ell}{9r}\right)^4
      \operatorname{Vol}(B_{9r}(y))
 \ge c\left(\frac{\ell}{9r}\right)^4\operatorname{Vol}(U).
\]

所以笔记中的 \(5\) 应理解为被常数吸收后的记号，而非直接同心 Bishop–Gromov 比较。后续时刻可由固定域上的双 Lipschitz 比较转移该体积比例；双 Lipschitz 性本身并不赋予 \(g(t)\) 新的 Ricci 下界。

于是

\[
\fint_WF^2\le CM\left(\frac r\ell\right)^4,
\qquad
\ell^4\fint_WF^2\le CMr^4.
\]

当 \(\ell=cr\chi_0\) 时，局部平均确可增长为 \(O(\chi_0^{-4})\)。

---

## 2. Whitney Sobolev 消去

四维相对 Sobolev 系数具有尺度

\[
A_W^2\lesssim \ell^2\operatorname{Vol}(W)^{-1/2}.
\]

结合分量能量和上述体积比，

\[
\begin{aligned}
A_W^2\|F\|_{L^2(W)}
&\lesssim
\ell^2\operatorname{Vol}(W)^{-1/2}
\bigl(M\operatorname{Vol}(U)\bigr)^{1/2}\\
&\lesssim
\ell^2\sqrt M\left(\frac r\ell\right)^2
\lesssim r^2\sqrt M.
\end{aligned}
\]

因此两个保留量的幂均正确，而且 \(\chi_0\) 恰好消去。这是四维临界现象。相关脚本正确检查了尺度，但不能替代体积比较和 Sobolev 定理。

---

## 3. 第一退出能量：正确变量，但当前图估计尚需修补

自然的临界变量确为

\[
\gamma_\alpha=A_\alpha^2H_{2,\alpha}^{1/2},
\qquad
\Gamma=\sup_\alpha\gamma_\alpha.
\]

其理由是

\[
H_{3,\alpha}
=\int aF(\eta F)^2
\lesssim
\|F\|_{L^2(\widehat U_\alpha)}
\|\eta a^{1/2}F\|_4^2
\lesssim
\gamma_{\widehat\alpha}
\bigl(D_{2,\alpha}+r^{-2}H_{2,\widehat\alpha}\bigr),
\]

其中必须使用一个在内层测试区域上恒为 \(1\) 的**外层 cutoff/domain**。仅用

\[
H_{2,\alpha}=\int\eta_\alpha^2F^2
\]

不能控制 \(\operatorname{supp}\eta_\alpha\) 上的无权 \(L^2\) 能量，因为 \(\eta_\alpha\) 在边缘趋零。

另外，当前从

\[
H'_{2,\alpha}+cD_{2,\alpha}
\le C\sum_{\beta\sim\alpha}
(r^{-2}H_{2,\beta}+H_{3,\beta})
\]

直接推到 (2.5) 并不成立：代入 \(H_{3,\beta}\) 后出现邻居耗散
\(D_{2,\beta}\)，不能逐个吸收到 \(D_{2,\alpha}\)。需要二选一：

1. 在发生邻域扩张前，将每个反应项与其自身耗散配对吸收；或
2. 对图系统使用适当加权求和，使所有邻居耗散在总和中被吸收。

由于各分量 Sobolev 常数可能不同，真正适合传播的图变量是

\[
S_\alpha=A_\alpha^4H_{2,\alpha}=\gamma_\alpha^2.
\]

需证明邻居间 \(A_\alpha/A_\beta\) 一致可比，然后得到

\[
S_\alpha'
\le Cr^{-2}\sum_{\beta\sim\alpha}
\frac{A_\alpha^4}{A_\beta^4}S_\beta.
\]

有界度图上的 Dini-sup Gronwall 或图半群估计才给出不依赖分量总数的 \(\Gamma\) 持久性。

因此，\(\Gamma(t)\) 是正确的第一退出对象，但 (2.5)–(2.7) 目前仍是有待完整证明的图局部化结论。

---

## 4. 三次势 \(A^4H_3\)

在上述能量循环严密成立后，预期结论

\[
A_\alpha^4H_{3,\alpha}(t)
\le \frac{C\Gamma_*^3}{t}
\]

的尺度和机制正确：

1. \(q=2\) 吸收给出时空 \(H_3\) 控制；
2. 固定 \(q=3\) 估计传播 \(H_3\)；
3. 在 \([t/2,t]\) 向后平均；
4. 使用 \(A_\beta^4H_{2,\beta}(0)\le \Gamma(0)^2\)。

但 (3.4) 中“固定有限邻居星”并非一般图系统自动给出的结论。正时间传播可沿任意长度路径扩散。严谨形式应使用图半群，例如

\[
H_3(t)\lesssim
t^{-1}e^{C(t/r^2)\mathcal A}
\int_0^t H_3(s)\,ds,
\]

其行和由 \(e^{CNt/r^2}\) 控制；或使用指数加权局部和。这样仍能得到所需
\(C\Gamma_*^3/t\)，且不依赖分量总数。

---

## 5. 加权矩代数：\(a,F\) 次数正确，但 cutoff 次数写错

定义

\[
H_q=\int\eta^2a^{q-2}F^q,
\qquad
v_q=\eta a^{(q-1)/2}F^{q/2}
\]

是正确的，并且

\[
v_q^2=\eta^2a^{q-1}F^q,\qquad
Fv_q^2=\eta^2a^{q-1}F^{q+1},
\]

而

\[
(a^{q-2}F^q)^{1/q}\to aF.
\]

反应项的 \(a,F\) 次数也正确：

\[
R_q=\int\eta^2a^{q-1}F^{q+1}
\]

由 \(H_3^{1/3}\) 与 \(3q/2\) 阶矩组合，Young 损失确为

\[
\varepsilon D_q+
C\varepsilon^{-2}A^4H_3H_q.
\]

但是笔记中的等式

\[
H_{2q,k}^{1/2}=\|v_{q,k}\|_4^2
\]

按所给定义是错误的，因为

\[
H_{2q,k}^{1/2}
=
\left(\int\eta_k^2a^{2q-2}F^{2q}\right)^{1/2},
\]

而

\[
\|v_{q,k}\|_4^2
=
\left(\int\eta_k^4a^{2q-2}F^{2q}\right)^{1/2}.
\]

修复方法是显式使用嵌套 cutoff。若 \(\xi_k\equiv1\) 于
\(\operatorname{supp}\eta_k\)，令

\[
H_{3,\widehat k}=\int\xi_k^2aF^3.
\]

则

\[
R_q\le H_{3,\widehat k}^{1/3}K_q^{2/3},
\quad
K_q=\int\eta_k^3a^{3q/2-2}F^{3q/2},
\]

且

\[
K_q
\le H_{q,k}^{1/2}\|v_{q,k}\|_4^2.
\]

这恢复预期的 Sobolev–Young 估计，但所有右端低阶项应写成外层矩。

同样，

\[
\int a^{q-1}|d\eta_k|^2F^q
\]

不能由同一 \(\eta_k\) 的 \(H_{q,k}\) 直接控制；应由外层无 cutoff/较大 cutoff 矩控制。其 Whitney 系数本身正确：

\[
a|d\eta_k|^2
\lesssim \chi_0^2\frac{4^k}{(r\chi_0)^2}
\lesssim 4^kr^{-2}.
\]

脚本只验证了 \(a,F\) 单项式，没有追踪 \(\eta\) 次数，因此未发现此缺口。

---

## 6. 时间柱嵌套有明确错误

笔记定义

\[
I_k=[t/2+2^{-k-2}t,t].
\]

但 \(I_0=[3t/4,t]\)、\(I_1=[5t/8,t]\)，所以 \(I_{k+1}\) 比 \(I_k\) 更大，无法选择“支撑于 \(I_k\)、在 \(I_{k+1}\) 上为 \(1\)”的时间 cutoff。

可改为例如

\[
I_k=
\left[
\frac t2+\frac t4(1-2^{-k}),t
\right],
\]

它随 \(k\) 缩小至 \([3t/4,t]\)。相应时间 cutoff 导数为
\(O(2^k/t)\)，用较粗的 \(O(4^k/t)\) 仍然成立。

修复内外空间 cutoff 和时间嵌套后，抽象递推

\[
q_{k+1}=\frac32q_k
\]

及无限乘积收敛是正确的。

---

## 7. 终点尺度

曲率从 \(q_0=2\) 开始：

\[
\|aF(t)\|_\infty
\lesssim
A^2(t^{-1}+r^{-2})^{3/2}M_2(Q_0)^{1/2}.
\]

若 \(t\le r^2\) 且 \(M_2(Q_0)\le tH_2\le t\Gamma_*^2/A^4\)，则

\[
\|aF(t)\|_\infty\lesssim \frac{\Gamma_*}{t}.
\]

缺陷从 \(m_0=6\) 开始：

\[
\|aE(t)\|_\infty
\lesssim
A^{2/3}(t^{-1}+r^{-2})^{1/2}M_6(Q_0)^{1/6},
\]

结合 \(J_6\lesssim\delta^6V\) 和
\(A\lesssim rV^{-1/4}\)，得到

\[
\|aE(t)\|_\infty
\lesssim \delta(r^2/t)^{1/3}.
\]

这些尺度正确。但这里需要**正时间 \(J_6\) 持久性**，不能只引用
\(J_6(0)\le\delta^6V\)。固定指数 \(m=6\) 可直接用临界吸收

\[
\int Fz_6^2
\lesssim A^2\|F\|_2(D_6+r^{-2}J_6)
\le \Gamma_*(D_6+r^{-2}J_6),
\]

从而避免从 \(0\) 积分 \(H_3(s)\sim s^{-1}\) 的不可积势。

---

## 8. 度量位移与 transition 曲率

删除“transition 曲率接近初始曲率”的推断完全正确。由

\[
\partial_tg=-2aE
\]

及速度界，

\[
\int_0^T|aE|\,dt
\lesssim
\delta r^{2/3}T^{2/3}
\lesssim \delta r^2
\quad (T=\theta r^2),
\]

只能得到 \(C^0\)/双 Lipschitz 度量位移；曲率涉及空间二阶导数，因此不能推出

\[
\operatorname{Rm}(T)\approx\operatorname{Rm}(0).
\]

而且当 \(a\) 很小时，\(|a\operatorname{Rm}|\) 不控制
\(|\operatorname{Rm}|\)。

在 plateau buffer 上 \(a=1\)，终端界

\[
|\operatorname{Rm}(T)|\le Cr^{-2}
\]

确实给出有限曲率。但若要获得受控光滑 Einstein germ，通常还需稍大 plateau buffer 上、至少在 \([T/2,T]\) 的曲率界，以使用内部导数估计；单一终端时刻的零阶曲率界不足以自动给出所有曲率导数。塌缩情形仍需指数映射拉回，而不能假设统一正 injectivity radius。

另有尺度一致性问题：使

\[
\Gamma(0)\sim r^2\sqrt{1+K_0}
\]

小，要求 \(r\lesssim(1+K_0)^{-1/4}\)，故 plateau 曲率界
\(r^{-2}\gtrsim(1+K_0)^{1/2}\)。若 \(K_0\) 随近 Einstein 序列变化，必须确认先固定 \(r\) 的操作在该序列上具有统一性；否则 plateau 曲率界不足以支持统一极限。

---

## 9. 未加权缺陷 \(Q\)

预期的三角形式

\[
Q_\alpha'
\le Cr^{-2}\sum_{\beta\sim\alpha}Q_\beta,
\qquad
Q_\alpha=\int\eta_\alpha^2|E|^2,
\]

在结构上可信：\(E=0\) 时流速为零且 \(E\) 的演化应齐次于 \(E\)，故不应出现纯曲率源项。但它尚未由材料证明。

精确计算必须证明所有项只产生：

\[
\int\eta^2a|\nabla E|^2,\qquad
\Gamma_*\int\eta^2a|\nabla E|^2,\qquad
r^{-2}\int_{\mathrm{outer}}|E|^2,
\]

并且**没有**

\[
+\varepsilon\int a|\nabla\operatorname{Rm}|^2
\]

或其他与 \(E\) 无关的加性源。随后才能利用有界重叠求和得到全局 \(Q\) 的乘法持久性。

---

## 10. 尚未闭合的核心数学对象

当前修复成立的是归一化、临界尺度与形式代数；仍需完成：

1. 对 \(-2\chi^2(\operatorname{Ric}+g)\) 的完整张量幂估计，包括演化体积、\(F\) 正则化及全部 Hessian-\(a\) 分部积分；
2. 严格的内外 cutoff 系统；
3. 邻居耗散的全局吸收和带 Sobolev 权的图传播；
4. 修正后的时间柱递推；
5. 固定 \(J_6\) 的正时间持久性；
6. 未加权 \(Q\) 三角估计；
7. 空间 cutoff normalized flow 的存在、寿命和光滑延拓；
8. 度量比较、Sobolev、\(\Gamma\)、速度与 \(Q\) 的统一第一退出连续性论证；
9. plateau 上时间区间曲率/导数控制，以及 \(K_0,r\) 对序列的统一性。

因此，Step 22 已正确修复错误的 Whitney-volume-normal 假设，并保住四维临界机制；但目前的 weak nested estimate 和能量持久性仍是**可修复而未完成的证明框架**，不能按现有公式直接视为定理。
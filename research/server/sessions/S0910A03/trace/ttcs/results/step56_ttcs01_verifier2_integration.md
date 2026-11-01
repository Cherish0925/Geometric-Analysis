# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 56,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step56_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step56_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Step 56 Section 6 as the interface between per-datum flow construction and the collapse-uniform first-exit program. Check specifically: H_2 must be unweighted in a; shifted T versus Rm comparability; the exact global-Q decomposition with Q_rest and whether Q_rest is stationary given eta=1 near active supports; and the logical continuation argument that starts each datum separately, obtains uniform first-exit estimates only on its actual lifespan, and uses the positive-time U/T/cutoff-jet hierarchy to rule out an endpoint before theta r^2 without importing high cutoff jets into the uniform estimates. Identify any circularity or support-geometry flaw.

## Integrated Scientific Memo

# Step 56 §6 核验结论

§6 的接口结构基本正确，但要成为严格论证，须作三项明确修订：

1. 将 \(T\) 与曲率的比较写成  
   \[
   1+|T|^2\asymp_n 1+|\Rm|^2,
   \]
   不能写成 \(|T|^2\asymp 1+|\Rm|^2\)；
2. \(T_i^*\) 必须是通过所有可行光滑重启拼接得到的**极大可延拓分支**的端点，而非任意“chosen branch”的端点；
3. 明示全局系数与多支撑构造的对应：
   \[
   \chi=\sum_\alpha\chi_\alpha,\qquad
   a=\chi^2=\sum_\alpha\chi_\alpha^2,
   \]
   这里等式依赖 \(\chi_\alpha\) 支撑两两不交。

在这些修订以及下述严格支撑嵌套下，没有发现 §6 本身的循环论证或支撑几何缺陷。

---

## 1. \(H_2^\alpha\) 必须无 \(a\)-权

由
\[
H_q^\alpha(t)=\int_M\eta_\alpha^2a^{q-2}F_T^q\,d\mu_t,
\qquad F_T=(1+|T|^2)^{1/2},
\]
在 \(q=2\) 时严格得到
\[
\boxed{H_2^\alpha(t)=\int_M\eta_\alpha^2F_T^2\,d\mu_t.}
\]
此处 \(a^0\) 按 \(1\) 解释，包括 \(\{a=0\}\)。

这不是符号选择，而是临界 Sobolev 吸收所必需：\(H_2^\alpha\) 要控制整个 \(\eta_\alpha\)-区域，包括 \(a\) 很小或为零的缓冲环带。若插入额外因子 \(a\)，该能量在环带上丢失全部曲率信息，不能代入
\[
\gamma_\alpha=\mathcal S_\alpha H_2^\alpha(0)^{1/2}
\]
的吸收论证。

应同时区分两个不同对象：

- \(H_2^\alpha\) 是覆盖整个 \(\eta_\alpha\)-支撑的无权能量；
- \(\|aF_T(t)\|_\infty\lesssim\gamma/t\) 是加权点态界，主要在 \(a=1\) 平台上提供曲率控制。

二者用途不同，并不矛盾。

---

## 2. shifted curvature 的正确比较式

令
\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\Rm+G.
\]
由于 \(|G|_g=b_n\) 是纯维数常数，
\[
1+|T|^2\le C_n(1+|\Rm|^2),\qquad
1+|\Rm|^2\le C_n(1+|T|^2).
\]
因此正确陈述是
\[
\boxed{F_T^2=1+|T|^2\asymp_n1+|\Rm|^2.}
\]

Step 56 中“\(|T|^2\) 与 \(1+|\Rm|^2\) 可比”的原句不成立。例如 \(\Rm=-G\) 时 \(T=0\)，而 \(1+|\Rm|^2>0\)。

若
\[
\supp\eta_\alpha\subset B_{7r}(x_\alpha),\qquad
\fint_{B_{7r}(x_\alpha)}|\Rm|^2\le\kappa_0^2,
\]
则
\[
H_2^\alpha(0)
\le C_n(1+\kappa_0^2)\Vol B_{7r}(x_\alpha),
\]
从而
\[
\mathcal S_\alpha H_2^\alpha(0)^{1/2}
\le Cr^2\sqrt{1+\kappa_0^2}.
\]
这里必须同步以下三个半径数据：

- 包含 \(\supp\eta_\alpha\) 的球；
- maximal-function 可用的最大半径；
- 局部 Sobolev 区域。

源材料中有 \(6r\) 与 \(7r\) 两套记号；任一套均可，但不得混用。若使用不同半径，须显式用 Ricci 下界下的 Bishop–Gromov 比较体积。

---

## 3. 全局 \(Q\) 的精确分解与静止余项

设外层支撑两两不交，且
\[
0\le\eta_\alpha\le1,\qquad
\rho=\sum_\alpha\eta_\alpha^2.
\]
于是 \(0\le\rho\le1\)。定义
\[
Q_\alpha(t)=\int\eta_\alpha^2|E|^2\,d\mu_t,\qquad
Q_{\rm rest}(t)=\int(1-\rho)|E|^2\,d\mu_t.
\]
逐点代数恒等式给出
\[
\boxed{
Q_{\rm global}(t)
=Q_{\rm rest}(t)+\sum_\alpha Q_\alpha(t).
}
\]

### 静止性所需的准确支撑条件

需要严格嵌套
\[
\boxed{\supp\chi_\alpha\Subset\{\eta_\alpha=1\}.}
\]
因此 \(\rho=1\) 于 \(\supp a\) 的一个开邻域，而
\[
\supp(1-\rho)\Subset\{a=0\}.
\]
在精确几何流
\[
\partial_tg=-2a(\Ric_g+g)
\]
上，该开集内 \(g(t)=g(0)\)，因而其全部空间 jet、\(E\) 和体积元均固定。所以
\[
Q_{\rm rest}(t)=Q_{\rm rest}(0),
\]
最终得到精确分解
\[
\boxed{
Q_{\rm global}(t)
=Q_{\rm rest}(0)+\sum_\alpha Q_\alpha(t).
}
\]

仅知道某些点上 \(a=0\) 而没有开缓冲并不足以直接推出 Ricci 张量静止，因为 Ricci 涉及二阶空间导数；严格嵌套消除了这一问题。

若
\[
Q_\alpha(t)\le e^{Lt}Q_\alpha(0),
\]
则因 \(Q_{\rm rest}(0)\ge0\)，
\[
\begin{aligned}
Q_{\rm global}(t)
&\le Q_{\rm rest}(0)+e^{Lt}\sum_\alpha Q_\alpha(0)\\
&=e^{Lt}Q_{\rm global}(0)
 -(e^{Lt}-1)Q_{\rm rest}(0)\\
&\le e^{Lt}Q_{\rm global}(0).
\end{aligned}
\]
因此被选择的支撑无需覆盖 \(M\)。

该论证只能用于去除 \((\varepsilon,\nu)\) 后并完成 DeTurck pullback 的精确流；正则化近似在原活动区域之外仍会演化，不能声称 \(Q_{\rm rest}\) 静止。

---

## 4. 多支撑与 §5 单一 transported cutoff 的接口

§§1–5 用一个标量初值 \(\chi\)，而 §6 写
\[
a=\sum_\alpha\chi_\alpha^2.
\]
由于外层 \(\eta_\alpha\)-支撑两两不交，内层 \(\chi_\alpha\)-支撑也两两不交。令
\[
\chi=\sum_\alpha\chi_\alpha.
\]
则
\[
0\le\chi\le1,\qquad
\chi^2=\sum_\alpha\chi_\alpha^2=a.
\]
这应在正文中显式写出，否则单 cutoff 构造与多支撑 first-exit 之间存在记号缺口。

统一 first-exit 常数还使用
\[
|d\chi|\lesssim r^{-1},\qquad |d\eta_\alpha|\lesssim r^{-1},
\]
而不仅是前者。高阶 cutoff jets 不应出现在这些统一常数中。

---

## 5. 正确的逐数据延拓论证

对每个 datum \(i\)，Step 56 的 tame 局部定理只给出某个
\[
T_i=T_i(g_i,\chi_i)>0,
\]
它可以依赖高 Sobolev 范数和所有高阶 cutoff jets，不能由曲率—体积预算统一下界。

应定义 \(T_i^*\) 为：从该局部解出发，每逢得到光滑端点就允许用同一固定 \(a_i\) 重启并拼接，由此所得一个**极大可延拓光滑分支**的右端点。任意人为截断的 chosen branch 不足以产生“重启违背极大性”的矛盾。

在实际存在区间
\[
0<t<\min\{T_i^*,\theta r^2\}
\]
上定义 first-exit 条件，并仅使用下列统一输入：

- 无权 \(H_2^\alpha\)；
- 局部 Sobolev 系数及其 bilipschitz 比较；
- \(|d\chi|,|d\eta|\lesssim r^{-1}\)；
- 初始 defect 能量；
- 固定的严格支撑缓冲。

由 first-exit 改进得到
\[
\|aF_T(t)\|_\infty\le \frac{C\gamma}{t},
\qquad
\|aE(t)\|_\infty
 \le C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]
第一式在 \(t=0\) 不可积，也不是零时刻一致界；第二式的 \(t^{-1/3}\) 可积，正好给出
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
 \le C\delta\theta^{2/3}r^2,
\]
从而严格改进 metric drift、moving Sobolev 和支撑几何条件。

若反设
\[
T_i^*<\theta r^2,
\]
则在终端正时间片
\[
[T_i^*/2,T_i^*)
\]
上
\[
\|U\|_\infty=\|aT\|_\infty
\le \|aF_T\|_\infty
\le \frac{2C\gamma}{T_i^*}<\infty.
\]
该常数可能随 datum 变坏，但对当前 datum 有限，已足够继续：

\[
T_0
\longrightarrow(U_1,C_2)
\longrightarrow T_1
\longrightarrow(U_2,C_3)
\longrightarrow T_2\longrightarrow\cdots .
\]

其中：

1. Step 44 的无权估计先给每个有限 \(p\) 的 \(T_0\in L^p\)；
2. Step 40 的同阶耦合估计传播 \((U_m,C_{m+1})\)；
3. 随后传播 \(T_m\)；
4. 取 \(p>n\) 得到所有 \(U\) 的点态导数界；
5. 因
   \[
   \partial_tg=-2\Ric(U),
   \]
   固定坐标中 \(g(t)\) 收敛到光滑正定 \(g(T_i^*)\)；
6. Step 56 的逐数据局部定理从该端点重启。

方程自治且 \(a\) 固定，旧解与新解的全部时间 jets 由相同端点数据递归决定，故即使尚无唯一性，也能光滑拼接。这与极大可延拓性矛盾，故
\[
T_i^*\ge\theta r^2.
\]

---

## 6. 循环性判断

上述结构本身不循环：

- collapse-uniform first-exit 估计只在解的**实际 lifespan** 上运行；
- 它们只证明阈值条件在解存在期间不能先退出；
- 若存在性本身先终止，则在正时间终端片上使用 datum-dependent continuation；
- 高阶 cutoff jets 只用于证明“有限并可延拓”，不反馈到 \(r,\theta,\gamma,\delta\) 等统一参数。

这种分离依赖一个关键事实：统一的 \(H_2,J_6,Q\) 能量中出现的 \(\nabla^2a\) 项必须全部通过 signed-Hessian integration by parts 降为只含 \(|d\chi|^2\) 的系数。若某个统一矩估计仍直接使用 \(\|\nabla^2\chi\|\) 或更高 jets，则 §6.3 的无循环声明会失败。

---

## 7. 精确剩余依赖

§6 的接口经上述修订后成立，但其结论仍以以下上游模块为条件，当前给定材料未重新逐项证明它们：

1. \(J_6\) persistence 确实不依赖非可积的 \(Y(t)\sim t^{-1}\)，否则 defect drift 闭合会循环；
2. 每个 uniform moment inequality 中均完整实施 signed-Hessian IBP；
3. 精确流上的局部
   \[
   Q_\alpha(t)\le e^{Ct/r^2}Q_\alpha(0)
   \]
   已在不引入支撑数因子的情况下证明；
4. Step 56 的 tame product estimate (2.6) 足以严格建立逐数据 start/restart。

因此，核验结果是：**§6 作为“逐数据构造 \(\to\) collapse-uniform first exit \(\to\) 正时间延拓”的接口是逻辑一致的；不存在已识别的循环或支撑漏洞，但必须修正曲率比较式、极大分支措辞，并显式写出多支撑 cutoff 与严格缓冲条件。**
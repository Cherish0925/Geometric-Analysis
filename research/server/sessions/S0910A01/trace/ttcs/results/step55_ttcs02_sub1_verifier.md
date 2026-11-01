# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A01/workspace/data/step55_finite_restart_threshold_verify.json",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md"
  ]
}
```

## Task

Verify the Step 55 finite restart threshold and next cutoff-jet exchange. Read the new finite-restart note plus A03 Step56 base pair and Step57 H2/continuation note. Focus on the actual mathematics of the positive-time collar continuation: starting from T,T1,U1,C2 in all finite Lp and |T|_infty, does the derivation of the (U2,C3) estimate correctly handle the dangerous chi*C4*U term and the evolution partial_t C3 ~ C1*U2? Are the Hölder exponents and weighted Sobolev absorption in I31 valid for p>=2? Is the claimed finite restart package through (U_s0,C_{s0+1}) and T_0..T_{s0-1} sufficient to obtain fixed-background H^{s0} restart data via A=∇^{g(t)}-∇bar? Identify any false term, missing counterterm, or weaker assumption needed. Do not review the whole Yau 26 route; only this finite continuation bridge.

## Output

# 科学核验备忘录：正时间 collar 延拓与有限阶重启

## 1. \((U_2,C_3)\) 的核心交换

设
\[
D_{2,p}^U=\int_M\chi^2|\nabla U_2|^2|U_2|^{p-2}\,d\mu,
\qquad U_2=\nabla^2U .
\]
对顶阶项
\[
\int |U_2|^{p-2}U_2*\chi C_4*U
\]
作一次分部积分，确实产生三类项：
\[
\chi C_3*U*\nabla(|U_2|^{p-2}U_2),\qquad
C_1C_3*U*|U_2|^{p-1},
\]
以及
\[
\chi C_3*U_1*|U_2|^{p-1}.
\]
前两类分别由 \(D_{2,p}^U\) 吸收和同指数 Young 不等式控制。第三类就是需要认真处理的
\[
I_{31}=\int\chi |C_3||U_1||U_2|^{p-1}.
\]

令
\[
f=\chi |U_2|^{p/2},\quad
x=\|C_3\|_p,\quad y=\|U_2\|_p,\quad b=\|U_1\|_4.
\]
当 \(p>2\) 时，
\[
\frac14+\frac1p+\frac14+\frac{p-2}{2p}=1,
\]
故
\[
I_{31}\le \|f\|_4\,x\,b\,y^{p/2-1}.
\]
当 \(p=2\) 时使用 \((4,2,4)\)，最后一个因子消失。这两组 Hölder 指数均正确。

四维 Sobolev 不等式和 Kato 不等式给出
\[
\|f\|_4^2
\le C_S\left(
p^2D_{2,p}^U+
(1+\|C_1\|_\infty^2)\|U_2\|_p^p
\right).
\]
因此
\[
\begin{aligned}
I_{31}
&\le Cpbxy^{p/2-1}(D_{2,p}^U)^{1/2}
   +Cbxy^{p-1}\\
&\le \varepsilon D_{2,p}^U
 +C_{\varepsilon,p}b^2x^2y^{p-2}
 +Cbxy^{p-1}.
\end{aligned}
\]
对 \(p\ge2\)，
\[
x^2y^{p-2}\le \frac2p x^p+\frac{p-2}{p}y^p,
\qquad
xy^{p-1}\le \frac1p x^p+\frac{p-1}{p}y^p.
\]
所以
\[
I_{31}\le
\varepsilon D_{2,p}^U+
C_{\varepsilon,p,b}(1+x^p+y^p).
\]
这也直接覆盖 \(p=2\)。`step55_finite_restart_threshold_verify.json` 对 Hölder 指数的数值核算与上述解析计算一致。

## 2. \(C_3\) 的时间演化

由于 \(\chi\) 是固定标量，
\[
\partial_t C_2=-(\partial_t\Gamma)*C_1,
\]
进而
\[
\partial_t C_3
=-(\nabla\partial_t\Gamma)*C_1
-(\partial_t\Gamma)*C_2
\]
，省略号只代表指标排列产生的有限多个同型收缩。又有
\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)
=g^{-1}*g^{-1}*U_1,
\]
以及内禀地
\[
\nabla\partial_t\Gamma=g^{-1}*g^{-1}*U_2.
\]
因此最高阶结构确为
\[
\partial_tC_3=C_1*U_2+C_2*U_1.
\]
固定背景表示时可以出现 \(A\)-乘积，但内禀公式本身不需要 \(A\) 或 \(T\) 项。

计入张量范数和体积元随时间的变化后，只增加由 \(\|U\|_\infty\) 控制的
\(\|C_3\|_p^p\) 项。两个主要积分满足
\[
\int |C_3|^{p-1}|U_2|
\le C(\|C_3\|_p^p+\|U_2\|_p^p),
\]
以及
\[
\int |C_3|^{p-1}|C_2||U_1|
\le
\|C_3\|_p^{p-1}\|C_2\|_{2p}\|U_1\|_{2p}.
\]
所以 Step 55 的 \(C_3\) 能量估计是正确的。

## 3. \(U_2\) 方程漏写了一个当前阶 Hessian 项

Step 55 的式 (2.3) 没有显式列出
\[
\boxed{\chi C_2*U_2}.
\]
该项至少从以下两处自然产生：

1. 对基准项 \(\chi C_2*U\) 微分两次；
2. 对漂移项 \(\chi C_1*\nabla U\) 微分时，使用
   \[
   \nabla(\chi C_1)=C_1*C_1+\chi C_2.
   \]

它不能被描述成“有界系数乘 \(U_2\)”，因为基准输入只有
\(C_2\in L^q\) 对每个有限 \(q\)，并没有 \(C_2\in L^\infty\)。

不过该项由 Step 56 的 signed-Hessian 方法直接控制。测试后写成
\[
J=\int\chi(C_2)_{ij}\mathcal B^{ij}(U_2),
\qquad
|\mathcal B|\le C|U_2|^p,\quad
|\nabla\mathcal B|\le Cp|U_2|^{p-1}|\nabla U_2|.
\]
分部积分得到
\[
\begin{aligned}
|J|
&\le C\int |C_1|^2|U_2|^p
 +Cp\int\chi|C_1||U_2|^{p-1}|\nabla U_2|\\
&\le \varepsilon D_{2,p}^U+
 C_{\varepsilon,p}\|C_1\|_\infty^2\|U_2\|_p^p.
\end{aligned}
\]
所以这个漏项可由已有结构处理，但必须写入推导。加入它以后，\((U_2,C_3)\) 的闭合式
\[
\frac d{dt}\bigl(\|U_2\|_p^p+\|C_3\|_p^p\bigr)
+cD_{2,p}^U
\le C_{p,\tau}
\bigl(1+\|U_2\|_p^p+\|C_3\|_p^p\bigr)
\]
在所述正时间输入下成立。

另一个书写问题是一般式 (4.1) 把
\[
\sum_j C_{k+2-j}*U_j
\]
写得过于粗略：\(j=k\) 时实际的当前阶项应保留
\(\chi C_2*U_k\)，而 \(j=1\) 的关键项应为
\(\chi C_{k+1}*U_1\)。去掉这些 \(\chi\) 因子会丢失用于吸收的权重。

较合适的当前阶结构是
\[
\begin{aligned}
(\partial_t-a\Delta)U_k
={}&\chi C_1*\nabla U_k
+\chi C_2*U_k+C_1*C_1*U_k\\
&+\chi C_{k+2}*U
+C_1*C_{k+1}*U
+\chi C_{k+1}*U_1
+\mathcal P_k,
\end{aligned}
\]
其中 \(\mathcal P_k\) 只含先前已控制的 \(U_j,C_j,T_j\) 以及由时空交换子产生的乘积。

## 4. 所需输入可以写得更精确

对固定 \(p\)，上述两个核心交换实际只使用：

\[
\|U\|_\infty,\quad \|C_1\|_\infty,\quad
U_1\in L^4\cap L^{2p},\quad C_2\in L^{2p},
\]
再加上当前的 \(U_2,C_3\in L^p\)、统一双 Lipschitz 等价和一个固定的 Sobolev 常数。

\(|T|_\infty\) 不参与 \(I_{31}\) 或 \(C_3\) 演化本身。它可用于简化其余曲率反应项以及后续 \(T_2\) 估计。Step 55 的开头已经把 Step 57 的 \(|T|_\infty\) 作为输入，但式 (2.2) 没有列出；若“其余系数由 \(|T|\) 控制”被直接当作有界系数使用，应在 (2.2) 中补上
\[
T\in L^\infty_{t,x}.
\]

对于 \(T_2\)，同样还要显式处理 \(\chi C_2*T_2\) 的 signed-Hessian 项。顶阶
\(\chi C_4*T\) 的一次分部积分和
\(\chi C_3*T_1\) 的 Hölder–Sobolev处理则与 \(U_2\) 完全平行。

## 5. 固定背景导数计数

取 \(\bar\nabla=\nabla^{g(\tau)}\)，
\(A=\nabla^{g(t)}-\bar\nabla\)。连接变分满足
\[
\partial_tA=g^{-1}*\nabla\operatorname{Ric}(U).
\]
对 \(m\) 次固定背景导数，
\[
\bar\nabla^m\partial_tA
=g^{-1}*U_{m+1}
+P_m(A_0,\ldots,A_{m-1};U_0,\ldots,U_m;g^{-1}),
\]
其中没有 \(A_m\)。这里的三角结构是正确的。由 \(A(\tau)=0\)，可依次得到
\[
A_m\in L^\infty_tL^q_x,\qquad 0\le m\le s_0-1
\]
，对每个有限 \(q\) 成立。

需要注意：仅说“低阶 \(A_j\) 在 \(L^2\)”不足以估计 \(P_m\) 中的乘积。应当在各有限 \(L^q\) 中同步积分该三角系统，再用 Hölder 将乘积放入 \(L^2\)。所提出的 current-pair 输入恰好提供了这些有限指数。

由
\[
\bar\nabla g=A*g
\]
递推可得
\[
\bar\nabla^{m+1}g=A_m*g+\text{低阶 }A\text{ 乘积}.
\]
因此控制 \(A_0,\ldots,A_{s_0-1}\) 正好给出固定背景
\(H^{s_0}\) 控制，而控制这些 \(A_m\) 正好需要
\[
U_1,\ldots,U_{s_0}.
\]
同时
\[
\bar\nabla^m\partial_tg
=\bar\nabla^m[-2\operatorname{Ric}(U)]
\]
在 \(m\le s_0\) 时只需要 \(U_0,\ldots,U_{s_0}\) 和
\(A_0,\ldots,A_{s_0-1}\)。有限时间区间上的统一估计给出
\[
\partial_tg\in L^1_tH^{s_0}_{\bar g},
\]
故 \(g(t)\) 在 \(H^{s_0}_{\bar g}\) 中为 Cauchy。由
\(\int\|U\|_\infty dt<\infty\) 得到统一正定性。

在 \(n=4\) 且局部定理要求 \(s_0>6\) 时，最小整数确为
\[
s_0=7.
\]
于是
\[
(U_1,C_2),\ldots,(U_7,C_8),
\qquad T_0,\ldots,T_6
\]
具有正确的导数计数。这里 \(T_j,C_j\) 是构造 \(U_j\) 估计所需的辅助层；固定背景 \(H^7\) 转换本身直接使用的是 \(U_0,\ldots,U_7\)。

若局部定理只对光滑初始度量表述，可以在 \(t_i\uparrow T_*\) 的光滑时刻重启；统一的 \(H^{s_0}\) 范数和正定性必须给出只依赖这些量的统一存在时间。这样不必先证明终端 \(H^{s_0}\) 极限本身光滑。

## 6. 综合判断

- \(\chi C_4*U\) 经一次分部积分后产生的 \(I_{31}\) 处理正确，四维 Sobolev 指数和所有 \(p\ge2\) 的 Hölder 指数均成立。
- \(\partial_tC_3\) 的最高阶交换 \(C_1*U_2\) 正确，\(C_2*U_1\) 由先前所有有限 \(L^q\) 信息控制。
- \(U_2\) 方程漏写了 \(\chi C_2*U_2\)，但 signed-Hessian 分部积分正好处理它，不需要 \(C_2\in L^\infty\)。
- 固定背景的导数计数与 \(s_0=7\)、\(U_7\)、\(C_8\)、\(T_6\) 完全一致。
- 一般式 (4.1)–(4.6) 尚需把 \(\chi C_2*U_k\)、空间交换子、时间连接交换子及
  \[
  aT_k=U_k-\sum_{\ell=1}^k{\binom{k}{\ell}}(\nabla^\ell a)*T_{k-\ell}
  \]
  逐类写出。当前 \(k=2\) 计算表明这些项具有可用的吸收机制，但简写的 (4.1) 本身还不能代表完整的有限阶推导。
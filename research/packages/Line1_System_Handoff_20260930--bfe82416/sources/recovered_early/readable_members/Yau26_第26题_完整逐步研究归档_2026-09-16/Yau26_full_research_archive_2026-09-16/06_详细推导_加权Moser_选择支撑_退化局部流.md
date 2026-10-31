# 06 详细推导：选择支撑、加权 Moser、退化局部流与 continuation

## 1. selected support

四维
\[
\int|Rm|^2
\]
scale invariant，因此不能靠缩小球自动得到小能量。

采用
\[
\mathcal M_Rf(x)=
\sup_{0<s\le R}\fint_{B_s(x)}f.
\]
最终结构：
- \(7r\le R\)；
- outer \(B_{7r}\) pairwise disjoint；
- strict gradient buffers；
- inner centers 位于较大 \(a=1\) plateau；
- global
  \[
  a=\sum_\alpha\chi_\alpha^2.
  \]

## 2. Sobolev-volume cancellation

\[
\|u\|_4^2
\le
\mathcal S(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2),
\qquad
\mathcal S\asymp\frac{r^2}{\sqrt V}.
\]
若
\[
K_2\le K_0V,
\]
则
\[
\gamma=\mathcal S K_2^{1/2}
\lesssim r^2\sqrt{K_0}.
\]

Step33 曾把已是 squared-form coefficient 的 symbol 再平方；Step34 撤回并恢复该 volume cancellation。

## 3. 为什么 ordinary unweighted Moser 不够

退化 flow 中 diffusion coefficient 是 \(a\)：
\[
\partial_tT=a\Delta T+\cdots.
\]
直接对 \(T\) 做标准 Moser，diffusion 与 nonlinear weight 不匹配。

定义 weighted unknown
\[
U=aT.
\]

## 4. mixed recurrence

关键：
\[
H_{3p/2}\lesssim H_p^{1/2}\|z_p\|_4^2.
\]
再用 squared Sobolev。指数
\[
p_{k+1}=\frac32p_k,
\qquad
\sum_{k\ge0}\frac1{p_k}=\frac3{p_0}.
\]

这解释最终 temporal exponent \(t^{-3/p_0}\)。

## 5. first-exit 中的时间积分

代表性目标：
\[
\|aE(t)\|_\infty
\lesssim
\delta(r^2/t)^{1/3},
\]
从而
\[
\int_0^T\|aE\|_\infty dt
\lesssim \delta\,\theta^{2/3}r^2.
\]

该积分用于 metric drift、support geometry、moving Sobolev 的同步控制。

## 6. top cutoff jets

\(a=\chi^2\)：
\[
\nabla^{m+2}a
=
2\chi C_{m+2}+\text{lower}.
\]
又
\[
a(\nabla^2a)T=(\nabla^2a)U.
\]
所以 highest cutoff jet 总以
\[
\chi C_{m+2}U
\]
或更好形式出现。signed integration by parts 若打到 \(\chi\)，cutoff order 降一阶。

## 7. staggered pair

正确 induction unit 是
\[
(U_m,C_{m+1}),
\]
因为
\[
\int|C_{m+1}|^2|U_m|^{p-2}
\]
需要同 exponent coupled energy 闭合。

## 8. base-order dependency 修复

后期正确顺序：
\[
U_0\in L^\infty,\ T_0\in L^q
\]
先推出
\[
(U_1,C_2),
\]
再 \(T_1\)，之后再升级 \(T_0\in L^\infty\)，最后进入 \(m\ge2\)。

防止 \(W^{1,p}\to L^\infty\) circularity。

## 9. fixed-background connection

修正后的形式：
\[
\partial_tA_m
=
g^{-1}*U_{m+1}
+
P_m(A_{\le m-1},U_{\le m},g^{-1}),
\]
不允许出现 uncontrolled current \(A_m\) coefficient。

## 10. 为什么禁止 \(a+\varepsilon\)

selected-support 设计让 exterior \(a=0\) 静止。若
\[
a_\varepsilon=a+\varepsilon,
\]
外区也开始流动，需要不存在的 exterior curvature/derivative control。

所以：
- Kato norm regularization 可以；
- diffusion coefficient regularization 不可直接用。

## 11. transported-cutoff DeTurck

后续转向：
- fixed degenerate coefficient；
- transported cutoff；
- DeTurck gauge；
- tame high–low derivative allocation；
- scalar viscosity；
- per-datum high-order restart。

这解决单 datum 可运行问题，不自动给 sequence-uniform time。

## 12. per-datum vs sequence-uniform

矛盾序列需要统一：
- support energy；
- observation time；
- metric drift；
- moving Sobolev；
- plateau volume；
- \(K_2/J_6/Q\)；
- terminal derivative bounds。

这仍是 restricted IL theorem 的核心未闭合量词。

## 13. finite checks 的地位

记录包括：
- 14,002,305 tame allocation checks；
- 54/54 critical→subcritical checks；
- 252,256 family enumerations through order64；
- 多个 11/11、28/28、34/34、101/101。

它们可发现 index/weight/schedule 错误，但不证明 tensor signs、PDE existence、uniqueness、continuation、compactness 或 Yau26。

## 14. terminal chart

inner plateau 允许：
- pullback；
- Liouville/Rauch averaging；
- radius shrink；
- strong \(W^{2,p}\) / smooth local convergence。

若 limit 同时满足 \(\mathrm{Ric}=-g\) 并继承 calibrated forbidden Weyl/eigenline profile，则可尝试触发 Derdziński/局部 rigidity contradiction。

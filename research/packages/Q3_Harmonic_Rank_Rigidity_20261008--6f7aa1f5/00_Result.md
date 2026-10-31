# Q3：负标量临界度量不能沿一个谐和方向完全对齐

2026年10月8日。目标仍为光滑、非 Bach-flat 的全局 P 极小元。本稿证明对一个完整候选类别的排除，不证明 Godeaux 单吹起上的光滑取得性。

## 1. 本轮命题

设 M 为闭连通定向四流形，g 的标量曲率为负常数 s，记

\[
E=\operatorname{Ric}^{\circ},\qquad P(g)=\int|E|^2,\qquad
\mathcal R=\begin{pmatrix}W^++sI/12&B^*\\B&W^-+sI/12\end{pmatrix}.
\]

假设存在非零反自对偶谐和二形式 h，使

\[
\operatorname{im}B_x\subset\mathbb Rh_x\qquad(h_x\ne0).
\]

则完整 L² 梯度满足

\[
\boxed{\|\mathcal G_P\|_\infty\ge\frac{|s|}{2}\|E\|_\infty.}
\]

若 E 不恒为零，则存在非负光滑函数 χ，使真正的度量族

\[
g_t=g(e^{-t\chi E^\sharp}\cdot,\cdot)
\]

逐点保持体积形式，并在充分小正 t 时严格降低 P。因此，此类度量若为 P 临界点，就必须 Einstein。

不要求 h 无零点，也不要求由 E 与 h 分解出的另一个因子有界或等长。常数 1/2 由两个不同负常曲率曲面的乘积达到。

## 2. 第一条连接：在 h 的零点，E 必须为零

若 h(p)=0 但 B(p)不为零，则 B 在 p 的邻域具有光滑秩一像线。选择这条线的光滑单位反自对偶形式 θ，便有 h=fθ。由 dh=0，

\[
df\wedge\theta+f\,d\theta=0.
\]

非零反自对偶二形式非退化，所以 α↦α∧θ 是同构，进而 df=fω，其中 ω 光滑。从 f(p)=0 沿路径求解这一线性方程，得到 f 在整个邻域为零，与非零谐和形式的唯一延拓矛盾。因此 B=0、E=0 于 Z(h)。

这没有证明商因子在所有零点可去；它证明了后续真正需要的结论：|E|² 的正最大值不会出现在 Z(h)。

## 3. 第二条连接：保留逐点梯度，而非仅保留积分相关项

在 h 非零的区域，令

\[
\phi=-2B^*h/|h|^2,\qquad E=\phi\circ h.
\]

相反手性与 dh=0 给

\[
\operatorname{div}(\phi\circ h)=h(d^*\phi).
\]

常标量 contracted Bianchi 使左端为零，h 可逆，故 φ 闭且余闭。于是两个局部因子都调和。

记 a=|φ|²、b=|h|²。经典完整梯度与两个 Weitzenböck 方程合并为

\[
\boxed{\mathcal G_P=-\frac{s}{2}E-
2\sum_i(\nabla_i\phi)\circ(\nabla_i h),}
\]

\[
\boxed{\langle\mathcal G_P,E\rangle
=-\frac{s}{2}ab-\frac12\langle da,db\rangle.}
\]

这里两手性 Weyl 项在完整张量式中精确抵消。令 p 为 |E|²=ab 的正最大点。上一节保证 h(p)不为零，因此

\[
b\,da+a\,db=0,\qquad
\langle da,db\rangle=-\frac ba|da|^2\le0.
\]

于是

\[
\langle\mathcal G_P,E\rangle(p)
=\frac{|s|}{2}|E|^2(p)+\frac{b(p)}{2a(p)}|da|^2(p)>0.
\]

由此得到梯度下界；在这个点附近选 χ，就有 DP[-χE]<0。

前稿的积分式允许幅度相关项与正项相互抵消，但临界度量必须满足逐点 Euler–Lagrange 方程。最大点的符号关系排除了这种逐点相容性，不需要先控制整个幅度相关积分。

## 4. Einstein–Maxwell 推论

采用黎曼规范

\[
dF=d^*F=0,\qquad (\operatorname{Ric}+F\circ F)_0=0.
\]

标量曲率为常数，并且

\[
E=(-2F^+)\circ F^-.
\]

因此，闭、负标量 Einstein–Maxwell 度量若同时是 P 临界点，必为 Einstein。这包括两个谐和因子的模长都变化的情形，而不只包括前稿中的等长 almost-Kähler 分支。

对真正的负标量非 Einstein 光滑 P 极小元，还必有

\[
\min_{\substack{0\ne h\in\mathcal H^-\\\|h\|_2=1}}
\int\left|B-\frac{h\otimes B^*h}{|h|^2}\right|^2>0
\]

（当 b⁻>0；正数可依赖该度量）。有限维谐和空间的紧性、谐和零集测度为零与控制收敛给出此结论。

## 5. 与 Q3 的关系

本轮处理了《03_Subsequent_Mathematical_Developments》“The weaker rank-aligned system”的临界性问题，不再需要其中为了全局构造 Maxwell 场而使用的商因子有界性。它也严格加强了前稿只排除等长谐和因子的结论。

但一般极小度量没有被证明必须满足上述谐和像线条件。因此，本稿不提供光滑取得性，也不排除全部轨形和塌缩极限。已知 Godeaux 单吹起区间仍为 16π²/3 ≤ P_* < 8π²。原问题的完整解答尚未取得。

## 6. 来源

完整梯度：Gursky–Viaclovsky, *Rigidity and stability of Einstein metrics for quadratic curvature functionals*, arXiv:1105.4648v2, (2.5), (2.9)。

Einstein–Maxwell 规范：LeBrun, *The Einstein–Maxwell Equations, Extremal Kähler Metrics, and Seiberg–Witten Theory*, arXiv:0803.3734v2。

唯一延拓及谐和零集：Bär, *Zero sets of solutions to semilinear elliptic systems of first order*, Invent. Math. 138 (1999), arXiv:math/9805065。

本轮推导：逐点谐和乘积梯度、谐和像线零点引理及最大值连接。英文稿给出完整证明；check_algebra.py 检查曲率张量恒等式、81项乘积内积关系和闭反自对偶形式的微分收缩。

# Q4：扭率零点、横向 Weyl 与局部指数

2026-10-09。本稿只研究闭四维负 Goldberg 问题的扭率零点入口。局部定理本身不要求紧性或标量曲率符号，不使用项目 FD2、N1 或统一 Einstein 间隙。

## 1. 实际结论

设光滑正定四维 almost-Kähler Einstein 结构满足

\[
 d\Omega=0,\quad |\Omega|^2=2,\quad \operatorname{Ric}=(s/4)g,
 \qquad q=|\nabla\Omega|^2.
\]

采用二形式范数及 Weyl 曲率算子范数。定义

\[
 \eta=W^+(\Omega)-(s/6+q/4)\Omega.
\]

令 \(n=\Omega/\sqrt2\)，并将 \(W^+\) 写成

\[
 W^+=\begin{pmatrix} t & (\eta/\sqrt2)^*\\
 \eta/\sqrt2 & -tI/2+V\end{pmatrix},
 \qquad t=s/6+q/4,\quad \operatorname{tr}V=0.
\]

在每一个 \(q(p)=0\) 的点，有

\[
 \boxed{|\nabla^2\Omega|^2=4|V|^2-6|\eta|^2.}
\]

使用经典适配标架

\[
 \nabla\Omega=a\otimes\phi-Ja\otimes J\phi,\qquad q=4|a|^2,
\]

将零点处 \(L(X)=(\nabla_Xa)^\sharp\) 写成复线性与反复线性部分，完整形式为

\[
 \boxed{L(z)=cz+A\bar z,\qquad \operatorname{tr}(A\bar A)=-8|c|^2.}
\]

这里 \(\bar A\) 是逐元素共轭，不是共轭转置。于是

\[
 |\eta|^2=8|c|^2,
\]
\[
 \boxed{|V|^2-4|\eta|^2=4\|\operatorname{Sym}A\|_F^2\ge0,}
\]
\[
 \boxed{\det_{\mathbb R}L=9|c|^4+|\det_{\mathbb C}A|^2
 \ge25|c|^4=\frac{25}{64}|\eta|^4.}
\]

因此，**在扭率零点处，只要横向 Weyl 分量不为零，零点就必定孤立、横截，局部指数为 +1。** 若零点退化，则 \(\eta=0\)，且扭率的一阶导数实秩只能是 0 或 2。

若闭流形上的全部扭率零点横截，则

\[
 \boxed{\#\{N_J=0\}=5\chi(M)+6\tau(M).}
\]

此处按 Nijenhuis 丛的复取向计数。它不是对任意退化零集的计数公式。

## 2. 关键推导

非负 Laplacian 约定为 \(\Delta=-\operatorname{div}\nabla\)。经典方程为

\[
 \nabla^*\nabla\Omega=2W^+\Omega-\frac{s}{3}\Omega,
\]
\[
 \nabla^*\nabla W^++\frac{s}{2}W^+-6(W^+)^2+2|W^+|^2I=0.
\]

在扭率零点，\(\nabla n=0\)、\(t=s/6\)、\(\nabla^*\nabla n=\sqrt2\eta\)。直接两次微分 \(t=\langle W^+n,n\rangle\) 得

\[
 \Delta t=3|\eta|^2-2|V|^2.
\]

另一方面，\(\Delta q=4\Delta t=-2|\nabla^2\Omega|^2\)，得到第一条零点恒等式。

Einstein 条件使曲率保持两手性。标架曲率方程

\[
 da-Ja\wedge b=-\mathcal R(J\phi),\qquad
 d(Ja)+a\wedge b=-\mathcal R(\phi)
\]

在 \(a=0\) 处说明 \(da,d(Ja)\) 都自对偶。它们对 \(\nabla a\) 提供六条独立实线性约束，解空间恰好是 \(cz+A\bar z\)。范数计算把零点恒等式化为 \(\operatorname{tr}(A\bar A)=-8|c|^2\)。

随后使用实线性复表示的行列式公式

\[
 \det_{\mathbb R}(cI+A\mathsf C)
 =|c|^4-|c|^2\operatorname{tr}(A\bar A)+|\det A|^2
\]

以及 \(\operatorname{tr}(A\bar A)\ge-2|\det A|\)，即得正行列式和定量下界。全文写出了完整十实参数矩阵及所有收缩。

## 3. 与闭 Goldberg 目标的关系

项目已有的经典拓扑论证只要求闭候选必须具有扭率零点。本轮继续确定了这个零点的首阶几何。

这里不能从“有一个零点”直接进入唯一延拓：若该点 \(\eta\ne0\)，导数反而非退化。这个命题是对真实解的必要条件；并未构造具有这样的零点的负 Einstein 局部解。矩阵的代数可实现不等于完整 PDE 可实现。

正指数也没有给出闭流形矛盾，因为非零标量 Einstein 情形的

\[
 5\chi+6\tau=\chi+2(2\chi+3\tau)>0.
\]

所以一般闭负 Goldberg 仍未由本稿解决。若能从完整闭流形方程证明 \(\eta\equiv0\)，则可接 AAD 的第三 Gray 条件可积性定理；本稿没有证明该全局消失。

## 4. 保留散度项的点态恒等式

令 \(\theta(X)=\langle\eta,\nabla_X\Omega\rangle\)，则

\[
 \boxed{\frac14\Delta q+2\operatorname{div}\theta^\sharp+\frac{s}{8}q+\frac{3}{16}q^2+|\eta|^2+2|V|^2=0.}
\]

上式的 `theta^sharp` 表示该一形式的度量对偶向量场。对闭流形积分后，它恢复项目已经有的积分平衡，不是另一条独立的正性预算。在扭率零点，虽然 \(\theta=0\)，仍有 \(\operatorname{div}\theta^\sharp=-2|\eta|^2\)。不能按点删除这一项。

## 5. 来源与计算

经典输入：AAD《Local models and integrability of certain almost Kähler 4-manifolds》中的适配标架方程；Derdziński 的 Weyl–Weitzenböck 公式；Nijenhuis 丛的经典陈类计算。项目输入用于比较已有状态与显式模型，不参与本稿局部定理的上游证明。

新增推导集中在零点二阶恒等式、完整复线性分解、行列式与指数的连接。没有完成全领域优先性比较，不将这些推论称为已确定的首次发现。

`verify_zero_structure.py` 已运行，精确检查了六条线性约束、十维解空间、范数与行列式公式、代数等号数据，并在系统的有理非紧实例上复核完整散度恒等式，残差为零。它不证明任意形式零点数据存在实际度量。

LaTeX 主文件 `Q4_Torsion_Zero_Structure.tex` 可独立编译。对应 PDF 六页。

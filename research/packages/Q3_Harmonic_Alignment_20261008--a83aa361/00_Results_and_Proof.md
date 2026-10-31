# Q3：谐和通量等号支的真实下降方向

2026年10月8日。

## 1. 本轮结论

固定原目标：寻找光滑闭四流形上的非 Bach-flat 全局
\(P(g)=\int|\operatorname{Ric}^\circ_g|^2\) 极小元。

本轮从新稿的谐和通量等号结构和经典变分公式推出：若闭四维度量是常标量的 almost-Kähler 度量，且 Ricci 张量关于其几乎复结构不变，则

\[
\boxed{DP_g[Z]=-\frac{s}{2}P(g),\qquad Z=\operatorname{Ric}^\circ_g.}
\]

所以当 \(s\ne0\)、\(P>0\) 时，存在显式保持体积形式的下降路径

\[
g_t(X,Y)=g\bigl(e^{t\operatorname{sgn}(s)Z^\sharp}X,Y\bigr),
\qquad
P(g_t)=P(g)-\frac{|s|}{2}P(g)t+O_g(t^2).
\]

它不需要 Kähler 可积性、非零谐和形式无零点、谱隙或局部对称性。路径不必继续 almost-Kähler：目标泛函是在全部光滑度量上极小化。

结合系统新增的“常标量谐和通量等号结构”定理，可排除整个非 Einstein 等号支作为 Q3 极小元。这里不必先解决该支上的负 Blair–Ianus 可积性问题。尚未证明 Godeaux 单吹起上的光滑取得性，也没有由此给出 Q3 的完整实例。

## 2. 范数与经典变分

二形式使用形式范数，\(|e^{12}+e^{34}|^2=2\)；二形式同时视为反对称端同态，组合产生对称张量。Weyl 取曲率算子范数。令

\[
\mathscr R(H,H)=R_{ikjl}H^{ij}H^{kl},\qquad R_{ikjl}g^{kl}=\operatorname{Ric}_{ij}.
\]

粗 Laplacian \(\nabla^*\nabla\) 与标量 Laplacian \(\Delta_0=d^*d\) 取非负规范。由 Gursky–Viaclovsky 的两条梯度公式，在常标量度量上

\[
\mathcal G_P=\nabla^*\nabla Z-2\mathscr R(Z)+\frac12|Z|^2g.
\]

故对基点处固定的方向 \(Z\)，

\[
DP_g[Z]=\int\bigl(|\nabla Z|^2-2\mathscr R(Z,Z)\bigr).
\tag{1}
\]

这个导数不是对沿路径重新选择的实际解求导。度量范数和体积的变化已经包含在经典梯度中。

## 3. 相反手性调和形式的精确配对

设 \(\phi\in\Omega^+\)、\(\psi\in\Omega^-\) 均为光滑调和二形式，且

\[
Z=\phi\circ\psi,\qquad f=|\phi|^2,\quad h=|\psi|^2.
\]

相反手性二形式的组合满足

\[
|Z|^2=fh,
\]

\[
|\nabla Z|^2=h|\nabla\phi|^2+f|\nabla\psi|^2
+\frac12\langle df,dh\rangle,
\tag{2}
\]

\[
\mathscr R(Z,Z)
=h\langle W^+\phi,\phi\rangle
+f\langle W^-\psi,\psi\rangle-\frac{s}{12}fh.
\tag{3}
\]

在一点将二形式写为 \(\phi=a(e^{12}+e^{34})\)、\(\psi=b(e^{12}-e^{34})\)，则 \(Z=ab\operatorname{diag}(-1,-1,1,1)\)。式(3)由六个截面曲率的组合直接得到；其中无迹 Ricci 曲率块精确相消，并没有假设度量 Einstein。

调和二形式的 Weitzenböck 公式给

\[
|\nabla\phi|^2
=2\langle W^+\phi,\phi\rangle-\frac{s}{3}f-\frac12\Delta_0f,
\]

\[
|\nabla\psi|^2
=2\langle W^-\psi,\psi\rangle-\frac{s}{3}h-\frac12\Delta_0h.
\]

将两式代入(2)，再减去两倍(3)并在闭流形上积分，即得

\[
\boxed{
DP_g[Z]=-\frac{s}{2}P(g)
-\frac12\int\langle d|\phi|^2,d|\psi|^2\rangle.
}
\tag{4}
\]

两种 Weyl 曲率在这个完整组合中消失，余下的是标量项和两种幅度的梯度配对。

## 4. almost-Kähler、Ricci 不变情形的闭合

设 \(\Omega\) 是 almost-Kähler 形式，\(|\Omega|^2=2\)，并令其端同态为 \(J\)。因为 \(Z\) 对称、无迹且与 \(J\) 交换，

\[
\psi=-JZ^\sharp\in\Lambda^-,\qquad Z=\Omega\circ\psi.
\]

\(d\Omega=0\) 与自对偶性使 \(\Omega\) 调和。相反手性乘积的散度式给

\[
\operatorname{div}(\Omega\circ\psi)=\Omega(d^*\psi).
\]

常标量条件与 contracted Bianchi 使左边为零；\(J\) 可逆，故 \(d^*\psi=0\)。由反自对偶性，又有 \(d\psi=0\)。因此 \(\psi\) 是全局光滑调和形式，不需要除以它的模长。

式(4)中的第一个幅度恒为2，梯度配对消失，得到本轮主式。路径 \(g_t=g(e^{t\operatorname{sgn}(s)Z^\sharp}\cdot,\cdot)\) 正定且行列式不变，因为 \(\operatorname{tr}Z=0\)。其一阶导数严格负，给出真正的竞争度量。

还得到

\[
\boxed{\|\mathcal G_P\|_{L^2}\ge\frac{|s|}{2}\sqrt{P(g)}.}
\]

这是一条对显示结构内的每个度量成立的全局梯度下界；没有将其扩大到一般未对齐的度量。

## 5. 如何接入最新稿的等号结构

新稿的定义为

\[
\mathfrak F_h=\sqrt2\int|B^*h|,
\qquad L_h=\frac{P/2-\mathfrak F_h^2/\|h\|_2^2}{4\pi^2}\ge0.
\]

其等号结构定理已证明：常标量且 \(L_h=0\) 时，度量或者 Einstein，或者具有上述全局 almost-Kähler、Ricci 不变结构。故

\[
\boxed{s\ne0,\ P>0,\ L_h=0
\quad\Longrightarrow\quad \text{不是全部度量上的局部 }P\text{ 极小元}.}
\]

在 \(s=-4\) 时，下降方向就是 \(-Z\)，且 \(DP[-Z]=-2P\)。即使希望竞争者继续具有常负标量，也可在下降后取相应负 Yamabe 代表，\(P\) 不增加。

假如 Godeaux 单吹起的 \(P_*\) 确实被光滑度量 \(g_*\) 取得，则它必须满足

\[
\min_{h\in\mathcal H^-(g_*),\ \|h\|_2=1}L_h(g_*)>0.
\]

证明只用每一个 \(L_h>0\)、固定有限维单位球的紧性和函数连续性。这个正数依赖 \(g_*\)，不提供退化序列上的统一下界。

此外，任一光滑闭 \(P\)-临界度量的标量为常数；若其具备上述 almost-Kähler、Ricci 不变结构，非零标量分支必为 Einstein。零标量分支由 \(P=(\int|\mathrm{Ric}|^2-\tfrac13\int s^2)+\tfrac1{12}\int s^2\) 的梯度关系必 Bach-flat。因此这整个结构类都不能提供 Q3 所需的非 Bach-flat 全局极小元。

## 6. 未消失的精确信息

只要求较弱的全局调和乘积 \(Z=\phi\circ\psi\)，不要求其中一项等长时，负标量临界度量仍须满足

\[
\int\langle d|\phi|^2,d|\psi|^2\rangle=|s|P>0.
\]

它允许非恒幅度的正相关，因此不能删去这个项后宣布整个 Einstein–Maxwell 类都被排除。

本轮排除的是最新等号分支，不是所有未对齐的候选；也没有证明极小化序列必须进入等号分支。单个零模式 ALE、其他泡以及部分塌缩仍与取得性有关。真正的 Q3 终点依旧是一个光滑全局取得性证明。

## 来源

1. M. T. Gursky and J. A. Viaclovsky, *Rigidity and stability of Einstein metrics for quadratic curvature functionals*, arXiv:1105.4648v2, equations (2.5), (2.9).
2. 用户提供的 `03_Subsequent_Mathematical_Developments(1).tex`，谐和通量等号定理、较弱秩一结构、局部校正泛函。
3. 前一轮 `Q3_Global_Period_Constraints.tex`，固定 Godeaux 单吹起、经典下界和系统严格构造。

配套 `check_identities.py` 检查相反手性乘积的等距关系、曲率收缩、梯度交叉项，以及曲面乘积上的变分符号。分析证明在上文与英文 LaTeX 中完整列出。

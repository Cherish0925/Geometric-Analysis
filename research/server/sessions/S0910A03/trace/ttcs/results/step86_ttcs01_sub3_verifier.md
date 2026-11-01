# TTCS Independent Branch Record

```json
{
  "step_id": 86,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/scripts/step85_bochner_comparison.py",
    "Sessions/S0910A03/trace/ttcs/results/step85_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Independently audit and derive the forced superlevel Caccioppoli inequality for e=|dU|^2 on the OT weighted base. Start with 1/2 Le=|DdU|^2+div_sigma V-|F|^2+Q-3e+(1/2)|dU(grad sigma)|^2+E_B:A, V(X)=<dU(X),F>, Q>=e^2/2. Test with eta^2 u, u=(e-k)_+, k>=6, and retain -int eta^2<V,grad u> as well as the cutoff term. Use Kato |grad e|<=2 sqrt(e)|DdU| and pointwise |F|,|E_B| controlled by the full operator Ricci defect to obtain the sharpest valid inequality without assuming u small. Then assess whether CD(-(3+delta),4), normalized doubling/Poincare/Sobolev on buffered balls, and this inequality genuinely imply any universal interior upper bound below 12 when exit e is small. Check locality, boundary, volume normalization, and whether Moser needs an independent local L2/L1 seed. If a proposed universal ceiling is false, construct the simplest scalar weak/PDE model exhibiting the failure mechanism while respecting the inequality's sign structure.

## Output

# 科学核验备忘：强迫情形的超水平 Caccioppoli 公式

记
\[
d\mu=e^\sigma\,d\operatorname{vol}_{\gamma_B},\qquad
e=|dU|^2,\qquad
D_k=\{e>k\},\qquad
u=(e-k)_+,\quad k\ge 6.
\]
以下积分均相对于 \(d\mu\)。令 \(\eta\) 为 Lipschitz 截断函数；先假设其支撑位于域内。

## 1. 精确分部积分：两个 \(V\) 项都必须保留

从
\[
\frac12Le
=
|DdU|^2+\operatorname{div}_\sigma V-|F|^2+Q(A)-3e
+\frac12|dU(\nabla\sigma)|^2+E_B:A
\]
及
\[
Q(A)\ge \frac12e^2
\]
得到
\[
Q(A)-3e\ge W(e),\qquad
W(e):=\frac12e(e-6).
\]

在 \(D_k\) 上 \(\nabla u=\nabla e\)，且
\[
\frac12\int\eta^2uLe
=
-\frac12\int\eta^2|\nabla u|^2
-\int\eta u\langle\nabla\eta,\nabla u\rangle .
\]
关键的散度项是
\[
\boxed{
\int\eta^2u\,\operatorname{div}_\sigma V
=
-\int\eta^2\langle V,\nabla u\rangle
-2\int\eta u\langle V,\nabla\eta\rangle .
}
\]
因此，舍去 \(\frac12u|dU(\nabla\sigma)|^2\ge0\) 后，
\[
\boxed{
\begin{aligned}
&\frac12\int_{D_k}\eta^2|\nabla u|^2
+\int_{D_k}\eta^2u|DdU|^2\\
&\quad
+\int_{D_k}\eta^2u
\bigl[W(e)+E_B:A-|F|^2\bigr]\\
&\le
\int_{D_k}\eta^2\langle V,\nabla u\rangle
+2\int_{D_k}\eta u\langle V,\nabla\eta\rangle
-\int_{D_k}\eta u\langle\nabla\eta,\nabla u\rangle .
\end{aligned}}
\tag{1}
\]

脚本 `step85_bochner_comparison.py` 中的 `integrated_ibp` 使用测试函数 \(\eta^2\)，该公式本身成立，但它不是超水平测试 \(\eta^2u\)。后者多出
\[
-\int\eta^2\langle V,\nabla u\rangle,
\]
不能省略。由于这一项没有因子 \(u\)，它正是强迫情形中最重要的项。

## 2. 由完整 Ricci 误差得到的点态估计

设
\[
|F|\le \bar f,\qquad
\|E_B\|_{\rm op}\le \bar b.
\]
由 \(A\ge0\) 且 \(\operatorname{tr}A=e\)，
\[
E_B:A\ge-\bar b\,e.
\]
同时
\[
|V|^2
=\sum_i|\langle dU(e_i),F\rangle|^2
\le e\,|F|^2
\le \bar f^2e.
\]

如果完整四维 Ricci 误差满足
\[
\|\operatorname{Ric}_g+3g\|_{\rm op}\le\delta,
\]
则可写
\[
\bar b=C_B\delta,\qquad \bar f=C_F\delta.
\]
当前材料没有给出 \(C_B,C_F\) 在所用 \(\mathbb H^2\) 归一化下的数值，因此任何显式 \(\delta\) 数值都还依赖这两个常数的张量换算。

定义
\[
\Psi(e):=\frac12e(e-6)-\bar b\,e-\bar f^2.
\tag{2}
\]
则 (1) 给出
\[
\begin{aligned}
&\frac12\int\eta^2|\nabla u|^2
+\int\eta^2u|DdU|^2
+\int\eta^2u\Psi(e)\\
&\le
\int\eta^2\langle V,\nabla u\rangle
+2\int\eta u\langle V,\nabla\eta\rangle
-\int\eta u\langle\nabla\eta,\nabla u\rangle .
\end{aligned}
\tag{3}
\]

## 3. Kato 后的最紧 Caccioppoli 形式

Kato 不等式给出
\[
|\nabla e|\le2\sqrt e\,|DdU|,
\]
故在 \(D_k\) 上
\[
u|DdU|^2\ge\frac{u}{4e}|\nabla u|^2.
\]
于是梯度的总系数为
\[
a_k(e):=\frac12+\frac{u}{4e}
=\frac{3e-k}{4e},
\qquad
\frac12\le a_k(e)<\frac34.
\tag{4}
\]

将两个含 \(\nabla u\) 的项合并：
\[
\eta^2V\cdot\nabla u-\eta u\nabla\eta\cdot\nabla u
=
\eta(\eta V-u\nabla\eta)\cdot\nabla u.
\]
对任意 \(0<\theta<1\)，点态 Young 不等式给出
\[
\boxed{
\begin{aligned}
&(1-\theta)\int_{D_k}a_k(e)\eta^2|\nabla u|^2
+\int_{D_k}\eta^2u\Psi(e)\\
&\le
\frac1{4\theta}\int_{D_k}
a_k(e)^{-1}|\eta V-u\nabla\eta|^2
+2\int_{D_k}\eta u\langle V,\nabla\eta\rangle .
\end{aligned}}
\tag{5}
\]
这是仅使用现有点态信息时较紧的形式。进一步取绝对值：
\[
\boxed{
\begin{aligned}
&(1-\theta)\int a_k\eta^2|\nabla u|^2
+\int\eta^2u\Psi(e)\\
&\le
\frac1{4\theta}\int a_k^{-1}
\bigl(\eta\bar f\sqrt e+u|\nabla\eta|\bigr)^2
+2\int\eta u\bar f\sqrt e\,|\nabla\eta|.
\end{aligned}}
\tag{6}
\]

取 \(\theta=\frac12\)，利用 \(a_k\ge\frac12\)，可得较方便但稍弱的版本：
\[
\boxed{
\frac14\int\eta^2|\nabla u|^2
+\int\eta^2u\Psi(e)
\le
3\int\left(
\eta^2\bar f^2e+u^2|\nabla\eta|^2
\right).
}
\tag{7}
\]

这里的源项是
\[
\bar f^2e\,\mathbf1_{\{e>k\}},
\]
不是 \(u\bar f^2\)。在 \(u\downarrow0\) 时它仍然存在。若改用
\[
|V||\nabla u|
\le2\bar f e|DdU|
\le\varepsilon u|DdU|^2
+C_\varepsilon\frac{\bar f^2e^2}{u},
\]
右侧在集合 \(\{e=k\}\) 附近奇异，不能作为一般的超水平估计。公式 (5)–(7) 避免了这一问题，也未假设 \(u\) 很小。

## 4. 吸收多项式及自然根值

\(\Psi\) 的正根为
\[
\boxed{
k_*=
3+\bar b+\sqrt{(3+\bar b)^2+2\bar f^2}.
}
\tag{8}
\]
故 \(k\ge k_*\) 时，\(\Psi(e)\ge0\) 于 \(D_k\)。当
\(\bar b=C_B\delta,\ \bar f=C_F\delta\) 时，
\[
k_*
=
6+2C_B\delta+\frac{C_F^2}{3}\delta^2+O(\delta^3).
\]

令
\[
S=\sqrt{(3+\bar b)^2+2\bar f^2},\qquad
k_-=3+\bar b-S.
\]
则
\[
\Psi(e)=\frac12(e-k_*)(e-k_-).
\]
特别地，对 \(k=k_*\)、\(u=e-k_*\)，
\[
\boxed{
u\Psi(e)=S\,u^2+\frac12u^3.
}
\tag{9}
\]
因此吸收项同时控制 \(u^2\) 和 \(u^3\)。

若出口满足 \(e<k_*\)，并且中心反射给出光滑加倍，则全域测试 \(\eta\equiv1\) 可用。由 (5) 取 \(\theta=\frac12\)，
\[
\boxed{
\frac14\int|\nabla u|^2
+S\int u^2+\frac12\int u^3
\le
\bar f^2\int_{\{u>0\}}(k_*+u).
}
\tag{10}
\]
再用
\[
\bar f^2u\le\frac S2u^2+\frac{\bar f^4}{2S},
\]
得到
\[
\boxed{
\frac14\int|\nabla u|^2
+\frac S2\int u^2+\frac12\int u^3
\le
\left(\bar f^2k_*+\frac{\bar f^4}{2S}\right)
\mu(\{u>0\}).
}
\tag{11}
\]
这是严格的全域积分控制，但它本身还不是点态上界。

## 5. \(CD(-(3+\delta),4)\) 的核算

对
\[
L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle
\]
而言，有效维数 \(4\) 的 Bakry–Émery 张量为
\[
\operatorname{Ric}_{L,4}
=
\operatorname{Ric}_B-\nabla^2\sigma-\frac12d\sigma\otimes d\sigma.
\]
利用基底方程，
\[
\operatorname{Ric}_{L,4}
=
-3\gamma_B+\frac12A+E_B.
\]
由于 \(A\ge0\)，
\[
\operatorname{Ric}_{L,4}\ge-(3+\bar b)\gamma_B.
\]
因此准确写法是
\[
CD(-(3+\bar b),4);
\]
只有在 \(\bar b\le\delta\) 时才可直接写成 \(CD(-(3+\delta),4)\)。

在完全位于域内的缓冲球上，这给出归一化倍增、Poincaré 和局部 Sobolev 不等式；有效维数 \(4\) 对应 \(W^{1,2}\to L^4\)。常数还依赖球半径以及
\(\sqrt{3+\bar b}\,R\)。

## 6. 这些材料尚未给出 \(e<12\) 的普适点态结论

现有公式产生了三类不同信息：

1. **全域超水平积分量。**  
   出口小于 \(k_*\) 时，(11) 控制全域的 \(L^2\)、\(L^3\) 和 Dirichlet 能量。

2. **缓冲球上的局部正则估计。**  
   标准 Moser 或 De Giorgi 过程通常给出结构形如
   \[
   \operatorname*{ess\,sup}_{B_r}u
   \le
   C\left[
   \left(\fint_{B_R}u^2\right)^{1/2}
   +\text{强迫项与截断尺度项}
   \right].
   \]
   因而需要较大球上的归一化 \(L^2\) 或 \(L^1\) 输入。公式 (11) 控制的是全域积分；它不能自动控制每个缓冲球上的
   \(\fint_{B_R}u^2\)，因为该球可能只占全域加权体积的极小部分。

3. **出口信息的传播。**  
   出口 \(e\) 小使全域超水平测试没有外缘通量，但一个远离出口的球并不直接看到该数据。把出口信息传至中心需要全域 Sobolev 常数、Green 核估计、超水平连通分量的统一估计，或带显式衰减率的逐球传播。局部 \(CD\) 数据并未提供这些全域常数；长 connector 上逐球常数还会累积。

加权测度乘以常数不会改变 \(L\)，也只会把 Caccioppoli 两侧同时乘以同一因子。归一化 Sobolev 形式消除了这一任意缩放，但不会产生局部 \(L^2\) 输入。并且 \(CD\) 下允许加权体积塌缩，不能把未归一化欧氏 Sobolev 常数当作统一常数使用。

因此，当前材料严格支持 (5)–(11)，但“局部 \(CD\)+归一化 Sobolev+Caccioppoli”本身还不能推出与 connector 长度、缓冲宽度和局部均值无关的
\[
\sup e\le6+C\delta<12.
\]
另一个保留吸收项 \(Su^2+\frac12u^3\) 的全域非线性论证仍有可能得到这种结果；现有文件中没有该论证及其显式常数。

## 7. 标量模型：截断项与尺度为何不可省略

取二维欧氏球 \(B_R\)，令 \(\sigma=0\)、\(E_B=0\)，并固定
\[
e\equiv H>6,\qquad
W_H=\frac12H(H-6),\qquad W_H>f^2.
\]
定义
\[
V(x)=-\frac{W_H-f^2}{2}\,x.
\]
于是
\[
\operatorname{div}V=-(W_H-f^2)
\]
且
\[
\frac12\Delta e
=
\operatorname{div}V-f^2+W_H
=0.
\]
若
\[
R\le\frac{2f\sqrt H}{W_H-f^2},
\]
则
\[
|V|\le f\sqrt H=f\sqrt e.
\]
该欧氏模型满足 \(CD(0,4)\) 及所有归一化局部几何不等式，但 \(H\) 可任意大，只需相应缩小 \(R\)。测试 \(\eta^2(H-k)\) 时，
\[
(H-k)(W_H-f^2)\int\eta^2
=
2(H-k)\int\eta\langle V,\nabla\eta\rangle.
\]
也就是说，正的二次反应项恰由
\[
2\int\eta u\langle V,\nabla\eta\rangle
\]
平衡。若省略该截断项，就会得到不成立的局部 ceiling。

这个模型只使用了 Caccioppoli 推导中实际采用的结构
\[
|V|\le f\sqrt e,
\]
并不构成带小出口的完整 OT connector。它严格说明：归一化倍增、Poincaré、Sobolev 与局部强迫估计不能产生一个与球半径及外层数据无关的绝对点态上界。完整低出口陈述的真值还取决于出口到内部的全域传播机制。

## 结论

- 强迫超水平公式的核心是 (5)；(7) 是方便使用的统一版本。
- \(-\int\eta^2\langle V,\nabla u\rangle\) 与截断项
  \(-2\int\eta u\langle V,\nabla\eta\rangle\) 都不可省略。
- 自然能量根值是 \(k_*=6+O(\delta)\)，且在 \(k=k_*\) 处有精确吸收
  \(Su^2+\frac12u^3\)。
- 小出口数据给出全域积分估计 (11)，但现有局部几何信息尚未把它转化为统一的 \(L^\infty\) ceiling，更没有给出显式低于 \(12\) 的数值。
- 所缺的数学内容是带明确常数的全域非线性 De Giorgi/Moser 推导、统一 Green 核估计，或从出口到中心的定量传播公式。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 86,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step86_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step86_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently audit and derive the forced superlevel Caccioppoli inequality for e=|dU|^2 on the OT weighted base. Start with 1/2 Le=|DdU|^2+div_sigma V-|F|^2+Q-3e+(1/2)|dU(grad sigma)|^2+E_B:A, V(X)=<dU(X),F>, Q>=e^2/2. Test with eta^2 u, u=(e-k)_+, k>=6, and retain -int eta^2<V,grad u> as well as the cutoff term. Use Kato |grad e|<=2 sqrt(e)|DdU| and pointwise |F|,|E_B| controlled by the full operator Ricci defect to obtain the sharpest valid inequality without assuming u small. Then assess whether CD(-(3+delta),4), normalized doubling/Poincare/Sobolev on buffered balls, and this inequality genuinely imply any universal interior upper bound below 12 when exit e is small. Check locality, boundary, volume normalization, and whether Moser needs an independent local L2/L1 seed. If a proposed universal ceiling is false, construct the simplest scalar weak/PDE model exhibiting the failure mechanism while respecting the inequality's sign structure.

## Integrated Scientific Memo

# 强迫超水平 Caccioppoli 核验

令
\[
d\mu=e^\sigma d\mathrm{vol}_{\gamma_B},\qquad
e=|dU|^2,\qquad u=(e-k)_+,\quad k\ge6,
\]
并记 \(D_k=\{e>k\}\)。设
\[
|F|\le f,\qquad \|E_B\|_{\mathrm{op}}\le b.
\]
若这些量来自完整算子 Ricci 缺陷 \(\|\mathrm{Ric}_g+3g\|_{\mathrm{op}}\le\delta\)，则只能在已核准张量换算后写
\[
f=C_F\delta,\qquad b=C_B\delta;
\]
现有材料未给出 \(C_F,C_B\) 的精确值，故不能无条件把它们都替换为 \(\delta\)。

## 1. 精确弱形式与符号

从
\[
\frac12Le=|DdU|^2+\operatorname{div}_\sigma V-|F|^2+Q-3e
+\frac12|dU(\nabla\sigma)|^2+E_B:A,
\quad V(X)=\langle dU(X),F\rangle ,
\]
以及 \(Q\ge \frac12e^2\)，以 \(\eta^2u\) 测试。若 \(\eta\) 紧支于内部，则
\[
\int\eta^2u\,\operatorname{div}_\sigma V
=
-\int\eta^2\langle V,\nabla u\rangle
-2\int\eta u\langle V,\nabla\eta\rangle .
\]
因此
\[
\begin{aligned}
&\frac12\int_{D_k}\eta^2|\nabla u|^2
+\int_{D_k}\eta^2u|DdU|^2\\
&\quad+\int_{D_k}\eta^2u
\left[\frac12e(e-6)+E_B:A-|F|^2\right] \\
&\le
\int_{D_k}\eta^2\langle V,\nabla u\rangle
+2\int_{D_k}\eta u\langle V,\nabla\eta\rangle
-\int_{D_k}\eta u\langle\nabla\eta,\nabla u\rangle .
\end{aligned}
\tag{1}
\]
这里要求保留的两项确实都存在：

* \(-\int\eta^2\langle V,\nabla u\rangle\) 是散度分部积分中的超水平项；
* \(-2\int\eta u\langle V,\nabla\eta\rangle\) 是截断项。

它们在把散度项移到 (1) 右侧后分别变成正号。仅用测试函数 \(\eta^2\) 得到的源文件公式不能替代此超水平公式。

若截断碰到真实边界，还必须加入
\[
B_\partial
=\frac12\int_{\partial\Omega}\eta^2u\,\partial_\nu e\,d\mu_\partial
-\int_{\partial\Omega}\eta^2u\,V(\nu)\,d\mu_\partial .
\tag{2}
\]
中心只有在所有数据均可光滑反射加倍时才不是边界；“形式 Neumann 条件”本身不够。出口处若 \(u=0\)，则 (2) 消失。

## 2. 点态缺陷控制与最稳健的 Caccioppoli 形式

由 \(A\ge0\)、\(\operatorname{tr}A=e\)，
\[
E_B:A\ge-be,\qquad |V|\le f\sqrt e.
\]
定义
\[
\Psi(e)=\frac12e(e-6)-be-f^2.
\tag{3}
\]
则 (1) 蕴含
\[
\begin{aligned}
&\frac12\int\eta^2|\nabla u|^2
+\int\eta^2u|DdU|^2+\int\eta^2u\Psi(e)\\
&\le
\int\eta^2\langle V,\nabla u\rangle
+2\int\eta u\langle V,\nabla\eta\rangle
-\int\eta u\langle\nabla\eta,\nabla u\rangle .
\end{aligned}
\tag{4}
\]

Kato 不等式
\[
|\nabla e|\le2\sqrt e\,|DdU|
\]
在 \(D_k\) 上给出
\[
u|DdU|^2\ge\frac{u}{4e}|\nabla u|^2.
\]
故总梯度系数可精确取为
\[
a_k(e)=\frac12+\frac{u}{4e}
=\frac{3e-k}{4e}\in\left[\frac12,\frac34\right).
\tag{5}
\]
将两个 \(\nabla u\) 项合并后，对任意 \(0<\theta<1\)，得到
\[
\boxed{
\begin{aligned}
&(1-\theta)\int_{D_k}a_k(e)\eta^2|\nabla u|^2
+\int_{D_k}\eta^2u\Psi(e)\\
&\le
\frac1{4\theta}\int_{D_k}a_k(e)^{-1}
|\eta V-u\nabla\eta|^2
+2\int_{D_k}\eta u\langle V,\nabla\eta\rangle .
\end{aligned}}
\tag{6}
\]
这是仅凭现有点态资料、且不假设 \(u\) 小时较紧而无奇异性的形式。进一步用 \(|V|\le f\sqrt e\)，
\[
\boxed{
\begin{aligned}
&(1-\theta)\int a_k\eta^2|\nabla u|^2+\int\eta^2u\Psi(e)\\
&\le
\frac1{4\theta}\int a_k^{-1}
\bigl(\eta f\sqrt e+u|\nabla\eta|\bigr)^2
+2\int\eta u f\sqrt e\,|\nabla\eta|.
\end{aligned}}
\tag{7}
\]
例如取 \(\theta=\frac12\)，可简化为
\[
\boxed{
\frac14\int\eta^2|\nabla u|^2+\int\eta^2u\Psi(e)
\le
3\int\bigl(\eta^2f^2e+u^2|\nabla\eta|^2\bigr).
}
\tag{8}
\]
关键是右侧源项为
\[
f^2e\,\mathbf1_{\{e>k\}},
\]
而不是 \(f^2u\)。当 \(u\downarrow0\) 时它不消失。企图用 Hessian 项直接吸收 \(V\cdot\nabla u\) 会产生 \(f^2e^2/u\)，在水平集附近奇异，因而无效。

## 3. 自然阈值及全域积分结论

\(\Psi\) 的正根为
\[
k_*=3+b+\sqrt{(3+b)^2+2f^2}.
\tag{9}
\]
因此 \(e\ge k_*\) 时 \(\Psi(e)\ge0\)。若 \(b=C_B\delta,\ f=C_F\delta\)，则
\[
k_*=6+2C_B\delta+\frac{C_F^2}{3}\delta^2+O(\delta^3).
\]
令
\[
S=\sqrt{(3+b)^2+2f^2}.
\]
在 \(k=k_*\)、\(u=e-k_*\) 时，
\[
u\Psi(e)=Su^2+\frac12u^3.
\tag{10}
\]
所以反应项确有二次及三次吸收。

若出口 \(e<k_*\)，中心又可光滑加倍，则可取全域 \(\eta\equiv1\)。由 (6) 得
\[
\boxed{
\frac14\int|\nabla u|^2+S\int u^2+\frac12\int u^3
\le f^2\int_{\{u>0\}}(k_*+u).
}
\tag{11}
\]
进而
\[
\boxed{
\frac14\int|\nabla u|^2+\frac S2\int u^2+\frac12\int u^3
\le
\left(f^2k_*+\frac{f^4}{2S}\right)\mu(\{u>0\}).
}
\tag{12}
\]
这是可靠的全域超水平积分控制，但并非点态上界。

## 4. \(CD\)、局部几何及 Moser 的实际能力

对
\[
L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle
\]
及有效维数 \(4\)，
\[
\operatorname{Ric}_{L,4}
=\operatorname{Ric}_B-\nabla^2\sigma-\frac12d\sigma\otimes d\sigma
=-3\gamma_B+\frac12A+E_B.
\]
故
\[
\operatorname{Ric}_{L,4}\ge-(3+b)\gamma_B,
\]
即准确结论是
\[
CD(-(3+b),4).
\tag{13}
\]
只有 \(b\le\delta\) 时才可写 \(CD(-(3+\delta),4)\)。

该条件在完全包含于光滑域内的缓冲球上给出归一化 doubling、Poincaré 及局部 \(W^{1,2}\to L^4\) Sobolev 不等式；常数依赖无量纲半径 \(\sqrt{3+b}\,R\)。归一化形式对 \(d\mu\mapsto c\,d\mu\) 不敏感，但不会自动制造局部能量种子。

由 (8) 进行 Moser/De Giorgi，所得结构至多是
\[
\operatorname*{ess\,sup}_{B_r}u
\le C\left[
\left(\fint_{B_R}u^2\,d\mu\right)^{1/2}
+\text{强迫和截断尺度项}
\right].
\tag{14}
\]
因此仍需独立的局部 \(L^2\) 或 \(L^1\) 种子。全域估计 (12) 不控制任意缓冲球上的归一化平均，因为该球可能占全域加权体积极小的一部分。小出口只消除了全域测试的出口通量；它不会仅凭局部 \(CD\) 将信息无损传播到远处。沿长 connector 逐球传播还可能累积常数。

此外，\(CD\) 允许加权体积塌缩；不能把未归一化欧氏 Sobolev 常数当作统一常数。若讨论轨道塌缩区，还需单独证明相应加权局部不等式，而不能仅声称 \(\rho\) 有统一上下界。

所以现有输入并不推出任何与 connector 长度、缓冲尺度及局部均值无关的
\[
\sup e\le6+C\delta<12.
\]
这不是该上界已被完整 OT 反例证伪，而是所列分析工具不足以推出它。

## 5. 最简严格标量局部反例

取二维欧氏球 \(B_R\)，\(\sigma=0\)，令
\[
e\equiv H>6,\qquad W_H=\frac12H(H-6),
\]
选 \(0<f^2<W_H\)，并定义
\[
V(x)=-\frac{W_H-f^2}{2}\,x.
\]
则
\[
\operatorname{div}V=-(W_H-f^2),
\qquad
\frac12\Delta e
=\operatorname{div}V-f^2+W_H=0.
\tag{15}
\]
若
\[
R\le \frac{2f\sqrt H}{W_H-f^2},
\tag{16}
\]
则
\[
|V|\le f\sqrt H=f\sqrt e.
\]
该模型满足 \(CD(0,4)\)、归一化局部 doubling/Poincaré/Sobolev，并完全尊重弱公式中的符号结构；\(H\) 可任意大，只需相应缩小球半径。测试 \(\eta^2(H-k)\) 时，
\[
(H-k)(W_H-f^2)\int\eta^2
=
2(H-k)\int\eta\langle V,\nabla\eta\rangle,
\]
即正反应项恰由必须保留的 cutoff 项平衡。因而这些局部假设不能产生与半径和外层数据无关的绝对 ceiling。

这是最稳妥的反例：它严格否定“局部 Caccioppoli+\(CD\)+归一化 Sobolev 自动给普适上界”的推断，但不冒充具有小出口的完整 OT connector。仅凭 \(|V|\le f\sqrt e\) 构造带小出口的全域尖峰还需验证弱不等式及边界层，现有材料未完成这一点。

## 结论

1. 正确的强迫超水平估计是 (6)，方便版本是 (8)；两个 \(V\) 项和真实边界通量都不可遗漏。
2. 自然阈值为 \(k_*=6+O(\delta)\)，在该阈值有精确吸收 \(Su^2+\frac12u^3\)。
3. 小出口给出 (11)–(12) 的全域积分控制，但不能单靠局部 \(CD\) 与归一化 Sobolev 转化成普适 \(L^\infty\) ceiling。
4. Moser 确实需要独立的局部 \(L^2/L^1\) 种子，或等价的全域传播机制、统一 Green 核/超水平分量控制。
5. 现阶段精确未决对象是：能否利用全域几何和吸收项，把 (12) 升级为长度一致的局部平均控制；或者能否从额外的 \(DF\) 正则性得到更强点态源控制。仅有 \(C^0\) Ricci 缺陷尚不足以完成这一步。
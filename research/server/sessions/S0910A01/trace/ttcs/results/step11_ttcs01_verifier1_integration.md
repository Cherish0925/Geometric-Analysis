# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 11,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step11_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step11_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Pontryagin localization mechanism for the four-dimensional negative-branch Yau 26 program.

1. VERIFY THE PONTRYAGIN DENSITY FORMULA: For a 4-manifold with curvature decomposition Rm = W⁺ + W⁻ + E + s, what is p₁(Λ²₊) as an integrand? Specifically, verify that on a region of regular fibered collapse (fiber dim d ≥ 1, base dim ≤ 3) where the self-dual forms are 'basic' (pulled back from the base), the contribution to ∫p₁(Λ²₊) = 8π²(2χ+3τ)/? vanishes or is constrained.

2. CHECK THE COUNTERMODEL: For the Taub-NUT-AdS metric with NUT parameter ν→0, verify:
   (a) The claim that the ψ-circle at distance 1/2 from the NUT is contractible in B₁.
   (b) The claim that the curvature |Rm|² remains bounded as ν→0 at fixed distance from the NUT.
   (c) Whether the maximal function bound ∫_{B_r}|Rm|² ≤ K₀·Vol(B_r) holds.

3. VERIFY THE WEITZENBÖCK COMPUTATION: For Einstein Ric=-g with calibrated W⁺ spectrum (-1/6,1/12,1/12), check that the Weitzenböck formula gives ∫|∇H|²/∫|H|² = 1 for the simple eigenform and 3/2 for the double eigenspace. Distinguish between the curvature-operator arrangement and the Weitzenböck R̃ arrangement.

4. CHECK THE DEFINITE-PAIR EXCLUSION: A03 claims flat rank ≥ 2 collapse is excluded. Verify the argument: two independent near-harmonic SD forms with locally nondegenerate Gram matrix, closedness, and constant amplitude → ∇ → 0, contradicting the Weitzenböck gradient energy. Is 'locally nondegenerate Gram matrix' automatic or an additional hypothesis?

5. ASSESS: Is the Pontryagin charge 4π²(A-k) correctly computed? Does basic collapse really contribute zero to this charge?

## Integrated Scientific Memo

# 核验结论

## 1. \(p_1(\Lambda^2_+)\) 的密度与“basic collapse”

采用材料中的曲率范数约定，
\[
8\pi^2\chi(M)=\int_M\left(
|W^+|^2+|W^-|^2-\frac12|E|^2+\frac{s^2}{24}
\right)d\mu ,
\]
\[
12\pi^2\tau(M)=\int_M\left(|W^+|^2-|W^-|^2\right)d\mu .
\]
故
\[
\boxed{
p_1(\Lambda^2_+)
=
\frac1{4\pi^2}
\left(
2|W^+|^2-\frac12|E|^2+\frac{s^2}{24}
\right)d\mu
}
\]
（取定使 \(\int p_1(\Lambda^2_+)=2\chi+3\tau\) 的定向约定）。等价地，
\[
p_1(\Lambda^2_+)
=-\frac1{8\pi^2}\operatorname{tr}(\Omega^+\wedge\Omega^+),
\]
因此
\[
\boxed{
\int_Mp_1(\Lambda^2_+)=2\chi+3\tau ,
}
\]
而未正规化的标量曲率密度满足
\[
\boxed{
\int_M\left(
2|W^+|^2-\frac12|E|^2+\frac{s^2}{24}
\right)d\mu
=4\pi^2(2\chi+3\tau).
}
\]
这澄清了 \(4\pi^2\) 与 \(8\pi^2\) 的混淆。

若规则纤维化区域
\[
\pi:U^4\to B^m,\qquad m\le3
\]
上，\(\Lambda^2_+\) 的诱导联络确实来自底空间，即
\[
\Omega^+=\pi^*\Omega_B,
\]
则
\[
\operatorname{tr}(\Omega^+\wedge\Omega^+)
=\pi^*\operatorname{tr}(\Omega_B\wedge\Omega_B)=0,
\]
因为 \(B\) 上不存在非零四形式。因此这种**联络层面的 basic collapse** 对 \(p_1(\Lambda^2_+)\) 的局部密度贡献为零。

但“自对偶形式本身从底空间拉回”不能按字面使用：若非零
\(\omega\in\Lambda^2_+\)，则
\[
\omega\wedge\omega=|\omega|^2d\mu\ne0,
\]
而若 \(\omega=\pi^*\beta\) 且 \(\dim B\le3\)，则
\[
\omega\wedge\omega=\pi^*(\beta\wedge\beta)=0.
\]
正确命题必须表述为 **\(\Lambda^2_+\) 联络或其曲率是 basic**，而不是非零 SD 二形式是普通微分形式意义下的拉回。

并且 collapse 本身不推出 basic：垂直—水平混合曲率、束扭曲、nil 结构和奇异纤维均可产生非零 Pontryagin 密度。

---

## 2. Taub–NUT–AdS 反模型

给定
\[
g_\nu=\frac{dr^2}{F_\nu}
 +(r^2-\nu^2)(d\theta^2+\sin^2\theta\,d\phi^2)
 +4\nu^2F_\nu(d\psi+\cos\theta\,d\phi)^2,
\]
\[
F_\nu(r)=\frac{r-\nu}{r+\nu}
\left(1+\frac{(r-\nu)(r+3\nu)}{3}\right).
\]

### (a) \(\psi\)-圆在 \(B_1\) 内可缩

令
\[
r=\nu+\frac{\rho^2}{8\nu}.
\]
则在 \(\rho=0\) 附近，
\[
g_\nu=
d\rho^2+\frac{\rho^2}{4}\Bigl[
d\theta^2+\sin^2\theta\,d\phi^2+
(d\psi+\cos\theta\,d\phi)^2
\Bigr]+\text{高阶项}.
\]
当 \(\psi\) 周期为 \(4\pi\) 时，这是光滑 \(\mathbb R^4\) 的 Hopf 坐标展开；\(\psi\)-轨道在 NUT 点收缩。

若 \(p_\nu\) 到 NUT 的距离为 \(1/2\)，沿径向把该轨道扫到 NUT 所得圆盘包含于 \(B_1(p_\nu)\) 中。因此
\[
\boxed{\psi\text{-圆在 }B_1(p_\nu)\text{ 中零伦。}}
\]
严格处理开球边界时，可把基点距离取为略小于 \(1/2\)，不改变结论。故该短圆不会被局部普适覆盖解开。

### (b) 固定距离环带上的曲率

在
\[
d(\,\cdot\,,\mathrm{NUT})\in[1/6,5/6]
\]
上，\(r\) 保持在远离零的统一紧区间。取正交标架
\[
e^0=\frac{dr}{\sqrt F},\quad
e^1=\sqrt{r^2-\nu^2}\,d\theta,\quad
e^2=\sqrt{r^2-\nu^2}\sin\theta\,d\phi,
\]
\[
e^3=2\nu\sqrt F(d\psi+\cos\theta\,d\phi).
\]
此环带上
\[
r^2-\nu^2\asymp r^2,\qquad F_\nu\to1+\frac{r^2}{3}.
\]
Hopf 联络的结构项为
\[
2\nu\sqrt F\,d(d\psi+\cos\theta\,d\phi)
=-2\nu\sqrt F\sin\theta\,d\theta\wedge d\phi
=O(\nu)e^1\wedge e^2.
\]
其余结构系数及所需一阶导数也统一有界。因此 Cartan 结构方程给出
\[
\boxed{
\sup_{\{d(\cdot,\mathrm{NUT})\in[1/6,5/6]\}}
|\mathrm{Rm}_{g_\nu}|\le C
}
\]
其中 \(C\) 与小参数 \(\nu\) 无关。

这是一项标架估计，而材料没有给出完整的分量列表；若后续需要可机核的反模型，仍应直接符号计算 \(\operatorname{Ric}\) 和 \(|\mathrm{Rm}|^2\)。但从给定 \(F_\nu\) 与上述统一结构系数，固定环带有界性成立。

### (c) 最大函数估计

由于
\[
B_{1/3}(p_\nu)\subset
\{d(\cdot,\mathrm{NUT})\in[1/6,5/6]\},
\]
故对所有 \(0<r\le1/3\)，
\[
\boxed{
\int_{B_r(p_\nu)}|\mathrm{Rm}|^2
\le K_0\,\operatorname{Vol}(B_r(p_\nu)),
}
\]
即
\[
\fint_{B_r(p_\nu)}|\mathrm{Rm}|^2\le K_0.
\]
所以只要 (b) 的点态界成立，(c) 立即成立。该模型确实否定“一切尺度上平均 \(L^2\) 曲率受控加 Ricci 下界会迫使局部普适覆盖非塌缩”的一般局部命题。

---

## 3. Weitzenböck 计算

Einstein 四流形上
\[
\operatorname{Ric}=\lambda g,\qquad s=4\lambda,
\]
自对偶二形式满足标准公式
\[
\boxed{
\Delta_dH=\nabla^*\nabla H-2W^+(H)+\frac{s}{3}H.
}
\]
若 \(H\) 是调和的，并处于 \(W^+\) 的 \(w\)-特征空间，则
\[
\boxed{
\frac{\int|\nabla H|^2}{\int|H|^2}
=2w-\frac{s}{3}.
}
\]
在 \(\operatorname{Ric}=-g\)、\(s=-4\) 以及
\[
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
时，
\[
w=-\frac16:\qquad
2w-\frac{s}{3}=1,
\]
\[
w=\frac1{12}:\qquad
2w-\frac{s}{3}=\frac32.
\]
因此
\[
\boxed{
\frac{\int|\nabla H|^2}{\int|H|^2}
=
1\quad\text{（单特征线）},\qquad
\frac32\quad\text{（二重特征空间）}.
}
\]

需要修正材料中的一句解释。逐指标公式中的 contraction 确实是
\[
\widetilde R(H)_{ij}=R_{ikjl}H_{kl},
\]
不能不顾约定地换成 \(R_{ijkl}\)。但在这里，限制到 \(\Lambda^2_+\) 并采用材料的约定后，
\[
\boxed{
\widetilde R|_{\Lambda^2_+}=W^++\frac{s}{12}I.
}
\]
其特征值正是
\[
-\frac12,-\frac14,-\frac14.
\]
所以“它的特征值不是通常的 \(W^++s/12\)”这一句是错误的；正确区别只在原始指标排列及投影的处理中，最终 Einstein–SD 端同一化为上述曲率算子。

---

## 4. definite-pair 排除并未成立到所声称的强度

“局部 Gram 矩阵非退化”是额外假设，不由全局线性独立自动推出。全局独立的调和形式可能有零点，也可能在某区域几乎共线；因此必须另证一个逐点或局部统一的 Gram 行列式下界。

更重要的是，即使有两个闭、自对偶、常 Gram 矩阵的形式，也一般不能仅由这些条件推出平行性。取局部正交标架
\[
(\omega_1,\omega_2,\omega_3)
\]
并写
\[
\nabla\omega_1=a\,\omega_2+b\,\omega_3,\qquad
\nabla\omega_2=-a\,\omega_1+c\,\omega_3,
\]
\[
\nabla\omega_3=-b\,\omega_1-c\,\omega_2.
\]
条件
\[
d\omega_1=d\omega_2=0
\]
给出线性约束，但仍可留下未被消去的 torsion 分量；不能推出
\(a=b=c=0\)。

若完整正交三元组都闭，
\[
d\omega_1=d\omega_2=d\omega_3=0,
\]
则可迫使 \(\Lambda^2_+\) 联络平坦、\(\nabla\omega_i=0\)。因此：

\[
\boxed{
\text{闭的 definite triple 可推出局部平行；闭的 definite pair 一般不能。}
}
\]

所以 A03 的“flat rank \(\ge2\) 已排除”必须降格为条件命题。它还需要某项额外的塌缩模型方程，例如：

* 第三个代数生成形式也渐近闭；
* 明确的平坦乘积结构直接给出近似平行；
* 或结构方程消去剩余 torsion。

只有在这些额外条件以及局部统一 Gram 非退化下，才可用
\[
\|\nabla H\|_{L^2}\to0
\]
与上述 Weitzenböck 正能量相矛盾。当前材料只严格支持完整 definite triple 的排除，而非一般 definite pair。

---

## 5. Pontryagin charge 的数值与定位含义

对单个极小一般型复曲面 \(X\)，令
\[
A=c_1^2(X)=2\chi(X)+3\tau(X).
\]
对
\[
M=X\#k\,\overline{\mathbb{CP}}^{\,2},
\]
有
\[
\chi(M)=\chi(X)+k,\qquad
\tau(M)=\tau(X)-k,
\]
从而
\[
\boxed{2\chi(M)+3\tau(M)=A-k.}
\]
故
\[
\boxed{\int_Mp_1(\Lambda^2_+)=A-k,}
\]
以及
\[
\boxed{
\int_M\left(
2|W^+|^2-\frac12|E|^2+\frac{s^2}{24}
\right)d\mu
=4\pi^2(A-k).
}
\]
在 \(k=A/3\) 时，
\[
\int p_1=\frac{2A}{3},\qquad
\int\mathcal P_+\,d\mu=\frac{8\pi^2A}{3}.
\]
因此题目所问的 \(4\pi^2(A-k)\) 作为**未正规化曲率密度积分**是正确的。

若 Ishida–LeBrun 流形含 \(m>1\) 个一般型曲面连通和，则需保留连通和修正：
\[
2\chi+3\tau
=
\sum_{j=1}^m c_1^2(X_j)-4(m-1)-k,
\]
除非文中的 \(A\) 已专门吸收该 \(-4(m-1)\) 项。故不能无条件把多块情形也写成 \(A-k\)。

在校准好区域，
\[
E\to0,\qquad s\to-4,\qquad |W^+|^2\to\frac1{24},
\]
于是未正规化 Pontryagin 密度趋于
\[
2\cdot\frac1{24}+\frac{16}{24}=\frac34.
\]
所以 bulk 上若同时满足校准缺陷很小，则该密度接近严格正值；而真正 basic 的 \(\Lambda^2_+\) 联络会使它恰为零。由此得到比“所有 charge 可集中在小坏集”更强的结论：

\[
\boxed{
\text{校准 good bulk 不能同时是严格 basic collapse。}
}
\]

若 bulk 仍塌缩，其 \(\Lambda^2_+\) 联络必须在大体积区域保留非-basic 的垂直/混合扭曲；并不一定只是奇异纤维附近携带全部 charge。Taub–NUT 的 Hopf 扭曲正是这种机制的局部模型。

不过，Pontryagin 密度含
\(-|E|^2/2\)，一般并非非负；上述正下界只在近 Einstein、近校准区域成立，不能推广到任意塌缩区。

## 最终判定

1. Pontryagin 密度和 \(4\pi^2(A-k)\) 的归一化正确，但须区分拓扑数 \(\int p_1=A-k\)。
2. basic collapse 零贡献只对 **basic \(\Lambda^2_+\) 联络曲率**成立，不对任意塌缩成立，也不能把 SD 形式字面说成低维底空间的拉回。
3. Taub–NUT–AdS 的可缩短圆与最大平均曲率反模型机制成立；固定环带曲率界可由 Cartan 标架估计得到，完整机核仍需显式曲率分量。
4. Weitzenböck 比率 \(1,3/2\) 正确；\(\widetilde R\) 最终正是 \(W^++s/12\)。
5. “definite pair 排除 flat rank \(\ge2\)”目前不成立；局部 Gram 非退化是额外假设，且即使加入它，pair 仍需额外结构方程才能推出 \(\nabla\to0\)。
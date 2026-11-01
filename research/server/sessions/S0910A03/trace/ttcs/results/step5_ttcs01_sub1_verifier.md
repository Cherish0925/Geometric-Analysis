# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step4_weyl_profile_and_bubble_restriction.tex",
    "Sessions/S0910A01/workspace/notes/step7_local_vs_global_rigidity.md",
    "Knowledge/objects/papers/Conformal-Kähler-rigidity-of-Einstein-four-manifolds--ee41ec8c511e--4518ab125268/object.md",
    "Knowledge/objects/papers/Einstein-metrics-via-Derdziński-duality--f7ddbaf86999--f2cdc1a49708/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md"
  ]
}
```

## Task

Analyze the proposed local-limit route for the fixed critical Ishida–LeBrun sequence. Starting from the exact quantitative deficit decomposition and Weyl norm profile, determine precisely what convergence on a harmonic-radius patch yields for (i) the selected Seiberg–Witten 2-form/eigenline, (ii) the W+ eigenvalue multiplicities, and (iii) the limiting Einstein metric. Check whether the nonnegative eigenvalue defect plus amplitude/Hodge projection control forces the limiting spectrum (-1/6,1/12,1/12) on a regular patch. Then check the Derdzinski consequence carefully: is this spectrum locally impossible at Ric=-g, or does it give a locally conformally Kähler noncompact model? Resolve conventions, conformal factor, scalar curvature, and Bochner formula, and identify the strongest true theorem.

## Output

# 科学核验备忘

## 1. 临界序列给出的全局趋零量

设固定 Ishida–LeBrun 临界流形上

\[
\delta_i=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_\infty\longrightarrow0,
\]

且 \(A>0\) 固定。由文稿中的 (25)–(30)，

\[
R_i=O(A\delta_i^2),\qquad
\Delta_i=O(A\delta_i^2).
\]

固定流形的符号类只有有限多个；取子列后，可令选出的类 \(a\) 不随 \(i\) 改变。对相应正则化权重 \(f_i\) 和 monopole 解，(13)–(17) 给出

\[
D_{{\rm eig},i},D_{{\rm Hodge},i},D_{{\rm amp},i},J_{A_i}\to0,
\]

以及

\[
\|f_i\varphi_i+6\sqrt2\pi H_i\|_2\to0, \qquad
\left\||2\pi H_i|-\frac{q_i}{3\sqrt2}\right\|_2\to0. \tag{1}
\]

这里 \(H_i\) 是 \(a^+\) 的调和自对偶代表，

\[
\varphi_i=\frac32\psi_i,\qquad |\psi_i|=\rho_i,\qquad
q_i=-s_i+\sqrt6\,|W^+_i|.
\]

令

\[
t_i=s_i+8\sqrt6\,|W_i^+|.
\]

由 (32) 和 Ricci 夹逼，

\[
\|t_i\|_2^2\le864\pi^2R_i\to0,\qquad
\|s_i+4\|_\infty\le4\delta_i.
\]

因此

\[
|W_i^+|-\frac1{2\sqrt6}
=\frac{t_i-(s_i+4)}{8\sqrt6}
\longrightarrow0\quad\text{于 }L^2, \tag{2}
\]

且

\[
q_i-\frac92=\frac18t_i-\frac98(s_i+4)\longrightarrow0
\quad\text{于 }L^2. \tag{3}
\]

这些是局部极限分析实际需要的全部全局输入。

---

## 2. 一个 harmonic-radius 坐标片上的极限

设存在固定 \(r_0>0\) 和点 \(x_i\)，使 \(x_i\) 处具有统一的 \(C^{2,\alpha}\) harmonic radius 下界。取稍小坐标片并经微分同胚拉回，可设

\[
g_i\longrightarrow g_\infty\qquad\text{于 }C^{2,\beta}_{\rm loc},
\quad 0<\beta<\alpha.
\]

于是曲率在 \(C^{0,\beta}_{\rm loc}\) 中收敛，而 Ricci 夹逼推出

\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\qquad s_\infty=-4. \tag{4}
\]

极限度量由 Einstein 方程继续成为光滑度量。由 (2) 与曲率的局部一致收敛，

\[
|W^+_\infty|\equiv\frac1{2\sqrt6}. \tag{5}
\]

### 调和代表与 monopole 二形式

\(\|H_i\|_2^2=(a_i^+)^2\) 一致有界。调和形式的局部椭圆估计给出子列

\[
H_i\longrightarrow H_\infty
\]

于较小坐标片的 \(C^{1,\beta}\) 中，其中

\[
dH_\infty=d^*H_\infty=0,\qquad *H_\infty=H_\infty.
\]

由 (1)、(3) 和局部一致收敛，

\[
|H_\infty|\equiv
c_0=\frac{3}{4\sqrt2\pi}>0. \tag{6}
\]

在此坐标片上 \(q_i\to9/2\)，故可选正则化使

\[
f_i\longrightarrow f_\infty=\sqrt{\frac92}=\frac3{\sqrt2}.
\]

再由 (1)，

\[
\varphi_i\longrightarrow
-\frac{6\sqrt2\pi}{3/\sqrt2}H_\infty
=-4\pi H_\infty
\quad\text{于 }L^2_{\rm loc}, \tag{7}
\]

从而

\[
\psi_i\longrightarrow\psi_\infty
=-\frac{8\pi}{3}H_\infty,\qquad
|\psi_\infty|=\sqrt2. \tag{8}
\]

而 \(D_{{\rm Hodge},i}\to0\) 给出

\[
d\psi_\infty=d^*\psi_\infty=0.
\]

因此 \(\psi_\infty\) 是闭、自对偶、处处非零且长度为 \(\sqrt2\) 的二形式；它在局部定义一个 almost-Kähler 结构。

这里必须使用定量分解文稿的重标度约定。按该约定

\[
u_i=\frac32|\Phi_i|^2\to\frac3{\sqrt2},
\qquad |\Phi_i|^2\to\sqrt2.
\]

另一份笔记中“\(|\Phi_i|^2\to4\)”属于不同的未重标度方程，不能与 \(f_i=\sqrt{q_i}\) 的公式直接混用。

---

## 3. 本征值余项确实强制两重本征值

定义点态二次式

\[
\mathcal E(W,v)
=\langle Wv,v\rangle+\sqrt{\frac23}|W|\,|v|^2\ge0.
\]

文稿中的

\[
D_{\rm eig}=2\int\mathcal E(W^+,\psi)
\]

趋于零。由 (7)、\(W_i^+\to W_\infty^+\) 以及强 \(L^2\) 收敛，可传递到极限：

\[
\mathcal E(W_\infty^+,\psi_\infty)=0
\]

于整个较小坐标片成立。因为 \(\psi_\infty\neq0\)，其方向就是 \(W_\infty^+\) 的最小本征线，而且

\[
\lambda_{\min}
=-\sqrt{\frac23}|W_\infty^+|. \tag{9}
\]

设三个本征值为 \(\lambda_1\le\lambda_2\le\lambda_3\)。迹为零给出

\[
\lambda_2+\lambda_3=-\lambda_1,
\]

并且

\[
\lambda_2^2+\lambda_3^2\ge\frac{\lambda_1^2}{2}.
\]

故

\[
|W^+|^2\ge\frac32\lambda_1^2,
\]

等号当且仅当

\[
\lambda_2=\lambda_3=-\frac{\lambda_1}{2}.
\]

结合 (5) 和 (9)，

\[
\boxed{\operatorname{Spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right),} \tag{10}
\]

且 \(\psi_\infty\) 张成 \(-1/6\) 的简单本征线。

所以，本征值余项、振幅控制和调和投影控制不仅给出“接近某条本征线”，而是在正则极限上给出完整的点态谱 (10)。

---

## 4. Derdziński 后果：该谱在 \(\operatorname{Ric}=-g\) 下局部不存在

目标谱的最大本征值具有重数二，因此 Catino–Dameno 关于“最大本征值一致简单”的定理不能直接使用。不过原始 Derdziński 结论正好处理 \(W^+\neq0\) 且至多有两个本征值的情形，包括这里的

\[
\alpha=\beta=\frac1{12},\qquad \gamma=-\frac16.
\]

Einstein 条件给出 \(\delta W_\infty^+=0\)。Derdziński 定理于是说明，在简单本征线可定向的局部坐标片上，某个与

\[
|W_\infty^+|^{2/3}g_\infty
\]

成常数倍的度量是 Kähler。由于 (5) 中 \(|W_\infty^+|\) 是常数，该共形倍数也是常数。因此 \(g_\infty\) 本身局部 Kähler。

对复定向的 Kähler 四维度量，取 Kähler 形式长度平方为 \(2\)，有

\[
\operatorname{Spec}(W^+)
=\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right). \tag{11}
\]

由 \(s_\infty=-4\)，(11) 必须是

\[
\left(-\frac23,\frac13,\frac13\right),
\]

与 (10) 不同。故不存在具有 (4)、(5)、(10) 的 Einstein 正则坐标片。

### 共形因子方程为何不能产生非紧模型

若暂写

\[
\widetilde g=f^2g_\infty
\]

并假设 \(\widetilde g\) Kähler，则 Weyl 端同态的本征值满足

\[
\lambda_{g_\infty}=f^2\lambda_{\widetilde g}.
\]

简单本征值为 \(-1/6\)，而 Kähler 简单本征值为
\(\widetilde s/6\)，所以

\[
f^2\widetilde s=-1. \tag{12}
\]

若采用 \(\Delta=\operatorname{div}\nabla\)，标量曲率变换为

\[
\widetilde s
=f^{-3}(s_\infty f-6\Delta f).
\]

将 \(s_\infty=-4\) 和 (12) 代入，得到

\[
\Delta f=-\frac12f. \tag{13}
\]

方程 (13) 单独在非紧开集上可以有局部正解，但它只编码标量曲率的迹部分。完整 Einstein–Kähler 共形关系还包含无迹 Ricci 方程；Derdziński 一阶结构进一步固定 Kähler 代表的共形倍数为 \(|W^+|^{2/3}\) 的常数倍。这里 \(|W^+|\) 恒定，因此 \(f\) 必须恒定，与 (13) 不相容。

所以非紧性不能挽救精确校准谱。一般的非紧共形 Kähler–Einstein 度量可以存在，但其 Einstein 代表的 \(|W^+|\) 必须变化；供应的 Derdziński-duality 文献中的 Poincaré–Einstein 例子属于这种情形。

---

## 5. Bochner 公式及数值修正

以 \(W^+\) 作为 \(\Lambda^+\) 上迹为零的对称端同态，并采用 \(\Delta=\operatorname{div}\nabla\)，Einstein 四维度量满足

\[
\frac12\Delta|W^+|^2
=
|\nabla W^+|^2+\frac{s}{2}|W^+|^2
-6\,\operatorname{tr}\bigl((W^+)^3\bigr). \tag{14}
\]

这与 Catino–Dameno 文稿 Lemma 2.5 的张量 Weitzenböck 方程一致。对谱 (10)，

\[
|W^+|^2=\frac1{24},\qquad
\operatorname{tr}\bigl((W^+)^3\bigr)=-\frac1{288}.
\]

若其范数恒定，(14) 给出

\[
0=|\nabla W^+|^2-\frac1{12}+\frac1{48},
\qquad
\boxed{|\nabla W^+|^2=\frac1{16}.} \tag{15}
\]

先前笔记中的 \(1/24\) 来自系数
\((s/3,-4)\)，与标准 Einstein–Weyl Weitzenböck 公式不一致。

公式 (15) 本身只说明假想谱需要非平行的 \(W^+\)；它并不构造这样的 Einstein 度量。Derdziński 结构却迫使恒定二本征值谱对应的共形因子为常数，继而使度量 Kähler，产生上述矛盾。

---

## 6. 最强可证表述

**局部正则坐标片排斥定理。**  
在固定临界 Ishida–LeBrun 流形上，不存在满足

\[
\|\operatorname{Ric}_{g_i}+g_i\|_{L^\infty(g_i)}\to0
\]

且在某些点 \(x_i\) 具有统一正 \(C^{2,\alpha}\) harmonic radius 的序列。任何这样的坐标片都会产生光滑 Einstein 极限，并由定量 monopole 余项得到谱 (10)，随后与局部 Derdziński–Kähler 结构矛盾。

等价地，对固定的 harmonic-radius 归一化，

\[
\boxed{\sup_{x\in M}r_h^{2,\alpha}(x,g_i)\longrightarrow0.}
\]

这一结论不需要直径上界、全局光滑收敛、Stokes 积分或 Armstrong 的紧致版本。它比“全局有界几何时不存在该序列”更强：任何固定未缩放尺度的正则坐标片都已被排除。缩放尺度趋零后的 Ricci-flat、\(W^+=0\) 极限仍是另一种现象，与此结论相容。
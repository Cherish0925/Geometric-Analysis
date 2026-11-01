# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 6,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step6_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step6_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Review the regular-patch and spectral-transfer chain needed to exploit any local algebraic contradiction. For a fixed critical Ishida–LeBrun manifold with ||Ric+g||∞→0 and absolute scalar–Weyl/SW deficits O(Aδ²), determine rigorously whether the existence of one unit ball with Vol B1≥v yields a fixed harmonic chart on which a smooth Einstein limit exists and the full spectrum (−1/6,1/12,1/12) holds. Check the use of Cheeger–Naber Theorem 1.13, the definition/propagation of harmonic radius, strong W^{2,p} convergence under only L∞ Ricci defect, and transfer of the selected regularized SW forms/eigenvalue defect. Pay special attention to whether a monopole solution can be chosen coherently across i and regularization, and whether local elliptic estimates give a nonzero limiting eigenform. State the strongest theorem actually justified, and exactly what conclusion about sup_p Vol B1 can follow if the local projector obstruction is valid.

## Integrated Scientific Memo

# 核验结论

在固定临界 Ishida–LeBrun 流形上，设
\[
\delta_i=\|g_i^{-1}(\Ric_{g_i}+g_i)\|_{L^\infty}\to0,
\]
且所有相关标量–Weyl/SW 非负总缺陷均为绝对量
\[
O(A\delta_i^2),\qquad A\ \text{固定}.
\]
若存在单位球
\[
\Vol_{g_i}B_1(p_i)\ge v>0,
\]
则确实可以抽取一个固定尺度的谐和坐标片，其极限是光滑负 Einstein 度量。经一个明确的对角正则化选择后，SW 本征值缺陷也可传递，并迫使
\[
\Spec(W_\infty^+)=\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
以及一个处处非零的极限调和自对偶最低本征形式。

但该谱型并非局部矛盾；它与局部 Derdziński 共形 Kähler 结构相容。因此现有“局部 projector obstruction”并不成立，当前不能由此推出单位球体积塌缩。只有在另行证明一个真正排除上述 Einstein germ 的局部定理后，才可推出
\[
\sup_{p\in M}\Vol_{g_i}B_1(p)\longrightarrow0.
\]

## 1. Cheeger–Naber 只给谐和半径正则片

充分大时 \(|\Ric_{g_i}|\le3\)。Cheeger–Naber Theorem 1.13 给出
\[
\Vol\!\left(
T_r\{x\in B_1(p_i):r_h(x)\le r\}
\right)\le C(v)r^4. \tag{1}
\]
这里是谐和半径 \(r_h\)，不是曲率正则尺度 \(r_x\)。后者的对应估计需要精确 Einstein 或 \(\nabla\Ric\) 控制，而
\[
\|\Ric+g\|_\infty\to0
\]
不控制 \(\nabla\Ric\)。

由 Bishop–Gromov，
\[
\Vol B_{1/2}(p_i)\ge b(v)>0.
\]
取固定 \(\rho=\rho(v)>0\)，使
\[
C(v)(2\rho)^4<\frac12b(v).
\]
令
\[
G_i=B_{1/2}(p_i)\setminus
T_{2\rho}\{r_h\le2\rho\}.
\]
则
\[
\Vol(G_i)\ge \frac12b(v).
\]
任取 \(x_i\in G_i\)，在 \(B_\rho(x_i)\) 上都有统一正的谐和半径。因此可取得固定大小的谐和坐标图。该结论仅产生正测度的局部正则片，不能推出整个 \(B_1(p_i)\) 或整个 \(M\) 上谐和半径一致有下界。

## 2. 仅用 \(L^\infty\) Ricci defect 可得到光滑 Einstein 极限

在缩小后的固定谐和坐标域内，Cheeger–Naber 对谐和半径的定义及其标准椭圆推论给出，对每个有限 \(p\) 与适当 \(\alpha<1\)，
\[
\|g_i\|_{C^{1,\alpha}}+\|g_i\|_{W^{2,p}}\le C.
\]
取子列后，
\[
g_i\to g_\infty\quad\text{强 }C^{1,\beta}_{\rm loc},
\qquad
g_i\rightharpoonup g_\infty\quad\text{弱 }W^{2,p}_{\rm loc}. \tag{2}
\]

谐和坐标中
\[
(\Ric g_i)_{ab}
=-\frac12g_i^{kl}\partial_k\partial_l(g_i)_{ab}
+Q_{ab}(g_i,\partial g_i). \tag{3}
\]
令 \(E_i=\Ric(g_i)+g_i\)。由 \(E_i\to0\) 于 \(L^\infty\)，结合 (2)，可在分布意义下传递 (3)，得到
\[
\Ric(g_\infty)=-g_\infty. \tag{4}
\]
极限方程无 defect，椭圆 bootstrap 因而给出
\[
g_\infty\in C^\infty.
\]

之后对 \(g_i-g_\infty\) 的线性化差分方程使用内点 \(W^{2,p}\) 估计，才可加强为
\[
g_i\to g_\infty
\quad\text{强 }W^{2,p}_{\rm loc}
\qquad(\forall p<\infty). \tag{5}
\]
于是
\[
\Rm(g_i)\to\Rm(g_\infty)
\quad\text{强 }L^p_{\rm loc}. \tag{6}
\]

不能声称 \(g_i\to g_\infty\) 于 \(C^{2,\alpha}\)：\(E_i\to0\) 于 \(L^\infty\) 不蕴含 \(C^\alpha\) 控制。

## 3. 绝对总缺陷可自动限制到任意所选片

这里 \(M,A\) 固定，所有非负总缺陷满足
\[
\int_M\mathfrak d_i=O(A\delta_i^2)\to0.
\]
故对任意随 \(i\) 选择的正则片 \(U_i\subset M\)，都有
\[
\int_{U_i}\mathfrak d_i\to0. \tag{7}
\]
这与“仅有全局平均缺陷”的情形不同；后者不能仅由一个非塌缩球保证该球上的缺陷很小。

由 \(s_i\to-4\) 一致、标量–Weyl completion 以及 (5)–(7)，得到
\[
s_\infty=-4,\qquad
|W_\infty^+|=\frac1{2\sqrt6},\qquad q_\infty=\frac92. \tag{8}
\]

## 4. 正则化 monopole 不必在参数间连续，但必须作对角选择

最优权重 \(f=\sqrt q\) 可能不光滑。严格做法是：对每个 \(i\)，取光滑正权重 \(f_{i,k}\to\sqrt{q_i}\)，并为每个 \(f_{i,k}\) 选取一个 rescaled SW 解。无需这些解随 \(i\) 或 \(k\) 连续，也不存在所需的“规范 monopole 序列”。

应明确选取 \(k(i)\to\infty\)，使正则化余项趋零，例如
\[
o_{k(i)}(1)\le \delta_i^2
\]
（若必须保留同阶上界，则取相应 \(A\delta_i^2\) 阈值）。这给出单一对角序列
\[
f_i:=f_{i,k(i)},\qquad \Phi_i,\psi_i,\varphi_i,
\]
满足全部缺陷趋零及
\[
\|f_i\varphi_i+6\sqrt2\pi H_i\|_2\to0, \tag{9}
\]
\[
\left\||2\pi H_i|-\frac{q_i}{3\sqrt2}\right\|_2\to0. \tag{10}
\]
其中 \(H_i\) 是所选固定符号类的调和自对偶代表；它由度量和类决定，不依赖具体 monopole 解。

固定流形上符号类只有有限多个，可先取子列使该类固定。无需跨 \(i\) 的解空间连续选择。

## 5. 极限调和形式确实非零

\(H_i\) 满足
\[
dH_i=0,\qquad d_{g_i}^*H_i=0,\qquad *_iH_i=H_i,
\]
且其全局 \(L^2\) 范数有统一上界。谐和坐标上的局部椭圆估计给出子列收敛到光滑 \(g_\infty\)-调和自对偶形式 \(H_\infty\)。

由 (8)、(10)，在每个紧包含子片上
\[
|H_i|\longrightarrow
c_0:=\frac{3}{4\sqrt2\pi}
\quad\text{于 }L^2. \tag{11}
\]
结合调和形式的局部紧致性可得
\[
|H_\infty|\equiv c_0>0. \tag{12}
\]
因此非零性不是由任选 monopole 的紧致性猜出的，而是由规范的 \(H_i\) 及振幅缺陷强制得到。

## 6. 本征值缺陷的传递需要补上一条 spinor 一致可积性估计

设
\[
\mathcal W_i
=
W_i^++\sqrt{\frac23}|W_i^+|\Id_{\Lambda_i^+}\ge0.
\]
本征值缺陷为
\[
D_{{\rm eig},i}
=
2\int_M\langle\mathcal W_i\psi_i,\psi_i\rangle\to0. \tag{13}
\]
由 (9)、\(f_i\to\sqrt{9/2}>0\) 及 (12)，可得
\[
\psi_i\to\psi_\infty
\quad\text{于局部 }L^2,
\qquad \psi_\infty\ne0,
\]
且 \(\psi_\infty\) 是 \(H_\infty\) 的非零常数倍。

为了将
\[
\langle W_i^+\psi_i,\psi_i\rangle
\]
传到极限，仅有 \(L^2\) 收敛尚不够。需使用 rescaled SW Weitzenböck 最大值估计：由于 \(f_i\) 在所选片上一致远离零且 \(s_i\) 有界，spinor 振幅具有局部一致 \(L^\infty\) 上界。由此和 \(L^2\) 收敛可得任意有限指数的局部强收敛。结合
\[
W_i^+\to W_\infty^+\quad\text{强 }L^p_{\rm loc},
\]
可传递 (13)，得到
\[
\int_U
\langle\mathcal W_\infty\psi_\infty,\psi_\infty\rangle=0.
\]
积分核非负且极限对象光滑，因此
\[
\mathcal W_\infty\psi_\infty=0. \tag{14}
\]

于是
\[
\lambda_{\min}(W_\infty^+)
=-\sqrt{\frac23}|W_\infty^+|
=-\frac16. \tag{15}
\]
对三维欧氏空间上的迹零对称算子，尖锐不等式达到等号当且仅当另外两个本征值相等。结合迹零和 (8)，得到
\[
\boxed{
\Spec(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right)
}. \tag{16}
\]
且 \(H_\infty\) 张成简单最低本征线。

## 7. 最强已证定理

**局部临界谱型提取定理。**  
在上述固定临界 Ishida–LeBrun 假设及绝对 \(O(A\delta_i^2)\) 缺陷下，若
\[
\Vol_{g_i}B_1(p_i)\ge v>0,
\]
则存在 \(\rho(v)>0\)、点 \(x_i\in B_{1/2}(p_i)\)、固定域上的谐和坐标以及子列，使得
\[
g_i\to g_\infty
\quad\text{强 }C^{1,\beta}_{\rm loc}
\cap W^{2,p}_{\rm loc}
\]
（每个有限 \(p\)），其中
\[
\Ric(g_\infty)=-g_\infty
\]
且 \(g_\infty\) 光滑。并存在光滑调和自对偶形式 \(H_\infty\)，满足
\[
|H_\infty|=\frac{3}{4\sqrt2\pi}>0,
\]
位于 \(W_\infty^+\) 的最低本征线中，而且
\[
s_\infty=-4,\qquad
|W_\infty^+|=\frac1{2\sqrt6},\qquad
\Spec(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

该定理只产生一个开集上的 Einstein germ，不给出完备性、全局 Einstein 度量、原流形拓扑恢复、直径控制，也不排除别处的曲率集中、orbifold 点、ALE bubbles 或远处塌缩。

## 8. 对局部矛盾与 \(\sup_p\Vol B_1\) 的精确结论

上述谱型不是局部不可能对象。Derdziński 两本征值机制在局部双覆盖上给出正函数 \(f\)，使 \(f^2g_\infty\) 为负标量 Kähler 度量，并满足
\[
\Delta_{g_\infty}f=-\frac12f.
\]
正解在局部域上不矛盾；只有在闭流形上积分才产生
\[
0=\int\Delta f=-\frac12\int f<0.
\]
因此现有 projector/spectral 数据本身没有局部 obstruction，故无条件下不能推出关于
\[
\sup_p\Vol B_1(p)
\]
的任何新结论。

精确的条件命题是：

> 若另有一个有效局部 projector obstruction，能排除上述“光滑 \(\Ric=-g\) germ + 非零最低本征调和自对偶形式 + 谱型 (16)”这一完整局部对象，则必有
> \[
> \boxed{\sup_{p\in M}\Vol_{g_i}B_1(p)\to0.}
> \]

证明是直接反证：若存在子列及 \(v>0\) 使该上确界至少为 \(v\)，选择实现该下界的 \(p_i\)，上述提取定理即产生被排除的局部对象。

这一条件结论仅表示统一的单位尺度塌缩；它本身既不否定原序列存在，也不恢复拓扑或产生全局 Einstein 度量。
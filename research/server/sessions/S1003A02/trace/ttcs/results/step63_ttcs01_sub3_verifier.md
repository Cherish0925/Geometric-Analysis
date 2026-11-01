# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md"
  ]
}
```

## Task

Verify the Step-62/63 derivations on M = X#kCP̄² (X minimal general type, A = c1²(X), P = ∫|Ric°|², p = P/8π²). Check each with explicit conventions (AAD: |Ω|²=2, ∇Ω = a⊗φ − Ja⊗Jφ, s*−s=|∇Ω|²=4|a|², κ_J = s+6u with u=|a|², W2 = ½(ρ*''⊗Ω+Ω⊗ρ*''), γ_J = R(Ω) − a∧Ja). (1) Identity 62.1 and Theorem 62.A (step62 note §1–3). (2) Theorem 63.T: the general Gauss formula γ_J = R(Ω)+α∧β for an arbitrary orthogonal J with ∇Ω = α⊗φ+β⊗Jφ (sign, factor, gauge independence, that it represents 2πc1(J)), that R(Ω)^- = ρ0 with |ρ0|² ≤ |Ric°|²/2, the Hodge step ‖γ^-‖ ≥ 2π|c1^-|, the choice of class a_ε with |a_ε^-|² ≥ k+Π and existence of J with c1(J)=a_ε (Wu), and the Kähler-tariff reduction. (3) Proposition 63.AK: P = 2‖γ^-‖² + ∫u(5u+s) + 2∫|ρ*''|² + 4∫|W3|², including norms |W1|²=κ²/24, |W2|²=|ρ*''|², and the Sekigawa consistency check and the AK-Einstein consequences. (4) §3 emptiness of the 62.A equality locus: does LeBrun's Prop 2.4 equality plus Cauchy–Schwarz really force u constant; is N a section of a bundle with c2 = c2+2c1² = 5χ+6τ, and is 5χ+6τ = c2(X)+2A−k on M; the Taubes/Li–Liu period argument. (5) §4 model numbers: constant-torsion bound p ≥ (A−k)(2−3u)²/(u(4−3u)); the variance–slack relation ∫(u−ū)² = 8π²σ; the ASD-patch saturating configuration (υ=5k, patch volume 18π², ½∫u² = 4π²k, p=0) and the \overline{FPP} numerology; the two-ended AE neck bound P ≥ 32π². Report every error with the corrected statement, and say which conclusions survive.

## Output

# 科学核验备忘录

记
\[
C:=2\chi(M)+3\tau(M)=A-k,\qquad 
B:=A+\upsilon,\qquad 
V(\widetilde g)=2\pi^2B .
\]

以下采用题中给定的 AAD 约定：
\[
|\Omega|^2=|\phi|^2=|J\phi|^2=2,\quad
\nabla\Omega=a\otimes\phi-Ja\otimes J\phi,\quad
u=|a|^2=\frac14|\nabla\Omega|^2,
\]
\[
s^*-s=4u,\qquad \kappa_J=s+6u,\qquad
\gamma_J=R(\Omega)-a\wedge Ja.
\]

---

## 1. Identity 62.1 与 Theorem 62.A

### 1.1 Identity 62.1 正确，但原推导中有一处中间系数笔误

由定义
\[
\kappa=\frac A2-\frac{3}{8\pi^2}\int|W^+|^2
\]
得到
\[
\int|W^+|^2=\frac{4\pi^2}{3}(A-2\kappa).
\]
在 Yamabe 代表元 \(\widetilde g\) 上，
\[
\int s_{\widetilde g}^{\,2}=Y[g]^2=32\pi^2(A+\upsilon).
\]
四维 Chern–Weil 公式为
\[
P=4\int|W^+|^2+\frac1{12}\int s^2-8\pi^2(A-k).
\]
因此
\[
\begin{aligned}
p(\widetilde g)
&=\frac{1}{8\pi^2}\left[
\frac{16\pi^2}{3}(A-2\kappa)
+\frac{8\pi^2}{3}(A+\upsilon)
-8\pi^2(A-k)\right]\\
&=k-\frac43\kappa+\frac13\upsilon\\
&=(k-\kappa)+\frac13(\upsilon-\kappa).
\end{aligned}
\]
所以 Identity 62.1 正确。

Step 62 的证明文字把第一项写成了
\[
\frac16(A-2\kappa);
\]
正确值是
\[
\frac23(A-2\kappa).
\]
最终公式没有受这一笔误影响。

由于该共形类的 Yamabe 常数为负，并且
\[
\int s_g^2\ge Y[g]^2,
\]
同时 \(\int|W^+|^2\) 在四维共形变换下不变，所以
\[
p(g)\ge p(\widetilde g)
\]
也正确。

### 1.2 公式 (62.2) 的常数正确

LeBrun 的估计与
\[
(a_\varepsilon^+)^2=A+\Pi
\]
给出
\[
\int(s-\sqrt6|W^+|)^2\ge72\pi^2(A+\Pi).
\]
在 \(s_{\widetilde g}\equiv-4\) 时，
\[
\|s\|_2=4\sqrt2\,\pi\sqrt{A+\upsilon},
\qquad
\sqrt6\,\|W^+\|_2=2\sqrt2\,\pi\sqrt{A-2\kappa}.
\]
Minkowski 不等式于是给出
\[
2\sqrt{A+\upsilon}+\sqrt{A-2\kappa}
\ge3\sqrt{A+\Pi},
\]
即 (62.2)。

### 1.3 Theorem 62.A 的主公式正确，但参数区间的文字需要修正

令
\[
y=\sqrt{1-\frac{2\kappa}{A}}.
\]
当
\[
0\le\kappa\le \frac A2
\]
时，\(0\le y\le1\)，从 (62.2) 丢掉 \(\Pi\ge0\) 可得
\[
\upsilon\ge
A\left[\left(\frac{3-y}{2}\right)^2-1\right].
\]
代入 Identity 62.1：
\[
\boxed{
p\ge L_A(k,\kappa)
=(k-\kappa)+\frac12\left(A-\kappa-\sqrt{A^2-2A\kappa}\right).
}
\]
展开为
\[
L_A(k,\kappa)
=(k-\kappa)+\frac{\kappa^2}{4A}
+\frac{\kappa^3}{4A^2}
+O\!\left(\frac{\kappa^4}{A^3}\right).
\]
这些系数正确。

需要修正的两处是：

1. **上述固定-\(\kappa\) 估计事实上对整个**
   \[
   0\le\kappa\le A/2
   \]
   **都成立**，不只到 \(4A/9\)。

2. \(4A/9\) 的作用是：\(L_A(k,\kappa)\) 作为 \(\kappa\) 的函数在
   \[
   \kappa=\frac{4A}{9}
   \]
   取得最小值
   \[
   k-\frac A3.
   \]
   因而“\(\kappa\ge4A/9\) 时只剩 \(k-A/3\)”应理解为：如果不再固定 \(\kappa\)，而在所有允许的 \(\kappa\) 上取统一下界，最小值是 \(k-A/3\)。对一个给定的 \(\kappa>4A/9\)，\(L_A(k,\kappa)\) 仍比 \(k-A/3\) 更强。

当 \(\kappa<0\) 时，最直接且更强的公式是
\[
\upsilon\ge0
\quad\Longrightarrow\quad
p\ge k-\frac43\kappa\ge k.
\]
原文把 Theorem 62.A 写成对所有 \(\kappa\le4A/9\) 统一成立；其通过平方 (62.2) 的证明不能覆盖任意大的负 \(\kappa\)。在研究所需的 Weyl-saving 区域 \(\kappa\ge0\) 中，公式完全成立。

### 1.4 保留下来的结论

- Weyl-channel 恒等式完全正确。
- \(k^2/(4A)\) 的展开系数正确。
- 若有上界 \(\kappa_*\le k\)，则
  \[
  \alpha(M)\ge
  4\pi^2\left(A-k-\sqrt{A^2-2Ak}\right)
  \]
  正确。
- 使用 \(\kappa_*\le4A/9\) 时，\(L_A\) 对 \(\kappa\) 单调递减，因而 Corollary 62.B 的用法正确。
- Kähler 情形 \(\kappa\le0\) 给出 \(p\ge k\)，但最简证明应使用 \(\upsilon\ge0\) 与 Identity 62.1，或者使用第 2 节的 Chern-form 论证。

---

## 2. Theorem 63.T

### 2.1 一般 Gauss 公式的符号与系数正确

记 \(\psi=J\phi\)。对任意正定向正交几乎复结构，
\[
\nabla\Omega=\alpha\otimes\phi+\beta\otimes\psi,
\]
并可写成
\[
\nabla\phi=-\alpha\otimes\Omega+b\otimes\psi,
\qquad
\nabla\psi=-\beta\otimes\Omega-b\otimes\phi.
\]
在 \(\phi\) 的 Ricci 恒等式中，\(\psi\)-分量是
\[
db+\alpha\wedge\beta=-R(\Omega).
\]
故
\[
\boxed{\gamma_J:=-db=R(\Omega)+\alpha\wedge\beta.}
\]

在 almost-Kähler 情形
\[
\alpha=a,\qquad \beta=-Ja,
\]
从而
\[
\gamma_J=R(\Omega)-a\wedge Ja,
\]
与 AAD 方程 (25) 完全一致。

若换规范
\[
\phi'=\cos\theta\,\phi+\sin\theta\,J\phi,
\]
则
\[
b'=b+d\theta
\]
且 \((\alpha,\beta)\) 作同一个 \(SO(2)\) 旋转，所以
\[
\alpha'\wedge\beta'=\alpha\wedge\beta.
\]
因此 \(-db\) 和 \(\alpha\wedge\beta\) 都是规范无关对象。

AAD 方程 (25) 已确定其 Chern 归一化：
\[
\boxed{[\gamma_J]=2\pi c_1(J).}
\]

### 2.2 \(R(\Omega)^-\) 与 Ricci 张量之间的系数正确

Singer–Thorpe 分解给出
\[
R(\Omega)^-=\frac12\widetilde{\operatorname{Ric}^{\circ}}(\Omega).
\]
将 \(\Omega\) 视为端同态 \(J\)，有
\[
\widetilde S(\Omega)=SJ+JS.
\]
\(J\)-反不变部分与 \(J\) 反交换，因而不贡献；\(J\)-不变部分贡献
\[
\frac12(SJ+JS)=SJ.
\]
故
\[
R(\Omega)^-=\operatorname{Ric}_0'\circ J=\rho_0.
\]
在题中 2-形式范数约定下，
\[
\boxed{|\rho_0|^2=\frac12|\operatorname{Ric}_0'|^2
\le\frac12|\operatorname{Ric}^{\circ}|^2.}
\]

### 2.3 twist 的点态常数正确

因为
\[
|\nabla\Omega|^2
=2(|\alpha|^2+|\beta|^2),
\]
而
\[
|\alpha\wedge\beta|
\le\frac12(|\alpha|^2+|\beta|^2)
=\frac14|\nabla\Omega|^2,
\]
又因为任意可分解 2-形式 \(\eta\) 满足
\[
|\eta^+|=|\eta^-|=\frac1{\sqrt2}|\eta|,
\]
所以
\[
|(\alpha\wedge\beta)^-|
\le\frac{1}{4\sqrt2}|\nabla\Omega|^2.
\]
因此
\[
\mathcal T_J
:=\|(\alpha\wedge\beta)^-\|_2
\le\frac{1}{4\sqrt2}\|\nabla\Omega\|_4^2.
\]

### 2.4 Hodge 步骤正确

写
\[
\gamma_J=H+d\theta,
\]
其中 \(H\) 是代表 \(2\pi c_1(J)\) 的调和形式。由于 \(H^-\) 调和，
\[
\langle H^-,d\theta\rangle_{L^2}=0,
\]
而 \(H^-\) 与 \((d\theta)^+\) 点态正交，因此
\[
\|\gamma_J^-\|_2^2
=\|H^-\|_2^2+\|(d\theta)^-\|_2^2.
\]
于是
\[
\boxed{\|\gamma_J^-\|_2\ge2\pi|c_1(J)^-|.}
\]

结合
\[
\gamma_J^-=\rho_0+(\alpha\wedge\beta)^-
\]
得到
\[
\left(\frac12\int|\operatorname{Ric}_0'|^2\right)^{1/2}
\ge
2\pi|c_1(J)^-|-\mathcal T_J,
\]
以及
\[
\boxed{
P\ge
2\left(2\pi|c_1(J)^-|-\mathcal T_J\right)_+^2.
}
\]

### 2.5 \(a_\varepsilon\) 与 almost-complex 结构

对
\[
a_\varepsilon=c_1(X)+\sum_i\varepsilon_iE_i
\]
有
\[
a_\varepsilon\equiv w_2(M)\pmod2,
\qquad
a_\varepsilon^2=A-k=2\chi(M)+3\tau(M).
\]
四维 Wu–Hirzebruch–Hopf 存在定理于是给出正定向 almost-complex 结构 \(J\)，满足
\[
c_1(J)=a_\varepsilon.
\]

符号平均给出
\[
\mathbb E_\varepsilon (a_\varepsilon^+)^2
=(c_1(X)^+)^2+\sum_i(E_i^+)^2
\ge A+|c_1(X)^-|^2+\sum_i(E_i^+)^2.
\]
若 \(\varepsilon_*\) 实现最大值并定义
\[
\Pi=(a_{\varepsilon_*}^+)^2-A,
\]
则实际上有精确等式
\[
\boxed{|a_{\varepsilon_*}^-|^2=k+\Pi,}
\]
而不只是“\(\ge k+\Pi\)”。

因此
\[
\boxed{
\sqrt{\frac P2}\ge
2\pi\sqrt{k+\Pi}
-\inf_{J:\,c_1(J)=a_{\varepsilon_*}}\mathcal T_J.
}
\]

### 2.6 Kähler tariff

若所用 Kähler 结构确实是一个 \(k\) 次 blow-up 的 general-type 最小曲面结构，则其 Kähler \(J\) 满足
\[
\mathcal T_J=0,\qquad \operatorname{Ric}^{\prime\prime}=0.
\]
Hodge index 给出
\[
(c_1(J)^+)^2
=\frac{(c_1(J)\cdot[\omega])^2}{[\omega]^2}\ge A,
\]
从而
\[
|c_1(J)^-|^2
=(c_1(J)^+)^2-(A-k)\ge k.
\]
所以
\[
\boxed{P\ge8\pi^2k.}
\]

对于底层光滑流形上的任意 Kähler 结构，还需要引用 symplectic minimal-model 唯一性或等价的结构定理，以确认该结构也有恰好 \(k\) 个 blow-up 且最小模型的 \(c_1^2\) 为 \(A\)。单靠类平均与 Wu 定理不能同时保证“最佳符号类”对应的 \(J\) 就是给定的平行 Kähler \(J\)。

---

## 3. Proposition 63.AK

### 3.1 \(W_1,W_2\) 的范数正确

AAD 的
\[
W_1^+
=\frac{\kappa_J}{8}\Omega\otimes\Omega
-\frac{\kappa_J}{12}\operatorname{Id}_{\Lambda^+}
\]
在 \(\Omega/\sqrt2\) 方向的特征值是 \(\kappa_J/6\)，在正交二维空间上的特征值各为 \(-\kappa_J/12\)。因此
\[
\boxed{|W_1^+|^2
=\frac{\kappa_J^2}{36}
+2\frac{\kappa_J^2}{144}
=\frac{\kappa_J^2}{24}.}
\]

对
\[
W_2^+
=\frac12(\rho_*''\otimes\Omega+\Omega\otimes\rho_*'')
\]
使用 \(|\Omega|^2=2\)，其两个非零矩阵元均为
\[
\frac{|\rho_*''|}{\sqrt2},
\]
故
\[
\boxed{|W_2^+|^2=|\rho_*''|^2.}
\]

### 3.2 Chern form 的自对偶部分正确

因为
\[
(a\wedge Ja)^+=\frac u2\Omega
\]
且
\[
R(\Omega)^+
=\left(\frac{\kappa_J}{6}+\frac{s}{12}\right)\Omega+\rho_*'',
\]
利用 \(\kappa_J=s+6u\) 得
\[
\gamma_J^+
=\frac{s+2u}{4}\Omega+\rho_*''
=\frac{s+s^*}{8}\Omega+\rho_*''.
\]
所以
\[
\boxed{
|\gamma_J^+|^2
=\frac{(s+2u)^2}{8}+|\rho_*''|^2.
}
\]

### 3.3 恒等式 (63.3) 完全正确

由
\[
P=4\int|W^+|^2+\frac1{12}\int s^2-8\pi^2c_1^2(M),
\]
以及
\[
4\pi^2c_1^2(M)
=\|\gamma_J^+\|_2^2-\|\gamma_J^-\|_2^2,
\]
得到
\[
\begin{aligned}
P
={}&2\|\gamma_J^-\|_2^2\\
&+\int\left[
\frac{(s+6u)^2}{6}
+\frac{s^2}{12}
-\frac{(s+2u)^2}{4}\right]\\
&+2\int|\rho_*''|^2+4\int|W_3^+|^2.
\end{aligned}
\]
而
\[
\frac{(s+6u)^2}{6}
+\frac{s^2}{12}
-\frac{(s+2u)^2}{4}
=su+5u^2.
\]
故
\[
\boxed{
P=2\|\gamma_J^-\|_2^2
+\int u(5u+s)
+2\int|\rho_*''|^2
+4\int|W_3^+|^2.
}
\]

进一步，
\[
\|\gamma_J^-\|_2^2\ge4\pi^2|c_1(J)^-|^2
\]
给出
\[
P\ge
8\pi^2|c_1(J)^-|^2
-\int u(|s|-5u)_+.
\]

### 3.4 Sekigawa 与 Einstein 推论

- Kähler 时 \(u=0\)、\(\rho_*''=W_3=0\)，且
  \[
  2\|\gamma^-\|^2
  =2\|\rho_0\|^2
  =\int|\operatorname{Ric}_0'|^2,
  \]
  与 \(P=\int|\operatorname{Ric}_0'|^2\) 一致。

- Einstein 且 \(s\ge0\) 时 \(P=0\)，(63.3) 右端每项均非负，并且 \(5u^2+su\) 强制 \(u=0\)。这正是 Sekigawa 结论。

- Einstein 且 \(s<0\) 时，\(\rho_0=0\)，所以
  \[
  \gamma^- =-(a\wedge Ja)^-,
  \qquad
  \|\gamma^-\|^2=\frac12\int u^2.
  \]
  将 \(2\|\gamma^-\|^2=\int u^2\) 并入 \(u(5u+s)\)，得到
  \[
  \boxed{
  \int u(|s|-6u)
  =2\int|\rho_*''|^2+4\int|W_3^+|^2.
  }
  \]
  同时
  \[
  \frac12\int u^2\ge4\pi^2|c_1^-|^2,
  \]
  因而
  \[
  \boxed{
  \int|\nabla\Omega|^4
  =16\int u^2
  \ge128\pi^2|c_1^-|^2.
  }
  \]

这些系数全部正确。

---

## 4. Theorem 62.A 等号集合

### 4.1 \(u\) 必为常数

等号同时要求：

1. LeBrun 曲率估计取等；
2. Minkowski/Cauchy–Schwarz 取等；
3. \(\Pi=0\).

LeBrun Proposition 2.4 给出 almost-Kähler 结构、\(\Omega\) 位于 \(W^+\) 最低特征空间、\(s+s^*\) 为常数，并且在相应 Weyl 范数估计取等时 \(W^+\) 是 \(J\)-不变的。Yamabe 归一化已给出 \(s\equiv-4\)，所以
\[
s^*=s+4u
\]
为常数，进而
\[
\boxed{u\ \text{为常数}.}
\]
也可由 \(|W^+|\) 常数和
\[
\kappa_J=s+6u
\]
得到同一结论。

### 4.2 Nijenhuis bundle 的 \(c_2\) 计算正确

若 \(u>0\) 为常数，则 \(N\) 处处不为零。AAD 把 \(N\) 看成
\[
N\in
\Gamma(\Lambda^{0,1}\otimes\Lambda^{0,2})
\cong
\Gamma(T^{1,0}\otimes K^{-1}).
\]
令 \(E=T^{1,0}\)、\(L=K^{-1}\)，则
\[
c_1(E)=c_1(J),\qquad c_1(L)=c_1(J).
\]
对秩二复向量丛，
\[
c_2(E\otimes L)
=c_2(E)+c_1(E)c_1(L)+c_1(L)^2,
\]
故
\[
\boxed{
c_2(T^{1,0}\otimes K^{-1})
=c_2(M)+2c_1(J)^2
=5\chi+6\tau.
}
\]
处处非零截面要求这个顶 Chern 数为零。

对
\[
M=X\#k\overline{\mathbf{CP}}^{\,2},
\]
有
\[
\chi(M)=\chi(X)+k,\qquad
\tau(M)=\tau(X)-k,
\]
所以
\[
\boxed{
5\chi(M)+6\tau(M)=c_2(X)+2A-k.
}
\]

原文只说该数在 \(k<c_2(X)+2A\) 时为正。实际上只要
\[
k\ne c_2(X)+2A,
\]
该数非零，便已排除处处非零的 \(N\)。在特殊数值
\[
k=c_2(X)+2A
\]
时，这个 Chern 数论证本身不给出矛盾。

### 4.3 period 论证排除所有 \(k\ge1\)

由
\[
\Pi\ge|c_1(X)^-|^2+\sum_i|E_i^+|^2
\]
以及 \(\Pi=0\)，得到
\[
c_1(X)^-=0,\qquad E_i^+=0\quad\forall i.
\]
almost-Kähler 形式 \(\Omega\) 闭且自对偶，故是调和形式并属于 \(H_g^+\)。于是
\[
E_i\cdot[\Omega]=E_i^+\cdot[\Omega]=0.
\]

LeBrun Proposition 3.2 的所给原文正是这一情形：利用相差 \(2E_i\) 的另一个 blow-up monopole class和 Taubes 的 \(SW\Rightarrow Gr\)，可得到 \(E_i\) 或相反定向类由伪全纯 \((-1)\)-球表示，其 symplectic 面积严格为正。这与
\[
E_i\cdot[\Omega]=0
\]
矛盾。

所以在 Step 62 所用的 monopole-class 假设下，
\[
\boxed{k\ge1\quad\Longrightarrow\quad
\text{Theorem 62.A 的等号集合为空}.}
\]
这一结论主要由 period 论证完成；Chern 数论证提供独立解释，并覆盖除一个特殊拓扑数值外的严格 almost-Kähler 常扭率情形。

---

## 5. 第 4 节模型计算

### 5.1 常扭率公式：成立，但必须写出 \(\boldsymbol{0<u\le2/3}\)

设
\[
s=-4,\qquad W_2=W_3=0,\qquad u\equiv\bar u,
\qquad B=A+\upsilon,\qquad C=A-k.
\]
则
\[
|W^+|^2=\frac{(2-3u)^2}{6}
\]
以及
\[
\boxed{
p
=B\left(1-2u+\frac32u^2\right)-C.
}
\]
又因为
\[
\gamma^+=\frac{u-2}{2}\Omega
\]
是调和自对偶形式，
\[
|c_1^+|^2=\frac{B(2-u)^2}{4},
\qquad
|c_1^-|^2=\frac{B(2-u)^2}{4}-C.
\]
twist 的范数是
\[
\mathcal T^2
=\frac12\int u^2
=\pi^2Bu^2.
\]

将这些精确表达式代入 Theorem 63.T，并在
\[
0<u<\frac23
\]
使用 \(P\ge0\) 确认平方两边均为正，化简得到
\[
\boxed{
B\,u(4-3u)\ge4C.
}
\]
在 \(u=2/3\) 时，同一公式直接由 \(p\ge0\) 得到。

此外
\[
p=
\frac{B}{4}(2-3u)^2
+\left[\frac{B}{4}u(4-3u)-C\right],
\]
从而
\[
\boxed{
p\ge
C\,\frac{(2-3u)^2}{u(4-3u)}.
}
\]

原文未写出 \(u\le2/3\)。对 \(u>2/3\)，Theorem 63.T 中
\[
2\pi|c_1^-|-\mathcal T
\]
可以变为非正，以上平方化简不再等价；此时应保留原始的平方根不等式，而不能普遍使用显示的有理函数下界。

在 formal common mode 中
\[
u\sim\frac{2k}{3A},
\]
所以
\[
p\gtrsim \frac{3A^2}{2k},
\]
这一渐近结论正确。

当 \(u=2/3\) 时 \(W^+=0\)，故 Weyl deficit 确为
\[
\kappa[g]=\frac A2.
\]

### 5.2 方差项：系数是渐近系数，不是一般精确等式

令
\[
m=\frac1V\int u,\qquad
v=\operatorname{Var}(u)
=\frac1V\int(u-m)^2.
\]
则模型中精确有
\[
\int|W^+|^2
=\frac V6\left[(2-3m)^2+9v\right],
\]
以及
\[
\boxed{
p=B\left(1-2m+\frac32m^2+\frac32v\right)-C.
}
\]

若同时令 LeBrun 估计近乎取等，则
\[
B\,[4-4m+m^2+v]=4A.
\]
在 \(m\to0\)、\(v\) 为二阶量时，
\[
\frac BA
=1+m+\frac34m^2-\frac14v+\cdots,
\]
\[
\frac{\kappa}{A}=m-v+\cdots,
\]
并且若
\[
\sigma:=p-L_A(k,\kappa),
\]
则
\[
\boxed{
\sigma=\frac A4\,v+\text{更高阶项}.
}
\]
又
\[
\int(u-m)^2=Vv=2\pi^2Bv,
\]
所以
\[
\boxed{
\int(u-m)^2
=8\pi^2\sigma\,[1+o(1)]
}
\]
只是在 \(B/A\to1\) 的近等号区间成立。Step 63 把它写成精确等号，需改成上述渐近形式；若 LeBrun 本身还有剩余量，则 \(\sigma\) 还包含该部分。

### 5.3 ASD patch 的算术正确，但只能在 \(\boldsymbol{k\le A/4}\) 时形成非负体积分解

令 \(u=2/3\) 的区域体积为
\[
V_p=18\pi^2k,
\]
其余区域 \(u=0\)，并令
\[
\upsilon=5k,\qquad
V=2\pi^2(A+5k).
\]
则剩余 \(u=0\) 区域的体积是
\[
V-V_p=2\pi^2(A-4k).
\]
因此这种二值分布需要
\[
\boxed{k\le A/4.}
\]
在 \(A/4<k<A/3\) 时，原文给出的 patch 体积超过总可用的 \(u=0\) 主体体积，不能作为非负测度分布。

在 \(k\le A/4\) 时，所有列出的数字正确：

- LeBrun 积分：
  \[
  36V-20V_p
  =72\pi^2A.
  \]

- twist flux：
  \[
  \frac12\int u^2
  =\frac12\cdot\frac49\cdot18\pi^2k
  =4\pi^2k.
  \]

- Weyl deficit：
  \[
  \int|W^+|^2
  =\frac23(V-V_p)
  =\frac{4\pi^2}{3}(A-4k),
  \]
  因而
  \[
  \kappa=2k.
  \]

- Identity 62.1：
  \[
  p=k-\frac43(2k)+\frac13(5k)=0.
  \]

这是一种不连续的积分密度配置，不是闭连通光滑 almost-Kähler Einstein 度量。任何光滑实现都必须处理 \(u=0\) 与 \(u=2/3\) 之间的过渡区。

### 5.4 \(\overline{\mathrm{FPP}}\) 数字正确，但只是曲率与拓扑数字对应

单个 patch 具有
\[
s=-4,\quad W^+=0,\quad V=18\pi^2,
\]
所以
\[
2\chi+3\tau
=\frac1{4\pi^2}\int\frac{s^2}{24}
=3.
\]
fake projective plane 满足
\[
\chi=3,\qquad \tau=1,\qquad c_1^2=9.
\]
反向定向后
\[
\chi=3,\qquad\tau=-1,\qquad
2\chi+3\tau=3,
\]
其 complex-hyperbolic Einstein 度量成为 \(W^+=0\)，并且在 \(s=-4\) 归一化下
\[
V=2\pi^2c_1^2=18\pi^2.
\]
有理交叉形式也确为
\[
\langle-1\rangle.
\]

但 \(\overline{\mathrm{FPP}}\) 有 \(b^+=0\)，不能携带与该定向相容的 symplectic 形式；事实上其交叉形式上也不存在平方为 \(3\) 的 characteristic 类，因此它本身没有该定向的 almost-complex 结构。故它不能逐字实现 almost-Kähler \(u=2/3\) patch；对应关系仅是
\[
(\chi,\tau,V,s,W^+)
\]
层面的数字吻合。

另外，真正的断开并
\[
X\sqcup k\,\overline{\mathrm{FPP}}
\]
满足
\[
(2\chi+3\tau)=A+3k,
\]
而不是 \(A-k\)。每做一次 connected sum，
\[
2\chi+3\tau
\]
减少 \(4\)，才得到 \(A-k\)。这正是 joining 几何必须承担的拓扑差额。原文将断开并直接称作 \(\upsilon=5k\) 的 saturating configuration，需按此区分。

关于 SW blow-up 公式向一般 \(b_1=0\) 负定 summand 的延伸，所给文件没有提供相应定理；这一点目前没有文献支撑材料。

### 5.5 两端 AE neck 的 \(32\pi^2\) 公式正确

对具有两个标准 Euclidean ends、拓扑为 \(S^3\times\mathbb R\) 的完整 AE 四维空间，Chern–Gauss–Bonnet 的每个端贡献 \(1\)，故
\[
\frac1{8\pi^2}
\int\left(
|W|^2-\frac12|\operatorname{Ric}^{\circ}|^2+\frac{s^2}{24}
\right)
=\chi-2=-2.
\]
因此
\[
\boxed{
P
=2\int|W|^2+\frac1{12}\int s^2+32\pi^2
\ge32\pi^2.
}
\]
这个结论适用于完整两端 AE 极限并要求相应曲率衰减。对有限长度的平滑过渡区，单凭该公式尚不能直接推出同一个统一常数；需控制其端部逼近或另行建立局部过渡估计。

---

## 总结

完全成立的核心结果包括：

1. Identity 62.1；
2. (62.2)；
3. \(0\le\kappa\le A/2\) 上的固定-\(\kappa\) 下界 \(L_A(k,\kappa)\)，以及其在 \(\kappa=4A/9\) 的最小值 \(k-A/3\)；
4. Theorem 63.T 的符号、系数、规范无关性、Chern 类归一化、Hodge 估计和最佳符号类；
5. Proposition 63.AK 及全部范数系数；
6. Sekigawa 与 \(s<0\) almost-Kähler Einstein 推论；
7. 在 Step 62 monopole-class 假设下，\(k\ge1\) 时等号集合由 period 论证排除；
8. 常扭率有理函数下界在 \(0<u\le2/3\) 时成立；
9. ASD patch 的积分算术在 \(k\le A/4\) 时成立；
10. 两端 AE 极限的 \(P\ge32\pi^2\)。

需要改写的部分是：

- Theorem 62.A 的负 \(\kappa\) 表述与 \(4A/9\) 的含义；
- 常扭率公式遗漏 \(u\le2/3\)；
- 方差公式应写成近等号区间的渐近关系；
- patch 分布要求 \(k\le A/4\)；
- \(\overline{\mathrm{FPP}}\) 只提供精确数字模型，不提供所需 almost-Kähler patch；
- 断开并与 connected sum 的 \(2\chi+3\tau\) 相差每个 summand 四个单位；
- 一般负定 summand 的 SW gluing 公式仍缺所给材料中的来源。
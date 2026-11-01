# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 70,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step70_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step70_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematical correctness and completeness of the selected-support lemma for the restricted IL negative-gap theorem. The note proves:

1. FULL-CURVATURE BUDGET: ∫|Rm|² ≤ C₀A_i from Chern-Gauss-Bonnet, using I-J=2A/3-q, J≤δ²Vol/(2π²), and Vol≤CA. Check that the identities are correctly applied, the volume upper bound derivation from the mixed SW inequality is valid, and equation (2.4) ∫|Rm|²=8π²χ+3/2∫|Ric°|² holds.

2. WEAK-TYPE MAXIMAL INEQUALITY: Lemma 4.1 under Ric≥-(n-1)g. Check the Vitali covering argument, the Bishop-Gromov volume doubling ratio, and the constant C(n,R₀).

3. COLLAPSE-CANCELLING PRODUCT: γ_α(0)=S_α·H_{2,α}^{1/2}≤C(r²+γ̃). The claim is that S_α~r²/Vol^{1/2} grows under collapse while H_{2,α}^{1/2}~Vol^{1/2}·(1+γ̃/r²) shrinks, so their product eliminates volume. Check each factor's scaling carefully, especially whether H₂ = ∫η²F_T² ≤ C(1+γ̃²/r⁴)Vol is correct.

4. PARAMETER ORDERING: The construction requires fixing γ̃ before r. Verify that the constraints C₁r⁴/γ̃² < c_V/2 and C(r²+γ̃) < γ*/2 are simultaneously satisfiable.

5. INTERFACE: Check that the listed outputs (7 sequence-uniform items and 5 datum-dependent items) are correctly categorized. In particular, is it true that no sequence-uniform bound on initial sectional curvature is needed?

## Integrated Scientific Memo

# 核验结论：当前 selected-support lemma **尚不成立**

核心的 maximal-function 选择、局部能量估计、collapse-cancelling product，以及“先定 \(\widetilde\gamma\)、后定 \(r\)”的参数次序基本正确；但全文至少有四处必须修复的实质性错误：

1. §2 的曲率分解和式 (2.4) 与声明的 operator-normalized 范数不一致；
2. 式 (2.5) \(8\pi^2\chi=I+J\) 为假，故当前 full-curvature budget 的证明不闭合；
3. Proposition 3.1 中归一化均值应为 \(3/4\)，不是 \(2/9\)；
4. §5.2–5.3 错误地从 Ricci 下界推出固定半径球的一致正体积下界；允许塌缩时这不成立。

此外，平滑 cutoff 的描述没有保持证明 support identities 所需的精确支撑包含关系。

---

## 1. Full-curvature budget

### 1.1 正确的 operator-normalized 恒等式

文中约定
\[
|\operatorname{Rm}|_{\rm op}^{2}
=\frac14 R_{ijkl}R^{ijkl},
\qquad |G|^2=\frac23.
\]
在此约定下，四维曲率正交分解给出
\[
\boxed{
|\operatorname{Rm}|_{\rm op}^{2}
=
|W|_{\rm op}^{2}
+\frac12|\operatorname{Ric}^{\circ}|_{\rm HS}^{2}
+\frac{s^2}{24}.}
\]
Chern–Gauss–Bonnet 为
\[
8\pi^2\chi(M)
=
\int_M
\left(
|W|_{\rm op}^{2}
-\frac12|\operatorname{Ric}^{\circ}|_{\rm HS}^{2}
+\frac{s^2}{24}
\right)d\mu.
\]
相减得到
\[
\boxed{
\int_M|\operatorname{Rm}|_{\rm op}^{2}\,d\mu
=
8\pi^2\chi(M)
+\int_M|\operatorname{Ric}^{\circ}|_{\rm HS}^{2}\,d\mu.}
\]

因此：

- (2.3) 中 \(|\operatorname{Ric}^{\circ}|^2\) 的系数应为 \(1/2\)；
- (2.4) 中积分系数应为 \(1\)，不是 \(3/2\)。

另一分支提出的 tensor-norm 公式不能用于核验这里声明的 operator normalization；在当前约定下，上述公式才是相容的。

### 1.2 \(E\) 的范数换算

\[
\delta_i=\|g^{-1}E_i\|_{\infty,\rm op}
\]
意味着
\[
|\operatorname{tr}E_i|\le4\delta_i,
\qquad |E_i|_{\rm HS}\le2\delta_i.
\]
又因 trace-free projection 是 Hilbert–Schmidt 正交投影，
\[
|\operatorname{Ric}^{\circ}|
=|E_i^\circ|
\le2\delta_i.
\]
故
\[
J_i=\frac1{8\pi^2}\int|E_i^\circ|^2
\le
\frac{\delta_i^2}{2\pi^2}\operatorname{Vol}(M_i).
\]
最终的 \(J_i\) 估计正确，但原文“\(|E|\le\delta_i\)”若指 Hilbert–Schmidt 范数则不正确。

### 1.3 体积上界正确

由 \(s=-4+\operatorname{tr}E_i\) 和 \(|\operatorname{tr}E_i|\le4\delta_i\)，当 \(\delta_i<1\) 时
\[
|s|\ge4(1-\delta_i),
\]
所以
\[
I_i\ge
\frac{(1-\delta_i)^2}{6\pi^2}\operatorname{Vol}(M_i).
\]
另一方面，
\[
I_i=J_i+\frac{2A_i}{3}-q_i
\le
\frac{\delta_i^2}{2\pi^2}\operatorname{Vol}(M_i)
+\frac{2A_i}{3}.
\]
于是
\[
\bigl((1-\delta_i)^2-3\delta_i^2\bigr)
\operatorname{Vol}(M_i)
\le4\pi^2A_i,
\]
从而对于充分小的 \(\delta_i\)，
\[
\operatorname{Vol}(M_i)\le C_VA_i.
\]
这里应使用 \(|s+4|\le4\delta_i\)，而不是仅凭一句 \(s\ge-4-4\delta_i\) 去平方。

### 1.4 当前 Euler-characteristic 论证错误，但可以修复

依照文中 \(I_i,J_i\) 的定义，
\[
I_i-J_i=2\chi(M_i)+3\tau(M_i)
=\frac{2A_i}{3}-q_i,
\]
而
\[
\boxed{I_i+J_i\neq8\pi^2\chi(M_i).}
\]
故 (2.5) 无效。§2 中 connected-sum Euler 公式也写错了；正确的是
\[
\chi(M_i)=\sum_j c_2(X_{j,i})+\chi(N_i)-2m_i.
\]

可按以下方式修补。Mixed SW inequality 给出
\[
I_i\ge\frac{2A_i}{3},
\]
结合 \(I_i=J_i+\frac{2A_i}{3}-q_i\)，得到
\[
0\le q_i\le J_i\le C\delta_i^2A_i.
\]
因
\[
D_i=\frac{A_i}{3}+q_i,
\]
故 \(D_i=O(A_i)\)。对于连通定向且 \(b_+(N_i)=0\) 的 \(N_i\)，
\[
(2\chi+3\tau)(N_i)=4-4b_1(N_i)-b_-(N_i),
\]
所以
\[
D_i=4(m_i-1)+4b_1(N_i)+b_-(N_i),
\]
进而
\[
|\chi(N_i)|\le C(1+D_i)=O(A_i).
\]

还需控制 \(\sum c_2(X_{j,i})\)。利用文献模块中允许调用的 general-type surface 数值不等式，例如 Noether inequality，可得
\[
c_2(X)\le C\,c_1^2(X),
\]
其中加法常数可由 \(c_1^2(X)\ge1\) 吸收。因此
\[
|\chi(M_i)|\le CA_i.
\]

最后用修正后的恒等式：
\[
\int|\operatorname{Rm}|^2
=
8\pi^2\chi(M_i)+\int|\operatorname{Ric}^{\circ}|^2
\le CA_i.
\]
并且
\[
F_T^2
=1+|\operatorname{Rm}-G|^2
\le\frac73+2|\operatorname{Rm}|^2,
\]
故
\[
\int F_T^2\le C A_i.
\]

结论是：**full-curvature budget 可以成立，但 Step 70 当前给出的证明不成立；必须替换 Euler-characteristic 步骤并修正范数系数。**

---

## 2. Volume lower bound 还需一项数值修正

令
\[
u=s+8\sqrt6\,|W^+|,
\qquad
d=\frac{s^2}{24}+2|W^+|^2.
\]
由 \(u\to0\) 和 \(s\to-4\)，极限满足
\[
|W^+|^2\to\frac1{24},
\]
所以
\[
d\to \frac{16}{24}+\frac{2}{24}
=\boxed{\frac34},
\]
不是 \(2/9\)。

更直接地，
\[
d=\frac{3s^2}{64}-\frac{su}{96}+\frac{u^2}{192},
\]
而 \(\int u^2\le108Q\)、\(Q\le4\delta_i^2\operatorname{Vol}\) 以及
\(|s+4|\le4\delta_i\) 给出
\[
\fint d\le\frac34+C\delta_i.
\]
再由
\[
\int d=4\pi^2I_i\ge\frac{8\pi^2}{3}A_i
\]
得到
\[
\operatorname{Vol}(M_i)
\ge
\frac{8\pi^2A_i/3}{3/4+C\delta_i}
=
\frac{32\pi^2}{9}A_i(1-O(\delta_i)).
\]
所以 Proposition 3.1 的最终常数正确，但中间的 \(2/9\) 及对应除法错误。

---

## 3. Weak-type maximal inequality 正确

Vitali \(5r\)-covering 给出互不相交的 \(B_{s_j}(x_j)\)，使超水平集被 \(B_{5s_j}(x_j)\) 覆盖。Ricci 下界
\[
\operatorname{Ric}\ge-(n-1)g
\]
下 Bishop–Gromov 给出
\[
\frac{\operatorname{Vol}(B_{5s}(x))}
     {\operatorname{Vol}(B_s(x))}
\le
\frac{V_{-1}(5s)}{V_{-1}(s)}
\le
C(n,R_0),
\qquad 0<s\le R_0.
\]
因此
\[
\operatorname{Vol}\{\mathcal M_{R_0}f>\lambda\}
\le
\frac{C(n,R_0)}{\lambda}\int_Mf.
\]

可取
\[
C(n,R_0)=
\sup_{0<s\le R_0}\frac{V_{-1}(5s)}{V_{-1}(s)}<\infty.
\]
当 \(R_0=10r\) 且 \(0<r\le r_0\) 时，该常数可由只依赖 \(n,r_0\) 的常数一致控制；当 \(r\downarrow0\) 时趋向 \(5^n\)。

Remark 4.2 中写出的
\[
V_{-1}(5R_0)/V_{-1}(R_0/5)
\]
不是证明实际使用的比值，应改为上述 supremum。这个笔误不影响 Lemma 4.1。

---

## 4. Packing/coloring 的现有证明错误，但结论可由 doubling 修复

Ricci 下界不能推出
\[
\operatorname{Vol}(B_{r/2}(x))\ge v_-(r/2)>0
\]
这样的绝对下界；这正是 collapse 情形下失效的命题。因此 (5.2)、(5.3) 当前写法错误。

有限性可直接由紧致性得到。图的统一次数界应改用相对体积比较。固定中心 \(x\)，设 \(y_j\) 是与其相邻的中心。则：

- \(B_{r/2}(y_j)\) 两两不交；
- \(y_j\in B_{14r}(x)\)，故 \(B_{r/2}(y_j)\subset B_{15r}(x)\)；
- \(B_{15r}(x)\subset B_{29r}(y_j)\)。

Bishop–Gromov 在 \(y_j\) 处给出
\[
\operatorname{Vol}(B_{r/2}(y_j))
\ge
\frac{V_{-1}(r/2)}{V_{-1}(29r)}
\operatorname{Vol}(B_{29r}(y_j))
\ge
c(n,r)\operatorname{Vol}(B_{15r}(x)).
\]
将两两不交的小球体积求和，
\[
\#\{y_j\}
\le
\frac{V_{-1}(29r)}{V_{-1}(r/2)}.
\]
由此得到 sequence-uniform 的有限颜色数，进而保留某个颜色类，使
\[
\sum_{\alpha\ {\rm retained}}\operatorname{Vol}(B_r(x_\alpha))
\ge\alpha_0A_i.
\]
所以 coloring 结论成立，但必须删除任何绝对 noncollapse 球体积下界。

---

## 5. Collapse-cancelling product 正确

对于 \(U_\alpha=B_{7r}(x_\alpha)\)，good-center 条件给出
\[
\int_{U_\alpha}|\operatorname{Rm}|^2
\le
\frac{\widetilde\gamma^2}{r^4}
\operatorname{Vol}(U_\alpha).
\]
又有
\[
F_T^2
=1+|\operatorname{Rm}-G|^2
\le
\frac73+2|\operatorname{Rm}|^2.
\]
因此
\[
\boxed{
H_{2,\alpha}(0)
\le
C\left(1+\frac{\widetilde\gamma^2}{r^4}\right)
\operatorname{Vol}(U_\alpha).}
\]
此式正确。

局部 normalized Sobolev inequality 给出
\[
\mathcal S_\alpha(0)
\le
Cr^2\operatorname{Vol}(U_\alpha)^{-1/2}.
\]
于是
\[
\begin{aligned}
\gamma_\alpha(0)
&=\mathcal S_\alpha(0)H_{2,\alpha}(0)^{1/2}\\
&\le
Cr^2\operatorname{Vol}(U_\alpha)^{-1/2}
\left[
\left(1+\frac{\widetilde\gamma^2}{r^4}\right)
\operatorname{Vol}(U_\alpha)
\right]^{1/2}\\
&=
C\sqrt{r^4+\widetilde\gamma^2}\\
&\le C(r^2+\widetilde\gamma).
\end{aligned}
\]
局部体积完全消去。这里无需 noncollapse，也无需 pointwise curvature bound。

---

## 6. 参数次序相容

记
\[
\gamma_\alpha(0)\le C_\gamma(r^2+\widetilde\gamma).
\]
先取
\[
0<\widetilde\gamma<
\frac{\gamma_*}{4C_\gamma},
\]
同时满足 downstream absorption 所需的小量条件。再取
\[
0<r<
\min\left\{
r_0,\,
\left(\frac{\gamma_*}{4C_\gamma}\right)^{1/2},\,
\left(\frac{c_V\widetilde\gamma^2}{2\overline C_1}\right)^{1/4}
\right\},
\]
其中 \(\overline C_1\) 是 \(0<r\le r_0\) 上 maximal-function 常数的统一上界。则同时有
\[
C_\gamma(r^2+\widetilde\gamma)<\frac{\gamma_*}{2},
\qquad
\frac{C_1r^4}{\widetilde\gamma^2}<\frac{c_V}{2}.
\]
故“先定 \(\widetilde\gamma\)，再定 \(r\)”没有矛盾或循环依赖。

---

## 7. Cutoff 平滑须保留精确 support nesting

原文所述 mollification 会把 \(\operatorname{supp}\chi_\alpha\) 扩张至
\(B_{6r+\varepsilon}\)，不能直接推出
\[
\operatorname{supp}\nabla\eta_\alpha
\subset\{a_i=0\}.
\]
应在平滑前预留缓冲，例如先构造：

- raw \(\chi_\alpha=1\) 于 \(B_{5r+\varepsilon}\)，在 \(B_{6r-\varepsilon}\) 外为零；
- raw \(\eta_\alpha=1\) 于 \(B_{6r+\varepsilon}\)，在 \(B_{7r-\varepsilon}\) 外为零；

再以更小尺度平滑。最终才可同时保持
\[
\chi_\alpha=1\text{ on }B_{5r},\quad
\operatorname{supp}\chi_\alpha\subset B_{6r},
\]
\[
\eta_\alpha=1\text{ on }B_{6r},\quad
\operatorname{supp}\eta_\alpha\subset B_{7r},
\]
以及
\[
a_i|\nabla\eta_\alpha|^2=0,\qquad
\nabla a_i\cdot\nabla\eta_\alpha=0.
\]
高阶 cutoff jets 仍只需 datum-dependent。

---

## 8. Interface 核验

修复上述问题后，可作为 sequence-uniform outputs 的是：

1. \(\int|\operatorname{Rm}|^2\le CA_i\)；
2. \(\int F_T^2\le CA_i\)；
3. \(c_VA_i\le\operatorname{Vol}(M_i)\le C_VA_i\)；
4. good-set 和 retained-color volume 的 \(A_i\)-比例下界；
5. doubling 导出的统一颜色数及 disjoint \(B_{7r}\)-supports；
6. global cutoff 的 \(0\le a_i\le1\)、一阶梯度界及精确 support identities；
7. \(\gamma_\alpha(0)\le C(r^2+\widetilde\gamma)\)；
8. \(Q_i(0)\le C\delta_i^2A_i\)。

只属 datum-dependent 或不能单独统一控制的是：

- \(\nabla^m\chi_\alpha\), \(m\ge2\)；
- per-datum existence time；
- 单独的 \(\mathcal S_\alpha(0)\)；
- 单独的 \(H_{2,\alpha}(0)\)；
- initial sectional curvature。

因此，**确实不需要 sequence-uniform 的初始 sectional-curvature 上界**。该模块只使用全局 \(L^2\) 曲率预算、局部平均曲率界及小乘积
\(\mathcal S_\alpha H_{2,\alpha}^{1/2}\)。每个固定光滑 datum 的曲率当然有限，并可影响其自身短时存在时间；序列一致的正时刻点态曲率必须由后续 smoothing/Moser 模块产生，而不能被视为本 lemma 已经证明的输入。

最终判定：selected-support lemma 的核心机制可修复成立，但 **Step 70 当前版本不是完整正确证明**；至少必须修正 (2.3)–(2.5)、Proposition 3.1 的均值、§5 的 collapse-incompatible packing 论证，以及 cutoff smoothing 的支撑保留。
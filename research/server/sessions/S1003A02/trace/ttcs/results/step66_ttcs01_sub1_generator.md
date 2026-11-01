# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step66_rank_one_exceptional_ricci_rigidity.md",
    "Sessions/S1003A02/workspace/notes/step65_cell_exceptional_flux_ledger.md",
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md",
    "Sessions/S1003A02/workspace/notes/step64_diffuse_twist_AAD_and_SW_zeros.md"
  ]
}
```

## Task

Context: the unrestricted Einstein-defect problem α(M)=inf∫|Ric°|² on M=X#kCP̄² (X minimal general type, A=c₁²(X), open range 0<k<A/3 where LeBrun's SW bound is vacuous). Step 65 proved a metric-only exceptional flux ledger p=(1−δ)²/‖h‖²+L (δ = exceptional Ricci-flux deficit, L ≥ 0 misalignment). Step 66 showed (on the constant-scalar slice, which is WLOG) that L splits as L_rank+L_amp; L_rank=0 is exactly the Riemannian Einstein–Maxwell system with F⁻ ∝ the exceptional harmonic ASD form ĥ_a; L=0 is the subclass with |F⁺| constant = AK metrics with J-invariant Ricci (Blair–Ianus class), joining cscK (δ=0, p=|a⁻|²≥k) to Einstein (δ=1, p=0). The near-equality Bianchi estimate gives no coercivity. Generate the strongest scientifically serious ideas for what new information could decide the open range, now that the problem is organized by Einstein–Maxwell theory: (i) Seiberg–Witten curvature estimates adapted to Einstein–Maxwell metrics or to metrics near the EM layer (what inequality, which class, which weight), and whether they would give a k-threshold or a k²/A law; (ii) whether the Blair–Ianus variational characterization (critical points of ∫s on ω-compatible metrics) plus Taubes' symplectic SW theory constrains the strictly-AK members with [ρ₀]∥a⁻ and δ near 1 (e.g. via c₁·[ω], Hermitian scalar curvature integrals, the exceptional (−1)-spheres being symplectic); (iii) a construction route: conformally Kähler or other EM metrics on general-type blow-ups with small L_amp and δ bounded away from 0, or an argument they cannot exist; (iv) a quantitative formulation that is genuinely weaker than Einstein nonexistence but still gives a tariff for metrics near the Kähler end (δ ≤ δ₀). For each idea give the exact inequality or construction, why it might work, the decisive first computation, and what would falsify it. Do not invent literature; name precise knowledge requests where needed.

## Output

令
\[
p=\frac1{8\pi ^2}\int_M|\Ric^\circ|^2,\qquad
Q=|a^-|^2\ge k,\qquad
\Phi=2\pi\sqrt Q,\qquad D=\delta\Phi .
\]
在 \(L=0\) 的非 Einstein 分支上，
\[
p=Q(1-\delta)^2,\qquad D=\delta\Phi .
\]
以下最有价值的新信息并不是另一条纯代数恒等式，而是 Einstein–Maxwell 结构与加权 Seiberg–Witten、Gray 型微分恒等式、辛典范类面积以及接合参数之间的交叉约束。

---

## 1. 以 \(F^+\) 为权的 Seiberg–Witten–Einstein–Maxwell 估计

### 1.1 应首先保留的加权 monopole 不等式

设 \(\psi\) 是非零调和自对偶二形式，\(\lambda _1(W^+)\) 是 \(W^+\) 的最小特征值。与 Kähler 等号校准一致的 LeBrun 型加权式应写成
\[
\int_M\left(\frac23s+2\lambda _1(W^+)\right)|\psi|\,d\mu
\le 4\pi\sqrt2\,a\cdot[\psi]                         \tag{1.1}
\]
其中 \(a\) 取符号使右端与 \(s<0\) 的 Kähler 情形一致。对 EM 度量，最自然的选择是
\[
\psi=F^+,
\]
而不是用 \(|h|\) 人为加权。原因是 \(F^+\) 本身闭且调和；若 \(F^+\) 无零点，则
\[
\widehat g=qg,\qquad q=\frac{|F^+|_g}{\sqrt2},\qquad \omega=F^+
\]
给出真正的 almost-Kähler 度量 \((\widehat g,\omega)\)。相应的 monopole 类应首先取
\[
b=c_1(J_\omega),
\]
随后再对 blow-up 符号族 \(a_\varepsilon\) 应用同一估计。

关键不是再次对 (1.1) 做 Cauchy–Schwarz，而是回到其证明并保留被丢弃的平方项。自然的精细余项应具有形式
\[
\begin{split}
\mathcal E_{a}(\psi)
:=&\,4\pi\sqrt2\,a\cdot[\psi]
-\int_M\left(\frac23s+2\lambda _1(W^+)\right)|\psi|\,d\mu\\
\ge &\ c_0\int_M\frac{|\nabla\psi|^2}{|\psi|}\,d\mu
+c_0\int_M|\psi|\,
 \frac{|\Pi_{\psi^\perp}(W^+(\widehat\psi))|^2}
 {|s|+|W^+|}\,d\mu ,                                  \tag{1.2}
\end{split}
\]
其中 \(\widehat\psi=\psi/|\psi|\)。两项分别测量：

* \(q\) 的变化及归一化方向 \(J_\psi\) 的扭转；
* \(W^+\) 偏离 \(J_\psi\)-不变退化型的程度。

等号时，(1.2) 把 EM 等号类送入 LeBrun 的 almost-Kähler 等号类。此时 EM 给出 \(J\)-不变 Ricci，而 LeBrun 等号给出 \(J\)-不变的特殊 \(W^+\)。二者相交正是 AAD 第三 Gray 条件所覆盖的结构，闭四维情形应迫使 Kähler。这里存在一个很强的“两个等号类横截”机制。

**首个决定性计算。** 在 Step 66 的 \(AK_{\rm Ric}\) 类上，把
\[
4\pi c_1(J)\cdot[\omega]=\int(s+2u)\,d\mu
\]
和 \(W^+\) 的 almost-Kähler 分解代入 \(\mathcal E_b(\omega)\)，将它精确化成
\[
u,\quad \rho_*'',\quad W_3^+
\]
的积分表达式，再与 (66.5) 比较。需要看余项保留的是：

\[
D^2\lesssim \mathcal E_b
\quad\text{还是仅有}\quad
\frac{D^4}{A}\lesssim \mathcal E_b.                    \tag{1.3}
\]

两种结果对应完全不同的尺度：

* 若进一步有 \(\mathcal E_b\lesssim p\)，则
  \[
  p\gtrsim D^2\asymp Q\delta^2.
  \]
  与 \(p\ge Q(1-\delta)^2\) 联合后得到 \(p\gtrsim Q\)，即每个 exceptional class 的固定费用。

* 若只能得到
  \[
  p\gtrsim\frac{D^4}{A}\asymp\frac{Q^2\delta^4}{A},
  \]
  则在 \(\delta\to1\) 时自然出现
  \[
  p\gtrsim \frac{k^2}{A}.
  \]
  这正是 Step 62 的 formal common mode 尺度。

能推翻第一种强形式的现象，是一列紧致 EM 或 \(AK_{\rm Ric}\) 度量，其 \(D\) 保持固定阶，而 \(\mathcal E_b/D^2\to0\)。若同时 \(\mathcal E_b\asymp D^4/A\)，则它反而支持 \(k^2/A\) 律。

### 1.2 符号族平均能看到什么

令 \(\omega=F^+\)。对全部 \(a_\varepsilon=K_X+\sum\varepsilon_iE_i\)，有精确恒等式
\[
2^{-k}\sum_\varepsilon
   \bigl(a_\varepsilon\cdot[\omega]\bigr)^2
=
\bigl(K_X\cdot[\omega]\bigr)^2
+\sum_i\bigl(E_i\cdot[\omega]\bigr)^2.                 \tag{1.4}
\]
因此，将加权 SW 估计在平方之前对符号族平均，能够保留 exceptional symplectic areas
\[
e_i=E_i\cdot[\omega].
\]
普通的最大符号论证会把这些信息压缩成 \(\Pi\)。这里应保留 \(\sum e_i^2\)，因为它可能与 \(F^-\propto a^-\) 的 Maxwell 能量共同形成逐点吹起费用。

仅有 \(e_i>0\) 仍不足以给出固定费用，因为 \(e_i\to0\) 是允许的。真正有力的结果应是 EM 方程导出的
\[
\sum_i e_i^2+\mathcal E_b(F^+)
\ \gtrsim\ Q\delta^2
\quad\text{或}\quad
\gtrsim\frac{Q^2\delta^4}{A}.                           \tag{1.5}
\]

### 1.3 接近 EM 层时应加入哪一个量

\(L_{\rm rank}\) 只通过 Bianchi 给出 \(\phi_h\) 的加权 \(H^{-1}\) 闭性；在 \(h\) 的零集附近，它不能自动产生一个真正的调和 \(F^+\)。因此，对“接近 EM”最自然的量是
\[
\mathfrak R_{\rm EM}(g,h)
=
\inf_{\psi\in\Omega^+}
\left[
 \|\Ric^\circ-\psi\circ h\|_2^2
 +\|(d+d^*)\psi\|_{H^{-1}_{|h|}}^2
\right].                                                \tag{1.6}
\]
目标式可取为
\[
\frac{D^4}{A}
\le C\bigl(p+\mathfrak R_{\rm EM}\bigr)                 \tag{1.7}
\]
或更强的 \(D^2\le C(p+\mathfrak R_{\rm EM})\)。这比直接从 \(L_{\rm rank}\) 推导普通 \(L^2\) Maxwell 场更贴合现有的 Bianchi 信息。

所需精确文献查询：

1. LeBrun 对任意调和自对偶二形式的加权 monopole 估计，确认 (1.1) 的常数、符号和等号结构；
2. 其证明中被舍弃平方项的完整形式，特别是 \(|\nabla|\psi||\)、归一化方向和 \(W^+\) 特征向量偏差；
3. Taubes 大参数扰动 \(\eta_r\propto rF^+\) 在 almost-Kähler 背景上的次阶展开，而不只是首阶典范类面积公式；
4. AAD 第三 Gray 条件闭情形证明中的积分恒等式，判断其量化后产生 \(D^2\) 还是 \(D^4/A\)。

---

## 2. Blair–Ianuş、Taubes 典范类与 \(\delta\to1\)

### 2.1 一个已经可精确推出的 \(A/3\) 机制

在 \(AK_{\rm Ric}\) 类中取 \(s=-4\)，令
\[
I=\int_Mu\,d\mu,\qquad K_\omega=-c_1(J).
\]
Hermitian scalar curvature 的拓扑公式给出
\[
4\pi K_\omega\cdot[\omega]=4V-2I.                       \tag{2.1}
\]
另一方面，(66.5) 与
\[
D^2\le\frac12\int u^2
\]
联合，精确推出
\[
I\ge \Phi^2\delta(1-\delta)+3\Phi^2\delta^2
=\Phi^2(\delta+2\delta^2).                              \tag{2.2}
\]
由于 \(\Phi^2=4\pi^2Q\)，
\[
K_\omega\cdot[\omega]
\le
\frac V\pi-2\pi Q(\delta+2\delta^2).                    \tag{2.3}
\]
Taubes 的 symplectic general-type 正性 \(K_\omega\cdot[\omega]>0\) 因而只给出
\[
\boxed{\ V>2\pi^2Q(\delta+2\delta^2).\ }                \tag{2.4}
\]
当 \(\delta\to1\) 且 \(V\approx2\pi^2A\) 时，(2.4) 正好变成
\[
Q<\frac A3.
\]
所以单纯使用 \(K_\omega\cdot[\omega]>0\)，其信息恰好停在已知 \(A/3\) 位置；它本身不会解决 \(0<k<A/3\)。

### 2.2 真正能推进的典范类面积不等式

对 symplectic blow-down 写
\[
K_\omega=K_0+\sum_iE_i,\qquad
[\omega]=[\omega_0]-\sum_i e_i\,\mathrm{PD}(E_i),
\]
于是
\[
K_\omega\cdot[\omega]=K_0\cdot[\omega_0]+\sum_i e_i,
\qquad
[\omega]^2=[\omega_0]^2-\sum_i e_i^2=2V.                \tag{2.5}
\]
若能在相关 \(AK_{\rm Ric}\) 类上证明 Kähler Hodge-index 型估计
\[
K_0\cdot[\omega_0]\ge\sqrt{A[\omega_0]^2},              \tag{2.6}
\]
则
\[
K_\omega\cdot[\omega]\ge\sqrt{2AV}.
\]
与 (2.1)–(2.2) 联合得到
\[
4\pi^2Q(\delta+2\delta^2)
\le
2V-2\pi\sqrt{2AV}.                                      \tag{2.7}
\]
写 \(V=2\pi^2(A+\upsilon)\)，便是
\[
Q(\delta+2\delta^2)
\le
A+\upsilon-\sqrt{A(A+\upsilon)}.                        \tag{2.8}
\]
当 \(\upsilon/A\) 很小时，右端为 \(\upsilon/2+O(\upsilon^2/A)\)，故
\[
\upsilon\gtrsim 2Q(\delta+2\delta^2).                   \tag{2.9}
\]
再与某个 EM 特有的上式
\[
\upsilon\le k+C\,p+C\,\mathfrak R_{\rm EM}              \tag{2.10}
\]
联合，就会直接产生固定费用或 \(k^2/A\) 估计。

(2.6) 在一般 \(b^+>1\) 的辛几何中并不由交叉形式的线性代数自动得到；其成立必须来自 \(AK_{\rm Ric}\)、Chern 形式的型分解或 Taubes 曲线结构。能推翻这一方向的最清楚现象，是固定体积的 general-type 辛形式序列满足
\[
K_0\cdot[\omega_0]\to0
\]
而 \(K_0^2=A>0\)。

### 2.3 逐个 exceptional sphere 的 Chern 通量

若同一个 \(J\) 下 \(E_i\) 有 \(J\)-holomorphic 代表，则
\[
c_1(J)\cdot E_i=1.
\]
Step 64–66 的 frame curvature 分解应在该球面上给出
\[
2\pi
=
\frac{s}{4}e_i
+\int_{E_i}\rho_0
+\int_{E_i}t_J,                                         \tag{2.11}
\]
其中 \(e_i=\int_{E_i}\omega>0\)。当 \(\delta\to1\) 时，\(\rho_0\) 很小；又因 \(s<0\)，第一项与 \(2\pi\) 方向相反，所以扭转项必须承担超过 \(2\pi\) 的通量。

决定性局部计算是求 \(t_J|_{TE_i}\) 的精确公式。若能证明
\[
\left|\int_{E_i}t_J\right|
\le C\int_{E_i}u\,dA                                   \tag{2.12}
\]
并利用正规丛 \(E_i^2=-1\) 把右端传到四维 \(\int u^2\)、\(W_3\) 或 Ricci defect，就会产生逐球费用。若 \(t_J|_{TE_i}\) 可通过任意细的管状区域承担固定通量而四维相关能量趋零，则这种逐球路线被推翻。

这里需要确认 Taubes–Gromov 理论是否为给定的 \(AK_{\rm Ric}\) 之 \(J\) 提供 \(E_i\) 的嵌入 \(J\)-holomorphic 球，而不只是对另一个 tame \(J\) 提供代表。

### 2.4 Blair–Ianuş Hessian，而不只是临界点陈述

固定 \(\omega\) 时，
\[
\int s\,d\mu
=
4\pi c_1(J)\cdot[\omega]-2\int u\,d\mu.                 \tag{2.13}
\]
因此 \(J\)-不变 Ricci 等价于 \(I(J)=\int u\) 在 \(\omega\)-compatible \(J\) 空间中的临界点。可计算的对象是其 Hessian：
\[
\mathrm{Hess}_J I(A,A),
\qquad AJ+JA=0.
\]
对支持在 exceptional 球面附近的 \(A\)，零阶项会显式含有
\[
\rho_0=Fh,\qquad E_i^2=-1.
\]
若所有 \(F\ll\Phi\) 的严格 almost-Kähler 临界点都存在一个方向使一阶驻定方程不成立，便可排除 \(\delta\) 接近 \(1\) 的 \(AK_{\rm Ric}\) 解。更现实的结果是：每个 exceptional sphere 贡献一个 Hessian 的下降方向。这本身不排除鞍点，但若该 EM 解同时来自 \(\alpha\) 的局部极小结构，则会变得有效。

首个计算应在 cscK blow-up 上完成：写出 Hessian 的主符号与零阶曲率项，识别其核是否仅由复结构变形和 Hamiltonian 对称产生。若出现一个核向量使 \(\dot\delta\ne0\)，则存在严格 AK 分支的无穷小种子。

所需文献查询：Blair–Ianuş 一阶与二阶变分的原始公式；Donaldson moment-map 形式下总 Hermitian scalar curvature的 Hessian；给定 tame \(J\) 下 exceptional 类的球面代表定理。

---

## 3. 构造：先处理 conformally Kähler，再处理真正的 EM 接合

### 3.1 Conformally Kähler EM 在 general-type 拓扑上很可能只能给出常数因子

若
\[
g=f^{-2}g_K
\]
是 strongly Hermitian Einstein–Maxwell，则现有分类理论通常把 \(f\) 识别为 \(g_K\) 的实 holomorphy potential；非恒定 \(f\) 产生非零 holomorphic vector field。紧致 general-type 复曲面的自同构群是离散的，吹起也不会凭空产生连续 holomorphic 对称。因此，只要分类定理的假设与当前 EM 约定完全吻合，就应有
\[
f\equiv\mathrm{const}.
\]
于是 \(L_{\rm amp}=0\)，且该路线退回 cscK，而不能构造 \(\delta>0\)。

这里的决定性文献查询是：

* 紧致 strongly Hermitian Einstein–Maxwell 四维分类中，是否确实推出 \(J\nabla f\) 为 holomorphic Killing field；
* 结论是否需要 \(F\) 的额外 \(J\)-不变性；
* 任意 Kähler 结构落在 \(X\#k\overline{\mathbf{CP}}^{\,2}\)、\(b^+>1\) 上时，Kodaira dimension 是否必为 \(2\)，从而 \(H^0(T^{1,0})=0\)。

能推翻这一排除机制的对象，是该光滑四维流形上的非恒定 strongly Hermitian EM 度量，而其关联复结构仍无 holomorphic vector field。

### 3.2 一般 EM 的精确 almost-Kähler 重写

令
\[
q=\frac{|F^+|_g}{\sqrt2},\qquad \widehat g=qg,\qquad
\omega=F^+,\qquad \ell=\log q,\qquad h=F^-.
\]
则 \(|\omega|_{\widehat g}^2=2\)，且 \(\omega,h\) 都对 \(\widehat g\) 调和。按 Step 66 的归一化，EM 方程等价于
\[
\Ric^\circ_{\widehat g}
+\left(\widehat\nabla^2\ell+\frac12d\ell\otimes d\ell\right)_0
=
q\,\omega\circ_{\widehat g}h,                           \tag{3.1}
\]
以及
\[
s_g
=
q\left(
s_{\widehat g}
+3\widehat\Delta\ell
-\frac32|d\ell|_{\widehat g}^2
\right)=\mathrm{const}.                                 \tag{3.2}
\]
同时，原始 amplitude loss 的未归一化形式正是
\[
\Lambda_{\rm amp}
=
2\int_M(q-\bar q_h)^2|h|_{\widehat g}^2\,d\mu_{\widehat g},
\qquad
\bar q_h=
\frac{\int q|h|^2}{\int|h|^2}.                          \tag{3.3}
\]

方程 (3.1) 的 \(J\)-反不变部分是关键：
\[
\Ric_{\widehat g}''
+
\left(\widehat\nabla^2\ell+\frac12d\ell\otimes d\ell\right)''
=0.                                                      \tag{3.4}
\]
若由 (3.4) 能推出 Hamiltonian 向量场
\[
X_q=J\widehat\nabla q
\]
是 \(\widehat g\)-Killing，则非恒定 \(q\) 会产生 Hamiltonian circle action。闭辛四维流形具有 Hamiltonian circle action时属于 rational 或 ruled 类型；这与 general type 的 blow-up 拓扑不相容。因此
\[
q\equiv\mathrm{const},
\]
从而整个 EM 层缩到 \(L=0\)。

**首个计算。** 将 (3.4) 与 \(\mathcal L_{X_q}J\) 配对并积分，寻找
\[
\int q^{-m}|\mathcal L_{X_q}J|^2
=
\int q^{-m}\langle \Ric_{\widehat g}'',\mathcal T(dq,\nabla J)\rangle .
\]
再用 almost-Kähler Ricci 恒等式和 Maxwell 方程处理右端。若右端恰为散度或由 EM 的 \(J\)-不变应力抵消，则得到所需 Killing 结论。若存在紧致 EM 例子使 \(X_q\) 明显不是 Killing，这一路会被直接推翻。

### 3.3 带电 Taub–Bolt–AdS 接合是最值得计算的构造

Step 64 的纯 Einstein Taub–Bolt–AdS \(O(-1)\) 内部给出 \(P=0\)，但其接合超曲面的第一阶 Cauchy 数据与 CH 球不匹配。Einstein–Maxwell 家族增加电、磁参数，正好可能补足缺少的自由度。可采用
\[
g=\frac{dr^2}{V(r)}
+a(r)^2(\sigma_1^2+\sigma_2^2)
+c(r)^2\sigma_3^2,
\qquad
F=d(\psi(r)\sigma_3)+q_m\,\sigma_1\wedge\sigma_2,       \tag{3.5}
\]
并施加：

* bolt 光滑条件；
* \(\int_EF^-=2\pi\)；
* \(s=-4\)；
* 与 CH 小球在某个 \(r=R\) 上的诱导度量、第二基本形式和 Maxwell Cauchy 数据匹配。

定义有限维错配映射
\[
\mathcal M(n,q_e,q_m,r_b,R)
=
(\text{两个 squashing 数据},
 \text{两个二基本形式数据},
 \text{Maxwell 通量数据}).                             \tag{3.6}
\]
首个决定性工作是求 \(\mathcal M\) 在小 bolt 参数下的渐近展开，并看电参数是否改变 Step 64 中不可调的 Ricci/Lichnerowicz cokernel 配对符号。

若存在 \(\mathcal M=0\) 且
\[
\frac{\|F^+\|_{\text{core}}}{\|F^-\|_{\text{core}}}\ll1,
\]
那么核心区域同时具有 \(\delta\approx1\) 和很小的 Ricci defect；剩余问题只是多个核心及外部 Maxwell 场的全局接合。若所有光滑 \(O(-1)\) EM 解的错配映射始终同号，或唯一零点迫使 \(F^+\) 取 cscK 校准值，则这种构造被排除。

---

## 4. 一个确实不触及 Einstein 端点的量化目标

### 4.1 仅用 ledger 已有的局部 tariff

对任意固定 \(0<\delta_0<1\)，
\[
\delta\le\delta_0
\quad\Longrightarrow\quad
p\ge Q(1-\delta_0)^2
\ge k(1-\delta_0)^2.                                   \tag{4.1}
\]
所以
\[
P\ge8\pi^2k(1-\delta_0)^2.                              \tag{4.2}
\]
这完全不涉及 \(\delta=1\) 的 Einstein 度量。真正需要增加的是一个几何上可识别的条件，使 \(\delta\le\delta_0\) 可由曲率、谱或与 cscK 模空间的距离推出。

### 4.2 最自然的全局弱形式

比 \(L\ge c\delta\) 更符合光滑变分阶数的是
\[
\boxed{\quad
L\ge c_0Q\delta^2,
\qquad 0\le\delta\le\delta_0<1.
\quad}                                                   \tag{4.3}
\]
它不对 Einstein 端点作任何陈述。由 ledger，
\[
p\ge Q\bigl[(1-\delta)^2+c_0\delta^2\bigr].
\]
因此
\[
p\ge Q\,m(c_0,\delta_0),                                \tag{4.4}
\]
其中
\[
m(c_0,\delta_0)=
\begin{cases}
(1-\delta_0)^2+c_0\delta_0^2,
&\delta_0\le(1+c_0)^{-1},\\[1mm]
\dfrac{c_0}{1+c_0},
&\delta_0\ge(1+c_0)^{-1}.
\end{cases}
\]
这给出真正的 per-class tariff，同时允许 \(\delta>\delta_0\) 的 diffuse、EM 或 Einstein 型几何另行处理。

### 4.3 在 cscK 端的首个谱计算

设 \(g_K\) 是无 holomorphic vector field 的 cscK blow-up，且 primitive Ricci form 对应 \(h_K\)。固定微分同胚与缩放规范，考察
\[
g_t=g_K+t\dot g+O(t^2).
\]
由于 \(L(g_K)=0\) 且 \(L\ge0\)，其一阶变分消失。定义
\[
c_K
=
\inf_{\dot g:\,\dot\delta=1}
\frac{\frac12D^2L_{g_K}(\dot g,\dot g)}{Q}.              \tag{4.5}
\]
若
\[
c_K>0,
\]
则在 \(g_K\) 的 Sobolev 邻域内得到
\[
L\ge \frac{c_K}{2}Q\delta^2,                            \tag{4.6}
\]
从而得到 (4.4)。

这里的核心线性代数是
\[
\ker D^2L_{g_K}
=
\{\text{线性化 EM 解，且 }|F^+|\text{ 一阶常数}\}
\]
是否成立，以及
\[
D\delta\big|_{\ker D^2L}=0                              \tag{4.7}
\]
是否成立。若核中存在 \(\dot\delta\ne0\) 的向量，则 (4.3) 的二次形式被推翻，同时它给出一条严格 almost-Kähler EM 分支的无穷小候选。若核只有 Kähler 模、复结构模和规范方向，而这些方向都满足 \(\dot\delta=0\)，则局部 tariff 很有希望。

这个线性化计算比处理整个 \(0<k<A/3\) 区间轻得多，却能产生严格而有用的结果；它也能直接比较 CH/Burns cell 中观察到的 \(L/\delta\approx1\) 与光滑 cscK 邻域中预期的 \(L\sim\delta^2\)。

---

## 5. 最有区分力的三项计算

1. **在 \(AK_{\rm Ric}\) 上精确展开加权 SW 余项。**  
   判明它控制 \(D^2\) 还是 \(D^4/A\)。前者导向固定费用，后者导向 \(k^2/A\)。

2. **计算 cscK 端的广义特征值 \(c_K\)。**  
   这直接决定局部式 \(L\ge c_KQ\delta^2\)，且不触碰 Einstein 端点。

3. **计算带电 Taub–Bolt–AdS 的错配映射 \(\mathcal M\)。**  
   它会说明 Maxwell 参数究竟能否消除纯 Einstein 接合中残留的 cokernel 模；这是目前最具体的低 \(p\)、大 \(\delta\) 构造试验。

整体上，普通 Taubes 正性只重现 \(A/3\)；要进入 \(0<k<A/3\)，必须取得以下三类信息之一：加权 SW 等号的量化余项、典范类面积相对体积的强化式、或带 Maxwell 电荷的真实接合解。三者分别对应固定费用、\(k^2/A\) 律和 \(\alpha(M)\) 可能趋零的几何机制。
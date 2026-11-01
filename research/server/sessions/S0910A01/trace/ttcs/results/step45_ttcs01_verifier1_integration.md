# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 45,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step45_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step45_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical correctness of the consolidated restricted negative Ishida-LeBrun gap theorem proof. Focus on three load-bearing points:

1. **Proposition 3.2 (quantitative local Φ lower bound from compactness).** The proof argues: on Riemannian 4-balls with |Rm| ≤ K and Vol(B_{ρ/2}) ≥ v₀, the density Φ = |E|² + (s+4)² + (s+8√6|W⁺|)² + G has fint Φ ≥ η(K,ρ,v₀) > 0. Otherwise a minimizing sequence converges smoothly (Cheeger-Gromov) to a germ with Φ ≡ 0, which is Einstein with the calibrated W⁺ spectrum, contradicting Derdziński. Is this compactness argument valid? Are the hypotheses sufficient for smooth subsequential convergence on B_{ρ/2}? Does Φ = 0 really force all four calibrated conditions, or could a density vanishing in the mean have a nontrivial limit? Does the passage from mean-zero Φ to pointwise Φ=0 on the limit require strong L¹ convergence (which Cheeger-Gromov does supply) or something else?

2. **Terminal averaging and support-count independence.** The Liouville average integral over P_i^in is claimed to be bounded by C(K,ρ)∫_M Φ without a factor depending on the number of supports. Check whether the Liouville-Rauch double integral over P_i^in can indeed be controlled by a single global integral of Φ over M, given bounded curvature and the fact that different centers' pullback images may overlap in M.

3. **Coefficient regularization order of operations.** The proof constructs regularized flows b_ε = χ² + ε² for each ε > 0, obtains ε-uniform bounds from the geometric energies (NOT from the ε-dependent PDE constants), passes to a smooth limit solving the exact a = χ² equation, and only THEN applies stationary-complement and disjoint-support identities. Check whether the ε-uniform geometric bounds (§5.2 properties) are indeed sufficient for a common existence time and smooth compactness, or whether additional information is needed.

## Integrated Scientific Memo

# 独立核验结论

## 总结

这三个承重点的状态不同：

1. **命题 3.2 的结论可以成立，但现有证明不成立。**  
   仅由
   \[
   |\mathrm{Rm}|\le K,\qquad \operatorname{Vol}(B_{\rho/2})\ge v_0
   \]
   不能推出光滑 Cheeger–Gromov 收敛；必须利用 \(\Phi\) 中的
   \(|E|^2\) 项，通过调和坐标下的 Ricci 方程取得强
   \(W^{2,p}\) 收敛，进而取得曲率强 \(L^p\) 收敛。

2. **终端 Liouville 平均确实不产生支撑个数因子。**  
   重叠发生在底流形上并不重要；在单位切丛上使用 Liouville 测度和测地流不变性，可一次性控制所有中心。需要明确小半径、测地缓冲和半径归一化。

3. **系数正则化的操作顺序正确，但共同存在时间及光滑紧性尚未被所给材料独立证明。**  
   (5.2) 中的代数界是必要结构输入，却不足以单独推出共同时间。还需要完整的、在正则化流层面成立的固定坐标一致估计，包括度量等价、无权曲率导数、连接差和时间导数。所给文件验证了最高阶 cutoff jet 的关键权重结构，但没有完整展示这套解析闭合。

因此，当前 consolidated note 还不是可独立复现的完整证明；主要未闭合对象是 **正则化流的 \(\varepsilon\)-一致短时存在与固定坐标全阶紧性模块**。

---

## 1. 命题 3.2：应替换其紧性证明

### 1.1 原证明中的错误

由有界曲率和体积非塌缩，缩小到内部球并选取调和坐标后，一般只能直接得到
\[
g_k\to g_\infty\quad\text{于 }C^{1,\alpha},
\qquad
g_k\rightharpoonup g_\infty\quad\text{于 }W^{2,p}.
\]
仅有 \(|\mathrm{Rm}_{g_k}|\le K\) 而无各阶曲率导数界，不能引用光滑 Cheeger–Gromov 紧性。

这不是措辞上的小问题。弱 \(W^{2,p}\) 收敛不足以把 Weyl 张量范数及谱函数 \(\mathcal G\) 强传到极限；原则上可能损失校准 Weyl 张量，甚至留下 \(W_\infty^+=0\) 的 Einstein 极限，从而无法使用 Derdziński。

### 1.2 正确的椭圆升级

反设存在一列球满足命题假设且
\[
\fint_{B_{\rho/2}}\Phi_{g_k}\to0.
\]
固定曲率和半径给出统一体积上界，因此
\[
\int_{B_{\rho/2}}\Phi_{g_k}\to0.
\]
特别地，
\[
E_k:=\operatorname{Ric}_{g_k}+g_k\to0
\quad\text{强于 }L^2.
\]
又因 \(|\mathrm{Rm}_{g_k}|\le K\)，\(E_k\) 一致有界，故经插值
\[
E_k\to0\quad\text{强于每个有限 }L^p.
\]

曲率界加非塌缩在一个较小内球上给出统一调和半径。在调和坐标中，
\[
g_k^{ab}\partial_a\partial_b(g_k)_{ij}
=
-2\operatorname{Ric}_{ij}(g_k)
+Q_{ij}(g_k^{-1},\partial g_k),
\]
而
\[
\operatorname{Ric}(g_k)=-g_k+E_k.
\]
系数由 \(C^{1,\alpha}\) 收敛而强收敛，\(E_k\to0\) 强于 \(L^p\)。内部椭圆估计遂给出
\[
g_k\to g_\infty
\quad\text{强于 }W^{2,p}_{\mathrm{loc}}
\]
（可取每个有限 \(p\)，至少先取足够大的 \(p\)）。因此
\[
\mathrm{Rm}_{g_k}\to\mathrm{Rm}_{g_\infty}
\quad\text{强于 }L^p_{\mathrm{loc}}.
\]

这才是将平均零传递为极限点态零的关键。由于 \(\Phi\) 是有界曲率范围内曲率的连续代数函数，
\[
\Phi_{g_k}\to\Phi_{g_\infty}
\quad\text{于 }L^1_{\mathrm{loc}},
\]
故
\[
\int\Phi_{g_\infty}=0.
\]
非负性给出 \(\Phi_{g_\infty}=0\) 几乎处处；同时 \(E_\infty=0\)，于是极限为弱 Einstein 度量，并由调和坐标下的椭圆正则性光滑化。最终所有校准恒等式点态成立。

需要注意边界：上述结论先在严格较小的内球上成立。命题只需得到一个非空 Einstein germ，因此可把最终球缩小一次，或在命题中预留例如 \(B_{\rho/4}\) 的缓冲。

### 1.3 \(\Phi=0\) 的代数确实给出完整校准谱

由
\[
E=0
\]
得
\[
\operatorname{Ric}=-g,\qquad s=-4.
\]
由第三项为零，
\[
-4+8\sqrt6\,|W^+|=0,
\]
故
\[
|W^+|^2=\frac1{24}.
\]

令 \(w\) 为 \(W^+\) 最小特征值。按文中的定义
\[
f=\frac23s-2\sqrt{\frac23}|W^+|=-3,
\qquad
a_*=\frac23s+2w=-\frac83+2w.
\]
由于 \(w\le0\)，这里 \(a_*<0\)。若明确约定
\[
a_{*,-}=\max\{-a_*,0\},
\]
则 \(\mathcal G=0\) 给出 \(a_*=-3\)，从而
\[
w=-\frac16.
\]
另两个特征值 \(x,y\) 满足
\[
x+y=\frac16,\qquad
x^2+y^2=\frac1{72},
\]
所以
\[
x=y=\frac1{12}.
\]
因此
\[
\operatorname{spec}(W^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

故不存在“平均趋零但极限保留非平凡误差”的问题，前提是采用上述强曲率收敛，而不是仅用弱 Cheeger–Gromov 紧性。

### 1.4 Derdziński 矛盾

极限 Einstein，故 \(\delta W^+=0\)。其 \(W^+\neq0\) 且只有两个特征值；Derdziński 定理使
\[
(24|W^+|^2)^{1/3}g_\infty=g_\infty
\]
局部 Kähler。另一方面，四维 Kähler–Einstein 且 \(s=-4\) 时
\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
与 \(1/24\) 矛盾。

因此命题 3.2 的结论可保留，但证明必须改为“调和坐标紧性 + \(|E|^2\) 驱动的椭圆强收敛”。

---

## 2. 终端平均没有支撑数量因子

令 \(P=P_i^{\rm in}\)。在每个相关测地段均留在有界曲率 plateau 内、且 \(\rho\) 小于统一比较半径时，设
\[
D_p=\int_{S_pM}\int_0^\rho J_p(t,\xi)\,dt\,d\xi.
\]
Jacobi 场比较给出
\[
c(K,\rho)\rho^4\le D_p\le C(K,\rho)\rho^4,
\qquad
J_p(t,\xi)\le C(K,\rho)t^3.
\]
于是
\[
A_\rho\Phi(p)
\le
\frac{C}{\rho^4}
\int_{S_pM}\int_0^\rho
t^3\Phi(\gamma_{p,\xi}(t))\,dt\,d\xi.
\]
在 \(P\) 上积分，并将 \(SM|_P\) 扩张到整个 \(SM\)：
\[
\begin{aligned}
\int_P A_\rho\Phi\,d\mu
&\le
\frac{C}{\rho^4}
\int_0^\rho t^3
\int_{SM|_P}\Phi(\pi G_t v)\,dL(v)\,dt\\
&\le
\frac{C}{\rho^4}
\int_0^\rho t^3
\int_{SM}\Phi(\pi G_t v)\,dL(v)\,dt.
\end{aligned}
\]
Liouville 测度在测地流下不变，因此
\[
\int_{SM}\Phi(\pi G_t v)\,dL(v)
=
|S^3|\int_M\Phi\,d\mu.
\]
故
\[
\int_P A_\rho\Phi\,d\mu
\le C(K,\rho)\int_M\Phi\,d\mu.
\]

这里没有支撑数量因子。不同中心的指数映射像可以在 \(M\) 上重叠，但整个积分是在单位切丛中计算；Liouville 不变性已经统一控制所有起点与方向。

需要补两点：

* Proposition 3.2 的下界写在 \(B_{\rho/2}\)，而 \(A_\rho\) 使用半径 \(\rho\)。由 \(\Phi\ge0\) 及体积比较，只能推出
  \[
  A_\rho\Phi(p)\ge c(K,\rho,v_0)\eta,
  \]
  应重新命名常数，而不能默认同一个数值 \(\eta\)。

* 若使用上述 Liouville 证明，仅需沿相关测地段的曲率比较及分母下界，不必额外假设终端度量在整个 \(M\) 上有统一 Ricci 下界。若改用底流形 Fubini 球体积证明，则必须另证终端全局体积上界/下 Ricci 界。前者更干净。

---

## 3. 系数正则化：顺序正确，但一致存在模块未闭合

### 3.1 正确的操作顺序

对
\[
b_\varepsilon=\chi^2+\varepsilon^2
\]
而言，在 \(\chi=0\) 区域仍有
\[
\partial_tg_\varepsilon
=-2\varepsilon^2(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon),
\]
所以有限 \(\varepsilon\) 时：

* 补集并不静止；
* 外部度量并未冻结；
* 精确的互不相交支撑求和恒等式不能使用。

只有在固定坐标中取得光滑极限
\[
g_\varepsilon\to g,\qquad b_\varepsilon\to\chi^2
\]
之后，才能得到
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g)
\]
并应用 stationary-complement 与 disjoint-support 身份。该顺序完全正确。

### 3.2 (5.2) 本身不够

下列界
\[
0<b_\varepsilon\le2,\quad
\nabla^r b_\varepsilon=\nabla^r(\chi^2),\quad
\frac{|\nabla b_\varepsilon|^2}{b_\varepsilon}\le4|d\chi|^2,\quad
\frac{\chi^2}{b_\varepsilon}\le1
\]
是关键的结构性输入，尤其保证最高 cutoff jet 能与
\[
\int b_\varepsilon|\nabla U_m|^2|U_m|^{p-2}
\]
配对。Step 43 对两个最高阶来源均带 \(\chi\) 权重的追踪，是支持这一点的重要证据。

但这些代数界不能单独推出共同存在时间或光滑紧性。一个充分的一致估计包至少应包含：

\[
\Lambda^{-1}g_0\le g_\varepsilon(t)\le\Lambda g_0,
\]
以及在固定有限图册中，对每个 \(m\),
\[
\sup_{\varepsilon,t\le T_*}
\|\nabla_0^m g_\varepsilon(t)\|_{L^\infty}<\infty,
\]
并有相应时间导数界。为从几何能量推出这些界，还需明确：

1. \(\varepsilon\)-一致的初始能量；
2. 共同区间上的零阶界
   \[
   \sup|U_\varepsilon|
   =\sup|b_\varepsilon T_\varepsilon|\le K;
   \]
3. 无权 \(T_\varepsilon\) 及其各阶导数估计；
4. 一致 Sobolev 常数和度量等价；
5. 固定背景连接差
   \(\nabla^{g_\varepsilon}-\nabla^{g_0}\) 的控制；
6. DeTurck diffeomorphism/transported coefficient 的一致正则性；
7. 将协变导数估计转换为固定坐标估计；
8. 由方程获得时间导数估计。

仅控制
\[
U_\varepsilon=b_\varepsilon T_\varepsilon
\]
不够：在 \(\chi=0\) 处 \(b_\varepsilon=\varepsilon^2\)，它允许
\[
|T_\varepsilon|\sim\varepsilon^{-2}.
\]
因此无权 \(T\)-链条不是可省略的技术细节。

### 3.3 所给材料尚不能独立验证共同时间

Step 43 验证了最高 cutoff jet 的来源及其 \(\chi\) 权重，并给出当前配对
\[
(U_m,C_{m+1})
\]
的正确能量结构。这解决了一个必要的导数损失问题，但不等同于完整证明：

* 正则化流在共同区间内存在；
* 所有固定坐标导数一致有界；
* 可在同一流形、同一固定 \(\chi\) 上光滑取极限。

Step 45 §5.2 将这些作为已获得结论，但当前输入没有展示完整的 continuation argument。尤其必须避免循环：

1. 先在正则化方程上证明不使用 frozen complement 的 \(\varepsilon\)-一致短时估计；
2. 再取固定坐标光滑极限，得到精确退化流；
3. 此后才能用 stationary complement、全局 \(Q\) 求和和 first-exit 的精确支撑结构；
4. 再据此延拓或重启。

如果共同时间的证明在取极限前调用了依赖冻结补集的 first-exit/global-\(Q\) 恒等式，则论证是循环的。现有文字宣称没有这样做，但没有给出足够细节核验。

此外，极限应明确为 **固定坐标收敛**，而非仅“模微分同胚的 Cheeger–Gromov 收敛”；否则固定函数 \(\chi\) 及支撑位置可能被移动，后续 stationary-complement 身份无法直接沿用。

---

## 最终判定

* **命题 3.2：可修复且结论可信。** 原“有界曲率 + 非塌缩 \(\Rightarrow\) 光滑收敛”错误；应以 \(|E|^2\to0\) 和调和坐标 Ricci 方程取得强曲率收敛。
* **终端平均：正确。** Liouville–Rauch 论证天然独立于支撑数量；需处理小半径、测地缓冲及 \(\rho/2\) 与 \(\rho\) 的常数转换。
* **系数正则化：操作顺序正确，但完整性未验证。** (5.2) 是必要而非充分条件。当前最精确的未解决对象是：构造一个不使用精确支撑冻结性质的、\(\varepsilon\)-一致固定坐标短时存在与全阶估计定理。

因此，基于所给材料，不能把 consolidated restricted negative Ishida–LeBrun gap theorem 认定为已完整证明；前两点可严格修复，第三点仍需补出独立可复核的解析模块。
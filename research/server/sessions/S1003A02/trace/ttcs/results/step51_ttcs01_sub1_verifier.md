# TTCS Independent Branch Record

```json
{
  "step_id": 51,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step50_minimizer_entry_PS_noncollapsed_alternative.md",
    "Knowledge/objects/papers/Fourth-order-curvature-flows-and-geometric-applications--db88daa8ad64--7e5bf41704a0/object.md"
  ]
}
```

## Task

The active goal is a rigorous noncollapsed structure theorem for minimizing sequences of P(g)=∫|Ric°|² on closed four-manifolds. Read the Step-50 note and the cited Bour fourth-order-flow source. Scrutinize only Theorem 50.A/Lemma W: (i) scaling of the L2 gradient and the weight rho^4; (ii) whether a smoothed curvature scale with all asserted derivative bounds exists without injectivity/noncollapse; (iii) whether multiplying the fourth-order DeTurck flow by a fixed variable weight yields a uniform own-scale existence interval on possibly collapsed metrics; (iv) whether energy descent yields the stated global weighted L2 residual and enough local residual after rescaling; (v) whether the selected metric stays in or can be returned to the scalar -4 Yamabe slice without losing residual. Identify exactly what is proved, what is plausible but unwritten, and what is false. Give a corrected theorem statement with the weakest sufficient entrance hypothesis if the construction is not yet a theorem.

## Output

# 科学核验备忘录：Theorem 50.A / Lemma W

## 总结

1. **\(\rho^4\) 的指数与 \(L^2\)-梯度缩放完全正确。**  
   若 \(g_\lambda=\lambda^2g\)，则
   \[
   \operatorname{Grad}P(g_\lambda)=\lambda^{-2}\operatorname{Grad}P(g)
   \]
   作为 \((0,2)\)-张量，并且
   \[
   |\operatorname{Grad}P(g_\lambda)|_{g_\lambda}^2\,d\mu_{g_\lambda}
   =\lambda^{-4}|\operatorname{Grad}P(g)|_g^2\,d\mu_g.
   \]
   因而 \(\rho^4|\operatorname{Grad}P|^2d\mu\) 尺度不变；在半径 \(r\) 的区域重标度时，\(r^4\int|\operatorname{Grad}P|^2\) 正是正确量。

2. **对每个固定的光滑 \((g_0,\rho)\)，固定权重的 DeTurck 方程有某个短时间光滑解。**  
   若使用
   \[
   \partial_tg=-w\,\operatorname{Grad}P(g)+\mathcal L_{\,wV_B(g)}g,
   \qquad w=\rho^4,
   \]
   其中 \(V_B\) 是 Bour 的三阶 DeTurck 向量场，则主符号是 \(w\) 乘以 Bour 的强椭圆主符号；\(dw\otimes V_B\) 仅为三阶项。因为固定闭流形上 \(w>0\)，普通拟线性抛物理论给出依赖于 \(g_0,\rho\) 的存在时间。

3. **Step 50 所需的统一 own-scale 时间 \(c_0>0\) 并未由 Bour 建立。**  
   Bour Theorem 1.4 只给每个固定初值的短时间存在；Theorem 1.5 假定流已经存在且全时段曲率有上界，随后给出全局 \(L^2\) 曲率导数估计。它不提供：
   - 只由初始曲率尺度决定的统一存在时间；
   - 可能塌缩情形下的局部 \(C^\infty\) 平滑估计；
   - 变权 \(w=\rho^4\) 的统一估计；
   - 从初始 \(|\mathrm{Rm}|\) 上界直接推出流期间曲率上界。

   因而 Lemma W 目前是一个新的粗糙初值四阶流定理，而不是所引文献的例行推论。

4. **由曲率尺度本身不能得到文中所需的全部统一导数控制。**  
   \(r_g\) 的 1-Lipschitz 性成立；逐个度量进行光滑化也成立。但
   \[
   |\nabla^j\log\rho|_{\rho^{-2}g}\le C_j\qquad\text{对所有 }j
   \]
   且 \(C_j\) 只依赖阶数，并不能从 \(|\mathrm{Rm}|\) 控制推出。尤其，\(|\mathrm{Rm}|\) 有界的光滑度量可以有任意大的 \(|\nabla\mathrm{Rm}|\)、\(|\nabla^2\mathrm{Rm}|\)。选择一个标量函数 \(\rho\) 也不会使 \(\rho^{-2}g\) 自动具有统一高阶有界几何。

5. **能量下降恒等式正确，但 Theorem 50.A(3) 的第一个不等式不成立。**  
   平均值选择只能给出
   \[
   \int\rho^4|\operatorname{Grad}P(g(t_*))|^2d\mu
   \le \frac2T\bigl(P(g(T/2))-P(g(T))\bigr)
   \le \frac2T\bigl(P(g_0)-\alpha(M)\bigr),
   \]
   不能一般替换成
   \[
   \frac2T\bigl(P(g_0)-P(g(t_*))\bigr).
   \]

6. **加权全局残差确实足以给出重标度后的局部 \(L^2\) 残差，但不是点态残差。**  
   这一部分在统一流存在和尺度可比性成立后是严格的。

7. **该流不保持 \(s=-4\) Yamabe 子空间。**  
   取 Yamabe 代表可以在 Yamabe 常数小于零的共形类中不增加 \(P\)，但没有理由保持 \(\operatorname{Grad}P\) 的加权 \(L^2\) 小量。要同时得到 Yamabe 代表和全梯度残差趋零，还需要一个定量 Yamabe 投影定理或直接构造投影流。

---

## 1. 梯度与权重的缩放

记
\[
\mathcal Q(g)=\operatorname{Grad}_{L^2}P(g),
\qquad
DP_g(h)=\int_M\langle\mathcal Q(g),h\rangle_g\,d\mu_g.
\]
因为 \(P(\lambda^2g)=P(g)\)，对任意 \((0,2)\)-张量 \(h\)，
\[
DP_{\lambda^2g}(h)=DP_g(\lambda^{-2}h).
\]
另一方面，在四维中
\[
\langle A,h\rangle_{\lambda^2g}d\mu_{\lambda^2g}
=\langle A,h\rangle_gd\mu_g.
\]
因此
\[
\boxed{\mathcal Q(\lambda^2g)=\lambda^{-2}\mathcal Q(g)}.
\]
随后
\[
|\mathcal Q(\lambda^2g)|_{\lambda^2g}^2
=\lambda^{-8}|\mathcal Q(g)|_g^2,
\qquad
d\mu_{\lambda^2g}=\lambda^4d\mu_g,
\]
故
\[
\boxed{|\mathcal Q(\lambda^2g)|_{\lambda^2g}^2d\mu_{\lambda^2g}
=\lambda^{-4}|\mathcal Q(g)|_g^2d\mu_g}.
\]

若 \(\rho_\lambda=\lambda\rho\)，则
\[
\rho_\lambda^4|\mathcal Q(\lambda^2g)|_{\lambda^2g}^2d\mu_{\lambda^2g}
=\rho^4|\mathcal Q(g)|_g^2d\mu_g.
\]
所以 \(\rho^4\) 是唯一自然的四次权重。

同样，若 \(g'=r^{-2}g\)，则
\[
\int_U|\mathcal Q(g')|_{g'}^2d\mu_{g'}
=r^4\int_U|\mathcal Q(g)|_g^2d\mu_g.
\]
只要在 \(U\) 上 \(\rho\ge \kappa r\)，就有
\[
\boxed{
\int_U|\mathcal Q(r^{-2}g)|_{r^{-2}g}^2d\mu_{r^{-2}g}
\le \kappa^{-4}\int_U\rho^4|\mathcal Q(g)|_g^2d\mu_g.}
\]
这是后续 blow-up 极限中局部残差消失的准确公式。

权重流本身也有正确的尺度协变性。若 \(w=\rho^4\)，则在 \(g'=r^{-2}g\)、\(\rho'=r^{-1}\rho\) 下，
\[
-w'\mathcal Q(g')
=-(r^{-4}w)(r^2\mathcal Q(g))
=r^{-2}(-w\mathcal Q(g)),
\]
恰好与 \(\partial_t(r^{-2}g)\) 相符。时间参数不需要再缩放，这正是“每个曲率尺度运行单位局部时间”的数学内容。

---

## 2. 曲率尺度及其光滑化

### 2.1 \(r_g\) 的 1-Lipschitz 性

若
\[
r_g(x)=\sup\{r:\sup_{B_g(x,r)}r^2|\mathrm{Rm}|\le1\},
\]
则对 \(d=d_g(x,y)<r_g(x)\)，由
\[
B_g(y,r-d)\subset B_g(x,r)
\]
得到
\[
(r-d)^2\sup_{B(y,r-d)}|\mathrm{Rm}|
\le r^2\sup_{B(x,r)}|\mathrm{Rm}|\le1.
\]
令 \(r\uparrow r_g(x)\)，有
\[
r_g(y)\ge r_g(x)-d.
\]
交换 \(x,y\) 即得
\[
|r_g(x)-r_g(y)|\le d_g(x,y).
\]
这一点正确。

### 2.2 光滑近似逐个存在，但统一高阶估计并不随之而来

对固定光滑紧致度量，可以将正的 Lipschitz 函数 \(r_g\) 光滑化为
\[
\tfrac12r_g\le\rho\le r_g.
\]
不过光滑化常数一般依赖该度量的高阶局部几何。Step 50 使用的是强得多的统一结论：
\[
\rho^j|\nabla^j\log\rho|_g\le C_j
\quad\text{对任意 }j,
\]
其中 \(C_j\) 与初始度量无关。

从 \(|\mathrm{Rm}|\) 控制无法推出这一点。一个直接的张量原因是：对 \(f=\log\rho\)，将
\[
(\nabla_a\nabla_b-\nabla_b\nabla_a)\nabla_cf
=R_{abc}{}^d\nabla_df
\]
再求一次导数，得到
\[
\nabla_e\!\left[
(\nabla_a\nabla_b-\nabla_b\nabla_a)\nabla_cf
\right]
=(\nabla_eR_{abc}{}^d)\nabla_df
+R_{abc}{}^d\nabla_e\nabla_df.
\]
因此，若 \(f\) 在某区域确实发生变化，则统一的四阶导数估计会接触到
\[
\nabla\mathrm{Rm}*\nabla f.
\]
而有界曲率并不控制 \(\nabla\mathrm{Rm}\)。局部高频、小振幅度量扰动可以保持 \(|\mathrm{Rm}|\) 有界，同时令 \(|\nabla\mathrm{Rm}|\to\infty\)。

更明确地说，即使取 \(\rho\equiv1\)，\(\rho\) 自己的导数全为零，也不能推出
\[
\rho^{-2}g=g
\]
的高阶导数统一有界。故 Lemma W 中“初始归一化度量具有所有阶统一控制”的推断不成立。

### 2.3 指数映射拉回不是普通坐标图

在曲率有界且半径小于共轭半径时，指数映射拉回可以给出切空间球上的局部覆盖度量。即便原流形塌缩，该拉回球仍可有良好的体积和注入半径性质。但指数映射可能多对一，因此这些不是原流形上的统一坐标图。

对于已经存在的几何流，可把方程拉回这些局部覆盖并做内部估计。反过来用这些覆盖建立统一存在时间，还需要：

- 覆盖之间的相容性；
- 变权四阶方程的局部 Schauder 或最大正则估计；
- 从低阶初值到正时间高阶平滑的定量估计；
- 流期间曲率尺度不迅速缩短。

这些内容不在 Bour 的 Theorem 1.4–1.5 中。

---

## 3. 变权 DeTurck 方程究竟给出什么

设 \(V_B(g)\) 是 Bour 为 \(-\mathcal Q(g)\) 构造的三阶 DeTurck 向量场。必须使用
\[
\boxed{\mathcal L_{\,wV_B(g)}g}
\]
而不是 \(w\mathcal L_{V_B(g)}g\)。前者是真正的 Lie 导数，因此对 \(P\) 的一阶变化为零；并且
\[
\mathcal L_{wV_B}g
=w\mathcal L_{V_B}g
+2\,\mathrm{sym}(dw\otimes V_B^\flat).
\]
第二项至多三阶，所以四阶主符号为
\[
w\,\sigma\!\left(D[-\mathcal Q+\mathcal L_{V_B}]\right).
\]
对固定光滑正函数 \(w\)，这是强抛物方程。因此：

> 对每个固定的光滑闭四维流形 \((M,g_0)\) 和每个固定的光滑正函数 \(\rho\)，方程在某个
> \[
> [0,T(g_0,\rho))
> \]
> 上有唯一光滑解。

但 Bour 的结果没有给出
\[
T(g_0,\rho)\ge c_0>0
\]
且 \(c_0\) 只由曲率尺度归一化决定。

Bour Theorem 1.5 也不能补上这一环。该定理的输入已经包括：

1. 流在给定时间段存在；
2. \(\sup|\mathrm{Rm}_{g_t}|\le D\)。

其输出主要是
\[
\int_M|\nabla^{2k}\mathrm{Rm}_{g_t}|^2d\mu_{g_t}
\le \frac{C}{t^k},
\]
而不是无需 Sobolev 常数的局部点态 \(C^\infty\) 估计。Bour 后续把 \(L^2\) 导数估计转成点态估计时，明确使用 Sobolev 控制；在塌缩情形中这正是缺少的输入。

因此，用“\(t\ge c_0/2\) 后已经平滑”来证明流能到达 \(c_0/2\) 是循环论证。统一存在时间、曲率保持和正时间平滑必须在同一个粗糙初值理论中建立。

---

## 4. 能量下降与正确的 Palais–Smale 选择

令
\[
A(t)=\int_Mw\,|\mathcal Q(g_t)|_{g_t}^2\,d\mu_{g_t}.
\]
由于 \(P\) 对微分同胚不变，
\[
DP_g(\mathcal L_Zg)=0
\]
对任意向量场 \(Z\) 成立。因此
\[
\frac{d}{dt}P(g_t)
=DP_{g_t}(-w\mathcal Q+\mathcal L_{wV_B}g_t)
=-A(t).
\]
这部分严格成立。

对任意已有的时间 \(T>0\)，在 \([T/2,T]\) 上选择 \(t_*\) 使 \(A(t_*)\) 不超过平均值，则
\[
A(t_*)
\le \frac2T\int_{T/2}^TA(t)\,dt
=\frac2T\bigl(P(g(T/2))-P(g(T))\bigr).
\]
若 \(\alpha\) 是包含整条流路径的度量类上的下确界，则
\[
\boxed{
A(t_*)\le \frac2T\bigl(P(g_0)-\alpha\bigr).}
\]

Step 50 所写
\[
A(t_*)\le\frac2T\bigl(P(g_0)-P(g(t_*))\bigr)
\]
没有由平均值论证推出，而且对一般下降函数并不成立。下降速率可以在后半段快速增长，使瞬时 \(A(t)\) 大于从 \(0\) 到 \(t\) 的平均下降速率。

对最小化序列 \(P(g_i)-\alpha=\delta_i\to0\)，真正需要的是：

- 流存在到时间 \(T_i\)；
- \(\delta_i/T_i\to0\)。

随后
\[
\int\rho_i^4|\mathcal Q(g_i(t_i))|^2d\mu_{g_i(t_i)}
\le \frac{2\delta_i}{T_i}\longrightarrow0.
\]
统一 \(T_i=T_0>0\) 是一个方便的充分输入，但不是逻辑上最弱的输入。

### 局部残差

若所选度量 \(h_i=g_i(t_i)\) 满足
\[
C^{-1}\rho_i\le r_{h_i}\le C\rho_i,
\]
并在某局部区域 \(U_i\) 上 \(\rho_i\ge\kappa r_i\)，则
\[
\int_{U_i}
|\mathcal Q(r_i^{-2}h_i)|_{r_i^{-2}h_i}^2d\mu_{r_i^{-2}h_i}
\le
\kappa^{-4}
\int_M\rho_i^4|\mathcal Q(h_i)|_{h_i}^2d\mu_{h_i}.
\]
因此右侧趋零时，每个这样的 own-scale 区域上都有 \(L^2\) 残差趋零。它本身不产生
\[
\sup|\mathcal Q|\to0.
\]
点态结论还要结合正时间高阶估计和局部抛物或椭圆估计。

---

## 5. 与 \(s=-4\) Yamabe 子空间的关系

### 5.1 流不保持常标量曲率

由 Bour 对 \(\mathcal F^\alpha\) 的迹公式，以及 \(P=2\mathcal F^1\) 加拓扑常数，可得
\[
\operatorname{tr}_g\mathcal Q(g)=\frac12\Delta_gs_g
\]
（符号取决于拉普拉斯约定，但系数结构如此）。

若初始 \(s\equiv-4\)，则初始时 \(\operatorname{tr}\mathcal Q=0\)。然而标量曲率的一阶变化为 Bour Proposition 9.5 中的
\[
Ds_g(h)=\delta\widetilde\delta h+\Delta\operatorname{tr}h-\langle\mathrm{Ric},h\rangle.
\]
取
\[
h=-w\mathcal Q+\mathcal L_{wV_B}g
\]
时，即便 \(\operatorname{tr}\mathcal Q=0\)，
\[
\delta\widetilde\delta(w\mathcal Q)-\langle\mathrm{Ric},w\mathcal Q\rangle
\]
一般也不为常数。因此流会立即离开 \(s=-4\) 子空间。

### 5.2 Yamabe 投影可以控制能量，但不能自动控制残差

Gauss–Bonnet 给出
\[
P(g)
=2\int_M|W_g|^2d\mu_g
+\frac1{12}\int_Ms_g^2d\mu_g
-16\pi^2\chi(M).
\]
在 Yamabe 常数小于零的共形类中，Yamabe 代表实现该共形类内的最小 \(\int s^2\)。因此把 \(g\) 换成其 Yamabe 代表 \(\widehat g\) 时，
\[
P(\widehat g)\le P(g).
\]
这可保持“接近下确界”的能量性质。

但 \(\mathcal Q\) 不是共形不变量。若 \(\widehat g=u^2g\)，其变换具有示意形式
\[
\mathcal Q(u^2g)
=u^{-2}\mathcal Q(g)+\mathcal T_g(u),
\]
其中 \(\mathcal T_g(u)\) 含有 \(\log u\) 的最高四阶导数以及曲率耦合项。故
\[
\int\rho^4|\mathcal Q(g)|^2\to0
\]
不能推出
\[
\int\widehat\rho^4|\mathcal Q(\widehat g)|^2\to0.
\]

要传递残差，至少需要定量证明
\[
\int_M\widehat\rho_i^4
\left|
\mathcal Q(u_i^2g_i)-u_i^{-2}\mathcal Q(g_i)
\right|_{\widehat g_i}^2
d\mu_{\widehat g_i}
\longrightarrow0,
\]
并证明 \(\widehat\rho_i\) 与 \(\rho_i\) 可比。Step 50 没有这样的估计。

若最终极限已经满足 \(\mathcal Q(g_\infty)=0\)，则闭流形上 \(s_{g_\infty}\) 为常数；若该常数小于零，可以用常数缩放改成 \(s=-4\)，此时残差仍为零。这是极限之后的归一化，不是近似序列上的 Yamabe 投影结论。

---

## 6. 可严格使用的修正版

### 6.1 固定初值版本

**命题 A\(_{\mathrm{fixed}}\).**  
设 \(M^4\) 为闭光滑流形，\(g_0\) 为光滑度量，\(\rho>0\) 为固定光滑函数，\(w=\rho^4\)。令 \(V_B(g;g_0)\) 为 Bour 的 DeTurck 向量场。则存在
\[
T=T(g_0,\rho)>0
\]
以及光滑解
\[
\partial_tg
=-w\,\mathcal Q(g)+\mathcal L_{\,wV_B(g;g_0)}g,
\qquad g(0)=g_0,
\]
定义于 \([0,T]\)。对每个 \(0<S\le T\)，存在 \(t_*\in[S/2,S]\)，使得
\[
P(g(t_*))\le P(g_0)
\]
且
\[
\int_M\rho^4|\mathcal Q(g(t_*))|^2d\mu_{g(t_*)}
\le
\frac2S\bigl(P(g(S/2))-P(g(S))\bigr).
\]
若 \(\alpha\) 是包含流路径的度量类上的下确界，则
\[
\int_M\rho^4|\mathcal Q(g(t_*))|^2d\mu_{g(t_*)}
\le \frac2S\bigl(P(g_0)-\alpha\bigr).
\]

这里所有度量可比性常数、曲率尺度可比性常数和存在时间均可依赖 \((g_0,\rho)\)。

这就是 Bour 加普通变系数拟线性抛物理论当前直接支持的版本。

### 6.2 最小化序列的最弱充分入口

**命题 A\(_{\mathrm{seq}}\).**  
设
\[
P(g_i)-\alpha=\delta_i\to0,
\]
并给定光滑正函数 \(\rho_i\)。假设固定权重方程
\[
\partial_tg_i(t)
=-\rho_i^4\mathcal Q(g_i(t))
+\mathcal L_{\rho_i^4V_{B,i}(g_i(t))}g_i(t)
\]
存在于 \([0,T_i]\)，且
\[
\boxed{\delta_i/T_i\to0.}
\]
则存在 \(t_i\in[T_i/2,T_i]\)，使
\[
P(g_i(t_i))\le P(g_i)
\]
以及
\[
\boxed{
\int_M\rho_i^4|\mathcal Q(g_i(t_i))|^2d\mu_{g_i(t_i)}
\le \frac{2\delta_i}{T_i}\to0.}
\]

若另有
\[
C^{-1}\rho_i\le r_{g_i(t_i)}\le C\rho_i,
\]
则上述加权残差在每个 \(\rho_i\) 有统一下界的 own-scale 重标度区域上转化为局部 \(L^2\) 残差趋零。

这一定理只把真正需要的入口写出：**存在时间不必统一，但能量缺口必须比可用流时间更快趋零。**

### 6.3 可用于建立统一时间的一组较强几何输入

一种标准可操作的输入是：在每个 \(x\) 处以 \(\rho_i(x)\) 重标度后，存在半径统一的局部覆盖，使得

\[
C^{-1}\delta\le \rho_i(x)^{-2}\pi_x^*g_i\le C\delta,
\]
并且这些拉回度量及其逆矩阵具有统一 \(C^{4,\beta}\) 控制，同时
\[
\frac{\pi_x^*\rho_i}{\rho_i(x)}
\]
具有统一 \(C^{4,\beta}\) 控制并保持在两个正常数之间。对应的兼容局部抛物估计若建立起来，就会给出统一 \(T_0>0\)，并在 \(t\ge T_0/2\) 给出高阶平滑。

更几何化但更强的替代输入是
\[
\rho_i^{m+2}|\nabla^m\mathrm{Rm}_{g_i}|\le C_m,
\qquad
\rho_i^m|\nabla^m\log\rho_i|\le C_m
\]
对所需阶数成立，并配合 own-scale 局部覆盖上的统一非退化。仅有
\[
\rho_i^2|\mathrm{Rm}_{g_i}|\le C
\]
尚不足以调用经典四阶 Schauder 存在理论。

---

## 最终科学判断

- **已严格成立：** 梯度缩放、\(\rho^4\) 权重、固定数据短时间强抛物性、能量下降恒等式、修正后的平均值选择、加权残差到局部重标度 \(L^2\) 残差的传递。
- **具有合理几何机制但尚未写出：** 用局部覆盖处理塌缩、从曲率尺度低阶控制建立统一变权四阶流时间、正时间 own-scale \(C^\infty\) 平滑、流期间曲率尺度可比。
- **按现有表述不成立：**
  1. 从曲率尺度直接得到全部统一高阶导数；
  2. 用 Bour Theorem 1.4–1.5 直接推出 Lemma W；
  3. Theorem 50.A(3) 中含 \(P(g_0)-P(g(t_*))\) 的第一个不等式；
  4. 将所选度量投影回 \(s=-4\) Yamabe 代表而自动保留加权全梯度残差。

因此，Theorem 50.A 当前可严格保留为 A\(_{\mathrm{fixed}}\) 与 A\(_{\mathrm{seq}}\)；要用于任意非塌缩最小化序列，核心新增分析是证明一个以 own-scale 低阶几何为输入的统一变权四阶平滑定理。
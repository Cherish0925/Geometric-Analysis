# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A01/workspace/notes/step38_continuation_repair_and_support_normalization.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md"
  ]
}
```

## Task

Verify whether the first-exit bootstrap for the normalized cutoff flow ∂_t g = -2χ²(Ric+g) actually closes when all conditional pieces are assembled. The argument is:

1. Per-datum DeTurck existence (citing Yang's Theorem 4.1 with the +g normalization as a zeroth-order perturbation) gives flow on [0,T₁).
2. Define T* = sup{T ≤ θr²: first-exit conditions (F1)-(F3) hold on [0,T]}. By smooth initial data, T* > 0.
3. On [0,T*): energy estimates from Steps 34-36 give K₂^η(t) ≤ e^{Cθ(1+1)}K₂^η(0), B(t) ≤ Cγ³, Y(t) ≤ CγK₂(0)/t, J₆(t) ≤ Ce^{Cθ}J₆(0). Weighted Moser gives ||aF(t)||_∞ ≤ Cγ/t and ||aE(t)||_∞ ≤ Cδ(r²/t)^{1/3}.
4. From (3): |U(t)| = |a(Rm+G)(t)| ≤ ||aF(t)||_∞ + C ≤ Cγ/τ + C for t ≥ τ > 0.
5. A03's all-order staggered continuation (TTCS-verified, 70/70): |U| bounded on [τ,T*) → all derivatives bounded → flow extends past T*.
6. Self-improvement: K₂^η(T*) < 2K₂^η(0) for small θ; metric drift ∫₀^{T*} ||aE||_∞ dt ≤ (3/2)δθ^{2/3}r² < Λ/2; Sobolev constant comparison.

Check specifically: (a) Is the velocity integral ∫₀^T ||aE||_∞ dt finite near t=0 given the (r²/t)^{1/3} singularity? (b) Does the Moser endpoint depend on quantities that themselves depend on (F1)-(F3), creating a circular dependency? (c) Is there a timing issue between the DeTurck existence (which may be very short) and the Moser estimates (which need positive time)? (d) Does the global Q propagation Q(T) ≤ e^{C(1+r⁻²)T}Q(0) hold through the macro-disjoint support summation? (e) Is the per-datum DeTurck existence for ∂_t g = -2χ²(Ric+g) really a trivial modification of Yang's ∂_t g = -2χ²Ric?

## Output

# 科学复核备忘录

## 总结

把步骤 1 和步骤 5 当作已经证明的定理时，首次退出的估计链是相容的，且 (a)–(d) 没有出现实质性循环或时间尺度矛盾。特别是，缺陷 Moser 估计的 \(t^{-1/3}\) 奇性可积，正时间的曲率估计足以给延拓所需的 \(|U|\) 上界。

但按所给文件的实际内容，完整流平台尚未成为定理，原因集中在两处：

1. Yang 的定理原文处理的是
   \(\partial_tg=-2\chi^2\operatorname{Ric}\)。加入
   \(-2\chi^2g\) 不改变主部，但所需的退化能量/Nash–Moser 适配并未在当前材料中写出；单纯称其为零阶扰动还不足以直接引用原定理。
2. `step40_staggered_all_order_continuation_candidate.md` 给出了可信的导数能量机制，但该文件自己在 §0、§5 明确说明：终端重启仍依赖上述正规化短时存在性；此外，零阶无权 \(T\in L^q\) 模块及结构式 (1.4)–(1.5) 仍作为输入使用。

因此，目前得到的是一个结构一致的条件式首次退出论证，而不是已经由所给 TeX 文件完全证明的流存在至 \(\theta r^2\) 的结果。

---

## (a) 速度积分在 \(t=0\) 附近确实有限

由缺陷 Moser 端点
\[
\|aE(t)\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3}
=C\delta r^{2/3}t^{-1/3},
\]
直接积分得
\[
\begin{aligned}
\int_0^T\|aE(t)\|_\infty\,dt
&\le C\delta r^{2/3}\int_0^Tt^{-1/3}\,dt\\
&=\frac32C\delta r^{2/3}T^{2/3}.
\end{aligned}
\]
当 \(T\le\theta r^2\) 时，
\[
\boxed{
\int_0^T\|aE(t)\|_\infty\,dt
\le \frac32C\delta\theta^{2/3}r^2.}
\]

所以 \(t^{-1/3}\) 奇性可积。这里自改进不等式中必须保留 Moser 常数 \(C\)；实际的小量选择是
\[
\frac32C\delta\theta^{2/3}r^2<D_0
\]
之类，其中 \(D_0\) 是预先用于度量和 Sobolev 比较的漂移阈值。

此外，
\[
|\partial_tg(v,v)|
\le2\|aE(t)\|_\infty g(v,v)
\]
给出
\[
e^{-2D(t)}g(0)\le g(t)\le e^{2D(t)}g(0),
\qquad
D(t)=\int_0^t\|aE(s)\|_\infty ds.
\]
在四维，固定支撑域上的标量 Sobolev 常数随之满足
\[
\mathcal S(t)\le e^{C_4D(t)}\mathcal S(0),
\]
因此足够小的 \(D(t)\) 确实给出 \(\mathcal S(t)<2\mathcal S(0)\)。

---

## (b) Moser 端点依赖首次退出假设，但依赖关系可以按耦合自改进闭合

设首次退出区间上暂时有
\[
K_2^\eta(t)\le2K_2^\eta(0),\qquad
\mathcal S(t)\le2\mathcal S(0),
\]
以及小的度量漂移。则
\[
\mathcal S(t)\bigl(K_2^\eta(t)\bigr)^{1/2}
\le2\sqrt2\,\gamma_0,
\qquad
\gamma_0=\mathcal S(0)\bigl(K_2^\eta(0)\bigr)^{1/2}.
\]
只要初始 \(\gamma_0\) 比吸收常数充分小，Steps 34–36 中所有使用
\(\mathcal S(K_2^\eta)^{1/2}\) 的项都能统一吸收。

具体依赖次序是
\[
(K_2^\eta,\mathcal S)
\Longrightarrow
\int_0^tY,\ B(t),\ Y(t)
\Longrightarrow
\|aF(t)\|_\infty,
\]
以及
\[
(K_2^\eta,\mathcal S)
\Longrightarrow J_6(t),
\qquad
(J_6,\|aF\|_\infty,\mathcal S)
\Longrightarrow\|aE(t)\|_\infty.
\]

关键事实如下。

### 曲率端点

由 Step 34，
\[
\int_0^tY(s)\,ds\le C\gamma_0K_2^\eta(0),
\qquad
\mathcal S(t)^2Y(t)\le\frac{C\gamma_0^3}{t}.
\]
在正时间片 \([t/2,t]\) 上，
\[
\int_{t/2}^t\mathcal S(s)^2Y(s)\,ds
\le C\gamma_0^3\log2.
\]
所以高指数迭代中的曲率势在每个这样的时间片上具有统一可积上界，而无需预先知道 \(\|aF\|_\infty\)。

将 \(p_0=3\) 代入 Step 34 的 Moser 公式，
\[
\|aF(t)\|_\infty
\le C\mathcal S^{2/3}t^{-1}
\left(\int_{t/2}^tY(s)\,ds\right)^{1/3}.
\]
利用
\[
\mathcal S^{2/3}
(\gamma_0K_2^\eta(0))^{1/3}
=
\bigl(\mathcal S^2\gamma_0K_2^\eta(0)\bigr)^{1/3}
=\gamma_0,
\]
得到
\[
\boxed{\|aF(t)\|_\infty\le C\gamma_0/t.}
\]

### 缺陷端点

Step 34 的 \(J_6\) 估计只使用
\(\mathcal S(K_2^\eta)^{1/2}\) 吸收 \(F w_6^2\)，并不使用预先给出的
\(\|aE\|_\infty\)：
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0)
\le C\delta^6V.
\]
以 \(p_0=6\) 代入 Moser 公式，
\[
\begin{aligned}
\|aE(t)\|_\infty
&\le C\mathcal S^{1/3}t^{-1/2}
       \left(\int_{t/2}^tJ_6(s)\,ds\right)^{1/6}\\
&\le C\delta\,\mathcal S^{1/3}V^{1/6}t^{-1/3}.
\end{aligned}
\]
由
\(\mathcal S\simeq r^2V^{-1/2}\)，
\[
\mathcal S^{1/3}V^{1/6}\simeq r^{2/3},
\]
故
\[
\boxed{
\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3}.}
\]

缺陷高指数迭代如果使用曲率势 \(\|aF(s)\|_\infty\)，在
\([t/2,t]\) 上也只有
\[
\int_{t/2}^t\|aF(s)\|_\infty ds
\le C\gamma_0\log2.
\]

因此，Moser 端点虽然使用首次退出区间上的 \(K_2^\eta\)、Sobolev 和度量比较，但它只使用这些量预设的粗上界，并反推出严格更小的上界。这是标准的耦合首次退出结构。Step 34 对 Hessian-\(a\) 项采用带符号分部积分，也避免了把高阶截止函数控制或延拓定理偷偷放入 Moser 层。

---

## (c) 极短的 DeTurck 存在时间不会妨碍正时间 Moser；但停止时间定义必须包含最大存在时间

令 \(\mathcal T_{\max}\) 为每个固定数据的最大光滑存在时间。精确的停止时间应写成
\[
T_*=\sup\left\{
T<\min(\mathcal T_{\max},\theta r^2):
\mathrm{(F1)-(F3)}\text{ 在 }[0,T]\text{ 成立}
\right\}.
\]
初始不等式严格成立，加上任意正的短时存在区间，给出 \(T_*>0\)。

对于每个 \(0<t<T_*\)，Moser 所使用的
\([t/4,t/2]\) 和 \([t/2,t]\) 都包含在已有光滑区间内。它不要求一个与数据无关的最小等待时间。因此，即使 Yang 构造最初给出的时间非常短，所有正时间估计仍可在该短区间内运行。

若 \(T_*<\mathcal T_{\max}\)，则自改进和连续性排除首次达到粗上界的情形。若 \(T_*=\mathcal T_{\max}<\theta r^2\)，取
\[
\tau=T_*/2>0.
\]
由曲率端点，
\[
|U(t)|
=|a(\operatorname{Rm}+G)|
\le\|aF(t)\|_\infty+C
\le C\gamma_0/\tau+C,
\qquad t\in[\tau,T_*).
\]
该常数可能依赖 \(T_*\) 和单个初始数据，但延拓只需要其有限，不需要沿序列统一。

所以这里没有 Moser 等待时间方面的矛盾。真正决定能否越过 \(T_*\) 的，是步骤 5 的全阶导数定理及步骤 1 的正规化重启定理是否已经证明。

---

## (d) 宏观不交支撑下，全局 \(Q\) 传播没有支撑个数因子

设缓冲域 \(U_\alpha\) 两两不交，且
\[
a|_{U_\alpha}=\chi_\alpha^2,
\]
每个活跃支撑紧含于 \(U_\alpha\)，其过渡环带上 \(a=0\)。令
\[
q_\alpha(t)=\int_{U_\alpha}|E|^2\,d\mu_t.
\]
Step 36 的局部计算给出
\[
q_\alpha'+cX_\alpha
\le C(1+r^{-2})q_\alpha
+C\gamma_\alpha(X_\alpha+r^{-2}q_\alpha).
\]
在
\[
\gamma_\alpha(t)
=\mathcal S_\alpha(t)
   (K_{2,\alpha}^\eta(t))^{1/2}
\]
统一充分小时，
\[
q_\alpha'(t)\le Lq_\alpha(t),
\qquad L=C(1+r^{-2}).
\]

在 \(a\equiv0\) 的开集上，\(g\) 和 \(E=\operatorname{Ric}+g\) 均保持不变。记该静止部分的能量为 \(q_0\)。由于缓冲域不交，
\[
Q(t)=q_0+\sum_\alpha q_\alpha(t),
\]
从而
\[
Q'(t)=\sum_\alpha q_\alpha'(t)
\le L\sum_\alpha q_\alpha(t)
\le LQ(t).
\]
因此
\[
\boxed{
Q(t)\le e^{C(1+r^{-2})t}Q(0)
\le e^{C\theta(1+r^2)}Q(0).}
\]

没有出现支撑数目因子。这个结论依赖“宏观不交”包含缓冲域也不交；若只有内层平台不交而缓冲域重叠，则需要把重叠重数和全局系数 \(a\) 的结构重新带入局部计算。

---

## (e) 加入 \(+g\) 不改变主部，但当前材料尚不足以把它视为原定理的直接实例

正确的传输系数 DeTurck 系统是
\[
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{\widehat aW}\widehat g,
\]
\[
\partial_t\varphi_t\circ\varphi_t^{-1}
=-\widehat aW,
\qquad
\widehat a=a\circ\varphi_t^{-1}.
\]
这里必须是
\(\mathcal L_{\widehat aW}\widehat g\)，因为
\[
\mathcal L_{\widehat aW}\widehat g
=\widehat a\mathcal L_W\widehat g
+d\widehat a\otimes W^\flat
+W^\flat\otimes d\widehat a.
\]
拉回后确实得到
\[
\partial_tg=-2a(\operatorname{Ric}_g+g).
\]

正规化项在线性化中增加
\[
\delta(-2\widehat a\widehat g)
=-2\widehat a\,h-2(\delta\widehat a)\widehat g.
\]
它不增加 \(h\) 的二阶导数，也不改变 Yang 线性化系统中
\(\widehat a\Delta h\) 的退化主部；从方程结构看，它应当只给高阶能量增加可由 Gronwall 处理的低阶项。

但 Yang 的所引定理在材料中只明确陈述了无正规化方程。要从该定理得到当前方程，还需要核实以下数学内容：

- 传输变量 \(\widehat a\) 与映射变量的线性化中，新增项仍满足 Yang 使用的 tame 能量估计；
- 系数或线性方程的 \(\varepsilon\)-正则化具有对固定数据统一的正时间和高阶估计；
- \(\varepsilon\to0\) 后得到光滑解；
- 同一论证可从终端光滑度量重新启动。

普通严格抛物型 Schauder 理论本身不能完成第三点，因为常数会依赖趋于零的椭圆性下界。`step36_analytic_platform_and_global_Q.md` §1.1–§1.2 也明确记录了这一点。

---

## 与全阶延拓文件的对应关系

`step40_staggered_all_order_continuation_candidate.md` 中的交错次序
\[
T_0\longrightarrow
(U_1,C_2)\longrightarrow T_1
\longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots
\]
解决了当前截止函数导数不能从 \(L^p\) 跳到 \(L^{2p}\) 的问题。其额外一次分部积分
\[
\int\chi C_{m+1}*U_1*P(U_m)
\]
确实把当前 \(C_{m+1}\) 从扩大指数中移除。以结构式 (1.4)–(1.5) 和零阶无权 \(T\in L^q\) 传播为输入时，这部分导数能量机制是相容的。

不过该文件还没有单独给出：

- 零阶无权 \(T\in L^q\) 能量引理的完整推导；
- (1.4)–(1.5) 所有正规化和 \(G\) 项的逐项展开；
- 终端度量上的正规化退化流重启。

尤其该文件 §5 明写重启仍依赖有效的 transported-coefficient 短时构造。因此，步骤 5 与步骤 1 实际上共享同一个尚未写完的定理接口。

最终判断是：

\[
\boxed{
\text{首次退出的能量、Moser、漂移和全局 }Q\text{ 反馈链可以条件式闭合；}
}
\]
\[
\boxed{
\text{当前文件还未证明正规化退化短时存在/重启，故整个流平台尚未完全闭合。}
}
\]
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 39,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step39_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step39_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify whether the first-exit bootstrap for the normalized cutoff flow ∂_t g = -2χ²(Ric+g) actually closes when all conditional pieces are assembled. The argument is:

1. Per-datum DeTurck existence (citing Yang's Theorem 4.1 with the +g normalization as a zeroth-order perturbation) gives flow on [0,T₁).
2. Define T* = sup{T ≤ θr²: first-exit conditions (F1)-(F3) hold on [0,T]}. By smooth initial data, T* > 0.
3. On [0,T*): energy estimates from Steps 34-36 give K₂^η(t) ≤ e^{Cθ(1+1)}K₂^η(0), B(t) ≤ Cγ³, Y(t) ≤ CγK₂(0)/t, J₆(t) ≤ Ce^{Cθ}J₆(0). Weighted Moser gives ||aF(t)||_∞ ≤ Cγ/t and ||aE(t)||_∞ ≤ Cδ(r²/t)^{1/3}.
4. From (3): |U(t)| = |a(Rm+G)(t)| ≤ ||aF(t)||_∞ + C ≤ Cγ/τ + C for t ≥ τ > 0.
5. A03's all-order staggered continuation (TTCS-verified, 70/70): |U| bounded on [τ,T*) → all derivatives bounded → flow extends past T*.
6. Self-improvement: K₂^η(T*) < 2K₂^η(0) for small θ; metric drift ∫₀^{T*} ||aE||_∞ dt ≤ (3/2)δθ^{2/3}r² < Λ/2; Sobolev constant comparison.

Check specifically: (a) Is the velocity integral ∫₀^T ||aE||_∞ dt finite near t=0 given the (r²/t)^{1/3} singularity? (b) Does the Moser endpoint depend on quantities that themselves depend on (F1)-(F3), creating a circular dependency? (c) Is there a timing issue between the DeTurck existence (which may be very short) and the Moser estimates (which need positive time)? (d) Does the global Q propagation Q(T) ≤ e^{C(1+r⁻²)T}Q(0) hold through the macro-disjoint support summation? (e) Is the per-datum DeTurck existence for ∂_t g = -2χ²(Ric+g) really a trivial modification of Yang's ∂_t g = -2χ²Ric?

## Integrated Scientific Memo

# 核验结论

**按当前材料，首次退出 bootstrap 尚未无条件闭合。**  
能量—Moser—漂移—Sobolev—全局 \(Q\) 的反馈链，在首次退出假设下基本相容；真正缺失的是流平台：

1. 正规化退化方程
   \[
   \partial_tg=-2\chi^2(\operatorname{Ric}+g)
   \]
   的 transported-coefficient DeTurck 短时存在及终端重启尚未由 Yang 原定理直接推出；
2. Step 40 验证的是交错全阶导数能量机制，不包含重启；并且仍以零阶无权 \(T=\operatorname{Rm}+G\) 的全有限指数传播及完整结构式为输入。

因此，若把这两个接口作为定理，则首次退出论证可以闭合；按现有文件，它仍是**条件式闭合**。

## (a) \(t=0\) 附近的速度积分

给定
\[
\|aE(t)\|_\infty\le C\delta\left(\frac{r^2}{t}\right)^{1/3},
\]
则
\[
\int_0^T\|aE(t)\|_\infty\,dt
\le C\delta r^{2/3}\int_0^Tt^{-1/3}\,dt
=\frac32C\delta r^{2/3}T^{2/3}.
\]
当 \(T\le\theta r^2\) 时，
\[
\boxed{\int_0^T\|aE(t)\|_\infty\,dt
\le \frac32C\delta\theta^{2/3}r^2.}
\]
故奇性可积。自改进式必须保留常数 \(C\)，而非直接写成
\((3/2)\delta\theta^{2/3}r^2\)。

由
\[
|\partial_t g(v,v)|\le2\|aE\|_\infty g(v,v)
\]
可得
\[
e^{-2D(t)}g(0)\le g(t)\le e^{2D(t)}g(0),\qquad
D(t)=\int_0^t\|aE(s)\|_\infty ds,
\]
从而小漂移给出严格的度量及 Sobolev 常数自改进。

不过，所给文件没有重现完整高指数迭代。Step 34 的公式 (6.1) 与随后宣称的 \(t^{-1/3}\) 端点之间需要依赖未附的 nested-time recurrence；因此当前材料可确认可积性，但不能仅由显示的单行公式独立重验精确 \(t^{-1/3}\) 次数。

## (b) Moser 是否循环依赖首次退出条件

没有恶性循环，但它确实是一个**耦合 bootstrap**。在首次退出区间上假设
\[
K_2^\eta(t)\le2K_2^\eta(0),\qquad
\mathcal S(t)\le2\mathcal S(0),
\]
则
\[
\mathcal S(t)\bigl(K_2^\eta(t)\bigr)^{1/2}
\le2\sqrt2\,\gamma_0,\qquad
\gamma_0=\mathcal S(0)\bigl(K_2^\eta(0)\bigr)^{1/2}.
\]
故所有吸收仅需初始 \(\gamma_0\) 足够小。

关键依赖链为
\[
(K_2^\eta,\mathcal S)
\Longrightarrow \int_0^tY,\ B(t)
\Longrightarrow Y(t)
\Longrightarrow \|aF(t)\|_\infty,
\]
以及
\[
(K_2^\eta,\mathcal S)
\Longrightarrow J_6(t)
\Longrightarrow \|aE(t)\|_\infty.
\]

其中看似自指的
\[
Y'\le C(r^{-2}+1+\mathcal S^2Y)Y
\]
由独立的 \(q=2\) 估计化解：
\[
B(t)=\int_0^t\mathcal S(s)^2Y(s)\,ds\le C\gamma_0^3.
\]
因此 Gronwall 系数已有先验时间积分控制，再通过 good-slice 得到
\[
Y(t)\le \frac{C\gamma_0K_2^\eta(0)}{t}.
\]
这不需要预先知道 \(\|aF\|_\infty\)。

同样，\(J_6\) 的吸收只用
\(\mathcal S(K_2^\eta)^{1/2}\)，不使用预设的 \(\|aE\|_\infty\)：
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
\]
所以估计层的依赖结构是三角形的；严格自改进再关闭首次退出阈值。

## (c) 极短 DeTurck 存在时间与正时间 Moser

不存在“必须先等待一个统一正时间”的问题。停止时间应精确定义为
\[
T_*=\sup\left\{
T<\min(T_{\max},\theta r^2):
\mathrm{(F1)-(F3)}\text{ 在 }[0,T]\text{ 成立}
\right\}.
\]
初始数据光滑且初始阈值严格，任何正的 per-datum 存在时间都给出 \(T_*>0\)。

对任意 \(0<t<T_*\)，Moser 使用的 \([t/4,t/2]\)、\([t/2,t]\) 都位于已有光滑区间内；无需数据无关的等待时间。若
\[
T_*=T_{\max}<\theta r^2,
\]
取 \(\tau=T_*/2\)，则
\[
|U(t)|\le \|aF(t)\|_\infty+C
\le \frac{C\gamma}{\tau}+C,\qquad t\in[\tau,T_*).
\]
该界只需对单个数据有限，不必沿序列一致。

真正的缺口是：

- Step 40 从 \(|U|\) 有界推导全阶导数界的交错机制，仍依赖零阶无权 \(T\in L^q\) 模块和所写结构方程的完整正当化；
- 即使全阶界给出终端光滑极限 \(g(T_*)\)，仍须有正规化退化短时定理从 \(g(T_*)\) 重启。

因此“全阶导数有界 \(\Rightarrow\) 延拓”在当前文件中尚未完成。Step 40 自身明确说明其验证不包括 terminal restart；所谓 70/70 不能解释为完整 continuation theorem 已获证明。

## (d) 宏观不交支撑的全局 \(Q\) 传播

若**缓冲支撑本身**两两不交，而不仅是内层 plateau 不交，则局部估计可直接求和。设
\[
q_\alpha(t)=\int_{U_\alpha}|E|^2\,d\mu_t.
\]
统一小量吸收后，
\[
q_\alpha'(t)\le Lq_\alpha(t),\qquad L=C(1+r^{-2}).
\]
在 \(a=0\) 的补集上 \(g\) 和 \(E\) 均静止。若其能量为 \(q_0\)，则
\[
Q(t)=q_0+\sum_\alpha q_\alpha(t)
\]
并且
\[
Q'(t)=\sum_\alpha q_\alpha'(t)
\le L\sum_\alpha q_\alpha(t)\le LQ(t).
\]
故
\[
\boxed{
Q(t)\le e^{C(1+r^{-2})t}Q(0)
\le e^{C\theta(1+r^2)}Q(0).}
\]
没有支撑个数因子。

此结论的必要条件应明确写入支撑构造：有限着色必须使 \(\eta\)-缓冲域宏观不交。若仅 \(\chi\)-核心不交而缓冲域有重叠，则需保留有界重叠重数并重新计算；当前简洁求和不能直接使用。

## (e) 加入 \(+g\) 是否只是 Yang 定理的平凡修改

在主符号层面，它确实只是低阶扰动；在退化存在性定理层面，尚不能称为已经证明的“平凡修改”。

正确的 hatted 系统是
\[
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{\widehat aW}\widehat g,
\]
\[
\partial_t\varphi_t\circ\varphi_t^{-1}
=-\widehat aW,\qquad
\widehat a=a\circ\varphi_t^{-1}.
\]
必须使用 \(\mathcal L_{\widehat aW}\widehat g\)，因为
\[
\mathcal L_{\widehat aW}\widehat g
=\widehat a\mathcal L_W\widehat g
+d\widehat a\otimes W^\flat+W^\flat\otimes d\widehat a.
\]
拉回后才得到固定截止方程
\[
\partial_tg=-2a(\operatorname{Ric}_g+g).
\]

新增正规化项的线性化为
\[
\delta(-2\widehat a\widehat g)
=-2\widehat a\,h-2(\delta\widehat a)\widehat g.
\]
它不增加 \(h\) 的二阶导数，故不改变退化抛物主部，原则上应可由 Gronwall/tame estimates 处理。但是 Yang 的构造不是普通一致抛物 Schauder 理论：\(\widehat a\) 可以消失，正则化极限需要对退化参数一致的能量估计。当前材料没有验证：

1. 新增两项满足 Yang 的全部 tame 能量估计；
2. 正则化解具有统一正时间和高阶界；
3. 极限是光滑解；
4. 同一定理可从终端光滑度量重启。

所以，Yang Theorem 4.1 加“零阶扰动”目前只是可信的证明方案，不是已完成引用。

# 最终判定

\[
\boxed{\text{(a) 可积；(b) 无恶性循环；(c) 无正时间等待矛盾；(d) 在缓冲域不交时成立。}}
\]

但

\[
\boxed{\text{完整首次退出流平台尚未闭合。}}
\]

精确未决对象是：

1. 正规化 transported-coefficient 退化 DeTurck 的短时存在与终端重启；
2. Step 40 所需零阶无权 \(T\in L^q\) 传播以及 weighted-\(U\)/unweighted-\(T\) 方程中全部 \(G\) 与正规化项的完整验证；
3. 从所引用但未提供的 Moser recurrence 独立确认
   \(\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}\) 的精确端点；
4. 支撑着色确实使全部 \(\eta\)-缓冲域而非仅核心区域不交。

这些接口补齐后，现有能量、Moser、漂移、Sobolev 和 \(Q\) 自改进链即可推出 \(T_*=\theta r^2\)。
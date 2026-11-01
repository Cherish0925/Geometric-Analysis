# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 20,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step20_ttcs02_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step20_ttcs02_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Test a potentially decisive simplification of the Step-20 cutoff-flow first-exit. Given the weighted curvature moments H_q and defect moments J_m in the supplied note, determine whether any pointwise connection or Hessian-a control is actually needed for the zero-order smoothing theorem and metric comparability. Specifically: all Hess(a) terms in the q=2,3 and high-exponent weak estimates are integrated by parts to leave only |da|^2/a and localization gradients; relative Sobolev and fixed-domain overlap then depend only on metric comparability, while metric comparability follows from the integrable pointwise aE estimate. If this is sound, the prior target |chi nabla(aE)| may be unnecessary for the first-exit itself. Check every place it could re-enter: local critical-energy persistence, H_2-to-H_3, curvature and defect Moser recurrences, triangular unweighted Q, preservation of cutoff-gradient bounds, moving volume/balls, and smooth continuation of the normalized cutoff flow. Read Wang Theorem 4.1/Proposition 4.9 and decide whether a terminal bound on |a Rm| (plus fixed smooth cutoff) extends to the normalized flow with -2ag, or what extra qualitative—not dimension-uniform quantitative—derivative input is actually needed. Also derive the curvature high-exponent recurrence from H_3 to |aRm| and verify its scaling C gamma/t. Give a rigorous mathematical memo; do not assume full finite-neighbor implementation or conclude Yau 26.

## Integrated Scientific Memo

# 核验备忘录：零阶 first-exit 不需要定量连接控制，但高指数曲率迭代尚未被现有材料严格闭合

## 1. 结论

在固定空间 cutoff、固定底层区域和暂定度量可比性的框架内，下列简化在结构上成立：

\[
\boxed{\text{零阶弱估计、Sobolev 传递及度量可比性均不需要 }
|\chi\nabla(aE)|\text{ 的点态控制。}}
\]

这里
\[
\partial_tg=-2aE,\qquad a=\chi^2,\qquad E=\Ric+g.
\]

原因是：

1. 曲率 \(H_q\)、缺陷 \(J_m\) 以及无权缺陷 \(Q\) 的所有 \(\nabla^2a\) 项都可在弱公式中积分分部一次；
2. 剩余 cutoff 项只有
   \[
   \frac{|da|^2}{a}=4|d\chi|^2,\qquad a|d\eta|^2,
   \]
   它们由固定 cutoff 与度量双 Lipschitz 可比性控制；
3. \(J_6\) 的零阶平滑若给出
   \[
   |aE(t)|\le C\delta\Bigl(1+\frac{r^2}{t}\Bigr)^{1/3},
   \]
   则其时间奇性 \(t^{-1/3}\) 可积，直接得到度量可比性，无须控制连接漂移。

因此先前目标
\[
|\chi\nabla(aE)|
 \le C\delta\,t^{-1/2}(r^2/t)^{1/3}
\]
不是零阶 first-exit 的必要输入。它只对定量 \(C^1\) 几何控制或旧的 cutoff-Hessian 漂移路线有用。

但须作一项重要修正：供应材料已经严格支持 \(H_2\to H_3\) 和 \(A^4H_3\lesssim\gamma^3/t\)，却**尚未严格证明**从 \(H_3\) 到
\[
|a\Rm|\le C\gamma/t
\]
的全高指数迭代。分支给出的形式 recurrence 是合理候选，但存在固定指数吸收与 \(q\)-依赖阈值之间的关键问题，不能将其视为已证定理。

---

## 2. Hessian-\(a\) 为何不再进入零阶估计

令
\[
F=(1+|\Rm|^2)^{1/2},\qquad
H_{q,k}=\int\eta_k^2a^{q-2}F^q,
\qquad
v_{q,k}=\eta_k a^{(q-1)/2}F^{q/2}.
\]

完整速度必须保持为 \(-2aE\)。曲率演化的结构为
\[
\partial_t\Rm
=a\Delta\Rm+a(\Rm*\Rm+\Rm)
+da*\nabla E+(\nabla^2a)*E+aE*\Rm .
\]
由于
\[
E=\operatorname{contr}(\Rm)+g,\qquad
\nabla E=\operatorname{contr}(\nabla\Rm),
\]
有
\[
|E|\le CF,\qquad |\nabla E|\le C|\nabla\Rm|.
\]

典型 Hessian 项
\[
\int\eta^2a^{q-2}F^{q-2}\Rm*(\nabla^2a)*E
\]
积分分部后只产生
\[
da*\nabla\Rm*E,\quad da*\Rm*\nabla E,\quad
d\eta*da*\Rm*E,
\]
以及权函数的导数。Young 不等式把这些项估计为耗散的一小部分加上
\[
C_q\int\eta^2\frac{|da|^2}{a}a^{q-2}F^q
+
C_q\int a^{q-1}|d\eta|^2F^q.
\]
因而得到
\[
\begin{aligned}
\frac d{dt}H_{q,k}+c_q\int|\nabla v_{q,k}|^2
\le Cq^2\bigg[
&\int a^{q-1}|d\eta_k|^2F^q\\
&+\int\eta_k^2\frac{|da|^2}{a}a^{q-2}F^q\\
&+\int\eta_k^2a^{q-1}F^{q+1}
\bigg].
\end{aligned}
\tag{2.1}
\]

同理，对
\[
J_{m,k}=\int\eta_k^2a^{m-2}|E|^m,\qquad
z_{m,k}=\eta_k a^{(m-1)/2}|E|^{m/2},
\]
得到
\[
\begin{aligned}
\frac d{dt}J_{m,k}+c_m\int|\nabla z_{m,k}|^2
\le Cm^2\bigg[
&\int a^{m-1}|d\eta_k|^2|E|^m\\
&+\int\eta_k^2\frac{|da|^2}{a}a^{m-2}|E|^m\\
&+\int\eta_k^2a^{m-1}F|E|^m
\bigg].
\end{aligned}
\tag{2.2}
\]

这些公式只使用当前度量下的张量恒等式及积分分部，不需要点态 \(\nabla(aE)\) 或点态 \(\nabla^2a\)。

---

## 3. 各潜在重入点的核验

### 3.1 局部临界能量保持及 \(H_2\to H_3\)

令
\[
\gamma=A^2\|F\|_{L^2(\widetilde U)}.
\]
在 \(q=2\) 时，
\[
H_3=\int Fv_2^2
\le \|F\|_2\|v_2\|_4^2
\le C\gamma\left(\int|\nabla v_2|^2+r^{-2}H_2\right).
\]
小 \(\gamma\) 吸收后，
\[
\int_0^tH_3(s)\,ds\le C\gamma H_2(0).
\tag{3.1}
\]
在固定指数 \(q=3\) 处同样可吸收反应项，从而
\[
H_3'\le Cr^{-2}H_3.
\]
向后平均给出
\[
H_3(t)\le \frac{C\gamma H_2(0)}t.
\]
再由 \(A^4H_2(0)\le\gamma^2\)，得到已核准的尺度
\[
\boxed{A^4H_3(t)\le \frac{C\gamma^3}{t}}.
\tag{3.2}
\]
整个推导没有连接项。

### 3.2 缺陷 Moser recurrence

精确代数关系为
\[
Fz_m^2=(aF^3)^{1/3}(a^{-1/3}z_m^2),
\]
且第二因子的 \(3/2\) 次方正好是 \(J_{3m/2}\) 的密度。还有
\[
J_{3m/2}\le J_m^{1/2}J_{2m}^{1/2},
\]
而 Sobolev 控制
\[
J_{2m}^{1/2}
\le CA^2\left(\int|\nabla z_m|^2+r^{-2}J_m\right).
\]
因此
\[
\int\eta^2a^{m-1}F|E|^m
\le
\varepsilon X_m+
C\varepsilon^{-2}A^4H_3J_m,
\tag{3.3}
\]
其中 \(X_m=\int|\nabla z_m|^2\)。这一步完全是零阶势能加弱梯度耗散，不需要 \(\nabla(aE)\)。

从 \(J_6\) 出发得到
\[
|aE|\lesssim
\delta\left(1+\frac{r^2}{t}\right)^{1/3}
\tag{3.4}
\]
的有限邻域实现仍须完整书写，但其权重和尺度是相容的。

### 3.3 三角形无权缺陷 \(Q\)

对
\[
Q_\alpha=\int\eta_\alpha^2|E|^2
\]
测试齐次 \(E\)-方程，积分分部 Hessian-\(a\) 后有
\[
\begin{aligned}
\frac d{dt}Q_\alpha
+c\int\eta_\alpha^2a|\nabla E|^2
\le C\int\eta_\alpha^2
\left(\frac{|da|^2}{a}+a+a|\Rm|\right)|E|^2
+C\int a|d\eta_\alpha|^2|E|^2.
\end{aligned}
\tag{3.5}
\]
曲率势通过临界 \(L^2\)-Sobolev 吸收，得到有限邻域系统
\[
Q_\alpha'\le Cr^{-2}\sum_{\beta\sim\alpha}Q_\beta.
\tag{3.6}
\]
有界重叠求和后
\[
Q_{\rm support}(T)
\le e^{CT/r^2}Q_{\rm support}(0).
\tag{3.7}
\]
这里不能退回带附加项
\(\varepsilon\int a|\nabla\Rm|^2\) 的旧估计；但也不需要点态连接控制。

### 3.4 cutoff 梯度、Sobolev 与固定覆盖

若
\[
e^{-\kappa}g_0\le g_t\le e^\kappa g_0,
\]
则固定函数 \(\chi,\eta\) 满足
\[
|d\chi|_{g_t}^2\le e^\kappa|d\chi|_{g_0}^2,\qquad
|d\eta|_{g_t}^2\le e^\kappa|d\eta|_{g_0}^2.
\]
这只涉及逆度量，不涉及连接。相同双 Lipschitz 比较直接传递固定域上的体积、梯度范数和相对 Sobolev 不等式；无需证明演化度量继续满足原 Ricci 下界。

固定覆盖的组合重叠数不随度量变化。若用度量球表述，则
\[
B_{g_0}(x,e^{-\kappa/2}r)
\subset B_{g_t}(x,r)
\subset B_{g_0}(x,e^{\kappa/2}r),
\]
故只需预留缓冲域。

### 3.5 移动体积和度量可比性

由
\[
\partial_td\mu=-\operatorname{tr}(aE)\,d\mu
\]
以及 (3.4)，体积密度可比。更根本地，
\[
\left|\partial_t\log g_t(v,v)\right|
\le 2|aE|_{g_t},
\]
而
\[
\int_0^{\theta r^2}
\left(1+\frac{r^2}{s}\right)^{1/3}ds<\infty.
\]
所以
\[
\int_0^{\theta r^2}|aE|\,ds
\le C\delta r^2\bigl(\theta+\theta^{2/3}\bigr),
\tag{3.8}
\]
并可严格改善 first-exit 中暂定的度量可比常数。这里 \(t^{-1/3}\) 可积，完全不需要 \(p>4\) 的连接漂移阈值。

---

## 4. 曲率高指数 recurrence：可核准部分与缺口

反应项满足与缺陷层平行的恒等式。写
\[
R_q=\int\eta^2a^{q-1}F^{q+1}.
\]
则
\[
R_q\le H_3^{1/3}H_{3q/2}^{2/3},
\qquad
H_{3q/2}\le H_q^{1/2}H_{2q}^{1/2},
\]
且
\[
H_{2q}^{1/2}
\le CA^2(X_q+r^{-2}H_q),\qquad
X_q=\int|\nabla v_q|^2.
\]
因此
\[
R_q
\le
\varepsilon X_q+
C\left(\varepsilon^{-2}A^4H_3+r^{-2}\right)H_q.
\tag{4.1}
\]
在 \([t/2,t]\) 上，由 (3.2)
\[
A^4H_3(s)\le \frac{C\gamma^3}{t}.
\tag{4.2}
\]
形式上这给出
\[
\frac d{ds}H_q+c_qX_q
\le Cq^\sigma
\left(r^{-2}+\frac{\gamma^3}{t}\right)H_q
\tag{4.3}
\]
以及 \(q\mapsto3q/2\) 的嵌套 recurrence。若 (4.3) 中耗散常数和 Young 参数能以足够可控的 \(q\)-依赖保持正值，则标准乘积计算确实产生
\[
\|aF(t)\|_\infty
\lesssim A^2t^{-3/2}
\left(\int_{t/2}^{t}H_2\right)^{1/2}
\lesssim \frac{\gamma}{t}.
\tag{4.4}
\]
所以所要求的尺度是
\[
\boxed{|a\Rm(t)|\lesssim \gamma/t,}
\]
且 \(t^{-1}\) 与四维抛物缩放一致。

然而，(4.4) 目前只能视为**条件性 recurrence 的结果**。关键未决点是：

- 原始临界反应的直接吸收阈值随 \(q\) 恶化；
- 必须证明用固定 \(H_3\) 势的 Young 分解后，梯度耗散足以支持所有 \(q_j\to\infty\)，且常数乘积收敛；
- 所有内层 cutoff 替换、时间 cutoff、有限邻域扩张和演化 Sobolev 常数必须统一进入该 recurrence。

供应材料明确建议更稳妥的路线是：只在 \(q=2,3\) 建立超临界 \(H_3\)，再把曲率不等式视为带 \(L^3\) 空间势的线性抛物不等式，进行正时间 De Giorgi/Moser mean-value 迭代。该论证尚未完整写出。因此不能仅凭形式指数计算宣布零阶曲率定理已经证明。

---

## 5. Wang 延拓定理对归一化流的适用性

Wang 定理 4.1 对
\[
\partial_tg=-2\chi^2\Ric
\]
断言：有限终止时间前若
\[
\|\chi^2\Rm\|_\infty<\infty,
\]
则局部 Ricci 流可光滑延拓。其证明不是假设所有导数，而是依次生成：

1. 度量等价、\(|\nabla\chi|\) 与 Sobolev 常数有界（命题 4.9）；
2. 无权 \(\Rm\) 的高 \(L^p\) 控制；
3. \(\nabla(\chi^2\Rm)\) 与 \(\nabla^2\chi\) 的耦合 \(L^p\) 控制；
4. 全部加权曲率导数的 \(L^\infty\) 控制；
5. Hamilton 型光滑延拓。

对
\[
\partial_tg=-2a(\Ric+g)
\]
而言，Wang 的文字没有直接陈述该版本，故不能仅以引用完成论证。不过其归纳机制应稳定于这一零阶归一化项：

- 速度仍为 \(aE\)，且
  \[
  |aE|\le C(|a\Rm|+1);
  \]
- 保持完整速度书写时，新项为
  \[
  da*\nabla E,\quad(\nabla^2a)*E,\quad aE*\Rm,
  \]
  并有 \(\nabla^jE=\operatorname{contr}(\nabla^j\Rm)\)（\(j\ge1\)）；
- 拆分 \(-2a\Ric-2ag\) 时出现的 \((\nabla^2a)*g\) 是可由固定平滑 \(a\) 的导数处理的低阶项，但完整写法更清楚地保持 \(E=0\) 时流静止。

因此合理的严格结论是：

\[
\boxed{\text{终端 }|a\Rm|\text{ 有界很可能足以延拓归一化 cutoff 流，}
}
\]
但需要把 Wang 的 Lemma 4.4–Proposition 4.14 对 \(E=\Ric+g\) 重新书写一次，不能称为其定理的直接推论。

若暂不完成该适配，所需额外输入仅是**定性**的终端高阶正则性，例如
\[
\sup_{[T-\varepsilon,T)}
\|\nabla^m(a\Rm)\|_\infty<\infty
\quad(m=0,1,\dots),
\]
连同 Wang 归纳中固定 cutoff 的相应导数有界性。常数可以依赖具体初始度量、cutoff、\(T\) 及其高阶导数；不需要维数一致、体积无关或 \(\delta\)-线性的
\(|\chi\nabla(aE)|\) 估计。

---

## 6. 最终判定

零阶 first-exit 的依赖关系可简化为
\[
(H_q,J_m,Q\text{ 的弱估计})
\Longrightarrow
\begin{cases}
|a\Rm|\lesssim\gamma/t,\\
|aE|\lesssim\delta(1+r^2/t)^{1/3},
\end{cases}
\Longrightarrow
\text{度量、体积、Sobolev、cutoff 梯度及固定覆盖可比}.
\]

在这条链中，点态连接或 Hessian-\(a\) 控制没有重入。真正剩余的数学对象是：

1. 从 \(H_3\) 势到 \(|a\Rm|\lesssim\gamma/t\) 的严格有限邻域正时间 mean-value/Moser 定理；
2. \(J_6\) 到点态 \(|aE|\) 的完整有限邻域迭代；
3. Wang 光滑延拓论证对 \(-2a(\Ric+g)\) 的定性适配。

这些都是零阶平滑或定性延拓问题；先前的定量 Bernstein 目标 \(|\chi\nabla(aE)|\) 不再是 first-exit 本身的必要条件。
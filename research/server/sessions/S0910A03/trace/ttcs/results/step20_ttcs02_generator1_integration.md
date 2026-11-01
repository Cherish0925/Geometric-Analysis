# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 20,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step20_ttcs02_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step20_ttcs02_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop or refute a derivative-free first-exit theorem for the normalized cutoff flow based solely on weak weighted moments. Use H_q=∫eta²a^(q-2)F^q to obtain H_3 and then |aRm|, J_m=∫eta²a^(m-2)|E|^m to obtain |aE|, and triangular local Q energies. Ask whether one can choose the provisional quantities so no evolving Hess(a) or connection norm is ever assumed: only metric equivalence, local Sobolev, local energy, cutoff-gradient bounds, fixed-domain containment, and weighted pointwise curvature/velocity. If possible, formulate the exact first-exit closure and identify what remains to prove (especially smooth continuation for dg/dt=-2a(Ric+g)); if impossible, exhibit the precise term that cannot be controlled weakly. Include finite-neighbor and buffered-good-ball dependencies and preserve the distinction between local averages and support-global averages.

## Integrated Scientific Memo

## 结论

可以提出一个**不把演化中的 \(\nabla^2a\)、连接差或任何点态导数估计列为 bootstrap 假设**的零阶 first-exit 定理。其机制是：

\[
a=\chi^2,\qquad 
\frac{|da|^2}{a}=4|d\chi|^2,
\qquad
E=\operatorname{Ric}+g,\qquad
\nabla E=\operatorname{contr}(\nabla\operatorname{Rm}).
\]

因此，曲率方程和缺陷方程中的 \((\nabla^2a)*E\) 可在张量测试中分部积分一次；所得 \(\nabla E\) 项由曲率耗散吸收，余项只含固定 cutoff 的一阶势。零阶弱层没有不可控项。

但这目前仍是一个**条件性定理框架**。尚缺：

1. \(H_q\) 的完整有限邻居、嵌套时空 Moser 递推，推出 \(|a\operatorname{Rm}|\)；
2. \(J_m\) 的相应递推，推出 \(|aE|\)；
3. 对
   \[
   \partial_tg=-2a(\operatorname{Ric}+g)
   \]
   的规范化局部流光滑延拓定理。

不能把这些缺口简化为一个未经证明的“\(L^{3+\sigma}\) 势的标准线性理论”：此流在 \(a=0\) 退化，且已有资料并未给出所需的局部张量定理。尤其从 \(H_3\) 得到正时间 \(L^{3+\sigma}\) 本身就是待证明的高次递推内容。临界小 \(L^3\) 势是否已足够、抑或必须制造 \(3+\sigma\)，现有材料不能决定；直接使用 \(H_3\) 控制高次反应则绕开了预先裁定该问题。

---

# 1. 几何数据与局部量必须怎样定义

以下限于当前资料覆盖的四维情形。取固定嵌套区域
\[
U_\alpha^-\Subset U_\alpha\Subset U_\alpha^+,
\]
以及完整外邻域星
\[
\widetilde U_\alpha
=\bigcup_{\beta\in\mathcal N(\alpha)}U_\beta^+ .
\]
假定：

- 邻接度及覆盖重数至多 \(N\)；
- 所有 buffer 宽度均与 \(r\) 可比；
- 固定 cutoff \(\eta_{\alpha,k}\) 满足嵌套支撑关系和
  \[
  |d\eta_{\alpha,k}|_{g_0}\le C2^kr^{-1};
  \]
- 初始局部 Sobolev 不等式为
  \[
  \|u\|_4^2\le A_\alpha^2
  \left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
  \qquad
  A_\alpha\le C_SrV_\alpha^{-1/4}.
  \]

关键小参数应按**完整外邻域星**定义：
\[
\Gamma(t):=
\sup_\alpha A_\alpha(t)^2
\left(\int_{\widetilde U_\alpha}F(t)^2\,d\mu_t\right)^{1/2},
\qquad
F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

若有逐中心的 buffered-good-ball 预算
\[
\fint_{B_{g_0}(x_\alpha,10r)}F_0^2\le K_0,
\]
则由体积比较及有限邻居性，
\[
\Gamma(0)\le
C(C_S,C_V,N)\,r^2\sqrt{K_0}.
\]

这里必须保持两个不同层次：

- 曲率小性需要**逐中心局部平均**；一个不连通大支撑集上的全局平均不能推出各 Whitney 球的小性。
- 三角 \(Q\)-估计使用的是**未归一化局部积分之和**；bounded overlap 能控制这些积分之和，却不能控制各球归一化平均之和。

---

# 2. 弱曲率层：由 \(H_2\) 创建 \(H_3\)

定义
\[
H_{q,\alpha,k}
=\int\eta_{\alpha,k}^2a^{q-2}F^q\,d\mu_t,
\qquad
v_{q,\alpha,k}
=\eta_{\alpha,k}a^{(q-1)/2}F^{q/2}.
\]

在仅假设度量等价、局部 Sobolev、外邻域能量小性和固定 cutoff 梯度界的区间上，张量测试应给出
\[
\begin{aligned}
\frac d{dt}H_{q,\alpha,k}
+c_q\int|\nabla v_{q,\alpha,k}|^2
\le Cq^2\bigg[
&r^{-2}\sum_{\beta\in\mathcal N(\alpha)}
 H_{q,\beta,k-1}\\
&+\int\eta_{\alpha,k}^2a^{q-1}F^{q+1}
\bigg].
\end{aligned}
\tag{2.1}
\]

其关键点不是形式上的曲率演化式，而是先保留完整速度
\[
\partial_tg=-2aE.
\]
于是 Hessian-cutoff 项为 \((\nabla^2a)*E\)，在 \(E=0\) 时消失；若把速度拆成 \(-2a\operatorname{Ric}-2ag\)，会人为产生看似独立的 Hessian 源。分部积分后，
\[
|\nabla E|\le C|\nabla\operatorname{Rm}|,\qquad |E|\le CF
\]
使所有高阶项由同一曲率耗散吸收，余项由
\[
|da|^2/a=4|d\chi|^2
\]
控制。

在 \(q=2\) 时，
\[
H_3=\int Fv_2^2
\le \|F\|_{L^2(\widetilde U_\alpha)}
   \|v_2\|_4^2
\le C\Gamma(t)\bigl(X_2+r^{-2}H_2\bigr).
\]
若 \(\Gamma\) 足够小，反应项可吸收，得到 \(H_2\) 持续性及
\[
\int_0^tH_{3,\alpha}(s)\,ds
\le C\Gamma(0)
\sum_{\beta\in\mathcal N(\alpha)}H_{2,\beta}(0).
\tag{2.2}
\]

在 \(q=3\) 时，同一固定指数吸收给出 \(H_3'\lesssim r^{-2}H_3\)。结合后向平均，
\[
\boxed{
A_\alpha^4H_{3,\alpha}(t)
\le \frac{C\Gamma(0)^3}{t}
},
\qquad 0<t\le\theta r^2.
\tag{2.3}
\]

这是真正与 transition 区兼容的三次势；不能用无权 \(\int F^3\) 代替它。

---

# 3. 从 \(H_3\) 到 \(|a\operatorname{Rm}|\)

对 \(q\ge3\)，精确分解
\[
Fv_q^2=(aF^3)^{1/3}(a^{-1/3}v_q^2)
\]
以及
\[
H_{3q/2}\le H_q^{1/2}H_{2q}^{1/2},
\qquad
H_{2q}^{1/2}\le
CA_\alpha^2\bigl(X_q+r^{-2}H_q\bigr)
\]
应给出
\[
\int\eta^2a^{q-1}F^{q+1}
\le
\varepsilon X_q+
C\left(r^{-2}+\varepsilon^{-2}A_\alpha^4H_3\right)H_q.
\tag{3.1}
\]

在 \([t/2,t]\) 上，由 (2.3)，势系数至多
\[
C_q\left(r^{-2}+\frac{\Gamma(0)^3}{t}\right).
\]
因此预期可沿
\[
q\longmapsto\frac{3q}{2}
\]
作嵌套抛物 Moser 递推，得到
\[
\boxed{
\sup_{U_\alpha^-}aF(\cdot,t)
\le
\frac{C_R\Gamma(0)}{t}
\left(1+\frac{t}{r^2}\right)^\nu
}.
\tag{3.2}
\]

终点权重确为 \(aF\)，因为
\[
H_q=\int a^{-2}(aF)^q,
\qquad
H_q^{1/q}\to\|aF\|_\infty.
\]

但 (3.2) 尚未由现有材料严格证明。必须补全：

- 时 cutoff；
- 空间 cutoff 的全部嵌套；
- 有限邻居泄漏；
- \(q\)-依赖可求和；
- \(a=0\) 附近的极限。可用 \(a_\varepsilon=a+\varepsilon\)，因为
  \[
  \frac{|da|^2}{a+\varepsilon}
  =\frac{4a}{a+\varepsilon}|d\chi|^2
  \le4|d\chi|^2.
  \]

---

# 4. 从 \(J_6\) 到 \(|aE|\)

定义
\[
J_{m,\alpha,k}
=\int\eta_{\alpha,k}^2a^{m-2}|E|^m\,d\mu_t,
\qquad
z_{m,\alpha,k}
=\eta_{\alpha,k}a^{(m-1)/2}|E|^{m/2}.
\]

不能用较弱的
\[
I_m=\int|aE|^m=\int a^m|E|^m
\]
替代 \(J_m\)：transition 区少掉的两个 \(a\)-幂正是迭代所需。

缺陷方程对 \(E\) 是齐次的：
\[
\partial_tE
=
a\Delta_LE+(\nabla a)*\nabla E
+(\nabla^2a)*E
+a\operatorname{Rm}*E+aE*E-2aE.
\]
弱测试后，
\[
\begin{aligned}
\frac d{dt}J_{m,\alpha,k}
+c_m\int|\nabla z_{m,\alpha,k}|^2
\le Cm^2\bigg[
&r^{-2}\sum_{\beta\in\mathcal N(\alpha)}
J_{m,\beta,k-1}\\
&+\int\eta_{\alpha,k}^2a^{m-1}F|E|^m
\bigg].
\end{aligned}
\tag{4.1}
\]

初始点态 pinching 直接给出
\[
J_{6,\alpha}(0)\le
\delta^6\operatorname{Vol}_{g_0}(U_\alpha^+).
\]
在固定 \(m=6\) 时，临界曲率小性吸收反应项，故
\[
J_{6,\alpha}(t)
\le C\sum_{\beta\in\mathcal N(\alpha)}J_{6,\beta}(0).
\tag{4.2}
\]

高次反应满足与曲率层相同的估计：
\[
\int\eta^2a^{m-1}F|E|^m
\le
\varepsilon\int|\nabla z_m|^2+
C\left(r^{-2}+\varepsilon^{-2}A_\alpha^4H_3\right)J_m.
\tag{4.3}
\]
预期由 \(m\mapsto3m/2\) 得到
\[
\boxed{
\sup_{U_\alpha^-}a|E|(\cdot,t)
\le
C_E\delta
\left(1+\frac{r^2}{t}\right)^{1/3}
}.
\tag{4.4}
\]

体积因子在四维相消：
\[
A_\alpha\lesssim rV_\alpha^{-1/4},
\qquad
J_6(0)^{1/6}\le\delta V_\alpha^{1/6}.
\]
因此常数可以与塌缩体积无关。

---

# 5. 三角形的无权缺陷能量

取固定 partition-type cutoffs \(\zeta_\alpha\)，定义
\[
Q_\alpha(t)=\int\zeta_\alpha^2|E|^2\,d\mu_t.
\]
弱测试、分部积分 Hessian-cutoff 项，并用完整外邻域上的临界曲率小性吸收曲率势，得到
\[
\boxed{
\frac d{dt}Q_\alpha(t)
\le Cr^{-2}
\sum_{\beta\in\mathcal N(\alpha)}Q_\beta(t).
}
\tag{5.1}
\]
于是
\[
\sum_\alpha Q_\alpha(t)
\le e^{CNt/r^2}\sum_\alpha Q_\alpha(0).
\tag{5.2}
\]

这是必须保留的三角结构。不能接受
\[
Q'\le Cr^{-2}Q+\varepsilon
\int a|\nabla\operatorname{Rm}|^2,
\]
因为后一个耗散的时间积分可为 \(O(\mathcal A)\)，从而留下 \(O(\varepsilon\mathcal A)\) 而非所需的 \(o(\mathcal A)\)。

在 \(\operatorname{supp}a\) 外度量静止；结合 bounded overlap，
\[
\int_M|E(t)|^2\,d\mu_t
\le
C e^{CNt/r^2}\int_M|E(0)|^2\,d\mu_0.
\tag{5.3}
\]

---

# 6. 精确的 derivative-free first-exit 系统

令 \(T_*\) 为不超过最大光滑存在时间及 \(\theta r^2\) 的最大时间，使下列条件成立：

1. **度量等价**
   \[
   e^{-\kappa_0}g_0\le g(t)\le e^{\kappa_0}g_0.
   \]

2. **局部 Sobolev**
   \[
   A_\alpha(t)\le2A_\alpha(0).
   \]

3. **完整外邻域星上的临界小性**
   \[
   \Gamma(t)\le2\bar\gamma.
   \]

4. **固定 cutoff 梯度**
   \[
   |d\chi|_{g(t)}\le2L_\chi r^{-1},
   \qquad
   |d\eta_{\alpha,k}|_{g(t)}
   \le2C2^kr^{-1}.
   \]

5. **固定域 containment**  
   所有用于局部估计的内域或移动球均包含于指定 buffered 外域中。

6. **加权曲率**
   \[
   t\sup_{\{a>0\}}aF(t)\le2C_R\bar\gamma.
   \]

7. **加权速度**
   \[
   \sup_{\{a>0\}}
   \frac{a|E|(t)}
   {\delta(1+r^2/t)^{1/3}}
   \le2C_E.
   \]

8. **无权缺陷总量**
   \[
   \sum_\alpha Q_\alpha(t)
   \le
   2e^{CNt/r^2}\sum_\alpha Q_\alpha(0).
   \]

不存在 \(\nabla^2a\)、连接范数或 \(\chi\nabla(aE)\) 假设。

由 (4.4)，
\[
\left|\log\frac{g(t)(v,v)}{g_0(v,v)}\right|
\le2\int_0^t|aE|\,ds
\le
C_E\delta r^2
\left[
\frac t{r^2}
+\left(\frac t{r^2}\right)^{2/3}
\right].
\tag{6.1}
\]
故选取
\[
C(6)\bar\gamma\ll1,\qquad
e^{CN\theta}<\frac32,\qquad
C_E\delta r^2(\theta+\theta^{2/3})<\frac{\kappa_0}{4},
\tag{6.2}
\]
则：

- \(H_2\) 持续性改进第 3 项；
- 完整 \(H_q\) 递推改进第 6 项；
- 完整 \(J_m\) 递推改进第 7 项；
- (6.1) 改进第 1 项；
- \(C^0\) 度量等价自动传递 Sobolev 常数、固定 cutoff 梯度和距离 containment，改进第 2、4、5 项；
- (5.2) 改进第 8 项。

因此，只要相应弱递推定理成立，\(T_*<\theta r^2\) 的唯一剩余可能是最大光滑流在 \(T_*\) 终止。

---

# 7. 光滑延拓仍需单独证明

所需命题是：

> 若闭流形上的光滑解
> \[
> \partial_tg=-2\chi^2(\operatorname{Ric}+g),
> \qquad 0\le t<T<\infty,
> \]
> 满足
> \[
> \sup_{M\times[0,T)}|\chi^2\operatorname{Rm}|<\infty,
> \]
> 则解可光滑延拓过 \(T\)。

Wang 的 Theorem 4.1 只直接证明了
\[
\partial_tg=-2\chi^2\operatorname{Ric}
\]
的对应结论。其证明的重要启示是：高阶 \(\nabla^m\chi\)、连接及加权曲率导数是在延拓证明内部，通过三角 \(L^p\) 归纳推出的，并非应加入 first-exit 的先验条件。

规范化项预期不改变最高阶结构。因为 \(\nabla g=0\)，对 \(ag\) 求导只产生
\[
\nabla^k a*g,
\]
而曲率演化中新出现的 \(a\operatorname{Rm}\) 是低阶反应项。故 Wang 的链条
\[
\nabla^m(a\operatorname{Rm})
\leftrightarrow \nabla^{m+1}\chi
\leftrightarrow \nabla^{m-1}\operatorname{Rm}
\]
应可逐项改写。但必须真正核对：

- 规范化流的各阶曲率演化；
- \(L^p\) 归纳中的最高阶项；
- Sobolev 嵌入；
- \(g(t)\to g(T)\) 的光滑收敛；
- 规范化局部 Ricci–DeTurck 重启。

这不是现有引用已经覆盖的结论。

---

# 8. 精确的不可控项及其逻辑位置

若只做上述零阶 first-exit，弱方程中没有必须点态控制的导数项。

若进一步要求
\[
|\chi\nabla(aE)|,
\]
则对 \(U=aE\) 的方程微分会产生
\[
\boxed{\chi a\,\nabla\operatorname{Rm}*U.}
\]
现有的 \(H_3\)、\(J_6\)、\(|a\operatorname{Rm}|\) 和 \(Q\) 均不能点态控制它。Whitney 缩放表明该项不是 cutoff 奇异的，但具有临界 \(1/t\) 系数，不能从 \(0\) 时刻直接 Gronwall。因此它确实阻碍 Bernstein/连接漂移估计，却**不阻碍 derivative-free 的零阶 first-exit**。

综上，最准确的状态是：零阶 derivative-free closure 在结构上可行；核心未决对象是两个完整的加权嵌套递推及规范化 Wang 延拓定理，而不是连接或 cutoff Hessian 的先验控制。
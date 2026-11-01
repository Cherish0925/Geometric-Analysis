# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 18,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step18_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step18_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently derive and assess the proposed simultaneous first-exit bootstrap for the normalized cutoff flow ∂_t g=-2aE, a=χ², E=Ric+g, in dimension four. Focus on the weighted defect estimate |aE(t)| ≤ C_p δ (r²/t)^{2/p}, p>2, under provisional metric comparability, relative Sobolev control, finite-neighbor local critical curvature energies, and appropriate connection/cutoff bounds. Derive the scalar/tensor L^p energy inequality with all a, ∇a, and Hessian-a commutators accounted for; determine whether a fixed supercritical exponent can be obtained before applying a Li-type time-dependent-potential iteration, and state exactly which terms remain uncontrolled. Check that the C/t weighted curvature estimate cannot by itself preserve E because ∫dt/t diverges. Treat coupled L² propagation only as conditional on the provisional bootstrap assumptions. Provide a mathematical memo, not procedural advice.

## Integrated Scientific Memo

# 数学核验备忘录：归一化截断流的加权 Einstein 缺陷

设
\[
\partial_tg=-2aE,\qquad a=\chi^2,\qquad E=\Ric+g,\qquad n=4,
\]
并在某个首次退出区间 \([0,T]\) 内暂时假设：

- \(g(t)\simeq g(0)\)；
- 固定尺度 \(r\) 上的相对 Sobolev 不等式及有限重叠覆盖保持；
- 邻接区域上的归一化临界能量保持小：
  \[
  \frac{r^4}{V_\alpha}\int_{\widetilde U_\alpha}|\Rm|^2\le \varepsilon_*,
  \qquad
  \frac{r^4}{V_\alpha}\int_{\widetilde U_\alpha}|E|^2\lesssim \delta^2r^4;
  \]
- \(|\nabla\chi|\lesssim r^{-1}\)，并允许把 \(\nabla^2a\) 在积分中分部积分消去。

结论是：**固定的超临界指数 \(p>2\) 的局部 \(L^p\) 传播可以在点态曲率估计之前得到；但由此推出**
\[
|aE(x,t)|\le C_p\delta\Big(\frac{r^2}{t}\Big)^{2/p}
\tag{1}
\]
**仍需一个尚未证明的、过渡区兼容的时间依赖曲率势估计。** 关键缺口是退化算子 \(\partial_t-a\Delta\) 下的加权曲率 \(\varepsilon\)-正则性，而不是缺陷张量低阶能量代数。

---

## 1. 精确缺陷方程及加权化

记 \(\tau=\tr E\)。缺陷演化为
\[
\partial_tE_{ij}=a(\Delta_LE_{ij}-2E_{ij})+\mathcal C_{ij},
\]
其中
\[
\begin{aligned}
\mathcal C_{ij}={}&(\Delta a)E_{ij}
+2a^k\nabla_kE_{ij}
+\tau a_{ij}
+\frac12(a_i\nabla_j\tau+a_j\nabla_i\tau)\\
&-a_i{}^kE_{kj}-a_j{}^kE_{ki}
-a^k(\nabla_iE_{kj}+\nabla_jE_{ki}).
\end{aligned}
\tag{2}
\]
这里使用了
\[
\nabla^iE_{ij}=\frac12\nabla_j\tau.
\]

令
\[
U=aE,\qquad \sigma=\tr U=a\tau.
\]
由于
\[
a\Delta(aE)=a^2\Delta E+a(\Delta a)E+2a\nabla a\cdot\nabla E,
\]
乘以 \(a\) 后，式 (2) 中的 \((\Delta a)E\) 和 \(2\nabla a\cdot\nabla E\) 与 Laplace 交换子精确抵消。于是
\[
\partial_tU=a(\Delta_LU-2U)+\mathcal B_a(U),
\tag{3}
\]
其中
\[
\begin{aligned}
(\mathcal B_a(U))_{ij}={}&
\sigma a_{ij}-a_i{}^kU_{kj}-a_j{}^kU_{ki}\\
&+\frac12(a_i\nabla_j\sigma+a_j\nabla_i\sigma)
-a^k(\nabla_iU_{kj}+\nabla_jU_{ki})\\
&-\sigma\,\frac{a_i a_j}{a}
+\frac{a^k}{a}(a_iU_{kj}+a_jU_{ki}).
\end{aligned}
\tag{4}
\]
表面上的除以 \(a\) 不产生 \(1/\chi\) 奇性，因为
\[
\frac{da\otimes da}{a}=4\,d\chi\otimes d\chi,\qquad
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2.
\tag{5}
\]

---

## 2. 平方范数演化与三次项抵消

因 \(\partial_tg^{ij}=2U^{ij}\)，逆度量变化对 \(\partial_t|U|^2\) 贡献
\[
4\tr(U^3).
\]
另一方面，
\[
2a\langle U,\Delta_LU\rangle
=a\Delta|U|^2-2a|\nabla U|^2
+4a\Rm(U,U)-4a\Ric(U,U).
\]
由
\[
\Ric=\frac Ua-g
\]
得
\[
-4a\Ric(U,U)=-4\tr(U^3)+4a|U|^2.
\]
这分别抵消逆度量三次项和 \(-2U\) 所给的 \(-4a|U|^2\)。因此
\[
(\partial_t-a\Delta)|U|^2
=-2a|\nabla U|^2+4a\Rm(U,U)
+2\langle U,\mathcal B_a(U)\rangle.
\tag{6}
\]
故张量方程没有内禀 \(U^3\) 反应项。不过体积元满足
\[
\partial_td\mu=-\sigma\,d\mu,
\tag{7}
\]
所以 \(L^p\) 能量中仍出现可由 \(|E|\) 控制的 \(w^{p+1}\) 项。

---

## 3. 完整的局部张量 \(L^p\) 能量不等式

令
\[
w=|U|,\qquad
I_p=\int\eta^2w^p\,d\mu,\qquad
D_p=\int\eta^2a\,|\nabla w^{p/2}|^2\,d\mu,
\]
其中 \(\eta\) 是独立的空间局部化函数。对零点可用
\((|U|^2+\varepsilon)^{1/2}\) 正则化。

测试 (3) 以 \(\eta^2w^{p-2}U\)：

### 一阶交换子

所有 \(da*U*\nabla U\) 项均满足
\[
C_p\eta^2|da|w^{p-1}|\nabla U|
\le \varepsilon \eta^2a w^{p-2}|\nabla U|^2
+C_{p,\varepsilon}\eta^2\frac{|da|^2}{a}w^p.
\tag{8}
\]
这里必须使用**张量耗散**
\[
\int\eta^2a\,w^{p-2}|\nabla U|^2,
\]
而不能仅从一个先行的标量 Kato 不等式依赖
\(|\nabla w|\)。标量化会丢失 \(\nabla U\) 的旋转部分；因此完整证明应在张量层面完成，然后再用 Kato 得到 \(D_p\)。

### Hessian-\(a\) 项

\[
\sigma\,\nabla^2a,\qquad \nabla^2a*U
\]
经一次分部积分后变成
\[
da*U*\nabla U,\qquad da*d\eta*w^2,
\]
故由 (8) 及 Young 不等式控制为
\[
\varepsilon \eta^2a w^{p-2}|\nabla U|^2
+C_{p,\varepsilon}
\left(\eta^2\frac{|da|^2}{a}+a|d\eta|^2\right)w^p.
\tag{9}
\]
所以**缺陷的积分 \(L^p\) 不等式不需要点态 \(|\nabla^2a|\) 界**。

综合主部、体积变化及 \(|\sigma|\le 2w\)，得到
\[
\boxed{
\begin{aligned}
\frac d{dt}I_p+c_pD_p
\le{}&
C_p\int\left(a|d\eta|^2+
\eta^2\frac{|da|^2}{a}\right)w^p\\
&+C_p\int\eta^2a|\Rm|\,w^p
+C_p\int\eta^2w^{p+1}.
\end{aligned}}
\tag{10}
\]
这是所需的、包含全部 \(a,\nabla a,\nabla^2a\) 交换子的局部能量不等式。

---

## 4. 固定 \(p>2\) 确实可先于点态曲率估计获得

在扩大的邻域上假设相对 Sobolev 不等式
\[
\|\varphi\|_{L^4}
\le A_\alpha\big(\|\nabla\varphi\|_2+r^{-1}\|\varphi\|_2\big),
\qquad
A_\alpha\lesssim rV_\alpha^{-1/4}.
\tag{11}
\]
取 \(z=w^{p/2}\)。则
\[
\int\eta^2a|\Rm|w^p
=\int |\Rm|(\chi\eta z)^2,
\]
且因 \(w=a|E|\)，
\[
\int\eta^2w^{p+1}
=\int |E|(\chi\eta z)^2.
\]
于是
\[
\begin{aligned}
&\int\eta^2a|\Rm|w^p+\int\eta^2w^{p+1}\\
&\quad\le
C A_\alpha^2\big(\|\Rm\|_{L^2(\widetilde U_\alpha)}
+\|E\|_{L^2(\widetilde U_\alpha)}\big)
\left(D_p+r^{-2}\sum_{\beta\sim\alpha}I_{p,\beta}\right).
\end{aligned}
\tag{12}
\]
四维中塌缩体积消去：
\[
A_\alpha^2\|\Rm\|_2
\lesssim
\left(
\frac{r^4}{V_\alpha}
\int_{\widetilde U_\alpha}|\Rm|^2
\right)^{1/2},
\tag{13}
\]
对 \(E\) 同理。若临界能量足够小（小量阈值可依赖于所固定的 \(p\)），则 (12) 的耗散部分可吸收，得到
\[
\frac d{dt}I_{p,\alpha}+c_pD_{p,\alpha}
\le Cr^{-2}\sum_{\beta\sim\alpha}I_{p,\beta}.
\tag{14}
\]
有限邻接与 Gronwall 给出
\[
\sup_{0\le s\le \theta r^2}
\fint_{U_\alpha}|aE(s)|^p\le C_p\delta^p.
\tag{15}
\]

因此答案是：

- **可以在 Li 型时间依赖势迭代之前得到一个固定 \(p>2\)**；
- 这必须通过张量 \(L^p\) 能量完成，而非不保留全张量耗散的粗糙标量化；
- 可固定例如 \(p=3\)，无需把此临界能量吸收直接迭代到 \(p=\infty\)。

后一种直接高次幂迭代不可行：反应项的吸收系数随幂次 \(m\) 增长，条件形如
\[
m\,A_\alpha^2\|\Rm\|_2\ll1,
\]
固定 \(\varepsilon_*\) 无法支持 \(m\to\infty\)。

---

## 5. 从固定 \(L^p\) 到点态估计仍需要的曲率势

高次幂阶段必须把曲率当作时间依赖势，而不是继续以临界 \(L^2\) 小量吸收。一个充分输入是
\[
K_{3,\alpha}(t):=
\int_{\widetilde U_\alpha}a|\Rm|^3
\le \frac{C}{A_\alpha^4t}.
\tag{16}
\]
事实上，对 \(z=\eta w^{m/2}\)，
\[
\begin{aligned}
\int a|\Rm|z^2
&\le K_{3,\alpha}^{1/3}
\left(\int a|z|^3\right)^{2/3}\\
&\le \varepsilon\|\nabla(\chi z)\|_2^2
+C_\varepsilon A_\alpha^4K_{3,\alpha}\|z\|_2^2
+Cr^{-2}\|z\|_2^2.
\end{aligned}
\tag{17}
\]
更强的充分条件是
\[
a|\Rm|\le \frac Ct
\tag{18}
\]
连同局部 \(L^2\) 曲率能量保持，因为
\[
A_\alpha^4K_{3,\alpha}(t)
\le \frac Ct\,A_\alpha^4
\int_{\widetilde U_\alpha}|\Rm|^2
\lesssim \frac{\varepsilon_*}{t}.
\tag{19}
\]
在时间圆柱 \([t/2,t]\) 上，这是标准 Li 型迭代可接受的势。由 (15) 出发，条件性地得到
\[
|aE(x,t)|
\le C_p A_\alpha^{4/p}
(t^{-1}+r^{-2})^{2/p}
\|E(0)\|_{L^p(\widetilde U_\alpha)}.
\tag{20}
\]
再用
\[
A_\alpha\lesssim rV_\alpha^{-1/4},
\qquad
\|E(0)\|_p\le \delta V_\alpha^{1/p},
\]
体积再次消去，得到目标式 (1)。

Li 的结果覆盖非退化全支撑 Ricci 流；Wang/Yang 的局部流结果具有相同的四维时间指数 \(t^{-2/p}\)，但其输入是全局 Sobolev、不变的全支撑临界曲率小量及 \(L^p\)-Ricci 界。它们不能直接提供这里的有限邻接、相对 Sobolev、塌缩兼容过渡区版本。

---

## 6. \(C/t\) 加权曲率不能直接保持 \(E\)

缺陷最大值原理至多给出
\[
D^+\|E(t)\|_\infty^2
\le C\left(
\|a\Rm(t)\|_\infty+
\|\nabla^2a\|_\infty+
\frac{|\nabla a|^2}{a}
\right)\|E(t)\|_\infty^2.
\tag{21}
\]
若仅有 \(\|a\Rm(t)\|_\infty\le C/t\)，则
\[
\int_0^T\frac{dt}{t}=\infty.
\]
从 \(t_0>0\) 积分只能得到
\[
\|E(t)\|_\infty^2
\lesssim \|E(t_0)\|_\infty^2
\left(\frac{t}{t_0}\right)^C,
\tag{22}
\]
无法一致地令 \(t_0\downarrow0\)。因此“\(C/t\) 曲率使缺陷自动保持 \(O(\delta)\)”是错误的；所谓“仅对数增长”仍然在初时刻发散。

相反，(1) 给出
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le
\frac{C_pp}{p-2}\,
\delta\,\theta^{1-2/p}r^2,
\tag{23}
\]
其有限性恰好等价于 \(p>2\)。由于 \(\partial_tg=-2aE\)，这才是获得塌缩一致度量可比性的正确机制。端点 \(p=2\) 再次产生对数发散。

---

## 7. 精确未控制项

目前未闭合的对象是：

1. **过渡区退化曲率正则化**
   \[
   R_\alpha\le\varepsilon_*
   \Longrightarrow
   |a\Rm|\le C/t
   \quad\text{或至少}\quad
   A_\alpha^4\int a|\Rm|^3\le C/t.
   \]
   这是 \(\partial_t-a\Delta\) 在 \(0<a<1\) 上的真正缺口。

2. **曲率方程中的连接与截断导数耦合**
   \[
   \nabla^2a*E,\qquad \nabla a*\nabla E.
   \]
   缺陷能量中可将 \(\nabla^2a\) 分部积分消掉，但曲率正则化和光滑延拓仍需控制
   \[
   \partial_t(\nabla^2a)\sim \nabla(aE)*\nabla a.
   \]
   点态 \(aE\) 界不控制 \(\nabla(aE)\)。Wang 的导数估计也明确表现出
   \(\nabla^2\chi\) 与 \(\nabla(\chi^2\Rm)\) 的耦合。

3. **有限邻接 Li 迭代的完整版本**  
   式 (17)–(20) 是正确的条件性机制，但仍需在演化测度、邻接区域和退化耗散下写出闭合递推。

4. **联合首次退出输入本身**  
   度量可比性、相对 Sobolev、邻接体积比较、覆盖重叠及临界能量保持目前均是暂定假设；它们不能被已引用文献直接同时推出。

5. **无权全局缺陷**
   \[
   Q(t)=\int_M|E|^2.
   \]
   加权点态界只控制 \(aE\)，在 \(a\to0\) 处不给出无权 \(E\) 控制。故 \(Q(t)\) 的传播仍只能条件性地由耦合 \(L^2\) 系统获得，不能从 (1) 推出。

综上，缺陷侧的张量能量代数是闭合的：固定 \(p>2\) 的局部传播在暂定几何与临界能量假设下成立；目标点态估计则条件于过渡区加权曲率势。真正未解决的是退化曲率 \(\varepsilon\)-正则性及其与连接、截断 Hessian、Sobolev 几何的同步延拓。
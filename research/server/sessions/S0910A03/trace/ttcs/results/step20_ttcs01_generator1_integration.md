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
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step20_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step20_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop the strongest viable local weighted parabolic iteration suggested by Wang for a=χ² under the normalized cutoff flow ∂tg=-2a(Ric+g), in dimension four. Focus on a self-contained theorem at the level actually supported by H_q=∫η²a^{q-2}F^q and J_m=∫η²a^{m-2}|E|^m. Seek an exact recurrence whose output norms feed the next stage, with nested localization cutoffs and finite-neighbor terms. Explore whether the curvature hierarchy can produce weighted cubic potential and whether the defect hierarchy can produce |aE| and χ∇(aE) estimates from initial |E|≤δ, while preserving homogeneity at E=0. Explicitly analyze where normalization, derivatives of a, evolving metric/measure, and curvature derivative terms enter. Compare the direct weighted hierarchy against Whitney-ball localization and identify a decisive calculation or counterexample that would choose between them. The result should be a technical construction memo, not a generic roadmap or a conclusion about the full Yau problem.

## Integrated Scientific Memo

# 技术构造备忘录：四维归一化截断流的加权 Wang 迭代

考虑
\[
\partial_tg=-2aE,\qquad E=\Ric+g,\qquad a=\chi^2,\quad 0\le a\le1.
\]
以下结论是在第一退出区间内成立的局部命题：演化度量可比、相对 Sobolev 常数、有限邻域覆盖以及独立局部化截断均暂时受控。它不是无条件的流存在性定理。

## 1. 正确的局部量与精确代数闭合

令 \(F=(1+|\Rm|^2)^{1/2}\)（或先用 \(F_\varepsilon\) 正则化再极限），\(G=|E|\)。在局部块 \(U_\alpha\) 及其放大块 \(\widetilde U_\alpha\) 上取嵌套截断 \(\eta_{\alpha,k}\)，满足
\[
|\nabla\eta_{\alpha,k}|\le C2^kr^{-1},
\]
并假设四维相对 Sobolev 不等式
\[
\|\phi\|_4^2\le A_\alpha^2
\left(\|\nabla\phi\|_2^2+r^{-2}\|\phi\|_2^2\right).
\]
定义
\[
H_{q,\alpha,k}=\int\eta_{\alpha,k}^2a^{q-2}F^q\,d\mu_t,
\qquad
J_{m,\alpha,k}=\int\eta_{\alpha,k}^2a^{m-2}G^m\,d\mu_t.
\]
其 Sobolev 变量是
\[
v_q=\eta a^{(q-1)/2}F^{q/2},\qquad
w_m=\eta a^{(m-1)/2}G^{m/2}.
\]
关键恒等式为
\[
v_q^4=\eta^4a^{2q-2}F^{2q},\qquad
Fv_q^2=\eta^2a^{q-1}F^{q+1},
\]
以及
\[
w_m^4=\eta^4a^{2m-2}G^{2m}.
\]
因此 Sobolev 端对应 \(H_{2q}\)、\(J_{2m}\)，而势项对应 \(H_{q+1}\)。

最重要的三次势恒等式是
\[
Fw_m^2=(aF^3)^{1/3}\bigl(a^{-1/3}w_m^2\bigr),
\]
且
\[
\bigl(a^{-1/3}w_m^2\bigr)^{3/2}
=\eta^3a^{3m/2-2}G^{3m/2}.
\]
故
\[
\int Fw_m^2
\le H_3^{1/3}J_{3m/2}^{2/3},
\qquad
J_{3m/2}\le J_m^{1/2}J_{2m}^{1/2}.
\]
同理，
\[
\int Gw_m^2\le J_3^{1/3}J_{3m/2}^{2/3}.
\]
这给出自然的高指数步长
\[
s\longmapsto \frac32s,
\]
而不是必须采用纯倍增。

当 \(q,m\to\infty\) 时，
\[
(a^{q-2}F^q)^{1/q}\to aF,\qquad
(a^{m-2}G^m)^{1/m}\to aG=|aE|.
\]
因此这些权正好以 \(|a\Rm|\) 和 \(|aE|\) 为端点。

---

## 2. 归一化项和 \(E=0\) 齐次性

曲率演化必须从完整速度
\[
h=-2aE
\]
出发。一般变分公式给出
\[
\partial_t\Rm=\nabla^2(aE)+\Rm*(aE)
\]
的张量结构。若人为拆成 \(-2a\Ric-2ag\)，会分别出现
\[
(\nabla^2a)\owedge\Ric,\qquad (\nabla^2a)\owedge g;
\]
代入 \(\Ric=E-g\) 后，两个纯 \(g\) 项相消，只剩
\[
(\nabla^2a)\owedge E.
\]
所以归一化不会产生在 \(E=0\) 时仍存在的曲率源。所有截断源应保持为 \(E\) 或 \(\nabla E\) 的线性项。

更精确地，曲率方程可按
\[
\partial_t\Rm
=a(\Delta\Rm+\Rm*\Rm+\Rm)
+\nabla a*\nabla E+\nabla^2a*E
+\Rm*(aE)+\nabla a*\Rm*E
\]
组织；第一行是抛物主部，第二行整体在 \(E=0\) 时消失。

缺陷的最佳变量是
\[
U=aE.
\]
其精确方程为
\[
\partial_tU=a(\Delta_LU-2U)+\mathcal B_a(U),
\]
其中 \(\mathcal B_a\) 对 \(U,\nabla U\) 线性，系数由
\[
\nabla a,\quad \nabla^2a,\quad
\frac{da\otimes da}{a}=4\,d\chi\otimes d\chi
\]
组成。故 \(U=0\) 是严格不变解。

体积形式的正确演化是
\[
\partial_td\mu=-\tr(aE)\,d\mu=-\tr U\,d\mu.
\]
因此高阶矩获得由 \(G\) 控制的势项；符号不能写反。逆度量变分和缺陷张量反应中的三次项相消，缺陷能量仍保持对 \(E\) 的齐次性。

---

## 3. 零阶加权能量不等式

结构性截断恒等式为
\[
\frac{|da|^2}{a}=4|\nabla\chi|^2\le Cr^{-2}.
\]
任何零阶推导若留下 \(|\nabla^2a|/a\)，都尚未闭合。必须对 Hessian 项分部积分，直至只出现
\[
\frac{|da|^2}{a},\qquad a|\nabla\eta|^2,\qquad da*d\eta.
\]

在有限邻域系统中，张量测试给出以下可靠的模型不等式：
\[
\begin{aligned}
\frac d{dt}H_{q,\alpha,k}+c_qD^R_{q,\alpha,k}
\le{}&
Cq^2\Theta_k\sum_{\beta\sim\alpha}H_{q,\beta,k-1}\\
&+Cq\int Fv_q^2+Cq\int Gv_q^2
+\mathcal L^R_{q,\alpha,k},
\end{aligned}
\tag{3.1}
\]
以及
\[
\begin{aligned}
\frac d{dt}J_{m,\alpha,k}+c_mD^E_{m,\alpha,k}
\le{}&
Cm^2\Theta_k\sum_{\beta\sim\alpha}J_{m,\beta,k-1}\\
&+Cm\int Fw_m^2+Cm\int Gw_m^2,
\end{aligned}
\tag{3.2}
\]
其中
\[
\Theta_k=4^kr^{-2}+1,
\]
\[
D^R_q\simeq\int|\nabla v_q|^2,\qquad
D^E_m\simeq\int|\nabla w_m|^2,
\]
而 \(\mathcal L^R_q\) 是由 \((\nabla^2a)E+\nabla a\nabla E\) 产生、需与缺陷耗散耦合处理的低阶项。仅写曲率能量而忽略该耦合并不充分。

利用四维 Sobolev 和上面的三次恒等式，
\[
\int Fw_m^2
\le \varepsilon D^E_m+
C_\varepsilon A_\alpha^4
\Bigl(\sum_{\beta\sim\alpha}H_{3,\beta,k-1}\Bigr)
\Bigl(\sum_{\beta\sim\alpha}J_{m,\beta,k-1}\Bigr),
\tag{3.3}
\]
\[
\int Gw_m^2
\le \varepsilon D^E_m+
C_\varepsilon A_\alpha^4
\Bigl(\sum_{\beta\sim\alpha}J_{3,\beta,k-1}\Bigr)
\Bigl(\sum_{\beta\sim\alpha}J_{m,\beta,k-1}\Bigr).
\tag{3.4}
\]
曲率侧有同型估计。因此两套层级归约到
\[
\boxed{
\frac d{dt}M_{s,\alpha,k}+cD_{s,\alpha,k}
\le Cs^3\bigl(\Theta_k+\mathcal P_{\alpha,k}(t)\bigr)
\sum_{\beta\sim\alpha}M_{s,\beta,k-1},
}
\tag{3.5}
\]
其中
\[
\mathcal P_{\alpha,k}
=A_\alpha^4\sum_{\beta\sim\alpha}(H_{3,\beta,k-1}+J_{3,\beta,k-1}).
\]

这里不能声称临界小量可对所有 \(s\to\infty\) 反复吸收：原始能量常数通常随 \(s\) 墻长。正确策略是只在固定低指数建立 \(H_3,J_3,J_p\)，再把它们当作时间依赖势进入高指数迭代。

---

## 4. 曲率层级真正需要的三次势

令
\[
\beta_\alpha
=A_\alpha^2
\left(\sum_{\beta\sim\alpha}\int_{\widetilde U_\beta}F^2\right)^{1/2}.
\]
四维相对 Sobolev标度
\[
A_\alpha\lesssim rV_\alpha^{-1/4}
\]
与临界 \(L^2\) 曲率精确抵消塌缩体积，因此 \(\beta_\alpha\) 可与局部相对能量的小量等价，常数只依赖倍增和邻域数。

在 \(q=2\) 时，
\[
H_3=\int aF^3=\int F(\chi F)^2,
\]
故
\[
H_3\le \|F\|_2\|\chi F\|_4^2
\le \beta_\alpha\left(D^R_2+r^{-2}\sum_{\beta\sim\alpha}H_{2,\beta}\right).
\tag{4.1}
\]
这首先给出
\[
\int_0^T H_3(t)\,dt
\le C\beta_\alpha\sum_{\beta\sim\alpha}H_{2,\beta}(0).
\tag{4.2}
\]

进一步用时间截断运行固定 \(q=3\) 能量，预期且与 Wang 的 \(n/2+1=3\) 矩完全同标度的局部结论是
\[
\boxed{
A_\alpha^4H_{3,\alpha}(t)
\le C_N\left(\frac{\beta_\alpha^3}{t}
+r^{-2}\beta_\alpha^2\right).
}
\tag{4.3}
\]
但必须明确：由现有材料完全严谨得到 (4.3)，仍需写出耦合曲率–缺陷 \(q=2,3\) 张量推导及有限邻域时间截断。不能通过先假设 \(|a\Rm|\le C/t\) 再推导 \(H_3\)，否则会循环。

缺陷自势在固定 \(m=3\) 下满足
\[
J_3(0)\le \delta^3\int a\,d\mu_0.
\]
在 (4.3) 和固定指数能量闭合后，
\[
A_\alpha^4J_{3,\alpha}(t)\le C_{N}\delta^3
\tag{4.4}
\]
是相应的低阶输入。

---

## 5. 可用的有限邻域递推

取
\[
I_k=[\tau_k,T],\qquad
\tau_k=T(1-2^{-k-1}),
\]
并令
\[
X_{s,\alpha,k}=\sup_{t\in I_k}M_{s,\alpha,k}(t).
\]
时间截断贡献 \(C2^kT^{-1}\)，空间截断贡献 \(C4^kr^{-2}\)。置
\[
\Lambda_k=C4^k(T^{-1}+r^{-2})
+C\sup_{I_k}\mathcal P_{\alpha,k}.
\]
由 (3.5)、Sobolev 及
\[
M_{3s/2}\le M_s^{1/2}M_{2s}^{1/2}
\]
得到适合下一阶段的递推
\[
\boxed{
X_{\frac32s,\alpha,k+2}^{\,2/(3s)}
\le
\left(
C_NA_\alpha^2s^6\Lambda_k^2|I_k|
\right)^{2/(3s)}
\left(
\sum_{\beta\in\mathcal N_2(\alpha)}
X_{s,\beta,k}
\right)^{1/s}.
}
\tag{5.1}
\]
这是自然的“输出范数喂给下一层”形式。由于
\[
s_j=s_0(3/2)^j,\qquad
\sum_j\frac1{s_{j+1}}=\frac2{s_0},
\]
且邻域扩大由固定放大块吸收，迭代积收敛，有限邻域损失为 \(N^{C/s_0}\)。

在假设 (4.3)–(4.4) 已建立时，(5.1) 给出：

- 以 \(s_0=3\) 起步，
  \[
  \boxed{
  \|a\Rm(T)\|_{\infty,U_{\alpha,\infty}}
  \le C_N\beta_\alpha(T^{-1}+r^{-2}).
  }
  \tag{5.2}
  \]

- 以固定 \(p>2\) 起步，先传播 \(J_p\)，再迭代，
  \[
  \boxed{
  \|aE(T)\|_{\infty,U_{\alpha,\infty}}
  \le C_{p,N}A_\alpha^{4/p}
  (T^{-1}+r^{-2})^{2/p}
  \Bigl(\sum_{\beta}J_{p,\beta}(T/2)\Bigr)^{1/p}.
  }
  \tag{5.3}
  \]
  若 \(|E(0)|\le\delta\)，体积因子消去，得到
  \[
  \boxed{
  \|aE(T)\|_\infty
  \le C_{p,N}\delta
  \left(1+\frac{r^2}{T}\right)^{2/p}.
  }
  \tag{5.4}
  \]

(5.4) 对 \(\delta\) 严格一次齐次；若 \(E(0)=0\)，则 \(E(t)=0\)，不会产生伪缺陷。度量漂移
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty dt
\le C_{p,N}\delta r^2\theta^{1-2/p}
\]
当且仅当 \(p>2\) 可积。

归一化中的 \(-2aE\) 是有利的零阶阻尼，但 \(t^{-2/p}\) 主要来自四维抛物 \(L^p\to L^\infty\) 标度，不能归因于阻尼本身。

---

## 6. 缺陷层级能给出的梯度结论

零阶 \(J_m\) 层级直接给出的不是点态 Bernstein 界，而是 Caccioppoli 界。由
\[
U=aE,\qquad
w_m=\eta a^{-1/2}|U|^{m/2}
\]
可得
\[
\boxed{
\int_{I_{k+1}}\!\!\int
\eta^2|\chi\nabla U|^2|U|^{m-2}
\le
C\int_{I_{k+1}}D^E_m
+Cr^{-2}\int_{I_{k+1}}J_m .
}
\tag{6.1}
\]
这是 \(H_q,J_m\) 零阶体系实际支持的最强梯度信息。

若微分 \(U\)-方程，则 \(W=\chi\nabla U\) 的方程含有
\[
a\Rm*W,\qquad
\frac{da}{\sqrt a}*\nabla W,\qquad
\left(\nabla^2a+\frac{da\otimes da}{a}\right)*W,
\]
以及关键项
\[
\boxed{\chi a\,\nabla\Rm*U}
\tag{6.2}
\]
和更高截断导数项。仅凭 \(H_3\) 或 \(|a\Rm|\le C/t\) 不能控制 (6.2)。因此
\[
|\chi\nabla(aE)|
\lesssim \delta t^{-1/2}(r^2/t)^{2/p}
\tag{6.3}
\]
不是零阶矩层级的结论；它需要加权曲率导数估计或局部非退化的张量 Bernstein 定理。

一旦 (6.3) 成立，
\[
\int_0^{\theta r^2}|\chi\nabla(aE)|\,dt
\lesssim \delta r\,\theta^{1/2-2/p}
\]
当且仅当 \(p>4\) 可积。因此同时控制度量、与 \(da\) 收缩的连接漂移及 \(\nabla^2a\) 漂移，应取固定 \(p>4\)，例如 \(p=6\)。

---

## 7. 直接权层级与 Whitney 局部化

两者在零阶上表达同一四维标度。在 \(\chi\simeq\lambda\) 的过渡层，
\[
a\simeq\lambda^2,\qquad \ell\simeq r\lambda.
\]
直接权矩满足
\[
H_q\simeq \lambda^{-4}\int(aF)^q.
\]
而 Whitney 球的 Bishop–Gromov 能量转移产生
\[
\ell^4\fint_{B_\ell}F^2
\lesssim K_0r^4,
\]
其中 \((r/\ell)^4=\lambda^{-4}\) 正是同一因子。因此零阶权层级不是与 Whitney 竞争的不同标度，而是其全局编码。

决定性 Hessian 计算也一致。模型 \(a=s^2/r^2\) 中
\[
\frac{|da|^2}{a}=\frac4{r^2},
\qquad
\frac{|\nabla^2a|}{a}\simeq \frac1{s^2}.
\]
直接法必须分部积分消去后一个奇性；Whitney 球上
\[
\frac{|\nabla^2a|}{a_0}\simeq \ell^{-2},
\]
它恰为局部抛物尺度。

然而 Whitney 不能被视为已经自动给出导数估计。对
\[
\ell=cr\chi_0,\qquad a_0=\chi_0^2,
\]
有效时间是 \(a_0t\)，扩散长度为 \(\chi_0\sqrt t\)，与 \(\ell\) 的比值独立于 \(\chi_0\)。这确实消除椭圆退化；但要应用 Shi/Bernstein，仍须把完整归一化流的 \(\nabla a,\nabla^2a\)、缺陷耦合和有限邻域边界项纳入局部定理。不能说“逐字应用 Shi”。

### 真正有判别力的计算

在单个 Whitney 球上，以 \(a_0t\) 为时间，直接推导 \(W=\chi\nabla U\) 的局部能量，并单独估计
\[
\chi a\nabla\Rm*U.
\]
若局部曲率导数估计能以
\[
|\nabla\Rm|\lesssim (a_0t)^{-3/2}
\]
配合 \(U\) 在边界附近的额外 \(a_0^{1-2/p}\) 衰减，使所有 \(a_0\) 幂非负且常数与 \(\chi_0\) 无关，则 Whitney 路线闭合；若留下 \(a_0^{-\gamma}\), \(\gamma>0\)，则该路线失败或需要更强权重。

相反，若直接法尝试依赖一般退化散度理论，模型权 \(a\simeq d^2\) 不属于 codimension-one 的 \(A_2\) 类，因为
\[
\int_{-\varepsilon}^{\varepsilon}d^{-2}\,dd=\infty.
\]
这排除了标准 \(A_2\) 退化 Harnack/Bernstein 作为直接闭合工具，但不排除利用特殊代数结构的直接张量能量法。故目前最可靠的分工是：

- 直接 \(H_q,J_m\) 层级：临界能量、加权三次势、\(|a\Rm|\)、\(|aE|\)；
- Whitney 球：研究曲率导数与 \(\chi\nabla(aE)\) 的非退化局部估计。

---

## 8. 当前可严格陈述的条件性定理

**条件性加权 Wang 矩定理（四维）。**  
在上述第一退出几何、有限邻域 Sobolev 系统和嵌套截断下，假设：

1. 耦合 \(H_2\) 临界曲率能量在 \([0,T]\), \(T\le cr^2\), 内保持小；
2. 固定 \(q=3\) 推导给出
   \[
   A_\alpha^4H_{3,\alpha}(t)
   \le C_N\bigl(\beta_\alpha^3/t+r^{-2}\beta_\alpha^2\bigr);
   \]
3. 固定 \(J_3,J_p\) 能量保持，且 \(p>2\).

则递推 (5.1) 成立，并给出
\[
|a\Rm|(T)\le C_N\beta_\alpha(T^{-1}+r^{-2}),
\]
\[
|aE|(T)\le C_{p,N}\delta(1+r^2/T)^{2/p}.
\]
此外，\(J_m\) 层级给出 (6.1)，但不单独蕴含点态 \(\chi\nabla(aE)\)。

尚未闭合的精确科学对象有两个：

1. 从完整归一化曲率演化出发，证明含有限邻域项的固定 \(q=2,3\) 耦合不等式，从而无循环地建立 (4.3)；
2. 在 Whitney 球上证明常数独立于 \(\chi_0\) 和塌缩体积的曲率导数–缺陷 Bernstein 定理，以控制 (6.2) 并推出 (6.3)。

这两项分别是零阶加权方案和连接/截断继续性的实际承重点。
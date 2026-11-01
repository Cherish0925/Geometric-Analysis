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
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step20_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step20_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify and strengthen the proposed weighted-moment bridge for the normalized cutoff flow in dimension four. The active goal is Yau Problem 26, but this task concerns the four-dimensional negative critical Ishida–LeBrun laboratory. Read the supplied Step 18–20 notes, Wang source excerpt/object, and exponent-check script. Assess these exact points by derivation rather than analogy: (1) for curvature F=(1+|Rm|^2)^{1/2}, whether moments H_q=∫η² a^{q-2}F^q, a=χ², naturally have dissipation/sobolev variable η a^{(q-1)/2}F^{q/2}, and what local differential inequality—including η, da, evolving measure, full velocity aE, and normalized source—can rigorously be asserted; (2) whether H_2 small and the q=3 interpolation can yield A^4 H_3(t)≤C beta^3/t (or the correct beta/r source variant) without dividing by a; (3) for the Einstein defect, whether J_m=∫η²a^{m-2}|E|^m propagates from initial |E|≤δ under the known tensor cancellation, and whether weighted cubic H_3 controls its curvature reaction through the exact J_m–J_{3m/2}–J_{2m} interpolation; (4) whether this hierarchy can start at a fixed p=6 and iterate to a pointwise a|E| estimate, thereby genuinely replacing the weaker I_p=∫|aE|^p, or identify the exact term that prevents it; (5) assess the A01 Whitney-ball argument, especially whether its use of a physical time θr² on every Whitney level is compatible with obtaining pointwise information at arbitrary t near zero and whether global support energy alone really gives the required local smallness. Give a mathematical memo distinguishing derived identities, conditional estimates, and any fatal mismatch. Do not infer that the full Yau problem is solved.

## Integrated Scientific Memo

# 数学核验备忘录：四维归一化截断流的加权矩桥

令
\[
\partial_tg=-2aE,\qquad E=\Ric+g,\qquad a=\chi^2,\qquad
F=(1+|\Rm|^2)^{1/2},
\]
并令 \(\eta\) 为与 \(\chi\) 独立、暂取时间不变的局部化函数。以下结论均只在预设的 first-exit 区间内成立；该区间上需已有度量等价、局部 Sobolev 不等式、有限邻接、截断导数及临界能量控制。

---

## 1. 曲率矩 \(H_q\)：正确变量及可严格主张的不等式

定义
\[
H_q=\int \eta^2a^{q-2}F^q\,d\mu,\qquad q\ge2.
\]

### 1.1 主耗散和 Sobolev 变量

全速度 \(-2aE\) 下，曲率方程具有结构
\[
\partial_t\Rm
=a\Delta\Rm+a(\Rm*\Rm+\Rm)
+da*\nabla E+\nabla^2a*E+aE*\Rm.
\]
这里
\[
|E|\lesssim F,\qquad |\nabla E|=|\nabla\Ric|\lesssim|\nabla\Rm|.
\]
以
\[
\eta^2a^{q-2}F^{q-2}\Rm
\]
测试主部，张量耗散是
\[
\mathcal T_q
=\int\eta^2a^{q-1}F^{q-2}|\nabla\Rm|^2.
\]
相应的自然 Sobolev 变量确为
\[
\boxed{v_q=\eta\,a^{(q-1)/2}F^{q/2}}.
\]
展开 \(\nabla v_q\) 后出现的截断代价为
\[
a^{q-3}|da|^2F^q
=\frac{|da|^2}{a}\,a^{q-2}F^q,
\qquad
\frac{|da|^2}{a}=4|d\chi|^2.
\]
因此这里没有真正除以退化系数 \(a\) 的奇性。

### 1.2 Hessian 源、体积变化和归一化项

\(\nabla^2a*E\) 项必须分部积分一次。它产生
\[
\varepsilon\mathcal T_q+
C_{\varepsilon,q}\int\eta^2a^{q-3}|da|^2F^q+
C_{\varepsilon,q}\int a^{q-1}|d\eta|^2F^q.
\]
故无需先验点态 \(\nabla^2a\) 界。

演化体积为
\[
\partial_td\mu=-a\,\tr E\,d\mu.
\]
因此体积项以及曲率范数中的逆度量变化均可估为
\[
C\int\eta^2a^{q-1}F^{q+1}.
\]
使用 \(F\ge1\) 吸收所有归一化产生的低阶幂后，可严格主张如下局部不等式：
\[
\boxed{
\begin{aligned}
\frac d{dt}H_q+c_q\int|\nabla v_q|^2
\le Cq^2\bigg[
&\int a^{q-1}|d\eta|^2F^q\\
&+\int\eta^2\frac{|da|^2}{a}\,a^{q-2}F^q\\
&+\int\eta^2a^{q-1}F^{q+1}
\bigg].
\end{aligned}}
\tag{1}
\]
常数关于 \(q\) 的精确多项式次数依赖张量约定，但不影响固定指数和 Moser 迭代。若 \(\eta=\eta(t)\)，还要加入
\[
2\int\eta\,\partial_t\eta\,a^{q-2}F^q.
\]

关键代数为
\[
Fv_q^2=\eta^2a^{q-1}F^{q+1},
\qquad
v_q^4=\eta^4a^{2q-2}F^{2q}.
\]
第二式的局部化权是 \(\eta^4\)，不是 \(H_{2q}\) 的 \(\eta^2\)；必须使用嵌套截断，不能把两者逐字等同。

这与 Wang 源中四维 \(q=2\) 的 \(\nabla(\chi|\Rm|)\) 及下一矩的 \(\nabla(\chi^2|\Rm|^{3/2})\) 权重一致；但 Wang 处理的是全局、未归一化局部 Ricci 流，不能直接替代上述归一化、有限邻接的推导。

---

## 2. 从 \(H_2\) 到加权三次矩 \(H_3\)

设扩大球上有
\[
\|\phi\|_4\le A\bigl(\|\nabla\phi\|_2+r^{-1}\|\phi\|_2\bigr),
\]
并定义真正适合 \(F\) 的临界参数
\[
\gamma:=A^2\|F\|_{L^2(\widetilde B)}.
\]

对 \(q=2\)，
\[
H_3=\int\eta^2aF^3=\int Fv_2^2
\le C\gamma\left(\int|\nabla v_2|^2+r^{-2}H_2\right).
\]
若 \(\gamma\) 足够小，(1) 中的反应项可吸收，并得到
\[
\sup_{s\le t}H_2(s)+\int_0^t\!\!\int|\nabla v_2|^2
\le Ce^{Ct/r^2}H_2(0),
\]
以及
\[
\int_0^tH_3(s)\,ds\le C\gamma H_2(0).
\tag{2}
\]

对 \(q=3\)，同理
\[
H_4=\int\eta^2a^2F^4=\int Fv_3^2
\le C\gamma\left(\int|\nabla v_3|^2+r^{-2}H_3\right).
\]
吸收后
\[
\frac d{dt}H_3\le Cr^{-2}H_3.
\]
将此不等式从某个 \(s<t\) 推到 \(t\)，再用 (2) 对 \(s\) 平均，得到
\[
H_3(t)\le \frac{C\gamma H_2(0)}{t}.
\]
而
\[
H_2(0)\le \|F\|_2^2=\frac{\gamma^2}{A^4},
\]
故
\[
\boxed{A^4H_3(t)\le \frac{C\gamma^3}{t}}.
\tag{3}
\]

若 Wang 参数定义为
\[
\beta=A^2\|\Rm\|_2,
\]
则由于 \(F^2=1+|\Rm|^2\)，一般只能直接得到
\[
\gamma\le\beta+A^2\Vol(\widetilde B)^{1/2}
\lesssim \beta+r^2,
\]
从而无条件形式是
\[
\boxed{A^4H_3(t)\le
\frac{C(\beta+Cr^2)^3}{t}}.
\tag{4}
\]
在当前近负 Einstein 实验中，若已知 \(|E|\le\delta\ll1\)，则 \(\Ric\approx-g\)，故 \(|\Rm|\) 有统一正下界并可令 \(F\lesssim|\Rm|\)；此时 \(\gamma\lesssim\beta\)，(3) 才化为
\[
\boxed{A^4H_3(t)\le C\beta^3/t}.
\tag{5}
\]
整个推导没有使用 \(F/a\) 或 \(1/a\)；唯一表面商 \(|da|^2/a\) 等于光滑有界量 \(4|d\chi|^2\)。

---

## 3. Einstein 缺陷矩 \(J_m\)

定义
\[
G=|E|,\qquad
J_m=\int\eta^2a^{m-2}G^m,\qquad
z_m=\eta a^{(m-1)/2}G^{m/2}.
\]

必须在标量化前测试张量方程，因为 \(da*E*\nabla E\) 需要完整的
\[
\int\eta^2a^{m-1}G^{m-2}|\nabla E|^2
\]
耗散。已知逆度量变化与缺陷的三次张量反应发生抵消；体积项仍存在，但
\[
a|\tr E|G^m\lesssim aG^{m+1}\lesssim aFG^m.
\]

对完整截断交换项分部积分后，可得
\[
\boxed{
\begin{aligned}
\frac d{dt}J_m+c_m\int|\nabla z_m|^2
\le Cm^2\bigg[
&\int a^{m-1}|d\eta|^2G^m\\
&+\int\eta^2\frac{|da|^2}{a}\,a^{m-2}G^m\\
&+\int\eta^2a^{m-1}FG^m
\bigg].
\end{aligned}}
\tag{6}
\]
这比 \(I_m=\int|aE|^m=\int a^mG^m\) 强两个 \(a\)-幂。

对固定 \(m\)，若临界曲率能量足够小，
\[
\int Fz_m^2
\le C\gamma\left(\int|\nabla z_m|^2+r^{-2}J_m\right),
\tag{7}
\]
可直接吸收。因此固定基指数 \(m=6\) 确可从
\[
|E(0)|\le\delta
\]
传播，并有
\[
J_6(0)\le\delta^6\Vol(\widetilde B).
\]

### 精确三次曲率插值

使用适当嵌套截断，
\[
\int\eta^2a^{m-1}FG^m
\le H_3^{1/3}J_{3m/2}^{2/3},
\tag{8}
\]
因为
\[
Fz_m^2=(aF^3)^{1/3}(a^{-1/3}z_m^2),
\]
且
\[
(a^{-1/3}z_m^2)^{3/2}
=\eta^3a^{3m/2-2}G^{3m/2}.
\]
这里 \(a^{-1/3}\) 只是 Hölder 分解的记号；乘开后的密度具有非负权 \(a^{3m/2-2}\)，不存在对 \(a\) 的分析性除法。

同时逐点密度的几何平均给出
\[
\boxed{J_{3m/2}\le J_m^{1/2}J_{2m}^{1/2}}.
\tag{9}
\]
Sobolev 不等式给出
\[
J_{2m}^{1/2}
\le CA^2\left(\int|\nabla z_m|^2+r^{-2}J_m\right).
\tag{10}
\]
结合 (8)–(10) 和 Young 不等式，
\[
\boxed{
\int\eta^2a^{m-1}FG^m
\le\varepsilon X_m+
C\varepsilon^{-2}A^4H_3\,J_m,
}
\tag{11}
\]
其中
\[
X_m=\int|\nabla z_m|^2+r^{-2}J_m.
\]
因此脚本给出的 \(J_m\)-\(J_{3m/2}\)-\(J_{2m}\) 指数链是正确的。

---

## 4. 从固定 \(p=6\) 到点态 \(a|E|\)：成立范围和剩余障碍

由 (3)，高指数能量中的势系数为
\[
Cm^3A^4H_3(t)\lesssim \frac{Cm^3\gamma^3}{t}.
\]
它不能从 \(t=0\) 直接作 Grönwall 积分。正确的两阶段构造是：

1. 用固定指数吸收式 (7) 从初时刻传播 \(J_6\)；
2. 对任意给定 \(t>0\)，只在时间柱 \([t/2,t]\) 上作
   \[
   m\mapsto\frac32m
   \]
   的 Moser 迭代，此时 \(H_3(s)\lesssim \gamma^3/(A^4t)\)。

配合嵌套时空截断，得到条件性估计
\[
\|aE(\cdot,t)\|_{L^\infty(B')}
\le
CA^{2/3}(t^{-1}+r^{-2})^{1/3}J_6(0)^{1/6}.
\]
再用
\[
A\lesssim rV^{-1/4},\qquad J_6(0)^{1/6}\le\delta V^{1/6},
\]
体积幂恰好抵消：
\[
\boxed{
\|aE(\cdot,t)\|_\infty
\le C\delta\left(1+\frac{r^2}{t}\right)^{1/3}}.
\tag{12}
\]
而
\[
\left(a^{m-2}|E|^m\right)^{1/m}
=a^{1-2/m}|E|\longrightarrow a|E|,
\]
故这一层级确实比 \(I_p\) 强，并能在权重和指数层面替代 \(I_p\) 来获取点态 \(a|E|\)。

但它没有给出 Step 19 关闭 connection/Hessian 漂移所需的
\[
|\chi\nabla(aE)|
\lesssim\delta\,t^{-1/2}(r^2/t)^{1/3}.
\]
直接微分缺陷方程会产生
\[
a\,\nabla\Rm*U,
\]
以及更高截断导数项；仅有 \(|a\Rm|\lesssim t^{-1}\) 和 (12) 不足以控制该项。因此，固定 \(p=6\) 的加权矩桥解决的是点态速度，而非加权 Bernstein 估计。这个导数项仍是 first-exit 中连接和 \(\nabla^2a\) 延拓的实质障碍。

---

## 5. Whitney 球方案的核验

在 \(y\) 点令
\[
a_0=\chi(y)^2,\qquad \ell=cr\chi(y).
\]
若 \(|\nabla\chi|\le L/r\)，则在 \(B_\ell(y)\) 上
\[
\frac a{a_0}\in[(1-Lc)^2,(1+Lc)^2].
\]
有效时间为 \(\tau=a_0t\)，而
\[
\frac{\tau}{\ell^2}
=\frac{t}{c^2r^2}.
\]
因此同一个物理时间范围
\[
0<t\le\theta r^2,\qquad \theta<c^2,
\]
确实与所有 Whitney 层兼容。对任意很小的 \(t>0\)，扩散半径
\[
\sqrt{a_0t}=\chi(y)\sqrt t
\]
仍位于相应 Whitney 球内。故“每层使用同一物理时间 \(\theta r^2\)”本身并不妨碍在任意近零时刻取得点态信息；估计按预期在 \(t\downarrow0\) 时发散。

但 A01 论证有两处必须修正：

1. 系数变化实际是
   \[
   \frac{|a-a_0|}{a_0}\le 2Lc+(Lc)^2=O(c),
   \]
   不是 \(O(c^2)\)。可通过选小 \(c\) 控制，但不能漏掉一阶项。

2. 单一的全支撑平均能量
   \[
   \int_\Omega F^2\le K_0\Vol(\Omega)
   \]
   对一个可能含许多分量的大并集，并不推出每个 Whitney 球的临界小能量；能量可集中在单个分量。所需输入应是局部预算，例如
   \[
   \int_{B_{10r}(y)}F^2\le K_0\Vol(B_{10r}(y)),
   \]
   或等价的每分量/有限邻接能量控制。此时 Bishop–Gromov 与 provisional metric equivalence 才给出
   \[
   \ell^4\fint_{B_\ell(y)}F^2\le CK_0r^4,
   \]
   且常数独立于 \(\chi(y)\)。

有限重叠只能控制非归一化积分的和，不能自动控制体积归一化能量的和。

---

## 结论

加权矩的代数与 Sobolev 结构是正确的：

- 曲率变量是 \(\eta a^{(q-1)/2}F^{q/2}\)；
- \(H_2\) 与 \(q=3\) 步可给出
  \[
  A^4H_3\lesssim \gamma^3/t,
  \]
  在近 Einstein 输入下为 \(C\beta^3/t\)，一般则应写成 \(C(\beta+Cr^2)^3/t\)；
- 缺陷矩 \(J_m\) 具有正确的张量耗散，且曲率反应严格通过
  \[
  H_3,\quad J_{3m/2},\quad J_m,\quad J_{2m}
  \]
  闭合；
- 从固定 \(J_6\) 出发，可条件性迭代到点态 \(a|E|\)，因此这一层级确实强于并可替代 \(I_p\) 完成速度估计。

尚未解决的是完整 first-exit：需要在有限邻接的演化几何中落实上述局部不等式，并另外证明加权导数/Bernstein 估计以控制 \(a\nabla\Rm*U\) 所导致的 connection 与 cutoff-Hessian 漂移。Whitney 时间尺度并非致命问题；真正错误是以全支撑平均能量替代逐局部小能量，以及把 \(a/a_0\) 的变化误记为 \(O(c^2)\)。这些结果并不构成 Yau 第26题的证明。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 28,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step28_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step28_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the complete analytic chain for the normalized cutoff flow on the selected disjoint supports. Read the actual derivations, not their status labels. Determine whether the q=2 and q=3 estimates, global Q and J6 propagation, general-p tensor inequality, three-factor/time-slab Moser iteration, first-exit closure, and shifted-curvature continuation form a logically closed proof with volume-independent constants for a fixed critical four-manifold. Attack the most consequential non-routine transitions: active-region versus collar energy, use of the unweighted F factor, relative Sobolev domains, polynomial p dependence, terminal H3 propagation, the t=0 splice, and the current-order Wang derivative induction. State any precise missing lemma or false inference, with equations and a concrete repair if available. Do not infer validity from scripts or prior summaries.

## Integrated Scientific Memo

# 核验结论

就给定文件而言，归一化截断流的局部解析链**尚不能称为完全闭合的、自包含的证明**。以下部分在作必要修正后是相互一致且局部体积无关的：

\[
q=2,3\ \text{能量}
\Longrightarrow H_3(t)\ \text{终端控制}
\Longrightarrow Q,J_6\ \text{传播}
\Longrightarrow \text{正时间 Moser}
\Longrightarrow |a\Rm|,\ |aE|
\Longrightarrow \text{第一退出改进}.
\]

但仍有两个实质性缺口：

1. Step 26 的一般 \(p\) 证明没有从其所写的 \(D_p\) 控制推出统一系数的
   \(\|\nabla Z_p\|_2^2\)；必须保留 \(p(p-2)\) 标量梯度耗散，或接受一个多项式退化的耗散系数。
2. shifted-curvature continuation 的关键当前阶 Wang 能量引理仍通过“verbatim Wang/有限错列指数”调用，给定文本没有展开足以独立复核的分组积分和指数配置。

因此：**若补入这两个精确引理，局部流解析链可闭合；按当前展示的推导，它仍是条件性闭合。**

---

## 1. 活动区能量必须替代包含静止 collar 的能量

Step 23 定义
\[
\gamma_j=S_j\|F\|_{L^2(U_j)}
\]
有缺陷：\(U_j\) 包含 \(a=0\) 的静止 collar，其曲率能量不受活动区估计改善。

正确变量是
\[
\widehat H_2(t)
 =\int_{\supp\chi}F^2\,d\mu_t,\qquad
\beta(t)=S(t)\widehat H_2(t)^{1/2}.
\]
若
\[
C_{\rm col}
=\int_{\supp\eta\setminus\supp\chi}\eta^2F_0^2\,d\mu_0,
\]
则 \(H_2=\widehat H_2+C_{\rm col}\)，且 \(C_{\rm col}\) 恒定。

不能从已经粗化为 \(Cr^{-2}H_2\) 的不等式中形式地减去 \(C_{\rm col}\)。必须在逐项推导时利用：所有变化项都含有
\[
a,\quad da,\quad\text{或}\quad \frac{|da|^2}{a}=4|d\chi|^2,
\]
故支撑在活动区。由此才得到
\[
\boxed{
\widehat H_2'+cD_2
\le Cr^{-2}\widehat H_2+C H_3,
\qquad H_3=\int aF^3.}
\]
Step 26 的活动区修复是正确方向；其中后来写出的
\(\widehat H_2(0)+C_{\rm col}\) 只是多余且较弱，正确 Grönwall 直接给出
\[
\widehat H_2(t)\le e^{Ct/r^2}\widehat H_2(0).
\]

---

## 2. \(q=2\)、\(q=3\) 与终端 \(H_3\) 传播成立

无权 \(F\) 因子的使用是合法的，因为其他因子支撑在活动区：
\[
H_3=\int_{\supp\chi}F(\chi F)^2
\le \|F\|_{2,\supp\chi}\|\chi F\|_4^2.
\]
相对 Sobolev 不等式和
\[
|\nabla(\chi F)|^2
\le 2a|\nabla\Rm|^2+2|d\chi|^2F^2
\]
给出
\[
H_3\le C\beta(t)\bigl(D_2+r^{-2}\widehat H_2\bigr).
\]
当 \(\beta\) 足够小时，
\[
\widehat H_2'+\frac c2D_2
\le Cr^{-2}\widehat H_2,
\]
因而
\[
\int_0^tH_3(s)\,ds
\le C\beta_*\widehat H_2(0).
\]

对 \(q=3\)，令 \(v_3=aF^{3/2}\)。有
\[
\int a^2F^4=\int Fv_3^2
\le \|F\|_{2,\supp\chi}\|v_3\|_4^2,
\]
且
\[
|\nabla v_3|^2
\le Ca^2F|\nabla\Rm|^2+C|da|^2F^3
\le CD_3+Cr^{-2}H_3.
\]
吸收后
\[
H_3'\le Cr^{-2}H_3.
\]

于是选取 \(s\in[t/4,t/2]\) 满足
\[
H_3(s)\le \frac4t\int_0^{t/2}H_3(\tau)\,d\tau,
\]
再由 \(q=3\) 方程向前传播至 \(t\)，得到
\[
H_3(t)\le \frac{C\beta_*\widehat H_2(0)}t,
\qquad
\boxed{S^2H_3(t)\le \frac{C\beta_*^3}{t}.}
\]
这一步确实排除了终端尖峰；它不是仅由时空积分作出的平均值推断。

---

## 3. 全局 \(Q\) 与 \(J_6\) 传播成立

对
\[
Q=\int_M|E|^2,
\]
齐次缺陷方程给出
\[
Q'+c\int a|\nabla E|^2
\le C\int\left(\frac{|da|^2}{a}+a\right)|E|^2
 +C\int aF|E|^2.
\]
在每个互不相交的活动支撑上，
\[
\int aF|E|^2
=\int F|\chi E|^2
\le \|F\|_{2,\supp\chi}\|\chi E\|_4^2.
\]
由小 \(\beta\) 吸收梯度项，求和不产生支撑个数因子，故
\[
\boxed{Q'(t)\le Cr^{-2}Q(t).}
\]

对
\[
J_6=\int a^4|E|^6,\qquad Z_6=a^{5/2}|E|^3,
\]
反应项满足
\[
\int a^5F|E|^6
=\int F|Z_6|^2
\le \|F\|_{2,\supp\chi}\|Z_6\|_4^2.
\]
相对 Sobolev 给出
\[
J_6'+c\|\nabla Z_6\|_2^2
\le Cr^{-2}J_6+
 C\beta\bigl(\|\nabla Z_6\|_2^2+r^{-2}J_6\bigr).
\]
故
\[
\boxed{J_6(t)\le e^{Ct/r^2}J_6(0).}
\]
初始 \(|E|\le\delta\) 因而保留 \(\delta^6\) 因子。此处不需要从零时刻积分非可积的 \(H_3(t)\sim t^{-1}\)。

---

## 4. 一般 \(p\) 推导中的精确缺陷与修复

Step 26 从
\[
K_p'+cD_p\le Cp^2r^{-2}K_p+CpR_p
\]
推到
\[
K_p'+c\|\nabla Z_p\|_2^2
\le Cp^2r^{-2}K_p+CpR_p
\]
按其已写论证并不成立，因为
\[
\|\nabla Z_p\|_2^2
\lesssim p^2D_p+p^2r^{-2}K_p.
\]
仅有 \(cD_p\) 时，最多得到 \(cp^{-2}\|\nabla Z_p\|_2^2\)。

修复存在于原始 Laplacian 计算中，但必须明确保留：
\[
\begin{aligned}
K_p'
&+c_1p\int a^{p-1}F^{p-2}|\nabla\Rm|^2\\
&+c_2p(p-2)\int a^{p-1}F^{p-2}|\nabla F|^2\\
&\le Cp^2r^{-2}K_p+CpR_p .
\end{aligned}
\]
第二项具有与 \(Z_p=a^{(p-1)/2}F^{p/2}\) 的 \(F\)-梯度部分相匹配的 \(p^2\) 系数；结合 cutoff 梯度项
\[
a^{p-3}|da|^2=4a^{p-2}|d\chi|^2
\]
才可得到统一的
\[
\boxed{
K_p'+c\|\nabla Z_p\|_2^2
\le Cp^2r^{-2}K_p+CpR_p.}
\]
正则化缺陷
\(\Phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2}\)
同样必须保留链式法则产生的
\[
p(p-2)a\Phi_\varepsilon^{p-2}
|\nabla\Phi_\varepsilon|^2.
\]

另一种可行修复是接受耗散系数 \(cp^{-2}\)；这只会提高右端的固定多项式 \(p^N\)，Moser 乘积仍收敛。但当前文本声称统一 \(c\)，就必须写出上述耗散。

所需精确引理是：

> 对所有 \(p\ge3\)，曲率及正则化缺陷均满足一个完整张量能量不等式，其耗散系数或者一致正，或者仅按固定多项式退化；所有 Hessian-\(a\)、移动范数、移动体积和 Lichnerowicz 反应项的总损失不超过 \(Cp^Nr^{-2}K_p+Cp^NR_p\)，其中 \(N\) 与 \(p\) 无关。

现有文本只对代表性项充分展开，尚未完全证明该引理。

---

## 5. 三因子吸收和时间薄片 Moser 迭代是正确的

精确分解为
\[
\eta^2a^{p-1}F\Phi^p
=(aF^3)^{1/3}
(\eta^2a^{p-2}\Phi^p)^{1/3}
|Z_p|^{4/3}.
\]
因此
\[
R_p\le Y^{1/3}K_p^{1/3}\|Z_p\|_4^{4/3},
\qquad Y=\int aF^3.
\]
Sobolev 与 Young 给出
\[
CpR_p
\le \frac c2\|\nabla Z_p\|_2^2
 +Cp^3\bigl(r^{-2}+S^2Y\bigr)K_p.
\]
这里 \(Y\) 是线性势系数，而不是随 \(p\) 缩小的临界小量。

关键权重插值是
\[
\boxed{K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}},
\qquad
K_{2p}=\|Z_p\|_4^4,
\]
其中第二式使用了 \(\eta=1\) 于整个 \(a>0\) 区域。它补回了零集附近容易丢失的半个 \(a\)-权重。

在 \([t/2,t]\) 上，
\[
S^2Y(s)\le C\beta^3/t.
\]
时间 cutoff 后，
\[
\mathcal M_{3p/2,j+1}
\le CS\bigl(L_j\mathcal M_{p,j}\bigr)^{3/2},
\qquad
L_j=Cp^N4^j(t^{-1}+r^{-2}).
\]
由于
\[
\sum_j\frac1{p_j}<\infty,\qquad
\sum_j\frac{j+\log p_j}{p_j}<\infty,
\]
任意固定多项式 \(p^N\) 都无害。可取 \(\tau_j\uparrow3t/4\)，从而直接在非退化终端薄片上得到：

\[
\boxed{\|aF(t)\|_\infty\le C\beta/t},
\]
以及由 \(J_6\) 种子
\[
\boxed{
\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3}.}
\]

---

## 6. 相对 Sobolev 域和体积消去必须统一到同一个外球

证明中应固定一个外球
\[
\supp\eta\Subset B_R(x),\qquad R\simeq r,
\qquad V_R=\Vol(B_R(x)).
\]
所有常数均用该球：
\[
S\le C(4,KR^2)R^2V_R^{-1/2},
\]
\[
\int_{\supp\chi}F(0)^2\le CK_0V_R,
\qquad
J_6(0)\le\delta^6V_R.
\]
于是
\[
\beta(0)\le CR^2\sqrt{K_0},
\]
与塌缩体积无关；缺陷端则
\[
S^{1/3}V_R^{1/6}\le CR^{2/3}.
\]
故两种 Moser 输出中的体积确实完全消去。

原笔记在 \(U_j,B_r,B_{6r}\) 之间交替。只要最大函数估计和 Sobolev 不等式均在同一个固定倍数外球上陈述，这不是本质障碍；若局部 Poincaré/Sobolev 使用膨胀球，其膨胀必须被预留 buffer 包含。

---

## 7. 第一退出与 \(t=0\) 拼接可以闭合

缺陷估计可积：
\[
\int_0^{\theta r^2}\|aE(s)\|_\infty\,ds
\le C\delta\theta^{2/3}r^2.
\]
因而
\[
e^{-2I(t)}g_0\le g(t)\le e^{2I(t)}g_0,
\qquad
I(t)=\int_0^t\|aE(s)\|_\infty ds,
\]
严格改善度量比较，并随之改善 Sobolev 常数、固定域体积、\(|d\chi|\) 和 \(\beta\)。结合
\[
\widehat H_2(t)\le e^{C\theta}\widehat H_2(0),\quad
Q(t)\le e^{C\theta}Q(0),\quad
J_6(t)\le e^{C\theta}J_6(0),
\]
小 \(\theta,\delta,\beta(0)\) 下第一退出条件可严格改善。

\(t=0\) 不存在逻辑断裂：

- 短时光滑存在提供每个固定初值的初始时间段；
- \(J_6\) 从 \(t=0\) 直接传播；
- \(|aE|\sim t^{-1/3}\) 可积；
- \(|a\Rm|\sim t^{-1}\) 从不在零时刻积分，仅用于正终端时刻的 continuation。

若最大存在时间 \(T>0\)，则在 \([T/2,T)\)
\[
|a\Rm|\le 2C\beta/T
\]
一致有界，早期紧区间由光滑性控制。因此 continuation 只需处理正时间终端。

---

## 8. shifted-curvature 代数正确，但当前阶 Wang 引理尚未在文本内证明

取
\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\Rm+G,\qquad U=aT.
\]
则
\[
\Ric(G)=g,\qquad
aE=\Ric(U),\qquad
g_t=-2\Ric(U).
\]
因此 connection evolution 中没有独立的 \(ag\) 分支。移位曲率满足
\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T).
\]
特别地不存在独立的 \((\nabla^2a)*G\) 源；\(T=0\) 对应负 Einstein 静止解，这也是必要一致性检查。

基本无权估计
\[
\frac d{dt}\int|T|^p+
c_p\int a|\nabla T|^2|T|^{p-2}
\le C_p\int|T|^p
\]
是可信且已给出核心证明：对 Hessian-\(a\) 积分一次，并使用
\[
|da|^2/a=4|d\chi|^2.
\]

真正未自包含展开的是当前阶 \(U\) 导数估计。原始方程包含
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U,\quad
\Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
\]
\[
\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,\quad
\Gamma_4=\chi\nabla\chi*\nabla^{m+1}U.
\]
所需结论是
\[
\left|
\int |\nabla^mU|^{p-2}\nabla^mU*
\sum_{\nu=1}^4\Gamma_\nu
\right|
\le \varepsilon D_m+
C\bigl(1+\|\nabla^mU\|_p^p\bigr),
\]
并与
\[
\partial_t\nabla^{m+1}\chi
\sim \nabla^mU*\nabla\chi+\text{低阶}
\]
组成有限错列指数的 Volterra 系统
\[
Y_m'+cD_m
\le C_m\left(1+Y_m+\int_0^tY_m(s)\,ds\right).
\]

给定文件只说明：

- \(\Gamma_4\) 由加权耗散吸收；
- \(\Gamma_1,\Gamma_2,\Gamma_3\) 按 Wang Proposition 4.14 分组积分；
- 唯一残余顶阶 cutoff 乘积为
  \[
  \nabla^2\chi*\nabla^m\chi*U*
  \nabla^mU|\nabla^mU|^{p-2};
  \]
- 新增 \(G\)-项只是有界线性或低阶项。

这些结构判断是正确的，且说明归一化本身没有引入新障碍；但分组收缩、每一项的 Hölder 指数以及有限错列指数族尚未实际列出。因此 continuation 模块仍依赖一个未展开的源定理迁移。

所需补充的精确引理是：

> 对每个 \(m\)，存在有限个均大于 \(n+2\) 的指数，使 \(\nabla^mU\) 与 \(\nabla^{m+1}\chi\) 的联合能量满足上述 Volterra 不等式；所有 \(\Gamma_1,\ldots,\Gamma_4\) 的顶阶项均由 \(D_m\) 或当前 cutoff 能量控制，且新增 \(G\)-单项式不引入 \(\nabla^{m+1}U\) 或 \(\nabla^{m+2}\chi\) 的未控制输入。

归一化 DeTurck restart 的形式是正确的：同一个 transported coefficient \(\widehat a\) 必须同时乘在 \(\Ric(\widehat g)\) 和 \(\widehat g\) 前；否则拉回后不能恢复固定 \(a\) 的原方程。

---

# 最终判定

- **已核准：**活动区 \(q=2,3\)、终端 \(H_3\)、全局 \(Q\)、固定 \(J_6\)、三因子吸收、时间薄片 Moser、四维体积消去、第一退出改进以及 \(t=0\) 拼接。
- **须修正：**一般 \(p\) 推导必须保留 \(p(p-2)\) 梯度耗散，不能仅凭 \(D_p\) 宣称统一的 \(\|\nabla Z_p\|_2^2\) 系数。
- **尚缺的实质引理：**完整一般 \(p\) 张量账本，以及当前阶 normalized Wang 分组积分/错列指数引理。
- **条件性结论：**承认上述两个引理后，该固定四维临界流的解析链可用局部体积无关常数闭合；按当前文件中实际展示的推导，尚未达到完全自包含的闭合证明。
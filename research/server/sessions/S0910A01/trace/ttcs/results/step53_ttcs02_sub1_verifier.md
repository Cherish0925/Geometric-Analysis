# TTCS Independent Branch Record

```json
{
  "step_id": 53,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A03/workspace/notes/step55_direct_nonlinear_flow_construction.md",
    "Sessions/S0910A03/workspace/scripts/verify_step55_direct_construction.py",
    "Sessions/S0910A03/workspace/data/step55_direct_construction_checks.json",
    "Sessions/S0910A01/trace/ttcs/results/step53_ttcs01_verifier1_integration.md",
    "Sessions/S0910A01/workspace/notes/step45_consolidated_IL_negative_gap_proof.md"
  ]
}
```

## Task

Verify A03 Step56's repaired direct transported-cutoff flow construction after the Step55 critique. Read the Step56 note, the Step55 note/checks for context, the TTCS Step53 critique, and the patched A01 Step45 consolidated IL proof. Focus on whether the tame product lemma and arbitrary-order hierarchy really repair the false derivative split; whether the doubly regularized parabolic-scalar-viscosity system can be used without epsilon/nu losses; whether the smooth epsilon,nu->0 passage and pullback give a per-datum exact flow; and whether the corrected first-exit interface (unweighted H2/K2, stationary Q remainder, per-datum start plus positive-time continuation) is coherent. Also check the patched Liouville-invariance averaging in A01 Step45 lines around 560--580: does it remove the exponential-map multiplicity concern under collapse? Identify remaining mathematical work before the restricted Ishida--LeBrun theorem is complete, without treating Step56 as a global Yau-26 solution.

## Output

# 科学核验备忘录

## 总结

Step 56 在解析结构上实质修复了 Step 55 的错误导数分拆。其两导数 tame 乘积估计足以把所有非主导项控制为当前 \(H^m\) 能量的线性函数，而不再假设高阶系数导数由固定低阶能量控制。双重正则化系统的能量计算也未出现 \(\varepsilon^{-1}\) 或 \(\nu^{-1}\)。

在补入标准的固定参数抛物理论以及 tame 引理的完整证明后，现有论证支持：

\[
(g_0,\chi)\longmapsto (G,\beta)\longmapsto g=\varphi^*G
\]

给出逐数据的光滑短时解

\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]

修正后的 first-exit 接口在逻辑上相容：\(H_2\) 必须不带 \(a\) 权重，全局 \(Q\) 必须包含静止区域余项，逐数据起动与统一观测时间应通过正时间延拓连接。不过，first-exit 微分不等式和正时间全阶延拓在所供材料中仍主要以模块形式出现，尚未形成逐项推导。A01 Step45 的 Liouville 测度改写确实消除了塌缩时指数映射多重覆盖带来的常数问题。

---

## 1. Tame 乘积引理确实修复了高阶导数问题

设一个乘积中高阶因子的导数阶数为 \(q_i>4\)。在固定的 \(W^{4,\infty}\) 低阶控制下，Gagliardo–Nirenberg 插值可写成

\[
\|D^{q_i}u_i\|_{L^{p_i}}
 \le C_R\|u_i\|_{H^m}^{\theta_i},
\qquad
\theta_i=\frac{q_i-4}{m-4},
\qquad
\frac1{p_i}=\frac{\theta_i}{2}.
\]

若只有一个高阶因子，则 \(q_i\le m\) 给出 \(\theta_i\le1\)。若有 \(k\ge2\) 个高阶因子，由总导数预算 \(\sum q_i\le m+2\)，

\[
\sum_i\theta_i
 \le \frac{m+2-4k}{m-4}
 \le \frac{m-6}{m-4}<1.
\]

其余至多四阶的因子置于 \(L^\infty\)。在紧流形上，\(\sum 1/p_i\le1/2\) 足以得到 \(L^2\) 乘积估计，因此

\[
\left\|\prod_iD^{q_i}u_i\right\|_2
 \le C_{m,R}\left(1+\sum_i\|u_i\|_{H^m}\right).
\]

光滑复合 \(G\mapsto G^{-1}\) 的 Faà di Bruno 展开仍由同一导数预算控制。这正是 (2.6) 所需的线性高阶结构。

对系统中各项，最高分配可明确列成：

- 主项：\(A D^{m+2}G\) 产生耗散，\(DA*D^{m+1}G\) 单独作加权 Young 估计；
- \(Q\) 项：\(A*DG*D^{m+1}G\) 单独吸收；
- Lie 项：\(\beta D\beta*D^{m+1}G\) 以及 \(\beta W*D^{m+1}\beta\)；
- 输运项：\(V\cdot D^{m+1}\beta\) 以及 \(\beta^2D\beta*D^{m+1}G\)。

取出这些项后，其余每个乘积中未知量的总导数阶数至多 \(m+2\)，每个单独因子至多 \(m\)，所以 (2.6) 可以逐项应用。特别是

\[
\sum_{j=2}^mD^jA*D^{m-j+2}G
\]

不再需要 Step 55 中错误的 \(j\le m-s\) 分拆。

目前 (2.6) 的文字证明仍是提要。完整版本需要明确张量乘积、光滑复合、固定背景曲率交换子及有限乘积个数，但这些内容与上述插值计算一致，没有显现新的导数损失。

---

## 2. 双重正则化没有产生 \(\varepsilon,\nu\) 损失

固定 \(\varepsilon,\nu>0\) 时，主符号是对角的：

\[
\operatorname{diag}\!\left(
(\beta^2+\varepsilon)G^{ab}\xi_a\xi_b\,\mathrm{Id}_{S^2},
\ \nu\bar g^{ab}\xi_a\xi_b
\right),
\]

因此系统是标准的强抛物拟线性系统。最大值原理也正确给出 \(0\le\beta\le1\)。

关键权重比值为

\[
\frac{\beta^2}{\beta^2+\varepsilon}\le1,\qquad
\frac{\beta^4}{\beta^2+\varepsilon}\le1.
\]

此外，

\[
DA=2\beta D\beta\,G^{-1}
   +(\beta^2+\varepsilon)D(G^{-1}),
\]

所以主项第一次系数微分同样不需要除以 \(\varepsilon\)。\(Q\) 的最高项带完整系数 \(A=\beta^2+\varepsilon\)，加权 Young 后余项只多出一个有界的 \(A\)。标量扩散的交换子均乘以 \(\nu\le1\)，也不需要除以 \(\nu\)。

因此 (3.2) 的常数可独立于两个参数。低阶层级应按标准连续性论证理解：先在

\[
\lambda\bar g\le G\le\lambda^{-1}\bar g,\qquad
\mathcal E_{s_0}\le R^2
\]

成立的最长时间上推导多项式估计，再利用

\[
\|\partial_tG\|_{H^{s_0-2}}
+\|\partial_t\beta\|_{H^{s_0-2}}
\le P(1+\mathcal E_{s_0})
\]

保持度量正定并改善预设界。固定参数的抛物延拓随后把每个近似解延伸到同一个逐数据时间 \(T_0\)。

高阶估计在该时间段上具有

\[
\mathcal E_m'\le C_{m,R}(1+\mathcal E_m),
\]

其中 \(C_{m,R}\) 只使用已经固定的低阶界。故所有 \(m\) 共用 \(T_0\)，这正是 Step 55 所缺少的 tame 特征。

---

## 3. 光滑极限与几何拉回

所有空间阶数的统一 \(H^m\) 界，加上方程给出的

\[
\|\partial_tG\|_{H^{m-2}}
+\|\partial_t\beta\|_{H^{m-2}}\le C_m,
\]

足以逐阶取得强紧性。反复时间微分只引入更高空间导数和系数 \(\varepsilon,\nu\)，不引入其倒数，因此可以得到时空 \(C^k\) 收敛。于是

\[
\varepsilon_jG_j^{-1}D^2G_j\to0,\qquad
\nu_j\bar\Delta\beta_j\to0
\]

在任意固定 \(C^k\) 中成立，极限解满足未正则化系统。

拉回计算完全正确。令

\[
X=-\beta^2W(G),\qquad
\partial_t\varphi=X\circ\varphi.
\]

则

\[
\frac d{dt}\beta(t,\varphi(t,x))
=\partial_t\beta+D\beta(X)=0,
\]

所以 \(\beta\circ\varphi=\chi\)。又因

\[
\partial_tG
=-2\beta^2(\operatorname{Ric}_G+G)
+\mathcal L_{\beta^2W}G,
\]

有

\[
\partial_t(\varphi^*G)
=\varphi^*(\partial_tG+\mathcal L_XG)
=-2\chi^2\bigl(\operatorname{Ric}_{\varphi^*G}+\varphi^*G\bigr).
\]

这给出逐数据存在性。Step 56 没有从规范系统推出任意几何解之间的唯一性，但后续 IL 论证只使用一个可延伸的光滑分支。

Step 55 的 Python/JSON 文件不能补充这里的解析证明：其中多数布尔条件直接写为 `True`，并仍保留正文已经弃用的一般张量“反对称积分恒等式”。Step 56 的实质依据是新的 tame 能量计算，而不是该脚本。

---

## 4. First-exit 接口的两项修正正确

### 4.1 \(H_2\) 必须不带 \(a\) 权重

由

\[
H_q^\alpha=\int\eta_\alpha^2a^{q-2}F_T^q
\]

可见

\[
H_2^\alpha=\int\eta_\alpha^2F_T^2.
\]

这使初始曲率能量覆盖整个 \(\eta_\alpha\) 缓冲区，包括 \(a\) 很小的过渡环带。若额外插入 \(a\)，局部 Sobolev 吸收无法控制这些位置。由最大函数条件和

\[
F_T^2\asymp 1+|\operatorname{Rm}|^2
\]

得到 (6.3) 是一致的。

### 4.2 全局 \(Q\) 必须包含静止余项

若外层 \(\eta_\alpha\) 支撑互不相交，且每个 \(\eta_\alpha=1\) 于 \(\operatorname{supp}a\) 的一个开邻域，则

\[
1-\rho,\qquad \rho=\sum_\alpha\eta_\alpha^2,
\]

只支撑在一个 \(a=0\) 的开区域中。精确几何流在该区域恒等于初始度量，因此 Ricci 张量、\(E\) 和体积元都不变：

\[
Q_{\mathrm{rest}}(t)=Q_{\mathrm{rest}}(0).
\]

于是

\[
Q_{\mathrm{global}}(t)
=Q_{\mathrm{rest}}(0)+\sum_\alpha Q_\alpha(t)
\]

是正确恒等式。选取的缓冲支撑不必覆盖整个流形。

### 4.3 逐数据起动加正时间延拓

这一逻辑结构是相容的，但依赖两个尚未在所供材料中完整推导的定理：

1. 任意已有光滑分支上，first-exit 估计的常数只使用不带权 \(H_2\)、局部 Sobolev系数、\(|d\chi|\)、初始 defect 和支撑缓冲；
2. 若 \(aF_T\) 在终端时间片有界，则 staggered 层级能控制过渡环带中的不带权曲率、固定坐标高阶导数和 cutoff 协变导数，从而得到光滑终点。

特别地，单独知道

\[
\|aF_T(t)\|_\infty\le C/t
\]

并不能直接控制 \(a\to0\) 位置的 \(|F_T|\)。Step45 §5.3 所述不带权 \(T\) 种子和

\[
T_0\to(U_1,C_2)\to T_1\to\cdots
\]

正是填补这一点所需的机制，但其完整能量推导尚未出现。因此“每个数据都达到统一时间 \(\theta r^2\)”目前是有明确解析路线的结论，仍依赖该正时间延拓模块。

---

## 5. Liouville 测度改写消除了多重覆盖问题

A01 Step45 的补丁是有效的。Rauch 比较在

\[
\rho<cK^{-1/2}
\]

且所有相关测地线留在平台内时给出

\[
c\,t^3\le J_p(t,\xi)\le C\,t^3.
\]

因此

\[
A_\rho\Phi(p)
\le C\rho^{-4}\int_0^\rho t^3
 \int_{S_pM}\Phi(\pi\varphi_t(p,\xi))\,d\xi\,dt.
\]

对 \(p\in P^{\mathrm{in}}\) 积分，并使用

\[
d\Lambda=d\mu(p)\,d\xi
\]

及测地流对 Liouville 测度的不变性：

\[
\begin{aligned}
\int_{SM|_{P^{\mathrm{in}}}}
 \Phi(\pi\varphi_t(v))\,d\Lambda(v)
&\le
\int_{SM}\Phi(\pi\varphi_t(v))\,d\Lambda(v)\\
&=
\int_{SM}\Phi(\pi v)\,d\Lambda(v)
=\omega_3\int_M\Phi\,d\mu .
\end{aligned}
\]

这里每个初始单位向量只被计算一次；无需把终点按指数映射原像数目计数。即使 \(\exp_p\) 多对一，上式的常数也不会随短闭测地线的数量增长。

局部下界则在切空间球上的拉回度量 \(\exp_p^*g\) 上使用。只要 \(\rho\) 小于共轭尺度，拉回度量光滑，Rauch 给出统一体积比，故局部 \(\Phi\) 下界可转化为 \(A_\rho\Phi(p)\ge\eta'>0\)。这一部分还需在正式证明中明确 \(\rho\) 同时满足平台缓冲距离和 Rauch 尺度要求。

---

## 6. 受限 IL 定理尚缺的数学内容

现有材料中仍需形成完整推导的对象是：

- 固定 \((\varepsilon,\nu)\) 的拟线性抛物定理，或严格定义的谱截断构造；
- (2.6) 的完整张量版证明及系统中全部交换子的逐项归类；
- 不带权 \(H_2\)、\(Y\)、\(J_6\)、全局 \(Q\) 与 metric drift 的微分不等式，尤其要把 \(\chi\nabla^2\chi\) 项积分转化为只依赖统一一阶 cutoff 数据的量；
- 从终端时间片上的加权曲率控制到光滑终点的 staggered 延拓定理；
- 终端平台缓冲、曲率界、切空间拉回体积下界与 Liouville 平均之间的统一参数选择；
- Proposition 3.2 中局部 harmonic-radius 紧性与 Ricci 方程椭圆升级的完整书写；
- Seiberg–Witten、Chern–Weil 和 Derdziński 输入的原始来源核对及常数归一化。

因此，Step 56 已经提供了可信而重要的逐数据 cutoff-flow 起动模块，并修正了 Step 55 的核心高阶问题；它本身尚未完成受限 IL 间隙定理，更未处理所有维数的 Yau 第26题或 Lean 4 形式化。
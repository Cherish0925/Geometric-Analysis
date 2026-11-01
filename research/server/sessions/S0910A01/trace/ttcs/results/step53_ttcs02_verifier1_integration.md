# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 53,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step53_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step53_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify A03 Step56's repaired direct transported-cutoff flow construction after the Step55 critique. Read the Step56 note, the Step55 note/checks for context, the TTCS Step53 critique, and the patched A01 Step45 consolidated IL proof. Focus on whether the tame product lemma and arbitrary-order hierarchy really repair the false derivative split; whether the doubly regularized parabolic-scalar-viscosity system can be used without epsilon/nu losses; whether the smooth epsilon,nu->0 passage and pullback give a per-datum exact flow; and whether the corrected first-exit interface (unweighted H2/K2, stationary Q remainder, per-datum start plus positive-time continuation) is coherent. Also check the patched Liouville-invariance averaging in A01 Step45 lines around 560--580: does it remove the exponential-map multiplicity concern under collapse? Identify remaining mathematical work before the restricted Ishida--LeBrun theorem is complete, without treating Step56 as a global Yau-26 solution.

## Integrated Scientific Memo

# 核验结论

Step 56 **实质修复了** Step 55 的错误高阶导数分拆，并给出了可信的逐数据光滑 cutoff-flow 构造。其核心结论可接受为：

> 对每个固定光滑数据 \((g_0,\chi)\)，在补全标准的 tame 乘积证明和固定参数抛物理论后，存在 \(T(g_0,\chi)>0\) 及至少一个光滑解
> \[
> \partial_t g=-2\chi^2(\operatorname{Ric}_g+g),\qquad g(0)=g_0 .
> \]

该结果不提供塌缩族统一的初始寿命，也没有完成 restricted Ishida–LeBrun 定理。Step 56 §6 提出的“逐数据起动 + uniform first exit + 正时间延拓”是正确接口，但其中 first-exit 和 collar continuation 仍是未完成的负载模块。

A01 Step45 §7.2 的 Liouville 不变性补丁确实消除了塌缩下指数映射多重覆盖造成的上界常数问题。

---

## 1. Tame 引理修复了 Step 55 的明确错误

Step 55 声称某些高阶系数导数由固定低阶 \(E_s\) 控制，这是错误的。Step 56 改为：在
\[
H^{s_0}\hookrightarrow W^{4,\infty},\qquad s_0>\frac n2+4
\]
的低阶控制下，若
\[
q_i\le m,\qquad \sum_iq_i\le m+2,
\]
且已单独取出 \(D^{m+1}G,D^{m+1}\beta\) 型最高项，则
\[
\left\|\prod_iD^{q_i}u_i\right\|_2
\le C_{m,R}\left(1+\sum_i\|u_i\|_{H^m}\right).
\]

其插值计数是正确的。对 \(q_i>4\)，可取
\[
\theta_i=\frac{q_i-4}{m-4},\qquad \frac1{p_i}=\frac{\theta_i}{2}.
\]
若只有一个高阶因子，则 \(\theta_i\le1\)；若至少两个，则
\[
\sum_i\theta_i
\le\frac{m+2-8}{m-4}
=\frac{m-6}{m-4}<1.
\]
其余至多四阶因子放入 \(L^\infty\)。因此高阶 \(H^m\) 范数只以总次数不超过一出现。对 \(G^{-1}\) 的 Faà di Bruno 展开也服从相同预算。

这足以验证两个关键后果：

\[
\sum_{j=2}^m\|D^jA*D^{m-j+2}G\|_2
\le C_{m,R}(1+\|G\|_{H^m}+\|\beta\|_{H^m}),
\]
以及
\[
\|D^{m+1}(\beta^2)-2\beta D^{m+1}\beta\|_2
\le C_{m,R}\|\beta\|_{H^m}.
\]

因此，Step 56 不再把高系数导数伪装成低阶常数，而是将其线性保留在当前 \(H^m\) 能量中；这确实修复了 Step 55 §5 的核心漏洞。

尚需正式写出的只是完整张量版 tame 引理：包括光滑复合、背景协变导数交换子和系统内全部有限乘积的逐项归类。现有计数没有显示新的导数损失。

---

## 2. 双正则化系统没有 \(\varepsilon^{-1}\) 或 \(\nu^{-1}\) 损失

固定 \(\varepsilon,\nu>0\) 时，系统主符号为
\[
\operatorname{diag}\!\left(
(\beta^2+\varepsilon)G^{ab}\xi_a\xi_b\,\mathrm{Id}_{S^2},
\ \nu\bar g^{ab}\xi_a\xi_b
\right),
\]
故为强抛物系统。最大值原理正确给出
\[
0\le\beta\le1.
\]

所有关键吸收只使用
\[
\frac{\beta^2}{\beta^2+\varepsilon}\le1,
\qquad
\frac{\beta^4}{\beta^2+\varepsilon}\le1,
\]
以及
\[
D\!\left((\beta^2+\varepsilon)G^{-1}\right)
=2\beta D\beta\,G^{-1}
 +(\beta^2+\varepsilon)D(G^{-1}).
\]

因此：

- 主项第一次系数微分可由加权 Young 吸收；
- \(j\ge2\) 的系数微分由 tame 引理处理；
- \(Q\) 项中的 \(D^{m+1}G\) 带完整 \(\beta^2+\varepsilon\) 权重；
- Lie 项中 \(D^{m+1}\beta\) 经一次分部积分转成带 \(\beta D^{m+1}G\) 的可吸收项；
- 输运的顶阶耦合带 \(\beta^2D^{m+1}G\)；
- 标量扩散交换子乘有 \(\nu\le1\)，不需除以 \(\nu\)。

所以
\[
\mathcal E_m'
+c\mathcal D_m^G+c\mathcal D_m^\beta
\le C_{m,R}(1+\mathcal E_m)
\]
可具有独立于 \((\varepsilon,\nu)\) 的常数。

在 \(m=s_0\) 阶应以 stopping-time bootstrap 理解：同时控制度量正定性和低阶 Sobolev 球；随后所有 \(m>s_0\) 的系数只依赖该低阶球，故 Grönwall 在同一个逐数据区间 \([0,T_0]\) 上闭合。这正是 tame 层级相对于 Step 55 的决定性改进。

仍需补齐固定 \((\varepsilon,\nu)\) 的严格存在构造。直接引用强抛物理论是可行的；若采用谱截断，则应说明：

1. 截断如何保持度量正定性；
2. 最大值原理是在固定参数 PDE 极限后使用，而不是对一般谱投影近似直接使用；
3. 截断与能量配对、背景导数交换子的兼容性。

---

## 3. 光滑极限及拉回给出逐数据精确流

全阶空间界和
\[
\|\partial_tG\|_{H^{m-2}}
+\|\partial_t\beta\|_{H^{m-2}}\le C_m
\]
给出逐阶强紧性。反复时间微分只引入更高空间导数以及非负次幂的 \(\varepsilon,\nu\)，不引入倒数。因此可取
\[
(\varepsilon_j,\nu_j)\to(0,0)
\]
使 \((G_j,\beta_j)\) 在所有固定时空 \(C^k\) 中收敛，并且
\[
\varepsilon_jG_j^{-1}D^2G_j\to0,\qquad
\nu_j\bar\Delta\beta_j\to0.
\]
极限满足未正则化 transported-cutoff 系统。

令
\[
X=-\beta^2W(G),\qquad \partial_t\varphi=X\circ\varphi.
\]
则
\[
\frac d{dt}\beta(t,\varphi(t,x))
=\partial_t\beta+D\beta(X)=0,
\]
所以
\[
\beta(t,\varphi(t,x))=\chi(x).
\]
又
\[
\partial_tG
=-2\beta^2(\operatorname{Ric}_G+G)
+\mathcal L_{\beta^2W}G,
\]
故
\[
\partial_t(\varphi^*G)
=\varphi^*(\partial_tG+\mathcal L_XG)
=-2\chi^2\bigl(\operatorname{Ric}_{\varphi^*G}+\varphi^*G\bigr).
\]

因此逐数据存在性成立。Step 56 正确地不再声称任意几何解之间的唯一性；规范解唯一性不能自动推出退化几何方程的唯一性，而 IL 应用目前只需要一个可重启的光滑分支。

Step 55 的 Python/JSON 检查不能作为该结论的证据：大多数条件被硬编码为 `True`，且其中一般张量系数的所谓“反对称积分恒等式”并不成立。正文改用加权 Young 才是正确处理。

---

## 4. 修正后的 first-exit 接口是相容的

### 4.1 \(H_2\) 必须不带 \(a\) 权重

由
\[
H_q^\alpha=\int\eta_\alpha^2a^{q-2}F_T^q
\]
直接得到
\[
H_2^\alpha=\int\eta_\alpha^2F_T^2.
\]
这使曲率控制覆盖整个 \(\eta_\alpha\) 缓冲区，包括 \(a\) 很小的 collar；额外插入 \(a\) 会丢失 Sobolev 吸收所需的非加权曲率信息。该修正是必要且正确的。

### 4.2 全局 \(Q\) 必须包含静止余项

若 \(\eta_\alpha\) 外支撑互不相交，且在每个 active support 的邻域内 \(\eta_\alpha=1\)，则
\[
\rho=\sum_\alpha\eta_\alpha^2,\qquad
\operatorname{supp}(1-\rho)\subset\{a=0\}.
\]
在该区域精确流静止，故 \(E\) 与体积元均不变：
\[
Q_{\rm rest}(t)=Q_{\rm rest}(0).
\]
于是
\[
Q_{\rm global}(t)
=Q_{\rm rest}(0)+\sum_\alpha Q_\alpha(t)
\]
是正确恒等式；选取的支撑不必覆盖整个流形。

### 4.3 逐数据起动与统一观测时间

Step 56 正确撤回了 Step 55 Appendix 中“曲率—体积预算给出统一 \(H^s\) 寿命”的错误断言。正确逻辑应为：

1. 每个 datum 先获得一个可能很短的精确流；
2. 在任意已有光滑区间内运行只依赖统一低阶输入的 first-exit 估计；
3. 若最大分支提前终止，则在正时间 terminal slab 上使用 staggered continuation 得到光滑终点；
4. 逐数据重启，从而排除在 \(\theta r^2\) 前终止。

这在逻辑上不循环：first-exit 常数是序列统一的，而重启所需高阶界只需逐数据有限。

但目前还不能把“每个 datum 都到达 \(\theta r^2\)”视为已证明，因为仍缺两项解析内容：

- 必须完整推导 \(H_2,Y,J_6,Q\)、Moser endpoint 和 drift 不等式，并确保常数不依赖未统一控制的 \(\nabla^2\chi\)。特别是
  \[
  \nabla^2a=2\,d\chi\otimes d\chi+2\chi\nabla^2\chi
  \]
  中的 \(\chi\nabla^2\chi\) 必须逐项分部积分，降至一阶 cutoff 数据；仅引用“signed Hessian contraction”不够。
- \(\|aF_T\|_\infty\) 不能直接控制 \(a\to0\) collar 上的不带权曲率。必须证明 Step45 §5.3 的
  \[
  T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to\cdots
  \]
  层级确实给出 terminal slab 上的非加权曲率、固定坐标高阶导数和光滑终点。这是正时间 continuation 的实际负载。

---

## 5. Liouville 补丁确实消除了指数映射重数问题

A01 Step45 §7.2 的上界不再通过把切空间球积分推到基流形，而是写成单位切丛上的测地流积分。由 Rauch Jacobian 界，
\[
A_\rho\Phi(p)
\le C\rho^{-4}\int_0^\rho t^3
 \int_{S_pM}\Phi(\pi\varphi_t(p,\xi))\,d\xi\,dt.
\]
对 \(p\in P^{\rm in}\) 积分后，
\[
\int_{SM|_{P^{\rm in}}}\Phi(\pi\varphi_t(v))\,d\Lambda(v)
\le\int_{SM}\Phi(\pi\varphi_t(v))\,d\Lambda(v).
\]
测地流 \(\varphi_t\) 是保 Liouville 测度的微分同胚，因此
\[
\int_{SM}\Phi(\pi\varphi_t(v))\,d\Lambda(v)
=\int_{SM}\Phi(\pi v)\,d\Lambda(v)
=\omega_3\int_M\Phi\,d\mu.
\]
这里每个初始单位向量只计算一次；完全不需要 \(\exp_p\) 单射或具有统一重数。因此塌缩产生的短环路不会引入发散的 multiplicity 常数。

下界方向仍可在切空间拉回度量 \(\exp_p^*g\) 上进行：选择 \(\rho\) 小于曲率控制给出的共轭尺度，并保证所有长度 \(\le\rho\) 的测地线留在 bounded-curvature plateau 中，则拉回球光滑且由 Jacobian 下界非塌缩。这个“拉回球解开塌缩”的下界与 Liouville 上界完全相容。

---

## 6. restricted IL 定理完成前的具体剩余工作

1. 完整张量版 tame 引理及 Step 56 系统内全部交换子的逐项核对。
2. 固定 \((\varepsilon,\nu)\) 强抛物存在、延拓及近似方案的严格书写。
3. 序列统一的 \(H_2,Y,J_6,Q\)、Moser endpoint 和 metric-drift 推导，尤其消除 \(\chi\nabla^2\chi\) 对高 cutoff jets 的依赖。
4. 从正时间 weighted curvature 控制到 collar 非加权高阶控制和光滑重启的 staggered continuation 定理。
5. 终端参数的一致选择：plateau buffer、\(\rho\)、共轭尺度、Rauch Jacobian 界及拉回球体积下界。
6. 独立核对 topological/local core：Seiberg–Witten 平均不等式、\(\Phi\) 的 \(119Q\) 常数、Derdziński 输入，以及 Proposition 3.2 的 harmonic-radius/椭圆升级。
7. 统一最终使用的支撑半径和分离约定，避免 Step45 与 Step55 中 \(5r/6r/7r\)、\(12r/14r\) 两套记号混用。

综上，Step 56 已将逐数据 direct transported-cutoff flow 提升为可信且可严格补全的解析模块；Liouville averaging 的重数漏洞也已修复。尚未闭合的是 first-exit 与正时间 continuation 的完整证明，以及 restricted IL 链的拓扑和局部紧性核验。这些结论仅涉及四维负号 Ishida–LeBrun 路线，不构成 Yau 第26题的全局解答。
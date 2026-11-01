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
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step28_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step28_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 28 consolidation of the restricted four-dimensional negative LeBrun/Ishida-LeBrun route. Read the A01 terminal recalibration/pullback note, the patched A01 weak-Moser note, A03's general-p note, A03's shifted-curvature continuation theorem and Codex report/artifact, plus the Step 16 pullback and Step 8 Derdzinski/gap notes. Please check three scientific points: (1) whether the corrected Moser recurrence (using A03 Sections 5.2-5.3, fixed J6 from time zero, polynomial p-dependence inside the time-cutoff recurrence) avoids the exponent/Gronwall errors; (2) whether the shifted curvature U=a(Rm+G) continuation proof really removes the normalization/cutoff-jet obstacle at the schematic proof level; (3) whether terminal recalibration plus exponential-pullback selection legitimately bypasses plateau noncollapse and Euler-density localization, assuming the analytic selected-support theorem produces a positive-volume bounded-curvature plateau set and Q(T)/A -> 0. Identify any remaining logical gaps or corrections without lowering the all-dimensional Yau-26 goal.

## Integrated Scientific Memo

# Step 28 科学核验结论

## 总结

三项整合在其声明的层级上基本成立：

1. **修正后的 Moser 递推确实避开了旧的指数与逐层 Grönwall 错误。**
2. **移位曲率**
   \[
   U=a(\operatorname{Rm}+G),\qquad G=\frac{g\owedge g}{2(n-1)}
   \]
   **在示意证明层面消除了归一化项造成的 cutoff-jet 障碍，并恢复 Wang 型三角归纳。**
3. **终端重新校准加指数映射拉回选择，确实可以绕过基流形非塌缩和 Euler 密度定位。**但所需假设必须是定量的：
   \[
   \operatorname{Vol}(P_i)\ge \alpha A_i
   \]
   且 \(\alpha,\rho,K\) 与序列无关；“仅有正体积”并不够。

因此 Step 28 的**下游逻辑**是有效的，但受制于尚未证明的 selected-support 定理、全局 \(Q\)-传播以及若干仍为示意层级的张量能量计算。

---

## 1. Moser 递推

### 1.1 指数账本正确

令
\[
p_{k+1}=\kappa p_k,\qquad \kappa=\frac32
\]
（四维抛物 Sobolev 指数）。则
\[
\sum_{k\ge0}\frac1{p_k}
=\frac{1}{p_0}\frac{\kappa}{\kappa-1}
=\frac3{p_0}
=\frac{n+2}{2p_0},
\]
但每一步 Sobolev 因子是
\[
S^{1/(\kappa p_k)},
\]
故总 Sobolev 次数为
\[
\frac1\kappa\sum_{k\ge0}\frac1{p_k}
=\frac2{p_0}
=\frac{n}{2p_0},
\]
而不是 \((n+2)/(2p_0)\)。脚本对此的核验正确。

底层空间插值也恰好匹配权重：
\[
K_p=\int \eta^2a^{p-2}\Phi^p,\qquad
Z_p=\eta a^{(p-1)/2}\Phi^{p/2},
\]
并且在 active region（其中 \(\eta=1\)）上
\[
K_{2p}=\int Z_p^4,
\]
以及
\[
K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2},
\]
因为插值得到的 \(a\)-次数为
\[
\frac{p-2}{2}+\frac{2p-2}{2}
=\frac{3p}{2}-2.
\]
因此在 \(a=0\) 附近没有遗留负权重。

### 1.2 不再逐指数使用 Grönwall

在时间片 \([t/2,t]\) 上，
\[
S^2Y(s)\le \frac{C\beta^3}{s}
\le \frac{2C\beta^3}{t}.
\]
三因子吸收后得到
\[
K_p'+c\|\nabla Z_p\|_2^2
\le Cp^N\left(r^{-2}+\frac{\beta^3}{t}\right)K_p .
\]
这里必须直接乘时间 cutoff 并积分，产生
\[
L_k=Cp_k^N4^k(t^{-1}+r^{-2}),
\]
而不能先对每个 \(p_k\) 使用 Grönwall。递推为
\[
m_{k+1}
\le (CS)^{1/(\kappa p_k)}L_k^{1/p_k}m_k .
\]
因为
\[
\sum_k\frac{\log L_k}{p_k}<\infty,
\]
任意固定的多项式 \(p^N\) 都是无害的。

相反，若逐层 Grönwall，则会出现近似 \(\exp(Cp_k^N)\)，其在取 \(1/p_k\) 次方后仍给出 \(\exp(Cp_k^{N-1})\)，无法形成收敛乘积。修正后的机制确实排除了这一旧错误。

这里把 \(\beta^3/t\) 吸收到 \(t^{-1}\) 中还使用了固定临界小量
\(\beta\le\beta_*\ll1\)，正式表述中应显式写出。

### 1.3 端点输出与塌缩体积消去

曲率情形 \(p_0=3\)：
\[
\int_{t/2}^tY(s)\,ds\le C\beta^3S^{-2},
\]
故
\[
\|aF(t)\|_\infty
\le CS^{2/3}t^{-1}
  (\beta^3S^{-2})^{1/3}
=\frac{C\beta}{t}.
\]

缺陷情形 \(p_0=6\)：
\[
\int_{t/2}^tJ_6(s)\,ds\le C\delta^6Vt.
\]
于是
\[
\|aE(t)\|_\infty
\le CS^{1/3}t^{-1/2}(\delta^6Vt)^{1/6}.
\]
代入
\[
S=Cr^2V^{-1/2}
\]
可得
\[
S^{1/3}V^{1/6}=Cr^{2/3},
\]
从而
\[
\boxed{\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3}.}
\]
因此修正后的 Sobolev 次数正是塌缩体积消去所必需的次数。

### 1.4 \(J_6\) 从 \(t=0\) 固定指数传播

正确的起点是固定 \(p=6\) 的临界吸收：
\[
J_6'+c\|\nabla Z_6\|_2^2
\le Cr^{-2}J_6+C\int a^5F|E|^6 .
\]
而
\[
\int a^5F|E|^6
\le \|F\|_{L^2(\operatorname{supp}\chi)}
   \|Z_6\|_4^2
\le \bar\beta\bigl(\|\nabla Z_6\|_2^2+r^{-2}J_6\bigr).
\]
固定的小量阈值吸收后：
\[
J_6(t)\le e^{Ct/r^2}J_6(0).
\]
这避免了从 \(0\) 积分 \(Y(t)\sim t^{-1}\) 的不可积系数，修复是有效的。

### 1.5 仍缺失的严格内容

Moser **递推本身已经正确**，但它尚依赖：

- 完整的、统一于所有 \(p\ge3\) 的张量能量不等式
  \[
  K_p'+c\|\nabla Z_p\|_2^2
  \le Cp^Nr^{-2}K_p
  +Cp^N\int a^{p-1}F\Phi^p,
  \]
  其中 \(c>0\) 与 \(p\) 无关，\(N<\infty\) 固定；
- 对正则化 \(\Phi=(|E|^2+\varepsilon^2)^{1/2}\) 的 Hessian-cutoff 缩并、Kato 极限和 moving-norm/volume 项的完整指标证明；
- 非整数 \(p_k\) 时 \(a^{p-2}\) 的统一光滑逼近或无限平坦 cutoff 方案；
- \(q=2\to q=3\) 势估计
  \[
  S^2Y(t)\le C\beta^3/t
  \]
  的无循环闭合证明；
- active \(H_2\)、固定 \(J_6\) 与 global \(Q\) 在同一多支撑流中的同步传播。

---

## 2. 移位曲率 continuation

### 2.1 归一化项被精确吸收

在给定约定下，
\[
G=\frac{g\owedge g}{2(n-1)},\qquad \operatorname{Ric}(G)=g.
\]
令
\[
T=\operatorname{Rm}+G,\qquad U=aT.
\]
则有精确恒等式
\[
\operatorname{Ric}(T)=\operatorname{Ric}+g=E,
\qquad
\operatorname{Ric}(U)=aE,
\]
从而
\[
\boxed{\partial_tg=-2\operatorname{Ric}(U).}
\]

这不是把 \(-2ag\) 粗略称为“低阶项”，而是把完整速度写成 \(U\) 的 Ricci 缩并。因此
\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)
\]
恢复了 Wang 的 cutoff-derivative 三角结构。

移位演化为
\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T).
\]
特别地，没有独立的
\[
\nabla^2a*G
\]
源项。这个消失也由一致性强制：当 \(T=0\) 时，\(\operatorname{Ric}=-g\)，流对任意固定 cutoff 都静止，因此右端每项必须在 \(T=0\) 时消失。

### 2.2 \(U=aT\) 避免在 \(a=0\) 除法

\(U\) 满足示意方程
\[
(\partial_t-a\Delta)U
=da*\nabla U+\nabla^2a*U+d\chi*d\chi*U
 +U*U+aG*U.
\]
唯一需要的退化商为
\[
\frac{|da|^2}{a}=4|d\chi|^2,
\]
它在 \(\{a=0\}\) 上连续延拓。因此证明不引入 \(a^{-1}\) 奇性。

### 2.3 cutoff-jet 三角结构

原始高阶项确实包括
\[
\chi\nabla^{m+2}\chi*U,\quad
\nabla\chi*\nabla^{m+1}\chi*U,\quad
\chi\nabla^{m+1}\chi*\nabla U,\quad
\chi\nabla\chi*\nabla^{m+1}U.
\]
它们不能被简单称为低阶项。

Wang 型分组分部积分的预期结果是：

- \(\nabla^{m+1}U\) 项保留 \(\chi\)，由
  \[
  \int \chi^2|\nabla^{m+1}U|^2|\nabla^mU|^{p-2}
  \]
  吸收；
- 表面的 \(\nabla^{m+2}\chi\) 输入降阶；
- 唯一残余的最高 cutoff 乘积为
  \[
  \nabla^2\chi*\nabla^m\chi*U*
  \nabla^mU|\nabla^mU|^{p-2}.
  \]

由此归纳次序为
\[
\nabla^{m-1}U
\longrightarrow \nabla^m\chi
\longrightarrow \nabla^{m-1}T
\longrightarrow \nabla^mU.
\]
新出现的 \(G\)-项若含当前 \(\nabla^mU\)，只是有界线性系数；否则只含已控制低阶量，不增加反向依赖。

基准无权 \(L^p\) 估计也合理：
\[
\frac d{dt}\int|T|^p
+c_p\int a|\nabla T|^2|T|^{p-2}
\le C_p\int|T|^p.
\]
其中 \(\nabla^2a\) 项经一次分部积分后使用
\[
|da|^2/a=4|d\chi|^2
\]
控制，不要求先验高阶 cutoff jet。

因此，在**示意证明和 Wang 源机制迁移层面**，归一化及 cutoff-jet 障碍已经解除。

### 2.4 DeTurck 公式的必要修正

A03 简略笔记中的
\(\mathcal L_V\widehat g\) 写法不够准确。与详细 artifact 一致的系统应为
\[
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}(\widehat g)+\widehat g)
+\mathcal L_{\widehat aW}\widehat g,
\]
并配合
\[
\partial_t\phi\circ\phi^{-1}=-\widehat aW,\qquad
\phi^*\widehat a=a.
\]
只有把 \(\widehat a\) 同时放在归一化速度和 gauge 向量中，拉回后才恢复固定空间 cutoff 的原方程。

### 2.5 尚需补足

continuation 的核心剩余严格性是：

1. 详细重写 Wang Proposition 4.14 的分组分部积分，至少完整核验 \(m=2\)，确认没有任何 \(\nabla^{m+1}\chi\) 遗留；
2. 明确给出 staggered Hölder 指数族，而非仅称“与 Wang 相同”；
3. 对照 Yang 的退化 DeTurck 构造，核验新增
   \(-2\widehat a\widehat g\) 不仅不改变主符号，也不破坏其正则化极限估计和唯一性；
4. 保持“逐个流形的 continuation 常数”与 selected-support 中需要的序列统一常数严格分离。

这些不否定当前示意 continuation 定理，但阻止把它称为完全独立的逐指标证明。

---

## 3. 终端重新校准与指数拉回

### 3.1 终端常数正确

四维中
\[
\mathcal E=\operatorname{Ric}+g
=\operatorname{Ric}^{\circ}+\frac{s+4}{4}g,
\]
故
\[
|\mathcal E|^2
=|\operatorname{Ric}^{\circ}|^2+\frac{(s+4)^2}{4}.
\]
于是
\[
\int(s+4)^2\le4Q(T),\qquad
J\le \frac{Q(T)}{8\pi^2}.
\]
选定 monopole 符号后
\[
0\le D_a\le J.
\]
Step 8 的平方补全和 gap 给出
\[
\int(s+8\sqrt6|W^+|)^2\le108Q(T),
\qquad
\int\mathcal G\le6Q(T).
\]
因此
\[
\boxed{\int\mathfrak D\le119Q(T).}
\]
脚本中的 \(108,6,119\) 均正确。将 \((s+4)^2\) 单独加入会部分重复 \(|\mathcal E|^2\) 中已有项，但只会扩大非负密度，无逻辑问题。

关键点也正确：这些校准关系是在终端闭度量上从拓扑和 SW/CGB 恒等式**重新生成**，而不是借助初末曲率的 \(C^0\) 传输。

### 3.2 拉回平均确实不需要基空间 injectivity radius

若从每个 \(p\in P_i\) 出发、长度不超过 \(\rho\) 的径向测地线均位于满足
\[
|\sec|\le K,\qquad K\rho^2<\pi^2/4
\]
的 buffer 中，则 Rauch 给出
\[
s_K(t)^3\le J_p(t,\xi)\le s_{-K}(t)^3.
\]
Liouville 不变性于是给出
\[
\int_{P_i}A_\rho D(p)\,d\mu(p)
\le C(4,K,\rho)\int_{M_i}D\,d\mu.
\]
若
\[
\operatorname{Vol}(P_i)\ge\alpha A_i,\qquad
\int\mathfrak D_i=o(A_i),
\]
则存在 \(p_i\in P_i\) 使
\[
A_\rho\mathfrak D_i(p_i)\to0.
\]

这里多重覆盖无害，因为积分发生在切空间径向参数中，且密度非负。完全不需要基流形的 injectivity radius、F-structure 或 Euler 密度定位。

但必须强调：

\[
\boxed{\text{“正体积”不够；需要固定 }\alpha>0
\text{ 使 }\operatorname{Vol}(P_i)\ge\alpha A_i.}
\]

同样，\(\rho,K\) 也必须是序列统一常数，且所有径向线必须留在受控 buffer 中。

### 3.3 拉回域上的非塌缩与极限

对
\[
\widehat g_i=(\exp_{p_i})^*g_i(T)
\]
而言，在无共轭半径内切空间点不作识别，且
\[
J_i(t,\xi)\ge s_K(t)^3.
\]
因此原点附近较小球有统一正体积下界，同时曲率有统一界。

从原点的体积下界到整个较小球上的统一 harmonic radius，正式证明应补一层标准论证：先由曲率和中心球体积得到中心 injectivity/harmonic-radius 下界，再缩小到 \(B_{\rho'}(0)\) 并传播该下界。Step 28 当前一句带过了这个 center-to-neighborhood 步骤。

另外，所选拉回积分只直接给出 \(E_i\to0\) 于 \(L^2\)。但曲率有统一 \(L^\infty\) 界，因此 \(E_i\) 也有统一 \(L^\infty\) 界；插值可得任意有限 \(L^p\) 的强收敛。结合 harmonic-coordinate 方程，足以得到较小球上的强有限 \(W^{2,p}\) 收敛，并将各非负 gap 密度传到光滑 Einstein 极限。

极限满足
\[
\operatorname{Ric}=-g,\qquad s=-4,\qquad
s+8\sqrt6|W^+|=0,\qquad \mathcal G=0.
\]
所以
\[
|W^+|^2=\frac1{24},
\qquad
\operatorname{spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Derdziński 因子为
\[
(24|W^+|^2)^{1/3}=1,
\]
故极限度量本身局部 Kähler。另一方面四维 Kähler–Einstein 度量满足
\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
与 \(1/24\) 矛盾。下游 Derdziński 矛盾成立。

---

## 4. 精确剩余缺口

Step 28 尚未闭合的核心数学对象是：

1. **selected-support 流定理**：同时产生序列统一的
   \[
   \operatorname{Vol}(P_i)\ge\alpha A_i,\qquad
   \rho>0,\qquad K<\infty,
   \]
   并保证从每个中心出发的长度-\(\rho\) 径向测地线留在终端有界曲率 buffer 中；
2. **统一能量包**：在同一个多支撑 cutoff 流中证明
   \[
   S^2Y(t)\le C\beta^3/t,\quad
   J_6(t)\le e^{Ct/r^2}J_6(0),\quad
   Q_i(T)\le e^{C\theta}Q_i(0),
   \]
   以及 active \(H_2\) 传播，并明确消除 \(q=2\to q=3\) 的潜在循环；
3. **general-\(p\) 完整指标证明**，包括 regularized defect、非整数权重和统一多项式 \(p\)-依赖；
4. **Wang 分组分部积分及 Yang 退化 restart 的独立展开**。

在这些条件下，终端重新校准和指数拉回确实完全取代 plateau 基空间非塌缩与 Euler-density localization；目前真正未解决的不是下游选择，而是产生定量 plateau family 的上游分析定理。

即使上述缺口全部补齐，所得结论仍只排除受限的四维负归一化 LeBrun/Ishida–LeBrun 临界实验族；它尚不处理任意四维拓扑、正分支、\(n\ge5\)、维数唯一常数的完整量词，也不提供全 Yau-26 命题所要求的 Lean 4 形式化。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 10,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step10_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step10_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Given the Step 10 pivot, propose concrete Execute-level mathematical attacks on the true pinched regularity bottleneck for Yau Problem 26. The goal is not final writing but actionable research: how to refute or salvage a Cheeger--Tian-style pointwise epsilon-regularity theorem under only ||Ric-g||_{L∞}≤δ; how to use high-frequency transverse-traceless/Weyl packet perturbations as counterexample probes; how to extract a weaker Li/Cheeger--Tian scale-selection or smoothing theorem; and how to connect any surviving regularity to the simply-connected volume gap and the A01/A03 accessible-cover bridge. Give a prioritized set of candidate lemmas/probes with assumptions, expected calculations, failure modes, and what evidence would change the route.

## Integrated Scientific Memo

# Execute-level memo：\(C^0\)-Ricci 夹逼下真正可攻的正则性瓶颈

核心判断是：

\[
\|\operatorname{Ric}_g-g\|_{L^\infty}\le \delta
\]

本身不提供 Einstein 型曲率方程，因而不能直接从小 \(L^2\) 曲率推出原度量的点态曲率控制。现有来源严格支持的替代物只有：

1. Li/Cheeger–Tian 的**可比尺度选择**；
2. Li 的**小局部能量下 Ricci-flow 平滑**；
3. Naber–Zhang 在特定塌缩模型与最大幂零秩下给出的**局部覆盖调和半径**；
4. 在覆盖调和图中得到的**光滑 Einstein 极限 germ**；
5. 只把 Ricci 缺陷与光滑测试场配对的**投影/通量恒等式**。

下面按优先级给出可直接执行的数学攻击。

---

## I. 首先精确判定强点态 \(\varepsilon\)-正则性是否为假

### 候选强命题 \(CT_{C^0}\)

检验是否存在普适 \(\varepsilon,C,\delta_0>0\)，使四维度量满足

\[
\|\operatorname{Ric}_g-g\|_{L^\infty(B_r)}\le\delta_0,\qquad
\int_{B_r}|\operatorname{Rm}|^2\le\varepsilon
\]

便推出

\[
\sup_{B_{r/2}}|\operatorname{Rm}|\le Cr^{-2}.
\]

现有来源没有支持这个命题。Naber–Zhang Proposition 6.5 明确表明：即使已有覆盖调和半径，曲率上界仍需 \(|\nabla\operatorname{Ric}|\) 上界或 Einstein 条件。

### Probe 1A：先排除朴素单频 TT 包

在 Einstein 背景 \(g_0\) 上令

\[
h=a\,e^{ikx\cdot\xi}q .
\]

欧氏主符号为

\[
2D\operatorname{Ric}_\xi(q)_{ij}
=
|\xi|^2q_{ij}+\xi_i\xi_j\operatorname{tr}q
-\xi_i\xi^a q_{aj}-\xi_j\xi^a q_{ai}.
\]

若 \(q\) 关于 \(\xi\) 横截且无迹，则

\[
D\operatorname{Ric}(h)\sim ak^2q,\qquad
DW(h)\sim ak^2q.
\]

故控制 Ricci 缺陷迫使 Weyl 主振幅同阶受控。若落在 Ricci 主符号核，则该符号是纯规范方向 \(\xi\odot v\)，Weyl 主符号也消失。

**结论。** 单一 WKB/TT 高频波不是反例；真正反例若存在，必须利用：

- \(L^\infty\to\mathrm{BMO}\) 型 Calderón–Zygmund 现象；
- 多频/非局部椭圆消去；
- 塌缩；
- 或精确非线性结构。

这是最低成本且应先正式写成引理的负结果。

---

## II. 最有希望的反例机制：显式 \(T^2\) 扭曲模型

比尚未闭合的“DeTurck 张量尖峰”更应优先，因为这里 Ricci 对迹自由 Hessian 的消去是精确的。

在 \(D^2\times T^2_\ell\) 上取

\[
g_u=dx^2+dy^2+e^{2u(x,y)}d\theta^2+e^{-2u(x,y)}d\phi^2 .
\]

在正交标架中直接计算得到

\[
\operatorname{Ric}_{ab}=-2u_au_b,\qquad
\operatorname{Ric}_{33}=-\Delta u,\qquad
\operatorname{Ric}_{44}=+\Delta u,
\]

而曲率含有

\[
R_{a3b3}=-u_{ab}-u_au_b,\qquad
R_{a4b4}=+u_{ab}-u_au_b .
\]

因此存在维数常数 \(c,C>0\) 使

\[
|W|
\ge c|(\nabla^2u)^\circ|
-C\bigl(|\Delta u|+|\nabla u|^2\bigr).
\tag{2.1}
\]

### Probe 2A：构造标量 CZ 尖峰

目标是构造光滑 \(u_j\)，满足

\[
\|\nabla u_j\|_\infty+\|\Delta u_j\|_\infty\to0,
\]

但在某点 \(p_j\)

\[
|(\nabla^2u_j)^\circ(p_j)|\to\infty,
\]

同时

\[
\|\nabla^2u_j\|_{L^2(D^2)}\to0
\quad\text{或至少一致有界。}
\]

这正是二维 Poisson 方程中有界右端不控制 Hessian \(L^\infty\) 的具体化。需要给出显式光滑右端 \(f_j=\Delta u_j\)，而不是只引用抽象 CZ 原理。

由精确 Ricci 公式，

\[
\|\operatorname{Ric}_{g_{u_j}}\|_\infty
\le C\bigl(\|\Delta u_j\|_\infty+\|\nabla u_j\|_\infty^2\bigr)\to0,
\]

而由 (2.1)

\[
|W(g_{u_j})(p_j)|\to\infty.
\]

纤维面积为 \(O(\ell^2)\)，故

\[
\int_{D^2\times T^2_\ell}|\operatorname{Rm}|^2
\lesssim
\ell^2\int_{D^2}
\bigl(|\nabla^2u|^2+|\nabla u|^4\bigr).
\tag{2.2}
\]

固定 \(u_j\) 后再缩小 \(\ell_j\)，可令绝对 \(L^2\) 能量任意小而不改变点态 Weyl 尖峰。

### Probe 2B：将 Ricci-flat 模型移植到 \(\operatorname{Ric}\approx g\)

在正 Einstein 背景的小测地球内植入上述结构。需逐项验证：

\[
\operatorname{Ric}_{g_j}-g_j
=
\text{平坦模型缺陷}
+
O(|u_j|+r_j|\nabla u_j|)
+
\text{截断误差}.
\]

选择尖峰尺度 \(s_j\ll r_j\)，并要求

\[
\|u_j\|_{C^1}\to0,\qquad
s_j/r_j\to0,
\]

以压低背景曲率和截断项。

**成功标准。** 获得闭流形上的度量 \(g_j\)：

\[
\|\operatorname{Ric}_{g_j}-g_j\|_\infty\to0,\qquad
\int_{B_{r_j}}|\operatorname{Rm}|^2\to0,
\]

但

\[
r_j^2\sup_{B_{r_j/2}}|\operatorname{Rm}|\to\infty.
\]

这将严格否定 \(CT_{C^0}\)。

**主要失败模式。**

- 截断产生 \(r_j^{-2}u_j\) 级 Ricci 缺陷；
- 正 Einstein 零阶项破坏精确消去；
- 所构造的 Hessian 尖峰在 \(L^2\) 中代价过大；
- 小纤维只降低绝对能量，却测试不到命题所需的正确球尺度。

---

## III. DeTurck–CZ 张量方案：有价值，但当前不能视为完成构造

在 Bianchi 规范下定义

\[
\Phi_{g_0}(g)
=
\operatorname{Ric}_g-g+\delta_g^*\beta_{g_0}(g),
\]

其线性化 \(L=D\Phi_{g_0}\) 椭圆。理想构造是找 \(h_j\) 满足

\[
\|Lh_j\|_\infty\le1,\qquad
\|h_j\|_{C^1}\le C,\qquad
\|\nabla^2h_j\|_{L^2}\le C,
\]

同时某个 Weyl-active Hessian 分量在 \(p_j\) 趋于无穷。

令 \(g_j=g_0+a_jh_j\)，则形式上

\[
\Phi_{g_0}(g_j)
=
a_jLh_j
+
O\!\left(a_j^2|\nabla^2h_j|+a_j^2|\nabla h_j|^2\right).
\]

若 Hessian 峰值为 \(H_j\)，选择

\[
a_jH_j\to\infty,\qquad
a_j^2H_j\to0
\]

便可能同时得到 Weyl 爆破和小非线性缺陷。

但必须补齐两个关键缺口：

1. **规范缺陷不是 Ricci 缺陷。**  
   从 \(\Phi_{g_0}(g_j)\) 小不能自动推出
   \(\operatorname{Ric}_{g_j}-g_j\) 小；必须证明
   \(\delta_{g_j}^*\beta_{g_0}(g_j)\) 同样小，或通过真实微分同胚/规范求解消去它。

2. **Bianchi 投影可能消灭尖峰。**  
   必须证明张量 CZ 构造在投影后仍保留非纯规范的 Weyl-active 二阶分量。

因此此路线的第一个可检验引理应是：

> 是否存在紧支撑、Bianchi 规范的对称张量 \(h_j\)，使 \(Lh_j\) 一致 \(L^\infty\) 有界、\(\nabla^2h_j\) 的 Weyl 投影点态无界且 \(L^2\) 有界？

若否，其失败所揭示的隐藏椭圆复形估计本身将是新的正则性信息。

---

## IV. 立即可用的真替代定理：Li 尺度选择与平滑

来源已给出明确版本。经缩放后可使用：

### Lemma L：可比尺度选择

对每个 \(\varepsilon>0\)，存在

\[
\delta_L(\varepsilon)>0,\qquad a_L(\varepsilon)>0,
\]

使四维流形若在 \(B_r(x)\), \(r\le1\) 上满足

\[
|\operatorname{Ric}|\le3,\qquad
\int_{B_r(x)}|\operatorname{Rm}|^2\le\delta_L,
\]

则存在 \(s\ge a_Lr\)，使

\[
s^4\fint_{B_s(x)}|\operatorname{Rm}|^2\le\varepsilon.
\tag{4.1}
\]

这正是 Ge–Jiang Theorem 3.4 对 Cheeger–Tian/Li 的引用。它不是原度量的点态曲率估计。

### Lemma S：局部无浓缩下平滑

Li II 支持如下全局局部能量版本：若所有 \(r\)-球满足

\[
\int_{B_r(x)}|\operatorname{Rm}(g_0)|^2\le\varepsilon_L,
\qquad
|\operatorname{Ric}(g_0)|\le K,
\]

则 Ricci flow 至少存在到

\[
T\ge C\min\{r^2,K^{-1}\},
\]

且

\[
|\operatorname{Rm}(g(t))|\le Ct^{-1}.
\tag{4.2}
\]

也可先通过 (4.1) 得到小体积归一化能量，再应用 Li 的平滑框架。

### 用途与限制

可用于：

- 构造 chopping 边界；
- 提取有界曲率比较几何；
- 识别局部 \(F\)-structure/infra-nil 纤维；
- 把“无浓缩区域”与“能量集中区域”分开。

不能未经证明用于：

- 保持 \(\operatorname{Ric}\approx g\)；
- 将平滑度量的 Einstein 障碍直接转回原度量；
- 得到原度量的点态 Weyl 控制。

---

## V. Naber–Zhang 的准确可用输出：覆盖调和半径，而非预极限曲率

设 \(B_2(p)\) 满足 \(|\operatorname{Ric}|\le n-1\)，并固定尺度 GH 逼近

\[
\mathbb R^{k-\ell}\times Z^\ell,\qquad \ell\le3,
\]

模型非塌缩半径 \(r_c(Z,z)\ge r_*>0\)，且纤维基本群达到最大幂零秩

\[
\operatorname{rank}\Gamma_{\delta}(p)=n-k.
\]

Naber–Zhang Proposition 6.4 给出局部通用覆盖上

\[
r_h(\tilde q)\ge h_0(n,r_*)>0.
\tag{5.1}
\]

### Lemma E：覆盖上的 Einstein germ 极限

若在这些图上

\[
\|\operatorname{Ric}_{g_i}-g_i\|_\infty\to0,
\]

则经子列

\[
g_i\to g_\infty
\quad\text{于 }C^{1,\alpha}\cap W^{2,p}_{\mathrm{loc}}
\]

并且弱意义下

\[
\operatorname{Ric}_{g_\infty}=g_\infty.
\]

调和坐标方程

\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=
-2(\operatorname{Ric}_{g_i})_{jk}
+
Q_{jk}(g_i^{-1},\partial g_i)
\tag{5.2}
\]

允许通过极限；极限方程变成真正 Einstein 方程，继而椭圆 bootstrap 得到 \(g_\infty\) 光滑。

这不推出 \(|\operatorname{Rm}(g_i)|\) 一致有界，但足以产生光滑 Einstein 极限 germ。

### 与 A01/A03 cover-mean 桥连接

对非负密度 \(F_i\)，正规缓冲覆盖满足

\[
\fint_{B_a(\tilde p_i)}\pi_i^*F_i
\le
C(n,K,a)
\fint_{B_a(p_i)}F_i.
\tag{5.3}
\]

因此，小 downstairs 平均缺陷可传到非塌缩覆盖图，而不受覆盖次数影响。A01/A03 的负支校准矛盾正应在这一层使用：平均缺陷 \(\to0\) 加上 Lemma E，产生被排除的光滑 Einstein germ。

**精确剩余对象：**

- 秩下降；
- \(r_c\to0\)；
- 残余四维核；
- 奇异纤维/边界区域；
- 只有 \(r_i\to0\) 才能解包的点。

这些点构成真正的 accessible-cover 缺口。

---

## VI. 不应优先追求预极限曲率界；应构造弱 Pohozaev/Komar 投影

在一个已假设存在的 \(\mathbb R^4/\mathbb Z_2\)–Eguchi–Hanson 两尺度颈区中，目标恒等式是

\[
\int_{\Omega_i}
\langle\operatorname{Ric}(g_i)-g_i,\phi_i\rangle\,d\mu_{g_i}
=
t_i\,\mathcal O(R_+(p),\mathrm{orientation},\mathrm{rotation})
+o(t_i).
\tag{6.1}
\]

若

\[
\|\phi_i\|_{L^1}=O(t_i),
\]

则 \(C^0\)-Ricci 夹逼直接给出

\[
|\text{LHS}|\le \delta_i\,O(t_i),
\]

从而

\[
\mathcal O=O(\delta_i)+o(1).
\tag{6.2}
\]

### 最先必须计算的量

若 EH 模式衰减使颈区出现

\[
\|\phi_i\|_{L^1(\mathrm{neck})}
\sim t_i\log(t_i^{-1}),
\]

则 (6.2) 只能给出 \(\delta_i\log(t_i^{-1})\) 误差，这在 Yau 26 中不可控。故优先比较：

1. 紧支撑近似余核张量及其伴随误差；
2. Komar/旋转场边界通量形式。

后者利用

\[
d(*dX^\flat)=2*\operatorname{Ric}(X,\cdot)
\]

并减去已知 Einstein 常数项。对于

\[
\operatorname{Ric}=g+E,
\]

未知项仅为 \(E(X,\cdot)\) 的体积分，不出现 \(\nabla E\)。

### 该桥所需的最小输入

- 颈区 \(C^{1,\alpha}\cap W^{2,p}\) 规范控制；
- 内外渐近展开足以识别通量首项；
- 近似旋转场的 Killing 缺陷可积；
- 泡树情况下各颈通量的守恒/求和公式。

首阶障碍消失只给出 \(R_+\) 的适当退化条件；它不等同于 Kähler–Einstein，也不解决高阶或全局障碍。

---

## VII. 关于“吹起后 Ricci-flat，所以恢复 CT”的修正

若按长度因子 \(r_i^{-1}\) 吹起，即

\[
\tilde g_i=r_i^{-2}g_i,
\]

则

\[
|\operatorname{Ric}_{\tilde g_i}|_{\tilde g_i}
=
r_i^2|\operatorname{Ric}_{g_i}|_{g_i}\to0.
\tag{7.1}
\]

因此任何具有足够紧性的泡极限确实是 Ricci-flat。但不能由此无条件推出：

- 极限一定 ALE；
- 每个集中点都有统一正能量量子；
- ALF/ALG/ALH 泡可由同一来源下界处理；
- 或原序列在覆盖球上满足点态正则性。

由现有材料只能提出下列**条件性无泡引理**：

> 若在固定非塌缩覆盖尺度上可提取完整、非平坦、有限 \(L^2\) 的 Ricci-flat 四维泡，并且该允许泡类别具有统一能量下界 \(\varepsilon_{\rm bub}>0\)，则覆盖球能量 \(<\varepsilon_{\rm bub}\) 排除该类集中。

要升级为定理，必须补充：

1. 泡极限的完整性及体积增长；
2. 有限能量；
3. ALE/ALF/ALG/ALH 分类范围；
4. 该范围内统一正能量下界。

当前来源只提醒 K3 型塌缩可能产生 ALF/过渡区，不能把 Eguchi–Hanson 的 \(12\pi^2\) 当成普适量子。

---

## VIII. Simply-connected volume gap 的正确接口

假设四维正支存在

\[
\pi_1(M)=0,\qquad
\|\operatorname{Ric}-g\|_\infty\le\delta<1/2,\qquad
\operatorname{Vol}(M)\to0.
\]

现有公式给出

\[
8\pi^2\chi(M)
=
\int_M
\left(
|W|^2+\frac{s^2}{24}-\frac{|E|^2}{2}
\right)d\mu,
\]

以及

\[
\int|W|^2
\ge
8\pi^2\left[
\chi(M)-2\left(\frac{1+\delta}{1-\delta}\right)^2
\right].
\tag{8.1}
\]

故高 \(\chi\) 可以支付任意多的浓缩点；仅靠 CGB 加“每泡一份能量”不能给出维数一致体积下界。

### 真正需要的局部化引理

优先攻击：

> **Rank-drop energy/topology lemma.**  
> 对正 Ricci 紧夹逼四维球，若固定尺度上的纤维幂零秩不是最大值，则在一个可比尺度上，要么出现统一 Weyl 能量下界，要么该球属于一个可控的奇异纤维类型，并且该类型携带非零局部 Euler/topological charge。

其价值是把所有 Euler 特征从规则塌缩区推到可数的奇异/秩降区域。还需进一步证明这些局部 charge 无法以无界数量塞进体积趋零的 simply-connected 序列；这正是当前体积间隙路线最缺的对象。

### 不可使用的捷径

“规则 \(F\)-structure 区的 \(\chi=0\)”不等于整个流形 \(\chi=0\)。任意大的 \(\chi\) 可由许多奇异区承担，正如 K3 型塌缩所示。因此不能由规则区体积占比大直接推出矛盾。

### 一旦 simply-connected gap 成立

若存在 \(v_0>0\)，使所有 simply-connected 正夹逼四流形体积至少 \(v_0\)，则 Step 10 的有限覆盖放大是有效的：

- Myers 给出有限 \(\pi_1\)；
- universal cover 的体积至少 \(v_0\)；
- Cheeger–Naber 四维非塌缩有限型给出 covers 的有限微分同胚类型及 \(\chi\) 上界；
- 覆盖次数由
  \[
  |\pi_1(M)|\le \chi(\widetilde M)
  \]
  控制；
- 从而所有基流形具有统一体积下界和有限微分同胚类型。

但这仍不自动产生 Einstein 度量；非塌缩 orbifold 极限仍需第 VI 节的投影与解奇异桥。

---

## IX. 建议的执行顺序与路线判据

### 优先级 1：完成显式标量尖峰

严格构造 \(u_j\)，验证 \(T^2\) 模型的全部 Ricci/Riemann 公式与尺度。  
**若成功：** 强 \(CT_{C^0}\) 被否定，研究骨架固定为 Li + NZ covers + 弱投影。  
**若失败：** 查明失败是否来自二维 Hessian/CZ 约束或闭合移植误差。

### 优先级 2：写成可引用的 Li 定理包

准确记录 (4.1)、(4.2) 的球、缓冲、缩放和常数依赖；避免把尺度选择误写成点态控制。

### 优先级 3：证明 accessible-cover Einstein-germ lemma

从 Proposition 6.4 和调和坐标方程严格推出覆盖上的光滑 Einstein 极限，并同时写入 cover-mean 输运。此结果可直接服务 A01/A03 的固定尺度排除。

### 优先级 4：计算 EH 测试模式的颈区 \(L^1\) 与 Komar 通量

决定是否存在对数损失。  
**无对数损失：** 建立 \(O(\delta t)\) 首障碍投影。  
**有不可消除对数：** 纯 bulk-cokernel 路线不足，必须改用边界通量或增加尺度关系。

### 优先级 5：条件性 bubble/no-bubble 定理

先明确假设泡类别，而不是宣称普适 ALE 量子。补齐 ALF/ALG/ALH 能量下界后再扩大范围。

### 优先级 6：rank-drop 局部 charge 定理

这是 simply-connected volume gap 与 A01/A03 accessible-cover 残余的共同核心：定量描述没有固定尺度可达覆盖的点如何携带能量、Euler 特征或纤维退化。

---

## 最终科学分叉

当前最可信的结构不是“从 \(C^0\)-Ricci 夹逼恢复原度量点态曲率”，而是：

\[
\boxed{
\text{Li 可比尺度}
\;+\;
\text{Naber--Zhang 覆盖调和图}
\;+\;
\text{覆盖平均输运}
\;+\;
\text{光滑 Einstein 极限 germ}
\;+\;
\text{Pohozaev/Komar 弱投影}.
}
\]

精确未决对象是：**几乎全部体积是否可能落在无任何固定尺度 accessible cover 的秩降、退化模型或残余四维核中。** 对这一集合建立局部能量/拓扑 charge 定理，将同时推进正支 simply-connected volume gap、负支 A01/A03 排除，以及 orbifold/ALE 投影桥。
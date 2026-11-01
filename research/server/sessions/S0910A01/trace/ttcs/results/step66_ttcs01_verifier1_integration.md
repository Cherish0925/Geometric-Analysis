# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 66,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step66_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step66_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step 66 route reorientation note and related context. Check the mathematical logic and scope: the correction to Step65's family-uniform C^k wording; exclusion of #5CP2 by tight-pinching Hitchin--Thorpe; asymmetric interpretation of A02's Green-operator desingularization computation; and the claimed flow-transfer principle from sign-general cutoff flow plus calibration density to a branch gap. Identify any overstatement, missing assumption, or stronger route suggested by the same evidence. Keep the answer scientific and concrete.

## Integrated Scientific Memo

# Step 66 数学核验结论

Step 66 的路线修正总体方向正确，但有两处实质性过述：

1. **Step 65 尚未单独补齐到共同观察时刻 \(\theta r^2\) 的延拓。**
2. **“Green 算子计算成功即构造 Einstein 度量”必须降为“首阶相容”；只有完整非线性拼接成功才证明存在。**

此外，所谓 flow-transfer principle 还缺一个关键接口：**初始校准缺陷如何传递为终端拉回球上的小平均密度**。

---

## 1. 对 Step 65 的 \(C^k\) 修正：逻辑正确，但完成度被高估

撤回“族上一致的高阶 \(C^k\) 界”是正确的。对单个 datum，若在有限时刻 \(T\) 已得到光滑正定极限 \(g_T\)，则可以在几何变量中从 \((g_T,\chi)\) 重启
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g-\sigma g).
\]
因为方程自治，所有时间 jet 都是 \(g_T,\chi\) 的空间 jets 所决定的通用表达式，故两段解在 \(T\) 处自动匹配；不需要贯穿全程的 DeTurck gauge，也不需要族上一致的全部高阶估计。

但这不能推出记录中已经到达统一观察时刻。仍需证明：

- 每个潜在终止时刻都有唯一的 \(C^\infty\) 正定端点；
- fixed-background current-pair 层级达到重启所需阶数；
- 重启时间不会发生 Zeno 累积。

Step 55 明确把“完成所需各阶 current-pair hierarchy”列为尚缺工作。其 \((\Gamma,V)\) bootstrap 给出双 Lipschitz 控制和正定性：
\[
e^{-2V}g(0)\le g(t)\le e^{2V}g(0),
\]
但不直接给出 Step 65 局部时间依赖的 \(H^{s_0}\)（四维为 \(H^7\)）统一界。因此 Step 66 所称“移除了最后一个解析假设”以及 Front A 已可组装成完整定理，都超出当前文件所证。

同时应修正 Step 65 §7 的 gauge 表述：若在几何坐标中从 \((g(T),\chi)\) 重启且新 DeTurck 映射初值为恒等，则
\[
\widetilde\beta(0)=\chi,
\]
而不是 \(\chi\circ\varphi_T^{-1}\)。后者只适用于沿用旧 transported 坐标的描述。直接在几何变量中拼接可避免混淆。

还有文本缺损：§4.5 中 “Grönwall gives” 后中断，所引用的 (4.9) 不存在，且 (4.7) 重号。这些使全阶一致估计无法由本束材料独立核验。

### 终端 germ 所需的正则性可以更弱

延拓单个流需要 datum-dependent 高阶端点控制；但抽取 Einstein germ 不必要求族上一致 \(C^\infty\) 控制。指数拉回球上若有统一曲率界，Rauch 给出体积控制；配合 harmonic-radius 理论和有限 \(W^{2,p}\) 紧性即可得到弱 Einstein 极限，再由 harmonic-coordinate Einstein 方程提升为光滑极限。Step 8 的有限 \(W^{2,p}\) 路径比 Step 55 所暗示的“先有全部导数界再作光滑紧性”更经济。

---

## 2. \(\#_5\mathbb{CP}^2\) 的排除正确，而且应扩展到 \(m=4\)

对
\[
M_m=\#_m\mathbb{CP}^2
\]
有
\[
\chi=m+2,\qquad \tau=m,\qquad 2\chi-3|\tau|=4-m.
\]
若
\[
\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{\infty,\mathrm{op}}
\le\varepsilon,\qquad \sigma=\pm1,
\]
则四维 Chern–Weil 公式给出
\[
2\chi\pm3\tau\ge
\frac{\operatorname{Vol}(M,g)}{4\pi^2}
\left[\frac23(1-\varepsilon)^2-2\varepsilon^2\right].
\]
当
\[
\varepsilon<\varepsilon_{\mathrm{HT}}
:=\frac1{1+\sqrt3}
\]
时，右侧严格为正，故
\[
2\chi>3|\tau|.
\]

因此：

- \(m\ge5\) 的严格 Hitchin–Thorpe 违例者不能有任意紧的 \(\pm1\)-Ricci 夹逼；
- **\(m=4\) 的等号情形也被严格不等式排除；**
- 在该连通和族中，只有 \(m\le3\) 尚可能作为紧正分支候选。

所以 Step 66 的“\(\#_5\mathbb{CP}^2\) 不再是 live target”正确，但“all stronger violators”遗漏了边界型 \(\#_4\mathbb{CP}^2\)。此外，\(\#_3\mathbb{CP}^2\) 目前只能称为“需核准 Einstein 存在状态的 strict-HT 类型”，不能先当作已知无 Einstein 流形。

同一估计还给出有用的拓扑依赖体积界：
\[
\operatorname{Vol}(M,g)
\le
\frac{4\pi^2(2\chi-3|\tau|)}
{\kappa(\varepsilon)},\qquad
\kappa(\varepsilon)=\frac23(1-\varepsilon)^2-2\varepsilon^2.
\]
结合 Chern–Weil 可进一步得到固定拓扑上的 \(L^2\)-全曲率界。故四维紧夹逼序列在非塌缩区域已落入标准 bounded-Ricci/orbifold compactness 框架；真正未统一处理的仍是塌缩与去奇点。

---

## 3. Green 算子计算：非对称解释正确，但“成功”一侧过强

应区分三个层级：

1. **首阶相容：**Green 算子或 interaction matrix 的余核投影为零；
2. **指定通道受阻：**在已证明的必要性定理下，投影非零排除指定 orbifold、ALE 泡、方向、尺度及参数模式；
3. **精确存在：**高阶阻碍全部消失，并建立线性反算子、规范控制和非线性固定点，实际构造出 Einstein 度量。

因此，有利的 Green 算子结果通常只说明“首阶未受阻”，不能直接说“构造 exact Einstein metrics”。还必须检查尺度、旋转、多个奇点耦合和 orbifold 变形等所有可调参数；单个矩阵元非零也未必排除整体参数组合的抵消。

另一方面，完整非线性拼接若成功，确实证明所得光滑类型承载 Einstein 度量，从候选库中删除该类型。失败或局部阻碍只排除所研究的退化通道，不能排除远离该 orbifold 的 Einstein 度量。要升级为全局无 Einstein，必须有分类或紧性/刚性定理把该光滑类型上的所有相关 Einstein 度量都迫入已分析的退化列表，并另行覆盖不同 Einstein 常数符号及 Ricci-flat 情形。

---

## 4. flow-transfer principle 必须写成带假设的条件命题

Step 66 的抽象机制是合理的，但“sign-general cutoff flow + calibration density \(\Rightarrow\) branch gap”并非由现有结果自动成立。一个可用版本至少需要以下数据。

### 4.1 统一可运行的局部流

需有统一尺度 \(r,\theta\)、cutoff 平台及缓冲区，并满足相应临界小量条件，例如四维中的
\[
\mathcal S_i(0)H_i(0)^{1/2}<\gamma_*,
\]
连同 cutoff jets 的控制。仅有全局积分预算并不自动产生该局部小量。

### 4.2 到共同终端时刻的估计

在
\[
T=\theta r^2
\]
必须得到平台上的统一全曲率界和
\[
\|\operatorname{Ric}_{g_i(T)}-\sigma g_i(T)\|_\infty\to0,
\]
以及控制度量畸变的
\[
V_i(T)=\int_0^T\|\chi_i^2E_{\sigma,i}(t)\|_\infty\,dt.
\]
这里 datum-dependent 高阶控制用于延拓，族上一致的低阶几何界用于局部紧性；两者不能混为一谈。

### 4.3 缺失的核心接口：终端校准密度

必须证明某个非负自然密度 \(\Phi_\sigma\) 在终端拉回球上满足
\[
\fint_{\mathcal B_\rho(p_i)}
(\exp_{p_i})^*\Phi_\sigma(g_i(T))\,d\mu\to0.
\]

现有 IL 预算首先控制的是初始度量。Step 55 只控制加权量 \(\chi^2E\) 和加权曲率能量；在 cutoff 过渡区 \(0<\chi<1\) 并不能直接控制未加权的 \(|E|\)，也没有现成结论保证
\[
(s+8\sqrt6|W^+|)^2+\mathcal G
\]
的小平均由 \(t=0\) 保持到 \(t=T\)。因此需要额外证明以下任一项：

- 校准密度的时空传输估计；
- 终端时刻的局部 Chern–Weil 预算，并控制平台边界的 transgression 项；
- cutoff 过渡区贡献可忽略的定量构造。

这是当前 flow-transfer 链条中最明确的缺口之一。

### 4.4 极限和零集

拉回球上需要有限 \(W^{2,p}\) 紧性，使极限满足
\[
\operatorname{Ric}_{g_\infty}=\sigma g_\infty
\]
并能在 \(L^1\) 中传递 \(\Phi_\sigma\)。由非负性和平均趋零，才能推出
\[
\Phi_\sigma(g_\infty)\equiv0
\]
于开球。

最后还必须区分：

- **局部 germ 矛盾型：**不存在满足 Einstein 方程及 \(\Phi_\sigma=0\) 的局部光滑 germ。IL 的 Derdziński 机制属于此型。
- **全局刚性型：**零集只给出合法局部模型，但其全局延拓与拓扑冲突。此时还需解析延拓、完备化、单值性或全局收敛定理；局部紧性不足。

只有全部常数对目标流形族统一时，反证序列法才产生该族的正 gap；只有这些常数最终仅依赖 \(n\)，才接近 Yau 26 的维数常数。

---

## 5. IL 校准本身可靠，但“统一 IL gap 已完成”仍早

Step 8 的局部终结机制是坚实的。若终端极限满足
\[
\operatorname{Ric}=-g,\qquad
\operatorname{spec}(W^+)=
\left(-\frac16,\frac1{12},\frac1{12}\right),
\]
则 Derdziński 因子为常数 \(1\)，迫使局部 Kähler；但归一化为 \(\operatorname{Ric}=-g\) 的 Kähler–Einstein 四维度量应有
\[
\operatorname{spec}(W^+)=
\left(-\frac23,\frac13,\frac13\right),
\]
产生局部矛盾。等价地，Einstein–Weyl 恒等式要求
\[
|\nabla W^+|^2=\frac1{16},
\]
而 Derdziński/projector 机制给出 \(\nabla W^+=0\)。

不过，当前材料尚未把以下统一常数链完整闭合：

\[
\text{初始 near-Einstein}
\Longrightarrow
\text{共同时间存在}
\Longrightarrow
\text{终端小校准平均}
\Longrightarrow
\text{拉回球极限}
\Longrightarrow
\text{禁戒 germ}.
\]

因此 Step 66 Front A 的 uniform \(\varepsilon_{IL}\) 应标为待完成的条件性定理，而不是已经由 Step 65 自动获得的结果。

一个可简化 IL bookkeeping 的恒等式是
\[
D(g)
=(2\chi+3\tau)-\frac23(a^+)^2
+\frac1{8\pi^2}\int |E|^2\,d\mu,
\]
直接来自 Chern–Weil。对
\[
M=X\#k\,\overline{\mathbb{CP}}^2,\qquad c_1^2(X)=A,
\]
它给出
\[
D(g)=\left(\frac A3-k\right)
+\frac1{8\pi^2}\int|E|^2.
\]
故初始 deficit 小主要归结为 \(k/A\to1/3\)、Ricci defect 小以及体积控制，而非额外独立的解析假设。真正困难仍是终端密度接口。

---

## 6. 符号和维数不能仅凭 Step 65 自动迁移

Step 65 的**局部存在构造**确实对所有 \(\sigma\in\mathbb R\)、所有 \(n\ge2\) 适用；但 Steps 55–63 的 smoothing/calibration 模块是四维负分支结构，不能由此宣称 sign-general flow-transfer 已完成。

在规范
\[
G_0=\frac{g\owedge g}{2(n-1)},\qquad \operatorname{Ric}(G_0)=-g
\]
下，与
\[
E_\sigma=\operatorname{Ric}-\sigma g
\]
相配的 shifted curvature 应为
\[
T_\sigma=\operatorname{Rm}+\sigma G_0,
\qquad \operatorname{Ric}(T_\sigma)=E_\sigma.
\]
特别地，负分支 \(\sigma=-1\) 使用
\[
T_{-1}=\operatorname{Rm}-G_0.
\]
Step 55 中 \(T=\operatorname{Rm}+G\) 与 \(E=\operatorname{Ric}+g\) 在该新规范下不相容，不能只修正文首显示式；凡涉及 Ricci 收缩、\(U_m=\nabla^m(aT)\)、势项及终端密度的公式均须重算。

高维方面，四维层级依赖临界 \(L^2\) 曲率和 \(H^1\hookrightarrow L^4\)。在 \(n\ge5\) 应改为 \(L^{n/2}\) 及相应 Sobolev 指数，而纯 Ricci 夹逼没有现成的统一临界全曲率预算。这是比“缺少高维校准密度”更上游的障碍。

---

## 7. 对正分支的更准确定位

Step 66 正确指出目前没有正分支的 LeBrun 型校准。还可更明确：当
\[
\delta_+(g)<1
\]
时标量曲率严格为正，所记录的 monopole/Seiberg–Witten 型障碍通常与输入本身不相容。因此正分支不只是“尚未找到同类校准”，而是现有 monopole 机制很可能不是可迁移工具。

四维正分支最有价值的分解是：

1. Chern–Weil 已强迫 strict Hitchin–Thorpe，并给出固定拓扑的体积及 \(L^2\)-曲率界；
2. 非塌缩子序列进入 Einstein orbifold 紧性；
3. orbifold 极限能否在原光滑类型上去奇点，正是 Green 算子及高阶阻碍计算能够回答的局部问题；
4. 塌缩情形和“所有可能 orbifold 极限是否已覆盖”仍是全局缺口。

这比直接寻找另一个正 Ricci 连通和构造更强：现有 coarse positive-Ricci gluing 没有提供 \(\delta_+\to0\)，而 orbifold compactness/desingularization 路线至少直接针对 near-Einstein 序列的必要退化结构。

---

## 精确结论

Step 66 中应保留：

- 撤回 family-uniform \(C^k\) 断言；
- 排除 \(\#_5\mathbb{CP}^2\)；
- Green 计算只能局部解释；
- cutoff flow 本身不产生正分支校准。

应修正为：

- 排除范围包括所有 \(2\chi\le3|\tau|\) 类型，特别是 \(\#_4\mathbb{CP}^2\)；
- Green “成功”仅是首阶相容，除非完整非线性拼接已完成；
- Step 65 尚未独立消除共同时间延拓和全阶 continuation 缺口；
- flow-transfer 必须加入终端校准密度的传输/局部预算假设；
- “局部禁戒 germ”与“全局刚性类别不相容”须分成两个命题；
- sign-general 仅适用于局部流存在，不适用于现有四维 IL smoothing/calibration 全链条。
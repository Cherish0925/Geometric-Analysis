# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 25,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step25_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step25_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the corrected Step 25 single-support argument as a PDE/geometric compactness expert. Determine exactly which parts of the simultaneous first-exit are now established and whether the whole-support bounds for a Rm and aE genuinely restore metric/Sobolev/cutoff control before plateau regularity. Then analyze the remaining normalized Yang-Wang existence/continuation adaptation: does bounded |a Rm| together with the derived metric comparison suffice after adding -2ag, or are additional uniform quantities missing? Finally verify that the only justified terminal local obstruction is the Step 6 projector plus Einstein-Weyl identity, not local-symmetry classification. Produce a precise scientific memo that distinguishes proved implications from remaining derivations without reducing the original Yau 26 goal.

## Integrated Scientific Memo

# 科学复核备忘录

## 结论

Step 25 已经实质修复了归一化能量记账和“只控平台、不控过渡带”两个漏洞。对一个**已经存在且光滑**、并处于预设双 Lipschitz/Sobolev 首次逸出区间内的解，它建立了：

\[
H_2\text{ 持续控制}
\Longrightarrow H_3(t)\lesssim t^{-1}
\Longrightarrow
\|a\Rm\|_\infty,\ \|aE\|_\infty
\]

在整个活动支撑 \(\{a>0\}\) 上的估计。尤其

\[
\|aE(t)\|_\infty
\le C\delta \Bigl(\frac{r^2}{t}\Bigr)^{1/3}
\]

可积到 \(t=0\)，因此确实恢复过渡环带上的度量、体积、Sobolev 与一阶截断控制；平台正则性不能替代这一点。

但完整论证仍未闭合。尚需：

1. 把 Step 25 的一般 \(p\) 张量能量不等式写成完整引理；
2. 修正或补充 \(\beta\) 与辅助支撑 \(H_2\) 的比较；
3. 在实际塌缩支撑上证明所假设的相对 Sobolev 不等式；
4. 写出加入 \(-2ag\) 后的 Wang 高阶延拓归纳。

终端局部矛盾只能使用 Step 6 的投影子引理与 Einstein–Weyl 标量恒等式；不能诉诸局部对称空间分类。

---

## 1. 已核实的能量层

### 1.1 四维归一化项没有临界曲率能量耗散

对空间常数 \(a\) 的纯缩放部分 \(\partial_tg=-2ag\)，混合指标曲率不变，而

\[
\partial_tR_{ijkl}=-2aR_{ijkl}.
\]

令 \(x=|\Rm|^2\)。两个曲率因子贡献 \(-4ax\)，四个逆度量贡献 \(+8ax\)，故

\[
\partial_tx=4ax.
\]

四维中 \(\partial_td\mu=-4a\,d\mu\)，所以

\[
\partial_t(x\,d\mu)=0.
\]

更一般地，对 \(F=(1+x)^{1/2}\)，

\[
\left.\partial_t(F^pd\mu)\right|_{-2ag}
=2a\bigl[(p-2)F^p-pF^{p-2}\bigr]d\mu .
\]

因此 \(p=2\) 时仅有常数 \(1\) 的体积变化，不存在可用于吸收反应项的 \(-4aF^2\) 耗散。Step 25 改用

\[
H_2'+cD_2
\le C\int\eta^2aF^3+Cr^{-2}H_2
\]

是正确修复。

### 1.2 \(q=2,3\) 与缺陷二次能量有逐指标依据

A01 的张量计算支持

\[
\begin{aligned}
H_2'+cD_2&\le C\int\eta^2aF^3+Cr^{-2}H_2,\\
H_3'+cD_3&\le Cr^{-2}H_3+C\int\eta^2a^2F^4,\\
Q'+cX&\le Cr^{-2}Q+C\int\eta^2aF|E|^2.
\end{aligned}
\]

关键结构均正确：

- 曲率演化可写成
  \[
  \partial_t\Rm
  =a\Delta\Rm+a\mathcal A(\Rm)
   +(da)*\nabla E+(\nabla^2a)*E;
  \]
- 不存在独立的 \((\nabla^2a)*g\) 源；
- Hessian-\(a\) 项一次分部积分后由
  \[
  \frac{|da|^2}{a}=4|d\chi|^2
  \]
  控制；
- 严格缓冲条件消除所有 \(a\,d\eta\) 和 \(da\,d\eta\) 项；
- 缺陷方程齐次：
  \[
  (\partial_t-a\Delta)|E|^2
  =-2a|\nabla E|^2+4a\Rm(E,E)
   +2\langle E,\mathcal C_a(E)\rangle,
  \]
  因而没有纯曲率加性源。

固定 \(q=3\) 方程也确实排除了终端时间尖峰：先从 spacetime \(H_3\) 选取好时间片，再用 \(H_3'\le Cr^{-2}H_3\) 向终点传播，而非从时间积分直接推出终值。

### 1.3 Yang 固定截断迭代的幂次完全匹配

四维中

\[
p_{j+1}=\frac32p_j,\qquad
p'_{j+1}=\frac32p'_j+1.
\]

若 \(p'_0=p_0-2\)，则 \(p'_j=p_j-2\)，从而

\[
\chi^{2p'_j}\Phi^{p_j}
=a^{p_j-2}\Phi^{p_j}=K_{p_j}[\Phi],
\]

且极限对象为

\[
\chi^{2p'_j/p_j}\Phi\to a\Phi.
\]

势函数指数 \(q=6\) 时，Yang 所需的加权势正是

\[
\int\chi^{q-4}F^{q/2}=\int aF^3=H_3.
\]

所以该迭代真正覆盖整个过渡环带，而非只覆盖 \(a=1\) 平台。

---

## 2. 首次逸出目前闭合到什么程度

### 2.1 全支撑点态输出

在一般 \(p\) 不等式成立、临界能量保持小且 Sobolev 不等式可用的前提下，Moser 迭代给出：

\[
\|a\Rm(t)\|_\infty
\le C\frac{\beta_*}{t},
\]

以及

\[
\|aE(t)\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3},
\qquad 0<t\le r^2.
\]

后一式满足

\[
\int_0^{\theta r^2}\|aE(s)\|_\infty\,ds
\le \frac32C\delta\,\theta^{2/3}r^2.
\]

这两个估计作用不同：

- \(\|aE\|_\infty\) 控制度量速度，负责从 \(t=0\) 起闭合低阶首次逸出；
- \(\|a\Rm\|_\infty\sim t^{-1}\) 不可积到零，不能单独控制初始时刻附近的度量，但可用于正时间延拓和平台内部正则性。

### 2.2 度量、Sobolev 和截断控制确实被恢复

由

\[
\partial_tg=-2aE
\]

直接得到

\[
e^{-2I(t)}g_0\le g(t)\le e^{2I(t)}g_0,
\qquad
I(t)=\int_0^t\|aE(s)\|_\infty ds.
\]

因此，在 \(\delta\) 足够小时，全活动支撑上同时得到：

- 双 Lipschitz 度量比较；
- 固定区域体积元比较；
- 初始相对 Sobolev 不等式向 \(g(t)\) 的转移；
- \(|d\chi|_{g(t)}\) 控制；
- 若初始缓冲有正余量，则固定支撑包含关系的保持。

这正是过渡环带所缺失的控制。仅有平台上的正则性不能推出这些结论，因为过渡带上 \(a>0\) 时度量仍在演化。

需要区分：双 Lipschitz 比较只直接控制 \(|d\chi|\)，不自动控制 \(\nabla^2\chi,\nabla^3\chi,\ldots\)。后者不参与当前弱能量闭环，却参与 Wang 高阶延拓归纳。

### 2.3 \(\beta\) 的表述需要修正

Step 25 定义

\[
\beta(t)=\mathsf S\|F\|_{L^2(\operatorname{supp}\chi)},
\]

但

\[
H_2=\int\eta^2F^2
\]

在更大的辅助支撑上积分。直接由 \(q=2,3\) 方程得到的是

\[
H_3(t)\le \frac{C\beta_*H_2(0)}{t},
\]

故

\[
\mathsf S^2H_3(t)
\le \frac{C\beta_*b_0^2}{t},
\qquad
b_0:=\mathsf S H_2(0)^{1/2}.
\]

要写成 \(C\beta_*^3/t\)，需额外证明 \(b_0\lesssim\beta_*\)。更稳妥的定义是

\[
\bar\beta(t):=\mathsf S H_2(t)^{1/2}.
\]

它仍控制临界吸收系数，并直接给出

\[
\mathsf S^2H_3(t)\le C\bar\beta_*^3t^{-1},
\qquad
\|a\Rm(t)\|_\infty\le C\bar\beta_*t^{-1}.
\]

此外，\(H_2(t)\le e^{Ct/r^2}H_2(0)\) 表明的是“带初始余量的持续小性”，并非单调改善。首次逸出阈值必须预留 \(e^{C\theta}\) 的增长余量。

### 2.4 最大的几何前提仍是相对 Sobolev 不等式

整个吸收和 Moser 过程预设

\[
\|u\|_4^2
\le\mathsf S\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\qquad
\mathsf S\lesssim r^2V^{-1/2},
\]

在所选辅助支撑上成立。Step 25 证明了：**一旦初始 Sobolev 不等式成立，\(\|aE\|_\infty\) 可使其在首次逸出区间内持续成立。** 它没有证明塌缩宏支撑本身具备该初始不等式。

Yang 的标准局部 Sobolev构造依赖小球体积下界，而 Step 6 的固定拓扑临界序列恰在单位尺度处处塌缩。因此，这一初始 Sobolev 输入不能由所引 Yang 定理直接推出。它需要额外的塌缩几何论证，例如受控局部解包、覆盖空间上的不等式及向下传递，或针对所选宏支撑的独立相对等周/Sobolev 定理。

故正确结论是：

> Step 25 已闭合“给定初始 Sobolev 与短时光滑解后的首次逸出 a priori 循环”，但尚未闭合塌缩支撑上的几何初始化。

---

## 3. 一般 \(p\) 不等式仍是待补证明，而非已由逐指标文件完全验证

A01 文件完整推导了 \(q=2,3\) 曲率能量和 \(Q\) 缺陷能量，但未逐项证明 Step 25 的一般式

\[
\frac d{dt}K_p+c\|\nabla Z_p\|_2^2
\le Cp^2r^{-2}K_p
 +Cp\int\eta^2a^{p-1}F\Phi^p.
\tag{*}
\]

权重代数、Yang 的迭代结构及 \(p^3\) 增长均相容，未发现反例；但严格证明仍需处理：

- 演化度量下的张量范数和体积变化；
- 对一般 \(p\) 的 Hessian-\(a\) 分部积分；
- 缺陷情形的 \(|E|\) 光滑正则化及极限；
- 常数关于 \(p\) 的一致多项式界。

由于 \(J_6\) 传播以及两次高指数迭代都依赖 \((*)\)，它应被视为剩余解析引理，而不是已经由 A01 的 \(q=2,3\) 计算自动覆盖。

---

## 4. 归一化 Yang–Wang 存在与延拓

### 4.1 短时存在

加入 \(-2ag\) 不改变 DeTurck 系统的主符号；它是度量变量中的零阶项。因此 Yang 的退化局部 Ricci 流构造或 \(\varepsilon^2+a\) 严格抛物逼近应直接给出短时存在。这里没有新的主符号障碍。

### 4.2 \(|a\Rm|\) 有界和度量比较是否已经足够

在正时间区间 \([t_0,T)\) 上，若

\[
\sup_{M\times[t_0,T)}|a\Rm|<\infty,
\]

则

\[
|aE|
\le C_n|a\Rm|+C_na
\]

也有界，因此度量一致等价、Sobolev 常数和 \(|d\chi|\) 均有界。结构上，这正是 Wang 延拓定理的起点。

但这些零阶量**不会自动给出光滑延拓**。Wang 的证明还需建立耦合高阶体系：

\[
\|\Rm\|_{L^p},\qquad
\|\nabla^m(a\Rm)\|_{L^p},\qquad
\|\nabla^m\chi\|_{L^p},\qquad
\|\nabla^{m-1}\Rm\|_{L^p},
\]

最后通过 Sobolev 嵌入得到

\[
\|\nabla^m(a\Rm)\|_\infty<\infty.
\]

因此“\(|a\Rm|\) 有界加度量比较即直接延拓”尚未证明；缺少的是 Wang Lemmas 4.4–4.6、4.10–4.14 的归一化版本。

### 4.3 新增 \(-2ag\) 是否需要额外几何量

现有结构表明不需要新的曲率阶假设。新增项分为：

- 曲率演化中的零阶 \(a\Rm\) 型项；
- 对空间变化的 \(a\)，出现固定截断导数与 \(g\) 的组合；
- 在与局部 Ricci 部分合并后，Hessian 项可保持为 \((\nabla^2a)*E\)。

例如非加权 \(L^p\) 曲率能量中的

\[
\int |\Rm|^{p-2}\Rm*(\nabla^2a)*g
\]

经分部积分可由

\[
\varepsilon\int a|\Rm|^{p-2}|\nabla\Rm|^2
+
C_\varepsilon\int \frac{|da|^2}{a}(1+|\Rm|^p)
\]

控制。由于 \(|da|^2/a=4|d\chi|^2\)，这只增加低阶或加性项。

因此最合理的严格判断是：

> 对固定光滑 \(a=\chi^2\) 的紧致流，\(\sup|a\Rm|<\infty\) 很可能仍是充分延拓判据；加入 \(-2ag\) 不显示需要新的独立几何小量。但是必须实际完成高阶 \(L^p\)/截断导数归纳，不能仅以“低阶项”一句代替证明。

还需明确时间分工：Wang 的延拓归纳可从任意 \(t_0>0\) 启动；从 \(0\) 到 \(t_0\) 的度量一致性不能由 \(t^{-1}\) 的曲率界积分得到，而由可积的 \(\|aE\|\sim t^{-1/3}\) 已经提供。

---

## 5. 终端局部障碍

在 Einstein 四维局部极限上，

\[
\Ric=-g,\qquad s=-4,\qquad
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

Einstein 条件给出 \(\delta W^+=0\)。令 \(\omega\) 张成简单特征线，则

\[
W^+=\mu I+(\lambda-\mu)P_\omega.
\]

常特征值和 \(\delta W^+=0\) 导出

\[
(\nabla^a\omega_{ab})\omega_{cd}
+\omega_{ab}\nabla^a\omega_{cd}=0.
\]

与 \(\omega^{cd}\) 收缩并利用 \(|\omega|\) 常数，得到

\[
\nabla^a\omega_{ab}=0.
\]

代回后

\[
\omega_{ab}\nabla^a\omega_{cd}=0.
\]

非零自对偶二形式在四维非退化，故

\[
\nabla\omega=0,\qquad \nabla W^+=0.
\]

另一方面，

\[
|W^+|^2=\frac1{24},
\qquad
\det W^+=-\frac1{864}.
\]

Einstein–Weyl 标量恒等式

\[
\Delta|W^+|^2
=2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]

因谱常数而左端为零，于是

\[
0
=2|\nabla W^+|^2-\frac16+\frac1{24},
\]

即

\[
|\nabla W^+|^2=\frac1{16},
\]

与 \(\nabla W^+=0\) 矛盾。

这就是目前唯一被材料充分支持的终端局部机制。由 \(\nabla W^+=0\) 不能推出 \(\nabla\Rm=0\)，因为 \(W^-\) 仍可能变化；故不能调用局部对称空间分类。

---

## 6. 对整体研究目标的准确定位

这些结果推进的是四维负 Einstein、临界 Ishida–LeBrun 分支中的局部平滑与紧致性机制。尚未建立：

- 从 Yau 第 26 题的双边 Ricci 夹逼到 \(\|\Ric+g\|_\infty\to0\) 的桥梁；
- 塌缩宏支撑上的初始相对 Sobolev 定理；
- 归一化 Wang 完整延拓；
- 所有维数的统一结论。

因此，它既未证明也未证伪完整的 Yau 第 26 题；但 Step 25 的全支撑修复本身是有效的，其剩余障碍已可精确定位为上述三个解析/几何推导，而非过渡环带上的再次失控。
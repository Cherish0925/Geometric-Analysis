# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 24,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step24_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step24_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 24 buffered selected-support energy formulation for the normalized cutoff flow in the Yau 26 four-dimensional negative LeBrun laboratory. Read the note and script together with the prior tensor-structure note and support-geometry correction. Focus on whether separating the physical cutoff chi from the auxiliary energy cutoff eta really avoids bad-center/all-center smallness, whether the weighted cubic moment is the right one for the q=2 and q=3 estimates, whether the time-average propagation for A^4 H3(t) is mathematically justified or needs repair, and whether the triangular Q estimate has hidden terms or unsupported assumptions. Return a direct scientific memo: valid structural points, precise mathematical gaps, corrections, and which exact inequalities remain load-bearing.

## Integrated Scientific Memo

# Step 24 核验备忘录

## 总结判断

Step 24 的核心结构修复是有效的：

\[
\operatorname{supp}\chi\Subset\{\eta=1\}\Subset\Omega_\eta
\]

确实把物理流 cutoff \(a=\chi^2\) 与能量 cutoff \(\eta\) 分离，并使 \(q=2\)、\(q=3\) 及缺陷 \(Q\) 的局部估计只依赖**一个被选 good center \(p\)** 上的最大函数控制，而不需要 bad centers 或 all-center smallness。

但是当前文本仍不是闭合的 PDE 证明。主要修正是：

1. \(q=2\) 的加权三次矩 \(\int aF^3\) 是正确且必要的；
2. \(q=3\) 结论 \(A_\Omega^4Y(t)\lesssim\beta^3/t\) 可以成立，但文中二次反应估计 (6.2) 未被现有推导支持，应改成使用 \(u=aF^{3/2}\) 的**线性临界吸收**；
3. 时间平均只能产生某个 \(s_0\in[t/2,t]\) 的估计，必须结合前向 \(q=3\) 微分不等式传播到 \(t\)；修正后该步骤严格；
4. 三角形 \(Q\) 估计在结构上无隐藏的 curvature-only source，但精确张量计算、演化 Sobolev 控制和统一存在时间仍是实质缺口。

---

## 1. 缓冲支持是否真正消除了 all-center smallness？

### 局部能量层面：是

若

\[
\mathcal M_{R_0}(|\Rm_{g_0}|^2)(p)\le K_0,\qquad L_\eta r\le R_0,
\]

则直接以半径 \(L_\eta r\) 在同一中心 \(p\) 取球，得到

\[
\int_{\Omega_\eta}|\Rm_{g_0}|^2
\le K_0\Vol_{g_0}(\Omega_\eta).
\]

因此

\[
H_2(0)=\int\eta^2F^2
\le (1+K_0)\Vol(\Omega_\eta),
\]

结合四维相对 Sobolev 常数

\[
A_\Omega^2\le C(L_\eta)r^2\Vol(\Omega_\eta)^{-1/2},
\]

得到

\[
\beta_0:=A_\Omega^2H_2(0)^{1/2}
\le C(L_\eta)r^2\sqrt{1+K_0}.
\]

塌缩体积严格消去。若实际相对 Sobolev 定理需要更大的膨胀球，则该膨胀球也必须包含于 \(B_{R_0}(p)\)；这只要求调整固定支持比例，不恢复 all-center 假设。

支持恒等式

\[
a|\nabla\eta|^2=0,\qquad
\langle\nabla a,\nabla\eta\rangle=0,\qquad
\operatorname{supp}a\subset\{\eta=1\}
\]

对所有 \(g(t)\) 都成立，因为它们是时间不变函数的支持关系。在包含 \(\operatorname{supp}\nabla\eta\) 的开 collar 上，\(\chi\equiv0\)，故 \(a,\nabla a,\nabla^2a\) 均为零且

\[
\partial_tg=0.
\]

这里是系数支持导致的精确冻结，不是有限传播。物理 cutoff 的过渡区则位于 \(\eta=1\) 区域内，故其 \(\nabla a,\nabla^2a\) 项被完整纳入能量估计。

### 全局几何结论层面：尚未解决

单支持估计不自动给出：

- 具有确定总体积比例的互不相交 plateau 家族；
- 未选区域的缺陷控制；
- 全流形归一化缺陷 \(Q_i/A_i\to0\)。

“固定比例 thinning 后仍保留确定体积”需要明确的 packing/coloring 引理：先有 \(r\)-分离的 good-center 家族，利用 Ricci 下界产生固定尺度局部 doubling 和交图有界度数，再作加权着色选出互不相交的 \(\Omega_\eta\)。对任意支持族直接 thinning 并不足够。

---

## 2. \(q=2\)：正确的加权三次矩

令

\[
H_2=\int\eta^2F^2,\qquad
D_2=\int\eta^2a|\nabla\Rm|^2,\qquad
R_2=\int\eta^2aF^3.
\]

因 \(\eta=1\) 于 \(\operatorname{supp}a\)，

\[
R_2=\int(\chi F)^2F.
\]

于是

\[
R_2
\le \|F\|_{L^2(\operatorname{supp}\chi)}
   \|\chi F\|_{L^4}^2
\le C\beta(t)\bigl(D_2+r^{-2}H_2\bigr),
\]

其中可取更精确的 active parameter

\[
\beta(t)=A_\Omega^2
\|F(t)\|_{L^2(\operatorname{supp}\chi)}
\le A_\Omega^2H_2(t)^{1/2}.
\]

这是比全 \(\Omega_\eta\) 范数更直接的 first-exit 参数。若仍使用
\(\|F\|_{L^2(\Omega_\eta)}\)，需补上：

\[
\|F(t)\|_{L^2(\Omega_\eta)}^2
\le H_2(t)+
\int_{\Omega_\eta\cap\{\eta<1\}}F(0)^2\,d\mu_0,
\]

因为后一部分位于冻结 collar。

以尚待证明的精确张量不等式

\[
H_2'+cD_2
\le CR_2+Cr^{-2}H_2
\tag{L2}
\]

为前提，临界小量吸收给出

\[
H_2'+c_1D_2\le C_1r^{-2}H_2.
\]

故在 \(T=\theta r^2\) 上

\[
H_2(t)\le e^{C_1\theta}H_2(0),\qquad
\int_0^T D_2\le CH_2(0).
\]

继而

\[
A_\Omega^4\int_0^T\!\!\int aF^3
\le C\beta_*^3.
\tag{Cubic}
\]

这是正确的反应矩。使用 \(\eta\sqrt a\,F\) 产生的
\(a^{3/2}F^3\) 不能代替它，因为曲率能量中的实际反应权重是 \(aF^3\)。

---

## 3. \(q=3\)：文中 (6.2) 应替换为线性吸收

设

\[
Y(t)=\int\eta^2aF^3=\int aF^3.
\]

正确的耗散权重应明确写为，例如

\[
D_3:=\int\eta^2a^2F|\nabla\Rm|^2,
\]

等价地可按常数比较为
\(\int\eta^2a^2|\nabla F^{3/2}|^2\)。

预期的固定指数张量不等式是

\[
Y'+cD_3
\le Cr^{-2}Y+C I_4,
\qquad
I_4:=\int\eta^2a^2F^4.
\tag{L3}
\]

Step 24 的

\[
I_4\le\varepsilon D_3+
C(r^{-2}+A_\Omega^4Y)Y
\tag{6.2}
\]

没有由所给笔记推导出来。尤其使用
\(\sqrt a\,F^{3/2}=\chi F^{3/2}\) 会产生

\[
\int|\nabla\chi|^2F^3,
\]

而该项不能统一由
\(r^{-2}\int\chi^2F^3=r^{-2}Y\) 控制；紧支撑 cutoff 不满足
\(|\nabla\chi|\lesssim r^{-1}\chi\)。

正确而更强的修复是取

\[
u=\eta aF^{3/2}.
\]

由于 \(\eta=1\) 于 active support，

\[
I_4=\int F\,u^2
\le \|F\|_{L^2(\operatorname{supp}\chi)}
   \|u\|_{L^4}^2.
\]

并且

\[
\|\nabla u\|_2^2
\le C D_3+C\int|\nabla a|^2F^3
\le C D_3+Cr^{-2}Y,
\]

因为

\[
|\nabla a|^2=4a|\nabla\chi|^2
\le Cr^{-2}a.
\]

于是

\[
\boxed{
I_4\le C\beta(t)\bigl(D_3+r^{-2}Y\bigr).
}
\tag{R3}
\]

固定 \(q=3\) 后，选择 \(r\) 使 \(C\beta<c/2\)，由 (L3)–(R3) 得

\[
Y'\le Cr^{-2}Y.
\tag{P3}
\]

因此不需要文中的 Riccati 项 \(A_\Omega^4Y^2\)。即使另有正确推导能得到该较弱 Riccati 不等式，其积分系数可由 (Cubic) 控制，传播仍不循环；但目前最干净且由现有结构直接支持的是线性形式 (P3)。

---

## 4. 时间平均传播是否合法？

修复 \(q=3\) 估计后是合法的。

由 (Cubic)，对每个 \(0<t\le T\)，存在 \(s_0\in[t/2,t]\) 使

\[
A_\Omega^4Y(s_0)
\le \frac{2}{t}
A_\Omega^4\int_{t/2}^{t}Y(s)\,ds
\le \frac{C\beta_*^3}{t}.
\]

时间平均本身只控制某个中间时刻，不能直接推出端点 \(t\)。真正 load-bearing 的第二步是 (P3)：

\[
Y(t)\le
e^{Cr^{-2}(t-s_0)}Y(s_0)
\le e^{C\theta}Y(s_0).
\]

所以

\[
\boxed{
A_\Omega^4Y(t)
\le \frac{C\beta_*^3}{t},
\qquad 0<t\le\theta r^2.
}
\]

因此 Step 24 的最终尺度正确，但 Section 6 应以线性临界吸收取代未经证明的“spatially subcritical”二次估计。

---

## 5. 三角形 \(Q\) 估计

令

\[
Q=\int\eta^2|E|^2,\qquad
X=\int\eta^2a|\nabla E|^2.
\]

使用组合变量 \(E=\Ric+g\) 至关重要。因为流速是 \(-2aE\)，其演化具有齐次结构

\[
\partial_tE
=a\Delta_LE-2aE
+(\nabla a)*\nabla E
+(\nabla^2a)*E
+a(\Rm*E)+a(E*E),
\]

所有项都含 \(E\) 或 \(\nabla E\)。因此 \(E=0\) 时流完全静止，不可能残留独立的 \((\nabla^2a)*g\) 源项。Step 22 所称 normalization 产生独立加性源与这一精确 stationarity 不相容；该说法应废弃。

测试后预期得到

\[
Q'+cX
\le Cr^{-2}Q+C\int\eta^2aF|E|^2.
\tag{Q1}
\]

其中：

- 主项产生 \(X\)；
- \((\nabla^2a)*E\) 分部积分后由
  \(|\nabla a|^2/a=4|\nabla\chi|^2\)
  给出 \(\varepsilon X+Cr^{-2}Q\)；
- \(\nabla\eta\) 交叉项因 collar 支持恒等式消失；
- Lichnerowicz 曲率、\(E*E\)、张量范数与体积元变化都由
  \(CaF|E|^2\) 控制，因为 \(|E|\le CF\)。

势项用 \(w=\eta\chi E\)：

\[
\int aF|E|^2
\le \|F\|_2\|\chi E\|_4^2
\le C\beta(t)\bigl(X+r^{-2}Q\bigr).
\tag{Q2}
\]

临界小量吸收后

\[
Q'\le Cr^{-2}Q.
\]

所以局部三角结构无明显遗漏项，也没有 curvature-only 加性源。但 (Q1) 仍需完整 index-level 推导，尤其要核对当前度量下的张量缩并、体积变化和 \(\Delta_L\) 约定。

另外，若支持彼此不交，active 区域的 \(Q\) 可直接求和，外部因 \(a=0\) 而冻结；这并不控制未选区域原本已有的缺陷。全局拓扑重新标定仍需要额外的 selected-volume/density 与初始缺陷输入。

---

## 6. 仍然 load-bearing 的精确命题

1. **演化中的 Sobolev 控制**
   \[
   \|u\|_{L^4(g(t))}^2
   \le C A_\Omega^2
   \left(\|\nabla u\|_{L^2(g(t))}^2+
   r^{-2}\|u\|_{L^2(g(t))}^2\right)
   \]
   以及 \(|\nabla\chi|_{g(t)}\le Cr^{-1}\)，常数在
   \(0\le t\le\theta r^2\) 上统一。

2. **精确 \(q=2\) 张量不等式** (L2)，包括
   \(\nabla^2a\)、metric-norm 和 volume-form 项。

3. **精确 \(q=3\) 张量不等式** (L3)，明确
   \(D_3\) 的 \(a^2\) 权重，并采用修正后的 (R3)。

4. **精确缺陷不等式** (Q1)，确认无独立于 \(E\) 的源项。

5. **统一光滑存在时间与度量等价性**，至少覆盖
   \([0,\theta r^2]\)。仅有临界 \(L^2\) 持续性并不直接给出点态流速控制，因此不能把 evolving Sobolev 常数的保持视为自动结论。

6. **静态 packing/coloring 与密度桥梁**：既要保留确定比例的互不相交 selected plateaux，也要说明其局部 \(Q\) 控制如何满足最终所需的全局归一化缺陷条件。

脚本只验证了支持关系、尺度和单项式账本：

\[
\beta\sim r^2\sqrt{1+K_0},\qquad
A_\Omega^4\int Y\sim\beta^3,\qquad
A_\Omega^4Y(t)\sim\beta^3/t.
\]

它不验证张量演化、\(q=3\) 反应结构、演化 Sobolev 常数、流存在时间或体积保留选择。

**最终核验结论：** buffered \(\chi/\eta\) 结构在单个 selected good support 上确实消除了 bad-center/all-center smallness；\(aF^3\) 是正确的加权三次矩；时间平均传播在补入修正后的前向 \(q=3\) 估计后成立；三角形 \(Q\) 结构可信且无曲率独立源。当前关键缺口不是支持几何，而是上述三个精确张量能量不等式、演化几何控制，以及从 selected supports 到全局归一化缺陷的密度桥梁。
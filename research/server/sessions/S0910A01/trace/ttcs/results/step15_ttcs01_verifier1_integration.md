# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 15,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step15_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step15_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the cutoff-smoothing accessibility architecture for the negative branch of Yau Problem 26 in dimension 4. The architecture claims: (A) For a sequence of closed 4-manifolds (M_i, g_i) with Ric_{g_i}+g_i -> 0 in C^0 and no Einstein metric, a normalized cutoff flow d_t g = -2 chi^2(Ric+g) on the closed manifold produces bounded curvature on a definite volume proportion while preserving global near-Einstein. (B) Calibration recovery: the LeBrun mixed SW estimate and Chern-Gauss-Bonnet applied to the smoothed metric g_i(t) give the SAME near-saturation profile because topology and near-Einstein are preserved. (C) The Li all-centers condition is satisfied at all covering centers inside the good set because the comparable-ball Bishop-Gromov ratio V_{-1}(13r*/2)/V_{-1}(r*) is bounded (~1785 in 4D), making r*^4 * C_BG * K_0 small for small r*, regardless of collapse. Verify each component and identify any gaps or errors: (1) Is the calibration recovery correct? Are there any subtleties about Seiberg-Witten invariants changing under the flow? (2) Is the BG transfer chain correct? The maximal function at p gives fint_{B_{4r*}(p)} |Rm|^2 <= K_0; for y within 5r*/2 of p, B_{r*}(y) subset B_{4r*}(p), so int_{B_{r*}(y)} <= K_0 Vol(B_{4r*}(p)); BG gives Vol(B_{4r*}(p))/Vol(B_{r*}(y)) <= C_BG. (3) Does the cutoff flow actually have short-time existence (degenerate parabolicity where chi=0)? (4) Does bounded curvature + collapse give CFG chart accessibility for the forbidden-germ argument? (5) Is the volume contradiction valid: definite proportion of accessible points vs vanishing proportion from calibrated defect?

## Integrated Scientific Memo

# 核验结论

该 cutoff–smoothing 架构目前是一个**有希望但未闭合的条件性反证框架**：

- **(C) Bishop–Gromov 可比球转移成立**，确实不依赖非塌缩。
- **(B) 拓扑重新校准机制成立**，但前提是终端闭度量具有**全局** near-Einstein 控制（至少全局 \(L^2\) traceless-Ricci 缺陷为 \(o(A_i)\)），并且必须恢复完整的谱退化余项，而不只是一个标量平方项。
- **(A) 尚未证明**：缺少 collapse-uniform 的局部 cutoff-flow 能量闭合、统一存在时间以及过渡环带中的全局 Einstein 缺陷传播。
- “平台上有界全曲率 \(\Rightarrow\) 固定参数 CFG chart accessibility”是正确方向，但提供的材料没有给出足够精确、统一的局部正规覆盖定理；不能简单视为自动成立。
- 最终体积矛盾的逻辑正确，但完全依赖上述分析和塌缩几何输入。

---

## 1. Calibration recovery 与 Seiberg–Witten

令终端度量 \(h_i=g_i(t_0)\)，并定义
\[
I_i(h_i)=\frac1{4\pi^2}\int_{M_i}
\left(\frac{s_{h_i}^2}{24}+2|W^+_{h_i}|^2\right)d\mu_{h_i},
\]
\[
J_i(h_i)=\frac1{4\pi^2}\int_{M_i}
\frac{|\mathring{\operatorname{Ric}}_{h_i}|^2}{2}\,d\mu_{h_i}.
\]
对任意光滑度量，Chern–Weil 恒等式给出
\[
I_i-J_i=2\chi(M_i)+3\tau(M_i)=A_i-k_i.
\]

### SW 不变量不会因流改变

cutoff flow 只是在同一个闭光滑流形上改变度量，不改变：

- 光滑结构和取向；
- 交叉形式；
- Spin\(^c\) 结构；
- Seiberg–Witten 基本类。

因此不存在“SW 不变量沿流改变”的问题。对每个终端度量可以重新选择吹起类
\[
a_\varepsilon=c_1(X_i)+\sum_j\varepsilon_jE_j
\]
的符号，使
\[
(a_i^+)^2\ge A_i.
\]
无需沿流固定同一个符号选择。

此外 \(A_i\to\infty\) 时，BMY 与
\[
b^+(X_i)=1+2p_g(X_i)
\]
说明尾部序列有 \(b^+>1\)，故没有 \(b^+=1\) 的 chamber 微妙性。

### 正确的条件性恢复

若至少有
\[
J_i(h_i)=o(A_i),
\]
则
\[
I_i(h_i)=A_i-k_i+J_i(h_i)=\frac23A_i+o(A_i).
\]
LeBrun 混合估计给出
\[
D_{a,i}:=I_i-\frac23(a_i^+)^2\ge0,
\]
同时
\[
D_{a,i}\le \frac{A_i}{3}-k_i+J_i=o(A_i).
\]
因此可在 \(h_i\) 上重新运行等号余项分析；无需比较 \(W^+(g_i(t_0))\) 与 \(W^+(g_i(0))\)。

若已有全局点态估计
\[
\|\operatorname{Ric}_{h_i}+h_i\|_\infty\le C\delta_i,
\]
则先由 \(s=-4+O(\delta_i)\) 和 Chern–Weil 得到
\[
\operatorname{Vol}(M_i,h_i)=O(A_i),
\]
进而
\[
J_i(h_i)\le C\delta_i^2\operatorname{Vol}(M_i,h_i)=o(A_i).
\]
所以不应先验假设终端体积渐近；它可由 near-Einstein 与拓扑吸收得到。

### 需要修正的谱余项

仅有
\[
\int (s+8\sqrt6\,|W^+|)^2=o(A_i)
\]
并不足以推出
\[
\operatorname{Spec}(W^+)\to
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
它只控制 \(s\) 与 \(|W^+|\) 的校准关系。还必须重新得到控制两个相等特征值的非负余项，例如 Step 11 中的
\[
\mathcal G=f^2-(a_-)^2
\]
或等价的谱投影余项，并证明其积分也是 \(o(A_i)\)。只有完整的等号分解由 \(D_{a,i}\) 控制时，“相同 calibrated profile”才严格成立。

**结论：** calibration recovery 的拓扑机制正确；真正缺失的是终端度量上的全局 Ricci 缺陷控制以及完整谱余项的重新执行，而不是 SW 沿流输运。

---

## 2. Bishop–Gromov 转移链

设
\[
\mathcal M_R(|\operatorname{Rm}|^2)(p)\le K_0,\qquad 4r_*\le R,
\]
且
\[
d(p,y)\le\frac52r_*.
\]
则
\[
B_{r_*}(y)\subset B_{\frac72r_*}(p)\subset B_{4r_*}(p),
\]
故
\[
\int_{B_{r_*}(y)}|\operatorname{Rm}|^2
\le K_0\,\operatorname{Vol}(B_{4r_*}(p)).
\]
又因为
\[
B_{4r_*}(p)\subset B_{\frac{13}{2}r_*}(y),
\]
在 \(\operatorname{Ric}\ge-3g\) 下，Bishop–Gromov 给出
\[
\frac{\operatorname{Vol}(B_{4r_*}(p))}
     {\operatorname{Vol}(B_{r_*}(y))}
\le
\frac{V_{-1}(\frac{13}{2}r_*)}{V_{-1}(r_*)}.
\]
因此
\[
r_*^4\fint_{B_{r_*}(y)}|\operatorname{Rm}|^2
\le
r_*^4K_0
\frac{V_{-1}(\frac{13}{2}r_*)}{V_{-1}(r_*)}.
\]

当 \(r_*\downarrow0\) 时，
\[
\frac{V_{-1}(\frac{13}{2}r_*)}{V_{-1}(r_*)}
\longrightarrow
\left(\frac{13}{2}\right)^4=1785.0625.
\]
对正的 \(r_*\)，该比值并不严格等于或必然小于 \(1785\)。正确做法是先取 \(r_0>0\)，令
\[
C_0=\sup_{0<r\le r_0}
\frac{V_{-1}(\frac{13}{2}r)}{V_{-1}(r)}<\infty,
\]
再选择
\[
r_*\le
\min\left\{r_0,\left(\frac{\varepsilon_{\rm Li}}
{2C_0K_0}\right)^{1/4}\right\}.
\]

这确实与塌缩无关：只用了**可比半径球的相对体积比**，没有绝对体积下界。相应的 Sobolev–能量乘积也有消去：
\[
C_S(B_{r_*})\|\operatorname{Rm}\|_{L^2(B_{r_*})}
\le
Cr_*^2\left(\fint_{B_{r_*}}|\operatorname{Rm}|^2\right)^{1/2}.
\]

但这只验证了 Li 的**初始局部 all-centers 小量条件**。Li 已发表的定理使用全流形中心的 supremum 和延拓论证，不能直接从一个缓冲 good ball 调用。

此外，\(\rho\) 与 \(r_*\) 必须统一。若希望平台、缓冲区和上述 \(13/2\) 计算完全匹配，可例如取 \(\rho=8r_*\)，或重新计算更大中心区域所需的可比球常数。

---

## 3. 退化 cutoff flow 的短时存在

方程
\[
\partial_tg=-2\chi^2(\operatorname{Ric}+g)
\]
在 \(\chi=0\) 处退化，DeTurck 后的主符号仍为 \(\chi^2\Delta\)，故不能直接称为标准一致抛物系统。

Yang 型 local Ricci flow 理论支持：对每个固定的光滑初始度量和 cutoff，存在某个短时局部流；加入正规化低阶项 \(-2\chi^2g\) 不改变主要存在机制。然而，这并未自动给出本架构所需的：

\[
T\ge c r_*^2
\]
且 \(c\) 与 \(i\) 无关，以及在该时间内的统一能量、度量等价和缺陷估计。普通存在时间可能依赖于初始 \(\sup|\operatorname{Rm}|\)、cutoff 几何和过渡环带数据，而这些在序列中不受控。

正则化
\[
a_\varepsilon=\chi^2+\varepsilon^2
\]
使方程一致抛物，但不能仅凭“外部移动率为 \(O(\varepsilon^2\delta_i)\)”通过极限，因为该说法已经预设
\[
|E(t)|=O(\delta_i).
\]
要令 \(\varepsilon\to0\)，仍需与 \(\varepsilon\) 无关的统一时间及估计。

还有一个技术点：仅由 Ricci 下界通常不能直接构造具有统一
\[
|\nabla^2\chi|\le C\rho^{-2}
\]
的光滑 cutoff。A03 的积分恒等式通过分部积分消除了 cutoff Hessian，这有助于能量法，但不等于完整的存在理论。

因此：

- **固定 \(i\) 的裸存在性：有可靠支持；**
- **架构所需的 collapse-uniform existence-with-estimates：未证明。**

---

## 4. 平台曲率与全局 Einstein 缺陷

A03 验证了
\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E),\qquad a=\chi^2,
\]
且 \(\mathcal C_a(E)\) 的每项均含 \(E,\nabla E\) 或其迹。因此：

- \(E\equiv0\) 时流确实静止；
- \(\chi=0\) 的开集确实完全冻结；
- cutoff 不产生与 \(E\) 无关的加性误差。

但“同次性”并不推出
\[
\|E(t)\|_\infty\le C\|E(0)\|_\infty.
\]
过渡环带含有
\[
d\chi*\nabla E,\qquad \nabla^2\chi*E
\]
等项，而初始假设没有控制 \(\nabla E\)。同样，
\[
\partial_t\operatorname{Rm}\sim\nabla^2(aE)+\operatorname{Rm}*aE
\]
表明笔记中所谓环带曲率改变
\[
O(|d\chi|^2\delta_i^2t)
\]
没有依据。

在 \(\chi=1\) 的平台内部，若局部 Li bootstrap 已给出
\[
|\operatorname{Rm}|\le C/t,
\]
则 Li Corollary 3.5 可条件性地推出
\[
|E(x,t)|\le C\delta_i
\left(\frac{r_*^2}{t}\right)^{2/3},
\]
并在 \(t_0=\theta r_*^2\) 得到
\[
|E(x,t_0)|\le C_\theta\delta_i,\qquad
|\log(g(t_0)/g(0))|=O(\delta_i r_*^2).
\]
该缩放和两次体积消去都是正确的。但这一结论仅覆盖有缓冲的平台内部，不能自动覆盖 transition annuli。

于是当前有两个不同的分析缺口：

1. **局部曲率能量 bootstrap：**
   \[
   \sup_{B_{\rho/8}(p)}|\operatorname{Rm}(t)|\le C/t
   \]
   在 collapse-uniform、buffered、all-centers-only-locally 的条件下成立；

2. **过渡环带上的全局缺陷传播：**
   \[
   \|\operatorname{Ric}_{g_i(t_0)}+g_i(t_0)\|_\infty
   \le C\delta_i,
   \]
   或至少足够用于校准的较弱结论
   \[
   \int_{M_i}|\mathring{\operatorname{Ric}}_{g_i(t_0)}|^2=o(A_i).
   \]

第二项不能由第一项的平台估计代替，因为过渡环带可能占固定体积比例。

---

## 5. 有界曲率与 CFG chart accessibility

平台上若在固定缓冲尺度内已有
\[
|\operatorname{Rm}|\le\Lambda,
\]
则确实进入 bounded-sectional-curvature collapse 理论的适用范围。这消除了原先仅有 bounded Ricci 或 mean \(L^2\) curvature 时的 Hessian spikes 问题。

不过，提供的文本尚未严格证明：

> 存在仅依赖 \(n,\Lambda\) 和缓冲尺度的固定 \(h,v>0\)，使平台内固定体积比例的点具有 Step 11 所需的正规覆盖、覆盖球体积下界和 harmonic-radius 下界。

CFG 通常给出 N-structure、正则分层及局部 infranil 纤维化；要转化为这里的 \((h,v)\)-accessibility，还需明确：

- 选择的覆盖必须是适于平均输运的正规覆盖；
- 提升后的固定尺度体积有统一下界；
- harmonic radius 有统一下界；
- 奇异纤维、可收缩短轨道和 rank-drop 集不会吞掉全部平台体积；
- 所有常数只依赖 \(\Lambda\) 和缓冲尺度，而不依赖 \(i\)。

Naber–Zhang 的相应结论还要求 residual dimension 和 maximal fibered nilpotency rank；Section 6.2 并未验证这些条件。因此，“有界全曲率是正确入口”成立，但“所有平台点自动可访问”仍属过强表述。需要一个精确的局部定量 CFG/正规覆盖定理，或只证明平台内固定比例的 regular points 可访问。

---

## 6. 最终体积矛盾

若以下三项均成立：

1. 平台内部在 \(t_0\) 有统一 \(|\operatorname{Rm}|\) 上界和 bilipschitz 控制；
2. 终端闭度量有全局 \(J_i=o(A_i)\)，并恢复完整 calibrated defect
   \[
   \int F_{g_i(t_0)}=o(A_i);
   \]
3. CFG 层产生固定 \(h,v\) 的 chart-accessible 集，其体积比例至少 \(c_0>0\)；

则最终矛盾有效。

Vitali packing 和同中心 Bishop–Gromov 比较给出平台内部初始体积的固定比例；bilipschitz 控制将该比例传到 \(t_0\)。完整 calibration 与全局 Ricci 下界使 Step 11 的最大函数选点、正规覆盖平均输运和 forbidden-germ 紧致性论证适用于 \(g_i(t_0)\)，从而
\[
\frac{\operatorname{Vol}\mathcal A_i(h,v)}
{\operatorname{Vol}(M_i,g_i(t_0))}\to0.
\]
这与 CFG 给出的
\[
\frac{\operatorname{Vol}\mathcal A_i(h,v)}
{\operatorname{Vol}(M_i,g_i(t_0))}\ge c_0
\]
矛盾。

所以体积计数本身没有新的逻辑错误；它是条件性的，而不是当前已完成的反证。

---

## 精确剩余对象

目前需要证明的核心对象可压缩为三个：

1. **Collapse-uniform localized Li theorem：**  
   在缓冲 good ball 内只有局部 all-centers 初始无量纲 \(L^2\) 小量时，对退化 normalized cutoff flow 获得统一 \(T\asymp r_*^2\)、能量延拓、度量等价和内部 \(C/t\) 曲率估计。

2. **Transition-inclusive defect theorem：**  
   利用 cutoff 方程的同次结构，控制所有 transition annuli，得到全局
   \[
   \|E(t_0)\|_\infty=O(\delta_i)
   \]
   或至少
   \[
   \|\mathring{\operatorname{Ric}}(t_0)\|_{L^2}^2=o(A_i).
   \]

3. **Quantitative bounded-curvature accessibility theorem：**  
   将固定缓冲球上的 \(|\operatorname{Rm}|\le\Lambda\) 转化为固定体积比例的正规覆盖 \((h,v)\)-chart accessibility，明确处理 rank drop 和奇异纤维。

因此 Step 15 的状态表中，“cutoff flow existence established”“CFG accessibility established”“calibration recovery established”都应分别改为：

- 裸存在性有支持，但统一 estimates-package 未建立；
- bounded curvature 是 CFG 的正确输入，但所需固定比例正规覆盖结论未写出；
- calibration 的拓扑重做正确，但依赖尚未证明的全局终端缺陷估计和完整谱余项。
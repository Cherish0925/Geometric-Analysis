# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 21,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step21_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step21_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

The derivative-free first-exit framework reduces the 4D negative-branch cutoff-flow program to one PDE task: the localized zero-order Moser iteration for the degenerate normalized cutoff flow. Consider what alternative approaches or structural insights could bypass or simplify this remaining PDE localization.

Specifically: (A) Wang's proof is for the unnormalized cutoff Ricci flow on a complete manifold with global Sobolev and energy bounds. The needed adaptation is to finite-neighbor domains with normalized flow. What is the simplest way to extract the needed local estimates? Could the completed-manifold trick (extend the closed manifold trivially and apply Wang's global theorem) work? Could a time-layer argument avoid the nested-cutoff/evolving-measure complexity?

(B) Is there a more direct route to the calibrated contradiction that avoids the full Moser iteration? For example: if one only needs |Rm| bounded at some positive time on the plateau (not the sharp C/t rate), could a softer estimate suffice? The downstream needs are: (i) smooth compactness at fixed time T_0, (ii) defect → 0 on the limit, (iii) |W+| = 1/(2sqrt6) on the limit.

(C) A02's CZ spike audit shows that the weighted estimate is not broken by singular-kernel transplants. Could this stability property be used constructively to prove the estimate, e.g., by showing that the heat kernel of the degenerate operator dt - chi^2 Delta smooths faster than it generates curvature?

## Integrated Scientific Memo

## 核心结论

最稳妥的简化不是把原闭流形“平凡延拓”后直接套用 Wang 的全局定理，而是：

1. **把局部张量能量不等式先压缩成一个抽象的非自治 Nash/热半群引理**；
2. 只证明下游真正需要的两个较软估计：
   \[
   \|\chi^2\Rm(t)\|_\infty\lesssim t^{-1},
   \qquad
   \|\chi^2E(t)\|_\infty\lesssim \delta\,t^{-1/2},
   \quad E=\Ric+g,
   \]
   第二个速率虽弱于原来的 \(t^{-1/3}\)，但对度量漂移仍可积；
3. 在固定正时间层 \([T_0/2,T_0]\) 上，用平台内普通 normalized Ricci flow 的 Shi 估计完成光滑紧性；
4. 保留 Step 20 的三角形全局 \(L^2\)-缺陷估计来完成校准。

这可以消除完整的 \(q\mapsto3q/2\)、\(m\mapsto3m/2\) 无限 Moser 迭代；但**不能仅凭现有材料直接宣称半群估计已经成立**。最关键的剩余对象是：由真实的加权张量弱方程构造一个统一的非自治闭扇形形式，并证明其 Nash 超收缩估计。

---

## A. 完成流形技巧：什么不行，什么值得保留

### 1. 平凡使用原闭流形不能套 Wang 的全局定理

Wang 的全局假设会看到
\[
A_{\rm glob}^{2}\|\Rm\|_{L^2(M)},
\]
而现有小量只是逐球或有限邻域的小临界能量。流在 \(\{\chi=0\}\) 上静止，并不使该区域的曲率从 Wang 的全局假设中消失。给局部区域粘帽也无明显帮助，因为四维
\[
\int |\Rm|^2
\]
具有临界尺度不变性，缩放帽子不能自动制造小能量。

因此，“把闭流形平凡延拓并直接调用 Wang”不能解决局部化。

### 2. 加权测度确实揭示了一个有用的全局形式结构

令
\[
a=\chi^2,\qquad \Omega=\{a>0\},\qquad
d\nu_t=a^{-2}d\mu_{g(t)},
\]
以及
\[
\mathcal K=aF,\quad F=(1+|\Rm|^2)^{1/2},
\qquad
\mathcal U=a|E|.
\]
则 Step 20 的矩恰好变为
\[
H_q=\int_\Omega \mathcal K^q\,d\nu_t,
\qquad
J_m=\int_\Omega \mathcal U^m\,d\nu_t.
\]
这不是形式巧合：四维共形体积因子正是 \(a^{-2}\)。

若令
\[
\widehat g=a^{-1}g=\chi^{-2}g,
\]
则 \(d\nu=d\mu_{\widehat g}\)。不过必须修正一个细节：

> \(\widehat g\) 的完备性不能仅由“光滑 cutoff 至多线性消失”推出。

真正需要的是沿零集
\[
\int \frac{ds}{\chi(s)}=\infty.
\]
标准 cutoff 若线性或更高阶消失通常满足此条件；任意平坦或非标准消失仍应单独核验。更重要的是，即使 \(\widehat g\) 完备，其几何可能具有无界曲率或退化注入半径，因此这仍不是对 Wang 原定理的直接应用。

### 3. 正确的分析对象是 ground-state 型二次形式

原局部 Sobolev 不等式给出
\[
\|\phi\|_{L^4(\nu_t)}^2
=
\|a^{-1/2}\phi\|_{L^4(\mu_t)}^2
\le C A^2\,\mathfrak e_t[\phi],
\]
其中可取
\[
\mathfrak e_t[\phi]
=
\int_\Omega
\left|\nabla(a^{-1/2}\phi)\right|^2\,d\mu_t
+r^{-2}\|\phi\|_{L^2(\nu_t)}^2.
\]
于是曲率势满足
\[
\int_\Omega \mathcal K\phi^2\,d\nu_t
\le
\|\mathcal K\|_{L^2(\nu_t)}
\|\phi\|_{L^4(\nu_t)}^2
\le
C A^2\|\mathcal K\|_{L^2(\nu_t)}\,
\mathfrak e_t[\phi].
\]
而
\[
\|\mathcal K\|_{L^2(\nu_t)}^2
=\int_\Omega F^2\,d\mu_t,
\]
故相对形式界正是 Step 19–20 的无塌缩体积依赖参数 \(\gamma\)。当 \(C\gamma<1\) 时，曲率反应是扩散形式的严格次从属扰动。

这也是 CZ spike 稳定性的建设性内容：尖峰可以点态很高，但对任意能量模态只能消耗扩散形式的一个固定小比例。

### 4. 不能跳过的技术核验

不能仅从上述代数直接断言存在满足
\[
\|P(t,s)\|_{2\to\infty}
\le CA^2(t-s)^{-1}e^{C(t-s)(1+r^{-2})}
\tag{1}
\]
的演化族。必须从真实的张量弱方程核验：

- 主部与 \(\mathfrak e_t\) 的对应关系；
- 一阶 \(da\)-项的扇形估计；
- \(\partial_t\nu_t/\nu_t=-\tr(aE)\) 的处理；
- 时变 Hilbert 空间 \(L^2(\nu_t)\) 的同一化；
- 向量值系统到标量支配或 Kato 型不等式；
- 归一化项仅贡献 \(Cr^{-2}+C\) 的低阶界；
- 零集处形式闭性、稠密性以及无边界通量。

好消息是
\[
\frac{|da|^2}{a}=4|d\chi|^2\le Cr^{-2}
\]
消除了显式的 cutoff 奇性；这正是 Nash 路线可能比嵌套 cutoff 更短的原因。

---

## B. 下游不需要完整的尖锐 Moser 层级

### 1. 曲率只需在终端时间层有界

为了在 \(T_0>0\) 取得光滑紧性，只需
\[
\sup_{P_{\rm inner}\times[T_0/2,T_0]}|\Rm|<C(T_0),
\]
不必从 \(t=0\) 开始维持最优常数的 \(C\gamma/t\) 估计。

若抽象半群引理 (1) 可用于曲率标量弱不等式，则由 \(L^2\to L^\infty\) 平滑得到
\[
\|\mathcal K(t)\|_\infty
\lesssim
A^2t^{-1}\|\mathcal K(0)\|_{L^2(\nu_0)}
+C(1+r^{-2}).
\]
在平台 \(a=1\) 上，这给出固定正时间层的普通曲率界。随后直接应用平台内 normalized Ricci flow 的 Shi 内部估计，即得 \(T_0\) 时刻所有曲率导数的一致界。

因此曲率部分可以由**一次 Nash 超收缩**替代完整高指数迭代。

### 2. 缺陷只需 \(t^{-1/2}\)，不必达到 \(t^{-1/3}\)

令
\[
w=|\mathcal U|^2=|aE|^2.
\]
缺陷方程对 \(E\) 是齐次的；若其标量化弱不等式由同一形式和曲率势控制，则对 \(w\) 应用一次 \(L^2\to L^\infty\) 平滑给出
\[
\|\mathcal U(t)\|_\infty
\lesssim
A\,t^{-1/2}
\|\mathcal U(0)\|_{L^4(\nu_0)}.
\]
而
\[
\|\mathcal U(0)\|_{L^4(\nu_0)}^4
=\int a^2|E(0)|^4\,d\mu_0
\le \delta^4V.
\]
结合
\[
A\lesssim rV^{-1/4},
\]
得到
\[
\boxed{
\|aE(t)\|_\infty
\lesssim
\delta r\,t^{-1/2}
=
\delta\left(\frac{r^2}{t}\right)^{1/2}.
}
\tag{2}
\]
尽管 (2) 比 Step 20 的 \(t^{-1/3}\) 更差，但
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\lesssim
\delta r^2\sqrt{\theta},
\]
仍足以严格改善度量可比性。因此从 first-exit 角度，基指数 \(J_4\) 已经足够，不必使用 \(J_6\) 和无限缺陷迭代。

### 3. 固定时刻的 Einstein 缺陷有两条路线

在 \(T_0\) 固定后，可由 (2) 直接得到
\[
\|E(T_0)\|_{L^\infty(P)}\to0.
\]
或者更保守地：

1. 用 Step 20 的三角形系统保持
   \[
   Q_i(t)=\int_M|E_i(t)|^2d\mu_{g_i(t)}
   \le C Q_i(0)\to0;
   \]
2. 在平台终端时间层已有曲率界后，对普通缺陷方程使用局部 \(L^2\to L^\infty\) 平滑。

第二条路线将退化问题限制在曲率平滑和度量漂移，通常更稳健。

### 4. 校准仍需要全局 \(L^2\) 控制

点态 \(aE\) 估计不能控制过渡区中的未加权 \(E\)。因此 Step 20 的三角形无加性误差估计
\[
\frac d{dt}Q_\alpha
\le Cr^{-2}\sum_{\beta\sim\alpha}Q_\beta
\]
仍是必要的。终端光滑收敛给出局部点态极限，而
\[
Q_i(T_0)\to0
\]
和 \(7/24\) 完全平方不等式负责传递
\[
|W_\infty^+|\equiv\frac1{2\sqrt6}.
\]

---

## C. 时间层方法能简化什么，不能简化什么

在每个目标时刻 \(t\) 上，仅在
\[
[t/2,t]
\]
做正时间平滑，可避免：

- 从 \(0\) 积分 \(1/t\) 势所产生的非可积 Grönwall；
- 追踪从初始时刻开始的曲率导数；
- 终端正则性所不需要的尖锐早时行为。

但时间层不能单独消除空间泄漏：若仍使用有边界局部球，空间 cutoff 误差依然存在。它必须与以下之一结合：

1. 加权测度上的闭形式方法；
2. 无边界的共形完成；
3. 有统一缓冲的有限邻域 Dirichlet/Neumann 形式。

因此“时间层”应视为半群方法的自然实现方式，而不是独立的局部化证明。

---

## D. 有限邻域的最短处理方式

覆盖图具有有界度数，着色可使同色的充分扩张支持两两不交。对每种颜色取 cutoff 分量之和后，形式成为分量的直和。若每个分量满足统一的小能量与 Sobolev 界，则：

- 直和形式的 \(2\to\infty\) 算子范数是分量范数的上确界；
- 全部组件的总 \(L^2\) 曲率可以很大，并不影响逐组件的相对形式小量；
- 无需写有限邻居矩阵的无限指数递推。

但必须确保**扩张后的影响区也不相交**；仅原球不相交不够。若整个几何构造要求多个颜色的 cutoff 同时活动，则颜色不能直接彼此解耦；更安全的表述是：着色用于逐批建立局部估计，再由有界颜色数恢复统一常数，而非自动把原单个流分裂成独立流。

---

## E. CZ 稳定性应如何用于证明

合适的表达不是逐点比较“热核平滑速度”和“曲率产生速度”，而是相对形式不等式
\[
\int \mathcal K\phi^2\,d\nu
\le
\varepsilon\,\mathfrak e[\phi]
+Cr^{-2}\|\phi\|_2^2,
\qquad \varepsilon<1.
\tag{3}
\]
(3) 意味着任何奇异核型尖峰对反应项的贡献都被扩散能量吸收。直接 Duhamel 法反而处在四维临界端点：
\[
\|P_t\|_{2\to\infty}\sim t^{-1},
\]
时间卷积容易产生对数发散。应把曲率势纳入生成元，用形式方法而不是把它作为外力迭代。

真正需要证明的抽象引理可精确表述为：

> 若非自治向量值形式 \(\mathfrak a_t\) 在 \(L^2(\nu_t)\) 上一致闭合并满足统一四维 Nash 不等式；其一阶反对称部分相对形式有界；势 \(V_t\) 满足 (3)；测度漂移也满足同类相对形式界，则相应演化族满足
> \[
> \|P(t,s)\|_{L^2(\nu_s)\to L^\infty(\nu_t)}
> \le
> CA^2(t-s)^{-1}
> e^{C(t-s)(1+r^{-2})}.
> \]

证明应由前向 \(L^2\) 能量、伴随演化的 \(L^2\) 能量、Nash 微分不等式和对偶性组成。它将嵌套空间 cutoff、嵌套时间层和指数乘积统一封装起来。

---

## 最小化后的 PDE 任务

原剩余任务可缩减为以下三个精确对象：

1. **曲率形式化：** 从 normalized cutoff flow 的真实张量方程推出 \(\mathcal K=aF\) 的标量弱不等式，并证明曲率势满足统一的小相对形式界。
2. **非自治 Nash 引理：** 在时变测度 \(a^{-2}d\mu_t\) 上建立上述 \(2\to\infty\) 估计，包括零集、扇形一阶项和向量值支配。
3. **缺陷与全局校准：**
   - 将同一平滑引理用于 \(w=|aE|^2\)，得到可积的 \(t^{-1/2}\) 度量漂移；
   - 独立保留并证明 Step 20 的有限邻域三角形未加权 \(Q\)-估计。

若第 2 项在共形完成上出现域或几何障碍，Step 20 已写出的 recurrence (11.1)–(11.4) 仍是可靠后备路线。两者共享同一个核心事实：四维临界曲率势是扩散形式的小扰动；区别只在于用 Nash 演化族一次性封装，还是用嵌套 Moser 指数显式展开。
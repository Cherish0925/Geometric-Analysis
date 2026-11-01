# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 38,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step38_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step38_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematical content of `step38_continuation_repair_and_support_normalization.md` in the restricted four-dimensional negative Yau-26 route. Focus on four questions: (1) Does the note correctly identify the failure of Step 37 Lemma 1.2a from the degeneracy of a=chi^2 and the fact that |U| only gives |aE|, not chi^2-small drift? (2) Is the proposed repair direction faithful to Wang Lemmas 4.5, 4.6, Proposition 4.13, and Proposition 4.14: weighted shifted equation for U=a(Rm+G), separate unweighted curvature-derivative module, finite Hölder exponents, and smooth terminal recovery via dt g=-2 Ric(U)? (3) Are there hidden derivative, cutoff, G/normalization, or exponent gaps in the sketched estimates that would still block a continuation theorem? (4) Is the support-selection normalization correct: volume-average maximal function, large threshold for retained volume, small fixed radius for r^4 average smallness, Sobolev-volume cancellation, and Vol/A lower from calibration rather than Euler upper bound? Give a scientific verification/critique and concrete repairs, not a route decision.

## Integrated Scientific Memo

# Step 38 数学核验结论

## 总评

Step 38 对 Step 37 核心错误的撤回是正确的，修复方向也忠实于 Wang 第 4 节的实际交错归纳：

\[
\text{加权 }U=a(\Rm+G)
\;\longleftrightarrow\;
\text{演化 cutoff jets}
\;\longleftrightarrow\;
\text{无权曲率导数}.
\]

支持选择部分的主要归一化——体积平均极大函数、大阈值保留体积、小固定半径产生 \(r^4\fint |\Rm|^2\) 小量、Sobolev–体积消去，以及由校准得到 \(\Vol/A\) 下界——基本正确。

但本文仍只是续接证明的正确框架，不是完整续接定理。尤其 (1.2)、shifted Proposition 4.13、终端固定坐标恢复以及重启短时存在尚未严格证明。另有一个明确错误：§4 对 \(m=2\) 的 \(\Gamma _3\) 不能用“低阶 \(\nabla U\) 已有 \(L^\infty\)”处理；它可以用有限指数和分部积分修复。

---

## 1. Step 37 Lemma 1.2a 的失效判断正确

设

\[
a=\chi^2,\qquad T=\Rm+G,\qquad U=aT.
\]

因 Ricci 收缩是有界线性映射，且按所选 \(G\) 的约定

\[
\Ric(T)=E=\Ric+g,
\]

故

\[
\Ric(U)=aE,\qquad |aE|\le C|U|.
\]

因此

\[
|U|\le K\quad\Longrightarrow\quad |aE|\le CK,
\]

绝不能推出

\[
|aE|\le CaK=C\chi^2K.
\]

取点态模型 \(a=\varepsilon^2\)、\(T=a^{-1}T_0\)，则 \(U=T_0\) 和
\(aE=\Ric(T_0)\) 均可为 \(O(1)\)，而 \(aK=O(\varepsilon^2)\)。所以在
\(\chi\ll1\) 的过渡区，流速有界但不随 \(\chi^2\) 变小。

真正成立的是对固定切向量 \(v\)

\[
\left|\frac d{dt}\log g_t(v,v)\right|
\le C|aE|\le CK,
\]

从而

\[
e^{-CK(t-\tau)}g(\tau)\le g(t)\le e^{CK(t-\tau)}g(\tau).
\]

这只给出双 Lipschitz 比较、体积比较及 \(|d\chi|_{g(t)}\) 有界，不能给出无权曲率导数。

关于 cutoff jets 的批评也正确：虽然 \(d\chi\) 与联络无关，但

\[
\nabla^2\chi=\partial^2\chi-\Gamma*d\chi
\]

及更高阶 \(\nabla^\ell\chi\) 依赖演化联络，而

\[
\partial_t\Gamma=g^{-1}*\nabla\Ric(U).
\]

固定坐标导数不能替代这些演化协变导数。因此按
\(\{\chi\ge\delta\}\cup\{\chi<\delta\}\) 分区，不能从 \(\nabla^kU\) 恢复过渡区的无权 \(\nabla^k\Rm\)。

---

## 2. 与 Wang Lemmas 4.5、4.6、Propositions 4.13、4.14 的对应

### 2.1 加权最高阶结构正确

Wang Lemma 4.5 演化的是

\[
\nabla^m(\chi^2\Rm),
\]

其高 cutoff 行中的曲率因子是

\[
\nabla^k(\chi^2\Rm),
\]

不是无权 \(\nabla^k\Rm\)。因此 shifted 对象必须取

\[
U=a(\Rm+G),
\]

而顶层 cutoff 分配应为

\[
\begin{aligned}
\Gamma_1&=\chi\nabla^{m+2}\chi*U,\\
\Gamma_2&=\nabla\chi*\nabla^{m+1}\chi*U,\\
\Gamma_3&=\chi\nabla^{m+1}\chi*\nabla U,\\
\Gamma_4&=\chi\nabla\chi*\nabla^{m+1}U.
\end{aligned}
\]

这与 Wang Proposition 4.14 的四项吻合，也是 Step 38 相对 Step 37 最重要的修正。

不过，(1.2) 尚不能视为已证明。必须固定 Kulkarni–Nomizu 约定并逐项验证，在四维确有

\[
G=\frac{g\owedge g}{6},\qquad \Ric(G)=g.
\]

虽然每个时刻 \(\nabla G=0\)，但

\[
\partial_tG
=\frac16\bigl((\partial_tg)\owedge g+g\owedge(\partial_tg)\bigr)\ne0.
\]

因为 \(\partial_tg=-2\Ric(U)\)，这些项预期只含当前阶或较低阶 \(U\) 导数；但这一点必须从完整曲率变分中实际证明，不能仅收入未定义的
\(\mathcal L_m^{G,\mathrm{norm}}\)。

### 2.2 cutoff-jet 方程方向正确，但显示式不够精确

更准确的张量结构为

\[
\partial_t\nabla^\ell\chi
=
\sum_{j=1}^{\ell-1}
\nabla^j\Ric(U)*\nabla^{\ell-j}\chi
\]

加低阶收缩项。计算范数及 \(L^p\) 能量时还会出现

\[
|U|\,|\nabla^\ell\chi|
\]

和体积元变化项。

例如 \(Z=\nabla^2\chi\)、\(V=\nabla U\) 时，

\[
\partial_tZ=\nabla U*d\chi
\]

在张量层面成立，而范数估计应写成

\[
\partial_t|Z|
\le C|V||d\chi|+C|U||Z|.
\]

所以 Step 38 的 (2.4) 中
\((|V|+|U||d\chi|)|Z|^{p-1}\) 并非准确的直接展开；应替换为

\[
\int |V||d\chi||Z|^{p-1}
+
\int |U||Z|^p.
\]

由于 \(|d\chi|\) 和 \(|U|\) 有界，最后的 Grönwall 结论不变。

### 2.3 无权模块必须独立证明

Step 38 不再除以 \(a\)，而恢复 Wang Proposition 4.13 型无权方程，这是正确的。严谨的交错顺序应为

\[
\|\Rm\|_{L^q}
\Longrightarrow
(\nabla U,\nabla^2\chi)
\Longrightarrow
\nabla\Rm
\Longrightarrow
(\nabla^2U,\nabla^3\chi)
\Longrightarrow\cdots .
\]

每一层应同时对所有充分大的有限指数成立，类似 Wang 的“所有 \(q>100\)”，而不必声称所有正指数。

Step 38 的代表性 Hölder 恒等式正确：

\[
\frac2{2p}+\frac2{2p}+\frac{p-2}{p}=1,
\qquad
\frac{N}{Np}+\frac{p-1}{p}=1.
\]

但脚本只验证了这些代数恒等式；其最后几个 PDE 检验直接设置为 `True`，不能作为张量演化或续接定理的证明。

---

## 3. 仍阻碍续接定理的具体缺口及修复

### 3.1 \(m=2\) 的 \(\Gamma_3\) 论证错误，但可修复

Step 38 称 \(m\ge2\) 时 \(\nabla U\) 已由低阶 Sobolev 得到 \(L^\infty\)。在 \(m=2\) 不成立：从所有有限 \(L^q\) 的 \(\nabla U\) 推出其 \(L^\infty\)，仍需当前未知的 \(\nabla^2U\)。

令

\[
V_2=\nabla^2U,\qquad V_1=\nabla U,\qquad Z_1=\nabla^2\chi.
\]

测试

\[
\chi\nabla^3\chi*V_1
\]

对 \(|V_2|^{p-2}V_2\)，把一阶导数从 \(\nabla^3\chi\) 移走：

1. 导数落在测试张量上时，

   \[
   \begin{aligned}
   &\int
   \chi |Z_1||V_1||\nabla V_2||V_2|^{p-2}\\
   &\le
   \varepsilon\int a|\nabla V_2|^2|V_2|^{p-2}
   +C_\varepsilon
   \int |Z_1|^2|V_1|^2|V_2|^{p-2},
   \end{aligned}
   \]

   而

   \[
   \int |Z_1|^2|V_1|^2|V_2|^{p-2}
   \le
   \|Z_1\|_{2p}^2\|V_1\|_{2p}^2\|V_2\|_p^{p-2}.
   \]

2. 导数落在 \(V_1\) 上时产生

   \[
   \int\chi\nabla^2\chi*V_2*|V_2|^{p-2}V_2,
   \]

   它正是 signed Hessian 形式，故

   \[
   \le
   \varepsilon\int a|\nabla V_2|^2|V_2|^{p-2}
   +Cr^{-2}\|V_2\|_p^p.
   \]

3. 导数落在 \(\chi\) 上只产生 \(d\chi*Z_1\) 的低阶项。

因此 \(m=2\) 可由基层的 \(L^{2p}\) 控制闭合，无需 \(\|\nabla U\|_\infty\)。对 \(m\ge3\)，同样分部积分后只剩前一层 cutoff jet 和低阶 \(U\) 导数。

### 3.2 shifted Proposition 4.13 仍需逐类处理当前阶项

无权 \(\nabla^m\Rm\) 方程至少必须明确覆盖：

\[
\chi\,d\chi*\nabla^{m+1}\Rm,
\]

由

\[
|\chi d\chi|^2\le \|d\chi\|_\infty^2a
\]

吸收到退化耗散；

\[
\chi\nabla^2\chi*\nabla^m\Rm,
\]

由 signed Hessian 分部积分处理；

\[
a\Rm*\nabla^m\Rm,
\]

由

\[
|a\Rm|\le |U|+C
\]

控制；其余项则只含低阶曲率导数和 cutoff jets，再用有限指数 Hölder。

Step 38 的 (3.3)–(3.5) 只展示了代表项，尚未证明所有交换子、归一化项和 \(G\)-项均落入这些类别。

### 3.3 零阶无权 \(L^p(\Rm)\) 不能只称为 plausible

需要正式证明 shifted Lemma 4.10。反应项确有

\[
a|\Rm|^{p+1}
\le (|U|+C)|\Rm|^p.
\]

Hessian-\(a\) 项需把 \(E=\Ric+g\) 分开并做 signed 分部积分；在 \(\Rm=0\) 附近使用
\((|\Rm|^2+\varepsilon)^{p/2}\) 正则化。目标是

\[
\frac d{dt}\int|\Rm|^p
+c_p\int a|\nabla\Rm|^2|\Rm|^{p-2}
\le
C_{p,K,r}\int|\Rm|^p+C_{p,K,r}.
\]

这是整个有限指数归纳的基底。

### 3.4 “有限”必须改成时间一致有界

续接需要

\[
\sup_{t\in[\tau,T)}
\|\nabla^mU(t)\|_{L^p(g(t))}<\infty,
\]

而不仅是每个时刻范数有限。所有低阶系数也必须在该时间段一致有界或时间可积。双 Lipschitz 度量比较可提供每个给定初值所需的 Sobolev 常数比较。

### 3.5 终端恢复方向正确，但尚需固定背景联络证明

若已获得所有阶的时间一致点态 \(U\)-导数界，则无需除以 \(a\)。可固定

\[
\bar\nabla=\nabla^{g(\tau)},\qquad
A(t)=\nabla^{g(t)}-\bar\nabla.
\]

利用

\[
\partial_tg=-2\Ric(U),\qquad
\partial_tA=g^{-1}*\nabla\Ric(U),
\]

及其 \(\bar\nabla\)-导数逐阶证明 \(g(t)\)、\(A(t)\) 在固定坐标中 Cauchy，并平滑收敛；双 Lipschitz 界保证极限正定。

但从终端度量重启仍需要归一化退化流

\[
\partial_tg=-2\chi^2(\Ric+g)
\]

的 transported-DeTurck 短时存在定理。该项是低阶扰动，但所需退化 tame estimates 在现有材料中没有证明。

---

## 4. 支持选择归一化

### 4.1 体积平均极大函数与体积保留正确

定义

\[
K_0=\fint_M|\Rm|^2,\qquad
\mathcal M_Rf(x)=\sup_{0<s\le R}\fint_{B_s(x)}f.
\]

在 \(\Ric\ge-2g\) 下，固定半径尺度有局部 doubling，故截断极大函数满足

\[
\Vol\{\mathcal M_R(|\Rm|^2)>\Lambda K_0\}
\le \frac{C_D}{\Lambda}\Vol M.
\]

严格的 Vitali 证明中常数可能应写成 \(C_D(5R)\)，或将定义中的最大半径改为 \(R/5\)。若 \(K_0=0\)，应单独处理，此时 \(\Rm\equiv0\)。

取固定大 \(\Lambda\) 后，

\[
\Vol G_R(\Lambda)\ge\eta_0\Vol M.
\]

随后取固定小 \(r\)，使

\[
Cr^4\Lambda\overline K_0\le\varepsilon,
\]

便有

\[
r^4\fint_{B_r(x)}|\Rm|^2\le\varepsilon.
\]

这里必须核对实际 \(\varepsilon\)-正则性假设究竟使用：

\[
r^4\fint_{B_r}|\Rm|^2
\]

还是四维尺度不变的

\[
\int_{B_r}|\Rm|^2.
\]

两者在塌缩球上不等价。若定理要求未归一化积分，则可由 Bishop–Gromov 上体积界得到

\[
\int_{B_r}|\Rm|^2
\le C r^4\Lambda\overline K_0,
\]

不需要、也不应声称校准提供逐球 noncollapse。校准体积比只给全局总体积尺度，并不自动给每个好球的下体积界。

### 4.2 Sobolev–体积消去正确

若 \(\eta\) 支撑于 \(B_{R_0r}(x)\)，则

\[
K_2^\eta
\le
(1+\Lambda\overline K_0)\Vol(B_{R_0r}(x)).
\]

配合体积归一化局部 Sobolev 常数

\[
\mathcal S
\le
C\frac{r^2}{\Vol(B_{R_0r})^{1/2}},
\]

得到

\[
\mathcal S(K_2^\eta)^{1/2}
\le
Cr^2(1+\Lambda\overline K_0)^{1/2}.
\]

体积完全消去，允许局部塌缩；这部分代数正确。真正仍需核对的是上述局部 Sobolev 不等式的精确几何假设及常数依赖。

### 4.3 校准体积比计算正确

令

\[
x=s+4,\qquad y=s+8\sqrt6|W^+|.
\]

则直接展开

\[
\frac{s^2}{24}+2|W^+|^2
=
\frac34-\frac38x+\frac1{24}y
+\frac{x^2}{24}
+\frac{(y-x)^2}{192}.
\]

由

\[
\|x\|_2^2+\|y\|_2^2=o(A),\qquad \Vol/A=O(1),
\]

Cauchy–Schwarz 给出其与 \(3/4\) 的 \(L^1\) 误差为 \(o(A)\)。再由

\[
I/A\to\frac23
\]

得到

\[
\frac34\Vol(M_i)+o(A_i)
=4\pi^2I_i
=\frac{8\pi^2}{3}A_i+o(A_i),
\]

所以

\[
\boxed{\frac{\Vol(M_i)}{A_i}\to\frac{32\pi^2}{9}}.
\]

因此把固定比例的总体积转成 \(A_i\)-比例体积，确实依赖校准给出的体积下界，而不是 Euler 特征的上估计。

但该论证预先使用了 \(\Vol/A=O(1)\)，其来源必须独立给出。

### 4.4 尚缺的支持构造输入

还需明确证明：

1. 序列一致平均全曲率界
   \[
   \sup_i\fint_{M_i}|\Rm|^2<\infty;
   \]
   仅控制 \(s\) 和 \(W^+\) 不自动控制 \(W^-\)，通常还需四维曲率分解及拓扑恒等式。

2. 极大分离网、内 plateau 球和扩大 support 球的固定半径比。

3. 相交图的统一有限度数及颜色数 \(N\)，以及 Bishop–Gromov 体积比较常数 \(c_{\mathrm{BG}}\)。

有了这些，才能严格推出某一颜色满足

\[
\sum_{\alpha\in\mathcal C}\Vol(P_\alpha)
\ge
\frac{c_{\mathrm{BG}}\eta_0}{N}\Vol(M_i)
\ge \alpha A_i.
\]

---

## 最终核验结论

四个问题的答案是：

1. **是。** Step 38 正确识别了 \(a=\chi^2\) 的退化及
   \(|U|\) 只能控制 \(|aE|\)，不能产生额外 \(\chi^2\) 小因子。

2. **基本是。** 加权 shifted \(U\) 方程、独立无权曲率导数模块、有限 Hölder 指数族及通过
   \(\partial_tg=-2\Ric(U)\) 恢复终端度量，均忠实于 Wang 的机制；但目前仍是结构性移植而非完整证明。

3. **仍有实质缺口。** 主要是完整推导 (1.2)、修复 \(m=2\) 的 \(\Gamma_3\)、写出 shifted Lemma 4.10 与 Proposition 4.13 的逐项估计、证明所有时间一致点态界、固定坐标终端恢复及退化短时重启。

4. **支持归一化主体正确。** 体积平均极大函数、大阈值保留体积、小固定半径、Sobolev–体积消去和校准体积比 \(32\pi^2/9\) 均正确；仍需核对所用小能量条件的精确归一化，并补足 \(\overline K_0\)、\(\Vol/A=O(1)\) 的来源以及覆盖着色常数。
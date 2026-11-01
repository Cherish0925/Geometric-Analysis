# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step38_continuation_repair_and_support_normalization.md",
    "Sessions/S0910A01/workspace/scripts/step38_continuation_support_verify.py",
    "Sessions/S0910A01/trace/ttcs/results/step37_ttcs01_verifier1_integration.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step39_general_p_defect_power_inequality.md"
  ]
}
```

## Task

Verify the mathematical content of `step38_continuation_repair_and_support_normalization.md` in the restricted four-dimensional negative Yau-26 route. Focus on four questions: (1) Does the note correctly identify the failure of Step 37 Lemma 1.2a from the degeneracy of a=chi^2 and the fact that |U| only gives |aE|, not chi^2-small drift? (2) Is the proposed repair direction faithful to Wang Lemmas 4.5, 4.6, Proposition 4.13, and Proposition 4.14: weighted shifted equation for U=a(Rm+G), separate unweighted curvature-derivative module, finite Hölder exponents, and smooth terminal recovery via dt g=-2 Ric(U)? (3) Are there hidden derivative, cutoff, G/normalization, or exponent gaps in the sketched estimates that would still block a continuation theorem? (4) Is the support-selection normalization correct: volume-average maximal function, large threshold for retained volume, small fixed radius for r^4 average smallness, Sobolev-volume cancellation, and Vol/A lower from calibration rather than Euler upper bound? Give a scientific verification/critique and concrete repairs, not a route decision.

## Output

# 科学核验备忘录

## 总体结论

Step 38 对 Step 37 核心错误的识别是正确的：

\[
|U|=|a(\operatorname{Rm}+G)|\le K
\quad\Longrightarrow\quad
|aE|=|\operatorname{Ric}(U)|\le C_4K,
\]

其中没有额外的 \(a=\chi^2\) 因子。因此过渡区 \(\chi\ll1\) 内不能推出流速按 \(\chi^2\) 衰减，也不能由小的 \(C^0\) 度量位移恢复无权曲率导数。

修复后的依赖顺序与 Wang 第 4 节基本一致：

\[
\text{加权 }U\text{ 方程}
\leftrightarrow
\text{cutoff jets}
\leftrightarrow
\text{无权曲率导数}.
\]

不过，现有 Step 38 仍是续接证明的结构蓝图，不是完整续接定理。最具体的数学缺口是：

1. (1.2) 尚未从张量变分逐项推出；
2. \(m=2\) 时把 \(\nabla U\) 当作已有 \(L^\infty\) 量是不成立的；
3. shifted Proposition 4.13 中所有当前阶项、shift 项和归一化项尚未分类；
4. 零阶无权 \(L^p(\operatorname{Rm})\) 模块仍只被称为“plausible”；
5. 终端重启仍使用未在此文证明的退化短时存在定理。

支持选择部分的尺度和代数归一化基本正确。体积平均极大函数、先取大阈值保留体积、再取小的固定半径获得 \(r^4\fint|\operatorname{Rm}|^2\) 小量，以及 Sobolev–体积消去都成立。校准推出

\[
\frac{\operatorname{Vol}(M_i)}{A_i}\to\frac{32\pi^2}{9}
\]

的计算也正确，但必须单独提供 \(\operatorname{Vol}/A=O(1)\) 和平均全曲率能量 \(K_0\) 的一致上界。

---

## 1. Step 37 Lemma 1.2a 的错误识别完全正确

设 \(a=\chi^2\)、\(T=\operatorname{Rm}+G\)、\(U=aT\)。在固定维数下，曲率型张量的 Ricci 收缩是有界线性映射，因此

\[
|\operatorname{Ric}(U)|\le C_4|U|.
\]

由于 \(\operatorname{Ric}(T)=E\)，

\[
\operatorname{Ric}(U)=aE.
\]

所以 \(|U|\le K\) 只给出

\[
|aE|\le C_4K,
\]

而不是

\[
|aE|\le C_4aK.
\]

一个点态代数模型已经足以否定后一个推断：取 \(a=\varepsilon^2\) 和曲率型张量
\(T=\varepsilon^{-2}T_0\)，则

\[
U=T_0,\qquad aE=\operatorname{Ric}(T_0),
\]

二者均可保持 \(O(1)\)，而 \(aK=O(\varepsilon^2)\)。

因此真正得到的是全局对数度量估计

\[
\left|\frac{d}{dt}\log g_t(v,v)\right|
\le C_4K,
\]

从而

\[
e^{-C_4K(t-\tau)}g(\tau)
\le g(t)\le
e^{C_4K(t-\tau)}g(\tau).
\]

这保证双 Lipschitz 等价、体积比较和 \(|d\chi|_{g(t)}\) 有界，但不产生过渡区内的 \(\chi^2\)-小位移。

Step 38 关于 cutoff jets 的说明也正确。对标量函数，\(d\chi\) 与联络无关，但

\[
\nabla^2\chi=\partial^2\chi-\Gamma*d\chi
\]

以及更高阶 \(\nabla^\ell\chi\) 都依赖演化联络。固定坐标导数有界并不能替代演化协变导数估计；而

\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)
\]

又依赖 \(U\) 的导数。这正是 Wang 交错归纳存在的原因。

---

## 2. 与 Wang 第 4 节的对应关系

### 2.1 加权方程的最高阶结构正确

Wang Lemma 4.5 的主对象是

\[
\nabla^m(\chi^2\operatorname{Rm}),
\]

其最高 cutoff 行确实含有

\[
\nabla^i\chi*\nabla^j\chi*
\nabla^k(\chi^2\operatorname{Rm}),
\]

而不是无权 \(\nabla^k\operatorname{Rm}\)。因此 shifted 对象应当是

\[
U=a(\operatorname{Rm}+G),
\]

并产生 Step 38 的四个最高分配：

\[
\begin{aligned}
\Gamma_1&=\chi\nabla^{m+2}\chi*U,\\
\Gamma_2&=\nabla\chi*\nabla^{m+1}\chi*U,\\
\Gamma_3&=\chi\nabla^{m+1}\chi*\nabla U,\\
\Gamma_4&=\chi\nabla\chi*\nabla^{m+1}U.
\end{aligned}
\]

这与 Wang Proposition 4.14 显示的四项一致。

在四维中还需固定 Kulkarni–Nomizu 乘积约定，使

\[
G=\frac{g\owedge g}{6},\qquad \operatorname{Ric}(G)=g.
\]

虽然 \(\nabla G=0\)，但

\[
\partial_tG
=\frac16\bigl((\partial_tg)\owedge g+
g\owedge(\partial_tg)\bigr)
\]

并不为零。由于 \(\partial_tg=-2\operatorname{Ric}(U)\)，它只产生 \(U\) 的代数项及其至多当前阶的导数，不改变最高空间导数结构。这个判断正确，但必须在完整推导中实际写出。

### 2.2 cutoff-jet 方程方向正确，显示式需修正

在张量层面，更准确的形式是

\[
|\partial_t\nabla^\ell\chi|
\le
C_\ell\sum_{j=1}^{\ell-1}
|\nabla^jU|\,|\nabla^{\ell-j}\chi|.
\]

当计算张量范数和 \(L^p\) 积分的时间导数时，还会加入

\[
C|U|\,|\nabla^\ell\chi|
\]

以及体积元变化项。因此 \(Z=\nabla^2\chi\) 的准确模型是

\[
\partial_t Z=\nabla U*d\chi,
\]

而其范数满足

\[
\partial_t|Z|
\le C|\nabla U||d\chi|+C|U||Z|.
\]

Step 38 的 (2.4) 把这些因子的配对写成了
\((|V|+|U||d\chi|)|Z|^{p-1}\)，并不逐字对应张量方程；正确积分项应为

\[
\int |V||d\chi||Z|^{p-1}
+\int |U||Z|^p.
\]

因为 \(|d\chi|\) 和 \(|U|\) 已有界，最后得到的 Grönwall 型估计仍然相同。

### 2.3 无权曲率模块必须独立存在

Step 38 不再尝试除以 \(a\)，而是恢复 Wang Proposition 4.13 的独立无权方程。这一点完全正确。正确的交错顺序应写成

\[
\begin{array}{c}
\operatorname{Rm}\text{ 的零阶 }L^q\\
\Downarrow\\
(\nabla U,\nabla^2\chi)\\
\Downarrow\\
\nabla\operatorname{Rm}\\
\Downarrow\\
(\nabla^2U,\nabla^3\chi)\\
\Downarrow\\
\nabla^2\operatorname{Rm}\\
\Downarrow\cdots
\end{array}
\]

其中每一层都应对任意足够大的有限指数成立。Wang 原文使用 \(q>100\)；这里无需声称所有正指数，只需“任意足够大的有限 \(q\)”。

(3.4) 和 (3.5) 的 Hölder 指数核算正确：

\[
\frac1p+\frac1p+\frac{p-2}{p}=1,
\]

以及

\[
\frac{N}{Np}+\frac{p-1}{p}=1.
\]

脚本 `step38_continuation_support_verify.py` 正确核算了这些恒等式，但脚本最后三个 PDE 项直接使用布尔常量 `True`，所以它没有检验张量演化式或续接证明。

### 2.4 终端恢复的变量选择正确

只要能得到所有阶的时间一致点态估计，

\[
\sup_{[\tau,T)}|\nabla^mU|<\infty,
\]

则

\[
\partial_tg=-2\operatorname{Ric}(U),\qquad
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)
\]

提供正确的终端恢复途径，不需要除以 \(a\)。

更严密的写法是固定 \(\nabla^\tau=\nabla^{g(\tau)}\)，令

\[
A(t)=\nabla^{g(t)}-\nabla^\tau.
\]

由 \(\partial_tA=g^{-1}*\nabla\operatorname{Ric}(U)\) 及其固定联络导数，可逐阶证明 \(A(t)\) 和 \(g(t)\) 在固定坐标中收敛。双 Lipschitz 估计保证终端极限仍正定。随后重启需要一个适用于

\[
\partial_tg=-2\chi^2(\operatorname{Ric}+g)
\]

的退化短时存在结果；归一化项是低阶项，但该存在结果仍需明确引用或证明。

---

## 3. 仍阻碍完整续接定理的具体数学点

### 3.1 \(m=2\) 的 \(\Gamma_3\) 估计写错了

Step 38 §4 写道：对 \(m\ge2\)，\(\nabla U\) 可由低层估计和 Sobolev 得到 \(L^\infty\) 控制。对 \(m=2\) 这不成立。

低层只给出

\[
\nabla U\in L^q\quad\text{对任意大有限 }q,
\]

而要由 Sobolev 得到 \(\nabla U\in L^\infty\)，还需要
\(\nabla^2U\in L^q\)，这正是当前未知量。

可用一次分部积分修复。令

\[
V=\nabla^2U,\qquad W=\nabla U,\qquad Z_1=\nabla^2\chi.
\]

对

\[
\Gamma_3=\int |V|^{p-2}V*
\chi\nabla^3\chi*W
\]

把一阶导数从 \(\nabla^3\chi\) 移走。导数落在测试张量上时得到

\[
\varepsilon D_{2,p}
+C_\varepsilon
\int |Z_1|^2|W|^2|V|^{p-2},
\]

且

\[
\int |Z_1|^2|W|^2|V|^{p-2}
\le
\|Z_1\|_{2p}^2\|W\|_{2p}^2\|V\|_p^{p-2}.
\]

导数落在 \(W\) 上时产生

\[
\int \chi\nabla^2\chi*V*|V|^{p-2}V,
\]

这正是 signed Hessian 结构，可再次估计为

\[
\varepsilon D_{2,p}+Cr^{-2}\|V\|_p^p.
\]

这给出 \(m=2\) 所需的有限指数修复。Wang Proposition 4.14 原文也是对 \(\Gamma_1,\Gamma_2,\Gamma_3\) 做分部积分，而不是直接使用 \(\nabla U\) 的点态估计。

### 3.2 (1.2) 必须证明最高 cutoff 项中的系数确为 \(U\)

若把流拆成局部 Ricci 部分和 \(-2ag\) 部分分别计算，会暂时出现

\[
a\nabla^{m+2}a*G
\]

一类看似不含 \(U\) 的项。正确做法是从整体速度

\[
\partial_tg=-2\operatorname{Ric}(U)
\]

推导曲率变分；最高二阶导数具有

\[
\nabla^2\operatorname{Ric}(U)
\]

结构。使用 \(U=aT\) 的微分 Bianchi 展开后，最高 cutoff jet 应与 \(U\) 相乘。这个消去必须逐项展示，否则 (1.2) 中
\(\mathcal L_m^{G,\mathrm{norm}}\) 的阶数描述还没有数学依据。

### 3.3 shifted Proposition 4.13 需要当前阶项分类

无权 \(\nabla^m\operatorname{Rm}\) 方程中至少要明确处理：

* \(k=m+1\) 项：
  \[
  \chi\,d\chi*\nabla^{m+1}\operatorname{Rm},
  \]
  由 \(|\chi d\chi|^2\le C a\) 吸收到退化耗散中；

* \(k=m\) 项：
  \[
  \chi\nabla^2\chi*\nabla^m\operatorname{Rm},
  \]
  使用 signed Hessian 分部积分；

* 反应项中的当前阶因子：
  \[
  a\operatorname{Rm}*\nabla^m\operatorname{Rm},
  \]
  由
  \[
  |a\operatorname{Rm}|\le |U|+C
  \]
  控制；

* 其余乘积只含低阶曲率导数和 cutoff jets，再按因子数选择 \(Np\)、\(2Np\) 等有限指数。

(3.2)–(3.5) 展示了其中一个代表项，但尚未证明所有归一化与 \(G\) 项均落入上述类型。

### 3.4 零阶无权 \(L^p(\operatorname{Rm})\) 传播仍需写成引理

Step 38 正确保留了反应项估计

\[
a|\operatorname{Rm}|^{p+1}
\le (|U|+C)|\operatorname{Rm}|^p.
\]

Hessian-\(a\) 项还需拆分 \(E=\operatorname{Ric}+g\)，使用 signed 分部积分，并在 \(\operatorname{Rm}=0\) 附近用

\[
(|\operatorname{Rm}|^2+\varepsilon)^{p/2}
\]

作光滑测试。预期得到

\[
\frac d{dt}\int|\operatorname{Rm}|^p
+c_p\int a|\nabla\operatorname{Rm}|^2|\operatorname{Rm}|^{p-2}
\le
C_{p,K,r}\int|\operatorname{Rm}|^p+C_{p,K,r}.
\]

这个引理是后续所有低阶 Hölder 因子的起点，不能仅以“plausible”代替。

### 3.5 所有估计必须是时间一致的

符号“\(<\infty\)”应替换为

\[
\sup_{t\in[\tau,T)}
\|\cdot\|_{L^p(g(t))}<\infty.
\]

Grönwall 中出现的低层系数也必须在该时间段一致有界或可积。由于 \(g(t)\) 与 \(g(\tau)\) 双 Lipschitz 等价，全局 Sobolev 常数可按单个初始数据控制；这足以把任意大有限 \(L^q\) 导数族转换成点态估计。

---

## 4. 支持选择归一化

### 4.1 极大函数选择正确

定义

\[
K_0=\fint_M|\operatorname{Rm}|^2,\qquad
\mathcal M_Rf(x)=\sup_{0<s\le R}\fint_{B_s(x)}f.
\]

若 \(\operatorname{Ric}\ge-2g\)，Bishop–Gromov 给出固定半径尺度上的 doubling 常数。截断极大函数满足

\[
\operatorname{Vol}\{\mathcal M_Rf>\Lambda K_0\}
\le \frac{C_D}{\Lambda K_0}\int f
=\frac{C_D}{\Lambda}\operatorname{Vol}M.
\]

严格使用 Vitali 五倍球论证时，常数应写成 \(C_D(5R)\)，或者把极大半径改成 \(R/5\)。若 \(K_0=0\)，则 \(\operatorname{Rm}\equiv0\)，应单独处理，避免除以零。

选择固定大 \(\Lambda\) 后得到

\[
\operatorname{Vol}G_R(\Lambda)\ge\eta_0\operatorname{Vol}M.
\]

随后选择固定小 \(r\)，使

\[
r^4\Lambda\overline K_0\ll1,
\]

则对每个好点

\[
r^4\fint_{B_r(x)}|\operatorname{Rm}|^2
\le r^4\Lambda K_0.
\]

若所用 \(\varepsilon\)-正则性定理要求的是未归一化积分，还需加入 Bishop–Gromov 上体积估计：

\[
\int_{B_r(x)}|\operatorname{Rm}|^2
\le V_{-2,4}(r)\Lambda\overline K_0
\le C r^4\Lambda\overline K_0.
\]

因此 (5.4) 中可能需要一个维数常数 \(C\)。

### 4.2 Sobolev–体积消去正确

若 \(\eta\) 支持于 \(B_{R_0r}(x)\)、\(0\le\eta\le1\)，则好点性质给出

\[
K_2^\eta
=\int\eta^2(1+|\operatorname{Rm}|^2)
\le
(1+\Lambda\overline K_0)
\operatorname{Vol}(B_{R_0r}(x)).
\]

Ricci 下界下的体积归一化局部 Sobolev 不等式具有

\[
\mathcal S
\le
C\frac{r^2}{\operatorname{Vol}(B_{R_0r})^{1/2}}.
\]

故

\[
\mathcal S(K_2^\eta)^{1/2}
\le
Cr^2(1+\Lambda\overline K_0)^{1/2},
\]

体积因子完全消去。脚本对此代数消去的核算正确。

### 4.3 校准体积比计算正确

令

\[
x_i=s_i+4,\qquad
y_i=s_i+8\sqrt6\,|W_i^+|.
\]

则

\[
s_i=-4+x_i,\qquad
|W_i^+|=\frac{4+y_i-x_i}{8\sqrt6}.
\]

直接展开可得

\[
\frac{s_i^2}{24}+2|W_i^+|^2
=
\frac34-\frac38x_i+\frac1{24}y_i
+\frac{x_i^2}{24}
+\frac{(y_i-x_i)^2}{192}.
\]

若

\[
\|x_i\|_2^2+\|y_i\|_2^2=o(A_i),
\qquad
\operatorname{Vol}(M_i)=O(A_i),
\]

则 Cauchy–Schwarz 给出所有线性项的 \(L^1\) 大小为 \(o(A_i)\)，二次项也是 \(o(A_i)\)。因此

\[
\int\left(\frac{s_i^2}{24}+2|W_i^+|^2\right)
=
\frac34\operatorname{Vol}(M_i)+o(A_i).
\]

结合

\[
I_i/A_i\to\frac23
\]

便得到

\[
\frac34\operatorname{Vol}(M_i)
=
\frac{8\pi^2}{3}A_i+o(A_i),
\]

所以

\[
\boxed{\frac{\operatorname{Vol}(M_i)}{A_i}
\to\frac{32\pi^2}{9}}.
\]

这里的体积下界确实来自校准恒等式，而不是 Euler 数的上估计。

### 4.4 覆盖与着色仍需写出常数依赖

取尺度 \(\rho\simeq r\) 的极大分离网。覆盖球覆盖好点集，Bishop–Gromov 比较内 plateau 球与覆盖球体积，得到

\[
\sum_\alpha\operatorname{Vol}(P_\alpha)
\ge c\,\operatorname{Vol}(G_R(\Lambda)).
\]

扩大 support 球的相交图在 doubling 空间中有统一有限度数，因此可用固定颜色数 \(N\) 着色；至少一个颜色满足

\[
\sum_{\alpha\in\mathcal C}\operatorname{Vol}(P_\alpha)
\ge
\frac{c\eta_0}{N}\operatorname{Vol}(M_i)
\ge \alpha A_i.
\]

常数依赖应明确为维数、Ricci 下界、\(R_0\) 和固定半径比，而不依赖序列指标。

最后还有两个必须提供来源的输入：

1. \(\overline K_0=\sup_i\fint|\operatorname{Rm}_{g_i}|^2<\infty\)；
2. 先验的 \(\operatorname{Vol}(M_i)/A_i=O(1)\)。

仅由 (5.8) 控制 \(s_i\) 和 \(W_i^+\) 还不能直接控制 \(W_i^-\) 的能量；平均全曲率上界通常还需四维曲率分解、Gauss–Bonnet、signature 恒等式及相关拓扑量相对 \(A_i\) 的估计。

---

## 归纳性评价

Step 38 已正确修正两个核心结构：

\[
|U|\not\Rightarrow |aE|=O(a),
\]

以及

\[
\nabla^mU,\ \nabla^{m+1}\chi,\
\nabla^{m-1}\operatorname{Rm}
\]

必须交错估计，不能在 \(\chi\to0\) 区域除以 \(a\)。

最重要的局部修补是重写 \(m=2\) 的 \(\Gamma_3\) 估计，并从整体速度
\(-2\operatorname{Ric}(U)\) 推导完整 shifted 演化式。支持选择的平均归一化、尺度选择、Sobolev 消去和校准体积比均具有正确数学结构；其余所需内容是平均全曲率上界、覆盖常数以及退化短时重启定理的明确证明或来源。
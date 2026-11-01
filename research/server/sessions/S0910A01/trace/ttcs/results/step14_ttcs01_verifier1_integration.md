# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 14,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step14_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step14_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Evaluate the source-grounded smoothing route for the four-dimensional negative branch of Yau Problem 26. Read the Step 14 route note and the Ye Li 0911.3104 smoothing source carefully. Check the scale calculation: bounded local mean |Rm|^2 on a maximal-function good ball implies Ye Li's r^4-average smallness after choosing a fixed small physical radius. Determine exactly what is and is not supplied by Li's theorem as stated (complete/all-centers vs buffered local), and whether the route note faithfully identifies the missing bridges. Then assess how this could interact with the existing Derdziński chart-accessibility theorem: what additional statement would be sufficient to turn smoothing into a fixed-scale normal-cover/harmonic-chart contradiction, and what assumptions would be unsupported? Do not decide the session; give a rigorous mathematical memo with source-specific hypotheses and possible proof repairs.

## Integrated Scientific Memo

# 核验备忘录：四维负分支中的 Ye Li 平滑路线

## 1. 固定小尺度计算：成立，但必须以极大函数控制表述

记
\[
f=|\Rm_g|^2,\qquad
\mathcal M_R f(p)=\sup_{0<s\le R}\fint_{B_s(p)}f.
\]
设
\[
\Ric_g\ge -3g,\qquad \mathcal M_R f(p)\le K_0.
\]
取固定缓冲倍数 \(m\ge1\)，并令
\[
(m+1)\rho\le R.
\]
若 \(q\in B_{m\rho}(p)\)，则
\[
B_\rho(q)\subset B_{(m+1)\rho}(p)
          \subset B_{(2m+1)\rho}(q).
\]
因此
\[
\int_{B_\rho(q)}f
\le K_0\,\Vol B_{(m+1)\rho}(p),
\]
而 Bishop–Gromov 相对体积比较给出
\[
\fint_{B_\rho(q)}f
\le K_0\frac{\Vol B_{(2m+1)\rho}(q)}
                  {\Vol B_\rho(q)}
\le K_0\frac{V_{-1}((2m+1)\rho)}{V_{-1}(\rho)}
\le C_mK_0
\]
（对 \(0<\rho\le1\)，最后常数只依赖维数和 \(m\)）。于是
\[
\frac{\rho^4}{\Vol B_\rho(q)}
\int_{B_\rho(q)}|\Rm|^2
=\rho^4\fint_{B_\rho(q)}|\Rm|^2
\le C_mK_0\rho^4.
\]
故若
\[
\rho\le
\min\left\{
1,\frac{R}{m+1},
\left(\frac{\varepsilon_{\rm Li}}{C_mK_0}\right)^{1/4}
\right\},
\]
则 Li 的无量纲小量条件在整个 \(B_{m\rho}(p)\) 的每个中心成立。若再令 \(\rho^2\lesssim K^{-1}\)，Li 型寿命应为 \(T\gtrsim\rho^2\)。

因此 Step 14 的核心尺度判断正确：有界的局部均值并不因非零背景曲率而妨碍 Li 小量条件；乘子 \(\rho^4\) 允许选取一个在序列指标 \(i\) 之前固定的物理尺度 \(\rho>0\)。这里没有通过随 \(i\) 缩小尺度而把 Einstein 常数“冲掉”。

但必须修正一个潜在歧义：

\[
\fint_{B_R(p)}|\Rm|^2\le K_0
\]
这一单独的大球平均并不足以推出上述结论。若用 \(B_R(p)\) 控制小球，体积比约为 \((R/\rho)^4\)，会抵消 \(\rho^4\)。真正需要的是：

- 截断极大函数控制 \(\mathcal M_Rf(p)\le K_0\)，或
- 至少在与 \((m+1)\rho\) 可比的同心尺度上有均值控制。

Step 14 最后一段确实调用 Hardy–Littlewood 极大函数选择，因此路线实质上具备正确输入；§3 的局部计算应明确改写为上述形式。Step 11 的全局平均曲率能量界配合局部 doubling 的弱 \((1,1)\) 估计，可选择固定正体积比例的曲率极大函数良点，并可与平均趋零的校准缺陷良点相交。

---

## 2. Li 0911.3104 的精确结论

### 2.1 定理是 complete/all-centers，而非 buffered-local

源文的相关层次为：

1. Theorem 1.1：完整非紧四维流形，统一半径 \(r\le1\)，并要求
   \[
   \int_{B_r(x)}|\Rm(g_0)|^2\le\varepsilon
   \qquad\text{对每个 }x\in M,
   \]
   以及 \(|\Ric(g_0)|\le K\)。

2. Theorem 3.1：同样是对所有中心的 Sobolev 加权临界能量条件。

3. Theorem 3.6：将输入改写为
   \[
   \frac{r^4}{\Vol B_r(x)}
   \int_{B_r(x)}|\Rm(g_0)|^2\le\varepsilon.
   \]
   虽然抽取文本的该行没有再次写出 “for every \(x\)”，其上下文、Theorem 3.1 的设定及任意中心覆盖论证都表明应作全中心统一条件理解。

结论是全局 Ricci 流
\[
\partial_tg=-2\Ric(g),\qquad g(0)=g_0,
\]
存在于
\[
0\le t<T,\qquad
T\ge C_1\min(r^2,K^{-1}),
\]
且
\[
\|\Rm(g(t))\|_\infty\le C_2t^{-1}.
\]

该全中心性质是证明结构所必需的：证明用
\[
B_{2r}(x)\subset\bigcup_{j=1}^N B_r(y_j)
\]
的相邻球覆盖，并在 continuation argument 中控制关于所有 \(x\) 的局部曲率能量上确界。源文也明确说其所研究的方程“is not local”。

### 2.2 闭流形并非主要障碍

Yau 26 的流形是闭的；闭流形当然已有 Hamilton 短时流。但其寿命可能依赖于 \(\sup|\Rm(g_0)|\)，无法给出序列一致的固定时间及 \(C/t\) 曲率界。Li 定理的价值正是寿命和曲率控制只依赖于 \(r,K,\varepsilon\)。

真正的障碍是：极大函数选择只在一个缓冲良域上给出全中心小量，坏的高能区域仍可能违反该条件。因此不能把闭流形直接代入 Li 的全局定理。

### 2.3 源文尚未提供的结论

Li 的文章没有陈述：

> 若无量纲曲率能量在一个缓冲域的每个中心都小，则存在只依赖该缓冲数据、与外部几何无关的局部流，并在更小内域上满足 \(|\Rm|\le C/t\)。

这正是路线所需的 collapsed buffered-local theorem。它不是 Theorem 3.6 的直接推论。尤其：

- 共形补全可能在 collar 中产生 \(O(\rho^{-2})\) 曲率，使
  \[
  \rho^4\fint|\Rm|^2
  \]
  仍为 \(O(1)\)，未必小于 \(\varepsilon_{\rm Li}\)；
- 补全 collar 的 Ricci 一致控制也需另证；
- 外部高曲率对内域的影响需要真正的局部/pseudolocality 论证，而非 Li 的全局 continuation argument。

Step 14 将此识别为首要缺桥，是忠实的；“证明结构暗示局部版本”只能作为研究提案，不能当作来源结论。

### 2.4 双 Lipschitz 控制的准确强度

Li 的 continuation 证明维护
\[
\frac12g_0\le g(t)\le2g_0.
\]
所以粗糙的半径、体积和距离可比较性确实存在于证明中，尽管未列入 Theorem 3.6 的最终显示结论。

但源文不提供：

- \(g(t)\) 与 \(g_0\) 的 \(C^{1,\alpha}\) 或 \(W^{2,p}\) 比较；
- 正时间 harmonic radius 向初始度量的反向传递；
- 足以保持 Weyl 校准数据的小时间一致连续模；
- 由有界截面曲率自动得到的非塌缩正规覆盖。

因此 Step 14 中“metric/distance distortion”只能理解为粗双 Lipschitz 控制，不能理解为 harmonic-chart transfer。

---

## 3. 与 Derdziński 可达性矛盾相接所需的充分陈述

Step 8/11 的真正输入不是“有一个平滑度量”，而是原度量或一个可控替代度量上的固定尺度正规覆盖与 harmonic chart。存在两种严格可行的桥接形式。

### 3.1 最干净的桥：为原度量产生非塌缩正规覆盖

对正体积比例的极大函数良点 \(p_i\)，若能证明存在与 \(i\) 无关的 \(h,v>0\) 及缓冲正规覆盖
\[
\pi_i:(\widehat U_i,\hat g_i(0))
\longrightarrow(U_i,g_i(0))
\]
满足：

1. \(\overline{B_{3h}(\hat p_i)}\Subset\widehat U_i\)；
2. \(\Vol_{\hat g_i(0)}B_h(\hat p_i)\ge vh^4\)；
3. 原始校准缺陷可按已建立的 cover-mean 估计传递：
   \[
   \fint_{B_h(\hat p_i)}\pi_i^*F_i
   \le C\,\mathcal M_RF_i(p_i)\longrightarrow0,
   \]

则在原度量具有一致 Ricci 界的条件下，现有 harmonic-radius 坏集估计可在该非塌缩覆盖球内找到固定半径的 harmonic chart。随后 Step 8 的有限 \(W^{2,p}\) 极限和 Derdziński 禁止胚芽矛盾可直接应用。

这个版本无需证明 Ricci 流保持 \(E=\Ric+g\) 或 \(W^+\) 校准；所有缺陷均在 \(t=0\) 使用。正时间平滑只需帮助建立上述非塌缩正规覆盖。粗双 Lipschitz 比较足以把同一个覆盖域上的体积非塌缩从 \(g_i(t_0)\) 转回 \(g_i(0)\)，但前提是该正规覆盖作为拓扑/几何对象已被真正构造。

如果不愿调用 harmonic-radius 坏集定理，也可把充分结论加强为：上述覆盖同时直接为 \(g_i(0)\) 提供固定 \(C^{1,\alpha}\cap W^{2,p}\) harmonic chart。仅由正时间 chart 加双 Lipschitz 比较不能得到这一加强结论。

### 3.2 在平滑度量自身上运行矛盾

另一充分形式是在归一化 Ricci 流
\[
\partial_\tau\bar g=-2(\Ric_{\bar g}+\bar g)
\]
的固定正时间 \(\tau_0\asymp\theta\rho^2\) 上获得非塌缩正规覆盖及 harmonic chart，并证明
\[
\fint_{\widehat B_h}F_{\bar g_i(\tau_0)}
\le
C\fint_{\widehat B_{Ch}}\pi_i^*F_{g_i(0)}
+\omega(\theta),
\qquad \omega(\theta)\to0
\]
且所有常数关于 \(i\) 一致。先选 \(\theta\) 使 \(\omega(\theta)\) 小于固定的 Derdziński forbidden-germ gap，再令 \(i\to\infty\)，即可矛盾。

近 Einstein 部分可能有可修复的抛物估计。令
\[
S=\Ric_{\bar g}+\bar g.
\]
其方程是齐次 Lichnerowicz 型方程，Li 的 Corollary 3.5 所用 Moser 机制有希望在缓冲局部版本中把
\[
\|S(0)\|_\infty\le\delta_i
\]
传为固定正时间的 \(C(\theta)\delta_i\to0\)。但仅写
\[
\partial_t|S|\lesssim\Delta|S|+\frac C t|S|
\]
并作从 \(0\) 开始的 Grönwall 是无效的，因为
\[
\int_0^{t_0}\frac{dt}{t}=\infty.
\]
所以 Step 14 中“至多多项式放大”的说法不能单独作为证明；必须使用更精细的初始能量/Moser 估计。

Weyl 校准项
\[
s+8\sqrt6|W^+|,\qquad \mathcal G
\]
更困难。它们是非线性曲率函数，其演化含二次曲率项。仅有初始 \(L^2\) 曲率有界和正时间 \(C/t\) 界，并不给出关于整个序列一致的小时间连续模。故“取一个很小但固定的时间”本身不能保证校准数据仍小；需要专门的演化不等式、曲率测度传输定理或额外导数紧性。

---

## 4. 平滑之后仍缺少正规覆盖/秩桥

即使局部 Li 流成立，在
\[
t_0=\theta\rho^2
\]
只能直接得到
\[
|\Rm(g_i(t_0))|\le\frac{C}{\theta\rho^2},
\]
即固定尺度的有界截面曲率塌缩几何。它不自动蕴含：

- 所需基域的 genuine normal cover；
- 覆盖球的统一非塌缩；
- 局部短纤维在缓冲域基本群中的存活；
- 最大 fibered nilpotency rank。

在 bounded-curvature collapse 的正规层上，CFG 型结构有望产生 nilpotent fibration 和非塌缩局部覆盖；这正是平滑的实际增益。但不能把“CFG 结构”无条件读成“每点都有非塌缩正规覆盖”。秩零或奇异层仍可出现：短轨道可能在缓冲域内收缩为零，局部基本群不能解开它。Step 11 所述 Taub–NUT 型机制正展示了这种风险。平滑把问题转化到有界曲率范畴，却没有自动排除该机制。

因此，除 buffered-local Li 外，还需要下列任一类陈述：

1. **正体积正规层定理：** 平滑良域中有固定正体积比例落在 CFG 正规层，且该层的局部纤维秩足以产生统一非塌缩正规覆盖；
2. **秩零排除：** 平滑后的 rank-zero/contractible-fiber 区域若占正体积，则原度量的校准缺陷有固定正下界；
3. **直接覆盖定理：** 不经完整 CFG 分类，直接由局部 Li 平滑、原始近 Einstein 条件及极大函数能量控制推出上述原度量覆盖非塌缩结论。

Huang–Wang 路线只有在预先验证 GH 低维模型和最大 nilpotency rank 时才给出相关局部平滑/覆盖结构；这些条件不能由 Noether 平均能量或 Li 定理默默推得。

---

## 5. 对 Step 14 的最终核验

Step 14 对以下关键点判断正确：

- Li 小量是 \(r^4\) 乘局部曲率均值，非零 \(O(1)\) 背景曲率不是尺度障碍；
- 应选一个先于 \(i\to\infty\) 固定的物理小尺度；
- Li 3.6 是完整流形、统一半径、全中心条件；
- 选定良球只给缓冲局域全中心条件，不能直接代入源定理；
- 必须处理平滑几何向原度量的传递，或证明近 Einstein/校准缺陷沿流保留；
- 有界曲率平滑后仍需覆盖非塌缩和纤维秩信息。

需要作三点加强：

1. §3 的输入必须明确为截断极大函数控制，而不是单个大球均值。
2. Li 的 factor-two metric comparison 只是粗双 Lipschitz 控制，不能推出原度量 harmonic radius。
3. “局部化”和“缺陷传递”之外，应把“正体积比例上的 genuine noncollapsed normal-cover production”列为同等独立的第三座桥；bounded sectional curvature 本身并不完成它。

最精确的未决数学对象因而是：

> 在四维、\(|\Ric|\le K\) 的缓冲域上，若每个中心满足固定尺度的 Li 无量纲 \(L^2\) 小量，证明一个不依赖外部高能区的内域 Ricci-flow 曲率估计；并证明该正时间有界曲率几何在正体积比例上产生可转回初始度量的非塌缩正规覆盖，或证明所有阻碍这种覆盖的秩零/奇异区域都具有固定的原始校准缺陷下界。

没有这两部分，Li 0911.3104 尚不能与现有 Derdziński chart-accessibility 定理闭合；但固定尺度计算本身是正确且有实质推进作用的。
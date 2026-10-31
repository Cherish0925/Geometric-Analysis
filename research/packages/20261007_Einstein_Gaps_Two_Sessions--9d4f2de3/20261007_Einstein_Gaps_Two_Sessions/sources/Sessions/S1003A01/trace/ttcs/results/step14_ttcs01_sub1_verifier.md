# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step14_large_collar_resistance_and_cluster_budget.md",
    "Sessions/S1003A01/workspace/scripts/neutral_mode_resistance.py",
    "Sessions/S1003A01/workspace/data/perp_collar/neutral_mode_resistance.json",
    "Sessions/S1003A01/workspace/data/pair_profile/exterior_budget_X8.json",
    "Sessions/S1003A01/workspace/data/perp_collar/rigorous_continued_X16_to_X32_J_d12.json",
    "Sessions/S1003A01/workspace/data/perp_collar/rigorous_continued_X32_to_X64_J_d16.json",
    "Sessions/S1003A02/workspace/notes/step13_einstein_fillings_blown_up_ball.md"
  ]
}
```

## Task

Independently examine the Step-14 mathematical synthesis. Check especially: (i) the frozen-core cluster saving inequality and its interpretation at overlap depth w=1.6; (ii) whether the exact one-dimensional minimization for A_T(q)=∫_0^T e^{4t}(q''+4q')^2 with clamped endpoint data really tends to 64 Delta^2; (iii) whether that reduced result justifies only a conditional route to diagonal coercivity rather than a lower bound for the full cell problem; and (iv) what the new rigorous X=32 and X=64 cell enclosures establish. Identify any mathematical or interpretive correction that should be made, and state the strongest sound implication for the Einstein-gap programme.

## Output

# Step 14 数学核验备忘录

## 总结

Step 14 的四个主要数学点可以区分为三种强度：

1. 冻结核区不等式是一个精确的非线性能量记账式；但在 \(w=1.6\) 时，其数值余量极大，只能排除无限制的逐对累加，不能否定通常配位数下的多体增益。
2. 加权一维变分问题可以完全解析求解，最小作用量确实趋于
   \[
   64\Delta^2=39.603109991\ldots .
   \]
   脚本中名为 `resistance` 的量却是其倒数型系数 \(\Delta^2/E\)，趋于 \(1/64\)；正文最好明确这两个互为倒数的约定。
3. 该一维结果只给出统一非塌缩 ACH 管内、近似夹持端点条件下的定量机制。它目前没有给出对角 cell 泛函的无条件下界，更没有给出全体度量上的下界。
4. \(X=32,64\) 的 Arb 区间给出了两个固定 admissible profile 的严格积分上界，并且 \(X=64\) 严格改进 \(X=32\)。它们建立了当前最强的显式 cell 上界，但没有建立极限饱和、极小元存在或正的最小 defect。

---

## 1. 冻结核区 cluster 不等式

设 cluster 中的核区 \(C_i\) 两两不交，并且 \(g_{\mathrm{cluster}}\) 在 \(C_i\) 上与孤立 cell 度量 \(g_i\) 等距一致。由于
\[
|\operatorname{Ric}+6g|^2\ge 0,
\]
有
\[
\begin{aligned}
J(g_{\mathrm{cluster}})
&=\sum_iJ(g_{\mathrm{cluster}};C_i)
  +J\!\left(g_{\mathrm{cluster}};
     M_{\mathrm{cluster}}\setminus\bigcup_i C_i\right)\\
&\ge \sum_iJ(g_i;C_i).
\end{aligned}
\]
因此
\[
\sum_iJ(g_i)-J(g_{\mathrm{cluster}})
\le \sum_iJ(g_i;M_i\setminus C_i).
\]
同一推导也适用于 \(P=\int|\operatorname{Ric}^{\circ}|^2\)。

这确实说明：相对于固定的孤立 cells，每个可调 exterior 的能量只能被使用一次，而不能为每一个邻居重新记一次。

### \(w=1.6\) 的正确数值解释

`exterior_budget_X8.json` 给出
\[
r_{\mathrm{cut}}=\rho-w
=1.762747174039086-1.6
=0.162747174039086
\]
以及单个 cell 的 exterior 能量
\[
E_{\mathrm{ext}}/(8\pi^2)
=0.1510633950729049.
\]
所以对于一对 cells，精确记账式给出的其实是
\[
\frac{2J_{\mathrm{cell}}-J_{\mathrm{pair}}}{8\pi^2}
\le 2E_{\mathrm{ext}}/(8\pi^2)
=0.3021267901458098.
\]
观测到的 pair saving 约为 \(1.25\times10^{-5}\)，只占这个上限约
\[
4.1\times10^{-5}.
\]
因此这个估计在 \(w=1.6\) 上非常宽松。若形式上把每条边的 saving 都取为该值，平均配位数要达到约
\[
z\sim \frac{2(0.15106)}{1.25\times10^{-5}}
\approx 2.4\times10^4
\]
才会碰到这一能量记账上限。普通几何 packing 的配位数远小于此值。

所以，“不能任意乘以配位数”在数学上正确；但这个特定数值并没有显示常见配位数下的 pair extrapolation 已经与总能量冲突。真正的多体非加性仍需由一个共同优化的 cluster 计算来确定。

### \(r>1\) 的能量不能与 \(w=1.6\) 的 pair 结果混用

同一 JSON 给出
\[
J(r>1)/(8\pi^2)
=1.9897222876485987\times10^{-4}.
\]
如果一个 cluster 确实在每个 cell 的整个 \(r<1\) 区域保持不变，那么一对 cells 的 saving 满足
\[
S_2/(8\pi^2)\le
3.9794445752971974\times10^{-4}.
\]
但 \(w=1.6\) 的几何构造只保证 \(r<0.162747\) 不动。因此上述 \(r>1\) 预算不适用于这个 pair witness，除非另有构造证明重叠后仍完整保留 \(r<1\)。

还有一个数值层面的区别：不等式本身是精确的，而
\(0.151063395\) 和 \(1.98972\times10^{-4}\) 来自网格积分。文件中
\[
J_{\mathrm{grid}}-J_{\mathrm{record}}
=2.2143389589\times10^{-7},
\]
所以这些 exterior 数应称为高精度数值估计，而不是 Arb 区间值。

二次近似下，更完整的表述是：令 \(v_i=Ah_i\)，则
\[
\left\|\sum_i v_i\right\|_{L^2}^2
=\sum_i\|v_i\|^2+2\sum_{i<j}\langle v_i,v_j\rangle\ge0.
\]
所有交叉项来自同一个半正定 Gram 矩阵，因此不能把每一对的最优相位当作互相独立的数据。不过这个半正定性本身并不排除有限配位图上若干 pair saving 同时出现。

---

## 2. 加权一维问题的精确解

令
\[
v=q',\qquad f=v'+4v=q''+4q'.
\]
端点条件等价于
\[
v(0)=v(T)=0,\qquad \int_0^T v\,dt=\Delta.
\]
所求为
\[
E_T=\min\int_0^T e^{4t}f(t)^2\,dt.
\]

Euler–Lagrange 方程给出
\[
f(t)=C+\frac{\mu}{4}e^{-4t}.
\]
由 \(v(0)=0\) 得
\[
v(t)=\frac C4(1-e^{-4t})
     +\frac{\mu}{4}t e^{-4t}.
\]
写
\[
\varepsilon=e^{-4T},
\]
由 \(v(T)=0\) 可得
\[
C=-\frac{\mu T\varepsilon}{1-\varepsilon}.
\]
再由 \(\int_0^Tv=\Delta\) 得
\[
\Delta=\mu D_T,
\]
其中
\[
\boxed{
D_T=
\frac{1-e^{-4T}}{64}
-\frac{T^2e^{-4T}}{4(1-e^{-4T})}.
}
\]
对极小解分部积分可得
\[
E_T=\mu\Delta,
\]
因此
\[
\boxed{
E_T=\frac{\Delta^2}{D_T}.
}
\]

由于
\[
D_T\longrightarrow \frac1{64},
\]
所以
\[
\boxed{
E_T\longrightarrow64\Delta^2.
}
\]
取
\[
\Delta=\log 2.196=0.7866375236472842
\]
便得到
\[
64\Delta^2=39.60310999103562,
\]
与 `neutral_mode_resistance.json` 完全一致。文件中的
\[
E_2/(64\Delta^2)=1.022298659996459,
\]
\[
E_4/(64\Delta^2)=1.0000289223796248
\]
也正好由上式给出。

半无限区间上还有一个简短证明。夹持条件给出
\[
4\Delta=\int_0^\infty f(t)\,dt.
\]
加权 Cauchy–Schwarz 不等式给出
\[
(4\Delta)^2
\le
\left(\int_0^\infty e^{4t}f^2dt\right)
\left(\int_0^\infty e^{-4t}dt\right)
=\frac14E,
\]
因而
\[
E\ge64\Delta^2.
\]
等号由
\[
f(t)=16\Delta e^{-4t},\qquad
q'(t)=16\Delta\,t e^{-4t}
\]
实现。

### 无权情形也可解析求解

对
\[
E_T^{(0)}=\int_0^T(v'+4v)^2dt
\]
利用 \(v(0)=v(T)=0\)，交叉项积分为零，因此
\[
E_T^{(0)}
=\int_0^T\bigl((v')^2+16v^2\bigr)dt.
\]
精确最小值为
\[
\boxed{
E_T^{(0)}
=
\frac{16\Delta^2}
{T-\frac12\tanh(2T)}
\sim\frac{16\Delta^2}{T}.
}
\]
所以脚本中的无权数值趋势也正确，并且不需要数值 BVP 才能建立。

### “resistance” 的倒数约定

脚本记录的是
\[
\texttt{resistance}=\frac{\Delta^2}{E_T}=D_T
\longrightarrow\frac1{64}.
\]
因此有两个不同但常用的系数：

- energetic coefficient：
  \[
  E_T/\Delta^2\to64;
  \]
- compliance-type coefficient：
  \[
  \Delta^2/E_T\to1/64.
  \]

在
\[
|\Delta\Phi|^2
\le \frac{P}{8\pi^2}R_\Phi
\]
这种写法中，\(R_\Phi\) 对应第二种系数，而不是 \(64\)。实际几何中还要乘入 orbit 体积、角向积分和 Ricci 分量比较常数。

### 夹持导数是机制的一部分

端点值不相同本身不足以产生该正作用量。若不固定初始导数，则
\[
q(t)=\Delta(1-e^{-4t})
\]
满足
\[
q(0)=0,\qquad q(\infty)=\Delta,\qquad
q''+4q'=0,
\]
因而作用量为零；但它有 \(q'(0)=4\Delta\)。

所以 \(64\Delta^2\) 来自“端点位移 + 两端近似零斜率 + 指数体积权重”的组合。几何应用必须控制 Rossi 端截面上的 \(q'\)，不能只控制其渐近值 \(\Delta\)。

---

## 3. 为什么这仍只是对角 coercivity 的条件性机制

由 Step 13 的 Ricci 公式，写
\[
L_i=\log a_i,\qquad y_i=L_i',\qquad
H=y_1+y_2+y_3,\qquad q=L_2-L_3,
\]
并把代数势项记作 \(\operatorname{Pot}_i\)。则有精确恒等式
\[
R_{22}-R_{33}
=-q''-Hq'
+\operatorname{Pot}_2-\operatorname{Pot}_3.
\]
因此
\[
q''+4q'
=-(R_{22}-R_{33})
+\bigl(\operatorname{Pot}_2-\operatorname{Pot}_3\bigr)
+(4-H)q'.
\]
而
\[
R_{22}-R_{33}
=(\operatorname{Ric}^{\circ})_{22}
-(\operatorname{Ric}^{\circ})_{33},
\]
所以
\[
|R_{22}-R_{33}|^2
\le 2|\operatorname{Ric}^{\circ}|^2.
\]

这说明 Ricci defect 确实直接控制中性模的一个主要 forcing 分量；但 \(q''+4q'\) 并不在整个对角 cell 上精确等于该 Ricci 分量。还存在：

- \(H-4\) 项；
- Bianchi IX 势差；
- 有限截面处的非零 \(q'\)；
- 实际 orbit 体积 \(a_1a_2a_3\) 与 \(e^{4t}\) 的比较系数；
- 径向坐标平移带来的整体体积因子。

在统一 ACH 管中，若能得到
\[
a_1a_2a_3\ge c_{\mathrm{vol}}e^{4t},
\]
并把额外项吸收到 Ricci defect 或可控小量中，则会产生形如
\[
\mathcal A_T(q)
\le C\,P_{\mathrm{tube}}+o(1).
\]
若同时有
\[
|q(T)-q(0)|\ge\Delta_0-o(1),\qquad
q'(0),q'(T)=o(1),
\]
那么一维结果给出
\[
P_{\mathrm{tube}}
\ge \frac{64}{C}\Delta_0^2-o(1).
\]
这正是一个可用的对角 coercivity 机制。

当前材料中还没有提供上述统一比较。尤其是：

1. \(\rho\gtrsim2.196\) 来自 floating-point Einstein shooting，尚无覆盖全部 bolt 参数的 interval enclosure；
2. 低 \(P\) 序列尚未被证明必须进入并长时间停留在统一非塌缩 ACH 管；
3. 还没有排除通过小 orbit-volume coefficient、离开 ACH 动力区或较大初始 \(q'\) 来输送 Rossi 位移；
4. 非对角度量没有全局定义的单一 \(q=\log(a_2/a_3)\)，需要一个不依赖对称性的替代几何量。

因此，模型结果准确地排除了“在保持非塌缩 ACH 几何和夹持斜率时，仅靠把过渡拉长便令作用量趋零”这一机制。它尚未给出
\(\mathfrak P_{1,0}>0\)、\(\mathfrak J_{1,0}>0\) 或全体允许度量上的 Einstein gap。

---

## 4. \(X=32\) 与 \(X=64\) 区间结果的精确含义

两个 Arb 输出给出以下归一化区间：

\[
\begin{array}{c|cc}
 & J_6/(8\pi^2)&P/(8\pi^2)\\ \hline
X=32&
[0.9987367698625724,\ 0.9987367698714824]&
[0.9987321473767184,\ 0.9987321473883820]\\[2mm]
X=64&
[0.9987027644738578,\ 0.9987027644835269]&
[0.9987000858929286,\ 0.9987000859072952].
\end{array}
\]

由此得到固定 \(X=64\) profile 的严格上界
\[
\boxed{
J_6/(8\pi^2)
\le0.9987027644835269,
}
\]
\[
\boxed{
P/(8\pi^2)
\le0.9987000859072952.
}
\]
相应的严格 depletion 为
\[
1-\frac{J_6}{8\pi^2}
\ge0.0012972355164731,
\]
\[
1-\frac{P}{8\pi^2}
\ge0.0012999140927048.
\]

而且两个 \(X\) 的区间不相交：
\[
0.9987027644835269
<
0.9987367698625724,
\]
所以 \(X=64\) 的固定 metric 确实严格优于 \(X=32\)，差值至少约
\[
3.40054\times10^{-5}
\]
于 \(J_6/(8\pi^2)\) 单位。相同结论也适用于 \(P\)。

在四维中还有
\[
J_6-P
=\frac14\int(R+24)^2\,d\mu\ge0.
\]
\(X=64\) 数据给出其归一化值约
\[
2.67858\times10^{-6},
\]
说明该 profile 的 scalar defect 已比 trace-free 部分小许多，但并非严格为零。

若这些记录的参数化按说明自动保证全区间正定、bolt 光滑和 exact-CH 拼接，则对包含这些度量的 cell 类有
\[
\frac{\mathfrak J_{1,0}}{8\pi^2}
\le0.9987027644835269,
\qquad
\frac{\mathfrak P_{1,0}}{8\pi^2}
\le0.9987000859072952.
\]
两个 JSON 本身直接认证的是固定记录的积分区间；其中 `pointwise` 只列出五个采样位置，因此全区间正定与端点光滑仍由 profile 的重构公式承担，而不是由这几行 pointwise 数据单独承担。

`float_record` 与 Arb 中心相差约 \(10^{-10}\)，大于 Arb 半径；这表示普通浮点积分没有达到 Arb 输出的精度。正文采用 Arb 区间而不采用 `float_record` 的末位数字是正确的。

这些结果没有给出：

- \(X\to\infty\) 的极限存在；
- 极限值约为 \(0.9987\) 的定理；
- 完整有限能量 metric 的存在；
- 当前有限维 profile 已达到最小值；
- cell infimum 的正下界。

特别是 \(X=64\) 的梯度无穷范数仍为 \(3.2\times10^{-3}\)，这不影响固定 profile 的积分认证，但意味着继续优化仍可能产生可见下降。

---

## 对 Einstein-gap 研究的最强可靠含义

现有材料共同建立了以下三点：

1. **显式上界取得严格改进。**  
   \(X=64\) metric 把当前 cell cost 严格压到
   \[
   J_6/(8\pi^2)<0.998703,\qquad
   P/(8\pi^2)<0.998701.
   \]
   这是可直接进入后续全局 gluing 上界的定量输入。

2. **长 ACH collar 并不会在夹持、非塌缩模型中自动稀释 Rossi 位移。**  
   精确一维定理给出
   \[
   \inf\mathcal A_T\to64\Delta^2,
   \]
   并识别了指数 orbit-volume growth 是保持有限正代价的机制。

3. **正的对角 cell 下界已有明确的数学形态。**  
   一旦获得统一 ACH 进入、orbit-volume 下比较、近零端点斜率以及 Rossi 位移的 interval separation，就会得到
   \[
   P_{\mathrm{cell}}\ge c\,\Delta_0^2.
   \]
   当前缺少的是这些几何比较与紧致性结果，而不是一维变分常数。

因此，Step 14 最有力的综合结论是：它同时给出了一个经过区间算术认证的更优上构造，以及一个解释“为何无限拉长 collar 未必把 defect 降到零”的精确模型定理；但正的 Einstein gap 仍取决于把该模型嵌入真实对角 ODE，并进一步处理非对角退化。
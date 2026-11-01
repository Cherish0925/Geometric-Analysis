# TTCS Independent Branch Record

```json
{
  "step_id": 1,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md",
    "Sessions/S0910A02/workspace/notes/step1_initial_resolution_and_routes.md",
    "Skills/qiushi-yau26/references/research/20260910.tex",
    "Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md"
  ]
}
```

## Task

Adversarially verify the Step 1 package for Yau Problem 26. Check the quantifier reduction Q_n <=> P_n^+ or P_n^-, the refutation burden, the corrected Min-Oo scope, and especially the Calabi/orbifold scaling claim: Morteza--Viaclovsky remainder O(t^2 rho^2) can become small in g_t-operator norm but the nonzero t*lambda*o obstruction term is order one, so current nonexistence examples do not directly yield delta_sigma->0. Identify any mathematical errors, hidden target changes, source overclaims, or missing assumptions that could materially alter the next research route. Suggest the sharpest next checks that would settle the most important uncertainties.

## Output

# 科学核验备忘录

## 总结

Step 1 的三个核心数学判断均成立：

1. 固定维数中
   \[
   Q_n\Longleftrightarrow P_n^+\vee P_n^-
   \]
   的量词归约正确。
2. 否定整体命题确实需要某个固定维数 \(n\) 中同时否定正、负两支；两支可使用不同流形，但维数必须相同。
3. Morteza–Viaclovsky 的估计经 \(g_t\)-算子范数换算后，余项至多为 \(O(t^{1/2})\)，而 \(t\lambda o\) 在固定 Calabi 核心点产生非零常数量级的各向异性。因此，对固定基轨形且 \(\lambda\ne0\) 的构造，不能得到 \(\delta_\sigma\to0\)。

有几项需要写得更精确：Min-Oo 原文中的几何量仍受 OCR 干扰；Calabi 结论中的“\(\lambda\ne0\)”是固定基轨形陈述；\(\lambda=0\) 只有在轨形 Einstein 常数 \(\Lambda\ne0\) 时才直接产生某个 \(\pm1\) 分支；多奇点消解需要逐核处理全部局部系数；Morteza–Viaclovsky 的紧致结果排除的是指定加权邻域中的 Einstein 度量，而不是底层光滑流形上的全部 Einstein 度量。

---

## 1. 量词归约与反例责任

设 \(Q_n\) 由某个区间 \([a,b]\), \(a<b\), 实现。任意非退化实区间都含有闭子区间
\[
[u,v]\subset[a,b],\qquad u<v,\qquad uv>0.
\]
置
\[
\mu=\frac{u+v}{2},\qquad
\sigma=\operatorname{sign}\mu,\qquad
\varepsilon=\frac{v-u}{|u+v|}.
\]
同号性给出 \(0<\varepsilon<1\)。

若
\[
\delta_\sigma(h)\le\varepsilon,
\]
则 \(A_h=h^{-1}\Ric_h\) 的谱包含于
\[
[\sigma-\varepsilon,\sigma+\varepsilon].
\]
令
\[
g=\frac{h}{|\mu|}.
\]
由
\[
A_{cg}=c^{-1}A_g
\]
可得
\[
A_g=|\mu|A_h.
\]
正号时谱恰落在
\[
[|\mu|(1-\varepsilon),|\mu|(1+\varepsilon)]=[u,v],
\]
负号时谱恰落在
\[
[-|\mu|(1+\varepsilon),-|\mu|(1-\varepsilon)]=[u,v].
\]
所以 \(Q_n\Rightarrow P_n^\sigma\)。反向只需取
\[
[a,b]=[\sigma-\varepsilon,\sigma+\varepsilon].
\]

因此
\[
\neg Q_n
\Longleftrightarrow
\neg P_n^+\wedge\neg P_n^-,
\]
而
\[
\neg\bigl(\forall n\ge2\,Q_n\bigr)
\Longleftrightarrow
\exists n\ge2\,
\bigl(\neg P_n^+\wedge\neg P_n^-\bigr).
\]
Step 1 关于“同一固定维数、两支都要有误差趋零的无 Einstein 序列”的表述正确。两支中的流形无需相同。

这里没有对用户给定目标作隐性替换。1982 年原页尚未逐字取得，但用户已经明确指定闭、连通、光滑实流形；Step 1 使用的正是该对象类别。

---

## 2. Min-Oo 定理的精确后果

检索对象的引言 OCR 将类 \(\mathcal M^-(n,\Lambda)\) 的第二个条件破坏成了不可直接读取的字符串。不过论文第 3 节采用
\[
\max|K(0)|=1,\qquad d(0)<\Lambda,
\]
这与尺度不变量
\[
d(g)^2\max|K_g|<\Lambda^2
\]
完全对应。因此 Step 1 的修正读法有很强的正文支撑；原 PDF 页图仍可消除最后的排印不确定性。

Min-Oo 的 Ricci 偏差不是 \(\delta_-\)，而是
\[
\max_{SM}\left|\frac{n\,p}{r}-1\right|,
\]
其中 \(p(v)=\Ric(v,v)\)，\(r\) 是平均标量曲率。二者可显式转换。若
\[
\delta_-(g)\le\delta<1,
\]
写
\[
p=-1+e(x,v),\qquad |e(x,v)|\le\delta.
\]
又设
\[
\frac rn=-1+\eta,\qquad |\eta|\le\delta.
\]
于是
\[
\left|\frac{np}{r}-1\right|
=
\left|\frac{-1+e}{-1+\eta}-1\right|
=
\frac{|e-\eta|}{|1-\eta|}
\le\frac{2\delta}{1-\delta}.
\]
同时 \(r<0\)。

由此可严格推出：实维 \(n>3\) 中，若一列无任何 Einstein 度量的闭流形满足
\[
\delta_-(g_j)\to0,
\]
则
\[
d(g_j)^2\max|K_{g_j}|\to\infty.
\]
证明是：若存在无限子列使该量被 \(L\) 控制，固定取 \(\Lambda>\sqrt L\)，上述标准化偏差便趋于零，最终小于 Min-Oo 的 \(\varepsilon(n,\Lambda)\)，与每个底层流形无 Einstein 度量矛盾。

因此，在 Min-Oo 条件的原始公式确认后，Step 1 中“或落在精确标准化之外”这一备用措辞可以删去：\(\delta_-<1\) 已经给出 \(r<0\) 及标准化误差控制。维数 \(n>3\) 必须保留。

---

## 3. Calabi 消解中的无权算子范数换算

为避免与 Yau 问题的实维 \(n\) 混淆，记 Morteza–Viaclovsky 的复维为 \(q\ge3\)，实维为 \(2q\)。在 Calabi 区域中
\[
h_t=g_{\rm cal}+t h,\qquad
g_t=t h_t=t(g_{\rm cal}+t h)
\]
位于固定核心；Lemma 4.2 给出
\[
\Ric_{g_t}-\Lambda g_t
=
t\lambda\chi_t o+R_t,
\qquad
|\nabla^kR_t|_{g_{\rm cal}}
\le C_k t^2\rho^{2-k}.
\]

### 3.1 余项确实趋于零

由论文中的
\[
|h|_{g_{\rm cal}}\le C\rho^2,
\qquad
\rho\le2t^{-1/4},
\]
得到
\[
|t h|_{g_{\rm cal}}\le C t\rho^2\le C t^{1/2}.
\]
拼接区两侧的度量也都与 \(t g_{\rm cal}\) 一致到 \(O(t^{1/2})\)，故在整个 \(X^t\) 上有统一双边比较
\[
g_t\asymp t g_{\rm cal}.
\]
对称 \((0,2)\) 张量的算子范数因此满足
\[
|R_t|_{g_t,\mathrm{op}}
\le C t^{-1}|R_t|_{g_{\rm cal}}
\le C t\rho^2
\le C t^{1/2}.
\]
在固定 \(\rho\) 的核心点，所得估计更强，为 \(O(t)\)。

所以 Step 1 对余项的换算正确。

### 3.2 非零首阶阻碍保持非零常数量级

在固定核心点 \(p\) 上，取例如 \(r(p)=1\)。对充分小的 \(t\)，有 \(\chi_t(p)=1\)，且
\[
g_t(p)=t(g_{\rm cal}+t h)(p).
\]
因而
\[
A_{g_t}(p)
=
g_t^{-1}\Ric_{g_t}(p)
=
\Lambda I+\lambda\,g_{\rm cal}^{-1}o(p)+O(t).
\]

显式公式
\[
o=\frac1{1+r^{2q}}
\left(
-\overline g_{FS}
+(q-1)d\bar r^2
+(q-1)\bar\theta^2
\right)
\]
表明，在 \(r=1\) 处，
\[
O:=g_{\rm cal}^{-1}o
\]
的特征值为
\[
-\frac12
\quad\text{及}\quad
\frac{q-1}{2}.
\]
因此
\[
\|O\|_{\mathrm{op}}=\frac{q-1}{2},
\qquad
\inf_{a\in\mathbb R}\|O-aI\|_{\mathrm{op}}=\frac q4.
\]
该项既不趋零，也不能通过改变目标标量吸收。

若 \(\Lambda\ne0\)，自然标准化
\[
\widehat g_t=|\Lambda|g_t,\qquad
\sigma=\operatorname{sign}\Lambda
\]
给出
\[
\liminf_{t\to0}\delta_\sigma(\widehat g_t)
\ge
\frac{q-1}{2}\frac{|\lambda|}{|\Lambda|}>0.
\]
更一般地，任取常数缩放 \(c_tg_t\)，外部区域满足
\[
A_{c_tg_t}=c_t^{-1}\Lambda I.
\]
若其接近 \(\sigma I\)，必有
\[
c_t\to|\Lambda|,\qquad \sigma=\operatorname{sign}\Lambda.
\]
固定核心点随后仍留下
\[
\frac{\lambda}{|\Lambda|}O.
\]
所以其他常数缩放也不能消除该各向异性。

若 \(\Lambda=0\)，外部区域上 \(A=0\)，故任何常数缩放都满足
\[
\delta_\pm\ge1.
\]
零中心的近 Ricci-flat 族不能直接转成 \(P^\pm\)。

这验证了 Step 1 的核心判断：固定基轨形且 \(\lambda\ne0\) 时，现有首阶阻碍构造不能给出 \(\delta_\sigma\to0\)。

### 3.3 \(\lambda=0\) 时的精确收益

若
\[
\lambda=0,\qquad \Lambda\ne0,
\]
同一估计立即给出
\[
\delta_{\operatorname{sign}\Lambda}
\bigl(|\Lambda|g_t\bigr)
\le
C|\Lambda|^{-1}t^{1/2}\to0.
\]
因此，“首阶系数消失”不是仅仅改善加权残差；它确实产生 Yau 问题所需的无权逐点 Ricci 夹逼输入。此时尚缺的是底层光滑流形上全部 Einstein 度量的排除。

---

## 4. 需要补入 Step 1 的几项精确说明

### 4.1 固定基轨形与变化基轨形必须区分

“\(\lambda\ne0\) 导致常数量级误差”对固定轨形成立。若使用一列不同轨形并满足
\[
\frac{|\lambda_j|}{|\Lambda_j|}\to0,
\]
则每个 \(\lambda_j\) 虽非零，标准化后的核心误差仍可能趋零；每个构造常数 \(C_j\) 可通过选择更小的 \(t_j\) 吸收。现有命名例子，特别是 Kähler–Einstein 情形，其首阶系数是 \(\Lambda\) 的维数倍数，不展示这种现象，但一般变化族尚未被上述缩放论证排除。

### 4.2 多奇点需要逐个局部系数消失

足球轨形有两个奇点。只消解一个奇点通常仍留下轨形奇点，不能作为 Yau 问题中的光滑输入。完全消解时，每个 Calabi 核心应出现自己的
\[
t_a\lambda_a o_a.
\]
即使某个全局投影中不同奇点的积分相消，逐点上确界仍会看见每个非零 \(\lambda_a\)。固定基轨形要获得无权紧夹逼，需要每个局部系数都被消去，或为每个核心构造匹配的全局参数。所给 Morteza–Viaclovsky 文本主要写单奇点模型，多点版本需要独立推导。

### 4.3 Morteza–Viaclovsky 的维数不是四维

该论文采用复维 \(q\ge3\)，对应实维至少六。四维 Eguchi–Hanson 情形具有额外旋转参数，不能直接由其高维公式代替。Ozuch 的例子位于实维四，而 Morteza–Viaclovsky 的 Calabi结果位于实维至少六；二者不能直接拼成同一维数中的正、负两支反例。

### 4.4 局部非存在不等于底层全局非存在

Morteza–Viaclovsky Theorem 1.1 排除的是满足指定加权 \(C^3\) 邻近条件的 Einstein 度量。Ozuch 的 Example 1 排除的是具有指定 GH 极限的 Einstein 度量序列。这两项都没有证明相应光滑流形不承载远离该退化模型的 Einstein 度量。Step 1 已意识到这一点，后续文字应持续把这两种结论分开。

### 4.5 公式抽取有两个需要原页确认的位置

所给文本中：

- Lemma 4.1 的陈述含 \(t\lambda o\)，但证明抽取的一行似乎漏掉了一个 \(t\)；Taylor 展开及 Lemma 4.2 均支持陈述中的 \(t\lambda o\)。
- Proposition 3.2 使用 \(\|o\|_{L^2}^2\)，Proposition 3.5 的抽取式看起来出现 \(\|o\|_{L^2}\)。阻碍是否为零不受影响，但若需要精确计算 \(\lambda/\Lambda\)，必须回看原 PDF。

---

## 5. 最有判别力的后续核验材料

1. **`minoo_delta_corollary.tex`**  
   包含原 PDF 定理页图、\(\mathcal M^-(n,\Lambda)\) 的逐字符转写，以及
   \[
   \max_{SM}\left|\frac{np}{r}-1\right|
   \le\frac{2\delta_-}{1-\delta_-}
   \]
   的完整推导。该文件可把“反例序列必有 \(d^2\max|K|\to\infty\)”固定成可直接引用的推论。

2. **`calabi_C0_operator_scaling.tex`**  
   陈述并证明
   \[
   |R_t|_{g_t,\mathrm{op}}\le Ct^{1/2},
   \qquad
   A_{g_t}(p)\to\Lambda I+\lambda O(p),
   \]
   再记录 \(r=1\) 处 \(O\) 的显式谱。这个 TeX 片段能独立解决当前最重要的缩放疑问。

3. **多奇点局部模型公式**  
   对每个核心写成
   \[
   \Ric_{g_{\mathbf t}}-\Lambda g_{\mathbf t}
   =
   \sum_a t_a\lambda_a\chi_a o_a+R_{\mathbf t},
   \]
   并证明
   \[
   \sup|R_{\mathbf t}|_{g_{\mathbf t},\mathrm{op}}\to0.
   \]
   该公式会明确积分相消为何不能消除逐点误差。

4. **候选消解的微分同胚类型与全符号 Einstein 排除证明**  
   对每个 \(\lambda=0\)、\(\Lambda\ne0\) 的紧致轨形候选，需要明确：所有奇点均已消解；所得对象为闭光滑流形；已有拓扑或光滑结构结果排除任意 \(\lambda\in\mathbb R\) 的 Einstein 度量。现有来源没有提供这一部分。

5. **变化轨形的无量纲首阶系数表**  
   记录
   \[
   \Lambda_j,\qquad \lambda_j,\qquad
   \lambda_j/\Lambda_j,
   \]
   以及各拼接常数。它能区分固定非零首阶项与“每项非零但比值趋零”的可能族。

6. **Anderson 1989 Corollary B(4) 与 Ye 1993 的原始定理文本**  
   需要完整记录几何参数依赖、范数、微分同胚结论和输出度量。Step 1 没有把未取得的内容当成纯 Ricci 定理，这一点处理正确；原文仍可能显著改变经典基线的精确表述。

整体而言，Step 1 的主要逻辑和 Calabi 缩放判断可靠。最重要的数学修正是：把固定基轨形、变化基轨形、\(\Lambda=0\)、多奇点以及“指定邻域内无解”和“底层流形无任何 Einstein 度量”五种情形明确分开。
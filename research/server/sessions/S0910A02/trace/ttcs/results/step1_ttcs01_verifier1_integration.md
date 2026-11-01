# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 1,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step1_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step1_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Adversarially verify the Step 1 package for Yau Problem 26. Check the quantifier reduction Q_n <=> P_n^+ or P_n^-, the refutation burden, the corrected Min-Oo scope, and especially the Calabi/orbifold scaling claim: Morteza--Viaclovsky remainder O(t^2 rho^2) can become small in g_t-operator norm but the nonzero t*lambda*o obstruction term is order one, so current nonexistence examples do not directly yield delta_sigma->0. Identify any mathematical errors, hidden target changes, source overclaims, or missing assumptions that could materially alter the next research route. Suggest the sharpest next checks that would settle the most important uncertainties.

## Integrated Scientific Memo

# Step 1 核验结论

Step 1 的核心逻辑成立，尤其是：

\[
Q_n\iff P_n^+\vee P_n^-,
\]

相应反证量词正确；Min-Oo 的适用范围基本修正正确；Morteza–Viaclovsky（MV）Calabi 消解中，余项虽在 \(g_t\)-算子范数下趋零，但非零首阶阻碍 \(t\lambda o\) 变成阶一各向异性，因此现有非消解例子不能直接给出 \(\delta_\sigma\to0\)。

不过应补入若干限定，否则会高估 orbifold 路线的否定力。

## 1. 分支归约与反证责任

若 \(Q_n\) 由 \([a,b]\), \(a<b\), 实现，取同号非退化子区间

\[
[u,v]\subset[a,b],\qquad uv>0.
\]

设

\[
\mu=\frac{u+v}{2},\qquad
\sigma=\operatorname{sign}\mu,\qquad
\varepsilon=\frac{v-u}{|u+v|}\in(0,1).
\]

若 \(\delta_\sigma(h)\le\varepsilon\)，令 \(g=h/|\mu|\)。由

\[
\Ric_{cg}=\Ric_g,\qquad A_{cg}=c^{-1}A_g
\]

得到 \(A_g=|\mu|A_h\)，其谱落入 \([u,v]\)，故 \(Q_n\Rightarrow P_n^\sigma\)。反向取区间
\([\sigma-\varepsilon,\sigma+\varepsilon]\) 即得。

因此固定维数中

\[
\neg Q_n\iff \neg P_n^+\wedge\neg P_n^-,
\]

而整体命题的否定为

\[
\neg\forall n\ge2\,Q_n
\iff
\exists n\ge2\,
(\neg P_n^+\wedge\neg P_n^-).
\]

两支反例可以使用不同流形，但必须位于同一固定维数；每支都需要误差趋零的无 Einstein 序列，一个固定小误差实例不够。跨零区间确实不是第三分支。这一归约没有改变用户指定的研究目标。

## 2. Min-Oo：可强化为严格必要退化结论

原文将 \(d\) 定义为直径；第 3 节归一化

\[
\max |K(0)|=1,\qquad d(0)<\Lambda,
\]

支持其尺度不变量条件为

\[
d(g)^2\max |K_g|<\Lambda^2.
\]

因此 Step 1 对 OCR 的纠正可信；但最好仍从 PDF 页图逐字符确认定理开头的公式。

Min-Oo 使用的缺陷为

\[
\max_{SM}\left|\frac{n\,p}{r}-1\right|,
\]

其中 \(p(v)=\Ric(v,v)\)，\(r\) 为平均标量曲率。若

\[
\delta_-(g)\le\delta<1,
\]

则可写 \(p=-1+e\)、\(r/n=-1+\eta\)，其中
\(|e|,|\eta|\le\delta\)，从而

\[
\left|\frac{np}{r}-1\right|
=
\frac{|e-\eta|}{|1-\eta|}
\le \frac{2\delta}{1-\delta},
\qquad r<0.
\]

所以对任意实维 \(n>3\)，若无 Einstein 度量序列满足
\(\delta_-(g_j)\to0\)，则必有

\[
d(g_j)^2\max |K_{g_j}|\longrightarrow\infty.
\]

否则取该量有界的子列和一个固定 \(\Lambda\)，最终会触发 Min-Oo 定理。故 Step 1 中“或落在精确标准化之外”的保留语可删除：\(\delta_-<1\) 已自动保证负平均标量曲率和标准化缺陷趋零。需要保留的是 \(n>3\) 及阈值依赖 \(\Lambda\)，所以它仍不能推出纯 Ricci 的 \(P_n^-\)。

## 3. Calabi 消解：阶一阻碍判断正确，而且有显式下界

MV 采用复维 \(q\ge3\)，即实维 \(2q\ge6\)。在 Calabi 区域，Lemma 4.2 给出

\[
\Ric_{g_t}-\Lambda g_t
=
t\lambda\chi_t o+R_t,
\qquad
|R_t|_{g_{\rm cal}}\le Ct^2\rho^2,
\]

且核心中

\[
g_t=t(g_{\rm cal}+t h),\qquad
\rho\le 2t^{-1/4}.
\]

对 \((0,2)\) 张量，若 \(g_t\asymp t g_{\rm cal}\)，算子范数多出 \(t^{-1}\)。因此

\[
|R_t|_{g_t,\mathrm{op}}
\le Ct^{-1}t^2\rho^2
= Ct\rho^2
\le Ct^{1/2},
\]

在固定核心更是 \(O(t)\)。余项确实一致趋零。

但在固定核心点 \(p\)（例如 \(r(p)=1\)，此处 \(\chi_t=1\)）：

\[
A_{g_t}(p)
=
\Lambda I+\lambda\,g_{\rm cal}^{-1}o(p)+O(t).
\]

由 MV 的显式公式

\[
o=\frac1{1+r^{2q}}
\left[-\overline g_{FS}
 +(q-1)d\bar r^2+(q-1)\bar\theta^2\right],
\]

在 \(r=1\) 处，\(O=g_{\rm cal}^{-1}o\) 的特征值包括

\[
-\frac12,\qquad \frac{q-1}{2}.
\]

所以 \(O\) 非零且非标量，并且

\[
\|O\|_{\mathrm{op}}=\frac{q-1}{2},\qquad
\inf_{a\in\mathbb R}\|O-aI\|_{\mathrm{op}}=\frac q4.
\]

因此该项不能靠改变目标 Einstein 常数吸收。若 \(\Lambda\ne0\)，对自然归一化
\(\widehat g_t=|\Lambda|g_t\)：

\[
\liminf_{t\to0}\delta_{\operatorname{sign}\Lambda}(\widehat g_t)
\ge
\frac{q-1}{2}\frac{|\lambda|}{|\Lambda|}>0.
\]

任何其他常数缩放也无效：外部 Einstein 区迫使缩放因子趋于
\(|\Lambda|\)，核心仍留下 \((\lambda/|\Lambda|)O\)。若 \(\Lambda=0\)，外部区域 \(A=0\)，故对任意缩放都有 \(\delta_\pm\ge1\)。

所以固定基轨形且 \(\lambda\ne0\) 时，不仅未证明 \(\delta_\sigma\to0\)，而是该具体近似族的缺陷具有统一正下界。

### 必须加入的范围限定

1. **固定基轨形与变化族不同。**  
   上述下界依赖 \(|\lambda|/|\Lambda|\)。若轨形随 \(j\) 变化且
   \[
   |\lambda_j|/|\Lambda_j|\to0,
   \]
   则每个 \(\lambda_j\ne0\) 仍可能与 Yau 夹逼相容。现有 Kähler–Einstein 非例中该比值是维数阶常数，但一般变化族尚未被排除。

2. **多奇点必须逐核消阻。**  
   完全光滑化时，每个核心一般出现
   \[
   t_a\lambda_a\chi_a o_a.
   \]
   不同奇点的积分投影相消不能消除 \(C^0\) 上确界；必须逐个令
   \(\lambda_a=0\)，或逐核引入能消除各局部项的参数。

3. **MV 高维结果不能直接移植到四维。**  
   MV 的此处结论是实维至少六；四维 Eguchi–Hanson 情形有额外旋转参数。Ozuch 的四维例子与 MV 高维 Calabi 非例不能直接组合成同一维数的两支反例。

4. **只排除邻近解。**  
   MV Theorem 1.1 排除指定加权 \(C^3\) 邻域中的 Einstein 度量；Ozuch 排除具有指定 GH 极限的 Einstein 序列。二者都没有证明消解流形上不存在远处、不同符号或不同几何类型的 Einstein 度量。

5. **源文本有公式抽取瑕疵。**  
   Lemma 4.1 证明中的一行似乎漏了 \(t\)，但定理陈述、Taylor 展开和 Lemma 4.2 都支持 \(t\lambda o\)。Proposition 3.2/3.5 对 \(\|o\|_{L^2}\) 与其平方的抽取也不一致；判断 \(\lambda=0\) 不受影响，但计算精确比值前需查 PDF 原页。

## 4. \(\lambda=0\) 才真正产生 Yau 型输入，但并不产生反例

若每个奇点都有

\[
\lambda=0,\qquad \Lambda\ne0,
\]

则同一估计确实给出

\[
\delta_{\operatorname{sign}\Lambda}
\bigl(|\Lambda|g_t\bigr)
\le C|\Lambda|^{-1}t^{1/2}\to0.
\]

这是 orbifold 路线目前最重要的精确分界：

- \(\lambda\ne0\)：具体消解族有阶一 \(C^0\) 缺陷；
- \(\lambda=0\)、\(\Lambda\ne0\)：得到真正的逐点 Ricci 夹逼；
- \(\Lambda=0\)：只是近 Ricci-flat，不能经常数缩放转成 \(P^\pm\)。

但 \(\lambda=0\) 与已知存在现象存在明显张力：MV 的 AHE 非退化情形在首阶阻碍消失时能构造 Einstein 消解；平坦 Kummer 型例子也确有 Calabi–Yau 消解。它们并不证明紧致情形总存在，却说明“消掉首阶项”不是非存在证据。反例仍需独立证明所得闭光滑流形不承载任何符号的 Einstein 度量。

## 5. 其他需防止的目标漂移

- Ozuch 的
  \[
  \|\Ric(g_i)-3g_i\|_{L^p}\to0,\qquad \Ric(g_i)\ge3g_i
  \]
  不是无权 \(C^0\) 算子夹逼。
- “无具有同一 GH 极限的 Einstein 序列”不是“该流形无 Einstein 度量”。
- Kähler–Einstein 不存在、对称 ansatz 无解或某一拼接程序受阻，都不足以排除一般 Riemannian Einstein 度量。
- 四维任一 \(\delta_\pm\to0\) 候选最终必须满足
  \[
  2\chi>3|\tau|,
  \]
  所以违反或饱和 Hitchin–Thorpe 的流形不能作为任一分支的紧夹逼反例。

## 6. 最有判别力的后续核验

1. **查清紧致 \(\lambda=0\)、\(\Lambda\ne0\) 候选。**  
   对每个奇点验证首阶系数均为零，完成全流形 \(C^0\) 算子范数估计，并计算消解后的光滑拓扑；随后寻找排除所有 Einstein 常数的全局障碍。这一步直接决定 orbifold 反例路线是否仍有实质生命力。

2. **检查变化轨形族。**  
   计算无量纲量
   \[
   \lambda_j/\Lambda_j
   \]
   及各拼接常数，测试“每项阻碍非零但比值趋零”的漏洞。固定轨形的阶一下界不能排除这种族。

3. **写出多奇点逐核公式。**  
   严格证明
   \[
   \Ric-\Lambda g
   =
   \sum_a t_a\lambda_a\chi_a o_a+R_{\mathbf t},
   \qquad
   \|R_{\mathbf t}\|_{g,\mathrm{op}}\to0.
   \]
   这将彻底区分全局投影相消与逐点夹逼。

4. **取得 Anderson 1989 Corollary B(4) 和 Ye 1993 原文。**  
   必须记录阈值究竟依赖哪些体积、直径、导数、注入半径或全曲率参数；这会精确定位经典稳定性与纯 Ricci 命题之间的缺口。

5. **固定 Min-Oo 引用。**  
   从 PDF 页图确认 \(d^2\max|K|<\Lambda^2\)，并将
   \[
   \delta_-\to0,\ \Ein(M_j)=\varnothing
   \Longrightarrow d^2\max|K|\to\infty
   \]
   写成独立引理。

总体上，Step 1 的主要数学判断可靠。最关键的修正不是推翻其结论，而是明确：阶一阻碍只否定当前固定模型的 \(C^0\) 夹逼；真正可能产生 Yau 型输入的是逐核 \(\lambda=0\) 或变化族 \(\lambda_j/\Lambda_j\to0\)，而这两种情形仍完全缺少“底层流形无任何 Einstein 度量”的全局部分。
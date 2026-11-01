# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 43,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step43_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step43_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the terminal spectral density derivation in step43_terminal_density_G_lemma.md. Check: (1) that f = -2q/3 is correct with the stated conventions (q = sqrt(6)|W+| - s, f = 2s/3 - 2*sqrt(2/3)|W+|); (2) that the integral identity int G = (4/9)E - int(b_-)^2 follows from pointwise algebra; (3) that the LeBrun conformal/Yamabe decomposition (4/9)Delta_a = D_spec + D_Yam + D_mono correctly establishes D_spec <= (4/9)Delta_a (in particular, verify from the source at quantitative_deficit_analysis.md eq 24 that D_Yam and D_mono are both nonneg); (4) that Delta_a <= 108pi^2(R - q_top) follows from K <= 3I/2, I = T_M + R, T_M = 2A/3 - q_top, and p >= A; (5) that R <= Q/(8pi^2) uses Ric^0 = E^0 correctly; (6) that the bound applies to the evolved terminal metric without pointwise Ricci pinching. Also verify the coefficient 912 = 864 + 48 in the full density. If any step contains an error, identify the exact formula and the correction.

## Integrated Scientific Memo

# 终端谱密度推导核验结论

为消除原文中 \(E\) 同时表示积分与张量的歧义，记
\[
\mathcal E_{\mathrm{SW}}
=\int_M(s-\sqrt6|W^+|)^2\,d\mu,\qquad
\mathcal E_{\mathrm{Ric}}=\operatorname{Ric}+g,\qquad
Q=\int_M|\mathcal E_{\mathrm{Ric}}|^2\,d\mu .
\]

## 1. \(f=-2q/3\)：正确

令 \(u=|W^+|\)。由
\[
q=\sqrt6u-s,\qquad
f=\frac23s-2\sqrt{\frac23}\,u
\]
以及
\[
2\sqrt{\frac23}=\frac{2\sqrt6}{3},
\]
可得
\[
f=\frac23(s-\sqrt6u)=-\frac23q.
\]
因此
\[
f^2=\frac49(s-\sqrt6|W^+|)^2.
\]

## 2. \(\int G\) 的积分恒等式：正确

由
\[
G=f^2-(b_-)^2
\]
逐点积分即得
\[
\boxed{\int_MG\,d\mu
=\frac49\mathcal E_{\mathrm{SW}}
-\int_M(b_-)^2\,d\mu.}
\]

点态非负性也正确：写
\[
\xi=w+\sqrt{\frac23}u\ge0,\qquad b=f+2\xi\ge f.
\]
若 \(b\ge0\)，则 \(G=f^2\ge0\)；若 \(b<0\)，则 \(f\le b<0\)，所以
\(f^2\ge b^2=(b_-)^2\)。

但原文件 Lemma 1.1 的零点刻画有误。其声称
\[
G=0\iff \xi=0\ \text{or}\ f=0
\]
并不成立；例如 \(\xi=0,f>0\) 时 \(b=f>0\)，从而 \(G=f^2>0\)。

正确公式是
\[
\boxed{
G=0\iff
\bigl(f=0\bigr)\ \text{或}\ \bigl(\xi=0\text{ 且 }f<0\bigr).}
\]
终端校准中 \(f=-3<0\)，故 Lemma 1.2 所用的
\[
G=0\iff\xi=0
\]
仍然成立，终端谱确定不受影响。

## 3. LeBrun 共形/Yamabe 分解：正确，但依赖独立的谱下界

`quantitative_deficit_analysis.md` 式 (24) 给出
\[
\frac49\Delta_a
=
\underbrace{\left(\frac49\mathcal E_{\mathrm{SW}}
-\mathcal B(g)\right)}_{D_{\mathrm{spec}}}
+
\underbrace{\left(\mathcal B(g)-\mathcal B(g_\gamma)\right)}_{D_{\mathrm{Yam}}}
+
\underbrace{\left(\mathcal B(g_\gamma)-32\pi^2p\right)}_{D_{\mathrm{mono}}},
\]
其中
\[
\mathcal B(g)=\int_M(b_-)^2\,d\mu_g.
\]

三项之和确为
\[
\frac49\mathcal E_{\mathrm{SW}}-32\pi^2p
=\frac49\bigl(\mathcal E_{\mathrm{SW}}-72\pi^2p\bigr)
=\frac49\Delta_a.
\]

各项符号为：

- \(D_{\mathrm{spec}}=\int G\ge0\)，由点态代数；
- \(D_{\mathrm{Yam}}\ge0\)，因为 \(g_\gamma\) 是相应广义 Yamabe 泛函的共形极小者；
- \(D_{\mathrm{mono}}\ge0\)，因为 LeBrun 的谱/广义 Yamabe 单极子下界给出
  \[
  \mathcal B(g_\gamma)\ge32\pi^2p.
  \]

故
\[
\boxed{\int G=D_{\mathrm{spec}}\le\frac49\Delta_a.}
\]

需要明确：这个结论不由混合不等式
\[
\mathcal E_{\mathrm{SW}}\ge72\pi^2p
\]
单独推出。它实质上还需要独立的 LeBrun 谱下界
\[
\int(b_-)^2\ge32\pi^2p.
\]
因此 Section 0 中“using only the published SW monopole inequality, Chern–Weil identities, and pointwise algebra”不完整，应加入“LeBrun generalized-Yamabe spectral lower bound”。

## 4. \(\Delta_a\) 上界：正确

设
\[
K=\frac{\mathcal E_{\mathrm{SW}}}{72\pi^2},\qquad I=S+W.
\]
由点态平方恒等式，
\[
K\le\frac32I.
\]
又由 Chern–Weil，
\[
I=T_M+R=\frac{2A}{3}-q_{\mathrm{top}}+R.
\]
选取符号平均给出的单极子类，使 \(p\ge A\)。于是
\[
\begin{aligned}
K-p
&\le K-A\\
&\le\frac32\left(\frac{2A}{3}-q_{\mathrm{top}}+R\right)-A\\
&=\frac32(R-q_{\mathrm{top}}).
\end{aligned}
\]
因此
\[
\boxed{
\Delta_a
=72\pi^2(K-p)
\le108\pi^2(R-q_{\mathrm{top}}).}
\]
同时单极子不等式给出 \(\Delta_a\ge0\)，故这些假设也蕴含
\(R-q_{\mathrm{top}}\ge0\)。

## 5. \(R\le Q/(8\pi^2)\)：正确

令 \(\mathcal E_{\mathrm{Ric}}=\operatorname{Ric}+g\)。在四维中
\[
\operatorname{tr}\mathcal E_{\mathrm{Ric}}=s+4,
\]
从而
\[
\begin{aligned}
\mathcal E_{\mathrm{Ric}}^\circ
&=\operatorname{Ric}+g-\frac{s+4}{4}g\\
&=\operatorname{Ric}-\frac{s}{4}g
=\operatorname{Ric}^\circ.
\end{aligned}
\]
因此
\[
R=\frac1{8\pi^2}\int|\operatorname{Ric}^\circ|^2
=\frac1{8\pi^2}\int|\mathcal E_{\mathrm{Ric}}^\circ|^2
\le\frac{Q}{8\pi^2}.
\]
原文 Step A 的括号内说明较混乱，宜直接替换为上述两行计算，但结论无误。

结合前两步，
\[
\int G
\le\frac49\Delta_a
\le48\pi^2(R-q_{\mathrm{top}}),
\]
故
\[
\boxed{
\int G\le6Q+48\pi^2(-q_{\mathrm{top}})_+.}
\]

## 6. 对演化终端度量的适用性：正确

该估计只要求终端 \(g(T)\) 是同一闭定向光滑四维流形上的光滑度量，并使用：

- Chern–Weil 拓扑恒等式；
- 点态平方恒等式；
- 对任意光滑度量成立的单极子混合估计；
- 拓扑性的符号平均；
- LeBrun 广义 Yamabe 谱下界；
- \(\operatorname{Ric}^\circ=(\operatorname{Ric}+g)^\circ\)。

这些均不要求 \(g(T)\) 满足逐点 Ricci 夹逼。因此只要流确实产生光滑终端度量，并且已有 \(Q(T)\) 的全局控制，该谱密度界就适用。终端 \(Q(T)\) 是否足够小属于上游流分析，非本引理本身的内容。

## 7. 完整密度系数：正确

令
\[
t=s+8\sqrt6|W^+|.
\]
由平方恒等式，
\[
\int t^2=864\pi^2I-576\pi^2K.
\]
利用 \(K\ge p\ge A\) 和
\[
I=\frac{2A}{3}-q_{\mathrm{top}}+R
\]
得到
\[
\int t^2
\le864\pi^2(R-q_{\mathrm{top}})
\le108Q+864\pi^2(-q_{\mathrm{top}})_+.
\]
此外
\[
\int(s+4)^2\le4Q,\qquad \int|E|^2=Q,
\]
以及
\[
\int G\le6Q+48\pi^2(-q_{\mathrm{top}})_+.
\]
故
\[
\boxed{
\int\mathfrak D
\le119Q+912\pi^2(-q_{\mathrm{top}})_+,}
\]
其中
\[
119=1+4+108+6,\qquad
\boxed{912=864+48}.
\]

## 最终判定

主结论及所有请求核验的系数均正确：
\[
\int G\le6Q+48\pi^2(-q_{\mathrm{top}})_+,
\qquad
\int\mathfrak D\le119Q+912\pi^2(-q_{\mathrm{top}})_+.
\]

应修正三处：

1. Lemma 1.1 的零点条件改为
   \[
   G=0\iff f=0\ \text{或}\ (\xi=0,\ f<0).
   \]
2. 避免以 \(E\) 同时表示 SW 标量积分与张量 \(\operatorname{Ric}+g\)。
3. 明示 Step C 依赖独立的 LeBrun 广义 Yamabe 谱下界，而非仅依赖混合 SW 不等式、Chern–Weil 和点态代数。
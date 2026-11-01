# TTCS Independent Branch Record

```json
{
  "step_id": 43,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step43_terminal_density_G_lemma.md",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step43_corrected_negative_IL_theorem.md",
    "Sessions/S0910A03/trace/ttcs/results/step42_ttcs01_verifier2_integration.md"
  ]
}
```

## Task

Verify the terminal spectral density derivation in step43_terminal_density_G_lemma.md. Check: (1) that f = -2q/3 is correct with the stated conventions (q = sqrt(6)|W+| - s, f = 2s/3 - 2*sqrt(2/3)|W+|); (2) that the integral identity int G = (4/9)E - int(b_-)^2 follows from pointwise algebra; (3) that the LeBrun conformal/Yamabe decomposition (4/9)Delta_a = D_spec + D_Yam + D_mono correctly establishes D_spec <= (4/9)Delta_a (in particular, verify from the source at quantitative_deficit_analysis.md eq 24 that D_Yam and D_mono are both nonneg); (4) that Delta_a <= 108pi^2(R - q_top) follows from K <= 3I/2, I = T_M + R, T_M = 2A/3 - q_top, and p >= A; (5) that R <= Q/(8pi^2) uses Ric^0 = E^0 correctly; (6) that the bound applies to the evolved terminal metric without pointwise Ricci pinching. Also verify the coefficient 912 = 864 + 48 in the full density. If any step contains an error, identify the exact formula and the correction.

## Output

# 终端谱密度推导核验备忘

为避免原文件中 \(E\) 同时表示标量积分与二阶张量，以下记
\[
\mathcal E_{\mathrm{SW}}
 :=\int_M(s-\sqrt6|W^+|)^2\,d\mu,
\qquad
\mathcal E_{\mathrm{Ric}}:=\operatorname{Ric}+g,
\qquad
Q:=\int_M|\mathcal E_{\mathrm{Ric}}|^2\,d\mu.
\]

## 1. \(f=-2q/3\) 完全正确

令 \(u=|W^+|\)、\(\alpha=\sqrt{2/3}=\sqrt6/3\)。则
\[
f=\frac23s-2\alpha u
 =\frac23s-\frac{2\sqrt6}{3}u
 =\frac23(s-\sqrt6u).
\]
而 \(q=\sqrt6u-s\)，所以
\[
\boxed{f=-\frac23q}.
\]
因而
\[
f^2=\frac49q^2
=\frac49(s-\sqrt6|W^+|)^2.
\]

## 2. \(\int G\) 的积分恒等式正确

按定义
\[
G_{\rm pt}=f^2-(b_-)^2,\qquad b_-=\min\{b,0\}.
\]
逐点积分立即得到
\[
\boxed{
\int_MG_{\rm pt}\,d\mu
=\frac49\mathcal E_{\mathrm{SW}}
-\int_M(b_-)^2\,d\mu.}
\]

点态非负性也正确。令
\[
\xi=w+\alpha u\ge0,\qquad b=f+2\xi.
\]
若 \(b\ge0\)，则 \(G_{\rm pt}=f^2\ge0\)；若 \(b<0\)，则
\(f\le b<0\)，从而 \(f^2\ge b^2=(b_-)^2\)。

不过 Lemma 1.1 中的零点描述
\[
“G=0\iff \xi=0\ \text{or}\ f=0”
\]
不正确。例如 \(\xi=0,\ f>0\) 时，\(b=f>0\)，故 \(G=f^2>0\)。准确表述是
\[
\boxed{
G_{\rm pt}=0
\iff
\bigl(f=0\bigr)
\ \text{或}\ 
\bigl(\xi=0\ \text{且}\ f<0\bigr).}
\]
终端校准处 \(f=-3<0\)，所以那里仍有
\[
G_{\rm pt}=0\iff\xi=0,
\]
Lemma 1.2 不受这一文字错误影响。

## 3. 广义 Yamabe 分解确实给出
\(\displaystyle D_{\rm spec}\le \frac49\Delta_a\)

为避免与点态 \(G_{\rm pt}\) 混淆，记
\[
\mathcal B(g):=\int_M(b_-)^2\,d\mu_g.
\]
`quantitative_deficit_analysis.md` 的式 (24) 是
\[
\frac49\Delta_a
=
\underbrace{\left(\frac49\mathcal E_{\mathrm{SW}}-\mathcal B(g)\right)}
_{D_{\rm spec}}
+
\underbrace{\left(\mathcal B(g)-\mathcal B(g_\gamma)\right)}
_{D_{\rm Yam}}
+
\underbrace{\left(\mathcal B(g_\gamma)-32\pi^2p\right)}
_{D_{\rm mono}}.
\]
其中：

* 第一项就是
  \[
  D_{\rm spec}=\int_MG_{\rm pt}\,d\mu\ge0.
  \]
* \(g_\gamma\) 是该共形类中的广义 Yamabe 极小度量，所以
  \[
  \mathcal B(g)-\mathcal B(g_\gamma)\ge0.
  \]
* LeBrun 的广义 Yamabe–单极子估计给出
  \[
  \mathcal B(g_\gamma)\ge32\pi^2p,
  \]
  因而第三项非负。

三项相加也直接伸缩为
\[
\frac49\mathcal E_{\mathrm{SW}}-32\pi^2p
=\frac49(\mathcal E_{\mathrm{SW}}-72\pi^2p)
=\frac49\Delta_a.
\]
所以
\[
\boxed{D_{\rm spec}\le\frac49\Delta_a}
\]
成立。这也等价于
\[
\mathcal B(g)\ge32\pi^2p.
\]

这里有一处来源描述需要修正：式 (4.4) 不只是由 Proposition 3.8 的
\(\mathcal E_{\mathrm{SW}}\ge72\pi^2p\)、Chern–Weil 和点态恒等式推出；它还使用了广义 Yamabe 谱函数下界
\(\mathcal B(g)\ge32\pi^2p\)。Section 6 已列出该输入，但 Section 0 的“using only”表述漏掉了它。

## 4. \(\Delta_a\) 的上界系数正确

定义
\[
K=\frac{\mathcal E_{\mathrm{SW}}}{72\pi^2},
\qquad
I=S+W.
\]
点态平方恒等式给出
\[
K\le\frac32I.
\]
Chern–Weil 给出
\[
I=T_M+R=\frac{2A}{3}-q_{\rm top}+R.
\]
对按符号平均选出的单极子类，有 \(p\ge A\)。因此
\[
\begin{aligned}
K-p
&\le K-A\\
&\le\frac32\left(\frac{2A}{3}-q_{\rm top}+R\right)-A\\
&=\frac32(R-q_{\rm top}).
\end{aligned}
\]
乘以 \(72\pi^2\) 后得到
\[
\boxed{
\Delta_a
=72\pi^2(K-p)
\le108\pi^2(R-q_{\rm top}).}
\]
同时 Proposition 3.8 给出 \(\Delta_a\ge0\)，所以在所选单极子类下这些公式还蕴含 \(R-q_{\rm top}\ge0\)。

于是
\[
\int G_{\rm pt}
\le\frac49\Delta_a
\le48\pi^2(R-q_{\rm top}).
\]

## 5. \(R\le Q/(8\pi^2)\) 正确

在四维中
\[
\operatorname{tr}_g(\mathcal E_{\mathrm{Ric}})=s+4,
\]
并且
\[
\begin{aligned}
\mathcal E_{\mathrm{Ric}}^\circ
&=\operatorname{Ric}+g-\frac{s+4}{4}g\\
&=\operatorname{Ric}-\frac{s}{4}g\\
&=\operatorname{Ric}^\circ.
\end{aligned}
\]
正交迹分解给出
\[
|\mathcal E_{\mathrm{Ric}}^\circ|^2
\le|\mathcal E_{\mathrm{Ric}}|^2.
\]
故
\[
\boxed{
R
=\frac1{8\pi^2}\int|\operatorname{Ric}^\circ|^2
\le\frac{Q}{8\pi^2}.}
\]

结合上一节：

* 若 \(q_{\rm top}\ge0\)，
  \[
  \int G_{\rm pt}\le48\pi^2R\le6Q.
  \]
* 若 \(q_{\rm top}<0\)，
  \[
  \int G_{\rm pt}
  \le48\pi^2R+48\pi^2(-q_{\rm top})
  \le6Q+48\pi^2(-q_{\rm top}).
  \]

所以
\[
\boxed{
\int_MG_{\rm pt}\,d\mu
\le6Q+48\pi^2(-q_{\rm top})_+.}
\]

## 6. 对演化终端度量的适用性

上述链只要求：

1. \(g(T)\) 是同一闭定向四维流形上的光滑 Riemann 度量；
2. 相应 Ishida–LeBrun 符号单极子类仍是单极子类；
3. \(Q(T)=\int|\operatorname{Ric}_{g(T)}+g(T)|^2\) 有定义。

Chern–Weil、符号平均和单极子类均不依赖所采用的光滑度量；广义 Yamabe 谱下界适用于任意光滑度量。因此此估计不使用 \(g(T)\) 的逐点 Ricci 夹逼。演化过程只负责产生光滑终端度量及控制 \(Q(T)\)。

## 7. 完整密度中的系数

令
\[
t=s+8\sqrt6|W^+|.
\]
由平方恒等式，
\[
\int t^2
=864\pi^2I-576\pi^2K.
\]
又 \(K\ge p\ge A\)，故
\[
\begin{aligned}
\int t^2
&\le864\pi^2\left(\frac{2A}{3}-q_{\rm top}+R\right)
   -576\pi^2A\\
&=864\pi^2(R-q_{\rm top})\\
&\le108Q+864\pi^2(-q_{\rm top})_+.
\end{aligned}
\]
此外
\[
\int(s+4)^2
=\int|\operatorname{tr}\mathcal E_{\mathrm{Ric}}|^2
\le4Q.
\]
因此
\[
\begin{aligned}
\int\mathfrak D
&\le Q+4Q+
\left(108Q+864\pi^2(-q_{\rm top})_+\right)\\
&\qquad+
\left(6Q+48\pi^2(-q_{\rm top})_+\right)\\
&=119Q+912\pi^2(-q_{\rm top})_+.
\end{aligned}
\]
所以
\[
\boxed{912=864+48}
\]
以及 \(119=1+4+108+6\) 均正确。

## 总核验

终端谱密度主链及常数全部成立。需要修订的具体位置有三处：

1. Lemma 1.1 的 \(G=0\) 等价条件应改为  
   \[
   f=0\quad\text{或}\quad(\xi=0,\ f<0).
   \]
2. 标量积分 \(\mathcal E_{\mathrm{SW}}\) 与张量
   \(\mathcal E_{\mathrm{Ric}}=\operatorname{Ric}+g\) 不应共用符号 \(E\)。
3. 式 (4.4) 还依赖 LeBrun 广义 Yamabe 谱下界；它不是仅由 Proposition 3.8、Chern–Weil 和点态平方恒等式推出。

这些修订不改变
\[
\int G\le6Q+48\pi^2(-q_{\rm top})_+
\]
或
\[
\int\mathfrak D\le119Q+912\pi^2(-q_{\rm top})_+
\]
的结论。
# TTCS Independent Branch Record

```json
{
  "step_id": 43,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step43_period_linear_lebrun_ledger_and_ricci_flow.md",
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A01/workspace/scripts/step43_yamabe_lebrun_ledger.py",
    "Sessions/S1003A01/workspace/data/step43/ledger_x003_X128_N80000.json"
  ]
}
```

## Task

Check the mathematics of the new note Sessions/S1003A01/workspace/notes/step43_period_linear_lebrun_ledger_and_ricci_flow.md, against A02's Step-48 note (LeB_full, Theorem Y, Y0) and the script that produced the numbers. Specifically: (1) Is Proposition 43.1 correct — that maximizing LeBrun's Proposition-4 bound over the sign family a_eps=K+sum eps_i E_i gives Pi_g >= (K.c + sum|E_i.c|)^2/c^2 - A for every c in H^+_g, hence a LINEAR period term 2 sum|e_i|, e_i=E_i.K^+, improving A02's quadratic |K^-|^2+sum|E_i^+|^2; and the exact formulas K.c=A, E_i.c=sigma_i, c^2=A-|sigma|^2, e_i=sigma_i+(G sigma)_i when c=K-sum sigma_i E_i is SD-harmonic? Are the sign conventions (K.E_i=0, E_i^2=-1, monopole classes K +- E_i under the sign-family hypothesis) right? (2) Theorem 43.2 and the scalar consequence Delta V >= 4 pi^2 sum|e_i|. (3) Corollary 43.3: does the ledger really reproduce the first-order slope 6t/pi of the aligned Kahler law P=2(2pi+6t)^2+L/4 (profile Ric=-6g, sigma=3t/pi after rescaling psi=6 omega), including the Yamabe-volume upper estimate 16 hatV = Y^2 <= int s^2 and the Kahler integrals int s = -8pi^2(A+sigma), V=2pi^2(A-sigma^2)? Check c_1(M)=-(K+E) pairings. (4) Remark 43.4 smoothness/strictness argument. (5) The numerical ledger: the tail-free Yamabe-volume identity int s^2 - 576 hatV = int[e^2+48ev-1152v^3-576v^4] (profile scale, e=s+24, v=u-1, equation -6 Lap u + s u + 24u^3=0) and the conversions Ric=-g (g1=6g) giving Delta V = 36 dV_profile, D_W = deltaW + (2/3)DeltaV, Y0 in the form 8pi^2-P(hat g)=4 deltaW-(4/3)DeltaV; the LeBrun integrand (sqrt6|W+|_g - 12u^2)^2 dV_g; and the correction of A02's quoted split. (6) Theorem 43.5 (Ricci flow). Report errors with corrected formulas; do not restate correct parts at length.

## Output

# 数学核验备忘录

## 总结

- Proposition 43.1 的投影论证、符号约定以及 \(c=K-\sum\sigma_iE_i\) 时的精确公式均正确。
- Theorem 43.2 及
  \[
  \Delta V\ge4\pi^2\sum_i|e_i|
  \]
  正确；还能保留若干严格更强的项。
- Corollary 43.3 的 \(c_1(M)\) 配对、缩放 \(\sigma=3t/\pi\) 和线性系数 \(6t/\pi\) 都正确。其 Yamabe 估计其实可以写成无 \(O(t^2)\) 的精确不等式。
- Remark 43.4 的导数公式漏掉了 \(G(0)\sigma'(0)\)。定性严格性仍成立，但定量式需要明确二阶控制所在的参数区间。
- 尾部消除恒等式和尺度转换正确。表格使用的是 `DeltaV_identity`，而 JSON 中名为 `DeltaV`、`D_W`、`fourDeltaV`、`fourD_W` 的主字段仍是直接尾部积分值；这使数据文件和正文表格表面上不一致。
- Theorem 43.5 的永生流部分有完整证明。有限时间部分完全依赖 “family 351, Theorem 1.1” 是否给出同一光滑流形上的光滑延拓；所给材料没有该定理原文，因此这一部分尚不能由当前文件独立确认。

---

## 1. Proposition 43.1

对任意 \(c\in\mathcal H_g^+\)，
\[
(a_\varepsilon^+)^2\ge
\frac{(a_\varepsilon^+\cdot c)^2}{c^2}
=\frac{(a_\varepsilon\cdot c)^2}{c^2}.
\]
取 \(\varepsilon_i=\operatorname{sign}(E_i\cdot c)\)，得到
\[
a_\varepsilon\cdot c=K\cdot c+\sum_i|E_i\cdot c|,
\]
所以
\[
\Pi_g\ge
\frac{(K\cdot c+\sum_i|E_i\cdot c|)^2}{c^2}-A.
\]
即使 \(K\cdot c<0\)，这仍是合法下界；在实际使用的两个选择中 \(K\cdot c>0\)。

令 \(c=K^+\)，记
\[
x=(K^+)^2=A+|K^-|^2,\qquad B=\sum_i|e_i|,
\qquad e_i=E_i\cdot K^+.
\]
则精确地
\[
\Pi_g\ge\frac{(x+B)^2}{x}-A
=|K^-|^2+2B+\frac{B^2}{x}.
\]
因此线性项 \(2\sum|e_i|\) 正确。

不过，这个估计并不逐度量支配 A02 的平均符号估计
\[
\Pi_g\ge |K^-|^2+\sum_i|E_i^+|^2.
\]
例如可以有 \(E_i\cdot K^+=0\) 而 \(E_i^+\ne0\)。最强的直接组合是
\[
\Pi_g\ge\max\left\{
|K^-|^2+\sum_i|E_i^+|^2,\,
|K^-|^2+2\sum_i|e_i|
+\frac{(\sum_i|e_i|)^2}{(K^+)^2}
\right\}.
\]
“线性改进”应理解为在 \(e_i\) 打开的方向上给出一阶代价，而不是对原二次估计的全面支配。

若
\[
c=K-\sum_i\sigma_iE_i\in\mathcal H_g^+,
\]
则由 \(K\cdot E_i=0\)、\(E_i\cdot E_j=-\delta_{ij}\)，
\[
K\cdot c=A,\qquad E_i\cdot c=\sigma_i,\qquad
c^2=A-|\sigma|_2^2.
\]
因此必须有 \(A>|\sigma|_2^2\)，并且
\[
\Pi_g\ge \frac{(A+|\sigma|_1)^2}{A-|\sigma|_2^2}-A.
\]
事实上右端可精确写为
\[
2|\sigma|_1+|\sigma|_2^2+
\frac{(|\sigma|_1+|\sigma|_2^2)^2}{A-|\sigma|_2^2},
\]
所以正文中的
\[
\Pi_g\ge2|\sigma|_1+|\sigma|_2^2
\]
正确。

由 \(K=c+\sum_j\sigma_jE_j\) 取自对偶投影，
\[
K^+=c+\sum_j\sigma_jE_j^+,
\]
故
\[
e_i=E_i\cdot K^+
=\sigma_i+\sum_j(E_i^+\cdot E_j^+)\sigma_j
=\sigma_i+(G\sigma)_i.
\]
这一公式及其符号正确。

吹起后的复曲面约定也一致：
\[
K_M=K+\sum_iE_i,\qquad
c_1(M)=-(K+\sum_iE_i),
\]
而 blow-up 公式确实产生 \(K+\sum_i\varepsilon_iE_i\) 这一符号族。

---

## 2. Theorem 43.2

由 LeB\(_{\rm full}\)
\[
8\pi^2k-P(\hat g)
\le4\Delta V-\frac49I-16\pi^2\Pi_g,
\qquad
I=\int(\sqrt6|W^+|-2)^2,
\]
以及
\[
\Delta V_{\rm free}=\Delta V-2\pi^2\Pi_g,
\]
有
\[
4\Delta V-16\pi^2\Pi_g
=4\Delta V_{\rm free}-8\pi^2\Pi_g.
\]
因此
\[
P(\hat g)\ge
8\pi^2k-4\Delta V_{\rm free}
+8\pi^2\Pi_g+\frac49I.
\]
代入 \(\Pi_g\ge2\sum|e_i|\) 就得到正文方框中的公式。四维中自对偶调和分解在共形变换下保持，因此这里 \(g\) 与 \(\hat g\) 的投影数据一致。

标量曲率估计给出
\[
\Delta V\ge2\pi^2\Pi_g
\ge
2\pi^2\left(
|K^-|^2+2\sum_i|e_i|
+\frac{(\sum_i|e_i|)^2}{(K^+)^2}
\right),
\]
故正文较弱的
\[
\Delta V\ge4\pi^2\sum_i|e_i|
\]
正确。

---

## 3. Corollary 43.3

对单个 Kähler blow-up，
\[
c=\frac{[\psi]}{2\pi}=K-\sigma E,\qquad
c_1(M)=-(K+E).
\]
于是
\[
c_1(M)\cdot c=-(K+E)\cdot(K-\sigma E)=-(A+\sigma),
\]
以及
\[
c^2=A-\sigma^2.
\]
Kähler 恒等式因此给出
\[
\int s\,d\mu=4\pi\,c_1(M)\cdot[\psi]
=-8\pi^2(A+\sigma),
\]
\[
V=\frac12[\psi]^2=2\pi^2(A-\sigma^2).
\]
正文符号正确。

若 \(t=\int_E\omega\) 是 \(\operatorname{Ric}=-6g\) 尺度的 exceptional area，而 \(\psi=6\omega\)，则
\[
2\pi\sigma=\int_E\psi=6t,
\qquad
\sigma=\frac{3t}{\pi}.
\]
单个 exceptional class 时 \(G_{11}\ge0\)，故
\[
e=\sigma(1+G_{11})\ge\sigma.
\]
Theorem 43.2 因而给出
\[
P\ge8\pi^2(1+2\sigma)-4\Delta V_{\rm free}
=8\pi^2\left(1+\frac{6t}{\pi}\right)
-4\Delta V_{\rm free}.
\]

Yamabe 体积估计还能精确加强。令
\[
L_s=\int(s-\bar s)^2d\mu.
\]
则
\[
\int s^2d\mu
=L_s+\frac{(\int s)^2}{V}
=L_s+32\pi^2\frac{(A+\sigma)^2}{A-\sigma^2}.
\]
由 \(16\hat V=Y[g]^2\le\int s^2\)，得到
\[
4\Delta V
\le
8\pi^2
\left[
\frac{(A+\sigma)^2}{A-\sigma^2}-A
\right]
+\frac{L_s}{4}.
\]
方括号恰好就是 Proposition 43.1 用 \(c=K-\sigma E\) 得到的 \(\Pi_g\) 下界。因此
\[
\boxed{\ 4\Delta V_{\rm free}\le\frac{L_s}{4}\ }
\]
是精确式，不需要 \(O(\sigma^2)\)。相应地，
\[
P_{\rm K\ddot ahler\ cell}
\ge
8\pi^2\left(1+\frac{6t}{\pi}\right)
-\frac{L_s}{4}
+\frac49\int(\sqrt6|W^+|-2)^2.
\]

此外
\[
2(2\pi+6t)^2
=8\pi^2(1+\sigma)^2
=8\pi^2(1+2\sigma)+O(\sigma^2),
\]
所以显式拓扑项的一阶系数确实相同。若要把“整个 \(P(t)\) 的一阶导数”也解释为完全相同，还需该族满足 \(L_s=o(t)\)；例如 \(L_s=O(t^2)\) 足够。实际 Kähler 公式中的 \(+L_s/4\) 与下界中的 \(-L_s/4\) 本身并不相等。

---

## 4. Remark 43.4

平滑性陈述正确：当 \(Y[g_\psi]<0\) 时，标量归一化的 Yamabe 解唯一，线性化可逆，因而随 \(g_\psi\) 平滑变化；调和投影也平滑。

需要修正的是导数公式。恒等式
\[
(a_\varepsilon^+)^2-(a_{-\varepsilon}^+)^2
=4\sum_i\varepsilon_i e_i
\]
给出
\[
F_\varepsilon-F_{-\varepsilon}
=-64\pi^2\sum_i\varepsilon_i e_i.
\]
又因为
\[
e(\psi)=(I+G(\psi))\sigma(\psi),\qquad \sigma(0)=0,
\]
所以
\[
e'(0)=(I+G(0))\sigma'(0).
\]
正确公式是
\[
\boxed{\;
F_\varepsilon'(0)-F_{-\varepsilon}'(0)
=-64\pi^2\,
\varepsilon\cdot(I+G(0))\sigma'(0).
\;}
\]
正文漏掉了 \(G(0)\sigma'(0)\)。只有在 \(G(0)=0\) 时才退化为所写公式；\(b^+>1\) 时 \(K\in\mathcal H^+\) 并不蕴含 \(E_i^+=0\)。

定性严格性仍然成立，因为 \(G(0)\) 半正定，故 \(I+G(0)\) 正定。若 \(\sigma'(0)\ne0\)，则 \(e'(0)\ne0\)，可选符号 \(\varepsilon\) 使 \(\varepsilon\cdot e'(0)\ne0\)。若公共值
\[
F_\varepsilon(0)=F_{-\varepsilon}(0)
\]
为零，两个非负光滑函数都在零点取局部最小值，导数差必须为零，矛盾。

定量式应写成带参数区间的形式。设
\[
d=32\pi^2|\varepsilon\cdot e'(0)|.
\]
若相关偶对称二阶余项在 \(|\psi|\le r\) 上由 \(\Lambda\psi^2/2\) 控制，则
\[
F(0)\ge
\sup_{0\le \rho\le r}
\left(d\rho-\frac{\Lambda}{2}\rho^2\right).
\]
只有当 \(d/\Lambda\le r\) 时，右端才等于
\[
\frac{d^2}{2\Lambda}.
\]
正文直接把局部 \(o(\psi^2)\) 式优化到 \(d/\Lambda\)，尚缺这一参数区间和余项控制。多 exceptional class 时自然出现的是
\[
\max_{\varepsilon}|\varepsilon\cdot e'(0)|
=\|e'(0)\|_1,
\]
而不是未说明范数的 \(|\sigma'(0)|\)。

---

## 5. 数值 Yamabe ledger

### 5.1 尾部消除恒等式

写 \(s=-24+e\)、\(u=1+v\)。Yamabe 方程等价于
\[
-6\Delta v+e+(e+48)v+72v^2+24v^3=0.
\]
直接展开可得点态恒等式
\[
\begin{aligned}
&(s^2-576u^4)
-\bigl(e^2+48ev-1152v^3-576v^4\bigr)\\
&\hspace{3cm}=-288\,\Delta v .
\end{aligned}
\]
因此在 bolt 通量为零且无穷远通量消失时，
\[
\int s^2-576\hat V
=
\int\left(e^2+48ev-1152v^3-576v^4\right).
\]
公式正确。若在有限外端点使用它，则还需加入 \(-288\int\Delta v\) 对应的通量项；脚本通过把计算端点放到 \(1.28\times10^6\)，并在较早位置截取局域化积分来压低该项。

### 5.2 尺度转换与 Y0

对 \(g_1=6g\)，
\[
d\mu_{g_1}=36\,d\mu_g,\qquad
\Delta V_{s=-4}=36\,\Delta V_{\rm profile}.
\]
Weyl 能量共形不变，因此
\[
D_W=\delta W+\frac23\Delta V.
\]
代入 Y0：
\[
8\pi^2-P(\hat g)
=4D_W-4\Delta V
=4\delta W-\frac43\Delta V.
\]
这些转换正确。

LeBrun 被积函数也正确：
\[
|W^+_{\hat g_1}|=\frac{|W^+_g|}{6u^2},
\qquad
d\mu_{\hat g_1}=36u^4d\mu_g,
\]
故
\[
(\sqrt6|W^+_{\hat g_1}|-2)^2d\mu_{\hat g_1}
=
(\sqrt6|W^+_g|-12u^2)^2d\mu_g.
\]

### 5.3 正文实际采用的数值

对 \(x_0=.03\)，尾部恒等式给出
\[
\Delta V=0.0530962911742,
\qquad
4\Delta V=0.212385164697.
\]
结合
\[
\delta W=0.0187835500983
\]
得到
\[
D_W
=0.0187835500983+\frac23(0.0530962911742)
=0.0541810775478,
\]
\[
4D_W=0.216724310191.
\]
而
\[
4\delta W=0.0751342003932,\qquad
\frac43\Delta V=0.0707950548990,
\]
两者之差为 \(0.00433914549\)，与
\[
1-P(\hat g)=0.00433913961
\]
相差 \(5.9\times10^{-9}\)，正是可见的 Gauss–Bonnet 数值误差。因此对 A02 数字的修正确实正确：旧的 \(0.07513\) 和 \(0.07080\) 是 \(4\delta W\) 与 \(\frac43\Delta V=48\Delta V_{\rm profile}\)，不是 \(4D_W\) 与 \(4\Delta V\)。

### 5.4 JSON 字段和正文表格不一致

`ledger_x003_X128_N80000.json` 的主字段仍保存直接尾部积分：
\[
\texttt{DeltaV}=0.0532416945762,\qquad
\texttt{D\_W}=0.0542780131442,
\]
所以
\[
\texttt{Y0\_residual}=1.94\times10^{-4}.
\]
正文表格实际用了
\[
\texttt{DeltaV\_identity}=0.0530962911742
\]
并重新计算了 \(D_W\)、\(F_{\rm LeB}\)、\(F_Y\)。例如正文的
\[
F_{\rm LeB}=0.20374895346
\]
对应 JSON 的 `F_LeB_identity`，而不是主字段 `F_LeB=0.20433056707`。数学表格是自洽的，但数据文件的字段命名没有反映正文“采用尾部恒等式数值”的选择。

### 5.5 另外两个数值说明

1. JSON 中
   \[
   \texttt{residual\_max}=0.242865,\qquad
   \texttt{newton\_iter}=59
   \]
   表明 Newton 循环走到了预设的 60 次。近 bolt 的离散算子系数达到约 \(10^{14}\)，所以这个绝对残差不直接衡量积分精度；Gauss–Bonnet、尾部恒等式以及两种共形能量公式对积分量提供了很强的相互印证。若要给出点态 PDE 精度，还需要加权残差或在 bolt 正则坐标中测量残差。

2. “\(W^+_{\hat g}\) 的 eigenvalue 从 \(-4\) 升到 \(-1.12\)”混用了尺度。脚本的
   \[
   [-4.00012,-1.12208]
   \]
   是 profile metric \(g\) 的 `Wplus_g` 数据。对 \(s=-4\) 的
   \(\hat g_1=6u^2g\)，CH 值应为 \(-2/3\)，而 \(-1.12208\) 对应约
   \[
   \frac{-1.12208}{6u^2}\simeq-0.187.
   \]
   eigenline 的位置不受共形缩放影响，因此“最小特征线在哪个 slot”仍正确；数值特征值应注明 profile 尺度。

此外，A02 已明确指出闭流形版 Theorem Y 需要 collar bookkeeping。这里求解的是非紧“cell + exact CH end”模型，其正的 \(F_{\rm LeB}\)、\(F_Y\) 是局部相对组合；它们不是闭流形上 monopole 不等式的直接数值求值。闭宿主上的 Yamabe 解还会受到宿主 Green 函数和其他 cells 的影响。

---

## 6. Theorem 43.5

永生流部分成立，而且可以直接写出完整推导。令
\[
m(t)=\min_M s(\cdot,t).
\]
由
\[
m(t)V^{1/2}\le Y[g(t)]\le Y(M)<0
\]
可取 \(c>0\) 使 \(m(t)\le-c\)。标量演化在最小点给出 Dini 意义下
\[
m'(t)\ge\frac12m(m-\bar s)
=\frac12(-m)(\bar s-m)
\ge\frac c2(\bar s-m).
\]
若 \(|s|\le C\)，则
\[
\int_0^\infty(\bar s-m)\,dt<\infty
\]
并且
\[
L_s
=\int(s-\bar s)^2
\le\int(s-m)^2
\le 2CV(\bar s-m).
\]
故
\[
\int_0^\infty L_s\,dt<\infty.
\]
另一方面，
\[
\bar s'=\frac{2P}{V}-\frac{L_s}{2V}
\]
正确；由于 \(\bar s\) 有界，积分后得到
\[
\int_0^\infty P\,dt<\infty.
\]
于是存在 \(t_j\to\infty\) 使 \(P(t_j)+L_s(t_j)\to0\)。又有
\[
S(t)=\int s^2\ge Y(M)^2>0,
\]
所以
\[
\mathscr D(g(t_j))
=\frac{4P+L_s}{P+S/4}\longrightarrow0,
\]
与 \(\alpha(M)>0\) 不相容。这一分支完整。

有限时间分支需要外部定理精确提供：

> 闭四维流形上的 Ricci flow 若在有限奇异时刻前具有一致标量曲率界，则原光滑流形上的流可光滑延拓越过该时刻。

归一化与非归一化之间的转换没有问题：有限时间内 \(\bar s\) 有界，缩放因子保持在两个正数之间，标量界也随之保持。

但当前材料没有给出 “family 351, Theorem 1.1” 的原文、页码或其“extend”的确切含义。若该定理只产生 orbifold 或弱 Ricci-flow continuation，它不能推出原光滑流形上 maximality 的矛盾。因而当前文件独立确定的是
\[
T=\infty,\quad Y(M)<0,\quad\alpha(M)>0
\quad\Longrightarrow\quad
\sup_{M\times[0,\infty)}|s|=\infty.
\]
Theorem 43.5 对所有 maximal flows 的完整表述，取决于上述外部定理是否确实具有同一光滑流形上的光滑延拓结论。
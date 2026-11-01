# TTCS Independent Branch Record

```json
{
  "step_id": 41,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step41_symplectic_closure_bolt_layer_and_new_inputs.md",
    "Knowledge/materials/openai-math-20261007/archive/sources/ricci-extension.txt",
    "Knowledge/materials/openai-math-20261007/archive/sources/ishida-0807.2169.txt",
    "Knowledge/materials/openai-math-20261007/continuation/20261007_openai_math_connections/connections.md"
  ]
}
```

## Task

Check the Ricci-flow proposition in Step 41 against the supplied primary sources and the note. Verify the normalized-to-unnormalized scaling/time conversion, Yamabe-minimum estimate, scalar evolution/minimum argument, mean-scalar identity including volume-form terms, and the inference that Y(M)<0 plus inf_g P(g)>0 forces scalar curvature to be unbounded on every maximal normalized Ricci flow, using family 351 for finite time and Ishida for the immortal branch. Also assess exactly how this adds to the Einstein-gap programme and whether any current inherited gap actually supplies inf P>0. Return mathematical corrections and scope.

## Output

# 数学核验备忘

## 1. 总结

Step 41 的 Ricci-flow 命题在下述解释下成立：

- \(M\) 为闭连通光滑四维流形；
- \(P(g)=\int_M|\operatorname{Ric}^{\circ}_g|^2\,d\mu_g\)；
- 采用体积归一化 Ricci 流
  \[
  \partial_tg=-2\operatorname{Ric}+\frac12\bar s\,g,
  \qquad
  \bar s=\frac1V\int_Ms\,d\mu,
  \]
  其中 \(V\) 沿流不变；
- 有 \(Y(M)<0\) 与
  \[
  p_0:=\inf_{g\in\operatorname{Met}(M)}P(g)>0;
  \]
- 有限时间部分引入 family 351, Theorem 1.1。

则每条极大体积归一化 Ricci 流都满足
\[
\sup_{M\times[0,T_{\max})}|s|=\infty.
\]

归一化与非归一化流之间的换元、Yamabe 最小值估计、标量曲率最小值微分不等式、平均标量曲率公式均正确。需要修改的是 Step 41 最后一句“A bound only for \(P+D_2\) does not suffice”：若项目中的
\[
D_2=\int_M(s-\bar s)^2\,d\mu,
\]
那么正的全度量 \(P+D_2\) 下界同样足以推出上述流结论，尽管它并不推出 \(\inf P>0\)。

---

## 2. 有限时间：归一化到非归一化的换元

设归一化流定义在 \(0\le t<T<\infty\)，并暂时假设
\[
|s_{g(t)}|\le C.
\]
定义
\[
a(t)=\exp\!\left(-\frac12\int_0^t\bar s(u)\,du\right),
\qquad
\tau(t)=\int_0^t a(u)\,du,
\qquad
\widetilde g(\tau(t))=a(t)g(t).
\]

常数倍缩放下，作为 \((0,2)\)-张量有
\[
\operatorname{Ric}_{ag}=\operatorname{Ric}_g,
\qquad
s_{ag}=a^{-1}s_g.
\]
又因为
\[
\frac{a'}a=-\frac12\bar s,
\]
所以
\[
\frac d{dt}(ag)
=a'g+a\left(-2\operatorname{Ric}+\frac12\bar s\,g\right)
=-2a\,\operatorname{Ric}.
\]
由 \(d\tau/dt=a\) 得
\[
\partial_\tau\widetilde g=-2\operatorname{Ric}_{\widetilde g}.
\]

由于 \(|\bar s|\le C\)，在有限区间上
\[
e^{-CT/2}\le a(t)\le e^{CT/2}.
\]
因此
\[
0<\tau(T)=\int_0^Ta(t)\,dt<\infty,
\qquad
|s_{\widetilde g}|=a^{-1}|s_g|\le e^{CT/2}C.
\]
family 351, Theorem 1.1 恰好适用于这一闭四维流，因而 \(\widetilde g\) 可越过 \(\tau(T)\) 光滑延拓。

反向归一化也没有缺口。对延拓后的非归一化流置
\[
a(\tau)=\left(\frac{\operatorname{Vol}_{\widetilde g(\tau)}M}{V}\right)^{1/2},
\qquad
\frac{dt}{d\tau}=a^{-1},
\qquad
g(t(\tau))=a(\tau)^{-1}\widetilde g(\tau).
\]
非归一化流满足
\[
\frac d{d\tau}\operatorname{Vol}_{\widetilde g}
=-\bar s_{\widetilde g}\operatorname{Vol}_{\widetilde g},
\]
所以
\[
\frac{a_\tau}{a}=-\frac12\bar s_{\widetilde g},
\qquad
a_\tau=-\frac12\bar s_g.
\]
于是
\[
\partial_tg=-2\operatorname{Ric}_g+\frac12\bar s_g\,g.
\]
这确实把原归一化流延拓到 \(T\) 之后，与极大性矛盾。

因此在有限极大时间情形，标量曲率不可能全程有界。这里 \(Y(M)<0\) 与 \(p_0>0\) 都没有被使用；有限时间部分完全来自 family 351。

---

## 3. Yamabe 不变量给出的标量最小值估计

令
\[
m(t)=\min_Ms_{g(t)}.
\]
四维 Yamabe 商为
\[
Q_g(u)=
\frac{\int_M(6|\nabla u|^2+su^2)\,d\mu}
{\left(\int_Mu^4\,d\mu\right)^{1/2}}.
\]
记当前共形类的 Yamabe 常数为 \(Y_{[g]}\)。因为
\[
Y_{[g]}\le Y(M)<0,
\]
当前度量不可能满足 \(m\ge0\)，否则 \(Q_g(u)\ge0\) 对所有 \(u\) 成立。

当 \(m<0\) 时，
\[
Q_g(u)\ge
m\,\frac{\int u^2\,d\mu}{(\int u^4\,d\mu)^{1/2}}.
\]
Hölder 不等式给出
\[
\frac{\int u^2\,d\mu}{(\int u^4\,d\mu)^{1/2}}\le V^{1/2}.
\]
由于 \(m<0\)，乘法反向产生
\[
Q_g(u)\ge mV^{1/2}.
\]
取下确界并使用 \(Y_{[g]}\le Y(M)\)，得到
\[
mV^{1/2}\le Y_{[g]}\le Y(M),
\]
故
\[
\boxed{m(t)\le Y(M)V^{-1/2}=-c<0.}
\]
这正是 Ishida Proposition 5 在四维、固定体积情形的估计。

---

## 4. 标量演化与最小值论证

四维归一化流的标量曲率演化为
\[
\partial_ts
=\Delta s+2|\operatorname{Ric}|^2-\frac12\bar s\,s.
\]
写
\[
\operatorname{Ric}
=\operatorname{Ric}^{\circ}+\frac s4g,
\qquad
|\operatorname{Ric}|^2
=|\operatorname{Ric}^{\circ}|^2+\frac{s^2}{4},
\]
可得
\[
\partial_ts
=\Delta s+2|\operatorname{Ric}^{\circ}|^2
+\frac12s(s-\bar s).
\]

在标量最小点，按 Hamilton 的 barrier 解释或几乎处处微分，
\[
m'\ge\frac12m(m-\bar s).
\]
又因 \(m\le-c\) 且 \(\bar s-m\ge0\)，
\[
m(m-\bar s)=(-m)(\bar s-m)\ge c(\bar s-m).
\]
因此
\[
\boxed{m'\ge\frac c2(\bar s-m)\ge0.}
\]
所以 \(m\) 单调不减且仍满足 \(m\le-c\)，从而
\[
\int_0^\infty(\bar s-m)\,dt<\infty.
\]

若假设 immortal 流上 \(|s|\le C\)，则
\[
0\le s-m\le2C.
\]
利用
\[
\fint(s-m)^2
=\fint(s-\bar s)^2+(\bar s-m)^2
\]
得到
\[
\operatorname{Var}(s)
:=\fint(s-\bar s)^2
\le\fint(s-m)^2
\le2C(\bar s-m).
\]
故
\[
\boxed{\int_0^\infty\operatorname{Var}(s)\,dt<\infty.}
\]

这一步必须保留“标量曲率一致有界”这一假设；仅由 \(Y(M)<0\) 得不到方差的时间可积性。

---

## 5. 平均标量曲率公式及体积形式项

归一化流下
\[
\partial_td\mu
=\frac12\operatorname{tr}_g(\partial_tg)\,d\mu
=(\bar s-s)\,d\mu.
\]
因此 \(V' =0\)。进一步，
\[
\begin{aligned}
\frac d{dt}\int_Ms\,d\mu
&=\int_M
\left[
\Delta s+2|\operatorname{Ric}|^2-\frac12\bar s\,s
+s(\bar s-s)
\right]d\mu\\
&=\int_M
\left[
2|\operatorname{Ric}|^2-s^2+\frac12\bar s\,s
\right]d\mu.
\end{aligned}
\]
代入
\[
2|\operatorname{Ric}|^2
=2|\operatorname{Ric}^{\circ}|^2+\frac12s^2
\]
以及
\[
\int_M\bar s\,s\,d\mu=V\bar s^2,
\]
得到
\[
\frac d{dt}\int_Ms\,d\mu
=2P-\frac12\left(S-V\bar s^2\right),
\]
其中
\[
P=\int_M|\operatorname{Ric}^{\circ}|^2\,d\mu,
\qquad
S=\int_Ms^2\,d\mu.
\]
除以固定体积 \(V\)，即
\[
\boxed{
\bar s'
=\frac{2P}{V}
-\frac12\fint_M(s-\bar s)^2\,d\mu.
}
\]

所以对任意 \(T>0\)，
\[
\frac2V\int_0^TP(g(t))\,dt
=
\bar s(T)-\bar s(0)
+\frac12\int_0^T\operatorname{Var}(s)\,dt.
\]
若 \(|s|\le C\)，则 \(\bar s\) 有界；上一节又给出方差时间可积，于是
\[
\boxed{\int_0^\infty P(g(t))\,dt<\infty.}
\]

这与 Ishida Proposition 3 的结论一致；Ishida 使用 Proposition 5、标量波动的 \(L^1\) 控制以及标量演化积分来得到同一结果。上述平均标量公式是在本归一化下更直接的推导。

---

## 6. \(p_0>0\) 如何完成 immortal 情形

若
\[
p_0=\inf_gP(g)>0,
\]
则流上的每个时间切片都是 \(M\) 上的光滑度量，故
\[
P(g(t))\ge p_0.
\]
若流存在于 \([0,\infty)\)，则
\[
\int_0^\infty P(g(t))\,dt
\ge\int_0^\infty p_0\,dt
=\infty,
\]
与上一节矛盾。

因此 immortal 流不可能具有一致有界的标量曲率。结合有限时间换元，得到
\[
\sup_{M\times[0,T_{\max})}|s|=\infty.
\]

---

## 7. 关于 \(P+D_2\) 的必要修正

若项目记号是
\[
D_2(g)=S-\frac{(\int s)^2}{V}
=\int_M(s-\bar s)^2\,d\mu,
\]
那么 Step 41 中“只有 \(P+D_2\) 的下界不够”这一句不成立。

在假设 \(|s|\le C\) 的 immortal 流上，上面已经证明
\[
\int_0^\infty P\,dt<\infty,
\qquad
\int_0^\infty D_2\,dt
=V\int_0^\infty\operatorname{Var}(s)\,dt<\infty.
\]
所以若存在
\[
\inf_g\bigl(P(g)+D_2(g)\bigr)>0,
\]
同样立即产生矛盾。更一般地，任意固定正系数的组合
\[
aP+bD_2,\qquad a,b>0,
\]
只要具有正的全度量下界，就足以完成 immortal 部分。

对 connections.md 中的归一化泛函
\[
\mathcal E
=4-\frac{(\int s)^2}{VR}
=\frac{4P+D_2}{R},
\qquad
R=P+\frac S4,
\]
若已有全度量下界 \(\mathcal E\ge e_0>0\)，则 \(Y(M)<0\) 还给出
\[
S\ge |Y(M)|^2
\]
——这是 Ishida 公式 (10) 在四维的直接结果。因此
\[
4P+D_2
=\mathcal ER
\ge e_0R
\ge\frac{e_0}{4}S
\ge\frac{e_0}{4}|Y(M)|^2>0.
\]
故一个真正覆盖所有度量的 \(\mathcal E\)-间隙也足以推出流结论，即使它不推出 \(\inf P>0\)。

若 Step 41 中的 \(D_2\) 指另一个量，例如 \(\int(s+4)^2\)，则上述时间可积论证不适用；文稿应明确写出定义。

---

## 8. 现有材料中哪些结果确实给出 \(\inf P>0\)

### 8.1 仅有 \(Y(M)<0\) 不够

\(Y(M)<0\) 本身不推出 \(p_0>0\)。若 \(M\) 携带满足
\[
\operatorname{Ric}=\lambda g,\qquad \lambda<0
\]
的度量，则 \(Y(M)<0\)，但该度量有 \(P=0\)。

### 8.2 全度量 \(\mathcal J\)-间隙可以给出 \(p_0\)

若已证明对固定 \(M\) 的所有度量都有
\[
\mathcal J(g)=\frac{4P}{P+S/4}\ge c_0>0,
\]
则
\[
(4-c_0)P\ge\frac{c_0}{4}S.
\]
由 \(S\ge|Y(M)|^2\)，得到
\[
\boxed{
p_0\ge
\frac{c_0|Y(M)|^2}{4(4-c_0)}>0.
}
\]
所以真正的全度量 \(\mathcal J\)-间隙确实提供命题所需输入。

Step 41 的局部 cell 构造
\[
J(g_*)<1
\]
属于上界构造；它不产生全度量的 \(P\) 下界。connections.md 中仍待闭合的 O10/O11 连接也没有在当前材料内给出目标族上的无附加假设全度量 \(\mathcal J\)-间隙。因此，对该目标族而言，Step 41 的 \(p_0>0\) 仍是额外假设。

### 8.3 Ishida–LeBrun 曲率不等式在一部分拓扑区间确实给出 \(p_0>0\)

供应的 Ishida 原文已经包含一个可计算的例子。令
\[
I_+(g)=\int_M\left(2|W^+|^2+\frac{s^2}{24}\right)d\mu.
\]
Corollary 15 与 Theorem 20 给出
\[
\frac{I_+(g)}{4\pi^2}\ge\frac23\beta^2(M).
\]
另一方面，Chern–Gauss–Bonnet 与 signature 公式给出
\[
\frac{I_+(g)}{4\pi^2}
=T_+(M)+\frac{P(g)}{8\pi^2},
\qquad
T_+=2\chi+3\tau.
\]
因此
\[
\boxed{
P(g)\ge
8\pi^2\left(\frac23\beta^2(M)-T_+(M)\right).
}
\]

在 Ishida 的
\[
M=X\#N,\qquad b^+(N)=0
\]
情形，置
\[
C=c_1^2(X),\qquad
B=4b_1(N)+b^-(N).
\]
其 monopole-class 输入给出 \(\beta^2(M)\ge C\)，而
\[
T_+(M)=C-B.
\]
于是
\[
\boxed{
P(g)\ge8\pi^2\left(B-\frac C3\right).
}
\]
当
\[
4b_1(N)+b^-(N)>\frac13c_1^2(X)
\]
时，这就是明确的正 \(P\)-间隙。Theorem 19 同时给出 \(Y(M)<0\)，所以 Step 41 命题可直接应用。

对纯 blow-up
\[
M=X\#k\,\overline{\mathbb{CP}}^{\,2},
\]
有
\[
P(g)\ge8\pi^2\left(k-\frac13c_1^2(X)\right),
\]
故 \(k>c_1^2(X)/3\) 时得到 \(p_0>0\)。

在等号
\[
k=\frac13c_1^2(X)
\]
处，Ishida 对等号结构的分析可排除某些单个度量达到等号，但“每个度量都有 \(P(g)>0\)”并不自动产生
\[
\inf_gP(g)>0.
\]
因此 Step 41 的命题不能仅凭这种逐个度量的严格性应用在等号位置。

---

## 9. 对 Einstein-gap 研究的实际增量

这项 Ricci-flow 推论的作用可精确分成三部分：

1. **静态到动力学的接口。**  
   任意真正的全度量 \(P\)-间隙都排除所有 immortal、标量曲率一致有界的归一化 Ricci 流。

2. **有限时间补全。**  
   family 351 排除有限极大时间且标量曲率一致有界的情形；这一部分对所有闭四维流成立，不依赖 Einstein-gap 输入。

3. **与 Ishida 的关系。**  
   immortal 部分实质上是 Ishida Propositions 3 和 5 的直接组合。新的组织方式是把拓扑条件替换为抽象静态输入 \(p_0>0\)，再与 family 351 合并成“每条极大归一化流的标量曲率都无界”。

它没有建立新的 \(P\)-间隙，也没有推出极大时间一定有限、标量曲率的发散速率、发散符号、曲率集中位置或全曲率张量的几何模型。对于 Ishida–LeBrun 已经给出正 \(P\)-间隙的严格拓扑区间，immortal 结论与 Ishida 的 quasi-non-singular 排除结果高度重合；新增部分主要是与 family 351 合并后统一覆盖有限和无限极大时间。

最重要的文本修订是：将“只有 \(P+D_2\) 的下界不够”改为区分两件事——它一般不推出 \(\inf P>0\)，但若 \(D_2\) 是标量方差，则正的全度量 \(P+D_2\) 下界本身已经足以推出同一 Ricci-flow 结论。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 27,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step27_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step27_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the shifted-curvature continuation mechanism for the normalized fixed-cutoff flow ∂_t g=-2a(Ric+g), a=χ². Read the Step 27 note, Wang's actual Section 4 proof, Yang's DeTurck construction, and the full-velocity tensor derivation. Check the convention G=(g∧g)/(2(n−1)), Ric(G)=g, ∇G=0, ∂_tG algebraic; derive the schematic evolutions of T=Rm+G and U=aT with all highest cutoff derivatives visible. Then assess whether Wang Lemmas 4.10, 4.11, 4.13, 4.14 transfer without an uncancelled highest-order term. Focus especially on χ∇^{m+2}χ*U, the integration by parts, the cutoff derivative equation driven by Ric(U), and any error in the proposed dependency triangle. Give explicit repairs or a precise obstruction; do not merely call terms lower order.

## Integrated Scientific Memo

# 核验结论

移位曲率机制可以修复 Step 26，但 Step 27 的依赖三角形写错了一阶。采用一致曲率约定后，Wang §4 的 Lemma 4.10、4.11、Propositions 4.13–4.14 可以转移到

\[
\partial_tg=-2a(\Ric+g),\qquad a=\chi^2,
\]

且没有无法消除的 \(\nabla^{m+2}\chi\) 项。唯一最高阶项仍是

\[
\chi\nabla^{m+2}\chi*U,
\]

它必须保留至能量积分中，再分部积分一次。真正的当前阶闭环是

\[
\nabla^mU\longleftrightarrow \nabla^{m+1}\chi,
\]

而 \(\nabla^{m-1}T\) 只依赖 \(\nabla^m\chi\)，已经属于前一阶数据。

---

## 1. 移位张量及约定

固定

\[
(g\owedge g)_{ijkl}=2(g_{ik}g_{jl}-g_{il}g_{jk}),\qquad
G=\frac{g\owedge g}{2(n-1)}.
\]

于是

\[
G_{ijkl}=\frac1{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}),
\]

按第一、第三指标缩并，

\[
g^{ik}G_{ijkl}=g_{jl}.
\]

以下须固定曲率约定使

\[
g^{ik}R_{ijkl}=\Ric_{jl}.
\]

定义

\[
T=\Rm+G,\qquad U=aT.
\]

则有精确恒等式

\[
\Ric(T)=\Ric+g=:E,\qquad aE=\Ric(U).
\]

因为 \(\nabla g=0\)，

\[
\nabla G=0,\qquad \nabla^rT=\nabla^r\Rm\quad(r\ge1).
\]

若 \(h=\partial_tg=-2aE\)，则

\[
\partial_tG_{ijkl}
=\frac1{n-1}
(h_{ik}g_{jl}+g_{ik}h_{jl}-h_{il}g_{jk}-g_{il}h_{jk}),
\]

故 \(\partial_tG\) 仅代数依赖 \(a,E,g\)，不含 \(a\) 或 \(E\) 的空间导数。

此外

\[
aT=a\Rm+aG.
\]

若 \(0\le \chi\le1\)，则 \(|aG|\le C_n\)；对任意固定光滑 \(\chi\)，常数改为 \(C_n\|\chi\|_\infty^2\)。所以 \(\|a\Rm\|_\infty\) 与 \(\|U\|_\infty\) 的有界性等价。

一个重要的精确修正是：移位后的代数反应项没有纯常数项。若 \(T=0\)，则 \(E=0\)，从而流静止且 \(\partial_tT=0\)。因此可取

\[
|\mathcal Q_G(T)|\le C_n(|T|+|T|^2),
\]

而不是必须写成 \(C_n(1+|T|+|T|^2)\)。

---

## 2. \(T\) 的演化：不存在纯 \(\nabla^2a*G\) 源

全速度曲率变分给出

\[
\partial_t\Rm
=a\Delta\Rm+a\mathcal A(\Rm)
+da*\nabla E+\nabla^2a*E.
\]

利用 \(E=\Ric(T)\)、\(\nabla G=0\) 和 \(\partial_tG\) 的代数性，可整理为

\[
\boxed{
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T).
}
\tag{2.1}
\]

这里是通用缩并意义下的等式。右端每一项都含 \(T\) 或其导数；特别地，不存在独立的

\[
\nabla^2a*G
\]

或纯 cutoff 源。将速度拆成 \(-2a\Ric-2ag\) 会分别产生这类表观项，但它们在完整变分与 \(\partial_tG\) 中相消。

交换 \(m\) 次协变导数后，

\[
\begin{aligned}
\partial_t\nabla^mT
={}&a\Delta\nabla^mT\\
&+\sum_{\substack{i+j+k=m+2\\k\le m+1}}
 \nabla^i\chi*\nabla^j\chi*\nabla^kT\\
&+\sum_{i+j+k=m}
 \nabla^ia*\nabla^jT*\nabla^kT\\
&+\sum_{i+k=m}\nabla^ia*G*\nabla^kT.
\end{aligned}
\tag{2.2}
\]

真正最高的 cutoff 项是

\[
\chi\nabla^{m+2}\chi*T.
\]

最后一行只含至多 \(m\) 阶 cutoff 导数；它不能制造新的最高阶障碍。

---

## 3. \(U=aT\) 的演化

因 \(a\) 是固定标量，\(\partial_ta=0\)。由

\[
\Delta(aT)=a\Delta T+2\,da*\nabla T+(\Delta a)T
\]

并使用 \(a=\chi^2\)，可不除以 \(a\) 地写成

\[
\boxed{
(\partial_t-a\Delta)U
=da*\nabla U+\nabla^2a*U
+d\chi*d\chi*U+U*U+aG*U.
}
\tag{3.1}
\]

例如

\[
|da|^2T=4\chi^2|d\chi|^2T=4|d\chi|^2U,
\]

所以该表达在 \(\chi=0\) 处也无奇性。

交换 \(m\) 次导数后得到 Wang Lemma 4.5 型结构：

\[
\begin{aligned}
\partial_t\nabla^mU
={}&a\Delta\nabla^mU\\
&+\sum_{\substack{i+j+k=m+2\\k\le m+1}}
 \nabla^i\chi*\nabla^j\chi*\nabla^kU\\
&+\sum_{\substack{i+j+k=m\\k\le m-1}}
 \nabla^ia*\nabla^jU*\nabla^kT\\
&+U*\nabla^mU+\mathcal G_m.
\end{aligned}
\tag{3.2}
\]

其中 \(\mathcal G_m\) 的每个单项式：

- 含一个 \(G\) 和一个 \(\nabla^sU\)，\(s\le m\)；
- cutoff 导数阶至多 \(m\)；
- 若 \(s=m\)，其系数为有界的 \(aG\)。

最高 cutoff 项来自 \(\nabla^{m+2}a*U\)，即

\[
\boxed{
\chi\nabla^{m+2}\chi*U,\quad
\nabla\chi*\nabla^{m+1}\chi*U,\quad
\chi\nabla^{m+1}\chi*\nabla U.
}
\tag{3.3}
\]

不能在点态估计阶段把第一项称为低阶项。

---

## 4. 最高项的分部积分

令

\[
W=\nabla^mU,\qquad
D_m=\int a|\nabla W|^2|W|^{p-2}.
\]

最高项对应

\[
I_m=\int |W|^{p-2}
\left\langle W,\chi\nabla^{m+2}\chi*U\right\rangle.
\]

从 \(\nabla^{m+2}\chi\) 转移一次导数：

\[
\begin{aligned}
I_m={}&
-\int \nabla(|W|^{p-2}W)
 *\chi\nabla^{m+1}\chi*U\\
&-\int |W|^{p-2}W
 *\nabla\chi*\nabla^{m+1}\chi*U\\
&-\int |W|^{p-2}W
 *\chi\nabla^{m+1}\chi*\nabla U.
\end{aligned}
\tag{4.1}
\]

第一项满足

\[
|\text{第一项}|
\le \varepsilon D_m+
C_{\varepsilon,p}
\int |\nabla^{m+1}\chi|^2|U|^2|W|^{p-2}.
\tag{4.2}
\]

吸收之所以成立，正是因为原项保留了因子 \(\chi\)，而扩散权为 \(a=\chi^2\)。其余项只含 \(\nabla^{m+1}\chi\)，不再含 \(\nabla^{m+2}\chi\)。

与 Wang 原证明相同，闭合通常需要错列指数：对所有足够大的 \(p\) 建立估计，再用 Hölder，例如

\[
\int |\nabla^{m+1}\chi|^2|W|^{p-2}
\le
\|\nabla^{m+1}\chi\|_{L^p}^2
\|W\|_{L^p}^{p-2},
\]

含额外 \(\nabla U\) 的项则使用更大的辅助指数。这是需要在正式证明中保留的分析细节。

---

## 5. cutoff 导数方程

关键恒等式是

\[
aE=\Ric(U).
\]

由于 contraction 与协变导数交换，

\[
\nabla^q\Ric(U)=\Ric(\nabla^qU)
\]

完全精确，不存在所谓“随时间变化的 contraction 所产生的低阶空间项”。

又有

\[
\partial_t\Gamma=g^{-1}*\nabla h
=g^{-1}*\nabla\Ric(U).
\]

对 \(r\ge2\)，

\[
\partial_t\nabla^r\chi
=
\sum_{q=0}^{r-2}
\nabla^q(\partial_t\Gamma)
*\nabla^{r-1-q}\chi.
\]

计入范数随度量的变化后，

\[
\boxed{
\partial_t|\nabla^r\chi|
\le
C_r|U|\,|\nabla^r\chi|
+C_r\sum_{s=1}^{r-1}
|\nabla^sU|\,|\nabla^{r-s}\chi|.
}
\tag{5.1}
\]

取 \(r=m+1\)，当前阶唯一最高项是

\[
|\nabla^mU|\,|\nabla\chi|.
\]

因此适当 Hölder 后，

\[
\|\nabla^{m+1}\chi(t)\|_{L^p}
\le C+
C\int_0^t
\left(1+\|\nabla^mU(s)\|_{L^{p_1}}\right)\,ds.
\tag{5.2}
\]

这正产生 Wang Lemma 4.8 所处理的 Volterra 型闭环。

---

## 6. Wang 四个结果的转移

### Lemma 4.10：\(T\) 的无权 \(L^p\) 界

以 \(|T|^{p-2}T\) 测试 (2.1)，将 \(\nabla^2a*T\) 分部积分一次，并用

\[
\frac{|da|^2}{a}=4|d\chi|^2
\]

得到

\[
\frac d{dt}\int|T|^p
+c_p\int a|\nabla T|^2|T|^{p-2}
\le
C_p(1+\|U\|_\infty)\int|T|^p.
\tag{6.1}
\]

因为 \(aT*T=U*T\)，而 \(aG*T\)、范数变化和体积变化都具有有界系数，所以 Lemma 4.10 直接转移。

### Lemma 4.11：\(\nabla U\) 与 \(\nabla^2\chi\) 的耦合基例

在 \(m=1\) 时，最高项为

\[
\chi\nabla^3\chi*U.
\]

按 (4.1) 分部积分后只剩 \(\nabla^2\chi,\nabla U\) 及可由扩散吸收的 \(\nabla^2U\)。另一方面，(5.1) 给出

\[
\partial_t|\nabla^2\chi|
\le C|U||\nabla^2\chi|
+C|\nabla U||\nabla\chi|.
\]

故

\[
\|\nabla^2\chi(t)\|_p
\le C+C\int_0^t\|\nabla U(s)\|_p\,ds.
\]

代回 \(\nabla U\) 能量不等式即得到

\[
y'(t)\le C\left(1+y(t)+\int_0^ty(s)\,ds\right).
\]

\(G\)-项只增加 \(Cy\)、常数或已由 (6.1) 控制的 \(T\)-范数，不产生新的最高阶项。

### Proposition 4.13：\(T\) 的无权高阶导数

在 \(\nabla^rT\) 方程中，

\[
\chi\nabla^{r+2}\chi*T
\]

分部积分一次后，只需 \(\nabla^{r+1}\chi\) 和较低阶 \(T\)-导数。故准确依赖关系是

\[
\nabla^rT\quad\text{需要 cutoff 导数至 }r+1\text{ 阶}.
\tag{6.2}
\]

\(G\)-项仅含至多 \(r\) 阶 cutoff 导数；含 \(\nabla^rT\) 的项系数为有界 \(aG\)。

### Proposition 4.14：\(U\) 的高阶导数

在第 \(m\) 阶，\(\nabla^mU\) 的能量估计依赖

\[
\nabla^{m+1}\chi,\qquad \nabla^{m-1}T,
\]

以及更低阶 \(U\)-导数。由 (5.2)，\(\nabla^{m+1}\chi\) 通过 \(\nabla^mU\) 的时间积分控制；选取 Wang 所需的错列指数后，仍归结为有限个

\[
y'(t)\le C\left(1+y(t)+\int_0^ty(s)\,ds\right)
\]

型不等式。没有残留的 \(\nabla^{m+2}\chi\) 项。

---

## 7. Step 27 依赖三角形的精确修正

Step 27 将无权曲率分支多算了一阶。设

\[
A_m=\|\nabla^mU\|,\qquad
B_{m-1}=\|\nabla^{m-1}T\|,\qquad
C_r=\|\nabla^r\chi\|.
\]

准确依赖是

\[
A_m\ \text{依赖}\ B_{m-1},\,C_{m+1},
\]

\[
B_{m-1}\ \text{依赖}\ C_m,
\]

\[
C_{m+1}\ \text{依赖}\ \int_0^t A_m.
\]

原因是 Proposition 4.13 在阶数 \(r\) 只要求 \(C_{r+1}\)；代入 \(r=m-1\) 得 \(C_m\)，不是 \(C_{m+1}\)。

因此当前阶唯一闭环为

\[
\boxed{A_m\longleftrightarrow C_{m+1}},
\]

而 \(B_{m-1}\) 已由前一阶归纳获得。这比 Step 27 所述“三角循环”更简单。

---

## 8. DeTurck 与延拓

Yang 的 transported-coefficient 系统应改为

\[
\partial_t\widehat g
=-2\widehat a(\Ric(\widehat g)+\widehat g)
+\mathcal L_V\widehat g,
\qquad
\widehat a=(\chi\circ\varphi_t^{-1})^2.
\]

新增的 \(-2\widehat a\,\widehat g\) 对 \(\widehat g\) 是零阶项，不改变 Yang 正则化线性系统的主部。又有

\[
\varphi_t^*\widehat a=a,
\]

且 pullback 导数中的 Lie 项与 gauge 项相消，得到固定 cutoff 方程

\[
\partial_tg=-2a(\Ric(g)+g).
\]

若 \(\|U\|_\infty\) 有界，则

\[
|\partial_tg|=2|\Ric(U)|\le C_n|U|,
\]

从而有限时间内度量一致双 Lipschitz，\(|\nabla\chi|\) 与闭流形 Sobolev 常数也一致受控。若所有 \(\nabla^mU\) 有界，则所有

\[
\nabla^m(aE)=\nabla^m\Ric(U)
\]

有界，进而控制速度、连接变化及终端度量的全部空间 jet，可应用 Wang Proposition 4.3/Hamilton 的终端重构论证延拓。

---

## 最终判定

1. 移位 \(T=\Rm+G\) 是正确修复；它将 \(E\) 精确表示为 \(\Ric(T)\)。
2. 移位不会消除最高 cutoff 导数；必须显式保留
   \[
   \chi\nabla^{m+2}\chi*U.
   \]
3. 分部积分一次后，该项只留下 \(\nabla^{m+1}\chi\) 和扩散可吸收项。
4. cutoff 导数方程精确由 \(\Ric(U)\) 驱动，故当前阶 Volterra 闭环成立。
5. \(G\)-项不产生纯最高阶 cutoff 源；每项都含 \(T\) 或 \(U\)，且导数阶严格不坏于 Wang 原结构。
6. Wang Lemmas 4.10、4.11、Propositions 4.13、4.14 在固定曲率符号和完整错列指数 bookkeeping 下可转移，没有未消除的最高阶障碍。
7. Step 27 的实质错误是依赖关系多算一阶：
   \[
   \nabla^{m-1}T\text{ 依赖 }\nabla^m\chi,
   \quad\text{不是 }\nabla^{m+1}\chi.
   \]

因此，现有材料已经排除了最高阶结构性障碍；尚需写出的不是新机制，而是 Wang 各项的完整 Hölder 指数选择、Volterra 不等式和终端重构细节。
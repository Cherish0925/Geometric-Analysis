# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 64,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step64_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step64_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Cross-note sign-convention consistency audit for a Riemannian flow proof. The shifted curvature used in an Ishida-LeBrun cutoff-flow proof was redefined in the newest note (Step 63) as T = Rm - G with G = (g KN g)/(2(n-1)) under the standard Kulkarni-Nomizu product, giving Ric(G) = -g, Ric(T) = E, nabla T = nabla Rm. All earlier notes (Steps 34,43,54,55,58,59,60) wrote T = Rm + G with the SAME auxiliary properties Ric(T)=E, nabla T = nabla Rm, |G|^2 = n/(2(n-1)). The sweep note claims: (a) the two conventions define the SAME tensor T (legacy G_old = -G); (b) |G|^2 and F_T=(1+|T|^2)^{1/2} asymptotic F=(1+|Rm|^2)^{1/2} are sign-invariant; (c) all energies H_2, K_p, Y, Gamma and dissipations built from F_T or |Rm| are numerically unchanged; (d) the U=aT evolution conversion uses only the sign-free cancellation d_t U = a d_t T, so the continuation equations are unaffected. Read the sweep note plus the Step 63 anchor and the legacy Step 54/58 notes. Verify or refute claims (a)-(d) rigorously at the tensor level. Specifically: is it TRUE that requiring Ric(T)=E and nabla T = nabla Rm forces the same T regardless of the G sign? Are there any displayed equations in the legacy notes whose SIGN genuinely flips (not just relabels) under one consistent convention? Identify any compensating-error risk the sweep missed.

## Integrated Scientific Memo

## 核验结论

Step 64 的核心结论只能作如下限定性认可：

\[
G_{\rm old}:=-G,\qquad
T_{\rm old}=\operatorname{Rm}+G_{\rm old}
          =\operatorname{Rm}-G=:T
\]

这一**同步重命名**确实使物理张量 \(T\) 相同，因此由 \(T\)、\(F_T\) 或 \(\nabla\operatorname{Rm}\) 构成的估计栈不受影响。但 Step 64 更强的说法——“上述两个辅助性质强迫同一个 \(T\)”“旧显示均可原样保留”“无跨笔记矛盾”——不成立。另有若干非符号性的系数与范数归一化错误。

---

### 1. 固定 Step 63 约定后的基本代数

采用

\[
(\varphi\owedge\psi)_{ijkl}
=\varphi_{ik}\psi_{jl}+\varphi_{jl}\psi_{ik}
-\varphi_{il}\psi_{jk}-\varphi_{jk}\psi_{il},
\]

\[
G=\frac{g\owedge g}{2(n-1)}
  =\frac{g_{ik}g_{jl}-g_{il}g_{jk}}{n-1},
\qquad
\operatorname{Ric}(A)_{jk}=g^{il}A_{ijkl},
\]

则

\[
\operatorname{Ric}(G)_{jk}
=\frac{g_{jk}-ng_{jk}}{n-1}=-g_{jk}.
\]

故规范选择为

\[
\boxed{T=\operatorname{Rm}-G},\qquad
\operatorname{Ric}(T)=\operatorname{Ric}+g=E,\qquad
\nabla T=\nabla\operatorname{Rm}.
\]

若旧符号定义为 \(G_{\rm old}=-G\)，则

\[
\operatorname{Ric}(G_{\rm old})=g,\qquad
T=\operatorname{Rm}+G_{\rm old}.
\]

这是两套记号描述同一张量的正确方式。

然而，旧笔记若被字面读取为同时采用标准 KN 乘积、

\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\operatorname{Rm}+G,
\]

则

\[
\operatorname{Ric}(T)=\operatorname{Ric}-g\ne E.
\]

因此旧显示不是“原样 sign-safe”；必须把旧 \(G\) 明确重命名为 \(G_{\rm old}=-G\)，或者把每个显式 \(G\) 的符号改写。

---

### 2. 两个辅助性质并不强迫唯一的 \(T\)

问题所问的答案是：

\[
\boxed{\operatorname{Ric}(T)=E,\quad \nabla T=\nabla\operatorname{Rm}
\text{ 本身不强迫同一个 }T.}
\]

若

\[
T_{\rm old}=\operatorname{Rm}+A,
\]

两个条件仅给出

\[
\operatorname{Ric}(A)=g,\qquad \nabla A=0.
\]

可以再加入任意平行、Ricci-free 的代数曲率张量 \(W\)：

\[
A=-G+W,\qquad \nabla W=0,\qquad \operatorname{Ric}(W)=0.
\]

例如平坦四维环面上可取非零常系数 Weyl 型张量 \(W\)。于是

\[
T_{\rm old}=\operatorname{Rm}-G+W
\]

仍满足两个辅助性质，却不同于规范 \(T\)。

唯一性需要额外假设，例如：

* \(G_{\rm old}\) 被明确规定为 \(g\owedge g\) 的普适倍数；此时 Ricci 条件强迫 \(G_{\rm old}=-G\)；
* 或在代数曲率张量类别内再要求旧、规范辅助张量具有相同范数。此时 \(G_{\rm old}=-G+W\)，标量曲率部分与 Weyl 部分正交，故
  \[
  |G_{\rm old}|^2=|G|^2+|W|^2,
  \]
  相同范数迫使 \(W=0\)。

因此 Step 64 §2 的“those two properties force \(G_{\rm old}=-G\)”缺少关键代数假设。

---

### 3. 对 (a)–(d) 的判定

#### (a) 两种约定定义相同 \(T\)

**有条件为真。** 必须进行完整同步反射

\[
G_{\rm old}=-G,\qquad
\operatorname{Rm}+G_{\rm old}=\operatorname{Rm}-G.
\]

不能把旧的加号与规范的正 \(G=(g\owedge g)/(2(n-1))\) 同时保留。

#### (b) \(|G|^2\) 与 \(F_T\asymp F\)

符号反射下

\[
|-G|^2=|G|^2
\]

当然成立。并且对任一符号，

\[
\bigl||\operatorname{Rm}\pm G|-|\operatorname{Rm}|\bigr|\le |G|,
\]

所以

\[
1+|\operatorname{Rm}\pm G|^2\asymp_n1+|\operatorname{Rm}|^2.
\]

若作同步反射，则 \(T\) 本身相同，故 \(F_T\) 完全相同，而不仅是可比。若只把旧式字面读成 \(\operatorname{Rm}+G_{\rm canonical}\)，则两个 \(F_T\) 只可比，并非数值相等。

#### (c) 能量和耗散

在同步反射下，以下量确实逐点、逐时刻数值相同：

\[
H_2,\quad K_p,\quad Y,\quad\Gamma,
\]

以及由 \(F_T\)、\(\nabla F_T\)、\(\nabla T=\nabla\operatorname{Rm}\) 或 \(|\operatorname{Rm}|\) 构成的耗散和吸收参数。缺陷能量本来就不含 \(G\)。

但“数值完全不变”依赖于 \(T_{\rm old}=T\)，而不是仅依赖 \(F_T\asymp F\)。仅有后者只能推出维数常数意义下的可比性。

#### (d) \(U=aT\) 转换

基本微分恒等式确实与符号无关：

\[
\partial_tU=a\,\partial_tT
\]

因为 \(a=\chi^2\) 时间不变；同理

\[
\nabla U=a\nabla T+(\nabla a)*T,
\]

\[
\Delta U=a\Delta T+2\nabla a\cdot\nabla T+(\Delta a)T.
\]

但这不能证明完整 \(T\)-或 \(U\)-演化式的零阶项正确。将

\[
Q(\operatorname{Rm}),\quad
\operatorname{Rm}*E,\quad
\partial_tG
\]

改写成 \(T\)-变量时必须使用规范关系

\[
\boxed{\operatorname{Rm}=T+G}.
\]

这些零阶项可能出现补偿符号或系数错误；粗略的 \(CaF_T^3\) 估计会掩盖它们。

---

### 4. 必须真正翻转或修正的显示

以下不是可以直接原样保留的式子。

1. **定义**
   \[
   T=\operatorname{Rm}+G_{\rm old}
   \quad\rightsquigarrow\quad
   T=\operatorname{Rm}-G.
   \]

2. **静止参考**
   \[
   T=0\Longrightarrow\operatorname{Rm}=-G_{\rm old}
   \quad\rightsquigarrow\quad
   \boxed{\operatorname{Rm}=G}.
   \]
   Step 58 §2.1 已被注释，但 §2.2 的“\(\operatorname{Rm}=-G\)”仍是另一处未列入 Step 64 的旧符号。

3. **范数交叉项**

   Step 64 (2.6) 在规范 \(G\) 下写成了错误的加号。正确式为

   \[
   \boxed{
   |T|^2
   =|\operatorname{Rm}|^2
   -2\langle\operatorname{Rm},G\rangle+|G|^2.}
   \]

   旧符号下则为

   \[
   |T|^2
   =|\operatorname{Rm}|^2
   +2\langle\operatorname{Rm},G_{\rm old}\rangle+|G_{\rm old}|^2.
   \]

4. **\(G\) 的演化**

   规范符号下

   \[
   \partial_tG
   =-\frac{2a}{n-1}(E\owedge g),
   \]

   而

   \[
   \partial_tG_{\rm old}
   =+\frac{2a}{n-1}(E\owedge g).
   \]

5. **Step 58 §4.1 的代数关系**

   规范关系是

   \[
   \nabla^m\operatorname{Rm}=T_m+\nabla^mG,
   \]

   而不是 \(T_m-\nabla^mG\)。其实际应用限定于 \(m\ge1\)，此时 \(\nabla^mG=0\)，所以估计数值不变；但 \(m=0\) 时符号不可忽略。

---

### 5. Step 63 另有独立的因子二错误

这不是 KN 正负号问题，而是纯缩放校验本身错误。

Step 63 已写出

\[
\partial_t(g\owedge g)=2(h\owedge g).
\]

在 \(h=-2g\) 时，

\[
\partial_t(g\owedge g)=-4(g\owedge g),
\]

故

\[
\boxed{\partial_tG=-4G},
\]

不是 Step 63 §3.6 所写的 \(-2G\)。因此当 \(a=1,E=g\) 时

\[
\partial_t\operatorname{Rm}=-2\operatorname{Rm},
\]

\[
\boxed{\partial_tT
=-2\operatorname{Rm}+4G
=-2T+2G,}
\]

一般并非 \(-2T\)。

平坦环面给出直接反例：

\[
\operatorname{Rm}=0,\qquad T=-G,
\]

在 \(g(t)=e^{-2t}g_0\) 下 \(G(t)=e^{-4t}G_0\)，因此

\[
\partial_tT=-4T.
\]

同时四个逆度量的缩放恰好抵消 \(T\) 的协变缩放，所以

\[
\partial_t|T|_g^2=0,
\]

而非 Step 63 所写的 \(+4|T|^2\)。故 Step 63 §§3.6、5.3、9 中相应缩放行均需撤销重算。

这不会破坏

\[
\partial_tF_T^2
\le a\Delta F_T^2-2a|\nabla\operatorname{Rm}|^2+\cdots+CaF_T^3
\]

这类粗估计，因为修正后的零阶项仍由 \(CaF_T^3\) 控制；但它使 Step 58 中精确线性项 \(a(T*T+T)\) 的现有“缩放验证”失效，必须在规范关系 \(\operatorname{Rm}=T+G\) 下重新导出。

---

### 6. \(|G|^2\) 还存在范数归一化冲突

Step 63 §5.1 明示的是完整四指标收缩

\[
|A|^2
=g^{ip}g^{jq}g^{kr}g^{ls}A_{ijkl}A_{pqrs}.
\]

在此约定下

\[
|g_{ik}g_{jl}-g_{il}g_{jk}|^2=2n(n-1),
\]

从而

\[
\boxed{|G|^2=\frac{2n}{n-1}},
\]

四维时为 \(8/3\)，不是各笔记所引的 \(2/3\)。后一个数值对应在完整收缩前乘 \(1/4\) 的曲率算子范数。

因此必须二选一：

* 保留 Step 63 §5.1 的完整收缩，并把常数改为 \(2n/(n-1)\)；
* 或在所有曲率范数定义中明确加入 \(1/4\)。

此冲突不影响符号不变性和 \(F_T\asymp F\)，但影响声称“数值完全相同”的常数及全部依赖该归一化的精确显示。

---

## 最终判定

\[
\boxed{\text{同步反射 }G_{\rm old}=-G\text{ 后，估计栈与能量栈确实不变。}}
\]

但以下说法应予否定：

* 两个辅助性质本身强迫唯一的 \(T\)；
* 所有旧显示在固定标准 KN 约定下都可原样保留；
* Step 64 找到了全部符号问题；
* Step 63 的纯缩放校验验证了精确 \(T\)-演化。

遗漏的主要补偿错误通道是：把 \(\operatorname{Rm}=T+G\) 代入 \(Q(\operatorname{Rm})\)、Lichnerowicz 反应、度量变分和 \(\partial_tG\) 时，粗绝对值估计可隐藏错误的零阶符号或系数。精确的规范 \(T\)-演化及其线性项目前仍需从 Step 63 的指标公式重新计算。
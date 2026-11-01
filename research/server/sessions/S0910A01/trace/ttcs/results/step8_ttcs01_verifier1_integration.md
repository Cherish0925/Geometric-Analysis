# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 8,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step8_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step8_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 8 measure-local rigidity theorem for the four-dimensional LeBrun near-boundary negative-pinching route. Check (i) the primary-source Derdziński conformal factor and orientation/eigenvalue normalization used in the local contradiction, (ii) the local averaging lemma with local means under Ricci lower/doubling, (iii) the harmonic-coordinate passage through finite W^{2,p} convergence and smoothness of the limiting Einstein metric without derivative-Ricci assumptions on the approximating metrics, and (iv) the exact strength of the conclusion Vol{p: Vol(B_1(p))>=v}/Vol(M)->0 rather than pointwise collapse. Identify any mathematical gaps, missing hypotheses, or normalization errors that could invalidate the theorem.

## Integrated Scientific Memo

# Step 8 核验结论

## 总结

Step 8 的目标结论

\[
\frac{\operatorname{Vol}E_i(v)}{\operatorname{Vol}M_i}\to0,\qquad
E_i(v)=\{p:\operatorname{Vol}B_1(p)\ge v\},
\]

在下列全局输入成立时是正确的：

\[
\frac1{\operatorname{Vol}M_i}\int_{M_i}F_i\,d\mu_i\to0,
\qquad |\operatorname{Ric}_{g_i}+g_i|_{L^\infty}\to0.
\]

Derdziński 因子、取向和谱归一化均正确；局部均值引理正确；有限 \(W^{2,p}\) 调和坐标极限足够，而且不需要近似度量满足 \(\nabla\operatorname{Ric}\) 控制；证明只能推出非塌缩点集的体积比例趋零，不能推出逐点或一致塌缩。

不过原笔记仍有两个需要修正或补写的实质问题：

1. \(Q_i,P_i\) 未定义，因此
   \[
   \int \xi_i(Q_i+P_i)\le24\pi^2D_i
   \]
   及其精确系数无法由给定材料独立核验。应改用下述显式、规范的 LeBrun gap density。
2. 调和坐标中的“右端一致收敛”和直接对差方程应用标准估计说得过强；由 \(C^{1,\beta}\) 收敛只能得到 \(Q(\partial g_i)\) 在有限 \(L^q\) 中强收敛。经过正确的有限指数和可变系数椭圆估计仍能得到所需的强 \(W^{2,p}\) 收敛。

---

## 1. Derdziński 因子与取向：正确

Derdziński Proposition 5(i) 明确给出：若四维定向度量满足

\[
\delta W^+=0,\qquad \#\operatorname{spec}(W^+)\le2,
\]

则在 \(\{W^+\neq0\}\) 上

\[
\widehat g=(24\,g(W^+,W^+))^{1/3}g
          =(24|W^+|^2)^{1/3}g
\]

局部 Kähler，且 Kähler 取向与给定取向一致。Kähler 形式来自简单特征值对应的 \(\Lambda^+\)-特征向量。Proposition 5(ii) 给出本质唯一性；Proposition 5(iii) 给出

\[
|W^+|\ \text{常数}\iff \nabla W^+=0.
\]

对于 Kähler 取向，Derdziński Proposition 2 给出

\[
\operatorname{spec}(W^+)
 =\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right),
\qquad |W^+|^2=\frac{s^2}{24}.
\]

因此若 \(\operatorname{Ric}=-g\)，则 \(s=-4\)，Kähler–Einstein 谱应为

\[
\left(-\frac23,\frac13,\frac13\right),\qquad |W^+|^2=\frac23.
\]

Step 8 的校准谱

\[
\left(-\frac16,\frac1{12},\frac1{12}\right)
\]

则满足

\[
|W^+|^2=\frac1{24},\qquad
(24|W^+|^2)^{1/3}=1.
\]

故 Derdziński 构造的 Kähler 度量恰好就是极限度量本身，而不只是另一个共形代表。这与 Kähler–Einstein 恒等式

\[
|W^+|^2=\frac{s^2}{24}=\frac23
\]

直接矛盾。取向也一致：在 \(s<0\) 时简单特征值为 \(s/6\)，即校准谱中的 \(-1/6\)。

原笔记将 Kähler–Einstein 谱写成

\[
(1/3,1/3,-2/3)
\]

只是排列不同，不是符号或取向错误。

---

## 2. 建议用显式 LeBrun gap 代替未定义的 \(Q,P\)

令

\[
\alpha=\sqrt{\frac23},\qquad
f=\frac23s-2\alpha|W^+|,\qquad
a=\frac23s+2w,
\]

其中 \(w\) 是 \(W^+\) 的最小特征值，并令

\[
\xi=w+\alpha|W^+|\ge0.
\]

因为 \(a=f+2\xi\)，可定义完全显式的非负密度

\[
\mathcal G:=f^2-(a_-)^2,\qquad a_-=\min(a,0).
\]

其非负性正是

\[
w\ge-\sqrt{\frac23}|W^+|
\]

所对应的 LeBrun 点态比较。当 \(a<0\) 时，

\[
\mathcal G=f^2-a^2=-4\xi(f+\xi).
\]

在极限校准值

\[
s=-4,\qquad |W^+|=\frac1{2\sqrt6}
\]

下，

\[
f=-3,\qquad
\mathcal G=4\xi(3-\xi).
\]

又因 trace-free 三维对称算子的最小特征值满足

\[
-\sqrt{\frac23}|W^+|\le w\le0,
\]

这里 \(0\le\xi\le1/6\)，故

\[
\mathcal G=0\quad\Longrightarrow\quad \xi=0.
\]

于是

\[
w=-\sqrt{\frac23}|W^+|=-\frac16.
\]

其余两个特征值之和为 \(1/6\)，平方和为

\[
\frac1{24}-\frac1{36}=\frac1{72},
\]

从而二者均为 \(1/12\)。因此完整谱被推出，而不是预先假设：

\[
\operatorname{spec}(W^+)
 =\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

此外恒等式

\[
\frac{s^2}{24}+2|W^+|^2
=
\frac1{12}f^2+
\frac1{216}(s+8\sqrt6|W^+|)^2
\]

直接解释了 \(8\sqrt6\) 和校准值 \(1/24\)：它们来自 LeBrun Proposition 3.1 的 equality profile，而不是 Kähler 恒等式。这个区别正是局部矛盾的机制。

若

\[
D_i=
\frac1{4\pi^2}\int
\left(\frac{s_i^2}{24}+2|W_i^+|^2\right)d\mu_i
-\frac23A_i,
\]

则由 LeBrun 估计可取得足以证明定理的界

\[
\int\mathcal G_i\,d\mu_i\le48\pi^2D_i,
\]

以及

\[
\int(s_i+8\sqrt6|W_i^+|)^2\,d\mu_i
\le864\pi^2D_i.
\]

所以可以将 deficit density 改写为

\[
F_i=
|\operatorname{Ric}_{g_i}+g_i|^2
+(s_i+8\sqrt6|W_i^+|)^2
+\mathcal G_i.
\]

这样不再依赖未展示的 \(Q_i,P_i\)。原式中 \(24\pi^2\) 的精确系数只有在证明
\(\xi(Q+P)=\mathcal G/2\) 后才成立；该系数不是局部定理所必需。

---

## 3. 局部均值引理：正确

若

\[
\operatorname{Ric}\ge -(n-1)Kg,\qquad F\ge0,
\]

定义

\[
H_R(p)=\frac1{\operatorname{Vol}B_R(p)}
       \int_{B_R(p)}F\,d\mu.
\]

Fubini 给出

\[
\frac1{\operatorname{Vol}M}\int_MH_R(p)\,d\mu(p)
=
\frac1{\operatorname{Vol}M}\int_MF(x)
\left[
\int_{B_R(x)}
\frac{d\mu(p)}{\operatorname{Vol}B_R(p)}
\right]d\mu(x).
\]

若 \(p\in B_R(x)\)，则

\[
B_R(x)\subset B_{2R}(p).
\]

Bishop–Gromov doubling 因而给出

\[
\operatorname{Vol}B_R(x)
\le D(n,K,R)\operatorname{Vol}B_R(p),
\]

所以方括号至多为 \(D(n,K,R)\)，即

\[
\frac1{\operatorname{Vol}M}\int_MH_R
\le
D(n,K,R)\frac1{\operatorname{Vol}M}\int_MF.
\]

若

\[
\operatorname{Vol}E_i(v)\ge\eta\operatorname{Vol}M_i,
\]

则

\[
\frac1{\operatorname{Vol}E_i(v)}
\int_{E_i(v)}H_{i,1}
\le
\frac{D}{\eta}
\frac1{\operatorname{Vol}M_i}\int_{M_i}F_i
\to0.
\]

故存在 \(p_i\in E_i(v)\) 使 \(H_{i,1}(p_i)\to0\)。

近 Einstein 条件给出统一的双边 Ricci 界；特别是大 \(i\) 时

\[
|\operatorname{Ric}_{g_i}|\le3,\qquad
\operatorname{Ric}_{g_i}\ge-2g_i.
\]

由 \(p_i\in E_i(v)\) 和 Bishop–Gromov，

\[
\operatorname{Vol}B_{1/2}(p_i)\ge c(v)>0,
\]

同时 \(\operatorname{Vol}B_1(p_i)\) 有统一上界，因此

\[
\int_{B_1(p_i)}F_i\,d\mu_i\to0.
\]

这里必须使用局部平均值而不是局部绝对积分；后者在塌缩球上会自动变小。

---

## 4. 调和坐标极限：成立，但需按有限指数严谨表述

Cheeger–Naber Theorem 1.13 在四维、\(|\operatorname{Ric}|\le3\) 和单位球非塌缩下给出

\[
\operatorname{Vol}\!\left(
T_r\{x\in B_1(p_i):r_h(x)\le r\}
\right)\le C(v)r^4.
\]

选择 \(r_0(v)>0\) 使

\[
C(v)r_0^4<c(v)
\]

即可在 \(B_{1/2}(p_i)\) 中找到

\[
q_i,\qquad r_h(q_i)\ge r_0.
\]

缩小坐标域后，固定的调和坐标球包含在 \(B_1(p_i)\) 内。

在该坐标球上，Cheeger–Naber 的定义和调和坐标正则性给出每个有限 \(p\) 的统一

\[
C^{1,\alpha}\cap W^{2,p}
\]

界。取子列后，

\[
g_i\to g_\infty \quad\text{强于 }C^{1,\beta},
\qquad
g_i\rightharpoonup g_\infty\quad\text{于 }W^{2,p}.
\]

调和坐标方程为

\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=
-2(\operatorname{Ric}_{g_i})_{jk}
+Q_{jk}(g_i^{-1},\partial g_i).
\]

需要修正原笔记中“\(Q\) 一致收敛”的说法：从 \(C^{1,\beta}\) 紧性通常只有 \(\partial g_i\) 在 \(C^{0,\beta}\) 强收敛；若仅从有限 \(W^{2,p}\) 出发，则应陈述为在任意适当有限 \(L^q\) 中强收敛。由于可以先选择任意大的有限指数，二次项 \(Q\) 仍在所需 \(L^p\) 中强收敛。

又因

\[
\operatorname{Ric}_{g_i}=-g_i+e_i,\qquad
\|e_i\|_{L^\infty}\to0,
\]

方程右端在有限 \(L^p\) 中强收敛。结合系数
\(g_i^{ab}\to g_\infty^{ab}\) 的 \(C^0\) 强收敛和统一椭圆性，局部可变系数估计给出更小坐标球上的

\[
g_i\to g_\infty\qquad\text{强于 }W^{2,p}.
\]

极限弱满足

\[
\operatorname{Ric}_{g_\infty}=-g_\infty.
\]

其调和坐标 Einstein 方程随后对极限本身进行 bootstrap，推出 \(g_\infty\) 光滑。此处完全不需要 \(\nabla\operatorname{Ric}_{g_i}\) 的界，也没有推出近似度量的统一 \(C^{2,\alpha}\) 正则性。

取 \(p>2\) 并在需要时先取更大的有限指数，可得到曲率及其二次代数密度的 \(L^1\) 强收敛。还应明确固定坐标图的取向，使 \(W_i^+\to W_\infty^+\) 而不会交换为 \(W_\infty^-\)。

由于固定子球上

\[
\int F_i\to0,
\]

极限 deficit 几乎处处为零；极限光滑性将这些恒等式提升为处处成立。于是得到

\[
s_\infty=-4,\qquad
|W_\infty^+|^2=\frac1{24},\qquad
\operatorname{spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

再由 Einstein 条件得 \(\delta W_\infty^+=0\)，故可应用 Derdziński 并得到前述矛盾。

---

## 5. 结论的精确强度

反证只排除了以下情形：存在固定 \(v,\eta>0\) 和子列使

\[
\operatorname{Vol}E_i(v)\ge\eta\operatorname{Vol}M_i.
\]

因此严格结论恰为

\[
\boxed{
\forall v>0,\qquad
\frac{\operatorname{Vol}\{p:\operatorname{Vol}B_1(p)\ge v\}}
     {\operatorname{Vol}M_i}
\to0.
}
\]

等价地，对按归一化体积随机选取的点 \(p_i\)，

\[
\operatorname{Vol}B_1(p_i)\to0
\]

依概率成立。

它不推出

\[
\sup_{p\in M_i}\operatorname{Vol}B_1(p)\to0,
\]

也不推出固定 \(v\) 时 \(E_i(v)\) 最终为空。体积为
\(o(\operatorname{Vol}M_i)\) 的非塌缩岛仍可存在，并可承载拓扑、曲率集中或 bubble tree。因而将 Step 8 描述成“所有非塌缩区域逐点消失”是不成立的。

---

## 最终核验状态

在全局 Steps 3–7 确实证明

\[
D_i/A_i\to0,\qquad
\operatorname{Vol}M_i/A_i\to32\pi^2/9,
\qquad
\frac1{\operatorname{Vol}M_i}\int F_i\to0
\]

的条件下，Step 8 的 measure-local rigidity theorem 成立。给定材料尚不能独立核验这些前置 bookkeeping，尤其是原 \(Q_i,P_i\) 和 \(24\pi^2\) 系数。用显式 \(\mathcal G_i\) 替代它们后，局部谱锁定和 Derdziński 矛盾可以完全独立复核。
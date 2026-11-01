# TTCS Independent Branch Record

```json
{
  "step_id": 45,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A03/workspace/notes/step44_coefficient_regularization_start.md",
    "Sessions/S0910A03/workspace/notes/step44_normalized_yang_tame_start_restart.md",
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Check whether the coefficient-regularization construction now yields a genuine per-datum short-time existence and restart theorem for ∂_t g=-2χ²(Ric+g), assuming the corrected Step 45 finite-exponent ledger. Compare with Yang Theorem 8.2 Approach 2 and the Step 44 coefficient-regularization note. Examine fixed-ε geometric/DeTurck existence with a spatial coefficient, the first-exit bootstrap, uniform Sobolev upgrades, control of spatial and time derivatives, ε→0 compactness, passage to the exact degenerate equation, positivity, and smooth endpoint restart by time-jet matching. Identify any remaining circularity, missing gauge transport, dependence on ε, loss of derivatives, or need for uniqueness. State precisely what would be established for the restricted Ishida–LeBrun route, without treating it as a solution of Yau 26.

## Output

# 科学核验备忘

## 结论

把 Step 45 的任意阶张量族与有限指数能量闭合作为已证引理，并且对每个 \(\varepsilon>0\) 使用**带输运系数的准确 DeTurck 构造**，则系数正则化确实给出如下逐数据定理。

> **逐数据短时存在与重启定理。**  
> 设 \(M\) 紧致光滑，\(g_0\) 为光滑 Riemann 度量，\(\chi\in C^\infty(M)\)，\(0\leq\chi\leq1\)。则存在
> \[
> T=T(g_0,\chi)>0
> \]
> 及光滑正定度量族 \(g(t)\)，满足
> \[
> \partial_tg=-2\chi^2(\operatorname{Ric}_g+g),\qquad g(0)=g_0,
> \quad 0\leq t\leq T.
> \]
> 此外，若某个此类解在 \(t\uparrow T_*\) 时收敛到光滑正定度量 \(g_*\)，则存在 \(\delta>0\)，可将它光滑延拓到 \([0,T_*+\delta]\)。

这里的 \(T\) 可以依赖 \((g_0,\chi)\) 的全部光滑范数。该构造本身只给出子列极限；不借助另一个唯一性论证时，不推出不同 \(\varepsilon_j\to0\) 子列产生同一个解。

---

## 1. 固定 \(\varepsilon\) 的 DeTurck 构造必须输运系数

令
\[
b_\varepsilon=\chi^2+\varepsilon^2,\qquad \varepsilon>0.
\]
Yang 定理 8.2 的 Approach 2 明确讨论
\[
\partial_tg=-2(\varepsilon^2+\chi^2)\operatorname{Ric}_g
\]
并指出它可通过 DeTurck 方法构造；加入 \(-2b_\varepsilon g\) 只改变零阶项，不改变主符号。

但这里有一个必须写清的几何点。若在 hatted 坐标中把 \(b_\varepsilon\) 固定不动，解
\[
\partial_t\widehat g
=-2b_\varepsilon(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{b_\varepsilon W(\widehat g)}\widehat g
\]
再作通常的 DeTurck 拉回，所得方程的系数一般是
\(\varphi_t^*b_\varepsilon\)，而不是原来的 \(b_\varepsilon\)。

一个准确的写法是
\[
\widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1},
\]
并取
\[
\partial_t\widehat g
=-2\widehat b_\varepsilon
  (\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_X\widehat g,
\qquad
X=\widehat b_\varepsilon W(\widehat g,\bar g),
\]
\[
\partial_t\varphi_t=-X\circ\varphi_t,\qquad \varphi_0=\mathrm{id}.
\]
于是
\[
\varphi_t^*\widehat b_\varepsilon=b_\varepsilon
\]
且
\[
g_\varepsilon=\varphi_t^*\widehat g
\]
准确满足
\[
\partial_tg_\varepsilon
=-2b_\varepsilon(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon).
\]

等价地，hatted 系数满足输运方程
\[
\partial_t\widehat b_\varepsilon=X(\widehat b_\varepsilon).
\]
其取值沿输运保持，故
\[
\widehat b_\varepsilon\geq\varepsilon^2.
\]
度量方程的主部为
\[
\widehat b_\varepsilon\,
\widehat g^{pq}\bar\nabla_p\bar\nabla_q\widehat g,
\]
所以对每个固定 \(\varepsilon>0\) 为强抛物型。相应局部存在时间及 DeTurck 估计可以依赖 \(\varepsilon^{-1}\)；公共时间并不从这里取得。

因此，Step 44 中“固定 \(\varepsilon\) 的严格抛物 DeTurck 解”应理解为 Yang 的准确输运构造。Step 45 的张量能量必须应用于拉回后的几何解 \(g_\varepsilon\)，因为只有在那里
\[
\partial_tb_\varepsilon=0.
\]

---

## 2. 第一退出自举现在闭合，且不借用 Yang 的公共时间结论

设
\[
T_\varepsilon
=\operatorname{Rm}_{g_\varepsilon}
+\frac{g_\varepsilon\owedge g_\varepsilon}{2(n-1)},
\qquad
U_\varepsilon=b_\varepsilon T_\varepsilon.
\]
取
\[
K_0=1+\sup_{0<\varepsilon\leq1}
\|U_\varepsilon(0)\|_{L^\infty(g_0)},\qquad K=2K_0.
\]
在满足
\[
\|U_\varepsilon\|_\infty\leq K,\qquad
\tfrac12g_0\leq g_\varepsilon\leq2g_0
\]
的首个区间上，Step 44 的零阶 \(T_0\) 估计和 Step 45 的交错次序给出，对每个有限 \(m,p\)，
\[
\sup_t\left(
 \|\nabla^mU_\varepsilon\|_{L^p}
 +\|\nabla^{m+1}\chi\|_{L^p}
 +\|\nabla^mT_\varepsilon\|_{L^p}
 \right)\leq C_{m,p},
\]
其中 \(C_{m,p}\) 与 \(\varepsilon\) 无关。

其正则化一致性来自 Step 45 的四个具体事实：
\[
0<b_\varepsilon\leq2,\qquad
\nabla^rb_\varepsilon=\nabla^r(\chi^2)\quad(r\geq1),
\]
\[
\frac{|db_\varepsilon|^2}{b_\varepsilon}
\leq4|d\chi|^2,\qquad
\frac{\chi^2}{b_\varepsilon}\leq1.
\]
特别是
\[
(db_\varepsilon*db_\varepsilon)*T
=4\chi^2(d\chi*d\chi)*T
\]
保留了将 \(T\) 转成 \(U=bT\) 所需的 \(\chi^2\)。这正是 \(m=1\) 起始层不会要求 \(\|T_0\|_\infty\) 的原因。

由于度量与 \(g_0\) 双 Lipschitz 等价，固定背景的标量 Sobolev 不等式与 Kato 不等式给出，对 \(p>n\)，
\[
\|A\|_{L^\infty}
\leq C\bigl(\|A\|_{L^p}+\|\nabla A\|_{L^p}\bigr).
\]
对 \(A=U_m,T_m,C_{m+1}\) 使用下一阶估计，即得所有这些张量的逐点一致有界性。这里不使用无权扩散，也不需要 \(b_\varepsilon\) 的正下界。

由 Step 45 的
\[
\partial_tU
=b\Delta U+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+bU+b^2
\]
可得
\[
\|\partial_tU_\varepsilon\|_\infty\leq C(g_0,\chi,K),
\]
而
\[
\partial_tg_\varepsilon=-2\operatorname{Ric}(U_\varepsilon)
\]
给出
\[
|\partial_tg_\varepsilon|_{g_\varepsilon}\leq C_nK.
\]
初始时 \(\|U_\varepsilon(0)\|_\infty\leq K_0-1\)，故选取仅依赖数据的充分小时间 \(T_0\)，可以同时得到
\[
\|U_\varepsilon(t)\|_\infty<K_0<K
\]
以及比 \(\tfrac12g_0\leq g_\varepsilon\leq2g_0\) 更强的度量比较。

若某个固定 \(\varepsilon\) 的解在 \(T_0\) 以前终止而未发生首次退出，则上述任意阶估计产生光滑正定终端度量；固定 \(\varepsilon\) 的局部理论可从该度量再次启动。由此所有 \(g_\varepsilon\) 存在于同一个 \([0,T_0]\)。

这没有循环使用 Yang Approach 2 中“公共时间”的后半部分：Yang 在此仅提供每个固定 \(\varepsilon\) 的起始解，公共时间由 Step 45 的几何能量和第一退出改进产生。

---

## 3. 从协变导数到固定坐标紧性还需写出一个标准桥接引理

Step 45 第 6 节从“所有协变空间导数有界”直接跳到“所有时空导数有界”。结论正确，但完整证明应加入连接差张量。

固定 \(\bar\nabla=\nabla^{g_0}\)，令
\[
A_\varepsilon=\nabla^{g_\varepsilon}-\bar\nabla.
\]
连接变分公式给出
\[
\partial_tA_\varepsilon
=g_\varepsilon^{-1}*\nabla\operatorname{Ric}(U_\varepsilon).
\]
因此 \(U_1\) 的逐点估计先控制 \(A_\varepsilon\)。对该公式取 \(\bar\nabla^k\)，并用
\[
\bar\nabla=\nabla+A_\varepsilon
\]
归纳，可得
\[
\sup_{M\times[0,T_0]}
|\bar\nabla^kA_\varepsilon|\leq C_k.
\]
随后
\[
\bar\nabla g_\varepsilon=A_\varepsilon*g_\varepsilon
\]
及其高阶导数给出
\[
\sup_{M\times[0,T_0]}
|\bar\nabla^kg_\varepsilon|\leq C_k.
\]

时间导数可从固定坐标微分算子
\[
\mathcal F_\varepsilon(g)
=-2b_\varepsilon(\operatorname{Ric}_g+g)
\]
递归取得。每次时间微分最多增加两个空间导数；由于所有空间阶均已一致控制，任意混合导数均有界。此过程只乘以 \(b_\varepsilon\) 及其导数，从不除以 \(b_\varepsilon\)，所以不产生 \(\varepsilon^{-1}\)。

这个连接差引理同时完成两件事：

1. 排除 DeTurck 坐标漂移对紧性的影响；
2. 为固定 \(\varepsilon\) 的终端延拓提供固定坐标 \(C^\infty\) 收敛。

---

## 4. \(\varepsilon\to0\) 极限、正定性与准确方程

由上述固定背景时空导数估计，在紧致 \(M\times[0,T_0]\) 上可取子列
\[
g_{\varepsilon_j}\longrightarrow g
\quad\text{于 }C^\infty.
\]
度量比较
\[
\tfrac12g_0\leq g_{\varepsilon_j}\leq2g_0
\]
传递到极限，所以 \(g(t)\) 始终正定。

又因为
\[
b_{\varepsilon_j}=\chi^2+\varepsilon_j^2
\longrightarrow\chi^2
\quad\text{于 }C^\infty,
\]
且 Ricci 张量对 \(C^\infty\) 度量连续，逐项通过方程得到
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g),
\qquad g(0)=g_0.
\]
在 \(\{\chi=0\}\) 上，这一等式来自光滑极限，而不是来自“该区域动力学可忽略”的推断。

固定 \(\varepsilon\) 的 DeTurck 微分同胚不需要任何一致估计；紧性是在已经拉回、满足准确几何方程的 \(g_\varepsilon\) 上证明的。

---

## 5. 光滑终端重启不需要唯一性

设已有解在 \(t\uparrow T_*\) 时于 \(C^\infty\) 收敛到正定度量 \(g_*\)。将上述逐数据定理应用于 \((g_*,\chi)\)，得到右侧解 \(h(s)\)。

记
\[
\mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g).
\]
方程自治，因此两侧的一阶时间导数均为
\[
\partial_tg(T_*^-)=\mathcal F(g_*)
=\partial_sh(0^+).
\]
继续微分，
\[
\partial_t^2g(T_*^-)
=D\mathcal F(g_*)[\mathcal F(g_*)]
=\partial_s^2h(0^+),
\]
更高阶时间导数由同样递归确定。每个时间阶都是 \(g_*\) 的有限阶空间微分算子，所以左右全部时间 jet 以及其空间导数相同。拼接后的度量因此光滑并满足原方程。

这一延拓存在性不需要唯一性。唯一性只在以下陈述中需要：正则化子列无关、重启分支无关，或构造一个典范的极大流。

---

## 6. 对四维 Ishida–LeBrun \(\lambda<0\) 支线实际提供的内容

在 Step 45 张量引理成立的前提下，这套构造提供：

- 对每个固定四维初始度量和固定 cutoff，归一化局部 Ricci 流的真实光滑起始解；
- 在加权曲率、度量比较及交错导数估计保持时，得到光滑正定终端度量；
- 从该终端度量再次启动并光滑拼接；
- 使后续同时第一退出论证可以作用于一条实际存在的流，而不再依赖形式演化式。

它没有给出坍缩度量族共同的观察时间；该时间仍须来自后续独立的序列一致加权估计。它也没有产生维数常数 \(c_n,C_n\)、任意维拓扑结论或 Einstein 度量，因此并未证明或证伪 Yau 第 26 题。

概括而言，Step 45 消除了正则化能量中的主要 \(\varepsilon\)-奇异性；当前论证中应显式补入的是“输运后的 DeTurck 系数”和“连接差张量到固定坐标紧性”这两个桥接步骤。加入它们后，逐数据短时存在与光滑重启在数学上闭合。
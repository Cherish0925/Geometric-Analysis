# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 45,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step45_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step45_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check whether the coefficient-regularization construction now yields a genuine per-datum short-time existence and restart theorem for ∂_t g=-2χ²(Ric+g), assuming the corrected Step 45 finite-exponent ledger. Compare with Yang Theorem 8.2 Approach 2 and the Step 44 coefficient-regularization note. Examine fixed-ε geometric/DeTurck existence with a spatial coefficient, the first-exit bootstrap, uniform Sobolev upgrades, control of spatial and time derivatives, ε→0 compactness, passage to the exact degenerate equation, positivity, and smooth endpoint restart by time-jet matching. Identify any remaining circularity, missing gauge transport, dependence on ε, loss of derivatives, or need for uniqueness. State precisely what would be established for the restricted Ishida–LeBrun route, without treating it as a solution of Yau 26.

## Integrated Scientific Memo

# 核验结论

在**假定 Step 45 的有限指数张量 ledger 确实完备且成立**、并采用正确的固定 \(\varepsilon\) DeTurck/输运系数构造后，系数正则化路线能够给出真正的逐数据结论：

> 对闭流形 \(M\)、光滑正定 \(g_0\) 及固定 \(\chi\in C^\infty(M)\), \(0\leq\chi\leq1\)，存在  
> \[
> T=T(g_0,\chi)>0
> \]
> 和光滑正定解
> \[
> \partial_tg=-2\chi^2(\operatorname{Ric}_g+g),\qquad g(0)=g_0
> \]
> 于 \(M\times[0,T]\)。若某一此类解在有限端点平滑收敛到正定度量 \(g_*\)，则可从 \(g_*\) 重新启动，并通过时间 jet 匹配得到光滑延拓。

此结论是**存在及重启**；系数正则化本身不证明退化方程的唯一性，也不保证不同 \(\varepsilon_j\to0\) 子列给出同一极限。

---

## 1. 与 Yang Theorem 8.2 Approach 2 的关系

Yang 的原文明确采用
\[
\partial_tg_\varepsilon
=-2(\chi^2+\varepsilon^2)\operatorname{Ric}_{g_\varepsilon}
\]
并称其经 DeTurck 化为严格抛物系统，再以 \(\varepsilon\)-一致曲率能量获得共同时间并取极限。加入
\[
-2(\chi^2+\varepsilon^2)g_\varepsilon
\]
只是零阶项，不改变固定 \(\varepsilon\) 的主符号。因此 Yang Approach 2 支持固定 \(\varepsilon\) 的局部存在框架，但其原文并未提供本任务所需的详细任意阶一致 ledger；Step 44–45 正是在补这个压缩环节。

这里必须补正一个几何细节。令
\[
b_\varepsilon=\chi^2+\varepsilon^2.
\]
在 hatted DeTurck 系统中不能简单把 \(b_\varepsilon\) 当作固定空间函数后再通常拉回，否则系数会变成 \(\varphi_t^*b_\varepsilon\)。应使用输运系数
\[
\widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1},
\]
例如取
\[
\partial_t\widehat g
=-2\widehat b_\varepsilon(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_X\widehat g,
\qquad X=\widehat b_\varepsilon W(\widehat g,\bar g),
\]
\[
\partial_t\varphi=-X\circ\varphi.
\]
则
\[
\varphi_t^*\widehat b_\varepsilon=b_\varepsilon
\]
且 \(g_\varepsilon=\varphi_t^*\widehat g\) 精确满足几何方程。固定 \(\varepsilon>0\) 时 \(\widehat b_\varepsilon\geq\varepsilon^2\)，故 hatted 系统严格抛物；该固定-\(\varepsilon\) 理论的常数可以依赖 \(\varepsilon^{-1}\)。

Step 45 的能量计算则必须施加在拉回后的几何解 \(g_\varepsilon\) 上，因为在那里
\[
\partial_tb_\varepsilon=0.
\]
共同存在时间不是由固定-\(\varepsilon\) DeTurck 估计取得，而是由后续几何能量和第一退出改进取得，故没有循环。

---

## 2. Step 45 修复为何足以消除 \(\varepsilon\)-奇性

设
\[
T=\operatorname{Rm}+\frac{g\owedge g}{2(n-1)},\qquad U=b_\varepsilon T.
\]
Yang 原文第 9 节给出的局部 Ricci 流曲率方程具有
\[
\chi^2(\Delta\operatorname{Rm}+Q(\operatorname{Rm},\operatorname{Rm}))
+2\chi\nabla\chi*\nabla\operatorname{Rm}
+\nabla\chi*\nabla\chi*\operatorname{Rm}
+\chi\nabla^2\chi*\operatorname{Rm}
\]
结构，与 Step 45 的
\[
\partial_tT
=b\Delta T+B_1*\nabla T+B_2*T+b(T*T+T+1)
\]
一致；归一化仅添加低阶代数项。

一致估计只使用
\[
0<b_\varepsilon\leq2,\qquad
\nabla^rb_\varepsilon=\nabla^r(\chi^2)\quad(r\geq1),
\]
\[
\frac{|db_\varepsilon|^2}{b_\varepsilon}
=4\frac{\chi^2}{\chi^2+\varepsilon^2}|d\chi|^2
\leq4|d\chi|^2,
\qquad
\frac{\chi^2}{b_\varepsilon}\leq1.
\]
没有任何一步需要 \(b_\varepsilon^{-1}\) 的导数或无权椭圆性。

最关键的修复是
\[
(db*db)*T=4\chi^2(d\chi*d\chi)*T.
\]
因此当前 \(T_m\) 项可以写为
\[
4\frac{\chi^2}{b}(d\chi*d\chi)*U_m
\]
加低阶项，而不会引入不可用的 \(T_0\in L^\infty\)。同样，顶层 cutoff 耦合
\[
B_{m+1}*B_1*T_0
\]
的首项为
\[
4\frac{\chi^2}{b}C_{m+1}*C_1*U_0,
\]
具有一致有界系数。这正是旧 ledger 的实质性缺口。

在假定 T1–T6、U1–U7 的枚举完备时：

* 当前二次曲率项的系数是 \(bT_0=U_0\)，而不是 \(T_0\)；
* 空间交换子的零阶曲率系数由
  \[
  b\operatorname{Rm}=U-bG
  \]
  控制；
* \(T_{m+1}\)、\(U_{m+1}\) 只乘 \(B_1\)，可由
  \[
  |B_1|^2/b\leq4|C_1|^2
  \]
  吸收；
* signed Hessian 项先积分分部，不能粗略取 \(\|\nabla^2\chi\|_\infty\)；
* 当前 \((U_m,C_{m+1})\) 必须联合估计，然后才估计 \(T_m\)。

结合 Step 44 的零阶种子，交错次序
\[
T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
\longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots
\]
遂对每个有限 \(m,p\) 给出
\[
\sup_t\left(
\|\nabla^mU_\varepsilon\|_{L^p}
+\|\nabla^{m+1}\chi\|_{L^p}
+\|\nabla^mT_\varepsilon\|_{L^p}
\right)\leq C_{m,p},
\]
其中 \(C_{m,p}\) 依赖完整数据、bootstrap 常数和阶数，但不依赖 \(\varepsilon^{-1}\)。Hölder 只要求前面已完成层级的某些更大但有限指数，没有当前指数无限升级或导数损失。

---

## 3. 第一退出闭合且不循环

取
\[
K_0=1+\sup_{0<\varepsilon\leq1}
\|U_\varepsilon(0)\|_\infty,\qquad K=2K_0,
\]
并考察首个满足
\[
\|U_\varepsilon\|_\infty\leq K,\qquad
\tfrac12g_0\leq g_\varepsilon\leq2g_0
\]
的区间。

在度量双 Lipschitz 比较下，可使用固定背景 Sobolev 常数。对足够大的 \(p>n\)，由相邻两个协变导数层级和标量 Sobolev/Kato 得到所有 \(U_j,T_j,C_{j+1}\) 的一致逐点界。特别地，
\[
\partial_tU
=b\Delta U+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+bU+b^2
\]
给出
\[
\|\partial_tU_\varepsilon\|_\infty
\leq C(g_0,\chi,K),
\]
而
\[
\partial_tg_\varepsilon=-2\operatorname{Ric}(U_\varepsilon)
\]
给出
\[
|\partial_tg_\varepsilon|_{g_\varepsilon}\leq C_nK.
\]

因初值距 \(\|U\|_\infty=K\) 有统一余量，选取仅依赖数据的充分小 \(T_0>0\)，可同时严格改进 \(U\) 界和度量比较。若固定 \(\varepsilon\) 的最大时间小于 \(T_0\) 而未首退，则任意阶估计及固定-\(\varepsilon\) 抛物延拓会延长该解，矛盾。因此所有正则化流均存在于同一 \([0,T_0]\)。

这里 bootstrap 假设只用于建立估计，然后被严格改进；共同时间没有预先借用 Yang Approach 2 的结论。

---

## 4. 从协变估计到固定坐标 \(C^\infty\) 紧性

Step 45 原文在此略跳了一步，但无需依赖 \(\varepsilon\)-一致 DeTurck 微分同胚。可直接在几何解上固定
\[
\bar\nabla=\nabla^{g_0},\qquad
A_\varepsilon=\nabla^{g_\varepsilon}-\bar\nabla.
\]
连接变分满足
\[
\partial_tA_\varepsilon
=g_\varepsilon^{-1}*\nabla\operatorname{Ric}(U_\varepsilon).
\]
由 \(U_1\) 的逐点界积分得到 \(A_\varepsilon\) 的一致界；对该方程取 \(\bar\nabla^k\)，并利用
\[
\bar\nabla=\nabla+A_\varepsilon
\]
归纳，得到
\[
\sup_{M\times[0,T_0]}|\bar\nabla^kA_\varepsilon|\leq C_k.
\]
再由
\[
\bar\nabla g_\varepsilon=A_\varepsilon*g_\varepsilon
\]
取得
\[
\sup_{M\times[0,T_0]}|\bar\nabla^kg_\varepsilon|\leq C_k.
\]

时间导数由固定坐标方程
\[
\partial_tg_\varepsilon
=-2b_\varepsilon(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon)
\]
递归控制；每取一次时间导数至多消耗有限个额外空间导数，而所有空间阶已可用。该递归只乘 \(b_\varepsilon\) 及其空间导数，从不除以它。因此得到所有固定背景混合时空导数的一致界。

这比试图直接证明 DeTurck 微分同胚 \(\varphi_\varepsilon\) 一致收敛更简洁，并排除了潜在的 gauge 漂移缺口。

---

## 5. 极限、正定性及精确退化方程

由紧致性和上述固定背景估计，可取子列
\[
g_{\varepsilon_j}\to g
\quad\text{于 }C^\infty(M\times[0,T_0]).
\]
度量比较传递到极限：
\[
\tfrac12g_0\leq g(t)\leq2g_0,
\]
故极限始终正定。

又因
\[
b_{\varepsilon_j}=\chi^2+\varepsilon_j^2
\to\chi^2
\quad\text{于 }C^\infty,
\]
Ricci 对光滑正定度量平滑依赖，逐项通过方程得到
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g),\qquad g(0)=g_0.
\]
在 \(\{\chi=0\}\) 上的等式来自精确光滑极限，不能用“该区域动力学可忽略”代替。

---

## 6. 光滑端点重启与唯一性

若已有解在 \(t\uparrow T_*\) 时于 \(C^\infty\) 收敛到正定 \(g_*\)，将逐数据存在定理应用于 \((g_*,\chi)\) 得到右侧解。记
\[
F(g)=-2\chi^2(\operatorname{Ric}_g+g).
\]
自治性给出
\[
\partial_tg(T_*^\pm)=F(g_*),
\]
\[
\partial_t^2g(T_*^\pm)=DF(g_*)[F(g_*)],
\]
且高阶时间导数递归为 \(g_*\) 的有限阶空间微分表达式。因左侧已有 \(C^\infty\) 极限，全部空间—时间 jets 匹配，故拼接解为 \(C^\infty\) 并跨端点满足方程。

这一“存在某个延拓”不需要唯一性。唯一性只用于：

* 证明所有 \(\varepsilon_j\to0\) 子列极限相同；
* 证明重启分支唯一；
* 定义典范最大流。

若后续 Ishida–LeBrun 论证只需在某一实际存在的共同流上执行 simultaneous first-exit，则存在性足够；若需要子列无关或典范流，则应另行引入 Yang Approach 1 的 coupled \((\widehat g,\varphi)\) 唯一性，不能声称 Approach 2 自身已经给出。

---

## 7. 剩余数学义务

在本任务明确“假定 corrected Step 45 finite-exponent ledger”的条件下，下游存在—紧性—重启链条已经闭合。若要将该定理做成完全独立证明，仍需证明的核心对象正是 ledger 的完备性：

\[
[\nabla^m,b\Delta],\qquad
\nabla^r(\partial_t\Gamma),\qquad
\partial_t\nabla^{m+1}\chi,
\]
以及所有 signed Hessian/cutoff 收缩均确实落入 T1–T6、U1–U7，且没有遗漏带无权 \(T_0\) 的当前系数、\(U_{m+1}\) 或过高 cutoff jet。Yang 原文验证了基础曲率方程和 Approach 2 框架，但不替代这一任意阶索引证明。Step 45 的星号仍隐藏数值系数和槽位排列；若“ledger 已核准”只是工作假设而非已证引理，那么完整定理仍条件性地依赖此对象。

---

## 对 restricted Ishida–LeBrun 路线的精确产出

该结果提供：

1. 每个固定四维初始度量和固定 cutoff 的归一化局部 Ricci 流真实光滑启动；
2. 无 \(\varepsilon^{-1}\) 的逐数据任意阶传播及共同正时间；
3. 光滑正定端点与无需唯一性的存在性重启；
4. 后续加权曲率/defect simultaneous first-exit 可以施加于一条实际流，而不再只操作形式演化式。

它不提供坍缩序列的一致观察时间；那仍来自独立的序列一致估计。它也不覆盖正分支、一般四维拓扑、\(n\ge5\)、维数唯一夹逼常数、Einstein 度量存在性或 Lean 形式化。因此这是 restricted negative Ishida–LeBrun smoothing route 的一个分析接口，而不是 Yau 第 26 题的证明或证伪。
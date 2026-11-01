# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 45,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step45_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step45_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the corrected coordinate-time tensor ledger for the normalized coefficient flow. The active equations are ∂_t g=-2 Ric(U), T=Rm+g∧g/[2(n-1)], U=bT, b=χ²+ε². Read the new Step 45 note, the superseded Step 44 ledger, Wang's exact coordinate-time local Ricci-flow formulas, and the zero-order seed. Verify: (i) consistency of the ∂_t convention, ∂_t G, ∂_tΓ, [∂_t,∇^m], and cutoff-jet evolution; (ii) the base T and division-free U equations including all coefficient weights; (iii) the corrected differentiated family ∇^{r+1}b*∇^{s+1}b*T_t and its χ factors; (iv) exhaustive current-variable allocations, spatial/time commutators, and signed integrations; (v) whether the staggered finite-Lp estimates really close uniformly for b=χ²+ε² without hidden T∞, current-exponent escalation, ε^{-1}, or an omitted current derivative. Give explicit corrections to any formula or inference; do not infer correctness from schematic notation alone.

## Integrated Scientific Memo

# 核验结论

Step 45 的两项核心修正确实有效：

1. 全程采用坐标时间导数 \(\partial_t\)，消除了 Step 44 中 \(D_t\) 与 \(\partial_tG\) 混用的问题；
2. 将
   \[
   (db*db)*T
   \]
   的微分族保留为
   \[
   B_{r+1}*B_{s+1}*T_t,\qquad r+s+t=m,
   \]
   正确保留了两个 \(\chi\) 因子，从而避免在当前 \((U_m,C_{m+1})\) 阶段要求 \(T_0\in L^\infty\)。

在给定光滑固定-\(\varepsilon\) 解、\(\|U_0\|_\infty\le K\) 和度量双 Lipschitz 等价的 bootstrap 假设下，交错有限-\(L^p\) 归纳可对 \(0<\varepsilon\le1\) 一致闭合；未发现隐藏的 \(T_\infty\)、当前层指数升级、\(\varepsilon^{-1}\) 或遗漏的当前阶导数。

但 Step 45 仍有三处必须作字面修正，另有一处需要更精确地表述。

---

## 1. 时间 convention 与基本变分

令
\[
S=\operatorname{Ric}(U),\qquad \partial_tg=-2S.
\]

### 1.1 \(\partial_tG\) 少了因子 \(2\)

由于
\[
G=\frac{g\owedge g}{2(n-1)},
\]
应有
\[
\begin{aligned}
\partial_tG
&=\frac{(-2S)\owedge g+g\owedge(-2S)}{2(n-1)}\\
&=-\frac{S\owedge g+g\owedge S}{n-1}.
\end{aligned}
\]
因此 Step 45 (1.2) 的分母 \(2(n-1)\) 错了，应为 \(n-1\)。

缩放检验也立即显示这一点：若 \(S=g\)，则 \(\partial_tg=-2g\)，而 \(G\) 关于 \(g\) 二次，故 \(\partial_tG=-4G\)；原式只给出 \(-2G\)。

此错误只改变低阶归一化项的固定数值系数，不改变后续系数权重或闭合机制。

### 1.2 \(\partial_t\Gamma\)、时间交换子正确

坐标时间下
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}
\bigl(\nabla_iS_{j\ell}+\nabla_jS_{i\ell}-\nabla_\ell S_{ij}\bigr)
\]
正确。因 \(S=\operatorname{Ric}(U)\) 且 \(\nabla g^{-1}=0\)，对有序协变导数，
\[
\nabla^r(\partial_t\Gamma)=g^{-1}*U_{r+1}.
\]

因此
\[
\partial_t(\nabla^mA)
=\nabla^m(\partial_tA)
+\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^sA
\]
正确。导数槽重排会产生 \(\nabla^q\operatorname{Rm}\) 乘较低阶导数，但不会额外产生 \(U_{m+1}\)。

### 1.3 cutoff jets 正确

因 \(\chi\) 是固定标量，
\[
\partial_t(d\chi)=0.
\]
故
\[
\partial_tC_{m+1}
=\sum_{r+s=m-1}U_{r+1}*C_{s+1}.
\]
唯一当前阶分配是
\[
U_m*C_1.
\]
原始 jet 方程中没有 \(U_{m+1}\)、\(C_{m+2}\)，也没有 \(U_0*C_{m+1}\)；后者只在微分张量范数和体积元时出现。

---

## 2. 基础 \(T\)、\(U\) 方程及系数权重

Wang 的精确坐标公式显示，局部 Ricci 流曲率演化由以下部分组成：

- \(b\Delta\operatorname{Rm}\)；
- \(\nabla b*\nabla\operatorname{Ric}\)；
- \(\nabla^2b*\operatorname{Ric}\)；
- 所有二次曲率反应均带 \(b\)。

加入平行 shift \(G\) 及已修正的代数项 \(\partial_tG\) 后，结构式
\[
\partial_tT
=b\Delta T+B_1*\nabla T+B_2*T+b(T*T+T+1)
\]
的全部系数权重正确。这里星号可隐藏固定数值和槽排列，但不能隐藏 \(b,B_1,B_2\) 的权重；Step 45 在此方面合格。

由
\[
\nabla U=b\nabla T+B_1*T,
\qquad
\Delta U=b\Delta T+2B_1*\nabla T+(\Delta b)T
\]
以及 \(\partial_tb=0\)，得到
\[
\partial_tU
=b\Delta U+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+bU+b^2.
\]
各星号项的符号和固定系数未被指定，但结构权重正确。唯一未加权的曲率因子确实只在
\[
(B_1*B_1)*T
\]
中。

---

## 3. 微分族与当前变量分配

### 3.1 修正后的 \((B_1B_1)T\) 微分族正确

精确 Leibniz 分配为
\[
B_{r+1}*B_{s+1}*T_t,\qquad r+s+t=m.
\]
不能整体替换成 \(C_{r+1}*C_{s+1}*T_t\)，因为
\[
B_k=2\chi C_k+\sum_{\mathcal P_k}'C_{|I|}*C_{k-|I|}.
\]

当前 \(T_m\) 只来自 \((r,s,t)=(0,0,m)\)：
\[
\begin{aligned}
B_1*B_1*T_m
&=4\chi^2(C_1*C_1)*T_m\\
&=4\frac{\chi^2}{b}(C_1*C_1)*
\left(U_m-\sum_{q=1}^m B_q*T_{m-q}\right).
\end{aligned}
\]
其当前系数由 \(4|C_1|^2\) 一致控制。

当前 cutoff jet \(C_{m+1}\) 只来自
\[
(m,0,0),\qquad(0,m,0).
\]
领先部分为
\[
(2\chi C_{m+1})*(2\chi C_1)*T_0
=4\frac{\chi^2}{b}C_{m+1}*C_1*U_0.
\]
这正是关键修复：只需 \(U_0\in L^\infty\)，不需 \(T_0\in L^\infty\)。

若直接讨论 \(\varepsilon=0\)，不应在 \(\chi=0\) 处字面使用 \(\chi^2/b\)。应写成
\[
4\chi^2C_{m+1}C_1T_0=4C_{m+1}C_1U_0
\]
以及
\[
B_1B_1T_m=4C_1C_1\,(bT_m),
\]
或明示采用连续延拓约定。正则化估计本身只需 \(\varepsilon>0\)。

### 3.2 空间交换子需显式保留 \(\operatorname{Rm}\)

准确形式是
\[
b\sum_{r+s=m}\nabla^r\operatorname{Rm}*\nabla^sA.
\]
当 \(r\ge1\) 时可用 \(T_r\)；当 \(r=0\) 时必须使用
\[
b\operatorname{Rm}=b(T-G)=U-bG.
\]
因此 Step 45 的 \(b*T_r*A_s\) 记法只有在附带这个 \(G\)-修正后才是完备的。

在 \(U_m\) 方程中，空间交换子的极端分配
\[
bT_m*U_0
\]
必须列出，并由
\[
bT_m=U_m-\sum_{q=1}^m B_q*T_{m-q}
\]
化为 \(U_m*U_0\) 加既往层项。它不要求当前 \(T_m\)。

### 3.3 “完整”当前变量表仍漏了两个低阶项

Step 45 (4.2) 的 \(T_m\) 行还应包含
\[
bT_m,
\]
来自 (T6) 的 \(r=0\)。完整的零阶当前结构应包括
\[
B_2*T_m,\qquad U_0*T_m,\qquad b*T_m,
\]
以及空间交换子中的有界 \(bG*T_m\) 修正。

类似地，(4.6) 的 \(U_m\) 行还应包含
\[
bU_m,
\]
来自 (U7) 的 \(r=0\)。在化简前还应列出
\[
bT_m*U_0,
\]
化简后并入 \(U_0*U_m\) 及既往层项。

这些遗漏均无害，因为 \(0<b\le2\)，但原表不能称为字面上的 exhaustive table。

除此以外，没有遗漏当前阶导数：

- \(T_{m+1}\)、\(U_{m+1}\) 只与 \(B_1=2\chi C_1\) 同现；
- \(C_{m+2}\) 只来自 \(B_{m+2}\) 的 \(2\chi C_{m+2}\) 部分；
- 时间交换子在 \(T_m\) 方程中最高给出 \(U_m*T_0\)，在 \(U_m\) 方程中最高给出 \(U_m*U_0\)；
- cutoff-jet 方程最高为 \(U_m*C_1\)。

---

## 4. 带符号分部积分与有限指数闭合

令
\[
V=U_m,\qquad Z=C_{m+1},\qquad P(V)=|V|^{p-2}V.
\]

### 4.1 一阶系数项

由
\[
\frac{|B_1|^2}{b}
=4\frac{\chi^2}{b}|C_1|^2
\le4|C_1|^2,
\]
所有 \(B_1*\nabla V\) 项均可被
\[
\int b|\nabla V|^2|V|^{p-2}
\]
吸收，无 \(\varepsilon^{-1}\)。

### 4.2 Hessian 项

当前 \(B_2*V\) 写成
\[
\int(\nabla_i\nabla_jb)\,\mathcal B^{ij}(V),
\]
其中
\[
|\mathcal B(V)|\le C_p|V|^p,\qquad
|\nabla\mathcal B(V)|\le C_p|V|^{p-1}|\nabla V|.
\]
先分部积分，再用 \(db=2\chi\,d\chi\)，得到
\[
\left|\int\nabla^2b*\mathcal B(V)\right|
\le \delta\int b|\nabla V|^2|V|^{p-2}
+C_{\delta,p}\|d\chi\|_\infty^2\|V\|_p^p.
\]
不需要 \(\|\nabla^2\chi\|_\infty\)。

### 4.3 顶阶 cutoff jet

一次分部积分后，
\[
\chi C_{m+2}*U_0*P(V)
\]
产生
\[
C_1*Z*U_0*P(V),\quad
\chi Z*U_1*P(V),\quad
\chi Z*U_0*\nabla P(V).
\]
最后一项经吸收后只留下
\[
|Z|^2|V|^{p-2},
\]
且
\[
\int |Z|^2|V|^{p-2}
\le \frac2p\|Z\|_p^p+\frac{p-2}{p}\|V\|_p^p.
\]

对 \(m\ge2\)，再次对 \(\chi Z*U_1*P(V)\) 分部积分，得到
\[
C_1*C_m*U_1*P(V),\quad
\chi C_m*U_2*P(V),\quad
\chi C_m*U_1*\nabla P(V),
\]
以及
\[
\nabla^q\operatorname{Rm}*C_s*U_1*P(V),\qquad q\le m-1
\]
的重排余项。后者只用既往 \(T\)-层。

在 \(m=2\) 时，\(\chi C_2*U_2*P(U_2)\) 应明确视作
\[
\int\chi\nabla^2\chi*\mathcal B(U_2)
\]
并按上述 signed-Hessian 公式再处理；这不是要求 \(C_2\in L^\infty\)。Step 45 的结论正确，但最好把这一步写出，而不是仅称其为 signed Hessian contraction。

修正后的 \((U3)\) 顶 jet 项仅为
\[
\frac{\chi^2}{b}C_1*Z*U_0*P(V),
\]
仍是同指数的 \(|Z||V|^{p-1}\) 型项。

所以当前 pair 仅出现
\[
|Z||V|^{p-1},\qquad |Z|^2|V|^{p-2},
\]
不发生当前层 \(p\mapsto2p\) 升级，得到
\[
\frac d{dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
+c_{m,p}\int b|\nabla U_m|^2|U_m|^{p-2}
\le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).
\]

### 4.4 随后的 \(T_m\) 阶段不需要 \(T_\infty\)

顶阶 cutoff 项一次分部积分后留下
\[
C_1*C_{m+1}*T_0*P(T_m),\quad
\chi C_{m+1}*T_1*P(T_m),\quad
\chi C_{m+1}*T_0*\nabla P(T_m).
\]
最后一项产生
\[
|C_{m+1}|^2|T_0|^2|T_m|^{p-2}.
\]
可由已完成层的有限高指数控制，例如
\[
\begin{aligned}
\int |C_{m+1}|^2|T_0|^2|T_m|^{p-2}
&\le C_p\|C_{m+1}T_0\|_p^p+C_p\|T_m\|_p^p\\
&\le C_p\|C_{m+1}\|_{2p}^p\|T_0\|_{2p}^p
 +C_p\|T_m\|_p^p.
\end{aligned}
\]
时间交换子 \(U_m*T_0\) 同样是有限指数 forcing，而非点态系数。

因此
\[
\frac d{dt}\|T_m\|_p^p
+c_{m,p}\int b|\nabla T_m|^2|T_m|^{p-2}
\le C_{m,p}(1+\|T_m\|_p^p).
\]

这里 \(T_m\) 阶段可以调用已经完成的 \((U_m,C_{m+1})\) 在 \(2p\) 或其他有限指数的估计；这不是当前层循环。

---

## 5. 零阶种子与 \(\varepsilon\)-一致性

零阶种子从 \(a=\chi^2\) 推广到
\[
b=\chi^2+\varepsilon^2
\]
时只需将恒等式改为不等式
\[
\frac{|\nabla b|^2}{b}
=4\frac{\chi^2}{b}|d\chi|^2
\le4|d\chi|^2.
\]
二次反应仍满足
\[
b|T|^{p+1}=|U|\,|T|^p,
\]
signed-Hessian 项仍仅用
\[
db=2\chi\,d\chi.
\]
故 \(T_0\) 的所有有限-\(L^p\) 估计对 \(0<\varepsilon\le1\) 一致。

高阶常数只使用
\[
0<b\le2,\qquad
\nabla^rb=\nabla^r(\chi^2)\ (r\ge1),\qquad
\frac{|B_1|^2}{b}\le4|C_1|^2,\qquad
\frac{\chi^2}{b}\le1.
\]
没有微分 \(b^{-1}\)，也没有负次 \(\varepsilon\)。初值的 \(U=bT\) 及其导数同样一致，因为 \(b\le2\) 且所有正阶 \(B_r\) 与 \(\varepsilon\) 无关。

---

## 最终判定

经以下修正后，Step 45 的坐标时间 tensor ledger 和交错有限-\(L^p\) 闭合成立：

1. 将
   \[
   \partial_tG
   =-\frac{S\owedge g+g\owedge S}{2(n-1)}
   \]
   改为
   \[
   \boxed{\partial_tG
   =-\frac{S\owedge g+g\owedge S}{n-1}}.
   \]

2. 在当前变量表中补入 \(bT_m\)、\(bU_m\)，并在 \(U_m\) 空间交换子中显式列出及化简 \(bT_m*U_0\)。

3. 空间交换子零阶曲率因子应写为
   \[
   b\operatorname{Rm}=U-bG,
   \]
   而不能无说明地直接以 \(bT_0\) 代替。

4. \(m=2\) 的 \(\chi C_2*U_2*P(U_2)\) 需明确按 signed-Hessian 分部积分处理。

这些修正不改变结论：正则化估计在每个 datum 的共同 bootstrap 区间上对 \(\varepsilon\) 一致，且不存在隐藏的 \(T_\infty\)、当前指数升级、\(\varepsilon^{-1}\) 或漏失的当前阶导数。

不过，固定-\(\varepsilon\) DeTurck 短时存在、共同存在时间及极限后的 restart 并非 Wang 文献或该 ledger 本身所证明；它们是 Step 45 后续正则化构造所需的独立解析输入。
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
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step43_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step43_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the H-WU resolution for the weighted cutoff flow U_m = nabla^m(chi^2(Rm+G)) under dt g = -2 chi^2 (Ric+g). The central claim (Proposition §5) is: in the evolution equation for U_m, the UNIQUE source of the single cutoff jet C_{m+2} = nabla^{m+2}chi is from the Hessian-a contraction in the Lichnerowicz variation, giving the form 2*chi*C_{m+2} * (aE) plus products of lower jets. All other terms (commutator, G-variation, normalization, reaction, outer Leibniz j>=1) produce single jets of order <= m+1. Verify: (1) The product-rule identity nabla^k(chi^2) = sum_{s=0}^k C(k,s) C_s C_{k-s} and its top jet 2*chi*C_k. (2) The factorization a*(nabla^2 a)*E = (nabla^2 a)*(aE) and why this preserves chi weight after m derivatives. (3) The commutator bound max single jet = C_m from [dt, nabla^m]U. (4) That the chi factor in 2*chi*C_{m+2} is essential for pairing with weighted dissipation int chi^2|nabla U_m|^2|U_m|^{p-2} via Cauchy-Schwarz, and that bare C_{m+2} would fail. (5) Whether any curvature-commutator correction from reordering covariant derivatives in the Leibniz expansion could introduce an unaccounted C_{m+2} term.

## Integrated Scientific Memo

# H-WU 核验结论

## 结论

所需的**权重结论成立**，但 Step 43 的“唯一来源”表述必须区分两种方程形式：

1. 对原始展开
   \[
   \partial_tU_m=\nabla^m(a\,\partial_tT)+[\partial_t,\nabla^m]U,
   \qquad a=\chi^2,
   \]
   单个最高截止喷射 \(C_{m+2}\) 的唯一来源确为曲率变分中的 Hessian-\(a\) 项。

2. 若把方程改写成用于能量估计的抛物形式
   \[
   (\partial_t-a\Delta)U_m=\cdots,
   \]
   则将 \(a^2\Delta T\) 攖写为 \(a\Delta U\) 会额外产生
   \[
   -(\Delta a)U,
   \]
   其 \(m\) 阶导数也含 \(C_{m+2}\)。因此在此形式中，“唯一来自 Hessian-\(a\) 收缩”并不字面成立。

关键且正确的最终命题是：

\[
\boxed{\text{抛物形式中所有单个 }C_{m+2}\text{ 项都具有 }
\chi C_{m+2}*\mathcal A(U)\text{ 的形式，绝无裸 }C_{m+2}*\mathcal A(U).}
\]

这里 \(\mathcal A(U)\) 是 \(U\) 的代数收缩，包括
\[
aE=\operatorname{Ric}(U),\qquad |\mathcal A(U)|\le C_n|U|.
\]

---

## 1. \(\nabla^k(\chi^2)\) 的乘积公式

对有序多指标 \(I=(i_1,\dots,i_k)\)，精确公式是 shuffle/subset Leibniz 展开：

\[
\nabla_I(\chi^2)
=
\sum_{S\subseteq\{1,\dots,k\}}
(\nabla_{I_S}\chi)\,\widetilde\otimes_S\,
(\nabla_{I_{S^c}}\chi).
\]

若采用对称化记号，可写为

\[
\nabla^k(\chi^2)
=
\sum_{s=0}^k\binom ks
\operatorname{Sym}(C_s\otimes C_{k-s}).
\]

因此源文件中的

\[
\nabla^k(\chi^2)=\sum_{s=0}^k\binom ks C_s\otimes C_{k-s}
\]

作为喷射阶数或 \(*\)-记号公式正确；若固定一个未经对称化的张量槽位排列，则不能把所有 shuffle 字面合并为同一个 \(C_s\otimes C_{k-s}\)。

两个端点分配给出

\[
C_0C_k+C_kC_0=2\chi C_k,
\]

故

\[
\boxed{
\nabla^ka
=
2\chi C_k+
\sum_{1\le s\le k-1}C_s*C_{k-s},
\qquad a=\chi^2.
}
\]

所有非端点项的每个单独截止喷射阶数至多 \(k-1\)。

---

## 2. Hessian-\(a\) 项及最高喷射的权重

记曲率变分中的 Hessian 收缩为双线性映射
\[
\mathcal H(A,E).
\]
由于 \(a\) 是标量且收缩对各槽 \(C^\infty\)-线性，

\[
a\,\mathcal H(\nabla^2a,E)
=
\mathcal H(\nabla^2a,aE).
\]

又因为
\[
\operatorname{Ric}(T)=E,\qquad U=aT,
\]
所以
\[
aE=\operatorname{Ric}(U),\qquad |aE|\le C_n|U|.
\]

在
\[
a\nabla^m\mathcal H(\nabla^2a,E)
\]
中，只有把全部 \(m\) 个外部导数置于 \(\nabla^2a\) 上，才可能得到 \(m+2\) 阶截止喷射：

\[
a\,\mathcal H(\nabla^{m+2}a,E)
=
\mathcal H(\nabla^{m+2}a,aE).
\]

利用上一节，

\[
\mathcal H(\nabla^{m+2}a,aE)
=
2\chi\,\mathcal H(C_{m+2},aE)
+
\sum_{s=1}^{m+1}
C_s*C_{m+2-s}*(aE).
\]

因此原始方程中的最高项确为

\[
\boxed{2\chi C_{m+2}*(aE).}
\]

任何外层 Leibniz 分配 \(j\ge1\) 的最大单喷射阶数为

\[
\max\{j,m-j+2\}\le m+1.
\]

---

## 3. 抛物改写产生的额外最高项

由
\[
(\partial_t-a\Delta)T
=
\mathcal H(\nabla^2a,E)
+\mathcal G(\nabla a,\nabla E)+\cdots
\]
及 \(U=aT\)，有

\[
\begin{aligned}
(\partial_t-a\Delta)U
={}&a(\partial_t-a\Delta)T
-a(\Delta a)T-2a\nabla a*\nabla T\\
={}&\mathcal H(\nabla^2a,aE)
-(\Delta a)U
-2\nabla a*\nabla U
+2\frac{|\nabla a|^2}{a}U+\cdots ,
\end{aligned}
\]
其中
\[
\frac{|\nabla a|^2}{a}=4|d\chi|^2
\]
光滑延拓至 \(\chi=0\)。

于是
\[
-\nabla^m((\Delta a)U)
\]
还包含一个最高分配

\[
-(\nabla^m\Delta a)*U
=
-2\chi\,\operatorname{tr}(C_{m+2})*U
+\text{低阶截止喷射乘积}.
\]

所以抛物形式中至少有两种张量来源：

\[
2\chi\,\mathcal H(C_{m+2},aE),
\qquad
-2\chi\,\operatorname{tr}(C_{m+2})*U.
\]

它们都属于统一结构
\[
\chi C_{m+2}*\mathcal A(U).
\]

因此应把 Proposition §5 修订为：

\[
\boxed{
(\partial_t-a\Delta)U_m
\text{ 的所有 }C_{m+2}\text{ 项均带显式 }\chi,
\text{且系数是 }U\text{ 的代数收缩。}
}
\]

---

## 4. 时间—联络交换子

对协变张量 \(U\)，

\[
[\partial_t,\nabla^m]U
=
\sum_{q=0}^{m-1}
\nabla^q(\partial_t\Gamma)*
\nabla^{m-1-q}U.
\]

在
\[
\partial_tg=-2aE
\]
下，

\[
\partial_t\Gamma=g^{-1}*\nabla(aE).
\]

因此 \(\nabla^q(\partial_t\Gamma)\) 中最大的显式截止喷射为 \(C_{q+1}\)，而
\[
\nabla^{m-1-q}U
\]
中最大的显式截止喷射为 \(C_{m-1-q}\)。故

\[
\max\{q+1,m-1-q\}\le m.
\]

结论：

\[
\boxed{
[\partial_t,\nabla^m]U
\text{ 的最大单截止喷射为 }C_m;
\text{不产生 }C_{m+1}\text{ 或 }C_{m+2}.
}
\]

也可直接写
\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
\]
此时交换子可完全按 \(U\) 的导数组织。

---

## 5. \(\chi\) 对加权耗散是必要的

令
\[
V=U_m,\qquad P(V)=|V|^{p-2}V.
\]
一个最高源项为

\[
I=\int\chi C_{m+2}*\mathcal A(U)*P(V),
\qquad |\mathcal A(U)|\le CK.
\]

从 \(C_{m+2}\) 上分部积分一次后，导数落到 \(P(V)\) 的项满足

\[
|\nabla P(V)|
\le (p-1)|V|^{p-2}|\nabla V|.
\]

故

\[
\begin{aligned}
&\int \chi |C_{m+1}|\,|\mathcal A(U)|
|V|^{p-2}|\nabla V|\\
&\quad\le
\varepsilon\int\chi^2|\nabla V|^2|V|^{p-2}
+
C_{p,\varepsilon}K^2
\int |C_{m+1}|^2|V|^{p-2}.
\end{aligned}
\]

第一项正好被

\[
D^U_{m,p}
=
\int\chi^2|\nabla U_m|^2|U_m|^{p-2}
\]

吸收。第二项只需当前耦合对的 \(L^p\) 范数：

\[
\int |C_{m+1}|^2|V|^{p-2}
\le
\|C_{m+1}\|_p^2\|V\|_p^{p-2}
\le
C\bigl(\|C_{m+1}\|_p^p+\|V\|_p^p\bigr).
\]

因此 Step 43 §6 所称“使用前一层 \(C_{m+1}\in L^{2p}\)”不正确也不需要；\(C_{m+1}\) 是当前 staggered pair 的未知量，按同指数 \(p\) 闭合。

若源项是裸的 \(C_{m+2}*\mathcal A(U)\)，Young 不等式将产生

\[
\frac{|\mathcal A(U)|^2}{\chi^2}.
\]

仅由 \(|U|\le K\) 无法控制 \(U/\chi\) 或 \((aE)/\chi\)；在 \(\chi\to0\) 的过渡区会失效。因此显式 \(\chi\) 是结构上必需的，而非记号改善。

---

## 6. 协变导数重排不会生成遗漏的 \(C_{m+2}\)

若保留导数的实际顺序，迭代 Leibniz 公式本身没有曲率修正。曲率项只在把交错导数重排为某个标准顺序时出现。

对 \(\nabla^r a\)，

\[
[\nabla_i,\nabla_j](\nabla^r a)
=
\operatorname{Rm}*\nabla^r a.
\]

在总阶 \(m+2\) 的最高项中，任一重排修正具有形式

\[
\nabla^q\operatorname{Rm}*\nabla^{r'}a,
\]
并满足微分阶守恒
\[
(q+2)+r'=m+2.
\]

故
\[
r'=m-q\le m.
\]

因此曲率交换子中的截止喷射至多为 \(C_m\)，不可能恢复 \(C_{m+2}\)，甚至不能产生新的 \(C_{m+1}\)。同理，\([\nabla^m,\Delta]U\) 只产生曲率导数乘以较低阶 \(U\) 导数，不会形成额外的 \(C_{m+2}\)。

---

## 最终核验命题

严格可支持的版本为：

\[
\boxed{
\begin{aligned}
(\partial_t-a\Delta)U_m
={}&a\Delta\text{ 已移至左侧后的低阶项}\\
&+\chi C_{m+2}*\mathcal A(U)
+\{\text{单截止喷射阶数}\le m+1\},
\end{aligned}
}
\]

其中所有 \(C_{m+2}\) 项均带显式 \(\chi\)，且
\[
|\mathcal A(U)|\le C_n|U|.
\]
时间—联络交换子仅到 \(C_m\)，曲率重排修正也不产生新的 \(C_{m+2}\)。

因此，H-WU 所需的**最高截止喷射权重结论成立**，并足以支撑 A03 Step 40 的加权耗散机制；但“抛物形式中唯一来自原始 Hessian-\(a\) 收缩”这一更强的来源唯一性应删除或限定为未经 \(a\Delta U\) 改写的原始表达。
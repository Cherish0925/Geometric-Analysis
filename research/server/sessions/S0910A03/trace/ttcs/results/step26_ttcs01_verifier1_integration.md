# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 26,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step26_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step26_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 26 mathematical development for the 4D negative-branch cutoff-flow program. The note claims to resolve two of three remaining obstacles: (1) the general-p weighted tensor inequality and (2) the initial Sobolev inequality on collapsed balls. Check specifically:

(a) Does the general-p derivation (Section 3) correctly extend the A01 q=2,3 template? In particular: is the boundary term d(eta^2 a^{p-1}) correctly handled (vanishing deta part for p>=3, Young for da part giving Cp^2 r^{-2} K_p)? Is the Hessian-a IBP at general p correct (no singular terms)? Is the dissipation constant c>0 uniform in p? Is the polynomial p-dependence on the RHS (at most p^3 after the full Young/Sobolev chain) sufficient for the infinite-product convergence?

(b) Does the Maheux-Saloff-Coste theorem (Section 1) genuinely resolve the initial Sobolev question? The claim is that for n=4, p=2, p*=4, the relative Sobolev inequality gives S = Cr^2 Vol^{-1/2} with C depending only on n and Kr^2, valid on any geodesic ball regardless of collapse. Is the passage from the mean-subtracted form to the compactly-supported form correct? Are the constants truly volume-independent?

(c) Is the corrected beta-bar definition (Section 2) consistent: does subtracting the collar from H_2 and using S on the active support give a self-consistent absorption? Does the additive constant from the collar spoil the Gronwall bound?

(d) Is the explicit J_6 propagation (Section 4) a genuine critical absorption argument, not just an appeal to homogeneity?

(e) Does the first-exit closure (Section 6) genuinely self-improve all conditions simultaneously, conditional on smooth existence?

Identify any hidden error or gap. Give corrected formulas if needed.

## Integrated Scientific Memo

# Step 26 核验结论

## 总结

Step 26 **不能按现稿认定已经完整解决 general-\(p\) 障碍及 first-exit 闭合**。主要结论如下：

1. **曲率的 general-\(p\) 权重结构基本正确**：边界项、\(\nabla^2a\) 分部积分、\(Cp^2r^{-2}K_p\) 余项以及最终 \(p^3\) 增长均可成立。
2. **缺陷张量的 general-\(p\) 证明尚未写完整**，且正则化链式法则有明确错误。
3. **Maheux–Saloff-Coste 型相对 Sobolev 不等式确实适用于塌缩球**；体积只通过显式的 \(V^{-1/2}\) 出现。不过现有材料不能独立核验所引定理的精确版本、球是否需扩大等文献细节。
4. **collar 修正按现稿不闭合**：吸收公式多出一个 \(\mathsf S^{-1}\)，而由带 \(C_{\rm col}\) 的粗 Gronwall 估计不能传播以活跃区能量定义的 \(\bar\beta\) 小量。
5. \(J_6\) 传播的机制确是临界 Sobolev 吸收，但依赖修正后的缺陷 general-\(p\) 公式和 \(\bar\beta\) 传播。
6. first-exit 的结构在已有光滑解的条件下可闭合，但必须使用修正后的活跃区 \(H_2\) 估计；现稿的 (F3a) 太弱。
7. 退化 normalized cutoff flow 的统一存在/延拓仍未证明。

---

## (a) General-\(p\) 张量不等式

### 曲率部分：结构正确，但正文需修正

令
\[
K_p=\int\eta^2a^{p-2}F^p,\qquad
Z_p=\eta a^{(p-1)/2}F^{p/2}.
\]
扩散项中的权重为
\[
wa=\eta^2a^{p-1},
\]
故
\[
d(wa)=2\eta\,d\eta\,a^{p-1}
 +(p-1)\eta^2a^{p-2}da.
\]

由于
\[
\operatorname{supp}d\eta\subset\{a=0\}^{\circ},
\]
\(d\eta\) 项确实消失。对 \(da\) 项，用
\[
\langle R,\nabla R\rangle=F\nabla F
\]
并相对于
\[
p(p-2)\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2
\]
作 Young，得到
\[
\begin{aligned}
|B_p|
&\le \varepsilon p(p-2)
 \int\eta^2a^{p-1}F^{p-2}|\nabla F|^2\\
&\quad+
C_\varepsilon\frac{p(p-1)^2}{p-2}
 \int\eta^2a^{p-3}|da|^2F^p.
\end{aligned}
\]
对 \(p\ge3\)，系数为 \(O(p^2)\)，且
\[
a^{p-3}|da|^2
=4a^{p-2}|d\chi|^2.
\]
因此余项为
\[
Cp^2r^{-2}K_p.
\]

### Hessian-\(a\) 项

代表项
\[
p\int\eta^2a^{p-2}F^{p-2}R*(\nabla^2a)*E
\]
一次分部积分后为
\[
-p\int da*\nabla\!\left(
\eta^2a^{p-2}F^{p-2}R*E
\right).
\]
其中：

- 微分落在 \(\eta\) 上时，由 \(da=0\) 于 \(\operatorname{supp}d\eta\)，该项消失；
- 微分落在 \(a^{p-2}\) 上时，出现
  \[
  p(p-2)a^{p-3}|da|^2F^p
  \le Cp^2r^{-2}a^{p-2}F^p;
  \]
- 微分落在 \(F,R,E\) 上时，由
  \[
  |E|\le CF,\qquad |\nabla E|\le C|\nabla R|
  \]
  和 Young 得到同型余项。

因此这里没有不可控的负幂。

### Step 26 式 (3.5) 的幂次错误

正确公式为
\[
\begin{aligned}
\nabla Z_p={}&
a^{(p-1)/2}F^{p/2}d\eta\\
&+\frac{p-1}{2}\eta a^{(p-3)/2}F^{p/2}da\\
&+\frac p2\eta a^{(p-1)/2}F^{p/2-1}\nabla F.
\end{aligned}
\]
故权重导数平方为
\[
a^{p-3}|da|^2F^p
=a^{p-1}\left|\frac{da}{a}\right|^2F^p,
\]
而不是现稿 (3.5) 的
\[
a^{p-2}|da/a|^2F^p.
\]
后者少了一个 \(a\)。

### 耗散常数可以统一于 \(p\)

不能仅凭
\[
\|\nabla Z_p\|_2^2\le C_p(D_p+r^{-2}K_p)
\]
宣称左端系数与 \(p\) 无关。正确理由是保留标量耗散：
\[
p(p-2)\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2.
\]
同时
\[
\|\nabla Z_p\|_2^2
\le Cp^2\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2
 +Cp^2r^{-2}K_p.
\]
因为
\[
p(p-2)\ge \frac13p^2\qquad(p\ge3),
\]
所以可得到统一的 \(c>0\)。

### 缺陷张量部分尚未完成

现稿公式
\[
\partial_t\Phi_\varepsilon
=\frac{|E|^2}{\Phi_\varepsilon}\partial_t|E|^2
\frac1{2\Phi_\varepsilon}
\]
错误。正确的是
\[
\partial_t\Phi_\varepsilon
=\frac{1}{2\Phi_\varepsilon}\partial_t|E|^2,
\qquad
\Phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2}.
\]

应直接使用
\[
\boxed{
(\partial_t-a\Delta)\Phi_\varepsilon^p
=
\frac p2\Phi_\varepsilon^{p-2}
(\partial_t-a\Delta)|E|^2
-p(p-2)a\Phi_\varepsilon^{p-4}
|\langle E,\nabla E\rangle|^2.}
\]
最后一项等于
\[
-p(p-2)a\Phi_\varepsilon^{p-2}
|\nabla\Phi_\varepsilon|^2.
\]

在 A01 式 (6.5) 中应取
\[
q=\frac p2\eta^2a^{p-2}\Phi_\varepsilon^{p-2}.
\]
展开 \(dq\) 后：

- \(da\) 项留下
  \[
  Cp^2\int\eta^2a^{p-3}|da|^2\Phi_\varepsilon^p;
  \]
- \(\nabla\Phi_\varepsilon\) 项由 \(p(p-2)\) 标量耗散吸收；
- 反应项由
  \[
  CpaF\Phi_\varepsilon^p
  \]
  控制。

极限 \(\varepsilon\to0\) 时，零阶项可用控制收敛；梯度耗散须用弱下半连续性，不能统一写成“dominated convergence”。

### 非整数幂问题

“\(\chi\) 光滑且非负，所以 \(\chi^\alpha\) 对任意实数 \(\alpha>0\) 光滑”是错误的。Moser 序列通常产生非整数指数。严格处理方式是：

- 选取在零集边界无限阶平坦的 cutoff；或
- 在 \(W^{1,\infty}\) 层面使用链式法则，并用平滑逼近。

此处能量计算主要需要一阶权重导数，第二种方案足够，但必须写明。

### \(p^3\) 与无限乘积

反应项满足
\[
\begin{aligned}
I_p
&=\int\eta^2a^{p-1}F\Phi^p\\
&\le H_3^{1/3}K_p^{1/3}K_{2p}^{1/3}\\
&\le \mathsf S^{2/3}H_3^{1/3}K_p^{1/3}
\bigl(\|\nabla Z_p\|_2^2+r^{-2}K_p\bigr)^{2/3}.
\end{aligned}
\]
因此
\[
CpI_p
\le \frac c2\|\nabla Z_p\|_2^2
 +Cp^3(\mathsf S^2H_3+r^{-2})K_p.
\]
对 \(p_j=p_0(3/2)^j\)，
\[
\sum_j\frac{\log(Cp_j^34^j)}{p_j}<\infty.
\]
所以 \(p^3\) 完全足够；事实上任意固定次数的多项式增长都不影响乘积收敛。

---

## (b) 塌缩球上的初始 Sobolev 不等式

以笔记所陈述的 Maheux–Saloff-Coste 定理为前提，该推导正确。四维 \(p=2,p^*=4\) 时，
\[
\|u-u_B\|_4
\le C(4,Kr^2)\,r\,V^{-1/4}\|\nabla u\|_2.
\]
又由 Hölder，
\[
\|u_B\|_{L^4(B_r)}
=V^{1/4}|u_B|
\le V^{-1/4}\|u\|_2.
\]
故
\[
\boxed{
\|u\|_4^2
\le C(4,Kr^2)\,r^2V^{-1/2}
\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right).}
\]

这里 \(C(4,Kr^2)\) 与体积无关；塌缩只体现在显式因子
\[
V^{-1/2}.
\]
因此这一形式不需要非塌缩假设。

但当前材料未包含原论文，故无法从所给文件独立核验定理号、是否使用扩大球或梯度积分区域等精确文献细节。若原定理右端使用 \(B_{2r}\)，通常可通过零延拓和体积比较恢复同型估计，只改变 \(C(4,Kr^2)\)，但该细节仍应对原文核准。

---

## (c) \(\bar\beta\) 与 collar

定义
\[
\widehat H_2=H_2-C_{\rm col}
\]
本身合理，因为在 \(a=0\) 的开 collar 上 \(g,F,d\mu\) 均静止。

但现稿吸收式错误。正确的是
\[
\begin{aligned}
\int\eta^2aF^3
&\le \|F\|_{L^2(\operatorname{supp}\chi)}
 \|\chi F\|_4^2\\
&\le \frac{\bar\beta}{\mathsf S}\,
\mathsf S(D_2+r^{-2}\widehat H_2)\\
&=\boxed{\bar\beta(D_2+r^{-2}\widehat H_2)}.
\end{aligned}
\]
Step 26 式 (2.4) 多写了 \(\mathsf S^{-1}\)。Section 4 的 \(J_6\) 吸收也有同样错误。

更重要的是，若保留粗估计
\[
\widehat H_2'
\le Cr^{-2}(\widehat H_2+C_{\rm col}),
\]
则只能得到
\[
\widehat H_2(t)
\le e^{Ct/r^2}\widehat H_2(0)
 +(e^{Ct/r^2}-1)C_{\rm col}.
\]
这不能推出
\[
\bar\beta(t)\lesssim\bar\beta(0)
\]
，除非另证
\[
C_{\rm col}\lesssim\widehat H_2(0)
\quad\text{或}\quad
\mathsf S\sqrt{C_{\rm col}}\ll1.
\]
现稿的 \(H_2(0)\le CV\) 没有根据；Ricci 夹逼不控制 Weyl 能量，尤其不能在塌缩球上给出这种曲率能量—体积估计。

最直接的修复来自 A01 能量推导本身：所有 cutoff 余项都含 \(a\)、\(da\) 或 \(|da|^2/a\)，实际支撑在活跃区。因此应保留支撑信息并写成
\[
\boxed{
\widehat H_2'+cD_2
\le C\int\eta^2aF^3
 +Cr^{-2}\widehat H_2.}
\]
吸收后得到
\[
\widehat H_2(t)
\le e^{Ct/r^2}\widehat H_2(0),
\]
从而
\[
\bar\beta(t)
\le
\frac{\mathsf S(t)}{\mathsf S(0)}
e^{Ct/(2r^2)}\bar\beta(0).
\]

另一种修复是额外证明 maximal-function good region 控制整个 buffer 的初始能量，使
\[
\mathsf S\sqrt{C_{\rm col}}
\]
本身小；但该选取引理不在现有材料中。活跃区版本不需要这一额外输入。

需要注意集合边界：严格地说，应将活跃区写成 \(\{a>0\}\) 或固定开邻域，并利用积分不受零测边界影响，而不应依赖不同文献对 \(\operatorname{supp}\chi\) 的约定。

---

## (d) \(J_6\) 是真正的临界吸收

在缺陷 general-\(p\) 公式补齐后，\(p=6\) 给出
\[
J_6'+c\|\nabla Z_6\|_2^2
\le Cr^{-2}J_6
+C\int\eta^2a^5F|E|^6,
\]
其中
\[
Z_6=\eta a^{5/2}|E|^3.
\]
而
\[
\begin{aligned}
\int\eta^2a^5F|E|^6
&=\int F|Z_6|^2\\
&\le \|F\|_{L^2(\{a>0\})}\|Z_6\|_4^2\\
&\le
\bar\beta\left(
\|\nabla Z_6\|_2^2+r^{-2}J_6\right).
\end{aligned}
\]
当 \(C\bar\beta<c/2\) 时，
\[
J_6'+\frac c2\|\nabla Z_6\|_2^2
\le Cr^{-2}J_6,
\]
所以
\[
J_6(t)\le e^{Ct/r^2}J_6(0).
\]
这确实是四维临界 \(L^2\)-势吸收，不是仅凭齐次性。

体积符号应区分：
\[
V_B=\operatorname{Vol}(B_r),\qquad
V_\eta=\operatorname{Vol}(\operatorname{supp}\eta)\le V_B.
\]
于是
\[
J_6(0)\le C\delta^6V_\eta,\qquad
\mathsf S\le Cr^2V_B^{-1/2},
\]
最终
\[
\|aE(t)\|_\infty
\le
C\delta\left(\frac{r^2}{t}\right)^{1/3}
\left(\frac{V_\eta}{V_B}\right)^{1/6}
\le
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]

---

## (e) First-exit 闭合

使用修正后的活跃区估计后，conditional first-exit 结构成立：

\[
\int_0^{\theta r^2}\|aE(s)\|_\infty\,ds
\le C\delta\theta^{2/3}r^2,
\]
故
\[
e^{-2I(t)}g_0\le g(t)\le e^{2I(t)}g_0.
\]
由固定区域上的范数比较，
\[
\mathsf S(t)\le e^{CI(t)}\mathsf S(0),
\qquad
|d\chi|_{g(t)}\le e^{I(t)}|d\chi|_{g_0}.
\]
同时
\[
\bar\beta(t)
\le e^{CI(t)+C\theta}\bar\beta(0),
\]
从而同一个 \(\bar\beta\) 小量可吸收 \(H_2,Q,J_6\) 的临界势项。

(F3a) 应改成
\[
\boxed{\widehat H_2(t)\le2\widehat H_2(0)}
\]
而不是
\[
\widehat H_2(t)\le2H_2(0).
\]
后者不能确保活跃区临界小量自改善。

此外，“指数映射保持 \(C^0\)-接近”不能仅由双 Lipschitz 度量比较推出。此处只需距离比较
\[
e^{-I}d_{g_0}\le d_{g(t)}\le e^Id_{g_0},
\]
以获得固定球之间的包含；指数映射的比较需连接或曲率导数控制，应留到正时间 plateau 正则化之后。

因此：**在假设平滑解已存在于所考察区间的条件下，并采用上述修正公式，所有 first-exit 条件可以同时严格改善。** 但 Step 26 尚未证明退化 normalized cutoff flow 存在到统一时间；该延拓问题仍是实质性未解环节，不能仅称为“lower-order structural exercise”。
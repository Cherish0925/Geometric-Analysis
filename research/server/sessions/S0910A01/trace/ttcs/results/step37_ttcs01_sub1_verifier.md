# TTCS Independent Branch Record

```json
{
  "step_id": 37,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step37_continuation_theorem_and_first_exit.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Verify the shifted continuation theorem (Theorem 1.1) and first-exit closure (Section 3) in the Step 37 note. The central claim is: if sup|U| = sup|chi^2(Rm+G)| is bounded on [tau, T_max) for some tau > 0, then the smooth degenerate flow dt g = -2 chi^2(Ric+g) extends past T_max. The proof adapts Wang's staggered induction (Lemma 4.10, Remark 4.2) to the normalized shifted variable. Check specifically:

1. L^p(Rm) propagation (Lemma 1.2): Is the reaction term correctly bounded by (K+C) int|Rm|^p using a|Rm|^{p+1} <= |aRm||Rm|^p <= (|U|+C)|Rm|^p? Does the signed IBP (0.4) correctly absorb the Hessian-a term into the degenerate diffusion int a|nabla Rm|^2|Rm|^{p-2}? Are there any terms where the degenerate weight 'a' in the diffusion is insufficient to absorb the cutoff terms?

2. Staggered induction: Does the Wang triple (nabla^m U, nabla^{m-1} Rm, nabla^m chi) correctly generalize to the normalized equation? At level m=1, does the base-pair Y_1 Gronwall use L^p(Rm) from level 0? At higher levels, does the signed IBP handle all chi nabla^2 chi * nabla^m U terms, and does the top-jet integration by parts correctly reduce nabla^{m+2} chi to the current-level coupled pair?

3. First-exit closure (Section 3.2): The Moser endpoint ||aF(t)||_inf <= C gamma/t gives K(tau) = C gamma/tau < inf for tau > 0. Does the continuation theorem then extend the flow past T*? Does the energy self-improvement (K_2 Gronwall) and metric drift (delta theta^{2/3} r^2) correctly give strict improvement of (F1)-(F3)? Is the contradiction at T* logically complete?

4. Are there any hidden inputs not stated as hypotheses, any circularity between the continuation theorem and the first-exit quantities, or any terms in the staggered induction that require unweighted sup|Rm| (which would be circular)?

## Output

# 科学复核备忘录

## 总体结论

Section 3 的首次退出逻辑在以下前提下可以闭合：

1. 归一化退化流对每个光滑初值都有短时光滑解；
2. Theorem 1.1 的续接定理已经严格证明；
3. Step 34–35 与 A03 Step 38 的 \(K_2\)、\(J_6\) 和 Moser 估计在光滑首次退出区间上成立。

其中，首次退出推理本身基本正确，只需修正 \(r\) 尺度和最大存在时间的表述。真正尚未由 Step 37 证明的是 Theorem 1.1 的高阶 staggered induction。零阶 \(L^p(\mathrm{Rm})\) 传播可以修补；高阶部分目前只有结构性说明，没有给出足以推出 (1.21) 的指数安排和无权曲率导数估计。A03 Step 38 §3 也明确指出同一缺口。

---

## 1. \(L^p(\mathrm{Rm})\) 传播

### 1.1 反应项估计正确

由
\[
U=a(\operatorname{Rm}+G),\qquad a\operatorname{Rm}=U-aG
\]
以及 \(|G|_g=C_4\)，有
\[
|a\operatorname{Rm}|\le |U|+C.
\]
因此 Hamilton 二次项满足
\[
a|\operatorname{Rm}|^{p+1}
\le |a\operatorname{Rm}|\,|\operatorname{Rm}|^p
\le (K+C)|\operatorname{Rm}|^p.
\]
同样，
\[
|aE|=|\operatorname{Ric}(U)|\le C|U|\le CK,
\]
所以体积形式变化和逆度量变化都只贡献
\[
C_p(K+1)\int |\operatorname{Rm}|^p.
\]
这部分没有使用无权 \(\sup|\operatorname{Rm}|\)。

### 1.2 度量等价需要改用对数微分

(1.2) 以 \(|g(t)-g(\tau)|\) 直接积分并不够严谨，因为范数本身随时间变化。正确写法是对任意固定非零切向量 \(v\)：
\[
\left|\frac{d}{dt}\log g_t(v,v)\right|
 =2\frac{|aE(v,v)|}{g_t(v,v)}
 \le C_4K.
\]
于是
\[
e^{-C_4K(t-\tau)}g(\tau)
 \le g(t)\le
e^{C_4K(t-\tau)}g(\tau).
\]
这确实给出 \([\tau,T_{\max})\) 上的双 Lipschitz 等价、体积控制、\(|d\chi|_{g(t)}\) 控制和标量 Sobolev 常数控制。

### 1.3 Hessian-\(a\) 项在 Step 37 中写错了一层张量因子

Step 35 的指标公式 (2.7) 表明曲率方程中的该项是
\[
\nabla^2a*E,
\]
而不是 (1.4) 所写的
\[
\nabla^2a*\operatorname{Rm}*E.
\]
测试后得到
\[
\int \nabla^2a*E*\operatorname{Rm}\,
 |\operatorname{Rm}|^{p-2}.
\]

Step 37 随后取
\[
B\sim E*\operatorname{Rm}|\operatorname{Rm}|^{p-2}
\]
是与正确曲率方程相符的，但
\[
|B|\le C|\operatorname{Rm}|^p
\]
并不成立于 \(|\operatorname{Rm}|\) 很小时，因为 \(E=\operatorname{Ric}+g\) 含有 \(g\) 项。应拆成两部分：

\[
B=B_{\operatorname{Ric}}+B_g.
\]

对于 Ricci 部分，
\[
|B_{\operatorname{Ric}}|\le C|\operatorname{Rm}|^p,\qquad
|\nabla B_{\operatorname{Ric}}|
 \le C|\operatorname{Rm}|^{p-1}|\nabla\operatorname{Rm}|,
\]
所以 (0.4) 可直接使用。

对于 \(g\) 部分，
\[
|B_g|\le C|\operatorname{Rm}|^{p-1},\qquad
|\nabla B_g|
 \le C|\operatorname{Rm}|^{p-2}|\nabla\operatorname{Rm}|.
\]
由
\[
\nabla^2a=2\chi\nabla^2\chi+2\,d\chi\otimes d\chi
\]
并对 \(\chi\nabla^2\chi\) 作一次分部积分，可得
\[
|J_g|
\le \varepsilon
 \int a|\nabla\operatorname{Rm}|^2|\operatorname{Rm}|^{p-2}
 +C_{\varepsilon,p}\|d\chi\|_\infty^2
 \int\bigl(1+|\operatorname{Rm}|^p\bigr).
\]
这里用到
\[
|\operatorname{Rm}|^{p-2}\le 1+|\operatorname{Rm}|^p.
\]
张量范数在零点处可用
\((\epsilon+|\operatorname{Rm}|^2)^{1/2}\) 正则化后令 \(\epsilon\downarrow0\)。

因此，(0.4) 不能按 Step 37 当前文字直接用于整个 \(E\) 项，但修正后仍可得到
\[
\frac{d}{dt}\int|\operatorname{Rm}|^p
+c_p\int a|\nabla\operatorname{Rm}|^2|\operatorname{Rm}|^{p-2}
\le
C_p(K+1+r^{-2})\int|\operatorname{Rm}|^p+C_p.
\]
退化权重 \(a\) 本身足够：所有一阶 cutoff 项都利用
\[
|da|^2\le4a|d\chi|^2,
\]
而 Hessian 项经有符号分部积分后也产生一个 \(\chi\)，正好与退化耗散匹配。

---

## 2. Staggered induction

### 2.1 归一化 shift 不改变最高空间微分阶数

结构上，Wang 的层级可以推广。原因是

\[
G=\frac{g\owedge g}{6},\qquad \nabla G=0,
\]
而 \(\partial_tG\) 仅代数依赖于 \(aE=\operatorname{Ric}(U)\)。因此 shift 和 \(-2ag\) 产生的都是当前层或更低层项，不引入比未归一化局部 Ricci 流更高的空间导数。

此外，
\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)
\]
是正确的，从而
\[
\partial_t\nabla^2\chi
=g^{-1}*\nabla U*d\chi
\]
也是正确的。由 \(|aE|\le CK\)，范数和体积变化只给出 \(C(K)\) 系数，所以 (1.13) 的结构可信。

### 2.2 当前的 level \(m=1\) 方程存在内部不一致

Wang Lemma 4.5 对应的高 cutoff 行使用
\[
\nabla^k(\chi^2\operatorname{Rm}),
\]
在 shifted 变量中应主要写成 \(\nabla^kU\)，外加 shift 产生的低阶项。

Step 37 的 (1.14) 却写成
\[
\sum\nabla^i\chi*\nabla^j\chi*\nabla^k\operatorname{Rm},
\]
并随后说
\[
\chi\nabla^3\chi*\operatorname{Rm}
\]
分部积分后产生 \(\nabla^2\chi*\nabla\operatorname{Rm}\)。但 Step B 只给出了无权 \(\operatorname{Rm}\) 的 \(L^p\) 控制，没有给出 \(\nabla\operatorname{Rm}\) 控制；(1.15) 中也没有保留这一项。

若正确的顶层因子是 \(U\)，分部积分后出现的是 \(\nabla U\)，可以与 base pair 配合。若确实出现无权 \(\nabla\operatorname{Rm}\)，则必须先建立相应的无权导数估计。当前文字没有解决这个二选一问题，因此 (1.15) 尚未从 (1.14) 推出。

### 2.3 高阶归纳缺少 Wang Proposition 4.13 的对应模块

Wang 的完整顺序实际包含三个不同估计：

1. 由较低阶 \(U\) 导数控制 cutoff jets；
2. 由 cutoff jets 控制无权 \(\nabla^{m-1}\operatorname{Rm}\)；
3. 再控制当前的 \(\nabla^mU\)。

具体地，在已知前一层
\[
\nabla^{m-1}U,\qquad \nabla^m\chi
\]
后，应先证明
\[
\|\nabla^{m-1}\operatorname{Rm}\|_{L^q}<\infty
\]
的归一化版本；这对应 Wang Proposition 4.13。然后才估计耦合对
\[
\bigl(\nabla^mU,\nabla^{m+1}\chi\bigr).
\]

Step 37 虽在表格中提到无权曲率导数，但在 \(Y_m\) 的推导中没有建立它，也没有展示它如何进入 (1.17) 后被前层量控制。因此
\[
Y_m'\le C(Y_m+C_{m-1})+C
\]
目前不是已推导的不等式。

### 2.4 有符号 Hessian 引理只处理一类当前层项

引理 (0.4) 确实处理
\[
\chi\nabla^2\chi*\nabla^mU
\]
测试后形成的有符号收缩。但最高 cutoff jet
\[
\chi\nabla^{m+2}\chi*U
\]
分部积分后还会产生
\[
\nabla^{m+1}\chi*\nabla U*
 |\nabla^mU|^{p-1}
\]
及类似项。它们需要：

- 前层 \(U\)、无权曲率和 cutoff jets 的一组有限 \(L^q\) 估计；
- 明确的 Hölder 指数分配；
- 当前 \(\nabla^mU\) 与 \(\nabla^{m+1}\chi\) 的耦合 Gronwall；
- 对 \(m=2\) 的单独指数安排。

A03 Step 38 §3 正是指出这些 top-jet/lower-curvature 耦合尚未写完。因而“\(\Gamma_2,\Gamma_3\) are paid by the coupled cutoff-jet equation”还不足以推出 (1.21)。

### 2.5 无权 \(\sup|\operatorname{Rm}|\) 并非理论上必需

正确的 Wang 型路径只需要：

- \(\sup|U|\)，用来控制所有 \(a\operatorname{Rm}\) 顶阶反应项；
- 无权 \(\nabla^j\operatorname{Rm}\) 的有限 \(L^q\) 矩；
- 前层 \(U\) 和 cutoff jets 的有限 \(L^q\) 矩。

因此不必引入无权 \(\sup|\operatorname{Rm}|\)。但 Step 37 将许多乘积统称为 “lower”，没有给出指数安排，尚不能排除其估计中暗中使用了无权点态曲率。

---

## 3. 从高阶估计到续接

若已经证明所有
\[
\sup_{[\tau,T_{\max})}|\nabla^mU|<\infty,
\]
则 Wang Proposition 4.3 的 shifted 版本应当成立，因为
\[
\partial_tg=-2\operatorname{Ric}(U),\qquad
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
\]
更高连接导数也由更高 \(U\) 导数控制。这样 \(g(t)\) 在固定坐标中平滑收敛到 \(g(T_{\max})\)。

Step 37 只说在 \(a\ge a_0\) 的区域恢复 \(\nabla^m\operatorname{Rm}\)，这不是续接所需的核心陈述。真正有用的是“所有 \(\nabla^mU\) 点态有界直接控制所有时间导数和连接导数”的 shifted extension proposition。

此外，从终端光滑度量重新启动流仍依赖归一化 transported-coefficient DeTurck 短时存在定理。Step 36 §1 明确说 Yang 型 tame energy estimates 尚未在材料中重写；归一化项虽只是低阶项，但当前文件并没有完整证明这一存在定理。

---

## 4. 首次退出闭合

### 4.1 正时间片上的 \(U\) 确实有界

应直接写成
\[
|U|
\le a|\operatorname{Rm}|+a|G|
\le aF+C
\le \frac{C\gamma}{t}+C.
\]
因此对任意 \(\tau>0\)，
\[
\sup_{M\times[\tau,T^*)}|U|
\le \frac{C\gamma}{\tau}+C<\infty.
\]
Step 37 中
\[
\sup |a|\,\sup|T|
\]
这一中间表达式不可用，因为 \(\sup|T|\) 可能无限增大而 \(aT\) 仍有界；上述逐点不等式修正了这一点。

若 \(T^*\) 正好是最大光滑存在时间，则 Theorem 1.1 会给出越过 \(T^*\) 的续接。若原解本来已存在到 \(T^*+\varepsilon\)，则无需使用续接定理。这个二分应在文字中明确。

### 4.2 \(F1\) 的指数需要保留归一化尺度

由归一化流中的 \(+1\) 反应项，一般应写
\[
K_2(t)\le
e^{C(1+r^{-2})t}K_2(0).
\]
在 \(t\le\theta r^2\) 上为
\[
K_2(t)\le
e^{C\theta(1+r^2)}K_2(0).
\]
只有在额外假定 \(r\le1\)，或 \(r\) 固定且有统一上界时，才能简写为 \(e^{C\theta}\)。在此修正后，选择
\[
e^{C\theta(1+r^2)}<2
\]
便得到 \(F1\) 的严格余量。

### 4.3 度量漂移计算正确

由
\[
\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3}
\]
可得
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta r^{2/3}(\theta r^2)^{2/3}
=C\delta\theta^{2/3}r^2.
\]
因此正确的度量比较是
\[
e^{-CD}g_0\le g(t)\le e^{CD}g_0,
\qquad
D=C\delta\theta^{2/3}r^2.
\]
当 \(D\) 足够小时，\(F3\) 有严格余量，局部 Sobolev 常数也满足
\[
\frac{\mathcal S(t)}{\mathcal S(0)}
\le e^{C_4D}.
\]

结合 \(K_2\) 传播，
\[
\frac{\gamma(t)}{\gamma(0)}
\le
\exp\!\left(
C_4D+\frac C2\theta(1+r^2)
\right).
\]
让右侧严格小于 \(2\)，即可得到 \(F2\) 的严格余量。仅写
“\(\mathcal S(t)=(1+o(1))\mathcal S(0)\)”表达了正确机制，但上述定量形式更适合首次退出论证。

### 4.4 反证步骤在连续性层面完整

一旦解已续接到 \(T^*+\varepsilon\)，则 \(K_2(t)\)、\(\gamma(t)\) 和度量比较量都连续到 \(T^*\)。若三者在 \(T^*\) 均严格位于退出阈值之内，它们在稍长区间上仍满足 \(F1\)–\(F3\)，与 \(T^*\) 的定义矛盾。因此，在续接定理和尺度修正成立时，
\[
T^*=\theta r^2.
\]

---

## 5. 依赖关系与当前数学状态

抽象依赖关系没有循环：

\[
\text{每个初值的短时存在}
\longrightarrow
\text{光滑首次退出区间}
\longrightarrow
\text{条件能量/Moser 估计}
\longrightarrow
\sup_{[\tau,T^*)}|U|<\infty
\longrightarrow
\text{每个初值的续接}
\longrightarrow
\text{严格自改进}.
\]

续接常数可以依赖 \(g(\tau),\chi,\tau\)，不会反馈进入序列统一的 Moser 常数。

当前文件中仍缺少的具体数学材料是：

1. shifted \(U\) 方程的完整高阶公式，特别是 (1.14) 中 \(U\) 与无权 \(\operatorname{Rm}\) 的正确分配；
2. Wang Proposition 4.13 的归一化对应版本，即无权 \(\nabla^{m-1}\operatorname{Rm}\) 的 \(L^q\) 传播；
3. top cutoff jets 与较低曲率导数乘积的 Hölder 指数安排；
4. shifted Proposition 4.3 的平滑终端度量论证；
5. 归一化 transported DeTurck 短时存在定理；
6. 若要求 \(\theta\) 与 \(r\) 无关，则需明确 \(r\le1\) 或将时间改为 \(c\min\{r^2,1\}\)。

因此，反应项和首次退出机制基本成立，Hessian-\(a\) 零阶估计可修补；但 Step 37 现有文字尚未独立证明 Theorem 1.1，高阶 staggered induction 是决定性的未写部分。
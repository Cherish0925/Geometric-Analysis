# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 37,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step37_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step37_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the shifted continuation theorem (Theorem 1.1) and first-exit closure (Section 3) in the Step 37 note. The central claim is: if sup|U| = sup|chi^2(Rm+G)| is bounded on [tau, T_max) for some tau > 0, then the smooth degenerate flow dt g = -2 chi^2(Ric+g) extends past T_max. The proof adapts Wang's staggered induction (Lemma 4.10, Remark 4.2) to the normalized shifted variable. Check specifically:

1. L^p(Rm) propagation (Lemma 1.2): Is the reaction term correctly bounded by (K+C) int|Rm|^p using a|Rm|^{p+1} <= |aRm||Rm|^p <= (|U|+C)|Rm|^p? Does the signed IBP (0.4) correctly absorb the Hessian-a term into the degenerate diffusion int a|nabla Rm|^2|Rm|^{p-2}? Are there any terms where the degenerate weight 'a' in the diffusion is insufficient to absorb the cutoff terms?

2. Staggered induction: Does the Wang triple (nabla^m U, nabla^{m-1} Rm, nabla^m chi) correctly generalize to the normalized equation? At level m=1, does the base-pair Y_1 Gronwall use L^p(Rm) from level 0? At higher levels, does the signed IBP handle all chi nabla^2 chi * nabla^m U terms, and does the top-jet integration by parts correctly reduce nabla^{m+2} chi to the current-level coupled pair?

3. First-exit closure (Section 3.2): The Moser endpoint ||aF(t)||_inf <= C gamma/t gives K(tau) = C gamma/tau < inf for tau > 0. Does the continuation theorem then extend the flow past T*? Does the energy self-improvement (K_2 Gronwall) and metric drift (delta theta^{2/3} r^2) correctly give strict improvement of (F1)-(F3)? Is the contradiction at T* logically complete?

4. Are there any hidden inputs not stated as hypotheses, any circularity between the continuation theorem and the first-exit quantities, or any terms in the staggered induction that require unweighted sup|Rm| (which would be circular)?

## Integrated Scientific Memo

# 核验结论

**Step 37 当前尚未证明 Theorem 1.1。**  
零阶无权 \(L^p(\mathrm{Rm})\) 传播可经小修正成立；首次退出论证在续接定理、短时存在及条件 Moser 端点成立的前提下逻辑闭合。决定性缺口是 \(m\ge2\) 的 Wang 型交错高阶归纳：文中没有建立无权曲率导数模块，也没有给出最高 cutoff jet 项的 Hölder 指数安排，因而 (1.21) 不能由现有文字推出。

---

## 1. Lemma 1.2：可修复，但当前写法有两处错误

### 1.1 反应项正确

由
\[
U=a(\mathrm{Rm}+G),\qquad a\mathrm{Rm}=U-aG,
\]
且 \(|G|_g=C_4\)，
\[
|a\mathrm{Rm}|\le |U|+C.
\]
故
\[
a|\mathrm{Rm}|^{p+1}
=(a|\mathrm{Rm}|)|\mathrm{Rm}|^p
\le (K+C)|\mathrm{Rm}|^p.
\]
体积及逆度量变化也只需
\[
|aE|=|\operatorname{Ric}(U)|\le C|U|\le CK.
\]
这里不需要无权 \(\sup|\mathrm{Rm}|\)。

### 1.2 度量等价应使用对数估计

(1.2) 直接积分随时间变化的张量范数并不严谨。对固定 \(v\ne0\)，应写
\[
\left|\frac d{dt}\log g_t(v,v)\right|
=\frac{2|aE(v,v)|}{g_t(v,v)}
\le CK,
\]
从而
\[
e^{-CK(t-\tau)}g(\tau)\le g(t)\le e^{CK(t-\tau)}g(\tau).
\]
这足以统一控制体积、\(|d\chi|_{g(t)}\) 和 Sobolev 常数。

### 1.3 Hessian-\(a\) 项需要拆分

Step 35 的指标公式给出曲率方程中的项是
\[
\nabla^2a*E,
\]
不是 (1.4) 所写的 \(\nabla^2a*\mathrm{Rm}*E\)。测试后才得到
\[
\nabla^2a*E*\mathrm{Rm}|\mathrm{Rm}|^{p-2}.
\]

更重要的是，Step 37 声称整个相应 \(B\) 满足
\[
|B|\lesssim |\mathrm{Rm}|^p
\]
不正确，因为 \(E=\mathrm{Ric}+g\) 的 \(g\)-部分仅给出
\[
|B_g|\lesssim |\mathrm{Rm}|^{p-1}.
\]
应拆成 \(E=\mathrm{Ric}+g\)：

- Ricci 部分满足
  \[
  |B_{\mathrm{Ric}}|\lesssim |\mathrm{Rm}|^p,\qquad
  |\nabla B_{\mathrm{Ric}}|
  \lesssim |\mathrm{Rm}|^{p-1}|\nabla\mathrm{Rm}|;
  \]
- \(g\)-部分满足
  \[
  |B_g|\lesssim |\mathrm{Rm}|^{p-1},\qquad
  |\nabla B_g|
  \lesssim |\mathrm{Rm}|^{p-2}|\nabla\mathrm{Rm}|.
  \]

利用
\[
\nabla^2a=2\chi\nabla^2\chi+2\,d\chi\otimes d\chi
\]
以及有符号分部积分，第二部分仍可估计为
\[
|J_g|
\le \varepsilon\int a|\nabla\mathrm{Rm}|^2|\mathrm{Rm}|^{p-2}
 +C_{\varepsilon,p}\|d\chi\|_\infty^2
   \int(1+|\mathrm{Rm}|^p).
\]
在 \(\mathrm{Rm}=0\) 附近可用
\((|\mathrm{Rm}|^2+\epsilon)^{1/2}\) 正则化。

其余 cutoff 项确实由退化耗散吸收，因为
\[
|da|^2=4a|d\chi|^2.
\]
因此修正后的结论是
\[
\frac d{dt}\int|\mathrm{Rm}|^p
+c_p\int a|\nabla\mathrm{Rm}|^2|\mathrm{Rm}|^{p-2}
\le C_p(K+1+\|d\chi\|_\infty^2)
 \int|\mathrm{Rm}|^p+C_p.
\]
故 Lemma 1.2 的结论成立，但 (1.4)、(1.8) 的当前论证不能原样接受。

---

## 2. 交错归纳：结构正确，证明未完成

### 2.1 shift 不引入新的最高阶导数

因为
\[
G=\frac{g\owedge g}{6},\qquad \nabla G=0,
\]
归一化和 shift 只产生当前阶或低阶代数项。并且
\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
\]
所以
\[
\partial_t\nabla^2\chi=g^{-1}*\nabla U*d\chi.
\]
因此 Wang 的三重结构原则上可推广为
\[
\nabla^mU,\qquad \nabla^{m-1}\mathrm{Rm},\qquad \nabla^m\chi.
\]

### 2.2 \(m=1\) 的现有公式内部不一致

Wang Lemma 4.5 的高 cutoff 行应主要含
\[
\nabla^k(\chi^2\mathrm{Rm}),
\]
shift 后应写成 \(\nabla^kU\) 加低阶 shift 项。Step 37 的 (1.14) 却写成
\[
\sum\nabla^i\chi*\nabla^j\chi*\nabla^k\mathrm{Rm},
\]
然后把
\[
\chi\nabla^3\chi*\mathrm{Rm}
\]
分部积分为含无权 \(\nabla\mathrm{Rm}\) 的项，但 Step B 并未控制它，(1.15) 也没有保留该项。

因此必须二选一并明确证明：

1. 正确展开后顶层因子其实是 \(U\)，分部积分只产生当前对中的 \(\nabla U\)；或
2. 确实出现无权 \(\nabla\mathrm{Rm}\)，则须先建立其 \(L^q\) 估计。

当前文字尚未推出 (1.15)。有符号 Hessian 引理修复了
\(\chi\nabla^2\chi*\nabla U\) 型项，但不自动解决上述分配问题。

### 2.3 高阶缺少 Wang Proposition 4.13 的 shifted 对应物

完整顺序必须是：

1. 由前层 \(U\) 导数控制 cutoff jets；
2. 由 cutoff jets 和前层量证明
   \[
   \|\nabla^{m-1}\mathrm{Rm}\|_{L^q}<\infty;
   \]
3. 再估计当前耦合对
   \[
   (\nabla^mU,\nabla^{m+1}\chi).
   \]

Step 37 的表格提到第 2 项，但 \(Y_m\) 推导完全没有建立它。这正是 Wang Proposition 4.13 在原证明中的作用。

### 2.4 最高 cutoff jet 项尚未闭合

对
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U
\]
分部积分会产生诸如
\[
\nabla^{m+1}\chi*\nabla U*
|\nabla^mU|^{p-1}
\]
以及含 \(\nabla^{m+1}U\) 的项。后者可由耗散吸收，但 Young 后会留下例如
\[
\int |\nabla^{m+1}\chi|^2|U|^2
|\nabla^mU|^{p-2}.
\]
同样，\(\Gamma_3\) 的后代和交换子可能含较低阶无权
\(\nabla^jT\)。

要得到 (1.21)，必须给出：

- 前层 \(U,T,\chi\) 的有限 \(L^q\) 指数族；
- 每个乘积的 Hölder 指数安排；
- 当前 \(\nabla^mU\) 与 \(\nabla^{m+1}\chi\) 的耦合估计；
- 尤其 \(m=2\) 的基始指数安排。

有符号引理 (0.4) 只解决
\[
\chi\nabla^2\chi*B(\nabla^mU)
\]
这一类当前 Hessian 项；它不证明上述 top-jet/lower-curvature 耦合。A03 Step 38 §3 明确记录了同一缺口。

所以
\[
Y_m'\le C(Y_m+C_{m-1})+C
\]
目前只是目标不等式，不是已证明结果。

---

## 3. 续接终步的正确表述

不应以“在 \(a\ge a_0\) 处恢复所有 \(\nabla^m\mathrm{Rm}\)”作为续接核心；过渡区中不能统一除以 \(a\)。

真正需要证明的是 shifted Wang Proposition 4.3：

> 若所有 \(\nabla^mU\) 一致有界，则由
> \[
> \partial_tg=-2\operatorname{Ric}(U),\qquad
> \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)
> \]
> 及其高阶版本，得到 \(g(t)\) 在固定坐标中平滑收敛到正定光滑极限，并从该极限重新启动。

归一化项是低阶的，预期不破坏该论证，但 Step 37 没有写出 shifted 版本。此外，从终端度量重新启动仍依赖归一化 transported-DeTurck 短时存在定理；Step 36 明确说明该定理的 Yang 型退化 tame estimates 尚未证明。

---

## 4. 首次退出论证：条件成立时闭合

### 4.1 正时间片上的 \(U\) 有界

应直接逐点写
\[
|U|\le a|\mathrm{Rm}|+a|G|
\le aF+C
\le \frac{C\gamma}{t}+C.
\]
不要写成 \(\sup a\,\sup T\)，因为无权 \(\sup|T|\) 可能发散。因此
\[
\sup_{M\times[\tau,T^*)}|U|
\le \frac{C\gamma}{\tau}+C<\infty.
\]

若 \(T^*\) 是最大光滑存在时间，则 Theorem 1.1 给出越过 \(T^*\) 的延拓；若解本来已存在到更晚，则无需调用续接。这个二分应显式写入证明。

### 4.2 \(K_2\) 自改进需保留归一化的 \(+1\)

一般估计是
\[
K_2(t)\le e^{C(1+r^{-2})t}K_2(0).
\]
在 \(t\le\theta r^2\) 上，
\[
K_2(t)\le e^{C\theta(1+r^2)}K_2(0).
\]
只有在明确假设 \(r\le1\) 或 \(r\) 有固定统一上界时，才能简写为 \(e^{C\theta}\)。选择参数使该指数严格小于 \(2\)，即可严格改进 (F1)。

### 4.3 度量与 Sobolev 自改进

由
\[
\|aE(t)\|_\infty\le
C\delta(r^2/t)^{1/3}
\]
得到
\[
D:=\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2.
\]
于是
\[
e^{-CD}g_0\le g(t)\le e^{CD}g_0,
\qquad
\frac{\mathcal S(t)}{\mathcal S(0)}\le e^{C_4D}.
\]
故
\[
\frac{\gamma(t)}{\gamma(0)}
\le
\exp\!\left(C_4D+\frac C2\theta(1+r^2)\right).
\]
选择参数使右侧严格小于 \(2\)，便同时严格改进 (F2)、(F3)。这里同样需要声明 \(r\) 的尺度范围，或将选定时间改为与 \(\min\{r^2,1\}\) 相容的形式。

### 4.4 反证逻辑完整

一旦解已延拓过 \(T^*\)，且 \(K_2,\gamma\) 和度量漂移在 \(T^*\) 均严格位于退出阈值内，连续性保证它们在稍长区间仍满足 (F1)–(F3)，与 \(T^*\) 的定义矛盾。因此，在所有分析输入成立时，
\[
T^*=\theta r^2.
\]

---

## 5. 循环性和最终状态

依赖链本身没有循环：
\[
\text{短时存在}
\to\text{光滑首次退出区间}
\to\text{条件能量/Moser}
\to\sup_{[\tau,T^*)}|U|<\infty
\to\text{续接}
\to\text{严格自改进}.
\]
续接常数可依赖单个数据 \(g(\tau),\chi,\tau\)，不会反馈进入序列统一的 Moser 常数。

正确的 Wang 型方案也不需要无权 \(\sup|\mathrm{Rm}|\)；但需要无权曲率导数的有限 \(L^q\) 矩。Step 37 把许多乘积记为 “lower” 而未给出指数安排，因此当前文本尚不能排除估计时暗用无权点态曲率。

**尚缺的精确数学对象为：**

1. shifted \(U\) 的完整高阶演化式；
2. Wang Proposition 4.13 的归一化版本：
   \(\nabla^{m-1}\mathrm{Rm}\) 的无权 \(L^q\) 传播；
3. top cutoff jet 项的逐项 Hölder/Young 指数表；
4. shifted Proposition 4.3 的平滑终端续接证明；
5. 归一化 transported-DeTurck 短时存在证明；
6. 首次退出定理中明确的 \(r\)-尺度假设。

因此，Step 37 §3.3 所称“不是带未验证外部假设的条件定理”不受现有材料支持。准确状态是：**条件 Moser—首次退出机制成立；Lemma 1.2 可修复；Theorem 1.1 的高阶续接证明仍未完成。**
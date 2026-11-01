# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 44,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step44_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step44_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the repaired continuation seed and higher-order allocation. Read the Step 44 zero-order T note together with the Step 40 staggered induction and the corrected Step 43 note. Check the exact zero-order shifted-curvature energy structure under |U|=|aT|<=K: quadratic reaction, inverse-metric and volume variation, signed Hessian-a contraction, gradient terms, and whether the resulting unweighted L^p bound truly supplies T_0 uniformly up to a finite maximal endpoint. Then check that higher connection-variation terms should be kept as derivatives of Ric(U), and whether the m=1 signed Hessian treatment plus the arbitrary-order schedule closes without any hidden pointwise T assumption or current-exponent escalation. Identify any tensor term or logical dependence that remains unproved; give corrections rather than accepting schematic equations.

## Integrated Scientific Memo

# 核验结论

## 1. Step 44 的零阶 \(T\) 种子成立，但必须明确其适用范围

令
\[
S:=\operatorname{Ric}(U)=aE,\qquad
a=\chi^2,\qquad
T=\operatorname{Rm}+G,\qquad U=aT,
\]
则
\[
\partial_tg=-2S,\qquad |S|\le C_n|U|\le C_nK.
\]

由一般曲率变分公式
\[
\partial_t\operatorname{Rm}=\mathscr D^2S+\operatorname{Rm}*S
\]
以及 \(S=aE\)、\(\nabla G=0\)，可整理为
\[
\partial_tT
=a\Delta T+a\,\mathcal Q(T,G)
+\nabla a*\nabla T
+\mathscr H(\nabla^2a,E)
+\mathcal N(a,T,G),
\]
其中
\[
|\mathcal Q(T,G)|\le C_n(|T|^2+|T|+1),\qquad
|\mathcal N(a,T,G)|\le C_n(a|T|+a).
\]
此外
\[
\partial_tG=-\frac{2a}{n-1}(E\owedge g).
\]

这里真正关键的是：

1. 所有二次曲率反应均带 \(a\)；
2. Hessian 项是 \(\nabla^2a\) 与 \(E\) 的有符号张量收缩；
3. 范数和体积元变分仅由 \(S=\operatorname{Ric}(U)\) 控制。

### 二次反应项

测试 \(p|T|^{p-2}T\) 后，最高次项满足
\[
a|T|^{p+1}=|aT|\,|T|^p=|U|\,|T|^p\le K|T|^p.
\]
因此完全不需要除以 \(a\)，也不需要 \(T\) 的点态控制。

低次项可用 Young 不等式处理；这里默认通常的截止归一化 \(0\le\chi\le1\)。若不作该归一化，常数还必须依赖 \(\|a\|_\infty\)。

### 逆度量和体积元变分

由于 \(T\) 是协变四阶张量，
\[
\partial_t|T|^p
=p|T|^{p-2}\langle\partial_tT,T\rangle
+O_{n,p}(|S||T|^p),
\]
而
\[
\partial_td\mu=-\operatorname{tr}(S)d\mu.
\]
由 \(|S|\le C_nK\)，两者均贡献至多
\[
C_{n,p}K\int_M|T|^p\,d\mu.
\]

### 梯度项

扩散分部积分及显式 \(\nabla a*\nabla T\) 项均产生
\[
C_{n,p}\int |\nabla a|\,|T|^{p-1}|\nabla T|.
\]
利用
\[
\nabla a=2\chi\,d\chi,\qquad
\frac{|\nabla a|^2}{a}=4|d\chi|^2
\]
（在 \(a=0\) 处按零延拓理解），得到
\[
\le \varepsilon\int a|T|^{p-2}|\nabla T|^2
+C_{n,p,\varepsilon}\|d\chi\|_\infty^2\int|T|^p.
\]

### Hessian-\(a\) 项

其准确结构是
\[
I_H=p\int(\nabla_i\nabla_ja)\,
B^{ij}(T,E)|T|^{p-2}\,d\mu,
\]
其中
\[
|B(T,E)|\le C_n|T||E|\le C_n|T|^2,
\qquad
|\nabla B(T,E)|\le C_n|T||\nabla T|.
\]
第二式使用
\[
\nabla E=\operatorname{Ric}(\nabla T),\qquad \nabla G=0.
\]

必须先保留符号并分部积分：
\[
I_H=-p\int(\nabla_ja)\,
\nabla_i\!\left(B^{ij}|T|^{p-2}\right)d\mu.
\]
于是
\[
|I_H|
\le \varepsilon\int a|T|^{p-2}|\nabla T|^2
+C_{n,p,\varepsilon}\|d\chi\|_\infty^2\int|T|^p.
\]
因此这里确实不需要 \(\|\nabla^2\chi\|_\infty\)。

严格处理非整数实数 \(p\ge2\) 时，可用
\[
(|T|^2+\eta)^{(p-2)/2}T
\]
作测试并令 \(\eta\downarrow0\)。

综上，
\[
\frac d{dt}\mathcal T_p+c_{n,p}\mathcal D_p
\le C_{n,p}(K+1+\|d\chi\|_\infty^2)\mathcal T_p
+C'_{n,p}(K+1)\operatorname{Vol}(g(t)).
\]

由
\[
|\partial_tg|_g\le C_nK
\]
可得有限时间区间上的双 Lipschitz 比较，故 \(\|d\chi\|_{g(t),\infty}\) 与体积均一致有限。于是
\[
\sup_{\tau\le t<T_*}\|T(t)\|_{L^p(g(t))}<\infty
\]
对每个有限 \(p\ge2\) 成立。

这确实给出所需的 \(T_0\) 种子，并且一直一致控制到有限端点 \(T_*\)。但它是：

- 对每个固定数据的估计；
- 依赖 \(\tau,K,T_*-\tau,\|T(\tau)\|_p\) 和截止函数；
- 不具有塌缩序列的一致性；
- 不等价于 \(T\) 的点态有界性。

所以它足够用于继续性导数传播，但不能替代序列一致的加权平滑估计。

---

## 2. 高阶连接变分必须保持为 \(U\) 的导数

对
\[
S=\operatorname{Ric}(U)
\]
有准确公式
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}
\bigl(\nabla_iS_{j\ell}
+\nabla_jS_{i\ell}
-\nabla_\ell S_{ij}\bigr).
\]
因 \(\nabla g^{-1}=0\)，按固定顺序取协变导数时，
\[
\nabla^\ell(\partial_t\Gamma)
=g^{-1}*\nabla^{\ell+1}\operatorname{Ric}(U).
\]
因此
\[
[\partial_t,\nabla^m]T
=\sum_{\ell=0}^{m-1}U_{\ell+1}*T_{m-1-\ell}
\]
至多差有限的槽位收缩系数及因导数重排产生的低阶曲率交换项。

顶阶连接变分项是
\[
U_m*T_0,
\]
而不是 \(T_m*T_0\) 的无权系数。测试 \(T_m\) 时，
\[
\int |U_m||T_0||T_m|^{p-1}
\le
\|U_m\|_{2p}\|T_0\|_{2p}\|T_m\|_p^{p-1}.
\]
此时 \(U_m\) 已由当前配对阶段得到，\(T_0\) 已由零阶种子在任意有限指数得到。因此不需要 \(T_0\in L^\infty\)。

Step 43 的式 (4.2) 把 \(\nabla^j(\partial_t\Gamma)\) 展开成含若干 \(T*T\) 的表达，并不是最安全的原始几何恒等式。应以
\[
\nabla^j(\partial_t\Gamma)
=g^{-1}*\nabla^{j+1}\operatorname{Ric}(U)
\]
作为分配起点；只有在重排协变导数时才引入曲率乘积，而且这些交换项应逐项证明落在先前空间层级。

---

## 3. \(m=1\) 的现有正文包含一处实质性错误

Step 43 §3 对
\[
\int\chi C_2\,T_1\,P(T_1)
=\int\chi C_2|T_1|^p
\]
曾声称可由 \(C_2\in L^\infty\) 控制。该说法错误且会循环：当前阶段没有可用的 \(\|\nabla^2\chi\|_\infty\) 控制。

必须改为有符号 Hessian 分部积分。若 \(X=T_1\)，则相应项具有
\[
J=\int\chi\,\nabla_i\nabla_j\chi\,
B^{ij}(X)|X|^{p-2}
\]
的结构，其中
\[
|B(X)|\le C|X|^2,\qquad
|\nabla B(X)|\le C|X||\nabla X|.
\]
分部积分后得到
\[
|J|
\le
\varepsilon\int\chi^2|\nabla X|^2|X|^{p-2}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|X\|_p^p.
\]
这与 Step 40 的机制一致，也与 Step 43 §9 的后续更正一致。故 Step 43 §3 中“\(C_2\) bounded or in \(L^\infty\)”必须删除。

---

## 4. 有限指数的交错安排在已列出的项上闭合

正确顺序为
\[
T_0\to(U_1,C_2)\to T_1
\to(U_2,C_3)\to T_2\to\cdots.
\]

设当前加权变量
\[
V=U_m,\qquad Z=C_{m+1}.
\]
关键分配如下。

1. \(\chi C_1U_{m+1}\) 由加权耗散吸收。

2. \(\chi C_2V\) 保留为有符号 Hessian 收缩并分部积分，不能用 \(C_2\) 点态界。

3. 唯一含 \(C_{m+2}\) 的项是
   \[
   \chi C_{m+2}U.
   \]
   一次分部积分后只留下当前 \(Z=C_{m+1}\)。

4. 产生的
   \[
   \int\chi ZU_1P(V)
   \]
   在 \(m\ge2\) 时写 \(Z=\nabla C_m\) 再分部积分，得到
   \[
   d\chi*C_m*U_1*P(V),\quad
   \chi C_m*U_2*P(V),\quad
   \chi C_m*U_1*\nabla P(V),
   \]
   加上重排交换项。放大的指数只落在先前层级 \(C_m,U_1,U_2\) 上。\(m=2\) 的第二项是当前 Hessian 型，\(m\ge3\) 时 \(U_2\) 是先前层级。

5. 当前配对变量只以
   \[
   |Z|^2|V|^{p-2},
   \qquad |Z||V|^{p-1}
   \]
   出现，因此仅需 \(Z,V\in L^p\)，不存在当前指数从 \(p\) 升到 \(2p\) 的无限链。

截止 jet 的原始演化为
\[
\partial_tC_{m+1}
=\sum_{\ell=0}^{m-1}
\nabla^\ell(\partial_t\Gamma)*C_{m-\ell},
\]
顶阶为 \(U_m*C_1\)，不出现 \(U_{m+1}\) 或 \(C_{m+2}\)。能量中的逆度量、范数和体积变化可记为有界系数 \(U_0*C_{m+1}\)，但这不是固定标量 \(\chi\) 的原始 jet 演化项。

在随后的 \(T_m\) 阶段，
\[
\chi C_{m+2}T\,P(T_m)
\]
一次分部积分后产生
\[
\int |C_{m+1}|^2|T|^2|T_m|^{p-2},
\]
并可由
\[
C_{m+1},T\in L^{2p},\qquad T_m\in L^p
\]
控制。这里 \(C_{m+1}\) 是已完成的当前配对层级，\(T=T_0\) 是已完成的零阶层级；只有当前未知 \(T_m\) 保持在指数 \(p\)。

Laplacian 交换子的当前阶代数项形如
\[
a\,\operatorname{Rm}*T_m=(U-aG)*T_m,
\]
故其系数由 \(K+C_n\) 点态控制，而不是由 \(T\) 点态控制。

因此，就已明确列出的张量类型而言，交错安排没有隐藏的点态 \(T\) 假设，也没有当前变量的指数升级。

---

## 5. 尚未证明的精确对象

当前材料还不能把任意阶导数传播称为完整张量级证明，原因不是指数预算，而是以下全项分类尚未展开：

1. **Step 40 (1.4)、(1.5) 的全指标推导。**  
   需证明把 \(\nabla^m\) 与 \(a\Delta\)、时间依赖连接及所有归一化项交换后，每个收缩都确实落入所列家族，且没有遗漏含 \(U_{m+1}\)、\(T_{m+1}\) 或当前 jet 的异常项。

2. **第二次分部积分后的重排余项。**  
   需要明确证明所有
   \[
   [\nabla_i,\nabla_j]C_m
   \]
   型项均为
   \[
   \nabla^q\operatorname{Rm}*C_s,\qquad q+s\le m-1,
   \]
   或相应的已完成层级组合，而不是仅以 \(\mathcal R_{\rm com}\) 表示。

3. **完整 Laplacian 交换子 ledger。**  
   应逐项验证
   \[
   [\nabla^m,\Delta]T
   \]
   中当前阶部分均带 \(a\operatorname{Rm}=U-aG\)，其余项只含 \(T_j\)、\(j<m\)。

4. **各 signed-Hessian 收缩的 tensor provenance。**  
   不能仅凭标量原型断言所有 \(\chi C_2V\) 或 \(\chi C_2T_m\) 项都具有允许一次分部积分且满足
   \[
   |\nabla B|\lesssim |X||\nabla X|+\text{低阶项}
   \]
   的准确收缩结构；需从曲率变分和交换公式逐项确认。

提供的 Python 脚本只核验权重恒等式、Hölder 指数和层级顺序，明确没有核验这些张量来源，因此不能填补上述缺口。

最后，即便全阶 ledger 补齐，现有结果也只给出：

\[
\sup|U|<\infty
\Longrightarrow
\text{正时间区间上的全部导数有界及平滑终端极限}.
\]

从终端度量真正延拓到 \(T_*\) 之后，还依赖尚未证明的退化、带输运系数的 DeTurck 短时间存在/重启定理。该问题与本次零阶种子和指数安排不同，不能由小 \(a\) 区域的 Schauder 估计替代。

**最终判断：**Step 44 的零阶 \(T_0\) 修复有效；连接变分必须保持为 \(\nabla^{j+1}\operatorname{Ric}(U)\)；修正 \(m=1\) 的错误 Hessian 处理后，已展示的任意阶分配在指数层面闭合。尚未完成的是任意阶演化和交换项的全指标穷尽证明，以及独立的退化 DeTurck 重启定理。
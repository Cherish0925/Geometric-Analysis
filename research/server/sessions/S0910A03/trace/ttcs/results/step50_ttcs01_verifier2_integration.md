# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 50,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step50_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step50_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the normalized Wang continuation argument in Step 50. Read the actual Wang source and the Step 40/44/45 shifted-curvature notes. Focus on whether the equations for T=Rm+G, U=χ²T, evolving cutoff jets C_j, and connection difference really support the staggered inequalities (3.9),(3.11),(3.12), pointwise all-order bounds, fixed-coordinate convergence, and restart under only bounded |χ²Rm| on a positive-time slab. Look for hidden use of pointwise unweighted T, a prescribed Hessian cutoff, exponent escalation, missing current derivative, incorrect ∂tΓ, insufficient Sobolev order, or endpoint integrability. Give exact repairs if needed and state what is actually established.

## Integrated Scientific Memo

# 核验结论：Step 50 的 normalized Wang 延拓

## 1. 结论与准确表述

Wang 源文第 4 节确实支持如下**正时间终端薄片版本**的导数传播结论。

设 \(M\) 闭，\(0<\tau<T_*<\infty\)，且
\[
\partial_tg=-2\chi^2(\Ric_g+g)
\]
在 \([\tau,T_*)\) 上光滑。若
\[
\sup_{M\times[\tau,T_*)}|\chi^2\Rm_g|\le K,
\]
则：

1. \(T=\Rm+G\)、\(U=\chi^2T\) 及演化中的 cutoff jets
   \(C_j=\nabla^j\chi\) 在所有有限 \(L^p\) 阶数上均一致有界；
2. 进而所有这些张量的协变导数均逐点一致有界；
3. \(g(t)\) 在任意固定背景联络下的每个 \(C^k\) 范数中收敛到光滑正定极限 \(g_*\)。

若另行接受 Step 50 §2 的 normalized Yang 短时存在/重启定理，则原解可光滑延拓越过 \(T_*\)。

因此 Step 50 的 Wang 导数传播核心成立；更精确地，假设只需位于终端薄片，不需控制 \(t=0\) 附近。常数是 per-datum 的，依赖 \(g(\tau),\chi,K,T_*-\tau,n\)，并非序列一致常数。

---

## 2. 与 Wang 源文的对应关系

Wang Theorem 4.1 的原命题是：局部 Ricci 流
\[
\partial_tg=-2\chi^2\Ric
\]
若 \(\|\chi^2\Rm\|_\infty\) 在有限时间区间有界，则可光滑延拓。其 Remark 4.2 和 Lemmas 4.4–4.6、4.10–4.11、Propositions 4.13–4.14 明确采用三个相互耦合的族：

\[
\nabla^m(\chi^2\Rm),\qquad \nabla^m\Rm,\qquad \nabla^{m+1}\chi.
\]

Step 40/44/45 所作的错位顺序
\[
T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots
\]
正是这一机制的更精细、避免当前指数升级的版本。

归一化由
\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\Rm+G,\qquad U=aT,\quad a=\chi^2
\]
吸收，因为
\[
\Ric(G)=g,\qquad \Ric(T)=\Ric+g,\qquad
\partial_tg=-2\Ric(U).
\]
而且 \(\nabla G=0\)，
\[
\partial_tG=-\frac{2a}{n-1}\bigl((\Ric+g)\owedge g\bigr)
\]
只含 \(U\) 的代数收缩，不增加最高空间导数。因此 Wang 的三族结构在 shift 后保持不变。

---

## 3. 方程与导数计数

令 \(B_j=\nabla^ja\)、\(C_j=\nabla^j\chi\)。坐标时间下的结构式为
\[
\partial_tT
=a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T+1), \tag{1}
\]
以及
\[
\partial_tU
=a\Delta U+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+aU+a^2. \tag{2}
\]

必须始终保留
\[
B_j=2\chi C_j+
 \sum_{1\le q\le j-1}C_q*C_{j-q},\qquad B_1=2\chi C_1. \tag{3}
\]
只有最高单个 jet \(C_j\) 自动带 \(\chi\)；其余乘积不能虚构 \(\chi\) 因子。

### 联络变化

若 \(S=\Ric(U)\)，则
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}\left(\nabla_iS_{j\ell}
+\nabla_jS_{i\ell}-\nabla_\ell S_{ij}\right). \tag{4}
\]
符号和导数阶数均正确。因此按有序协变导数
\[
\nabla^r(\partial_t\Gamma)=g^{-1}*\nabla^{r+1}U, \tag{5}
\]
重排导数时只增加曲率乘较低阶导数。

### cutoff jets

因为 \(\chi\) 仅作为标量函数固定，并非其高阶协变导数固定，
\[
\partial_tC_1=0,
\]
且对 \(m\ge1\),
\[
\partial_tC_{m+1}
=\sum_{r+s=m-1}U_{r+1}*C_{s+1}. \tag{6}
\]
唯一当前项是
\[
U_m*C_1.
\]
不存在遗漏的 \(U_{m+1}\) 或 \(C_{m+2}\)。能量中出现的
\(U_0*C_{m+1}\) 来自范数及体积形式变化，不是原始 jet 方程中的首项。

---

## 4. 三个能量不等式

### 4.1 零阶 \(T\) 种子：式 (3.9)

由 \(|a\Rm|\le K\) 得
\[
|U|=|a(\Rm+G)|\le K+C(n,\|\chi\|_\infty).
\]
故 \(|\partial_tg|_g\lesssim |U|\)，有限终端薄片上度量双 Lipschitz 等价，体积、标量 Sobolev 常数和 \(|d\chi|\) 一致有界。

以 \(|T|^{p-2}T\) 测试 (1)。反应项的关键恒等式是
\[
a|T|^{p+1}=|U|\,|T|^p.
\]
Hessian 项必须保留其带符号收缩：
\[
I_H=\int(\nabla_i\nabla_ja)\,
 \mathcal B^{ij}(T,E)|T|^{p-2},\qquad E=\Ric(T).
\]
由于
\[
|\mathcal B|\lesssim |T|^2,\qquad
|\nabla\mathcal B|\lesssim |T||\nabla T|,
\]
后一式依赖
\[
E=\Ric(T),\qquad \nabla E=\operatorname{tr}(\nabla T),\qquad \nabla G=0.
\]
闭流形上积分分部一次后只留下 \(da=2\chi\,d\chi\)，并由
\[
\frac{|da|^2}{a}=4|d\chi|^2
\]
吸收到加权耗散。因此
\[
\frac d{dt}\|T\|_p^p
+c_p\int a|\nabla T|^2|T|^{p-2}
\le C_p\|T\|_p^p+C_p\Vol_g(M). \tag{7}
\]
这才是 (3.9) 的完整形式；有限体积加项不可省略，但对 Gronwall 无害。

结论只是
\[
T_0\in L^p\quad\text{对每个有限 }p,
\]
此处没有、也不需要逐点无权 \(T\) 界。

### 4.2 当前对 \((U_m,C_{m+1})\)：式 (3.11)

令
\[
V=U_m,\qquad Z=C_{m+1},\qquad P(V)=|V|^{p-2}V.
\]
当前一阶导数只以
\[
B_1*U_{m+1}=2\chi C_1*U_{m+1}
\]
出现，故可吸收到
\[
D_{m,p}=\int a|\nabla V|^2|V|^{p-2}.
\]

\(B_2*V\) 不能由预设 \(\|\nabla^2\chi\|_\infty\) 控制，而须作为
\[
\int(\nabla^2a)*\mathcal B(V)
\]
带符号积分分部。

最高 cutoff jet 的全部来源均具有共同形式
\[
\chi C_{m+2}*\mathcal A(U_0),\qquad
|\mathcal A(U_0)|\lesssim |U_0|.
\]
其中包括 Hessian-\(a\) 源和把方程整理为
\((\partial_t-a\Delta)U_m\) 时出现的 \(-(\nabla^m\Delta a)U\) 源；两者都带必要的 \(\chi\)。

积分分部一次产生
\[
C_1*Z*U_0*P(V),\quad
\chi Z*U_1*P(V),\quad
\chi Z*U_0*\nabla P(V). \tag{8}
\]
最后一项经 Young 留下
\[
|Z|^2|V|^{p-2}
\le \frac2p|Z|^p+\frac{p-2}{p}|V|^p, \tag{9}
\]
故当前 \(Z\) 不需要 \(L^{2p}\)。

中间项 \(\chi Z*U_1*P(V)\) 对 \(m\ge2\) 再将
\(Z=\nabla C_m\) 积分分部，产生的因子均在较早空间层；\(m=1,2\) 的端点则恰为 signed-Hessian 型。故没有无限指数上升。

还必须显式消去 \((B_1*B_1)*T\) 的当前 \(T_m\)：
\[
aT_m=U_m-\sum_{q=1}^mB_q*T_{m-q}, \tag{10}
\]
所以
\[
B_1*B_1*T_m
=4C_1*C_1\left(U_m-\sum_{q=1}^mB_q*T_{m-q}\right), \tag{11}
\]
这里是精确流 \(a=\chi^2\) 的写法；不除以 \(a\)。同一恒等式也处理空间曲率交换子中表面的当前 \(T_m\)。

结合 (6)，得到
\[
\frac d{dt}\left(\|U_m\|_p^p+\|C_{m+1}\|_p^p\right)
+c_{m,p}D_{m,p}
\le C_{m,p}\left(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\right). \tag{12}
\]
因此 (3.11) 成立。

### 4.3 后续无权 \(T_m\)：式 (3.12)

在当前对已对所有有限指数完成后，令 \(X=T_m\)。唯一尚未直接已知的 cutoff jet 是
\[
\chi C_{m+2}*T_0.
\]
积分分部一次后得到
\[
d\chi*C_{m+1}*T_0*P(X),\quad
\chi C_{m+1}*T_1*P(X),\quad
\chi C_{m+1}*T_0*\nabla P(X). \tag{13}
\]
最后一项吸收后留下
\[
|C_{m+1}|^2|T_0|^2|X|^{p-2}.
\]
此时 \(C_{m+1}\) 和 \(T_0\) 已对所有有限指数控制，所以可使用 \(L^{2p}\) 等较大指数；这不是对未知 \(X\) 的指数升级。

\(m=1\) 的中间项为 signed-Hessian 型；\(m\ge2\) 时 \(T_1\) 是前层。时间联络项 \(U_m*T_0\) 只作为有限指数 forcing 使用，不作为逐点系数。当前二次曲率项的系数是
\[
aT_0=U_0,
\]
故逐点有界。于是
\[
\frac d{dt}\|T_m\|_p^p
+c_{m,p}\int a|\nabla T_m|^2|T_m|^{p-2}
\le C_{m,p}(1+\|T_m\|_p^p). \tag{14}
\]
即 (3.12)。

---

## 5. 点态界与固定坐标极限

每层先对**所有有限指数**建立估计。取
\[
p>\max\{n,100\}
\]
即可同时符合 Wang 源文的 \(p>100\) 选择和 Sobolev 嵌入。由一致标量 Sobolev 不等式和 Kato 不等式，
\[
\|U_m\|_\infty
\lesssim \|U_m\|_p+\|U_{m+1}\|_p,
\]
对 \(T_m,C_m\) 同理。因此所有协变导数逐点有界。固定坐标 \(k\) 阶估计实际需要再多一至两个 \(L^p\) 空间层，但全阶归纳已经提供。

固定 \(\bar\nabla=\nabla^{g(\tau)}\)，令
\[
A=\nabla^g-\bar\nabla.
\]
由 (4)
\[
\partial_tA=g^{-1}*\nabla\Ric(U). \tag{15}
\]
利用 \(\bar\nabla=\nabla+A*\) 归纳可得
\[
\sup_{t<T_*}\|\bar\nabla^kA(t)\|_\infty<\infty,
\qquad
\sup_{t<T_*}\|\partial_t\bar\nabla^kg(t)\|_\infty<\infty. \tag{16}
\]
终端区间长度有限，故右侧在时间上可积，\(g(t)\) 在每个固定背景 \(C^k\) 范数中 Cauchy。双 Lipschitz 控制保证极限正定。

这里不存在端点可积性问题：若外部 Moser 估计仅给
\[
|a\Rm|\lesssim t^{-1},
\]
它只用于证明 \([T_*/2,T_*)\) 上有界；不对 \(t^{-1}\) 从零积分。

---

## 6. 重启部分的证据边界

Wang 能量论证本身严格建立的是：

> 有光滑正定终端度量 \(g_*\)，且原流在固定坐标中光滑趋于 \(g_*\)。

“延拓越过 \(T_*\)”还依赖 normalized Yang 短时存在。Step 50 对新增项
\[
-2\widehat a\,\widehat g
\]
的线性化
\[
-2\widehat a\,h
+4\widehat\chi\,d\widehat\chi(\zeta)\widehat g
\]
确实只改变 Yang 线性系统的零阶 \(D,E\) slots，形式上不改变主符号或导数损失。因此其扰动论证是合理的。

但本输入中实际提供的是 Wang 全文，未提供 Yang 原文相应线性系统及 smooth-tame inverse 的完整证明。因此，基于当前材料可独立核验的是 Wang 导数传播和光滑终端极限；完整重启定理仍条件性依赖 Step 50 所引 Yang 定理。若该短时定理成立，则无需唯一性：自治方程使左右两段的全部时间 jets 均由 \(g_*\) 递归决定，拼接光滑。

---

## 7. 必须保留的修正

最终陈述中应作以下三点修正：

1. 将 (3.9) 写成含有限体积加项的 (7)，不要伪装成纯齐次 Gronwall。
2. 在 signed-Hessian 处明确写出
   \[
   E=\Ric(T),\qquad \nabla E=\operatorname{tr}(\nabla T),
   \]
   这是归一化 Hessian 项无需预设 \(\nabla^2\chi\) 界的关键。
3. 明确区分：
   - (3.9)–(3.15)：由 Wang 型论证得到光滑终端极限；
   - 延拓越过终点：另需 normalized Yang 重启。

综上，没有发现隐藏的逐点无权 \(T\)、预设 Hessian cutoff、当前指数升级、遗漏当前导数、错误的 \(\partial_t\Gamma\)、Sobolev 阶数不足或 \(t=0\) 端点不可积。真正尚未由本材料直接重验的对象，是 Yang 的原始 smooth-tame 逆及其 normalized 零阶扰动后的短时重启。
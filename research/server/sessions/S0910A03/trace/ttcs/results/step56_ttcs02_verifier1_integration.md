# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 56,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step56_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step56_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Attack the earliest positive-time continuation interface for the exact cutoff flow, not the start theorem. On a fixed smooth terminal slab [tau,T*) assume sup|U|<K, metric bilipschitz equivalence, fixed smooth chi, and finite initial norms at tau, where T=Rm+g∧g/(2(n−1)), U=chi^2 T. Verify in detail the m=1 coupled pair (U_1=∇U,C_2=∇²chi), then the unweighted T_1=∇T estimate. List every highest-order term, especially chi C_3 U, chi C_2 U_1, dchi C_2 U, ∇³a T, and connection variation; perform the needed signed integrations by parts and state exact L^p inequalities. Determine whether any estimate divides by chi, needs unweighted pointwise T, introduces a ratio of regularization parameters, or fails near the small-chi collar. Ground the answer in the attached Step 40/44/45 notes and correct them if needed.

## Integrated Scientific Memo

# \(m=1\) 精确正时间延拓接口核验

令
\[
a=\chi^2,\qquad
T=\Rm+G,\qquad G=\frac{g\owedge g}{2(n-1)},\qquad U=aT,
\]
且
\[
\partial_tg=-2S,\qquad S=\Ric(U)=a(\Ric+g).
\]
在固定终端时间片 \([\tau,T_*)\) 上假设
\[
\|U\|_{L^\infty(M\times[\tau,T_*))}\le K,
\]
度量一致双 Lipschitz 等价，\(\chi\) 为固定光滑函数，且 \(t=\tau\) 时所需范数有限。以下采用 **坐标时间 \(\partial_t\)**；所有范数和协变导数均相对于 \(g(t)\)。

记
\[
C_j=\nabla^j\chi,\quad B_j=\nabla^ja,\quad
V=U_1=\nabla U,\quad Z=C_2=\nabla^2\chi,\quad X=T_1=\nabla T,
\]
并置
\[
L=\sup_{M\times[\tau,T_*)}|d\chi|<\infty .
\]

结论是：Step 44 的 \(T_0\) 种子成立；其后
\[
T_0\longrightarrow (U_1,C_2)\longrightarrow T_1
\]
在每个有限 \(L^p\) 中闭合。全过程不除以 \(\chi\)，不需要 \(T\) 的无权逐点界，不引入正则化参数比值，并且在小 \(\chi\) collar 上不失效。

---

## 1. 必需的无权 \(T_0\) 种子

不能由 \(|U|=|\chi^2T|\le K\) 直接推出无权 \(T\) 控制。正确输入是 Step 44 的独立能量估计：对每个有限 \(q\ge2\)，
\[
\frac d{dt}\|T\|_q^q
+c_{n,q}\int_M a|\nabla T|^2|T|^{q-2}
\le
C_{n,q,K,L}\bigl(\|T\|_q^q+\Vol_{g(t)}M\bigr).
\tag{1.1}
\]
其中：

* 漂移项使用
  \[
  B_1=2\chi C_1,\qquad \frac{|B_1|^2}{a}=4|C_1|^2
  \tag{1.2}
  \]
  ——这应理解为不等式 \(|B_1|^2\le4a|C_1|^2\)，而非在 \(a=0\) 处真的作商；
* 二次反应项使用
  \[
  a|T|^{q+1}=|U||T|^q\le K|T|^q;
  \]
* \(\nabla^2a\) 的曲率变分收缩保留符号后积分分部，只留下 \(da\)，无需 \(\|\nabla^2\chi\|_\infty\)。

故
\[
\sup_{\tau\le t<T_*}\|T(t)\|_q<\infty
\qquad(\forall q<\infty).
\tag{1.3}
\]

---

## 2. 通用 signed-Hessian 引理

若 \(Y=V\) 或 \(Y=X\)，当前 Hessian 项均可写为
\[
H_p(Y)=\int_M\chi(C_2)_{ij}\,\mathcal B^{ij}(Y)\,d\mu,
\]
其中
\[
|\mathcal B(Y)|\le C_{n,p}|Y|^p,\qquad
|\nabla\mathcal B(Y)|
\le C_{n,p}|Y|^{p-1}|\nabla Y|.
\]
在闭流形上，
\[
H_p(Y)
=-\int C_{1,i}C_{1,j}\mathcal B^{ij}(Y)
-\int\chi C_{1,j}\nabla_i\mathcal B^{ij}(Y).
\]
因此对任意 \(\varepsilon>0\)，
\[
|H_p(Y)|
\le
\varepsilon\int a|\nabla Y|^2|Y|^{p-2}
+C_{n,p,\varepsilon}L^2\|Y\|_p^p.
\tag{2.1}
\]
这是 \(m=1\) 的核心第二次 signed integration by parts：当前未知 \(C_2\) 被降为 \(d\chi\)，而不是以绝对值系数估计。

---

# 3. 耦合对 \((U_1,C_2)\)

## 3.1 完整最高阶账本

Step 45 的无除法坐标时间方程为
\[
\partial_tU
=a\Delta U+B_1*U_1+B_2*U+(B_1*B_1)*T
+U*U+aU+a^2,
\tag{3.1}
\]
其中
\[
B_1=2\chi C_1,\qquad
B_2=2\chi C_2+2C_1*C_1,\qquad
B_3=2\chi C_3+C_1*C_2.
\tag{3.2}
\]
对 (3.1) 求一次协变导数，并加入空间 Laplacian commutator 与坐标时间 connection variation，最高阶族为
\[
\begin{array}{c|l}
\text{来源}&m=1\text{ 项}\\ \hline
a\Delta U&
a\Delta V,\ B_1*U_2,\ a\Rm*V,\ a\nabla\Rm*U\\
B_1*U_1&
B_1*U_2,\ B_2*V\\
B_2*U&
B_3*U,\ B_2*V\\
(B_1*B_1)*T&
B_2*B_1*T,\ B_1*B_2*T,\ B_1*B_1*X\\
U*U&U*V\\
[\partial_t,\nabla]U&(\partial_t\Gamma)*U=V*U\\
aU+a^2&aV,\ B_1*U,\ aB_1 .
\end{array}
\tag{3.3}
\]

特别地，题目要求的三种最高 cutoff 类型全部出现：
\[
\boxed{\chi C_3U,\qquad \chi C_2U_1,\qquad d\chi\,C_2U.}
\tag{3.4}
\]
不存在裸的 \(C_3U\)。

### 消除表面上的 \(T_1\) 循环

不能把 \(B_1B_1X\) 独立估计。对精确流 \(a=\chi^2\)，完整组合满足
\[
(B_1*B_1)*T=4(C_1*C_1)*U,
\tag{3.5}
\]
故
\[
\nabla\big((B_1*B_1)*T\big)
=C_1*C_2*U+C_1*C_1*V.
\tag{3.6}
\]
所以该族不需要尚未建立的 \(X=T_1\)。

同样，
\[
a\nabla T=V-B_1*T,
\tag{3.7}
\]
从而
\[
a\nabla\Rm*U=(V-B_1*T)*U.
\tag{3.8}
\]
右端只含当前 \(V\)、有界 \(U\) 和已知有限 \(L^q\) 的 \(T\)。这保证顺序确为
\[
T_0\to(U_1,C_2)\to T_1,
\]
不存在循环依赖。

---

## 3.2 \(\chi C_3U\) 的第一次积分分部

置
\[
P(V)=|V|^{p-2}V,\qquad
D^U_{1,p}=\int_Ma|\nabla V|^2|V|^{p-2}.
\]
对每个有序收缩，
\[
\begin{aligned}
\int P(V)*\chi C_3*U
={}&-\int\nabla P(V)*\chi Z*U\\
&-\int P(V)*C_1*Z*U
-\int P(V)*\chi Z*V .
\end{aligned}
\tag{3.9}
\]

第一项满足
\[
\begin{aligned}
\left|\int\nabla P(V)*\chi Z*U\right|
&\le \varepsilon D^U_{1,p}
+C_{n,p,\varepsilon}K^2
 \int |Z|^2|V|^{p-2}\\
&\le \varepsilon D^U_{1,p}
+C_{n,p,K,\varepsilon}
 \bigl(\|Z\|_p^p+\|V\|_p^p\bigr),
\end{aligned}
\tag{3.10}
\]
其中用了逐点 Young 不等式
\[
|Z|^2|V|^{p-2}
\le \frac2p|Z|^p+\frac{p-2}{p}|V|^p.
\tag{3.11}
\]

第二项即题目点名的 \(d\chi\,C_2U\)：
\[
\left|\int P(V)*C_1*Z*U\right|
\le C_{p}LK
\left(\frac1p\|Z\|_p^p+\frac{p-1}{p}\|V\|_p^p\right).
\tag{3.12}
\]

第三项即 \(\chi C_2U_1\)，是 (2.1) 的 signed-Hessian 项：
\[
\left|\int\chi Z*V*P(V)\right|
\le\varepsilon D^U_{1,p}
+C_{n,p,\varepsilon}L^2\|V\|_p^p.
\tag{3.13}
\]
直接来自 \(B_2*V\) 的 \(\chi C_2V\) 也按 (3.13) 处理；来自 \(B_3U\) 和 (3.6) 的 \(C_1C_2U\) 按 (3.12) 处理。

关键点：当前 \(Z=C_2\) 只以 \(L^p\) 出现，绝不要求 \(Z\in L^{2p}\)。

---

## 3.3 导数项及其余项

漂移项满足
\[
\left|\int P(V)*B_1*\nabla V\right|
\le \varepsilon D^U_{1,p}
+C_{n,p,\varepsilon}L^2\|V\|_p^p.
\tag{3.14}
\]

当前曲率系数均是加权的：
\[
a\Rm=U-aG,
\tag{3.15}
\]
故为有界系数。由 (3.8)，剩余 forcing 满足
\[
\int |B_1||T||U||V|^{p-1}
\le C LK\,\|T\|_p\|V\|_p^{p-1}
\le C_{p,L,K}\bigl(\|T\|_p^p+\|V\|_p^p\bigr).
\tag{3.16}
\]

连接变分精确为
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}\bigl(
\nabla_iS_{j\ell}+\nabla_jS_{i\ell}-\nabla_\ell S_{ij}
\bigr),
\tag{3.17}
\]
而 \(S=\Ric(U)\)，故
\[
|\partial_t\Gamma|\le C_n|V|.
\tag{3.18}
\]
因此 \([\partial_t,\nabla]U=(\partial_t\Gamma)*U\) 是有界 \(U\) 乘当前 \(V\)。张量范数和体积元的时间变分系数为 \(S=\Ric(U)\)，同样由 \(K\) 控制。

合并后
\[
\boxed{
\frac d{dt}\|V\|_p^p+c_{n,p}D^U_{1,p}
\le
C_{n,p,K,L}
\bigl(1+\|T\|_p^p+\|V\|_p^p+\|Z\|_p^p\bigr).}
\tag{3.19}
\]

---

## 3.4 \(C_2\) 的坐标时间演化

由于 \(\chi\) 是固定标量，
\[
\partial_tC_1=0,\qquad
\partial_tC_2=-(\partial_t\Gamma)*C_1.
\tag{3.20}
\]
因此
\[
|\partial_tZ|\le C_nL|V|.
\tag{3.21}
\]
原始 jet 方程中没有 \(U*Z\)；此类项只由 \(Z\) 的范数及体积元变化产生，系数由 \(|U|\le K\) 控制。于是
\[
\boxed{
\frac d{dt}\|Z\|_p^p
\le C_{n,p,K,L}
\bigl(\|V\|_p^p+\|Z\|_p^p\bigr).}
\tag{3.22}
\]

由 (3.19)、(3.22) 和 (1.3)，
\[
\boxed{
\frac d{dt}\bigl(\|V\|_p^p+\|Z\|_p^p\bigr)
+c_{n,p}D^U_{1,p}
\le
C_{n,p,K,L}
\bigl(1+\|T\|_p^p+\|V\|_p^p+\|Z\|_p^p\bigr).}
\tag{3.23}
\]
Gronwall 给出
\[
\sup_{\tau\le t<T_*}
\bigl(\|\nabla U(t)\|_p+\|\nabla^2\chi(t)\|_p\bigr)<\infty
\quad(\forall p<\infty).
\tag{3.24}
\]

---

# 4. 随后的无权 \(T_1=\nabla T\) 估计

## 4.1 完整最高阶账本

无权 \(T\) 方程为
\[
\partial_tT
=a\Delta T+B_1*T_1+B_2*T+a(T*T+T+1),
\tag{4.1}
\]
保留所有固定收缩、shift 与 \(G\)-变分低阶项。求一次协变导数后：
\[
\begin{array}{c|l}
\text{来源}&m=1\text{ 项}\\ \hline
a\Delta T&
a\Delta X,\ B_1*T_2,\ a\Rm*X,\ a\nabla\Rm*T\\
B_1*T_1&
B_1*T_2,\ B_2*X\\
B_2*T&
B_3*T,\ B_2*X\\
aT*T&
B_1*T*T,\ aX*T\\
[\partial_t,\nabla]T&
(\partial_t\Gamma)*T=V*T\\
\text{shift/G 项}&aX,\ B_1*T,\ B_1 .
\end{array}
\tag{4.2}
\]

当前 \(X\) 的曲率系数仍是加权的：
\[
aT*X=U*X,\qquad
a\nabla\Rm*T=aX*T=X*U,\qquad
a\Rm*X=(U-aG)*X.
\tag{4.3}
\]
无权 \(T\) 只作为 forcing 因子出现，不作为 \(L^\infty\) 系数。

---

## 4.2 \(\nabla^3a*T\) 必须先展开

精确地，
\[
\nabla^3a*T
=2\chi C_3*T+C_1*C_2*T,
\tag{4.4}
\]
其中星号包含所有排列及固定数值系数。必须只对 \(\chi C_3T\) 积分分部；不能把整个 \(\nabla(\nabla^2a)\) 盲目积分，否则会产生无 \(\chi\) 的
\[
C_1*C_1*T*\nabla P(X),
\]
而加权耗散无法控制它。

置
\[
P(X)=|X|^{p-2}X,\qquad
D^T_{1,p}=\int_Ma|\nabla X|^2|X|^{p-2}.
\]
则
\[
\begin{aligned}
\int P(X)*\chi C_3*T
={}&-\int C_1*Z*T*P(X)\\
&-\int\chi Z*X*P(X)
-\int\chi Z*T*\nabla P(X).
\end{aligned}
\tag{4.5}
\]

第一项：
\[
\int |C_1||Z||T||X|^{p-1}
\le
L\|Z\|_{2p}\|T\|_{2p}\|X\|_p^{p-1},
\tag{4.6}
\]
故对任意 \(\delta>0\)，
\[
\le \delta\|X\|_p^p
+C_{p,\delta}L^p
\bigl(\|Z\|_{2p}\|T\|_{2p}\bigr)^p.
\tag{4.7}
\]

第二项是 signed Hessian：
\[
\left|\int\chi Z*X*P(X)\right|
\le\varepsilon D^T_{1,p}
+C_{n,p,\varepsilon}L^2\|X\|_p^p.
\tag{4.8}
\]

第三项：
\[
\begin{aligned}
\left|\int\chi Z*T*\nabla P(X)\right|
&\le \varepsilon D^T_{1,p}
+C_{n,p,\varepsilon}
 \int|Z|^2|T|^2|X|^{p-2}\\
&\le \varepsilon D^T_{1,p}
+C_{n,p,\varepsilon}
 \|Z\|_{2p}^2\|T\|_{2p}^2\|X\|_p^{p-2}\\
&\le \varepsilon D^T_{1,p}
+\delta\|X\|_p^p
+C_{n,p,\varepsilon,\delta}
\bigl(\|Z\|_{2p}\|T\|_{2p}\bigr)^p .
\end{aligned}
\tag{4.9}
\]
当 \(p=2\) 时直接去掉 \(\|X\|_p^{p-2}\) 因子理解。

低阶 \(C_1*C_2*T\) 项按 (4.6)–(4.7) 直接 Hölder，不作进一步积分分部。

---

## 4.3 其余最高项和 connection variation

漂移项：
\[
\left|\int P(X)*B_1*T_2\right|
\le\varepsilon D^T_{1,p}
+C_{n,p,\varepsilon}L^2\|X\|_p^p.
\tag{4.10}
\]

\(B_2*X\) 展开为
\[
(2\chi C_2+2C_1*C_1)*X.
\]
前者按 signed-Hessian 引理，后者为有界零阶系数，故
\[
\left|\int P(X)*B_2*X\right|
\le\varepsilon D^T_{1,p}
+C_{n,p,\varepsilon}L^2\|X\|_p^p.
\tag{4.11}
\]

二次 forcing：
\[
\int |B_1||T|^2|X|^{p-1}
\le
\delta\|X\|_p^p
+C_{p,\delta,L}\|T\|_{2p}^{2p}.
\tag{4.12}
\]

坐标时间 connection variation 为
\[
[\partial_t,\nabla]T=(\partial_t\Gamma)*T=V*T,
\tag{4.13}
\]
故
\[
\int |V||T||X|^{p-1}
\le
\delta\|X\|_p^p+
C_{p,\delta}\bigl(\|V\|_{2p}\|T\|_{2p}\bigr)^p.
\tag{4.14}
\]

所有右端 \(2p\)-范数都已经完成：先用 (1.1) 在指数 \(2p\) 得到 \(T\)，再用 (3.23) 在指数 \(2p\) 得到 \(V,Z\)。于是
\[
\boxed{
\begin{aligned}
\frac d{dt}\|X\|_p^p+c_{n,p}D^T_{1,p}
\le C_{n,p,K,L}\bigl[
1+\|X\|_p^p
+\|T\|_{2p}^{2p}
+\|V\|_{2p}^{2p}
+\|Z\|_{2p}^{2p}
\bigr].
\end{aligned}}
\tag{4.15}
\]
因此
\[
\sup_{\tau\le t<T_*}\|\nabla T(t)\|_p<\infty
\qquad(\forall p<\infty).
\tag{4.16}
\]

注意：这里使用已完成层次的 \(2p\)-范数是合法的；被禁止的是在当前 \((V,Z)\) 对的同一指数方程中要求未知 \(Z\in L^{2p}\)。

---

# 5. 四项风险的最终判定

### 1. 是否除以 \(\chi\)？

**没有。**

使用的是全局无除法恒等式
\[
B_1=2\chi C_1,\qquad
|B_1|^2\le4a|C_1|^2,
\]
\[
aT_1=U_1-B_1T,\qquad
aT=U,\qquad
a\Rm=U-aG.
\]
不能把这些写成 \(T=U/\chi^2\) 或 \(\chi E=\Ric(U)/\chi\)。

### 2. 是否需要无权逐点 \(T\)？

**不需要。**

只需要由 (1.1) 得到的
\[
T\in L^q\quad\text{对所有有限 }q.
\]
凡是曲率作为当前变量的系数出现时，均有权重 \(aT=U\) 或
\(a\Rm=U-aG\)，因而有界。无权 \(T\) 只以 Hölder forcing 因子出现。

### 3. 是否引入正则化参数比值？

**精确流中没有任何正则化参数。**

若与 Step 45 的 \(b=\chi^2+\varepsilon^2\) 账本比较，只使用
\[
\frac{\chi^2}{b}\le1,\qquad \frac{|db|^2}{b}\le4|d\chi|^2,
\]
不出现负幂 \(\varepsilon^{-1}\)，更无 \(\varepsilon/\nu\) 比值。Step 56 的标量粘性属于起始定理，不进入本正时间延拓层。

### 4. 小 \(\chi\) collar 是否失效？

**不失效。**

所有需要用耗散吸收的导数项都带有恰好一个 \(\chi\)：
\[
\chi C_1\nabla V,\quad
\chi C_1\nabla X,\quad
\chi ZU\nabla P(V),\quad
\chi ZT\nabla P(X).
\]
Young 后与
\[
\int\chi^2|\nabla V|^2|V|^{p-2},
\qquad
\int\chi^2|\nabla X|^2|X|^{p-2}
\]
精确配对。没有留下裸的 \(|\nabla V|\) 或 \(|\nabla X|\) 项。若最高 cutoff 项是裸 \(C_3\) 而非 \(\chi C_3\)，该机制才会在 collar 上失败；实际 \(\nabla^3(\chi^2)\) 的最高单 jet 始终是 \(2\chi C_3\)。

---

# 6. 对 Step 40/44/45 的必要修正

1. **Step 44 的 \(T_0\) 能量种子不可省略。**  
   \(|U|\) 有界不能代替无权 \(T\in L^q\)。

2. **统一使用坐标时间。**  
   对 \(m=1\)，原始 cutoff-jet 方程精确为
   \[
   \partial_tC_2=-(\partial_t\Gamma)*C_1=U_1*C_1
   \]
   （忽略固定收缩符号）。Step 40 中的 \(U_0*C_2\) 只能解释为范数和体积元变化，不是 \(C_2\) 的原始坐标演化项。

3. **必须整体处理 \(\nabla((B_1B_1)T)\)。**  
   若孤立估计 \(B_1B_1T_1\)，会制造虚假的 \(T_1\) 循环；正确组合是 (3.5)–(3.6)。

4. **\(\nabla^3a*T\) 必须先展开。**  
   只对 \(2\chi C_3*T\) 积分分部；\(C_1C_2T\) 直接 Hölder。盲目积分整个 \(\nabla(\nabla^2a)\) 会产生无 \(\chi\) 的导数项，确实在小-\(\chi\) collar 上不可吸收。

5. **不应让常数依赖 \(\|C_2\|_\infty\) 或 \(\|C_3\|_\infty\)。**  
   虽然固定光滑 \(\chi\) 形式上使这些量有限，但该耦合机制的实质正是通过 signed IBP 只使用 \(\|d\chi\|_\infty\) 和当前有限 \(L^p\) 范数。依赖高阶 cutoff 的逐点界会掩盖并破坏所需的 continuation/regularization 结构。

综上，最早的正时间延拓层严格闭合为
\[
\boxed{
T_0\in\bigcap_{q<\infty}L^q
\ \Longrightarrow\
(U_1,C_2)\in\bigcap_{q<\infty}L^q
\ \Longrightarrow\
T_1\in\bigcap_{p<\infty}L^p.}
\]
这只验证导数传播接口，不包含起始/重启定理，也不单独证明完整终端延拓。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 61,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step61_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step61_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently reconstruct the shifted-curvature evolution for the exact fixed-cutoff flow in dimension four, with a=chi^2, G=g\owedge g/[2(n-1)], T=Rm+G, U=aT, and g_t=-2a(Ric+g)=-2 Ric(U). Read the listed notes. Determine the correct star-contraction base equations, enforcing the exact stationarity test T=U=0 (hyperbolic Einstein data) for arbitrary chi. Then assess Step 60's all-order induction after deleting any fictitious a·1 or a^2 forcing: which derivative families remain, whether any missing family appears, and whether the proof must start at m=2 from the separately established T0,T1,U1,C2 base rather than at m=1. Check the same-exponent residual estimate, time/spatial commutator derivative ordering, fixed-background C-infinity endpoint, and autonomous time-jet splice. Identify any further load-bearing flaw with an explicit term or explain why the corrected hierarchy closes. Produce a direct mathematical memo, not procedural commentary.

## Integrated Scientific Memo

# 数学核验备忘录：四维固定截断流的移位曲率层级

令
\[
a=\chi^2,\qquad
G=\frac{g\owedge g}{2(n-1)}=\frac{g\owedge g}{6},\qquad
T=\Rm+G,\qquad U=aT,
\]
并考虑
\[
\partial_tg=-2a(\Ric_g+g)=-2\Ric(U).
\]
这里 \(\chi\) 在坐标时间中固定。

## 1. 精确基础方程与驻定性检验

按给定 Kulkarni–Nomizu 约定，
\[
\Ric(G)=g,\qquad \Ric(T)=\Ric_g+g=:E,\qquad \Ric(U)=aE.
\]
因此 \(T=0\) 等价于
\[
\Rm=-G,\qquad \Ric=-g,\qquad E=0,
\]
从而对任意 \(\chi\) 都有 \(g_t=0\)。故 \(T=U=0\) 必须是精确驻定解。

由全协变 Riemann 张量的变分公式、第二 Bianchi 恒等式及 \(\partial_tG\) 的代数项，可得正确的星收缩方程
\[
\boxed{
(\partial_t-a\Delta)T
=(\nabla a)*\nabla T+(\nabla^2a)*T
+a\bigl(T*T+G*T\bigr).}
\tag{1}
\]
由于 \(G\) 平行，最后一项也可简写为 \(a(T*T+T)\)，但这里的 \(T\) 表示某个固定的 \(G*T\) 线性收缩，而不是常数项。

乘以 \(a\)，再使用
\[
\Delta(aT)=a\Delta T+2\nabla a*\nabla T+(\Delta a)T,
\qquad
\nabla U=a\nabla T+(\nabla a)*T,
\]
得到
\[
\boxed{
(\partial_t-a\Delta)U
=(\nabla a)*\nabla U+(\nabla^2a)*U
+\bigl((\nabla a)*(\nabla a)\bigr)*T
+U*U+aG*U.}
\tag{2}
\]
对 \(a=\chi^2\)，有精确因子恒等式
\[
\boxed{
\bigl((\nabla a)*(\nabla a)\bigr)*T
=4(\nabla\chi*\nabla\chi)*U.}
\tag{3}
\]

这些方程在 \(T=U=0\) 时逐项为零。因此 Step 60 中的
\[
a\cdot1,\qquad a^2
\]
不是实际张量演化项，必须删除；它们最多只能在 Young 不等式之后作为能量估计中的常数包络出现。

相应地还必须删除：

- \(T\)-族中来自 \(a\cdot1\) 的孤立 \(B_m\)；
- \(U\)-族中来自 \(a^2\) 的 \(\nabla^m(a^2)\)。

其中 \(B_j=\nabla^ja\)。

---

## 2. 修正后的导数族

记
\[
T_m=\nabla^mT,\qquad U_m=\nabla^mU,\qquad
C_j=\nabla^j\chi,\qquad B_j=\nabla^ja.
\]

修正后的 \(T_m\) 族为
\[
\begin{array}{lll}
\mathrm{(T1)}&a\Delta T_m,\\
\mathrm{(T2)}&B_r*T_{m+2-r},&1\le r\le m+2,\\
\mathrm{(T3)}&B_r*T_i*T_j,&r+i+j=m,\quad B_0=a,\\
\mathrm{(T4)}&B_\ell*\nabla^r\Rm*T_s,
&\ell+r+s=m,\\
\mathrm{(T5)}&U_{r+1}*T_s,&r+s=m-1,\\
\mathrm{(T6)}&B_r*T_{m-r},&0\le r\le m.
\end{array}
\tag{4}
\]
(T6) 来自 \(aG*T\)，不再含孤立 \(B_m\)。

修正后的 \(U_m\) 族为
\[
\begin{array}{lll}
\mathrm{(U1)}&a\Delta U_m,\\
\mathrm{(U2)}&B_r*U_{m+2-r},&1\le r\le m+2,\\
\mathrm{(U3)}&C_{r+1}*C_{s+1}*U_t,&r+s+t=m,\\
\mathrm{(U4)}&U_i*U_j,&i+j=m,\\
\mathrm{(U5)}&B_\ell*\nabla^r\Rm*U_s,
&\ell+r+s=m,\\
\mathrm{(U6)}&U_{r+1}*U_s,&r+s=m-1,\\
\mathrm{(U7)}&B_r*U_{m-r},&0\le r\le m.
\end{array}
\tag{5}
\]
(U7) 来自 \(aG*U\)，不再含 \(\nabla^m(a^2)\)。

若要求逐字面枚举每个经重排产生的单项式，还应注明时间交换子重排会生成
\[
T_q*U_{r-q}*T_s,
\qquad
T_q*U_{r-q}*U_s,
\qquad
q\le r-1,\quad r+s=m-1,
\tag{6}
\]
以及可能的迭代低阶版本。这不是新的当前阶族，因为
\[
q\le m-2,\qquad r-q\le m-1,\qquad s\le m-1.
\]
保留有序协变导数时甚至无需显式引入这些项。

另一个小的记号精度是：若 (T4)/(U5) 被理解为字面上的 \([\nabla^k,\Delta]\) 项，则应有 \(\ell\le m-1\)；允许 \(\ell=m\) 只是加入一个普适系数为零的模式，不影响估计。

没有遗漏新的当前阶族。

---

## 3. 两个防止层级失去三角性的恒等式

空间交换子的危险配置由
\[
\boxed{
aT_m=U_m-\sum_{q=1}^m B_q*T_{m-q}}
\tag{7}
\]
消除。例如
\[
aT_m*U_0
=U_m*U_0-\sum_{q=1}^mB_q*T_{m-q}*U_0.
\tag{8}
\]
因此 \(U_m\) 方程中不会出现尚未控制的裸 \(T_m\)。

其他当前项的系数同样有界：
\[
a\Rm=U_0-aG,\qquad
aT_m*T_0=U_0*T_m,\qquad
a\Rm*T_m=(U_0-aG)*T_m.
\tag{9}
\]
这里仅需终端时间片上的 \(\|U_0\|_\infty\) 控制。

---

## 4. 时间交换子与截断函数导数次序

一般张量满足
\[
[\partial_t,\nabla^m]A
=\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^sA,
\tag{10}
\]
且
\[
\partial_t\Gamma
=g^{-1}*\nabla\Ric(U)=g^{-1}*U_1.
\tag{11}
\]
因此未重排的最高项为 \(U_{r+1}*A_s\)，在第 \(m\) 层最多达到 \(U_m\)，不出现 \(U_{m+1}\)。

对截断函数必须利用一个额外事实：\(\chi\) 是固定标量，所以
\[
\partial_t(d\chi)=0.
\]
不能把一般张量交换子公式机械地用于 \(\nabla^{m+1}\chi\)，否则会虚假地产生 \(U_{m+1}\)。应写
\[
C_{m+1}=\nabla^m(d\chi),
\]
于是
\[
\boxed{
\partial_t C_{m+1}
=U_m*C_1+
\sum_{1\le j<m}U_j*C_{m+1-j}
+\mathcal R_m,}
\tag{12}
\]
其中 \(\mathcal R_m\) 只含严格低阶曲率及截断导数。特别地，不出现
\[
U_{m+1}\quad\text{或}\quad C_{m+2}.
\]

空间交换子
\[
[\nabla^k,\Delta]A
=\sum_{r+s=k}\nabla^r\Rm*\nabla^sA
\tag{13}
\]
中，若先有 \(\ell\ge1\) 个导数落在 \(a\) 上，则 \(r+s=m-\ell\le m-1\)，故均为先前层 forcing；只有 \(\ell=0\) 可能到当前阶，而其危险项已由 (7)–(9) 处理。

---

## 5. 同指数残差估计与正确起始层

令
\[
V=U_m,\qquad Z=C_{m+1},\qquad
D^U_{m,p}=\int a|\nabla V|^2|V|^{p-2}.
\]
主要系数项满足：

1. \(B_1*U_{m+1}=2\chi C_1*\nabla V\) 可由加权 Young 吸收到 \(D^U_{m,p}\)；
2. \(B_2*V\) 必须按带符号 Hessian 项积分一次：
   \[
   \left|\int(\nabla_i\nabla_ja)\,\mathcal B^{ij}(V)\right|
   \le \varepsilon D^U_{m,p}
   +C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p.
   \tag{14}
   \]
   这不需要 \(\|C_2\|_\infty\)。

由
\[
B_{m+2}
=2\chi C_{m+2}
+\sum_{i=1}^{m+1}C_i*C_{m+2-i},
\tag{15}
\]
唯一的新截断 jet 是 \(2\chi C_{m+2}*U_0\)。只对其中的 \(\chi C_{m+2}\) 部分积分一次；不可盲目积分整个 \(B_{m+2}\)。所得关键残差为
\[
I_m=\int\chi|Z|\,|U_1|\,|V|^{p-1}.
\tag{16}
\]
在四维，令 \(f=\chi|V|^{p/2}\)，则
\[
I_m
\le \|f\|_4\|Z\|_p\|U_1\|_4
\|V\|_p^{p/2-1},
\tag{17}
\]
因为
\[
\frac14+\frac1p+\frac14+\frac{p/2-1}{p}=1.
\]
而
\[
\|f\|_4^2
\le C_S\left(p^2D^U_{m,p}
+C_{p,\chi}\|V\|_p^p\right).
\tag{18}
\]
故
\[
I_m\le \varepsilon D^U_{m,p}
+C_{m,p,\tau}\bigl(1+\|Z\|_p^p+\|V\|_p^p\bigr).
\tag{19}
\]
当前未知量始终保持在同一指数 \(p\)，没有 \(2p\) 型当前阶要求。

但是该论证要求 \(\|U_1\|_4\) 已是先前层数据。因此统一归纳不能从 \(m=1\) 开始：当 \(m=1\) 时 \(U_1=V\)，(17) 对当前未知量循环使用。首层必须使用 Step 56 的专门带符号 Hessian 论证。

严格的顺序应为
\[
\boxed{
T_0
\longrightarrow (U_1,C_2)
\longrightarrow T_1,
}
\tag{20}
\]
然后仅对 \(m\ge2\) 使用统一步骤
\[
\boxed{
(U_m,C_{m+1})\longrightarrow T_m.
}
\tag{21}
\]

完成当前对后，\(T_m\) 方程中顶阶截断项积分后只留下
\[
C_{m+1},\quad T_0,\quad T_1,\quad \nabla T_m,
\]
以及已知的有限指数乘积；时间交换子项 \(U_m*T_0\) 也已成为 forcing。由先前层“所有有限 \(q\)”的控制，可为这些乘积选择足够大的有限 Hölder 指数。因此
\[
\frac d{dt}\|T_m\|_p^p+cD^T_{m,p}
\le C_{m,p,\tau}(1+\|T_m\|_p^p).
\tag{22}
\]

---

## 6. 固定背景的 \(C^\infty\) 终点

取 \(\bar g=g(\tau)\)，记
\[
A=\nabla^{g(t)}-\bar\nabla.
\]
有
\[
\partial_tA=g^{-1}*U_1.
\tag{23}
\]
将 \(\bar\nabla\) 与 \(\nabla^{g(t)}\) 相互转换并按阶归纳，\(\bar\nabla^k\partial_tA\) 的最高源项是 \(U_{k+1}\)，其余只含较低阶 \(A\)、\(U\) 及 \(g^{-1}\)。选择足够大的有限 \(p>4\)，利用完整内禀层级和 Sobolev 嵌入，可得所有固定背景导数的统一控制。

又因为
\[
\nabla g=0,\qquad \bar\nabla g=A*g,
\]
所有 \(\bar\nabla^kg\) 均有界。此外
\[
\partial_tg=-2\Ric(U)
\]
以及完整 \(U\)-层级给出，对每个 \(s\),
\[
\sup_{\tau\le t<T_*}
\|\partial_tg(t)\|_{H^s(\bar g)}<\infty.
\tag{24}
\]
因此 \(g(t)\) 在每个 \(H^s(\bar g)\) 中关于时间 Lipschitz，故
\[
g(t)\to g_*
\quad\text{于 }C^\infty(M),\qquad t\uparrow T_*.
\tag{25}
\]
正定性由
\[
|g_t|_g\le C|U|_g
\]
及有限时间片上的 \(\|U\|_\infty\) 控制所给出的双边指数度量比较保持。

这里不需要 Step 60 (5.2) 中额外的 \(B_0*A_m\) 作为独立结构；任何这类写法都应被理解为背景/移动联络转换产生的低阶有界系数项。真正的最高阶源是 \(U_{m+1}\)。

---

## 7. 自治方程的时间 jet 拼接

设
\[
\mathcal F(g)=-2\chi^2(\Ric_g+g),
\qquad
\mathcal F_1=\mathcal F,\qquad
\mathcal F_{\ell+1}(g)
=D\mathcal F_\ell(g)[\mathcal F(g)].
\tag{26}
\]
每个 \(\mathcal F_\ell\) 只依赖 \(g\) 的有限空间 jet 及固定函数 \(\chi\)。旧解满足
\[
\partial_t^\ell g(t)=\mathcal F_\ell(g(t)),
\]
故由 \(C^\infty\) 收敛，
\[
\partial_t^\ell g(t)\to\mathcal F_\ell(g_*)
\quad\text{于 }C^\infty.
\tag{27}
\]
任何从 \(g_*\) 出发的光滑局部重启解 \(\widehat g\) 都满足
\[
\partial_s^\ell\widehat g(0)=\mathcal F_\ell(g_*).
\tag{28}
\]
于是旧解、\(g_*\) 与重启解的全部混合时空 jet 在 \(T_*\) 匹配，分段拼接为光滑解。此论证完全不需要重叠区上的非规范 Ricci 流唯一性。

---

## 8. 结论与剩余依赖

删除虚假的 \(a\cdot1\) 与 \(a^2\) 后：

- 导数族仅失去孤立 \(B_m\) 和 \(\nabla^m(a^2)\)；
- 不出现新的当前阶族；
- 规范重排只增加严格低阶乘积；
- 统一归纳必须从 \(m=2\) 开始；
- 四维同指数残差估计、时间/空间交换子次序、固定背景 \(C^\infty\) 终点及自治时间-jet 拼接均成立。

闭合真正依赖的外部输入是：

1. Step 56 已单独建立
   \[
   T_0,\ U_1,\ C_2,\ T_1\in L^q
   \quad\forall q<\infty;
   \]
2. 正时间终端片上的 \(\|U\|_\infty\)、双 Lipschitz 度量及 Sobolev 常数控制；
3. 每个光滑正定终点度量的局部存在性。

未发现进一步破坏层级的显式项。最容易误读、但实际承重的两点是：

- \(\partial_t(d\chi)=0\)，使截断 jet 方程的最高项是 \(U_m*C_1\)，不是 \(U_{m+1}\)；
- 只对 \(2\chi C_{m+2}\) 部分积分，不能对整个 \(\nabla^{m+2}(\chi^2)\) 盲目积分。

因此，经上述修正后，Step 60 的四维全阶延拓层级在其陈述的正时间片假设下闭合。
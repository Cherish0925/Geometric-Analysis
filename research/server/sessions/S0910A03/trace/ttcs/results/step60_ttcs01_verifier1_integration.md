# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 60,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step60_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step60_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Audit the continuation mechanism for the exact degenerate geometric flow ∂_t g=-2χ²(Ric_g+g), focusing on the two disputed points. First, determine whether the coordinate-time derivative-family enumeration (T1–T6 and U1–U7) in step45, combined with the signed integrations and Step59/A01 Step55 residual estimate, genuinely exhausts every commutator and gives the arbitrary finite-order L^p induction for the exact case b=χ². Identify any missing current-level or unweighted coefficient, with an explicit derivative allocation if one exists. Second, assess uniqueness: is A01 Step56's proposed direct estimate d/dt∫|g1-g2|²≤C∫|g1-g2|² valid for the geometric Ricci-type equation without fixing diffeomorphism gauge? Account for diffeomorphism invariance and the actual principal symbol. If invalid, decide whether the all-order energy route can instead yield a smooth terminal metric and a direct smooth splice/restart without overlap uniqueness, and state the precise time-regularity/matching needed. Give a mathematical memo, not process advice.

## Integrated Scientific Memo

# 数学审计备忘录

设
\[
a=\chi^2,\qquad
T=\Rm+\frac{g\owedge g}{2(n-1)},\qquad U=aT,
\qquad
\partial_tg=-2\Ric(U).
\]

## 一、T1–T6、U1–U7 是否闭合

### 结论

在 Step45 所采用的 **star-contraction 结构层面**，这些族确实穷尽了由 Leibniz 法则、空间交换子和坐标时间交换子产生的导数类型；未发现遗漏的当前层对象，也未发现无法处理的裸 \(T_m\) 或裸 \(T_0\) 当前系数。结合有符号 Hessian 分部积分及 Step59/A01 Step55 的残差估计，可得到精确情形 \(a=\chi^2\) 的任意有限阶 \(L^p\) 三角归纳。

但这仍不是逐指标的穷尽证明：现有材料没有逐项展开所有槽位排列和 Ricci 交换余项。脚本只验证导数预算，不能替代这一 tensor-level lemma。

### 1. 两类交换子均已计入

坐标时间微分满足
\[
\partial_t(\nabla^mA)
=\nabla^m(\partial_tA)
+\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^sA,
\qquad
\nabla^r(\partial_t\Gamma)=U_{r+1}*g^{-1},
\]
而
\[
[\nabla^m,\Delta]A
=\sum_{r+s=m}\nabla^r\Rm*\nabla^sA .
\]
因此 T4/U5 是空间交换子，T5/U6 是时间交换子。重新排列导数时产生的额外曲率因子阶数严格降低；在时间交换子中，典型余项为
\[
T_\alpha*U_{\beta+1}*A_s,
\qquad \alpha+\beta\le r-1,
\]
故在第 \(m\) 阶至多出现 \(T_{m-2}\)，属于先前已完成层，不会产生裸 \(T_m\) 系数。

### 2. \(T_m\) 方程中没有遗漏的裸当前系数

由
\[
\partial_tT
=a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T+1)
\]
微分 \(m\) 次，正好得到 T1–T6。

当前 \(T_m\) 的二次项和空间交换子系数分别为
\[
aT_0=U_0,\qquad
a\Rm=U_0-aG,
\]
均有界。唯一含裸 \(T_0\) 的最高时间交换子是
\[
U_m*T_0.
\]
它不是乘在当前 \(T_m\) 上的点态系数，而是在完成
\((U_m,C_{m+1})\) 后处理 \(T_m\) 时的 forcing。零阶有符号 Hessian 能量已经给出
\[
T_0\in L^\infty_tL_x^q\qquad\forall q<\infty,
\]
所以用有限指数 Hölder 即可。

最高 cutoff 项
\[
2\chi C_{m+2}*T_0
\]
分部积分后产生
\[
C_1*C_{m+1}*T_0*P(T_m),\quad
\chi C_{m+1}*T_1*P(T_m),\quad
\chi C_{m+1}*T_0*\nabla P(T_m).
\]
其中 \(m=1\) 的中项是当前有符号 Hessian 项；\(m\ge2\) 时 \(T_1\) 已属于先前层。没有新的当前量。

### 3. \(U_m\) 方程中两个看似致命的分配都可精确消除

结构方程为
\[
\partial_tU
=a\Delta U+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+aU+a^2 .
\]

#### (a) U3 的当前 \(T_m\)

极端分配
\[
B_1*B_1*T_m
=4\chi^2(C_1*C_1)*T_m
\]
不能丢掉 \(\chi^2\)。利用
\[
aT_m
=U_m-\sum_{q=1}^m B_q*T_{m-q},
\]
得到
\[
B_1*B_1*T_m
=4(C_1*C_1)\left(
U_m-\sum_{q=1}^mB_q*T_{m-q}
\right).
\]
故当前项只是有界系数 \(C_1*C_1\) 乘 \(U_m\)，其余全是先前 \(T\)-层。这里若误写成 \(C_1*C_1*T_m\)，归纳确会失效。

在精确情形还可直接先化简
\[
(B_1*B_1)*T=4(C_1*C_1)*U,
\]
再微分；这立即显示该族只产生
\[
C_1*C_1*U_m,\qquad C_{m+1}*C_1*U_0
\]
等当前项，不产生裸 \(T_m\)。

#### (b) U5 的当前空间交换子

极端分配为
\[
aT_m*U_0.
\]
同一恒等式将其化为
\[
U_m*U_0-\sum_{q=1}^mB_q*T_{m-q}*U_0.
\]
因此也没有尚未完成的 \(T_m\) 依赖。

### 4. cutoff jet 方程没有更高当前量

对固定标量 \(\chi\)，
\[
\partial_tC_{m+1}
=U_m*C_1+\sum_{1\le j<m}U_j*C_{m+1-j}
+\text{低阶曲率交换余项}.
\]
唯一当前项是 \(U_m*C_1\)；没有 \(U_{m+1}\) 或 \(C_{m+2}\)。范数和体积元变化只添加有界的 \(U_0|C_{m+1}|^p\)。

### 5. 当前残差确实闭合

令
\[
V=U_m,\quad Z=C_{m+1},\quad
D_{m,p}=\int\chi^2|\nabla V|^2|V|^{p-2}.
\]
最高 cutoff 项 \(\chi C_{m+2}*U_0\) 一次分部积分后的实质残差为
\[
I_{\rm res}
=\int\chi |Z|\,|U_1|\,|V|^{p-1}.
\]
在四维令 \(f=\chi|V|^{p/2}\)，则
\[
I_{\rm res}
\le \|f\|_4\|Z\|_p\|U_1\|_4\|V\|_p^{p/2-1},
\]
且
\[
\|f\|_4^2
\le C\bigl(p^2D_{m,p}+C_{\chi,p}\|V\|_p^p\bigr).
\]
Young 不等式给出
\[
I_{\rm res}\le
\varepsilon D_{m,p}
+C_{m,p,\tau}
\bigl(1+\|Z\|_p^p+\|V\|_p^p\bigr).
\]
所以当前 cutoff jet 只需 \(L^p\)，没有 \(p\mapsto2p\) 的当前层指数升级。一般 \(n>2\) 可相应用
\(H^1\hookrightarrow L^{2n/(n-2)}\) 和先前层 \(U_1\in L^n\)；\(n=2\) 取任意有限 Sobolev 指数。

最终得到
\[
\frac d{dt}
\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
+cD_{m,p}
\le
C\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr),
\]
随后
\[
\frac d{dt}\|T_m\|_p^p+cD^T_{m,p}
\le C(1+\|T_m\|_p^p).
\]
因此
\[
T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots
\]
在每个固定有限阶、每个有限 \(p\) 上闭合。

需要补写的严格对象是：从坐标公式出发，逐指标证明所有导数项都落入 T1–T6/U1–U7，并证明每个重排余项满足上述严格降阶规则。现有证据支持该结论，但尚未构成该逐指标 lemma。

---

## 二、无 gauge 的直接 \(L^2\) 唯一性估计无效

A01 Step56 所声称的
\[
\frac d{dt}\int|g_1-g_2|^2
\le C\int|g_1-g_2|^2
\]
不能由其给出的论证推出。

Ricci 线性化的二阶部分不是单纯 \(-\frac12\Delta_Lh\)。对
\[
F(g)=-2a(\Ric_g+g),
\]
有
\[
DF_g(h)
=a\bigl(
\Delta h+\nabla^2\tr h
-2\,\sym\nabla(\div h)
\bigr)+\text{低阶}.
\]
其主符号为
\[
\sigma_\xi(DF)(h)_{ij}
=a\left(
-|\xi|^2h_{ij}
-\xi_i\xi_j\tr h
+\xi_i\xi^kh_{kj}
+\xi_j\xi^kh_{ki}
\right).
\]
它在微分同胚方向
\[
h=\xi\odot v
\]
上有核；\(\nabla^2\tr h\) 和 \(\nabla\div h\) 是主阶 gauge 项，不能列入“低阶”。其 \(L^2\) 二次型也不满足
\[
\langle\sigma_\xi(DF)h,h\rangle
\le -c\,a|\xi|^2|h|^2+C|h|^2.
\]
例如在 \(a=1\) 的平坦区域取 \(\xi=e_1\) 和高频
\[
h=\diag(1,-\varepsilon,0,\ldots,0)e^{ikx^1},
După 0<\varepsilon<1,
\]
主贡献可为正且按 \(k^2\) 增长。因此不存在频率无关的常数 \(C\) 支持上述直接 Grönwall 估计。

这里应区分两点：

* 方程的几何协变性意味着其 Ricci 主符号具有 gauge 退化；
* 固定空间函数 \(\chi\) 使时间依赖 diffeomorphism 不再自动保留同一个固定系数，因而“任意 pullback 都是解”不是准确表述。但这并不会消除 Ricci 主符号的 gauge 核，也不会使未经 gauge fixing 的差分能量变成强抛物型。

因此从较早时刻 \(t_j<T^*\) 重启，再靠该 \(L^2\) 估计证明新旧解在重叠区相同，是不成立的。

---

## 三、无需重叠唯一性的终端拼接

可以改为在 \(T^*\) 本身拼接，但必须得到真正的光滑终端度量，而不仅是有限阶弱极限。

若全阶能量和固定背景连接转换给出，对每个 \(k\),
\[
\sup_{t<T^*}\|\partial_tg(t)\|_{C^k}<\infty,
\]
则有限时间区间上
\[
g(t)\longrightarrow g_*
\quad\text{于 }C^\infty(M)
\]
且 bilipschitz 控制保证 \(g_*>0\)。

写
\[
\mathcal F(g)=-2\chi^2(\Ric_g+g).
\]
由空间 \(C^\infty\) 收敛，
\[
\partial_tg(t)=\mathcal F(g(t))
\longrightarrow\mathcal F(g_*)
\quad\text{于 }C^\infty.
\]
递归定义
\[
\mathcal F_1=\mathcal F,\qquad
\mathcal F_{\ell+1}(g)
=D\mathcal F_\ell(g)[\mathcal F(g)].
\]
每个 \(\mathcal F_\ell\) 都只依赖 \(g,\chi\) 的有限空间 jet，故
\[
\lim_{t\uparrow T^*}\partial_t^\ell g(t)
=\mathcal F_\ell(g_*)
\quad\forall\ell.
\]

从 \(g_*\) 取任意一个同方程的光滑局部重启解 \(\hat g(s)\)。它满足
\[
\partial_s^\ell\hat g(0)=\mathcal F_\ell(g_*).
\]
于是
\[
\widetilde g(t)=
\begin{cases}
g(t),&t<T^*,\\
g_*,&t=T^*,\\
\hat g(t-T^*),&t>T^*
\end{cases}
\]
的所有左右时间 jets 一致，是穿过 \(T^*\) 的光滑解，无需任何重叠唯一性。

### 所需的精确正则性

最干净且足够的条件是：

1. \(g(t)\to g_*\) 于空间 \(C^\infty\)；
2. \(g_*\) 正定；
3. 对每个 \(\ell\)，左侧时间导数存在并满足
   \[
   \partial_t^\ell g(T^{*-})=\mathcal F_\ell(g_*).
   \]

第 3 条可由第 1 条和方程递归推出；实践中可用全阶空间估计和
\(\partial_tg=\mathcal F(g)\) 获得。

仅有 Step59 的有限 \(H^7\) 有界性、\(H^5\) 时间 Lipschitz 收敛，并不足以宣称一个 \(C^\infty\) 拼接。它可支持有限正则性的弱延拓，但若“最大分支”定义为光滑解，则需要：

* 要么完成所有阶的统一终端估计，得到上述 \(C^\infty\) 匹配；
* 要么建立一个有限正则性局部理论，并证明有限正则性拼接随后在退化方程中恢复到所需光滑性；现有材料没有给出这种退化 Schauder bootstrap。

所以正确的延拓路线是：用任意阶 \(L^p\) 塔和固定背景转换证明 \(C^\infty\) 终端收敛，在终端数据处直接重启并按 PDE 生成的全部时间 jets 拼接。此前“从 \(t_j\) 重启并用无 gauge 的 \(L^2\) 唯一性粘合”的论证应删除。
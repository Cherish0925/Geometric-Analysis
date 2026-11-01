# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step32_preceptor_analytic_review.md",
    "Sessions/S0910A01/workspace/notes/step31_general_p_tensor_power_inequality.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Independently verify the restored weighted-flow analysis in Step 34. Focus on four load-bearing points: (i) whether the Sobolev convention and collapse cancellation are now correct; (ii) whether the nested-time mixed recurrence and endpoint time powers in equations (4.2)-(4.9) follow from the cited energy structure, identifying any missing factors or circular use of Y, J6, or moving Sobolev control; (iii) whether direct J6 absorption via the unweighted L2 curvature coefficient in (4.10) is mathematically plausible from the exact defect equation, and what exact tensor/Kato calculation remains; (iv) whether the evolving cutoff-Hessian discussion and proposed base coupled estimate correctly isolate the m=2 continuation issue. Give corrected formulas where needed and sharply distinguish derived consequences from open estimates. Do not infer any pinching-gap theorem.

## Output

# Step 34 加权流分析核验备忘

## 总体结论

Step 34 对 Sobolev 系数的修正是正确的；塌缩体积在临界吸收参数与缺陷端点中确实消去。混合插值给出的指数映射 \(p\mapsto 3p/2\) 以及 \(t^{-3/p_0}\) 时间幂也正确。

但式 (4.2)–(4.5) 需要把式 (4.3) 中的 \(L^1_t\) 平均系数改成点态时间上界。单凭
\(\int_I\mathcal S^2Y\) 不能得到展示的全 \(p\) 递推；现有的
\(\mathcal S^2Y(s)\lesssim\gamma^3/s\) 点态估计恰好能够修复这一处。另一个实质性空缺是：一般 \(p\) 的完整张量能量不等式和正则化 \(J_6\) 不等式尚未逐项写出。给定这些不等式后，(4.6)、(4.8)、(4.9) 的幂次与体积消去成立。

式 (4.10) 本身是 Sobolev–Hölder 的直接推论，数学上可信；真正尚需完成的是证明精确缺陷方程测试后只出现这种曲率势，并且所有 \(\nabla^2a\)、移动范数与正则化项都服从同一权重。

演化 cutoff Hessian 的讨论正确。配对 \((\nabla U,\nabla^2\chi)\) 是合适的起始层，\(m=2\) 时的单个 \(\chi\) 因子确实是首个不能直接归入加权耗散的项。式 (6.6) 的主要机制正确，但应补一个零阶系数。

---

## 1. Sobolev 约定与塌缩体积消去

采用

\[
\|u\|_4^2\le \mathcal S
 \left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
\qquad
\mathcal S\asymp \frac{r^2}{\sqrt V},
\]

与四维局部 Sobolev 缩放一致。若另一符号定义为

\[
\|u\|_4\le S
\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right)^{1/2},
\]

则确实是 \(S^2=\mathcal S\)。

对 \(p=2\)，\(z_2=a^{1/2}F=\chi F\)，故

\[
K_3=\int Fz_2^2
 \le \|F\|_{L^2(U)}\|z_2\|_4^2
 \le C\mathcal S K_2^{1/2}
       \left(D_2+r^{-2}K_2\right).
\]

因此吸收参数是

\[
\gamma=\mathcal S K_2^{1/2},
\]

而不是再多乘一次 \(\mathcal S\)。若 Sobolev 不等式与 \(K_2\) 使用同一宏支撑域或体积一致可比的球，并且好中心给出 \(K_2\le K_0V\)，则

\[
\gamma\le C\frac{r^2}{\sqrt V}\sqrt{K_0V}
       =Cr^2\sqrt{K_0}.
\]

这里的体积消去完全正确。域的匹配很重要：若 Sobolev 系数使用一个球的体积，而 \(K_2\) 使用体积比不可控的另一个区域，则还会留下体积比。

归一化平均式也正确：

\[
\langle |u|^4\rangle_V^{1/2}
 \le Cr^2\left(
 \langle|\nabla u|^2\rangle_V+r^{-2}\langle u^2\rangle_V
 \right).
\]

不过在移动度量下，最好直接使用未归一化能量，或者始终以初始体积 \(V_0\) 表示并加入双 Lipschitz 比较因子；不能把 \(V(t)^{-1}\int h\,d\mu_t\) 当作固定分母求导。

---

## 2. 混合递推与时间幂

### 2.1 反应项确实产生 \(\mathcal S^2Y\)

从精确分解

\[
R_p=\int a^{p-1}Ff^p
\le Y^{1/3}H_p^{1/3}\|z_p\|_4^{4/3},
\qquad
Y=\int aF^3,
\]

以及

\[
\|z_p\|_4^2
 \le Cp^2\mathcal S(D_p+r^{-2}H_p),
\]

得到

\[
R_p\le
Cp^{4/3}\mathcal S^{2/3}Y^{1/3}H_p^{1/3}
(D_p+r^{-2}H_p)^{2/3}.
\]

Young 不等式于是给出

\[
pR_p\le \varepsilon D_p
 +C_{\varepsilon}p^N\mathcal S^2Y\,H_p
 +Cp^Nr^{-2}H_p.
\]

因此 Step 34 的反应系数 \(\mathcal S^2Y\) 正确。

这里仍依赖一个尚未逐项完成的一般 \(p\) 张量能量式。A01 Step 31 开头已明确指出，\(\nabla^2a\) 分部积分时导数落到
\(a^{p-2}F^{p-2}\) 的所有项尚未完整展开；Codex 文档中的式 (5.2) 是结构式，不是全部收缩项的推导。

### 2.2 式 (4.3) 需要修正

假设已经有

\[
H_p'+cD_p
 \le Cp^N\bigl(r^{-2}+1+\mathcal S_*^2Y(t)\bigr)H_p,
\tag{E\(_p\)}
\]

其中 \(\mathcal S_*=\sup_I\mathcal S(t)\)。时间截断后可直接推出

\[
\sup_{I'}H_p+\int_{I'}D_p
\le Cp^N\Lambda_p(I,I')\int_IH_p,
\]

其中应取

\[
\boxed{
\Lambda_p(I,I')
=(\tau'-\tau)^{-1}+r^{-2}+1+
 \operatorname*{ess\,sup}_{s\in I}\mathcal S_*^2Y(s).}
\tag{2.1}
\]

Step 34 式 (4.3) 中

\[
|I|^{-1}\|\mathcal S^2Y\|_{L^1(I)}
\]

不能一般性替代这个本质上确界。原因是能量项为
\(\int_I(\mathcal S^2Y)H_p\)，时间平均并不控制它，除非另有 \(H_p\) 与系数的相关控制。用 Gronwall 处理只给出

\[
\exp\!\left(Cp^N\int_I\mathcal S^2Y\right),
\]

这种 \(p\)-依赖不适合展示的无限次迭代。

现有点态估计正好提供所需修复：

\[
\mathcal S_*^2Y(s)\le \frac{C\gamma^3}{s}.
\]

在 \(I_t=[t/2,t]\) 上，

\[
\operatorname*{ess\,sup}_{I_t}\mathcal S_*^2Y
\le \frac{C\gamma^3}{t}.
\]

因此一般 \(p\) 递推不需要仅依赖式 (4.4) 的时间积分；它使用更强的式 (3.3)。这个 \(Y\) 估计来自固定 \(q=2,3\) 能量，而不使用一般 \(p\) Moser，因而没有逻辑回返。

### 2.3 混合递推和指数和

逐时有

\[
H_{3p/2}
\le H_p^{1/2}\|z_p\|_4^2.
\]

结合上面的时间截断能量式，

\[
\int_{I'}H_{3p/2}
\le Cp^N\mathcal S_*
\left[\Lambda_p(I,I')\int_IH_p\right]^{3/2}.
\tag{2.2}
\]

这就是式 (4.2) 的正确版本。令 \(p_{k+1}=\frac32p_k\)，则迭代中

\[
\sum_{k\ge0}\frac1{p_k}=\frac3{p_0},
\qquad
\sum_{k\ge0}\frac1{p_{k+1}}=\frac2{p_0}.
\]

所以 \(\mathcal S_*\) 的总幂为 \(2/p_0\)，时间截断的总幂为 \(3/p_0\)。更完整的端点式是

\[
\boxed{
\|af\|_{L^\infty(\text{末端子区间})}
\le C\mathcal S_*^{2/p_0}
\Lambda_t^{3/p_0}
\left(\int_{t/2}^tH_{p_0}(f,s)\,ds\right)^{1/p_0},
}
\tag{2.3}
\]

其中

\[
\Lambda_t=t^{-1}+r^{-2}+1+\gamma^3t^{-1}.
\]

当 \(t\le c\min\{r^2,1\}\) 时，

\[
\Lambda_t\le C(\gamma,c)t^{-1},
\]

于是得到 Step 34 的

\[
\mathcal S_*^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^tH_{p_0}\right)^{1/p_0}.
\]

因此时间幂正确，但隐含了正时间短尺度条件；若不作该简化，应保留 \(\Lambda_t\)。

### 2.4 曲率与缺陷端点

曲率取 \(p_0=3\)。由

\[
\int_{t/2}^tY(s)\,ds\le C\gamma K_2(0)
\]

得到

\[
\|aF(t)\|_\infty
\le C\mathcal S_*^{2/3}t^{-1}
(\gamma K_2(0))^{1/3}.
\]

利用 \(\gamma=\mathcal S_*K_2(0)^{1/2}\)，

\[
\mathcal S_*^{2/3}
(\gamma K_2(0))^{1/3}=\gamma,
\]

故

\[
\boxed{\|aF(t)\|_\infty\le C(\gamma,\theta)\frac{\gamma}{t}.}
\]

缺陷取 \(p_0=6\)。若已经证明

\[
\sup_{0<s<T}J_6(s)\le C\delta^6V_0,
\]

则

\[
\begin{aligned}
\|aE(t)\|_\infty
&\le C\mathcal S_*^{1/3}t^{-1/2}
   (\delta^6V_0t)^{1/6}\\
&\le C\delta\,r^{2/3}t^{-1/3}
 =C\delta(r^2/t)^{1/3}.
\end{aligned}
\]

最后一步使用

\[
\mathcal S_*^{1/3}V_0^{1/6}
\le C(r^2V_0^{-1/2})^{1/3}V_0^{1/6}
=Cr^{2/3}.
\]

积分确实给出

\[
\int_0^T\|aE(t)\|_\infty\,dt
\le C\delta r^{2/3}T^{2/3}
=C\delta\theta^{2/3}r^2.
\]

这些推论仍以 \((E_p)\)、\(J_6\) 持续性以及首出区间内的 \(\mathcal S_*\) 比较为前提。

---

## 3. 直接 \(J_6\) 吸收

由给出的精确缺陷方程

\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)
\]

可见每一项都含 \(E\) 或其导数，没有纯曲率源。令

\[
\phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2},
\qquad
J_{m,\varepsilon}
=\int\eta^2a^{m-2}\phi_\varepsilon^m.
\]

所需的精确能量式应为

\[
\boxed{
\begin{aligned}
J_{m,\varepsilon}'
+c_m\!\int\eta^2a^{m-1}\phi_\varepsilon^{m-2}
 |\nabla E|^2
\le {}&
C_m(r^{-2}+1)J_{m,\varepsilon}\\
&+C_m\int\eta^2a^{m-1}F\phi_\varepsilon^m ,
\end{aligned}}
\tag{3.1}
\]

且常数与 \(\varepsilon\) 无关。

这个结构与精确方程相容：

* Lichnerowicz 代数项、移动张量范数和移动测度均由
  \(F\phi_\varepsilon^m\) 控制；
* \(\nabla^2a*E\) 项分部积分一次后，最差 cutoff 权重为
  \[
  a^{m-3}|da|^2\phi_\varepsilon^m
  =\frac{|da|^2}{a}a^{m-2}\phi_\varepsilon^m
  =4|d\chi|^2a^{m-2}\phi_\varepsilon^m;
  \]
* Kato 正则化满足
  \[
  |\nabla\phi_\varepsilon|\le|\nabla E|.
  \]

令

\[
z_{m,\varepsilon}
=\eta a^{(m-1)/2}\phi_\varepsilon^{m/2}.
\]

则

\[
\|\nabla z_{m,\varepsilon}\|_2^2
\le C_mX_{m,\varepsilon}+C_mr^{-2}J_{m,\varepsilon},
\]

并且

\[
\begin{aligned}
\int Fz_{m,\varepsilon}^2
&\le \|F\|_{L^2(U)}\|z_{m,\varepsilon}\|_4^2\\
&\le C_m\mathcal S_*\|F\|_{L^2(U)}
 \left(X_{m,\varepsilon}+r^{-2}J_{m,\varepsilon}\right)\\
&\le C_m\gamma
 \left(X_{m,\varepsilon}+r^{-2}J_{m,\varepsilon}\right).
\end{aligned}
\tag{3.2}
\]

所以式 (4.10) 作为函数不等式成立。对固定 \(m=6\)，若
\(C_6\gamma<c_6\)，便可吸收梯度项，得到

\[
J_{6,\varepsilon}'\le C(r^{-2}+1)J_{6,\varepsilon},
\]

再令 \(\varepsilon\to0\)。

尚需补出的部分是式 (3.1) 的完整张量测试：必须同时保留两个梯度正项，逐一处理 \(\mathcal C_a(E)\) 中的
\(\tau\nabla^2a\)、\((\nabla^2a)*E\)、\(da*\nabla E\)，并确认正则化没有留下与 \(E\) 无关的余项。完成这一步后，\(J_6\) 不需要先使用
\(\|aF\|_\infty\)，从而避开 \(t^{-1}\) 的零时刻积分。

---

## 4. cutoff Hessian 与 \(m=2\) 延拓项

固定标量 \(\chi\) 满足

\[
\partial_t(\nabla_i\nabla_j\chi)
=-(\partial_t\Gamma^k_{ij})\nabla_k\chi.
\]

若 \(U=a(\operatorname{Rm}+G)\)，则
\(\operatorname{Ric}(U)=aE\)，故

\[
\partial_t\Gamma=g^{-1}*\nabla(aE)
=g^{-1}*\nabla\operatorname{Ric}(U),
\]

从而

\[
\partial_t\nabla^2\chi=\nabla U*\nabla\chi
\]

在收缩记号下正确。移动 \(L^p\) 范数时还会出现
\(U*\nabla^2\chi\) 的零阶项。双 Lipschitz 比较本身不控制连接，所以不能由它推出 \(\nabla^2_{g(t)}\chi\) 的控制。

Wang 文献 Lemma 4.11 明确把

\[
\nabla(\chi^2\operatorname{Rm})
\quad\text{与}\quad
\nabla^2\chi
\]

一起估计，这支持 Step 34 的起始配对

\[
W_1=\nabla U,\qquad C_2=\nabla^2\chi.
\]

技术上应使用正则化平方范数

\[
\mathcal X_{1,p}
=(\varepsilon+\|W_1\|_p^p)^{2/p},
\qquad
\mathcal Z_{2,p}
=(\varepsilon+\|C_2\|_p^p)^{2/p},
\]

并证明

\[
(\mathcal X_{1,p}+\mathcal Z_{2,p})'
+c\,(\varepsilon+\|W_1\|_p^p)^{2/p-1}D_{1,p}
\le C_p(t)(1+\mathcal X_{1,p}+\mathcal Z_{2,p}),
\tag{4.1}
\]

其中 \(C_p\in L^1(0,T)\)。仅说每个时刻有限还不够；可用的系数应来自
\(\|U\|_\infty\)、统一有限的未加权 \(T\)-矩以及前一层 cutoff 导数。

在 \(m=1\) 时，进一步分部积分会把最后的 \(\nabla^2U\) 变成
\(\nabla W_1\)，可进入耗散。到 \(m=2\) 时，同一操作留下

\[
I=\int\chi |C_2||W_2|^p.
\]

令 \(u=\chi|W_2|^{p/2}\)、\(X=\|W_2\|_p^p\)。则

\[
\|\nabla u\|_2^2
\le Cp^2D_{2,p}+Cr^{-2}X,
\qquad
\|u\|_2^2\le X,
\]

以及

\[
I\le \|C_2\|_4\|u\|_4X^{1/2}.
\]

因此更精确的估计为

\[
\begin{aligned}
I\le{}&
\varepsilon D_{2,p}
+C_{\varepsilon}p^2\mathcal S_*
 \|C_2\|_4^2X\\
&+C\mathcal S_*^{1/2}r^{-1}\|C_2\|_4X,
\end{aligned}
\]

进而

\[
\boxed{
I\le\varepsilon D_{2,p}
+C_{\varepsilon,p}
\left[1+\mathcal S_*\|C_2\|_4^2(1+r^{-2})\right]X.}
\tag{4.2}
\]

Step 34 式 (6.6) 的 Sobolev 幂 \(\mathcal S\|C_2\|_4^2\) 正确，但单独写成
\(\mathcal S\|C_2\|_4^2(1+r^{-2})X\) 少了可吸收线性
\(\mathcal S^{1/2}r^{-1}\|C_2\|_4X\) 的零阶常数。式 (4.2) 是可直接用于 Gronwall 的形式。

因此，\(m=2\) 的核心机制已被正确定位：先由起始配对提供统一
\(\|C_2\|_4\)，再以 (4.2) 处理单个 \(\chi\) 因子。仍需把
\((W_1,C_2)\) 和 \((W_2,C_3)\) 两层的其余张量乘积逐项写入 (4.1) 型不等式；Wang 的未平移局部 Ricci 流公式不能自动替代当前带 \(G\) 的平移方程。

---

## 已由现有材料支持与仍待公式级推导的部分

**现有材料支持：**

- \(\gamma=\mathcal S K_2^{1/2}\) 及匹配体积下的塌缩消去；
- 混合恒等式 \(H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2\)；
- 在点态 \(Y(s)\lesssim s^{-1}\) 输入下，端点时间幂 \(t^{-3/p_0}\)；
- 曲率 \(C\gamma/t\)、缺陷 \(C\delta(r^2/t)^{1/3}\) 的代数与缩放；
- 式 (4.10) 的 Sobolev–Hölder机制；
- cutoff Hessian 的演化式及 \(m=2\) 单-\(\chi\) 项的处理方式。

**仍待完整推导：**

- 一般 \(p\) 的曲率与缺陷张量能量式 \((E_p)\)；
- 统一于 \(\varepsilon\) 的式 (3.1)，以及由此得到的 \(J_6\) 持续性；
- 首出区间中移动 Sobolev、\(K_2\)、测度和支撑几何的定量联立；
- 起始配对 (4.1) 与下一层所有收缩项的逐项估计。

这些分析只处理加权流的解析链条，不产生任何 Ricci 夹逼间隙或 Einstein 度量存在性结论。
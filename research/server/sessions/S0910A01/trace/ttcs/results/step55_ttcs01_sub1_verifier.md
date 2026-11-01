# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step54_first_exit_continuation_derivation.md",
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A01/workspace/data/step55_bootstrap_continuation_verify.json",
    "Sessions/S0910A03/workspace/data/step57_H2_verification.json"
  ]
}
```

## Task

Verify the combined analytic interface for the restricted Ishida--LeBrun negative-gap route after Step 55 and A03 Step57. Read the Step55 repair note, the patched Step54 derivation, and A03 Step57 H2/continuation note. Focus on scientific correctness of: (i) the coupled first-exit bootstrap using Gamma(t)=S(t)H2(t)^{1/2} and V(t)=int||aE||_inf rather than an evolving unweighted |E|<=delta; (ii) H2 evolution/absorption with shifted curvature T, including whether the bounded source C0=O(Vol) is compatible with the small gamma/Whitney cancellation and does not destroy sequence-uniform first exit; (iii) the W^{1,p}->L^infty continuation bridge and whether the fixed-background connection difference A is needed to obtain smooth restart data; (iv) terminal local compactness on exponential pullback balls rather than base image balls. Identify any remaining mathematical gaps precisely and suggest the next proof object to write, but do not treat this as a complete Yau 26 proof.

## Output

# 科学核验备忘录

## 总体结论

Step 55 对首出自举和固定背景延拓的修补方向正确，并消除了 Step 54 中两个实质性问题：

1. 度量漂移应由  
   \[
   V(t)=\int_0^t\|aE(s)\|_\infty\,ds
   \]
   控制，而不是假设演化中的无权点态估计 \(|E(t)|\le\delta\)。

2. 光滑延拓必须在固定连接下控制度量分量；移动 Levi–Civita 连接满足 \(\nabla^{g(t)}g(t)=0\)，不能直接把 \(\nabla^m\partial_tg\) 对时间积分成度量的坐标正则性。

A03 Step 57 的 \(W^{1,p}\to L^\infty\) 论证能够从加权曲率控制推出正时间片上的无权曲率上界，但它本身只完成“曲率有界”这一层。光滑重启仍需 Step 55 的连接差
\[
A=\nabla^{g(t)}-\bar\nabla
\]
以及有限阶 current-pair 估计。

目前最需要统一的是 Step 57 中 \(H_2\) 方程的体积型项及其 §8 对 \(Y(0)\) 的使用；后者不能提供序列一致估计。终端几何放在指数映射拉回球上是正确的，但光滑局部紧致性还需显式加入终端曲率导数估计。

---

## 1. 耦合首出自举 \((\Gamma,V)\)

### 1.1 度量与 Sobolev 常数的传递正确

由
\[
\partial_tg=-2aE
\]
及 \(V(t)=\int_0^t\|aE\|_\infty\)，对固定切向量 \(\xi\) 有
\[
\left|\partial_t\log g(t)(\xi,\xi)\right|\le 2\|aE(t)\|_\infty.
\]
因此 Step 55 (1.6)
\[
e^{-2V(t)}g(0)\le g(t)\le e^{2V(t)}g(0)
\]
成立。

令长度双 Lipschitz 因子 \(L=e^V\)。在维数 \(n\) 的临界 Sobolev 不等式中：

- \(L^p\) 范数平方产生 \(L^{n-2}\)；
- 把初始梯度积分换成当前梯度积分至多产生 \(L^{n+2}\)；
- 合并后得到 \(L^{2n}\)。

故
\[
\mathcal S(t)\le e^{2nV(t)}\mathcal S(0),
\]
四维时为 \(e^{8V}\)。`step55_bootstrap_continuation_verify.json` 中的指数计算与此一致。

### 1.2 两个自举量确实能够同时改善

在 \(\Gamma\le\gamma_*\) 下，若 \(H_2\) 满足 Step 55 (1.9)，则
\[
H(t)\le H(0)\exp\!\left(C_H(1+r^{-2})t+C_VV(t)\right).
\]
结合 Sobolev 传递，在 \(t\le\theta r^2\)、\(r\le1\) 时，
\[
\gamma(t)\le\gamma(0)
 \exp\!\left[\left(2n+\frac{C_V}{2}\right)V(t)+C_H\theta\right].
\]
因此小的 \(V_*,\theta\) 将初始 \(\gamma(0)\le\gamma_*/2\) 改善为
\[
\Gamma\le\frac34\gamma_*.
\]

另一方面，条件性缺陷 Moser 端点
\[
\|aE(t)\|_\infty
 \le C_E\delta\left(\frac{r^2}{t}\right)^{1/3}
\]
在 \(t=0\) 可积，并给出
\[
V(T)\le\frac32 C_E\delta r^{2/3}T^{2/3}
       \le\frac32C_E\delta\theta^{2/3}r^2.
\]
这正是首出论证所需的第二个改善。数据文件中的积分数值与该公式相符。

### 1.3 仍需在正式证明中明确的三点

- 对多个不交支撑，应使用
  \[
  \Gamma(t)=\max_\alpha\sup_{s\le t}
     \mathcal S_\alpha(s)H_{2,\alpha}(s)^{1/2},
  \qquad
  V(t)=\int_0^t\|aE(s)\|_{L^\infty(M)}\,ds.
  \]
  单支撑写法本身正确，但共同时间需要这个最大值版本。

- 最优 Sobolev 常数随时间的连续性没有在材料中证明。可以直接定义显式上界
  \[
  \widehat{\mathcal S}_\alpha(t)
  =e^{8V(t)}\mathcal S_\alpha(0)
  \]
  并用 \(\widehat{\mathcal S}_\alpha H_{2,\alpha}^{1/2}\) 定义首出量。这样首出函数由连续的 \(H_2,V\) 构成。

- 缺陷 Moser 端点必须写成在
  \[
  \Gamma\le\gamma_*,\qquad V\le V_*
  \]
  下成立的条件性引理，且常数只能依赖 \(n,\gamma_*,V_*,r\) 与初始几何数据中已经固定的量。现有文稿给出了端点，但完整迭代仍为引用式叙述。

---

## 2. 移位曲率 \(T\) 的 \(H_2\) 方程

### 2.1 移位变量的结构正确

取
\[
T=\operatorname{Rm}+\frac{g\owedge g}{2(n-1)}.
\]
在文稿采用的 Kulkarni–Nomizu 与曲率张量范数约定下，
\[
\operatorname{Ric}(T)=E,\qquad \nabla T=\nabla\operatorname{Rm}.
\]
因此
\[
D_2=\int\eta^2a|\nabla T|^2
\]
就是原曲率耗散项。固定张量 \(G\) 的范数只依赖维数，所以
\[
1+|T|^2\asymp_n1+|\operatorname{Rm}|^2.
\]

Step 57 §§3–5 中以下处理是成立的：

- Bochner 主项给出 \(-2D_2\)；
- \(\nabla a*\nabla E*T\) 由
  \[
  \frac{|\nabla a|^2}{a}=4|\nabla\chi|^2
  \]
  吸收；
- \(\nabla^2a\) 项经过一次有符号分部积分，化为
  \[
  \varepsilon D_2+C_{\varepsilon}r^{-2}H_2;
  \]
- 因 \(\operatorname{supp}\nabla\eta\subset\{a=0\}\)，所有
  \(\nabla\eta\cdot\nabla a\) 项消失。

### 2.2 Step 57 的体积记号有一处等式错误

Step 57 (2.2) 写道
\[
s=\operatorname{tr}E-n=\operatorname{scal}+n.
\]
正确关系是
\[
\operatorname{tr}E=R+n,\qquad
s:=\operatorname{tr}E-n=R.
\]
于是
\[
\partial_td\mu=-a(R+n)d\mu=-a\,\operatorname{tr}E\,d\mu.
\]
后续估计
\[
|\operatorname{tr}E|\le\sqrt n\,|E|\le C_nF_T
\]
仍然正确，因此这是记号等式问题，不改变能量估计。

### 2.3 \(C_0\) 必须局部化；局部化后不会破坏 Whitney 抵消

Step 57 (7.1) 写成
\[
H_2'+cD_2
 \le C_1Y+C_2r^{-2}H_2+C_0.
\]
实际计算中的体积型项均含 \(\eta^2a\)，所以至多是
\[
C_0(t)\le C_n\int\eta^2a\,d\mu_t.
\]
由于 \(F_T\ge1\)，
\[
\int\eta^2a
 \le\int\eta^2aF_T^3=Y,
\]
也有
\[
\int\eta^2a\le H_2.
\]
故该项可并入 \(CY\) 或 \(CH_2\)，无需出现依赖整个 \(\operatorname{Vol}(M)\) 的局部加项。

若把 Step 57 的 \(C_0=O(\operatorname{Vol})\) 理解为每个支撑都加入全流形体积，则局部 \(H_2\) 与局部体积之间的 Whitney 抵消不再成立。但原始局部积分并不会产生这样的全局项。

此外，Step 57 §2 已将体积变分和范数变分估计进 \(CY\)，§6 又将它们列入 Type (D)；这是重复记账，所得较弱不等式仍可成立，但会掩盖上述局部结构。

### 2.4 正确的 \(H_2\) 闭合不需要 \(Y(0)\)

因为 \(\eta=1\) 于 \(\operatorname{supp}\chi\)，
\[
Y=\int aF_T^3
 \le H_2^{1/2}
       \left(\int a^2F_T^4\right)^{1/2}.
\]
对 \(\chi F_T\) 使用局部 Sobolev 不等式：
\[
\left(\int a^2F_T^4\right)^{1/2}
 =\|\chi F_T\|_4^2
 \le C\mathcal S
   \left(D_2+r^{-2}H_2\right).
\]
因此
\[
Y\le C\gamma(t)\left(D_2+r^{-2}H_2\right),
\qquad
\gamma(t)=\mathcal S(t)H_2(t)^{1/2}.
\]
当 \(\gamma\le\gamma_*\) 足够小时，\(D_2\) 项被吸收，得到 Step 55 所需的
\[
H_2'+c'D_2
 \le C(1+r^{-2})H_2
    +C\|aE\|_\infty H_2.
\]

这条路线只使用初始 \(L^2\) 曲率预算。相比之下，Step 57 (8.3)
\[
H_2(t)\le e^{Ct/r^2}\bigl(H_2(0)+Cr^2Y(0)\bigr)
\]
不能给出序列一致控制，因为初始局部 \(L^2\) 曲率并不控制 \(Y(0)=\int aF_T^3\)。每个初始度量虽光滑，但 \(Y(0)\) 可随序列增长。组合后的首出证明应采用 Step 54 (2.7b) 的直接吸收，而不是依赖 \(Y(0)\)。

局部化后的体积项被 \(H_2\) 自身吸收，所以初始
\[
H_2(0)\lesssim(1+\kappa_0^2)V_\alpha,\qquad
\mathcal S_\alpha(0)\lesssim r^2V_\alpha^{-1/2}
\]
仍给出
\[
\gamma_\alpha(0)\lesssim r^2\sqrt{1+\kappa_0^2},
\]
体积因子完全抵消。

---

## 3. \(W^{1,p}\to L^\infty\) 与固定背景延拓

### 3.1 Step 57 的有限阶曲率桥成立

在正时间片 \([\tau,T_*)\) 上，由
\[
\|aF_T(t)\|_\infty\le C\gamma/t
\]
可得 \(U=aT\) 有界，进而度量与 \(g(\tau)\) 双 Lipschitz 等价。

若接受 Step 56 supplement 的三组能量式：

\[
T\in L^\infty_tL^q_x,
\]
\[
(V,Z)=(\nabla U,\nabla^2\chi)
   \in L^\infty_tL^q_x,
\]
\[
X=\nabla T\in L^\infty_tL^q_x
\]
对每个有限 \(q\) 成立，那么取 \(p>4\)，Kato 不等式与标量 Sobolev 嵌入给出
\[
\|T(t)\|_\infty
 \le C_{\tau,p}\bigl(\|T(t)\|_p+\|\nabla T(t)\|_p\bigr).
\]
这一步只需要双 Lipschitz 控制；不需要固定背景连接。它正确地把加权 \(U\) 控制转化为全流形无权曲率控制。

### 3.2 无权曲率有界尚不足以产生光滑重启数据

Step 57 Proposition 9.1 的第 (i) 部分由上述论证支持，但第 (ii) 部分还缺少有限阶坐标正则性。原因是：

- \(\nabla^{g(t)}g(t)=0\) 不包含度量分量的空间导数信息；
- \(|\operatorname{Rm}|\le C\) 并不直接给出固定坐标下的 \(H^{s_0}\) 度量控制；
- Step 57 (9.8) 只由 \(\nabla U\in L^p\) 得到连接的一阶时间积分，尚未覆盖重启定理所需的高阶数据。

Step 55 的固定背景构造解决了正确的转换问题。取
\[
\bar\nabla=\nabla^{g(\tau)},\qquad
A=\nabla^{g(t)}-\bar\nabla.
\]
则
\[
\partial_tA=g^{-1}*\nabla(aE).
\]
对固定背景求 \(m\) 阶导数后，
\[
\bar\nabla^m\partial_tA
 =g^{-1}*U_{m+1}
  +P_m\bigl(A,\ldots,\bar\nabla^{m-1}A;
            U_0,\ldots,U_m\bigr).
\]
右端不含 \(\bar\nabla^mA\)，这是严格的三角结构。若 current-pair 层级已给出 \(U_j\) 的足够高阶有限指数估计，则可依次积分得到
\[
\sup_{t<T_*}\|\bar\nabla^mA(t)\|_{L^p(\bar g)}<\infty.
\]
再由
\[
\bar\nabla g=A*g
\]
得到固定背景下的度量 Sobolev 控制。

为了真正得到终端数据，还需补写时间收敛：把
\[
\bar\nabla^m\partial_tg
 =-2\bar\nabla^m(aE)
\]
转换为 \(U_j\) 与低阶 \(A\) 的组合，并证明其在时间上可积。这样 \(g(t)\) 才在所需 \(W^{s,p}\) 或 \(H^{s_0}\) 空间中收敛到正定度量 \(g(T_*)\)。

因此，固定背景 \(A\) 对本路线中的光滑重启是必需的；等价的固定 DeTurck 规范也可承担同一作用。Step 57 所说“只需最初两层”适用于取得 \(|T|_\infty\)，不适用于生成完整重启数据。

---

## 4. 指数映射拉回球上的终端几何

Step 55 §3 的定位是正确的。设终端平台内
\[
|\operatorname{Rm}|\le K,
\]
并选
\[
\rho<\min\{\text{平台缓冲距离},\,\pi/(2\sqrt K)\}.
\]
沿所有长度不超过 \(\rho\) 的径向测地线，Rauch–Günther 比较给出：

- \(d\exp_p\) 非退化；
- 拉回度量 \(\tilde g_p=(\exp_p)^*g(T)\) 光滑；
- 径向 Jacobian 满足
  \[
  c_Ks^{n-1}\le J_p(s,u)\le C_Ks^{n-1};
  \]
- 因而
  \[
  c\rho^n\le
  \operatorname{Vol}_{\tilde g_p}(\mathcal B_\rho(p))
  \le C\rho^n.
  \]

指数映射可以在底流形上自重叠，但这不影响拉回球上的体积或积分。对非负标量密度 \(\Phi\)，
\[
A_\rho\Phi(p)
 =\frac{1}{\operatorname{Vol}_{\tilde g_p}\mathcal B_\rho}
   \int_{S_pM}\int_0^\rho
      \Phi(\exp_p(su))J_p(s,u)\,ds\,du.
\]
由 Jacobian 的统一比较和单位切丛上测地流的 Liouville 测度不变性，
\[
\int_{P^{\rm in}}A_\rho\Phi(p)\,d\mu(p)
 \le C\int_M\Phi\,d\mu.
\]
这里不需要底流形像球的体积下界，也没有指数映射重数因子。

尚需补充的是局部紧致性的正则度。仅有 \(|\operatorname{Rm}|\le K\) 与拉回体积下界通常先给出较低阶紧致性；若 Proposition 3.2 使用曲率密度的平滑极限，应在更小的平台球上加入统一的
\[
|\nabla^m\operatorname{Rm}(T)|\le C_m.
\]
这些估计可由 \(t\in[T/2,T]\) 上的平台曲率上界和局部 Shi 型估计获得，因为平台内 \(a=1\)，方程就是归一化 Ricci 流。还应明确初始平台缓冲在小 \(V(T)\) 的双 Lipschitz扰动后仍包含所有长度 \(\rho\) 的终端径向测地线。

---

## 5. 精确剩余缺口与建议证明对象

现有材料尚缺以下成文推导：

1. 无全局体积加项的局部移位 \(H_2\) 引理，并使用
   \[
   Y\le C\gamma(D_2+r^{-2}H_2)
   \]
   直接闭合，而非 Step 57 (8.3) 的 \(Y(0)\)。

2. 在 \((\Gamma,V)\) 假设下完整书写曲率与缺陷 Moser 迭代，特别是
   \[
   \|aF_T(t)\|_\infty\le C\gamma_0/t,\qquad
   \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3},
   \]
   并列明所有常数的依赖。

3. 从基础对 \((T,U_1,C_2,T_1)\) 推广到重启所需有限阶数的 current-pair 归纳。

4. 固定背景下 \(A\)、\(g\) 及 \(\partial_tg\) 的有限阶估计和终端时间收敛。

5. 平台内部的终端曲率导数估计及指数拉回球上的平滑紧致性陈述。

能够一次封装这些接口的证明对象是一个“四维共同观察时间命题”：

> 在缓冲 cutoff、初始 \(\gamma_0\le\gamma_*/2\) 及 \(\|E(0)\|_\infty\le\delta_*\) 下，最大光滑解至少存在到 \(\theta r^2\)，并在该区间满足统一的 \(\Gamma,V,H_2,Q,aF_T,aE\) 估计；若最大时间早于 \(\theta r^2\)，有限阶 current-pair 估计与固定背景连接差产生 \(H^{s_0}\) 终端度量并允许重启。

这一命题将 Step 55 的首出机制、Step 57 的 \(W^{1,p}\) 曲率桥及固定背景延拓统一成可独立核验的分析模块。现有两个 JSON 文件验证了指数、积分和阶数记账，但不能代替上述张量演化、Moser 迭代与有限阶延拓证明。上述材料也尚未构成 Yau 第 26 题的整体证明。
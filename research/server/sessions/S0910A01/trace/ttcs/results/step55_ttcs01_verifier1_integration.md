# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 55,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step55_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step55_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the combined analytic interface for the restricted Ishida--LeBrun negative-gap route after Step 55 and A03 Step57. Read the Step55 repair note, the patched Step54 derivation, and A03 Step57 H2/continuation note. Focus on scientific correctness of: (i) the coupled first-exit bootstrap using Gamma(t)=S(t)H2(t)^{1/2} and V(t)=int||aE||_inf rather than an evolving unweighted |E|<=delta; (ii) H2 evolution/absorption with shifted curvature T, including whether the bounded source C0=O(Vol) is compatible with the small gamma/Whitney cancellation and does not destroy sequence-uniform first exit; (iii) the W^{1,p}->L^infty continuation bridge and whether the fixed-background connection difference A is needed to obtain smooth restart data; (iv) terminal local compactness on exponential pullback balls rather than base image balls. Identify any remaining mathematical gaps precisely and suggest the next proof object to write, but do not treat this as a complete Yau 26 proof.

## Integrated Scientific Memo

# 核验结论

组合后的解析接口**方向基本正确，但尚未闭合**。四个指定问题的结论如下：

1. 以
   \[
   \Gamma(t)=\sup_{s\le t}\mathcal S(s)H_2(s)^{1/2},
   \qquad
   V(t)=\int_0^t\|aE(s)\|_\infty\,ds
   \]
   作耦合首出自举是正确修复；不能继续使用演化中的无权假设 \(|E(t)|\le\delta\)。

2. 移位曲率 \(T\) 的 \(H_2\) 耗散及 Hessian-\(a\) 吸收机制成立。Step 57 所写 \(C_0=O(\operatorname{Vol})\) 必须理解为**每个支撑上的局部体积项**；局部化后它被 \(H_2\) 自身吸收，不破坏 Whitney 体积抵消。Step 57 §8 依赖 \(Y(0)\) 的闭合则不能用于序列一致首出。

3. \(W^{1,p}\to L^\infty\) 确实给出正时间片上的无权曲率上界，但不能单独产生光滑重启数据。固定背景连接差
   \[
   A=\nabla^{g(t)}-\nabla^{g(\tau)}
   \]
   对把 moving-covariant 估计转换为固定坐标 Sobolev 数据是必要的。

4. 终端局部紧致性必须放在指数映射拉回球上，而不能声称塌缩底流形中的像球有统一体积下界。若局部禁形下界需要光滑极限，还必须补入平台内部的曲率高阶导数估计。

---

## 1. 耦合首出自举

由 \(\partial_tg=-2aE\)，
\[
\left|\partial_t\log g(t)(\xi,\xi)\right|
 \le 2\|aE(t)\|_\infty,
\]
故
\[
e^{-2V(t)}g(0)\le g(t)\le e^{2V(t)}g(0).
\]
若长度双 Lipschitz 因子为 \(L=e^V\)，临界 Sobolev 常数满足
\[
\mathcal S(t)\le L^{2n}\mathcal S(0)=e^{2nV(t)}\mathcal S(0);
\]
四维时即 \(e^{8V}\)。这部分与验证数据一致。

在 \(\Gamma\le\gamma_*\) 下，正确的局部能量不等式应归结为
\[
H_2'+cD_2
 \le C(1+r^{-2})H_2+C\|aE\|_\infty H_2.
\]
于是
\[
\gamma(t)\le \gamma(0)
 \exp\!\left[\left(2n+\frac{C_V}{2}\right)V(t)+C\theta\right],
 \qquad t\le\theta r^2.
\]
小的 \(V_*,\theta\) 将 \(\gamma(0)\le\gamma_*/2\) 改善为
\(\Gamma\le3\gamma_*/4\)。

条件性缺陷端点
\[
\|aE(t)\|_\infty
 \le C_E\delta (r^2/t)^{1/3}
\]
给出
\[
V(T)\le \frac32C_E\delta r^{2/3}T^{2/3}
 \le \frac32C_E\delta\theta^{2/3}r^2.
\]
故 \(V(T)\le V_*/2\) 的精确充分条件是
\[
\delta\le
 \frac{V_*}{3C_E\theta^{2/3}r^2}.
\]
Step 55 (1.17) 省略了 \(r^2\)。其写法
\[
\delta\le\frac{V_*}{3C_E\theta^{2/3}}
\]
在 \(r\le1\) 时只是更强的充分条件，并非逻辑错误，但与 JSON 样例所用参数不一致，应修正或注明故意采用更强条件。

正式的多支撑版本应定义
\[
\Gamma(t)=\max_\alpha\sup_{s\le t}
 \widehat{\mathcal S}_\alpha(s)H_{2,\alpha}(s)^{1/2},
\qquad
\widehat{\mathcal S}_\alpha(t)
 =e^{8V(t)}\mathcal S_\alpha(0),
\]
以及全局
\[
V(t)=\int_0^t\|aE(s)\|_{L^\infty(M)}\,ds.
\]
使用显式的 \(\widehat{\mathcal S}\) 可避免尚未证明“最优 Sobolev 常数随时间连续”的技术问题。

仍缺的是把两个 Moser 端点明确表述为在
\[
\Gamma\le\gamma_*,\qquad V\le V_*
\]
下成立的条件性引理，并核对其常数对 \(V\le V_*\) 一致。

---

## 2. 移位 \(H_2\) 方程与体积源

设
\[
T=\operatorname{Rm}+\frac{g\owedge g}{2(n-1)},\qquad
F_T=(1+|T|^2)^{1/2}.
\]
在给定约定下
\[
\operatorname{Ric}(T)=E,\qquad \nabla T=\nabla\operatorname{Rm},
\]
所以
\[
D_2=\int\eta^2a|\nabla T|^2
\]
正是原曲率耗散。Step 57 对以下项的处理成立：

- Bochner 项给出 \(-2D_2\)；
- \(\nabla a*\nabla E*T\) 由
  \[
  |\nabla a|^2/a=4|\nabla\chi|^2
  \]
  吸收；
- \(\nabla^2a\) 项经一次有符号分部积分成为
  \[
  \varepsilon D_2+C_\varepsilon r^{-2}H_2;
  \]
- \(\operatorname{supp}\nabla\eta\subset\{a=0\}\) 消除边界交叉项；
- \(G\) 的演化只产生有界代数反应。

Step 57 (2.2) 有一个记号错误：
\[
\operatorname{tr}E=R+n,\qquad
s:=\operatorname{tr}E-n=R,
\]
不是 \(s=R+n\)。但
\[
\partial_td\mu=-a\,\operatorname{tr}E\,d\mu
\]
及后续估计不受影响。

### 体积型项的正确解释

局部能量计算产生的所谓 \(C_0\) 实际满足
\[
C_{0,\alpha}(t)\le
 C_n\int\eta_\alpha^2a\,d\mu_t.
\]
它不是对每个支撑都加入的全流形 \(\operatorname{Vol}(M)\)。由于
\[
F_T\ge1,\qquad 0\le a\le1,
\]
有
\[
\int\eta^2a\,d\mu_t\le H_2(t),
\]
甚至可并入 \(Y=\int\eta^2aF_T^3\)。因此
\[
C_{0,\alpha}\le C H_{2,\alpha},
\]
从而恢复 Step 55 使用的纯乘法型不等式。若将 \(C_0\) 错写为每个支撑上的 \(C\operatorname{Vol}(M)\)，则确会破坏局部 Whitney 抵消；原始积分并不产生这种项。

正确的直接吸收是
\[
Y:=\int\eta^2aF_T^3
 \le H_2^{1/2}\|\chi F_T\|_4^2
 \le C\mathcal S H_2^{1/2}
       (D_2+r^{-2}H_2),
\]
即
\[
Y\le C\gamma(t)(D_2+r^{-2}H_2).
\]
在 \(\gamma\le\gamma_*\) 下吸收 \(D_2\)，即可得到首出所需的 \(H_2\) Grönwall。

Step 57 (8.3) 使用
\[
H_2(t)\lesssim H_2(0)+r^2Y(0)
\]
不能作为序列一致闭合，因为初始 \(L^2\) 曲率预算并不控制
\(Y(0)=\int aF_T^3\)。组合证明必须采用上述直接 \(H_2\)-Sobolev 吸收，而非 \(Y(0)\)。

这样
\[
H_{2,\alpha}(0)\lesssim
 (1+\kappa_0^2)V_\alpha,\qquad
\mathcal S_\alpha(0)\lesssim r^2V_\alpha^{-1/2}
\]
仍给出
\[
\gamma_\alpha(0)\lesssim
 r^2\sqrt{1+\kappa_0^2},
\]
体积完全抵消。

---

## 3. 延拓桥

Step 56 的基础块若成立，则在正时间片 \([\tau,T_*)\) 上可得
\[
T\in L^\infty_tL^q_x,\qquad
(\nabla U,\nabla^2\chi)\in L^\infty_tL^q_x,\qquad
\nabla T\in L^\infty_tL^q_x
\]
对每个有限 \(q\) 成立。取 \(p>4\)，Kato 与 Sobolev 嵌入给出
\[
\|T(t)\|_\infty
 \le C_{\tau,p}\bigl(\|T(t)\|_p+\|\nabla T(t)\|_p\bigr).
\]
因此 Step 57 的有限阶论证确实产生无权曲率上界。

但这只证明“曲率不爆破”，尚未证明固定坐标下的重启正则性。必须固定
\[
\bar\nabla=\nabla^{g(\tau)},\qquad
A=\nabla^{g(t)}-\bar\nabla.
\]
连接变分为
\[
\partial_tA=g^{-1}*\nabla(aE).
\]
固定背景求导后具有三角结构
\[
\bar\nabla^m\partial_tA
 =g^{-1}*U_{m+1}
 +P_m(A,\ldots,\bar\nabla^{m-1}A;
       U_0,\ldots,U_m).
\]
右端不含顶阶 \(\bar\nabla^mA\)。因此足够高阶的 current-pair 估计可推出
\[
\sup_{t<T_*}\|\bar\nabla^mA(t)\|_{L^p(\bar g)}<\infty,
\]
再由
\[
\bar\nabla g=A*g
\]
获得固定背景度量的 \(W^{m+1,p}\) 控制。

还需证明终端收敛，而不只是有界性：将
\[
\bar\nabla^m\partial_tg=-2\bar\nabla^m(aE)
\]
写成 \(U_j\) 与低阶 \(A\) 的组合，并证明其时间可积，才能得到
\(g(t)\to g(T_*)\) 于重启定理要求的 \(H^{s_0}\) 或 \(W^{s,p}\) 拓扑，且极限保持正定。

所以：

- \(W^{1,p}\to L^\infty\) 足够获得无权曲率控制；
- 固定背景 \(A\) 对光滑重启仍是必要的；
- Step 57 所称“高阶一旦曲率有界便平凡闭合”只在平台 \(a=1\) 上可直接援引均匀抛物理论；在退化 collar 上仍需有限阶加权归纳。

---

## 4. 指数拉回球

终端局部几何应定义在
\[
\mathcal B_\rho(p)\subset T_pM,\qquad
\tilde g_p=(\exp_p)^*g(T)
\]
上。若平台内 \(|\operatorname{Rm}|\le K\)，并取 \(\rho\) 小于曲率尺度及平台缓冲尺度，则 Rauch/Jacobi 比较给出拉回球上的统一 Jacobian 和体积控制：
\[
c\rho^n\le
\operatorname{Vol}_{\tilde g_p}\mathcal B_\rho(p)
\le C\rho^n.
\]
这不要求 \(\exp_p\) 在底流形上单射；像球可以因塌缩而高度自重叠。

因此平均应写为
\[
A_\rho\Phi(p)=
 \fint_{\mathcal B_\rho(p)}
   (\exp_p)^*\Phi\,d\mu_{\tilde g_p}.
\]
单位切丛上的测地流保持 Liouville 测度，从而
\[
\int_{P^{\rm in}}A_\rho\Phi(p)\,d\mu(p)
 \le C\int_M\Phi\,d\mu,
\]
没有指数映射重数损失。

尚缺两项：

1. 明确小 \(V(T)\) 的双 Lipschitz 扰动后，所选终端径向测地线仍完全处于平台缓冲内；
2. 若局部禁形命题使用光滑极限，则须在较小平台球上证明
   \[
   |\nabla^m\operatorname{Rm}(T)|\le C_m.
   \]
   这可在 \(t\in[T/2,T]\) 上利用平台内 \(a=1\) 的归一化 Ricci 流和局部 Shi 型估计完成。

---

## 精确剩余证明对象

最有效的下一证明对象是一个**四维共同观察时间与光滑延拓命题**，包含：

1. 每个支撑上的局部移位 \(H_2\) 引理，明确
   \[
   C_{0,\alpha}\le CH_{2,\alpha},\qquad
   Y_\alpha\le C\gamma_\alpha
      (D_{2,\alpha}+r^{-2}H_{2,\alpha});
   \]
2. 在共同假设 \(\Gamma\le\gamma_*,V\le V_*\) 下完整推导两个 Moser 端点；
3. 把 Step 56 的基础块推广到重启阶数 \(s_0+1\) 的有限 current-pair 归纳，逐阶保留最高 cutoff jet 的显式 \(\chi\) 权；
4. 通过固定背景 \(A\) 推出 \(g(t)\) 的 \(H^{s_0}\) 终端收敛并重启；
5. 在终端平台上补入曲率导数界和指数拉回球的平滑紧致性。

现有 JSON 只验证指数、积分和阶数记账，不能替代这些 PDE、Moser 和有限阶延拓证明。该模块即使完成，也仍只是受限四维 Ishida–LeBrun 负间隙路线的一部分，并非 Yau 第 26 题的完整证明。
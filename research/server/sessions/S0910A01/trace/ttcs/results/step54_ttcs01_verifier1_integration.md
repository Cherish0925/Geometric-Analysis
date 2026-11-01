# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 54,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step54_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step54_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the first-exit and continuation derivation in step54_first_exit_continuation_derivation.md. Focus on three critical mathematical points:

1. AUGMENTED ENERGY vs FLAT-TORUS TEST: The derivation claims that the flat-torus test (creating curvature from zero by nonconstant cutoff) does not invalidate augmented-energy estimates H_2 = int eta^2(1+|Rm|^2), because the normalization reaction +4a|R|^2 is absorbed by the CaF^3 reaction term already present. Check: is the reaction structure in the curvature power inequality (eq 4.4 of Step 35, eq 2.6 of this note) genuinely compatible with the normalization? Specifically, does the Hamilton quadratic + normalization + Hessian-a absorption close with the available dissipation, without introducing a bare additive constant?

2. DEFECT HOMOGENEITY: The derivation separates defect energies from curvature energies by the property B_def|_{E=0} = 0. Check whether every term in the J_6 evolution (eq 4.2) and the Q propagation (eq 7.2) genuinely has E-homogeneous coefficients. In particular, verify that the volume form variation d mu contributes an E-dependent term (not a curvature-only term) in the defect energy evolution.

3. CONTINUATION ARGUMENT: The staggered hierarchy (eq 6.2-6.3) claims that the highest cutoff jet C_{m+2} always carries a chi factor from the product rule nabla^{m+2}(chi^2) = 2 chi C_{m+2} + lower. Check: does this chi factor survive integration by parts and pairing with the weighted dissipation? Is there a term where the chi weight is consumed by a different factor, leaving a bare C_{m+2} contribution?

Provide a mathematical assessment of each point, identifying any gaps or errors.

## Integrated Scientific Memo

# 核验结论

Step 54 的三个核心结构中：

1. **增广曲率能量的思路基本正确，但 (2.7) 被写得过强，且平坦环面机制解释不准确。**
2. **缺陷方程确实完全对 \(E\) 齐次，包括体积元变分；但 \(J_6\) 和 \(Q\) 的闭合仍需小临界能量吸收，不能仅援引点态曲率界。**
3. **最高 cutoff jet 的一个 \(\chi\) 因子在主导积分分部中足够且不会留下裸 \(C_{m+2}\)；然而这只验证了主项，尚未证明完整延拓层级。Step 54 从 \(U_m=\nabla^m(aT)\) 在退化 collar 上恢复裸 \(T_m\) 的说法是错误的。**

---

## 1. 增广能量与平坦环面测试

### 1.1 归一化反应与 Hamilton 二次项相容

对
\[
\partial_tg=-2a(\operatorname{Ric}+g)=-2aE
\]
以及 Step 35 的全下标曲率约定，归一化与逆度量变分合计给出
\[
4a|\operatorname{Rm}|^2+8aW_{pq}\operatorname{Ric}^{pq},
\]
故
\[
|\text{Hamilton 二次项}+\text{归一化项}|
\le CaF^3,\qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]
体积元满足
\[
\partial_td\mu=-a\,\operatorname{tr}E\,d\mu,
\]
且 \(|\operatorname{tr}E|\le CF\)，所以测试 \(p\)-次能量时也产生
\[
C\int \eta^2a^{p-1}F^{p+1},
\]
而不是与曲率能量无关的常数源。Step 35 (4.2) 的 Sobolev–Young 吸收因此与归一化项相容。

对平移曲率
\[
T=\operatorname{Rm}+G,\qquad F_T=(1+|T|^2)^{1/2},
\]
若采用满足 \(\operatorname{Ric}(G)=g\) 的 Kulkarni–Nomizu 约定，则
\[
\operatorname{Ric}(T)=E,\qquad \nabla G=0.
\]
Hessian-\(a\) 收缩相应变为
\[
\Sigma_H^T
=8(\nabla_p\nabla_q a)B_T^{pq},
\qquad
B_T^{pq}=T^p{}_j{}^q{}_lE^{jl},
\]
并有
\[
|B_T|\le C F_T^2,\qquad
|\nabla B_T|\le C F_T|\nabla\operatorname{Rm}|.
\]
因此 Step 35 的有符号积分分部同样给出
\[
|T_H^T|
\le \varepsilon p\bigl(D_p^{\rm Rm}+(p-2)D_p^{F_T}\bigr)
+C_\varepsilon p^3r^{-2}K_p .
\]
此外 \(\partial_tG\)、逆度量变分以及将 Hamilton 多项式写成
\(\operatorname{Rm}=T-G\) 后产生的项都是代数项，大小至多
\[
CaF_T^3.
\]
所以从结构上看，\(F_T\) 版本不会产生裸加法常数。Step 54 §9.2.1 所称“仍需显式检查”的部分可以按上述方式完成，但原文尚未写出这一推导。

### 1.2 \(p=2\) 估计不是无条件 Grönwall

Step 54 的
\[
(H_2^\alpha)'\le C(1+r^{-2})H_2^\alpha \tag{2.7}
\]
不能仅由“\(F_T^2\) 含常数 \(1\)”直接推出。吸收前应为
\[
(H_2^\alpha)'+cD_2^\alpha
\le CY_T+C(1+r^{-2})H_2^\alpha,
\qquad
Y_T=\int\eta^2aF_T^3 .
\]
然后
\[
Y_T
\le (H_2^\alpha)^{1/2}\|\chi F_T\|_4^2
\le C\mathcal S(H_2^\alpha)^{1/2}
   \bigl(D_2^\alpha+r^{-2}H_2^\alpha\bigr).
\]
只有在
\[
\gamma(t)=\mathcal S(t)(H_2^\alpha(t))^{1/2}
\]
低于固定吸收阈值时，才能得到 (2.7)。Step 34 已明确使用这一小临界能量条件；Step 54 将其省略，形成实质性缺口。

### 1.3 平坦环面真正检验的是 Hessian-\(a\) 项

平坦初始度量上
\[
\operatorname{Rm}(0)=0,\qquad E(0)=g,
\]
所以归一化反应 \(4a|\operatorname{Rm}|^2\) 在 \(t=0\) 为零。曲率创建来自
\[
\partial_t\operatorname{Rm}\big|_{0}
\sim (\nabla^2a)\owedge g,
\]
故
\[
|\operatorname{Rm}(t)|^2=O(t^2|\nabla^2a|^2).
\]
因此“平坦环面不会推翻增广估计”的真正原因是 Hessian-\(a\) 收缩经过有符号积分分部后满足
\[
|T_H|
\le \varepsilon D_2+Cr^{-2}H_2,
\]
而不是归一化项本身解释了曲率创建。归一化项确实无害，但它不是该 benchmark 的创建机制。

### 1.4 两处工件错误

- 对 \(0\le\eta\le1\)，
  \[
  \int\eta^2\,d\mu\le \operatorname{Vol}(\operatorname{supp}\eta),
  \]
  并非 Step 54/JSON 所称 \(H_2\ge\operatorname{Vol}(\operatorname{supp}\eta)\)。正确下界是 \(\eta=1\) 的 plateau 体积。
- Step 54 写
  \[
  |G|^2=\frac{2n}{n-1},
  \]
  而 JSON 写
  \[
  |G|^2=\frac{n}{2(n-1)}.
  \]
  两者差四倍，来自不一致的 \(\owedge\) 约定。若 \(G\) 采用使
  \(\operatorname{Ric}(G)=g\) 的约定，则应固定相应的第一种归一化。该错误不破坏定性范数等价，但 JSON 的数值检查不能验证笔记所用的张量约定。

---

## 2. 缺陷齐次性

### 2.1 方程本身严格对 \(E\) 齐次

有精确公式
\[
\partial_tE
=D\operatorname{Ric}_g[-2aE]-2aE.
\]
Ricci 线性化对输入线性，故每一项都含有
\[
E,\quad \nabla E,\quad\text{或}\quad\nabla^2E.
\]
曲率可以作为系数出现在 \(a\,\operatorname{Rm}*E\) 中，但不存在仅依赖曲率和 \(a\) 的源项。因而 \(E\equiv0\) 对任意 cutoff 都严格平稳。

Step 35 给出的 Hessian 收缩
\[
B_{\rm def}^{pq}
=|E|^2g^{pq}+(\operatorname{tr}E)E^{pq}-2(E^2)^{pq}
\]
满足
\[
B_{\rm def}=O(|E|^2),\qquad
\nabla B_{\rm def}=O(|E||\nabla E|).
\]
所以其积分分部项完全保持缺陷齐次性。

### 2.2 体积元项也含 \(E\)

精确地，
\[
\partial_td\mu=-a\,\operatorname{tr}E\,d\mu.
\]

对
\[
J_6=\int\eta^2a^4|E|^6\,d\mu,
\]
体积元贡献为
\[
-\int\eta^2a^5(\operatorname{tr}E)|E|^6\,d\mu,
\]
它至少七次于 \(E\)，并可估为
\[
C\int\eta^2a^5F_T|E|^6=CP_6.
\]
因此绝非 curvature-only source。

对
\[
Q_\alpha=\int\eta_\alpha^2|E|^2\,d\mu,
\]
体积项为
\[
-\int\eta_\alpha^2a(\operatorname{tr}E)|E|^2\,d\mu,
\]
同样在 \(E=0\) 时消失。

### 2.3 \(J_6\) 与 \(Q\) 闭合仍需吸收

对 \(J_6\)，实际中间式是
\[
J_6'+cX_6
\le C(1+r^{-2})J_6+CP_6,
\]
且
\[
P_6\le C\gamma(t)\bigl(X_6+r^{-2}J_6\bigr).
\]
故 Step 54 (4.2) 仍以小 \(\gamma\) 为前提，而非单由
\(B_{\rm def}|_{E=0}=0\) 自动得到。

对 \(Q_\alpha\)，不能从正时间点态曲率界
\[
aF_T(t)\lesssim \gamma/t
\]
直接 Grönwall 到 \(t=0\)，因为 \(t^{-1}\) 不可积。正确路线是临界 \(L^2\)-Sobolev 吸收：
\[
Q_\alpha'+cD_E
\le CP_2+C(1+r^{-2})Q_\alpha,
\]
其中
\[
P_2=\int\eta_\alpha^2aF_T|E|^2
\le C\gamma(t)\bigl(D_E+r^{-2}Q_\alpha\bigr).
\]
小 \(\gamma\) 时才得到
\[
Q_\alpha'\le C(1+r^{-2})Q_\alpha.
\]
因此 (7.2) 可成立，但 Step 54 所给“依赖点态曲率界”的解释不足且在 \(t=0\) 附近错误。

另外，分解 (7.1) 要精确选择例如
\[
\rho=\sum_\alpha\eta_\alpha^2,
\]
并利用 \(\eta_\alpha=1\) 于 \(\operatorname{supp}a\)，才能保证
\(\operatorname{supp}(1-\rho)\subset\{a=0\}\)，从而 remainder 真正静止。

---

## 3. 最高 cutoff jet 与延拓

### 3.1 主导积分分部中不会留下裸 \(C_{m+2}\)

Leibniz 展开确实给出
\[
\nabla^{m+2}(\chi^2)
=2\chi C_{m+2}
+\sum_{1\le j\le m+1}C_j*C_{m+2-j}.
\]
最高 cutoff jet 在 \(U_m=\nabla^m(aT)\) 方程中的典型危险项可写成
\[
I_m
=\int \chi\,C_{m+2}*(aE)\,
     |U_m|^{p-2}U_m .
\]
把 \(C_{m+2}\) 看成 \(\nabla C_{m+1}\) 并积分分部：
\[
I_m
=-\int C_{m+1}*
 \nabla\!\left(\chi(aE)|U_m|^{p-2}U_m\right).
\]

- 导数打到 \(U_m\) 时，\(\chi\) 保留并可配对：
  \[
  \int\chi |C_{m+1}||aE||U_m|^{p-2}|\nabla U_m|
  \]
  \[
  \le \varepsilon\int\chi^2|\nabla U_m|^2|U_m|^{p-2}
   +C_\varepsilon\int|C_{m+1}|^2|aE|^2|U_m|^{p-2}.
  \]
- 导数打到 \(\chi\) 时，最高 jet 已从 \(C_{m+2}\) 降为
  \(C_{m+1}\)；因此即便 \(\chi\) 被消耗，也不会留下裸
  \(C_{m+2}\)。
- 导数打到 \(aE\) 时，由 \(U_1\) 及低阶 cutoff 项控制。

所以对被询问的精确主项，答案是：**没有一个积分分部项既消耗 \(\chi\) 又保留裸 \(C_{m+2}\)**。

### 3.2 这不足以证明 (6.3)

单一 Leibniz 恒等式并未覆盖：

- 全部 \([\partial_t,\nabla^m]\) 项；
- 与退化扩散 \(a\Delta\) 交换产生的项；
- 中间项 \((\nabla^ja)*\nabla^{m+2-j}T\) 如何无除法地改写为 \(U_k\)；
- \(C_{m+1}\) 自身演化中的最高 forcing；
- 低阶 \(U_j,C_j\) 的 \(L^\infty\) 控制；
- 达到重启所需 \(H^{s_0}\) 的有限阶数和 \(p>n\) 选择。

因此主导权重机制正确，但 (6.3) 及完整有限阶 induction 仍未证明。

### 3.3 collar 上恢复裸 \(T_m\) 是错误的

Step 54 声称由 \(U_m=\nabla^m(aT)\) 和 \(a\ge0\) 可在
\(0<a<1\) collar 上恢复 \(\nabla^mT\)。这不成立。零阶已有
\[
U_0=aT,
\]
而 \(a\to0\) 时 \(U_0\) 不控制 \(T\)。高阶关系
\[
U_m
=aT_m+\sum_{j=1}^m(\nabla^ja)*T_{m-j}
\]
若解出 \(T_m\)，必然除以 \(a\)，没有统一估计。

可行的无除法延拓应直接使用
\[
\partial_tg=-2aE,
\]
以及
\[
\nabla^m(aE)=\operatorname{RicciContraction}(U_m).
\]
若能获得足够高阶且时间可积的 \(U_m\) 控制，就可直接积分度量方程，控制固定坐标下 \(g\) 的 Sobolev 导数，从而获得重启所需的 endpoint regularity。这与恢复 collar 上裸曲率导数是不同论证，Step 54 尚未给出。

---

## 最终判定

- **点 1：部分验证。** 归一化、Hamilton 反应和 Hessian-\(a\) 项可在增广能量中闭合，无裸加法常数；但 \(H_2\) Grönwall 依赖小 \(\gamma\) 吸收，平坦环面的创建机制应归因于 Hessian-\(a\)，且 \(F_T\) 张量推导与 \(G\) 约定需显式修正。
- **点 2：验证。** 所有 \(J_6\) 和 \(Q\) 项，包括体积元变分，均对 \(E\) 齐次；不过两种能量不等式仍需临界 Sobolev 吸收，Step 54 对 \(Q\) 的证明理由不充分。
- **点 3：主项验证、完整延拓未验证。** 最高 jet 的 \(\chi\) 在所需处分配给加权耗散；若导数消耗它，cutoff 阶数已下降，因此没有裸 \(C_{m+2}\)。但完整交换子 induction 缺失，而且 collar 上由 \(aT\) 恢复 \(T\) 的步骤无效。
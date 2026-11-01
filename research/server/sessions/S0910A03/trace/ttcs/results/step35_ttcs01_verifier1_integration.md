# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 35,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step35_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step35_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the unregularized J_6 defect persistence lemma in the companion note. The flow is ∂_t g = -2χ²(Ric+g) on a closed 4-manifold with a fixed smooth cutoff χ. The key claims to check:

1. REGULARITY: s = |E|² is smooth, s³ is smooth, and the Sobolev variable w₆ = ηχ⁵|E|³ = ηa^{5/2}s^{3/2} is C¹ with bounded gradient. No ε-regularization is needed.

2. EXACT CHAIN RULE: (∂_t - aΔ)s³ = 3s²(∂_t - aΔ)s - 6as|∇s|², with the extra term nonpositive.

3. HESSIAN-a TENSOR IBP: The integrated identity (Step 34 eq 2.4) is tested with q = 3η²a⁴s². The resulting tensor B^{ij} = 2g^{ij}|E|² + 2τE^{ij} - 4E^{ik}E_k^j is QUADRATIC in E (vanishes at E=0), so this is not a bare curvature source. The IBP moves one derivative from ∇²a onto the smooth test weight, producing only terms of the structure εX₆ + C r⁻²J₆. Check that this honest tensor IBP is valid (no IBP on |∇²a|) and that all three branches of the product rule land on the claimed weight exponents.

4. TWO-FACTOR HÖLDER: The defect potential P₆ = ∫Fw₆² is absorbed by P₆ ≤ ‖F‖₂‖w₆‖₄² ≤ γ(X₆ + r⁻²J₆) with γ = S·K₂^{1/2}. This uses ONLY ‖F‖₂, NOT Y = ∫aF³. Verify that this is correct because the defect reaction integrand is aF|E|² (linear in F), unlike the curvature reaction aF³ (cubic in F). Is there any hidden cubic term that would require Y?

5. FINAL GRONWALL: J₆' ≤ C(1+r⁻²)J₆ with no time-dependent coefficient. Compare with A01's route using ∫S²Y ≤ Cγ³. Which is correct? Are they compatible?

6. Are there any terms in the defect evolution that have been dropped or underbounded?

## Integrated Scientific Memo

## 核验结论

在以下条件下，未正则化的 \(J_6\) 持续性论证成立：

- 截断流 \(g(t)\) 在所论时段内光滑存在；
- 移动 Sobolev 常数、支撑区域和度量比较均处于预设 first-exit 范围；
- 同支撑曲率能量给出
  \[
  \gamma(t):=\mathcal S(t)\|F(t)\|_{L^2(U)}\le \gamma_0
  \]
  且 \(\gamma_0\) 足够小。

修正 Step 35 中若干指数和符号笔误后，可严格得到
\[
J_6'+cX_6\le C(1+r^{-2})J_6+CP_6,
\qquad
P_6\le C\gamma(X_6+r^{-2}J_6),
\]
从而
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
\]
该证明只需要 \(K_2\) 控制，不需要 \(Y=\int aF^3\)。

---

## 1. 正则性与精确链式法则

令
\[
s=|E|^2,\qquad E=\operatorname{Ric}+g,\qquad a=\chi^2.
\]
光滑流上 \(E\) 和 \(s\) 都光滑，因此 \(s^3\) 以及测试权
\[
q=3\eta^2a^4s^2
\]
均光滑，在 \(E=0\) 处没有任何奇性。能量恒等式不需要
\((s+\varepsilon^2)^{1/2}\) 正则化。

Sobolev 变量
\[
w_6=\eta a^{5/2}s^{3/2}=\eta\chi^5|E|^3
\]
为 \(C^1\)；这里默认标准截断 \(\chi\ge0\)。映射
\[
E\longmapsto |E|^3
\]
的导数为 \(3|E|\langle E,\cdot\rangle\)，在 \(E=0\) 连续。闭流形的紧致时空子区间上，\(\nabla w_6\) 有界，特别地 \(w_6\in W^{1,2}\)，足以用于 Sobolev 不等式。

精确链式法则为
\[
(\partial_t-a\Delta)s^3
=3s^2(\partial_t-a\Delta)s-6as|\nabla s|^2.
\]
由于 \(a,s\ge0\)，最后一项非正。若
\[
(\partial_t-a\Delta)s=-2a|\nabla E|^2+\Sigma_s,
\]
则主耗散正是
\[
-6\int\eta^2a^5s^2|\nabla E|^2=-6X_6.
\]

---

## 2. Hessian-\(a\) 项的诚实张量分部积分

Hessian 部分在与 \(E\) 收缩后为
\[
T_H=\int q\,(\nabla_i\nabla_j a)B_0^{ij},
\]
其中
\[
B_0^{ij}
=2g^{ij}|E|^2+2\tau E^{ij}-4E^{ik}E_k{}^j,
\qquad \tau=\operatorname{tr}E.
\]
这是 \(E\) 的二次齐次张量，因此
\[
B_0|_{E=0}=0,\qquad
|B_0|\le Cs,\qquad
|\nabla B_0|\le Cs^{1/2}|\nabla E|.
\]
故不存在“裸”曲率源或与 \(E\) 无关的源项。

正确的分部积分是
\[
\int q\,a_{ij}B_0^{ij}
=-\int a_j\nabla_i(qB_0^{ij}),
\]
而不是对 \(|\nabla^2a|\) 分部积分。闭流形上无边界项；\(d\eta\) 分支因
\(a=da=0\) 于 \(\operatorname{supp}d\eta\) 而消失。

对
\[
q=3\eta^2a^4s^2
\]
展开后，三个非零分支为：

1. **导数落在 \(a^4\)：**
   \[
   a^3|da|^2s^3
   =4a^4|d\chi|^2s^3
   \le Cr^{-2}a^4s^3.
   \]

2. **导数落在 \(s^2\)：**
   \[
   a^4|da|\,s|\nabla s|\,|B_0|
   \le Ca^4|da|s^{5/2}|\nabla E|.
   \]

3. **导数落在 \(B_0\)：**
   \[
   a^4|da|s^2|\nabla B_0|
   \le Ca^4|da|s^{5/2}|\nabla E|.
   \]

后两项由 Young 不等式给出
\[
\int \eta^2a^4|da|s^{5/2}|\nabla E|
\le \varepsilon X_6
 +C_\varepsilon\int\eta^2a^3|da|^2s^3
\le \varepsilon X_6+C_\varepsilon r^{-2}J_6.
\]
因此
\[
|T_H|\le \varepsilon X_6+C_\varepsilon r^{-2}J_6.
\]

Step 34 (2.4) 中其余
\[
q[-\tau\langle da,d\tau\rangle+2E(da,d\tau)]
\]
项也满足同一估计，因为
\[
|d\tau|\le C|\nabla E|,
\]
且测试后同样产生
\[
a^4|da|s^{5/2}|\nabla E|.
\]

---

## 3. Step 35 必须修正的文字错误

以下是实质上需要改正的笔误：

1. §3.5(i) 中应为
   \[
   a^3|da|^2s^3,
   \]
   不是 \(a^3|da|^2s^2\)。

2. §3.5(iii) 和 §3.6 中的交叉项应为
   \[
   a^4|da|s^{5/2}|\nabla E|,
   \]
   不是 \(s^{3/2}\)。只有 \(s^{5/2}\) 经 Young 后精确留下
   \(r^{-2}J_6\)。

3. §2.2 的概括性界中，一阶截断项自然是
   \[
   |\nabla a|\,s^{1/2}|\nabla E|,
   \]
   而非 \(|\nabla a||\nabla E|s\)。

4. 体积形式符号应为
   \[
   \partial_t d\mu
   =\frac12\operatorname{tr}_g(\partial_tg)d\mu
   =-a\tau\,d\mu,
   \]
   不是 \(+a\tau\,d\mu\)。由于这里只取绝对值，此笔误不影响估计。

配套脚本的权重核算采用的是上述正确指数，因此脚本与最终结论一致，但 Step 35 正文目前不宜原样引用。

---

## 4. 两因子 Hölder 吸收及支撑条件

定义
\[
P_6=\int\eta^2a^5Fs^3=\int Fw_6^2.
\]
直接 Hölder 给出
\[
P_6\le \|F\|_{L^2(\operatorname{supp}w_6)}\|w_6\|_4^2.
\]
而
\[
\begin{aligned}
\nabla w_6
={}&(d\eta)a^{5/2}s^{3/2}
+\frac52\eta a^{3/2}(da)s^{3/2}\\
&+\frac32\eta a^{5/2}s^{1/2}\nabla s .
\end{aligned}
\]
第一项消失；第二项平方后为
\[
C\eta^2a^4|d\chi|^2s^3\le Cr^{-2}J_6;
\]
第三项满足
\[
\eta^2a^5s|\nabla s|^2
\le4\eta^2a^5s^2|\nabla E|^2.
\]
故
\[
\|\nabla w_6\|_2^2\le C(X_6+r^{-2}J_6),
\qquad
\|w_6\|_2^2=\int\eta^2a^5s^3\le J_6.
\]
Sobolev 不等式遂给出
\[
P_6\le C\mathcal S\,
 \|F\|_{L^2(\operatorname{supp}w_6)}
 (X_6+r^{-2}J_6).
\]

若
\[
K_2=\int\eta^2F^2
\]
且 \(\eta=1\) 于 \(\operatorname{supp}a\)，那么
\[
\operatorname{supp}w_6\subseteq\operatorname{supp}a,
\qquad
\|F\|_{L^2(\operatorname{supp}w_6)}\le K_2^{1/2}.
\]
这是所需支撑论证；不能仅由 \(a,\eta\le1\) 推出。于是
\[
P_6\le C\gamma(X_6+r^{-2}J_6),
\qquad
\gamma=\mathcal S K_2^{1/2}.
\]

---

## 5. 不存在要求 \(Y\) 的隐藏三次曲率项

缺陷方程的反应结构为
\[
a\,\operatorname{Rm}*E
\]
以及关于 \(E\) 的低阶项。对 \(s=|E|^2\) 而言，曲率反应为
\[
a\,\operatorname{Rm}*E*E,
\]
测试后恰产生
\[
\int\eta^2a^5Fs^3=P_6,
\]
即对 \(F\) 仅线性。

移动范数可能产生关于 \(E\) 的三次项，但
\[
a|E|^3=as^{3/2}\le CaFs,
\]
因为 \(|E|\le CF\)。它仍归入 \(P_6\)，不是 \(F^3\) 项。截断项经上述张量分部积分归入 \(X_6+r^{-2}J_6\)。因此没有遗漏的
\[
F^3,\quad F^2s
\]
或与 \(E\) 无关的曲率源。

这与曲率能量不同：曲率自身演化含
\(\operatorname{Rm}^3\)，所以其能量估计才自然需要
\[
Y=\int aF^3.
\]

---

## 6. Gronwall 与 A01 路线的关系

汇总所有项并吸收小的 cutoff 交叉项后，
\[
J_6'+cX_6
\le C(1+r^{-2})J_6+CP_6.
\]
若 \(C\gamma_0<c/2\)，则
\[
J_6'+\frac c2X_6
\le C(1+r^{-2})J_6,
\]
从而
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
\]

A01 的三因子分解
\[
P_6\le \varepsilon X_6
 +C_\varepsilon\mathcal S^2Y\,J_6
\]
也是合法的，并借助
\[
\int_0^T\mathcal S^2Y\,dt\le C\gamma^3
\]
得到有限 Gronwall 指数。两条路线并不矛盾：

- A01 用 \(L^3\) 型曲率种子 \(Y\)；
- 两因子路线直接用 \(L^2\) 曲率控制 \(K_2\)。

对于线性于 \(F\) 的缺陷反应，后一条更直接，消除了 \(q=3\) 曲率种子的依赖；但仍依赖 first-exit 区间内 \(\mathcal S(t)\) 与 \(K_2(t)\) 的统一控制。

---

## 最终判定

修正上述笔误并明确支撑关系后，六项关键主张均成立，且未发现被遗漏或低估到需要 \(Y\) 的缺陷演化项。最稳妥的引理表述应当是一个**条件性 PDE 能量引理**：它不自行证明退化截断流的存在、移动 Sobolev/支撑比较、\(K_2\) 持续性或 first-exit 闭合，但在这些假设下，未正则化的 \(J_6\) 持续性证明完整有效。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 58,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step58_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step58_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the curvature all-p and Moser part of Step 58, distinct from the Step 39 defect ladder. Starting from the exact weighted curvature inequality K_p'+dissipation <= C p^N(1+r^-2+S^2 Y)K_p and the positive-slab bound S^2Y<=C Gamma^3/t, check the time-slab recurrence, correct use of z_p, all powers of S,t,H(0),Gamma, and the conclusion ||a F_T(t)||_infty <= C Gamma/t. Determine whether the displayed recurrence M_{3p/2} <= C S (L M_p)^(3/2) is actually justified by the available sup K_p and integrated gradient terms, including any missing square roots or time factors. State a corrected recurrence and endpoint if needed.

## Integrated Scientific Memo

## 核验结论

在把以下三点明确写入假设后，Step 58 的曲率 Moser 迭代成立：

1. Sobolev 常数采用约定
   \[
   \|u\|_4^2\le \mathcal S\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr);
   \]
2. 正时间 slab 上有一致估计
   \[
   \mathcal S(s)^2Y(s)\le \frac{C\Gamma^3}{t},
   \qquad s\in[t/2,t];
   \]
3. first-exit 区间内 \(\Gamma\le \Gamma_*\)，且通常取
   \(t\le \theta r^2,\ r\le1\)。

显示的递推
\[
\mathcal M_{3p/2}\le C\mathcal S(L\mathcal M_p)^{3/2}
\]
没有缺平方根，也没有缺时间因子；但 \(L\) 必须同时支配 Sobolev 中的 \(r^{-2}K_p\) 项和反应项 \(\Gamma^3/t\)。若不作这种放大，需使用下述更精确的递推。

---

## 1. 权重与插值

令
\[
K_p=\int\eta^2a^{p-2}F^p,\qquad
z_p=\eta a^{(p-1)/2}F^{p/2},\qquad p\ge3.
\]
因 \(\eta=1\) 于 \(\operatorname{supp}a\)，
\[
K_{2p}=\|z_p\|_4^4.
\]
并且 Cauchy–Schwarz 给出
\[
K_{3p/2}
\le K_p^{1/2}K_{2p}^{1/2},
\]
因为 \(a\) 与 \(F\) 的指数分别满足
\[
\frac{p-2}{2}+(p-1)=\frac{3p}{2}-2,\qquad
\frac p2+p=\frac{3p}{2}.
\]

特别地，
\[
z_3=\eta aF^{3/2},
\]
其平方含 \(a^2\)，正好匹配 \(p=3\) 方程的耗散。变量
\(\eta a^{1/2}F^{3/2}\) 不匹配，不能替代。

---

## 2. 时间截断后的正确能量估计

从
\[
K_p'+c\{pD_p^T+p(p-2)D_p^F\}
\le Cp^N(1+r^{-2}+\mathcal S^2Y)K_p
\]
以及 slab 上
\[
\mathcal S^2Y\le C\Gamma^3/t,
\]
对嵌套区间 \(I_j=[\tau_j,t]\) 使用时间截断，可得
\[
\sup_{I_{j+1}}K_{p_j}
+\int_{I_{j+1}}\|\nabla z_{p_j}\|_2^2
\le L_j\,\mathcal M_{p_j,j},
\qquad
\mathcal M_{p,j}:=\int_{I_j}K_p,
\]
其中安全的选择是
\[
\boxed{
L_j=Cp_j^{N+2}
\left(\frac{4^j}{t}+1+r^{-2}+\frac{\Gamma^3}{t}\right).}
\]
这里使用
\[
\|\nabla z_p\|_2^2
\le Cp^2(D_p^T+D_p^F+r^{-2}K_p).
\]

在 \(\Gamma\le\Gamma_*\)、\(t\le r^2\le1\) 下，可以粗化为
\[
L_j\le C_{\Gamma_*}p_j^{N+2}4^j(t^{-1}+r^{-2}),
\]
这正是 Step 58 的写法。其常数隐含依赖固定的 first-exit 阈值
\(\Gamma_*\)。

---

## 3. 递推的严格推导

逐时间片，
\[
K_{2p}^{1/2}=\|z_p\|_4^2
\le\mathcal S\bigl(\|\nabla z_p\|_2^2+r^{-2}K_p\bigr).
\]
所以
\[
\begin{aligned}
\mathcal M_{3p/2,j+1}
&\le
\bigl(\sup_{I_{j+1}}K_p\bigr)^{1/2}
\int_{I_{j+1}}K_{2p}^{1/2}\\
&\le
\mathcal S
\bigl(\sup_{I_{j+1}}K_p\bigr)^{1/2}
\left[
\int_{I_{j+1}}\|\nabla z_p\|_2^2
+r^{-2}\int_{I_{j+1}}K_p
\right].
\end{aligned}
\]
因此不作额外放大时，精确递推是
\[
\boxed{
\mathcal M_{3p/2,j+1}
\le
C\mathcal S\,
(L_j\mathcal M_{p,j})^{1/2}
(L_j+r^{-2})\mathcal M_{p,j}.}
\]
若 \(L_j\ge r^{-2}\)，便化为
\[
\boxed{
\mathcal M_{3p/2,j+1}
\le C\mathcal S(L_j\mathcal M_{p,j})^{3/2}.}
\]

故显示的 \(3/2\) 次方完全有依据。平方根来自
\((\sup K_p)^{1/2}\)，另一个整次因子来自
\(\int K_{2p}^{1/2}\)；没有遗漏平方根。关键是积分
\(K_{2p}^{1/2}\)，而非 \(K_{2p}\)，所以每步只有一个
\(\mathcal S\)。

---

## 4. 迭代指数与端点

取
\[
p_j=3(3/2)^j,\qquad m_j=\mathcal M_{p_j,j}^{1/p_j}.
\]
则
\[
m_{j+1}
\le(C\mathcal S)^{2/(3p_j)}L_j^{1/p_j}m_j.
\]
而
\[
\sum_{j\ge0}\frac1{p_j}=1,\qquad
\frac23\sum_{j\ge0}\frac1{p_j}=\frac23,
\]
且所有 \(p_j^{N+2}\)、\(4^j\) 因子形成收敛乘积。因此，在 first-exit 简化后的 \(L_j\) 下，
\[
\|aF_T(t)\|_\infty
\le
\frac{C_{\Gamma_*}}{t}\,
\mathcal S^{2/3}\mathcal M_{3,0}^{1/3}.
\]
种子为
\[
\mathcal M_{3,0}
=\int_{t/2}^tY(s)\,ds
\le C\Gamma H(0),
\]
故
\[
\|aF_T(t)\|_\infty
\le\frac{C_{\Gamma_*}}{t}
\mathcal S^{2/3}(\Gamma H(0))^{1/3}.
\]
若
\[
\mathcal S H(0)^{1/2}\le C\Gamma
\]
（Step 58 的 first-exit 比较），则
\[
\mathcal S^{2/3}(\Gamma H(0))^{1/3}
=\Gamma^{1/3}\bigl(\mathcal S H(0)^{1/2}\bigr)^{2/3}
\le C\Gamma.
\]
因此
\[
\boxed{\|aF_T(t)\|_\infty\le C_{\Gamma_*}\Gamma/t.}
\]

若不吸收 \(\Gamma^3/t\)，可安全写成
\[
\boxed{
\|aF_T(t)\|_\infty
\le
\frac{C(1+\Gamma^3)}{t}\,
\mathcal S^{2/3}(\Gamma H(0))^{1/3}
\le \frac{C(1+\Gamma^3)\Gamma}{t}.}
\]
不能简单声称“精确依赖必为 \(\Gamma^4/t\)”：\(L_j\) 是若干项之和，其迭代贡献应为 \(1+\Gamma^3\) 型，而不是纯 \(\Gamma^3\) 型。小参数区间 \(\Gamma\le\Gamma_*\) 内，这仍给出所需线性上界。

---

## 最终判断

- \(z_p\) 及全部 \(a\)-权重正确；
- \(\mathcal S\) 的总幂为 \(2/3\)，时间总幂为 \(t^{-1}\)，种子幂为 \(1/3\)；
- Step 58 的显示递推成立，但应注明 \(L_j\ge r^{-2}\) 且包含或吸收 \(\Gamma^3/t\)；
- 在 first-exit 小参数假设下，
  \[
  \|aF_T(t)\|_\infty\le C\Gamma/t
  \]
  确实成立，不需要 \(Y(0)\)，也不使用 Step 39 的 defect ladder。
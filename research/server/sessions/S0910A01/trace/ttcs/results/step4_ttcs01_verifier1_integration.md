# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 4,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step4_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step4_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the Step 4 mathematical correction and route reorientation for Yau Problem 26. Ground your answer in the provided files. In particular: (1) verify or correct the derivation D_a=I-(2/3)(a^+)^2 <= J-q with I-J=A-k and q=k-A/3, and the conclusion D_a/A->0 when delta_->0 and k/A->1/3; (2) verify the source-based equality mechanism of LeBrun's mixed Seiberg-Witten estimate (almost-Kähler structure, lowest W_+ eigenspace, s+s* constant, exact blow-up equality obstruction), distinguishing it from the withdrawn Weyl-only/harmonic-F_A+ argument; (3) check the corrected interpretation of bare ALE cores versus corrected gluing; (4) assess whether the Taub-Bolt-AdS boundary sampler supports only the stated conclusion that exact zero-defect fillings exist for attained boundary Cauchy data, not a general cap lower bound. Give a direct scientific memo identifying any mistakes, missing assumptions, and the most consequential next mathematical/computational test.

## Integrated Scientific Memo

# Step 4 数学复核备忘录

## 结论

Step 4 的路线重定向总体正确，但有三处必须收紧：

1. \(D_a\le J-q\) 完全正确；由此推出 \(D_a/A\to0\) 还必须明确证明体积满足 \(\operatorname{Vol}(g)=O(A)\)。
2. LeBrun 的等号机制确实来自混合标量–Weyl 估计及其 almost-Kähler 等号分析，而非已撤回的“\(F_A^+\) 调和/Weyl-only”论证。
3. Taub–Bolt 计算只证明：对该族实际达到的边界 Cauchy 数据存在零缺陷填充。它既不能给出一般 cap 下界，也不能仅凭当前有限采样刻画完整的可达边界数据集。

---

## 1. 缺陷计算

由
\[
I-J=A-k,\qquad q=k-\frac A3
\]
有精确恒等式
\[
\begin{aligned}
D_a
&=I-\frac23(a^+)^2\\
&=J+A-k-\frac23(a^+)^2\\
&=J-q-\frac23\bigl((a^+)^2-A\bigr).
\end{aligned}
\]
对 LeBrun 符号选择得到的 monopole class，\((a^+)^2\ge A\)，故
\[
\boxed{0\le D_a\le J-q}.
\]
左端来自 LeBrun 2001 Proposition 3.1。因此同时得到 \(J\ge q\)。

### \(J/A\to0\) 所需的完整条件链

令
\[
\delta=\sup_M\|g^{-1}(\operatorname{Ric}+g)\|_{\mathrm{op}}.
\]
若 \(\operatorname{Ric}+g\) 的特征值为 \(\epsilon_i\)，\(|\epsilon_i|\le\delta\)，则
\[
|\mathring r|^2
=\sum_{i=1}^4(\epsilon_i-\bar\epsilon)^2
\le \sum_i\epsilon_i^2\le4\delta^2.
\]
从而
\[
J\le \frac{\delta^2}{2\pi^2}\operatorname{Vol}(g).
\]

这里必须补上 \(\operatorname{Vol}(g)=O(A)\)。一种直接证明使用
\[
8\pi^2\chi(M)
=\int_M\left(|W|^2+\frac{s^2}{24}
-\frac{|\mathring r|^2}{2}\right)d\mu.
\]
由于 \(|s+4|\le4\delta\)，
\[
8\pi^2\chi(M)\ge
\left[\frac23(1-\delta)^2-2\delta^2\right]\operatorname{Vol}(g).
\]
对充分小的 \(\delta\)，括号为正。因此只要
\[
\frac{\chi(M)}A=O(1),
\]
便有 \(\operatorname{Vol}(g)/A=O(1)\)，进而
\[
\frac JA=O(\delta^2).
\]

对 \(M=X\#k\overline{\mathbb{CP}}^{\,2}\)、\(X\) 为最小一般型曲面，该拓扑有界性成立：Noether 不等式给出
\[
A=c_1^2(X)\ge2\chi_{\mathrm{hol}}(X)-6,
\]
故
\[
c_2(X)=12\chi_{\mathrm{hol}}(X)-A\le5A+36,
\]
而
\[
\chi(M)=c_2(X)+k.
\]
当 \(k/A\to1/3\) 时，\(\chi(M)/A\) 一致有界。

因此，在这些假设下，
\[
\frac JA\to0,\qquad
\frac qA=\frac{k}{A}-\frac13\to0,
\]
并由
\[
0\le\frac{D_a}{A}\le\frac JA-\frac qA
\]
得到
\[
\boxed{\frac{D_a}{A}\to0}.
\]

若 \(X\) 只是任意具有 monopole class 的四流形，而没有 \(\chi(M)/A=O(1)\) 或等价体积控制，则 \(\delta\to0\) 本身不足以推出该结论。Step 4 中“由 CGB 体积上界”应展开为上述假设和推导。

### 全符号平均

若所有
\[
a_\varepsilon=c_1(X)+\sum_j\varepsilon_jE_j
\]
均为可用 monopole classes，则
\[
2^{-k}\sum_\varepsilon(a_\varepsilon^+)^2
=(c_1(X)^+)^2+\sum_j(E_j^+)^2.
\]
取平方最大的符号并用 \((c_1(X)^+)^2\ge A\)，得到
\[
I\ge\frac23\left(A+\sum_j(E_j^+)^2\right),
\]
于是
\[
\boxed{J\ge q+\frac23\sum_j(E_j^+)^2}.
\]
所以
\[
\frac1A\sum_j(E_j^+)^2\to0
\]
确为实际 Ricci-pinched 度量的推论，而不是交叉形式本身的结论。

---

## 2. LeBrun 混合估计及等号机制

所附 LeBrun 2001 原文支持 Step 4 的来源修正。正确证明链是：

1. Seiberg–Witten spinor Weitzenböck 公式；
2. 自对偶二形式 Weitzenböck 公式；
3. 使用
   \[
   \varphi=\sigma(\Phi)=-iF_A^+
   \]
   及
   \[
   |\varphi|^2=\frac18|\Phi|^4,\qquad
   |\nabla\varphi|^2\le\frac12|\Phi|^2|\nabla\Phi|^2;
   \]
4. 引入 \(W_+\) 的最低特征值 \(w\)，得到 Proposition 2.1 的 \(L^3\) 估计；
5. 共形变换使 \(s+3w\) 为非正常数；
6. 用
   \[
   w\ge-\sqrt{\frac23}|W_+|
   \]
   得到
   \[
   \int_M
   \left(\frac23s-2\sqrt{\frac23}|W_+|\right)^2d\mu
   \ge32\pi^2(a^+)^2;
   \]
7. 再由三角不等式和二维 Cauchy–Schwarz 推出
   \[
   \frac1{4\pi^2}\int_M
   \left(\frac{s^2}{24}+2|W_+|^2\right)d\mu
   \ge\frac23(a^+)^2.
   \]

### 撤回论证为何错误

Seiberg–Witten 方程只给出 \(F_A^+=i\sigma(\Phi)\)。Bianchi 恒等式是 \(dF_A=0\)，并不推出 \(dF_A^+=0\)，所以 \(F_A^+\) 一般不调和。原文只使用：

\[
-2\pi a^+
\quad\text{是}\quad \sigma(\Phi)
\quad\text{的调和投影}.
\]

只有在等号情形下，\(\sigma(\Phi)\) 才被迫等于相应调和代表。所给来源也不支持一个可替代上述混合估计的 Weyl-only 下界。

### 精确等号机制

LeBrun Proposition 2.4 确实给出：

- \(g\) 为 almost-Kähler；
- almost-Kähler 形式 \(\omega\) 点态属于 \(W_+\) 的最低特征子空间；
- 
  \[
  s+s^*
  \]
  为非正常数，其中
  \[
  s^*=\frac s3+2W_+(\omega,\omega);
  \]
- almost-complex 第一 Chern 类与相关 spin\(^c\) 第一 Chern 类一致；
- 对最终较强后继估计的等号，\(W_+\) 还必须是 \(J\)-不变的。

若饱和度量同时 Einstein，则 Corollary 2.5 经 Armstrong 推出它是 Kähler–Einstein。

### 吹起等号阻碍

LeBrun Proposition 3.2 的机制也被 Step 4 正确描述：等号迫使
\[
[\omega]\cdot E_j=0,
\]
而改变异常类符号后的 Seiberg–Witten 信息与 Taubes 理论给出异常类的伪全纯球代表，其辛面积必须为正，却又等于上述零配对，矛盾。因此 \(k>0\) 时精确等号不可能。

但该论证没有给出统一定量间隙。异常球面积可能趋于零；所以
\[
D_a/A\to0
\]
尚不能直接推出近 almost-Kähler 几何。塌缩、共形因子退化、spinor 零集及 Weyl 能量集中都可能阻断紧性。Step 4 将此作为尚待证明的 quantitative stability/concentration–compactness 问题，是正确的。

---

## 3. 裸 ALE 核与修正 gluing

若 \(h\) 为 Ricci-flat ALE 度量，\(g_t=t^2h\)，则
\[
g_t^{-1}(\operatorname{Ric}_{g_t}+g_t)=I.
\]
故裸核相对于目标 \(\operatorname{Ric}=-g\) 的无权算子缺陷恒为 \(1\)，与尺度无关。这只排除了未修正的 Ricci-flat 核。

若在缩放坐标中
\[
g_t=t^2(h+t^2k),
\]
则形式上
\[
\operatorname{Ric}(h+t^2k)
=t^2D\operatorname{Ric}_h(k)+O(t^4),
\]
所以
\[
g_t^{-1}(\operatorname{Ric}(g_t)+g_t)
=
h^{-1}\!\left(D\operatorname{Ric}_h(k)+h\right)+O(t^2).
\]
因此相对 \(O(t^2)\) 的 **\(C^2\)** 修正确实能改变阶一 Ricci 端同态；仅有 \(C^0\) 小量不够。

实际构造仍需解决 gauge-fixed 线性 Einstein 方程、核/余核投影、ALE 增长条件、边界 Cauchy 匹配及非线性迭代。首个 obstruction 为零只消除首阶障碍，不保证完整 gluing 存在。Step 4 保留 corrected gluing 路线是合理的。

---

## 4. Taub–Bolt–AdS sampler 的证据范围

脚本中的公式与 Akbar 的 \(\Lambda=-1\) Taub–Bolt–AdS 公式一致：

\[
0<L^2\le\frac{2-\sqrt3}{4},\qquad
\rho_b=\frac{1\pm\sqrt{1+16L^4-16L^2}}{4L},
\]
以及
\[
a^2=\rho^2-L^2,\qquad
b^2=\frac{4L^2\Delta}{\rho^2-L^2}.
\]
第二基本形式比值的计算也正确。\(p=1\) 的截断 bolt 拓扑可读为 \(\mathcal O(-1)\to S^2\) 的圆盘丛，即按标准复定向为 \(\overline{\mathbb{CP}}^{\,2}\) 去掉一个球；Akbar 的 \(CP^2\) 说法涉及定向约定。

因此可严格采用的结论是：

> 对每个由正则 Taub–Bolt 参数实际达到的有限截面第一、第二基本形式数据，存在一个光滑 \(\operatorname{Ric}=-g\) 的异常柄型填充。

于是，如果 cap 优化不固定边界数据，只在此拓扑的允许填充中取 Ricci 残差下确界，该下确界为零。故不能从“自由 cap 残差”推出一般正下界。

不能推出：

- 任意指定 \((a,b,K)\) 都可实现；
- 任意外部 collar 都可匹配；
- 过渡区能保持小的无权 Ricci 缺陷；
- 固定边界 Cauchy 数据的 cap 问题没有正下界；
- 当前有限网格给出的 \(b/a\) 数值范围是完整参数像。

尤其，JSON 中 `ricci_defect_sup: 0.0` 是按解析 Einstein 性直接写入，并非脚本数值计算了 Ricci 张量。目标 \(b/a=0.5,1,2,4\) 返回同一个 \(b/a\approx0.397\) 样本，只表示这些目标没有被当前网格达到，不应解释为对应边界数据的近似填充。

Akbar 原文另声称任意 Berger Dirichlet 数据均有 Taub–Bolt 填充；当前脚本没有重验其七次多项式和去平方后的分支条件。有限采样与该定理表面上的差异，不能据此宣称一般“squashing ceiling”；需要直接求解未平方的边界方程才能判定。

---

## 最关键的下一项检验

最有判别力的下一步是**完整 Cauchy 数据匹配加线性余核测试**。

定义 bolt cap 的数据映射
\[
\mathcal C_{\rm cap}(L,\rho)
=(a,b,\alpha,\beta),
\qquad
\alpha=\frac{a'}a,\quad \beta=\frac{b'}b,
\]
并从实际候选外部——例如 Kähler–Einstein orbifold 去球后的 collar——提取
\[
\mathcal C_{\rm ext}(\theta).
\]
若两边均使用各自向外法向，平滑拼接要求
\[
(a,b)_{\rm cap}=(a,b)_{\rm ext},\qquad
(\alpha,\beta)_{\rm cap}=-(\alpha,\beta)_{\rm ext}.
\]

应同时计算：

1. 该数据映射的完整像，而非有限网格范围；
2. 与真实外部数据的最小 Cauchy 失配；
3. gauge-fixed 线性 Einstein 算子的余核投影；
4. 若失配和投影趋零，过渡解是否满足
   \[
   \sup\|g^{-1}(\operatorname{Ric}+g)\|_{\rm op}\to0.
   \]

这会直接区分两种情形：局部 exact bolt 能通过 corrected gluing 产生临界反例候选，或者其边界/余核失配必然留下阶一缺陷。

并行的核心理论缺口是 LeBrun 证明链的定量稳定性定理：从
\[
\delta_i\to0,\qquad D_{a_i}/A_i\to0
\]
控制 SW spinor、共形极小化因子和 Weyl 集中，从而产生受控的近 almost-Kähler 结构。没有该定理，精确等号下的 Taubes 矛盾尚不能升级为近等号矛盾。

最后，Step 4 所称 “Ishida–LeBrun Theorem 7 中 \(k+4=A/3\) 或 \(k+8=A/3\)” 无法由给出的 `math/0111228` 核验：该文件的 Theorem 7 是 Bauer 的 smash-product 定理。该具体阈值及编号必须回到实际引用的 Spin-Manifolds 文本核对，不能由当前来源支持。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 5,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step5_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step5_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the proposed h=0 Einstein-gap theorem for minimal Kähler surfaces of general type: alpha=inf E should be zero by orbifold/ALE approximation; alpha is attained exactly when the underlying smooth four-manifold admits some Einstein metric, not necessarily Kähler; if K is ample Aubin-Yau supplies a negative Kähler-Einstein metric, while if K is nef nonample Kähler-Einstein attainment is impossible but non-Kähler Einstein existence may remain. Read the Step 4 Y-test and the actual Ozuch higher-order source. Determine precisely what Ozuch's first and second compact obstructions say for A1/Eguchi-Hanson resolution of a negative Kähler-Einstein orbifold. In particular, check whether the rank-one Kähler-Einstein curvature block automatically satisfies not just det R+=0 but also Ozuch's stronger second obstruction, and hence whether that source excludes or leaves open nearby non-Kähler Einstein metrics. Give a theorem with exact hypotheses and a corrected status of the unresolved part.

## Integrated Scientific Memo

## 核验结论

设 \(M\) 是紧致极小一般型 Kähler 曲面 \((X,J)\) 的底层定向光滑四维流形，并定义
\[
\mathcal E(g)=\inf_{\lambda\neq 0}
\frac{\int_M |\Ric_g-\lambda g|^2\,d\mu_g}
{\lambda^2\Vol_g(M)},\qquad
\alpha(M)=\inf_g\mathcal E(g).
\]

正确结论是：

1. \(\alpha(M)=0\)；
2. \(\alpha(M)\) 被达到，当且仅当 \(M\) 承载某个非 Ricci-flat Einstein 度量；
3. 若 \(K_X\) ample，则 Aubin–Yau 给出负 Kähler–Einstein 度量，故达到；
4. 若 \(K_X\) nef 但非 ample，只能断言**固定复结构 \(J\)** 下不存在 Kähler–Einstein 度量；底层光滑流形可能因另一复结构而仍承载 Kähler–Einstein 度量，更不用说非 Kähler Einstein 度量；
5. 对负 Kähler–Einstein \(A_1\) orbifold，Ozuch 的方向化第一障碍只允许
   \[
   \zeta\in\ker \mathbf R^+=\omega^\perp;
   \]
   对这些允许方向，其第二障碍自动消失。因而 Ozuch 的论文并不排除邻近的非 \(J\)-Kähler Einstein 解消，也不证明其存在。

这里
\[
\mathbf R^\pm=W^\pm+\frac{s}{12}I_{\Lambda^\pm}
\]
是完整 Riemann 曲率算子在 \(\Lambda^\pm\) 上的块，而不是单独的 \(W^\pm\)。

---

# 1. \(h=0\) 的精确定理

### 定理 A：零 Einstein 间隙及达到

设 \((X,J)\) 是紧致极小一般型 Kähler 曲面，\(M\) 是其底层光滑四维流形。则：

\[
\boxed{\alpha(M)=0.}
\]

此外，对任意光滑度量 \(g\)，
\[
\mathcal E(g)=0
\quad\Longleftrightarrow\quad
\Ric_g=\lambda g\ \text{且}\ \lambda\neq0.
\]
因此
\[
\boxed{\alpha(M)\text{ 被达到}
\iff M\text{ 承载非零 Einstein 常数的 Einstein 度量}.}
\]

在通常的 canonical-class monopole 输入成立时，这种 Einstein 度量必有 \(\lambda<0\)。为避免 \(b^+=1\) 的 chamber 细节，最干净的无条件表述仍是“\(\lambda\neq0\)”；若要统一声称“必为负”，应明确引用相应的 Seiberg–Witten/Yamabe 非正性结论及其 chamber 假设。

### 证明：\(\alpha(M)=0\)

令
\[
\pi:X\longrightarrow X_{\rm can}
\]
为 canonical model。它收缩全部 \((-2)\)-曲线；\(X_{\rm can}\) 具有 ADE 型 Du Val 奇点，且 \(K_{X_{\rm can}}\) ample。取其负 Kähler–Einstein orbifold 度量 \(g_0\)，归一化为
\[
\Ric(g_0)=-g_0.
\]

在每个 ADE 奇点插入相应的 Kronheimer Ricci-flat hyperkähler ALE 空间，并在 \(r\asymp\varepsilon^{1/2}\) 截断。局部有
\[
g_0=e+O(r^2),\qquad
g_{{\rm ALE},\varepsilon}=e+O(\varepsilon^4r^{-4}).
\]
所得光滑度量 \(g_\varepsilon\) 满足
\[
\Vol(g_\varepsilon)\to\Vol(g_0)>0,\qquad
\int_M|\Ric(g_\varepsilon)+g_\varepsilon|^2\,d\mu_{g_\varepsilon}
=O(\varepsilon^2).
\]

这里 Step 4 的体积叙述应细化：只有 ALE 的固定紧核体积是 \(O(\varepsilon^4)\)；截断半径以内的整个 Ricci-flat plateau 体积一般是 \(O(\varepsilon^2)\)。但该区上
\[
\Ric=0,\qquad |\Ric+g|^2=|g|^2=4,
\]
故仍只贡献 \(O(\varepsilon^2)\)。过渡环带的体积也是 \(O(\varepsilon^2)\)，曲率误差有界，因而总误差仍趋于零。于是取 \(\lambda=-1\) 得
\[
0\le \mathcal E(g_\varepsilon)
\le
\frac{\int_M|\Ric(g_\varepsilon)+g_\varepsilon|^2\,d\mu_{g_\varepsilon}}
{\Vol(g_\varepsilon)}
\longrightarrow0.
\]

### 证明：达到等价于 Einstein 存在

由材料中的恒等式
\[
\mathcal E(g)=4-\frac{I^2}{VR}
=\frac{4P+L_s}{R},
\]
其中
\[
P=\int|\Ric^\circ|^2,\qquad
L_s=\int(s-\bar s)^2,
\]
只要 \(R>0\)，便有
\[
\mathcal E(g)=0
\iff P=0,\quad L_s=0.
\]
这等价于 \(\Ric^\circ=0\) 且 \(s\) 为非零常数，即
\[
\Ric_g=\lambda g,\qquad \lambda\neq0.
\]
Ricci-flat 时按所给定义 \(\mathcal E=4\)，故不产生零值。

---

# 2. Kähler–Einstein 达到：必须区分固定复结构与底层流形

若 \(K_X\) ample，Aubin–Yau 给出与 \(J\) 相容的负 Kähler–Einstein 度量，故 \(\alpha(M)=0\) 被达到。

若 \(K_X\) nef 但非 ample，则对某条 \((-2)\)-曲线 \(E\) 有
\[
K_X\cdot E=0.
\]
若存在与 \(J\) 相容的负 Kähler–Einstein 度量，则
\[
[\rho]=2\pi c_1(X)=-2\pi c_1(K_X),\qquad
\rho=\lambda\omega,\quad \lambda<0,
\]
所以
\[
c_1(K_X)=\frac{-\lambda}{2\pi}[\omega]
\]
是 Kähler 类，从而 \(K_X\) ample，矛盾。因此：

\[
\boxed{K_X\text{ nef 非 ample }\Longrightarrow
(X,J)\text{ 不存在 }J\text{-Kähler--Einstein 度量}.}
\]

但不能由此推出底层 \(M\) 不存在 Kähler–Einstein 度量。若 canonical model \(X_{\rm can}\) 存在平滑化 \(X_t\)，则 ADE 奇点的 Milnor fibre 与最小解消在相关四维拓扑意义下给出同一底层光滑流形，而光滑 fibre 的 canonical bundle 为 ample；于是 Aubin–Yau 在另一复结构上给出 Kähler–Einstein 度量。因此应把 Step 4 中

> “\(Y\) has no Kähler–Einstein metric”

改成

> “\((Y,J)\) has no Kähler–Einstein metric.”

故 nef 非 ample 情形的正确状态是：

- 原复结构下的 KE 达到不可能；
- 另一复结构下的 KE 达到可能；
- 不与任何复结构相容的 Einstein 达到也未被排除；
- 全局达到问题仍恰好是底层 \(M\) 的 Einstein 存在问题。

---

# 3. Ozuch 的第一、第二个 \(A_1\)/Eguchi–Hanson 障碍

设 \((X_0,g_0)\) 是紧致 Einstein 四维 orbifold，
\[
\Ric(g_0)=\Lambda g_0,
\]
奇点为 \(\mathbb R^4/\mathbb Z_2\)，且 Einstein 无穷小变形可积。假设光滑 Einstein 度量通过 Eguchi–Hanson bubbling 收敛到 \(g_0\)。令 \(\sigma=\pm\) 表示插入的手性，\(\zeta\in\Lambda^\sigma_p\) 是 EH period/gluing 向量。

## 3.1 第一障碍是方向化条件，而不只是行列式

Ozuch §2.1.1 给出
\[
\lambda_k(\zeta^\sigma)
=
c\left\langle
\mathbf R^\sigma_{g_0}(p)\zeta^\sigma,\,
\zeta_{(k)}^\sigma
\right\rangle,\qquad c>0.
\]
因此所有第一阶系数消失等价于
\[
\boxed{\mathbf R^\sigma_{g_0}(p)\zeta=0.}
\]

所以
\[
\det \mathbf R^\sigma(p)=0
\]
只是“存在某个可用核方向”的方向无关必要条件。对已经指定的 EH 插入，真正需要的是
\[
\zeta\in\ker\mathbf R^\sigma(p).
\]

这正是 Step 4 需要修正之处：“\(\det\mathbf R^+=0\)，故 leading obstruction 满足”并不充分；还必须检查所选 gluing 向量。

## 3.2 第二障碍

假设第一障碍已消失，取正交基使 \(\zeta=e_1\)。则
\[
\mathbf R^\sigma(p)=
\begin{pmatrix}
0&0&0\\
0&R_{22}&R_{23}\\
0&R_{23}&R_{33}
\end{pmatrix}.
\]
Ozuch §2.1.4 给出
\[
\mu_1
=
C\det
\begin{pmatrix}
R_{22}&R_{23}\\
R_{23}&R_{33}
\end{pmatrix},
\qquad C>0.
\]
第二障碍要求 \(\mu_1=0\)，即在已经存在的核方向之外，\(\mathbf R^\sigma\) 还必须再有一个零方向。由于
\[
\tr\mathbf R^\sigma=\frac{s}{4}=\Lambda,
\]
其目标形式为
\[
\boxed{
\mathbf R^\sigma(p)
\sim\diag(0,0,\Lambda).
}
\]

但这个较强结论不是对任意 GH 收敛序列无条件成立。Ozuch 的 Theorem 0.2 / Proposition 0.4 在以下附加情形得到它：

- 序列 transverse；
- \(\Lambda=0\) 且序列 nondegenerate；
- orbifold 只有一个奇点且序列 nondegenerate；
- stable Ricci-flat 解消序列；
- 或 orbifold 单奇点且 rigid。

对这里的 \(\Lambda<0\) Kähler–Einstein 情形，直接相关的是 transverse 分支，以及单奇点的 nondegenerate/rigid 分支；Ricci-flat 专用分支不适用。

---

# 4. 负 Kähler–Einstein 曲率块同时通过第二障碍

在复定向下，Kähler–Einstein 四维度量满足
\[
W^+
=
\diag\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right)
\]
于基
\[
\left(\widehat\omega,\Re\Theta,\Im\Theta\right)
\]
中，其中 \(\widehat\omega\) 是归一化 Kähler 形式。因此
\[
\mathbf R^+
=
W^++\frac{s}{12}I
=
\diag\left(\frac{s}{4},0,0\right)
=
\diag(\Lambda,0,0).
\]
所以
\[
\det\mathbf R^+=0,\qquad
\dim\ker\mathbf R^+=2,\qquad
\ker\mathbf R^+=\omega^\perp.
\]

由此得到精确答案：

\[
\boxed{
\text{负 Kähler--Einstein 的 rank-one }\mathbf R^+
\text{ 自动满足 Ozuch 的第二障碍，}
}
\]
但第一障碍只对核方向成立。

更具体地：

- 若
  \[
  \zeta\in\omega^\perp,
  \]
  则 \(\mathbf R^+\zeta=0\)，第一障碍成立；
- 在 \(\zeta^\perp\) 上，\(\mathbf R^+\) 的特征值为 \(0,\Lambda\)，故
  \[
  \mu_1=C(0\cdot\Lambda)=0;
  \]
- 若
  \[
  \zeta\parallel\omega,
  \]
  则
  \[
  \mathbf R^+\zeta=\Lambda\zeta\neq0,
  \]
  第一障碍已经失败。

因而必须区分两种 EH 方向：

1. **保持原复结构的 crepant/Kähler resolution 方向**  
   \(\zeta\parallel\omega\)。它被第一障碍排除，与 \(K_Y\cdot E=0\)、\(K_Y\) 非 ample 的复几何障碍一致。

2. **旋转的 hyperkähler / smoothing-type 方向**  
   \(\zeta\in\omega^\perp\)。它同时通过 Ozuch 的第一和第二障碍，通常不保持原复结构 \(J\)。

这也与存在全局平滑化时的 Kähler–Einstein smoothing 序列相容：这种序列必沿第一、第二障碍允许的 vanishing-cycle 方向，而不是沿固定 \(J\) 的 holomorphic resolution 方向。

---

# 5. Ozuch 来源究竟排除什么、留下什么

Ozuch 的高阶论文在这里给出的是**必要条件**：

- 第一障碍排除 \(J\)-holomorphic EH resolution 方向；
- 对 \(\zeta\in\omega^\perp\)，第二障碍自动满足；
- 论文没有由此构造 Einstein 解消；
- 也没有证明所有更高阶局部障碍或全局 compact obstructions \(\nu_l\) 消失。

因此准确结论是：

\[
\boxed{
\text{该来源不排除邻近 orbifold 的非 }J\text{-Kähler Einstein 度量。}
}
\]

它留下的精确未决对象包括：

1. 沿 \(\omega^\perp\) 的后续高阶局部障碍；
2. orbifold Einstein 变形所产生的全局障碍 \(\nu_l\)；
3. 多奇点间的尺度、方向及全局相互作用；
4. canonical model 不可全局平滑时，局部 smoothing directions 是否能组合成真实 Einstein 解消；
5. 即使邻近 orbifold 的所有解消都被排除，\(M\) 是否在远离该 orbifold 的区域承载其他 Einstein 度量。

此外，所读正文的显式二阶公式针对 \(A_1\)/Eguchi–Hanson。论文 Remark 2.21 只说明 \(D_k,E_k\) 有相似推广，而较高 \(A_k\) 还涉及曲率导数。因此不能把此处 \(A_1\) 的“第二障碍自动消失”未经额外证明推广到 Step 4 的所有 \(A_{k-1}\) 链。

---

# 6. 建议采用的修正版定理

### 定理 B：一般型极小曲面的 \(h=0\) 状态

设 \((X,J)\) 是紧致极小一般型 Kähler 曲面，\(M\) 为底层定向光滑四维流形。

1. **零间隙**
   \[
   \alpha(M)=0.
   \]

2. **达到**
   \[
   \alpha(M)\text{ 被达到}
   \iff
   M\text{ 存在 }\Ric_g=\lambda g,\ \lambda\neq0.
   \]
   在适用的 canonical monopole/Yamabe 假设下，必有 \(\lambda<0\)。

3. **ample 情形**  
   若 \(K_X\) ample，则 Aubin–Yau 给出与 \(J\) 相容的负 Kähler–Einstein 度量，故达到。

4. **nef 非 ample 情形**  
   与固定 \(J\) 相容的 Kähler–Einstein 度量不存在。但 \(M\) 仍可能：
   - 对另一复结构承载 Kähler–Einstein 度量，例如 canonical model 存在适当平滑化时；
   - 或承载非 Kähler Einstein 度量。  
   因而一般的达到问题仍未解决。

5. **\(A_1\) 邻近解消的 Ozuch 条件**  
   再设 canonical model 的奇点全为 \(A_1\)，其负 Kähler–Einstein orbifold 度量具有可积 Einstein 变形，并考虑在复定向插入 Eguchi–Hanson 的 Einstein 收敛序列。则每个极限 EH 向量必须满足
   \[
   \zeta_j\in\ker\mathbf R^+(p_j)=\omega(p_j)^\perp.
   \]
   所以固定 \(J\) 的 holomorphic resolution 方向 \(\zeta_j\parallel\omega\) 被排除。对所有允许的 \(\zeta_j\in\omega^\perp\)，Kähler–Einstein rank-one 曲率块
   \[
   \mathbf R^+=\diag(\Lambda,0,0)
   \]
   自动满足 Ozuch 的第二障碍。在 Ozuch 定理要求的 transverse、单奇点 nondegenerate 或 rigid 等附加假设下，第二障碍不再提供进一步排除。

最终状态不是“higher-order obstruction 尚未检查”，而是更精确的：

> Ozuch 已计算的第二个 compact obstruction 对负 Kähler–Einstein rank-one 曲率块自动消失；因此该论文明确留下了 kernel/smoothing-type 非 \(J\)-Kähler Einstein 解消的可能性。真正未决的是更高阶及全局障碍与实际存在性。
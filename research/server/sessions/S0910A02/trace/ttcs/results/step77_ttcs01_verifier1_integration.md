# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 77,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step77_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step77_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following structural theorem about the Ozuch desingularization obstruction on the product orbifold (S²×S²)/Z₂ with Ric=Λg, Λ>0.

CLAIM: All local Ozuch second obstruction coefficients μ_k(ζ^ε) = 0 (k=1,2,3) at every A₁ node, for both chiralities ε, in every chirality pattern.

PROOF SKETCH:
1. The degree-4 del Pezzo Bl₄CP² admits KE metrics (Tian 1990). These approach the product orbifold along comparable-scale nondegenerate sequences with compatible (Kähler) EH insertions. Ozuch's necessary conditions t²μ_k = O(t^{5/2}) at comparable scales force μ_k = 0 (since μ_k is t-independent).
2. The reflection c(z,w)=(z̄,w) is an isometry fixing every A₁ node and exchanging chiralities. Since R⁺=R⁻ and ∇Rm≡0, local μ_k are c-equivariant, giving μ_k(ζ⁻) = μ_k(ζ⁺) = 0.
3. D₈ symmetry and ∇Rm≡0 give node independence.

POTENTIAL ISSUES TO CHECK:
(a) Does the del Pezzo KE desingularization truly approach the product orbifold at comparable scales? The four A₁ points have Z₂-permutation symmetry; does the family preserve this?
(b) Is μ_k truly t-independent in Ozuch's framework? The h₂ and h₄ equations (eqs (22)-(23)) define μ_k from the source Λ·eh - Q^(2)(h₂,h₂), which depends on the orbifold geometry and EH direction but not the scale t. Verify.
(c) Does the c-equivariance argument correctly identify μ_k(ζ⁻) with μ_k(ζ⁺)? The key point is that c maps the SD kernel basis to the ASD kernel basis while preserving the local curvature structure (since R⁺=R⁻).
(d) Is there any gap between 'existence of KE desingularization' and 'Ozuch's necessary conditions vanish'? Ozuch's equations are necessary for any nearby Einstein metric; the KE metrics exist; so the equations must be satisfied. But check whether the KE metrics are nondegenerate in Ozuch's sense (Definition 1.26).

## Integrated Scientific Memo

# 核验结论

所给材料**尚不足以证明 CLAIM 的全部内容**。目前可严格确认的是

\[
\boxed{\mu_1(\zeta^\varepsilon)=0}
\]

对每个节点、两种手征以及每个 \(\zeta^\varepsilon\in\ker R^\varepsilon\) 都成立。  
而

\[
\boxed{\mu_2=\mu_3=0}
\]

只有在补足特定 KE 退化与 Ozuch 参数匹配后才能由证明草图推出；这些关键环节在现有材料中没有得到证明。故原证明草图应判为**有实质缺口，而非已验证定理**。

## 1. 已严格成立的部分：\(\mu_1=0\)

产品轨形每个 \(A_1\) 点处都有

\[
R^+=R^-=\operatorname{diag}(\Lambda,0,0),\qquad
\ker R^\pm=\operatorname{span}\{\omega_2^\pm,\omega_3^\pm\}.
\]

Ozuch Lemma 2.14 所给公式为

\[
\mu_1=C\det\!\left(R^\varepsilon\big|_{\ker R^\varepsilon}\right).
\]

这里核上的 \(2\times2\) 块恒为零，故

\[
\mu_1=0.
\]

这不依赖 KE 退化，也不依赖节点间相互作用。

相比之下，秩一曲率结构本身不能推出 \(\mu_2=\mu_3=0\)。若
\(\rho(\zeta)^-=(0,\cos\alpha,\sin\alpha)\)，则

\[
12\pi_{\rm tr}(\rho\otimes\rho)=
\begin{pmatrix}
-4&0&0\\
0&12\cos^2\alpha-4&12\sin\alpha\cos\alpha\\
0&12\sin\alpha\cos\alpha&12\sin^2\alpha-4
\end{pmatrix}.
\]

其核平面上的特征值为 \(8,-4\)，并不为零。因此虽然
\(R^-\rho(\zeta)^-=0\)，完整 Biq16 二阶公式仍可能含有非零的
\(dR\) 项；现有代数计算没有算出 \(\mu_2,\mu_3\)。

## 2. \(\mu_k\) 的尺度独立性：正确，但需规范表述

写 EH 参数为

\[
\zeta=t\phi,\qquad \|\phi\|=1.
\]

Ozuch 展开中的尺度独立对象是

\[
\lambda_k(\phi,v),\qquad \mu_k(\phi,v),
\]

而 \(t,t^2\) 是显式阶数因子。固定轨形背景、归一化方向 \(\phi\) 和
\(v=0\) 后，定义 \(h_2,h_4\) 的源

\[
\Lambda\,\mathrm{eh}-Q^{(2)}(h_2,h_2)
\]

不含胶合尺度 \(t\)。因此“固定方向上的 \(\mu_k\) 与 \(t\) 无关”是正确的。

但仅凭

\[
t^2\mu_k=O(t^{5/2})
\]

推出 \(\mu_k=0\)，要求 Ozuch 方程中的一阶项确实满足足够强的消失条件，不能只知道其极限方向落在曲率核中。

## 3. KE 控制论证缺少的关键参数匹配

Ozuch 必要条件的实际形式是

\[
t_j\lambda_k^j(\phi_j(t),v(t))
+t_j^2\mu_k^j(\phi_j(t),v(t))
=O(t_{\max}^{5/2}).
\]

若整个序列中

\[
\lambda_k^j(\phi_j(t),v(t))=o(t_j),
\qquad t_j\asymp t_{\max},
\]

则除以 \(t_j^2\) 后确可推出

\[
\mu_k^j(\phi_{j,0},0)=0.
\]

然而若

\[
\phi_j(t)=\phi_{j,0}+t_j\dot\phi_j+o(t_j),\qquad
v(t)=t_jv_1+o(t_j),
\]

即使 \(\lambda(\phi_{j,0},0)=0\)，也可能有

\[
\lambda(\phi_j(t),v(t))
=t_j\!\left(D_\phi\lambda(\dot\phi_j)+D_v\lambda(v_1)\right)+o(t_j).
\]

此时二阶方程只给出

\[
D_\phi\lambda(\dot\phi_j)+D_v\lambda(v_1)
+\mu(\phi_{j,0},0)=0,
\]

不能单独推出 \(\mu=0\)。因此证明草图必须证明以下至少一种陈述：

1. KE 序列在 Ozuch 规范中始终保持
   \(\phi_j(t)\in\ker R^\varepsilon\)，且 \(v(t)=0\)；或
2. 更一般地，
   \(\lambda_k^j(\phi_j(t),v(t))=o(t_j)\)。

现有文件没有提供这种局部参数匹配定理。四个标量零模

\[
u_1g_1,\ u_1g_2,\ u_2g_1,\ u_2g_2
\]

确实属于 Ozuch 的完整 \(L^2\) 核；若整个 KE 平滑族及其规范均保持 \(A\)-对称，它们可由奇偶性排除，但现有材料没有构造并验证这样的完整等变规范化。

## 4. “光滑 del Pezzo KE 存在”不自动给出所需退化

仅引用 Tian 的光滑 del Pezzo KE 存在性，不足以证明所需的退化序列。还需证明或精确引用：

1. 存在平滑族
   \[
   \mathcal X\to\Delta,\qquad
   \mathcal X_0=(\mathbb{CP}^1\times\mathbb{CP}^1)/\mathbb Z_2,
   \]
   一般纤维为光滑四次 del Pezzo；
2. 其归一化 KE 度量收敛到指定的产品轨形 KE 度量；
3. 四个泡均为 Kähler-compatible EH 泡；
4. 四个尺度可比，最好由延拓到总空间的传递对称性得到相等尺度；
5. 该序列满足 Ozuch Definition 1.26 及 Theorem 0.2 的全部非退化和多节点假设。

中央纤维有节点置换对称性，并不意味着任意平滑路径保持该对称性。现有材料没有给出具体等变平滑族，也没有核验 Definition 1.26。因此问题 (a) 和 (d) 均未解决。

还有一个必须纠正的几何错误：四次 del Pezzo 是

\[
\operatorname{Bl}_5\mathbb{CP}^2
\cong \mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2,
\]

不是材料中多次写出的 \(\operatorname{Bl}_4\mathbb{CP}^2\)；后者是五次 del Pezzo。

## 5. 反射换手征：成立，但应表述为协变关系

反射

\[
c(z,w)=(\bar z,w)
\]

是产品度量的等距映射，固定四个极点节点，与商作用相容，并反转四维定向，因此交换

\[
\Lambda^+\longleftrightarrow\Lambda^-.
\]

Ozuch 的局部方程、二次 Einstein 项及正交归一化在等距映射下自然。因此正确关系是

\[
\boldsymbol\mu^{-}(c_*\phi)
=
U_c\,\boldsymbol\mu^{+}(\phi),
\]

其中 \(U_c\) 是传输后阻碍基之间的正交变换。只有在 ASD 基明确取为 SD 基的 \(c\)-传输时，才可逐分量写成相等。

这一区别不影响零性：

\[
\boldsymbol\mu^+=0\quad\Longrightarrow\quad
\boldsymbol\mu^-=0.
\]

故问题 (c) 基本解决，但证明草图中的逐分量等式应改成上述协变公式。

## 6. 节点与核方向的覆盖

节点等价可由归一化商作用的产品等距映射得到；\(\nabla\mathrm{Rm}=0\) 进一步保证各节点具有相同局部曲率喷流。因此一旦某节点某手征的局部系数向量恒为零，零性可传到所有节点。

但单条 KE 序列通常只实现一个极限 EH 方向。要覆盖整个

\[
\ker R^\varepsilon\simeq\mathbb R^2
\]

还应使用局部等距协变性：两个球因子的轴向旋转在 SD 和 ASD 核平面上分别以角组合 \(\alpha+\beta\)、\(\alpha-\beta\) 作用，且对单位圆传递。因此某一非零方向上的系数向量为零，可推出同一手征所有单位方向上的系数向量为零。这里需要的是等距协变性，而不只是笼统的“SO(2) 下系数独立”。

## 7. 最强可证结论

现有证据支持：

\[
\boxed{
\mu_1(\zeta^\varepsilon)=0
\quad
\text{于所有节点、两种手征和所有核方向。}
}
\]

并支持以下条件命题：

\[
\boxed{
\begin{gathered}
\text{若存在满足 Ozuch Definition 1.26 的四节点可比尺度 KE 退化，}\\
\text{且其 Ozuch 参数满足 }\lambda_k(\phi_j(t),v(t))=o(t_j),\\
\text{则 }\mu_2=\mu_3=0
\text{ 于一个 compatible 方向；}\\
\text{再由核平面旋转、反射和节点等距性推广到全部情形。}
\end{gathered}}
\]

因此对原 CLAIM 的核验结果是：

\[
\boxed{\text{尚未验证；}\ \mu_2,\mu_3\text{ 仍是精确未决对象。}}
\]

最直接的闭合方式是把完整 Biq16 公式在一个便利方向（如
\(\zeta=\omega_2^+\)）逐项代入；核平面旋转、反射及节点对称随后自动覆盖所有方向、手征和节点。另一条路线则必须补齐具体等变 KE 平滑族、可比尺度、Definition 1.26 非退化性以及 \(\lambda=o(t)\) 的参数匹配证明。

最后，即使所有局部 \(\mu_k\) 均为零，混合手征节点间项仍可在

\[
t_it_j^2\,\mathcal I_{ij,k}=O(t^3)
\]

出现；它小于 Ozuch 当前的 \(O(t^{5/2})\) 余项，却可能控制更高阶构造。因此局部 \(\mu\)-消失不能单独推出所有手征模式均可 Einstein 解奇。
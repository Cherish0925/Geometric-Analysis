# TTCS Independent Branch Record

```json
{
  "step_id": 35,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/scripts/step35_tensor_hessian_verification.py",
    "Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md"
  ]
}
```

## Task

Verify the index-level derivation of the two Hessian-a contraction tensors for the normalized cutoff flow dt g = -2a(Ric+g) on a 4-manifold. Specifically check:

1. CURVATURE TENSOR: Starting from the standard all-lower Riemann variation formula dt R_{ijkl} = g_{lp}[nabla_j(delta Gamma^p_{ik}) - nabla_i(delta Gamma^p_{jk})] + R_{ijk}^p h_{lp}, with h = -2aE and E = Ric+g, the Hessian-a terms in dt|Rm|^2 give Sigma_H = 8 A_{pq} B^{pq}_curv where B^{pq}_curv = R^p_j^q_l E^{jl}. Verify the pair-symmetry and antisymmetry reductions that eliminate two of the four terms and double the remaining two. Check the derivative structure |nabla B_curv| <= CF|nabla Rm| from the explicit product rule. Does this correctly use |nabla E| = |nabla Ric| <= C|nabla Rm|?

2. DEFECT TENSOR: Starting from the Besse Theorem 1.174 Ricci linearization 2(DRic)[h]_{ij} = g^{kl}(-nabla_k nabla_l h_{ij} + nabla_k nabla_i h_{jl} + nabla_k nabla_j h_{il} - nabla_i nabla_j h_{kl}) + curvature terms, extract the Hessian-a part of dt E_{ij} and show the contribution to dt|E|^2 is Sigma_H^E = 2 A_{pq} B^{pq}_def where B_def = s g^{pq} + tau E^{pq} - 2(E^2)^{pq}. Verify this matches A03's formula (which has 2*B_def due to test function convention).

3. NORMALIZATION CANCELLATION: Verify that the +g in E = Ric+g produces no additional quadratic curvature term in the algebraic/lowering variation, only the normalization lowering -2aR_{ijkl}, because R_{ijkl} - R_{ijkl} = 0 from the skew symmetry R_{ijlk} = -R_{ijkl}.

4. DISSIPATION: Verify the pre-absorption dissipation is -pD_p^Rm - p(p-2)D_p^F, not -p(p-3)D_p^F.

## Output

## 科学核验备忘录

四个目标公式均可由所给变分公式推出。曲率收缩的最终系数 \(8\)、缺陷收缩的最终系数 \(2\)，以及两个耗散系数都正确。有两处中间文字需要修正：

1. 曲率收缩中第 3、4 项相等依赖两对指标同时反对称，不是单独由 pair symmetry 得到。
2. \(B_{\mathrm{def}}\) 的导数可直接得到更强的全局估计
   \[
   |\nabla B_{\mathrm{def}}|\le C|E||\nabla E|,
   \]
   无需使用文中并不成立的一般反向估计
   \(|\nabla\mathrm{Rm}|\lesssim |\nabla E|+1\)。

### 1. 曲率的 Hessian-\(a\) 收缩

令 \(A_{ij}=\nabla_i\nabla_j a\)。由 \(h=-2aE\)，

\[
(\delta\Gamma^p_{ik})_{\nabla a}
=-(\nabla_i a)E_k{}^p-(\nabla_k a)E_i{}^p
+(\nabla^p a)E_{ik}.
\]

代入

\[
\partial_tR_{ijkl}
=g_{lp}\bigl[\nabla_j\delta\Gamma^p_{ik}
-\nabla_i\delta\Gamma^p_{jk}\bigr]
+R_{ijk}{}^ph_{lp},
\]

只保留 \(\nabla^2a\) 项，两个 \(A_{ij}E_{kl}\) 项因
\(A_{ij}=A_{ji}\) 相消，得到

\[
(H_a)_{ijkl}
=-A_{jk}E_{il}-A_{il}E_{jk}
+A_{ik}E_{jl}+A_{jl}E_{ik}.
\]

令

\[
X=R^{ijkl}A_{ik}E_{jl},\qquad
S_1=R^{ijkl}A_{jk}E_{il},\qquad
S_2=R^{ijkl}A_{il}E_{jk}.
\]

曲率对称性给出：

\[
S_1=S_2
\]

由 \(R^{ijkl}=R^{klij}\) 及 \(A,E\) 的对称性得到；同时

\[
S_1=-X
\]

由交换 \(i,j\) 及第一对指标反对称性得到。最后，

\[
R^{ijkl}A_{jl}E_{ik}=X
\]

由同时交换 \(i\leftrightarrow j\)、\(k\leftrightarrow l\)，两次反对称符号相消得到。因此

\[
R^{ijkl}(H_a)_{ijkl}
=-S_1-S_2+X+X=4X,
\]

从而

\[
\boxed{
\Sigma_H^{\mathrm{Rm}}
=2R^{ijkl}(H_a)_{ijkl}
=8R^{ijkl}A_{ik}E_{jl}
=8A_{pq}B_{\mathrm{curv}}^{pq}
}
\]

其中

\[
\boxed{
B_{\mathrm{curv}}^{pq}
=R^p{}_j{}^q{}_lE^{jl}.
}
\]

所以最终系数 \(8\) 正确。Step 35 中“第 3、4 项由同一个 pair-symmetry argument 相等”的表述不准确：pair exchange 分别把这两项送回自身；它们相等使用的是两对指标同时反对称。

导数结构也是正确的。由于 \(\nabla g=0\)，

\[
\nabla_rB_{\mathrm{curv}}^{pq}
=(\nabla_rR^p{}_j{}^q{}_l)E^{jl}
+R^p{}_j{}^q{}_l\nabla_rE^{jl}.
\]

又因为

\[
\nabla E=\nabla\operatorname{Ric},\qquad
(\nabla_r\operatorname{Ric})_{ij}
=g^{kl}(\nabla_rR)_{kilj},
\]

故

\[
|\nabla E|=|\nabla\operatorname{Ric}|
\le C(n)|\nabla\operatorname{Rm}|.
\]

此外

\[
|E|\le |\operatorname{Ric}|+|g|
\le C(n)(|\operatorname{Rm}|+1)\le C F.
\]

于是

\[
\boxed{
|\nabla B_{\mathrm{curv}}|
\le C F|\nabla\operatorname{Rm}|.
}
\]

这里使用 \(\nabla E=\nabla\operatorname{Ric}\) 完全正确。

### 2. 缺陷的 Hessian-\(a\) 收缩

将 \(h=-2aE\) 代入所列 Ricci 线性化公式，四个二阶导数项分别贡献

\[
\begin{aligned}
-\nabla_k\nabla_lh_{ij}
&\rightsquigarrow 2A_{kl}E_{ij},\\
+\nabla_k\nabla_ih_{jl}
&\rightsquigarrow -2A_{ki}E_{jl},\\
+\nabla_k\nabla_jh_{il}
&\rightsquigarrow -2A_{kj}E_{il},\\
-\nabla_i\nabla_jh_{kl}
&\rightsquigarrow 2A_{ij}E_{kl}.
\end{aligned}
\]

收缩 \(k,l\) 并除以公式左侧的系数 \(2\)，得到

\[
(\partial_t\operatorname{Ric}_{ij})_{\nabla^2a}
=(\Delta a)E_{ij}
-A_i{}^lE_{jl}
-A_j{}^lE_{il}
+A_{ij}\tau.
\]

因为 \(\partial_tg=-2aE\) 不含 \(\nabla^2a\)，

\[
\boxed{
(\partial_tE_{ij})_{\nabla^2a}
=(\Delta a)E_{ij}
-A_i{}^lE_{jl}
-A_j{}^lE_{il}
+A_{ij}\tau.
}
\]

这也可直接从上一节的 \(H_{kilj}\) 收缩得到，是两个变分计算之间的独立一致性验证。

记 \(s=|E|^2\)。逆度量变分不含 \(\nabla^2a\)，故

\[
\begin{aligned}
\Sigma_H^E
&=2E^{ij}(\partial_tE_{ij})_{\nabla^2a}\\
&=2s\,\Delta a
-4A_{pq}(E^2)^{pq}
+2\tau A_{pq}E^{pq}\\
&=2A_{pq}
\left(sg^{pq}+\tau E^{pq}-2(E^2)^{pq}\right).
\end{aligned}
\]

因此

\[
\boxed{
B_{\mathrm{def}}^{pq}
=sg^{pq}+\tau E^{pq}-2(E^2)^{pq},
\qquad
\Sigma_H^E=2A_{pq}B_{\mathrm{def}}^{pq}.
}
\]

A03 使用测试函数 \(q=3\eta^2a^4s^2\)，所以其被积张量为

\[
q\,(2B_{\mathrm{def}})
=q\left(2sg+2\tau E-4E^2\right),
\]

与 A03 的公式完全一致。

此外，由 \(\tau=\operatorname{tr}E\)，

\[
|\nabla\tau|\le C|\nabla E|,
\qquad
|\nabla(E^2)|\le C|E||\nabla E|,
\]

所以直接有

\[
\boxed{
|\nabla B_{\mathrm{def}}|
\le C|E||\nabla E|
=C s^{1/2}|\nabla E|.
}
\]

这在所有 \(E\) 上成立，不需要先假设 \(|E|\) 很小。Step 35 §6.3 中经过
\(|\nabla\mathrm{Rm}|\lesssim|\nabla E|+1\) 的路线应删去，因为 Ricci 的导数只是 \(\nabla\mathrm{Rm}\) 的收缩，不能一般地反向控制完整的 \(\nabla\mathrm{Rm}\)。

### 3. \(E=\operatorname{Ric}+g\) 中 \(+g\) 的归一化项

单独取 \(h^{(g)}=-2ag\)，则

\[
\delta\Gamma^p_{ik}[h^{(g)}]
=-(\nabla_i a)\delta_k^p-(\nabla_k a)\delta_i^p
+(\nabla^p a)g_{ik}.
\]

因此连接变分只产生 \(H_a(A,g)\)，没有含 \(aR\) 的连接代数项。显式 lowering 项为

\[
R_{ijk}{}^ph^{(g)}_{lp}
=-2aR_{ijkl}.
\]

若把 Ricci-flow 二阶项通过交换协变导数改写，来自 \(E_l{}^p\) 和
\(E_k{}^p\) 中恒等映射的部分正比于

\[
R_{ijkp}\delta_l^p+R_{ijlp}\delta_k^p
=R_{ijkl}+R_{ijlk}=0.
\]

所以在代数/lowering 部分，

\[
\boxed{
(+g)\text{ 的唯一剩余项为 }-2aR_{ijkl}.
}
\]

对空间变化的 \(a\)，\(+g\) 仍会进入前述 Hessian-\(a\) 张量
\(H_a(A,g)\)；“唯一”仅指代数/lowering 部分。

作为缩放交叉验证，在 \(a=1,E=g\) 时，lowering 对
\(\partial_t|\mathrm{Rm}|^2\) 的贡献为 \(-4|\mathrm{Rm}|^2\)，四个逆度量贡献合计 \(+8|\mathrm{Rm}|^2\)，净值为 \(+4|\mathrm{Rm}|^2\)。四维体积元变化率为 \(-4\)，故
\(\int|\mathrm{Rm}|^2d\mu\) 不变。

### 4. 耗散系数

扩散项测试为

\[
\frac p2\int
\eta^2a^{p-2}F^{p-2}\,a\Delta(F^2)
=
\frac p2\int
\eta^2a^{p-1}F^{p-2}\Delta(F^2).
\]

对其积分分部，导数落在 \(F^{p-2}\) 上时给出

\[
-p(p-2)
\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2
=-p(p-2)D_p^F.
\]

导数落在 \(a^{p-1}\) 上产生 \(\nabla a\)-交叉项，随后由 Young 不等式处理；它不是径向耗散的来源。显式 Bochner 项给出

\[
\frac p2\int
\eta^2a^{p-2}F^{p-2}
(-2a|\nabla\mathrm{Rm}|^2)
=-pD_p^{\mathrm{Rm}}.
\]

因此处理交叉项以前的两个有利平方项确为

\[
\boxed{
-pD_p^{\mathrm{Rm}}-p(p-2)D_p^F.
}
\]

特别在 \(p=3\) 时仍有 \(-3D_3^F\)；\(-p(p-3)D_p^F\) 不是该积分分部的系数。

最后，`step35_tensor_hessian_verification.py` 中 C1–C4、D1–D6 等核心张量项目主要是 `check(..., True, ...)`，并未进行指标数组或符号张量运算；其作用是记录公式和检验标量指数。上面的逐指标推导才提供这些恒等式的独立数学验证。
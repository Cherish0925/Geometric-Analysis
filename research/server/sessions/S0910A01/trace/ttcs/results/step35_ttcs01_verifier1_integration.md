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
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step35_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step35_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the index-level derivation of the two Hessian-a contraction tensors for the normalized cutoff flow dt g = -2a(Ric+g) on a 4-manifold. Specifically check:

1. CURVATURE TENSOR: Starting from the standard all-lower Riemann variation formula dt R_{ijkl} = g_{lp}[nabla_j(delta Gamma^p_{ik}) - nabla_i(delta Gamma^p_{jk})] + R_{ijk}^p h_{lp}, with h = -2aE and E = Ric+g, the Hessian-a terms in dt|Rm|^2 give Sigma_H = 8 A_{pq} B^{pq}_curv where B^{pq}_curv = R^p_j^q_l E^{jl}. Verify the pair-symmetry and antisymmetry reductions that eliminate two of the four terms and double the remaining two. Check the derivative structure |nabla B_curv| <= CF|nabla Rm| from the explicit product rule. Does this correctly use |nabla E| = |nabla Ric| <= C|nabla Rm|?

2. DEFECT TENSOR: Starting from the Besse Theorem 1.174 Ricci linearization 2(DRic)[h]_{ij} = g^{kl}(-nabla_k nabla_l h_{ij} + nabla_k nabla_i h_{jl} + nabla_k nabla_j h_{il} - nabla_i nabla_j h_{kl}) + curvature terms, extract the Hessian-a part of dt E_{ij} and show the contribution to dt|E|^2 is Sigma_H^E = 2 A_{pq} B^{pq}_def where B_def = s g^{pq} + tau E^{pq} - 2(E^2)^{pq}. Verify this matches A03's formula (which has 2*B_def due to test function convention).

3. NORMALIZATION CANCELLATION: Verify that the +g in E = Ric+g produces no additional quadratic curvature term in the algebraic/lowering variation, only the normalization lowering -2aR_{ijkl}, because R_{ijkl} - R_{ijkl} = 0 from the skew symmetry R_{ijlk} = -R_{ijkl}.

4. DISSIPATION: Verify the pre-absorption dissipation is -pD_p^Rm - p(p-2)D_p^F, not -p(p-3)D_p^F.

## Integrated Scientific Memo

## 核验结论

四个目标恒等式均正确，但源笔记有两处应修正：

1. 曲率收缩中第 3、4 项相等不能归因于单独的 pair symmetry；需要同时交换两对指标并使用两次反对称性。
2. 缺陷张量应直接使用更强的全局估计
   \[
   |\nabla B_{\rm def}|\le C|E||\nabla E|,
   \]
   源笔记中
   \[
   |\nabla{\rm Rm}|\lesssim |\nabla E|+1
   \]
   的反向控制一般不成立，也完全不需要。

### 1. 曲率 Hessian-\(a\) 收缩

令 \(A_{ij}=\nabla_i\nabla_j a\)。由 \(h=-2aE\)，连接变分中含一阶 \(a\) 的部分为
\[
(\delta\Gamma^p_{ik})_{\nabla a}
=-(\nabla_i a)E_k{}^p-(\nabla_k a)E_i{}^p
+(\nabla^pa)E_{ik}.
\]
代入全降指标曲率变分并仅保留 \(\nabla^2a\) 项，利用 \(A_{ij}=A_{ji}\)，得到
\[
(H_a)_{ijkl}
=-A_{jk}E_{il}-A_{il}E_{jk}
+A_{ik}E_{jl}+A_{jl}E_{ik}.
\]

记
\[
X=R^{ijkl}A_{ik}E_{jl},\quad
S_1=R^{ijkl}A_{jk}E_{il},\quad
S_2=R^{ijkl}A_{il}E_{jk}.
\]
曲率对称性给出：

- 由 pair exchange \(R^{ijkl}=R^{klij}\) 及 \(A,E\) 对称，
  \[
  S_1=S_2.
  \]
- 交换 \(i,j\) 并用第一对反对称性，
  \[
  S_1=-X.
  \]
- 对 \(R^{ijkl}A_{jl}E_{ik}\) 同时交换 \(i\leftrightarrow j\)、
  \(k\leftrightarrow l\)，两次反对称符号相消，故
  \[
  R^{ijkl}A_{jl}E_{ik}=X.
  \]

因此
\[
R^{ijkl}(H_a)_{ijkl}=-S_1-S_2+X+X=4X,
\]
进而
\[
\boxed{
\Sigma_H^{\rm Rm}
=2R^{ijkl}(H_a)_{ijkl}
=8A_{pq}B_{\rm curv}^{pq}},
\qquad
\boxed{
B_{\rm curv}^{pq}=R^p{}_j{}^q{}_lE^{jl}}.
\]
系数 \(8\) 正确。逆度量的变分不含 \(\nabla^2a\)，故此前置系数 \(2\) 没有遗漏。

其导数由乘积法则直接给出：
\[
\nabla_rB_{\rm curv}^{pq}
=(\nabla_rR^p{}_j{}^q{}_l)E^{jl}
+R^p{}_j{}^q{}_l\nabla_rE^{jl}.
\]
由于
\[
\nabla E=\nabla{\rm Ric},\qquad
(\nabla_r{\rm Ric})_{ij}=g^{kl}(\nabla_rR)_{kilj},
\]
所以
\[
|\nabla E|\le C(n)|\nabla{\rm Rm}|.
\]
再由 \(|E|\le C(1+|{\rm Rm}|)\le CF\)、\(|{\rm Rm}|\le F\)，得到
\[
\boxed{
|\nabla B_{\rm curv}|
\le CF|\nabla{\rm Rm}|}.
\]
这里对 \(|\nabla E|=|\nabla{\rm Ric}|\le C|\nabla{\rm Rm}|\) 的使用方向正确。

### 2. 缺陷 Hessian-\(a\) 收缩

将 \(h=-2aE\) 代入给定 Ricci 线性化公式，四个二阶导数项的 Hessian-\(a\) 部分依次为
\[
\begin{aligned}
-\nabla_k\nabla_lh_{ij}&\rightsquigarrow 2A_{kl}E_{ij},\\
+\nabla_k\nabla_ih_{jl}&\rightsquigarrow-2A_{ki}E_{jl},\\
+\nabla_k\nabla_jh_{il}&\rightsquigarrow-2A_{kj}E_{il},\\
-\nabla_i\nabla_jh_{kl}&\rightsquigarrow 2A_{ij}E_{kl}.
\end{aligned}
\]
收缩 \(k,l\)，再除以线性化公式左侧的 \(2\)，有
\[
(\partial_t{\rm Ric}_{ij})_{\nabla^2a}
=(\Delta a)E_{ij}
-A_i{}^lE_{jl}
-A_j{}^lE_{il}
+A_{ij}\tau ,
\qquad \tau=\operatorname{tr}E.
\]
而 \(\partial_tg=-2aE\) 不含 Hessian-\(a\) 项，所以同样有
\[
(\partial_tE_{ij})_{\nabla^2a}
=(\Delta a)E_{ij}
-A_i{}^lE_{jl}
-A_j{}^lE_{il}
+A_{ij}\tau.
\]

令 \(s=|E|^2\)。逆度量变分仍不含 \(\nabla^2a\)，于是
\[
\begin{aligned}
\Sigma_H^E
&=2E^{ij}(\partial_tE_{ij})_{\nabla^2a}\\
&=2s\,\Delta a-4A_{pq}(E^2)^{pq}
+2\tau A_{pq}E^{pq}\\
&=2A_{pq}\left(sg^{pq}+\tau E^{pq}-2(E^2)^{pq}\right).
\end{aligned}
\]
故
\[
\boxed{
\Sigma_H^E=2A_{pq}B_{\rm def}^{pq}},
\qquad
\boxed{
B_{\rm def}^{pq}=sg^{pq}+\tau E^{pq}-2(E^2)^{pq}}.
\]

A03 的张量
\[
2sg^{pq}+2\tau E^{pq}-4(E^2)^{pq}
\]
恰为 \(2B_{\rm def}\)。这是其测试函数记号把
\(\Sigma_H^E=2A:B_{\rm def}\) 中的系数 \(2\) 吸收到被积张量后的结果，因而完全一致。

同时，由
\[
\nabla s=2\langle E,\nabla E\rangle,\qquad
\nabla\tau=\operatorname{tr}(\nabla E),\qquad
\nabla(E^2)=(\nabla E)E+E\nabla E,
\]
直接得到全局估计
\[
\boxed{
|\nabla B_{\rm def}|\le C|E||\nabla E|
=C s^{1/2}|\nabla E|}.
\]
无需 pinching，也不存在额外的 \(C|\nabla E|\) 项。这正好支持 Hessian 项积分分部后的
\(s^{5/2}|\nabla E|\) 结构。

### 3. 归一化项消去

在通过交换协变导数得到的代数项中，\(E_l{}^p\) 和 \(E_k{}^p\) 的恒等映射部分为
\[
R_{ijkp}\delta_l^p+R_{ijlp}\delta_k^p
=R_{ijkl}+R_{ijlk}=0.
\]
故 \(E={\rm Ric}+g\) 中的 \(+g\) 不产生额外的代数二次曲率项。

显式 lowering variation 则留下
\[
R_{ijk}{}^ph_{pl}\big|_{h=-2ag}
=-2aR_{ijkl}.
\]
因此，在代数/lowering 部分，
\[
\boxed{\text{\(+g\) 的唯一剩余贡献是 }-2aR_{ijkl}.}
\]
这里“唯一”不包括空间变化的 \(a\) 所产生的 Hessian-\(a\) 项 \(H_a(A,g)\)。

缩放检验一致：当 \(a=1,E=g\) 时，lowering 对
\(\partial_t|{\rm Rm}|^2\) 贡献 \(-4|{\rm Rm}|^2\)，四个逆度量贡献 \(+8|{\rm Rm}|^2\)，净值
\[
\partial_t|{\rm Rm}|^2=4|{\rm Rm}|^2.
\]
四维中 \(\partial_td\mu=-4d\mu\)，故
\(\int|{\rm Rm}|^2d\mu\) 缩放不变。

### 4. 耗散系数

测试扩散项得到
\[
\frac p2\int\eta^2a^{p-2}F^{p-2}\,a\Delta(F^2).
\]
积分分部后，导数落在 \(F^{p-2}\) 上产生
\[
-p(p-2)\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2
=-p(p-2)D_p^F.
\]
显式 Bochner 项
\(-2a|\nabla{\rm Rm}|^2\) 则产生
\[
-p\int\eta^2a^{p-1}F^{p-2}|\nabla{\rm Rm}|^2
=-pD_p^{\rm Rm}.
\]
导数落在 \(a^{p-1}\) 上的是待 Young 吸收的交叉项，不改变预吸收平方项。因此
\[
\boxed{
-pD_p^{\rm Rm}-p(p-2)D_p^F
}
\]
是正确的预吸收耗散；\(-p(p-3)D_p^F\) 错误。特别 \(p=3\) 时仍保留
\(-3D_3^F\)。

最后，所给 Python 脚本中的核心张量项目大多是 `check(..., True, ...)`，只能记录预期恒等式，并非符号指标验证；上述逐指标计算才构成独立核验。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 49,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step49_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step49_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following chain of reasoning about Einstein metric existence on product-quotient surface resolutions, checking each link for mathematical correctness:

1. HYPERKÄHLER IDENTIFICATION: For the A_1 singularity {uv-w^2=0}, the hyperkähler family of ALE metrics on the resolution T*CP^1 has three real parameters (ζ_1, ζ_2, ζ_3). The ζ_1 direction corresponds to the size of the exceptional CP^1 (Kähler/resolution direction); the (ζ_2, ζ_3) directions correspond to the complex smoothing {uv-w^2=t}. On a product Kähler-Einstein orbifold (Σ_1×Σ_2)/G with Ric=Λg, the curvature operator has R_+=diag(Λ,0,0) with the nonzero eigenvalue in the Kähler form direction and the kernel in the (2,0)+(0,2) directions. Therefore the kernel-directed Eguchi-Hanson replacement (which kills the first Ozuch obstruction) corresponds to a complex smoothing of each A_1 node, not a holomorphic resolution.

2. GLOBAL QG SMOOTHING: For a canonical model Z of a surface of general type with only rational double points (A_1 singularities), a global Q-Gorenstein smoothing exists if H^2(T_Z^0) = 0. By the Burns-Wahl result for RDPs, this equals H^2(T_S) where S is the minimal resolution. By Serre duality, H^2(T_S) = H^0(Ω^1_S ⊗ K_S). The sufficient condition fails (i.e., H^2 > 0) when χ(T_S) = 2K^2-10 > 0, which occurs for K^2 ≥ 6.

3. AMPLENESS PERSISTENCE: If the canonical model Z has a QG smoothing π:Z→Δ with K_{Z/Δ} Q-Cartier, and K_{Z_0} is ample, then K_{Z_t} is ample for small t≠0.

4. AUBIN-YAU: A smooth projective surface with ample canonical bundle carries a unique negative Kähler-Einstein metric with Ric(ω)=-ω.

5. SIMULTANEOUS RESOLUTION: For a flat family of surfaces with ADE singularities, after a finite Weyl-group base change, the family admits a simultaneous resolution. For A_1, this is a Z/2Z base change. The resolved family is smooth, so all fibers are diffeomorphic. The central fiber is the minimal resolution S.

6. CONCLUSION: S is diffeomorphic to Z_t, which carries a KE metric, so the smooth 4-manifold underlying S carries an Einstein metric.

Check each link for correctness. Are there hidden assumptions, missing hypotheses, or known counterexamples to any step?

## Integrated Scientific Memo

## 核验结论

链条 **3–6 在补齐标准假设后成立**，因此可得到严格的条件性定理：

> 若只有 \(A_1\) 奇点的射影 canonical model \(Z\) 存在一个适当的全局 \(\mathbb Q\)-Gorenstein 光滑化，且一般纤维光滑，则 \(Z\) 的极小解消 \(S\) 所在的光滑四维流形承载负 Einstein 度量。

但目前材料没有证明任何具体 product-quotient \(Z\) 确实存在这种全局光滑化。第 1 步还需修正 Weyl 二重覆盖及局部/全局之间的逻辑；第 2 步的 Euler 特征论证只排除了一个**充分条件**，不能证明不可光滑化。

---

## 1. Hyperkähler 参数与曲率核

### 曲率算子部分正确

取复定向。四维 Kähler–Einstein 流形若
\[
\operatorname{Ric}=\Lambda g,\qquad s=4\Lambda,
\]
则在
\[
\Lambda^+=\mathbb R\omega\oplus\Lambda_{\mathbb R}^{2,0}
\]
上
\[
W_+=\operatorname{diag}\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right).
\]
故完整的 self-dual 曲率块
\[
\mathcal R_+=W_++\frac{s}{12}I
\]
满足
\[
\mathcal R_+=\operatorname{diag}(\Lambda,0,0),
\qquad
\ker\mathcal R_+
=\operatorname{span}_{\mathbb R}\{\Re\Omega,\Im\Omega\}.
\]
这适用于两个因子具有相同 Einstein 常数的曲面乘积，并可下降到有限商。

不过，材料中的
\[
R_-= \operatorname{diag}(\Lambda,0,0)
\]
不是一般 Kähler–Einstein 事实；它若用于该特定等曲率乘积，应单独计算。若 ALE 泡的 chirality 反转，相关阻碍块也会从 \(\mathcal R_+\) 换成 \(\mathcal R_-\)。

### ALE 参数解释基本正确，但平滑参数写错了一层

固定一个有标记的 hyperkähler 复结构 \(I\)，令
\[
\zeta_{\mathbb R}=\zeta_1,\qquad
\zeta_{\mathbb C}=\zeta_2+i\zeta_3.
\]
则：

- \(\zeta_{\mathbb C}=0,\ \zeta_{\mathbb R}\neq0\)：原复结构中的 holomorphic resolution；
- \(\zeta_{\mathbb C}\neq0\)：节点的复平滑方向。

但普通半通用形变参数不是直接 \(t=\zeta_{\mathbb C}\)。\(A_1\) Weyl 群作用为
\[
\zeta_{\mathbb C}\mapsto-\zeta_{\mathbb C},
\]
所以在适当归一化下
\[
uv-w^2=t,\qquad t=c\,\zeta_{\mathbb C}^{\,2},\quad c\neq0.
\]
\(\zeta_{\mathbb C}\) 是 Weyl 覆盖上的坐标；\(t\) 才是未标记形变基底上的坐标。这正对应第 5 步的二重基变。

### 与 Ozuch/Biquard 阻碍的联系只能作局部结论

若所用 gluing 公式确实是
\[
\mathcal R_+(p)\zeta=0
\]
（同 chirality、固定 framing），则其核方向位于
\((2,0)+(0,2)\) 平面，因而相对于环境复结构是局部平滑方向，而不是 Kähler resolution 方向。

但源材料没有写出或验证这一首阶阻碍公式。因此“kills the first Ozuch obstruction”仍需以明确的阻碍配对公式核验。更重要的是：

- 这是局部、有标记的 Riemannian 参数识别；
- 它不自动给出 integrable complex deformation；
- 更不自动给出兼容所有节点的全局 \(\mathbb Q\)-Gorenstein family。

所以“局部近 Einstein 构造就是全局 QG smoothability 问题”过强。二者有关联，但由不同的全局兼容性和非线性理论控制。

---

## 2. 全局 \(\mathbb Q\)-Gorenstein 光滑化条件

设
\[
\mathcal T_Z^0=\mathcal Hom(\Omega_Z,\mathcal O_Z),\qquad
\mathcal T_Z^1=\mathcal Ext^1(\Omega_Z,\mathcal O_Z).
\]
局部到整体序列包含
\[
\operatorname{Ext}^1(\Omega_Z,\mathcal O_Z)
\longrightarrow H^0(\mathcal T_Z^1)
\longrightarrow H^2(\mathcal T_Z^0).
\]
每个 \(A_1\) 是 Gorenstein hypersurface，局部平滑方向一维且局部无阻碍。因此
\[
H^2(\mathcal T_Z^0)=0
\]
给出所有局部平滑方向可被整体提升的标准充分条件；再结合 RDP 的局部无阻碍性，可取得同时平滑全部节点的全局形变。由于 \(A_1\) 是 Gorenstein，该形变属于所需 QG 情形。

对于 RDP 的 crepant 极小解消 \(\rho:S\to Z\)，所需 Burns–Wahl 比较为
\[
H^2(Z,\mathcal T_Z^0)\cong H^2(S,T_S).
\]
这不是简单从
\[
0\to T_S(-\log E)\to T_S\to Q\to0
\]
形式推出的。尤其不应无说明地声称
\[
H^2(T_S(-\log E))=H^2(T_S).
\]
上述正合列一般只直接给出相关映射；若要同构，必须引用精确的 Burns–Wahl 结果及其假设。纯 RDP 问题最干净的表述是直接使用
\[
H^2(\mathcal T_Z^0)\cong H^2(T_S).
\]

Serre 对偶也应写成
\[
H^2(S,T_S)^\vee
\cong H^0(S,\Omega_S^1\otimes K_S),
\]
而不是两个向量空间未经对偶的字面相等；其维数相等，消失性等价。

### Euler 特征计算正确，但需要 \(\chi(\mathcal O_S)=1\)

一般公式为
\[
\chi(T_S)=\frac16(7K_S^2-5c_2(S)).
\]
由 Noether 公式
\[
c_2(S)=12\chi(\mathcal O_S)-K_S^2
\]
得到
\[
\chi(T_S)=2K_S^2-10\chi(\mathcal O_S).
\]
只有在 \(p_g=q=0\)、即 \(\chi(\mathcal O_S)=1\) 时，才化为
\[
\chi(T_S)=2K^2-10.
\]

一般型曲面有 \(H^0(T_S)=0\)，故
\[
h^2(T_S)-h^1(T_S)=2K^2-10.
\]
因此当 \(K^2\ge6\) 时
\[
h^2(T_S)\ge 2K^2-10>0.
\]
结论仅是：

> \(H^2=0\) 这一充分判据在 \(K^2\ge6\) 时不可使用。

它**不说明**全局 QG 光滑化不存在。障碍空间非零不等于实际障碍类非零。

对 \(K^2=2,4\)，计算也仅说明 \(H^2=0\) 在数值上可能，完全没有证明它成立。所附 Python 脚本只验证了 Riemann–Roch 算术，没有计算任何具体 \(H^2\)、局部到整体映射或实际障碍类。另不能把 \(h^1(T_S)\) 直接当成 \(Z\) 的 QG 形变空间维数，因为局部 \(T^1\) 项和 Burns–Wahl 映射会介入。

---

## 3. canonical bundle 的 ample 性保持

此步正确，但应明确假设：

- \(\pi:\mathcal Z\to\Delta\) proper、flat；
- 纤维正常且一般纤维光滑；
- 存在固定 \(m>0\)，使
  \[
  L=\omega_{\mathcal Z/\Delta}^{[m]}
  \]
  在中央纤维邻域为线丛，并与各纤维限制相容。

若 \(K_{Z_0}\) ample，则
\[
L|_{Z_0}\cong mK_{Z_0}
\]
ample。proper flat family 中线丛的 ample 性是开条件，故缩小 \(\Delta\) 后
\[
L|_{Z_t}\cong mK_{Z_t}
\]
ample，从而 \(K_{Z_t}\) ample。

仅有各奇点邻域的局部平滑 germ 不足以推出这一步；需要全局 proper QG family。

---

## 4. Aubin–Yau

正确。光滑紧致复曲面若 \(K_{Z_t}\) ample，则它是射影的且
\[
c_1(Z_t)<0.
\]
Aubin–Yau 给出归一化为
\[
\operatorname{Ric}(\omega_t)=-\omega_t
\]
的 Kähler–Einstein 度量。其 Kähler 类为
\[
[\omega_t]=2\pi c_1(K_{Z_t}).
\]
唯一性并非拓扑结论所需，存在性已经足够。

---

## 5. 同时解消及微分同胚

ADE 同时解消结论正确，但需作如下精确化。

局部 ADE 形变由半通用形变拉回；在 Cartan/Weyl 覆盖后可作 simultaneous resolution。单个 \(A_1\) 的 Weyl 群为
\[
W(A_1)\cong\mathbb Z/2.
\]
对多个独立节点，完整多参数 Weyl 覆盖的群一般是
\[
(\mathbb Z/2)^r,
\]
而不是全局只有一个 \(\mathbb Z/2\)。不过对单参数解析圆盘，所有局部平滑函数
\[
f_i(t)=t^{m_i}u_i(t)
\]
中的单位 \(u_i\) 在缩小圆盘后都有解析平方根，因此归一化后共同采用 \(t=s^2\) 通常足以处理所有奇数阶分支；偶数阶无需基变。故在本单参数情形，“至多二重基变”是合理的，但应与多参数 \(2^r\) 覆盖区分。

全局 simultaneous resolution 可能自然存在于复解析范畴或代数空间范畴，而非射影 scheme；对拓扑结论只需获得 proper smooth 的解析族
\[
\widetilde{\mathcal Z}\to\Delta'.
\]
于是 Ehresmann 定理给出纤维间微分同胚。中央纤维是极小解消 \(S\)，一般纤维本来光滑，所以解消映射在一般纤维上为同构。因此
\[
S\cong_{\mathrm{diff}} Z_t.
\]

这一步本质上依赖 RDP/ADE。对 Wahl 或一般 \(T\)-singularity，Milnor fiber 与极小解消通常不是同一光滑拓扑类型，链条不能原样推广。

源笔记中“Milnor fiber 与 minimal resolution symplectomorphic”的附加说法既非必要，也需强烈限定：标准 Milnor-fiber symplectic form 是 exact，而标准 Kähler 解消形式在 exceptional sphere 上有正积分，两者不能按该标准结构直接 symplectomorphic。微分同胚应直接由 simultaneous resolution 获得。

---

## 6. Einstein 度量的转移

正确。若
\[
F:S\to Z_t
\]
为上述微分同胚，令 \(g_t\) 为 Aubin–Yau 度量，则
\[
h=F^*g_t
\]
满足
\[
\operatorname{Ric}_h
=F^*(\operatorname{Ric}_{g_t})
=-F^*g_t=-h.
\]
所以 \(S\) 的底层光滑四维流形承载 Einstein 度量。

此度量通常不必相对于 \(S\) 原来的复结构为 Kähler。事实上 \(S\) 上 exceptional \((-2)\)-曲线满足 \(K_S\cdot E=0\)，故原复结构下 \(K_S\) 不 ample；Einstein 度量来自微分同胚到平滑纤维后的新复结构。

---

## 最终判定

没有发现链条 3–6 的反例；补齐 proper flat QG family、光滑一般纤维和 simultaneous resolution 的解析适用条件后，它们构成严格证明。

需要修复或仍未证明之处是：

1. \(A_1\) 平滑参数应满足 \(t\propto(\zeta_2+i\zeta_3)^2\)，不是直接相等；
2. Ozuch/Biquard 首阶阻碍等式及 chirality 尚未在材料中实际推导；
3. 局部 kernel-directed ALE 参数不等于全局 integrable QG 光滑化；
4. log tangent 与 \(T_S\) 的 \(H^2\) 不应无条件直接等同；
5. \(K^2\ge6\) 只说明 vanishing criterion 失败，不说明不可光滑化；
6. \(K^2=2,4\) 的具体 cohomology vanishing 仍完全未算出。

因此当前可严格声称的是条件性定理，而不是具体 product-quotient resolution 的无条件 Einstein 存在定理。决定性未解对象是具体模型的局部到整体映射
\[
\operatorname{Ext}^1(\Omega_Z,\mathcal O_Z)
\longrightarrow
H^0(\mathcal T_Z^1)
\]
是否包含一个在每个 \(A_1\) 分量都非零且可积分的方向；\(H^2(T_S)=0\) 是保证该性质的充分办法，但不是唯一办法。
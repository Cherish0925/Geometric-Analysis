# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 17,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step17_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step17_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the three-bridge assessment for Yau Problem 26. The session claims: (1) Bridge 1 (general-to-invariant) is blocked because CZ spike prevents bounded sectional curvature from Ricci pinching, and CFG F-structure theory needs bounded sectional curvature. Is this assessment correct? Are there known results that give global structural decompositions under only Ricci bounds? Specifically check: Cheeger-Colding theory for Ricci limit spaces, Bamler's structure theory, Naber-Zhang accessible covers, and whether any of these can produce a global torus action or F-structure analog under Ricci alone. (2) Bridge 3 (finiteness-to-existence) claims that finite diffeomorphism type does not imply Einstein existence and that this is as hard as the general existence problem. Is this correct? Are there results showing that manifolds admitting Ric>0 (or near-Einstein) metrics must admit Einstein metrics? Check DeTurck's implicit function theorem approach, Besse's stability theory, and recent breakthroughs. (3) The T^k identity tr_h Ric^V = −Δ_B w/w is claimed for twist-free diagonal T^k metrics for all k and m. Verify the algebraic proof (product-rule identity for w=prod p_I). Also verify the Barta lower bound: does −Δw ≥ k(1−δ)w with w>0, w|_{∂Ω}=0 really imply λ₁≥k(1−δ)? Check whether the hypothesis of Barta's lemma requires w to be in the domain of the Dirichlet Laplacian or just a supersolution.

## Integrated Scientific Memo

# 三座桥与 \(T^k\) 谱恒等式核验结论

## 1. Bridge 1：仅由 Ricci 夹逼不能得到全局环面作用或 F-structure

这一评估基本正确，但应精确表述为：

> CZ spike 排除了“由 \(C^0\) Ricci 夹逼直接推出点态截面曲率界”，因而不能把原度量直接送入经典 Cheeger–Fukaya–Gromov（CFG）塌缩理论；现有 Ricci-only 结构定理也没有提供所需的全局 \(T^k\) 作用或兼容的全局 F-structure。

源材料中的反例机制确实实现了
\[
\|\Ric_{g_j}-g_j\|_{L^\infty,\mathrm{op}}\to0,
\qquad
\sup |\Rm_{g_j}|\to\infty,
\]
因为反向 warping 消掉了 Ricci 中的 trace-free Hessian，而该 Hessian 仍出现在 Weyl/完整曲率中。因此：

* 它不否定 CFG；
* 它只说明 CFG 不能直接用于原始 Ricci-pinched 度量；
* 若先通过 Ricci flow 等方法得到有界截面曲率，仍可能再用 CFG，但必须控制平滑后的几何及 Ricci 缺陷，这正是尚缺的一步。

### 各类 Ricci-only 理论的实际输出

- **Cheeger–Colding**：提供 Ricci 下界下极限空间的分裂、正则/奇异分解、切锥与度量测度结构。即使在塌缩情形，也不自动在预极限光滑流形上构造兼容的全局环面作用。
- **Bamler**：其 Ricci flow/奇异极限结构理论给出正则区域、奇异分层和曲率尺度信息，更适合平滑或流极限路线；它不是从静态双边 Ricci 界提取全局 nilpotent Killing structure 的替代品。
- **Naber–Zhang accessible covers**：最接近所需桥梁，但结论是选定尺度上的局部覆盖、局部基本群/幂零结构及在最大 fibered nilpotency rank 等附加条件下的 harmonic-radius 控制。最大秩不是单由 Ricci 界推出的，且局部秩可变化；这些局部覆盖数据没有已知的自动粘合过程可生成全局 \(T^k\) 作用、统一 toric orbit space 或 CFG 型全局 F-structure。
- **有界 Ricci 下的 harmonic-coordinate 正则性**：通常给 \(W^{2,p}\)、\(C^{1,\alpha}\) 或 BMO 型控制，而不是 \(W^{2,\infty}\) 或点态 \(|\Rm|\) 界，恰与 CZ spike 相容。

因此 Bridge 1 确实仍是实质性空缺。不能声称 Cheeger–Colding、Bamler 或 Naber–Zhang 已提供 general-to-invariant reduction。

---

## 2. Bridge 3：有限微分同胚型不能推出 Einstein 存在性

这一评估正确。有限性只把问题缩成有限个光滑流形上的非线性 PDE 存在性问题，并不解决任何一个流形上的
\[
\Ric_h=\lambda h.
\]

尤其不存在一般定理
\[
\Ric>0 \quad\Longrightarrow\quad \text{存在 Einstein 度量}.
\]
事实上，正 Ricci 条件远弱于 Einstein 存在性。一个清楚的拓扑反例模式是：正 Ricci connected-sum 构造可给某些
\(\#_k\CP^2\) 正 Ricci 度量，而
\[
\chi(\#_k\CP^2)=k+2,\qquad \tau(\#_k\CP^2)=k.
\]
若 \(k\ge5\)，则
\[
2\chi=2k+4<3k=3|\tau|,
\]
违反 Einstein 四流形必须满足的 Hitchin–Thorpe 不等式，故这些流形不能承载任何 Einstein 度量。因而“\(\Ric>0\) 蕴含 Einstein”本身就是假的，而不只是未证明。

### 局部扰动理论为何不够

- **DeTurck/隐函数定理方法**需要一个已有的 Einstein 背景以及 gauge-fixed 线性化算子的非退化性，并要求 \(C^{2,\alpha}\) 或相应强 Sobolev 范数中的接近。仅有
  \[
  \|\Ric_g-g\|_{C^0}\ll1
  \]
  不提供 Einstein 基点，也不提供 \(C^2\) 接近；CZ spike 正好显示 Ricci 缺陷很小而二阶曲率可很大。
- **Besse–Koiso 型稳定性和模空间理论**描述已有 Einstein 度量附近的刚性、无穷小变形及可积性，不会从拓扑有限性、正 Ricci 或弱 near-Einstein 条件中制造 Einstein 度量。
- **特殊存在性结果**——Kähler–Einstein/K-stability、特殊 orbifold desingularization、已知稳定 Einstein 度量附近的 Ricci flow 收敛等——都需要额外结构或已知模型，不能用于任意 Ricci-pinched 光滑流形。

还须区分两种“near-Einstein”：

1. 单个度量只有 \(C^0\) Ricci 缺陷小：现有 IFT 不适用；
2. 同一流形有一列 \(\|\Ric_{g_j}-g_j\|_{C^0}\to0\)：这比单纯 \(\Ric>0\) 强得多，但若无非塌缩、强拓扑收敛、Einstein 极限及非退化性，仍没有一般的存在性定理。

因此即使前两桥给出有限微分同胚型，Bridge 3 仍需要一个全新的闭性/紧致性加变形论定理；现有材料没有它。

---

## 3. \(T^k\) determinant identity：代数证明正确

对 twist-free diagonal 度量
\[
g=g_B+\sum_{I=1}^k p_I^2(d\phi^I)^2,\qquad
w=\prod_{I=1}^k p_I,
\]
在主轨道区域 \(p_I>0\) 上有
\[
\boxed{\ \tr_h\Ric^V=-\frac{\Delta_Bw}{w}\ }.
\]

竖直单位向量 \(E_I=p_I^{-1}\partial_{\phi^I}\) 的 multiply-warped Ricci 公式为
\[
\Ric(E_I,E_I)
=-\frac{\Delta_Bp_I}{p_I}
-\sum_{J\ne I}
\frac{\langle\nabla p_I,\nabla p_J\rangle}{p_Ip_J}.
\]
求和得到
\[
\tr_h\Ric^V
=-\sum_I\frac{\Delta_Bp_I}{p_I}
-\sum_{I\ne J}
\frac{\langle\nabla p_I,\nabla p_J\rangle}{p_Ip_J}.
\]

另一方面，
\[
\log w=\sum_I\log p_I,
\]
故
\[
\frac{\Delta_Bw}{w}
=\Delta_B\log w+|\nabla\log w|^2.
\]
展开后，\(|\nabla p_I|^2/p_I^2\) 项与双和中的 \(I=J\) 项相消，得到
\[
\frac{\Delta_Bw}{w}
=\sum_I\frac{\Delta_Bp_I}{p_I}
+\sum_{I\ne J}
\frac{\langle\nabla p_I,\nabla p_J\rangle}{p_Ip_J}.
\]
两式相合即得结论。该证明只使用 \(g_B\) 上的协变乘积法则，因此对任意 \(k,m\) 成立；文件中 \(k\le5,m=2\) 的符号计算只是有限维检查，不是一般性证明的必要依据。

此式不应未经重算推广到一般非对角 fiber matrix 或有 twist 的情形；那里会出现额外项。

---

## 4. Barta 下界正确，而且下界不要求 \(w\) 属于强 Dirichlet 算子定义域

令
\[
\alpha=k(1-\delta).
\]
由竖直方向的 Ricci 夹逼和恒等式，
\[
-\Delta_Bw\ge \alpha w,\qquad w>0\quad\text{于 }\Omega.
\]

对任意 \(\varphi\in C_c^\infty(\Omega)\)，写
\(\varphi=w\psi\)。积分分部给出 ground-state transform
\[
\int_\Omega |\nabla\varphi|^2
=
\int_\Omega\frac{-\Delta w}{w}\,\varphi^2
+\int_\Omega w^2|\nabla\psi|^2
\ge
\alpha\int_\Omega\varphi^2.
\]
因此
\[
\boxed{\lambda_1^D(\Omega,g_B)\ge k(1-\delta)}.
\]

这一论证只要求 \(w\) 是正的局部正则 supersolution；弱形式也足够。因为测试函数紧支于内部：

* 下界不需要 \(w\in H^2\cap H_0^1\)；
* 甚至不需要为此下界使用 \(w|_{\partial\Omega}=0\)。

但另一个方向
\[
\lambda_1^D\le k(1+\delta)
\]
若通过把 \(w\) 本身代入 Rayleigh quotient，则必须验证
\[
w\in H_0^1(\Omega).
\]
对光滑 torus degeneration，通常由 rod/bolt 附近 \(p_I\) 的线性消失推出，但应明确证明其零迹和有限能量，而不能只写 \(w=0\) 于边界。

---

## 5. 附带发现：材料中的二维 Faber–Krahn 面积结论未被证明

谱夹逼
\[
k(1-\delta)\le\lambda_1^D\le k(1+\delta)
\]
在上述函数空间条件下成立；但由此直接断言
\[
\Area(\Omega,g_B)\ge
\frac{\pi j_{0,1}^2}{k(1+\delta)}
\]
对任意二维 Riemannian orbit metric 并不成立。

常数 \(\pi j_{0,1}^2\) 是欧氏平面域的经典 Faber–Krahn 常数。一般曲面需要额外的等周不等式、曲率比较、平坦 Weyl 坐标与正确测度关系，或其他全局几何输入。总空间 Ricci 夹逼并未在材料中给出这种 base 几何控制。因此：

* \(T^k\) 恒等式和 Barta 下界可靠；
* 上界需补充 \(w\in H_0^1\)；
* 表中的 orbit-area 数值下界目前是条件性的，不能称为“无需 base Ricci/曲率控制”的结论。
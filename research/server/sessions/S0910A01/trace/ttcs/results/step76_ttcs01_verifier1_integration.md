# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 76,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step76_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step76_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the reduced obstruction-map formulation for Einstein desingularization of (S^2 x S^2)/Z_2. The note claims: (1) All first obstructions lambda_k^j vanish automatically when the EH direction zeta_j lies in the 2D kernel of R^{pm} = diag(Lambda, 0, 0). (2) The second obstruction mu_1^j vanishes because the 2x2 remaining block has determinant 0 (one eigenvalue is 0, the other is Lambda). (3) The leading surviving obstruction is the global system nu_l, which pairs H^4 (the r^{-4} EH correction) against V_{l,2} (quadratic jet of orbifold kernel modes) via an L^2 integral on S^3/Z_2. (4) H^4 restricted to S^3 lives in l=2 tensor harmonics (NOT constant) because theta_1^-(x) depends on x through the quaternionic conjugation formula theta_i^-(x) = sum_j (x^T(omega_i^+ circ omega_j^-) x/|x|^2) omega_j^-, making it quadratic in x. (5) V_{l,2} also lives in l=2 tensor harmonics, so the pairing is not automatically zero by representation theory. (6) The reduced system has 4 in-kernel angle unknowns and at most 4 global equations, giving a generically solvable dimension count. Check each claim against the Ozuch source, identify any errors in the curvature calculation (R^+ on S^2 x S^2), the angular structure of lambda_k near the kernel, and the harmonic-degree argument. Does the trigonometric form sum_j (A_l^j cos alpha_j + B_l^j sin alpha_j) = 0 correctly capture the alpha-dependence of nu_l?

## Integrated Scientific Memo

# 核验结论

该 reduced obstruction-map 方案的**局部曲率与前两级消失机制基本正确**，但其核心全局系统目前不能成立为所写形式：

1. \(S^2\times S^2\) 的曲率算子确为
   \[
   \mathbf R^\pm=\operatorname{diag}(\Lambda,0,0),
   \]
   但笔记中的 Weyl 特征值少了因子 \(2\)。

2. 对 \(v=0\) 且 EH 方向位于二维核时，所有 \(\lambda_k^j\) 消失，且 \(\mu_1^j=0\)。

3. Ozuch 的一般公式确实给出
   \[
   \nu_l=3\sum_j\int_{S^3/\mathbb Z_2}
   \langle H^4(\zeta_j^{\epsilon_j}),V_{l,2}^{(j)}\rangle\,dv,
   \]
   但只有在背景存在非零 \(\mathbf O(g_o)=\ker P_{g_o}\) 时才有这些方程。对等半径 \(S^2\times S^2\) 产品 orbifold，现有“\(d\le4\)”及 shape/isometry kernel 说明是错误的；实际的 Einstein deformation kernel 应为零，因此该 \(\nu_l\) 系统为空。

4. \(H^4|_{S^3}\) 确有非恒定的二次角向内容；但“每个 \(V_{l,2}\) 都在同一纯 \(\ell=2\) 不可约块”并未由 Ozuch 证明。

5. 即便假设存在非空 \(\nu\) 系统，其角度依赖一般也不是
   \[
   A\cos\alpha+B\sin\alpha,
   \]
   而是
   \[
   C+A\cos2\alpha+B\sin2\alpha,
   \]
   并带有各节点尺度平方权重。

6. “4 个角度、至多 4 个方程，所以一般可解”不是有效的存在性论证。

---

## 1. 产品曲率计算

取乘积正交标架，其中 \(e_1,e_2\) 切于第一个球面，\(e_3,e_4\) 切于第二个球面。两球面 Gauss 曲率均为 \(\Lambda\)，所以

\[
\mathcal R(e^{12})=\Lambda e^{12},\qquad
\mathcal R(e^{34})=\Lambda e^{34},
\]

所有混合二形式均被消去。于是，在标准自对偶/反自对偶基中，

\[
\boxed{\mathbf R^+=\mathbf R^-=\operatorname{diag}(\Lambda,0,0).}
\]

这确认了 rank \(1\) 与二维核。

由于 \(s=4\Lambda\) 且

\[
\mathbf R^\pm=W^\pm+\frac{s}{12}I,
\]

正确的 Weyl 特征值是

\[
\boxed{
W^\pm=\operatorname{diag}
\left(\frac{2\Lambda}{3},-\frac{\Lambda}{3},-\frac{\Lambda}{3}\right).
}
\]

笔记所写
\[
(\Lambda/3,-\Lambda/6,-\Lambda/6)
\]
少了因子 \(2\)，并与同处所写的
\(\mathbf R^\pm=\operatorname{diag}(\Lambda,0,0)\) 不相容。

---

## 2. 第一 obstruction \(\lambda_k^j\)

Ozuch 式 (24)/(28) 为

\[
\lambda_k^j(\phi_j,0)
=
c\langle \mathbf R^{\epsilon_j}\phi_j,
\phi_{j,(k)}\rangle .
\]

因此若

\[
\phi_j\in\ker\mathbf R^{\epsilon_j},
\]

则

\[
\boxed{\lambda_k^j(\phi_j,0)=0\quad(k=1,2,3).}
\]

所以陈述 (1) 成立，但必须保留限定 **\(v=0\)**。Ozuch 式 (40) 表明 \(v\neq0\) 会改变常数 jet、二次 jet 及相应曲率算子，故此时不再自动消失。

### 核平面附近的正确展开

令

\[
\phi(s,\alpha)
=
s e_1+\sqrt{1-s^2}
(\cos\alpha\,e_2+\sin\alpha\,e_3),
\]

并取适配正交基

\[
u_\alpha=-\sin\alpha\,e_2+\cos\alpha\,e_3,
\]
\[
w(s,\alpha)=\sqrt{1-s^2}e_1
-s(\cos\alpha e_2+\sin\alpha e_3).
\]

对 \(R=\operatorname{diag}(\Lambda,0,0)\)，

\[
R\phi=\Lambda s e_1,
\]

从而

\[
\langle R\phi,\phi\rangle=\Lambda s^2,
\]
\[
\langle R\phi,u_\alpha\rangle=0,
\]
\[
\langle R\phi,w\rangle
=\Lambda s\sqrt{1-s^2}
=\Lambda s+O(s^3).
\]

因此不变的局部结构是：

- 径向分量二阶；
- 一个横向分量一阶；
- 核平面切向分量恒为零。

笔记的
\(\lambda_2=O(\epsilon_3\epsilon_2)\)
不够准确：对这个固定 rank-one 算子及自然适配基，该分量严格为零。

另外，由

\[
t_j\lambda_3^j+t_j^2\mu_3^j=O(t_{\max}^{5/2})
\]

且尺度可比、\(\mu_3^j=O(1)\)，通常得到

\[
s_j=O(t_j)+O(t_j^{3/2}),
\]

而非笔记声称的 \(O(t_j^{1/2})\)。

---

## 3. 第二 obstruction \(\mu_1^j\)

当 \(\phi_j\) 位于二维核内时，可取基使

\[
\mathbf R^{\epsilon_j}
=
\begin{pmatrix}
0&0&0\\
0&0&0\\
0&0&\Lambda
\end{pmatrix}.
\]

Ozuch Lemma 2.14 在 \(\lambda_k^j=0\) 时给出

\[
\mu_1^j
=
C\det
\begin{pmatrix}
R_{22}^j&R_{23}^j\\
R_{32}^j&R_{33}^j
\end{pmatrix}.
\]

剩余块为 \(\operatorname{diag}(0,\Lambda)\)，故

\[
\boxed{\mu_1^j(\phi_j,0)=0.}
\]

陈述 (2) 正确。但该公式只验证 \(\mu_1^j\)，不能据此宣称全部 \(\mu_k^j\) 消失。

---

## 4. Ozuch 的全局 obstruction 及尺度

Proposition 2.10 确实给出：当所有 \(\lambda_k^j=0\) 时，Lemma 2.3 蕴含 \(H_2^4=0\)，因而

\[
\boxed{
\nu_l
=
3\sum_j\int_{S^3/\mathbb Z_2}
\langle H^4(\zeta_j^{\epsilon_j}),V_{l,2}^{(j)}\rangle\,dv.
}
\]

所以陈述 (3) 是正确的**一般公式**。

但是

\[
H^4(\zeta^+)
=
-\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4},
\]

而 \(\rho(\zeta)\) 对 \(\zeta\) 线性，故

\[
H^4(t\phi)=t^2H^4(\phi).
\]

因此正确的归一化形式是

\[
\frac{\nu_l}{t_{\max}^2}
=
3\sum_j\tau_j^2 I_l^j(\phi_j),
\qquad
\tau_j=\frac{t_j}{t_{\max}}.
\]

不能简单说“尺度整体因子消去”，除非：

- 所有尺度相同；或
- 尺度比 \(\tau_j\) 已固定，并明确吸收到系数中。

此外，领先公式中的 \(V_{l,2}^{(j)}\) 是固定 kernel basis 元素 \(\mathbf v_l\) 的 jet；它不是随背景参数 \(v\) 自由变化的未知量。笔记把 \(V_{l,2}^{(j)}(v)\) 和背景 deformation \(v\) 混在了一起。

---

## 5. 对产品 orbifold，\(\nu_l\) 系统实际上为空

Ozuch 的 \(\nu_l\) 由

\[
\mathbf v_l\in\mathbf O(g_o)=\ker P_{g_o},
\qquad
P_g=\frac12\nabla^*\nabla-\mathring R,
\]

产生。笔记声称：

- TT kernel 为零；
- 但 full gauged kernel 为四维；
- 其中有 shape deformation 和 isometry-moduli；
- Bianchi slicing 后成为 genuine integrable Einstein deformations。

这一组说法互相不相容，也不符合 Einstein deformation 方程。

所谓 shape 模式

\[
h_0=g_1-g_2
\]

是平行且 TT，但

\[
\nabla^*\nabla h_0=0,\qquad
\mathring R(h_0)=\Lambda h_0,
\]

所以

\[
P_g h_0=-\Lambda h_0\ne0.
\]

它是不稳定方向，而不是零模。等价地，对

\[
g=a\,g_{S^2}+b\,g_{S^2},
\]

Einstein 条件要求同一个 \(\lambda\) 满足

\[
1=\lambda a,\qquad 1=\lambda b,
\]

故 \(a=b\)；相对尺度变化不切于 Einstein family。

同样：

- Killing 场满足 \(\mathcal L_Xg=0\)，不产生 metric moduli；
- 一般纯 gauge/conformal 方向不属于 Ozuch 的 genuine \(L^2\) Einstein deformation 空间。

因此现有证据支持

\[
\boxed{\mathbf O(g_o)=0}
\]

对 \(S^2\times S^2\) 及其 \(\mathbb Z_2\)-不变子空间均成立。于是

\[
d=0,\qquad
\mathcal F:(S^1)^4\longrightarrow\mathbb R^0,
\]

不存在任何 \(\nu_l\) 方程。

因此，“\(\nu_l\) 是 leading surviving obstruction”对这个背景是错误的。Ozuch 已显式计算的 \(\lambda,\mu,\nu\) 在此处分别自动消失、自动消失、空缺；真正下一项是该来源未显式算出的更高阶 obstruction。

若实际意图是先部分解消，再以所得 orbifold 为新背景，则 \(\mathbf v_l\) 应来自该**部分解消背景**的 moduli，而不是产品 orbifold；整个 kernel 与 jet 计算需据此重写。

---

## 6. \(H^4\) 的角向谐波结构

Ozuch 给出

\[
\theta_i^-(x)
=
\sum_m
\frac{x^T(\omega_i^+\circ\omega_m^-)x}{|x|^2}\omega_m^-.
\]

因为 \(\omega_i^+\circ\omega_m^-\) 是对称无迹矩阵，在 \(S^3\) 上

\[
x^T(\omega_i^+\circ\omega_m^-)x
\]

是 degree-two 标量球谐，而非常数。因此

\[
\boxed{H^4|_{S^3}\text{ 有非平凡二次角向内容，不是常量模式。}}
\]

陈述 (4) 的核心正确。

但“\(H^4\) 属于 \(\ell=2\) tensor harmonics”需要说明张量 Laplacian 和表示标签。最安全的严格表述是：在固定平行张量基展开后，\(H^4|_{S^3}\) 的系数属于 degree-two 标量谐波；其角向表示位于 \(\Omega^+\otimes\Omega^-\) 的相应非恒定分量。

---

## 7. \(V_{l,2}\) 的 harmonic-degree 主张

\(V_{l,2}\) 是二次齐次张量，但一般二次齐次张量在球面上的分解可含：

- 无迹 degree-two 部分；
- \(r^2\) 乘常数张量产生的 degree-zero 部分；
- 不同张量不可约表示和 gauge 分量。

Ozuch Proposition 2.10 只证明积分中 \(V_{l,0}\) 因 harmonic mismatch 不贡献，并留下

\[
\int\langle H^4,V_{l,2}\rangle.
\]

它没有证明任意 \(V_{l,2}\) 都纯属与 \(H^4\) 相同的不可约表示，也没有证明积分非零。准确结论为：

\[
\boxed{
\nu_l\text{ 只看见 }V_{l,2}
\text{ 在 }H^4\text{ 所在表示分量上的投影。}
}
\]

所以陈述 (5) 应改为：

- “该 pairing 不会仅因齐次次数而自动为零”是合理的；
- “两者必在同一纯 \(\ell=2\) block，故一般非零”未获证明；
- 对当前产品背景，由于 \(\mathbf O(g_o)=0\)，根本没有这些 \(V_{l,2}\)。

---

## 8. 正确的 \(\alpha\)-依赖

原笔记把

\[
H^4\sim
(\cos\alpha\,\omega_2+\sin\alpha\,\omega_3)
\circ\theta_1^-
\]

视为对方向线性，但这错误地固定了 \(\theta_1^-\)。Ozuch 的准确公式是

\[
H^4(\phi)
=
-\frac{\rho(\phi)^-\circ\phi^+}{2r^4},
\]

两个因子均对 \(\phi\) 线性，所以 \(H^4\) 对 \(\phi\) 二次。

令

\[
\phi(\alpha)=\cos\alpha\,e_2+\sin\alpha\,e_3.
\]

展开后出现

\[
\cos^2\alpha,\quad
\sin^2\alpha,\quad
\sin\alpha\cos\alpha,
\]

即

\[
1,\quad\cos2\alpha,\quad\sin2\alpha.
\]

故一般形式是

\[
\boxed{
I_l^j(\alpha_j)
=
C_l^j+A_l^j\cos2\alpha_j+B_l^j\sin2\alpha_j.
}
\]

保留尺度比后，全局方程应为

\[
\boxed{
\sum_j\tau_j^2
\left(
C_l^j+A_l^j\cos2\alpha_j+B_l^j\sin2\alpha_j
\right)=0.
}
\]

某些特殊表示投影可能令 \(C_l^j=0\)，但这需要实际计算，不能预设。因此所问的

\[
\sum_j(A_l^j\cos\alpha_j+B_l^j\sin\alpha_j)=0
\]

**一般不正确**。

---

## 9. 维数计数

即使暂时假设 \(1\le d\le4\)，从

\[
(S^1)^4\to\mathbb R^d
\]

也不能因“变量数不少于方程数”推出零点存在。连续映射可以完全避开原点，修正后的常数偏置 \(C_l^j\) 更使这一点明显。

即使找到零点，构造性横截条件还要求 Jacobian 满秩。对修正后的系统，

\[
\frac{\partial\mathcal F_l}{\partial\alpha_j}
=
2\tau_j^2
\left(
-A_l^j\sin2\alpha_j+B_l^j\cos2\alpha_j
\right),
\]

必须在零点处验证其秩为 \(d\)。故陈述 (6) 的“generically solvable dimension count”不成立。

---

## 最终核验表

| 主张 | 判定 |
|---|---|
| (1) 核方向使全部 \(\lambda_k^j\) 消失 | 正确，但限于背景 \(v=0\) |
| (2) rank-one 使 \(\mu_1^j=0\) | 正确；不推出其他 \(\mu_k^j\) |
| (3) \(\nu_l\) 为 \(H^4\)-\(V_{l,2}\) 球面积分 | Ozuch 的一般公式正确；但产品背景 kernel 为零，故系统为空，并须保留 \(t_j^2\) |
| (4) \(H^4\) 非常数、有二次角向内容 | 正确 |
| (5) pairing 不因次数不同自动为零 | 弱形式正确；“同一纯表示且一般非零”未证明 |
| (6) 4 变量、至多 4 方程故一般可解 | 错误 |
| 单角 \(\cos\alpha,\sin\alpha\) 形式 | 错误；一般为 \(C+A\cos2\alpha+B\sin2\alpha\) |
| Weyl 特征值 | 应改为 \((2\Lambda/3,-\Lambda/3,-\Lambda/3)\) |
| 核附近 \(\lambda\) | 自然基中为 quadratic / zero / linear |
| 当前真正未决项 | \(\lambda,\mu\) 之后的更高阶局部/全局 obstruction，而非所写四方程 \(\nu\) 系统 |

最重要的修正是：先独立谱算并固定 \(\mathbf O(g_o)\)。对产品 orbifold，它应为零；因此目前没有 \(A_l^j,B_l^j\) 可计算，所提 reduced global map 并不是该解奇异化问题的下一有效对象。
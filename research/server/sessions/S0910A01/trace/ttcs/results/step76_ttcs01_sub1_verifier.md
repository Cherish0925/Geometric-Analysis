# TTCS Independent Branch Record

```json
{
  "step_id": 76,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step76_mixed_row_reduced_obstruction_map.md",
    "Sessions/S0910A01/workspace/data/step76_harmonic_pairing_analysis.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the reduced obstruction-map formulation for Einstein desingularization of (S^2 x S^2)/Z_2. The note claims: (1) All first obstructions lambda_k^j vanish automatically when the EH direction zeta_j lies in the 2D kernel of R^{pm} = diag(Lambda, 0, 0). (2) The second obstruction mu_1^j vanishes because the 2x2 remaining block has determinant 0 (one eigenvalue is 0, the other is Lambda). (3) The leading surviving obstruction is the global system nu_l, which pairs H^4 (the r^{-4} EH correction) against V_{l,2} (quadratic jet of orbifold kernel modes) via an L^2 integral on S^3/Z_2. (4) H^4 restricted to S^3 lives in l=2 tensor harmonics (NOT constant) because theta_1^-(x) depends on x through the quaternionic conjugation formula theta_i^-(x) = sum_j (x^T(omega_i^+ circ omega_j^-) x/|x|^2) omega_j^-, making it quadratic in x. (5) V_{l,2} also lives in l=2 tensor harmonics, so the pairing is not automatically zero by representation theory. (6) The reduced system has 4 in-kernel angle unknowns and at most 4 global equations, giving a generically solvable dimension count. Check each claim against the Ozuch source, identify any errors in the curvature calculation (R^+ on S^2 x S^2), the angular structure of lambda_k near the kernel, and the harmonic-degree argument. Does the trigonometric form sum_j (A_l^j cos alpha_j + B_l^j sin alpha_j) = 0 correctly capture the alpha-dependence of nu_l?

## Output

## 科学核验备忘录

### 总结

六项陈述中：

- **(1)、(2)、(3)** 在固定背景 \(v=0\)、并采用 Ozuch 的方向/尺度分解后基本成立。
- **(4)** “\(H^4\) 非常数、具有二次角向依赖”成立；但将它简单称作普通标量意义的“\(\ell=2\) tensor harmonic”需要先固定张量球谐的定义及其 \(\mathrm{SO}(4)\)-表示标签。
- **(5)** 尚未由给出的材料证明。\(V_{l,2}\) 是二次齐次张量，但这本身不保证它的限制只属于与 \(H^4\) 相同的不可约分量；实际配对可能因具体模态、规范或对称性为零。
- **(6)** “四个变量、至多四个方程”只是形式计数，不能推出零点存在，更不能推出满射性。这里还有更强的几何问题：所述 orbifold kernel 维数与“shape deformation/isometry-moduli”的解释不可信。

此外，当前 reduced map 漏掉了各泡尺度的二次权重；正确的领先系统通常依赖尺度比。

---

## 1. \(S^2\times S^2\) 的曲率算子

取乘积正交标架 \(e_1,e_2\) 属于第一球面，\(e_3,e_4\) 属于第二球面，并取

\[
\omega_1^\pm=\frac{e^{12}\pm e^{34}}{\sqrt2},\quad
\omega_2^\pm=\frac{e^{13}\mp e^{24}}{\sqrt2},\quad
\omega_3^\pm=\frac{e^{14}\pm e^{23}}{\sqrt2}.
\]

若两个球面的截面曲率都为 \(\Lambda\)，则

\[
\mathcal R(e^{12})=\Lambda e^{12},\qquad
\mathcal R(e^{34})=\Lambda e^{34},
\]

而混合二形式 \(e^{13},e^{14},e^{23},e^{24}\) 均被 \(\mathcal R\) 消去。因此

\[
\mathcal R|_{\Lambda^\pm}
=
\operatorname{diag}(\Lambda,0,0).
\]

这也与四维 Einstein 分解一致：

\[
\mathcal R|_{\Lambda^\pm}=W^\pm+\frac{s}{12}I,
\qquad s=4\Lambda,
\]

故

\[
W^\pm=\operatorname{diag}\!\left(\frac{2\Lambda}{3},
-\frac{\Lambda}{3},-\frac{\Lambda}{3}\right).
\]

笔记中的

\[
W^\pm=\operatorname{diag}\!\left(\frac{\Lambda}{3},
-\frac{\Lambda}{6},-\frac{\Lambda}{6}\right)
\]

少了因子 \(2\)，且与其同时写出的
\(\mathcal R^\pm=\operatorname{diag}(\Lambda,0,0)\) 不相容。除非另有未说明的曲率归一化，否则该 Weyl 数值应改正。

---

## 2. 第一局部 obstruction

Ozuch 式 (24) 给出

\[
\lambda_k(\zeta^\pm)
=
c\left\langle
\mathbf R^\pm(H_2)\zeta^\pm,\zeta_{(k)}^\pm
\right\rangle .
\]

方向归一化后，令单位向量 \(\phi\in S^2\)。若

\[
R=\operatorname{diag}(\Lambda,0,0),
\qquad
\phi\in\ker R=\operatorname{span}(e_2,e_3),
\]

则 \(R\phi=0\)，所以三个 \(\lambda_k\) 全为零。故陈述 (1) 对 \(v=0\) 成立。

这里需区分：

\[
\lambda_k(\phi,0)=0
\]

与

\[
\lambda_k(\phi,v)=0.
\]

Ozuch 式 (40) 表明 orbifold deformation \(v\) 会改变常数项、二次 jet 和曲率算子，因此在 \(v\neq0\) 时并非自动消失。

### 核平面附近的角向展开

令

\[
\phi(s,\alpha)
=
s e_1+\sqrt{1-s^2}
(\cos\alpha\,e_2+\sin\alpha\,e_3).
\]

取

\[
u_\alpha=-\sin\alpha\,e_2+\cos\alpha\,e_3,
\qquad
w(s,\alpha)=\sqrt{1-s^2}e_1-s(\cos\alpha e_2+\sin\alpha e_3).
\]

则 \((\phi,u_\alpha,w)\) 是一组适配正交基，且

\[
R\phi=\Lambda s e_1.
\]

所以

\[
\langle R\phi,\phi\rangle=\Lambda s^2,
\]

\[
\langle R\phi,u_\alpha\rangle=0,
\]

\[
\langle R\phi,w\rangle
=
\Lambda s\sqrt{1-s^2}
=
\Lambda s+O(s^3).
\]

因此，按该自然基编号，

\[
\lambda_1=c\Lambda s^2,\qquad
\lambda_2=0,\qquad
\lambda_3=c\Lambda s+O(s^3).
\]

笔记中的“\(\lambda_2=O(\epsilon_3\epsilon_2)\)”不精确：对固定的 rank-one 对角算子和自然旋转基，它实际上恒等于零。若基随扰动以其他方式选取，相关分量标签会变化；不变的内容是：

- radial 分量为二阶；
- 一个 transverse 分量为一阶；
- 核平面切向分量为零。

另外，由

\[
t_j\lambda_3^j+t_j^2\mu_3^j=O(t_{\max}^{5/2})
\]

且尺度可比，可得通常

\[
s_j=O(t_j)+O(t_j^{3/2}),
\]

而不是笔记中的 \(O(t_j^{1/2})\)，前提是 \(\mu_3^j=O(1)\)。若只从较粗信息推导，必须明确为何忽略 \(t_j^2\mu_3^j\)。

---

## 3. 第二局部 obstruction

Ozuch Lemma 2.14 在第一组 obstruction 消失时给出

\[
\mu_1
=
C\det
\begin{pmatrix}
R_{22}&R_{23}\\
R_{32}&R_{33}
\end{pmatrix}.
\]

若第一基向量 \(\phi\) 位于二维核中，则可取第二基向量为核平面内与 \(\phi\) 正交的向量，第三基向量为 \(e_1\)。此时

\[
R=
\begin{pmatrix}
0&0&0\\
0&0&0\\
0&0&\Lambda
\end{pmatrix},
\]

故剩余块行列式为零，因而

\[
\mu_1(\phi,0)=0.
\]

所以陈述 (2) 成立。

但 Ozuch 在此公式中只明确计算了 \(\mu_1\)。这不能自动推出所有 \(\mu_k\) 均消失；笔记后文若把整个二阶局部系统都移除，需要额外公式或对称性论证。

---

## 4. 全局 obstruction \(\nu_l\)

Ozuch Proposition 2.10 明确给出，在所有 \(\lambda_k^j=0\) 时，

\[
\nu_l
=
3\sum_j
\int_{S^3/\mathbb Z_2}
\left\langle
H^4(\zeta_j^{\epsilon_j}),V_{l,2}^{(j)}
\right\rangle\,dv.
\]

同时 Lemma 2.3 给出 \(H_2^4=0\)，因此陈述 (3) 与源文一致。

然而尺度依赖不能删掉。源文 Proposition 1.16 的准确公式是

\[
H^4(\zeta^+)
=
-\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4},
\]

其中 \(\rho(\zeta)\) 对 \(\zeta\) 线性。因此

\[
H^4(t\phi)=t^2H^4(\phi),
\qquad
\nu_l(t\cdot\phi,0)
=
3\sum_j t_j^2 I_l^j(\phi_j).
\]

所以尺度可比时应写成

\[
\frac{\nu_l}{t_{\max}^2}
=
3\sum_j \tau_j^2 I_l^j(\phi_j),
\qquad
\tau_j=\frac{t_j}{t_{\max}}.
\]

笔记中“scales factor out”只有在所有 \(t_j\) 相等，或固定了尺度比并把 \(\tau_j^2\) 吸收到系数中时才成立。不同节点的尺度不能统一消去。

此外，笔记的 reduced map 将 \(v\) 同时作为自变量，又写入 \(V_{l,2}^{(j)}(v)\)，这混合了两个不同对象：

1. \(V_{l,2}^{(j)}\) 是固定 kernel basis element \(\mathbf v_l\) 的二次 jet；
2. \(v=\sum_l v_l\mathbf v_l\) 是背景 Einstein deformation 参数。

在 Ozuch 的领先公式 \(\nu_l(\zeta,0)\) 中，\(V_{l,2}^{(j)}\) 固定，不是随 \(v\) 变化的未知量。\(v\)-依赖属于更高阶展开。

---

## 5. \(H^4\) 的角向结构与球谐次数

源文公式为

\[
\theta_i^-(x)
=
\sum_{m=1}^3
\frac{x^T(\omega_i^+\circ\omega_m^-)x}{|x|^2}
\,\omega_m^-.
\]

在单位球面上，系数

\[
x^T(\omega_i^+\circ\omega_m^-)x
\]

是 trace-free quadratic polynomial，因为
\(\omega_i^+\circ\omega_m^-\) 是 trace-free symmetric matrix。因此这些系数是标量 degree-two spherical harmonics，而不是常数。由此

\[
H^4
=
-\frac{1}{2r^4}\,\zeta_{(1)}^\pm\circ\theta_1^\mp
\]

具有非平凡的二次角向依赖。陈述 (4) 的核心内容成立。

更精确地说，\(H^4|_{S^3}\) 是一个张量值函数，其坐标系数属于 degree-two 标量谐波。是否把整个对象标记为“\(\ell=2\) tensor harmonic”取决于所采用的张量 Laplacian 和 \(\mathrm{SO}(4)\) 表示记号。材料中的

\[
H^4\text{ representation}=V_1\times V_1
\]

并未由所引 Ozuch 段落建立，且“\(V_1\times V_1\)”与“\(\ell=2\)”的标签关系需另行定义。

---

## 6. \(V_{l,2}\) 与表示配对

\(V_{l,2}\) 是二次齐次 symmetric 2-tensor。其限制到 \(S^3\) 的坐标系数是二次多项式，但一般二次多项式分解为：

- trace-free degree-two 部分；
- \(r^2\) 乘常数张量的 degree-zero 部分；
- 再按张量表示和规范条件进一步分解。

Ozuch Proposition 2.10 只证明

\[
\nu_l
=
3\int\langle H^4,V_{l,2}\rangle,
\]

并没有证明每个 \(V_{l,2}\) 都纯属与 \(H^4\) 相同的不可约分量，也没有证明积分非零。能得到的准确结论是：

\[
\nu_l
\quad\text{只看见 }V_{l,2}\text{ 在 }H^4\text{ 所在表示分量上的投影}.
\]

因此陈述 (5) 中“不会仅因 harmonic degree 自动为零”是合理的；但“\(V_{l,2}\) 也 lives in 同一个 \(\ell=2\) block，故 generically nonzero”尚缺少具体 kernel jet 的分解。

这里还有一个更根本的问题：笔记所述 orbifold kernel 数据很可能不正确。对于等半径乘积 Einstein metric：

- 改变两因子的相对尺度通常不是 Einstein infinitesimal deformation；
- 等尺度整体缩放对应改变 Einstein 常数或体积归一化，而非固定 \(\Lambda\) 的 \(P_g\)-kernel；
- isometry-generated metric variations 为 \(\mathcal L_Xg=0\)，不会产生 metric moduli。

笔记中的
“shape deformation \(\delta\rho_1=-\delta\rho_2\) 满足 Einstein constraint”
可直接由乘积 Ricci 方程否定。若 \(g=a\,g_{S^2}+b\,g_{S^2}\)，则作为 \((0,2)\)-张量，各因子的 Ricci 对常数缩放不变；要求

\[
\operatorname{Ric}(g)=\lambda g
\]

给出 \(1=\lambda a\) 与 \(1=\lambda b\)，故 \(a=b\)。相反方向的变分不切于 Einstein family。

所以 \(d\le4\) 及相应 \(V_{l,2}\) 必须从采用的 \(P_g\) 约定、\(\Lambda\) 是否固定、体积是否固定、Bianchi slicing 和 orbifold parity 重新导出。若真正的 \(\mathbf O(g_o)\) 为零，则根本不存在 \(\nu_l\) 方程。

---

## 7. \(\alpha_j\)-依赖是否为正弦余弦线性形式

这取决于如何参数化 EH 数据。

对 \(\zeta=t\phi\)，Ozuch 的准确远场项为

\[
H^4(\zeta^+)
=
-\frac{t^2}{2r^4}
\bigl(\rho(\phi)^-\circ\phi^+\bigr).
\]

因此 \(H^4\) 对单位方向 \(\phi\) 一般是**二次**的，而不是线性的。若

\[
\phi(\alpha)=\cos\alpha\,e_2+\sin\alpha\,e_3,
\]

则二次依赖产生

\[
1,\quad \cos 2\alpha,\quad \sin 2\alpha
\]

型 Fourier 模式。于是一般应写

\[
I_l^j(\alpha)
=
C_l^j+A_l^j\cos 2\alpha+B_l^j\sin 2\alpha,
\]

或在某些 trace-free 配对消掉常数项后写成

\[
I_l^j(\alpha)
=
A_l^j\cos 2\alpha+B_l^j\sin 2\alpha.
\]

笔记使用

\[
H^4=-\frac{|\zeta|}{2r^4}\,
\zeta_{(1)}^\pm\circ\theta_1^-
\]

并据此推出对 \(\phi\) 的线性依赖，遗漏了 \(\theta_1^-\) 也随 EH 旋转参数变化这一点；固定 \(\theta_1^-\) 同时旋转 \(\zeta_{(1)}^\pm\) 并不是 Proposition 1.16 的一般旋转公式。

另一个直观佐证是 EH 参数通常满足 \(\zeta\sim-\zeta\) 的同一轴向数据，因此 reduced integrand 应具有 \(\alpha\mapsto\alpha+\pi\) 的偶性；单独的 \(\cos\alpha,\sin\alpha\) 不具此性质，而 \(\cos2\alpha,\sin2\alpha\) 具备。

所以所问的三角形式

\[
\sum_j(A_l^j\cos\alpha_j+B_l^j\sin\alpha_j)=0
\]

一般不正确。更接近源公式的是

\[
\sum_j \tau_j^2
\left(
C_l^j+A_l^j\cos2\alpha_j+B_l^j\sin2\alpha_j
\right)=0.
\]

具体是否 \(C_l^j=0\)，需计算 \(V_{l,2}^{(j)}\) 的相应表示投影。

---

## 8. 四变量与至多四方程

即使接受 \(d\le4\)，形式计数也不能推出零点存在。一个从紧致空间 \((S^1)^4\) 到 \(\mathbb R^d\) 的连续映射完全可以避开原点，例如常值非零映射。即使每一项没有常数 Fourier 模式，多向量椭圆和

\[
\sum_j \tau_j^2 q_j(\alpha_j)
\]

也未必包含原点。

此外，满射性需要在零点验证 Jacobian：

\[
\frac{\partial\mathcal F_l}{\partial\alpha_j}
=
2\tau_j^2
\left(
-A_l^j\sin2\alpha_j+B_l^j\cos2\alpha_j
\right),
\]

其秩必须为 \(d\)。变量数不少于方程数不保证该秩条件。

---

## 结论表

| 陈述 | 核验结果 |
|---|---|
| (1) 核方向使全部 \(\lambda_k^j\) 消失 | 成立，但限于 \(v=0\) 的背景曲率 |
| (2) rank-one 曲率使 \(\mu_1^j=0\) | 成立；不等于全部 \(\mu_k^j=0\) |
| (3) 下一项是 \(\nu_l\) 的球面积分 | 源文支持；应保留 \(t_j^2\) 权重，并先确认 orbifold kernel 非零 |
| (4) \(H^4\) 非常数且有二次角向内容 | 成立；表示标签需精确定义 |
| (5) pairing 不因次数不同而自动消失 | 可以这样表述；“同一不可约分量、通常非零”尚未证明 |
| (6) 四角度、至多四方程意味着通常可解 | 不成立；形式计数不能推出零点或满射性 |
| 线性 \(\cos\alpha,\sin\alpha\) 形式 | 一般不成立；源公式给出二次方向依赖，通常是 \(1,\cos2\alpha,\sin2\alpha\) |
| Weyl 特征值 | 笔记少因子 \(2\)：应为 \((2\Lambda/3,-\Lambda/3,-\Lambda/3)\) |
| 核平面附近的 \(\lambda\) | 自然基中为 quadratic / zero / linear；笔记的 \(O(\epsilon_3\epsilon_2)\) 与 \(O(t^{1/2})\) 需改写 |

最关键的数学对象是固定 kernel mode 的二次 jet \(V_{l,2}^{(j)}\) 及其在 \(H^4\) 对应表示分量上的投影。没有这些 jet 的实际计算，以及 orbifold kernel 维数的重新谱算，当前 reduced system 的维数、系数和零集都还不能确定。
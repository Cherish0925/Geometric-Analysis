# TTCS Independent Branch Record

```json
{
  "step_id": 76,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step76_preceptor_audit_mixed_green_factorization.md",
    "Sessions/S0910A02/workspace/data/step76_product_green_factorization_audit.json",
    "Sessions/S0910A02/workspace/data/step75_symmetry_selection_collapse.json",
    "Sessions/S0910A02/workspace/notes/step68_spectral_symmetry_and_multipole_gate.md",
    "Sessions/S0910A02/workspace/notes/step64_positive_mirror_homeomorphism_and_allocation.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/On-infinitesimal-Einstein-deformations--3392b31fc0b0--66ff3e854e20/object.md"
  ]
}
```

## Task

Verify the Step-76 Preceptor audit before the next mixed-row Green computation is built. Focus on the scientific correctness of four gates: (1) Ozuch's \bar h^4 singular asymptotic is a source/self-node issue and inter-node expansions at other A1 points are regular second-jet extractions; (2) on a product background the P-Green/resolvent separates with additive spectral denominators (or heat-kernel integral) and is not a literal product of two static S^2 Green functions, so adjacent coincident-in-one-factor pairs must be treated in the full product resolvent or a justified massive one-factor reduction; (3) the T^2 pole selection rule restricts characters but does not truncate spherical degree l; (4) the D8 reduction, working diagonal=spin identification caveat, scalar full-gauged kernel slice requirement, and Yau-26 scope statements are faithful. Identify any overclaims, missing tensor/operator convention issues, or a better completion criterion for the next diagonal r=2 calibration computation.

## Output

# 科学核验备忘录

## 总体判断

四个核心数学方向基本正确：

1. \(\bar h_i^4\) 的奇异渐近属于源点 \(p_i\)；在另一节点 \(p_j\ne p_i\) 的提升是光滑偶函数，因此读取常数项与二阶项是正确对象。
2. \(S^2\times S^2\) 上的 \(P\)-算子按张量块分离，但逆算子的谱分母是加法型；两个静态 \(S^2\) Green 核的乘积一般不是四维逆核。
3. \(T^2\) 对称性只筛选等变字符，并不使球谐次数 \(l\) 成为有限集合。
4. 四节点子集的 \(D_8\) 轨道分类正确；对角型与 spin 行的联系目前仍依赖局部 spin-lift 和 seam 约定；完整 \(P\)-kernel 必须显式处理；这些计算不直接解决 Yau 第26题。

但有三处会实质改变下一次计算的数学含义：

- 文中的无修正热核积分不适用于当前含零模与小于零特征值的 \(P\)。
- inter-node 二阶 jet 通常不是 Ozuch 方程中的局部 \(\mu\)；在等尺度展开中它首先产生 \(t_jt_i^2\) 阶相互作用。
- 仅令解与四个 full-\(P\) 零模正交，并不会自动令对应投影系数 \(\nu_l\) 消失。

---

## 1. 源点奇异性与其他节点的正则 jet

Ozuch Proposition 2.10 给出的对象是：对指定节点 \(p_i\) 和指定 \(H^4(\zeta_i)\)，求解
\[
P_o\bar h_i^4
 =\sum_l\nu_l v_l+\sum_k\lambda_k\bar o_{i,k}^4,
\qquad
\bar h_i^4=H^4(\zeta_i)+H_{i,2}^4+O(r_i^{-\varepsilon})
\]
并规定 \(\bar h_i^4\perp\mathbf O(g_o)\)。所以 \(r^{-4}\) 项确实固定在源点 \(p_i\)。

在 \(p_j\ne p_i\) 附近，方程的右端和算子系数在局部统一化覆盖上都是光滑的。椭圆正则性给出光滑提升；局部 \(A_1\) 作用为 \(x\mapsto-x\)，故奇次 Taylor 项消失：
\[
\bar h_i^4
 =H_{ji,0}+H_{ji,2}+O(r_j^4).
\]
Ozuch 在 torus 模型中写出的
\[
\sum_{i'\ne i}\bar h_{i'}^4
 =H_0(i)+H_2(i)+O(d(i,\cdot)^4)
\]
正是这一一般局部事实的显式实例。因此，对有序节点对 \(i\to j\)：

- \(p_i\) 处需要固定奇异渐近及其通量归一化；
- \(p_j\ne p_i\) 处不需要减去任何 \(r^{-4}\) 项；
- 同时处理全部节点时，节点 \(p_j\) 仍含自己的 self-source 项，正则展开只适用于总和中 \(i\ne j\) 的部分。

常数项 \(H_{ji,0}\) 不能简单删除。Ozuch 的公式使用满足
\[
\psi^*e=e+H_{ji,0}
\]
的线性映射，并在新标架中读取 \(\psi_*H_2\)。由于基准乘积曲率不为零，\(H_{ji,0}\) 对 \(\Lambda^\pm\) 标架和基准二阶 jet 的作用与 \(H_{ji,2}\) 同阶。相关曲率数据应写成
\[
\delta\mathcal R_j^\pm
=
\left.
D\mathcal R^\pm
\bigl(
\psi(H_{ji,0})_*
(H^{\rm base}_{j,2}+H_{ji,2})
\bigr)
\right|_{\text{对源数据的一次项}},
\]
而不是只对 \(H_{ji,2}\) 取普通坐标二阶导数。

---

## 2. 产品 \(P\)-算子、加法型分母与热核修正

取
\[
P=\frac12\nabla^*\nabla-\mathring R,
\qquad
\Delta_E=2P.
\]
在
\[
S^2_1\times S^2_2
\]
上，对沿第一因子的二阶张量 \(h_1\) 和第二因子的函数 \(f_2\)，有
\[
P(h_1f_2)
=(P_1h_1)f_2+\frac12h_1\Delta^{(2)}_0f_2.
\]
交换两因子得到另一张量块；混合块 \(\alpha_1\odot\beta_2\) 则由两个 connection Laplacian 的和给出。因而在分离变量后，特征值必为
\[
p_{a,l_1}+\frac12\lambda_{l_2},
\quad
\frac12\lambda_{l_1}+p_{b,l_2},
\quad\text{或相应的一形式特征值之和}.
\]
将有限维张量分量对角化后，可以出现曲率位移或有限矩阵，但不会普遍变成
\[
(\lambda_{l_1}+a)(\lambda_{l_2}+b).
\]
JSON 中的代数反例 \(1/5\ne1/9\) 正确表达了这一点。

### 热核公式需要补上谱投影

原文写出的
\[
P^{-1}=\int_0^\infty e^{-tP}\,dt
\]
在当前背景上不能直接使用。事实上：

- \(P(g_1-g_2)=-\Lambda(g_1-g_2)\)；
- 更一般地，平行张量 \(g_1,g_2\) 均有特征值 \(-\Lambda\)；
- quotient 上还有四个零模。

正确的伪逆表示可写成
\[
G^\perp
=
\sum_{\sigma<0}\sigma^{-1}\Pi_\sigma
+
\int_0^\infty
\left(
e^{-tP}-\Pi_0-\sum_{\sigma<0}e^{-t\sigma}\Pi_\sigma
\right)\,dt.
\]
括号中只留下严格大于零的谱。各张量块的 \(e^{-tP}\) 在投影修正前按产品热核分离；有限个谱投影则单独加入。

### adjacent 节点的关键细节

对 \((N,N)\to(N,S)\)，完整四维点彼此不同，Green 核及其全部 jet 均光滑。热核中第二因子的 antipodal Gaussian 因子在 \(t\downarrow0\) 时提供
\[
e^{-\pi^2/(ct)}
\]
衰减，从而压住第一因子在 coincident 点的短时奇性。

所谓 massive one-factor 化简只有在投影方向选择正确时才可逐项取值：

- 若 coincident 因子先被投影到固定特征空间，剩下的是另一因子上的 antipodal massive Green 问题，逐项光滑。
- 若 antipodal 因子先固定，而剩下 coincident 因子的二维 Green 核，则每一项通常含对数奇性；其消去依赖对另一因子全部模态的总和，不能逐项取静态值。

因此 adjacent 情形最自然的严格表达是完整产品热核，或经过证明且把 coincident 因子固定下来的 massive 化简。

---

## 3. \(T^2\) 字符筛选与无限 \(l\)

对标量球谐函数，
\[
Y_l^m(\theta,\phi)=O(\theta^{|m|})
\]
在极点成立，所以 \(k\)-jet 只能看见 \(|m|\le k\)。二阶 jet 中 \(|m|=2\) 的系数与
\[
P_l''(1)
=\frac{(l+2)(l+1)l(l-1)}8
\]
成比例，对每个 \(l\ge2\) 都非零。文件中的端点符号
\[
P_l''(-1)=(-1)^lP_l''(1)
\]
也正确。

张量或 spin-weighted harmonics 必须把纤维本身的 isotropy weight 计入。若局部张量标架具有 weight \(q\)，真正的极点条件是形如
\[
|m\pm q|\le k,
\]
符号取决于约定，而不是无条件的 \(|m|\le k\)。使用全张量的总 \(T^2\)-字符可以避免这一歧义。

EH kernel-product 的四个字符
\[
(\pm2,0),\qquad(0,\pm2)
\]
与
\[
K^+_{\mathbb C}\sim(\pm1,\pm1),
\qquad
K^-_{\mathbb C}\sim(\pm1,\mp1),
\qquad
\operatorname{Sym}^2_0\simeq\Lambda^+\otimes\Lambda^-
\]
相容。半转 quotient 给出 \(m_1+m_2\) 为偶数。这里得到的是少数等变通道；每个通道仍含所有满足 \(l_a\ge|m_a|\) 的次数。

---

## 4. D8、spin 解释与 full-\(P\) kernel

### D8 组合约化

四节点方格上，由两种 pole flip 和 factor swap 生成的八元素置换群及其子集轨道计算正确：

- \(r=1\) 与 \(r=3\) 经 \(c\) 和 complement 对应；
- \(r=2\) 分为 adjacent 与 diagonal；
- diagonal 子集稳定子大小为 \(4\)，adjacent 为 \(2\)。

这里的 \(D_8\) 是节点置换群，不是乘积背景的全部等距群；连续 \(T^2\) 以及固定节点但非平凡作用于局部标架的分量仍提供额外等变关系。

对任意 EH 方向和尺度，稳定子只给出
\[
F(\gamma\cdot t,\gamma\cdot\zeta)
=
\rho_{\rm out}(\gamma)\,
F(t,\zeta)\,
\rho_{\rm in}(\gamma)^{-1}.
\]
只有当参数本身也由 \(\gamma\) 固定时，才能把它化成同一数组上的数值相等。类似地，\(r=1\) 与 \(r=3\) 的比较必须包含 \(c\) 对 \(\Lambda^\pm\)、kernel basis 和 EH 参数的运输。

### diagonal = spin

单个 \(S^2\) 上半转的 spin lift 在南北极取相反符号，两因子相乘给出
\[
(+,-,-,+)
\]
至多差一个整体符号，因此同号节点组成对角 pair。这支持“spin pair 属于 diagonal orbit”。

不过从 fixed-point lift 符号到 punctured quotient 上两个 \(RP^3\) spin structures 的对应，还依赖 seam orientation 和填充约定。现有文件未给出独立的 Kirby 或局部 spin-trivialization 推导，所以 diagonal \(=\) spin 适合作为工作识别和拓扑解释，而不能参与 Green 系数本身的证明。

另有一个术语应修正：\(\rho(z,w)=(-z,-w)\) 在每个 \(S^2\) 上是有南北极固定点的半转，不是 antipodal map；真正的 antipodal map 没有固定点。

### 四个 full-\(P\) 零模

令 \(u_1,u_2\) 为两个因子上 quotient-invariant 的轴向 \(l=1\) 函数，
\[
\Delta u_a=2\Lambda u_a.
\]
则
\[
u_1g_1,\quad u_1g_2,\quad u_2g_1,\quad u_2g_2
\]
都满足 \(Ph=0\)。Step 68 关于 TT kernel 为零的直接推导是正确的，但 TT rigidity 并不自动给出 full-\(P\) 伪逆。

需要区分两个操作：

1. \(\bar h\perp\ker P\) 只固定伪逆解的唯一性；
2. 源 multipole 对零模的配对决定
   \[
   P\bar h=S-\Pi_{\ker P}S
   \]
   中的投影系数，即 Ozuch 的 \(\nu_l\)。

因此，“正交切片”不能单独替代 \(\nu_l\) 计算。完整处理只有两种数学形式：证明所有相关源配对恒为零；或保留四个投影系数并写出相应有限维方程。若采用 reduced Bianchi/gauge slice，还需明确该 slice 上的算子、余核和源张量确实都落在同一子空间。

---

## 5. inter-node jet 与 Ozuch \(\mu\) 的阶数

这是 Step 76 中最需改写的一处。

由 EH 渐近，
\[
H^4(t_i\phi_i)=t_i^2H^4(\phi_i).
\]
另一方面，Ozuch 的局部方程是
\[
t_j\lambda_{j,k}+t_j^2\mu_{j,k}
=O(t_{\max}^{5/2}).
\]
在乘积背景上
\[
R^\pm=\operatorname{diag}(\Lambda,0,0),
\qquad \phi_j\in\ker R^\pm,
\]
所以 \(\lambda_{j,k}^{(0)}=0\)。Ozuch 给出的 determinant 公式还推出径向分量
\[
\mu_{j,1}^{(0)}
=
C\det\!\left(R^\pm|_{\phi_j^\perp}\right)=0,
\]
因为该二维块的特征值为 \(\Lambda,0\)。所引文段并未单独给出全部 \(\mu_{j,2},\mu_{j,3}\) 的公式。

源 \(i\) 的正则二阶 jet 在节点 \(j\) 为 \(O(t_i^2)\)，故它对 receiver 第一 obstruction 的改变量具有形式
\[
\delta\lambda_{j,k}
=t_i^2\,\mathcal I_{ji,k}+o(t_i^2).
\]
代回有限维方程后得到
\[
t_j\,\delta\lambda_{j,k}
=
t_jt_i^2\,\mathcal I_{ji,k}+\cdots.
\]
等尺度 \(t_i=t_j=t\) 时，这是 \(t^3\) 阶项，而不是 Ozuch 原始记号中的 \(t^2\mu\)。

因此，下一计算真正得到的对象更准确地写成
\[
\mathcal I_{ji,k}
=
c\Big\langle
\delta R_j^{\epsilon_j}
\bigl(H_{ji,0},H_{ji,2}\bigr)\phi_j,
\,e_{j,k}
\Big\rangle,
\]
即 multipole-to-curvature interaction map。若先构造一种 chirality 的部分解消，再把另一种 chirality 的 EH 插入剩余节点，它会成为部分解消背景上的第一 obstruction；但它仍不等同于 Proposition 2.10/Equation (23) 中的局部 \(\mu\)。

---

## 6. 对角 \(r=2\) 校准的完整数学产物

一个足以独立复验的 diagonal 计算应包含以下具体对象：

1. **固定规范**：\(\Lambda\)、产品 orientation、四个 orbifold charts、\(\Lambda^\pm\) 基、kernel basis、factor swap 与 \(c\) 的矩阵，以及 \(P=\frac12\nabla^*\nabla-\mathring R\) 的因子 \(1/2\)。

2. **源 multipole 的精确定义**：用小球面通量给出分布 \(S_{i,\zeta}\)，使
   \[
   \bar h_i^4=G^\perp S_{i,\zeta},
   \qquad
   \bar h_i^4\sim H^4(\zeta)
   \]
   的常数与符号唯一确定。

3. **全部 kernel 投影**：
   \[
   \nu_{i,l}=\langle S_{i,\zeta},v_l\rangle
   \]
   或其通量等价式；同时说明 diagonal 总配置中这些系数如何相消或进入有限维方程。

4. **有序节点对的正则数据**：
   \[
   (H_{ji,0},H_{ji,2}),\qquad i\ne j,
   \]
   随后执行 \(\psi(H_{ji,0})\) 归一化并输出
   \[
   \delta R_j^\pm,\qquad \mathcal I_{ji,k}.
   \]
   结果应覆盖 receiver kernel 平面的一个固定实基，而不仅是一个对称方向。

5. **实际 obstruction 展开**：明确写出
   \[
   F_{j,k}(t,\phi)
   =
   t_j\lambda^{(0)}_{j,k}
   +t_j^2\mu^{(0)}_{j,k}
   +\sum_{i\ne j}t_jt_i^2\mathcal I_{ji,k}
   +\cdots,
   \]
   并标出此次程序计算的是哪一个系数。

6. **强校验关系**：
   - factor-swap 与 diagonal 稳定子的等变性；
   - \(c\) 诱导的 chirality/complement 运输；
   - Green 自伴性给出的 source–jet reciprocity；
   - all-compatible 与 all-reversed 已知 Einstein 行中，总投影和总 interaction 应按同一规范相消。

7. **可证误差控制**：热核采用短时/长时分裂。短时部分用 antipodal Gaussian 衰减控制全部二阶导数；长时部分在去除零模及 \(\sigma<0\) 模后用严格谱隙控制。若使用双球谐和，应规定 Abel/Ewald 求和次序并给出尾项区间，而不能依赖未经证明的交错相消。

---

## 与 Yau 第26题的关系

一个固定 diagonal 对称参数点上的非零 \(\mathcal I\)，只排除具有该尺度、EH 方向、slice 和 orbifold 极限的渐近 Einstein 序列。要排除整个 smooth row 的所有近 orbifold 序列，还需要证明该有限维映射在全部允许参数上无零点，并处理 orbifold deformation 与 gauge 投影。

反之，一个有限阶系数为零也不产生 Einstein 度量；后续阶、非线性可解性和参数横截性仍需独立证明。无论哪种数值结果，都不涉及远离该 orbifold degeneration 的 Einstein 度量，因此不会单独证明或否定 Yau 第26题。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 41,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step41_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step41_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Evaluate the Step-40 diagonal toric reframe and the Step-41 critical updates for the Yau-26 project. The central questions are: (1) Does Liu's source really make the diagonal-sector identification unconditional for closed simply connected Einstein 4-manifolds with diagonal T^2 action, without nonnegative sectional curvature? (2) What exactly is source-grade about the reduced orbit-metric problem: fixed g_Σ determines g^Ω uniquely, but existence requires determinant/eigenfunction and boundary compatibility; does this justify saying the system is overdetermined, and what remains unproved? (3) Does the corrected Step-41 FEM probe legitimately strengthen or weaken the claim that constant-curvature m>=6 diagonal polygons are inconsistent? Treat it only as numerical evidence. (4) For Yau-26 route allocation, how much value should remain in the diagonal toric front versus returning to Route A's noncollapsed bridges or the negative cutoff-flow front? Please identify hidden overclaims, target drift, and the best next mathematical object to attack, using the files, not general guesses.

## Integrated Scientific Memo

# Step 40–41 核验结论

## 1. 对角扇区识别确实不依赖 \(\sec\ge0\)

Liu 的原文支持如下无条件链条；这里“无条件”仍指保留**闭、单连通、Einstein 四流形及等距 \(T^2\)-作用**这些假设：

1. **Theorem 3.1**：任意这样的作用都是 geometrically polar，故水平分布可积、twist scalars 消失。
2. **Proposition 5**：若作用是 diagonal，即所有余维二奇异层的 isotropy 都属于 \(S(1,0)\) 或 \(S(0,1)\)，则
   \[
   g^\Omega_{12}\equiv0.
   \]
   证明使用 Proposition 3 的线性方程和 Lemma 5.2 的唯一性，不使用截面曲率非负。
3. 此时
   \[
   g^\Omega=\operatorname{diag}(a^2,b^2).
   \]
   杆 \(S(p,q)\) 上消失向量的平方长度为
   \[
   p^2a^2+q^2b^2.
   \]
   在杆的内部只有一个纤维因子消失，因此杆类只能是无向的 \([e_1]\) 或 \([e_2]\)。相邻 primitive labels 的行列式必须为 \(\pm1\)，所以两类必须交替。

因此，“diagonal action \(\Rightarrow\) diagonal metric”和“diagonal metric 的杆类恰为两个交替坐标类”都成立，而且不需要 \(\sec\ge0\)。非负截面曲率只在 Liu 后续把商空间压成平坦矩形、进而分类时进入。

必须修正三个表述：

- \(\pm e_i\) 表示同一个 isotropy circle；符号只是 primitive representative 的选择。
- 闭合交替多边形的边数必须为偶数。真正的族为
  \[
  m=2k+2,\qquad M\cong \#_k(S^2\times S^2).
  \]
  JSON 中 \(m=5\mapsto\#_1(S^2\times S^2)\) 是错误的；奇数 \(m\) 只能作为纯几何数值测试。
- “Page/CLW/\(dP_3\) irrelevant”过强。记录的 toric actions 含三个以上无向 circle classes，所以不能校准**交替对角杆 ansatz**；但它们仍可校准一般 polar 方程、行列式约定和边界归一化。且这些具体 fan labels 在所给 Liu 文本中没有来源，应另行核准。

Liu 并未证明无 \(\sec\ge0\) 时 \(S^2\times S^2\) 的 product Einstein metric 唯一，也未分类全部 diagonal Einstein metrics。

---

## 2. 固定 \(g_\Sigma\) 时只有唯一候选；存在性仍是非线性兼容问题

### 源文严格给出的内容

令
\[
\phi=\sqrt{\det g^\Omega}.
\]
Liu Proposition 2 给出
\[
-\Delta_\Sigma\phi=2\Lambda\phi,\qquad
\phi>0\ \text{于内部},\quad \phi|_{\partial\Sigma}=0,
\]
所以
\[
\lambda_1(\Sigma,g_\Sigma)=2\Lambda.
\]

每个纤维矩阵分量 \(u=g^\Omega_{ij}\) 满足
\[
-\frac12\Delta_\Sigma u
+\frac1{2\phi}\langle\nabla\phi,\nabla u\rangle
+2K_\Sigma u
=\Lambda u. \tag{1}
\]
Proposition 3 与 Lemma 5.2 说明：固定 torus action 和 \(g_\Sigma\)，并固定作用与杆光滑性所决定的 Dirichlet 边值后，满足 smooth-even 条件的解至多一个。因此严格结论是：

> 固定 \((T^2\text{-action},g_\Sigma)\) 后，至多存在一个 invariant Einstein completion。

不是“总存在且唯一”。

杆上 surviving-circle 长度 \(u\) 还满足
\[
-\frac{u''}{u}+2K_\Sigma=\Lambda, \tag{2}
\]
及归一化后的过定端点数据
\[
u(0)=u(\ell)=0,\qquad u'(0)=1,\qquad u'(\ell)=-1.
\]
在 \(K_\Sigma=-A,\Lambda=1\) 时才推出
\[
\ell=\frac{\pi}{\sqrt{1+2A}}.
\]

### 仍未证明的兼容条件

即使解出主特征函数和 (1)，仍须同时满足：

1. \(\lambda_1=2\Lambda\) 及与杆导数归一化一致的 \(\phi\)；
2. 每条边的 ODE (2) 满足四个端点条件；
3. \(g^\Omega_{ij}\) 的 smooth-even 边界/角点 jets；
4. 内部正定性；
5. 核心闭合条件
   \[
   \det g^\Omega=\phi^2; \tag{3}
   \]
6. 水平 Einstein 方程。对角情况下为
   \[
   \operatorname{Ric}_\Sigma
   -a^{-1}\operatorname{Hess}a
   -b^{-1}\operatorname{Hess}b
   =\Lambda g_\Sigma. \tag{4}
   \]

Liu Proposition 4 的价值恰是展示：逐分量线性问题可以有唯一候选，但该候选仍可因 (3) 失败而不是 Einstein metric。源文没有证明 (1)、特征函数方程和 (3) 自动蕴含 (4)。

因此，“overdetermined”可以作为**全局兼容性描述**：固定 \(g_\Sigma\) 后，纤维矩阵被唯一性定死，而 (3)、(4)、正定性及杆/角点数据仍可能不兼容。但不能把“一个自由函数、三类约束”当成 Fredholm 指标或刚性证明。Einstein 方程存在 Bianchi 依赖，二维度量还有 diffeomorphism gauge 与 polygon moduli；必须写出完整规范固定线性算子，计算其 kernel/cokernel。

### Step 40 的 product 线性化目前不可信

在
\[
g_{\Sigma,0}=dx^2+dy^2,\quad a_0=\sin x,\quad b_0=\sin y
\]
处写
\[
g_\Sigma=e^{2\varepsilon s}g_{\Sigma,0},\quad
a=a_0+\varepsilon\alpha,\quad b=b_0+\varepsilon\beta,
\]
并令
\[
\psi=\delta(ab)=\alpha\sin y+\beta\sin x.
\]
直接线性化
\[
-\Delta_{g_\Sigma}(ab)=2ab
\]
得到
\[
-(\Delta_0+2)\psi=4s\sin x\sin y. \tag{5}
\]
二维共形变换满足
\[
\Delta_{e^{2\varepsilon s}g_0}=e^{-2\varepsilon s}\Delta_0,
\]
故直接线性化中没有 \(\Delta s\) 项。

Step 40 所写
\[
-(\Delta_0+1)\alpha=(\Delta_0s-2s)\sin x
\]
并非 Proposition 2 的直接线性化；若它来自结合水平方程后的消元，当前文件缺少推导。其所谓 kernel mode \(\alpha=\sin x\) 在 \(s=0\) 时也违反所列杆导数修正：
\[
\alpha_x(0)=1,\qquad \alpha_x(\pi)=-1,
\]
而完整边界条件要求零修正。固定 \(\Lambda=1\) 时也不能简单称为“\(\Lambda\)-rescaling”。

尚缺 \(\beta\) 方程、(4) 的完整线性化、geodesic-edge 条件、角点兼容、商空间共形模量和 diffeomorphism quotient。因此 product isolation 目前只是猜想。

---

## 3. 修正 FEM 的合法结论：支持受限模型不相容，但削弱“大间隙”叙事

Poincaré disk 中
\[
g=\rho(dx^2+dy^2),\qquad \rho=\frac4{(1-r^2)^2}.
\]
二维下
\[
\int|\nabla u|_g^2\,dV_g
=\int|\nabla u|_{\rm Euc}^2\,dx\,dy,\qquad
\int u^2\,dV_g=\int\rho u^2\,dx\,dy.
\]
所以修正版本以 \(\rho\) 而非 \(\rho^2\) 作为 mass weight 是正确的；旧 probe 应完全废弃。

设 \(P_m\subset\mathbb H^2(-1)\) 为正则直角 \(m\)-边形，
\[
\mu_m=\lambda_1(P_m).
\]
缩放到曲率 \(-A\) 后
\[
\lambda_1=A\mu_m.
\]
当 \(\Lambda=1\) 时，特征值条件要求
\[
A_{\rm eig}=\frac2{\mu_m},
\]
而杆长与正则边长相等要求 \(A=A_{\rm side}\)。故该受限模型必须满足
\[
A_{\rm eig}=A_{\rm side}
\quad\Longleftrightarrow\quad
\mu_m=\frac2{A_{\rm side}}. \tag{6}
\]

对首个真实 diagonal 案例 \(m=6\)，最细网格给出
\[
\mu_6\approx6.97315,\qquad
A_{\rm eig}\approx0.286815,\qquad
A_{\rm side}\approx0.270961.
\]
在 \(A_{\rm side}\)：
\[
\lambda_1\approx1.88945,
\]
比 \(2\) 低约 \(0.11055\)；在 \(A_{\rm eig}\)，杆仅比边长约 \(1.84\%\)。

这比 Step 40 的 Faber–Krahn 估计更有辨别力，因为后者并未排除 \(A_{\rm side}\)。网格序列也显示稳定趋势。但它仍不是认证的谱界：未给出脚本、严格域表示、quadrature 误差及 interval enclosure。

尤其，Step 40 的“\(m=6\) 有 \(68.7\%\) gap”来自 \(A\to\infty\) 渐近区，并非特征值选出的几何参数。相关参数处真正的 rod/side mismatch 只有约 \(1.8\%\)，这是一个 near miss。故修正 FEM：

- **加强**了“所测试的正则常曲率模型不同时满足两项必要条件”的数值证据；
- **削弱**了“存在巨大几何障碍”的解释；
- 仅覆盖所运行的 \(m=6,8,10,12\)，不能推出所有偶数 \(m\ge6\)；
- 完全不覆盖 variable \(K_\Sigma\)、非正则多边形、完整方程 (3)–(4)，更不覆盖非 toric Einstein metric。

可转化为严格短定理的对象是：构造可认证的 conforming trial function，使
\[
\mathcal R(u)<\frac2{A_{\rm side}}
\]
并用精确内多边形及区间积分控制误差，从而严格排除 \(m=6\) 的**正则常曲率**模型。即便完成，其 Yau-26 杠杆仍有限。

---

## 4. 研究价值与最佳下一对象

### 对角 toric front

应保留为四维正号、对称性受限的 collapse laboratory，但不应成为主线。其已获得的耐久成果是无 \(\sec\ge0\) 的 diagonal reduction；尚未获得：

- 任意 \(m\ge6\) diagonal Einstein 非存在；
- \(\#_k(S^2\times S^2)\) 上任意 Einstein metric 非存在；
- 从 Yau-26 的 \(C^0\)-Ricci pinching 推出 \(T^2\) symmetry；
- 甚至一个趋于 Einstein 的 diagonal pinched stress family。

\(b_+\ge2\) 也不是现成障碍：所给来源没有“正 Einstein 且有 \(T^2\) 作用必有 \(b_+\le1\)”定理，Hitchin–Thorpe 本身不排除这些 connected sums。

若继续该 front，最有价值的对象不是更多常曲率 FEM，而是首个真实案例 \(m=6\) 的完整**variable-curvature nonlinear compatibility map**：
\[
g_\Sigma
\longmapsto
\Bigl(
\lambda_1(g_\Sigma)-2\Lambda,\ 
\det g^\Omega[g_\Sigma]-\phi[g_\Sigma]^2,\ 
\mathcal E_{\rm hor}[g_\Sigma]
\Bigr),
\]
连同 geodesic right-angle boundary、杆 jets、角点光滑性和 gauge fixing。需证明该映射无零点或构造零点；这才是实际 diagonal existence problem。

### Route A：更直接的正号非坍缩桥梁

Step 33 中最清晰、有限且贴近原问题的对象是
\[
C(S^3/\mathbb Z_2)
\]
上 symmetric \(2\)-tensor 的真实 Lichnerowicz–Bianchi indicial inventory：处理 \(\mathbb Z_2\) parity、trace/Bianchi/volume gauge 和 pure-gauge quotient，确认 \((-4,2)\) 中是否只剩可去除的 \((0,-2)\) 对以及几何 \((2,-4)\) 对，并写出与 Ozuch \(R_+v=0\) 对应的 Wronskian pairing matrix。随后所需的是 balanced annulus
\[
r\asymp t^{2/3}
\]
上的 harmonic-radius/无中间尺度能量损失定理，使误差配对成为 \(o(t^4)\)。

这条线不假设 toric symmetry，直接面向 \(C^0\)-Ricci-pinched 非坍缩序列，因此在现有正号候选中科学杠杆最高；但仍仅覆盖四维非坍缩子情形。

### 负号 cutoff-flow front

A03 的 staggered induction 实质性修复了两项高阶 bookkeeping 错误，但它仍假设正时间光滑解及 \(\sup|U|<\infty\)，尚未给出：

- transported-coefficient start/restart；
- 从仅有的 Ricci-endomorphism pinching 推出 \(U\)-控制；
- sequence-uniform smoothing/calibration；
- 维数统一、与流形无关的 collapse 控制。

因此它有跨维潜力，但距 Yau-26 antecedent 的关键桥仍未建立。最具体的近期对象是固定 cutoff 退化方程的 Ricci–DeTurck start/restart，加上由 Ricci defect 导出 \(U\)-控制；而维数统一的 collapse-independent 常数仍是更深的最终瓶颈。

## 综合判断

优先级应由与原命题的逻辑距离决定：

1. **最高直接价值：** Route A 的真实 cone indicial/Wronskian 计算及 balanced-annulus bridge。
2. **高潜力但桥梁较长：** 负号 flow 的 start/restart 与 pinching-to-\(U\) 控制。
3. **保留但降权：** diagonal toric front；只值得攻击 \(m=6\) variable-curvature 的完整闭合映射，而非继续细化常曲率 near miss。

主要 target drift 不是 diagonal identification——它是正确的——而是把“固定商度量至多一个 completion”和“受限常曲率数值不匹配”滑向“任意 Einstein metric 不存在”或“Yau-26 正号支路已受控”。现有来源不支持这些升级。
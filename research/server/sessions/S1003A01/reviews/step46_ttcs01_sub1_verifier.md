# TTCS Independent Branch Record

```json
{
  "step_id": 46,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step46_o10_finite_marked_block_and_spinor_matching.md",
    "Sessions/S1003A01/workspace/scripts/step46_o10_block_matching.py",
    "Sessions/S1003A01/workspace/data/step46/o10_block_matching.json",
    "Sessions/S1003A01/workspace/notes/step45_o10_cell_tiling_tidal_radius_charge.md",
    "Sessions/S1003A01/workspace/data/step45/tnads_cartan.json",
    "Sessions/S1003A02/workspace/scripts/verify_gh_tangent.py",
    "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_generator2_integration.md",
    "Skills/geometric-analysis/research/sources/archive/sources/20261001-web-increment/Line1_Web_Increment_20260929_30/research/B/O10_Resolvent_Prolongation.md",
    "Skills/geometric-analysis/research/sources/continuation/20260926_actual_topological_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_actual_torsion_prolongation.md"
  ]
}
```

## Task

Read the Step-46 note and its computation against the inherited O10 equations and the exact TN/TNAdS sources. Check especially: (i) why a periodic one-compatible-nut block is topologically inadmissible; (ii) the distinction among circle Chern degree, scalar mass flux, and determinant/torsion boundary data; (iii) the half-order expansion Phi=Phi0+L chi1+..., the coefficient a=sqrt(2)/3, and the exact parent Hessian-energy calculation; (iv) the Hermite jet interpolation identity and its four-dimensional collapsed-cell scaling; (v) the correction that the raw TN field requires a leading q-pairing rather than solving the normalized resolvent equation at the flux-balance radius; and (vi) whether the finite marked-block problem states the correct residual and Cauchy scales. Identify any mathematical error, convention ambiguity, missing hypothesis, or stronger consequence. Give corrected formulas where needed.

## Output

# 独立科学核验备忘

## 总体结论

Step 46 的四个核心计算是正确的：

1. 在保持同一半自由 \(S^1\) 结构的周期商中，一个同号 nut 不能单独出现。
2. \(\Phi=\Phi_0+L\chi_1+\cdots\) 的首项确为 \(L\) 阶，且
   \[
   a=\frac{\sqrt2}{3},\qquad
   \int_{B_R}|\nabla^2\chi|^2
   =\frac{32\pi^2}{9}\ell^2\left(\frac{R}{R+\ell}\right)^2.
   \]
3. Hermite 插值公式及 \(L^{-2}\) 重置代价正确。
4. 在 Ricci-flat TN 上，原始粗调和场满足 \(q=-2v\)，故其 \(q\)-配对是主阶 \(-2M\)，并非小量。

有三处需要实质改写：

- 周期 nut 的拓扑结论依赖于整个拼接保持同一个自由圆纤维结构；任意非对称度量拼接并不保留这个整数。
- Step-46 脚本把 TN 与 TNAdS 的量放在同一数据行中：法向导数使用 TNAdS 的 \(F/H\)，质量通量和能量却使用 TN 公式。因此第 5 节给出的精确 \(-2M\) 是 TN 算子的恒等式，不是已经计算出的 TNAdS 解析结果。
- 式 (6.5) 不是同一胶合界面上的标准 Cauchy 拼接式；它应解释为相距 \(L\) 的两个横截面之间的慢变 jet 条件。同一界面上的实际拼接要求值相等、两侧外法向导数互为相反数。

---

## 1. 一个周期同号 nut 为何不可能

设 \(Q\) 是周期商的三维轨道空间，去掉 nut 的一个小球，圆轨道构成主 \(S^1\)-丛。取归一化连接曲率 \(\Omega\)，则
\[
d\Omega=0,\qquad
\frac1{2\pi}\int_{S^2_{\rm nut}}\Omega=+1
\]
，其中 \(S^2_{\rm nut}\) 按从 nut 向外的方向定向。

若基本胞元的相对面通过保持圆纤维的映射识别，则这些面上的曲率积分两两抵消。对穿孔后的周期商应用 Stokes：
\[
0=\int_Qd\Omega
  =\int_{\partial Q}\Omega
  =-\int_{S^2_{\rm nut}}\Omega=-2\pi,
\]
矛盾。若胞元还有真实外端，则定向符号给出
\[
\frac1{2\pi}\int_{S^2_{\rm out}}\Omega
=\frac1{2\pi}\int_{S^2_{\rm nut}}\Omega=1.
\]
多个同号 nuts 时，外侧 Chern 数等于 nut 数目的总和。

这段论证需要以下几项：

- 一个全局一致的圆生成元及其取向；
- nut 外部确实是自由主 \(S^1\)-丛；
- 周期识别映射保持该丛结构。

现有 O10 估计本身并未产生这种全局圆作用。若外部过渡区不再保持圆纤维，Hopf 纤维整数不再是整个拼接度量的不变量；任意四维度量可以沿 \(S^3\) 接入而不延拓该圆作用。因此，“所有 degree 必须到达宏观外端或由 bolts、异号 nuts 抵消”只在圆结构贯穿全部过渡区时成立。对一般 O10 序列，还需要一个把近似纤维方向延拓为实际主丛或弱圆结构的定理。

---

## 2. 三类通量确实彼此独立

### 2.1 几何圆 Chern 数

这是轨道空间二维截面上的整数：
\[
\deg_{\rm circ}
=\frac1{2\pi}\int_{\Sigma^2}\Omega\in\mathbb Z.
\]
它无量纲，属于几何圆丛，而不是 Spin\(^c\) 行列式线丛。

### 2.2 标量质量通量

这是总空间三维外侧界面上的实数：
\[
\Phi_m(Y)=\int_Y\partial_\nu |v|^2\,dS.
\]
对当前胞元它的自然量级是
\[
\Phi_m=O(\ell^2)=O(L^6).
\]
即使 \(\deg_{\rm circ}=1\)，这个数仍可趋于零；反之，它也不携带整数拓扑信息。还应区分“绝对趋零”和胞元归一化后的 \(o(L^6)\)：原始 TN 通量虽绝对趋零，却仍与胞元体积同阶。

### 2.3 行列式连接与 torsion 数据

\(A,\Phi,t_\Phi\) 给出的是另一组信息：

- \(A^{\tan}\) 及参考平凡化下的 Chern–Simons 数；
- \(\Phi\) 与其协变法向导数；
- \(t_\Phi\) 的迹及其相对零点指数。

nut 邻域在四维上是一个球，普通复线丛可完全平凡，而其外侧 \(S^3\) 仍带 degree-one Hopf 圆纤维。故几何圆 degree 不等于 \(c_1(L)\)。同样，标量通量只见到 \(|v|^2\)，不能恢复 \(A\) 的切向 holonomy 或 \(t_\Phi/|t_\Phi|\) 的相对同伦类。

相对 torsion 指数还要求 \(t_\Phi\) 在外侧界面处处非零，并选定平凡化。块内 \(H^1\) 接近本身不能推出迹的逐点非零；需要 \(C^0\) 迹估计或单独的非消失输入。

---

## 3. \(L\chi_1\) 首项、系数与 Hessian 能量

在 Ricci-flat TN 切空间上取平行正手征基 \(e_1,e_2\)，令
\[
\Phi_0=\sqrt{\rho_*}\,e_1,\qquad
\rho_*=\frac43,
\qquad
\chi=a\,\bar f\,e_2.
\]
按所给 Clifford 约定，torsion 的线性化满足
\[
D t_{\Phi_0}(\chi)
=2\rho_*a\,\mathbf e^-_1.
\]
另一方面
\[
v_{\rm TN}
=\sqrt{\frac{m_*}{2}}\,d\bar f
=\sqrt{m_*}\,\mathbf e^-_1,
\qquad m_*=\frac{128}{81}.
\]
故
\[
2\rho_*a=\sqrt{m_*},
\qquad
a=\frac{\sqrt{m_*}}{2\rho_*}
=\frac{\sqrt2}{3}.
\]
不同 Clifford 相位约定可能把 \(a\) 乘以单位复数，或交换 \(f,\bar f\)，但其模及能量不变。

因为 \(f=x_1+ix_2\) 在物理胞元上是 \(O(L)\)，在 \(X=x/L\) 坐标中
\[
a\bar f\,e_2=L\,a(\bar X_1-i\bar X_2)e_2.
\]
因此正确写法是
\[
\Phi=\Phi_0+L\chi_1(X)+L^2\chi_2(X)+\cdots ,
\qquad
\chi_1(X)=a(X_1-iX_2)e_2.
\]
式 (6.2) 中“\(\chi_1\) contains \(a\bar f e_2\)”应明确这里的 \(f\) 是胞元坐标函数；若仍用物理 \(f\)，就会重复计入一个 \(L\)。

由于
\[
v=\sqrt{\frac{m_*}{2}}\,d\bar f,\qquad
\chi=a\bar f e_2,
\]
且 \(e_2\) 在 TN 上平行，
\[
|\nabla^2\chi|^2
=\frac{2a^2}{m_*}|\nabla v|^2
=\frac9{32}|\nabla v|^2.
\]
代入
\[
E_{\rm TN}(R)
=8\pi^2m_*\ell^2
 \left(\frac{R}{R+\ell}\right)^2
\]
即得
\[
\int_{B_R}|\nabla^2\chi|^2
=\frac{32\pi^2}{9}\ell^2
 \left(\frac{R}{R+\ell}\right)^2.
\]

TN/TNAdS 的精确径向体积为
\[
\operatorname{Vol}(B_R)
=16\pi^2\ell
 \left(\frac{R^3}{3}+\frac{\ell R^2}{2}\right).
\]
取 \(R=cL,\ \ell=L^3,\ c^3=3/4\)，则
\[
\operatorname{Vol}(B_{cL})
=4\pi^2L^6+8\pi^2c^2L^8,
\]
从而
\[
\frac{\int|\nabla^2\chi|^2}{\operatorname{Vol}(B_{cL})}
\longrightarrow\frac89.
\]
这一计算是 TN 切模型上的精确结果，也是 TNAdS 块的首阶渐近量；它不是 TNAdS 上完整正旋量 Hessian 的精确分解，因为 TNAdS 不再有这组平行旋量，后续修正还会产生交叉项。

---

## 4. Hermite 公式及塌缩四维缩放

对实、复或 Hilbert 空间值的 \(u\)，固定两端一阶 jet 后，Euler–Lagrange 方程是 \(u^{(4)}=0\)，所以极小元是唯一三次 Hermite 多项式，并且
\[
\inf\int_0^L|u''|^2
=
\frac{12}{L^3}
\left|u_1-u_0-\frac L2(p_0+p_1)\right|^2
+\frac1L|p_1-p_0|^2.
\]
Step-46 脚本中的数值与此完全一致。

若基方向宽度为 \(L\)，横截面三维体积为 \(A_L\asymp L^5\)，则胞元体积为 \(A_LL\asymp L^6\)。重置数据
\[
u_1=u_0,\qquad p_1=p_0=p\ne0
\]
给出
\[
E_{\rm cell}\ge A_L\frac{12|p|^2}{L},
\qquad
\frac{E_{\rm cell}}{\operatorname{Vol}_{\rm cell}}
\ge\frac{12|p|^2}{L^2}.
\]
因而 \(L^{-2}\) 发散律正确。

这成为协变四维估计时还需：

- 一个厚度可比于 \(L\) 的乘积型或均匀可控 collar；
- 沿同一有向法线比较 jet；
- 先用同一个 Spin\(^c\) 与行列式 gauge 识别两端；
- 控制几何 Jacobian 与联络的低阶项。

在这些条件下，有限 Hessian 密度要求横截面 RMS 意义下
\[
p_1-p_0=O(L),\qquad
u_1-u_0-\frac L2(p_0+p_1)=O(L^2).
\]
若有比例 \(\eta_L\) 的胞元发生 \(|p|\ge p_0\) 的独立重置，则统一 Hessian 密度给出更强的数量结论
\[
\eta_L=O(L^2).
\]
所以不仅“不能每个胞元重置”，而且具有固定比例的重置胞元也不可能持续存在。

### 式 (6.5) 的几何含义需改写

若两块在同一个界面直接胶合，取各自外法向 \(\nu_i,\nu_j\)，则光滑拼接要求
\[
\Phi_j=G_{ij}\Phi_i,\qquad
\nabla_{\nu_j}\Phi_j
=-G_{ij}\nabla_{\nu_i}\Phi_i,
\]
并对 \(v\) 有相同形式；连接切向部分按标准 gauge 变换拼接。

Hermite 式
\[
\Phi_1-\Phi_0-\frac L2(P_0+P_1)=O(L^2)
\]
适用于相距 \(L\) 的两个横截面，且 \(P_0,P_1\) 都沿同一有向法线定义。它不是同一胶合界面两侧的直接相等式。Step 46 的 (6.5) 应按此前者解释，否则法向符号和空间距离均不明确。

---

## 5. 原始 TN 场的 \(q\)-配对

在 Ricci-flat TN 上，
\[
\nabla^*\nabla v_{\rm TN}=0,
\qquad
q_{\rm TN}=(\nabla^*\nabla-2)v_{\rm TN}=-2v_{\rm TN}.
\]
因此无需借助通量公式就有精确等式
\[
\operatorname{Re}\int_{B_R}\langle q_{\rm TN},v_{\rm TN}\rangle
=-2M(R),
\]
其中
\[
M(R)=\frac{16\pi^2}{3}m_*\ell R^3.
\]
同时
\[
\Phi_m^{\rm TN}(R)=2E_{\rm TN}(R),\qquad
E_{\rm TN}(R)=8\pi^2m_*\ell^2
 \left(\frac{R}{R+\ell}\right)^2.
\]
在精确平衡半径
\[
R(R+\ell)^2=\frac{3\ell}{4}
\]
处，\(2E=4M\)，故
\[
\operatorname{Re}\int\langle q_{\rm TN},v_{\rm TN}\rangle
=-2M=-E.
\]
取近似半径 \(R=cL,\ c^3=3/4\) 时，
\[
-2M=-8\pi^2m_*\ell^2
\]
是精确式，而 \(-E\) 与它相差 \(O(L^8)\)。

还有一个更强的直接结论。由 Cauchy–Schwarz，
\[
\|q_{\rm TN}\|_2^2
\ge
\frac{\left|\int\langle q_{\rm TN},v_{\rm TN}\rangle\right|^2}
     {\|v_{\rm TN}\|_2^2}
=4M.
\]
在 \(R=cL\) 处，
\[
\boxed{
\|q_{\rm TN}\|_2^2
\ge16\pi^2m_*L^6.
}
\]
故原始 TN 场明确不满足 \(\int|q|^2=o(L^6)\)。

### 这还不是一个精确 TNAdS 计算

TNAdS 对径向标量 \(m=m_*R/(R+\ell)\) 的通量是
\[
\Phi_m^{\rm TNAdS}(R)
=16\pi^2\ell R^2F(R)m'(R)
=F(R)\Phi_m^{\rm TN}(R),
\]
不是 Step-46 脚本使用的 \(\Phi_m^{\rm TN}\)。

对任意 TNAdS 上的实际 section \(v^\sharp\)，精确公式只能写成
\[
Q_{\rm AdS}:=
\operatorname{Re}\int\langle q_{\rm AdS},v^\sharp\rangle
=
E_{\rm AdS}-2M_{\rm AdS}
-\frac12\Phi_{m,\rm AdS}.
\]
要得到 \(Q_{\rm AdS}=-2M+o(L^6)\)，还需证明
\[
E_{\rm AdS}=E_{\rm TN}+o(L^6),\quad
M_{\rm AdS}=M_{\rm TN}+o(L^6),\quad
\Phi_{m,\rm AdS}=\Phi_m^{\rm TN}+o(L^6)
\]
对所选 spinor 延拓成立。

此外，若把 \(d\bar f\) 直接作为 TNAdS 上的基底协向量延拓，则
\[
|v_0|^2_{\rm TNAdS}
=\frac{m_*}{2H}
 \left(F\sin^2\theta+1+\cos^2\theta\right)
=\frac{m_*}{H}
 \left(1+\frac{F-1}{2}\sin^2\theta\right),
\]
其 \(L^2\) 阶修正已经带角向依赖。因此
\[
m=m_*\frac{R}{R+\ell}
\]
不是某个已指定 TNAdS spinor 延拓的自动精确公式。

Step-46 脚本实际上混合了两套几何量：

- `proper_dm_over_L` 使用 TNAdS 的 \(\sqrt{F/H}\)；
- `flux` 与 `tangent_energy` 使用 TN；
- `grad_v_sq` 也是 TN 公式。

这些数足以核对量级和 TN 主项，但不能视为 TNAdS resolvent 的直接求解。第 5 节的主阶机制很可信，精确 TNAdS 系数仍需实际 spinor/connection 计算。

---

## 6. 有限 marked block 的残差与 Cauchy 数据尺度

### 6.1 体内残差尺度

胞元体积为 \(O(L^6)\)，所以
\[
\|q_L\|_{L^2}=o(L^3)
\]
等价于
\[
\int_{\mathcal B_L}|q_L|^2=o(L^6).
\]
若 \(\|v_L\|_\infty\le C\)，则
\[
\left|\int\langle q_L,v_L\rangle\right|
\le\|q_L\|_2\|v_L\|_2=o(L^6),
\]
这正是从质量恒等式推出 (5.5) 所需的尺度。

同理，
\[
t_{\Phi_L}-v_L=o_{H^1}(L^3)
\]
应明确解释为
\[
\|t_{\Phi_L}-v_L\|_2=o(L^3),\qquad
\|\nabla(t_{\Phi_L}-v_L)\|_2=o(L^3).
\]
这部分是正确的。

完整的目标系统还应显式记录，例如
\[
\|D^-_{3A_L}v_L\|_2=o(L^3),\qquad
\|\mathsf P_{J_+}\nabla v_L\|_2=o(L^3),
\]
若这些正是所继承误差的 \(L^2\) 形式。现有材料并未自动推出每个移动胞元都具备这些估计；它们可由总体平均在适当 good-block 选择后获得，或作为有限块求解的输入目标。

### 6.2 外侧 Cauchy 尺度

式 (6.4) 列出了正确的几何对象，但没有实际写出尺度。模型预测为
\[
\Phi-\Phi_0=O(L),\qquad
\nabla_\nu\Phi=O(1),\qquad
v=O(1),\qquad
\nabla_\nu v=O(L).
\]
由于 \(\operatorname{Vol}(Y_L)\asymp L^5\)，相应 \(L^2(Y_L)\) 量级是
\[
\|\Phi-\Phi_0\|_2=O(L^{7/2}),\qquad
\|\nabla_\nu\Phi\|_2=O(L^{5/2}),
\]
\[
\|v\|_2=O(L^{5/2}),\qquad
\|\nabla_\nu v\|_2=O(L^{7/2}).
\]
若在径向 gauge 中还能控制完整 \(F_A=O(1)\)，则物理切向连接通常是 \(A^{\tan}=O(L)\)；当前 O10 数据只直接控制相关曲率分量，不能无条件加入这一逐点估计。

这里的 Cauchy 元组只能作为求解后的输出。Dirac 方程与自对偶曲率方程是一阶系统，而 resolvent 方程是二阶系统；同时指定所有迹和法向导数会形成过定数据。一个真正的 Cauchy 映射还需要：

- Coulomb 或 temporal gauge；
- 模去外侧 gauge 群；
- 明确 Sobolev 迹空间；
- 固定共同法向方向；
- 对相对 Chern–Simons 数选定参考平凡化。

---

## 7. 计算文件的可复现性

`step46_o10_block_matching.py` 对以下代数给出了正确数值：

- \(a=\sqrt2/3\)；
- \(2a^2/m_*=9/32\)；
- parent Hessian 密度 \(8/9\)；
- Hermite 重置常数 \(12\)；
- TN 配对 \(-2M\) 的系数。

它没有计算 TNAdS spin connection、\(\nabla^*_{3A}\nabla_{3A}v\)、实际 torsion 或 determinant 方程，因此不能验证有限块 PDE 的存在性。

另一个所给脚本 `verify_gh_tangent.py` 按当前文件顺序在定义 `sqrtg` 和 `cs` 之前就调用二者，直接执行会产生 `NameError`。其中的 TN 公式仍可由已给出的解析计算独立确认，但该脚本需调整定义顺序后才能充当可执行佐证。

---

## 最终科学评价

Step 46 成功确立了两个真实而重要的必要结构：

\[
\text{同号 nut 的圆 degree 不能在保圆周期胞元中自行消失},
\]
\[
\text{首阶 affine spinor jet 不能逐胞元独立重置}.
\]

它也正确识别了原始 TN 粗调和场具有主阶 \(q\)-配对，并可加强为
\[
\|q_{\rm TN}\|_2^2\ge16\pi^2m_*L^6.
\]

尚未闭合的核心对象是：在精确 TNAdS 几何上选定实际 Spin\(^c\) 延拓后，计算
\[
E_{\rm AdS},\quad \Phi_{m,\rm AdS},\quad
\int\langle q_{\rm AdS},v\rangle,
\]
并同时求解 determinant、Dirac 与 cubic torsion 方程。只有这项计算才能把当前 TN 主阶不匹配提升为精确有限块结果，或展示 TNAdS 的二阶几何修正确实消去该配对。
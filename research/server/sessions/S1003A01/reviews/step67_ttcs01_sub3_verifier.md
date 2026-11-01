# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step80_Q4_universal_functional_and_lambda_quadratic.md",
    "Sessions/S1003A02/workspace/data/step80/lambda_scan_a.json",
    "Sessions/S1003A02/workspace/data/step80/universal_pi.json",
    "Sessions/S1003A02/workspace/data/step80/recon_F012_gen2_lam0.json",
    "Sessions/S1003A02/workspace/data/step80/recon_F012_gen5_lam-5.json",
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Sessions/S1003A01/workspace/notes/step65_homogeneous_torsion_zero_classification_and_surface_transport.md",
    "Sessions/S1003A01/workspace/data/step67/verify_A02_step80_reconstructions.json"
  ]
}
```

## Task

Analyze the corrected order-6 scalar functional scientifically. Read A02's Step-80 note/data and A01's independent verification. Develop a coordinate-free interpretation or at least a sharp invariant ansatz for the universal multiplier and Phi6 on the first-jet cone, respecting U(2) invariance and weighted homogeneity. Explain why F0,F1,F2 can each change sign, identify plausible invariant generators and dimensionless ratios, and propose exact symbolic/numerical experiments that could recover the formula without assuming the earlier false positivity. Also assess whether compact negative Einstein almost-Kahler geometry supplies any known pointwise/global control of the torsion-derivative-to-lambda ratio that could make this finite-order law globally useful.

## Output

# 科学核验备忘：六阶标量泛函的几何来源、\(U(2)\) 不变量与整体意义

## 1. 目前数据真正确定的内容

`universal_pi.json` 给出四个不同一阶挠率射线上的乘子方向，其两两余弦在 \(10^{-15}\) 内等于 \(1\)，缩放实验满足
\[
\Phi _6(\mu ^2K,\mu ^2\lambda)=\mu ^8\Phi _6(K,\lambda)
\]
至 \(1.6\times10^{-12}\)。这里 \(K=\nabla T(p)\), 等价于 \(\nabla ^2\Omega(p)\)，矩阵坐标为 \((c,S,A)\)。

`lambda_scan_a.json` 在两个固定 \(K\) 上数值支持
\[
\Phi _6(K,\lambda)=F_0(K)+\lambda F_1(K)+\lambda ^2F_2(K).
\]
在 \(|\lambda|\le20\) 的数据中，二次拟合余差约为 \(10^{-7}\) 或更小；\(\lambda=0,\pm1\) 三点已经直接给出相同系数。例如 jet 0：
\[
F_0=0.82201828,\qquad F_1=-0.02105189,\qquad F_2=-0.001160188.
\]

三个重构点的独立复算文件 `verify_A02_step80_reconstructions.json` 确认：

- 锥关系余差为 \(10^{-16}\)；
- \(\Phi _6\) 与保存值一致；
- 保存的 \(z\) 使标量方程达到 \(10^{-15}\) 量级；
- 全部 Einstein Taylor 余差至六次齐次项分别约为
  \[
  6.2\times10^{-8},\quad 1.25\times10^{-7},\quad 7.7\times10^{-9};
  \]
- 正号对照点保留 \(4.64\) 的六阶余差。

因此，六阶不存在统一的正号排除机制。特别地，\(\lambda=0\) 的 gen2 和 \(\lambda=-5\) 的 gen2、gen5 都位于可解侧，并且受限 Hessian 的最小特征值分别约为
\[
6.8\times10^{-2},\quad 5.4\times10^{-3},\quad 4.7\times10^{-3}.
\]
这些严格不等式及 \(\Phi _6<0\) 给出相邻一阶射线上的开放可解集。

不过，这只是六阶截断解。它说明“六阶必然排除非退化零点”不成立，但不否定“无限阶形式解不存在”这一命题。保存解还具有
\[
\|H_8\|\sim 5.8\times10^5\text{--}10^7,
\]
所以当前绝对余差来自很大的项之间的抵消；高精度或精确算术仍有实质价值。

另有两个文件层面的差异值得澄清：

1. 同一 lsA jet、\(\lambda=-40\) 在 `lambda_scan_a.json` 中记录 `quad_rank=12`、最小特征值 \(2.45\times10^{-4}\)，而 Step-80 重构叙述给出 rank 13 和约 \(7\times10^{-15}\)。极端 \(\lambda\) 点不宜用于精确公式恢复，直至两个活动空间的定义完全对齐。
2. 文本称奇数阶余差由奇偶性消失，而保存数组中 \(E_3,E_5\) 约为 \(10^{-11}\)–\(10^{-10}\)，且 \(H_5,H_7\) 约为 \(10^{-8}\)–\(10^{-6}\)。这与理想奇偶分支相容，但不是保存浮点数组中的恒等零。

---

## 2. 普适乘子的最可能坐标自由解释

令
\[
\mathscr E=\operatorname{Ric}-\lambda g.
\]
六次齐次 \(\mathscr E_6\) 经过二阶标量微分后成为四次齐次标量多项式，其维数正好是
\[
\dim\operatorname{Sym}^4(\mathbb R^4)^*=\binom73=35.
\]
这与重构中出现的 35 个标量行、其中 34 行被高阶自由参数吸收而剩下一行完全吻合。它强烈支持以下解释：

> 普适乘子 \(\ell\) 是某个二阶标量 Einstein 微分后果的四次 Laplace 收缩，而不是偶然出现的 840 维数值向量。

在平坦背景及固定 \(J\) 下，任意 \(U(2)\)-不变的二阶主符号至多具有形式
\[
\sigma _2(\mathcal P)(\xi)\mathscr E
=
a|\xi|^2\operatorname{tr}\mathscr E
+b\,\mathscr E(\xi,\xi)
+c\,\mathscr E(J\xi,J\xi)
+d\,\mathscr E(\xi,J\xi).
\tag{2.1}
\]
因此一个尖锐且可直接检验的乘子公式是
\[
\boxed{
\ell(\mathscr E_6)
=C\,[\Delta^2\mathcal P_0(\mathscr E_6)]_p ,
}
\tag{2.2}
\]
其中 \(\mathcal P_0\) 的主符号为 (2.1)，低阶曲率项不影响平坦六阶行。

几何上最自然的来源是 Step-65 的精确标量方程
\[
\begin{aligned}
\mathcal C(g,J):={}&
\Delta q-8\operatorname{tr}V^2+24|\eta|^2
+\frac{3s}{2}q+\frac94q^2\\
&-16\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle .
\end{aligned}
\tag{2.3}
\]
对 Einstein 度量，\(\mathcal C=0\)。对一般 almost-Kähler 度量，Weyl 粗 Laplace 方程会多出由 Cotton 张量、\(\nabla\operatorname{Ric}_0\) 和 \(\nabla s\) 产生的项；于是应有
\[
\mathcal C(g,J)
=
\mathcal P_g(\mathscr E)+
\text{含 }\mathscr E,\nabla\mathscr E\text{ 的低阶项}.
\tag{2.4}
\]
(2.4) 的平坦主部正是 (2.1) 型。零阶 Taylor 系数给出 Step-62 锥；继续展开并消去较高挠率导数，则自然产生六阶的单个标量兼容式。这也解释了为什么乘子不依赖具体的一阶射线。

这一解释可通过 `ell_ref_a.npy` 精确识别：将 (2.2) 的四个候选行按保存的单项式阶序展开，再把 \(\ell\) 投影到其张成空间。若投影余差在高精度下为零，随后可用有理重构得到 \(a:b:c:d\)。

---

## 3. 一阶挠率锥的 \(U(2)\) 商及自然不变量

在标准复标架中写
\[
f(z,\bar z)=cz+(S+A)\bar z,\qquad A=a\varepsilon,\qquad
\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
由 Step-62 的曲率字典，\(c\) 对应 \(\eta\)，\(a\) 对应 \(W_3^+\) 的复系数，\(S\) 是在点曲率中不可见的六维分量。

若 \(\chi=\det U\)，自然的标架变换律为
\[
c\longmapsto \chi c,\qquad
S\longmapsto \chi\,USU^T,\qquad
a\longmapsto \chi^2a.
\tag{3.1}
\]
若代码采用共轭的行列式线，(3.1) 全部共轭；下述实不变量结构不变。

设
\[
u=|c|^2,\qquad v=\|S\|^2,\qquad w=|a|^2.
\]
由于 \(\|A\|^2=2|a|^2\)，一阶锥为
\[
2w=v+8u.
\tag{3.2}
\]
除三个二次范数外，最低次的自然不变量为
\[
P=c^2\bar a,\qquad
D=|\det S|^2,\qquad
Q=a^2\overline{\det S}.
\tag{3.3}
\]
其中 \(P\) 是复三次不变量，\(D\) 是实四次不变量，\(Q\) 是复四次不变量，并满足
\[
|P|^2=u^2w,\qquad |Q|^2=w^2D.
\tag{3.4}
\]

维数也完全匹配：

- \((c,S,a)\) 有 10 个实参数；
- 锥 (3.2) 后有 9 个；
- 除去一般的 \(U(2)\) 轨道后有 5 个；
- 再除去整体缩放后恰有 4 个无量纲形状参数。

可以取
\[
\frac{u}{R^2},\qquad
\frac{D}{R^4},\qquad
\frac{P}{R^3},\qquad
\frac{Q}{R^4},
\tag{3.5}
\]
并用 (3.4) 去掉两个实自由度。这里
\[
R^2:=\mathrm{tn}^2
=4u+2v+2\|A\|^2
=20u+4v,
\tag{3.6}
\]
且 Step-62 的范数关系给出
\[
|\nabla^2\Omega|^2=4R^2.
\tag{3.7}
\]

这一维数计算解释了早先抽样为何容易产生单一符号印象：表中的 “\(c^2\)-fraction” 只描述四个形状变量中的一个。

### 一个重要的缩放修正

由于
\[
K\mapsto \mu^2K,\qquad \lambda\mapsto\mu^2\lambda,
\]
有 \(R\mapsto\mu^2R\)。所以真正无量纲的曲率比是
\[
\boxed{
\Lambda=\frac{\lambda}{R}
=\frac{\lambda}{\sqrt{\mathrm{tn}^2}}
=\frac{2\lambda}{|\nabla^2\Omega|}.
}
\tag{3.8}
\]
若 `tn²` 按 (3.6) 表示平方范数，则 \(\lambda/\mathrm{tn}^2\) 不是尺度不变量。所有保存案例都归一化为 \(\mathrm{tn}^2=1\)，故这一记号差异在数值表中没有显现。

---

## 4. \(\Phi _6\) 的不变量形式

加权齐次性要求
\[
\boxed{
\Phi _6(K,\lambda)
=
R^4\phi_0(X)
+\lambda R^3\phi_1(X)
+\lambda^2R^2\phi_2(X),
}
\tag{4.1}
\]
其中 \(X\) 表示 (3.5) 的四个无量纲轨道参数。

### 4.1 最小多项式模型

若消元后的 \(\Phi _6\) 本身仍是 \((c,S,a)\) 的多项式，则不变量理论把形式压缩为
\[
\begin{aligned}
F_2&=\alpha u+\beta v,\\
F_1&=2\operatorname{Re}(\gamma P),\\
F_0&=
A u^2+Buv+Cv^2
+D_0D+2\operatorname{Re}(E_0Q),
\end{aligned}
\tag{4.2}
\]
其中已使用锥关系消去 \(w\)。

这个模型立即说明三个系数为何都无需定号：

- \(F_1\) 由 \(P=c^2\bar a\) 的相位控制；表中 small-\(c\) 射线的 \(F_1\approx0\) 与此高度一致。
- \(F_0\) 包含 \(Q=a^2\overline{\det S}\) 的相位和 \(D\) 所描述的 \(S\) 奇异值不均匀性；锥关系没有固定这些量。
- \(F_2\) 是两个二次模长的线性组合，系数异号时可跨零。

### 4.2 现有数据更像 Schur 补形式

重构中的实际定义是
\[
q(z)=\frac12z^THz+j^Tz+c,\qquad
\Phi _6=c-\frac12j^TH^{-1}j.
\tag{4.3}
\]
即使原始 Taylor 方程是多项式，\(H^{-1}\) 也会使约化后的 \(\Phi _6\) 成为轨道不变量的有理函数。于是更一般的形式是
\[
F_k=R^{4-k}f_k(X),\qquad k=0,1,2,
\tag{4.4}
\]
其中 \(f_k\) 在固定秩层上为实有理函数。

F012 表已经提示 (4.2) 可能过窄：多个 small-\(c\) 点有几乎相同的 \(u/R^2\)，但 \(F_2\) 从约 \(1.1\times10^{-3}\) 变化到 \(3.6\times10^{-3}\)；gen2 与 gen7 的标示 \(c\)-比例也相近，而 \(F_2\) 符号不同。这种形状依赖可由 \(D/R^4,P/R^3,Q/R^4\) 进入 (4.4)。

### 4.3 符号变化的直接数据

在固定乘子方向、并以活动 Hessian 正定来定向后：

- \(F_0\)：gen2 为 \(-0.165\)，其余多个点为正；
- \(F_1\)：gen0 为 \(-0.034\)，gen1 为 \(+0.134\)；
- \(F_2\)：gen2 和 small-\(c\) 点为正，gen0、gen3–gen7 多为负。

这些变化不是 λ 多项式拟合误差能够解释的；典型 \(F_2\) 大小约 \(10^{-3}\)，而拟合余差对应的系数误差远小于此量级。

乘子本身可整体乘以 \(-1\)，所以单独说“正”或“负”需要固定定向；“同一连通秩层上出现两种符号”不受这一整体翻转影响。

---

## 5. \(\Phi _6\le0\) 的适用形式

在活动空间上若 \(H\) 正定，则
\[
q(z)=0\quad\Longleftrightarrow\quad \Phi _6\le0.
\tag{5.1}
\]
三个实际重构点满足这一情形。

但原始的全 \(H_4\) 二次型有 99 个正特征方向和 84 个反向特征方向；正定性来自一阶方程选择出的 12 维活动子空间。若该子空间随 \(K,\lambda\) 变化而使 \(H\) 成为不定型，则 \(q(z)\) 通常取遍实数，不再由 (5.1) 描述；若出现零特征方向，还需同时考察 \(j\) 在核上的分量。

因此完整的六阶不变量对象不是单独一个 \(\Phi _6\)，而是
\[
\bigl(\operatorname{inertia}H,\ \Phi _6\bigr).
\tag{5.2}
\]
在当前三个严格正定点附近，\(\Phi _6<0\) 的开放可解结论稳定。要把整个严格锥写成统一的 \(\{\Phi _6\le0\}\) 区域，还需要活动 Hessian 惯性在全商空间上的映射。

---

## 6. 恢复精确公式的实验设计

### 6.1 识别普适乘子

1. 按保存的单项式及阶乘约定，构造
   \[
   \Delta^3\operatorname{tr}\mathscr E,\quad
   \Delta^2\nabla^i\nabla^j\mathscr E_{ij},\quad
   \Delta^2\nabla^{Ji}\nabla^{Jj}\mathscr E_{ij},\quad
   \Delta^2\nabla^{Ji}\nabla^j\mathscr E_{ij}.
   \]
2. 将四个行向量与 `ell_ref_a.npy` 作 200 位投影。
3. 对拟合系数使用 PSLQ 或有理重构。
4. 精确验证 \(\ell L_6=0\)。
5. 以 \(\mathfrak u(2)\) 的四个无穷小生成元作用于 \(\ell\)，验证其固定性；再用 Haar-\(U(2)\) 变换同一射线，确认乘子、Hessian 惯性及归一化 \(\Phi _6/R^4\) 不变。

### 6.2 从 Weyl 方程直接推出乘子

对一般 almost-Kähler Taylor 度量计算 (2.3)，不要先代入 Einstein 方程。利用
\[
\delta W^+=\text{Cotton}(\operatorname{Ric},s)
\]
把所有非 Einstein 项写成 \(\mathscr E,\nabla\mathscr E,\nabla^2\mathscr E\)。提取平坦二阶主符号并与 (2.1) 比较。这会同时给出乘子的坐标自由含义及精确系数。

### 6.3 精确恢复 \(F_0,F_1,F_2\)

锥
\[
\|A\|^2-\|S\|^2-8|c|^2=0
\]
是有理二次曲面，可从一个有理基点作直线参数化，生成严格且完全精确的有理射线。对每个射线：

\[
F_0=\Phi(0),\qquad
F_1=\frac{\Phi(1)-\Phi(-1)}2,\qquad
F_2=\frac{\Phi(1)+\Phi(-1)-2\Phi(0)}2.
\tag{6.1}
\]

所有矩阵消元可在多个大素数域中完成，再用 CRT 与有理重构恢复结果。正定性可用精确 \(LDL^T\) 分解确定。

先拟合有限模型 (4.2)。若精确余差不为零，则保存 \(H,j,c\)，使用
\[
\Phi _6=
\frac{2c\det H-j^T\operatorname{adj}(H)j}{2\det H}
\tag{6.2}
\]
并把分子、分母分别插值为
\[
u,v,D,P,\bar P,Q,\bar Q
\]
的多项式。先按 \(U(2)\) 不可约分量分块 \(H\)，可显著降低 \(\det H\) 的复杂度。

### 6.4 相位扫描

取近似 Takagi 标架
\[
S=\operatorname{diag}(s_1,s_2),\quad
c=|c|e^{i\alpha},\quad
a=|a|e^{i\beta},
\]
并由锥固定 \(|a|\)。固定 \(u/R^2\) 和 \(D/R^4\)，扫描 \((\alpha,\beta)\)。

多项式模型预言：

- \(F_1\) 只含 \(2\alpha-\beta\) 的一阶正弦、余弦；
- \(F_0\) 的相位部分只含 \(2\beta-\arg\det S\)；
- \(F_2\) 与相位无关。

任何额外 Fourier 模式都会直接显示 Schur 补中的有理轨道依赖。

### 6.5 高精度重构

当前 \(H_8\) 达到 \(10^7\)，应以 100–300 位算术重算三个可解点，并对每个阶次报告：

- 绝对余差；
- 相对于最大单项的反向误差；
- 线性求解的条件数；
- 活动 Hessian 的全部特征值；
- 用区间算术包住的 \(\Phi _6\) 与残差。

这可以把现有浮点证据转化为精确六阶代数解，或至少得到严格符号区间。

---

## 7. 紧致 \(\lambda<0\) 几何是否控制 \(\lambda/R\)

Step-62 的点态关系在非退化零点给出
\[
|\eta|^2=4u,\qquad
\operatorname{tr}V^2=4\|A\|^2=4v+32u.
\]
结合 (3.6)，有
\[
R^2=4v+20u.
\]
另一方面
\[
|W^+|^2-\frac{s^2}{24}
=2|\eta|^2+\operatorname{tr}V^2
=4v+40u.
\]
所以得到很有用的坐标自由比较：
\[
\boxed{
R^2\le
|W^+|^2-\frac{s^2}{24}
\le 2R^2 .
}
\tag{7.1}
\]
因此六阶中的真正参数
\[
\Lambda=\frac{\lambda}{R}
\]
等价于比较 Einstein 尺度与零点处 \(W^+\) 偏离 Kähler 型谱的幅度。

现有点态方程并未把这个比值固定：

- 零点恒等式
  \[
  |\nabla^2\Omega|^2=4\operatorname{tr}V^2-12|\eta|^2
  \]
  中所有 \(\lambda\) 项抵消；
- 一阶锥同样与 \(\lambda\) 无关；
- 非退化零点的局部指数恒为 \(+1\)，但指数不记录 \(|\nabla^2\Omega|\) 的大小；
- 总零点数 \(5\chi+6\tau\) 只提供计数信息，不控制四个轨道形状参数或 \(\Lambda\)。

闭 Einstein 四流形的 Chern–Gauss–Bonnet 与签名公式控制
\[
\int |W^\pm|^2\,dV
\]
以及 \(\lambda^2\operatorname{Vol}\)，但离散零点上的 \(R\) 不由这些 \(L^2\) 数据直接决定。Step-65 标量方程积分后还保留
\[
16\int\sum_i
\langle(\nabla_iW^+)\nabla_i u,u\rangle,
\]
其符号未被当前恒等式固定，也没有给出零点处的逐点估计。

由此，紧致性和 \(\lambda<0\) 本身目前没有提供统一的
\[
0<c\le \frac{R}{|\lambda|}\le C
\]
型估计。若另有点态 Weyl pinching、非塌缩加曲率正则性，或零点的一致横截性，则 (7.1) 可把这些条件转化为 \(\Lambda\) 的区间；但现有拓扑计数和整体曲率积分还做不到这一点。

所以六阶定律当前最直接的整体用途是：每个非退化零点都必须落入某个允许的 \(U(2)\) 轨道子集
\[
\bigl\{X,\Lambda:\text{标量二次方程可解}\bigr\}.
\]
要从这点推出闭流形结论，还需要一个把各零点的 \(X\) 或 \(\Lambda\) 汇总起来的局部化公式，或一个把 \(R\) 与 \(|\lambda|\) 逐点联系起来的几何估计。现有零点数与指标公式尚未携带这些权重。
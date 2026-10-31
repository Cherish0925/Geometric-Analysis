# 四题续研：共形 Kähler 分离、具体极小化对象与 Darboux 主符号

2026年10月8日。底本为用户本次上传的 `01_Research_Synthesis(1).tex` 与 `02_Mathematical_Source_Companion(1).tex`。采用主稿列出的四题及其最新修正：Q1 非极小一般型曲面的 Einstein 存在性；Q2 无迹 Ricci／全曲率下确界；Q3 光滑非 Bach-flat 全局极小元；Q4 四维负标量 Goldberg。

本次完整推导见 `Four_Problems_Direct_Connections.tex`，阅读本为同名 PDF。该文件独立编译，无外部 TeX 或图像依赖。`check_symbol_and_channel.py` 提供有限代数与齐次最高阶块计算。

## 1. 本次实际取得的连接

本轮没有完成四题中任一题的一般解答。以下结果分别是经典恒等式与新稿上界的组合、一个明确的 Q3 候选、经典可行区域的精确反解，以及原稿 Darboux 兼容式的完整主符号计算。一般背景 Burns 的负对数构造属于系统已经完成的输入，不重新计为本轮成果。

### 1.1 从固定复结构比较扩大到整个全局共形 Kähler 类

统一记

\[
P=\int|\mathrm{Ric}^{\circ}|^2,\quad S=\int s^2,\quad
W_\pm=\int|W^\pm|^2,\quad T_\pm=2\chi\pm3\tau.
\]

设流形上已有全度量标量预算 \(S(g)\ge32\pi^2A\)。若 \(g=u^2h\)，其中 \(u>0\) 光滑、\(h\) 是某个任意复结构的光滑 Kähler 度量，诱导取向为 \(\epsilon\)，则

\[
\boxed{
P(g)-8\pi^2(A-T_\epsilon)
=\frac{S(g)-32\pi^2A}{12}
 +\frac{S(h)-32\pi^2A}{6}\ge0.}
\]

证明仅用四维 Weyl 能量的共形不变性、Kähler 恒等式 \(W_\epsilon(h)=S(h)/24\) 及
\(P=S/12+4W_\epsilon-8\pi^2T_\epsilon\)。因此，对
\(M=X\#k\overline{\mathbb{CP}}^2\)，原取向的整个全局共形 Kähler 类都满足 \(P\ge8\pi^2k\)，不固定复结构，也不固定共形因子。若 \(\tau(M)\ge0\)，另一取向同样受此下界约束。

用户新稿已经给出实际竞争者 \(P<8\pi^2k\)。故它的真正极小化序列最终离开上述整个几何类别；若存在光滑全局极小元，该极小元也不能位于此类别。对 \(P(g)\le8\pi^2k-\delta\)，还有

\[
W_+(g)\le\frac{4\pi^2A}{3}-\frac\delta4,
\qquad W_+(h)\ge\frac{4\pi^2A}{3}
\]

对所有原取向的全局共形 Kähler \(h\) 成立。这是 Weyl 能量的分离，不是未经定义的度量空间距离。

只假设局部共形 Kähler、允许共形因子奇异、或者仅有任意 Hermitian 结构，不满足本命题的输入。

### 1.2 为 Q3 选择一个已经排除 Einstein 的具体对象

可取经典的光滑 Horikawa 曲面

\[
X=\{w^2+z^5+x^{10}+y^{10}=0\}\subset\mathbb P(1,1,2,5),
\qquad M=X\#\overline{\mathbb{CP}}^2.
\]

四坐标的权依次为 \(1,1,2,5\)。仿射锥的偏导只在原点同时为零，曲面避开环境的两个奇点；故 \(X\) 光滑。加权伴随公式给 \(K_X=\mathcal O_X(1)\) ample，且

\[
K_X^2=1,\quad p_g=2,\quad q=0,\quad
\chi(X)=35,\quad\tau(X)=-23.
\]

从而

\[
\chi(M)=36,\quad\tau(M)=-24,\quad T_+(M)=0.
\]

这些曲面的存在与加权超曲面描述是经典输入。对该单吹起，全单极子符号供给的投影预算为 \(p_{\rm SW}\ge A=1\)。经典 \(D_8\ge0\) 给

\[
0\le D_8=\frac{27}{2}P-72\pi^2p_{\rm SW},
\qquad P\ge\frac{16\pi^2}{3}.
\]

系统新的一般负 KE Burns 构造则给严格上界。合并得

\[
\boxed{\frac{16\pi^2}{3}\le p_*(M)<8\pi^2.}
\]

因此，这个具体 \(M\) 的 Einstein 非存在性已经确定，并且 Yamabe 不变量为负。任意光滑闭 \(P\)-临界元的标量曲率为常数；以总 Weyl 能量的 \(L^2\) 梯度 \(\mathfrak B\) 归一化 Bach 张量，有

\[
\mathfrak B=\frac{s}{12}\mathrm{Ric}^{\circ}.
\]

故只要 \(p_*(M)\) 在这个 \(M\) 上由光滑度量取得，该极小元必定非 Bach-flat。这样，第3题的这一尝试不再依赖第1题未知的小吹起 Einstein 非存在性。

尚未得到的是光滑取得性。标准 Burns 气泡在适用的能量相加情形下已因 \(p_*<8\pi^2\) 被排除，但较便宜的 ALE、Ricci-flat 气泡及部分塌缩仍须处理。这里没有将轨形极小元写成原光滑流形上的极小元。

## 2. Q1：把 Einstein 竞争者需要达到的 Weyl 区域精确写出

沿用新稿的共形类变量

\[
\kappa=\frac A2-\frac{3W_+}{8\pi^2},\quad
\upsilon=\frac{S}{32\pi^2}-A,\quad p=\frac{P}{8\pi^2},
\]

注意这里的 \(\kappa\) 不是 O10 的参数缺陷。已知

\[
p=k-\frac43\kappa+\frac13\upsilon,
\qquad2\sqrt{A+\upsilon}+\sqrt{A-2\kappa}\ge3\sqrt A.
\]

令 \(\ell=k-p\)，\(0<\ell<A/3\)。精确解上述经典可行区域的较小边界得

\[
\boxed{
\kappa\ge r_-(\ell)
=\ell+\frac{\ell^2}{A(1+\sqrt{1-3\ell/A})^2}.}
\]

因而在 \(0<k<A/3\) 中，任何 Einstein 候选必须满足

\[
\kappa\ge r_-(k)>k.
\]

这是经典包络的反解，不是新的一般下界。它使 Q1 的一个可能终点更精确：只需在**精确 Einstein 候选**上证明 \(\kappa<r_-(k)\)，不必先对所有度量证明更强的 \(\kappa\le k\)。本次未证明这一 Einstein 专属上界。

形式数据 \(p=0,\kappa=2k,\upsilon=5k\) 在 \(0<k/A\le1/4\) 时仍通过以上经典约束。它不是度量，但说明不能仅靠反解旧预算排除全部 Einstein 候选。

## 3. Q4：完整主符号、Hamiltonian 自由度与可复现的齐次块

固定四维 Hermitian 向量空间，Darboux 相容变分满足

\[
H^T=H,\qquad HJ+JH=0.
\]

源稿规范的 Ricci 主符号为

\[
S_\xi(H)=\tfrac12\{\xi\otimes H\xi+H\xi\otimes\xi-|\xi|^2H\}.
\]

本次完整求出

\[
\ker S_\xi=\mathbb R(\xi\otimes J\xi+J\xi\otimes\xi),
\]

\[
\operatorname{im}S_\xi=
\{K:K\xi-\tfrac12(\operatorname{tr}K)\xi=0,\quad
K(J\xi,J\xi)-\tfrac12|\xi|^2\operatorname{tr}K=0\}.
\]

即四条 Bianchi 关系与原稿补回的一条 Darboux 关系，在固定非零实协向量处完整描述了值域。秩为5，唯一核是 Hamiltonian 规范自由度。进一步有锐常数估计

\[
\boxed{|S_\xi(H)|^2+\tfrac14|H(\xi,J\xi)|^2
\ge\tfrac18|\xi|^4|H|^2.}
\]

取 \(\xi=e_1,Je_1=e_2,Je_3=e_4\)，写

\[
H=\begin{pmatrix}
a&b&c&d\\b&-a&d&-c\\c&d&e&f\\d&-c&f&-e
\end{pmatrix},
\quad
S_{e_1}H=\frac12\begin{pmatrix}
a&0&0&0\\0&a&-d&c\\0&-d&-e&-f\\0&c&-f&e
\end{pmatrix}.
\]

取 \(b=0\) 即得显式右逆，范数不超过 \(\sqrt8\)。相容度量可用 \(G=\exp H\) 表示，自动保持正定、\(\det G=1\) 及 \(GJ_0G=J_0\)。因此不用把这些代数约束再次作为带罚系数的非线性残差。

脚本对齐次最高阶块在两个有限域作了计算：

| 度数 | 矩阵大小 | 两个模素数秩 | 扣除 Hamiltonian 维数后的计数 |
|---|---:|---:|---:|
| 4 | 100×210 | 83 | 43 |
| 5 | 200×336 | 156 | 60 |
| 6 | 350×504 | 260 | 79 |
| 7 | 560×720 | 400 | 100 |

它们符合系统已经修正的 \(N^2+8N-5\) 计数。最高的这个整数矩阵占 3,225,600 bytes。这里计算的是已知最高阶线性块，而非原来超过内存的完整非线性 jet 系统；两者不作同一计算的速度比较。

新的计算顺序是：先固定真实代数参数与 Hamiltonian 规范；逐次数组装最高阶线性块；把低阶产生的非线性右端投影到值域及其余核，真正新增的相容性必须从余核分量中出现。固定协向量的符号结论并不自动决定非线性系统的所有延拓。

本轮未证明负标量情况下的全阶形式可积性、解析收敛或闭流形上的 \(\nabla\omega=0\)。曲率符号不出现在这个主符号中；必须在低阶完整相容性或全局方程里区分负 Einstein 与控制例。

## 4. 对系统的直接接入

- Q1：小 \(k/A\) 的全部 Einstein 排除仍是目标；使用精确 Einstein 特有关系，而不是把 Q2 的全度量最优值作为前置。
- Q2：系统已建立的 \(p_*<8\pi^2k\) 进入本文的整共形 Kähler 分离。继续求匹配的非 Kähler 全局下界，不返回已被阈值排除的共形类别。
- Q3：可选用本文件的具体 Horikawa 单吹起，将未知环节集中到光滑取得性。其 Einstein 排除、负 Yamabe 与严格上界都有明确来源。
- Q4：先使用完整符号与规范消除重复自由度，再计算真正的非线性相容性。不得把修正后的正维数计数当作严格 almost-Kähler 解的存在证明。

## 5. 直接文献与文件来源

1. 本次两份用户稿件。一般背景负对数、主符号额外关系与正确计数均来自系统原稿；本文只补出所写的连接与完整线性代数。
2. C. LeBrun, *Ricci curvature, minimal volumes, and Seiberg–Witten theory*, Invent. Math. 145 (2001), 279–316. https://arxiv.org/abs/math/0003068
3. S. Coughlan and R. Pignatelli, *Simple fibrations in (1,2)-surfaces*, Forum of Mathematics, Sigma (2023). https://doi.org/10.1017/fms.2023.41
4. M. J. Gursky and J. A. Viaclovsky, *Rigidity and stability of Einstein metrics for quadratic curvature functionals*, arXiv:1105.4648v2. https://arxiv.org/abs/1105.4648
5. M. T. Anderson, *Canonical metrics on 3-manifolds and 4-manifolds*, Asian J. Math. 10 (2006), 127–163. https://arxiv.org/abs/math/0511034
6. V. Apostolov and T. Drăghici, *The curvature and the integrability of almost-Kähler manifolds: a survey*. https://arxiv.org/abs/math/0302152
7. V. Apostolov, J. Armstrong and T. Drăghici, *Local models and integrability of certain almost Kähler 4-manifolds*. https://arxiv.org/abs/math/0109098

运行有限计算：`python check_symbol_and_channel.py --jets 7`。所需 Python 库为 SymPy 与 NumPy；输出保存为 `exact_check_results.json`。脚本的任务是有限代数与最高阶块，不承担源稿的 Burns 拼接证明或极小值取得性。

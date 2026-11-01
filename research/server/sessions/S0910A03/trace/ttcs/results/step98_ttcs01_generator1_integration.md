# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 98,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step98_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step98_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Given the exact charged Koiso center data and Step 98's full SPD logarithmic-matrix finite-domain formulation, develop a mathematically serious next construction/obstruction experiment that can distinguish genuine two-ended matching from low-resolution overfitting. Work directly with the supplied equations and artifacts. Seek a representation that preserves the full center q,K and both attachments, allows resolution continuation, and exposes residual projections versus inverse scales. Specify a small number of decisive computations, exact variables/boundary conditions, and what numerical scaling would reveal. Do not treat the cosh exterior as solving the inner transition and do not assume a gauge change cures elliptic Cauchy ill-posedness.

## Integrated Scientific Memo

## 下一步实验：精确喷流约束的双端 SPD 配置空间与尺度归一化余核检验

现有 Step 98 的下降不能解释为双端匹配。它至少混合了三个不同对象：

1. `ns=16` 时中心残差 \(1.3634185\) 几乎完全等于 Fourier–Codazzi 离散误差；分辨率表显示该量在 \(N_s=128\) 降至 \(6.76\times10^{-6}\)。
2. 直接节点脚本只固定 \(X\) 的端点值，随后在残差中手工覆盖 \(q_n,q_{nn}\)。因此优化所得多项式度量一般不具有所声称的端点一、二阶喷流，端点残差行也不是该离散度量的真实 Ricci 张量。
3. 外端 \(q=e^{2r}q_0(s)\) 本身不是 Einstein，除非 \(q_0\) 平坦。其端点缺陷是
   \[
   E_{rr}=E_{ri}=0,\qquad E_{ij}=\operatorname{Ric}(q_0)_{ij},
   \]
   因而正交标架中的精确地板为
   \[
   \delta_{\rm inh}(R)
   =e^{-2R}\left\|q_0^{-1/2}\operatorname{Ric}(q_0)q_0^{-1/2}\right\|_{\rm op}.
   \]
   \(R=1\) 数据中的 \(1.07419\) 正是这种外端模型缺陷，而非内层障碍。

所以真正有判别力的下一步应同时做到：精确保留中心 \((q_0,K_0)\)、精确保留两个附件的真实喷流、可在 \(N\) 与 \(R\) 上延拓，并把残差投影与物理逆尺度联系起来。

---

### 1. 单一有符号柱面上的精确喷流表示

取
\[
n\in[-R_-,R_+],\qquad
g=dn^2+q(n,s),\qquad
q=S_0(s)e^{X(n,s)}S_0(s),
\]
其中
\[
S_0=q_0^{1/2},\qquad
A=S_0^{-1}K_0S_0^{-1},\qquad
B=S_0^{-1}\operatorname{Ric}(q_0)S_0^{-1}+3I.
\]

中心统一使用有符号法向，施加
\[
X(0)=0,\qquad X_n(0)=2A,\qquad X_{nn}(0)=2B. \tag{1}
\]
于是
\[
q(0)=q_0,\qquad q_n(0)=2K_0,
\]
且
\[
q_{nn}(0)=
2\!\left(\operatorname{Ric}(q_0)+3q_0+
2K_0q_0^{-1}K_0\right). \tag{2}
\]
结合精确 Hamiltonian、Codazzi 约束，中心十个 Einstein 残差解析地为零；不能再由端点行覆盖来“实现”。

若暂时保留 Step 98 的 inherited 附件，则
\[
\begin{aligned}
X(R_+)&=2R_+I,&X_n(R_+)&=2I,&X_{nn}(R_+)&=0,\\
X(-R_-)&=2R_-I,&X_n(-R_-)&=-2I,&X_{nn}(-R_-)&=0.
\end{aligned} \tag{3}
\]
但该族必须明确扣除上述 \(e^{-2R}\) 外端地板。

更干净的对照族取两个常值平坦三环面度量 \(\bar q_\pm\)，令
\[
L_\pm(s)=\log\!\bigl(S_0^{-1}\bar q_\pm S_0^{-1}\bigr),
\]
并把端点值改为
\[
X(R_+)=2R_+I+L_+,\qquad
X(-R_-)=2R_-I+L_-, \tag{4}
\]
仍使用 (3) 的一、二阶导数。这样外部可固定为
\[
q=e^{2n}\bar q_+\quad(n\ge R_+),\qquad
q=e^{-2n}\bar q_-\quad(n\le-R_-),
\]
它们确实满足 \(\operatorname{Ric}=-3g\)。附件最好占据一个固定宽度的开放谱元，而非仅一个端点。

令 \(H_R(n,s)\) 为逐分量满足 \(-R_-,0,R_+\) 三点各三阶条件的八次 Hermite 插值，设置
\[
X=H_R+w_RY,\qquad
w_R=n^3(n+R_-)^3(R_+-n)^3, \tag{5}
\]
缩放 \(w_R\) 以改善条件数。展开
\[
Y=\sum_{k,m}Y_{km}B_k(n)e^{ims},\qquad
Y_{km}\in\operatorname{Sym}(3),\quad
Y_{k,-m}=\overline{Y_{km}}. \tag{6}
\]
这在每个分辨率上严格保持中心和双端全部喷流。长柱面应使用固定物理单元宽度的高阶谱元或 \(C^2\) B-spline；否则增大 \(R\) 会同时降低径向物理分辨率。

矩阵指数应在接受的状态上使用真实 \(e^X\)。当前代码的特征值裁剪会改变配置映射及其 Jacobian，只可作为拒绝非法试探点的保护，不能进入最终残差或线性谱。

---

### 2. 计算一：固定 \(R\) 的网格外连续性检验

最小化完整几何量
\[
\mathcal J_2(X)=
\int_{\Omega_R}|E^{\rm orth}(X)|_F^2\,d\mu_g,
\qquad E=\operatorname{Ric}_g+3g, \tag{7}
\]
同时报告
\[
\delta_\infty(X)=
\sup_{\Omega_R}\|E^{\rm orth}(X)\|_{\rm op}. \tag{8}
\]
不能排除端点，也不能覆盖导数。为防止 \(L^2\) 隐藏窄峰，可继续计算 \(L^p\), \(p=4,8,16\)。

每个优化解必须在三处重新评估：

* 优化网格；
* 径向和 Fourier 均加密 \(2\)–\(3\) 倍的独立网格；
* 加密网格上各残差块 \(E_{nn},E_{ns},E_{ij}\) 的模态投影。

定义物理逆尺度
\[
\kappa_{km}^2=
\left(\frac{\pi k}{R_-+R_+}\right)^2+m^2,
\]
以及壳能量
\[
\mathcal E_E(\kappa)^2
=\sum_{\kappa\le\kappa_{km}<2\kappa}
|\widehat E_{km}|^2. \tag{9}
\]

可信的固定域序列表现为：

* 优化网格与加密网格残差一致；
* 高频壳能量衰减；
* \(q_N\) 在固定紧子柱面上 \(C^2\) 收敛；
* \(\lambda_{\min}(q_N)\) 有统一正下界；
* \(\delta_\infty(N,R)\) 收敛，而不是随截止频率迁移。

若优化网格残差趋零但加密网格保持 \(O(1)\)，或峰值逆尺度满足 \(\kappa_{\rm peak}\sim\kappa_{\max}\)，即为低分辨率过拟合。

中心 Fourier 误差应独立列出，不应混入匹配残差。现有数据建议至少用
\[
N_s=48,64,96,128
\]
做延拓；只有在固定 \(R\) 上先获得 \(N_s,N_r\) 收敛后，才能解释 \(R\)-缩放。

---

### 3. 计算二：外尺度延拓，并分离三种衰减机制

取
\[
\eta=e^{-R},\qquad R_j=R_0+j\log2,
\]
径向自由度随 \(R\) 线性增长，保持固定物理分辨率。对每个 \(R_j\) 同时计算：

1. inherited 外端族 (3)；
2. exact-flat 外端族 (4)。

两族之差直接识别 inherited 外端项。前者预期有
\[
\delta_{\rm inh}=C_0\eta^2,\qquad
C_0=\|q_0^{-1/2}\operatorname{Ric}(q_0)q_0^{-1/2}\|_{\rm op}. \tag{10}
\]
后者无该项。

随后逐块拟合残差，而非只拟合总 supremum：

* inherited 曲率：\(E_{TT}\sim C_0e^{-2R}\)；
* 延迟 charge taper：
  \[
  \|E_{\rm mix}\|=O(e^{-3R}/\ell),\qquad Q=O(e^{-6R})
  \tag{11}
  \]
  在 Step 96 的归一化中；
* 宽缓过渡：\(R^{-1},R^{-2}\) 型；
* 真正水平/轨道代价：某一低频块趋向正数。

由于 Step 94 的另一径向归一化给出 \(\rho\sim e^{\sqrt6r}\)，其中混合源率为 \(e^{-3\sqrt6r/2}\)，指数必须按实际所用径向坐标和外端模型由 indicial roots 推导，不能把 \(e^{-3R}\) 与 \(e^{-3\sqrt6R/2}\) 混用。

还应记录残差峰的位置和厚度：

* 红移层：\(|n_{\rm peak}|=R-O(1)\)，物理厚度及逆尺度有界；
* 中心障碍：峰和左投影场停留在固定紧区域；
* 数值伪层：厚度随网格缩小，逆尺度追随 \(\kappa_{\max}\)。

同时比较不同 \(R\) 下 \(q_R|_{|n|\le r_*}\)。若其在每个固定 \(r_*\) 上收敛，而缺陷层向端部逃逸，这是两端近似构造的核心证据。

---

### 4. 计算三：尺度归一化 Jacobian、残差投影与余核场

在每个已通过网格外验证的 \(X_R\) 处构造真实线性化
\[
J_R=D_X(\operatorname{Ric}_{g_X}+3g_X). \tag{12}
\]
应使用自动微分或
\[
D e^X[V]=\int_0^1e^{(1-t)X}Ve^{tX}\,dt, \tag{13}
\]
而不是有限差分和裁剪指数。

原始节点 Euclidean SVD 不具网格不变性。使用质量矩阵定义
\[
\|V\|_{\mathcal X}^2
=\int\left|
q^{-1/2}Dq_X[V]q^{-1/2}
\right|_F^2d\mu_g,
\quad
\|F\|_{\mathcal Y}^2=\int|F^{\rm orth}|_F^2d\mu_g. \tag{14}
\]
求广义奇异系统
\[
J_Rv_j=\sigma_ju_j,\qquad J_R^*u_j=\sigma_jv_j. \tag{15}
\]
逐模记录
\[
\pi_j=\langle u_j,E_R\rangle_{\mathcal Y},
\qquad
a_j=\frac{|\pi_j|}{\sigma_j}, \tag{16}
\]
以及右模的物理逆尺度
\[
\kappa_j^2=
\frac{\int|\nabla(q^{-1/2}Dq[v_j]q^{-1/2})|^2d\mu_g}
{\int|q^{-1/2}Dq[v_j]q^{-1/2}|^2d\mu_g}. \tag{17}
\]
Ricci 在高频上是二阶的，故通常 \(\sigma_j\sim\kappa_j^2\)。定义
\[
\widetilde\sigma_j=\frac{\sigma_j}{1+\kappa_j^2} \tag{18}
\]
才能把几何软模与普通高频刚性区分开。

应绘制
\[
P_R(\tau)^2=
\sum_{\sigma_j\le\tau}|\pi_j|^2+
\|\Pi_{\ker J_R^*}E_R\|^2,
\quad
A_R(\tau)^2=
\sum_{\sigma_j>\tau}\frac{|\pi_j|^2}{\sigma_j^2}. \tag{19}
\]
前者表示残差在弱可控/余核方向上的质量，后者表示消除其余残差所需的一阶修正尺度。

完整输出还应把 \(u_j\) 分解到 Step 96 的
\[
(H,T,Z,\mathcal B)
\]
四块，并计算其与以下有限维匹配方向的配对：

* 两侧 vector charge flux；
* 两端 connection holonomy；
* 水平 traceless \(TT\)/Hopf 模；
* 三个 \(\mathbb H^2\) target-Killing currents；
* 共享中心参数 \(S,c,\) target phase/frame 及双端尺度/形状。

这比仅看最小奇异值更重要：障碍是稳定的左零模及其非零中心配对，而不是单纯“小 \(\sigma_{\min}\)”。

---

### 5. 决定性数值签名

在每个固定 \(R\) 先证实 \(N\)-收敛，再读 \(R\)-行为：

#### 真正的红移匹配机制
\[
\widetilde\sigma_{\min}(R)\sim e^{-\alpha R},
\qquad
\pi_{\min}(R)\to0,
\qquad
\delta_\infty(R)\to0,
\]
其中 \(\alpha\) 与外端 indicial root 一致；右奇异场位于 \(|n|=R-O(1)\)，具有有界物理 \(\kappa\)，中心紧区域上的度量收敛。两侧必须同时满足同一中心数据，而不是两个互不相关的半问题。

#### 有限维全局障碍
存在光滑低-\(\kappa\) 左场 \(u_R\)，在分辨率和 \(R\) 延拓下收敛，
\[
J_R^*u_R\to0,\qquad
\langle u_R,E_R\rangle\to c\ne0,
\]
且场不逃向端部。其块分解将指出障碍来自 charge-work、水平 \(TT\)/Hopf 或 target-current 配对，可进一步寻找积分恒等式。

#### 离散过拟合
固定 \(R\) 时 \(\sigma_{\min}\) 或残差随 \(N\) 继续下降而不收敛，奇异场高频化，\(\kappa\sim\kappa_{\max}\)，或加密网格残差保持 \(O(1)\)。

#### 模型外端污染
只有 inherited 族表现 \(e^{-2R}\)，exact-flat 族消失；这只是附件曲率，不是内层机制。

---

### 6. 关于“先求 charged radial exterior”的限制

可把保持非零坐标 charge 的径向约化 ODE 当作廉价的外端模型和 indicial-root 探针，但不能把它作为决定性二分。Koiso 中心本质上依赖 \(s\)，径向 ODE 失败只排除该径向外端子类，不能推出所有二维 \(s\)-依赖外端不存在；成功也不能完成内层连接。类似地，DeTurck/Bianchi gauge 可使适当边值问题椭圆化，但不能保证给定两端 Dirichlet 数据必有解，更不能使过定的 Einstein Cauchy 问题良定。因此 DtN 缺陷可作为辅助匹配量，但其可定义性须建立在实际边值解存在之后。

最后，\(\cosh\) 外部不能替代内层求解。即使 \(\bar q\) 平坦，
\[
g=dn^2+\cosh^2n\,\bar q
\]
仍有
\[
E_{TT}=2\bar q,\qquad
\|E_{TT}\|_{\rm op}=2\cosh^{-2}n.
\]
它至多提供衰减的非 Einstein 终端数据；所有该残差必须保留在完整张量范数中。

这组三项计算——精确喷流的固定域延拓、双终端族的 \(R\)-缩放、以及按物理逆尺度归一化的残差—余核谱——能够区分真正双端匹配、红移近核、有限全局障碍和低分辨率过拟合，而不借助正常方向演化或坐标规范上的虚假良定性。
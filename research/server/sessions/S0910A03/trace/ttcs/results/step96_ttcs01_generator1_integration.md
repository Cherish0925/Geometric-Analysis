# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 96,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step96_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step96_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop a high-value next mathematical construction from the exact charged Koiso center and the verified horizontal Noether/K_X pairing. The goal is a genuinely two-variable, shared-parameter joint matching formulation that can decide whether local Ricci flexibility extends to two expanded ends. Use the provided exact Cauchy data, quotient equations, and short Taylor/numerical evidence. Propose an explicit gauge-fixed unknown space, boundary data, residual/matching map including all Ricci blocks and two ends, and independent adjoint projections (not rearrangements of the area equation). Seek either a low-cost near-kernel analogous to log-Weyl slow interpolation or a finite projection that cannot vanish. Keep flat radial T3 models excluded; do not assume transition length or an interface. Derive as much of the linearized principal operator and dimension/index structure as possible, and specify a decisive computation/proof that could be done next.

## Integrated Scientific Memo

## 两端共享参数匹配问题：一个可执行的严格 formulation

最有价值的下一对象不是闭合轨道空间上的面积积分，也不是把 \(q\) 当作满足二阶 Maxwell 方程的独立场，而是：

> 在固定抽象两端圆柱上，同时求解全部约化 Ricci 块，以精确 charged Koiso 数据作为共享中心迹，并把两个展开端作为同一全局边值问题的两个无穷端；随后计算该全匹配映射的最小奇异值及左伴随极限。

这直接区分两种情形：存在红移近核，或存在有界、非零的有限余核投影。

### 必要纠正

1. 当前基本混合方程是
   \[
   dq_a(W)=2\rho E(JW,V_a),\qquad
   e^{-3\sigma}M^{ab}\langle dq_a,dq_b\rangle=4|E_{\rm mix}|^2.
   \]
   因此 \(q\) 是一阶守恒/强迫变量；不能从现有材料推出
   \[
   \rho^{-1}\operatorname{div}(\rho A\nabla q)=\text{source}
   \]
   这样的二阶场方程，也不能据此断言其 Dirichlet 核、特征值或“全耦合 transverse operator”。

2. 本任务研究的是非紧两端 quotient cylinder。把它替换为无边界闭轨道空间后积分
   \(L\sigma=6+Q\) 所得矛盾，回答的是另一个问题；展开端有非零无穷远通量。该面积积分也明确不满足“独立伴随投影、不得只是面积方程重排”的要求。

3. \(Q=\frac12e^{-3\sigma}q^TM^{-1}q\) 是势能，不是目标度量中的 \(dq\)-动能；把
   \(\mathbb R^2_q\) 添加为 sigma-model target 并不能从给出的约化方程推出。

4. 精确 OT 开端要求 \(q=0\)。固定非零 \(q\) 的展开端只能称为**红移带电渐近端**，不能称为 OT；它可作为随后远端 taper 的中间构造。

---

## 1. 固定域、未知空间及规范

取固定圆柱
\[
\Omega=\mathbb R_\tau\times S^1_s,
\]
不预设过渡长度或接口。固定 \(T^2\) 标记，并用

\[
\gamma=e^{2\varphi}(d\tau^2+ds^2),\qquad
G=e^\sigma M(U),\qquad U=(\alpha,\zeta)\in\mathbb H^2
\]
表示基底和轨道度量，其中
\[
M=
\begin{pmatrix}
e^\alpha+\zeta^2e^{-\alpha}&\zeta e^{-\alpha}\\
\zeta e^{-\alpha}&e^{-\alpha}
\end{pmatrix},\qquad \det M=1.
\]

连接取 Coulomb 规范
\[
d_\gamma^*A=0,
\]
再固定其两个端部 holonomy；其曲率由 \(q=(q_1,q_2)\) 编码。余下共形自同构用以下条件消除：

* 中心圆固定为 \(\{\tau=0\}\)；
* 一个指定的 \(s\)-相位固定 Koiso target circle 的参数原点；
* 两端定义函数的加性平移通过中心归一化固定。

未知量为
\[
V=(\varphi,\sigma,U,q;p),
\]
其中 \(p\) 是**两端共享的有限参数向量**，至少包含
\[
p=(S,\mathfrak q,\vartheta_0;
 \ell_\pm,\sigma_\pm,U_\pm,\text{hol}_\pm).
\]
这里同一个 \(S,\mathfrak q,\vartheta_0\) 同时进入左右半问题，不能分别调节。

适合的 Banach 空间可取 compactified \(b\)-Hölder 空间。在两端令
\[
y_\pm=e^{-r_\pm}\to0,
\]
并分离模型项
\[
\varphi=-\log y_\pm+\log\ell_\pm+\widehat\varphi_\pm,\quad
\sigma=-2\log y_\pm+\sigma_\pm+\widehat\sigma_\pm,\quad
U=U_\pm+\widehat U_\pm.
\]
余项置于 \(y_\pm^\eta C_b^{k,\alpha}\)，而 \(q\) 的空间依所求分支选择：

* 固定电荷桥：\(q-\mathfrak q\in y^\eta C_b^{k-1,\alpha}\)；
* OT taper：\(q\in y^\eta C_b^{k-1,\alpha}\)，且中心迹为 \(\mathfrak q\)。

必须保留全部 \(s\)-Fourier 模式；径向平坦 \(T^3\) 子模型不属于允许的未知空间。

---

## 2. 全 Ricci 残差

定义
\[
\mathscr E(V)=(H,T,Z,\mathcal B),
\]
其中
\[
\begin{aligned}
H={}&\operatorname{Ric}_\gamma-\operatorname{Hess}_\gamma\sigma
-\frac12d\sigma\otimes d\sigma-\frac12U^*h
-Q\gamma+3\gamma,\\
T={}&L\sigma-6-Q,\\
Z={}&\tau_\sigma(U)+\nabla_UQ,\\
\mathcal B={}&e^{-3\sigma/2}M^{-1/2}dq,\\
Q={}&\frac12e^{-3\sigma}q^TM^{-1}q,\qquad
L=\Delta_\gamma+\langle\nabla\sigma,\nabla\cdot\rangle .
\end{aligned}
\]

该 \(\mathcal B\) 归一化与精确公式
\[
|\mathcal B|^2=4|E_{\rm mix}|_{\rm HS}^2
\]
一致。不能仅求 \(T=Z=\operatorname{tr}H=0\) 而把 \(\mathring H\) 留到最后；那样会产生可能根本不是几何解的“core solve”。可行的数值/分析实现是：

* 用 \((T,Z,\operatorname{tr}H)\) 构成椭圆主块；
* 将 \(\mathring H\)、一阶混合块及有限余核投影视为同时求零的匹配条件；
* 利用 Noether/Bianchi 恒等式删除真正冗余的方程，而不是任意丢弃 \(H\) 分量。

在平坦共形坐标中，最高阶项为
\[
DT_2=e^{-2\varphi}\Delta_0\dot\sigma,\qquad
DZ_2=e^{-2\varphi}\Delta_0\dot U,
\]
\[
D(\operatorname{tr}_\gamma H)_2
=e^{-2\varphi}(-2\Delta_0\dot\varphi-\Delta_0\dot\sigma),
\]
\[
D(\mathring H)_2=-(\nabla_0^2\dot\sigma)^\circ,
\qquad
D\mathcal B_1=e^{-3\sigma/2}M^{-1/2}d\dot q+\text{低阶项}.
\]
所以 \((\dot\varphi,\dot\sigma,\dot U)\) 是二阶椭圆块，而 \(\dot q\) 是两分量一阶 de Rham 块。经规范固定和 Bianchi 冗余消除后，主系统是混合阶 Douglis–Nirenberg 椭圆系统；其有限指数缺陷来自：

* 两端渐近模量；
* 圆柱的长度/相位共形模；
* \(q\) 的常数零阶模式及两端/中心迹；
* 加权伴随核。

精确 Fredholm 指数不能仅凭当前资料给出；应由两端 indicial family 计算，而非简单 Fourier 未知数计数。

---

## 3. 精确共享中心数据

固定 \(0<S<3\)，取周期解析曲线 \(U_0(s)\) 满足
\[
|U_0'|^2=12+2S.
\]
选择常数协向量 \(\mathfrak q\ne0\)，使
\[
Q_0(s)=\frac12\mathfrak q^TM(U_0(s))^{-1}\mathfrak q<S,\qquad
P(s)=S-Q_0(s)>0.
\]
令 \(N\perp U_0'\) 为 target unit normal。中心 Dirichlet 迹为
\[
\varphi(0,s)=0,\quad \sigma(0,s)=0,\quad
U(0,s)=U_0(s),\quad q(0,s)=\mathfrak q.
\]

Koiso 法向迹应以完整第二基本形式编码：
\[
\operatorname{tr}W=0,\qquad |W|^2=S,
\]
\[
B=\sqrt{P/2}\,M^{-1}dM(N),\qquad m=-\mathfrak q/2,
\]
并在两侧采用各自向外法向的相反符号。等价地，在与该几何法向一致的约定下，
\[
\varphi_\nu=0,\qquad \sigma_\nu=0,\qquad
U_\nu=\sqrt{2P}\,N,
\]
但实际实现应直接由 \(W\) 转换，以避免方向和连接符号错误。

给出的 Taylor 数据提供了重要非退化信息：
\[
\sigma_{\nu\nu}=6+Q_0(s),\qquad
a_{\nu\nu}=-(3+S+Q_0(s)),
\]
且三维切片平均曲率满足
\[
\mathcal H(0)=0,\qquad \partial_\nu\mathcal H(0)=2.
\]
因此两侧最初都沿各自向外方向扩张。短程 \(N=96\) 演化在 \(0\le n\le0.02\) 上保持正定，\(Q_{\max}\) 从 \(0.5\) 变到约 \(0.50956\)；这只证明种子适合作为局部初猜，不是全局存在证据。

---

## 4. 两个端及联合匹配映射

### 固定电荷红移桥

要求两端
\[
\gamma=dr_\pm^2+\ell_\pm^2e^{2r_\pm}ds^2+o(1),\quad
\sigma=2r_\pm+\sigma_\pm+o(1),\quad
U=U_\pm+o(1),
\]
且
\[
q\equiv\mathfrak q.
\]
于是
\[
Q=O(e^{-6r_\pm}).
\]
这是 exact charged asymptotic bridge 问题，不是 OT 问题。

### OT taper 两端问题

要求
\[
q\to0
\]
于两端，同时 \(q|_{\tau=0}=\mathfrak q\)。taper 的位置和宽度都不预先指定；它们由全局未知函数 \(q(\tau,s)\) 自发产生。

定义联合映射
\[
\mathfrak M(V,p)=
\left(
\mathscr E(V),\
\mathcal C_+(V,p),\
\mathcal C_-(V,p),\
\mathcal K_+(V,p),\
\mathcal K_-(V,p),\
\mathcal G(V),\
\Pi(V)
\right).
\]
其中：

* \(\mathcal C_\pm\)：各端渐近系数及 OT/fixed-charge 条件；
* \(\mathcal K_\pm\)：由左右全局解返回中心的 Dirichlet–Neumann 数据与同一 Koiso \(W(S,\mathfrak q,\vartheta_0)\) 的差；
* \(\mathcal G\)：Coulomb、中心位置和相位规范；
* \(\Pi\)：有限维独立伴随投影。

若采用两半域 Dirichlet-to-Neumann 实现，真正的共享匹配条件是
\[
\mathcal N_\pm(p)-\mathcal K_\pm(p)=0
\]
同时成立，而不是分别选择两套中心参数。也应加入两半连接 holonomy 和所有切向导数的兼容条件。

---

## 5. 已存在的红移近核

在展开端 \(\sigma=2r+O(1)\) 上，若将 \(q\) 在远处 \(R\) 附近、宽度 \(\ell\) 内从 \(\mathfrak q\) taper 到 \(0\)，则
\[
\|\mathcal B\|_\infty
\lesssim |\mathfrak q|e^{-3R}\ell^{-1},
\qquad
\|Q\|_\infty\lesssim|\mathfrak q|^2e^{-6R}.
\]
此外 \(D_q(H,T,Z)=0\) 于 \(q=0\) 端，因为这些块对 \(q\) 二次依赖。因此 \(q\)-taper 是比 log-Weyl 的 \(L^{-1}\) 插值更便宜的指数近核候选。

但该估计只说明：**若**存在通向两个展开端的全耦合固定电荷桥，则可在更远处加上极小 Ricci 代价的 OT taper。红移面积模型冻结 \(M\) 并违反 \(Z=0\)，故不能单独证明桥存在。

---

## 6. 真正独立的伴随投影

### (a) TT/Hopf 投影

对满足
\[
\operatorname{tr}_\gamma\Theta=0,\qquad
\operatorname{div}_\sigma\Theta=0
\]
的加权伴随张量，取
\[
\Pi_\Theta=\int_\Omega \mathring H:\Theta\,d\mu_\sigma.
\]
最低圆柱模式检测相对长度和相位；它们不是面积方程的重排。

### (b) 水平 Noether/\(K_X\) 投影

对在精确端 collar 内截断的向量场 \(X\)，
\[
\int m_q(X)\,d\mu_\sigma
=
\int\!\left[
2H:\operatorname{sym}\nabla X
-(\operatorname{tr}H)\operatorname{div}_\sigma X
+T\operatorname{div}X
-\langle Z,dU(X)\rangle
\right]d\mu_\sigma,
\]
以及
\[
\int m_q(X)\,d\mu_\sigma
=-\frac12\int q^TK_Xq\,d\mu_\sigma,
\]
\[
K_X=X(A)+(\operatorname{div}_\sigma X)A,\qquad
A=e^{-3\sigma}M^{-1}.
\]

不要选 \(X=\nabla\sigma\)，因为固定电荷时它退化为面积—电荷恒等式。应解真正的伴随边值问题，分别选取：

\[
X_{\rm len},\qquad X_{\rm phase},
\qquad X_{k,c},X_{k,s}\ (k=1,\ldots,K),
\]
其端部条件检测两端相对长度、中心 target 相位及 \(s\)-依赖。特别是 wind-one 种子必须保留 \(k=\pm1\) 模式。

Step 96 的紧支撑 \(X\) 诊断趋于零，正是精确 Einstein germ 上 Noether 恒等式的预期；它排除了“任取局部 \(X\) 就产生正 obstruction”的想法。候选余核必须贯穿中心和无穷端。

### (c) target Killing-current 投影

对 \(\mathbb H^2\) 的 Killing 场 \(Y\)，定义
\[
J_Y(r)=\int_{S^1}e^\sigma a
\langle U_r,Y(U)\rangle\,ds.
\]
由 \(Z\) 方程，
\[
J_Y(r_2)-J_Y(r_1)
=
\int_{r_1<r<r_2}
\left[
\langle Z,Y\rangle-\langle\nabla_UQ,Y\rangle
\right]d\mu_\sigma.
\]
三个独立 \(SL(2,\mathbb R)\) 方向检测 target 形状和电荷方向是否能同时匹配两个常值端。这些投影与 TT 和水平 Noether 投影具有不同几何来源。

---

## 7. 决定性计算

最便宜且真正回答本任务的计算是 compactified Chebyshev–Fourier 全域求解和奇异值延拓。

### A. 固定电荷桥

以
\[
S=1,\qquad Q_{\max}=1/2,\qquad \mathrm{wind}=1
\]
的精确 Koiso 数据为中心迹，令 \(q\equiv\mathfrak q\)，同时求
\[
H=T=Z=0
\]
及两个展开端条件。监测：

\[
\|\mathscr E\|,\qquad
\|\mathcal K_+\|+\|\mathcal K_-\|,\qquad
\Pi_\Theta,\quad \Pi_Y,
\]
并做 \(N_\tau,N_s\) 双向谱收敛。若全残差和共享中心 mismatch 同时谱收敛到零，即给出固定电荷两端桥的强数值证据。

### B. 完整变量电荷线性化

对逐渐增大的 compactified truncation 参数 \(R\)，计算
\[
s_{\min}(R)=
\inf_{\dot V}
\frac{\|D\mathfrak M_R\,\dot V\|}
{\|\dot q|_{\Sigma}\|},
\]
这里分子必须包含
\[
DH,\ DT,\ DZ,\ D\mathcal B
\]
以及 TT、\(K_X\)、target-current 和规范条件。

结果只有两种关键型态：

* **红移近核：**
  \[
  s_{\min}(R)\sim Ce^{-3R}
  \]
  或更快趋零，右奇异向量在远端主要是 \(q\)-taper，左奇异向量的自然范数发散或向无穷端逃逸。

* **有限 obstruction：**
  \[
  s_{\min}(R)\to s_*>0
  \]
  或出现收敛的归一化左零模 \(\Psi_*\)，其 TT、\(K_X\) 或 target-current 分量对中心 Koiso 数据给出非零投影。

必须同时改变 \(R\)、Fourier 截断和权重，避免把有限盒的虚假谱隙误认成 obstruction。最有证明价值的输出不是单个数值，而是收敛左伴随场：一旦获得它，可以尝试证明其加权范数一致有界，并利用
\[
-\frac12\int q^TK_Xq\,d\mu_\sigma
\]
或 target flux 确立严格非零配对。

这一 formulation 保留了精确 charged Koiso 局部自由度、两个展开端的共享参数、所有 Ricci 块及两个独立于面积方程的伴随机制；同时明确了唯一尚未解决的数学对象：**全耦合两端匹配映射是否具有逃向无穷的红移近核，还是具有有界非零余核。**
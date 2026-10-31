# O10：无界密度的定量逃逸约束；O11：本轮边界

日期：2026-09-29。本文继续研究原 O10／O11，不改动原统一积分障碍、N1 或 I40/I41 的陈述。

## 0. 本轮结果及其准确地位

本轮将最新附件 `O10_All_Finite_Density.md` 的线丛对数 resolvent 引理定量化，使截面的 Dirichlet 能量可以增长，而不是先假设它沿序列一致有界。再把实际负手性辅助截面构造中的常数依赖逐项保留，得到：

> **条件于已经提供的同解参数预算与 R1 强流前置，在原 O10 输入下，存在普适常数 \(c,C>0\)，使标量曲率归一化为 \(-4\) 的代表、\(\beta\ge4\) 满足**
> \[
> \boxed{\kappa_\beta+\beta^{-2}\ge
> c\exp\!\left[-C\left(1+\fint|W^-|^2\right)^2\right].}
> \tag{D.1}
> \]
> 其中 \(\kappa_\beta=(P+D_\beta)/V\)。

由此，可以把任意有限 Euler 密度版本中的存在型常数具体下控为
\[
\boxed{
\frac{\chi(M)}A\le B\quad\Longrightarrow\quad
\fint|\operatorname{Ric}_g+g|^2+\frac{D_\beta(g,a)}{V_g}
\ge c_1e^{-C_1(1+B)^2}\frac{(\beta-2)^2}{\beta^2},\quad\beta\ge2.
}
\tag{D.2}
\]
这里 \(B\ge0\)，常数 \(c_1,C_1\) 不依赖 \(B\)。负的 \(B\) 不需要另作新的渐近讨论。

与“任意固定有限 \(B\)”的前置结果相比，(D.1) 不先假设密度有界，并排除了确实允许 \(\fint|W^-|^2\to\infty\) 的一类慢增长逃逸。例如，当 \(\eta_j:=\kappa_j+\beta_j^{-2}\to0\) 时，
\[
1+\fint|W_j^-|^2=o\!\left(\sqrt{\log(1/\eta_j)}\right)
\tag{D.3}
\]
与原实际系统不相容。

**本轮没有证明完全无密度损失的 O10，也没有决定 O11 的最佳首项。**(D.1) 仍允许反手性曲率能量增长至少达到所示速率；不能把这一可能性删去。没有给出满足全部 O10 条件的反例。O11 本轮未产生新的匹配全局下界或低成本闭流形构造。

(D.1) 的新内容是跟踪实际误差与增长能量的关系，不是把“对每个 B 存在 c(B)”误换成“存在对所有 B 有效的正 c”。第1节的定量线丛引理独立证明；第2—5节清楚列出继承的分析输入。本文未重新认证整份整合稿，也不主张已经完成全球首创性核查。

---

## 1. 线丛的定量对数障碍：允许 Dirichlet 能量增长

以下平均均为 \(V^{-1}\int_M\)，包括在子集上积分。所有范数按这个概率测度计算。

### 1.1 命题

设 \((M^4,g)\) 为闭定向光滑四流形，\(K\to M\) 为 Hermitian 线丛，带 unitary 联络 \(\nabla\)。记其实曲率为 \(F=-iF^K\)。假设
\[
\fint|\operatorname{Ric}|^2\le C_R,
\qquad F=F_0+e_F,
\qquad |F_0|\le C_F.
\tag{1.1}
\]
不要求 \(F_0\) 闭。曲率 \(F\) 本身闭。

设 \(s\) 为光滑截面，满足
\[
|s|\le M_0,\qquad \ell>0,
\qquad \mathsf E:=1+\fint|\nabla s|^2\ge1.
\]
其中 \(M_0,\ell,C_R,C_F\) 固定，而 \(\mathsf E\) 允许任意增长。置
\[
d=\fint(|s|-\ell)^2,
\qquad \Delta=d+\fint|e_F|^2.
\tag{1.2}
\]
当 \(0<\Delta\le e^{-4}\) 时，存在只依赖上述固定常数和维数的 \(C\)，使
\[
\boxed{
\frac{|c_1(K)^2[M]|}{V}
\le \frac{C\mathsf E}{\sqrt{\log(1/\Delta)}}.
}
\tag{1.3}
\]
若 \(\Delta=0\)，截面处处具有非零常模，线丛平凡，左边为零。

特别地，若左边至少为固定 \(q_0>0\)，则
\[
\boxed{
\log(1/\Delta)\le C_{q_0}\mathsf E^2.
}
\tag{1.4}
\]
这里既不要求非塌缩，也不使用统一 Sobolev 常数、直径、注入半径或全 Riemann 曲率预算。

### 1.2 谱参数的选择

令 \(L=\nabla^*\nabla\ge0\)，以及
\[
u_\varepsilon=(I+\varepsilon L)^{-1}s,
\qquad K(\varepsilon)=\fint|Lu_\varepsilon|^2.
\]
最大值原理与谱计算给出
\[
|u_\varepsilon|\le M_0,
\qquad \fint|u_\varepsilon-s|^2\le\varepsilon\mathsf E,
\qquad \fint|\nabla u_\varepsilon|^2\le\mathsf E.
\tag{1.5}
\]
每个特征值 \(\lambda\ge0\) 满足
\[
\int_0^\infty\frac{\lambda^2}{(1+\varepsilon\lambda)^2}\,d\varepsilon=\lambda.
\]
因而
\[
\int_0^\infty K(\varepsilon)\,d\varepsilon
=\fint|\nabla s|^2\le\mathsf E.
\tag{1.6}
\]
在区间 \([\Delta^{1/2},\Delta^{1/4}]\) 上按 \(d\varepsilon/\varepsilon\) 平均，存在 \(\varepsilon\) 使
\[
\Delta^{1/2}\le\varepsilon\le\Delta^{1/4},
\qquad
\varepsilon K(\varepsilon)\le
\frac{4\mathsf E}{\log(1/\Delta)}.
\tag{1.7}
\]
这里没有先假设 \(\mathsf E\) 一致有界。

### 1.3 Hessian 换指标估计

对固定有界截面 \(u\)，令 \(I=\int|\nabla^2u|^2\)、\(J=\int|\nabla u|^4\)。精确 Hessian 换指标后，联络曲率项不带导数，切空间曲率只通过 Ricci 缩并出现。因此
\[
I\le C\int|Lu|^2+C M_0^2\int|F|^2
+C\int(|\operatorname{Ric}|+|F|)|\nabla u|^2.
\tag{1.8}
\]
直接对 \(|\nabla u|^2\operatorname{Re}\langle u,\nabla u\rangle\) 作散度积分，得到
\[
J\le C M_0^2 I.
\tag{1.9}
\]
用 Cauchy–Schwarz、Young 在 (1.8) 中吸收 \(I\)，得到
\[
\fint\bigl(|\nabla^2u|^2+|\nabla u|^4\bigr)
\le C\left(\fint|Lu|^2+\fint|\operatorname{Ric}|^2+\fint|F|^2\right).
\tag{1.10}
\]
由于 \(\Delta\le e^{-4}\)，(1.1) 保证此处最后两项有统一常数界。于是对所选 \(u=u_\varepsilon\)，
\[
\fint|\nabla u|^4\le C(K(\varepsilon)+1).
\tag{1.11}
\]
此估计不使用任何统一坐标图。

### 1.4 低幅度区与 Chern 配对

令 \(Z=\{|u|\le3\ell/4\}\)。由 (1.2)、(1.5)，
\[
\mu(Z):=\frac{\operatorname{Vol}(Z)}V
\le C(d+\varepsilon\mathsf E)
\le C\varepsilon\mathsf E.
\tag{1.12}
\]
最后一步用 \(d\le\Delta\le\varepsilon\)、\(\mathsf E\ge1\)。即使右边超过1，这仍是合法上界，不需要 \(\varepsilon\mathsf E\to0\)。

选固定光滑 \(\chi\)，在 \(|u|\le\ell/2\) 为0，在 \(|u|\ge3\ell/4\) 为1。置
\[
a=|u|^2,\qquad j_u=\operatorname{Im}\langle u,\nabla u\rangle,
\qquad\theta=\chi(a)j_u/a.
\]
它在零点附近为零，因此全局光滑。线丛上的精确局部恒等式为
\[
d\theta=\chi F+\chi'\,da\wedge j_u/a.
\tag{1.13}
\]
由于 \(dF=0\)，Stokes 给出
\[
\left|\fint F\wedge F\right|
\le C\fint_Z|F|^2+C\fint_Z|F|\,|\nabla u|^2.
\tag{1.14}
\]
将 \(F\) 分为有界模型和小误差，利用 (1.11)—(1.12)，得到
\[
\left|\fint F\wedge F\right|
\le C\left[
\varepsilon\mathsf E+\Delta
+\sqrt{\varepsilon\mathsf E(K+1)}
+\sqrt{\Delta(K+1)}\right].
\tag{1.15}
\]
所有常数独立于 \(\mathsf E\)、\(\Delta\) 及所选谱参数。

写 \(\mathsf L=\log(1/\Delta)\ge4\)。由 (1.7)，右边至多
\[
C\left[
\mathsf E\Delta^{1/4}+\Delta
+\frac{2\mathsf E}{\sqrt{\mathsf L}}
+\sqrt{\mathsf E}\Delta^{1/8}
+\frac{2\sqrt{\mathsf E}\Delta^{1/4}}{\sqrt{\mathsf L}}
+\sqrt\Delta\right].
\]
因为 \(\mathsf E\ge1\)，指数小量均可由固定常数乘 \(\mathsf E/\sqrt{\mathsf L}\) 控制。再用
\[
c_1(K)^2[M]/V=(4\pi^2)^{-1}\fint F\wedge F
\]
即得 (1.3)。这也证明 (1.4)。

---

## 2. O10 的辅助截面：保留增长常数，而不假设其一致有界

本节只使用已给强流系统、同丛 resolvent 和第1节的独立估计。**不使用 Nijenhuis 第一括号延拓，不调用弱 CR 第五幂线丛证明。**

在 \(s=-4\) 的实际代表上，令
\[
\eta=\kappa_\beta+\beta^{-2},\quad
\rho=|\Phi|^2,\quad\rho_*=4/3,\quad
\tau=t_\Phi\in S^-\otimes L,\quad m_*=128/81.
\]
记 \(T=\nabla_{3A}^*\nabla_{3A}\)。使用附件的有界截断和
\[
v=3(I+T)^{-1}u.
\tag{2.1}
\]
其构造不需要 \(W^-\) 上界，给出统一的
\[
|\Phi|+|v|+|Tv|\le C,\quad
\fint|\nabla\Phi|^4\le C,\quad
\fint|\nabla v|^2\le C.
\tag{2.2}
\]
把接下来所需的实际小量合成
\[
\begin{aligned}
\mathfrak e={}&
\|\rho-\rho_*\|_2+
\||v|^2-m_*\|_2+
\|Tv-2v\|_2+
\|D^-_{3A}v\|_2\\
&+\|N_v\|_{2,\{\rho\ge c_0\}}
+\|f-K_{\mathrm{fit}}\|_2
+\|\operatorname{Ric}+g\|_2,
\end{aligned}
\tag{2.3}
\]
其中 \(0<c_0<\rho_*/4\) 固定，\(f=-iF_A^-\)，\(K_{\mathrm{fit}}\) 是原有界同场拟合，\(N_v=(\nabla v)^{1,0}_{J_+}\)。\(N_v\) 只在正旋量非零的区域使用；零区通过后述低幅度估计处理。

这些量沿 O10 零端都趋零，而不需 \(b:=\fint|W^-|^2\) 有界。第5节从原有定量前置给出一个保守的统一幂次率。先不使用该速率，仅假定 \(0<\mathfrak e\le1\)。

置
\[
\mathsf K=1+b\ge1.
\]
负手性联络完整曲率满足
\[
\fint|F^{S^-\otimes L}|^2\le C\mathsf K.
\]
由 (1.8)—(1.10) 的同秩向量丛版本，
\[
\boxed{
\fint\bigl(|\nabla^2v|^2+|\nabla v|^4\bigr)\le C\mathsf K.
}
\tag{2.4}
\]
这里的 \(C\) 独立于 \(b\)。不能把 (2.4) 写成没有 \(\mathsf K\) 的一致界。

---

## 3. 定量幅度—相位—Dirac 归约

令
\[
a=|v|^2,\quad q=|\nabla v|^2,\quad q_*=2m_*.
\]
由 \(Tv=2v+r_v\)，\(\|r_v\|_2\le\mathfrak e\)，有
\[
\Delta a=4a-2q+r_a,\qquad
\|r_a\|_2\le C\mathfrak e,
\tag{3.1}
\]
其中 \(\Delta=d^*d\)。因 \(v\) 有界，\(r_a=2\operatorname{Re}\langle v,r_v\rangle\)。同时
\[
\left|\fint q-q_*\right|\le C\mathfrak e.
\tag{3.2}
\]

### 3.1 径向导数

测试 (3.1) 对 \(a-m_*\)：
\[
\boxed{
\|da\|_2^2\le C\mathfrak e\mathsf K^{1/2}.
}
\tag{3.3}
\]
因为 \(\|q\|_2\le C\mathsf K^{1/2}\)。这一步明确保留了增长能量的依赖。

### 3.2 梯度密度的协方差

取 \(\mathcal T(q)=q/(1+q)\)。有
\[
|d\mathcal T(q)|\le C|\nabla^2v|,
\]
故
\[
\left|\fint\langle da,d\mathcal T(q)\rangle\right|
\le C\mathfrak e^{1/2}\mathsf K^{3/4}.
\]
将 (3.1) 与 \(\mathcal T(q)\) 配对，再减去常数 \(\mathcal T(q_*)\) 乘 (3.2)，使用
\[
(\mathcal T(q)-\mathcal T(q_*))(q-q_*)
=\frac{(q-q_*)^2}{(1+q)(1+q_*)},
\]
得到
\[
\boxed{
\fint\frac{(q-q_*)^2}{1+q}
\le C\mathfrak e^{1/2}\mathsf K^{3/4}.
}
\tag{3.4}
\]
因此
\[
\boxed{
\|q-q_*\|_1\le C\mathfrak e^{1/4}\mathsf K^{3/8}.
}
\tag{3.5}
\]
最后使用 \(\fint q\le C\)，不是用一个随 \(b\) 增长的 \(L^1\) 界。

### 3.3 低幅度区及剩余导数分量

取 \(G=\{\rho\ge c_0,\ a\ge m_*/4\}\)。由 (2.3)，
\[
\mu(M\setminus G)\le C\mathfrak e^2,
\qquad
\fint_{M\setminus G}q\le C\mathfrak e\mathsf K^{1/2}.
\tag{3.6}
\]
第二式来自 (2.4) 与 Cauchy–Schwarz，不能无依据忽略坏集合。

写 \(j_v=\operatorname{Im}\langle v,\nabla v\rangle\)。原实际型投影的代数关系为
\[
|j_v+J_+da/2|^2\le2a|N_v|^2.
\]
由 (3.3)、(3.6) 得
\[
\|j_v\|_2^2\le C\mathfrak e\mathsf K^{1/2}.
\tag{3.7}
\]
在 \(G\) 的适配局部标架中，令
\[
A_i=\nabla_{Z_i}v,\quad B=\nabla_{\bar Z_1}v,\quad C_2^{\rm vec}=\nabla_{\bar Z_2}v.
\]
这里最后一个符号是二分量旋量，不是 Chen 类；下文写其第二分量为 \(c_2\)。

由 \(N_v\) 小、\((\nabla v)_1=(da/2+ij_v)/\sqrt a\)、以及
\[
D^-v=((A_1)_1-(A_2)_2,B_2+(C_2^{\rm vec})_1),
\]
除 \(c_2=(\nabla_{\bar Z_2}v)_2\) 外的分量，其总二次能量不超过
\[
C\mathfrak e\mathsf K^{1/2}.
\tag{3.8}
\]
这些论证只使用代数投影、质量与 Dirac 残差，不使用未控制的括号导数。

---

## 4. 第五幂线丛的定量质量与能量

定义全局光滑多项式截面
\[
\sigma=\Phi\wedge t(v)\in\Gamma(L^5).
\tag{4.1}
\]
在同时适配 \(\Phi=\sqrt\rho(1,0)\)、\(v=\sqrt a(1,0)\) 的标架上，项目 Clifford 规范给
\[
t(v)_2=a\,c_2,
\qquad |\sigma|^2=\rho a^2|c_2|^2.
\tag{4.2}
\]
四个复方向的导数规范满足
\[
2q=|A_1|^2+|A_2|^2+|B|^2+|C_2^{\rm vec}|^2.
\]
因此 (3.8) 控制 \(|\sigma|^2-2\rho a^2q\) 的 \(L^1\) 误差。用 (3.5)，并以 \(\|q\|_2\le C\sqrt{\mathsf K}\) 处理系数 \(\rho a^2-\rho_*m_*^2\)，得到
\[
\left\||\sigma|^2-\ell_*^2\right\|_1
\le C\left(\mathfrak e^{1/4}\mathsf K^{3/8}
+\mathfrak e\mathsf K^{1/2}\right)
\le C\mathfrak e^{1/4}\mathsf K,
\tag{4.3}
\]
其中
\[
\ell_*^2=4\rho_*m_*^3=\frac{33554432}{1594323}>0.
\]
在 \(M\setminus G\) 上使用全局多项式界 \(|\sigma|^2\le Cq\) 及 (3.6)，所以 (4.3) 没有省略零点区。

又因为 \(\Phi,v\) 一致有界，
\[
|\nabla^{5A}\sigma|
\le C\left(|\nabla\Phi|\,|\nabla v|
+|\nabla v|^2+|\nabla^2v|\right),
\]
故
\[
\boxed{1+\fint|\nabla^{5A}\sigma|^2\le C\mathsf K.}
\tag{4.4}
\]
同样，这里没有把右边的 \(\mathsf K\) 删掉。

对 \(\sigma\) 作一个固定有界径向 cap，在 \(\ell_*\) 附近恒等，得 \(s\in L^5\)。它满足
\[
|s|\le M_*,\qquad
\mathsf E_s:=1+\fint|\nabla s|^2\le C\mathsf K,
\]
\[
d_s:=\fint(|s|-\ell_*)^2
\le C\mathfrak e^{1/4}\mathsf K.
\tag{4.5}
\]
这里使用 \((x-\ell)^2\le|x^2-\ell^2|\) 以及 cap 的固定 Lipschitz 性。

\(L^5\) 的实曲率是 \(5(-iF_A)\)。其有界模型与误差只来自原行列式场，不含 \(W^-\)：
\[
\|e_{F^{L^5}}\|_2\le C\mathfrak e,
\qquad
\Delta_s:=d_s+\|e_{F^{L^5}}\|_2^2
\le C\mathsf K\mathfrak e^{1/4}.
\tag{4.6}
\]
同一实际曲率恒等式给
\[
\frac{c_1(L^5)^2[M]}V\longrightarrow\frac{25}{6\pi^2}.
\tag{4.7}
\]
因此，在足够小实际误差范围，此值至少 \(25/(12\pi^2)\)。第5节说明这里也有统一的误差阈值。

将第1节应用于 (4.5)—(4.7)：若 \(\Delta_s<e^{-4}\)，
\[
\log(1/\Delta_s)\le C\mathsf K^2.
\]
而 (4.6) 给
\[
\log(1/\Delta_s)\ge\tfrac14\log(1/\mathfrak e)-\log(C\mathsf K).
\]
故
\[
\boxed{\log(1/\mathfrak e)\le C\mathsf K^2.}
\tag{4.8}
\]
若 \(C\mathsf K\mathfrak e^{1/4}\ge e^{-4}\)，直接由该不等式也得到 (4.8)，调整常数即可。不能仅用 \(\Delta_s\le C\mathsf K\mathfrak e^{1/4}\) 而逆转其对数方向。

这是本轮的一个不依赖上游速率选取的独立结论：**第五幂线丛实际误差与反手性曲率增长必须满足 (4.8)。**

---

## 5. 从原始 O10 误差得到保守的幂次率

本节把 \(\mathfrak e\) 与原始 \(\eta=\kappa_\beta+\beta^{-2}\) 连接；不允许任意挑一个子列，事后假定误差比增长的 \(\mathsf K\) 更快衰减。

令 \(0<\epsilon_0\le1\) 为已给 R1 的固定慢梯度指数，置
\[
\gamma=\frac{\epsilon_0}{1+\epsilon_0}\in(0,1/2],
\qquad \vartheta=\gamma/16>0.
\]
下面得到的较强中间指数，最终统一减弱为 \(\vartheta\)。常数仅来自已给同解预算及 R1，不依赖 \(b\)。

### 5.1 明确继承的定量输入

写 \(q_\Phi=|\nabla_A\Phi|^2\)、\(m=|\tau|^2\)、\(S=m_*+2\rho^2q_\Phi\)。所用输入是
\[
\fint\left(|\rho-\rho_*|^2+|\zeta|^2+|\operatorname{Ric}^{\circ}|^2\right)\le C\eta,
\]
\[
\fint\frac{(S-2m_*)^2}{S}\le C\sqrt\eta,
\qquad
\|f-K_{\mathrm{fit}}\|_2^2\le C\sqrt\eta,
\tag{5.1}
\]
以及 \(0\le\rho\le2\)、\(m\le8q_\Phi\)、\(\nu=2\rho^2q_\Phi-m\le4\rho|\zeta|^2\)。这些式子见原整合稿 `sec:endpoint-covariance` 的 (1.2)—(1.3) 及强流前置第3.2节。

R1 给
\[
\fint_{q_\Phi>L^2}q_\Phi^2
\le C L^{-2\epsilon_0}+C\sqrt\eta.
\tag{5.2}
\]
取 \(L=\eta^{-1/(2+2\epsilon_0)}\)，将 \(|\zeta|^2q_\Phi\) 分到 \(q_\Phi\le L^2\) 及其补集，得到
\[
\fint|\zeta|^2q_\Phi+\fint|\zeta|^4\le C\eta^\gamma.
\tag{5.3}
\]
这里用 \(|\zeta|^2\le2q_\Phi\)。因 \(\gamma\le1/2\)，R1 中的 \(\sqrt\eta\) 余项已被保留在右边。

### 5.2 扭率质量的定量强收敛

由 (5.1)、\(\fint S\le C\) 及 \(\fint\nu\le C\eta\)，
\[
\|m-m_*\|_1\le C\eta^{1/4}.
\]
在 \(m\le M\) 上，以 \(CM\|m-m_*\|_1\) 控制平方误差；在 \(m>M\) 上，用 \(m\le8q_\Phi\) 和 (5.2)。取
\(M=\eta^{-1/[4(1+\epsilon_0)]}\)，得到
\[
\boxed{\|m-m_*\|_2\le C\eta^{\gamma/8}.}
\tag{5.4}
\]
此外 \(\|\nu\|_2\le C\eta^{\gamma/2}\)。

实际三次 Dirac 方程及轴向抵消给
\[
\|D^-_{3A}\tau\|_2\le C\eta^{\gamma/2}.
\tag{5.5}
\]
本式不是从弱 Dirac 收敛中凭空得到的速率；使用的是强流前置中明确的平方估计及 (5.3)。

### 5.3 电流和完整第一扭率投影

原多项式曲率式为
\[
\rho^3f+2Q=2\rho^2(d\operatorname{Im}\zeta)^-+\mathcal R,
\qquad
|\mathcal R|\le C\left(\rho^3|\operatorname{Ric}^{\circ}|
+\rho^{3/2}|\zeta|\,|\nabla\Phi|\right).
\]
令 \(S=m_*+m+\nu\)。\(S\ge m_*\)、\(m\le S\)，且
\[
\|S-2m_*\|_2\le C\eta^{\gamma/8}.
\]
使用有界系数
\(2-(9/8)\rho^6/S\)，先把 \(m\) 写成 \(m_*+(m-m_*)\)，便可用 (5.4) 控制与 \(Q\) 的乘积，不需要对两个任意 \(L^2\) 量作错误乘积估计。由此
\[
\|\rho^2(d\operatorname{Im}\zeta)^-\|_2\le C\eta^{\gamma/8}.
\]
在 \(\rho\ge c_0\) 上除以 \(\rho^2\)。在 \(\rho<c_0\) 上，体积比例为 \(O(\eta)\)，并用
\[
|d\zeta|\le C\left(q_\Phi+\rho|F^{S^+}|\right).
\]
R1 通过阈值分割给出
\[
\fint_{\rho<c_0}q_\Phi^2
\le C\eta^{\epsilon_0/(2+\epsilon_0)}+C\sqrt\eta.
\]
\(F^{S^+}\) 的有界模型加 \(L^2\) 小误差也控制另一项。因此
\[
\|d\operatorname{Im}\zeta\|_2\le C\eta^{\gamma/8}.
\]
这里由 Stokes 使两手性 exterior derivative 能量相等。对1-form和标量 \(\rho\) 使用 Bochner 时，只出现 Ricci 与 \(|\zeta|^2\)、\(|d\rho|^2\) 的配对，(5.3) 控制这些误差；同样对 \(q_\Phi-4/9\) 的有界 \(\rho\) 区及低 \(\rho\) 区分割给 \(L^2\) 误差 \(O(\eta^{\gamma/8})\)。遂得
\[
\boxed{\|\nabla\zeta\|_2+\|N_\tau\|_2\le C\eta^{\gamma/8}.}
\tag{5.6}
\]
完整 \(N_\tau\) 使用原给定多项式投影式；不把它只解释成 Dirac 迹。

### 5.4 上幅度截断和 resolvent 的速率

对固定大阈值测试扭率 Lichnerowicz 公式，正的径向项保留在左边。右边由 (5.4)—(5.5) 和 \(\|f-K_{\rm fit}\|_2\) 控制。因阈值与 \(m_*\) 有固定正距离，
\[
\fint_{m>L}|\nabla\tau|^2\le C\eta^{\gamma/4}
\]
（调整固定阈值后使用）。因此有界径向 cap \(u\) 满足
\[
\|u-\tau\|_{H^1}\le C\eta^{\gamma/8},
\quad \|Du\|_2+\|(\mathcal V+2)u\|_2\le C\eta^{\gamma/8}.
\]
对 (2.1)，精确恒等式
\[
(I+T)(v-u)=-D^*Du+(\mathcal V+2)u
\]
和能量配对给
\[
\|v-u\|_{H^1}\le C\eta^{\gamma/8}.
\]
\(v,u\) 均一致有界，所以 \(\||v|^2-m_*\|_2\le C\eta^{\gamma/8}\)；同时
\(Tv-2v=3(u-v)\)，且 \(N_v-N_\tau\) 在 \(\rho\ge c_0\) 上由 \(\nabla(v-\tau)\) 控制。综上，可保守地统一写为
\[
\boxed{\mathfrak e\le C\eta^\vartheta,\qquad
\vartheta=\frac{\epsilon_0}{16(1+\epsilon_0)}>0.}
\tag{5.7}
\]
这些前置速率全部独立于 \(b\)。\(b\) 第一次以增长预算进入本证明，是 (2.4) 中对负手性辅助截面的完整 Hessian 控制。

### 5.5 特征数的统一正下界

\(\fint|F_A^+|^2\to8/9\) 由 \(\rho\) 的速率直接得到。\(K_{\rm fit}\) 的范数平方是 \(\rho,m,S\) 的有界有理表达式，分母 \(S\ge m_*\)，故 (5.4) 控制其平均误差。再用 \(f-K_{\rm fit}\) 的 \(L^2\) 误差，得到
\[
\frac{a^2[M]}V=\frac1{4\pi^2}\fint\left(|F_A^+|^2-|F_A^-|^2\right)
=\frac1{6\pi^2}+O(\eta^\vartheta).
\]
故 \(c_1(L^5)^2/V\ge25/(12\pi^2)\) 在一个普适的小 \(\eta\) 范围内成立。

把 (5.7) 代入 (4.8) 得
\[
\vartheta\log(1/\eta)-\log C
\le\log(1/\mathfrak e)\le C\mathsf K^2.
\]
整理即得 (D.1)。若 \(\eta\) 不小，缩小前面的普适 \(c\) 使 (D.1) 自动成立。

---

## 6. 全参数及原度量上的显式有限密度常数

在 \(s=-4\)、\(\kappa\le1\)、\(\chi/A\le B\) 时，原标量预算给 \(A/V\le1/(2\pi^2)\)。Gauss–Bonnet 因而给
\[
b\le4B-\frac23+\frac{P}{2V}\le C(1+B).
\]
(D.1) 遂给
\[
\kappa+\beta^{-2}\ge m_B,
\qquad m_B=c_0e^{-C_0(1+B)^2},
\tag{6.1}
\]
可先缩小 \(c_0\) 使 \(m_B\le1/8\)。置 \(\beta_B=(2/m_B)^{1/2}\ge4\)。

- 当 \(\beta\ge\beta_B\)，有 \(\kappa\ge m_B/2\)。
- 当 \(2\le\beta\le\beta_B\)，使用原有限参数估计
  \[
  \kappa\ge r+D_\beta/(\beta V)
  \ge c_f(\beta-2)^2/\beta^4
  \ge(c_fm_B/2)(\beta-2)^2/\beta^2.
  \]

\(\kappa\ge1\) 分支显然足够。故得到标量代表上的 (D.2)。对于原度量，若 \(\kappa_g<1/16\)，原精确共形比较使
\[
\kappa_{\widehat g}\le
\frac{\kappa_g}{1-\sqrt{\kappa_g}-\kappa_g/16}\le2\kappa_g.
\]
大缺陷分支直接处理。\(p,a^2,A,\chi/A\) 的原供给与拓扑条件沿这一比较保留。由此得到 (D.2) 对全部原允许度量成立。

**这一推论不要求按 \(B\) 重新证明一次几何紧性。它只依赖明确显示的指数损失，不能将损失删掉。**

---

## 7. 为什么这仍然不是无条件 O10：一个独立边界检验

(D.1) 允许 \(b\) 至少以 \(\sqrt{\log(1/\eta)}\) 的规模增长。原 O10 的输入没有禁止例如 \(b\) 为 \(\log(1/\eta)\) 量级；本文没有证明这样的实际序列存在，也没有证明它被排除。

不能仅把第1节的线丛引理加强成“不管 Dirichlet 能量多大都使陈数消失”。在固定紧几何上，取具有正平方的线丛及一个具有横截零除子的光滑截面 \(s_0\)，令
\[
s_\varepsilon=\frac{s_0}{\sqrt{|s_0|^2+\varepsilon^2}}.
\]
固定曲率保持不变，\(|s_\varepsilon|\to1\) 于 \(L^2\)，但在横截的实余维2零集附近，相位导数产生 \(O(|\log\varepsilon|)\) 的能量增长。陈数当然不会随截面改变。这是线丛分析的范围检验，**不是**满足 O10 实际 SW 与 Ricci 条件的反例。

因此要彻底删除密度，必须继续使用实际 O10 方程，阻止 (D.1) 允许的快速增长机制，或构造满足原始全部假设的真实逃逸。单纯再次正则化一个能量任意增长的线丛截面，并不能自动完成这件事。

---

## 8. O11：本轮实际检查与未获得的结论

本轮仍保持原平衡族、\(Q=Ah\) 和 \(o(Q)\) 精度。前置的自适应试验
\[
(\nabla^*\nabla+\sqrt{1+|Z|^2})H=Z,
\qquad Z=\operatorname{Ric}^{\circ},
\]
已经给出合法的临界预算及
\[
2\int\operatorname{Rm}(Z,H)
\ge\int|\nabla H|^2+
\int(1+|Z|^2)^{-1/2}|\nabla^*\nabla H|^2-o(Q).
\]
本轮检查的方向是：能否由其正量、弱稳定性或线丛正则化，直接控制原 scalar–Weyl 联合极值的缺失斜率。尚未获得这一连接。原因不是缺一个更大测试空间，而是目前以上配对还没有将其符号和大小与具体拓扑成本 \(8\pi^2Q\) 绑定。

原目标保持为
\[
\inf_gP(g)=8\pi^2Q+o(Q)
\]
或匹配的更低值与真实构造。已知精确 Ricci 下界、标量下界不能相减，弱驻点不能冒充精确临界方程，局部稳定不能排除全部远离标准恢复的竞争者。

本轮没有给出新的 \(O11\) 全局下界；也不将旧变分工具登记为新的突破。第1节及 (D.1) 处理的是 O10 的非零扭率极限，不可把其 \(V\) 尺度结果自动用于 O11 的 \(Q=o(V)\) 尺度。

---

## 9. 依赖与文献核对

### 直接项目前置

1. 用户新文件 `O10_All_Finite_Density.md`：§2 的线丛对数 resolvent 与 rank-one transgression；§3 的幅度—相位—Dirac 归约及 \(L^5\) 截面；§5 对增长常数的保留。本轮的第1节将其改成 \(\mathsf E\) 可增长的定量命题。
2. `01_O10_Strong_Current.md`：R1 的慢梯度截断、同解曲率模型、\(\zeta\) 与 \(N\) 的实际恒等式。第5节补追这些式子的保守幂次速率。
3. `20260929_Line1_Integrated_Manuscript.tex`：`sec:endpoint-covariance` 的 (1.2)—(1.3)、同解类平方预算、有限参数分离和精确共形比较。
4. 续研B `O10_Strengthened_Endpoint.md`：有界 cap 与 \(v=3(I+T)^{-1}u\)；本文不依赖其 \(50/3\) 临界谱定理。
5. 续研B `O11_Positive_Curvature_Compensation.md`：原自适应试验与有符号补偿；仅作为当前 O11 未闭合位置使用。

### 外部核对，非本证明前置

- G. Canevari, F. L. Dipasquale, G. Orlandi, *The Yang–Mills–Higgs functional on complex line bundles: asymptotics for critical points*, arXiv:2304.11346；以及 *The Yang–Mills–Higgs functional on complex line bundles: Γ-convergence and the London equation*, arXiv:2206.03327。其固定底空间和相应场方程／能量假设不能替代本项目变动、可能退化的几何。对数能量尺度已有成熟研究背景；本文不将“发现对数”本身称为首创。
- M. Gursky, J. Viaclovsky, *Rigidity and stability of Einstein metrics for quadratic curvature functionals*, arXiv:1105.4648。局部临界度量与稳定性结论不能直接替代 O11 全度量的极值判定。

### 核验范围

本轮给出了第1—6节的推导，并以精确代数脚本检查谱积分、协方差恒等式、常数及指数比较。脚本不是 PDE 证明，亦不是第二位独立数学研究者的认证。最值得复核的新分析是：第1节中常数对增长能量的独立性，第3—4节的定量投影／低幅度集合估计，以及第5节对继承小量的幂次追踪。

最终状态：O10 获得一个显式增长率障碍与 \(c(B)\) 的下控；无密度损失的 O10 和 O11 最佳首项仍未闭合。

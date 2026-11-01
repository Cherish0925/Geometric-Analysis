# TTCS Independent Branch Record

```json
{
  "step_id": 59,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step58_chiral_bolt_and_zero_charge.md",
    "Sessions/S1003A01/workspace/notes/step55_darboux_ricci_compatibility.md",
    "Sessions/S1003A01/workspace/notes/step56_soldered_instanton_and_SU2_AKE.md",
    "Sessions/S1003A01/workspace/notes/step58_verified_bianchiVIII_AKE_and_closed_zero_locus.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Analyze the zero of the torsion/Nijenhuis section in the closed four-dimensional negative-Einstein almost-Kähler problem. Starting from alpha=∇Ω as a section of E=Λ^{0,1}⊗Λ^{0,2}, the soldered equations (d_b alpha)^-=0, d_b^*alpha=2eta, and the AAD Bianchi/Weitzenböck equations recorded in the supplied notes, derive the strongest trustworthy leading-order constraints at a zero alpha(p)=0. Determine what can and cannot be concluded about vanishing order, isolated local index, sign of that index, and localized top Chern charge. Explore a consequential new route: whether Einstein curvature identities force the leading homogeneous coefficient map into a proper algebraic class incompatible with positive total c2, or instead allow the principal f=z model. Clearly distinguish a proved derivation from a plausible conjecture and point to the next decisive calculation.

## Output

# 科学核验备忘：闭四维 \(s<0\) Einstein–almost-Kähler 结构中的扭率零点

## 1. 零点必然存在，并带有非平凡局部化 Chern 类

令
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2},\qquad \alpha=\nabla\Omega\in\Gamma(E).
\]
这是复秩二、实秩四的向量丛，\(\alpha=0\) 与 Nijenhuis 张量为零等价。

若 \(x_1,x_2\) 是 \(T^{1,0}M\) 的形式 Chern 根，并记 \(c=x_1+x_2=c_1(TM,J)\)，则 \(E\) 的根为 \(x_1+c,x_2+c\)，所以
\[
c_2(E)=c_2(TM)+2c_1(TM)^2.
\]
在四维，
\[
\left\langle c_2(E),[M]\right\rangle
=\chi+2(2\chi+3\tau)=5\chi+6\tau.
\]
对 Einstein 度量，
\[
8\pi^2\chi=\int_M\left(|W^+|^2+|W^-|^2+\frac{s^2}{24}\right)d\mu>0,
\]
\[
4\pi^2(2\chi+3\tau)
=\int_M\left(2|W^+|^2+\frac{s^2}{24}\right)d\mu>0.
\]
因此
\[
\boxed{\left\langle c_2(E),[M]\right\rangle=5\chi+6\tau>0.}
\]
特别地，严格 almost-Kähler 情形中 \(\alpha\) 不可能处处非零。

更精确地，若 \(Z=\alpha^{-1}(0)\)，Thom 类给出
\[
\mathfrak e(\alpha)=\alpha^*U_E
\in H^4(M,M\setminus Z;\mathbb Z),
\]
其到 \(H^4(M;\mathbb Z)\) 的像正是 \(c_2(E)\)。这就是零集承载的局部化最高 Chern 类。

- 若所有零点孤立，则每个零点有 Brouwer 局部次数
  \[
  \operatorname{ind}_p(\alpha)
  =\deg\!\left(\frac{\alpha}{|\alpha|}:S^3_\varepsilon(p)\to S^3\right),
  \]
  且
  \[
  \sum_{p\in Z}\operatorname{ind}_p(\alpha)=5\chi+6\tau.
  \]
- 若零集含曲线或曲面，单点整数不再适用；相对上同调类 \(\mathfrak e(\alpha)\) 仍然存在，并可能由整个零集分支承载。
- 对任意横截扰动得到的带符号点数仍等于 \(c_2(E)\)，但扰动后的截面不再满足 Einstein–almost-Kähler 方程，因而不能据此推断原零集的局部几何。

## 2. 消失阶：有限，但现有方程不给出统一上界

Einstein 度量在调和坐标中实解析；\(\Omega\) 是自对偶闭二形式，故也是调和形式，椭圆解析正则性给出 \(\Omega\) 与 \(\alpha=\nabla\Omega\) 的实解析性。因此在连通严格情形中：

- 若 \(\alpha\) 在一点无限阶消失，则 \(\alpha\) 恒等为零，结构为 Kähler；
- 每个实际零点都有有限消失阶 \(m\ge1\)。

取 \(p\in Z\)，选 \(J(p)\)-标准测地坐标、\(\Lambda^{0,2}\) 的酉标架，并令 \(b(p)=0\)。写
\[
\alpha=P_m+O(r^{m+1}),
\]
其中 \(P_m:T_pM\to E_p\) 是非零齐次次数 \(m\) 的多项式截面。由
\[
(d_b\alpha)^-=0,\qquad d_b^*\alpha=2\eta
\]
的最低次项得到
\[
\boxed{(dP_m)^-=0,\qquad
\eta_{m-1}=\frac12d^*P_m.}
\]
第二式确定 \(\eta\) 的首项，并不是 \(d^*P_m=0\)。

同时
\[
q=|\alpha|^2=|P_m|^2+O(r^{2m+1}),
\]
所以 \(q\) 的消失阶为 \(2m\)。特别地
\[
dq(p)=0,\qquad
\nabla^2q(p)(X,Y)=2\langle\nabla_X\alpha,\nabla_Y\alpha\rangle.
\]
普通强唯一延拓只排除无限阶零，不能排除这种有限阶行为。

若 \(m\ge2\)，则 \(\nabla\alpha(p)=0\)。在 soldered \(\Lambda^+\) 连接中，两个横向曲率行 \(d_b\alpha\) 在 \(p\) 消失；结合 Einstein 曲率算子的对称性可得
\[
\eta(p)=0,\qquad W_3^+(p)=0,
\]
且 \(W^+(p)\) 在 \(\Omega^\perp\) 上具有 Kähler 型特征值。这个点态结论仍不推出邻域内 \(\alpha=0\)。

## 3. 一阶零点的完整主符号

写
\[
\alpha=(f_1\,d\bar z^1+f_2\,d\bar z^2)\otimes\ell .
\]
当 \(m=1\) 时，\((dP_1)^-=0\) 等价于
\[
\partial_{z_1}f_2=0,\qquad
\partial_{z_2}f_1=0,\qquad
\partial_{z_1}f_1=\partial_{z_2}f_2.
\]
所以全部线性首项恰为
\[
\boxed{P_1(z)=cz+B\bar z,\qquad
c\in\mathbb C,\quad B\in M_2(\mathbb C).}
\]

在通常欧氏归一化下，
\[
d^*P_1=-4c\,\ell,
\]
故 \(\eta(p)\) 与 \(c\) 成正比。另一方面，
\[
dP_1
=c\sum_{j=1}^2dz^j\wedge d\bar z^j
+(B_{21}-B_{12})\,d\bar z^1\wedge d\bar z^2.
\]
因此：

- \(c\) 给出 \(\eta(p)\) 的两个实分量；
- \(B_{21}-B_{12}\) 给出 \(W_3^+(p)\) 的两个实分量，差一个固定标架归一化；
- \(B_{\rm sym}\) 完全不出现在 \(dP_1\) 与 \(d^*P_1\) 中。它正是曲率交换子看不到的对称 Hessian 模式。

这说明任何纯点态 Einstein 曲率恒等式都无法控制 \(B_{\rm sym}\)。

## 4. 孤立局部指标的符号并不固定

若 \(P_1\) 可逆，则零点非退化，局部指标是实 Jacobian 的符号：
\[
\operatorname{ind}_p(\alpha)
=\operatorname{sgn}\det_{\mathbb R}(z\mapsto cz+B\bar z).
\]
其行列式可写为
\[
\det_{\mathbb R}P_1
=\det_{\mathbb C}
\begin{pmatrix}
cI&B\\
\bar B&\bar cI
\end{pmatrix}.
\]

主符号中同时出现两种符号：

1. **正指标模型**
   \[
   f(z)=z,\qquad c=1,\quad B=0,
   \]
   给出
   \[
   \det_{\mathbb R}P_1=1,\qquad \operatorname{ind}_p=+1.
   \]

2. **负指标模型**
   \[
   f_1=z_1+2\bar z_1,\qquad f_2=z_2,
   \]
   即 \(c=1,\ B=\operatorname{diag}(2,0)\)。其 Jacobian 为 \(-3\)，故
   \[
   \operatorname{ind}_p=-1.
   \]

3. **非孤立线性零集**
   \[
   c=1,\qquad B=\operatorname{diag}(1,0)
   \]
   给出 \(f_1=2\operatorname{Re}z_1,\ f_2=z_2\)，线性零集含一条实直线。

有一个有用的附加结论：若 \(\eta(p)=0\)，则 \(c=0\)，首项成为纯共轭线性映射
\[
P_1(z)=B\bar z.
\]
若 \(B\) 可逆，则
\[
\det_{\mathbb R}P_1=|\det_{\mathbb C}B|^2>0,
\]
所以这种非退化零点必有指标 \(+1\)。不过一般 Einstein–almost-Kähler 零点并不要求 \(\eta(p)=0\)。

## 5. AAD 方程在零点处没有产生新的首阶代数关系

在 \(p\) 有
\[
\alpha(p)=0,\qquad q(p)=0,\qquad dq(p)=0,\qquad \kappa(p)=s.
\]
AAD Bianchi 方程在该点化为
\[
\boxed{
(\delta\eta)_Z\Omega+\nabla_{JZ}\eta
+2(\delta W_3^+)_Z=0.}
\]
Weitzenböck 方程与式 (3.9) 给出
\[
\boxed{
(\nabla^*\nabla\alpha)_X
=2(\delta\eta)_{JX}\Omega+2(\nabla_X\eta)''.}
\]
这些式子涉及 \(\alpha\) 的二阶 jet、\(\eta\) 与 \(W_3^+\) 的一阶 jet；它们没有给出只含 \(c,B\) 的代数等式。

特别地，\(f=z\) 可通过所有在 \(p\) 直接取值的已显示方程：它满足 \((dP_1)^-=0\)，其非零散度由 \(\eta(p)\) 承担；可取 \(W_3^+(p)=0\)，并令 \(\nabla\eta(p)\)、\(\delta W_3^+(p)\) 与 \(\alpha\) 的二阶迹满足上面两式。这只是一个相容的一阶/二阶点 jet，不是实际 Einstein–almost-Kähler germ。

从连接观点看，这一现象是必然的：在 \(\alpha(p)=0\) 处，Bianchi 恒等式的最高阶部分是
\[
d(dP_m)=0,
\]
而 Weitzenböck 主部是同一连接复形的形式伴随关系。它们不会在主符号层面再切掉 \(P_m\)。

## 6. 对“局部指标阻碍”路线的结论

目前可以严格得出：

- 闭流形上的总局部化电荷为 \(5\chi+6\tau>0\)；
- 零点有限阶，但不必孤立；
- 一阶主符号空间
  \[
  \{\,cz+B\bar z\,\}
  \]
  同时穿过实可逆映射的两个定向分支；
- 正指标模型 \(f=z\) 已被主方程允许；
- 对称矩阵 \(B_{\rm sym}\) 不被点曲率看见，因此点态 Einstein 代数无法固定指标符号。

所以，仅凭 \((d_b\alpha)^-=0\)、\(d_b^*\alpha=2\eta\) 以及未微分的 AAD 方程，不能把首项压入一个与正总 \(c_2\) 不相容的代数子集。即使更高方程只推出 \(\det P_1=0\)，退化孤立零与正维零集仍可承载非零局部化 Chern 类；还需要控制其实际相对 Euler 类。

## 7. 尚未解决的部分与决定性计算

一个可检验但尚未证明的猜想是：\(f=z\) 能延拓到若干阶的形式 Einstein–almost-Kähler jet。支持它的事实是：其 \(\eta\) 源正好吸收散度，\(W_3^+\) 与对称 Hessian 模式仍有充足自由。现有材料没有给出收敛 germ。

真正首次含有 \(P_1\) 非线性信息的是 AAD 方程的一次微分，因为
\[
\nabla^2q(p)(X,Y)
=2\langle P_1(X),P_1(Y)\rangle,
\qquad
\nabla^2\kappa(p)
=3\langle P_1(X),P_1(Y)\rangle,
\]
同时
\[
\nabla(\nabla_{\eta(Z)}\Omega)\big|_p
\]
产生 \(P_1\) 与 \(\eta(p)\) 的二次耦合。

决定性的科学对象是如下有限 jet 消元：

1. 固定 \(c=1,B=0\)；
2. 同时保留无挠 Cartan 结构方程、\(\alpha\) 的型条件、\(F_{A^+}^-=0\)、曲率算子对称性、AAD Bianchi 与 Weitzenböck 方程；
3. 将方程微分到首次出现
   \(\nabla^2q=2P_1^*P_1\) 的阶数；
4. 消去 \(\alpha\) 的二、三阶 jet 以及 \(\eta,W_3^+\) 的导数。

若所得精确线性—二次系统对 \(f=z\) 无解，就会产生一个明确的 \(U(2)\)-不变量多项式，说明首项确实落入更小代数集合；若有解，则正局部电荷模型至少通过首次非线性延拓，零指标路线不能仅依靠现有曲率恒等式。当前资料只支持前述主符号与点 jet 结论，尚未决定这一步。
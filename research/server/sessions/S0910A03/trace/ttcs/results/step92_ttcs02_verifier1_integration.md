# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 92,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step92_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step92_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify a proposed exact family of analytic stable minimal T^3 Cauchy data for local Ric=-3g germs. Let P(s)>0 be analytic periodic on a circle. Choose a closed immersed curve U:S^1->H^2 with |U_s|^2=12+2P(s), and set q=ds^2+M(U(s))_{ab}dx^a dx^b with det M=1. Let A=(1/2)M^{-1}M_s. Choose a target unit normal N(s) perpendicular to U_s, let C_N=M^{-1}dM(N), and define a vertical tracefree Weingarten endomorphism B=sqrt(P/2) C_N, with W(T)=0 and W|vertical=B. Check carefully, in the normalization e_s=(1/2)tr[(M^{-1}M_s)^2], that: Scal_q=-e_s/2; tr W=0; tr W^2=P; the momentum constraint d tr W+delta W=0 is exactly tr(A B)=0 (and all other components vanish by T^2 invariance); the Hamiltonian constraint Scal_q+tr W^2-(tr W)^2=-6 holds; |II|^2=P and e_nu=2P; invariant stability is equivalent to -d_s^2+3-P>=0. If P is a sufficiently narrow analytic von Mises bump of fixed mass m<2sqrt(3)tanh(sqrt(3)L/2), does the stability hold for large concentration, and does Koiso's analytic theorem then yield a genuine local analytic Einstein germ with arbitrarily large e_nu on the center? Identify any hidden error: target-to-matrix normalization, momentum divergence connection terms, global closed curve/normal, analyticity, sign of W, or distinction between invariant and full stability. Explain exactly what this would establish for the connector route and what it would not.

## Integrated Scientific Memo

## 核验结论

该构造在约定的靶空间归一化下是严格成立的。对每个固定的正解析周期函数 \(P\)，所给 \((q,W)\) 精确满足 \(\operatorname{Ric}=-3g\) 的 Hamilton–momentum 约束；Koiso 定理因而给出一个真实的局部解析 Einstein germ。窄 von Mises 峰在所述质量阈值以下最终严格稳定，并且峰心
\[
e_\nu=2P\longrightarrow\infty .
\]

没有隐藏的因子、散度联络项、闭曲线或解析性障碍。需要修正或强调的只有：

- 按来源中的 Weingarten 约定，实际是
  \[
  U_\nu=-\sqrt{2P}\,N,
  \]
  而非正号；能量仍为 \(e_\nu=2P\)。
- 虽然一般的“环路最小化”只给不变稳定性，但对这里的特殊 \(T^2\)-平移不变块度量，不变稳定性事实上等价于完整稳定性。
- Koiso 只逐个峰给出某个 germ；没有随浓度一致的 collar 宽度，也没有两端匹配。

---

## 1. 靶空间与矩阵归一化

令
\[
\mathcal P=\{M=M^T>0:\det M=1\},\qquad
C_X=M^{-1}dM(X),
\]
并采用
\[
\langle X,Y\rangle_{\mathbb H^2}
=\frac12\operatorname{tr}(C_XC_Y).
\]
给定文件中的参数化
\[
M(\alpha,\beta)=
\begin{pmatrix}
e^\alpha+\beta^2e^{-\alpha}&\beta e^{-\alpha}\\
\beta e^{-\alpha}&e^{-\alpha}
\end{pmatrix}
\]
满足
\[
\frac12\operatorname{tr}\bigl[(M^{-1}dM)^2\bigr]
=d\alpha^2+e^{-2\alpha}d\beta^2.
\]
因此题设归一化确实给出
\[
e_s=|U_s|^2
=\frac12\operatorname{tr}\bigl[(M^{-1}M_s)^2\bigr].
\]

设
\[
A=\frac12M^{-1}M_s.
\]
由 \(\det M=1\)，
\[
\operatorname{tr}A=\frac12\partial_s\log\det M=0.
\]

---

## 2. 内蕴标量曲率

对
\[
q=ds^2+M(s)_{ab}\,dx^a dx^b
\]
及平坦 \(T^2\) 纤维，直接的 Gauss/Christoffel 计算给出
\[
\operatorname{Scal}_q
=-2(\operatorname{tr}A)_s-(\operatorname{tr}A)^2-\operatorname{tr}(A^2).
\]
故
\[
\operatorname{Scal}_q=-\operatorname{tr}(A^2).
\]
另一方面
\[
e_s=\frac12\operatorname{tr}[(2A)^2]
=2\operatorname{tr}(A^2),
\]
所以
\[
\boxed{\operatorname{Scal}_q=-\frac12e_s}.
\]
取 \(e_s=12+2P\) 即得
\[
\boxed{\operatorname{Scal}_q=-6-P}.
\]

---

## 3. \(W\) 的代数恒等式

若 \(N\) 是靶空间单位法向，则
\[
\operatorname{tr}C_N=0,\qquad
\frac12\operatorname{tr}(C_N^2)=1.
\]
定义
\[
B=\sqrt{\frac P2}\,C_N,\qquad
W(\partial_s)=0,\qquad W|_{\mathrm{vert}}=B.
\]
于是
\[
\operatorname{tr}B=0,\qquad
\operatorname{tr}(B^2)
=\frac P2\operatorname{tr}(C_N^2)=P.
\]
且
\[
MB=\sqrt{\frac P2}\,dM(N)
\]
是对称矩阵，因此 \(B\) 对纤维度量 \(M\) 自伴。故
\[
\boxed{\operatorname{tr}W=0},\qquad
\boxed{\operatorname{tr}(W^2)=|II|^2=P}.
\]

---

## 4. Momentum 约束及全部联络项

相关 Christoffel 符号为
\[
\Gamma^a_{sb}=A^a{}_b,\qquad
\Gamma^s_{ab}=-(MA)_{ab}.
\]
来源采用
\[
(\delta W)_j=-\nabla_iW^i{}_j.
\]
由于 \(W^s{}_j=0\)，散度中没有 \(B_s\) 项。直接计算得到
\[
(\delta W)(\partial_s)=\operatorname{tr}(AB).
\]
所有垂直分量均为零：系数与 \(x^a\) 无关，纤维内 Christoffel 符号为零，且 \(W\) 没有混合分量。

又因为
\[
A=\frac12C_{U_s},\qquad
B=\sqrt{\frac P2}C_N,
\]
所以
\[
\operatorname{tr}(AB)
=\sqrt{\frac P2}\,
\frac12\operatorname{tr}(C_{U_s}C_N)
=\sqrt{\frac P2}\,\langle U_s,N\rangle_{\mathbb H^2}=0.
\]
由于 \(\operatorname{tr}W\equiv0\)，
\[
\boxed{d\operatorname{tr}W+\delta W=0}.
\]

因此“遗漏 momentum 散度中的联络项”不是问题；这些联络项恰好产生 \(\operatorname{tr}(AB)\)。

---

## 5. Hamiltonian 约束与法向轨道能量

三维超曲面嵌于四维、Einstein 常数 \(\lambda=-3\) 时，Koiso 约束为
\[
\operatorname{Scal}_q+\operatorname{tr}(W^2)-(\operatorname{tr}W)^2
=(3-1)\lambda=-6.
\]
这里
\[
(-6-P)+P-0=-6,
\]
故约束精确成立。

来源中的符号约定是
\[
g_t(WX,Y)=-\frac12\dot g_t(X,Y).
\]
因此中心处
\[
M_\nu=-2MB,\qquad
M^{-1}M_\nu=-2B.
\]
从而
\[
C_{U_\nu}=-2B=-\sqrt{2P}\,C_N,
\]
即
\[
\boxed{U_\nu=-\sqrt{2P}\,N}.
\]
这只是方向符号；能量为
\[
e_\nu
=\frac12\operatorname{tr}(C_{U_\nu}^2)
=2\operatorname{tr}(B^2)
=\boxed{2P}.
\]

---

## 6. 闭曲线、全局法向与解析性

令
\[
v(s)=\sqrt{12+2P(s)},\qquad
\mathcal L=\int_0^L v(s)\,ds,
\]
并取
\[
R=\operatorname{arsinh}\frac{\mathcal L}{2\pi},\qquad
\theta(s)=\frac1{\sinh R}\int_0^s v(u)\,du.
\]
则 \(\theta(L)=2\pi\)。把半径 \(R\) 的双曲圆按 \(\theta(s)\) 参数化，得到闭解析浸入
\[
U:S^1\to\mathbb H^2,\qquad |U_s|=v.
\]
因 \(v>0\)，它确为浸入。利用 \(\mathbb H^2\) 的定向，
\[
N=J\frac{U_s}{|U_s|}
\]
给出全局周期解析单位法向。因此不存在闭合或法向 monodromy 障碍。

严格 \(P>0\) 还保证 \(\sqrt P\) 在圆周上解析。字面上的紧支撑光滑 bump 不足以应用 Koiso；正解析 von Mises 峰恰好避免了这一点。

数值脚本有一个极小的离散化不一致：它重标了数组 `theta`，却未同步重标 `theta_prime`。这解释了 `theta_total` 与 \(2\pi\) 的约 \(10^{-10}\) 偏差；采用上述精确积分定义即可消除，数学构造不受影响。

---

## 7. 稳定性：此处不变稳定性等价于完整稳定性

最小超曲面的二次变分为
\[
Q[f]=\int_{T^3}
\left(
|\nabla f|_q^2-
(\operatorname{Ric}(\nu,\nu)+|II|^2)f^2
\right)d\mu_q .
\]
这里
\[
\operatorname{Ric}(\nu,\nu)=-3,\qquad |II|^2=P,\qquad
d\mu_q=ds\,dx
\]
（因为 \(\det M=1\)），故
\[
Q[f]=\int_{T^3}\bigl(|\nabla f|^2+(3-P)f^2\bigr)\,ds\,dx.
\]
对不变函数 \(f=\phi(s)\)，
\[
Q[\phi]\ge0
\iff
\boxed{-\partial_s^2+3-P\ge0}
\]
作为周期算子。

而对一般函数作固定 \(T^2\) Fourier 展开
\[
f(s,x)=\sum_{k\in\mathbb Z^2}y_k(s)e^{ik\cdot x},
\]
得到
\[
Q[f]
=\sum_k\int_0^L
\left(
|y_k'|^2+
[3-P+k^TM(s)^{-1}k]|y_k|^2
\right)ds.
\]
额外项 \(k^TM^{-1}k\ge0\)，所以最低模态是 \(k=0\)。因此在这个特殊构造中
\[
\boxed{\text{完整稳定性}
\iff\text{\(T^2\)-不变稳定性}
\iff-\partial_s^2+3-P\ge0.}
\]
这不应泛化为一般 separator 最小化问题；等价性依赖这里的平移不变块结构。

---

## 8. 窄 von Mises 峰确实稳定

取圆周长度 \(L\)，质量固定为 \(m\) 的解析峰 \(P_\kappa\)，使
\[
P_\kappa(s)\,ds\rightharpoonup m\delta_0.
\]
设
\[
H_0=-\partial_s^2+3.
\]
其周期 Green 核在对角线上为
\[
G(0,0)=\frac1{2\sqrt3}
\coth\!\left(\frac{\sqrt3L}{2}\right).
\]
因此点值不等式为
\[
|y(0)|^2\le G(0,0)
\int_0^L(|y'|^2+3|y|^2)\,ds.
\]
极限点相互作用
\[
H_0-m\delta_0
\]
严格正定恰在
\[
m<\frac1{G(0,0)}
=2\sqrt3\tanh\!\left(\frac{\sqrt3L}{2}\right).
\]
von Mises 测度收敛结合一维 \(H^1\) 的一致连续性给出
\[
\int P_\kappa |y|^2
\le
\bigl(mG(0,0)+o(1)\bigr)
\int(|y'|^2+3|y|^2).
\]
所以若
\[
\boxed{m<2\sqrt3\tanh(\sqrt3L/2),}
\]
则充分大 \(\kappa\) 时
\[
-\partial_s^2+3-P_\kappa>0.
\]
这不仅是不变严格稳定，也是完整严格稳定。

同时
\[
P_\kappa(0)\sim \frac{m\sqrt{2\pi\kappa}}{L},
\]
故
\[
\boxed{\sup e_\nu=2\sup P_\kappa\to\infty.}
\]
文件中的 \(L=2\pi,m=1\) 满足阈值（阈值约 \(3.464\)），数值最低特征值 \(2.7218>0\) 与此一致。

---

## 9. Koiso 定理的精确后果

来源中的 Theorem 2.1 说明：解析 \(q\) 与解析对称 \(W\) 若满足上述两个约束，则存在唯一的局部解析 Einstein germ
\[
g^{(4)}=dt^2+q_t,\qquad q_0=q,\qquad W_0=W,
\]
且
\[
\boxed{\operatorname{Ric}_{g^{(4)}}=-3g^{(4)}}.
\]
故对每个固定 \(\kappa\)，存在某个 \(\varepsilon_\kappa>0\)，使 germ 定义于
\[
(-\varepsilon_\kappa,\varepsilon_\kappa)\times T^3.
\]
由解析解唯一性，初值的 \(T^2\)-平移对称性传递给 germ。

---

## 对 connector 路线的确切意义

该族严格证明：

1. 完整 Einstein Cauchy 约束；
2. 真实局部解析 Einstein 可延拓；
3. 最小性；
4. 甚至完整严格稳定性；

这些 separator 层面的条件合在一起，仍不能给出 \(e_\nu\) 的通用点态上界。确实存在
\[
\sup_{T^3}e_\nu\to\infty
\]
的真实 Einstein germs，而不仅是形式 jet。因此任何排除法若要控制法向轨道能量，必须使用跨 collar 的传播、正则性或全局两端信息，不能只依赖中心稳定 separator 的约束和 Jacobi 形式。

它没有证明：

- 存在完整或两端的 connector；
- 能匹配预定端几何；
- \(\varepsilon_\kappa\) 有与 \(\kappa\) 无关的正下界；
- 中心 \(T^3\) 在某原始同伦类中是全局面积最小者；
- 在额外假设 \(e_s\) 或内蕴曲率点态有界时仍可集中——事实上
  \[
  e_s=12+2P,\qquad \operatorname{Scal}_q=-6-P
  \]
  与 \(e_\nu\) 同时爆高；
- Yau 第26题或一般非对称、非自由 \(T^2\)、正 Einstein 分支的任何结论。

因此，构造关闭的是“仅凭 separator 层面稳定性控制 \(e_\nu\)”这一局部路线；仍未解决的精确对象是：能否从两端和完整 reduced Einstein/Codazzi–Bianchi 方程导出具有统一尺度的 collar 传输估计，或反过来把这些局部峰延伸成真正的两端 connector。
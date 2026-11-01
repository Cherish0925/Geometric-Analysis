# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 96,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step96_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step96_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step 96 charged-Koiso Einstein Cauchy evolution and relative K_X experiment as a differential geometer/numerical analyst. Check (i) the Gaussian evolution equations and sign conventions; (ii) whether the extraction of quotient variables a, rho, connection, charge, Q and K_X is invariantly correct; (iii) whether the initial Taylor conclusions H_n=2, sigma_nn=6+Q, a_nn=-(4+Q) (as the data suggest), and coordinate-charge conservation follow analytically; (iv) whether the short-resolution results at n=0.02 genuinely support a local exact continuation or are numerical artifacts; (v) whether the R_X numerator cancellation is an independent validation of the Noether pairing or merely an integration identity; and (vi) what exact finite-dimensional/joint-matching object should be constructed next from this center, without reverting to radial flat-slice models or assuming a bounded transition. Identify any errors precisely and derive corrected formulas where possible.

## Integrated Scientific Memo

# Step 96 核验结论

## 1. Gaussian 演化方程与符号

令
\[
g=dn^2+q_{ij}(n,s)\,dy^i dy^j,\qquad
K=\frac12q_n,\qquad W=q^{-1}K,\qquad H=\operatorname{tr}W .
\]
则
\[
\operatorname{Ric}_{nn}=-H_n-|W|^2,
\]
\[
\operatorname{Ric}_{ni}=(\operatorname{div}_qK-dH)_i,
\]
以及
\[
\operatorname{Ric}_{ij}(g)
=\operatorname{Ric}_{ij}(q)-K_{ij,n}-HK_{ij}
+2(Kq^{-1}K)_{ij}.
\]
因此 \(\operatorname{Ric}_g=-3g\) 等价于
\[
\boxed{q_n=2K},
\qquad
\boxed{K_n=\operatorname{Ric}(q)+3q-HK+2Kq^{-1}K},
\]
辅以约束
\[
\boxed{R(q)-H^2+|W|^2=-6},\qquad
\boxed{\operatorname{div}_qK-dH=0}.
\]
脚本中的演化、Hamilton 约束及动量约束的符号和指标顺序均正确。等价的二阶形式为
\[
q_{nn}=2\operatorname{Ric}(q)+6q-Hq_n+q_nq^{-1}q_n.
\]

这里的 Cauchy 问题虽非双曲型且数值正向演化病态，但方程对 \(q_{nn}\) 已解析解出；Step 94 的周期初值是解析的并满足约束。因此 Cauchy–Kowalevski 给出一个唯一的周期解析局部解，Bianchi 恒等式传播其余 Einstein 分量。**局部精确 Einstein 延拓本身是解析定理，不依赖 \(n=0.02\) 的计算。**

反转法向使 \(K\mapsto-K\)。在 \(H=0\) 的中心，以两侧各自向外法向计，\(H_n\) 保持相同。

---

## 2. 商变量：正确部分及需要限定之处

将切片度量写为
\[
q=a^2ds^2+
G_{ab}(dx^a+\mathcal A_s^a ds)(dx^b+\mathcal A_s^b ds),
\]
并记 \(v_a=q_{as}\)，则
\[
G=q|_{\mathrm{Vert}},\qquad
\mathcal A_s=G^{-1}v,\qquad
a^2=q_{ss}-v^TG^{-1}v.
\]
脚本的 Schur 补提取正确。Gaussian/temporal gauge 中 \(\mathcal A_n=0\)，故
\[
F_{ns}=\partial_n\mathcal A_s,\qquad
\partial_n\mathcal A_s
=G^{-1}(v_n-G_n\mathcal A_s).
\]
商基度量为 \(dn^2+a^2ds^2\)，所以正交标架中的曲率系数是
\[
f=\frac{\partial_n\mathcal A_s}{a}.
\]
再令
\[
\rho=\sqrt{\det G},\qquad \sigma=\log\rho,\qquad M=\rho^{-1}G,
\]
则
\[
c=\rho Gf,\qquad
Q=\frac12f^TGf
=\frac12c^T\!\left(e^{-3\sigma}M^{-1}\right)c,
\]
并且
\[
e^{-3\sigma}M^{-1}=\rho^{-2}G^{-1},\qquad
d\mu_\sigma=\rho a\,dn\,ds.
\]
因此代码中的 `charge`、`Q`、`Amat` 和加权测度均正确。

但应明确：

* \(\mathcal A_s\) 本身依赖 gauge；`connection_abs_max` 不是不变量。其法向导数只是在当前 temporal gauge 中直接代表曲率。
* \(c\) 的整体符号依赖基底定向；当前代码得到 \(c=-\mathfrak q\)，而 metadata 记录的是 \(\mathfrak q\) 的正幅度，并不矛盾。
* \(c\) 的分量依赖固定的环面格基；不变陈述是 \(dc=0\)。
* `sqrt(max(...,0))` 会在长程计算中掩盖 \(a^2\) 或 \(\det G\) 失正。短程数据中最小特征值仍为 \(0.127\)，故尚未触发。

### `relative_KX` 中一个明确错误

脚本定义
\[
C_n=M^{-1}M_n=G^{-1}G_n-\sigma_n I.
\]
由于 \(n\) 已是商基上的单位坐标，
\[
|U_n|_h^2=\frac12\operatorname{tr}(C_n^2),
\]
**没有 \(a^{-2}\)**。故
```python
Un2=.5*np.einsum("nij,nji->n",Cn,Cn)/(a*a)
```
应改为
```python
Un2=.5*np.einsum("nij,nji->n",Cn,Cn)
```
而
```python
dUX=abs(ch)*sqrt(Un2)
```
保持不变。\(a^{-2}\) 只应出现在 \(s\)-方向导数的范数中。因短程内 \(a=1+O(10^{-3})\)，该错误对已报告分母影响很小，但概念上必须修正。

此外，当前分母并非 Noether 右侧的精确对偶范数。若以
\[
|H|,\ |T|,\ |Z|\le\varepsilon
\]
估计二维商空间中的 Noether 配对，自然权重至少为
\[
2|\operatorname{sym}\nabla X|
+\sqrt2\,|\operatorname{div}_\sigma X|
+|\operatorname{div}X|
+|dU(X)|.
\]
当前分母遗漏了前两项系数 \(2,\sqrt2\)，故 \(R_X\) 只是归一化诊断量，不是严格算子范数比。

---

## 3. 中心 Taylor 系数的解析推导

中心数据满足
\[
H=0,\qquad |W|^2=P+Q=S.
\]

### 平均曲率

由法向 Einstein 方程
\[
-H_n-|W|^2=-3
\]
得到
\[
\boxed{H_n=3-S}.
\]
本次 \(S=1\)，所以
\[
\boxed{H_n=2}.
\]

等价地，利用演化和 Hamilton 约束可得一般点态公式
\[
H_n=3-|W|^2.
\]

### 基尺度

中心内蕴度量为 \(ds^2+M(s)_{ab}dx^adx^b\)，且
\[
\operatorname{Ric}_{ss}(q_\Sigma)
=-\frac12|U_s|^2=-6-S.
\]
又因混合 Weingarten 块 \(m=-\mathfrak q/2\)，
\[
(Kq^{-1}K)_{ss}=m^TM^{-1}m=\frac Q2.
\]
于是
\[
(K_n)_{ss}=-6-S+3+Q=-3-S+Q,
\]
\[
(q_{ss})_{nn}=-6-2S+2Q.
\]
中心 \(v=0\)，且
\[
v_n=2K_{as}=-\mathfrak q,\qquad
v_n^TM^{-1}v_n=2Q.
\]
由
\[
a^2=q_{ss}-v^TG^{-1}v
\]
得
\[
(a^2)_{nn}=-6-2S-2Q.
\]
因 \(a=1,\ a_n=0\)，
\[
\boxed{a_{nn}=-3-S-Q}.
\]
本次 \(S=1\)，故
\[
\boxed{a_{nn}=-(4+Q)}.
\]

### 轨道面积

切片体积密度为 \(a\rho\)，从而
\[
H=\partial_n\log(a\rho)=\frac{a_n}{a}+\sigma_n.
\]
中心 \(a_n=\sigma_n=0\)，所以
\[
H_n=a_{nn}+\sigma_{nn}.
\]
代入上式：
\[
\boxed{\sigma_{nn}=6+Q}.
\]

因此
\[
H=2n+O(n^2),
\]
\[
a=1-\frac12(4+Q)n^2+O(n^3),
\]
\[
\sigma=\frac12(6+Q)n^2+O(n^3),\qquad
\rho=1+\frac12(6+Q)n^2+O(n^3).
\]
中心离开后，基圆方向收缩、环面轨道面积膨胀，而其和给出 \(H_n=2\)。

### 坐标荷守恒

中心
\[
\partial_n\mathcal A_s=M^{-1}v_n=-M^{-1}\mathfrak q,
\]
故
\[
c=\rho Gf=-\mathfrak q,
\]
沿 \(s\) 精确常值。混合 Einstein 方程进一步给出整个连通解析 germ 上
\[
\boxed{dc=0},
\]
即同时有 \(c_s=c_n=0\)。数据中的
\[
\max|c_n|\approx9.8\times10^{-14}
\]
只是浮点残差。

注意物理量 \(Q=\frac12c^T\rho^{-2}G^{-1}c\) 不必守恒；其变化来自 \(\rho\) 和 \(M\) 的演化，这与数据一致。

---

## 4. \(n=0.02\) 结果的实际证据强度

二阶 Taylor 预言与 \(N=96\) 数据定量一致：

\[
\rho(0.02)\approx
1+\frac12(6+Q)(0.02)^2
\in[1.0012017,1.0013000],
\]
而计算得到
\[
[1.0012022,1.0013013].
\]

\[
a(0.02)\approx
1-\frac12(4+Q)(0.02)^2
\in[0.99910,0.999198],
\]
而计算得到
\[
[0.9990785,0.9991693].
\]

初始
\[
\max|\mathcal A_{s,n}|=2.75946
\]
预言
\[
\max|\mathcal A_s(0.02)|\approx0.05519,
\]
计算值为 \(0.05573\)。

约束残差随分辨率显著下降：
\[
\begin{array}{c|ccc}
N&48&64&96\\ \hline
\|\mathcal H\|_\infty
&8.32\!\times10^{-2}&9.96\!\times10^{-3}&1.32\!\times10^{-4}\\
\|\mathcal M\|_\infty
&5.79\!\times10^{-2}&1.01\!\times10^{-2}&2.29\!\times10^{-4}
\end{array}
\]
且 \(Q_{\max}(0.02)\) 在 \(N=64,96\) 间已稳定到约 \(4\times10^{-7}\)。

不过 \(N=96\) 的初始动量残差已经是 \(2.09\times10^{-4}\)，末端为 \(2.29\times10^{-4}\)；大部分并非演化中产生，而是初始谱离散误差。Hamilton 残差则从 \(10^{-11}\) 增至 \(1.3\times10^{-4}\)，反映滤波半离散演化误差。

结论应严格表述为：

* 数据可信地追踪了已有解析 germ 的极短程 Taylor 演化；
* 没有迹象表明在 \(0\le n\le0.02\) 上发生高频数值灾难；
* 它们不构成局部存在证明——局部存在已由解析理论给出；
* 它们不支持任何 \(O(1)\) 法向距离的延拓、完整性、cusp 形成或两端匹配结论。

若要把数值证据做成真正的收敛研究，应比较不同 \(N\) 解投影到共同 Fourier 模式后的场范数，并同时运行 filtered/unfiltered、\(N=128,160\) 版本；仅比较约束最大值还不够。

---

## 5. \(R_X\) 分子消失不是 Noether 恒等式的独立验证

令
\[
A=e^{-3\sigma}M^{-1},\qquad
Q=\frac12c^TAc,\qquad
m_c=c^T A\,dc.
\]
对任意 \(X\)，
\[
X(Q)=m_c(X)+\frac12c^TX(A)c.
\]
定义
\[
K_X=X(A)+(\operatorname{div}_\sigma X)A,
\]
便有点态恒等式
\[
\boxed{
\frac12c^TK_Xc
=\operatorname{div}_\sigma(QX)-m_c(X)}.
\]
若 \(X\) 在边界消失，
\[
\frac12\int c^TK_Xc\,d\mu_\sigma
=-\int m_c(X)\,d\mu_\sigma.
\]
而本次精确 germ 上 \(dc=0\)，故
\[
\frac12c^TK_Xc=\operatorname{div}_\sigma(QX),
\qquad
\int\frac12c^TK_Xc\,d\mu_\sigma=0.
\]
这对任意度量都只是“固定荷 \(+\) 分部积分”的结论，不需要 Einstein 方程，更不需要水平 Bianchi/Noether 恒等式。

这也解释了切片值在 \(n=0.005\) 和 \(0.015\) 分别约为
\[
252.75,\qquad -254.55,
\]
但整体积分仅为 \(10^{-9}\)：主要是端点消失的加权散度发生正负抵消。分子在
\[
7.93,\ 2.34,\ 2.66\times10^{-9}
\]
之间也未随分辨率单调下降，符合时间求积/ODE 容差底噪，而非一个独立几何泛函的谱收敛。

因此该实验最多验证：

1. \(K_X\) 的分部积分实现；
2. 短程内数值荷近似守恒。

它**没有独立验证 Noether 恒等式的非平凡部分**。真正的三方核验应分别、独立编码并比较
\[
-\frac12\int c^TK_Xc\,d\mu_\sigma,
\]
\[
\int m_c(X)\,d\mu_\sigma,
\]
和
\[
\int\!\left[
2H:\operatorname{sym}\nabla X
-(\operatorname{tr}H)\operatorname{div}_\sigma X
+T\operatorname{div}X
-\langle Z,dU(X)\rangle
\right]d\mu_\sigma.
\]
并应使用具有 \(s\)-依赖、法向和切向分量的多个 \(X\)，以及 \(H,T,Z,dc\) 真正非零但由同一度量产生的 defect geometry。

---

## 6. 下一步应构造的精确联合匹配对象

纯 Einstein 延拓不能从这个中心接到 OT 开集：中心
\[
c_\Sigma=-\mathfrak q\ne0,
\]
而精确 Einstein 区域满足 \(dc=0\)。所以需要研究的不是更长的纯 Cauchy marching，而是一个保留全部 \(s\)-依赖的、**两侧联合的有限维 Lyapunov–Schmidt/Fredholm 匹配映射**。

取小的精确 Koiso 中心 collar \(|n|\le\varepsilon\)，两侧接
\[
B_{\pm,L_\pm}=[\varepsilon,L_\pm]\times S^1,
\]
其中 \(L_\pm\) 是自由参数，不能预设有界。未知场保留完整形式
\[
Y=(a,\sigma,M,\mathcal A_s)
\]
及相应 gauge-fixed 全部二维商方程。消去无限维余补后，有限维匹配映射至少应含：

### 6.1 向量荷通量

每侧两分量条件
\[
c_{\rm OT}-c_\Sigma
=\int_{\gamma_\pm}dc
=2\int_{\gamma_\pm}\rho\,
E(J\dot\gamma_\pm,V)\,dr\in\mathbb R^2,
\]
定向符号需统一。两端 \(c_{\rm OT}=0\)，故这正是产生并消灭中心非零荷所需的 defect 通量。

### 6.2 水平 Noether 余核矩

对线性化算子伴随余核的一组基 \(X_j^\pm\)，加入
\[
\int_{B_{\pm,L_\pm}}\!\left[
2H:\operatorname{sym}\nabla X_j
-(\operatorname{tr}H)\operatorname{div}_\sigma X_j
+T\operatorname{div}X_j
-\langle Z,dU(X_j)\rangle
\right]d\mu_\sigma
+\frac12\int c^TK_{X_j}c\,d\mu_\sigma=0.
\]
这是总荷通量之外的第二类加权矩；Step 94 的 redshift taper 已证明，仅凭 Maxwell、面积方程和两端零荷不足以控制中心荷。

### 6.3 平坦连接的 holonomy

当外端 \(F\to0\) 时还需匹配
\[
\oint_{S^1}\mathcal A_s\,ds
\quad \bmod \text{torus lattice}.
\]
\(\mathcal A_s\) 点态依赖 gauge，但该 holonomy 是残留的全局匹配数据。

### 6.4 外端 Jacobi 模式

将 strip 的外端 Cauchy 数据与所选精确 OT collar 家族匹配，并投影到求解无限维余补后剩余的 kernel/cokernel 模式。中心两侧共享
\[
(S,\mathfrak q,U\text{-phase},M\text{-frame})
\]
等参数，故必须联合求解，不能把两侧独立调整后再拼接。

中心严格稳定性
\[
\mathcal J(\phi)
=\int\bigl(|\nabla\phi|^2+(3-S)\phi^2\bigr),
\qquad 3-S=2,
\]
应进入该 Fredholm/余核分析；它是当前中心提供、径向平切片模型没有利用的真正强制性结构。

尚未确定的精确数学对象是：对这一 gauge-fixed、全 \(s\)-依赖 strip 问题，线性化算子的 Fredholm 边界条件、kernel/cokernel 的维数及其自然基。只有确定这些后，才能写出真正有限维的联合匹配映射并判断：

* 是否存在由同一度量生成的分布式、变号 defect \(E\)，使荷通量、水平矩、holonomy 和端 Jacobi 数据同时匹配且 \(\|E\|_\infty\to0\)；或
* 中心的 Jacobi coercivity 强迫这些匹配量之一具有与长度无关的正下界。

不得把 \(dc,H,T,Z\) 当作独立可指定源；它们必须来自同一度量，并由 Bianchi/Noether 恒等式耦合。这个联合 Fredholm 匹配问题才是从 charged-Koiso 中心自然得到的下一有限维对象。
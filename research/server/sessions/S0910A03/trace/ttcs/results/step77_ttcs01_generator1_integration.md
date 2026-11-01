# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 77,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step77_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step77_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Consider the following mathematical problem arising in the negative branch of Yau Problem 26.

We seek a complete, non-ASD Einstein metric on ℝ × T³ with Ric = -3g that has two Poincaré-Einstein (PE) ends and a totally geodesic T³ center (equivalently, a reflected half-core on [0,∞) × T³ with S(0)=0 and PE at infinity). The ASD obstruction rules out Li-Liu-type fillings. The conformal infinity satisfies R_γ < -12.

Generate concrete mathematical mechanisms or structural arguments addressing:

(A) EXISTENCE/NON-EXISTENCE: Are there known results about non-ASD PE Einstein metrics on (0,∞) × T³? Anderson's boundary theory gives Fredholm index 0 for the PE boundary map. For the Li-Liu ASD sector, the Toda equation uniquely determines the filling. What is the dimension of the non-ASD moduli? Is there a parity or topological argument for/against non-ASD fillings?

(B) FORWARD EVOLUTION: From center data (q₀, S=0) with R(q₀)=-6 on T³, the Einstein evolution is well-posed after DeTurck gauge-fixing. Under what conditions does the forward evolution produce a PE end (rather than a singularity)? The pure cosh warped product requires Ric(q₀) = -2q₀, impossible on T³ by Preissmann. So the evolution is genuinely anisotropic. What structural conditions on q₀ control the long-time behavior?

(C) OBSTRUCTION MECHANISMS: Could a Bochner-type, index-theory, or topological argument prove that NO reflected Einstein core exists on ℝ × T³? The Witten-Yau one-endedness doesn't apply (negative Yamabe). The integrated shear identity R_γ = -12 - 4∫e^{2r}|S-I|²dr provides quantitative constraints. Is there a global monotonicity or Pohozaev-type identity that separates reflected centers from PE ends?

(D) DEFECT-BASED ALTERNATIVE: If no exact reflected core exists, could a family of approximate Einstein metrics with defect → 0 still work for the graph construction? The tail mechanism can flatten anisotropy at vanishing cost. If an exact obstruction exists, it might not extend to approximate metrics (analogous to how nearby Einstein metrics don't exist but the manifold might carry a distant Einstein metric).

Develop the most promising ideas with concrete mathematical content, equations, and testable predictions.

## Integrated Scientific Memo

## 综合结论

目前材料既没有构造出所需的双 PE、反射对称 Einstein 核，也没有给出非存在证明。最可靠的结论是：

1. 所需解若存在，必为 genuinely non-ASD，并且不能由 Li–Liu ASD 填充作小的“反射截断”得到。
2. Anderson 的指数零理论只给局部 Fredholm 结构：固定正则边界共形类时填充通常离散；它不提供存在性、奇偶性或非零 degree。
3. 中心数据与 PE 数据形成一个维数平衡的无限维射击问题，而非明显过定问题：
   \[
   (q_0,\ S(0)=0,\ R(q_0)=-6)\longmapsto(\gamma,g_3).
   \]
4. 可从已有恒等式严格加强边界标量约束：
   \[
   \boxed{R_\gamma<-24}
   \]
   对中心距离 \(r\) 所选定的 canonical boundary representative 成立；此前的 \(R_\gamma<-12\) 非最优。
5. 精确解的主要未知量是中心产生的 anisotropic stress 能否无奇点地散射为允许的 \(g_3\)。小缺陷构造则可能绕过任何精确积分障碍，因为指数权重可把点态趋零的缺陷积累为有限的重整化通量。

---

# A. 非 ASD 填充的模空间与拓扑

## 1. 正确的自由度计数

四维 PE Einstein 展开为
\[
g=dr^2+e^{2r}\left(
\gamma-\operatorname{Sch}(\gamma)e^{-2r}
+g_3e^{-3r}+O(e^{-4r})
\right),
\]
其中
\[
\operatorname{tr}_\gamma g_3=0,\qquad
\operatorname{div}_\gamma g_3=0.
\]

三维边界度量模掉微分同胚和共形缩放后具有两个局部函数自由度。\(g_3\) 也是 TT、形式上具有两个局部函数自由度，但对真实填充它不是独立边界数据，而是非线性 Dirichlet-to-Neumann 响应。

因此 Anderson 边界映射
\[
\Pi:\mathcal E_{\rm PE}\longrightarrow \mathcal C(T^3)
\]
的 Fredholm 指数为零意味着：

- 在非退化点，固定 \([\gamma]\) 的填充局部离散；
- 允许 \([\gamma]\) 变化时，填充模空间与边界共形类具有相同的函数维数；
- 若 gauged Lichnerowicz 核非零，则可能有分岔或正维固定边界纤维；
- 指数零本身不蕴含 surjectivity、非零 degree 或存在性。

中心一侧同样维数平衡：\(q_0\) 有六个分量，模掉三维微分同胚并施加
\[
R(q_0)=-6
\]
后，仍剩两个局部函数自由度。故中心到 PE 的匹配不是由朴素维数或 parity 排除的。

## 2. ASD 部分只是特殊的 chiral sheet

ASD 填充中 \(g_3\) 由边界局部共形数据（等价地 Cotton–York 型张量，具体常数依约定）所约束。一般非-ASD 填充则没有此局部约束。Li–Liu 的 Toda 唯一性只描述其 ASD、一个 PE 端加一个 cusp 端的特殊族，不能决定双 PE 拓扑上的一般填充模空间。

反射中心直接排除 ASD。反射是 orientation-reversing local isometry，交换 \(W^+\) 与 \(W^-\)。若一侧 ASD，则反射后同时迫使另一 chirality 消失；Einstein 解析性给出 \(W=0\)，从而曲率恒为 \(-1\)。 totally geodesic \(T^3\) 将继承恒负曲率，这与其基本群 \(\mathbb Z^3\) 不相容。

所以 Li–Liu 可作为 PE/cusp 外端与 DtN 响应的基准，但不能被直接切开反射，也不能作为反射核附近的 ASD 扰动模型，除非首先找到一个改变端型的非-ASD Jacobi 模。

## 3. 拓扑积分公式不是现成障碍

对完整 doubled manifold \(M\simeq\mathbb R\times T^3\)，
\[
\chi(M)=0,\qquad \tau(M)=0.
\]
若标准 AH Einstein 重整化 Gauss–Bonnet 公式在该双端设定下适用，则
\[
0=8\pi^2\chi(M)
=\int_M|W|^2\,dV+6V_{\rm ren},
\]
故
\[
V_{\rm ren}=-\frac16\int_M|W|^2\,dV<0.
\]
反射还给出
\[
\int_M|W^+|^2\,dV=\int_M|W^-|^2\,dV.
\]

这些是必要条件，不是矛盾。使用它们时需要核对双 PE 端的重整化约定和可能的端项；现有材料没有给出一个 \(V_{\rm ren}\ge0\) 定理。因此不能声称拓扑或 parity 已排除 mixed-Weyl 填充。

最具体的线性测试是研究 Li–Liu cusp 背景上 gauged Einstein 算子的非-ASD、反射偶 Jacobi 场：

- 若存在改变第二端型、并改变 \(g_3\) 离开 ASD sheet 的模，可能产生 cusp-opening 机制；
- 若该核为零，只能排除 Li–Liu 附近的小变形，不能排除有限振幅反射核。

---

# B. 从中心到 PE 端的“演化”

## 1. 这不是通常意义的适定时间演化

Gaussian gauge 中
\[
q_r'=2q_rS,
\]
\[
S'+HS=\operatorname{Ric}(q_r)^\sharp+3I,
\]
并满足
\[
H'=3-|S|^2,
\]
\[
R(q_r)+|S|^2-H^2=-6,\qquad
\operatorname{div}_{q_r}S=dH.
\]

中心条件为
\[
S(0)=0,\qquad R(q_0)=-6,
\]
且
\[
S'(0)=\operatorname{Ric}(q_0)^\sharp+3I,
\]
\[
q_r=q_0+r^2(\operatorname{Ric}(q_0)+3q_0)+O(r^4).
\]

但 Riemannian Einstein 方程在切向变量上本质为椭圆系统。DeTurck gauge 给出椭圆边值问题，而不是稳定的抛物型 forward flow。高频模式
\[
\psi_k''+3\psi_k'-k^2e^{-2r}\psi_k=0,\qquad
\psi_k(0)=1,\quad\psi_k'(0)=0
\]
满足
\[
\psi_k(\infty)=\frac{\sinh k}{k},\qquad
e^{2r}\psi_k'(r)\to k\sinh k.
\]
所以中心到无穷远的射击映射随频率指数恶化。解析或 Gevrey 正则性、而非仅 \(C^\infty\) Sobolev 控制，很可能是对称约化射击中的自然函数空间。

## 2. 归一化动力学及 PE 判据

置
\[
u=3-H,\qquad P=S-\frac H3I,\qquad \bar q_r=e^{-2r}q_r.
\]
则
\[
S-I=P-\frac u3I,
\]
并有
\[
\bar q_r'=2\bar q_r\left(P-\frac u3I\right),
\]
\[
u'=|P|^2+\frac{u^2}{3}-2u,
\]
\[
P'+(3-u)P=e^{-2r}\operatorname{Ric}(\bar q_r)^{\circ\sharp},
\]
以及
\[
e^{-2r}R(\bar q_r)
=-4u+\frac23u^2-|P|^2.
\]

PE 端要求
\[
\bar q_r\to\gamma
\]
在适当 Hölder/Sobolev 范数中非退化收敛，并且
\[
u=-\frac{R_\gamma}{4}e^{-2r}+O(e^{-4r}),
\]
\[
P=\operatorname{Ric}(\gamma)^{\circ\sharp}e^{-2r}
-\frac32\gamma^{-1}g_3e^{-3r}+O(e^{-4r}).
\]

因此一组可检验的充分型 bootstrap 条件是：

- \(\bar q_r\) 一致椭圆、预紧，且不发生 torus cycle collapse；
- \(u>0\) 最终较小，且 \(\int e^{2r}|S-I|^2dr<\infty\)；
- \(e^{-2r}\operatorname{Ric}(\bar q_r)^\circ\) 可积到足以控制 \(P\)；
- momentum constraint 持续满足；
- 所有归一化切向曲率及其必要导数有界。

单独的 expansion \(H\to3\) 不够：若 \(\bar q_r\) 退化或 \(e^{-2r}|\operatorname{Ric}(\bar q_r)|\) 不受控，仍可能形成 cusp 或有限距离奇点。

## 3. 中心结构给出的风险

在 \(T^2\)-cohomogeneity-one 类
\[
q_0=ds^2+G(s)_{ab}dx^adx^b
\]
中，已有严格结果：
\[
\lambda_{\min}S'(0)\le-3.
\]
由于
\[
\operatorname{tr}S'(0)=3,
\]
中心必有强烈各向异性初始加速度。相关能量恒等式为
\[
\int\rho|A_0|^2
=6\int\rho+\frac12\int\rho h^2,
\]
故对角变量 \(d\) 满足
\[
\langle d_s^2\rangle_\rho\ge12.
\]

最温和的候选中心应尽量使 \(h\approx0\)，并使 orbit-shape map 的能量密度接近均匀，而不是把能量集中在少数点。更一般地写
\[
G=\rho U,\qquad
U:S^1\to SL(2,\mathbb R)/SO(2),
\]
可允许收缩特征方向在两个 torus 周期间旋转，从而分散累计应变。这是纯对角 \(d=b-c\) 模型没有的真实自由度，但目前没有证明它足以防止 collapse。

一个直接数值/解析判据是沿解监测归一化 torus block 的最小特征值以及
\[
\inf_{r,z}\lambda_{\min}(\bar q_r).
\]
若该量趋零，则端更接近 cusp/退化而非 PE；若保持正下界并同时满足上述加权曲率估计，则有希望进入 PE bootstrap。

---

# C. 更强的精确单调性与障碍候选

## 1. 边界标量的尖锐改进

由
\[
H'=3-|S|^2,\qquad |S|^2\ge \frac{H^2}{3},
\]
并与
\[
y'=3-\frac{y^2}{3},\qquad y(0)=0
\]
比较，得
\[
H(r)\le3\tanh r.
\]
于是
\[
3-H(r)\ge3(1-\tanh r).
\]
又 PE 展开给出
\[
-\frac{R_\gamma}{4}
=\lim_{r\to\infty}e^{2r}(3-H(r)).
\]
由于
\[
\lim_{r\to\infty}e^{2r}\,3(1-\tanh r)=6,
\]
得到
\[
R_\gamma\le-24.
\]

等号条件迫使 Cauchy–Schwarz 全程取等，即 \(S\) 纯迹。于是
\[
g=dr^2+\cosh^2r\,q_0,\qquad
\operatorname{Ric}(q_0)=-2q_0,
\]
这在 \(T^3\) 上不可能。因此
\[
\boxed{R_\gamma<-24}.
\]

这里 \(R_\gamma\) 指由中心距离 \(\rho=e^{-r}\) 确定的 boundary representative 的点态标量；它不是整个共形类的共形不变量。

这与已有恒等式
\[
-\frac{R_\gamma}{4}
=3+\int_0^\infty e^{2r}|S-I|^2dr
\]
结合，给出新的严格下界
\[
\boxed{\int_0^\infty e^{2r}|S-I|^2dr>3}.
\]

## 2. 精确的 Fuchsian-defect 分解

令
\[
w(r)=3(1-\tanh r),\qquad z=u-w.
\]
由于
\[
u'=|P|^2+\frac{u^2}{3}-2u,\qquad
w'=\frac{w^2}{3}-2w,
\]
有
\[
z'=\left(\frac{u+w}{3}-2\right)z+|P|^2,\qquad z(0)=0.
\]
因此
\[
z(r)=\int_0^r
\exp\!\left[
\int_s^r\left(\frac{u(t)+w(t)}3-2\right)dt
\right]|P(s)|^2ds\ge0.
\]
故
\[
-\frac{R_\gamma}{4}
=
6+\lim_{r\to\infty}e^{2r}z(r).
\]

这是真正把 Fuchsian warped case 与 anisotropic core 分开的 Pohozaev 型量。若能证明非平凡中心数据使最后极限具有某个不可与 PE 数据兼容的下界或张量符号，即可得到非存在；目前只得到严格正性，而负 Yamabe \(T^3\) 边界可以容纳任意负的标量，故尚无矛盾。

## 3. 各向异性方程中的 Weyl 源

traceless Riccati 方程可写成
\[
P'+\frac{2H}{3}P=-(P^2)_0-\mathcal W_n,
\]
其中
\[
\mathcal W_n=W(\,\cdot,n,\cdot,n\,)_0.
\]
配对 \(P\) 得
\[
\frac12(|P|^2)'
=-\frac{2H}{3}|P|^2-\operatorname{tr}(P^3)
-\langle\mathcal W_n,P\rangle.
\]

因此任何真正的精确障碍必须控制 electric Weyl 与 shear 的全局配对；单独控制 \(H\) 或 \(\int|W|^2\) 通常不足。值得寻找的是带 PE 权重的恒等式，例如对上述方程乘 \(e^{\alpha r}\)，再结合 Bianchi 方程消去 \(\mathcal W_n'\)，看是否得到由中心 \(\operatorname{Ric}(q_0)^\circ\) 与边界 \(g_3\) 控制的边界项。

## 4. 基本 Bochner 与 minimal-hypersurface 路线不产生矛盾

totally geodesic 中心的稳定二次型为
\[
Q(\varphi)
=\int_{T^3}\bigl(
|\nabla\varphi|^2
-(\operatorname{Ric}(n,n)+|S|^2)\varphi^2
\bigr)
=\int_{T^3}(|\nabla\varphi|^2+3\varphi^2)>0.
\]
因此中心是严格稳定最小超曲面；稳定性支持局部非退化，而不排除存在。环境 Ricci 和 scalar 均为负，基本 harmonic one-form 或 Dirac Bochner 公式也没有所需的正号。

## 5. 对称约化中最有希望的精确对象

在 \(T^2\)-对称情形，可把 orbit block 写成
\[
G=\rho U,\qquad U\in SL(2,\mathbb R)/SO(2).
\]
其 anisotropy 方程具有加权 harmonic-map 形式
\[
\operatorname{div}(\rho\,U^{-1}dU)=0
\]
（精确系数和 quotient conformal factors 应由完整 Einstein reduction 再推导，不能只依“schematic” dilaton 方程）。对角情形退化为
\[
\operatorname{div}(\rho\nabla d)=0.
\]

已知有限柱面恒等式为
\[
F_c(R)
=\int_{[0,R]\times S^1}\rho|\nabla d|^2,
\quad
F_c(R)=\int_{C_R}(d-c)\rho d_r.
\]
净 signed flux 恒为零，但 boundary covariance 承载全部能量。PE 端并不要求该 covariance 为零，所以这不是障碍。需要把它的无穷远极限精确表达成 \((\gamma,g_3)\) 的函数，再与中心能量下界配对；仅使用
\[
e^{2r}P\to\operatorname{Ric}(\gamma)^\circ
\]
会丢失填充信息，真正的非局部量是
\[
e^{3r}\left[P-\operatorname{Ric}(\gamma)^{\circ\sharp}e^{-2r}\right]
\to-\frac32\gamma^{-1}g_3.
\]

---

# D. 小缺陷替代路线

令
\[
E=\operatorname{Ric}+3g.
\]
符号一致地，由 \(E_{rr}\) 的定义可得
\[
u'=|P|^2+\frac{u^2}{3}-2u-E_{rr},
\]
而不是加号；等价地
\[
\bigl(e^{2r}(3-H)\bigr)'
=e^{2r}\bigl(|S-I|^2+E_{rr}\bigr).
\]
因此即使
\[
\|E\|_\infty\le\delta\to0,
\]
加权量仍可能是 order one：
\[
\int_0^R e^{2r}E_{rr}\,dr
=O(\delta e^{2R}).
\]
当
\[
R\sim\frac12\log(1/\delta)
\]
时已经不会趋零。

同样，CMC gauge 中
\[
(e^{3a}P)'
=e^a\operatorname{Ric}(q_r)^\circ-e^{3a}E_T^\circ.
\]
点态很小的 \(E_T^\circ\) 可以通过 \(e^{3a}\) 权重调节有限的 PE stress。因此精确单调性或精确无解定理通常不会自动给出点态 defect 的正下界。

可行的 defect 架构是：

1. **精确反射 germ：**
   \[
   S(0)=0,\qquad R(q_0)=-6,
   \]
   在短区间使用满足完整 constraints 的偶 Einstein jet。

2. **长 forced bridge：** 允许
   \[
   \|E\|_{\rm op}\le\delta,
   \]
   同时把 \(H\) 推向 \(3\)、\(P\) 推向 \(0\)，并控制
   \[
   e^{-2a}\|\operatorname{Ric}(q_r)\|.
   \]
   必须允许非零的重整化缺陷矩
   \[
   \int e^{2r}E_{rr}\,dr,\qquad
   \int e^{3a}E_T^\circ\,dr.
   \]

3. **adiabatic tail：** 一旦达到
   \[
   S=(1-\varepsilon)I+P,\qquad
   \varepsilon+\|P\|\ll1,
   \qquad e^{-2a}\|\operatorname{Ric}(q)\|\ll1,
   \]
   使用已有 tail lemma：
   \[
   \|\operatorname{Ric}+3g\|_{\rm op,\infty}
   \le C\left(
   \varepsilon+K^{-1}+K^{-2}+e^{-2a_0}
   \right).
   \]
   这可在 vanishing cost 下移除 order-one orbit anisotropy。

成功序列的清晰诊断信号应是
\[
\|E_j\|_\infty\to0
\]
但
\[
\int e^{2r}(E_j)_{rr}\,dr=O(1),\qquad
\int e^{3a}(E_j)_T^\circ\,dr=O(1).
\]
若反而能证明这些加权矩在所有允许几何下都随 \(\|E_j\|_\infty\) 一同趋零，才可能把精确障碍升级为 approximate obstruction；当前材料没有这样的紧性估计。

---

## 最有判别力的具体问题

1. **证明并利用 \(R_\gamma<-24\)：** 在数值/解析候选中核验 canonical infinity 的标量，而不是误把 \(\gamma\) 与 \(q_0\) 混同。
2. **计算真正的 scattering output：**
   \[
   (\gamma,g_3),\qquad
   g_3=-\frac23\lim e^{3r}
   \left[P-\operatorname{Ric}(\gamma)^{\circ\sharp}e^{-2r}\right].
   \]
3. **分析 Li–Liu cusp 上的非-ASD even Jacobi 核：** 这决定 cusp-opening 是否可能是小变形机制。
4. **建立完整 \(T^2\)-reduced Einstein–DeTurck 系统：** 保留 matrix-valued \(U\)、dilaton、Hamilton 和 momentum constraints；不能只解 scalar anisotropy equation。
5. **射击时监测三类量：**
   \[
   \lambda_{\min}(\bar q_r),\qquad
   e^{-2r}\|\operatorname{Ric}(\bar q_r)\|,\qquad
   e^{3r}\left[P-\operatorname{Ric}(\gamma)^\circ e^{-2r}\right].
   \]
   第一项区分 PE 与 collapse，第二项决定 damping 是否有效，第三项给出填充的非局部响应。
6. **对 defect 路线按加权矩而非仅 residual norm 记账。** 早先有限 Fourier 基底中 residual 停在约 \(16\) 只说明参数化未解析椭圆 jet cascade，不具有非存在意义。

精确问题最终归结为：中心约束产生的 matrix-valued anisotropic stress 是否落在某个非-ASD PE 边界映射的像中。近似问题则归结为：能否用长度趋于无穷的 forced bridge 实现相同的有限重整化 stress，同时令未加权 Einstein defect 一致趋零。
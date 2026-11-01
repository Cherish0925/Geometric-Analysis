# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 81,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step81_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step81_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following chain of results for the reflected Einstein evolution from T²-invariant constant-area centers on T³ with Ric=-3g:

1. ORBIT MATRIX PARAMETRIZATION: In SL(2,R)/SO(2) with metric ds²=(1/2)tr((M⁻¹dM)²), geodesic polar gives M=cosh(d)I+sinh(d)n(θ) with n=[[cosθ,sinθ],[sinθ,-cosθ]], n²=I. The metric is dd²+sinh²(d)dθ² (curvature -1). A rotating loop d=d*, θ=kz has energy k²sinh²(d*). Setting this to 12 gives R(q₀)=-6 for constant area.

2. S'(0) EIGENVALUES: The reflected Einstein germ has S(0)=0, S'(0)=Ric(q₀)+3I. For constant-area centers: the z-eigenvalue is -|A|²+3=-3 (universal). The orbit eigenvalues have trace 6 but split depending on k and d*. Numerical: k=2 gives orbit eigenvalues ≈(9.93,-3.93); k=8 gives ≈(18.09,-12.09). Derive the exact analytical formula for the orbit eigenvalues.

3. ANGULAR-SLIP ENERGY PRESERVATION: For the perturbation d=d*+εcos(k̃z), θ=k₀z+εB₀sin(k̃z)/k̃ with B₀=-(k₀/k̃)coth(d*), the H² speed² deviates from 12 by O(ε²) with coefficient ~20. Verify this cancellation analytically: what is the exact O(ε²) coefficient? Does the cancellation extend to the orbit Ricci components, not just the trace?

4. UNIVERSAL AVERAGE CONTRACTION: For ANY constant-area center with R(q₀)=-6: ⟨|A|²⟩=6, hence ⟨u'(0)⟩=-3. For non-constant area: ⟨u'(0)⟩=-3+⟨h²⟩. Is this derivation correct? What are the assumptions?

5. VII₀ COLLAPSE: The ODE evolution for the Bianchi VII₀ system shows finite-distance collapse at r≈0.3-0.4 for all k=2,...,8. The cascade is K>3→u'<0→a↓→K↑. Does this collapse persist in the z-dependent (non-VII₀) case? Specifically: if u'(0,z)=-3+O(ε²) everywhere (from result 3), can the z-dependent evolution avoid collapse through spatial redistribution?

6. IMPLICATIONS FOR GRAPH CONSTRUCTION: Does the collapse force O(1) Ricci defect near the center, preventing ||E||_∞→0? Or is there an escape through non-constant-area centers, non-OT geometry, or non-reflected metrics?

## Integrated Scientific Memo

## 核验结论

链条中的第 1、2 项成立；第 3 项需要修正振幅约定，而且“轨道 Ricci 分量也一阶抵消”不成立；第 4 项必须明确平均测度；第 5 项只在固定 Bianchi VII\(_0\) 类中可证明有限径向奇异，不能推广到一般 \(z\)-依赖系统；因此第 6 项目前只给出 VII\(_0\) 类中的 \(O(1)\) 缺陷下界，而非一般图流形构造的障碍。

---

## 1. 轨道矩阵与标量曲率

令
\[
n(\theta)=
\begin{pmatrix}
\cos\theta&\sin\theta\\
\sin\theta&-\cos\theta
\end{pmatrix}.
\]
则
\[
n^2=I,\qquad \operatorname{tr}n=0,
\]
并且
\[
M=\cosh d\,I+\sinh d\,n(\theta),\qquad
M^{-1}=\cosh d\,I-\sinh d\,n(\theta).
\]
\(M\) 的特征值为 \(e^{\pm d}\)，故它是正定、行列式为 \(1\) 的对称矩阵。直接计算得到
\[
\frac12\operatorname{tr}\bigl((M^{-1}dM)^2\bigr)
=dd^2+\sinh^2d\,d\theta^2.
\]
这是曲率
\[
-\frac{(\sinh d)''}{\sinh d}=-1
\]
的双曲平面度量。

对常面积中心
\[
q_0=dz^2+M_{ab}(z)d\xi^a d\xi^b,\qquad \det M=1,
\]
置
\[
Q=M^{-1}M_z,\qquad \mathcal A=\frac12Q.
\]
则
\[
|\mathcal A|^2=\frac14\operatorname{tr}(Q^2)
=\frac12|U_z|_{\mathbb H^2}^2,
\]
而平坦 \(T^2\) 轨道的 Gauss–Riccati 公式给出
\[
\operatorname{Ric}_{q_0}(\partial_z,\partial_z)
=-|\mathcal A|^2,\qquad
R(q_0)=-|\mathcal A|^2
=-\frac12|U_z|_{\mathbb H^2}^2.
\]
所以
\[
R(q_0)=-6
\quad\Longleftrightarrow\quad
|U_z|_{\mathbb H^2}^2=12.
\]

对旋转环
\[
d=d_*,\qquad \theta=kz,
\]
有
\[
|U_z|^2=k^2\sinh^2d_*,
\]
故
\[
\boxed{k^2\sinh^2d_*=12},
\qquad
d_*=\operatorname{arsinh}\frac{\sqrt{12}}{|k|}.
\]

注意：这里的双曲极角 \(\theta\) 是轨道特征标架旋转角的两倍；与 Step 78 的 VII\(_0\) 余标架频率比较时必须保留这一因子 \(2\)。

---

## 2. \(S'(0)\) 的精确谱

在 Gaussian 规范
\[
g=dr^2+q_r,\qquad S=\frac12q_r^{-1}\partial_rq_r
\]
下，切向 Einstein 方程为
\[
S'=\operatorname{Ric}(q_r)+3I-HS.
\]
反射中心满足 \(S(0)=H(0)=0\)，所以
\[
S'(0)=\operatorname{Ric}(q_0)+3I.
\]

### \(z\) 方向

常面积时
\[
\operatorname{Ric}_{zz}=-|\mathcal A|^2=-6,
\]
因此
\[
\boxed{\lambda_z(S'(0))=-3}.
\]

### 轨道方向

对 \(d=d_*,\theta=kz\)，轨道 Ricci 端同态的特征值为
\[
\pm L,\qquad
L=\frac{k^2}{2}\sinh d_*\cosh d_*.
\]
利用 \(k^2\sinh^2d_*=12\)，
\[
L=6\coth d_*
=\sqrt{3(k^2+12)}.
\]
故
\[
\boxed{
\operatorname{Spec}S'(0)=
\left\{
-3,\;
3+\sqrt{3(k^2+12)},\;
3-\sqrt{3(k^2+12)}
\right\}.}
\]

特别地，
\[
k=2:\quad 3\pm\sqrt{48}
=(9.928203\ldots,-3.928203\ldots),
\]
\[
k=8:\quad 3\pm\sqrt{228}
=(18.099669\ldots,-12.099669\ldots).
\]
`step81_evolution.json` 中略有偏差，是因为数值中心本身已有
\(\operatorname{Ric}_{zz}+6\neq0\) 的离散误差。

---

## 3. 角滑移：精确二阶项及张量层面的失败

记
\[
m=k_0,\qquad q=\widetilde k,\qquad
s=\sinh d_*,\quad c=\cosh d_*,
\qquad m^2s^2=12.
\]

### 3.1 题述振幅存在一个额外的 \(q^{-1}\)

题中写成
\[
\theta=mz+\varepsilon B_0\frac{\sin(qz)}q,
\qquad
B_0=-\frac mq\coth d_*.
\]
于是
\[
\theta_z=m+\varepsilon B_0\cos(qz),
\]
速度平方的一阶项为
\[
2\varepsilon m^2sc\left(1-\frac1q\right)\cos(qz).
\]
因此该表达只有在 \(q=1\) 时才一阶抵消。

一般 \(q\) 下正确的等价约定是二者之一：
\[
\theta=mz+\varepsilon b\sin(qz),
\qquad
b=-\frac mq\coth d_*,
\]
或
\[
\theta=mz+\varepsilon B\frac{\sin(qz)}q,
\qquad
B=-m\coth d_*.
\]

以下采用第一种。

### 3.2 精确的 \(O(\varepsilon^2)\) 系数

令
\[
d=d_*+\varepsilon\cos(qz),\qquad
\theta_z=m-\varepsilon m\coth d_*\cos(qz).
\]
由
\[
|U_z|^2=d_z^2+\sinh^2d\,\theta_z^2
\]
展开可得
\[
\boxed{
|U_z|^2
=
12+\varepsilon^2
\left[
q^2\sin^2(qz)-(2m^2+12)\cos^2(qz)
\right]
+O(\varepsilon^3).}
\]
等价地，负的余弦系数是
\[
-m^2(c^2+1)=-(2m^2+12).
\]

对数据所用 \(m=2,q=1\)，
\[
\boxed{
|U_z|^2-12
=
\varepsilon^2(1-21\cos^2z)+O(\varepsilon^3).}
\]
所以二阶系数范围为
\[
[-20,1],
\]
从而
\[
\boxed{
\lim_{\varepsilon\to0}
\frac{\|\,|U_z|^2-12\,\|_\infty}{\varepsilon^2}=20.}
\]
这解释了数据中的 \(20.0919\)：超过 \(20\) 的部分来自三阶及更高阶项。相应地
\[
u'(0,z)
=3-\frac12|U_z|^2
=-3-\frac{\varepsilon^2}{2}
\left[q^2\sin^2(qz)-(2m^2+12)\cos^2(qz)\right]
+O(\varepsilon^3).
\]
对 \(m=2,q=1\)，其圆周平均为
\[
-3+\frac{19}{4}\varepsilon^2+O(\varepsilon^3),
\]
与数据中的 \(-2.999525\) 一致。

### 3.3 抵消不延伸到轨道 Ricci 张量

设 \(t=\partial_\theta n\)、\(J=nt\)。对任意 \(d(z),\theta(z)\)，
\[
\begin{aligned}
Q'={}&(d''-\sinh d\cosh d\,\theta'^2)n\\
&+(2\cosh^2d\,d'\theta'
+\sinh d\cosh d\,\theta'')t\\
&-(2\sinh d\cosh d\,d'\theta'
+\sinh^2d\,\theta'')J .
\end{aligned}
\]
在上述正确滑移下，
\[
\begin{aligned}
Q'={}&-m^2sc\,n\\
&+\varepsilon\Big[
(m^2-q^2)\cos(qz)n
-mq c^2\sin(qz)t
+mqsc\sin(qz)J
\Big]
+O(\varepsilon^2).
\end{aligned}
\]
而
\[
\operatorname{Ric}_{\rm orb}=-\frac12Q'.
\]
因此轨道 Ricci 的无迹部分一般在 \(O(\varepsilon)\) 已变化；只有速度平方、标量曲率和 \(zz\) 分量的一阶变化被抵消。

所以应纠正为：

\[
\boxed{\text{角滑移一阶保持能量迹，但不一阶保持完整轨道 Ricci 张量。}}
\]

裸滑移还仅满足 \(R=-6+O(\varepsilon^2)\)。若要求精确 \(R=-6\)，必须加入二阶零模和 \(2q\) 模的面积/基底回作用。

---

## 4. 平均收缩公式及平均测度

取商圆的单位弧长 \(s\)，写
\[
q_0=ds^2+G_{ab}(s)d\xi^a d\xi^b,
\qquad
\mathcal A=\frac12G^{-1}\dot G,
\qquad
h=\operatorname{tr}\mathcal A
=\frac d{ds}\log\sqrt{\det G}.
\]
则
\[
\operatorname{Ric}_{q_0}(\nu,\nu)
=-\dot h-|\mathcal A|^2,
\]
\[
R(q_0)=-2\dot h-h^2-|\mathcal A|^2.
\]
若反射中心满足精确的 \(R(q_0)=-6\)，则
\[
u'(0,s)=3-\dot h-|\mathcal A|^2
=-3+\dot h+h^2.
\]

### 常面积

若 \(h\equiv0\)，则实际上有逐点恒等式
\[
|\mathcal A|^2=6,\qquad
\boxed{u'(0,s)=-3}.
\]
因此“平均为 \(-3\)”比真实结论更弱。

### 非加权单位弧长平均

定义
\[
\langle f\rangle_s=\frac1L\int_0^L f(s)\,ds.
\]
周期性给出 \(\langle\dot h\rangle_s=0\)，所以
\[
\boxed{
\langle u'(0)\rangle_s
=-3+\langle h^2\rangle_s.}
\]
若要求非负平均初始响应，则必须
\[
\langle h^2\rangle_s\ge3.
\]

### 中心体积加权平均

令
\[
\rho=\sqrt{\det G},\qquad
\langle f\rangle_\rho
=\frac{\int f\rho\,ds}{\int\rho\,ds}.
\]
由于 \(\dot\rho=h\rho\)，
\[
\langle\dot h\rangle_\rho=-\langle h^2\rangle_\rho.
\]
于是
\[
\boxed{\langle u'(0)\rangle_\rho=-3}
\]
对任意面积函数仍成立。

因此“非恒面积时为 \(-3+\langle h^2\rangle\)”只对非加权单位弧长平均成立，而不是几何体积平均。若 \(z\) 不是单位弧长，均匀 \(z\)-平均也不能直接代替它。

若写
\[
G=e^\sigma M,\qquad \det M=1,\qquad
e=\frac12\operatorname{tr}\bigl((M^{-1}\dot M)^2\bigr),
\]
则
\[
|\mathcal A|^2=\frac12h^2+\frac12e,
\]
精确标量约束等价于
\[
\boxed{e=12-4\dot h-3h^2\ge0.}
\]
因此非恒面积不是一个自由的正贡献；它必须与轨道形状能量满足上述逐点耦合。

`step81_contraction_analysis.json` 的 `nonconst_c*` 数据实际上是常面积、变速度的环，并未重新强制 \(R\equiv-6\)，故不能用来检验上述非恒面积公式。

所需假设是：光滑自由 \(T^2\) 作用、商空间为周期圆、单位水平弧长、平坦 \(T^2\) 轨道、精确反射 \(S(0)=0\)，以及精确的中心标量约束 \(R(q_0)=-6\)；若只假设平均标量为 \(-6\)，相应结论也只能取平均形式。

---

## 5. VII\(_0\) 的有限径向奇异与一般 \(z\)-依赖系统

固定 VII\(_0\) 方程中
\[
u'+Hu=3-K,\qquad
p'+Hp=2K\coth d,
\]
\[
(\log K)'=-2u+2\coth d\,p,
\]
反射数据给出
\[
K(0)=6,\qquad u<0,\quad p>0,\quad K>6.
\]
结合 normal 方程和 Hamilton 约束还得到
\[
\boxed{H'=9-H^2-K.}
\]

由于 \(K\ge6\)，
\[
H'\le3-H^2,
\qquad
H(r)\le\sqrt3\tanh(\sqrt3r)<\sqrt3.
\]
用积分因子处理 \(u\) 方程：
\[
-u(r)\ge
3\int_0^r
\exp\!\left(-\int_t^rH(s)\,ds\right)dt
\ge\sqrt3(1-e^{-\sqrt3r}).
\]
因此
\[
(\log K)'\ge-2u
\ge2\sqrt3(1-e^{-\sqrt3r}),
\]
所以 \(K\) 在有限半径超过 \(10\)。此后
\[
H'\le-1-H^2,
\qquad
(\arctan H)'\le-1,
\]
故 \(H\) 不可能在任意长的有限值区间上保持光滑。由此可严格推出：

\[
\boxed{\text{精确的固定 VII}_0\text{ 解具有有限最大径向区间。}}
\]

数据记录的端点为
\[
\begin{array}{c|ccccc}
k&2&3&4&6&8\\ \hline
r_{\max}&0.3624&0.3395&0.3160&0.2739&0.2407,
\end{array}
\]
即约 \(0.24\)–\(0.36\)，不是统一的 \(0.3\)–\(0.4\)。文件没有 \(k=5,7\) 的运行；\(r>r_{\max}\) 的表格值大多只是重复终止状态，并非继续积分。

### 不能推广到一般 \(z\)-依赖演化

一般反射 Einstein 演化满足
\[
H'=3-|S|^2,\qquad
R(q_r)=-6+H^2-|S|^2,
\]
即
\[
H'=9-H^2+R(q_r).
\]
VII\(_0\) 证明关键使用
\[
R(q_r)=-K
\]
以及单一势 \(K\) 的单调性。完整 OT 系统中，\(R(q_r)\) 同时含面积导数、矩阵映射能量及空间导数，没有已知的对应单调 \(K\)。

即使
\[
u'(0,z)=-3+O(\varepsilon^2)
\]
逐点成立，也只确定
\[
u(r,z)=-3r+O(r^3)
\]
的首个径向系数。更重要的是，第 3 项表明轨道 \(S'(0)\) 已在 \(O(\varepsilon)\) 改变，故空间再分配可以在比 \(u'\) 的二阶变化更早的阶数进入后续反馈。

完整轨道方程
\[
\operatorname{div}\bigl(\rho M^{-1}dM\bigr)=0
\]
允许径向和切向矩阵通量再分配，并满足反射诱导的 Noether 约束
\[
\int_{S^1}\rho M^{-1}M_r\,dz=0.
\]
这破坏了 VII\(_0\) 的标量单调机制，但现有材料既没有构造出避免奇异的解，也没有证明所有 \(z\)-依赖解仍奇异。

另有一个精确限制：若有限圆柱上外边界轨道映射恰为常数 \(P\)，内边界满足反射 Neumann 条件，则
\[
F(M)=\frac12d_{\mathbb H^2}(M,P)^2
\]
的加权次调和性迫使 \(M\equiv P\)。所以精确 Einstein 连接不能在有限出口把非平凡中心精确松弛成常轨道映射；但近似 Einstein、近似常出口时会出现加权强迫项，当前没有足以产生或排除 \(O(1)\) 累积的估计。

---

## 6. 对图构造的严格含义

### 固定 VII\(_0\) 类

Step 78 已证明：若
\[
\|\operatorname{Ric}+3g\|_{\rm op}\le\delta\le\frac35,
\]
则整个光滑正径向区间上
\[
u<0,\qquad p>0,\qquad K>K_0\ge6-4\delta.
\]
而扩张尾要求 \(u\approx1\)。因此任何始终留在该 ansatz 内并到达扩张尾的连接器都必须满足
\[
\boxed{
\sup\|\operatorname{Ric}+3g\|_{\rm op}>\frac35.}
\]
这已经是一个与数值崩塌无关的严格 \(O(1)\) 缺陷下界。

### 一般构造

没有证据把该下界推广到一般反射 \(T^2\)-不变连接器。收缩本身不产生 Ricci 缺陷：精确 VII\(_0\) 解在其光滑区间内 \(E=0\)，却仍持续收缩并最终奇异。要推出一般 \(O(1)\) 缺陷，尚需证明完整矩阵系统存在继承 VII\(_0\) 反馈的单调量或全局兼容障碍；现有材料没有这样的结果。

具体逃逸方向的状态如下：

1. **非恒面积中心：**  
   非加权平均可变为
   \[
   -3+\langle h^2\rangle_s,
   \]
   但体积加权平均仍严格为 \(-3\)，且必须满足
   \[
   e=12-4\dot h-3h^2\ge0.
   \]
   因而这是可能但强约束的机制。

2. **完整 OT 矩阵 \(M(r,z)\)：**  
   角滑移确实提供了 VII\(_0\) 中不存在的新张量方向；当 \(q<m\) 时，线性化关系
   \[
   A''(0)=(q^2-m^2)A(0)
   \]
   给出朝较小双曲半径弯曲的初始趋势。但尚无完整连接器。

3. **非 OT：**  
   对精确 Einstein、标准反射并保持两个交换 Killing 场的情形，两个 twist 标量恒定且在反射下变号，因此必须恒为零。故精确反射核心不能靠非 OT twist 逃逸。近似 Einstein 时 twist 可由缺陷累积，尚无统一控制。

4. **非反射度量：**  
   若 \(S(0)\ne0\)，则中心约束变为
   \[
   R(q_0)-H(0)^2+|S(0)|^2=-6
   \]
   并伴随 Codazzi 方程；\(S'(0)=\operatorname{Ric}(q_0)+3I\) 及普适 \(-3\) 初始响应都不再适用。这是尚未被当前障碍覆盖的真正不同机制。

5. **Step 80 的数值峰值：**  
   \(r\approx0.2\) 处约 \(15\) 的峰值不能视为几何下界：计算只匹配二阶中心 jet，而估计四阶 jet 已达约 \(149\)；还存在低 Fourier 截断、\(L^2\) 目标、未收敛优化和无离网 supremum 认证等问题。

综上，现有证据严格排除了固定 VII\(_0\) 的小缺陷连接路线，但尚未证明一般 \(z\)-依赖 OT、非恒面积或非反射构造必有 \(O(1)\) 缺陷。精确未决对象是：完整耦合的 \((\gamma_B,\sigma,M)\) 系统在中心后的第一个 \(O(1)\) 物理层中，是否存在满足约束并转入扩张区的均匀小缺陷演化，或是否存在阻止这种转移的矩阵/加权应力单调量。
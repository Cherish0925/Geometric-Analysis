# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 70,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step70_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step70_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

The research asks whether a T²-invariant Einstein half-core exists: a Riemannian 4-metric on [0,R]×T³ with Ric=-3g, totally geodesic at t=0 (shape operator S=0) with prescribed Koiso center metric q on T³ (scalar curvature -6), and approaching an expanding cusp state at t=R. The T²-invariant Gaussian-gauge system is b_tt - e^{-2a}b_θθ = lower order, which is WAVE-like (hyperbolic), not elliptic. The central obstruction is: every scalar-minus-six T³ metric has S'(0) = Ric_q♯+3I with a negative eigenvalue (from Preissmann/sectional curvature). Numerical Cauchy evolution for all tested conformal seeds shows H reversal before reaching the expanding regime. Li-Liu's exact PE-to-AH-cusp Einstein metrics on (0,∞)×T³ demonstrate global compensation exists without reflection symmetry, using the Toda equation. QUESTION: (1) Characterize when a T²-invariant reflection-symmetric Einstein half-core exists: what conditions on the center metric q guarantee that the exact analytic continuation reaches an expanding cusp state rather than developing a singularity? (2) For the approximate problem, if we allow Einstein defect ||Ric+3g||≤δ, can a smooth core be constructed over a domain of length R~log(1/δ) connecting Koiso center to cusp? (3) Is there a deformation of the Li-Liu ASD Toda solution that breaks W⁺=0 while acquiring a nearly-geodesic T³ slice?

## Integrated Scientific Memo

## 结论性备忘

### 0. 首要修正：该约化不是双曲型

由给出的
\[
\hat E_{22}=3-b_{tt}-b_tH_t+e^{-2a}(a_\theta b_\theta-b_\theta^2-b_\theta c_\theta-b_{\theta\theta})
\]
可见其主部为
\[
-b_{tt}-e^{-2a}b_{\theta\theta}.
\]
故 \(\hat E_{22}=0\) 对 Fourier 模 \(e^{ik\theta}\) 给出
\[
\widehat b_k''-k^2e^{-2a}\widehat b_k=\text{低阶项},
\]
是指数增长/衰减的椭圆 Cauchy 行为，而不是波动方程。\(c\) 同理；\(a\) 方向的符号退化来自 Gaussian gauge/约束自由度。完整 Einstein–DeTurck 系统严格椭圆。

因此：

* 从 \((q,S=0)\) 向前数值“演化”是病态的椭圆 Cauchy 计算；
* \(t\approx0.45\) 后的 Fourier 爆炸不能证明几何奇性；
* 两端 Dirichlet 并非“固定端点弦问题”；
* 在 \(t=0\) 光滑反射必须显式施加 \(S=0\)，不能靠 Dirichlet 解直接加倍得到。

不过以下精确恒等式比数值演化给出了更强的全局限制。

---

## 1. 精确反射半核：平坦扩张 cusp 不可能

写
\[
g=dt^2+\gamma_t,\qquad
S=\frac12\gamma_t^{-1}\dot\gamma_t,\qquad H=\operatorname{tr}S,
\]
并取扩张归一化
\[
h_t=e^{-2t}\gamma_t,\qquad B=S-I,\qquad b=\operatorname{tr}B=H-3.
\]
若 \(\operatorname{Ric}_g=-3g\)，则 normal-normal Einstein 方程给出
\[
\dot b+2b+|B|^2=0. \tag{1}
\]
反射中心满足 \(S(0)=0\)，故
\[
B(0)=-I,\qquad b(0)=-3.
\]
积分 (1)：
\[
\boxed{\;
e^{2t}b(t,\theta)
=-3-\int_0^t e^{2s}|B(s,\theta)|^2\,ds .
\;} \tag{2}
\]

### 1.1 有限距离不能达到精确 cusp Cauchy 数据

由 (2)，对每个有限 \(t\),
\[
b(t,\theta)<0,\qquad H(t,\theta)<3.
\]
精确平坦扩张 cusp 的 \(S=I\)，即 \(B=b=0\)，故任何反射 Koiso germ 都不可能在有限 \(R\) 达到它。更定量地，
\[
3-H=-b\ge 3e^{-2t},\qquad
|B|\ge \frac{|b|}{\sqrt3}\ge \sqrt3e^{-2t}. \tag{3}
\]

这已经回答了“在 \(t=R\) 达到精确 expanding cusp state”的版本：其中心度量集合为空，与 \(q\) 的选择无关。

### 1.2 平坦 conformal infinity 也不可能

若解存在至 \(t=\infty\)，并具有光滑 Poincaré–Einstein 展开
\[
h_t=h_0+e^{-2t}h_2+e^{-3t}h_3+\cdots ,
\]
则四维 PE 展开给出
\[
h_2=-P_{h_0},\qquad
b=e^{-2t}\frac{R_{h_0}}4+O(e^{-3t}).
\]
令 \(t\to\infty\) 于 (2)，得到逐点恒等式
\[
\boxed{\;
\frac14R_{h_0}(\theta)
=-3-\int_0^\infty e^{2s}|B(s,\theta)|^2\,ds .
\;} \tag{4}
\]
因 \(B(0)=-I\)，右端严格小于 \(-3\)，所以
\[
\boxed{R_{h_0}<-12\quad\text{逐点}.} \tag{5}
\]
尤其 \(R_{h_0}=0\) 的平坦 \(T^3\) conformal infinity 不可能出现。

因此，“反射对称、totally geodesic \(T^3\) 中心并渐近通常的平坦 AH cusp”不存在。Li–Liu 的非反射解不与此矛盾。

### 1.3 一般扩张 PE 端的精确刻画

对解析 \(q\) 且 \(R_q=-6\)，Koiso 定理给出唯一最大解析延拓。反射半核通向某个一般 PE 端，当且仅当该延拓：

1. 在每个有限区间保持正定且曲率不爆；
2. \(h_t=e^{-2t}\gamma_t\) 光滑收敛到某个 \(h_0\)；
3. \(B\) 具有相应 Fefferman–Graham 衰减；
4. 满足 momentum、Hamiltonian 及 tensor evolution 方程；
5. 必然满足散射约束 (4)，特别是 \(R_{h_0}<-12\)。

这可表述为 Koiso 初值流形
\[
\{(q,-I):R_q=-6\}
\]
与 PE 端稳定流形的交。它是非局部条件，不能仅由 \(S'(0)\) 的符号判断。

中心处
\[
S'(0)=\operatorname{Ric}_q^\sharp+3I,
\]
且三维 \(R_q=-6\) 时，某主方向满足
\[
\operatorname{Ric}_i+3=-K_{jk}.
\]
Preissmann 给出某处 \(K\ge0\)，而严格负特征值可进一步由无共紧平坦因子的非正曲率刚性推出：若处处 \(K\le0\)，\(T^3\) 必平坦，与 \(R=-6\) 矛盾；故某处 \(K>0\)。这说明必有初始收缩，但它不是上述平坦端不可能性的核心；真正的全局障碍是 (2)。

---

## 2. 近似问题：对数长度是必要的，但现有材料尚未构造出核

设
\[
E=\operatorname{Ric}_g+3g,\qquad \|E\|_{\mathrm{op}}\le\delta .
\]
则 (1) 变为
\[
\dot b+2b+|B|^2=-E_{00},
\]
故
\[
e^{2R}b(R)
=-3-\int_0^R e^{2s}|B|^2ds
-\int_0^R e^{2s}E_{00}ds. \tag{6}
\]

若末端 shape 精确 cuspidal，即 \(B(R)=0\)，则
\[
3+\int_0^R e^{2s}|B|^2ds
=-\int_0^R e^{2s}E_{00}ds
\le \frac{\delta}{2}(e^{2R}-1).
\]
从而
\[
\boxed{\;
R\ge \frac12\log\!\left(1+\frac6\delta\right).
\;} \tag{7}
\]
更精确地，
\[
R\ge \frac12\log\!\left[
1+\frac2\delta
\left(3+\int_0^R e^{2s}|B|^2ds\right)
\right]. \tag{8}
\]
若仅要求 \(|B(R)|\le\eta\)，则
\[
3+\int_0^R e^{2s}|B|^2ds
\le \sqrt3\,\eta e^{2R}+\frac{\delta}{2}(e^{2R}-1). \tag{9}
\]
当 \(\eta=O(\delta)\) 时仍强制 \(R\gtrsim \frac12\log(1/\delta)\)。

这还揭示必要的 defect 符号：\(-E_{00}\) 必须补偿初值 \(-3\) 及全部加权 shear 能量。任意无符号振荡误差都不够。

### 2.1 终端平坦尾部本身容易控制

在
\[
g=dt^2+f(t)^2h_{\rm flat},\qquad f'/f=1+\beta
\]
中，
\[
E_{00}=-3\beta'-6\beta-3\beta^2,
\qquad
E_{\tan}=-\beta'-6\beta-3\beta^2.
\]
若 \(\beta,\beta'=O(\delta)\)，则完整 Einstein defect 为 \(O(\delta)\)，且可在固定长度内令 \(\beta\to0\)。困难不在最终 smoothing layer，而在此前必须达到
\[
\|h_T-h_{\rm flat}\|_{C^{2,\alpha}}
+\|B_T\|_{C^{1,\alpha}}=O(\delta),\qquad
T=\tfrac12\log(1/\delta)+O(1). \tag{10}
\]

### 2.2 “Koiso germ—插值—扩张锥”并未给出所需构造

扩张锥
\[
dt^2+e^{2t}q
\]
的切向 defect endomorphism 确实为
\[
e^{-2t}\operatorname{Ric}_q^\sharp,
\]
故在已经进入该锥后，内禀曲率误差按 \(e^{-2t}\) 稀释。这解释了系数 \(1/2\)。

但从 \(S=0\) 转到 \(S\simeq I\) 是 \(O(1)\) 的 shape 改变。若在长度 \(L\) 上缓慢插值，误差通常为 \(O(1/L)\)；要令其 \(\le\delta\) 需要 \(L\gtrsim\delta^{-1}\)，而不是 \(\log(1/\delta)\)。因此不能把“固定长度过渡层”或“长度 \(R\) 上普通慢插值”当作证明。精确 normal identity 同样表明所需补偿是定向且带权的。

固定 Fourier 模在标准 cusp 中也不能提供对数放大，因为
\[
\int_0^R |k|e^{-a(t)}dt
\]
在 \(a\sim t\) 时有界。真正可能实现对数 steering 的机制只能是例如：

* 精确 Koiso 延拓随参数长期贴近 cusp 稳定流形；
* 存在 \(e^{-a}\) 不快速衰减的长区域；
* 使用随 \(\delta\) 增长的频率，同时统一控制曲率与非线性耦合；
* Einstein–DeTurck 端到内部算子的最小奇异值满足
  \(\sigma_{\min}(R)\sim e^{-\kappa R}\)，并且 mismatch 在相应 cokernel 方向有非零投影。

所以当前严格结论是：

\[
\boxed{\text{\(R\asymp\log(1/\delta)\) 是必要且尺度上自然，但存在性尚未证明。}}
\]

决定性未知量是达到 (10) 的全张量 steering 轨道，而非末端锥形稀释。

---

## 3. Li–Liu 变形：小扰动不能产生近全测地 \(T^3\)

首先，源笔记中的 Toda 化简存在代数歧义：
\[
(e^v)_{\xi\xi}+\Delta v=0
\]
并不等同于
\[
(e^v)_{\xi\xi}+\Delta(e^v)=0.
\]
若 \(v=v(\xi,\theta)\)，前者为
\[
(e^v)_{\xi\xi}+v_{\theta\theta}=0,
\]
仍是非线性的；必须核对 Li–Liu 原方程后才能采用调和函数方法。

对 Type-I 度量
\[
g=\xi^{-2}\!\left(Wd\xi^2+W^{-1}\eta^2+We^vg_{T^2}\right),
\qquad W>0,
\]
置
\[
p=\frac{\xi W_\xi}{2W},\qquad \frac{\xi v_\xi}{2}=1-W.
\]
忽略 \(\partial_\xi\eta\) 产生的非对角项（它们不会降低 Frobenius 范数），\(\xi\)-level 的主 shape 特征值为
\[
s_\eta=-\frac{1+p}{\sqrt W},\qquad
s_1=s_2=\frac{p-W}{\sqrt W}.
\]
故
\[
|S|^2\ge
\frac{(1+p)^2+2(p-W)^2}{W}.
\]
先对 \(p\)、再对 \(W>0\) 极小化得到
\[
\boxed{|S|^2\ge\frac83.} \tag{11}
\]
所以任何 coordinate level 都与全测地相差 \(O(1)\)；足够小的 \(C^1\) 度量扰动不可能修复它。若想留在 Li–Liu 附近，只能考察强烈倾斜的图形切片 \(\xi=\phi\)，其线性化满足
\[
DS(k,\phi)=D_gS[k]-\nabla^2\phi
-\phi\bigl(R_{\nu i\nu j}+S_i{}^mS_{mj}\bigr). \tag{12}
\]
于是问题变成逐 Fourier 模判断目标 shape tensor 是否落在“度量变形项 + Hessian-potential 算子”的像内。

此外，Gauss–Codazzi 与四维 Weyl 分解给出 \(T^3\) 上某点的定量关系
\[
\boxed{\;
1\le C\bigl(|W^+|+|\nabla S|+|S|^2\bigr).
\;} \tag{13}
\]
理由是 Preissmann 保证某个切平面 \(K_\Sigma\ge0\)，而
\[
K_\Sigma(e_i,e_j)
=-1+W_{ijij}+\det(S|_{ij}),
\]
混合 Weyl 分量又由 Codazzi
\[
W_{\nu ijk}=\nabla_jS_{ik}-\nabla_kS_{ij}
\]
控制；ASD 条件把切向 Weyl 与混合分量联系起来。

其后果是：

* ASD Einstein 度量不能含 totally geodesic \(T^3\)；
* 若 \(S\to0\) 于 \(C^1\)，则必须有 \(\sup|W^+|\ge c_0>0\)；
* 因而不存在同时满足 \(W^+\to0\)、\(S\to0\) in \(C^1\) 且有统一 bounded geometry 的变形族。

所以答案不是“小幅破坏 \(W^+=0\) 是否足够”，而是：

\[
\boxed{\text{近全测地 \(T^3\) 要求有限幅度 ASD-breaking，或强倾斜/高频/退化。}}
\]

严格的变形问题应在 mixed PE–cusp 加权空间中求解 Bianchi-gauge 线性 Einstein 方程
\[
D(\operatorname{Ric}+3g+\delta^*\beta)_gk=0, \tag{14}
\]
并与 (12) 联立。尚未确定的核心对象是：

1. mixed-end Lichnerowicz 算子的 kernel/cokernel；
2. conformal-infinity 变分是否产生 \(DW^+(k)\neq0\) 的模式；
3. end-to-slice 映射是否覆盖 (12) 中 Hessian-potential 像之外的 tensor 分量；
4. 有限幅继续是否保持完备性及 cusp 渐近。

---

## 总结

1. Gaussian \(T^2\)-约化具有椭圆 Cauchy 行为；现有 forward Galerkin 爆炸不构成奇性证据。
2. 对任何反射中心，
   \[
   e^{2t}(H-3)
   =-3-\int_0^t e^{2s}|S-I|^2ds.
   \]
   因而有限距离精确平坦 cusp jet、以及无穷远平坦 conformal boundary，均不可能。
3. 一般 PE 端只有在其边界代表满足逐点 \(R_{h_0}<-12\) 及完整稳定流形条件时才可能。
4. \(\delta\)-近 Einstein 核若达到 cusp shape，必有
   \[
   R\ge\tfrac12\log(1+6/\delta),
   \]
   但该恒等式只证明必要尺度；\(R=O(\log(1/\delta))\) 的构造仍缺少全张量 steering 机制。
5. Li–Liu coordinate slices 满足 \(|S|^2\ge8/3\)，且近全测地 \(T^3\) 强制 order-one \(W^+\) 或 order-one \(\nabla S\)。故所需变形不可能是 bounded-geometry 下的微小 ASD 扰动。
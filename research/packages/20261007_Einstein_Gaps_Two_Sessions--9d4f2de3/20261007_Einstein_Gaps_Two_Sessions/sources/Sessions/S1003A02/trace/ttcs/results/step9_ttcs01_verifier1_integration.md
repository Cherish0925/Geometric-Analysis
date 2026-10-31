# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 9,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step9_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step9_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the attached O11 computation artifacts as a geometric analyst and assess what is scientifically established by the new Fubini–Study versus complex-hyperbolic sign experiment and by the attempted Hessian tests. Check normalizations and the inference that P/(8π²)=1-x0 R^+(ζ,ζ)+O(x0²): in the code the complex-space-form collar is K=x+kappa x² with s=-24kappa and aligned R^+(ω,ω)=-6kappa. Determine whether P<1 for kappa=-1 is a genuine same-metric cell result, whether the finite outer radius or interpolation can mimic the sign, and what asymptotic extrapolation is justified by x0=.001,.003. Then evaluate the second-variation design: full radial symmetric-h Hessian and non-invariant coordinate/coframe Hessians, their quadrature consistency, base stationarity, diffeomorphism modes, and why negative numerical eigenvalues accompanied by two-sided energy rise are not yet negative directions. Recommend one mathematically decisive executable next check that stays focused on the spectral problem modulo diffeomorphisms.

## Integrated Scientific Memo

# O11 核验结论

记
\[
\widehat P(g)=\frac1{8\pi^2}\int |\Ric_g^\circ|^2\,dV_g;
\]
脚本输出的 `P` 是 \(\widehat P\)，不是未归一化积分。

## 1. 复空间形式的归一化与符号正确

对
\[
g=\frac{dx^2}{4K}+x(\sigma_1^2+\sigma_2^2)+K\sigma_3^2
\]
有
\[
s=-4K''-\frac{8K'}x+\frac8x.
\]
因此
\[
K=x+\kappa x^2\quad\Longrightarrow\quad s=-24\kappa.
\]
在 Kähler 方向 \(\omega\) 上，
\[
W^+(\omega,\omega)=\frac{s}{6},\qquad
\mathcal R^+=W^++\frac{s}{12}I,
\]
故
\[
\mathcal R^+(\omega,\omega)=\frac{s}{4}=-6\kappa.
\]
所以
\[
\boxed{\widehat P=1+6\kappa x_0+O(x_0^2)
      =1-x_0\mathcal R^+(\omega,\omega)+O(x_0^2)}
\]
在符号和系数上均一致：

- \(\kappa=+1\)：CH，\(s=-24\)，首阶 \(1+6x_0\)；
- \(\kappa=-1\)：FS，\(s=24\)，首阶 \(1-6x_0\)。

FS collar 必须取 \(0<X<1\)，因为 \(K=x-x^2>0\) 仅在该区间成立。

这个符号翻转只检验 aligned Kähler 方向。复空间形式中 \(s\) 和 \(W^+\) 被绑定并同时翻号，所以新实验本身不能独立证明一般方向的
\[
-x_0\mathcal R^+(\zeta,\zeta)
\]
张量律；一般 \(\zeta\) 的结论仍依赖先前角度实验及 \(SO(3)_+\)-等变性。

---

## 2. FS 的 \(\widehat P<1\) 是真实 cell 效应，不是背景扣除

`o11_general_bulk_cell.py` 最后直接积分
```python
P = sum(r0*wx*dv)/(8*pi**2)
```
其中 `r0` 是 \(|\Ric^\circ|^2\)。它没有调用带 CH 硬编码背景扣除的 `Cell.report`。因此，只要优化后度量正定且端点光滑匹配成立，\(\kappa=-1\) 输出的 `P<1` 就是一张实际 FS-cell 度量自身的能量，不是“cell 减 background”的伪差值。

还可在未优化的四常数 Kähler seed 上解析确认。若
\[
K=x+\frac{c_1x^3}{4}-\frac{c_2}{2}+\alpha x^2+\frac{\beta}{x},
\]
则
\[
|\Ric^\circ|^2
=4\left(K''-\frac{2K}{x^2}+\frac2x\right)^2,
\qquad
dV=\pi^2x\,dx,
\]
而
\[
K''-\frac{2K}{x^2}+\frac2x=c_1x+\frac{c_2}{x^2}.
\]
故
\[
\widehat P_0=
\frac{c_1^2}{8}(X^4-x_0^4)
+c_1c_2(X-x_0)
+\frac{c_2^2}{4}\left(x_0^{-2}-X^{-2}\right).
\]
由四个匹配条件展开得
\[
\boxed{
\widehat P_0
=1+6\kappa x_0+
9\left(\kappa^2+X^{-2}\right)x_0^2+O(x_0^3).
}
\]
因此对于任意固定 \(0<X<1\)，\(\kappa=-1\) 且 \(x_0\) 充分小时，
\[
\widehat P_0<1.
\]
也就是说，阈值以下现象在显式未优化 Kähler 度量中已经存在。

这不与点态非负性矛盾：\(1\) 是完整 Burns ALE 能量的归一化值，不是任意截断并接入正曲率 Einstein collar 的局部 cell 下界。

随附材料没有新的 FS 输出 JSON，因此尚不能核对某个具体运行的小数值、`grad_inf` 或优化后正定性。严格认证某次运行还需检查优化后而非仅 seed 的 \(G>0\)、\(h>0\) 及端点消失条件。当前 `min_K` 只采样 seed，且在 bolt 处 \(K(x_0)=0\) 本来就是预期行为。

---

## 3. 有限外半径和插值不能伪造首阶符号

上式表明在固定 \(X\)、\(x_0/X\to0\) 时，有限半径的首个显式影响为
\[
9X^{-2}x_0^2,
\]
不可能制造 \(\pm6x_0\) 的符号翻转。固定 \(x>0\) 时，
\[
K(x)=x+\kappa x^2+
x_0\!\left[-1+3(x/X)^2-2(x/X)^3\right]+O(x_0^2).
\]
远离 bolt，度量扰动为 \(O(x_0)\)，而外部背景满足 \(\Ric^\circ=0\)，故该区域的能量贡献从 \(O(x_0^2)\) 开始。首阶项来自 \(x=O(x_0)\) 的 Burns 缩放区。

若 \(X\) 很小，\(x_0^2/X^2\) 在 \(x_0=.001,.003\) 上仍可能显著弯曲有限尺度斜率；所以数值比较必须保持两种符号使用同一个固定 \(X\)，并记录 \(x_0/X\)。

对优化后的非 Kähler profile，现有 CH 数据还暗示 \(x_0^2\log(X/x_0)\) 型松弛效应；两点不足以在 \(x_0^2\)、\(x_0^2\log x_0\) 和参数族漂移之间作区分。但这些仍是次阶，不改变解析 seed 已确立的首阶符号。

最干净的成对检验是
\[
A(x_0,X)=
\frac{\widehat P_{+}(x_0,X)-\widehat P_{-}(x_0,X)}{2x_0},
\]
以及
\[
E(x_0,X)=
\frac{\widehat P_{+}+\widehat P_{-}}2-1.
\]
对 Kähler seed，
\[
A=6+O(x_0^2),\qquad E=O(x_0^2),
\]
因为共同的偶次修正在 odd combination 中相消。

---

## 4. \(x_0=.001,.003\) 所能支持的外推

设
\[
q_\kappa(t)=\frac{\widehat P_\kappa(t)-1}{t}.
\]
若额外假定
\[
q_\kappa(t)=a_\kappa+b_\kappa t+O(t^2),
\]
则两点 Richardson 截距为
\[
a_\kappa^{(2)}
=\frac{3q_\kappa(.001)-q_\kappa(.003)}2.
\]
例如笔记中的 CH aligned 数据
\[
q_+(.001)=5.956,\qquad q_+(.003)=5.900
\]
给出
\[
a_+^{(2)}=5.984.
\]
这与 \(6\) 相容，但远非独立证明；更小尺度 \(3\times10^{-4},10^{-4}\) 的数据才更有力地显示趋于 \(6\)。

对 FS，两点可以可靠说明：

1. `P<1` 若在两尺度均出现，是稳定的有限尺度现象；
2. 斜率若接近 \(-6\)，与解析首阶响应一致；
3. 在预设修正模型后可以给出截距估计。

两点不能识别次阶形式，也不能证明优化后 cell 下确界满足完整渐近展开。新运行给出的只是显式上界序列，不是匹配下界或 SU(2)-cell infimum 的定理。

---

## 5. 径向 Hessian：积分一致，但基点不驻定

`o11_radial_hessian.py` 的径向空间包含 \(G\) 和 \(h\) 的六个对称分量，端点 bubbles 固定 bolt/collar 数据，径向 \(L^2\) Gram 形式也与张量范数一致。

其积分归一化极好：

\[
1.0185958458021929
\quad\text{vs.}\quad
1.0185958454323307,
\]
\[
1.0185958458067998
\quad\text{vs.}\quad
1.0185958454323307.
\]
误差约 \(3.7\times10^{-10}\)，故径向 quadrature 和体积因子没有明显归一化问题。

然而基点不是扩大空间中的临界点：
\[
\|\nabla\widehat P\|_{L^2}=5.22\quad(n=6),\qquad
12.65\quad(n=8).
\]
原始优化还以 `msg="ABNORMAL"` 结束。原 30 参数 profile 的近似优化并不意味着在新的 42/56 维全径向张量空间中驻定。

谱也未收敛：
\[
\lambda_{\min}=-1.63\quad(n=6),
\qquad
\lambda_{\min}=-23.18\quad(n=8),
\]
负特征值数从 1 增至 2。最低模态的原始系数达到 \(10^3\!-\!10^4\)，并随着分辨率集中在更细尺度，因此当前结果更像非驻定、gauge 和高频离散效应的混合，而非稳定 Ritz 负模。

此外，\(G\mapsto Ge^d\) 是非线性参数化。在非临界点，坐标 Hessian 会多出“一阶梯度乘参数化二阶导数”的项；故其惯性还不是度量空间或商空间上内禀的二次变分。

---

## 6. 为什么“负特征值但双侧能量上升”尚非负方向

在临界点 \(g\) 的真正负模 \(v\) 上，应有
\[
\widehat P(g+tv)+\widehat P(g-tv)-2\widehat P(g)
=t^2H(v,v)+o(t^2)<0
\]
对充分小 \(t\) 成立。

现有最低模曲线在 \(t=.005\) 的对称二阶差商却为正：

- \(n=6\)：约 \(4.26\)，而 AD 特征值为 \(-1.63\)；
- \(n=8\)：约 \(59.7\)，而 AD 特征值为 \(-23.18\)。

这并不能反证 AD Hessian，因为 Gram-unit 模态的点态幅值极大，\(t=.005\) 很可能已远离二次区；四次及更高阶项可以主导。合适的小量应由
\[
\|g^{-1}(t h)\|_{L^\infty}
\]
而不是固定的系数 \(t\) 控制。现有数据估计二次区可能在 \(t\lesssim10^{-3}\) 甚至更小。

另一方面，双侧曲线还含明显奇部，即一阶漂移；因此它们混合了：

- 非零梯度；
- 坐标 Hessian；
- 巨大的高阶项；
- 可能的 diffeomorphism 污染。

所以当前负数仅是“原始有限维坐标 Hessian 在非临界点的负惯性”，不是已建立的模微分同胚负方向。

---

## 7. 微分同胚模态的具体污染机制

对紧支撑向量场 \(X\)，微分同胚不变性给出
\[
d\widehat P_g(\mathcal L_Xg)=0.
\]
沿真实轨道 \(\phi_t^*g\) 二次微分：
\[
H_g(\mathcal L_Xg,\mathcal L_Xg)
+d\widehat P_g(\mathcal L_X^2g)=0.
\]
只有当 \(d\widehat P_g=0\) 时，Lie derivative 方向才是 Hessian 零模。当前基点非驻定，因此线性路径
\[
g+t\mathcal L_Xg
\]
缺失真实轨道的二阶修正，并可产生任意符号的伪 Hessian。

径向重参数化 \(X=\xi(x)\partial_x\) 作用为
\[
d=\xi\,\frac{G'}G-2\xi',\qquad
\delta h=\xi h'.
\]
当前最低模主要位于 \(G\) 与 \(h\) 的对角块，正是这一 gauge 作用最强的区域。径向脚本又不含 \(dx\,\sigma_i\) shifts，因此尚未完整容纳一般 SU(2)-不变 gauge 轨道。

---

## 8. 非不变 Hessian 两个实现尚不能用于谱结论

### 坐标分量版 `o11_full_hessian.py`

- 文档声称加入 DeTurck/Bianchi penalty，但代码没有计算 \(\beta_g(h)\)，也没有把任何 penalty 加入 Hessian；输出仍是 raw Hessian。
- 用 \(u=\cos\theta\) quadrature 后除以 \(\sin\theta\) 的测度变换本身可成立。
- 但常数 Euler 坐标分量如 \(d\psi^2,d\psi\,d\phi\) 通常不是 \(S^3\) 上全局光滑张量；避开坐标极点的低阶 quadrature 会掩盖奇性。
- 对 \(\psi,\phi\) 使用低阶 Gauss–Legendre 也不精确积分 Fourier 模态，因此角向 Hessian 容易 alias。

### 自然 coframe 版 `o11_full_hessian2.py`

把扰动放在
\[
(dx,\sigma_1,\sigma_2,\sigma_3)
\]
中再转回 Euler 坐标，修复了 constant coframe tensor 的全局性问题，并加入 \(dx\,\sigma_i\) 分量。但：

- 默认 `nqa=2` 时，
  \[
  \int_0^\pi\sin\theta\,d\theta
  \]
  仅得到约 \(0.968\) 倍真值，故 `P_quad` 预期已有约 3.2% 偏差；这大于当前 \(P-1\approx0.019\) 的信号尺度。
- 二阶角导数对两点 quadrature 更易 alias。
- \(\cos\psi,\sin\psi\) 单独作为 Euler 角函数未必是 \(S^3\) 上全局光滑标量；应改用 Wigner \(D\)-functions 或明确的球面/群表示谐波。
- `constant` angular set 实质上主要是 SU(2)-不变 sector 加 shift，并不是充分的非不变检验。
- 仍未显式商去 diffeomorphisms。

随附材料没有这两个脚本的输出，因此也无法检验它们的 `P_quad/P_cell` 或谱随角分辨率的收敛。

---

## 9. 一个决定性的可执行下一步：SU(2)-不变 Bianchi-slice Ritz 谱

当前最聚焦且能直接裁决已出现负模的检查，是在自然 coframe 中做完整 SU(2)-不变、模微分同胚的驻定 Hessian：

1. 采用全部十个径向对称张量分量，包括 \(dx\,\sigma_i\) shifts，并使用统一端点 bubbles。
2. 同时离散四分量紧支撑向量场
   \[
   X=f_0(x)\partial_x+\sum_{i=1}^3f_i(x)E_i,
   \]
   构造 Lie derivative 映射
   \[
   D:X\mapsto\mathcal L_Xg.
   \]
3. 用张量 \(L^2\) Gram 矩阵 \(G\) 构造离散正交补
   \[
   D^TGZ=0,
   \]
   即 Bianchi/gauge slice。
4. 先在该 slice 内重新求真正临界点，要求投影梯度
   \[
   \|Z^T\nabla\widehat P\|_{(Z^TGZ)^{-1}}
   \]
   降至数值精度，再解
   \[
   Z^THZ\,u=\lambda\,Z^TGZ\,u.
   \]
5. 对 \(N=6,8,10,12,\ldots\) 和加密径向 quadrature 检查最低特征值收敛；最低模路径按
   \[
   \|g^{-1}th\|_\infty=10^{-5},10^{-4},10^{-3},\ldots
   \]
   缩放，而不是固定 \(t=.005\)。
6. 同时验证
   \[
   d\widehat P(DX)\approx0,
   \]
   以及临界点处
   \[
   HD\approx0,
   \]
   并检查中心差商趋于相应 Ritz 值。

若负特征值在驻定化、Bianchi 投影和谱加密后稳定，则它才是一个真正的 SU(2)-不变、模微分同胚下降方向；若消失，则现有负值可归因于非驻定/gauge/参数化污染。该计算只需一维径向积分，避开当前非不变试验的 Euler 奇性和角 quadrature 缺陷。

## 最终判定

- \(\mathcal R^+(\omega,\omega)=-6\kappa\) 及首阶律的归一化、符号正确。
- FS 中 \(\widehat P<1\) 是显式同一 cell 度量的真实可能性；四常数 Kähler seed 已解析实现它。
- 固定 \(X\) 时，有限半径和插值从次阶进入，不能伪造首阶符号，但小 \(X\) 会显著扭曲有限尺度斜率。
- \(x_0=.001,.003\) 足以支持符号和近似首阶系数，不足以识别次阶渐近或证明优化下确界。
- 径向积分一致，但基点明显不驻定，raw 谱不收敛且未商去 diffeomorphisms。
- “负数值特征值 + 已采样双侧上升”既未建立也未排除真正负模；现有步长尚未进入可靠二次区。
- 下一项决定性检查应是完整 SU(2)-不变自然 coframe 上的驻定化 Bianchi-slice Ritz 谱，而不是继续扩大未经 gauge 处理的非不变 Hessian。
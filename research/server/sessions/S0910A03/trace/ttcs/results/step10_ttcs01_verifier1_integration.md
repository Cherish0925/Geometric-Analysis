# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 10,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step10_ttcs01_sub5_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step10_ttcs01_sub6_verifier.md"
    }
  ]
}
```

## Exact Task

Check and correct the Step-10 reassessment of Taub–NUT–AdS and scaling. Independently verify from the metric and the supplied symbolic scripts: (i) the exact |W|^2 formula, its value near the NUT, cumulative Weyl energy and all-radius curvature-mean behavior; (ii) whether a smaller fixed buffered domain around a point at distance 1/2 unwraps the short circle for all small nu; (iii) the locally unwrapped annular limit and its calibrated deficit; (iv) the correct homothetic scaling of Ricci endomorphism, Weyl endomorphism spectrum, |W|, and the forbidden calibrated Einstein germ. Decide precisely what Taub–NUT–AdS refutes and what it does not. Also flag orientation/factor-of-four convention issues between full Weyl and W+ before conclusions are used.

## Integrated Scientific Memo

# Taub–NUT–AdS 与缩放：核验结论

设
\[
g_\nu=\frac{dr^2}{F_\nu(r)}
 +(r^2-\nu^2)d\Omega_2^2
 +4\nu^2F_\nu(r)(d\psi+\cos\theta\,d\phi)^2,
\]
\[
F_\nu(r)=\frac{r-\nu}{r+\nu}
\left(1+\frac{(r-\nu)(r+3\nu)}3\right),\qquad r\ge \nu,
\]
其中 \(\phi\) 周期 \(2\pi\)、\(\psi\) 周期 \(4\pi\)。符号计算确证
\[
\operatorname{Ric}_{g_\nu}=-g_\nu,\qquad s=-4.
\]

## 1. 精确曲率、NUT 曲率峰与累积能量

脚本 `compute_taub_nut_ads_curvature.py` 算出的 \(W^2\) 是四指标张量范数
\(W_{abcd}W^{abcd}\)，其精确值为
\[
\boxed{
|W|_{\rm tens}^2
=\frac{32\nu^2(4\nu^2-3)^2}{3(r+\nu)^6}.
}
\]
由于度量是 Einstein，
\[
\boxed{
|\operatorname{Rm}|_{\rm tens}^2
=\frac83+|W|_{\rm tens}^2.
}
\]

在 NUT 点 \(r=\nu\)，
\[
\boxed{
|W|_{\rm tens}^2(\nu)
=\frac{(4\nu^2-3)^2}{6\nu^4}
\sim \frac{3}{2\nu^4}.
}
\]
因此“每个固定 \(\nu\) 的 NUT 光滑”与“当 \(\nu\to0\) 时 NUT 曲率爆破”并不矛盾。若
\[
r=\nu+\frac{\rho^2}{8\nu},
\]
则
\[
|W|_{\rm tens}^2
=\frac{(4\nu^2-3)^2}{6\nu^4}
\left(1+\frac{\rho^2}{16\nu^2}\right)^{-6}.
\]
Step 9 中“近 NUT 是平直 \(\mathbb R^4\)，故曲率趋零”的暗示不成立：平直的是切锥，不是随 \(\nu\to0\) 一致的曲率。

### 体积因子修正

由
\[
\sqrt{\det g}=2\nu(r^2-\nu^2)\sin\theta
\]
得到完整轨道的径向体积密度
\[
\boxed{\frac{dV}{dr}=32\pi^2\nu(r^2-\nu^2),}
\]
而两个 multiscale/curvature 脚本误用了 \(64\pi^2\nu(r^2-\nu^2)\)。该误差使绝对体积与绝对能量多一倍，但在平均值中相消。

记
\[
\mathcal B_R=\{\nu\le r\le R\}.
\]
则
\[
\boxed{
V_\nu(R)=\frac{32\pi^2\nu}{3}(R-\nu)^2(R+2\nu),
}
\]
\[
\boxed{
E_\nu^W(R)
=\int_{\mathcal B_R}|W|_{\rm tens}^2\,d\mu
=
\frac{32\pi^2(4\nu^2-3)^2}{9}
\frac{(R-\nu)^2(R^2+6R\nu+17\nu^2)}
{(R+\nu)^4}.
}
\]
所以
\[
\boxed{
E_\nu^W(\infty)=\frac{32\pi^2(4\nu^2-3)^2}{9}
\longrightarrow 32\pi^2.
}
\]
Weyl 能量有限；\(\int|\operatorname{Rm}|^2=\infty\) 来自无限体积上的常数背景项 \(8/3\)，不是 Weyl 核心能量发散。

精确平均值为
\[
\boxed{
\fint_{\mathcal B_R}|W|_{\rm tens}^2
=
\frac{(4\nu^2-3)^2(R^2+6R\nu+17\nu^2)}
{3\nu(R+\nu)^4(R+2\nu)}.
}
\]
因此：

* \(R=\nu x\)、\(x>1\) 固定时，
  \[
  \fint_{\mathcal B_{\nu x}}|W|^2
  =
  \frac{(4\nu^2-3)^2}{3\nu^4}
  \frac{x^2+6x+17}{(x+1)^4(x+2)}
  =\Theta(\nu^{-4});
  \]
* \(R>0\) 固定时，
  \[
  \nu\fint_{\mathcal B_R}|W|^2\longrightarrow\frac3{R^3},
  \]
  即平均值为 \(\Theta(\nu^{-1})\)。

## 2. 以距 NUT 为 \(1/2\) 的点为中心时的各半径行为

取
\[
d(p_\nu,N_\nu)=\frac12.
\]
其 \(r\)-坐标不严格是 \(\nu+\frac12\)；事实上
\[
r(p_\nu)\to \sqrt3\sinh\!\left(\frac1{2\sqrt3}\right).
\]
这不影响环带估计。

对 \(0<s\le1/3\)，
\[
B_s(p_\nu)\subset
\{1/6\le d(\cdot,N_\nu)\le5/6\}.
\]
在该环带上
\[
|W|_{\rm tens}^2=O(\nu^2),
\qquad
\fint_{B_s(p_\nu)}|\operatorname{Rm}|^2
=\frac83+O(\nu^2),
\]
同时
\[
\operatorname{Vol}B_s(p_\nu)=\Theta(\nu).
\]

但是这种平均曲率控制不能延伸到所有 \(s\le1\)。若固定 \(s>1/2\)，球会捕获 NUT 核心；由三角不等式
\[
B_{s-1/2}(N_\nu)\subset B_s(p_\nu)
\subset B_{s+1/2}(N_\nu),
\]
故球内 Weyl 能量趋于 \(32\pi^2\)，而体积仍为 \(\Theta(\nu)\)，从而
\[
\boxed{
\fint_{B_s(p_\nu)}|\operatorname{Rm}|^2
=\Theta(\nu^{-1}),\qquad s>1/2.
}
\]
所以截断到半径 \(1\) 的全尺度极大函数并不一致有界。

## 3. 小缓冲域确实会展开短圆

Step 9 的“局部普适覆盖仍塌缩”只对包含 NUT 的大缓冲域成立，不能用于任意较小固定域。

### 包含 NUT 的 \(B_1(p_\nu)\)

短 \(\psi\)-圆可沿径向扫入距 \(p_\nu\) 为 \(1/2\) 的 NUT，因此在
\(B_1(p_\nu)\) 中可缩。相对于这个大域，纤维基本群像为零，提升后的环带仍塌缩。

### 不含 NUT 的小缓冲域

固定取
\[
\boxed{\frac13<R_0<\frac12.}
\]
则 \(B_{R_0}(p_\nu)\) 不含 NUT，且对充分小的 \(\nu\)，完整短纤维位于该域中。域位于一个固定环带；在小的三维商球上 Hopf 圆丛平凡，纤维生成
\(\pi_1\cong\mathbb Z\)，不能在域内缩掉。因此其普适覆盖会展开短圆，且固定尺度覆盖球非塌缩。

故 fibered rank 是缓冲域依赖的：

\[
\boxed{
\begin{array}{ll}
R_0<1/2:& \text{短圆本质，rank}=1,\ \text{覆盖展开并非塌缩};\\[2mm]
R_0>1/2\text{ 且域含 NUT}:&
\text{短圆可缩，相关基本群像 rank}=0.
\end{array}}
\]

## 4. 局部展开后的环带极限与 deficit

在小域的普适覆盖上令
\[
t=2\nu\psi.
\]
则
\[
4\nu^2F_\nu(d\psi+\cos\theta\,d\phi)^2
=
F_\nu(dt+2\nu\cos\theta\,d\phi)^2.
\]
在固定环带上，
\[
g_\nu\longrightarrow
g_0=
\frac{dr^2}{1+r^2/3}
+r^2d\Omega_2^2
+(1+r^2/3)dt^2.
\]
以
\[
r=\sqrt3\sinh(u/\sqrt3)
\]
改写：
\[
g_0=du^2
+3\sinh^2(u/\sqrt3)d\Omega_2^2
+\cosh^2(u/\sqrt3)dt^2.
\]
这是截面曲率 \(-1/3\) 的双曲四维度量：
\[
\operatorname{Ric}_{g_0}=-g_0,\qquad s_{g_0}=-4,\qquad W_{g_0}=0.
\]
因而 LeBrun 完全平方中的关键项不是趋零，而是
\[
\boxed{
(s+8\sqrt6\,|W^+|)^2\longrightarrow16.
}
\]
所以展开极限是非塌缩的 \(H^4\)，但不是 calibrated Einstein germ。Taub–NUT–AdS 避开 projector obstruction 的真正原因是 deficit 不小，而不是小域覆盖仍塌缩。

## 5. 全 Weyl 与 \(W^+\) 的取向及四倍约定

脚本中的量是四指标全 Weyl 范数；Step 6 使用的是
\(W^\pm:\Lambda^\pm\to\Lambda^\pm\) 的 Hilbert–Schmidt 范数。按给定二形式内积约定，
\[
\boxed{
|W|_{\rm tens}^2
=4\bigl(\|W^+\|_{\rm end}^2+\|W^-\|_{\rm end}^2\bigr).
}
\]
若所选取向把 Taub–NUT–AdS 的非零半部记为 \(W^+\)，则
\[
\|W^+\|_{\rm end}^2
=\frac{8\nu^2(4\nu^2-3)^2}{3(r+\nu)^6};
\]
反向取向则非零部分是 \(W^-\)。

calibrated 谱
\[
\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
满足
\[
\|W^+\|_{\rm end}^2=\frac1{24},
\]
对应的四指标全 Weyl 范数平方是
\[
|W|_{\rm tens}^2=\frac16,
\]
不是 \(1/24\)。

因此 `analyze_taub_nut_ads_multiscale.py` 直接解 `W2=1/24` 有四倍约定错误。正确过渡壳满足
\[
|W|_{\rm tens}^2=\frac16
\quad\Longleftrightarrow\quad
(r+\nu)^6=64\nu^2(4\nu^2-3)^2,
\]
于是
\[
\boxed{r\sim576^{1/6}\nu^{1/3}.}
\]

仅由 \(|W|^2\) 不能确定非零半部、简单特征值符号或 Riemann 符号约定。任何调用带符号 calibrated 谱的论证，都必须在同一取向、同一曲率符号和同一范数约定下直接计算 Weyl 端同态。

## 6. Homothety 的正确缩放

令
\[
\widehat g=a^2g.
\]
则联络不变，并且：

\[
\operatorname{Ric}_{\widehat g}
=\operatorname{Ric}_g
\quad\text{作为 }(0,2)\text{ 张量},
\]
\[
\boxed{
\widehat g^{-1}\operatorname{Ric}_{\widehat g}
=a^{-2}g^{-1}\operatorname{Ric}_g,
\qquad
s_{\widehat g}=a^{-2}s_g.
}
\]

Weyl 的 \((1,3)\) 形式不变，但作为二形式束上的曲率端同态，
\[
\boxed{
W^\pm_{\widehat g}=a^{-2}W^\pm_g,
\quad
\operatorname{Spec}(W^\pm_{\widehat g})
=a^{-2}\operatorname{Spec}(W^\pm_g).
}
\]
因此
\[
\|W^\pm_{\widehat g}\|=a^{-2}\|W^\pm_g\|,
\qquad
|W|_{\widehat g}=a^{-2}|W|_g,
\qquad
|W|_{\widehat g}^2=a^{-4}|W|_g^2.
\]
四维的 \(\int|W|^2\,d\mu\) 不变。

特别地，对
\[
\widetilde g=r_*^{-2}g
\]
有
\[
\operatorname{Ric}_{\widetilde g}
=-r_*^2\widetilde g,\qquad
s_{\widetilde g}=-4r_*^2,
\]
而 calibrated 谱应缩放为
\[
\boxed{
\operatorname{Spec}(W^+_{\widetilde g})
=
\left(-\frac{r_*^2}{6},
\frac{r_*^2}{12},
\frac{r_*^2}{12}\right).
}
\]
Step 9 中“谱数值保持不变”错误；保持的是谱比例及 calibration 关系的齐次形式。

一般地，禁止的 germ 应写为
\[
\operatorname{Ric}=-\kappa g,\qquad
\operatorname{Spec}(W^+)
=\left(-\frac\kappa6,\frac\kappa{12},\frac\kappa{12}\right),
\qquad \kappa>0.
\]
此时
\[
s=-4\kappa,\qquad
\|W^+\|^2=\frac{\kappa^2}{24},\qquad
\det W^+=-\frac{\kappa^3}{864}.
\]
常谱 harmonic-Weyl projector 论证给出 \(\nabla W^+=0\)，而标量 Weitzenböck 恒等式要求
\[
\boxed{|\nabla W^+|^2=\frac{\kappa^3}{16}>0.}
\]
故对每个固定 \(r_*>0\)，取 \(\kappa=r_*^2\) 后矛盾仍成立；只有
\(r_*\to0\) 时 \(\kappa\to0\)，矛盾退化为平直极限。

## 7. Taub–NUT–AdS 精确反驳什么

它反驳下述不带 deficit、且结论针对原球的纯局部命题：

> \(\operatorname{Ric}\ge-3g\) 且在距 NUT 为 \(1/2\) 的点周围，对所有  
> \(0<s\le1/3\) 有一致的 \(\fint_{B_s(p)}|\operatorname{Rm}|^2\) 控制，便能推出原度量球在某固定尺度四维非塌缩。

这里平均曲率趋于 \(8/3\)，但固定尺度体积为 \(\Theta(\nu)\)。

若把 Step 9 的命题严格表述为“较小缓冲域的局部普适覆盖必须非塌缩”，则 Taub–NUT–AdS **不是反例**：任何固定
\[
1/3<R_0<1/2
\]
的域都会展开纤维并趋于 \(H^4\)。

它也不反驳：

1. 所有半径直到 \(1\) 的一致曲率均值控制；
2. 缓冲域内所有中心的曲率极大函数控制；
3. maximal fiber rank 假设；
4. calibrated deficit 趋零的覆盖极限；
5. 闭 Ishida–LeBrun 序列的拓扑、Pontryagin 与 SW 约束；
6. Yau 第 26 题本身。

因此 Step 9 应作如下实质修正：

\[
\boxed{
\text{Taub–NUT–AdS 说明“曲率均值控制本身不排除原空间塌缩”，}
}
\]
但
\[
\boxed{
\text{它不说明所有局部普适覆盖仍塌缩；小域覆盖实际非塌缩。}
}
\]
其展开极限之所以不产生禁止的 calibrated germ，是因为
\[
\boxed{F_{\rm calibrated}\to16\neq0,}
\]
而非因为 NUT 型机制在所有固定缓冲尺度都阻止解绕。
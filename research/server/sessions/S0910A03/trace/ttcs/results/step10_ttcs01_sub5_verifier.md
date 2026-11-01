# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step9_regularity_false_and_new_direction.tex",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/scripts/verify_taub_nut_ads.py",
    "Sessions/S0910A03/workspace/scripts/compute_taub_nut_ads_curvature.py",
    "Sessions/S0910A03/workspace/scripts/analyze_taub_nut_ads_multiscale.py",
    "Sessions/S0910A03/staging/acquired/gr-qc_0202073__Classical_Boundary-value_Problem_in_Riemannian_Q_b30651e52bda5fb0/content.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Check and correct the Step-10 reassessment of Taub–NUT–AdS and scaling. Independently verify from the metric and the supplied symbolic scripts: (i) the exact |W|^2 formula, its value near the NUT, cumulative Weyl energy and all-radius curvature-mean behavior; (ii) whether a smaller fixed buffered domain around a point at distance 1/2 unwraps the short circle for all small nu; (iii) the locally unwrapped annular limit and its calibrated deficit; (iv) the correct homothetic scaling of Ricci endomorphism, Weyl endomorphism spectrum, |W|, and the forbidden calibrated Einstein germ. Decide precisely what Taub–NUT–AdS refutes and what it does not. Also flag orientation/factor-of-four convention issues between full Weyl and W+ before conclusions are used.

## Output

# 科学复核备忘录

## 1. 曲率张量与 NUT 邻域

令
\[
q_\nu=4\nu^2-3,\qquad
F_\nu(r)=\frac{r-\nu}{r+\nu}
\left(1+\frac{(r-\nu)(r+3\nu)}3\right).
\]
由 `compute_taub_nut_ads_curvature.py` 中先求导、再取
\(\theta=\pi/2\) 的直接张量缩并，并结合 \(SU(2)\)-不变性，得到
\[
\operatorname{Ric}_{g_\nu}=-g_\nu,\qquad s=-4,
\]
以及按四指标张量缩并计算的
\[
\boxed{
|W|_{\rm tens}^2
=
\frac{32\nu^2q_\nu^2}{3(r+\nu)^6}
},
\]
从而
\[
\boxed{
|\operatorname{Rm}|_{\rm tens}^2
=
\frac83+\frac{32\nu^2q_\nu^2}{3(r+\nu)^6}.
}
\]

`verify_taub_nut_ads.py` 本身没有计算 Christoffel 符号、Ricci 或 Riemann；其中相关文字是启发式说明。真正完成张量计算的是 `compute_taub_nut_ads_curvature.py`。

在 NUT 点 \(r=\nu\)，
\[
\boxed{
|W|_{\rm tens}^2(\nu)
=
\frac{q_\nu^2}{6\nu^4}
\sim \frac{3}{2\nu^4}.
}
\]
若写
\[
r=\nu+\frac{\rho^2}{8\nu},
\]
则
\[
|W|_{\rm tens}^2
=
\frac{q_\nu^2}{6\nu^4}
\left(1+\frac{\rho^2}{16\nu^2}\right)^{-6}.
\]
因此，对每个固定 \(\nu>0\)，NUT 是光滑点；但当 \(\nu\to0\) 时，曲率峰值按 \(\nu^{-4}\) 发散，并集中在 \(\rho=O(\nu)\) 的区域。近 NUT 的 Euclidean 展开只说明切锥平直，并不表示曲率随 \(\nu\to0\) 一致趋零。

另一个小修正是：若 \(p_\nu\) 到 NUT 的度量距离恰为 \(1/2\)，其 \(r\)-坐标并非严格等于 \(\nu+1/2\)。极限径向距离满足
\[
d_0(0,R)=\sqrt3\,\operatorname{arsinh}(R/\sqrt3),
\]
故
\[
r(p_\nu)\longrightarrow
\sqrt3\,\sinh\!\left(\frac1{2\sqrt3}\right).
\]
这不影响固定环带上的一致曲率估计。

---

## 2. 体积、累积 Weyl 能量和各尺度平均值

由
\[
d\mu
=
2\nu(r^2-\nu^2)\sin\theta\,
dr\,d\theta\,d\phi\,d\psi
\]
及
\[
0\le\theta\le\pi,\quad
0\le\phi\le2\pi,\quad
0\le\psi\le4\pi,
\]
完整轨道的径向体积密度是
\[
\boxed{
\frac{dV}{dr}=32\pi^2\nu(r^2-\nu^2),
}
\]
不是两个脚本中使用的 \(64\pi^2\nu(r^2-\nu^2)\)。该因子二的误差同时进入其能量和体积，所以脚本给出的平均值仍然正确，但累积体积和累积能量均多了一倍。

记
\[
\mathcal B_R=\{\nu\le r\le R\}.
\]
则
\[
\boxed{
V_\nu(R)
=
\frac{32\pi^2\nu}{3}(R-\nu)^2(R+2\nu)
}
\]
以及
\[
\boxed{
E^W_\nu(R)
=
\int_{\mathcal B_R}|W|_{\rm tens}^2\,d\mu
=
\frac{32\pi^2q_\nu^2}{9}
\frac{(R-\nu)^2(R^2+6R\nu+17\nu^2)}
{(R+\nu)^4}.
}
\]
因此
\[
\boxed{
\lim_{R\to\infty}E^W_\nu(R)
=
\frac{32\pi^2q_\nu^2}{9},
}
\]
并且当 \(\nu\to0\) 时该极限趋于 \(32\pi^2\)。所以 Weyl 能量是有限的；发散的是
\(\int|\operatorname{Rm}|^2\)，因为常数项 \(8/3\) 乘上无穷体积。

精确平均值为
\[
\boxed{
\fint_{\mathcal B_R}|W|_{\rm tens}^2
=
\frac{
q_\nu^2(R^2+6R\nu+17\nu^2)
}{
3\nu(R+\nu)^4(R+2\nu)
}.
}
\]
相应地，
\[
\fint_{\mathcal B_R}|\operatorname{Rm}|_{\rm tens}^2
=
\frac83+\fint_{\mathcal B_R}|W|_{\rm tens}^2.
\]

两种重要渐近为：

* 若 \(R=\nu x\)，其中 \(x>1\) 固定，则
  \[
  \fint_{\mathcal B_{\nu x}}|W|_{\rm tens}^2
  =
  \frac{q_\nu^2}{3\nu^4}
  \frac{x^2+6x+17}{(x+1)^4(x+2)}.
  \]
  NUT 尺度上的平均曲率按 \(\nu^{-4}\) 发散。

* 若坐标半径 \(R>0\) 固定，则
  \[
  \nu\fint_{\mathcal B_R}|W|_{\rm tens}^2
  \longrightarrow\frac3{R^3}.
  \]
  任何固定大小、包含 NUT 的区域都捕获渐近 \(32\pi^2\) 的 Weyl 能量，而其体积只有 \(O(\nu)\)。

---

## 3. 距 NUT 为 \(1/2\) 的点：小尺度与大尺度完全不同

取
\[
d(p_\nu,N_\nu)=\frac12.
\]
对任意 \(0<s\le1/3\)，
\[
B_s(p_\nu)\subset
\{1/6\le d(\,\cdot\,,N_\nu)\le5/6\}.
\]
这个环带的 \(r\)-坐标一致远离 \(\nu\)，故
\[
\sup_{B_{1/3}(p_\nu)}|W|_{\rm tens}^2=O(\nu^2),
\]
于是对所有 \(0<s\le1/3\)，
\[
\boxed{
\fint_{B_s(p_\nu)}|\operatorname{Rm}|_{\rm tens}^2
=
\frac83+O(\nu^2).
}
\]
另一方面，每个固定 \(s>0\) 的这类环带球满足
\[
\operatorname{Vol}B_s(p_\nu)=\Theta(\nu),
\]
所以任意固定尺度上的四维体积比趋于零。

但该估计不能延伸到所有 \(s\le1\)。若 \(s>1/2\) 固定，则
\[
B_{s-1/2}(N_\nu)\subset B_s(p_\nu)
\subset B_{s+1/2}(N_\nu).
\]
两端的 Weyl 能量都趋于 \(32\pi^2\)，而体积均为 \(\Theta(\nu)\)。因此
\[
\boxed{
\fint_{B_s(p_\nu)}|\operatorname{Rm}|^2
=
\Theta(\nu^{-1})
\qquad(s>1/2\ \text{固定}).
}
\]
特别地，以 \(p_\nu\) 为中心、截断半径为 \(1\) 的曲率极大函数并不一致有界。

---

## 4. 覆盖区域的大小决定短圆是否被展开

### 半径 \(1\) 的区域

在固定 \((\theta,\phi)\) 下，
\[
\{\,\nu\le r\le r(p_\nu),\ \psi\in S^1\,\}
\]
形成一张以 NUT 为中心的径向圆盘。圆盘上任一点到 \(p_\nu\) 的距离至多
\[
\frac12+O(\nu)<1.
\]
所以短 \(\psi\)-圆在 \(B_1(p_\nu)\) 中可缩。

环带小球 \(B_{1/3}(p_\nu)\) 的基本群由短圆生成，而其映入
\(\pi_1(B_1(p_\nu))\) 后为零。因此 \(B_1(p_\nu)\) 的局部普适覆盖在该小球上不给出沿 \(\psi\) 的新层；提升后的小球仍与原小球等距，体积仍为 \(\Theta(\nu)\)。

### 更小但仍有缓冲的固定区域

取任意
\[
\frac13<R_0<\frac12.
\]
在 \(B_{R_0}(p_\nu)\) 上圆作用没有固定点。商空间度量为
\[
q_\nu=
\frac{dr^2}{F_\nu(r)}
+(r^2-\nu^2)d\Omega_2^2,
\]
并在固定环带上光滑趋于三维曲率 \(-1/3\) 的双曲度量。

纤维长度为
\[
8\pi\nu\sqrt{F_\nu}=O(\nu),
\]
故对充分小的 \(\nu\)，整条 \(p_\nu\)-纤维位于
\(B_{R_0}(p_\nu)\) 中。投影是距离不增映射，并且
\(q_\nu\)-球是三维球；其逆像是平凡的 \(S^1\)-丛。纤维在该逆像的
\(\pi_1\) 中生成 \(\mathbb Z\)，因而不能在
\(B_{R_0}(p_\nu)\) 内缩掉。

所以：

\[
\boxed{
\text{对所有充分小的 }\nu,\ 
B_{R_0}(p_\nu)\text{ 的局部普适覆盖会展开短圆。}
}
\]

这也表明 fibered rank 依赖于所选缓冲区域：在含 NUT 的 \(B_1\) 中其像为零；在任何上述 \(B_{R_0}\) 中其像为秩一。

---

## 5. 展开后的环带极限及 calibrated deficit

在较小区域的普适覆盖上令
\[
t=2\nu\psi.
\]
于是
\[
4\nu^2F_\nu(d\psi+\cos\theta\,d\phi)^2
=
F_\nu(dt+2\nu\cos\theta\,d\phi)^2.
\]
在任意固定环带上，
\[
g_\nu\longrightarrow
g_0=
\frac{dr^2}{1+r^2/3}
+r^2d\Omega_2^2
+(1+r^2/3)dt^2.
\]
令
\[
r=\sqrt3\sinh(u/\sqrt3),
\]
则
\[
g_0=
du^2+3\sinh^2(u/\sqrt3)d\Omega_2^2
+\cosh^2(u/\sqrt3)dt^2.
\]
这是四维双曲度量，截面曲率为 \(-1/3\)，故
\[
\operatorname{Ric}_{g_0}=-g_0,\qquad s_{g_0}=-4,\qquad W_{g_0}=0.
\]

因此，LeBrun 完全平方中的度量项满足
\[
|\operatorname{Ric}+g|^2=0,
\]
但
\[
\boxed{
(s+8\sqrt6\,|W^+|)^2\longrightarrow16.
}
\]
若所选取向把非零 Weyl 半部放入 \(W^-\)，该项恒等于 \(16\)；若放入
\(W^+\)，固定环带上的 \(|W^+|\to0\)，结论相同。故这个展开极限不是 calibrated Einstein germ，也不具有趋零的 calibrated deficit。

---

## 6. 全 Weyl 张量与 \(W^+\) 的四倍因子

脚本计算的是
\[
W_{ijkl}W^{ijkl}.
\]
Step 6 中的 \(W^+\) 则是
\(\Lambda^+\to\Lambda^+\) 的对称无迹算子，其范数为 Hilbert–Schmidt 范数。两者满足
\[
\boxed{
|W|_{\rm tens}^2
=
4\bigl(\|W^+\|_{\rm op}^2+\|W^-\|_{\rm op}^2\bigr).
}
\]
若 Taub–NUT–AdS 的非零半部按所选取向是 \(W^+\)，则
\[
\boxed{
\|W^+\|_{\rm op}^2
=
\frac{8\nu^2q_\nu^2}{3(r+\nu)^6}.
}
\]
若取向相反，则这里的 \(W^+\) 为零。

Step 6 的 calibrated 谱
\[
\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
具有
\[
\|W^+\|_{\rm op}^2=\frac1{24}.
\]
若另一半为零，对应的四指标全 Weyl 范数平方是
\[
|W|_{\rm tens}^2=\frac16,
\]
不是 \(1/24\)。

因此 `analyze_taub_nut_ads_multiscale.py` 将其 `W2` 直接与 \(1/24\) 比较时有四倍误差。正确的过渡壳层满足
\[
(r+\nu)^6=64\nu^2q_\nu^2,
\]
所以当 \(\nu\to0\) 时
\[
r\sim576^{1/6}\nu^{1/3},
\]
而不是脚本所得的 \(2304^{1/6}\nu^{1/3}\)。

此外，\(|W|^2\) 只给出模长，不能确定：

1. 非零半部究竟是 \(W^+\) 还是 \(W^-\)；
2. 简单特征值的符号；
3. 所用 Riemann 张量符号是否与 Step 6 一致。

任何调用 calibrated 特征谱的论证都需要在同一取向和同一曲率符号下直接计算带符号的 Weyl 算子。

---

## 7. 常数 homothety 下的正确缩放

令
\[
\widehat g=a^2g,\qquad a>0.
\]
则 Levi-Civita 联络不变，并有
\[
\operatorname{Ric}_{\widehat g}
=
\operatorname{Ric}_g
\quad\text{作为 }(0,2)\text{ 张量},
\]
但 Ricci 端同态满足
\[
\widehat g^{-1}\operatorname{Ric}_{\widehat g}
=
a^{-2}g^{-1}\operatorname{Ric}_g.
\]
同时
\[
s_{\widehat g}=a^{-2}s_g.
\]

Weyl 的 \((1,3)\) 形式在常数共形变换下不变，但作为
\(\Lambda^+\to\Lambda^+\) 的曲率端同态，
\[
W^+_{\widehat g}=a^{-2}W^+_g.
\]
故
\[
\operatorname{Spec}(W^+_{\widehat g})
=
a^{-2}\operatorname{Spec}(W^+_g),
\qquad
\|W^+_{\widehat g}\|=a^{-2}\|W^+_g\|.
\]
四指标 Weyl 范数也按 \(a^{-2}\) 缩放，范数平方按 \(a^{-4}\) 缩放；四维的
\(\int|W|^2d\mu\) 保持不变。

特别地，若
\[
\widetilde g=r_*^{-2}g,\qquad \operatorname{Ric}_g=-g,
\]
则
\[
\operatorname{Ric}_{\widetilde g}
=
-r_*^2\widetilde g,
\qquad
s_{\widetilde g}=-4r_*^2,
\]
且 calibrated 谱变成
\[
\boxed{
\operatorname{Spec}(W^+_{\widetilde g})
=
\left(
-\frac{r_*^2}{6},
\frac{r_*^2}{12},
\frac{r_*^2}{12}
\right).
}
\]
所以 Step 9 中“谱保持不变”的表述不正确；保持的是齐次关系，而不是数值。

更一般地，令 \(\kappa>0\)。禁止出现的 germ 应写成
\[
\operatorname{Ric}=-\kappa g,\qquad
\operatorname{Spec}(W^+)
=
\left(-\frac\kappa6,\frac\kappa{12},\frac\kappa{12}\right).
\]
此时
\[
s=-4\kappa,\qquad
\|W^+\|^2=\frac{\kappa^2}{24},\qquad
\det W^+=-\frac{\kappa^3}{864}.
\]
常谱 projector 论证给出 \(\nabla W^+=0\)，而标量 Weitzenböck 恒等式给出
\[
|\nabla W^+|^2=\frac{\kappa^3}{16}.
\]
只要 \(\kappa>0\)，二者不相容。对每个固定 \(r_*>0\)，这里
\(\kappa=r_*^2>0\)，故原来的局部排除仍成立。若 \(r_*\to0\)，则
\(\kappa\to0\)，极限变成平直情形，矛盾量也趋零。

位于
\(r\asymp\nu^{1/3}\) 的 calibrated 模长壳层在原度量中趋向 NUT。若把该壳层放大到单位大小，homothety 同时使 Einstein 常数和 Weyl 谱趋零；所得极限仍是平直模型，而不是固定 \(\kappa>0\) 的 calibrated germ。

---

## 8. Taub–NUT–AdS 精确排除了什么

它确实给出下述局部命题的反例：

> 只假设 \(B_1(p)\) 的局部普适覆盖上  
> \(\operatorname{Ric}\ge-3g\)，并且仅对提升点为中心的  
> \(0<s\le1/3\) 有  
> \(\fint_{B_s(\tilde p)}|\operatorname{Rm}|^2\le K\)，  
> 就能推出某个固定尺度上的四维非塌缩。

在当前序列中，这些平均值趋于 \(8/3\)，而固定尺度体积为
\(\Theta(\nu)\)。

它没有排除以下更强的几何输入：

* 以 \(p_\nu\) 为中心、所有半径直到 \(1\) 的曲率平均一致有界；NUT 使这些平均值达到 \(\Theta(\nu^{-1})\)。
* 在整个缓冲区域内对所有中心控制曲率极大函数；NUT 邻域有 \(\nu^{-4}\) 峰值。
* 使用任意 \(1/3<R_0<1/2\) 的较小缓冲区域；其普适覆盖会展开短圆并趋于非塌缩的双曲四维模型。
* 同时要求 calibrated deficit 趋零；环带上的完全平方项趋于 \(16\)。
* 闭的临界 Ishida–LeBrun 流形序列或 Yau 第 26 题本身。

最后，NUT 核心并不需要无穷 Weyl 能量：当 \(\nu\to0\) 时，每个核心携带约
\(32\pi^2\) 的四指标 Weyl 能量，或在非零半部的算子范数约定下携带约
\(8\pi^2\)。Taub–NUT–AdS 的全曲率积分发散来自无穷体积的双曲端，而不是 NUT 曲率集中本身。
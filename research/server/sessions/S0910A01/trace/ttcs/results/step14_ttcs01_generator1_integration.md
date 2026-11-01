# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 14,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step14_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step14_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop concrete mathematical bridges from localized Ricci-flow smoothing to the existing calibrated-Einstein-germ obstruction in the LeBrun negative branch. Assume a sequence with Ric+g -> 0, global calibrated W+ defect o(Vol), and a maximal-function set with bounded local |Rm|^2 mean. Explore two possibilities: (A) use local smoothing only to obtain bounded-curvature collapsed structure or cover charts and then transfer that chart/control back to the original metric where defects are small; (B) run a normalized/local Ricci flow and prove the Einstein error and calibrated W+ residual remain small at a fixed small time. Derive the relevant evolution/compactness estimates at a level sufficient to identify a plausible theorem or a decisive obstruction. Keep the rank-one reduced equations as context but do not assume exact symmetry.

## Integrated Scientific Memo

## 局部 Ricci-flow 平滑到 calibrated Einstein germ 的桥梁

设四维闭流形上的序列满足
\[
E_i(0):=\Ric_{g_i}+g_i,\qquad \|E_i(0)\|_{L^\infty}\to0,
\]
以及全局 calibrated \(W^+\) 缺陷为 \(o(\Vol g_i)\)。在 maximal-function 好点集上，假设对所有 \(0<\rho\le R\)
\[
\fint_{B_\rho(p)}|\Rm(g_i)|^2\le K_0 .
\]

核心结论是：

1. **固定小尺度确实可满足 Li 型临界能量条件**；
2. **单纯的 \(|\Rm(t)|\le C/t\) 不足以保持近 Einstein 性或 calibration**；
3. 路线 A 最稳健，但仍需要一个真正的 cover-rank/accessibility 输入；
4. 路线 B 可通过“Einstein 稳定性 + 拓扑重新校准”实现，直接输运 \(W^+\) 则需要更强的抛物型估计。

---

### 1. 从 maximal-function 好球到固定尺度平滑输入

取 \(p_i\) 为好点，并假设
\[
\fint_{B_{4r}(p_i)}|\Rm|^2\le K_0.
\]
若 \(q\in B_r(p_i)\)，则 \(B_r(q)\subset B_{2r}(p_i)\)。由 \(\Ric\ge-3g+o(1)\) 下的相对 Bishop–Gromov 比较，
\[
\frac{\Vol B_{2r}(p_i)}{\Vol B_r(q)}
 \le \frac{V_{-1}(3r)}{V_{-1}(r)}
 \le C_{BG}\qquad (r\le1),
\]
故
\[
\fint_{B_r(q)}|\Rm|^2\le C_{BG}K_0.
\]
于是
\[
\frac{r^4}{\Vol B_r(q)}
\int_{B_r(q)}|\Rm|^2
\le C_{BG}K_0r^4.
\]
取一次性固定的
\[
r_*\le
\left(\frac{\varepsilon_{\rm Li}}{2C_{BG}K_0}\right)^{1/4},
\]
即可在缓冲区内每个中心满足 Li 的无量纲小能量条件。这里 \(r_*>0\) 与 \(i\) 无关，因此负 Einstein 归一化尺度没有在极限中消失。

但当前材料中的 Li 定理是 complete/all-centers 版本；Huang–Wang 的局部定理虽然是真正局部的，却额外要求：

- 每点 GH 接近低维欧氏模型；
- pseudo-local fundamental group 具有最大幂零秩。

因此仍需要以下内部版本之一：

> **局部 Li 平滑命题。**  
> 若缓冲球内所有中心满足上述临界小能量条件，且初始 Ricci 双边有界，则在更小内球上存在统一时间 \(cr_*^2\) 的局部流，并有
> \[
> |\Rm(g(t))|\le C/t .
> \]

Huang–Wang 不能仅由 maximal-function 能量条件推出这一命题；其模型与秩假设恰是 accessibility 问题的一部分。

---

## 2. 归一化流与 Einstein 误差

将非归一化流 \(\bar g(s)\) 化为使 \(\Ric=-g\) 静止的归一化流：
\[
g(t)=e^{-2t}\bar g\!\left(\frac{e^{2t}-1}{2}\right),
\qquad
\partial_tg=-2(\Ric_g+g)=-2E.
\]

Einstein 误差满足
\[
\boxed{
(\partial_t-\Delta)E_{ij}
=
2R_{ikjl}E^{kl}-2E_i{}^kE_{kj}
}
\]
以及
\[
\boxed{
(\partial_t-\Delta)|E|^2
=
-2|\nabla E|^2+
4R_{ikjl}E^{ij}E^{kl}.
}
\]
特别地，
\[
(\partial_t-\Delta)|E|^2
\le C|\Rm|\,|E|^2.
\]

### \(C/t\) 曲率界本身不够

若只知道 \(|\Rm(t)|\le C/t\)，则势项在 \(t=0\) 不可积。标量模型
\[
y_i'(t)=\frac{C}{t+\kappa_i^{-1}}y_i(t),
\qquad y_i(0)=\delta_i
\]
给出
\[
y_i(t)=\delta_i(1+\kappa_it)^C.
\]
即使 \(\delta_i\to0\)，只要初始曲率尺度 \(\kappa_i\) 增长更快，固定正时刻的误差也未必趋零。因此不能从 Li 曲率估计直接断言
\[
E_i(t_*)\to0.
\]

### 需要的临界 form estimate

在四维，若缓冲球上有体积归一化 Sobolev 不等式
\[
\left(\fint |\phi|^4\right)^{1/2}
\le S\left(r^2\fint|\nabla\phi|^2+\fint\phi^2\right)
\]
和
\[
r^4\fint|\Rm|^2\le\varepsilon,
\]
则 Hölder 给出
\[
\int |\Rm|\,\phi^2
\le
S\varepsilon^{1/2}\int|\nabla\phi|^2
+
CS\varepsilon^{1/2}r^{-2}\int\phi^2.
\tag{2.1}
\]
若此 form-smallness 沿局部流在内区保持，且
\(S\varepsilon^{1/2}\) 足够小，则对 \(E\) 的 cutoff 能量估计可吸收曲率势项，得到
\[
\sup_{0<t\le\theta r^2}
\fint_{B_{2r}}|E(t)|^2
+
\int_0^{\theta r^2}\fint_{B_{2r}}|\nabla E|^2\,dt
\le
C\|E(0)\|_\infty^2.
\tag{2.2}
\]
再在 \(t\in[\theta r^2/2,\theta r^2]\) 使用有界曲率、Shi 型估计和抛物平均值不等式，可望推出
\[
\sup_{B_r}|E(\theta r^2)|
+
\sum_{m=1}^k(\theta r^2)^{m/2}
\sup_{B_r}|\nabla^mE(\theta r^2)|
\le
C_{k,\theta}\|E(0)\|_\infty.
\tag{2.3}
\]

这精确标识了所需的新分析结果：不只是局部存在与 \(C/t\) 曲率界，而是**临界曲率 form-smallness 的保持及 Einstein 张量稳定性**。在完全塌缩环境中，普通未加权 Sobolev 常数可能退化；因此 (2.1) 不能仅由原始球上的平均能量自动推出。可行位置是：

- 最大秩 normal cover，在其上 Huang–Wang 的 Lemma 2.4 给出近欧氏体积与等周常数；
- 或 Li 四维证明中真正不依赖非塌缩的临界吸收机制。

---

# 3. 路线 A：只用平滑建立 cover，再回到原度量

这是避免输运 calibrated \(W^+\) 的优选桥梁。

### 3.1 正时刻建立 bounded-curvature collapse structure

令
\[
t_*=\theta r_*^2.
\]
平滑后
\[
|\Rm(g_i(t_*))|\le C(\theta)r_*^{-2},
\]
且正时间导数也受控。若该区域同时具有低维 GH 模型和最大 pseudo-local 幂零秩，则 Huang–Wang 的机制在 local normal cover 上给出近欧氏体积/等周控制，并可产生 infranil 结构或固定尺度 noncollapsed cover。

重要的是：**有界曲率本身不产生最大秩 cover**。若幂零秩小于维数亏损，平滑后仍可能发生“未被局部基本群展开”的额外塌缩。这是路线 A 的决定性拓扑障碍。

### 3.2 从正时刻向 \(t=0\) 转移

归一化流有精确关系
\[
\partial_t\log g(t)(v,v)
=
-2\,\frac{E(t)(v,v)}{g(t)(v,v)}.
\]
定义
\[
L_i(t_*):=\int_0^{t_*}\|E_i(t)\|_{\op,\infty}\,dt.
\]
则
\[
e^{-2L_i}g_i(0)\le g_i(t_*)\le e^{2L_i}g_i(0),
\tag{3.1}
\]
并且四维体积元满足
\[
e^{-4L_i}dV_{g_i(0)}
\le dV_{g_i(t_*)}
\le e^{4L_i}dV_{g_i(0)}.
\tag{3.2}
\]
因此：

- \(L_i\le L<\infty\) 足以把固定尺度 noncollapse 从 \(g_i(t_*)\) 转回 \(g_i(0)\)；
- \(L_i\to0\) 则给出渐近等距转移。

Huang–Wang 的距离失真估计本身不够替代 (3.1)。其典型输出是 Hölder 或 \(O(\sqrt t)\) 型距离控制，在自然平滑尺度 \(\sqrt t\) 上并不趋于相对零，不能直接保持固定 harmonic radius 或 tile multiplicity。

### 3.3 cover 是拓扑对象

若正时刻得到 normal cover
\[
\pi_i:\widetilde U_i\to U_i,
\]
同一 covering map 可拉回原度量 \(\pi_i^*g_i(0)\)。若
\[
\Vol_{\pi_i^*g_i(t_*)}
B(\tilde p_i,\rho)\ge v_*\rho^4,
\]
则由 (3.1)–(3.2)
\[
\Vol_{\pi_i^*g_i(0)}
B(\tilde p_i,c(L)\rho)
\ge c(L,v_*)\rho^4.
\tag{3.3}
\]

但原球上的 \(L^2\) 平均界向大 cover 球的转移必须另外证明。仅“每个 tile 同样重复”并不自动成立，因为：

- cover 球未必恰由等形 fundamental tiles 构成；
- 初始度量不具精确 circle/infranil 对称性；
- 边界 tile 和不同 deck displacement 可能改变计数。

可靠的替代是对所有 lift-center 都具有统一原始小球平均界，再用有界重叠 covering 将 cover 球分解为等半径小球。若每个小球满足
\[
\int_{B_s(\tilde q)}|\Rm|^2
\le K_1\Vol B_s(\tilde q),
\]
且 cover 已 noncollapsed、Ricci 有界，则有界重叠求和给出 cover 球上的同类平均控制。

### 3.4 回到原度量并产生 forbidden germ

在 \(\pi_i^*g_i(0)\) 上，固定尺度 noncollapse、Ricci 双边界以及临界 \(L^2\) 曲率小量应给出统一有限 \(p>4\) 的 \(W^{2,p}\) harmonic radius。取子列，
\[
\pi_i^*g_i(0)\to h
\quad\text{于 }W^{2,p}_{\loc}.
\]
由于
\[
\Ric_{g_i(0)}+g_i(0)\to0,
\]
极限满足
\[
\Ric_h=-h,
\]
并由椭圆自举光滑。

必须在选点时同时使用 calibrated 缺陷的 maximal-function 控制，使每个固定内球上
\[
\fint |P(W_i^+)|\to0,
\qquad
P(A):=A^2+\frac1{12}A-\frac1{72}I.
\]
对 trace-free 对称 \(A:\Lambda^+\to\Lambda^+\)，
\[
P(A)=0
\iff
\Spec A=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
强 \(W^{2,p}\) 收敛足以传递此局部缺陷，故
\[
P(W_h^+)=0.
\]
于是得到被既有 Derdziński 论证排除的 calibrated Einstein germ。

因此路线 A 的充分命题可表为：

> **局部 smoothing-accessibility 定理。**  
> 在缓冲好球上，Li 临界小能量平滑若同时产生最大秩 normal cover，并满足
> \[
> \int_0^{t_*}\|E(t)\|_\infty dt\le L,
> \]
> 则正时刻 cover 的固定尺度 noncollapse 可转移到初始度量；结合原始 Ricci 界、局部临界能量及 calibrated 缺陷，可产生 forbidden calibrated Einstein germ。

---

# 4. 路线 B：直接使用正时刻度量

若 (2.3) 成立，则在固定 \(t_*>0\)
\[
E_i(t_*)\to0
\]
且在最大秩 normal cover 上可取得光滑极限
\[
\pi_i^*g_i(t_*)\to h,\qquad \Ric_h=-h.
\]
剩余问题是 \(W^+\) calibration。

## 4.1 直接输运 calibration 的困难

沿 \(\dot g=-2E\)，Weyl 张量的一阶变分具有结构
\[
\partial_tW^+
=
\Pi_+(\nabla^2E)+\Rm*E.
\tag{4.1}
\]
因此
\[
|\partial_tP(W^+)|
\le
C(1+|W^+|)
\bigl(|\nabla^2E|+|\Rm||E|\bigr).
\tag{4.2}
\]
由正时间抛物正则性通常只能预期
\[
|\nabla^2E(t)|\lesssim \delta_i/t,
\]
其时间积分在 \(0\) 附近有对数发散。故初始
\(\|E_i(0)\|_\infty\to0\) 与 \(|\Rm|\le C/t\) 不足以推出固定时刻 calibration。

足够的直接输运条件是
\[
\int_0^{t_*}\!\!\int_U
(1+|W^+|)
\bigl(|\nabla^2E|+|\Rm||E|\bigr)
=o(\Vol U).
\tag{4.3}
\]
这需要体积归一化临界空间上的抛物 maximal regularity；(2.2) 只控制 \(\nabla E\)，尚未达到 (4.3)。

## 4.2 拓扑重新校准比直接输运更合理

在同一闭流形上，Chern–Weil 数不随流改变：
\[
4\pi^2(2\chi+3\tau)
=
\int_M\left(
2|W^+|^2+\frac{s^2}{24}
-\frac12|\Ric_0|^2
\right)dV.
\tag{4.4}
\]
若 (2.3) 与 \(L_i(t_*)\to0\) 成立，则
\[
s_i(t_*)=-4+o(1),\qquad
\Ric_{0,i}(t_*)=o(1),
\]
且体积与初始时刻相差 \(o(\Vol)\)。于是 (4.4) 可恢复正时刻的 \(W^+\) 总范数：
\[
\fint |W_i^+(t_*)|^2=\frac1{24}+o(1),
\tag{4.5}
\]
前提是初始拓扑/体积关系确实给出该常数。

但 (4.5) 只固定范数，不固定谱型。若 \(w(A)=\lambda_{\min}(A)\)，则任意 trace-free 对称 \(3\times3\) 矩阵满足
\[
w(A)+\sqrt{\frac23}|A|\ge0,
\tag{4.6}
\]
等号当且仅当谱为
\[
(-2a,a,a).
\]
因此还需 LeBrun/Seiberg–Witten 的**对所有同一光滑流形上的度量成立**的曲率不等式及其非负余项，证明正时刻
\[
\int_M
\left(
w(W_i^+)+\sqrt{\frac23}|W_i^+|
\right)dV
=o(\Vol).
\tag{4.7}
\]
结合 (4.5) 才能重新得到目标谱
\[
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

目前给定材料没有提供该 LeBrun 不等式的精确常数与 equality remainder，因此拓扑重新校准是一个明确可检验的候选桥梁，而非已经完成的证明。

---

## 5. rank-one reduced equations的作用与限制

精确恒等式
\[
H=
\frac13I+\frac14(|z|^2I-z\otimes z)
-\frac12(W^++W^-)
\]
表明 calibrated \(W^+\) 不控制 \(H\) 的符号。若
\[
\lambda_{\min}(H)\le-\eta,
\]
则必有
\[
\lambda_{\max}(W^-)\ge \frac7{12}+2\eta
\]
并产生阶一 derivative-twist 代价。因此 reduced equations 解释了 smoothing 后可能暴露的障碍：反自对偶曲率或导数扭曲可以在保持 \(W^+\) calibration 时破坏简单 rank-one 重建。

但这一点既不构造全局塌缩序列，也不替代 cover-rank 分析。且即使 \(H\ge0\)，Ricci 下界只给相对 Bishop–Gromov 比较，并不给绝对体积锚点。

---

## 6. 精确剩余障碍

要闭合 smoothing-to-germ 桥梁，仍需解决三个彼此独立的对象：

1. **局部化：**  
   从缓冲区 all-centers Li 小能量条件推出内球统一局部流。

2. **抛物稳定性：**  
   证明临界 form-smallness 沿流保持，从而得到 (2.2)–(2.3)，至少得到
   \[
   \int_0^{t_*}\|E(t)\|_\infty dt\le L
   \]
   且最好趋零。

3. **accessibility/rank：**  
   证明在 calibrated 好集的正体积部分，正时刻 bounded-curvature collapse 具有最大 pseudo-local 幂零秩；否则 Huang–Wang 的 normal-cover noncollapse 机制不可应用。

路线 B 还需二选一：

- 证明 Weyl 输运估计 (4.3)；
- 或核验精确的 metric-uniform LeBrun equality remainder，以由 (4.4)–(4.7) 在正时刻重新校准。

因此，现有证据支持的最强判断是：**固定尺度 Li 平滑消除了“背景曲率非小”的尺度障碍，但没有消除 localization、Einstein 稳定性和 maximal-rank cover 三个真正障碍。路线 A 避免了最困难的 Weyl 输运，因而只要获得 integrated Einstein control 与最大秩 cover，就能把原始缺陷直接送入既有 forbidden-germ 机制。**
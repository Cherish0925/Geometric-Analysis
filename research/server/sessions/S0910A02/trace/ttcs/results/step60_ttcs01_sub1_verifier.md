# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step60_resonant_h4_neck_drift_and_alf_flux.md",
    "Sessions/S0910A02/workspace/data/step60_resonant_flux_neck_alf.json",
    "Sessions/S0910A02/workspace/data/step60_neck_drift_schedules.json",
    "Sessions/S0910A02/workspace/data/step60_warp_neck_drift_model.json",
    "Sessions/S0910A02/workspace/notes/step59_h4dual_two_scale_matching_analysis.md",
    "Sessions/S0910A02/workspace/notes/step34_indicial_modediag_resonance_and_collapse.md",
    "Sessions/S0910A02/workspace/notes/step42_mode_projection_bridge_resolution.md",
    "Sessions/S0910A02/workspace/notes/step11_cz_spike_and_proposition_A.md"
  ]
}
```

## Task

Verify the mathematical substance of the Step-60 correction for Yau-26. Read the Step-60 note and supporting data, with the Step-59 and Step-34/42 context. Check scale conventions, the l=2 Wronskian/log resonance, the claim that H4 necessity is only rate-limited by delta_i log(1/t_i)->0 (conditional on annular gauge/projection), the local opposite-warping neck-drift model, and the first ALF scalar flux model. Identify any serious mathematical error, hidden assumption, or overstatement; also state which parts look sound and what the next decisive computation/proof should be. Do not decide the whole Yau-26 problem; focus on this correction and its consequences.

## Output

# Step 60 数学复核备忘录

## 总体评价

Step 60 对 Step 34/42 的固定环带论证所作修正，在核心尺度和一维 Wronskian 计算上是正确的：

- 若 \(t_i\) 表示长度平方尺度，则 ALE 坐标半径为 \(R_i\asymp t_i^{-1/2}\)；
- \(l=2\) 模式确实有根 \(2,-4\)，以 \(r^{-4}\) 模式配对时，常值投影源产生 \(\log R_i\)；
- Ricci 缺陷对归一化 \(H_2\) 通量的最坏贡献确为
  \[
  O\!\left(\delta_i\log\frac1{t_i}\right).
  \]
  因而固定泡坐标环带不能自行识别外部 orbifold 的 \(H_2\) 系数。

不过，当前材料得到的是一个可靠的一维通量估计，而不是已经闭合的几何必要性定理。最重要的缺口是：必须证明实际张量方程的内外端面通量、EH 参数调制、非线性项和规范项具有所需的 \(o(t_i)\) 控制。局部反向翘曲计算也只验证了线性 Laplace 通道；按 JSON 中采用的半径关系，其精确 Ricci 张量还含有过大的二次梯度项。ALF 标量模型本身正确，但尚不能决定 ALF 张量通量或塌缩泡的类型。

---

## 1. 尺度约定是相容的，但应显式写成拉回与缩放

令
\[
F_i(y)=\sqrt{t_i}\,y,\qquad
\widetilde g_i=t_i^{-1}F_i^*g_i .
\]
若
\[
Z_i=\operatorname{Ric}_{g_i}-\Lambda g_i,
\qquad |Z_i|_{g_i}\le\delta_i,
\]
则
\[
\operatorname{Ric}_{\widetilde g_i}
 =\Lambda t_i\widetilde g_i+F_i^*Z_i,
\qquad
|F_i^*Z_i|_{\widetilde g_i}\le t_i\delta_i.
\]
所以 Step 60 使用的 ALE 源强度 \(t_i\delta_i\) 正确。

Step 34/42 使用的是长度参数；若记其参数为 \(a_i\)，则
\[
t_i=a_i^2,\qquad a_i^4=t_i^2.
\]
这解释了 Step 34 的 EH 插入系数 \(a_i^4\) 与 Step 60 的尺度并不矛盾。

若外部匹配发生在固定 orbifold 半径 \(\eta\)，精确关系是
\[
R_i=\frac{\eta}{\sqrt{t_i}},
\qquad
\log R_i=\frac12\log\frac1{t_i}+\log\eta.
\]
因此 \(R_i\sim t_i^{-1/2}\) 在固定 \(\eta\) 时可用；若 \(\eta=\eta_i\) 也变化，\(\log\eta_i\) 必须保留。

---

## 2. \(l=2\) 共振与 \(1/12\) 系数

对
\[
Lf=f''+\frac3r f'-\frac8{r^2}f
\]
有
\[
L(r^\alpha)=(\alpha-2)(\alpha+4)r^{\alpha-2},
\]
故齐次解为 \(r^2,r^{-4}\)，且
\[
r^3\bigl(r^2(r^{-4})'-r^{-4}(r^2)'\bigr)=-6.
\]

以 \(o=r^{-4}\) 配对并定义
\[
\Phi(r)=r^3\bigl(f\,o'-o\,f'\bigr),
\]
若 \(Lf=S(r)\)，则符号约定之外有
\[
\Phi'(r)=-r^3o(r)S(r)=-\frac{S(r)}r.
\]
因此常值源产生
\[
|\Phi(R)-\Phi(r_0)|
 \le |S|\log\frac R{r_0}.
\]
等价地，增长系数改变
\[
\Delta A_2=\frac S6\log\frac R{r_0}+O(S).
\]

Step 60 给出的精确特解
\[
f_p(r)=\frac S6r^2\log\frac r{r_0}
-\frac S{36}\left(r^2-r_0^6r^{-4}\right)
\]
确实满足 \(Lf_p=S\) 以及 \(f_p(r_0)=f_p'(r_0)=0\)。

取 \(S=t_i\delta_i\)、\(R_i=t_i^{-1/2}\)，得到
\[
\Delta A_2
 =\frac{t_i\delta_i}{12}\log\frac1{t_i}+O(t_i\delta_i).
\]
相对于 \(t_i\kappa\) 的信号，这给出
\[
O\!\left(\delta_i\log\frac1{t_i}\right).
\]
JSON 中的 \(1/12\) 只属于这个标量归一化；几何 Lichnerowicz 算子、张量球谐函数归一化及 \(P=\frac12\nabla^*\nabla-\mathring R\) 的约定会改变常数，但不会改变对数尺度。

### 加权估计部分

对 \(\beta<2\)，若加权范数采用 \(O(r^\beta)\) 约定，则
\[
\|E_i\|_{C^0_{\beta-2}}
 \asymp t_i\delta_iR_i^{2-\beta}
 =\delta_i t_i^{\beta/2}.
\]
与紧集上所需的 \(O(t_i)\) 相比，比例为
\[
\delta_i t_i^{\beta/2-1}.
\]
例如 \(\delta_i=\log^{-2}(1/t_i)\) 时，该比例对每个固定 \(\beta<2\) 最终趋于无穷。Step 60 对 Step 59 加权估计的纠正因此成立。

这排除了 Step 59 中那种直接、统一的固定权重估计；它并不排除投影后估计、双权重空间或令 \(\beta\to2\) 的对数加权方法。后一类方法会重新产生同一个对数项。

---

## 3. 几何必要性还需要一个更精确的通量命题

在完整张量论证中，理想形式应是
\[
c_k\left\langle R_\pm(p)\zeta,\zeta_{(k)}\right\rangle
 =
 \frac{\Phi_{k,\mathrm{in}}}{t_i}
 +O\!\left(\delta_i\log R_i\right)+o(1),
\]
并通过 EH 参数正交化证明
\[
\frac{\Phi_{k,\mathrm{in}}}{t_i}\longrightarrow0.
\]
在此形式下，
\[
\delta_i\log(1/t_i)\to0
\]
才推出 \(R_\pm(p)\zeta=0\)。

Step 60 写成
\[
\lambda_k=c\langle R_\pm(p)\zeta,\zeta_{(k)}\rangle
+O(\delta_i\log(1/t_i))
\]
时，\(\lambda_k\) 的含义不够明确。仅有这条等式并不能推出右侧曲率向量为零；还必须证明 \(\lambda_k\to0\)，或直接把 \(\lambda_k\) 定义为已经归一化并趋零的内端通量。

所需的几何内容包括：

1. 在整段 \(1\le r\le\eta/\sqrt{t_i}\) 上构造相容的 Bianchi 规范；
2. 证明所选 EH 障碍张量的投影确实化为上述 \(l=2\) 方程；
3. 调整 EH 尺度与方向参数，消去核方向的内端通量；
4. 证明非线性项、规范交换项以及 EH 与平锥算子之差，在与 \(o_k\sim r^{-4}\) 配对后总计为 \(o(t_i)\)；
5. 定量控制已减去的 \(H_2/H_4\) 环境展开直到增长半径；
6. 证明外端通量除以 \(t_i\) 收敛到 orbifold 曲率配对。

Step 42 的固定泡坐标环带只能测量泡一侧已有的增长系数。没有 \(h_i=O(t_i)\) 的紧集速率，它不能证明该系数等于外部 orbifold 的二阶系数。Step 60 对这一逻辑循环的指出是正确的。

还有一个相关公式应修正。对
\[
E=\operatorname{Ric}-\Lambda g
\]
并非一般有 \(\operatorname{div}E=0\)，而是
\[
\nabla^iE_{ij}=\frac12\nabla_j\operatorname{tr}E.
\]
这仍不足以消去共振，因为 \(C^0\) Ricci 夹逼没有给出 \(\nabla E\) 控制；但 Step 34 中“总误差无散”的说法不准确。

---

## 4. 指数尺度描述需要两侧指数估计

若
\[
t_i=e^{-a/\delta_i},
\]
则标量模型给出
\[
\frac{\delta_i}{12}\log\frac1{t_i}=\frac a{12}.
\]
JSON 中 \(a=3,12\) 对应 \(1/4,1\)，数值正确。

但
\[
t_i\lesssim e^{-c/\delta_i}
\]
只推出
\[
\delta_i\log(1/t_i)\gtrsim c,
\]
并不推出该量为 \(O(1)\)。若要同时得到上下常数量级，应写成
\[
e^{-C/\delta_i}\lesssim t_i\lesssim e^{-c/\delta_i}.
\]
更小的 \(t_i\) 允许通量上界进一步增大；也可通过采用小于允许上界的 Ricci 源，把实际漂移调成常数量级。

---

## 5. 反向翘曲模型：Laplace 恒等式正确，但 JSON 尚未控制精确 Ricci

恒等式
\[
\Delta\!\left[t r^2A(\log r)\cos2\theta\right]
=t\left(A''+4A'\right)\cos2\theta
\]
完全正确。若 \(A\) 在对数长度 \(L\) 上改变 \(O(1)\)，则
\[
|\Delta u|\le C\frac tL.
\]

但是对最简单的精确度量
\[
g_u=dx^2+dy^2+e^{2u}d\theta^2+e^{-2u}d\varphi^2
\]
可直接算得
\[
(\operatorname{Ric}_{g_u})_{ab}=-2u_a u_b,\qquad
\operatorname{Ric}_{\theta\theta}=-\Delta u,\qquad
\operatorname{Ric}_{\varphi\varphi}=+\Delta u
\]
（纤维分量取单位正交标架）。

而
\[
|\nabla u|\le Ct r\bigl(|A|+|A'|\bigr).
\]
按 JSON 使用的
\[
R=e^L=t^{-1/2}
\]
有
\[
\sup_{r\le R}|\nabla u|^2\asymp t,
\]
而所需 Ricci 缺陷是 \(O(t\delta)\)。因此数据中的“Ricci/Laplacian source \(O(t\delta)\)”对精确翘曲度量并不成立；当前脚本只验证了线性 Laplace 项。

这一问题存在一个值得保留的修正尺度。若外部 orbifold 半径取
\[
\eta_i^2\asymp\delta_i,\qquad
R_i=\frac{\eta_i}{\sqrt{t_i}},
\]
则
\[
\sup|\nabla u|^2\le Ct_i\eta_i^2\le Ct_i\delta_i.
\]
再取
\[
L_i=\log R_i\asymp\frac a{\delta_i},
\]
便有
\[
t_i=\eta_i^2e^{-2L_i}
 \asymp \delta_i e^{-2a/\delta_i},
\qquad
|\Delta u|\le Ct_i\delta_i.
\]
所以二次梯度项未必摧毁长颈机制，但需要使用逐渐缩小的外部半径，而不是 JSON 中的 \(\eta=1\)。随后还需把该模型叠加到满足 \(\operatorname{Ric}=\Lambda g\) 的局部二阶展开上，并计算所有交叉项。

另外：

- \(q(z)=3z^2-2z^3\) 只有一阶导数在端点为零，直接接常值函数不能得到光滑度量；可改用在两端恒定的 \(C^\infty\) 轮廓，导数量级仍为 \(L^{-1},L^{-2}\)。
- 二维基底上的 \(\cos2\theta\) 模式是否对目标 EH 障碍张量 \(o_k\) 有非零投影，尚未计算。
- 当前局部空间是双纤维翘曲环带，不是 \(S^3/\mathbb Z_2\) 锥颈；与 EH 端及闭流形端帽的匹配仍是独立的几何问题。

因此，局部模型有力支持“线性方程允许指数长颈漂移”，但尚未给出闭光滑近 Einstein 度量。

---

## 6. Chern–Weil 与 ALF 标量模型

### Chern–Weil 部分

若四维固定流形满足
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op}}\to0,
\qquad \operatorname{Vol}(g_i)\to0,
\]
则
\[
8\pi^2\chi
=\int\left(|W|^2-\frac12|E|^2+\frac{R^2}{24}\right)dV
\]
确实给出
\[
\int|W|^2\to8\pi^2\chi.
\]
结合签名公式可得
\[
\int|W^\pm|^2
\to2\pi^2(2\chi\pm3\tau).
\]
若 \(\chi>0\) 且全曲率一致有界，则 \(\int|W|^2\le\|W\|_\infty^2\operatorname{Vol}\to0\)，产生矛盾。故曲率必然趋于无界。这一部分成立。

“因此局部泡必为 ALF”则尚未由此推出。曲率尺度下的单射半径比例可以产生 ALE、ALF 或更强塌缩的模型；ALF 需要额外证明圆纤维在曲率尺度上保留有限长度。Euclidean Schwarzschild 是 ALF，但并非 Gibbons–Hawking 超 Kähler模型，所以 Taub–NUT 的标量 \(V\) 方程不能代替其张量分析。

支持数据还有一处计数不一致：Step 60 JSON 取 rod 数 \(2k+2=\chi\)，而 Step 34 写作 \(\chi-2\)。因此“每 rod 一个 \(8\pi^2\) 能量单位恰好饱和总能量”的解释，需要明确两个端帽是否也各产生一个单位。Chern–Weil 总能量公式不受这一计数问题影响。

### ALF 标量通量

对 \(\mathbb R^3\) 上的球谐模式，
\[
\alpha_+=\ell,\qquad\alpha_-=-\ell-1,
\]
且
\[
r^2(f_+f_-'-f_-f_+')=-(2\ell+1).
\]
质量模式 \(\ell=0\) 为 \(1,r^{-1}\)，完全正确。

若
\[
\Delta V=S,\qquad S=t\delta r^{-q},
\]
则
\[
(r^2V')'=r^2S,
\]
所以质量通量变化的绝对值为
\[
t\delta\int_1^Rr^{2-q}\,dr.
\]
由此得到 \(q<3\) 的幂增长、\(q=3\) 的对数以及 \(q>3\) 的有界尾项；JSON 数值与这些公式一致。质量符号取决于把 \(r^2V'\) 还是 \(-r^2V'\) 定义为 \(m\)，不影响量级。

不过，JSON 仍直接采用 \(R=t^{-1/2}\) 和源 \(t\delta r^{-q}\)，而 ALF 塌缩中这两个尺度尚未从几何缩放推导出来。标量质量模也可能只是 ALF 模空间中的参数变化，而非可解性障碍。单凭此模型还不能排除 ALE 型曲率条件在某些 ALF 张量通道中重新出现。

---

## 7. 最具决定性的数学对象

对 Step 60 修正本身，核心对象是一条完整的 EH 张量通量恒等式：
\[
\Phi_k(R_i)-\Phi_k(r_0)
 =\int_{r_0}^{R_i}
   \langle \operatorname{Ric}_{\widetilde g_i}
           -\Lambda t_i\widetilde g_i,\,
           o_k\rangle
 +\mathcal N_i+\mathcal G_i+\mathcal T_i,
\]
其中分别记录非线性项、规范项和环境展开余项，并证明
\[
|\text{Ricci 项}|
 \le Ct_i\delta_i\log R_i,\qquad
\mathcal N_i+\mathcal G_i+\mathcal T_i=o(t_i).
\]
再加上内端 EH 参数正交化和外端曲率系数识别，才能把一维共振估计转化为几何必要性结果。

对长颈反例机制，关键计算是采用
\[
\eta_i^2\asymp\delta_i,\qquad
t_i\asymp\delta_i e^{-2a/\delta_i}
\]
后，写出完整双翘曲或 Kaluza–Klein 度量的全部 Ricci 分量，并验证其 \(l=2\) Wronskian 投影确实改变 \(O(1)\)。

对 ALF 方向，关键对象是 Taub–NUT 与 Euclidean Schwarzschild 上规范固定的 Lichnerowicz 算子、其 \(S^1\)-不变张量根、伴随核和端面通量。现有标量表是正确的预备计算，但不能替代该张量系统。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 51,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

The active goal is a rigorous noncollapsed structure theorem for minimizing sequences of P(g)=∫|Ric°|² on closed four-manifolds. Read the Step-50 note and the cited Bour fourth-order-flow source. Scrutinize only Theorem 50.A/Lemma W: (i) scaling of the L2 gradient and the weight rho^4; (ii) whether a smoothed curvature scale with all asserted derivative bounds exists without injectivity/noncollapse; (iii) whether multiplying the fourth-order DeTurck flow by a fixed variable weight yields a uniform own-scale existence interval on possibly collapsed metrics; (iv) whether energy descent yields the stated global weighted L2 residual and enough local residual after rescaling; (v) whether the selected metric stays in or can be returned to the scalar -4 Yamabe slice without losing residual. Identify exactly what is proved, what is plausible but unwritten, and what is false. Give a corrected theorem statement with the weakest sufficient entrance hypothesis if the construction is not yet a theorem.

## Integrated Scientific Memo

# 核验结论：Theorem 50.A / Lemma W 目前不是定理

## 总判定

Step 50 中以下部分成立：

1. \(L^2\)-梯度的缩放律与权重 \(\rho^4\) 正确；
2. 对任意固定光滑正权重 \(w\)，加权 DeTurck 方程是强抛物的，并对每个固定初值存在某个依赖于全部数据的短时间解；
3. 在解已存在的任意时间区间上，能量下降与平均值选点成立；
4. 若加权残差的权重与考察区域的尺度可比较，则它确实给出重标度后的局部 \(L^2\) 残差。

但 Lemma W 所声称的、对任意可能塌缩初值都统一的 own-scale 存在时间与平滑估计，并非 Bour 的结果，也未被 Step 50 的论证证明。更严重的是：

- 所断言的 \(\rho\) 的全阶统一协变导数估计一般不成立；
- \(C^2\)-接近初值的统一估计一般不成立；
- 输出曲率尺度的上界
  \[
  r_{g(t_*)}\le C\rho_{g_0}
  \]
  对一般粗糙初值是假的；
- Theorem 50.A(3) 中包含 \(P(g_0)-P(g(t_*))\) 的第一个不等式不由平均值论证推出；
- 回到 \(s=-4\) Yamabe 切片虽可保持近极小能量，却不能一般保持加权 Euler–Lagrange 残差。

因此，Theorem 50.B 中以 \(r_{g_i'}\) 做点选并由 Theorem 50.A(3) 推出 own-scale 局部残差的关键步骤目前存在缺口：它恰好需要上述错误的尺度上比较。

---

## 1. 缩放与 \(\rho^4\)：正确

记
\[
Q(g):=\operatorname{Grad}_{L^2}P(g),\qquad
DP_g(h)=\int_M\langle Q(g),h\rangle_g\,d\mu_g .
\]
在四维中 \(P(\lambda^2g)=P(g)\)。由
\[
DP_{\lambda^2g}(h)=DP_g(\lambda^{-2}h)
\]
及四维中
\[
\langle A,h\rangle_{\lambda^2g}\,d\mu_{\lambda^2g}
=\langle A,h\rangle_g\,d\mu_g
\]
可得
\[
\boxed{Q(\lambda^2g)=\lambda^{-2}Q(g)}
\]
作为 \((0,2)\)-张量。因此
\[
|Q(\lambda^2g)|_{\lambda^2g}^2\,d\mu_{\lambda^2g}
=\lambda^{-4}|Q(g)|_g^2\,d\mu_g.
\]
若长度尺度同时按 \(\rho\mapsto\lambda\rho\) 缩放，则
\[
\boxed{\rho^4|Q|^2\,d\mu}
\]
不变。

若以半径 \(r\) 重标度
\[
\hat g=r^{-2}g,
\]
则
\[
\int_U|Q(\hat g)|_{\hat g}^2\,d\mu_{\hat g}
=r^4\int_U|Q(g)|_g^2\,d\mu_g.
\]
故只要在 \(U\) 上 \(\rho\ge\kappa r\)，就有
\[
\int_U|Q(r^{-2}g)|^2\,d\mu_{r^{-2}g}
\le \kappa^{-4}\int_U\rho^4|Q(g)|^2\,d\mu_g.
\]
这正是从全局加权残差到重标度局部残差的正确公式。

未加权四阶梯度流的自然时间缩放是 \(t\mapsto\lambda^4t\)；乘以 \(\rho^4\) 后，每个长度尺度 \(\rho\) 获得单位局部时间。这一设计思想完全正确。

---

## 2. 曲率尺度及其平滑：低阶可行，全阶断言错误

### 2.1 \(r_g\) 的 Lipschitz 性

定义
\[
r_g(x)=\sup\left\{r:\ r^2\sup_{B_g(x,r)}|\mathrm{Rm}_g|\le1\right\}
\]
并作固定上限截断。利用
\[
B_g(y,r-d_g(x,y))\subset B_g(x,r)
\]
可得
\[
|r_g(x)-r_g(y)|\le d_g(x,y).
\]
所以 1-Lipschitz 性成立。

### 2.2 固定度量上可以平滑，但常数通常依赖高阶几何

对每个固定光滑紧致 \((M,g)\)，可构造光滑正函数 \(\rho\) 满足
\[
\tfrac12r_g\le \rho\le r_g.
\]
然而 Step 50 需要的是与度量无关的全阶估计
\[
\rho^j|\nabla^j\log\rho|_g\le C_j,
\]
且只依赖阶数。这不能从 own-scale 曲率界
\[
\rho^2|\mathrm{Rm}|\lesssim1
\]
推出。

对标量 \(f=\log\rho\)，四阶协变导数的交换包含
\[
\nabla\mathrm{Rm}*\nabla f+\mathrm{Rm}*\nabla^2f.
\]
因此，在 \(f\) 真正变化的区域，统一 \(\nabla^4f\) 控制会接触 \(\nabla\mathrm{Rm}\)。但仅有 \(|\mathrm{Rm}|\) 有界时，\(|\nabla\mathrm{Rm}|\) 可任意大：高频、小振幅的度量扰动可保持曲率振幅有界，同时令曲率导数发散。故至少从 \(j=4\) 起，上述全阶结论一般是假的。

即使取 \(\rho\equiv1\)，也只能说明权重的导数为零，不能说明 \(\rho^{-2}g=g\) 具有统一高阶有界几何。因此“由 \(\rho\) 的选择可知初始归一化度量所有阶均统一受控”这一推断错误。

### 2.3 “切空间球上的指数图”并不能自动解决塌缩

曲率有界时，可在切空间球上拉回度量，得到可能多对一的局部覆盖；这对局部估计很有用。但它不是原流形上的普通统一坐标图。要由此建立统一流存在时间，还需证明：

- 局部覆盖间的兼容性；
- 变系数四阶方程的统一局部估计；
- 从仅有曲率界的粗糙初值到正时间高阶平滑；
- 流期间曲率不立即越过可控范围。

这些均不在 Bour Theorem 1.4–1.5 中。

此外，在局部覆盖上直接卷积得到的函数未必对局部 deck/pseudogroup 作用不变，因而未必下降为 \(M\) 上的函数。平滑构造必须是内禀的，或者证明其等变性。

---

## 3. 固定权重的 DeTurck 流：固定数据短时存在成立，统一 own-scale 时间未证

考虑
\[
\partial_tg=-wQ(g)+\mathcal L_{\,wV_B(g)}g,
\qquad w>0\ \text{固定},
\]
其中 \(V_B\) 是 Bour 的三阶 DeTurck 向量场。

必须使用真正的 Lie 导数 \(\mathcal L_{wV_B}g\)，而不是仅写 \(w\mathcal L_{V_B}g\)。两者关系为
\[
\mathcal L_{wV_B}g
=w\mathcal L_{V_B}g
+2\,\mathrm{sym}(dw\otimes V_B^\flat),
\]
附加项至多三阶。因此四阶主符号是
\[
w\,\sigma\!\left(D[-Q+\mathcal L_{V_B}]\right).
\]
Bour Proposition 2.4 对 \(P=\int|\mathring{\mathrm{Ric}}|^2\) 给出 \(a=b=0\)，所以该主符号强椭圆。对固定闭流形、固定光滑正 \(w\) 及固定光滑初值，标准拟线性理论给出
\[
[0,T(g_0,w))
\]
上的唯一光滑解。

这只是数据依赖的短时存在。Bour 没有证明存在统一
\[
T(g_0,w)\ge c_0>0
\]
且 \(c_0\) 仅由曲率尺度归一化决定。

### Bour Theorem 1.5 不能补足该缺口

Bour 的 Bando–Bernstein–Shi 型估计预先假设：

1. 流已经存在于所述时间段；
2. 整个时间段上 \(\|\mathrm{Rm}\|_\infty\le D\)。

其结论是全局 \(L^2\) 曲率导数估计。将这些估计转为点态估计时，Bour 明确使用 Sobolev 常数；而在塌缩情形中，这正是缺失的量。该来源没有提供：

- 从初始曲率上界直接推出短时间曲率上界；
- 无注入半径假设的局部点态平滑定理；
- 固定变权 \(w=\rho^4\) 的统一存在时间；
- 粗糙初始数据的统一延拓准则。

所以 Step 50 中“先由 \(t\ge c_0/2\) 的平滑取得高阶控制，再据此证明解存在到 \(c_0\)”是循环论证。

### DeTurck 背景也是问题

Bour 的 DeTurck 场依赖背景联络。若直接用 \(g_0\) 作背景，其表达式包含背景的三、四阶坐标导数；一般 own-scale 曲率界并不控制这些量。因此若试图证明统一粗糙初值定理，应使用一个已平滑、own-scale 有界几何的背景，而不能未经论证地用原始 \(g_0\)。

---

## 4. Lemma W 中的 \(C^2\) 接近与双向尺度比较

### 4.1 统一 \(C^2\)-接近一般是假的

Lemma W 声称
\[
\|\rho^{-2}g_t-\rho^{-2}g_0\|_{C^2}\le Ct^\theta.
\]
高频曲率波纹可以具有统一曲率振幅但很短波长。四阶流在时间约为波长四次方时就会显著削弱其曲率。因此，对固定小 \(t>0\)，可令波长远小于 \(t^{1/4}\)，使二阶导数发生 \(O(1)\) 改变。故不能有只依赖曲率界的统一 \(C^2\) 模连续性。

合理的替代是：

- \(C^0\) 或 \(C^{1,\beta}\) 接近；
- 正时间的平滑估计；
- 以及独立证明的曲率上界。

### 4.2 下尺度比较可能成立，上尺度比较一般不成立

若有一个正确的统一平滑定理并能控制流期间曲率，则
\[
r_{g_t}\ge c\,\rho_{g_0}
\]
是合理目标：流不应在单位 own-scale 时间内凭空制造更小曲率尺度。

但
\[
\boxed{r_{g_t}\le C\,\rho_{g_0}}
\]
对任意初值是错误的。初值可包含高频但小能量的曲率波纹或薄曲率层。它们决定了很小的 \(r_{g_0}\)，却能被四阶流迅速抹平，于是输出尺度远大于输入尺度。此类扰动的 \(P\)-代价可以趋于零，所以不能因考虑极小化序列而排除。

这不是无关紧要的技术错误。Theorem 50.B 在输出度量 \(g_i'\) 的曲率尺度 \(r_{g_i'}(y_i)\) 上重标度。要由输入权重 \(\rho_{g_i}\) 控制该重标度残差，需在相应区域有
\[
\rho_{g_i}\gtrsim r_{g_i'}(y_i),
\]
即恰好需要错误的上尺度比较。

因此，当前 Theorem 50.A 的加权残差并不足以证明 Theorem 50.B 所使用的“输出度量自身尺度上的 Palais–Smale 残差”。

---

## 5. 能量下降：恒等式正确，50.A(3) 的第一不等式错误

令
\[
A(t)=\int_Mw|Q(g_t)|^2\,d\mu_{g_t}.
\]
因为 \(P\) 对微分同胚不变，对任意向量场 \(X\) 有
\[
DP_g(\mathcal L_Xg)=0.
\]
故
\[
\frac{d}{dt}P(g_t)
=DP_{g_t}\bigl(-wQ+\mathcal L_{wV_B}g_t\bigr)
=-A(t).
\]

若解存在于 \([0,T]\)，在 \([T/2,T]\) 上可选 \(t_*\) 使
\[
A(t_*)\le\frac2T\int_{T/2}^TA(t)\,dt
=\frac2T\bigl(P(g(T/2))-P(g(T))\bigr).
\]
进而
\[
\boxed{
A(t_*)\le\frac2T\bigl(P(g_0)-\alpha(M)\bigr).}
\]

但一般不能推出
\[
A(t_*)\le\frac2T\bigl(P(g_0)-P(g(t_*))\bigr).
\]
后者把选定时刻的瞬时下降率与此前平均下降率错误地比较；下降速率可在后半区间增长。应删除 50.A(3) 中这一中间不等式。

### 对极小化序列真正需要的条件

设
\[
\delta_i=P(g_i)-\alpha(M)\to0.
\]
若对应加权流至少存在到 \(T_i>0\)，且
\[
\boxed{\delta_i/T_i\to0,}
\]
则存在 \(t_i\in[T_i/2,T_i]\) 使
\[
\int_Mw_i|Q(g_i(t_i))|^2\,d\mu_{g_i(t_i)}
\le\frac{2\delta_i}{T_i}\to0.
\]
所以逻辑上不需要统一 \(T_i\ge T_0\)；最弱的时间条件是能量缺口比可用流时间更快趋零。

### 局部残差的精确地位

若以 \(r_i\) 重标度，并且在目标区域上 \(w_i=\rho_i^4\ge\kappa^4r_i^4\)，则
\[
\int_{\widehat U_i}|Q(r_i^{-2}g_i(t_i))|^2
\le\kappa^{-4}\int_M\rho_i^4|Q(g_i(t_i))|^2\to0.
\]
这是局部 \(L^2\) 残差，不是点态残差。要得到光滑临界极限，还需局部紧性和椭圆正则性。

此外，Step 50.B 中写出的常数 \(16\) 忽略了尺度可比常数；若 \(\rho\ge (2C)^{-1}r\)，相应因子应为 \(16C^4\)。

---

## 6. Yamabe 切片：能量可恢复，残差不能自动恢复

### 6.1 加权流不保持 \(s=-4\)

\(P\) 的梯度迹满足
\[
\operatorname{tr}_gQ(g)=\tfrac12\Delta_gs_g
\]
（拉普拉斯号约定可能改变符号）。即使初始 \(s\equiv-4\)，沿
\[
h=-wQ+\mathcal L_{wV}g
\]
的标量曲率变分
\[
Ds_g(h)=\delta\widetilde\delta h+\Delta\operatorname{tr}h
-\langle\mathrm{Ric},h\rangle
\]
一般并非常数。因此流会立即离开常标量曲率切片。

加权流也不保持体积，因为
\[
\frac d{dt}\operatorname{Vol}(g_t)
=-\frac14\int_Mw\,\Delta s\,d\mu
\]
一般不为零；这可用常数缩放修正，且不影响 \(P\)。

### 6.2 回到非正 Yamabe 代表不会增加 \(P\)

四维 Gauss–Bonnet 给出
\[
P(g)=2\int_M|W_g|^2\,d\mu_g
+\frac1{12}\int_Ms_g^2\,d\mu_g
-16\pi^2\chi(M).
\]
第一项为共形不变量。在 Yamabe 常数非正的共形类中，Yamabe 代表最小化该共形类内的 \(\int s^2\)。故若 \(\hat g\) 是 \(g\) 的 Yamabe 代表，
\[
P(\hat g)\le P(g).
\]
若其常标量曲率为负，再作常数缩放可规范为 \(s_{\hat g}=-4\)，且 \(P\) 不变。

因此，在所有相关共形类均为负 Yamabe 型的情形，返回 \(s=-4\) 切片可以保持“极小化序列”性质。

### 6.3 但 Euler–Lagrange 残差一般不保留

若
\[
\hat g=u^2g,
\]
则 \(Q\) 不是共形协变张量；其变换含有 \(u\) 的最高四阶导数以及曲率耦合项。因此
\[
\int\rho^4|Q(g)|^2\to0
\]
不能推出
\[
\int\hat\rho^4|Q(\hat g)|^2\to0.
\]
同时还需证明 \(\hat\rho\) 与 \(\rho\) 可比。Step 50 未给出任何这样的定量 Yamabe 投影估计。

只有在极限已经满足 \(Q(g_\infty)=0\) 时，闭流形上的迹方程给出 \(s_{g_\infty}\) 为常数；若该常数为负，再作常数缩放至 \(s=-4\)，残差仍严格为零。这是极限后的规范化，不是近似序列上的残差传递。

---

## 7. 当前真正已证的修正版

### 定理 50.A\(_0\)：固定数据版本

设 \(M^4\) 闭，\(g_0\) 为光滑度量，\(w>0\) 为固定光滑函数，\(\bar g\) 为光滑 DeTurck 背景。则
\[
\partial_tg=-wQ(g)+\mathcal L_{\,wV_{\bar g}(g)}g,\qquad g(0)=g_0
\]
在某个依赖于 \((g_0,w,\bar g)\) 的区间 \([0,T)\) 上有唯一光滑解。

对任意 \(0<S<T\)，存在 \(t_*\in[S/2,S]\)，使
\[
P(g(t_*))\le P(g_0)
\]
且
\[
\int_Mw|Q(g(t_*))|^2\,d\mu_{g(t_*)}
\le
\frac2S\bigl(P(g(S/2))-P(g(S))\bigr)
\le
\frac2S\bigl(P(g_0)-\alpha(M)\bigr).
\]
这里所有存在时间、度量可比和曲率控制常数均允许依赖固定数据。该版本由 Bour 的强抛物性加标准固定数据短时理论及能量恒等式支持。

### 定理 50.A\(_{\rm seq}\)：极小化序列的最弱抽象入口

设
\[
P(g_i)-\alpha(M)=\delta_i\to0,
\]
给定正光滑权重 \(w_i\)，且相应加权 DeTurck 流存在于 \([0,T_i]\)。若
\[
\delta_i/T_i\to0,
\]
则存在 \(t_i\in[T_i/2,T_i]\)，满足
\[
P(g_i(t_i))\le P(g_i),
\qquad
\int_Mw_i|Q(g_i(t_i))|^2\,d\mu_{g_i(t_i)}
\le\frac{2\delta_i}{T_i}\to0.
\]
若另有某些尺度 \(r_i\) 满足目标区域上
\[
w_i\ge c\,r_i^4,
\]
则对应 \(r_i\)-重标度区域上的局部 \(L^2\) 残差趋零。

这一定理不声称 \(r_i\) 必为输出度量的曲率尺度；要用于 Theorem 50.B，必须额外建立这一可比较性。

---

## 8. 若坚持单步构造，足够且接近最弱的入口假设

要恢复 Step 50 所需的双向尺度比较，可加入初始曲率的 own-scale 模连续性。一个直接可用的假设是：

\[
(H_{\beta,\Lambda})\qquad
\text{在每个 }x\text{ 的半径 }r_{g_0}(x)\text{ 的局部提升球上，重标度后 }
[\mathrm{Rm}_{g_0}]_{C^\beta}\le\Lambda,
\]
其中 \(0<\beta<1\)。

这一假设排除决定 \(r_{g_0}\) 却会被瞬时抹去的任意高频波纹。它也是经典四阶 Schauder 理论可直接处理的最弱自然形式之一。

在该假设下，可将目标修正为：

### 条件版 Theorem 50.A\(_H\)

假设 \(g_0\) 满足 \((H_{\beta,\Lambda})\)，并可构造与 \(r_{g_0}\) 可比的权重 \(\rho\) 及一个 own-scale 有界几何的光滑背景 \(\bar g\)。若进一步证明下述 Lemma W′，则存在度量 \(g\) 满足
\[
P(g)\le P(g_0),
\]
\[
C^{-1}g_0\le g\le Cg_0,
\qquad
C^{-1}r_{g_0}\le r_g\le Cr_{g_0},
\]
以及
\[
\int_Mr_g^4|Q(g)|^2\,d\mu_g
\le C\bigl(P(g_0)-\alpha(M)\bigr).
\]
常数依赖于 \((\beta,\Lambda)\)，不依赖注入半径。

### 尚需证明的 Lemma W′

在 \((H_{\beta,\Lambda})\) 下，固定权重 \(\rho^4\)、平滑背景 \(\bar g\) 的加权 DeTurck 系统存在于统一区间
\[
[0,t_0(\beta,\Lambda)]
\]
并在局部提升球上满足例如
\[
|\mathrm{Rm}(t)-\mathrm{Rm}(0)|
\le Ct^{\beta/4},
\qquad
|\nabla^k\mathrm{Rm}(t)|
\le C_kt^{-k/4}.
\]
第一式保留初始曲率峰，从而给出 \(r_{g_t}\lesssim r_{g_0}\)；曲率上界给出反向比较。这里不应再要求统一 \(C^2\)-接近初值。

该 Lemma W′仍未由 Bour 证明，但其入口假设已足以消除原 Lemma W 的高频反例。

---

## 9. 对非塌缩结构定理最合适的直接入口

Theorem 50.B 真正需要的不是输入、输出尺度比较，而是对同一个输出度量 \(h_i\) 的 own-scale Palais–Smale 条件：
\[
\boxed{
\varepsilon_i:=
\int_M r_{h_i}^4|Q(h_i)|^2\,d\mu_{h_i}\to0,
}
\]
再加：

- 体积归一化；
- 统一非塌缩
  \[
  \operatorname{vol}_{h_i}B(x,r)\ge\nu_0r^4;
  \]
- 统一 \(\int|\mathrm{Rm}|^2\) 界。

在此假设下，点选于 \(r_{h_i}\) 后，重标度局部 \(L^2\) 残差直接趋零，不再需要错误的 \(r_{h_i}\lesssim\rho_{g_i}\)。

不过从该残差得到光滑临界极限仍需写出一个近临界椭圆正则性步骤。非塌缩和曲率界给出 harmonic coordinates；在适当 gauge 下，\(Q(g)=f\in L^2\) 是四阶椭圆系统，预期可从 \(W^{2,p}\) 启动得到 \(W^{4,2}_{\rm loc}\)，继而强紧性并令极限满足 \(Q(g_\infty)=0\)。这一方案合理，但 Step 50 尚未给出完整证明。

因此，严谨的非塌缩结构定理目前应写成：

> **条件性结构定理。** 若一个非塌缩的 \(P\)-极小化序列可替换为满足
> \[
> \int r_{g_i}^4|Q(g_i)|^2\to0
> \]
> 的同尺度序列，并且上述 harmonic-gauge 四阶椭圆正则性成立，则 Anderson 型点选和气泡分析产生 \(P\)-临界的 orbifold 主体与临界 ALE 气泡。

这准确隔离了两个尚未闭合的对象：

1. 任意极小化序列的**输出-own-scale Palais–Smale 选择定理**；
2. 从 own-scale \(L^2\) 残差到临界极限的**局部四阶椭圆紧性定理**。

---

## 最终状态表

| 断言 | 判定 |
|---|---|
| \(Q(\lambda^2g)=\lambda^{-2}Q(g)\) | 已证 |
| \(\rho^4|Q|^2d\mu\) 尺度不变 | 已证 |
| \(r_g\) 为 1-Lipschitz | 已证 |
| 固定光滑权重下强抛物性 | 已证 |
| 固定数据的某个短时间存在 | 已证 |
| 任意塌缩初值上的统一 own-scale 时间 | 未证；Bour 不提供 |
| \(\rho\) 相对 \(g_0\) 的全阶统一导数界 | 一般错误 |
| 统一 \(C^2\)-接近初值 | 一般错误 |
| \(r_{g(t_*)}\gtrsim\rho_{g_0}\) | 在修正平滑定理下合理，未证 |
| \(r_{g(t_*)}\lesssim\rho_{g_0}\) | 对一般初值错误 |
| 能量下降恒等式 | 已证 |
| 50.A(3) 中以 \(P(g_0)-P(g(t_*))\) 为右端 | 错误 |
| 加权全局残差推出可比较尺度上的局部 \(L^2\) 残差 | 已证 |
| 当前残差足以支撑 50.B 的输出-own-scale blow-up | 未证 |
| 流保持 \(s=-4\) | 错误 |
| Yamabe 投影不增加 \(P\)（非正 Yamabe 类） | 已证 |
| Yamabe 投影保持加权梯度残差 | 一般错误 |

核心修正是：不得把 Lemma W 称为 Bour 理论的“例行适配”；当前可无条件使用的是固定数据版本与抽象序列版本。完整的非塌缩结构定理需要直接假设输出度量自身尺度上的 Palais–Smale 残差，或先证明带 own-scale 曲率模连续性入口的 Lemma W′。
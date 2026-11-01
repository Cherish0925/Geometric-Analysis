# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 42,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step42_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step42_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Critically verify and repair the connected first-exit and terminal-chart proof for the near-critical Ishida–LeBrun negative four-dimensional route. Focus on three exact interfaces raised by the strategist. (1) A01's first-exit equation (4.13) contains an additive C0*T term that may dominate a shrinking support energy. Determine from the index-level curvature identity whether the correct q=2 inequality is homogeneous relative to K2=∫η²(1+|Rm|²), or whether a nonhomogeneous term remains; give a precise relative self-improvement estimate valid componentwise under collapse. (2) Determine whether the support construction needs a sequence-uniform Hessian bound for χ. Use the signed Hessian-a integration mechanism and distinguish zero-order smoothing estimates from per-datum continuation. (3) Repair the terminal chart passage: give a precise buffered-center construction and a rigorous route from positive-time plateau estimates to strong curvature convergence on exponential pullback charts. Check whether standard interior normalized Ricci-flow derivative estimates apply when χ=1 on a larger plateau, and state required radius/time margins. Also identify any remaining load-bearing issue in passing the explicit spectral density G to the limit. Do not accept either note's theorem status; reason from the equations and files.

## Integrated Scientific Memo

# 核验与修复结论

## 1. \(q=2\) 曲率能量是齐次的；A01 (4.13) 中 \(C_0T\) 应删除

令
\[
F^2=1+|\Rm|^2,\qquad
K_2^\eta=\int \eta^2F^2\,d\mu,\qquad
D_2^\eta=\int\eta^2a|\nabla\Rm|^2\,d\mu,\qquad
Y=\int\eta^2aF^3\,d\mu,
\]
其中 \(a=\chi^2\)，且 \(\eta=1\) 于 \(\supp a\) 邻域、\(a=da=0\) 于 \(\supp d\eta\)。

A01 Step 35 的指标恒等式给出
\[
\partial_t|\Rm|^2
=a\Delta|\Rm|^2-2a|\nabla\Rm|^2
+da*\Rm*\nabla E
+(\nabla^2a)_{pq}B_{\rm curv}^{pq}
+O(aF^3),
\]
其中
\[
B_{\rm curv}^{pq}=R^p{}_j{}^q{}_lE^{jl},\qquad
|B_{\rm curv}|\le CF^2,\qquad
|\nabla B_{\rm curv}|\le CF|\nabla\Rm|.
\]

对 Hessian 项保留符号并积分一次：
\[
\int\eta^2\nabla_p\nabla_qa\,B^{pq}
=-\int\nabla_qa\,\nabla_p(\eta^2B^{pq}).
\]
由于平稳 collar，\(d\eta\) 项消失；再用
\[
\frac{|da|^2}{a}=4|d\chi|^2\le Cr^{-2},
\]
得到
\[
\left|\int\eta^2(\nabla^2a):B_{\rm curv}\right|
\le \varepsilon D_2^\eta+C_\varepsilon r^{-2}K_2^\eta.
\]
其余一阶 cutoff 项相同处理。

体积元满足
\[
\partial_td\mu=-a\,\tr E\,d\mu.
\]
由于 \(|\tr E|\le CF\)，
\[
\left|\int\eta^2F^2\partial_td\mu\right|
\le C\int\eta^2aF^3 + C K_2^\eta.
\]
特别地，\(F^2\) 中常数 \(1\) 引起的项只满足
\[
\int\eta^2a|\tr E|
\le C\int\eta^2aF
\le CK_2^\eta,
\]
并不产生与局部体积、\(K_2^\eta\) 无关的常数源。归一化和逆度量变化同样由 \(CaF^3\) 控制。因此正确估计为
\[
\boxed{
(K_2^\eta)'+cD_2^\eta
\le CY+C(1+r^{-2})K_2^\eta .}
\tag{1}
\]

再由匹配支撑上的 Sobolev 插值
\[
Y=\int(\eta F)(\chi F)^2
\le (K_2^\eta)^{1/2}\|\chi F\|_4^2
\le C\gamma\bigl(D_2^\eta+r^{-2}K_2^\eta\bigr),
\qquad
\gamma=\mathcal S(K_2^\eta)^{1/2},
\]
若 \(C\gamma\le c/2\)，则
\[
\boxed{
(K_2^\eta)'+\frac c2D_2^\eta
\le C(1+r^{-2})K_2^\eta .}
\tag{2}
\]

所以 A01 (4.4)、(4.13) 中独立的 \(C_0\)、\(C_0T_*\) 是把 \(F^2\) 的常数部分误估为绝对体积源造成的，应删除。

### 坍缩下逐分量的相对自改进

对每一支撑分量 \(\alpha\)，在 \(t\le \theta r^2\) 上，
\[
\boxed{
\frac{K_{2,\alpha}^\eta(t)}
     {K_{2,\alpha}^\eta(0)}
\le
\exp\!\bigl(C\theta(1+r^2)\bigr)
\le
\exp\!\bigl(C\theta(1+r_0^2)\bigr).}
\tag{3}
\]
若沿用未先吸收 \(Y\) 的写法及 \(B(t)=\int_0^t\mathcal S^2Y\le C\gamma_*^3\)，则同样有
\[
K_{2,\alpha}^\eta(t)
\le e^{C\theta(1+r_0^2)+C\gamma_*^3}
K_{2,\alpha}^\eta(0).
\tag{4}
\]
选取
\[
C\theta(1+r_0^2)+C\gamma_*^3<\log(3/2)
\]
即可得到严格的
\[
K_{2,\alpha}^\eta(t)<\frac32K_{2,\alpha}^\eta(0)<2K_{2,\alpha}^\eta(0).
\]
这是比值估计，即使局部体积以及 \(K_{2,\alpha}^\eta(0)\to0\) 也不退化。

还有一个上游修正：最大函数的好点条件必须控制整个 \(\eta_\alpha\)-支撑尺度，而不只是 \(B_r(x_\alpha)\)。应取最大函数截断半径 \(R\ge7r\)，从而
\[
K_{2,\alpha}^\eta(0)
\le C(1+\Lambda\overline K_0)\Vol B_{7r}(x_\alpha),
\]
并与
\[
\mathcal S_\alpha(0)
\le Cr^2\Vol(B_{7r}(x_\alpha))^{-1/2}
\]
结合，得到坍缩一致的
\[
\gamma_\alpha(0)
\le Cr^2(1+\Lambda\overline K_0)^{1/2}.
\]

---

## 2. 支撑构造不需要序列一致的 \(\nabla^2\chi\) 界

仅有 Ricci 下界和 doubling 并不能推出
\[
\|\nabla^2\chi_\alpha\|_\infty\le Cr^{-2}
\]
的序列一致估计；A01 Lemma 3.1(a) 的这一断言没有由其假设支持，应删除或明确标成逐 datum 常数。

序列一致的零阶平滑链只需
\[
|d\chi_\alpha|\le C/r
\]
以及平稳 collar。原因是曲率与缺陷的 Hessian-\(a\) 项都有特殊符号结构：

\[
B_{\rm curv}=\Rm*E,\qquad
|B_{\rm curv}|\le CF^2,\quad
|\nabla B_{\rm curv}|\le CF|\nabla\Rm|,
\]
以及
\[
B_{\rm def}^{pq}
=|E|^2g^{pq}+(\tr E)E^{pq}-2(E^2)^{pq},
\]
\[
|B_{\rm def}|\le C|E|^2,\qquad
|\nabla B_{\rm def}|\le C|E||\nabla E|.
\]
积分一次后，所有代价均由
\[
|da|^2/a=4|d\chi|^2
\]
承担。因此 \(K_2\)、一般 \(p\) 曲率能量、\(J_6\)、一般 \(p\) 缺陷能量以及 Moser 端点都不需要一致 Hessian 界。

必须区分：

* **序列一致的零阶平滑估计：**只用 \(|d\chi|\le C/r\)；
* **逐 datum 延拓：**交错归纳涉及任意高阶 \(\nabla^m\chi\)，但只要求它们对该固定光滑 datum 有限；
* **序列一致的终端高阶正则性：**应从 \(\chi=1\) 内部的标准 Ricci 流估计获得，而不能使用逐 datum 的 cutoff-jet 常数。

可采用光滑 Lipschitz 近似构造
\[
\chi_\alpha=1\ \text{于 }B_{4r}(x_\alpha),\qquad
\supp\chi_\alpha\subset B_{5r}(x_\alpha),\qquad
|d\chi_\alpha|\le C/r,
\]
\[
\eta_\alpha=1\ \text{于 }B_{6r}(x_\alpha),\qquad
\supp\eta_\alpha\subset B_{7r}(x_\alpha).
\]
高阶导数允许依赖 \(i,\alpha\)。

---

## 3. 终端图表必须加入空间和时间缓冲

### 3.1 中心集及空间裕量

令
\[
P_\alpha=B_{g_0}(x_\alpha,r).
\]
由 Bishop–Gromov 比较以及原有 \(B_{2r}\) 总体积下界，
\[
\sum_\alpha\Vol_{g_0}(P_\alpha)\ge \alpha_1A_i
\]
其中 \(\alpha_1>0\) 一致。若首出区间内
\[
e^{-\Lambda}g_0\le g(t)\le e^\Lambda g_0,
\]
则在四维
\[
\Vol_{g(T)}\Bigl(\bigcup_\alpha P_\alpha\Bigr)
\ge e^{-2\Lambda}\alpha_1A_i.
\tag{5}
\]

对 \(p\in P_\alpha\)，取
\[
R=\frac12e^{-\Lambda/2}r.
\]
若 \(q\in B_{g(t)}(p,2R)\)，则
\[
d_{g_0}(p,q)\le e^{\Lambda/2}2R=r,
\qquad
d_{g_0}(x_\alpha,q)<2r.
\]
因而对所有 \(t\in[0,T]\)，
\[
B_{g(t)}(p,2R)
\subset B_{g_0}(x_\alpha,2r)
\subset\{\chi_\alpha=1\}.
\tag{6}
\]
这给出了此前以整个 \(B_{2r}\) 为中心集时缺失的空间裕量。采用更大的 \(B_{4r}\) plateau 只会增加裕量。

### 3.2 正时间柱上的标准局部 Ricci 流估计

在 (6) 的时空柱内，方程严格成为
\[
\partial_tg=-2(\Ric+g).
\tag{7}
\]
Moser 估计给出，在 \(t\in[T/2,T]\) 上
\[
|\Rm|(t)\le K_*,
\qquad
K_*=C\left(1+\frac{\gamma_*}{T}\right),
\qquad T=\theta r^2,
\tag{8}
\]
且 \(K_*\) 序列一致。

通过缩放和重参数化
\[
\bar g(t)=e^{2(t-T/2)}g(t),\qquad
\frac{ds}{dt}=e^{2(t-T/2)},
\]
方程 (7) 化为普通 Ricci 流
\[
\partial_s\bar g=-2\Ric_{\bar g}.
\]
因此标准局部 Shi 型内部估计确实适用；不需要有限传播性，也不受 plateau 外过渡区影响。由较大柱
\[
B_{g(t)}(p,2R)\times[T/2,T]
\]
缩至终端 \(B_{g(T)}(p,R)\)，可得
\[
\boxed{
\sup_{B_{g(T)}(p,R)}
|\nabla^m\Rm|(T)
\le
C_mK_*
\bigl(1+K_*+R^{-2}+T^{-1}\bigr)^{m/2}.}
\tag{9}
\]
固定 \(r,\theta,\Lambda,\gamma_*\) 后，这些常数与序列无关。核心必要条件是：

1. 较大空间球始终处于 \(\chi=1\) 区域；
2. 有正时间裕量，例如 \([T/2,T]\)；
3. 在该较大柱上有一致的 \(|\Rm|\) 界；
4. 估计只在较小终端球上使用。

### 3.3 指数拉回图上的强收敛

取
\[
0<\rho<
\min\left\{\frac R8,\frac{\pi}{4\sqrt{K_*}}\right\}.
\tag{10}
\]
则从任何 \(p\in P_\alpha\) 发出的长度 \(2\rho\) 终端径向测地线均停留在导数受控区，且没有径向共轭点。

指数平均引理应用于拉回 Riemannian 测度，而非无权 Euclidean 测度。由
\[
\int\mathfrak D_i=o(A_i)
\]
和 (5)，可选 \(p_i\in\bigcup_\alpha P_\alpha\)，使
\[
\fint_{B_\rho(0),h_i}
\mathfrak D_i(\exp_{p_i}v)\,d\mu_{h_i}(v)\longrightarrow0,
\qquad
h_i=(\exp_{p_i}^{g_i(T)})^*g_i(T).
\tag{11}
\]

Rauch 给出 \(h_i\) 在固定切空间球上的一致非退化性；(9) 给出所有曲率协变导数的一致界。Jacobi 方程或正规坐标展开随后给出度量系数的全阶局部界。经选择定向正交标架并缩小半径后，
\[
\boxed{
h_i\longrightarrow h_\infty
\quad\text{于 }B_\rho(0)\text{ 上 }C^\infty_{\rm loc}\text{ 收敛}.}
\tag{12}
\]
基底上的指数映射可以多重覆盖；这不妨碍切空间域上的拉回度量。A01 §7.2 仅凭 \(C^{1,\alpha}\) 和弱 \(W^{2,p}\) 声称曲率本征值连续是不成立的；曲率依赖二阶导数，必须用上述强曲率收敛，或另行完成严格的强 \(W^{2,p}\) 升级。

---

## 4. 显式谱密度 \(G\) 的极限

定义
\[
f=\frac23s-2\sqrt{\frac23}|W^+|,
\qquad
b=\frac23s+2w,
\qquad
G=f^2-(b_-)^2,
\]
其中 \(w\) 是 \(W^+\) 的最小本征值。

对三维迹零对称算子，
\[
w\ge-\sqrt{\frac23}|W^+|.
\]
故 \(b\ge f\)。当 \(b<0\) 时，\(b_-= -b\)，且 \(f\le b<0\)，所以
\[
|f|\ge |b|=b_-;
\]
当 \(b\ge0\) 时显然 \(b_-=0\)。因此
\[
\boxed{G\ge0.}
\tag{13}
\]

最小本征值对对称算子按算子范数 Lipschitz 连续，\(x\mapsto x_-\) 亦 Lipschitz。因此 (12) 蕴含
\[
G_i\to G_\infty
\]
在紧子球上一致；本征值重数增加不造成问题。由 (11) 和非负性，
\[
G_\infty\equiv0.
\]

其余密度分量给出
\[
E_\infty=0,\qquad s_\infty=-4,\qquad
|W_\infty^+|=\frac1{2\sqrt6}.
\]
于是
\[
f_\infty=-3.
\]
由 \(G_\infty=0\) 得 \((b_\infty)_-=3\)，结合 \(b_\infty\ge f_\infty=-3\)，只能有
\[
b_\infty=-3,\qquad w_\infty=-\frac16.
\]
迹零以及 \(|W^+|^2=1/24\) 随即推出另外两个本征值相等：
\[
\spec(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

### 仍然承重的输入

这里的点态非负性及极限连续性已经验证；但
\[
\int G_i\le48\pi^2D_{a_i}
\]
的完整 Seiberg–Witten／平方完成推导没有在给定文件中重现，仍是导入的实质性引理。

此外，终端重校准的纯 \(Q(T)\) 界隐含使用
\[
q_i=k_i-\frac{A_i}{3}\ge0.
\]
若仅假设 \(k_i/A_i\to1/3\)，则正确形式为
\[
\boxed{
\int\mathfrak D_i
\le119Q_i(T)+912\pi^2(-q_i)_+.}
\tag{14}
\]
由于 \((-q_i)_+/A_i\to0\)，仍足以推出
\[
A_i^{-1}\int\mathfrak D_i\to0.
\]
只有附加 \(q_i\ge0\) 时，才能写成单纯的 \(119Q_i(T)\)。

---

## 最终核验状态

三个指定接口均可如下修复：

1. **首出能量：**删除 \(C_0T\)；使用逐分量乘法型估计 (3) 或 (4)，从而在坍缩下仍严格自改进。
2. **cutoff Hessian：**删除序列一致的 \(\nabla^2\chi\) 要求；零阶平滑只用一致的梯度界，任意高阶 cutoff jets 仅用于逐 datum 延拓。
3. **终端图表：**将中心缩入内 plateau，保留半径 \(2R\to R\) 和时间 \(T/2\to T\) 的双重裕量；在 \(\chi=1\) 区域把归一化流化为普通 Ricci 流，应用局部 Shi 估计，再在指数拉回图上获得 \(C^\infty\) 曲率收敛。

这些修复尚不证明整条定理，因为给定材料仍未内部证明：

* transported-coefficient 退化 DeTurck 的启动／重启；
* Step 40 全阶交错归纳的完整非示意化版本；
* \(\int G\le48\pi^2D_a\) 的全部谱－SW 缺陷代数。

但 \(q=2\) 的非齐次疑点、cutoff Hessian 的序列一致性疑点，以及终端图表的正则性缺口本身都已被明确解决。
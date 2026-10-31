# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md",
    "Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260927_covering_geometry_and_sharp_subfamilies.md",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py"
  ]
}
```

## Task

Independently verify the geometric and global deduction from the frozen C² cell to a smooth exact-CH-collar blow-up cell and then to a balanced sequence with coefficient below four. Check bolt smoothness with dσ_i=2σ_j∧σ_k and ∫σ123=2π², topology/orientation of collapsing σ1 versus the aligned blow-up, the O(δ³) exact-collar smoothing, constant rescaling Ric=-6g to Ric=-g, I54 transfer arithmetic, and residual-finite fixed-ball supply. Also analyze the consequence of the inherited exact handle-only formula α=4h/(1+h): prove or refute that every pure-handle exact-CH cell must have J≥32π²ℓ, and formulate the distinct mixed-cell interaction question without conflating it with isolated handle improvement.

## Output

# 科学核验备忘录

## 1. Bolt 光滑性与归一化

令 \(y=x-x_0\)。在 \(u=0\) 附近，
\[
u=\frac{1}{\ell}\log\!\left(1+\frac y{x_0}\right)
=\frac{y}{x_0\ell}+O(y^2),\qquad S(u)=O(y^3).
\]
设
\[
f_1=e^{q_F(0)},\qquad g_1=e^{q_G(0)}.
\]
系数修正给出
\[
q_F(0)+q_G(0)=0,
\]
故 \(f_1g_1=1\)。冻结剖面的展开为
\[
F=f_1y+O(y^2),\qquad G=g_1y+O(y^2),\qquad w=O(y^2).
\]

取径向测地坐标
\[
dt=\frac{dx}{2\sqrt G}.
\]
由 \(G=g_1y+O(y^2)\) 得
\[
t=\sqrt{\frac y{g_1}}+O(y^{3/2}),\qquad
y=g_1t^2+O(t^4).
\]
于是三个轨道方向的平方长度满足
\[
\begin{aligned}
h_1=F&=t^2+O(t^4),\\
h_2=x&=x_0+g_1t^2+O(t^4),\\
h_3=xe^w&=x_0+g_1t^2+O(t^4),
\end{aligned}
\qquad h_2-h_3=O(t^4).
\]
而且 \(h_1/t^2\)、\(h_2\)、\(h_3\) 都是 \(t^2\) 的解析函数。

给定
\[
d\sigma_i=2\sigma_j\wedge\sigma_k,\qquad
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2,
\]
\(\sum\sigma_i^2\) 是单位圆三球度量，\(\sigma_1\)-对偶圆轨道的周期是 \(2\pi\)。因此 \(h_1=t^2+O(t^4)\) 正好是无锥角的极坐标条件，而不是其他文献中采用周期 \(4\pi\) 时出现的 \(t^2/4\)。

在奇异轨道处，\(\operatorname{span}\{\sigma_2,\sigma_3\}\) 在该圆作用下以权二旋转；它的无迹对称二次张量以权四旋转。因此 \(h_2-h_3\) 必须从 \(t^4\) 开始。冻结剖面的 \(w=O(y^2)=O(t^4)\) 正好满足这一条件。由此 bolt 处是解析光滑的二维球，而不是轨道商奇点。

体积形式也与计算采用的常数一致：
\[
dV_g=\frac{x e^{w/2}}{2}\sqrt{\frac FG}\,
dx\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3,
\]
所以轨道积分后
\[
dV_g=\pi^2x e^{w/2}\sqrt{\frac FG}\,dx.
\]
这验证了数值积分中 \(8\pi^2\) 的归一化没有遗漏 \(2\) 或有限群阶数。

## 2. 折叠 \(\sigma_1\) 的拓扑与定向

CH collar 的 Kähler 形式可写为
\[
\omega_{\rm CH}=\frac12\,dx\wedge\sigma_3+x\,\sigma_1\wedge\sigma_2,
\]
故其复定向是
\[
dx\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3>0.
\]

循环置换
\[
(\sigma_1,\sigma_2,\sigma_3)\longmapsto
(\sigma_2,\sigma_3,\sigma_1)
\]
保持 Maurer–Cartan 方程和三形式 \(\sigma_{123}\)。它由 \(SU(2)\) 的适当平移诱导，属于 \(SO(3)\)，因而保持定向并与恒等映射同伦。取该旋转在 bolt 邻域恒定，再沿自由轨道区逐渐退回恒等映射，可得到在外侧 collar 上逐点为恒等的微分同胚。

因此，折叠 \(\sigma_1\) 的填充与通常折叠 \(\sigma_3\) 的 aligned 填充定向微分同胚。后者是 Hopf 圆丛对应的负一自交圆盘丛，即截断的 \(\mathcal O(-1)\)。等价地，在上述复定向下，单位 Hopf 圆丛是 tautological line bundle 的单位圆丛，其第一 Chern 数为 \(-1\)。所以该 cell 的拓扑确为
\[
D\#\overline{\mathbb{CP}}^{\,2}.
\]
轴的改变没有把 \(\overline{\mathbb{CP}}^{\,2}\) 换成 \(\mathbb{CP}^2\)，也没有产生 \(-2\) 球或透镜空间轨道。

## 3. 从 \(C^2\) 拼接到光滑 exact-CH collar

令 \(r=X-x\)。由于
\[
1-S=(1-u)^3(1+3u+6u^2),\qquad
q_F,q_G=O((1-u)^3),
\]
三个偏差
\[
d_F=F-x,\qquad d_G=G-(x+x^2),\qquad
d_w=w-\log(1+x)
\]
都满足
\[
d^{(k)}=O(r^{3-k}),\qquad k=0,1,2.
\]
因此直接接上 CH 剖面得到 \(C^2\) 度量，且二阶 jet 在 \(x=X\) 与 CH 完全相同。

对
\[
\chi_\delta(x)=\chi\!\left(\frac{X-x}{\delta}\right)
\]
及任一上述偏差 \(d\)，乘积法则给出
\[
\left|\partial_x^k(\chi_\delta d)\right|
\le C\delta^{3-k},\qquad k=0,1,2.
\]
由此在
\[
B_\delta=[X-\delta,X]
\]
上，
\[
\|g_\delta-g_{\rm CH}\|_{C^2}
+\|g-g_{\rm CH}\|_{C^2}\le C\delta.
\]
该区域远离 bolt，CH 度量一致正定；故 \(\delta\) 充分小时 \(g_\delta\) 仍正定。Ricci 张量是度量二阶 jet 的光滑函数，所以
\[
|\operatorname{Ric}(g_\delta)+6g_\delta|
+|\operatorname{Ric}(g)+6g|
\le C\delta
\quad\text{on }B_\delta.
\]
同时 \(\operatorname{Vol}(B_\delta)\le C\delta\)。两度量在 \(B_\delta\) 外的非零缺陷部分一致，于是
\[
|J_6(g_\delta)-J_6(g)|\le C\delta^3.
\]
截断函数在常值区的所有导数均消失，故 \(g_\delta\) 全局光滑，并在 \(x\ge X-\delta/2\) 精确等于 CH。bolt 区完全未改动。

从文中显示的 \(X=8\) enclosure 可直接取
\[
\frac{J_6(g)}{8\pi^2}\le0.999116243147,
\qquad
\eta_8^*=8.83756853\times10^{-4}.
\]
因此可选固定 \(\delta>0\) 使
\[
J_6(g_\delta)\le8\pi^2(1-\eta_8^*/2).
\]
若只要求逼近原冻结值，则对任意 \(\rho>0\) 可选固定 \(\delta(\rho)\) 使
\[
\frac{J_6(g_{\delta(\rho)})}{8\pi^2}
\le1-\eta_8^*+\rho.
\]
摘录中写出的 \(\eta=8.8375686\times10^{-4}\) 比显示 enclosure 直接支持的末位略大；采用上面的 \(\eta_8^*\) 即可完全避开舍入问题，不改变几何结论。类似地，\(X=16\) 的显示 enclosure 给出
\[
\eta_{16}^*=1-(0.99890294372+2.4\times10^{-12})
=1.0970562776\times10^{-3}.
\]

## 4. 从 \(\operatorname{Ric}=-6g\) 到 \(\operatorname{Ric}=-g\)

令
\[
\widetilde g=6g.
\]
常数倍缩放不改变协变 Ricci 张量：
\[
\operatorname{Ric}_{\widetilde g}=\operatorname{Ric}_g.
\]
因此在 CH 区
\[
\operatorname{Ric}_{\widetilde g}
=-6g=-\widetilde g.
\]
而且
\[
\operatorname{Ric}_{\widetilde g}+\widetilde g
=\operatorname{Ric}_g+6g.
\]
四维中，协变二张量范数平方在 \(g\mapsto6g\) 下乘以 \(6^{-2}\)，体积乘以 \(6^2\)，故
\[
\int|\operatorname{Ric}_{\widetilde g}+\widetilde g|_{\widetilde g}^2
\,dV_{\widetilde g}
=
\int|\operatorname{Ric}_g+6g|_g^2\,dV_g.
\]
所以冻结积分就是 I54 归一化中的 cell cost \(J_1\)，没有额外的 \(6\) 次幂因子。

径向距离相应乘以 \(\sqrt6\)。由于
\[
\int_0^X\frac{dx}{2\sqrt{x(1+x)}}=\operatorname{arsinh}\sqrt X,
\]
\(X=8\) 的 \(\operatorname{Ric}=-g\) 半径为
\[
\sqrt6\,\operatorname{arsinh}\sqrt8\approx4.32.
\]

## 5. 固定大球在有限覆盖中的供给

设 \(\Gamma\) 是紧 CH 曲面的无挠格，\(\widetilde p\in\mathbb{CH}^2\)，\(r\) 包含整个 cell 及缓冲 collar。集合
\[
\mathcal F_r=
\{\gamma\in\Gamma\setminus\{1\}:
d(\widetilde p,\gamma\widetilde p)\le2r\}
\]
由 proper discontinuity 可知是有限集。格群是有限生成线性群，因而 residually finite。对每个 \(\gamma\in\mathcal F_r\) 取不含它的有限指数正规子群，再取有限交，得到
\[
\Gamma_*\cap\mathcal F_r=\varnothing.
\]
于是 \(B_r(\widetilde p)\) 在
\[
X_*=\mathbb{CH}^2/\Gamma_*
\]
中嵌入：若球中两点被某个 \(\gamma\in\Gamma_*\) 识别，则三角不等式会给出
\(d(\widetilde p,\gamma\widetilde p)<2r\)，与构造矛盾。

在任一进一步有限覆盖 \(X_j\to X_*\) 中，该球的原像是互不相交的等距复制，复制数等于覆盖次数。与此同时
\[
A_j=c_1^2(X_j)
=[X_j:X_*]\,c_1^2(X_*).
\]
故可用的固定大球数严格与 \(A_j\) 成正比。平衡族满足
\[
Q_j=o(A_j),\qquad k_j+\ell_j=O(Q_j),
\]
所以这些复制足以容纳全部 blow-up cells 和 handle surgeries。该论证支持“适当选择的覆盖塔”这一存在性表述，而不要求先前任意指定的覆盖塔都具有同样的大球。

## 6. I54 转移算术

记
\[
Q_j=k_j+4\ell_j,\qquad h_j=\frac{Q_j}{A_j},
\]
且
\[
\frac{k_j}{Q_j}\to\frac29,\qquad
\frac{\ell_j}{Q_j}\to\frac7{36}.
\]
每个 blow-up cell 的代价为 \(J_1\)，每个标准 handle surgery 的一阶代价为 \(32\pi^2\)。体积与总标量的一阶交叉项在 \(Q_j=o(A_j)\) 时贡献 \(o(Q_j)\)。因此
\[
\begin{aligned}
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
&\le
\frac29\frac{J_1}{2\pi^2}
+\frac7{36}\frac{32\pi^2}{2\pi^2}\\
&=\frac{J_1}{9\pi^2}+\frac{28}{9}.
\end{aligned}
\]
若
\[
J_1=8\pi^2(1-\varepsilon_0),
\]
则右端为
\[
4-\frac{8\varepsilon_0}{9}.
\]

使用一次固定平滑并取
\(\varepsilon_0=\eta_8^*/2\)，得到
\[
\limsup\frac{\alpha}{h}
\le4-\frac{4\eta_8^*}{9}
\approx3.9996072192.
\]
更精确地，对每个给定 \(\epsilon>0\)，先固定一个足够小的 \(\delta(\epsilon)\)，再构造相应的全局序列，可得
\[
\limsup\frac{\alpha}{h}
\le4-\frac{8\eta_8^*}{9}+\epsilon
\approx3.9992144384+\epsilon.
\]
\(X=16\) 给出
\[
4-\frac{8\eta_{16}^*}{9}
\approx3.9990248389.
\]
因此“低于四”的全局推论与平滑、缩放、覆盖供给及比例算术一致。

## 7. 纯 handle exact-CH cell 必须满足 \(J\ge32\pi^2\ell\)

这一点可由继承的精确公式严格推出。

设
\[
C=D\#\ell(S^1\times S^3)
\]
带任意光滑 exact-CH outer collar 度量，并记
\[
v=\operatorname{Vol}(C),\quad
I=\int_Cs,\quad
R=\int_C|\operatorname{Ric}|^2,
\]
\[
t=I+4v,\qquad
J=R+2I+4v=\int_C|\operatorname{Ric}+g|^2.
\]
把该固定 cell 插入 \(c_1^2=A\) 的 CH 有限覆盖。所得闭流形为
\[
M_A=X_A\#\ell(S^1\times S^3),\qquad
h_A=\frac{4\ell}{A}.
\]
若 \(V_A=2\pi^2A+(v-d)\) 是替换后的总体积，则精确 cell 代数给出
\[
\mathcal E(g_A)
=
\frac{4J-t^2/V_A}{4V_A+J-2t}.
\]
令 \(A\to\infty\)，得到
\[
\frac{\mathcal E(g_A)}{h_A}
\longrightarrow
\frac{J}{8\pi^2\ell}.
\]

另一方面，纯 handle 闭流形的精确全度量公式是
\[
\alpha(M_A)=\frac{4h_A}{1+h_A}
\qquad (h_A\le1/3).
\]
由于 \(\alpha(M_A)\le\mathcal E(g_A)\)，
\[
\frac{\mathcal E(g_A)}{h_A}
\ge
\frac{\alpha(M_A)}{h_A}
=\frac4{1+h_A}.
\]
取极限即得
\[
\frac{J}{8\pi^2\ell}\ge4,
\]
也就是
\[
\boxed{J\ge32\pi^2\ell.}
\]

所以，在相同 exact-CH collar 与 \(J=\int|\operatorname{Ric}+g|^2\) 归一化下，孤立的纯 handle cell 不可能低于 \(32\pi^2\ell\)。结合经典缩小 surgery 序列，若允许在固定 CH 区域内让 surgery 尺度趋零，则纯 handle cell infimum 正是 \(32\pi^2\ell\)。

这也表明 Step 10 中“handle cells 能否低于 \(32\pi^2\)”若按孤立纯 handle cell 理解，与精确公式不相容。

## 8. 真正不同的问题：混合 cell 的非加性相互作用

定义
\[
\mathfrak J_{k,\ell}
=
\inf\left\{
\int_C|\operatorname{Ric}+g|^2:
C=D\#k\overline{\mathbb{CP}}^{\,2}
\#\ell(S^1\times S^3),
\ g\text{ 在外侧 collar 上精确为 CH}
\right\},
\]
其中允许选择足够大的固定 CH 球。上节给出
\[
\mathfrak J_{0,\ell}=32\pi^2\ell.
\]
但这并不推出
\[
\mathfrak J_{k,\ell}
\ge
\mathfrak J_{k,0}+32\pi^2\ell.
\]
\(J\) 的相对 Chern–Weil 表达式涉及整个 cell 上的标量曲率和 \(W^+\) 分布，并不会按 connected-sum 拓扑块自动相加。冻结 blow-up cell 已经给出
\[
\mathfrak J_{1,0}<8\pi^2,
\]
说明一旦 \(k>0\)，标准拓扑权重 \(8\pi^2(k+4\ell)\) 本身就不再是普遍的局部下界。

平衡比例的最小整数块是
\[
(k,\ell,q)=(8,7,36).
\]
重复使用一个这样的混合 cell 时，全局一阶系数为
\[
c_{\rm mix}=\frac{\mathfrak J_{8,7}}{72\pi^2}.
\]
其绝对低于四的条件是
\[
\mathfrak J_{8,7}<288\pi^2.
\]
分离式构造的基准为
\[
\mathfrak J_{\rm sep}
=
8\mathfrak J_{1,0}+7(32\pi^2)
=
8\mathfrak J_{1,0}+224\pi^2,
\]
对应
\[
c_{\rm sep}
=
\frac{\mathfrak J_{\rm sep}}{72\pi^2}
=
\frac{28}{9}
+\frac{\mathfrak J_{1,0}}{9\pi^2}.
\]

因此真正的混合相互作用问题是严格次可加性：
\[
\boxed{
\mathfrak J_{8,7}
<
8\mathfrak J_{1,0}+224\pi^2\;?
}
\]
它询问的是 handles 与 blow-up 几何放在同一个 cell 后，是否能共同重排 Ricci 缺陷、标量平方和手性 Weyl 能量，从而使总成本低于八个 blow-up cells 加七个纯 handle cells 的总和。这与孤立纯 handle cell 低于 \(32\pi^2\) 是两个不同命题。

进一步，分离式路线即使令 blow-up cell 代价趋零，也只能逼近
\[
\frac{28}{9}.
\]
若要低于这一数值，需要某个混合 cell 满足
\[
\mathfrak J_{8,7}<224\pi^2.
\]
纯 handle 定理并不排除这种混合现象；现有材料也尚未计算 \(\mathfrak J_{8,7}\) 或证明上述严格次可加性。
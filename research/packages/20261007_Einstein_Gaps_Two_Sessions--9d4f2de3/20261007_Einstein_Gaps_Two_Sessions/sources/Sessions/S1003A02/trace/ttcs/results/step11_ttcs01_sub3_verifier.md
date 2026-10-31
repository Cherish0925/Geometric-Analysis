# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md",
    "Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py",
    "Sessions/S1003A02/workspace/scripts/o11_collar_arb_certificate.py",
    "Sessions/S1003A02/workspace/data/o11_collar_independent_x001_X8.json",
    "Sessions/S1003A02/workspace/data/o11_collar_arb_x001_X8.json",
    "Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json",
    "Skills/geometric-analysis/research/paper/sections/variational_geometry.tex"
  ]
}
```

## Task

Read the fixed perpendicular complex-hyperbolic cell record and both independent verification notes/scripts. Check the mathematical chain needed for a strict same-metric cell J_6<8π²: normalization, Cartan/relative identities, bolt smoothness, positivity, CH attachment and smoothing, numerical integral, residual-finite cover supply, and inherited global transfer. Identify any substantive error that would invalidate the candidate, and distinguish what is proved from what remains numerical. In particular inspect the 160-bit Arb script: say exactly what it encloses and whether its Richardson-inflated result is or is not a rigorous quadrature certificate. Give a direct scientific memo aimed at completing O11, not generic review.

## Output

# 数学核验备忘录：有限尺度垂直复双曲胞腔

## 核心结论

在所给记录、两套重建程序及变分传递公式之间，没有发现会使候选胞腔失效的归一化错误、拓扑类型错误、光滑性错误或全局传递系数错误。数值结果也不是把不同度量所得的 \(P\) 与标量项拼接起来：两项均由同一组 \(G,F,w\) 及其导数计算。

目前尚未严格成立的是
\[
J_6<8\pi^2.
\]
160-bit Arb 程序严格包住了有限个 Simpson 节点上的函数值以及相应的有限加权和，但没有严格包住积分：程序没有计算四阶导数上界，也没有处理 \(u\in[0,10^{-12}]\) 的遗漏积分。因此输出字段 `J_enclosure` 和 `J_upper` 不是积分的严格区间证书。它们是很强的数值证据，但不能单独完成 O11。

另有一个不影响 \(P,J\) 输出的代码细节：`o11_collar_independent_verify.py` 中返回但未使用的
```python
C = jnp.sum(u*u)+jnp.prod(u)
```
不是相对分解所对应的端点原函数；正确原函数是
\[
u_1^2+u_3^2+u_1u_2u_3.
\]
这不进入脚本报告的任何积分值，但相关注释不准确。

---

## 1. 归一化与“同一度量”问题

在四维，
\[
\Ric=\Ric^\circ+\frac{s}{4}g,
\]
且无迹部分与纯迹部分正交。因此
\[
\begin{aligned}
|\Ric+6g|^2
&=\left|\Ric^\circ+\left(\frac{s}{4}+6\right)g\right|^2\\
&=|\Ric^\circ|^2+4\left(\frac{s}{4}+6\right)^2\\
&=|\Ric^\circ|^2+\frac14(s+24)^2.
\end{aligned}
\]
所以
\[
J_6=P+\frac14\int(s+24)^2
\]
是精确恒等式。

令 \(\widetilde g=6g\)。常数缩放下，作为 \((0,2)\)-张量的 Ricci 曲率不变，
\[
\Ric_{\widetilde g}=\Ric_g,
\qquad
\Ric_{\widetilde g}+\widetilde g=\Ric_g+6g.
\]
同时
\[
|T|_{\widetilde g}^2=6^{-2}|T|_g^2,\qquad
dV_{\widetilde g}=6^2dV_g.
\]
故
\[
\int|\Ric_{\widetilde g}+\widetilde g|_{\widetilde g}^2\,dV_{\widetilde g}
=J_6(g).
\]
这与全局构造中 \(\Ric=-g\) 的归一化完全一致。

在独立 JAX 程序中，`P_positive`、`P_relative` 和 `scalar` 都由同一个 `Metric` 实例及同一组 quadrature 节点计算。Arb 程序也在同一个 `dens_x` 调用中相加相对 \(P\) 密度和标量平方密度。因此不存在跨度量拼接。

---

## 2. Cartan 公式与相对恒等式

采用脚本中的轴次序
\[
(a_1,a_2,a_3)
=\bigl(\sqrt{x},\sqrt{xe^w},\sqrt F\bigr),
\qquad
\frac{dx}{dt}=2\sqrt G.
\]
定义
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},
\qquad
H_i=u_i+\frac12u_ju_k,
\qquad
\lambda_i=\frac{a_ja_k}{a_i}.
\]

正平方密度为
\[
\mathcal P
=\sum_i\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2.
\]
相对密度写成
\[
\begin{aligned}
\mathcal R={}&
\frac{\lambda_1}{4}
 \left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2\\
&+\frac{\lambda_2}{4}
 \left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2\\
&+\frac{\lambda_3}{4}
 \left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}.
\end{aligned}
\]
直接展开平方可得精确恒等式
\[
\boxed{\;
\mathcal P-\mathcal R
=-\frac{d}{dt}\left(u_1^2+u_3^2+u_1u_2u_3\right).
\;}
\]

在 bolt 端，由光滑展开得到
\[
(u_1,u_2,u_3)\longrightarrow(0,0,-1),
\]
而在复双曲外端
\[
(u_1,u_2,u_3)=(0,3x,0).
\]
因此端点原函数从 \(1\) 变为 \(0\)，从而
\[
\frac{P}{8\pi^2}
=1+\int\mathcal R\,dt.
\]
这解释了相对公式中的常数 \(1\)，也把 \(8\pi^2\) 的单胞阈值固定下来。

脚本中的未使用量
\[
\sum_i u_i^2+u_1u_2u_3
\]
在复双曲端等于 \(9X^2\)，显然不是上述原函数。由于它既未进入 `P_relative`，也未进入 `P_positive`、`scalar` 或 `J`，故不改变报告数值。

复双曲剖面是
\[
G=x+x^2,\qquad F=x,\qquad w=\log(1+x).
\]
代入可得
\[
u=(0,3x,0),\qquad
\dot u_2=6\sqrt{x(1+x)},\qquad
\lambda_2=\sqrt{\frac{x}{1+x}},
\]
于是
\[
\dot u_2=\frac{2H_2}{\lambda_2},
\]
所有正平方均为零。标量公式中的
\[
\Sigma=\sum_i\left(\frac{\dot u_i}{a_i}
+\frac{2H_i}{a_ja_k}\right)
\]
在该剖面上恰为 \(12\)，所以脚本的
\[
\frac{a_1a_2a_3}{4}(\Sigma-12)^2
\]
也为零。这是背景标量曲率 \(s=-24\) 与 `Sigma-12` 常数选择的精确一致性测试。

在标准主轨道体积 \(2\pi^2\) 的约定下，
\[
s+24=2(\Sigma-12),
\]
故
\[
\frac1{8\pi^2}\frac14\int(s+24)^2dV
=\int\frac{a_1a_2a_3}{4}(\Sigma-12)^2dt,
\]
正是两套程序使用的标量平方积分。

---

## 3. Bolt 光滑性与度量正定性

令 \(y=x-x_0\)。由剖面公式及 \(S(u)=10u^3-15u^4+6u^5\)，在 \(x=x_0\) 有
\[
F=f_1y+O(y^2),\qquad
G=g_1y+O(y^2),\qquad
w=O(y^2).
\]
程序中对 \(c_G\) 的常数平移使
\[
q_F(0)+q_G(0)=0,
\]
所以
\[
f_1g_1=e^{q_F(0)+q_G(0)}=1
\]
是代数恒等式，而不只是浮点近似。数值为
\[
f_1=0.9688603622004124,\qquad
g_1=1.0321404807281673.
\]

取
\[
\rho=\sqrt{\frac{y}{g_1}}+O(y^{3/2}).
\]
则
\[
\frac{dy^2}{4G}=d\rho^2+O(\rho^2)d\rho^2,
\qquad
F=\rho^2+O(\rho^4).
\]
另外
\[
x=x_0+g_1\rho^2+O(\rho^4),\qquad
xe^w-x=O(\rho^4).
\]
因此两个非塌缩方向在 bolt 上具有相同长度平方 \(x_0\)，其差到四阶才出现；塌缩方向是标准极坐标形式
\[
d\rho^2+\rho^2\sigma_1^2.
\]
在继承构造所使用的 \(\sigma_1\) 周期约定下，这给出光滑的 \((-1)\)-圆盘丛，即一次 blow-up 胞腔。最终论文中应显式写明该周期约定；现有复双曲极坐标模型使用同一约定，没有看到因子 \(2\) 或 \(4\) 的不一致。

正定性不依赖网格采样。对 \(x_0<x\le X\)，
\[
F=(x-x_0)e^{q_F}+x_0S(u)>0,
\]
且
\[
G=\bigl[(x-x_0)+(x^2+x_0)S(u)\bigr]e^{q_G}>0.
\]
这里
\[
S'(u)=30u^2(1-u)^2\ge0,\qquad S(0)=0,\quad S(1)=1,
\]
所以 \(0\le S\le1\)。此外 \(x>0\) 且 \(e^w>0\)。样本最小值
\[
\min\frac{G}{x-x_0}=1.0321404811,\qquad
\min\frac{F}{x-x_0}=0.9661766585
\]
只反映数值条件良好，正定性本身已经由公式给出。

---

## 4. 复双曲接合与光滑化

令 \(v=1-u\)。平滑步函数满足
\[
S(u)=1-10v^3+15v^4-6v^5.
\]
全部自由扰动都含 \(v^3\)，故在 \(x=X\)
\[
(G,F,w)
=(x+x^2,\ x,\ \log(1+x))
\]
并且前两阶 \(x\)-导数也完全相同。`endpoint()` 只输出了一阶导数，但二阶匹配直接来自上述三阶消失结构。

直接拼接得到全局 \(C^2\) 度量。设 \(z=X-x\)，其相对复双曲度量的偏差为
\[
h=O(z^3),\qquad
\partial h=O(z^2),\qquad
\partial^2h=O(z).
\]
在宽度 \(\delta\) 的接合带中用平坦 cutoff 截去 \(h\) 后，
\[
h_\delta-h=O(\delta^3),\quad
\partial(h_\delta-h)=O(\delta^2),\quad
\partial^2(h_\delta-h)=O(\delta).
\]
所以 Ricci 缺陷改变 \(O(\delta)\)。原度量在该接合带内的 Ricci 缺陷本身也是 \(O(\delta)\)，而体积为 \(O(\delta)\)，因此
\[
J_6(g_\delta)-J_6(g)=O(\delta^3).
\]
一旦未光滑剖面的严格亏量得到积分证书，就存在充分小的 \(\delta\) 使光滑且具有精确复双曲 collar 的胞腔仍满足
\[
J_6(g_\delta)<8\pi^2.
\]
此处只需定性 \(O(\delta^3)\) 估计即可证明存在性；若希望给出某个固定 cutoff 的十进制亏量，则还需写出相应常数。

数值 \(3.9992144383\) 对应未光滑 \(C^2\) 剖面，或者对应 \(\delta\to0\) 的光滑化序列。单个未量化的平滑胞腔给出某个严格小于 \(4\) 的系数，但不自动等于打印出的全部小数位。令全局序列中的 \(\delta_j\to0\) 可以在 \(\limsup\) 中恢复该数值。

---

## 5. 浮点积分给出的证据

独立 JAX 重建给出
\[
\begin{aligned}
S_1&=0.00159729167196687,\\
S_2&=0.00052244698325698,\\
S_3&=0.00109028656646375,\\
C_3&=-0.00410132248809498.
\end{aligned}
\]
因此
\[
\frac{P}{8\pi^2}
=1+S_1+S_2+S_3+C_3
=0.9991087027335926.
\]
同一剖面的标量平方为
\[
\frac{J_6-P}{8\pi^2}
=7.54040173166\times10^{-6},
\]
从而
\[
\boxed{\;
\frac{J_6}{8\pi^2}
=0.9991162431353243,
\qquad
1-\frac{J_6}{8\pi^2}
=8.83756864676\times10^{-4}.
\;}
\]

200、400、800 阶分段 Gauss 结果在所显示位数上一致；正平方公式和相对公式相差不到 \(5\times10^{-15}\)。记录文件内的较早数值
\[
J=0.9991162428177064
\]
与独立重建相差约 \(3.2\times10^{-10}\)，来自旧的 600 节点计算，不参与最终数值。

这些结果非常稳定，而且亏量比观察到的离散变化大约八个数量级。不过，浮点稳定性本身不是严格积分上界。

---

## 6. 160-bit Arb 程序到底包住了什么

### 6.1 严格包住的对象

`J2` 代数正确传播剖面到二阶 \(x\)-导数。`dens_x` 需要 \(a_i,a_i',a_i''\)，因而二阶 jet 足够计算 \(u_i\) 和 \(\dot u_i\)。对每一个 Simpson 节点，Arb 包住：

1. 输入十进制系数经过 `repr(float(...))` 后得到的数；
2. \(G,F,w\) 及相应导数；
3. 相对 \(P\) 密度和标量平方密度；
4. 160-bit 运算舍入；
5. 节点值的有限 Simpson 加权和。

输出中的
\[
[-0.00088375686366234348\pm 4.74\times10^{-30}]
\]
可视为对 \(n=2000\) 有限 Simpson 和的严格包球。

输入先经 `json.loads` 转为 binary64，再由 `repr` 送入 Arb。该记录本来就是 Python 浮点导出的 JSON，所列字符串与通常的 `repr` 一致；不过从代码本身看，它定义的是 `repr(binary64)` 所对应的胞腔。直接用 `parse_float=str` 再转 Arb 会使“JSON 中写出的十进制数”这一数学对象更加明确。

### 6.2 没有包住的对象

程序定义
\[
e=\frac{|S_{2000}-S_{1000}|}{15},
\qquad
r=1000e,
\]
然后输出
\[
1+\operatorname{mid}(S_{2000})+[-r,r].
\]
这里除以 \(15\) 使用了 Simpson 主误差为 \(Ch^4\) 的渐近模型；乘以 \(1000\) 只是经验放大。代码没有给出
\[
\sup |f^{(4)}|
\]
的 Arb 区间，也没有其他定理把相邻网格差转成积分误差。因此
\[
J_{\rm upper}=0.999116244147447\ldots
\]
不是积分的严格上界。

此外，程序实际积分的是
\[
u\in[10^{-12},1].
\]
注释写道遗漏部分会另行包住，但 `simpson()` 只返回 Simpson 和与节点值；没有任何代码估计
\[
\int_0^{10^{-12}}f(u)\,du.
\]
这也是严格证书中必须补上的一项。

程序开头关于“rigorous global fourth-derivative remainder”的描述与实际代码不一致：程序没有构造四阶导数，也没有相应的全局上界。

### 6.3 现有网格所需的导数估计并不苛刻

若正则化后的密度记为 \(f(u)\)，复合 Simpson 公式给出
\[
\left|\int_\epsilon^1f-S_n\right|
\le
\frac{(1-\epsilon)^5}{180n^4}
\sup_{\epsilon\le u\le1}|f^{(4)}(u)|.
\]
对于 \(n=2000\)，只需总误差小于
\[
8.8\times10^{-4}
\]
即可确定符号。忽略极小的端点段后，一个足够的粗略目标是
\[
\sup|f^{(4)}|<2.5\times10^{12}.
\]
因此不需要复现 \(10^{-9}\) 的 Richardson 半径；一个相当宽松的解析或 Arb 四阶导数上界已经足够。

适合区间计算的正则变量是
\[
y=x-x_0,\qquad
F=y\widehat F,\qquad
G=y\widehat G,\qquad
w=y^2\widehat w.
\]
由给定剖面，
\[
\widehat F,\widehat G,\widehat w
\]
在 \(y=0\) 都是解析函数，且 \(\widehat F,\widehat G>0\)。先代数消去 \(\sqrt y\) 与 \(1/\sqrt y\) 的可去项后，相对密度加标量密度在 \(u=0\) 具有普通 Taylor 展开。此正则化表达式可以直接接受 Arb 分段 Taylor 积分，或用于求取 Simpson 四阶导数上界及
\[
\left|\int_0^{10^{-12}}f\right|
\]
的显式估计。只要最终区间的上端低于零，例如得到
\[
\int_0^1f(u)\,du<-8\times10^{-4},
\]
就足以完成严格不等式，无需追求现有浮点小数位。

---

## 7. 有限覆盖中的大球供应

在 \(\mathbb{CH}^2\) 中固定中心 \(p\) 和包含胞腔及接合带的半径 \(r\)。满足
\[
d(p,\gamma p)\le2r
\]
的格元素只有有限多个。逐一用剩余有限性排除这些元素，并取对应有限指数正规子群的交，可得有限覆盖 \(X_*\)，使 \(p\) 的投影处含有嵌入的半径 \(r\) 球。

任一进一步有限覆盖 \(Y\to X_*\) 中，该球的原像是互不相交的等距副本，其数目等于覆盖次数。若
\[
A(Y)=d\,A(X_*),
\]
可用大球数就是 \(d\)，与 \(A(Y)\) 成正比。

在平衡族中
\[
k_j\sim\frac29Q_j,\qquad Q_j=A_jh_j,\qquad h_j\to0,
\]
所以
\[
\frac{k_j}{d_j}
\sim \frac29 A(X_*)h_j\longrightarrow0.
\]
因而大球副本数远多于需要的有限尺度 blow-up 胞腔数。半径换算
\[
r_{-6}=\operatorname{arsinh}\sqrt8,\qquad
r_{-1}=\sqrt6\,\operatorname{arsinh}\sqrt8\approx4.32
\]
也是正确的。

---

## 8. 全局传递系数

设光滑胞腔在 \(\Ric=-g\) 归一化下的代价为 \(J_1\)。每个 handle 的标准缩小构造代价趋于 \(32\pi^2\)。复双曲外部没有 \(\Ric+g\) 缺陷。因此
\[
\int_{M_j}|\Ric+g|^2
\le k_jJ_1+32\pi^2\ell_j+o(Q_j).
\]
总体积为
\[
2\pi^2A_j+O(Q_j),
\]
而 \(Q_j/A_j=h_j\to0\)，所以体积修正只产生 \(o(h_j)\) 的归一化影响。于是
\[
\limsup\frac{\alpha(M_j)}{h_j}
\le
\lim_j
\frac{k_jJ_1+32\pi^2\ell_j}{2\pi^2Q_j}.
\]
使用
\[
\frac{k_j}{Q_j}\to\frac29,\qquad
\frac{\ell_j}{Q_j}\to\frac7{36},
\]
得到
\[
\boxed{\;
\limsup\frac{\alpha(M_j)}{h_j}
\le
\frac{J_1}{9\pi^2}+\frac{28}{9}.
\;}
\]
若
\[
J_1=8\pi^2(1-\varepsilon_0),
\]
则
\[
\limsup\frac{\alpha(M_j)}{h_j}
\le4-\frac{8\varepsilon_0}{9}.
\]
以未光滑剖面的数值
\[
\varepsilon_0=0.000883756864676
\]
代入，得到
\[
4-\frac{8\varepsilon_0}{9}
=3.9992144383\ldots.
\]
该代数传递完全正确。任意一个严格次阈值的固定光滑胞腔已经足以把系数压到 \(4\) 以下；若采用 \(\delta_j\to0\) 的光滑化，则 \(\limsup\) 可达到上述未光滑剖面的胞腔代价。

---

## 最终科学状态

1. \(J_6=\int|\Ric+6g|^2\) 的归一化、缩放和同度量性质严格正确。
2. Cartan 正平方公式与相对公式相容；相对公式的端点常数确为 \(1\)。
3. bolt 条件、无锥关系、横向各向异性阶数以及正定性由剖面公式直接成立。
4. 外端与复双曲剖面具有相同二阶 jet；光滑 cutoff 的能量改变量为 \(O(\delta^3)\)。
5. 三组 Gauss 积分、两种 \(P\) 公式及 Arb Simpson 序列共同给出高度稳定的
   \[
   J_6/(8\pi^2)\approx0.9991162431353.
   \]
6. 160-bit Arb 输出只严格包住有限 Simpson 和，不严格包住积分；Richardson 差的 1000 倍放大没有定理支撑，并且 \(u\in[0,10^{-12}]\) 没有被积分或估计。
7. 固定大球的覆盖供应与
   \[
   \frac{28}{9}+\frac{J_1}{9\pi^2}
   \]
   传递公式均成立。
8. O11 的最后数学对象是正则化相对加标量密度的严格积分区间。现有 \(8.84\times10^{-4}\) 亏量允许很宽的误差预算；获得任何上端低于零的 Arb/Taylor 或 Simpson-导数区间，即可把该候选转化为严格的次 \(8\pi^2\) 光滑胞腔，并由现有全局构造推出系数严格小于四。
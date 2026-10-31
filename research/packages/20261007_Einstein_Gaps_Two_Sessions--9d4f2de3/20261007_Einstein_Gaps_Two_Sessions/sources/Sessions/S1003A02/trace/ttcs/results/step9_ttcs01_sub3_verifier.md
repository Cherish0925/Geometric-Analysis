# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/o11_general_bulk_cell.py",
    "Sessions/S1003A02/workspace/scripts/o11_radial_hessian.py",
    "Sessions/S1003A02/workspace/scripts/o11_full_hessian.py",
    "Sessions/S1003A02/workspace/scripts/o11_full_hessian2.py",
    "Sessions/S1003A02/workspace/data/o11perp/radial_hessian_x0.03_n6b.json",
    "Sessions/S1003A02/workspace/data/o11perp/radial_hessian_x0.03_n8.json",
    "Sessions/S1003A02/workspace/data/o11perp/perp_smooth_hi_x0.03.json",
    "Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md"
  ]
}
```

## Task

Read the attached O11 computation artifacts as a geometric analyst and assess what is scientifically established by the new Fubini–Study versus complex-hyperbolic sign experiment and by the attempted Hessian tests. Check normalizations and the inference that P/(8π²)=1-x0 R^+(ζ,ζ)+O(x0²): in the code the complex-space-form collar is K=x+kappa x² with s=-24kappa and aligned R^+(ω,ω)=-6kappa. Determine whether P<1 for kappa=-1 is a genuine same-metric cell result, whether the finite outer radius or interpolation can mimic the sign, and what asymptotic extrapolation is justified by x0=.001,.003. Then evaluate the second-variation design: full radial symmetric-h Hessian and non-invariant coordinate/coframe Hessians, their quadrature consistency, base stationarity, diffeomorphism modes, and why negative numerical eigenvalues accompanied by two-sided energy rise are not yet negative directions. Recommend one mathematically decisive executable next check that stays focused on the spectral problem modulo diffeomorphisms.

## Output

# 科学核验备忘

## 1. 归一化与符号实验

先区分记号：脚本中的 `P` 是
\[
\widehat P(g):=\frac1{8\pi^2}\int |\operatorname{Ric}^\circ_g|^2\,dV_g,
\]
而研究笔记中有些段落把未除 \(8\pi^2\) 的积分也记作 \(P\)。

对
\[
g=\frac{dx^2}{4K}+x(\sigma_1^2+\sigma_2^2)+K\sigma_3^2
\]
可直接算得
\[
s=-4K''-\frac{8K'}x+\frac8x.
\]
因此 \(K=x+\kappa x^2\) 给出
\[
s=-24\kappa.
\]
在 Kähler 曲率方向上，
\[
W^+(\omega)=\frac{s}{6}\omega,\qquad
\mathcal R^+=W^++\frac{s}{12}I,
\]
故
\[
\mathcal R^+(\omega,\omega)=\frac{s}{4}=-6\kappa.
\]
于是脚本中的预测
\[
\widehat P=1+6\kappa x_0+O(x_0^2)
          =1-x_0\mathcal R^+(\omega,\omega)+O(x_0^2)
\]
在归一化和符号上完全一致：

- \(\kappa=+1\)：\(s=-24\)，CH，首项为 \(1+6x_0\)；
- \(\kappa=-1\)：\(s=+24\)，FS，首项为 \(1-6x_0\)。

FS 情形要求 \(X<1\)，因为外侧 \(K=x-x^2\) 只在 \(0<x<1\) 为正。

---

## 2. 四常数 Kähler 插值可以解析验证首阶系数

这次符号实验不只可作数值观察；未加 profile 松弛的 Kähler seed 可直接积分。

令 Ricci 张量的两个 Kähler 实特征值为 \(A,A,B,B\)。对此 ansatz，
\[
B=\frac{-2xK'-2K+4x}{x^2},\qquad A=(xB)'.
\]
于是
\[
|\operatorname{Ric}^{\circ}|^2=(A-B)^2
=4\left(K''-\frac{2K}{x^2}+\frac2x\right)^2.
\]
又因
\[
dV=\pi^2x\,dx,
\]
得到
\[
\widehat P
=\frac12\int_{x_0}^{X}
\left(K''-\frac{2K}{x^2}+\frac2x\right)^2x\,dx.
\]

脚本采用
\[
K=x+\frac{c_1x^3}{4}-\frac{c_2}{2}+\alpha x^2+\frac{\beta}{x},
\]
而上述 integrand 中出现极简消去：
\[
K''-\frac{2K}{x^2}+\frac2x=c_1x+\frac{c_2}{x^2}.
\]
故 seed 的能量有精确公式
\[
\widehat P_0
=\frac{c_1^2}{8}(X^4-x_0^4)
+c_1c_2(X-x_0)
+\frac{c_2^2}{4}\left(\frac1{x_0^2}-\frac1{X^2}\right).
\]

记 \(t=x_0\)。由四个匹配方程展开可得
\[
c_1=-\frac{8t}{X^3}-\frac{24\kappa t^2}{X^3}+O(t^3),
\]
\[
c_2=2t+6\kappa t^2+\frac{18t^3}{X^2}+O(t^4).
\]
代回即得
\[
\boxed{\;
\widehat P_0
=1+6\kappa t
+9\left(\kappa^2+\frac1{X^2}\right)t^2
+O(t^3).
\;}
\]

这给出三个重要事实。

1. 首阶符号反转是解析结构，不依赖优化器。
2. 固定 \(X\) 且 \(t/X\to0\) 时，有限外半径首先进入 \(t^2\) 项，不能制造 \(6\kappa t\)。
3. 对 \(\kappa=-1\)，固定任意 \(0<X<1\)，充分小的 \(t\) 都有
   \[
   \widehat P_0<1.
   \]
   因而 FS 中低于 Burns 值 \(1\) 的 cell 已由显式 Kähler 度量实现，不需要 profile 优化才能出现。

在任意固定 \(x>0\) 处，匹配解还有展开
\[
K(x)=x+\kappa x^2+
t\left[-1+3\left(\frac{x}{X}\right)^2
-2\left(\frac{x}{X}\right)^3\right]+O(t^2).
\]
外部 Einstein 度量的 \(\operatorname{Ric}^{\circ}\) 为零；这里的度量扰动为 \(O(t)\)，所以远离 bolt 的曲率能量为 \(O(t^2)\)。首阶项来自 \(x=O(t)\) 的 Burns 缩放区，而不是外侧有限截断。

如果 \(X\) 很小，二阶项仍可在 \(t=.001,.003\) 上显著。例如斜率修正为
\[
9\left(1+X^{-2}\right)t
\]
于 FS seed。故两点拟合必须连同记录中的 \(X\) 一起解释；当 \(t/X\) 并不很小时，两点看起来可有明显偏斜。

---

## 3. `P<1` 是否为真实度量积分

脚本末尾使用
```python
s, r0, wa, wb, dv = c.fields(zz, 0.0)
P = sum(r0*wx*dv)/(8*pi**2)
```
直接计算 \(|\operatorname{Ric}^{\circ}|^2\) 的积分，没有减去 CH 或 FS 背景。因此，只要输出度量保持正定且 bolt、collar 匹配成立，\(\kappa=-1\) 的 `P<1` 是该度量本身的能量，而不是背景相减造成的数值。

这里有两点语义上的区分：

- \(\kappa=\pm1\) 两次运行当然对应两张不同的度量，因为 Einstein collar 和插值都改变了。
- 在单次 \(\kappa=-1\) 运行内，`P<1` 是一张实际 FS-cell 度量的积分值。

这也不与积分的点态正性冲突：数值 \(1\) 是完整 Burns ALE 度量的归一化总能量，不是每个带外侧 collar 的局部 cell 都必须满足的下界。

脚本所称的“direct integral”只独立于 `Cell.report` 中硬编码的 CH 扣除；它仍与优化目标共用 `Cell.fields` 及同一曲率实现。因此它排除了“背景扣除”这一解释，但不是第二套独立曲率程序。

另有两个实现细节值得明确：

- `min_K` 只检查未松弛的 seed，而且采样包含 \(x=x_0\)，那里 \(K=0\) 是 bolt 的预期行为。它没有给出优化后 \(G\) 与 \(h\) 在内部的最小特征值。
- 若要把输出视为光滑 cell，需要看到 \(G>0\)、\(h>0\) 在 \(x_0<x\le X\) 成立，并核实 profile 在两个端点按设计消失。即使优化器没有完全收敛，只要这些几何条件成立，输出仍是一张有效的显式度量。

随附材料没有包含 `o11_general_bulk_cell.py` 的 JSON 数值输出，因此这里能够验证程序的归一化、解析首阶系数和 `P<1` 的机制，但不能从所附文本复核某个具体运行的小数值。

---

## 4. \(x_0=.001,.003\) 支持到什么程度

令
\[
q_\kappa(t)=\frac{\widehat P_\kappa(t)-1}{t}.
\]
若假设
\[
q_\kappa(t)=a_\kappa+b_\kappa t+O(t^2),
\]
则 \(t=.001\) 与 \(t=.003\) 的两点 Richardson 外推为
\[
a_\kappa^{(2)}
=\frac{3q_\kappa(.001)-q_\kappa(.003)}2.
\]

笔记中已有 CH aligned 数据
\[
q_+(0.001)=5.956,\qquad q_+(0.003)=5.900,
\]
所以这两点给出
\[
a_+^{(2)}=5.984.
\]
更小尺度 \(3\times10^{-4},10^{-4}\) 的 5.984、5.994 才进一步显示其向 \(6\) 靠近。

对新 FS 实验，只有 \(0.001,0.003\) 两点时，可以支持：

- \(\widehat P<1\) 是稳定的有限尺度现象；
- 若 \(q_-\) 接近 \(-6\)，符号和首阶大小与解析响应一致；
- 在预设 \(O(t^2)\) 展开下，可以给出一个两点截距。

仅凭两点不能从数值上区分 \(t^2\)、\(t^2\log t\) 或优化 profile 的尺度漂移。对未松弛 Kähler seed，前述精确积分已经给出真正的幂级数展开；对优化后的有限参数族，首阶不变还需要 profile 在缩放区和外部区域的统一行为。

最能消除有限 \(X\) 偶次修正的组合是
\[
\frac{\widehat P_{+}(t,X)-\widehat P_{-}(t,X)}{2t}.
\]
对显式 seed，
\[
\frac{\widehat P_{+}-\widehat P_{-}}{2t}=6+O(t^2),
\]
因为 \(9(1+X^{-2})t^2\) 在两种符号间相消。另一个有用组合是
\[
\frac{\widehat P_{+}+\widehat P_{-}}2-1=O(t^2).
\]
在多个固定 \(X\) 上重复这两个组合，能直接分离首阶局部响应和外侧插值项。

科学上，新符号实验验证的是 aligned Kähler 方向上的系数。由于复空间形式中 \(s\) 与 \(W^+\) 同时变号，它本身没有单独分离 spin-0 与 spin-2 响应。一般
\[
1-x_0\mathcal R^+(\zeta,\zeta)
\]
的张量形式还使用了此前的角度实验和 \(SO(3)_+\) 等变性。数值优化产生的是显式上界序列；SU(2) cell 下确界的等式以及匹配下界并不由这些运行单独推出。

---

## 5. 径向 Hessian：积分一致，但基点不驻定

径向脚本的若干部分设计良好：

- \(G\) 与 \(h\) 的全部六个对称分量均被扰动；
- Chebyshev bubbles 固定 bolt 与 collar 数据；
- \(L^2\) Gram 矩阵使用了正确的径向和角向张量范数；
- 自动微分直接生成一阶与二阶导数。

基点积分的一致性非常好：
\[
1.0185958458021929
\quad\hbox{vs.}\quad
1.0185958454323307
\]
以及
\[
1.0185958458067998
\quad\hbox{vs.}\quad
1.0185958454323307.
\]
差约 \(3.7\times10^{-10}\)，说明径向 quadrature、体积因子与原 cell 的归一化彼此吻合。

但谱的主要问题是基点在扩大后的径向空间里并非驻点：

\[
\|\nabla \widehat P\|_{L^2}=5.22
\quad (n=6),
\qquad
12.65
\quad (n=8).
\]
原 JSON 的优化状态还是 `msg="ABNORMAL"`。它只在原有 30 参数 profile 内作过优化，并没有在新的 42 或 56 维 \(G,h\) 空间中消去一阶变分。

相应地，最小广义特征值从
\[
-1.63\quad(n=6)
\]
变为
\[
-23.18\quad(n=8),
\]
小于零的特征值数也从 1 变为 2。这个变化没有显示 Ritz 谱收敛。

更根本的是：在非驻定点，普通坐标 Hessian 依赖于度量参数化。这里 \(G\mapsto G e^d\) 是非线性参数化；坐标变换的二阶项会把“一阶梯度乘以参数化二阶导数”加入 Hessian。因此当前特征值还不是度量商空间上的几何二次型。

---

## 6. 为什么双侧能量上升没有给出下降二次模态

若 \(v\) 是驻定点处真正的小于零二次模态，则
\[
\widehat P(tv)+\widehat P(-tv)-2\widehat P(0)
=t^2H(v,v)+o(t^2)
\]
在充分小的 \(t\) 上应小于零。

现有曲线在 \(t=.005\) 给出相反现象。由表中数值计算：

- \(n=6\) 的对称二阶差商约为
  \[
  \frac{P(.005)+P(-.005)-2P(0)}{(.005)^2}
  \approx 4.26,
  \]
  而自动微分特征值为 \(-1.63\)。

- \(n=8\) 的同一差商约为
  \[
  59.7,
  \]
  而自动微分特征值为 \(-23.18\)。

这不说明自动微分必然有错；最低模态的原始系数达到 \(10^3\)–\(10^4\)，所以 \(t=.005\) 在点态上可能早已离开二次区。路径中的指数 \(G e^{td}\) 会进一步放大高阶项。合理的小参数应由
\[
\sup |\;g^{-1}(t h)\;|
\]
控制，而不是固定取 \(t=.005\)。

同时，两条曲线的中心一阶差商也不接近零：

- \(n=6\)：约 \(7.5\times10^{-3}\)；
- \(n=8\)：约 \(-3.6\times10^{-2}\)。

因此这些曲线混合了一阶漂移、二阶项和很大的高阶项，尚未展示驻定点上的下降二次方向。

---

## 7. 微分同胚模态为何会产生伪谱符号

对任意紧支撑向量场 \(X\)，泛函的微分同胚不变性给出
\[
d\widehat P_g(\mathcal L_Xg)=0.
\]
沿真实轨道 \(\phi_t^*g\) 再求一次导数，
\[
H_g(\mathcal L_Xg,\mathcal L_Xg)
+d\widehat P_g(\mathcal L_X^2g)=0.
\]
只有在 \(d\widehat P_g=0\) 时，原始 Hessian 才会在 Lie derivative 方向上消失。在当前非驻定基点，线性路径
\[
g+t\mathcal L_Xg
\]
缺少真实微分同胚轨道的二阶修正 \(\frac12t^2\mathcal L_X^2g\)，所以原始 Hessian 在 gauge 方向上可以呈任意符号。

当前最低径向模态主要落在 \(G\) 和 \(h\) 的对角分量中，恰好是径向重参数化
\[
X=f(x)\partial_x
\]
能够强烈进入的部分。因此 gauge 污染是一个具体机制，而不是抽象可能性。

此外，径向脚本只含 \(G,h\)，不含 \(dx\,\sigma_i\) 分量；一般 SU(2)-不变向量场的 Lie derivative 会产生这些交叉项。故当前张量空间甚至没有完整容纳 SU(2)-不变的 gauge 轨道。

---

## 8. 两个非不变 Hessian 脚本

### 8.1 坐标分量版本

`o11_full_hessian.py` 的说明文字说会加入 DeTurck/Bianchi penalty，但实现中没有计算 \(\beta_g(h)\)，也没有把任何 penalty 加入 \(H\)。返回的仍是原始 metric Hessian。

其基点角积分写法本身是合理的：以 \(u=\cos\theta\) 积分，再除以 \(\sin\theta\)，可正确恢复 \(d\theta\) 测度。

主要几何问题在于扰动由 Euler 坐标分量直接给出。常数 \(d\psi^2\)、\(d\psi\,d\phi\) 等并不自动定义为 \(S^3\) 上的全局光滑张量；在 Euler 极点处会带坐标奇性。Gram 矩阵中的逆度量又会放大这些奇性。由这类模态得到的谱可能随角 quadrature 和 Gram 截断强烈变化。

### 8.2 自然 coframe 版本

`o11_full_hessian2.py` 把扰动先放在
\[
(dx,\sigma_1,\sigma_2,\sigma_3)
\]
中，再转为 Euler 坐标。这正确修复了常数 coframe 模态的全局张量问题，并且加入了 \(dx\,\sigma_i\) 分量。

但默认 `nqa=2` 明显不足。即使在未扰动的 SU(2)-不变基点，体积密度含 \(\sin\theta\)，而脚本直接对 \(\theta\in[0,\pi]\) 使用二点 Gauss–Legendre。其对
\[
\int_0^\pi\sin\theta\,d\theta=2
\]
的近似比例为
\[
\frac{\pi\sin\!\left[\frac\pi2(1-1/\sqrt3)\right]}2
\approx0.968.
\]
所以默认设置下 `P_quad` 预期已有约百分之三的角积分偏差。对含二阶角导数的 Hessian，二点积分还会产生严重 aliasing。统一的整体因子有时会在广义特征值中相消，但非恒定角模态及其导数不会这样相消。

另外，\(\cos\theta,\sin\theta\cos\phi,\sin\theta\sin\phi\) 是可用的全局函数；单独的 \(\cos\psi,\sin\psi\) 在 Hopf/Euler 坐标转换处未必是全局光滑标量。非不变部分更适合用 Wigner \(D\)-functions 或明确的 \(S^3\) 标量、向量、张量谐波。

所附材料没有这两个脚本的输出 JSON，因此无法验证其 `P_quad/P_cell`、角积分收敛或谱随 `nqa` 的稳定性。仅从代码看，它们尚未实现微分同胚商空间上的 Hessian。

---

## 9. 一个聚焦而可执行的决定性谱实验

最直接的实验是完整的 **SU(2)-不变 Bianchi-slice Ritz 计算**。它足以处理当前已出现的小于零径向模态，同时避开低阶角积分和 Euler 坐标奇性。

采用自然 coframe 中全部十个径向张量分量，并配套四分量向量场
\[
X=f_0(x)\partial_x+\sum_{i=1}^3f_i(x)E_i,
\]
所有函数使用相同的端点 bubbles。令 \(B\) 为张量基，\(D\) 为 Lie derivative 映射
\[
D:X\longmapsto\mathcal L_Xg.
\]
以 \(G\) 表示 \(L^2\) Gram 矩阵，可取矩阵 \(Z\) 张成
\[
D^T G\,Z=0,
\]
等价于离散 Bianchi slice。随后在同一个 \(Z\)-空间内重新消去投影梯度，并计算
\[
Z^THZ\,u=\lambda\,Z^TGZ\,u.
\]

这一计算应同时输出三项恒等关系：

\[
d\widehat P(DX)\approx0,
\]
\[
HD\approx0
\quad\text{在驻定基点处},
\]
以及对最低商空间模态 \(h=Zu\)，
\[
\frac{\widehat P(th)+\widehat P(-th)-2\widehat P(0)}{t^2}
\longrightarrow \lambda\,\|h\|_{L^2}^2
\]
当 \(\sup|g^{-1}th|\) 逐级减小时成立。

因为 SU(2) 群积分可解析完成，这个实验只需要一维径向 quadrature。对 \(n=6,8,10,12\) 重复后，它会明确区分：

- 当前小于零特征值主要来自径向 gauge；
- 它来自非驻定基点和非线性参数化；
- 或者它在商空间、驻定基点和谱加密后仍保持为真正的二次下降模态。

## 总结

- 符号与归一化正确：\(\mathcal R^+(\omega,\omega)=-6\kappa\)。
- 四常数 Kähler seed 可解析得到
  \[
  \widehat P_0
  =1+6\kappa x_0+
  9(\kappa^2+X^{-2})x_0^2+O(x_0^3).
  \]
  因此 FS 的 \(\widehat P<1\) 是实际 cell 现象，有限外半径只在二阶进入首个显式修正。
- \(x_0=.001,.003\) 可支持首阶符号与近似系数；两点本身不足以数值建立优化后序列的完整渐近式。
- 径向积分归一化极为一致，但基点在扩大空间中远未驻定，谱也未随模态数稳定。
- 当前所有 Hessian 都尚未投影到微分同胚商空间；第一个全坐标脚本所述的 Bianchi penalty 实际未实现。
- 最有信息量的后续计算是自然 coframe 中完整 SU(2)-不变张量与向量基的 Bianchi 投影、同空间驻定化及商空间 Ritz 谱。
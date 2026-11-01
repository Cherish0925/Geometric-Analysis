# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 90,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step90_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step90_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the new Step 90 radial charged-core and forced-discharge computation as a scientific result. Read the structured reduction note and all four radial scripts/data summaries. Check: (1) whether the ODEs for gamma=dr^2+psi^2 dtheta^2, M=diag(e^alpha,e^-alpha), q=(q(r),0) correctly encode the reduced area, traceless-orbit, and horizontal equations under the stated forcing; (2) smooth-center coefficients, especially K(0)=3Q0/2; (3) whether monitoring the unused rr equation is meaningful and whether its small residual is algebraic/constraint propagation rather than accidental; (4) whether prescribed b=-A sin^2(pi s/L), w'=b-(3u+v)w/2 corresponds to mixed Ricci defect O(delta), and what endpoint regularity is missing for an exact splice; (5) interpret the numerical scaling without overstating it. Determine precisely what the runs establish or refute inside the reduced free/singular-orbit T^2 model, and identify any coefficient/sign error that changes the conclusion.

## Integrated Scientific Memo

## Step 90 径向计算核验结论

### 1. 径向 ODE 编码正确

取基底正交标架
\[
e_r=\partial_r,\qquad e_\theta=\psi^{-1}\partial_\theta,
\]
并记
\[
u=\sigma',\quad v=\alpha',\quad H=\psi'/\psi,\quad
K=-\psi''/\psi,\quad Q=\frac12q^2e^{-3\sigma-\alpha}.
\]
径向函数满足
\[
L\phi=\phi''+(H+u)\phi'.
\]

对 \(M=\operatorname{diag}(e^\alpha,e^{-\alpha})\)，形状映射位于 \(\mathbb H^2\) 的测地线上，且
\[
\tau_\sigma(\alpha)=v'+(H+u)v,\qquad
-\partial_\alpha Q=Q.
\]
因此在 \(T=Z=0\) 时，面积方程和无迹轨道方程分别为
\[
u'=6+Q-u^2-Hu,
\qquad
v'=Q-Hv-uv.
\]

水平方程的两个正交分量为
\[
K-u'-\frac12u^2=-3+Q+\frac12v^2+E_{rr},
\]
\[
K-Hu=-3+Q+E_{\theta\theta}.
\]
令 \(E_{\theta\theta}=0\)，得到
\[
K=-3+Q+Hu,\qquad H'=-K-H^2.
\]
故两个脚本所实现的方程与结构化约化一致；没有改变结论的 \(Q\) 符号、因子或常数错误。

变量电荷时应将 \(w\) 看作带符号的规范化电荷
\[
w=e^{-(3\sigma+\alpha)/2}q,\qquad Q=\frac12w^2.
\]
于是
\[
b=e^{-(3\sigma+\alpha)/2}q',
\qquad
\boxed{w'=b-\frac12(3u+v)w},
\]
正是 taper 脚本使用的方程。数值轨道在终点前保持 \(w\ge0\)，所以此处与 \(w=\sqrt{2Q}\) 一致。

---

### 2. 光滑中心系数正确

设
\[
u=Ar+O(r^3),\quad v=Br+O(r^3),\quad
H=r^{-1}+hr+O(r^3).
\]
由面积和形状方程的常数阶得
\[
A=\frac{6+Q_0}{2},\qquad B=\frac{Q_0}{2}.
\]
角向水平方程给出
\[
K(0)=-3+Q_0+A=\boxed{\frac32Q_0}.
\]
再由 \(H'=-K-H^2\) 得
\[
h=-\frac{K(0)}3=-\frac{Q_0}{2}.
\]
因此
\[
u=\frac{6+Q_0}{2}r+O(r^3),\qquad
v=\frac{Q_0}{2}r+O(r^3),
\]
\[
H=\frac1r-\frac{Q_0}{2}r+O(r^3),\qquad
\psi=r-\frac{Q_0}{4}r^3+O(r^5).
\]
脚本和笔记中的这些系数均正确。JSON 中的初始 \(K\) 值也逐项吻合 \(3Q_0/2\)。

非零电荷不妨碍中心处的四维度量光滑。中心塌缩的是基底极坐标的 \(\theta\)-圆，而原来的纤维 \(T^2\) 作用仍可自由；不过商空间是圆盘而不是自由模型所需的圆柱。这正是该构造不能直接进入两端最小分离曲线论证的拓扑差别。

---

### 3. 未使用的 \(rr\) 方程是传播约束，不是偶然数值检验

定义脚本监测的残差
\[
C:=E_{rr}
=K-u'+3-Q-\frac12u^2-\frac12v^2.
\]
利用被演化的方程可改写为
\[
C=-6-Q+\frac12u^2+2Hu-\frac12v^2.
\]
一般强迫下
\[
Q'=wb-(3u+v)Q,
\]
直接微分并代入 ODE 得到闭合恒等式
\[
\boxed{C'=-2(u+H)C-wb.}
\]

#### 常电荷核心

核心中 \(b=0\)，故
\[
\boxed{C'=-2(u+H)C.}
\]
光滑中心条件给出 \(C(0)=0\)，因而正规解满足 \(C\equiv0\)。所以核心系统实际上自动满足完整的水平方程；监测 \(C\) 是有意义的 Bianchi/约束传播检验。

脚本只在 \(r=\varepsilon\) 使用截断到最低阶的中心展开。其初始误差为
\[
C(\varepsilon)
=\left(\frac92+3Q_0+\frac12Q_0^2\right)\varepsilon^2
+O(\varepsilon^4).
\]
例如 \(Q_0=100,\varepsilon=10^{-5}\) 给出
\[
C(\varepsilon)\simeq5.3045\times10^{-7},
\]
与 JSON 的 \(5.3044999302\times10^{-7}\) 精确吻合。随后由于记录轨道上 \(u+H>0\)，该误差快速衰减。因此小残差不是偶然抵消。

#### 强迫 taper

这里
\[
C(s)=-e^{-2I(s)}
\int_0^s e^{2I(t)}w(t)b(t)\,dt,
\qquad I'=u+H,
\]
忽略极小的入射截断误差。由于 \(w=O(\delta)\)、\(b=O(\delta)\)，必有
\[
C=O(\delta^2).
\]
记录中 \(w\ge0,b\le0\)，故 \(C\ge0\)，也与数据符号一致。因而 taper 的 \(rr\) 标度有解析结构解释，而不只是数值拟合。

---

### 4. \(b\) 与混合 Ricci 缺陷的精确关系

由
\[
dq_1=\pm2\rho *_\gamma E(\,\cdot\,,K_1)
\]
以及单位竖直向量
\[
V_1=e^{-(\sigma+\alpha)/2}K_1
\]
可得本秩一径向模型中
\[
\boxed{|E(e_\theta,V_1)|=\frac{|b|}{2}}.
\]
径向 \(dq_1\) 经 Hodge 星变为角向混合分量。

在构造所强制的
\[
T=0,\quad Z=0,\quad E_{\theta\theta}=0
\]
条件下，适配正交标架中的缺陷只有 \(C=E_{rr}\) 和这一混合块，因此
\[
\boxed{\|E\|_{\rm op}=\max\{|C|,|b|/2\}.}
\]
27 次运行中最大
\[
\frac{\max|b|}{2\delta}
=\frac{1.8499415859}{2}
=0.9249707929,
\]
而 \(|C|/\delta\) 至多约 \(7.3\times10^{-3}\)。所以这些具体 collar 实际满足
\[
\|\operatorname{Ric}+3g\|_{\rm op}<0.925\,\delta.
\]
笔记所说“尚需最终 operator-norm 转换”过于保守：在此径向秩一约化内可以完成上述转换。不过 JSON 中 `T=0`、`Theta=0` 是方程构造的硬编码结果，并非独立重建完整四维 Ricci 张量所得。

---

### 5. taper 射击、标度和端点问题

在圆 cusp 线性极限 \(u=2,v=0\) 中，
\[
w'+3w=-A\sin^2(\pi s/L),\qquad
w(0)=\delta,\quad w(L)=0.
\]
令 \(k=2\pi/L\)，精确得到
\[
\boxed{
\frac A\delta=
\frac{6(9+k^2)}{k^2(e^{3L}-1)}.
}
\]
对 \(L=0.5,1,2\) 分别给出
\[
1.8215179,\qquad0.3860429,\qquad0.0285053,
\]
与运行范围吻合。

脚本注释中的“by linearity”并不严格：完整射击映射因
\[
Q=\frac12w^2
\]
反馈到 \(u,v,H\) 而是非线性的。但 `brentq` 求解的是实际耦合射击方程，因此这只是注释错误，不影响数值结果。

数据支持的是：

* 固定 \(L\) 时，\(\max|b|/\delta\) 在所采样参数上接近只依赖 \(L\) 的圆-cusp 常数；
* 当 \(\delta\) 变小时，各组更接近该线性极限；
* \(rr\) 缺陷按 \(\delta^2\) 缩放，并由约束源项 \(-wb\) 解析解释。

不能把有限的 \(Q_0\in\{1,10,100\}\)、\(\delta\in\{0.1,0.03,0.01\}\) 数据表述为已经证明“严格独立于 \(Q_0\)”或证明任意 \(Q_0\) 的全局渐近行为。

#### 端点正则性

\[
b=-A\sin^2(\pi s/L)
\]
在两端满足
\[
b=b'=0,\qquad b''\ne0.
\]
把它外延为零只能得到 \(C^1\) 的 \(b\)。由于
\[
q'=e^{(3\sigma+\alpha)/2}b,
\]
\(q\) 一般仅为 \(C^2\) 而非 \(C^3\)；相应连接势再光滑一阶，但仍不是 \(C^\infty\)。终端附近具体有
\[
b=O((L-s)^2),\qquad q=O((L-s)^3).
\]
精确光滑拼接需要端点全阶平坦的 forcing，并同时匹配几何变量的全部 jets。

此外，单符号 forcing 产生 \(C(L)>0\)。终点后取 \(b=0,q=0\) 会得到 OT 且 \(rr\) 缺陷继续衰减的近 Einstein 端，但不是立即接上的精确 Einstein 外部。若目标是精确 Einstein splice，还必须消除或补偿该 \(O(\delta^2)\) 约束缺陷。

---

### 6. 这些运行精确建立了什么

在所研究的径向圆盘商模型中，运行及解析约束恒等式共同建立：

1. 对所采样
   \[
   Q_0=0.1,1,3,10,30,100,
   \]
   常电荷约化解从光滑中心延拓到 \(r=4\)，并趋近
   \[
   (u,v,H,K,Q)=(2,0,1,-1,0).
   \]
   特别是 \(Q_0=100\) 时，原始数据确认
   \[
   Q<10^{-2}\ \text{于 }r\simeq0.982,\qquad
   Q<10^{-4}\ \text{于 }r\simeq1.720.
   \]

2. 核心不是“仅近似满足”完整约化 Einstein 方程：对于正规中心解，\(rr\) 方程由
   \[
   C'=-2(u+H)C
   \]
   精确传播。数值残差来自截断初始 jet。

3. 从 \(w=\delta\) 开始，27 个强迫 collar 均可通过 \(O(\delta)\) 的混合 Ricci forcing 将 \(w\) 射击至零，同时面积、无迹轨道和 \(\theta\theta\) 水平方程精确满足，剩余 \(rr\) 缺陷为结构性的 \(O(\delta^2)\)。

4. 因而，**仅凭局部 mixed-Ricci 控制和一个向外红移区域，不可能推出局部普适的 \(Q_+=O(\delta)\) 估计**：核心中 \(b=0\)，而中心正规展开允许任意有限的参数 \(Q_0\)。数值计算进一步展示了截至 \(Q_0=100\) 的具体红移轨道。

但这些材料没有证明：

* 对每个任意大的 \(Q_0\)，解都全局存在并具有上述渐近；
* 光滑、精确 Einstein 的 forced taper 或 exact OT splice；
* 自由圆柱商空间上的双端连接；
* 含最小分离曲线的全局构造；
* 紧致流形上的反例，更不构成对 Yau 第 26 题的反例。

“arbitrarily large physical core twist is compatible with the exact reduced equations”在**局部正规解族**意义上成立；作为“任意 \(Q_0\) 均全局红移到 cusp”的定理则尚未证明。核心运行只验证到 \(Q_0=100\)。

### 总判定

没有发现会改变 Step 90 机制或结论的系数/符号错误。需要修正或强化的表述是：

* `by linearity` 应改为非线性标量射击；
* 核心 \(rr\) 小残差应归因于精确约束传播及截断中心数据；
* taper 的 \(O(\delta^2)\) 残差由
  \[
  C'=-2(u+H)C-wb
  \]
  强制产生；
* 混合块精确为 \(|b|/2\)，径向模型内可完成 operator-norm 换算；
* 当前端点仅有限阶正则，且终端仍有非零 \(rr\) 缺陷；
* 数值结果支持采样范围和渐近机制，不能升级为全 \(Q_0\) 的全局存在定理或两端自由 \(T^2\) 模型的构造。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 9,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step9_ttcs01_sub5_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step9_ttcs01_sub6_verifier.md"
    }
  ]
}
```

## Exact Task

Analyze the exact relative calibration and transgression results from peer Session S1003A01 together with the perpendicular cell profile and the active Einstein-gap goal. Explain whether the decomposition P/(8π²)-1 = three nonnegative squares + ∫2u1u2u3/λ2 can plausibly yield a general lower bound in the perpendicular SU(2)-invariant sector, what matrix Hardy/Riccati inequality would be needed, and how the first-order cancellation R^+ζ=0 enters. Compare its mathematical value to brute-force Hessian computations. Identify a concrete inequality or transformed variable that could control the cubic term by the endpoint data and squares without losing an O(x0) term.

## Integrated Scientific Memo

# 核验结论：相对校准把问题精确化，但尚未证明一般下界

## 1. 已被材料可靠支持的核心事实

在 bolt-adapted 循环坐标
\[
(a,b,c)=(\sqrt x,\sqrt{xe^w},\sqrt F),\qquad dt=\frac{dx}{2\sqrt G},
\]
令
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad
H_i=u_i+\frac12u_ju_k,\qquad
\lambda_i=\frac{a_ja_k}{a_i}.
\]
端点数据为
\[
u_{\rm bolt}=(0,0,-1),\qquad u_{\rm CH}=(0,3X,0),
\]
而 Chern–Simons 电荷为
\[
C(u)=u_1^2+u_2^2+u_3^2+u_1u_2u_3.
\]
相对校准
\[
\Phi=C-u_2^2=u_1^2+u_3^2+u_1u_2u_3,\qquad
\Phi_{\rm bolt}=1,\quad \Phi_{\rm CH}=0
\]
给出精确恒等式
\[
\boxed{
\frac{P}{8\pi^2}-1
=
\int\left[
\frac{\lambda_1}{4}E_1^2+
\frac{\lambda_2}{4}E_2^2+
\frac{\lambda_3}{4}E_3^2+
\frac{2u_1u_2u_3}{\lambda_2}
\right]dt
}
\]
其中
\[
E_1=\dot u_1+\frac{2u_1+u_2u_3}{\lambda_1},\quad
E_2=\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2},\quad
E_3=\dot u_3+\frac{2u_3+u_1u_2}{\lambda_3}.
\]

因此 \(P\ge 8\pi^2\) 恰好等价于
\[
\int\sum_i\frac{\lambda_i}{4}E_i^2dt
\ge
2\int\frac{(-u_1u_2u_3)_+}{\lambda_2}\,dt.
\]
这不是逐点符号问题，也不能把 cubic 当成低阶小误差：在 \(x_0=.01\) 的近极值剖面中
\[
S_1+S_2+S_3=0.003428047,\qquad C_{\rm cub}=-0.00143166,
\]
负 cubic 抵消约 \(42\%\) 的平方和。

给出的 \(x_0=.03\) 剖面也与该坐标和端点分析一致：

- bolt 处 \(G=F=0,\ h_{22}=h_{33}=x_0\)，且
  \[
  G'(x_0)F'(x_0)\approx1;
  \]
- \(h_{33}-x=O((x-x_0)^2)\)，符合 smooth `wpow=2`；
- \(x=1\) 处一、二阶数据与 CH 数据吻合。

故旧坐标下“\(Y\) 在 perpendicular bolt 奇异”的说法只是坐标伪象；但 aligned 情形的零 flux 中值机制确实不再适用。这里发生的是从 \(u_3\)-轴到 \(u_2\)-轴的异宿电荷输运。

---

## 2. 它能否给出整个 perpendicular SU(2)-invariant 扇区的一般下界？

**有合理可能，但现有材料没有证明，而且存在一个必须优先排除的 neck resonance。**

相对校准的优势是：阈值 \(8\pi^2\) 已由端点 transgression 精确编码，剩余问题完全是一个二维横向 Hardy/Sturm 问题。设
\[
\eta=\binom{u_1}{u_3},\qquad
A=\frac14
\begin{pmatrix}\lambda_1&0\\0&\lambda_3\end{pmatrix},
\]
\[
K=
\begin{pmatrix}
2/\lambda_1&u_2/\lambda_1\\
u_2/\lambda_3&2/\lambda_3
\end{pmatrix},
\qquad
N=\frac{u_2}{\lambda_2}
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
则第一、第三平方和 cubic 正好是
\[
\boxed{
\mathcal Q_\perp[\eta]
=
\int\left[
(\dot\eta+K\eta)^TA(\dot\eta+K\eta)
+\eta^TN\eta
\right]dt,
}
\]
并且
\[
\frac{P}{8\pi^2}-1
=
\mathcal Q_\perp[\eta]
+\int\frac{\lambda_2}{4}E_2^2dt.
\]

因此一个足够强的定理是
\[
\mathcal Q_\perp[\eta]\ge0,
\]
而真正精确所需的较弱形式是
\[
\mathcal Q_\perp[\eta]\ge
-\int\frac{\lambda_2}{4}E_2^2dt.
\]

不过，第二分支指出了一个实质性风险。记
\[
W=u_2u_3.
\]
在 Burns/CH neck 的形式近似中，
\[
u_2\sim3x,\qquad u_3\sim-\frac{x_0}{x},
\qquad W\sim-3x_0,
\]
即 growing CH mode 与 decaying Burns mode 的乘积在对数 neck 上近似常数。若允许 \(u_1\) 沿整个 neck 响应，这可能积累
\[
x_0^2\log(1/x_0)
\]
级相互作用。该机制与现有正的数值上界不矛盾，因为全局 \(x\)-多项式基底可能难以表示 log-uniform plateau；但它目前也没有被构造成满足全部 bolt/collar 光滑条件的严格次阈值度量。

所以合理判断是：

- 校准分解确实提供了证明一般下界的最佳结构框架；
- 但不能仅凭 CH 上的齐次 Sturm 正性断言全局下界；
- 必须控制由 bolt 固定的非齐次 Burns tail 与 \(u_1\) 响应的 Schur complement；
- 若该 Schur complement 为负并产生 \(-c x_0^2\log(1/x_0)\)，则一般阈值 \(P\ge8\pi^2\) 反而失败；
- 当前源材料只支持“所有已算剖面均在阈值之上”，不支持任一方向的最终结论。

---

## 3. 所需的矩阵 Hardy/Riccati 不等式

若存在对称矩阵 \(\Gamma(t)\)，满足
\[
\boxed{
N-\dot\Gamma+K^T\Gamma+\Gamma K-\Gamma A^{-1}\Gamma\succeq0,
}
\]
则
\[
\begin{aligned}
\mathcal Q_\perp[\eta]
={}&
\int
(\dot\eta+K\eta-A^{-1}\Gamma\eta)^T
A(\dot\eta+K\eta-A^{-1}\Gamma\eta)\,dt\\
&+\int\eta^T
\bigl(N-\dot\Gamma+K^T\Gamma+\Gamma K-\Gamma A^{-1}\Gamma\bigr)
\eta\,dt\\
&+\bigl[\eta^T\Gamma\eta\bigr]_{\rm bolt}^{\rm collar}.
\end{aligned}
\]
由于 CH 端 \(\eta=0\)，bolt 端 \(\eta=(0,-1)\)，边界项为
\[
-\Gamma_{33}({\rm bolt}).
\]
故条件
\[
\Gamma_{33}({\rm bolt})\le0
\]
连同 Riccati 矩阵不等式足以推出 \(\mathcal Q_\perp\ge0\)。bolt 处 \(A\) 退化，因此应使用光滑 bolt 展开取极限；剖面中的 \(G'F'=1\) 与 \(w=O((x-x_0)^2)\) 正是相应正则数据。

展开成 Sturm 型，令
\[
B=AK=\frac14
\begin{pmatrix}2&u_2\\u_2&2\end{pmatrix},
\]
则
\[
\mathcal Q_\perp
=
[\eta^TB\eta]_{\rm bolt}^{\rm collar}
+\int\bigl(\dot\eta^TA\dot\eta+\eta^TV\eta\bigr)dt,
\]
其中
\[
V=K^TAK-\dot B+N.
\]
若 \(R=\Gamma-B\)，Riccati 条件化为
\[
\boxed{V-\dot R-RA^{-1}R\succeq0.}
\]
等价地，需要一个始终可逆、无共轭点的矩阵 Jacobi 场 \(Y\)：
\[
-(A\dot Y)^{\cdot}+VY=0,\qquad
R=A\dot YY^{-1},
\]
并控制其 bolt-to-collar Dirichlet-to-Neumann 边界型。

**关键修正：**仅证明齐次 \(\mathcal Q_\pm\) 正定未必够。一般下界需要把 bolt 强制的 Burns tail 纳入矩阵系统，或者加入线性 Riccati/Hamilton–Jacobi 项。否则会漏掉 \(W=u_2u_3\) 所产生的非齐次源。

---

## 4. CH 段上可精确控制 cubic 的变量

在精确 CH 段，\(\lambda_1=\lambda_3\)、\(u_2=3x\)。令
\[
v_\pm=u_1\pm u_3.
\]
横向型对角化为
\[
\mathcal Q_\pm[v]
=\int\left[p(x)(v')^2+V_\pm(x)v^2\right]dx,
\qquad p(x)=\frac{x(1+x)}4,
\]
\[
V_+=\frac{4+18x+15x^2}{16x(1+x)},\qquad
V_-=\frac{4-18x+3x^2}{16x(1+x)}.
\]
\(V_-\) 会变号，所以点态势能正性不成立。但两个方程有显式正解
\[
y_+=x(1+x)^{1/2},\qquad
y_-=x(1+x)^{-5/2},
\]
满足
\[
-(py_\pm')'+V_\pm y_\pm=0.
\]
于是 ground-state transform 给出
\[
\mathcal Q_\pm[v]
=
\int p\,y_\pm^2
\left(\frac{v}{y_\pm}\right)'^{\!2}dx
+
\left[p\frac{y_\pm'}{y_\pm}v^2\right]_{\rm in}^{\rm out}.
\]

特别是定义
\[
\boxed{
z_+=\frac{u_1+u_3}{x\sqrt{1+x}},\qquad
z_-=\frac{(1+x)^{5/2}}{x}(u_1-u_3),
}
\]
便有
\[
\boxed{
\mathcal Q_+
=
\int\frac{x^3(1+x)^2}{4}(z_+')^2dx
+
\left[\frac{2+3x}{8}v_+^2\right]_{\rm in}^{\rm out},
}
\]
\[
\boxed{
\mathcal Q_-
=
\int\frac{x^3}{4(1+x)^4}(z_-')^2dx
+
\left[\frac{2-3x}{8}v_-^2\right]_{\rm in}^{\rm out}.
}
\]
这是目前最明确的“不丢失 \(O(x_0)\) 信息”的变量变换：变号势——包括 cubic 的横向效应——被精确写成平方和边界通量，而不是用
\[
|u_1u_3|\le \tfrac12(u_1^2+u_3^2)
\]
之类 Young 估计粗暴吸收。

若精确 CH 段始于 \(x=a\)，外端 \(v_\pm=0\)，则需要内区能量满足具体迹比较
\[
\boxed{
\mathcal E_{\rm inner}(a)
\ge
\frac{2+3a}{8}v_+^2(a)
+
\frac{2-3a}{8}v_-^2(a),
}
\]
其中必须保留 \(E_2\) 平方。它就是内区 Dirichlet-to-Neumann 型支配 CH Riccati 边界型的标量化版本。

但需强调：该 CH 因子化只处理齐次外段；全局证明仍须把 Burns tail 的非齐次 forcing 纳入内区迹型，不能直接由上式推出一般阈值。

---

## 5. 一个应立即核验的精确再完平方

第二分支提出的最有价值异议是对 channel 1 再完平方。以
\[
W=u_2u_3
\]
记，形式上可将 cubic 与第一平方重组为一个平移后的平方，并暴露一个负的 \(W^2\) 项。自然的 transformed residual 是
\[
\boxed{
\widetilde E_1
=
\dot u_1+\frac{2H_1}{\lambda_1}
+\frac{2u_2u_3}{\lambda_2}.
}
\]
相应候选恒等式为
\[
\begin{aligned}
\frac{P}{8\pi^2}-1
={}&
\int\left[
\frac{\lambda_1}{4}\widetilde E_1^2+
\frac{\lambda_2}{4}E_2^2+
\frac{\lambda_3}{4}E_3^2
\right]dt\\
&-\int
W^2\frac{\lambda_1+\lambda_2}{\lambda_2^2}\,dt
+\int u_1\,d\!\left(\frac{\lambda_1W}{\lambda_2}\right),
\end{aligned}
\]
端点项因 \(u_1=0\) 消失。

这正是具体回答“如何不损失 \(O(x_0)\) 地控制 cubic”：不是用绝对值估计，而是把它精确转化为

1. 一个平移平方；
2. 一个显式负 \(W^2\) 项；
3. 一个仅在 \(W\) 变化区贡献的 transport 项。

然而该式并未在源文件中得到符号验证，因此在据此宣布 \(-9x_0^2\log(1/x_0)\) 前必须逐项代数核验。即便恒等式正确，仍需证明：

- \((u_1,u_2,u_3)\) 的候选 neck 响应来自真实正定 Bianchi-IX 度量；
- 满足 smooth bolt 与 CH collar 条件；
- 切换区成本确为 \(O(x_0^2)\) 而非抵消 logarithmic gain；
- \(E_2,E_3\) 与 \(\lambda_i\) 修正不恢复正的同阶项。

因此“阈值已被小 \(x_0\) competitor 推翻”的结论超出当前证据。它应被视为对矩阵 Hardy 猜想的明确反例候选，而非结果。

另一个精确警示是
\[
u_1u_3=2u_2-\lambda_2\dot u_2+\lambda_2E_2,
\]
从而
\[
\frac{\lambda_2}{4}E_2^2+\frac{2u_1u_2u_3}{\lambda_2}
=
\frac{\lambda_2}{4}
\left(\dot u_2+\frac{2u_2+u_1u_3}{\lambda_2}\right)^2
-\frac d{dt}(u_2^2).
\]
单独重组 \(E_2\) 与 cubic 会重新产生 outgoing CH 电荷
\[
-[u_2^2]_{\rm bolt}^{\rm CH}=-9X^2,
\]
因此不能替代相对校准 \(C-u_2^2\)。

---

## 6. \(R^+\zeta=0\) 如何进入

Step 8 的一阶律是
\[
\frac{P}{8\pi^2}
=
1-x_0R^+(\zeta,\zeta)+O(x_0^2),
\]
而 CH 上
\[
R^+=W^++\frac{s}{12}
=\operatorname{diag}(-6,0,0)
\]
于 \((\omega_{\rm CH},\omega_2,\omega_3)\) 基底中。故
\[
-x_0R^+(\zeta,\zeta)=6x_0\cos^2\theta.
\]
perpendicular 情形 \(\zeta\perp\omega_{\rm CH}\) 正好满足
\[
R^+\zeta=0,
\]
所以不存在统一正的 \(c x_0\) 余量：
\[
\frac{P}{8\pi^2}-1=O(x_0^2)
\]
或可能为 \(O(x_0^2\log(1/x_0))\)。

在 Sturm/Riccati 语言中，这意味着横向最低通道是**临界通道**：内区和 CH 的 Dirichlet-to-Neumann 型在一阶必须精确匹配。显式正 Jacobi 解
\[
y_-(x)=\frac{x}{(1+x)^{5/2}},
\qquad
\frac{y_-'}{y_-}
=\frac{2-3x}{2x(1+x)}
\]
就是该临界通道的外段权函数。

因此：

- \(R^+\zeta=0\) 不是 cubic 偶然较小；
- 它是 Einstein 脱奇第一障碍与 cell 一阶代价的同一张量条件；
- 任何一般 lower bound 都必须允许 perpendicular 通道在 \(O(x_0)\) 阶取等；
- 真正决定阈值的是二阶 Schur complement，而不是一阶 Hessian 系数。

---

## 7. 与 brute-force Hessian 的数学价值比较

相对校准远比单纯 Hessian 更接近定理：

1. **全振幅且参数化无关。**  
   它对整个 fixed-slot 对角 Bianchi-IX 路径成立，不仅是某有限维多项式族附近的二次展开。

2. **保留拓扑阈值。**  
   \(8\pi^2\) 直接来自 bolt/collar 的相对 transgression，而非数值拟合。

3. **暴露唯一 signed interaction。**  
   所有困难都集中到 \(u_1u_2u_3\)，因此可精确识别需要的矩阵 Sturm、Riccati 或 Dirichlet-to-Neumann 比较。

4. **能识别 ansatz 伪效应。**  
   旧 diabatic Hessian 强制 \(h_{13}=\phi(F-x)=0\) 于特征值交叉点，制造了虚假的 \(O(x_0)\) misalignment cost；fixed-slot 模型恢复了 \(R^+\zeta=0\)。

5. **Hessian 仍有辅助价值。**  
   正确 fixed-slot 类中的 Hessian 可近似最低谱值、寻找共轭点、生成 Riccati 初值并测量二阶系数；但它不能证明全局 nonlinear lower bound，也容易漏掉 log-uniform neck 模式。

---

## 8. 精确未决对象

当前最关键的数学对象不是另一个 brute-force Hessian，而是以下二者之一：

1. **正向证书：**构造满足 bolt 正则渐近、穿过整个 transition 且无 Riccati 极点的 \(2\times2\) 矩阵 \(\Gamma\)，并证明
   \[
   N-\dot\Gamma+K^T\Gamma+\Gamma K-\Gamma A^{-1}\Gamma\succeq0,
   \qquad
   \Gamma_{33}({\rm bolt})\le0;
   \]
   或证明相应内区 Dirichlet-to-Neumann 型支配 CH 边界型。

2. **反例方向：**严格核验 \(\widetilde E_1\) 再完平方，并构造 smooth bolt-to-CH cutoff，使
   \[
   W=u_2u_3\sim-3x_0,\qquad
   u_1\ \text{接近平移平方的最优响应}
   \]
   在长对数 neck 上成立，同时全部切换成本仅为 \(O(x_0^2)\)。这将决定是否真的出现
   \[
   -c\,x_0^2\log(1/x_0)
   \]
   的次阈值项。

现有数据在 \(x_0=.001,.003,.01,.03\) 均给正 excess，约为 \(10\!-\!20\,x_0^2\)，但既不能区分 \(cx_0^2\) 与带 logarithmic 修正的律，也不能排除未被全局多项式基底解析的 neck 响应。故最稳健结论是：**相对校准极有数学价值，并把一般下界压缩成临界矩阵 Hardy/Riccati 问题；但它尚未证明该下界，而且 \(W=u_2u_3\) 的 resonant Schur complement 是必须先解决的具体障碍。**
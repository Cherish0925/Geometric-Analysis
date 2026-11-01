# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 67,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step67_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step67_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the new Step 67 local curved-neck result in full mathematical detail. Check sign conventions, Koiso/Theorem 2.1 hypotheses, existence of an analytic constant-scalar-curvature -6 metric on T^3, the W=0 constraint for a four-dimensional Ric=-3g extension, the formula for g''(0), time-reflection symmetry, and H'(0)=3 under the opposite S convention. Identify any hidden issue that would invalidate the conclusion that an exact local negative-Einstein germ reverses mean curvature through a curved totally geodesic T^3. Also distinguish exactly what this refutes and what remains global. Ground every conclusion in the supplied source and note; do not assume a global extension.

## Integrated Scientific Memo

# Step 67 核验结论

## 结论

Step 67 的核心局部结论成立：

> 存在 \(T^3\) 上的解析度量 \(g_0\)，满足
> \(\operatorname{Scal}_{g_0}=-6\)，并存在某个 \(\varepsilon>0\) 及解析 Einstein 度量
> \[
> g^Z=dt^2+g_t\quad\text{on }(-\varepsilon,\varepsilon)\times T^3,
> \qquad \operatorname{Ric}_{g^Z}=-3g^Z,
> \]
> 使中央截面完全测地；对约定
> \[
> S=-W=\tfrac12g_t^{-1}\dot g_t,\qquad H=\operatorname{tr}S,
> \]
> 有
> \[
> H(0)=0,\qquad H'(0)=3,
> \]
> 因而相对于固定法向 \(\nu=\partial_t\)，\(H\) 在 \(t=0\) 两侧异号。

没有发现会推翻此局部 germ 的隐藏问题。需要修正或限定的只有若干措辞：解析 Yamabe 方程是半线性的；“各向异性”只能断言为非恒等消失，而未证明逐点非零；“反转”必须固定法向和非归一化平均曲率约定。

---

## 1. 符号约定与 Einstein 方程

给定来源采用
\[
\nabla_X^Z\nu=-W_tX,\qquad
g_t(W_tX,Y)=-\frac12\dot g_t(X,Y),
\]
故
\[
W_t=-\frac12g_t^{-1}\dot g_t.
\]

来源 §2 的公式为
\[
\begin{aligned}
\operatorname{Ric}^Z(\nu,\nu)
 &=\operatorname{tr}(W_t^2)-\frac12\operatorname{tr}_{g_t}\ddot g_t,\\
\operatorname{Ric}^Z(\nu,X)
 &=d\operatorname{tr}W_t(X)+\delta^{g_t}W_t(X),\\
\operatorname{Ric}^Z(X,Y)
 &=\operatorname{Ric}^{g_t}(X,Y)+2g_t(W_tX,W_tY)\\
 &\quad+\frac12\operatorname{tr}(W_t)\dot g_t(X,Y)
 -\frac12\ddot g_t(X,Y).
\end{aligned}
\]
Step 67 与之完全一致。

若截面维数为 \(n\)，且
\[
\operatorname{Ric}^Z=\lambda g^Z,
\]
则约束为
\[
d\operatorname{tr}W+\delta W=0,
\]
以及
\[
\operatorname{Scal}^{g_0}
+\operatorname{tr}(W^2)-(\operatorname{tr}W)^2=(n-1)\lambda.
\tag{1}
\]
这里 \(n=3,\lambda=-3,W_0=0\)，故第一约束自动成立，而第二约束恰为
\[
\operatorname{Scal}_{g_0}=2(-3)=-6.
\tag{2}
\]

切向演化方程也是来源 (2.11)：
\[
\ddot g_t
=2\operatorname{Ric}^{g_t}
+\dot g_t(g_t^{-1}\dot g_t\,\cdot,\cdot)
-\operatorname{tr}(g_t^{-1}\dot g_t)\dot g_t
-2\lambda g_t.
\tag{3}
\]

---

## 2. \(T^3\) 上解析常标量曲率 \(-6\) 度量确实存在

可将 Step 67 的存在性论证完全具体化。令
\[
T^3=(\mathbb R/2\pi\mathbb Z)^3
\]
并取非常值解析周期函数 \(f(x)\)，定义
\[
\bar g=dx^2+e^{2f(x)}dy^2+e^{-2f(x)}dz^2.
\]
对双扭曲积 \(dx^2+A^2dy^2+B^2dz^2\)，
\[
K_{xy}=-\frac{A''}{A},\quad
K_{xz}=-\frac{B''}{B},\quad
K_{yz}=-\frac{A'B'}{AB}.
\]
代入 \(A=e^f,B=e^{-f}\)，得到
\[
\operatorname{Scal}_{\bar g}=-2(f')^2.
\]
而 \(dv_{\bar g}=dx\,dy\,dz\)，故
\[
\int_{T^3}\operatorname{Scal}_{\bar g}\,dv_{\bar g}<0.
\]
以常函数测试 Yamabe 商，得
\[
Y(T^3,[\bar g])<0.
\]

Yamabe 定理给出
\[
\widehat g=u^4\bar g,\qquad
\operatorname{Scal}_{\widehat g}=Y<0.
\]
函数 \(u>0\) 满足
\[
-8\Delta_{\bar g}u+\operatorname{Scal}_{\bar g}u=Yu^5.
\tag{4}
\]
这是解析系数的**半线性**椭圆方程，不是来源 Corollary 2.3 证明中所称的“线性方程”；但解析椭圆正则性仍推出 \(u\) 解析，因此 \(\widehat g\) 解析。

最后令
\[
g_0=\frac{-Y}{6}\widehat g.
\]
常数缩放下标量曲率按比例倒数变化，所以
\[
\operatorname{Scal}_{g_0}=-6.
\]
因此 Koiso 所需的解析初值真实存在。\(T^3\) 的整体 Yamabe invariant 为零并不排除某个具体共形类具有负 Yamabe 常数。

---

## 3. Koiso/Theorem 2.1 的全部假设均满足

来源 Theorem 2.1 要求：

1. \(M\) 为解析流形；
2. \(g_0\) 为解析 Riemann 度量；
3. \(W_0\) 为解析、对称的自同态场；
4. 满足两个约束 (1)。

这里 \(M=T^3\)，上述 \(g_0\) 解析，\(W_0=0\) 解析且对称；约束由 (2) 成立。因此定理给出唯一解析 Einstein germ
\[
g^Z=dt^2+g_t,\qquad \operatorname{Ric}_{g^Z}=-3g^Z,
\]
满足
\[
g_{t=0}=g_0,\qquad \dot g_0=-2g_0(W_0\cdot,\cdot)=0.
\tag{5}
\]
因此中央 \(T^3\) 完全测地。

由于 \(T^3\) 紧致，局部 Cauchy–Kowalevskaya 解可拼接，并在缩小半径后取统一 \(\varepsilon>0\)，从而得到整个
\[
(-\varepsilon,\varepsilon)\times T^3
\]
上的双侧 collar，而不只是逐点坐标 germ。正定性由 \(g_t\) 对 \(t\) 的连续性保持。

来源 Corollary 2.2 也直接给出同一结论：其脐形参数满足
\[
\alpha^2=\frac{-6}{3\cdot2}-\frac{-3}{3}=0.
\]

---

## 4. \(\ddot g_0\) 的公式及一致性检查

由 (3)、\(\lambda=-3\) 和 \(\dot g_0=0\)，
\[
\boxed{\ddot g_0=2\operatorname{Ric}_{g_0}+6g_0.}
\tag{6}
\]
取迹：
\[
\operatorname{tr}_{g_0}\ddot g_0
=2\operatorname{Scal}_{g_0}+18
=-12+18=6.
\tag{7}
\]
所以 \(\ddot g_0\neq0\)，germ 确实随 \(t\) 非平凡变化。

写成迹与无迹分解：
\[
\operatorname{Ric}_{g_0}
=\operatorname{Ric}_{g_0}^{\circ}-2g_0,
\]
则
\[
\ddot g_0=2g_0+2\operatorname{Ric}_{g_0}^{\circ},
\qquad
(\ddot g_0)^\circ=2\operatorname{Ric}_{g_0}^\circ.
\tag{8}
\]
若 \(\operatorname{Ric}_{g_0}^\circ\equiv0\)，则
\[
\operatorname{Ric}_{g_0}=-2g_0.
\]
三维 Einstein 度量具有常截面曲率 \(-1\)，这与
\(\pi_1(T^3)=\mathbb Z^3\) 和 Preissmann 定理矛盾。因此无迹部分不可能**恒等**为零。

这里必须精确限定 Step 67 的“anisotropic”：已证明其无迹部分不是全局恒零，但没有证明它在每一点均非零。局部反转不需要后一更强命题。

所有 Einstein 分量在 \(t=0\) 也一致：
\[
\operatorname{Ric}^Z(\nu,\nu)
=-\frac12\operatorname{tr}\ddot g_0=-3,
\]
混合分量因 \(W_0=0\) 为零，而
\[
\operatorname{Ric}^Z(X,Y)
=\operatorname{Ric}_{g_0}(X,Y)-\frac12\ddot g_0(X,Y)
=-3g_0(X,Y).
\]
这明确展示了此前 slice-only 推理遗漏的机制：
\(\ddot g_0\) 的无迹部分精确抵消截面的内禀无迹 Ricci。

---

## 5. 时间反射对称性

定义
\[
\widetilde g_t=g_{-t}.
\]
则 \(dt^2+\widetilde g_t\) 是 \(dt^2+g_t\) 在
\((t,x)\mapsto(-t,x)\) 下的拉回，仍满足
\(\operatorname{Ric}=-3g\)。又有
\[
\widetilde g_0=g_0,\qquad
\dot{\widetilde g}_0=-\dot g_0=0.
\]
它与原解具有相同 Koiso 初值。由 Theorem 2.1 的解析唯一性，
\[
\boxed{g_t=g_{-t}.}
\tag{9}
\]
故 \(g_t\) 为偶函数，\(\dot g_t\) 为奇函数，并且
\[
g_t=g_0+\bigl(\operatorname{Ric}_{g_0}+3g_0\bigr)t^2+O(t^4).
\]

---

## 6. 相反 \(S\) 约定下 \(H'(0)=3\)

令
\[
S=-W=\frac12g_t^{-1}\dot g_t,\qquad
H=\operatorname{tr}S
=\frac12\operatorname{tr}(g_t^{-1}\dot g_t).
\tag{10}
\]
这里 \(H\) 是未除以 \(3\) 的迹平均曲率。微分得
\[
H'
=\frac12\operatorname{tr}_{g_t}\ddot g_t
-\frac12\operatorname{tr}\bigl((g_t^{-1}\dot g_t)^2\bigr).
\]
由于 \(g_t^{-1}\dot g_t=2S\)，
\[
H'=\frac12\operatorname{tr}_{g_t}\ddot g_t-2|S|^2.
\]
另一方面
\[
\operatorname{Ric}^Z(\nu,\nu)
=|S|^2-\frac12\operatorname{tr}_{g_t}\ddot g_t,
\]
故
\[
\boxed{H'=-\operatorname{Ric}^Z(\nu,\nu)-|S|^2.}
\tag{11}
\]
在 \(\operatorname{Ric}^Z=-3g^Z\) 下，
\[
H'=3-|S|^2.
\]
中央截面 \(S_0=0\)，因此
\[
\boxed{H(0)=0,\qquad H'(0)=3.}
\tag{12}
\]
也可由 (7) 直接核验：
\[
H'(0)=\frac12\operatorname{tr}_{g_0}\ddot g_0=3.
\]

由时间对称性 \(H\) 为奇函数，故
\[
H(t)=3t+O(t^3),
\]
从而相对于固定连续法向 \(\nu=\partial_t\)，
\[
H(t)<0\quad(t<0),\qquad H(t)>0\quad(t>0)
\]
在足够靠近零处成立。

约定注意事项：

- 若采用归一化平均曲率 \(\bar H=\frac13\operatorname{tr}S\)，则
  \(\bar H'(0)=1\)；
- 若采用 \(\operatorname{tr}W\)，其导数为 \(-3\)；
- 若在 collar 两端分别采用向外法向，则左端法向为
  \(-\partial_t\)，端点符号不能直接与固定 \(\partial_t\) 下的符号比较。

这些只是约定变化，不影响固定法向下确有符号反转。

---

## 7. 该结果精确否定什么

这个例子同时具有：

- 中央截面拓扑为 \(T^3\)；
- \(S_0=0\)，故完全测地；
- \(S\) 自伴；
- \(\operatorname{Scal}_{g_0}=-6\)；
- ambient Einstein defect 精确为零；
- \(H\) 穿过零并变号。

因此它否定任何仅依赖下列局部信息的普遍“禁止反转”命题：

1. 截面是环面；
2. shape operator 自伴；
3. 只掌握截面标量曲率的符号或数值；
4. ambient metric 具有很小的 Einstein defect；
5. 试图把 Step 63 的平坦截面结论直接推广到任意曲截面。

它不反驳 Step 63 的有效平坦截面定理。该定理要求每个 \(T^3\) 截面内禀平坦；当前中央截面有
\[
\operatorname{Scal}_{g_0}=-6,
\]
故不平坦。其 Gauss 方程中的内禀曲率和法向二阶导数正是允许反转的补偿项。

---

## 8. 它没有解决的全局问题

Koiso 定理只提供 \(|t|<\varepsilon\) 上的解析 germ。它不提供：

- 任意长时间解析延拓；
- 完备性；
- 远端平坦 \(T^3\) 截面；
- 与双侧双曲 cusp 数据的度量及所需 jets 匹配；
- 匹配层中趋于零的 \(L^\infty\) Einstein defect；
- 紧致 graph-manifold 上的整体度量；
- extended graph manifold 上
  \(\|\operatorname{Ric}+3g\|_{\mathrm{op}}\to0\) 的度量序列。

时间反射只说明两个局部侧面相互镜像，不蕴含 cusp 渐近。

若 Step 63 所引用的 Di Cerbo 全局 Einstein 排除适用于目标紧致 extended graph manifold，则把此 germ 与精确 Einstein cusps **全局无缺陷地**拼成该闭流形是不可能的，否则会直接产生被排除的 Einstein 度量。真正未决的对象因此是：

\[
\inf\left\{
\|\operatorname{Ric}_g+3g\|_{L^\infty}:
g\text{ 实现所需双端匹配与拓扑拼接}
\right\}
\]
究竟为零还是有严格正下界。

最后，这个局部负 Einstein germ 本身既不证明也不证伪 Yau 第 26 题。即使负号 graph-manifold 匹配最终成功，也只处理负 Ricci 归一化附近；完整证伪还必须排除命题可选取的其他夹逼窗口，尤其正 Ricci 分支。
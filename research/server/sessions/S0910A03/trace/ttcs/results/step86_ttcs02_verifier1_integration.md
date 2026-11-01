# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 86,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step86_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step86_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the new coupled orbit-area energy derivation in Step 86, section 9. Use the conventions dmu=e^sigma dvol, L=Delta+grad sigma dot grad, E=Ric+3g, T=tr_orbit E, e=|dU|^2, X=|grad sigma|^2, W=e+cX, F=tau_sigma(U), V=<dU,F>. Check: (i) whether the forced area trace equation is exactly L sigma=6-T and the sign; (ii) the weighted scalar Bochner formula for X and the rewrite -<grad sigma,grad T>=-div_sigma(T grad sigma)+T(6-T); (iii) after adding orbit Bochner, whether 1/2 L W >= div_sigma(V-cT grad sigma)+W^2/[2(1+c)]-(3+delta)W-D_c(delta)+P with P>=0 and D_c=12c delta+4(c+1)delta^2 really follows under operator |E|<=delta; track every cross/stress/error coefficient and correct it if needed; (iv) the norm bound on J; (v) c=1/2 reaction root series; and (vi) the conditional Cheeger inequality from W<=B and L sigma>=6-2delta, including orientation/absolute-value and domain/boundary caveats. Then assess whether this combined W identity creates a plausible noncircular bootstrap to a length-independent pointwise ceiling, or whether an explicit coupled scalar model still defeats it. Give a direct mathematical memo, preserving the restricted free-OT scope.

## Integrated Scientific Memo

# Step 86 §9 核验备忘录

以下限于光滑、自由、正交可迁的 \(T^2\)-区域。记
\[
s=\nabla\sigma,\qquad A=U^*h_{\mathbb H^2},\qquad
e=\operatorname{tr}A,\qquad X=|s|^2,\qquad W=e+cX,
\]
且
\[
\operatorname{div}_\sigma Y=e^{-\sigma}\operatorname{div}(e^\sigma Y),
\qquad L=\operatorname{div}_\sigma\nabla .
\]

## 1. 面积迹方程及符号

轨道 Ricci 迹满足
\[
\operatorname{tr}_{G}\bigl(\operatorname{Ric}_g|_{T^2}\bigr)=-L\sigma .
\]
因为 \(T=\operatorname{tr}_{\rm orb}E\)、\(E=\operatorname{Ric}+3g\)，而二维轨道块中
\(\operatorname{tr}_{G}(3G)=6\)，故
\[
T=-L\sigma+6,
\qquad\boxed{L\sigma=6-T.}
\]
符号正确。圆 cusp 上 \(\sigma=2r\) 且
\(L=\partial_{rr}+3\partial_r+e^{-2r}\partial_{zz}\)，确有 \(L\sigma=6\)。

若 \(\|E^\sharp\|_{\mathrm{op}}\le\delta\)，则
\[
|T|\le2\delta .
\]

## 2. 标量加权 Bochner 公式

对 \(L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle\)，
\[
\frac12LX
=|\operatorname{Hess}\sigma|^2
+\langle s,\nabla L\sigma\rangle
+(\operatorname{Ric}_B-\operatorname{Hess}\sigma)(s,s).
\]
这里应使用无穷维漂移张量 \(\operatorname{Ric}_B-\operatorname{Hess}\sigma\)，而不是直接使用 \(\operatorname{Ric}_{f}^{4}\)。由
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=-3\gamma_B+\frac12d\sigma\otimes d\sigma+\frac12A+E_B
\]
及 \(L\sigma=6-T\)，得到
\[
\boxed{
\begin{aligned}
\frac12LX={}&|\operatorname{Hess}\sigma|^2-3X+\frac12X^2
+\frac12A(s,s)+E_B(s,s)\\
&-\langle s,\nabla T\rangle .
\end{aligned}}
\]
又
\[
\operatorname{div}_\sigma(T\nabla\sigma)
=\langle\nabla T,s\rangle+T L\sigma,
\]
所以
\[
\boxed{
-\langle s,\nabla T\rangle
=-\operatorname{div}_\sigma(T\nabla\sigma)+T(6-T).}
\]
Step 86 的公式、符号和系数均正确。

## 3. 联合恒等式与全部系数

轨道 Bochner 恒等式为
\[
\frac12Le
=|DdU|^2+\operatorname{div}_\sigma V-|F|^2
+\frac12e^2+\det A-3e+\frac12A(s,s)+E_B:A.
\]
与 \(c\) 倍标量公式相加，并令
\[
J=V-cT\nabla\sigma,
\]
可得精确恒等式
\[
\boxed{
\begin{aligned}
\frac12LW={}&\operatorname{div}_\sigma J
+\frac12e^2+\frac c2X^2-3W\\
&+|DdU|^2+c|\operatorname{Hess}\sigma|^2+\det A
+\frac{1+c}{2}A(s,s)\\
&+E_B:A+cE_B(s,s)-|F|^2+cT(6-T).
\end{aligned}}
\tag{1}
\]

因此：

* stress 项的准确系数是 \((1+c)/2\)；
* 没有遗漏 \(eX\) 项；
* \(A\succeq0\)，故 \(\det A\ge0\) 且 \(A(s,s)\ge0\)；
* 二次项有精确分解
  \[
  \frac12e^2+\frac c2X^2
  =
  \frac{W^2}{2(1+c)}
  +\frac{c}{2(1+c)}(e-X)^2.
  \]

可取
\[
\mathcal P=
|DdU|^2+c|\operatorname{Hess}\sigma|^2+\det A
+\frac{1+c}{2}A(s,s)
+\frac{c}{2(1+c)}(e-X)^2\ge0.
\]
缺陷收缩满足
\[
E_B:A+cE_B(s,s)\ge-\delta e-c\delta X=-\delta W.
\]
此外
\[
|F|\le2\delta,\qquad |T|\le2\delta,
\]
故
\[
-|F|^2+cT(6-T)
\ge-4\delta^2-c(12\delta+4\delta^2).
\]
于是 Step 86 的粗估计确实成立：
\[
\boxed{
\frac12LW\ge
\operatorname{div}_\sigma J
+\frac{W^2}{2(1+c)}
-(3+\delta)W-D_c(\delta)+\mathcal P,
}
\]
其中
\[
\boxed{D_c(\delta)=12c\delta+4(c+1)\delta^2.}
\]

还有一个可利用的梯度强制性：
\[
|DdU|^2+c|\operatorname{Hess}\sigma|^2
\ge\frac{|\nabla W|^2}{4W}\qquad(W>0).
\tag{2}
\]

### 更尖锐但非必需的垂直缺陷估计

若垂直缺陷特征值为 \(\lambda_1,\lambda_2\in[-\delta,\delta]\)，则在当前归一化下
\[
T=\lambda_1+\lambda_2,\qquad |F|=|\lambda_1-\lambda_2|,
\]
从而
\[
|T|+|F|\le2\delta.
\]
这给出
\[
-|F|^2+cT(6-T)
\ge-\max\{4\delta^2,\;12c\delta+4c\delta^2\}.
\]
因此原 \(D_c\) 正确但不是最优常数。

## 4. 联合流 \(J\) 的范数

直接有
\[
\begin{aligned}
|J|
&\le |F|\sqrt e+c|T|\sqrt X\\
&\le2\delta\sqrt e+2c\delta\sqrt X\\
&\le\boxed{2(1+\sqrt c)\delta\sqrt W}.
\end{aligned}
\]
Step 86 的估计正确。

利用 \(|T|+|F|\le2\delta\) 还可加强为
\[
\boxed{|J|\le2\delta\max\{1,\sqrt c\}\sqrt W.}
\]
特别地，\(c=\tfrac12\) 时原估计为
\((2+\sqrt2)\delta\sqrt W\)，加强后为 \(2\delta\sqrt W\)。

## 5. \(c=\tfrac12\) 的反应根

粗常数下，正根满足
\[
\frac{k_c^2}{2(1+c)}-(3+\delta)k_c-D_c=0,
\]
即
\[
k_c=(1+c)\left[(3+\delta)+
\sqrt{(3+\delta)^2+\frac{2D_c}{1+c}}\right].
\]
当 \(c=\tfrac12\) 时，
\[
D_{1/2}=6\delta+6\delta^2
\]
且
\[
\boxed{
k_{1/2}
=\frac32\left(3+\delta+\sqrt{9+14\delta+9\delta^2}\right)
=9+5\delta+\frac89\delta^2+O(\delta^3).}
\]
因此原展开完全正确。零缺陷根为 \(9\)，而反射中心仍有
\(\langle W\rangle\ge\langle e\rangle\ge12\)，留下大小 \(3\) 的平均间隙。

若使用尖锐垂直常数，在小 \(\delta\) 区间内根改善为
\[
k_{1/2}^{\rm vert}
=9+5\delta-\frac49\delta^2+O(\delta^3).
\]

## 6. 条件 Cheeger 不等式

假设某自由 OT 区域 \(\mathcal D\) 上 \(W\le B\)。则
\[
|\nabla\sigma|\le\sqrt{B/c},
\qquad L\sigma=6-T\ge6-2\delta .
\]
要获得正下界需 \(\delta<3\)。对光滑相对紧集
\(\Omega\Subset\mathcal D\)，取外法向 \(\nu\)，有
\[
\begin{aligned}
(6-2\delta)\mu(\Omega)
&\le\int_\Omega L\sigma\,d\mu\\
&=\int_{\partial\Omega}\langle\nabla\sigma,\nu\rangle e^\sigma\,dA\\
&\le\int_{\partial\Omega}
|\langle\nabla\sigma,\nu\rangle|e^\sigma\,dA\\
&\le\sqrt{B/c}\,P_\mu(\Omega).
\end{aligned}
\]
方向无误：有符号通量因等于 \(\int_\Omega L\sigma\,d\mu\) 而为正；绝对值只用于上界。因此对于紧支撑/Dirichlet Cheeger 常数，
\[
\boxed{h_{\mu,\mathcal D}\ge(6-2\delta)\sqrt{c/B}}
\]
并由 Cheeger 不等式
\[
\boxed{\lambda_1^{\rm Dir}(-L)
\ge\frac{c(6-2\delta)^2}{4B}.}
\]

边界限定必须明确：

* 这是 Dirichlet 或紧支撑谱底，不是 Neumann 谱底；后者含常函数，谱底为零。
* 在反射双倍域中，中心不再是边界。
* 在半 connector 上，中心面通常给 Neumann 条件，出口给 Dirichlet 条件。
* 若集合接触物理出口，该面必须计入加权周长及通量；否则公式遗漏边界项。
* 闭基底上不可能在 \(\delta<3\) 时处处有 \(L\sigma\ge6-2\delta>0\)，因为 \(\int L\sigma\,d\mu=0\)。

圆 cusp 上 \(W=4c\)、\(\delta=0\)，取 \(B=4c\) 正好给出
\[
\lambda_1\ge\frac94,
\]
与 §8 的精确长圆柱极限一致。

还有一个不依赖先验全局 \(B\) 的层集版本：若正则层集分支
\(\Omega_t\) 相对紧且不接触未控制出口，则其边界上 \(W=t\)，因而
\[
\boxed{
P_\mu(\Omega_t)\ge
(6-2\delta)\sqrt{\frac ct}\,\mu(\Omega_t).}
\tag{3}
\]

## 7. 是否形成非循环 pointwise bootstrap？

尚未形成闭合证明。全局 Cheeger 下界依赖先验 \(W\le B\)，而这正是所求结论；所得谱隙还按 \(B^{-1}\) 衰减，目前没有推出严格改进 \(B\mapsto B'<B\) 的估计。

不过联合恒等式确有两项新增结构：

1. 层集膨胀估计 (3)，无需全局 ceiling；
2. 梯度强制项 (2)。

写 \(W=y^2\) 时，
\[
\frac12L(y^2)=yLy+|\nabla y|^2,
\qquad
\frac{|\nabla W|^2}{4W}=|\nabla y|^2,
\]
梯度项恰可消去链式法则损失，而 \(|J|/y=O(\delta)\)。这比单独处理 \(e\) 的普通 Moser 路线更有希望，但尚不足以排除薄层。

事实上，粗标量系统仍允许局部高平台。以圆 cusp 背景
\[
\sigma=2r,\qquad X=4,\qquad T=0
\]
为例，可在厚度 \(\ell\) 的层内令 \(W=H\)，并选径向流
\(J=j(r)\partial_r\) 使
\[
\operatorname{div}_\sigma J
=-\left[\frac{H^2}{2(1+c)}-(3+\delta)H-D_c+\mathcal P_H\right].
\]
因高 \(H\) 时反应量为 \(O(H^2)\)，取
\[
\ell=O(\delta H^{-3/2})
\]
即可同时满足 \(|J|=O(\delta\sqrt H)\)。这类层的周长/体积比很大，故也不违反条件 Cheeger 估计。

该模型只实现 \((\sigma,W,J)\)，并未实现真实 \(U\)、\(A=U^*h\)、\(F=-2\widehat E_0\)、水平 Einstein 方程及平滑出口匹配；因此它不是 OT connector 反例。但它证明：**面积方程、粗 \(W\) 不等式、流幅度界和条件 Cheeger 估计本身仍不能推出长度无关的 pointwise ceiling。**

真正未决对象是：梯度强制性、层集膨胀、\(A\) 的可积性及完整水平约束共同作用后，是否排除上述 \(O(\delta H^{-3/2})\) 薄层；或者能否构造满足全部 OT 方程的匹配薄层。当前资料没有解决此点。

结论：§9 的微分恒等式、误差常数、\(J\) 范数、根展开及条件 Cheeger 估计均正确；它提供了有实质价值但仍循环的 bootstrap 结构，尚未建立长度无关的点态上界。所有结论严格限于自由、正交可迁 \(T^2\) 区域，不能外推至有 twist、奇异轨道或一般非对称度量。
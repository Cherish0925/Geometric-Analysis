# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 74,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step74_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step74_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following derivation for the linearized Einstein equations around the flat hyperbolic cusp g0 = dt^2 + e^{2t}(dz^2 + dx^2 + dy^2), perturbed by T^2-invariant diagonal modes a=t+alpha(t)cos(kz), b=t+beta(t)cos(kz), c=t+gamma(t)cos(kz):

1. The constraint E_{01}=0 linearizes to beta'+gamma'=0, so beta+gamma=const for each k!=0 mode.
2. E_{00}=0 gives h''+2h'=0 for h=alpha+beta+gamma.
3. The anisotropy psi=beta-gamma satisfies psi''+3psi'-k^2 e^{-2t}psi=0.
4. Under x=ke^{-t}, this becomes x^2 psi_xx + 4x psi_x - x^2 psi = 0, which via psi=x^{-3/2}z reduces to the modified Bessel equation with nu=3/2.
5. The I-branch psi ~ x^{-3/2}I_{3/2}(x) is bounded as t->infinity (x->0), while the K-branch grows as e^{3t}.

Check each step. Also verify: does this BVP structure (center Neumann + cusp boundedness) give a unique solution per Fourier mode? What happens at k=0 (zero mode)? Are there corrections needed for the constraint propagation? Does the E_{11} equation actually give the correct z-derivative terms?

## Integrated Scientific Memo

## 核验结论

令
\[
w=\beta+\gamma,\qquad \psi=\beta-\gamma,\qquad
h=\alpha+\beta+\gamma=\alpha+w,\qquad q=k^2e^{-2t}.
\]
所有扰动均乘 \(\cos(kz)\)；混合分量相应乘 \(\sin(kz)\)。

由给出的精确 Ricci 公式线性化，得到
\[
\delta E_{00}=-(h''+2h')\cos(kz),
\]
\[
\delta E_{0z}=k\,w'\sin(kz),
\]
以及归一化切向分量
\[
e^{-2t}\delta E_{zz}
=-\alpha''-3\alpha'-h'+qw,
\]
\[
e^{-2t}\delta E_{xx}
=-\beta''-3\beta'-h'+q\beta,
\]
\[
e^{-2t}\delta E_{yy}
=-\gamma''-3\gamma'-h'+q\gamma.
\]

因此原推导的第 1–3 步正确，第 4 步有链式法则符号错误，第 5 步及其 BVP 解释随之错误。

### 1. 混合约束

对 \(k\neq0\)，
\[
E_{0z}=0\iff w'=0,
\]
故
\[
w=W
\]
关于 \(t\) 为常数。注意它仍乘 \(\cos(kz)\)，并非空间常数。

### 2. \(E_{00}\) 方程

\[
E_{00}=0\iff h''+2h'=0,
\]
所以
\[
h=H+De^{-2t}.
\]

### 3. 各向异性方程

用 \(E_{xx}-E_{yy}=0\) 得
\[
\boxed{\psi''+3\psi'-k^2e^{-2t}\psi=0.}
\]

### 4. 正确的 Bessel 化

取
\[
x=ke^{-t},\qquad \partial_t=-x\partial_x.
\]
则
\[
\psi_t=-x\psi_x,\qquad
\psi_{tt}=x^2\psi_{xx}+x\psi_x.
\]
代入后应得
\[
\boxed{x^2\psi_{xx}-2x\psi_x-x^2\psi=0,}
\]
而不是 \(x^2\psi_{xx}+4x\psi_x-x^2\psi=0\)。

令
\[
\psi=x^{3/2}z
\]
才得到
\[
x^2z''+xz'-\left(x^2+\frac94\right)z=0.
\]
因此
\[
\boxed{
\psi=x^{3/2}\left(AI_{3/2}(x)+BK_{3/2}(x)\right).
}
\]

### 5. 正确的末端渐近

当 \(t\to+\infty\)、\(x\to0\) 时，
\[
x^{3/2}I_{3/2}(x)\sim Cx^3=Ck^3e^{-3t},
\]
而
\[
x^{3/2}K_{3/2}(x)\longrightarrow C'\neq0.
\]
所以：

- \(I\)-支按 \(e^{-3t}\) 衰减；
- \(K\)-支趋于常数；
- 两支都 bounded；
- 不存在所声称的 \(e^{3t}\) 增长解。

这也可由渐近方程
\[
\psi''+3\psi'=0
\]
直接看出，其解为常数和 \(e^{-3t}\)。

脚本中的
```python
x**(-1.5)*iv(1.5,x)
x**(-1.5)*kv(1.5,x)
```
不是实际各向异性 ODE 的解；应改为
```python
x**(1.5)*iv(1.5,x)
x**(1.5)*kv(1.5,x)
```
因此 `step74_linearized_modes.json` 中所谓 \(e^{3t}\) 增长和 transmission 数值均不能用于验证正确方程。脚本中的 ODE
```python
ddp = -3*dp + k**2*np.exp(-2*t)*p
```
本身与
\[
\psi''+3\psi'-k^2e^{-2t}\psi=0
\]
是一致的；错误在闭式分支及其初值和解释，不在该 ODE 行。

---

## \(E_{zz}\) 的 \(z\)-导数项

精确归一化 \(zz\) 分量中的空间项为
\[
e^{-2a}\left(
a_zb_z+a_zc_z-b_z^2-b_{zz}-c_z^2-c_{zz}
\right).
\]
所有一阶导数乘积都是扰动的二阶项。线性阶仅剩
\[
-e^{-2t}(b_{zz}+c_{zz})
=k^2e^{-2t}(\beta+\gamma)\cos(kz).
\]
故脚本中 \(q(\beta+\gamma)\) 项正确；线性阶没有 \(\alpha_{zz}\) 项。

不过 \(E_{zz}=0\) 还给出遗漏的标量关系。由 \(w=W\) 和
\[
h=H+De^{-2t},\qquad \alpha=h-W,
\]
代入 \(E_{zz}=0\)，得到
\[
\boxed{4D+k^2W=0.}
\]
等价地，
\[
\boxed{h'=\frac12k^2We^{-2t}.}
\]
因此步骤 1–3 不是完整线性 Einstein 系统；还必须保留此迹/和模式耦合关系。

---

## 中心 Neumann 加 cusp boundedness 不唯一

对 \(k>0\)，两个基本解在 \(t\to\infty\) 都有界。因此：

\[
\psi'(0)=0
\quad+\quad
\psi\ \text{bounded at infinity}
\]
只施加一个有效线性条件，留下一个一维齐次解空间，不能给出唯一性。

若进一步规定渐近值
\[
\lim_{t\to\infty}\psi=L,
\]
则常数型 \(K\)-支系数由 \(L\) 决定，Neumann 条件再确定 \(I\)-支系数，因而唯一。

特别地，若真正的 cusp 条件是非零 Fourier 模式消失，
\[
\psi(t)\to0,
\]
则 \(B=0\)。但纯 \(I\)-支满足
\[
\frac d{dt}\!\left[x^{3/2}I_{3/2}(x)\right]
=-\sqrt{\frac2\pi}\,x^2\sinh x\neq0
\]
于任何有限 \(x=k>0\)，所以再加 \(\psi'(0)=0\) 会迫使 \(A=0\)。齐次 BVP 只有零解；对应的适当非齐次问题才有唯一性。

有限区间上，中心 Neumann 加外端 Dirichlet 条件也唯一。可将方程写成
\[
(e^{3t}\psi')'-k^2e^t\psi=0
\]
并作能量积分证明齐次核为零。

此外，\(g_0\) 的 \(t=\mathrm{const}\) 切片形算子为 \(S=I\)，不是反射中心所需的 \(S=0\)。因此“中心 Neumann”只能作为某些差值变量的形式边界条件；完整反射中心不能被视为 \(g_0\) 附近的小扰动。

---

## \(k=0\) 模式

当 \(k=0\) 时，\(E_{0z}\) 恒等为零，不能推出 \(w'=0\)。完整零模系统的解为
\[
\alpha=A_\alpha+B_\alpha e^{-3t},\qquad
\beta=A_\beta+B_\beta e^{-3t},\qquad
\gamma=A_\gamma+B_\gamma e^{-3t},
\]
并满足
\[
B_\alpha+B_\beta+B_\gamma=0.
\]
特别地，
\[
\psi=C+De^{-3t}.
\]
Neumann 条件给出 \(D=0\)，但常数各向异性 \(C\) 保留；它是平坦 \(T^3\) 横截面的形状模量。若对三个函数都施加 Neumann，则所有 \(B_i=0\)，三个常数 \(A_i\) 仍保留。因此零模绝不由 boundedness 消除，必须由归一化、固定 cusp 横截面或额外端值条件处理。

---

## 约束传播所需修正

不能只求解各向异性差方程并声称全部 Einstein 约束自动传播。线性化 contracted Bianchi 恒等式适用于迹反转张量
\[
\bar E=E-\frac12(\operatorname{tr}_{g_0}E)g_0,
\qquad
\nabla^i\delta\bar E_{ij}=0.
\]

若写
\[
\delta E_{tt}=A\cos(kz),\qquad
\delta E_{tz}=P\sin(kz),
\]
及
\[
e^{-2t}\delta E_{zz}=Z\cos(kz),\quad
e^{-2t}\delta E_{xx}=X\cos(kz),\quad
e^{-2t}\delta E_{yy}=Y\cos(kz),
\]
令 \(T=Z+X+Y\)，则 Bianchi 系统为
\[
A'-T'+6A-2T+2ke^{-2t}P=0,
\]
\[
P'+3P-k\left(Z-\frac{A+T}{2}\right)=0.
\]
若全部三个切向方程 \(Z=X=Y=0\) 已成立，则
\[
A'+6A+2ke^{-2t}P=0,\qquad
P'+3P+\frac{k}{2}A=0.
\]
因此 \(A=P=0\) 在某一切片成立时才传播为零。只解 \(X-Y=0\)，或只解某个缩减的空间方程组，并不足以控制 \(E_{00},E_{0z}\)。这与源材料中关于必须求解完整 Einstein–DeTurck 系统或严格证明约束传播的警告一致。

最后还应区分方向：所写
\[
dt^2+e^{2t}g_{T^3}
\]
在 \(t\to+\infty\) 是扩张端。标准有限体积 cusp 常写为
\[
dr^2+e^{-2r}g_{T^3},\qquad r\to+\infty.
\]
若改取 \(r=-t\)，端点及 Bessel 大参数渐近也随之改变，不能沿用上述“小 \(x\)”叙述。

**最终判定：** 第 1–3 步及 \(E_{zz}\) 的空间导数项正确；第 4 步符号错误，正确 prefactor 是 \(x^{3/2}\)；第 5 步错误，两支分别衰减至零和趋于常数。因两支均有界，“Neumann + boundedness”不唯一；必须规定渐近值或非零 Fourier 模式趋零。零模含不可消除的平坦环面模量，而完整约束传播还要求全部切向方程和兼容的初始约束数据。
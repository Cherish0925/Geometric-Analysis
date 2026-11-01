# TTCS Independent Branch Record

```json
{
  "step_id": 74,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/data/step70_ricci_T2inv.json",
    "Sessions/S0910A03/workspace/scripts/step74_linearized_mode_analysis.py",
    "Sessions/S0910A03/workspace/data/step74_linearized_modes.json",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md"
  ]
}
```

## Task

Verify the following derivation for the linearized Einstein equations around the flat hyperbolic cusp g0 = dt^2 + e^{2t}(dz^2 + dx^2 + dy^2), perturbed by T^2-invariant diagonal modes a=t+alpha(t)cos(kz), b=t+beta(t)cos(kz), c=t+gamma(t)cos(kz):

1. The constraint E_{01}=0 linearizes to beta'+gamma'=0, so beta+gamma=const for each k!=0 mode.
2. E_{00}=0 gives h''+2h'=0 for h=alpha+beta+gamma.
3. The anisotropy psi=beta-gamma satisfies psi''+3psi'-k^2 e^{-2t}psi=0.
4. Under x=ke^{-t}, this becomes x^2 psi_xx + 4x psi_x - x^2 psi = 0, which via psi=x^{-3/2}z reduces to the modified Bessel equation with nu=3/2.
5. The I-branch psi ~ x^{-3/2}I_{3/2}(x) is bounded as t->infinity (x->0), while the K-branch grows as e^{3t}.

Check each step. Also verify: does this BVP structure (center Neumann + cusp boundedness) give a unique solution per Fourier mode? What happens at k=0 (zero mode)? Are there corrections needed for the constraint propagation? Does the E_{11} equation actually give the correct z-derivative terms?

## Output

# 科学核验备忘

令 \(w=\beta+\gamma\)、\(h=\alpha+\beta+\gamma=\alpha+w\)，并记

\[
q(t)=k^2e^{-2t}.
\]

在线性阶，所有量均乘相应的 \(\cos(kz)\) 或 \(\sin(kz)\)。

## 1. 完整线性化分量

从给出的精确 Ricci 公式直接展开可得

\[
\delta E_{tt}=-(h''+2h')\cos(kz),
\]

\[
\delta E_{tz}=k(\beta'+\gamma')\sin(kz)
              =k w'\sin(kz).
\]

采用复 Fourier 模式 \(e^{ikz}\) 时，后一式写成

\[
\delta E_{tz}=-ik\,w'e^{ikz};
\]

两种约定给出同一方程 \(w'=0\)。

三个切向对角分量为

\[
e^{-2t}\delta E_{zz}
=
\left[-\alpha''-3\alpha'-h'+q(\beta+\gamma)\right]\cos(kz),
\]

\[
e^{-2t}\delta E_{xx}
=
\left[-\beta''-3\beta'-h'+q\beta\right]\cos(kz),
\]

\[
e^{-2t}\delta E_{yy}
=
\left[-\gamma''-3\gamma'-h'+q\gamma\right]\cos(kz).
\]

由于背景满足 \(E=0\)，在线性阶使用 \(e^{-2a}E_{zz}\) 或 \(e^{-2t}\delta E_{zz}\) 是等价的。

### \(E_{zz}\) 中的 \(z\)-导数项

精确归一化分量含有

\[
e^{-2a}
\left(
a_zb_z+a_zc_z-b_z^2-b_{zz}-c_z^2-c_{zz}
\right).
\]

前四个一阶导数的乘积均为二阶小量，线性阶只留下

\[
-e^{-2t}(b_{zz}+c_{zz})
=
k^2e^{-2t}(\beta+\gamma)\cos(kz).
\]

因此脚本中 \(E_{11}\) 的 \(q(\beta+\gamma)\) 项正确。在线性阶没有 \(\alpha_{zz}\) 项，这与精确公式一致。

## 2. 对五个推导步骤的核验

### 步骤 1：正确

当 \(k\ne0\) 时，

\[
E_{tz}=0\quad\Longrightarrow\quad
\beta'+\gamma'=w'=0,
\]

故 \(w\) 关于 \(t\) 为常数。它仍然乘 \(\cos(kz)\)，所以不是空间常数。

### 步骤 2：正确

\[
E_{tt}=0
\quad\Longrightarrow\quad
h''+2h'=0,
\]

故

\[
h(t)=H+D e^{-2t}.
\]

### 步骤 3：正确

将归一化的 \(xx\) 与 \(yy\) 方程相减，并令

\[
\psi=\beta-\gamma,
\]

得到

\[
\boxed{\psi''+3\psi'-k^2e^{-2t}\psi=0.}
\]

这也正是背景双曲度量上 Fourier 模式的调和方程。

### 步骤 4：变量替换中有符号错误

取

\[
x=ke^{-t},\qquad \frac{d}{dt}=-x\frac{d}{dx},
\]

则

\[
\psi_t=-x\psi_x,\qquad
\psi_{tt}=x^2\psi_{xx}+x\psi_x.
\]

因此正确方程是

\[
x^2\psi_{xx}+x\psi_x-3x\psi_x-x^2\psi=0,
\]

即

\[
\boxed{x^2\psi_{xx}-2x\psi_x-x^2\psi=0.}
\]

脚本中的 \(+4x\psi_x\) 来自把 \(3\psi_t=-3x\psi_x\) 写成了 \(+3x\psi_x\)。

正确代换是

\[
\boxed{\psi=x^{3/2}z},
\]

而不是 \(x^{-3/2}z\)。代入后得到

\[
x^2z''+xz'-\left(x^2+\frac94\right)z=0,
\]

这是阶数 \(\nu=3/2\) 的修正 Bessel 方程。因此

\[
\boxed{
\psi(x)
=x^{3/2}\left[A I_{3/2}(x)+B K_{3/2}(x)\right].
}
\]

### 步骤 5：两支的渐近行为需重写

当 \(t\to+\infty\)、\(x\to0\) 时，

\[
I_{3/2}(x)\sim
\frac{x^{3/2}}{2^{3/2}\Gamma(5/2)},
\qquad
K_{3/2}(x)\sim
2^{1/2}\Gamma(3/2)x^{-3/2}.
\]

故

\[
x^{3/2}I_{3/2}(x)\sim C_Ix^3
=C_Ik^3e^{-3t},
\]

而

\[
x^{3/2}K_{3/2}(x)\sim C_K.
\]

所以正确结论是：

\[
\boxed{\text{\(I\) 支按 \(e^{-3t}\) 衰减，\(K\) 支趋于常数；两支都保持有界。}}
\]

不存在这里所述的 \(e^{3t}\) 增长支。这也可从渐近方程直接看出：

\[
\psi''+3\psi'=0
\quad\Longrightarrow\quad
\psi=C_1+C_2e^{-3t}.
\]

半整数阶的显式公式进一步给出

\[
x^{3/2}I_{3/2}(x)
=\sqrt{\frac2\pi}\bigl(x\cosh x-\sinh x\bigr),
\]

\[
x^{3/2}K_{3/2}(x)
=\sqrt{\frac\pi2}(1+x)e^{-x}.
\]

## 3. “中心 Neumann + 末端有界”不产生唯一解

对 \(k>0\)，正确的两支在 \(t\to+\infty\) 都有界。因此“末端有界”没有排除任何一个基本解。

中心条件

\[
\psi'(0)=0
\]

只在两个系数 \(A,B\) 之间给出一个线性关系，因而仍保留一维解族。显式地，

\[
\frac d{dt}\bigl(x^{3/2}I_{3/2}(x)\bigr)
=-\sqrt{\frac2\pi}x^2\sinh x,
\]

\[
\frac d{dt}\bigl(x^{3/2}K_{3/2}(x)\bigr)
=\sqrt{\frac\pi2}x^2e^{-x}.
\]

两者在任何有限 \(x=k>0\) 都非零，故 Neumann 条件确实只确定 \(A/B\)。

若额外指定渐近值

\[
\lim_{t\to\infty}\psi(t)=L,
\]

则 \(K\) 支系数先由 \(L\) 确定，Neumann 条件再唯一确定 \(I\) 支系数。特别地，若要求非零 Fourier 模式满足

\[
\psi(t)\longrightarrow0,
\]

则 \(B=0\)，随后 Neumann 条件迫使 \(A=0\)。这时齐次解只有零解。

在有限区间上，中心 Neumann 加另一端的 Dirichlet 端值也给出唯一解。齐次情形可由

\[
(e^{3t}\psi')'-k^2e^t\psi=0
\]

乘以 \(\psi\) 后积分证明。

还有一个几何事实：背景 \(g_0\) 的切片形算子为 \(S=I\)，并非反射中心所需的 \(S=0\)。因此该线性化只能研究各向异性差值的 Neumann 条件，不能把完整反射中心看成 \(g_0\) 的小扰动。

## 4. \(k=0\) 模式

当 \(k=0\) 时，\(E_{tz}\) 恒等为零，不能从中推出 \(w'=0\)。各向异性方程退化为

\[
\psi''+3\psi'=0,
\]

故

\[
\psi=C+De^{-3t}.
\]

两支均有界。中心 Neumann 条件给出 \(D=0\)，但常数各向异性 \(C\) 保留；它对应于改变平坦 \(T^3\) 横截面的常数模参数。

若要求全部线性 Einstein 方程成立，则零模的一般解可写成

\[
\alpha=A_\alpha+B_\alpha e^{-3t},\qquad
\beta=A_\beta+B_\beta e^{-3t},\qquad
\gamma=A_\gamma+B_\gamma e^{-3t},
\]

其中

\[
B_\alpha+B_\beta+B_\gamma=0.
\]

完整中心 Neumann 条件迫使所有 \(B_i=0\)，而三个常数 \(A_i\) 仍保留。

## 5. \(E_{zz}\) 还给出额外的标量关系

步骤 1、2、3 并非整个线性 Einstein 系统。对 \(k\ne0\)，令

\[
w=W,\qquad h=H+De^{-2t}.
\]

由 \(E_{zz}=0\) 得到

\[
(4D+k^2W)e^{-2t}=0,
\]

即

\[
\boxed{D=-\frac{k^2W}{4}.}
\]

所以 \(E_{zz}\) 不改变各向异性方程，却是迹/和模式所必需的方程。

## 6. 约束传播

需要使用迹反转张量

\[
\overline E
=E-\frac12(\operatorname{tr}_{g_0}E)g_0,
\]

因为线性化恒等式是

\[
\nabla^i\overline E_{ij}=0,
\]

而不是直接写成 \(\nabla^iE_{ij}=0\)。

设

\[
\delta E_{tt}=A\cos(kz),\quad
\delta E_{tz}=P\sin(kz),
\]

以及

\[
e^{-2t}\delta E_{zz}=Z\cos(kz),\quad
e^{-2t}\delta E_{xx}=X\cos(kz),\quad
e^{-2t}\delta E_{yy}=Y\cos(kz),
\]

并令 \(T=Z+X+Y\)。线性 Bianchi 恒等式给出

\[
A'-T'+6A-2T+2ke^{-2t}P=0,
\]

\[
P'+3P-k\left(Z-\frac{A+T}{2}\right)=0.
\]

若三个切向方程 \(Z=X=Y=0\) 全部成立，则

\[
A'+6A+2ke^{-2t}P=0,
\]

\[
P'+3P+\frac{k}{2}A=0.
\]

因此若 \(A\) 与 \(P\) 在某一切片同时为零，它们随后保持为零。只求解各向异性差方程 \(X-Y=0\) 并不足以得到这一传播结论。

## 7. 数值脚本对应关系

`aniso_ode`

```python
ddp = -3*dp + k_val**2*np.exp(-2*t_val)*p
```

编码的是正确 ODE。但 `psi_I`、`psi_K` 采用了错误的 prefactor：

```python
x**(-1.5) * I_{3/2}(x),  x**(-1.5) * K_{3/2}(x)
```

它们不满足 `aniso_ode`。正确函数应为

```python
x**(1.5) * iv(1.5, x)
x**(1.5) * kv(1.5, x)
```

因此 `step74_linearized_modes.json` 中的 \(e^{3t}\) 数值增长及相应 transmission 数值不能验证所述 Bessel 分支。正确 ODE 的所有解在所写的 \(t\to+\infty\) 方向都趋于常数或按 \(e^{-3t}\) 衰减。

最后，按所写度量，\(t\to+\infty\) 是横截面扩张方向。通常的有限体积双曲 cusp 写成

\[
dr^2+e^{-2r}g_{T^3},\qquad r\to+\infty.
\]

若研究的是这一方向，应取 \(r=-t\)；此时 \(x=ke^r\to\infty\)，\(I\) 支按 \(e^x\) 增长，\(K\) 支按 \(e^{-x}\) 衰减，仍不是 \(e^{3r}\) 型行为。

**总评：步骤 1–3 及 \(E_{zz}\) 的空间导数项正确；步骤 4 的链式法则符号有误，因而步骤 5、数值分支解释和“有界性选择唯一分支”的结论均需按上述公式重写。**
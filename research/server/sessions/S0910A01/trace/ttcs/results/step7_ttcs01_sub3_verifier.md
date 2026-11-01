# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/scripts/step7_bochner_conformal_kahler.py",
    "Sessions/S0910A01/workspace/notes/step7_local_vs_global_rigidity.md",
    "Sessions/S0910A01/workspace/scripts/step6_tensor_slack_algebra.py"
  ]
}
```

## Task

Verify the following chain of claims for the negative-branch analysis of Yau Problem 26 in dimension 4.

1. BOCHNER FORMULA: On a 4-dimensional Einstein manifold with div(W+)=0, the scalar Bochner formula is (1/2)Δ|W+|² = |∇W+|² + (s/3)|W+|² - 4·tr(W+³), where tr(W+³) = α³+β³+γ³ = 3αβγ for trace-free eigenvalues α+β+γ=0. Check the coefficient -4 against the ℂℍ² example (s=-4, eigenvalues (1/3,1/3,-2/3), |W+|²=2/3, W+ parallel).

2. CALIBRATED PROFILE CONSISTENCY: At the target eigenvalues (1/12,1/12,-1/6) with |W+|²=1/24 and s=-4, the Bochner formula gives |∇W+|² = 1/24 > 0. Is this calculation correct? Does it mean the calibrated two-eigenvalue profile with constant norm is consistent but NOT parallel?

3. CONFORMAL-KÄHLER OBSTRUCTION: On a smooth Einstein 4-manifold with Ric=-g, if W+ has the two-eigenvalue profile, Derdziński gives conformally Kähler: g̃=f²g is Kähler. The conformal weight gives |W+_g|² = f⁴s̃²/24 where s̃ is the Kähler scalar curvature. For constant |W+_g|²=1/24: f²|s̃|=1. The conformal scalar curvature relation s̃=f⁻²(s-6f⁻¹Δf) with s=-4 and f²s̃=-1 gives Δf=-f/2. On a COMPACT Einstein manifold: Stokes gives ∫Δf=0=-(1/2)∫f<0, contradiction, so f=const and the metric is Kähler with |W+|²=s²/24=2/3≠1/24. On a NONCOMPACT limit: Δf=-f/2 can have nonconstant positive solutions. Verify each step, especially the sign conventions and the conformal transformation formula.

4. STRUCTURAL CONSEQUENCE: Does this correctly show that the local Derdziński mechanism cannot give a contradiction on noncompact pointed limits, making the negative-branch argument inherently global?

## Output

## 科学核验备忘

按文中采用的曲率算子归一化
\[
|W^+|^2=\alpha^2+\beta^2+\gamma^2,\qquad
s_{\mathrm{K\ddot ahler}}\Longrightarrow
\operatorname{spec}(W^+)=\left(\frac s6,-\frac s{12},-\frac s{12}\right),
\]
这条推理链有两处核心数学错误：

1. Bochner 公式的系数应为 \(s/2\) 与 \(-6\operatorname{tr}(W^+)^3\)，不是 \(s/3\) 与 \(-4\operatorname{tr}(W^+)^3\)。
2. Derdziński 给出的 Kähler 共形因子不是任意的；它正比于 \(|W^+|^{2/3}\)。因此常模长的精确二重特征值结构已经在局部推出 \(g\) 本身为 Kähler，并立即排除目标特征值，无须紧致性或 Stokes。

### 1. 正确的 Einstein–Weyl Bochner 公式

令
\[
\Delta_0=\nabla^i\nabla_i=\operatorname{div}\nabla
\]
为在紧致流形上谱非正的 Laplacian。Einstein 四维流形上，\(W^+\) 作为
\(\Lambda^+\) 上的无迹对称端omorphism，满足
\[
\nabla^*\nabla W^+
+\frac{s}{2}W^+
-6(W^+\circ W^+)_0=0,
\]
即
\[
\nabla^*\nabla W^+
+\frac{s}{2}W^+
-6W^+\circ W^+
+2|W^+|^2I=0.
\]
与 \(W^+\) 内积，并利用 \(\operatorname{tr}W^+=0\)，得到
\[
\boxed{
\frac12\Delta_0|W^+|^2
=
|\nabla W^+|^2
+\frac{s}{2}|W^+|^2
-6\,\operatorname{tr}\bigl((W^+)^3\bigr)
}.
\]
等价写法是
\[
\frac12\Delta_0|W^+|^2
=
|\nabla W^+|^2+\frac{s}{2}|W^+|^2-18\det(W^+),
\]
因为
\[
\alpha^3+\beta^3+\gamma^3=3\alpha\beta\gamma
\]
在 \(\alpha+\beta+\gamma=0\) 时确实成立。

若采用正谱 Laplacian \(\Delta_+=-\Delta_0\)，整个公式变为
\[
\frac12\Delta_+|W^+|^2
=
-|\nabla W^+|^2-\frac{s}{2}|W^+|^2
+6\operatorname{tr}\bigl((W^+)^3\bigr).
\]

#### 为什么 \(\mathbb{CH}^2\) 不能确定系数

对 \(s=-4\) 及特征值
\[
\left(\frac13,\frac13,-\frac23\right)
\]
有
\[
|W^+|^2=\frac23,\qquad
\operatorname{tr}(W^+)^3=-\frac29.
\]
正确公式中的代数项为
\[
\frac{s}{2}|W^+|^2-6\operatorname{tr}(W^+)^3
=-\frac43+\frac43=0.
\]
脚本中的表达式也为零：
\[
\frac{s}{3}|W^+|^2-4\operatorname{tr}(W^+)^3
=-\frac89+\frac89=0.
\]
原因是二者分别等于
\[
\frac12\bigl(s|W^+|^2-12\operatorname{tr}(W^+)^3\bigr),
\qquad
\frac13\bigl(s|W^+|^2-12\operatorname{tr}(W^+)^3\bigr),
\]
而括号在该 Kähler–Einstein 例子上本来就是零。由于同时还有
\(\nabla W^+=0\)，这个例子不能区分 \(1/2\) 与 \(1/3\)。因此
`step7_bochner_conformal_kahler.py` 第一部分的断言只核对了内部算术，没有确定几何公式的绝对系数。

### 2. 目标特征值处的正确数值

对
\[
\left(\frac1{12},\frac1{12},-\frac16\right)
\]
有
\[
|W^+|^2=\frac1{24},\qquad
\operatorname{tr}(W^+)^3
=2\left(\frac1{12}\right)^3-\left(\frac16\right)^3
=-\frac1{288}.
\]
若模长恒定，正确 Bochner 公式给出
\[
0
=
|\nabla W^+|^2
-\frac{2}{24}
+\frac{6}{288}
=
|\nabla W^+|^2-\frac1{16}.
\]
所以
\[
\boxed{|\nabla W^+|^2=\frac1{16}},
\]
而不是 \(1/24\)。

脚本中的 \(1/24\) 是在所写的非标准公式下算术正确的结果。采用正确公式后，这条标量恒等式单独看仍没有符号矛盾，并且若这样的几何对象存在，它不会是平行 Weyl 张量。但这一条标量恒等式没有纳入 \(\delta W^+=0\) 的全部一阶关系；Derdziński 结构实际上排除了该精确剖面。

### 3. 共形公式、符号和 Derdziński 因子

#### 共形 Weyl 模长

若
\[
\widetilde g=f^2g,
\]
四维 Hodge 分解保持不变，而 Weyl 曲率算子的特征值按 \(f^{-2}\) 缩放。因此
\[
|W_g^+|^2=f^4|W_{\widetilde g}^+|_{\widetilde g}^2.
\]
当 \(\widetilde g\) 为 Kähler 度量时，
\[
|W_{\widetilde g}^+|^2=\frac{\widetilde s^2}{24},
\]
故
\[
\boxed{|W_g^+|^2=\frac{f^4\widetilde s^2}{24}}.
\]
目标模长给出
\[
f^2|\widetilde s|=1.
\]
为匹配简单特征值 \(-1/6\)，确实应选择
\[
f^2\widetilde s=-1.
\]

#### 标量曲率变换

使用 \(\Delta_0=\operatorname{div}\nabla\)，四维公式为
\[
\boxed{
\widetilde s
=f^{-2}\left(s-6f^{-1}\Delta_0f\right)
}.
\]
代入 \(s=-4\) 和 \(f^2\widetilde s=-1\)，得到
\[
-1=-4-6\frac{\Delta_0f}{f},
\qquad
\boxed{\Delta_0f=-\frac12f}.
\]

若使用正谱算子 \(\Delta_+=-\Delta_0\)，相应公式必须同时改成
\[
\widetilde s=f^{-2}\left(s+6f^{-1}\Delta_+f\right),
\qquad
\Delta_+f=\frac12f.
\]
脚本第四部分把 \(\Delta\) 称为正谱 Laplacian，却继续采用
\(\Delta_0\) 的标量曲率公式与方程，文字中的符号约定不一致。

#### 紧致情形

在 \(\Delta_0\) 约定下，若 \(f>0\)，则
\[
0=\int_M\Delta_0 f\,d\mu
=-\frac12\int_M f\,d\mu<0,
\]
所以不存在满足目标分支方程的正函数。这里不能推出“因此 \(f\) 为常数”；正的常函数同样不满足
\(\Delta_0f=-f/2\)。积分直接排除了这样的 \(f\)。

#### 非紧致情形中的标量方程

仅就标量方程而言，非紧致完备 Einstein 流形上确实可能存在非恒定正解。例如在截面曲率 \(-1/3\) 的 \(\mathbb H^4\) 上，\(\operatorname{Ric}=-g\)。取满足
\[
|\nabla b|=1,\qquad \Delta_0b=\sqrt3
\]
的 Busemann 函数，并令
\[
f=e^{-ab},\qquad a=\frac{\sqrt3\pm1}{2}.
\]
则
\[
\Delta_0f=(a^2-\sqrt3a)f=-\frac12f.
\]
不过该例子有 \(W^+=0\)，只说明标量方程可解，并不提供目标 Weyl 剖面的 Einstein–Kähler 几何。

### 4. Derdziński 的完整微分结论给出局部矛盾

对于 \(\delta W^+=0\)、\(W^+\neq0\) 且恰有两个特征值的连通开集，Derdziński 的结论比“存在某个 \(f\)”更强：对应的 Kähler 度量为
\[
\boxed{
g_K=C\,|W_g^+|^{2/3}g
}
\]
，其中 \(C>0\) 为常数；等价地，共形因子由 \(W^+\) 的简单特征值确定。

目标剖面满足
\[
|W_g^+|^2=\frac1{24}
\]
处处恒定，所以 \(g_K\) 只是 \(g\) 的常数倍。因此 \(g\) 本身局部 Kähler。又因
\[
\operatorname{Ric}_g=-g,\qquad s_g=-4,
\]
Kähler 曲率代数强制
\[
\operatorname{spec}(W_g^+)
=
\left(-\frac23,\frac13,\frac13\right),
\qquad
|W_g^+|^2=\frac23.
\]
这与
\[
\left(-\frac16,\frac1{12},\frac1{12}\right),
\qquad
|W_g^+|^2=\frac1{24}
\]
不相容。该推导在任一满足精确剖面的开集上成立，不使用紧致性、Stokes 或全局拓扑。

因此，非紧致情形中 \(\Delta f=-f/2\) 的正解只表明“标量曲率变换方程”本身不足；一旦保留 Derdziński 对共形因子的微分确定性，精确目标剖面已经被局部排除。

### 5. 对结构性结论的影响

所述“局部 Derdziński 机制无法在非紧致 pointed limit 上产生矛盾”并不成立于文中假定的精确光滑极限。若极限在开集上同时满足：

\[
\operatorname{Ric}=-g,\qquad
|W^+|^2=\frac1{24},\qquad
\operatorname{spec}(W^+)=
\left(-\frac16,\frac1{12},\frac1{12}\right),
\]
则上述局部推导已经排除该开集。

全局方法仍可能用于另外的环节，例如从平均缺量推出整个正则开集上的精确特征值等式，或处理塌缩序列。那与精确剖面在局部是否相容是不同的数学问题。

另有两处文件一致性问题：

- `step7_bochner_conformal_kahler.py` 称 \(\mathbb H^2\times\mathbb H^2\) 的 \(W^+=0\)。按乘积复结构的 Kähler 定向，它有 \(s=-4\)，故
  \[
  \operatorname{spec}(W^+)=\left(-\frac23,\frac13,\frac13\right),
  \]
  并非共形平坦。
- `step7_local_vs_global_rigidity.md` 的 Step C 从 Ricci 误差的一致收敛直接推出 \(C^{2,\alpha}\) 收敛，缺少 Ricci 误差的 Hölder 半范数控制。谐和坐标下可先获得 \(W^{2,p}\) 收敛，使极限弱满足 Einstein 方程，再由极限方程提升为光滑；Weyl 剖面的传递应通过强 \(W^{2,p}\)/曲率积分收敛完成，而不能直接引用所写的 Schauder 步骤。
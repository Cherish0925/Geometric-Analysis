# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 7,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step7_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step7_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following chain of claims for the negative-branch analysis of Yau Problem 26 in dimension 4.

1. BOCHNER FORMULA: On a 4-dimensional Einstein manifold with div(W+)=0, the scalar Bochner formula is (1/2)Δ|W+|² = |∇W+|² + (s/3)|W+|² - 4·tr(W+³), where tr(W+³) = α³+β³+γ³ = 3αβγ for trace-free eigenvalues α+β+γ=0. Check the coefficient -4 against the ℂℍ² example (s=-4, eigenvalues (1/3,1/3,-2/3), |W+|²=2/3, W+ parallel).

2. CALIBRATED PROFILE CONSISTENCY: At the target eigenvalues (1/12,1/12,-1/6) with |W+|²=1/24 and s=-4, the Bochner formula gives |∇W+|² = 1/24 > 0. Is this calculation correct? Does it mean the calibrated two-eigenvalue profile with constant norm is consistent but NOT parallel?

3. CONFORMAL-KÄHLER OBSTRUCTION: On a smooth Einstein 4-manifold with Ric=-g, if W+ has the two-eigenvalue profile, Derdziński gives conformally Kähler: g̃=f²g is Kähler. The conformal weight gives |W+_g|² = f⁴s̃²/24 where s̃ is the Kähler scalar curvature. For constant |W+_g|²=1/24: f²|s̃|=1. The conformal scalar curvature relation s̃=f⁻²(s-6f⁻¹Δf) with s=-4 and f²s̃=-1 gives Δf=-f/2. On a COMPACT Einstein manifold: Stokes gives ∫Δf=0=-(1/2)∫f<0, contradiction, so f=const and the metric is Kähler with |W+|²=s²/24=2/3≠1/24. On a NONCOMPACT limit: Δf=-f/2 can have nonconstant positive solutions. Verify each step, especially the sign conventions and the conformal transformation formula.

4. STRUCTURAL CONSEQUENCE: Does this correctly show that the local Derdziński mechanism cannot give a contradiction on noncompact pointed limits, making the negative-branch argument inherently global?

## Integrated Scientific Memo

## 核验结论

所给四步链条不成立。关键有两处：

1. 在题中采用的归一化下，标准 Einstein–Weyl Bochner 公式的系数是 \(s/2\) 与 \(-6\)，不是 \(s/3\) 与 \(-4\)。
2. Derdziński 的共形因子并非任意正函数；在二重特征值区域，它由 \(W^+\) 决定，正比于 \(|W^+|^{2/3}\)。因此“二重特征值且 \(|W^+|\) 恒定”已经局部推出 \(g\) 本身为 Kähler，从而立即与目标模长矛盾。非紧致性不能解除这个局部矛盾。

以下固定
\[
\Delta=\operatorname{div}\nabla ,
\]
即闭流形上谱非正的 Laplacian。

### 1. Bochner 公式

按
\[
|W^+|^2=\alpha^2+\beta^2+\gamma^2,\qquad
\operatorname{tr}(W^{+3})=\alpha^3+\beta^3+\gamma^3
\]
的归一化，Einstein 四维流形上正确公式是
\[
\boxed{\frac12\Delta |W^+|^2
=|\nabla W^+|^2+\frac{s}{2}|W^+|^2
-6\,\operatorname{tr}(W^{+3}).}
\]
由于 \(\alpha+\beta+\gamma=0\)，
\[
\operatorname{tr}(W^{+3})=3\alpha\beta\gamma.
\]

\(\mathbb{CH}^2\) 检验不能区分题中的错误系数和正确系数。对于
\[
s=-4,\qquad \operatorname{spec}(W^+)=\left(\frac13,\frac13,-\frac23\right),
\]
有
\[
|W^+|^2=\frac23,\qquad \operatorname{tr}(W^{+3})=-\frac29.
\]
于是正确公式的代数项为
\[
\frac{s}{2}|W^+|^2-6\operatorname{tr}(W^{+3})
=-\frac43+\frac43=0,
\]
而题设公式也偶然给出
\[
\frac{s}{3}|W^+|^2-4\operatorname{tr}(W^{+3})
=-\frac89+\frac89=0.
\]
两组系数都满足比例 \(b=-12a\)，所以该平行 Kähler–Einstein 例子只能检验系数比，不能检验绝对系数。

若改用正谱算子 \(\Delta_+=-\Delta\)，则整个标量公式右端变号：
\[
\frac12\Delta_+|W^+|^2
=-|\nabla W^+|^2-\frac{s}{2}|W^+|^2
+6\operatorname{tr}(W^{+3}).
\]

### 2. 目标剖面处的数值

对
\[
\left(\frac1{12},\frac1{12},-\frac16\right)
\]
有
\[
|W^+|^2=\frac1{24},\qquad
\operatorname{tr}(W^{+3})=-\frac1{288}.
\]
若 \(|W^+|\) 恒定，则正确 Bochner 公式给出
\[
0=|\nabla W^+|^2
+\frac{-4}{2}\frac1{24}
-6\left(-\frac1{288}\right),
\]
故
\[
\boxed{|\nabla W^+|^2=\frac1{16},}
\]
不是 \(1/24\)。

因此：

- 脚本中的 \(1/24\) 仅是在错误系数下的正确算术；
- 正确标量 Bochner 恒等式本身仍不给出符号矛盾，并要求 \(W^+\) 非平行；
- 但这只是必要条件，不足以证明该剖面几何上可实现。完整的 \(\delta W^+=0\) 一阶结构通过 Derdziński 定理排除了它。

### 3. 共形公式与紧致积分

若
\[
\widetilde g=f^2g
\]
为 Kähler，则 Weyl 特征值的共形缩放给出
\[
|W_g^+|^2=f^4|W_{\widetilde g}^+|_{\widetilde g}^2
=\frac{f^4\widetilde s^{\,2}}{24}.
\]
因此目标模长意味着
\[
f^2|\widetilde s|=1.
\]
为匹配简单特征值 \(-1/6\)，取负分支
\[
f^2\widetilde s=-1.
\]

在 \(\Delta=\operatorname{div}\nabla\) 约定下，四维标量曲率变换公式是
\[
\boxed{\widetilde s
=f^{-2}\left(s-6f^{-1}\Delta f\right).}
\]
代入 \(s=-4\) 和 \(f^2\widetilde s=-1\)，得到
\[
-1=-4-6\frac{\Delta f}{f},
\qquad
\boxed{\Delta f=-\frac12f.}
\]
这一计算正确。若使用正谱 \(\Delta_+=-\Delta\)，则应同时写成
\[
\widetilde s=f^{-2}\left(s+6f^{-1}\Delta_+f\right),
\qquad
\Delta_+f=\frac12f.
\]
源脚本把 \(\Delta\) 称为正谱 Laplacian，却使用了非正谱约定的变换公式，符号说明不一致。

在闭流形上，若 \(f>0\)，则
\[
0=\int_M\Delta f\,d\mu
=-\frac12\int_M f\,d\mu<0,
\]
所以该方程根本没有正解。这里不应表述为“因此 \(f\) 为常数”；非零正的常函数同样不满足方程。

仅把它视为标量方程时，在非紧致流形上确实可能有正的非恒定解。但这并不证明存在所需的 Einstein–Weyl 几何，因为 Derdziński 的共形因子还满足更强的几何约束。

### 4. Derdziński 因子给出的局部矛盾

在 \(\delta W^+=0\)、\(W^+\neq0\) 且恰有两个特征值的连通开集上，Derdziński 结论不是“存在任意 \(f\) 使 \(f^2g\) Kähler”，而是 Kähler 度量可取为
\[
\boxed{g_K=C\,|W_g^+|^{2/3}g}
\]
（常数归一化无关紧要）。

目标剖面满足
\[
|W_g^+|^2=\frac1{24}
\]
恒定，所以这个共形因子恒定。因此 \(g_K\) 与 \(g\) 局部同尺度，\(g\) 本身局部 Kähler。再结合
\[
\operatorname{Ric}_g=-g,\qquad s_g=-4,
\]
Kähler 曲率代数强制
\[
\operatorname{spec}(W_g^+)
=\left(-\frac23,\frac13,\frac13\right),
\qquad
|W_g^+|^2=\frac{s_g^2}{24}=\frac23.
\]
这与目标
\[
\operatorname{spec}(W_g^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right),
\qquad |W_g^+|^2=\frac1{24}
\]
直接矛盾。

故精确假设
\[
\operatorname{Ric}=-g,\qquad |W^+|^2=\frac1{24},
\qquad W^+\text{ 有二重特征值}
\]
在任何开集上都不可同时成立。这是纯局部结论，不依赖紧致性、Stokes 或全局拓扑。

## 对第 4 项的修正

“局部 Derdziński 机制不能在非紧致 pointed limit 上产生矛盾，因此论证内在地是全局的”是错误的。对于**光滑、非塌缩且确实继承了恒定模长和二重特征值等式的 Einstein 极限**，Derdziński 已经给出局部矛盾。

真正仍可能需要全局或塌缩分析的环节是：

- 是否能从积分缺量严格传递到极限上的点态二重特征值等式；
- 塌缩序列中没有光滑四维 pointed limit 时如何处理；
- 奇异极限或仅弱曲率收敛时如何实施 Derdziński 结构。

另需修正源文件中的两个旁支错误：

- \(\mathbb H^2\times\mathbb H^2\) 按乘积复结构的 Kähler 定向并非 \(W^+=0\)；因 \(s=-4\)，其
  \[
  \operatorname{spec}(W^+)=\left(-\frac23,\frac13,\frac13\right).
  \]
- 谐和坐标中，仅由 Ricci 误差一致趋零不能直接用 Schauder 得到 \(C^{2,\alpha}\) 收敛，因为缺少误差的 Hölder 控制。应先建立 \(W^{2,p}\) 紧性和弱 Einstein 极限，再对极限方程正则化，并另行证明曲率剖面的强传递。

最后，目标关系 \(s+8\sqrt6|W^+|=0\) 应回溯到所用 LeBrun 不等式核对。通常 Kähler–Einstein 关系是
\[
s+2\sqrt6|W^+|=0\quad(s<0).
\]
若 \(8\sqrt6\) 确由相关等号分析推出，则上述局部矛盾正是非塌缩极限所需结论；若该常数来自归一化错误，则目标剖面本身需要重新校准。
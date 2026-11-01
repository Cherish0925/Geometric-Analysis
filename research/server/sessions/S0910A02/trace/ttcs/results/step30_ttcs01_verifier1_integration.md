# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 30,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step30_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step30_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the Step-30 route reassessment for Yau Problem 26. The key proposed direction is the four-dimensional positive noncollapsed bubble route: if the Cheeger--Naber bad set is empty, smooth Einstein existence on the same manifold follows; if singularities occur, use a variational Pohozaev/Komar projection for merely C^0 Ricci-pinched metrics to recover the Ozuch/Biquard Eguchi--Hanson first obstruction R_+ v=0, without assuming exact Einstein weighted normal form. Read the supplied notes and source excerpts/files. Assess target fidelity, mathematical correctness of the noncollapsed reduction, source-scope limits, whether the divergence-free Einstein-tensor identity is the right C^0-safe bulk pairing, whether first-obstruction vanishing plausibly leads toward actual Einstein existence, and the most serious gaps or likely false assumptions.

## Integrated Scientific Memo

# Step-30 路线独立核验结论

## 1. 总体判断

Step 30 的目标口径基本忠实，且有三项可靠成果：

1. **非塌缩且无调和半径退化时，原光滑流形最终承载 Einstein 度量；**
2. **带宇宙常数的 Einstein 张量是适合 \(C^0\) Ricci 缺陷的散度自由体配对；**
3. **Eguchi–Hanson 固定取向的一阶障碍确为 \(R_+v=0\)，允许改变取向后才弱化为 \(\det R_+=0\)。**

但所提“变分 Pohozaev/Komar 投影”目前尚未跨过核心障碍。缺失的不只是一个边界恒等式，而是：

\[
C^0\text{-Ricci 夹逼}
\Longrightarrow
\text{具有尺度精度的 orbifold/ALE 双尺度展开}.
\]

现有 Ozuch 资料只为**精确 Einstein 序列**提供这种加权颈部正规形。即使成功推出 \(R_+v=0\)，也远不能推出原解析拓扑上存在 Einstein 度量；高阶障碍、全局余核、多个泡及拓扑恢复仍是独立问题。因而 Route A 是合理的必要条件研究路线，但目前不能称为接近闭合的存在性路线。

---

## 2. 目标口径

同号区间可通过常数缩放正规化为近正或近负 Einstein 分支。若 \(0<c<C\)，取适当缩放可写成

\[
\|\operatorname{Ric}_{\tilde g}-\tilde g\|_{\mathrm{op}}
\le \frac{C-c}{C+c}.
\]

所以证明任一足够窄的正分支，确实足以给出原命题中的一组常数。

需要修正反证口径：若要否定原命题，必须击败**所有** \(c_n<C_n\)，包括跨零区间；仅击败正、负同号正规化分支并不逻辑上涵盖任意宽的混号区间。这不影响当前作为证明方向的四维正分支研究，但不能把“两种符号分支均失败”直接等同于原命题被否定。

当前路线只涉及四维、正分支、非塌缩子情形；它没有处理一般塌缩、\(n\ge5\)、非定向流形的全局取向/下降问题。

---

## 3. 非塌缩正分支的规则部分

设

\[
\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op}}\le \delta_i\to0,
\qquad
\operatorname{Vol}(M_i,g_i)\ge v_0>0.
\]

则

\[
\operatorname{Ric}_{g_i}\ge(1-\delta_i)g_i,
\]

故 Myers 给出统一直径界

\[
\operatorname{diam}(M_i,g_i)
\le \pi\sqrt{\frac{3}{1-\delta_i}}.
\]

结合总容量下界和 Bishop–Gromov，可得固定尺度上的局部非塌缩。Cheeger–Naber 型调和坐标紧性于是给出规则区域上的

\[
C^{1,\alpha}\cap W^{2,p}
\]

收敛。写

\[
A_i=\operatorname{Ric}_{g_i}-g_i,\qquad
\|A_i\|_{L^\infty}\to0,
\]

调和坐标中的 Ricci 方程可弱极限到

\[
\operatorname{Ric}_{g_\infty}=g_\infty.
\]

随后由 Einstein 方程的椭圆正则性，极限在规则区域上光滑。

若“坏集为空”具体指全流形上有统一正的调和半径下界，则可得到紧致全局图册和最终微分同胚

\[
F_i:M_\infty\to M_i.
\]

于是

\[
(F_i^{-1})^*g_\infty
\]

是 \(M_i\) 上的光滑 Einstein 度量，满足“同一个光滑流形”的要求。

这里应删去“输入度量 \(g_i\) 光滑收敛”这一过强说法。仅有 \(L^\infty\) Ricci 缺陷时，没有 Ricci 导数控制；通常只能直接得到 \(C^{1,\alpha}\cap W^{2,p}\) 收敛。它足以恢复微分同胚，但不足以声称 \(g_i\) 本身 \(C^\infty\) 收敛。此外，“极限度量空间光滑”不自动等价于“没有微观调和半径集中”；后者才是上述结论所需的正确条件。

---

## 4. 奇异情形尚未被归约成已验证的有限 ALE 泡树

这是 Step 30 最需收紧之处。

所给 Ozuch 文献中的以下结论都以**精确 Einstein** 为假设：

- 非塌缩四维 Einstein 序列收敛到 Einstein orbifold；
- 奇点吹起为 Ricci-flat ALE；
- 颈部具有加权 \(C^k\) 控制；
- GH 逼近 orbifold 的 Einstein 度量来自 gluing–perturbation 正规形。

对仅满足

\[
\|\operatorname{Ric}_{g_i}-g_i\|_{L^\infty}\to0
\]

的序列，所给资料并未同时证明：

1. 奇异能量只集中于有限个点；
2. 无未建模的颈部能量损失；
3. 每个尺度吹起均为光滑完备 Ricci-flat ALE；
4. 存在有限泡树并携带 \(M_i\) 的完整微分拓扑；
5. 可在重叠区写出兼容的
   \[
   g_o=e+H_2+O(r^3),\qquad
   g_b=e+H^4+O(r^{-5})
   \]
   及足够强的余项估计。

Cheeger–Naber 的有界 Ricci 正则理论不等同于这套 Einstein 泡树正规形。Ozuch 颈部估计依赖精确 Einstein 方程产生的曲率椭圆方程/调和曲率；一般 \(C^0\) Ricci 缺陷会引入不可控的 \(\nabla\operatorname{Ric}\) 项。因此，目前不能把奇异情形无条件称为“已经归约成有限 orbifold/ALE 问题”。该表述只有在另加一个针对 \(L^\infty\)-近 Einstein 序列的泡树定理后才成立。

---

## 5. 散度自由 Einstein 张量：正确且有用，但只是外壳

令

\[
\mathcal E_g
=
\operatorname{Ric}_g-\frac12s_g g+\frac{n-2}{2}g.
\]

若

\[
A=\operatorname{Ric}_g-g,
\]

则恰有

\[
\boxed{\mathcal E_g=A-\frac12(\operatorname{tr}_gA)g.}
\]

因此：

- \(\operatorname{Ric}_g=g\) 时 \(\mathcal E_g=0\)；
- 由缩约 Bianchi 恒等式，
  \[
  \delta_g\mathcal E_g=0;
  \]
- 若 \(A\) 的特征值均在 \([-\delta,\delta]\)，则
  \[
  |\mathcal E_g|_{\mathrm{HS}}
  \le \frac{n^{3/2}}2\delta.
  \]

故 Ozuch Lemma 1.4 直接给出

\[
\boxed{
\int_{\partial\Omega}\mathcal E_g(Z,\nu)
=
\frac12\int_\Omega
\langle\mathcal E_g,\mathcal L_Zg\rangle\,d\mu_g.
}
\]

若

\[
J(Z)=\int_\Omega|\mathcal L_Zg|^2\,d\mu_g,
\]

则

\[
\left|
\int_{\partial\Omega}\mathcal E_g(Z,\nu)
\right|
\le
\frac{n^{3/2}}4\,
\delta\,\operatorname{Vol}(\Omega)^{1/2}J(Z)^{1/2}.
\]

四维时为

\[
\boxed{
\left|
\int_{\partial\Omega}\mathcal E_g(Z,\nu)
\right|
\le
2\delta\,\operatorname{Vol}(\Omega)^{1/2}J(Z)^{1/2}.
}
\]

这确实优于直接使用 \(\operatorname{Ric}-g\)，因为后者的散度涉及 \(ds\)。因此，\(\mathcal E_g\) 是目前最自然的 **\(C^0\)-安全 bulk pairing**。

但该恒等式本身不会识别 Ozuch 的二阶系数

\[
\operatorname{Ric}^{(2)}_e(H_2,H^4).
\]

即使精确 Einstein 时 \(\mathcal E_g\equiv0\)，障碍也是把这个“零”在双尺度加权展开中抽取特定阶系数后得到的。要从小 flux 推出 \(R_+v=0\)，必须证明在除以泡尺度后所有余项仍为 \(o(1)\)。这正需要当前缺失的加权正规形或等价尺度估计。

---

## 6. Eguchi–Hanson 代数核验

Step 30 的 EH 展开正确。令 \(x=r^{-4}\)，相对平锥的四个系数为

\[
A,A,B,B,\qquad
A=(1+x)^{-1/2},\quad B=(1+x)^{1/2}.
\]

一阶迹为

\[
-\frac12-\frac12+\frac12+\frac12=0.
\]

事实上

\[
A^2B^2=1,
\]

所以该坐标下体积比是严格等于一，而不只是一阶等于一。这与 Ozuch 的 volume gauge 一致，并解释普通标量 mass/volume flux 为什么看不到各向异性的 \(H^4\)。

Ozuch Theorem 4.6 与 Corollary 4.10 对

\[
H^4=-\frac{\theta_1^-\circ\omega_1^+}{2r^4}
\]

确实给出

\[
\boxed{
R_e^{+,(1)}(H_2)\omega_1^+=0.
}
\]

因此：

- 固定 EH 取向 \(v\) 时，条件是
  \[
  R_+v=0;
  \]
- 只有允许选择某个取向时，才等价于
  \[
  \det R_+=0.
  \]

\(\det R_+=0\) 远弱于 Kähler–Einstein。对于 \(\operatorname{Ric}=g\)，

\[
R_+=W_++\frac13I;
\]

它只说明 \(W_+\) 有一个特征值为 \(-1/3\)，不强迫 Kähler–Einstein 的完整谱型。

---

## 7. 变分向量场方案的具体问题

对固定边界值最小化

\[
J(Z)=\int_\Omega|\mathcal L_Zg|^2
=4\int_\Omega|\delta_g^*Z|^2
\]

确实给出 Euler–Lagrange 方程

\[
\delta_g\delta_g^*Z=0.
\]

但这并不自动产生所需尺度改进：

\[
J(Z_{\min})\le J(Z_{\mathrm{competitor}})
\]

只说明不比已有竞争场差；若竞争场误差本身不足以分辨 \(t^4\) 信号，最小化并不保证获得更强的 \(t\)-阶数。还需要在长锥/EH 环域上一致的 Korn 型估计和精确能量上界。

还必须区分两类模型场：

- 锥旋转是 Killing 场，使用 \(J\) 合理；
- \(r\partial_r\) 是共形 Killing 场，
  \[
  \mathcal L_{r\partial_r}e=2e,
  \]
  因而其完整 \(J\)-能量在平锥上本来就不小。

径向通道更应考虑

\[
\int|(\mathcal L_Zg)^\circ|^2
\]

并固定 dilation 归一化，这才接近 Ozuch Proposition 4.1 中的

\[
(\mathcal L_Xg_b)^\circ.
\]

此外，Ozuch 的场是在 Ricci-flat ALE 上满足

\[
\nabla^*\nabla X=0
\]

的调和场；它与 \(J\)-极小场满足的 \(\delta\delta^*Z=0\) 通过 Bochner Ricci 项相差。在未先获得与 ALE 模型的加权 \(C^2\) 接近前，不能把两者视为可直接替换的同一对象。

JSON 中

\[
\eta^2r^4\ll t^4
\quad\Longleftrightarrow\quad
\eta\ll t^2/r^2
\]

的代数在其假设模型下无误，但该误差模型尚未从真正的 Pohozaev 展开导出；它只能作为尺度警报，不能作为已证明的检测阈值。

---

## 8. 一阶障碍消失并不通向一般存在定理

所给来源仅证明 \(R_+v=0\) 是特定精确 Einstein EH 退化的必要局部条件，并未证明它对一般紧 orbifold resolution 充分。仍需处理：

- Ozuch 已明确指出的高阶障碍；
- orbifold 和 ALE 两侧的非退化性；
- 全局 Einstein 线性算子的核与余核；
- 多奇点及相对泡尺度；
- 一般 \(\Gamma\) 和非 EH ALE 泡；
- gluing 后光滑流形与原 \(M_i\) 的微分同胚识别。

而且，高阶障碍未必造成尺度无关的 \(C^0\) Ricci 缺口。若在 ALE 核心上第一阶方程已可解，取

\[
G_\varepsilon=\varepsilon(g_b+\varepsilon h_2),
\]

则常数缩放不改变协变 Ricci 张量，可能有

\[
\operatorname{Ric}(G_\varepsilon)-\lambda G_\varepsilon
=O(\varepsilon^2)
\]

作为协变张量，从而

\[
\|\operatorname{Ric}(G_\varepsilon)-\lambda G_\varepsilon\|_{\mathrm{op},G_\varepsilon}
=O(\varepsilon).
\]

所以一个非零的更高阶余核分量完全可能阻止精确 Einstein 解，却仍允许 \(C^0\) Ricci 缺陷趋零。由此，不能期待“所有高阶障碍都像第一障碍一样产生 \(O(1)\) operator-norm 缺口”。

这也是该路线最严重的潜在错误假设：**第一障碍可被 \(C^0\) 夹逼检测，并不意味着全部精确可解性障碍都可被同一夹逼检测。**

---

## 9. 最精确的未决对象

当前决定路线成败的数学对象可表述为：

> 对非塌缩四维序列
> \[
> \|\operatorname{Ric}_{g_i}-g_i\|_{L^\infty}\to0,
> \]
> 在某个曲率集中尺度附近，构造兼容 orbifold 与 ALE 两端的规范、测试场或测试张量，并证明一个尺度归一化恒等式
> \[
> t_i^{-a}
> \int_{\Omega_i}\langle\mathcal E_{g_i},\delta^*Z_i\rangle
> =
> c\,\langle R_+(p)v,\cdot\rangle+o(1),
> \]
> 其中左端由 \(L^\infty\) Ricci 缺陷控制，且所有规范、颈部和截断余项在除以 \(t_i^a\) 后仍为 \(o(1)\)。

解决它至少需要下列二者之一：

1. 针对 \(L^\infty\)-近 Einstein 度量的新加权 orbifold/ALE 泡树与颈部衰减定理；或
2. 一个真正绕开双尺度点态正规形的弱投影理论，其紧性足以识别 \(H_2\)-\(H^4\) 交叉项。

即使该对象解决，后续仍需一个独立的“全阶障碍消失 + 全局 gluing + 拓扑恢复”定理，才能推出同一流形上的 Einstein 存在性。

**结论：** Step 30 的规则非塌缩归约、Einstein 张量配对及 EH 一阶障碍代数均可靠；但从 \(C^0\) Ricci 夹逼恢复 Ozuch 障碍仍缺少决定性的尺度正规性，而从一阶障碍消失到实际 Einstein 存在目前更没有来源支持。
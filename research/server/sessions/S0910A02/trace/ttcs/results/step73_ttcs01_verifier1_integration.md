# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 73,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step73_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step73_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step 73 allocation note and the higher-mode flux plan. Check the mathematical plausibility and risks of the proposed general cone higher-obstruction flux identity: the homogeneous degree-l tensor K_l, dual o_l=r^{-(d+2l-2)}K_l, expected Wronskian coefficient -(d+2l-2)/2, TT/radial-gauge cancellation of linearized Ricci gauge terms, operator-norm lower bound, nonlinear/weighted extension cautions, and the decision to prove an isolated cone lemma first while only stating a stratified obstruction-bundle extension. Identify any sign/scaling mistakes or hidden assumptions that Agent2 must fix before treating it as a theorem. Do not decide the whole Yau26 problem; focus on making the next theorem statement correct and useful.

## Integrated Scientific Memo

## 核查结论

拟议中的**线性通量恒等式本身成立**，包括对偶张量与 Wronskian 系数：

\[
o_\ell=r^{-(d+2\ell-2)}K_\ell,
\qquad
\int_A\langle D\Ric_eu,o_\ell\rangle
=-\frac{d+2\ell-2}{2}I_{K_\ell}.
\]

其负号与 `20260912.tex` 中 \(\ell=2\) 的命题 `FND:flux` 一致。但计划中的关键推论

\[
\|D\Ric_eu\|_{\mathrm{op},\infty}
\ge \frac{(d+2\ell-2)I_{K_\ell}}{2LJ_{K_\ell}}
\]

**只对 \(\ell=2\) 正确**。对 \(\ell>2\)，无权 \(L^\infty\) 下界不是 \(L^{-1}\)，而是由内半径控制的幂次量。因而“任意高阶模均迫使 \(\delta L\gtrsim1\)”以及相应指数颈结论不能作为一般高阶定理陈述。

---

## 1. 可严格证明的孤立锥线性引理

令 \(A=\{b<r<R\}/\Gamma\)，其中 \(\Gamma<O(d)\) 在球面上自由作用。必须明确“齐次次数 \(\ell\)”指**笛卡尔分量**满足

\[
K_\ell(rx)=r^\ell K_\ell(x),
\]

而不是协变二张量在 dilation pullback 下的总权重；后者会多出两个指标的权重。

假设非零、\(\Gamma\)-不变的 \(K_\ell\) 满足

\[
\tr K_\ell=0,\qquad
\div K_\ell=0,\qquad
\Delta K_\ell=0,\qquad
K_\ell(x,\cdot)=0 .
\]

令

\[
a=d+2\ell-2,\qquad o_\ell=r^{-a}K_\ell.
\]

则：

\[
\tr o_\ell=0,\qquad o_\ell(x,\cdot)=0,
\]

且

\[
\div(r^{-a}K_\ell)
=r^{-a}\div K_\ell-a r^{-a-2}K_\ell(x,\cdot)=0.
\]

又对任意径向 \(f\),

\[
\Delta(fK_\ell)
=
\left(f''+\frac{d-1+2\ell}{r}f'\right)K_\ell.
\]

取 \(f=r^{-a}\) 得

\[
\Delta o_\ell
=a(a-d-2\ell+2)r^{-a-2}K_\ell=0.
\]

因此

\[
K_\ell=r^\ell Y_\ell(\theta),
\qquad
o_\ell=r^{-(d+\ell-2)}Y_\ell(\theta)
\]

确为同一角模的两条共轭调和 indicial 解。

### 线性 Ricci 的规范项

在约定 \(\Delta=\sum_i\partial_i^2\) 下，

\[
(D\Ric_eu)_{ij}
=-\frac12\Delta u_{ij}
+\frac12(\partial_i\beta_j+\partial_j\beta_i),
\qquad
\beta_j=\partial^ku_{kj}-\frac12\partial_j\tr u.
\]

与 \(o_\ell\) 配对并分部积分时：

- 体项由 \(\div o_\ell=0\) 消失；
- 边界项由 \(o_\ell(\nu,\cdot)=0\) 消失。

所以不要求一般插值 \(u\) 本身 TT；真正需要 TT/radial-null 的是测试张量 \(o_\ell\)。若专取 \(u=\chi(r)K_\ell\)，径向乘子还保持无迹、无散度，规范项本来就逐点为零。

### Wronskian

若 \(u=0\) 于内边界邻域，\(u=K_\ell\) 于外边界邻域，则

\[
\nabla_{\partial_r}K_\ell=\frac{\ell}{r}K_\ell,
\qquad
\nabla_{\partial_r}o_\ell
=-\frac{d+\ell-2}{r}o_\ell.
\]

Green 公式只留下外边界：

\[
\boxed{
\int_A\langle D\Ric_eu,o_\ell\rangle
=-\frac{d+2\ell-2}{2}I_{K_\ell}.
}
\]

这里

\[
I_{K_\ell}
=\int_{S^{d-1}/\Gamma}|K_\ell|_{r=1}^{2}\,d\theta.
\]

故系数和符号均正确；\(\ell=2\) 时恢复 `FND:flux` 的
\(-\frac{d+2}{2}I_K\)。若改用 \(\nabla^*\nabla=-\Delta\)，必须同步改写符号约定。

---

## 2. 必须修正的算子范数下界

在半径 \(r\) 的球面上，

\[
\|o_\ell\|_*
=r^{-(d+\ell-2)}\|K_\ell\|_{*,r=1}.
\]

因此

\[
\int_A\|o_\ell\|_*\,dV
=J_{K_\ell}\int_b^R r^{1-\ell}\,dr,
\]

其中

\[
J_{K_\ell}
=\int_{S^{d-1}/\Gamma}\|K_\ell\|_{*,r=1}\,d\theta.
\]

记

\[
H_\ell(b,R)=
\begin{cases}
\log(R/b),&\ell=2,\\[1mm]
\dfrac{b^{2-\ell}-R^{2-\ell}}{\ell-2},&\ell>2.
\end{cases}
\]

算子范数—核范数对偶给出的正确无权估计是

\[
\boxed{
\|D\Ric_eu\|_{\mathrm{op},\infty}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2J_{K_\ell}H_\ell(b,R)}.
}
\]

所以：

- \(\ell=2\)：\(H_2=L\)，得到原稿的 \(L^{-1}\) 临界下界；
- \(\ell>2\)、\(b\ll R\)：
  \[
  H_\ell(b,R)\sim\frac{b^{2-\ell}}{\ell-2},
  \]
  因而
  \[
  \|D\Ric_eu\|_{\infty}
  \gtrsim b^{\ell-2},
  \]
  并不迫使 \(\delta L\gtrsim1\)。

直接取 \(u_b=\chi(r/b)K_\ell\) 可验证此尺度：

\[
D\Ric_eu_b
=-\frac12\left(
\chi_b''+\frac{d-1+2\ell}{r}\chi_b'
\right)K_\ell,
\qquad
\|D\Ric_eu_b\|_\infty=O(b^{\ell-2}).
\]

这排除了 \(\ell>2\) 时统一 \(1/L\) 下界的可能。

存在一个正确的加权对数版本：

\[
\int_A r^{\ell-2}\|o_\ell\|_*\,dV=LJ_{K_\ell},
\]

故

\[
\boxed{
\sup_A r^{2-\ell}\|D\Ric_eu\|_{\mathrm{op}}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2LJ_{K_\ell}}.
}
\]

但 Yau–26 的假设控制的是无权 Ricci 算子范数，因此该加权结论不能直接替代 \(\ell=2\) 的指数颈机制。

**结论：**普通 \(C^0\) Ricci pinching 下，二次模是唯一的对数临界多项式模。高阶模若无额外“不得在内端集中过渡”的持续性假设，只给幂次必要条件。

---

## 3. 对“高阶障碍必要性”的正确表述

计划中的

\[
\delta_iL_i\gtrsim c(K_\ell,d,\ell)
\]

只能无条件用于 \(\ell=2\)。因此：

- 对 \(\ell=2\)，非零 mismatch 可推出
  \[
  \delta_iL_i\ge c-o(1),
  \]
  并在 \(L_i\asymp|\log t_i|\) 时得到
  \[
  t_i\le e^{-c/\delta_i}.
  \]

- 对 \(\ell>2\)，由孤立锥引理只能推出
  \[
  \delta_i\gtrsim c\,b_i^{\ell-2}
  \]
  （再加端点及非线性误差），这允许该模在 \(\delta_i\to0\) 时持续存在。不能由此推出指数小尺度。

若希望恢复某种 \(L^{-1}\) 结论，必须明确附加例如：

1. 控制加权范数 \(\sup r^{2-\ell}|\Ric-\lambda g|\)；
2. 或证明 mismatch 在整个对数颈上以尺度归一化幅度持续存在，不能集中在 \(r\sim b\)；
3. 或从完整耦合障碍方程导出额外传播估计。

这些都不是当前孤立通量恒等式的后果。

---

## 4. 非线性和加权扩展目前不能照搬

计划提出

\[
\mathcal E_\ell(v)
=\int_A r^{-d-2\ell+4}|Dv|^2
\]

作为高阶能量。它对纯 \(v\sim r^\ell\) 模确有合理的形式缩放，但尚不足以支配实际非线性配对。一次分部积分后，典型最高阶项产生

\[
\int_A |Dv|^2|o_\ell|
\sim
\int_A |Dv|^2r^{-d-\ell+2}.
\]

与拟议权重相比，两者只在 \(\ell=2\) 精确一致。对 \(\ell>2\)，必须保留额外内端 \(b\)-幂或改用更强权重；不能直接写成 manuscript 的 \(\ell=2\) 能量式。

此外必须区分：

- 总扰动通常从 \(r^2\) 开始，不可能整体满足 \(O(r^\ell)\)；
- \(v_\ell\) 必须是在完整低阶 tower subtraction 后分离出的第 \(\ell\) 模；
- 二次背景与 \(v_\ell\) 的交叉项通常为 \(O(R^2)\)，而纯 \(v_\ell^2\) 项可为 \(O(R^\ell)\)；
- 对归一化 Einstein 算子还存在
  \[
  D(\Ric-\lambda g)_e v=D\Ric_ev-\lambda v,
  \]
  与 \(o_\ell\) 的积分贡献一般为 \(O(R^2)\)；
- Wronskian 含 \(u\) 与 \(\partial_ru\)，故端点误差至少需要相应模投影的 \(C^1\) 控制，而非仅 \(C^0\) 匹配。

因此下一版可以给出“条件性非线性模板”，但不宜宣称一般高阶 energy-flux theorem 已建立。

---

## 5. “\(K_\ell\) 是高阶障碍”所需的额外假设

孤立锥引理只处理满足四个张量条件的抽象模式。把它解释为 Biquard–Ozuch 高阶障碍，还需解决：

1. **模式存在性。**  
   对指定 \((d,\Gamma,\ell)\)，非零 \(\Gamma\)-不变 TT、调和、radial-null 子空间可能为空。必须将 \(K_\ell\ne0\) 明列为假设，并另作表示论识别。

2. **规范与坐标不变量。**  
   二次纯 Weyl 正规张量具有明确几何意义；高阶 Taylor 系数会被高阶坐标变化改变。需固定 Bianchi slice、端点 marking，并证明所取投影模纯规范不变。

3. **低阶 tower subtraction。**  
   高阶 Einstein 方程含低阶 jet 的乘积强迫项。\(K_\ell\) 应是减去完整形式塔后的齐次残差，而不是原始 Taylor 系数。

4. **共振对数项。**  
   若出现 \(r^\ell\log r\)，
   \[
   \partial_r(r^\ell\log r)
   =r^{\ell-1}(\ell\log r+1),
   \]
   会改变边界通量；纯齐次 Wronskian 公式不能直接套用。

5. **“障碍阶数”与 \(\ell\) 的对应。**  
   Biquard/Ozuch 的 obstruction order、ALE Jacobi 场衰减阶及锥角模次数并非自动相同。必须先给出 mode-identification theorem，不能在定理中把三者直接等同。

6. **维数范围。**  
   线性欧氏锥计算本身并不显然需要 \(d\ge4\)，但几何应用的 ALE/codimension-four背景需要。定理若保留 \(d\ge4\)，应说明这是应用范围而非 Wronskian 代数的必要条件。

---

## 6. 分层版本应只作为目标陈述

先证明孤立锥引理、暂不声称一般分层 ALE 束定理，是正确决策。

在精确积 \(S^m\times A^d\) 且 \(K_\ell\) 沿 \(S\) 平行时，可以把孤立恒等式沿 \(S\) 积分；这是可证明的中间情形。但若 \(K_\ell=K_\ell(y)\)，完整算子包含

\[
\Delta_{\mathrm{full}}
=\Delta_{\mathrm{normal}}+\Delta_S
\]

以及 normal connection、第二基本形式和混合分量，因而出现

\[
-\frac12\int_{S\times A}
\langle\Delta_SK_\ell(y),o_\ell(y)\rangle
\]

等项。正确对象是 stratum 上 obstruction bundle 的椭圆方程，而非单纯积分障碍或仅有

\[
R_{\mathrm{normal},\pm}(y)\zeta(y)=0.
\]

Step 53 的局部性警告是正确的，但应表述得更精确：点态 pinching 控制的是**包含切向导数在内的完整束值方程**。若未假设 \(\zeta\) 平行或慢变，非零代数 normal coefficient 可能与切向项抵消，不能单独断言其在每一点必须为零。

分层目标至少应假设：

- 固定 isotropy type 的光滑 stratum；
- 明确的 obstruction orbibundle 与 normal connection；
- 一致 transverse ALE charts 和 markings；
- fiberwise tower subtraction；
- obstruction section 的协变导数控制；
- 足以把沿 stratum 的积分控制升级为局部控制的椭圆估计；
- bubble trees 情形下逐层尺度的嵌套 subtraction，而不是单颈公式。

---

## 建议采用的下一条定理

可立即严格陈述的结果应限于：

\[
\int_A\langle D\Ric_eu,o_\ell\rangle
=-\frac{d+2\ell-2}{2}I_{K_\ell},
\]

\[
\|D\Ric_eu\|_{\infty}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2J_{K_\ell}H_\ell(b,R)},
\]

以及

\[
\sup_A r^{2-\ell}\|D\Ric_eu\|_{\infty}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2LJ_{K_\ell}}.
\]

并明确分成：

- \(\ell=2\)：无权对数临界 flux，可进入 \(\delta L\) 与指数颈必要性；
- \(\ell>2\)：无权幂次 flux；其几何障碍解释、非线性估计及分层 bundle 推广仍需额外结构。

这是当前证据支持的最强且不会误导后续 Yau–26 分析的版本。
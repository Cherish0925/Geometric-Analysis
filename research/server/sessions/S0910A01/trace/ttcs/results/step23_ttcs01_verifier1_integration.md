# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 23,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step23_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step23_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the central structural claim in the Step 23 cooperative persistence theorem for the four-dimensional negative LeBrun/Ishida-LeBrun cutoff-flow route. The claim: for the normalized cutoff flow ∂_t g = -2χ²(Ric+g) on a closed four-manifold, when the q=2 curvature energy H_{2,α} = ∫ η_α² F² is tested against η_α² H (the testing function), and the reaction ∫ η_α² aF³ is absorbed using the Sobolev variable v = η_α a^{1/2} F, the resulting gradient integral ||∇v||² decomposes into the α-component dissipation D_{2,α} plus r⁻² H-type localization terms, all supported within U_α. Specifically: (1) The gradient ∇(η_α a^{1/2} F) = η_α a^{1/2}∇F + η_α (∇a/(2a^{1/2}))F + a^{1/2}F ∇η_α has all three contributions supported in supp(η_α) ⊂ U_α. (2) The term η_α² a|∇F|² is bounded by C·D_{2,α}. (3) The term η_α²(|∇a|²/a)F² ≤ Cr⁻² H_{2,α}. (4) The term a|∇η_α|²F² ≤ Cr⁻² ∫_{U_α}F². (5) Therefore the Sobolev inequality ||v||₄² ≤ A_α²(CD_{2,α} + Cr⁻²∫_{U_α}F²) involves ONLY the α-component dissipation, no neighbor dissipation Z_β. (6) After Hölder R ≤ γ_α(D + r⁻²H) and absorption into cD, the vector inequality is S' + cZ ≤ (b/r²)BS with ε=0 (no εBZ term). Check whether any term was missed: inverse metric variation in F, measure evolution, Hessian-a integrations by parts, the lower-order aFq term from normalization, or overlap contributions to ∫_{U_α}F². Also check: does the cooperative comparison for the resulting S'≤(b/r²)BS give componentwise Gronwall with constants independent of component count?

## Integrated Scientific Memo

## 验证结论

**核心“耗散局部性”结论成立，但 Step 23 当前写法中的完整合作系统尚未被证明。**

更精确地说：

\[
H'_{2,\alpha}+cD_{2,\alpha}
\le C r^{-2}\int_{U_\alpha}F^2
\]

在吸收三次反应项后，确实只含 \(\alpha\)-分量耗散 \(D_{2,\alpha}\)，不会产生任何邻居耗散 \(D_{2,\beta}\)。因此 PDE 层面的结构是

\[
\varepsilon=0.
\]

但从这个局部不等式推到

\[
S'+cZ\le \frac b{r^2}BS
\]

还需要把裸积分 \(\int_{U_\alpha}F^2\) 和 Hölder 因子中的局部 \(L^2\) 范数控制为已定义的分量能量。Step 23 所称“由有界重叠得到”

\[
\int_{U_\alpha}F^2\le\sum_{\beta\sim\alpha}H_{2,\beta}
\tag{*}
\]

并不成立；其给定球族实际上也不具备所需覆盖性质。这是目前唯一实质性的结构缺口。

---

## 1. Sobolev 梯度只含 \(\alpha\)-耗散

应写 \(a=\chi^2\) 且直接使用

\[
v=\eta_\alpha\chi F,
\]

以避免在 \(\chi=0\) 处写出形式上的 \(\nabla a/\sqrt a\)。有

\[
\nabla v
=\eta_\alpha\chi\nabla F
+\eta_\alpha F\nabla\chi
+\chi F\nabla\eta_\alpha .
\]

所有项均支撑于 \(\operatorname{supp}\eta_\alpha\subset U_\alpha\)。由
\(|x+y+z|^2\le3(|x|^2+|y|^2+|z|^2)\)，

\[
\int|\nabla v|^2
\le
3\int\eta_\alpha^2a|\nabla F|^2
+3\int\eta_\alpha^2|\nabla\chi|^2F^2
+3\int a|\nabla\eta_\alpha|^2F^2.
\tag{1}
\]

Step 23 中这里写系数 \(2\) 对三个任意向量不正确，但改成 \(3\) 不影响结构。

因为

\[
\nabla F
=\frac{\langle\operatorname{Rm},\nabla\operatorname{Rm}\rangle}{F},
\qquad
|\nabla F|\le|\nabla\operatorname{Rm}|,
\]

故

\[
\int\eta_\alpha^2a|\nabla F|^2\le D_{2,\alpha}.
\tag{2}
\]

又由 Whitney/cutoff 界

\[
|\nabla\chi|\le Cr^{-1},
\qquad
|\nabla\eta_\alpha|\le Cr^{-1},
\qquad 0\le a\le1,
\]

得到

\[
\int\eta_\alpha^2|\nabla\chi|^2F^2
=
\frac14\int\eta_\alpha^2\frac{|\nabla a|^2}{a}F^2
\le Cr^{-2}H_{2,\alpha},
\tag{3}
\]

以及

\[
\int a|\nabla\eta_\alpha|^2F^2
\le Cr^{-2}\int_{U_\alpha}F^2.
\tag{4}
\]

于是局部 Sobolev 不等式给出

\[
\boxed{
\|v\|_4^2
\le CA_\alpha^2
\left(
D_{2,\alpha}
+r^{-2}\int_{U_\alpha}F^2
\right).}
\tag{5}
\]

这里没有任何 \(D_{2,\beta}\)。

---

## 2. 三次反应项的吸收

四维中

\[
R_{2,\alpha}
=\int\eta_\alpha^2aF^3
=\int_{U_\alpha}Fv^2
\le \|F\|_{L^2(U_\alpha)}\|v\|_4^2.
\]

令

\[
\gamma_\alpha=A_\alpha^2\|F\|_{L^2(U_\alpha)},
\]

则由 (5)

\[
R_{2,\alpha}
\le C\gamma_\alpha
\left(
D_{2,\alpha}
+r^{-2}\int_{U_\alpha}F^2
\right).
\tag{6}
\]

因此若精确 \(q=2\) 能量不等式的好耗散系数为 \(c_0\)，所需小量条件是

\[
C\gamma_\alpha\le \frac{c_0}{2},
\]

而不应省略常数 \(C\)。吸收后得到

\[
\boxed{
H'_{2,\alpha}+\frac{c_0}{2}D_{2,\alpha}
\le Cr^{-2}\int_{U_\alpha}F^2,}
\tag{7}
\]

在 \(r\le1\) 的约定下；一般尺度下右端应写
\(C(1+r^{-2})\int_{U_\alpha}F^2\)。

这严格验证了所要求的关键点：反应吸收使用的是与左端完全相同权重的 \(D_{2,\alpha}\)，所以不会出现 \(\varepsilon BZ\)。

---

## 3. 所列几何变分项均不会产生邻居耗散

Step 20 给出的张量账本足以验证其结构，但尚未给出精确系数。

- **逆度量变分：**
  \(\partial_tg^{-1}=2aE^\sharp\)，故 \(\partial_t|\operatorname{Rm}|^2\) 中相应项为
  \[
  aE*\operatorname{Rm}*\operatorname{Rm},
  \]
  由 \(|E|\le CF\) 控制为 \(CaF^3\)。

- **体积元变分：**
  \[
  \partial_t d\mu=-a\,\operatorname{tr}E\,d\mu,
  \]
  对 \(H_{2,\alpha}\) 的贡献同样至多为
  \(C\int\eta_\alpha^2aF^3\)。

- **\(\nabla^2a\) 分部积分：**代表项
  \[
  \int\eta_\alpha^2\operatorname{Rm}*(\nabla^2a)*E
  \]
  分部积分后，结合
  \[
  |E|\le CF,\qquad
  |\nabla E|\le C|\nabla\operatorname{Rm}|,
  \]
  由 Young 不等式控制为
  \[
  \varepsilon D_{2,\alpha}
  +C_\varepsilon\int\eta_\alpha^2
       \frac{|\nabla a|^2}{a}F^2
  +C\int a|\nabla\eta_\alpha|^2F^2.
  \]
  导数始终落在 \(\eta_\alpha\) 支撑内。

- **归一化产生的低阶 \(aF^2\) 项：**
  它是零阶对角项，没有梯度。若 \(r\le1\)，可并入
  \(Cr^{-2}\int_{U_\alpha}F^2\)；否则合作矩阵额外增加一个 \(CI\)。

因此没有遗漏任何能产生 \(D_{2,\beta}\) 的项。需要精确张量计算来确定 \(c_0,C,b\)，但“\(\varepsilon=0\)”不依赖这些系数。

---

## 4. Step 23 中真正未闭合的覆盖问题

“有界重叠”只给出上界

\[
\sum_\beta\mathbf 1_{U_\beta}\le N,
\]

并不推出所需下覆盖界

\[
\mathbf1_{U_\alpha}
\le C\sum_{\beta\sim\alpha}\eta_\beta^2.
\tag{8}
\]

Step 23 设中心距离至少 \(10r\)，而

\[
U_\alpha=B_{5r}(p_\alpha),\qquad
\operatorname{supp}\eta_\alpha\subset B_{4r}(p_\alpha).
\]

于是内支撑互不相交，\(U_\alpha\) 至多相切；环带

\[
B_{5r}(p_\alpha)\setminus B_{4r}(p_\alpha)
\]

不被任何所定义的 \(H_{2,\beta}\) 控制。把 \(F^2\) 集中在该环带即可否定 \((*)\)。

同一问题也影响

\[
\gamma_\alpha=A_\alpha^2\|F\|_{L^2(U_\alpha)}:
\]

由 \(H_{2,\alpha}=\int\eta_\alpha^2F^2\) 不能上控
\(\int_{U_\alpha}F^2\)。所以当前的 first-exit 量 \(\Gamma\) 尚不能保证吸收小量条件。

充分的修正条件是引入外 cutoff/覆盖能量 \(\xi_\beta\)，满足

\[
\mathbf1_{U_\alpha}
\le C_0\sum_{\beta\sim\alpha}\xi_\beta^2,
\tag{9}
\]

从而

\[
\int_{U_\alpha}F^2
\le C_0\sum_{\beta\sim\alpha}
\int\xi_\beta^2F^2.
\tag{10}
\]

同时令用于 Sobolev 的内 cutoff \(\eta_\alpha\) 满足
\(\xi_\alpha\equiv1\) 于 \(\operatorname{supp}\eta_\alpha\)。那么

\[
\|F\|_{L^2(\operatorname{supp}\eta_\alpha)}
\le \|\xi_\alpha F\|_2,
\]

而 Sobolev 梯度仍只作用于
\(v=\eta_\alpha\chi F\)，故仍然只有 \(\alpha\)-局部耗散。还需明确一个有限、不无限外扩的 buffer 层级，使外能量自身的演化闭合；这正是完整合作系统尚缺的几何账本。

---

## 5. 一旦覆盖闭合，合作 Gronwall 与分量数无关

若修正后的能量满足

\[
S_\alpha'+cZ_\alpha
\le \frac b{r^2}\sum_\beta B_{\alpha\beta}S_\beta,
\qquad
B_{\alpha\beta}\ge0,\qquad
\sup_\alpha\sum_\beta B_{\alpha\beta}\le L,
\tag{11}
\]

则令 \(m(t)=\max_\alpha S_\alpha(t)\)，在最大分量处有

\[
D^+m(t)\le \frac{bL}{r^2}m(t).
\]

故

\[
\boxed{
S_\alpha(t)\le
e^{bLt/r^2}\max_\beta S_\beta(0).}
\tag{12}
\]

在 \(T=\theta r^2\) 时，

\[
\Gamma(T)\le e^{bL\theta/2}\Gamma(0).
\tag{13}
\]

常数只依赖行和界 \(L\)，与分量总数无关。若有额外 \(CI\) 低阶项，则指数变为
\(bLt/r^2+Ct\)，仍与分量数无关。

由 (11) 积分并使用 (12)，还可得

\[
c\int_0^tZ_\alpha(s)\,ds
\le e^{bLt/r^2}\max_\beta S_\beta(0),
\tag{14}
\]

同样是逐分量、与分量数无关的界。若要控制总和即 \(\ell^1\) 能量，仅有行和界不够，还需统一列和界；对称有限邻接关系和双向 \(A_\alpha/A_\beta\) 可比性可提供该条件。

这里 \(A_\alpha\) 应取为整个时间区间有效的固定 Sobolev 上界。若令其随时间变化，则

\[
S_\alpha'=A_\alpha^4H'_{2,\alpha}
+4\frac{A_\alpha'}{A_\alpha}S_\alpha
\]

还会多出一项，须另行控制。

---

## 最终判定

1. 任务中的 (1)–(5) 在常数修正后成立，且只出现 \(D_{2,\alpha}\)。
2. 逆度量、测度、Hessian-\(a\) 和归一化项均不会产生邻居耗散。
3. 因此 PDE 吸收层面的 **\(\varepsilon=0\) 已验证**。
4. Step 23 当前的球族并不能把 \(\int_{U_\alpha}F^2\) 或 \(\gamma_\alpha\) 控制为其 \(H_{2,\beta}\)；故其展示的完整矩阵不等式尚未由现有定义推出。
5. 一旦补上明确的内/外 cutoff 覆盖支配及有限 buffer 闭合，合作 Gronwall 的逐分量常数确实与分量总数无关。
6. 配套 Python 脚本只检验了预设矩阵系统后的数值 ODE，不验证张量局部性；其 resolvent 示例参数还满足
   \(1-0.1/\rho<0\)，与脚本声称的正性不符。
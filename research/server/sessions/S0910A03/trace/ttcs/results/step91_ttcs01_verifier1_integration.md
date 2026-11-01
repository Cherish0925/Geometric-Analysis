# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 91,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step91_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step91_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following geometric claim about free-T² metrics with twist on a 4-manifold. Setting: (X⁴,g) complete, free isometric T²-action, g = γ_B + G_ab(dξ^a + A^a)(dξ^b + A^b), G = e^σ M with det M = 1, ρ = e^σ. Connection curvature F^a = dA^a = f^a vol(γ_B). Twist energy Q = (1/2)G_{ab}f^af^b. Orbit-shape map U: B → H² with e = |dU|². Defect E = Ric_g + 3g, ‖E‖_op ≤ δ.

Claim 1 (twist contribution to |II|²): Let Σ = π⁻¹(C) be an invariant hypersurface, C a curve in the base B with tangent T and normal ν. In the orthonormal frame {e_T, e₁, e₂, e_ν}, the second fundamental form satisfies:
  |II|² = |II|²_OT + Q
where |II|²_OT = κ² + (1/2)h_ν² + (1/2)e_ν (with κ = geodesic curvature, h_ν = ∂_ν σ, e_ν = |dU(ν)|²) and the twist contribution is Q through the off-diagonal terms II(e_T, e_a).

Verify: From the Kaluza-Klein/O'Neill formulas, II(e_T, e_a) = (1/2)G_{aa}^{1/2}f^a (in orthonormal orbit frame, for diagonal G). Then 2∑_a II(e_T,e_a)² = (1/2)G_{ab}f^af^b = Q.

Claim 2 (separator stability): If Σ is minimal and area-minimizing in its homology class, then ∫_Σ(|II|² + Ric(ν,ν))dvol ≤ 0 (second variation with φ=1). Since Ric(ν,ν) = -3 + E(ν,ν) ≥ -3 - δ:
  ⟨|II|²⟩_Σ ≤ 3 + δ
and hence Q_C := ⟨Q⟩_Σ ≤ 3 + δ.

Claim 3 (raised floor): The separator identity from Step 88 gives ⟨e_s⟩ = 12 - 2⟨D⟩ + 2⟨|II|²⟩ + ⟨h²⟩ where h = (log ρ)_T. With |II|² = |II|²_OT + Q, this becomes ⟨e_s⟩ ≥ 12 - 8δ + 2Q_C.

Claim 4 (resolvent-floor obstruction): At the exact OT threshold δ* ≈ 0.246 where the Step 87 ceiling B(δ*) = 12 - 8δ*, any Q_C > 0 would make the floor strictly exceed the ceiling, ASSUMING the ceiling still applies. However, the ceiling B(δ) was derived under Q=0 (exact OT). With Q>0, the Bochner identity is modified and the ceiling may increase. The key question is whether the ceiling increases faster or slower than the floor.

Please verify all four claims, check the O'Neill formula for II(e_T, e_a) carefully, and assess whether the resolvent-floor argument genuinely constrains Q_C or whether the modified ceiling with Q>0 invalidates it.

## Integrated Scientific Memo

## 核验结论

在给定约定下，Claims 1–3 成立；Claim 1 中混合分量的**符号依赖定向及水平提升约定**，但其平方贡献无歧义。Claim 4 的条件判断也正确：若错误地沿用 OT 上界，则在 \(\delta=\delta_*\) 会推出 \(Q_C=0\)；但 \(Q>0\) 时该上界并不适用。现有含扭曲 Bochner/预解式估计增长快于分离面下界，因此目前不能从这一论证得到超出稳定性
\[
Q_C\le 3+\delta
\]
的约束。

---

### 1. 混合第二基本形式及 \(Q\) 的系数

令 \(K_a=\partial_{\xi^a}\) 为垂直基本场，\(\bar T,\bar\nu\) 为 \(T,\nu\) 的水平提升，并设
\[
F^a(T,\nu)=\varepsilon f^a,\qquad
\varepsilon=\operatorname{vol}_{\gamma_B}(T,\nu)\in\{\pm1\}.
\]
对约定 \(\theta^a=d\xi^a+A^a\)，有
\[
[\bar T,\bar\nu]^{\mathcal V}
=-F^a(T,\nu)K_a=-\varepsilon f^aK_a.
\]
Koszul 公式给出
\[
2g(\nabla_{\bar T}\bar\nu,K_a)
=g(K_a,[\bar T,\bar\nu])
=-\varepsilon G_{ab}f^b,
\]
故
\[
\boxed{\operatorname{II}(\bar T,K_a)
=-\frac{\varepsilon}{2}G_{ab}f^b.}
\]
若 \(G\) 对角化且 \(e_a=K_a/\sqrt{G_{aa}}\)，则
\[
\operatorname{II}(\bar T,e_a)
=-\frac{\varepsilon}{2}\sqrt{G_{aa}}\,f^a.
\]
题中正号对应相反的 \((T,\nu)\) 定向或水平括号约定；范数结论不受影响。

在任意垂直正交标架中，
\[
\sum_{\alpha=1}^2\operatorname{II}(\bar T,e_\alpha)^2
=\frac14G_{ab}f^af^b.
\]
因为对称二阶张量范数同时计数 \((T,e_\alpha)\) 与
\((e_\alpha,T)\)，所以
\[
\boxed{
2\sum_\alpha\operatorname{II}(\bar T,e_\alpha)^2
=\frac12G_{ab}f^af^b=Q.}
\]

其余分量不含 \(F\)。垂直形算子由
\[
S_\nu=\frac12G^{-1}\partial_\nu G
=\frac12\bigl(h_\nu I+M^{-1}\partial_\nu M\bigr)
\]
控制，在所用归一化
\[
e_\nu=\frac12\operatorname{tr}
  \bigl((M^{-1}\partial_\nu M)^2\bigr)
\]
下，
\[
|S_\nu|^2=\frac12h_\nu^2+\frac12e_\nu.
\]
连同 \(\operatorname{II}(T,T)=\pm\kappa\)，得到
\[
\boxed{
|\operatorname{II}|^2
=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q.}
\]
扭曲只进入无迹混合分量，因此不改变平均曲率。

---

### 2. 稳定性估计

对闭、双侧、稳定的极小超曲面，
\[
\int_\Sigma\left(
|\nabla_\Sigma\phi|^2-
\bigl(|\operatorname{II}|^2+\operatorname{Ric}(\nu,\nu)\bigr)\phi^2
\right)d\mu_\Sigma\ge0.
\]
取 \(\phi\equiv1\)，得
\[
\int_\Sigma
\bigl(|\operatorname{II}|^2+\operatorname{Ric}(\nu,\nu)\bigr)d\mu_\Sigma
\le0.
\]
由
\[
\operatorname{Ric}(\nu,\nu)=-3+E(\nu,\nu),
\qquad E(\nu,\nu)\ge-\delta,
\]
推出
\[
\boxed{\langle|\operatorname{II}|^2\rangle_\Sigma\le3+\delta.}
\]
因此
\[
\boxed{
\left\langle
\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q
\right\rangle_\Sigma\le3+\delta,}
\qquad
\boxed{Q_C\le3+\delta.}
\]
另有有用推论
\[
\boxed{\langle e_\nu\rangle_C
\le6+2\delta-2Q_C.}
\]

完整同调面积最小性比所需条件更强。Step 88 的加权长度最小曲线仅保证对不变变分稳定，但 \(\phi=1\) 正是不变法向变分，已足以推出上述积分不等式。并且
\[
d\mu_\Sigma=\rho\,ds\,d\xi^1d\xi^2,
\]
故这里的超曲面平均与 \(C\) 上的 \(\rho\)-加权平均一致。

---

### 3. 含扭曲的 raised floor

连接限制到一维曲线 \(C\) 后曲率拉回为零；局部可规范消去，可能存在的平坦环流不影响内蕴标量曲率。因此 Step 88 的内蕴公式保持不变：
\[
\langle R_\Sigma\rangle
=\frac12\bigl(\langle h_T^2\rangle-\langle e_s\rangle\bigr),
\qquad h_T=(\log\rho)_T.
\]
注意 \(h_T\) 与上面的法向导数 \(h_\nu=\partial_\nu\sigma\) 不同。

极小性及 Gauss 方程给出
\[
\langle e_s\rangle
=12-2\langle D\rangle
 +2\langle|\operatorname{II}|^2\rangle
 +\langle h_T^2\rangle,
\]
其中
\[
D=\operatorname{tr}E-2E(\nu,\nu),\qquad |D|\le4\delta.
\]
代入第二基本形式分解：
\[
\begin{aligned}
\langle e_s\rangle
={}&12-2\langle D\rangle
 +2\langle\kappa^2\rangle+\langle h_\nu^2\rangle
 +\langle e_\nu\rangle\\
&+2Q_C+\langle h_T^2\rangle .
\end{aligned}
\]
故
\[
\boxed{\langle e_s\rangle
\ge12-8\delta+2Q_C,}
\qquad
\boxed{\sup_Be\ge12-8\delta+2Q_C.}
\]
所以 Claim 3 正确，而且 \(2Q_C\) 的系数是精确的。

---

### 4. 预解式上界不能直接约束 \(Q_C\)

若额外假设 OT 上界仍成立，
\[
\sup_Be\le\mathcal B(\delta),
\]
则形式上有
\[
Q_C\le
\frac{\mathcal B(\delta)-12+8\delta}{2}.
\]
在
\[
\delta_*=0.246249763690668\ldots,\qquad
\mathcal B(\delta_*)=12-8\delta_*
\approx10.0300019,
\]
这确实会迫使 \(Q_C=0\)。

但这是一个无效的无扭曲外推。含扭曲时
\[
\tau_\sigma(U)=-\nabla_{\mathbb H^2}Q+Z,
\]
且基底 drift curvature 中的 \(+Qe\) 与目标势微分产生的
\(-Qe\) 点态抵消。剩余 Bochner 恒等式包含 \(Q^2\)、电荷梯度项及散度通量，不能只由 \(\delta\) 控制。

当前可用的粗略比较为
\[
12+2Q_C-8\delta\le
\left[
\frac{2(Q_++2\delta)}{\sqrt{3-Q_-+\delta}}
+
\sqrt{
2(3-Q_-+\delta)
+\frac{5(Q_++2\delta)^2}{3-Q_-+\delta}}
\right]^2,
\]
其中
\[
Q_-=\inf_BQ,\qquad Q_+=\sup_BQ.
\]
对具有 exact OT 开端的情形，\(Q_-=0\)，但稳定性只控制分离面平均 \(Q_C\)，并不控制 \(Q_+\).

更具体地，在 \((\delta_*,Q_+)=(\delta_*,0)\) 处，右端对 \(Q_+\) 的导数约为
\[
8.86,
\]
而下界对 \(Q_C\) 的斜率仅为 \(2\)。即使作最有利但通常不成立的识别 \(Q_+=Q_C\)，现有“上界”也比下界增长更快；大 \(Q_+\) 时右端更呈二次增长。因此该比较不会在 OT 临界点附近强迫 \(Q_C=0\)。

最终严格结论只有
\[
\boxed{Q_C\le3+\delta},
\qquad
\boxed{\sup_Be\ge12-8\delta+2Q_C.}
\]
要得到更强限制，需要新的传输或预解式定理，把 \(Q_+\)（或 Green 核加权的扭曲能量）控制为 \(Q_C\) 的函数；现有材料没有这种控制。Step 90 的局部径向计算还表明，大而局域化的 \(Q_+\) 可经面积膨胀迅速红移，因此不能期待仅凭混合 Ricci 小量及一个 OT 端推出 \(Q_+=O(\delta)\)。

最后，`step91_flat_slice_and_stability.json` 中
`step87_ceiling: 12.0` 是数值记录错误：在 \(\delta=0.246\) 时约为 \(10.025139\)，在精确 \(\delta_*\) 时约为 \(10.030002\)。其中把 OT ceiling 与含扭曲 floor 结合后列出的 `Q_C_max_resolvent = 0` 不构成有效数学结论。
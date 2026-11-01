# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 1,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step1_ttcs01_sub5_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step1_ttcs01_sub6_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the dossier's central reduction Q_n iff P_n^+ or P_n^- and search for hidden quantifier, scaling, sign, or vacuity issues. Then critically assess what low-dimensional cases are already settled and what a full refutation actually requires. Check especially whether arbitrary intervals can be vacuous, how homothetic rescaling acts on Ricci as a (0,2)-tensor and on the Ricci endomorphism, and whether n=2,3 yield complete positive results under the stated smooth closed connected conventions.

## Integrated Scientific Memo

# 核验结论

## 1. 核心归约成立，但应区分“全局非空”与“逐流形空前提”

固定维数 \(n\)，令

\[
Q_n:\ \exists a<b\ \forall M^n\forall g,\quad
ag\le \Ric_g\le bg\Longrightarrow \Ein(M)\neq\varnothing,
\]

以及

\[
P_n^\sigma:\ \exists \varepsilon\in(0,1)\ \forall M^n\forall g,\quad
\delta_\sigma(g)\le\varepsilon\Longrightarrow \Ein(M)\neq\varnothing,
\qquad \sigma=\pm1.
\]

则确有

\[
\boxed{Q_n\iff P_n^+\vee P_n^-}.
\]

没有隐藏的 \(M\)-依赖、度量依赖或统一符号要求；由 \(Q_n\) 提取出的符号可随维数改变。

另外，因为结论 \(\Ein(M)\neq\varnothing\) 不依赖输入 \(g\)，对固定 \(M\) 有

\[
\forall g\,[B(M,g)\Rightarrow \Ein(M)]
\iff
[(\exists g\,B(M,g))\Rightarrow \Ein(M)].
\]

因此在当前结论形式下，“每个满足夹逼的度量”与“若 \(M\) 存在一个满足夹逼的度量”没有实质量词差异。不过，对某个特定 \(M\)，夹逼度量集合仍可能为空；此时该 \(M\) 对应的蕴含确实真空成立。

---

## 2. 缩放公式及归一化无误

对常数 \(c>0\)，若 \(\widetilde g=cg\)，则 Levi–Civita 联络不变，因此

\[
\Ric_{\widetilde g}=\Ric_g
\]

是作为 \((0,2)\)-张量的等式；但 Ricci 端同态满足

\[
A_{\widetilde g}
=\widetilde g^{-1}\Ric_{\widetilde g}
=c^{-1}A_g.
\]

故

\[
ag\le \Ric_g\le bg
\iff
\frac ac\,\widetilde g\le \Ric_{\widetilde g}
\le \frac bc\,\widetilde g.
\]

若 \(\Ric_g=\lambda g\)，则

\[
\Ric_{cg}=\frac{\lambda}{c}(cg),
\]

所以 Einstein 常数除以 \(c\)，符号不变。

算子范数还有一个易混点：对固定端同态 \(T\)，

\[
\|T\|_{\mathrm{op},cg}=\|T\|_{\mathrm{op},g},
\]

但 \(A_{cg}=c^{-1}A_g\)，因而一般

\[
\delta_\sigma(cg)
=\sup_M\|c^{-1}A_g-\sigma I\|_{\mathrm{op},g}
\ne c^{-1}\delta_\sigma(g).
\]

底稿的证明没有犯这一错误，它使用的是特征值区间的正确缩放。

---

## 3. 两个方向的严格验证

### \(P_n^\sigma\Rightarrow Q_n\)

自伴随谱刻画给出

\[
\delta_\sigma(g)\le\varepsilon
\iff
(\sigma-\varepsilon)g\le\Ric_g\le(\sigma+\varepsilon)g.
\]

取 \(a=\sigma-\varepsilon,\ b=\sigma+\varepsilon\) 即可。负分支的正确顺序是

\[
(-1-\varepsilon)g\le\Ric_g\le(-1+\varepsilon)g.
\]

### \(Q_n\Rightarrow P_n^+\vee P_n^-\)

任意非退化区间 \([a,b]\) 都包含同号非退化闭子区间

\[
[u,v]\subset[a,b],\qquad uv>0.
\]

定义

\[
\mu=\frac{u+v}{2},\qquad
\sigma=\operatorname{sign}\mu,\qquad
\varepsilon=\frac{v-u}{|u+v|}\in(0,1).
\]

若 \(\delta_\sigma(h)\le\varepsilon\)，令

\[
g=\frac{h}{|\mu|}.
\]

则 \(A_g=|\mu|A_h\)，而且恒等式

\[
|\mu|(\sigma-\varepsilon)=u,\qquad
|\mu|(\sigma+\varepsilon)=v
\]

在正、负两种情况下都成立，故

\[
ug\le\Ric_g\le vg.
\]

由于 \([u,v]\subset[a,b]\)，可应用 \(Q_n\)。提取出的 \(\varepsilon,\sigma\) 只依赖 \(Q_n\) 的见证区间，因而只依赖维数。

---

## 4. 区间的真空性

任何 \(a<b\) 在固定 \(n\ge2\) 中都不是“对所有流形和度量完全无人满足”的区间：

- 若区间含某个 \(t>0\)，缩放圆球可使 \(\Ric=tg\)；
- 若区间含某个 \(t<0\)，缩放闭实双曲 \(n\)-流形可使 \(\Ric=tg\)；
- 若 \(0\in[a,b]\)，平坦环面满足 \(\Ric=0\)。

因此不能靠选择全局空区间使 \(Q_n\) 廉价成立。

更强地，若

\[
a<0<b,
\]

则任意闭流形上的任意度量充分放大后都有

\[
\operatorname{Spec}(A_{cg})=c^{-1}\operatorname{Spec}(A_g)\subset[a,b].
\]

所以跨零开区间实际上覆盖所有闭 \(n\)-流形。若该维数存在不承载任何 Einstein 度量的流形，则这种区间不可能见证 \(Q_n\)。

当 \(0\) 只是端点时，放大只能使特征值趋近零，不能改变符号，因此不能推出“每个流形都进入区间”。但这不影响核心归约，因为可在原区间内部选取严格同号子区间。

---

## 5. 低维结论

### \(n=2\)：完整成立

每个闭、连通、光滑曲面，包括非定向曲面，都承载常高斯曲率度量。二维中

\[
\Ric_h=K_hh,
\]

故常高斯曲率度量正是当前定义下的 Einstein 度量。于是所有闭曲面都满足 \(\Ein(M)\neq\varnothing\)，从而

\[
P_2^+,\qquad P_2^-
\]

对任意 \(\varepsilon\in(0,1)\) 都成立；\(Q_2\) 的前提甚至无关紧要。

必须避免把二维恒等式 \(\Ric_g=K_gg\) 误读为任意二维度量都是 Einstein：这里要求 Einstein 常数为全局常数。

### \(n=3\)：原命题已由正分支完整解决

若 \(\delta_+(g)\le\varepsilon<1\)，则

\[
\Ric_g\ge(1-\varepsilon)g>0.
\]

Hamilton 的三维正 Ricci 定理给出常正截面曲率度量，因此

\[
P_3^+
\]

对每个 \(\varepsilon<1\) 成立。仅此已经证明 \(Q_3\)；例如可取

\[
c_3=\frac12,\qquad C_3=\frac32.
\]

负分支也可建立：若 Ricci 特征值满足

\[
r_i\in[-1-\varepsilon,-1+\varepsilon],
\]

则在 Ricci 特征标架中

\[
K_{ij}=\frac{r_i+r_j-r_k}{2}
\le\frac{-1+3\varepsilon}{2}.
\]

三维曲率算子在该标架诱导的 \(\Lambda^2\) 基中对角化，所以 \(\varepsilon<1/3\) 时是所有二平面的严格负截面曲率，而不仅是三个坐标平面。再结合三维几何化/双曲化可得 \(M\) 承载双曲度量，故 \(P_3^-\) 至少对 \(\varepsilon<1/3\) 成立。

这里从 \(\sec<0\) 到双曲度量是深层三维拓扑步骤，不能由代数公式单独替代；非定向情形也需采用相应非定向几何化版本或定向双覆盖的等变论证。不过，\(Q_3\) 并不依赖这一负分支，因为正分支已经充分。

关于阈值：由 \(S^2\times S^1\) 的积度量可见 \(\delta_+=1\)，并结合 Hamilton 可推出三维正分支间隙的边界行为；但“阈值在何种定义下严格达到或最优”不是当前任务所需，宜与已充分证明的 \(\varepsilon<1\) 区分。负分支目前只得到 \(\Gamma_3^-\ge1/3\)，没有材料支持等号。

---

## 6. 完整证伪的精确要求

由于 \(Q_2,Q_3\) 已成立，整体命题若为假，必须存在一个固定维数

\[
\boxed{n\ge4}
\]

使正、负两支同时失败：

\[
\forall\varepsilon\in(0,1)\ \exists M_\varepsilon^+,g_\varepsilon^+:
\quad
\delta_+(g_\varepsilon^+)\le\varepsilon,\qquad
\Ein(M_\varepsilon^+)=\varnothing,
\]

并且

\[
\forall\varepsilon\in(0,1)\ \exists M_\varepsilon^-,g_\varepsilon^-:
\quad
\delta_-(g_\varepsilon^-)\le\varepsilon,\qquad
\Ein(M_\varepsilon^-)=\varnothing.
\]

两支可使用不同流形，流形也可随 \(\varepsilon\) 改变，但维数必须相同。等价地，可给出两列

\[
\delta_\pm(g_j^\pm)\to0,\qquad
\Ein(M_j^\pm)=\varnothing.
\]

其中 \(\Ein(M)=\varnothing\) 必须排除：

- 所有光滑 Riemann 度量；
- 所有 Einstein 常数 \(\lambda\in\mathbb R\)；
- 所有符号、复结构和对称类型。

只排除邻近解、同号解、Kähler–Einstein 解、指定 ansatz，或只构造某个固定的极小误差，均不足以证伪。

不同维数中分别否定两支也不足够：例如在 \(n_1\) 否定正支、在 \(n_2\) 否定负支，仍未产生任何一个 \(\neg Q_n\)。

---

## 7. 四维反例路线的已验证限制

底稿的四维定量 Hitchin–Thorpe 推论计算正确。若

\[
\delta_\sigma(g)\le\varepsilon<
\frac1{1+\sqrt3},
\]

则由

\[
|s|\ge4(1-\varepsilon),\qquad |E|^2\le4\varepsilon^2
\]

及 Chern–Gauss–Bonnet/签名公式得到

\[
2\chi(M)\pm3\tau(M)>0,
\]

即

\[
2\chi(M)>3|\tau(M)|.
\]

这一约束对 \(\sigma=\pm1\) 同时成立。因此违反 Hitchin–Thorpe 或位于其等号边界的四维流形，不可能承载任意紧的 \(\pm1\) Ricci 夹逼；它们虽可能不存在 Einstein 度量，却不能作为所需反例序列。真正的四维候选必须同时满足：

1. 严格 Hitchin–Thorpe 等必要约束；
2. 存在趋于零的无权逐点 Ricci 缺陷；
3. 仍有能够排除任意符号、任意类型 Einstein 度量的全局障碍。

综上，底稿的核心等价、缩放、符号及证伪量词均正确；需明确补入的关键事实是：所有非退化区间在全局上都有输入实例，\(n=2,3\) 已完整正面解决，因此任何完整反例只能在同一个固定 \(n\ge4\) 中同时摧毁两个归一化分支。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 16,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step16_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step16_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Review the monopole-amplitude/eigenline transfer needed after selecting bounded-curvature exponential pullback charts in the fixed critical Ishida-LeBrun sequence. Use the exact quantitative deficit decomposition in the Codex report. Suppose at an evolved time one has global Q=∫|Ric+g|²→0 and hence the scalar-Weyl completion-square profile, and suppose bounded sectional curvature plus derivative estimates hold on a positive-volume buffered set P. Identify a single nonnegative density or finite family of densities whose small global integrals and exponential-chart averaging would guarantee on one pullback chart: (i) a quantitatively nonzero limiting harmonic self-dual form, (ii) lowest-W+ eigenvalue saturation, and (iii) enough compactness to pass these to a local Einstein limit. Carefully distinguish harmonic representative H_a, spinor quadratic form ψ/φ, the fact the selected sign class may depend on metric/time, and any equations not preserved by cutoff flow. Decide whether the existing identities actually make such joint chart selection possible, or expose an exact missing estimate. Do not use unique continuation as a substitute for quantitative local amplitude.

## Integrated Scientific Memo

## 核验结论

在题设的“演化时刻快照”上，若除 \(Q_i=\int|\Ric_{g_i}+g_i|^2\to0\) 外，还确有正体积缓冲集 \(P_i\)，其上具有统一截面曲率及各阶导数界，并用指数拉回图而不是额外的高重覆盖，则**可以用一个有限非负密度族（或其总和）同时选出一张好图**，得到：

1. 非零的极限调和自对偶二形式；
2. \(W_i^+\) 最低特征值饱和；
3. 向局部 Einstein 极限传递所需的紧性。

但这并非仅由 \(Q_i\to0\) 自动推出。现有 Codex 最优权重分解还缺少一个关键输入：在演化度量上，全局
\[
q_i:=\sqrt6|W_i^+|-s_i>0
\]
并不由 \(Q_i\to0\) 保证。若只知道 \(q_i\to 9/2\) 于 \(L^2\)，则 \(f_i=\sqrt{q_i}\) 可能不是全局合法正权重，因此报告中导出振幅、调和投影和特征线误差的最优权重步骤尚不能直接调用。

---

## 1. 必须在演化度量上重新构造所有 monopole 对象

记演化后的度量仍为 \(g_i\)，
\[
E_i=\Ric_{g_i}+g_i,\qquad Q_i=\int_M|E_i|^2\to0.
\]
在固定临界 Ishida–LeBrun 流形上，选取当前度量的符号类 \(a_i\)，使
\[
p_i=(a_i^+)^2\ge A.
\]
符号类可以依赖 \(i\) 或演化时刻；由于固定流形上的符号集合有限，可取子列令 \(a_i=a\)。不能把初始时刻的 \(a^+\)、调和代表元或 monopole 解沿 cutoff flow 搬运。

对当前 \(g_i\)：

- \(H_i=H_{a_i}\) 是 \(a_i^+\) 的调和自对偶代表元：
  \[
  dH_i=d_{g_i}^*H_i=0,\qquad *_iH_i=H_i,\qquad \int|H_i|^2=p_i.
  \]
- \(\psi_i=2\sqrt2\,\sigma(\Phi_i)\)、\(\varphi_i=\frac32\psi_i\) 是 spinor 二次型，不是调和形式，通常也不闭。
- \(iF_{A_i}^+\) 的调和投影是 \(2\pi H_i\)，但 \(F_{A_i}^+\) 本身不调和。
- 只有对当前快照重新求解
  \[
  D_{A_i}\Phi_i=0,\qquad -iF_{A_i}^+=f_i\sigma(\Phi_i)
  \]
  后，才有
  \[
  f_i\varphi_i=3\sqrt2(-iF_{A_i}^+).
  \]

这些方程、最优权重、Hodge 分解及 harmonic projection 都不由 cutoff flow 保持。

---

## 2. 全局曲率轮廓和 primitive deficit

令
\[
w_i=|W_i^+|,\qquad q_i=\sqrt6w_i-s_i,\qquad
t_i=s_i+8\sqrt6w_i.
\]
固定临界流形上，Chern–Gauss–Bonnet、符号平均和完成平方给出
\[
0\le \Delta_i:=\int q_i^2-72\pi^2p_i
 \le108\pi^2R_i
 =\frac{27}{2}\int|\Ric_i^\circ|^2
 \le\frac{27}{2}Q_i\to0.
\]
同时
\[
\int t_i^2\le108Q_i,\qquad
\int(s_i+4)^2\le4Q_i.
\]
由精确关系
\[
q_i-\frac92=\frac18t_i-\frac98(s_i+4)
\]
可得
\[
\left\|q_i-\frac92\right\|_2^2\le C Q_i. \tag{1}
\]

这只说明 \(q_i\) 在 \(L^2\) 中接近 \(9/2\)，不能排除小集合上 \(q_i\le0\)。

---

## 3. 若最优权重估计可用，合适的联合密度

假设已经得到 Codex 分解的演化时刻版本，即存在正光滑权重 \(f_i\) 及相应 rescaled monopole，使下列误差趋零。可以使用单一总密度
\[
\begin{aligned}
\mathcal G_i={}&|E_i|^2+
\left(q_i-\frac92\right)^2+
\left(|2\pi H_i|-\frac{q_i}{3\sqrt2}\right)^2\\
&+\left|f_i\varphi_i+6\sqrt2\pi H_i\right|^2\\
&+2\left[
W_i^+(\psi_i,\psi_i)
+\sqrt{\frac23}\,w_i|\psi_i|^2
\right].
\end{aligned} \tag{2}
\]
每项逐点非负。最后一项非负来自
\[
W(v,v)\ge-\sqrt{\frac23}|W|\,|v|^2
\]
对三维空间上的迹零对称算子成立。

Codex 分解给出
\[
\int\left|f_i\varphi_i+6\sqrt2\pi H_i\right|^2
\le \Delta_i+o(1), \tag{3}
\]
\[
\int\left(|2\pi H_i|-\frac{q_i}{3\sqrt2}\right)^2
\le\frac{2}{9}\Delta_i+o(1), \tag{4}
\]
以及
\[
2\int\left[
W_i^+(\psi_i,\psi_i)+
\sqrt{\frac23}w_i|\psi_i|^2
\right]
\le\frac4{27}\Delta_i+o(1). \tag{5}
\]
结合 (1)，
\[
\int_M\mathcal G_i\to0. \tag{6}
\]

这里不需要把全局 Hölder gaps 本身局部化；它们没有天然逐点密度。它们的作用只是通过精确全局分解证明 (3)–(5)。

---

## 4. 可改写成纯调和形式的特征线密度

在缓冲集 \(P_i\) 上，若 \(W_i^+\) 和 \(f_i\) 一致有界，定义
\[
B_i=W_i^++\sqrt{\frac23}\,w_i I_{\Lambda^+}\ge0,
\qquad
\mathfrak e_i=2\langle B_iH_i,H_i\rangle\ge0. \tag{7}
\]
又令
\[
\widetilde H_i=-\frac{f_i\varphi_i}{6\sqrt2\pi}.
\]
由 (3)
\[
\|H_i-\widetilde H_i\|_2^2
\le \frac{\Delta_i+o(1)}{72\pi^2}. \tag{8}
\]
而 spinor eigenline density 与 \(\widetilde H_i\) 满足
\[
2\langle B_i\widetilde H_i,\widetilde H_i\rangle
=\frac{f_i^2}{32\pi^2}\,
2\left[W_i^+(\psi_i,\psi_i)
+\sqrt{\frac23}w_i|\psi_i|^2\right].
\]
故在有界几何区上，(5)、(8) 推出
\[
\int_{P_i}\mathfrak e_i\to0. \tag{9}
\]

因此更干净的有限密度总和是
\[
\boxed{
\mathcal D_i=
|E_i|^2+
\left(q_i-\frac92\right)^2+
\left(|2\pi H_i|-\frac{q_i}{3\sqrt2}\right)^2+
2\langle B_iH_i,H_i\rangle .
} \tag{10}
\]
它避免了对 spinor 本身建立局部紧性。

---

## 5. 指数图平均确实可实现联合选择

设 \(\Vol(P_i)\ge v_0>0\)，并且每个 \(p\in P_i\) 的半径 \(2r\) 指数图均落在有界几何缓冲区内。定义
\[
\mathcal A_i(p)=
\int_{B_r(0_p)}
\mathcal D_i(\exp_pv)\,
d\mu_{\exp_p^*g_i}(v).
\]
由统一截面曲率界下的 Jacobi 场/Jacobian 控制和测地流的 Liouville 测度不变性，
\[
\int_{P_i}\mathcal A_i(p)\,d\mu_i(p)
\le C(r,K)\int_{U_i}\mathcal D_i\,d\mu_i. \tag{11}
\]
指数映射不必单射；重叠次数已经由该平均公式控制。于是存在 \(p_i\in P_i\) 使
\[
\int_{B_r(0)}
\exp_{p_i}^*\mathcal D_i\to0. \tag{12}
\]

因此，对于题设所说的**有界曲率指数拉回图**，不需要额外的“cover sheet number \(\times\Delta_i\to0\)”估计。该乘数障碍只在另行取高重 CFG 覆盖、直接把 downstairs 原积分提升到 cover 时出现；它不适用于这里的指数图平均机制。若实际方案确实改用高重局部覆盖，则必须改为先控制 downstairs local means，并证明覆盖保持这些均值，或给出相应 multiplicity–deficit 控制。

---

## 6. 局部极限及定量非消失

令
\[
\widehat g_i=\exp_{p_i}^*g_i,\qquad
\widehat H_i=\exp_{p_i}^*H_i.
\]
缓冲集上的曲率导数界给出缩小球上
\[
\widehat g_i\to g_\infty
\]
的光滑子列收敛。

由 (10)、(12)，\(\widehat H_i\) 有统一局部 \(L^2\) 界；又因
\[
d\widehat H_i=0,\qquad
d_{\widehat g_i}^*\widehat H_i=0,\qquad
*_{\widehat g_i}\widehat H_i=\widehat H_i,
\]
内点 Hodge 椭圆估计给出
\[
\widehat H_i\to H_\infty
\]
在更小球上光滑收敛。误差密度依次给出
\[
\Ric_{g_\infty}=-g_\infty,\qquad s_\infty=-4,
\]
\[
q_\infty=\frac92,\qquad
|W_\infty^+|=\frac1{2\sqrt6},
\]
并且
\[
|H_\infty|
=\frac1{2\pi}\frac{9/2}{3\sqrt2}
=\frac{3}{4\sqrt2\pi}>0. \tag{13}
\]
这就是所需的定量局部振幅。unique continuation 完全不参与此步骤，也不能替代 (4)、(12)。

最后由 (7)、(9) 得
\[
\left\langle
\left(W_\infty^++
\sqrt{\frac23}|W_\infty^+|I\right)H_\infty,H_\infty
\right\rangle=0.
\]
括号中的算子半正定，且 \(H_\infty\ne0\)，故
\[
W_\infty^+H_\infty
=-\sqrt{\frac23}|W_\infty^+|H_\infty.
\]
迹零三维算子的等号情形给出
\[
\Spec(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right). \tag{14}
\]

---

## 7. 现有假设下的精确缺口

真正未由“演化时刻 \(Q_i\to0\) 加局部有界几何”填补的是**全局合法权重**：

\[
\boxed{
\text{需证明存在 }f_i>0\text{ 光滑，使 }
L_{f_i}-72\pi^2p_i\to0,
\quad
\sup_{U_i}f_i<\infty .
} \tag{15}
\]

Codex 的最优选择 \(f_i=\sqrt{q_i}\) 要求 \(q_i>0\)，而 \(Q_i\to0\) 只给 \(q_i\to9/2\) 于 \(L^2\)。等价的修复方案是证明带
\[
q_i^+=\max(q_i,0)
\]
的扩展 deficit decomposition，并把 \(q_i^-=\max(-q_i,0)\) 作为额外非负误差；由 (1) 已知
\[
\|q_i^-\|_2\to0.
\]
但该扩展尚未在提供的材料中证明。

此外，正则化 \(f_{i,k}\to\sqrt{q_i}\) 时应做对角选择，使 (3)–(5) 的 \(o(1)\) 对图平均足够；由于这些是统一的全局积分误差，这属于需要明确写出的对角化，而不是新的几何障碍。

### 最终判断

- **若**演化度量上可获得 (15)，或证明 \(q_i\ge\eta>0\)，或建立 \(q_i^+\) 版本的分解，则密度 (10) 与指数图平均足以联合选出一张图并完成 (i)–(iii)。
- **仅凭** \(Q_i\to0\)、完成平方轮廓和 \(P_i\) 上有界几何，现有恒等式尚不能启动该联合选择，因为最优 rescaled-monopole deficit 控制尚未在可能变号的 \(q_i\) 上得到证明。
- 用 unique continuation 宣称所选图上的极限形式非零是不成立的替代；所需非消失必须来自振幅密度的局部小积分。
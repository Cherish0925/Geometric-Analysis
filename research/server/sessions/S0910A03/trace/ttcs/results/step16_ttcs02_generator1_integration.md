# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 16,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step16_ttcs02_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step16_ttcs02_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop a rigorous repair for the global positivity/weight issue in the LeBrun rescaled monopole deficit after cutoff smoothing. On a fixed critical Ishida-LeBrun 4-manifold, suppose Q_i=∫|Ric+g|²→0, hence q_i:=sqrt(6)|W_i^+|-s_i satisfies ||q_i-9/2||_2→0 but q_i may be nonpositive on a small set. The Codex exact decomposition assumes a smooth positive weight f and becomes sharp at f=sqrt(q). Seek the strongest valid construction of smooth f_i>0 (e.g. sqrt(q_i^+ + epsilon), truncations, or variational weights) for which L_{f_i}-∫q_i² or the primitive deficit tends to zero, with enough control on bounded-curvature plateau regions to recover harmonic-amplitude and lowest-eigenline densities. Carefully derive how the negative part q_i^- enters, whether derivatives of f occur, and whether only L2 closeness plus bounded volume/curvature suffices. Produce either a proof with quantitative error or a concrete obstruction that identifies extra needed input.

## Integrated Scientific Memo

## 修复结论

令
\[
q_i=\sqrt6\,|W_i^+|-s_i,\qquad r_i=q_i^+,\qquad n_i=q_i^-,
\]
并选当前度量 \(g_i\) 的符号 monopole 类 \(a_i\)，记
\[
p_i=(a_i^+)^2,\qquad \beta_i=72\pi^2p_i,\qquad
Q_i=\int_M|\Ric_{g_i}+g_i|^2.
\]
在固定临界 Ishida–LeBrun 流形上，已有完成平方估计给出
\[
0\le \int q_i^2-\beta_i\le \frac{27}{2}Q_i,\qquad
\left\|q_i-\frac92\right\|_2^2\le C Q_i. \tag{1}
\]

变号问题可完全修复：把 Codex 中的 \(q\) 换成 \(q^+\)，并在精确 deficit 分解中加入唯一的新非负项
\[
\int q^-u^2.
\]
不需要任何 \(df_i\) 控制。仅凭 (1) 和有界体积即可构造光滑正权重，使 primitive deficit 为 \(O(Q_i)\)；在有界曲率平台上还可恢复调和振幅和最低特征线密度。

---

## 1. 正确的正部泛函

对任意光滑 \(f>0\)，定义
\[
L_i^+(f)=
\left(\int f^4\right)^{1/3}
\left(\int r_i^3f^{-2}\right)^{2/3}. \tag{2}
\]
Hölder 不等式给出
\[
\int r_i^2\le L_i^+(f). \tag{3}
\]

取形式权重
\[
f^2=r_i+\varepsilon.
\]
记
\[
E_i^+=\int r_i^2,\qquad I_i=\int r_i,\qquad V_i=\Vol(g_i).
\]
则
\[
F_{i,\varepsilon}:=\int(r_i+\varepsilon)^2
=E_i^++2\varepsilon I_i+\varepsilon^2V_i,
\]
以及
\[
G_{i,\varepsilon}:=\int\frac{r_i^3}{r_i+\varepsilon}
=E_i^+-\varepsilon I_i+\varepsilon^2V_i
-\varepsilon^3\int\frac1{r_i+\varepsilon}.
\]
因此
\[
E_i^+
\le F_{i,\varepsilon}^{1/3}G_{i,\varepsilon}^{2/3}
\le \frac13F_{i,\varepsilon}+\frac23G_{i,\varepsilon}
\le E_i^++\varepsilon^2V_i. \tag{4}
\]

虽然 \(r_i\) 一般只有 Lipschitz 正则性，但 \(r_i+\varepsilon\) 连续且严格为正。用正光滑函数 \(a_{i,\varepsilon,k}\) 一致逼近它并令
\[
f_{i,\varepsilon,k}=\sqrt{a_{i,\varepsilon,k}},
\]
即可由固定正下界传递 (2) 的两个积分。因此
\[
\inf_{f\in C^\infty,\ f>0}L_i^+(f)=\int r_i^2. \tag{5}
\]

对每个此类光滑权重，rescaled monopole 估计给出
\[
\beta_i\le L_i^+(f).
\]
取下确界可得关键结论
\[
\boxed{\beta_i\le\int(q_i^+)^2.} \tag{6}
\]
于是
\[
0\le \Delta_i^+:=\int r_i^2-\beta_i
=\left(\int q_i^2-\beta_i\right)-\|n_i\|_2^2
\le\frac{27}{2}Q_i, \tag{7}
\]
并自动得到
\[
\boxed{\|q_i^-\|_2^2\le\frac{27}{2}Q_i.} \tag{8}
\]

所以负部不是未受控误差；它被总 scalar–Weyl deficit 吸收。

---

## 2. 含负部的精确 deficit 分解

固定一个 \(i\) 并略去下标。对权重 \(f>0\) 的 rescaled monopole，沿用 Codex 记号
\[
u=|\varphi|,\quad Z=\int fu^3,\quad C=\int f^2u^2,
\]
\[
A_f=\left(\int f^4\right)^{1/3},\qquad
X_f=\left(\int r^3f^{-2}\right)^{1/3}.
\]
原始 Weitzenböck–Hodge 恒等式仍为
\[
P_f:=\int(qu^2-fu^3)=\frac{27}{8}D_0\ge0. \tag{9}
\]
定义
\[
N_f:=\int q^-u^2\ge0, \tag{10}
\]
以及
\[
H_1^+:=X_fZ^{2/3}-\int ru^2\ge0,\qquad
H_2:=A_fZ^{2/3}-C\ge0. \tag{11}
\]
因为 \(r=q+q^-\)，
\[
\int ru^2=Z+P_f+N_f,
\]
故
\[
X_fZ^{2/3}-Z=P_f+N_f+H_1^+. \tag{12}
\]
Hodge 投影恒等式不变：
\[
C=\beta+18J_A,\qquad
J_A=\int|iF_A^+-2\pi H_a|^2. \tag{13}
\]
纯代数整理得到
\[
\boxed{
L_f^+-\beta
=18J_A+H_2+
A_f\frac{X_f+Z^{1/3}}{Z^{2/3}}
\bigl(P_f+N_f+H_1^+\bigr).
} \tag{14}
\]

这就是所需全局修复。负部只通过
\[
N_f=\int q^-u^2
\]
出现，并具有有利的非负符号。

特别重要的是，(9)–(14) 中没有 \(df\) 或 \(\nabla^2f\)。证明对 \(\psi\) 使用 Hodge–Weitzenböck，而不是对 \(f\psi\) 使用；\(f\) 仅经
\[
-iF_A^+=f\sigma(\Phi)
\]
代数出现。因此光滑逼近的导数可以发散，不影响这些估计。

---

## 3. 序列权重及定量误差

固定流形且 \(Q_i\to0\) 时，由 (1) 可推出体积和 \(\int r_i^2\) 一致有界。取例如
\[
\varepsilon_i=Q_i
\]
（若希望尺度更自然，任何满足 \(\varepsilon_i^2V_i=o(1)\) 的选择均可）。将 \(r_i+\varepsilon_i\) 光滑逼近得 \(a_i>0\)，令
\[
f_i=\sqrt{a_i},
\]
并通过逐个 \(i\) 的对角逼近保证
\[
L_i^+(f_i)
\le \int r_i^2+\varepsilon_i^2V_i+o(Q_i). \tag{15}
\]
于是
\[
\boxed{
0\le d_i:=L_i^+(f_i)-\beta_i\le C Q_i.
} \tag{16}
\]
同时
\[
\left|L_i^+(f_i)-\int q_i^2\right|\le C Q_i, \tag{17}
\]
其中差异包括负部能量 \(\|q_i^-\|_2^2=O(Q_i)\)。

更一般地，不假设体积一致有界时，应选
\[
\varepsilon_i^2V_i\to0
\]
并把光滑逼近误差取得更小；若还直接估计展开中的线性项，可同时要求
\[
\varepsilon_i\sqrt{V_i\int r_i^2}\to0.
\]

由 (14) 及各整体因子远离零、保持有界，可得
\[
J_{A_i}\le \frac{d_i}{18},\qquad
D_{0,i}\le C d_i,\qquad
N_{f_i}\le C d_i. \tag{18}
\]

---

## 4. 调和振幅恢复

令 \(a_i=f_i^2\)。由两次 Hölder 近等号、Hodge 投影以及
\[
\int a_i^2=\beta_i+O(Q_i),\qquad
\int r_i^3a_i^{-1}=\beta_i+O(Q_i),
\]
可推出
\[
\|f_iu_i-a_i\|_2^2\le C Q_i. \tag{19}
\]
若逼近另满足
\[
\|a_i-(r_i+\varepsilon_i)\|_2^2=o(Q_i),
\]
则
\[
\boxed{\|f_iu_i-r_i\|_2^2\le C Q_i.} \tag{20}
\]

由于
\[
|iF_{A_i}^+|=\frac{f_iu_i}{3\sqrt2}
\]
且 \(2\pi H_i\) 是 \(iF_{A_i}^+\) 的调和投影，
\[
\boxed{
\left\||2\pi H_i|-\frac{r_i}{3\sqrt2}\right\|_2^2
\le C Q_i.
} \tag{21}
\]
又因
\[
\left|r_i-\frac92\right|\le\left|q_i-\frac92\right|,
\]
最终得到
\[
\boxed{
\left\||H_i|-\frac{3}{4\sqrt2\pi}\right\|_2^2
\le C Q_i.
} \tag{22}
\]

这里 \(H_i\)、monopole 解和 \(f_i\) 必须在演化后的当前度量上重新构造；它们不由 cutoff flow 保持。所选符号类可依赖 \(i\)，但固定流形上符号族有限，必要时可取子列使其固定。

---

## 5. 有界曲率平台上的最低特征线密度

在缓冲平台 \(U_i\) 上若
\[
|\Rm_{g_i}|\le K,
\]
则 \(r_i\le C(K)\)。光滑逼近可局部保持上界：
\[
\sup_{U_i}f_i^2\le C(K)+1. \tag{23}
\]
无需 \(f_i\) 的一致正下界。

定义半正定算子
\[
\mathscr A_i
=W_i^++\sqrt{\frac23}|W_i^+|I_{\Lambda^+}\ge0.
\]
\(D_0\) 的特征线项给出
\[
2\int\langle\mathscr A_i\psi_i,\psi_i\rangle
\le C Q_i. \tag{24}
\]
再令
\[
\widetilde H_i
=-\frac{f_i\varphi_i}{6\sqrt2\pi}
=\frac{iF_{A_i}^+}{2\pi}.
\]
则
\[
\|\widetilde H_i-H_i\|_2^2
=\frac{J_{A_i}}{4\pi^2}\le C Q_i, \tag{25}
\]
且
\[
\langle\mathscr A_i\widetilde H_i,\widetilde H_i\rangle
=\frac{f_i^2}{32\pi^2}
\langle\mathscr A_i\psi_i,\psi_i\rangle.
\]
利用平台上的 \(\mathscr A_i,f_i\) 上界，得到
\[
\boxed{
\int_{U_i}\langle\mathscr A_iH_i,H_i\rangle
\le C(K)Q_i.
} \tag{26}
\]

因此可用于指数图联合平均的单一非负密度是
\[
\boxed{
\begin{aligned}
\mathcal D_i={}&|\Ric_{g_i}+g_i|^2
+\left(r_i-\frac92\right)^2\\
&+\left(|2\pi H_i|-\frac{r_i}{3\sqrt2}\right)^2
+2\langle\mathscr A_iH_i,H_i\rangle .
\end{aligned}} \tag{27}
\]
其平台积分趋于零。选取局部平均趋零的有界几何指数图后，若度量具有足够的曲率导数界从而光滑收敛，则 Hodge 内点估计给出 \(H_i\) 的局部光滑子列，并在极限上得到
\[
|H_\infty|=\frac{3}{4\sqrt2\pi}>0,\qquad
\mathscr A_\infty H_\infty=0.
\]
结合
\[
|W_\infty^+|=\frac1{2\sqrt6},
\]
可推出
\[
\Spec(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

---

## 6. 输入的精确强度与剩余限制

这项权重修复只需要：

1. \(q_i^+\) 连续（光滑度量自动满足）；
2. 全局 primitive deficit 和 \(L^2\) 轮廓 (1)；
3. \(\varepsilon_i^2V_i\to0\)；
4. 为转移最低特征线密度，在平台上有 \(f_i\) 与 \(W_i^+\) 的上界。

因此，在固定临界流形上，\(L^2\) 接近和由拓扑恢复的有界体积足以解决**全局正权重及调和振幅**问题；不需要导数权重估计，也不需要全局点态 \(q_i>0\)。

但仅有 \(L^2\) 轮廓和体积界不足以产生局部光滑极限。最终图上传递 \(W_i^+\)、Hodge 方程和特征线关系，仍需平台上的截面曲率及足够的曲率导数控制（或等价的光滑几何紧性）。这与权重修复是独立问题。
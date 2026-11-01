# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step21_corrections_from_ttcs_and_peers.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md"
  ]
}
```

## Task

Independently check the downstream geometric passage from the terminal cutoff-flow metrics to the forbidden calibrated Einstein germ. Focus on whether the good-support/Vitali construction truly supplies a positive-volume set with a fixed terminal-metric geodesic buffer; whether the exponential-pullback averaging inequality supplies a noncollapsed smooth chart despite collapse and sheet multiplicity; whether global terminal L2 defect can be converted, after rebuilding the Seiberg-Witten objects for that same terminal metric, into one joint nonnegative density whose pullback limit has nonzero harmonic self-dual form in the lowest W+ eigenspace; and whether the Step 6 projector/Einstein-Weyl contradiction then follows. Distinguish fixed topology from varying topology. Identify every load-bearing statement still asserted rather than proved, and formulate the shortest rigorous bridge that would close it if possible.

## Output

# 独立科学复核备忘录

## 总结

从终端截断流度量到校准 Einstein 局部模型的几何链条，在补齐几个明确引理后是成立的：

1. Step 23 的互不相交支撑可以借助初始 Ricci 下界、最大分离点集和 Bishop–Gromov 比较，产生终端度量下占固定体积比例的中心集，并有固定长度的测地缓冲。
2. Step 16 的指数拉回平均不等式确实消除了底流形塌缩和多重指数映射片层带来的困难。它本身只给拉回体积下界；拉回度量的光滑收敛还需要终端平台上的全部曲率导数估计。
3. 对同一个终端度量重新求 harmonic representative 与 rescaled Seiberg–Witten 解后，可以组成一个逐点 \(\ge0\) 的联合密度。这里必须修正 Step 21 中 \(q^+\) 和 Weyl 算子的两处公式。
4. 联合密度在选定指数图上趋零后，极限满足
   \[
   \operatorname{Ric}=-g,\qquad
   \operatorname{Spec}(W^+)=\left(-\frac16,\frac1{12},\frac1{12}\right),
   \]
   并带有非零、定长、位于最低特征线的自对偶调和二形式。Step 6 的 projector 论证与 Einstein–Weyl 恒等式随后给出矛盾。

当前材料尚未完整给出产生终端度量所需的统一首退出估计；Step 27 解决的是已有 \(\|a\operatorname{Rm}\|_\infty\) 控制后的延拓。下游部分还缺一个书面化的“终端联合密度引理”，但其最短证明可以由现有代数组成。

---

## 1. 正体积支撑与终端测地缓冲

Step 23 直接写出“进一步稀疏后 \(U_j\) 互不相交且内球仍占固定体积比例”，但没有给出覆盖计算。该结论可由下述标准论证得到。

设初始度量满足
\[
\operatorname{Ric}_{g_i(0)}\ge-\Lambda g_i(0),
\]
且好点集 \(G_i\) 满足
\[
\operatorname{Vol}_{g_i(0)}G_i\ge\alpha\operatorname{Vol}_{g_i(0)}M_i.
\]
在 \(G_i\) 中取极大的 \(12r\)-分离点集 \(\{p_{ij}\}\)。于是

\[
B_{6r}(p_{ij})\quad\text{两两不交},\qquad
G_i\subset\bigcup_jB_{12r}(p_{ij}).
\]

Bishop–Gromov 比较给出统一常数
\[
\operatorname{Vol}B_{12r}(p_{ij})
 \le D(n,\Lambda,r)\operatorname{Vol}B_{2r}(p_{ij}).
\]
因此对
\[
P_i^0=\bigcup_jB_{2r}^{g_i(0)}(p_{ij})
\]
有
\[
\operatorname{Vol}_{g_i(0)}P_i^0
 \ge D^{-1}\operatorname{Vol}_{g_i(0)}G_i
 \ge \alpha D^{-1}\operatorname{Vol}_{g_i(0)}M_i.
\tag{1}
\]

若终端度量 \(\bar g_i=g_i(T_0)\) 满足统一双 Lipschitz 比较
\[
L^{-1}g_i(0)\le \bar g_i\le Lg_i(0),
\tag{2}
\]
则
\[
\operatorname{Vol}_{\bar g_i}P_i^0
 \ge c(n,\alpha,D,L)\operatorname{Vol}_{\bar g_i}M_i.
\tag{3}
\]

测地缓冲也由 (2) 直接得到。若 \(p\in B_{2r}^{g_i(0)}(p_{ij})\)，且 \(\gamma\) 是从 \(p\) 出发、终端长度不超过 \(\rho\) 的 \(\bar g_i\)-测地线，则
\[
d_{g_i(0)}(p_{ij},\gamma(t))
 \le2r+\sqrt L\,\rho.
\]
取
\[
\rho\le\frac r{\sqrt L},
\tag{4}
\]
整条测地线都位于 \(B_{3r}^{g_i(0)}(p_{ij})\subset\{\chi_j=1\}\)。

因此，只要在 \(B_{4r}\) 上有统一抛物曲率控制，局部 normalized Ricci-flow 导数估计便可在 \(B_{3r}\) 上给出
\[
\sup_{B_{3r}(p_{ij})}|\nabla^m\operatorname{Rm}_{\bar g_i}|
 \le K_m,\qquad m=0,1,\ldots .
\tag{5}
\]

这一段不需要体积不塌缩。真正尚缺的是：材料中没有把好点集 \(G_i\)、固定 \(r\)、体积比例 \(\alpha\)、双 Lipschitz 常数 \(L\) 和终端估计 (5) 放进同一个已证明命题。Step 23 仍在 provisional interval 上工作；Step 27 则从已有 \(|a\operatorname{Rm}|\) 上界开始。

---

## 2. 指数拉回平均与光滑图

Step 16 的平均不等式是正确的。若所有长度至多 \(\rho\) 的相关测地线均处于 \(|\sec|\le K\) 的区域，并且
\[
\rho<\frac{\pi}{2\sqrt K},
\]
则 Rauch 比较给出
\[
s_K(t)^{n-1}\le J_p(t,\theta)\le s_{-K}(t)^{n-1}.
\]
上界控制分子，下界控制每个拉回球的体积。Liouville 测度在测地流下不变，所以
\[
\int_{P_i}\fint_{B_\rho(0),h_{i,p}}
 F(\exp_pv)\,d\mu_{h_{i,p}}\,d\mu_{\bar g_i}(p)
 \le C(n,K,\rho)\int_{\Omega_i}F\,d\mu_{\bar g_i}.
\tag{6}
\]

这里 \(h_{i,p}=\exp_p^*\bar g_i\)。指数映射即使有任意多片层，(6) 也不出现片层数：测地流保留终端方向和 Liouville 测度。

此外，\(\rho<\pi/\sqrt K\) 排除了径向共轭点，故 \(h_{i,p}\) 是真正的光滑正定度量。更强地，\(h_{i,p}\) 在原点的指数映射就是
\[
\exp^{h_{i,p}}_0(v)=v.
\]
所以拉回球本身是统一正规坐标球；底流形的 injectivity radius 不参与。

若再有 (5)，则曲率及其全部协变导数在拉回球上一致有界。Jacobi 方程和标准正规坐标估计给出：选取定向正交标架后，\(h_{i,p_i}\) 在任意较小球上有 \(C^\infty\) 收敛子列。仅有 \(|\sec|\le K\) 时，不能推出这一光滑收敛；Step 16 对这一点的说明是准确的。

---

## 3. 终端 Seiberg–Witten 密度

令
\[
E_i=\operatorname{Ric}_{\bar g_i}+\bar g_i,\qquad
Q_i=\int_{M_i}|E_i|^2,\qquad V_i=\operatorname{Vol}_{\bar g_i}M_i.
\]
所需的归一化输入是
\[
\frac{Q_i}{V_i}\longrightarrow0.
\tag{7}
\]

### 两处必须修正的公式

正确的权函数是
\[
q_i=\sqrt6\,|W_i^+|-s_i,\qquad r_i=q_i^+.
\tag{8}
\]
Step 21 §9.5 写成了
\[
\max(\sqrt6|W^+|-|s|,0),
\]
这在模型 \(s=-4,\ |W^+|=1/(2\sqrt6)\) 上等于零，与目标值 \(9/2\) 不相容。

有限 \(i\) 时应使用
\[
\mathcal A_i
 =W_i^++\sqrt{\frac23}|W_i^+|\,I_{\Lambda^+}\succeq0.
\tag{9}
\]
不能提前改成 \(W_i^++\frac16I\)，因为后者未必逐点半正定。只有在极限已经得到
\[
|W_\infty^+|=\frac1{2\sqrt6}
\]
后，(9) 才变成 \(W_\infty^++\frac16I\)。

### 从 \(Q_i\) 到同一个 \(H_i\)

由 \(7/24\) 校准不等式和 \(|s_i+4|=|\operatorname{tr}E_i|\le2|E_i|\)，
\[
\int\left(r_i-\frac92\right)^2\le C Q_i.
\tag{10}
\]

Chern–Gauss–Bonnet 与临界拓扑恒等式给出
\[
\frac{V_i}{A_i^{\rm top}}\longrightarrow\frac{32\pi^2}{9}.
\tag{11}
\]
于是
\[
\int r_i^2
 =72\pi^2A_i^{\rm top}+o(V_i).
\tag{12}
\]

对终端度量重新选择一个符号 monopole 类，使其 harmonic self-dual 投影平方满足
\[
p_i=(a_i^+)^2\ge A_i^{\rm top}.
\]
正部 rescaled monopole 不等式给出
\[
0\le\Delta_i:=\int r_i^2-72\pi^2p_i=o(V_i).
\tag{13}
\]

对该同一个终端度量和同一个类，取平滑正权 \(f_{ik}^2\to r_i+\varepsilon_i\)。定量 deficit 分解产生 harmonic representative \(H_i\) 以及

\[
\int\left(
 |2\pi H_i|-\frac{r_i}{3\sqrt2}
 \right)^2=o(V_i),
\tag{14}
\]
并控制 spinor 二次型在 \(\mathcal A_i\) 上的能量。由于 \(H_i\) 是所选类在 \(\bar g_i\) 下的 harmonic representative，它不依赖正权正则化参数。

在平台 \(\Omega_i\) 上已有 \(|\operatorname{Rm}|\le K\)，故 \(f_i^2\) 与 \(\|\mathcal A_i\|\) 一致有界。利用
\[
\|f_i\varphi_i+6\sqrt2\pi H_i\|_2^2\le C\Delta_i
\]
和 spinor eigenspace 项，可得
\[
\int_{\Omega_i}
 \langle\mathcal A_iH_i,H_i\rangle=o(V_i).
\tag{15}
\]

因此
\[
\begin{aligned}
\mathcal D_i={}&|E_i|^2+
 \left(r_i-\frac92\right)^2+
 \left(|2\pi H_i|-\frac{r_i}{3\sqrt2}\right)^2\\
&+2\langle\mathcal A_iH_i,H_i\rangle
\end{aligned}
\tag{16}
\]
满足
\[
\mathcal D_i\ge0,\qquad
\int_{\Omega_i}\mathcal D_i=o(V_i).
\tag{17}
\]

材料中的代数脚本与 quantitative deficit note 支持 (13)–(15)，但尚未给出一个完整书面引理，把正部正则化、rescaled SW 解的存在、同一个 \(H_i\)、以及 (15) 连续串联起来。这是下游最重要的书面缺口。

---

## 4. 图选择与极限

由 (3)、(6)、(17)，存在 \(p_i\in P_i\) 使
\[
\fint_{B_\rho(0),h_i}
 \mathcal D_i(\exp_{p_i}v)\,d\mu_{h_i}\longrightarrow0,
\qquad h_i=\exp_{p_i}^*\bar g_i.
\tag{18}
\]

取较小固定球，(5) 给出
\[
h_i\longrightarrow h_\infty\quad\text{于 }C^\infty_{\rm loc}.
\tag{19}
\]

由 (14) 和平台曲率界，拉回 \(H_i\) 有统一局部 \(L^2\) 界。Hodge 方程
\[
dH_i=0,\qquad d_{h_i}^*H_i=0,\qquad *_iH_i=H_i
\]
的内点椭圆估计给出
\[
H_i\longrightarrow H_\infty\quad\text{于 }C^\infty_{\rm loc}.
\tag{20}
\]

将 (18) 传到极限：

\[
\operatorname{Ric}_{h_\infty}=-h_\infty,\qquad s_\infty=-4,
\tag{21}
\]
\[
r_\infty=\frac92,\qquad
|W_\infty^+|=\frac1{2\sqrt6},
\tag{22}
\]
\[
|H_\infty|=\frac{3}{4\sqrt2\pi}>0,
\tag{23}
\]
\[
\mathcal A_\infty H_\infty=0.
\tag{24}
\]

对任意无迹对称 \(3\times3\) 算子 \(W\)，
\[
\lambda_{\min}(W)\ge-\sqrt{\frac23}|W|,
\]
且等号恰好对应另外两个特征值相等。由 (22)–(24)，
\[
\operatorname{Spec}(W_\infty^+)
 =\left(-\frac16,\frac1{12},\frac1{12}\right).
\tag{25}
\]

这说明单独的 Weyl 模长校准确实不够；\(H_\infty\) 的最低特征线信息是确定 (25) 的必要成分。

---

## 5. Step 6 的局部矛盾

由 (21)，
\[
\delta W_\infty^+=0.
\]
由 (25)，\(W_\infty^+\) 有常数单特征值和常数双特征值。写
\[
W_\infty^+=\mu I+(\lambda-\mu)P_\omega,
\]
其中 \(\omega\) 是定长的局部特征二形式。对 \(\delta W^+=0\) 展开并与 \(\omega\) 收缩，先得
\[
\nabla^a\omega_{ab}=0,
\]
再得
\[
\omega_{ab}\nabla^a\omega_{cd}=0.
\]
自对偶非零二形式在四维可逆，因此
\[
\nabla\omega=0,\qquad \nabla W_\infty^+=0.
\tag{26}
\]

另一方面 Einstein 四维 Weyl 恒等式为
\[
\Delta|W^+|^2
 =2|\nabla W^+|^2+s|W^+|^2-36\det W^+.
\]
代入
\[
s=-4,\quad |W^+|^2=\frac1{24},\quad
\det W^+=-\frac1{864}
\]
得到
\[
|\nabla W^+|^2=\frac1{16},
\tag{27}
\]
与 (26) 矛盾。Step 6 的这一局部论证成立，而且不再需要任何全局塌缩分类。

---

## 6. 固定拓扑与变拓扑

### 固定拓扑

此时 \(A^{\rm top}\)、总体积和初始平均曲率能量一致有界，Step 21 给出的 Li 尺度有统一正下界。于是：

\[
r\ge r_0>0,\qquad T_0=\theta r^2\ge T_*>0,
\]
\[
Q_i\to0,\qquad \operatorname{Vol}P_i\ge v_0>0.
\]

联合密度的总积分绝对趋零，(18) 直接成立。符号类有限，但局部论证其实不需要固定类子列。

### 变拓扑

此时通常只有
\[
Q_i=o(V_i),\qquad \int\mathcal D_i=o(V_i).
\]
指数平均仍然有效，只要同时有

\[
\operatorname{Vol}P_i\ge cV_i,\qquad
r_i\ge r_0>0,\qquad K_m\le C_m.
\tag{28}
\]

符号类数目增长不影响“每个度量选择一个最大投影类”；它只阻止关于所有符号类逐一趋近等号的统一结论。

若 \(r_i\to0\)，现有链条不能产生固定半径的 Einstein 图。将度量按 \(r_i^{-2}\) 放大后，
\[
\operatorname{Ric}_{r_i^{-2}g_i}=-r_i^2(r_i^{-2}g_i),
\]
极限趋向 Ricci-flat，校准 Weyl 常数也缩为零，Step 6 的模型不再出现。因此一般变拓扑情形还需要统一 Li 尺度与统一正时间平台；Step 21 只说明在额外的 \(\chi/A\) 控制族中可能得到这一点。

---

## 7. 最短可闭合桥梁

现有下游论证可压缩为如下命题。

> **终端平台引理。**  
> 设 \((M_i,\bar g_i)\) 属于临界 Ishida–LeBrun 家族，并存在 \(P_i\Subset\Omega_i\)、常数 \(c,\rho,K_m>0\)，使  
> \[
> \operatorname{Vol}P_i\ge c\,\operatorname{Vol}M_i,
> \]
> 从 \(P_i\) 发出的长度至多 \(2\rho\) 的测地线都留在 \(\Omega_i\)，
> \[
> \sup_{\Omega_i}|\nabla^m\operatorname{Rm}|\le K_m,
> \qquad
> \frac{\int|\,\operatorname{Ric}+\bar g_i\,|^2}
> {\operatorname{Vol}M_i}\to0.
> \]
> 若终端度量上的正部 rescaled monopole 分解给出 (13)–(15)，则指数平均选择出固定半径的光滑拉回极限；该极限满足 (21)–(25)，从而与 (26)–(27) 矛盾。

这个引理的几何证明已由上面的 Vitali–Bishop–Gromov计算、指数平均、Hodge 内点估计和 Step 6 组成。当前真正没有在所给文件中完成的是：

- 统一产生该终端平台的首退出/Moser 估计；
- 把好点集、固定尺度、平台体积比例和双 Lipschitz 漂移写成一个定量命题；
- 把终端正部 rescaled Seiberg–Witten 代数整理成同一个 \(H_i\) 满足 (14)–(15) 的完整引理；
- Step 27 中 Wang 型高阶指数安排仍以引用性叙述为主，尚未逐项展开。

除这些输入外，指数图选择和 Step 6 的局部 Einstein–Weyl 矛盾没有发现新的几何障碍。
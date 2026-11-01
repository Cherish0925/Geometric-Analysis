# TTCS Independent Branch Record

```json
{
  "step_id": 44,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step42_uniform_gap_weight_terminal_repairs.md",
    "Sessions/S0910A01/workspace/notes/step43_H_WU_resolution_weighted_evolution.md",
    "Sessions/S0910A01/workspace/notes/step43_H_DT_assessment.md",
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A03/trace/ttcs/results/step45_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/trace/ttcs/results/step45_ttcs01_verifier2_integration.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md"
  ]
}
```

## Task

Independently review the restricted four-dimensional negative Ishida--LeBrun defect-gap chain as assembled in A01. Focus on whether the proof now coherently runs on one exact degenerate cutoff flow after coefficient regularization, and whether the analytic estimates feed the terminal Derdzinski contradiction without a hidden unsupported step. Please examine especially: (1) A01 Step43 §6 saying C_{m+1} is a previous layer versus A03 Step45/TTCS correction that it is the current partner of U_m and closes by same-exponent L^p energies; (2) whether coefficient-regularized flows with b=chi^2+eps^2 are used only to construct a common-time smooth limit solving the exact a=chi^2 flow before stationary collars, frozen complement, disjoint supports, and global Q are applied; (3) support construction with maximal-function good sets, disjoint buffers, one global a=sum chi_alpha^2, inner centers, and plateau volume from Vol/A -> 32 pi^2/9; (4) first-exit chain K2^eta -> integrated Y -> J6 -> Moser endpoints and global Q on the same exact flow; (5) terminal recalibration with q>=0 and the corrected D_av identity; (6) Liouville--Rauch pullback, strong finite W^{2,p} convergence, and Derdzinski forbidden germ. Return a direct scientific memo: which links are now sound, which statements in the notes must be corrected, and whether the family-uniform restricted gap follows after those corrections. Do not treat this as a solution of full Yau Problem 26.

## Output

# 科学复核备忘录：四维 Ishida–LeBrun 的 \(\operatorname{Ric}\approx-g\) 缺陷间隙链

## 总体结论

所给材料能够组成一条作用于**同一条精确退化流**
\[
\partial_tg=-2a(\operatorname{Ric}_g+g),\qquad a=\chi^2,
\]
的完整矛盾链。系数正则化
\[
b_\varepsilon=\chi^2+\varepsilon^2
\]
只负责逐数据构造公共正时间上的光滑解；选取支撑、冻结补集、局部能量、全局 \(Q\)、终端再校准和 Liouville–Rauch 选择都必须在取 \(\varepsilon\to0\) 后得到的精确 \(a=\chi^2\) 流上进行。按这个次序，流平台与几何终端机制是相容的。

现有笔记仍有几处需要按数学内容改写：

1. A01 Step43 §6 把 \(C_{m+1}\) 写成“previous layer”不对；它是 \(U_m\) 的当前伙伴，必须联合做同指数 \(L^p\) 能量。
2. A01 Step41 §7.2 的终端缺陷公式仍有一个多余的 \(A\)-项。
3. A01 Step41 (7.4) 的终端密度遗漏 \(|E|^2\)。按该式选点不能推出极限满足 \(\operatorname{Ric}=-g\)；应直接使用 Step28 的四项密度。
4. 支撑构造中的非归一化曲率能量阈值、辅助 cutoff 的缓冲余量，以及终端测地线半径，需要作固定常数调整。
5. Step43 §6 只展示了 Hessian-\(a\) 顶阶项；抛物形式中由 \(-(\Delta a)U\) 产生的第二个 \(\chi C_{m+2}U\) 项也必须并入同一积分分部计算。

这些修正加入后，在所述 Ishida–LeBrun 地理族及其 \(q\ge0\) 分支内，反证法确实给出与 \(A,D,q,N\) 无关的
\[
\varepsilon_{\mathrm{IL}}>0.
\]
这只是四维 \(\operatorname{Ric}\approx-g\) 分支的族一致间隙，不是 Yau 第26题的全维证明或证伪。

---

## 1. \(C_{m+1}\) 必须与 \(U_m\) 联合估计

令
\[
V=U_m,\qquad Z=C_{m+1}=\nabla^{m+1}\chi .
\]
在空间阶 \(m\) 开始时，已知量是
\[
T_j\ (j<m),\qquad U_j,C_{j+1}\ (j<m),
\]
而 \(Z=C_{m+1}\) 并不属于此前完成的层级。其演化式
\[
\partial_tC_{m+1}
 =\sum_{r+s=m-1}U_{r+1}*C_{s+1}
\]
含有当前耦合
\[
U_m*C_1.
\]
因此 A01 Step43 §6 中下列说法不成立：

> “\(C_{m+1}\in L^q\) by induction.”

正确闭合方式正是 A03 Step45 (5.7)：
\[
\frac d{dt}\left(\|U_m\|_p^p+\|C_{m+1}\|_p^p\right)
+c_{m,p}\int b|\nabla U_m|^2|U_m|^{p-2}
\le C_{m,p}\left(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\right).
\tag{1.1}
\]

顶阶 cutoff 项应统一写成
\[
\chi C_{m+2}*\mathcal A(U_0)*|U_m|^{p-2}U_m,
\qquad |\mathcal A(U_0)|\le C|U_0|.
\]
一次积分分部后出现
\[
C_1*Z*U_0*P(V),\qquad
\chi Z*U_1*P(V),\qquad
\chi Z*U_0*\nabla P(V).
\]
最后一项满足
\[
\left|\int\chi ZU_0|V|^{p-2}\nabla V\right|
\le \eta\int\chi^2|\nabla V|^2|V|^{p-2}
+C_{\eta,p}K^2\int |Z|^2|V|^{p-2},
\]
而
\[
\int |Z|^2|V|^{p-2}
\le \frac2p\|Z\|_p^p+\frac{p-2}{p}\|V\|_p^p.
\]
这正好由联合能量吸收，不需要先验 \(C_{m+1}\) 高指数估计。

还需区分低阶端点：

- \(m=1\) 时，\(\chi C_2*U_1*P(U_1)\) 是当前 signed-Hessian 结构；
- \(m=2\) 时，二次积分分部产生的
  \[
  \chi C_2*U_2*P(U_2)
  \]
  仍须按 signed-Hessian 形式处理；
- \(m\ge3\) 时，第二次积分分部中的 \(C_m,U_1,U_2\) 才全部来自此前层级。

完成 \((U_m,C_{m+1})\) 后再估计 \(T_m\)，得到交错次序
\[
T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
\longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots .
\]

因此，Step43 的 cutoff 权重来源分析可以保留，但其 §6 的能量闭合必须替换为 Step45 的当前双变量估计。

---

## 2. 系数正则化与精确退化流的先后次序

对一组两两不交的 cutoff，令
\[
\chi_{\mathrm{glob}}=\sum_\alpha\chi_\alpha .
\]
由于任一点至多一个 \(\chi_\alpha\) 非零，
\[
\chi_{\mathrm{glob}}^2=\sum_\alpha\chi_\alpha^2=a,
\qquad 0\le\chi_{\mathrm{glob}}\le1.
\]
因此 Step45 的单 cutoff 正则化可直接用于全局系数
\[
b_\varepsilon=a+\varepsilon^2
=\chi_{\mathrm{glob}}^2+\varepsilon^2.
\]

正确的构造次序是：

1. 对每个固定 \(\varepsilon>0\)，用输运系数
   \[
   \widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1}
   \]
   的 DeTurck 系统构造严格抛物解。
2. 拉回后得到精确几何方程
   \[
   \partial_tg_\varepsilon
   =-2b_\varepsilon(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon).
   \]
3. Step45 的有限指数估计、固定背景连接差估计和逐数据第一退出改进给出与 \(\varepsilon^{-1}\) 无关的公共正时间。
4. 在固定背景坐标中取
   \[
   g_{\varepsilon_j}\to g\quad\text{于 }C^\infty,
   \]
   得到
   \[
   \partial_tg=-2a(\operatorname{Ric}_g+g).
   \tag{2.1}
   \]
5. 从此以后才使用 \(a=0\) 区域静止、支撑不交、局部 \(K_2^\eta,J_6\) 和全局 \(Q\)。

在 \(b_\varepsilon\) 流上，支撑外仍以速度
\[
-2\varepsilon^2(\operatorname{Ric}+g)
\]
演化，所以冻结补集及静止 collar 不能用于正则化阶段。A01 的终端链应明确注明所有这些性质都属于极限流 (2.1)。

退化方程的唯一性不参与这里的矛盾。逐数据构造产生一条实际光滑分支；若在光滑正定端点 \(g_*\) 重新启动，自治方程
\[
F(g)=-2a(\operatorname{Ric}_g+g)
\]
决定左右两侧全部时间 jets，因而可光滑拼接。这里需要的是延拓的存在，而不是正则化子列无关性。

Step43 H-DT 中“一般零阶光滑 tame 扰动自动保持可逆”的表述过宽。当前链最好直接采用 Step45 的系数正则化、几何能量和固定背景紧性论证；这样不依赖该抽象句子。

---

## 3. 支撑构造：主体正确，三处常数需修订

### 3.1 好集、着色和平台体积

在初始度量满足 \(\operatorname{Ric}\ge-2g\) 时，局部测度具有固定尺度 doubling 性质，截断极大函数满足弱型估计。若
\[
\lambda=\frac{\widetilde\gamma^2}{r^4},
\]
则
\[
\operatorname{Vol}\{\mathcal M_{R_0}(|\operatorname{Rm}|^2)>\lambda\}
\le C(R_0)\frac{r^4}{\widetilde\gamma^2}
\int|\operatorname{Rm}|^2
\le C\frac{r^4}{\widetilde\gamma^2}A.
\]
结合
\[
\operatorname{Vol}(g)/A\to\frac{32\pi^2}{9},
\]
固定足够小的 \(r\) 后，好集具有 \(\alpha A\) 量级体积。

最大 \(r\)-分离网覆盖好集。把网点分成有限个 \(14r\)-分离颜色类后，
\[
\operatorname{Vol}(\mathrm{good})
\le\sum_{\ell=1}^{N_0}
\operatorname{Vol}\!\left(
  \bigcup_{\alpha\in\mathcal A_\ell}B_r(x_\alpha)
\right)
\le\sum_{\ell=1}^{N_0}
\operatorname{Vol}\!\left(
  \bigcup_{\alpha\in\mathcal A_\ell}B_{5r}(x_\alpha)
\right).
\]
故至少一类的 \(B_{5r}\) 并集具有 \(cA\) 体积，同时其 \(B_{7r}\) 两两不交。这个体积论证应在 Step41 §2 中显式写出。

### 3.2 初始能量阈值

若 \(x_\alpha\) 属于好集且 \(7r\le R_0\)，定义本身已经给出
\[
r^4\fint_{B_{7r}(x_\alpha)}|\operatorname{Rm}|^2
\le\widetilde\gamma^2.
\]
Step41 (2.5) 不需要先转到 \(B_{R_0}\)。

若后续模块要求
\[
\int_{B_{7r}}|\operatorname{Rm}|^2\le\gamma_{\rm abs}^2,
\]
不能在固定 \(\widetilde\gamma=\gamma_{\rm abs}\) 后仅靠缩小 \(r\) 获得，因为四维中
\[
\frac{V_{-2}(7r)}{r^4}\to\omega_4\,7^4\neq0.
\]
正确做法是预先取
\[
\widetilde\gamma=c_*\gamma_{\rm abs}
\]
且 \(c_*\) 足够小，再相应缩小 \(r\) 维持好集体积。这个调整不影响族一致性。

### 3.3 cutoff 与辅助 \(\eta\) 的缓冲

局部 \(K_2^\eta\) 要求
\[
\eta\equiv1\ \text{于 }\operatorname{supp}\chi,
\qquad
a=0\ \text{于 }\operatorname{supp}d\eta,
\]
同时 \(K_2^\eta(0)\) 仍由好球 \(B_{7r}\) 控制。因此需要在半径间留出固定余量，例如：

- \(\chi=1\) 于 \(B_{5r}\)；
- \(\operatorname{supp}\chi\subset B_{6r}\)；
- \(\eta=1\) 于 \(B_{6r}\)；
- \(\operatorname{supp}\eta\subset B_{7r}\)。

距离函数的光滑化也应从稍宽的平台和稍窄的支撑开始，才能在光滑化后保留这些包含关系。高阶 cutoff jets 仍只需逐数据有限。

终端测地线缓冲同样应留固定比例。若中心在 \(B_r(x_\alpha)\)，可取 \(\rho\le r/2\)，或把中心集缩到 \(B_{r/2}\)。在终端度量与初始度量充分接近时，长度 \(\rho\) 的终端测地线便留在 \(B_{2r}(x_\alpha)\subset B_{5r}(x_\alpha)\)。Bishop–Gromov 仍给出中心集体积 \(\ge cA\)。

---

## 4. 同一精确流上的第一退出链

这里的依赖关系不是单线
\[
K_2^\eta\to Y\to J_6.
\]
更准确的是三个并行分支：
\[
K_2^\eta
\Longrightarrow
\begin{cases}
\displaystyle \int_0^tY\le C\gamma K_2^\eta(0),
\quad
Y(t)\le C\gamma K_2^\eta(0)/t,\\[1mm]
\displaystyle J_6(t)\le
e^{C(1+r^{-2})t}J_6(0),\\[1mm]
\displaystyle Q(t)\le
e^{C(1+r^{-2})t}Q(0).
\end{cases}
\tag{4.1}
\]

- 第一行供曲率 Moser 使用；
- 第二行供 Einstein 缺陷 Moser 使用，且不依赖 \(Y\)；
- 第三行供终端 Chern–Weil 再校准使用。

随后
\[
\|aF(t)\|_\infty\le\frac{C\gamma}{t},
\qquad
\|aE(t)\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3},
\tag{4.2}
\]
并且
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2.
\tag{4.3}
\]
式 (4.3)控制全局双 Lipschitz 比较、局部 Sobolev 常数和平台体积。式 (4.2) 在 \(a=1\) 的平台上给出终端统一曲率界。

这些估计只用 cutoff 的一阶界及 signed-Hessian 积分分部；高阶 cutoff jets 只进入逐数据启动与延拓，所以不会把支撑数目或拓扑复杂度带入终端常数。

由于各 \(B_{7r}(x_\alpha)\) 不交，在每个支撑上 \(a=\chi_\alpha^2\)，局部计算不会出现交叉项。全局 \(Q\) 估计可对支撑求和；精确流在 \(a=0\) 的开集上静止，因此补集中的 \(E\) 和体积元也静止。这正是必须先取 \(\varepsilon\to0\) 的原因。

---

## 5. 终端再校准的两个必要修正

为避免与 Einstein 缺陷 \(E=\operatorname{Ric}+g\) 混淆，把异常上同调类记为 \(e_\ell\)。正确恒等式是
\[
I-J=(2\chi+3\tau)(M)=\frac{2A}{3}-q.
\]
定义
\[
D_{\rm av}
=I-\frac{2A}{3}-\frac23\sum_\ell(e_\ell^+)^2.
\]
则
\[
\boxed{
D_{\rm av}
=J-q-\frac23\sum_\ell(e_\ell^+)^2.
}
\tag{5.1}
\]
因此在 \(q\ge0\) 时
\[
0\le D_{\rm av}\le J
\le\frac{Q}{8\pi^2}.
\tag{5.2}
\]

A01 Step41 §7.2 的
\[
J-q-\frac23\left(\sum_\ell(e_\ell^+)^2-A\right)
\]
多出了 \(2A/3\)，必须改为 (5.1)。

更重要的是终端选点密度。Step41 (7.4)
\[
\frac1{4\pi^2}
\left[(s+4)^2+\frac1{16}
(s+8\sqrt6|W^+|)^2+\mathcal G\right]
\]
没有 \(|E|^2\)，所以其拉回均值趋零只能控制标量曲率和 \(W^+\) 谱，不能消去无迹 Ricci 部分。§8.4 从该密度直接写出
\[
\|E_i\|_{L^p_{\rm loc}}\to0
\]
在逻辑上缺少依据。

应改用 Step28 的密度
\[
\boxed{
\Phi_i=
|E_i|^2+(s_i+4)^2+
(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i.
}
\tag{5.3}
\]
由
\[
\int(s+4)^2\le4Q,\qquad
\int(s+8\sqrt6|W^+|)^2\le108Q,\qquad
\int\mathcal G\le6Q
\]
得到
\[
\boxed{\int\Phi_i\le119Q_i(T).}
\tag{5.4}
\]
式 (5.4) 同时提供 Einstein 缺陷、标量校准和 Weyl 谱校准，是后续强收敛所需的正确对象。

---

## 6. Liouville–Rauch、\(W^{2,p}\) 强收敛与 Derdziński

在终端中心集 \(P_i\) 上，
\[
\operatorname{Vol}(P_i)\ge cA_i.
\]
平台曲率界和固定测地线缓冲给出
\[
\int_{P_i}A_\rho\Phi_i(p)\,d\mu(p)
\le C(K,\rho)\int_{M_i}\Phi_i\,d\mu.
\]
这里 Liouville 不变性作用于无权单位切丛测度；径向 Jacobian 用 Rauch 的上下界控制。非负性允许把 \(P_i\) 扩展到整个底流形进行估计，也允许多次覆盖同一点。

由
\[
Q_i(T)/A_i\to0
\]
可选 \(p_i\in P_i\) 使
\[
A_\rho\Phi_i(p_i)\to0.
\tag{6.1}
\]
对拉回度量
\[
\widehat g_i=(\exp_{p_i}^{g_i(T)})^*g_i(T)
\]
有固定球上的截面曲率界和中心非塌缩。缩小一次半径后可取统一 harmonic 坐标，得到
\[
\widehat g_i\to g_\infty
\quad\text{于 }C^{1,\beta}_{\rm loc},
\qquad
\widehat g_i\rightharpoonup g_\infty
\quad\text{于 }W^{2,p}_{\rm loc}.
\]

由 (6.1) 和 (5.3)，
\[
\|E_i\|_{L^2_{\rm loc}}\to0.
\]
曲率统一有界又给出 \(E_i\) 的 \(L^\infty\) 界，所以插值得到每个有限 \(p\) 下
\[
\|E_i\|_{L^p_{\rm loc}}\to0.
\]
在 harmonic 坐标中，
\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=-2(\operatorname{Ric}_{g_i})_{jk}
+Q_{jk}(g_i^{-1},\partial g_i),
\]
右端强收敛于
\[
2(g_\infty)_{jk}
+Q_{jk}(g_\infty^{-1},\partial g_\infty).
\]
内部椭圆估计遂给出
\[
\widehat g_i\to g_\infty
\quad\text{强于 }W^{2,p}_{\rm loc}.
\tag{6.2}
\]
因此曲率张量强 \(L^p\) 收敛，Weyl 模长及特征值缺陷均可通过极限。

极限满足
\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\qquad
s_\infty=-4,
\]
\[
s_\infty+8\sqrt6|W_\infty^+|=0,\qquad
\mathcal G_\infty=0.
\]
弱 Einstein 方程经 harmonic 坐标椭圆正则性给出光滑 \(g_\infty\)。于是
\[
|W_\infty^+|^2=\frac1{24},\qquad
\operatorname{spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Einstein 条件给出 \(\delta W_\infty^+=0\)。Derdziński 定理使
\[
(24|W_\infty^+|^2)^{1/3}g_\infty
\]
局部 Kähler；这里因 \(24|W_\infty^+|^2=1\)，原度量本身局部 Kähler。可是四维 Kähler–Einstein 度量满足
\[
|W^+|^2=\frac{s^2}{24}
=\frac{16}{24}=\frac23,
\]
与 \(1/24\) 矛盾。此终端机制在加入 \(|E|^2\) 后闭合，不需要序列一致的高阶 Shi 型估计。

---

## 7. 族一致量词

若不存在统一 \(\varepsilon_{\mathrm{IL}}\)，可取一列
\[
\delta_i=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_{\infty,\mathrm{op}}
\to0.
\]
初始再校准给出
\[
q_i/A_i\to0,\qquad
D_{{\rm av},i}/A_i\to0,\qquad
\operatorname{Vol}(g_i)/A_i\to32\pi^2/9.
\]
若 \(A_i\to\infty\)，以上统一支撑和流链直接适用。若 \(A_i\) 有界，取子列使 \(A_i=A_0\)；由于
\[
q_i\in\frac13\mathbb Z,\qquad q_i\ge0,
\]
有 \(q_i=0\) 最终成立。此时平台体积仍为固定正数 \(cA_0\)，而终端密度积分为 \(o(A_0)\)，Liouville–Rauch 选择仍然成立。

因此全部常数只来自四维局部几何、固定 \(m\in\{2,3\}\)、吸收参数、\(r\) 和 \(\theta\)，不依赖 \(A,D,q,N\)。经上述公式修订，反证推出族一致 \(\varepsilon_{\mathrm{IL}}>0\)。

所给材料未重现 Step35 的全部 Hessian-\(a\) 指标收缩及 Step32 的完整高指数 Moser 递推；本备忘录核对的是这些模块与单一精确流、全局 \(Q\) 及终端几何之间的数学衔接。若引用的 Step32、Step35 模块按其记录成立，则没有剩余的中间推理缺口。
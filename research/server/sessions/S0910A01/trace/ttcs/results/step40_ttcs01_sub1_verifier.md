# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step39_complete_conditional_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step39.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A03/workspace/notes/step37_transported_deturck_existence.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step41_continuation_criterion_and_first_exit_assembly.md",
    "Sessions/S0910A01/trace/ttcs/results/step39_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Critically verify the assembled four-dimensional negative Ishida--LeBrun defect-gap theorem and A03's claimed discharge of H1, focusing only on mathematical interfaces that could invalidate the proof. User goal is the full Yau Problem 26, but the artifact under review is the restricted negative-family theorem. Read the supplied files and give a direct scientific memo addressing: (1) whether Step39's support Lemma 3.1 proves all cutoff regularity it uses, especially Hessian/higher jets under only Ricci lower bound and mean curvature energy; (2) whether the K2 self-improvement with any additive C0*T is homogeneous enough in collapsed or tiny-support regimes; (3) whether A03 Step40/Step41 sufficiently verify the normalized weighted-U and unweighted-T evolution interfaces, including G, normalization, connection variation, and zero-order T propagation, or still leave structural equations to derive; (4) whether the transported DeTurck existence/restart proof is a complete theorem or a plausible adaptation needing detailed tame estimates; (5) whether terminal recalibration requires q>=0 and selected monopole class with (a^+)^2>=A, and whether Step39's theorem statement says this clearly; (6) whether the exponential-pullback/terminal compactness passage must use inner plateau centers, Liouville averaging on a center set, and strong finite-W^{2,p} convergence rather than weak convergence or Lipschitz-in-metric claims. Conclude what should be repaired next to turn the restricted theorem into a rigorous mathematical result, without treating it as completion of Yau 26.

## Output

# 科学核验备忘录

## 总体结论

当前组装尚不能作为无条件成立的四维 \(\operatorname{Ric}\approx-g\) 缺陷间隙定理。拓扑校准、局部能量链、终端 Derdziński 矛盾之间的总体构想具有实质内容，但六个接口中有四处尚缺证明，两处的现有表述直接不成立：

1. Lemma 3.1 没有从其几何前提推出统一 Hessian 截止函数，更没有推出统一高阶截止导数；
2. \(K_2^\eta\) 自改进中的裸加项 \(C_0T\) 无法在塌缩支撑上统一吸收；
3. Step40 的 \(U_m,T_m\) 演化式仍含未展开的 \(\mathcal G_m,\mathcal N_m\)，而零阶无权 \(T\in L^p\) 传播并未在所给文件中推导；
4. Step37 给出了可信的 Yang 型低阶扰动框架，但没有写出完成 Nash–Moser 所需的 tame 估计；
5. 终端常数 \(119Q(T)\) 需要 \(q=k-A/3\ge0\) 以及终端度量下重新选择满足 \((a^+)^2\ge A\) 的 monopole 类；定理陈述没有写明前者；
6. Step39 的弱 \(W^{2,p}\) 收敛和“曲率量对度量系数 Lipschitz”不足以传递 \(W^+\) 谱校准。这里需要内层中心、Liouville 平均及强有限 \(W^{2,p}\) 收敛，或正时间局部曲率导数估计。

---

## 1. Lemma 3.1 的截止函数正则性

### 最大函数部分能够给出的内容

由 \(\operatorname{Ric}\ge-2g\)、局部 doubling 和 (3.2)，确实可以选出总体积为固定比例的好点集。最大 \(14r\)-分离网也确实给出：

- \(B_{7r}(x_\alpha)\) 两两不交；
- \(G_R\subset\bigcup_\alpha B_{14r}(x_\alpha)\)；
- 借助 Bishop–Gromov，
  \[
  \sum_\alpha\operatorname{Vol}B_{2r}(x_\alpha)\ge c\,\operatorname{Vol}M
  \ge c'A_i.
  \]

但局部能量 \(K_2^\eta(0)\) 覆盖到 \(B_{7r}(x_\alpha)\)，所以还必须明确取
\[
7r\le R.
\]
否则中心处的 \(\mathcal M_R\) 控制只证明 \(B_r\) 上的平均曲率控制，不能推出 (4.2) 所用的整个 \(\eta\)-支撑能量估计。加入 \(7r\le R\) 后，Bishop–Gromov 还可比较 \(B_{5r}\) 与 \(B_{7r}\) 的体积，从而得到
\[
\mathcal S(0)\sqrt{K_2^\eta(0)}
 \le C r^2(1+\Lambda\overline K_0)^{1/2}.
\]

### Hessian 界没有被证明

Lemma 3.1(a) 写有
\[
\|\nabla^2\chi_\alpha\|_\infty\le C r^{-2}.
\]
其证明没有构造这样的函数。Ricci 下界和平均 \(L^2\) 曲率能量通常只能支持带统一梯度的光滑 Lipschitz 逼近；统一完整 Hessian 控制需要更强的局部几何信息。选定中心的平均曲率小也不排除支撑内部存在点状大曲率，因此不能由 (3.3) 推出上述 Hessian 界。

所幸 Step34–35 的 signed Hessian-\(a\) 分部积分只使用
\[
\frac{|da|^2}{a}=4|d\chi|^2\le Cr^{-2},
\]
不需要逐点 \(\nabla^2a\) 控制。因此严密版本可以删除统一 Hessian 界，只保留：

- \(\chi_\alpha\) 光滑；
- \(|d\chi_\alpha|\le C/r\)；
- \(\chi_\alpha=1\) 于内层球；
- \(\operatorname{supp}\chi_\alpha\) 与 \(d\eta_\alpha\) 之间有开邻域间隔。

Step40 使用的高阶截止导数只需对每个固定数据有限；其延拓常数可以依赖该数据，不必沿序列统一。当前文件应明确区分“统一梯度控制”与“每个固定光滑截止函数具有有限高阶导数”。

### 还需一个单一的全局流

§4 按单个 \(\chi_\alpha\) 书写，而 §5、§7 需要同一个终端度量同时覆盖所有 plateau。应明确令
\[
\chi_i=\sum_\alpha\chi_\alpha,\qquad
a_i=\chi_i^2=\sum_\alpha\chi_\alpha^2,
\]
其中最后一个等号利用支撑两两不交，然后只运行一次全局截止流。若分别运行每个局部流，所得终端度量不是同一个对象，§5 的 \(Q\) 求和与 §7 的总体中心选择便不能衔接。

---

## 2. \(K_2^\eta\) 的裸加项不能统一吸收

Step39 的 (4.4) 和 (4.13) 使用
\[
(K_2^\eta)'
 \le C(1+r^{-2}+\mathcal S^2Y)K_2^\eta+C_0,
\]
继而要求
\[
C_0\theta r^2\ll K_2^\eta(0).
\]

Ricci 下界不给固定半径球的体积下界。在塌缩支撑上，即使曲率很小，
\[
K_2^\eta(0)=\int\eta^2(1+|\operatorname{Rm}|^2)
\]
也可以趋于零。因此不存在与支撑无关的 \(\theta>0\) 使
\[
C_0\theta r^2<K_2^\eta(0)
\]
对所有支撑成立。若每个支撑均产生一个裸 \(C_0\)，支撑数还可能趋于无穷。

Step34 已经提供了正确的齐次机制：
\[
(K_2^\eta)'+cD_2^\eta
 \le CY+Cr^{-2}K_2^\eta,
\]
以及
\[
Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta).
\]
吸收 \(D_2^\eta\) 后得到
\[
(K_2^\eta)'\le C(1+r^{-2})K_2^\eta,
\]
于是
\[
K_2^\eta(t)
 \le e^{C(1+r^{-2})t}K_2^\eta(0),
\]
这在任意小体积支撑上仍然有效。若某个低阶来源实际产生
\(C\,\operatorname{Vol}(\operatorname{supp}\eta)\)，也必须写成
\[
C\,\operatorname{Vol}(\operatorname{supp}\eta)
 \le C K_2^\eta(0)
\]
或其随时间的可比较版本，而不能压缩成独立的 \(C_0\)。

因此 Step39 的 F1 自改进只有在删去裸加项或证明其与 \(K_2^\eta\) 成比例后才成立。

---

## 3. Step40–41 尚未完成 \(U,T\) 演化接口

Step40 的核心是 (1.4)–(1.5)，但其中
\[
\mathcal G_m,\qquad \mathcal N_m
\]
仅被描述为“具有相同导数排序”。这不足以确认每个最高阶项都落入其交错归纳结构。

需要逐项处理的具体对象包括：

1. \(G=(g\owedge g)/(2(n-1))\) 的时间变化：
   \[
   \partial_tG
   =\frac{(\partial_tg)\owedge g+g\owedge(\partial_tg)}
          {2(n-1)},
   \qquad
   \partial_tg=-2\operatorname{Ric}(U),
   \]
   它是 \(U\) 的代数项，但高阶协变微分后必须核对最高导数恰为 \(U_m\)。

2. 连接变化：
   \[
   \partial_t\Gamma
   =g^{-1}*\nabla\operatorname{Ric}(U).
   \]
   在
   \([\partial_t,\nabla^m]U\) 和
   \([\partial_t,\nabla^m]T\) 中，它分别产生
   \(\nabla^jU*\nabla^kU\) 与
   \(\nabla^jU*\nabla^kT\)。必须证明没有出现超出当前交错层的
   \(U_{m+1}\) 或 \(T_{m+1}\) 裸项。

3. \(U=aT\) 不满足通常曲率张量的微分 Bianchi 恒等式。把
   \(\nabla^2\operatorname{Ric}(U)\) 化成 \(a\Delta T\) 或
   \(a\Delta U\) 时，会产生 \(\nabla a*\nabla T\) 和
   \(\nabla^2a*T\)。这些正是权重结构最敏感的项，不能只用星号记号概括。

4. Step39 的 (4.12)
   \[
   \frac d{dt}\|T\|_p^p
   +c\int a|\nabla T|^2|T|^{p-2}
   \le C(K+1+r^{-2})\|T\|_p^p+C_p
   \]
   没有在 Step35 中出现。Step35 推导的是带 \(a^{p-2}\) 权的
   \(\operatorname{Rm}\) 能量，而不是无权的移位曲率 \(T\) 估计。
   Step40 和 Step41 又把该无权估计当作 stage zero 输入。因此这一层目前仍是未证明的独立引理。

Step40 的二次分部积分思想确实解决了“当前 \(C_{m+1}\) 被要求进入
\(L^{2p}\)”的问题，但它只验证了假定 (1.4)–(1.5) 后的指数安排，并没有建立这些方程本身。

此外，Step41 §5 把固定的 \(\sup|U|\le K_*\) 放进从 \(t=0\) 开始的 bootstrap，而导出的 Moser 估计只有
\[
|U(t)|\le C\gamma_0/t+C.
\]
光滑初值可在一个数据相关的初始时间段控制 \(U\)，但这样得到的 \(K_*\) 也依赖单个数据；若再用它建立序列统一的 \(K_2\) 估计，常数便不再统一。Step39 原来的 \(K_2\to Y\to\) Moser 链不需要预设固定 \(K_*\)，因而更适合该序列论证。

---

## 4. transported DeTurck 存在性仍是证明框架

Step37 正确识别了两个重要事实：

- gauge 系数必须是 transported coefficient \(\widehat a\)，而不是固定的 \(a\mathcal L_Wg\)；
- 新增项的线性化
  \[
  \delta(-2\widehat a\,\widehat g)
  =-2\widehat a\,h-2(\delta\widehat a)\widehat g
  \]
  不含 \(h\) 的二阶导数，因此不改变退化抛物主部。

这说明 Yang 构造很可能可容纳正规化项。但 Step37 §3 到 §4 的论证仍缺少 Yang 方法真正使用的 tame 估计。尤其没有写出：

- 正则化线性系统的 \(\varepsilon\)-一致高阶能量估计；
- 新增 \(\widehat a h\) 与 \((\delta\widehat a)\widehat g\) 在每个交换导数层的估计；
- 线性右逆对基点 \((\widehat g,\varphi)\) 的 smooth tame 依赖；
- Nash–Moser 邻域内统一的正时间和度量正定性；
- 所引用的 Yang Theorem 8.2 与 Step39 所称 Theorem 4.1 的准确对应；
- 若使用“唯一极大解”，还需要非线性局部唯一性。

“固定点或 Nash–Moser”不能作为同一个未展开步骤：Yang 的退化系统存在导数损失时，普通固定点并非自动可用。

因此，短时存在和从任意光滑终端度量重新启动在当前材料中尚未成为完整引用定理。重新启动本身并不困难：一旦归一化短时定理成立，便可应用于终端光滑度量；真正缺少的是归一化扰动保留 Yang 全部 tame 估计的明确命题及证明。

---

## 5. 终端 recalibration 的 \(q\) 与 monopole 类条件

令
\[
q=k-\frac A3,\qquad
e=(a^+)^2-A.
\]
对终端度量选取满足 \(e\ge0\) 的符号类后，
\[
D_a=J-q-\frac23e.
\]
由于 \(D_a\ge0\)，若 \(q\ge0\)，才有
\[
0\le D_a\le J.
\]
这正是 Step28 的 (1.3) 和 Step39 §6 中
\[
\int(s+8\sqrt6|W^+|)^2\le108Q,\qquad
\int G\le6Q
\]
的依据。

但 Theorem 1.1 只写
\[
k_i/A_i\to1/3,
\]
没有写 \(q_i\ge0\)。若 \(q_i<0\)，正确估计是
\[
D_a\le J+q_-,
\qquad q_-=\max\{-q,0\},
\]
从而
\[
\int\mathfrak D
 \le119Q+912\pi^2q_-.
\]
由于定理已经假设 \(q_i/A_i\to0\)，这个修正式仍足以得到
\[
A_i^{-1}\int\mathfrak D_i\to0
\]
，只是不能继续写纯粹的 \(119Q\) 控制。另一种写法是在定理中明确加入
\(k_i\ge A_i/3\)。

符号类还必须在终端度量上重新选择。正投影依赖度量，初始时选择的
\(\varepsilon\) 不必在终端仍满足 \((a_\varepsilon^+)^2\ge A\)。所需事实是所有符号类均为 monopole 类，并在每个终端度量上用平均恒等式重新选一个符号。

此外，Step39 的 (2.3) 写成
\[
2^{-k}\sum_\varepsilon(a_\varepsilon^+)^2
 =A+\sum_j(E_j^+)^2.
\]
通常直接展开得到的是
\[
2^{-k}\sum_\varepsilon(a_\varepsilon^+)^2
 =(c_1(X)^+)^2+\sum_j(E_j^+)^2
 \ge A+\sum_j(E_j^+)^2,
\]
因为
\[
(c_1(X)^+)^2=A+(c_1(X)^-)^2.
\]
除非前文另有理由证明 \(c_1(X)^-=0\)，这里应使用不等式。它仍然保证至少存在一个符号使 \((a_\varepsilon^+)^2\ge A\)。

---

## 6. exponential pullback 与终端紧致性

### 必须使用真正的内层中心集

Step39 取
\[
P_\alpha=B_{2r}(x_\alpha),
\]
而曲率界只在 \(\chi_\alpha=1\) 的 plateau 上成立。若 \(p\) 接近
\(B_{2r}\) 外缘，长度为固定 \(\rho\) 的终端测地线可能立即离开该区域，因而 Rauch 比较没有所需的沿线曲率控制。

可用的中心集应为更小的球，例如
\[
P_i=\bigcup_\alpha B_r(x_\alpha).
\]
Bishop–Gromov 给出
\[
\operatorname{Vol}B_r(x_\alpha)
 \ge c\,\operatorname{Vol}B_{2r}(x_\alpha),
\]
所以仍有 \(\operatorname{Vol}P_i\ge cA_i\)。再结合终端度量与初始度量的双 Lipschitz 比较，选取固定 \(\rho\ll r\)，便可保证从 \(P_i\) 出发的终端长度 \(\rho\) 测地线都留在 \(\chi=1\) 的较大内层区域。

### 平均公式需要 Jacobian 与 Liouville 测度

应使用 Step28 的量
\[
A_\rho D(p)=
\frac{\int_{S_pM}\int_0^\rho
 D(\exp_p(t\xi))J_p(t,\xi)\,dt\,d\xi}
{\int_{S_pM}\int_0^\rho J_p(t,\xi)\,dt\,d\xi}.
\]
Rauch 给出 \(J_p\) 的上下比较，Liouville 不变性给出
\[
\int_{P_i}A_\rho D(p)\,d\mu(p)
 \le C\int_MD\,d\mu.
\]
随后由 \(\operatorname{Vol}P_i\ge cA_i\) 选择 \(p_i\)。Step39 的平坦
\(dv\) 平均可以通过 Jacobian 比较改写，但必须明确这一中间步骤。

### 弱 \(W^{2,p}\) 不足以传递 \(W^+\) 谱

Step39 §7.2 中“曲率特征值、标量曲率、\(|W^+|\)、\(G\) 对度量系数 Lipschitz”的表述不正确。曲率依赖度量的二阶导数；\(C^{1,\alpha}\) 收敛和弱 \(W^{2,p}\) 收敛并不保证曲率张量、曲率平方或最小特征值强收敛。

现有估计其实提供了获得强收敛的途径。在内层 plateau 上，
\[
\|E_i(T)\|_\infty\le C\delta_i\to0.
\]
经 exponential pullback、固定缩小半径和 harmonic-coordinate 紧致性，可先取得
\[
g_i\to g_\infty\quad\text{于 }C^{1,\beta}.
\]
在 harmonic 坐标中，
\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
 =-2(\operatorname{Ric}_{g_i})_{jk}
   +Q_{jk}(g_i,\partial g_i),
\]
而
\[
\operatorname{Ric}_{g_i}=-g_i+E_i\to-g_\infty
\]
强收敛。椭圆估计于是给出较小球上的强有限
\[
g_i\to g_\infty\quad\text{于 }W^{2,p},\qquad p>4.
\]
因此
\[
\operatorname{Rm}_{g_i}\to\operatorname{Rm}_{g_\infty}
\quad\text{于 }L^p,
\]
随后 \(s_i,W_i^+\) 及 \(W_i^+\) 最小特征值均可强收敛；特征值对有限维自伴算子本身是 Lipschitz 的。这样才能把
\[
\int\mathfrak D_i\to0
\]
传递成极限上的 Einstein 方程和校准谱。

另一条可行路径是利用 \([T/2,T]\) 上内层区域的统一曲率界建立局部正时间曲率导数估计，从而在更小的 exponential pullback 球上取得光滑收敛。无论采用哪条路径，Step39 当前的弱收敛论证都不够。

---

## 严密版本所缺的核心补充命题

要把这一特定四维族的结果变成可独立验证的数学定理，需要形成以下可引用的证明模块：

1. **支撑命题**：只要求统一梯度截止函数、stationary collar、\(7r\le R\)、单一全局截止函数，以及总体积 \(\gtrsim A_i\) 的内层中心集；
2. **齐次 \(K_2\) 命题**：
   \[
   (K_2^\eta)'\le C(1+r^{-2})K_2^\eta,
   \]
   不含与局部体积无关的裸加项；
3. **精确 \(U,T\) 演化命题**：展开 \(G\)、正规化、连接交换子和 Bianchi 余项，并独立证明零阶无权 \(T\in L^p\) 传播；
4. **归一化 Yang 扰动命题**：写出 \(\varepsilon\)-一致 tame 估计和 Nash–Moser 右逆，从而得到短时存在及重新启动；
5. **拓扑校准命题**：明确 \(q\ge0\)，或使用
   \[
   \int\mathfrak D\le119Q+912\pi^2q_-,
   \]
   并在终端度量上重新选择符号类；
6. **终端紧致性命题**：内层中心集、Jacobian 加权 Liouville 平均、缩小半径、harmonic 坐标及强有限 \(W^{2,p}\) 收敛。

这些补充后，现有路线有望给出近临界 Ishida–LeBrun 四流形上的统一 \(\operatorname{Ric}+g\) 缺陷间隙。它仍只涉及一个特定四维拓扑族和 \(\operatorname{Ric}\approx-g\) 情形；原始 Yau 第26题还包含 \(\operatorname{Ric}\approx+g\)、一般四维流形、\(n\ge5\)、仅依赖维数的常数以及 Lean 4 形式化。
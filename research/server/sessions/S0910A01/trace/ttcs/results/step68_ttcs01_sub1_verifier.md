# TTCS Independent Branch Record

```json
{
  "step_id": 68,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step68_restricted_IL_canonical_assembly.md",
    "Sessions/S0910A01/workspace/notes/step67_terminal_recalibration_recovery.md",
    "Sessions/S0910A01/workspace/notes/step62_defect_moser_general_p_proof.md",
    "Sessions/S0910A01/workspace/notes/step64_convention_consistency_sweep.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md"
  ]
}
```

## Task

Verify the mathematical consistency of this assembled restricted Ishida-LeBrun negative-gap theorem. Check specifically:

1. INTERFACE CONSISTENCY: Does the terminal calibration (§3) correctly interface with the flow output (§7)? Is the passage from Q(T)/A_i→0 through the Liouville averaging (§9) to the forbidden-germ contradiction logically complete? Are there any missing hypotheses at any interface?

2. CONVENTION CORRECTNESS: Under T=Rm-G with G=(g⊙g)/(2(n-1)) and Ric(G)=-g, does the pure-scaling correction ∂_tT=-2aT+2aG add a term that is genuinely absorbed by CaF_T^3? Does this break any energy inequality or Moser iteration?

3. UNIFORMITY SEPARATION: Is the distinction between sequence-uniform (first-exit curvature/defect/Q) and datum-dependent (all-order continuation) correctly maintained? Could a datum-dependent quantity leak into the terminal contradiction?

4. DEFECT MOSER ENDPOINT: Is the three-factor route (§6.5) genuinely p-independent? Does S²Y ≤ Cγ³/t come from the curvature branch without circularity? Is the nested Moser product convergence rigorous?

5. FORBIDDEN GERM: Does Φ=0 actually force the specific W+ spectrum (-1/6, 1/12, 1/12)? Is the passage from G_gap=0 to two-eigenvalue W+ correct? Does Derdziński's proposition apply to this exact setting (Einstein, two W+ eigenvalues, dimension 4)?

## Output

# 科学核验备忘录

## 总体结论

终端校准的代数、曲率约定修正以及禁阻芽的谱代数彼此一致。特别是

\[
\int_M\Phi\le119Q
\]

和

\[
\Phi=0\Longrightarrow
\operatorname{Ric}=-g,\qquad
\operatorname{spec}(W^+)=\left(-\frac16,\frac1{12},\frac1{12}\right)
\]

都可由所给公式直接推出。

但当前组装文本还不能单独构成完整证明。主要缺失集中在三个具体数学接口：

1. §4–§8 没有明确定义一个同时作用于全部选定平台的全局截止流，而 §9 的校准和 Liouville 平均要求同一个终端度量。
2. §9.5 从曲率有界和拉回球体积下界直接写出 \(C^\infty\) Cheeger–Gromov 收敛，这一步需要统一曲率导数估计，或改用调和坐标下的有限 \(W^{2,p}\) 椭圆收敛。
3. 三因子 Moser 机制在代数上可行，但 Step 62 中从时空积分递推到最终 \(L^\infty\) 估计的完整推导、实指数正则化以及 \(a=0\) 附近的极限仍只被列出，没有完全展开。

此外，初始体积上界、支持集构造和局部 Sobolev 常数的来源需要补写。

---

## 1. 终端校准与流输出

### 1.1 校准公式本身正确

由

\[
E=\operatorname{Ric}+g
=E^\circ+\frac{s+4}{4}g
\]

以及四维中 \(|g|^2=4\)，确有

\[
|E|^2=|E^\circ|^2+\frac{(s+4)^2}{4},
\qquad
\int(s+4)^2\le4Q,
\qquad
J\le\frac{Q}{8\pi^2}.
\]

Chern–Weil 等式给出

\[
I-J=\frac{2A}{3}-q.
\]

与符号族平均后的 Seiberg–Witten 不等式结合，

\[
D_{\rm av}
=I-\frac23A-\frac23\sum_\ell |e_\ell^+|^2
=J-q-\frac23\sum_\ell |e_\ell^+|^2.
\]

在 \(q\ge0\) 时，

\[
0\le D_{\rm av}\le J.
\]

平方恒等式

\[
\frac{s^2}{24}+2\nu^2
=\frac1{12}f^2+\frac1{216}(s+8\sqrt6\,\nu)^2
\]

也可直接展开核对。由截断型 LeBrun 不等式可得

\[
\int (s+8\sqrt6|W^+|)^2\le108Q,
\qquad
\int\mathcal G\le6Q.
\]

所以 \(119Q\) 的常数计算没有问题。该推导只依赖终端度量仍位于同一光滑流形、保持固定取向，并不依赖校准量沿流输运。

### 1.2 \(Q(0)/A\to0\) 需要一个未写出的体积上界

组装文本写道

\[
Q(0)\le\delta_i^2\operatorname{Vol}(M_i)=O(\delta_i^2A_i),
\]

但定理中的 \(\delta_i\) 是算子范数。严格地说，

\[
|E|_{\mathrm{HS}}^2\le4\delta_i^2,
\qquad
Q(0)\le4\delta_i^2\operatorname{Vol}(M_i).
\]

更重要的是，§4.4 只陈述了体积下界，而这里需要

\[
\operatorname{Vol}(M_i,g_i)\le C A_i.
\]

该上界可以从已有公式推出。因为

\[
s=-4+\operatorname{tr}E,\qquad
|\operatorname{tr}E|\le4\delta_i,
\]

故

\[
I\ge
\frac{(1-\delta_i)^2}{6\pi^2}\operatorname{Vol}(M_i).
\]

另一方面，

\[
I=J+\frac{2A_i}{3}-q_i
\le J+\frac{2A_i}{3},
\qquad
J\le\frac{\delta_i^2}{2\pi^2}\operatorname{Vol}(M_i).
\]

因此对充分小的 \(\delta_i\)，

\[
\left[
\frac{(1-\delta_i)^2}{6\pi^2}
-\frac{\delta_i^2}{2\pi^2}
\right]\operatorname{Vol}(M_i)
\le\frac{2A_i}{3},
\]

从而 \(\operatorname{Vol}\le CA_i\)。加入这一步后，

\[
\frac{Q(0)}{A_i}=O(\delta_i^2)\to0,
\qquad
\frac{Q(T)}{A_i}\to0
\]

才完整成立。

### 1.3 当前文本没有提供 Liouville 平均所需的单一终端度量

§4–§5 对每个中心写出 \(\chi_\alpha\) 并分别讨论对应流；§7–§9 却使用一个全局 \(g_i(T)\)、一个全局 \(Q(T)\) 和一个终端平台集 \(P_i\)。这两种表述不等价。

如果每个 \(\alpha\) 独立流动，则得到的是不同度量 \(g_{i,\alpha}(T)\)。此时不能在一个单位切丛上对所有中心应用 Liouville 不变性，也不能用一次全局校准得到除以 \(\operatorname{Vol}(P_i)\asymp A_i\) 的抵消。

需要的数学对象是一个全局平滑截止函数 \(a_i\)，满足：

- 在一个体积 \(\ge\alpha A_i\) 的内平台上 \(a_i=1\)；
- 支持分量具有统一分离或统一重叠次数；
- \(|\nabla a_i|\)、低阶截止项具有统一估计；
- 辅助函数 \(\eta_\alpha\) 的导数支撑处，全局 \(a_i\) 也确实为零。

一种可行组织是先用局部倍增性质把球族分成有限个颜色，选取其中体积比例固定的一类，使扩大的支持互不相交，再以这些分量组成单个全局截止函数。当前组装没有给出这一步。

### 1.4 Liouville 平均还需要明确的几何缓冲

公式

\[
\int_{P_i}\mathcal A_\rho\Phi
\le C(K,\rho)\int_{M_i}\Phi
\]

本身与单位切丛上的测度不变性一致，但它要求从每个 \(p\in P_i\) 出发、长度不超过 \(\rho\) 的相关测地线始终位于曲率受控平台中。应明确选择

\[
\rho<
\min\{c\,r,\;cK^{-1/2}\}
\]

并利用 \(V(T)\to0\) 把初始平台缓冲转移到终端度量。这样拉回指数映射在该半径内无共轭退化，Rauch 比较才给出统一体积下界和 Jacobian 控制。

### 1.5 §9.5 的 \(C^\infty\) 收敛理由不充分

统一 \(|\operatorname{Rm}|\) 与体积下界通常给出调和坐标中的 \(C^{1,\alpha}\) 紧致性，而不是自动给出 \(C^\infty\) 收敛。这里有两条可行的严格通路：

1. 在 \([T/2,T]\) 的平台缓冲区上使用局部 Ricci 流导数估计。因为
   \[
   |\operatorname{Rm}(t)|\le C/t
   \]
   在该时段统一有界，局部抛物型估计可产生终端时刻的统一曲率导数界。
2. 使用 Step 8 已写出的调和坐标通路。曲率有界给出 \(E\) 的统一 \(L^\infty\) 界，而
   \[
   \fint|E|^2\to0
   \]
   通过插值得到所有有限 \(L^p\) 中的收敛。调和坐标方程
   \[
   g^{ab}\partial_a\partial_b g_{jk}
   =-2\operatorname{Ric}_{jk}+Q(g^{-1},\partial g)
   \]
   随后给出内部强 \(W^{2,p}\) 收敛；极限满足 Einstein 方程，再由椭圆正则性变光滑。

第二条通路只使用序列统一的低阶信息，更符合 §11 所陈述的参数分离。

---

## 2. 曲率约定与纯缩放修正

在

\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\operatorname{Rm}-G
\]

及 Hamilton 收缩约定下，

\[
\operatorname{Ric}(G)=-g,\qquad
\operatorname{Ric}(T)=E.
\]

对一般变分 \(h=\partial_tg=-2aE\)，

\[
\partial_tG
=\frac1{n-1}(h\owedge g)
=-\frac{2a}{n-1}(E\owedge g).
\]

所以

\[
\partial_tT
=\partial_t\operatorname{Rm}
+\frac{2a}{n-1}(E\owedge g).
\]

在纯缩放情形 \(a=1,E=g\) 中，

\[
\partial_t\operatorname{Rm}=-2\operatorname{Rm},
\qquad
\partial_tG=-4G,
\]

因而

\[
\partial_tT=-2T+2G.
\]

这里的 \(2aG\) 只应理解为纯缩放分量或一般演化式中的一个零阶分量，不是一般截止流的完整精确公式。

该项不会破坏 \(H_2\) 或 Moser 估计。由于 \(G\) 的范数是维数常数且 \(F_T\ge1\)，

\[
a|\langle T,G\rangle|
\le CaF_T
\le CaF_T^2
\le CaF_T^3.
\]

因此它既可作为 \(CH_2\) 型低阶项处理，也可并入原有的 \(Y=\int aF_T^3\) 项。对一般 \(p\) 次能量，它产生 \(CaF_T^p\) 或更低阶反应项，不引入新的大指数吸收要求。

空间协变导数方面，\(\nabla G=0\)，故

\[
\nabla^m(aG)
\]

只产生截止函数导数与 \(G\) 的乘积，属于原有截止喷流结构。约定修正确实不会改变缺陷方程，也不会改变三因子 Moser 的核心项。

---

## 3. 序列统一量与逐数据量

逐数据存在时间和高阶延拓常数可以依赖初始度量；它们只负责排除一个光滑分支在 \(T=\theta r^2\) 之前终止。这一思路是合理的。不过 §8.3 的“有限次重启”表述不够严密：局部存在时间可能逐次缩短。正确形式应是取最大光滑时间 \(T_*<\theta r^2\)，由所有固定背景 \(C^m\) 估计得到 \(g(t)\to g(T_*)\) 的光滑极限，再直接延拓越过 \(T_*\)。

当前终端论证中有一处逐数据量渗入：§9.5 使用 \(C^\infty\) 紧致性，却没有序列统一的高阶估计。若使用上面的调和坐标 \(W^{2,p}\) 通路，则不再需要逐数据高阶常数；若坚持 \(C^\infty\) Cheeger–Gromov 通路，则必须从平台上的局部抛物型估计重新得到序列统一的导数界。

此外，全局截止函数的支持重叠次数若随 \(i\) 增长，§7 中对局部 \(Q\) 不等式求和会引入依赖 \(i\) 的系数。统一分离或有限着色是保持

\[
Q(T)\le e^{C(1+r^{-2})T+C_VV(T)}Q(0)
\]

中常数固定的必要成分。

---

## 4. 三因子缺陷 Moser 机制

### 4.1 三因子分解与吸收正确

恒等式

\[
\eta^2a^{p-1}F s^{p/2}
=(aF^3)^{1/3}
(\eta^2a^{p-2}s^{p/2})^{1/3}
z_p^{4/3}
\]

的所有 \(\eta,a,s\) 次数都匹配。Hölder 给出

\[
P_p\le Y^{1/3}J_p^{1/3}\|z_p\|_4^{4/3}.
\]

再由

\[
\|z_p\|_4^2
\le C\mathcal S p^2(Q_p+r^{-2}J_p)
\]

及 Young 不等式，可得

\[
pP_p
\le\varepsilon pQ_p
+C_\varepsilon p^N\mathcal S^2YJ_p
+Cp^Nr^{-2}J_p.
\]

因为主耗散含 \(cp^2Q_p\)，\(\varepsilon pQ_p\) 对所有 \(p\ge2\) 都可统一吸收。这里所谓与 \(p\) 无关，准确含义是“不需要 \(\gamma\le c/p\)”；右侧仍有可接受的多项式因子 \(p^N\)。

### 4.2 \(Y\) 的来源没有逻辑循环

在联合首次退出论证中，先暂时假设 \(\Gamma\le\gamma_*\) 与 \(V\le V_*\)。曲率支路只用这两个暂时假设得到

\[
\mathcal S^2Y\le\frac{C\gamma^3}{t}.
\]

缺陷支路随后产生 \(\|aE\|_\infty\)，并用它改进 \(V\)。因此曲率支路并没有预先使用最终的缺陷端点。

但 \(t^{-1}\) 在 \((0,T]\) 上不可积；实际可用的是每个固定观测时刻对应的时段

\[
[t/2,t],
\]

或 Step 62 的嵌套时段 \([\tau_k,t]\)。在这些时段上

\[
\int_{\tau_k}^t\mathcal S^2Y\,ds\le C\gamma^3.
\]

组装文本中的“可积系数”应按这一局部时段含义理解。

### 4.3 无限乘积收敛没有代数问题，但递推证明尚未完全写出

若确有

\[
C_k=C\mathcal S p_k^N4^kt^{-1},
\qquad
p_k=6\left(\frac32\right)^k,
\]

则

\[
\sum_k\frac1{p_k}<\infty,
\qquad
\sum_k\frac{k}{p_k}<\infty,
\]

所以来自 \(p_k^N\)、\(4^k\)、\(\mathcal S\) 和 \(t^{-1}\) 的乘积都收敛。

当前 Step 62 仍有两个未完成的技术点：

- 能量不等式先按偶整数 \(p\) 陈述，而迭代立刻经过 \(p=9,13.5,\ldots\)。需要对 \(s_\varepsilon=s+\varepsilon\) 写出实指数版本，再令 \(\varepsilon\to0\)。
- 为消除种子中的额外 Sobolev 因子，文本改用
  \[
  I_k=\int_{\tau_k}^tJ_{p_k},
  \]
  并直接陈述
  \[
  I_{k+1}\le Cp_k^N\mathcal S(L_kI_k)^{3/2}.
  \]
  需要完整展示时间截止后如何同时控制
  \(\sup J_{p_k}\) 与 \(\int\|z_{p_k}\|_4^2\)，以及
  \[
  J_{3p/2}\le J_p^{1/2}\|z_p\|_4^2.
  \]
  这一结构是可行的，但现有文件中的推导仍过于压缩。

因此三因子机制是正确方向，最终端点还需要上述细节才能成为可独立复核的证明。

---

## 5. 禁阻芽

由 \(\Phi=0\) 的各平方项，

\[
E=0,\qquad s=-4,
\qquad s+8\sqrt6|W^+|=0,
\]

故

\[
|W^+|=\frac1{2\sqrt6},
\qquad
|W^+|^2=\frac1{24}.
\]

令

\[
\xi=w+\sqrt{\frac23}|W^+|
=w+\frac16.
\]

最低特征值的标准估计给出

\[
0\le\xi\le\frac16.
\]

此时

\[
f=-3,\qquad a_*=f+2\xi=-3+2\xi<0,
\]

且

\[
\mathcal G
=f^2-a_*^2
=4\xi(3-\xi).
\]

所以 \(\mathcal G=0\) 强制 \(\xi=0\)，即

\[
w=-\frac16.
\]

若另两个特征值为 \(x,y\)，则

\[
x+y=\frac16,\qquad
x^2+y^2=\frac1{24}-\frac1{36}=\frac1{72}.
\]

由此 \(xy=1/144\)，于是

\[
x=y=\frac1{12}.
\]

因此谱确为

\[
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

Einstein 条件通过第二 Bianchi 恒等式给出

\[
\delta W^+=0.
\]

该谱在每一点恰有两个不同特征值，且 \(W^+\neq0\)，所以 Derdziński Proposition 5 可局部应用。其共形因子为

\[
(24|W^+|^2)^{1/3}=1,
\]

故原度量本身局部 Kähler。对于 Kähler–Einstein 四维度量，取 Kähler 取向时

\[
|W^+|^2=\frac{s^2}{24}.
\]

这里 \(s=-4\)，右侧为 \(2/3\)，与 \(1/24\) 冲突。禁阻芽的核心数学完全成立。

局部积分下界的常数应明确写成依赖

\[
K,\quad v,\quad \rho
\]

的 \(\eta(K,v,\rho)>0\)，然后与流产生的固定 \(K,v,\rho\) 配对。若使用紧致性证明该下界，也应采用前述调和坐标强 \(W^{2,p}\) 通路，或补充统一导数估计。

---

## 6. 另外两个支持层问题

1. §4.1 中某中心的最大平均有界，并不能推出整个 \(B_{10r}\) 上截面曲率逐点有界；而且最大函数只取 \(\rho\le r\)，不能直接控制 \(B_{10r}\) 的 \(H_2\) 种子。半径需重新设置，Sobolev 估计应由初始 Ricci 双侧控制与归一化局部 Sobolev 定理获得，而不是由逐点截面曲率获得。
2. 要得到低能量中心占据 \(A_i\)-比例体积，需要先证明
   \[
   \int_MF_T^2\le CA_i.
   \]
   这应由初始体积上界、四维 Chern–Weil 公式以及 IL 拓扑数据给出。当前 §4 直接陈述了选取结果，没有展示这项全局能量估计。

---

## 最终评估

以下部分已经数学闭合：

- 终端 \(119Q\) 校准；
- \(T=\operatorname{Rm}-G\) 的符号与范数约定；
- \(2aG\) 零阶项的能量吸收；
- 三因子吸收中不再需要 \(\gamma\le c/p\)；
- \(\Phi=0\) 的谱计算及 Derdziński 局部矛盾。

当前仍需补足的核心材料是：

- 一个全局截止函数及其统一支持几何；
- 初始体积上界和全局 \(F_T^2\) 预算；
- 时空积分版 Moser 递推的完整实指数证明；
- 终端调和坐标强收敛，或平台上的统一局部曲率导数估计。

这些补齐后，终端校准—Liouville 平均—禁阻芽这条链在逻辑上可以闭合；以现有组装文本而言，这条链尚缺上述几个明确的分析模块。
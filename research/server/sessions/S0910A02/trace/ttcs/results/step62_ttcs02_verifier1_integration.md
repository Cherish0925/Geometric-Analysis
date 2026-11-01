# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 62,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step62_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step62_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the current peer restricted negative Ishida--LeBrun/cutoff-flow chain for Yau Problem 26, using the supplied A01/A03 notes plus A02's Step-62 triage. Do not decide the full Yau-26 problem. Assess whether the chain, as written, plausibly proves a restricted four-dimensional negative-sign gap, and identify exact load-bearing gaps or scope limitations. Focus on: per-datum transported-cutoff DeTurck existence; low-order first-exit/Moser modules imported into common time; all-order continuation without ungauged uniqueness; terminal Liouville-pullback compactness and Derdzinski forbidden-germ contradiction; whether any conclusion gives dimension-only constants or a counterexample. Return a mathematical verification memo with concrete items A02 should audit next.

## Integrated Scientific Memo

# 数学核验备忘录：受限四维负号 Ishida–LeBrun／截断流链

## 结论

现有材料支持一个**结构连贯但仍有关键条件输入未核验**的定理框架：

\[
\inf_{\substack{M\in\mathcal F\\ g\in\mathrm{Met}(M)}}
\left\|g^{-1}(\operatorname{Ric}_g+g)\right\|_{L^\infty,\mathrm{op}}
\ge \varepsilon_{\mathcal F}>0,
\]

其中 \(\mathcal F\) 必须是一个明确指定的四维 Ishida–LeBrun 无 Einstein 家族，并且支撑选择、低阶首退出估计、SW/Chern–Weil 标定及终端几何常数在该家族上一致。

现有笔记中，高阶延拓、无唯一性的终端拼接、Liouville 拉回球选择以及禁忌 germ 的基本机制均具有可信的数学结构。真正承重而尚未在所给材料中闭合的是：

1. 序列一致的低阶 \(H_2,Y,J_6,Q_\alpha,(\Gamma,V)\) 模块；
2. 过渡环带 \(0<a<1\) 上全局非加权基层
   \[
   T_0,T_1,U_1,C_2\in L^\infty_tL^q_x;
   \]
3. 终端标定密度 \(\mathfrak D\)（尤其 \(\mathcal G\)）及
   \[
   \int\mathfrak D\le C\delta^2A
   \]
   的来源；
4. Derdziński 命题的准确假设、定向约定及局部适用性；
5. IL 地理数据和所有常数的家族一致性。

因此，当前链条可称为**可信的受限定理架构**，但不能称为所给材料内部自足的完整证明。

---

## 1. 每个初值的 transported-cutoff DeTurck 存在性

### 已核实部分

令
\[
X=-\beta^2W(G),\qquad \partial_t\varphi=X\circ\varphi,\qquad g=\varphi^*G.
\]
则
\[
\partial_tg=\varphi^*(\partial_tG+\mathcal L_XG).
\]
恒等式
\[
\mathcal L_{\beta^2W}G
=\beta^2\mathcal L_WG+
2\operatorname{sym}\bigl(d(\beta^2)\otimes W_G^\flat\bigr)
\]
说明 Step 56 中额外的交叉项正好补偿变系数 Lie 导数中的 \(d(\beta^2)\) 项。只要其 \(R+Q\) 确为标准 Ricci–DeTurck 坐标表达式，即
\[
G^{-1}D^2G+R+Q=-2\operatorname{Ric}_G+\mathcal L_WG,
\]
便得到
\[
\partial_tg=-2(\beta\circ\varphi)^2(\operatorname{Ric}_g+g).
\]
同时
\[
\frac d{dt}\beta(t,\varphi(t,x))
=\partial_t\beta-\beta^2W\cdot D\beta=0,
\]
故 \(\beta\circ\varphi=\chi\)，从而
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]
拉回符号和系数是正确的。

固定 \(\varepsilon,\nu>0\) 时，主符号两块为
\[
(\beta^2+\varepsilon)G^{ab}\xi_a\xi_b I_{\mathrm{Sym}^2},
\qquad
\nu\bar g^{ab}\xi_a\xi_b,
\]
故在 \(G>0\) 时为强抛物系统。标量方程在空间极值点满足 \(D\beta=0\)，输运项消失，\(\nu\bar\Delta\beta\) 具有正确符号，因而
\[
0\le\beta\le1
\]
的最大值原理成立。

tame 插值计数也正确。对 \(q_i>4\) 取
\[
\theta_i=\frac{q_i-4}{m-4},
\]
若有 \(k\ge2\) 个高阶因子，则
\[
\sum\theta_i
\le \frac{m+2-4k}{m-4}
\le \frac{m-6}{m-4}<1,
\]
故余项只线性依赖当前高阶 \(H^m\) 范数，而不会产生多个高范数的乘积。所列四类顶阶项均可用
\[
\frac{\beta^2}{\beta^2+\varepsilon}\le1,
\qquad
\frac{\beta^4}{\beta^2+\varepsilon}\le1
\]
及一次分部积分处理，没有显式引入 \(\varepsilon^{-1}\) 或 \(\nu^{-1}\)。

### 尚需逐项核验

该模块仍缺少以下证明接口：

- \(R+Q\) 与 Ricci–DeTurck 算子的完整指标恒等式；
- \(m=s_0\) 时包含所有背景曲率交换子的多项式能量估计；
- 所调用的固定参数强抛物存在及延拓定理与所用 Sobolev 空间完全匹配；
- \((\varepsilon,\nu)\to0\) 时获得所有时空 \(C^k\) 收敛的紧性论证；
- 反复时间微分中无隐藏的 \(\varepsilon^{-1},\nu^{-1}\)；
- 极限在 \(\{a=0\}\) 上确实满足静止方程，而非仅满足弱松弛方程。

这些更像未展开的标准但必要接口；当前展示的公式中未发现内在矛盾。此定理只能给出**每个初值自己的局部时间**，不能给出序列一致观察时间。

---

## 2. 低阶首退出／Moser 模块是当前主要缺口

公共时间依赖以下序列一致估计：

\[
H_2^\alpha=\int\eta_\alpha^2F_T^2\,d\mu,
\]
\[
\|aF_T(t)\|_\infty\le \frac{C\Gamma}{t},
\qquad
\|aE(t)\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3},
\]
以及 \(J_6\)、局部 \(Q_\alpha\) 传播和 \((\Gamma,V)\) 严格自改善。这些均由当前文件引用早期步骤，却未在当前材料中重证。

### 非加权 \(H_2\) 必不可少

\(H_2\) 必须是
\[
\int\eta_\alpha^2F_T^2,
\]
而不能插入 \(a\)。否则在 \(a\ll1\) 的过渡环带会丢失曲率控制，而后续非加权 \(T_m\) 能量正需要该区域的信息。

### signed-Hessian 机制必须在原始张量式中保留

模型上
\[
\int(\nabla^2a)_{ij}\mathcal B^{ij}
=-\int \nabla a*\nabla\mathcal B
\]
以及
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2
\]
确能避免使用一致的 \(\|\nabla^2\chi\|_\infty\)。

但必须检查实际 \(H_2,Y,J_6,Q_\alpha\) 方程中的每个 \(\nabla^2a\) 项，在取绝对值或形成标量上包络之前是否仍保持可分部积分的带符号张量缩并。若过早丢失符号，此修复无效。

### 最危险的是过渡环带基层

高阶归纳需要
\[
T_0,T_1,U_1,C_2\in L^\infty([\tau,T_*);L^q(M))
\quad\forall q<\infty.
\]
但
\[
\|aT\|_\infty<\infty
\]
不能推出 \(T\) 在 \(a\to0\) 处有界。区域应分三类：

- \(a=1\) 平台：加权估计即非加权估计；
- \(a=0\) 开集：流静止，初始光滑性给出逐初值控制；
- \(0<a<1\) 过渡环带：仅由 \(aT\) 无法控制 \(T\)，必须由被引用的独立零阶 seed 或 \(W^{1,p}\to L^\infty\) 桥梁处理。

需要明确证明该桥梁覆盖整个过渡环带，并在整个 \([\tau,T_*)\) 上一致，而不是只在 \(\{a\ge a_0\}\) 上成立。这是高阶链条最直接的分析承重点。

严格缓冲也不可省略。只有当 \(1-\rho\) 支持于一个 \(a\equiv0\) 的开集时，才有
\[
Q_{\rm global}(t)
=Q_{\rm rest}(0)+\sum_\alpha Q_\alpha(t).
\]

---

## 3. 不使用 ungauged 唯一性的全阶延拓

### 删除原始唯一性论证是正确的

对
\[
F(g)=-2a(\operatorname{Ric}_g+g)
\]
的线性化主符号含 Ricci 的规范核。取 \(\xi=e_1\) 和
\[
h=\operatorname{diag}(1,-\varepsilon,0,0)e^{ikx^1}
\]
得到
\[
\langle\sigma_\xi(DF)h,h\rangle
=(\varepsilon-\varepsilon^2)k^2>0.
\]
因此不能从未定规的 Ricci 算子推出
\[
\frac d{dt}\|g_1-g_2\|_2^2\le C\|g_1-g_2\|_2^2.
\]
当前笔记改用全阶终端收敛和自治方程拼接，是正确修复。

### \(m\ge2\) 的 current-pair 估计结构成立

关键余项为
\[
I_m=\int\chi|C_{m+1}|\,|U_1|\,|U_m|^{p-1}.
\]
令 \(f=\chi|U_m|^{p/2}\)，则
\[
I_m\le
\|f\|_4\|C_{m+1}\|_p
\|U_1\|_4\|U_m\|_p^{p/2-1},
\]
所用指数满足
\[
\frac14+\frac1p+\frac14+\frac{p-2}{2p}=1.
\]
Sobolev 和 Young 给出
\[
I_m\le\varepsilon D^U_{m,p}
+C\bigl(1+\|C_{m+1}\|_p^p+\|U_m\|_p^p\bigr),
\]
前提是 \(U_1\in L^4\) 已由基层给出。故归纳必须从 \(m=2\) 开始；在 \(m=1\) 时 \(U_1\) 本身就是当前未知量，论证会循环。

恒等式
\[
(B_1*B_1)*T=4(C_1*C_1)*U
\]
准确消除了表面上的裸 \(T\) 系数。类似地，
\[
aT_m
=U_m-\sum_{q=1}^m\binom mq B_q*T_{m-q}
\]
将当前非加权 \(T_m\) 化为当前 \(U_m\) 加严格低阶项。

signed Hessian 项
\[
\int\chi(\nabla^2\chi)_{ij}\mathcal B^{ij}(U_m)
\]
经一次分部积分可估为
\[
\varepsilon D^U_{m,p}
+C\|\nabla\chi\|_\infty^2\|U_m\|_p^p.
\]

### 仍需验证的高阶结构

脚本只验证整数阶分配，不验证张量恒等式。必须对以下内容作一次指标级审计：

- 全协变 Riemann 变分；
- 空间交换子和时间交换子中的度量缩并；
- 重排公式
  \[
  \nabla^r(\partial_t\Gamma)
  =g^{-1}*U_{r+1}
   +\sum_{q\le r-1}T_q*U_{r-q};
  \]
- 范数及体积形式的时间变化；
- 不存在遗漏的裸当前 \(T_m\)、\(U_{m+1}\) 或 \(C_{m+2}\)。

固定背景联络转换的三角结构可信：
\[
\bar\nabla^m\partial_tA
=g^{-1}*U_{m+1}+B_0*A_m+\text{低阶},
\]
但仍应明确写出 \(A_j*U_k\) 乘积的 Sobolev 分配，确保所谓“有界当前系数”确由一个额外导数和 Sobolev 嵌入得到。

### 终端自治拼接成立

一旦有
\[
g(t)\to g_*\quad\text{于 }C^\infty
\]
且 \(g_*>0\)，定义
\[
\mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g),\qquad
\mathcal F_{\ell+1}=D\mathcal F_\ell[\mathcal F].
\]
旧支和任意从 \(g_*\) 出发的新局部解在拼接点的所有时间导数均等于 \(\mathcal F_\ell(g_*)\)，所以拼接解光滑。此处无需重叠区唯一性。

---

## 4. 终端 Liouville 选择与拉回紧性

### Liouville 平均和 \(A\)-消去正确

若
\[
\operatorname{Vol}(P_i)\ge c_0A_i,\qquad
\int_{M_i}\mathfrak D_i\le C_0\delta_i^2A_i,
\]
径向 Jacobi 比较和 Liouville 测度不变性给出
\[
\int_{P_i}\mathcal A_\rho\mathfrak D_i(p)\,d\mu_i(p)
\le C\int_{M_i}\mathfrak D_i\,d\mu_i.
\]
故存在 \(p_i\in P_i\) 使
\[
\mathcal A_\rho\mathfrak D_i(p_i)
\le \frac{CC_0}{c_0}\delta_i^2.
\]
拓扑尺度 \(A_i\) 精确消去；没有旧的 \(A_i^{-1/2}\) 损失。指数映射折叠不影响该论证，因为积分是在初始单位切向量空间上进行。

### 拉回球紧性机制正确，但缓冲须证明

在沿所有长度不超过 \(\rho\) 的径向测地线都有曲率上界、且 \(\rho\) 小于一致共轭半径时，\((\exp_p)^*g\) 是切空间球上的光滑度量。中心处实际上有
\[
\exp^{(\exp_p)^*g}_0(v)=v,
\]
这给出所需的中心 injectivity，而不仅是体积非塌缩。

需要从原始支撑缓冲和终端双 Lipschitz 控制中明确推出：从 \(P_i\) 出发、长度 \(\rho\) 的所有径向测地线始终停留在曲率受控平台上。当前 Step 60 将其列为假设，尚未展示推导。

曲率界及中心 injectivity 给出调和坐标中的 \(C^{1,\alpha}\)、\(W^{2,q}\) 界。由
\[
\mathfrak D_i\ge|E_i|^2,\qquad
\mathcal A_\rho\mathfrak D_i(p_i)\to0
\]
得到 \(E_i\to0\) 于局部 \(L^2\)，再由曲率一致有界插值到所有有限 \(L^q\)。调和坐标 Ricci 方程随后给出光滑 Einstein 极限及
\[
g_i\to g_\infty
\quad\text{强于 }W^{2,q}_{\rm loc}.
\]
这足以使曲率及其连续代数函数在 \(L^q/L^1\) 中收敛，但不足以直接处理含 \(\nabla W^+\) 的密度。因此必须核实 \(\mathcal G\) 纯粹是 \(W^+\) 的代数谱函数。

---

## 5. Derdziński 禁忌 germ

若极限满足
\[
\operatorname{Ric}=-g,\qquad s=-4,
\]
及
\[
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right),
\]
则
\[
|W^+|^2=\frac1{24}.
\]

Einstein 四维度量满足 \(\delta W^+=0\)。若 Derdziński 定理在当前定向下确实说明“两特征值且非零的 \(W^+\)”使
\[
(24|W^+|^2)^{1/3}g
\]
局部 Kähler，则因 \(24|W^+|^2=1\)，原度量本身局部 Kähler。

对复定向的 Kähler 曲面，
\[
\operatorname{Spec}(W^+)
=\left(\frac s6,-\frac s{12},-\frac s{12}\right).
\]
当 \(s=-4\) 时，
\[
\operatorname{Spec}(W^+)
=\left(-\frac23,\frac13,\frac13\right),
\qquad
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
与 \(1/24\) 矛盾。这个禁忌 germ 的数值计算是正确的。

A01 笔记中另一处把相同谱写成
\[
\left(\frac13,\frac13,-\frac23\right)
\]
只是排列；但必须固定 \(W^+\) 所对应的定向，不能混用复定向与反定向。

A03 的替代论证声称“常谱投影引理”给出 \(\nabla W^+=0\)，这一点不能仅由特征值常数推出，因为本征空间可以旋转。除非有额外 Codazzi/散度自由方程并完整证明投影引理，否则不应把它作为已核实步骤。更稳妥的是直接使用上述 Derdziński 局部 Kähler 结论与 \(1/24\neq2/3\) 的矛盾。

仍须对原文核实：

- 命题是否局部适用于 germ；
- 重根及简单根的符号/极值条件；
- 共形指数和正规化常数；
- SW 标定使用的 \(W^+\) 定向是否与 Kähler 公式一致。

---

## 6. 终端标定及 IL 地理仍是独立承重点

现有材料没有给出：

- \(\mathcal G\) 的显式定义；
- \(\mathcal G\ge0\) 的证明；
- \(\mathcal G=0\) 强迫指定谱的代数推导；
- 常数 \(119\) 和
  \[
  \int\mathfrak D\le119\,Q
  \]
  的完整来源；
- \(q_{\rm top}\ge0\) 及 monopole sign family 在不等式中的精确作用；
- \(A\) 的定义及
  \[
  \operatorname{Vol}(P)\ge c_0A
  \]
  的构造；
- 哪个 Ishida–LeBrun 定理排除该家族上**任意符号** Einstein 度量。

因此，A01 Step 58 所称“只有每初值存在性仍为条件输入”不符合当前材料本身：低阶首退出模块、终端标定和 Derdziński 来源同样未在所给文件中闭合。

---

## 7. 所得结论的准确范围

算子缺陷界
\[
\left\|g^{-1}(\operatorname{Ric}_g+g)\right\|_{\mathrm{op}}\le\delta
\]
等价于
\[
-(1+\delta)g\le\operatorname{Ric}_g
\le-(1-\delta)g.
\]

若一般地 \(c<C<0\) 且
\[
cg\le\operatorname{Ric}_g\le Cg,
\]
令
\[
\widetilde g=-\frac{c+C}{2}\,g,
\]
则
\[
-(1+\varepsilon)\widetilde g
\le\operatorname{Ric}_{\widetilde g}
\le-(1-\varepsilon)\widetilde g,
\qquad
\varepsilon=\frac{C-c}{-(c+C)}.
\]
因此一个已证的 \(\varepsilon_{\mathcal F}\) 只会排除该 IL 家族上足够窄的**相对负号区间**。

它不产生只依赖维数的常数。当前常数依赖
\[
r,\theta,\gamma_*,V_*,c_0,K,\rho
\]
以及支撑构造、Sobolev、标定和地理数据。

它也不是 Yau 第 26 题的反例：反例需要在无 Einstein 流形上实际构造满足候选维数统一区间的度量；该链恰恰证明某些无 Einstein 流形不能具有任意紧的 \(\operatorname{Ric}\approx-g\) 度量。它同样不证明完整负号命题，因为没有覆盖所有无 Einstein 四流形。正号、一般四维拓扑及 \(n\ge5\) 均未涉及。

---

## 建议 A02 下一步按依赖顺序核验

1. **过渡环带基层**：完整证明
   \[
   T_0,T_1,U_1,C_2\in
   L^\infty([\tau,T_*);L^q(M))
   \]
   对所有有限 \(q\) 成立，尤其不能由 \(aT\) 除以 \(a\) 得出。

2. **低阶原始演化账本**：逐项核验 \(H_2,Y,J_6,Q_\alpha\) 和 \((\Gamma,V)\) 的微分不等式，确认所有 cutoff Hessian 项都可在保留符号时分部积分，并且一致常数只依赖 \(\|\nabla\chi\|_\infty\)。

3. **DeTurck 存在性接口**：核实 Ricci–DeTurck 指标恒等式、\(m=s_0\) 能量、固定参数延拓及 \((\varepsilon,\nu)\to0\) 的全时空光滑紧性。

4. **终端标定原式**：给出 \(\mathcal G\) 的公式、非负性、零集，重推
   \[
   \int\mathfrak D\le119Q
   \]
   的符号和拓扑抵消。

5. **Derdziński 原文匹配**：核实局部性、定向、重特征值假设和共形正规化；优先采用 Kähler 范数 \(1/24\neq2/3\) 的矛盾，不依赖未经证明的“常谱即平行”断言。

6. **高阶张量族指标审计**：独立验证 (T1)–(T6)、(U1)–(U7) 的完备性，特别是时间交换子重排后不存在裸当前 \(T_m\)。

7. **家族一致性**：明确 \(\mathcal F,A,q_{\rm top},c_0,K,\rho\)、缓冲半径及排除所有 Einstein 度量的准确 IL 假设。

完成前两项和第 4 项最可能改变当前“可信条件链”是否能升级为严格受限定理的判断。
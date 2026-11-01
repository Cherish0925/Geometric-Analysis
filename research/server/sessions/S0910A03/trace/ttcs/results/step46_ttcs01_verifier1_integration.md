# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 46,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step46_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step46_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently reconstruct the support-selection and simultaneous first-exit portion of the proposed family-uniform negative Ricci-defect gap for the Ishida–LeBrun geography. Work on one exact degenerate normalized cutoff flow obtained by the Step 45 coefficient-regularization limit. Check the quantifiers and all collapse-sensitive constants: maximal-function threshold, weighted coloring and disjoint outer buffers, smooth cutoffs with only a uniform gradient bound, a single global coefficient, matched local Sobolev domains, initial K2 and gamma, moving Sobolev comparison, homogeneous K2-to-Y propagation, fixed J6, all-p defect Moser, integrable metric drift, global unweighted Q, and continuation to T=theta r^2. Identify any load-bearing mathematical failure or domain/weight mismatch; if repairable, give a precise corrected construction and dependency argument rather than merely listing concerns. Distinguish per-datum continuation estimates from sequence-uniform first-exit estimates.

## Integrated Scientific Memo

# 核验结论：支撑选择与同步首次退出

对 Step 45 系数正则化极限所得的一条固定退化流
\[
\partial_tg=-2a(\Ric_g+g),\qquad   
a=\sum_{\alpha}\chi_\alpha^2,
\]
支撑选择和序列一致的首次退出链可以闭合，但必须采用下面的修正版。主要修复是：

1. 按局部体积权重而非中心数选择颜色；
2. 使整个 Sobolev 外域两两不交，而不只是活动支撑不交；
3. 用无量纲小量 \(\mathcal S_\alpha K_{2,\alpha}^{1/2}\)，不能要求四维未归一化曲率积分因缩小半径而变小；
4. 所有局部估计固定在初始域上，再由可积度量漂移搬运 Sobolev 常数；
5. \(J_6\) 只负责 Moser 初始指数；全 \(p\) 缺陷迭代还必须使用 \(\mathcal S^2Y\)；
6. 序列一致首次退出与逐数据延拓必须严格区分。

以下给出匹配所有权重和量词的构造。

---

## 1. 参数顺序与全局几何输入

设反证序列满足
\[
\delta_i=\|g_i^{-1}(\Ric_{g_i}+g_i)\|_{\infty,\op}\to0.
\]
在先用混合 monopole 不等式得到 \(q_i/A_i\to0\) 后，可丢弃有限项，使
\[
\Ric_{g_i}\ge-2g_i,\qquad
v_-A_i\le \Vol(M_i,g_i)\le v_+A_i,
\]
以及
\[
\int_{M_i}F_{i,0}^2\,d\mu_{g_i}\le L A_i,\qquad
F_{i,0}=(1+|\Rm_{g_i}|^2)^{1/2}.
\tag{1.1}
\]
这里 \(v_\pm,L\) 是允许的 Ishida–LeBrun geography 内一致的常数；现有材料不足以称 \(L\) 为所有四流形上的普适常数。

正确选择顺序为
\[
\gamma_{\rm abs}\;\to\;\kappa\;\to\;r\;\to\;N_{\rm col}
\;\to\;\theta,d_0\;\to\;\delta_*.
\tag{1.2}
\]
其中先令 \(C\kappa<\gamma_{\rm abs}\)，再把 \(r\) 取得足够小以控制坏集。不能先固定 \(r\) 后任意缩小 \(\kappa\)，因为坏集界含 \(r^4/\kappa^2\)。

---

## 2. 修正后的支撑选择

固定 \(R_0\le1\)，定义截断中心极大函数
\[
\mathcal M_{R_0}f(x)=
 \sup_{0<s\le R_0}\fint_{B_s(x)}f.
\]
由 \(\Ric\ge-2g\) 下的局部 doubling/覆盖论证，
\[
\Vol\{\mathcal M_{R_0}f>\lambda\}
 \le \frac{C_M}{\lambda}\int_Mf.
\tag{2.1}
\]
令
\[
\lambda=\frac{\kappa^2}{r^4},\qquad
\mathcal G_i=
\left\{x:\mathcal M_{R_0}(F_{i,0}^2)(x)
 \le\frac{\kappa^2}{r^4}\right\}.
\]
取 \(8r<R_0\) 且
\[
C_ML\,\frac{r^4}{\kappa^2}\le\frac{v_-}{2},
\tag{2.2}
\]
则
\[
\Vol(\mathcal G_i)\ge\frac{v_-}{2}A_i.
\tag{2.3}
\]

在 \(\mathcal G_i\) 中取极大 \(r\)-分离网 \(\{x_\beta\}\)。把中心有限着色，使同色中心至少相距 \(18r\)。Bishop–Gromov 给出只依赖维数和固定半径比的度数界，因此颜色数
\[
N_{\rm col}<\infty
\]
不依赖塌缩体积。

必须按权重
\[
w_\beta=\Vol B_r(x_\beta)
\]
选颜色。由于 \(\mathcal G_i\subset\bigcup_\beta B_r(x_\beta)\)，存在颜色类 \(\mathcal A_i\) 使
\[
\sum_{\alpha\in\mathcal A_i}\Vol B_r(x_\alpha)
 \ge \frac{v_-}{2N_{\rm col}}A_i.
\tag{2.4}
\]
同色的 \(B_{8r}(x_\alpha)\) 两两不交。

选择光滑固定函数
\[
\chi_\alpha=1\ \text{于 }B_{4r}(x_\alpha),\qquad
\supp\chi_\alpha\Subset B_{5r}(x_\alpha),
\]
\[
\eta_\alpha=1\ \text{于 }B_{6r}(x_\alpha),\qquad
\supp\eta_\alpha\Subset B_{7r}(x_\alpha),
\tag{2.5}
\]
并满足
\[
|d\chi_\alpha|_{g_i}+|d\eta_\alpha|_{g_i}\le Cr^{-1}.
\tag{2.6}
\]
高阶 cutoff jets 对每个固定数据有限，但不要求序列一致。令
\[
\Omega_{\alpha,i}=B_{8r}(x_\alpha),\qquad
a_i=\sum_{\alpha\in\mathcal A_i}\chi_\alpha^2.
\tag{2.7}
\]
则
\[
0\le a_i\le1,\qquad
a_i=\chi_\alpha^2\text{ 于 }\Omega_{\alpha,i},
\]
且
\[
a_i=da_i=0\quad\text{于 }\supp d\eta_\alpha.
\tag{2.8}
\]
这同时匹配 \(K_2,Y,J_6\)、全 \(p\) Moser 以及全局 \(Q\) 的积分域；外域两两不交还避免了全局 \(Q\) 求和时的隐藏重叠因子。

---

## 3. 塌缩敏感的初值归一化

设
\[
V_{\alpha,i}=\Vol_{g_i}\Omega_{\alpha,i}.
\]
需要的局部 Sobolev 输入是固定外域上的体积归一化形式
\[
\|u\|_4^2
 \le\mathcal S_{\alpha,i}(0)
 \bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\quad
\mathcal S_{\alpha,i}(0)
 \le C_S\frac{r^2}{\sqrt{V_{\alpha,i}}},
\tag{3.1}
\]
其中 \(u\) 支撑在相应内域，\(C_S\) 只依赖维数、固定半径比和下 Ricci 界的无量纲乘积。这一精确形式是所有塌缩消去的承重点。

由极大函数在半径 \(8r\) 处的定义直接得到
\[
\fint_{\Omega_{\alpha,i}}F_{i,0}^2
 \le\frac{\kappa^2}{r^4}.
\tag{3.2}
\]
因此
\[
K_{\alpha}(0):=
 \int_{\Omega_{\alpha,i}}\eta_\alpha^2F_{i,0}^2
 \le \frac{\kappa^2}{r^4}V_{\alpha,i},
\]
以及
\[
\gamma_\alpha(0)
 :=\mathcal S_{\alpha,i}(0)K_\alpha(0)^{1/2}
 \le C\kappa.
\tag{3.3}
\]
局部体积恰好消去。

Step 41 中“继续缩小 \(r\) 即可令
\(\int_{B_{7r}}|\Rm|^2\le\gamma_0^2\)”的说法不成立：四维中
\(V_{-2}(7r)/r^4\) 在 \(r\to0\) 时趋于非零常数。下游真正需要的是 (3.3)，不是未归一化 \(L^2\) 小量。

此外
\[
J_{6,\alpha}(0)
 =\int\eta_\alpha^2a_i^4|E_i(0)|^6
 \le C\delta_i^6V_{\alpha,i},
\tag{3.4}
\]
且
\[
Q_i(0)=\int_M|E_i(0)|^2
 \le C\delta_i^2\Vol(M_i),\qquad
Q_i(0)/A_i\to0.
\tag{3.5}
\]

---

## 4. 一条固定极限流及同步首次退出

对每个 \(i\)，固定 Step 45 的某个系数正则化极限解
\[
\partial_tg=-2a_i(\Ric_g+g),\qquad g(0)=g_i.
\tag{4.1}
\]
\(a_i\) 是流形上的单个固定光滑函数； transported coefficient 只出现在 DeTurck 构造中。

定义
\[
\mathfrak d_i(t)=
 \int_0^t\|a_iE(s)\|_{\infty,\op}\,ds.
\tag{4.2}
\]
则
\[
e^{-2\mathfrak d_i(t)}g_i
 \le g(t)\le
e^{2\mathfrak d_i(t)}g_i.
\tag{4.3}
\]
故固定初始域和 cutoff 可始终使用，并且
\[
\mathcal S_\alpha(t)
 \le e^{C\mathfrak d_i(t)}\mathcal S_\alpha(0),\qquad
|d\chi_\alpha|_{g(t)}+|d\eta_\alpha|_{g(t)}
 \le e^{\mathfrak d_i(t)}Cr^{-1}.
\tag{4.4}
\]

令 \(T_i^*\) 为所有 \(t\le\min(T_{\max,i},\theta r^2)\) 的上确界，使对每个 \(\alpha\) 和 \(s\le t\)：
\[
K_\alpha(s)\le2K_\alpha(0),\qquad
\mathfrak d_i(s)\le d_0.
\tag{4.5}
\]
Sobolev 控制由第二条件和 (4.4) 自动携带，无需另设一个逻辑独立的退出条件。于该区间，
\[
\mathcal S_\alpha(t)K_\alpha(t)^{1/2}
 \le e^{Cd_0}\sqrt2\,C\kappa,
\tag{4.6}
\]
故初始选择足够小的 \(\kappa,d_0\) 后，所有吸收一致成立。

---

## 5. \(K_2\to Y\) 及曲率 Moser

设
\[
D_{2,\alpha}
 =\int\eta_\alpha^2a_i|\nabla\Rm|^2,\qquad
Y_\alpha=\int\eta_\alpha^2a_iF^3.
\]
张量能量不等式和匹配域上的插值给出
\[
K_\alpha'+cD_{2,\alpha}
 \le CY_\alpha+C(1+r^{-2})K_\alpha,
\tag{5.1}
\]
\[
Y_\alpha
 \le C\gamma_\alpha(t)
 \bigl(D_{2,\alpha}+r^{-2}K_\alpha\bigr).
\tag{5.2}
\]
吸收后
\[
K_\alpha'\le C(1+r^{-2})K_\alpha.
\]
取 \(\theta\) 使
\[
e^{C(1+r^{-2})\theta r^2}
=e^{C\theta(1+r^2)}\le\frac32,
\tag{5.3}
\]
便有严格改进
\[
K_\alpha(t)\le\frac32K_\alpha(0).
\tag{5.4}
\]

进一步，
\[
\int_0^tY_\alpha\le C\gamma_\alpha(0)K_\alpha(0),
\qquad
\int_0^t\mathcal S_\alpha^2Y_\alpha
 \le C\gamma_\alpha(0)^3.
\tag{5.5}
\]
好切片加 Grönwall 给出
\[
Y_\alpha(t)
 \le\frac{C\gamma_\alpha(0)K_\alpha(0)}{t},
\qquad
\mathcal S_\alpha(t)^2Y_\alpha(t)
 \le\frac{C\gamma_\alpha(0)^3}{t}.
\tag{5.6}
\]
于是全 \(p\) 曲率迭代得到
\[
\|a_iF(t)\|_{L^\infty(\Omega_\alpha)}
 \le\frac{C\gamma_\alpha(0)}t.
\tag{5.7}
\]

---

## 6. 固定 \(J_6\)、全 \(p\) 缺陷与可积漂移

固定指数估计为
\[
J_{6,\alpha}'\le C(1+r^{-2})J_{6,\alpha},
\]
故
\[
J_{6,\alpha}(t)\le C\delta_i^6V_{\alpha,i}.
\tag{6.1}
\]

但这并不直接给出 Moser 阶梯。对每个实数 \(p\ge6\)，必须使用 Step 39 的齐次估计
\[
H_{p,\alpha}
 =\int\eta_\alpha^2a_i^{p-2}|E|^p,
\]
\[
z_{p,\alpha}
 =\eta_\alpha a_i^{(p-1)/2}|E|^{p/2},
\]
\[
H_{p,\alpha}'
 +c\|\nabla z_{p,\alpha}\|_2^2
 \le Cp^4
 \bigl(1+r^{-2}+\mathcal S_\alpha^2Y_\alpha\bigr)
 H_{p,\alpha}.
\tag{6.2}
\]
这里 \(H_{6,\alpha}=J_{6,\alpha}\)，且 Sobolev 变量和初值域完全匹配。

固定 \(p=6\) 的两因子吸收不能迭代到 \(p\to\infty\)：它会要求
\(\gamma\lesssim p^{-1}\)。全 \(p\) 阶梯必须使用三因子分解，把反应项转化为
\(Cp^4\mathcal S^2Y\) 的 Grönwall 系数，并保留 \(q(q-1)X'_p\) 以获得 \(p\)-一致的梯度控制。

结合 (5.6) 与 (6.1)，Moser 迭代给出
\[
\boxed{
\|a_iE(t)\|_\infty
 \le C\delta_i\left(\frac{r^2}{t}\right)^{1/3}.
}
\tag{6.3}
\]
于是
\[
\mathfrak d_i(\theta r^2)
 \le C\delta_i\theta^{2/3}r^2.
\tag{6.4}
\]
当 \(i\) 足够大时这严格小于 \(d_0/2\)，从而同时改进漂移和移动 Sobolev 条件。

因为外域两两不交，全局 \(\|a_iE\|_\infty\) 是各局部范数的最大值，不随支撑个数累积。

---

## 7. 全局无权 \(Q\)

令
\[
Q(t)=\int_M|E|^2,\qquad
X(t)=\int_Ma_i|\nabla E|^2.
\]
有
\[
Q'+cX
 \le C(1+r^{-2})Q
 +C\sum_\alpha\int_{\Omega_\alpha}F(\chi_\alpha E)^2.
\tag{7.1}
\]
对每个支撑，
\[
\int_{\Omega_\alpha}F(\chi_\alpha E)^2
 \le C\gamma_\alpha(t)
 \left(
 \int_{\Omega_\alpha}a_i|\nabla E|^2
 +r^{-2}\int_{\Omega_\alpha}|E|^2
 \right).
\tag{7.2}
\]
吸收梯度项并利用 \(\Omega_\alpha\) 两两不交，
\[
Q(t)\le e^{C(1+r^{-2})t}Q(0).
\tag{7.3}
\]
因此
\[
Q(\theta r^2)/A_i\to0.
\tag{7.4}
\]
\(J_6\) 或 \(\|aE\|_\infty\) 均不能替代这个全局无权估计。

---

## 8. 到达 \(T=\theta r^2\)：量词分离

由 (5.4) 和 (6.4)，首次退出条件都有严格改进，所以
\[
T_i^*=\min(T_{\max,i},\theta r^2).
\tag{8.1}
\]

若 \(T_{\max,i}<\theta r^2\)，取 \(\tau=T_{\max,i}/2\)。由 (5.7)
\[
\sup_{M\times[\tau,T_{\max,i})}
 \left|a_i\left(\Rm+\frac{g\owedge g}{6}\right)\right|
 <\infty,
\tag{8.2}
\]
而 (6.4) 给出有限双 Lipschitz 比较。Step 45 的逐数据交错顺序
\[
T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to\cdots
\tag{8.3}
\]
再给出所有有限阶空间估计，并允许在终点重新运行系数正则化构造。其常数可依赖
\[
g_i(\tau),\ \tau,\ T_{\max,i},\ 
\{\nabla^m\chi_\alpha\}_{m\ge2}
\]
及该单个数据的无权 \(T\)-范数；它们完全不是序列一致常数。由此排除 \(T_{\max,i}<\theta r^2\)，所以
\[
T_i^*=\theta r^2.
\tag{8.4}
\]

序列一致的对象是：支撑体积比例、\(\gamma\)、\(K_2,Y,J_6\)、全 \(p\) 缺陷、两个 Moser 端点、漂移和 \(Q/A\)。高阶 cutoff jets 与延拓估计仅逐数据有限。

---

## 9. 尚存的承重问题

在给定材料内部，序列一致首次退出部分经上述修复后没有剩余的域或权重冲突。尤其 Step 45 保留了
\[
\frac{|B_1|^2}{b}\le4|C_1|^2,\qquad
\frac{\chi^2}{b}\le1,
\]
以及顶阶项的 \(\chi C_{m+2}U_0\) 权重，修复了旧版裸 \(C_{m+2}U\) 的不可吸收问题。

但若要求完全独立的无条件证明，逐数据延拓仍有一个精确待核对象：必须从真实的全协变 Riemann 变分逐指标证明 Step 45 的族
\[
(T1)-(T6),\qquad (U1)-(U7)
\]
确实穷尽所有时间、空间换序项，并确认没有产生裸 \(C_{m+2}U_0\)、未加权当前 \(T_0\) 系数或需要 \(\varepsilon^{-1}\) 的项。现有“110/110”组合脚本本身不能验证张量收缩或 PDE 存在性。

同样，系数正则化极限给出共同逐数据时间区间的论证依赖 Step 45 所述高阶能量和固定坐标紧致性；它不提供退化流唯一性。对本任务指定的“一条固定极限流”和存在性拼接，唯一性不是必需的，但若要定义规范的最大流或证明正则化子序列无关，则仍需唯一性。

因此，精确结论是：**支撑选择和同步序列一致首次退出链在上述四项修复后闭合；到达 \(\theta r^2\) 的最后一步依赖逐数据 Step 45 张量延拓，而其完整逐指标穷尽性仍是现有材料中唯一主要未完全审计的承重对象。**
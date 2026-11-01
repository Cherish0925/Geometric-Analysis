# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 44,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step44_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step44_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently review the restricted four-dimensional negative Ishida--LeBrun defect-gap chain as assembled in A01. Focus on whether the proof now coherently runs on one exact degenerate cutoff flow after coefficient regularization, and whether the analytic estimates feed the terminal Derdzinski contradiction without a hidden unsupported step. Please examine especially: (1) A01 Step43 §6 saying C_{m+1} is a previous layer versus A03 Step45/TTCS correction that it is the current partner of U_m and closes by same-exponent L^p energies; (2) whether coefficient-regularized flows with b=chi^2+eps^2 are used only to construct a common-time smooth limit solving the exact a=chi^2 flow before stationary collars, frozen complement, disjoint supports, and global Q are applied; (3) support construction with maximal-function good sets, disjoint buffers, one global a=sum chi_alpha^2, inner centers, and plateau volume from Vol/A -> 32 pi^2/9; (4) first-exit chain K2^eta -> integrated Y -> J6 -> Moser endpoints and global Q on the same exact flow; (5) terminal recalibration with q>=0 and the corrected D_av identity; (6) Liouville--Rauch pullback, strong finite W^{2,p} convergence, and Derdzinski forbidden germ. Return a direct scientific memo: which links are now sound, which statements in the notes must be corrected, and whether the family-uniform restricted gap follows after those corrections. Do not treat this as a solution of full Yau Problem 26.

## Integrated Scientific Memo

# 科学复核备忘录

## 结论

这条受限的四维负号 Ishida–LeBrun 链，在若干明确修订后，确实可以连成作用于**同一条精确退化流**
\[
\partial_tg=-2a(\Ric_g+g),\qquad a=\sum_\alpha\chi_\alpha^2
\]
上的族一致反证链。正则化系数
\[
b_\varepsilon=a+\varepsilon^2
\]
只能用于构造公共正时间上的光滑极限；冻结补集、静止 collar、支撑不交求和和全局 \(Q\) 必须在 \(\varepsilon\to0\) 后的精确流上使用。

不过，A01 当前不能原样宣布“全部链条已无缺口”。必须修正：

1. \(C_{m+1}\) 是 \(U_m\) 的**当前伙伴**，不是 previous layer；
2. Step43 的加权能量闭合应替换为 A03 Step45 的同指数联合能量；
3. Step41 的终端 \(D_{\rm av}\) 公式和终端非负密度仍写错；
4. 支撑构造需修正曲率积分阈值和辅助 cutoff 缓冲；
5. Step45 tensor ledger 有数个字面公式修正；此外，若要求完全自包含，曲率 ledger 和 defect ledger 仍应成为明确证明的指标引理。

在把 Step34–35 的 defect/curvature 变分模块视为已核准输入，并加入以下修订后，族一致的 restricted gap
\[
\varepsilon_{\rm IL}>0
\]
成立；它与 \(A,D,q,N\) 和输入度量无关。这里不涉及完整 Yau 第26题。

---

## 1. 正确的导数层级：\((U_m,C_{m+1})\) 必须联合闭合

令
\[
V=U_m,\qquad Z=C_{m+1}=\nabla^{m+1}\chi .
\]
cutoff jet 演化为
\[
\partial_tC_{m+1}
 =\sum_{r+s=m-1}U_{r+1}*C_{s+1},
\]
其最高分配是
\[
U_m*C_1.
\]
所以 \(C_{m+1}\) 不可能在估计 \(U_m\) 前已由归纳得到。

A01 Step43 §6 中

> “\(C_{m+1}\in L^q\) by induction”

必须删除。正确结论是同指数联合估计
\[
\frac d{dt}\left(\|U_m\|_p^p+\|C_{m+1}\|_p^p\right)
+c_{m,p}\int b|\nabla U_m|^2|U_m|^{p-2}
\le C_{m,p}\left(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\right).
\tag{1}
\]

顶阶项
\[
\chi C_{m+2}*U_0*P(U_m)
\]
积分分部后产生
\[
C_1*Z*U_0*P(V),\quad
\chi Z*U_1*P(V),\quad
\chi Z*U_0*\nabla P(V).
\]
最后一项由
\[
\left|\int\chi ZU_0|V|^{p-2}\nabla V\right|
\le \eta\int\chi^2|\nabla V|^2|V|^{p-2}
+C_{\eta,p}K^2\int |Z|^2|V|^{p-2}
\]
及
\[
\int |Z|^2|V|^{p-2}
\le \frac2p\|Z\|_p^p+\frac{p-2}{p}\|V\|_p^p
\]
在同一能量中闭合；不需要 previous-layer \(L^{2p}\) 控制。

低阶端点也应明确：

- \(m=1\)：\(\chi C_2*U_1*P(U_1)\) 直接按 signed-Hessian 处理；
- \(m=2\)：二次积分分部产生的
  \(\chi C_2*U_2*P(U_2)\) 仍须再做 signed-Hessian 分部积分；
- 完成 \((U_m,C_{m+1})\) 后才估计 \(T_m\)。

故正确交错顺序是
\[
T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots .
\]

---

## 2. H-WU 的实质结构正确，但 Step43 §6 证明应由 Step45 取代

抛物形式中有两个 \(C_{m+2}\) 来源：

1. Hessian 系数项
   \[
   (\nabla^{m+2}a)*(aE)
   =2\chi C_{m+2}*(aE)+\cdots;
   \]
2. 从 \(a\Delta U\) 抽取出的
   \[
   -\nabla^m((\Delta a)U)
   =-2\chi\,\operatorname{tr}(C_{m+2})U+\cdots.
   \]

两者都带必要的 \(\chi\)，不存在裸的 \(C_{m+2}U\)。这一权重结论与 A03 Step45 相符。但是，Step43 §6 只按第一个来源展示积分分部，并错误调用 previous-layer \(C_{m+1}\)。应将两个来源统一归入 (1) 的联合估计。

Step45 本身还应纳入已识别的字面修正：

- 若
  \[
  G=\frac{g\owedge g}{2(n-1)},\qquad\partial_tg=-2S,
  \]
  则
  \[
  \boxed{\partial_tG
  =-\frac{S\owedge g+g\owedge S}{n-1}},
  \]
  不是分母 \(2(n-1)\)；
- 当前变量表补入 \(bT_m\)、\(bU_m\)；
- 空间交换子的零阶曲率因子必须写成
  \[
  b\Rm=U-bG;
  \]
- \(U_m\) 空间交换子的 \(bT_m*U_0\) 应显式转换为
  \[
  U_m*U_0-\sum_{q=1}^m B_q*T_{m-q}*U_0.
  \]

这些都是低阶或已可闭合项，不推翻结论。

---

## 3. 正则化只负责构造精确退化流

令不交支撑上的
\[
\chi_{\rm glob}=\sum_\alpha\chi_\alpha .
\]
因为至多一个 \(\chi_\alpha\) 非零，
\[
\chi_{\rm glob}^2=\sum_\alpha\chi_\alpha^2=a.
\]
因此 Step45 的单 cutoff 正则化可用于
\[
b_\varepsilon=\chi_{\rm glob}^2+\varepsilon^2.
\]

逻辑顺序必须是：

1. 对每个 \(\varepsilon>0\)，在 DeTurck 系统中输运系数
   \[
   \widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1};
   \]
2. 拉回后得到
   \[
   \partial_tg_\varepsilon
   =-2b_\varepsilon(\Ric_{g_\varepsilon}+g_\varepsilon);
   \]
3. 用无 \(\varepsilon^{-1}\) 的联合有限-\(L^p\) 能量、固定背景连接差和第一退出改进获得公共逐数据时间；
4. 固定背景坐标下取 \(C^\infty\) 子列极限，得到
   \[
   \partial_tg=-2a(\Ric_g+g);
   \]
5. **仅从此时起**使用：
   - \(a=0\) 处度量冻结；
   - collar 静止；
   - 不交支撑求和；
   - 全局 \(Q\) 的“活跃部分加冻结补集”分解。

正则化流在 \(\chi=0\) 处仍以 \(-2\varepsilon^2(\Ric+g)\) 演化，故不能提前使用冻结性质。

退化流唯一性并非该反证所需。存在一条实际极限流即可；从光滑正定端点重新启动时，自治方程决定全部时间 jets，因而可光滑拼接。A01 H-DT 中“任意零阶 tame 扰动自动保持可逆”的表述过宽；对当前证明，Step45 的正则化—紧性路线更直接。

---

## 4. 支撑选择基本正确，但需三项修订

### 4.1 好集与平台体积

由初始 pinching，充分大 \(i\) 时
\[
\Ric_{g_i}\ge-(1+\delta_i)g_i\ge-2g_i,
\]
故固定尺度 doubling、截断极大函数弱型估计可用。

最大 \(r\)-分离网覆盖好集；有限着色后，每个颜色类的 \(B_{7r}\) 两两不交。由于
\[
\mathrm{good}\subset\bigcup_\alpha B_r(x_\alpha)
\subset\bigcup_\alpha B_{5r}(x_\alpha),
\]
至少一个颜色类的 \(B_{5r}\) 并集具有 \(cA_i\) 体积。结合
\[
\frac{\Vol(g_i)}{A_i}\to\frac{32\pi^2}{9}
\]
即得族一致平台体积。

### 4.2 初始曲率阈值

若极大函数阈值是 \(\widetilde\gamma^2/r^4\)，则直接有
\[
r^4\fint_{B_{7r}(x_\alpha)}|\Rm|^2
\le\widetilde\gamma^2.
\]
Step41 (2.5) 无需先转到 \(B_{R_0}\)。

若后续要求非归一化阈值
\[
\int_{B_{7r}}|\Rm|^2\le\gamma_{\rm abs}^2,
\]
不能仅靠缩小 \(r\) 实现，因为四维中
\[
V_{-2}(7r)/r^4\to \omega_4 7^4.
\]
应先取
\[
\widetilde\gamma=c_*\gamma_{\rm abs}
\]
且 \(c_*\) 足够小，再选择 \(r\) 保持好集体积。

### 4.3 辅助 cutoff 和测地缓冲

Step34 的 \(K_2^\eta\) 要求
\[
\eta=1\text{ on }\supp\chi,\qquad
a=0\text{ on }\supp d\eta.
\]
应采用例如
\[
\chi=1\text{ on }B_{5r},\quad
\supp\chi\subset B_{6r},\quad
\eta=1\text{ on }B_{6r},\quad
\supp\eta\subset B_{7r}.
\]
平滑化距离 cutoff 时需预留这些严格余量。

终端内中心可取 \(B_r\) 或更小集合，并选 \(\rho\le r/2\)，使终端长度-\(\rho\) 测地线在小漂移后仍留在 \(B_{2r}\subset B_{5r}\)。Bishop–Gromov 仍给出中心集体积 \(\ge cA_i\)。

---

## 5. 第一退出依赖不是串行 \(Y\to J_6\)，而是三个并行分支

在同一条精确 \(a\)-流上，正确结构为
\[
K_2^\eta\Longrightarrow
\begin{cases}
\displaystyle
\int_0^tY\le C\gamma K_2^\eta(0),\quad
Y(t)\le C\gamma K_2^\eta(0)/t,\\[1mm]
\displaystyle
J_6(t)\le e^{C(1+r^{-2})t}J_6(0),\\[1mm]
\displaystyle
Q(t)\le e^{C(1+r^{-2})t}Q(0).
\end{cases}
\tag{2}
\]
其中：

- \(Y\) 分支供曲率 Moser；
- \(J_6\) 分支供 defect Moser，且不依赖 \(Y\)；
- 全局 \(Q\) 分支供终端 Chern–Weil 再校准。

Moser 端点为
\[
\|aF(t)\|_\infty\le\frac{C\gamma}{t},
\qquad
\|aE(t)\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3},
\]
所以
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2.
\]
后式同时控制双 Lipschitz 比较、移动 Sobolev 常数和平台体积；前式在 \(a=1\) 平台上给终端曲率界。

应把参数顺序写明：先固定吸收尺度和 \(r\)，再取统一小 \(\theta\)，使
\[
e^{C(1+r^{-2})\theta r^2}\le e^{C\theta(1+r^2)}<2,
\]
最后用 \(\delta_i\to0\) 严格改进漂移退出条件。

### 尚需如何表述 defect ledger

Step45 核验的是 \(T,U\) 曲率 ledger，而 \(J_6,Q\) 使用的是
\[
(\partial_t-a\Delta)|E|^2
=-2a|\nabla E|^2+\Sigma_E
\]
及 signed Hessian tensor
\[
B_{\rm def}
=2g|E|^2+2(\tr E)E-4E^2.
\]
供应材料中的 Step34、Step36 给出了这一结构和能量推导，但 Step34 自己仍把完整指标推导列为义务。因而：

- 若 Step35 的 defect 变分及 signed-Hessian 指标计算已作为核准模块，则 (2) 闭合；
- 若要求从本输入独立重建每个指标收缩，则 defect ledger 仍是唯一直接影响 \(J_6\)、Moser defect 端点和全局 \(Q\) 的解析义务。

不能用 Step45 的曲率 ledger 自动替代它。

---

## 6. 终端再校准必须修正两处

为避免与 Einstein defect \(E=\Ric+g\) 混淆，将异常上同调类记为 \(e_\ell\)。正确恒等式是
\[
I-J=\frac{2A}{3}-q.
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
\tag{3}
\]
所以 \(q\ge0\) 时
\[
0\le D_{\rm av}\le J\le\frac{Q}{8\pi^2}.
\]

Step41 §7.2 中
\[
J-q-\frac23\left(\sum_\ell(e_\ell^+)^2-A\right)
\]
是错误的，必须换成 (3)。

第二个更关键的错误是 Step41 (7.4) 的终端密度没有 \(|E|^2\)。仅从
\[
(s+4)^2,\quad
(s+8\sqrt6|W^+|)^2,\quad G
\]
的拉回均值趋零，不能推出无迹 Ricci 消失。因此 §8.4 的
\[
\|E_i\|_{L^p_{\rm loc}}\to0
\]
不能由 Step41 (7.4) 推出。

应使用 Step28 的非负密度
\[
\boxed{
\Phi_i=
|E_i|^2+(s_i+4)^2+
(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i.
}
\tag{4}
\]
由
\[
\int(s+4)^2\le4Q,\qquad
\int(s+8\sqrt6|W^+|)^2\le108Q,\qquad
\int\mathcal G\le6Q
\]
得到
\[
\int\Phi_i\le119Q_i(T).
\tag{5}
\]
常数 \(119\) 与未归一化的 (4) 配套；Step41 (7.4) 中的 \(1/(4\pi^2)\) 和 \(1/16\) 版本不能再与 \(119Q\) 混用。

---

## 7. Liouville–Rauch、强 \(W^{2,p}\) 极限和 Derdziński 矛盾闭合

由
\[
\Vol(P_i^{\rm in})\ge cA_i,\qquad Q_i(T)/A_i\to0
\]
及 (5)，Liouville–Rauch 给出
\[
\int_{P_i^{\rm in}}A_\rho\Phi_i(p)\,d\mu(p)
\le C(K,\rho)\int_M\Phi_i\,d\mu,
\]
故可选 \(p_i\) 使
\[
A_\rho\Phi_i(p_i)\to0.
\]

拉回度量
\[
\widehat g_i=(\exp_{p_i}^{g_i(T)})^*g_i(T)
\]
在固定缩小球上有：

- 统一截面曲率界；
- Rauch Jacobian 下界和中心非塌缩；
- 统一 harmonic radius。

由 (4) 得
\[
\|E_i\|_{L^2_{\rm loc}}\to0.
\]
曲率统一有界给出 \(E_i\) 的 \(L^\infty\) 界，故插值产生每个有限 \(p\) 下
\[
\|E_i\|_{L^p_{\rm loc}}\to0.
\]
在 harmonic 坐标中
\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=-2(\Ric_{g_i})_{jk}+Q_{jk}(g_i^{-1},\partial g_i),
\]
椭圆稳定性遂给出
\[
\widehat g_i\to g_\infty
\quad\text{strongly in }W^{2,p}_{\rm loc}
\quad(p<\infty).
\]
这足以令曲率强 \(L^p\) 收敛并传递 Weyl 模长与谱缺陷；不需要先前错误的 \(W^{4,p}\) 推论。

极限弱满足
\[
\Ric_{g_\infty}=-g_\infty
\]
并经 harmonic-coordinate 椭圆正则性变光滑，同时
\[
|W_\infty^+|^2=\frac1{24},\qquad
\spec(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Einstein 条件给出 \(\delta W_\infty^+=0\)。Derdziński 定理使
\[
(24|W_\infty^+|^2)^{1/3}g_\infty
\]
局部 Kähler；该因子恒为 \(1\)，所以 \(g_\infty\) 本身局部 Kähler。但四维 Kähler–Einstein 度量满足
\[
|W^+|^2=\frac{s^2}{24}
=\frac{16}{24}=\frac23,
\]
与 \(1/24\) 矛盾。终端环节在使用正确密度 (4) 后没有隐藏缺口。

---

## 8. 族一致结论

若无统一 gap，可取
\[
\delta_i=\|g_i^{-1}(\Ric_{g_i}+g_i)\|_{\infty,\mathrm{op}}\to0.
\]
初始校准给出
\[
q_i/A_i\to0,\qquad
D_{{\rm av},i}/A_i\to0,\qquad
\Vol(g_i)/A_i\to32\pi^2/9.
\]

- 若 \(A_i\to\infty\)，上述统一支撑—流—终端链直接适用；
- 若 \(A_i\) 有界，取子列 \(A_i=A_0\)。因
  \[
  q_i\in\frac13\mathbb Z,\qquad q_i\ge0,\qquad q_i/A_i\to0,
  \]
  最终 \(q_i=0\)。平台体积仍为固定正数 \(cA_0\)，而终端密度为 \(o(A_0)\)，相同选择论证成立。

因此，经上述修订并核准曲率与 defect 变分模块后，确实推出 Ishida–LeBrun \(q\ge0\) 地理族上的统一负号间隙。仍应将证明状态精确表述为：

- **流的存在/重启：** 系数正则化给出至少一条精确退化流和存在性延拓；不声称唯一性；
- **任意阶延拓：** 使用当前 \((U_m,C_{m+1})\) 同指数联合能量；
- **终端输入：** 使用全局 \(Q\) 和包含 \(|E|^2\) 的密度 \(\Phi\)；
- **若 Step35 的 defect 指标引理尚未正式写成定理，族一致 gap 仍以该单一解析对象为条件。**

这只是受限的四维 \(\lambda<0\) Ishida–LeBrun 结论。
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 53,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step53_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step53_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical substance of A03 Step55's direct nonlinear construction of the normalized cutoff flow and its interface with the restricted Ishida--LeBrun negative-gap architecture. Read the supplied A03 note, structural check script/data, and the A01 consolidated IL proof/route notes. Focus on whether the transported-cutoff DeTurck system, epsilon-regularized parabolic-plus-transport construction, epsilon-uniform H^s and all-order hierarchy, epsilon->0 passage, and pullback identity plausibly give a genuine per-datum smooth solution of ∂_t g = -2 χ^2(Ric+g). Then identify precisely what remains before the restricted IL theorem is an end-to-end proof: first-exit quantities, support/terminal chain, sequence-uniform time, or hidden derivative/epsilon losses. Do not decide the session route; give a direct scientific verification memo with load-bearing errors, corrections, and implications for the Yau 26 research state.

## Integrated Scientific Memo

# 科学核验备忘录

## 结论

Step 55 找到了**正确的规范化未知量和正确的拉回机制**。其主导项配权显示：对每个固定光滑数据 \((g_0,\chi)\)，通过
\[
(G_\varepsilon,\beta_\varepsilon)\longrightarrow (G,\beta)
\longrightarrow g=\varphi^*G
\]
构造
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g)
\]
的短时光滑解，是高度可信且原则上可补成严格证明的；先前冻结系数迭代中的输运导数损失确实被联合非线性求解消除了。

但现稿还不是完整 PDE 定理证明，主要缺口是：

1. §5 的全阶估计所给导数分拆论证有明确错误，必须改用 tame Moser 估计；
2. 固定 \(\varepsilon\) 的抛物–输运耦合存在理论及全部交换子尚未严格写完；
3. 几何方程的“唯一性”没有由规范系统唯一性自动推出；
4. 更关键地，所得寿命取决于固定背景 \(H^s/C^s\) 范数，**不能推出 IL 塌缩序列上的统一时间**。Appendix 最后一句关于曲率–体积预算蕴含统一寿命的断言没有依据；
5. A01 的 first-exit、终端图表与全局 \(Q\) 链仍主要是陈述而非在所给材料中完成的推导；
6. 终端 Liouville 平均在塌缩下还存在指数映射重数问题，A01 的全局上界目前没有排除重数常数发散。

因此，Step 55 可视为可信的**逐数据精确 cutoff-flow 起动模块**，尚不能视为 restricted Ishida–LeBrun 定理的端到端完成。

---

## 1. DeTurck 系统与拉回恒等式

令
\[
W^k(G)=G^{ab}\bigl(\Gamma(G)^k_{ab}-\Gamma(\bar g)^k_{ab}\bigr).
\]
利用
\[
-2\operatorname{Ric}(G)+\mathcal L_WG
=G^{-1}D^2G+R(G,G)+Q(G,DG)
\]
以及
\[
\mathcal L_{fW}G
=f\mathcal L_WG+df\otimes W_G^\flat+W_G^\flat\otimes df,
\]
(1.4) 的度量方程确切等于
\[
\partial_tG
=-2\beta^2(\operatorname{Ric}(G)+G)
+\mathcal L_{\beta^2W(G)}G. \tag{1}
\]
额外的 \(d(\beta^2)\)-项不可省略；否则拉回后得不到固定 \(\chi\) 的几何方程。

取 Euler 速度
\[
X=-\beta^2W(G),\qquad
\partial_t\varphi=X\circ\varphi,\quad \varphi(0)=\mathrm{id}.
\]
输运方程给出
\[
\frac d{dt}\beta(t,\varphi(t,x))
=\partial_t\beta+D\beta\cdot X=0,
\]
故
\[
\beta(t,\varphi(t,x))=\chi(x). \tag{2}
\]
再由
\[
\partial_t(\varphi^*G)=\varphi^*(\partial_tG+\mathcal L_XG)
\]
和 (1)，Lie 项完全抵消：
\[
\partial_t(\varphi^*G)
=-2\chi^2\bigl(\operatorname{Ric}_{\varphi^*G}+\varphi^*G\bigr).
\]
符号、复合点和 Ricci 自然性均正确。由于 \(X=0\) 于 \(\{\beta=0\}\)，拉回也保持静止外部。

---

## 2. \(\varepsilon\)-正则化与无 \(\varepsilon^{-1}\) 机制

正则化主系数
\[
a_\varepsilon=\beta^2+\varepsilon
\]
对每个固定 \(\varepsilon>0\) 严格椭圆，但并非关于 \(\varepsilon\) 一致椭圆。因此不能调用带一致抛物常数的普通 Schauder 理论；必须依赖加权能量。

关键恒等式是
\[
\frac{|Da_\varepsilon|^2}{a_\varepsilon}
=\frac{4\beta^2|D\beta|^2}{\beta^2+\varepsilon}
\le 4|D\beta|^2. \tag{3}
\]
这消除了零集附近看似可能出现的 \(\varepsilon^{-1}\)。

### 度量主项

保留 \(G^{-1}\) 收缩后，最高阶耗散为
\[
-\int a_\varepsilon\,G^{-1}*D^{k+1}G*D^{k+1}G.
\]
系数导数项满足
\[
\left|\int Da_\varepsilon*D^{k+1}G*D^kG\right|
\le
\eta\int a_\varepsilon|D^{k+1}G|^2
+C_\eta\int |D\beta|^2|D^kG|^2,
\]
其中使用了 (3)，没有除以 \(\varepsilon\)。

### 输运耦合

最高阶项为
\[
\int D^k\beta\,
\beta^2D^kW(G)\,D\beta
\sim
\int \beta^2D^k\beta\,D^{k+1}G\,D\beta.
\]
由于
\[
\frac{\beta^4}{\beta^2+\varepsilon}\le \beta^2\le1,
\]
加权 Young 不等式给出
\[
\le \eta\int a_\varepsilon|D^{k+1}G|^2
+C_{\eta}\|D\beta\|_\infty^2\|D^k\beta\|_2^2.
\]

### Lie 交叉项

最高 \(\beta\)-导数项
\[
\int D^kG*\beta W*D^{k+1}\beta
\]
积分一次后产生
\[
-\int \beta W*D^{k+1}G*D^k\beta
\]
及低阶项；这里恰有一个 \(\beta\)，可由 \(a_\varepsilon\) 耗散吸收。若导数全部落在 \(W\) 上，\(d(\beta^2)=2\beta\,d\beta\) 同样提供所需权重。

因此，现有主导项计算确实支持
\[
E_s'+cD_s\le C_R(1+E_s)
\]
且常数无 \(\varepsilon^{-1}\)。这是 Step 55 最重要的解析贡献。

需要修正文稿中的三个细节：

- (1.6) 中 \(Q\) 的系数是 \(a_\varepsilon\)，§3 却写成 \(\beta^2Q\)。正确估计仍成立：
  \[
  \left|\int D^kG*a_\varepsilon A(G,DG)D^{k+1}G\right|
  \le \eta D_s+C_{\eta,R}E_s.
  \]
- “取 \(A\) 足够大以控制输运耦合”并不准确，因为乘大输运能量也同时乘大其交叉项。应固定 \(A>0\)，再选择相应小的 Young 参数。
- 含积分耗散的 (3.2) 需在 Grönwall 后另行积分并进一步缩短时间；仅点态 \(E_s\) 界并不直接给出所写精确右端。

还需要显式设置 stopping-time bootstrap，同时控制 \(G^{-1}\)、\(E_s\) 和度量正定性。

---

## 3. 差分估计、全阶层级与极限

### 差分估计

按
\[
A_1D^2G_1-A_2D^2G_2
=A_2D^2Z+(A_1-A_2)D^2G_1
\]
定向展开是正确选择。在 \(r=s-2\) 时，最坏的系数差项是
\[
\omega\,D^{r+2}G_1=\omega\,D^sG_1,
\]
从而
\[
\|\omega D^sG_1\|_2
\le C\|\omega\|_{H^r}\|G_1\|_{H^s},
\qquad r>n/2.
\]
不需要对差分作插值。Lie 项和输运速度采用 branch-oriented 分拆后，所有 \(D^{r+1}Z\) 都带有 \(\beta_2\) 或 \(\beta_2^2\)，可由
\[
(\beta_2^2+\varepsilon)|D^{r+1}Z|^2
\]
吸收。其主导结构可信，但严格证明仍须逐项核对所有 Moser 交换子。

### §5 的明确错误与修复

§5 声称当 \(j\le m-s\) 时，
\[
D^j[(\beta^2+\varepsilon)G^{-1}]
\]
可由 \(E_s\) 控制。这是错误的；例如 \(m=3s,j=2s\) 时显然不能由 \(H^s\) 控制 \(2s\) 阶导数。

应以标准 tame Moser 估计替代该分拆。隔离
\[
a_\varepsilon D^{m+2}G,
\qquad
\beta W\,D^{m+1}\beta
\]
两个最高结构后，其余项应证明满足
\[
C\!\left(\|(G,\beta)\|_{H^s},
\|G^{-1}\|_{L^\infty}\right)(1+E_m),
\]
或允许系数依赖已经建立的 \(E_{m-1}\)。例如
\[
\|D\beta\,D\beta\|_{H^{m-1}}
\le C\|D\beta\|_{L^\infty}\|\beta\|_{H^m}.
\]
所以全阶结论很可能可修，但现有 Proposition 5.1 的证明不成立。

### \(\varepsilon\to0\)

一旦修复后的全阶界在共同时间上成立，紧性步骤没有结构性障碍：

- 高阶空间界加方程给出的时间等度连续性产生逐阶紧嵌入；
- 对任意固定 \(k\)，取足够高的空间阶数即可得
  \[
  \varepsilon G_\varepsilon^{-1}D^2G_\varepsilon\to0
  \quad\text{于 }C^k;
  \]
- 差分唯一性可将子列收敛提升为规范变量的全序列收敛。

零集保持也正确。对固定 \(x\)，
\[
\partial_t\beta(t,x)
=\bigl(W(G)\cdot D\beta\bigr)(t,x)\,\beta(t,x)^2
\]
是关于 \(\beta(t,x)\) 的 ODE；初值为零则恒为零。此处 \(d(\beta^2)=2\beta\,d\beta=0\)，故 \(G\) 在零集点上静止。

---

## 4. 逐数据存在与唯一性的准确范围

现有论证在补齐 tame 估计和固定 \(\varepsilon\) 理论后，足以支持：

> 对每个闭流形上的固定光滑 \((g_0,\chi)\)，存在短时光滑几何解，并在 \(\{\chi=0\}\) 静止、跨 cutoff 界面光滑。

但 Theorem 9.1 的“唯一几何解”尚未证明。规范系统唯一性只比较已经满足同一 \((G,\beta)\) 系统的解。若要比较两个任意固定-\(\chi\) 几何解，必须把每个解通过逆 DeTurck 构造送入同一个 transported-cutoff 规范系统，并证明该构造在退化系数下有效。IL 应用只需存在性，所以此缺口不是其当前主要障碍。

固定 \(\varepsilon\) 的存在也不能仅以“Galerkin 标准”略过：投影可能破坏输运积分恒等式和度量正定性。需要引用适当的 quasilinear parabolic–transport 定理，或写出保持所需交换子结构的 Friedrichs 正则化。

---

## 5. 与 restricted Ishida–LeBrun 架构的接口

Step 55 成功提供了 A01 后续估计真正需要的精确对象：

- \(\{a=0\}\) 上度量严格静止；
- \(a=1\) 的平台上是标准规范化 Ricci 流；
- 支撑不交时
  \[
  \left(\sum_\alpha\chi_\alpha\right)^2
  =\sum_\alpha\chi_\alpha^2;
  \]
- 后续全局 \(Q\) 分拆和 stationary-collar 恒等式可直接在 \(\varepsilon=0\) 精确流上使用，而无须对正则化流作近似论证。

但这仅解决“存在一个正确的逐数据流”，没有解决以下端到端对象。

### 5.1 序列统一寿命仍未得到

Step 55 给出的时间本质上是
\[
T=T\bigl(\|g_0\|_{H^s(\bar g)},\|\chi\|_{C^s(\bar g)}\bigr).
\]
IL 序列允许塌缩，并只有 Ricci defect、\(L^2\) 曲率、体积及低阶 cutoff 控制。A01 §4.2 甚至明确说二阶以上 cutoff jet 只逐数据有限。因此既无统一固定背景 \(H^s\) 度量界，也无统一 \(C^s\) cutoff 界。

故 A03 Appendix 的断言
\[
T_i\ge T_0>0
\quad\text{“由统一 curvature-to-volume budgets 得出”}
\]
不成立。\(L^2\) 曲率和体积预算不能控制高阶固定坐标 Sobolev 范数。

可行的正确桥梁只能是几何 continuation/first-exit 定理：证明精确流在 \(0\le t\le\theta r^2\) 内所有导致延拓失败的量均由低阶、塌缩无关预算控制，即使高阶常数逐数据依赖。该定理目前未写出。

### 5.2 first-exit 链仍需完整推导

所给 A01 材料没有逐项证明以下负载项：

\[
(K_2^\eta)'\le C(1+r^{-2})K_2^\eta,
\qquad
\|a\,\mathrm{Rm}(t)\|_\infty\le C/t;
\]
\[
J_6'+cX_6\le C(1+r^{-2})J_6,
\qquad
\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3};
\]
\[
Q(T)\le e^{C(1+r^{-2})T}Q(0)
\]
且没有加性曲率误差；以及由 defect 速度得到的 metric drift、平台体积保持和全阶延拓。

最危险的 cutoff 项是
\[
\nabla^2a
=2\,d\chi\otimes d\chi+2\chi\nabla^2\chi. \tag{4}
\]
因为支撑构造没有统一控制 \(\nabla^2\chi\)，每个低阶 family-uniform 估计都必须明确把 \(\chi\nabla^2\chi\) 分部积分，直至只剩统一控制的一阶 cutoff 项。仅引用“signed Hessian contraction”不足以证明常数与序列无关。

### 5.3 终端 Liouville 平均的塌缩重数问题

A01 使用指数拉回球以绕过基流形塌缩，从而获得局部非塌缩并应用 forbidden-germ 下界。这一**下界方向**是合理的。但上界
\[
\int_{P_i^{\rm in}}A_\rho\Phi(p)\,d\mu(p)
\le C(K,\rho)\int_M\Phi\,d\mu \tag{5}
\]
尚未建立塌缩无关常数。

曲率界控制共轭半径，却不控制 injectivity radius。于是
\[
\exp_p:B_\rho(0)\subset T_pM\to M
\]
可能多对一；指数拉回平均会按短测地环路的重数重复计算基流形上的 \(\Phi\)。塌缩时该重数可能发散。“所有测地线留在平台”只保证 buffer，不保证指数映射单射或重数有界。

因此须补充下列之一：

- 对相关平台证明统一 injectivity/noncollapse；
- 证明指数映射在所取尺度上的重数有统一界；
- 或改写平均论证，使其通过 Liouville 测度/测地流得到不依赖点到点重数的全局估计。

仅取
\[
\rho<cK^{-1/2}
\]
可避开共轭点，但不能排除拓扑性短环路，因此不自动修复 (5)。

### 5.4 支撑半径需统一

A01 使用 \(B_{5r}\subset B_{6r}\subset B_{7r}\) 及 \(14r\)-分离，A03 Appendix 使用 \(B_{4r},B_{5r}\) 及 \(12r\)-分离。两种约定都可工作，但最终证明必须固定一套半径，同时确保：

- \(\chi_\alpha\) 支撑互不相交；
- \(\eta_\alpha\) 缓冲支撑互不相交；
- 终端指数球完全留在 \(a=1\) 平台中。

---

## 6. 脚本与 JSON 的证据权重

“22/22 checks passed”不能作为 PDE 验证。绝大多数检查条件被直接硬编码为 `True`；少数实际计算只是 \(r>s\) 型算术或 \(2p-n=0\)。脚本没有验证：

- 非线性交换子；
- 固定 \(\varepsilon\) 存在；
- \(\varepsilon\)-一致能量；
- 全阶 tame 层级；
- 紧性与极限。

并且脚本仍宣称一般的 “Q-type antisymmetric IBP identity”，而 Step 55 正文已经正确弃用它并改为加权 Young。对张量/矩阵系数 \(A\)，
\[
\int h*A*Dh
\]
不能一般化成标量形式的
\[
-\frac12\int |h|^2\,DA.
\]
脚本应删除该检查。其正确定位只是结构清单，而非证明或计算验证。

---

## 7. 对当前研究状态的影响

Step 55 的实质进展是：

- 修正 transported-versus-fixed cutoff 的规范不匹配；
- 给出正确的 \(\beta^2W\) 输运和 Lie 乘积项；
- 揭示退化耗散与输运速度之间恰当的 \(\beta\)-权重；
- 避开先前 contraction 路线中的导数损失；
- 为 A01 的精确支撑恒等式提供可信的逐数据光滑流。

它尚未完成 restricted IL 负间隙定理。最精确的剩余数学对象是：

1. 修复后的 tame 全阶 \(\varepsilon\)-一致 PDE 定理；
2. 由几何低阶预算而非固定背景 \(H^s\) 范数控制的 \(\theta r^2\) 延拓定理；
3. \(K_2^\eta,Y,J_6\)、全 \(p\) defect ladder、全局 \(Q\) 和 drift 的逐项 family-uniform first-exit 证明，尤其处理 (4)；
4. 终端平均中指数映射重数的塌缩无关控制。

即使这些全部完成，所得仍只是四维、\(\operatorname{Ric}\approx-g\)、Ishida–LeBrun 特定地理族的统一负间隙；正号分支、任意四维拓扑、\(n\ge5\)、维数唯一常数以及 Lean 4 完整形式化均未由该模块触及。
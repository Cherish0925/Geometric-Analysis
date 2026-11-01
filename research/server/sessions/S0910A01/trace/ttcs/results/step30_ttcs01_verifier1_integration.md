# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 30,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step30_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step30_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 30 repair of the four-dimensional negative Ishida--LeBrun selected-support route. Focus on four concrete issues, not the old dependency diagram: (1) whether the mixed Hölder--Sobolev estimate H_{3p/2} <= H_p^{1/2} ||z_p||_4^2 correctly repairs the half-power gap in the weighted Moser hierarchy with z_p=a^{(p-1)/2} f^{p/2}, including time cutoffs and polynomial p-losses; (2) whether ordinary unweighted Moser on U=a(Rm+G) is indeed unjustified as a first bound because the operator remains a Delta and the quadratic term becomes U*U, while U remains useful for continuation; (3) whether the Ishida--LeBrun family bookkeeping should use an O(A) Euler bound plus Vol/A lower bound rather than chi(M)=A+O(1) or K0->9, and whether sigma_i/A_i->0 (not exact sigma=0) is the full analytic regime; (4) whether the macro-disjoint support/plateau/eigenline zero-extension refinements are the right hypotheses for the terminal pullback chain. Please identify any remaining hidden mathematical gaps precisely.

## Integrated Scientific Memo

# Step 30 核验结论

四项修补在其所声称的层次上均成立，但它们只修复了路线的代数、迭代结构和族参数记账；尚未证明 Step 29 的 selected-support flow theorem。最核心的未决对象仍是统一的张量级全 \(p\) 能量不等式及与之兼容的 \(q=3\) 正时间势估计。

## 1. 混合 Hölder–Sobolev 桥确实修复半次幂缺口

令
\[
H_p=\int \eta^2a^{p-2}f^p,\qquad
z_p=\eta a^{(p-1)/2}f^{p/2},\qquad \kappa=\frac32.
\]
在下一层能量的支撑位于 \(\{\eta=1\}\) 时，
\[
(a^{p-2}f^p)^{1/2}z_p^2
=\eta^2a^{(p-2)/2+p-1}f^{3p/2}
=\eta^2a^{3p/2-2}f^{3p/2}.
\]
故 Cauchy–Schwarz 给出
\[
\boxed{H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2.}
\]
这正好消除了旧比较中的缺口。事实上
\[
z_p^3=\eta^3a^{3p/2-3/2}f^{3p/2}
      =\eta\,a^{1/2}\bigl(\eta^2a^{3p/2-2}f^{3p/2}\bigr),
\]
所以 \(0\le a\le1\) 仅给出
\[
\|z_p\|_3^3\le H_{3p/2},
\]
方向无法用于控制下一层能量。

由
\[
\nabla z_p
=(\nabla\eta)a^{(p-1)/2}f^{p/2}
+\eta\frac{p-1}{2}a^{(p-3)/2}f^{p/2}\nabla a
+\eta\frac p2a^{(p-1)/2}f^{(p-2)/2}\nabla f
\]
以及
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le Cr^{-2},
\]
得到
\[
\|\nabla z_p\|_2^2\le Cp^2(D_p+r^{-2}H_p),
\qquad
\|z_p\|_2^2\le H_p.
\]
这里必须满足下列二者之一：

* \(\eta\equiv1\) 于全部 \(\operatorname{supp}a\)，且 \(a=0\) 于 \(\operatorname{supp}\nabla\eta\)；或
* 明确采用嵌套空间截断，使第 \(p_{k+1}\) 层支撑位于第 \(p_k\) 层截断等于一的区域。

否则 Cauchy–Schwarz 第一因子不等于已有的 \(H_p\)。

局部 Sobolev 因而给出
\[
\|z_p\|_4^2\le Cp^NS(D_p+r^{-2}H_p).
\]
配合时间截断能量估计
\[
\sup_{[\tau_{k+1},t]}H_{p_k}
+\int_{\tau_{k+1}}^t(D_{p_k}+r^{-2}H_{p_k})
\le L_k\int_{\tau_k}^tH_{p_k},
\]
其中
\[
L_k=Cp_k^N4^k(t^{-1}+r^{-2})
\]
（\(t\le cr^2\)，且小的 \(\beta\) 已把 \(\beta^3/t\) 并入 \(t^{-1}\)），可得
\[
M_{k+1}\le Cp_k^NS(L_kM_k)^{3/2},
\qquad
M_k=\int_{\tau_k}^tH_{p_k},\quad p_{k+1}=\frac32p_k.
\]
于是
\[
M_{k+1}^{1/p_{k+1}}
\le (Cp_k^NS)^{1/p_{k+1}}L_k^{1/p_k}M_k^{1/p_k}.
\]
因为
\[
\sum_k\frac{\log p_k}{p_k}<\infty,\qquad
\sum_k\frac{k}{p_k}<\infty,
\]
任意固定有限阶的多项式 \(p\)-损失和 \(4^k\)-损失均无害；并且
\[
\sum_k\frac1{p_k}=\frac3{p_0},
\qquad
\sum_k\frac1{\kappa p_k}=\frac2{p_0}.
\]
因此形式终点为
\[
\|af(t)\|_\infty
\lesssim S^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^tH_{p_0}\right)^{1/p_0}.
\]
它分别产生
\[
p_0=3:\quad \|aF(t)\|_\infty\lesssim\beta/t,
\]
以及
\[
p_0=6:\quad
\|aE(t)\|_\infty
\lesssim \delta r^{2/3}t^{-1/3}
=\delta(r^2/t)^{1/3}.
\]

### 尚需补写的迭代细节

1. 从时空积分到固定终时的取极限不能只依赖收缩到单点的时间区间。应使用
   \[
   H_{p_k}(t)\le L_kM_k
   \]
   或等价的终时能量估计，然后令 \(p_k\to\infty\)。
2. \(p_k\) 一般为非整数，需对 \(a=0\) 处的实次幂链式法则作严格处理；可用 \(a+\varepsilon\) 正则化后取极限。
3. 加性 source 项若真实存在，必须证明它们可被吸收到 \(H_p\) 或形成可迭代的受控种子；脚本没有验证这一点。

因此混合估计本身成立，并修复了特定缺口，但终点仍以张量能量不等式为条件。

## 2. \(U=a(\operatorname{Rm}+G)\) 不能产生第一个点态界

设
\[
T=\operatorname{Rm}+G,\qquad U=aT.
\]
若
\[
(\partial_t-a\Delta)T
=a(T*T+G*T)+(\nabla a)*\nabla T+(\nabla^2a)*T,
\]
则乘以 \(a\) 后二次项为
\[
a^2T*T=(aT)*(aT)=U*U,
\]
不是 \(aU*U\)。重写扩散项会产生截断交换子，但主部仍为 \(a\Delta\)。测试 \(|U|^{p-2}U\) 只能得到
\[
\int a\,\bigl|\nabla |U|^{p/2}\bigr|^2,
\]
并不能得到普通 Sobolev–Moser 所需的无权梯度控制。故普通无权 Moser 不能从零开始构造 \(\|a\operatorname{Rm}\|_\infty\)。

同一批评也适用于 Step 29 中“ordinary Moser on \(|aE|\)”的残留表述：\(aE\) 的主算子同样退化。缺陷终点必须使用修复后的加权层级，而不是无权 Moser；虽然二者的形式指数恰好相同，但论证机制不同。

\(U\) 在得到首个加权曲率界之后仍然有正确且重要的用途：
\[
\operatorname{Ric}(U)=aE,\qquad
\partial_tg=-2\operatorname{Ric}(U),\qquad
\partial_t\Gamma\sim\nabla U.
\]
这些恒等式维持 Wang 型导数三角结构，可用于延拓和重启。

还需明确连接一个小点：\(\|aF(t)\|_\infty\lesssim t^{-1}\) 在 \(t=0\) 发散，而延拓定理写作 \(\sup_{[0,T)}|a\operatorname{Rm}|<\infty\)。应以初始光滑短时解控制 \([0,t_0]\)，以 Moser 界控制 \([t_0,T)\)，固定 \(t_0>0\) 后拼接；不能直接把 \(C/t\) 当作闭区间一致界。

此外，Step 29 中
\[
(\partial_t-a\Delta)U=\cdots+a(U*U+G*U)
\]
的二次项系数是旧误写；正确结构是 \(U*U+aG*U\)，另加截断交换子。

## 3. Ishida–LeBrun 族记账修补正确

在实际假设 \(m=2,3\)、\(X_j\) 为极小一般型复曲面、\(b_+(N)=0\) 下，
\[
c_2(X_j)\le5c_1^2(X_j)+36,
\]
而
\[
D=\frac A3+\sigma
\]
给出
\[
\chi(N)=\frac A3+\sigma+6-4m-6b_1(N)
\le\frac A3+\sigma+6-4m.
\]
所以
\[
\boxed{\chi(M)\le\frac{16}{3}A+\sigma+30m+6.}
\]
这在 \(\sigma/A\to0\) 时仅说明 \(\chi(M)=O(A)\)，并不说明
\(\chi(M)=A+O(1)\)。相应地，所给资料不能推出 \(K_0\to9\)。

近负 Einstein 夹逼下，两侧体积估计的用途不同且都不可省略：

* \(\operatorname{Vol}/A\ge v_->0\) 用于把保留的固定体积分数转化为
  \[
  \operatorname{Vol}(P)\ge \alpha A;
  \]
* \(\operatorname{Vol}/A\le v_+<\infty\) 用于
  \[
  \sigma/A\le C\delta^2
  \]
  及均值曲率能量控制。

在所给公式中，可由标量 monopole 界与 \(|s|\le4(1+\delta)\) 得到典型下界
\[
\frac{\operatorname{Vol}}A\ge \frac{2\pi^2}{(1+\delta)^2},
\]
而 Chern–Weil 和
\[
|s|\ge4(1-\delta),\qquad |\operatorname{Ric}^\circ|^2\le4\delta^2
\]
给出小 \(\delta\) 时的典型上界
\[
(1-2\delta-2\delta^2)\operatorname{Vol}\le4\pi^2A.
\]
结合 Euler 上界与 CGB，足以推出
\[
K_0=\operatorname{Vol}^{-1}\int|\operatorname{Rm}|^2\le C.
\]
路线只需该一致有界性。

参数区域也修正正确。由
\[
\sigma\le R
=\frac1{8\pi^2}\int|\operatorname{Ric}^\circ|^2
\le\frac{\delta^2}{2\pi^2}\operatorname{Vol}
\]
以及体积上界，
\[
\boxed{\sigma/A\le C\delta^2.}
\]
故任意 \(\delta_i\to0\) 的候选序列都满足
\[
\sigma_i/A_i\to0,
\]
即使每个 \(\sigma_i>0\)。仅处理精确 \(\sigma=0\) 不能覆盖完整分析区域。

这里的负载输入 \(R\ge\sigma\)、标量 monopole 界及其规范常数仍应从原始 Ishida–LeBrun/Seiberg–Witten 公式独立核准；Step 30 只正确使用了它们，并未重新证明。

## 4. 终端 pullback 所需的支撑几何修补方向正确

所需的精确空间结构应是
\[
P_j\Subset\{a_j=1\}
\Subset\text{有界曲率 plateau}_j
\Subset\text{静止外缓冲区}_j,
\]
并要求不同 \(j\) 的外缓冲区两两不交。

宏观相互作用图按例如 \(d(x_i,x_j)\le12r\) 连边，保留一个颜色类后可使 \(B_{6r}\) 缓冲两两不交。这比仅使小支撑不交更强，且是全局缺陷能量精确求和的必要条件。

但“最大体积颜色类”必须严格定义为对分配给中心的 Voronoi 单元或其他不交权重求和，而不是按中心数选择；塌缩情形中不同球体积可相差很大。需要证明
\[
\operatorname{Vol}(P)\ge\theta\operatorname{Vol}(M)
\ge\theta v_-A.
\]

终端指数映射还需要定量余量。若
\[
P_j\subset B_r(x_j),\qquad B_{4r}(x_j)\subset\{a_j=1\},
\qquad e^{-\zeta}g_0\le g(T)\le e^\zeta g_0,
\]
则可取 \(\rho\) 满足
\[
r+e^{\zeta/2}\rho<4r,
\]
以保证从 \(P_j\) 出发、长度不超过 \(\rho\) 的终端测地线完全留在 plateau 内；同时要求
\[
K\rho^2<\pi^2/4
\]
以应用 Rauch/Jacobian 控制。

对于仅在有界曲率缓冲区上证明估计的非负 eigenline/harmonic-form 密度，先在外部置零再应用全局 pullback 平均是正确的：它保持非负性，并且选中的指数球完全位于真实定义区域内。该扩张只需可测，不需光滑。

需更正术语：
\[
\mathscr A=W^++\sqrt{2/3}|W^+|I
\]
通常是半正定移位 Weyl 自同态，不是一般意义下的“projector”；终端只使用其核等于最低 Weyl 特征线这一性质。

终端密度结论应直接按
\[
A_\rho\mathfrak D(p)\le C\,Q/A
\]
表述，而不是以未归一化的 \(Q\) 作为族极限参数。正权 monopole 正则化参数也应在
\(\varepsilon=Q\) 与 \(\varepsilon=Q/\operatorname{Vol}\) 之间统一：由于 \(Q=o(A)\) 未必蕴含 \(Q\to0\)，族上一致的小参数应取均值尺度 \(Q/\operatorname{Vol}\)，但必须重新核验所有平滑误差仍为 \(O(Q)\)。

## 精确的剩余缺口

1. **全 \(p\) 张量能量不等式。**  
   需对 \(F\) 和正则化 \(|E|\) 逐指标证明
   \[
   H_p'+cp^{-m}D_p
   \le Cp^N(r^{-2}+S^2Y)H_p
   \]
   具有固定有限 \(m,N\)，涵盖移动范数、移动体积、Lichnerowicz 反应、所有 \(\nabla^2a\) 分部积分、实指数和 Kato 极限。这是当前最关键的未决对象。

2. **同一支撑上的 \(q=3\) 正时间势。**  
   尚需完整证明
   \[
   S^2Y(t)\le C\beta^3/t
   \]
   并确保其截断、演化 Sobolev 常数和高 \(p\) 层级完全一致。

3. **\(J_6\) 与全局 \(Q\) 传播。**  
   必须完整处理过渡区项；不能从 \(C/t\) 曲率系数自 \(t=0\) 直接 Gronwall。特别需要得到
   \[
   Q(T)/A\to0.
   \]

4. **退化流的存在与延拓。**  
   Wang 分组分部积分的移植目前仍有结构性省略；严格短时存在也依赖退化系数的抛物正则化极限，尚未在这些材料中展开。

5. **加权宏观支撑选择定理。**  
   有界度着色、Voronoi 体积权重、固定 \(A\)-比例 plateau 质量、终端测地线包含关系尚未组合成完整证明。

6. **终端 gauge 密度。**  
   harmonic amplitude、\(\int\langle\mathscr AH,H\rangle\) 的一致常数、均值尺度正则化以及 \(H_i\) 的局部椭圆紧性仍需核验。

综上，Step 30 的四项修补均成立，并正确撤回了无权 \(U\)／\(aE\) 首界捷径；但它建立的是一致的条件性路线，不是已完成的 selected-support theorem。
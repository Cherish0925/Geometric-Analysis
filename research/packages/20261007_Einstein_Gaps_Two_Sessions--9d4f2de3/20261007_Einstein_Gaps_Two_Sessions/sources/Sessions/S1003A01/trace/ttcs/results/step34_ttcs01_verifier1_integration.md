# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 34,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step34_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step34_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the proposed corrected separated-depletion theorem and the ramification-cap realization logic. Context: We study the two-parameter ramified Kähler--Einstein surgery law for Einstein-defect gaps on four-manifolds. Step 33 left a partial anti-self-dual retention argument; the current strategist note proposes that if U contains the surgery regions and N is a disjoint topology-preserving modification region with exact KE boundary matching, then retaining the global scalar variance term gives a clean lower bound: for t=theta_0 in [0,1/3], the numerator of equation (4.1) is bounded below by -16 B_U^0 - 48 t B_N^0, hence E >= 4t/(1+t)-o(h) when Delta/A -> 0 and B_U^0=o(Q), even if Delta/Q grows. Peer Step38 adds the local identity on a ramification neighbourhood with matching boundary: Delta_N B = P_N/4 - Delta_N S/48, or in scalar -4 normalization Delta_N B=P_N/4-Delta_N V/3, so flux alone has no sign. Please read the context and give a mathematical verification memo: identify exact assumptions needed, check the algebra and scale estimates, distinguish what this closes from unrestricted competitors, and assess the bridge from the exact Calabi cap model to actual ramified towers (Biquard--Guenancia only gives C0/quasi-isometric model comparison in the negative setting near D unless further elliptic/local chart work is supplied).

## Integrated Scientific Memo

# 核验备忘录：修正后的 separated-depletion 定理与 ramification-cap 实现

## 1. 结论概览

修正后的分离耗散命题在明确的切割与边界匹配假设下成立。令
\[
t=\theta_0=h(1-6\theta)\in[0,1/3],
\]
并令 \(\mathcal N(g)\) 为 (4.1) 的分子，则
\[
\boxed{\mathcal N(g)\ge -16B_U^0-48tB_N^0.}
\]
实际上可保留额外的非负项，得到更强估计。若
\[
B_U^0=o(Q),\qquad \Delta/A\to0,
\]
则
\[
\boxed{\mathcal E(g)\ge \frac{4t}{1+t}-o(h),\qquad h=Q/A,}
\]
且不要求 \(\Delta/Q\) 有界；允许 \(\Delta/Q\to\infty\)。

该结果只排除了“与手术区域分离、拓扑不变、且与 KE 背景精确匹配”的 \(W^-\) 耗散改变一阶系数。它不是对所有竞争度量的估计，因而尚不能直接改善 \(\alpha(M)\) 的全度量下界。仍未处理的是手术与 ramification cap 重叠、弥散型全局变形以及无 KE 接口的近极值序列。

Step 38 的局部恒等式正确：
\[
\boxed{\Delta_NB=\frac14P_N-\frac1{48}\Delta_NS.}
\]
若两侧均满足 \(s=-4\)，则
\[
\boxed{\Delta_NB=\frac14P_N-\frac13\Delta_NV.}
\]
故相对 Euler/signature flux 本身没有保留性的符号；其价值在分离论证中是精确地把标量平方通道与 \(P_N\)、\(B_N\) 联系起来。

---

## 2. 基本代数

记
\[
P=\int|\Ric^\circ|^2,\qquad
S=\int s^2,\qquad
L_s=\int(s-\bar s)^2,\qquad
R=P+\frac14S .
\]
直接对 Einstein 常数最小化得
\[
\mathcal E=\frac{4P+L_s}{R}.
\]
因此
\[
(1+t)R\left(\mathcal E-\frac{4t}{1+t}\right)
=4P-tS+(1+t)L_s.
\tag{2.1}
\]
结合 Step 33 的恒等式
\[
P=\frac{S-S_0}{12}+4(B-B_\Delta)+8\pi^2At,
\]
其中
\[
S_0=32\pi^2A,\qquad B_\Delta=\frac{8\pi^2}{3}\Delta,
\]
且 \(8\pi^2At=tS_0/4\)，可得
\[
\boxed{
\mathcal N(g)
=\frac{1-3t}{3}(S-S_0)+16(B-B_\Delta)+(1+t)L_s,
}
\tag{2.2}
\]
即 (4.1) 的分子。

一个小修正：在未手术底流形 \(\bar X\) 上，\(t=0\) 时
\[
S-S_0=12P-48(B-B_\Delta)
\]
是 Chern–Weil 恒等式，而不是依赖 KE 极小性的额外不等式；Step 33 中出现的 \(-3L_s\) 对本论证并不需要。

---

## 3. 分离定理所需的精确假设

设 \(g_0=g_{\rm KE}\) 是 \(\bar X\) 上满足 \(\Ric(g_0)=-g_0\) 的背景。

需要：

1. **区域与拓扑。**  
   \(U\) 包含全部 blow-up、handle 等拓扑手术区域；它对应底流形中的旧区域 \(U^0\)。区域 \(N\) 与 \(U\) 不交，且 \(N\) 内不发生拓扑改变，可与 \(\bar X\) 中的 \(N^0\) 识别。

2. **背景外部。**  
   除 \(U\cup N\) 外，\(g=g_0\)。

3. **精确 KE 接口。**  
   在 \(\partial U,\partial N\) 的开放环带上，\(g\) 与 \(g_0\) 完全一致。于是可以光滑定义：
   - \(g_1\)：在 \(U\) 保留 \(g\)，其余恢复为 \(g_0\)，作为 \(M\) 上的度量；
   - \(g'\)：在 \(N\) 保留 \(g\)，其余取 \(g_0\)，作为 \(\bar X\) 上的度量。

   该假设也保证曲率积分严格可加，且相对 Euler/signature 公式无额外 Chern–Simons 边界项。

4. **全度量标量预算。**  
   对 \(M\) 上每个光滑度量，尤其对 \(g\) 与 \(g_1\)，有
   \[
   S\ge32\pi^2p\ge S_0.
   \tag{3.1}
   \]
   这是实际 monopole 输入 \(p\ge A\) 的使用点。

5. **参数范围。**
   \[
   0\le t\le\frac13.
   \tag{3.2}
   \]
   等价地，当前目标只在 \(\theta\le1/6\) 的非平凡范围内。

无需假设 \(s\) 点态接近 \(-4\)，也无需比较 \(L_s(g)\)、\(L_s(g_1)\)、\(L_s(g')\)。

---

## 4. 局部相对恒等式

令
\[
\Delta_NS=S_N(g)-S_N(g_0),\qquad
\Delta_NB=B_N(g)-B_N(g_0),
\]
并记
\[
P_N=\int_N|\Ric^\circ_g|^2.
\]

因为 \(g\) 与 \(g_0\) 在边界环带上相同，相对 signature 公式给出
\[
\Delta_N\int|W^+|^2=\Delta_N\int|W^-|^2=\Delta_NB.
\]
相对 Gauss–Bonnet 公式给出
\[
0=2\Delta_NB-\frac12P_N+\frac1{24}\Delta_NS.
\]
故
\[
\boxed{\Delta_NB=\frac14P_N-\frac1{48}\Delta_NS.}
\tag{4.1}
\]
等价地，
\[
\Delta_NS=12P_N-48\Delta_NB.
\tag{4.2}
\]
由 \(B_N(g)\ge0\)，
\[
\Delta_NB\ge-B_N^0,
\]
所以
\[
\boxed{\Delta_NS\le12P_N+48B_N^0.}
\tag{4.3}
\]

若 \(s_g=s_{g_0}=-4\)，则 \(\Delta_NS=16\Delta_NV\)，于是
\[
\Delta_NB=\frac14P_N-\frac13\Delta_NV.
\]
这表明 flux 没有独立符号；耗散恰对应于相对体积增长超过 \(3P_N/4\)。

---

## 5. 分离估计的证明

令
\[
\Delta_US=S(g_1)-S_0.
\]
由标量预算，
\[
\Delta_US\ge0.
\tag{5.1}
\]

由于背景只在 \(U,N\) 内被替换，
\[
B-B_\Delta
=\bigl(B_U(g)-B_U^0\bigr)+\Delta_NB
\ge -B_U^0+\Delta_NB.
\]
将其代入 (2.2)：
\[
\begin{aligned}
\mathcal N(g)
&\ge -16B_U^0
+\frac{1-3t}{3}\Delta_US
+\frac{1-3t}{3}\Delta_NS
+16\Delta_NB
+(1+t)L_s(g).
\end{aligned}
\]
由 (4.1)，
\[
\frac{1-3t}{3}\Delta_NS+16\Delta_NB
=4P_N-t\Delta_NS.
\]
故
\[
\mathcal N(g)\ge
-16B_U^0
+\frac{1-3t}{3}\Delta_US
+4P_N-t\Delta_NS
+(1+t)L_s(g).
\]
使用 (4.3)：
\[
4P_N-t\Delta_NS
\ge (4-12t)P_N-48tB_N^0.
\]
因此得到强化式
\[
\boxed{
\begin{aligned}
\mathcal N(g)\ge{}&
-16B_U^0-48tB_N^0\\
&+\frac{1-3t}{3}\Delta_US
+4(1-3t)P_N
+(1+t)L_s(g).
\end{aligned}}
\tag{5.2}
\]
在 \(0\le t\le1/3\) 下，后三项均非负，故
\[
\boxed{\mathcal N(g)\ge-16B_U^0-48tB_N^0.}
\tag{5.3}
\]

这正是所提修正结论。其关键是保留全局 \(L_s(g)\ge0\)，并把 monopole 标量预算应用于恢复 \(N\) 后的 \(g_1\)，从而完全绕开 Step 33 未闭合的 scalar-variance 比较。

---

## 6. 尺度核验

由标量预算，
\[
R=P+\frac14S\ge\frac14S_0=8\pi^2A.
\]
从 (2.1)、(5.3) 得
\[
\mathcal E(g)\ge
\frac{4t}{1+t}
-\frac{16B_U^0+48tB_N^0}{(1+t)8\pi^2A}.
\tag{6.1}
\]
而
\[
B_N^0\le B_\Delta=\frac{8\pi^2}{3}\Delta,
\]
故第二个误差满足
\[
\frac{48tB_N^0}{8\pi^2A}
\le16\,\frac{t\Delta}{A}.
\]
因为
\[
0\le t=h(1-6\theta)\le h=\frac QA,
\]
有
\[
\frac{t\Delta}{A}
\le h\,\frac{\Delta}{A}=o(h)
\qquad\text{若 }\Delta/A\to0.
\]
同时
\[
\frac{B_U^0}{A}=o(Q/A)=o(h)
\qquad\text{若 }B_U^0=o(Q).
\]
因此
\[
\boxed{\mathcal E(g)\ge\frac{4t}{1+t}-o(h).}
\tag{6.2}
\]
又
\[
\frac{4t}{1+t}
=4h(1-6\theta)+O(h^2).
\]

注意
\[
\frac{t\Delta}{Q}\le\frac{\Delta}{A}\to0,
\]
所以完全不需要 \(\Delta=O(Q)\)；即使 \(\Delta/Q\to\infty\)，结论仍成立。

在 CH-close 手术位置，\(W^-_{\rm CH}=0\)。若每个固定大小的旧手术区域上
\[
\|g_0-g_{\rm CH}\|_{C^2}\le\varepsilon_m\to0,
\]
则每个区域的旧 \(W^-\)-能量为 \(O(\varepsilon_m^2)\)，故
\[
B_U^0=O(Q\varepsilon_m^2)=o(Q).
\]
缩小 handle 区域则需单独保证其被移除的背景 Weyl 能量总和为 \(o(Q)\)。

---

## 7. 该结果闭合了什么，未闭合什么

### 已闭合

它排除了如下机制在 \(h\) 的首阶上改善系数：

- 手术局限于 \(U\)；
- 在与 \(U\) 分离的 \(N\) 中任意改变度量，甚至大量耗散背景 \(W^-\)；
- \(N\) 不改变拓扑；
- 修改在 KE 环带上精确闭合。

即使 \(N\) 包含全部 ramification 区域并且 \(B_N^0\asymp B_\Delta\)，其代价也只以 \(tB_N^0\) 进入；由于 \(t=O(Q/A)\) 与 \(\Delta/A\to0\)，这是 \(o(Q)\)。因此“与手术分离的 ramification depletion”不能改变首阶 tariff。

### 尚未闭合

该类不是 \(\alpha(M)\) 的全部竞争度量。尤其未处理：

1. 手术区域与 ramification cap 重叠；
2. cell 直接置于 \(W^-_{g_0}=O(1)\) 的非局部对称区域；
3. 度量在全流形弥散变化，不能切割出 KE 接口；
4. 近极值度量只局部接近某个 Einstein 几何，而非指定 \(g_0\)；
5. 仅有近似匹配、但尚未控制总 Chern–Simons 和曲率插值误差的情形。

所以该定理是结构性必要条件，而不是新的 unrestricted all-metric gap theorem。若某族满足
\[
\mathcal E/h<4(1-6\theta)-c,
\]
则它必须破坏上述分离结构；最自然的剩余机制正是手术与 cap 的局部相互作用。

对近似环带，可以通过插值恢复上述构造，但必须定量控制：

- Euler/signature transgression；
- 插值层的 \(P,S,L_s\)；
- 所有接口的总误差。

需要的总分子误差是 \(o(Q)\)。仅有未定量的点态接近不足以推出这一点。

---

## 8. 精确 Calabi cap 模型的核验

模型为
\[
g=\tau(dx^2+dy^2)+\frac{d\tau^2}{\Theta}+\Theta\eta^2,
\qquad
\Theta=\frac23\tau^2-\frac c\tau,
\qquad d\eta=dx\wedge dy.
\]
令
\[
\tau_0=\left(\frac{3c}{2}\right)^{1/3}.
\]
则
\[
\Theta(\tau_0)=0,\qquad \Theta'(\tau_0)=2\tau_0.
\]
取角变量周期 \(2\pi/\tau_0\)，闭合端光滑。若坐标环面面积为 \(a\)，则
\[
e=\frac{a\tau_0}{2\pi},\qquad
\Area(D')=a\tau_0=2\pi e.
\]

给定精确曲率公式
\[
s=-4,\qquad |W^+|^2=\frac23,\qquad
|W^-|^2=\frac{6c^2}{\tau^6},
\]
以及
\[
d\mu=\tau\,dx\,dy\,d\tau\,d\psi,
\]
可直接计算
\[
\begin{aligned}
\int_{\tau_0}^{\infty}|W^-|^2\,d\mu
&=
6c^2a\frac{2\pi}{\tau_0}
\int_{\tau_0}^{\infty}\tau^{-5}\,d\tau\\
&=\frac{8\pi^2}{3}e.
\end{aligned}
\]
在零截面上
\[
|W^-|^2
=\frac{6c^2}{\tau_0^6}
=\frac83.
\]
所以模型常数完全一致。

但“全部能量位于单位邻域”不能按字面理解。尾部比例为
\[
\frac{\int_{L\tau_0}^{\infty}|W^-|^2}
{\int_{\tau_0}^{\infty}|W^-|^2}
=L^{-4}.
\]
正确说法是：能量在 cap 中指数集中；任意指定比例 \(1-\varepsilon\) 可由某个固定宽度邻域捕获。

---

## 9. 从模型到真实 ramified tower：已证明与尚缺部分

### 已由来源支持

1. Biquard–Guenancia §4.3：当
   \[
   \beta_{m,\lambda}=v_{m,\lambda}^{-1},
   \]
   conic KE 度量拉回 ramified compactification 后成为光滑 KE 度量。

2. 在远离 divisor 的固定紧集上，有
   \[
   C^\infty_{\rm loc}
   \]
   收敛到 complex-hyperbolic 度量。这足以实现 CH-close surgery sites 和
   \[
   B_U^0=o(Q).
   \]

3. 对任何紧致 KE 背景，全局恒等式
   \[
   \int|W^-|^2=\frac{8\pi^2}{3}\Delta
   \]
   是精确的，不需要局部模型。

4. 对 ramification curves，
   \[
   \sum_c e_c=\Delta
   \]
   与全局 Chern 数一致。

5. Džambić 的指数及边界自交公式支持惯性素数幂塔中的
   \[
   A_n\asymp p^{8n},\qquad
   \Delta_n\asymp p^{6n},
   \qquad \Delta_n/A_n\to0.
   \]

因此，分离耗散定理本身不依赖真实 cap 的曲率级模型逼近：它只用
\[
B_N^0\le B_\Delta.
\]

### BG 当前结果不足以直接推出

BG 在 divisor 附近证明的是趋于 \(1\) 的准等距比较：
\[
(1-\varepsilon_\beta)\omega_{\rm model}
\le\widehat\omega_\beta
\le(1+\varepsilon_\beta)\omega_{\rm model},
\]
以及 Theorem 4.5 的 \(C^0\)/quasi-isometric 渐近。这不能直接推出：

- 真实度量在 \(D'\) 上 \(|W^-|^2\to8/3\)；
- 固定 cap 带捕获
  \[
  \frac{8\pi^2}{3}e_c+o(e_c)
  \]
  的能量；
- 真实度量在固定物理半径上与模型 \(C^2\)-接近；
- 模型 cell 成本自动转移到真实 cap。

曲率依赖二阶导数，\(C^0\) 双线性比较并不控制曲率。

### 所需的桥梁

至少需要在 ramified 局部坐标或局部通用覆盖上建立
\[
\boxed{
\|\widehat g_m-g_{{\rm cap},m}\|_{C^{2,\alpha}(K)}
\to0
}
\]
对固定 cap 子域 \(K\) 成立，并且常数对 ramification 阶数和所有 divisor 分量统一。若涉及高阶光滑拼接，则需相应 \(C^{k,\alpha}\) 控制。

自然路线是：

1. 在 \(v\)-重 branched cover 上解除 cone；
2. 使用 BG 的 \(C^0\) 势控制和双边度量比较取得统一椭圆性；
3. 在切向塌缩方向使用局部通用覆盖或统一 quasi-coordinate；
4. 对两度量满足的 KE/Monge–Ampère 方程应用 Evans–Krylov 与 Schauder；
5. 用 \(\|F\|_{C^0}\to0\) 与统一高阶界插值得到实际 \(C^2\) 收敛。

这里必须真正验证：

- 多参数 \(\beta_\lambda\to0\) 时的统一常数；
- branched pullback 后坐标和方程的统一性；
- 靠近 \(D'\) 的局部图半径；
- 误差在所有分量求和后的积分尺度。

对 cap 内能量定位，固定宽度 cap 上的 \(C^2\) 收敛加上精确全局总量已经足够：先令 cap 宽度足够大以捕获模型能量的 \(1-\rho(R)\)，再令度量误差趋零，可通过对角过程得到 cap 外能量 \(o(\Delta)\)。不应依赖整个 cusp 区域上的无速率点态接近，因为其体积可能为 \(A\gg\Delta\)。

---

## 10. “\(\asymp\Delta\) 个可用 cap sites”仍需额外几何

由
\[
\sum_c\Area(D'_c)=2\pi\Delta
\]
只能得到总面积尺度，不能自动得到 \(\asymp\Delta\) 个能容纳现有认证 cell 的互不相交四维球。认证 cell 的外半径约为
\[
7.6451
\]
并带缓冲，因此还需：

- ramification tori 的切向 systole 下界；
- 所需半径内法向 cap 的嵌入控制；
- 不同 cap/cusp 之间的统一分离；
- cusp stabilizer 与切向格点在算术覆盖中的增长估计。

Džambić 的 Chern 数公式不提供这些局部嵌入半径。

此外，当前认证 cell 具有**精确 CH collar**。若研究与 ramification cap 相互作用，则还需：

- 构造具有精确 Calabi-cap collar 的新 cell；或
- 定量控制 CH collar 与 cap collar 之间的过渡成本。

不能直接把现有 \(J_1<8\pi^2\) 的 CH-collar 证书解释为 cap-interacting cell 的证书。

---

## 11. 最终判定

1. **修正后的 separated-depletion 定理成立**，其严格形式为 (5.2)，从而
   \[
   \mathcal N(g)\ge-16B_U^0-48tB_N^0.
   \]

2. **尺度论证正确**：
   \[
   B_U^0=o(Q),\quad \Delta/A\to0
   \quad\Longrightarrow\quad
   \mathcal E(g)\ge\frac{4t}{1+t}-o(h),
   \]
   即使 \(\Delta/Q\to\infty\)。

3. **Step 38 局部恒等式正确且必要**，但它本身无保留符号；分离定理之所以闭合，是因为全局 scalar budget 施用于 \(g_1\)，而 \(N\) 通道只以额外因子 \(t\) 进入。

4. **该结果只闭合分离竞争类，不闭合 unrestricted \(\alpha(M)\)**。真正剩余的一阶 \(r\)-依赖机制是手术与 ramification cap 的局部相互作用，或无法形成 KE 接口的非局域退化。

5. **精确 Calabi 模型的常数与积分自洽**，但将其曲率分布和 cell 成本转移到真实 ramified towers，仍缺统一的 ramified \(C^{2,\alpha}\) 乃至更高阶局部比较、积分误差控制和足够大的嵌入半径。BG 现有的 \(C^0\)/准等距比较不能单独完成这一步。
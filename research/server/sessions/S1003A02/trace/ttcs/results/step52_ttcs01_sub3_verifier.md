# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step52_residual_norm_selection_absorption.md",
    "Sessions/S1003A02/workspace/notes/step51_residual_entry_link_charges_and_kahler_recovery.md",
    "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_verifier1_integration.md",
    "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_verifier2_integration.md",
    "Knowledge/objects/papers/The-long-time-behavior-of-fourth-order-curvature-flows--5b1863f1c7b9--f1cab1a2d745/object.md"
  ]
}
```

## Task

Verify Sections 1-2 of the Step-52 note on minimizing sequences of P(g)=∫|Ric°|² on closed four-manifolds. Check rigorously: (a) Proposition 52.1 — the harmonic-coordinate bootstrap from L^6 curvature, Sobolev and an L² residual of the gradient Q to W^{4,2} bounds, strong L^q convergence of curvature, and passage to an exact smooth P-critical limit (is the triangular structure Q = -ΔRic + a∇²s + b(Δs)g + Rm*Ric, tr Q = c0 Δs correct; are the Sobolev exponents in dimension four right, especially W^{2,6}⊂C^{1,1/3}, W^{2,2}⊂W^{1,4}, W^{4,2}⊂⊂W^{3,p}, p<4); (b) Proposition 52.2 — the logarithmic-cloud computation and whether it really shows that an own-scale L² residual cannot control pointwise curvature for the P-gradient (can the scalar profile be realized geometrically with small full residual?); (c) Proposition 52.4 — the contradiction proof via the L^6 curvature radius: point-picking, which integral-curvature harmonic-radius theorem is needed and whether it is true with a Sobolev bound, completeness and Euclidean volume growth of the limit, s≡0 by Yau, and the use of Tian–Viaclovsky small-energy regularity for scalar-flat Bach-flat complete metrics with a Sobolev bound; (d) Theorem 52.3 — whether (PS_ε) with the energy radius plus a uniform Sobolev bound really suffices for the orbifold/ALE structure without derivative hypotheses, and whether the remark r_ε ≥ cρ is right; (e) Section 2 — horizontality and length bound, the two warnings, the frozen-weight time-stepping construction and Theorem 52.5's deduction from Lemma 52.KS (is the deduction correct; is Lemma 52.KS a plausible true statement for this non-Willmore functional whose Weyl part is not dissipated; identify the exact obstacle or a counter-mechanism). Return a corrected statement of every item that is wrong or overstated, and distinguish proved, plausible-but-unwritten, and false.

## Output

# 科学核验备忘录：Step 52 §§1–2

## 总结

| 项目 | 状态 | 核心结论 |
|---|---|---|
| Proposition 52.1 | 在明确的调和坐标假设下成立 | 三角椭圆结构与 Sobolev 指数正确；最高阶项只弱收敛，不是强收敛；常数还依赖调和坐标常数 |
| Proposition 52.2 | 标量计算正确；原文到几何结论少了一步 | 可在平坦四环面上用共形扰动补成真正的度量序列，满足 \(\|Q\|_2\to0\) 而一点曲率不趋零 |
| Proposition 52.4 | 反证框架正确，但依赖两个需精确陈述的局部定理 | 调和半径输入应使用 \(p=6\)，不是文中的 \(p=3\)；Sobolev 只直接给出欧氏型体积下界；Tian–Viaclovsky 局部估计需按其准确假设调用 |
| Theorem 52.3 | 有充分数学依据，但短证尚未覆盖全部泡树技术 | \((\mathrm{PS}_\varepsilon)+(S)\) 确实可替代导数假设；轨形延拓、ALE 端及拼合仍依赖标准精确临界度量理论 |
| §2.1 | 梯度、正交性、能量律与长度估计正确 | 体积重标只是不改变 \(P\)，并非在路径长度中零代价 |
| Lemma 52.KS | 按现有表述不成立 | 同一阈值能量半径的上比较会被抛物平滑立即破坏；还存在冻结权重的高阶平滑问题 |
| Theorem 52.5 | 作为条件推导正确 | 实际只需在选取时刻有 \(r_\varepsilon(g(t))^4\le Cw_n\)；原 KS 中恰是这一关系不稳定 |

---

## 1. Proposition 52.1：四阶椭圆紧性

### 1.1 \(Q\) 的三角结构正确

四维恒等式
\[
P(g)=2\int |W|^2+\frac1{12}\int s^2-16\pi^2\chi(M)
\]
给出，在一组常用拉普拉斯号约定下，
\[
Q=-4B+\frac1{12}\left(
2\nabla^2s-2(\Delta s)g-2s\,\Ric+\frac12s^2g
\right).
\]
Bach 张量的主部为
\[
B_{ij}
=-\frac12\Delta\Ric_{ij}
+\frac16\nabla_i\nabla_js
+\frac1{12}(\Delta s)g_{ij}
+\mathcal R_{ij}(\Rm,\Ric).
\]
因此
\[
Q
=
2\Delta\Ric-\frac12\nabla^2s-\frac12(\Delta s)g
+\Rm*\Ric+\Ric*\Ric,
\]
其中符号和整体常数随约定改变，但主部系数均为固定非零常数。取迹得到
\[
\boxed{\operatorname{tr}Q=c_0\Delta s,\qquad c_0\ne0.}
\]
在上述约定中 \(c_0=-\tfrac12\)。

这里点态迹恒等式来自显式变分公式；尺度不变性只解释
\[
\int\operatorname{tr}Q=0,
\]
本身不足以推出点态公式。

### 1.2 调和坐标中的 bootstrap

应把假设写得更精确：在稍大的球上存在调和坐标，使
\[
\theta^{-1}\delta\le g_i\le\theta\delta,\qquad
\|g_i\|_{C^{1,\beta}}\le H,
\]
并有
\[
\|\Rm_i\|_{L^6}\le\Lambda,\qquad
\|Q(g_i)\|_{L^2}\le K.
\]
则内球上的估计常数依赖
\[
\theta,\ H,\ \Lambda,\ K,\ \operatorname{dist}(\text{内球},\text{球缘}),
\]
不能只写成 \(C(\Lambda)\)。

具体推导如下。

1. 调和坐标方程
   \[
   g^{kl}\partial_k\partial_lg_{ij}
   =-2\Ric_{ij}+B_{ij}(g,\partial g)
   \]
   与 \(\Ric\in L^6\) 给出
   \[
   g\in W^{2,6}.
   \]
   四维 Morrey 嵌入确为
   \[
   W^{2,6}\hookrightarrow C^{1,1/3}.
   \]

2. 迹方程给出
   \[
   \Delta_gs=c_0^{-1}\operatorname{tr}Q\in L^2.
   \]
   因 \(s\in L^6\)，内点椭圆估计给出
   \[
   s\in W^{2,2}.
   \]

3. 将 \(Q\)-方程解作 \(\Delta\Ric\)：
   \[
   \Delta\Ric
   =a\nabla^2s+b(\Delta s)g+\Rm*\Ric+\Ric*\Ric+Q.
   \]
   右端属于 \(L^2\)：曲率二次项属于 \(L^3\subset L^2\)；坐标展开中的
   \[
   \partial\Gamma*\Ric\in L^3,
   \qquad
   \Gamma*\partial\Ric
   \]
   是具有有界系数的一阶项。故
   \[
   \Ric\in W^{2,2}.
   \]
   四维端点嵌入
   \[
   W^{2,2}\hookrightarrow W^{1,4}
   \]
   是连续嵌入，原文指数正确。

4. 对调和坐标方程微分一次，\(\partial\Ric\in L^4\)，而
   \[
   \partial g*\partial^2g\in L^6,
   \]
   从而
   \[
   g\in W^{3,4}.
   \]

5. 再微分一次：
   \[
   \partial^2B
   =
   \partial g*\partial^3g+\partial^2g*\partial^2g.
   \]
   第一项至少属于 \(L^4\)，第二项属于 \(L^2\)，并且
   \(\partial^2\Ric\in L^2\)，故
   \[
   g\in W^{4,2}.
   \]

所有步骤都应在逐次缩小的同心球上完成。

### 1.3 紧嵌入和曲率强收敛

四维 Rellich 嵌入为
\[
W^{4,2}\Subset W^{3,p},\qquad p<4.
\]
由选择 \(p\) 任意接近 \(4\)，还得到
\[
g_i\to g_\infty\quad\text{强于 }W^{2,q}_{\rm loc}
\quad\text{对每个 }q<\infty.
\]
曲率由二阶导数和一阶导数二次项组成，因此
\[
\Rm(g_i)\to\Rm(g_\infty)
\quad\text{强于 }L^q_{\rm loc},\qquad q<\infty.
\]

原文关于 \(Q\) 中“所有项强收敛”的表述需要修正：线性的四阶项只在 \(L^2\) 中弱收敛。正确传递方式是：

- \(g_i\to g_\infty\) 强于 \(C^{1,\beta'}\)；
- \(\partial^4g_i\rightharpoonup\partial^4g_\infty\) 于 \(L^2\)；
- 四阶项的系数强收敛；
- 所有低阶乘积强收敛；
- \(Q(g_i)\to0\) 于 \(L^2\)。

于是
\[
Q(g_\infty)=0
\]
在分布意义成立。

### 1.4 光滑性

由迹方程
\[
\Delta_{g_\infty}s_{g_\infty}=0.
\]
结合 \(g_\infty\in W^{2,6}\subset C^{1,1/3}\) 和 Ricci 方程，可以先提高 \(s\) 的正则性，再提高 \(\Ric\) 与调和坐标中的 \(g\)。等价地，可调用 \(B^t\)-flat 弱解的调和规范正则性，因为这里对应的参数非零。最终 \(g_\infty\) 光滑。

因此 Proposition 52.1 的主体成立，修正版应显式保留调和坐标常数，并将最高阶收敛写成弱收敛。

---

## 2. Proposition 52.2：临界对数云

### 2.1 标量计算正确

令
\[
h_\sigma(r)=\frac1{r^2\log(1/r)},
\qquad \sigma<r<\sigma^{1/2}.
\]
在四维，
\[
\|h_\sigma\|_2^2
=
2\pi^2\int_\sigma^{\sigma^{1/2}}
\frac{dr}{r\log^2(1/r)}
=
\frac{2\pi^2}{\log(1/\sigma)}.
\]
若
\[
\Gamma(x)=\frac1{4\pi^2|x|^2},
\qquad u_\sigma=\Gamma*h_\sigma,
\]
则
\[
u_\sigma(0)
=
\frac1{4\pi^2}\,2\pi^2
\int_\sigma^{\sigma^{1/2}}
\frac{dr}{r\log(1/r)}
=
\frac{\log2}{2}.
\]
平滑截断端点不会改变此极限。与此同时，
\[
u_\sigma\to0\quad\text{于每个有限 }L^q_{\rm loc}.
\]

这准确表现了四维
\[
W^{2,2}\not\hookrightarrow L^\infty.
\]

### 2.2 仅靠迹方程还不足以推出几何结论

原文从
\[
\Delta s=\operatorname{tr}Q
\]
直接写到“标量曲率可携带这种云”，逻辑上少了度量兼容性与 \(Q\) 的无迹部分。完整 \(Q\)-方程还包含
\[
\Delta\Ric,\qquad \nabla^2s,
\]
所以标量 Poisson 模型本身并未构造度量。

不过这个缺口可以补齐。

### 2.3 平坦四环面上的共形实现

取平坦四环面 \((T^4,g_0)\)，把 \(h_\sigma\) 平滑后放在一个固定坐标球中，并减去平均值：
\[
f_\sigma=h_\sigma-\fint_{T^4}h_\sigma.
\]
解
\[
-\Delta_{g_0}u_\sigma=f_\sigma,\qquad \int u_\sigma=0.
\]
则
\[
\|u_\sigma\|_{W^{2,2}}
\le C\|f_\sigma\|_2\to0,
\]
但 Green 核的局部奇异部分仍给出
\[
u_\sigma(0)\longrightarrow\frac{\log2}{2}.
\]

再解
\[
\Delta_{g_0}\phi_\sigma=-\frac16u_\sigma,
\qquad \int\phi_\sigma=0.
\]
于是
\[
\|\phi_\sigma\|_{W^{4,2}}
\le C\|u_\sigma\|_{W^{2,2}}\to0.
\]
定义
\[
g_\sigma=e^{2\phi_\sigma}g_0.
\]
四维共形标量曲率公式给出
\[
s_{g_\sigma}
=e^{-2\phi_\sigma}
\left(u_\sigma-6|\nabla\phi_\sigma|^2\right),
\]
故
\[
s_{g_\sigma}(0)\to\frac{\log2}{2}.
\]
特别地，\(|\Rm_{g_\sigma}(0)|\) 不趋于零。

另一方面，四维嵌入
\[
W^{4,2}\hookrightarrow W^{2,q},\qquad q<\infty,
\]
给出
\[
\|\Rm_{g_\sigma}\|_{L^q}\to0
\quad\text{对每个有限 }q.
\]
而 \(Q\) 是从 \(W^{4,2}\) 度量到 \(L^2\) 的连续四阶非线性算子；在平坦度量附近，
\[
\|Q(g_\sigma)\|_2
\le C\|\phi_\sigma\|_{W^{4,2}}
+C\|\phi_\sigma\|_{W^{4,2}}^2
\to0.
\]

对任意固定 \(\varepsilon>0\)，最终还有
\[
\int_{T^4}|\Rm_{g_\sigma}|^2<\varepsilon,
\]
所以带截断 \(r_0=1\) 的能量半径处处等于 \(1\)。因此
\[
\int r_\varepsilon^4|Q(g_\sigma)|^2\to0,
\]
而一点曲率仍不趋零。

这给出了 Proposition 52.2 所需的真正几何实现。结论确实成立，但原注中的标量模型本身尚未包含这一步。

---

## 3. Proposition 52.4：\(L^6\) 小能量正则性

### 3.1 点选与缩放

若结论不成立，归一化 \(r=1\) 后可选 \(L^6\)-曲率半径
\[
r^{(6)}(x)
=
\sup\left\{\rho:
\rho^8\int_{B(x,\rho)}|\Rm|^6\le1
\right\}.
\]
由通常的“距球缘权重”点选，可得 \(y_i\) 与
\[
\lambda_i=r_i^{(6)}(y_i)\to0,
\]
并使重标后
\[
r_{\widetilde g_i}^{(6)}\ge\frac12
\]
在越来越大的球上成立。若 \(\lambda_i\) 未碰到截断值，则可取
\[
\int_{B_{\widetilde g_i}(y_i,1)}|\Rm_{\widetilde g_i}|^6=1.
\]
若半径定义中出现轻微连续性问题，改用 \(1-o(1)\) 的归一化即可。

残差缩放正确：
\[
\int|Q(\lambda_i^{-2}g_i)|^2\,d\mu_{\lambda_i^{-2}g_i}
=
\lambda_i^4\int|Q(g_i)|^2\,d\mu_{g_i}
\le\lambda_i^4\eta_0\to0.
\]
事实上，这里只需要原尺度残差有统一上界；“\(\eta_0\) 很小”并未用于吹起极限成为精确临界度量。

### 3.2 所需调和半径定理

所需局部输入应写为：

> 若四维球上有统一局部 Sobolev 不等式，并且
> \[
> \rho^{12-4}\int_{B(z,\rho)}|\Rm|^6\le\Lambda
> \]
> 在固定比例子球上成立，则内球的 \(W^{2,6}\) 调和半径有统一下界。

在点选后的度量中，
\[
r^{(6)}(z)\ge\frac12
\]
直接给出
\[
\int_{B(z,1/2)}|\Rm|^6\le 2^8.
\]
所以这里应使用
\[
\boxed{p=6>4/2,}
\]
而不是原文括号中的 \(p=3\)。若想改用 \(p=3\)，还需先取得体积上界；这在该阶段并未直接给出。

该调和半径结论可由标准反证得到：若调和半径趋零，在调和半径尺度再缩放，则 \(p>2\) 使缩放后的 \(L^p\) 曲率趋零；Sobolev 常数排除塌缩；所得平坦非塌缩极限与调和半径归一化矛盾。Step 52 仍应给出准确来源或把这段证明完整写入。

### 3.3 极限的完整性和体积性质

点选球的可用半径趋于无穷，配合统一调和半径，得到完整 pointed 极限。极限上的全局 Sobolev 不等式给出
\[
\operatorname{Vol}B(y,R)\ge cR^4.
\]
这是欧氏型体积下界。此时尚不能仅凭 Sobolev 不等式写成双边的“Euclidean volume growth”。

全局 Sobolev 不等式也排除紧致极限，因此极限非紧。

### 3.4 \(s\equiv0\)

极限满足 \(Q=0\)，故
\[
\Delta s=0.
\]
又因
\[
|s|\le C|\Rm|,\qquad \int_N|\Rm|^2\le\varepsilon_0,
\]
有 \(s\in L^2(N)\)。取标准截断函数 \(\eta_R\)，
\[
\int\eta_R^2|\nabla s|^2
\le
C R^{-2}\int_{B(2R)\setminus B(R)}s^2\to0.
\]
所以 \(s\) 为常数；极限体积无限且 \(s\in L^2\)，从而
\[
s\equiv0.
\]
无需额外 Ricci 符号假设。

由 \(Q=0\) 与 \(s=0\)，极限 Bach-flat。

### 3.5 Tian–Viaclovsky 估计的正确用法

需要的局部结论是：对标量平坦 Bach-flat 四维度量，若球上有统一 Sobolev 常数且
\[
\int_{B(y,R)}|\Rm|^2\le\varepsilon_{\rm TV},
\]
则
\[
\sup_{B(y,R/2)}|\Rm|
\le
CR^{-2}
\left(\int_{B(y,R)}|\Rm|^2\right)^{1/2}.
\]
选
\[
\varepsilon_0\le\varepsilon_{\rm TV}
\]
后，该估计可对所有 \(R\) 使用，得到
\[
\sup_{B(y,R/2)}|\Rm|\le C\varepsilon_0^{1/2}R^{-2}\to0.
\]
极限平坦，与归一化的 \(L^6\) 曲率矛盾。

因此 Proposition 52.4 的反证机制是正确的。当前文本尚需把调和半径定理和 Tian–Viaclovsky 局部定理的准确假设写清楚，尤其是前者的指数应改成 \(6\)。

---

## 4. Theorem 52.3：能量半径上的 Palais–Smale 结构

### 4.1 从 \((\mathrm{PS}_\varepsilon)\) 到局部残差

设
\[
r_i=r_{\varepsilon,i}(x).
\]
能量半径的 1-Lipschitz 性给出，在
\[
B(x,r_i/2)
\]
上
\[
r_{\varepsilon,i}(y)\ge r_i/2.
\]
因此
\[
r_i^4
\int_{B(x,r_i/2)}|Q(g_i)|^2
\le
16\int_{B(x,r_i/2)}
r_{\varepsilon,i}(y)^4|Q(g_i)|^2
\to0.
\]
重标到 \(r_i=1\) 后，局部 \(L^2\) 残差趋零。

同时，由能量半径定义，
\[
\int_{B(x,r_i)}|\Rm|^2\le\varepsilon.
\]
Proposition 52.4 给出固定比例内球上的尺度化 \(L^6\) 曲率界，再由调和半径定理得到
\[
r_h(x)\ge c\,r_{\varepsilon,i}(x).
\]
这确实删除了 Step 51 的显式导数假设。

### 4.2 泡树结论所需的精确输入

要得到完整轨形–ALE 结构，\((S)\) 必须具体到足以提供：

1. 所有相关子球上的尺度不变 Sobolev 不等式；
2. 局部体积下界；
3. 重标后 Sobolev 不等式传递到极限。

若文中的 \((S)\) 只表示一个未规范化的“局部 Sobolev 常数”，则还应把体积下界单列出来。

在上述形式下，有限总曲率使浓缩点个数有限；在其余区域，
\[
r_\varepsilon\ge c>0,
\]
于是 Proposition 52.1 给出
\[
C^{1,\beta'}\cap W^{2,q}_{\rm loc}
\]
强收敛以及 \(W^{4,2}_{\rm loc}\) 弱收敛。极限正则部分满足 \(Q=0\)。

在浓缩尺度重复同一论证，所有泡极限均为精确 \(P\)-临界度量；有限总曲率和全局 Sobolev 不等式给出 \(s\equiv0\)，故泡为标量平坦 Bach-flat。

还需调用精确临界度量的两项标准结果：

- 孤立奇点的轨形可移性；
- 完整有限曲率标量平坦 Bach-flat 极限的 ALE 结构。

Step 52 的两段短证没有重写这两项的全部技术内容，所以 Theorem 52.3 应表述为依赖这些精确临界度量定理。能量方面仍只有
\[
\alpha(M)\ge P(g_\infty)+\sum_bP(N_b);
\]
颈区能量消失未由 §§1–2 得到。

### 4.3 \(r_\varepsilon\ge c\rho\) 正确

若曲率半径 \(\rho(x)\) 满足
\[
|\Rm|\le\rho^{-2}
\quad\text{于 }B(x,\rho),
\]
则
\[
\Ric\ge-C\rho^{-2}g.
\]
局部 Bishop 比较给出
\[
\operatorname{Vol}B(x,c\rho)\le C(c\rho)^4.
\]
因此
\[
\int_{B(x,c\rho)}|\Rm|^2
\le
\rho^{-4}\operatorname{Vol}B(x,c\rho)
\le Cc^4.
\]
取 \(c=c(\varepsilon)\) 足够小，
\[
r_\varepsilon(x)\ge c\,\rho(x).
\]
所以
\[
\int r_\varepsilon^4|Q|^2\to0
\]
确实强于相应的曲率半径加权条件。

---

## 5. §2.1：加权几何与长度

对固定正函数 \(w\)，
\[
\langle h,k\rangle_{w,g}
=
\int w^{-1}\langle h,k\rangle\,d\mu
\]
的梯度是 \(wQ\)，因为
\[
DP_g(h)=\int\langle Q,h\rangle
=\langle wQ,h\rangle_{w,g}.
\]
对任意向量场 \(X\)，
\[
\langle wQ,\mathcal L_Xg\rangle_w
=
\int\langle Q,\mathcal L_Xg\rangle
=0.
\]
因此正交性正确。

沿
\[
\partial_tg=-wQ
\]
有
\[
\frac d{dt}P(g(t))
=-\int w|Q|^2,
\]
且路径速度为
\[
\|\partial_tg\|_w
=
\left(\int w|Q|^2\right)^{1/2}.
\]
若 \(P(g_0)-\alpha\le\delta\)，则
\[
L_w
\le
\sqrt{T}
\left(\int_0^T\int w|Q|^2\right)^{1/2}
\le\sqrt{T\delta}.
\]

体积方面，
\[
\frac d{dt}\operatorname{Vol}(g(t))
=
-\frac12\int w\,\operatorname{tr}Q,
\]
一般不为零。加入时间依赖的常数缩放项 \(\lambda(t)g\) 不改变 \(P\)，因为
\[
DP_g(g)=\int\operatorname{tr}Q=0.
\]
所以“at no cost”只应解释为不增加 \(P\)；该缩放项在加权路径长度中并非零长度。

---

## 6. 两个 warning 的准确形式

### 6.1 点态曲率权重

\[
w=(|\Rm|^2+V^{-1})^{-1}
\]
本身是光滑函数，并非真的发生不连续跳跃。问题是：

- 在 \(|\Rm|=0\) 的点，它取全局尺度 \(V\)，即使任意近处已有曲率集中；
- 它不编码邻域积分浓缩；
- 其高阶导数无法从曲率零阶信息控制。

所以“不适合建立统一 own-scale 抛物估计”是准确表述；“unusable”过强。

### 6.2 冻结长度不能控制新生高频结构

取局部度量扰动
\[
h_\nu(x)=a\,h(\nu x),
\]
支集直径约为 \(\nu^{-1}\)。则
\[
\|h_\nu\|_{L^2}^2\asymp a^2\nu^{-4},
\qquad
\int|\partial^2h_\nu|^2\asymp a^2.
\]
因此它可携带固定量级的 \(L^2\) 曲率能量，却在冻结的宏观权重下具有趋零的路径长度。这一观察正确，也正说明长度估计不能单独控制能量半径。

---

## 7. 冻结权重构造中的额外分析问题

从一个 1-Lipschitz 能量半径 \(r_\varepsilon\) 构造
\[
c\,r_\varepsilon^4\le w\le C\,r_\varepsilon^4
\]
的光滑函数并不困难；困难在于同时取得统一的 own-scale 高阶估计
\[
|\nabla^kw|\le C_k r_\varepsilon^{4-k}.
\]
任意固定光滑度量上可作数据依赖的平滑，但仅凭能量半径和 Sobolev 常数，尚不能自动得到统一 \(C_k\)。尤其 Proposition 52.2 的对数云表明：能量半径可为宏观尺度，而点上曲率及其导数仍很大。

因此 §2.2 中“positive times 时该平滑可得”还需要相应的正时间 own-scale 正则性；它不是单纯由“度量已经光滑”推出的。

---

## 8. Lemma 52.KS：同阈值上比较不成立

最严重的问题是
\[
r_\varepsilon(g(t))
\le2r_\varepsilon(g(t_n))
\]
这一上比较。

考虑尺度 \(\ell\) 的局部曲率包，其总曲率能量为
\[
\varepsilon(1+\delta),
\qquad 0<\delta\ll1,
\]
而其余区域近乎平坦。初始能量半径约为 \(\ell\)。冻结权重在该包附近满足
\[
w\asymp\ell^4.
\]
线性化的四阶耗散模在这种加权时间中以 \(O(1)\) 速率衰减；其能量近似为
\[
E(t)\simeq E(0)e^{-ct}.
\]
当
\[
t\asymp\delta
\]
时，局部总能量便降到 \(\varepsilon\) 以下。若外部没有其他曲率，能量半径立即从 \(O(\ell)\) 增至截断尺度 \(1\)。令 \(\delta\to0\)，这一增大可发生在任意短的正时间内，同时初始 Sobolev 常数保持接近平坦值。

这是固定阈值定义
\[
r_\varepsilon(x)
=\sup\{r:\int_{B(x,r)}|\Rm|^2\le\varepsilon\}
\]
固有的阈值穿越现象。抛物平滑正会触发它。因此不存在只依赖 Sobolev 常数的统一时间 \(c_1>0\)，使所有初值都满足同一 \(\varepsilon\) 下的上述上比较。

采用两个分开的阈值
\[
0<\varepsilon_-<\varepsilon_+
\]
后，“短时间内不产生新的浓缩”这一方向仍有合理形式，例如比较
\[
r_{\varepsilon_+}(g(t))
\quad\text{与}\quad
r_{\varepsilon_-}(g(0)).
\]
但这种一侧估计允许能量半径增大，不能提供 Theorem 52.5 所需的
\[
r_\varepsilon(g(t))^4\le Cw_n.
\]

### 8.1 其余分析障碍

即使删去上比较，统一 own-scale 存在时间仍需新的局部能量估计：

- \(P\) 的全局耗散是
  \[
  -\int w|Q|^2,
  \]
  但局部 \(\int\varphi|\Rm|^2\) 的演化包含环带通量和 \(w\) 的高阶导数；
- Pfaffian 的局部变化产生 \(\partial_tg\) 与 \(\nabla\partial_tg\) 的通量，仅有 \(\int w|Q|^2\) 尚不能直接控制后者；
- Weyl 能量没有独立的符号良好局部耗散式；
- \(\delta W\sim\nabla\Ric\) 只是一阶 Bianchi 关系，仍需与四阶抛物估计、截断函数和权重导数结合；
- Einstein 度量满足 \(Q=0\) 却可有非零 Weyl 曲率，说明不能从 \(P\)-速度单独获得局部 Weyl 强制衰减。

所给 Streets 文献不提供该结论：Theorem 1.3 预先假设整段流上有曲率上界；Remark 1.14 明确指出局部化平滑估计困难；Remark 1.12 把曲率尺度上的非塌缩列为未解问题。变权流还多出权重导数这一层。

因此，一个带分离阈值、只给出“新浓缩不会迅速形成”的 Kuwert–Schätzle 型引理是有数学依据的研究对象；Lemma 52.KS 当前的双向同阈值比较则不成立。

---

## 9. Theorem 52.5 的条件推导

设每一步确实存在长度至少 \(c_1\) 的流，并且在选取时刻满足
\[
r_\varepsilon(g(t))^4\le Cw_n.
\]
令
\[
D_n
=
\int_{t_n}^{t_{n+1}}\int w_n|Q|^2.
\]
能量律给出
\[
\sum_nD_n
\le P(g_0)-\alpha
=\delta,
\]
所以 \(D_n\to0\)。每一步有某个 \(\tau_n\) 满足
\[
\int w_n|Q(g(\tau_n))|^2
\le\frac{D_n}{c_1}.
\]
于是
\[
\int r_\varepsilon(g(\tau_n))^4|Q(g(\tau_n))|^2
\le
C\frac{D_n}{c_1}\to0.
\]
这段推导完全正确。

值得强调的是，它只使用当前能量半径相对冻结权重的上控制；下控制并非此处必需。恰恰这一上控制会被抛物耗散造成的能量半径增大破坏。因此 Theorem 52.5 是一个正确的抽象条件定理，但现有 Lemma 52.KS 不能为它提供所需输入。

## 最终科学判断

Sections 1 的核心修正是局部而明确的：Proposition 52.1 成立；Proposition 52.2 可用四环面共形构造补成真正几何例子；Proposition 52.4 的反证机制成立，但必须改正调和半径指数并明确两个局部正则性定理；Theorem 52.3 在这些输入和标准精确临界泡树理论下成立。

Section 2 的代数部分成立，但分析闭合尚未完成。更具体地，缺少的不只是 Weyl 局部能量估计：同一阈值能量半径的时间上比较本身与抛物平滑不相容，而这一比较正是把冻结权重残差转成输出度量自身能量半径残差的关键关系。
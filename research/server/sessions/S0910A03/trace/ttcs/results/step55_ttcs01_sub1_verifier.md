# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step55_direct_nonlinear_flow_construction.md",
    "Sessions/S0910A03/workspace/notes/step54_exact_synchronized_output_ledger.md",
    "Sessions/S0910A03/workspace/notes/step54_route_reassessment_and_joint_weighted_iteration.md"
  ]
}
```

## Task

Verify the direct nonlinear construction for the normalized cutoff flow ∂_tg = -2χ²(Ric+g) presented in the attached note. The construction uses ε-regularization of the coupled DeTurck metric equation + transported cutoff β, standard quasilinear parabolic theory for ε>0, ε-uniform joint H^s energy estimates, and compactness for ε→0.

Focus on these load-bearing mathematical claims:

1. JOINT H^s ENERGY (Proposition 3.1): The cross-coupling between metric and transport equations closes. Specifically, the transport top term β²·D^sW(G)·Dβ (which involves D^{s+1}G) when tested against D^sβ gives ∫β|D^sβ|·β|D^{s+1}G|·|Dβ|, claimed to be absorbed by the metric dissipation (β²+ε)|D^{s+1}G|². Check: does Cauchy-Schwarz work here? Is the β² factor correct or do we need β²+ε?

2. DIFFERENCE ESTIMATE (Proposition 4.1): At r=s-2, the coefficient difference (β₁²-β₂²)G₁⁻¹D²G₁ is bounded in H^r by C_R‖ω‖_{H^r} using the individual H^s ball. Check: at the top level, the product ω·D^sG₁ needs ‖ω‖_∞·‖D^sG₁‖_2; does Sobolev embedding H^r ↪ L^∞ hold for r>n/2? Is the Q-type antisymmetric identity ∫h·a·Dh = -½∫|h|²·Da correctly applied to the actual DeTurck Q-tensor?

3. PULLBACK IDENTITY (Proposition 7.1): The claim is β₀(t,φ(t,x))=χ(x) from f'(t)=0. Then the Lie derivative cancellation β₀²=χ_E² on the image of φ. Check: is the Eulerian velocity formula correct? Does the pullback of the scalar-weighted tensor -2β²(Ric+G) correctly give -2χ²(Ric(g)+g)?

4. ε→0 PASSAGE: ε·G_ε⁻¹D²G_ε → 0 as ε→0. The all-order ε-uniform hierarchy gives C^∞ compactness. Check: is the uniqueness argument for ε=0 valid? The Grönwall holds without the dissipation term, but the equation is degenerate; does the H^r framework still apply to non-uniformly-parabolic equations?

5. ZERO-SET REGULARITY: The solution is claimed smooth across ∂{χ>0} because it's a C^∞ limit of smooth functions. Check: is this sufficient? Could the limit develop singularities at the zero-set boundary despite C^k convergence?

## Output

# 科学验证备忘录

## 总结

五个关键点的核验结果如下：

1. **联合 \(H^s\) 能量中的 transport–metric 顶阶耦合可以闭合**；\(\beta^2\) 恰好提供所需权重，不需要把它替换成 \(\beta^2+\varepsilon\)。
2. **主系数差在 \(r=s-2\) 阶的乘积估计成立**。但当前 \(Q\)-项所用的积分恒等式并不自动适用于张量系统；可用带权 Young 不等式替代。更重要的是，Lie 差项在 Step 55 中有一处无权顶阶导数的错误处理，必须采用 Step 54 §6.1 的分支定向分解。
3. **pullback 的最终公式正确，但文中的微分同胚 ODE 和 Eulerian 速度写错了复合位置**。按标准 DeTurck ODE 修正后，抵消完全成立。
4. **\(\varepsilon\to0\) 的方程极限成立**。退化系统的光滑解唯一性不要求一致椭圆性，但依赖修正后的差分能量。任意阶一致估计目前只有纲要，尚未形成完整推导。
5. **真正的 \(C^\infty\) 收敛足以排除零集界面产生奇异性**；仅仅“每个近似解都光滑”则不够。

因此，直接非线性构造具有可成立的核心结构，但当前文本仍含两个明确公式错误、一处差分能量错误，以及任意阶一致估计和共同存在时间 bootstrap 的证明缺口。

---

## 1. 联合 \(H^s\) 能量

令 \(h=D^s\beta\)。由于
\[
D^sW(G)=A(G)D^{s+1}G+\text{低阶项},
\]
transport 方程的关键项具有形式
\[
I_s=\int_M
\left\langle h,\,
\beta^2 A(G)D^{s+1}G\cdot D\beta
\right\rangle .
\]
在 \(G,G^{-1}\) 和 \(D\beta\) 有一致 \(L^\infty\) 控制时，
\[
\begin{aligned}
|I_s|
&\le C_R
\left(\int(\beta^2+\varepsilon)|D^{s+1}G|^2\right)^{1/2}
\left(\int\frac{\beta^4}{\beta^2+\varepsilon}|h|^2\right)^{1/2}\\
&\le
\eta\int(\beta^2+\varepsilon)|D^{s+1}G|^2
+C_{\eta,R}\|h\|_2^2,
\end{aligned}
\]
因为
\[
\frac{\beta^4}{\beta^2+\varepsilon}\le \beta^2.
\]
所以这里的 **\(\beta^2\) 因子正好足够**。若顶阶项只有不带 \(\beta\) 的 \(D^{s+1}G\)，则会产生 \(\varepsilon^{-1}\)；实际 transport 结构没有这一问题。

Lie 交叉项中
\[
\int D^sG\cdot \beta W(G)D^{s+1}\beta
\]
经一次分部积分成为
\[
-\int \beta D^{s+1}G\cdot W(G)D^s\beta+\text{低阶项},
\]
同样由上述带权估计吸收。另一类
\[
\int D^sG\cdot \beta D\beta\,D^{s+1}G
\]
也由
\[
\eta\int(\beta^2+\varepsilon)|D^{s+1}G|^2
+C_{\eta,R}\|D^sG\|_2^2
\]
处理。

### \(Q\)-项的张量问题

文中的
\[
\int h\cdot a\,Dh=-\frac12\int |h|^2Da
\]
对标量 \(h\)，或对张量指标上自伴的矩阵系数 \(a\)，才直接成立。一般 DeTurck \(Q\)-张量的线性化顶阶项写成
\[
\int \langle h,\beta^2 A^a D_a h\rangle
\]
时，尚未证明 \(A^a\) 在张量指标上自伴。

不过这不妨碍能量闭合，因为可以直接写
\[
\left|\int \langle h,\beta^2 A^aD_ah\rangle\right|
\le
\eta\int(\beta^2+\varepsilon)|Dh|^2
+C_{\eta,R}\|h\|_2^2.
\]
因此 Proposition 3.1 的这一部分可成立，但理由应改为带权 Young 估计，而不是未经验证的张量版恒等式。

另有两个书写层面的缺口：

- 由 (3.11) 得到的是对 \(1+\mathcal E_s\) 的控制；文中的 \(2\mathcal E_s(0)\) 与随后得到的 \(2\mathcal E_s(0)+1\) 不一致，可通过把能量改成 \(1+\mathcal E_s\) 修正。
- 共同时间还需要一个 bootstrap：用一致的
  \[
  \|\partial_tG_\varepsilon\|_{H^{s-2}}\le C
  \]
  保证 \(G_\varepsilon\) 在 \(C^0\) 中接近 \(g_0\)，从而保持一致正定并延拓到同一 \(T_0\)。

---

## 2. \(H^{s-2}\) 差分估计

令 \(r=s-2\)。由于 \(r>n/2\)，
\[
H^r(M)\hookrightarrow L^\infty(M)
\]
且 \(H^r\) 是乘法代数。于是
\[
\|D^2G_1\|_{H^r}\le \|G_1\|_{H^{r+2}}=\|G_1\|_{H^s},
\]
并且
\[
\|\beta_1^2-\beta_2^2\|_{H^r}
\le C_R\|\omega\|_{H^r}.
\]
所以
\[
\|(\beta_1^2-\beta_2^2)G_1^{-1}D^2G_1\|_{H^r}
\le C_R\|\omega\|_{H^r}
\]
确实成立。顶阶项
\[
\omega\,D^sG_1
\]
正是由
\[
\|\omega\|_\infty\|D^sG_1\|_2
\]
控制。

### Lie 差项中的实质性错误

设
\[
\mathcal W(G)=W(G)^\flat_G.
\]
应使用
\[
\begin{aligned}
d(\beta_1^2)\odot\mathcal W(G_1)
-d(\beta_2^2)\odot\mathcal W(G_2)
={}&[d(\beta_1^2)-d(\beta_2^2)]\odot\mathcal W(G_1)\\
&+d(\beta_2^2)\odot[\mathcal W(G_1)-\mathcal W(G_2)],
\end{aligned}
\]
以及
\[
d(\beta_1^2)-d(\beta_2^2)
=2\beta_2d\omega+2\omega d\beta_1.
\]

这样：

- \(\beta_2d\omega\,\mathcal W(G_1)\) 的顶阶项是
  \[
  \beta_2\mathcal W(G_1)D^{r+1}\omega,
  \]
  分部积分后产生 \(\beta_2D^{r+1}Z\)，与分支 2 的耗散匹配；
- \(\omega d\beta_1\,\mathcal W(G_1)\) 保持为完整分支量，并有
  \[
  \|\omega d\beta_1\,\mathcal W(G_1)\|_{H^r}
  \le C_R\|\omega\|_{H^r};
  \]
- \(d(\beta_2^2)[\mathcal W(G_1)-\mathcal W(G_2)]\) 的顶阶项带有
  \[
  \beta_2d\beta_2\,D^{r+1}Z,
  \]
  也可由同一带权耗散吸收。

Step 55 中写出的
\[
\omega\,d\beta_1\,D^{r+1}Z
\]
若真的出现，则没有 \(\beta_2\) 权重，不能一致吸收；Young 不等式会引入 \((\beta_2^2+\varepsilon)^{-1}\)。该项应通过上述完整分支分解避免，而不是按当前文字处理。

\(Q\)-差项同样不必依赖张量版积分恒等式。对
\[
\int D^rZ\cdot\beta_2^2 A\,D^{r+1}Z
\]
直接使用带权 Young 即可。

由此看，Proposition 4.1 的目标估计具有可行结构，但当前证明必须替换 Lie 差项段落，并改写 \(Q\)-项论证。

---

## 3. Pullback 公式

文中 (7.1) 写成
\[
\partial_t\varphi(t,x)
=-\beta(t,x)^2W(G)(t,\varphi(t,x)),
\]
这不是标准 DeTurck ODE。正确公式是
\[
\boxed{
\partial_t\varphi(t,x)
=-\beta(t,\varphi(t,x))^2
W(G)(t,\varphi(t,x)).
}
\]
等价地，Eulerian 速度为
\[
X_t=\partial_t\varphi_t\circ\varphi_t^{-1}
=-\beta(t,\cdot)^2W(G_t).
\]
不是文中所写的
\[
-\beta(t,\varphi^{-1}(y))^2W(G)(t,y).
\]

在修正后的 ODE 下，
\[
\frac d{dt}\beta(t,\varphi(t,x))
=\partial_t\beta+X\cdot D\beta
=\beta^2W\cdot D\beta-\beta^2W\cdot D\beta=0,
\]
故
\[
\beta(t,\varphi(t,x))=\chi(x),
\qquad
\beta(t,y)=\chi(\varphi^{-1}(t,y)).
\]
随后
\[
\frac d{dt}\varphi^*G
=\varphi^*(\partial_tG+\mathcal L_XG)
\]
中的 Lie 项严格抵消。对任意二阶张量 \(T\)，
\[
\varphi^*(\beta^2T)
=(\beta\circ\varphi)^2\varphi^*T
=\chi^2\varphi^*T.
\]
因此
\[
\varphi^*\!\left[-2\beta^2(\operatorname{Ric}(G)+G)\right]
=-2\chi^2(\operatorname{Ric}(\varphi^*G)+\varphi^*G),
\]
即得到目标几何方程。

若保留原 (7.1)，则 \(f'(t)=0\) 的计算并不成立。

---

## 4. \(\varepsilon\to0\) 与退化系统唯一性

若任意 \(k\) 都有一致估计
\[
\sup_{\varepsilon,t}\|G_\varepsilon(t)\|_{C^{k+2}}<\infty,
\]
则
\[
\|\varepsilon G_\varepsilon^{-1}D^2G_\varepsilon\|_{C^k}
\le C_k\varepsilon\longrightarrow0.
\]
因此该项的极限没有问题。

对 \(\varepsilon=0\) 的唯一性，一致椭圆性并不是必需前提。对两个已经光滑的解，主项分部积分给出
\[
-\int\beta_2^2|D^{r+1}Z|^2,
\]
这是符号确定的项；即使在 \(\beta_2=0\) 处消失，也可在 Grönwall 估计中保留或舍去。只要所有其余顶阶项按上一节正确配置权重，就有
\[
E_r'(t)\le C_RE_r(t),
\]
从同初值推出 \(E_r\equiv0\)。

当前真正未展开的是 Proposition 5.1。文中“至多 \(m-1\) 阶的系数由 \(E_s\) 控制”并不准确：当 \(m-1>s\) 时，这些量需要 \(E_{m-1}\)。合理的 tame 形式应是
\[
E_m'+c_mD_m
\le C(E_s)E_m+P_m(E_{m-1}),
\]
并逐项处理：

- 主系数 \(D^j[(\beta^2+\varepsilon)G^{-1}]\)；
- Lie 项中的 \(D^{m+1}\beta\)，经分部积分转移到 \(G\)；
- transport 项中的 \(\beta^2D^{m+1}G\)；
- 各阶时间导数且不出现 \(\varepsilon^{-1}\)。

固定 \(\varepsilon\) 的存在性本身较为标准，但 Proposition 2.1 中“mollification 后成为 parabolic + ODE”并不准确：\(\beta\) 方程仍是空间 transport PDE，除非也对其右端作 Friedrichs 截断。混合抛物—transport 理论或完整 Friedrichs–Galerkin 构造可以补足这一点。

---

## 5. 零集界面的光滑性

“光滑函数序列”本身不能保证光滑极限，例如
\[
\sqrt{x^2+\varepsilon}\to |x|.
\]
但若确实得到对每个 \(k\) 的一致高阶估计，并经对角抽取得到
\[
(G_{\varepsilon_j},\beta_{\varepsilon_j})
\to(G_0,\beta_0)
\quad\text{于每个 }C^k([0,T]\times M),
\]
那么极限就是 \(C^\infty\)，零集界面不可能另外生成奇异性。

零集保持也可直接验证。对固定 \(x\)，
\[
\partial_t\beta(t,x)
=a(t,x)\beta(t,x)^2,
\qquad
a=W(G)\cdot D\beta,
\]
而 \(a\) 光滑；若 \(\beta(0,x)=0\)，则 \(\beta(t,x)=0\)。此时
\[
\beta^2=0,\qquad d(\beta^2)=2\beta\,d\beta=0,
\]
所以退化 gauged 方程在该点给出 \(\partial_tG=0\)。

因此，零集正则性结论在真正的全阶一致紧致性成立后是正确的；仅 Proposition 3.1 的有限阶估计还不足以推出这一结论。

---

## 最终数学状态

直接非线性方案的两个核心机制——平方权重对顶阶耦合的吸收，以及 \(r=s-2\) 对主系数差的控制——均得到支持。当前文稿需要三项实质修订：

1. 用正确的分支定向分解重写 Lie 差项；
2. 修正微分同胚 ODE 与 Eulerian 速度；
3. 把任意阶 tame 能量、时间正则性、正定性 bootstrap 和共同时间延拓写成完整证明。

完成这些推导后，所给五个问题中没有发现阻止逐数据短时光滑解构造的结构性障碍。Theorem 9.1 中几何解的“唯一”还需补充标准的反向 DeTurck 变换：把任意几何解送入同一个 \((G,\beta)\) 系统，再应用修正后的 Proposition 4.1。
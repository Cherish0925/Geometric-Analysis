# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 16,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step16_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step16_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently analyze the proposed exponential-pullback chart averaging lemma in dimension four. Let (M,g) be closed with |sec_g|<=K on a buffered region U, fix 0<r<min(buffer, pi/(2 sqrt K)) so exp_p^*g is nonsingular on B_r(0) subset T_pM for every p in a positive-volume set P whose r-geodesics remain in U. For nonnegative measurable F supported in U, determine whether one can prove

∫_P [Vol_{exp_p^*g}(B_r(0))^{-1} ∫_{B_r(0)} F(exp_p v) dμ_{exp_p^*g}(v)] dμ_g(p) <= C(n,K,r) ∫_U F dμ_g,

with no injectivity-radius or sheet-number assumption. Give a rigorous derivation or counterexample. Track polar-coordinate Jacobians, the v=0 singularity, conjugate-radius assumptions, Liouville/geodesic-flow invariance, and normalization of pullback-ball volume. Also explain what curvature-derivative bounds are needed for smooth compactness of these exponential charts. This is for a collapsed near-Einstein four-manifold route; do not assume CFG or local covers.

## Integrated Scientific Memo

## 结论

该平均不等式成立，而且不需要注入半径、指数映射单射性或 sheet 数上界。事实上，仅需曲率控制沿 \(p\in P\) 发出的长度 \(<r\) 径向测地线成立：

\[
\int_P
\frac{\displaystyle\int_{B_r(0)}F(\exp_pv)\,d\mu_{\exp_p^*g}(v)}
{\displaystyle\operatorname{Vol}_{\exp_p^*g}(B_r(0))}
\,d\mu_g(p)
\le C(n,K,r)\int_UF\,d\mu_g,
\]

其中可取

\[
\boxed{
C(n,K,r)=
\frac{\displaystyle\int_0^r
\left(\frac{\sinh(\sqrt K\,t)}{\sqrt K}\right)^{n-1}dt}
{\displaystyle\int_0^r
\left(\frac{\sin(\sqrt K\,t)}{\sqrt K}\right)^{n-1}dt}
}
\]

并按 \(K=0\) 的极限解释为 \(C(n,0,r)=1\)。这里 \(r<\pi/(2\sqrt K)\)；实际上对比较论证，\(r<\pi/\sqrt K\) 已足够。

在四维，令 \(x=\sqrt K r\)，则

\[
C(4,K,r)
=
\frac{\cosh ^3x-3\cosh x+2}
{2-3\cos x+\cos ^3x}
\le
\left(\frac{\sinh x}{\sin x}\right)^3 .
\]

第二分支提出需要对 \(\operatorname{supp}F\) 的整个 \(r\)-邻域控制曲率，是其 multiplicity-reversal 证明所需的额外条件，但不是原不等式本身所需条件。下面的 Liouville–Jacobian 证明只使用 \(p\in P\) 的指定径向段上的曲率控制，因此与题设完全吻合。

---

## 1. 指数拉回图的极坐标 Jacobian

固定 \(p\in P\)、\(\theta\in S_pM\)，记

\[
\gamma_{p,\theta}(t)=\exp_p(t\theta).
\]

令径向 Jacobi 张量

\[
A_{p,\theta}(t):\theta^\perp\longrightarrow \dot\gamma(t)^\perp
\]

满足

\[
A(0)=0,\qquad D_tA(0)=I,\qquad
D_t^2A+R(\,\cdot\,,\dot\gamma)\dot\gamma=0.
\]

设 \(h_p=\exp_p^*g\)。由于 \(d\exp_p\) 在 \(B_r(0)\) 上非奇异，极坐标密度为

\[
J_p(t,\theta)=|\det A_{p,\theta}(t)|>0,
\qquad
d\mu_{h_p}=J_p(t,\theta)\,dt\,d\sigma_p(\theta).
\]

从 Rauch 比较及 \(-K\le\sec_g\le K\) 得到各奇异值满足

\[
s_K(t)\le \sigma_j(A_{p,\theta}(t))\le s_{-K}(t),
\]

其中

\[
s_K(t)=\frac{\sin(\sqrt Kt)}{\sqrt K},
\qquad
s_{-K}(t)=\frac{\sinh(\sqrt Kt)}{\sqrt K}.
\]

因此

\[
\boxed{
s_K(t)^{n-1}\le J_p(t,\theta)\le s_{-K}(t)^{n-1}.
}
\tag{1}
\]

上截面曲率界也保证首次共轭时刻不早于 \(\pi/\sqrt K\)，故若所有径向段均留在曲率受控区内，则题设的非奇异性事实上由 \(r<\pi/\sqrt K\) 推出。短闭环可以造成很小的 cut radius，却不会造成 \(d\exp_p\) 奇异；这正是 collapse 与 conjugacy 必须区分之处。

### \(v=0\) 没有真正奇性

极坐标在 \(t=0\) 退化，但拉回度量并不退化，因为

\[
d\exp_p|_0=I.
\]

更精确地，

\[
A(t)=tI+O(t^3),\qquad
J_p(t,\theta)=t^{n-1}(1+O(t^2)).
\]

所以 Cartesian 体积密度 \(J_p/t^{n-1}\to1\)。点 \(v=0\) 是零测集，对任意非负可测 \(F\) 不产生附加项。

---

## 2. 拉回球体积的统一下界

记

\[
V_p=\operatorname{Vol}_{h_p}(B_r(0)).
\]

由 (1)，

\[
\begin{aligned}
V_p
&=\int_{S_pM}\int_0^rJ_p(t,\theta)\,dt\,d\sigma_p(\theta)\\
&\ge
\omega_{n-1}\int_0^r s_K(t)^{n-1}\,dt.
\end{aligned}
\tag{2}
\]

这个 normalizer 是拉回球体积，而不是像集 \(B_r^g(p)\) 的体积。即使 \(\exp_p\) 绕一个高度塌缩流形许多次，拉回积分和 \(V_p\) 都逐 sheet 计数，而 (2) 仍给出仅依赖 \(n,K,r\) 的正下界。

---

## 3. Liouville 不变性给出平均上界

把 \(F\) 在 \(M\setminus U\) 上延拓为零，并设

\[
N_p=\int_{B_r(0)}F(\exp_pv)\,d\mu_{h_p}(v).
\]

由极坐标公式和 (1)，

\[
N_p
\le
\int_0^r s_{-K}(t)^{n-1}
\int_{S_pM}F(\gamma_{p,\theta}(t))\,d\sigma_p(\theta)\,dt.
\tag{3}
\]

令 \(SM\) 为单位切丛，\(\phi_t\) 为测地流，\(\pi:SM\to M\) 为投影。Liouville 测度

\[
dL(p,\theta)=d\mu_g(p)\,d\sigma_p(\theta)
\]

由 \(\phi_t\) 保持。因此

\[
\int_{SM}F(\pi\phi_tz)\,dL(z)
=
\int_{SM}F(\pi z)\,dL(z)
=
\omega_{n-1}\int_UF\,d\mu_g.
\tag{4}
\]

由于 \(F\ge0\)，可以把 \(SM|_P\) 扩大为整个 \(SM\)。由 Tonelli、(3)、(4)，

\[
\begin{aligned}
\int_PN_p\,d\mu_g(p)
&\le
\int_0^r s_{-K}(t)^{n-1}
\int_{SM|_P}F(\pi\phi_tz)\,dL(z)\,dt\\
&\le
\omega_{n-1}
\left(\int_0^r s_{-K}(t)^{n-1}\,dt\right)
\int_UF\,d\mu_g.
\end{aligned}
\tag{5}
\]

结合 (2) 即得

\[
\begin{aligned}
\int_P\frac{N_p}{V_p}\,d\mu_g(p)
&\le
\frac{\int_0^r s_{-K}(t)^{n-1}dt}
{\int_0^r s_K(t)^{n-1}dt}
\int_UF\,d\mu_g.
\end{aligned}
\]

这完成证明。

---

## 4. 为什么任意 sheet multiplicity 不造成损失

固定 \(p\) 时，\(\exp_p:B_r(0)\to M\) 可以多次覆盖同一点；若应用面积公式，确实会出现 multiplicity

\[
m_r(p,y)=\#\{v\in B_r(0):\exp_pv=y\}.
\]

但上述证明根本不需要估计 \(m_r\)。遗忘终端方向后，映射

\[
(p,\theta)\mapsto \gamma_{p,\theta}(t)
\]

可能高度多对一；保留终端方向后，

\[
(p,\theta)\mapsto
\bigl(\gamma_{p,\theta}(t),\dot\gamma_{p,\theta}(t)\bigr)
=\phi_t(p,\theta)
\]

却是 \(SM\) 上保持 Liouville 测度的双射。终端方向精确保留了 sheet 信息。

塌缩平坦环面是校验例：即使 \(B_r(0)\) 在环面上绕行任意多次，

\[
\exp_p^*g=g_p^{\mathrm{Eucl}},\qquad
J_p=t^{n-1},
\]

故 \(C(n,0,r)=1\)。反之，若错误地用像球体积
\(\operatorname{Vol}_g(B_r(p))\) 归一化，则该量在平坦塌缩环面上趋零，而拉回积分仍按所有 sheet 计数，不等式一般失效。

---

## 5. 关于 alternative multiplicity proof 的限定

也可借面积公式、测地线反演以及

\[
m_r(p,y)=m_r(y,p)
\]

证明同一常数：

\[
\int_Mm_r(p,y)\,d\mu_g(p)
=
\operatorname{Vol}_{\exp_y^*g}(B_r(0)).
\]

但随后要用模型上界控制右侧，就必须知道从每个
\(y\in\operatorname{supp}F\) 发出的全部长度 \(r\) 测地段也处于
\(|\sec|\le K\) 区域。题设只明确保证了 \(p\in P\) 的径向段，因此该证明会人为增加对 \(\operatorname{supp}F\) 的 buffer 条件。Liouville–Jacobian 证明避免了此缺口。

此外，单个纤维的 preimage 未必需要逐点声明为有限；面积公式只需其几乎处处 multiplicity。Liouville 证明也避开了这一不必要的技术问题。

---

## 6. 指数拉回图的光滑紧性需要什么

截面曲率界本身只给 Jacobi 比较、体积控制及 \(C^0\) 椭圆性；它不蕴含拉回度量族的 \(C^\infty\) 预紧性。

在选定正交标架把 \(T_pM\) 识别为 \(\mathbb R^n\) 后，径向和横向 Jacobi 比较给出，在 \(B_{r'}(0)\)、\(r'<r\) 上，

\[
a(K,r')^2g_{\mathrm{Eucl}}
\le h_p\le
b(K,r')^2g_{\mathrm{Eucl}},
\]

其中可取

\[
a(K,r')=\frac{\sin(\sqrt Kr')}{\sqrt Kr'},
\qquad
b(K,r')=\frac{\sinh(\sqrt Kr')}{\sqrt Kr'}.
\]

但若要求拉回度量本身在固定坐标中 \(C^\infty_{\rm loc}\) 预紧，一个标准充分条件是对每个 \(m\ge0\)，

\[
\sup_U|\nabla^m\operatorname{Rm}(g_i)|\le C_m,
\tag{6}
\]

并且这些界在所考察径向像之外有少量 cushion。因为 \(\exp_{p_i}\) 是局部等距，

\[
|\nabla^m\operatorname{Rm}(h_i)|(v)
=
|\nabla^m\operatorname{Rm}(g_i)|(\exp_{p_i}v).
\]

对测地线和 Jacobi 方程反复微分即可从 (6) 得到 \(h_i\) 的各阶坐标导数界。于是对每个 \(r'<r\) 可抽取

\[
h_i\to h_\infty
\quad\text{in }C^\infty(B_{r'}(0)).
\]

若要直到闭球 \(\overline{B_r(0)}\) 的一致光滑控制，应在稍大于 \(r\) 的区域有同样估计。

仅有 \(|\sec|\le K\) 不能替代 (6)。例如在 \(T^4\) 上取

\[
g_j=e^{2u_j(x_1)}(dx_1^2+dx_2^2)+dx_3^2+dx_4^2,
\qquad
u_j=j^{-2}\sin(jx_1).
\]

其截面曲率一致有界，但在适当基点

\[
|\nabla\operatorname{Rm}(g_j)|\asymp j,
\]

故对应指数拉回图不可能具有光滑收敛子列。

较弱的结论应明确区分：

- 有界曲率、非塌缩和适当 Ricci 控制可给 harmonic-coordinate 中的 \(C^{1,\alpha}\)/\(W^{2,p}\) 紧性；
- 若弱极限满足 Einstein 方程，则可由 harmonic-coordinate 椭圆正则性把**极限**提升为光滑；
- 这并不意味着近似度量族具有 \(C^{2,\alpha}\)，更不意味着其 \(C^\infty\) 一致控制；
- 若平滑流已在正时间给出 Shi 型
  \(|\nabla^m\mathrm{Rm}|\) 界，则可直接获得所需的光滑图紧性。

---

## 7. 对 collapsed near-Einstein 路线的准确产出

若 \(\mu_g(P)>0\)，上述平均不等式立即给出某个 \(p\in P\) 满足

\[
\frac1{V_p}
\int_{B_r(0)}F(\exp_pv)\,d\mu_{h_p}
\le
\frac{C(n,K,r)}{\mu_g(P)}
\int_UF\,d\mu_g.
\]

因此取 \(F=|\operatorname{Ric}+g|^2\) 或非负 Chern–Weil/monopole deficit 密度，可在完全不使用 CFG 或局部覆盖的情况下，把全局小缺陷传送到一个“展开的”指数拉回图上，且不受 collapse 或 sheet 数影响。

该结论只提供归一化 \(L^1\) 传送（对 \(F=|E|^2\) 即缺陷的 \(L^2\) 小性）。它本身不提供：

1. 曲率导数界或拉回图的光滑紧性；
2. Weyl 谱的点态收敛；
3. monopole harmonic form 在选定图上的非消失；
4. 从平均缺陷到 step6 中 calibrated Einstein germ 的完整椭圆传递。

这些仍需正时间平滑/导数估计、Einstein 椭圆正则性及 monopole/eigenline 论证。该 averaging lemma 严格解决的是“任意塌缩和任意指数 sheet multiplicity 下，能否保持拉回平均缺陷”这一环节。
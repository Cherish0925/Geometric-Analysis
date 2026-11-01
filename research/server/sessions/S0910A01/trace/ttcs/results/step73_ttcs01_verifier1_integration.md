# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 73,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step73_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step73_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematical correctness and completeness of three structural results for the graph-neck construction on T^3 graph manifolds.

Result 1 — Preissmann obstruction: For every Riemannian metric h on T^3, max |Ric_h + 2h|_op >= 2/3. The argument uses the 3D identity K_{ij} = (r_i + r_j - r_k)/2 to show that if all Ricci eigenvalues satisfy |r_i + 2| < c with c < 2/3, then all sectional curvatures are strictly negative, contradicting Preissmann's theorem for T^3 (which has Z^3 fundamental group containing Z^2). At c = 2/3, the flat torus theorem forces flatness but R_h = -16/3 ≠ 0.

Result 2 — Koiso center: At a totally geodesic center S(0) = 0 in a Gaussian collar, the Einstein equations force S'(0) = Ric_h + 3I and R_h = -6. Isotropic S' = I requires Ric_h = -2h (constant negative curvature), impossible on T^3 by Preissmann. For the T^2-invariant diagonal ansatz with a_0 = 0, the constraint R_h = -6 becomes u^2 + v^2 + uv + u' + v' = 3 where u = b_{0,theta}, v = c_{0,theta}. The Koiso accelerations are a_tt = uv, b_tt = v^2 + v', c_tt = u^2 + u'.

Result 3 — ODE anisotropy decay: For the diagonal ODE f_i'' + f_i' H = 3, the difference delta_ij = f_i' - f_j' satisfies delta_ij' + H delta_ij = 0, giving exponential decay delta_ij(t) = delta_ij(0) sech(sqrt(3) t). The claim that higher Fourier modes in the full PDE decay faster rests on the additional n^2 e^{-2a} term in the linearized operator.

Check: (a) Is the Preissmann argument correct at the boundary c = 2/3? (b) Are the Koiso formulas (3.3) correct from the T^2-inv Einstein equations? (c) Is the difference equation (4.2) correct? (d) Does the a=0 gauge really force b_t c_t = 0? (e) Is the claim about higher Fourier mode stability justified?

## Integrated Scientific Memo

# 核验结论

## 总表

| 待核验项 | 结论 |
|---|---|
| (a) \(c=2/3\) 的 Preissmann 边界论证 | 结论正确，但原文的固定特征值三元组论证不成立；可修正并加强为严格 \(>2/3\) |
| (b) Koiso 中心公式与 (3.3) | 正确，取决于约定 \(S=\frac12h_t^{-1}\partial_t h_t\) |
| (c) 差分方程 (4.2) | 对所写的简化 ODE 正确；但 \(\operatorname{sech}(\sqrt3t)\) 不正确，且该 ODE 丢失了产生 Koiso 各向异性的内禀 Ricci 项 |
| (d) \(a\equiv0\) 是否迫使 \(b_tc_t=0\) | 对完整 \(T^2\)-不变 PDE：否；正确关系是 \(b_tc_t+b_\theta c_\theta=0\)。仅在齐次 ODE 子系统中才推出 \(b_tc_t=0\) |
| (e) 高频 Fourier 模式是否衰减更快 | 现有论证不足；主部项既不保证选取衰减支，也不改变固定模式的 cusp 主导指标根 |

---

## 1. Preissmann 阻碍

令
\[
D(h)=\max_{T^3}\bigl|\operatorname{Ric}_h+2h\bigr|_{\mathrm{op}}.
\]
若 \(D(h)\le 2/3\)，则对每个单位向量 \(X\)，
\[
-\frac83\le \operatorname{Ric}(X,X)\le-\frac43.
\]
在三维，对任意正交单位标架 \(u,v,w\)，
\[
K(u,v)=\frac12\{\operatorname{Ric}(u,u)+\operatorname{Ric}(v,v)
-\operatorname{Ric}(w,w)\}\le0.
\]
因此 \(h\) 具有非正截面曲率。非正曲率三维环面的平坦环面定理推出 \(h\) 平坦，于是
\[
D(h)=|0+2I|_{\mathrm{op}}=2,
\]
与 \(D(h)\le2/3\) 矛盾。故实际上
\[
\boxed{D(h)>\frac23}.
\]

所以所需较弱结论 \(D(h)\ge2/3\) 成立。若只证明这一弱结论，\(D<2/3\) 时由严格负截面曲率和 Preissmann 已足够；排除等号才需要非正曲率下的平坦性结论。

原文“边界特征值必为
\((-4/3,-4/3,-8/3)\)，故 \(R=-16/3\)”不成立：界限饱和并不强迫全体 Ricci 特征值等于这一组三元组。可用上述“\(K\le0\Rightarrow\) 平坦，但平坦时 \(D=2\)”替换。也可直接注意区间给出 \(R\le-4\)，与平坦性矛盾。

因此对
\[
g=dt^2+\cosh^2(t)h
\]
中心截面的 Einstein 缺陷下界正确：
\[
\left.\|\operatorname{Ric}_g+3g\|_{\mathrm{op}}\right|_{t=0}
=D(h)>\frac23.
\]
现有论证并未证明 \(2/3\) 是所有环面度量中 \(D(h)\) 的实际下确界；它只是这一代数曲率论证的临界值。

---

## 2. Koiso 中心和公式 (3.3)

取
\[
S=\frac12h_t^{-1}\partial_t h_t,\qquad H=\operatorname{tr}S.
\]
Gaussian 坐标下
\[
\operatorname{Ric}_{00}=-H'-|S|^2,
\qquad
\operatorname{Ric}^{\sharp}_{\mathrm{tan}}
=\operatorname{Ric}_{h_t}^{\sharp}-S'-HS.
\]
若 \(S(0)=0\) 且 \(\operatorname{Ric}_g=-3g\)，则
\[
\operatorname{tr}S'(0)=3,\qquad
S'(0)=\operatorname{Ric}_{h}^{\sharp}+3I.
\]
取迹得到
\[
3=R_h+9,\qquad \boxed{R_h=-6}.
\]
若 \(S'(0)=I\)，则 \(\operatorname{Ric}_h=-2h\)。三维 Einstein 度量具有常截面曲率 \(-1\)，这与 \(T^3\) 的基本群含 \(\mathbb Z^2\) 相矛盾。

对
\[
h=d\theta^2+e^{2b_0(\theta)}dx^2+e^{2c_0(\theta)}dy^2,
\qquad u=b_0',\quad v=c_0',
\]
Ricci 特征值为
\[
\begin{aligned}
r_\theta&=-(u'+v'+u^2+v^2),\\
r_x&=-(u'+u^2+uv),\\
r_y&=-(v'+v^2+uv).
\end{aligned}
\]
故
\[
R_h=-2(u^2+v^2+uv+u'+v'),
\]
而 \(R_h=-6\) 等价于
\[
u^2+v^2+uv+u'+v'=3.
\]
由 \(S'(0)=\operatorname{Ric}_h^\sharp+3I\)：
\[
\boxed{
a_{tt}=uv,\qquad
b_{tt}=v^2+v',\qquad
c_{tt}=u^2+u'.}
\]
所以 (3.3) 完全正确，其和确为 \(3\)。

### 数值“环面纤维”的额外缺口

要使 \(u=b_0'\)、\(v=c_0'\) 真正来自 \(S^1\) 上的周期函数，还必须满足
\[
\int_0^{2\pi}u\,d\theta=0,\qquad
\int_0^{2\pi}v\,d\theta=0.
\]
\(v=B\sin\theta\) 自动满足第二式，但 Riccati 方程的周期解 \(u\) 不自动具有零平均值。现有 JSON 只核验了 \(u\) 的周期性/曲率残差，没有记录 \(\int u\)。因此它验证了局部公式，却尚未证明所列 \(b_0\) 真正下降为 \(T^3\) 上的光滑度量。

---

## 3. ODE 差分式及其适用范围

若确实采用简化系统
\[
s_i'+Hs_i=3,\qquad H=s_1+s_2+s_3,
\]
则相减得到
\[
\boxed{\delta_{ij}'+H\delta_{ij}=0},
\qquad
\delta_{ij}=s_i-s_j,
\]
以及
\[
\delta_{ij}(t)=\delta_{ij}(0)
\exp\!\left(-\int_0^tH(\tau)\,d\tau\right).
\]
所以 (4.2) 的代数恒等式正确。

但是其后的具体公式不正确。对所显示的三方向 ODE 求和：
\[
H'+H^2=9.
\]
若 \(H(0)=0\)，则
\[
H(t)=3\tanh(3t),\qquad
e^{-\int_0^tH}=\operatorname{sech}(3t).
\]
因此该 ODE 给出的是
\[
\boxed{\delta_{ij}(t)=\delta_{ij}(0)\operatorname{sech}(3t),}
\]
不是 \(\operatorname{sech}(\sqrt3t)\)。\(\sqrt3\tanh(\sqrt3t)\) 来自 \(a=0\) 的两方向/rank-one 归约 \(H'=3-H^2\)，不能与三方向 cusp 的 \(H\to3\) 混用。

更关键的是，这个简化 ODE 不能描述 Koiso 中心各向异性。反射中心有 \(s_i(0)=0\)，故 \(\delta_{ij}(0)=0\)，简化系统会永久保持各向同性，并强迫所有 \(s_i'(0)=3\)。真正的切向 Einstein 方程包含切片的内禀 Ricci：
\[
s_i'+Hs_i=3+r_i(h_t).
\]
因此正确的差分方程是
\[
\boxed{
\delta_{ij}'+H\delta_{ij}=r_i(h_t)-r_j(h_t),
}
\]
并有 Duhamel 表示
\[
\delta_{ij}(t)
=e^{-\int_0^tH}
\int_0^t e^{\int_0^\tau H}
\bigl(r_i(h_\tau)-r_j(h_\tau)\bigr)\,d\tau
\]
（反射中心时初始差为零）。正是右端内禀 Ricci 各向异性产生了 Koiso 的不同加速度。要证明完整 PDE 中各向异性衰减，必须控制这一强迫项；无强迫 ODE 本身不能完成该论证。

---

## 4. \(a\equiv0\) 的实际约束

令
\[
p=b_t,\quad q=c_t,\quad u=b_\theta,\quad v=c_\theta.
\]
对完整度量
\[
g=dt^2+d\theta^2+e^{2b(t,\theta)}dx^2+e^{2c(t,\theta)}dy^2,
\]
Einstein 方程的组合给出
\[
\boxed{pq+uv=0},
\]
即
\[
\boxed{b_tc_t=-b_\theta c_\theta}.
\]
因此完整 \(T^2\)-不变 PDE 并不推出 \(b_tc_t=0\)。

只有进一步施加 \(\theta\)-齐次条件 \(u=v=0\) 时，才得到
\[
b_tc_t=0.
\]
所以“\(a=0\) 迫使形算子秩至多一”仅是齐次 ODE 子系统的结论，不是完整 PDE 的结论。

此外，\(a\equiv0\) 不是无害的坐标规范，而是限制性度量 ansatz。中心处它要求 \(a_{tt}=0\)，而 Koiso 公式要求
\[
a_{tt}=uv.
\]
因此只要 \(uv\ne0\)，Koiso 解立即离开 \(a\equiv0\) 类。无论是否使用错误的 \(b_tc_t=0\)，\(a_t\equiv0\) 本身也已阻止该方向趋向 cusp 所需的 \(a_t\to1\)。

---

## 5. 高频 Fourier 模式

主部
\[
\partial_{tt}+e^{-2a}\partial_{\theta\theta}
\]
作用于 \(y_n(t)e^{in\theta}\) 后成为
\[
y_n''-n^2e^{-2a(t)}y_n.
\]
单凭这一项不能推出高频模式自动衰减更快：

1. 在 \(a\) 近似常数的区域，模型方程
   \[
   y_n''-n^2y_n=0
   \]
   同时具有 \(e^{|n|t}\) 和 \(e^{-|n|t}\) 两支；椭圆 Cauchy 问题的高频不稳定性反而更强。

2. cusp 上 \(a(t)\sim t\)，故
   \[
   n^2e^{-2a(t)}\sim n^2e^{-2t}\to0.
   \]
   对每个固定 \(n\)，它是渐近低阶项，不改变由 \(n\)-无关部分决定的主导指标根。因此不能据此声称更快的 cusp 渐近指数。

在有限区间的两端边值问题中，该正频率项可能改善某个恰当符号下的 coercivity，但这与“沿 \(t\) 更快衰减”不同。严格结论需要完整 Einstein–DeTurck 线性化、规范项、边界条件、耦合零阶矩阵以及 cusp 指标谱的计算。

---

## 最终核验结论

- **Result 1：**成立，并可加强为
  \[
  \max_{T^3}|\operatorname{Ric}_h+2h|_{\mathrm{op}}>\frac23.
  \]
  但原边界特征值三元组应删除。
- **Result 2：**Koiso 中心恒等式、标量约束和 (3.3) 均正确；数值纤维还缺少 \(\int u=0\) 的全局周期核验。
- **Result 3：**差分恒等式只对无内禀 Ricci 强迫的简化 ODE 正确；其 \(\sqrt3\) 速率错误，且该简化系统无法产生 Koiso 各向异性。
- **\(a=0\)：**完整 PDE 只给出 \(b_tc_t+b_\theta c_\theta=0\)，并不迫使 \(b_tc_t=0\)。
- **高频稳定性：**尚未证明；现有主部观察不足以支持“高频模式渐近衰减更快”。
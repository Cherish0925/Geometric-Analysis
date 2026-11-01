# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 25,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step25_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step25_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check a claimed correction in a toric reduced-Einstein computation for Yau Problem 26. Context: a twist-free diagonal T^2-invariant Einstein 4-metric g = g_B + p^2 dtheta^2 + q^2 dphi^2 over a 2D orbit space Omega (a polygon), with w = pq, v = log(p/q). The verified reduced equations are: (1) -Delta_B w = 2w with w=0 on dOmega (Einstein lambda=1); the individual warping equations -Delta_B p=(K_B-1)p, -Delta_B q=(K_B-1)q, and <grad p, grad q> = -K_B w. On each rod (boundary segment) the collapsing fiber vanishes at unit slope and the surviving fiber Q(s) satisfies Q''+(1-2K_edge)Q=0 with Q'(0)=1,Q'(L)=-1, giving the exact rod identity int_rod (1-2K_edge)Q ds = 2, i.e. flux Phi_i = int Q ds = 2 + 2 int_rod K_edge Q ds.

CLAIM 1 TO CHECK: A prior note (Step 20) recorded an interior identity 'int_Omega K_B w = int_Omega w'. I now claim this clean interior identity is FALSE because the Green's-identity derivation drops boundary/corner terms. My evidence: for the exact product S^2 x S^2, Omega = [0,pi]^2 flat (K_B=0 in interior), w = sin x sin y, so int_Omega K_B w = 0 but int_Omega w = 4, a contradiction. Is my reasoning correct that the clean interior weighted-curvature identity does not hold, and that the only rigorous boundary-anchored constraints are (a) total flux = 2 int w and (b) the per-rod identity int(1-2K_edge)Q=2? Or is there a correct corner/edge-corrected version of int K_B w = int w that I am missing (e.g. with explicit corner delta-curvature terms), and if so what is it exactly?

CLAIM 2 TO CHECK: For a single rod with constant edge curvature K_edge = -A (A>0), Q = sin(sqrt(1+2A) s)/sqrt(1+2A), L = pi/sqrt(1+2A). I compute the Q-weighted negative-curvature charge G_i := int_rod (-K_edge) Q ds = int_0^L A Q ds = 2A/(2A+1), which tends to 1 as A -> infinity, and Phi_i = 2/(2A+1) = 2 - 2 G_i, tending to 0. Verify these two integrals and the relation Phi_i = 2 - 2 G_i exactly. Confirm or refute that a single constant-curvature rod can drive its flux to 0 while its Q-weighted negative charge G_i saturates at 1.

Do the exact integral algebra yourself. State whether each claim holds, and flag any sign or boundary-term error. Do not invent external literature; reason only from the stated equations.

## Integrated Scientific Memo

## 核验结论

### Claim 1：结论成立，但归因需要纠正

\[
\int_\Omega K_Bw\,dA=\int_\Omega w\,dA
\]

这个“纯内部恒等式”确实是假的。\(S^2\times S^2\) 的例子已经严格否定它：

\[
\Omega=[0,\pi]^2,\qquad K_B=0,\qquad w=\sin x\sin y,
\]

所以

\[
\int_\Omega K_Bw\,dA=0,\qquad
\int_\Omega w\,dA
=\left(\int_0^\pi\sin x\,dx\right)^2=4.
\]

但错误的根源不是遗漏了边界或角点项，而是题面所列的单独翘曲方程符号反了。与其余已核验方程及乘积例子相容的正确形式应为

\[
\boxed{-\Delta_Bp=(1-K_B)p,\qquad
-\Delta_Bq=(1-K_B)q.}
\]

而不是

\[
-\Delta_Bp=(K_B-1)p,\qquad
-\Delta_Bq=(K_B-1)q.
\]

两个直接检验是：

1. 对 \(S^2\times S^2\)，\(p=\sin x\)、\(K_B=0\)，有
   \[
   -\Delta_Bp=p,
   \]
   只符合 \(1-K_B\) 的符号。

2. 使用
   \[
   \langle\nabla p,\nabla q\rangle=-K_Bpq
   \]
   和正确方程，
   \[
   \begin{aligned}
   \Delta_B(pq)
   &=q\Delta_Bp+p\Delta_Bq
     +2\langle\nabla p,\nabla q\rangle\\
   &=-2(1-K_B)pq-2K_Bpq\\
   &=-2pq,
   \end{aligned}
   \]
   正好得到 \(-\Delta_Bw=2w\)。题面中的反号则不能与该方程一般相容。

### 正确的 Green 恒等式

记 \(\Phi_p\) 为所有 \(p\)-塌缩杆的通量之和。由 Green 公式，

\[
\int_\Omega q(-\Delta_Bp)\,dA
=
\int_\Omega\langle\nabla p,\nabla q\rangle\,dA
-\int_{\partial\Omega}q\,\partial_\nu p\,ds.
\]

在 \(p\)-杆上 \(\partial_\nu p=-1\)、\(q=Q\)；在 \(q\)-杆上 \(q=0\)，故

\[
-\int_{\partial\Omega}q\,\partial_\nu p\,ds=\Phi_p.
\]

代入正确方程及交叉项：

\[
\int_\Omega(1-K_B)w\,dA
=
-\int_\Omega K_Bw\,dA+\Phi_p.
\]

曲率项恰好消去，得到

\[
\boxed{\Phi_p=\int_\Omega w\,dA.}
\]

同理，

\[
\boxed{\Phi_q=\int_\Omega w\,dA.}
\]

因此

\[
\boxed{\Phi_{\rm total}=\Phi_p+\Phi_q
=2\int_\Omega w\,dA.}
\]

所以严谨约束不止题目所说的两条，还应保留通量等分恒等式

\[
\boxed{\Phi_p=\Phi_q=\int_\Omega w\,dA.}
\]

### 没有能修复原等式的角点曲率项

在光滑 toric 角点附近，\(p=O(r_1)\)、\(q=O(r_2)\)，一阶导数有界。切除半径 \(\varepsilon\) 的小弧时，

\[
q\,\partial_\nu p\,ds=O(\varepsilon^2),
\]

故角点 Green 边界项趋于零。即使把多边形 Gauss–Bonnet 的角点曲率写成原子测度，其 \(w\)-加权也为零，因为 \(w=0\) 于角点；任何杆上的边支撑曲率同样被 \(w|_{\partial\Omega}=0\) 消去。因此不存在由这些项产生的、可将

\[
0=\int K_Bw
\]

修复为 \(4=\int w\) 的版本。

每杆恒等式仍然严格成立：

\[
\boxed{\int_{\mathrm{rod}_i}(1-2K_{\rm edge})Q_i\,ds=2,}
\]

等价于

\[
\boxed{\Phi_i
=2+2\int_{\mathrm{rod}_i}K_{\rm edge}Q_i\,ds.}
\]

将其求和并使用总通量公式，还得到

\[
\boxed{
\int_\Omega w\,dA
=
m+\sum_{i=1}^m\int_{\mathrm{rod}_i}K_{\rm edge}Q_i\,ds.
}
\]

---

## Claim 2：完全成立

令

\[
K_{\rm edge}=-A,\qquad A>0,\qquad
\omega=\sqrt{1+2A},
\]

则

\[
Q(s)=\frac{\sin(\omega s)}{\omega},
\qquad
L=\frac{\pi}{\omega}.
\]

确有

\[
Q'(0)=1,\qquad Q'(L)=\cos\pi=-1.
\]

杆通量为

\[
\begin{aligned}
\Phi_i
&=\int_0^LQ(s)\,ds\\
&=\int_0^{\pi/\omega}\frac{\sin(\omega s)}{\omega}\,ds\\
&=\frac{1}{\omega^2}\int_0^\pi\sin t\,dt\\
&=\boxed{\frac{2}{1+2A}}.
\end{aligned}
\]

负曲率荷为

\[
\begin{aligned}
G_i
&=\int_0^L(-K_{\rm edge})Q\,ds\\
&=A\int_0^LQ\,ds\\
&=\boxed{\frac{2A}{1+2A}}.
\end{aligned}
\]

于是

\[
2-2G_i
=
2-\frac{4A}{1+2A}
=
\frac{2}{1+2A}
=
\boxed{\Phi_i}.
\]

并且

\[
\boxed{\lim_{A\to\infty}\Phi_i=0,\qquad
\lim_{A\to\infty}G_i=1.}
\]

因此，一个常负曲率杆在局部 ODE 层面确实可以令通量趋于零，同时 \(Q\)-加权负曲率荷饱和到 \(1\)。这只是单杆局部结论，并不保证存在满足全部内部耦合 Einstein 方程的全局轨道空间。

源脚本中的 SymPy 输出

\[
G_i=\frac{2A}{2A+1}
\]

是正确的；随后手写注释误写成了 \(A/(1+2A)\)，由此虚假地产生了 \(G_i\to\frac12\) 和关系失效的“矛盾”。应删除该注释及基于漏掉因子 \(2\) 的 `part_B_reconcile` 计算。
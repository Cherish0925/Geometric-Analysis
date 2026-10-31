# TTCS Independent Branch Record

```json
{
  "step_id": 22,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md",
    "Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md",
    "Skills/geometric-analysis/research/sources/continuation/20260927_conformal_separation_and_zero_end.md"
  ]
}
```

## Task

Independently check the proposed theorem and proof that every smooth complete four-dimensional metric which is exactly complex hyperbolic outside a compact set admits a unique positive conformal factor u→1 giving scalar curvature -24, without any sign assumption on the original scalar curvature. Check the weak sub/supersolution signs including derivative jumps, exhaustion argument, positivity, uniqueness, decay range 4<m<2+2sqrt(3), derivative estimates, Pfaffian and integration-by-parts boundary terms, exact conformal energy identities, and equality of exact-ended J6 and scalar-normalized P infima. Identify and repair any incorrect implication; provide a direct mathematical memo rather than procedural commentary.

## Output

# Scientific memo: conformal normalization of exact-CH-ended four-metrics

## Overall assessment

For a marked end isometric to the exterior of a geodesic ball in normalized \(\mathbf{CH}^{2}\), the existence, positivity, uniqueness, decay, and conformal energy identities are mathematically valid. No sign hypothesis on \(s_g\) is needed.

The infimum statement also holds, but the normalized class must be defined precisely. As presently written, “decay in item 2” describes the conformal factor \(u\), not an arbitrary metric in \({\cal C}_{-24}\). There are two clean formulations:

1. define \({\cal C}_{-24}\) as the image of the exact-ended class under this conformal normalization; or
2. more naturally, define it as all scalar-\(-24\) metrics converging to the marked CH metric in \(C^\infty\) at some rate \(e^{-\mu r}\), \(\mu>4\).

For the second formulation, direct metric splicing proves the reverse infimum inequality. The stated cutoff argument only directly treats metrics of the form \(u^{2}g\) with \(g\) exactly CH-ended.

---

## 1. Weak sub- and supersolutions

Let \(\Sigma_R=\{r=R\}\), with the normal pointing toward increasing \(r\). For a continuous, piecewise \(C^{2}\) function \(f\),

\[
\Delta f=(\Delta f)_{\mathrm{reg}}
       +[\partial_\nu f]_{\Sigma_R}\,\delta_{\Sigma_R},
\]

where the jump is the exterior derivative minus the interior derivative.

For

\[
u_-=
\begin{cases}
0,&r\le R,\\
1-e^{-a(r-R)},&r\ge R,
\end{cases}
\qquad 0<a<4,
\]

the derivative jump is \(a\). Hence the singular part of

\[
F(u_-)=-6\Delta u_-+s_gu_-+24u_-^3
\]

is \(-6a\,\delta_{\Sigma_R}\le0\).

For

\[
u_+=
\begin{cases}
M,&r\le R,\\
1+(M-1)e^{-a(r-R)},&r\ge R,
\end{cases}
\]

the derivative jump is \(-a(M-1)\), so the singular part of \(F(u_+)\) is

\[
6a(M-1)\,\delta_{\Sigma_R}\ge0.
\]

Thus the corner signs are correct.

On the CH end, put \(t=r-R\) and \(H=\Delta r=3\coth r+\tanh r\ge4\). Then

\[
\Delta(1-e^{-at})=a(H-a)e^{-at}\ge0
\]

and, since \(0\le u_-<1\),

\[
F(u_-)
=-6a(H-a)e^{-at}+24u_-(u_-^2-1)\le0.
\]

Similarly,

\[
\Delta(1+(M-1)e^{-at})
=a(a-H)(M-1)e^{-at}\le0,
\]

while \(u_+\ge1\), so

\[
F(u_+)=-6\Delta u_++24u_+(u_+^2-1)\ge0.
\]

On the compact core,

\[
F(u_-)=0,\qquad F(u_+)=M(s_g+24M^2).
\]

Since \(s_g\) is bounded on the core and equals \(-24\) on the end, one can choose \(M\ge1\) so that \(s_g+24M^2\ge0\) everywhere. The ordering \(0\le u_-\le u_+\) and the inequalities at \(S_L=\{r=L\}\),

\[
u_-\le1\le u_+,
\]

are also correct.

---

## 2. Exhaustion and strict positivity

On \(\Omega_L=\{r<L\}\), prescribe \(u=1\) on \(S_L\). A fully explicit monotone scheme is obtained by choosing

\[
K>\sup_C(s_g+72M^2)
\]

and writing the equation as

\[
(-6\Delta+K)u=(K-s_g)u-24u^3.
\]

The right-hand side has derivative

\[
K-s_g-72u^2\ge0
\]

for \(0\le u\le M\). The inverse of \(-6\Delta+K\) with the stated Dirichlet data preserves order, so iteration between \(u_-\) and \(u_+\) gives a smooth solution \(u_L\) satisfying

\[
u_-\le u_L\le u_+.
\]

The shift \(K\) is uniform in \(L\), because \(s_g=-24\) outside a compact set.

The uniform \(C^0\) estimate gives uniform local elliptic estimates. Indeed,

\[
\Delta u_L=\frac{s_gu_L+24u_L^3}{6},
\]

whose right-hand side is uniformly bounded on every fixed compact subset. Local \(W^{2,p}\), Schauder estimates, and bootstrapping give a diagonal smooth limit \(u\). The barrier inequalities imply \(u\to1\) uniformly on the end.

The limit is positive on \(r>R\), since \(u\ge u_->0\) there. It satisfies

\[
-6\Delta u+(s_g+24u^2)u=0
\]

with bounded coefficient. The local Harnack theorem on the connected manifold therefore propagates strict positivity through the compact core. Since \(u\to1\), strict positivity on the compact part also gives a global constant \(c>0\) with

\[
c\le u\le M.
\]

Consequently \(u^2g\) is uniformly equivalent to \(g\) and is complete.

This construction does not require positivity of the conformal Laplacian. The shifted Dirichlet operator is used only on compact exhaustions, while the lower barrier is permitted to vanish on the core.

---

## 3. Uniqueness

Suppose \(u_i^2g\) both have scalar curvature \(-24\), with \(u_i\to1\). Set

\[
w=\frac{u_1}{u_2},\qquad g_2=u_2^2g.
\]

The scalar transformation law gives

\[
-6\Delta_{g_2}w-24w+24w^3=0,
\]

or

\[
-6\Delta_{g_2}w+24w(w^2-1)=0.
\]

Because \(w\to1\), any supremum above one or infimum below one is attained in a compact subset. At a maximum with \(w>1\),

\[
\Delta w\le0,
\]

so both terms in the last equation are \(>0\) after allowing the first to be \(0\), which is impossible. At a minimum with \(0<w<1\), both terms are \(<0\) after allowing the first to be \(0\), again impossible. Hence \(w\equiv1\).

This also justifies rerunning the barrier construction with different values of \(a\): every resulting exhaustion limit is the same function.

---

## 4. Exponential decay

Let \(v=u-1\). On the exact CH end,

\[
-6\Delta v+48v+72v^2+24v^3=0.
\]

Equivalently,

\[
(-6\Delta+q)v=0,
\qquad
q=48+72v+24v^2=24u(u+1)>0.
\]

For \(\phi_m=e^{-mr}\),

\[
(-6\Delta+q)\phi_m
=
\bigl[-6m^2+6mH+24u(u+1)\bigr]\phi_m.
\]

As \(r\to\infty\), the coefficient tends to

\[
6(-m^2+4m+8).
\]

It is strictly positive precisely for

\[
0<m<2+2\sqrt3.
\]

Fix such an \(m\). On a sufficiently far-out region,

\[
(-6\Delta+q)\phi_m>0.
\]

Choose \(C\) so that \(C\phi_m\ge |v|\) on its inner sphere. Both

\[
z_+=C\phi_m-v,\qquad z_-=C\phi_m+v
\]

tend to zero at infinity and satisfy

\[
(-6\Delta+q)z_\pm>0.
\]

If either became less than zero, its infimum below zero would be achieved at an interior point; there \(\Delta z_\pm\ge0\) and \(qz_\pm<0\), contradicting the displayed inequality. Thus

\[
|u-1|=|v|\le Ce^{-mr}.
\]

In fact this proves \(C^0\) decay for every \(0<m<2+2\sqrt3\), slightly more than the recorded interval. The interval \(m>4\) is selected because the CH sphere area grows like \(e^{4r}\).

For derivatives, on CH unit balls one has uniform geometric control and

\[
\Delta v=8v+12v^2+4v^3.
\]

Local \(W^{2,p}\) estimates followed by Sobolev embedding give the same exponential rate for the first two derivatives. Differentiating the equation and iterating gives, for every fixed \(k\),

\[
|\nabla^k(u-1)|=O(e^{-mr}),
\qquad 0<m<2+2\sqrt3.
\]

If desired, one may first take \(m<m'<2+2\sqrt3\) in the \(C^0\) estimate and use \(m'\) to absorb any local covering constants.

---

## 5. Surface contributions and conformal energy identities

Write

\[
A=\frac{\Delta u}{u}.
\]

For \(\widehat g=u^2g\),

\[
s_{\widehat g}^2\,dV_{\widehat g}
=(s_g-6A)^2\,dV_g.
\]

The pointwise Weyl density is conformally invariant. Comparing the Euler forms of \(g\) and \(\widehat g\) on \(C_R=\{r\le R\}\) therefore gives

\[
P(\widehat g;C_R)-P(g;C_R)
=
\int_{C_R}\bigl(-s_gA+3A^2\bigr)\,dV_g+\tau_R,
\]

where \(\tau_R\) is the Pfaffian transgression integral over \(S_R\).

The connection difference satisfies

\[
\nabla^{\widehat g}-\nabla^g
=O(|\nabla\log u|)
=O(e^{-mr}).
\]

Both curvature tensors remain bounded. The transgression is a polynomial of the form

\[
(\nabla^{\widehat g}-\nabla^g)\wedge R_t
\]

plus cubic connection-difference terms, hence its pointwise norm is \(O(e^{-mr})\). Since

\[
\operatorname{Area}(S_R)=O(e^{4R}),
\]

one obtains

\[
\tau_R=O(e^{(4-m)R})\longrightarrow0
\]

for any \(m>4\).

The scalar equation gives

\[
s_g=6A-24u^2.
\]

Consequently,

\[
\begin{aligned}
P(\widehat g)-P(g)
&=\int_C\left[-(6A-24u^2)A+3A^2\right]dV_g\\
&=\int_C\left[-3A^2+24u\Delta u\right]dV_g.
\end{aligned}
\]

Integration by parts on \(C_R\) produces the surface integral

\[
\int_{S_R}u\,\partial_\nu u\,dA_g
=O(e^{(4-m)R})\to0.
\]

Therefore

\[
P(g)-P(\widehat g)
=
24\int_C|\nabla u|^2\,dV_g
+
3\int_C\left(\frac{\Delta u}{u}\right)^2dV_g.
\]

Since \(s_{\widehat g}=-24\),

\[
J_6(\widehat g)=P(\widehat g),
\]

and hence

\[
J_6(g)-J_6(\widehat g)
=
\int_C\left[
24|\nabla u|^2
+3\left(\frac{\Delta u}{u}\right)^2
+\frac{(s_g+24)^2}{4}
\right]dV_g.
\]

All terms are finite. The scalar term for \(g\) is compactly supported, while the derivative terms decay quadratically. The exponent \(m>4\) is needed for the linear transgression and integration-by-parts contributions; quadratic integrability alone would only require \(m>2\).

If the first identity is an equality, then \(\nabla u=0\), and the end normalization gives \(u\equiv1\). On a closed manifold the same calculation permits constant conformal rescalings. In the \(J_6\) identity, equality also gives \(s_g\equiv-24\).

---

## 6. The infimum identity and its precise repair

Let \(g_{\mathrm{CH}}\) denote the marked CH metric. A mathematically definite normalized class is

\[
{\cal C}_{-24}^{\mathrm{aCH}}
=
\left\{
h:
s_h=-24,\quad
|\nabla_{\mathrm{CH}}^k(h-g_{\mathrm{CH}})|
=O(e^{-\mu r})\ \text{for all }k,
\ \text{for some }\mu>4
\right\}.
\]

Every normalized metric \(\widehat g=u^2g\) produced from an exact-ended \(g\) belongs to this class, since the decay above holds for every

\[
4<m<2+2\sqrt3.
\]

Thus the energy identity gives

\[
\inf_{{\cal C}_{\mathrm{exact}}}J_6
\ge
\inf_{{\cal C}_{-24}^{\mathrm{aCH}}}P.
\]

For the reverse inequality, take any \(h\in{\cal C}_{-24}^{\mathrm{aCH}}\) and a cutoff \(\chi_R\) equal to one for \(r\le R\) and zero for \(r\ge R+1\). On the end set

\[
h_R=g_{\mathrm{CH}}+\chi_R(h-g_{\mathrm{CH}}),
\]

and retain \(h\) on the compact interior. For large \(R\), \(h_R\) is positive definite, smooth, complete, and exactly CH for \(r\ge R+1\). On the transition annulus,

\[
\operatorname{Ric}_{h_R}+6h_R=O(e^{-\mu R}),
\]

while the annulus has volume \(O(e^{4R})\). Also,

\[
\operatorname{Ric}_{h}+6h=\operatorname{Ric}_h^\circ
=O(e^{-\mu r})
\]

because \(s_h=-24\). Directly from the defining integral of \(J_6\),

\[
J_6(h_R)
=
P(h)+O(e^{(4-2\mu)R}).
\]

Therefore

\[
\inf_{{\cal C}_{\mathrm{exact}}}J_6
\le P(h),
\]

and taking the infimum over \(h\) yields

\[
\boxed{
\inf_{{\cal C}_{\mathrm{exact}}}J_6
=
\inf_{{\cal C}_{-24}^{\mathrm{aCH}}}P
}.
\]

For metrics specifically of the form \(h=u^2g\), the conformal cutoff \(u_R\) gives the same result. The direct residual estimate above also repairs a small inconsistency in the written proof: an error stated as \(O(e^{(4-2m)R})\) cannot simultaneously contain an additional \(O(e^{(4-m)R})\) term. No linear transgression is needed in the truncation step; integrating \(|\operatorname{Ric}+6g|^2\) directly gives the sharper quadratic rate.

## Final mathematical conclusion

The no-sign conformal normalization theorem is correct for the stated marked CH end. The weak corner signs, exhaustion construction, strict positivity, uniqueness, decay interval, derivative estimates, vanishing surface contributions, and both exact energy identities all withstand direct verification. The infimum identity becomes complete once the scalar-normalized asymptotic class is stated in metric \(C^\infty\) terms, or alternatively defined as the image of the conformal normalization map.
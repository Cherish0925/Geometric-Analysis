# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 22,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step22_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step22_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the proposed theorem and proof that every smooth complete four-dimensional metric which is exactly complex hyperbolic outside a compact set admits a unique positive conformal factor u→1 giving scalar curvature -24, without any sign assumption on the original scalar curvature. Check the weak sub/supersolution signs including derivative jumps, exhaustion argument, positivity, uniqueness, decay range 4<m<2+2sqrt(3), derivative estimates, Pfaffian and integration-by-parts boundary terms, exact conformal energy identities, and equality of exact-ended J6 and scalar-normalized P infima. Identify and repair any incorrect implication; provide a direct mathematical memo rather than procedural commentary.

## Integrated Scientific Memo

# Verification memo: conformal normalization on an exact \(\mathbf{CH}^{2}\) end

## Verdict and necessary repairs

For an end isometric, in a fixed marking, to the exterior of a geodesic sphere in normalized \(\mathbf{CH}^{2}\) (or the corresponding finite spherical quotient), the proposed no-sign theorem is valid:

* every smooth complete exact-CH-ended four-metric has a unique positive conformal factor \(u\to1\) producing scalar curvature \(-24\);
* the barriers, exhaustion, positivity, uniqueness, and decay range needed for the energy argument are correct;
* the two conformal energy identities are correct, provided they are derived first on compact truncations;
* the boundary terms vanish because one can choose \(4<m<2+2\sqrt3\).

Two statements require repair.

1. **The normalized comparison class must be defined precisely.**  
   “Decay in item 2” applies to a conformal factor, not intrinsically to an arbitrary metric. One may either:
   * define the normalized class as the conformal-normalization image of the exact-ended class; or
   * define the larger intrinsic class of scalar-\(-24\) metrics converging in \(C^\infty\) to the marked CH metric at a rate \(e^{-\mu r}\), \(\mu>4\), and use direct metric splicing for the reverse infimum inequality.

2. **The truncation estimate is quadratic and uses no Pfaffian transgression.**  
   For the cutoff metric, direct use of
   \[
   J_6(h)=\int|\operatorname{Ric}_h+6h|^2
   \]
   gives \(O(e^{(4-2\mu)R})\). The parenthetical additional \(O(e^{(4-\mu)R})\) “linear transgression” in Step 22 should be deleted.

There are also two threshold distinctions:

* \(m>2\) already makes the final quadratic energy integrals finite;
* \(m>4\) is needed to kill the linear finite-domain boundary/transgression terms against CH sphere area growth \(e^{4r}\).

The theorem does not cover cusp ends merely from the words “complex hyperbolic outside a compact set”; it uses the distance-sphere end with
\[
\Delta r=3\coth r+\tanh r,\qquad \operatorname{Area}(S_r)=O(e^{4r}).
\]

---

## 1. Weak barriers, including the derivative jumps

Set
\[
F(v)=-6\Delta_gv+s_gv+24v^3.
\]
Choose \(R\) in the exact CH region, \(0<a<4\), and \(M\ge1\) such that
\[
s_g+24M^2\ge0
\]
everywhere. This is possible because \(s_g\) is bounded on the compact core and equals \(-24\) on the end.

Define
\[
u_-=
\begin{cases}
0,&r\le R,\\
1-e^{-a(r-R)},&r\ge R,
\end{cases}
\qquad
u_+=
\begin{cases}
M,&r\le R,\\
1+(M-1)e^{-a(r-R)},&r\ge R.
\end{cases}
\]
Then \(0\le u_-\le u_+\), and both tend to \(1\).

On the CH end, with \(t=r-R\) and
\[
H=\Delta r=3\coth r+\tanh r>4,
\]
one has
\[
\Delta(1-e^{-at})=a(H-a)e^{-at}\ge0
\]
and hence
\[
F(u_-)
=-6a(H-a)e^{-at}+24u_-(u_-^2-1)\le0.
\]
Likewise,
\[
\Delta(1+(M-1)e^{-at})
=a(a-H)(M-1)e^{-at}\le0,
\]
and because \(u_+\ge1\),
\[
F(u_+)=-6\Delta u_++24u_+(u_+^2-1)\ge0.
\]
On the core,
\[
F(u_-)=0,\qquad F(u_+)=M(s_g+24M^2)\ge0.
\]

For a continuous piecewise \(C^2\) function, with the normal pointing toward increasing \(r\),
\[
\Delta f=(\Delta f)_{\rm reg}
   +\bigl(\partial_\nu f|_{\rm out}-\partial_\nu f|_{\rm in}\bigr)
     \delta_{\{r=R\}}.
\]
Thus:

* \(u_-\) has derivative jump \(+a\), so the singular part of \(F(u_-)\) is
  \[
  -6a\,\delta_{\{r=R\}}\le0;
  \]
* \(u_+\) has derivative jump \(-a(M-1)\), so the singular part of \(F(u_+)\) is
  \[
  6a(M-1)\,\delta_{\{r=R\}}\ge0.
  \]

The proposed weak sub- and supersolution signs are therefore correct.

---

## 2. Exhaustion, strict positivity, and completeness

On
\[
\Omega_L=\{r<L\}
\]
impose \(u=1\) on \(S_L\). Choose a constant
\[
K>\sup_C(s_g+72M^2)
\]
and rewrite the equation as
\[
(-6\Delta+K)u=(K-s_g)u-24u^3.
\]
The derivative of the right-hand side with respect to \(u\) is
\[
K-s_g-72u^2>0,\qquad 0\le u\le M.
\]
The Dirichlet inverse of \(-6\Delta+K\) is order preserving, so standard monotone iteration between the weak barriers produces a smooth solution \(u_L\) with
\[
u_-\le u_L\le u_+,\qquad u_L|_{S_L}=1.
\]
The choice of \(K\) is independent of \(L\).

The uniform \(C^0\) bound and
\[
\Delta u_L=\frac{s_gu_L+24u_L^3}{6}
\]
give uniform local elliptic estimates. A diagonal subsequence converges smoothly on compact subsets to a global solution \(u\) satisfying the same barriers. Hence \(u\to1\) uniformly on the end.

Since \(u\ge u_->0\) for \(r>R\), the limit is not zero. It obeys
\[
-6\Delta u+(s_g+24u^2)u=0.
\]
The coefficient is locally bounded. Equivalently, writing
\[
c=s_g+24u^2=c^+-c^-,
\]
one has
\[
-6\Delta u+c^+u=c^-u\ge0.
\]
The strong maximum principle for nonnegative supersolutions implies that an interior zero would force \(u\equiv0\), impossible because \(u>0\) on the end. Thus
\[
u>0\quad\text{everywhere}.
\]

Moreover, \(u\to1\) and positivity on the compact core imply
\[
0<c_0\le u\le M.
\]
Therefore \(u^2g\) is uniformly equivalent to \(g\) and is complete.

This proves that no sign condition on \(s_g\) is needed. Positivity of the conformal Laplacian is not being assumed: the compact-exhaustion problem is solved after a harmless positive shift, while the global lower barrier may vanish on the core.

---

## 3. Uniqueness

Let \(u_i>0\), \(u_i\to1\), and suppose \(u_i^2g\) both have scalar curvature \(-24\). Set
\[
g_2=u_2^2g,\qquad w=\frac{u_1}{u_2}.
\]
Then
\[
-6\Delta_{g_2}w-24w+24w^3=0,
\]
or
\[
-6\Delta_{g_2}w+24w(w^2-1)=0.
\]

Because \(w\to1\), a supremum above \(1\), if present, is attained in a compact set. At such a maximum,
\[
\Delta w\le0,
\]
so
\[
-6\Delta w\ge0,\qquad 24w(w^2-1)>0,
\]
contradicting the equation. Similarly, an infimum in \((0,1)\) is attained and gives
\[
-6\Delta w\le0,\qquad 24w(w^2-1)<0,
\]
again a contradiction. Hence \(w\equiv1\).

In particular:

* the global solution does not depend on the choices \(a,M\) or exhaustion subsequence;
* rerunning the barrier construction for different \(a<4\) gives estimates for the same solution;
* every end-preserving isometry fixes \(u\), so symmetry classes are preserved.

---

## 4. Decay and derivatives

Put \(v=u-1\). On the exact CH end,
\[
-6\Delta v+48v+72v^2+24v^3=0,
\]
equivalently
\[
(-6\Delta+q)v=0,\qquad
q=48+72v+24v^2=24u(u+1)>0.
\]

For \(\phi_m=e^{-mr}\),
\[
(-6\Delta+q)\phi_m
=
\bigl[-6m^2+6mH+q\bigr]\phi_m.
\]
As \(r\to\infty\), the coefficient tends to
\[
6(-m^2+4m+8).
\]
It is positive exactly when
\[
0<m<m_*:=2+2\sqrt3.
\]
Thus, for fixed \(m<m_*\), \(\phi_m\) is a strict supersolution sufficiently far out.

Choose \(C\) so that \(C\phi_m\ge|v|\) on an inner sphere. Since
\[
(-6\Delta+q)(C\phi_m\mp v)>0
\]
and both functions tend to zero at infinity, the maximum principle on the exterior region gives
\[
|v|\le Ce^{-mr}.
\]
Therefore
\[
|u-1|=O(e^{-mr})
\qquad\text{for every }0<m<2+2\sqrt3.
\]

This includes the interval needed later:
\[
4<m<2+2\sqrt3.
\]

The characteristic equation is
\[
m^2-4m-8=0.
\]
The expression \(m^2+4m-8=0\) in Step 21 is a typo; it does not have \(2+2\sqrt3\) as a root.

On unit CH balls, the geometry is uniformly controlled and
\[
\Delta v=8v+12v^2+4v^3.
\]
Interior \(W^{2,p}\) or Schauder estimates give the same exponential rate for \(\nabla v\) and \(\nabla^2v\); differentiation and iteration yield
\[
|\nabla^k(u-1)|=O(e^{-mr})
\]
for every fixed \(k\) and every \(m<m_*\).

The endpoint \(m=m_*\) can also be obtained. Indeed,
\[
6(-m_*^2+m_*H+8)+(q-48)
=6m_*(H-4)+(q-48).
\]
Here
\[
H-4=4e^{-2r}+O(e^{-4r}),
\]
while an initial barrier with any \(a\in(2,4)\) gives \(q-48=O(e^{-ar})\). Hence the coefficient is eventually positive. The stated open interval is nevertheless sufficient and avoids needing this refinement.

---

## 5. Pfaffian and integration-by-parts boundary terms

The comparison must first be performed on
\[
C_R=\{r\le R\},
\]
because \(\int |W|^2\) and \(\int s^2\) generally diverge separately on the infinite CH end.

For \(\widehat g=u^2g\), set
\[
A=\frac{\Delta u}{u}.
\]
The scalar-curvature law gives
\[
s_{\widehat g}^2\,dV_{\widehat g}
=(s_g-6A)^2\,dV_g.
\]
Since \(|W|^2dV\) is conformally invariant in dimension four, Chern–Gauss–Bonnet on \(C_R\) yields
\[
P(\widehat g;C_R)-P(g;C_R)
=
\int_{C_R}\bigl(-s_gA+3A^2\bigr)\,dV_g+\tau_R,
\]
where \(\tau_R\) is the boundary Pfaffian transgression.

The connection difference is
\[
\nabla^{\widehat g}-\nabla^g
=O(|\nabla\log u|)=O(e^{-mR}),
\]
and all required background curvature and hypersurface geometry are bounded. More explicitly, a Chern–Simons transgression has terms schematically of the form
\[
A_{\rm conn}\wedge R_t
\]
and cubic connection-difference terms; \(R_t\) remains bounded because first and second derivatives of \(u-1\) have the same decay. Hence
\[
|\tau_R|=O(e^{(4-m)R}),
\]
using
\[
\operatorname{Area}(S_R)=O(e^{4R}).
\]
Thus \(\tau_R\to0\) for \(m>4\).

The scalar equation gives
\[
s_g=6A-24u^2.
\]
Substitution produces a term \(24\int u\Delta u\). On \(C_R\),
\[
\int_{C_R}u\Delta u
=-\int_{C_R}|\nabla u|^2
+\int_{S_R}u\,\partial_\nu u.
\]
Since
\[
u\,\partial_\nu u=O(e^{-mR}),
\]
the boundary integral is also
\[
O(e^{(4-m)R})\to0
\]
for \(m>4\).

Thus the warning in Step 22 is correct: these finite-domain fluxes are linear in \(u-1\), not all quadratic.

---

## 6. Exact conformal energy identities

Taking \(R\to\infty\) gives
\[
\begin{aligned}
P(\widehat g)-P(g)
&=\int_C\left[-s_gA+3A^2\right]dV_g\\
&=\int_C\left[-(6A-24u^2)A+3A^2\right]dV_g\\
&=\int_C\left[-3A^2+24u\Delta u\right]dV_g.
\end{aligned}
\]
After integration by parts,
\[
\boxed{
P(g)-P(\widehat g)
=
24\int_C|\nabla u|^2\,dV_g
+
3\int_C\left(\frac{\Delta u}{u}\right)^2dV_g.
}
\]

Because \(s_{\widehat g}=-24\),
\[
J_6(\widehat g)=P(\widehat g),
\]
and by definition
\[
J_6(g)=P(g)+\frac14\int_C(s_g+24)^2dV_g.
\]
Hence
\[
\boxed{
J_6(g)-J_6(\widehat g)
=
\int_C\left[
24|\nabla u|^2
+3\left(\frac{\Delta u}{u}\right)^2
+\frac14(s_g+24)^2
\right]dV_g.
}
\]

The final integrals are finite already for \(m>2\): the first two integrands are \(O(e^{-2mr})\), while CH volume grows as \(e^{4r}\); furthermore \(s_g+24\) is compactly supported for an exact-ended input. The stronger \(m>4\) is required only in the finite-domain proof to remove the linear fluxes.

Equality in the first identity implies \(\nabla u=0\), and the end normalization then gives \(u\equiv1\). On a closed manifold, absent the end normalization, constant conformal rescalings remain possible. Equality in the \(J_6\) identity additionally gives
\[
s_g\equiv-24.
\]

A useful consistency check is
\[
6\frac{\Delta u}{u}
=s_g+24u^2
=(s_g+24)+24(u^2-1),
\]
so
\[
3\left(\frac{\Delta u}{u}\right)^2
=
\frac{\bigl[(s_g+24)+24(u^2-1)\bigr]^2}{12}.
\]

---

## 7. Precise equality of the infima

### Intrinsic formulation

Let \(g_{\mathrm{CH}}\) denote the marked model metric and define
\[
\mathcal C_{-24}^{\mathrm{aCH}}
=
\left\{
h:
s_h=-24,\quad
|\nabla_{\mathrm{CH}}^k(h-g_{\mathrm{CH}})|
=O(e^{-\mu r})\ \text{for every }k,
\ \text{for some }\mu>4
\right\}.
\]
Every normalized metric \(\widehat g=u^2g\) arising from an exact-ended \(g\) lies in this class. The energy identity therefore gives
\[
\inf_{g\in\mathcal C_{\mathrm{exact}}}J_6(g)
\ge
\inf_{h\in\mathcal C_{-24}^{\mathrm{aCH}}}P(h).
\]

Conversely, take \(h\in\mathcal C_{-24}^{\mathrm{aCH}}\). Let \(\chi_R\) equal \(1\) for \(r\le R\) and \(0\) for \(r\ge R+1\), and define on the end
\[
h_R=g_{\mathrm{CH}}+\chi_R(h-g_{\mathrm{CH}}),
\]
retaining \(h\) on the compact interior. For large \(R\), this is smooth, positive definite, complete, and exactly CH outside \(r\ge R+1\).

Because the cutoff and its derivatives are uniformly bounded,
\[
\operatorname{Ric}_{h_R}+6h_R=O(e^{-\mu R})
\]
on the transition annulus. Since \(s_h=-24\),
\[
\operatorname{Ric}_h+6h=\operatorname{Ric}_h^\circ=O(e^{-\mu r})
\]
on the discarded tail. Consequently,
\[
J_6(h_R)
=
P(h)+O(e^{(4-2\mu)R}).
\]
No Pfaffian transgression is involved in this estimate: it follows directly from the squared Einstein residual.

Thus
\[
\inf_{\mathcal C_{\mathrm{exact}}}J_6
\le P(h).
\]
Taking the infimum over \(h\) proves
\[
\boxed{
\inf_{g\in\mathcal C_{\mathrm{exact}}}J_6(g)
=
\inf_{h\in\mathcal C_{-24}^{\mathrm{aCH}}}P(h).
}
\]

### Conformal-image formulation

Alternatively, define \(\mathcal C_{-24}\) to consist of scalar-\(-24\) metrics \(h=w^2g'\), where \(g'\) is exact CH-ended, \(w\to1\), and \(w-1\) has sufficient exponential \(C^\infty\) decay. Then the original conformal cutoff
\[
w_R=1+\chi_R(w-1),\qquad g_R=w_R^2g'
\]
is valid. Moreover
\[
h=(w/w_R)^2g_R,
\]
and uniqueness identifies \(h\) as the normalization of \(g_R\). Again,
\[
J_6(g_R)=P(h)+O(e^{(4-2\mu)R}).
\]

The intrinsic class is broader and geometrically cleaner; the conformal-image class is the minimal repair of the wording in Step 22.

---

## Corrected theorem

For every smooth complete connected four-metric whose marked end is exactly the exterior distance-sphere end of normalized \(\mathbf{CH}^{2}\), there is a unique smooth positive \(u\to1\) such that
\[
-6\Delta_gu+s_gu+24u^3=0.
\]
The metric \(\widehat g=u^2g\) is complete and has \(s_{\widehat g}=-24\). For every
\[
4<m<2+2\sqrt3
\]
and every fixed \(k\),
\[
|\nabla^k(u-1)|=O(e^{-mr}).
\]
The two displayed energy identities hold exactly, with equality only as described above. Finally, after defining the scalar-normalized asymptotic class intrinsically or as the conformal-normalization image,
\[
\inf_{\mathcal C_{\mathrm{exact}}}J_6
=
\inf_{\mathcal C_{-24}}P.
\]

This is an infimum reduction only: it proves neither attainment nor a lower bound for the resulting \(P\)-problem, and it does not automatically extend to merely asymptotically CH inputs without explicit decay assumptions on the metric and scalar forcing.
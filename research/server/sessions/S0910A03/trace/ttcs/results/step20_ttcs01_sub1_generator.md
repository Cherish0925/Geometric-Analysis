# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md",
    "Sessions/S0910A01/workspace/notes/step19_whitney_tensor_estimate.md",
    "Sessions/S0910A03/workspace/scripts/verify_step20_weighted_moment_hierarchy.py",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Develop the strongest viable local weighted parabolic iteration suggested by Wang for a=χ² under the normalized cutoff flow ∂tg=-2a(Ric+g), in dimension four. Focus on a self-contained theorem at the level actually supported by H_q=∫η²a^{q-2}F^q and J_m=∫η²a^{m-2}|E|^m. Seek an exact recurrence whose output norms feed the next stage, with nested localization cutoffs and finite-neighbor terms. Explore whether the curvature hierarchy can produce weighted cubic potential and whether the defect hierarchy can produce |aE| and χ∇(aE) estimates from initial |E|≤δ, while preserving homogeneity at E=0. Explicitly analyze where normalization, derivatives of a, evolving metric/measure, and curvature derivative terms enter. Compare the direct weighted hierarchy against Whitney-ball localization and identify a decisive calculation or counterexample that would choose between them. The result should be a technical construction memo, not a generic roadmap or a conclusion about the full Yau problem.

## Output

# Technical construction memo: weighted Wang iteration for \(a=\chi^2\) under  
\[
\partial_t g=-2a(\operatorname{Ric}+g),\qquad E=\operatorname{Ric}+g,\qquad U=aE
\]
in dimension four

## 1. Local finite-neighbor formulation

Work on a finite-neighbor family of patches \(U_\alpha\) with fixed enlarged patches \(\widetilde U_\alpha\). On the time interval under discussion assume the evolving metrics satisfy a relative Sobolev inequality
\[
\|\phi\|_{L^4(U_\alpha,g(t))}^2
\le A_\alpha^2\left(\|\nabla\phi\|_{L^2(\widetilde U_\alpha,g(t))}^2
+r^{-2}\|\phi\|_{L^2(\widetilde U_\alpha,g(t))}^2\right),
\]
and the finite-neighbor count is \(N\). Let nested cutoffs \(\eta_{\alpha,k}\) satisfy
\[
\eta_{\alpha,k+1}\equiv1\text{ on the next smaller patch},\qquad
|\nabla\eta_{\alpha,k}| \le C2^k r^{-1}.
\]
The structural cutoff condition is
\[
0\le a\le1,\qquad \frac{|da|^2}{a}=4|d\chi|^2\le C r^{-2}.
\]
No pointwise \(\nabla^2 a/a\) estimate should appear in the zero-order iteration; every Hessian term has to be integrated by parts until only \(|da|^2/a\) and \(|d\eta|^2\) occur.

For curvature use \(F\sim |\operatorname{Rm}|\), with a harmless regularization \(F_\varepsilon=(\varepsilon^2+|\operatorname{Rm}|^2)^{1/2}\) during differentiations. For the defect let \(G=|E|\). Define
\[
H_{q,\alpha,k}(t)=\int \eta_{\alpha,k}^2 a^{q-2}F^q\,d\mu_t,
\]
\[
J_{m,\alpha,k}(t)=\int \eta_{\alpha,k}^2 a^{m-2}G^m\,d\mu_t
=\int \eta_{\alpha,k}^2 a^{-2}|U|^m\,d\mu_t.
\]
The Sobolev variables are
\[
V^R_q=\eta\,a^{(q-1)/2}F^{q/2},\qquad
V^E_m=\eta\,a^{(m-1)/2}G^{m/2}
      =\eta\,a^{-1/2}|U|^{m/2}.
\]
The algebraic identities driving the construction are exact:
\[
(V^R_q)^4=\eta^4 a^{2q-2}F^{2q}\quad\leadsto\quad H_{2q},
\]
\[
F(V^R_q)^2=\eta^2a^{q-1}F^{q+1}=H_{q+1},
\]
and similarly
\[
(V^E_m)^4\leadsto J_{2m},\qquad
F(V^E_m)^2=\eta^2a^{m-1}FG^m,
\qquad
G(V^E_m)^2=\eta^2a^{m-1}G^{m+1}.
\]

The weighted cubic identity is the key one:
\[
F(V_m^E)^2
=(aF^3)^{1/3}\,\bigl(a^{-1/3}(V_m^E)^2\bigr),
\]
and
\[
\left(a^{-1/3}(V_m^E)^2\right)^{3/2}
=\eta^3 a^{\frac32m-2}G^{\frac32m},
\]
which is exactly the \(J_{3m/2}\) monomial. Thus
\[
\int F(V_m^E)^2
\le H_3^{1/3}J_{3m/2}^{2/3}.
\]
Likewise,
\[
\int G(V_m^E)^2
\le J_3^{1/3}J_{3m/2}^{2/3}.
\]
The curvature hierarchy has the same monomial closure:
\[
H_{q+1}\le H_3^{1/3}H_{3q/2}^{2/3}.
\]

## 2. Equations and homogeneity at \(E=0\)

The normalized cutoff flow should always be organized through
\[
h:=\partial_tg=-2aE.
\]
If one splits \(h=-2a\operatorname{Ric}-2ag\), the \(-2ag\) part produces apparent terms
\[
(\nabla^2a)\owedge g+a\,\operatorname{Rm},
\]
which are not homogeneous in \(E\). Combining the two pieces before estimating gives the homogeneous variation form
\[
\partial_t\operatorname{Rm}
=
\nabla^2(aE)+\operatorname{Rm}*(aE).
\]
For parabolic smoothing one rewrites this schematically as
\[
\partial_t\operatorname{Rm}
=
a\bigl(\Delta\operatorname{Rm}+\operatorname{Rm}*\operatorname{Rm}
+\operatorname{Rm}\bigr)
+\nabla a*\nabla E+\nabla^2a*E
+\nabla a*\operatorname{Rm}*E+a\operatorname{Rm}*E.
\]
The first line is Wang’s parabolic curvature operator; the second line is homogeneous in \(E\). The \(\nabla a*\nabla E+\nabla^2a*E\) combination is integrated by parts in the curvature energy, leaving only first-derivative cutoff quantities and \(E\)-weighted zeroth-order terms.

For the defect the clean variable is \(U=aE\). Its equation is
\[
\partial_tU=a(\Delta_LU-2U)+\mathcal B_a(U),
\]
where \(\mathcal B_a(U)\) is linear in \(U,\nabla U\) and has coefficients built from
\[
\nabla a,\qquad \nabla^2a,\qquad \frac{da\otimes da}{a}=4\,d\chi\otimes d\chi.
\]
Testing the \(U\)-equation against
\[
\eta^2a^{-2}|U|^{m-2}U
\]
gives the \(J_m\) hierarchy. All terms vanish when \(U=0\), so \(E=0\) is preserved exactly at the energy level.

The evolving measure satisfies
\[
\partial_t d\mu_t=-\operatorname{tr}(aE)\,d\mu_t=-\operatorname{tr}U\,d\mu_t.
\]
Thus curvature powers acquire terms of the form
\[
\int G(V^R_q)^2,
\]
and defect powers acquire
\[
\int G(V^E_m)^2.
\]
These are handled by the same \(J_3\)-potential algebra above.

## 3. Local weighted energy inequalities

After integrating \(\nabla^2a\)-terms by parts and using
\[
\frac{|da|^2}{a}\le Cr^{-2},
\]
one obtains, on each patch \(U_\alpha\), the schematic curvature inequality
\[
\frac{d}{dt}H_{q,\alpha,k}
+c\,D^R_{q,\alpha,k}
\le
Cq^2\Theta_k\sum_{\beta\sim\alpha}H_{q,\beta,k-1}
+Cq\int F(V^R_q)^2
+Cq\int G(V^R_q)^2,
\]
where
\[
D^R_{q,\alpha,k}
\sim
\int\left|\nabla\bigl(\eta_{\alpha,k}a^{(q-1)/2}F^{q/2}\bigr)\right|^2,
\]
and
\[
\Theta_k=4^k r^{-2}+1.
\]
The curvature and defect potential terms reduce to
\[
\int F(V^R_q)^2
\le
\varepsilon D^R_{q,\alpha,k}
+C_\varepsilon A_\alpha^4
\left(\sum_{\beta\sim\alpha}H_{3,\beta,k-1}\right)
\sum_{\beta\sim\alpha}H_{q,\beta,k-1},
\]
\[
\int G(V^R_q)^2
\le
\varepsilon D^R_{q,\alpha,k}
+C_\varepsilon A_\alpha^4
\left(\sum_{\beta\sim\alpha}J_{3,\beta,k-1}\right)
\sum_{\beta\sim\alpha}H_{q,\beta,k-1}.
\]

For the defect hierarchy,
\[
\frac{d}{dt}J_{m,\alpha,k}
+c\,D^E_{m,\alpha,k}
\le
Cm^2\Theta_k\sum_{\beta\sim\alpha}J_{m,\beta,k-1}
+Cm\int F(V^E_m)^2
+Cm\int G(V^E_m)^2,
\]
where
\[
D^E_{m,\alpha,k}
\sim
\int\left|\nabla\bigl(\eta_{\alpha,k}a^{-1/2}|U|^{m/2}\bigr)\right|^2.
\]
The potential reductions are
\[
\int F(V^E_m)^2
\le
\varepsilon D^E_{m,\alpha,k}
+C_\varepsilon A_\alpha^4
\left(\sum_{\beta\sim\alpha}H_{3,\beta,k-1}\right)
\sum_{\beta\sim\alpha}J_{m,\beta,k-1},
\]
\[
\int G(V^E_m)^2
\le
\varepsilon D^E_{m,\alpha,k}
+C_\varepsilon A_\alpha^4
\left(\sum_{\beta\sim\alpha}J_{3,\beta,k-1}\right)
\sum_{\beta\sim\alpha}J_{m,\beta,k-1}.
\]

Choosing \(\varepsilon\sim q^{-1}\) or \(\varepsilon\sim m^{-1}\) yields polynomial factors \(q^3,m^3\), harmless in the iteration.

Thus both hierarchies reduce to the model inequality
\[
\boxed{
\frac{d}{dt}M_{s,\alpha,k}
+cD_{s,\alpha,k}
\le
Cs^3\Bigl(\Theta_k+\mathcal P_{\alpha,k}(t)\Bigr)
\sum_{\beta\sim\alpha}M_{s,\beta,k-1},
}
\]
with \(M_s=H_s\) or \(J_s\), and
\[
\mathcal P_{\alpha,k}(t)
=
A_\alpha^4
\sum_{\beta\sim\alpha}
\bigl(H_{3,\beta,k-1}(t)+J_{3,\beta,k-1}(t)\bigr).
\]

## 4. Curvature cubic potential from \(H_2\)

Let
\[
\beta_\alpha
=
A_\alpha^2
\left(\sum_{\beta\sim\alpha}\int_{\widetilde U_\beta}F^2\,d\mu_t\right)^{1/2}.
\]
For \(q=2\),
\[
H_3=\int aF^3=\int F(\chi F)^2.
\]
By Sobolev,
\[
H_3
\le
\|F\|_2\,\|\chi\eta F\|_4^2
\le
\beta_\alpha
\left(D^R_{2,\alpha}+r^{-2}\sum_{\beta\sim\alpha}H_{2,\beta}\right).
\]
If \(\beta_\alpha\) is small enough for the fixed \(q=2\) energy, the \(H_2\) energy persists:
\[
\sup_{0\le t\le T}\sum_{\beta\sim\alpha}H_{2,\beta}(t)
+
\int_0^T\sum_{\beta\sim\alpha}D^R_{2,\beta}(t)\,dt
\le
C\sum_{\beta\sim\alpha}H_{2,\beta}(0).
\]
Consequently,
\[
\int_0^T H_{3,\alpha}(t)\,dt
\le
C\beta_\alpha
\sum_{\beta\sim\alpha}H_{2,\beta}(0).
\]
Running the fixed \(q=3\) energy with a time cutoff gives the pointwise-in-time cubic potential
\[
\boxed{
A_\alpha^4H_{3,\alpha}(t)
\le
C_N\left(\frac{\beta_\alpha^3}{t}+r^{-2}\beta_\alpha^2\right),
\qquad 0<t\le T\le cr^2.
}
\]
This is the weighted analogue of Wang’s \(L^3\) curvature potential. It is the quantity needed in Li-type high-exponent iteration; repeated absorption by \(L^2\) curvature smallness is avoided.

For the defect self-potential, if initially \(|E|\le\delta\), then
\[
J_{3,\alpha}(0)\le \delta^3\int_{\widetilde U_\alpha}a\,d\mu_0.
\]
The fixed \(m=3\) defect energy gives
\[
\boxed{
A_\alpha^4J_{3,\alpha}(t)\le C_N\delta^3
}
\]
on \(0\le t\le T\), after the same finite-neighbor Sobolev cancellation.

## 5. Exact recurrence \(s\mapsto \frac32s\)

Let
\[
I_k=[\tau_k,T],\qquad
\tau_k=T(1-2^{-k-1}),
\]
so \(I_0=[T/2,T]\) and \(I_k\searrow\{T\}\). Let
\[
X_{s,\alpha,k}:=\sup_{t\in I_k}M_{s,\alpha,k}(t).
\]
On \(I_k\), the time cutoff contributes \(C2^kT^{-1}\), and the spatial cutoff contributes \(C4^kr^{-2}\). With
\[
\Lambda_k
=
C4^k(T^{-1}+r^{-2})
+
C\sup_{t\in I_k}\mathcal P_{\alpha,k}(t),
\]
the energy inequality gives
\[
\sup_{I_{k+1}}M_{s,\alpha,k+1}
+
\int_{I_{k+1}}D_{s,\alpha,k+1}
\le
Cs^3\Lambda_k |I_k|
\sum_{\beta\sim\alpha}X_{s,\beta,k}.
\]

Sobolev plus exact interpolation gives
\[
M_{3s/2,\alpha,k+1}
\le
M_{s,\alpha,k+1}^{1/2}
M_{2s,\alpha,k+1}^{1/2},
\]
and
\[
M_{2s,\alpha,k+1}^{1/2}
\le
CA_\alpha^2
\left(D_{s,\alpha,k+1}+4^kr^{-2}
\sum_{\beta\sim\alpha}M_{s,\beta,k}\right).
\]
Applying the energy inequality once more to convert the spacetime \(M_{3s/2}\)-control into a supremum gives the recurrence
\[
\boxed{
X_{\frac32s,\alpha,k+2}^{\,1/(\frac32s)}
\le
\left(
C_NA_\alpha^2s^6\Lambda_k^2|I_k|
\right)^{1/(\frac32s)}
\left(
\sum_{\beta\in\mathcal N_2(\alpha)}X_{s,\beta,k}
\right)^{1/s}.
}
\]
Equivalently,
\[
\boxed{
X_{\frac32s,\alpha,k+2}^{\,2/(3s)}
\le
\left(
C_NA_\alpha^2s^6\Lambda_k^2|I_k|
\right)^{2/(3s)}
\left(
\sum_{\beta\in\mathcal N_2(\alpha)}X_{s,\beta,k}
\right)^{1/s}.
}
\]

Since
\[
s_j=s_0\left(\frac32\right)^j,\qquad
\sum_{j\ge0}\frac1{s_{j+1}}=\frac2{s_0},
\]
and, for \(T\le cr^2\),
\[
\Lambda_j^2|I_j|
\le
C8^j(T^{-1}+r^{-2})
\]
once
\[
A_\alpha^4H_3(t)\le C\beta_\alpha^3t^{-1},\qquad
A_\alpha^4J_3(t)\le C\delta^3,
\]
the infinite product yields
\[
\boxed{
\|aZ\|_{L^\infty(U_{\alpha,\infty}\times\{T\})}
\le
C_{s_0,N}
A_\alpha^{4/s_0}
(T^{-1}+r^{-2})^{2/s_0}
\left(
\sum_{\beta\in\mathcal N_*(\alpha)}
X_{s_0,\beta,0}
\right)^{1/s_0},
}
\]
where \(Z=F\) for curvature and \(Z=G=|E|\) for the defect. The finite-neighbor factor is \(N^{C/s_0}\), because all cutoffs are supported in one fixed enlarged patch family.

## 6. Curvature output

Use \(s_0=3\) and the cubic potential at time \(T/2\):
\[
X^R_{3,\alpha,0}
\le
C_N\frac{\beta_\alpha^3}{A_\alpha^4T}
+
C_Nr^{-2}\frac{\beta_\alpha^2}{A_\alpha^4}.
\]
The recurrence gives
\[
\|aF\|_{\infty,U_{\alpha,\infty}}(T)
\le
C_NA_\alpha^{4/3}(T^{-1}+r^{-2})^{2/3}
\left(\frac{\beta_\alpha^3}{A_\alpha^4T}\right)^{1/3}
+
\text{lower scale terms}.
\]
For \(T\le cr^2\),
\[
\boxed{
\|a\,\operatorname{Rm}\|_{\infty,U_{\alpha,\infty}}(T)
\le
C_N\frac{\beta_\alpha}{T}
+
C_N\beta_\alpha r^{-2}.
}
\]
This is the local weighted Wang estimate in the finite-neighbor formulation.

The essential feature is that the high-exponent iteration uses the time-dependent potential \(A^4H_3(t)\sim \beta^3/t\). It does not require absorbing \(qH_{q+1}\) by \(L^2\)-smallness at every exponent.

## 7. Defect output from \(|E(0)|\le\delta\)

Choose one fixed \(p>2\), and in applications requiring connection drift take \(p>4\), e.g. \(p=6\).

First propagate the fixed \(J_p\) moment from \(t=0\) to \(T/2\) using fixed-exponent critical absorption:
\[
\sup_{0\le t\le T/2}J_{p,\alpha}(t)
\le
C_{p,N}J_{p,\alpha}(0).
\]
With \(|E(0)|\le\delta\),
\[
J_{p,\alpha}(0)
\le
\delta^p\int_{\widetilde U_\alpha}a^{p-2}\,d\mu_0
\le
\delta^p\,\operatorname{Vol}(\widetilde U_\alpha).
\]
Now apply the recurrence with \(s_0=p\), using the curvature potential already produced:
\[
\boxed{
\|aE\|_{\infty,U_{\alpha,\infty}}(T)
\le
C_{p,N}
A_\alpha^{4/p}
(T^{-1}+r^{-2})^{2/p}
\left(
\sum_{\beta\in\mathcal N_*(\alpha)}J_{p,\beta}(T/2)
\right)^{1/p}.
}
\]
The relative Sobolev volume scaling in dimension four is
\[
A_\alpha\lesssim r\,V_\alpha^{-1/4}.
\]
Hence
\[
A_\alpha^{4/p}J_{p,\alpha}(0)^{1/p}
\le
C\delta\,r^{4/p},
\]
and therefore
\[
\boxed{
\|aE\|_{\infty,U_{\alpha,\infty}}(T)
\le
C_{p,N}\delta
\left(1+\frac{r^2}{T}\right)^{2/p}.
}
\]
For \(0<T\le cr^2\),
\[
\boxed{
\|aE\|_{\infty}(T)
\le
C_{p,N}\delta\left(\frac{r^2}{T}\right)^{2/p}.
}
\]
This is the desired \(M_p\)-type estimate. Its time integral is finite exactly for \(p>2\):
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le
C_{p,N}\delta\,r^2\,\theta^{1-2/p}.
\]

## 8. What the \(J_m\) hierarchy gives for \(\chi\nabla(aE)\)

The \(J_m\) energy directly controls a Caccioppoli quantity for \(U=aE\):
\[
D^E_m
\sim
\int \left|\nabla\bigl(\eta a^{-1/2}|U|^{m/2}\bigr)\right|^2.
\]
Since
\[
\nabla U=a\nabla E+da\otimes E,
\]
one has
\[
|\chi\nabla U|^2|U|^{m-2}
\le
C\left(
a^{-1}|U|^{m-2}|\nabla U|^2
+
\frac{|da|^2}{a}a^{-2}|U|^m
\right).
\]
Therefore
\[
\boxed{
\int_{I_{k+1}}\int
\eta^2|\chi\nabla(aE)|^2|aE|^{m-2}
\le
C\int_{I_{k+1}}D^E_m
+
Cr^{-2}\int_{I_{k+1}}J_m.
}
\]
This is the gradient information genuinely contained in the zero-order \(J_m\) hierarchy.

A pointwise Bernstein estimate
\[
|\chi\nabla(aE)|(T)
\lesssim
\delta\,T^{-1/2}\left(\frac{r^2}{T}\right)^{2/p}
\]
requires differentiating the \(U\)-equation. For \(W=\chi\nabla U\), the schematic differentiated equation contains
\[
(\partial_t-a\Delta)W
=
a\operatorname{Rm}*W
+\frac{da}{\sqrt a}*\nabla W
+\left(\nabla^2a+\frac{da\otimes da}{a}\right)*W
+\chi a(\nabla\operatorname{Rm})*U
+\nabla^3a*U
+\text{quadratic }U,W\text{ terms}.
\]
The term
\[
\chi a(\nabla\operatorname{Rm})*U
\]
is not controlled by \(H_3\), \(J_m\), or \(|a\operatorname{Rm}|\le C/t\) alone. It can sometimes be integrated by parts in an \(L^2\) derivative hierarchy, but a pointwise Bernstein argument needs either a weighted curvature-derivative estimate, or a parabolic gradient theorem in a coordinate system where the coefficients have enough regularity.

Thus the zero-order weighted hierarchy supplies \(|aE|\) and the Caccioppoli form of \(\chi\nabla(aE)\); it does not by itself supply the pointwise \(\chi\nabla(aE)\) estimate needed for connection drift. The missing analytic object is a weighted derivative theorem for \(U\) coupled to a weighted derivative theorem for curvature.

## 9. Direct weighted hierarchy versus Whitney-ball localization

The direct hierarchy and Whitney localization encode the same scaling at zero order.

On a collar where \(\chi\sim\lambda\), \(a\sim\lambda^2\), and the Whitney radius is
\[
\ell\sim r\lambda.
\]
The weighted moment is
\[
H_q\sim \lambda^{2q-4}\int F^q
=\lambda^{-4}\int (aF)^q.
\]
The factor \(\lambda^{-4}\) is exactly the four-dimensional cost of using the singular measure \(a^{-2}d\mu\). In Whitney variables the Sobolev coefficient is
\[
A_\ell^4\sim \frac{\ell^4}{\operatorname{Vol}(B_\ell)}.
\]
The energy transfer estimate
\[
\ell^4\fint_{B_\ell}F^2\le Cr^4K_0
\]
contains the compensating factor \((r/\ell)^4=\lambda^{-4}\). Hence the direct weighted \(a^{-2}\)-measure and the Whitney scale \(\ell=r\chi\) carry the same four-dimensional power.

A decisive calculation concerns Hessian terms. In the model collar \(a=s^2/r^2\),
\[
\frac{|da|^2}{a}=\frac{4}{r^2}
\]
is harmless, while
\[
\frac{|\nabla^2a|}{a}\sim \frac1{s^2}
\]
is singular at the cutoff edge. A direct derivation that leaves \(\nabla^2a/a\) cannot represent Wang’s mechanism. The correct direct computation integrates Hessian terms by parts until only \(|da|^2/a\) remains. Whitney localization expresses the same fact differently:
\[
\frac{|\nabla^2a|}{a_0}\sim \frac1{r^2\lambda^2}=\frac1{\ell^2},
\]
which is precisely the local parabolic scale on the Whitney ball.

For zero-order curvature and defect smoothing, the direct hierarchy is more compact: it gives one recurrence
\[
s\mapsto \frac32s
\]
with \(H_3\) and \(J_3\) as potentials. Whitney localization is scientifically sharper for derivative estimates: on \(B_\ell\), \(a\) is uniformly comparable to \(a_0\), the effective time is \(a_0t\), and derivative estimates reduce to nondegenerate parabolic estimates at scale \(\ell\). The direct derivative equation keeps the term \(\chi a\nabla\operatorname{Rm}*U\), while the Whitney formulation points to the needed nondegenerate curvature-derivative input.

## 10. Resulting viable theorem

The strongest local statement supported by the \(H_q,J_m\) hierarchy is:

**Weighted Wang moment theorem in dimension four.**  
Under the finite-neighbor Sobolev system above, assume the fixed-exponent \(H_2,H_3,J_3,J_p\) energies persist on \(0\le t\le T\le cr^2\), with
\[
A_\alpha^2\|\operatorname{Rm}\|_{L^2(\widetilde U_\alpha)}\le \beta_\alpha,
\qquad
|E(0)|\le\delta,
\]
and \(p>2\). Then:

1. The curvature hierarchy produces the weighted cubic potential
   \[
   A_\alpha^4H_{3,\alpha}(t)
   \le
   C_N\left(\frac{\beta_\alpha^3}{t}+r^{-2}\beta_\alpha^2\right).
   \]

2. The exact high-exponent recurrence is
   \[
   s_{j+1}=\frac32s_j,
   \]
   with
   \[
   X_{s_{j+1},\alpha}^{1/s_{j+1}}
   \le
   \left(
   C_NA_\alpha^2s_j^6\Lambda_j^2|I_j|
   \right)^{1/s_{j+1}}
   \left(
   \sum_{\beta\in\mathcal N_2(\alpha)}
   X_{s_j,\beta}
   \right)^{1/s_j}.
   \]

3. With \(s_0=3\), this gives
   \[
   |a\,\operatorname{Rm}|(T)\le C_N\beta_\alpha T^{-1}+C_N\beta_\alpha r^{-2}.
   \]

4. With \(s_0=p\), this gives
   \[
   |aE|(T)
   \le
   C_{p,N}\delta\left(1+\frac{r^2}{T}\right)^{2/p}.
   \]

5. The hierarchy also gives the Caccioppoli gradient estimate
   \[
   \int_{T/2}^{T}\int
   |\chi\nabla(aE)|^2|aE|^{m-2}
   \le
   C\int_{T/2}^{T}D^E_m
   +
   Cr^{-2}\int_{T/2}^{T}J_m.
   \]

A pointwise estimate for \(\chi\nabla(aE)\) is a separate weighted Bernstein theorem. Its differentiated equation contains \(\chi a\nabla\operatorname{Rm}*U\), so it needs curvature-derivative control or a Whitney-ball nondegenerate derivative theory.
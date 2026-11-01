# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 46,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step46_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step46_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Step 46 of the Einstein-gap programme: `workspace/notes/step46_lemmaM_elementary_and_AC.md` (S1003A02). Work in the normalization CH^2 with holomorphic sectional curvature -4, Ric=-6g. Part 1, Lemma M by elementary means. (a) Check the block decomposition N = B_1 ⊕ (Δ0+12) ⊕ (Δ0+6) ⊕ ∇*∇ on K^{-1}, and that B_1 = dd* + ½d*d + 6 is the Hodge form of the one-form block, where the Step-44 'potential 1/2 at s=-4' is the Bochner form after dropping ½||d*a||². Then judge the strategist's worry that the coclosed sector has operator ½Δ_H + 3 with bottom 3.5 < 4 and so breaks L^1. (b) For the K^{-1} radial reduction, check the radial gauge A=6iη with η=½sinh²r σ3, V=9tanh²r, the claim that the Green kernel is radial f(r)e⊗e_o*, the Landau state cosh^{-3}r with eigenvalue 12, the zero-energy decay 2+√13, positivity, and the identity ∫tanh² G = 1/9. (c) Check formula (2.2) for B_1^{-1}, the Kato bound on 2(∇*∇+6)^{-1}, the mixed Hessian of distance on CH^2 (0, -2/sinh 2r, -1/sinh r), local cancellation, and the resulting L^∞ bound. (d) Check periodization, invertibility on quotients, derivative kernels, and the Schauder step (2.3), including surjectivity of L from index 0 plus injectivity. Part 2, Theorem A_C proof steps 1–6. Check: the Yamabe linearization 6(Δ+8); the DeTurck harmonic-map gauge with no loss of derivatives and Jacobi operator ∇*∇+6; the exact identity Ric°=Ric-λg when s=4λ; the Bianchi-gauge expansion with pointwise Q bound; and the York-decomposition coercivity argument. In that argument check the linearized scalar constraint 3Δf+24f, the relation ½(∇*∇+6)X=-df (signs and constants), that the linearized Einstein operator kills δ*X, the upgrade to H² on the locally symmetric quotient, and whether ||h||_{H²} ≤ 2||k||_{H²} really follows. Then check the canonical-branch IFT and the L² torsion bound ∫|∇n|² ≤ C||h||²_{H¹}. Identify any genuine gap, wrong constant or circularity, and state the exact corrected statement. Also check whether an absolute H^s (s≥5) neighbourhood with an injectivity-radius bound implies the C^{2,α}_b hypothesis, given that Step 44's A_H used the false H²⊂L^∞ in dimension 4. Do not infer any blow-up tariff.

## Integrated Scientific Memo

# Step 46 verification memo

## Verdict

The main conclusions are valid after several precise corrections.

1. **Lemma M is proved qualitatively.** The four blocks have quotient-independent \(L^\infty\) inverses, and the first-derivative kernels needed for \(\mathcal L^{-1}\) are \(L^1\). The strategist’s coclosed one-form objection is based on confusing Hodge and Bochner forms and does not threaten \(L^1\)-integrability.

2. **The elementary \(K^{-1}\) calculation is correct.** It gives
   \[
   A=\pm6i\eta,\qquad V=9\tanh^2r,\qquad
   f_0=\cosh^{-3}r,\quad \nabla^*\nabla f_0=12f_0,
   \]
   and zero-energy decay \(e^{-(2+\sqrt{13})r}\), with positive radial Green coefficient and
   \[
   \int_{\mathbb{CH}^2}\tanh^2r\,G\,d\mu=\frac19.
   \]

3. **The decimal constants \(0.21490\) and \(0.6790\) are numerical approximations, not certified upper bounds.** The script uses floating-point ODE integration and truncates at finite radius. What is rigorous is finiteness, the exact scalar bounds \(1/12,1/6\), and
   \[
   \|B_1^{-1}\|_{\infty\to\infty}
   \le \frac13+\frac16 I_{dd},\qquad I_{dd}<\infty.
   \]

4. **Theorem \(A_C\) is correct in substance but the written proof needs three repairs:**
   - harmonic-map gauge gives
     \[
     \beta_{g_\Gamma}h=O(h\nabla h),
     \]
     not exact linear Bianchi gauge;
   - \(L_E=\nabla^*\nabla-2\mathring R\) does **not** annihilate \(\delta^*X\); diffeomorphism invariance applies to the ungauged linearization;
   - the final coercivity constant must retain the small error:
     \[
     P(\hat g)^{1/2}\ge(\kappa/4-C\varepsilon)\|h\|_{H^2},
     \]
     hence, after shrinking \(\varepsilon_0\), for example
     \[
     P(\hat g)^{1/2}\ge\frac{\kappa}{8}\|h\|_{H^2}.
     \]

5. **There is no circularity in**
   \[
   \|h\|_{H^2}\le2\|k\|_{H^2}.
   \]
   It follows from the scalar constraint and gauge equation before invoking \(P\).

6. **An absolute single-scale \(H^s\) neighborhood with \(s\ge5\), together with an injectivity-radius lower bound, implies the \(C_b^{2,\alpha}\) hypothesis for every \(\alpha<1\).** The former Step-44 \(H^2\) argument remains false because \(H^2\not\hookrightarrow L^\infty\) in dimension four. Smallness only of \(k\) and \(df\) in the old conformal parametrization does not necessarily give closeness to one global scale on growing covers.

No blow-up tariff follows.

---

## 1. Normal operator and the one-form sector

At the canonical solution, \(|\Phi_0|^2=24\). The Step-44 cancellation of first-order cross terms yields
\[
\boxed{
N=B_1\oplus(\Delta_0+12)\oplus(\Delta_0+6)
\oplus\nabla^*\nabla_{K^{-1}}.
}
\]

For one-forms,
\[
\|d^*a\|^2+\|d^+a\|^2+
\left\|\frac12a\cdot\Phi_0\right\|^2
=
\left\langle
\left(dd^*+\frac12d^*d+6\right)a,a
\right\rangle,
\]
because
\[
(d^+)^*d^+=\frac12d^*d,\qquad
\left|\frac12a\cdot\Phi_0\right|^2=6|a|^2.
\]
Therefore
\[
\boxed{B_1=dd^*+\frac12d^*d+6.}
\]

Since
\[
\Delta_1=\nabla^*\nabla+\operatorname{Ric}
=\nabla^*\nabla-6,
\]
one also has
\[
B_1=\frac12\nabla^*\nabla+3+\frac12dd^*
=\frac12\Delta_1+6+\frac12dd^*.
\]
Thus Step 44’s “potential \(1/2\)” at scalar curvature \(-4\) is the **Bochner** potential after dropping \(\frac12\|d^*a\|^2\). In the present normalization it is \(\frac12\nabla^*\nabla+3\). Calling this the “Hodge form” is inaccurate.

On coclosed forms,
\[
\boxed{B_1=\frac12(\Delta_1+12),}
\]
whose coexact continuous threshold is \(\frac12(1+12)\), not \(3.5\). The proposed operator \(\frac12\Delta_H+3\) mixes the Bochner constant with the Hodge Laplacian.

Even the counterfactual operator
\[
\frac12(\Delta_1+6)
\]
would have Green decay
\[
e^{-(2+\sqrt7)r},
\]
because the coexact one-form threshold is \(\alpha_1=1\). Since \(2+\sqrt7>4\), it is \(L^1\) against shell growth \(e^{4r}\). The objection based on “spectral bottom \(3.5<4\)” therefore applies the decay test to the incorrectly scaled operator.

The sentence in §5 should read
\[
2+\sqrt7>4
\quad\text{or equivalently}\quad
\sqrt7>\rho_0,
\]
not \(2+\sqrt7>4-2\).

---

## 2. The \(K^{-1}\) radial block

### 2.1 Geometry and radial gauge

With
\[
\eta=\frac12\sinh^2r\,\sigma_3,
\qquad |\eta|^2=\frac14\tanh^2r,
\]
the Chern connection in synchronous radial gauge is
\[
A=\pm6i\eta.
\]
Thus
\[
\boxed{|A|^2=9\tanh^2r.}
\]

The script’s explicit orientation gives
\[
d\eta=e^0\wedge e^3-e^1\wedge e^2,
\]
not the plus sign written in the note. This is only an orientation/convention discrepancy: \(|d\eta|^2=2\), \(|\eta|^2\), the connection potential, and all spectral conclusions are unchanged.

Parallel transport along radial geodesics gives an isotropy-equivariant frame \(e\). The isotropy characters at \(x\) and \(o\) cancel in
\[
G(x,o)=f(r)e(x)\otimes e_o^*,
\]
so the scalar coefficient is radial. Since \(A(\partial_r)=0\), \(d^*A=0\), and \(\langle A,df\rangle=0\),
\[
\boxed{
\nabla^*\nabla(fe)=
\left[
-f''-(3\coth r+\tanh r)f'
+9\tanh^2r\,f
\right]e.
}
\]

### 2.2 Landau state and continuous threshold

Direct substitution gives
\[
\boxed{
f_0(r)=\cosh^{-3}r,\qquad
\nabla^*\nabla(f_0e)=12f_0e.
}
\]
Moreover,
\[
|f_0|^2\,\sinh^3r\cosh r\sim e^{-2r},
\]
so \(f_0\in L^2\). Together with the Kodaira lower bound
\[
\nabla^*\nabla_{K^{-1}}\ge12,
\]
this realizes the bottom.

At infinity the zero-energy equation becomes
\[
-f''-4f'+9f=0.
\]
For \(f\sim e^{-\mu r}\),
\[
\mu^2-4\mu-9=0,
\]
so
\[
\boxed{\mu_+=2+\sqrt{13}.}
\]
This derives the continuous threshold \(13\), rather than inserting it by hand.

### 2.3 Positivity and flux identity

Let
\[
J(r)=\sinh^3r\cosh r.
\]
The radial equation is
\[
-(Jf')'+9J\tanh^2r\,f=0.
\]
The decaying Green solution has positive pole normalization
\[
f(r)\sim\frac1{4\pi^2r^2}.
\]
If \(f>0\), then
\[
Jf'(r)
=-\int_r^\infty 9J(s)\tanh^2s\,f(s)\,ds<0,
\]
so \(f\) is decreasing. Sturm/maximum-principle uniqueness gives positivity of the radial coefficient.

Since shell volume grows as \(e^{4r}\),
\[
G\,d\mu
=O\!\left(e^{-(\sqrt{13}-2)r}\right)dr,
\]
and hence \(G\in L^1\).

Integrating the equation outside a small ball and using
\[
-2\pi^2J(r)f'(r)\longrightarrow1
\]
at the pole gives
\[
\boxed{
9\int_{\mathbb{CH}^2}\tanh^2r\,G\,d\mu=1.
}
\]
Consequently
\[
\|G\|_1\ge\frac19.
\]

The script’s value
\[
\|G\|_1\approx0.2148993934
\]
is consistent but not certified. A rigorous coarse comparison gives a finite model bound; for example, the supplied branch derivation yields
\[
\frac19\le\|G\|_1\le0.343.
\]

The numerical \(1.452\) is the radial quantity \(\int|f'|\), not the full covariant derivative norm. Since
\[
|\nabla(fe)|\le |f'|+3\tanh r\,f,
\]
the full derivative kernel is nevertheless \(L^1\).

---

## 3. The one-form inverse

Exact and coexact splitting gives
\[
B_1=\Delta_1+6\quad\text{on exact forms},\qquad
B_1=\frac12(\Delta_1+12)\quad\text{on coexact forms}.
\]
Since
\[
\Delta_1+12=\nabla^*\nabla+6,
\]
the formula
\[
\boxed{
B_1^{-1}
=
2(\nabla^*\nabla+6)^{-1}
-\frac16d\left[(\Delta_0+6)^{-1}-(\Delta_0+12)^{-1}\right]d^*
}
\]
is correct.

Indeed, on an exact \(\Delta_1\)-eigenmode of eigenvalue \(x\),
\[
\frac2{x+12}
-\frac{x}{(x+6)(x+12)}
=\frac1{x+6},
\]
while on coexact modes the second term vanishes. Harmonic one-forms receive multiplier \(1/6\), as required.

Kato domination gives
\[
\boxed{
\left\|2(\nabla^*\nabla+6)^{-1}\right\|_{\infty\to\infty}
\le\frac13.
}
\]

For
\[
h=G_6-G_{12},
\]
the correction kernel is \(\frac16d_xd_yh(r)\). The mixed Hessian of distance has eigenvalues
\[
0,\qquad -\frac2{\sinh2r},\qquad
-\frac1{\sinh r},\qquad-\frac1{\sinh r},
\]
up to simultaneous convention-dependent signs. Thus
\[
\left|d_xd_yh\right|_{\mathrm{op}}
=
\max\left\{|h''|,\frac{|h'|}{\sinh r}\right\},
\]
because \(2/\sinh2r\le1/\sinh r\).

Near \(r=0\), the universal \(r^{-2}\) terms in \(G_6\) and \(G_{12}\) cancel. More precisely,
\[
h'(r)\sim\frac{6-12}{8\pi^2r},
\]
so
\[
h''=O(r^{-2}),\qquad
\frac{h'}{\sinh r}=O(r^{-2}).
\]
This is locally integrable in dimension four. At infinity the slow rate is
\[
e^{-(2+\sqrt{10})r},
\]
also \(L^1\).

Therefore, defining
\[
I_{dd}
=
\int_{\mathbb{CH}^2}
\max\left\{|h''|,\frac{|h'|}{\sinh r}\right\}\,d\mu,
\]
one rigorously has
\[
\boxed{
I_{dd}<\infty,\qquad
\|B_1^{-1}\|_{\infty\to\infty}
\le\frac13+\frac{I_{dd}}6.
}
\]
The values
\[
I_{dd}\approx2.07381238,\qquad
\|B_1^{-1}\|\lesssim0.67896873
\]
must be labeled numerical estimates, not rigorous decimal upper bounds.

---

## 4. Periodization and Schauder estimates

For every homogeneous kernel \(K\in L^1(\mathbb{CH}^2)\), twisted periodization satisfies
\[
\sup_x\int_{X_\Gamma}|K_\Gamma(x,y)|\,dy
\le
\sup_{\tilde x}\int_{\mathbb{CH}^2}|K(\tilde x,z)|\,dz.
\]
Thus the \(L^\infty\) norm is independent of the quotient.

The block operators are \(L^2\)-invertible:
\[
B_1\ge6,\qquad
\Delta_0+12\ge12,\qquad
\Delta_0+6\ge6,\qquad
\nabla^*\nabla_{K^{-1}}\ge12.
\]
Hence the periodized kernels are the actual inverses.

Near the diagonal, second-order inverse kernels are \(O(r^{-2})\) and their first derivatives are \(O(r^{-3})\), both \(L^1\) in four dimensions. Away from the diagonal, homogeneous interior estimates preserve the exponential decay. Therefore \(N^{-1}\) and the differentiated kernels needed for \(N^{-1}\mathcal L^*\) are quotient-uniform.

Local Schauder estimates on fixed universal-cover balls give
\[
\boxed{
\|u\|_{C_b^{2,\alpha}}
\le C\|Nu\|_{C_b^{0,\alpha}}.
}
\]

For \(\mathcal L\), positivity of \(N=\mathcal L^*\mathcal L\) gives injectivity. The real Fredholm index of the canonical Seiberg–Witten deformation operator is zero, hence \(\mathcal L\) is surjective and
\[
\mathcal L^{-1}=N^{-1}\mathcal L^*.
\]
Thus
\[
\boxed{
\|v\|_{C_b^{1,\alpha}}
\le C\|\mathcal Lv\|_{C_b^{0,\alpha}}.
}
\]
This verifies Lemma M.

---

## 5. Theorem \(A_C\)

### 5.1 Yamabe normalization

For \(\hat g=u^2g\) with scalar curvature \(-24\),
\[
6\Delta_gu+s_gu+24u^3=0.
\]
At \((g_\Gamma,1)\),
\[
D_uF=6\Delta_0-24+72
=\boxed{6(\Delta_0+8)}.
\]
The inverse has \(L^\infty\) norm at most \(1/48\). The uniformly local implicit-function theorem therefore gives
\[
\|u-1\|_{C_b^{2,\alpha}}\le C\varepsilon.
\]
Near the negative Einstein metric the conformal class has negative Yamabe invariant, so the negative constant-scalar-curvature representative is unique and
\[
P(\hat g)\le P(g).
\]

### 5.2 Harmonic-map gauge

The harmonic-map tension map involves first derivatives of the source metric and second derivatives of the map:
\[
C_b^{2,\alpha}\times C_b^{2,\alpha}\longrightarrow C_b^{0,\alpha}.
\]
There is no loss of derivatives. Its linearization at the identity is
\[
\boxed{\nabla^*\nabla-\operatorname{Ric}
=\nabla^*\nabla+6.}
\]

The resulting metric \(g'=g_\Gamma+h\) is in nonlinear harmonic-map/DeTurck gauge:
\[
g'^{ij}\bigl(\Gamma(g')-\Gamma(g_\Gamma)\bigr)^k_{ij}=0.
\]
It does **not** satisfy \(\beta_{g_\Gamma}h=0\) exactly. Instead,
\[
\boxed{\beta_{g_\Gamma}h=O(h\nabla h).}
\]
Differentiating gives terms of the form
\[
O(h\nabla^2h)+O(|\nabla h|^2),
\]
which fit the quadratic remainder. Equivalently, one can subsequently pass to an exact Bianchi slice.

### 5.3 Ricci expansion

Because \(s(g')=-24=4\lambda\), \(\lambda=-6\),
\[
\boxed{
\operatorname{Ric}^\circ(g')
=\operatorname{Ric}(g')-\lambda g'
=\operatorname{Ric}(g')+6g'
}
\]
exactly.

In DeTurck gauge,
\[
\operatorname{Ric}(g')+6g'
=
\frac12L_Eh+Q(h),
\qquad
L_E=\nabla^*\nabla-2\mathring R,
\]
with
\[
|Q(h)|
\le
C\bigl(
|h||\nabla^2h|+|\nabla h|^2+|h|^2
\bigr).
\]
Under \(C_b^{2,\alpha}\)-smallness,
\[
\|Q(h)\|_2\le C\varepsilon\|h\|_{H^2}.
\]

### 5.4 York decomposition and coercivity

Write
\[
h=k+\delta^*X+fg_\Gamma,\qquad k\ \text{TT}.
\]
With the nonnegative Laplacian convention,
\[
D s(k)=0,\qquad
D s(\delta^*X)=0,\qquad
D s(fg_\Gamma)=\boxed{3\Delta f+24f}.
\]
The constant-scalar-curvature equation gives
\[
\boxed{
\|f\|_{H^2}\le C\varepsilon\|h\|_{H^2}.
}
\]

For
\[
\beta=\delta+\frac12d\,\operatorname{tr},
\]
one has
\[
\beta(fg_\Gamma)=df,\qquad
\beta(\delta^*X)
=\frac12(\nabla^*\nabla+6)X.
\]
Thus, in exact Bianchi gauge,
\[
\boxed{
\frac12(\nabla^*\nabla+6)X=-df.
}
\]
In harmonic-map gauge there is an additional \(O(h\nabla h)\) term:
\[
\frac12(\nabla^*\nabla+6)X
=-df+O(h\nabla h).
\]
Consequently
\[
\boxed{
\|X\|_{H^3}\le C\varepsilon\|h\|_{H^2}.
}
\]

Hence
\[
\|h-k\|_{H^2}
\le C\varepsilon\|h\|_{H^2}.
\]
For \(C\varepsilon\le1/2\),
\[
\boxed{\|h\|_{H^2}\le2\|k\|_{H^2}.}
\]
This is independent of the desired \(P\)-estimate and is therefore noncircular.

The sentence “the linearized operator kills \(\delta^*X\)” is false if “linearized operator” means \(L_E\). Diffeomorphism invariance says
\[
D(\operatorname{Ric}+6g)(\delta^*X)=0,
\]
whereas
\[
D(\operatorname{Ric}+6g)(h)
=\frac12L_Eh-\delta^*\beta h
\]
up to simultaneous sign conventions. The needed replacement is simply
\[
\|L_E(h-k)\|_2
\le C\|h-k\|_{H^2}
\le C\varepsilon\|h\|_{H^2}.
\]

For TT \(k\),
\[
\langle L_Ek,k\rangle\ge2\|k\|_2^2.
\]
Since the quotient is locally symmetric, \(\nabla\mathrm{Rm}=0\), integration by parts and commutation of derivatives give a model-uniform elliptic estimate
\[
\boxed{
\|L_Ek\|_2\ge\kappa\|k\|_{H^2}.
}
\]
Therefore
\[
\begin{aligned}
P(\hat g)^{1/2}
&=\|\operatorname{Ric}(g')+6g'\|_2\\
&\ge \frac12\|L_Ek\|_2
-C\varepsilon\|h\|_{H^2}\\
&\ge \left(\frac{\kappa}{4}-C\varepsilon\right)\|h\|_{H^2}.
\end{aligned}
\]
After shrinking \(\varepsilon_0\),
\[
\boxed{
P(\hat g)^{1/2}
\ge\frac{\kappa}{8}\|h\|_{H^2}.
}
\]
The note’s final \(\kappa/4\) omitted the remaining \(-C\varepsilon\).

### 5.5 Canonical branch

Under the Bourguignon–Gauduchon identification,
\[
F(0)=O(|h|+|\nabla h|),
\]
\[
\|DF(0)-\mathcal L\|_{C_b^{1,\alpha}\to C_b^{0,\alpha}}
\le C\varepsilon,
\]
and the nonlinear terms are zeroth-order bilinear. Lemma M therefore supplies a quotient-uniform contraction argument, producing a unique solution in a fixed \(C_b^{1,\alpha}\) neighborhood.

For the phrase “unique modulo gauge,” one should explicitly include the local Coulomb-slice lemma. Its scalar gauge operator is the positive block \(\Delta_0+6\), so this is routine and quotient-uniform, but it is not written out in the note.

### 5.6 Torsion estimate

The equation for \(v=(a,\psi)\) and the Step-44 gap give
\[
\|v\|_{H^1}
\le C\|h\|_{H^1}
+C\varepsilon\|v\|_{H^1},
\]
hence
\[
\boxed{\|v\|_{H^1}\le C\|h\|_{H^1}.}
\]
Because \(\Phi_0\) is parallel, \(|\Phi|\) stays uniformly positive, and the spinor/connection identifications vary by \(h,\nabla h\),
\[
|\nabla n|
\le C\bigl(|\nabla v|+|v|+|\nabla h|\bigr).
\]
Thus
\[
\boxed{
\int|\nabla n|^2
\le C\|h\|_{H^1}^2
\le C\|h\|_{H^2}^2
\le CP(\hat g)
\le CP(g).
}
\]
After the fixed normalization change from scalar curvature \(-24\) to \(-4\), this yields
\[
R_{\mathrm{can}}(\hat g)\le C'P(g).
\]

---

## 6. Corrected theorem

A statement fully supported by the argument is:

> There exist \(\varepsilon_0,C>0\), depending only on the complex-hyperbolic model, such that for every compact ball quotient \(X_\Gamma\), if one global diffeomorphism \(\phi\) and one constant \(c>0\) satisfy
> \[
> \|c\,\phi^*g-g_\Gamma\|_{C_b^{2,\alpha}}\le\varepsilon_0,
> \]
> then the scalar-normalized Yamabe representative has a Seiberg–Witten solution in the canonical class lying in a fixed \(C_b^{1,\alpha}\) neighborhood of the canonical Kähler solution. It is unique modulo gauge among solutions in that neighborhood, after applying the uniformly local Coulomb slice. Its direction satisfies
> \[
> \int|\nabla n|^2\le CP(\hat g)\le CP(g),
> \qquad
> R_{\rm can}(\hat g)\le C'P(g),
> \]
> with constants independent of the quotient.
>
> In the proof, harmonic-map gauge is used as
> \[
> \beta h=O(h\nabla h),
> \]
> and the York gauge and conformal components satisfy
> \[
> \|h-k\|_{H^2}\le C\varepsilon\|h\|_{H^2}.
> \]

The hypothesis may be weakened to require that **some metric conformal to \(g\)** satisfy the displayed \(C_b^{2,\alpha}\) closeness, because Yamabe normalization and \(P(g)\ge P(\hat g)\) depend only on the conformal class in the required way.

---

## 7. Relation to absolute \(H^s\) neighborhoods

In dimension four,
\[
H^s\hookrightarrow C^{2,\alpha}
\quad\text{provided}\quad s>4+\alpha.
\]
Thus \(s=5\) works for every \(\alpha<1\). If
\[
\operatorname{inj}(X_\Gamma,g_\Gamma)\ge i_0>0,
\]
bounded geometry gives
\[
\|c\,\phi^*g-g_\Gamma\|_{C_b^{2,\alpha}}
\le C(i_0,\alpha)
\|c\,\phi^*g-g_\Gamma\|_{H^5}.
\]
Therefore a sufficiently small **absolute global \(H^s\) norm of the metric difference after one global diffeomorphism and one global scale**, with \(s\ge5\), implies the \(A_C\) hypothesis.

Two qualifications are essential:

- per-unit-volume or volume-normalized Sobolev smallness does not imply uniform local closeness;
- the old Step-44 condition expressed only through
  \[
  \|k\|_{H^s}+\|df\|_{H^{s-1}}
  \]
  need not control \(e^{2f}\) relative to one global constant scale on growing covers. Slow conformal drift can have small \(df\) but order-one oscillation.

The original absolute-\(H^2\) nonlinear theorem remains unproved: in four dimensions
\[
H^2\not\hookrightarrow L^\infty,
\]
so the quadratic terms \(h*\nabla^2h\) cannot be absorbed by that argument alone.

---

## Final status

- **Lemma M:** verified, with numerical constants downgraded to approximations and the orientation sign corrected.
- **Theorem \(A_C\):** valid for the nearby canonical branch after correcting the nonlinear gauge equation, the pure-gauge Einstein-operator claim, and the final coercivity constant; the local gauge-slice step should be stated explicitly.
- **Scope:** no selection of other monopole branches, no localization across blow-up collars or cores, and no blow-up tariff.
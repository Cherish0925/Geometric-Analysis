# TTCS Independent Branch Record

```json
{
  "step_id": 48,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A02/workspace/notes/step46_lemmaM_elementary_and_AC.md",
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md",
    "Sessions/S1003A02/workspace/scripts/step48_bianchi_indicial.py",
    "Sessions/S1003A02/workspace/data/step48_bianchi_indicial.json"
  ]
}
```

## Task

Verify §3 of Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md (localized complex-hyperbolic coercivity) as rigorous analysis. Check: (1) Proposition 48.3: L=½(∇*∇−2R̊) on symmetric 2-tensors over any closed ball quotient with Ric=−6g satisfies ⟨Lu,u⟩≥‖u‖², via the L²-orthogonal decomposition TT ⊕ closure(im T), T(X,f)=δ*X+fg, the intertwining LT=TD with D=diag(½Δ_H+6, ½Δ_0+6), commutation [T*T,D]=0, and Koiso's identity on TT (Step 44 G1, R̊≤4). Are the intertwining identities Δ_Lδ*=δ*Δ_H and Δ_L(fg)=(Δf)g correct on Einstein manifolds, and does the commuting-operator argument legitimately give ≥6‖Tw‖²? (2) Proposition 48.4 (Combes–Thomas) and Theorem 48.L, including the nonlinear absorption, Dirichlet DeTurck gauge on a region with boundary, weighted elliptic regularity, and uniformity in Γ, B, k. (3) Lemma 48.5: the scalar-curvature linearization in Bianchi gauge s'(h)=½(Δ+12)tr h (check sign conventions with Besse 1.174) and the volume formula with boundary flux. (4) Theorem 48.LY: does the combination with Theorem Y (Section 2) legitimately give P ≥ (8π²k − 4ΔV_U − CΛ²)/(1+C)? Watch scale conversions between Ric=−6 and s=−4, and whether the hypothesis is placed on the Yamabe representative consistently. (5) The indicial-root table from workspace/data/step48_bianchi_indicial.json (diagonal Bianchi IX about CH² with A=B=sinh r, C=sinh r cosh r; Ricci formulas in the script docstring) and the interpretation: J-anti triaxial tail e^{-4r} marginal vs volume e^{4r}, U(2) tails e^{-6r}, and the claim that the triaxial mode changes μ_min and |W+|² only at second order. Give corrected statements where needed and say what remains unproved.

## Output

# Scientific verification memo: localized complex-hyperbolic coercivity

## Executive result

1. **Proposition 48.3 is correct** with the stated Laplacian conventions. The intertwining formulas are exact on an Einstein manifold, and the \(T^*T\)-commutation argument gives the stronger constant \(6\) on \(\overline{\operatorname{im}T}\). The TT sector gives the global constant \(1\).

2. **Proposition 48.4 is correct** after writing the real part of the quadratic form. The threshold \(a<\sqrt2\) follows exactly from the factor \(1/2\) in \(L\).

3. **Theorem 48.L has the right analytic mechanism**, but its written proof needs three explicit additions:
   - the nonlinear Einstein remainder contains an algebraic \(O(|h|^2)\) term;
   - the weighted \(H^2\) estimate and the cutoffs require a smooth distance surrogate with model-uniform derivatives;
   - the harmonic-map/DeTurck parenthesis establishes uniform gauge construction only with regular \(\partial\Omega\) and specified Dirichlet data. If gauge is retained as a hypothesis, this last point does not affect the decay estimate.

4. **Lemma 48.5 has the correct sign and coefficient \(1/24\)** in the \(\operatorname{Ric}=-6g\), \(s=-24\) normalization. Its remainder should include \(O(|h|^2)\).

5. **Theorem 48.LY is not obtained exactly as written.** There are two concrete mismatches:
   - 48.L is invoked with \(T=1\), although its cutoff only controls \(\{d\ge2\}\);
   - the displayed core quantity is described as being in scalar-\(-4\) units but uses the scalar-\(-24\) flux coefficient \(1/24\).
   
   Both are repaired by taking the exterior to be \(\{d\ge2\}\) and defining the core excess either wholly in scalar-\(-24\) units and multiplying by \(36\), or wholly in scalar-\(-4\) units with flux coefficient \(1/4\).

6. In the indicial table, **the U(2)-invariant root \(\nu=8\) does not satisfy the \(E_{00}=0\) equation**. The full radial-gauge Einstein roots are
   \[
   \text{triaxial: }0,4,\qquad
   \text{U(2): }-2,0,6.
   \]
   The \(e^{-4r}\) versus \(e^{-6r}\) integrability interpretation is otherwise correct within the diagonal SU(2)-invariant sector.

---

## 1. Proposition 48.3

Let
\[
\Delta_E:=\nabla^*\nabla-2\mathring R,\qquad
L=\frac12\Delta_E.
\]
For the Lichnerowicz Laplacian convention
\[
(\Delta_Lh)_{ij}
=(\nabla^*\nabla h)_{ij}
+R_i{}^kh_{kj}+R_j{}^kh_{ik}
-2R_{ikjl}h^{kl},
\]
an Einstein metric with \(\operatorname{Ric}=\lambda g\) satisfies
\[
\Delta_L=\Delta_E+2\lambda.
\]
Here \(\lambda=-6\), so
\[
L=\frac12\Delta_L+6.
\]

### Intertwining identities

On an Einstein manifold,
\[
\Delta_L(\delta^*X)=\delta^*(\Delta_HX),
\qquad
\Delta_L(fg)=(\Delta_0f)g.
\]
The second identity follows directly because
\[
\nabla^*\nabla(fg)=(\Delta_0f)g
\]
and the two Ricci actions cancel the Riemann contraction on \(fg\). Consequently,
\[
L(\delta^*X)
=\delta^*\left(\frac12\Delta_H+6\right)X,
\qquad
L(fg)
=\left(\frac12\Delta_0+6\right)f\,g.
\]
Thus, for
\[
T(X,f)=\delta^*X+fg,\qquad
D=\operatorname{diag}\left(\frac12\Delta_H+6,\frac12\Delta_0+6\right),
\]
one has
\[
LT=TD.
\]

### Orthogonal decomposition and commutation

Since
\[
T^*h=(\delta h,\operatorname{tr}h)
\]
up to the fixed convention for \(\delta^*\),
\[
\ker T^*=\{h:\delta h=0,\ \operatorname{tr}h=0\}=TT.
\]
The Hilbert-space decomposition is therefore
\[
L^2(S^2T^*X_0)=TT\oplus\overline{\operatorname{im}T}.
\]

The component calculation of \(T^*T\) is not needed. Since \(L\) and \(D\) are self-adjoint,
\[
LT=TD
\quad\Longrightarrow\quad
T^*L=DT^*.
\]
Hence
\[
T^*TD=T^*LT=DT^*T.
\]
Thus \(A:=T^*T\) commutes with \(D\) on the common smooth core. Since \(D\ge6\),
\[
\begin{aligned}
\langle LTw,Tw\rangle
&=\langle TDw,Tw\rangle\\
&=\langle ADw,w\rangle\\
&=\langle D A^{1/2}w,A^{1/2}w\rangle\\
&\ge6\|A^{1/2}w\|^2
=6\|Tw\|^2.
\end{aligned}
\]
On a compact quotient this can also be justified eigenspace by eigenspace for the elliptic operator \(D\). Density extends the estimate to \(\overline{\operatorname{im}T}\).

### TT sector

For \(h\in TT\), the Koiso identity used in Step 44 gives
\[
\langle Lh,h\rangle
=\frac12\|d^\nabla h\|^2
+\frac12\langle(6-\mathring R)h,h\rangle.
\]
On \(\mathbb{CH}^2\), the largest eigenvalue of \(\mathring R\) on trace-free symmetric tensors is \(4\), so
\[
\langle Lh,h\rangle\ge\frac12(6-4)\|h\|^2=\|h\|^2.
\]

Therefore
\[
\boxed{\langle Lu,u\rangle\ge\|u\|^2}
\]
on all symmetric two-tensors. The natural form domain is \(H^1\); the stated \(H^2\) class is more regular than needed.

---

## 2. Proposition 48.4 and Theorem 48.L

### 2.1 Combes–Thomas estimate

For a real Lipschitz function \(\phi\), multiplication by \(e^{\pm\phi}\) preserves the form domain. For a real bundle section \(u\),
\[
\begin{aligned}
\left\langle e^\phi\nabla^*\nabla(e^{-\phi}u),u\right\rangle
&=\int\left\langle\nabla(e^{-\phi}u),\nabla(e^\phi u)\right\rangle\\
&=\|\nabla u\|^2-\int|d\phi|^2|u|^2.
\end{aligned}
\]
For complexified tensors the same formula holds after taking the real part. Since the curvature endomorphism commutes with scalar multiplication,
\[
\operatorname{Re}\langle e^\phi Le^{-\phi}u,u\rangle
=\langle Lu,u\rangle-\frac12\int|d\phi|^2|u|^2.
\]
Proposition 48.3 therefore gives
\[
\operatorname{Re}\langle e^\phi Le^{-\phi}u,u\rangle
\ge\left(1-\frac{a^2}{2}\right)\|u\|^2.
\]
The adjoint conjugated operator corresponds to \(-\phi\) and has the same estimate, so the conjugated operator is onto as well as one-to-one. Hence
\[
\boxed{
\|e^\phi L^{-1}e^{-\phi}\|_{2\to2}
\le\left(1-\frac{a^2}{2}\right)^{-1}
}
\]
for \(a<\sqrt2\).

### 2.2 Einstein expansion

For a scalar-\(-24\) metric \(g=g_0+h\),
\[
\operatorname{Ric}^\circ_g=\operatorname{Ric}(g)+6g
\]
exactly. In exact linear Bianchi gauge, or in nonlinear DeTurck gauge where
\[
\beta_{g_0}(h)=O(h\nabla h),
\]
the expansion is
\[
\operatorname{Ric}^\circ_g=Lh+Q(h).
\]
On a curved background, the complete pointwise remainder has the form
\[
\boxed{
|Q(h)|
\le C\bigl(
|h||\nabla^2h|
+|\nabla h|^2
+|h|^2
\bigr).
}
\]
The \(O(|h|^2)\) term comes from the background-curvature coefficients in the Ricci expansion. Under
\(\|h\|_{C^{2,\alpha}_{ul}}\le\varepsilon\),
\[
\|e^\phi Q(h)\|_2
\le C\varepsilon\|e^\phi h\|_{H^2}.
\]
Thus the omitted algebraic term does not change the absorption argument.

### 2.3 Cutoffs and weighted \(H^2\) regularity

The formula
\[
[L,\chi]h
=-\nabla_{\nabla\chi}h+\frac12(\Delta\chi)h
\]
is correct.

For arbitrary closed \(B\), the raw distance \(d(\cdot,B)\) is only Lipschitz. A rigorous construction can lift \(d\) to \(\mathbb{CH}^2\), smooth it using a compactly supported radial convolution kernel, and descend the resulting \(\Gamma\)-invariant function. This gives cutoffs with
\[
|\nabla\chi|+|\nabla^2\chi|\le C
\]
independently of \(\Gamma,B,k\), with transition contained in a slightly chosen subannulus of \(1<d<2\).

The same smoothing produces a weight differing by \(O(1)\) from \(a\min(d,T)\), with uniformly bounded first two derivatives. Using a slightly larger intermediate rate \(a<b<\sqrt2\) preserves the final \(e^{-aT}\) decay. Standard elliptic regularity then gives
\[
\|e^\phi u\|_{H^2}
\le C\bigl(\|e^\phi Lu\|_2+\|e^\phi u\|_2\bigr),
\]
with a model constant. The quotient uniformity can be proved either by lifting local estimates to \(\mathbb{CH}^2\) or by global Bochner estimates, using that the reference curvature is parallel.

### 2.4 Nonlinear absorption

Set
\[
h_1=L^{-1}(\chi\operatorname{Ric}^\circ_g),
\qquad
h_2=\chi h-h_1.
\]
Then
\[
Lh_2=-\chi Q(h)+[L,\chi]h.
\]
The unweighted elliptic estimate gives
\[
\|h_1\|_{H^2}
\le C\|\operatorname{Ric}^\circ_g\|_{L^2(d\ge1)}.
\]
Since the capped weight satisfies \(e^\phi\le e^{aT}\),
\[
\|e^\phi h_1\|_{H^2}
\le Ce^{aT}\|\operatorname{Ric}^\circ_g\|_{L^2(d\ge1)}.
\]
For \(h_2\),
\[
\|e^\phi h_2\|_{H^2}
\le C\Lambda
+C\varepsilon\|e^\phi\chi h\|_{H^2}.
\]
Substituting \(\chi h=h_1+h_2\) and taking \(C\varepsilon<1/2\) yields
\[
\|e^\phi h_2\|_{H^2}
\le C\Lambda
+C\varepsilon e^{aT}
\|\operatorname{Ric}^\circ_g\|_2.
\]
On \(\{d\ge T\}\), \(\chi=1\) and \(e^\phi=e^{aT}\), so
\[
\boxed{
\|h\|_{H^2(d\ge T)}
\le C\left(
\|\operatorname{Ric}^\circ_g\|_{L^2(d\ge1)}
+e^{-aT}\Lambda
\right).
}
\]

### 2.5 Gauge construction

The harmonic-map linearization at the identity is indeed
\[
J=\nabla^*\nabla-\operatorname{Ric}
=\nabla^*\nabla+6.
\]
With zero Dirichlet data on a smooth \(\partial\Omega\),
\[
\langle JX,X\rangle=\|\nabla X\|^2+6\|X\|^2,
\]
so no quotient-dependent small eigenvalue enters.

What is not supplied in §3 is a uniform nonlinear harmonic-map construction for an arbitrary closed \(B\) whose distance levels may be nonsmooth. Uniform Hölder estimates near \(\partial\Omega\) require regular geometric charts there. The decay theorem remains valid when DeTurck/Bianchi gauge is treated as an explicit hypothesis, as its statement already does.

---

## 3. Lemma 48.5

Let \(t=\operatorname{tr}_{g_0}h\), with
\[
\Delta=\delta d=-\nabla^i\nabla_i.
\]
Besse 1.174 gives
\[
s'_{g_0}(h)
=\Delta t+\delta\delta h-\langle\operatorname{Ric}_0,h\rangle.
\]
For
\[
\delta h=-\frac12dt
\]
one has
\[
\delta\delta h=-\frac12\Delta t.
\]
Since \(\operatorname{Ric}_0=-6g_0\),
\[
-\langle\operatorname{Ric}_0,h\rangle=6t.
\]
Therefore
\[
\boxed{
s'_{g_0}(h)=\frac12(\Delta+12)t.
}
\]

For exact scalar equality \(s_g=s_{g_0}=-24\),
\[
\frac12(\Delta+12)t=Q_s,
\]
where the complete remainder obeys
\[
|Q_s|
\le C\bigl(
|h||\nabla^2h|
+|\nabla h|^2
+|h|^2
\bigr).
\]
The same formula holds in nonlinear DeTurck gauge after absorbing the divergence of \(O(h\nabla h)\) into \(Q_s\).

Let \(\nu\) point out of \(\Omega\). Since
\[
\int_\Omega\Delta t\,d\mu_0
=-\int_{\partial\Omega}\partial_\nu t\,dA_0,
\]
integration gives
\[
-\frac12\int_{\partial\Omega}\partial_\nu t
+6\int_\Omega t
=\int_\Omega Q_s.
\]
Thus
\[
\int_\Omega t
=\frac1{12}\int_{\partial\Omega}\partial_\nu t
+O(\|h\|_{H^2(\Omega)}^2).
\]
The determinant expansion
\[
d\mu_g
=\left(1+\frac12t+O(|h|^2)\right)d\mu_0
\]
then yields
\[
\boxed{
\operatorname{Vol}_g(\Omega)-\operatorname{Vol}_{g_0}(\Omega)
=\frac1{24}\int_{\partial\Omega}\partial_\nu t
+O(\|h\|_{H^2(\Omega)}^2).
}
\]

The sign and coefficient in Lemma 48.5 are therefore correct. A smooth \(\partial\Omega\), or an explicitly regularized distance level, is needed for the classical flux expression.

---

## 4. Theorem 48.LY

### 4.1 Radius mismatch

The proof says to apply 48.L with \(T=1\), but 48.L was established using a cutoff that is zero for \(d\le1\) and one for \(d\ge2\). It controls
\[
\|h\|_{H^2(d\ge2)},
\]
not the full \(H^2\)-norm on \(\{d\ge1\}\). The \(H^1\) quantity
\[
\Lambda=\|h\|_{H^1(1\le d\le2)}
\]
does not by itself provide \(H^2\) control throughout that annulus.

A consistent formulation uses
\[
\Omega_2=\{d\ge2\},
\qquad
U_2=M\setminus F(\Omega_2),
\qquad
\Sigma_2=\{d=2\}.
\]
Then 48.L gives
\[
\|h\|_{H^2(\Omega_2)}^2
\le C\left(
P(\hat g)+\Lambda^2
\right).
\]
Equivalently, one can redesign the cutoff to become one by \(d=1\), but then its transition layer and the definition of \(\Lambda\) must be moved inside \(d<1\).

### 4.2 Scale conversion

Let
\[
\widetilde g=\frac16\hat g,
\]
so \(s_{\widetilde g}=-24\), and let \(g_0\) satisfy \(\operatorname{Ric}_{g_0}=-6g_0\). In these units define
\[
\widetilde{\Delta V}_{U_2}
=
\operatorname{Vol}_{\widetilde g}(U_2)
-\operatorname{Vol}_{g_0}(\{d<2\})
+\frac1{24}\int_{\Sigma_2}
\partial_{\nu_0}\operatorname{tr}_{g_0}(\widetilde g-g_0)\,dA_0.
\]
The scalar-\(-4\) quantity entering Theorem Y is
\[
\boxed{
\Delta V_{U_2}^{(-4)}
=36\,\widetilde{\Delta V}_{U_2}.
}
\]
Equivalently, with \(\hat g_0=6g_0\),
\[
\Delta V_{U_2}^{(-4)}
=
\operatorname{Vol}_{\hat g}(U_2)
-\operatorname{Vol}_{\hat g_0}(\{d<2\})
+\frac14\int_{\Sigma_2}
\partial_{\hat\nu_0}
\operatorname{tr}_{\hat g_0}(\hat g-\hat g_0)
\,dA_{\hat g_0}.
\]
Thus a formula described as being in \(\hat g\) units must use \(1/4\), not \(1/24\).

The Weyl penalty is scale invariant when the reference orbit is scaled simultaneously:
\[
\mathcal K_{-24}=6\mathcal K_{-4},
\]
and
\[
\int\operatorname{dist}_{\widetilde g}
(W^+_{\widetilde g},\mathcal K_{-24})^2\,d\mu_{\widetilde g}
=
\int\operatorname{dist}_{\hat g}
(W^+_{\hat g},\mathcal K_{-4})^2\,d\mu_{\hat g}.
\]

### 4.3 Correct combination with Theorem Y

Lemma 48.5 and 48.L now give
\[
\left|
\Delta V-\Delta V_{U_2}^{(-4)}
\right|
\le C\left(P(\hat g)+\Lambda^2\right).
\]
Since
\[
P(\hat g)\le P(g)
\]
and
\[
\|\operatorname{Ric}^\circ_{\widetilde g}\|_2^2=P(\hat g),
\]
Theorem Y yields
\[
\boxed{
8\pi^2k-P(g)
\le
4\Delta V_{U_2}^{(-4)}
-\frac{20}{9}\int_{U_2}
\operatorname{dist}(W^+,\mathcal K)^2
+C\bigl(P(g)+\Lambda^2\bigr).
}
\]
Dropping the explicitly subtracted Weyl term and rearranging gives
\[
\boxed{
P(g)
\ge
\frac{
8\pi^2k-4\Delta V_{U_2}^{(-4)}-C\Lambda^2
}{1+C}.
}
\]
Thus the algebraic lower estimate is valid once the radius and scale conventions are corrected. The core quantity is a marked relative-volume quantity: it depends on the chosen exterior identification \(F\), gauge, and interface germ.

---

## 5. Indicial roots

The script correctly verifies that
\[
A=B=\sinh r,\qquad C=\sinh r\cosh r
\]
solves \(E_{\alpha\alpha}=\operatorname{Ric}_{\alpha\alpha}+6=0\). Its asymptotic matrix is also internally consistent. The determinant used for the table, however, is formed only from the spatial rows \(E_{11},E_{22},E_{33}\). Every Einstein mode must also satisfy \(E_{00}=0\).

### 5.1 Triaxial sector

For
\[
(a,b,c)=(1,-1,0)e^{-\nu r},
\]
the spatial equation is
\[
-\nu(\nu-4)=0.
\]
The \(E_{00}\) row cancels identically between \(a\) and \(b\), so both roots survive:
\[
\boxed{\nu=0,\ 4.}
\]

### 5.2 U(2)-invariant sector

Set \(a=b=x\), \(c=z\). Imposing all four equations gives:

\[
\begin{array}{c|c}
\nu & (a,b,c)\\ \hline
-2 &(1,1,-4/3)\\
0 &(1,1,2)\\
6 &(1,1,-4).
\end{array}
\]

For the spatial root \(\nu=8\), the spatial equations require
\[
(a,b,c)=(1,1,2).
\]
But the \(E_{00}\) row at \(\nu=8\) is
\[
(-48,-48,-32),
\]
whose contraction with \((1,1,2)\) is
\[
-48-48-64=-160\ne0.
\]
Therefore
\[
\boxed{\nu=8\ \text{is not a radial-gauge Einstein indicial mode}.}
\]

The corrected table is
\[
\begin{array}{c|c}
\text{sector}&\text{full Einstein roots}\\ \hline
a=-b,\ c=0&0,\ 4\\
a=b&-2,\ 0,\ 6.
\end{array}
\]

The U(2) root \(0\) has vector \((1,1,2)\), exactly the leading effect of a radial translation, since
\[
\frac{A'}A\to1,\qquad \frac{C'}C\to2.
\]

### 5.3 Integrability interpretation

Since the volume density grows as \(e^{4r}\):

- a triaxial \(e^{-4r}\) metric or curvature perturbation has
  \[
  \int_0^R e^{-4r}e^{4r}\,dr=O(R),
  \]
  corresponding to logarithmic growth in the enclosed volume;

- the physical decaying U(2) mode \(e^{-6r}\) has
  \[
  \int_0^\infty e^{-6r}e^{4r}\,dr<\infty.
  \]

Thus the marginal versus summable distinction is correct in this diagonal SU(2)-invariant model.

At the CH metric, in scalar-\(-24\) units,
\[
\operatorname{spec}(W^+)=(-4,2,2).
\]
For the pure triaxial one-parameter family, exchanging the first two axes sends the triaxial parameter \(q\) to \(-q\) while preserving the unordered spectrum of \(W^+\). Since the lowest eigenvalue is simple near \(q=0\),
\[
\mu_{\min}(q)=\mu_{\min}(-q),\qquad
|W^+(q)|^2=|W^+(-q)|^2.
\]
Consequently,
\[
\mu_{\min}(q)-\mu_{\min}(0)=O(q^2),
\qquad
|W^+(q)|^2-|W^+(0)|^2=O(q^2).
\]
For \(q=O(e^{-4r})\), Theorem Y’s density is therefore \(O(e^{-8r})\), and
\[
\int e^{-8r}e^{4r}\,dr<\infty.
\]

The supplied script does not compute \(W^+\). In particular, it does not establish that the upper pair actually has a nonzero linear split
\[
2\pm cq+O(q^2),\qquad c\ne0.
\]
That requires a separate linearized Weyl calculation. If \(c\ne0\), then
\[
\operatorname{dist}(W^+,\mathcal K)=O(|q|),
\]
so Theorem K records the marginal \(e^{-4r}\) contribution while Theorem Y records its square. If \(c=0\), the distance to \(\mathcal K\) may also begin quadratically. The stronger phrase that this is exactly the sector counted linearly by Theorem K is therefore not yet established by the JSON calculation.

Finally, these are formal indicial modes only in the diagonal SU(2)-invariant sector. The computation does not supply the indicial spectrum for angularly varying tensors, nonlinear existence of the corresponding tails, or matching to the marked core metrics.
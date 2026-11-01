# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 48,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step48_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step48_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify §3 of Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md (localized complex-hyperbolic coercivity) as rigorous analysis. Check: (1) Proposition 48.3: L=½(∇*∇−2R̊) on symmetric 2-tensors over any closed ball quotient with Ric=−6g satisfies ⟨Lu,u⟩≥‖u‖², via the L²-orthogonal decomposition TT ⊕ closure(im T), T(X,f)=δ*X+fg, the intertwining LT=TD with D=diag(½Δ_H+6, ½Δ_0+6), commutation [T*T,D]=0, and Koiso's identity on TT (Step 44 G1, R̊≤4). Are the intertwining identities Δ_Lδ*=δ*Δ_H and Δ_L(fg)=(Δf)g correct on Einstein manifolds, and does the commuting-operator argument legitimately give ≥6‖Tw‖²? (2) Proposition 48.4 (Combes–Thomas) and Theorem 48.L, including the nonlinear absorption, Dirichlet DeTurck gauge on a region with boundary, weighted elliptic regularity, and uniformity in Γ, B, k. (3) Lemma 48.5: the scalar-curvature linearization in Bianchi gauge s'(h)=½(Δ+12)tr h (check sign conventions with Besse 1.174) and the volume formula with boundary flux. (4) Theorem 48.LY: does the combination with Theorem Y (Section 2) legitimately give P ≥ (8π²k − 4ΔV_U − CΛ²)/(1+C)? Watch scale conversions between Ric=−6 and s=−4, and whether the hypothesis is placed on the Yamabe representative consistently. (5) The indicial-root table from workspace/data/step48_bianchi_indicial.json (diagonal Bianchi IX about CH² with A=B=sinh r, C=sinh r cosh r; Ricci formulas in the script docstring) and the interpretation: J-anti triaxial tail e^{-4r} marginal vs volume e^{4r}, U(2) tails e^{-6r}, and the claim that the triaxial mode changes μ_min and |W+|² only at second order. Give corrected statements where needed and say what remains unproved.

## Integrated Scientific Memo

# Verification of §3: localized complex-hyperbolic coercivity

## Verdict

- **Proposition 48.3 is correct.** The two Lichnerowicz intertwining identities hold with the conventions used, and the commuting-operator argument gives the stronger lower bound \(6\) on \(\overline{\operatorname{im}T}\); the TT sector determines the global constant \(1\).
- **Proposition 48.4 is correct**, interpreted at the quadratic-form level and with real parts for complexified tensors.
- **Theorem 48.L has a valid core argument**, but the current proof is not fully rigorous without repairing the distance/cutoff regularity, the nonlinear remainder, and the boundary-gauge assertion.
- **Lemma 48.5 has the correct sign and coefficient \(1/24\)** in the \(s=-24\), \(\operatorname{Ric}=-6g\) scale.
- **Theorem 48.LY is not correct exactly as stated.** It mixes scalar-\(-24\) and scalar-\(-4\) volume conventions, invokes 48.L outside its proved radius range, and silently identifies the reference ball quotient’s \(c_1^2\) with \(A=c_1^2(X)\).
- In the indicial table, **the U(2) root \(\nu=8\) is spurious** because it violates the \(00\) Einstein equation. The genuine diagonal radial-gauge roots are
  \[
  \text{triaxial}:0,4,\qquad \text{U(2)}:-2,0,6.
  \]
- The \(e^{-4r}\) marginal versus \(e^{-6r}\) summable interpretation is valid **within the diagonal SU(2)-invariant sector**. The first variations of \(\mu_{\min}\) and \(|W^+|^2\) vanish for the triaxial mode, but a nonzero first-order splitting of the upper Weyl eigenvalues has not been computed.

---

## 1. Proposition 48.3

Write
\[
L=\frac12(\nabla^*\nabla-2\mathring R).
\]
For the convention
\[
(\Delta_Lh)_{ij}
=(\nabla^*\nabla h)_{ij}
+R_i{}^kh_{kj}+R_j{}^kh_{ik}
-2R_{ikjl}h^{kl},
\]
an Einstein metric \(\operatorname{Ric}=\lambda g\) satisfies
\[
\Delta_L=\nabla^*\nabla-2\mathring R+2\lambda.
\]
At \(\lambda=-6\),
\[
L=\frac12\Delta_L+6.
\]

### Intertwining identities

On every Einstein manifold,
\[
\Delta_L\delta^*=\delta^*\Delta_H,
\qquad
\Delta_L(fg)=(\Delta_0f)g.
\]
The second follows directly because
\[
\nabla^*\nabla(fg)=(\Delta_0f)g
\]
and the two Ricci actions cancel \(2\mathring R(fg)=2f\operatorname{Ric}\).

Therefore, with
\[
T(X,f)=\delta^*X+fg,\qquad
D=\operatorname{diag}\left(\frac12\Delta_H+6,\frac12\Delta_0+6\right),
\]
one has
\[
LT=TD,\qquad D\ge6.
\]

### Orthogonal decomposition and the commuting argument

Up to harmless convention-dependent constants and signs,
\[
T^*h=(\delta h,\operatorname{tr}h),
\]
so
\[
\ker T^*=TT.
\]
Hence
\[
L^2(S^2T^*X_0)=TT\oplus\overline{\operatorname{im}T}.
\]
In fact \(\operatorname{im}T\) is closed because \(T\) is overdetermined elliptic, but closure suffices.

Since \(L,D\) are self-adjoint and \(LT=TD\),
\[
T^*L=DT^*,\qquad T^*TD=DT^*T.
\]
Thus \(A:=T^*T\) strongly commutes with \(D\). On a closed quotient this can be justified eigenspace-by-eigenspace for \(D\). Consequently,
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
So the claimed \(6\)-gap on the gauge-plus-trace sector is legitimate. No lower bound on the first positive eigenvalue of \(\Delta_H\) or \(\Delta_0\) is used.

### TT sector

For \(h\in TT\), Koiso’s identity gives
\[
\langle Lh,h\rangle
=\frac12\|d^\nabla h\|^2
+\frac12\langle(6-\mathring R)h,h\rangle.
\]
On \(\mathbb{CH}^2\) with holomorphic sectional curvature \(-4\),
\[
\max\operatorname{spec}(\mathring R|_{S^2_0})=4,
\]
so
\[
\langle Lh,h\rangle\ge\|h\|^2.
\]
The two orthogonal summands are \(L\)-invariant, since \(LT=TD\) and \(L\) is self-adjoint. Therefore
\[
\boxed{\langle Lu,u\rangle\ge\|u\|^2.}
\]
The natural form domain is \(H^1\); stating it for \(H^2\) is harmless.

---

## 2. Proposition 48.4 and Theorem 48.L

### 2.1 Combes–Thomas estimate

For real Lipschitz \(\phi\), the argument should be formulated on the \(H^1\) form domain. For a real section \(u\),
\[
\operatorname{Re}\left\langle
e^\phi\nabla^*\nabla(e^{-\phi}u),u
\right\rangle
=
\|\nabla u\|^2-\int|d\phi|^2|u|^2.
\]
The curvature endomorphism commutes with scalar multiplication, hence
\[
\operatorname{Re}\langle e^\phi Le^{-\phi}u,u\rangle
=
\langle Lu,u\rangle-\frac12\int|d\phi|^2|u|^2.
\]
Using Proposition 48.3,
\[
\operatorname{Re}\langle e^\phi Le^{-\phi}u,u\rangle
\ge\left(1-\frac{a^2}{2}\right)\|u\|^2
\]
when \(|d\phi|\le a\). The adjoint is the conjugation with \(-\phi\) and obeys the same estimate, giving surjectivity as well as injectivity. Thus
\[
\boxed{
\|e^\phi L^{-1}e^{-\phi}\|_{2\to2}
\le (1-a^2/2)^{-1},\qquad a<\sqrt2.
}
\]

### 2.2 Nonlinear Einstein expansion

For \(s_g=-24\),
\[
\operatorname{Ric}_g^\circ=\operatorname{Ric}_g+6g
\]
exactly. In exact Bianchi gauge, or nonlinear DeTurck gauge with
\[
\beta_{g_0}(h)=O(h\nabla h),
\]
one has
\[
\operatorname{Ric}_g^\circ=Lh+Q(h).
\]
The remainder quoted in the note is incomplete. On the curved background the correct estimate is
\[
\boxed{
|Q(h)|\le C\bigl(
|h||\nabla^2h|+|\nabla h|^2+|h|^2
\bigr).
}
\]
Under \(\|h\|_{C^{2,\alpha}_{ul}}\le\varepsilon\), the additional algebraic term is absorbable:
\[
\|e^\phi Q(h)\|_2\le C\varepsilon\|e^\phi h\|_{H^2}.
\]

### 2.3 Distance functions, cutoffs, and weighted regularity

For arbitrary closed \(B\), the raw function
\[
d(x)=\operatorname{dist}(x,B)
\]
is only Lipschitz. This is sufficient for the form-level Combes–Thomas estimate but not for:

- the pointwise commutator involving \(\Delta\chi\);
- weighted \(H^2\) estimates requiring controlled second derivatives;
- boundary regularity on a level set of \(d\).

One must replace \(d\) by a smooth model-uniform approximation \(\widetilde d\) satisfying, for chosen \(\eta>0\),
\[
|\widetilde d-d|\le C_\eta,\qquad
|\nabla\widetilde d|\le1+\eta,\qquad
|\nabla^2\widetilde d|\le C_\eta.
\]
This can be constructed after lifting to \(\mathbb{CH}^2\), smoothing equivariantly, and descending. Then choose cutoffs from \(\widetilde d\). Any desired final rate \(a<\sqrt2\) is obtained by first choosing \(\eta\) sufficiently small and using an intermediate rate below \(\sqrt2/(1+\eta)\).

For a smooth cutoff,
\[
[L,\chi]h
=-\nabla_{\nabla\chi}h+\frac12(\Delta\chi)h
\]
with the conventions of the note. Uniform weighted elliptic regularity then gives
\[
\|e^\phi u\|_{H^2}
\le C\bigl(\|e^\phi Lu\|_2+\|e^\phi u\|_2\bigr),
\]
where \(C\) depends only on the CH model and the chosen weight bounds, not on \(\Gamma,B,k\).

### 2.4 Absorption

Let
\[
h_1=L^{-1}(\chi\operatorname{Ric}_g^\circ),\qquad
h_2=\chi h-h_1.
\]
Then
\[
Lh_2=-\chi Q(h)+[L,\chi]h.
\]
The global gap and elliptic estimate imply
\[
\|h_1\|_{H^2}
\le C\|\operatorname{Ric}_g^\circ\|_{L^2(d\ge1)}.
\]
For a capped weight \(\phi=a\min(\widetilde d,T)\),
\[
\|e^\phi h_1\|_{H^2}
\le Ce^{aT}\|\operatorname{Ric}_g^\circ\|_2.
\]
The commutator is controlled by the collar norm, while
\[
\|e^\phi\chi Q(h)\|_2
\le C\varepsilon\|e^\phi\chi h\|_{H^2}.
\]
Substitution of \(\chi h=h_1+h_2\) and \(C\varepsilon<1/2\) gives
\[
\|e^\phi h_2\|_{H^2}
\le C\Lambda+
C\varepsilon e^{aT}\|\operatorname{Ric}_g^\circ\|_2.
\]
On the region where \(\chi=1\) and \(\widetilde d\ge T\),
\[
\boxed{
\|h\|_{H^2(d\ge T+O(1))}
\le C\left(
\|\operatorname{Ric}_g^\circ\|_{L^2(d\ge1)}
+e^{-aT}\Lambda
\right).
}
\]
After adjusting the numerical radii in the statement, this is Theorem 48.L.

### 2.5 DeTurck gauge with boundary

The harmonic-map Jacobi operator is indeed
\[
J=\nabla^*\nabla-\operatorname{Ric}
=\nabla^*\nabla+6,
\]
and with zero Dirichlet data on a **smooth regular boundary**
\[
\langle JX,X\rangle=\|\nabla X\|^2+6\|X\|^2.
\]
Thus its coercivity is quotient-independent.

However, the parenthetical claim in 48.L does not prove a uniform Dirichlet gauge for arbitrary regions \(\{d\ge1/2\}\): distance levels may have cut loci, corners, or degenerating boundary charts when \(B\) is an arbitrary union of nonseparated balls. There are two valid formulations:

1. retain Bianchi/DeTurck gauge as an explicit hypothesis; then the localized estimate above is valid; or
2. regularize the region and specify uniformly regular Dirichlet data, or extend/interpolate the metric to the closed quotient and use the global harmonic-map gauge from Step 46.

Accordingly, the decay estimate is sound, but the claimed general boundary gauge construction is not established in the current text.

---

## 3. Lemma 48.5

Let
\[
t=\operatorname{tr}_{g_0}h,\qquad \Delta=\delta d=-\nabla^i\nabla_i.
\]
Besse 1.174, with these conventions, gives
\[
s'_{g_0}(h)
=\Delta t+\delta\delta h-\langle\operatorname{Ric}_0,h\rangle.
\]
In linear Bianchi gauge,
\[
\delta h=-\frac12dt,
\qquad
\delta\delta h=-\frac12\Delta t.
\]
Since \(\operatorname{Ric}_0=-6g_0\),
\[
-\langle\operatorname{Ric}_0,h\rangle=6t.
\]
Therefore
\[
\boxed{s'_{g_0}(h)=\frac12(\Delta+12)t.}
\]

For the nonlinear gauge and exact equality \(s_g=s_{g_0}=-24\),
\[
\frac12(\Delta+12)t=Q_s,
\]
where
\[
|Q_s|\le C\bigl(
|h||\nabla^2h|+|\nabla h|^2+|h|^2
\bigr),
\]
plus an equivalent divergence-form quadratic term from the nonlinear gauge.

Assuming a smooth boundary and outward normal \(\nu\),
\[
\int_\Omega\Delta t=-\int_{\partial\Omega}\partial_\nu t.
\]
Thus
\[
-\frac12\int_{\partial\Omega}\partial_\nu t
+6\int_\Omega t
=O(\|h\|_{H^2(\Omega)}^2),
\]
and hence
\[
\int_\Omega t
=\frac1{12}\int_{\partial\Omega}\partial_\nu t
+O(\|h\|_{H^2(\Omega)}^2).
\]
Since
\[
d\mu_g=\left(1+\frac12t+O(|h|^2)\right)d\mu_0,
\]
one obtains
\[
\boxed{
\operatorname{Vol}_g(\Omega)-\operatorname{Vol}_{g_0}(\Omega)
=\frac1{24}\int_{\partial\Omega}\partial_\nu t
+O(\|h\|_{H^2(\Omega)}^2).
}
\]

Thus the sign and \(1/24\) coefficient are correct **only in the \(s=-24\) scale**. A cutoff formulation is preferable when the interface is not smooth; it converts the boundary flux into a transition-layer term and avoids uncontrolled boundary traces.

---

## 4. Theorem 48.LY

The intended argument is sound only after three corrections.

### 4.1 Radius/collar mismatch

The proof says to invoke 48.L with \(T=1\), but its cutoff is zero for \(d\le1\) and one only for \(d\ge2\). It therefore controls the exterior beginning at \(d=2\), not the whole region
\[
\Omega=\{d\ge1\}.
\]
Moreover,
\[
\Lambda=\|h\|_{H^1(1\le d\le2)}
\]
alone does not give the \(H^2\)-control needed for the volume remainder throughout that annulus.

A clean repair is to set
\[
\Omega_2=\{d\ge2\},\qquad
U_2=M\setminus F(\Omega_2)
\]
and place the flux at \(d=2\). Then
\[
\|h\|_{H^2(\Omega_2)}^2
\le C\bigl(P(\hat g)+\Lambda^2\bigr).
\]
Alternatively, use nested cutoffs so that the volume transition layer lies strictly inside the region on which the localized \(H^2\) estimate is available.

### 4.2 Scale conversion

If \(\hat g\) is the Yamabe metric with \(s_{\hat g}=-4\), define
\[
\widetilde g=\frac16\hat g.
\]
Then \(s_{\widetilde g}=-24\), and Lemma 48.5 applies to \(\widetilde g\) with coefficient \(1/24\).

In scalar-\(-24\) units define
\[
\widetilde{\Delta V}_{U_2}
=
\operatorname{Vol}_{\widetilde g}(U_2)
-\operatorname{Vol}_{g_0}(\{d<2\})
+\frac1{24}\int_{d=2}
\partial_{\nu_0}\operatorname{tr}_{g_0}(\widetilde g-g_0).
\]
The scalar-\(-4\) quantity used by Theorem Y is
\[
\boxed{
\Delta V_{U_2}^{(-4)}
=36\,\widetilde{\Delta V}_{U_2}.
}
\]
Equivalently, writing \(\hat g_0=6g_0\), the scalar-\(-4\) formula is
\[
\boxed{
\Delta V_{U_2}^{(-4)}
=
\operatorname{Vol}_{\hat g}(U_2)
-\operatorname{Vol}_{\hat g_0}(\{d<2\})
+\frac14\int_{d=2}
\partial_{\hat\nu_0}
\operatorname{tr}_{\hat g_0}(\hat g-\hat g_0).
}
\]
Therefore the phrase “in \(\hat g\) units” together with coefficient \(1/24\) is inconsistent. Also, this scalar-normalized volume excess is not intrinsically “scale-invariant”; its scale has been fixed by \(s=-4\).

The integrated Weyl penalty is invariant under the homothety when the Kähler orbit is rescaled consistently:
\[
\mathcal K_{-24}=6\mathcal K_{-4}.
\]

### 4.3 Reference topology

If the reference is an arbitrary ball quotient \(X_0\), then in scalar-\(-4\) units
\[
\operatorname{Vol}(X_0)=2\pi^2 c_1^2(X_0).
\]
The decomposition of the global Yamabe excess therefore contains
\[
2\pi^2\bigl(c_1^2(X_0)-A\bigr).
\]
The theorem as displayed silently requires
\[
c_1^2(X_0)=A,
\]
for example because \(X_0\) is the original ball-quotient host \(X\). If not, that topological correction must be retained.

### 4.4 Corrected inequality

Assume \(c_1^2(X_0)=A\), use a regular interface/nested cutoff, and define the core excess entirely in scalar-\(-4\) units. Then Lemma 48.5 and 48.L imply
\[
\left|\Delta V-\Delta V_{U_2}^{(-4)}\right|
\le C\bigl(P(\hat g)+\Lambda^2\bigr).
\]
Theorem Y gives
\[
8\pi^2k-P(g)
\le4\Delta V-\frac{20}{9}
\int_M\operatorname{dist}(W^+,\mathcal K)^2.
\]
Dropping only the nonpositive bulk Weyl term and using \(P(\hat g)\le P(g)\),
\[
\boxed{
8\pi^2k-P(g)
\le
4\Delta V_{U_2}^{(-4)}
-\frac{20}{9}\int_{U_2}\operatorname{dist}(W^+,\mathcal K)^2
+C\bigl(P(g)+\Lambda^2\bigr).
}
\]
Hence
\[
\boxed{
P(g)\ge
\frac{8\pi^2k-4\Delta V_{U_2}^{(-4)}-C\Lambda^2}{1+C}.
}
\]
If \(c_1^2(X_0)\ne A\), the numerator additionally contains
\[
-\,8\pi^2\bigl(c_1^2(X_0)-A\bigr).
\]

Thus the advertised lower bound is legitimate only in this corrected formulation. The core excess also depends on the chosen exterior identification, gauge, and interface germ; it is a marked relative-volume quantity.

---

## 5. Indicial roots and geometric interpretation

The script forms its displayed determinant from only the spatial equations \(E_{11},E_{22},E_{33}\). A radial-gauge Einstein perturbation must also satisfy \(E_{00}=0\).

### 5.1 Triaxial sector

For
\[
(a,b,c)=(1,-1,0)e^{-\nu r},
\]
the \(00\) and \(33\) rows vanish identically, while the spatial equation is
\[
-\nu(\nu-4)=0.
\]
Thus both roots are genuine:
\[
\boxed{\nu=0,\ 4.}
\]

### 5.2 U(2)-invariant sector

Set \(a=b\). Imposing all four Einstein equations gives
\[
\begin{array}{c|c}
\nu &(a,b,c)\\ \hline
-2 &(1,1,-4/3),\\
0 &(1,1,2),\\
6 &(1,1,-4).
\end{array}
\]
The \(\nu=0\) vector is the asymptotic radial-translation mode, since
\[
A'/A\to1,\qquad C'/C\to2.
\]

At the spatial root \(\nu=8\), the spatial equations require
\[
(a,b,c)=(1,1,2),
\]
but the \(00\) row is
\[
(-48,-48,-32),
\]
whose contraction with \((1,1,2)\) is
\[
-160\ne0.
\]
Therefore
\[
\boxed{\nu=8\text{ is spurious}.}
\]

The corrected table is
\[
\boxed{
\begin{array}{c|c}
\text{sector}&\text{full radial-gauge Einstein roots}\\ \hline
a=-b,\ c=0&0,\ 4,\\
a=b&-2,\ 0,\ 6.
\end{array}}
\]

### 5.3 Integrability

Since the volume density grows like \(e^{4r}\),

- a first-order triaxial perturbation \(q=O(e^{-4r})\) is \(L^1\)-marginal:
  \[
  \int_0^R e^{-4r}e^{4r}\,dr=O(R)
  =O(\log\operatorname{Vol}B_R);
  \]
- the physical decaying U(2) mode \(O(e^{-6r})\) is \(L^1\)-summable:
  \[
  \int_0^\infty e^{-6r}e^{4r}\,dr<\infty.
  \]

This conclusion is established only for the diagonal SU(2)-invariant modes computed by the script.

### 5.4 First variations of \(\mu_{\min}\) and \(|W^+|^2\)

For the pure triaxial family, interchanging the first two SU(2) axes sends its amplitude \(q\) to \(-q\) and preserves the unordered spectrum of \(W^+\). At the CH metric, the lowest eigenvalue is simple, while the upper pair is degenerate. Therefore
\[
\mu_{\min}(q)=\mu_{\min}(-q),
\qquad
|W^+(q)|^2=|W^+(-q)|^2,
\]
and hence
\[
\boxed{
\mu_{\min}(q)-\mu_{\min}(0)=O(q^2),\qquad
|W^+(q)|^2-|W^+(0)|^2=O(q^2).
}
\]
This uses the constant-scalar/Yamabe normalization; without fixing scalar curvature, a first-order scalar contribution can enter.

Thus for \(q=O(e^{-4r})\), the Theorem-Y orbit penalty is quadratic,
\[
\Psi=O(e^{-8r}),
\qquad
\int e^{-8r}e^{4r}\,dr<\infty.
\]

What is **not** established by the supplied computation is the stronger expansion
\[
\operatorname{spec}(W^+)
=
\bigl(\mu_{\min}+O(q^2),\lambda+cq+O(q^2),
\lambda-cq+O(q^2)\bigr),
\qquad c\ne0.
\]
Symmetry permits such a linear splitting but does not prove \(c\ne0\). Consequently, the statement that Theorem K definitely sees a linear marginal \(e^{-4r}\) Weyl departure requires a separate linearized \(W^+\) computation.

Also unproved are:

- the complete indicial spectrum outside the diagonal SU(2)-invariant ansatz;
- nonlinear existence and core matching of these formal tails;
- the assertion that all J-invariant tails in unrestricted sectors decay at least as \(e^{-6r}\);
- absence of additional decaying roots in other tensor harmonics.

---

## Corrected status of §3

The global tensor gap and Combes–Thomas mechanism are rigorous and quotient-uniform. Localized nonlinear coercivity follows once gauge is assumed and the distance/cutoff construction is regularized. The volume linearization is correct at the \(\operatorname{Ric}=-6\) scale. The near-CH reduction to cores survives, but only after:

1. using compatible exterior and collar radii;
2. defining the core excess consistently at one scalar normalization;
3. requiring \(c_1^2(X_0)=A\) or retaining the resulting topological correction;
4. treating the DeTurck gauge construction separately from the coercive estimate.

The principal unresolved geometric object remains a bound on the corrected marked core excess \(\Delta V_U\), together with a complete asymptotic spectrum and the explicit first-order Weyl splitting of the triaxial \(\nu=4\) mode.
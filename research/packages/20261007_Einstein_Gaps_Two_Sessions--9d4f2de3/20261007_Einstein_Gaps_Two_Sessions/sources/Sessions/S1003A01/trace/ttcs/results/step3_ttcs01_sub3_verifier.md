# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_localization_and_coupled_filling.md",
    "Sessions/S1003A01/workspace/notes/step2_cell_problem_and_triaxial_numerics.md"
  ]
}
```

## Task

Independently check the proposed C1 sharpening and assess the most promising rigorous mechanism in the actual conformal triaxial profile class. Verify algebraically that subtracting the conformally Kähler lower bound from I54 (6.6) yields exactly A0/12+4B0+(1/4)∫(s_G+4)^2 - N(2m0-3N)/(4vK), identify any hidden conformal-factor or normalization issue, and compare this with I55's radial decomposition (8.2) and scalar moment (8.6). Look for a fatal counter-scaling or, if none, formulate the strongest coercive lemma that would close the middle window. Also evaluate why a general bubble-compactness program does not yet imply the 8π² charge, accounting for orbifold bases, quotient-ended ALE bubbles, and marked relative topology. Ground every conclusion in the supplied files.

## Output

## Scientific verification memo

### 1. Exact subtraction of the Kähler-area term

Write
\[
L_G=\int_C(s_G+4)^2,\qquad
v_K=d-\frac12T_2,\qquad
m_0=4d+4\pi T_1,
\]
where \(T_1=\sum_i t_i\) and \(T_2=\sum_i t_i^2\). The scalar-free part of the conformally Kähler estimate in I54 (4.1) is
\[
\mathcal K
=8\pi^2k+8\pi T_1+2T_2
+\frac{(2\pi T_1+T_2)^2}{v_K}.
\]
A direct expansion gives the equivalent form
\[
\boxed{\mathcal K=8\pi^2k-4d+\frac{m_0^2}{4v_K}.}
\]
Indeed,
\[
-4d+\frac{4(d+\pi T_1)^2}{d-T_2/2}
=
8\pi T_1+2T_2+
\frac{(2\pi T_1+T_2)^2}{d-T_2/2}.
\]

I54 (6.6) reads
\[
J(G)-8\pi^2k
=-4d+\frac{m_0^2}{6v_K}
+\frac{3}{4v_K}\left(N-\frac{m_0}{3}\right)^2
+\frac{A_0}{12}+4B_0+\frac14L_G.
\]
The first two \(m_0,N\) terms satisfy
\[
\frac{m_0^2}{6v_K}
+\frac{3}{4v_K}\left(N-\frac{m_0}{3}\right)^2
=
\frac{m_0^2}{4v_K}
-\frac{N(2m_0-3N)}{4v_K}.
\]
Consequently
\[
\boxed{
J(G)-\mathcal K
=
\frac{A_0}{12}+4B_0+\frac14L_G
-\frac{N(2m_0-3N)}{4v_K}.
}
\]

Thus the subtraction requested in the task is algebraically exact.

There is one terminological distinction. The full right side of I54 (4.1) is \(\mathcal K+\frac14L_G\). Subtracting that full expression would give
\[
J(G)-\left(\mathcal K+\frac14L_G\right)
=
\frac{A_0}{12}+4B_0
-\frac{N(2m_0-3N)}{4v_K}.
\]
C1 only asserts \(J\ge\mathcal K\), so its required coercivity includes the scalar square \(L_G/4\). It is therefore weaker than extending the complete remainder form of I54 (4.1).

Since \(A_0,B_0,L_G\ge0\), C1 is automatic when \(N\ge2m_0/3\). Its substantive interval is
\[
0<N<\frac{2m_0}{3},
\]
where almost-Kähler nonintegrability lowers the forced Weyl contribution.

---

### 2. One-bolt normalization and the role of the conformal representative

For the radial one-bolt cell of I55, let \(r_0^2=\mu\), and truncate at any \(R\) lying in the exact CH collar. Then
\[
t_E=\pi\mu,\qquad
d_R=\frac{\pi^2R^4}{2},\qquad
v_K=\frac{\pi^2}{2}(R^4-\mu^2),
\]
and
\[
m_0=4d_R+4\pi t_E=2\pi^2(R^4+2\mu).
\]
For \(k=1\),
\[
\mathcal K
=\frac{2d_R(2\pi+t_E)^2}{v_K},
\]
so
\[
\boxed{
\frac{\mathcal K}{2\pi^2}
=
\frac{(2+\mu)^2R^4}{R^4-\mu^2}.
}
\]
This is exactly the proposed C1 constant.

Two normalization points matter:

1. I54 initially writes \(K=u^2G\), whereas I55 writes \(G=e^{2\phi}K\). Thus
   \[
   u=e^{-\phi}.
   \]
   The conformal Dirichlet term has not disappeared: with
   \[
   H=6\int_C|du|_G^2\,dV_G,
   \]
   one has in radial variables
   \[
   \frac{H}{2\pi^2}=6G_\phi,\qquad
   G_\phi=\int r^3F(\phi')^2\,dr.
   \]
   It is incorporated in the explicit formula for \(A_0\) in I54 (6.7a).

2. The quantities \(\mu,t_E,v_K,m_0,N\) belong to the canonical almost-Kähler representative \(K\), not directly to \(G\). In particular, \(\pi\mu\) is the \(K\)-area of the exceptional sphere; its \(G\)-area is changed by \(\phi(r_0)\). Within the diagonal ansatz this causes no ambiguity because the collar normalization uniquely fixes the conformal representative \(K\).

Choosing \(R\) inside the exact CH collar is legitimate: the exterior annulus has \(\operatorname{Ric}+g=0\), so it contributes zero to \(J\), and the inner piece is itself a complete relative cell with a full CH metric germ at \(R\). The numerical C1 constant depends on this truncation; the smallest admissible collar radius gives the strongest version.

---

### 3. Exact comparison with the radial decomposition

Define
\[
M_0=1+\frac2\mu,\qquad
q=T_\phi-P_w,\qquad
M=M_0-q,
\]
and
\[
I_R=\frac14(\mu^{-2}-R^{-4}).
\]
Then
\[
\frac{M_0^2}{4I_R}
=
\frac{(2+\mu)^2R^4}{R^4-\mu^2},
\]
which is again the C1 constant.

Let
\[
\begin{aligned}
\mathscr R_{\rm rad}={}&
\frac14\int r^3\left(X-\frac{M}{I_Rr^4}\right)^2dr
+\frac14\int r^3Y^2dr\\
&+\frac12\int r^3Z^2dr
+2\int r^3V_w^2dr .
\end{aligned}
\]
I55 (8.2) is precisely
\[
j:=\frac{J}{2\pi^2}
=\frac{M^2}{4I_R}+\mathscr R_{\rm rad}.
\]
Since \(M=M_0-q\),
\[
M_0^2-M^2=q(2M_0-q),
\]
and hence
\[
\boxed{
j-\frac{(2+\mu)^2R^4}{R^4-\mu^2}
=
\mathscr R_{\rm rad}
-\frac{q(2M_0-q)}{4I_R}.
}
\]
This is the radial counterpart of the I54 subtraction.

Thus C1 is equivalent to the coupled estimate
\[
\boxed{
\mathscr R_{\rm rad}
\ge
\frac{(T_\phi-P_w)\,[\,2(1+2/\mu)-(T_\phi-P_w)\,]}{4I_R}
}
\]
whenever
\[
0<T_\phi-P_w<2\left(1+\frac2\mu\right).
\]
Outside this interval the right side is at most zero and I55 (8.2) already suffices.

The radial moment \(P_w\) is not the same object as \(N\). With \(n=N/(2\pi^2)\),
\[
n
=2\int r^3F
\left(w'+\frac{2\sinh(2w)}{rF}\right)^2dr.
\]
After integrating the cross term and using \(w=0\) at both endpoints,
\[
n
=
2\int r^3F(w')^2dr
-8\int r(\cosh 2w-1)\,dr
+8\int\frac{r\sinh^2(2w)}{F}\,dr.
\]
By contrast,
\[
P_w=\int\left[
\frac{2F(w')^2}{r}
+\frac{8(\cosh2w-1)}{r^3}
+\frac{8\sinh^2(2w)}{r^3F}
\right]dr.
\]
They use different radial weights, and the integrated form of \(N\) contains a subtractive middle term. Replacing one by the other would be an algebraic error.

For completeness, with
\[
\bar v=\frac{R^4-\mu^2}{4},\qquad
m=R^4+2\mu,\qquad n=\frac{N}{2\pi^2},
\]
the two exact decompositions imply
\[
\begin{aligned}
\mathscr R_{\rm rad}
-\frac{q(2M_0-q)}{4I_R}
={}&
\frac{A_0}{24\pi^2}
+\frac{2B_0}{\pi^2}
+\frac{L_G}{8\pi^2}\\
&-\frac{n(2m-3n)}{4\bar v}.
\end{aligned}
\]
This identity confirms that the two descriptions are normalized consistently.

---

### 4. What the scalar moment does and does not control

Because
\[
Y=e^{2\phi}(s_G+4),\qquad dV_K=2\pi^2r^3dr,
\]
one has
\[
L_G=2\pi^2\int r^3Y^2dr.
\]
The scalar zeroth moment from I55 (8.6) is
\[
L_Y:=\int r^3Y\,dr
=
4B_\phi-\mu^2-2\mu-n-6G_\phi,
\]
with
\[
\frac{\mu^2}{2}T_\phi\le G_\phi\le\frac{R^4}{2}T_\phi.
\]
The exact orthogonal splitting is
\[
\frac14\int r^3Y^2dr
=
\frac{L_Y^2}{R^4-\mu^2}
+
\frac14\int r^3
\left(Y-\frac{4L_Y}{R^4-\mu^2}\right)^2dr.
\]

This scalar moment cannot by itself control the C1 deficit:

- \(q=T_\phi-P_w\) uses an \(r^{-1}\)-weighted conformal gradient.
- \(L_Y\) sees \(G_\phi\), which uses the much softer \(r^3\) weight.
- \(B_\phi\), \(n\), and \(G_\phi\) enter the same moment and may compensate one another.

The explicit zero-moment construction in I55 §8.1 makes this decisive. There,
\[
w=0,\qquad P_w=0,\qquad T_\phi=1+\frac2\mu,
\]
so
\[
q=M_0,\qquad M=0.
\]
The first radial moment term in (8.2) vanishes completely, yet the metric remains above \(8\pi^2\), and in fact above the conformally Kähler area term by I54. Its cost is carried by the remaining \(X,Y,Z\) squares. Any argument based only on keeping \(M\) away from zero, or only on \(L_Y\), cannot establish C1.

The scaling behind that example is also informative. For
\[
\phi(r)=a\,\eta(r/\sqrt\mu)
\]
supported at \(r\asymp\sqrt\mu\),
\[
T_\phi\asymp\frac{a^2}{\mu},
\qquad
G_\phi\asymp a^2\mu,
\qquad
B_\phi\asymp\mu^2.
\]
Thus a conformal payment of order \(\mu^{-1}\) can coexist with a small scalar zeroth moment. The second-derivative residuals \(X,Z\) remain of order one after integration, which is exactly where the missing coercivity can reside.

No fatal counter-scaling is exhibited in the supplied material:

- For \(w=0\), I54 Theorem 1 already proves the desired estimate.
- For \(\phi=0\), I55 (8.3) proves a stronger estimate.
- I55 §7 gives positivity of the full quadratic form around the cutoff recovery; its linear optimization saves only \(O(\mu^2)\), while the Kähler-area excess is \(4\mu+O(\mu^2)\).
- I55 Proposition 6 shows that a fixed descent below \(j=4\) needs both microscopic conformal energy and modification of a CH region of nonvanishing background volume.

What remains possible from the present formulas is an \(O(\mu)\) descent from the C1 value while staying above \(4\). Proposition 6 does not address that finer scale. The numerical results and the Hessian calculation give substantial evidence against it, but the exact finite-amplitude estimate is still absent.

---

### 5. The sharp coupled coercive lemma

The cleanest rigorous target in the actual profile variables is obtained by retaining every square in (8.2) and the full scalar splitting. Put
\[
\bar Y=\frac{4L_Y}{R^4-\mu^2}.
\]
Then the following lemma is exactly equivalent to C1:

> **Coupled radial coercivity.** For every smooth admissible profile triple \((F,w,\phi)\), with the ordinary-bolt data and exact CH collar of I55, and whenever
> \[
> 0<q:=T_\phi-P_w<2M_0,\qquad M_0=1+\frac2\mu,
> \]
> one has
> \[
> \begin{aligned}
> &\frac14\int r^3\left(X-\frac{M_0-q}{I_Rr^4}\right)^2dr
> +\frac{L_Y^2}{R^4-\mu^2}
> +\frac14\int r^3(Y-\bar Y)^2dr\\
> &\qquad
> +\frac12\int r^3Z^2dr
> +2\int r^3V_w^2dr\\
> &\hspace{35mm}\ge
> \frac{q(2M_0-q)}{4I_R}.
> \end{aligned}
> \]

No moment has been discarded here. The quantities on both sides are formed from the same \(F,w,\phi\), and the lemma automatically includes the scalar relation
\[
L_Y=4B_\phi-\mu^2-2\mu-n-6G_\phi.
\]

For the weaker goal \(J\ge8\pi^2\), only the interval (8.4) matters, and the required estimate is
\[
\mathscr R_{\rm rad}
\ge
4-\frac{M^2}{4I_R}.
\]
C1 replaces \(4\) by the strictly larger Kähler-area value \(M_0^2/(4I_R)\).

The radial decomposition is the most promising mechanism among the supplied approaches because it converts every unresolved interaction into explicit squares of the same profiles. The I54 remainder form identifies the geometric source—the competition between \(N\), scalar transfer, and the self-dual Weyl variance—but \(A_0\) and \(B_0\) are less directly accessible analytically. In the radial representation, a plausible coercive mechanism is a nonlinear Hardy–ODE estimate coupling:

- the \(r^{-1}\)-weighted quantity \(T_\phi-P_w\),
- the scalar mode and scalar fluctuation in \(Y\),
- the conformal radial equation in \(Z\),
- the anisotropic equation in \(V_w\),
- and the orthogonal part of \(X\).

The terminal-value estimate I55 (5.4) supplies this structure on fixed outer annuli. Near the bolt, the natural rescaling \(r=\sqrt\mu\,x\) preserves the relevant square energies. A matched inner coercivity plus the outer terminal estimate would directly address the two-scale behavior exposed by Proposition 6.

---

### 6. Why generic bubble compactness does not yet yield an \(8\pi^2\) charge

The conditional argument in the step note is valid only for a very specific degeneration: a smooth limiting cell plus AE bubbles with trivial group at infinity, with each lost marked exceptional class carried by an \(O(-1)\) bubble. A general four-dimensional bubble tree permits substantially more.

#### 6.1 Quotient-ended ALE bubbles

For an ALE bubble \(B\) asymptotic to \(\mathbb R^4/\Gamma\), define the eta convention by
\[
\frac1{12\pi^2}\int_B(|W^+|^2-|W^-|^2)
=\tau(B)+\eta(S^3/\Gamma).
\]
Combining this with ALE Gauss–Bonnet gives
\[
\begin{aligned}
\int_B|\operatorname{Ric}^\circ|^2
={}&2\int_B\left(2|W^+|^2+\frac{s^2}{24}\right)\\
&-8\pi^2
\left[
2\left(\chi(B)-\frac1{|\Gamma|}\right)
+3\left(\tau(B)+\eta(S^3/\Gamma)\right)
\right].
\end{aligned}
\]
For \(\Gamma=\{1\}\) and \(B=O(-1)\), the bracket equals \(-1\), recovering the step-note estimate
\[
\int_B|\operatorname{Ric}|^2\ge8\pi^2.
\]

For a quotient end, however, the \(1/|\Gamma|\) and eta terms alter the charge. Ricci-flat ALE spaces can carry nontrivial \(H_2\) while
\[
\int_B|\operatorname{Ric}|^2=0.
\]
Eguchi–Hanson, with its \(-2\) sphere and \(\Gamma=\mathbb Z_2\), is the basic model. Thus “one bubble class costs \(8\pi^2\)” is not available for arbitrary ALE trees. The bubble-scale limit of \(J=\int|\operatorname{Ric}+g|^2\) is precisely \(\int|\operatorname{Ric}|^2\); the \(2s\) and volume terms vanish under shrinking rescaling, so Ricci-flat ALE topology is invisible to the bubble part of \(J\).

#### 6.2 Orbifold bases

I54 Proposition 2 excludes a smooth stationary cell. If a regularized minimizing sequence converges instead to an orbifold base, the same local Euler–Lagrange and unique-continuation argument can force the regular part to be locally CH. It does not convert the orbifold into a smooth CH manifold.

The final contradiction in Proposition 2 uses smooth topology: an exceptional sphere or the relation \(\chi-3\tau=-2\ell\) contradicts a smooth closed locally CH manifold. For an orbifold, Euler number and signature acquire local group corrections, and exceptional classes may arise only after resolving singular points. A locally CH orbifold base together with Ricci-flat ALE resolutions is therefore not excluded by Proposition 2 alone.

#### 6.3 Marked relative topology

The cell carries more information than its unmarked Betti numbers:
\[
C=D\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3)
\]
with a fixed outer germ and marked exceptional and handle topology. To infer an \(8\pi^2q\) charge from a bubble tree, one needs a relative topological decomposition showing where each marked generator goes.

That decomposition is delicate:

- Quotient-ended ALE bubbles usually carry resolution lattices such as \(-2\) chains rather than primitive \(-1\) classes.
- Such root lattices can embed into \(-I_k\) when several blowups are present, leaving complementary rational data on the orbifold base.
- Handle topology is detected through \(H_1\) and fundamental-group data and may enter collapsing necks rather than isolated ALE \(H_2\)-bubbles.
- Lens-space links and their eta terms couple the topology of the base and bubbles; bubble energies cannot be charged separately without this bookkeeping.

Even for one marked \(-1\) class, obtaining a trivial end group requires a primitive relative-homology argument plus exclusion of collapse. Those conclusions are not supplied by an \(L^2\) curvature bound alone.

#### 6.4 Analytic compactness

I54 (7.2) gives a total volume window for subthreshold cells,
\[
\frac{4d}{9}<\operatorname{Vol}(C)<4d,
\]
but this does not control local volume ratios, injectivity radius, diameter, or collapsed regions. Generic near-minimizers of \(J\) are not critical metrics, so the usual epsilon-regularity theory for critical quadratic-curvature metrics does not immediately apply. A regularization such as
\[
J_\varepsilon=J+\varepsilon\int|\mathrm{Rm}|^p,\qquad p>2,
\]
would still require estimates uniform as \(\varepsilon\to0\), an energy identity, and preservation of the marked relative topology.

Accordingly, an energy identity of the form
\[
J_{\inf}\ge J(C_\infty)+\sum_\beta E(B_\beta)
\]
is not enough by itself. The smooth-base/AE-\(O(-1)\) case gives the desired charge, but an orbifold base plus quotient-ended Ricci-flat ALE bubbles can carry topology with little or no bubble Ricci energy. The missing theorem must combine analytic compactness with orbifold Chern–Weil corrections and a marked relative-lattice decomposition.

---

### Overall assessment

The C1 subtraction is correct after interpreting “conformally Kähler lower bound” as its scalar-free Kähler-area term \(\mathcal K\). There is no hidden factor of \(2\pi^2\) or omitted conformal Dirichlet term. The two points requiring explicit wording are that \(\mu\) belongs to the canonical almost-Kähler representative and that subtracting the full I54 (4.1) expression would remove \(L_G/4\).

Among the supplied methods, I55 (8.2) provides the strongest rigorous framework. It reduces C1 to one exact nonlinear coercive inequality involving \(X,Y,Z,V_w\) and \(T_\phi-P_w\). The scalar moment (8.6) is useful only as one component of that inequality; the supplied zero-moment example proves that it cannot carry the argument alone. No supplied scaling produces a counterexample, although \(r\asymp\sqrt\mu\) concentration leaves an unresolved \(O(\mu)\) regime.

The general bubble program remains insufficient for the \(8\pi^2\) charge because the AE \(O(-1)\) calculation does not extend termwise to orbifold bases and quotient-ended ALE bubbles, and because the marked exceptional and handle topology has not been shown to split among the limiting pieces.
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 3,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step3_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step3_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the proposed C1 sharpening and assess the most promising rigorous mechanism in the actual conformal triaxial profile class. Verify algebraically that subtracting the conformally Kähler lower bound from I54 (6.6) yields exactly A0/12+4B0+(1/4)∫(s_G+4)^2 - N(2m0-3N)/(4vK), identify any hidden conformal-factor or normalization issue, and compare this with I55's radial decomposition (8.2) and scalar moment (8.6). Look for a fatal counter-scaling or, if none, formulate the strongest coercive lemma that would close the middle window. Also evaluate why a general bubble-compactness program does not yet imply the 8π² charge, accounting for orbifold bases, quotient-ended ALE bubbles, and marked relative topology. Ground every conclusion in the supplied files.

## Integrated Scientific Memo

## Verification memo: C1, radial coercivity, and the limits of bubbling

### 1. Exact subtraction from I54 (6.6)

For the \(k\)-point conformal almost-Kähler filling, set
\[
v_K=d-\frac12T_2,\qquad m_0=4d+4\pi T_1,\qquad
L_G=\int_C(s_G+4)^2,
\]
where \(T_1=\sum_i t_i\), \(T_2=\sum_i t_i^2\). The scalar-free part of the conformally Kähler bound I54 (4.1) is
\[
\mathcal K
=8\pi^2k+8\pi T_1+2T_2
+\frac{(2\pi T_1+T_2)^2}{v_K}.
\]
It is exactly
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

I54 (6.6) gives
\[
J(G)-8\pi^2k
=-4d+\frac{m_0^2}{6v_K}
+\frac{3}{4v_K}\left(N-\frac{m_0}{3}\right)^2
+\frac{A_0}{12}+4B_0+\frac14L_G.
\]
The quadratic part expands as
\[
\frac{m_0^2}{6v_K}
+\frac{3}{4v_K}\left(N-\frac{m_0}{3}\right)^2
=
\frac{m_0^2}{4v_K}
-\frac{N(2m_0-3N)}{4v_K}.
\]
Therefore
\[
\boxed{
J(G)-\mathcal K
=
\frac{A_0}{12}+4B_0+\frac14L_G
-\frac{N(2m_0-3N)}{4v_K}.
}
\]

Thus the proposed C1 subtraction is algebraically correct.

A wording distinction matters. The **full** right side of I54 (4.1) is
\[
\mathcal K+\frac14L_G.
\]
Subtracting that full bound yields instead
\[
J(G)-\left(\mathcal K+\frac14L_G\right)
=
\frac{A_0}{12}+4B_0
-\frac{N(2m_0-3N)}{4v_K}.
\]
C1 asks only for \(J\ge\mathcal K\), so its coercivity legitimately includes \(L_G/4\). It is weaker than extending the complete remainder form of Theorem 1.

The nonintegrability term is dangerous only for
\[
0<N<\frac{2m_0}{3}.
\]
Outside this interval \(N(2m_0-3N)\le0\), and nonnegativity of \(A_0,B_0,L_G\) proves C1 immediately.

---

### 2. One-bolt normalization and conformal-factor bookkeeping

For the one-bolt radial cell, write
\[
r_0^2=\mu,\qquad t_E=\pi\mu,
\]
and choose \(R\) in the exact CH collar. The CH ball truncated at \(R\) has
\[
d_R=\frac{\pi^2R^4}{2},\qquad
v_K=\frac{\pi^2}{2}(R^4-\mu^2),
\]
and
\[
m_0=4d_R+4\pi t_E=2\pi^2(R^4+2\mu).
\]
For \(k=1\),
\[
\mathcal K=\frac{2d_R(2\pi+t_E)^2}{v_K},
\]
hence
\[
\boxed{
\frac{\mathcal K}{2\pi^2}
=\frac{(2+\mu)^2R^4}{R^4-\mu^2}.
}
\]
This is exactly the proposed C1 constant.

There is no missing factor of \(2\pi^2\), but two normalization issues must remain explicit:

1. I54 writes \(K=u^2G\), while I55 writes \(G=e^{2\phi}K\). Thus
   \[
   u=e^{-\phi}.
   \]
   The conformal Dirichlet energy has not been omitted. If
   \[
   H=6\int_C|du|_G^2\,dV_G,
   \]
   then in the radial variables
   \[
   \frac{H}{2\pi^2}=6G_\phi,\qquad
   G_\phi=\int r^3F(\phi')^2\,dr.
   \]
   This contribution is incorporated in \(A_0\), as displayed in I54 (6.7a).

2. The quantities \(\mu,t_E,v_K,m_0,N\) refer to the canonical almost-Kähler representative \(K\), not directly to \(G\). In particular, \(t_E=\pi\mu\) is the \(K\)-area of the exceptional sphere; the \(G\)-area depends on \(\phi(r_0)\). In the diagonal ansatz this is unambiguous because the CH collar normalization uniquely determines \(K\).

Truncating at any \(R\) inside the full CH collar is legitimate: the removed outer annulus has \(\operatorname{Ric}+g=0\), and the truncated piece still has a full CH metric germ at its boundary. The C1 constant depends on that chosen truncation radius; the innermost admissible \(R\) gives the strongest bound.

---

### 3. Exact relation to I55 (8.2)

Set
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
\boxed{
\frac{M_0^2}{4I_R}
=\frac{(2+\mu)^2R^4}{R^4-\mu^2}.
}
\]

Define the radial remainder
\[
\begin{aligned}
\mathscr R_{\rm rad}:={}&
\frac14\int r^3
\left(X-\frac{M}{I_Rr^4}\right)^2dr
+\frac14\int r^3Y^2dr\\
&+\frac12\int r^3Z^2dr
+2\int r^3V_w^2dr .
\end{aligned}
\]
I55 (8.2) is
\[
j:=\frac{J}{2\pi^2}
=\frac{M^2}{4I_R}+\mathscr R_{\rm rad}.
\]
Since
\[
M_0^2-M^2=q(2M_0-q),
\]
one obtains the exact C1-deficit formula
\[
\boxed{
j-\frac{(2+\mu)^2R^4}{R^4-\mu^2}
=
\mathscr R_{\rm rad}
-\frac{q(2M_0-q)}{4I_R}.
}
\]
Thus C1 is equivalent to
\[
\boxed{
\mathscr R_{\rm rad}\ge
\frac{(T_\phi-P_w)
\left[2(1+2/\mu)-(T_\phi-P_w)\right]}{4I_R}
}
\]
on the only nontrivial interval
\[
0<T_\phi-P_w<2\left(1+\frac2\mu\right).
\]
Outside it the right-hand side is nonpositive, so (8.2) already proves C1.

This is the radial version of the I54 subtraction. In normalized variables
\[
\bar v=\frac{R^4-\mu^2}{4},\qquad
m=R^4+2\mu,\qquad
n=\frac{N}{2\pi^2},
\]
the two decompositions agree through
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

A crucial warning is that \(P_w\) is not a radial rewriting of \(N\). From I54 (6.4),
\[
n=2\int r^3F
\left(w'+\frac{2\sinh(2w)}{rF}\right)^2dr.
\]
After integrating the cross term and using the endpoint conditions,
\[
n=
2\int r^3F(w')^2dr
-8\int r(\cosh2w-1)\,dr
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
The weights differ, and the integrated formula for \(N\) has a negative middle term. Any replacement of \(N\) by \(P_w\) would be invalid.

---

### 4. What the scalar moment (8.6) contributes

Because
\[
Y=e^{2\phi}(s_G+4),\qquad dV_K=2\pi^2r^3dr,
\]
one has
\[
L_G=2\pi^2\int r^3Y^2\,dr.
\]
I55 (8.6) gives
\[
L_Y:=\int r^3Y\,dr
=
4B_\phi-\mu^2-2\mu-n-6G_\phi,
\]
where
\[
\frac{\mu^2}{2}T_\phi\le G_\phi\le\frac{R^4}{2}T_\phi.
\]
The scalar square splits exactly as
\[
\frac14\int r^3Y^2dr
=
\frac{L_Y^2}{R^4-\mu^2}
+\frac14\int r^3
\left(Y-\frac{4L_Y}{R^4-\mu^2}\right)^2dr.
\]

This is useful, but cannot alone control the C1 deficit:

- \(q=T_\phi-P_w\) contains an \(r^{-1}\)-weighted conformal-gradient moment.
- \(L_Y\) contains \(G_\phi=\int r^3F(\phi')^2dr\), a much softer weight near the bolt.
- \(B_\phi,n,G_\phi\) can compensate in the same zeroth moment.

The genuine smooth zero-moment test of I55 §8.1 makes the obstruction precise. For \(w=0\) and
\[
\phi(r)=a_\mu\eta(r/\sqrt\mu),
\]
one can arrange
\[
P_w=0,\qquad T_\phi=1+\frac2\mu,\qquad M=0.
\]
Thus the first term in (8.2) vanishes, while the metric remains above the conformally Kähler lower bound. Its cost is carried by the remaining \(X,Y,Z\) squares. Therefore neither a lower bound on \(|M|\) nor an estimate using only \(L_Y\) can prove C1.

The associated scaling is
\[
T_\phi\asymp\frac{a^2}{\mu},\qquad
G_\phi\asymp a^2\mu,\qquad
B_\phi\asymp\mu^2.
\]
Hence a large \(r^{-1}\)-weighted conformal payment can coexist with a small scalar zeroth moment. The second-derivative residuals \(X,Z\), rather than the zeroth moment, carry the missing coercivity.

---

### 5. Counter-scaling assessment

No fatal counter-scaling appears in the supplied material.

- For \(w=0\), I54 Theorem 1 already proves C1.
- For \(\phi=0\), I55 (8.3) proves
  \[
  j\ge\frac{(\mu+2+\mu P_w)^2}{1-\mu^2/R^4},
  \]
  which is stronger than C1.
- I55 §7 proves positivity of the full coupled Hessian around the cutoff recovery. Optimizing the linear error can save only \(O(\mu^2)\), whereas the Kähler-area excess is
  \[
  4\mu+O(\mu^2).
  \]
- I55 Proposition 6 shows that any fixed improvement \(j\le4-\epsilon\) requires both:
  1. conformal energy concentrating at microscopic radii, with \(\mu T_\phi\) bounded below;
  2. modification of a CH background region of nonvanishing volume.

The remaining unresolved possibility is finer: an \(O(\mu)\) decrease from the C1 value while still remaining above \(4\). Proposition 6 does not exclude such a descent because it addresses a fixed subthreshold improvement. The numerical evidence and local Hessian computation argue against it, but they do not supply the finite-amplitude inequality.

---

### 6. Strongest coercive lemma closing the middle window

Let
\[
q=T_\phi-P_w,\qquad M_0=1+\frac2\mu,\qquad
M=M_0-q,
\]
and
\[
\bar Y=\frac{4L_Y}{R^4-\mu^2}.
\]
The sharp radial statement equivalent to C1 is:

> **Coupled radial coercivity lemma.**  
> For every admissible smooth profile triple \((F,w,\phi)\) with ordinary-bolt data and an exact CH collar, if
> \[
> 0<q<2M_0,
> \]
> then
> \[
> \begin{aligned}
> &\frac14\int r^3
> \left(X-\frac{M}{I_Rr^4}\right)^2dr
> +\frac{L_Y^2}{R^4-\mu^2}
> +\frac14\int r^3(Y-\bar Y)^2dr\\
> &\qquad
> +\frac12\int r^3Z^2dr
> +2\int r^3V_w^2dr\\
> &\hspace{28mm}\ge
> \frac{q(2M_0-q)}{4I_R},
> \end{aligned}
> \]
> where
> \[
> L_Y=4B_\phi-\mu^2-2\mu-n-6G_\phi.
> \]

This retains every square from (8.2) and the exact scalar relation (8.6); it does not optimize incompatible moments independently. It is precisely equivalent to
\[
\frac{J(G)}{2\pi^2}\ge
\frac{(2+\mu)^2R^4}{R^4-\mu^2}.
\]

For the weaker target \(J\ge8\pi^2\), it suffices on I55’s middle interval (8.4) to prove
\[
\mathscr R_{\rm rad}\ge4-\frac{M^2}{4I_R}.
\]

Among the supplied mechanisms, this radial form is the most promising because all unresolved terms are explicit differential residuals of the same profiles. The natural proof structure would combine:

- an outer terminal-value estimate of the type I55 (5.4), using \(w=\phi=0\) on the full collar;
- inner rescaling \(r=\sqrt\mu\,x\), where the bolt-concentrated conformal modes remain visible;
- a nonlinear Hardy/ODE estimate coupling \(T_\phi-P_w\) to \(X,Z,V_w\);
- the exact scalar mean and variance splitting for \(Y\).

The I54 formulation identifies the geometry—nonintegrability can reduce the forced \(W^+\) budget—but \(A_0,B_0\) are less directly coercive than the radial residuals.

---

### 7. Why general bubble compactness does not yet give \(8\pi^2\) per charge

The conditional bubbling argument in the session note works only under a restrictive outcome: a smooth limiting cell plus AE bubbles with trivial group at infinity, each lost primitive exceptional class carried by an \(O(-1)\) bubble. General four-dimensional compactness does not ensure this.

#### 7.1 Quotient-ended ALE bubbles

For an ALE bubble asymptotic to \(\mathbb R^4/\Gamma\), Gauss–Bonnet and APS signature include the corrections
\[
\frac1{|\Gamma|},\qquad \eta(S^3/\Gamma).
\]
With the convention
\[
\frac1{12\pi^2}\int_B(|W^+|^2-|W^-|^2)
=\tau(B)+\eta(S^3/\Gamma),
\]
one obtains
\[
\begin{aligned}
\int_B|\operatorname{Ric}^{\circ}|^2
={}&2\int_B\left(2|W^+|^2+\frac{s^2}{24}\right)\\
&-8\pi^2\left[
2\left(\chi(B)-\frac1{|\Gamma|}\right)
+3\left(\tau(B)+\eta(S^3/\Gamma)\right)
\right].
\end{aligned}
\]
For the trivial-ended \(O(-1)\) bubble, the bracket is \(-1\), recovering the \(8\pi^2\) lower charge.

For quotient ends the correction changes the charge. In particular, Ricci-flat ALE spaces may carry nontrivial \(H_2\) while
\[
\int_B|\operatorname{Ric}|^2=0.
\]
Thus topology can appear in a quotient-ended ALE bubble without paying \(8\pi^2\) in the blow-up limit of \(J\). Under shrinking rescaling,
\[
J=\int|\operatorname{Ric}+g|^2
\]
reduces to \(\int|\operatorname{Ric}|^2\); the scalar-linear and volume terms vanish at bubble scale.

#### 7.2 Orbifold bases

I54 Proposition 2 excludes a smooth stationary cell. A regularized minimizing sequence may instead converge to an orbifold base. Unique continuation can force its regular part to be locally CH, but this does not make the base a smooth CH manifold.

The final contradiction in Proposition 2 uses smooth topology. For an orbifold, Euler characteristic and signature contain local isotropy corrections, and exceptional topology may emerge only after resolving singularities. A locally CH orbifold base together with Ricci-flat ALE resolution bubbles is therefore not ruled out by the smooth nonattainment argument.

#### 7.3 Marked relative topology

The cell contains marked relative data, not merely unmarked Betti numbers:
\[
C=D\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
\]
with a fixed outer germ. To recover an \(8\pi^2q\) charge, one must prove where each marked exceptional or handle generator goes in the degeneration.

This is not automatic:

- quotient-ended ALE bubbles often carry \(-2\) root lattices rather than primitive \(-1\) classes;
- such lattices may embed into the negative diagonal lattice of several blowups, with complementary rational data retained by the orbifold base;
- handle topology may enter collapsing necks or fundamental-group degeneration rather than isolated \(H_2\)-bubbles;
- lens-space interfaces and eta invariants couple the base and bubble topologies, so their charges cannot be assigned independently.

Even for one marked \(-1\) class, forcing a trivial-end \(O(-1)\) bubble requires a primitive relative-homology argument and exclusion of collapse.

#### 7.4 Analytic gap

I54 (7.2) gives only the total-volume window
\[
\frac{4d}{9}<\operatorname{Vol}(C)<4d
\]
for a subthreshold cell. It does not control local volume ratios, injectivity radius, diameter, or collapse.

Moreover, arbitrary minimizing sequences for \(J\) are not critical metrics. Standard \(\varepsilon\)-regularity for critical quadratic-curvature metrics therefore does not apply directly. A regularization such as
\[
J_\varepsilon=J+\varepsilon\int|\mathrm{Rm}|^p,\qquad p>2,
\]
would still require estimates uniform as \(\varepsilon\to0\), a no-neck energy identity, noncollapse or a controlled collapsed alternative, and preservation of the marked relative topology.

Consequently, an abstract inequality
\[
J_{\inf}\ge J(C_\infty)+\sum_\beta E(B_\beta)
\]
does not imply \(J_{\inf}\ge8\pi^2q\). The missing theorem must combine:

1. analytic compactness and energy identity;
2. orbifold Chern–Weil and APS correction bookkeeping;
3. a marked relative homology/lattice decomposition;
4. a proof that each lost marked charge either remains on a costly base or is carried by a bubble configuration with total Ricci-energy charge \(8\pi^2\) per unit.

### Conclusion

The C1 algebra and normalization are consistent. Its unresolved content is exactly the nonlinear radial coercivity inequality above. The scalar moment (8.6) is necessary bookkeeping but cannot close the problem alone; bolt-scale conformal concentration defeats any argument based only on the first radial moment or scalar mean. No supplied scaling disproves C1. The radial square decomposition (8.2), combined with inner bolt rescaling and outer terminal ODE control, is the strongest available rigorous mechanism. General bubble compactness remains insufficient because quotient-ended Ricci-flat ALE bubbles and orbifold bases can carry topology without an individual \(8\pi^2\) Ricci-energy charge, and the marked relative topology has not yet been shown to split in the required way.
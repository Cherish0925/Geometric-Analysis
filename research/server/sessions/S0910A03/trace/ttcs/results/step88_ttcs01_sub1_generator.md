# TTCS Independent Branch Record

```json
{
  "step_id": 88,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step87_resolvent_obstruction_theorem.md",
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Skills/qiushi-yau26/references/research/20260912.tex"
  ]
}
```

## Task

Analyze the next geometric frontier after removing reflection in the complete free-T^2 orthogonally transitive connector class. First independently derive the minimal-separator mechanism and its scope. Then investigate, at equation level, the nearest genuine escape: a free T^2-invariant metric with nonzero connection curvature (failure of orthogonal transitivity), written g=gamma_ij dx^i dx^j+G_ab(dxi^a+A_i^a dx^i)(dxi^b+A_j^b dx^j). Identify how the Abelian curvature F^a=dA^a enters the base Ricci equation, orbit-shape/tension equation, scalar Gauss identity on an invariant separator, and weighted Bochner formula for e=|dU|^2. Determine whether its stress has a favorable or adverse sign for the resolvent obstruction, what end data or topology control (or fail to control) F, and propose one sharp, testable theorem or countermodel that would materially extend the obstruction. Do not assume small Ricci defect forces F small; derive the relevant Maxwell conservation law and conserved fluxes. Keep this within free T^2 symmetry and distinguish it from fully nonsymmetric graph metrics and S^3 necks.

## Output

### 1. Minimal-separator mechanism without reflection

Take a complete free \(T^2\)-invariant four-manifold whose quotient base \(B\) is a cylinder with two expanding cusp-type ends. Write locally
\[
g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\qquad
\rho=(\det G)^{1/2}=e^\sigma,\qquad G=\rho M,\quad \det M=1 .
\]
For any closed curve \(C\subset B\), its invariant lift
\[
\Sigma_C=\pi^{-1}(C)
\]
has three-volume
\[
\operatorname{Vol}_3(\Sigma_C)=\int_C \rho\,ds_\gamma .
\]
Thus invariant separators are geodesics for the conformally changed base metric
\[
\widehat\gamma=\rho^2\gamma .
\]
On exact expanding cusp ends,
\[
\gamma\sim dr^2+e^{2r}dz^2,\qquad \rho\sim e^{2r},
\]
so \(\int_{S^1_r}\rho\,ds_\gamma\sim e^{3r}\to\infty\). Hence the separating homology class has a minimizing invariant separator \(\Sigma\) in the interior. Its mean curvature in the full four-metric is zero.

Let \(s\) be arclength along the base curve, and write the induced metric on \(\Sigma\) as
\[
q=ds^2+G_{ab}(s)\bigl(d\xi^a+A_s^a(s)\,ds\bigr)
\bigl(d\xi^b+A_s^b(s)\,ds\bigr).
\]
Since \(A_s^a\,ds\) is a one-dimensional connection, it is locally removable; globally it only records a torus translation holonomy. Therefore the intrinsic scalar formula is the same as in the orthogonally transitive case:
\[
R_q=-2h_s-\frac32h^2-\frac12 e,\qquad
h=(\log\rho)_s,\qquad e=|U_s|_{\mathbb H^2}^2 .
\]
With weighted measure \(d\mu=\rho\,ds\),
\[
\langle R_q\rangle_\mu=-\frac12\langle e-h^2\rangle_\mu .
\]

If
\[
E=\operatorname{Ric}_g+3g,\qquad \|E\|_{\mathrm{op}}\le\delta ,
\]
the Gauss equation on a minimal \(\Sigma\) gives
\[
R_q=-6+\bigl(\operatorname{tr}E-2E(\nu,\nu)\bigr)-|II|^2 .
\]
Since \(|\operatorname{tr}_\Sigma E-E(\nu,\nu)|\le4\delta\),
\[
\boxed{
\langle e\rangle_\mu
\ge 12-8\delta+\langle h^2\rangle_\mu+2\langle |II|^2\rangle_\mu .
}
\]
In the exact case,
\[
\boxed{\langle e\rangle_\mu\ge 12.}
\]

This replaces the reflected-center identity. Reflection was only one way to produce a totally geodesic scalar \(-6\) separator. A least invariant separator gives the same energy floor, and usually a stronger one because \(|II|^2\) is present.

The mechanism applies to free \(T^2\)-invariant complete connectors with two expanding cusp-type ends and a separating invariant \(T^3\) class. It does not address singular orbit strata, fully nonsymmetric graph metrics, or \(S^3\)-interface necks.

---

### 2. Full free \(T^2\)-invariant equations with connection curvature

Let
\[
\theta^a=d\xi^a+A^a,\qquad F^a=dA^a .
\]
On the oriented two-dimensional base write
\[
F^a=f^a\,dA_\gamma,\qquad f_b=G_{bc}f^c,\qquad
Q=\frac12G_{ab}f^af^b .
\]
Equivalently, the horizontal curvature vector is
\[
\Omega=f^a\partial_{\xi^a},\qquad Q=\frac12|\Omega|_G^2 .
\]

#### 2.1 Maxwell law and conserved twist momenta

The mixed Ricci equation is the Abelian Maxwell equation
\[
\boxed{
d\bigl(\rho\,G_{ab} *_\gamma F^b\bigr)
=
2\rho *_\gamma E^{\mathrm{mix}}_a .
}
\]
For an exact Einstein metric,
\[
\boxed{
d\bigl(\rho\,G_{ab} *_\gamma F^b\bigr)=0 .
}
\]
Thus on each connected base component,
\[
\boxed{
q_a:=\rho\,G_{ab}f^b
}
\]
is constant. These \(q_a\) are the two twist momenta. In terms of \(q\),
\[
f^a=\rho^{-1}G^{ab}q_b=\rho^{-2}M^{ab}q_b ,
\]
and
\[
\boxed{
Q=\frac12\rho^{-3} q_aM^{ab}q_b .
}
\]

Important consequence: pointwise small \(\|E\|_{\mathrm{op}}\) does not by itself make \(F\) small. The source in the Maxwell equation is weighted by \(\rho\), so a long or high-area layer can change \(q_a\) by an order-one amount while \(\|E\|_\infty\) is small.

Exact end data behave differently:

* If one end is exactly a product cusp with \(F\equiv0\) on an open tail, then \(q_a=0\), hence \(F\equiv0\) everywhere in the connected exact Einstein region.
* If the end is only asymptotic to a cusp, nonzero \(q_a\) is compatible with \(F\to0\), because \(Q\sim \rho^{-3}q^TM^{-1}q\) decays rapidly.
* On a cylinder base, \(q_a\) is not a Chern number. The de Rham flux \(\int F^a\) records holonomy change of the torus connection, while \(q_a\) is the Einstein-Maxwell momentum. Topology of the trivial cylinder bundle does not quantize \(q_a\).

---

#### 2.2 Area equation

The vertical trace of the Ricci equation gives
\[
Q-\Delta_\gamma\sigma-|\nabla\sigma|^2
=
-6+E_{\mathrm{orb}},
\]
where \(E_{\mathrm{orb}}\) is the vertical trace of \(E\). Hence
\[
\boxed{
\Delta_\gamma \rho
=
(6+Q-E_{\mathrm{orb}})\rho .
}
\]
For exact Einstein,
\[
\boxed{
\Delta_\gamma\rho=(6+Q)\rho .
}
\]
Thus connection curvature increases the convexity of the orbit area. It strengthens expansion; it does not create an area-collapse escape.

---

#### 2.3 Base Ricci equation

Let \(U:B\to SL(2,\mathbb R)/SO(2)\cong\mathbb H^2\) be the orbit-shape map. Then
\[
\boxed{
\operatorname{Ric}_\gamma-\operatorname{Hess}\sigma
=
-3\gamma
+Q\gamma
+\frac12\,d\sigma\otimes d\sigma
+\frac12\,U^*h_{\mathbb H^2}
+E_B .
}
\]
Equivalently,
\[
\boxed{
\operatorname{Ric}^{4}_{\sigma}
:=
\operatorname{Ric}_\gamma-\operatorname{Hess}\sigma-\frac12d\sigma^2
=
-3\gamma+Q\gamma+\frac12U^*h_{\mathbb H^2}+E_B .
}
\]
The \(Q\gamma\) term has the helpful sign for heat-kernel comparison: it raises the Bakry–Émery tensor.

---

#### 2.4 Orbit-shape/tension equation

Let
\[
\mathcal S_F{}^a{}_b=f^a f_b-Q\delta^a_b ,
\]
a traceless symmetric vertical endomorphism. It has target norm
\[
|\mathcal S_F|_{\mathbb H^2}=Q .
\]
The orbit equation becomes
\[
\boxed{
\operatorname{div}_\gamma\bigl(\rho\,M^{-1}dM\bigr)
=
\rho\,\mathcal S_F
-2\rho\,E_V^0 .
}
\]
Here \(E_V^0\) is the traceless vertical endomorphism induced by the vertical block of \(E\).

For exact Einstein,
\[
\boxed{
\tau_\sigma(U)=\mathcal S_F .
}
\]
Thus nonzero connection curvature turns the orbit map from a weighted harmonic map into a forced weighted harmonic map. This forcing is not controlled by \(\|E\|_\infty\); it is part of the exact geometry.

In charge variables,
\[
Q=\frac12\rho^{-3}q^TM^{-1}q,
\]
and the force is the \(\mathbb H^2\)-gradient of this charge potential, with sign depending on the charged fiber direction. In Iwasawa coordinates,
\[
M=
\begin{pmatrix}
e^\alpha+\beta^2e^{-\alpha}&\beta e^{-\alpha}\\
\beta e^{-\alpha}&e^{-\alpha}
\end{pmatrix},
\]
\[
W=q^TM^{-1}q
=
e^{-\alpha}(q_1-\beta q_2)^2+e^\alpha q_2^2,
\]
and the exact orbit equation is
\[
\tau_\sigma(U)=-\frac12\rho^{-3}\nabla_{\mathbb H^2}W .
\]

---

### 3. Scalar Gauss identity on an invariant separator with \(F\neq0\)

The intrinsic scalar formula on the invariant separator contains no explicit \(F\), because the pulled-back connection along a one-dimensional base curve is locally removable:
\[
R_q=-2h_s-\frac32h^2-\frac12 e .
\]
But \(F\) enters the extrinsic tensor \(II\). If \(T\) is the unit tangent to the base curve and \(\nu\) its unit normal, then in a gauge \(A_\nu=0\),
\[
II_{sa}=\frac12G_{ab}F^b(\nu,T).
\]
Since \(F^a=f^a\,dA_\gamma\),
\[
2\,G^{ab}II_{sa}II_{sb}
=
\frac12G_{ab}f^af^b
=
Q .
\]
Therefore \(F\) contributes positively to \(|II|^2\), and hence raises the separator energy floor:
\[
\langle e\rangle_\mu
\ge
12-8\delta+\langle h^2\rangle_\mu+2\langle |II|^2\rangle_\mu .
\]
At the separator, connection curvature is not an escape from the lower bound; it strengthens it.

---

### 4. Weighted Bochner formula with connection curvature

Let
\[
A_{ij}=h_{\mathbb H^2}(U_i,U_j),\qquad e=\operatorname{tr}_\gamma A .
\]
For the weighted Laplacian
\[
L=\Delta_\gamma+\langle\nabla\sigma,\nabla\cdot\rangle ,
\]
the forced Bochner identity is
\[
\frac12Le
=
|DU|^2
+
(\operatorname{Ric}_\gamma-\operatorname{Hess}\sigma):A
+
2\det A
+
\operatorname{div}_\sigma V
-
|\tau_\sigma(U)|^2 ,
\]
where
\[
V(X)=\langle dU(X),\tau_\sigma(U)\rangle_{\mathbb H^2}.
\]
Substituting the base equation gives
\[
\boxed{
\begin{aligned}
\frac12Le
={}&
|DU|^2
+\frac12|dU(\nabla\sigma)|^2
+\frac12\operatorname{tr}(A^2)+2\det A \\
&+(Q-3)e
+E_B:A
+\operatorname{div}_\sigma V
-|\tau_\sigma(U)|^2 .
\end{aligned}
}
\]
In the exact case \(\tau_\sigma(U)=\mathcal S_F\) and \(|\mathcal S_F|=Q\), hence
\[
\boxed{
\frac12Le
\ge
\frac12e^2+(Q-3)e+\operatorname{div}_\sigma V_F-Q^2 .
}
\]

This displays the sign structure:

* \(+Qe\) in the base Ricci term is helpful.
* The separator floor is also strengthened by \(F\).
* The orbit-force term contributes
  \[
  \operatorname{div}_\sigma V_F-Q^2 .
  \]
  In a resolvent upper estimate, this becomes an uncontrolled source
  \[
  +2Q^2-2\operatorname{div}_\sigma V_F .
  \]
  Thus the traceless vertical stress is adverse for the resolvent obstruction unless \(Q\) or the Maxwell impulse is separately controlled.

For exact metrics,
\[
Le\ge e^2+2(Q-3)e+2\operatorname{div}_\sigma V_F-2Q^2 .
\]
Adding \(6e\) to the resolvent side gives
\[
\boxed{
(-L+6)e
\le
36-(e-6)^2-2Qe+2Q^2-2\operatorname{div}_\sigma V_F .
}
\]
Without a bound on \(Q\), the old ceiling \(e\le6\) is no longer available.

---

### 5. What controls \(F\), and what does not

**Exact Maxwell conservation.**  
For exact Einstein,
\[
q_a=\rho G_{ab} *_\gamma F^b
\]
is constant. This is the strongest control. If an exact cusp tail has \(F\equiv0\) on an open end, then \(q=0\), so \(F=0\) throughout the exact region.

**Asymptotic cusp data.**  
Pointwise decay \(F\to0\) does not force \(q=0\). Since
\[
F^a\sim \rho^{-2}M^{ab}q_b\,dA_\gamma ,
\]
nonzero \(q\) can be invisible at leading cusp order.

**Holonomy.**  
The integral \(\int F^a\) over a compact annulus records change of flat torus holonomy between its two circles. This is not the same as \(q_a\). A flat connection with \(F=0\) may still carry translation holonomy, but it is locally orthogonally transitive and does not alter the Bochner calculation.

**Topology of the base cylinder.**  
For a free \(T^2\)-bundle over a cylinder, there is no compact base two-cycle forcing a quantized Chern number. Thus topology alone does not bound \(q\) or \(Q\).

**Small Ricci defect.**  
The approximate Maxwell law is
\[
d q_a=2\rho *_\gamma E_a^{\mathrm{mix}} .
\]
Hence
\[
|q(p)-q(p_0)|
\le
2\int_{\Gamma}\rho\,|E^{\mathrm{mix}}|\,ds_\gamma .
\]
Small \(\|E\|_\infty\) does not make the right side small on a long high-\(\rho\) layer. A useful control quantity is the weighted Maxwell impulse
\[
\mathcal I(\Gamma)=\int_\Gamma \rho\,|E^{\mathrm{mix}}|\,ds_\gamma ,
\]
not merely \(\|E\|_\infty\).

---

### 6. A sharp testable extension

A natural theorem to test is a charged version of the resolvent obstruction.

Let \(Q=\frac12|F|_G^2\) and assume a complete free \(T^2\)-invariant connector with two exact expanding cusp ends, \(e\to0\) on the ends, and
\[
\|Q\|_\infty\le q_0 .
\]
For exact Einstein metrics, the Bochner-resolvent estimate above gives
\[
B:=\sup e
\le
6+\frac{q_0^2}{3}
+\frac{4q_0}{\sqrt3}\sqrt B ,
\]
using the same \(CD(-3,4)\) resolvent gradient constant \(2/\sqrt3\). Solving,
\[
\boxed{
B\le
\left[
\frac{2q_0}{\sqrt3}
+
\sqrt{6+\frac53q_0^2}
\right]^2 .
}
\]
The minimal separator gives
\[
\sup e\ge 12 .
\]
Therefore exact charged connectors are excluded whenever
\[
\left[
\frac{2q_0}{\sqrt3}
+
\sqrt{6+\frac53q_0^2}
\right]^2<12 .
\]
The threshold is explicit:
\[
\boxed{
q_0<q_*:=9\sqrt2-12\approx0.7279 .
}
\]

So the testable theorem is:

\[
\textit{A complete free \(T^2\)-invariant exact Einstein connector with two exact cusp ends and }
\|Q\|_\infty<9\sqrt2-12
\textit{ cannot exist.}
\]

This theorem would strictly extend the reflected orthogonally transitive obstruction: reflection is replaced by a minimal separator, and orthogonal transitivity is replaced by a quantitative twist-energy bound.

The complementary countermodel target is equally precise: construct a complete reduced solution with nonzero conserved \(q_a\), two cusp-type ends, and \(\sup Q\ge q_*\), while keeping \(e\to0\) on the ends. Such an example would identify the first genuine free-\(T^2\) route around the old resolvent ceiling. It would still remain within the symmetric class; it would not say anything about fully nonsymmetric graph metrics or \(S^3\) necks.
# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step91_separator_stability_and_barriers.md",
    "Sessions/S0910A03/workspace/scripts/step92_jacobi_concentration_models.py",
    "Sessions/S0910A03/workspace/data/step92_jacobi_concentration_models.json",
    "Sessions/S0910A03/workspace/scripts/step92_weighted_jacobi_transform.py",
    "Sessions/S0910A03/workspace/data/step92_weighted_jacobi_transform.json",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md"
  ]
}
```

## Task

Independently verify and sharpen the Step 92 separator analysis. Check the corrected contracted-Gauss sign; derive the full invariant second-variation inequality from the rho^2 gamma minimizing loop; conjugate the weighted Jacobi operator and verify the stated potential after substituting R_q=-2h_s-(3/2)h^2-e_s/2 and R_q=-6+D-|II|^2. Then assess the square-spike calculation: does stable J=-d^2+a-A 1_I on a periodic circle permit A→∞ with width ell→0 and A ell approaching 2 sqrt(a)tanh(sqrt(a)L/2)? State precisely what this proves and does not prove for geometric Q, including the role of variable rho and Maxwell/orbit equations. Seek any immediate rigorous concentration consequence stronger than the constant test, but reject unsupported regularity or scale assumptions.

## Output

# Scientific verification memo: Step 92 separator analysis

## 1. Contracted Gauss identity and the corrected sign

For a hypersurface \(\Sigma^3\subset(X^4,g)\), with
\[
E=\operatorname{Ric}_g+3g,
\qquad
D=\operatorname{tr}_gE-2E(\nu,\nu),
\]
the contracted Gauss equation is
\[
R_q=R_g-2\operatorname{Ric}_g(\nu,\nu)
      +\mathcal H^2-|\mathrm{II}|^2.
\]
Since
\[
R_g=-12+\operatorname{tr}E,
\qquad
\operatorname{Ric}_g(\nu,\nu)=-3+E(\nu,\nu),
\]
this becomes
\[
\boxed{R_q=-6+D+\mathcal H^2-|\mathrm{II}|^2.}
\]
Thus, on the minimal separator,
\[
\boxed{R_q=-6+D-|\mathrm{II}|^2.}
\]
In particular,
\[
R_q\le -6+4\delta
\]
when \(\|E\|_{\mathrm{op}}\le\delta\). This verifies the Step 91/92 correction: the tangential orbit energy term in
\[
R_q=-2h'-\frac32h^2-\frac12e_s
\]
supplies the required curvature below zero.

For a flat \(T^3\) slice, \(R_q=0\), so a minimal flat slice would require
\[
D=6+|\mathrm{II}|^2\ge6.
\]
This is impossible when \(4\delta<6\). More generally, on a flat slice,
\[
\mathcal H^2-|\mathrm{II}|^2=6-D.
\]
Using \(|\mathrm{II}|^2\ge \mathcal H^2/3\) gives
\[
\mathcal H^2\ge 9-6\delta.
\]
Hence the flat-slice barrier and its \(\delta=3/2\) threshold are correct. Minimality means \(\mathcal H=0\), not \(\partial_r\mathcal H=0\).

The supplied twist decomposition is also consistent:
\[
|\mathrm{II}|^2
=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q.
\]
Indeed, Koszul’s formula gives
\[
\mathrm{II}(T,K_a)=-\frac{\varepsilon}{2}G_{ab}f^b,
\]
and the two symmetric mixed entries contribute
\[
2G^{ab}\mathrm{II}(T,K_a)\mathrm{II}(T,K_b)
=\frac12G_{ab}f^af^b=Q.
\]

---

## 2. Full invariant second variation from the minimizing loop

Let \(C\subset(B,\gamma_B)\) minimize
\[
\int_C\rho\,ds_{\gamma_B}
=\operatorname{Length}_{\rho^2\gamma_B}(C)
\]
in its primitive essential class, and let \(\Sigma=\pi^{-1}(C)\).

For an invariant metric with connection, the determinant of the induced metric still gives
\[
d\mu_\Sigma=\rho\,ds\,d\xi^1d\xi^2.
\]
The pullback connection along the one-dimensional curve is locally removable; its translational holonomy does not change this volume formula or the local scalar expression.

Every sufficiently small normal variation of \(C\) remains in the same essential class. Its lift is an invariant normal variation of \(\Sigma\). Therefore, for every smooth periodic invariant speed \(\phi(s)\),
\[
0\le
\int_\Sigma
\left(
|\nabla_\Sigma\phi|^2-
\bigl(\operatorname{Ric}(\nu,\nu)+|\mathrm{II}|^2\bigr)\phi^2
\right)d\mu_\Sigma .
\]
Since \(|\nabla_\Sigma\phi|^2=(\phi')^2\), the torus coordinate volume factors out:
\[
\boxed{
\int_C\rho\,|\mathrm{II}|^2\phi^2\,ds
\le
\int_C\rho
\left[
(\phi')^2+(3-E(\nu,\nu))\phi^2
\right]ds.}
\]
Thus, with
\[
V:=|\mathrm{II}|^2
=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q,
\qquad
a:=3-E(\nu,\nu),
\]
the invariant Jacobi operator is
\[
J=-\rho^{-1}(\rho\,\partial_s)'+a-V,
\]
and its periodic quadratic form is \(\ge0\).

The minimizing-loop argument establishes this for invariant \(\phi(s)\). It does not supply the corresponding statement for speeds depending on the torus variables. Equation (8.4), which is explicitly invariant, is therefore justified.

The constant choice \(\phi=1\) gives
\[
\int_C\rho V\,ds\le\int_C\rho a\,ds,
\]
hence
\[
\langle V\rangle_C\le3+\delta,
\qquad
\langle Q\rangle_C\le3+\delta.
\]

---

## 3. Unitary removal of the weight and the exact potential

Write
\[
\rho=e^\sigma,\qquad h=\sigma',
\qquad
y=e^{\sigma/2}\phi.
\]
The map \(\phi\mapsto y\) is unitary from \(L^2(\rho\,ds)\) to \(L^2(ds)\). Direct differentiation yields
\[
e^{\sigma/2}J(e^{-\sigma/2}y)
=
-y''+
\left(
a-V+\frac12h'+\frac14h^2
\right)y.
\]

The intrinsic scalar formula
\[
R_q=-2h'-\frac32h^2-\frac12e_s
\]
gives
\[
\frac12h'+\frac14h^2
=-\frac14R_q-\frac18h^2-\frac18e_s.
\]
At the minimal separator,
\[
R_q=-6+D-V,
\]
so
\[
\frac12h'+\frac14h^2
=
\frac32-\frac14D+\frac14V
-\frac18h^2-\frac18e_s.
\]
Therefore the unweighted Schrödinger potential is exactly
\[
\boxed{
W=
\frac92-E(\nu,\nu)-\frac14D
-\frac34V-\frac18e_s-\frac18h^2.}
\]
This agrees with `step92_weighted_jacobi_transform.json`.

It is useful to rewrite the defect contribution as
\[
c_E:=\frac92-E(\nu,\nu)-\frac14D
=\frac92-\frac14\sum_{i=1}^3E(e_i,e_i)
       -\frac34E(\nu,\nu).
\]
The operator norm estimate gives the sharper bounds
\[
\boxed{
\frac92-\frac32\delta
\le c_E\le
\frac92+\frac32\delta.}
\]
The earlier separate estimates \(|D|\le4\delta\) and \(|E(\nu,\nu)|\le\delta\) would only give \(2\delta\) in place of \(3\delta/2\).

The transformed quadratic form is equivalently
\[
\boxed{
\int_C
\left[
\frac34V+\frac18(e_s+h^2)
\right]y^2\,ds
\le
\int_C\left[(y')^2+c_Ey^2\right]ds.}
\tag{3.1}
\]
This identity gives useful unweighted concentration information even when \(\rho\) varies strongly.

---

## 4. Rigorous local mass bounds stronger than the constant test

### 4.1 Weighted capacity form

Define
\[
q_{\rho,a}(\phi)
=\int_C\rho\bigl((\phi')^2+a\phi^2\bigr)\,ds.
\]
For any closed arc \(I\subset C\),
\[
\boxed{
\int_I\rho V\,ds
\le
\operatorname{Cap}_{\rho,a}(I),}
\]
where
\[
\operatorname{Cap}_{\rho,a}(I)
:=
\inf_{\substack{\phi\in H^1_{\rm per}(C)\\ \phi\ge1\text{ on }I}}
q_{\rho,a}(\phi).
\]
The same formula holds with \(Q\) in place of \(V\), since \(0\le Q\le V\).

For a point \(s_0\), let \(G_{\rho,a}\) be defined by
\[
q_{\rho,a}\bigl(G_{\rho,a}(s_0,\cdot),\phi\bigr)=\phi(s_0).
\]
Then
\[
\operatorname{Cap}_{\rho,a}(\{s_0\})
=\frac{1}{G_{\rho,a}(s_0,s_0)}.
\]
Thus the full form bounds the mass that can concentrate at a point, even though it gives no finite pointwise height bound.

### 4.2 Explicit constant-coefficient capacity

For \(\rho=1\), \(a>0\) constant, and a circle of length \(L\), an interval of length \(\ell\) has
\[
\boxed{
\operatorname{Cap}_{a}(I_\ell)
=
a\ell+
2\sqrt a\,
\tanh\!\left(\frac{\sqrt a\,(L-\ell)}2\right).}
\]
Consequently,
\[
\int_{I_\ell}V\,ds
\le
a\ell+
2\sqrt a\,
\tanh\!\left(\frac{\sqrt a\,(L-\ell)}2\right).
\]
As \(\ell\to0\), the right side tends
\[
2\sqrt a\,\tanh\!\left(\frac{\sqrt aL}{2}\right).
\]
This is substantially sharper than the compactly supported tent estimate
\[
\int_{I_{r/2}}V\,ds\le \frac8r+\frac83ar,
\]
whose right side diverges as \(r\to0\). The tent is a valid local test, but it is not the optimal periodic test; the optimal function uses the whole complement of the interval.

### 4.3 A \(\rho\)-independent geometric consequence

Set
\[
b_\delta:=\frac92+\frac32\delta.
\]
From (3.1),
\[
\frac34\int_I V\,ds
\le
\operatorname{Cap}_{b_\delta}(I).
\]
Hence, for an arc of length \(\ell\),
\[
\boxed{
\int_I Q\,ds
\le\int_I V\,ds
\le
\frac43\left[
b_\delta\ell+
2\sqrt{b_\delta}\,
\tanh\!\left(
\frac{\sqrt{b_\delta}(L-\ell)}2
\right)
\right].}
\tag{4.1}
\]
In particular, if \(Q\ge A\) throughout \(I\), then \(A\ell\) obeys the same upper estimate. Large plateaus must therefore be narrow, but arbitrarily narrow plateaus are not excluded.

Taking \(I=C\) also gives the unweighted average estimate
\[
\frac1L\int_CV\,ds\le6+2\delta.
\]
This and the weighted estimate \(\langle V\rangle_\rho\le3+\delta\) are distinct when \(\rho\) varies.

---

## 5. Square-spike model

Consider
\[
J_A=-\frac{d^2}{ds^2}+a-A\,\mathbf1_I
\]
on a periodic circle of length \(L\), where \(|I|=\ell\) and \(a>0\). Put
\[
\mu=\sqrt a,\qquad
k=\sqrt{A-a},\qquad
d=L-\ell.
\]
For \(A>a\), the zero-energy monodromy has trace
\[
T(A)=
2\cosh(\mu d)\cos(k\ell)
+
\sinh(\mu d)
\left(\frac{\mu}{k}-\frac{k}{\mu}\right)
\sin(k\ell).
\]
The first value \(A_{\rm crit}(\ell)\) satisfying \(T(A)=2\) is where the lowest periodic eigenvalue reaches zero. Monotonicity of the lowest eigenvalue with respect to \(A\) gives
\[
J_A\text{ has quadratic form }\ge0
\quad\Longleftrightarrow\quad
A\le A_{\rm crit}(\ell).
\]

Set \(A\ell\to\alpha\). Then
\[
k\ell\sim\sqrt{\alpha\ell}\to0,
\]
and the trace equation becomes
\[
2\cosh(\mu L)-\frac{\alpha}{\mu}\sinh(\mu L)=2.
\]
Therefore
\[
\boxed{
A_{\rm crit}(\ell)\,\ell
\longrightarrow
2\sqrt a\,
\tanh\!\left(\frac{\sqrt aL}{2}\right).}
\]
Thus \(A_{\rm crit}(\ell)\sim \alpha_{\rm crit}/\ell\to\infty\). Taking either \(A=A_{\rm crit}(\ell)\), or a fixed fraction below it, produces stable operators with unbounded spike height and shrinking width. Smoothing the two jump points preserves this behavior when the amplitude is kept a fixed fraction below \(A_{\rm crit}\).

For \(a=3\), \(L=2\pi\),
\[
\alpha_{\rm crit}
=
2\sqrt3\,\tanh(\sqrt3\,\pi)
\approx3.46397.
\]
The JSON masses
\[
5.6595,\ 4.5170,\ 3.9778,\ 3.7175,\ 3.5899,\ 3.5267
\]
decrease consistently toward this value. The normalization by \(2\sqrt3\) tends to
\[
\tanh(\sqrt3\pi)\approx0.9999624,
\]
rather than exactly \(1\); numerically the distinction is tiny.

---

## 6. Meaning for geometric twist \(Q\)

The square-spike family establishes the following:

1. The invariant Jacobi inequality by itself is compatible with
   \[
   \|V\|_\infty\to\infty,
   \qquad
   \ell\to0,
   \qquad
   V\ell=O(1).
   \]
   Hence it supplies no finite pointwise ceiling and no dimension-only lower length scale.

2. It does supply finite local mass bounds. Equations (4.1) and the weighted capacity formula are stronger than the constant test and quantify the allowed height–width tradeoff.

3. The square potential is not a construction of a geometric twist field. In the geometry,
   \[
   V=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q,
   \]
   while \(Q\), \(G\), \(\rho\), \(e_s\), and \(h\) obey the mixed Ricci, orbit-shape, and scalar equations simultaneously.

4. Under the charge normalization recorded in Step 88,
   \[
   q_a=\rho G_{ab}*F^b,
   \qquad
   Q=\frac{1}{2\rho^2}G^{ab}q_aq_b.
   \]
   For an exact Einstein metric, the Maxwell equation makes \(q_a\) constant. A \(Q\)-spike would then have to arise through corresponding behavior of \(\rho\) or \(G^{-1}\). With Ricci defect, the mixed equation has a source involving the mixed components of \(E\); a quantitative transport estimate requires the explicit source formula together with control of \(\rho\) and the eigenvalues of \(G\).

5. For a fixed smooth \(\rho\) and \(a\), a narrow spike with \(A\ell\to\alpha\) has the weighted point-mass condition
   \[
   \rho(s_0)\alpha
   \le
   \frac1{G_{\rho,a}(s_0,s_0)}.
   \]
   If \(\rho\) and \(G\) themselves vary on the shrinking scale, this fixed-coefficient asymptotic no longer supplies a uniform number.

Smoothness of each metric gives continuity of \(Q\), but no uniform modulus across a family follows from the supplied equations. No injectivity-radius estimate, orbit-metric ellipticity estimate, or quantitative Maxwell transport scale is presently available. Thus the rigorous output of Step 92 is a set of weighted and unweighted capacity bounds, not a pointwise estimate for geometric \(Q\).
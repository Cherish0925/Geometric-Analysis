# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 88,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step88_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step88_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify and strengthen the proposed removal of reflection from the Step 87 forced OT obstruction. Work in a complete 4-manifold with a free orthogonally transitive T^2 action, quotient base B diffeomorphic to a cylinder, exact outward expanding cusp ends, and E=Ric+3g with ||E||op<=delta. (i) For any invariant minimal hypersurface Sigma=pi^{-1}(C) over an essential closed base curve C, derive with explicit normal and induced-measure conventions the contracted Gauss formula and the periodic intrinsic T^3 scalar identity for q=ds^2+G(s), G=e^sigma M. Check whether <e_s>=12-2<D>+2<|II|^2>+<h^2> and hence >=12-8delta is exactly correct, where D=tr E-2E(nu,nu), h=sigma_s, e_s=|U_s|^2, averages use rho ds, and full base e dominates e_s. (ii) Prove or find the precise missing hypotheses in obtaining an interior smooth essential-loop minimizer for length in the auxiliary metric rho^2 gamma_B, using the two expanding ends. Check equivalence between geodesicity of C for rho^2 gamma_B and minimality of pi^{-1}(C) in g, and analyze boundary barriers/properness rather than assuming reflection or a global Gaussian foliation. (iii) Check that Step 87's complete-base massive-resolvent ceiling applies unchanged, and state the strongest mathematically justified theorem. Identify any subtle failure involving completeness, end orientation, homotopy-class minimization, self-intersection, weighted averages, or attachment regularity.

## Integrated Scientific Memo

# Reflection-free Step 87 obstruction: verified statement and necessary repairs

## 1. Minimal separator identity

Write the free OT metric as
\[
g=\gamma_B+G_{ab}\,d\xi^a d\xi^b,\qquad
G=e^\sigma M,\qquad \det M=1,\qquad \rho=\sqrt{\det G}=e^\sigma .
\]
Let \(C\subset B\) be a smooth embedded essential closed curve, parametrized by \(\gamma_B\)-arclength \(s\), with unit tangent \(T\) and either unit normal \(\nu\). Its lift
\[
\Sigma=\pi^{-1}(C)
\]
has induced metric
\[
q=ds^2+G_{ab}(s)d\xi^a d\xi^b,\qquad
d\operatorname{vol}_q=\rho\,ds\,d\xi^1d\xi^2.
\]
Thus reduced averages are
\[
\langle f\rangle_C=
\frac{\int_C f\,\rho\,ds}{\int_C\rho\,ds}.
\]

Use
\[
\mathrm{II}(X,Y)=g(\nabla_X\nu,Y),\qquad H=\operatorname{tr}_q\mathrm{II}.
\]
The contracted Gauss equation is
\[
R_q=R_g-2\operatorname{Ric}_g(\nu,\nu)+H^2-|\mathrm{II}|^2.
\]
Since \(E=\operatorname{Ric}_g+3g\),
\[
R_g=-12+\operatorname{tr}_gE,\qquad
\operatorname{Ric}_g(\nu,\nu)=-3+E(\nu,\nu).
\]
For a minimal \(\Sigma\), \(H=0\), hence
\[
\boxed{R_q=-6+D-|\mathrm{II}|^2},
\qquad
D:=\operatorname{tr}_gE-2E(\nu,\nu).
\tag{1}
\]
In an orthonormal frame \((T,V_1,V_2,\nu)\),
\[
D=E(T,T)+E(V_1,V_1)+E(V_2,V_2)-E(\nu,\nu),
\]
so
\[
|D|\le4\delta.
\tag{2}
\]

For the intrinsic scalar curvature, put
\[
A=\frac12G^{-1}G_s,\qquad h=\sigma_s=\frac{\rho_s}{\rho},\qquad
P=M^{-1}M_s.
\]
Then
\[
A=\frac12(hI+P),\qquad \operatorname{tr}P=0.
\]
With the normalization used in Steps 82–87,
\[
e_s:=|U_s|_{\mathbb H^2}^2=\frac12\operatorname{tr}(P^2).
\]
The scalar curvature of \(q=ds^2+G(s)\) is
\[
R_q=-2(\operatorname{tr}A)_s-(\operatorname{tr}A)^2-\operatorname{tr}(A^2)
=-2h_s-\frac32h^2-\frac12e_s.
\tag{3}
\]
Because \(C\) is periodic and \(\rho_s=h\rho\),
\[
\int_C \rho h_s\,ds=-\int_C\rho h^2\,ds,
\]
and therefore
\[
\boxed{\langle R_q\rangle_C
=\frac12\bigl(\langle h^2\rangle_C-\langle e_s\rangle_C\bigr)}.
\tag{4}
\]
Averaging (1), equating with (4), and solving gives exactly
\[
\boxed{
\langle e_s\rangle_C
=12-2\langle D\rangle_C
+2\langle|\mathrm{II}|^2\rangle_C
+\langle h^2\rangle_C.}
\tag{5}
\]
Consequently,
\[
\boxed{\langle e_s\rangle_C\ge12-8\delta.}
\tag{6}
\]
No reflection or total-geodesicity is used. The additional terms relative to the reflected-center formula are nonnegative.

Moreover, on \(C\),
\[
e=|dU|_{\gamma_B}^2
=|dU(T)|^2+|dU(\nu)|^2
=e_s+|dU(\nu)|^2\ge e_s,
\]
so the floor applies to the full base energy:
\[
\boxed{\sup_B e\ge12-8\delta.}
\tag{7}
\]

The symbolic checks in `step88_minimal_separator_verify.py` correctly verify all coefficients in (4)–(6).

---

## 2. Weighted geodesics and invariant minimal hypersurfaces

Set
\[
\widehat\gamma=\rho^2\gamma_B.
\]
Then
\[
\operatorname{Area}_g(\pi^{-1}(C))
=\operatorname{vol}(T^2)\int_C\rho\,ds_{\gamma_B}
=\operatorname{vol}(T^2)\operatorname{Length}_{\widehat\gamma}(C).
\tag{8}
\]

With
\[
k_\gamma=\langle\nabla_TT,\nu\rangle,
\]
one has
\[
\mathrm{II}(T,T)=\langle\nabla_T\nu,T\rangle=-k_\gamma.
\]
The vertical trace is
\[
\sum_{a=1}^2\mathrm{II}(V_a,V_a)
=\frac12\operatorname{tr}(G^{-1}\nu G)
=\nu(\log\rho).
\]
Thus
\[
H=-k_\gamma+\nu(\log\rho).
\tag{9}
\]
For the conformal metric \(\widehat\gamma=\rho^2\gamma_B\), with the same curvature convention,
\[
k_{\widehat\gamma}
=\rho^{-1}\bigl(k_\gamma-\nu(\log\rho)\bigr)
=-\rho^{-1}H.
\tag{10}
\]
Therefore
\[
\boxed{
C\text{ is a }\widehat\gamma\text{-geodesic}
\iff
\pi^{-1}(C)\text{ is minimal in }(M,g).}
\tag{11}
\]

This also resolves the apparent sign discrepancy between the two branch derivations: it came from opposite geodesic-curvature conventions. Equations (9)–(11) are consistent with the convention fixed above.

No global Gaussian foliation is required.

---

## 3. Existence of an interior embedded essential minimizer

The necessary end hypothesis must be stated with orientation:

For each of the two ends, there is an outward coordinate \(t_\pm\to+\infty\) such that
\[
\gamma_B=dt_\pm^2+e^{2t_\pm}dz_\pm^2,\qquad
\rho=c_\pm e^{2t_\pm},\qquad c_\pm>0,
\tag{12}
\]
with \(z_\pm\) periodic and representing the primitive cylindrical class. Then
\[
\widehat\gamma
=c_\pm^2e^{4t_\pm}dt_\pm^2
+c_\pm^2e^{6t_\pm}dz_\pm^2.
\tag{13}
\]

### Completeness and coercivity

The outward radial distance satisfies
\[
\int^\infty c_\pm e^{2t}\,dt=\infty,
\]
so \((B,\widehat\gamma)\) is complete; since it is a complete finite-dimensional Riemannian manifold, it is proper.

If the period of \(z_\pm\) is \(\ell_\pm\), any degree-one loop contained in \(t_\pm\ge T\) obeys
\[
L_{\widehat\gamma}(C)
\ge c_\pm e^{3T}\left|\int_C dz_\pm\right|
=c_\pm e^{3T}\ell_\pm\longrightarrow\infty.
\tag{14}
\]
Thus a minimizing sequence in the primitive essential class cannot escape entirely through either end. Once it meets a fixed compact core and has uniformly bounded length, it lies in a fixed closed metric neighborhood of that core, which is compact by properness. The direct method therefore produces a length minimizer.

A useful pointwise barrier is obtained by setting
\[
R=\frac{c_\pm}{2}e^{2t_\pm}.
\]
Then
\[
\widehat\gamma=dR^2+F(R)^2dz_\pm^2,\qquad F'(R)>0.
\]
Along an affinely parametrized geodesic,
\[
R''=F(R)F'(R)(z')^2.
\]
A closed geodesic cannot attain its maximum \(R\) in an exact end, so the resulting geodesic is confined to the compact side of the end.

### Embeddedness and primitive class

One may minimize integral \(1\)-cycle mass in the generator of \(H_1(B;\mathbb Z)\). A minimizing cycle on a smooth surface is a smooth union of embedded closed geodesics with integer multiplicities. Contractible components can be discarded. Every embedded essential component of a cylinder represents \(\pm1\), and total homology \(+1\) implies that the minimizer is one embedded essential geodesic with multiplicity one.

Equivalently, a shortest representative of the primitive free-homotopy class is simple. Specifying “primitive” is essential: a nonprimitive minimizer may merely be a multiple cover.

Hence there is a smooth embedded essential \(\widehat\gamma\)-geodesic \(C\), and its lift is a smooth embedded minimal \(T^3\).

### Why both end orientations matter

Completeness of \(g\) alone does not imply completeness or coercivity of \(\widehat\gamma\). On
\[
g=dt^2+e^{2t}g_{T^3},\qquad t\in\mathbb R,
\]
the \(t\to-\infty\) end is contracting:
\[
\int_{-\infty}^{t_0}\rho\,dt<\infty,\qquad
L_{\widehat\gamma}(\{t\}\times S^1)\to0.
\]
The primitive infimum escapes and is not attained. Thus “two exact ends” is insufficient: both must be outward expanding in the sense of (12).

---

## 4. The resolvent ceiling and its qualifications

Reflection does not enter the complete-base ceiling. Under the global OT equations,
\[
\operatorname{Ric}_f^4
=\operatorname{Ric}_B-\operatorname{Hess}\sigma-\frac12d\sigma\otimes d\sigma
=-3\gamma_B+\frac12U^*h_{\mathbb H^2}+E_B
\ge-(3+\delta)\gamma_B.
\tag{15}
\]
Thus the weighted base satisfies \(CD(-(3+\delta),4)\).

With
\[
K=3+\delta,\qquad \kappa=2K,
\]
the forced Bochner inequality gives
\[
(-L+\kappa)e
\le\kappa^2+8\delta^2-2\operatorname{div}_\sigma V,
\qquad |V|\le2\delta\sqrt e.
\tag{16}
\]
The Fisher-information argument yields the resolvent-gradient bound
\[
\boxed{
\sup_x\int_B|\nabla_yG_\kappa(x,y)|\,d\mu(y)
\le\frac{2}{\sqrt{3+\delta}}.}
\tag{17}
\]
Step 87’s equation (5.1) should therefore use “\(\le\),” not equality: equality in the heat-kernel estimates was not proved.

On exact end neighborhoods, \(U\) is constant and hence \(e=V=0\). Therefore \(e\) is bounded and the resolvent integration by parts has no boundary flux. Duhamel comparison yields, for \(\mathscr E=\sup_Be\),
\[
\mathscr E
\le
2(3+\delta)+\frac{4\delta^2}{3+\delta}
+\frac{8\delta}{\sqrt{3+\delta}}\sqrt{\mathscr E}.
\tag{18}
\]
Solving gives
\[
\boxed{
\mathscr E\le\mathcal B(\delta):=
\left[
\frac{4\delta}{\sqrt{3+\delta}}
+
\sqrt{2(3+\delta)+\frac{20\delta^2}{3+\delta}}
\right]^2.}
\tag{19}
\]

The ceiling therefore transfers unchanged, subject to the Step 87 analytic inputs. The source files establish the algebra of this implication, but do not supply an external independent proof of every global heat-kernel/resolvent theorem invoked there. The exact numerical threshold inherits those analytic constants.

---

## 5. Strongest justified theorem

**Theorem.** Let \((M^4,g)\) be complete and smooth, with a free isometric orthogonally transitive \(T^2\)-action. Assume:

1. \(B=M/T^2\cong S^1\times\mathbb R\);
2. outside a compact subset, both ends have outward coordinates \(t_\pm\to+\infty\) and the exact model
   \[
   \gamma_B=dt_\pm^2+e^{2t_\pm}dz_\pm^2,\qquad
   \rho=c_\pm e^{2t_\pm},
   \]
   with constant orbit map \(U\);
3. the metric and end attachments are globally \(C^\infty\);
4. \(\|\operatorname{Ric}_g+3g\|_{\mathrm{op}}\le\delta\).

Then there exists a smooth embedded essential invariant minimal \(T^3\), and
\[
12-8\delta\le\sup_Be\le\mathcal B(\delta).
\tag{20}
\]
Consequently such a metric cannot exist whenever
\[
12-8\delta>\mathcal B(\delta).
\]
The unique crossing is
\[
\delta_*=0.246249763690668\ldots,
\]
so, conditional only on the Step 87 forced-Bochner and complete weighted-resolvent inputs,
\[
\boxed{0\le\delta<\delta_*\quad\Longrightarrow\quad\text{nonexistence}.}
\]

Thus reflection is genuinely removable: the reflected center is replaced by a primitive weighted-length minimizing essential loop, and its lift supplies an equal or stronger energy floor.

For merely asymptotic ends, the theorem does not follow as stated. One must separately ensure:

- completeness and properness of \(\rho^2\gamma_B\);
- coercivity of primitive essential-loop length at both ends;
- boundedness of \(e\);
- the global \(CD(-(3+\delta),4)\) inequality;
- sufficient decay/integrability of \(V\) to eliminate resolvent boundary flux;
- smooth attachment regularity.

Twisted/non-OT actions, singular orbits, mixed expanding/contracting ends, and nonprimitive loop classes remain outside this result.
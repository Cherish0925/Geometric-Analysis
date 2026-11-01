# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 67,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step67_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step67_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently assess the mathematical significance and correctness of the Step-67 finite-jet result for the closed negative-scalar Goldberg programme. Read the Step-65 leading-zero theorem, the superseded Step-66 note, A02's corrected Step-80 note/reconstruction method, and A01's independent Step-67 verification outputs and coordinate-conversion script. Determine precisely what is established by the explicit H2..H8 jets and two-gauge residuals, what is not (formal all-orders/analytic germ/global closed example), whether the normal-coordinate pullback cross-check is mathematically valid including the geodesic exponential-map recursion, and what the highest-value next computation or invariant derivation is. Pay special attention to the order dictionary (E2/E4/E6 versus Taylor coefficients of the scalar compatibility), scaling parameters, positive-index nondegenerate zeros, and whether attempting degree 8 is scientifically justified. Give a direct technical memo, not process advice.

## Integrated Scientific Memo

# Technical memo: what Step 67 establishes for the negative-scalar Goldberg programme

## 1. Verdict

The supplied reconstructions and verification outputs give **strong, cross-validated numerical evidence for real almost-Kähler metric \(8\)-jets with nondegenerate, positive-index torsion zeros, satisfying the Einstein equations through curvature Taylor degree \(6\)**. They include two examples with \(\lambda=-5\) and one with \(\lambda=0\).

They invalidate the empirical premise behind Step 66:
\[
\text{“The reduced minimum }\Phi _6\text{ is positive at every strict cone point.”}
\]
The corrected data have substantial negative \(\Phi _6\) margins, not values indistinguishable from zero.

However:

* The computations are floating-point finite-jet results, **not certified exact finite-jet existence theorems**.
* They do not establish an all-orders formal solution, an analytic Einstein almost-Kähler germ, or a closed example.
* The general nonexistence conjecture for nondegenerate zeros is therefore **not refuted as an all-orders assertion**; its proposed exclusion mechanism at \(E_6\) is refuted numerically.
* The coordinate pullback cross-check remains mathematically meaningful, but its claimed geodesic exponential-map recursion is wrong. The resulting coordinates are point-normal, not established exponential normal coordinates.
* The next genuinely new even prolongation is **\(E_8\), requiring \(H_{10}\)**. Computing another metric degree-\(8\) jet would repeat the level already reached.

A further essential restriction is that Step 80 treats the **even branch \(H_3=0\)**. Its positive-\(\Phi _6\) obstruction is not proved to exclude extensions allowing nonzero odd jets.

## 2. The finite-jet construction and its evidential strength

### Exact almost-Kähler parametrization

The Darboux ansatz is
\[
g=e^H,\qquad H^T=H,\qquad HJ_0+J_0H=0,
\]
with constant standard symplectic form \(\omega\). In the stated matrix convention,
\[
J=g^{-1}\omega=e^{-H}J_0,\qquad J^2=-I.
\]
Thus compatibility and \(d\omega=0\) are identities of the parametrization, not equations solved approximately.

A finite polynomial \(H=H_2+\cdots+H_8\), inserted into the full exponential, defines an actual analytic, positive-definite almost-Kähler metric near the origin. Since \(H\) starts at degree two,
\[
g(0)=I,\qquad dg(0)=0,\qquad \nabla\omega(0)=0.
\]
The origin is a torsion zero, and its first torsion derivative is determined by \(H_2\). What is only approximately satisfied is the finite collection of Einstein Taylor equations.

### Reproduced numerical evidence

The verification script reloads the coefficients without rerunning the optimizer. It checks monomial conventions, the anti-\(J_0\) basis, the Einstein coefficients, the torsion cone, and the saved scalar quadratic.

| Reconstruction | \(\lambda\) | \(\det_{\mathbb R}Df\) | Recomputed \(\Phi _6\) | Darboux \(\|E_6\|\) | Pulled-back system norm |
|---|---:|---:|---:|---:|---:|
| gen2 | \(0\) | \(0.0166186\) | \(-0.165279\) | \(6.16\times10^{-8}\) | \(6.73\times10^{-8}\) |
| gen2 | \(-5\) | \(0.0166186\) | \(-0.236912\) | \(1.25\times10^{-7}\) | \(1.41\times10^{-7}\) |
| gen5 | \(-5\) | \(0.0233729\) | \(-0.416124\) | \(7.69\times10^{-9}\) | \(8.44\times10^{-9}\) |
| positive control | \(-1\) | \(0.0501890\) | \(+0.841910\) | \(4.64\) | \(4.78\) |

The lower Einstein coefficients are small, and the cone residuals are approximately \(10^{-16}\). In the best negative example, the \(H_8\) solve cancels an \(E_6\) vector of norm \(2.06\times10^6\), leaving approximately \(8\times10^{-9}\). This is compelling evidence of the intended algebraic cancellation, but it also explains why rigorous certification cannot be inferred from the absolute residual alone.

The first verification is an independent reevaluation, **not an independent implementation of Ricci**: it imports A02’s Tower code. The second evaluation uses A01’s general \((g,\omega)\) system and therefore supplies a more substantial implementation cross-check. The evaluator’s source and the coefficient NPZ files are not reproduced in this bounded input, so the present assessment checks the supplied scripts and reported outputs rather than rerunning them.

### Why the reduced equation is genuinely quadratic

Once \(H_2\) is fixed and \(H_3=0\), the equations through \(E_5\) are affine in
\[
u=(H_4,H_5,H_6,H_7).
\]
The first quadratic dependence on these variables is \(H_4H_4\), appearing in \(E_6\). On the affine lower-order solution space \(u=u_0+Ny\), the reduced equations therefore have the exact algebraic form
\[
\Psi(y)=c+Jy+\frac12H[y,y].
\]

The reconstruction splits \(y=Pz+Kw\), with \(K\) annihilated by the quadratic forms. On the reported regular stratum, \(JK\) has rank \(34\), and one scalar equation remains:
\[
\phi(z)=c_\pi+j^Tz+\frac12z^TH_\pi z=0.
\]
If \(H_\pi>0\), then
\[
\Phi _6=c_\pi-\frac12j^TH_\pi^{-1}j
\]
is its minimum, and real solvability is equivalent to \(\Phi _6\le0\).

This equivalence is exact **provided the rank reductions and quadratic decomposition are exact**. Their numerical realization has not yet been certified.

For \(\Phi _6<0\), the reconstructed root is transverse:
\[
z=z_*+tv,\qquad
t=\sqrt{-2\Phi _6/h},\qquad
\nabla\phi(z)=thv\ne0.
\]
For gen5, using the reported smallest eigenvalue, this scalar gradient has norm about \(0.0624\). Together with exact rank \(34\) for \(JK\), this would give rank \(35\) for the reduced derivative and local stability under perturbations. A rigorous certificate must also control the lower affine system, the selected right inverse, and the numerical rank gaps; a residual and Hessian bound alone are insufficient.

Accordingly, the sound statement is **robust numerical finite-order solvability on the sampled regular even stratum**. A universal exact semialgebraic classification of the strict cone is not supplied. The open portion is \(\{\Phi _6<0\}\), not \(\{\Phi _6\le0\}\); at equality the scalar root is its minimizer and loses transversality.

## 3. Order dictionary: three different notions of “order”

Write
\[
E(g)=\operatorname{Ric}(g)-\lambda g=\sum_{d\ge0}E_d.
\]
Here \(E_d\) is homogeneous coordinate degree \(d\), and it depends on metric terms through \(H_{d+2}\).

The scalar compatibility hierarchy has a two-degree shift relative to \(E_d\):

| Einstein level | Highest metric degree | Associated scalar Taylor degree | Scalar coefficient count |
|---|---:|---:|---:|
| \(E_2\) | \(H_4\) | \(0\) | \(1\) |
| \(E_4\) | \(H_6\) | \(2\) | \(10\) |
| \(E_6\) | \(H_8\) | \(4\) | \(35\) |
| \(E_8\) | \(H_{10}\) | \(6\) | \(84\) |

The count is
\[
\dim\operatorname{Sym}^{d-2}(\mathbb R^4)^*
=\binom{d+1}{3}.
\]

The cone
\[
\|A\|^2-\|S\|^2-8|c|^2=0
\]
is the scalar degree-zero relation associated with \(E_2\). Step 65 identifies the ten principal degree-two conditions at a second-order torsion zero with the ten Step-64 quadrics associated with \(E_4\).

At \(E_6\), the \(35\) scalar degree-four coefficients are reduced by adjustable lower-jet freedom to one quadratic solvability condition. **\(\Phi _6\) is the minimum after elimination; it is not the full degree-four scalar Taylor polynomial.**

The numerical universality of \(\ell\) suggests that the last obstruction is a fixed linear functional on \(E_6\). Calling it a “degree-six coefficient of scalar compatibility” without specifying the differential conversion obscures the shift: the natural geometric scalar equation has degree-four coefficients at this level. The complete identification of those \(35\) coefficients with the projected Einstein equations at a nondegenerate zero remains an invariant derivation to be done.

For exactly even \(H\), odd \(E_d\) vanish by parity. The saved arrays contain small nonzero \(H_5,H_7\), and their reevaluated odd residuals are small rather than identically zero. Thus the files are numerically near-even. An exact even construction would set all odd coefficients to zero.

## 4. Scaling: the dimensionless parameter needs correction

Define the displayed squared torsion-slope norm by
\[
N=4|c|^2+2\|S\|^2+2\|A\|^2.
\]
The reconstructed examples have \(N=1\).

Under
\[
H_k\mapsto\mu^kH_k,\qquad \lambda\mapsto\mu^2\lambda,
\]
one has
\[
(c,S,A)\mapsto\mu^2(c,S,A),\qquad
N\mapsto\mu^4N,
\]
and
\[
\det Df\mapsto\mu^8\det Df,\qquad
\Phi _6\mapsto\mu^8\Phi _6.
\]
Consequently the dimensionless quantities are
\[
\widehat\lambda=\frac{\lambda}{\sqrt N},
\qquad
\widehat\Phi _6=\frac{\Phi _6}{N^2}.
\]

Step 80 explicitly calls \(N\) “\(\mathrm{tn}^2\).” With that definition, \(\lambda/\mathrm{tn}^2\) is **not** scale invariant; the correct ratio is \(\lambda/\sqrt{\mathrm{tn}^2}\). At \(N=1\), the numerical labels \(0\) and \(-5\) are unchanged.

Scaling the negative example yields finite approximate jets at any prescribed negative \(\lambda\), but always at the same dimensionless ratio \(\widehat\lambda=-5\). It does not scan new normalized curvature regimes.

The reported fit
\[
\Phi _6=F_0+\lambda F_1+\lambda^2F_2
\]
is compatible with weights \(8,6,4\) for \(F_0,F_1,F_2\), respectively. Its exact universality is not proved by the finite numerical scans.

## 5. The pullback cross-check: valid coordinate change, invalid exponential recursion

### The defect

Let the true exponential map be
\[
X(y)=\sum_{m\ge1}X_m(y),\qquad X_1(y)=y,
\]
with \(X_m\) homogeneous of degree \(m\). Set
\[
\mathcal R=y^i\partial_{y^i}.
\]
The radial curve \(x(t)=X(ty)\) satisfies the geodesic equation precisely when
\[
(\mathcal R^2-\mathcal R)X^a+
\Gamma^a_{bc}(X)(\mathcal RX^b)(\mathcal RX^c)=0.
\]
Thus the correct recursion is
\[
m(m-1)X_m^a
=-\big[\Gamma^a_{bc}(X)(\mathcal RX^b)(\mathcal RX^c)\big]_m.
\]

The supplied script instead computes
\[
m(m-1)X_m^a
=-\big[\Gamma^a_{bc}(X)y^by^c\big]_m.
\]
It omits the velocity corrections
\[
\mathcal RX=y+\sum_{m\ge2}mX_m.
\]
Dividing by \(m(m-1)\) is correct; the right-hand side is not.

Because \(\Gamma(0)=0\), \(X_2=0\), and the two recursions agree through degree four. The first generic discrepancy is at degree five, involving \(\Gamma_1(y)\), \(y\), and \(3X_3\). Corresponding deviations from full normal-coordinate metric identities can begin in metric degree four. Special cancellations are possible, but none is checked here.

The reported
\[
\|\partial g_{\mathrm{new}}(0)\|=0
\]
does not detect this error: the source metric is already point-normal, and any \(X=y+O(|y|^3)\) preserves that property. A true normal-coordinate check would test the geodesic equation or Gauss lemma
\[
g_{ij}(y)y^j=y_i
\]
to the claimed order.

There is an additional truncation distinction: a true normal metric through degree eight generally requires the coordinate map through degree nine, since differentiating \(X_9\) contributes to its degree-eight pullback. The arbitrary polynomial map actually used, with higher coefficients set to zero, is nevertheless a legitimate coordinate map.

### Why the residual cross-check survives

The computed map has \(X(0)=0\) and \(DX(0)=I\), so it is an invertible local polynomial germ regardless of the failed geodesic interpretation. The pullback formulas
\[
g_{\mathrm{new}}=DX^T\,g(X)\,DX,\qquad
\omega_{\mathrm{new}}=DX^T\,\omega\,DX
\]
are correct. Since \(H\) starts at degree two, retaining
\[
I+H+\frac{H^2}{2}+\frac{H^3}{6}+\frac{H^4}{24}
\]
suffices for the metric Taylor coefficients through degree eight.

Any such pullback preserves the almost-Kähler equations and transforms the Einstein tensor covariantly. Hence the independent \((g,\omega)\) residuals remain useful. The correct description is **a non-Darboux, point-normal pullback cross-check**, not a verified geodesic-normal conversion.

The determinant comparison is particularly clean:
\[
\det(\mathrm{Mvec})=16\,\det Df
\]
in all four cases. This confirms the factor-of-two torsion-derivative convention in four dimensions and the positive local index.

If the lower Einstein coefficients vanish exactly, \(X=y+O(|y|^3)\) implies that the degree-six Einstein tensor is unchanged componentwise. The reported control norms \(4.640\) and \(4.778\) therefore call for a componentwise convention comparison. Different vectorizations or floating-point cancellation could explain the difference; the supplied aggregate norms do not determine which. It is not justified to assert that a normalization difference is necessarily the cause.

## 6. Relation to Step 65 and corrections to Step 66

Step 65 proves a necessary leading-term classification only when the first nonzero torsion term has degree \(m\ge2\):
\[
f_m=\kappa\bar z_2^{\,m}e_1.
\]
The Step-67 examples have \(m=1\), so there is no conflict.

Three geometries must remain distinct:

1. Nondegenerate first-order zeros, with index \(+1\).
2. Rank-deficient first-order zeros, including the rank-two surface model \(\kappa\bar z_2e_1\).
3. Higher-order zeros, to which Step 65’s classification applies.

Even a hypothetical exclusion of case 1 would not put every remaining zero under the \(m\ge2\) theorem.

Step 66 also incorrectly says an isolated degenerate zero has ill-defined Brouwer index. Its local degree is defined whenever the zero is isolated; only the determinant formula is unavailable.

For the compact programme, Step 67 shows that the positive-index contribution expected from nondegenerate zeros is compatible with the local equations through \(E_6\), including negative \(\lambda\). It supplies neither an exact germ carrying that contribution nor compact assembly.

The distinct surface problem remains unchanged. Step 65 gives
\[
(D^L_{e_1}-iD^L_{Je_1})b=\Xi,
\qquad b=W_3^+|_C,
\]
and negative degree
\[
\deg L=\frac{s\,\operatorname{Area}(C)}{4\pi}<0.
\]
No bounded divisibility law for \(\Xi\) through \(b=0\) is supplied. The scalar leading identity permits both tangential complex types and does not determine exceptional winding. The finite nondegenerate jets do not resolve or diminish this separate coupled-transport obstruction.

## 7. Highest-value new mathematical content

### Invariant identification of the surviving functional

The most leveraged invariant derivation is the degree-four expansion, at a nondegenerate torsion zero, of Step 65’s exact scalar equation:
\[
\mathcal S=
\Delta q-8\operatorname{tr}V^2+24|\eta|^2
+\frac{3s}{2}q+\frac94q^2
-16\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle=0.
\]

The precise object to identify is the relation between its \(35\) degree-four coefficients and the \(35\) non-Bianchi compatibility rows at \(E_6\), modulo the already imposed lower equations. Eliminating the \(34\) adjustable directions should then identify \(\ell\) and the quadratic minimum invariantly.

There is a sharp representation-theoretic candidate. If the surviving row is genuinely jet-independent and equivariant under \(U(2)\), its line must be invariant. Among scalar homogeneous quartics on \(\mathbb R^4\cong\mathbb C^2\), the invariant functional is, up to normalization, double trace:
\[
[\mathcal S]_4\longmapsto \Delta_0^2[\mathcal S]_4(0).
\]
Thus \(\Delta_0^2\mathcal S(0)\), after lower-order elimination, is a concrete candidate for the remaining scalar. Numerical agreement of four rows does not prove equivariance or this identification, but the candidate is substantially more specific than a generic “universal functional.”

This would explain the scaling weight eight and could distinguish a genuine geometric restriction from artifacts of coordinates, chosen complements, or rank strata.

### Is attempting \(E_8\) justified?

**Yes.** It is the first untested even compatibility level, with \(84\) scalar degree-six coefficients and metric data through \(H_{10}\). Its nonlinear forcing includes
\[
H_4H_6,\qquad H_2H_8,\qquad H_2H_4H_4,
\]
among other weighted-degree-ten terms. The \(H_5H_5\) contribution disappears in the exactly even branch.

The correct mathematical object is
\[
\Pi_8E_8(H_2,H_4,H_6,H_8,H_{10}=0)
\]
restricted to the **full lower-order solution family**, where \(\Pi_8\) eliminates the flat \(H_{10}\) range and the automatic identities.

A failed extension of one arbitrarily chosen reconstruction excludes only that lower jet. The lower-order free directions, including \(\ker L_6\) in \(H_8\), can change the \(E_8\) compatibility.

The best supplied numerical base point is gen5 at \(\lambda=-5\): it has the most negative margin, the smallest coefficient norms among the negative examples, and the smallest two-representation residual. Before interpreting its higher-order forcing, the \(H_8\) range/nullspace split needs to be controlled. The control’s \(\|H_8\|\approx3.5\times10^{14}\), despite a forcing norm near \(10^6\), strongly suggests a rank-sensitive least-squares issue. The script’s unqualified `lstsq` warrants inspection, but the available source does not establish a particular driver defect or prove that all large \(H_8\) coefficients are spurious. A rank-revealing range solve would separate necessary coefficients from numerical or freely chosen nullspace components.

Finally, **rank \(84\) of the projected Jacobian at an order-six solution does not by itself prove an order-eight extension**. It gives local openness and rules out a linearized compatibility deficit there. A root requires the projected residual to lie within a quantitatively controlled local image, or an actual corrected solve. Conversely, rank deficit alone is not an obstruction: one must identify and evaluate the remaining nonlinear compatibility.

The unresolved local object is therefore an \(E_8\) root—or a genuine sign obstruction—on the lower-order family, with odd branches considered before any universal exclusion. Neither an \(E_8\) root nor a full-rank calculation would decide formal all-orders existence, convergence, or the closed negative-scalar Goldberg problem.
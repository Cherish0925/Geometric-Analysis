# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step65_homogeneous_torsion_zero_classification_and_surface_transport.md",
    "Sessions/S1003A01/workspace/notes/step66_order6_obstruction.md",
    "Sessions/S1003A02/workspace/notes/step80_Q4_universal_functional_and_lambda_quadratic.md",
    "Sessions/S1003A02/workspace/scripts/step80_reconstruct.py",
    "Sessions/S1003A01/workspace/scripts/step67_verify_A02_reconstruction.py",
    "Sessions/S1003A01/workspace/scripts/step67_convert_darboux_to_normal.py",
    "Sessions/S1003A01/workspace/data/step67/verify_A02_step80_reconstructions.json",
    "Sessions/S1003A01/workspace/data/step67/normal_coordinate_crosscheck.json",
    "Sessions/S1003A02/workspace/data/step80/recon_F012_gen5_lam-5.json",
    "Sessions/S1003A02/workspace/data/step80/recon_lsA_jet0_lam-1.json"
  ]
}
```

## Task

Independently assess the mathematical significance and correctness of the Step-67 finite-jet result for the closed negative-scalar Goldberg programme. Read the Step-65 leading-zero theorem, the superseded Step-66 note, A02's corrected Step-80 note/reconstruction method, and A01's independent Step-67 verification outputs and coordinate-conversion script. Determine precisely what is established by the explicit H2..H8 jets and two-gauge residuals, what is not (formal all-orders/analytic germ/global closed example), whether the normal-coordinate pullback cross-check is mathematically valid including the geodesic exponential-map recursion, and what the highest-value next computation or invariant derivation is. Pay special attention to the order dictionary (E2/E4/E6 versus Taylor coefficients of the scalar compatibility), scaling parameters, positive-index nondegenerate zeros, and whether attempting degree 8 is scientifically justified. Give a direct technical memo, not process advice.

## Output

# Technical memo: Step-67 finite Einstein jets and the \(s<0\) Goldberg programme

## 1. Main assessment

The Step-80/67 artifacts provide strong, independently reproduced numerical evidence for the following finite-order statement:

> There are real almost-Kähler metric \(8\)-jets with a nondegenerate torsion zero of local index \(+1\), for \(\lambda=0\) and for \(\lambda=-5\), whose Einstein tensor
> \[
> E(g)=\operatorname{Ric}(g)-\lambda g
> \]
> has vanishing Taylor coefficients \(E_0,\ldots,E_6\) to approximately \(10^{-8}\)–\(10^{-7}\) in absolute norm and approximately machine precision relative to the large intermediate terms.

For the best \(\lambda=-5\) example, `recon_F012_gen5_lam-5`,

\[
\det_{\mathbb R}Df=0.02337291736636084>0,\qquad
\Phi_6=-0.41612425938887987,
\]
and the direct Darboux calculation gives

\[
\|E_6\|=7.7\times10^{-9},
\]
after canceling an \(E_6\) vector of norm \(2.06\times10^6\) by the \(H_8\) term. The independent \((g,\omega)\) representation gives total residual

\[
8.44\times10^{-9}.
\]

Thus the proposed universal order-\(6\) obstruction in Step 66 is not present. Some strict cone jets have \(\Phi_6>0\) and do not extend through \(E_6\), while other strict cone jets have \(\Phi_6<0\) and do extend through \(E_6\).

This is a finite Taylor result. It does not produce an all-orders formal Einstein jet, an analytic Einstein almost-Kähler germ, or a closed example.

If Conjecture 79.C is read literally as the nonexistence of an all-orders formal germ, its truth value is still unresolved. The Step-80 result refutes only the proposed obstruction at \(E_6\), not the all-orders statement.

---

## 2. What the \(H_2,\ldots,H_8\) arrays represent

The Darboux parametrization has

\[
g=e^H,\qquad HJ_0+J_0H=0,\qquad H^T=H,
\]
with the symplectic form fixed and constant. The anti-\(J_0\) condition gives exact almost-Hermitian compatibility. Indeed, with \(J=g^{-1}\omega=e^{-H}J_0\),

\[
J^2=e^{-H}J_0e^{-H}J_0
=e^{-H}e^H J_0^2=-I.
\]

The constant symplectic form is closed, so any such \(H\) defines an actual local almost-Kähler structure, not merely an approximate one. Since \(H\) begins in degree two,

\[
g(0)=I,\qquad dg(0)=0,\qquad \nabla\omega(0)=0.
\]

Thus the torsion vanishes at the origin. Its first derivative is determined by \(H_2\).

The supplied arrays may also be inserted into a finite polynomial \(H\) and then into the full analytic exponential \(e^H\). This gives an actual analytic almost-Kähler metric near the origin. What is approximate is its Einstein property: only the Taylor coefficients through \(E_6\) have been made numerically small.

The large coefficient norms,

\[
\|H_4\|\simeq638,\quad
\|H_6\|\simeq1164,\quad
\|H_8\|\simeq5.85\times10^5
\]
for the best \(\lambda=-5\) example, do not obstruct local positive definiteness because \(e^H\) is positive definite for real symmetric \(H\). They do make double-precision cancellation important. No interval or exact-algebra certification is supplied, so the result remains numerical rather than a theorem about an exact real solution of the finite polynomial equations.

The margins are nevertheless substantial where it matters most:

\[
\Phi_6=-0.416,\qquad
\lambda_{\min}(H_\pi)=0.00468,\qquad
\lambda_{\max}(H_\pi)=0.1064.
\]

These are far larger than the reported residuals. The positive-\(\Phi_6\) control also behaves distinctly: its lower coefficients are near zero, but the order-\(6\) residual remains approximately \(4.64\) in Darboux form and \(4.78\) after coordinate conversion.

---

## 3. Order dictionary

The subscript on \(E_d\) denotes homogeneous coordinate degree \(d\) in the Einstein tensor. Because Ricci curvature contains two derivatives, \(E_d\) uses metric coefficients through \(H_{d+2}\):

| Einstein coefficient | Highest metric term | Associated scalar-compatibility degree | Number of scalar coefficients |
|---|---:|---:|---:|
| \(E_0\) | \(H_2\) | — | — |
| \(E_2\) | \(H_4\) | \(0\) | \(1\) |
| \(E_4\) | \(H_6\) | \(2\) | \(10\) |
| \(E_6\) | \(H_8\) | \(4\) | \(35\) |
| \(E_8\) | \(H_{10}\) | \(6\) | \(84\) |

The count is

\[
\dim \operatorname{Sym}^{d-2}(\mathbb R^4)^*
=\binom{d+1}{3}.
\]

This matches the established hierarchy:

* The scalar degree-zero relation associated with \(E_2\) is the first-order cone
  \[
  \|A\|^2=\|S\|^2+8|c|^2.
  \]
* The scalar degree-two relation associated with \(E_4\) has ten coefficients. These are the ten Step-64 quadrics identified in Step 65.
* At \(E_6\), the scalar degree-four relation has \(35\) coefficients. In the Step-80 reduction, \(34\) directions are solved by lower-jet freedom and one real quadratic equation remains. Its minimum is \(\Phi_6\).

Consequently, \(\Phi_6\) is not itself the entire degree-four scalar relation. It is the final scalar Schur complement obtained after solving the other \(34\) projected equations.

The notation “order \(6\)” refers to \(E_6\), although \(\Phi_6\) has scaling weight eight:

\[
\Phi_6(\mu^2\theta,\mu^2\lambda)=\mu^8\Phi_6(\theta,\lambda).
\]

The existing construction has already reached metric degree eight. The next untested even equation is \(E_8\), requiring \(H_{10}\). Calling another computation merely “degree eight” is therefore ambiguous unless one specifies \(E_8\) rather than \(H_8\).

Because the selected branch is even, an exact choice

\[
H_3=H_5=H_7=H_9=0
\]
makes every odd \(E_d\) vanish identically by parity. The tiny saved \(H_5,H_7\) norms are numerical nullspace noise, not new odd geometry.

---

## 4. Scaling and the normalized curvature parameter

Let

\[
N=4|c|^2+2\|S\|^2+2\|A\|^2.
\]

All reconstructed examples are normalized by \(N=1\). Under

\[
H_k\mapsto\mu^k H_k,\qquad \lambda\mapsto\mu^2\lambda,
\]
the first torsion derivative coefficients satisfy

\[
(c,S,A)\mapsto\mu^2(c,S,A),
\]
and therefore

\[
N\mapsto\mu^4N,\qquad
\det Df\mapsto\mu^8\det Df,\qquad
\Phi_6\mapsto\mu^8\Phi_6.
\]

The scale-invariant Einstein parameter is therefore

\[
\widehat\lambda=\frac{\lambda}{\sqrt N},
\]
and the scale-invariant scalar value is \(\Phi_6/N^2\).

Thus the sentence “\(\lambda/\mathrm{tn}^2=-5\)” is consistent only if \(\mathrm{tn}^2\) denotes \(\sqrt N\). If the displayed definition \(\mathrm{tn}^2=N\) is used literally, the invariant ratio is \(\lambda/\sqrt{\mathrm{tn}^2}\), not \(\lambda/\mathrm{tn}^2\).

For the normalized examples \(N=1\), this notational issue does not alter the numerical value: \(\widehat\lambda=-5\). Scaling produces examples at any prescribed \(\lambda<0\), with the torsion slope adjusted so that \(\lambda/\sqrt N=-5\). It does not generate different values of this dimensionless ratio.

The decomposition

\[
\Phi_6=F_0+\lambda F_1+\lambda^2F_2
\]
is compatible with scaling provided \(F_i\) has weight \(8-2i\).

---

## 5. Torsion index and relation to Step 65

The reconstructed jets satisfy the strict cone to approximately \(10^{-16}\). For the three extending examples,

\[
\det_{\mathbb R}Df=
0.0166186,\quad 0.0166186,\quad 0.0233729,
\]
so the origin is an isolated nondegenerate torsion zero with local Brouwer index \(+1\).

The normal-representation values satisfy

\[
\det(\mathrm{Mvec})=16\,\det(Df).
\]

For example,

\[
0.3739666778617733
=16(0.02337291736636084).
\]

This is exactly the determinant factor expected from the convention \(\mathrm{Nphi}=2\,\mathrm{Mmat}\) in four real dimensions. It confirms that the two representations use the same orientation and index.

Step 65 concerns torsion zeros whose first nonzero term has degree \(m\ge2\). Its conclusion

\[
f_m=\kappa(\bar z_2)^m e_1
\]
does not apply to these \(m=1\) examples. There is therefore no contradiction. The combined local picture is:

* \(m=1\): strict cone, positive index, and further conditions such as \(\Phi_6\le0\);
* \(m\ge2\): GH-type leading polynomial, with higher terms controlling isolation, winding, and zero surfaces.

Step 66’s proposed consequence that every Einstein almost-Kähler torsion zero is degenerate cannot be inferred from \(E_6\). The positive-\(\Phi_6\) samples in that note remain genuine excluded jets at this order; what disappears is the universal quantifier.

For a closed manifold where the torsion section has total topological index \(5\chi+6\tau\), each realized nondegenerate model of the present type would contribute \(+1\). The finite jets show that such contributions are compatible with all equations through \(E_6\). They do not assemble these local models on a compact manifold or establish that any one extends to an exact Einstein germ.

A minor topological correction to Step 80 is also useful: \(\{\Phi_6<0\}\) is the open extending region in the positive-definite quadratic stratum. The set \(\{\Phi_6\le0\}\) includes the equality set and is not open. At \(\Phi_6=0\), the quadratic equation is solved at its minimizer, where transversality is lost.

---

## 6. Validity of the second-representation calculation

### Correct parts

The conversion formulas for pullback are correct:

\[
(g_y)_{ij}
=\frac{\partial X^a}{\partial y^i}
 \frac{\partial X^b}{\partial y^j}
 g_{ab}(X(y)),
\]
and similarly for \(\omega\). The exponential reconstruction retains terms through \(H^4/4!\), which is sufficient through coordinate degree eight because \(H\) begins in degree two.

The resulting map has

\[
X(0)=0,\qquad DX(0)=I,
\]
so it is a valid local formal coordinate change. Pullback by any such map preserves the almost-Kähler equations and transforms the Einstein tensor covariantly. Thus the agreement

\[
6.14\times10^{-8}\longleftrightarrow6.73\times10^{-8},
\]
\[
1.25\times10^{-7}\longleftrightarrow1.41\times10^{-7},
\]
\[
7.69\times10^{-9}\longleftrightarrow8.44\times10^{-9}
\]
is meaningful. It independently exercises the general \((g,\omega)\) evaluator, closure, compatibility, monomial conventions, and torsion normalization.

### The exponential-map recursion is not the geodesic recursion

Write the true exponential map as

\[
X(y)=\sum_{m\ge1}X_m(y),\qquad X_1(y)=y,
\]
where \(X_m\) is homogeneous of degree \(m\). Let

\[
\mathcal R=y^i\partial_{y^i}.
\]

The radial geodesic \(x(t)=X(ty)\) satisfies

\[
(\mathcal R^2-\mathcal R)X^a
+
\Gamma^a_{bc}(X)
(\mathcal RX^b)(\mathcal RX^c)=0.
\]

Hence the correct homogeneous recursion is

\[
m(m-1)X_m^a
=
-\Big[
\Gamma^a_{bc}(X)
(\mathcal RX^b)(\mathcal RX^c)
\Big]_m.
\]

The script instead uses

\[
m(m-1)X_m^a
=
-\big[\Gamma^a_{bc}(X)y^by^c\big]_m,
\]
which replaces \(\mathcal RX\) by \(y\). Since the source metric already has \(\Gamma(0)=0\), one gets \(X_2=0\), and the script agrees with the true recursion through degree four. In general the first omitted velocity contribution appears in degree five through terms of the form

\[
\Gamma_1(y)\,y\,(\mathcal RX_3).
\]

Therefore the generated coordinates are not demonstrated to be exponential normal coordinates beyond low degree. In particular, the full radial Gauss-lemma identity

\[
g_{ij}(y)y^j=\delta_{ij}y^j
\]
has not been established.

This does not invalidate the second-representation residuals. The computed \(X\) is still an invertible formal map, and the source Darboux coordinates already satisfy \(dg(0)=0\). Consequently the pulled-back metric remains point-normal, exactly as shown by

\[
\|\partial g_y(0)\|=0.
\]

The proper interpretation is therefore “an independent \((g,\omega)\) coordinate representation with point-normal metric,” rather than “the true geodesic exponential representation.”

---

## 7. What remains unresolved

The current data do not establish any of the following:

1. **An all-orders formal solution.**  
   No \(H_{10},H_{12},\ldots\) have been constructed, and no involutivity theorem is supplied.

2. **An analytic Einstein almost-Kähler germ.**  
   Even an all-orders formal series would require a convergence theorem or another local existence argument.

3. **A closed Einstein almost-Kähler four-manifold with \(s<0\).**  
   The data contain no compact assembly, global continuation, topology realization, or control of all torsion zeros.

4. **A universal formula for \(\Phi_6\).**  
   Universality of the row \(\ell\), quadratic dependence on \(\lambda\), and both signs of \(\Phi_6\) are numerical facts over the sampled jets. No \(U(2)\)-invariant symbolic expression has yet been given.

5. **A theorem about the whole strict cone.**  
   The reconstruction is valid on the sampled regular stratum where the relevant ranks are stable and \(H_\pi\) is positive definite. Other rank strata have not been classified.

---

## 8. Highest-value next mathematical object

The first genuinely new prolongation is the projected \(E_8\) equation, not another computation involving \(H_8\). In the even branch it has the form

\[
\Pi_8
E_8(H_2,H_4,H_6,H_8,H_{10}=0)=0,
\]
where \(\Pi_8\) projects onto the cokernel of the flat symbol

\[
L_8:H_{10}\longmapsto E_8.
\]

It corresponds to the \(84\) coefficients of the degree-six part of the scalar compatibility. Its nonlinear terms include \(H_4H_6\), \(H_2H_8\), and cubic expressions such as \(H_2H_4H_4\). The \(H_5H_5\) term disappears when exact even parity is imposed.

The scientifically decisive version of this object is its restriction to the full \(E_0,\ldots,E_6\) solution manifold, not merely its value at one arbitrarily selected reconstruction. A nonzero projected residual at one finite jet would only exclude that particular lower jet; the free coordinates left by the order-\(6\) construction can alter the \(E_8\) compatibility.

The best numerical seed in the supplied data is `F012_gen5_lam-5`: it has the largest subzero \(\Phi_6\) margin, the smallest \(H_4,H_6,H_8\) norms among the extending \(\lambda=-5\) examples, and the smallest two-representation residual.

The corresponding invariant derivation is equally concrete. Taking the homogeneous degree-four part of

\[
\Delta q
-8\operatorname{tr}V^2
+24|\eta|^2
+\frac{3s}{2}q
+\frac94q^2
-16\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle=0
\]
at a nondegenerate zero produces exactly \(35\) scalar coefficients. Eliminating the \(34\) adjustable directions should recover the universal row \(\ell\), the positive \(12\)-dimensional quadratic block, and the Schur complement \(\Phi_6\). This would convert the present floating construction into an invariant explanation and supply the natural degree-six scalar expression underlying \(E_8\).

In summary: Step 67 establishes a highly persuasive finite \(8\)-jet phenomenon and removes the proposed \(E_6\) exclusion of positive-index nondegenerate zeros. The coordinate-converted residuals remain valid, although the map is not the true exponential map beyond low degree. The next unresolved local content begins at \(E_8\), with metric terms through \(H_{10}\) and \(84\) scalar-compatibility coefficients.
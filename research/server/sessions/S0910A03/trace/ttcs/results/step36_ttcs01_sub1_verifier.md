# TTCS Independent Branch Record

```json
{
  "step_id": 36,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md",
    "Sessions/S0910A03/workspace/notes/step35_degenerate_flow_existence.md",
    "Sessions/S0910A03/workspace/notes/step35_cutoff_jet_continuation.md",
    "Sessions/S0910A03/workspace/notes/step35_first_exit_bootstrap_assembly.md",
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Review the Step 35 analytic handoff for the normalized fixed-cutoff Ricci flow in the four-dimensional negative Ishida--LeBrun route. Focus on four interfaces: (i) whether the unregularized fixed J6 persistence lemma is a genuine valid advance and exactly what assumptions it still needs; (ii) whether the Step 35 DeTurck/existence note uses the correct gauge and transported coefficient, and whether its epsilon/Schauder argument actually gives epsilon-independent smooth existence; (iii) whether the cutoff-jet continuation note proves an extension criterion on [0,Tmax) or instead assumes smoothness/uses uncontrolled quantities such as unweighted T or a∇Rm; and (iv) whether terminal calibration still needs a separate global Q=∫|E|^2 estimate rather than J6 or |aE|. Give a direct scientific memo with corrected mathematical status and the next proof targets, not publication advice.

## Output

# Scientific memo on the Step 35 analytic handoff

## 1. Fixed \(J_6\) persistence

The unregularized \(J_6\) argument is a real mathematical improvement, under the first-exit hypotheses stated in the note.

The strong point is the use of
\[
s=|E|^2,\qquad J_6=\int \eta^2 a^4s^3\,d\mu ,
\]
rather than powers of \(|E|\) requiring Kato smoothing. Since \(s^3\) and the test function
\[
q=3\eta^2a^4s^2
\]
are smooth tensor polynomials, the time derivative of \(J_6\) does not generate any \(\varepsilon\)-remainder at \(E=0\). The Sobolev function
\[
w_6=\eta a^{5/2}s^{3/2}=\eta\chi^5|E|^3
\]
is \(W^{1,2}\) and \(C^1\), which is enough for the Sobolev step.

The decisive absorption is also correct in form:
\[
P_6=\int Fw_6^2
 \le \|F\|_{2,U}\|w_6\|_4^2
 \le C\mathcal S K_2^{1/2}\left(X_6+r^{-2}J_6\right).
\]
Thus the \(J_6\) lemma uses only the unweighted component curvature energy
\[
K_2(t)=\int_U F^2\,d\mu_t
\]
or equivalently \(\int \eta^2F^2\) when \(\eta=1\) on \(\operatorname{supp}\chi\). It does not need the \(q=3\) curvature seed \(Y=K_3\), nor the curvature Moser endpoint.

The assumptions still needed are substantial and should be part of the lemma statement:

\[
\mathcal S(t)\,K_2(t)^{1/2}\le \gamma_0
\]
on the moving support, with \(\gamma_0\) small enough to absorb \(P_6\);

\[
\|u\|_4^2\le \mathcal S(t)\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right)
\]
for \(u\) supported in the auxiliary region;

\[
a=\chi^2,\qquad 0\le a\le1,\qquad |d\chi|_{g(t)}\le Cr^{-1};
\]

\[
\eta=1 \text{ near } \operatorname{supp}\chi,\qquad a=da=0 \text{ on } \operatorname{supp}d\eta;
\]

smooth existence of the fixed-cutoff flow on the interval in question, with metric comparability sufficient to keep these estimates valid.

Two textual points in the note need correction for a complete write-up.

First, in §3.6 the first-derivative cutoff term should have the same power as \(I_1\):
\[
C\int \eta^2a^4|da|\,s^{5/2}|\nabla E|.
\]
The displayed \(s^{3/2}\) loses one factor of \(s\). With \(s^{5/2}\), Young gives exactly
\[
\varepsilon X_6+C_\varepsilon r^{-2}J_6.
\]

Second, the Hessian-\(a\) identity in §3.5 should be written as
\[
T_H=\int a_{ij}\,q\,B_0^{ij}(E),
\qquad
B_0^{ij}=2g^{ij}|E|^2+2\tau E^{ij}-4E^{ik}E_k{}^j,
\]
with \(B_0=O(s)\), \(\nabla B_0=O(s^{1/2}|\nabla E|)\). The estimates in §3.5 are consistent with this formulation. The notation \(B^{ij}(q)\) obscures where the factors \(a^4s^2\) sit.

With these corrections, the derived inequality
\[
J_6'+cX_6\le C(1+r^{-2})J_6+CP_6
\]
and the absorption
\[
P_6\le C\gamma(X_6+r^{-2}J_6)
\]
give
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0)
\]
under the stated first-exit assumptions. This is a genuine advance, but it is not a substitute for the curvature \(K_2\) persistence estimate.

---

## 2. DeTurck/existence note

The Step 35 existence note does not yet give a correct proof of smooth existence for the normalized fixed-cutoff flow.

The main geometric issue is the gauge. For a fixed-cutoff flow
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g),
\]
the DeTurck construction must transport the coefficient in the gauged equation. Yang’s Section 8 source uses
\[
\hat a=(\chi\circ\varphi_t^{-1})^2
\]
in the hatted metric equation. For the normalized flow the corresponding gauged equation should have the form
\[
\partial_t\hat g
=
-2\hat a(\operatorname{Ric}_{\hat g}+\hat g)
+\mathcal L_{\hat a W(\hat g)}\hat g,
\]
or Yang’s equivalent \(\hat\delta^*(\hat a\,\omega)\) formulation. The coefficient belongs inside the gauge vector, so the Lie derivative contains the \(d\hat a*W\) terms.

The Step 35 note instead writes
\[
\partial_t g
=
-2a(\operatorname{Ric}+g)+a(\nabla W+\nabla W).
\]
This is not naturally equivalent to the original fixed-cutoff flow. If one pulls back a hatted solution with fixed coefficient \(a\), the coefficient becomes \(\varphi_t^*a\), not the original fixed \(\chi^2\). If one tries to cancel \(a\mathcal L_Wg\) by a vector field \(aW\), the missing \(da*W\) terms remain. The principal symbol is similar, but the exact geometric equivalence is not.

The \(\varepsilon\)-regularized Schauder argument also does not establish \(\varepsilon\)-independent smooth existence. Standard parabolic Schauder constants depend on the lower ellipticity constant, hence on \(\varepsilon^{-1}\) for
\[
a_\varepsilon=\chi^2+\varepsilon.
\]
The statement that interior Schauder estimates only need \(a_\varepsilon\ge0\) is not a standard theorem. On the region where \(a\) is small, the displayed energy inequality contains a positive term of the form
\[
C(2a_0+\varepsilon)\|h\|_{H^{k+1}}^2
\]
and does not close a \(C^k\) or \(H^k\) estimate by itself.

The reliable source object here is Yang’s Theorem 8.2: local Ricci flow existence is obtained through a transported-coefficient DeTurck system and smooth tame estimates, or through a regularized flow plus energy bounds independent of the regularization. The normalized term \(-2\chi^2g\) is lower order, so it should be absorbable into Yang’s construction, but that adaptation still has to be written with the transported coefficient and the gauge term \(\mathcal L_{\hat aW}\hat g\).

So the present existence note is useful as a heuristic decomposition, but not as a proof of smooth existence for the normalized fixed-cutoff equation.

---

## 3. Cutoff-jet continuation note

The Step 35 cutoff-jet note does not prove an extension theorem on \([0,T_{\max})\). It assumes too much smoothness and uses quantities not controlled by the zero-order bootstrap.

The plateau part is essentially sound after shrinking to an interior plateau where \(a=1\) on a full neighborhood. There the equation is ordinary normalized Ricci flow, and the Moser endpoint
\[
\|aF(t)\|_\infty\le C\gamma/t
\]
gives
\[
|\operatorname{Rm}|\le C/t
\]
on that plateau. Shi estimates then give derivative bounds at positive time on a smaller plateau.

The transition-region argument is the weak part. The coefficient
\[
\Lambda(t)
=
1+r^{-2}+\|T(t)\|_\infty
+\|a\nabla\operatorname{Rm}(t)\|_\infty^{2/(p-1)}
\]
is not controlled by the bootstrap. The zero-order estimate controls \(aF\), not \(F\), and not \(T=\operatorname{Rm}+G\). Near \(\chi=0\), a bound for
\[
U=aT
\]
does not give a pointwise bound for \(T\). Likewise, \(a\nabla\operatorname{Rm}\) is not available from the zero-order theory.

The note says these quantities are finite because the solution is smooth. That is true on compact subintervals strictly before a terminal time, but it does not give uniform bounds as \(t\uparrow T_{\max}\). Therefore it cannot be used to extend the solution through \(T_{\max}\).

The correct continuation mechanism is the shifted-curvature Wang induction from Step 27. The relevant objects are
\[
T=\operatorname{Rm}+G,\qquad U=aT,
\]
with
\[
\operatorname{Ric}(U)=a(\operatorname{Ric}+g)=aE.
\]
The differentiated system must estimate \(\nabla^mU\) together with \(\nabla^{m+1}\chi\), while separately proving finite unweighted \(L^p\) control of \(\nabla^mT\). The top cutoff term
\[
\chi\,\nabla^{m+2}\chi*U
\]
has to be integrated by parts once so that diffusion with weight \(a=\chi^2\) absorbs the derivative on \(\nabla^mU\). This is exactly the Wang-type triangular mechanism. The Step 35 cutoff-jet note does not carry out that mechanism; it replaces it by coefficients involving \(\|T\|_\infty\) and \(\|a\nabla\operatorname{Rm}\|_\infty\).

Thus, for continuation, the mathematically relevant proof object is still the detailed shifted-curvature induction, not the short cutoff-jet note.

---

## 4. Terminal calibration and the global \(Q\) estimate

Terminal calibration still needs a separate global estimate for
\[
Q(t)=\int_M |E|^2\,d\mu_t.
\]

Neither \(J_6\) nor \(\|aE\|_\infty\) supplies this.

The \(J_6\) estimate controls
\[
\int \eta^2a^4|E|^6.
\]
It is weighted by \(a^4\), so it is blind where \(a\) is small or zero. On an interior plateau it can give a local \(L^2\) estimate by Hölder:
\[
\int_{\{a=1\}}|E|^2
\le
\operatorname{Vol}^{2/3}J_6^{1/3},
\]
but the displayed calibration inequality uses the unweighted global integral \(\int_M|E|^2\).

The pointwise estimate
\[
\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}
\]
controls the velocity
\[
\partial_tg=-2aE
\]
and therefore metric drift. It does not control \(|E|\) where \(a\) is small.

The needed estimate is the separate homogeneous \(Q\)-energy inequality from the Step 23 bridge:
\[
Q'(t)+c\int_M a|\nabla E|^2
\le
Cr^{-2}Q(t)
+
C\sum_j\int_{U_j} aF|E|^2.
\]
On each good support,
\[
\int_{U_j} aF|E|^2
=
\int_{U_j} F(\chi_jE)^2
\le
\|F\|_{2,U_j}\|\chi_jE\|_4^2
\le
C\gamma_j
\left(
\int_{U_j}a|\nabla E|^2
+r^{-2}\int_{U_j}|E|^2
\right),
\]
so small \(\gamma_j\) absorbs the gradient term and gives
\[
Q(t)\le e^{Cr^{-2}t}Q(0).
\]
This estimate is independent of \(J_6\). It is the object that feeds the terminal calibration inequality.

The Step 35 handoff should therefore keep three defect estimates distinct:

\[
J_6(t)\lesssim J_6(0)
\quad\text{for the defect Moser seed;}
\]

\[
\|aE(t)\|_\infty
\quad\text{for metric drift;}
\]

\[
Q(t)\lesssim Q(0)
\quad\text{for terminal calibration.}
\]

---

## Corrected mathematical status

- The \(s\)-based unregularized \(J_6\) persistence lemma is a valid advance once the \(K_2\), Sobolev, cutoff-geometry, and smooth-flow assumptions are explicitly included.

- The Step 35 DeTurck/existence note does not yet prove existence for the normalized fixed-cutoff flow. The correct construction needs Yang’s transported coefficient and a gauge term with the coefficient inside the Lie derivative. The proposed \(\varepsilon\)/Schauder passage does not provide \(\varepsilon\)-independent \(C^\infty\) bounds.

- The cutoff-jet continuation note gives qualitative observations for an already smooth solution, but not an extension theorem. The transition-region estimates use \(\|T\|_\infty\) and \(\|a\nabla\operatorname{Rm}\|_\infty\), which are not produced by the zero-order bootstrap. The shifted-curvature Wang induction remains the needed analytic proof object.

- Terminal calibration requires the separate global \(Q=\int|E|^2\) estimate. Weighted \(J_6\) persistence and the weighted pointwise bound for \(aE\) do not replace it.
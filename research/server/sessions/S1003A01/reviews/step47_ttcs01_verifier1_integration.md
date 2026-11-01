# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 47,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step47_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step47_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the mathematics of the Step-47 O10 note, which claims to reverse Step 46's main local conclusion. Setting (from the inherited corpus): s=-4 metric, actual Seiberg-Witten fields D_A^+Phi=0, F_A^+=2i sigma(Phi), nabla^*nabla Phi=(1-rho/2)Phi, cubic torsion t_Phi=sum_i c(e^i)Phi⊗(Phi∧nabla_i Phi) in E=S^-⊗L with determinant connection 3A, endpoint rho*=4/3, m*=128/81, a=sqrt2/3, corpus Weitzenböck relation (L-2)t=D*Dt+(Gamma-1)t-R t and Proposition 7: D^-t=-4 sum P_i⊗(Phi∧P_i)+K(W^+). Please verify or correct, with explicit reasoning: (a) identity (1.1) and its sign/normalization, and whether the Step-46 raw-TN residual q=-2v is truly just the omitted s/4 and F^-_{3A} Weitzenböck terms (so that it is not a candidate obstruction); (b) the exact TN claims: Phi_TN=sqrt(rho*)e1+a fbar e2 Dirac-harmonic with delta≡0, t=sqrt2 rho* a dfbar in Lambda^{0,1}_{I3}, |t|^2=m*/V; the GH two-form families and closedness criteria, h=x3/V; the mismatch (2.3) and its use; (c) formula (3.1) |N|^2=sin^2 s |nabla tau|^2 and whether J_+ selected by Phi_TN is as described; (d) whether the corpus commutator (3.8) can legitimately be applied on the physical block to give the critical lower bound (3.2) for ∫|∇N_tau|^2, and what hypotheses (closure, rho=rho*, type (1,1)) actually fail in a TN core; (e) whether the conditional reduction in §4.4 (density-free O10 follows from ||∇N_tau||_{2,av}->0) is sound or overreaching, and whether the residual count of §2 genuinely needs only a null background jet. Identify any error that would change the conclusion that a TN core carries no local order-L^6 payment at the energy scale. Give a direct mathematical memo.

## Integrated Scientific Memo

# Mathematical verification memo: Step 47 O10

## Bottom line

Step 47 correctly removes **one specific alleged obstruction** from Step 46: the raw Ricci-flat, untwisted calculation
\[
(\nabla^*\nabla-2)t_{\rm TN}=-2t_{\rm TN}
\]
does not represent the physical \(s=-4\), \(3A\)-twisted resolvent. The omitted scalar-curvature and determinant-curvature terms cancel that \(-2t\) on the calibrated endpoint torsion line. Thus Step 46’s bound
\[
\|q_{\rm TN}\|_2^2\ge 16\pi^2m_*L^6
\]
is not a valid physical obstruction.

However, Step 47 does **not** establish its stronger conclusion that a physical TN/TNAdS core has no local order-\(L^6\) residual. The displayed \(\Phi_{\rm TN}\), its torsion, and the displayed nonflat determinant curvature do not constitute one exact Seiberg–Witten solution. The unresolved leading term is
\[
D_{3A}^{-*}\delta,\qquad
\delta=\sum_iP_i\otimes(\Phi\wedge P_i).
\]
A null first jet does not control its derivative. A physical second-jet correction can contribute \(O(1)\) pointwise and therefore \(O(L^6)\) in squared norm over a block. The defensible conclusion is therefore:

\[
\boxed{\text{The raw }-2t\text{ payment disappears, but absence of every local }O(L^6)
\text{ payment remains unproved.}}
\]

---

## 1. Weitzenböck identity and normalization

Let \(B=3A\), and use
\[
(D^-_B)^*D^-_B
=\nabla_B^*\nabla_B+\frac{s}{4}+\frac12c(F_B^-).
\]
For \(s=-4\),
\[
\begin{aligned}
(\nabla_B^*\nabla_B-2)t
&=(D^-_B)^*D^-_Bt-\frac{s}{4}t-\frac12c(F_B^-)t-2t\\
&=(D^-_B)^*D^-_Bt-
\left(1+\frac12c(F_B^-)\right)t.
\end{aligned}
\]
Thus Step 47’s (1.1) is correct, provided \(\mathcal L_B=\nabla_B^*\nabla_B\):
\[
\boxed{
(\mathcal L_{3A}-2)t
=D_{3A}^{-*}D^-_{3A}t-
\left(1+\frac12c(F^-_{3A})\right)t.}
\]

Combining this with Proposition 7,
\[
D^-_{3A}t_\Phi=-4\delta+\mathcal K(W^+),
\]
and \(W^+=0\), gives
\[
\boxed{
q=-4D^{-*}_{3A}\delta-
\left(1+\frac12c(F^-_{3A})\right)t_\Phi.}
\]

There is a notation error in Step 47’s (1.3). From the quoted corpus identity
\[
(\mathcal L-2)t=D^*Dt+(\Gamma-1)t-\mathcal Rt,
\]
the algebraic term is
\[
(\Gamma-\mathcal R-1)t
=-\left(1+\frac12c(F^-_{3A})\right)t.
\]
Writing merely \((\Gamma-1)t\) is valid only if \(\Gamma\) has been silently redefined to absorb \(-\mathcal R\).

### Why the raw \(-2t\) disappears

At the endpoint,
\[
F_A^-=\frac{i}{3}(e^{12}-e^{34}),\qquad
F_{3A}^-=i(e^{12}-e^{34}).
\]
On the selected \(S^-\) eigenline containing the endpoint torsion,
\[
\frac12c(F^-_{3A})t=-t,
\]
so
\[
\left(1+\frac12c(F^-_{3A})\right)t=0.
\]
Hence a Dirac-harmonic physical torsion has \(q=0\) at the calibrated endpoint.

By contrast, on the untwisted Ricci-flat tangent,
\[
s=0,\qquad F_{3A}=0,\qquad D^-t=0,
\]
and therefore
\[
(\nabla^*\nabla-2)t=-2t.
\]
The missing \(+2t\) consists of one unit from the scalar-curvature term and one from the determinant-curvature action. Step 47’s verbal sentence about “\(-1+1\cdot0\)” is garbled, but the actual cancellation is correct.

Thus Step 46’s raw-TN pairing is an artefact of changing the operator. It does not furnish a physical local payment.

---

## 2. Exact TN tangent statements

These statements are correct **for the untwisted Ricci-flat tangent model**.

Let
\[
\Phi_{\rm TN}=\sqrt{\rho_*}\,e_1+a\bar f\,e_2,
\qquad f=x_1+ix_2,\qquad a=\frac{\sqrt2}{3}.
\]

### Dirac and rough harmonicity

With \(e_1,e_2\) parallel in the hyperkähler frame and
\(e_2\leftrightarrow\Lambda^{0,2}_{I_3}\),
\[
c(d\bar f)e_2=0.
\]
Since \(\bar f\) is harmonic on a Gibbons–Hawking metric,
\[
D^+\Phi_{\rm TN}=0,\qquad
\nabla^*\nabla\Phi_{\rm TN}=0
\]
for the flat twisting connection.

### Vanishing of \(\delta\)

Here
\[
P_i=a(\partial_i\bar f)e_2,\qquad
\Phi\wedge P_i
=\sqrt{\rho_*}\,a(\partial_i\bar f)e_1\wedge e_2.
\]
Therefore
\[
\delta
=\sqrt{\rho_*}\,a^2
g^{ij}(\partial_i\bar f)(\partial_j\bar f)e_2.
\]
Because \(d\bar f\) is isotropic for the complex-bilinear metric,
\[
g^{-1}(d\bar f,d\bar f)=0,
\]
and hence
\[
\boxed{\delta_{\rm TN}=0.}
\]

### Torsion

The \(e_2\)-component of \(\Phi\) does not contribute because
\(c(d\bar f)e_2=0\), so
\[
\boxed{
t_{\Phi_{\rm TN}}=\sqrt2\,\rho_*a\,d\bar f.}
\]
Since
\[
|d\bar f|^2=\frac2V,
\]
one obtains
\[
|t|^2
=2\rho_*^2a^2\frac2V
=\frac{128}{81V}
=\frac{m_*}{V}.
\]
Also
\[
D^-t=0.
\]

These are valid tangent identities. They are not exact identities for the nonflat \(A^{\rm core}\) introduced later in Step 47.

---

## 3. The tangent spinor and determinant curvature are not one physical solution

Step 47 combines:

1. an untwisted Ricci-flat spinor \(\Phi_{\rm TN}\);
2. its torsion computed in a parallel frame;
3. a nonflat curvature
   \[
   F_A^{\rm core}
   =i\left(\frac23\omega_3+\frac13\beta^-_{x_3/V}\right).
   \]

These do not form an exact Seiberg–Witten configuration.

First, a frame parallel for the untwisted spin connection is not parallel for the nonflat determinant connection. Thus the equalities
\[
D_A^+\Phi_{\rm TN}=0,\qquad
\nabla_A^*\nabla_A\Phi_{\rm TN}=0,\qquad
\delta=0
\]
do not persist unchanged after inserting \(A^{\rm core}\).

Second,
\[
|\Phi_{\rm TN}|^2=\rho_*+a^2|f|^2,
\]
and \(2i\sigma(\Phi_{\rm TN})\) contains linear and quadratic terms in \(f\), whereas
\[
(F_A^{\rm core})^+=\frac{2i}{3}\omega_3
=2i\sigma(\sqrt{\rho_*}e_1)
\]
has no such terms. Hence
\[
(F_A^{\rm core})^+\ne 2i\sigma(\Phi_{\rm TN})
\]
away from \(f=0\).

This is acceptable as leading blow-up data, but Proposition 7 and the physical residual formula cannot be applied exactly to this hybrid package.

---

## 4. GH two-forms, closedness, and mismatch

With
\[
\beta_h^\pm=\eta\wedge dh\mp V*_3dh,
\qquad d\eta=*_{3}dV,
\]
the analytic calculation gives, in the stated orientation,
\[
*_4\beta_h^+=\beta_h^+,\qquad
*_4\beta_h^-=-\beta_h^-.
\]
Furthermore,
\[
d\beta_h^+=-V(\Delta h)\,\mathrm{vol}_3,
\]
and
\[
d\beta_h^-
=V^{-1}\operatorname{div}(V^2\nabla h)\,\mathrm{vol}_3.
\]
Therefore:
\[
\boxed{\beta_h^+\text{ is closed iff }\Delta h=0,}
\]
\[
\boxed{\beta_h^-\text{ is closed iff }\operatorname{div}(V^2\nabla h)=0.}
\]

For
\[
h=\frac{x_3}{V},
\]
\[
V^2\nabla\left(\frac{x_3}{V}\right)
=V\nabla x_3-x_3\nabla V,
\]
so, away from the origin,
\[
\operatorname{div}\left(V^2\nabla(x_3/V)\right)
=V\Delta x_3-x_3\Delta V=0.
\]
The lifted form extends smoothly over the nut. Thus \(h=x_3/V\) is the correct closed ASD continuation.

The mismatch asymptotic is also correct:
\[
\boxed{
\int_{B_R}
\left|\beta^-_{x_3/V}-\beta^-_{x_3}\right|^2
=
\frac{64\pi^2}{3}\ell^3R
+O\!\left(\ell^4[1+\log(R/\ell)]\right).}
\]
Consequently, using the endpoint Clifford cancellation and
\(\|c(\beta)\|_{\rm op}=\sqrt2|\beta|\),
\[
\int\left|
\frac12c\!\left(i(\beta^-_{x_3/V}-\beta^-_{x_3})\right)t
\right|^2
\le
\frac{32\pi^2}{3}m_*\ell^3R+\cdots.
\]
At \(R\asymp L=\ell^{1/3}\), this is \(O(L^{10})\).

### Script defect

The JSON records both `self_dual` and `anti_self_dual` as false for every form, including the hyperkähler family. Thus the stored booleans do not verify the prose. The likely cause is the unevaluated \(|\sin\theta|\) in \(\sqrt{\det g}\). The analytic type calculation above is reliable; the script’s Hodge-type test must be repaired.

### Determinant-sector qualification

The asymptotic continuation is not unique without fixing determinant holonomy/relative charge. One may add a decaying closed ASD harmonic form proportional to \(d(\eta/V)\). A coefficient of order one has \(L^2\)-size \(O(\ell^2)=O(L^6)\) and can therefore create an energy-scale algebraic residual. Thus “free core” additionally requires the relevant determinant holonomy mode to be absent or \(o(1)\); Step 47 implicitly selects that sector.

---

## 5. Formula for \(J_+\) and \(N_\tau\)

Writing
\[
u=\frac{\Phi}{|\Phi|}
=\cos s\,e_1+\sin s\,e^{-i\arg f}e_2,
\qquad
\tan s=\frac{a|f|}{\sqrt{\rho_*}},
\]
the Hopf map gives
\[
J_+
=\cos(2s)I_3+\sin(2s)K_f,
\]
where \(K_f\) is a phase-dependent linear combination of the two parallel complex structures anticommuting with \(I_3\).

Thus Step 47 is incorrect in calling \(K\) itself a fixed parallel complex structure: its phase varies with \(\arg f\). Nevertheless, the pointwise projector calculation is unaffected. If the derivative index \(\xi\) lies in \(\Lambda^{0,1}_{I_3}\), then \(K_f\xi\) is orthogonal to \(\xi\) with equal norm, and
\[
|P^{1,0}_{J_+}\xi|^2=\sin^2s\,|\xi|^2.
\]
Hence
\[
\boxed{
|N_\tau|^2
=\sin^2s\,|\nabla\tau|^2
=
\frac{a^2|f|^2}{\rho_*+a^2|f|^2}
|\nabla\tau|^2.}
\]
Formula (3.1) is therefore correct for the tangent model.

The phase variation of \(K_f\) does matter after differentiating \(N_\tau\); it contributes at the critical scale to \(\nabla N_\tau\).

Also, any claim involving
\[
\kappa^2=\frac{m}{4\rho_*^3}
\]
is exact only if \(\rho\) is frozen at \(\rho_*\). For the displayed full spinor,
\[
\rho=\rho_*+a^2|f|^2.
\]
On \(B_L\) this alters the leading weighted integral only by lower-order terms, but the equality is asymptotic rather than an exact identity for the full model.

---

## 6. The corpus commutator does not presently prove (3.2)

For an exact physical solution, the vanishing
\[
F^E(Z_1,Z_2)=0
\]
is justified by:

- Einstein geometry, which kills the trace-free Ricci block;
- \(F_A^+=2i\sigma(\Phi)\), which is \((1,1)\) for \(J_+=J(\Phi/|\Phi|)\);
- every ASD two-form being \((1,1)\) for a positively oriented orthogonal complex structure.

Neither \(\rho=\rho_*\) nor constancy of \(\rho\) is required for this curvature-type fact.

But these hypotheses fail for the displayed hybrid TN package:

- its \(F^{\rm core,+}\) is aligned with \(I_3\), not with the rotating \(J_+\);
- hence it has a nonzero \((2,0)+(0,2)\) part relative to \(J_+\);
- the structural adapted-frame closure used in corpus (3.8) has not been verified for this model;
- the frame coefficients \(L_i\) need not be uniformly bounded near a core;
- the \(\tau\)-adapted frame degenerates at the nut because \(m=|t|^2\to0\).

Most importantly, the passage
\[
2\kappa B=
-\nabla_{Z_1}A_2+\nabla_{Z_2}A_1+\sum_iL_iA_i
\]
to
\[
\|\nabla N_\tau\|_2
\gtrsim
\|\kappa B\|_2-C\|N_\tau\|_2
\]
requires a uniform bound on the frame coefficients and projector derivatives. In a TN core those coefficients can be critical, not bounded; the \(L_iA_i\) term can have the same scale as \(\kappa B\). Thus (3.2), as stated, is not justified by corpus (3.8).

### Direct replacement

The tangent model nevertheless has genuine critical current-gradient energy. From (3.1),
\[
|N_\tau|
=
\kappa_*\sqrt{m_*}\,\ell
\frac{r\sin\theta}{(r+\ell)^2}
\bigl(1+O(r^2)\bigr),
\qquad \kappa_*^2=\frac16.
\]
Kato’s inequality gives
\[
|\nabla N_\tau|\ge |d|N_\tau||.
\]
Direct integration then yields the convention-free lower bound
\[
\boxed{
\int_{\rm TN}|\nabla N_\tau|^2
\ge
\frac{16\pi^2}{5}\kappa_*^2m_*\ell^2
=
\frac{8\pi^2}{15}m_*\ell^2
=
\frac{E_{\rm core}}{15},
}
\]
up to the truncation error at \(R\gg\ell\). At minimum, an annulus
\(2\ell<r<3\ell\) gives a positive \(c\,\ell^2\) lower bound.

This establishes the critical derivative cost for the explicit tangent model without invoking the questionable commutator estimate. Transfer to physical blocks requires sufficiently strong rescaled \(C^1\) convergence.

---

## 7. The decisive gap: a null first jet does not control \(D^{-*}\delta\)

Step 47 asserts
\[
\|D^{-*}\delta\|_2^2=O(\ell^3L)
\]
from a null background jet and the modulation
\(V^{-1/2}-1=O(\ell/r)\). This does not follow.

A generic perturbation with
\[
\delta=O(\ell/r)
\]
has
\[
\nabla\delta=O(\ell/r^2).
\]
In the ALF region,
\[
d\mu\asymp \ell r^2\,dr,
\]
so
\[
\int_\ell^L|\nabla\delta|^2d\mu
\asymp
\int_\ell^L
\frac{\ell^2}{r^4}\,\ell r^2\,dr
\asymp\ell^2=L^6.
\]
Thus the natural generic size is precisely the energy scale.

Moreover, a physical \(s=-4\) solution necessarily has a nontrivial second jet because
\[
\nabla_A^*\nabla_A\Phi=(1-\rho/2)\Phi
\approx\frac13\Phi_0
\]
at \(\rho=\rho_*=4/3\). A quadratic spinor correction gives an \(O(r)\) correction to \(P=\nabla_A\Phi\). Unless its interaction with the null first jet is shown to remain tangent to the algebraic null set \(\delta=0\),
\[
\delta=O(r),\qquad D^{-*}\delta=O(1),
\]
and hence
\[
\|D^{-*}\delta\|_2^2=O(\operatorname{Vol}B_L)=O(L^6).
\]

The claimed smaller \(O(\ell^3L)=O(L^{10})\) size requires an additional cancellation, for example
\[
\delta=O(\ell),\qquad \nabla\delta=O(\ell/r),
\]
which is a **second-jet compatibility condition**, not merely a null first-jet condition.

Therefore the physical residual count requires:

1. an exact or quantitatively accurate TNAdS Seiberg–Witten correction;
2. a prolonged null condition through the relevant second jet;
3. control of transverse components of \(\delta\);
4. one common connection in the Dirac, torsion, and curvature calculations;
5. exclusion/control of the decaying determinant-holonomy mode.

No supplied computation establishes these points.

---

## 8. Status of the §4.4 conditional reduction

The narrow statement is sound:

> If a sequence decomposes into a positive density of cores converging strongly to the displayed TN tangent, then normalized \(H^1\)-smallness of \(N_\tau\) excludes that phase, because each core contributes \(c\ell^2\) to \(\int|\nabla N_\tau|^2\).

The broader claim that density-free O10 follows along all nut-type escapes from
\[
\|\nabla N_\tau\|_{2,\mathrm{av}}\to0
\]
is overreaching. It additionally needs:

- a bubble decomposition proving all relevant concentration pieces are TN-like;
- strong enough convergence to transfer the core lower bound;
- control of the commutator product terms without the forbidden finite-density \(W^-\)/higher-Hessian bounds;
- a lower bound for \(\kappa\) if one wishes to infer \(B\to0\) from \(\kappa B\to0\);
- verification that every subsequent finite-density argument remains valid without \(W^-\) control.

Thus normalized \(H^1\)-smallness of \(N_\tau\) is a useful conditional exclusion criterion for a specified TN bubble phase, not yet a reduction of the full density-free theorem.

---

## 9. Additional correction to §4.2

The displayed arithmetic
\[
\frac{112}{9}+\frac{48}{9}-\frac{16}{9}=16
\]
is inconsistent with the preceding assignments and with positivity of
\(4\int m^2|c|^2\).

Using
\[
\int|dm|^2=\frac{16}{3}
\quad
\text{in units }\pi^2m_*^2\ell^2,
\]
and
\[
E_1=\frac23|dm|^2,\qquad E_2=\frac13|dm|^2,
\]
gives
\[
2\int E_1=\frac{64}{9},\qquad
3\int E_2=\frac{48}{9}.
\]
To obtain a total of \(16=144/9\), one would need
\[
4\int m^2|c|^2=\frac{32}{9},
\]
not a negative contribution. The qualitative “\(c\)-depleted” interpretation may still be meaningful, but the numerical balance must be recomputed, including the outer flux because the block is not periodic.

---

## Final verdict

### Verified

- Weitzenböck identity (1.1), with the stated normalization.
- Cancellation of the raw Ricci-flat \(-2t\) on the physical endpoint eigenline.
- Therefore Step 46’s specific \(16\pi^2m_*L^6\) raw-TN obstruction is invalid.
- Untwisted tangent identities:
  \[
  D\Phi_{\rm TN}=0,\quad
  \delta_{\rm TN}=0,\quad
  t=\sqrt2\rho_*a\,d\bar f,\quad
  |t|^2=m_*/V,\quad
  D^-t=0.
  \]
- GH closedness criteria, \(h=x_3/V\), and the mismatch asymptotic.
- Formula (3.1), with \(K\) understood as phase-dependent.

### Not verified

- That the displayed tangent spinor and determinant curvature form one physical solution.
- The claimed \(O(L^{10})\) estimate for \(D^{-*}\delta\) from only a null first jet.
- Application of corpus (3.8) with a uniform constant to obtain (3.2).
- The full §4.4 density-free reduction.
- The numerical energy identity in §4.2.

### Conclusion-changing issue

Yes: the uncontrolled physical second jet can generate
\[
\|D^{-*}\delta\|_2^2\asymp L^6.
\]
Therefore the source-supported conclusion is not “a TN core carries no local order-\(L^6\) payment,” but only:

\[
\boxed{
\text{The particular raw-TN resolvent payment }q=-2t\text{ is spurious.}
}
\]

To establish the stronger no-payment claim one must solve the physical TNAdS correction problem and verify the prolonged null condition controlling \(D^{-*}\delta\), together with the determinant-holonomy sector.
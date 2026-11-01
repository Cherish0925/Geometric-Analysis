# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step47_o10_tn_core_free_at_energy_scale.md",
    "Sessions/S1003A01/workspace/notes/step46_o10_finite_marked_block_and_spinor_matching.md",
    "Sessions/S1003A01/workspace/data/step47/tn_core_exact.json",
    "Sessions/S1003A01/workspace/data/step47/tn_core_split.json",
    "Sessions/S1003A01/workspace/scripts/step47_tn_core_exact.py"
  ]
}
```

## Task

Check the mathematics of the Step-47 O10 note, which claims to reverse Step 46's main local conclusion. Setting (from the inherited corpus): s=-4 metric, actual Seiberg-Witten fields D_A^+Phi=0, F_A^+=2i sigma(Phi), nabla^*nabla Phi=(1-rho/2)Phi, cubic torsion t_Phi=sum_i c(e^i)Phi⊗(Phi∧nabla_i Phi) in E=S^-⊗L with determinant connection 3A, endpoint rho*=4/3, m*=128/81, a=sqrt2/3, corpus Weitzenböck relation (L-2)t=D*Dt+(Gamma-1)t-R t and Proposition 7: D^-t=-4 sum P_i⊗(Phi∧P_i)+K(W^+). Please verify or correct, with explicit reasoning: (a) identity (1.1) and its sign/normalization, and whether the Step-46 raw-TN residual q=-2v is truly just the omitted s/4 and F^-_{3A} Weitzenböck terms (so that it is not a candidate obstruction); (b) the exact TN claims: Phi_TN=sqrt(rho*)e1+a fbar e2 Dirac-harmonic with delta≡0, t=sqrt2 rho* a dfbar in Lambda^{0,1}_{I3}, |t|^2=m*/V; the GH two-form families and closedness criteria, h=x3/V; the mismatch (2.3) and its use; (c) formula (3.1) |N|^2=sin^2 s |nabla tau|^2 and whether J_+ selected by Phi_TN is as described; (d) whether the corpus commutator (3.8) can legitimately be applied on the physical block to give the critical lower bound (3.2) for ∫|∇N_tau|^2, and what hypotheses (closure, rho=rho*, type (1,1)) actually fail in a TN core; (e) whether the conditional reduction in §4.4 (density-free O10 follows from ||∇N_tau||_{2,av}->0) is sound or overreaching, and whether the residual count of §2 genuinely needs only a null background jet. Identify any error that would change the conclusion that a TN core carries no local order-L^6 payment at the energy scale. Give a direct mathematical memo.

## Output

# Mathematical memo on Step 47

## Main determination

The Weitzenböck correction in §1 is essentially right and it does remove the specific Step-46 estimate obtained from \(q_{\mathrm{TN}}=-2v\). On the calibrated endpoint eigenspace, the scalar-curvature term and the \(3A\)-curvature term together replace the missing \(+2v\). Thus the number \(16\pi ^2m_*L^6\) from Step 46 is not a valid obstruction for a physical \(s=-4\) block.

The stronger conclusion that every Taub–NUT core has \(o(L^6)\) physical residual is not established. The exact computations concern an untwisted Ricci-flat tangent spinor and a separately chosen curvature continuation; these do not form one exact Seiberg–Witten configuration. The unresolved term is
\[
D_{3A}^{-*}\delta,\qquad
\delta=\sum_iP_i\otimes(\Phi\wedge P_i),
\]
which contains one derivative more than the null-jet relation \(\delta=0\). A null first jet by itself does not give the estimate
\(\|D^{-*}\delta\|_2^2=O(\ell^3L)\). A transverse correction can contribute exactly \(O(\ell^2)=O(L^6)\).

The derivative-current mechanism is plausible and can be proved directly for the displayed tangent model, but the corpus commutator does not presently justify (3.2) on the displayed core.

---

## 1. Weitzenböck identity and the Step-46 residual

Let \(B=3A\) and let
\[
D^-_B:S^-\otimes L\longrightarrow S^+\otimes L .
\]
With the standard Seiberg–Witten normalization,
\[
(D^-_B)^*D^-_B
 =\nabla_B^*\nabla_B+\frac{s}{4}+\frac12c(F_B^-).
\]
Therefore, when \(s=-4\),
\[
\begin{aligned}
(\nabla_B^*\nabla_B-2)t
 &= (D^-_B)^*D^-_Bt-\frac{s}{4}t-\frac12c(F_B^-)t-2t\\
 &= (D^-_B)^*D^-_Bt-\left(1+\frac12c(F_B^-)\right)t .
\end{aligned}
\]
Thus (1.1) has the correct sign and normalization, provided
\(\mathcal L_B=\nabla_B^*\nabla_B\).

Comparing this with the corpus formula
\[
(\mathcal L_B-2)t
 =D_B^{-*}D_B^-t+(\Gamma-1)t-\mathcal Rt
\]
gives
\[
\Gamma-\mathcal R=-\frac12c(F_B^-).
\]
Consequently Proposition 7, with \(W^+=0\), yields
\[
\boxed{
q=-4D_B^{-*}\delta
  -\left(1+\frac12c(F_B^-)\right)t .
}
\]
Equivalently,
\[
q=-4D_B^{-*}\delta+(\Gamma-\mathcal R-1)t.
\]
Equation (1.3) in the note omits \(-\mathcal R\) from the notation. It is correct only if the symbol \(\Gamma\) is silently redefined there to mean \(\Gamma-\mathcal R\). This matters on Taub–NUT because the separate geometric curvature actions can be large even when their Weitzenböck combination is simple.

### Endpoint eigenspace

At the flat end, write
\[
\omega_3=e^{12}+e^{34},\qquad
\beta_0^-=e^{12}-e^{34}.
\]
The stated endpoint curvature has
\[
F_A^-=\frac{i}{3}\beta_0^-,
\qquad
F_{3A}^-=i\beta_0^-.
\]
In the standard Kähler realization \(S^-=\Lambda^{0,1}\),
\[
c\!\left(i(e^{12}-e^{34})\right)d\bar z_1=-2\,d\bar z_1.
\]
Hence, for the torsion direction used in the note,
\[
\left(1+\frac12c(F_{3A}^-)\right)t=0.
\]

By contrast, on untwisted Ricci-flat Taub–NUT,
\[
s=0,\qquad F_{3A}=0,\qquad D^-t=0,
\]
so
\[
(\nabla^*\nabla-2)t=-2t.
\]
For the physical endpoint operator, the same Dirac-kernel relation instead gives
\[
\nabla_{3A}^*\nabla_{3A}t
 =-\frac{s}{4}t-\frac12c(F_{3A}^-)t
 =t+t=2t,
\]
and therefore \((\nabla_{3A}^*\nabla_{3A}-2)t=0\).

Thus Step 46’s raw-TN value \(-2t\) comes exactly from applying the untwisted Ricci-flat rough Laplacian rather than the \(s=-4\), \(3A\)-twisted physical operator. That particular order-\(L^6\) estimate does not transfer to the physical block.

---

## 2. Exact Taub–NUT tangent calculations

### 2.1 Spinor, torsion, and \(\delta\)

On Ricci-flat Taub–NUT with a flat twisting connection, take
\[
S^+=\Lambda^{0,0}\oplus\Lambda^{0,2},
\qquad e_1=1,\quad e_2\in\Lambda^{0,2},
\]
and let \(f=x_1+ix_2\) be \(I_3\)-holomorphic. For
\[
\Phi_{\rm TN}=\sqrt{\rho_*}\,e_1+a\bar f\,e_2,
\]
one has
\[
c(d\bar f)e_2=0.
\]
Since \(\bar f\) is harmonic,
\[
D^+\Phi_{\rm TN}=0,\qquad
\nabla^*\nabla\Phi_{\rm TN}=0
\]
for the untwisted Ricci-flat connection.

Writing \(P_i=a(\partial_i\bar f)e_2\),
\[
\Phi_{\rm TN}\wedge P_i
 =\sqrt{\rho_*}\,a(\partial_i\bar f)e_1\wedge e_2.
\]
It follows that
\[
\delta
 =\sqrt{\rho_*}\,a^2
   g^{ij}(\partial_i\bar f)(\partial_j\bar f)e_2.
\]
The complex-bilinear contraction vanishes:
\[
g^{-1}(d\bar f,d\bar f)
 =|dx_1|^2-|dx_2|^2-2i\langle dx_1,dx_2\rangle=0.
\]
Hence
\[
\boxed{\delta_{\rm TN}=0.}
\]

For the cubic torsion,
\[
\begin{aligned}
t_{\Phi_{\rm TN}}
 &=\sqrt{\rho_*}a\,c(d\bar f)
   \bigl(\sqrt{\rho_*}e_1+a\bar f e_2\bigr)\\
 &=\rho_*a\,c(d\bar f)e_1\\
 &=\sqrt2\,\rho_*a\,d\bar f.
\end{aligned}
\]
Since
\[
|d\bar f|^2=\frac2V,
\]
one gets
\[
|t|^2
 =2\rho_*^2a^2\frac2V
 =\frac{128}{81V}
 =\frac{m_*}{V}.
\]
Also \(D^-d\bar f=0\), so \(D^-t=0\). These tangent identities are correct.

### 2.2 These are not one exact physical field configuration

There are three distinct objects in §2:

1. the untwisted Ricci-flat tangent spinor \(\Phi_{\rm TN}\);
2. its torsion computed with a flat determinant connection;
3. the nonflat curvature
   \[
   F_A^{\rm core}
   =i\left(\frac23\omega_3+\frac13\beta^-_{x_3/V}\right).
   \]

A parallel frame \(e_1,e_2\) for the untwisted spin connection is not parallel for a connection whose curvature is \(F_A^{\rm core}\). Consequently
\[
D_A^+\Phi_{\rm TN}=0,\qquad
\nabla_A^*\nabla_A\Phi_{\rm TN}=0
\]
do not hold exactly for that nonflat \(A\).

Moreover,
\[
|\Phi_{\rm TN}|^2=\rho_*+a^2|f|^2,
\]
and
\[
(F_A^{\rm core})^+=\frac{2i}{3}\omega_3
 =2i\sigma(\sqrt{\rho_*}e_1),
\]
whereas \(2i\sigma(\Phi_{\rm TN})\) also contains terms linear and quadratic in \(f\). Thus
\[
(F_A^{\rm core})^+\ne 2i\sigma(\Phi_{\rm TN})
\]
away from \(f=0\).

This does not invalidate the tangent expansion: after rescaling a shrinking core, the physical curvature has vanishing norm and the leading connection becomes flat. It does mean that Proposition 7 cannot be applied exactly to the displayed pair \((A^{\rm core},\Phi_{\rm TN})\). A physical TNAdS correction remains necessary.

---

## 3. Gibbons–Hawking two-forms

With
\[
d\eta=*_{3}dV,\qquad
\beta_h^\pm=\eta\wedge dh\mp V*_{3}dh,
\]
and the orientation in the note, direct orthonormal-frame calculation gives
\[
*_4\beta_h^+=\beta_h^+,\qquad
*_4\beta_h^-=-\beta_h^-.
\]
Also,
\[
d\beta_h^+=-V(\Delta h)\,\mathrm{vol}_3,
\]
while
\[
d\beta_h^-
 =\left(2\langle dV,dh\rangle+V\Delta h\right)\mathrm{vol}_3
 =V^{-1}\operatorname{div}(V^2\nabla h)\,\mathrm{vol}_3.
\]
Therefore:

- \(\beta_h^+\) is closed exactly when \(\Delta h=0\);
- \(\beta_h^-\) is closed exactly when
  \(\operatorname{div}(V^2\nabla h)=0\).

For
\[
h=\frac{x_3}{V},
\]
\[
V^2\nabla\!\left(\frac{x_3}{V}\right)
 =V\nabla x_3-x_3\nabla V,
\]
and hence
\[
\operatorname{div}\left(V^2\nabla(x_3/V)\right)
 =\partial_3V-\langle\nabla x_3,\nabla V\rangle-x_3\Delta V
 =0
\]
away from the base origin. The lift extends smoothly over the nut because the GH moment maps \(x_i\) and \(r\) are quadratic in smooth nut coordinates. Thus (2.2) is correct.

There is an artifact inconsistency: `tn_core_exact.json` records both Hodge-type booleans as `false` for every tested form. Those booleans do not verify the prose. The analytic Hodge calculation above does verify the prose; the stored type test needs componentwise simplification or correction.

### Mismatch integral

Let
\[
\Delta\beta
 =\beta^-_{x_3/V}-\beta^-_{x_3}.
\]
The symbolic expression in the JSON expands, for \(R/\ell\to\infty\), as
\[
\int_{B_R}|\Delta\beta|^2
 =\frac{64\pi^2}{3}\ell^3R
   +O\!\left(\ell^4\left[1+\log(R/\ell)\right]\right).
\]
This agrees with (2.3).

Using the endpoint eigenspace cancellation,
\[
-\left(1+\frac12c(i\beta^-_{x_3/V})\right)t
 =-\frac12c(i\Delta\beta)t.
\]
Since \(\|c(\beta)\|_{\mathrm{op}}=\sqrt2|\beta|\) on \(S^-\) and
\(|t|^2=m_*/V\le m_*\),
\[
\int\left|\frac12c(i\Delta\beta)t\right|^2
 \le \frac{m_*}{2}\int|\Delta\beta|^2
 =\frac{32\pi^2}{3}m_*\ell^3R+\cdots.
\]
At \(R=L=\ell^{1/3}\), this is \(O(L^{10})\). This computation correctly controls the algebraic determinant-curvature remainder. It says nothing by itself about \(D^{-*}\delta\).

---

## 4. The selected almost complex structure and \(N_\tau\)

Write
\[
z=\sqrt{\rho_*},\qquad w=a\bar f,\qquad
\tan s=\frac{|w|}{|z|}.
\]
The Hopf map from the normalized spinor gives, up to the phase convention for \(I_1,I_2\),
\[
J_\Phi
 =\frac{|z|^2-|w|^2}{|z|^2+|w|^2}I_3
  +\frac{2\operatorname{Re}(z\bar w)}{|z|^2+|w|^2}I_1
  +\frac{2\operatorname{Im}(z\bar w)}{|z|^2+|w|^2}I_2.
\]
Thus
\[
J_\Phi=\cos(2s)I_3+\sin(2s)K_f,
\]
where \(K_f\) is the phase-dependent combination of \(I_1,I_2\).

The note’s wording that \(K\) is one parallel complex structure is not correct globally: the phase of \(f\) varies, so \(K_f\) varies. The product \(\sin(2s)K_f\) is smooth across \(f=0\), but \(K_f\) itself is not parallel.

Pointwise, this phase variation does not alter the projector norm. If
\(\xi\in\Lambda^{0,1}_{I_3}\), then \(K_f\xi\) is orthogonal to \(\xi\) and
\[
\left|P_{J_\Phi}^{1,0}\xi\right|^2
 =\sin^2s\,|\xi|^2.
\]
Because the derivative index of \(\nabla\tau\) lies in
\(\Lambda^{0,1}_{I_3}\) for the untwisted tangent field,
\[
\boxed{
|N_\tau|^2
 =\sin^2s\,|\nabla\tau|^2
 =\frac{a^2|f|^2}{\rho_*+a^2|f|^2}\,|\nabla\tau|^2.
}
\]
Thus (3.1) is correct for the tangent model. The variation of \(K_f\) becomes important after differentiating \(N_\tau\).

The “exact” weighted integral in the table uses
\[
\kappa^2=\frac{m}{4\rho_*^3},
\]
with \(\rho_*\) frozen. The geometric quantity selected by the full spinor is instead
\[
\kappa^2
 =\frac{m}{4(\rho_*+a^2|f|^2)^3}.
\]
On \(B_L\), the relative difference is \(O(L^2)\), so the frozen computation still gives the correct leading term:
\[
\int_{B_L}\kappa^2|B|^2
 =\frac{E_{\rm core}}9+O(L^8).
\]
It is not an exact full-TN identity for the actual \(\rho\).

---

## 5. Applicability of the corpus commutator

The commutator
\[
2\kappa B
 =F^E(Z_1,Z_2)\tau
  -\nabla_{Z_1}A_2+\nabla_{Z_2}A_1+\sum_iL_iA_i
\]
requires more than \(W^+=0\).

### Curvature term

For an exact physical Seiberg–Witten field:

- Einstein geometry makes the \(\Lambda^+\to\Lambda^-\) Riemann block vanish;
- \(F_A^+=2i\sigma(\Phi)\) is of type \((1,1)\) for \(J_\Phi\);
- every ASD two-form is of type \((1,1)\) for every positively oriented orthogonal \(J\).

Then
\[
F^E(Z_1,Z_2)=0
\]
is correct.

For the displayed tangent package, however,
\[
(F_A^{\rm core})^+=\frac{2i}{3}\omega_3
\]
is aligned with \(I_3\), not with the rotating \(J_\Phi\). Its \((2,0)\) component relative to \(J_\Phi\) is nonzero away from \(f=0\), of size \(O(|f|)\). Thus the curvature term does not vanish exactly for the displayed model. Its squared contribution is plausibly \(O(L^8)\), but it must appear in the calculation.

### Structural hypotheses

The relation
\[
[Z_1,Z_2]\equiv-2\kappa\bar Z_1
\]
is a structural closure equation for the adapted frame; it is not a consequence of Einstein geometry and type \((1,1)\) curvature alone. Step 47 does not verify it directly for \(J_{\Phi_{\rm TN}}\), nor does it provide an exact physical field from which the corpus closure equations follow.

Further points are:

- \(\rho=\rho_*+a^2|f|^2\), not exactly \(\rho_*\);
- \(m=m_*/V\) varies and vanishes at the nut;
- a frame normalized using \(\tau\) is singular where \(m=0\);
- passage from the commutator to
  \[
  \|\nabla N_\tau\|_2
  \gtrsim\|\kappa B\|_2-C\|N_\tau\|_2
  \]
  requires uniform control of the frame coefficients \(L_i\), projector derivatives, and the inner surface terms around the nut.

Accordingly, (3.2) is not yet a consequence of the supplied physical block.

### Direct tangent-model replacement

The critical derivative energy can nevertheless be established directly for the explicit tangent field. From (3.1),
\[
|N_\tau|^2
 =\frac{a^2r^2\sin^2\theta}
        {\rho_*+a^2r^2\sin^2\theta}
   \frac{m_*\ell^2}{(r+\ell)^4}.
\]
Set \(r=\ell y\). On, for example,
\[
2\le y\le3,\qquad \frac\pi4\le\theta\le\frac{3\pi}4,
\]
one has, as \(\ell\to0\),
\[
|N_\tau|
 \longrightarrow
 a\sqrt{\frac{m_*}{\rho_*}}
 \frac{y\sin\theta}{(1+y)^2},
\]
while
\[
|\partial_r|N_\tau||\asymp\ell^{-1}.
\]
The volume of this core annulus is \(\asymp\ell^4\). Since
\[
|\nabla N_\tau|\ge |d|N_\tau||,
\]
there is a constant \(c_0>0\) such that
\[
\int_{\{2\ell<r<3\ell\}}|\nabla N_\tau|^2
 \ge c_0\ell^2
\]
for small \(\ell\). Thus the explicit tangent core really does carry critical \(H^1\)-current energy. This argument does not use the corpus commutator. Transferring it to physical blocks requires sufficiently strong convergence of the corrected current on the rescaled core.

---

## 6. The residual estimate and the null background jet

The determinant mismatch and the \(L^2\)-current have the announced subleading size:
\[
\|(\Gamma-\mathcal R-1)t\|_2^2=O(\ell^3L)=O(L^{10}),
\]
\[
\|N_\tau\|_2^2=O(\ell^3L)=O(L^{10}).
\]

The estimate
\[
\|D^{-*}\delta\|_2^2=O(\ell^3L)
\]
does not follow merely from
\[
V^{-1/2}-1=O(\ell/r)
\]
and a null endpoint first jet.

In the ALF region, after angular integration,
\[
d\mu(r)\asymp \ell r^2\,dr.
\]
For a generic transverse perturbation
\[
\delta=O(\ell/r),
\]
one instead gets
\[
\int|\nabla\delta|^2
 \asymp
 \int_\ell^L\frac{\ell^2}{r^4}\,\ell r^2\,dr
 \asymp\ell^2
 =L^6.
\]
The announced \(O(\ell^3L)\) size arises only after an additional null cancellation. For example, if the leading perturbation is exactly parallel to the null jet, its quadratic contribution remains zero; interaction with a smooth \(O(r)\) second jet then gives
\[
\delta=O(\ell),\qquad
\nabla\delta=O(\ell/r),
\]
and hence
\[
\int|\nabla\delta|^2=O(\ell^3L).
\]
That requires a quantitative expansion of the corrected physical field, not just the statement that its leading first jet is null.

This point is particularly important because an exact \(s=-4\) spinor has a nontrivial second jet. The scalar equation gives
\[
\nabla_A^*\nabla_A\Phi
 =(1-\rho/2)\Phi,
\]
whose right side is approximately \(\frac13\Phi_0\) at the endpoint. A physical correction of amplitude \(O(r^2)\) therefore has first-derivative correction \(O(r)\). Unless its interaction with the null jet is shown to remain tangent to the null algebraic set,
\[
\delta=O(r),\qquad D^{-*}\delta=O(1),
\]
and its squared contribution over a block of volume \(\asymp\ell^2=L^6\) is exactly of order \(L^6\).

Likewise, “TNAdS corrections are relatively \(O(L^2)\)” is sufficient for zeroth-order metric quantities but not automatically for residuals involving one or two derivatives: connection corrections are typically \(O(L)\), while curvature corrections can be \(O(1)\).

Therefore the residual conclusion needs substantially more than a null first jet:

- an exact or quantitatively accurate TNAdS Seiberg–Witten correction;
- control of its second jet relative to the calibrated background;
- control of transverse components in \(\delta\);
- the same spin and determinant connection in the torsion, Dirac, and curvature computations.

None of these is supplied by the exact tangent scripts.

---

## 7. The reduction using \(\|\nabla N_\tau\|_{2,\mathrm{av}}\to0\)

If a sequence is already known to decompose into a positive density of cores converging strongly to the displayed TN tangent, the direct annular estimate above gives
\[
\int_{\text{each core}}|\nabla N_\tau|^2\ge c_0\ell^2.
\]
Since the number of cores is proportional to \(V/\ell^2\), their normalized total remains bounded below by a positive multiple of the core fraction. Under that decomposition, normalized \(H^1\)-convergence \(N_\tau\to0\) excludes such a TN phase.

That implication does not by itself establish density-free O10, or even cover every geometry informally described as “nut-type.” It also requires:

1. a bubble decomposition identifying all relevant concentration pieces with TN cores;
2. strong enough convergence to transfer the annular \(H^1\) lower estimate;
3. control of the commutator product terms if the corpus route is used;
4. verification that subsequent finite-density arguments do not invoke \(W^-\)-dependent estimates elsewhere.

Thus §4.4 is a useful conditional exclusion mechanism for a specified TN bubble phase, not yet a reduction of the full density-free theorem.

---

## Final mathematical status

1. **Correct:** identity (1.1), after fixing the \(\Gamma-\mathcal R\) notation.

2. **Correct:** the endpoint Clifford eigenvalue cancels the algebraic
   \(1+\frac12c(F_{3A}^-)\) term. The Step-46 estimate based on raw
   \(q_{\rm TN}=-2v\) is not a physical local obstruction.

3. **Correct as untwisted tangent geometry:**  
   \(\delta_{\rm TN}=0\),  
   \(t_{\Phi_{\rm TN}}=\sqrt2\rho_*a\,d\bar f\),  
   \(|t|^2=m_*/V\),  
   \(D^-t=0\),  
   the GH closedness formulas, \(h=x_3/V\), and the mismatch asymptotic.

4. **Needs correction in presentation:** the stored Hodge-type booleans contradict the analytic form types; \(K_f\) is phase-dependent rather than one parallel complex structure; the frozen-\(\rho_*\) \(\kappa\)-integral is leading-order rather than the exact geometric quantity.

5. **Not established:** the application of the corpus commutator to the displayed core and the lower estimate (3.2) on an exact physical block. A direct tangent-model \(H^1\) lower estimate is available instead.

6. **Central unresolved term:** \(D^{-*}\delta\). The determinant mismatch is \(O(L^{10})\), but a physical transverse second-jet correction can produce an \(O(L^6)\) contribution. A null first jet alone does not remove it.

The strongest result supported by the supplied material is therefore:

\[
\boxed{\text{The specific raw-TN }-2t\text{ payment from Step 46 disappears in the physical Weitzenböck formula.}}
\]

The broader statement that a corrected TNAdS core has no local order-\(L^6\) residual remains unresolved until the physical field extension and the \(D^{-*}\delta\) estimate are constructed.
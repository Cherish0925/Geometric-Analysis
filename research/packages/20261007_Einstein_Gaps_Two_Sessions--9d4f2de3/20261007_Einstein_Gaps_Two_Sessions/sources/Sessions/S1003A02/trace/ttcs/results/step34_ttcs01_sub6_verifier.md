# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Sessions/S1003A02/workspace/notes/step31_charge_variation_constraint_pinning_nonround_opening.md",
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md",
    "Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md"
  ]
}
```

## Task

Derive and critically assess the proposed symmetry-free two-part link calculus. Starting from a hypersurface foliation of a scalar-normalized four-manifold, write the Gauss and Codazzi constraints in conventions compatible with Ric°(nu,nu), Ric°(nu,.) and the second fundamental form; explain exactly which squared constraint components are controlled by integral |Ric°|^2 and how the diagonal Lemmas N, P and beta-pinning instantiate them. Compare this kinematic/constraint channel with Theorem G's characteristic boundary channel. Give a precise theorem-level general principle without claiming compactness or link regularity from L2 control alone. Note sign/convention dependencies that must be stated.

## Output

# Symmetry-free two-part link calculus: leafwise derivation and comparison with Theorem G

## 0. Main findings

1. **Five of the nine components of Ric° are not constraints.** In any unit-lapse foliation by closed leaves, the trace-free Ricci tensor splits orthogonally and pointwise as
   \[
   |\operatorname{Ric}^\circ|^2=\tfrac43\,\mathcal C^2+2|\mathcal J|^2+|\mathcal T|^2 .
   \]
   - \(\mathcal C=\operatorname{Ric}^\circ(\nu,\nu)\) is the traced Gauss equation (1 component).
   - \(\mathcal J=\operatorname{Ric}^\circ(\nu,\cdot)|_{T\Sigma}\) is the traced Codazzi equation (3 components).
   - \(\mathcal T\) is the trace-free leaf part of Ric° (5 components). It cannot be read from the first jet \((h,k)\) of one leaf. It enters only through \(\partial_t k\), so it acts as the control of the leafwise evolution.

   Diagonal Bianchi-IX sees only \(\mathcal C\) (Lemma N) and two components of \(\mathcal T\) (the \(E,D\) channels). \(\mathcal J\equiv0\) there.

2. **Theorem G is an exact completion of the square in the control \(\mathcal T\).** With the Λ²-endomorphism norm on Weyl (the norm used in the notes),
   \[
   \frac{d\mathcal Q_\pm}{dt}=\frac1{8\pi^2}\int_{\Sigma_t}\Big[\tfrac43\mathcal C^2+2|\mathcal J|^2+|\mathcal T|^2-|\mathcal T-Z_\pm|^2-\tfrac{s^2}{12}\Big]dA,
   \qquad Z_\pm=2(G^\circ\mp B).
   \]
   - \(G^\circ\) is first-jet Gauss data and \(B\) is the magnetic Weyl part, i.e. first-jet Codazzi data.
   - The volume-renormalized charges \(\mathfrak B_\pm\) are therefore *exact* solutions of the leafwise Hamilton–Jacobi inequality of the cell control problem.
   - The pinning lemmas (β, P, D-Green) are Cauchy–Schwarz calibrations centred at the Einstein control \(\mathcal T=0\).

3. **The general principle is a calibration theorem.** A lower bound on an annulus is \(V(b)-V(a)\) for any first-jet functional \(V\) satisfying a pointwise HJ inequality on the states the metric visits. Two corollaries follow:
   - Lemma V holds without symmetry.
   - A bound beyond the charges needs a functional \(\phi\) that decreases along the \(W^+\)-flat reference evolution \(\mathcal T=Z_+\), with quadratic slack. This sharpens Step 33's remark "\(\nabla\phi\cdot f\le\omega_+\)".

   Nothing here gives compactness or link regularity.

4. **Checks performed.** Chern's transgression is \(\mathcal E=-\frac1{4\pi^2}\int_\Sigma(\sigma_3(k)+\langle G^\Sigma,k\rangle)\). I checked it on three geometries:
   - flat hypersurfaces (Gauss–Kronecker);
   - hyperbolic geodesic spheres;
   - CH Berger spheres, where it gives \(\mathcal E=1-3\sinh^4\tau\). This agrees with Step 33, item 5, through Gauss–Bonnet with \(e=6/\pi^2\), which in turn gives \(\mathcal H=\sinh^4\tau\) and the stated \((\mathcal Q_+,\mathcal Q_-)\).

   On CH spheres \(G^\circ=\operatorname{diag}(2,-1,-1)\), and \(W^-=0\) forces \(|W^+|^2=|2G^\circ|^2=24=s^2/24\). This is consistent.

---

## 1. Leaf decomposition of the curvature

**Setting.**
- \(t\) has \(|\nabla t|=1\) on an annulus \(C\cong[a,b]\times\Sigma\), with leaves \(\Sigma_t\) closed and embedded.
- \(\nu=\nabla t\) points from the inner link to the outer link.
- \(k(X,Y)=g(\nabla_X\nu,Y)\), \(H=\operatorname{tr}_hk\) (this is \(S\) of Lemma N), \(\pi=k-Hh\), \(\partial_th=2k\), and \(d\mu=dA\,dt\).
- \(R_{abba}\) is sectional curvature and \(\operatorname{Ric}_{bc}=\sum_aR_{abca}\), so spheres are positive.

**Counting.** The 20 curvature components split by the number of normal slots:
- \(R_{ijkl}\) (6 components) is first-jet data through Gauss.
- \(R_{ijk\nu}\) (8 components) is first-jet data through Codazzi.
- \(R_{i\nu\nu j}\) (6 components) involves \(\partial_tk\) through the Riccati equation.

In terms of irreducible pieces, \(W=(E,B)\) contributes 5+5, Ric° contributes 9, and \(s\) contributes 1, with \(E_{ij}=W_{i\nu\nu j}\).

**Gauss, traced.** \(R^\Sigma=s-2\operatorname{Ric}(\nu,\nu)+H^2-|k|^2\). Hence
\[
\mathcal C:=\operatorname{Ric}^\circ(\nu,\nu)=\sigma_2(k)-\tfrac12R^\Sigma+\tfrac s4=G(\nu,\nu)+\tfrac s4. \tag{1.1}
\]

**Gauss, trace-free in \(T\Sigma\).** Use \(\sum_lR_{illj}=\operatorname{Ric}_{ij}-R_{i\nu\nu j}\) together with
\[
R_{i\nu\nu j}=E_{ij}+\tfrac12(\operatorname{Ric}_{ij}+\operatorname{Ric}_{\nu\nu}\delta_{ij})-\tfrac s6\delta_{ij}.
\]
This gives
\[
\tfrac12\mathcal T-E=G^\circ:=(\operatorname{Ric}^\Sigma-Hk+k\circ k)^{\rm tf}. \tag{1.2}
\]

**Codazzi.** \(R(X,Y,Z,\nu)=(\nabla_Xk)(Y,Z)-(\nabla_Yk)(X,Z)\). Its trace is
\[
\mathcal J:=\operatorname{Ric}(\nu,\cdot)|_{T\Sigma}=\operatorname{div}_\Sigma k-dH=\operatorname{div}_\Sigma\pi. \tag{1.3}
\]
Its trace-free part is the magnetic Weyl \(B\), with \(W_{ijk\nu}=\varepsilon_{ijl}B_{lk}\) up to a convention sign. In three dimensions a Codazzi-type tensor has \(8=3+5\) components, matching \((\mathcal J,B)\).

**Riccati.** For the shape operator, \(\partial_tk=-k\circ k-R_\nu\), with \((R_\nu)_{ij}=R_{i\nu\nu j}\). By (1.2) the trace-free part of \(R_\nu\) equals \(E+\frac12\mathcal T=\mathcal T-G^\circ\). Hence
\[
(\partial_tk)^{\rm tf}=-(k\circ k)^{\rm tf}+G^\circ-\mathcal T,\qquad
\partial_tH=-H^2+R^\Sigma+\mathcal C-\tfrac34s. \tag{1.4}
\]
For \(s=-24\) the trace equation is Lemma N(4). The diagonal reduction is \(k=\operatorname{diag}(y_i)\). It reproduces \(y_i'=6-y_iS+P_i-e_i\), since \(-(k^2)+G^\circ\) has trace-free part \((P_i-Sy_i)^{\rm tf}\).

**Transport.** If \(ds=0\), then \(\operatorname{div}\operatorname{Ric}^\circ=0\), and its \(\nu\)-component gives
\[
\partial_t\mathcal C=-\tfrac43H\mathcal C+\langle k^\circ,\mathcal T\rangle-\operatorname{div}_\Sigma\mathcal J. \tag{1.5}
\]
In the diagonal case \(\mathcal J=0\), and (1.5) is exactly Lemma N(2): \(-2S\mathcal C-\sum(S-y_i)e_i=-S\mathcal C+\sum y_ie_i\). The tangential component of \(\operatorname{div}\operatorname{Ric}^\circ=0\) gives the analogous transport of \(\mathcal J\); I have not written it out.

**Norm.** Write \(\operatorname{Ric}^\circ|_{T\Sigma}=\mathcal T-\frac{\mathcal C}3h\). Then
\[
|\operatorname{Ric}^\circ|^2=\tfrac43\mathcal C^2+2|\mathcal J|^2+|\mathcal T|^2 . \tag{1.6}
\]
In the diagonal case \(|\mathcal T|^2=\frac23E^2+\frac12D^2\), and \(\mathcal C=-\frac34H_{31}\), where \(H_{31}\) is the Step 31 Ricci channel, not the mean curvature. This reproduces \(\frac34H_{31}^2+\frac23E^2+\frac12D^2\). With orbit volume \(2\pi^2W\), it also reproduces \(\widehat P=\int W(\mathcal C^2/3+E^2/6+D^2/8)\,dt\).

## 2. What \(\int|\operatorname{Ric}^\circ|^2\) controls

From (1.6),
\[
\int_C\big(\tfrac43\mathcal C^2+2|\mathcal J|^2\big)d\mu\le 8\pi^2\widehat P(C),
\]
with equality iff \(\mathcal T\equiv0\).

- **Hamiltonian residual \(\mathcal C\).** It is a pointwise function of the leaf state \((h,k)\) only when \(s\) is fixed. Without normalization \(\mathcal C=G(\nu,\nu)+s/4\), and \(s\) is not priced by \(P\). This is why the scalar-\(-24\) reduction is structural rather than cosmetic. Its own costs, from Step 31, are that it moves CH collars (rate \(m\)) and the bolt scale (\(u(0)b\)).
- **Momentum residual \(\mathcal J\).** It needs no normalization. It is also blind to the leaf geometry modulo diffeomorphisms: \(\int_\Sigma\langle\mathcal J,X\rangle=-\frac12\int\langle\pi,\mathcal L_Xh\rangle\), so it controls only the Lie-derivative (gauge) projection of \(\pi\).
- **What is not controlled pointwise or in \(L^2\):**
  - \(\sigma_2(k)\) and \(R^\Sigma\) separately (only their combination enters \(\mathcal C\));
  - \(|k|\), \(H\), \(\sigma_3(k)\), \(B\), \(E\).
  - \(\mathcal T\) appears in Gauss only in the Weyl-entangled combination \(\frac12\mathcal T-E\) of (1.2). Separating it from \(E\) requires \(\partial_tk\). This is the exact reason the \(E,D\) channels are first-order (kinematic) and not pointwise penalties.
- **Why diagonal Bianchi IX has no momentum channel.** For class-A Bianchi data the momentum constraint reduces to the commutator of \(k\) with the structure matrix, which vanishes when both are diagonal. So \(\mathcal J\equiv0\) in Steps 25–33. Non-diagonal Bianchi IX (rotating frames) is the first symmetric setting where \(\mathcal J\neq0\) and the three off-diagonal components of \(\mathcal T\) appear.

## 3. How the diagonal lemmas instantiate the calculus

**Lemma N** combines (1.1), (1.4) and (1.5) with \(\mathcal J=0\), together with the pointwise penalty \(\int W\mathcal C^2/3\).

**Lemma W, symmetry-free form.** The Riccati trace (1.4) holds pointwise along each normal geodesic \(\gamma_x\), \(x\in\Sigma_a\), with area Jacobian \(J\) satisfying \(\partial_tJ=HJ\).
- Put \(q_x=\int_a^bJ\mathcal C^2dt\). Then \(\int_{\Sigma_a}q_x\,dA=\int_C\mathcal C^2d\mu\le6\pi^2\widehat P\).
- The last-crossing proof of Step 31 then holds verbatim along \(\gamma_x\) under these hypotheses:
  - \(R^\Sigma\ge-\rho_0\) pointwise along \(\gamma_x\);
  - \(A^2=18-\rho_0>0\) and \(m=\min(H(a,x),A)\);
  - \(m-(q_x/(\sigma_0J(a,x)))^{1/2}>\sigma_0\).
- Conclusion: \(H>\sigma_0\), \(J\ge J(a,x)e^{\sigma_0(t-a)}\), and \(\int dt/J\le1/(\sigma_0J(a,x))\).
- By Chebyshev, the hypothesis on \(q_x\) holds outside a set of initial points of \(dA_a\)-measure at most \(6\pi^2\widehat P/\lambda\).
- In the diagonal case \(J\propto W\) and \(\int W\mathcal C^2\le3\widehat P\), which is Step 31's constant.
- What this does not give: absence of focal points and the pointwise bound on \(R^\Sigma\) remain hypotheses.

**Kinematic pinning.** For a first-jet functional \(\Phi(t;h,k)\), (1.4) gives
\[
\Phi'=\mathbb A_\Phi-\int_{\Sigma_t}\langle\psi_\Phi,\mathcal T\rangle dA.
\]
Here \(\mathbb A_\Phi\) is \(\Phi'\) evaluated at \(\mathcal T=0\) (the Einstein drift \(F\), with \(\mathcal C\) the actual state function), and \(\psi_\Phi=D_k\Phi\) as a leaf density. Therefore
\[
\Big|\Delta\Phi-\int\mathbb A_\Phi\Big|\le\big(8\pi^2\widehat P\big)^{1/2}\|\psi_\Phi\|_{L^2(C)}.
\]

**β-pinning (Step 30, eq. 10).** Here \(\Phi=\widetilde B\) and \(\widetilde B'=F_\beta-\frac14E\). Since \(v\) is a trace-free combination, \(\mathcal C\) cancels. With \(E=\frac{\sqrt6}2\langle\mathcal T,u_E\rangle\) and \(u_E=\operatorname{diag}(2,-1,-1)/\sqrt6\), the constant is \((\sqrt6/8)\cdot2=\sqrt{3/8}\). This matches (10).

**Lemma P** (statement not in the supplied files) is, per the Step 30 remark, the same construction coupled to \(D\), with the \(D\)-normalization of the control factor.

**D-Green identity.** It is the same pinning applied to the *time-dependent* observable \(\Phi=q+KJ\), with \(J=Wq'\) and \(K'=-1/W\). Then \(\Phi'=KW(\Pi-D)\): \(K\) is chosen as the costate that cancels the free momentum \(J\) from the drift. The constant \(8\) follows from \(\int WD^2\le8\widehat P\).

So all three pinnings are linearized HJ (Pontryagin) calibrations centred at \(\mathcal T=0\).

## 4. The characteristic channel in leaf variables

**Euler transgression.** It uses only tangential–tangential ambient curvature, which Gauss expresses intrinsically. It is therefore a combination \(\alpha\sigma_3(k)+\beta\langle G^\Sigma,k\rangle\). Fixing \(\alpha,\beta\) by flat space (where \(\langle G^\Sigma,k\rangle=-3\sigma_3\)) and by hyperbolic spheres (where \(\mathcal E=-\frac12\cosh^3r+\frac32\cosh r\)) gives
\[
\mathcal E(\Sigma)=-\frac1{4\pi^2}\int_\Sigma\big(\sigma_3(k)+\langle G^\Sigma,k\rangle\big)dA .
\]

**Independent check on a CH sphere.** Take \(a_f=\sinh\tau\cosh\tau\), \(a_g=a_h=\sinh\tau\), with \(y_f=\coth\tau+\tanh\tau\) and \(y_g=y_h=\coth\tau\). The Berger Einstein tensor is \(G_{ff}=(3c^2-4)/s^2\), \(G_{gg}=-c^2/s^2\), where \(c=\cosh\tau\), \(s=\sinh\tau\). The formula gives \(c^4-2s^2c^2-2s^4=1-3s^4\).

**Signature transgression.** \(\mathcal H=\eta+\int T_{p_1}\). Schematically, \(T_{p_1}\) is built from \(k\), the intrinsic connection and the mixed curvature \(R_{ijk\nu}\), i.e. the Codazzi data \(\mathcal J\oplus B\). The diagonal collar term \(\lambda^2(U-V)^2\) is the symmetric shadow of this. I have not fixed its constants.

**η along the foliation.** \(\eta(h_t)\) is \(C^1\) in \(t\): the kernel of the odd signature operator is the space of harmonic forms, whose dimension is topological, so there is no spectral flow.

**Derivative identity.** Apply APS to \(\Omega_t\). Then use \(|W^\pm|^2_{\Lambda^2}=|E\pm B|^2\) (valid in the Λ²-norm only) and \(E=\frac12\mathcal T-G^\circ\). This yields the identity of §0, equivalently \(\widehat P'=\mathcal Q_\pm'+\omega_\pm\) with
\[
\omega_\pm=\frac1{8\pi^2}\int_{\Sigma_t}\big(|\mathcal T-Z_\pm|^2+\tfrac{s^2}{12}\big)dA\ \ge 0 .
\]

**Consistency checks.**
- The \(|\mathcal T|^2\) terms cancel, so \(\mathcal Q_\pm'\) is linear in \(\mathcal T\). This is required, since the Pfaffian and \(\operatorname{tr}R\wedge R\) contain the normal–normal curvature linearly. The cancellation happens only in the Λ²-normalization, which independently confirms the norms used in Theorem G.
- On CH, \(Z_-=0\) and \(|Z_+|^2=96\).
- The constraint residuals enter \(\mathcal Q_\pm'\) with coefficient \(+\), in both chiralities.

**Consequences.**
- *Symmetry-free Lemma V.* For any unit-lapse foliation of \(C\) by links of fixed topology,
  \[
  \widehat P(C)\ge\int_a^b\max\{0,\mathcal Q_+',\mathcal Q_-'\}\,dt .
  \]
  The endpoint difference \(\Delta\mathcal Q_\pm\) depends only on the two link germs. The pathwise integral depends on the foliation, and one may take the supremum over admissible foliations.
- *Volume-renormalized charges solve HJ exactly.* With \(s\equiv s_0\), put \(\mathfrak B_\pm=\mathcal Q_\pm+\frac{s_0^2}{96\pi^2}\operatorname{Vol}(\Omega_t)\), which is \(\mathcal Q_\pm+3\widehat V\) when \(s_0=-24\). The term \(-s^2/12\) is then absorbed, and \(\widehat P'=\mathfrak B_\pm'+\frac1{8\pi^2}\int|\mathcal T-Z_\pm|^2\).

## 5. The two channels compared

| | Characteristic (Theorem G) | Constraint / kinematic |
|---|---|---|
| Observable | \(\mathcal Q_\pm\), \(\mathfrak B_\pm\): fixed universal first-jet functionals, with η nonlocal in \(h\) | arbitrary \(\Phi(t;h,k)\) |
| Reference control | \(\mathcal T=Z_\pm\) (leafwise \(W^\pm=0\)) | \(\mathcal T=0\) (Einstein evolution) |
| Loss | none (exact square) | Cauchy–Schwarz weight \(\|\psi_\Phi\|^2\sim\int dt/W\) |
| Drift | none | \(\mathbb A_\Phi\) must be bounded on visited states |
| Anchoring | topology \((\chi,\tau)\) at the ends | endpoint first jets |
| Foliation dependence | endpoints: none; pathwise integral: yes | yes |
| Strength | small scales, topology changes | large orbit volume (where the \(D\)-cost 4.30 of 6.48 sits) |
| Insensitive to | everything inside \(\omega_\pm\) | Weyl content; topology |

On one interval the two bounds do not add. Admissible combinations are:
- convex combinations \(\theta\mathfrak B_++(1-\theta)\mathfrak B_-\) (Euler and signature mixtures, with \(\omega\ge0\));
- the trivial calibration \(V=0\);
- sums over disjoint intervals;
- sums of pinnings in orthogonal channels \((\mathcal C,\mathcal J,\mathcal T\)-components) on the same interval.

## 6. Theorem-level statement

**Theorem (two-channel link calculus).** Assume:
- \((M,g)\) is smooth and oriented, with the blow-up orientation;
- \(C\cong[a,b]\times\Sigma\) is the diffeomorphic image of a normal-exponential map, so all leaves are closed, embedded, of fixed topology and focal-free;
- \(s\equiv s_0\) on \(C\);
- \(\mathcal C,\mathcal J,\mathcal T,G^\circ,B,Z_\pm\) are as above.

Then:

1. Identities (1.1)–(1.6) hold pointwise. Every \(\mathcal T\)-dependence of the evolution of \((h,k)\) is through \((\partial_tk)^{\rm tf}\).
2. \(\widehat P'=\mathfrak B_\pm'+\frac1{8\pi^2}\int_{\Sigma_t}|\mathcal T-Z_\pm|^2\,dA\). Hence \(\widehat P(C)\ge\int\max\{0,\mathcal Q_+',\mathcal Q_-'\}\) and \(\widehat P(C)\ge\Delta\mathfrak B_\pm\).
3. **Calibration.** Let \(V(t;h,k)\) be \(C^1\) with \(V'=\mathbb A_V-\int\langle\psi_V,\mathcal T\rangle\). Suppose that on the set of leaf states actually visited by \(g\),
   \[
   \mathbb A_V+2\pi^2\!\int_{\Sigma_t}|\psi_V|^2dA\le\frac1{8\pi^2}\int_{\Sigma_t}\big(\tfrac43\mathcal C^2+2|\mathcal J|^2\big)dA .
   \]
   Then \(\widehat P(C)\ge V(b)-V(a)\). The proof minimizes \(|\mathcal T|^2/8\pi^2+\langle\psi_V,\mathcal T\rangle\) pointwise; the minimum is \(-2\pi^2|\psi_V|^2\). \(\mathfrak B_\pm\) satisfy this with equality.
4. **Relative form.** \(V=\mathfrak B_++\phi\) is admissible iff
   \[
   \phi'\big|_{\mathcal T=Z_+}+2\pi^2\int|\psi_\phi|^2\le0
   \]
   on visited states. In that case \(\widehat P(C)\ge\Delta\mathfrak B_++\Delta\phi\).
5. **Constraint penalty and expansion.** \(\int_C(\frac43\mathcal C^2+2|\mathcal J|^2)\le8\pi^2\widehat P(C)\), and the geodesicwise Lemma W of §3 holds.
6. **Fubini.** \(|\{t:\int_{\Sigma_t}|\operatorname{Ric}^\circ|^2dA>\lambda\}|\le8\pi^2\widehat P/\lambda\).

**What is not part of the theorem.** Item 6 controls only \((\mathcal C,\mathcal J,\mathcal T)\) in \(L^2\) on good leaves. It does not control:
- the leaf geometry \((h,k)\), \(R^\Sigma\) or \(B\);
- \(\sigma_3(k)\), \(\langle G^\Sigma,k\rangle\) or \(T_{p_1}\), hence not the convergence of \(\mathcal E\) or \(\mathcal H\);
- the Dai adiabatic η correction along collapsing links;
- the visited state set in items 3–4;
- the existence of focal-free foliations.

These are exactly Step 33's link-regularity inputs (a)–(c), plus a state-space enclosure for the HJ test.

**Non-unit lapse.** With \(g=N^2dt^2+h\):
- (1.1)–(1.3) are unchanged, since they are leafwise;
- (1.4) gains \(-N^{-1}\operatorname{Hess}N\) and \(-N^{-1}\Delta N\) terms;
- \(d\mu=N\,dA\,dt\);
- item 2 holds with \(N\) inside the leaf integrals.

The lapse is therefore a gauge freedom available to item 3.

## 7. Sign and convention dependencies to state

1. The sign of \(k\) (\(+\nabla\nu\)) and the direction of \(\nu\) (inner → outer).
   - \(\sigma_3\), \(\langle G^\Sigma,k\rangle\), \(\mathcal E\) and \(H\) are odd under reversing \(\nu\).
   - \(\mathcal C\) is even.
   - (1.3) is covariant.
   - Each link is oriented as \(\partial\) of the region it encloses, and the inner link enters with reversed sign.
2. The curvature sign convention (\(R_{abba}\) sectional) and the Ricci contraction. The signs in (1.2), (1.4) and (1.5) depend on these.
3. The Weyl norm. Use the Λ²-endomorphism norm, \(|W^\pm|^2=|E\pm B|^2\). With the tensor norm the factor is 4 and the cancellation in §4 does not occur.
4. The definition of \(B\) and the sign in \(W^\pm\leftrightarrow E\pm B\). These depend on the Hodge star on \(\Sigma\), induced by \(\nu\wedge\mathrm{vol}_\Sigma=\mathrm{vol}_M\), and on the blow-up orientation. They decide which of \(Z_\pm\) vanishes on CH. Only \(B=\pm G^\circ\) is fixed by \(W^-=0\); I did not compute the sign of \(B\).
5. The η and odd-signature-operator convention, and the lift anchor (\(\eta(1)=0\) for Berger spheres). Step 33 notes that \(\mathcal H\) (Hopf-adiabatic) \(\to2/3\).
6. Scalar normalization \(s=-24\) (so Ric \(=-6g\)) and the diagonal volume \(\int\sigma_1\sigma_2\sigma_3=2\pi^2\), which is the source of the factor \(\tfrac14\) in \(\widehat P=\int W|\operatorname{Ric}^\circ|^2/4\).
7. Name collision: Step 31's \(H\) is the Ricci channel \(-\frac43\mathcal C\), not the mean curvature.

## 8. Unresolved and checkable items

- **Diagonal test of the derivative identity.** The identity \(8\pi^2\mathfrak b_\pm'=W\cdot2\pi^2[\dots]\) of §4 can be tested exactly in diagonal Bianchi IX, where \(G^\circ\) and \(B\) are explicit in \((a_i,y_i)\). It should reproduce \(\mathfrak b_\pm=\mathcal Q_\pm\) and fix the sign of \(B\).
- **Constants of \(T_{p_1}\).** Its explicit constants, and its continuity under first-jet convergence, are not derived here.
- **The relative HJ test for non-round opening.** The open object is a functional \(\phi\) on non-round Berger/triaxial leaf states that decreases along the \(W^+\)-flat reference evolution \(\mathcal T=Z_+\), with \(\|\psi_\phi\|^2\) affordable at the orbit volume where the triaxial swap of Lemma Z(iii) occurs. That is the precise symmetry-free form of input (N).
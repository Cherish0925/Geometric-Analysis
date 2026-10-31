# Step 90 route map: forced twist remains open, with a concrete radial mechanism

## Established this Step

1. For fixed charge and area, the twist energy
   \(Q=\frac12e^{-3\sigma}q^TM^{-1}q\) is a horospherical potential on
   \(\mathbb H^2\):
   \(\operatorname{Hess}Q=Qh\), \(|\nabla Q|=Q\), and the orbit-map source is
   \(S_F=-\nabla Q\).
2. The structured derivative is
   \(\langle dU,DS_F\rangle=-Qe+3X+R_q\), with
   \(|R_q|\le\sqrt{2Qe}|b|\). The base drift \(+Qe\) cancels the target
   \(-Qe\) exactly.
3. Maxwell normalization is
   \(dq=\pm2\rho *E_{mix}\), so \(|b|^2=4|E_{mix}|_{HS}^2\) and
   \(|b|\le2\sqrt2\delta\).
4. For variable \(Q\), curvature uses \(Q_-\), forcing uses \(Q_+\), and the
   separator floor uses \(Q_C\). Step 89's one-parameter curve does not apply.
5. The canonical derivative-free combined energy is
   \(W=e+2Q+3|\nabla\sigma|^2\). Its exchanges cancel, but its large-\(Q\)
   reaction is not coercive.
6. A smooth exact constant-charge radial core was numerically continued for
   \(Q_0\le100\); it rapidly redshifts \(Q\) and approaches an expanding
   near-cusp state. The unused horizontal constraint propagates exactly as
   \(C'=-2(u+H)C\). After switching at \(w=\delta\), a fixed-length collar
   discharges to \(q=0\) with \(\max|b|=C(L)\delta\), while
   \(C'=-2(u+H)C-wb\) makes the remaining horizontal defect \(O(\delta^2)\).
   In this rank-one model \(\|E\|_{op}=\max\{|C|,|b|/2\}<0.925\delta\) for all
   sampled collars. This refutes any local propagation premise that one exact OT
   end plus small mixed Ricci forces small interior \(Q\).

Canonical note:
`workspace/notes/step90_structured_forced_twist_and_radial_escape.md`.

## What the computation does not establish

The radial core has a polar base center, although the fibre \(T^2\) action remains
free; its quotient is a disk, not the cylindrical two-ended base of the Step 88
separator theorem. The taper is a reduced-model shot rather than an all-jet exact
splice, and its endpoint retains \(C=O(\delta^2)\). Since
\(C(L)=-e^{-2I(L)}\int e^{2I}wb\), a monotone discharge has \(C(L)>0\);
exact attachment needs sign-changing control or an extra horizontal source. A two-mode pilot achieved \(w=C=0\) only at \(\max|b|\approx26\delta\) for one test, so algebraic control exists but small-defect feasibility remains unresolved. No counterexample metric on a closed no-Einstein manifold has been constructed.

## Strong next work

### Free cylindrical charged throat

Build or obstruct a high-\(Q\) throat on a base cylinder with two outward ends.
The relevant unknown is global matching, not local charge damping. A useful BVP
should evolve \((\sigma,\alpha,H,w,C)\) with free middle data and flat-endpoint,
sign-changing controls satisfying both \(w=0\) and \(C=0\) at attachment. The
one tested basis was far too costly, so optimize the control shape or allow a
small horizontal source while tracking the true operator norm, then test whether
the auxiliary metric
\(e^{2\sigma}\gamma_B\) has the required minimal separator. Use the exact toral black-hole/Einstein Dehn-filling cap
\(ds^2/(s^2-a/s)+(s^2-a/s)d\theta^2+s^2g_{\mathbb R^2}\) as a benchmark for the
polar redshift geometry and all-jet cusp matching \cite{li2026poincar}; it caps one
cusp and is not itself the needed two-ended graph connector. If a two-ended
solution exists, it escapes the current OT resolvent mechanism inside the
free-\(T^2\) class; if not, the failed constraint identifies the missing global
identity.

### Analytic alternative

Seek a two-end identity controlling the redshift integral or the separator's
placement, not a pointwise \(Q_+\) bound. The radial core shows that any purely
local estimate from \(|dq|_{phys}=O(\delta)\), the area equation, and one exact
OT end is false in the reduced system.

### Other active routes

The diffuse non-OT \(S^3\)-neck route remains outside all torus arguments. The
positive branch is independently at a corrected determinantal response problem:
per A02 messages #658–#661, the missing object is the tensor-sector \(Q\)-channel
for diagonal and sigma-matched adjacent pairs; older scalar mixed-chirality
obstruction interpretations are superseded. None of these results resolves Yau
26 or starts the required Lean proof.

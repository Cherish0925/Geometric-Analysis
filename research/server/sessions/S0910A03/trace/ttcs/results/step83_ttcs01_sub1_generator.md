# TTCS Independent Branch Record

```json
{
  "step_id": 83,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step81_collapse_and_contraction.md"
  ]
}
```

## Task

Given the K-production framework for the OT graph-manifold connector, where K'=-2⟨τ,b⟩+2⟨vc⟩+Cov(v-u,k)-2xK with K(0)=12, K''(0)≥72, and a successful connector requires K≤6+2δ: investigate whether any known monotone or convex functional excludes the K-drop in the full coupled (γ_B, σ, M) OT system. Consider: (a) The total orbit energy E=∫ρ e_{H²} dz — does the full area/base evolution preserve E monotonicity? (b) The orbit-volume-weighted squared distance F=∫ρ d²_{H²}(U,P) dz for an appropriate reference P — does the coupled base response preserve its monotonicity? (c) The matrix Noether current Q=∫ρ M⁻¹M_r dz — can its vanishing be used in combination with other quantities? (d) Is there an energy/entropy functional combining K, x, y, ⟨|b|²⟩, ⟨h²⟩ that is monotone along the coupled Einstein evolution? Look for a differential inequality of the form d/dr(F)≥c·F or a Lyapunov argument. If no monotone quantity exists, identify which coupled mechanism breaks each candidate's monotonicity and what the resulting freedom is.

## Output

The natural OT identities do **not** presently give a radial Lyapunov functional that forces \(K\) to stay above \(6\). The only robust convex identity is the two-dimensional weighted harmonic-map divergence identity; it excludes an exact finite connector whose outer slice has constant orbit map, but it is not a monotone-in-\(r\) statement for \(K\), for the orbit energy, or for the orbit-distance variance. The coupled variables \(u,v,h,b\) introduce sign-changing exchange terms that are invisible in the VII\(_0\) reduction.

I write the source-free OT equations in physical gauge; a small Ricci defect adds forcing terms with arbitrary sign to the displayed formulas. Let
\[
e=|U_s|^2,\qquad b=U_r,\qquad 
\tau=D_sU_s+hU_s,\qquad H=u+v,\qquad d\mu=\rho\,ds,
\]
and use normalized averages \(\langle f\rangle=V^{-1}\int f\,d\mu\). The orbit equation is
\[
D_rb+Hb+\tau=0,
\]
and Codazzi gives
\[
D_sv=h\Bigl(u-\frac v2\Bigr)-\frac12\langle U_s,b\rangle_{\mathbb H^2}.
\]

### (a) Total orbit energy is not radially monotone in the coupled system

For the slice orbit energy
\[
\mathcal E_s=\int e\,d\mu,
\]
a direct kinematic calculation gives
\[
\boxed{\mathcal E_s'
=-2\int\langle\tau,b\rangle\,d\mu+\int (v-u)e\,d\mu.}
\]
Using the orbit equation, with
\[
\mathcal B=\int |b|^2\,d\mu,
\]
this can also be written
\[
\boxed{\mathcal E_s'
=\mathcal B'
+\int H|b|^2\,d\mu
+\int (v-u)e\,d\mu.}
\]
Thus tangential orbit energy exchanges with radial orbit kinetic energy and with the anisotropic volume factors \(u,v\). The term \((v-u)e\) has either sign; so does the tension-velocity term \(\langle\tau,b\rangle\). The fixed expanding tail has a damped linear energy because \(u,v,H\) are prescribed, but after the base responds dynamically, the damping identity acquires exactly these extra exchange terms.

In conformal gauge, for
\[
\mathcal E_z(r)=\int \rho |U_z|^2\,dz,\qquad 
\mathcal B_r(r)=\int \rho |U_r|^2\,dz,
\]
the weighted harmonic-map equation gives the stress identity
\[
\boxed{
(\mathcal E_z-\mathcal B_r)'
=\int \rho_r\bigl(|U_z|^2+|U_r|^2\bigr)\,dz.
}
\]
With defect source \(\mathcal R_0\), the right side gains
\[
-2\int \rho\langle \mathcal R_0,U_r\rangle\,dz.
\]
The sign is governed by the correlation between \(\rho_r\) and the map energy. The area equation
\[
\Delta \rho=6e^{2\lambda}\rho
\]
does not prescribe \(\rho_r\) slice-by-slice, and the base equation
\[
\Delta\lambda=\frac{|\nabla\sigma|^2-e_{\mathbb H^2}}4
\]
feeds orbit energy back into the next area response. Hence total orbit energy is not a closed monotone quantity.

Even if some version of orbit energy were increasing, it would not by itself prevent
\[
K=\langle e-h^2\rangle
\]
from decreasing: the area-gradient term \(\langle h^2\rangle\) can grow, and the volume weight can move toward regions where \(e-h^2\) is lower.

### (b) Squared distance has a convex elliptic identity, not a radial Lyapunov law

Let
\[
\phi(U)=\frac12 d_{\mathbb H^2}(U,P)^2,\qquad w=\nabla\phi(U).
\]
Because \(\mathbb H^2\) has curvature \(-1\),
\[
\nabla^2\phi\ge g_{\mathbb H^2}.
\]
The weighted harmonic-map equation gives the exact divergence identity
\[
\boxed{
\operatorname{div}\bigl(\rho\nabla(\phi\circ U)\bigr)
=
\rho\,\nabla^2\phi(dU,dU).
}
\]
With defect source \(\mathcal R_0\),
\[
\operatorname{div}\bigl(\rho\nabla(\phi\circ U)\bigr)
=
\rho\,\nabla^2\phi(dU,dU)
+\rho\langle w,\mathcal R_0\rangle.
\]
This is the standard convex-distance mechanism. It rules out an exact reflected cylinder that reaches \(U\equiv P\) at a finite outer slice: after doubling across the reflected slice, the convex subharmonic function cannot have that end behavior unless \(U\equiv P\).

But the slice functional
\[
\mathcal F_P(r)=\int \phi(U)\,d\mu
\]
does not satisfy a one-sided radial inequality. Its first derivative is
\[
\boxed{
\mathcal F_P'
=\int \bigl(\langle w,b\rangle+H\phi\bigr)\,d\mu.
}
\]
At a reflected center, \(b=0\) and \(H=0\), so \(\mathcal F_P'(0)=0\). Therefore an inequality of the form
\[
\mathcal F_P'\ge c\,\mathcal F_P,\qquad c>0,
\]
cannot hold from the center unless \(\mathcal F_P(0)=0\).

The second derivative displays the coupled obstruction:
\[
\boxed{
\mathcal F_P''
=
\int\Bigl[
\nabla^2\phi(b,b)
+\nabla^2\phi(U_s,U_s)
+(H'+H^2)\phi
+H\langle w,b\rangle
\Bigr]\,d\mu.
}
\]
The first two terms are positive in the source-free equation, but
\[
H'+H^2=3+H^2-|S|^2
\]
has either sign, and \(H\langle w,b\rangle\) can be strongly decreasing when the orbit map moves toward \(P\) in an expanding region. Thus convexity in the full \((r,z)\)-domain does not become monotonicity of \(\int\rho d^2(U,P)\) along \(r\).

A moving choice \(P=P(r)\), such as a weighted barycenter in \(\mathbb H^2\), removes one zero-mode of the distance variation but introduces \(P'\)-terms and still leaves the correlations with \(\rho_r\), \(H\), and \(b\). It does not control \(K\), which depends on \(U_s\) and \(h\), not on distance alone.

### (c) The Noether current removes only three zero modes

The matrix current
\[
\mathcal Q(r)=\int \rho\,M^{-1}M_r\,dz
\]
is constant for exact OT Einstein evolution, and reflection gives
\[
\mathcal Q\equiv0.
\]
This is a finite-dimensional constraint in \(\mathfrak{sl}(2,\mathbb R)\). It does not control
\[
\int \rho |M^{-1}M_r|^2\,dz
\sim \int |b|^2\,d\mu.
\]
Large oscillatory radial velocities may have zero matrix average. The nonabelian Maurer-Cartan relation couples \(M^{-1}M_r\) and \(M^{-1}M_z\), but it does not turn the vanishing of \(\mathcal Q\) into an \(L^2\) estimate.

There is a clean model illustrating the freedom. Take a constant-area loop \(U(s)\) in \(\mathbb H^2\), with \(\tau=D_sU_s\). For any Killing field \(X\) of \(\mathbb H^2\),
\[
\int \rho\,\langle X(U),\tau\rangle\,ds
=
\int \frac{d}{ds}\bigl(\rho\langle X(U),U_s\rangle\bigr)\,ds
=0.
\]
Thus \(b=\varepsilon\tau\) has zero Noether average. Replacing \(b\) by \(-b\) preserves \(K\), \(\langle |b|^2\rangle\), \(x\), \(y\), and \(\mathcal Q=0\), but changes
\[
-2\langle\tau,b\rangle
\]
to its opposite. In constant-speed loop geometries \(\tau\perp U_s\), so the leading Codazzi coupling through \(\langle U_s,b\rangle\) can also vanish. This shows why \(\mathcal Q=0\) cannot determine the sign of \(K'\).

The Noether current is still useful: it removes the pure radial translation of the orbit map in the symmetric-space directions. But the \(K\)-production term lives in all nonzero loop modes, precisely where \(\mathcal Q\) gives no size control.

### (d) Finite-moment Lyapunov combinations do not close

Let
\[
A=\langle h^2\rangle,\qquad B=\langle |b|^2\rangle.
\]
The normalized exact evolutions include
\[
\boxed{
B'
=
-2\langle\tau,b\rangle
-\langle H|b|^2\rangle
-(x+y)B,
}
\]
and, using Codazzi,
\[
\boxed{
A'
=
\operatorname{Cov}(u,h^2)-yA
-\langle h\langle U_s,b\rangle\rangle.
}
\]
The already derived \(K\)-law is
\[
\boxed{
K'=
-2\langle\tau,b\rangle
+2\langle vc\rangle
+\operatorname{Cov}(v-u,k)
-2xK.
}
\]
Codazzi rewrites
\[
\boxed{
2\langle vc\rangle
=
-2\langle h^2u\rangle
+\langle h^2v\rangle
+\langle h\langle U_s,b\rangle\rangle.
}
\]

These formulas explain why a Lyapunov functional depending only on
\[
K,\quad x,\quad y,\quad B,\quad A
\]
does not acquire a one-sided derivative. For a trial expression
\[
\mathcal L=\Phi(K,x,y,A,B),
\]
the derivative contains independent sign-changing productions:
\[
\langle\tau,b\rangle,\qquad
\langle h\langle U_s,b\rangle\rangle,\qquad
\langle H|b|^2\rangle,\qquad
\operatorname{Cov}(v-u,k),\qquad
\operatorname{Cov}(u,h^2).
\]
One may cancel \(\langle\tau,b\rangle\) by combining \(K\) with \(-B\):
\[
(K-B)'
=
2\langle vc\rangle
+\operatorname{Cov}(v-u,k)
-2xK
+\langle H|b|^2\rangle
+(x+y)B.
\]
But then the term \(\langle H|b|^2\rangle\) appears, and \(H\) is local, not just \(x+y\). Adding \(A\) can cancel the \(\langle h\langle U_s,b\rangle\rangle\) contribution after using Codazzi, but it leaves the \(u,v,h^2,k\) covariance terms. Those are not determined by \(K,x,y,A,B\).

Thus a closed inequality such as
\[
\mathcal L'\ge c\,\mathcal L
\]
or
\[
\mathcal L'\ge 0
\]
does not follow from the known OT balances in this finite family. A stronger functional would need to track the full phase relation between the loop tension \(\tau\) and radial velocity \(b\), plus the local volume response \(u,v,h\), not just their first few averages.

### Resulting freedom in the full coupled OT system

The known monotone/convex structures leave the following degrees of freedom available:

1. **Tension–velocity phase.**  
   The term \(-2\langle\tau,b\rangle\) can drive \(K\) downward if \(b\) becomes aligned with \(\tau\) after the universal initial phase, where \(b\sim-r\tau\) and \(K\) rises.

2. **Area-gradient subtraction.**  
   Since \(K=\langle e-h^2\rangle\), growth of \(h^2\) can lower \(K\) even when total orbit energy does not decrease.

3. **Volume redistribution.**  
   The evolving weight \(d\mu=\rho ds\) can emphasize regions with lower \(k=e-h^2\). The equations for \(\rho\) and \(\lambda\) respond to orbit energy, so this is part of the coupled dynamics, not an external choice.

4. **Mean/covariance separation.**  
   The clean equations for \(x\) and \(y\),
   \[
   x'=3-\frac12K-x(x+y),\qquad
   y'=6-y(x+y),
   \]
   do not determine the covariance terms in \(K'\). The reversal threshold is controlled by local correlations of \(u,v,k,h,b\), not by means alone.

5. **Noether-compatible oscillations.**  
   \(\mathcal Q=0\) removes only the matrix average of radial motion. Oscillatory \(b\)-fields can carry large \(L^2\) energy and large \(\langle\tau,b\rangle\) while preserving \(\mathcal Q=0\).

So the present known structures do not exclude a nonlinear \(K\)-drop in the full OT system. The one strong convex tool excludes exact relaxation to a constant orbit map at a finite outer slice; it does not produce a radial Lyapunov inequality for \(K\). A genuine obstruction would need a new nonlocal identity tying \(\langle\tau,b\rangle\), the Codazzi covariance terms, and the volume response to \(K,x,y,A,B\) in a one-sided way.
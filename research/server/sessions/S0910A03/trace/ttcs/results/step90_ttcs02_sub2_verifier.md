# TTCS Independent Branch Record

```json
{
  "step_id": 90,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/scripts/step90_radial_twist_core.py",
    "Sessions/S0910A03/workspace/data/step90_radial_twist_core.json",
    "Sessions/S0910A03/workspace/scripts/step90_radial_twist_taper.py",
    "Sessions/S0910A03/workspace/data/step90_radial_twist_taper.json",
    "Sessions/S0910A03/workspace/scripts/step90_taper_scaling_summary.py",
    "Sessions/S0910A03/workspace/data/step90_taper_scaling_summary.json",
    "Sessions/S0910A03/workspace/scripts/step89_symbolic_twist_ricci.py",
    "Sessions/S0910A03/workspace/data/step89_symbolic_twist_ricci.json"
  ]
}
```

## Task

Verify the new Step 90 radial charged-core and forced-discharge computation as a scientific result. Read the structured reduction note and all four radial scripts/data summaries. Check: (1) whether the ODEs for gamma=dr^2+psi^2 dtheta^2, M=diag(e^alpha,e^-alpha), q=(q(r),0) correctly encode the reduced area, traceless-orbit, and horizontal equations under the stated forcing; (2) smooth-center coefficients, especially K(0)=3Q0/2; (3) whether monitoring the unused rr equation is meaningful and whether its small residual is algebraic/constraint propagation rather than accidental; (4) whether prescribed b=-A sin^2(pi s/L), w'=b-(3u+v)w/2 corresponds to mixed Ricci defect O(delta), and what endpoint regularity is missing for an exact splice; (5) interpret the numerical scaling without overstating it. Determine precisely what the runs establish or refute inside the reduced free/singular-orbit T^2 model, and identify any coefficient/sign error that changes the conclusion.

## Output

## Verifier memo — Step 90 radial charged core and forced discharge

I reproduced the reduction algebra, the smooth-center expansion, the constraint structure, and the discharge scaling by hand and against the JSON. The reduced ODE system is encoded correctly, the central coefficient $K(0)=\tfrac32Q_0$ is exact, the monitored $rr$ equation is a genuine Hamiltonian constraint that propagates by an identity I verified in closed form, and the numerical statements are stated at the right strength. I found no coefficient or sign error. Details, with the pieces the core agent can re-check.

### 1. The ODEs correctly encode area, traceless-orbit, and horizontal equations

Base $\gamma=dr^2+\psi^2d\theta^2$, orbit $G=e^\sigma\mathrm{diag}(e^\alpha,e^{-\alpha})$, $q=(q_0,0)$, target $\mathrm{Ric}=-3g$ (so $E=\mathrm{Ric}+3g=0$). With $u=\sigma',v=\alpha',H=\psi'/\psi,K=-\psi''/\psi$:

- **Area / orbit-trace (1.1) with $T=0$.** The weighted Laplacian on a radial function is $L\sigma=\Delta_\gamma\sigma+|\nabla\sigma|^2=(u'+Hu)+u^2$. Setting $L\sigma=6+Q$ gives exactly $u'=6+Q-u^2-Hu$ (6.1a). The constant $6$ is the $\mathbb H^4$ horospherical value: at $u=2,H=1,Q=0$ the right side is $6-4-2=0$, and $\sigma=2r,\psi=e^r,\alpha=0$ is the flat-$T^3$ cusp $dr^2+e^{2r}(d\theta^2+d\xi_1^2+d\xi_2^2)$ with $\mathrm{Ric}=-3g$. This matches the observed attractor $(u,v,H,K,Q)\to(2,0,1,-1,0)$.
- **Traceless-orbit (1.2) with $Z=0$.** For diagonal $M$ ($\beta=0$), $Q=\tfrac12 q_0^2e^{-3\sigma-\alpha}$ gives $\partial_\alpha Q=-Q$, so the $\mathbb H^2$ tension equation is $L\alpha=-\partial_\alpha Q=+Q$, i.e. $v'+Hv+uv=Q$, hence $v'=Q-Hv-uv$ (6.1b). Consistent with the note's "$L\alpha=Q$".
- **Horizontal $\theta\theta$.** In 2D the base Ricci is $K\gamma_B$. The orthonormal $\theta\theta$ component of (1.3), $K-Hu=-3+Q$, gives $K=-3+Q+Hu$ (6.2a). The orthonormal $rr$ component, $K-u'-\tfrac12u^2=-3+Q+\tfrac12v^2$, is the **unused** equation, exactly the script's `Err = K - u' + 3 - Q - u²/2 - v²/2`.
- $H'=-K-H^2$ (6.2b) is the geometric identity for $\psi''/\psi$, not an Einstein equation.

The taper `rhs` uses the same four right sides with $Q=\tfrac12w^2$ and replaces charge conservation by $w'=b-\tfrac12(3u+v)w$; area/orbit/$\theta\theta$ stay exact, only $rr$ is left free. All encoding is correct.

### 2. Smooth-center jets, in particular $K(0)=\tfrac32Q_0$

With $u=u_1r,\,v=v_1r,\,H=r^{-1}+h_1r,\,Q=Q_0+O(r^2)$:
- (6.1a) leading: $u_1=6+Q_0-u_1\Rightarrow u_1=\tfrac{6+Q_0}{2}$.
- (6.1b) leading: $v_1=Q_0-v_1\Rightarrow v_1=\tfrac{Q_0}{2}$.
- (6.2a): $Hu\to u_1$, so $K(0)=-3+Q_0+\tfrac{6+Q_0}{2}=\tfrac{3Q_0}{2}$.
- $\psi=r-\tfrac{Q_0}{4}r^3$ gives $H=r^{-1}-\tfrac{Q_0}{2}r$.

All match (6.3) and the script's `init`. The JSON confirms $K(r{=}10^{-5})=0.15,1.5,4.5,15,150$ for $Q_0=0.1,1,3,10,100$, i.e. $\tfrac32Q_0$ to full precision.

### 3. The monitored $rr$ equation is a real constraint and its residual is propagation, not accident

Define the $rr$ residual $C=K-u'-\tfrac12u^2-\tfrac12v^2+3-Q$. Substituting the three evolution equations and $Q'=-(3u+v)Q$ (exact charge conservation) collapses it to
$$C=2Hu+\tfrac12u^2-\tfrac12v^2-Q-6,$$
and I verified term-by-term that along the flow
$$\boxed{\,C'=-2(u+H)\,C\,}.$$
Two consequences. (i) $C(0)=2\cdot\tfrac{6+Q_0}{2}-Q_0-6=0$, so the smooth-center data already satisfies the constraint. (ii) Near $r=0$, $-2(u+H)\sim-2/r$, so any nonzero homogeneous solution behaves like $r^{-2}$; regularity forces $C\equiv0$, and thereafter $C$ is exponentially damped ($u+H\to3$ on the cusp, $C\sim e^{-6r}$). This is the contracted second Bianchi identity made explicit: the evolution subsystem propagates the full Einstein equations. The observed `max_rel_rr_constraint` $\sim10^{-9}$–$10^{-10}$ tracks `rtol=1e-10`, and `rr_constraint_at_final` $\sim10^{-15}$ matches the predicted damping — exactly integration error on top of an exact identity. Monitoring the unused equation is therefore meaningful and the small numbers are real, not coincidental.

This identity is also the sharpest internal consistency test of the whole model (see §6).

### 4. Forcing = mixed-Ricci defect $O(\delta)$; what is missing for an exact splice

From $w=|q|\,e^{-(3\sigma+\alpha)/2}$, $\ln w'=q'/q-\tfrac12(3u+v)$, so
$$w'=b-\tfrac12(3u+v)w,\qquad b:=e^{-(3\sigma+\alpha)/2}q'.$$
Nonzero $b$ means $q'\neq0$, which by the mixed-Ricci law (1.4) requires a nonzero $E_{\rm mix}$; with (1.5), $\max|b|=C(L)\delta$ corresponds to $\|E_{\rm mix}\|=O(\delta)$ (the runs keep $C(L)/2\lesssim0.9<1$ for $L\ge0.5$, so a mixed defect below $\delta$). The other blocks $T,Z,\theta\theta$ are held at zero. So the collar is an **approximate** Einstein metric with $\|\mathrm{Ric}+3g\|=O(\delta)$ from the mixed block.

The taper leaves the $rr$ block off. With forcing, $Q'=wb-(3u+v)Q$, so the constraint identity acquires a source:
$$C'=-2(u+H)\,C-wb,\qquad |wb|\lesssim C(L)\,\delta^2 .$$
The strong damping gives a steady $|C|\sim wb/(2(u+H))=O(\delta^2)$, which is precisely the reported `Err_over_delta2` $\in[0.066,0.073],[0.011,0.013],[4\!-\!5]\times10^{-4}$ for $L=0.5,1,2$. So the $O(\delta^2)$ $rr$ residual is explained quantitatively as the forced source, not fitted.

Missing for an exact splice: (a) the collar is **not** an exact Einstein metric — the $rr$ block carries an uncorrected $O(\delta^2)$ defect; (b) the profile $b=-A\sin^2(\pi s/L)$ has $b(0)=b(L)=0$ and $b'(0)=b'(L)=0$ but $b''(0),b''(L)=-A\,2\pi^2/L^2\neq0$, so the connection curvature $F$ (hence $q$) matches the twist-free/OT exterior only to first order; all higher endpoint derivatives must vanish for a $C^\infty$ junction. Both the endpoint-jet matching and the correction of the $O(\delta^2)$ block to an exact solution are open.

### 5. Scaling, stated at the right strength

The discharge is governed by the linear cusp equation $w'+3w=b$: $A=\delta/\int_0^L e^{3s}\sin^2(\pi s/L)\,ds$, i.e. $A/\delta=e^{-3L}/I(L)=1.8215,0.3860,0.0285$ for $L=0.5,1,2$. The nonlinear runs give $[1.75,1.85],[0.36,0.40],[0.027,0.029]$ — agreement to a few percent, with the residual $Q_0$-spread coming from the switch geometry not being perfectly round at finite $\delta$. The note's "$A=C(L)\delta$ independent of $Q_0$" is therefore an asymptotic ($\delta\to0$) statement, correctly qualified. The note also explicitly defers the operator-norm conversion to "all reduced blocks," so it does not overstate the discharge as a norm bound.

**What the runs establish (inside the reduced radial model):**
- A one-parameter ($Q_0$) family of **exact** solutions of the full reduced $\mathrm{Ric}=-3g$ system on the polar-base / collapsing-$\theta$ configuration, smooth at the center, with arbitrarily large central twist $Q_0$, redshifting $Q\propto e^{-3\sigma-\alpha}\to0$ to the round hyperbolic cusp. Exactness (all blocks, including $rr$) rests on the verified constraint identity, not on the numerics alone.
- Consequently, any proposed theorem deriving $Q_+=O(\delta)$ from mixed-Ricci control plus one exact OT end is refuted: large physical twist is compatible with the exact equations and simply dilutes.
- A concrete redshift-and-discharge mechanism: from $w=\delta$, an $O(\delta)$ mixed forcing over length $L$ drives $w\to0$ following the linear prediction, with area/orbit/$\theta\theta$ exact and $rr$ residual $O(\delta^2)$.

**What they do not establish (open, and the note says so):** not a counterexample to Yau 26 — the model is non-compact, the collar is not exact Einstein, the splice is only first-order at the ends, and the topology is a collapsing-$\theta$ disk rather than the free two-ended cylindrical/minimal-separator setting. The next mathematical question — whether such a charged region survives on a free cylindrical base with two outward ends — is correctly identified as the real one.

### 6. Coefficient / sign audit

No error found; each contested number is pinned:
- **Constant $6$ in (6.1a).** Replacing it by $c$ gives $C(0)=6-c$, an $O(1)$ central residual for $c\neq6$. Observed residual $\sim10^{-9}$ ⇒ $c=6$.
- **Sign of $Q$ in (6.2a).** Using $K=-3-Q+Hu$ gives $C(0)=-2Q_0$, i.e. residual $\sim200$ at $Q_0=100$. Not observed ⇒ sign is $+Q$.
- **Sign of $Q$ in (6.1a),(6.1b) and the damping $-\tfrac12(3u+v)$.** All are consistent with (i) $K(0)=\tfrac32Q_0$ matching to full precision, and (ii) closure of the propagation identity $C'=-2(u+H)C$, which would break under any single mismatched coefficient.
- The step-89 SymPy blocks ($\hat R^{\rm tw}_{\rm orbit}=+Q$ in direction 1 and $0$ in direction 2, $\hat R^{\rm tw}_{\rm base}=-Q\gamma_B$, mixed law) are internally consistent with $Q=\tfrac12 G_{11}(f^1)^2$ and with the $+Q$/$-Q$ bookkeeping the note tracks in §1–§3.

The single most load-bearing fact I can add for the core agent: the exactness of the §6 core is not merely numerical — it follows from the closed-form constraint-propagation identity $C'=-2(u+H)C$ together with the regularity selection $C\equiv0$ at the smooth center. That is the piece worth carrying forward, both because it certifies the core as an honest solution family and because the same identity, with source $-wb$, is what pins the collar's $rr$ defect at $O(\delta^2)$.
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 47,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step47_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step47_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the logical chain of the consolidated restricted negative IL gap theorem in the provided file. Focus on these five load-bearing points:

1. COLLAPSE CANCELLATION (§3d): The claim is that on a good ball where the volume-averaging maximal function satisfies M_vol(|Rm|²)(x) ≤ κ², the initial curvature energy satisfies K₂ ≤ (1+κ²)Vol(B), and the Sobolev constant S ≤ Cr²/√Vol(B). Therefore γ = S·K₂^{1/2} ≤ Cr²√(1+κ²), independent of Vol. Check: is this computation correct? Does the volume-averaging Hardy-Littlewood maximal inequality hold under Ric ≥ -3g with the stated constants? Is the Maheux-Saloff-Coste Sobolev inequality correctly stated?

2. TERMINAL POINT SELECTION (§7b-7c): The claim is that min_{x∈Π} D(x,T) ≤ (119C₁/α)δ² → 0, and then a subsequence of pullback metrics on B_R(0) ⊂ R⁴ converges C^∞ to an Einstein limit with D_h(0) = 0. Check: is the minimum-of-average-gives-small-minimum argument correct? Does the pullback chart have noncollapsed volume (Rauch comparison under bounded curvature)? Does C^k convergence pass D to the limit?

3. SPECTRAL DETERMINATION (§7d): From D_h(0)=0 on the Einstein limit with s=-4, the claim is |W⁺|² = 1/24 and G = 0, forcing Spec(W⁺) = (-1/6,1/12,1/12). Check the algebra: G = 4ξ(3-ξ) where ξ = w + √(2/3)|W⁺|, so G=0 forces ξ=0, hence w=-1/6.

4. PROJECTOR-BOCHNER (§7e): The claim is that on any connected Einstein 4-manifold with Ric=-g and W⁺ spectrum (-1/6,1/12,1/12) at one point, the simple eigenform is parallel (from δW⁺=0 + constant eigenvalue), so ∇W⁺=0 and |W⁺|²=const, and then the Bochner identity gives 0 = -1/8, a pointwise contradiction. Check: is the projector argument correct for a LOCAL domain (not just closed manifolds)?

5. SELF-IMPROVING FIRST-EXIT (§5h): The drift estimate d(T) ≤ Cδθ^{2/3}r² is used to keep Sobolev constants comparable. Check: does the bilipschitz comparison from small drift transport the local Sobolev constant correctly? Is the self-improving closure non-circular?

## Integrated Scientific Memo

## Verification verdict

The consolidated proof is **not complete as written**. Points 1 and 3 are correct with minor scale/formulation qualifications. Point 2 is essentially correct after fixing volume bookkeeping and selecting from buffered cores. The local projector lemma in Point 4 is valid, but §7e applies it from only one-point spectral data; that inference is false. There is, however, a plausible repair using the stated terminal derivative bounds and a low-average **core ball**, without requiring injectivity or bounded covering multiplicity. Point 5 correctly handles Sobolev transport and drift, but the displayed \(K_2\) estimate is too weak to close the first-exit threshold.

### 1. Collapse cancellation

Let
\[
V_\alpha=\operatorname{Vol}_{g(0)}B_{6r}(x_\alpha).
\]
Provided \(6r\le1\), \(x_\alpha\in G\) gives
\[
\int_{B_{6r}(x_\alpha)}|\operatorname{Rm}|^2
 \le \kappa_0^2V_\alpha.
\]
Thus, assuming \(0\le\eta_\alpha\le1\),
\[
K_{2,\alpha}(0)
=\int\eta_\alpha^2(1+|\operatorname{Rm}|^2)
\le(1+\kappa_0^2)V_\alpha.
\]

The required local Sobolev inequality is the compact-support version
\[
\|u\|_{L^4(B_R)}^2
\le
C\,e^{CR}\frac{R^2}{\operatorname{Vol}(B_R)^{1/2}}
\left(\|\nabla u\|_2^2+R^{-2}\|u\|_2^2\right),
\qquad u\in C_c^\infty(B_R),
\]
under \(\operatorname{Ric}\ge-3g\). For \(R=6r\le1\), the exponential and numerical factors are absorbed into \(C\), yielding (3.3). Hence
\[
\gamma_\alpha
\le
\frac{Cr^2}{V_\alpha^{1/2}}
\bigl((1+\kappa_0^2)V_\alpha\bigr)^{1/2}
=
Cr^2\sqrt{1+\kappa_0^2}.
\]
The cancellation is exact and collapse-independent.

Bishop–Gromov gives uniform local doubling at all fixed radii involved in a Vitali proof of the maximal inequality. Therefore the truncated volume-average maximal operator satisfies
\[
\operatorname{Vol}\{\mathcal M_{\rm vol}f>\lambda\}
\le \frac{C_{\rm HL}}{\lambda}\int|f|,
\]
with \(C_{\rm HL}\) depending only on dimension and the fixed Ricci/radius scale, not on injectivity radius or collapse.

**Necessary edit:** impose \(r\le1/6\) and state (3.3) for compactly supported \(u\).

---

### 2. Terminal selection and pullback compactness

The averaging argument is valid:
\[
\inf_\Pi\mathfrak D
\le \frac{\int_\Pi\mathfrak D}{\operatorname{Vol}_{g(T)}\Pi}.
\]
“Minimum” should be replaced by “infimum” unless compact closed domains are used.

The volume lower bound in §3b is for \(g(0)\), whereas §7b integrates using \(g(T)\). From
\[
\partial_tg=-2aE,\qquad
d(t)=\int_0^t\|aE\|_{\infty,g(s)}\,ds,
\]
one obtains
\[
e^{-2d(t)}g(0)\le g(t)\le e^{2d(t)}g(0),
\]
and in dimension four
\[
e^{-4d(t)}d\mu_{g(0)}
\le d\mu_{g(t)}
\le e^{4d(t)}d\mu_{g(0)}.
\]
Thus the initial volume fraction remains bounded below by a fixed multiple, for example \(e^{-8d_0}\alpha_0\). This only modifies \(\alpha\).

A more important correction is to select from the buffered cores
\[
\Omega=\bigcup_{\alpha\in\mathcal C}B_r^{g(0)}(x_\alpha),
\]
not from all of \(\Pi=\bigcup B_{4r}(x_\alpha)\). These \(B_r\)'s are disjoint and already satisfy
\[
\operatorname{Vol}_{g(0)}\Omega
=\sum_\alpha\operatorname{Vol}_{g(0)}B_r(x_\alpha)
\ge \alpha_0\operatorname{Vol}_{g(0)}M.
\]
Every core point has a uniform buffer inside a region where \(a=1\). A point chosen near the boundary of \(B_{4r}\) need not have any common-radius \(a=1\) neighborhood.

Under uniform sectional-curvature and derivative bounds, choose
\[
R<\min\{cr,\pi/(2\sqrt K)\}.
\]
Rauch/Jacobi comparison gives
\[
c^{-1}g_{\mathrm{Euc}}
\le \exp_{x_i}^{*}g_i(T_i)
\le cg_{\mathrm{Euc}}
\quad\text{on }B_R(0)\subset T_{x_i}M_i,
\]
hence
\[
\operatorname{Vol}_{\exp^*g_i}B_R(0)\ge cR^4.
\]
The exponential map need not be injective in a collapsed manifold. Nevertheless, its pullback defines a smooth metric on the tangent ball, which is sufficient for local compactness and tensor equations.

Smooth convergence passes \(E,s,W^+\), ordered Weyl eigenvalues, \(G\), and \(\mathfrak D\) to the limit. Thus \(\mathfrak D_i(x_i)\to0\) gives \(\mathfrak D_h(0)=0\). To conclude \(\operatorname{Ric}_h=-h\) on a whole fixed ball, the centers must have the above buffer, since the available estimate is for \(aE\), not \(E\) where \(a\) may vanish.

---

### 3. Spectral determination

This algebra is correct. At a point with \(\mathfrak D=0\),
\[
E=0,\qquad s=-4,\qquad |W^+|=\frac1{2\sqrt6},
\qquad |W^+|^2=\frac1{24}.
\]
Writing \(u=|W^+|\), \(\alpha=\sqrt{2/3}\), and
\[
\xi=w+\alpha u=w+\frac16,
\]
one has \(0\le\xi\le1/6\). Moreover
\[
f=\frac23s-2\alpha u=-3,\qquad b=f+2\xi=-3+2\xi<0,
\]
so
\[
G=f^2-b^2=4\xi(3-\xi).
\]
Therefore \(G=0\) forces \(\xi=0\), hence \(w=-1/6\). If the remaining eigenvalues are \(\lambda_1,\lambda_2\), then
\[
\lambda_1+\lambda_2=\frac16,\qquad
\lambda_1^2+\lambda_2^2=\frac1{72},
\]
and consequently \(\lambda_1=\lambda_2=1/12\).

Thus
\[
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
at that point.

---

### 4. Projector–Bochner: valid lemma, invalid application, and a possible repair

The local projector lemma from Step 6 is correct and requires no closedness. On an open set where
\[
W^+=\mu I+(\lambda-\mu)P_\omega
\]
with two distinct **constant** eigenvalues, \(\delta W^+=0\) implies
\[
(\nabla^a\omega_{ab})\omega_{cd}
+\omega_{ab}\nabla^a\omega_{cd}=0.
\]
Contracting with \(\omega^{cd}\) gives \(\nabla^a\omega_{ab}=0\); substitution gives
\[
\omega_{ab}\nabla^a\omega_{cd}=0.
\]
Since a nonzero self-dual two-form is nondegenerate,
\[
\omega_a{}^c\omega_c{}^b=-\delta_a{}^b,
\]
so \(\nabla\omega=0\), hence \(\nabla W^+=0\).

The Bochner arithmetic is also correct:
\[
s|W^+|^2-36\det W^+
=-\frac4{24}-36\left(-\frac1{864}\right)
=-\frac18.
\]

However, §7c–§7d establish the calibrated spectrum only at the origin. Continuity preserves simplicity nearby but does **not** make the eigenvalue equal to \(-1/6\) nearby, nor keep the other two eigenvalues equal. Thus the statement in §7e that the eigenvalue is “constant … by continuity” is false. At one point, the identity merely says
\[
\Delta|W^+|^2(0)
=2|\nabla W^+|^2(0)-\frac18,
\]
which is not contradictory.

#### Repair using the stated core-ball geometry

A bounded-sheet unwrapping assumption is not necessary if the terminal derivative bounds are genuinely uniform. Because the core balls \(\Omega_\alpha=B_r(x_\alpha)\) are disjoint,
\[
\sum_\alpha\int_{\Omega_\alpha}\mathfrak D
\le C\delta_i^2\operatorname{Vol}M_i,
\qquad
\sum_\alpha\operatorname{Vol}\Omega_\alpha
\ge c\operatorname{Vol}M_i.
\]
Hence some core ball satisfies
\[
\fint_{\Omega_{\alpha_i}}\mathfrak D_i\le C\delta_i^2. \tag{*}
\]

On a smaller buffered core, the asserted Shi bounds imply a uniform Lipschitz estimate
\[
|\nabla\mathfrak D_i|\le L.
\]
This is legitimate despite the minimum eigenvalue in \(G\): ordered eigenvalues are Lipschitz in the endomorphism, and \(b\mapsto(\min\{b,0\})^2\) is \(C^1\).

If \(y\) lies in an inner core and \(m=\mathfrak D_i(y)\), then
\[
\mathfrak D_i\ge m/2
\quad\text{on}\quad
B_\rho(y),\qquad
\rho=\min\{cr,m/(2L)\}.
\]
Relative Bishop–Gromov comparison supplies
\[
\frac{\operatorname{Vol}B_\rho(y)}
     {\operatorname{Vol}\Omega_{\alpha_i}}
\ge c\left(\frac{\rho}{r}\right)^4,
\]
without requiring noncollapse. Combining this with (*) yields
\[
C\delta_i^2
\ge c\,m\min\left\{1,\left(\frac{m}{Lr}\right)^4\right\}.
\]
Therefore
\[
\sup_{\Omega_{\alpha_i}^{\rm inner}}\mathfrak D_i\to0
\]
(and in the small-\(m\) regime, \(m\le C\delta_i^{2/5}\)).

Pulling back at the center of this selected ball now gives
\[
\mathfrak D_h\equiv0
\]
on a fixed open tangent ball. Since \(E_h=0\), the spectral calculation applies at every point there, yielding the constant spectrum
\[
\operatorname{Spec}(W_h^+)
\equiv\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
The local projector lemma then gives \(\nabla W_h^+=0\), contradicting the Bochner identity.

This repair requires explicit verification that:

1. the \(C^1\) curvature bounds, hence \(L\), are uniform across the escaping sequence on a fixed buffered core;
2. the terminal relative-volume comparison is uniform after bilipschitz transport;
3. the selected inner core has a fixed-radius \(a=1\) neighborhood.

Absent that strengthening, the theorem remains unproved. The original one-point argument alone is definitely insufficient.

---

### 5. Self-improving first exit

Small drift correctly transports the local Sobolev inequality. On each fixed cutoff domain,
\[
e^{-2d_0}g(0)\le g(t)\le e^{2d_0}g(0)
\]
makes the \(L^4\), \(L^2\), and gradient norms comparable, so
\[
\mathcal S_\alpha(t)\le e^{Cd_0}\mathcal S_\alpha(0).
\]
Cutoff-gradient norms and local energies are likewise comparable.

The drift closure is non-circular. Before the first-exit time, \(d(t)<d_0\) holds by definition, so the transported Sobolev inequality is available while deriving (5.5). For every \(\tau\le T\),
\[
d(\tau)
\le C\delta r^{2/3}\tau^{2/3}
\le C\delta\theta^{2/3}r^2.
\]
Choosing \(\delta\) last, with strict margin, rules out exit through \(d=d_0\).

The \(K_2\) exit is not closed by the displayed estimate
\[
\sup_{t\le\tau}K_2(t)\le CK_2(0).
\]
A generic \(C\) need not be \(<2\), and shrinking \(\delta\) does not change it. What is needed is a retained-initial-value inequality such as
\[
K_2(t)+c\int_0^tD_2
\le K_2(0)+C\int_0^t(1+r^{-2})K_2(s)\,ds,
\]
which gives
\[
K_2(t)\le
e^{C(1+r^{-2})t}K_2(0)
\le e^{C\theta(1+r^2)}K_2(0).
\]
Choosing \(\theta\) sufficiently small then gives a strict improvement, e.g.
\[
K_2(t)\le \frac32K_2(0).
\]
The consolidated file neither states nor derives this sharper estimate. Therefore §5h is incomplete on its displayed equations, even though the intended Grönwall repair is standard in form.

## Bottom line

The five-point chain has two substantive gaps:

1. **§7e:** one-point calibrated spectrum is incorrectly promoted to neighborhood-wise constant spectrum. This can plausibly be repaired by low-average selection of an entire disjoint core ball plus uniform Lipschitz control of \(\mathfrak D\).
2. **§5h:** (5.1) does not imply strict improvement of the threshold \(K_2=2K_2(0)\). A time-sensitive Grönwall estimate with coefficient tending to \(1\) as \(\theta\to0\) is required.

Accordingly, Theorem A and its asserted family uniformity are **not established by the present consolidated text**. The spectral algebra, collapse cancellation, tangent-pullback compactness, local projector lemma, Bochner computation, Sobolev transport, and drift non-circularity are otherwise sound subject to the qualifications above.
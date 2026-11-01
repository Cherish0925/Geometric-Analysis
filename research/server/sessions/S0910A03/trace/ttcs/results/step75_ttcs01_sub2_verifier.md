# TTCS Independent Branch Record

```json
{
  "step_id": 75,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/data/step75_structural_identities.json",
    "Sessions/S0910A03/workspace/scripts/step75_structural_identities_verify.py",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md",
    "Sessions/S0910A03/workspace/data/step70_ricci_T2inv.json"
  ]
}
```

## Task

For the Yau-26 negative graph-neck program, independently check the mathematical results in the Step-75 note. Verify from first principles: (i) for q=ds^2+G(s) on T^3 with flat T^2 orbits and R_q=-6, the formula R_q=-2h'-|A|^2-h^2 and the downward-zero argument forcing an orbit-plane sectional curvature >=3; (ii) the equivalence to an eigenvalue <=-3 of Ric_q+3I and to reflected Einstein shape acceleration; (iii) under |Ric_4+3g|_op<=delta at a reflected center, the stated quantitative constant lambda_min S'(0)<=-3+5delta, including every trace and sign; (iv) the finite-cylinder anisotropy integration showing reflection plus exact equal orbit normal derivatives at the exit forces d=b-c constant and makes the scalar-minus-six center impossible; (v) the normal weighted identity and physical-length inequality. Report corrected formulas if anything is wrong, and distinguish exact results from statements requiring extra regularity, orientation, coordinates, or boundary assumptions.

## Output

## Verifier Memo — Step-75 center theorem, cylinder rigidity, and normal identity

I reworked each result from first principles. Every formula in parts (i)–(v) is correct as written, including all traces and signs. Below I give the independent derivations, confirm the numbers, and state precisely which conditions each result requires and where each is exact versus contingent on symmetry/gauge/outer-face data.

---

### (i) Scalar identity $R_q=-2h'-|A|^2-h^2$ and the downward-zero curvature statement

For $q=ds^2+G(s)_{ab}dx^adx^b$ on $T^3$ with $N=\partial_s$ the unit normal and $A=\tfrac12G^{-1}G'$ the orbit shape operator:

- $h=\operatorname{tr}A=\tfrac12\operatorname{tr}(G^{-1}G')=\tfrac12(\log\det G)'=(\log\sqrt{\det G})'$ by Jacobi's formula. Correct.
- Riccati trace gives $\operatorname{Ric}_q(N,N)=-h'-|A|^2$ (with $|A|^2=\operatorname{tr}(A^2)$, valid since $A$ is $G$-self-adjoint, including non-diagonal $G$).
- Trace-Gauss for the flat orbit ($R_\Sigma=0$, because a constant-in-$x^a$ metric on $T^2$ is intrinsically flat for every $s$): $R_q=R_\Sigma-(h^2-|A|^2)+2\operatorname{Ric}_q(N,N)=-(h^2-|A|^2)+2(-h'-|A|^2)=-2h'-|A|^2-h^2$. **Confirmed (3.3).**

Downward-zero: $h=(\log\sqrt{\det G})'$ is a derivative of a smooth periodic function, so $\oint h=0$. If $h\not\equiv0$ it changes sign, so there is a point with $h=0$ and $h'\le0$. At that point $R_q=-6$ gives $|A|^2=6-2h'$, hence $\tfrac12|A|^2=3-h'\ge3$. Since $A$ is trace-free self-adjoint on a 2-plane there, eigenvalues $\pm\lambda_1$, so $-\det A=\lambda_1^2=\tfrac12|A|^2$, and the Gauss relation for the flat orbit gives $K_{\rm orb}=-\det A=\tfrac12|A|^2\ge3$. The $h\equiv0$ case gives equality $\tfrac12|A|^2=3$. **All of (3.4)–(3.5) confirmed exactly.** The only structural input is smoothness/periodicity so that $h$ has mean zero and a downward zero exists.

### (ii) Equivalence to an eigenvalue $\le-3$ of $\operatorname{Ric}_q+3I$ and to $S'(0)$

Three-dimensional identity for unit $v\perp$ orbit: $\operatorname{Ric}_q(v,v)=\tfrac12R_q-K_{\rm orb}$, so with $R_q=-6$,
$$(\operatorname{Ric}_q+3q)(v,v)=\operatorname{Ric}_q(v,v)+3=-3-K_{\rm orb}+3=-K_{\rm orb}\le-3.$$
**Confirmed (3.6).** Hence $\lambda_{\min}(\operatorname{Ric}_q+3I)\le-3$.

For the reflected ($S(0)=0$) center of an exact $\operatorname{Ric}_g=-3g$ four-core: the Gauss constraint $R_q=R_g-2\operatorname{Ric}_g(N,N)+H^2-|S|^2$ at $S=0$ gives $R_q=-12-2(-3)=-6$, so (i)–(ii) apply to the center slice. The radial equation $S'+S^2=-\mathcal R$ with $\mathcal R_{ab}=R_{aNbN}$ gives at the center $S'(0)=-\mathcal R$. Totally-geodesic Gauss gives $\operatorname{Ric}_g(e_a,e_b)=\operatorname{Ric}_q(e_a,e_b)+\mathcal R_{ab}$, and Einstein $\operatorname{Ric}_g=-3g$ yields $\mathcal R=-3I-\operatorname{Ric}_q^\sharp$, hence
$$S'(0)=\operatorname{Ric}_q^\sharp+3I.$$
**Confirmed (3.7).** Therefore $\lambda_{\min}(S'(0))=\lambda_{\min}(\operatorname{Ric}_q+3I)\le-3$: at least one principal direction contracts with acceleration $\le-3$. The sign of the Riccati convention is internally consistent, since its trace reproduces $\operatorname{Ric}_g(N,N)=-\operatorname{tr}S'-|S|^2$.

### (iii) The quantitative $\lambda_{\min}(S'(0))\le-3+5\delta$ under $|E|_{\rm op}\le\delta$

Set $e:=R_q+6$. With $\operatorname{Ric}_g=E-3g$ and $S(0)=0$:
$$R_q=R_g-2\operatorname{Ric}_g(N,N)=(\operatorname{tr}_gE-12)-2(E_{nn}-3)=\operatorname{tr}_TE-E_{nn}-6,$$
so $e=\operatorname{tr}_TE-E_{nn}$, and with three tangential eigenvalues plus one normal, $|e|\le3\delta+\delta=4\delta$. **Confirmed (3.8).**

At a downward zero of $h$: $\tfrac12|A|^2=K_{\rm orb}=3-\tfrac e2-h'\ge3-\tfrac e2$ (**3.9**). The 3D identity now gives $(\operatorname{Ric}_q+3q)(v,v)=\tfrac e2-K_{\rm orb}\le e-3\le-3+4\delta$ (**3.10**). The defect Gauss relation is
$$S'(0)=\operatorname{Ric}_q^\sharp+3I-E_T^\sharp \quad(\textbf{3.11}),$$
so with $|E_T(v,v)|\le\delta$,
$$\langle S'(0)v,v\rangle=(\operatorname{Ric}_q+3q)(v,v)-E_T(v,v)\le(e-3)+\delta\le5\delta-3.$$
Since $S'(0)$ is self-adjoint, $\lambda_{\min}(S'(0))\le5\delta-3$. **Confirmed (3.12).** The constant is exactly $4\delta$ from the scalar trace plus $\delta$ from the tangential component of $E$ along $v$; every sign is as printed. The JSON chain (`Pupper=e-3`, `Sprime_upper=e-3+delta`, substitute $e=4\delta$) reproduces this.

Conditions used: center slice in the $T^2$-cohomogeneity-one form (3.1); reflection symmetry giving $S(0)=0$ exactly; pointwise operator bound $|E|_{\rm op}\le\delta$. These are exact given those conditions.

### (iv) Finite-cylinder anisotropy integration and the $R_q=-6$ impossibility

For $g=e^{2\phi}(dt^2+dz^2)+e^{2b}dx^2+e^{2c}dy^2$, forming $R_{xx}/g_{xx}-R_{yy}/g_{yy}$ produces the divergence combination $-e^{-2\phi}e^{-\sigma}\operatorname{div}_{t,z}(e^\sigma\nabla d)$ with $\sigma=b+c$, $d=b-c$. The $-3g$ terms enter each of $R_{xx}/g_{xx}$ and $R_{yy}/g_{yy}$ as the same constant $-3$ and cancel in the difference; hence exact $\operatorname{Ric}=-3g$ gives $\operatorname{div}_{t,z}(e^\sigma\nabla d)=0$. **Confirmed (2.2)** (this is the orthogonally-transitive $T^2$ Ernst/Gowdy-type reduction; the cosmological term drops out of the anisotropy equation). This is exact only for the diagonal orthogonally-transitive subclass in conformal base gauge, not for general $T^2$-invariant metrics — the note states this.

Integrate $d\cdot\operatorname{div}(e^\sigma\nabla d)$ over $[0,R]_t\times S^1_z$. Reflection at $t=0$ gives $\partial_t d=0$; an exit face umbilic in the orbit directions ($\partial_t b=\partial_t c$) gives $\partial_t d=0$ at $t=R$; $z$-periodicity removes the remaining face terms. So $\int e^\sigma|\nabla d|^2=0$ and $d\equiv d_0$. **Confirmed (2.3).**

Center slice then is $q=e^{2\phi(z)}dz^2+e^{\sigma+d_0}dx^2+e^{\sigma-d_0}dy^2$; the substitution $d\tau=e^{\phi-\sigma/2}dz$ gives $q=e^{\sigma}\bigl(d\tau^2+e^{d_0}dx^2+e^{-d_0}dy^2\bigr)$, i.e. $q$ is conformal to a fixed flat $T^3$ metric with $u=e^{\sigma/4}$, $q=u^4q_{\rm flat}$. **Confirmed (2.4).** In 3D, $R_q=u^{-5}(-8\Delta_{\rm flat}u+R_{\rm flat}u)$ with $R_{\rm flat}=0$; $R_q=-6$ forces $-8\Delta u=-6u^5$ (**2.5**), whose integral over $T^3$ gives $0=\int(-6u^5)<0$. Impossible. **Confirmed.**

This is an exact nonexistence for the *exact* configuration (exact $\operatorname{Ric}=-3g$, reflection center, and exactly-equal orbit normal derivatives at the outer face). It is the standard vanishing of the flat-torus Yamabe number reappearing through $d=$const. The note is correct that it does not touch small-defect cores, and that a viable interface must retain nonzero $d_n(R)$ — the exact $d_n=0$ is precisely what removes the anisotropy transport.

### (v) Normal weighted identity and the physical-length inequality

With $b=H-3$, $B=S-I$, $E_{rr}=E(N,N)=\operatorname{Ric}_g(N,N)+3=(-H'-|S|^2)+3$, and $|S-I|^2=|S|^2-2H+3$:
$$b'+2b+|B|^2=H'+(2H-6)+(|S|^2-2H+3)=H'+|S|^2-3=-E_{rr}.$$
**Confirmed (1.5).** Multiplying by $e^{2r}$: $(e^{2r}(H-3))'=-e^{2r}(|S-I|^2+E_{rr})$, matching the JSON identity and the symbolic residual $=0$.

At a reflection center $H(0)=0$, so $b(0)=-3$. Integrating with $\eta=3-H(R)=-b(R)$:
$$e^{2R}\eta=3+\int_0^R e^{2r}\bigl(|S-I|^2+E_{rr}\bigr)dr.\quad(\textbf{1.6})$$
Under $|E|_{\rm op}\le\delta$, $E_{rr}\ge-\delta$, so $\int e^{2r}E_{rr}\ge-\tfrac\delta2(e^{2R}-1)$ and
$$e^{2R}\eta+\tfrac\delta2(e^{2R}-1)\ge3+\int_0^R e^{2r}|S-I|^2\,dr\ge3.\quad(\textbf{1.7})$$
**Confirmed exactly.** The consequence is exactly as stated: as $\delta,\eta\to0$ the physical Gaussian distance $R$ must grow, $R\gtrsim\tfrac12\log\frac{3}{\eta+\delta/2}$. The essential caution is real and correctly flagged: $r$ here is arc length in the $dr^2$ Gaussian gauge; substituting a conformal coordinate length would invalidate the $e^{2r}$ weighting.

### Linear mode (1.1)–(1.4) and Yamabe seed (4.2), checked in passing

- $x=ke^{-t}$ maps $\psi''+3\psi'-k^2e^{-2t}\psi=0$ to $x^2\psi_{xx}-2x\psi_x-x^2\psi=0$; the closed form (1.2) satisfies $\psi(k)=1$, $\psi_x(k)=0$, and $\psi(x\to0)=\tfrac{e^k-e^{-k}}{2k}=\tfrac{\sinh k}{k}$. The amplification factors $1.1752,1.8134,3.3393,14.84,186.31$ for $k=1,2,3,5,8$ all reproduce $\sinh k/k$. Self-adjoint form $(e^{3t}\psi')'=k^2e^t\psi$ is correct (weight $e^{3t}$ = three fiber factors). The conclusion that fixed-mode Neumann–Dirichlet uniqueness does not give frequency-uniform inversion follows from this growth. Sound.
- For $h_f=dz^2+e^{2f}dx^2+e^{-2f}dy^2$: $A=\operatorname{diag}(f',-f')$, $h=0$, $R_{h_f}=-2f'^2$; with $\det h_f=1$, $\Delta_{h_f}u=u''$, giving $-8u''-2f'^2u=-6u^5$, i.e. $u''=\tfrac34u^5-\tfrac14 f'^2u$. **Confirmed (4.2)**; the sign is the one used, and the note's flag that a prior run used the opposite sign is consistent. The numerical max sectional curvatures $\to3.03$ from above corroborate the sharp lower bound $3$ from the center theorem rather than contradicting it.

---

### Summary of what is exact versus condition-dependent

- **Exact, structural (no extra input beyond smoothness):** the identities (3.3), (3.6)–(3.8), (3.10)–(3.11), (1.5)–(1.7), (2.2)–(2.5), (4.2). The trace and sign bookkeeping in (3.8), (3.12) and the $5\delta$ constant are exact.
- **Requires the $T^2$-cohomogeneity-one center form (3.1):** the downward-zero curvature statement and the eigenvalue $\le-3$ conclusion (i)–(iii). Outside this symmetry class the mean-zero/downward-zero mechanism does not by itself deliver a forced orbit-plane curvature.
- **Requires diagonal orthogonal-transitivity + conformal base gauge:** the anisotropy divergence (2.2) and the finite-cylinder rigidity (iv). The impossibility in (iv) additionally requires the *exact* equal-orbit-normal-derivative condition at the outer face and $z$-periodicity; it is a statement about that exact configuration only.
- **Requires reflection symmetry** ($S(0)=0$) for (ii)–(iii) and for $b(0)=-3$ in (v), and the physical Gaussian gauge for the $e^{2r}$ weighting in (v).

No formula needs correction. The one interpretive point worth keeping visible: results (iv) and the center theorem are exact statements inside the stated symmetry class and exact-outer-face configuration; the note's own reading — that they redirect the construction toward a nonzero weighted flux $d_n(R)$ and a growing physical length rather than excluding small-defect cores — is the correct reading of what these identities do and do not establish.
# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step30_route_reassessment_noncollapsed_bubble_variational.md",
    "Sessions/S0910A02/workspace/data/step30_noncollapsed_bubble_variational_audit.json",
    "Sessions/S0910A02/workspace/notes/step7_positive_branch_four_constructions.md",
    "Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md",
    "Sessions/S0910A02/workspace/notes/step29_positive_allocation_and_twist_spike_execute.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md"
  ]
}
```

## Task

Independently verify the Step-30 route reassessment for Yau Problem 26. The key proposed direction is the four-dimensional positive noncollapsed bubble route: if the Cheeger--Naber bad set is empty, smooth Einstein existence on the same manifold follows; if singularities occur, use a variational Pohozaev/Komar projection for merely C^0 Ricci-pinched metrics to recover the Ozuch/Biquard Eguchi--Hanson first obstruction R_+ v=0, without assuming exact Einstein weighted normal form. Read the supplied notes and source excerpts/files. Assess target fidelity, mathematical correctness of the noncollapsed reduction, source-scope limits, whether the divergence-free Einstein-tensor identity is the right C^0-safe bulk pairing, whether first-obstruction vanishing plausibly leads toward actual Einstein existence, and the most serious gaps or likely false assumptions.

## Output

# Scientific verification memo

## 1. Fidelity to Yau Problem 26

Step 30 keeps the original quantifiers visible and correctly treats the four-dimensional positive, noncollapsed regime as only one component of the full problem. Establishing this regime would not by itself handle positive collapse, dimensions \(n\ge 5\), or the branch centered at \(-g\). The original class also includes nonorientable manifolds; the local \(\Lambda^2_\pm\) analysis still makes sense after choosing a local orientation, but an Einstein metric constructed on an oriented cover need not descend without equivariance.

The same-sign normalization is mathematically correct. If \(0<c<C\), rescaling the metric turns
\[
cg\leq \operatorname{Ric}_g\leq Cg
\]
into
\[
\|\operatorname{Ric}_{\tilde g}-\tilde g\|_{\mathrm{op}}\leq
\frac{C-c}{C+c}.
\]
The analogous normalization applies to an interval lying strictly below zero.

## 2. The regular noncollapsed alternative

Let
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op}}\leq\delta_i\to0,
\qquad \operatorname{Vol}(M_i,g_i)\geq v_0>0.
\]
For large \(i\),
\[
\operatorname{Ric}_{g_i}\geq (1-\delta_i)g_i.
\]
Myers gives
\[
\operatorname{diam}(M_i,g_i)\leq
\pi\sqrt{\frac{3}{1-\delta_i}}.
\]
Bishop–Gromov, applied with \(B_D(p)=M_i\), then gives a uniform lower volume ratio on every fixed radius:
\[
\operatorname{Vol} B_r(p)
\geq
\frac{V_{k_i}(r)}{V_{k_i}(D)}
\operatorname{Vol}(M_i),
\qquad k_i=\frac{1-\delta_i}{3}.
\]
Thus total noncollapse implies local noncollapse in this positive normalized setting.

On harmonic-coordinate regions with uniform harmonic radius, one has subsequential
\[
C^{1,\alpha}\cap W^{2,p}
\]
convergence. Writing
\[
A_i:=\operatorname{Ric}_{g_i}-g_i,\qquad \|A_i\|_{L^\infty}\to0,
\]
the harmonic-coordinate Ricci equation passes to the limit distributionally. The limit metric satisfies
\[
\operatorname{Ric}_{g_\infty}=g_\infty.
\]
Elliptic bootstrapping then makes \(g_\infty\) smooth.

If “the bad set is empty” means that a uniform harmonic-radius lower bound holds throughout \(M_i\), then compact harmonic-chart convergence gives eventual diffeomorphisms
\[
F_i:M_\infty\longrightarrow M_i.
\]
The pulled-forward metric \((F_i^{-1})^*g_\infty\) is Einstein on \(M_i\). This part does answer the same-smooth-manifold requirement.

One correction is needed: the supplied hypotheses do **not** give smooth convergence of the input metrics \(g_i\). Their Ricci defects are controlled only in \(L^\infty\), with no derivative estimates. The available convergence is \(C^{1,\alpha}\cap W^{2,p}\); that regularity is already enough for diffeomorphism recovery when the harmonic radius is uniform. Also, smoothness of the metric-space limit alone is weaker than absence of harmonic-radius concentration, since microscopic concentration can in principle disappear at a regular limit point.

## 3. The singular reduction is not yet a verified finite ALE tree theorem

The supplied Ozuch compactness and weighted-coordinate theorems concern **exact Einstein sequences**. In particular:

- `Noncollapsed degeneration ... I`, Theorem 0.1, assumes each \(g_i\) is Einstein and obtains an Einstein orbifold plus Ricci-flat ALE blowups.
- Theorem 0.2 places an exact Einstein metric sufficiently GH-close to an orbifold into a weighted gluing description.
- Theorem 6.1 derives the scale-sensitive neck estimate from the exact Einstein equation.

For a sequence with only
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{L^\infty}\to0,
\]
Cheeger–Naber supplies \(L^2\)-curvature control and quantitative regularity information, but the supplied material does not establish all of the following together:

1. finitely many concentration points;
2. energy identity with no unmodeled neck concentration;
3. smooth complete Ricci-flat ALE blowups at every concentration scale;
4. a finite bubble tree carrying the topology of \(M_i\);
5. weighted \(C^2\) expansions relating the orbifold \(H_2\) term and ALE \(H^4\) term.

This is more than the absence of Ozuch’s optimal weighted normal form. The ALE/tree description itself still needs an approximate-Einstein compactness theorem. The earlier Calderón–Zygmund spike discussion is directly relevant: an \(L^\infty\) Ricci defect does not control the full Hessian of the metric pointwise, so high Weyl curvature can occur on very small sets without the exact Einstein curvature equation used in Bando–Kasue–Nakajima and Ozuch.

Consequently, the sentence that the singular regime has already become “a finite bubble/orbifold question” is stronger than the supplied theorems justify. It becomes correct after adding an ALE bubble-tree theorem for these \(L^\infty\)-pinched sequences.

## 4. The cosmological Einstein tensor identity is correct and genuinely useful

For the positive normalization define
\[
\mathcal E_g
=
\operatorname{Ric}_g-\frac12s_g g+\frac{n-2}{2}g.
\]
If
\[
A=\operatorname{Ric}_g-g,
\]
then
\[
\boxed{\mathcal E_g=A-\frac12(\operatorname{tr}_gA)g.}
\]
Hence \(\mathcal E_g=0\) when \(\operatorname{Ric}_g=g\), and the contracted Bianchi identity gives
\[
\delta_g\mathcal E_g=0.
\]

If the eigenvalues of \(A\) lie in \([-\delta,\delta]\), the eigenvalues of \(\mathcal E_g\) satisfy
\[
\left|a_i-\frac12\sum_j a_j\right|
=
\frac12\left|a_i-\sum_{j\ne i}a_j\right|
\leq \frac n2\delta.
\]
Therefore
\[
|\mathcal E_g|_{\mathrm{HS}}\leq \frac{n^{3/2}}2\delta.
\]

Ozuch’s Lemma 1.4 then gives, for every smooth vector field \(Z\),
\[
\boxed{
\int_{\partial\Omega}\mathcal E_g(Z,\nu)
=
\frac12\int_\Omega
\langle\mathcal E_g,\mathcal L_Zg\rangle\,d\mu_g.
}
\]
In particular, with
\[
J(Z)=\int_\Omega|\mathcal L_Zg|^2\,d\mu_g,
\]
one has
\[
\left|
\int_{\partial\Omega}\mathcal E_g(Z,\nu)
\right|
\leq
\frac{n^{3/2}}4\,
\delta\,\operatorname{Vol}(\Omega)^{1/2}J(Z)^{1/2}.
\]
In dimension four this becomes the clean estimate
\[
\boxed{
\left|
\int_{\partial\Omega}\mathcal E_g(Z,\nu)
\right|
\leq
2\delta\,\operatorname{Vol}(\Omega)^{1/2}J(Z)^{1/2}.
}
\]

This is the correct pairing for avoiding derivatives of the Ricci defect. The Euler–Lagrange equation
\[
\delta_g\delta_g^*Z=0
\]
also follows correctly from \(J(Z)=4\int|\delta_g^*Z|^2\) when the traces of \(Z\) on the two hypersurfaces are fixed.

What this identity does not supply by itself is the asymptotic coefficient
\[
\operatorname{Ric}^{(2)}_e(H_2,H^4).
\]
Recovering that coefficient still requires scale-sensitive comparison between the actual metric and the two model expansions.

## 5. Eguchi–Hanson algebra and source applicability

The Eguchi–Hanson expansion in Step 30 is correct. With \(x=r^{-4}\), the four relative metric coefficients are
\[
A,A,B,B,\qquad
A=(1+x)^{-1/2},\quad B=(1+x)^{1/2}.
\]
Their first-order trace is
\[
-\frac12-\frac12+\frac12+\frac12=0.
\]
Indeed \(A^2B^2=1\), so the volume ratio is exactly one in these coordinates, not merely one to first order. This agrees with Ozuch’s volume gauge and explains why a scalar mass-type quantity does not detect the anisotropic \(H^4\) term.

The first-obstruction algebra is also correctly stated. Ozuch 2021, Theorem 4.6 and Corollary 4.10, give for
\[
H^4=-\frac{\theta_1^-\circ\omega_1^+}{2r^4}
\]
the equivalence
\[
\boxed{
R_e^{+,(1)}(H_2)\,\omega_1^+=0.
}
\]
Thus for a fixed Eguchi–Hanson orientation \(v\),
\[
R_+v=0.
\]
Only after allowing the orientation to vary does this become
\[
\det R_+=0.
\]
The examples \(R_+=(1/3)I\) for round \(S^4\) and \(R_+=\operatorname{diag}(1,0,0)\) for the normalized Kähler–Einstein models are consistent.

The arithmetic
\[
\eta^2r^4\ll t^4
\quad\Longleftrightarrow\quad
\eta\ll\frac{t^2}{r^2}
\]
is correct for the stated model. It remains a model assumption rather than a consequence of the variational equation. The notation should also distinguish bubble **length** \(t\) from Ozuch’s metric gluing parameter \(\tau\): in the usual coordinates the \(H^4\) contribution is of order \(\tau^2\), corresponding to \(t^4\) when \(t=\sqrt{\tau}\).

## 6. The variational field does not automatically produce the needed weighted rate

Minimizing \(J\) gives the smallest symmetrized-gradient energy among fields with prescribed traces, but
\[
J(Z_{\min})\leq J(Z_{\mathrm{competitor}})
\]
does not by itself improve the scale dependence of the competitor. A proof still needs a Korn-type estimate uniform on the long cone/Eguchi–Hanson annulus and an energy bound small enough relative to the \(H^4\) signal.

There is also an important distinction between the model fields:

- Cone rotations are Killing, so \(J\) is the natural functional.
- \(r\partial_r\) is conformal Killing:
  \[
  \mathcal L_{r\partial_r}e=2e.
  \]
  Thus its full \(J\)-energy is already of order \(r^4\) on a flat annulus. Ozuch Proposition 4.1 instead uses
  \[
  (\mathcal L_Xg_b)^\circ,
  \]
  the trace-free deformation associated with the harmonic radial extension. A radial variational problem based on
  \[
  \int|(\mathcal L_Zg)^\circ|^2
  \]
  together with a fixed dilation normalization aligns more closely with the source construction.

Most importantly, Ozuch’s obstruction is obtained by expanding the exact Einstein equation in a region where both \(H_2\) and the scaled \(H^4\) term are visible. Even for an exact Einstein metric the actual tensor \(\mathcal E_g\) is identically zero; the obstruction arises from the coefficient of this zero after a weighted expansion. A small-flux identity alone cannot identify that coefficient unless the remainder is controlled after division by the bubble scale. Variational minimization may help obtain such control, but no estimate in the supplied notes establishes it.

## 7. First-obstruction vanishing is far from Einstein existence

The supplied sources make \(R_+v=0\) a necessary local condition for an exact Einstein Eguchi–Hanson degeneration. They do not give a general compact gluing theorem saying that this condition produces an Einstein metric on the resolution:

- Biquard’s existence theorem cited in the source is for a nondegenerate asymptotically hyperbolic setting with a simple singularity.
- Ozuch’s Theorem 0.2 describes exact Einstein metrics already known to exist and already GH-close to the orbifold.
- Ozuch 2021 explicitly records higher-order obstructions.
- Multiple singularities, relative scales, global infinitesimal Einstein modes, and topology identification remain separate analytic objects.

There is also a scaling mechanism showing why \(C^0\) pinching may detect only the first local obstruction. Suppose the first condition permits a local correction \(h_2\) satisfying schematically
\[
\operatorname{Ric}'_{g_b}(h_2)=\lambda g_b.
\]
On the ALE core set
\[
G_\varepsilon=\varepsilon(g_b+\varepsilon h_2).
\]
Since Ricci is unchanged as a covariant tensor under constant metric scaling,
\[
\operatorname{Ric}(G_\varepsilon)-\lambda G_\varepsilon
=O(\varepsilon^2)
\]
as a covariant tensor, hence
\[
\left\|
\operatorname{Ric}(G_\varepsilon)-\lambda G_\varepsilon
\right\|_{\mathrm{op},G_\varepsilon}
=O(\varepsilon).
\]
A second-order cokernel component can therefore obstruct an exact solution while the operator Ricci defect still tends to zero. This scaling points against the idea that every higher-order obstruction must create a scale-independent \(C^0\) defect. It also explains why first-obstruction vanishing may be more naturally associated with constructing strongly pinched approximate metrics than with obtaining an exact Einstein metric.

## 8. Overall assessment

Three components of Step 30 are solid and reusable:

1. the regular noncollapsed alternative, interpreted through uniform harmonic radius rather than smooth convergence of \(g_i\);
2. the divergence-free cosmological Einstein tensor and its explicit \(L^\infty\)-to-flux estimate;
3. the Eguchi–Hanson identity \(R_+v=0\) and the distinction between fixed orientation and \(\det R_+=0\).

The major unresolved mathematical content is the passage
\[
C^0\text{ Ricci pinching}
\;\Longrightarrow\;
\text{weighted orbifold/ALE overlap with scale-controlled test fields}.
\]
The supplied exact-Einstein sources do not provide that passage. Even if it is established and forces \(R_+v=0\), a further theorem controlling all higher and global obstructions is needed before an Einstein metric on the original smooth resolution follows.
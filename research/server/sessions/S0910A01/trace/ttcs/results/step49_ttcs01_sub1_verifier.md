# TTCS Independent Branch Record

```json
{
  "step_id": 49,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step49_qg_smoothing_einstein_existence_mechanism.md",
    "Sessions/S0910A01/workspace/scripts/step49_tangent_euler_and_qg_obstruction.py"
  ]
}
```

## Task

Verify the following chain of reasoning about Einstein metric existence on product-quotient surface resolutions, checking each link for mathematical correctness:

1. HYPERKÄHLER IDENTIFICATION: For the A_1 singularity {uv-w^2=0}, the hyperkähler family of ALE metrics on the resolution T*CP^1 has three real parameters (ζ_1, ζ_2, ζ_3). The ζ_1 direction corresponds to the size of the exceptional CP^1 (Kähler/resolution direction); the (ζ_2, ζ_3) directions correspond to the complex smoothing {uv-w^2=t}. On a product Kähler-Einstein orbifold (Σ_1×Σ_2)/G with Ric=Λg, the curvature operator has R_+=diag(Λ,0,0) with the nonzero eigenvalue in the Kähler form direction and the kernel in the (2,0)+(0,2) directions. Therefore the kernel-directed Eguchi-Hanson replacement (which kills the first Ozuch obstruction) corresponds to a complex smoothing of each A_1 node, not a holomorphic resolution.

2. GLOBAL QG SMOOTHING: For a canonical model Z of a surface of general type with only rational double points (A_1 singularities), a global Q-Gorenstein smoothing exists if H^2(T_Z^0) = 0. By the Burns-Wahl result for RDPs, this equals H^2(T_S) where S is the minimal resolution. By Serre duality, H^2(T_S) = H^0(Ω^1_S ⊗ K_S). The sufficient condition fails (i.e., H^2 > 0) when χ(T_S) = 2K^2-10 > 0, which occurs for K^2 ≥ 6.

3. AMPLENESS PERSISTENCE: If the canonical model Z has a QG smoothing π:Z→Δ with K_{Z/Δ} Q-Cartier, and K_{Z_0} is ample, then K_{Z_t} is ample for small t≠0.

4. AUBIN-YAU: A smooth projective surface with ample canonical bundle carries a unique negative Kähler-Einstein metric with Ric(ω)=-ω.

5. SIMULTANEOUS RESOLUTION: For a flat family of surfaces with ADE singularities, after a finite Weyl-group base change, the family admits a simultaneous resolution. For A_1, this is a Z/2Z base change. The resolved family is smooth, so all fibers are diffeomorphic. The central fiber is the minimal resolution S.

6. CONCLUSION: S is diffeomorphic to Z_t, which carries a KE metric, so the smooth 4-manifold underlying S carries an Einstein metric.

Check each link for correctness. Are there hidden assumptions, missing hypotheses, or known counterexamples to any step?

## Output

# Scientific verification memo

## Overall mathematical status

Links 2–6 give a valid conditional theorem:

> If the projective canonical model \(Z\) with only \(A_1\) singularities admits a proper global \(\mathbb Q\)-Gorenstein smoothing with smooth general fiber, then its minimal resolution \(S\) is diffeomorphic to that general fiber and therefore carries an Einstein metric with Einstein constant \(-1\).

Link 1 has the correct qualitative geometry, but its parameter formula and its connection to global deformation theory need two important corrections. In particular, the local hyperkähler interpretation does not itself produce a global \(\mathbb Q\)-Gorenstein smoothing.

---

## 1. Hyperkähler identification

### Curvature computation

Fix the complex orientation of the product Kähler surface. For any Kähler–Einstein four-manifold with
\[
\operatorname{Ric}=\Lambda g,\qquad s=4\Lambda,
\]
the self-dual Weyl operator has eigenvalues
\[
W_+=\operatorname{diag}\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right)
\]
on
\[
\Lambda^+=\mathbb R\omega\oplus \Lambda_{\mathbb R}^{2,0}.
\]
Since the curvature block is
\[
\mathcal R_+=W_++\frac{s}{12}I,
\]
one obtains
\[
\mathcal R_+=\operatorname{diag}(\Lambda,0,0).
\]
Thus
\[
\ker \mathcal R_+=\Lambda_{\mathbb R}^{2,0}
 =\operatorname{span}_{\mathbb R}\{\Re\Omega,\Im\Omega\}
\]
pointwise. This calculation is correct for the product metric when the two curve factors have the same Einstein constant. It descends through the finite quotient.

### Kronheimer parameters

For the marked \(A_1\) ALE family, write
\[
\zeta_{\mathbb R}=\zeta_1,\qquad
\zeta_{\mathbb C}=\zeta_2+i\zeta_3.
\]
Relative to a fixed complex structure \(I\):

- \(\zeta_{\mathbb C}=0\), \(\zeta_{\mathbb R}\ne0\) gives the holomorphic resolution, with the exceptional sphere having nonzero Kähler period.
- \(\zeta_{\mathbb C}\ne0\) gives the smooth complex deformation of the node.

There is, however, a Weyl-group squaring that is missing from the note. The \(A_1\) Weyl group acts by
\[
\zeta_{\mathbb C}\longmapsto-\zeta_{\mathbb C},
\]
so the coordinate on the semiuniversal deformation base is an invariant quadratic coordinate. In suitable coordinates,
\[
uv-w^2=c\,\zeta_{\mathbb C}^{\,2}
\]
for a nonzero normalization constant \(c\), rather than \(t=\zeta_{\mathbb C}\). Thus \(\zeta_{\mathbb C}\) is a coordinate on the Weyl cover, while \(t\) is the ordinary smoothing parameter. This is precisely the same double cover that appears in simultaneous resolution.

Also, the direction of \(\zeta\) belongs to a marked hyperkähler triple and an asymptotic framing. As an unmarked Riemannian metric, Eguchi–Hanson essentially has only a scale parameter; rotating \(\zeta\) rotates the hyperkähler identification.

### Relation to the Einstein gluing obstruction

Under the usual orientation convention, the leading \(A_1\) Einstein desingularization equation takes the form
\[
\mathcal R_+(p)\zeta=0
\]
or an equivalent framed formulation. In that convention, choosing \(\zeta\in\ker\mathcal R_+\) selects \(\zeta_{\mathbb C}\ne0\), hence the smoothing complex structure relative to the ambient Kähler structure.

Two qualifications are mathematically essential:

1. With the opposite ALE chirality, the relevant curvature block is \(\mathcal R_-\), not \(\mathcal R_+\).
2. A Riemannian approximate gluing need not define an integrable complex deformation. The parameter match is local and marked. Global \(\mathbb Q\)-Gorenstein deformation requires a compatible element of the global deformation space and its integration to an actual family.

Thus the local identification is correct after replacing \(t=\zeta_{\mathbb C}\) by \(t\propto\zeta_{\mathbb C}^2\), but it does not make global Einstein gluing and global \(\mathbb Q\)-Gorenstein smoothability equivalent problems.

---

## 2. Global \(\mathbb Q\)-Gorenstein smoothing and \(H^2\)

Let
\[
\mathcal T_Z^0=\mathcal Hom(\Omega_Z,\mathcal O_Z),\qquad
\mathcal T_Z^1=\mathcal Ext^1(\Omega_Z,\mathcal O_Z).
\]
For isolated \(A_1\) points, every local singularity has a one-dimensional, unobstructed Gorenstein smoothing. The local-to-global sequence contains
\[
\operatorname{Ext}^1(\Omega_Z,\mathcal O_Z)
 \longrightarrow H^0(\mathcal T_Z^1)
 \longrightarrow H^2(\mathcal T_Z^0).
\]
Therefore \(H^2(\mathcal T_Z^0)=0\) gives surjectivity onto all local smoothing directions. Together with the standard deformation theorem for locally unobstructed quotient singularities, this permits a global deformation simultaneously smoothing all nodes. Since \(A_1\) is Gorenstein and lci, these local smoothings are \(\mathbb Q\)-Gorenstein.

For a compact complex surface with rational double points and its minimal crepant resolution
\[
\rho:S\to Z,
\]
the Burns–Wahl comparison gives
\[
H^2(Z,\mathcal T_Z^0)\cong H^2(S,T_S).
\]
If the logarithmic tangent sheaf \(T_S(-\log E)\) is used instead, its comparison with \(\mathcal T_Z^0\) and \(T_S\) requires the corresponding Burns–Wahl result; it is not merely a formal consequence of
\[
0\to T_S(-\log E)\to T_S\to \bigoplus_i N_{E_i/S}\to0.
\]

Serre duality gives a duality, not a literal canonical equality:
\[
H^2(S,T_S)^\vee
 \cong H^0(S,\Omega_S^1\otimes K_S).
\]
Their dimensions agree, and one vanishes exactly when the other does.

### Riemann–Roch computation

For a smooth surface,
\[
\chi(T_S)=\frac{1}{6}(7K_S^2-5c_2(S)).
\]
Using Noether’s formula
\[
c_2(S)=12\chi(\mathcal O_S)-K_S^2
\]
gives
\[
\chi(T_S)=2K_S^2-10\chi(\mathcal O_S).
\]
Hence the formula
\[
\chi(T_S)=2K^2-10
\]
uses the additional hypothesis
\[
p_g=q=0,\qquad \chi(\mathcal O_S)=1.
\]

For a surface of general type over \(\mathbb C\), \(H^0(T_S)=0\). Therefore
\[
h^2(T_S)-h^1(T_S)=2K^2-10.
\]
Consequently, when \(K^2\ge6\),
\[
h^2(T_S)\ge 2K^2-10>0.
\]
So the vanishing theorem cannot be applied in these cases. This does **not** imply that \(Z\) has no global smoothing; \(H^2=0\) is a sufficient hypothesis, not a necessary one.

For \(K^2=2,4\), the Euler characteristic calculation only shows numerical compatibility with \(H^2(T_S)=0\). It does not establish that vanishing for any named family. The supplied script verifies the arithmetic but performs no cohomology computation.

Also, \(h^1(T_S)\) is the tangent dimension for deformations of the smooth resolution. It should not be identified directly with the dimension of the global \(\mathbb Q\)-Gorenstein deformation space of \(Z\), because local \(T^1\)-terms and the ramified Burns–Wahl map intervene.

---

## 3. Persistence of ampleness

This link is correct under the standard meaning of a global \(\mathbb Q\)-Gorenstein smoothing.

Required hypotheses are:

- \(\pi:\mathcal Z\to\Delta\) is proper and flat;
- the fibers are normal, with smooth general fiber;
- a fixed reflexive power
  \[
  L=\omega_{\mathcal Z/\Delta}^{[m]}
  \]
  is a line bundle near the central fiber and is compatible with restriction to fibers.

Then
\[
L|_{Z_0}\cong mK_{Z_0}.
\]
Since \(K_{Z_0}\) is ample, \(L|_{Z_0}\) is ample. Openness of ampleness for a line bundle in a proper flat family implies, after shrinking \(\Delta\), that
\[
L|_{Z_t}\cong mK_{Z_t}
\]
is ample for all nearby \(t\). Hence \(K_{Z_t}\) is ample.

A merely local smoothing germ around each singular point would not supply this step; properness and a global relative canonical power are essential.

---

## 4. Aubin–Yau

This link is correct. A smooth compact complex surface with ample \(K_{Z_t}\) is projective and has
\[
c_1(Z_t)<0.
\]
Aubin–Yau produces a Kähler metric satisfying
\[
\operatorname{Ric}(\omega_t)=-\omega_t
\]
after the usual normalization. Since this equation determines the Kähler class,
\[
[\omega_t]=2\pi c_1(K_{Z_t}),
\]
the solution is unique among Kähler metrics.

The uniqueness is not needed for the topological conclusion; existence is enough.

---

## 5. Simultaneous resolution

The local ADE statement is correct. A deformation of an ADE singularity is pulled back from its semiuniversal deformation. Pulling back along the Cartan/Weyl cover
\[
\mathfrak h\longrightarrow \mathfrak h/W
\]
produces a simultaneous resolution.

For one \(A_1\) singularity,
\[
W\cong \mathbb Z/2\mathbb Z,
\]
and the cover is the square-root cover discussed above. For \(r\) independently parameterized \(A_1\) points, the full multi-parameter Weyl group is
\[
(\mathbb Z/2\mathbb Z)^r.
\]
Along a single analytic disc, however, adjoining square roots of all local functions requires degree at most two after normalization, because every local smoothing function has the form
\[
f_i(t)=t^{m_i}u_i(t)
\]
with \(u_i\) an analytic unit having an analytic square root. Thus a common double cover is sufficient for a one-parameter smoothing, though the full semiuniversal cover has degree \(2^r\).

Globally, the simultaneous resolution may naturally exist as a complex-analytic family or algebraic space rather than as a projective scheme. For the diffeomorphism argument it is enough that
\[
\widetilde{\mathcal Z}\to\Delta'
\]
is a proper smooth morphism of complex manifolds or its equivalent analytic realization. Then Ehresmann’s theorem gives diffeomorphic fibers.

By definition of simultaneous resolution:

- the central fiber is the minimal resolution \(S\);
- over a smooth general fiber, the resolving morphism is an isomorphism.

Therefore
\[
S\cong_{\mathrm{diff}} Z_t.
\]

---

## 6. Transfer of the Einstein metric

Let
\[
F:S\longrightarrow Z_t
\]
be the diffeomorphism furnished above, and let \(g_t\) be the Aubin–Yau metric. Then
\[
h=F^*g_t
\]
is a smooth Riemannian metric on the underlying manifold of \(S\), and naturality of Ricci curvature gives
\[
\operatorname{Ric}_h
 =F^*(\operatorname{Ric}_{g_t})
 =F^*(-g_t)
 =-h.
\]
Thus the conclusion is fully valid.

The metric \(h\) need not be Kähler for the original complex structure on \(S\). This is expected: \(K_S\) has zero intersection with the exceptional \((-2)\)-curves and is not ample, while \(Z_t\) carries a different complex structure with ample canonical bundle. The research problem only asks for a Riemannian Einstein metric on the smooth manifold.

---

## Additional artifact-level observations

1. The Python script correctly verifies
   \[
   \chi(T_S)=2K^2-10,\qquad b_+=1
   \]
   for the entered \(p_g=q=0\) rows. It does not calculate \(H^2(T_S)\), global deformation maps, or the Ozuch obstruction tensor.

2. The sentence in the note that the local near-Einstein construction “is” the global smoothability question is too strong mathematically. The former is a framed metric PDE construction; the latter is governed by
   \[
   \operatorname{Ext}^1(\Omega_Z,\mathcal O_Z)
   \to \bigoplus_i T^1_{p_i}
   \to H^2(\mathcal T_Z^0)
   \]
   and nonlinear deformation theory.

3. The quoted assertion that standard Milnor fibers are symplectomorphic to standard Kähler minimal resolutions needs substantial qualification. The usual Milnor-fiber symplectic form is exact, whereas a Kähler form on the resolution has positive integral over the exceptional sphere. Those two standard symplectic structures therefore cannot be symplectomorphic. For \(A_1\), the required diffeomorphism follows cleanly from simultaneous resolution; no symplectic equivalence is needed.

4. The supplied note contains citation keys but not exact source passages for the Burns–Wahl cohomology comparison or the global simultaneous-resolution formulation. The mathematical statements above are the precise forms needed in the proof.

In summary, the Einstein-existence theorem from a proper global \(\mathbb Q\)-Gorenstein smoothing is mathematically sound. What remains unresolved for the listed product-quotient families is the actual existence of such a global smoothing; neither the Euler-characteristic script nor the local hyperkähler parameter match establishes that input.
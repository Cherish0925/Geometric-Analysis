# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 75,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step75_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step75_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the two proposed consequences in spirit_step74_attainment_and_root_lattice.md against the full Step-74 theorem. First, check the variational argument that an attained orbifold P floor forces an attained scalar-energy floor, then constant scalar curvature and Einsteinity; compute the first-variation formulas and normalized-defect equality cases for k<A/3, k=A/3, and k>A/3. Second, check the topology/root-lattice argument for X a compact ball quotient: every embedded (-2)-sphere in X#k CPbar^2 lies in the exceptional -I_k lattice, and any embedded Kronheimer ADE plumbing determines a root subsystem of D_k. Scrutinize whether the signed-support-graph conclusion 'only A and D components' is valid for arbitrary root subsystems (not merely reflection-closed sets), whether E6/E7/E8 are excluded without primitivity, and whether a full-rank A_r plumbing with k=r is impossible. Identify and repair any hidden assumptions. Give a direct mathematical memo, not procedural advice.

## Integrated Scientific Memo

# Mathematical verification memo

The \(P\)-nonattainment argument is valid under the all-metric supply and resolution hypotheses of Theorem 74.A. The root-lattice exclusions are also valid, but require distinguishing the plumbing’s simple sphere classes from its full root system. Two qualifications matter: scalar-energy supply alone does not determine the sign of constant scalar curvature, and a full-rank \(A_3\) is an exception to the proposed \(A_r\) exclusion.

## 1. An attained \(P\)-floor would be Einstein

Use Step 74’s notation on the connected compact orbifold \(V_m\), with \(k=2m>0\):
\[
\sigma=S-32\pi^2A\ge0,\qquad
w=W-\frac{4\pi^2A}{3}=2I_-\ge0.
\]
Its Chern–Weil identities give
\[
P=8\pi^2k+\frac{\sigma}{12}+2w.
\]
Thus
\[
P(g)=8\pi^2k
\quad\Longrightarrow\quad
S(g)=32\pi^2A,\qquad W^-(g)=0.
\]
Crucially, \(S\ge32\pi^2A\) holds for **every** orbifold-smooth metric on the fixed orbifold. Consequently, such a \(g\) would globally minimize \(S\) over the unconstrained metric space.

### First variations

Let \(\Delta=\operatorname{div}\nabla\), and let \(h=\dot g\) be an orbifold-smooth symmetric covariant tensor. Then
\[
Ds_g[h]=-\langle\operatorname{Ric},h\rangle
+\nabla^i\nabla^j h_{ij}-\Delta(\operatorname{tr}_g h),
\qquad
D(d\mu)_g[h]=\frac12\operatorname{tr}_g h\,d\mu.
\]
Integration by parts yields
\[
DS_g[h]=\int_V
\left\langle
2\nabla^2s-2(\Delta s)g-2s\operatorname{Ric}
+\frac12s^2g,\ h
\right\rangle d\mu. \tag{1}
\]
These formulas hold on the orbifold: one works in finite uniformizing charts with invariant tensors and orbifold integration. Isolated quotient points introduce no boundary terms.

For \(g_t=e^{2t\phi}g\), the four-dimensional conformal formula is
\[
s_{g_t}=e^{-2t\phi}
\bigl(s-6t\Delta\phi-6t^2|d\phi|^2\bigr),
\qquad d\mu_{g_t}=e^{4t\phi}d\mu_g.
\]
Therefore
\[
\left.\frac{d}{dt}\right|_0S(g_t)
=-12\int_Vs\Delta\phi\,d\mu
=-12\int_V\phi\Delta s\,d\mu. \tag{2}
\]
Stationarity implies \(\Delta s=0\), and compactness and connectedness imply that \(s\) is constant. Since \(S=32\pi^2A>0\), this constant is nonzero.

For constant \(s\), (1) reduces to
\[
DS_g[h]=-2s\int_V\langle\operatorname{Ric}^{\circ},h\rangle\,d\mu.
\]
The admissible choice \(h=\operatorname{Ric}^{\circ}\) gives
\[
0=-2sP,
\]
so \(P=0\). This contradicts \(P=8\pi^2k>0\).

Hence
\[
\boxed{\inf_{\mathscr G_{\rm orb}(V_m)}P=8\pi^2k
\text{ is not attained for any }m\ge1.}
\]

This strengthens Step 74’s equality discussion without importing smooth Seiberg–Witten equality classifications into the singular limit. The norm equalities alone do not force constant \(s\); global minimization of the unconstrained scalar functional does. More generally, a critical point of \(\int s^2\) on a connected closed four-orbifold is either scalar-flat or Einstein.

## 2. Exact normalized-defect equality cases

Set
\[
q=\frac{4k}{A+k},\qquad B=8\pi^2(A+k).
\]
Step 74 gives
\[
R=B+\frac{\sigma}{3}+2w,\qquad
4P=qB+\frac{\sigma}{3}+8w.
\]
Thus
\[
\mathscr D-q
=\frac{(1-q)\sigma/3+2(4-q)w+L_s}{R}, \tag{3}
\]
and
\[
\mathscr D-1
=\frac{(q-1)B+6w+L_s}{R}. \tag{4}
\]
The denominator is strictly positive.

### Below the wall: \(k<A/3\)

Here \(q<1\). Every coefficient in (3) is positive, so
\[
\mathscr D=q
\iff \sigma=w=L_s=0.
\]
This would attain the forbidden \(P\)-floor. Therefore
\[
\boxed{\alpha_{\rm orb}(V_m)=\frac{4k}{A+k}
\text{ is not attained when }k<A/3.}
\]

### At the wall: \(k=A/3\)

Equation (4) becomes
\[
\mathscr D-1=\frac{6w+L_s}{R}.
\]
Consequently,
\[
\boxed{\mathscr D=1
\iff W^-=0\ \text{and}\ s\ \text{is constant}.} \tag{5}
\]
The constant is nonzero, but **its negativity does not follow from \(S\ge32\pi^2A\) alone**.

The required sign follows from the negative Yamabe input recorded in Step 74. Indeed, for any smooth metric \(\gamma\) on \(M_k\), writing \(s_-=\min(s,0)\), Hölder’s inequality in the Yamabe quotient gives
\[
Y(M_k,[\gamma])\ge-\|s_-\|_{L^2(\gamma)}.
\]
Since
\[
Y(M_k,[\gamma])\le Y(M_k)=-4\pi\sqrt{2A},
\]
one obtains
\[
\int_{M_k}s_-^2\,d\mu_\gamma\ge32\pi^2A.
\]
The resolution construction of Theorem 74.A transfers this inequality as well: fillers have zero scalar curvature, annular contributions vanish, and the retained bulk converges to \(g\). Thus
\[
\int_{V_m}s_-^2\,d\mu_g\ge32\pi^2A. \tag{6}
\]
A constant-scalar metric on \(V_m\) must therefore have \(s<0\).

Moreover, any wall extremal necessarily has
\[
\sigma>0,\qquad
P=8\pi^2k+\frac{\sigma}{12}>8\pi^2k,
\]
because \(\sigma=0\) would attain the \(P\)-floor. It is not Einstein and need not be critical for \(S\).

Thus wall attainment is precisely existence of an orbifold-smooth self-dual, constant-negative-scalar metric on \(V_m\). The supplied curvature inequalities neither construct nor exclude it. Since \(k=2m\) and \(9\mid A\), this wall occurs only when
\[
A=18j,\qquad k=6j,\qquad m=3j.
\]

There is also a conformal reformulation. Inequality (6) excludes nonnegative orbifold Yamabe constant: the nonpositive case has a Yamabe minimizer, while a positive Yamabe constant supplies a positive-scalar conformal metric. In a negative orbifold conformal class, the Yamabe variational problem has a smooth orbifold minimizer; concentration is excluded by the positive local spherical thresholds. Since \(W^-=0\) is conformally invariant, wall attainment is equivalently existence of a self-dual orbifold conformal class. This uses orbifold Yamabe existence, not merely the algebraic equality calculation.

### Above the wall: \(k>A/3\)

Now \(q>1\), and (4) gives
\[
\mathscr D-1\ge\frac{(q-1)B}{R}>0.
\]
Together with Step 74’s dumbbell sequence,
\[
\boxed{\alpha_{\rm orb}(V_m)=1
\text{ is not attained when }k>A/3.}
\]

Accordingly, the statement in Step 74 that attainment remains open for all \(k\le A/3\) should be narrowed to the wall alone.

## 3. Every spherical class lies in the exceptional lattice

Let \(X\) be a compact ball quotient and
\[
M=X\#k\overline{\mathbb{CP}}^{\,2}.
\]
Its universal cover is the contractible complex ball, so \(\pi_2(X)=0\). The connected-sum collapse \(b:M\to X\) induces the integral splitting
\[
H_2(M;\mathbb Z)
=H_2(X;\mathbb Z)\oplus\bigoplus_{i=1}^k\mathbb ZE_i,
\qquad E_i\cdot E_j=-\delta_{ij},
\]
with \(b_*\) the first projection.

For every sphere map \(f:S^2\to M\), \(b\circ f\) is null-homotopic. Hence
\[
f_*[S^2]\in\ker b_*=\bigoplus_i\mathbb ZE_i.
\]
This is an exact integral statement, including torsion: the sphere class has no host or torsion component.

For an embedded sphere of square \(-2\),
\[
[f(S^2)]=\sum_i a_iE_i,\qquad \sum_i a_i^2=2,
\]
so
\[
\boxed{[f(S^2)]=\pm E_i\pm E_j,\qquad i\ne j.} \tag{7}
\]
After reversing the sign of the intersection form, these are exactly the roots of \(D_k\). All spherical classes have nonpositive square; a positive-oriented ADE plumbing, with \(+2\)-sphere generators, is therefore excluded too.

The proposed restriction to the original smooth connected-sum presentation is unnecessarily strong. An oriented homeomorphism from another manifold to \(M\) transports the collapse map, homology splitting, and intersection form. Thus the same homological obstruction holds on any oriented manifold homeomorphic to \(M\). It does not hold merely from numerical agreement of intersection forms, nor for a nonaspherical host without a replacement argument.

## 4. A plumbing supplies a full root subsystem, without primitivity

Suppose a negative ADE plumbing embeds in \(M\), with sphere classes \(a_1,\dots,a_r\) and Gram matrix \(-C_R\), where \(C_R\) is its Cartan matrix. All \(a_i\) lie in the exceptional summand by (7).

The map
\[
Q(R)\longrightarrow \mathbb Z^k
\]
sending the abstract simple roots to these classes is an isometric injection, using the positive form \(-(\,\cdot\,)\). Indeed, a relation among their images, paired with every \(a_j\), lies in the kernel of \(C_R\), which is nonsingular.

Every abstract ADE root is an integral combination of the simple roots and has norm squared \(2\). Its image is therefore a norm-\(2\) integral vector in \(\mathbb Z^k\), hence a \(D_k\)-root. The isometry intertwines root reflections:
\[
\varphi(s_\alpha\beta)=s_{\varphi(\alpha)}\varphi(\beta).
\]
Thus the **full** image \(\varphi(R)\), rather than just the displayed sphere basis, is a root subsystem of \(D_k\).

No primitivity is used. Nonprimitivity affects the quotient lattice and complement topology, not injectivity, root norms, or reflection invariance. Nor does this argument assert that every abstract root image is represented by an additional embedded sphere.

## 5. Signed-support graphs: precise scope and proof

In the supplied Rembado paper, a root subsystem means a subset invariant under reflections in its own roots. This is weaker than being Levi and does not assume additive closedness. The claimed classification is valid for **all root subsystems in this sense**, not for arbitrary subsets of roots.

Let \(\Psi\subset\Phi(D_k)\) be such a subsystem. Draw a coordinate-support edge for each opposite root pair supported on \(\{i,j\}\). On a connected support block with \(v\) vertices:

1. Choose a spanning tree. Coordinate sign changes make every tree root a difference \(e_i-e_j\). These changes preserve \(D_k\) and \(\mathbb Z^k\); they need not belong to \(W(D_k)\).
2. Reflections in the tree roots are coordinate transpositions generating \(S_v\). Reflection invariance therefore puts **all** difference roots on the block in \(\Psi\).
3. If no sum root remains, the block is \(A_{v-1}\), of rank \(v-1\).
4. If a sum root occurs, \(S_v\) produces every sum root, and the block is \(D_v\), of rank \(v\).

Distinct support blocks are orthogonal. The small exceptions are
\[
D_2=A_1\oplus A_1,\qquad D_3=A_3.
\]
In particular, a connected coordinate-support graph need not give an irreducible root system: \(D_2\) is the exception.

This proves the specialized content of Rembado’s Theorem 3.1.3, Theorem 4.1.1, Lemma 4.2.1, and Corollary 4.3.1. It requires neither primitivity nor a Levi hypothesis.

For an arbitrary root list, the same argument classifies its **reflection closure**, not the list itself. For example,
\[
\{e_1-e_2,\ e_2-e_3\}
\]
is not the full \(A_2\) root system. The plumbing argument in §4 supplies exactly the missing closure step.

### Consequences

- **\(E_6,E_7,E_8\) are excluded for every \(k\).** Their full root systems cannot be subsystems of \(D_k\). This excludes their negative Kronheimer plumbings without primitivity.
- **A single full-rank \(A_r\) with \(k=r\) is impossible except at \(r=3\).** Ordinarily \(A_r\) needs \(r+1\) coordinates. The sole full-rank alias is \(A_3=D_3\); for example
  \[
  e_2-e_3,\quad e_1-e_2,\quad e_2+e_3
  \]
  have the \(A_3\) Cartan Gram matrix. Thus impossibility holds for \(r=1,2\) and \(r\ge4\). At \(r=3\), lattice feasibility is not a plumbing-existence proof; Step 74 independently excludes the corresponding Einstein-bulk budget.
- **Complete rational absorption forces \(D\)-blocks.** For disjoint plumbings spanning all exceptional \(\mathbb Q^k\), no \(A_{v-1}\) support block or unused coordinate can remain. The blocks are two \(A_1\) plumbings on a \(D_2\) block, one \(A_3\) on a \(D_3\) block, or one \(D_v\) plumbing for \(v\ge4\).

## 6. Compatibility with the full Step-74 budget

The topology removes the full-absorption \(E\)-rows and \(A_r\)-rows with \(r\ge4\) that survived the analytic screening. It leaves \(D\)-blocks, whose metric realization and Einstein bulk remain separate questions.

For complete absorption, let
\[
H=\sum_j\left(\chi(N_j)-\frac1{|\Gamma_j|}\right),\qquad
\varepsilon=H-\frac{7k}{6}.
\]
Corollary 74.D is exactly
\[
\boxed{\varepsilon\le-\frac{A}{27}
\left(1-\sqrt{1-\frac{3k}{A}}\right)^2, \qquad k\le A/3.} \tag{8}
\]
A paired-EH \(D_2\) block contributes \(2/3\) to \(\varepsilon\). A \(D_v\) block, including \(D_3=A_3\), contributes
\[
\varepsilon_v=1-\frac v6-\frac1{4(v-2)}.
\]
Thus \(\varepsilon_3=1/4\), \(\varepsilon_4=5/24\), \(\varepsilon_5=1/12\), and \(\varepsilon_6=-1/16\), reproducing the analytic exclusion of configurations made solely from small blocks.

One proposed extra conclusion is false: a \(D_v\) block plus a paired-EH \(D_2\) block is **not** excluded for every \(v\). For \(v=10\),
\[
\varepsilon_{10}+\frac23=-\frac1{32}<0,
\]
so (8) permits this mixture for sufficiently large \(A\). This remains only budget feasibility.

The unresolved objects are now precise: existence of a self-dual orbifold conformal class at the wall; simultaneous smooth realization of the surviving \(D\)-plumbings with the required complement; and existence of a negative Einstein metric on the contracted bulk. Rational-ball fillings and hypothetical ADE-end fillings without the Kronheimer sphere lattice are unaffected by the root obstruction.
# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step82_goldberg_levelset_SW_and_symmetric_closures.md",
    "Sessions/S1003A01/workspace/scripts/step82_sw_bochner_algebra.py",
    "Sessions/S1003A01/workspace/scripts/step82_sw_model.py",
    "Sessions/S1003A01/workspace/data/step82/sw_model.json",
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Sessions/S1003A01/workspace/notes/step81_normalized_sections_and_ddc_canonical_pairing.md",
    "Sessions/S1003A01/workspace/notes/step77_goldberg_first_tier_collapse_and_canonical_curve_identity.md"
  ]
}
```

## Task

Verify the new mathematics in Step 82 of a research programme on the closed negative-scalar Goldberg conjecture in dimension four: a closed almost-Kähler Einstein 4-manifold with s<0, is it Kähler? Read step82 note first; Steps 77, 80 and 81 supply the conventions. Check four things.

(1) Identity (82.1): X=dq/8−ReY, and the level-set identity (LS). Is it exactly equivalent to F(t)−16∫⟨X,n⟩=∫_{q<t}ρ? Is the family (82.2) correct, including the checked f=q identity? Is the claim correct that the trace equation fixes only div Y, with the trace-free ∇Y free through ∂_Dv?

(2) The exact identity (82.B), obtained by combining the Bochner identity, the f=q identity and the AAD balance. Check its dimensional restoration from the s=−1 computation.

(3) Section 3. Is LeBrun's Seiberg–Witten Weyl estimate ∫(s−√6|W⁺|)²≥72π²(c₁⁺)² correctly stated and applicable here? State precisely its hypotheses (b⁺>1, monopole class c₁, conventions for |W⁺|) and whether a different normalization of |W⁺| changes the conclusion. Check the reduction to ∫ψ₀≥18‖Hγ⁻‖², the forced multiplier λ=36, the null direction and second-order analysis, and the interpretation of the model value ∫ψ₀=520.13 against the slack bound 96.

(4) Proposition 82.H, the exclusion of cohomogeneity-one-type closures with locally homogeneous class-A principal orbits for closed negative Einstein metrics. Check the Euler-characteristic argument, the smoothness analysis at strata (free circle actions only, Seifert fibre for SL2R, the Nil/Sol/E(2) cases, SU(2) nuts and bolts with Bochner's Killing-field theorem), and whether the hypotheses are stated precisely enough. Mention any missing case, such as non-diagonal metrics, collapse of a 2-torus, or principal orbits that are only locally homogeneous with nontrivial holonomy.

Give a direct scientific memo: what is correct, what must be corrected, and the corrected statements.

## Output

# Scientific verification memo — Step 82

## 1. Amplitude-level identities

### Identity (82.1) and the level-set formula

With the conventions of Steps 80–81, for a real function \(u\),
\[
\operatorname{Re}\partial u=\frac12\,du.
\]
Since \(r=s/6+q/4\),
\[
\operatorname{Re}Y=\operatorname{Re}(\partial r-\eta\alpha)
=\frac18\,dq-X,
\]
and therefore
\[
X=\frac18\,dq-\operatorname{Re}Y.
\]
Thus (82.1) is correct. The norm convention
\[
|\operatorname{Re}Y|^{2}=\frac12|Y|^{2}
\]
is also consistent with the earlier complex-form conventions.

Let
\[
A=dq-16X,\qquad \operatorname{div}A=\rho,
\qquad
\rho=8(e+v)-\frac{|s|}{2}q+\frac34q^{2}.
\]
Using
\[
|dq-8X|^{2}=32|Y|^{2},\qquad 64|X|^{2}=16qe,
\]
one obtains
\[
\langle A,dq\rangle
=|dq|^{2}-16\langle X,dq\rangle
=32|Y|^{2}-16qe.
\]
Hence, on a regular level \(q=t\),
\[
\langle A,n\rangle
=\frac{32|Y|^{2}-16te}{|\nabla q|}.
\]
Integration over \(\{q<t\}\) gives exactly
\[
32\int_{q=t}\frac{|Y|^{2}}{|\nabla q|}\,dA
=
16t\int_{q=t}\frac e{|\nabla q|}\,dA
+\int_{q<t}\rho\,d\mu.
\]
Thus (LS) is precisely equivalent to
\[
F(t)-16\int_{q=t}\langle X,n\rangle\,dA
=\int_{q<t}\rho\,d\mu,
\qquad
F(t)=\int_{q=t}|\nabla q|\,dA.
\]

### The multiplier family

On a closed manifold, multiplication by a smooth \(f(q)\) gives
\[
\int f(q)\rho
=-\int f'(q)\langle dq,A\rangle.
\]
Substituting the preceding contraction yields
\[
32\int f'(q)|Y|^{2}
=
\int\left[16f'(q)qe-f(q)\rho\right],
\]
which is (82.2). Taking a decreasing Heaviside approximation \(f(q)=H(t-q)\) recovers (LS), including its sign.

For \(f=q\),
\[
32\int |Y|^{2}
=
\int\left[
\frac{|s|}{2}q^{2}+8qe-8qv-\frac34q^{3}
\right].
\]
This algebra is correct.

The model value can be independently recovered from the functions in `step82_sw_model.py`. With
\[
u=\frac{1-p^{2}}{1+3p^{2}},
\]
the radial measure simplifies to
\[
d\mu=\frac8{3u^{3}}\,du,\qquad 0\le u\le \frac23,
\]
while
\[
q=36u^{3},\quad e=9u^{3}(2-3u),\quad
v=\frac{81}{2}u^{4}(2-3u)^{2}.
\]
At \(|s|=12\), direct integration gives
\[
\int\left[
6q^{2}+8qe-8qv-\frac34q^{3}
\right]
=\frac{23552}{105}
=224.304761904\ldots,
\]
so
\[
\int |Y|^{2}=\frac{736}{105}.
\]

### What the trace equation determines

The precise real divergence equation is
\[
16\,\operatorname{div}(\operatorname{Re}Y)-\Delta q=\rho.
\]
Thus it fixes one real contraction of \(\nabla Y\), once \(q,e,v\) are specified. It does not determine the trace-free tensorial part of \(\nabla Y\).

The supplied E2 equation shows that \(\bar\partial_D\eta\), and hence part of \(\nabla(\eta\alpha)\), depends on \(\partial_Dv\); the primitive Hessian of \(q\) also enters \(\nabla Y\). Therefore those components are absent from this scalar subsystem. Calling them “free” is accurate in the symbol-level sense that the trace equation does not control them; arbitrary global realization would require a separate integrability argument.

One wording should be narrowed: (82.2) is the complete family obtained by testing the divergence equation with functions of \(q\). It is equivalent to the level-set pushforward of that equation, not to the full pointwise divergence PDE tested against arbitrary spatial functions.

---

## 2. The algebraic identity (82.B)

Put \(S=|s|\). The Bochner integrand expands as
\[
\begin{aligned}
\mathrm{Bo}
={}&\frac{S^{2}q}{32}-\frac{3Sq^{2}}{32}
+\frac{9q^{3}}{128}\\
&+\left(-\frac S2+\frac{9q}{4}\right)e
+\left(2S-\frac{9q}{4}\right)v+18x.
\end{aligned}
\]
Let
\[
A_q=\frac S2q^{2}+8qe-8qv-\frac34q^{3},
\qquad
Z_s=\frac{Sq}{16}-e-v-\frac{3q^{2}}{32}.
\]
The pointwise Weyl-gradient decomposition and the \(f=q\) identity give
\[
\begin{aligned}
10\int|\partial_Dv|^{2}
+2\int|\bar\partial_Dv+\eta\bar\alpha|^{2}
=\int\left(\mathrm{Bo}-\frac5{32}A_q-\frac S2 Z_s\right).
\end{aligned}
\]
Since \(\int Z_s=0\), direct expansion yields
\[
\boxed{
\begin{aligned}
10\int|\partial_Dv|^{2}
+2\int|\bar\partial_Dv+\eta\bar\alpha|^{2}
={}&\int\left[
\frac{5S}{2}v+18x+qe-qv\right.\\
&\left.\hspace{18mm}-\frac S8q^{2}+\frac{3}{16}q^{3}
\right].
\end{aligned}}
\]
Thus the displayed (82.B) is correct.

There is one textual correction: at general scale one subtracts
\[
\frac{|s|}{2}Z_s,
\]
not \(Z_s/2\). The latter is valid only after the script normalization \(s=-1\).

The dimensional restoration in the displayed formula is correct: \(S v\), \(x\), \(qe\), \(qv\), \(Sq^{2}\), and \(q^{3}\) all have curvature dimension \(L^{-6}\), matching the derivative-square terms.

---

## 3. LeBrun’s Seiberg–Witten Weyl estimate

### Exact hypotheses and normalization

LeBrun’s estimate is
\[
\int_M\left(s-\sqrt6\,|W^{+}|\right)^{2}d\mu
\ge 72\pi^{2}(a_g^{+})^{2},
\]
where:

- \(M\) is closed and oriented;
- \(a\in H^{2}(M;\mathbb Z)/\text{torsion}\) is a monopole class;
- \(a_g^{+}\) is its harmonic self-dual projection for the metric \(g\);
- \(|W^{+}|\) is the Hilbert–Schmidt norm of \(W^{+}\) as a trace-free symmetric endomorphism of \(\Lambda^{+}\).

For a symplectic four-manifold with \(b^{+}>1\), Taubes’ canonical basic class gives the required monopole class \(a=\pm c_{1}(TM,J)\), and the sign does not affect \((a_g^{+})^{2}\). Thus the estimate applies to every metric in that case. For \(b^{+}=1\), the chamber must be specified and the same universal application does not follow without an additional chamber argument.

The norm convention agrees with Step 82: at a Kähler metric,
\[
|W^{+}|^{2}=\frac{s^{2}}{24}.
\]
If the four-index tensor norm is used instead, then
\[
|W^{+}|_{\mathrm{tensor}}=2|W^{+}|_{\mathrm{op}},
\]
and the coefficient becomes \(\sqrt{3/2}\). A consistent conversion leaves the mathematical conclusion unchanged; retaining \(\sqrt6\) with the doubled norm would be incorrect.

### Reduction to \(\psi _0\)

Since \(s=-S\),
\[
(s-\sqrt6|W^{+}|)^{2}=(S+\sqrt6|W^{+}|)^{2}.
\]
Also
\[
(c_{1}^{+})^{2}=c_{1}^{2}+(c_{1}^{-})_{\mathrm{abs}}^{2},
\qquad
4\pi^{2}(c_{1}^{-})_{\mathrm{abs}}^{2}
=\|H\gamma^{-}\|^{2}.
\]
Using
\[
S^{2}V=32\pi^{2}c_{1}^{2}+16T_{\rm AK},
\qquad
T_{\rm AK}=\int\left(v+\frac{3q^{2}}{32}\right),
\]
the estimate becomes exactly
\[
\int\psi _0\ge18\|H\gamma^{-}\|^{2},
\]
where
\[
\psi _0=
(S+\sqrt6|W^{+}|)^{2}
-\frac94S^{2}
+36\left(v+\frac{3q^{2}}{32}\right).
\]
Because harmonic projection is \(L^{2}\)-orthogonal,
\[
\|H\gamma^{-}\|^{2}
\le\|\gamma^{-}\|^{2}
=\int\frac{q^{2}}{32},
\]
so the full chain
\[
\int\psi _0\ge18\|H\gamma^{-}\|^{2}\ge0
\]
is correct.

### Linear multiplier and null direction

At \(S=1\), the linear parts are
\[
Z_s:\quad \frac1{16}q-e-v,
\]
\[
\psi _0:\quad -\frac94q+36e+54v,
\]
\[
\mathrm{Bo}:\quad \frac1{32}q-\frac12e+2v+18x.
\]
For \(\psi _0+\lambda Z_s\) to have all \(q,e,v\) coefficients at least zero, one needs
\[
-\frac94+\frac{\lambda}{16}\ge0,\qquad
36-\lambda\ge0,\qquad
54-\lambda\ge0.
\]
These force
\[
\lambda=36.
\]
The resulting identity
\[
\psi _0+36Z_s
=(1+\sqrt6|W^{+}|)^{2}-\frac94+\frac94q-36e
\]
is correct at \(S=1\), with the evident \(S\)-factors at general scale.

The common first-order null direction is
\[
e=\frac q{16},\qquad v=x=0
\]
at \(S=1\).

### Quadratic expansion

Set
\[
e=\frac q{16}+a q^{2},\qquad
v=bq^{2},\qquad x=cq^{2}.
\]
The integrated AAD relation eliminates the \(a\)-term, and
\[
\int\psi _0
=
\frac{27}{16}Q_{2}+18B_{2}+O(q^{3}),
\]
where
\[
Q_{2}=\int q^{2},\qquad B_{2}=\int bq^{2}.
\]

The exact Seiberg–Witten statement at this order retains its harmonic term:
\[
\frac{27}{16}Q_{2}+18B_{2}
\ge18\|H\gamma^{-}\|^{2}_{(2)}.
\]
Since
\[
18\|H\gamma^{-}\|^{2}_{(2)}
\le\frac9{16}Q_{2},
\]
it is automatically satisfied at quadratic order. The note’s displayed inequality with right side \(0\) is a weaker consequence, not the full quadratic form of the Seiberg–Witten estimate.

From (82.B),
\[
\frac52B_{2}+18C_{2}\ge\frac1{16}Q_{2},
\qquad
C_{2}=\int c q^{2},
\]
and
\[
|c|\le\frac1{16}\sqrt{\frac b2}.
\]
Thus \(B_{2}\) cannot vanish when \(Q_{2}>0\); the \(V\)-sector must carry a fixed-order portion of the \(q^{2}\)-energy. This remains algebraically compatible with all the preceding identities.

### Meaning of the model number

The supplied data give
\[
\int q^{2}=\frac{512}{3},
\qquad
18\int\frac{q^{2}}{32}=96,
\qquad
\int\psi _0=520.134113\ldots.
\]
Therefore any harmonic-projection term satisfying the compact projection estimate would be at most \(96\), far below the computed \(\psi _0\)-integral.

The complete Bianchi-VIII space is not closed, so it has no direct Seiberg–Witten application here. The number \(96\) is a formal compact-style upper bound derived from its local \(\gamma^{-}\)-density, not an actual monopole-class term on that model. The computation nevertheless shows that the local and integrable algebraic densities do not oppose the LeBrun inequality.

---

## 4. Proposition 82.H and class-A closures

The Euler-characteristic mechanism is useful, but the proposition and its proof need substantial revision.

### Euler characteristic

If the regular region is assembled from cylinders \(I\times N\), and every omitted stratum \(B_j\) has a tubular disk neighborhood whose unit normal sphere bundle is the nearby level \(N\), then
\[
\chi(M)=\sum_j\chi(B_j),
\]
because every closed three-manifold has \(\chi(N)=0\).

For an Einstein metric,
\[
8\pi^{2}\chi(M)
=\int_M\left(|W^{+}|^{2}+|W^{-}|^{2}+\frac{s^{2}}{24}\right)d\mu.
\]
Thus \(s\ne0\) forces \(\chi(M)>0\). Consequently any such decomposition with total stratum Euler characteristic at most zero is impossible.

This validates the core argument for:

- Bianchi VIII circle fibrations over hyperbolic surfaces, where \(\chi(B)<0\);
- Nil, Sol, \(\widetilde E(2)\), and \(\mathbb R^{3}\) cases admitting smooth circle fibrations only over surfaces with \(\chi=0\);
- decompositions without singular strata, including mapping-torus arrangements, which have \(\chi(M)=0\).

### Smooth links

A smooth stratum of codimension \(k\) has normal link \(S^{k-1}\). For three-dimensional regular levels, the possibilities include:

- codimension two: an \(S^{1}\)-bundle over a surface;
- codimension three: an \(S^{2}\)-bundle over a one-manifold;
- codimension four: an \(S^{3}\) link at a point.

Thus “free circle or \(S^{3}\) nut only” omits codimension-three strata. Such strata contribute zero Euler characteristic, so they do not disrupt the Euler argument, but they must appear in a complete smoothness statement.

A collapsing \(T^{2}\) cannot itself be the normal link of a smooth codimension-three stratum: the link must be \(S^{2}\). A cone with \(T^{2}\) link is not locally a smooth normal disk. More intricate torus actions would need to be recast through the actual \(S^{2}\)-link geometry.

### The SU(2) bolt classification in the note is incorrect

The assertion that a smooth bolt forces \(\Gamma\subset\{\pm1\}\) is false. For every \(p\ge1\), take
\[
\Gamma=\mathbb Z_p
\]
inside a maximal torus of \(SU(2)\). Up to orientation,
\[
\Gamma\backslash S^{3}=L(p,1),
\]
and \(L(p,1)\) is the unit circle bundle of the smooth disk bundle over \(S^{2}\) with Euler number \(p\). Hence smooth \(S^{2}\)-bolts exist for all \(p\), not only \(p=1,2\).

The desired Bochner conclusion can still be recovered in the oriented free-circle case: a cyclic \(\Gamma\) has a positive-dimensional normalizer containing its maximal torus. Left translations by that normalizer descend to \(\Gamma\backslash SU(2)\), preserve every descended left-invariant \(g_t\), and extend across a smooth filling. This supplies a nonzero Killing field. Since
\[
\operatorname{Ric}=\lambda g,\qquad \lambda<0,
\]
the compact Killing-field Bochner identity forces every Killing field to vanish, giving the contradiction.

This argument does not require \(g_t\) to be diagonal. Arbitrary left-invariant inner products remain invariant under the descended normalizer translations.

### Local homogeneity versus a global group action

A genuine cohomogeneity-one isometric action by a connected Lie group is excluded immediately by the Killing-field Bochner theorem. The note, however, assumes only locally homogeneous slices. Local Killing fields on \(\Gamma\backslash G\) need not descend to global Killing fields unless the lattice or holonomy is normalized by the relevant subgroup.

Accordingly, the present hypotheses do not justify the sentence “the left \(SU(2)\) or \(SO(3)\) action is isometric on \(M\)” in full generality. It is valid for:

- a nut with \(\Gamma=1\);
- an oriented lens-space bolt with cyclic \(\Gamma\);
- any setup where the collapsing subgroup lies in a connected subgroup of \(N_G(\Gamma)\).

It is not automatic for:

- nonorientable bolt normal bundles;
- spherical quotients with more complicated finite holonomy;
- infra-homogeneous flat, Nil, or Sol levels not presented as pure lattice quotients \(\Gamma\backslash G\);
- local homogeneous structures whose developing holonomy twists the homogeneous frames between levels.

### Corrected form of Proposition 82.H

A justified version is:

> Let \(M\) be closed and oriented, and suppose its regular region is a finite union of products \(I\times N\), with \(N=\Gamma\backslash G\) for a fixed unimodular three-dimensional Lie group, and \(g=dt^{2}+g_t\) with each \(g_t\) descended from a left-invariant inner product on \(G\). Assume every omitted stratum has a smooth tubular disk neighborhood whose unit normal sphere bundle is the adjacent level \(N\). Then all non-\(SU(2)\) class-A cases have \(\chi(M)\le0\) and admit no Einstein metric with \(s<0\). The \(SU(2)\) case is also excluded whenever each nut or bolt supplies a connected subgroup of \(N_{SU(2)}(\Gamma)\) acting isometrically on the regular region.

This covers the Bianchi-VIII model and the standard fixed-lattice class-A closures. The broader formulation involving arbitrary locally homogeneous levels with nontrivial holonomy requires additional topology and isometry-extension analysis.

## Overall result

- (82.1), (LS), (82.2), and the \(f=q\) identity are correct.
- (82.B) is correct; the general-scale derivation uses \((|s|/2)Z_s\).
- LeBrun’s estimate and the reduction to \(\psi _0\) are correct for \(b^{+}>1\) with the operator norm of \(W^{+}\). The quadratic discussion must retain the harmonic term, though it remains automatically satisfied.
- The model calculation has the stated algebraic meaning but is not itself an application of Seiberg–Witten theory.
- The Euler part of Proposition 82.H is strong. Its smooth-stratum and \(SU(2)\) analysis need the corrections above, especially the lens-space bolts and the distinction between local and global symmetry.
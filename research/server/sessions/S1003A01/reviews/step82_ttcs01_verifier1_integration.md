# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 82,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step82_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step82_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the new mathematics in Step 82 of a research programme on the closed negative-scalar Goldberg conjecture in dimension four: a closed almost-Kähler Einstein 4-manifold with s<0, is it Kähler? Read step82 note first; Steps 77, 80 and 81 supply the conventions. Check four things.

(1) Identity (82.1): X=dq/8−ReY, and the level-set identity (LS). Is it exactly equivalent to F(t)−16∫⟨X,n⟩=∫_{q<t}ρ? Is the family (82.2) correct, including the checked f=q identity? Is the claim correct that the trace equation fixes only div Y, with the trace-free ∇Y free through ∂_Dv?

(2) The exact identity (82.B), obtained by combining the Bochner identity, the f=q identity and the AAD balance. Check its dimensional restoration from the s=−1 computation.

(3) Section 3. Is LeBrun's Seiberg–Witten Weyl estimate ∫(s−√6|W⁺|)²≥72π²(c₁⁺)² correctly stated and applicable here? State precisely its hypotheses (b⁺>1, monopole class c₁, conventions for |W⁺|) and whether a different normalization of |W⁺| changes the conclusion. Check the reduction to ∫ψ₀≥18‖Hγ⁻‖², the forced multiplier λ=36, the null direction and second-order analysis, and the interpretation of the model value ∫ψ₀=520.13 against the slack bound 96.

(4) Proposition 82.H, the exclusion of cohomogeneity-one-type closures with locally homogeneous class-A principal orbits for closed negative Einstein metrics. Check the Euler-characteristic argument, the smoothness analysis at strata (free circle actions only, Seifert fibre for SL2R, the Nil/Sol/E(2) cases, SU(2) nuts and bolts with Bochner's Killing-field theorem), and whether the hypotheses are stated precisely enough. Mention any missing case, such as non-diagonal metrics, collapse of a 2-torus, or principal orbits that are only locally homogeneous with nontrivial holonomy.

Give a direct scientific memo: what is correct, what must be corrected, and the corrected statements.

## Integrated Scientific Memo

# Verification memo — Step 82

The amplitude identities and (82.B) are correct. The Seiberg–Witten reduction is also correct under the stated \(b^+>1\) hypothesis and the correct Weyl norm, but its quadratic discussion and model interpretation need qualification. Proposition 82.H has a valid Euler-characteristic mechanism; its smooth-stratum hypotheses must be sharpened, and the distinction between **left lattice quotients**, right quotients, and general locally homogeneous quotients is essential.

Write \(S=|s|\), \(e=|\eta|^2\), \(v=\operatorname{tr}V^2\), and \(x=\eta^TV\eta\). All integrals below use the metric volume measure.

## 1. Amplitude and level-set identities

### (82.1), (LS), and (82.2)

For a real function \(q\), the conventions give
\[
\operatorname{Re}\partial q=\frac12dq.
\]
Consequently,
\[
Y=\frac14\partial q-\eta\alpha
\quad\Longrightarrow\quad
\boxed{X=\frac18dq-\operatorname{Re}Y},
\qquad
|\operatorname{Re}Y|^2=\frac12|Y|^2.
\]
Thus (82.1) is correct.

Set
\[
A=dq-16X=16\operatorname{Re}Y-dq,
\qquad
\rho=8(e+v)-\frac S2q+\frac34q^2.
\]
The supplied norm identities imply
\[
\langle A,dq\rangle
=|dq|^2-16\langle X,dq\rangle
=32|Y|^2-16qe.
\]
On a regular level \(q=t\), with outward normal \(n=dq^\sharp/|dq|\),
\[
\langle A,n\rangle=\frac{32|Y|^2-16te}{|dq|}.
\]
The divergence theorem therefore gives exactly
\[
\boxed{
32\int_{q=t}\frac{|Y|^2}{|dq|}\,dA
=
16t\int_{q=t}\frac e{|dq|}\,dA+\int_{q<t}\rho.
}
\]
This is precisely
\[
F(t)-16\int_{q=t}\langle X,n\rangle\,dA=\int_{q<t}\rho,
\qquad F(t)=\int_{q=t}|dq|\,dA,
\]
not a further restriction.

For any smooth \(f\) on the range of \(q\), integration by parts gives
\[
\int f(q)\rho=-\int f'(q)\langle dq,A\rangle,
\]
hence
\[
\boxed{
32\int f'(q)|Y|^2
=\int\bigl[16f'(q)qe-f(q)\rho\bigr].
}
\tag{82.2}
\]
Both stated specializations are correct:
\[
f=-\frac1{q+\varepsilon}\quad\Longrightarrow\quad(80.S),
\]
and
\[
\boxed{
32\int|Y|^2
=\int\left[\frac S2q^2+8qe-8qv-\frac34q^3\right].
}
\]
For the level-set specialization, use \(f(q)=H(t-q)\), understood by smooth approximation; this gives (LS) directly with the correct sign. Using \(H(q-t)\) instead also works after using \(\int\rho=0\).

A useful simplification is
\[
\boxed{\rho=-8Z_s},
\qquad
Z_s=\frac{Sq}{16}-e-v-\frac{3q^2}{32}.
\]

### The model’s \(f=q\) value is reproducible

Although neither Step-82 script explicitly computes \(Y\), the right-hand side can be evaluated from the supplied model functions. With
\[
u=\frac{1-p^2}{1+3p^2},\qquad 0<u<\frac23,
\]
they become
\[
d\mu=\frac8{3u^3}\,du,\quad
q=36u^3,\quad e=9u^3(2-3u),\quad
v=\frac{81}{2}u^4(2-3u)^2.
\]
At \(S=12\), polynomial integration gives
\[
\int\left[6q^2+8qe-8qv-\frac34q^3\right]
=\frac{23552}{105}
=224.304761904\ldots.
\]
Thus the asserted value corresponds to
\[
\int|Y|^2=\frac{736}{105}.
\]
This verifies the numerical right-hand side; a separate direct \(Y\)-calculation is not contained in the Step-82 artifacts.

### What the trace equation actually controls

The precise equation is
\[
\boxed{
16\operatorname{div}(\operatorname{Re}Y)-\Delta q=\rho=-8Z_s.
}
\]
It specifies **one real contraction** of \(\nabla Y\), not the whole complex divergence or its imaginary part.

Moreover, (82.2) is not “the complete content of the trace equation.” It is its complete family of tests **against functions of \(q\)**, equivalently its level-set-averaged content. Arbitrary spatial test functions retain information that these tests discard.

The supplied E2 system explains why \(\nabla Y\) contains components not fixed by this scalar equation: it contains the primitive Hessian of \(q\), \(\nabla(\eta\alpha)\), and an antiholomorphic derivative of \(\eta\) involving \(\partial_Dv\). Step 81 also leaves a symmetric component of \(D'\alpha\) undetermined. The justified statement is therefore:

> The trace equation and the displayed first-order subsystem do not determine the trace-free components of \(\nabla Y\); some depend on \(\partial_Dv\) and other undetermined jets.

This does **not** establish arbitrary realizability of those jets under all prolonged Einstein equations, nor prove that the full coupled PDE can impose no additional level-set restriction.

### Additional correction: the \(\beta\) boundary weight

The boundary integrand in §1 uses the wrong complex plane. On \(u=t\), choose an orthonormal tangent frame \((Jn,e,Je)\), where \(e\perp_{\mathbb C}n\). Then
\[
d^cu\wedge\beta
=\pm |du|\,\beta(e,Je)\,dA,
\]
not \(\pm|du|\,\beta(n,Jn)\,dA\).

Using P4,
\[
\boxed{
\int_{u<t}dd^cu\wedge\beta
=\pm\int_{u=t}|du|\frac q4|n_\alpha|^2\,dA.
}
\]
Accordingly, for \(u=q\), this expresses \((t/4)F_\alpha(t)\), not \((t/4)F_\perp(t)\). This agrees with P5, whose interior density simplifies to
\[
dd^cu\wedge\beta
=\left(\frac q4L_u(\ell_\alpha)+2\langle du,X\rangle\right)d\mu.
\]
The maximum-point observation remains valid, but it does not justify a blanket assertion that the primitive identity has no possible additional global use.

## 2. Identity (82.B) and dimensional restoration

The Bochner integrand expands at arbitrary \(S\) as
\[
\mathrm{Bo}
=\frac{S^2q}{32}-\frac{3Sq^2}{32}+\frac{9q^3}{128}
+\left(-\frac S2+\frac{9q}{4}\right)e
+\left(2S-\frac{9q}{4}\right)v+18x.
\]
Let
\[
A_q=\frac S2q^2+8qe-8qv-\frac34q^3.
\]
Combining the supplied Weyl-gradient decomposition, Bochner identity, and \(f=q\) identity gives
\[
10\int|\partial_Dv|^2+
2\int|\bar\partial_Dv+\eta\bar\alpha|^2
=\int\left(\mathrm{Bo}-\frac5{32}A_q\right).
\]
Since \(\int Z_s=0\), subtracting \((S/2)Z_s\) yields
\[
\boxed{
\begin{aligned}
10\int|\partial_Dv|^2+
2\int|\bar\partial_Dv+\eta\bar\alpha|^2
=\int\left[
\frac{5S}{2}v+18x+qe-qv-\frac S8q^2+\frac3{16}q^3
\right].
\end{aligned}}
\tag{82.B}
\]

Thus **the displayed identity and its dimensional restoration are correct**. The prose must say “subtract \((|s|/2)Z_s\),” not “subtract \(Z_s/2\),” except in the normalized \(s=-1\) calculation. Every resulting term has dimension \(L^{-6}\).

This verification uses the Step-79 gradient decomposition as an input inherited through Step 80. The numerical left-hand value \(339.81\) is not independently available in the supplied Step-82 artifacts: the model script does not supply \(x\) or the derivative squares.

Extension to a complete noncompact model requires integrability and vanishing exhaustion flux for the particular Bochner and divergence terms—not merely the general description “local densities.” Subject to those verified conditions, (82.B) is indeed a consolidation rather than an obstruction.

## 3. Seiberg–Witten Weyl estimate

### Hypotheses and norm

The applicable estimate is
\[
\boxed{
\int_M(s-\sqrt6\,|W^+|)^2\,d\mu
\ge72\pi^2(a_g^+)^2,
}
\]
for a closed oriented four-manifold and a monopole class \(a\), with its harmonic self-dual projection \(a_g^+\). Here “monopole class” means the first Chern class of a spin\(^c\) structure admitting solutions of the unperturbed Seiberg–Witten equations for every metric; a nonzero Seiberg–Witten invariant with \(b^+>1\) supplies such a class.

For a closed symplectic manifold with \(b^+>1\), the canonical basic class supplies \(a=\pm c_1(TM,J)\), so the estimate applies to the candidate metric. The sign is immaterial. **The Goldberg problem itself does not assume \(b^+>1\)**: this section therefore covers that subclass, or more generally candidates for which the relevant monopole-class hypothesis is separately established. For \(b^+=1\), a chamber-sensitive argument is required.

The norm is the Hilbert–Schmidt norm of the curvature endomorphism of \(\Lambda^+\):
\[
|W^+|^2=\frac32r^2+2e+v.
\]
At a Kähler metric it gives \(|W^+|^2=s^2/24\), confirming the normalization.

If instead one uses the full four-index tensor norm, then
\[
|W^+|_{\rm tensor}=2|W^+|_{\rm endomorphism},
\]
and \(\sqrt6\) must be replaced by \(\sqrt6/2=\sqrt{3/2}\). Consistent conversion changes no conclusion; retaining \(\sqrt6\) with the doubled norm changes the inequality and invalidates the calculation.

### Reduction to \(\psi_0\)

The supplied topological identity gives
\[
72\pi^2c_1^2=\frac94S^2V-36T_{\rm AK},
\qquad
T_{\rm AK}=\int\left(v+\frac{3q^2}{32}\right).
\]
Together with
\[
(c_1^+)^2=c_1^2+|c_1^-|_{\rm abs}^2,
\qquad
4\pi^2|c_1^-|_{\rm abs}^2=\|(H\gamma)^-\|^2,
\]
this yields exactly
\[
\boxed{\int\psi_0\ge18\|(H\gamma)^-\|^2},
\]
where
\[
\psi_0=(S+\sqrt6|W^+|)^2-\frac94S^2
+36\left(v+\frac{3q^2}{32}\right).
\]
Harmonic projection gives
\[
\|(H\gamma)^-\|^2
\le\|\gamma^-\|^2=\int\frac{q^2}{32}.
\]
The reduction is correct; \((H\gamma)^-\), equivalently the harmonic projection of \(\gamma^-\) onto harmonic ASD forms, is the precise meaning of \(H\gamma^-\).

### Multiplier and null direction

At general scale, the linear parts are
\[
Z_s:\ \frac S{16}q-e-v,
\]
\[
\psi_0:\ -\frac{9S}{4}q+36e+54v,
\]
\[
\mathrm{Bo}:\ \frac{S^2}{32}q-\frac S2e+2Sv+18x.
\]
The table in Step 82 is thus a normalized \(S=1\) table.

Nonnegativity of the linear part of \(\psi_0+\lambda Z_s\) on the independent nonnegative \(q,e,v\) directions requires
\[
\lambda\ge36,\qquad\lambda\le36,\qquad\lambda\le54,
\]
forcing
\[
\boxed{\lambda=36}.
\]
This is uniqueness within this one-multiplier, first-order positivity test, not a classification of all possible multipliers or geometric constraints.

The exact cancellation is
\[
\psi_0+36Z_s
=(S+\sqrt6|W^+|)^2-\frac94S^2+\frac94Sq-36e.
\]
Its linear part is \(18v\). The common null direction of the original three linearized constraints is
\[
e=\frac{Sq}{16},\qquad v=x=0.
\]

### Second order: retain the harmonic term

In the normalized scale \(S=1\), put
\[
e=\frac q{16}+aq^2,\qquad v=bq^2,\qquad x=cq^2.
\]
The quadratic coefficients are
\[
Z_s=-(a+b+3/32)q^2,
\]
\[
\psi_0=(81/16+36a+54b)q^2+O(q^3),
\]
\[
\mathrm{Bo}=(3/64-a/2+2b+18c)q^2+O(q^3).
\]
Eliminating the integrated \(a\)-term by AAD gives
\[
\int\psi_0=\frac{27}{16}Q_2+18B_2+O(q^3).
\]
The full quadratic SW condition is
\[
\boxed{
\frac{27}{16}Q_2+18B_2
\ge18\|(H\gamma)^-\|_{(2)}^2,
}
\]
not merely an inequality with right-hand side zero. Nevertheless,
\[
18\|(H\gamma)^-\|_{(2)}^2\le\frac9{16}Q_2,
\]
so it is automatically satisfied at this order, with worst-case margin
\[
\frac{18}{16}Q_2+18B_2.
\]

Using (82.B), nonnegativity of the remaining derivative energy gives
\[
\boxed{\frac52B_2+18C_2\ge\frac1{16}Q_2},
\qquad
|c|\le\frac1{16}\sqrt{\frac b2}.
\]
Thus the stated necessary quadratic algebraic constraints are consistent and require a nonzero \(V\)-sector when \(Q_2>0\). They do not establish realization by a perturbative family of actual Einstein almost-Kähler metrics; the derivative equations remain additional information.

### Meaning of \(520.13\) versus \(96\)

The supplied model data give
\[
\int q^2=\frac{512}{3},\qquad
18\int\frac{q^2}{32}=96,\qquad
\int\psi_0=520.134113369439\ldots.
\]
Thus its integrable density value exceeds **every compact-style harmonic term allowed by the projection bound**, by at least \(424.134\ldots\).

This is not an application of Seiberg–Witten theory to the noncompact model, nor an actual computation of its monopole-class harmonic term. It shows that this numerical integral constraint does not distinguish the model densities from allowable closed-candidate densities. It does not prove that every closed geometry resembling the model satisfies all global SW constraints, or that all compactness-sensitive mechanisms must involve only infinite volume or torsion zeros.

## 4. Proposition 82.H: valid mechanism, corrected scope

### Euler characteristic

For a finite tubular-stratum decomposition, with regular pieces cylinders or mapping-torus pieces and adjacent levels the unit normal sphere bundles,
\[
\chi(M)=\sum_j\chi(B_j).
\]
The boundary three-manifolds contribute zero. For an Einstein metric,
\[
8\pi^2\chi(M)
=\int\left(|W^+|^2+|W^-|^2+\frac{s^2}{24}\right).
\]
Hence \(s\ne0\) forces \(\chi(M)>0\). Excluding decompositions with \(\sum_j\chi(B_j)\le0\) is sound.

The present words “open dense set” and “strata where \(g_t\) degenerates” do not themselves establish this finite tubular decomposition.

### Smooth strata and missing cases

Smooth normal links are:
\[
\begin{array}{c|c}
\dim B&\text{normal link}\\ \hline
2&S^1\\
1&S^2\\
0&S^3.
\end{array}
\]
Thus “free circle or \(S^3\) nut only” is incomplete. One must include curve strata, and possibly codimension-one exceptional strata with \(S^0\) links; both have Euler characteristic zero.

A direct collapse with normal link \(T^2\) is not smooth: a curve stratum requires \(S^2\), not \(T^2\). In fact an \(S^2\)-bundle over a closed curve cannot be one of the fixed class-A lattice quotients here: its fundamental group is virtually \(\mathbb Z\), unlike either a compact aspherical class-A quotient or a spherical quotient.

For bolts, the general smooth datum is a unit normal circle bundle, potentially with \(O(2)\) structure group—not universally a global free circle action. The free-action argument is justified in the fixed left-invariant setting only after identifying the collapsing line field and its uniform period.

### Fixed left quotients: circle collapse and the SU(2) disagreement

For the exact ansatz \(N=\Gamma\backslash G\), with every \(g_t\) induced by a **left-invariant** metric, a rank-one limiting kernel is left-invariant. Its leaves are right-multiplication trajectories
\[
g\longmapsto g\exp(t\xi).
\]
Smooth normal circles require a common period. Then
\[
g\exp(T\xi)g^{-1}\in\Gamma\quad\text{for every }g.
\]
Discreteness forces \(\exp(T\xi)\) to be central.

This gives:

- **\(\widetilde{SL}_2\):** only the elliptic/Seifert direction can close. Exceptional Seifert fibres are incompatible with this smooth bolt collapse. A free fibration has a hyperbolic surface base, with negative Euler characteristic.
- **Nil:** central circle collapse, with torus base.
- **Sol:** no such periodic collapsing direction.
- **\(\widetilde E(2)\):** circle collapse must not be dismissed. For example, a translation lattice together with a central full-turn period gives a free right-rotation circle and torus base. The Euler contribution is still zero.
- **\(\mathbb R^3\):** primitive lattice-circle collapse, with torus base. Klein-bottle bases belong to an enlarged holonomy setting, not the pure translation-lattice case.

For **SU(2)**, a nut requires \(\Gamma=1\). For a smooth bolt of this specific left-invariant-kernel type, freeness forces
\[
\Gamma\subset\{\pm1\}.
\]
Indeed every noncentral element of a finite \(\Gamma\subset SU(2)\) is conjugate into the collapsing maximal torus and creates shorter-period leaves; the induced action on \(SU(2)/U(1)=S^2\) has fixed points.

The proposed lens-space objection does **not** refute this restricted conclusion. Smooth disk bundles over \(S^2\) certainly have boundaries \(L(p,1)\) for arbitrary \(p\), but their homogeneous collapse uses the relevant **right-quotient/Hopf-fibre realization**, not an arbitrary left quotient carrying this fixed left-invariant collapsing kernel. Interchanging left and right also interchanges left- and right-invariance of the metric. Lens-space bolts therefore refute a claim about *all* spherical homogeneous closures, but not the above fixed-left-quotient argument.

When \(\Gamma\) is central, the left \(SU(2)\) action descends and preserves every \(g_t\), including non-diagonal ones. Its isometries extend to the smooth metric completion. A nonzero Killing field contradicts the compact Bochner identity
\[
\int|\nabla K|^2=\int\operatorname{Ric}(K,K)
=\lambda\int|K|^2,\qquad\lambda<0.
\]

### Corrected proposition

A sufficiently precise, supported version is:

> Let \(M\) be closed and oriented. Assume its regular region consists of finitely many product cylinders with fixed levels \(N=\Gamma\backslash G\), where \(G\) is a connected unimodular three-dimensional Lie group and \(\Gamma\subset G\) is a left lattice. Assume \(g=dt^2+g_t\), with every \(g_t\) descended from a left-invariant inner product. Assume the omitted sets are smooth strata with tubular disk neighborhoods whose unit normal sphere bundles are the adjacent levels, and that surface collapses are the smooth circle collapses of the limiting left-invariant kernel. Then \(g\) cannot be Einstein with negative scalar curvature.

For non-spherical class-A groups the strata have nonpositive total Euler characteristic; for SU(2), smooth compatible nuts and bolts supply a global Killing field. No diagonal-metric assumption is needed.

Arbitrary locally homogeneous principal levels with nontrivial developing holonomy are **not covered** by this proof. Such holonomy may prevent local Killing fields from descending, alter the circle-bundle structure, and require separate treatment of nonorientable bolts and spherical quotients. Genuine global cohomogeneity-one isometric actions are already excluded directly by Bochner.

**Consequently, the standard fixed-lattice Bianchi-VIII closure is excluded, but “every symmetric closure” and “any locally homogeneous hypersurface foliation of this type” are too broad without the corrected structural hypotheses.**
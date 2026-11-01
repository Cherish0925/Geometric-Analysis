# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 34,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step34_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step34_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 34 corrected fixed-exponent analytic layer for the selected-support normalized cutoff flow in the Yau-26 restricted 4D negative route. Read the new note and script, plus the prior Step 33 power note and Step 25 q=2 derivation as background. Focus on scientific correctness: (i) the all-lower curvature convention and pure scaling test; (ii) the corrected diffusion dissipation -p D_Rm - p(p-2) D_F before cutoff absorption; (iii) the volume-form term being controlled by the curvature reaction via |s+4|<=CF rather than C delta K_p; (iv) the integrated-potential bound B(t)<=C gamma^3 from q=2 and its use to obtain q=3 same-support propagation by good-slice + Gronwall without circularity; (v) the regularized defect derivation from Ricci variation and whether the no-additive-source conclusion is justified at the stated level. Identify any mathematical faults or missing assumptions that would invalidate these fixed-exponent consequences, and distinguish them from the later unproved moving-Sobolev/cutoff-jet continuation obligations.

## Integrated Scientific Memo

## Step 34 fixed-exponent layer: verification outcome

The corrected Step 34 analytic layer is essentially sound **as a conditional fixed-exponent module**, but two within-module clarifications are needed for a rigorous write-up:

1. the \(q=2\) seed must use the buffered local energy \(K_2^\eta=\int \eta^2F^2\), not the literal \(K_2=\int a^0F^2\) from the \(p\ge3\) convention;
2. the signed Hessian IBP estimates require derivative-structure bounds such as \(|\nabla B|\lesssim F|\nabla{\rm Rm}|\) and \(|\nabla C|\lesssim f_\varepsilon|\nabla E|\), not only \(|B|\lesssim F^2\), \(|C|\lesssim f_\varepsilon^2\).

With those inserted, the consequences
\[
B(t)=\int_0^t{\mathcal S}(s)^2Y(s)\,ds\le C\gamma^3,
\qquad
Y(t)\le {C\gamma K_2^\eta(0)\over t},
\qquad
J_6(t)\le C J_6(0)
\]
follow non-circularly on the provisional smooth first-exit interval where the moving Sobolev and metric-comparison assumptions hold. The later moving-Sobolev/cutoff-jet continuation remains unproved, but that is separate from this fixed-exponent verification.

---

## 1. All-lower convention and pure scaling test

Step 34’s all-lower convention is correct. For
\[
\partial_t g=-2g,\qquad g(t)=e^{-2t}g_0,
\]
the Levi-Civita connection and \(R_{ijk}{}^\ell\) are fixed, while
\[
R_{ijkl}=g_{\ell\alpha}R_{ijk}{}^\alpha
\]
scales as \(e^{-2t}\). Therefore
\[
2\langle R,\partial_tR\rangle=-4|R|^2.
\]
The four inverse metrics in
\[
|{\rm Rm}|^2=g^{-1}g^{-1}g^{-1}g^{-1}RR
\]
contribute \(+8|R|^2\), hence
\[
\partial_t|{\rm Rm}|^2=4|{\rm Rm}|^2.
\]
In dimension four,
\[
\partial_td\mu=-4d\mu,
\]
so
\[
\partial_t(|{\rm Rm}|^2d\mu)=0.
\]
For \(F^2=1+|{\rm Rm}|^2\),
\[
\frac d{dt}\int F^2\,d\mu=-4\int 1\,d\mu.
\]

Thus the normalization/conformal piece must not be recorded as pointwise curvature damping. It is only a lower-order weighted source in upper energy estimates. This agrees with Step 25’s correction and fixes the older Step 33 bookkeeping.

One small technical correction: Step 33’s schematic conformal contribution included a possible \(\nabla a\otimes\nabla a\) term. The first variation of curvature is linear in \(h\) and its derivatives; for \(h=-2ag\), the cutoff differentiation gives \(\nabla^2a*g\), not a quadratic \((\nabla a)^2\) term at the first-variation level. This does not affect Step 34’s corrected inequality, which keeps only signed Hessian contractions and first-derivative cutoff terms coming from the Ricci part.

---

## 2. Diffusion dissipation coefficient

Step 34’s corrected pre-absorption dissipation is right.

Testing
\[
a\Delta F^2-2a|\nabla{\rm Rm}|^2
\]
by
\[
\frac p2 a^{p-2}F^{p-2}
\]
gives, using \(\Delta F^2=2F\Delta F+2|\nabla F|^2\),
\[
\frac p2\int a^{p-2}F^{p-2}a\Delta F^2
=
-p(p-2)D_p^F
-p(p-1)\int a^{p-2}F^{p-1}\nabla a\cdot\nabla F,
\]
where
\[
D_p^F=\int a^{p-1}F^{p-2}|\nabla F|^2.
\]
The explicit tensor term gives
\[
\frac p2\int a^{p-2}F^{p-2}(-2a|\nabla{\rm Rm}|^2)
=
-pD_p^{\rm Rm},
\]
with
\[
D_p^{\rm Rm}=\int a^{p-1}F^{p-2}|\nabla{\rm Rm}|^2.
\]
Therefore before absorbing cutoff terms,
\[
\boxed{
-pD_p^{\rm Rm}-p(p-2)D_p^F
}
\]
is the correct dissipation.

The Step 33 coefficient \(-p(p-3)D_p^F\) came from treating the tensor term as \(-p(D_p^{\rm Rm}-D_p^F)\), thereby adding back a spurious \(+pD_p^F\). Step 34 correctly avoids that. This matters especially at \(p=3\): the corrected formula retains \(3D_3^F\), while Step 33’s formula loses radial dissipation at \(p=3\).

The first-derivative cutoff absorption is also consistent:
\[
|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}
\]
implies
\[
a^{p-3}|\nabla a|^2F^p\le Cr^{-2}a^{p-2}F^p,
\]
so the Young counterterms have the \(K_p\) weight.

---

## 3. Volume-form term

Step 34’s volume-form treatment is correct and removes a circular Step 33 input.

For the flow
\[
\partial_tg=-2aE,\qquad E={\rm Ric}+g,
\]
in dimension four,
\[
\partial_td\mu=-a(s+4)d\mu.
\]
Since
\[
s+4=\operatorname{tr}E,\qquad |s+4|\le C|E|\le CF,
\]
one has
\[
\left|\int a^{p-2}F^p\,\partial_td\mu\right|
=
\left|\int a^{p-1}(s+4)F^p\,d\mu\right|
\le
C\int a^{p-1}F^{p+1}\,d\mu.
\]
Thus the volume term belongs to the same curvature reaction
\[
R_p=Cp\int a^{p-1}F^{p+1}.
\]
It should not be bounded by \(C\delta K_p\) before defect persistence or pointwise smallness of \(E\) has been proved.

The reaction absorption identity is correct:
\[
a^{p-1}F^{p+1}
=
(aF^3)^{1/3}
(a^{p-2}F^p)^{1/3}
z_p^{4/3},
\qquad
z_p=a^{(p-1)/2}F^{p/2}.
\]
Hölder and the squared Sobolev convention
\[
\|u\|_4^2\le{\mathcal S}\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr)
\]
give the coefficient
\[
{\mathcal S}^2YK_p,
\]
not an extra Sobolev power. This matches the A03 correction that the relevant absorption parameter is
\[
\gamma={\mathcal S}K_2^{1/2}.
\]

Lower-order terms coming from the \(1\) inside \(F=(1+|{\rm Rm}|^2)^{1/2}\) are multiplicative:
\[
\int a^{p-2}\cdot 1 \le \int a^{p-2}F^p=K_p
\]
for \(F\ge1\). They can be included in \(C(r^{-2}+1)K_p\), not as an unweighted volume source.

---

## 4. Necessary \(q=2\) notation correction

There is a real notational fault in Step 34 as written.

For \(p\ge3\),
\[
K_p=\int a^{p-2}F^p
\]
is fine because \(a^{p-2}\) localizes the integral. But for \(p=2\), this formula gives
\[
K_2=\int F^2,
\]
with no \(a\)-localization. That is not the Step 25 local buffered energy and cannot be controlled by the local good-support estimate \(K_0V\).

The \(q=2\) seed must instead use
\[
K_2^\eta=\int \eta^2F^2,\qquad
D_2^\eta=\int \eta^2a|\nabla{\rm Rm}|^2,
\]
where \(\eta=1\) on \(\operatorname{supp}a\) and has the buffered support properties from Step 25.

Then
\[
Y=\int aF^3
=
\int (\eta F)(\chi F)^2
\le
(K_2^\eta)^{1/2}\|\chi F\|_4^2,
\]
and Sobolev gives
\[
\|\chi F\|_4^2
\le
C{\mathcal S}\bigl(D_2^\eta+r^{-2}K_2^\eta\bigr).
\]
Hence the correct \(p=2\) interpolation is
\[
Y\le C{\mathcal S}(K_2^\eta)^{1/2}
\bigl(D_2^\eta+r^{-2}K_2^\eta\bigr).
\]

The good-support volume cancellation becomes
\[
\gamma={\mathcal S}(0)(K_2^\eta(0))^{1/2},
\qquad
K_2^\eta(0)\le CK_0V,
\]
so
\[
\gamma\le C\frac{r^2}{\sqrt V}\sqrt{K_0V}
=Cr^2\sqrt{K_0}.
\]
With this replacement, the Step 34 \(q=2\to B(t)\) argument is valid.

---

## 5. Integrated potential \(B(t)\le C\gamma^3\) and same-support \(q=3\) propagation

On the provisional first-exit interval where
\[
{\mathcal S}(t)\le2{\mathcal S}(0),
\qquad
K_2^\eta(t)\le2K_2^\eta(0),
\]
Step 25’s \(q=2\) estimate has the form
\[
(K_2^\eta)'+cD_2^\eta
\le
CY+Cr^{-2}K_2^\eta.
\]
Using the interpolation above,
\[
Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta)
\]
on that interval. If \(C\gamma\) is small, the \(D_2^\eta\) contribution is absorbed, giving for \(t\le T=\theta r^2\)
\[
\sup_{s\le t}K_2^\eta(s)+\int_0^tD_2^\eta(s)\,ds
\le
CK_2^\eta(0)
\]
after choosing \(\theta\) fixed small enough for the \(r^{-2}K_2^\eta\) Gronwall factor.

Then
\[
\int_0^tY(s)\,ds
\le
C\gamma\int_0^t(D_2^\eta+r^{-2}K_2^\eta)\,ds
\le
C\gamma K_2^\eta(0).
\]
Therefore
\[
B(t)
=
\int_0^t{\mathcal S}(s)^2Y(s)\,ds
\le
C{\mathcal S}(0)^2\gamma K_2^\eta(0)
=
C\gamma^3.
\]
This uses only the \(q=2\) energy layer and Sobolev interpolation. It does not use any pointwise \(q=3\) estimate.

Now the fixed-\(p\) curvature inequality at \(p=3\) gives
\[
Y'\le C(r^{-2}+1+{\mathcal S}^2Y)Y.
\]
For any \(t>0\), choose a good slice \(\tau\in[t/4,t/2]\) such that
\[
Y(\tau)\le {4\over t}\int_{t/4}^{t/2}Y(s)\,ds
\le
{C\gamma K_2^\eta(0)\over t}.
\]
Integrating the differential inequality from \(\tau\) to \(t\),
\[
Y(t)
\le
Y(\tau)\exp\left(
C\int_\tau^t(r^{-2}+1)\,ds
+
C\int_\tau^t{\mathcal S}^2Y\,ds
\right).
\]
For \(t\le\theta r^2\),
\[
\int_\tau^t(r^{-2}+1)\,ds\le C(\theta+\theta r^2),
\]
and
\[
\int_\tau^t{\mathcal S}^2Y\,ds\le B(t)\le C\gamma^3.
\]
Thus
\[
Y(t)\le {C\gamma K_2^\eta(0)\over t},
\qquad
{\mathcal S}(t)^2Y(t)\le {C\gamma^3\over t}.
\]

The \(t^{-1}\) bound is a positive-time output and is not integrated from zero. The integrable-from-zero control used in \(J_6\) persistence is \(B(t)\le C\gamma^3\), so there is no circularity.

---

## 6. Signed Hessian cutoff terms

Step 34 correctly rejects the invalid Step 33 maneuver of integrating by parts on \(|\nabla^2a|\). The correct route is to keep the signed contractions
\[
T_H
=
p\int a^{p-2}F^{p-2}(\nabla_i\nabla_ja)B^{ij}
\]
and integrate by parts on \(\nabla_i\nabla_ja\).

However, the estimate
\[
|T_H|
\le
\varepsilon pD_p^{\rm Rm}
+\varepsilon p(p-2)D_p^F
+C_\varepsilon p^Nr^{-2}K_p
\]
does not follow merely from
\[
|B|\le CF^2.
\]
One also needs the actual tensor structure of the Hessian contractions to imply
\[
|\nabla B|\le CF|\nabla{\rm Rm}|.
\]
This is expected for the curvature terms because \(B\) is built algebraically from \({\rm Rm}\), \(E={\rm Ric}+g\), and \(g\), and
\[
|\nabla E|\le C|\nabla{\rm Rm}|.
\]
But it must be stated and checked for the finite list of actual contractions in the all-lower curvature variation.

With that added, the IBP is legitimate:

- derivative on \(a^{p-2}\): controlled by \(r^{-2}K_p\);
- derivative on \(F^{p-2}\): controlled by \(D_p^F\) and \(r^{-2}K_p\);
- derivative on \(B\): controlled by \(D_p^{\rm Rm}\) and \(r^{-2}K_p\).

Thus the fixed-\(p\) curvature inequality
\[
K_p'
+c\bigl[pD_p^{\rm Rm}+p(p-2)D_p^F\bigr]
\le
Cp^N(r^{-2}+1+{\mathcal S}^2Y)K_p
\]
is valid conditional on the index-level curvature variation and the above \(\nabla B\) structure.

This signed-Hessian route avoids needing a pointwise evolving bound \(|\nabla^2_{g(t)}a|\le Cr^{-2}\), which belongs to the later cutoff-jet continuation problem.

---

## 7. Defect equation and regularized homogeneous estimate

The defect equation must indeed be derived from Ricci variation, not copied from the curvature evolution. Structurally,
\[
E_t=(\operatorname{Ric}+g)_t
=D\operatorname{Ric}_g[-2aE]-2aE.
\]
Since \(D\operatorname{Ric}\) is linear in \(h=-2aE\) and its first two derivatives, all terms contain \(E\), \(\nabla E\), or \(\nabla^2E\). Using the contracted Bianchi identity, the \(a\nabla^2E\) terms combine into a Lichnerowicz-type principal operator, leaving
\[
\partial_tE
=
a\Delta E
+\operatorname{Rm}*(aE)
+(\nabla a)*\nabla E
+(\nabla^2a)*E
+\text{linear }aE
\]
up to harmless algebraic lower-order contractions. Step 34’s displayed additional \(aE*E\) term is at worst an over-inclusive schematic term; it is harmless because
\[
|aE*E|\le CaF|E|
\]
or after testing contributes to the same \(CaF|E|^2\) reaction. The important point is that there is no curvature-only forcing term independent of \(E\).

For
\[
f_\varepsilon=(|E|^2+\varepsilon)^{1/2},
\qquad
J_{p,\varepsilon}=\int a^{p-2}f_\varepsilon^p,
\]
the diffusion calculation is uniform in \(\varepsilon\). Since
\[
f_\varepsilon^2=|E|^2+\varepsilon,
\qquad
\Delta f_\varepsilon^2=\Delta |E|^2,
\]
the principal integration by parts introduces no additive \(\varepsilon\)-source. The favorable radial term
\[
-p(p-2)\int a^{p-1}f_\varepsilon^{p-2}|\nabla f_\varepsilon|^2
\]
may be retained or dropped; the essential dissipation is
\[
D_{p,\varepsilon}^E
=
\int a^{p-1}f_\varepsilon^{p-2}|\nabla E|^2.
\]
The inequalities
\[
|\nabla f_\varepsilon|\le|\nabla E|,
\qquad
|E|\le f_\varepsilon
\]
make the cutoff terms uniform in \(\varepsilon\).

As with curvature, the defect Hessian IBP needs more than
\[
|C|\le Cf_\varepsilon^2.
\]
One needs the actual homogeneous structure
\[
C=C(E,E)\quad\text{or at least}\quad
|C|\le C|E|^2,\qquad
|\nabla C|\le C|E||\nabla E|,
\]
with regularized replacements bounded by \(f_\varepsilon|\nabla E|\). This is expected from \((\nabla^2a)*E\) tested against \(E f_\varepsilon^{p-2}\), but should be made explicit.

The algebraic, norm-variation, and volume terms are bounded by
\[
C\int a^{p-1}Ff_\varepsilon^p.
\]
The identity
\[
a^{p-1}Ff_\varepsilon^p
=
(aF^3)^{1/3}
(a^{p-2}f_\varepsilon^p)^{1/3}
\left(a^{(p-1)/2}f_\varepsilon^{p/2}\right)^{4/3}
\]
is correct, and Sobolev–Young gives
\[
\int a^{p-1}Ff_\varepsilon^p
\le
\varepsilon D_{p,\varepsilon}^E
+
C_\varepsilon p^N{\mathcal S}^2YJ_{p,\varepsilon}
+
C_\varepsilon p^Nr^{-2}J_{p,\varepsilon}.
\]
Hence
\[
J_{p,\varepsilon}'+cD_{p,\varepsilon}^E
\le
Cp^N(r^{-2}+1+{\mathcal S}^2Y)J_{p,\varepsilon}.
\]

This is a multiplicative homogeneous inequality. The regularization does not generate a curvature-only additive source. Letting \(\varepsilon\downarrow0\) is justified at the energy level by monotone/dominated convergence for \(J_{p,\varepsilon}\) and lower semicontinuity, or monotone convergence, for the dissipative spacetime term.

For \(p=6\),
\[
J_6(t)
\le
J_6(0)
\exp\left(
C\int_0^t(r^{-2}+1+{\mathcal S}^2Y)\,ds
\right).
\]
Using \(t\le\theta r^2\) and \(B(t)\le C\gamma^3\),
\[
\int_0^t(r^{-2}+1)\,ds\le C(\theta+\theta r^2),
\qquad
\int_0^t{\mathcal S}^2Y\,ds\le C\gamma^3.
\]
Therefore
\[
J_6(t)\le C(\theta,\gamma,r_0)J_6(0),
\]
or simply \(J_6(t)\le CJ_6(0)\) if \(r\le r_0\) is fixed, e.g. \(r_0\le1\).

---

## 8. Script evidence

The script `step34_integrated_potential_q3_verify.py` correctly checks algebraic and scaling facts:

- pure conformal scaling in dimension four;
- the corrected diffusion coefficient form;
- cutoff-weight exponents using \(|\nabla a|^2/a\);
- the three-factor Hölder identities;
- \(\gamma={\mathcal S}K_2^{1/2}\) volume cancellation;
- \(B\sim\gamma^3\);
- good-slice/Gronwall algebraic form;
- absence of a logarithmic \(t=0\) singularity in the \(J_6\) Gronwall exponent.

But its checks do not verify the tensor PDE estimates, signed Hessian contraction structure, moving Sobolev first-exit, smooth existence, or cutoff-jet continuation. Some script lines are algebraic restatements rather than independent mathematical tests; in particular the sample times in the good-slice section are illustrative and not constrained by \(t\le\theta r^2\). This is acceptable because the script explicitly says it only checks algebra/scaling/ODE consequences conditional on the PDE premises.

---

## 9. Final verification status

The fixed-exponent consequences survive, with the following precise status.

### Correct and supported

\[
\partial_t|{\rm Rm}|^2=4|{\rm Rm}|^2
\]
under pure \(\partial_tg=-2g\) all-lower scaling in dimension four, and
\[
\int |{\rm Rm}|^2\,d\mu
\]
is invariant.

The corrected dissipation is
\[
-pD_p^{\rm Rm}-p(p-2)D_p^F.
\]

The volume-form term must be treated as
\[
C\int a^{p-1}F^{p+1},
\]
not \(C\delta K_p\).

The integrated potential estimate
\[
B(t)\le C\gamma^3
\]
is derived from the \(q=2\) energy estimate and Sobolev interpolation alone.

The same-support \(q=3\) bound
\[
Y(t)\le {C\gamma K_2^\eta(0)\over t}
\]
follows by good-slice plus Gronwall using \(B(t)\), without circularity.

The regularized defect inequality is homogeneous and yields
\[
J_6(t)\le CJ_6(0)
\]
without a curvature-only additive source.

### Must be corrected or added inside the fixed-exponent write-up

Replace the literal \(K_2=\int F^2\) by the buffered local quantity
\[
K_2^\eta=\int\eta^2F^2
\]
in the \(q=2\) seed, \(\gamma\), and \(B(t)\) derivation.

State and verify the derivative structure of Hessian-contraction tensors:
\[
|\nabla B|\lesssim F|\nabla{\rm Rm}|,
\qquad
|\nabla C|\lesssim f_\varepsilon|\nabla E|.
\]
Without these, the signed Hessian IBP estimates are not justified by the displayed size bounds alone.

### Still unproved but later-layer obligations, not fixed-exponent faults

- smooth existence of the degenerate cutoff Ricci-type flow on the required interval;
- moving Sobolev control \({\mathcal S}(t)\le2{\mathcal S}(0)\);
- metric comparability and support/buffer persistence;
- high-\(p\) nested Moser endpoint;
- evolving cutoff-jet estimates such as the coupled \((\nabla U,\nabla^2\chi)\) base pair.

Thus Step 34 is scientifically correct as a repaired fixed-exponent analytic layer, conditional on the explicitly stated tensor-variation and first-exit hypotheses, after the \(K_2^\eta\) and Hessian-derivative-structure clarifications are incorporated.
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 39,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step39_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step39_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 39 general-p homogeneous defect power inequality for the normalized cutoff flow. The note claims:

1. REGULARITY: For p≥6, s^{p/2} with s=|E|² is C² at s=0, so no Kato regularization is needed. Check this for non-integer p (e.g. p=9, 13.5, 20.25).

2. STRUCTURAL DICHOTOMY: The two-factor absorption P_p ≤ γ(X_p+r⁻²H_p) works at fixed p but fails on the Moser ladder because the reaction coefficient in (4.13) is Cq·R_p, so absorption requires γ≲1/p → 0. The three-factor route R_p ≤ Y^{1/3}H_p^{1/3}||z_p||_4^{4/3} followed by Young(3,3/2) converts to a Grönwall coefficient Cp⁴(S²Y)H_p with only polynomial p-growth, which does not require p-dependent smallness. Is this dichotomy correct? Is there a third option (e.g. interpolation between fixed-p two-factor and three-factor)?  

3. THREE-FACTOR HÖLDER IDENTITY: Check that η²a^{p-1}Fs^q = (η²aF³)^{1/3}(η²a^{p-2}s^q)^{1/3}(η²a^{2(p-1)}s^{2q})^{1/3} has matching exponents, and that the third factor is indeed z_p^{4/3}.

4. HESSIAN-a IBP for general q: The note integrates ∇²a against the defect tensor B_def^{ij} = sg^{ij}+τE^{ij}-2(E²)^{ij} with weight η²a^{p-2}s^{q-1}, hits three factors, and bounds each using |B_def|≤Cs, |∇B_def|≤Cs^{1/2}|∇E|. For the derivative-on-s branch, verify the integrand s^{q-3/2}|∇E| factor. For the derivative-on-B branch, verify the tensor derivative bound chain.

5. GRADIENT COMPARISON (5.2)-(5.4): With z_p = η a^{(p-1)/2} s^{q/2}, verify ||∇z_p||² ≤ (q²/2)X_p' + Cp²r⁻²H_p, and that the ratio q²/2 divided by q(q-1) equals q/(2(q-1)) ≤ 3/4 for all q≥3.

6. NO E-INDEPENDENT SOURCE: Confirm that every term in the assembled inequality (4.13) carries at least one power of E (i.e., at least s^{1/2} or |∇E|). Identify any possible source of a constant additive term.

## Integrated Scientific Memo

# Step 39 verification

Under the stated smooth first-exit, support, and Sobolev hypotheses, the general-\(p\) defect inequality is valid. The main corrections are:

- the Hessian derivative-on-\(s\) branch contains \(s^{q-3/2}|\nabla E|\) **before** multiplication by \(B_{\rm def}=O(s)\), and \(s^{q-1/2}|\nabla E|\) in the complete integrand;
- the three-factor method is not literally the only alternative to the \(K_2\)-only estimate: there is an interpolation family using higher curvature moments, and after curvature smoothing one may use \(\|aF\|_\infty\) directly.

## 1. Regularity for real \(p\)

Put \(q=p/2\ge3\). For any real \(\beta>2\),
\[
t^\beta\in C^2([0,\infty)),\qquad
(t^\beta)''=\beta(\beta-1)t^{\beta-2},
\]
with second derivative \(0\) at \(t=0\). Hence \(s^q\), with \(s=|E|^2\ge0\), is \(C^2\), and
\[
(\partial_t-a\Delta)s^q
=q s^{q-1}(\partial_t-a\Delta)s
-aq(q-1)s^{q-2}|\nabla s|^2
\]
holds classically across \(\{s=0\}\). At such points \(\nabla s=0\); alternatively,
\[
s^{q-2}|\nabla s|^2\le4s^{q-1}|\nabla E|^2\to0.
\]

For the listed exponents:
\[
p=9,\ 13.5,\ 20.25
\quad\Longrightarrow\quad
q=4.5,\ 6.75,\ 10.125,
\]
so all are safely above the \(C^2\) threshold. No Kato regularization is needed.

The claim in the note that \(s^q\) is \(C^3\) for \(q\ge3\) is also correct, including at \(q=3\). The proof itself only needs \(C^2\). Likewise,
\[
a^{p-2}=\chi^{2(p-2)}
\]
has sufficient finite regularity for the derivatives used; a flat cutoff is optional, not necessary.

## 2. Hessian-\(a\) integration by parts

The term is
\[
T_H=2q\int (\nabla_i\nabla_j a)\,
\eta^2a^{p-2}s^{q-1}B_{\rm def}^{ij},
\]
where
\[
B_{\rm def}^{ij}=sg^{ij}+\tau E^{ij}-2(E^2)^{ij}.
\]
Signed integration by parts gives
\[
T_H=-2q\int\nabla_j a\,
\nabla_i\!\left(\eta^2a^{p-2}s^{q-1}B_{\rm def}^{ij}\right).
\]

The tensor bounds follow directly:
\[
|B_{\rm def}|\le Cs,
\]
and, using metric compatibility,
\[
\nabla B_{\rm def}
=(\nabla s)g+(\nabla\tau)E+\tau\nabla E
-2\bigl((\nabla E)E+E\nabla E\bigr).
\]
Since
\[
|\nabla s|\le2|E||\nabla E|,\quad
|\nabla\tau|\le C|\nabla E|,\quad
|\tau|\le C|E|,
\]
every summand is \(O(|E||\nabla E|)\), so
\[
|\nabla B_{\rm def}|\le Cs^{1/2}|\nabla E|.
\]
In particular, \((\nabla\tau)E\) has the required factor \(|E|\); there is no bare \(C|\nabla E|\) term.

For the three nonzero derivative branches:

1. **Derivative on \(a^{p-2}\):**
   \[
   q(p-2)a^{p-3}|\nabla a|^2s^{q-1}|B_{\rm def}|
   \le Cpq\,a^{p-2}|d\chi|^2s^q,
   \]
   hence \(Cpq\,r^{-2}H_p\).

2. **Derivative on \(s^{q-1}\):**
   \[
   |\nabla(s^{q-1})|
   \le2(q-1)s^{q-3/2}|\nabla E|.
   \]
   This is the requested \(s^{q-3/2}\) factor. After multiplying by
   \(|B_{\rm def}|\le Cs\), the full density becomes
   \[
   Cq^2a^{p-3/2}|d\chi|\,
   s^{q-1/2}|\nabla E|.
   \]
   Thus the note’s complete integrand is correct.

3. **Derivative on \(B_{\rm def}\):**
   \[
   Cq\,a^{p-3/2}|d\chi|\,
   s^{q-1/2}|\nabla E|.
   \]

The last two have the factorization
\[
\bigl(\eta a^{(p-1)/2}s^{(q-1)/2}|\nabla E|\bigr)
\bigl(\eta a^{(p-2)/2}|d\chi|s^{q/2}\bigr),
\]
and therefore are controlled by \(\varepsilon qX_p\) plus polynomial-\(p\)
multiples of \(r^{-2}H_p\). The \(d\eta\) branch vanishes by the support convention. Hence
\[
|T_H|
\le\varepsilon qX_p+C\varepsilon^{-1}p^3r^{-2}H_p
\]
is justified, with no \(\nabla^2\chi\) estimate and no division by \(a\).

## 3. Gradient comparison

Writing
\[
z_p=\eta a^{(p-1)/2}s^{q/2},
\]
and using the vanishing of the \(d\eta\) term,
\[
\nabla z_p
=\eta\frac{p-1}{2}a^{(p-3)/2}\nabla a\,s^{q/2}
+\eta a^{(p-1)/2}\frac q2s^{q/2-1}\nabla s.
\]
Since \(\nabla a=2a^{1/2}d\chi\), the first square is bounded by
\(Cp^2r^{-2}H_p\). Applying \(|A+B|^2\le2|A|^2+2|B|^2\) to the second gives
\[
\boxed{\;
\|\nabla z_p\|_2^2
\le\frac{q^2}{2}X_p'+Cp^2r^{-2}H_p.
\;}
\]
Moreover,
\[
\frac{q^2/2}{q(q-1)}
=\frac{q}{2(q-1)}
\le\frac34,\qquad q\ge3,
\]
with equality at \(q=3\). Therefore
\[
\|\nabla z_p\|_2^2
\le\frac34\mathcal D_p+Cp^2r^{-2}H_p.
\]
Retaining the chain-rule dissipation \(q(q-1)X_p'\) is essential; \(2qX_p\) alone cannot uniformly pay the \(q^2X_p'\) gradient cost.

## 4. Three-factor identity

The \(a,F,s\) exponents in
\[
\eta^2a^{p-1}Fs^q
=(\eta^2aF^3)^{1/3}
(\eta^2a^{p-2}s^q)^{1/3}
(\eta^2a^{2(p-1)}s^{2q})^{1/3}
\]
match:
\[
\frac{1+(p-2)+2(p-1)}3=p-1,\qquad
\frac{q+2q}{3}=q,\qquad \frac33=1.
\]
The total \(\eta\)-power is also \(\eta^2\).

Strictly, the written third cube-root has \(\eta^{2/3}\), whereas
\[
z_p^{4/3}
=\eta^{4/3}a^{2(p-1)/3}s^{2q/3}.
\]
Their identification uses the single-support convention: \(\eta=1\) wherever \(a>0\), and both vanish where \(a=0\). Equivalently,
\[
\int\eta^2a^{2(p-1)}s^{2q}
=\int\eta^4a^{2(p-1)}s^{2q}
=\|z_p\|_4^4.
\]
Thus
\[
R_p\le Y^{1/3}H_p^{1/3}\|z_p\|_4^{4/3}
\]
is valid.

With
\[
\mathcal W_p=\|\nabla z_p\|_2^2+r^{-2}H_p,
\qquad
\|z_p\|_4^2\le\mathcal S\mathcal W_p,
\]
one obtains
\[
qR_p
\le q\mathcal S^{2/3}Y^{1/3}H_p^{1/3}\mathcal W_p^{2/3}
\le\varepsilon\mathcal W_p
+C\varepsilon^{-2}q^3\mathcal S^2YH_p.
\]
The cube of the prefactor is exactly
\[
q^3\mathcal S^2YH_p.
\]
Hence no \(p\)-dependent smallness is required. The displayed bookkeeping is actually \(O(p^3)\); the theorem’s \(Cp^4\) is a safe, non-sharp envelope.

## 5. Structural alternatives

The specific contrast is correct:

- the \(K_2\)-only estimate
  \[
  R_p\le\gamma\mathcal W_p
  \]
  yields \(Cq\gamma\mathcal D_p\), so absorption requires
  \[
  \gamma\lesssim q^{-1}\simeq p^{-1};
  \]
- the three-factor estimate makes the gradient dependence sublinear,
  \(\mathcal W_p^{2/3}\), allowing Young with a freely chosen \(\varepsilon\).

Thus the two-factor argument is suitable at fixed \(p\), but not uniformly on an unbounded Moser ladder for fixed nonzero \(\gamma\).

However, “the ladder must use this three-factor route” is too strong. There is a continuum of higher-integrability variants. For fixed \(m>2\), let
\[
L_m=\int\eta^2a^{m-2}F^m.
\]
The same weighted Hölder algebra gives
\[
R_p\le
L_m^{1/m}H_p^{(m-2)/m}\|z_p\|_4^{4/m},
\]
and therefore
\[
qR_p
\le\varepsilon\mathcal W_p+
C_{m,\varepsilon}
q^{m/(m-2)}
\mathcal S^{2/(m-2)}
L_m^{1/(m-2)}H_p.
\]
For \(2<m<3\),
\[
L_m\le K_2^{\,3-m}Y^{\,m-2}.
\]
These are genuine interpolations between the \(m=2\) endpoint and the \(m=3\) estimate, although their \(q\)-growth is worse than cubic. Among estimates based only on the already available \(K_2\) and \(Y=L_3\), \(m=3\) is the most efficient.

After the curvature endpoint is known, there is also the direct bound
\[
R_p=\int(aF)\,\eta^2a^{p-2}s^q
\le\|aF\|_\infty H_p,
\]
which on a dyadic slab gives a Grönwall coefficient \(Cp\gamma/t\). Thus the precise structural conclusion is:

> The \(K_2\)-only, two-factor power estimate fails uniformly on the ladder. Some curvature control strictly above \(L^2\), or the later \(L^\infty\) curvature estimate, converts the reaction to a Grönwall multiplier. The \(Y=L_3\) three-factor route is the simplest efficient pre-endpoint implementation, not the unique possible one.

## 6. Absence of an \(E\)-independent source

All terms retain defect factors:

- reaction terms: \(aFs\), \(as\);
- cutoff-gradient terms: \(|\nabla a|s^{1/2}|\nabla E|\);
- Hessian term: \((\nabla^2a):B_{\rm def}\), with \(B_{\rm def}=O(s)\);
- metric norm variation: algebraic terms at least cubic in \(E\);
- measure variation: \(-a\tau s^q\);
- Young remainders: multiples of \(H_p\);
- dissipative terms: powers of \(s\) times \(|\nabla E|^2\) or \(|\nabla s|^2\).

Although \(F=(1+|\mathrm{Rm}|^2)^{1/2}\) contains a constant \(1\), it occurs only multiplied by \(s^q\) in \(R_p\). Likewise, \(Y\) enters only as a coefficient multiplying \(H_p\), never additively.

A constant source could have been introduced by:

1. regularizing \(s\) to \(s+\varepsilon^2\) and failing to eliminate the resulting remainder; or
2. replacing the exact quadratic estimate \(B_{\rm def}=O(s)\) by a crude \(O(1+s)\) estimate.

Neither occurs. Consequently, when \(E\equiv0\), every term in (4.13) and the resulting inequality vanishes.

## Verdict

The term-by-term derivation supports
\[
H_p'+c\|\nabla z_p\|_2^2
\le Cp^4\bigl(1+r^{-2}+\mathcal S^2Y\bigr)H_p,
\qquad p\ge6,
\]
for every real \(p\), conditional on the stated smooth first-exit and support assumptions. It closes the previously missing general-\(p\) analytic input for the defect Moser ladder. The broader flow existence, continuation, simultaneous first-exit closure, and geometric conclusions remain separate unresolved inputs.
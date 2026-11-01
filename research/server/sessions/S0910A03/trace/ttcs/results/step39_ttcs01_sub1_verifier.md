# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step39_general_p_defect_power_inequality.md",
    "Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A03/trace/ttcs/results/step38_ttcs01_verifier2_integration.md"
  ]
}
```

## Task

Verify the Step 39 general-p homogeneous defect power inequality for the normalized cutoff flow. The note claims:

1. REGULARITY: For p≥6, s^{p/2} with s=|E|² is C² at s=0, so no Kato regularization is needed. Check this for non-integer p (e.g. p=9, 13.5, 20.25).

2. STRUCTURAL DICHOTOMY: The two-factor absorption P_p ≤ γ(X_p+r⁻²H_p) works at fixed p but fails on the Moser ladder because the reaction coefficient in (4.13) is Cq·R_p, so absorption requires γ≲1/p → 0. The three-factor route R_p ≤ Y^{1/3}H_p^{1/3}||z_p||_4^{4/3} followed by Young(3,3/2) converts to a Grönwall coefficient Cp⁴(S²Y)H_p with only polynomial p-growth, which does not require p-dependent smallness. Is this dichotomy correct? Is there a third option (e.g. interpolation between fixed-p two-factor and three-factor)?  

3. THREE-FACTOR HÖLDER IDENTITY: Check that η²a^{p-1}Fs^q = (η²aF³)^{1/3}(η²a^{p-2}s^q)^{1/3}(η²a^{2(p-1)}s^{2q})^{1/3} has matching exponents, and that the third factor is indeed z_p^{4/3}.

4. HESSIAN-a IBP for general q: The note integrates ∇²a against the defect tensor B_def^{ij} = sg^{ij}+τE^{ij}-2(E²)^{ij} with weight η²a^{p-2}s^{q-1}, hits three factors, and bounds each using |B_def|≤Cs, |∇B_def|≤Cs^{1/2}|∇E|. For the derivative-on-s branch, verify the integrand s^{q-3/2}|∇E| factor. For the derivative-on-B branch, verify the tensor derivative bound chain.

5. GRADIENT COMPARISON (5.2)-(5.4): With z_p = η a^{(p-1)/2} s^{q/2}, verify ||∇z_p||² ≤ (q²/2)X_p' + Cp²r⁻²H_p, and that the ratio q²/2 divided by q(q-1) equals q/(2(q-1)) ≤ 3/4 for all q≥3.

6. NO E-INDEPENDENT SOURCE: Confirm that every term in the assembled inequality (4.13) carries at least one power of E (i.e., at least s^{1/2} or |∇E|). Identify any possible source of a constant additive term.

## Output

# Scientific verification memo

## Overall assessment

Under the stated hypotheses—a smooth four-dimensional cutoff flow, time-independent \(a=\chi^2\), the single-support convention for \(\eta\), moving Sobolev comparability, and \(|d\chi|\lesssim r^{-1}\)—the derivation of Theorem 7.1 is mathematically consistent. The unregularized real-\(p\) calculation, Hessian-\(a\) integration by parts, gradient comparison, and three-factor Young estimate all work.

Two refinements are important:

1. In the Hessian derivative-on-\(s\) branch, \(s^{q-3/2}|\nabla E|\) occurs **before** multiplication by \(B_{\rm def}=O(s)\); the complete integrand contains \(s^{q-1/2}|\nabla E|\), as written in Step 39.
2. The two-factor/three-factor contrast is correct for those two endpoint estimates, but the word “necessarily” is too strong. There is a continuum of intermediate \(L^m\) estimates, and the already-derived curvature endpoint \(\|aF\|_\infty\lesssim\gamma/t\) gives another direct route. What is structurally established is that the \(K_2\)-only, two-factor power estimate leaves \(q\gamma\) multiplying the gradient energy.

## 1. Real-\(p\) regularity at \(s=0\)

Let \(q=p/2\ge3\). For \(\beta>2\),
\[
\phi_\beta(t)=t^\beta,\qquad t\ge0,
\]
has two continuous derivatives at \(0\), with
\[
\phi_\beta'(0)=\phi_\beta''(0)=0.
\]
Thus \(s^q\) is \(C^2\), sufficient for
\[
\Delta(s^q)
=q s^{q-1}\Delta s+q(q-1)s^{q-2}|\nabla s|^2
\]
and hence
\[
(\partial_t-a\Delta)s^q
=q s^{q-1}(\partial_t-a\Delta)s
-aq(q-1)s^{q-2}|\nabla s|^2.
\]

At a zero of the smooth scalar \(s\ge0\), \(\nabla s=0\), so the displayed formula extends classically across \(s=0\). For the actual Moser exponents:

\[
\begin{array}{c|c|c}
p&q=p/2&\text{regularity of }t^q\text{ at }0\\ \hline
9&4.5&C^4\\
13.5&6.75&C^6\\
20.25&10.125&C^{10}
\end{array}
\]

All exceed the required \(C^2\) regularity. At \(p=6\), \(s^3\) is a polynomial.

The Sobolev variable
\[
z_p=\eta a^{(p-1)/2}s^{q/2}
\]
also has the required \(C^1\) regularity because \(q/2\ge3/2\). Likewise
\[
a^{p-2}=\chi^{2(p-2)}
\]
has at least eight derivatives in \(\chi\) for \(p\ge6\), whereas the proof uses only its first derivative. Flatness of \(\chi\) is therefore optional rather than necessary.

## 2. Hessian-\(a\) integration by parts

The relevant term is
\[
T_H
=2q\int(\nabla_i\nabla_j a)\,
  \eta^2a^{p-2}s^{q-1}B_{\rm def}^{ij},
\]
where
\[
B_{\rm def}^{ij}
=sg^{ij}+\tau E^{ij}-2(E^2)^{ij}.
\]
On the closed manifold,
\[
T_H
=-2q\int \nabla_j a\,
\nabla_i\!\left(\eta^2a^{p-2}s^{q-1}B_{\rm def}^{ij}\right).
\]

### Derivative on \(a^{p-2}\)

Using \(|B_{\rm def}|\le Cs\) and
\[
|\nabla a|^2=4a|d\chi|^2,
\]
the density is bounded by
\[
Cq(p-2)a^{p-3}|\nabla a|^2s^{q-1}|B_{\rm def}|
\le Cpq\,a^{p-2}|d\chi|^2s^q.
\]
Its integral is at most \(Cpq\,r^{-2}H_p\).

### Derivative on \(s^{q-1}\)

First,
\[
|\nabla(s^{q-1})|
=(q-1)s^{q-2}|\nabla s|
\le 2(q-1)s^{q-3/2}|\nabla E|.
\]
This is the requested \(s^{q-3/2}|\nabla E|\) factor. Multiplication by
\[
|B_{\rm def}|\le Cs
\]
raises it to
\[
Cs^{q-1/2}|\nabla E|.
\]
Therefore the complete density is
\[
Cq^2a^{p-3/2}|d\chi|s^{q-1/2}|\nabla E|,
\]
exactly the expression in Step 39. Splitting it as
\[
\bigl(a^{(p-1)/2}s^{(q-1)/2}|\nabla E|\bigr)
\bigl(a^{(p-2)/2}|d\chi|s^{q/2}\bigr)
\]
and paying \(\varepsilon qX_p\) gives the remainder
\[
C\varepsilon^{-1}q^3r^{-2}H_p.
\]

### Derivative on \(B_{\rm def}\)

Metric compatibility gives
\[
\begin{aligned}
\nabla B_{\rm def}
={}&(\nabla s)g+(\nabla\tau)\otimes E+\tau\nabla E\\
&-2\bigl((\nabla E)E+E(\nabla E)\bigr).
\end{aligned}
\]
Now
\[
|\nabla s|\le2|E||\nabla E|,\qquad
|\nabla\tau|\le C|\nabla E|,\qquad
|\tau|\le C|E|.
\]
Every summand is consequently bounded by
\[
C|E||\nabla E|=Cs^{1/2}|\nabla E|.
\]
Thus this branch has density
\[
Cq\,a^{p-3/2}|d\chi|s^{q-1/2}|\nabla E|,
\]
again matching the same Young pairing.

The \(\nabla\eta\) branch is zero because \(\nabla a=0\) on \(\operatorname{supp}d\eta\). Hence
\[
|T_H|
\le \varepsilon qX_p+C\varepsilon^{-1}p^3r^{-2}H_p
\]
is supported by the explicit tensor calculation.

## 3. Gradient comparison

Since the \(d\eta\) term vanishes,
\[
\begin{aligned}
\nabla z_p
={}&\eta\frac{p-1}{2}a^{(p-3)/2}\nabla a\,s^{q/2}\\
&+\eta a^{(p-1)/2}\frac q2s^{q/2-1}\nabla s.
\end{aligned}
\]
Using \(\nabla a=2a^{1/2}d\chi\), the first term has square bounded by
\[
Cp^2r^{-2}\eta^2a^{p-2}s^q.
\]
For the second term, applying \(|A+B|^2\le2|A|^2+2|B|^2\) gives
\[
2\left(\frac q2\right)^2
\eta^2a^{p-1}s^{q-2}|\nabla s|^2
=\frac{q^2}{2}\,X_p'.
\]
Therefore
\[
\boxed{\;
\|\nabla z_p\|_2^2
\le\frac{q^2}{2}X_p'+Cp^2r^{-2}H_p.
\;}
\]

The chain-rule dissipation contains \(q(q-1)X_p'\), and
\[
\frac{q^2/2}{q(q-1)}
=\frac{q}{2(q-1)}
\le\frac34,\qquad q\ge3,
\]
with equality at \(q=3\). Hence
\[
\|\nabla z_p\|_2^2
\le\frac34\mathcal D_p+Cp^2r^{-2}H_p.
\]
The coefficient \(3/4\) is independent of \(p\).

## 4. Three-factor identity and Young estimate

The exponents in
\[
\eta^2a^{p-1}Fs^q
=(\eta^2aF^3)^{1/3}
(\eta^2a^{p-2}s^q)^{1/3}
(\eta^2a^{2(p-1)}s^{2q})^{1/3}
\]
match exactly:

\[
\frac13+\frac{p-2}{3}+\frac{2(p-1)}3=p-1,
\]
\[
\frac q3+\frac{2q}{3}=q,\qquad
\frac33=1,
\]
and the three \(\eta\)-powers sum to \(\eta^2\).

Algebraically,
\[
z_p^{4/3}
=\eta^{4/3}a^{2(p-1)/3}s^{2q/3},
\]
whereas the displayed third factor initially has \(\eta^{2/3}\). They are nevertheless equal under the single-support convention: where \(a>0\), one has \(\eta=1\), and where \(a=0\), both expressions vanish. Equivalently,
\[
\int\eta^2a^{2(p-1)}s^{2q}
=\int\eta^4a^{2(p-1)}s^{2q}
=\|z_p\|_4^4.
\]
Thus Hölder gives
\[
R_p\le Y^{1/3}H_p^{1/3}\|z_p\|_4^{4/3}.
\]

Writing
\[
\mathcal W_p=\|\nabla z_p\|_2^2+r^{-2}H_p
\]
and using \(\|z_p\|_4^2\le\mathcal S\mathcal W_p\),
\[
qR_p
\le q\,\mathcal S^{2/3}Y^{1/3}H_p^{1/3}\mathcal W_p^{2/3}.
\]
Young with exponents \(3\) and \(3/2\) yields
\[
qR_p
\le\varepsilon\mathcal W_p
+C\varepsilon^{-2}q^3\mathcal S^2YH_p.
\]
The free \(\varepsilon\) absorbs a fixed fraction of the gradient energy; no relation between \(p\) and \(\gamma\) is introduced.

The bookkeeping displayed in Step 39 actually produces at most cubic growth in \(p\): \(p^2q\), \(q^3\), and \(p^3\). Therefore the stated \(Cp^4\) coefficient is valid but not sharp.

## 5. Two-factor obstruction and other routes

The two-factor estimate gives
\[
R_p\le\gamma\mathcal W_p.
\]
Since the energy equation contains \(CqR_p\),
\[
CqR_p\le Cq\gamma
\left(\frac34\mathcal D_p+Cp^2r^{-2}H_p\right).
\]
Absorption into a fixed fraction of \(\mathcal D_p\) requires
\[
Cq\gamma<c,
\]
hence \(\gamma\lesssim p^{-1}\). For fixed geometry this cannot hold through \(p_k\to\infty\). Young’s inequality cannot alter this conclusion because \(\mathcal W_p\) occurs to the first power.

There are, however, intermediate alternatives. For \(m>2\), define
\[
L_m=\int\eta^2a^{m-2}F^m.
\]
The same support algebra and Hölder exponents
\[
m,\qquad \frac{m}{m-2},\qquad m
\]
give
\[
R_p
\le L_m^{1/m}H_p^{(m-2)/m}\|z_p\|_4^{4/m}.
\]
Consequently,
\[
qR_p
\le\varepsilon\mathcal W_p+
C_{m,\varepsilon}
q^{m/(m-2)}
\mathcal S^{2/(m-2)}
L_m^{1/(m-2)}H_p.
\]
Thus every fixed \(m>2\) produces a Grönwall multiplier rather than \(q\gamma\mathcal W_p\).

For \(2<m<3\),
\[
L_m\le K_2^{\,3-m}Y^{\,m-2},
\]
so these interpolated estimates use the same \(K_2\)-to-\(Y\) curvature information but incur the larger power
\[
q^{m/(m-2)}>q^3.
\]
The choice \(m=3\) is therefore the most efficient member of this family using only \(K_2\) and \(Y\).

A second concrete route uses the curvature endpoint from Step 38:
\[
R_p
=\int(aF)\,\eta^2a^{p-2}s^q
\le\|aF\|_\infty H_p.
\]
On a dyadic slab \([t/2,t]\),
\[
CqR_p\le Cp\,\frac{\gamma}{t}H_p.
\]
This also avoids \(p\)-dependent smallness and has only linear \(p\)-growth, but it uses the completed curvature Moser endpoint rather than \(Y\) directly.

Hence the precise structural statement is:

- the \(K_2\)-only two-factor power estimate leaves \(q\gamma\) multiplying the gradient energy;
- any weighted curvature integrability above exponent \(2\), including \(Y=L_3\), converts the reaction into a Grönwall multiplier;
- the \(m=3\) identity is the simplest and most efficient route from the quantities already present before invoking \(\|aF\|_\infty\).

## 6. Absence of an \(E\)-independent additive term

Every right-hand contribution retains defect factors:

- reaction:
  \[
  aFs,\quad as;
  \]
- first cutoff derivatives:
  \[
  |\nabla a|\,s^{1/2}|\nabla E|;
  \]
- Hessian cutoff:
  \[
  (\nabla^2a):B_{\rm def},\qquad B_{\rm def}=O(s);
  \]
- metric norm variation:
  \[
  a\,E*E*E;
  \]
- volume variation:
  \[
  -a\tau s^q,\qquad |\tau|\le Cs^{1/2};
  \]
- cutoff Young remainders:
  multiples of \(H_p\).

The favorable principal term contains \(|\nabla E|^2\) and remains on the dissipative side. Although \(F=(1+|\mathrm{Rm}|^2)^{1/2}\) contains \(1\), it always appears multiplied by \(s^q\) in \(R_p\).

A constant additive term could arise from either:

1. replacing \(s\) by \(s+\varepsilon^2\) and retaining an \(\varepsilon\)-term after passage to \(\varepsilon=0\); or
2. estimating the Hessian tensor as \(B_{\rm def}=O(1+s)\) rather than using its exact quadratic formula.

Neither occurs here. Since
\[
B_{\rm def}\big|_{E=0}=0
\]
and the unregularized chain rule is exact, the assembled inequality is homogeneous in the defect. In particular, if \(E\equiv0\), then \(H_p\equiv0\) and every right-hand term in (4.13) and (7.6) vanishes.

## Conclusion

Theorem 7.1 is supported by the supplied tensor identities and energy algebra. The real-exponent regularity, Hessian-\(a\) exponents, \(p\)-uniform gradient comparison, three-factor Hölder identity, and absence of an additive defect-free term are all correct. The only substantive wording adjustment is that the three-factor route is not unique: it is the \(m=3\) member of a broader interpolation family and can also be replaced, after curvature smoothing, by the direct potential estimate using \(\|aF\|_\infty\).
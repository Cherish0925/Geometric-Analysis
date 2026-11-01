# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md"
  ]
}
```

## Task

Audit the defect Moser endpoint for the restricted four-dimensional cutoff flow ∂_t g = -2aE, a=χ², E=Ric+g. The claimed endpoint is: J₆(t) = ∫η²a⁴|E|⁶ satisfies J₆(t) ≤ e^{C(1+r^{-2})t}J₆(0) (no curvature or Y input), and then a nested Moser iteration from seed J₆ gives ‖aE(t)‖_∞ ≤ Cδ(r²/t)^{1/3}. Read the Step 34 derivation (A01) and the A03 Step 56 base-pair note. Test adversarially for GAPS: (1) Does the defect J_p energy inequality really close with only the γ-smallness condition, or is there a hidden dependence on the curvature Y or ∫Y estimate (which would create a circular dependency with the curvature branch)? Check the reaction estimate in Step 33 §4 (eq 4.1-4.4): it bounds R_p^E = ∫a^{p-1}Ff_ε^p by εD_p^E + C S²Y J_p using a THREE-factor Hölder (aF³)^{1/3}(a^{p-2}f^p)^{1/3}z̃^{4/3}. Is this legitimate, or can the two-factor w₆ route in Step 34 §5 avoid Y entirely? The Step 34 route absorbs P₆=∫Fw₆² by Cγ(X₆+r^{-2}J₆) using Hölder with (K₂^η)^{1/2} as the F L² norm — verify this works and determine whether the defect endpoint is truly independent of Y. (2) Does the Moser iteration from the J₆ seed to ‖aE‖_∞ need a defect energy inequality for all p≥6, and if so, does THAT higher-p inequality require Y or γ? Can it be run with only two-factor absorption using w_p = ηa^{(p-1)/2}s^{p/4}? (3) The endpoint ‖aE(t)‖_∞ ≤ Cδ(r²/t)^{1/3}: check the exponent 1/3 and the volume cancellation. J₆(0) ≤ Cδ⁶V; the Moser iteration has Sobolev factors S^{2/p₀} with p₀=6, giving S^{1/3} ~ (r²V^{-1/2})^{1/3} = r^{2/3}V^{-1/6}. Verify the final bound is V-independent. (4) Is the nested Moser recurrence from 'Step 32/A03 Step 34' (eq 6.1) actually established anywhere, or is it cited? The general form ‖af(t)‖_∞ ≤ C S^{2/p₀}t^{-3/p₀}(∫_{t/2}^t H_{p₀})^{1/p₀} — check whether this needs only the energy inequality at each level plus Sobolev. (5) The Step 33 defect reaction (eq 4.3) vs the Step 34 two-factor P₆ absorption: these are different estimates. Determine which is actually used in the final J₆ persistence, and whether the Moser iteration needs the other one. Be explicit about every gap found and what it changes about the theorem status.

## Output

## Memo: examination of the defect \(J_6\) endpoint and its Moser consequence

**Material examined:**  
- `Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md`, especially §5–§6.  
- `Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md`, especially §4.  
- `Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md`.  

The object is the defect energy
\[
J_6(t)=\int \eta^2 a^4 |E|^6\,d\mu_t,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\]
for the four-dimensional cutoff flow
\[
\partial_t g=-2aE,
\]
and the proposed endpoint
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0),
\]
followed by a Moser estimate
\[
\|aE(t)\|_\infty\le C\delta\left(\frac{r^2}{t}\right)^{1/3},
\]
assuming \(\|E(0)\|_\infty\le\delta\) on the selected support.

The central conclusion of this examination is:

1. The **two-factor \(J_6\) absorption in Step 34 §5 is algebraically sound** and gives a \(Y\)-free \(J_6\) persistence estimate, provided the tensor evolution, signed Hessian absorption, Sobolev comparability, localized \(L^2\) curvature control, and the smallness of \(\gamma\) are available on the first-exit interval.

2. The estimate is **not curvature-free**: it uses the localized curvature \(L^2\) quantity \(K_2^\eta\) through \(\gamma={\mathcal S}(0)(K_2^\eta(0))^{1/2}\). What it avoids is the cubic curvature moment
   \[
   Y=\int \eta^2 aF^3
   \]
   and its time integral.

3. The **Moser endpoint is not yet fully established by the supplied notes**. The missing mathematical substance is not the \(J_6\) absorption itself, but: a general-\(p\) two-factor defect inequality, the precise definition and proof of the nested Moser recurrence, the time-factor needed for the exponent \(1/3\), and the index-level defect evolution/signed-Hessian estimates.

The rest of this memo details these points.

---

## 1. The \(J_6\) inequality and the two-factor absorption

Step 34 §5 gives the formal differential inequality
\[
J_6' + cX_6 \le C(1+r^{-2})J_6 + CP_6,
\tag{1.1}
\]
where
\[
X_6=\int \eta^2 a^5 |E|^4|\nabla E|^2,
\qquad
P_6=\int \eta^2 a^5 F |E|^6,
\]
and
\[
F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

The only term that can introduce curvature beyond the defect itself is \(P_6\). Step 34 introduces
\[
w_6=\eta a^{5/2}s^{3/2}=\eta\chi^5|E|^3,
\qquad s=|E|^2,
\]
so that
\[
w_6^2=\eta^2 a^5 s^3=\eta^2 a^5|E|^6,
\]
and therefore
\[
P_6=\int Fw_6^2.
\]

Hölder gives
\[
P_6\le \|F\|_{L^2(\operatorname{supp} w_6)}\|w_6\|_{L^4}^2.
\tag{1.2}
\]

Because the cutoff arrangement assumes \(\eta=1\) on \(\operatorname{supp} a\) and \(a=0\) on \(\operatorname{supp} d\eta\), the support of \(w_6\) lies inside the region where \(\eta=1\). Hence
\[
\|F\|_{L^2(\operatorname{supp} w_6)}
\le
\left(\int \eta^2F^2\right)^{1/2}
=
(K_2^\eta)^{1/2}.
\]

The Sobolev convention is
\[
\|w_6\|_4^2
\le {\mathcal S}\left(\|\nabla w_6\|_2^2+r^{-2}\|w_6\|_2^2\right).
\tag{1.3}
\]

Now compute the gradient. Since
\[
w_6=\eta a^{5/2}s^{3/2},
\]
we have formally
\[
\nabla w_6
=
(\nabla\eta)a^{5/2}s^{3/2}
+\eta \frac52 a^{3/2}(\nabla a)s^{3/2}
+\eta a^{5/2}\frac32 s^{1/2}\nabla s.
\]

The first term is inactive because \(a=0\) on \(\operatorname{supp}d\eta\). For the second term,
\[
a^3|\nabla a|^2s^3
=
a^4\frac{|\nabla a|^2}{a}s^3
=
4a^4|\nabla\chi|^2s^3
\le Cr^{-2}a^4s^3,
\]
so it contributes at most \(Cr^{-2}J_6\). For the third term,
\[
a^5s|\nabla s|^2
\le
4a^5s^2|\nabla E|^2,
\]
using \(|\nabla s|^2\le 4s|\nabla E|^2\). This contributes at most \(CX_6\). Thus
\[
\|\nabla w_6\|_2^2
\le C(X_6+r^{-2}J_6),
\qquad
\|w_6\|_2^2\le J_6.
\tag{1.4}
\]

Combining (1.2)–(1.4),
\[
P_6
\le
C(K_2^\eta)^{1/2}{\mathcal S}(X_6+r^{-2}J_6).
\tag{1.5}
\]

On the first-exit interval one provisionally has
\[
{\mathcal S}(t)\le 2{\mathcal S}(0),
\qquad
K_2^\eta(t)\le C K_2^\eta(0),
\]
so
\[
{\mathcal S}(t)(K_2^\eta(t))^{1/2}
\le C{\mathcal S}(0)(K_2^\eta(0))^{1/2}
=C\gamma.
\]

Therefore
\[
P_6\le C\gamma(X_6+r^{-2}J_6).
\tag{1.6}
\]

If \(C\gamma<c/2\), the \(X_6\) part is absorbed into the left side of (1.1), giving
\[
J_6'+c'X_6\le C(1+r^{-2})J_6,
\]
and hence
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
\tag{1.7}
\]

This is the two-factor route. It does not use
\[
Y=\int \eta^2aF^3.
\]

### Hidden dependence

The estimate does use curvature through \(K_2^\eta\). The small parameter is
\[
\gamma={\mathcal S}(0)(K_2^\eta(0))^{1/2}.
\]

At a good support with \(K_2^\eta(0)\le K_0V\) and \({\mathcal S}(0)\simeq r^2V^{-1/2}\),
\[
\gamma\lesssim r^2\sqrt{K_0},
\]
so the volume factor cancels. This cancellation is essential for sequence-uniform constants.

Thus the correct statement is:

- \(J_6\) persistence is independent of the cubic curvature moment \(Y\) and of the integrated potential \(B(t)=\int_0^t{\mathcal S}^2Y\).
- It is not independent of curvature altogether; it requires the localized \(L^2\) curvature seed \(K_2^\eta\) and the smallness of \(\gamma\).

---

## 2. Relation to the \(q=2\) curvature estimate and absence of circularity with \(Y\)

The localized \(q=2\) curvature estimate in Step 34 §3 has the form
\[
(K_2^\eta)' + cD_2^\eta
\le CY + Cr^{-2}K_2^\eta.
\tag{2.1}
\]

The interpolation used there is
\[
Y=\int \eta^2aF^3
=
\int (\eta F)(\chi F)^2
\le (K_2^\eta)^{1/2}\|\chi F\|_4^2.
\]

Sobolev gives
\[
\|\chi F\|_4^2
\le C{\mathcal S}(D_2^\eta+r^{-2}K_2^\eta),
\]
and therefore, on the first-exit interval,
\[
Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta).
\tag{2.2}
\]

For \(C\gamma\) small, the \(D_2^\eta\) contribution is absorbed into (2.1), yielding
\[
\sup_{s\le t}K_2^\eta(s)+\int_0^tD_2^\eta(s)\,ds
\le C K_2^\eta(0),
\qquad t\le \theta r^2.
\tag{2.3}
\]

This is the ingredient that keeps
\[
{\mathcal S}(t)(K_2^\eta(t))^{1/2}
\]
under control.

Important point: the \(q=2\) estimate contains \(Y\), but it closes \(Y\) algebraically through (2.2). It does not require the separately proved \(q=3\) propagation of \(Y\), nor does it require the integrated potential \(B(t)\). Therefore the two-factor \(J_6\) estimate does not create a circular dependence with the curvature \(q=3\) branch.

The dependence structure is:

\[
K_2^\eta \text{ and } \gamma
\quad\Longrightarrow\quad
\text{absorption of }P_6
\quad\Longrightarrow\quad
J_6 \text{ persistence}.
\]

There is no arrow from \(J_6\) back to \(Y\), and no need for
\[
\int_0^t{\mathcal S}^2Y
\]
in the \(J_6\) persistence argument as written in Step 34.

---

## 3. Step 33 three-factor estimate versus Step 34 two-factor estimate

Step 33 §4 uses the regularized defect \(f_\varepsilon=(|E|^2+\varepsilon)^{1/2}\) and writes the defect reaction as
\[
R_p^E=\int a^{p-1}Ff_\varepsilon^p.
\]

It then uses the three-factor identity
\[
a^{p-1}Ff_\varepsilon^p
=
(aF^3)^{1/3}
(a^{p-2}f_\varepsilon^p)^{1/3}
\left(a^{(p-1)/2}f_\varepsilon^{p/2}\right)^{4/3}.
\tag{3.1}
\]

Hölder with exponents \((3,3,3)\), Sobolev, and Young give
\[
R_p^E
\le
\varepsilon D_p^E
+
C_\varepsilon p^N{\mathcal S}^2YJ_p.
\tag{3.2}
\]

This is algebraically legitimate. It produces a Gronwall coefficient involving
\[
{\mathcal S}^2Y.
\]

If one uses this route, then one needs control of
\[
\int_0^T{\mathcal S}^2Y\,ds,
\]
which is precisely the integrated potential \(B(T)\). Step 34 §3 gives
\[
B(T)\le C\gamma^3,
\]
but that connects the defect estimate to the curvature branch.

The Step 34 two-factor estimate is different. It uses
\[
P_6=\int Fw_6^2
\]
and Hölder with exponents \((2,4,4)\), not \((3,3,3)\). It replaces the cubic curvature moment \(Y\) by the \(L^2\) curvature seed \(K_2^\eta\). For \(p=6\), this is sharper and simpler.

Therefore:

- The three-factor estimate in Step 33 is valid but not the route used in the final Step 34 \(J_6\) persistence argument.
- The final \(J_6\) persistence estimate uses the two-factor \(P_6\) absorption.
- If one wants a Moser iteration that remains independent of \(Y\), one needs the analogous two-factor absorption for all higher exponents, not the Step 33 three-factor family.

---

## 4. Higher-\(p\) defect inequalities needed for Moser iteration

The Moser endpoint
\[
\|aE(t)\|_\infty\le C\delta\left(\frac{r^2}{t}\right)^{1/3}
\]
cannot follow from the \(p=6\) inequality alone. One needs a family of defect inequalities for exponents \(p\ge 6\), or at least for a dyadic sequence \(p_k\to\infty\).

Define, for even \(p\ge6\),
\[
J_p=\int \eta^2 a^{p-2}s^{p/2}
=
\int \eta^2 a^{p-2}|E|^p,
\]
\[
D_p^E=\int \eta^2 a^{p-1}s^{p/2-1}|\nabla E|^2,
\]
and
\[
w_p=\eta a^{(p-1)/2}s^{p/4}
=
\eta a^{(p-1)/2}|E|^{p/2}.
\]

Then
\[
w_p^2=\eta^2a^{p-1}s^{p/2},
\]
and the natural reaction term is
\[
P_p=\int \eta^2a^{p-1}Fs^{p/2}
=
\int Fw_p^2.
\]

Exactly the same Hölder/Sobolev argument gives
\[
P_p
\le
\|F\|_{L^2}\|w_p\|_4^2
\le
C(K_2^\eta)^{1/2}{\mathcal S}
\left(\|\nabla w_p\|_2^2+r^{-2}\|w_p\|_2^2\right).
\tag{4.1}
\]

The gradient estimate now carries \(p\)-dependent constants:
\[
\|\nabla w_p\|_2^2
\le
C p^2(D_p^E+r^{-2}J_p).
\tag{4.2}
\]

Indeed:

- derivative of \(s^{p/4}\) gives a factor \(p\) and produces
  \[
  a^{p-1}s^{p/2-1}|\nabla E|^2,
  \]
  which is \(D_p^E\);

- derivative of \(a^{(p-1)/2}\) gives a factor \(p\) and produces
  \[
  p^2a^{p-3}|\nabla a|^2s^{p/2}
  \le
  Cp^2r^{-2}a^{p-2}s^{p/2}
  =
  Cp^2r^{-2}J_p;
  \]

- derivative of \(\eta\) is again inactive because \(a=0\) on \(\operatorname{supp}d\eta\).

Thus
\[
P_p
\le
Cp^2\gamma_t(D_p^E+r^{-2}J_p),
\qquad
\gamma_t={\mathcal S}(t)(K_2^\eta(t))^{1/2}.
\tag{4.3}
\]

On the first-exit interval,
\[
\gamma_t\le C\gamma.
\]

The defect equation and the chain rule for \(s^{p/2}\) should give a principal dissipative term of size
\[
c p^2D_p^E.
\]

Therefore, if \(C\gamma\) is small, one obtains the higher-\(p\) family
\[
J_p' + c p^2D_p^E
\le
Cp^N(1+r^{-2})J_p.
\tag{4.4}
\]

This is the form needed for a Moser iteration that does not involve \(Y\).

### Current status of this ingredient

Step 34 proves this two-factor absorption only for \(p=6\). Step 33 proves a \(p\)-family, but with the three-factor \(Y\)-dependent absorption. The supplied notes do not contain the explicit general-\(p\) two-factor inequality (4.4).

The algebra above indicates that the extension is natural and likely correct, but it is not yet written as a proved module. The missing pieces are:

- the general-\(p\) defect evolution at the index level;
- the signed Hessian absorption for general \(p\);
- the precise \(p\)-dependent constants;
- verification that the \(p^N\) constants are summable in the Moser sequence.

Until that is supplied, the Moser iteration from \(J_6\) to \(L^\infty\) is conditional.

---

## 5. The exponent \(1/3\) and volume cancellation

The proposed endpoint is
\[
\|aE(t)\|_\infty
\le
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\tag{5.1}
\]

Step 34 quotes the nested Moser recurrence
\[
\|af(t)\|_\infty
\le
C{\mathcal S}^{2/p_0}t^{-3/p_0}
\left(
\int_{t/2}^t H_{p_0}(f,s)\,ds
\right)^{1/p_0}.
\tag{5.2}
\]

For the defect, \(p_0=6\). Then
\[
{\mathcal S}^{2/p_0}={\mathcal S}^{1/3}.
\]

Using
\[
{\mathcal S}\simeq r^2V^{-1/2},
\]
we get
\[
{\mathcal S}^{1/3}\simeq r^{2/3}V^{-1/6}.
\]

The initial defect bound is
\[
J_6(0)\le C\delta^6V.
\]

If the lower-order seed in (5.2) satisfies
\[
\int_{t/2}^t H_6(s)\,ds
\le
CtJ_6(0)
\le
Ct\delta^6V,
\tag{5.3}
\]
then
\[
\left(
\int_{t/2}^t H_6
\right)^{1/6}
\le
C\delta V^{1/6}t^{1/6}.
\]

Substituting into (5.2),
\[
\|aE(t)\|_\infty
\le
C
r^{2/3}V^{-1/6}
t^{-1/2}
\delta V^{1/6}t^{1/6}
=
C\delta r^{2/3}t^{-1/3}.
\]

Equivalently,
\[
\|aE(t)\|_\infty
\le
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]

Thus the volume factor cancels:
\[
V^{-1/6}V^{1/6}=1.
\]

This is the expected four-dimensional parabolic scaling from an \(L^6\) seed:
\[
t^{-n/(2p)}=t^{-4/(12)}=t^{-1/3}.
\]

### Important dependence on the meaning of \(H_6\)

The exponent \(1/3\) requires the time factor \(t^{1/6}\) coming from (5.3). This is natural if \(H_6\) is a lower-norm quantity such as \(J_6\) itself, or a quantity comparable to \(J_6\) on the slab. Since \(J_6(t)\le C J_6(0)\), one then has
\[
\int_{t/2}^t J_6(s)\,ds\le CtJ_6(0).
\]

If, however, \(H_6\) is only the dissipation \(X_6\), then the energy inequality gives
\[
\int_{t/2}^t X_6(s)\,ds\le CJ_6(0),
\]
without the factor \(t\). In that case (5.2) would yield a time exponent \(t^{-1/2}\), not \(t^{-1/3}\).

The supplied notes do not explicitly define \(H_{p_0}\). Therefore the exponent \(1/3\) is consistent with the quoted recurrence only if \(H_6\) includes, or is comparable to, a time-integrated lower norm such as \(J_6\). The precise definition of \(H_6\) and the proof of the recurrence must make this explicit.

The drift integral also depends on this exponent. With \(t^{-1/3}\),
\[
\int_0^T\|aE(t)\|_\infty\,dt
\le
C\delta r^{2/3}\int_0^T t^{-1/3}\,dt
=
C\delta r^{2/3}T^{2/3}.
\]
For \(T=\theta r^2\),
\[
\int_0^T\|aE(t)\|_\infty\,dt
\le
C\delta\theta^{2/3}r^2.
\]
This is the scaling used for metric drift. If the endpoint instead had \(t^{-1/2}\), the drift scaling would be different.

---

## 6. Status of the nested Moser recurrence

The recurrence
\[
\|af(t)\|_\infty
\le
C{\mathcal S}^{2/p_0}t^{-3/p_0}
\left(
\int_{t/2}^t H_{p_0}(f,s)\,ds
\right)^{1/p_0}
\tag{6.1}
\]
is cited in Step 34 as coming from Step 32 / A03 Step 34. In the supplied documents, it is not rederived.

Mathematically, such a recurrence should follow from:

1. the defect energy inequalities for a sequence of exponents \(p_k\ge6\);
2. the Sobolev inequality
   \[
   \|w\|_4^2\le {\mathcal S}(\|\nabla w\|_2^2+r^{-2}\|w\|_2^2);
   \]
3. nested time slabs, e.g.
   \[
   t=t_0>t_1>t_2>\cdots,
   \]
   with time-cutoff derivatives producing powers of \(t^{-1}\);
4. uniform control of the zero-order coefficient
   \[
   C(1+r^{-2})
   \]
   on the slab;
5. summability of the \(p\)-dependent constants.

If the general-\(p\) two-factor inequalities (4.4) are available, the recurrence should not need \(Y\). It would need only the localized \(L^2\) curvature seed through \(\gamma\), the Sobolev constant, and the cutoff geometry.

But in the supplied record, the recurrence is an external citation. The exact definition of \(H_{p_0}\), the time-cutoff construction, and the dependence on \(p\) are not displayed. This is one of the principal unresolved pieces needed to turn the \(J_6\) persistence into the stated \(L^\infty\) endpoint.

---

## 7. Role of A03 Step 56

A03 Step 56 concerns a positive-time continuation block for a related weighted curvature system. It establishes a pattern:

\[
T_0\in \bigcap_{q<\infty}L^q
\Longrightarrow
(U_1,C_2)\in \bigcap_{q<\infty}L^q
\Longrightarrow
T_1\in \bigcap_{q<\infty}L^q,
\]
using signed Hessian absorption and without dividing by \(a\).

Its universal signed-Hessian estimate has the form
\[
|H_p(Y)|
\le
\epsilon\int a|\nabla Y|^2|Y|^{p-2}
+
C_{p,\epsilon}\|d\chi\|_\infty^2\|Y\|_p^p.
\tag{7.1}
\]

This is structurally relevant to the defect calculation because Step 34 also needs signed integration by parts for Hessian-\(a\) terms of the form
\[
\int \eta^2a^4(\nabla^2a)*B(E),
\]
with
\[
|B|\le C|E|^2,
\qquad
|\nabla B|\le C|E||\nabla E|.
\]

The A03 Step 56 estimate supports the mechanism: Hessian cutoff terms can be absorbed using the available weighted dissipation, without pointwise bounds on \(\nabla^2a\) and without division by \(a\).

However, A03 Step 56 does not itself prove the \(J_6\) persistence from \(t=0\). It works on a positive-time slab \([\tau,T_*)\) with \(\tau>0\), assumes a weighted \(L^\infty\) bound, and addresses continuation/restart near the cutoff collar. It does not supply:

- the \(q=2\) curvature seed;
- the smallness of \(\gamma\);
- the \(J_6\) Gronwall estimate from initial time;
- the higher-\(p\) two-factor defect inequalities;
- the Moser recurrence.

Thus Step 56 is consistent with and supportive of the signed-Hessian part of the defect estimate, but it does not close the defect Moser endpoint.

---

## 8. Specific answers to the five questions

### (1) Does the defect \(J_p\) energy inequality close with only \(\gamma\)-smallness?

For \(p=6\), the two-factor route in Step 34 closes the absorption of \(P_6\) using only
\[
\gamma_t={\mathcal S}(t)(K_2^\eta(t))^{1/2}
\]
and the smallness of \(\gamma\). It does not use \(Y\) or \(\int Y\).

It is not independent of curvature entirely: it uses the localized curvature \(L^2\) quantity \(K_2^\eta\). The \(q=2\) estimate used to keep \(K_2^\eta\) under control contains \(Y\), but \(Y\) is controlled algebraically through
\[
Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta),
\]
so no \(q=3\) propagation or integrated \(Y\)-potential is needed.

The two-factor \(w_6\) route is legitimate under the cutoff support assumptions and the Sobolev first-exit comparability. The three-factor route in Step 33 is also legitimate but gives a different, \(Y\)-dependent estimate.

### (2) Does Moser need a defect inequality for all \(p\ge6\)? Can it avoid \(Y\)?

Yes, the Moser iteration requires inequalities for a sequence of exponents tending to infinity.

The two-factor method extends algebraically. For even \(p\ge6\), set
\[
w_p=\eta a^{(p-1)/2}s^{p/4}.
\]
Then
\[
P_p=\int Fw_p^2
\le
Cp^2\gamma_t(D_p^E+r^{-2}J_p).
\]

If the defect evolution supplies principal dissipation \(cp^2D_p^E\), then small \(\gamma\) gives
\[
J_p'+cp^2D_p^E
\le
Cp^N(1+r^{-2})J_p.
\]

This contains no \(Y\). The missing part is that this general-\(p\) two-factor inequality is not explicitly proved in the supplied notes. Step 34 proves only \(p=6\); Step 33 proves a general-\(p\) inequality but with \(Y\).

### (3) Is the exponent \(1/3\) and the volume cancellation correct?

The volume cancellation is correct:
\[
{\mathcal S}^{1/3}(J_6(0))^{1/6}
\simeq
(r^2V^{-1/2})^{1/3}(\delta^6V)^{1/6}
=
\delta r^{2/3}.
\]

The exponent \(1/3\) is correct if the seed in the Moser recurrence satisfies a time-integrated lower-norm bound
\[
\int_{t/2}^t H_6(s)\,ds\le Ct\delta^6V.
\]

Then
\[
t^{-3/6}(t\delta^6V)^{1/6}
=
t^{-1/2}t^{1/6}\delta V^{1/6}
=
\delta t^{-1/3}V^{1/6},
\]
and the \(V^{1/6}\) cancels against \({\mathcal S}^{1/3}\).

If \(H_6\) is only dissipation and gives no factor of \(t\), then the quoted recurrence would produce \(t^{-1/2}\), not \(t^{-1/3}\). Therefore the definition of \(H_6\) and the proof of the recurrence must explicitly show the time factor.

### (4) Is the nested Moser recurrence established?

In the supplied notes, it is cited from Step 32 / A03 Step 34, not rederived.

It is plausible that it needs only:

- the energy inequality at each exponent;
- the Sobolev inequality;
- nested time cutoffs;
- uniform control of the zero-order coefficient.

But the supplied record does not display the recurrence proof, the definition of \(H_{p_0}\), or the \(p\)-constant bookkeeping. This remains an unresolved ingredient.

### (5) Which defect reaction estimate is actually used?

The final \(J_6\) persistence in Step 34 uses the two-factor estimate
\[
P_6\le C\gamma(X_6+r^{-2}J_6).
\]

It does not use the Step 33 three-factor estimate
\[
R_p^E\le \epsilon D_p^E+C_\epsilon p^N{\mathcal S}^2YJ_p.
\]

For the Moser iteration:

- If the general-\(p\) two-factor inequality is proved, the Moser iteration can avoid \(Y\).
- If one instead uses the Step 33 general-\(p\) inequality, then the Moser iteration inherits a dependence on \(Y\) and needs control of \(\int{\mathcal S}^2Y\).

Thus the two routes are not interchangeable. The \(Y\)-free endpoint depends on supplying the general-\(p\) two-factor route.

---

## 9. Net effect on the theorem status

The Step 34 \(J_6\) persistence module is mathematically coherent under the following explicit premises:

1. The defect evolution contains the principal dissipative term
   \[
   -2a|\nabla E|^2
   \]
   and reaction terms bounded by
   \[
   CaF|E|^2+Ca|E|^2.
   \]

2. The signed Hessian-\(a\) terms satisfy the derivative structure
   \[
   |B|\le C|E|^2,
   \qquad
   |\nabla B|\le C|E||\nabla E|,
   \]
   allowing absorption into \(X_6\).

3. The cutoffs satisfy
   \[
   \eta=1 \text{ on } \operatorname{supp}a,
   \qquad
   a=0 \text{ on } \operatorname{supp}d\eta,
   \qquad
   |\nabla\chi|^2\le Cr^{-2}.
   \]

4. The Sobolev constant and localized curvature energy remain comparable on the first-exit interval:
   \[
   {\mathcal S}(t)\le C{\mathcal S}(0),
   \qquad
   K_2^\eta(t)\le CK_2^\eta(0).
   \]

5. The smallness condition
   \[
   C\gamma<c
   \]
   holds.

Under these premises,
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0)
\]
is supported by the two-factor absorption and is independent of \(Y\).

The stronger endpoint
\[
\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}
\]
requires additional material not fully contained in the supplied notes:

- a general-\(p\) two-factor defect inequality;
- a proof of the nested Moser recurrence, including the definition of \(H_p\);
- verification that the time seed gives the factor \(t\) needed for the exponent \(1/3\);
- completion of the index-level defect evolution and signed Hessian estimates;
- closure of the simultaneous first-exit interval carrying \({\mathcal S}\), \(K_2^\eta\), \(J_6\), and metric comparability.

With those pieces supplied, the defect branch can be run without invoking the curvature \(q=3\) moment \(Y\). Without them, the \(J_6\) persistence is a conditional fixed-exponent module, and the Moser endpoint remains an open part of the argument.
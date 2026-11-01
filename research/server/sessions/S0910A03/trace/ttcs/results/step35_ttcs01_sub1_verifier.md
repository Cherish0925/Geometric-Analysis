# TTCS Independent Branch Record

```json
{
  "step_id": 35,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md",
    "Sessions/S0910A03/workspace/notes/step34_exact_defect_J6_lemma.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A03/workspace/scripts/verify_step35_defect_algebra.py",
    "Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md"
  ]
}
```

## Task

Verify the unregularized J_6 defect persistence lemma in the companion note. The flow is ∂_t g = -2χ²(Ric+g) on a closed 4-manifold with a fixed smooth cutoff χ. The key claims to check:

1. REGULARITY: s = |E|² is smooth, s³ is smooth, and the Sobolev variable w₆ = ηχ⁵|E|³ = ηa^{5/2}s^{3/2} is C¹ with bounded gradient. No ε-regularization is needed.

2. EXACT CHAIN RULE: (∂_t - aΔ)s³ = 3s²(∂_t - aΔ)s - 6as|∇s|², with the extra term nonpositive.

3. HESSIAN-a TENSOR IBP: The integrated identity (Step 34 eq 2.4) is tested with q = 3η²a⁴s². The resulting tensor B^{ij} = 2g^{ij}|E|² + 2τE^{ij} - 4E^{ik}E_k^j is QUADRATIC in E (vanishes at E=0), so this is not a bare curvature source. The IBP moves one derivative from ∇²a onto the smooth test weight, producing only terms of the structure εX₆ + C r⁻²J₆. Check that this honest tensor IBP is valid (no IBP on |∇²a|) and that all three branches of the product rule land on the claimed weight exponents.

4. TWO-FACTOR HÖLDER: The defect potential P₆ = ∫Fw₆² is absorbed by P₆ ≤ ‖F‖₂‖w₆‖₄² ≤ γ(X₆ + r⁻²J₆) with γ = S·K₂^{1/2}. This uses ONLY ‖F‖₂, NOT Y = ∫aF³. Verify that this is correct because the defect reaction integrand is aF|E|² (linear in F), unlike the curvature reaction aF³ (cubic in F). Is there any hidden cubic term that would require Y?

5. FINAL GRONWALL: J₆' ≤ C(1+r⁻²)J₆ with no time-dependent coefficient. Compare with A01's route using ∫S²Y ≤ Cγ³. Which is correct? Are they compatible?

6. Are there any terms in the defect evolution that have been dropped or underbounded?

## Output

## Scientific verification memo: unregularized \(J_6\) defect persistence lemma

### Bottom line

The unregularized \(J_6\) mechanism is mathematically sound **provided several textual exponent slips in Step 35 §3.5–§3.6 are corrected**. With the corrected powers, every cutoff and Hessian-\(a\) term has the form  
\[
\varepsilon X_6+C_\varepsilon r^{-2}J_6,
\]
and the potential term satisfies the sharper two-factor estimate
\[
P_6\le C\gamma\,(X_6+r^{-2}J_6),
\qquad \gamma=\mathcal S K_2^{1/2}.
\]
No \(Y=\int aF^3\) input is needed for \(J_6\) persistence. The A01 three-factor route is a compatible but less direct estimate.

---

## 1. Regularity

For a smooth solution \(g(t)\), the tensor
\[
E=\operatorname{Ric}+g
\]
is smooth, hence
\[
s=|E|^2=g^{ik}g^{jl}E_{ij}E_{kl}
\]
is a smooth scalar. Therefore \(s^2,s^3\), and the test function
\[
q=3\eta^2a^4s^2
\]
are smooth. This removes the need for \(\varepsilon\)-regularization in the energy identity.

For the Sobolev variable
\[
w_6=\eta a^{5/2}s^{3/2}=\eta\chi^5|E|^3,
\]
one should use \(\chi\ge0\), as is standard for cutoffs. Then \(a^{5/2}=\chi^5\) is smooth. The map \(E\mapsto |E|^3\) is \(C^1\), with derivative \(3|E|\langle E,\cdot\rangle\), continuous at \(E=0\). Thus \(w_6\in C^1\), and on compact spacetime subintervals its gradient is bounded.

The gradient formula is
\[
\nabla w_6
=(d\eta)a^{5/2}s^{3/2}
+\frac52\eta a^{3/2}(da)s^{3/2}
+\frac32\eta a^{5/2}s^{1/2}\nabla s.
\]
The last term is continuous at \(E=0\), since
\[
s^{1/2}\nabla s
=2|E|\langle E,\nabla E\rangle .
\]
The \(d\eta\) term vanishes because \(a=0\) on \(\operatorname{supp}d\eta\). Hence \(w_6\) is an admissible \(W^{1,2}\) Sobolev test function.

---

## 2. Chain rule

The scalar identity is exact:
\[
(\partial_t-a\Delta)s^3
=3s^2(\partial_t-a\Delta)s-6as|\nabla s|^2.
\]
Since \(a=\chi^2\ge0\) and \(s\ge0\), the extra term is nonpositive:
\[
-6as|\nabla s|^2\le0.
\]

If
\[
(\partial_t-a\Delta)s=-2a|\nabla E|^2+\Sigma_s,
\]
then testing \(3s^2(-2a|\nabla E|^2)\) against \(\eta^2a^4\) gives the full tensor dissipation
\[
-6\int\eta^2a^5s^2|\nabla E|^2=-6X_6.
\]
This is the correct coercive term for absorbing cutoff-gradient products.

One sign correction: for the flow \(\partial_tg=-2aE\),
\[
\partial_t d\mu=-a\tau\,d\mu,\qquad \tau=\operatorname{tr}E.
\]
Step 35 §3.1 writes the opposite sign. The estimate is unchanged, since only
\[
\left|\int \eta^2a^5\tau s^3\right|
\le C\int\eta^2a^5Fs^3=CP_6
\]
is used.

---

## 3. Hessian-\(a\) tensor integration by parts

The Hessian contribution has the tensor form
\[
T_H=\int q\,a_{ij}B_0^{ij},
\]
where
\[
B_0^{ij}
=2g^{ij}|E|^2+2\tau E^{ij}-4E^{ik}E_k{}^j.
\]
This tensor is quadratic in \(E\):
\[
|B_0|\le Cs,\qquad |\nabla B_0|\le Cs^{1/2}|\nabla E|.
\]
Thus \(B_0=0\) at \(E=0\), so no curvature-only source is created.

The tensor-level integration by parts is
\[
\int q\,a_{ij}B_0^{ij}
=-\int a_j\nabla_i(qB_0^{ij}).
\]
No integration by parts is performed on \(|\nabla^2a|\). On the closed manifold, or with compactly supported buffered cutoffs, no boundary term remains. The \(d\eta\) branch vanishes because \(a=da=0\) on \(\operatorname{supp}d\eta\).

With
\[
q=3\eta^2a^4s^2,
\]
the three nonzero product-rule branches are:

### (i) Derivative hits \(a^4\)

\[
|da|\,|\nabla(a^4)|\,s^2\,|B_0|
\lesssim a^3|da|^2s^3.
\]
Using \(a=\chi^2\),
\[
a^3|da|^2=4a^4|d\chi|^2\le Cr^{-2}a^4,
\]
so
\[
\int a^3|da|^2s^3\le Cr^{-2}J_6.
\]

### (ii) Derivative hits \(s^2\)

\[
a^4|da|\,s|\nabla s|\,|B_0|
\lesssim a^4|da|\,s^2|\nabla s|
\lesssim a^4|da|\,s^{5/2}|\nabla E|.
\]
Young gives
\[
\int a^4|da|\,s^{5/2}|\nabla E|
\le \varepsilon X_6+C_\varepsilon r^{-2}J_6.
\]

### (iii) Derivative hits \(B_0\)

\[
a^4|da|\,s^2|\nabla B_0|
\lesssim a^4|da|\,s^{5/2}|\nabla E|,
\]
again giving
\[
\le \varepsilon X_6+C_\varepsilon r^{-2}J_6.
\]

So the corrected estimate is
\[
|T_H|\le \varepsilon X_6+C_\varepsilon r^{-2}J_6.
\]

### Textual exponent corrections in Step 35

Step 35 §3.5(i) writes an \(s^2\) density, but the correct density is \(s^3\).  
Step 35 §3.5(iii) and §3.6 write \(s^{3/2}\), but the correct cross term is
\[
a^4|da|s^{5/2}|\nabla E|.
\]
This correction is essential: the \(s^{5/2}\) term leaves exactly \(r^{-2}J_6\) after Young, whereas an \(s^{3/2}\) term would leave \(a^3|da|^2s\), which is not controlled by \(J_6\) alone.

The companion script’s exponent bookkeeping uses the corrected \(s^{5/2}\) power.

---

## 4. First-derivative cutoff terms

The raw \((\nabla a)*\nabla E\) terms in \(\mathcal C_a(E)\), after pairing with \(E\) and testing by \(3\eta^2a^4s^2\), have size
\[
C\int \eta^2a^4|da|\,s^{5/2}|\nabla E|.
\]
Thus
\[
\le \varepsilon X_6+C_\varepsilon r^{-2}J_6.
\]
Again the correct power is \(s^{5/2}\), not \(s^{3/2}\).

---

## 5. Two-factor Hölder absorption

The potential is
\[
P_6=\int \eta^2a^5Fs^3=\int Fw_6^2.
\]
Hölder gives
\[
P_6\le \|F\|_{L^2(\operatorname{supp}w_6)}\|w_6\|_4^2.
\]
Then the local Sobolev inequality gives
\[
\|w_6\|_4^2
\le \mathcal S\left(\|\nabla w_6\|_2^2+r^{-2}\|w_6\|_2^2\right).
\]
The gradient estimate is
\[
\|\nabla w_6\|_2^2
\le C(X_6+r^{-2}J_6),
\]
and
\[
\|w_6\|_2^2
=\int\eta^2a^5s^3
\le J_6.
\]
Therefore
\[
P_6\le C\mathcal S\|F\|_{L^2(\operatorname{supp}w_6)}
(X_6+r^{-2}J_6).
\]

To write this as
\[
P_6\le C\gamma(X_6+r^{-2}J_6),
\qquad \gamma=\mathcal S K_2^{1/2},
\]
the support relation must be stated precisely. If
\[
K_2=\int \eta^2F^2
\]
and \(\eta=1\) on \(\operatorname{supp}a\), then
\[
\|F\|_{L^2(\operatorname{supp}w_6)}\le K_2^{1/2},
\]
because \(w_6\) is supported where \(a\neq0\). This is the correct reason; it is not a consequence of merely \(a\le1\) and \(\eta\le1\).

---

## 6. No hidden cubic curvature term

The defect evolution differs from curvature evolution in the crucial way:

- Curvature energy has reaction \(a\,\operatorname{Rm}*\operatorname{Rm}*\operatorname{Rm}\), producing integrals of type
  \[
  \int a^{p-1}F^{p+1},
  \]
  and in dimension four this naturally invokes
  \[
  Y=\int aF^3.
  \]

- The defect equation is homogeneous in \(E\). The curvature reaction in the \(s=|E|^2\) equation has the form
  \[
  a\,\operatorname{Rm}*E*E,
  \]
  hence after testing:
  \[
  \int \eta^2a^5Fs^3=P_6.
  \]
  This is linear in \(F\), not cubic in \(F\).

Other terms are also harmless in this sense:

\[
|E|^3\le C Fs,\qquad |E|^2\le Cs,\qquad |\tau|\le C|E|\le CF.
\]
Cutoff terms are \(E*\nabla E*da\) or \(E*E*\nabla^2a\), and after tensor IBP they are absorbed by \(X_6\) and \(r^{-2}J_6\). No term of the form \(F^3\), \(F^2s\), or curvature-only source appears in the \(J_6\) energy identity.

---

## 7. Final Gronwall estimate

After assembling the energy terms,
\[
J_6'+cX_6
\le C(1+r^{-2})J_6+CP_6.
\]
Using
\[
P_6\le C\gamma(X_6+r^{-2}J_6),
\]
and assuming \(C\gamma<c/2\), one gets
\[
J_6'+\frac c2X_6
\le C(1+r^{-2})J_6.
\]
Thus
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
\]
There is no \(\mathcal S^2Y(t)\) coefficient in this route.

A01’s route using
\[
\int_0^T \mathcal S^2Y(t)\,dt\le C\gamma^3
\]
is compatible: it comes from the three-factor estimate
\[
P_6
\le \varepsilon X_6+C_\varepsilon\mathcal S^2Y\,J_6.
\]
That estimate is valid as an alternative interpolation, but it uses the curvature \(K_3\) seed. The two-factor \(L^2\)-curvature estimate is sharper for \(J_6\) because the defect reaction is only linear in \(F\).

---

## 8. Remaining textual repairs needed before citing the lemma

The mathematical mechanism is correct after these repairs:

1. Replace the Step 35 §3.5(i) density \(s^2\) by \(s^3\).
2. Replace the Step 35 §3.5(iii) and §3.6 cross terms \(s^{3/2}\) by \(s^{5/2}\).
3. Correct the volume-form sign:
   \[
   \partial_t d\mu=-a\tau\,d\mu.
   \]
4. State the \(K_2\) support relation precisely:
   \[
   \|F\|_{L^2(\operatorname{supp}w_6)}\le K_2^{1/2}
   \]
   because \(\eta=1\) on \(\operatorname{supp}a\).

With these corrections, no dropped defect-evolution term appears to force a \(Y=\int aF^3\) input, and the unregularized \(J_6\) persistence estimate is scientifically supported.
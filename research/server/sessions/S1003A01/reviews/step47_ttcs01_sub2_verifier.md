# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step47_o10_tn_core_free_at_energy_scale.md",
    "Sessions/S1003A01/workspace/notes/step46_o10_finite_marked_block_and_spinor_matching.md",
    "Sessions/S1003A01/workspace/data/step47/tn_core_exact.json",
    "Sessions/S1003A01/workspace/data/step47/tn_core_split.json",
    "Sessions/S1003A01/workspace/scripts/step47_tn_core_exact.py"
  ]
}
```

## Task

Check the mathematics of the Step-47 O10 note, which claims to reverse Step 46's main local conclusion. Setting (from the inherited corpus): s=-4 metric, actual Seiberg-Witten fields D_A^+Phi=0, F_A^+=2i sigma(Phi), nabla^*nabla Phi=(1-rho/2)Phi, cubic torsion t_Phi=sum_i c(e^i)Phi⊗(Phi∧nabla_i Phi) in E=S^-⊗L with determinant connection 3A, endpoint rho*=4/3, m*=128/81, a=sqrt2/3, corpus Weitzenböck relation (L-2)t=D*Dt+(Gamma-1)t-R t and Proposition 7: D^-t=-4 sum P_i⊗(Phi∧P_i)+K(W^+). Please verify or correct, with explicit reasoning: (a) identity (1.1) and its sign/normalization, and whether the Step-46 raw-TN residual q=-2v is truly just the omitted s/4 and F^-_{3A} Weitzenböck terms (so that it is not a candidate obstruction); (b) the exact TN claims: Phi_TN=sqrt(rho*)e1+a fbar e2 Dirac-harmonic with delta≡0, t=sqrt2 rho* a dfbar in Lambda^{0,1}_{I3}, |t|^2=m*/V; the GH two-form families and closedness criteria, h=x3/V; the mismatch (2.3) and its use; (c) formula (3.1) |N|^2=sin^2 s |nabla tau|^2 and whether J_+ selected by Phi_TN is as described; (d) whether the corpus commutator (3.8) can legitimately be applied on the physical block to give the critical lower bound (3.2) for ∫|∇N_tau|^2, and what hypotheses (closure, rho=rho*, type (1,1)) actually fail in a TN core; (e) whether the conditional reduction in §4.4 (density-free O10 follows from ||∇N_tau||_{2,av}->0) is sound or overreaching, and whether the residual count of §2 genuinely needs only a null background jet. Identify any error that would change the conclusion that a TN core carries no local order-L^6 payment at the energy scale. Give a direct mathematical memo.

## Output

# Memo: Step 47 (the TN core is free at the energy scale)

## Summary

The main correction to Step 46 holds. The raw-TN resolvent residual \(q=-2v\) is a curvature-omission artefact and is not an order-\(L^6\) obstruction.

The Step-47 argument has one structural gap. The exact TN data (\(\delta\equiv0\), \(D^-t=0\)) are computed with \(A=0\) on a Ricci-flat model. The same curvature that §1 restores in the second-order identity also enters the first-order quantities \(\delta\) and \(D^\pm\Phi\) at order \(r\). After one more derivative it enters \(D^{-*}\delta\) and \(q\) at order one, which is the energy scale. With a correctly stated hypothesis, the conclusion "TN core increment \(=o(L^6)\)" survives:

- the background must have a null **2-jet**, not a null 1-jet;
- the core must carry asymptotically zero determinant charge.

Several secondary statements need repair:

- the JSON self-duality flags;
- "\(K\) parallel";
- the constant \(C\) in (3.2);
- the arithmetic in §4.2;
- the strength of the §4.4 reduction.

A convention-free critical lower bound for \(\int|\nabla N_\tau|^2\) can be computed directly; it is given in §5 below.

---

## 1. Identity (1.1) and the status of \(q=-2v\)

Take the twisted Lichnerowicz formula on \(E=S^-\otimes L^{3/2}\) (determinant \(3A\)) in the normalization \(D^2=\nabla^*\nabla+\frac s4+\frac12c(F_B)\):
\[
\nabla^*\nabla t-2t=D^{-*}D^-t-\bigl(\tfrac s4+2\bigr)t-\tfrac12c(F^-_{3A})t\overset{s=-4}{=}D^{-*}D^-t-\bigl(1+\tfrac12c(F^-_{3A})\bigr)t .
\]
So (1.1) is correct as a pointwise identity for every section and every \(s=-4\) metric.

**Consistency check with the endpoint numbers.** At the endpoint \(F_A^-=\frac i3(e^{12}-e^{34})\). On \(S^-\) one has \(c(e^{12}-e^{34})=2c(e^{12})\), with eigenvalues \(\pm2i\). Hence
\[
\tfrac12c(F^-_{3A})=\tfrac32c(F_A^-)\quad\text{has eigenvalues}\quad \mp1 .
\]
The bracket \(1+\frac12c(F^-_{3A})\) therefore vanishes exactly on one eigenline. This is precisely the statement that the endpoint torsion is null for the resolvent. The decomposition of the model's "\(-2\)" is
\[
-2=\underbrace{(-1)}_{s/4\ \text{omitted}}+\underbrace{(-1)}_{\frac12 c(F^-_{3A})\ \text{omitted}},
\]
which is what §1 states. The note's sentence "\(-1+1\cdot0\) relative to the needed \(-2\)" is garbled; the line above is the correct accounting. Whether \(t\propto d\bar z_1\) lies on the correct eigenline is a sign convention (orientation of \(\Lambda^{0,1}\) versus the action of \(e^{12}-e^{34}\)) that must be matched with the corpus. It is not checked in Step 47.

**Small inconsistency between (1.3) and (1.1).** (1.3) writes \(q=-4D^{-*}\delta+(\Gamma-1)t\). From (1.1) the correct form is
\[
q=-4D^{-*}\delta-\bigl(1+\tfrac12c(F^-_{3A})\bigr)t .
\]
This agrees with \((\Gamma-1)t\) only if \(\mathcal Rt\) is absorbed into \(\Gamma\) or vanishes. The bound (2.3) actually uses the bracket form, so no number changes.

**What Step 46 §5 still says correctly.** The raw TN section is not Dirac-harmonic for the physical connection. In a Coulomb gauge for the physical \(E\)-connection, \(\nabla=\nabla^{TN}+a\) with \(a=O(r)\). This gives \(\nabla^*\nabla t_{TN}=o(1)\), and hence by Weitzenböck \(D^{-*}D^-t_{TN}\approx-2t\) at order one. The physical \(t\) must carry an \(O(r^2)\) Taylor correction with \(\nabla^*\nabla t_2=2t\).

That correction belongs to the background's own second jet, not to the core. Step 46's "corrected field indispensable" is right. Its interpretation as a core payment is what Step 47 correctly withdraws.

## 2. Exact TN data

**Verified:**

- **Dirac-harmonicity.** \(D\Phi_{TN}=0\) holds because \(c(d\bar f)e_2=\sqrt2\,d\bar f\wedge e_2=0\) in \(\Lambda^{0,2}\). Also \(\nabla^*\nabla\Phi_{TN}=0\) because \(\Delta_g x_i=V^{-1}\Delta_{\mathbb R^3}x_i=0\).
- **Torsion formula, exactly.** \(\Phi\wedge P_i=\sqrt{\rho_*}\,a\,\partial_i\bar f\,e_{12}\), since the \(a\bar f e_2\) part wedges to zero. Then
  \[
  t=\sqrt{\rho_*}\,a\,c(d\bar f)\Phi=\sqrt2\,\rho_*a\,d\bar f
  \]
  holds with \(\rho_*\) and not \(\rho\). Further \(|t|^2=\frac{64}{81}\cdot\frac2V=m_*/V\), and \(D^-t=\sqrt2(\bar\partial+\bar\partial^*)d\bar f=0\).
- **\(\delta\equiv0\).** This follows from isotropy of \((0,1)\)-forms, \(\langle d\bar f,d\bar f\rangle_{\mathbb C}=0\). It holds for any antiholomorphic parent and not only by conformal flatness.
- **GH families.** Here \(d\eta=*_3dV\), so
  \[
  d(\eta\wedge dh\mp V*_3dh)=\bigl(\nabla V\!\cdot\!\nabla h\mp(\nabla V\!\cdot\!\nabla h+V\Delta h)\bigr)\mathrm{vol}_3 .
  \]
  This reproduces both closedness conditions. A frame check with \(e^1=\sqrt V dr,\dots,e^4=V^{-1/2}\eta\) gives \(\eta\wedge dr+V*_3dr=-e^{14}+e^{23}\). This is ASD for \(dr\,d\theta\,d\varphi\,d\psi\), so the typing \(\beta^-\) = ASD and \(\beta^+\) = SD (hyperkähler) is correct.
- **\(h=x_3/V\).** One has \(\operatorname{div}(V^2\nabla h)=-x_3\Delta V\), which vanishes off the nut. At the nut, \(h=x_3r/(r+\ell)\) is smooth because \(x_i\) and \(r\) are quadratic in \(\mathbb R^4\) coordinates. A bounded form closed off a codimension-4 point is closed. The form \(\beta^-_{x_3/V}\) has \(|\beta|^2=2|\nabla_{\mathbb R^3}h|^2\to0\) at the nut.
- **Mismatch (2.3).** The difference is \(h-x_3=-\ell x_3/(r+\ell)\). The leading term is
  \[
  2\cdot\tfrac23\,\ell^2\cdot16\pi^2\ell R=\tfrac{64\pi^2}{3}\ell^3R ,
  \]
  matching the JSON closed form. Combining \(|c(\beta)|_{op}=\sqrt2|\beta|\), \(\frac32\cdot\frac13=\frac12\) and \(|t|^2\le m_*\) gives \(\frac{32\pi^2}{3}m_*\ell^3R\).
- **Table entries.** The following were checked by Beta integrals:
  - \(E(R)\);
  - \(\int|\nabla\tau|^4=\frac{8\pi^2}{15}m_*^2\);
  - \(\int|\nabla^2\tau|^2=\frac{16\pi^2}{5}m_*\);
  - \(\int|\nabla^3\Phi|^2=\frac{64\pi^2}{45}\);
  - \(\int|dm|^2\);
  - \(\int\kappa^2|B|^2=E/9\), assuming \(\kappa^2=\kappa_*^2/V\).

**Defects:**

1. **JSON self-duality flags.** `tn_core_exact.json` records `self_dual: false, anti_self_dual: false` for every form, including the hyperkähler form. The cause is in the script: `sqrtg = sqrt(factor(det g))` returns \((r+\ell)r\,|\sin\theta|\) because \(\theta\) is only declared positive. The test `simplify(S-B)==zeros` then does not reduce. The typing in the note is correct, but the statement that it was "checked symbolically" is not what the data show. The script should replace \(|\sin\theta|\) by \(\sin\theta\) and be re-run.
2. **\(\int|W^-|^2=8\pi^2\).** This value is listed in the docstring but is never computed or stored. The ratios \(\int|\nabla\tau|^4=\frac{m_*^2}{15}\int|W^-|^2\) and \(\int|\nabla^2\tau|^2=\frac{2m_*}{5}\int|W^-|^2\) depend on it and on the norm convention for \(W\).
3. **The determinant continuation is not unique.** The general closed ASD continuation with the same asymptotics is
   \[
   F^-_A=\tfrac i3\beta^-_{x_3/V}+i\gamma\,d(\eta/V),
   \]
   where \(d(\eta/V)=\beta^-_{-1/V}\) is the \(L^2\) harmonic form of TN. Here \(\int|d(\eta/V)|^2=16\pi^2\ell^2\), and the fibre holonomy of \(A\) at the core's edge shifts by \(4\pi\ell\gamma\). Its contribution to the resolvent residual is
   \[
   \|\tfrac32c(i\gamma\,d(\eta/V))t\|_2^2\le48\pi^2\gamma^2m_*\ell^2,
   \]
   with equality iff \(t\) lies in the top eigenline. This is of order \(L^6\) for \(\gamma\asymp1\). So the core is free only in the sector \(\gamma=o(1)\), i.e. determinant fibre-holonomy shift \(o(\ell)\). Step 47 silently chooses \(\gamma=0\). This is the concrete form of Step 46's determinant relative-degree datum, and it is a genuine local channel at the energy scale.

## 3. The first-order omission (main gap in §2)

The exact data use \(P_i=\partial_i\Phi\) with \(A=0\) and flat \(S^+\). Turning on any connection one-form \(\alpha\) acting on the \(e_1\) phase leaves \(\Phi\wedge P_i\) unchanged, because \(\Phi\wedge\alpha\Phi=0\). It does change \(P_i\), giving
\[
\delta=\sqrt{\rho_*}\,a\,\langle\alpha,d\bar z_1\rangle_{\mathbb C}\,\Phi\otimes e_{12}+O(r^2).
\]
For a curvature with \(z_1\)-plane component \(f\), the symmetric gauge gives \(\langle\alpha,d\bar z_1\rangle=\frac f2\bar z_1\). The gauge-invariant derivative \(D^{-*}\delta\) is then a nonzero constant of order \(\rho_*af\).

Consequently the literal pair \((\Phi_{TN},A_{\rm core})\) on Ricci-flat TN has \(\|D^{-*}\delta\|^2_{B_L}\asymp L^6\). The note's \(\delta\equiv0\) does not survive inserting its own \(F_A^{\rm core}\).

On the physical TNAdS block, \(S^+\) is not flat: \(\mathcal R^+=\frac s{12}\mathrm{Id}\) for \(W^+=0\). This curvature contributes two things:

- an \(e_1\)-phase term;
- an \(e_1\to e_2\) mixing term \(\propto(z_1dz_2-z_2dz_1)\) or its conjugate, depending on convention.

Write \(\Phi=\sqrt{\rho_*}e_1+a\bar z_1e_2+Q(x)\) with \(Q\) quadratic. Requiring \(\nabla\delta(0)=0\) and \(\nabla(D^+\Phi)(0)=0\) gives the following O(r) equations:

| equation | determines |
|---|---|
| \(\delta\), \(e_1\)-component | \(\partial_{z_1}Q^{(1)}\) |
| \(\delta\), \(e_2\)-component | \(\partial_{z_1}Q^{(2)}\) (together with the mixing term) |
| Dirac, \(d\bar z_1\)-component | \(\partial_{\bar z_1}Q^{(1)}\) and \(\partial_{z_2}Q^{(2)}\) |

The coefficient of \(z_1z_2\) in \(Q^{(2)}\) is fixed twice. This yields one scalar compatibility relation between three quantities: the \(z_1\)-plane effective phase curvature (\(\tfrac12F_A\) plus the spin phase), the \(\frac s{12}\) mixing coefficient, and \(\rho_*\).

So "null background jet" in §2 must mean the background satisfies \(\delta_{bg}=O(r^2)\) and \(D^+\Phi_{bg}=O(r^2)\). Equivalently, its 2-jet solves this finite linear system (16 complex equations in 20 complex unknowns, plus Bianchi). Whether the endpoint numbers \(F_A^{12}=1\), \(s=-4\), \(\rho_*=4/3\) satisfy the compatibility relation is a short exact computation with corpus Clifford conventions. Step 47 does not perform it. A first-jet hypothesis does not imply it.

**If the background 2-jet is null, the core increment is small.** The ingredients scale as follows:

- TN metric perturbation: \(O(\ell/r)\);
- TN Christoffel symbols: \(O(\ell/r^2)\);
- background jet terms: \(O(r)\);
- core change of the effective \(z_1\)-plane curvature: exactly \(\frac13\Delta\beta\), the (2.3) mismatch.

All cross terms in \(q\), \(D^{-*}\delta\) and \(D^-t\) are then \(O(\ell/r)\) pointwise on \(\ell\lesssim r\lesssim L\). This gives
\[
\int_{B_L}(\ell/r)^2\,d\mathrm{vol}\approx16\pi^2\ell^3\bigl(L+\ell\log(L/\ell)\bigr)=O(L^{10}).
\]
The ball \(r\lesssim\ell\) has volume \(O(\ell^4)\). Likewise:

- The \(F^+\) correction \(2i\sigma(\Phi_{TN})-\frac{2i}3\omega_3=O(r)\), together with its closed \(F^-\) partner, contributes \(O(L^8)\).
- \(D_A\Phi_{TN}=O(r)\) contributes \(O(L^8)\).

The conclusion "no order-\(L^6\) core payment" is therefore correct under three conditions:

1. the background has a null 2-jet;
2. \(\gamma=o(1)\);
3. an actual corrector solve realises the scaling count. That solve is not done.

## 4. Formula (3.1) and \(J_+\)

The angle formula is correct:
\[
u=\cos s\,e_1+\sin s\,e^{-i\arg f}e_2,\qquad \tan s=a|f|/\sqrt{\rho_*},
\]
and Hopf doubling gives \(J_+=\cos2s\,I_3+\sin2s\,K\).

However, \(K=\cos\chi\,I_1+\sin\chi\,I_2\) with \(\chi\) tied to \(\arg f\). It is a pointwise combination of parallel structures and is **not parallel**, contrary to the note. Formula (3.1) is unaffected, because it is algebraic. For \(\xi\in\Lambda^{0,1}_{I_3}\),
\[
\Pi^{1,0}_{J_+}\xi=\sin^2\!s\,\xi-\tfrac i2\sin2s\,K\xi .
\]
Here \(K\xi\in\Lambda^{1,0}_{I_3}\) is Hermitian-orthogonal to \(\Lambda^{0,1}_{I_3}\) and \(K\) is unitary. Hence \(\langle\Pi\xi,\Pi\xi'\rangle=\sin^2s\,\langle\xi,\xi'\rangle\), and \(|N_\tau|^2=\sin^2s\,|\nabla\tau|^2\) exactly.

The vanishing at \(s=0\) requires \(J(e_1)\) to be the structure for which \(\tau\) is antiholomorphic. This holds when \(e_1\leftrightarrow\Lambda^{0,0}\).

Two further checks:

- \(\sin^2s\approx(a^2/\rho_*)|f|^2=\kappa_*^2r^2\sin^2\theta\) (note \(a^2/\rho_*=1/6=\kappa_*^2\)). This reproduces \(\int_{B_R}|N|^2=\frac{16\pi^2}{9}m_*\ell^3R\).
- The non-parallel \(K\) contributes \(|f|\nabla K=O(1)\) to \(\nabla N\). This is part of the critical term.

## 5. Use of (3.8) and the bound (3.2)

**Hypotheses that hold.** (3.8) is a pure commutator identity. Its only input is \(F^E(Z_1,Z_2)=0\). This needs two facts:

- the metric is Einstein, so the \(\Lambda^+\to\operatorname{End}S^-\) block \(\operatorname{Ric}^\circ\) vanishes; true on TN and TNAdS;
- \(F^\pm_A\) is of type \((1,1)\) for \(J_+\).

For an actual solution, \(F^+=2i\sigma(\Phi)\propto\omega_{J(\Phi/|\Phi|)}\) is automatically \((1,1)\), and \(F^-\) always is. The condition \(\rho=\rho_*\) is not needed for the identity; it enters only through \(\kappa^2=m/(4\rho_*^3)\) used to evaluate \(\int\kappa^2|B|^2\). In the model, \(F^{\rm core,+}\propto\omega_3\) has an \(O(\sin2s)=O(r)\) part of type \((2,0)+(0,2)\) for \(J_+\), which is negligible.

**What does not hold: the constant \(C\) in (3.2).** The frame normalised by \([Z_1,Z_2]^{0,1}=-2\kappa\bar Z_1\) is aligned with the Nijenhuis direction \(\propto(d\bar z_1)^\sharp\). That direction rotates at rate \(|\operatorname{Hess}\bar f|/|d\bar f|\sim\ell/r^2\). The coefficients \(L_i\) are therefore not bounded on a core, and
\[
\|L\,N\|^2\sim\int\frac{\ell^2}{r^4}\cdot\frac{\kappa^2\ell^2}{r^2}\,d\mathrm{vol}\sim\ell^2 ,
\]
which is critical, the same order as \(\|\kappa B\|^2=E/9\). Inequality (3.2) with a uniform \(C\) does not follow, and \(L\,N\) could a priori offset \(\kappa B\).

**A direct, convention-free replacement (Kato).** Use \(|\nabla N|\ge|\nabla|N||\) together with
\[
|N|=\kappa_*\sqrt{m_*}\,\ell\,\frac{r\sin\theta}{(r+\ell)^2}\,\bigl(1+O(r^2)\bigr),
\]
which is \(\psi\)-independent. The factor \(V\) cancels between \(|\nabla\cdot|_g^2\) and \(d\mathrm{vol}_g\). Substituting \(r=\ell x\), and using
\[
\int_0^\infty\frac{x^2(1-x)^2}{(1+x)^6}\,dx=\frac{2}{15},\qquad \int_0^\infty\frac{x^2}{(1+x)^4}\,dx=\frac13,
\]
one obtains
\[
\boxed{\int_{TN}|\nabla N_\tau|^2\ \ge\ \tfrac{16\pi^2}{5}\kappa_*^2m_*\ell^2=\tfrac{8\pi^2}{15}m_*\ell^2=\tfrac{E_{\rm core}}{15}}
\]
up to \(1+O(\ell/L)\). The integral is dominated by \(r\sim\ell\), where the model is accurate. Per normalization volume \(4\pi^2\ell^2\) this gives \(\fint|\nabla N|^2\ge\theta\cdot2m_*/15\).

This bound transfers to actual fields converging to the TN core in \(C^1\) on scale \(\ell\). Near \(r\sim\ell\), background contributions \(N_{bg}=O(r)\) are dominated by \(N_{\rm core}\sim\kappa_*\). The exact value of \(\int|\nabla N|^2\) can also be computed directly from (3.1), with no Clifford-sign choices. It should replace the unspecified constant in (3.2).

## 6. §4 consequences

**§4.4 reduction.** This section overreaches in three ways.

1. **Circularity for nut-type escapes.** For these escapes, the Kato bound already shows that \(\|\nabla N\|_{2,av}\to0\) excludes a positive nut fraction. The reduction therefore contains no information beyond the estimate itself.
2. **The step \(\nabla N\to0\Rightarrow\kappa B\to0\) needs a forbidden bound.** It requires \(\|L_iA_i\|_2\to0\) and control of \(\nabla Z\). By Hölder and Sobolev, \(\|LN\|_2\le\|L\|_4\|N\|_4\), and \(\|L\|_4\) is a Hessian \(L^4\) bound of exactly the finite-density type that §4.3 rules out. For TN cores, \(\int|\nabla^2\Phi|^4\) is \(O(1)\) per core.
3. **Passing from \(\kappa B\) to \(B\) needs \(\kappa\) bounded below**, i.e. \(m\) bounded below.

The phrase "discharges the weak proof obligation" is not supported. The supported content is narrower: a nut phase is characterised by a critical lower bound on \(\fint|\nabla N_\tau|^2\), and a density-free argument must prove \(\nabla N\to0\) by a mechanism that does not use \(L^4\) Hessian control.

**§4.2 arithmetic.** With \(\int|dm|^2=\frac{16}{3}\) (units \(\pi^2m_*^2\ell^2\)), \(E_1=\frac23|dm|^2\) and \(E_2=\frac13|dm|^2\):
\[
2\int E_1=\tfrac{64}{9},\qquad 3\int E_2=\tfrac{48}{9}.
\]
The note's display "\(\frac{112}9+\frac{48}9-\frac{16}9=16\)" double-counts and assigns a negative value to \(4\int m^2|c|^2\ge0\).

With these averages, the identity \(=16\) (which matches \(4\int m^2=16\) at \(R^3=3\ell/4\)) requires
\[
4\int m^2|c|^2=\tfrac{32}{9},
\]
i.e. an \(m^2\)-weighted \(\langle|c|^2\rangle=\frac29\). The qualitative "\(c\)-depleted" picture survives, but the numbers must be recomputed with the corpus definitions of \(E_1\), \(E_2\) and \(c\). The flux term through the cell's outer face must also be included, since the cell is not periodic.

## 7. Effect on the conclusion

No error found reverses "a TN core carries no local order-\(L^6\) payment at the energy scale." The correct statement is:

> The core's increment to \(q\), \(D^-t\), \(D^{-*}\delta\), \(N\) and the monopole residuals is \(o(L^6)\), with leading terms \(O(\ell^3L)\), provided that
> (i) the background 2-jet solves the prolonged system at the core point;
> (ii) the determinant charge satisfies \(\gamma=o(1)\);
> (iii) the corrector realising the scaling count exists.

The two remaining exact computations are:

- the endpoint 2-jet compatibility relation from §3;
- \(\int|\nabla N_\tau|^2\) on TN, which is bounded below by \(E_{\rm core}/15\).

Both are short sympy or Wolfram calculations that settle the open items without new analysis.
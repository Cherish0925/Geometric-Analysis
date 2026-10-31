# Step 33: Route A consolidation — single-annulus obstruction, indicial inventory, and topology filter

## 0. Scope and target fidelity

This note concerns only the **four-dimensional positive noncollapsed subroute** of the full Yau-26 problem.  It does not prove or refute the full proposition and does not address:

- the collapsed positive branch;
- the negative branch;
- dimensions \(n\ge 5\);
- the required final Lean formalization of the complete proposition.

The exact active target remains: for every \(n\ge2\), decide whether there exist dimension-only \(c_n<C_n\) such that any closed connected smooth \(n\)-manifold carrying a metric with \(c_ng\le \operatorname{Ric}_g\le C_ng\) must carry some smooth Einstein metric, with no proximity, sign, symmetry, topology, or noncollapse hypothesis.

This step consolidates the correction from Step 32 and the strategist note: Route A must not become an experiment on a rigid exact metric such as Page.  The valuable object is a **single balanced annulus** in a noncollapsed degeneration, where the orbifold \(H_2\) mode and the Eguchi--Hanson/ALE \(H^4\) mode have the same size and their Wronskian signal has scale \(t^4\).

## 1. Source status: LeBrun--Ozuch assumes Hermitian/admissible; it does not derive it from \(\det R_+=0\)

The source `Knowledge/objects/papers/Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771/object.md` is now the clean local source for arXiv:2601.19215v2, citation key `lebrun2026desingularizations`.

The exact relevant source statements are:

- Abstract/lines 23--24: for a sequence of **smooth compact oriented Einstein 4-manifolds** with fixed \(\lambda>0\) converging to an Einstein orbifold, if the limit is **Hermitian**, has at least one singular point, and every gravitational instanton bubble is **anti-self-dual**, then the sequence is eventually Kähler--Einstein and the limit is one of the Odaka--Spotti--Sun KE orbifold limits.
- Definition 1/line 44: an admissible sequence is an exact Einstein sequence whose every Ricci-flat ALE bubble satisfies \(W^+\equiv0\) in the induced orientation.
- Theorem B/lines 52--53: the Hermitian assumption is an explicit hypothesis: \((X,g_\infty)\) is a compact connected Einstein orbifold with \(\lambda>0\), and \(g_\infty\) is Hermitian with respect to an integrable orbifold complex structure.  If it has a singular point and the converging sequence is admissible, then the sequence is eventually KE and the limit lies in the OSS KE-orbifold list.
- Theorem 3.1/lines 136--143: for simply connected positive Einstein orbifolds, Hermitian is equivalent to conformally Kähler and to specific Weyl-eigenvalue conditions, including \(\det(W^+)>0\).  This is **not** the same as the Route-A first-obstruction condition \(\det R_+=0\), where \(R_+=W^++\frac{\Lambda}{3}I\).
- Theorem 4.1/lines 155--168: if a smooth compact oriented 4-manifold admits an admissible exact Einstein sequence converging to a Hermitian positive Einstein orbifold, then \(M\) is diffeomorphic to a Del Pezzo surface: either \(S^2\times S^2\) or \(\mathbb{CP}^2\#\ell\overline{\mathbb{CP}}{}^2\), \(0\le\ell\le8\).  In particular \(\pi_1(M)=0\), \(b_+(M)=1\), and \(b_-(M)\le8\).
- Lines 186--192: once Theorem B is applied, singular admissible Hermitian limits are narrowed further to \(\mathbb{CP}^2\#k\overline{\mathbb{CP}}{}^2\), \(5\le k\le8\), with listed ADE/class-T singularities.

Thus the classification bypass is useful only after one obtains a genuine **Hermitian/conformally Kähler + admissible exact-Einstein** input.  It cannot be applied to an arbitrary \(C^0\)-Ricci-pinched branch-(b) sequence merely because \(\det R_+=0\) at the bubble point.  This is a correction to any reading of Step 31 that treated the spectral condition as a Kähler detector.

## 2. Topological filter for the toric/spin stress family

The finite arithmetic in `workspace/data/step33_routeA_source_indicial_topology.json` gives a cheap but important filter.

For \(M_k=\#_k(S^2\times S^2)\), the standard convention gives
\[
\chi(M_k)=2k+2,\qquad b_2(M_k)=2k,\qquad b_+(M_k)=b_-(M_k)=k,
\]
and the intersection form is \(kH\), even and spin.  In contrast, the Del Pezzo diffeotypes in LeBrun--Ozuch Theorem 4.1 have \(b_+=1\): either \(S^2\times S^2\) with form \(H\), or \(\mathbb{CP}^2\#\ell\overline{\mathbb{CP}}{}^2\) with odd form \(\langle1\rangle\oplus \ell\langle-1\rangle\).

Therefore:

**Conditional topology consequence.** If a noncollapsed branch-(b) limit of a pinched sequence could be promoted to the LeBrun--Ozuch Hermitian/admissible setting, then the principal spin stress family \(\#_k(S^2\times S^2)\) with \(k\ge2\) is excluded immediately, because \(b_+=k\ge2\) and the form is even.  The only member of this family compatible with the Del Pezzo list is \(k=1\), namely \(S^2\times S^2\), which already carries the product Kähler--Einstein metric.

This filter is stronger and safer than an informal del Pezzo table.  It says: under the missing Hermitian/admissible input, the toric large-\(k\) stress family cannot appear in the noncollapsed classification branch.  It does **not** prove a volume gap and does not touch collapsed sequences.

## 3. OSS and low-degree Einstein existence sources

The access/audit script confirmed that arXiv:1210.0858 is indeed Odaka--Spotti--Sun, *Compact Moduli Spaces of Del Pezzo Surfaces and Kähler-Einstein metrics*.  Its arXiv abstract states that the GH compactification of the moduli space of KE del Pezzo surfaces agrees with an algebro-geometric compactification, recovers Tian's theorem on existence of KE metrics on smooth del Pezzo surfaces, and classifies degenerations.  This is sufficient for route orientation but should still be read in full before a final classification theorem uses its finite list.

For low-degree/non-KE exceptions, local source-grade objects give stronger support:

- Chen--LeBrun--Weber `Knowledge/objects/papers/0705.0710-On-Conformally-Kaehler-Einstein-Manifolds--a0085b5ef6ea--a3b06fcfd83b/object.md` lines 25--35 prove/explain a positive Einstein Hermitian metric on \(\mathbb{CP}^2\#2\overline{\mathbb{CP}}{}^2\); lines 55--63 state Page on \(\mathbb{CP}^2\#\overline{\mathbb{CP}}{}^2\), the solved KE case, and Corollary 2: a smooth compact oriented 4-manifold admitting a complex or symplectic structure carries a positive Einstein metric iff it is \(\mathbb{CP}^2\#k\overline{\mathbb{CP}}{}^2\), \(0\le k\le8\), or \(S^2\times S^2\).
- LeBrun `On Einstein, Hermitian 4-Manifolds` lines 23--44 classifies compact Einstein Hermitian 4-manifolds: KE, or Page on \(\mathbb{CP}^2\#\overline{\mathbb{CP}}{}^2\), or CLW on \(\mathbb{CP}^2\#2\overline{\mathbb{CP}}{}^2\).

This reinforces a Yau-26-specific point: the output Einstein metric need not be Kähler and need not be close to the input.  Page/CLW prevent the error “no Kähler--Einstein metric implies no Einstein metric.”

## 4. Single-annulus scaling: Route A is rate-free only at the balance radius

Step 32's scaling audit is now best interpreted sharply:

- Orbifold curvature 2-jet mode: \(|H_2|\sim r^2\), \(|\partial H_2|\sim r\).
- ALE/Eguchi--Hanson mode inserted at scale \(t\): \(|t^4H^4|\sim t^4r^{-4}\), \(|\partial(t^4H^4)|\sim t^4r^{-5}\).
- Boundary Wronskian signal:
\[
 r^3\big(H_2\partial(t^4H^4)-t^4H^4\partial H_2\big)\sim t^4,
\]
independent of \(r\), because the dual exponents satisfy \(2+(-4)=-2\).
- Balance radius solves \(r^2=t^4r^{-4}\), hence
\[
 r=t^{2/3},\qquad |H_2|=|t^4H^4|=t^{4/3}.
\]
- On a dyadic shell at this radius, a \(\delta\)-small Ricci-endomorphism residual pairing with either natural mode contributes \(\delta r^6=\delta t^4\), so the error-to-signal ratio is \(O(\delta)\), independent of the relation between \(t\) and \(\delta\).
- Away from the balance window, especially at \(r\sim1\), the same nonconservation is \(O(\delta)\) while the signal is \(O(t^4)\), so no rate-free argument can sum errors through the full neck to macroscopic scale.

Thus the A2 bridge should be stated as a **single-annulus comparison**:

> On a balanced annulus \(r\asymp t^{2/3}\) of a noncollapsed \(C^0\)-Ricci-pinched degeneration with an \(A_1\)/Eguchi--Hanson bubble, after fixing Bianchi/volume gauge, the metric equals the cone plus the Wronskian-dual modes \(H_2\) and \(t^4H^4\), plus an error whose bilinear pairing with the dual test modes is \(o(t^4)\).

This is much narrower than “build a global normal form across the neck” and much more relevant than a flux computation on an exact rigid metric.

## 5. Indicial inventory: the finite calculation to finish before committing Route A

Two scripts preserve the finite indicial arithmetic:

- `workspace/scripts/step33_routeA_source_indicial_topology.py` -> `workspace/data/step33_routeA_source_indicial_topology.json` records the general cone Wronskian exponent: for dimension 4 cone powers \(r^\alpha\) and \(r^\beta\), the boundary exponent is \(\alpha+\beta+2\); radius-independent pairings require \(\alpha+\beta=-2\).
- `workspace/scripts/step33_tt_bianchi_indicial_probe.py` -> `workspace/data/step33_tt_bianchi_indicial_probe.json` performs a finite symbolic sanity check in flat Bianchi gauge on \(\mathbb R^4/\{\pm1\}\).  In this model, componentwise harmonic homogeneous tensor modes have roots \(\alpha=l\) and \(\alpha=-l-2\), and the antipodal quotient keeps even \(l\).  The TT modulo polynomial gauge dimensions are: \(l=0\) gives only gauge after trace/divergence constraints; \(l=1\) is odd and absent on the quotient; \(l=2\) is the first even non-gauge regular mode, with dual \(-4\).

The current finite reading is:

1. The even roots strictly between \(-4\) and \(2\) reduce, in the flat Bianchi sanity model, to the \((0,-2)\) pair.  The odd \((1,-3)\) pair is removed by the \(\mathbb Z_2\) quotient, and \(\alpha=-1\) does not arise as a Cartesian harmonic root in this model.
2. The \((0,-2)\) pair is the cone scale/volume-mass pair.  It should be removed by tangent-cone and volume gauge, consistent with Step 30's Eguchi--Hanson expansion having no \(r^{-2}\) mass term.
3. The first remaining even geometric dual pair is exactly \((2,-4)\): orbifold curvature 2-jet against the Eguchi--Hanson \(r^{-4}\) coefficient.

This is **not yet a theorem**.  The next construction must replace this finite flat-cone sanity check by the actual tensor spherical-harmonic/Lichnerowicz inventory on \(C(S^3/\mathbb Z_2)\), with Bianchi gauge, volume gauge, parity, and pure-gauge quotient handled explicitly.  But the computation strongly supports the strategist's claim that Route A's finite ODE/representation problem is the right next object.

## 6. A1/A2 should be merged as a neck-energy/harmonic-radius regularity problem

The previous language separated bubble-tree finiteness (A1) from obstruction transfer (A2).  A better formulation uses one input:

> **No intermediate-scale annular \(L^2\)-energy loss plus harmonic-radius epsilon regularity.** In a four-dimensional noncollapsed sequence with \(\|\operatorname{Ric}_{g_i}-g_i\|_{L^\infty}\to0\), scale-invariant \(L^2\)-curvature energy is quantized into finitely many bubbles, and on buffered annuli with small \(L^2\) energy the harmonic radius is bounded below at the annulus scale.

The reasons are:

- Chern--Gauss--Bonnet gives a global scale-invariant \(L^2\)-curvature budget in dimension 4.
- The Eguchi--Hanson \(A_1\) quantum is \(8\pi^2(\chi-1/|\Gamma|)=12\pi^2\), so only finitely many such bubbles can occur under fixed topology.
- Blow-ups at a harmonic-radius scale have rescaled Ricci defect \(\to0\), local noncollapse from Bishop--Gromov, and finite \(L^2\) curvature; BKN-type theory should then give ALE bubbles.
- Step 11's Calderón--Zygmund spike does not refute this harmonic-radius formulation.  It refutes pointwise curvature regularity: curvature can blow up while the relevant \(C^{1,\alpha}\) harmonic-coordinate size can remain small because the spike is exponentially localized.

This lemma is load-bearing.  A proof would make the bubble category available for merely pinched sequences; a counterexample would reveal a new noncollapsed degeneration mechanism and would be equally route-changing.

## 7. Corrected Route-A status

Route A now has a sharper structure:

1. **Regular noncollapsed alternative** (already conceptually reliable): if no codimension-4 singularity/bubble appears, the weak limit is a smooth positive Einstein metric and diffeomorphism recovery gives an Einstein metric on \(M\).
2. **Bubble alternative**: if an \(A_1\)/EH bubble appears, the balanced annulus should carry a rate-free \(H_2\)-\(H^4\) Wronskian comparison.  Nonzero Ozuch first obstruction should force an \(O(1)\) pointwise Ricci-endomorphism defect, contradicting \(\delta_i\to0\), provided the finite indicial/gauge and harmonic-radius annulus lemmas are proved.
3. **Hermitian/admissible bypass**: if branch-(b) limits can be shown to be Hermitian and ASD-admissible in the LeBrun--Ozuch sense, then the smooth topology is Del Pezzo.  This immediately excludes \(\#_k(S^2\times S^2)\), \(k\ge2\), from that noncollapsed subcase.  It cannot be invoked without the Hermitian/admissible input.

The noncollapsed positive branch is therefore more benign than it looked in Steps 7--10, but it is not closed.  Moreover, every improvement of Route A increases the importance of the **collapsed positive branch**, because a complete \(P_4^+\) proof needs a topology-uniform volume gap or a collapse-to-Einstein-compatible topology theorem.  That collapsed half has not advanced in several steps and should not remain a placeholder.

## 8. Recommended next work

The next highest-value construction is to make the indicial inventory real:

- compute the Lichnerowicz/Bianchi indicial roots on \(C(S^3/\mathbb Z_2)\) for symmetric 2-tensors, with \(\mathbb Z_2\) parity, trace/Bianchi/volume gauge, and pure-gauge quotient;
- prove or refute that no non-gauge modes in \((-4,2)\) survive except the removable \((0,-2)\) pair;
- identify exactly the \(l=2\) curvature 2-jet space and its dual \(l=-4\) ALE coefficient space, and write the Wronskian pairing matrix matching Ozuch's \(R_+v=0\) condition.

In parallel or immediately afterward, the collapsed positive branch should be reactivated: the existing Bochner-center estimate only works once a central (almost-)Killing field is available, so the real missing bridge is either a topology-uniform lower volume theorem, a Ricci-only collapse scale-selection theorem, or a counterexample mechanism in the toric/fixed-strata family.


## 9. A03 correction and retraction on the negative-flow side branch

**UPDATE (Step 34):** Messages #332 and #333 from A03 **retract** message #330.
The error was a Sobolev-constant convention mix-up: the embedding coefficient
\(S_{\mathrm{cal}} = Cr^2/\sqrt{V}\) gives \(S_{\mathrm{cal}}\sqrt{H_2}\) that
is collapse-independent, not the divergent product claimed in #330.
The fixed-topology ball-volume argument was also false. Therefore:
- The per-manifold conclusion recorded in the original §9 below is **invalid**.
- The negative cutoff-flow route remains **unresolved** (neither dimension-uniform
  nor per-manifold).
- The genuine open work is the spacetime recurrence with all time factors retained,
  defect-drift summability, and evolving cutoff-jet estimates.

~~Original §9 (now retracted):~~
~~Peer message #330 from S0910A03 claimed the Moser absorption coefficient is
\(\gamma=S^2 H_2^{1/2}\), diverging under local collapse.  I read A03's note `Sessions/S0910A03/workspace/notes/step33_uniform_bootstrap_and_per_metric_continuation.md` and reran `Sessions/S0910A03/workspace/scripts/verify_step33_uniform_bootstrap.py`, which exited 0 and explicitly verifies the distinction: for a **fixed** manifold, Bishop--Gromov plus CGB gives a positive ball-volume lower bound depending on that manifold (hence a per-manifold gap \(\delta_0(M)\)); for a varying controlled family there is no family-uniform gap without an additional collapse-independent argument.

This correction matters for the full Yau-26 target because dimension-only constants cannot depend on the individual manifold.  Thus the negative IL cutoff-flow branch, even if otherwise repaired, currently supplies at most a fixed-topology or per-manifold statement and cannot be used as a full branch result.  It also reinforces the priority stated above: the collapsed positive branch and topology-uniform volume/collapse control are not optional residual issues but central to any dimension-only resolution.

# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step55_k1_orbifold_gate_charges_lattices_collapse.md",
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md",
    "Sessions/S1003A02/workspace/scripts/step55_orbifold_bubble_charges.py",
    "Sessions/S1003A02/workspace/scripts/step55_Tchain_embeddings.py",
    "Sessions/S1003A02/workspace/scripts/step55_Tchain_discriminants.py",
    "Sessions/S1003A02/workspace/data/step55_Tchain_embeddings.json"
  ]
}
```

## Task

Verify the mathematics of the Step-55 note (k=1 orbifold gate for P=int|Ric°|^2 on M = X # CP2bar, X a compact ball quotient). Check carefully and report concrete errors with corrections: (1) the two-orientation ALE charge formula (1.1) c_± = 2/|Γ| − 2χ ∓ 3τ ∓ 3η with η = −4 s(q,n) (Dedekind sum), its sign conventions as fixed by Burns, Eguchi–Hanson, A_{n−1}, and the numerically verified LeBrun O(−n) value P = 8π²(n−2)²/n; (2) the ledger identities (1.2) T_+^orb(V) = T_+(M) + c_+(N) and (1.3); (3) Lemma 55.1 (degree-one/free-indecomposability argument that orbifold bubble regions have H_2 ⊂ ZE, including whether the one-sided SW vanishing with a PSC orbifold cap is a correct/standard input); (4) Prop 55.3: the claim that m=1,2 cyclic-end b2=1 bubbles have c_+=1 (linking-form restriction q a unit square mod m^2), the surviving lists, and the noncyclic D_5, D_9, E_8 analysis (orientation and linking-form compatibility, the trefoil-trace realization); (5) Prop 55.4 (T-singularity Milnor fibres have charge 0 in complex orientation and −4(1−1/n²) reversed; Ricci-flat Kähler ALE on them); (6) Theorem 55.5: π1 pushout, degree one, K unimodular negative definite of rank r+1, the H_1-torsion argument forcing primitivity (gcd(o,n)=1 ⇒ o=1), and the discriminant criterion 1−na unit square mod n² ⇔ n odd or 8|n — including whether the discriminant form of the T-chain is ⟨(1−na)/n²⟩ and whether the anti-isometry condition is stated with the right sign; (7) Prop 55.6 blow-up counting argument (Σ(−D_j²) ≤ 3r+1 over r+1 exceptional components; T-chains have Σb_i = 3r+1) and its use of SW/general type; (8) Lemma 55.8 and the collapse discussion, especially the claim that a collapsed region with τ(C) = −1 would make the ledger favorable to absorption. Also say whether the n=3 example ([5,2] chain realized by 2E1+E2 and E2+E3 in #3CP2bar) is correct as a lattice/topology statement, and whether Theorem 55.7's trichotomy follows. Write a direct mathematical memo.

## Output

# Verification memo: Step 55 (the k = 1 orbifold channels for P on X # CP2bar)

## Summary

The computational core of the note is correct:

- the charge formula (1.1) and its sign conventions;
- the ledger identities (1.2) and (1.3);
- the T-chain discriminant and the primitivity mechanism of Theorem 55.5.

Five statements are not established as written:

- **(a) Prop. 55.3(a)** rests on a simple-connectivity assumption that Lemma 55.1 does not provide. A non-simply-connected cyclic-end bubble carrying \(E\) with \(c_+<1\) exists topologically.
- **(b) The surviving lists** in 55.3 and 55.7 omit spherical space forms that are neither cyclic nor in \(SU(2)\).
- **(c) Prop. 55.6** needs an extra input to get "exceptional rank \(=r+1\)". Siu rigidity supplies it.
- **(d) The collapse ledger in §6** is set up incorrectly, and its stated mechanism points the wrong way. The qualitative conclusion, that collapse is unpriced by charge, survives for a different reason.
- **(e) Theorem 55.7's "exactly one of"** is not a trichotomy. The channels coexist, and the "non-Kähler bulk" statement is proved only for the zero-charge T-channel.

(Sign convention below: "definite of signature \(-\mathrm{rank}\)" is written \(Q<0\).)

---

## 1. The charge formula (1.1) and its conventions — correct

**Derivation.** Write \(\tau(N)=\frac1{12\pi^2}\int(|W^+|^2-|W^-|^2)-\eta_N\) and \(\chi(N)=\frac1{8\pi^2}\int(|W|^2-\tfrac12|\mathrm{Ric}^\circ|^2+\tfrac{s^2}{24})+\frac1{|\Gamma|}\). Then
\[
P=2\!\int|W|^2+\tfrac1{12}\!\int s^2-16\pi^2\big(\chi-\tfrac1{|\Gamma|}\big)
\]
gives exactly
\[
c_\pm=\tfrac{2}{|\Gamma|}-2\chi\mp3\tau\mp3\eta .
\]

**Hand checks of the table, with \(\eta=-4s(q,n)\):**

| Case | \(\eta\) | \(c_+\) | \(c_-\) |
|---|---|---|---|
| \(A_{n-1}\), \(q=-1\) | \(4s(1,n)=\tfrac{(n-1)(n-2)}{3n}\) | \(0\) identically | \(-192/7\) at \(n=7\) |
| \(A_3\) | \(s(3,4)=-1/8\), so \(\eta=1/2\) | \(0\) | \(-15\) |
| EH | \(s(1,2)=0\) | \(0\) | \(-6\) |
| Burns | — | \(1\) | \(-5\) |
| \(\mathrm{EH}/\mathbb Z_2\), \(\eta(4,1)=-1/2\) | \(-1/2\) | \(0\) | \(-3\) |
| \(\mathcal O(-n)\), \(q=1\) | \(-\tfrac{(n-1)(n-2)}{3n}\) | \(\tfrac{(n-2)^2}{n}\) | — |

The \(\mathcal O(-n)\) value agrees with the symbolic \(s\equiv0\), \(W^+=0\) and with the quadrature in the script. The lens identifications are consistent:

- \(L(n,q)\cong L(n,q^{-1})\) preserves \(s\);
- orientation reversal sends \(q\mapsto-q\) and \(\eta\mapsto-\eta\).

One consistency fact is worth stating explicitly. For any Ricci-flat ALE, \(c_\pm=-\frac1{2\pi^2}\int|W^\pm|^2\le0\). The Ricci-flat checks (EH, \(A_n\), \(\mathrm{EH}/\mathbb Z_2\)) therefore test the sign of \(\eta\) only through the requirement that the side with \(W^\pm=0\) gives exactly 0. The LeBrun family, which is not Ricci-flat, is the genuinely independent test of the sign, and it passes.

## 2. Ledger identities (1.2), (1.3), and two-piece duality — correct

- **(1.2).** \(\chi(M)=\chi(V^\circ)+\chi(N)\) and \(\tau(M)=\tau(V^\circ)+\tau(N)\) (Novikov). The flat cone has \(\int L=0\) and its link carries the same orientation as the end of \(N\), so \(\tau_{\rm orb}(V)=\tau(V^\circ)-\eta_N\) and \(\chi_{\rm orb}=\chi(V^\circ)+1/|\Gamma|\). Subtracting gives \(T_+^{\rm orb}-T_+(M)=c_+(N)\).
- **(1.3).** This follows with \(C_+=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2\) and scalar-flat \(N\). It is a lower-bound relation under \(\mathrm H_{\rm lsc}\), not an identity for \(p_*\).
- **Two-piece duality.** It follows from \(\eta_W=-\eta_N\). The \(\overline{\mathbb{CP}}^2=\mathcal O(-4)\cup\bar B_2\) check \((1)+(-3)=1-3\) is right.

## 3. Lemma 55.1 — correct in structure, with two points to register

**What holds.**

- The pushout splitting \(\Gamma=G_1/\langle\!\langle\Gamma_p\rangle\!\rangle*G_2/\langle\!\langle\Gamma_p\rangle\!\rangle\) is valid because the finite \(\Gamma_p\) maps trivially into the torsion-free \(\Gamma\).
- When the bulk factor is trivial, \(c\) factors through \(\widehat N=N\cup\mathrm{cone}(L)\). This is a rational homology manifold, so \(Q_X\hookrightarrow Q_{\widehat N}\) over \(\mathbb Q\) and \(b^+(\widehat N)\ge3\).

**(SW\(_L\)) inputs.**

- The two-sided version (splitting along a PSC rational homology sphere with \(b^+\ge1\) on both sides) is a standard vanishing statement.
- The one-sided version is the Lemma 54.3 argument verbatim. Each spin\(^c\) structure on a lens space or spherical space form has a unique, nondegenerate reducible, since \(H^1(L;\mathbb R)=0\). An extra step is needed: convert the PSC orbifold metric on \(\widehat B\) into a PSC metric on \(B\) with a round cylindrical end over \(S^3/\Gamma\). This is a Gromov–Lawson bending carried out \(\Gamma\)-equivariantly in the uniformizing chart, and it descends because \(\Gamma\) acts freely on \(S^3\).
- When \(N_{\rm eff}\) is a tree of bubbles rather than one ALE space, PSC of \(\widehat N_{\rm eff}\) needs equivariant PSC gluing of the caps of the pieces along matching orbifold points. This should be written into the lemma.

**What the lemma does not give.** It shows that \(\pi_1(N)\to\Gamma\) is trivial. It does **not** show that \(\pi_1(N)=1\): \(\pi_1(N)\) need only be normally generated by the image of \(\Gamma_p\). This is exactly what the rational balls \(B_{n,a}\), with \(\pi_1=\mathbb Z_n\), do. It is the root of the error in §4 below.

## 4. Prop. 55.3

**Correct under its hypotheses.** For simply connected \(N\) with \(Q_N=\langle-m^2\rangle\):

- \(|H_1(\partial N)|=m^2\), and the linking form forces \(q\) to be a unit square mod \(m^2\), with orientation fixed by \(\mathcal O(-n)\leftrightarrow q=1\).
- For \(m=1,2\), \(q=1\) only, so \(c_+=1\).
- Hand recomputation gives \(s(4,9)=-4/27\), \(\eta=16/27\), \(c_+=-23/9\), \(c_-=-5\).
- The \(SU(2)\)-end formulas \(c_+=1-r\) and \(c_-=4/|\Gamma|-9+r\) hold, as do the reversed value \(4/|\Gamma|+r-3\) and \(E_8\): \((-7,-29/30)\).
- The \(D_r\) linking-form argument is right. For odd \(r\), the discriminant of \(-D_r\) on \(\mathbb Z_4\) is \(\langle -r/4\rangle\), and matching \(\langle-1/4\rangle\) gives \(r\equiv1\pmod4\). This keeps \(D_5,D_9\) and removes \(D_7\).
- \(E_6\) (\(\mathbb Z_3\)) and \(E_7\) (\(\mathbb Z_2\)) are removed by order.
- The \(E_8\) realization as the \(-1\)-trace of the left-handed trefoil, whose boundary is \(\Sigma(2,3,5)\) with the orientation of \(\partial(-E_8)\), is the standard identification.

**Error (a): \(E\) can reach a cyclic-end orbifold bubble.** Take
\[
N=\bar B_{t,a}\,\natural\,(\overline{\mathbb{CP}}^2\setminus B^4),
\]
the ∂-connected sum of the reversed T-ball with a punctured \(\overline{\mathbb{CP}}^2\). It has:

- \(\partial N=-L(t^2,ta-1)\), a cyclic end;
- \(\pi_1=\mathbb Z_t\), normally generated by the end, so Lemma 55.1 is satisfied;
- \(b_2=1\), class \(E\).

Its charges are
\[
c_+(N)=c_-(B)+1=-3+\tfrac4{t^2},\qquad c_-(N)=c_+(B)-5=-5 .
\]
For \(t=2\) this is \((-2,-5)\), with end \(L(4,3)\) (the \(A_3\) orientation). So the sentence "the class \(E\) or \(2E\) cannot escape into an orbifold bubble with a cyclic end" is false. The correct statement is "cannot escape into a **simply connected** such bubble".

In general, a \(b_2=1\) region has \(H_1(N)\) a cyclic quotient of \(H_1(L)\), and \(|H_1(\partial N)|=m^2|{\rm tors}\,H_1N|^2\). The enumeration must run over these pairs. The cheap repair is to rerun the script over all \((m,t)\) and all \(q\) with the corresponding linking forms.

**Error (b): missing spherical space forms.** Free \(\Gamma\subset SO(4)\) also includes \(\mathbb Z_k\times\) binary polyhedral groups (with coprimality conditions) and the prism and diagonal-index-2 families. Many have cyclic \(H_1\) of square order; for example \(\mathbb Z_{49}\times I^*\) has \(H_1=\mathbb Z_{49}\). Their \(\eta\)-invariants are computable (Dedekind-type sums over the group), but none is priced. The same applies to rational-ball ends in §4. The "finite explicit list" of 55.3 and 55.7 is therefore not yet complete.

## 5. Prop. 55.4 (T-type balls) — correct

**Charge check.** The condition \(c_+=0\) is \(3\eta(n^2,na-1)=2/n^2-2\). By hand at \(n=2\) (\(-1/2\)) and \(n=3\), \(a=1\) (\(s(2,9)=4/27\), \(\eta=-16/27\)) it holds.

**Metric.** The \(\mathbb Z_n\) action \((x,y,z)\mapsto(\zeta x,\zeta^{-1}y,\zeta^az)\) on \(\{xy=z^n+1\}\) is free. It is isometric for the Gibbons–Hawking metric with centres at a regular \(n\)-gon, preserves one complex structure, and rotates the others. So the quotient is Ricci-flat Kähler with holonomy \(U(2)\), and its Kähler orientation is the hyperkähler orientation. Hence \(W^+=0\), \(P=0\), and \(w_{\rm rev}=-c_-=4(1-1/n^2)\). Şuvaina's work is the right reference to register.

**Unverified converse.** The summary sentence "the zero-charge rational balls are exactly the T-Milnor fibres" is not checked by the script, which tests only T-type \(\Rightarrow\) zero charge. At \(m=3\) I find:

- \(q=1,8\) give \((40/9,-8)\);
- \(q=4,7\) give \(c_-=0\), which are T-type reversed (\(-4\equiv5\)).

So the converse is consistent at \(m=3\), but it needs the reverse test in the script for all \(m\le10\).

## 6. Theorem 55.5 — correct, one reasoning line to fix

- **(i)** The \(\pi_1\) and degree statements are correct. The factorization through \(V^\circ/\partial V^\circ\) is unambiguous because \([\Sigma L,X]=0\) for aspherical \(X\).
- **(ii)** \(c_*c^!=\mathrm{id}\) gives an orthogonal integral splitting with \(Q|_{c^!H_2X}=Q_X\). So \(K\) is unimodular, of rank \(r+1\) and signature \(-(r+1)\), and \(K\cong-I\) for rank \(\le7\).
- **(iii)** The torsion argument is correct, and it is the best step of the note. The extension \(0\to\mathbb Z_{\gcd(o,n)}\to H_1(M)\to H_1(Y)\to0\), with finite kernel, gives surjectivity on torsion. Equal \(H_1\) then gives \(\gcd(o,n)=1\), and \(o\mid n^2\) gives \(o=1\). For unimodular \(K\), surjectivity of \(K\to C^*\) is equivalent to primitivity.
- **Discriminant.** \((G^{-1})_{11}=-\det[b_2..b_r]/\det=-(na-1)/n^2\), so the discriminant is \(\langle(1-na)/n^2\rangle\). The required anti-isometry with \(\mathrm{disc}\langle-n^2\rangle=\langle-1/n^2\rangle\) is correctly stated as \(\cong\langle+1/n^2\rangle\). Because \(K\) may be odd, only the bilinear discriminant form enters. The graph of the anti-isometry is \(b\)-isotropic, so the condition is sufficient.
- **Parity law.** It is correct, but the stated reason for \(v_2(n)=1\) is not. There the 2-primary modulus is 4, not 8, and \(1-na\equiv3\pmod4\) is the obstruction. The mod-8 argument applies only for \(v_2=2\) (\(1-na\equiv5\bmod8\)).
- **Search.** The exhaustive search is genuinely exhaustive in the cases that return "no primitive embedding" (\(n=2,4,6\)). The 4000 cap is reached only for \(n=7,a=6\), where existence is what matters.

**The \(n=3\) example.**

- *Lattice.* \(v_1=2e_1+e_2\), \(v_2=-e_2-e_3\) in \(-I_3\) gives Gram \(\begin{pmatrix}-5&1\\1&-2\end{pmatrix}\) with maximal minors \(-2,-2,-1\). It is primitive. Correct.
- *Smooth realization.* The conic in the first summand # a line in the second, together with the tube of two lines, works. The class must be taken as \(-(E_2+E_3)\), i.e. that sphere with reversed orientation, to get the \(+1\) plumbing sign. Two distinct lines in the second summand meet once, so this is fine.
- *Topology.* The computation above gives \(H_1(V^\circ)=0\) and \(H_1(Z)=0\). Whether \(\pi_1(Z)=1\) and \(Z\cong\overline{\mathbb{CP}}^2\) is unresolved. Equivalently: is \(\overline{\mathbb{CP}}^2\) the union of \(B_{3,1}\) with a \(\langle-9\rangle\) filling of \(-L(9,2)=L(9,7)\cong L(9,4)\)?
- *Candidate filling and the test.* A candidate filling is the \(-9\)-trace of the mirror of \(T(2,5)\), whose boundary is a lens space of that type. A Kirby-calculus identification of the rational blowdown is the decisive computation. Smooth existence matters, since 3 is not a Markov number.
- *A weaker requirement suffices.* Only \(X\#Z\cong M\) is needed, not \(Z\cong\overline{\mathbb{CP}}^2\).

## 7. Prop. 55.6

**Counting step — correct given the setup.**

- The configuration of exceptional curves has simple normal crossings, so each later centre lies on at most 2 earlier curves, giving \(\sum(-D_j^2)\le(r+1)+2r\).
- An irreducible contracted curve is a strict transform of an exceptional curve.
- T-chains have \(\sum b_i=3r+1\).

**Missing link (c).** The step "\(b_2(Y)-b_2(X')=r+1\)" does not follow from "every curve with class in \(K\) is contracted". Exceptional classes lie in \(K\), so the exceptional rank \(e\le r+1\). Equality needs \(\ker(c_{X'*})=0\) on the minimal model.

A clean proof is Siu rigidity:

1. \(Y\) is Kähler, since \(b_1\) is even.
2. The degree-one map \(Y\to X\) is homotopic to a harmonic map (Eells–Sampson). Its real rank is 4 somewhere, and the target is strongly negatively curved, so the map is holomorphic.
3. A holomorphic degree-one map is a birational morphism. Since \(X\) is minimal of general type, \(Y\) is \(X\) blown up \(r+1\) times.

This also settles general type directly. Without Siu, general type follows from \(\pi_1\): \(\kappa\le1\) surfaces have \(\pi_1\) virtually abelian or extending an orbifold surface group by an abelian normal subgroup, and neither is possible for a cohomological-dimension-4 torsion-free hyperbolic \(\Gamma\).

**Rational blowdown input.** \(SW_M\ne0\Rightarrow SW_Y\ne0\) is the Fintushel–Stern/Park formula. It is not needed once Siu is used.

**Reach of the conclusion.** The result rules out complex orbifold bulks whose T-point is the complex quotient singularity. It says nothing about the \(b_2=1\) channels, the reversed balls, or non-T balls.

## 8. Lemma 55.8 and the collapse ledger

**Lemma 55.8 — correct.** Cyclic image gives factorization through \(S^1\), and \(H_2(S^1)=0\). Amenable subgroups of a torsion-free hyperbolic group are cyclic. The free-circle spin argument (\(TC=\pi^*TB\oplus\mathbb R\), Wu) and the \(G\)-signature statement are correct.

**Error (d): the ledger in §6.** Under bounded-curvature collapse, all curvature integrands over \(C\) tend to 0. Therefore:

- The global identity \(\frac1{8\pi^2}[4\int|W^+|^2+\frac1{12}\int s^2-P]=A-1\) is carried **entirely by \(\Omega\)'s integrals**. This gives
\[
\frac{P}{8\pi^2}=C_+(\Omega)-(A-1)+o(1),
\]
which is the same threshold \(C_+(\Omega)<A\) as with no collapse.
- The topological numbers \(\chi(C)=0\) and \(\tau(C)\) appear only as transgression/η-terms on \(\partial\Omega\) (adiabatic limits on the graph-manifold interface). Concretely, \(\tau(C)=-\lim\eta(\partial C,g_i)\), and \(\Omega\)'s end correction equals \(+3\tau(C)\).

The note's "\(T_+(\Omega)=A+2\), so \(\Omega\) needs only \(C_+(\Omega)\ge A+2\)" mixes a closed-manifold floor with an open region. Read literally, it would *exclude* the configuration, because \(A+2>A\) — the opposite of the stated conclusion. The correct mechanism is that \(C\) carries **zero integrated charge**. That is why collapse can absorb \(E\) at zero cost and must be excluded topologically. The sharp topological question then concerns \(\lim\eta(\partial C)\), not \(\tau(C)\) of a closed piece.

## 9. Theorem 55.7 (error e)

**Not a trichotomy.** Lemma 55.1 allows one \(b_2=1\) point together with any number of rational-ball points, and also orbifold points mixed with trivial-group points. The trivial-group points are handled by the Step 54 arguments applied in an orbifold bulk, which should be stated. The exclusion is also additive: it requires \(\sum_j\max\{c_+(N_j),c_-(N_j),0\}<1\), not a bound per point.

**Missing channels.** The list omits:

- the non-simply-connected \(b_2=1\) regions of §4, including \(\bar B_{t,a}\natural\overline{\mathbb{CP}}^2\);
- all non-cyclic, non-\(SU(2)\) ends.

**Non-Kähler bulk.** "The bulk is non-Kähler" in (B) and (C) is proved only for complex-orientation T-balls.

**The attainment statement is correct.** For all-\(P=0\) bubbles, \(p_*(M)=\alpha_{\rm orb}(V)=P(V,g_0)\) holds:

- gluing small Ricci-flat \(B_{n,a}\) into any orbifold metric gives \(\le\);
- \(\mathrm H_{\rm lsc}\) gives \(\ge\).

**The channel available for every \(X\).** The reversed \(B_2\subset\overline{\mathbb{CP}}^2\) has charge \(-3\) and an \(A_3\)-type point in \(M\)'s orientation. It gives \(V=X\#\overline{\mathbb P}(1,1,4)\) with \(T_+^{\rm orb}=A-4\) and requires \(C_+(V)<A-3\). It exists topologically for every \(X\), and the orbifold LeBrun bound \(2A/3\) removes it only for \(A\le9\). It is the cleanest test case for the orbifold threshold problem.
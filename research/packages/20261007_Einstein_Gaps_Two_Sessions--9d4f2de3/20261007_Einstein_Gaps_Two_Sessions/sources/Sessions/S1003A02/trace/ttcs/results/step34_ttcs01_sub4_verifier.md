# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/data/berger_eta_charge.json"
  ]
}
```

## Task

Independently verify the symmetry-free chiral link-charge theorem and its applications in Step 33. Re-derive all signs and normalizations from the stated Gauss–Bonnet and APS conventions. Check especially: (i) Q_±=2E∓3H and the annular orientation; (ii) thin disk-bundle charge for self-intersection n, including tau(D(n)) and the (-1)-sphere values (1,7); (iii) round S^3/Gamma charge and exact agreement with Lemma Q/Q' including the sign of eta; (iv) the Taub–NUT adiabatic derivation and whether E=O(R^-2) is justified; (v) G1, G2, and G3, including topology, quantifiers, multi-class counting, and exactly which bubble-tree degenerations G3 excludes for the certified ball-quotient cell. Identify and repair any statement stronger than the formulas prove.

## Output

# Verification of the Step 33 link-charge theorem and its applications

Convention used throughout: \(w_\pm(\Omega)=\frac1{2\pi^2}\int_\Omega|W^\pm|^2\) and \(\varsigma(\Omega)=\frac1{96\pi^2}\int_\Omega s^2\).

## Summary

- **Theorem G and \(\mathcal Q_\pm=2\mathcal E\mp3\mathcal H\)** are correct as stated.
- **Model charges 1, 2, 3 and 5** are correct.
- **Model 4** is correct for Taub–NUT links. Two statements around it need repair: the "self-dual filling" formula, and the unstated Hopf chirality.
- **G1** is correct and extends to a Betti-number form.
- **G2** is correct once three implicit hypotheses are made explicit.
- **G3** is correct as an inequality for \(k=1\). Its title, its "curvature scale" sentence, and its multi-class reading say more than the formulas give.

There is also one identity, not stated in Step 33, that unifies and strengthens G2, G3 and Corollary X2 (§3 below).

## 1. Theorem G, the sign of \(\mathcal Q_\pm\), and annular orientation

**The identity.** With \(|W|^2=|W^+|^2+|W^-|^2\):
\[
2e\pm3L=\tfrac1{4\pi^2}\bigl(|W|^2\pm(|W^+|^2-|W^-|^2)\bigr)-\tfrac1{8\pi^2}|\mathrm{Ric}^\circ|^2+\tfrac{s^2}{96\pi^2}
=\tfrac1{4\pi^2}\bigl(2|W^\pm|^2-\tfrac12|\mathrm{Ric}^\circ|^2+\tfrac{s^2}{24}\bigr).
\]
Integrating and inserting the two transgression formulas gives
\[
\int_\Omega(2e\pm3L)=2\chi\pm3\tau-2\mathcal E\pm3\mathcal H .
\]
Solving for \(\widehat P\) yields exactly \(\mathcal Q_\pm=2\mathcal E\mp3\mathcal H\).

**Normalization check on the CH ball.** Here \(|W^+|^2=24\), \(s^2=576\), \(\mathrm{Vol}\,B_\tau=\frac{\pi^2}{2}\sinh^4\tau\). So \(w_+=6\sinh^4\tau\) and \(\varsigma=3\sinh^4\tau\). Since \(\widehat P=0\), \(\chi=1\) and \(\tau=0\), this gives \(\mathcal Q_+=2-9\sinh^4\tau\) and \(\mathcal Q_-=2-3\sinh^4\tau\) (model 5). Two consequences:
- \(\mathcal H=\frac16(\mathcal Q_--\mathcal Q_+)=\sinh^4\tau=\int_{B_\tau}L\), as the signature formula requires.
- \(2\mathcal E=2-6\sinh^4\tau\), which is the \(\mathfrak b\) row of Step 27.

**Orientation reversal.** For a closed manifold cut along \(\Sigma\), \(\chi\) is additive because \(\chi(\Sigma^3)=0\), and \(\tau\) is additive by Novikov. Since \(\int e\) and \(\int L\) are additive, \(\mathcal E_A(\Sigma)+\mathcal E_B(\Sigma)=0\) and \(\mathcal H_A+\mathcal H_B=0\). Structurally, Chern's transgression is odd in the second fundamental form.

**Annulus inequality.** \(\widehat P(C)\ge\mathcal Q_\pm(\text{out})-\mathcal Q_\pm(\text{in})\) needs \((2\chi\pm3\tau)(C)=0\). This holds for \(C\cong\Sigma^3\times I\). For a region between two links that carries topology, the term \(-(2\chi\pm3\tau)(C)\) must be kept. The same applies to the pricing rule and to the pathwise \(\int\max\{0,\mathfrak B_\pm'\}\) bound, which also needs \(s\equiv-24\) on each sub-annulus.

**Continuity topology.** Section 2 of the note states that \(\mathcal H\) is continuous for links converging in the \(C^1\) collar topology. Both \(\mathcal E\) and \(\mathcal H\) contain curvature of the 4-metric along the link (second derivatives). For \(\mathcal H\), the Chern–Simons part contains \(\int\delta\wedge d\delta\), which need not vanish when the connection difference \(\delta\to0\) only uniformly. The correct statement is \(C^2\) (or \(W^{2,p}\) with \(p\) large enough) collar convergence. That is the topology G2 already uses.

## 2. Model charges

### Model 1 (round link in a flat region)
\(\mathcal E=1\) and \(\mathcal H=0\), so \((2,2)\). Correct.

### Model 2 (round \(S^3/\Gamma\) end) and agreement with Lemmas Q and Q′
On the truncation \(N_R\), (G) gives
\[
\widehat P(N)\ge \tfrac2{|\Gamma|}-2\chi\mp3(\tau+\eta_\Gamma).
\]
The better chirality gives Lemma Q exactly, provided Lemma Q's \(\eta\) is \(\lim\mathcal H\) with the end oriented as the outgoing link of \(N\), under the convention \(\int L=\tau+\mathcal H\).

This sign is a real constraint, not a convention to be read off a table. Take the Gibbons–Hawking \(A_{k-1}\) ALE space in its complex orientation (\(W^+=s=0\), \(\chi=k\), \(\tau=-(k-1)\)). Gauss–Bonnet gives \(\frac1{8\pi^2}\int|W^-|^2=k-\frac1k\). Hence
\[
\mathcal H_\infty=-\tfrac23\bigl(k-\tfrac1k\bigr)+(k-1)=\frac{(k-1)(k-2)}{3k}.
\]
With this sign, Lemma Q is an equality (value 0) for every \(k\), consistent with \(P=0\):
- \(k=2\): Eguchi–Hanson, \(\eta=0\) (\(\mathbb{RP}^3\) admits an orientation-reversing isometry).
- \(k=3\): \(\tau+\eta=-16/9\).

With the opposite sign at \(k=3\), the right side of Lemma Q would be \(4/3>0=\widehat P\), a contradiction. Any \(\eta_\Gamma\) imported from the lens-space literature must be oriented to match this.

**Lemma Q′ is (G)\(_+\).** Substituting \(\int|W^-|^2=\int|W^+|^2-12\pi^2(\tau+\mathcal H)\) into \(\widehat P=\frac1{4\pi^2}\int|W|^2+\varsigma-2\chi+2\mathcal E\) gives (G)\(_+\) identically. Lemma Q′'s chain \(2\int|W|^2\ge24\pi^2\) is therefore the same inequality, and \(\chi(U)=2\) exactly, because \(b_3(U)=b_1(U)=0\).

### Model 3 (thin tube around \(\Sigma\))
- \(H_2(D(n))=\mathbb Z[\Sigma]\) with form \((n)\), so \(\tau=\operatorname{sgn}n\); \(\chi(D)=\chi(\Sigma)\).
- \(\int_{D_\varepsilon}e\) and \(\int_{D_\varepsilon}L\) are \(O(\varepsilon^2\,\mathrm{Area}(\Sigma)\sup|\mathrm{Rm}|^2)\).
- Hence \(\mathcal Q_\pm\to2\chi(\Sigma)\pm3\operatorname{sgn}n\), and \((1,7)\) for \(\chi=2\), \(n=-1\). Correct.
- The formula also holds for \(n=0\), where \(\tau=0\) for the degenerate form.

The limit is for a fixed smooth metric. At finite radius the exact value is
\[
\mathcal Q_\pm(\partial D_\varepsilon)=2\chi\pm3\operatorname{sgn}n+\widehat P(D_\varepsilon)-w_\pm(D_\varepsilon)-\varsigma(D_\varepsilon).
\]
Along sequences whose curvature concentrates at the bolt, \((1,7)\) holds only for tubes thin relative to the curvature scale. This matters only when the tube charge is used as an inner link value inside a degenerating sequence.

### Model 4 (Hopf-adiabatic Berger link)

**Rate of \(\mathcal E\).** In ambient form, Chern's integrand is a sum of \(\varepsilon^{abc}k_a\tilde R_{bcbc}\)-type terms and \(k_1k_2k_3\). In intrinsic form, the linear terms combine to \(\sum_ak_aK_{bc}\) with \(\{a,b,c\}\) distinct, because \(\tfrac12R_\Sigma-\mathrm{Ric}_{aa}=K_{bc}\) in three dimensions.

Every term therefore contains one principal curvature paired with the curvature of the complementary plane, or the product of all three principal curvatures. Taub–NUT is \(U(2)\)-invariant, so the second fundamental form \(k\) is diagonal.
- Leading terms: \(k_fK_{bb}\sim R^{-4}\) and \(k_fk_b^2\sim R^{-4}\); the mixed term \(k_bK_{fb}\sim R^{-5}\).
- Equivalently, using ambient curvature \(|\mathrm{Rm}|=O(r^{-3})\): \(k\tilde R\sim R^{-4}\).
- With area \(O(R^2)\), this gives \(\mathcal E=O(R^{-2})\). The rate is justified.
- The rate depends on this index structure. The crude bound \((|k||\mathrm{Rm}_\Sigma|+|k|^3)\cdot\mathrm{Area}\) gives only \(O(R^{-1})\), which still suffices for \(\mathcal E\to0\).

**Eta-free derivation of \(\mathcal H\to2/3\).** The argument uses only:
- \(\chi=1\), \(\tau=0\);
- Ricci-flatness and \(W^-=0\);
- \(\mathcal E\to0\).

These give \(\frac1{8\pi^2}\int|W^+|^2=1\), hence \(\int L=2/3\), \(\mathcal H\to2/3\), and charges \((-2,2)\). In Bianchi-IX variables, \(V=c'a/c=O(r^{-1})\) and \(\lambda\to0\), so \(\lambda^2(U-V)^2\to0\). The diagonal formula agrees.

**Independent chirality check from Taub-bolt.** Taub-bolt has \(w_+=3\), \(w_-=5\), \(\chi=2\), \(\tau=-1\). Then:
- (G)\(_+\): \(0=3-1+\mathcal Q_+\), so \(\mathcal Q_+=-2\).
- (G)\(_-\): \(0=5-7+\mathcal Q_-\), so \(\mathcal Q_-=2\).
- Euler: \(\frac1{8\pi^2}\int|W|^2=2=\chi\), so \(\mathcal E_\infty=0\).
- Signature: \(\frac1{12\pi^2}(6\pi^2-10\pi^2)=-\frac13=\tau+\mathcal H\), so \(\mathcal H=\frac23\).

These are four mutually consistent identities. They confirm that the Hopf circle collapsing at the \(O(-1)\) bolt end corresponds to the Taub–NUT with \(W^-=0\) in the blow-up orientation.

**Repair (a): the self-dual filling formula.** "\(\mathcal H_{\rm ad}=\frac23(1-\mathcal E_{\rm ad})\) for any controlled self-dual filling" needs a Ricci-flat filling of a homology ball with \(W^-=0\). With \(s\ne0\) or \(\mathrm{Ric}^\circ\ne0\), Gauss–Bonnet contains \(\int s^2\) and \(\int|\mathrm{Ric}^\circ|^2\), and the relation changes.

**Repair (b): the Hopf chirality.** Reversing the ambient orientation leaves \(\mathcal E\) unchanged and flips \(\mathcal H\), so \(\mathcal Q_\pm\leftrightarrow\mathcal Q_\mp\).
- A link collapsing along the opposite Hopf circles has charges \((2,-2)\). Its controlled filling is Taub–NUT with \(W^+=0\).
- Diagonal Bianchi IX sees only \((-2,2)\), because all slots use left-invariant forms. Symmetry-free links can collapse either way.
- "Hopf-adiabatic \(\Rightarrow(-2,2)\)" should name the chirality.
- For non-invariant collapsing links, the value is established only under the link-regularity conditions (a) and (c) of §2 of the note, including the Dai correction.

### Model 5 (CH geodesic sphere)
Verified above, including \(\mathfrak B_-\equiv2\) and \(\mathfrak B_+=2-6\sinh^4\tau\).

## 3. A filling identity that unifies G2, G3 and Corollary X2

Let \(B\) be any compact homology ball (not necessarily inside \(M\)) carrying a metric whose collar germ at \(\partial B\) equals that of \(\Sigma\), with \(\Sigma\) outgoing on the same side. Then (G) on \(B\) gives
\[
\mathcal Q_\pm(\Sigma)=2+\widehat P(B)-w_\pm(B)-\varsigma(B),\qquad\text{so}\qquad \mathcal Q_\pm(\Sigma)\ge2-w_\pm(B)-\varsigma(B).
\tag{F}
\]
For two fillings \(D\) and \(B\) of the same germ,
\[
\widehat P(D)-\widehat P(B)=-\Delta(2\chi\pm3\tau)+\Delta w_\pm+\Delta\varsigma .
\]
This is Theorem C for arbitrary germs; Theorem C itself is the case \(B=\) CH ball.

Consequences:
- Roundness is not needed. Any germ \(C^2\)-close, after rescaling, to the germ of an embedded \(S^3\subset\mathbb R^4\) has \(\mathcal Q_\pm=2-o(1)\). The bounded complement of an embedded \(S^3\) is a homology ball by Alexander duality.
- The CH ball gives Corollary X2.
- Taub–NUT with \(W^+=0\) gives \(\mathcal Q_+=2\) for the opposite-Hopf collapsed links.

## 4. G1 in Betti-number form

The topology of \(D\) is correct:
- \(\chi=1+k_D-2\ell_D\), \(\tau=-k_D\), so \(2\chi+3\tau=2-k_D-4\ell_D\).
- Handle check: \((S^1\times S^3)\setminus B\) has \(\chi=-1\).

For any compact \(D\) with \(\partial D\cong S^3\), Lefschetz duality gives \(b_3=b_1\). With \(b_2^\pm\) the ranks of the maximal positive- and negative-definite subspaces of the intersection form,
\[
2\chi+3\tau=2-4b_1+5b_2^+-b_2^-,\qquad 2\chi-3\tau=2-4b_1-b_2^++5b_2^- .
\]
So
\[
\widehat P(D)\ge b_2^-+4b_1-5b_2^+-(2-\mathcal Q_+).
\]
G1 is the case \(b_2^+=0\), \(b_2^-=k_D\), \(b_1=\ell_D\). The connected-sum diffeomorphism type of \(D\) is not used, and the same formula holds rationally for rational homology sphere links.

## 5. G2: quantifiers and hidden hypotheses

The inequality \(\widehat P\ge\sum_i(k_i+4\ell_i-\varepsilon_i)\) is correct, with additivity over disjoint \(D_i\) and the bulk dropped since \(P(g;B)\ge0\). The phrase "enclosed by an almost-round almost-flat link" needs three explicit hypotheses:

1. **Side.** \(D_i\) lies on the bounded (ball) side of the flat model collar. If \(D_i\) is on the exterior side, \(\mathcal Q_+(\partial D_i)=-2\) and G2 says nothing.
2. **Trivial group.** \(\partial D_i\cong S^3\) with trivial \(\Gamma\). Orbifold necks \(S^3/\Gamma\) have \(\mathcal Q_\pm=2/|\Gamma|\mp3\eta_\Gamma\) and fall outside G1's topology. They require the \(\Gamma\)-version of (G) together with the actual \(\chi,\tau\) of \(D\).
3. **Collar regularity.** \(C^2\) collar convergence (§1).

By (F), hypothesis 3 can be replaced by: each germ admits a homology-ball filling with \(w_+ +\varsigma\le\varepsilon_i\).

## 6. G3: what is proved and which degenerations it excludes

**What is proved.** For every metric on \(X\#\overline{\mathbb{CP}}^2\) and every \(D\) with \(\partial D\cong S^3\), \(b_2^-(D)\ge1\), \(b_2^+(D)=0\):
\[
\mathcal Q_+(\partial D)\le1+\widehat P(D)\le1+\widehat P .
\]
The note's strict "<" should be "≤". Equality forces \(W^+=s=0\) on \(D\).

**Role of the ball quotient.** It enters only to make the class \(\{\widehat P<1-\varepsilon\}\) nonempty for \(\varepsilon<1-p_*=0.004152\). This uses the cell insertion, which needs an embedded CH ball containing the modified region of the cell.

By (F), the result is a statement about germs: every homology-ball filling \(B\) of \(\partial D\) has
\[
w_+(B)+\varsigma(B)\ge1-\widehat P(D)+\widehat P(B).
\]

**Excluded below threshold, for \(k=1\):** a link enclosing the class (with \(b_2^+(D)=0\), \(D\) on the bounded side) whose germ is any of the following:
- \(C^2\)-almost-flat at its own scale (any shape, any scale);
- a CH sphere with \(9\sinh^4\tau<1-\widehat P\);
- an opposite-Hopf controlled collapsed link (\(\mathcal Q_+=2\)). This is new, and it makes any opening analysis from such links unnecessary.

**Not excluded:**
1. Hopf-collapsed necks (\(\mathcal Q_+\approx-2\)), including Taub-bolt-type ALF bubbles at zero cost. G3 is silent on these.
2. Curved necks with \(\mathcal Q_+\le1+\widehat P\), such as CH spheres with \(\sinh^4\tau\ge(1-\widehat P)/9\) or links with large collar shear.
3. \(S^3/\Gamma\) necks.
4. Regions \(D\) containing \(b_2^+\) of the bulk.
5. **Bulk bubbling.** The ball-quotient side \(D_2=X\setminus B\) sits on the ball side of a round neck, with the \(\overline{\mathbb{CP}}^2\) side large. Here \(\mathcal Q_\pm(\partial D_2)=2\), \((2\chi+3\tau)(D_2)=3\chi(X)-2\) and \((2\chi-3\tau)(D_2)=\chi(X)-2\). This gives
   \[
   \widehat P(D_2)\ge\max\{4-3\chi(X),\,4-\chi(X)\}.
   \]
   - For a fake projective plane (\(\chi=3\)) this is \(1\), so the configuration is excluded, provided the cell fits.
   - For \(\chi(X)\ge6\), including the finite covers used for injectivity radius, the bound gives no information.

"Near-minimizers are not bubble trees" and "concentrate only at curvature-scale links" should therefore read: no near-minimizer separates the exceptional class by an almost-flat \(S^3\) germ, or by an opposite-Hopf collapsed germ, with the class on the bounded side.

**Multi-class count.** The count is correct: with \(m\le K\), \(K-m\varepsilon\le\widehat P\) gives \(K\le\widehat P/(1-\varepsilon)\). For \(\widehat P\le kp_*+\delta\), however, the number of classes that cannot be round-separated is only guaranteed to be
\[
\ge k-\Bigl\lfloor\frac{kp_*+\delta}{1-\varepsilon}\Bigr\rfloor\approx0.004152\,k ,
\]
rounded up to at least 1. Up to about \(0.996k\) classes may be round-separated.

Proving that all \(k\) classes stay unseparated would need a lower bound for the cost of the remaining \(k-K\) unseparated classes in the bulk. That is a positive lower bound of the type \(p_{1,0}>0\), which is open.

## 7. Remaining arithmetic

These all check:
- the volume-renormalized opening bounds \(4-9\sinh^4\tau+3\Delta\widehat V\) and \(3(\Delta\widehat V-\sinh^4\tau)\), given product topology and \(s\equiv-24\);
- Lemma Z(i): \((A-1)^2+4\), and \(A^2+s^2(5-2A)\) monotone for \(A\ge5/2\), with endpoint \(\tau>\operatorname{asinh}\sqrt{5/6}=0.8165\);
- Lemma Z(ii): \(\mathfrak b_+\equiv-2\) on \(u=(A,A,-2)\);
- Corollary X3's threshold \(\tau<0.7005\).

The shape-dependent \(\mathfrak b_-\) formula in Z(ii) depends on the \(\gamma(\beta,q)\) definitions in the script and was not recomputed here.
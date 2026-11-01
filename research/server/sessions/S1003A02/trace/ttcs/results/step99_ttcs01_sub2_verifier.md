# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step96_suvaina_lattice_and_kahler_filler_theorem.md",
    "Sessions/S1003A02/workspace/scripts/step98_wahl_gluing_lattice.py",
    "Sessions/S1003A02/workspace/data/step98/wahl_gluing_lattice.json",
    "Sessions/S1003A02/workspace/notes/step55_k1_orbifold_gate_charges_lattices_collapse.md"
  ]
}
```

## Task

Independently verify Proposition 98.W and Corollary 98.V in §3 of the Step-96/98 note. Reconstruct every Mayer–Vietoris, torsion, duality, Frattini, lattice-index, discriminant-linking, and five-square-block step. Check multiple Wahl balls, torsion in H1(X), boundary orientation/sign conventions, the generator/order calculation in the discriminant group, and the precise range k>=5t. Identify any missing hypothesis or overbroad conclusion, especially whether the bilinear condition can be said never to obstruct outside that range. Compare with the Step-55 second-filling condition and explain exactly why it is independent. Give a direct mathematical memo with repairs if needed.

## Output

# Memo: verification of Proposition 98.W and Corollary 98.V (Step-96 note §3)

## Summary

- **Proposition 98.W.** Items 1–3 are correct as proved. Item 4 is correct, but two things should change:
  - The "metabolizer" clause needs a sharper statement.
  - The hypothesis that \(H_1(X)\) is torsion-free can be removed.
- **A missing structural fact.** Every class pulled back from \(X\) lies in \(L\). So the whole bilinear problem lives in the definite part \(-I_k\). This has several consequences:
  - No Wahl ball embeds when \(k=0\).
  - There is a \(p\)-rank lower bound on \(k\).
  - At \(k=1\) the condition reproduces the Step-55 parity law exactly.
- **Corollary 98.V** is correct as a sufficient condition. Five coordinates per ball can be reduced to four, and four is sharp for a single ball. Below the stated range the bilinear condition does obstruct.
- **The Step-55 second-filling condition is not independent of item 4.** For Wahl balls under the standing \(\pi_1\) hypothesis, the two conditions are equivalent. Datum (0) in the note's list of remaining data should be merged into item 4.

---

## 1. Proposition 98.W, step by step

**Item 1: Mayer–Vietoris and the Frattini argument.**

- The sequence \(H_1(Y)\to H_1(W)\oplus\bigoplus H_1(B_\ell)\to H_1(M)\to 0\) is exact. Exactness at the right needs \(H_0(Y)=\mathbb Z^t\to H_0(W)\oplus\bigoplus H_0(B_\ell)=\mathbb Z^{1+t}\) to be injective. It is, because each \(Y_\ell\) maps to its own \(H_0(B_\ell)\). The note omits this step, but it holds.
- Since \(\pi_1(B_\ell)\) is finite and \(\pi_1(M)\cong\pi_1(X)\) is torsion-free, \(\iota_{B*}=0\). Hence \(j(\ker i)=\bigoplus H_1(B_\ell)\), that is, \(\ker i+K=G\).
- \(j_\ell:\mathbb Z_{n^2}\to\mathbb Z_n\) is onto, so its kernel is the unique index-\(n\) subgroup \(n\mathbb Z_{n^2}\). Since \(j=\oplus j_\ell\) is diagonal, \(K=\bigoplus n_j\mathbb Z_{n_j^2}\).
- \(\Phi(\mathbb Z_{n^2})=\mathrm{rad}(n)\mathbb Z_{n^2}\supseteq n\mathbb Z_{n^2}\). The Frattini property for finite groups (\(S+\Phi=G\Rightarrow S=G\)) holds even when the \(n_j\) share primes. So \(i=0\).
- Sanity check: \(B_2\subset\overline{\mathbb{CP}}^2\). The complement is the Euler-number-4 disk bundle, which is simply connected, so \(i=0\) there.

**Item 2.** \(H_2(Y)=0\) because lens spaces have \(H_2=H^1=0\). Then \(0\to H_2W\to H_2M\to\ker(i,j)=K\to0\). Correct.

**Item 3.**
- \(H_1(W)\cong H_1(M)\) is correct.
- \(H_1(W)\hookrightarrow H_1(W,Y)\to\mathbb Z^{t-1}\to0\) splits, so the torsion parts agree.
- \(\mathrm{Tor}H_2W\cong\mathrm{Tor}H^3W\cong\mathrm{Tor}H_1(W,Y)\cong\mathrm{Tor}H_1M\cong\mathrm{Tor}H_2M\).
- An injection between finite groups of equal order is an isomorphism.
- Two steps are implicit and both hold: \(L\to U\) is injective (if \(m f(x)=0\) then \(x\) is torsion), and the snake lemma gives \(0\to L\to U\to K\to0\).
- Hence index \(\prod n_j\) and \(|\det L|=\prod n_j^2\). Correct.

**Item 4.**
- \(0\to L\xrightarrow{Q}L^*\to H_1(Y)\xrightarrow{0}\) is correct, and the boundary-linking formula is standard.
- Orientation bookkeeping: \(\partial W=\bigsqcup(-\partial B_j)\). Fix one universal convention sign \(\varepsilon\) (with \(b_W=\varepsilon\lambda_{\partial W}\)). Then
  \[
  \operatorname{disc}(L)\cong\bigoplus_j -\varepsilon\,\lambda_{\partial B_j},
  \]
  and the orientation of each ball enters through \(\lambda_{\partial B_j}\).
- This matters because \(\lambda\) and \(-\lambda\) on \(\mathbb Z_{n^2}\) are isometric only when \(-1\) is a unit square mod \(n^2\). For small \(k\) the sign of each ball changes the answer (§4).

**Repair of the metabolizer clause.** "Metabolizer \(U/L\cong K\)" is too weak as written: it is only an abstract isomorphism. The correct statement is that under the boundary identification \(L^*/L\cong H_1(Y)\), the subgroup \(U/L\) maps *onto* \(K=\bigoplus n_j\mathbb Z_{n_j^2}\). Both maps are the restriction/boundary from \(H_2(M)\).

The distinction is real when several \(n_j\) share a prime. For example, \(\mathbb Z_{p^2}^2\) contains isotropic subgroups of order \(p^2\) such as \(\langle(1,u)\rangle\) that are not \(\oplus p\mathbb Z_{p^2}\). The realizability question must ask for the compatible pair (form, \(K\)). Corollary 98.V does produce the compatible pair (§3).

**Removing the torsion-free \(H_1(X)\) hypothesis from item 4.** Let \(T=\mathrm{Tor}H_1W\cong\mathrm{Tor}H_1X\). The map \(H_2W\cong L\oplus T\to H_2(W,Y)\cong L^*\oplus T^\vee\) is injective, since \(H_2Y=0\). It is block-triangular, \((l,t)\mapsto(Ql,\ \varphi(l)+\psi(t))\); there is no torsion-to-free component.

- The cokernel is \(H_1(Y)\), of order \(\prod n_j^2=|\det Q|\). Hence \(\psi:T\to T^\vee\) is injective with equal order, so it is an isomorphism.
- Eliminating \(T^\vee\) through \(\psi\) gives \(\mathrm{coker}\cong L^*/QL\).
- The linking computation is unchanged. Represent \(x\) by \((\lambda,0)\), write \(n x=\) image of \((l,-\psi^{-1}\varphi(l))\) with \(Ql=n\lambda\), and pair against \(y\). The torsion pairs to zero, giving \(Q^{-1}(\lambda,\mu)\bmod 1\).

So item 4 holds whenever \(\pi_1(X)\) is torsion-free. The sentence saying that this bookkeeping "is not done" can be replaced by this argument.

## 2. Missing fact: the lattice condition lives in \(-I_k\)

**Lemma.** \(c^!H_2(X)\subset\operatorname{im}(H_2W\to H_2M)\). Consequently \(L=Q_X\oplus L_0\) with \(L_0=L\cap\ker c_*\subset -I_k\).

*Proof.*
- The classifying map \(c:M\to X\) is homotopic to the collapse map, since both induce the identity on \(\pi_1\) and \(X\) is aspherical.
- \(c|_{B_j}\) is trivial on \(\pi_1\), so it lifts to the contractible \(\widetilde X\) and is null-homotopic. Hence \(c^*H^2(X)\to H^2(B_j)\) is zero.
- The exact sequence \(H^2(M,\sqcup B)\to H^2(M)\to\bigoplus H^2(B_j)\), together with excision and Lefschetz duality \(H^2(M,\sqcup B)\cong H^2(W,Y)\cong H_2(W)\), gives \(c^!H_2X\subset\operatorname{im}H_2W\).
- \(Q_X\) is unimodular mod torsion, so it splits off \(L\) orthogonally. \(\square\)

The same sequence shows that \(U/L\cong K\) is exactly the image of restriction \(H^2(M)\to\bigoplus H^2(B_j)=\bigoplus\mathbb Z_{n_j}\). This restriction is therefore onto, and it factors through \(\ker c_*=-I_k\).

**Consequences.**

- **(i) \(k=0\).** No Wahl ball with \(n\ge2\) embeds in \(X\) itself, for any aspherical \(X\). In that case restriction would be both zero and onto \(\mathbb Z_n\).
- **(ii) \(p\)-rank bound.** \(L_0^*/L_0\cong\bigoplus\mathbb Z_{n_j^2}\) needs at least \(\#\{j:p\mid n_j\}\) generators, so
  \[
  k\ \ge\ \max_p\#\{j: p\mid n_j\}.
  \]
- **(iii) Corollary 98.V's choice is forced.** Placing the \(v_j\) in \(-I_k\) is necessary, not merely convenient. The \(Q_X\) coordinates can never help.

## 3. Corollary 98.V: verification and sharpening

**Verification of the construction.** With disjoint supports, \(\gcd(N_j,n_j)=1\) holds automatically, because \(N_j\equiv-\sigma_j(n_ja_j-1)u_j^2\) is a unit.

- **Index.** \(x\mapsto(x\cdot v_j\bmod n_j)_j\) is onto, so \([U:L]=\prod n_j\).
- **Order of the generators.** Suppose \(m\,v_j/n_j\in L\).
  - Primitivity, or merely content coprime to \(n_j\), forces \(n_j\mid m\).
  - Then \((m/n_j)N_j\equiv0\pmod{n_j}\) forces \(n_j\mid m/n_j\).
  - So \(v_j/n_j\) has order exactly \(n_j^2\).
- **Independence.** Disjoint supports reduce \(\sum m_jv_j/n_j\in L\) to the individual conditions. The generated subgroup has order \(\prod n_j^2=|L^*/L|\), and the cross pairings vanish.
- **Metabolizer.** \(v_j\in U\setminus L\) equals \(n_j\cdot(v_j/n_j)\). So \(U/L=\bigoplus\langle v_j\rangle=\bigoplus n_j\mathbb Z_{n_j^2}\), which is the compatible \(K\) required by the repaired item 4.
- **Self-pairing.** \(-N_j/n_j^2\equiv\sigma_jq_ju_j^2/n_j^2\). On a cyclic group the form is determined by one generator's value up to unit squares. Also \(q^{-1}=q\,(q^{-1})^2\), so the choice between the \(q\) and \(q^{-1}\) lens conventions is immaterial.
- **Spot checks of the JSON.** \((4,1,+1)\): \(N=5\equiv-3\cdot9\pmod{16}\), and the self-pairing is \(11/16=27/16\bmod 1\). \((8,1,-1)\): \(N=7\equiv7\cdot1\pmod{64}\).
- **What the script does and does not test.** It does not compute the discriminant from \(G^{-1}\); the self-pairing is inserted from theory. It tests only \(t=1\). The proof above covers both gaps.

**Sharpening to four coordinates.** Primitivity is not needed. Only content coprime to \(n_j\) is needed, and this is implied by \(\gcd(N,n)=1\). Lagrange's theorem gives \(N\) as a sum of four squares, so \(k\ge4t\) suffices.

**Single-ball minimum.** By §2, every admissible \(L_0\) with \(t=1\) has the form \(L_v=\{x\cdot v\equiv0\bmod n\}\), \(v\in\mathbb Z^k\), with self-pairing \(-v\cdot v/n^2\). Hence
\[
k_{\min}(n,a,\sigma)=\min\{k:\ \text{some sum of }k\text{ squares lies in } -\sigma q\cdot(\text{unit squares})\bmod n^2\}.
\]
Evaluating this:

- \(k=1\) works iff \(-\sigma q\) is a unit square mod \(n^2\):
  - for \(\sigma=+1\): iff \(n\) is odd or \(8\mid n\);
  - for \(\sigma=-1\): iff \(4\nmid n\) and every odd prime dividing \(n\) is \(\equiv1\pmod4\).
- For odd \(n\), \(k\le2\).
- \(k=4\) is needed when \(v_2(n)\ge2\) and \(-\sigma q\equiv7\pmod8\). Example: \((8,1,-1)\), where every admissible \(N\equiv7\pmod8\) and so is not a sum of three squares.
- \(k=3\) is needed at \((2,1,+1)\) and at \((4,1,\pm1)\).
- The script's 5-coordinate vectors are not minimal. For example, \((6,1,+1)\) is realized by \(N=19=9+9+1\) with \(k=3\).

**Answer to "never obstructs outside the range".** "Never an obstruction once \(k\ge5t\)" is true, and so is the improved \(k\ge4t\). Below that range the bilinear condition genuinely obstructs:

- \(k=0\) always;
- \(k<\max_p\#\{j:p\mid n_j\}\);
- the single-ball cases with \(k<k_{\min}\).

The exact multi-ball threshold is a finite but unsolved lattice problem. One needs a definite lattice \(L_0\) of rank \(k\) with discriminant form \(\bigoplus\) (prescribed) and compatible metabolizer \(K\), and the corresponding overlattice must be \(\cong I_k\). This last requirement can fail only for \(k\ge8\). Sharing coordinates between the \(v_j\) may beat \(\sum k_{\min}\).

**Characteristic refinement (datum (a)).** For \(t=1\) and even \(n\), the image of the characteristic vector \(\chi=\sum e_i\) is \(\chi\cdot v\equiv v\cdot v=N\equiv1\pmod 2\). It is therefore the nonzero element of \(H^2(B;\mathbb Z_2)\cong\mathbb Z_n/2\). This matches \(w_2(B_{n,a})\ne0\), provided \(c_1(B_{n,a})\) generates \(H^2(B)=\mathbb Z_n\). That generator fact needs a source; for \(B_2=D(T^*\mathbb{RP}^2)\), \(w_2=w_1^2\ne0\) directly. So the \(w_2\) condition is automatic for single balls, and in the construction for every \(t\). The general multi-ball case is not proved here.

## 4. Step-55 second filling: equivalent, not independent

Let \(C\) be the minimal-resolution plumbing and \(Y'=W\cup C\). Since \(H_1(C)=0\) and \(i=0\), Mayer–Vietoris gives \(L\oplus C\subset H_2(Y')/\mathrm{Tor}\) with glue group \(H_1(Y)\) of order \(n^2=\sqrt{\det L\cdot\det C}\). So \(H_2(Y')\) is the unimodular overlattice glued along the anti-isometry \(\operatorname{disc}(L)\cong\lambda_{\partial W}=-\lambda_{\partial C}\cong-\operatorname{disc}(C)\).

The glue subgroup is a graph over both discriminant groups. Hence:

- \(C\) is automatically primitive;
- \(C^\perp=L\);
- by §2, \(C^\perp\cap\ker c_*=L_0\).

Conversely, a primitive \(C\subset K'\) with \(K'\) unimodular gives \(\operatorname{disc}(C^\perp)\cong-\operatorname{disc}(C)\), which is item 4.

So the second-filling condition is equivalent to item 4 restricted to \(L_0\), for every \(k\). At \(k=1\) both reduce to "\(1-na\) is a unit square mod \(n^2\)". The JSON confirms that the script's \(\sigma=+1\) is the complex orientation of Theorem 55.5:

| \(n\) | \(\sigma=+1\) at \(k=1\) | \(\sigma=-1\) at \(k=1\) | Step-55 law |
|---|---|---|---|
| odd | allowed (\(N=1\)) | — | allowed |
| 2 | not allowed (needs \(N=3\)) | allowed (\(N=1\): reversed \(B_2\subset\overline{\mathbb{CP}}^2\)) | complex orientation excluded |
| 4 | not allowed | not allowed | complex orientation excluded |
| 6 | not allowed (needs \(N=7\)) | — | complex orientation excluded |
| 8 | allowed (\(N=1\)) | — | allowed |

Thus §3's statements that Theorem 55.5 is "a different condition" and "a genuine further integral datum" are not correct. Datum (0) adds nothing beyond item 4. What genuinely remains is:

- the multi-ball definite-lattice threshold of §3;
- the general-\(t\) \(w_2\)/spin\(^c\) compatibility;
- the singular curvature data (b): \(\eta\)/Dedekind terms coupled to a second global identity, orbifold Seiberg–Witten, and type-T analysis.

These conclusions use the standard identification \(\operatorname{disc}(C)\cong\lambda_{\partial C}\) (up to the same \(\varepsilon\)), which is a textbook fact rather than something computed in this session.

## Repairs to the note

1. Item 4: drop the torsion-free \(H_1(X)\) hypothesis, using the block-triangular argument of §1. State the metabolizer as "\(U/L\) corresponds to \(K\) under the boundary identification".
2. Add the Lemma of §2 (\(L=Q_X\oplus L_0\), \(L_0\subset -I_k\)) together with the \(k=0\) and \(p\)-rank consequences.
3. Corollary 98.V: state \(k\ge4t\), remove the primitivity requirement, and give the formula for \(k_{\min}\). Record that below the range the condition obstructs, citing the explicit cases of §3.
4. Merge datum (0) into item 4, citing the equivalence of §4. Note that \(k=1\) recovers Theorem 55.5.
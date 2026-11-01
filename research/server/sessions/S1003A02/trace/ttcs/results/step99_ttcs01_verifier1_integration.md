# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 99,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step99_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step99_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify Proposition 98.W and Corollary 98.V in §3 of the Step-96/98 note. Reconstruct every Mayer–Vietoris, torsion, duality, Frattini, lattice-index, discriminant-linking, and five-square-block step. Check multiple Wahl balls, torsion in H1(X), boundary orientation/sign conventions, the generator/order calculation in the discriminant group, and the precise range k>=5t. Identify any missing hypothesis or overbroad conclusion, especially whether the bilinear condition can be said never to obstruct outside that range. Compare with the Step-55 second-filling condition and explain exactly why it is independent. Give a direct mathematical memo with repairs if needed.

## Integrated Scientific Memo

# Verification memo: Proposition 98.W and Corollary 98.V

## Conclusions and necessary repairs

The Mayer–Vietoris, Frattini, torsion, index, and five-coordinate arguments are valid. They work for multiple Wahl balls, including when their orders share prime factors.

The supplied material supports several stronger conclusions and two substantive corrections:

1. **The torsion-free \(H_1(X)\) hypothesis in item 4 is unnecessary.** Both the discriminant-group identification and the bilinear-form identification survive torsion in \(H_1(X)\). The torsion map in the relative sequence is an isomorphism and can be eliminated.
2. **The metabolizer must be identified as a subgroup:** under the boundary identification, \(U/L\) corresponds to the specified
   \[
   K=\bigoplus_j n_j\mathbb Z_{n_j^2},
   \]
   not merely to an abstractly isomorphic group.
3. **The uniform sufficient bound improves from \(k\ge5t\) to \(k\ge4t\).** Integral primitivity of the chosen vectors is unnecessary; primitivity modulo \(n_j\) suffices.
4. **“Never obstructs” must remain range-qualified.** There are genuine low-rank bilinear obstructions. Four coordinates are a sharp uniform bound for one ball in the definite exceptional sector.
5. **The asserted independence from Step 55 is not correct at the stated abstract lattice level.** Compatible discriminant gluing constructs the primitive resolution-chain embedding. At \(k=1\), the complement condition and Step-55 condition give exactly the same parity law. They concern different fillings, but that does not make their lattice conditions independent.
6. \(U\) is unimodular; it is automatically **odd only if \(k\ge1\)** or \(Q_X\) is already odd.

The precise qualifications concerning asphericity, prescribed ambient lattices, and geometric realization are given below.

---

## 1. Mayer–Vietoris and the multiple-ball Frattini argument

Assume \(M\) is closed and oriented, \(t\ge1\), and the \(B_j\) are standard Wahl balls, with
\[
\pi_1(B_j)=H_1(B_j)=\mathbb Z_{n_j},\qquad H_2(B_j)=0,\qquad
H_1(\partial B_j)=\mathbb Z_{n_j^2}.
\]
Boundary inclusion is onto on \(\pi_1\), hence on \(H_1\). Put
\[
G=H_1(Y)=\bigoplus_j\mathbb Z_{n_j^2},\qquad
R=\bigoplus_j\mathbb Z_{n_j},\qquad
K=\ker(j:G\to R)=\bigoplus_j n_j\mathbb Z_{n_j^2}.
\]

Choose compatible Mayer–Vietoris signs so that its relevant segment is
\[
G\xrightarrow{(i,j)}H_1(W)\oplus R
 \xrightarrow{\iota_W-\iota_B}H_1(M)
 \longrightarrow H_0(Y)
 \longrightarrow H_0(W)\oplus\bigoplus_j H_0(B_j).
\]
The last map is injective: up to signs, it sends
\[
(r_1,\ldots,r_t)\longmapsto
\left(\sum_jr_j,-r_1,\ldots,-r_t\right).
\]
Thus the map onto \(H_1(M)\) is surjective.

Each homomorphism
\[
\pi_1(B_j)\longrightarrow\pi_1(M)\cong\pi_1(X)
\]
is trivial because its source is finite and its target torsion-free. This does **not** require torsion-free abelianization. Therefore every \((0,b)\), \(b\in R\), lies in the Mayer–Vietoris kernel. Exactness yields
\[
j(\ker i)=R,\qquad \ker i+K=G.
\]

For a finite abelian group,
\[
\Phi(G)=\bigoplus_p pG_p.
\]
On every nonzero \(p\)-primary component of \(\mathbb Z_{n_j^2}\), multiplication by \(n_j\) contains a factor of \(p\). Hence
\[
K\subset\Phi(G).
\]
If \(\ker i\ne G\), it lies in a maximal subgroup, which also contains \(\Phi(G)\), contradicting \(\ker i+\Phi(G)=G\). Consequently
\[
\boxed{i=0.}
\]
This argument is unaffected by repeated primes or multiple balls.

Since \(H_2(Y)=0\) and \(H_2(B_j)=0\), the next segment gives
\[
\boxed{0\longrightarrow H_2(W)\longrightarrow H_2(M)
       \longrightarrow K\longrightarrow0.}
\]
The \(H_1\)-segment now gives, via inclusion,
\[
\boxed{H_1(W)\cong H_1(M)\cong H_1(X).}
\]

These establish items 1–2 and the \(H_1\) assertion of item 3.

---

## 2. Torsion, free-lattice index, and determinant

The pair sequence, using \(i=0\), is
\[
0\longrightarrow H_1(W)\longrightarrow H_1(W,Y)
 \longrightarrow\mathbb Z^{t-1}\longrightarrow0.
\]
It splits as an abelian-group sequence, so
\[
\operatorname{Tor}H_1(W,Y)\cong\operatorname{Tor}H_1(W).
\]

Lefschetz duality and universal coefficients imply
\[
\operatorname{Tor}H_2(W)
 \cong\operatorname{Tor}H^3(W)
 \cong\operatorname{Tor}H_1(W,Y).
\]
Likewise, for closed \(M\),
\[
\operatorname{Tor}H_2(M)\cong\operatorname{Tor}H_1(M).
\]
Thus the injective map \(H_2(W)\to H_2(M)\) restricts to an injection between finite torsion groups of equal order, and therefore an isomorphism.

With
\[
L=H_2(W)/\operatorname{Tor},\qquad
U=H_2(M)/\operatorname{Tor},
\]
quotienting the exact sequence by this common torsion gives
\[
\boxed{0\longrightarrow L\longrightarrow U\longrightarrow K\longrightarrow0.}
\]
The map preserves intersection forms. Poincaré duality makes \(U\) unimodular, and connected sum gives
\[
U\cong Q_X\oplus(-I_k).
\]
Therefore
\[
\boxed{[U:L]=\prod_jn_j,\qquad |\det L|=\prod_jn_j^2.}
\]

The adjective “odd” should be qualified as stated above.

---

## 3. Discriminant–linking identification, including host torsion

Let
\[
F=H_2(W),\qquad E=H_2(W,Y).
\]
The pair sequence is
\[
0\longrightarrow F\xrightarrow{J}E
 \xrightarrow{\partial}G\longrightarrow0.
\]
Duality and universal coefficients give
\[
E/\operatorname{Tor}E\cong L^*,\qquad
\operatorname{Tor}E\cong\operatorname{Ext}(H_1(W),\mathbb Z).
\]
From §2, \(\operatorname{Tor}F\) and \(\operatorname{Tor}E\) have the same order. Since \(J\) is injective, its restriction to torsion is an isomorphism. Quotienting by torsion therefore gives
\[
\boxed{0\longrightarrow L\xrightarrow{Q_L}L^*
       \xrightarrow{\bar\partial}G\longrightarrow0,}
\]
without assuming torsion-free \(H_1(X)\).

There is no residual torsion-linking block altering the resulting bilinear form. To see this explicitly, choose splittings
\[
F\cong L\oplus T_F,\qquad E\cong L^*\oplus T_E.
\]
Then
\[
J(l,t)=\bigl(Q_Ll,\varphi(l)+\psi(t)\bigr),
\]
where \(\psi:T_F\to T_E\) is an isomorphism. Eliminating its torsion component identifies the cokernel with \(L^*/Q_LL\).

For the pairing, represent boundary classes by relative lifts with free parts \(\lambda,\mu\in L^*\). If an integer \(m\) kills the first boundary class, its multiple comes from an absolute class whose free part \(l\) satisfies
\[
Q_Ll=m\lambda.
\]
The boundary-linking calculation evaluates the absolute–relative pairing divided by \(m\). Torsion contributes zero to this integer-valued pairing, giving
\[
\lambda_{\partial W}(\bar\partial\lambda,\bar\partial\mu)
 =\varepsilon\,Q_L^{-1}(\lambda,\mu)\pmod{\mathbb Z},
\]
for one fixed convention sign \(\varepsilon\). Thus
\[
\boxed{A_L=L^*/L\cong G}
\]
as groups with bilinear forms, up to that single global sign convention.

This completes the torsion bookkeeping left open in the note.

### Orientation and lens-space conventions

Use different notation for the two induced boundary orientations:
\[
Y_j^B=\partial B_j,\qquad
\partial W=\coprod_j(-Y_j^B).
\]
Consequently
\[
\lambda_{\partial W}=-\bigoplus_j\lambda_{Y_j^B}.
\]
Reversing one ball reverses that component’s linking form. Changing the definition of linking reverses **all** components simultaneously.

For a cyclic lens group of order \(p\), the descriptions using \(q/p\) and \(q^{-1}/p\) are isometric, since
\[
q^{-1}\equiv q(q^{-1})^2\pmod p.
\]
The unit-square formulation in Corollary 98.V correctly accommodates this generator convention.

The sentence “every self-linking value” should read:

> Every **generator’s** self-linking value is \(\pm qu^2/p\), with \(u\) a unit.

Non-generators need not have this form with unit \(u\).

### The specified metabolizer

Naturality of restriction to \(H_2(W,Y)\) and the Mayer–Vietoris boundary map gives
\[
\bar\partial(U/L)=K\subset G.
\]
Moreover \(U/L\) is isotropic because \(U\) is integral, and
\[
|U/L|=\prod_jn_j=\sqrt{|A_L|}.
\]
Hence it is a metabolizer.

The subgroup identification matters when different balls share primes: specifying only its abstract group type does not specify its position in \(G\).

---

## 4. The five-coordinate construction and its four-coordinate improvement

Fix a desired cyclic discriminant form
\[
\left\langle\frac{\sigma q}{n^2}\right\rangle,\qquad
q=na-1,\qquad \sigma\in\{\pm1\}.
\]
Choose a positive integer \(N\) satisfying
\[
N\equiv-\sigma qu^2\pmod{n^2}
\]
for a unit \(u\); \(u=1\) already proves existence. Necessarily \(\gcd(N,n)=1\).

### The stated five-coordinate proof

Choose \(N\ge1\). Lagrange’s theorem supplies
\[
N-1=x_1^2+x_2^2+x_3^2+x_4^2.
\]
Then
\[
v=(1,x_1,x_2,x_3,x_4)\in-I_5,\qquad v^2=-N
\]
is primitive. On disjoint blocks define
\[
\phi:U\longrightarrow\bigoplus_j\mathbb Z_{n_j},\qquad
\phi(x)=(x\cdot v_j\bmod n_j)_j,\qquad L=\ker\phi.
\]
Each component is onto, independently, so
\[
[U:L]=\prod_jn_j.
\]

Set \(g_j=v_j/n_j\). Then \(g_j\in L^*\). If \(r g_j\in L\), integral primitivity first gives \(n_j\mid r\). Writing \(r=n_js\), membership in \(L\) requires
\[
sN_j\equiv0\pmod{n_j}.
\]
Since \(N_j\) is a unit modulo \(n_j\), \(n_j\mid s\). Thus
\[
\operatorname{ord}[g_j]=n_j^2.
\]
Disjoint supports give independence and zero cross-pairings. Their generated group has order \(\prod_jn_j^2=|A_L|\), so
\[
A_L=\bigoplus_j\langle[g_j]\rangle,
\qquad
b_L(g_j,g_j)=-\frac{N_j}{n_j^2}
 \equiv\frac{\sigma_jq_ju_j^2}{n_j^2}\pmod1.
\]
Finally, \(n_jg_j=v_j\) generates the corresponding factor of \(U/L\). The construction realizes the required **form and specified metabolizer**.

### Four coordinates suffice

The fixed first coordinate \(1\) is unnecessary. Represent \(N\), rather than \(N-1\), by four squares:
\[
N=x_1^2+x_2^2+x_3^2+x_4^2.
\]
Because \(\gcd(N,n)=1\),
\[
\gcd(x_1,x_2,x_3,x_4,n)=1.
\]
Thus \(x\mapsto x\cdot v\bmod n\) is onto, even if \(v\) is not primitive over \(\mathbb Z\).

If \(rv/n\) is integral, Bézout modulo \(n\) gives \(n\mid r\). The preceding order argument then applies unchanged. Therefore
\[
\boxed{k\ge4t}
\]
is a valid uniform sufficient bound, with all other conclusions unchanged.

### What the supplied script verifies

The script and JSON are consistent with the five-coordinate construction:

- 54 single-ball cases, \(2\le n\le9\);
- the displayed kernel basis is correct;
- the Gram matrix is \(-BB^T\);
- Smith form is \((1,1,1,1,n^2)\);
- determinant magnitude and the target square class pass.

The script does not independently derive the generator’s self-pairing from \(G^{-1}\): it uses \(-N/n^2\). The proof above supplies that derivation and the multiple-ball argument. No finite computation is needed for the universal result.

---

## 5. The correct low-rank problem over an aspherical host

An additional structural fact applies when \(X\) is aspherical, in particular for a ball quotient. It does **not** follow merely from torsion-free \(\pi_1(X)\).

Let \(c:M\to X\) be the collapse/classifying map. Since the finite \(\pi_1(B_j)\) maps trivially to \(\pi_1(X)\), the restriction \(c|_{B_j}\) lifts to the contractible universal cover and is null-homotopic. Hence
\[
c^*H^2(X)\big|_{\coprod B_j}=0.
\]
The relative cohomology sequence, excision, and duality give
\[
H^2(M,\coprod B_j)\cong H^2(W,\partial W)\cong H_2(W).
\]
Naturality therefore places \(c^!H_2(X)\) inside the image of \(H_2(W)\). On free lattices,
\[
\boxed{L=Q_X\oplus L_0,\qquad L_0\subset-I_k.}
\]

Thus for actual complements over a ball quotient, \(Q_X\) cannot supply extra coordinates to evade the definite exceptional-lattice problem.

Immediate consequences are:

- No nontrivial Wahl ball embeds when \(k=0\).
- For every prime \(p\),
  \[
  \boxed{k\ge\#\{j:p\mid n_j\},}
  \]
  because a rank-\(k\) lattice’s discriminant group has at most \(k\) generators.

For one ball, every index-\(n\) sublattice with quotient \(\mathbb Z_n\) has the form
\[
L_v=\{x\in\mathbb Z^k:x\cdot v\equiv0\pmod n\},
\qquad \gcd(v_1,\ldots,v_k,n)=1.
\]
When its discriminant group is cyclic of order \(n^2\), \(v/n\) is a generator: it generates \(L_v^*/U\), and in a cyclic group of order \(n^2\), any lift of a generator of the quotient by its order-\(n\) subgroup is itself a generator. Consequently the necessary and sufficient arithmetic problem is
\[
\sum_{i=1}^k v_i^2\equiv-\sigma q\,u^2\pmod{n^2}.
\]

This gives explicit obstructions:

- For \(n=2,a=1,\sigma=+1\), every allowed norm is \(3\bmod4\), so one or two squares cannot work. Three suffice.
- For \(n=8,a=1,\sigma=-1\), every allowed norm is \(7\bmod8\), since odd unit squares are \(1\bmod8\). Three squares cannot work. Four suffice, for example
  \[
  7=2^2+1^2+1^2+1^2.
  \]

Hence four is a sharp **uniform single-ball bound** in this definite setting.

The original \(k\ge5t\) claim is true but nonoptimal. The improved \(k\ge4t\) is also sufficient, not a claimed optimal multi-ball threshold. Below it, some configurations pass and others fail. In particular, the unqualified conclusion in §4(b) that bilinear lattice data do not decide the Wahl sector is too broad.

---

## 6. Step 55: different fillings, but not an independent abstract lattice obstruction

The note’s claimed independence cannot be justified. Its two fillings are different, but discriminant gluing connects their lattice conditions directly.

Let \(C=\coprod_j C_j\) be the orientation-compatible resolution plumbing and
\[
Y'=W\cup C.
\]
Since \(H_1(C_j)=0\) and \(i=0\), Mayer–Vietoris gives
\[
0\longrightarrow H_2(W)\oplus H_2(C)
 \longrightarrow H_2(Y')
 \longrightarrow G\longrightarrow0,
\qquad
H_1(Y')\cong H_1(W).
\]
As before, the torsion maps isomorphically. On free lattices,
\[
0\longrightarrow L\oplus C
 \longrightarrow U'
 \longrightarrow G\longrightarrow0,
\]
where \(U'\) is unimodular.

The boundary orientations give an anti-isometry
\[
f:A_L\longrightarrow A_C.
\]
The corresponding gluing lattice is
\[
U'=\{(x,y)\in L^*\oplus C^*:[y]=f([x])\}.
\]
Its glue subgroup is the graph of \(f\). It follows immediately that:

- \(C\) is primitive in \(U'\);
- \(L\) is primitive in \(U'\);
- \(C^\perp=L\).

The same conclusion follows from the pair sequence for \((Y',W)\): \(H_1(W)\to H_1(Y')\) is an isomorphism, so \(U'\to C^*\) is onto, proving primitivity.

For the lattices constructed in Corollary 98.V,
\[
L=Q_X\oplus L_0.
\]
For complex-oriented Wahl points, the glued lattice therefore splits as
\[
U'=Q_X\oplus K',\qquad
K'\supset L_0\oplus C,
\]
where \(K'\) is negative-definite unimodular of rank \(k+\sum_jr_j\), and the chains embed primitively. Thus the corollary’s construction already supplies the abstract second-filling datum described in Step 55. Reversed points require correspondingly reversed plumbings and do not give this negative-definite assertion.

### At \(k=1\), the conditions coincide exactly

Over an aspherical host, \(L_0\subset\langle-1\rangle\) has index \(n\), hence
\[
L_0=\langle-n^2\rangle,\qquad
b_{L_0}=\left\langle-\frac1{n^2}\right\rangle.
\]
The complex-oriented chain has
\[
b_C=\left\langle\frac{1-na}{n^2}\right\rangle.
\]
An anti-isometry between these forms exists exactly when
\[
\boxed{1-na\equiv u^2\pmod{n^2}.}
\]
This is simultaneously:

- the one-coordinate complement condition, with the complex-orientation target sign; and
- Step-55’s primitive chain-embedding condition into some negative-definite unimodular lattice of rank \(r+1\).

For odd primes dividing \(n\), \(1-na\equiv1\pmod p\), and square roots lift. At the prime \(2\), it is a square exactly when \(8\mid n\), unless \(n\) is odd. Therefore
\[
\boxed{n\text{ odd or }8\mid n.}
\]

In particular, the complex-oriented \(B_{2,1}\) already fails the correct complement pairing at \(k=1\). The lattice \(\langle-4\rangle\subset\langle-1\rangle\) has the pairing for the **reversed** \(B_2\), not for the complex-oriented one. It is not an example separating the two conditions.

### The precise distinction that remains

A bare primitive chain embedding into **some** unimodular lattice does not, in higher rank, specify that subsequent rational-ball gluing produces the required diagonal exceptional lattice \(-I_k\). For \(k\ge8\), a definite unimodular lattice need not be diagonal. Thus a converse equivalence requires retaining the prescribed rational-filling overlattice and the labeled metabolizer.

Accordingly:

- Compatible complement data imply the abstract primitive second-filling embedding.
- At \(k=1\), the two numerical conditions coincide.
- In general rank, a bare “some unimodular lattice” formulation can be weaker than the full prescribed rational-filling condition.
- Neither abstract gluing nor primitivity constructs smooth embedded plumbings, embedded Wahl balls, a degree-one map realizing arbitrary lattice data, or an Einstein orbifold.

A constraint on a separately prescribed resolved manifold could add information, but no such extra constraint is supplied here. The claim that Step-55’s stated lattice condition is a “genuine further integral datum” should therefore be removed.

---

## Corrected formulation

A source-supported replacement is:

> Under the standard Wahl-ball hypotheses and torsion-free \(\pi_1(X)\), Proposition 98.W holds, including its discriminant–linking identification, without requiring torsion-free \(H_1(X)\). Under that identification, \(U/L\) is the specified boundary metabolizer \(K\). The ambient free lattice is unimodular, and is odd when \(k\ge1\).
>
> For arbitrary Wahl parameters and orientations, \(k\ge4t\) guarantees an abstract index-\(\prod_jn_j\) sublattice of \(Q_X\oplus(-I_k)\) realizing the required discriminant forms and labeled metabolizer. Below this sufficient range, bilinear obstructions may occur. Over an aspherical host the actual complement lattice splits as \(Q_X\oplus L_0\), so the remaining arithmetic lies entirely in \(-I_k\).
>
> Compatible discriminant gluing also gives the primitive resolution-chain embedding at the abstract lattice level. At \(k=1\), it recovers exactly Step-55’s parity law. Additional unresolved issues concern geometric realization, refinements not established by these arguments, and singular analytic data—not a separate primitive-chain obstruction already implied by the compatible gluing.
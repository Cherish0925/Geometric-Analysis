# TTCS Independent Branch Record

```json
{
  "step_id": 18,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/notes/step17_normalized_cutoff_flow_theorem.md",
    "Sessions/S0910A03/workspace/scripts/verify_step18_noether_topology_bound.py",
    "Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md"
  ]
}
```

## Task

Check the topological-uniformity correction for the critical Ishida–LeBrun family. Derive c2≤5c1²+36 for each minimal complex surface of general type from Noether's formula and Noether's inequality, then compute χ(M)/A for M=(#_{j=1}^m X_j)#N, m=2 or 3, using exact connected-sum formulas and D=4m-(2χ+3τ)(N)=A/3. Determine under the actual standard hypotheses on N in the Ishida–LeBrun construction whether χ(N)/A is automatically bounded above; distinguish what follows from D alone, from negative-definiteness/b1 assumptions, and from the common choices of N. Correct any convention mismatch. The aim is an exact, reusable bound or a precise statement of the missing N input.

## Output

## Scientific memo: topological uniformity for the critical Ishida–LeBrun family

Write
\[
a_j=c_1^2(X_j),\qquad c_j=c_2(X_j)=\chi_{\mathrm{top}}(X_j),
\qquad A=\sum_{j=1}^m a_j,
\]
where \(m=2\) or \(3\).

### 1. Noether gives the required upper estimate

For a minimal complex surface of general type \(X\), let
\[
p_g=h^{2,0}(X),\qquad q=h^{1,0}(X),\qquad
\chi_h=\chi(\mathcal O_X)=1-q+p_g.
\]
Noether’s formula and Noether’s inequality are
\[
c_1^2+c_2=12\chi_h,
\qquad
c_1^2\ge 2p_g-4.
\]
Hence
\[
p_g\le \frac{c_1^2+4}{2},
\qquad
\chi_h=1-q+p_g\le 1+p_g\le\frac{c_1^2+6}{2}.
\]
Substitution into Noether’s formula gives
\[
c_2=12\chi_h-c_1^2
\le 6(c_1^2+6)-c_1^2
=\boxed{5c_1^2+36}.
\]
Therefore
\[
\boxed{\sum_{j=1}^m c_2(X_j)\le 5A+36m.}
\]

The BMY relation relevant here is
\[
c_1^2\le 3c_2,
\]
equivalently \(c_1^2\le 9\chi_h\), not \(c_1^2\le3\chi_h\). It yields
\(c_2\ge c_1^2/3\), an estimate in the opposite direction from the one needed for an upper bound on \(\chi(M)/A\).

---

### 2. Exact connected-sum conventions

For
\[
M=\left(\#_{j=1}^m X_j\right)\#N,
\]
there are \(m+1\) summands and therefore \(m\) connected-sum operations. Thus
\[
\boxed{\chi_{\mathrm{top}}(M)
=\sum_{j=1}^m c_2(X_j)+\chi_{\mathrm{top}}(N)-2m.}
\]
Signature is additive, so
\[
(2\chi+3\tau)(M)
=A+(2\chi+3\tau)(N)-4m=A-D.
\]
At
\[
D=4m-(2\chi+3\tau)(N)=A/3,
\]
this becomes
\[
(2\chi+3\tau)(M)=\frac{2A}{3},
\]
in agreement with the Ishida–LeBrun formula.

For a closed oriented \(N\),
\[
\chi(N)=2-2b_1+b_++b_-,
\qquad
\tau(N)=b_+-b_-,
\]
and consequently
\[
(2\chi+3\tau)(N)=4-4b_1+5b_+-b_-.
\]
Hence
\[
D=4(m-1)+4b_1-5b_++b_-.
\]
Imposing \(D=A/3\) and eliminating \(b_-\) gives the exact identity
\[
\boxed{\chi(N)
=\frac A3+6-4m+6\bigl(b_+(N)-b_1(N)\bigr).}
\tag{1}
\]

This formula precisely separates what follows from \(D\) and what requires information about \(N\).

---

### 3. What follows from the different hypotheses on \(N\)

#### From \(D=A/3\) alone

Equation (1) contains the uncontrolled term \(6(b_+-b_1)\). There is no automatic upper bound for \(\chi(N)/A\).

Indeed, fix
\[
T=(2\chi+3\tau)(N)=4m-\frac A3
\]
and take
\[
N_p=p\,\mathbb{CP}^2\#q_p\,\overline{\mathbb{CP}}{}^2,
\qquad
q_p=5p+4-T.
\]
For all sufficiently large \(p\),
\[
(2\chi+3\tau)(N_p)=4+5p-q_p=T,
\]
whereas
\[
\chi(N_p)=2+p+q_p=6p+6-T\longrightarrow\infty.
\]
This also shows that \(b_1(N)=0\) by itself does not provide the desired upper estimate.

#### Under the standard Ishida–LeBrun hypothesis \(b_+(N)=0\)

Theorem D in the supplied Ishida–LeBrun paper assumes exactly \(b_+(N)=0\). Theorem C assumes that \(N\) carries an anti-self-dual metric of positive scalar curvature, and its proof states that this again implies \(b_+(N)=0\).

With \(b_+=0\), equation (1) reduces to
\[
\boxed{\chi(N)
=\frac A3+6-4m-6b_1(N).}
\tag{2}
\]
In particular, for \(m=2,3\),
\[
\frac{\chi(N)}A
=\frac13+\frac{6-4m-6b_1(N)}A
\le\frac13.
\]
Thus the actual source hypotheses do automatically control \(\chi(N)/A\); no assumption \(b_1(N)=0\) is needed.

The corresponding expression for \(D\) is
\[
\boxed{D=4(m-1)+4b_1(N)+b_-(N).}
\tag{3}
\]
At the critical value,
\[
A=12(m-1)+12b_1(N)+3b_-(N),
\]
so
\[
\boxed{A\ge 12(m-1).}
\tag{4}
\]

#### With \(b_+(N)=0\) and \(b_1(N)=0\)

Writing \(k=b_-(N)\),
\[
(2\chi+3\tau)(N)=4-k,
\qquad
D=4(m-1)+k.
\]
Therefore
\[
\boxed{k=\frac A3-4(m-1),}
\]
not \(k=A/3\). The missing \(4(m-1)\) is the convention mismatch caused by the \(m\) connected-sum operations. In this case
\[
\chi(N)=2+k=\frac A3+6-4m.
\]

---

### 4. Common choices of \(N\)

For the family appearing in Ishida–LeBrun Corollary 16,
\[
N=k\,\overline{\mathbb{CP}}{}^2\#
\ell(S^1\times S^3),
\]
one has
\[
b_1(N)=\ell,\qquad b_+(N)=0,\qquad b_-(N)=k,
\]
and
\[
\chi(N)=2+k-2\ell,\qquad
\tau(N)=-k.
\]
Thus
\[
D=4(m-1)+k+4\ell.
\]
At \(D=A/3\),
\[
\boxed{k+4\ell=\frac A3-4(m-1),}
\]
and
\[
\boxed{\chi(N)=\frac A3+6-4m-6\ell.}
\]
This is equation (2) with \(b_1(N)=\ell\).

---

### 5. Exact formula and reusable uniform bound for \(\chi(M)/A\)

Let
\[
C=\sum_{j=1}^m c_2(X_j).
\]
Combining the connected-sum formula with equation (2),
\[
\chi(M)
=C+\frac A3+6-6m-6b_1(N),
\]
so the exact normalized expression is
\[
\boxed{
\frac{\chi(M)}A
=\frac CA+\frac13+
\frac{6-6m-6b_1(N)}A.
}
\tag{5}
\]

Using \(C\le5A+36m\),
\[
\boxed{
\frac{\chi(M)}A
\le
\frac{16}{3}
+\frac{30m+6-6b_1(N)}A.
}
\tag{6}
\]
Dropping the favorable \(b_1\)-term and using \(A\ge12(m-1)\) yields
\[
m=2:\qquad
\frac{\chi(M)}A
\le \frac{16}{3}+\frac{66}{12}
=\boxed{\frac{65}{6}},
\]
and
\[
m=3:\qquad
\frac{\chi(M)}A
\le \frac{16}{3}+\frac{96}{24}
=\boxed{\frac{28}{3}}.
\]
Consequently, for both \(m=2\) and \(m=3\),
\[
\boxed{\frac{\chi(M)}A\le\frac{65}{6}.}
\]

This constant is independent of \(N\), \(A\), and the individual complex surfaces, provided:

1. each \(X_j\) is a minimal complex surface of general type, so that the Noether estimate applies; and  
2. \(N\) satisfies the standard Ishida–LeBrun condition \(b_+(N)=0\).

For a generalized construction without \(b_+(N)=0\), equation (1) shows that the additional topological input is an upper bound for
\[
\frac{b_+(N)-b_1(N)}A;
\]
an upper bound for \(b_+(N)/A\) is sufficient. Also, the broader almost-complex version of Ishida–LeBrun Theorem D does not itself furnish the Noether estimate for the \(X_j\); there one separately needs an upper bound on \(\sum_j\chi(X_j)/A\).
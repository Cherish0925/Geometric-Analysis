# TTCS Independent Branch Record

```json
{
  "step_id": 43,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step43_routeA_orientation_and_global_allocation.md",
    "Sessions/S0910A02/workspace/data/step43_orientation_obstruction_bookkeeping.json",
    "Sessions/S0910A02/workspace/notes/step42_mode_projection_bridge_resolution.md",
    "Sessions/S0910A02/workspace/data/step42_det_R_plus_computation.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771/object.md",
    "Knowledge/objects/papers/Conformal-Kähler-rigidity-of-Einstein-four-manifolds--ee41ec8c511e--4518ab125268/object.md"
  ]
}
```

## Task

Verify the Step-43 correction to Route A. Read the new Step-43 note, Step-42 mode-projection note/data, the orientation bookkeeping data, and the cited Ozuch/LeBrun-Ozuch/Catino-Dameno source objects. The scientific question is: is the correction sound that det R_+=0 for KE limits is not a ceiling but the orientation-compatible side, while b_+>1 over a KE limit forces reversed EH bubbles testing R_-? Check source fidelity, orientation dictionary, topology/betti bookkeeping for A1/EH bubbles, the claim that Derdzinski-type rigidity does not follow from finitely many singular-point constraints, and the route allocation away from immediate high-order Lambda>0 obstruction theory. Identify any overclaim that would mislead the next research step.

## Output

## Scientific memo

### Overall assessment

The central Step-43 correction is mathematically sound in the \(A_1\)/Eguchi–Hanson setting:

- for a Kähler–Einstein orbifold in its complex orientation, \(\det \mathbf R^+=0\) is automatic;
- the usual Eguchi–Hanson orientation contributes to \(b_-\) and couples to \(\mathbf R^+\);
- orientation reversal contributes to \(b_+\) and couples to \(\mathbf R^-\);
- consequently, if a positive Kähler–Einstein orbifold has \(b_+=1\), then producing a smooth target with \(b_+>1\) requires ALE topology carrying plus-sign intersection directions. For pure EH replacements, these are precisely the \(\zeta^-\) pieces.

The source objects support this dictionary. Several statements still require narrower wording, chiefly because the full local obstruction is direction-dependent and because the cited Ozuch theorem concerns exact Einstein desingularizations, not merely metrics with uniformly small Ricci defect.

---

### 1. Curvature-block and orientation dictionary

Ozuch’s formulas give, for an EH parameter \(\zeta^\pm\),
\[
\lambda_k(\zeta^\pm)
 =c\left\langle
 \mathbf R^\pm(p)\zeta^\pm,\zeta_{(k)}^\pm
 \right\rangle .
\]
Thus all three first obstruction coefficients vanish exactly when
\[
\mathbf R^\pm(p)\zeta^\pm=0.
\]
In particular,
\[
\det \mathbf R^\pm(p)=0
\]
is the existential form obtained after allowing the EH direction \(\zeta^\pm\) to vary.

The asymptotic expansions in the supplied Ozuch source agree with Step 43:

\[
H^4(\zeta^+)
 =-\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4}
\]
couples to \(\mathbf R^+\), while
\[
H^4(\zeta^-)
 =-\frac{\zeta^-\circ\rho(\zeta)^+}{2r^4}
\]
couples to \(\mathbf R^-\).

The topological sign agrees as well. In the source orientation, the EH \(L^2\)-cohomology generator is anti-self-dual, so its square is \(-2\) and it contributes one dimension to \(b_-\). Reversing orientation changes the square to \(+2\), hence contributes one dimension to \(b_+\).

A necessary refinement is that \(\det\mathbf R^+=0\) does **not** mean every \(\zeta^+\) EH direction passes the first obstruction. It means that suitable directions exist. For a positive Kähler–Einstein surface,
\[
\mathbf R^+
 =\operatorname{diag}(\Lambda,0,0)
\]
in the decomposition
\[
\Lambda^+=\mathbb R\omega\oplus\Lambda^2_{+,0}.
\]
Therefore the allowed directions satisfy
\[
\zeta^+\in\Lambda^2_{+,0},
\]
whereas a direction with a Kähler-form component is not annihilated by \(\mathbf R^+\). The Step-43 phrase “automatically satisfies the first obstruction for orientation-compatible EH bubbles” is accurate only at the determinant/existence level.

---

### 2. Kähler–Einstein block calculation

For \(\operatorname{Ric}=\Lambda g\) in dimension four,
\[
\mathbf R^\pm=W^\pm+\frac{\Lambda}{3}I.
\]
In the complex orientation of a Kähler–Einstein surface,
\[
\operatorname{spec}(W^+)
 =\left(\frac{2\Lambda}{3},
 -\frac{\Lambda}{3},
 -\frac{\Lambda}{3}\right),
\]
so
\[
\operatorname{spec}(\mathbf R^+)=(\Lambda,0,0).
\]
This verifies all Step-43 algebra concerning \(\mathbf R^+\).

The supplied model computations for the other block are also correct:

- For Fubini–Study \(\mathbb{CP}^2\), \(W^-=0\), hence
  \[
  \mathbf R^-=\frac{\Lambda}{3}I,
  \qquad
  \det\mathbf R^-=\frac{\Lambda^3}{27}\ne0.
  \]
  No \(\zeta^-\) EH direction satisfies the first obstruction.

- For the equal-radius product \(S^2\times S^2\), the curvature operator on each chirality has spectrum
  \[
  (\Lambda,0,0).
  \]
  Hence both determinants vanish. This is an important model showing that the reversed-orientation condition need not yield a contradiction.

- For general Kähler–Einstein geometry, writing
  \[
  \operatorname{spec}(W^-)=(a,b,-a-b)
  \]
  gives
  \[
  \det\mathbf R^-=
  \left(a+\frac{\Lambda}{3}\right)
  \left(b+\frac{\Lambda}{3}\right)
  \left(-a-b+\frac{\Lambda}{3}\right),
  \]
  exactly as recorded in the JSON file.

Thus the correction from “all KE bubbling is harmless” to “the plus block is pinned but the minus block remains model-dependent” is valid.

---

### 3. Betti-number bookkeeping

For a compact oriented orbifold \(X\) with isolated \(A_1\) points, remove small cone neighborhoods and glue truncated EH pieces along copies of \(\mathbb{RP}^3\). Since
\[
H_1(\mathbb{RP}^3;\mathbb R)
 =
H_2(\mathbb{RP}^3;\mathbb R)=0,
\]
Mayer–Vietoris over \(\mathbb R\) gives an orthogonal splitting of the degree-two intersection form:
\[
H^2(M;\mathbb R)
 \cong H^2(X;\mathbb R)
 \oplus\bigoplus_j\mathbb R[E_j].
\]
Each \(\zeta^+\) piece has \(E_j^2=-2\), while each \(\zeta^-\) piece has \(E_j^2=+2\). Hence
\[
b_+(M)=b_+(X)+N_-,
\qquad
b_-(M)=b_-(X)+N_+,
\]
where \(N_-\) denotes the number of orientation-reversed EH pieces and \(N_+\) the usual ones.

For a compact positive Kähler–Einstein orbifold with isolated quotient singularities, orbifold Hodge theory gives
\[
H^{2,0}(X)=0
\]
by positivity of Ricci curvature, while the Hodge index theorem gives exactly one plus-sign direction in \(H^{1,1}(X;\mathbb R)\). Thus
\[
b_+(X)=1.
\]
This conclusion can be made rigorous directly; it need not remain merely an expectation, provided orbifold de Rham cohomology and the intersection pairing are stated explicitly.

For
\[
M=\#_k(S^2\times S^2),
\qquad
b_+(M)=b_-(M)=k,
\]
the pure EH formulas become
\[
N_-=k-1,
\qquad
N_+=k-b_-(X).
\]
The JSON table implements these formulas correctly. In particular, the number \(k-1\) of reversed EH pieces is independent of \(b_-(X)\).

This exact count applies only when every added degree-two class comes from an EH piece. With higher-rank ALE spaces or bubble trees, the invariant statement is
\[
\sum_{\text{ALE pieces}} b_+^{\mathrm{cpt}}(Y)=k-1.
\]
It need not correspond to \(k-1\) distinct EH bubbles. Moreover, the supplied Ozuch source explicitly notes that a complete classification of Ricci-flat ALE fillings of \(\mathbb R^4/\mathbb Z_2\) is not being used as a general theorem. Hence “\(b_+>1\) forces reversed EH bubbles” is accurate inside the declared \(A_1\)/EH model, but not for arbitrary ALE geometry.

---

### 4. Relation to LeBrun–Ozuch expected topology

LeBrun–Ozuch Definition 8 identifies expected topology with all Ricci-flat ALE pieces being Kähler in the inherited orientation. Such pieces have compact intersection form contributing only to \(b_-\). Starting from a Kähler orbifold with \(b_+=1\), expected topology therefore preserves
\[
b_+(M)=1.
\]
This is consistent with their Theorem 4.1, which places \(M\) among Del Pezzo diffeotypes.

Accordingly, \(\#_k(S^2\times S^2)\), \(k\ge2\), is incompatible with every bubble being Kähler in the inherited orientation. That topological conclusion is sound. Its use for near-Einstein sequences, rather than exact Einstein sequences, rests on the separate bubble-tree reconstruction and symplectic-gluing argument; the cited theorem itself is stated for exact Einstein sequences.

---

### 5. Derdziński/Catino–Dameno rigidity

Step 43 correctly separates finite singular-point equations from global spectral hypotheses.

At a reversed EH point,
\[
\mathbf R^-(p)\zeta^-=0
\]
only says
\[
W^-(p)\zeta^-=-\frac{\Lambda}{3}\zeta^-.
\]
This imposes one specified eigenvalue at one point. It supplies neither eigenvalue multiplicity nor a globally defined eigenline.

By contrast:

- LeBrun–Ozuch Theorem 3.1 uses conditions holding everywhere or almost everywhere, together with compactness and simple connectivity.
- Catino–Dameno assumes the largest eigenvalue is simple at every point, or a uniform spectral separation in its strengthened theorem.

Finitely many equations \(\det\mathbf R^\pm(p_j)=0\) do not imply either hypothesis. Einstein analyticity does not change this: an analytic scalar such as \(\det\mathbf R^-\) may vanish at finitely many points without vanishing identically. The proposed global Kähler upgrade is therefore absent from the current derivation.

---

### 6. Analytic bridge from Ricci pinching

The Ozuch formulas cited in Step 43 concern exact Einstein desingularizations. The extension
\[
\|\operatorname{Ric}(g_i)-\Lambda g_i\|_{L^\infty}\to0
\quad\Longrightarrow\quad
\mathbf R^\pm(p)\zeta^\pm=0
\]
is plausible but not established by Step 42.

The load-bearing analytic objects are:

1. a Bianchi or harmonic gauge on the degenerating neck;
2. three weak mode projections, one for each EH Jacobi field, rather than one scalar pairing;
3. precise division by the bubble scale, showing that the rescaled Ricci defect contributes \(O(\delta_i)\);
4. control of angular-mode coupling from the nonconical metric;
5. nonlinear and gauge commutator estimates on a fixed bubble-frame annulus;
6. the iterated limits \(i\to\infty\) followed by \(R\to\infty\).

The scalar identity
\[
\langle\mathbf R^\pm\zeta^\pm,\zeta^\pm\rangle=0
\]
alone is insufficient: for an indefinite symmetric operator it does not imply
\[
\mathbf R^\pm\zeta^\pm=0.
\]
All three Ozuch coefficients are essential.

Step 42’s statement that the same fixed-annulus construction can read “any order” is also unsupported by the cited material. Higher-order Ozuch obstructions involve resonances, nonlinear interactions, global infinitesimal Einstein deformations, and multi-bubble terms; they are not repetitions of a single \(l=2\) radial extraction.

A related lingering sentence in Step 42 says that excluding EH bubbling near a round orbifold makes the limit smooth. This only follows after ruling out every other ALE and singularity type. Invertibility of \(\mathbf R^\pm\) excludes EH desingularization at an \(A_1\) point, not arbitrary Ricci-flat ALE bubbling.

---

### 7. Value of the revised allocation

Moving attention from immediate high-order \(\Lambda>0\) theory to the chirality-sensitive first obstruction is scientifically coherent. The correction identifies the actual first local object for topology-forced plus-sign classes:
\[
\mathbf R^-=W^-+\frac{\Lambda}{3}I.
\]

Its current value is as a necessary-condition theorem and a model filter. It is not yet a general exclusion mechanism: \(S^2\times S^2\) already has \(\det\mathbf R^-=0\) everywhere, and finitely many singular points can lie on the zero set of \(\det\mathbf R^-\) without producing global Kähler structure. High-order theory becomes materially relevant once a concrete model survives the full vector equation \(\mathbf R^-\zeta^-=0\).

In summary, Step 43 repairs the principal orientation error correctly. The two most important textual refinements are:

\[
\boxed{\det\mathbf R^+=0\text{ provides allowed }\zeta^+\text{ directions; it does not validate every direction}}
\]

and

\[
\boxed{b_+>1\text{ forces plus-sign ALE intersection topology; “}k-1\text{ reversed EH pieces” requires the pure EH model}.}
\]
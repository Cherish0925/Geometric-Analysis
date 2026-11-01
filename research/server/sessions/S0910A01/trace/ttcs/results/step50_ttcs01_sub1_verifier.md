# TTCS Independent Branch Record

```json
{
  "step_id": 50,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step50_global_smoothing_evidence_campedelli_front.md",
    "Sessions/S0910A01/workspace/scripts/step50_z4x4_character_smoothing_test.py",
    "Sessions/S0910A01/workspace/scripts/step50_six_nodal_campedelli_arrangement.py",
    "Knowledge/objects/papers/Quotients-of-products-of-curves-new-surfaces-with-p-g-0-and-their-fundam--d97fcf2e6caa--2319c75d6a35/object.md",
    "Sessions/S0910A01/staging/acquired/Explicit_compactifications_of_moduli_spaces_of_Campedelli_and_Bu_0d21d1e6f25f9468/part_001.md",
    "Knowledge/objects/papers/Campedelli-surfaces-with-fundamental-group-of-order-8--e42c09a11a73--c366290f58cb/object.md",
    "Knowledge/objects/papers/A-construction-of-Horikawa-surface-via-Q-Gorenstein-smoothings--5632dd8463a4--eda8d10a9e6a/object.md",
    "Sessions/S0910A01/staging/acquired/Resolutions_and_deformations_of_cyclic_quotient_surface_singular_e928abc78f657ed1/part_001.md"
  ]
}
```

## Task

Verify the Step 50 Campedelli/product-quotient smoothing evidence for the Yau 26 project. Read the note and scripts plus the source files. Focus on two mathematical bridges: (1) for the BCGP K^2=2, G=Z_4^2 product-quotient row with six A1 singularities, does the character calculation plausibly compute H^0(Omega^1_S \otimes K_S) for the minimal resolution via quotient/reflexive-form/RDP comparison, or are there missing correction terms at the fixed points/resolution? (2) Does H^2(T_S)=0 for such an RDP canonical model really imply a global Q-Gorenstein smoothing that smooths all six A1 points and yields, via simultaneous resolution and Aubin-Yau, a negative Einstein metric on the smooth four-manifold? Also check the separate explicit six-nodal classical Z_2^3 line arrangement smoothing argument and identify any overstatement or missing source premise. Return a direct mathematical memo with corrections and next computations, not a procedural checklist.

## Output

## Mathematical verification memo: Step 50 Campedelli/product-quotient smoothing evidence

### 1. BCGP \(K^2=2,\;G=\mathbb Z_4^2\) row: character computation

The script uses the exact BCGP §6.7 spherical triples
\[
S_1=((1,3),(1,0),(2,1)),\qquad
S_2=((3,2),(0,1),(1,1))
\]
for \(G=\mathbb Z_4^2\). This is the right input; the shared signature \((4,4,4)\) alone is not enough.

Using Chevalley–Weil for abelian covers \(C_i\to\mathbb P^1\), the script obtains
\[
H^0(K_{C_1})=(2,3)\oplus(3,0)\oplus(3,1),
\]
\[
H^0(K_{C_2})=(0,3)\oplus(1,2)\oplus(3,3).
\]
The genus count is correct: each side has dimension \(3\), matching BCGP \(g_1=g_2=3\).

The resulting symmetric-square decompositions are also arithmetically correct:
\[
H^0(2K_{C_1})=(0,2)+(1,0)+(1,3)+(2,0)+(2,1)+(2,2),
\]
\[
H^0(2K_{C_2})=(0,1)+(0,2)+(1,1)+(2,0)+(2,2)+(3,2).
\]
No character in \(H^0(K_{C_2})\) is the inverse of a character in \(H^0(2K_{C_1})\), and no character in \(H^0(2K_{C_2})\) is the inverse of a character in \(H^0(K_{C_1})\). Hence
\[
\left(H^0(2K_{C_1})\otimes H^0(K_{C_2})\right)^G=0,
\]
\[
\left(H^0(K_{C_1})\otimes H^0(2K_{C_2})\right)^G=0.
\]

One correction to the script explanation: the fixed-point count for order-two elements only excludes a hyperelliptic involution lying inside the given \(\mathbb Z_4^2\)-action. To exclude hyperellipticity of \(C_i\) itself, one needs the additional standard fact that a hyperelliptic genus-three curve has central hyperelliptic involution \(\iota\), and the induced image of \(\mathbb Z_4^2\) in \(\operatorname{PGL}_2\) would be an abelian finite subgroup too large or of the wrong type. Finite abelian subgroups of \(\operatorname{PGL}_2\) are cyclic or \(\mathbb Z_2^2\); neither \(\mathbb Z_4^2\) nor \(\mathbb Z_4\times\mathbb Z_2\) can occur. Thus the curves are indeed non-hyperelliptic, and
\[
\operatorname{Sym}^2 H^0(K_C)\cong H^0(2K_C)
\]
is valid.

### 2. Quotient/resolution comparison for \(H^0(\Omega^1_S\otimes K_S)\)

Let
\[
Y=C_1\times C_2,\qquad X=Y/G,\qquad \pi:S\to X
\]
be the minimal resolution. BCGP Table 2 and §6.7 place this row among the product-quotient surfaces with \(K^2=2\); by BCGP Proposition 5.2 the singularities are exactly
\[
8-K^2=6
\]
ordinary double points \(A_1\).

For this row, the quotient map \(q:Y\to X\) is étale in codimension one; the non-free orbits are isolated and give only \(A_1\) points. Therefore on the smooth locus of \(X\),
\[
\Omega_X^1\otimes \omega_X
\]
pulls back to
\[
\Omega_Y^1\otimes \omega_Y.
\]
Both sides extend as reflexive sheaves across codimension two, so
\[
H^0\!\left(X,\Omega_X^{[1]}\otimes \omega_X\right)
\cong
H^0\!\left(Y,\Omega_Y^1\otimes\omega_Y\right)^G.
\]
For rational double points, holomorphic one-forms on the smooth locus extend across the resolution, and \(K_S=\pi^*K_X\). Hence
\[
H^0\!\left(S,\Omega_S^1\otimes K_S\right)
\cong
H^0\!\left(X,\Omega_X^{[1]}\otimes \omega_X\right).
\]
Thus the character computation plausibly gives
\[
H^0(S,\Omega_S^1\otimes K_S)=0.
\]

There is no apparent local correction term from the \(A_1\) points for this ordinary sheaf. The exceptional \((-2)\)-curves cannot create extra global sections of the locally free sheaf \(\Omega_S^1\otimes K_S\); a section supported only on exceptional curves would vanish on the dense open set and hence vanish everywhere. The finite quotient also has no branch divisor, so there is no codimension-one ramification contribution.

### 3. Relation to the deformation obstruction group

The deformation-theoretic group in the Lee–Park source is
\[
H^2(T_X^0),
\]
where \(T_X^0=\mathcal Ext^0(\Omega_X,\mathcal O_X)\) is the tangent sheaf of the singular surface \(X\). The supplied Lee–Park Proposition 2.4 states that if
\[
H^2(T_X^0)=0,
\]
then local deformations of the singularities globalize.

For this \(A_1\)-only situation, the passage from \(H^2(T_S)\) to \(H^2(T_X^0)\) is reasonable but should be written explicitly. For an \(A_1\) exceptional curve \(E\simeq\mathbb P^1\),
\[
N_{E/S}\cong \mathcal O_E(-2).
\]
The quotient
\[
T_S \longrightarrow N_{E/S}
\]
has no local sections over the exceptional curve because \(H^0(\mathbb P^1,\mathcal O(-2))=0\). Thus vector fields on the resolution descend in the same way as logarithmic vector fields, and locally
\[
\pi_*T_S \cong T_X^0.
\]
Since \(R^1\pi_*T_S\) is supported at finitely many points, Leray gives
\[
H^2(S,T_S)\cong H^2(X,\pi_*T_S)\cong H^2(X,T_X^0).
\]
Therefore the character vanishing
\[
H^0(S,\Omega_S^1\otimes K_S)=0
\]
is Serre-dual to
\[
H^2(S,T_S)=0,
\]
and in this RDP case it gives the Lee–Park obstruction group vanishing
\[
H^2(T_X^0)=0.
\]

This tangent-sheaf bridge is the main missing written argument in Step 50. It is valid for \(A_1\) rational double points; for non-Du Val quotient singularities one would need the logarithmic tangent sheaf used in Lee–Park.

### 4. From \(H^2(T_X^0)=0\) to smoothing all six nodes

For an \(A_1\) point, the local deformation base is one-dimensional:
\[
xy-z^2=t.
\]
Since rational double points are Gorenstein, local deformations are already \(\mathbb Q\)-Gorenstein. With six \(A_1\) points,
\[
H^0(T_X^1)\cong \mathbb C^6.
\]
Lee–Park Proposition 2.4 gives that the global deformation space maps smoothly onto the product of the six local deformation bases when \(H^2(T_X^0)=0\). Hence one may choose a one-parameter deformation whose six local parameters are all nonzero for \(t\neq0\). The nearby fibers are then smooth.

The product-quotient canonical model \(X=(C_1\times C_2)/G\) has ample \(K_X\): \(K_{C_1\times C_2}\) is ample and the quotient is finite. Ampleness of the relative canonical class persists after shrinking the deformation base. Therefore smooth nearby fibers have ample canonical class. Aubin–Yau then gives a Kähler–Einstein metric with Einstein constant \(\lambda<0\) on each smooth nearby fiber.

Finally, for \(A_1\) singularities, simultaneous resolution exists after a finite base change. The resolved total space is a smooth proper family whose central fiber is the minimal resolution \(S\) and whose nearby fibers are the smooth deformed surfaces. Ehresmann’s theorem then identifies \(S\) diffeomorphically with the smooth nearby fibers. Thus, once the \(H^2(T_X^0)=0\) bridge is written, the BCGP \(\mathbb Z_4^2\) row yields an Einstein metric with \(\lambda<0\) on the smooth four-manifold underlying its minimal resolution.

### 5. Classical \(\mathbb Z_2^3\) six-nodal line arrangement

The separate line-arrangement script is mathematically coherent. The arrangement
\[
x=0,\ y=0,\ z=0,\ x-y=0,\ y-z=0,\ x-z=0,\ x-y+z=0
\]
has, by exact integer projective arithmetic,

\[
\#\{\text{intersection points}\}=9,\qquad
\text{multiplicity census } \{2:3,\;3:6\},
\]
and no point of multiplicity \(\ge4\). The six triple points are correctly listed.

The script then searches all bijective labelings by the seven nonzero elements of \(\mathbb F_2^3\) and finds labelings for which every triple-point label set is a basis. Under Alexeev–Pardini Definition 3.1 and Lemma 3.4, a triple concurrence with labels generating \(\mathbb Z_2^3\) gives one \(A_1\) point; a dependent triple would give \(\frac14(1,1)\) points instead. Since every triple in the displayed labeling is independent, the associated canonical Campedelli cover has exactly six \(A_1\) singularities. Double intersections of two distinct branch lines do not create singularities of the cover.

Moving the seven lines to general position gives a family of \(\mathbb Z_2^3\)-covers with smooth nearby fibers. Alexeev–Pardini state
\[
K_X=\pi^*(h/2),\qquad K_X^2=2,
\]
so the canonical class is ample on the canonical models. The same simultaneous-resolution/Ehresmann argument identifies the minimal resolution of the six-nodal central surface with the smooth nearby Campedelli fibers. Aubin–Yau then supplies Kähler–Einstein metrics with \(\lambda<0\) on that four-manifold.

The only scientific separation that should remain explicit is that this classical \(\mathbb Z_2^3\)-cover example is not identified with the BCGP \(\mathbb Z_4^2\) product-quotient row. It proves the smoothing mechanism exists inside the classical Campedelli component; it does not by itself place the BCGP product-quotient surface in that component.

### 6. Useful additional computations

Two short computations would make the BCGP part self-contained:

1. A direct equivariant computation of \(H^0(2K_{C_i})\), independent of the non-hyperelliptic shortcut, to confirm the same six characters for each curve.

2. A written local \(A_1\) tangent-sheaf comparison:
\[
\pi_*T_S=T_X^0,\qquad
H^2(S,T_S)=H^2(X,T_X^0),
\]
using \(N_{E/S}=\mathcal O_E(-2)\) and Leray. This is the precise deformation-theoretic bridge from the character computation to Lee–Park Proposition 2.4.
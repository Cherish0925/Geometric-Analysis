# Exact charged cores cannot be left unchanged in a closed Einstein metric

## 1. Question and result

The complete metrics G[z] in [the exact construction](round3_construction.md)
solve Ric(G)=-G on (R x S1)^2. The nonzero twist transfer in
[the nonlinear charge theorem](round4_construction.md) is a genuine invariant
of this Einstein solution, not just a defect of an approximate ansatz.

This raises a specific global question: can one insert an unchanged open
piece of this exact solution into a closed Einstein manifold and repair only
the exterior? The answer is **no when (b1,B1) is nonzero**. This statement
does not restrict the symmetry or topology of the proposed closed manifold.

**Theorem.** For sufficiently small parameters z of the round-three family,
suppose (b1,B1) is nonzero. Then:

1. the universal cover of ((R x S1)^2,G[z]) admits no cocompact group of
   isometries;
2. no nonempty open subset of this metric is locally isometric to an open
   subset of any connected closed Einstein four-manifold.

The second assertion concerns exact local agreement. It does not rule out
closed Einstein metrics converging to this model, or a global construction
which changes the metric on every open part of the core. In particular it
does not prove that the surface-bundle smooth manifolds have no Einstein
metrics.

## 2. A cocompactness lemma

**Lemma.** Let (X,g) be a connected real-analytic Riemannian manifold.
Suppose, for one fixed radius r>0, there are points p_j satisfying

    sup_(B_r(p_j)) |nabla Rm| -> 0.                         (2.1)

If a group of isometries acts cocompactly on X, then nabla Rm is identically
zero.

**Proof.** Choose a compact set K whose translates cover X. Translate p_j
to q_j in K and take a convergent subsequence q_j -> q. Isometry invariance
preserves (2.1). For all sufficiently large j,

    B_(r/2)(q) subset B_r(q_j).

Consequently nabla Rm vanishes on the fixed open ball B_(r/2)(q). Its
components are analytic, so they vanish throughout connected X. No lower
bound on injectivity radius is used. The radius in (2.1) must be fixed; small
curvature derivatives at isolated points or on shrinking balls do not
suffice. QED.

More generally the same argument applies to any analytic natural tensor
which has uniformly vanishing norm on fixed-radius balls. This observation
is an application of analyticity and cocompactness, not a new general
analytic-continuation theorem.

## 3. The exact family satisfies the local hypothesis

Lift G[z] to X=R^4. Its uniform equivalence to

    g0=dt^2+cosh(t)^2 dy^2+du^2+cosh(u)^2 dx^2

implies completeness. Fix t0 and let p_j=(t0,0,u_j,0), u_j -> +infinity.
For a fixed G-radius r, the t and u coordinates on B_r(p_j) differ from
t0 and u_j by bounded amounts: both coordinate differentials have uniformly
bounded G-norm. The angular directions cause no change to coefficient
estimates because all metrics under discussion are torus-invariant.

The round-three face estimate, with derivatives through order three, is

    G[z] -> h_(a+,b+)(t,y)+du^2+cosh(u)^2 dx^2              (3.1)

uniformly on these balls in background-frame C3. The rate is bounded by a
constant times

    |z|[sech(t)^2 exp(-u)+exp(-2u)]
       +|z|^2[cosh(t)cosh(u)]^(-3/4).

Each face metric in (3.1) is locally H2(-1) x H2(-1), hence has parallel
curvature. Uniform metric equivalence and the C3 estimate imply (2.1).
One shrinks the parameter neighborhood once to obtain these finitely many
derivative estimates; no uniform bound over all derivative orders is
needed.

If X had a cocompact isometry group, the lemma would imply nabla Rm=0.
Moreover the curvature tensor along the escaping balls converges to that
of H2(-1) x H2(-1). A parallel curvature tensor has constant algebraic
isometry type, so its type must be this product type. Completeness and
simple connectedness then identify X globally with H2(-1) x H2(-1), by
the standard determination of a simply connected locally symmetric space
by its curvature tensor.

## 4. Nonzero conserved charge excludes that product

Write the torus-invariant metric in its mechanical-connection form

    G=h_ab dx^a dx^b
        +H_ij(dtheta^i+A^i)(dtheta^j+A^j),
    v=sqrt(det H), F=dA, q=v H *_h F.

Here the ordered angular generators are (partial_y,partial_x), and the
base orientation is dt wedge du. The mixed Einstein equation makes q
constant. The nonlinear charge theorem proves

    S=integral_(R2) F=(pi^2/2)(-b1,B1),
    S=M[z]q,
    M[z]=integral_(R2) v^(-1)H^(-1) dA_h,                 (4.1)

where M[z] is finite and positive definite. Thus q is nonzero precisely
when (b1,B1) is nonzero.

Every locally free two-dimensional abelian Killing action on
H2 x H2 has integrable orthogonal complement. Here is the required
Lie-algebra argument, including actions which mix the two factors.
The identity-component isometry algebra is sl2(R) direct-sum sl2(R).
An abelian subalgebra of either sl2 factor has dimension at most one:
the centralizer of every nonzero traceless 2 x 2 matrix, within sl2, is
its one-dimensional span. Hence a two-dimensional abelian subalgebra of
the direct sum projects onto a one-dimensional subalgebra in each factor,
and is their entire two-dimensional direct sum. On the regular set its
orbits are products of two one-dimensional orbits. The orthogonal
distribution is the product of the two one-dimensional orthogonal line
fields and is integrable. A constant change of the two Killing generators
does not change this conclusion.

The lifted original angular action is everywhere locally free. Its
mechanical connection therefore has F=0 if X is this product. That would
give q=0, contradicting (4.1). This proves assertion 1. Notice that no
hypothetical cocompact group was assumed to preserve the original torus
action.

## 5. From compact quotients to an obstruction to exact local agreement

Suppose a nonempty open part of G[z] were locally isometric to a closed
Einstein manifold (N,h). Its Einstein constant is necessarily -1 because
of the local agreement. Both universal covers are complete, connected,
simply connected and real analytic. Einstein analyticity is
DeTurck--Kazdan, Theorem 5.2 [DK].

The classical extension theorem for local isometries between complete,
simply connected analytic Riemannian manifolds extends this local isometry
to a global isometry of their universal covers. Anderson recalls precisely
this version in the paragraph introducing the proof of Lemma 2.6 [A].
The compact quotient N would therefore give a cocompact deck-group action
on X, contrary to assertion 1. This proves assertion 2.

## 6. Consequence for the research program

There are now two different global matching requirements.

- The charge relation (4.1) is nonlinear and constrains the incoming and
  outgoing twist data of the exact noncompact model.
- Even if boundary data are matched, an exact closed construction cannot
  leave a nonzero-charge core unchanged on any open subset. A genuine
  closed solution must include a correction within the core, or use a
  different local model.

The result does not prohibit using G[z] as a leading approximation in
gluing. It also supplies no uniform lower bound for corrections when the
closed topology, diameter or gluing scale changes: the cocompactness
argument concerns one fixed metric. This is the precise distinction
between an exact insertion obstruction and a global no-Einstein theorem.

## References

[DK] D. DeTurck and J. Kazdan, Some regularity theorems in Riemannian
geometry, Ann. Sci. Ecole Norm. Sup. (4) 14 (1981), 249--260, Theorem 5.2.
https://www.numdam.org/article/ASENS_1981_4_14_3_249_0.pdf

[A] M. T. Anderson, On boundary value problems for Einstein metrics,
paragraph at the start of the proof of Lemma 2.6 (PDF p. 10), recalling
Kobayashi--Nomizu, Foundations of Differential Geometry I, Corollary 6.4.
https://www.math.stonybrook.edu/~anderson/dirichlet.pdf

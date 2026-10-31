# Q2 continuation: a uniform covering theorem and an exact limit on the current scalar-budget method

Read against `01_Research_Synthesis.tex`, Sections 3 and 6–7, and companion A01.52, A02.59 Part D, A02.62–64. This note does not claim a matching unrestricted infimum or an Einstein nonexistence theorem. It adds one construction transfer with a uniform quantifier, and proves precisely that the existing numerical endpoint estimates cannot by themselves decide the small-blowup lower bound.

## 1. A uniform strict upper bound over arbitrary covers of a general-type base

**Proposition.** Let X0 be a fixed minimal complex surface of general type. Assume the general Kähler–Einstein Burns insertion theorem proved in A01.52/A02.59D, including the canonical-model ADE resolution recovery described there. Let Xj -> X0 be arbitrary finite unramified covers of degrees dj -> infinity, and let integers kj satisfy 1 <= kj = o(dj). There is a constant delta_X0 > 0 such that, for all sufficiently large j, the smooth manifold

    Mj = Xj # kj CPbar^2

has an actual smooth metric gj with

    P(gj) <= 8 pi^2 (1-delta_X0) kj.

The covers need not form a tower and need not be regular. No uniform geometry hypothesis on arbitrary competing metrics is introduced.

**Proof.** On the canonical model of X0 choose one fixed contractible ball B in its regular locus, with a slightly larger fixed collar. All local data on this collar are those of one fixed negative KE metric g0, whose scalar curvature s is nonzero. Choose an insertion direction in the kernel of R+ perpendicular to the Kähler form. The supplied insertion theorem gives, for one fixed small parameter epsilon,

    I(epsilon) := P(after insertion)-P(before insertion)
       = 8 pi^2 - (pi^2 s^2/8) epsilon^2 log(1/epsilon)
         + O_B(epsilon^2).

Choose epsilon once, so that I(epsilon) = 8 pi^2 - sigma for some sigma > 0. Every lift of B has exactly the same background germ, collar and insertion error. Because B is contractible and evenly covered, Xj has dj disjoint lifts; eventually kj <= dj. Insert the same metric in kj of them. The local differences add exactly, since supports are disjoint.

If K_X0 is ample, the lifted background is Einstein and P=0; the result follows immediately. If the canonical model has ADE points, use the source's smooth resolution metrics g_lambda on X0, equal to g0 on the chosen insertion collar and satisfying P(g_lambda) -> 0. Their lifts have total P = dj P(g_lambda). The insertion difference I(epsilon) is independent of lambda, not merely bounded uniformly in lambda. Having fixed epsilon, choose lambda_j so that

    dj P(g_lambda_j) <= (sigma/2) kj.

Then P(gj) <= (8 pi^2-sigma/2) kj. Take delta_X0 = sigma/(16 pi^2). This also works in the ample case. QED.

The same proof allows kj/dj bounded by any prescribed finite L: choose an integer m >= L and m disjoint regular-locus balls on X0 first. The resulting delta may depend on X0 and L. The o(dj) version needs only one base ball and makes delta independent of the particular cover sequence and kj.

**Einstein-defect consequence.** Put Aj=dj c1^2(X0), hj=kj/Aj. Under the inherited actual sign-class supply on Mj, every conformal class is negative Yamabe. Replace gj by its negative constant-scalar representative ghat_j. Then

    P(ghat_j) <= P(gj),
    S(ghat_j) >= 32 pi^2 Aj,
    E(ghat_j) = J(ghat_j) = 4 P(ghat_j)/R(ghat_j).

Consequently

    alpha(Mj) <= 4 (1-delta_X0) hj,
    limsup alpha(Mj)/hj <= 4 (1-delta_X0) < 4.

This proof uses no balanced-family asymptotic equivalence. It extends the earlier complex-hyperbolic cover transfer to any fixed general-type base for which the stated recovery and actual supply hold. It does not identify the optimal coefficient, prove a lower bound of order kj, or rule out a smaller scale kj^2/Aj.

## 2. A formal zero-defect family survives the entire finite-parameter endpoint envelope

This section concerns finite-dimensional curvature and cohomology data, not constructed metrics or solutions of the field equations. Its purpose is to identify exactly what cannot be concluded by combining the present scalar budgets.

Use A>0, k>0, h=k/A, 0<h<=1/24. Take the topological numbers of a blowup of a ball-quotient-type base:

    chi = A/3+k,   tau=A/9-k,
    T+=A-k,       T-=A/3+5k.

Assign formal data

    P=0,
    S=32 pi^2(A+5k),
    W+= (4 pi^2/3)(A-4k),
    W-= (20 pi^2/3)k,
    V=2 pi^2(A+5k),   s=-4,
    a^2=T+=A-k,       p=(a+)^2=A.

They satisfy both Chern–Weil identities exactly, both Weyl energies are nonnegative, and S=16V. The sign-family period data are algebraically realizable in the intersection space: take the minimal canonical class in H+ and the exceptional classes in H-, so every sign class has the same projection square A and total square A-k. This is a statement about an abstract positive subspace, not about realization by a metric satisfying the assigned curvature values.

The Weyl-channel coordinates are

    kappa=2k,   upsilon=5k,   Pi_projection=0.

The classical mixed inequality is satisfied. Equivalently, its complete quadratic-envelope family

    D_beta = (1+1/beta) S + 6(beta+1) W+ -72 pi^2 p

has the exact value

    D_beta/(beta V)
      = [4(1-4h)(beta-2)^2 +144h] / [(1+5h) beta^2].       (2.1)

In particular, for every beta>=2,

    D_beta/(beta V)
      >= [4(1-4h)/(1+5h)] (beta-2)^2/beta^2.              (2.2)

Thus the data satisfy a finite-parameter separation whose coefficient tends to 4 as h -> 0. The KE calibration itself has coefficient exactly 4, so any fixed inherited separation constant strictly below 4 is compatible with these zero-P data for sufficiently small h.

There is a stronger observation relevant to FD2. For all beta>=2 and h<=1/24,

    D_beta/V >= 8 (beta-2)^2/beta^2.                      (2.3)

To verify it, put x=beta-2. Multiplying the difference between the two sides by the positive factor (1+5h) beta^2/4 gives

    (1-4h)x^3 -18h x^2 +36h x +72h.

Since 2x^2 <= x^3+x for x>=0, this is at least

    (1-13h)x^3 +27h x +72h >= 0.

A compact negative KE ball quotient with k=0 is an admissible calibration for any Euler-density bound B>=1/3. It has

    D_beta/V =4(beta-2)^2/beta,

so any universally valid FD inequality of the displayed form must have c(B)<=8, by beta down to 2. Therefore (2.3) means that **even the best possible constant in that scalar FD statement cannot exclude this formal small-blowup zero-P family.** Here chi/A=1/3+h is itself uniformly bounded.

This is not in conflict with the finite-density theorem: the data never approach its forbidden D_beta/V -> 0 endpoint as beta -> infinity. It shows that strengthening finite-density constants or applying more values of beta does not automatically solve the pure-blowup lower-bound problem.

The I41 numerical consequence with Y=(T-a^2)+=0 also allows the same family at the nonsharp constants used in the manuscript:

    Sigma=S-32 pi^2 p =160 pi^2 k,
    D2=144 pi^2 k,
    Sigma/(P+D2)=10/9.

Hence Sigma<=C(P+D2) is satisfied for C>=10/9. N1 likewise permits it whenever its constant epsilon0 is at most 1/3-h, because J=0 and (T/A-2/3)+=1/3-h. The actual stated small N1 constant satisfies this for small h.

**Conclusion of the calculation.** A positive unrestricted P lower bound in the small-blowup range cannot be deduced solely from Chern–Weil, Hodge sign-class budgets, classical scalar/mixed bounds, the displayed all-beta scalar separation, FD2's scalar conclusion, and I41 at its currently available coarse constant. A proof must use additional differential information, an effective sharp form not implied by these numerical inequalities, or a global realization obstruction. These formal data are not a counterexample to such a proof or to Q1/Q2 themselves.

## 3. What a sharply stronger I41 constant would actually imply

This is a conditional algebraic observation, not a claim that the constant is attainable.

Write p=P/(8 pi^2), upsilon=S/(32 pi^2)-A, and Pi=(a+)^2-A>=0. At the negative Yamabe representative the exact identities give

    D2=36 pi^2(upsilon-k+p-2Pi),
    Sigma=32 pi^2(upsilon-Pi).

Thus the inequality Sigma<=C(P+D2) is equivalent to

    11C p >=9C k +(8-9C)upsilon +(18C-8)Pi.              (3.1)

If one could prove it throughout this class with 4/9<=C<=8/9, then all coefficients on the right after 9Ck would be nonnegative, giving

    P >= (72 pi^2/11) k.

This would in particular exclude all Einstein metrics on these nonminimal surfaces. It is substantially stronger than the established nonsharp estimate. Formula (3.1) makes precise why merely knowing that some finite C exists does not answer the small-blowup problem. Improving C to this range is itself a new global theorem, not routine optimization of the printed proof.

## 4. Independent check of the Q4 finite-density torsion corollary

For the parent team's separate Q4 note, the constants follow directly from the companion's AK identity. Normalize Ric=-g and set

    u=|nabla omega|^2/4,  x=avg u, z=avg u^2,
    e=avg|rho_*''|^2,    w=avg|W3+|^2.

Then 3z+e+2w=2x, hence x<=2/3. Put delta=2/3-x. The stated convention |W2+|^2=|rho_*''|^2 gives

    avg|W+|^2=2/3-2x+(3/2)z+e+w=delta+e/2.

Jensen yields e<=2x-3x^2=3x delta<=2delta, so avg|W+|^2<=2delta. The canonical curvature paired with omega gives

    (c1+)^2/V >=(2-x)^2/(8 pi^2).

For an actually supplied canonical monopole class, take A=p=(c1+)^2. Since a^2=T and p>=T>0, the condition chi/T<=B implies chi/A<=B. Consequently

    D_beta/V <=16/beta+12beta delta-12delta-9delta^2
              <=16/beta+12beta delta.

For delta<=1/12 choose beta=2/sqrt(3delta)>=4. FD then gives

    c(B)/4 <=16 sqrt(3delta),
    delta >=c(B)^2/12288.

Combining with delta>1/12 gives delta>=min(1/12,c(B)^2/12288). Actual canonical SW supply should be stated explicitly; in b+=1 the chamber cannot be omitted. This proves separation from maximal average torsion, not integrability u=0.

## 5. Source and status

Primary classical comparison checked: Claude LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, arXiv:math/0003068, Theorem 2.3 and the Chern–Weil identity. https://arxiv.org/pdf/math/0003068 . The classical full Ricci infimum is not used as an infimum-subtraction argument anywhere above.

The general KE insertion expansion is inherited from the supplied new manuscript, not reproved in this note. The uniform covering transfer and the complete formal parameter-envelope calculation are the additional arguments supplied here. The unrestricted value p*(X#k CPbar^2) in the small-blowup range, and a matching lower bound for the new cover construction, remain undecided.

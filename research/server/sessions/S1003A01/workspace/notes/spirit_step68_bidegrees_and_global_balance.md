# Spirit follow-up to Step 68: bidegrees of the newest-jet map and the remaining global information

This note supplies a small algebraic explanation for Core to check against the full metric-jet map. It is not a new formal-existence theorem. The exact polynomial calculation is in `scripts/spirit_step68_top_channel_polarization.py`, with output `data/spirit_step68/top_channel_polarization.json`.

## 1. The claimed Kähler rank jump is roundoff, not evidence of a full map

In `data/step68b/kernel_absorption_cases.json`, the four Kähler cases have largest singular values

- 2.61e-12 and 9.85e-12 for lambda=-1, d=6,8;
- 2.07e-12 and 7.39e-12 for lambda=0, d=6,8.

All their singular values are at the cancellation scale. In contrast the nonzero torsion examples have largest singular values of order 30--1200 and separated null singular values near 1e-12. `step68_kernel_absorption.py` counts `s > 1e-9*s[0]` even when the whole matrix is numerical zero. Its resulting Kähler ranks 35 and 84, and its radial-image ratios divided by the norm of this numerical-zero matrix, have no geometric significance. Withdraw the full-rank Kähler conclusion. A truly exact Kähler control is the natural way to fix its value. The polarization below predicts zero, consistent with the absolute sizes already saved.

## 2. Polarization gives a candidate all-degree explanation of ranks 20 and 28

At a torsion zero write the first torsion polynomial as

    f1 = c z + B w,   w=bar(z),   B=S+A.

A change in H_d belonging to ker L_{d-2} first changes torsion in degree d-1. Its principal half-twistor form is

    v = z h(w) + g(w),

where n=d-2, h is homogeneous of degree n, and the vector g has degree n+1. Consider the principal scalar expression in the Step-65 identity,

    R(f,h) = -tr(bar(B_f) B_f) - 8|h|^2
             - 6 Re sum_i bar(f_i) partial_{w_i}h,
    B_f = z tensor Dh + Dg.

Here conjugation is entrywise, not adjoint. Linearizing this expression at f1 gives

    D R(f1)[v]
      = -2 Re[ tr(bar(B) Dg)
               + (3n+8) bar(c) h
               + 4 (Dh)^T bar(B) z ].                       (1)

Indeed the mixed trace contributes -2 Re[(Dh)^T bar(B)z], the derivative source contributes -6 times this, and Euler's identity w dot Dh = n h supplies the coefficient 3n+8.

The script constructs this polynomial over Q(i), using independent variables z,w and the involution z <-> w. At the rational strict-cone jet from A02,

    c=1, S=[[2,1],[1,1+i]], A=[[0,2+2i],[-2-2i,0]],

the exact real coefficient ranks are

| metric jet degree d | scalar degree n | rank of (1) | radial moment |
| --- | --- | --- | --- |
| 4 | 2 | 10 | not identically zero |
| 6 | 4 | 20 | zero |
| 8 | 6 | 28 | zero |
| 10 | 8 | 36 | zero |

These reproduce the meaningful Step-68 ranks and predict the next one without a large metric-jet system. At c=0, B=[[0,1],[0,0]] (the rank-one GH first-jet type), the ranks are 9,18,26,34. At c=B=0 they are identically zero.

### Bidegrees explain the radial cancellation

The pure terms in (1) have types (0,n) and (n,0). The mixed terms have types (1,n-1) and (n-1,1). For even n>=4 none has balanced type (n/2,n/2). The radial moment Delta^(n/2), which only sees that balanced type, therefore vanishes identically. At n=2, the mixed term is balanced and can have a trace. The phenomenon is a restriction on complex types, not a new sign obstruction at each order.

For invertible B and n>=3 the generic rank is exactly 4(n+1):

- g -> tr(bar(B)Dg) is onto the homogeneous scalar polynomials of degree n. One nonzero constant directional derivative already suffices. This supplies 2(n+1) real dimensions in the pure types.
- h -> (Dh)^T bar(B)z is injective when B is invertible. Its type differs from its conjugate for n>=3. This supplies another 2(n+1) real dimensions.
- The pure and mixed types are independent. The c h term adds no new range beyond the pure terms already supplied by g.

On the established cone every nondegenerate first jet has det B != 0, so invertibility is the relevant generic case. The rank-one case loses one complex direction of h, explaining 4n+2 there.

### What remains to identify geometrically

Equation (1) is an exact polarization of the displayed torsion polynomial expression. To promote it to an all-degree theorem for the Step-68 metric channel M_d, verify both:

1. the principal torsion map from ker L_{d-2} has the stated half-twistor image (and sufficient surjectivity for equality of ranks);
2. its full metric-channel scalar compatibility equals (1), up to the fixed nonzero normalization and Bianchi terms, with no additional lower-curvature source surviving at degree d-2.

Order counting makes this plausible: varying H_d changes q first in degree d, so the s q and q^2 terms are too high to affect degree d-2; the relevant terms are the coupling of f1 with the new degree-(d-1) torsion. This is a proposed structural derivation to complete, not a claim that a match of ranks alone proves it.

## 3. Implication for an induction

There is one U(2)-invariant functional, but not only one compatibility coefficient. At E8 the scalar polynomial has 84 real coefficients, while this newest-jet channel has rank 28. The radial row is only one of 56 missing directions. At E10 the candidate predicts rank 36 in a 165-dimensional scalar space. An induction must explain how lower freedoms solve the whole complementary representation, not just its invariant radial component.

The successful E8 tangent calculation addresses all 84 rows, which is genuinely useful. The next conceptual target is a regular projection/extension mechanism for the full solution tower, rather than repeated surjectivity of one moment. Moving earlier coefficients at every cutoff does not by itself produce a compatible inverse-limit jet or a convergent analytic germ.

Also distinguish the exact identity P composed with delta Ric = 0, valid in every degree, from completeness of the polynomial compatibility module. Step 68 verifies the latter through d=8. Pointwise rank five of the real symbol identifies a generic annihilator over fractions; it does not alone prove that Bianchi and P generate every polynomial syzygy in all degrees or that the nonlinear system is formally integrable. A homogeneous-module resolution or an all-degree dimension/exactness argument is the appropriate bridge. This is useful mathematics, not a reason to rerun the finite tables.

## 4. The proposed global mean bound is already contained in the AAD balance

Use form conventions from the existing closed Einstein-AK arguments, with q=|nabla Omega|^2, V=W3+, s<0, and put

    a = |s|/sqrt(24),
    T_AK = integral ( |W3+|^2 + 3 q^2/32 ).

The established norm decomposition and AAD integral balance imply exactly

    integral |W+|^2 = a^2 Vol - T_AK.                        (2)

Consequently mean |W+| <= a already follows by Cauchy--Schwarz, without using a new monopole estimate. Strict excess at isolated zeros does not contradict (2): points have zero measure and neither their positive index nor the determinant sign imposes a uniform neighborhood size.

There may still be useful additional information in the full LeBrun inequality, where actual canonical-class supply is established. Assuming

    integral (s-sqrt(6)|W+|)^2 >= 72 pi^2 (c1(J)^+)^2,

and writing h_minus = ||c1(J)^-||_Hodge^2, Einstein Chern--Weil gives

    4 pi^2 c1(J)^2 = integral (s^2/24 + 2|W+|^2).

Subtracting yields

    a^2 Vol + 4a integral |W+| - 5 integral |W+|^2
        >= 12 pi^2 h_minus.

Using (2), this is equivalently

    2 integral (|W+|-a)^2 + 12 pi^2 h_minus <= 3 T_AK.        (3)

Thus (3), not the weaker mean bound alone, isolates the extra potential input: Weyl-norm fluctuation and the harmonic ASD canonical class must fit inside the existing torsion/transverse-Weyl budget. The chamber and actual-supply hypotheses remain essential. No contradiction, optimal estimate, or localization theorem is asserted here.

The global challenge is to connect such an integrated budget to an actual zero neighborhood, a transported field, or compact geometry with controlled scale. The local cone and index alone do not provide that connection. This keeps the global route substantive while the local compatibility theory is strengthened.

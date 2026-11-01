---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: An introduction to the Seiberg-Witten equations on symplectic manifolds]

For this purpose, we must digress momentarily to consider deformations
of a pseudoholomorphic curve C. An infinitesimal deformation of C is given
by a section of the normal bundle N → C. (We can restrict attention to
the normal bundle, instead of considering the pullback of TX, because we
are interested only in the image of the curve in X.) The normal bundle is
∞
naturally a holomorphic line bundle on C. A deformation s ∈ C (N) is the
derivative of a 1-parameter family of pseudoholomorphic curves iff

N\to C

s\in C^{\infty}(N)

D s={\overline{{\partial}}}s+\nu s+\mu{\overline{{s}}}\in C^{\infty}\big(N\otimes T^{0,1}C\big)

∞ 0,1 ∞ 0,1 ⊗2
vanishes. Here ν ∈ C (T C) and µ ∈ C (T C ⊗N) are certain sections
determined by the 1-jet of the almost complex structure J near C. (If J is
integrable, then µ vanishes.)
We say that a curve C ⊂ X together with a set Ω ⊂ C of d points is

\nu\in C^{\infty}(T^{0,1}C)

\mu\in C^{\infty}(T^{0,1}C{\otimes}N^{\otimes2})

We say that a curve C ⊂ X together with a set ΩC⊂ C of d points is
nondegenerate if the operator

C\subset X

\Omega_{C}\subset C

D\oplus\operatorname{e v}:C^{\infty}(N)\to C^{\infty}(N\otimes T^{0,1}C)\oplus\oplus_{p\in\Omega_{C}}N_{p}

has no cokernel. By the dimension formula, this means that the operator has
no kernel either.
In this case we want to define r(C, 1) to be ±1, depending on “the sign

In this case we want to define r(C, 1) to be ±1, depending on “the sign
of the determinant of D ⊕ ev”. What is the sign of the determinant of an
infinite dimensional matrix? We are considering operators whose kernel and
cokernel are finite dimensional, and have the same dimension. We require
this sign to have the following properties:

r(C,1)

D\oplus{\mathrm{e v}}^{?}

\pm1

\{O(t)\}_{t\in[0,1]} properties hold: first, Ker(O(t)) = {0} for all but a finite set, Λ, of ∣t. Second, it t ∈ Λ, then dim Ker(O(t)) = 1. Third, if t ∈ Λ, then dO dt ∣ t maps the kernel of O(t) to the cokernel of O(t).)

These two criteria turn out to be consistent, and they unambiguously deter- mine a sign for the determinant of D. Thus, to find r(C, 1), we deform D to an invertible C-linear operator (e.g. by deforming the µ term to zero), count the number of points along the deformation where the kernel is not trivial, and take (−1) to this power. Now suppose C is a torus with trivial normal bundle. We say that C is strongly nodegenerate if, for every holomorphic covering f : C ′ → C by a torus C ′ , the operator f ∗ D on C ∞ (f ∗

N) defined by
(f ∗

D)s = ∂s + (f
∗ ν)s + (f ∗ µ)s

is surjective. In this case r(C,m) is defined as follows. There are 4 flat real line bundles {Lι} on C, classified by ι ∈ H1(C; Z/2). We can twist the operator D by Lι to get an operator Dιon C ∞ (N ⊗ Lι). The number r(C,m) depends on:

- The sign of the determinant D0, which we signify as + or −.
- The number k ∈ {0, 1, 2, 3} of nonzero ι such that the sign of the determinant of Dιis −1.
Let’s write r±,k(C,m) for the corresponding value of r(C,m). To define r±,k(C,m), it is convenient to use the generating function

∑ ∞ f±,k= 1 + r±,k(C,m)t m . n=1 Then we define 1 f+,0=, 1 − t f+,1= 1 + t, 1 + t f+,2= 2 , 1 + t (1 + t)(1 − t2) f+,3= 2 , 1 + t 1 f−,k=. f+,k

---

Note that r(C,m) is not always ±1. This completes the definition of Gr. Another derivation of this invariant has been given by Ionel and Parker [7].

# References

[1] M. F. Atiyah, R. Bott, and A. Shapiro, Clifford modules, Topology 3 (1964) suppl. 13–38. [2] N. Berline, E. Getzler, and M. Vergne, Heat kernels and Dirac operators, Grundlehren der Mathematischen Wissenschaften 298, Springer-Verlag,

192.
[3] P. A. M. Dirac, Principles of quantum mechanics, Oxford Univ. Press. [4] S. K. Donaldson, Polynomial invariants for smooth four-manifolds, Topology 29 (1990), no. 3, 257–315. [5] S. K. Donaldson and P. B. Kronheimer, The geometry of four-manifolds, Oxford Univ. Press, 1990. [6] M. Gromov, Pseudoholomorphic curves in almost complex manifolds, Invent. Math. 82 (1985), 307–347. [7] E. Ionel and T. Parker, The Gromov invariants of Ruan-Tian and Taubes, Math. Res. Lett. 4 (1997), no. 4, 521–532. [8] D. Kotschick, P. B. Kronheimer, and T. S. Mrowka, in preparation. [9] P. B. Kronheimer and T. S. Mrowka, The genus of embedded surfaces in the projective plane, Math. Res. Letters 1 (1994), 797–808. [10] S. Kobayashi and K. Nomizu, Foundations of differential geometry, John Wiley and Sons, 1963 (vol. I), 1969 (vol. II). [11] H. B. Lawson Jr. and M–L. Michelson, Spin geometry, Princeton Math- ematical Series 38, Princeton Univ. Press, 1989. [12] D. McDuff and D. Salamon, Introduction to symplectic topology, Oxford Univ. Press, 1995.

---

[13] J. Morgan, The Seiberg-Witten equations and applications to the topol- ogy of smooth four-manifolds, Mathematical Notes 44, Princeton Univ. Press, 1996.

[14] C. H. Taubes, The Seiberg-Witten invariants and symplectic forms, Math. Res. Lett. 1 (1994), 809–822.

[15] C. H. Taubes, More constraints on symplectic forms from the Seiberg- Witten invariants, Math. Res. Letters 2 (1995), 9–13.

[16] C. H. Taubes, The Seiberg-Witten and the Gromov invariants, Math. Res. Lett. 2 (1995), 221–238.

[17] C. H. Taubes, SW =⇒ Gr: from the Seiberg-Witten equations to pseu- doholomorphic curves, J. Amer. Math. Soc. 9 (1996), 845–918.

[18] C. H. Taubes, Counting pseudo-holomorphic submanifolds in dimension 4, J. Differential Geometry 44 (1996) no. 4, 818–893.

[19] C. H. Taubes, Counting curves and connections, preprint.

[20] E. Witten, Monopoles and 4-manifolds, Math. Res. Lett/ 1 (1994), 769–

796.
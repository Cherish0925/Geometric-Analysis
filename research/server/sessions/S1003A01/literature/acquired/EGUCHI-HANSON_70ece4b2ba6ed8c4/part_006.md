---
retention_scope: session
part: 6
total_parts: 6
---

[Part 6/6 of: EGUCHI-HANSON]

Now we may iterate the estimate of Claim 1 to prove the desired result. First
note that due to Shi’s estimates, for any *R<sub>0</sub>* > 0 and t<sub>0</sub> > 0 we have that *u ∈*
√<sub>τ</sub>
τ
L<sup>2</sup>(BR<sub>0</sub>(0) × [t<sub>0</sub>,T]). We take t<sub>0</sub> = <sup>τ</sup><sub>2</sub>, R<sub>0</sub> = 2 + <sub>2</sub>, ∆t<sub>i</sub> = (∆R<sub>i</sub>)<sup>2</sup> = <sub>i+1</sub>, p<sub>i</sub> = 2<sup>i+1</sup>
2
and

$$
R _ {0} > 0
$$

$$
t _ {0} > 0
$$

$$
u \in
$$

$$
L ^ {2} \left(B _ {R _ {0}} (0) \times [ t _ {0}, T ]\right)
$$

$$
t _ {0} = \frac {\tau}{2}, R _ {0} = 2 + \sqrt {\frac {\tau}{2}}, \Delta t _ {i} = \left(\Delta R _ {i}\right) ^ {2} = \frac {\tau}{2 ^ {i + 1}}, p _ {i} = 2 ^ {i + 1}
$$

$$
R _ {i + 1} = R _ {i} - \Delta R _ {i}
$$

$$
t _ {i + 1} = t _ {i} + \Delta t _ {i}.
$$

Then inductively applying the estimate of Claim 1 and taking the limit as *i →∞,*
we obtain

$$
i \rightarrow \infty
$$

$$
\| u \| _ {L ^ {\infty} \left(B _ {2} (0) \times [ \tau , T ]\right)} \leq C _ {\infty} \| u \| _ {L ^ {2} \left(B _ {R _ {0}} (0) \times [ \frac {\tau}{2}, T ]\right)} < \infty ,
$$

where *C*<sub>∞</sub>> 0 is a positive constant. This proves the desired result.

$$
C _ {\infty} > 0
$$

Next, we prove that the higher derivatives of the curvature tensor are also bounded
at positive times. For this we need a generalization of Shi’s estimates for the situation in which some of the derivatives of the curvature tensor are known to be
bounded. In particular, we have

Theorem 12.15 (Shi’s interior estimates with derivative bounds). *Let n ≥* 2 *and
m ≥ 1. Then for every choice of constant K* > 0 *there exists constants θ* > 0 *and
C* > 0 *such that the following holds: Let M be an open manifold M of dimension n*
θ
and 0 < T ≤ <sub>K</sub>. Assume that g(t), t ∈ [0,T], is a solution to the Ricci flow on an
*open subset U of M and*

$$
n \geq 2
$$

$$
m \geq 1
$$

$$
K > 0
$$

$$
\theta > 0
$$

$$
C > 0
$$

$$
0 < T \leq \frac {\theta}{K}
$$

$$
g (t), t \in [ 0, T ]
$$

$$
| \nabla^ {l} R m | \leq K \text {o n} U \times [ 0, T ] \text {a n d f o r} l \in \{0, 1, 2, \dots , m \}
$$

---

*If for p ∈ U and r* > 0 *the closed set B*
(

<sub>g(0)</sub>(p,r) is contained in U then
)
()

$$
p \in U
$$

$$
r > 0
$$

$$
B _ {g (0)} (p, r)
$$

$$
\left| \nabla^ {m + 1} R m \right| ^ {2} \leq C \left(\frac {1}{r ^ {2}} + \frac {1}{t} + 1\right) o n B _ {g (0)} \left(p, \frac {r}{2}\right) \times (0, T ]
$$

*Proof.* We follow the proofs of [CZ06, Theorem 1.4.2] and [ChII, Theorem 14.16].
In the following the constant *C* depends on *m* and *n* only and may vary from line
to line. Consider the quantity
()

$$
S = \left(B K ^ {2} + | \nabla^ {m} R m | ^ {2}\right) | \nabla^ {m + 1} R m | ^ {2},
$$

where *B* > 0 is to be fixed later. With help of the differential inequality (12.13) we
obtain

$$
B > 0
$$

$$
\begin{array}{l} \partial_ {t} S \leq \Delta S - 2 \nabla | \nabla^ {m} R m | ^ {2} \nabla | \nabla^ {m + 1} R m | ^ {2} - 2 | \nabla^ {m + 1} R m | ^ {4} \\ + \sum_ {j} c _ {m j} \cdot | \nabla^ {j} R m | \cdot | \nabla^ {m - j} R m | \cdot | \nabla^ {m} R m | \cdot | \nabla^ {m + 1} R m | ^ {2} \\ - 2 \left(B K ^ {2} + | \nabla^ {m} R m | ^ {2}\right) | \nabla^ {m + 2} R m | ^ {2} \\ + \left(B K ^ {2} + | \nabla^ {m} R m | ^ {2}\right) \sum_ {j} c _ {m + 1 j} \cdot | \nabla^ {j} R m | \cdot | \nabla^ {m + 1 - j} R m | \cdot | \nabla^ {m + 1} R m | \\ \end{array}
$$

Using Cauchy’s inequality and the assumption that
we deduce

|∇<sup>l</sup>

*Rm|≤ K* for *l* = *0,1,2, ··· m,*

$$
| \nabla^ {l} R m | \leq K
$$

$$
l = 0, 1, 2, \dots m
$$

$$
\begin{array}{l} \partial_ {t} S \leq \Delta S + 8 K | \nabla^ {m + 1} R m | ^ {2} | \nabla^ {m + 2} R m | - 2 | \nabla^ {m + 1} R m | ^ {4} - 2 B K ^ {2} | \nabla^ {m + 2} R m | ^ {2} \\ + C K ^ {3} | \nabla^ {m + 1} R m | ^ {2} + C K ^ {3} (B + 1) \left(| \nabla^ {m + 1} R m | ^ {2} + K | \nabla^ {m + 1} R m |\right) \\ \end{array}
$$

Noting that for all *x ∈* R we have *x<sup>2</sup>*
Young’s inequality that

+ *Kx ≤ 2x<sup>2</sup>* +

<sup>1</sup><sub>4</sub>K<sup>2</sup> we obtain with help of

$$
x \in \mathbb {R}
$$

$$
x ^ {2} + K x \leq 2 x ^ {2} + \frac {1}{4} K ^ {2}
$$

$$
\begin{array}{l} \partial_ {t} S \leq \Delta S - | \nabla^ {m + 1} R m | ^ {4} + 2 (3 2 - B) K ^ {2} | \nabla^ {m + 2} R m | ^ {2} \\ + C K ^ {6} + C K ^ {5} (B + 1) + C K ^ {6} (B + 1) ^ {2}. \\ \end{array}
$$

Taking *B* = 32 and assuming without loss of generality that

*K* > 1, we obtain

$$
K > 1
$$

$$
\partial_ {t} S \leq \Delta S - \frac {S ^ {2}}{C K ^ {4}} + C K ^ {6}
$$

From here we may follow the proof of [CZ06, Theorem 1.4.2] to deduce the desired
result.

With help of Theorem 12.15 we inductively prove that the higher derivatives of
the curvature tensor are bounded.

Lemma 12.16. *Let* (R<sup>4</sup> *\{0},g(t)), t ∈* [*0,T], be a Ricci flow as in Theorem 12.11.*
Then for any τ > 0 there exist constants C<sub>m</sub> = C<sub>m</sub>(K,τ) > 0, m ∈ N, such that

$$
\left(\mathbb {R} ^ {4} \backslash \{0 \}, g (t)\right), t \in [ 0, T ]
$$

$$
\tau > 0
$$

$$
C _ {m} = C _ {m} (K, \tau) > 0, m \in \mathbb {N}
$$

$$
| \nabla^ {m} R m | < C _ {m}
$$

*on* R<sup>4</sup> *×\{0}×* [*τ,T].*

$$
\mathbb {R} ^ {4} \times \backslash \{0 \} \times [ \tau , T ].
$$

---

*Proof.* We prove this lemma by induction. By Lemma 12.14 the result is true for
*m* = 1. Assume that the result is true for *m ≤ N.* Then there exist constants
C<sub>l</sub> > 0, l = 1,2,3, ··· ,N such that
[]
τ

$$
m = 1
$$

$$
m \leq N
$$

$$
C _ {l} > 0, l = 1, 2, 3, \dots , N
$$

$$
| \nabla^ {l} R m | \leq C _ {l} \mathrm {o n} \mathbb {R} ^ {4} \backslash \{0 \} \times \left[ \frac {\tau}{4}, T \right] \mathrm {a n d f o r} l = 1, 2, 3, \dots , N.
$$

As in the proof of Lemma 12.14, choose coordinates x<sup>i</sup>, i = 1,2,3,4, such that g(0)
∑
can be extended to a C<sup>1,1</sup> metric on R<sup>4</sup>, and write s<sup>2</sup> = <sub>i</sub>(x<sup>i</sup>)<sup>2</sup>. As the curvature
of *g(t), t ∈* [0,T], is bounded there exists a *λ* > 0 such that

$$
x ^ {i}, i = 1, 2, 3, 4
$$

$$
g (0)
$$

$$
\mathbb {R} ^ {4}
$$

$$
C ^ {1, 1}
$$

$$
s ^ {2} = \sum_ {i} \left(x ^ {i}\right) ^ {2}
$$

$$
g (t), t \in [ 0, T ]
$$

$$
\lambda > 0
$$

$$
\frac {1}{\lambda} g (0) \leq g (t) \leq \lambda g (0) \mathrm {o n} \mathbb {R} ^ {4} \setminus \{0 \} \times [ 0, T ].
$$

By the modified Shi’s estimates of Theorem 12.15 we see that
()
[

$$
| \nabla^ {N + 1} R m | \leq C \left(\frac {1}{s} + 1\right) \text {o n} \mathbb {R} ^ {4} \backslash \{0 \} \times \left[ \frac {\tau}{2}, T \right],
$$

for some C that depends on τ,K, and C<sub>l</sub>, l = 1,2, ··· ,N, only. In particular, this
implies that for all *R* > 0 the function *u ∈* L<sup>2</sup>(BR(0)) *×* [0,T]. By the differential
inequality (12.13) for the evolution of the curvature derivatives we see that

$$
\tau , K
$$

$$
C _ {l}, l = 1, 2, \dots , N
$$

$$
R > 0
$$

$$
u \in L ^ {2} \left(B _ {R} (0)\right) \times [ 0, T ]
$$

$$
\left(\partial_ {t} - \Delta\right) | \nabla^ {N + 1} R m | ^ {2} \leq - 2 | \nabla^ {N + 2} R m | ^ {2} + C K ^ {2} | \nabla^ {N + 1} R m | + C K | \nabla^ {N + 1} R m | ^ {2}
$$

and hence

$$
\left(\partial_ {t} - \Delta\right) | \nabla^ {N + 1} R m | \leq C K \left(K + | \nabla^ {N + 1} R m |\right).
$$

Thus defining

$$
u = e ^ {- C K t} \left(| \nabla^ {N + 1} R m | + K\right)
$$

we deduce that

$$
\left(\partial_ {t} - \Delta\right) u \leq 0.
$$

Now we are in the same setup as in the proof of Lemma 12.14. Therefore we may
use the same De Giorgi-Nash-Moser iteration argument to show that *u* and hence
|∇<sup>N+1</sup>Rm| are bounded in R<sup>4</sup> × [τ,T]. This proves the desired result.

$$
\left| \nabla^ {N + 1} R m \right|
$$

$$
\mathbb {R} ^ {4} \times [ \tau , T ]
$$

Now we may prove the main Theorem 12.11:

Proof of Theorem 12.11. By Lemma 12.12 we can choose coordinates x<sup>i</sup>, i = 1,2,3,4,
for R<sup>4</sup> such that g(T) can be extended to a C<sup>1,1</sup> metric on all of R<sup>4</sup>. Below we write
g = g(T) for brevity. By [DK81, Lemma 1.2] there exist C<sup>2,α</sup> harmonic coordinates
y<sup>i</sup>: U → R, i = 1,2,3,4, in an open neighborhood U of R<sup>4</sup> containing the origin
and satisfying

$$
x ^ {i}, i = 1, 2, 3, 4
$$

$$
\mathbb {R} ^ {4}
$$

$$
C ^ {1, 1}
$$

$$
g (T)
$$

$$
\mathbb {R} ^ {4}
$$

$$
g = g (T)
$$

$$
C ^ {2, \alpha}
$$

$$
y ^ {i}: U \rightarrow \mathbb {R}, i = 1, 2, 3, 4
$$

$$
\mathbb {R} ^ {4}
$$

$$
U
$$

(1)

$$
y ^ {i} = 0
$$

(2)

$$
\frac {\partial y ^ {i}}{\partial x ^ {j}} = \delta_ {j} ^ {i}
$$

at the origin. Furthermore, as *g* is smooth on *U \{0},* it follows from interior elliptic
regularity that y<sup>i</sup> are smooth on U \{0}. Write
() ()

$$
U \backslash \{0 \}
$$

$$
g
$$

$$
y ^ {i}
$$

$$
U \setminus \{0 \}
$$

$$
g _ {i j} = g \left(\frac {\partial}{\partial y ^ {i}}, \frac {\partial}{\partial y ^ {j}}\right) \mathrm {a n d} R i c _ {i j} = R i c _ {g} \left(\frac {\partial}{\partial y ^ {i}}, \frac {\partial}{\partial y ^ {j}}\right).
$$

---

We have that g<sub>ij</sub> ∈ C<sup>1,α</sup>(U) with respect to the y<sup>i</sup> coordinates. Furthermore, g<sub>ij</sub> is
smooth on *U \{0}.*

$$
g _ {i j} \in C ^ {1, \alpha} (U)
$$

$$
y ^ {i}
$$

$$
g _ {i j}
$$

$$
U \setminus \{0 \}
$$

By [PP, Chapter 10, Lemma 49]) we have

(12.16)

$$
\frac {1}{2} \Delta g _ {i j} + Q (g, \partial g) = - R i c _ {i j} \mathrm {o n} U \setminus \{0 \},
$$

where *Q(g,∂g*) is some universal analytic expression that is polynomial in the ma-
√
∂g
trix g, quadratic in <sub>i</sub>, and has a denominator term depending on detg<sub>ij</sub>. The
∂y
equation (12.16) makes sense on all of *U* if we interprete it in the weak sense.

$$
Q (g, \partial g)
$$

$$
g,
$$

$$
\frac {\partial g}{\partial y ^ {i}}
$$

$$
\sqrt {d e t g _ {i j}}
$$

Claim 1: If g<sub>ij</sub>(y) ∈ C<sup>k</sup>(U) for k ∈ N then R<sub>ij</sub>(y) ∈ C<sup>k−1,1</sup>(U).

$$
g _ {i j} (y) \in C ^ {k} (U) \mathrm {f o r} k \in \mathbb {N} \mathrm {t h e n} R _ {i j} (y) \in C ^ {k - 1, 1} (U)
$$

*Proof of Claim:* Write

$$
Y _ {i} = \frac {\partial}{\partial y ^ {i}} \mathrm {f o r} i = 1, 2, 3, 4.
$$

on *U \{0}* we have

$$
U \setminus \{0 \}
$$

$$
\begin{array}{l} \frac {\partial^ {k}}{\partial y ^ {i _ {1}} \partial y ^ {i _ {2}} \dots \partial y ^ {i _ {k}}} R i c _ {i j} = Y _ {i _ {1}} Y _ {i _ {2}} \dots Y _ {i _ {k}} R i c \left(Y _ {i}, Y _ {j}\right) \\ = \nabla_ {Y _ {i _ {1}}} \nabla_ {Y _ {i _ {2}}} \dots \nabla_ {Y _ {i _ {k}}} R i c \left(Y _ {i}, Y _ {j}\right) \\ \end{array}
$$

Since covariant differentiation commutes with contractions, we can use the product
rule to express the above derivative as a sum of terms, which only involve ∇<sup>m</sup>Ric,
m = 1,2, ··· ,k, and ∇<sup>m</sup>Y<sub>i</sub><sub>l</sub>, m,l = 1,2,3, ··· ,k, contracted with Y<sub>i</sub>, Y<sub>j</sub> and Y<sub>i</sub><sub>l</sub>,
*l* = *1,2, ··· ,k.* As by Lemma 12.16 all the derivatives of the curvature tensor are
bounded and g<sub>ij</sub>(y) ∈ C<sup>k</sup>(U) we see that

$$
\nabla^ {m} R i c.
$$

$$
m = 1, 2, \dots , k
$$

$$
\nabla^ {m} Y _ {i _ {l}}, m, l = 1, 2, 3, \dots , k
$$

$$
Y _ {i}, Y _ {j}
$$

$$
Y _ {i _ {l}}
$$

$$
l = 1, 2, \dots , k
$$

$$
g _ {i j} (y) \in C ^ {k} (U)
$$

$$
\frac {\partial^ {k}}{\partial y ^ {i _ {1}} \partial y ^ {i _ {2}} \cdots \partial y ^ {i _ {k}}} R i c _ {i j}
$$

is bounded as well. Hence the k-th spatial derivatives ∂<sup>k</sup>Ric<sub>ij</sub> are bounded, which
implies that ∂<sup>k−1</sup>Ric<sub>ij</sub> is a Lipshitz function and can be continuously extended to a
all of U. Similarly, the lower order derivatives ∂<sup>m</sup>Ric<sub>ij</sub>, m = 0,1,2, ··· ,k − 2, can
be continuously extended to the origin.

$$
\partial^ {k} R i c _ {i j}
$$

$$
\partial^ {k - 1} R i c _ {i j}
$$

$$
U
$$

$$
\partial^ {m} R i c _ {i j}, m = 0, 1, 2, \dots , k - 2
$$

First note that g is a C<sup>1,1</sup>(U) weak solution of the elliptic equation (12.16). Furthermore Q(g,∂g) ∈ C<sup>0,1</sup>(U) and by Claim 1 we have Ric<sub>ij</sub> ∈ C<sup>0,1</sup>(U) as well. Since
such weak solutions are unique, and there exists a C<sup>2,α</sup>(U) solution that agrees on
the boundary ∂U, we see that g is in fact C<sup>2,α</sup>(U). Bootstrapping standard Schauder
estimates and the result of Claim 1, we conclude that g<sub>ij</sub> is smooth with respect to
the harmonic coordinates y<sup>i</sup>, i = 1,2,3,4. As the higher derivatives of the curvature
tensor are bounded, it follows that for all times *t ∈* (0,T] the metric *g(t*) is smooth
with respect to the coordinates y<sup>i</sup>, i = 1,2,3,4. This proves the desired result.

$$
g
$$

$$
C ^ {1, 1} (U)
$$

$$
Q (g, \partial g) \in C ^ {0, 1} (U)
$$

$$
R i c _ {i j} \in C ^ {0, 1} (U)
$$

$$
C ^ {2, \alpha} (\tilde {U})
$$

$$
\partial U
$$

$$
C ^ {2, \alpha} (U)
$$

$$
g
$$

$$
g _ {i j}
$$

$$
y ^ {i}, i = 1, 2, 3, 4
$$

$$
t \in (0, T ]
$$

$$
g (t)
$$

$$
y ^ {i}, i = 1, 2, 3, 4
$$

---

## References

[A17] A. Appleton, *A family of non-collapsed steady Ricci solitons in even dimensions greater or
equal to four,* arXiv:1708.00161

[AIK11] S. B. Angenent, J. Isenberg, and D. Knopf, *Formal matched asymptotics for degenerate
Ricci flow neckpinches,* Nonlinearity 24 (2011), no. 8, 22652280

[AIK15] S. B. Angenent, J. Isenberg, and D. Knopf, *Degenerate neckpinches in Ricci flow,* J. Reine
Angew. Math. (Crelle) 709 (2015), 81-117

[AW19] A. Appleton, J. Wilkening, *Computation of* U(2)-*invariant Ricci flow singularities,* In
Preparation.

[B05] R.L. Bryant, *Ricci flow solitons in dimension three with SO(3)-symmetries,* available at
www.math.duke.edu/ bryant/3DRotSymRicciSolitons.pdf

[Bre18] S. Brendle, *Ricci flow with surgery in higher dimensions,* Ann. of Math. (2) 187 (2018),
no. 1, 263299

[Cal79] E. Calabi, *Ḿetriques k¨ahĺeriennes et fibŕes holomorphes,* Ann. Sci. Ecole Norm. Sup. (4)
12 (1979), no. 2, 269294.

[Cao10] H. D. Cao, *Recent Progress on Ricci Solitons,* Advanced Lectures in Mathematics, 11
(2010), 1-38.

[CZ06], H. D. Cao, X. P. Zhu, *A Complete Proof of the Poincaŕe and Geometrization Conjectures*
*- Application of the Hamilton-Perelman Theory of the Ricci Flow,* Asian J. Math., Vol. 10, No.
2, pp. 165492, 2006

[BC04] B. Chow, D. Knopf, *Ricci Flow: An Introduction,* Mathematical Surveys and Monographs,
AMS, Providence, RI, 2004.

[CLN06] , B. Chow, P. Lu, L. Ni, *Hamiltons Ricci flow,* Lectures in Contemporary Mathematics,
3, Science Press and Graduate Studies in Mathematics, 77, American Mathematical Society
(co-publication), 2006.

[ChI] B. Chow et al., *The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects,*
Mathematical Surveys and Monographs, Vol. 135 American Mathematical Society, Providence,
RI (2007)

[ChII] B. Chow et al., *The Ricci Flow: Techniques and Applications: Part II: Analytic Aspects,*
Mathematical Surveys and Monographs, Vol. 144 American Mathematical Society, Providence,
RI (2008)

[CZ06] B.-L. Chen, X.-P. Zhu, *Uniqueness of the Ricci flow on complete noncompact manifolds,*
J. Differential Geom., Volume 74, Number 1 (2006), 119-154.

[CZ10] H.-D. Cao, D. Zhou, *On complete gradient shrinking Ricci solitons,* J. Differential Geom.,
Volume 85, Number 2 (2010), 175-186

[DeT83] D. DeTurck, *Deforming metrics in the direction of their Ricci tensors,* Journal of Differential Geometry 18 (1983), no. 1, 157162.

[DK81] D. DeTurck, J. L. Kazdan, *Some regularity theorems in Riemannian geometry,* Ann. Sci.
Ecole Norm. Sup. (4) 14 (1981), no. 3, 249260. MR 83f:53018

[EH79] T. Eguchi; A. J. Hanson *Selfdual solutions to Euclidean gravity,* Annals of Physics. 120:
82105 (1979)

[EMT11] J. Enders, R. Mueller, P. Topping, *On Type I Singularities in Ricci flow,* Communications
in Analysis and Geometry, 19 (2011) 905–922

[FIK03] M. Feldman, T. Ilmanen, D. Knopf, *Rotationally symmetric shrinking and expanding
gradient K¨ahler-Ricci solitons,* J. Diff. Geom., 65 (2003), 169-209.

[F64] A. Friedman, *Partial Differential Equations of Parabolic Type,* Englewood Cliffs, N.J.,
Prentice-Hall [1964]

[Fee13] P. M. N. Feehan, *Maximum Principles For Boundary-Degenerate Linear Parabolic Differential Operators,* arXiv:1306.5197

---

[GH78] G.W.Gibbons, S.W.Hawking, *Gravitational multi-instantons,* Physics Letters B, Volume
78, Issue 4, Pages 430-432 (1978)

[GH79] G.W.Gibbons, S.W.Hawking, *Classification of gravitational instanton symmetries,* Comm.
Math. Phys. Volume 66, Number 3, Pages 291-310 (1979)

[Ham82] R. S. Hamilton, *Three-manifolds with positive Ricci curvature,* J. Differential Geometry,
17 (1982) 255-306

[Ham95] R. S. Hamilton, *The formation of singularities in the Ricci flow,* Surveys in Differential
Geometry, 2: 7136 (1995)

[Ham86] R. S. Hamilton, *Four-manifolds with positive curvature operator,* J. Differential Geom.
24 (1986), no. 2, 153179.

[Ham97] R. S. Hamilton, *Four-manifolds with positive isotropic curvature,* Comm. Anal. Geom. 5
(1997), no. 1, 192.

[IKS17] J. Isenberg, D. Knopf, N. Sesum, *Non-k¨ahler Ricci Flow Singularities That Converge To
K¨ahler-Ricci Solitons,* arXiv:1703.02918v2

[K14] B. Kotschwar, *An energy approach to the problem of uniqueness for the Ricci flow,* Communications in Analysis and Geometry, 22(1), 149-176 (2014)

[KL08] B. Kleiner, J. Lott, *Notes on Perelmans papers,* Geometry & Topology 12 (2008) 25872858

[KL17] B. Kleiner, J. Lott, *Singular Ricci flows I,* Acta Math. 219 (2017), no. 1, 65–134.

[KronI89] P.B. Kronheimer, *The Construction of ALE Spaces as Hyper-K¨ahler Quotients,* J. Differential Geometry, 29 (1989) 665-683

[KronII89] P.B. Kronheimer, *A Torelli-type Theorem for Gravitational Instantons,* J. Differential
Geometry, 29 (1989) 685-697

[L96] G. M. Lieberman, *Second order parabolic differential equations,* World Scientific Publishing,
N.J., River Edge (1996)

[LZ18] Xiaolong Li, Yongjia Zhang, *Ancient solutions to the Ricci flow in higher dimensions,*
arXiv:1812.04156

[M14] D. Maximo, *On the blow-up of four-dimensional Ricci flow singularities,* J. Reine Angew.
Math. 692 (2014), 153171

[N10] A. Naber, *Noncompact shrinking four solitons with nonnegative curvature.* J. Reine Angew.
Math. 645 (2010), 125153.

[Perl02] G. Perelman, *The entropy formula for the Ricci flow and its geometric applications,*
arXiv:math/0211159

[Perl03] G. Perelman, *Ricci flow with surgery on three-manifolds,* arXiv:math/0303109

[PP] P. Petersen, *Riemannian Geometry,* Springer International Publishing (2016)

[PW84] M. Protter, H. Weinberger, *Maximum Principles in Differential Equations,* Springer,
Berlin, Heidelberg, (1984)

[Shi89] W.-X. Shi, *Deforming the metric on complete Riemannian manifolds,* J. Differential Geometry 30(1989) 223-301

[Top06] P. Topping, *Lectures on the Ricci Flow,* London Mathematical Society, Lecture Note series
325, Cambridge University Press (2006)

[VZ18] L. Verdiani, W. Ziller, *Smoothness Conditions in Cohomogeneity manifolds,*
arXiv:1804.04680

[W43] H. Whitney, *Differentiable even functions,* Duke Math. J. Volume 10, Number 1 (1943),
159-160.

Department of Mathematics, UC Berkeley, CA 94720, USA
*Email address:* aja44@berkeley.edu
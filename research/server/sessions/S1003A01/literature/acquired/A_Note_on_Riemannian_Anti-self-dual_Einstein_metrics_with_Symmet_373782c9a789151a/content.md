---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: hep-th_0609071.pdf
converter: mathpix
format: mmd
---

\title{
A Note on Riemannian Anti-self-dual Einstein metrics with Symmetry
}

\author{
Paul Tod \\ Mathematical Institute and St John's College \\ Oxford
}

October 1, 2018

\begin{abstract}
We give a complete proof of the result stated in [1], that the general Einstein metric with a symmetry, an anti-self-dual Weyl tensor and nonzero scalar curvature is determined by a solution of the $S U(\infty)$ -Toda field equation. We consider the two canonical forms found for solutions to the same problem by Przanowski [2] and show that his Class A will reduce to the Toda equation with respect to a second complex structure, different from that in which the metric is first given.
\end{abstract}

\section*{1 Introduction}

In [1] it was claimed that the general four-dimensional Riemannian Einstein metric with anti-self-dual (ASD) Weyl curvature and a Killing vector could be written in a particular form, based on a solution of the $S U(\infty)$-Toda field equation. A similar problem had been addressed by Przanowski [2] a little earlier. Having previously found that these metrics are necessarily Hermitian, he considered four-dimensional Hermitian-Einstein metrics with anti-self-dual (ASD) Weyl curvature and a Killing vector, and he obtained two apparently different classes of metrics, depending on the form of the Killing vector. One he was able to reduce to the $S U(\infty)$-Toda field equation, but the other he was not.

In this note, we shall give details of the proof of the result in [1], which have not previously appeared. This provides an algorithm for reducing any particular ASD Einstein metric with symmetry to the desired form. As such, it is close to LeBrun's reduction of a scalar-flat Kähler metric with symmetry [3], which it was inspired by. Applying the algorithm to a metric
in Przanowski's class B effects the reduction to Toda, which he had already done. Applying it to a metric in his class A shows that such a metric has a second complex structure, and it is with respect to the second that the metric takes the desired form.

In the remainder of this Section, we shall review the construction given in [1], and in the next we shall apply it to Przanowski's two forms.

Suppose then that we have a four-dimensional Riemannian Einstein metric $g$ with ASD Weyl tensor and a Killing vector $K$. We shall use the two-component spinor formalism [4], adapted for Riemannian signature. The derivative of the Killing vector decomposes as
$$\nabla_{a} K_{b}=\phi_{A B} \epsilon_{A^{\prime} B^{\prime}}+\psi_{A^{\prime} B^{\prime}} \epsilon_{A B},$$
in terms of symmetric spinors $\phi_{A B}$ and $\psi_{A^{\prime} B^{\prime}}$. Any Killing vector satisfies the identity
$$\nabla_{a} \nabla_{b} K_{c}=R_{b c a d} K^{d}$$
in terms of the Riemann tensor $R_{a b c d}$, and with (1) and our assumptions about the curvature this entails
$$\begin{aligned}
\nabla_{A A^{\prime}} \phi_{B C} & =-\psi_{B C A D} K_{A^{\prime}}^{D}+2 \Lambda \epsilon_{A(B} K_{C) A^{\prime}} \\
\nabla_{A A^{\prime}} \psi_{B^{\prime} C^{\prime}} & =2 \Lambda \epsilon_{A^{\prime}\left(B^{\prime}\right.} K_{\left.C^{\prime}\right) A}
\end{aligned}$$
Here the conventions are slightly different from [1], to be in line with [4]: $\psi_{A B C D}$ is the ASD Weyl spinor, corresponding to the ASD Weyl tensor, and $\Lambda=R / 24$ where $R$ is the Ricci scalar.

Define the scalar $\psi$ by
$$2 \psi^{2}=\psi^{A^{\prime} B^{\prime}} \psi_{A^{\prime} B^{\prime}},$$
and then define the tensor $J_{a}^{b}$ by
$$J_{a}^{b}=\psi^{-1} \delta_{A}^{B} \psi_{A^{\prime}}^{B^{\prime}} .$$
From the definition of $\psi$ it follows that $J_{a}^{b}$ is an almost-complex structure. Now from (3) we have
$$\nabla_{A\left(A^{\prime}\right.} \psi_{\left.B^{\prime} C^{\prime}\right)}=0$$
so that the spinor field $\psi_{B^{\prime} C^{\prime}}$ satisfies the twistor equation [4]. It then follows from a result of Pontecorvo [5] that this almost-complex structure is integrable. (See the interpretation of this result in [6]; in our setting, it can be checked directly: given (3) it is straightforward to calculate the Nijenhuis
tensor for $J_{a}{ }^{b}$ and see that it vanishes.) Thus an ASD Einstein metric with symmetry is necessarily Hermitian, as was known to Przanowski, [2], [7], [8].

From (3) and the definition of the scalar $\psi$ we find
$$2 \psi \nabla_{A A^{\prime}} \psi=\psi^{B^{\prime} C^{\prime}} \nabla_{A A^{\prime}} \psi_{B^{\prime} C^{\prime}}=2 \Lambda \psi_{A^{\prime} B^{\prime}} K_{A}^{B^{\prime}}$$
We introduce a coordinate $w=\Lambda \psi^{-1}$ and then the equation above implies
$$J_{a b} K^{a} d x^{b}=-\frac{d w}{w^{2}} .$$
Guided by [1], we introduce a coordinate $\tau$ with $K^{a} \partial_{a} \tau=1$ and a function $P$ related to the norm of the Killing vector by
$$P w^{2}=\left(g_{a b} K^{a} K^{b}\right)^{-1} .$$
It follows from (5) and (6), since the complex structure preserves lengths, that
$$g\left(\frac{d w}{w^{2}}, \frac{d w}{w^{2}}\right)=g(K, K)=\left(P w^{2}\right)^{-1} .$$
Since the complex structure is integrable, we can introduce a complex coordinate $\zeta=x+i y$ on the 2-plane orthogonal to $K^{a}$ and $J_{b}{ }^{a} K^{b}$. The metric now takes the form
$$g=\frac{P}{w^{2}}\left(e^{v}\left(d x^{2}+d y^{2}\right)+d w^{2}\right)+\frac{1}{P w^{2}}(d \tau+\theta)^{2} .$$
for some function $v$ and one-form $\theta$. Note the similarity of this to LeBrun's scalar-flat Kähler metrics [3] (after multiplication by $w$, it is precisely one of LeBrun's class of metrics). To obtain an equation for $\theta$ we recall (1) and derive the pair of equations
$$\begin{aligned}
K^{b} \nabla_{a} K_{b} & =-\phi_{A B} K_{A^{\prime}}^{B}-\psi_{A^{\prime} B^{\prime}} K_{A}^{B^{\prime}} \\
K^{b}\left(\nabla_{a} K_{b}\right)^{*} & =\phi_{A B} K_{A^{\prime}}^{B}-\psi_{A^{\prime} B^{\prime}} K_{A}^{B^{\prime}}
\end{aligned}$$
where the star indicates Hodge dual. Using (4), (5) and (6) in these, we obtain
$$\frac{1}{2} d x^{a} \epsilon_{a b}{ }^{c d} K^{b} \nabla_{c} K_{d}=\frac{d P}{2 P^{2} w^{2}}+\frac{d w}{P w^{3}}+2 \Lambda \frac{d w}{w^{3}},$$
which translates into the following equation on $\theta$ :
$$\left.d \theta=P_{, x} d y \wedge d w+P_{, y} d w \wedge d x+e^{v}\left(P_{, w}+2 P(1+2 \Lambda P) w^{-1}\right)\right) d x \wedge d y .$$
This equation will have an integrability condition that we must return to.

To make further progress, we need to impose the ASD Einstein equations. A convenient route to these is as follows: suppose $\phi_{i}$ for $i=1,2,3$ is an orthonormal basis of SD 2-forms and introduce the connection 1-forms $\alpha_{i j}=$ $-\alpha_{j i}$ of the metric connection on these by the equation
$$d \phi_{i}=-\alpha_{i j} \wedge \phi_{j} ;$$
the ASD Einstein equations are now the system
$$d \alpha_{i j}+\alpha_{i k} \wedge \alpha_{k j}=2 \Lambda \epsilon_{i j k} \phi_{k} .$$
For the metric (7), a convenient orthonormal tetrad is
$$\begin{aligned}
\theta^{1} & =w^{-1} P^{1 / 2} e^{v / 2} d x, \\
\theta^{2} & =w^{-1} P^{1 / 2} e^{v / 2} d y, \\
\theta^{3} & =w^{-1} P^{1 / 2} d w, \\
\theta^{4} & =w^{-1} P^{-1 / 2}(d \tau+\theta),
\end{aligned}$$
and then the orthonormal basis of SD 2-forms can be taken to be
$$\begin{aligned}
& \phi_{1}=\theta^{1} \wedge \theta^{4}+\theta^{2} \wedge \theta^{3}, \\
& \phi_{2}=\theta^{2} \wedge \theta^{4}+\theta^{3} \wedge \theta^{1}, \\
& \phi_{3}=\theta^{3} \wedge \theta^{4}+\theta^{1} \wedge \theta^{2} .
\end{aligned}$$
For the connection one-forms we find
$$\begin{aligned}
\alpha_{31} & =A \theta^{1}, \\
\alpha_{23} & =-A \theta^{2}, \\
\alpha_{12} & =\frac{1}{2}\left(v_{, y} d x-v_{, x} d y\right)-\frac{2 \Lambda}{w}(d \tau+\theta),
\end{aligned}$$
where
$$A=-\frac{1}{2} P^{-1 / 2}\left(w v_{, w}-4 \Lambda P-4\right) .$$
Now impose the ASD Einstein equations to find first a condition defining $P$ :
$$-4 \Lambda P=2-w v_{, w},$$
and second an equation for $v$ :
$$v_{, x x}+v_{, y y}+\left(e^{v}\right)_{, w w}=0,$$
which one recognises as the $S U(\infty)$-Toda field equation.

This is all that one gets from the ASD Einstein equations. With the aid of (16), (8) simplifies to
$$d \theta=P_{, x} d y \wedge d w+P_{, y} d w \wedge d x+\left(P e^{v}\right)_{, w} d x \wedge d y,$$
The integrability condition is
$$P_{, x x}+P_{, y y}+\left(P e^{v}\right)_{, w w}=0,$$
which is easily seen to be satisfied by virtue of (16) and (17).
In summary, the metric is (7), where $v$ is chosen to be a solution of the $S U(\infty)$-Toda field equation, $P$ is given by (16) and $\theta$ is obtained by solving (18). The freedom in the choice of $\theta$ corresponds to the freedom in the choice of origin for $\tau$. Following the derivation of the metric in this form, we clearly have an algorithmic route to put any ASD Einstein metric with a symmetry into this form.

In the next section, we review Przanowski's form for ASD Hermitian-Einstein metrics with symmetry and show how to reconcile them with the form given here.

\section*{2 Przanowski's forms for the metric}

Przanowski [2] (see also [7], [8]) shows that an ASD Einstein metric can locally be written in terms of complex coordinates $Z^{\alpha}=\left(Z^{1}, Z^{2}\right)$ and a single real function $h$ in the form
$$g=2 g_{\alpha \bar{\beta}} d Z^{\alpha} d Z^{\bar{\beta}}$$
where, as usual, $Z^{\bar{\alpha}}=\overline{Z^{\alpha}}$, and
$$g_{\alpha \bar{\beta}}=-\frac{3}{l}\left(\partial_{\alpha} \partial_{\bar{\beta}} h+2 \delta_{\alpha}^{2} \delta_{\bar{\beta}}^{\overline{2}} e^{h}\right),$$
where $l=6 \Lambda$, in terms of $\Lambda$ from Section 1.
The ASD Einstein equation reduces to Przanowski's 'master equation' [2]
$$\partial_{1} \partial_{\overline{1}} h \partial_{2} \partial_{\overline{2}} h-\partial_{1} \partial_{\overline{2}} h \partial_{2} \partial_{\overline{1}} h+\left(2 \partial_{1} \partial_{\overline{1}} h-\partial_{1} h \partial_{\overline{1}} h\right) e^{h}=0 .$$
Now if $g$ has a Killing vector $K$, then Przanowski argues that it must be possible to arrange the coordinates so that one of the following two cases holds:

Class A:
$$K=i\left(\partial_{2}-\partial_{\overline{2}}\right)$$

Class B:
$$K=i\left(\partial_{1}-\partial_{\overline{1}}\right)$$
Let us attempt to reconcile the metric of Class B with what we have in Section 1. This has been done already in [2], but it prepares the way for Class A. Written out at length, the metric (19) is
$$g=-\frac{6}{l}\left(h_{, 1 \overline{1}} d Z^{1} d Z^{\overline{1}}+h_{, 1 \overline{2}} d Z^{1} d Z^{\overline{2}}+h_{, 2 \overline{1}} d Z^{2} d Z^{\overline{1}}+\left(h_{, 2 \overline{2}}+2 e^{h}\right) d Z^{2} d Z^{\overline{2}}\right),$$
with $h_{, 1}=h_{\overline{,} 1}$.
The function $P$ of (6) is obtained from the norm of the Killing vector via the equation
$$P=w^{-2}\left(K^{a} K_{a}\right)^{-1}=-w^{-2}\left(\frac{6}{l} h_{, 1 \overline{1}}\right)^{-1},$$
while the function $w$ is obtained from (5) by solving
$$\frac{d w}{w^{2}}=J_{a b} K^{a} d x^{b}=-\frac{3}{l}\left(h_{, 1 \overline{1}}\left(d Z^{1}+d Z^{\overline{1}}\right)+h_{, 1 \overline{2}} d Z^{\overline{2}}+h_{, 2 \overline{1}} d Z^{2}\right),$$
so that $w^{-1}=\frac{3}{l} h_{, 1}$.
The Killing vector lowered with the metric is
$$K_{a} d x^{a}=-\frac{3 i}{l}\left(h_{, 1 \overline{1}}\left(d Z^{\overline{1}}-d Z^{1}\right)+h_{, 1 \overline{2}} d Z^{\overline{2}}-h_{, 2 \overline{1}} d Z^{2} .\right.$$
With this, (24) and the formula for $w$, we can compare with (7) to find
$$\frac{P}{w^{2}} e^{v}\left(d x^{2}+d y^{2}\right)=-\frac{6 h_{1} h_{\overline{1}}}{l h_{1 \overline{1}}} d Z^{2} d Z^{\overline{2}}$$
so that the holomorphic coordinate $\zeta=x+i y$ can be taken to be $Z^{2}$, and then
$$e^{v}=4 w^{2} e^{h} .$$
It is now just a matter of checking that $v$ satisfies the Toda equation (17) by virtue of Przanowski's master equation (21).

If we try the same manipulations for Class A, with the Killing vector (22), we may first calculate
$$J_{a b} K^{a} d x^{b}=-\frac{3}{l}\left(h_{, 1 \overline{2}} d Z^{1}+h_{, \overline{12}} d Z^{\overline{1}}+\left(h_{, 2 \overline{2}}+2 e^{h}\right)\left(d Z^{2}+d Z^{\overline{2}}\right)\right),$$
but this is not (in general) exact, and so doesn't serve to define $w$. To see what has gone wrong, we calculate the self-dual part of the exterior derivative of $K$. By (1), this should be proportional to the complex structure. A lengthy but straightforward calculation leads to
$$(d K)^{+}=\frac{1}{2} h_{, 2} \Phi+i \frac{h_{, 1}}{\left|h_{, 1}\right|} e^{h / 2} \Psi-i \frac{h_{, \overline{1}}}{\left|h_{, 1}\right|} e^{h / 2} \bar{\Psi},$$
where
$$\begin{aligned}
\Phi= & -\frac{6 i}{l}\left(h_{, 1 \overline{1}} d Z^{1} \wedge d Z^{\overline{1}}+h_{, 1 \overline{2}} d Z^{1} \wedge d Z^{\overline{2}}\right. \\
& \left.+h_{, 2 \overline{1}} d Z^{2} \wedge d Z^{\overline{1}}+\left(h_{, 2 \overline{2}}+2 e^{h}\right) d Z^{2} \wedge d Z^{\overline{2}}\right) \\
\Psi= & \sqrt{\Delta} d Z^{1} \wedge d Z^{2},
\end{aligned}$$
and
$$\Delta=\frac{36}{l^{2}} h_{, 1} h_{, \overline{1}} e^{h}$$
which is (up to a constant) the determinant of the metric. $\Phi$ is the complex structure as a 2-form so that
$$\Phi \wedge \Phi=2 \Psi \wedge \bar{\Psi}=-2 \Delta d Z^{1} \wedge d Z^{\overline{1}} \wedge d Z^{2} \wedge d Z^{\overline{2}} .$$
Therefore the complex structure of Section 1, defined by the Killing vector, is different in Class A from the complex structure implicit in the metric written as in (19). If we follow the algorithm of Section 1 with the appropriate complex structure, then we must as before reduce to the Toda equation. However it doesn't seem possible to find the holomorphic coordinates for the new complex structure explicitly - one simply has a proof of local existence.

One shouldn't be surprised to find a second integrable complex structure. For an ASD Einstein metric, there are locally many integrable complex structures, as follows from the Kerr Theorem of twistor theory in the Riemannian setting (see e.g. [4]): an integrable complex structure is determined by a geodesic shear-free spinor field and these are given by the vanishing of a (suitable, local) holomorphic function in twistor space. In deriving the metric form (19), Przanowski [8] begins from an arbitrary complex structure, though he needs to make a specific choice within the class of holomorphic coordinates. Then for his Class B, the complex structure derived from the Killing vector coincides with the one from which he starts, but for Class A it doesn't.

There is a connection with scalar-flat Kähler metrics which is worth remarking: as noted above, the metric (7) is evidently conformal to Kähler
- multiply it by $w^{2}$ to obtain LeBrun's form [3] of the scalar-flat Kähler metric with symmetry. Thus an ASD Einstein metric with a symmetry is conformal to a scalar-flat Kähler metric. There is a partial converse of this result based on the following result:

Suppose $(M, J, g)$ is a Kähler manifold, with complex structure $J$ and metric $g$ and such that $(M, \tilde{g})$ is Einstein with nonzero scalar curvature, where $\tilde{g}$ is conformal to $g$, say $\tilde{g}=\Omega^{2} g$, then $g$ necessarily has a symmetry.

This is given in [9] as part of a larger theorem for compact $M$ but the argument is purely local, and doesn't require compactness. Clearly if $g$ or $\tilde{g}$ is ASD, then both are and $\tilde{g}$ has the form (7).

To prove the statement in italics above, suppose the Kähler form can be written in spinors as $J_{a b}=J_{A^{\prime} B^{\prime}} \epsilon_{A B}$. The Kähler condition implies that
$$\nabla_{A A^{\prime}} J_{B^{\prime} C^{\prime}}=0,$$
where $\nabla_{A A^{\prime}}$ is the Levi-Civita covariant derivative for $g$. From the formulae for conformal rescaling (see e.g. [4]), it follows that
$$\tilde{\nabla}_{A A^{\prime}} \tilde{J}_{B^{\prime} C^{\prime}}=2 \tilde{\epsilon}_{A^{\prime}\left(B^{\prime}\right.} K_{\left.C^{\prime}\right) A}$$
where $\tilde{J}_{B^{\prime} C^{\prime}}=\Omega^{2} J_{B^{\prime} C^{\prime}}, K_{A A^{\prime}}=\Upsilon_{A B^{\prime}} \tilde{\epsilon}^{B^{\prime} C^{\prime}} \tilde{J}_{A^{\prime} C^{\prime}}$ and $\Upsilon_{A A^{\prime}}=\partial_{A A^{\prime}} \log \Omega$. But now, by differentiating again and using the Ricci identities, the assumption that $(M, \tilde{g})$ is Einstein implies that
$$\tilde{\nabla}^{A B^{\prime}} \tilde{\nabla}_{A}^{C^{\prime}} \tilde{J}_{B^{\prime} C^{\prime}}=0=\tilde{\nabla}_{(B}^{A^{\prime}} \tilde{\nabla}_{A) A^{\prime}} \tilde{J}_{B^{\prime} C^{\prime}}$$
for any symmetric spinor $J_{B^{\prime} C^{\prime}}$. Substituting from (29) into this, we see that $K^{a}$ is a Killing vector.

\section*{Acknowledgements}

I acknowledge useful discussions with David Calderbank, Maciej Dunajski and Nigel Hitchin. This note was prompted by a question from Stefan Vandoren.

\section*{References}
\begin{itemize}
\item[] [1] K.P.Tod The $S U(\infty)$-Toda field equation and special four-dimensional metrics in Geometry and physics (1997) eds. J.E.Andersen, J.Dupont, H.Pedersen and A.Swann, Lecture Notes in Pure and Applied Mathematics, 184. Marcel Dekker, Inc., New York,
\end{itemize}
[2] M.Przanowski Killing vector fields in self-dual Euclidean Einstein spaces with $\Lambda \neq 0$ J.Math.Phys. 32 (1991) 1004-1010
[3] C.R.LeBrun Explicit self-dual metrics on $\mathbf{C P}_{2} \# \cdots \# \mathbf{C P}_{2}$ J.Diff.Geom. 34 (1991) 223-253
[4] R.Penrose and W.Rindler Spinors and space-time: I and II (1986) Cambridge: CUP
[5] M.Pontecorvo On twistor spaces of anti-self-dual Hermitian surfaces Trans.A.M.S. 33 (1992) 653-661
[6] D.Calderbank and H. Pedersen Self-dual Einstein metrics with torus symmetry J.Diff.Geom. 60 (2002) 485-521
[7] M.Przanowski and B.Baka One-sided type- $D$ gravitational instantons Gen.Rel.Grav. 16 (1984) 797-803
[8] M.Przanowski Locally-Hermit-Einstein self-dual gravitational instantons Acta.Phys.Polonica B14 (1983) 625-629
[9] V.Apostolov and P.Gauduchon The Riemannian Goldberg-Sachs theorem Int.Jour.Math. 8 (1997) 421-439
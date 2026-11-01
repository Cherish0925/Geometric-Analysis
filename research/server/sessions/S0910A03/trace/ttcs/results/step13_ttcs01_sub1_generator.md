# TTCS Independent Branch Record

```json
{
  "step_id": 13,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step12_reduced_equations_accessibility.md",
    "Sessions/S0910A01/workspace/notes/step13_normalized_accessibility_theorem.md"
  ]
}
```

## Task

For a four-dimensional negative Einstein metric Ric = -g with a local free circle action g = q + ell^2 theta^2, define H = Hess_q(ell)/ell. In the chiral variables a_+ = u - z/2 and a_- = u + z/2 where u = d log(ell) and z = *_q(ell F), we have W+ = -[sym nabla a_+ + a_+ otimes a_+]_0 and the electric Weyl E = (1/3)I - H + (|z|^2 I - z otimes z)/4, magnetic Weyl B = (1/2)(sym nabla z + u otimes z + z otimes u - <u,z>I). The trace constraint is tr(H) = 1 + |z|^2/2. The question: if the calibrated W+ spectrum is (-1/6, 1/12, 1/12), and the full curvature average is bounded (fint |Rm|^2 <= K_0), investigate whether H has nonnegative eigenvalues. In the static case (B=0, z=0), calibrated E has eigenvalues (-1/6, 1/12, 1/12), giving H = (1/2, 1/4, 1/4) > 0. For the general twisted case, express H = (1/3)I + Q - E where Q = (|z|^2 I - z otimes z)/4, and E = W+ - B. Determine: (A) Can large B (twist gradient) push an eigenvalue of H below zero while maintaining |W+|^2 = 1/24? (B) Does the L^2 smallness of |B| (from integral calibrated deficit) suffice to control H in L^p for p > 3/2? (C) Explore whether the chiral Riccati structure W+ = -[sym nabla a_+ + a_+ otimes a_+]_0 with |W+|^2 = 1/24 provides a direct estimate relating |B|^2 to |nabla z|^2 + |u|^2|z|^2 that would bound H from below. Seek a precise inequality or a counterexample (an explicit 1-jet model).

## Output

Let \(w=W^+\) and  
\[
G:=\frac13 I-w,\qquad 
Q:=\frac14\bigl(|z|^2I-z\otimes z\bigr).
\]
Then
\[
H=G+Q+B.
\]
For the calibrated spectrum
\[
\operatorname{Spec}(w)=\left(-\frac16,\frac1{12},\frac1{12}\right),
\]
one has
\[
\operatorname{Spec}(G)=\left(\frac12,\frac14,\frac14\right),
\qquad Q\ge 0.
\]
Hence the basic algebraic estimate is
\[
\boxed{H\ge \frac14 I+B}
\]
in operator order. Equivalently, for every unit vector \(v\),
\[
H(v,v)=\left(\frac13-w(v,v)\right)
+\frac14\bigl(|z|^2-\langle z,v\rangle^2\bigr)+B(v,v),
\]
so \(H(v,v)<0\) precisely requires
\[
B(v,v)<
-\left(\frac13-w(v,v)\right)
-\frac14|z\wedge v|^2.
\]
Thus \(Q\) never pushes \(H\) downward; the only downward mechanism is the magnetic/twist-gradient matrix \(B\).

## (A) Yes: a magnetic Weyl 1-jet can push an eigenvalue of \(H\) below zero while \(W^+\) stays calibrated

Take an orthonormal \(q\)-frame at a point \(p\), set
\[
z(p)=0,\qquad u(p)=0,
\]
and fix
\[
w=W^+=\operatorname{diag}\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Choose a trace-free symmetric magnetic matrix
\[
B_L=\operatorname{diag}\left(\frac L2,-L,\frac L2\right).
\]
Then
\[
H= \frac13I-w+B_L
=
\operatorname{diag}\left(\frac12+\frac L2,\frac14-L,\frac14+\frac L2\right).
\]
For every \(L>\frac14\), the second eigenvalue of \(H\) is below zero, while
\[
|W^+|^2=\frac1{24}
\]
and the full calibrated spectrum of \(W^+\) is unchanged.

This is compatible with the reduced point equations. Set
\[
\nabla z=2B_L,\qquad \nabla u=H.
\]
Then
\[
dz=0=-2u\wedge z,\qquad \operatorname{div}z=0=\langle u,z\rangle,
\]
and
\[
\operatorname{tr}H=1=1+\frac{|z|^2}{2}.
\]
Also
\[
E=\frac13I-H=w-B_L,
\qquad E+B_L=w=W^+.
\]
Thus this is an explicit calibrated reduced Einstein 1-jet with \(H\) having a sub-zero eigenvalue.

The anti-self-dual block is
\[
W^-=E-B_L=w-2B_L,
\]
so the full curvature sees \(B_L\). In this example
\[
|W^-|^2
=
6L^2+\frac12L+\frac1{24}.
\]
At the threshold \(L=\frac14\), this is \(13/24\), an order-one value. Therefore an averaged bound
\[
\fint |{\rm Rm}|^2\le K_0
\]
does not by itself force pointwise positivity of \(H\); it only gives an averaged \(L^2\)-type bound on \(B\).

## (B) \(L^2\)-small \(B\) controls only the sub-zero spectral tail of \(H\), not the full tensor \(H\)

From
\[
H\ge \frac14 I+B
\]
one obtains
\[
\lambda_{\min}(H)\ge \frac14+\lambda_{\min}(B)
\ge \frac14-|B|_{\rm op}.
\]
Hence, on a finite-measure region,
\[
\bigl(\lambda_{\min}(H)\bigr)_{<0}
\le \bigl(|B|_{\rm op}-\tfrac14\bigr)_+
\le |B|.
\]
Therefore, for \(1\le p\le2\),
\[
\boxed{
\left\|\bigl(\lambda_{\min}(H)\bigr)_{<0}\right\|_{L^p_{\rm av}}
\le
\|B\|_{L^p_{\rm av}}
\le
\|B\|_{L^2_{\rm av}}.
}
\]
In particular,
\[
\mu_{\rm av}\{\lambda_{\min}(H)<0\}
\le
16\,\|B\|_{L^2_{\rm av}}^2.
\]
So if some argument genuinely gives \(\|B\|_{L^2_{\rm av}}\ll1\), then \(H\) is positive semidefinite except on a small averaged spectral tail, and the tail is controlled in every \(L^p\) with \(p\le2\), including \(p>3/2\).

But this does **not** control the full \(H\) tensor in \(L^p\). The reason is the \(Q\)-term:
\[
H=\frac13I-w+Q+B,
\qquad Q\sim z^2.
\]
The four-dimensional Einstein curvature sees \(E\) and \(B\), while \(H\) and \(Q\) can cancel inside
\[
E=\frac13I-H+Q.
\]

A concrete 1-jet showing this is the following. Keep
\[
w=\operatorname{diag}\left(-\frac16,\frac1{12},\frac1{12}\right),
\qquad B=0,
\]
and choose
\[
u=N e^1,\qquad z=N e^1.
\]
Then
\[
Q=\operatorname{diag}\left(0,\frac{N^2}{4},\frac{N^2}{4}\right),
\]
and
\[
H=\frac13I-w+Q
=
\operatorname{diag}\left(
\frac12,\frac14+\frac{N^2}{4},\frac14+\frac{N^2}{4}
\right).
\]
Thus \(|H|\sim N^2\), while
\[
E=\frac13I-H+Q=w,\qquad W^+=W^-=w,
\]
so the Weyl blocks remain fixed.

The reduced first-order equations are satisfied by taking
\[
\nabla z
=
\langle u,z\rangle I-2u\otimes z
=
\operatorname{diag}(-N^2,N^2,N^2),
\]
and
\[
\nabla u=H-u\otimes u
=
\operatorname{diag}\left(
\frac12-N^2,\frac14+\frac{N^2}{4},\frac14+\frac{N^2}{4}
\right).
\]
Then
\[
dz=-2u\wedge z=0,\qquad
\operatorname{div}z=N^2=\langle u,z\rangle,
\]
and
\[
B=0
\]
exactly. Hence \(B\)-smallness can control the downward spectral tail of \(H\), but it cannot control \(|H|\), \(|z|^2\), \(|\nabla z|\), or ordinary quotient curvature.

Also, a \(W^+\)-calibrated integral residual alone cannot imply \(B\)-smallness: the first 1-jet above has exactly calibrated \(W^+\) for arbitrary \(B_L\). Smallness of \(B\) would have to enter through an additional identity involving \(W^-\), the full curvature distribution, or a separate twist estimate.

## (C) The chiral Riccati structure gives an exact cancellation identity, not a coercive bound for \(|\nabla z|^2+|u|^2|z|^2\)

Use the convention
\[
\operatorname{Sym}\nabla z=\frac12(\nabla z+\nabla z^T).
\]
From
\[
B=\frac12\left(\operatorname{Sym}\nabla z+u\odot z-\langle u,z\rangle I\right),
\]
together with
\[
dz=-2u\wedge z,\qquad \operatorname{div}z=\langle u,z\rangle,
\]
one obtains the pointwise reconstruction formula
\[
\boxed{
\nabla z=2B+\langle u,z\rangle I-2u\otimes z.
}
\]
Equivalently,
\[
\boxed{
4|B|^2
=
\left|\nabla z+2u\otimes z-\langle u,z\rangle I\right|^2.
}
\]
Expanding,
\[
|\nabla z|^2
=
4|B|^2
+4|u|^2|z|^2
-\langle u,z\rangle^2
-8B(u,z).
\]
This identity is sharp and explains the derivative-twist mechanism: \(B\) is the trace-free symmetric part of a combination of \(\nabla z\) and \(u\otimes z\), so large \(\nabla z\) and large \(u\otimes z\) can cancel inside \(B\).

The \(B=0\), \(u=z=Ne^1\) 1-jet above gives
\[
|\nabla z|^2+|u|^2|z|^2
=
3N^4+N^4
=
4N^4,
\]
while
\[
B=0,\qquad |W^+|^2=\frac1{24}.
\]
So no estimate of the form
\[
|\nabla z|^2+|u|^2|z|^2
\le C\bigl(1+|B|^2\bigr)
\]
can hold at the level of the reduced 1-jet equations.

The chiral Riccati formula
\[
W^+=-\left[\operatorname{Sym}\nabla a_+ +a_+\otimes a_+\right]_0
\]
controls only a trace-free symmetric Riccati tensor for \(a_+=u-\frac12z\). Its trace mode,
\[
\operatorname{tr}\left(\operatorname{Sym}\nabla a_+ +a_+\otimes a_+\right)
=
1+\frac34|z|^2-\frac32\langle u,z\rangle,
\]
can be large while the trace-free part remains calibrated. Therefore the chiral equation for \(W^+\) alone does not bind \(B\), \(|z|\), or \(|u||z|\). A genuinely coercive identity would have to include either the opposite chiral block \(W^-\), a trace-mode estimate, or a weighted Bochner formula for the full reduced system.

The sharp algebraic takeaway is:

\[
\boxed{
H\ge \frac14 I+B
}
\]
for exact calibrated \(W^+\). Thus \(B\) is the sole pointwise mechanism that can push an eigenvalue of \(H\) below zero, while \(z\)-amplitude can make \(H\) large upward without increasing \(W^+\) or \(B\).
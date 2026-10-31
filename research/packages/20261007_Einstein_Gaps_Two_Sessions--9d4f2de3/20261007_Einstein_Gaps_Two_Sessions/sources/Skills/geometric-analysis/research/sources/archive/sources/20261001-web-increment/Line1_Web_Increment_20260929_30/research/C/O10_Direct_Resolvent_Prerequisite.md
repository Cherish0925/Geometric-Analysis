# Direct bounded resolvent and derivative estimates

This appendix adopts and verifies the direct construction in the newly supplied O10 resolvent attachment. It is used as a proof simplification, not counted as a second new endpoint theorem.

## 2. Direct resolvent: complete energy estimate

Use normalized volume throughout. Let `t` be the actual cubic negative spinor, `L = nabla* nabla`, and `D` its twisted Dirac operator. The inherited endpoint conclusions are

\[
 \|Dt\|_2\to0,\qquad |t|^2\to m_* =128/81\text{ in }L^2,
 \qquad (L-2)t=D^*Dt+(\gamma-1)t-et,
\]

where `gamma` is uniformly bounded and converges to 1 in measure, while `e -> 0` in normalized `L2`. Thus `gamma-1 -> 0` in every finite normalized `Lp`, and `t` is bounded in normalized `L4`.

Choose a smooth radial bundle map `T` equal to the identity for `|t| <= 2` and bounded in norm by 4. Set `z=T(t)`. Since `m_*<4` and `|t|² -> m_*` strongly in `L2`,

\[
 \|z-t\|_2\to0.
\]

No derivative of this cutoff is required. Define

\[
 (4+L)u=6z.
\tag{2.1}
\]

The connection-Laplacian maximum principle gives

\[
 |u|\le6,\qquad |Lu|\le48.
\tag{2.2}
\]

Put `w=u-t` and `d=Dt`. Then

\[
 (4+L)w=6(z-t)-D^*d-(\gamma-1)t+et.
\]

Pairing with `w` gives

\[
 4\|w\|_2^2+\|\nabla w\|_2^2
 =6\langle z-t,w\rangle-\langle d,Dw\rangle
 -\langle(\gamma-1)t,w\rangle+\langle et,w\rangle.
\]

The first two terms are absorbed by Young's inequality, using `|Dw| <= 2|nabla w|`. The remaining two terms satisfy

\[
 |\langle(\gamma-1)t,w\rangle|
 \le\|\gamma-1\|_2\|t\|_4\|w\|_4=o(1),
\]

\[
 |\langle et,w\rangle|
 \le\|e\|_2\|t\|_4\|w\|_4=o(1).
\]

Here `||w||4 <= ||u||infinity + ||t||4` follows directly on the normalized probability space. It is not inferred from a Sobolev estimate. Therefore

\[
 \boxed{\|u-t\|_{H^1_{\rm av}}\to0.}
\tag{2.3}
\]

The same direct resolvent also supplies the residual needed in the stronger `39/4` argument:

\[
 \boxed{(L-2)u=6(z-u)\to0\text{ in }L^2_{\rm av},\qquad Du\to0\text{ in }L^2_{\rm av}.}
\tag{2.4}
\]

Thus all uses of the old bounded resolvent section remain valid after this substitution. In particular `|u|² -> m_*` in normalized `L2`, because `u` is bounded and converges in measure to the same amplitude as `t`.

## 3. Why the weighted Hessian estimate does not hide extra regularity

Write `P_i=nabla_i u`, `H_ij=nabla_i P_j`, `q=|P|²`, and `h=Lu`. The exact antisymmetry identity is

\[
 \int w|H|^2
 =\int w\operatorname{Re}\langle H_{ij},H_{ji}\rangle
 +\frac12\int w\sum_{i,j}|F_{ij}u|^2.
\]

In the first term, integrate the derivative with index `j`, then commute `nabla_j nabla_i P_j`. The contracted covector curvature is Ricci; the other curvature acts on the bundle slot. The only derivative of a traced quantity is `nabla h`. Integrating that term back once gives

\[
 \int w\operatorname{Re}\langle P,\nabla h\rangle
 =\int w|h|^2-\int\operatorname{Re}\langle dw\otimes P,h\rangle.
\]

No `nabla F`, `nabla Ric`, or estimate on `nabla h` is introduced. For

\[
 w=\left(\frac{q+\delta}{L_0^2+q+\delta}\right)^\epsilon,
 \qquad |dw|\sqrt q\le2\epsilon w|H|,
\]

the weight terms are absorbed for a fixed sufficiently small epsilon. The bounded-section interpolation from `div(wq Re<u,nabla u>)` gives

\[
 J=\int wq^2\le C_1\left(I+\int wq\right),
 \qquad I=\int w|H|^2.
\]

Split the bundle curvature at an arbitrary amplitude `T`. Its low part contributes `C_T int w(1+q)`. Young's inequality treats the tail-curvature times `q` term with a small multiple of `J`; choose that small coefficient after fixing `C1`. The coefficient multiplying the tail's squared norm is then independent of `T` and of the total curvature-energy bound. Consequently

\[
 \fint w(|H|^2+q^2)
 \le C_TL_0^{-2\epsilon}
 +C\fint_{|F|>T}|F|^2+C\fint|\operatorname{Ric}+g|^2.
\tag{3.1}
\]

The unweighted calculation first supplies the finite `L2` Hessian and `L4` gradient budgets. Their constants can depend on the total curvature-energy bound; this dependence is permitted in `C_T` and disappears when `L0 -> infinity` with `T` fixed.

For any sets `Z_j` of vanishing relative volume, let

\[
 \Gamma_F=\lim_{T\to\infty}\limsup_j\fint_{|F_j|>T}|F_j|^2.
\]

First take `j -> infinity`, then `L0 -> infinity`, then `T -> infinity` in (3.1). This proves

\[
 \limsup_j\fint_{Z_j}|\nabla u_j|^4\le C\Gamma_F.
\tag{3.2}
\]

This is a tail estimate, not an assertion that the Hessian squares are uniformly integrable on arbitrary small sets.

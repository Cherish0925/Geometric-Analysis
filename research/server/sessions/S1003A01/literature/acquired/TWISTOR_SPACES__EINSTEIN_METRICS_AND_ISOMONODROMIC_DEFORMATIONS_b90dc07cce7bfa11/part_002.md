---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: TWISTOR SPACES, EINSTEIN METRICS AND ISOMONODROMIC DEFORMATIONS]

$$P = M(\theta + \pi)^{-1}\phi(\theta + \pi)M(\theta + \pi) = -HM(\theta)^*\phi(\theta)^*M(\theta)^{*-1}H^{-1}$$

using (35). Hence

(40) $$P^* = -H^{*-1}PH^*.$$

As remarked above, the monodromy around this loop is defined by $H^*H^{-1}$. From (40), it commutes with $P$. Hence we may write

(41) $$H^*H^{-1} = c_1I + c_2P,$$

and so from (40)

$$H = H^{**} = H^*(\bar{c}_1I + \bar{c}_2P^*) = (\bar{c}_1I - \bar{c}_2P)H^* = (\bar{c}_1I - \bar{c}_2P)(c_1I + c_2P)H.$$

Now $P \in \mathfrak{g}$ so $\text{tr } P = 0$. Thus

$$P^2 = \frac{1}{2}(\text{tr } P^2)I = \frac{1}{2}(\text{tr }\phi^2)I = \frac{1}{2}RI$$

from the definition of $P$ and (39).

Hence,

$$(c_1\bar{c}_1 - \frac{1}{2}Rc_2\bar{c}_2) = 1 \quad \text{and} \quad c_1\bar{c}_2 = \bar{c}_1c_2.$$

Moreover since $\det(c_1I + c_2P) = 1$, we also have

$$c_1^2 - \frac{1}{2}Rc_2^2 = 1.$$

---

We deduce immediately that $c_1$ and $c_2$ are real and that $c_1^2 - \frac{1}{2} R c_2^2 = 1$. But the eigenvalues of the monodromy $c_1 I + c_2 P$ are $c_1 \pm c_2 \sqrt{R/2}$, thus if the scalar curvature $R$ is positive, the eigenvalues of this monodromy element are of the form $\lambda, \lambda^{-1}$ with $\lambda$ real, and if the curvature is negative, they are $\lambda, \lambda^{-1}$ with $\lambda \bar{\lambda} = 1$.

But now $\tau(x_1) = x_1$ so $\chi(\tau(x_1)) = \chi(x_1) = \lambda = \bar{\chi}(x_1)$ if $R$ is positive, and $\bar{\chi}(x_1)^{-1}$ if $R$ is negative.

To complete the proof of Theorem 5, suppose first that $R > 0$. Since $P$ is semisimple, the monodromy elements $\rho_i \rho_j$ commute with $P$ and are thus diagonalizable, so each $\rho_j$, being non-trivial in the normalizer of the corresponding diagonal subgroup, is of the form

$$\rho_j = \begin{pmatrix}
0 & a_j \\
-a_j^{-1} & 0
\end{pmatrix}$$

and

$$\rho_i \rho_j = \begin{pmatrix}
-a_i/a_j & 0 \\
0 & -a_j/a_i
\end{pmatrix}.$$

The real structure gives

$$\bar{\chi}(x_1) = \chi(\tau(x_1)) = \chi(x_1),$$

$$\bar{\chi}(x_2) = \chi(\tau(x_2)) = \chi(x_1)^2 \chi(x_2)^{-1},$$

using $\chi(y_i) = \rho_1^2 = -1$.

Thus

$$\frac{\bar{a}_1}{\bar{a}_2} = \frac{a_1}{a_2},$$

$$\frac{\bar{a}_1}{\bar{a}_3} = \frac{a_1^2 a_3}{a_2^2 a_1},$$

and so

$$\frac{a_1}{a_2} = \lambda^{-1} \quad \frac{a_1}{a_3} = \lambda^{-1} e^{i\theta}$$

for $\lambda \in \mathbf{R}$. By a change of basis we can set $a_4 = 1$, and the relation $\rho_1 \rho_2 \rho_3 \rho_4 = 1$ implies that $a_3 = a_2 a_1^{-1}$, which finally gives the full monodromy

$$a_1 = e^{i\theta}, \quad a_2 = \lambda e^{i\theta}, \quad a_3 = \lambda, \quad a_4 = 1.$$

---

The case of $R < 0$ is entirely similar.

It remains to deal with the case $R = 0$. Each generating monodromy element $\rho_j$ is of the form

$$\rho_j = \pm \begin{pmatrix} i & a_j \\ 0 & -i \end{pmatrix},$$

and so the monodromy preserves the subspace spanned by the first basis vector. This defines a line bundle $L$ on $\mathbf{CP}^1$ with a meromorphic connection whose residue at the point $z_j$ is $\pm 1/4$. The line bundle is a subbundle of the trivial bundle on which the connection $A$ is defined, and so must have non-positive degree. If it is trivial, then there is a vector $v \in \mathbf{C}^2$ which is an eigenvector for each residue $A_j$. But from the reality conditions (15) and (16), this implies that the $A_j$ are simultaneously diagonal, which (as in Lemma 1) is impossible, so $L$ must have negative degree. The degree is given by the sum of the residues of any connection, and so in this case is a number of the form $\pm \frac{1}{4} \pm \frac{1}{4} \pm \frac{1}{4} \pm \frac{1}{4}$, and we only obtain a negative integer, -1, by taking the negative sign at each pole. Hence

(42)

$$\rho_j = \begin{pmatrix} -i & a_j \\ 0 & i \end{pmatrix}$$

and

$$\rho_1\rho_2 = \begin{pmatrix} -1 & i(a_1 - a_2) \\ 0 & -1 \end{pmatrix}.$$

Thus $c_1 = -1$. From (41), we obtain

$$H + H^* = c_2PH.$$

Now choose a unitary basis of eigenvectors for $H + H^*$, then in this basis

$$H = \begin{pmatrix} a & b \\ -\bar{b} & d \end{pmatrix},$$

moreover, since $P$ is nilpotent and non-zero, one eigenvalue of $H + H^*$ is zero, and one non-zero, so $d + \bar{d} = 0$, say, and $a + \bar{a} \neq 0$. The condition det $H = 0$ then forces $d = 0$ and $b\bar{b} = 1$. From this we deduce that in this unitary basis,

$$c_2P = \begin{pmatrix} 0 & -b(a + \bar{a}) \\ 0 & 0. \end{pmatrix}.$$

---

But the first basis vector is the common $-i$ eigenspace for all the $\rho_j$ and so these have the form (42) with respect to a unitary basis.

Now using the reality conditions (32) and $H = \sigma$, we obtain

$$-\bar{a}_1 = 2ia\bar{b} + a_1 - a_2 + a_4,$$
$$-\bar{a}_2 = 2ia\bar{b} + a_1 - a_2 + a_3,$$
$$-\bar{a}_3 = 2ia\bar{b} + a_2 - a_3 + a_4,$$
$$-\bar{a}_4 = 2ia\bar{b} + a_1 - a_3 + a_4,$$

and from $\rho_1\rho_2\rho_3\rho_4 = 1$ we obtain $a_1 - a_2 + a_3 - a_4 = 0$.

Subtracting in pairs we find that $a_1 - a_2, a_2 - a_3, a_3 - a_4$ are imaginary. By a change of basis we can set $a_4 = 0$ and then $a_1, a_2, a_3$ are imaginary.

## 7. Elliptic curves and Einstein metrics

In this section, we shall adopt a geometrical approach to the monodromy for an Einstein metric, and thereby obtain explicit formulae. Our starting point is to consider the elliptic curve $C$ defined as the double covering of $\mathbf{CP}^1$ branched over the four singular points $\{z_1, z_2, z_3, z_4\}$ of the connection $A$. If the corresponding ramification points on $C$ are denoted by $\{w_1, w_2, w_3, w_4\}$, then

$$\pi_1(C \setminus \{w_1, w_2, w_3, w_4\}) \subset \pi_1(\mathbf{CP}^1 \setminus \{z_1, z_2, z_3, z_4\})$$

is a subgroup of index two. As is readily seen, it is in fact the subgroup of words of even length in the generators $\gamma_1, \gamma_2, \gamma_3$ of the free group $\pi_1(\mathbf{CP}^1 \setminus \{z_1, z_2, z_3, z_4\})$, so the covering $X$ of the previous section is simply $C \setminus \{w_1, w_2, w_3, w_4\}$. The key to obtaining explicit solutions is now Lemma 2, which says that the image of this subgroup in the monodromy group is abelian. Put another way, if we pull back the connection $A$ to $C$, then we obtain a connection with abelian holonomy, and we can then reduce the question of finding that monodromy to the calculation of periods of differentials on the curve $C$.

Let $\tilde{A}$ denote the connection $A$ pulled back to $C$. Since the residues of $A$ in the Einstein case have eigenvalues $\pm 1/4$, $\tilde{A}$ has poles at the points $w_i$ with residue conjugate to

$$\begin{pmatrix}
1/2 & 0 \\
0 & -1/2
\end{pmatrix},$$ because of the local branching $z - z_i = (w - w_i)^2 + \ldots$. It follows that a local covariant constant section has the form

(43)
$$s = (w - w_i)^{-1/2} \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \ldots \quad \text{or} \quad s = (w - w_i)^{1/2} \begin{pmatrix} a \\ b \end{pmatrix} + \ldots$$

First consider the case where the scalar curvature $R$ is non-zero. From Theorem 5, we see that the monodromy of the connection on $C$ preserves two 1-dimensional subspaces of $\mathbf{C}^2$, and so we obtain two line subbundles $L_1$ and $L_2$ of the trivial bundle over $C \setminus \{w_1, w_2, w_3, w_4\}$. Moreover, $\tilde{\Lambda}$ induces a connection on each of them. Consider a local covariant constant section $s$ of $L_1$ in a neighbourhood of $w = w_i$. From (43) we see that $L_1$ extends to $C$, and the induced connection extends to a connection with a pole of residue $\pm 1/2$.

Now the sum of the residues of a meromorphic connection on a line bundle $L$ is equal to $-\deg L$, so in our case this number is $\pm \frac{1}{2} \pm \frac{1}{2} \pm \frac{1}{2} \pm \frac{1}{2}$. On the other hand, $L_1$ is embedded as a holomorphic subbundle of $C \times \mathbf{C}^2$, and so its dual $L_1^*$ must have at least two linearly independent sections. This means, for an elliptic curve, that $\deg L_1 \leq -2$, and hence is equal to $-2 = -\frac{1}{2} - \frac{1}{2} - \frac{1}{2}$, so that the residues must all be $1/2$.

The same holds for $L_2$. Note that the involution on $C$ (the covering transformation of $C \rightarrow \mathbf{CP}^1$) interchanges $L_1$ and $L_2$, since the $\rho_i$, and hence all odd words, are non-trivial in the Weyl group $N(H)/H$ in the proof of Theorem 5. The subbundles $L_1$ and $L_2$ of $C \times \mathbf{C}^2$ coincide over the ramification points.

In a more analytical form, we represent the covering $C \rightarrow \mathbf{CP}^1$ as the meromorphic function on $C$ given by the Weierstrass $\wp$ function:

$$z = \wp(u),$$

where $u \in \mathbf{C}/\Lambda \cong C$, and $\Lambda$ is the lattice generated by $\{2\omega_1, 2\omega_3\}$. The involution on $C$ is $u \mapsto -u$, and its fixed points, the ramification points of the covering, are $u = 0, \omega_1, \omega_2, \omega_3$ (we shall use the notation in [33] for formulas involving elliptic functions). Since $\wp$ is of degree 2, any line bundle of degree 2 on $C$ is the pull back of $\mathcal{O}(1)$ by the meromorphic function $\wp(u-c)$ for some $c$. Thus we may take $L_1$ and

---

$L_2$ to be generated respectively by the two vectors in $C^2$:

(44) $v_1 = \begin{pmatrix} 1 \\ \wp(u - c) \end{pmatrix}$ and $v_2 = \begin{pmatrix} 1 \\ \wp(u + c) \end{pmatrix}$.

The connection $\tilde{A}$ preserves $L_1$, so there is a meromorphic 1-form $\theta_1 du$ on $C$ such that

(45) $\left(\frac{d}{du} + \wp'(u) A\right)\begin{pmatrix} 1 \\ \wp(u - c) \end{pmatrix} = \theta_1 \begin{pmatrix} 1 \\ \wp(u - c) \end{pmatrix}$.

Now $\theta_1 du$ is a connection form relative to the local trivialization $v_1$ of $L_1$. The meromorphic section $v_1$ has a double pole where $\wp(u - c) = \infty$, i.e., at $u = c$. As we have seen, the connection has simple poles at the ramification points with residue 1/2, so $\theta_1$ is an elliptic function with simple poles of residue 1/2 at $u = 0, \omega_1, \omega_2, \omega_3$ and a simple pole with residue $-2$ at $u = c$. Now

$$\frac{\wp''(u)}{2\wp'(u)}$$

has simple poles of residue 1/2 at $u = \omega_1, \omega_2, \omega_3$ and a simple pole of residue $-3/2$ at $u = 0$. Moreover,

$$\frac{2\wp'(c/2)}{\wp(u - c/2) - \wp(c/2)}$$

has a simple pole of residue 2 at $u = c$ and residue $-2$ at $u = 0$. Thus there is a constant $\kappa$ such that

(46) $\theta_1 = \frac{\wp''(u)}{2\wp'(u)} - \frac{2\wp'(c/2)}{\wp(u - c/2) - \wp(c/2)} + \kappa$.

The constants $\kappa$ and $c$ need to be determined from the monodromy of $A$. For a line bundle, however, the monodromy of a connection is easily obtained by integrating the connection form over closed loops, or their homology classes:

$$\rho(\gamma) = -\exp\left(\int_\gamma \theta_1 du\right).$$

Now consider the map on homology induced by the inclusion

$$
i : H_1(C \setminus \{w_1, w_2, w_3, w_4\}, Z) \rightarrow H_1(C, Z).
$$

---

The classes $y_i = \gamma_i^2$ bound in $C$, so $H_1(C, Z) \cong Z^2$ is generated by $i(x_1), i(x_2)$. Moreover, since from (38) $\tau(x_1) = x_1$ and $\tau(x_2) = 2x_1 - x_2 - y_1 - y_2$, $i(x_1)$ is a real generator and $i(x_1 - x_2)$ an imaginary one. Thus the periods of $\theta_1 du$ over these cycles are determined by the monodromy elements $\rho_1\rho_2$ and $\rho_3\rho_2$ of the connection on $CP^1$. In the fundamental rectangle, the cycles are represented by lines parallel to the $x$ and $y$ axes respectively.

To calculate the periods, we first use the general formula for the Weierstrass zeta function

(47) $$\zeta(u + a) - \zeta(u - a) - 2\zeta(a) = \frac{-\wp'(a)}{\wp(u) - \wp(a)}$$

and the definition of the sigma function

$$\zeta(u) = \frac{\sigma'(u)}{\sigma(u)}$$

to obtain

$$\int \frac{\wp'(a)}{\wp(u) - \wp(a)} du = -\log \frac{\sigma(u + a)}{\sigma(u - a)} + 2\zeta(a) u$$

and hence

$$\int \theta_1 du = \frac{1}{2} \log \wp'(u) + 2 \log \frac{\sigma(u)}{\sigma(u - c)} - 4\zeta(c/2) u + \kappa u.$$

Finally, using

$$\sigma(u + 2\omega_1) = -e^{2\eta_1(u + \omega_1)} \sigma(u),$$

$$\sigma(u + 2\omega_3) = -e^{2\eta_3(u + \omega_1)} \sigma(u),$$

where $\eta_i = \zeta(\omega_i)$, we obtain the monodromy $e^{\lambda_1}, e^{\lambda_3}$ of $\theta_1$ where:

$$\lambda_1 = 4\eta_1c - 8\omega_1\zeta(c/2) + 2\kappa\omega_1,$$

$$\lambda_3 = 4\eta_3c - 8\omega_3\zeta(c/2) + 2\kappa\omega_3.$$

From the Legendre relation $\eta_1\omega_3 - \eta_3\omega_1 = i\pi/2$, we find

(48) $$\lambda_1\omega_3 - \lambda_3\omega_1 = 2\pi ic,$$

(49) $$\lambda_1\eta_3 - \lambda_3\eta_1 = 4\pi i\zeta(c/2) - i\pi\kappa.$$

---

Each twistor line has a connection with the same monodromy, so $\lambda_1$ and $\lambda_3$ are fixed by the metric. Note that the ambiguity in the choice of logarithm is reflected in the two choices of lifting of the cycles $\gamma_1\gamma_2$ and $\gamma_3\gamma_2$. The equations (48) and (49) then define $c$ and $\kappa$, and hence the connection form $\theta_1$, in terms of the basic invariants $\omega_i,\eta_i$ of the elliptic curve. It will be more convenient to replace the parameters $c$ and $\kappa$ by $\omega$ and $\eta$ defined by:

$$\omega = 2c, \quad \text{and} \quad \eta = 4\zeta(c/2) - \kappa$$

thus giving

$$\lambda_1 = 2\omega\eta_1 - 2\eta\omega_1,$$
$$\lambda_3 = 2\omega\eta_3 - 2\eta\omega_3.$$

Note that, from Theorem 5, $\lambda_1$ is imaginary and $\lambda_3$ real for a metric with scalar curvature $R < 0$, and vice versa for $R > 0$.

To derive the full connection, we can use (47) and (49) to rewrite (46) as

$$\theta_1 = (\zeta(2u) - 2\zeta(u)) + 2(\zeta(u) - \zeta(u-c) - 2\zeta(c/2)) + \kappa$$
$$= \zeta(2u) - 2\zeta(u-c) - \eta,$$

and, since $\theta_2$ is obtained by replacing $c$ by $-c$, and taking the opposite period, we have

$$\theta_2 = \zeta(2u) - 2\zeta(u+c) + \eta.$$

These expressions, together with (45) provide a formula for the connection matrix $A$:

$$\rho'(u)(\wp(u+c) - \wp(u-c))A$$
$$= \begin{pmatrix}
\theta_1 & \theta_2 \\
\theta_1\rho(u-c) - \rho'(u-c) & \theta_2\rho(u+c) - \rho'(u+c)
\end{pmatrix}\begin{pmatrix}
\wp(u+c) & -1 \\
-\wp(u-c) & 1
\end{pmatrix}.$$

In practice, this is very cumbersome to use, so we shall make use of a different approach to the isomonodromic deformation problem, which involves just a single function. A reference for this is [20].

First note that if, in the general context of isomonodromic deformations, the connection on CP¹ is put in the form

$$A(z) = \frac{A_1}{z} + \frac{A_2}{z-1} + \frac{A_3}{z-x},$$ then each entry of the matrix $A_{ij}(z)$ is of the form $q(z)/[z(z-1)(z-x)]$ for some quadratic polynomial $q$. Now if, as in our case, $A_{\infty} = -(A_1 + A_2 + A_3)$ is diagonalizable, then there is a basis such that

$$A_{\infty} = \begin{pmatrix} \lambda & 0 \\ 0 & -\lambda \end{pmatrix},$$

and $A_{12}$ can be written

$$A_{12}(z) = \frac{k(z-y)}{z(z-1)(z-x)}$$

for some $y \in \mathbf{CP}^1 \setminus \{0,1,x,\infty\}$. If the $A_i(x)$ satisfy Schlesinger's equation (10), then the function $y(x)$ satisfies the Painlevé equation

$$\frac{d^2y}{dx^2} = \frac{1}{2}\left(\frac{1}{y} + \frac{1}{y-1} + \frac{1}{y-x}\right)\left(\frac{dy}{dx}\right)^2$$

(52)

$$-\left(\frac{1}{x} + \frac{1}{x-1} + \frac{1}{y-x}\right)\frac{dy}{dx}$$

$$+ \frac{y(y-1)(y-x)}{x^2(x-1)^2}\left(\alpha + \beta \frac{x}{y^2} + \gamma \frac{x-1}{(y-1)^2} + \delta \frac{x(x-1)}{(y-x)^2}\right),$$

where

$$\alpha = (2\lambda-1)^2/2,$$

$$\beta = 2\det A_1^2,$$

(53)

$$\gamma = -2\det A_2^2,$$

$$\delta = (1+4\det A_3^2)/2.$$

For our purposes it is useful to note the geometrical form of the definition of $y(x)$ given by (52): the solution $y(x)$ to the Painlevé equation corresponding to an isomonodromic deformation $A(z)$ is the point $y \in \mathbf{CP}^1 \setminus \{0,1,x,\infty\}$ at which $A(y)$ and $A_{\infty}$ have a common eigenvector, corresponding to the eigenvalue $\lambda$ at $\infty$.

Now in our example, $z = \wp(u) = \infty$ if $u=0$, and from (45) we see that the vector

$$v = \begin{pmatrix} 1 \\ \wp(c) \end{pmatrix}$$ is an eigenvector of $A_{\infty}$. Moreover, since, as noted in the course of its calculation, $\theta_1$ has a simple pole at $u = 0$ with residue $+1/2$, the corresponding eigenvalue of $A$ on CP$^1$ is $+1/4$. Thus the values of the coefficients in the Painlevé equation (52) are $\alpha = 1/8$, $\beta = -1/8$, $\gamma = 1/8$ and $\delta = 3/8$.

To obtain $y(x)$, we must find the value of $\wp(u)$ at which $v$ is again an eigenvalue of $A$. Equivalently, we want

$$\det \left( A \begin{pmatrix} 1 \\ \wp(c) \end{pmatrix} \begin{pmatrix} 1 \\ \wp(c) \end{pmatrix} \right) = 0.$$

The formula (52), after some manipulation, then gives the condition:

$$\theta_1 - \theta_2 = \frac{\wp'(u-c)}{\wp(u-c) - \wp(c)} - \frac{\wp'(u+c)}{\wp(u+c) - \wp(c)}.$$

Using (47) and the expressions for $\theta_1$ and $\theta_2$, this yields:

$$2\zeta(u+c) - 2\zeta(u-c) - 2\mu$$
$$= \zeta(u) + \zeta(u-2c) - 2\zeta(u-c) - (\zeta(u+2c) + \zeta(u) - 2\zeta(u+c)),$$

from which

$$-2\eta = \zeta(u-2c) - \zeta(u+2c) = -2\zeta(2c) + \frac{\wp'(2c)}{\wp(u) - \wp(2c)}.$$

Solving for $\wp(u)$, setting $\omega = 2c$ and using the Möbius transformation which takes the branch points $e_1, e_2, e_3$ to $0, 1, x$, we obtain the solution to the Painlevé equation as

(54)

$$y(x) = \frac{\xi-e_1}{e_2-e_1},$$

where

$$\xi = \wp(\omega) + \frac{\wp'(\omega)}{2(\zeta(\omega)-\eta)},$$

$$x = \frac{e_3-e_1}{e_2-e_1},$$

and

$$\omega = k_1\omega_3 - k_3\omega_1,$$

$$\eta = k_1\eta_3 - k_3\eta_1,$$

for constants $k_1, k_3$.

---

Remark. In the above form, it is not entirely clear that $y$ is a function of $x$ alone. If we express the Weierstrass elliptic functions in terms of theta functions $\vartheta_{\alpha}(\nu,\tau)$, then $y(x)$ is also defined as

$$y(x) = \frac{\vartheta_{1}^{\prime\prime}(0)}{3\pi^{2}\vartheta_{4}^{4}(0)\vartheta_{1}'(0)} + \frac{1}{3} \left( 1 + \frac{\vartheta_{3}^{4}(0)}{\vartheta_{4}^{4}(0)} \right) + \frac{\vartheta_{1}^{\prime\prime}(\nu)\vartheta_{1}(\nu) - 2\vartheta_{1}^{\prime}(\nu)\vartheta_{1}'(\nu) + 2\pi ik_{1}(\vartheta_{1}^{\prime}(\nu)\vartheta(\nu) - \vartheta_{1}^{\prime 2}(\nu))}{2\pi^{2}\vartheta_{4}^{4}(0)\vartheta_{1}(\nu)(\vartheta_{1}'(\nu) + \pi ik_{1}\vartheta_{1}(\nu))},$$

where $\nu = (k_{1}\tau - k_{3})/2$ and $x = \vartheta_{3}^{4}(0)/\vartheta_{4}^{4}(0)$. The above is the function which we shall use in the next sections to generate new solutions of the Einstein equations. Before doing that, however, we should for completeness consider the case $R = 0$, although the corresponding equations were solved already in the context of elliptic integrals in [4] and [5]. The advantage of our current viewpoint is the wider context in which the formula appears.

Consider then the case of $R = 0$. Here, from Theorem 5, the monodromy preserves a subbundle $L$ of $\mathbf{CP}^{1} \times \mathbf{C}^{2}$. From the proof of the theorem, $L$ has degree $-1$ and so $L \cong \mathcal{O}(-1)$. We can therefore take $L$ to be spanned by the vector

$$\begin{pmatrix} 1 \\ z \end{pmatrix}.$$

Now the connection preserves $L$ and so

$$\nabla \begin{pmatrix} 1 \\ z \end{pmatrix} = \theta \begin{pmatrix} 1 \\ z \end{pmatrix}.$$

Again from the proof of the theorem, the meromorphic 1-form $\theta$ has simple poles, and residues 1/4 over the finite branch points $e_{1}, e_{2}, e_{3}$. Thus

$$\theta = \frac{dz}{4(z-e_{1})} + \frac{dz}{4(z-e_{2})} + \frac{dz}{4(z-e_{3})}.$$

If we now set

$$f(z) = (z-e_{1})(z-e_{2})(z-e_{3})$$

and

$$s_{1} = f^{-1/4} \begin{pmatrix} 1 \\ z \end{pmatrix},$$ then

$$\nabla s_1 = 0.$$

Now put

$$s_2 = f^{1/4} \begin{pmatrix} z^{-1} \\ 0 \end{pmatrix},$$

then $$\nabla s_2 = as_1 + bs_2,$$ but since $< s_1, s_2 > = -1$ with respect to the skew pairing on $\mathbf{C}^2$, preserved by the $SL(2,\mathbf{C})$ connection $A$, we have

$$0 = d < s_1, s_2 > = < \nabla s_1, s_2 > + < s_1, \nabla s_2 > = b,$$

and so $$\nabla s_2 = as_1.$$

Thus the connection matrix $A$ is given by

$$\left( \frac{d}{dz} + A \right) \begin{pmatrix} f^{-1/4} & f^{1/4}z^{-1} \\ f^{-1/4}z & 0 \end{pmatrix} = \begin{pmatrix} 0 & f^{-1/4}a \\ 0 & f^{-1/4}az \end{pmatrix}.$$

Hence,

(55) $$A = \begin{pmatrix} -f'/4f + 1/z + f^{-1/2}az & f'/2fz - 1/z^2 - f^{-1/2}a \\ -f^{-1/2}az^2 & f'/4f - 1/z - f^{-1/2}az \end{pmatrix}.$$

Each entry in this matrix $A(z)$ must be of the form $q(z)/f$ for some quadratic polynomial $q(z)$. Taking account of the powers of $z$ in the denominator, we obtain

(56) $$a = f^{-1/2} \left( \frac{f'}{2z} - \frac{f}{z^2} - \frac{z}{2} + c \right) dz$$

(57) $$= d(f'/z) + f^{-1/2}(c - z/2)dz$$

for some constant $c$, to be determined from the monodromy.

To make this relationship, note that $f^{1/2} = \sqrt{(z-e_1)(z-e_2)(z-e_3)}$ is single valued on the elliptic curve $C$; in fact setting $z = \wp(u)$, then $\wp'(u) = 2f^{1/2}$. Thus the section $s_1 \otimes s_1$ (considered as a nilpotent element in the Lie algebra $\mathfrak{g}$ of $SL(2,\mathbf{C})$) is single valued and covariant constant. Moreover,

$$\nabla(s_1 \otimes s_2) = a(s_1 \otimes s_1),$$

so the two-dimensional subspace of $\mathfrak{g}$ spanned by $s_1 \otimes s_4$ and $s_1 \otimes s_2$ is preserved by the connection. We already know the monodromy is abelian but from this point of view, around a cycle $x$ it is given by a matrix conjugate to

$$\begin{pmatrix} 1 & \alpha \\ 0 & 1 \end{pmatrix}$$ where $\alpha = \int_x a.$

Using (57) we have

$$a = d(f'/z) + (2c - \wp(u))du,$$

and so the periods of this form over the real and imaginary cycles of $C$ are

(58) $$\lambda_1 = 4c\omega_1 + 2\eta_1,$$

(59) $$\lambda_3 = 4c\omega_3 + 2\eta_3.$$

Now replacing the nilpotent element $s_1 \otimes s_1$ by a multiple of itself gives another basis of the same type, so only the ratio $\lambda_1/\lambda_3$ is an invariant of the monodromy. We can now compare with the form of the monodromy in Theorem 5. Here the monodromy around the two cycles is given by

$$\begin{pmatrix} -1 & \mu - \lambda \\ 0 & -1 \end{pmatrix}$$ and $$\begin{pmatrix} -1 & \lambda \\ 0 & -1 \end{pmatrix},$$

and so $\lambda_1/\lambda_3 = (\mu - \lambda)/\lambda$ and is in particular a real number $k_0$. Using the Legendre relation from (59) we obtain

(60) $$c = \frac{-(k_0\eta_3 - \eta_1)}{2(k_0\omega_3 - \omega_1)}.$$

We need to find the corresponding solution to the Painlevé equation, and for this consider (55) as $z \to \infty$. It is easy to see, using (57), that the residue of $A$ at infinity has the eigenvector

$$\begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

corresponding to the eigenvalue 1/4, and so the solution to the Painlevé equation is the point $z = y$ at which this vector is again an eigenvector.

---

From (55) this is where $f'/2fz - 1/z^2 - f^{-1/2}a = 0$, or from (57) where $z = 2c$. By (60), we therefore obtain

(61) $$y(x) = \frac{\xi - e_1}{e_2 - e_1},$$

where

$$\xi = \frac{-(k\eta_3 - \eta_1)}{(k\omega_3 - \omega_1)}.$$

We may summarize our calculations in the following theorem:

Theorem 6. Let $M$ be an SU(2)-invariant anti-self-dual Einstein manifold with scalar curvature $R$ and such that its twistor space $Z$ has $\Lambda^3\alpha$ non-degenerate. Then the corresponding solution $y(x)$ to the Painlevé equation is given as follows:

• For $R < 0,$

$$y(x) = \frac{\xi - e_1}{e_2 - e_1},$$

where

$$\xi = \wp(\omega) + \frac{\wp'(\omega)}{2(\zeta(\omega) - \eta)} \quad \text{and} \quad x = \frac{e_3 - e_1}{e_2 - e_1},$$

and

$$\omega = k_1\omega_3 - ik_3\omega_1,$$

$$\eta = k_1\eta_3 - ik_3\eta_1$$

for constants $k_1, k_3 \in R$.

• For $R = 0,$

$$y(x) = \frac{\xi - e_1}{e_2 - e_1},$$

where

$$\xi = \frac{-(k_0\eta_3 - \eta_1)}{(k_0\omega_3 - \omega_1)},$$

and $k_0 \in R$.

• For $R > 0,$

$$y(x) = \frac{\xi - e_1}{e_2 - e_1},$$ where

$$\xi = \wp(\omega) + \frac{\wp'(\omega)}{2(\zeta(\omega) - \eta)} \quad and \quad x = \frac{e_3 - e_1}{e_2 - e_1},$$

and

$$\omega = ik_1\omega_3 - k_3\omega_1,$$
$$\eta = ik_1\eta_3 - k_3\eta_1$$

for constants $k_1, k_3 \in R$.

Remarks.

1. In [19], some algebraic Einstein metrics with $R > 0$ were produced directly from the twistor construction, by using a relationship with Poncelet polygons. The connection with the Painlevé equation and isomonodromic deformations was central in that description, but the essential fact giving algebraic solutions was that the monodromy group was finite, in fact a binary dihedral group. In our discussion here, we have seen that the monodromy group for an Einstein metric has the basic property that it has an abelian subgroup of index two. Of course this is true in particular for the covering of the rotations in the binary dihedral group. The values of the constants $k_1, k_3$ in Theorem 6 relating to monodromy given by the dihedral group of symmetries of a regular $k$-gon are $k_3 = 2/k$ and $k_1 = 0$.

2. A possible interpretation of the algebraic metrics in [19] was given there in terms of the moduli space of charge 2 monopoles on a hyperbolic space of curvature $-1/p^2$ where $p+1 = 1/(2k_3)$. The algebraicity of these metrics when $2/k_3 \in Z$ is consistent with the fact that the corresponding solutions of the Bogomolny equations are algebraic. However, solutions exist for all values of the curvature, and so one expects appropriate metrics for all values of $k_3$. This is what the above formula yields. In fact, the asymptotic analysis of [19] giving the global structure of the metric is independent of whether $k$ is an integer or not.

3. The natural metric on the moduli space of Euclidean charge 2 monopoles is hyperkähler and was calculated in [4]. The solution to the Painlevé equation which corresponds to it was derived as a limiting procedure of the dihedral metrics as $k \to \infty$ in [19]. By comparison with Theorem 6, it corresponds to the value of the constant $k_0 = 0$. We leave it as an exercise to relate the general solution of the $SU(2)$- invariant hyperkähler metrics as discussed in [4] and [5] to the general solution of the corresponding Painlevé equation above.

## 8. Einstein metrics on the 4-ball

We shall now use the explicit formulae of the previous section to produce a family of complete anti-self-dual Einstein metrics with negative scalar curvature on the interior of the unit ball. There are two basic models for such metrics. The first is the hyperbolic metric on the unit ball

$$g = \frac{1}{(1-r^2)^2}(dx_1^2 + dx_2^2 + dx_3^2 + dx_4^2).$$

It is the symmetric space $SO(4,1)/SO(4)$ with its natural metric. Away from the origin, this special metric is defined on $(0,1) \times S^3$ and as such can be written in the form

$$g = \frac{dr^2}{(1-r^2)^2} + \frac{r^2}{(1-r^2)^2}(\sigma_1^2 + \sigma_2^2 + \sigma_3^2).$$

The conformal structure extends over the boundary and induces the standard conformal structure on the sphere $r=1$.

The second model is the Bergmann metric on the unit ball in $\mathbf{C}^2$. This is the symmetric space $SU(2,1)/U(2)$ and is the metric dual to the Fubini-Study metric on $\mathbf{CP}^2$. In diagonal form it can be given by

$$g = \frac{1}{2}\left(\frac{dr^2}{(1-r^2)^2} + \frac{r^2\sigma_2^2}{(1-r^2)^2} + \frac{r^2}{(1-r^2)}(\sigma_1^2 + \sigma_3^2)\right).$$

In this case the conformal structure does not extend across the boundary. Asymptotically, by putting $s=1-r$ and letting $s \to 0$, the metric is a multiple of

$$g = \frac{ds^2}{s^2} + \frac{1}{2s}\sigma_1^2 + \frac{1}{4s^2}\sigma_2^2 + \frac{1}{2s}\sigma_3^2 + \dots.$$

The conformal structure on an $SU(2)$ orbit degenerates: the coefficient of $\sigma_2^2$ decays faster than the others, and what is left is a conformal structure on the two-dimensional subbundle of the tangent bundle of $S^3$ annihilated by $\sigma_2$. This is a left-invariant CR-structure, whose existence is a natural consequence of the fact that the Bergmann metric is a Kähler metric respecting a complex structure which extends to the boundary.

We begin with the first model. Its essential features for our purposes are that it is invariant under $SO(4)$ and blows up on the 3-sphere $r = 1$, although the conformal structure extends smoothly across the sphere. In the terminology of [22], the sphere is the conformal infinity of the Einstein metric. The metrics we shall define will be invariant under $SU(2) \subset SO(4)$, and induce on their conformal infinity a left-invariant conformal structure on the 3-sphere $S^3 \cong SU(2)$.

The existence of such a metric in a collar neighbourhood of $S^3$ follows from a rather general twistorial result of LeBrun [22], and was the motivation for Pedersen's work [29], which succeeded in finding explicitly the metrics which are invariant under $U(2) \subset SO(4)$. Pedersen's metrics extend to the whole of the ball and the more general question of whether an arbitrary left invariant metric extends is the theme of Tod's paper [34]. From the work of Graham and Lee [15], (see the discussion in [25]), it is known that a metric sufficiently close to the bi-invariant metric will extend to a possibly non-anti-self-dual Einstein metric.

Our point of view is to select from our explicit solutions for $SU(2)$-invariant anti-self-dual Einstein metrics the ones with negative scalar curvature, and to investigate the global behaviour of the metric as the parameter $x$ in (24) lies within a suitable interval. So far, we have only considered the conformal structure, for that is all the general twistor space gives us. In the anti-self-dual Einstein case it is the twisted form $\theta$ on the twistor space which defines the metric (see [8]) within the conformal structure, but there is a more direct expression given by Tod ([34]). With the conformal structure given by

$$g_0 = \frac{dx^2}{x(1-x)} + \frac{\sigma_1^2}{\Omega_1^2} + \frac{(1-x)\sigma_2^2}{\Omega_2^2} + \frac{x\sigma_3^2}{\Omega_3^2}$$

as in (24), the conformal factor to give an Einstein metric $g = e^{2u}g_0$ with scalar curvature $\Lambda$ is

$$-4\Lambda e^{2u} = \frac{(8x\Omega_1^2\Omega_2^2\Omega_3^2 + 2\Omega_1\Omega_2\Omega_3(x(\Omega_1^2 + \Omega_2^2) - (1-4\Omega_3^2)(\Omega_2^2 - (1-x)\Omega_1^2)))}{(x\Omega_1\Omega_2 + 2\Omega_3(\Omega_2^2 - (1-x)\Omega_1^2))^2}$$

---

As we saw in Section 5, the $\Omega_i$ are derived from the residues of the connection matrix $A$, which in turn, from [20] is determined from the solution to the Painlevé equation. Explicitly, in the Einstein case, we have

(66) $$\frac{dy}{dx} = \frac{y(y-1)(y-x)}{x(x-1)} \left(2z - \frac{1}{2y} - \frac{1}{2(y-1)} + \frac{1}{2(y-x)}\right),$$

which defines the auxiliary variable $z$, and then

$$\Omega_1^2 = \frac{(y-x)^2 y(y-1)}{x(1-x)} \left(z - \frac{1}{2(y-1)}\right) \left(z - \frac{1}{2y}\right),$$

(67) $$\Omega_2^2 = \frac{y^2(y-1)(y-x)}{x} \left(z - \frac{1}{2(y-x)}\right) \left(z - \frac{1}{2(y-1)}\right),$$

$$\Omega_3^2 = \frac{(y-1)^2 y(y-x)}{(1-x)} \left(z - \frac{1}{2y}\right) \left(z - \frac{1}{2(y-x)}\right).$$

We shall take a solution to the Painlevé equation giving negative scalar curvature. From Theorem 6 this is

$$y(x) = \frac{\xi-e_1}{e_2-e_1},$$

where

(68) $$\xi = \wp(\omega) + \frac{\wp'(\omega)}{2(\zeta(\omega)-\eta)} \quad \text{and} \quad x = \frac{e_3-e_1}{e_2-e_1},$$

and

$$\omega = k_1 \omega_3 - ik_3 \omega_1$$

$$\eta = k_1 \eta_3 - ik_3 \eta_1$$

for constants $k_1, k_3 \in \mathbf{R}$. Note that the real structure implies that $x$ is real and $\omega, \eta$ imaginary.

First consider the conformal structure. This is non-degenerate for $x \neq 0, 1, \infty$ so long as the $\Omega_i$ are finite and non-vanishing. From the Painlevé property of $y(x)$, the only branch points or essential singularities are at $x = 0, 1, \infty$, so $y(x)$ is meromorphic outside these values of $x$. If $y \neq 0, 1, x, \infty$, then from (67), $\Omega_i$ is finite. By considering the (holomorphic) linear factors in $z$ in these formulae, if the $\Omega_i$ vanish at all, they vanish in pairs. But the $\Omega_i$ satisfy the first order differential equation (27). If $\Omega_1 = \Omega_2 = 0$ at some point, then $\Omega_1 \equiv 0, \Omega_2 \equiv 0, \Omega_3 \equiv const$. is the unique solution with this initial value. This is a constant solution, which is clearly not the case here.

In Propositions 8-13, we establish some basic properties of the function $y(x)$ which provide the tools for determining the global behaviour of these metrics. These properties are concerned with the behaviour of $y(x)$ at the special values $0, 1, x, \infty$.

**Proposition 8.** Let $y(x)$ be a solution to the Painlevé equation (52), and suppose that $y$ has a singularity at $x = x_0$ where $x_0 \neq 0, 1, \infty$. Then

- $y(x)$ has a simple pole of the form

$$y(x) = \pm \frac{2x_0(x_0 - 1)}{(x - x_0)} = \dots.$$

- If the residue is $2x_0(x_0 - 1)$, then the conformal structure (24) extends from the punctured ball $B^4 \backslash 0 \cong S^3 \times (x_0, x_0 + \epsilon)$ to the whole ball $B^4$.

- If the residue is $-2x_0(x_0 - 1)$, then the conformal structure extends from $S^3 \times (x_0, x_0 + \epsilon)$ to $S^3 \times (x_0 - \epsilon, x_0 + \epsilon)$.

**Proof.** Since $y(x)$ is meromorphic at $x = x_0$, the first part of the proposition follows by substitution of the Laurent polynomial in the Painlevé equation, and equating coefficients.

If the residue is $2x_0(x_0 - 1)$, then by substituting in (66), we obtain

$$z = (x - x_0)^2 + \dots,$$

from which, in (67),

$$\Omega_1^2 = -x_0(x_0 - 1)/(x - x_0)^2 + \dots,$$

$$\Omega_2^2 = x_0(x_0 - 1)^2/(x - x_0)^2 + \dots,$$

$$\Omega_3^2 = -x_0^2(x_0 - 1)/(x - x_0)^2 + \dots,$$

and then the conformal structure is given by

$$g_0 = \frac{dx^2}{x_0(1 - x_0)} - \frac{(x - x_0)^2\sigma_1^2}{x_0(x_0 - 1)} - \frac{(x - x_0)^2\sigma_2^2}{x_0(x_0 - 1)} - \frac{(x - x_0)^2\sigma_3^2}{x_0(x_0 - 1)} + \dots,$$

which, comparing with the hyperbolic metric (62) at $r = 0$, clearly extends over the puncture. Note also that if $x_0 > 1$, the conformal structure is negative definite.

---

If the residue is $-2x_0(x_0 - 1)$, then

$$z = \frac{-(x-x_0)}{2x_0(x_0 - 1)} + \ldots,$$

and therefore

$$z - \frac{1}{2y} = -\frac{(x-x_0)}{2x_0(x_0 - 1)} + \frac{(x-x_0)}{2x_0(x_0 - 1)} + \ldots.$$

thus it follows by substituting in (67), that the $\Omega_i^2$ are regular at $x = x_0$. In fact, they are non-vanishing too, for if

$$z - \frac{1}{2y} = c(x-x_0)^n + \ldots$$

with $n > 2$, we obtain

$$\Omega_1^2 = A(x-x_0)^{n-2} + \ldots,$$

$$\Omega_2^2 = 1/4 + \ldots,$$

$$\Omega_3^2 = A(x-x_0)^{n-2} + \ldots,$$

which contradicts the fact (27) that $\Omega'_1 = -\Omega_2\Omega_3/x(1-x)$. Hence the conformal structure is non-singular.

We need to consider the two possibilities for our particular solution. Here $y(x)$ has a pole if

$$\xi = \wp(\omega) + \frac{\wp'(\omega)}{2(\zeta(\omega) - \eta)}$$

is infinite, and this holds if and only if $\omega = 2n\omega_3$, for some integer $n$, or $\zeta(\omega) = \eta$.

Proposition 9. Let $y(x)$ be the solution to the Painlevé equation given by (68). If $\zeta(\omega) = \eta$, then the residue is $-2x_0(x_0 - 1)$, and if $\omega = 2n\omega_3$ at $x = x_0$, then the residue of $y(x)$ is $2x_0(x_0 - 1)$.

Proof. It is sufficient to consider $\xi$ near $\omega = k_1\omega_3 - ik_3\omega_1 = 0$ so that $\tau = \omega_3/\omega_1 = ik_3/k_1$.

By using the standard expansion of Weierstrass elliptic functions, coming from

$$\zeta(u) = \frac{1}{u} - \frac{g_2u^3}{60} + \ldots$$ and its derivatives, we obtain $\xi = -\eta(x_0)/\omega + \dots$. But

$$\eta(x_0) = k_1\eta_3 - ik_3\eta_1 = k_1(\eta_3 - \tau\eta_1) = -k_1\pi i/2\omega_1$$

using the Legendre relation, so

$$\xi = \frac{\pi i}{2\omega_1^2(\tau - ik_3/k_1)} + \dots.$$

We need to relate the parameter $\tau$ in the upper half-plane to the cross ratio $x$. For this we use

$$x(\tau) = \frac{e_3 - e_1}{e_2 - e_1} = \frac{\vartheta_3^4(0)}{\vartheta_4^4(0)}.$$

Differentiating with respect to $\tau$ and using the heat equation

$$\vartheta_1'' = 4\pi i \frac{\partial}{\partial\tau}\vartheta_1$$

satisfied by theta functions, we find

$$\frac{dx}{d\tau} = \frac{x}{\pi i} \left[ \frac{\vartheta_3''(0)}{\vartheta_3(0)} - \frac{\vartheta_4''(0)}{\vartheta_4(0)} \right],$$

and from the relation

$$2\eta_1\omega_1 = -2e_\alpha\omega_1^2 - \frac{1}{2}\frac{\vartheta_{\alpha+1}'(0)}{\vartheta_{\alpha+1}(0)}$$

we obtain

(69)

$$\frac{dx}{d\tau} = \frac{1}{i\pi} 4x\omega_1^2(e_3 - e_2).$$

Thus

$$\xi = \frac{2x_0(e_3 - e_2)}{(x - x_0)} + \dots$$

giving

$$y(x) = \frac{2x_0(x_0 - 1)}{(x - x_0)} + \dots.$$

For the second case, using the theta function $\vartheta_1(\nu,\tau)$, we have the standard relation

(70)

$$\zeta(u) - \frac{\eta_1u}{\omega_1} = \frac{1}{2\omega_1} \frac{\vartheta_1'(\nu)}{\vartheta_1(\nu)},$$ where $v = u/2\omega_1$, $\tau = \omega_3/\omega_1$. Using the definitions $\omega = k_1\omega_3 - ik_3\omega_1$, $\eta = k_1\eta_3 - ik_3\eta_1$ and the Legendre relation, we can then write

(71) $$\zeta(\omega) - \eta = \frac{1}{2\omega_1} \left( \frac{\vartheta'_1}{\vartheta_1} (k_1\tau/2 - ik_3/2,\tau) + ik_1\pi \right).$$

Thus around a zero $\tau = \tau_0$ of $\zeta(\omega) - \eta$, we have an expansion:

$$\zeta(\omega) - \eta = \frac{1}{2\omega_1} \left[ \frac{k_1}{2} \left( \frac{\vartheta'_1}{\vartheta_1} \right)' + \frac{\partial}{\partial\tau} \left( \frac{\vartheta'_1}{\vartheta_1} \right) \right] (\tau - \tau_0) + \dots.$$

By the heat equation we can express this as

$$\zeta(\omega) - \eta = \frac{1}{2\omega_1} \left[ \frac{k_1}{2} \left( \frac{\vartheta'_1}{\vartheta_1} \right)' + \frac{1}{4\pi i} \left( \frac{\vartheta''_1}{\vartheta_1} \right)' \right] (\tau - \tau_0) + \dots.$$

However, differentiating the expression (70) leads to

$$\wp'(u) = -\frac{1}{8\omega_1^3} \left( \frac{\vartheta'_1}{\vartheta_1} \right)'' = -\frac{1}{8\omega_1^3} \left[ \left( \frac{\vartheta''_1}{\vartheta_1} \right)' - 2 \left( \frac{\vartheta'_1}{\vartheta_1} \right)' \left( \frac{\vartheta'_1}{\vartheta_1} \right) \right],$$

which, in consequence of the fact that

$$\frac{\vartheta'_1}{\vartheta_1} = -ik_1\pi$$

at $\tau_0$, gives

(72) $$\zeta(\omega) - \eta = \frac{i\omega_1^2}{\pi} \wp'(\omega)(\tau - \tau_0) + \dots.$$

Substituting in the formula (68) for $\xi$ we obtain

$$\xi = \frac{\pi}{2i\omega_1^2(\tau - \tau_0)} + \dots,$$

thus

$$\xi = \frac{-2x_0(e_3 - e_2)}{(x - x_0)} + \dots,$$

and finally

$$y(x) = \frac{-2x_0(e_3 - e_2)}{(e_2 - e_1)(x - x_0)} + \dots$$

$$= \frac{-2x_0(x_0 - 1)}{(x - x_0)} + \dots.$$

---

Proposition 10. If $y(x), y(x) - 1$ or $y(x) - x$ vanishes at $x = x_0$, then

$$y(x) = \mp \frac{(x - x_0)}{2(x_0 - 1)} + \ldots, \quad y(x) = 1 \pm \frac{(x - x_0)}{2x_0} + \ldots,$$

or $$y(x) = x_0 \mp \frac{(x - x_0)}{2} + \ldots,$$

where the conformal structure is singular if the lower sign holds.

Proof. The method of proof is by expansion as in Proposition 8. If $y(x) = -(x - x_0)/2(x_0 - 1) + \ldots$, then $z = z_0 + \ldots$ is regular, in which case

$$\Omega_1^2 = \frac{x_0}{2(1 - x_0)} \left(z_0 + \frac{1}{2}\right) + \ldots,$$

$$\Omega_2^2 = \frac{(x - x_0)^2}{4(x_0 - 1)^2} \left(z_0 + \frac{1}{2x_0}\right) \left(z_0 + \frac{1}{2}\right) + \ldots,$$

$$\Omega_3^2 = \frac{x_0}{2(1 - x_0)} \left(z_0 + \frac{1}{2x_0}\right) + \ldots.$$

Here $\Omega_2^2$ vanishes to higher order than either $\Omega_1^2$ or $\Omega_3^2$, so the conformal structure can not be extended over either a zero-dimensional or two-dimensional orbit. The other cases are similar, with $\Omega_3^2$ and $\Omega_1^2$ vanishing.

Now $y$ vanishes if $\xi = e_1$, which from (68) is when

$$e_1 = \wp(\omega) + \frac{\wp'(\omega)}{2(\zeta(\omega) - \eta)}.$$

Using the identity

$$\zeta_1(u) \equiv \zeta(u + \omega_1) - \eta_1 = \zeta(u) + \frac{\wp'(u)}{2(\wp(u) - e_1)},$$

this is equivalent to $\omega = \omega_1$ (mod $2\omega_1, 2\omega_3$) or $\zeta_1(\omega) = \eta$. But $\omega = k_1\omega_3 - ik_3\omega_1$ is imaginary and $\omega_1$ real, so only the second case may occur.

Proposition 11. If $\zeta_1(\omega) = \eta$ at $x = x_0$, then the solution to the Painlevé equation has the form $y(x) = -(x - x_0)/2(x_0 - 1) + \ldots$.

Proof. The calculation is similar to Proposition 9. By (68) and (74), $\xi$ satisfies

$$\frac{\wp'(\omega)(e_1 - \xi)}{2(\xi - \wp(\omega))(e_1 - \wp(\omega))} = \zeta_1(\omega) - \eta,$$ but we have the relation

$$\zeta_1(u) - \frac{\eta_1}{\omega_1} u = \frac{1}{2\omega_1} \frac{\vartheta'_2(\nu)}{\vartheta_2(\nu)}.$$

Following the arguments of Proposition 9 with the theta function $\vartheta_2$, we obtain

$$\zeta_1(\omega) - \eta = \frac{i\omega_1^2}{\pi} \wp'(\omega + \omega_1)(\tau - \tau_0) + \dots,$$

and so from (75),

$$e_1 - \xi = \frac{i\omega_1^2}{\pi} \frac{2(e_1 - \wp(\omega))^2 \wp'(\omega + \omega_1)}{\wp'(\omega)} (\tau - \tau_0) + \dots,$$

and differentiating the formula

$$\wp(u + \omega_1) = e_1 + \frac{(e_1 - e_2)(e_1 - e_3)}{\wp(u) - e_1}$$

gives

$$\xi - e_1 = \frac{2i\omega_1^2}{\pi}(e_1 - e_2)(e_1 - e_3)(\tau - \tau_0) + \dots.$$

Hence, converting from $\tau$ to $x$,

$$y(x) = \frac{\xi - e_1}{e_2 - e_1} = \frac{-2i\omega_1^2}{\pi}(e_1 - e_3)(\tau - \tau_0) + \dots$$

$$= \frac{(e_1 - e_3)}{2x_0(e_3 - e_2)}(x - x_0) + \dots$$

$$= -\frac{(x - x_0)}{2(x_0 - 1)} + \dots.$$

This discussion of the behaviour of $y(x)$ at some of the special values is sufficient for the regularity arguments which follow. However, we have so far only discussed the regularity of the conformal structure, and not the Einstein metric within that conformal class. The following proposition tells us when the metric is regular.

**Proposition 12.** Suppose the conformal structure is non-singular. Then the Einstein metric in the conformal class is well defined if $\zeta(\omega) - \eta \neq 0$.

**Proof.** From the twistor point of view, the metric is well-defined for those twistor lines on which the twisted 1-form $\theta$ is non-vanishing.

---

Recall, as in the proof of Theorem 4, that on the twistor space $Z$, we have

$$\alpha : \mathfrak{g}^c \rightarrow TZ \quad \text{and} \quad \theta : TZ \rightarrow K^{-1/2},$$

and the composition is defined by

$$x \mapsto \operatorname{tr}(\beta x)$$

for $\beta$ a holomorphic section of $\mathfrak{g}^c \otimes K^{-1/2}$. Since $A = \alpha^{-1}$, it follows that $\theta$ vanishes on a twistor line if and only if

$$\operatorname{tr}(A\beta) = 0.$$

Now in terms of the eigenvectors $v_1, v_2$ (44), we can write, up to a constant multiple,

$$\beta = v_1 \otimes v_2 + v_2 \otimes v_1$$

using the skew form on $C^2$ to identify with its dual. Thus

$$\operatorname{tr}(A\beta) = 2 < Av_1, v_2 >,$$

and now applying the formula (45) we see that

(76)

$$\operatorname{tr}(A\beta) = \frac{\wp'(u-c)}{\wp'(u)} + \frac{(\wp(u+c) - \wp(u-c))}{\wp'(u)} \theta_1.$$

So $\operatorname{tr}(A\beta)$ vanishes if

(77)

$$\theta_1 + \frac{\wp'(u-c)}{\wp(u+c) - \wp(u-c)} = 0.$$

From (50) and (47), this can be written as

$$0 = \zeta(2u) - 2\zeta(u-c) - \eta - \zeta(2u) + \zeta(2c) + 2\zeta(u-c)$$

$$= \zeta(2c) - \eta = \zeta(\omega) - \eta$$

from the definition of $\omega$.

**Proposition 13.** Let $x_0, x_1$ be two consecutive values of $x$ at which $\omega$ is a lattice point. Then there is a unique point $\bar{x} \in (x_0, x_1)$ at which $\zeta(\omega) = \eta$.

**Proof.** At $x_0, x_1$, $\vartheta_1(\omega, \tau)$ has a simple zero, and it follows that

$$f(x) = \frac{\vartheta'_1}{i\vartheta_1}(\omega, \tau) + k_1\pi$$ tends to $ +\infty $ as $ x\rightarrow x_{0}+ $ and $ -\infty $ as $ x\rightarrow x_{1}- $ . Since $ \vartheta_{1} $ only vanishes at the lattice points, $ f(x) $ is regular in the interval and thus has an odd number (with multiplicity) of zeros, and hence at least one.

$$
x\to x_{1}-
$$

$$
x\to x_{0}+
\vartheta_{1}
$$

$$
f(x)
$$

From (72), the sign of the derivative of f is determined by $ \wp^{\prime}(\omega) $ , and this vanishes only when $ \omega $ is a half-period. Since $ x_{0} $ and $ x_{1} $ correspond to neighbouring lattice points, there is only one point $ \tilde{x}\in(x_0,x_1) $ at which $ \wp^{\prime}(\omega)=0 $ . This cannot be a zero of $ \zeta(\omega)-\eta $ by using $ \zeta((2n+ 1)\omega_{3})=(2n+1)\eta_{3} $ and the Legendre relation, so the zeroes of f(x) are simple, and there is an odd number.

$$
\wp^{\prime}(\omega)
$$

$$
\omega
$$

$$
x_{1}
$$

$$
x_{0}
$$

$$
\tilde{x}\in(x_0,x_1)
$$

$$
\wp^{\prime}(\omega)=0
$$

$$
\zeta((2n+
\zeta(\omega)-\eta
$$

$$
1)\omega_{3})=(2n+1)\eta_{3}
$$

$$
f(x)
$$

On the other hand, in each interval $ \left(x_{0}\right) $ most one zero, since the sign of $ f^{\prime} $ is consta of zeros is odd, less than two, and hence o

$(\tilde{x}), (\tilde{x}, x_{1})$ there can be at least in each, thus the number of.

$$
(x_{0},\tilde{x}),\;(\tilde{x},x_{1})
$$

$$
f^{\prime}
$$

We now put together these results to obtain:

Theorem 7. Let y(x) be the solution to the where $ k_{3}>0 $ and $ 0\leq k_{1}<2 $ .Let $ x_{n}=x(i k_{3}/( $ positive integer n. Then the following hold:

ainlevé equation (68), [+2n-2)], for each

$$
y(x)
$$

$$
(68)
$$

$$
0\leq k_{1}<2
$$

$$
k_{3}>0
$$

$$
x_{n}=x(ik_{3}/(k_{1}+2n-2))
$$

1. If $ k_{1}\leq 1 $ , the poles of y(x) with negative residue are $ \bar{x}_{1},\bar{x}_{2},\dots $ with $ \bar{x}_{n}\in\left(x_{n},x_{n+1}\right). $

$$
k_{1}\leq1
$$

$$
\bar{x}_{1},\bar{x}_{2},\ldots
$$

$$
y(x)
$$

$$
\bar{x}_{n}\in(x_{n},x_{n+1})
$$

2. If $ k_{1} > 1 $ , the poles of y(x) with negative residue are $ \bar{x}_{0},\bar{x}_{1},\dots $ with $ \bar{x}_{n}\in\left(x_{n},x_{n+1}\right) $ and $ x_{0}=1. $

$$
k_{1}>1
$$

$$
y(x)
$$

$$
\bar{x}_{0},\bar{x}_{1},\ldots
$$

$$
\bar{x}_{n}\in(x_{n},x_{n+1})
$$

$$
x_{0}=1
$$

3. The function y(x) defines a complete aric for $ x\in\left(\bar{x}_{n},x_{n+1}\right] $ .The metric is de $ x=x_{n+1} $ the origin and $ x=\bar{x}_{n} $ the bo

anti-self-dual Einstein metined on the unit ball, with secondary.

$$
y(x)
$$

$$
x\in\left(\bar{x}_{n},x_{n+1}\right]
$$

$$
x=x_{n+1}
$$

$$
x=\bar{x}_n
$$

Proof. To begin with, note that

$$
x=\frac{e_{3}-e_{1}}{e_{2}-e_{1}}=\left[\frac{(1+q)(1+q^{3})(1+q^{5})\ldots}{(1-q)(1-q^{3})(1-q^{5})\ldots}\right]^{8}
$$

where $ q=e^{i\pi \tau} $ , so that for a real elliptic curve with $ q=e^{-\pi \sigma}, x>1 $ and $ \sigma\rightarrow0 $ corresponds to $ x\rightarrow\infty $ , whereas $ \sigma\rightarrow\infty $ gives $ x\rightarrow1. $ Moreover, since $ dx/d\sigma $ is negative from (69), $ x $ is decreasing as a function of $ \sigma. $

$$
q=e^{i\pi\tau}
$$

$$
q=e^{-\pi\sigma},x>1
$$

$$
\sigma\to0
$$

$$
x\to\infty.
$$

$$
\sigma\to\infty
$$

$$
x\to1
$$

$$
dx/d\sigma
$$

$$
\sigma
$$

Take a solution $ y ( x ) $ , assuming without loss of generality that $ k_{3}>0 $ and $ 0\leq k_{1}<2 $ . Then $ \omega=k_{1}\omega_{3}-ik_{3}\omega_{1} $ is a lattice point if and only if

$$
k_{3}>0
$$

$$
0\leq k_{1}<2
$$

$$
y(x)
$$

$$
\omega=k_{1}\omega_{3}-ik_{3}\omega_{1}
$$

$$
\sigma\equiv\frac{\omega_{3}}{i\omega_{1}}=\frac{k_{3}}{k_{1}+2n-2}
$$

for n a positive integer. Let $ x_{n} $ be the corresponding values of $ x(i\sigma). $ Then $ \{x_{n}\} $ is an increasing sequence. By Proposition 13, there is a unique zero $ \bar{x}_{n} $ of $ \zeta(\omega)-\eta $ in each interval $ (x_{n},x_{n+1}). $

$$
x_{n}
$$

$$
x(i\sigma)
$$

$$
\{x_n\}
$$

$$
\bar{x}_{n}
$$

$$
\zeta(\omega)-\eta
$$

$$
(x_{n},x_{n+1})
$$

---

We wish to enumerate all such zeros, not just those for $x > x_1$. Suppose $x < x_1$. Then $\sigma > k_3/k_1$. As in Proposition 13, we define

$$f(\sigma) = \frac{\vartheta_1}{i\vartheta_1}(k_1 i\sigma/2 - ik_3/2, i\sigma) + k_1 \pi.$$

The zeros of $f$ are the zeros of $\zeta(\omega) - \eta = f(\sigma)/(2\omega_1)$ and hence the poles of $y(x)$ with negative residue.

Near $\nu = 0$, $\vartheta'_1/\vartheta_1 \sim \pi \cot \pi\nu$, which shows that $f(\sigma) \rightarrow -\infty$ as $\sigma \rightarrow k_3/k_1+$. On the other hand, the expansion

$$\vartheta_1(\nu) = \sum_{n=0}^{\infty} (-1)^n 2q^{(n+1/2)} \sin(2n+1)\pi\nu$$

implies that $f(\sigma) \rightarrow \pi(k_1-1)$ as $\sigma \rightarrow \infty$.

Suppose $k_1 < 1$. Then $f$ is negative at both ends of the interval $(k_3/k_1,\infty)$. If it vanishes in the interval, it must do so with derivatives of both signs. However, $\wp'(\omega)$ vanishes only when $\omega = i(k_1\sigma-k_3)/2$ is a half period, and there are no such values when $\sigma > k_3/k_1$. Thus, as in Proposition 13, if $f$ vanishes, the sign of its derivative is fixed. We conclude that $f(\sigma)$ is negative for all $\sigma > k_3/k_1$.

Now suppose $k_1 > 1$. In this case $f$ is positive as $\sigma \rightarrow \infty$, and hence has an odd number of zeros in the interval. Since $\omega$ is a half-period when $\sigma = k_3/(k_1-1)$, we can repeat the argument of Proposition 13 and deduce that there is a unique such zero.

Finally consider $k_1 = 1$. Since $\omega = \omega_3 - ik_3\omega_1$, the points $x_n$ are given by

$$\sigma = \frac{k_3}{2n-1},$$

and so the largest such value is $\sigma = k_3$. Now for $\sigma > k_3$ we need to know if

$$f(\sigma) = \frac{\vartheta'_1}{i\vartheta_1}(\tau/2 - ik_3/2,\tau) + \pi$$

vanishes. But (see [33])

$$\vartheta_1(\nu+\tau/2) = iq^{-1/4}e^{-i\pi\nu}\vartheta_4(\nu),$$

where $q = e^{i\pi\tau}$, so differentiating with respect to $\nu$ shows (78) vanishes if and only if

$$\vartheta'_4(-ik_3/2) = 0.$$

---

But we have an expansion

$$\frac{1}{4\pi} \frac{\vartheta'_4}{\vartheta_4}(\nu) = \sum_{1}^{\infty} \frac{q^{2s-1} \sin 2\pi\nu}{1 - 2q^{2s-1} \cos 2\pi\nu + q^{4s-2}}.$$

The denominator can be written, for $\nu = -ik_3/2$, as

$$e^{-(4s-2)\pi\sigma} (e^{(2s-1)\pi\sigma} - e^{\pi k_3/2}) (e^{(2s-1)\pi\sigma} - e^{-\pi k_3/2})$$,

and if $\sigma > k_3 > 0$, this is positive, and so in this range $\vartheta'_4$ is non-zero. Hence $f$ is negative for all $\sigma > k_3$.

It follows that the poles of $y(x)$ with negative residue are $\bar{x}_1, \bar{x}_2 \dots$ if $k_1 < 1$, and $\bar{x}_0, \bar{x}_1 \dots$ if $k_1 > 1$ where $\bar{x}_n \in (x_n, x_{n+1})$ (setting $x_0 = 1$).

To deal with Part 3 of the Theorem, note that from Proposition 9, $y(x)$ has a pole with positive residue at $x_n$ and negative residue at $\bar{x}_n$, so $y \rightarrow -\infty$ at both ends of the interval $(\bar{x}_n, x_{n+1})$. It follows that $y(x)$ must be negative in the whole interval, for if the graph crosses the $x$-axis it must do so at some point with a positive derivative. However, from Proposition 11, only a negative derivative can occur. This means that in particular, $y, y-1$ and $y-x$ are non-zero in the interval, and so the conformal structure is non-singular. Since it is negative definite at $x=x_n$, it is negative definite everywhere. From Proposition 12, the Einstein metric is well-defined for $x \in (\bar{x}_n, x_{n+1})$.

There remains the question of the behaviour of the Einstein metric at the puncture and at the boundary, where we know it is singular. On the twistor space, the twisted 1-form is already well-defined at the boundary, and by Hartog's theorem extends over the twistor line corresponding to the puncture. This means that the inverse of the conformal factor (65) is smooth, but may vanish. To determine if it vanishes, we could calculate more expansions, but we can also rely on more general facts. The most important feature is that the conformal structure is everywhere regular. Choosing an Einstein metric within the conformal class can be done by solving a (conformally invariant) linear differential equation: if the metric is $g=f^{-2}g_0$, then $f$ satisfies the equation

$$H_0 f + Ric_0 f = 0,$$

where $H_0$ is the trace-free part of the hessian, and $Ric_0$ the trace-free Ricci tensor of some metric in the conformal class. This overdetermined equation severely restricts the behaviour of $f$ at a zero. For an isolated zero, we must have, in normal coordinates, $f = cr^2 + \ldots$. However, the scalar curvature of the Einstein metric is given by

$$f^3(6\Delta(f^{-1}) + Rf^{-1}).$$

Since this is a negative constant, $f$ can not in fact vanish at an isolated point. Thus the metric is non-singular at the puncture. On the boundary hypersurface $f$ must have a simple zero (see also [15]), which makes the metric complete.

The metric constructed in Theorem 7 depends on two parameters $k_1, k_3$ effectively describing the monodromy group. It is natural to ask how the conformal structure on the boundary of the ball depends on the parameters. For this we must calculate $\Omega_1^2, \Omega_2^2$ and $\Omega_3^2$ at the point where $\zeta(\omega) = \eta$. From Proposition 12 this corresponds to the conformal factor becoming singular, i.e., to the vanishing of the denominator:

(79) $$x\Omega_1\Omega_2 + 2\Omega_3(\Omega_2^2 - (1-x)\Omega_1^2) = 0.$$

This provides one relation, and we also have the conserved quantity (28),

(80) $$\Omega_1^2 - \Omega_2^2 - \Omega_3^2 = -1/4.$$

A third equation can be obtained by considering the determinant of the connection matrix at $x = \bar{x}_n$. This is a meromorphic quadratic differential $(\det A)dz^2$ which around $z = 0$ has an expansion:

$$\det A = -\frac{1}{16z^2} + \frac{1}{z}\left(\operatorname{tr} A_1A_2 + \frac{1}{x}\operatorname{tr} A_1A_3\right) + \ldots$$

and so, using (25), evaluating the coefficient of $1/z$ gives a linear equation in $\Omega_3^2$ and $\Omega_2^2$. Using $z = (w-e_1)/(e_2-e_1)$, the poles are at $w=e_i$, and the connection form is

$$\sum_{i=1}^{3} \frac{A_i dw}{(w-e_i)}$$

Now at $x = \bar{x}_n$, $\theta_1$ is given by (77), and it follows from (45) that

$$\wp'(u)Av_1 = -\frac{\wp'(u-c)}{\wp(u+c)-\wp(u-c)}v_2,$$

$$\wp'(u)Av_2 = \frac{\wp'(u+c)}{\wp(u+c)-\wp(u-c)}v_1,$$ and so

$$\wp'(u)^2 \det A = \frac{\wp'(u + c)\wp'(u - c)}{(\wp(u + c) - \wp(u - c))^2}$$

$$= \wp(2c) - \wp(2u) = \wp(\omega) - \wp(2u)$$

by a well-known identity. Expanding the right-hand side in $\wp(u) = w$ around $w = e_1$ gives

$$\det A = -\frac{1}{16(w - e_1)^2} + \frac{1}{(w - e_1)} \frac{(e_1 + 2\wp(\omega))}{8(e_1 - e_2)(e_1 - e_3)} + \ldots,$$

thus

$$\frac{\text{tr } A_1 A_2}{(e_1 - e_2)} + \frac{\text{tr } A_1 A_3}{(e_1 - e_3)} = -\frac{(e_1 + 2\wp(\omega))}{8(e_1 - e_2)(e_1 - e_3)},$$

which yields the equation

$$\Omega_3^2 - x\Omega_1^2 = \frac{(1+x)}{12} - \frac{\wp(\omega)}{4(e_1 - e_2)} = \frac{a}{4}.$$

The expansions about the other poles lead to similar equations which are linearly equivalent, given the relation (80).

We need to consider the signs involved here. For this, note the fact that, if $u$ is imaginary, $\wp(u)$ is real and $\wp(u) \rightarrow -\infty$ if $u \rightarrow 0$ or $2\omega_3$. The maximum in between occurs at the turning point $u = \omega_3$, with value $e_3$ and thus $\wp(\omega) < e_3$. From (81), this means that

$$a > \frac{(1+x)}{3} - \frac{e_3}{(e_1 - e_2)} = x.$$

Continuing, by (81),(79) and (80) we obtain a quadratic equation for $\Omega_3^2$ which yields the two solutions $\Omega_3^2 = 1/4$ and $\Omega_3^2 = a(a-x)/4(1-x)$. Since from (64), for $x > 1$, $\Omega_3^2$ must be negative to get a definite metric, it is the second case which holds and gives

$$\Omega_1^2 = \frac{a(1-a)}{4x(x-1)}, \quad \Omega_2^2 = \frac{(1-a)(x-a)}{4x}, \quad \Omega_3^2 = \frac{a(x-a)}{4(x-1)}.$$

Using (64), and the fact that $a > x$, the positive definite conformal structure on the sphere is then defined by

$$(a-x)\sigma_1^2 + a\sigma_2^2 + (a-1)\sigma_3^2,$$ and since $a > x$, it follows that $a > a - 1 > a - x$.

Remark. Note that the function $y(x)$ depends only on $k_1$ modulo 2Z, as befits its dependence on the monodromy $e^{\pi ik_1}$. However, for each choice of logarithm $k_1 + 2n$, there is a metric on the ball, inducing a different conformal structure on the boundary sphere, for $x$ can be read off from the conformal structure in (82). The analytic continuation of a single solution $y(x)$ to the Painlevé equation thus defines many Einstein metrics.

The obvious question to ask is whether every invariant conformal structure on $SU(2)$ can be obtained in this way. Let the conformal structure be given by

$$\lambda_1 \sigma_1^2 + \lambda_2 \sigma_2^2 + \lambda_3 \sigma_3^2.$$

Clearly, from (82), since $x \neq 0, 1$, the $\lambda_i$ must be distinct. Assuming this, choose a basis such that $\lambda_2 > \lambda_3 > \lambda_1 > 0$ and define

$$x = \frac{\lambda_2 - \lambda_1}{\lambda_2 - \lambda_3}.$$

Then $x > 1$. Now consider the elliptic curve in Weierstrass form

$$\wp'(u)^2 = 4(\wp(u) - e_1)(\wp(u) - e_2)(\wp(u) - e_3),$$

with $e_1 = \lambda_2 - (\lambda_1 + \lambda_2 + \lambda_3)/3, e_2 = \lambda_3 - (\lambda_1 + \lambda_2 + \lambda_3)/3, e_3 = \lambda_1 - (\lambda_1 + \lambda_2 + \lambda_3)/3$, so that

$$x = \frac{e_3 - e_1}{e_2 - e_1}.$$

Take $\omega$ to satisfy

$$\wp(\omega) = -(\lambda_1 + \lambda_2 + \lambda_3)/3.$$

Now $\omega$ must be imaginary: as above, for imaginary values of $u$, $\wp(u)$ lies in the interval $(-\infty, e_3)$, and since

$$e_3 = \lambda_1 - (\lambda_1 + \lambda_2 + \lambda_3)/3 > -(\lambda_1 + \lambda_2 + \lambda_3)/3,$$

the value $-(\lambda_1 + \lambda_2 + \lambda_3)/3$ is achieved at two imaginary points $\pm \omega$. This choice, by a simple manipulation, leads to the conformal structure (82) with $a$ satisfying

$$\frac{(1+x)}{12} - \frac{\wp(\omega)}{4(e_1 - e_2)} = \frac{a}{4},$$ as in formula (81).
Finally define $\eta$ by

$$\zeta(\omega) = \eta.$$

Since $\zeta(u)$ is real and odd, $\eta$ is imaginary. Now define real numbers

$$k_1 = 2(\omega \eta_1 - \omega_1 \eta)/i\pi,$$
$$k_3 = -2(\omega \eta_3 - \omega_3 \eta)/\pi.$$

For the sphere to arise as the boundary of one of the metrics of Theorem 7, we need to show that $k_3 \neq 0$. Suppose $k_3 = 0$. Then since $\omega$ is defined up to sign and addition of $2n\omega_3$ and $y(x)$ depends only on the monodromy, we can take $k_1 \leq 1$. In fact, since the monodromy is non-abelian, $k_1 < 1$. The relation $\zeta(\omega) = \eta$ implies that

$$\frac{\vartheta'_1}{\vartheta_1}(k_1\tau/2,\tau) + ik_1\pi = 0.$$

By the identity

$$\vartheta_1(\nu/\tau,-1/\tau) = \frac{\sqrt{\tau}}{i\sqrt{i}}e^{\pi i\nu^2/\tau}\vartheta_1(\nu,\tau),$$

this is equivalent to

$$\vartheta'_1(k_1/2,-1/\tau) = 0.$$

But the expansion

$$\frac{1}{4\pi} \frac{\vartheta'_1(\nu)}{\vartheta_1(\nu)} = \frac{1}{4} \cot \pi\nu + \sum_{n=1}^{\infty} \frac{\sin 2\pi\nu}{q^{-2n}-2\cos 2\pi\nu+q^{2n}}$$

shows that for a real elliptic curve with $\tau = i\sigma$, the right-hand side is positive if $k_1 < 1$. But then $\zeta(\omega)-\eta$ is never zero, which contradicts the definition of $\eta$.

From the above discussion, we can prove the following theorem:

**Theorem 8.** Given any left-invariant conformal structure on the 3-sphere, there exists a unique complete anti-self-dual Einstein metric on the 4-ball which induces the given conformal structure on the sphere at infinity.

**Proof.** Choose a basis such that the conformal structure is given by

$$\lambda_1 \sigma_1^2 + \lambda_2 \sigma_2^2 + \lambda_3 \sigma_3^2$$ with $\lambda_2 \geq \lambda_3 \geq \lambda_1 > 0$. If equality holds anywhere, then Pedersen's metric [29] or the hyperbolic metric provides the solution. Otherwise, use the solution of Theorem 7, with the values of $k_1, k_3$ given above.

As to uniqueness, LeBrun's twistor method [22] shows that the local metric in a collar neighbourhood is determined by the conformal structure: the twistor space is the space of null geodesics of the complexification of the conformal structure on the 3-manifold. Thus an $SU(2)$-invariant conformal structure generates an $SU(2)$-invariant Einstein metric, and hence one of the cases considered here. The only choice is then whether to take the solution for $x < \bar{x}_n$ in Theorem 7, or for $x > \bar{x}_n$. But the second case is an analytic continuation of the first, and if it can be completed to the ball, we would have an anti-self-dual conformal structure on a compact 4-manifold homeomorphic to $S^4$. Since the signature of the sphere is zero, but also represented by the $\mathcal{L}^2$ norm of the Weyl tensor, it must be conformally flat and hence the Einstein metric is the hyperbolic metric. This yields the standard conformal structure on $S^3$, and so any other metric is unique. Of course, since the upper and lower hemispheres are isometric the metric is also unique in this case too.

## Remark.

1. The classification of Theorem 13 in the final section will show in fact that we do not need to prescribe the topology of the interior as the ball — there are no other complete anti-self-dual Einstein metrics which induce a left invariant conformal structure on the 3-sphere.

2. Since we have seen in the proof of Theorem 8 that the explicit metrics of Theorem 7 are the same as the twistor-theoretic ones whose existence was shown by LeBrun, it is useful to note how the isomonodromic deformation story fits in to his approach. We recall that the twistor space $Z$ is the space of complex null geodesics on $SL(2,\mathbf{C})$ with respect to a left-invariant metric. Consider the action of $SL(2,\mathbf{C})$ on $Z$. The monodromy group $\Gamma$ should in principle be the stabilizer of a generic point in $Z$, i.e., a null geodesic. A geodesic $\gamma(z)$ is stabilized by $g \in SL(2,C)$ if

$$g\gamma(z) = \gamma(z + k).$$

In the general context of geodesics of left-invariant metrics on Lie groups (see [1], for example) we set

$$\omega_c = \gamma^{-1} \frac{d\gamma}{dz}.$$

Then $\omega_c$ satisfies Euler's equation, which is of the form

$$\frac{d\omega_c}{dz} = B(\omega_c, \omega_c).$$

For $SU(2)$, the problem is the same as the motion of a rigid body, where $\omega_c$ is interpreted as the angular velocity in the body. It is clearly invariant by any left multiplication, in particular by $g$ above and hence periodic. In fact, Euler's equation, as discussed in Section 3, can be solved with elliptic functions, and $\gamma(z)$ therefore satisfies a linear equation

$$\frac{d\gamma}{dz} = \gamma\omega_c$$

on an elliptic curve. In this context, $g$ is a monodromy element for the solution. We leave it to the reader to link up this monodromy problem for a connection on an elliptic curve with our discussion in Section 7. The explicit formulae for the motion of a rigid body given in [33] as an application of elliptic functions may be of some help.

Let us consider now the function (68) with $k_1 = 1$ and $k_3 > 0$. This will provide a one-parameter family of metrics in some ways modelled on the Bergmann metric. In particular, it will induce a left-invariant CR-structure on the boundary.

**Theorem 9.** Let $y(x)$ be the solution to the Painlevé equation (68) with $k_1 = 1$ and $k_3 > 0$. Let $x_1 = x(ik_3)$. Then $y(x)$ defines for $x \in (1,x_1]$ a complete anti-self-dual Einstein metric on the unit ball with $x = x_1$ the origin.

**Proof.** From Theorem 7, $y(x)$ has no poles in $(1,x_1)$ and so is regular for all $x \in (1,x_1)$. Moreover, as in the proof of that theorem, $y(x) \rightarrow -\infty$ as $x \rightarrow x_1 -$. As $x \rightarrow 1+$, $\sigma \rightarrow \infty$ and we can use the expansion

$$\vartheta_1(\nu) = \sum_{n=0}^{\infty} (-1)^n 2q^{(n+1/2)} \sin(2n + 1)\pi\nu$$

and its derivatives to estimate $y(x)$. We find

(84) $$y(x) = -1 - (2 + \cosh \pi k_3)s/4 + \ldots,$$ where $x = 1 + s$. In particular, the limit is negative as $x \rightarrow 1+$. Since from Proposition 11, the graph of $y(x)$ can only cross the $x$-axis with negative derivative, it follows that $y(x)$ is always negative, and in particular never equal to 0,1 or $x$, hence the Einstein metric is well defined, and as in Theorem 7, extends over the puncture at $x = x_1$.

The behaviour as $x \rightarrow 1$ can be seen by using (64) and (65). We obtain

$$\Omega_1^2 = -\frac{1}{4} \cosh^2(\pi k_3/2) + \ldots,$$

$$\Omega_2^2 = \frac{1}{16} \sinh^2(\pi k_3/2) \cosh^2(\pi k_3/2) + \ldots,$$

$$\Omega_3^2 = -\frac{1}{4} \sinh^2(\pi k_3/2) + \ldots,$$

and this yields a metric which is asymptotically a constant multiple of

$$g = \frac{ds^2}{s^2} + \frac{4}{s \cosh^2(\pi k_3/2)} \sigma_1^2 + \frac{16}{s^2 \sinh^2(\pi k_3/2) \cosh^2(\pi k_3/2)} \sigma_2^2$$

$$+ \frac{4}{s \sinh^2(\pi k_3/2)} \sigma_3^2 + \ldots,$$

which is clearly complete as $s \rightarrow 0$.

Note that the coefficient of $\sigma_2^2$ vanishes to order $s^2$ just as in the Bergmann metric. Moreover on the annihilator of $\sigma_2$, we have the conformal structure

$$h = \cosh^2(\pi k_3/2) \sigma_1^2 + \sinh^2(\pi k_3/2) \sigma_2^2.$$

From this, we evidently have the following:

**Theorem 10.** Let $h$ be a left-invariant CR-structure on $S^3$. Then there is a complete anti-self-dual Einstein metric on the ball which induces $h$ on the boundary.

**Proof.** Choosing a suitable basis, any invariant CR-structure can be represented in the form

$$\lambda_1 \sigma_1^2 + \lambda_3 \sigma_3^2$$

with $\lambda_1 \geq \lambda_3 > 0$. If $\lambda_1 = \lambda_3$, the Bergmann metric provides the required solution. Otherwise, take $k_3 > 0$ satisfying

$$\tanh(\pi k_3/2) = \sqrt{\lambda_3/\lambda_1}$$ and use the metric of Theorem 9.

## 9. A classification of Einstein metrics

In the previous sections we have seen how monodromy considerations enable us to write down explicitly the solutions to Einstein’s equations which arise from Painlevé’s sixth equation, whereas the general $SU(2)$-invariant anti-self-dual conformal structure is still as intractable as the general Painlevé transcendent. Recall that in Section 4 we mentioned the fact that the general anti-self-dual conformal structure with $\wedge^3\alpha$ vanishing with multiplicity 2 can be solved with Painlevé’s third equation, and hence more Painlevé transcendents. It turns out that the Einstein condition again provides a simplification which we shall use in this section to complete the classification of anti-self-dual Einstein metrics with $SU(2)$ symmetry and 3-dimensional generic orbits.

We shall prove the following:

Theorem 11. Let $M$ be an $SU(2)$-invariant anti-self-dual Einstein manifold with 3-dimensional orbits, and suppose that on its twistor space $\wedge^3\alpha$ vanishes on a divisor $D$ with multiplicity 2. Then the Einstein metric is defined by an $SU(2)$-invariant $U(1)$ monopole on a 3-dimensional space of constant curvature.

Before beginning the proof, let us recall the particular construction of anti-self-dual conformal structures by means of $U(1)$ monopoles. This has its origin in the Gibbons-Hawking Ansatz for hyperkähler metrics [13], where the 3-space is $\mathbf{R}^3$ and was used in the case of $S^3$ by Pedersen [29] and $H^3$ by LeBrun [24]. A $U(1)$ monopole on a 3-manifold $N^3$ with Riemannian metric $h$ is a connection $A$ on a principal $U(1)$-bundle, and a function $V$ such that $V$ and the curvature $F$ are related by the Bogomolny equations

$$F = -*dV.$$

This is essentially equivalent to $V$ being harmonic.

When $h$ is of constant curvature, the conformal structure

$$g_0 = Vh + V^{-1}(d\tau + A)^2$$

on the 4-dimensional principal $U(1)$-bundle over $N$ is anti-self-dual. Moreover, when $V$ and $A$ are $SU(2)$-invariant, the metric

$$g = f^2(Vh + V^{-1}(d\tau + A)^2)$$ is Einstein for a suitable choice of function $f$ (see [29]). In this symmetric situation, we have the following:

- If $N = \mathbf{R}^3$, then $V = \epsilon + m/r$ and $f = c$, which gives a metric with scalar curvature $R = 0$.

- If $N = S^3$, then $V = \epsilon + m \cot \rho$ and $f = c(\epsilon \cos \rho - m \sin \rho)^{-1}$, where $\rho$ is the distance from the fixed point of the $SU(2)$ action on $N$. This gives an Einstein metric with scalar curvature $R = -3\epsilon/c^2$.

- If $N = H^3$, then $V = \epsilon + m \coth \rho$ and $f = c(\epsilon \cosh \rho + m \sinh \rho)^{-1}$, where $\rho$ is the distance from the fixed point. This gives an Einstein metric with scalar curvature $R = 3\epsilon/c^2$

In all cases $\epsilon, m,$ and $c$ are real constants.

Proof of theorem. We shall use the twistor approach. From this point of view, a $U(1)$ monopole over a space of constant curvature is give by a holomorphic principal $\mathbf{C}^*$ bundle over its minitwistor space $\mathbf{T}$ which is of degree 0 on each twistor line in $\mathbf{T}$ (see [17]). The minitwistor space of $\mathbf{R}^3$ is the tangent bundle of $\mathbf{CP}^1$ with twistor lines the sections; of $S^3$ the quadric $\mathbf{CP}^1 \times \mathbf{CP}^1 \subset \mathbf{CP}^3$ with twistor lines plane sections; and of $H^3$ an open set in the quadric. Thus we need to prove that, if $Z$ is the twistor space of the Einstein manifold in the theorem, it can be expressed (at least locally around a twistor line) as a principal holomorphic $\mathbf{C}^*$ bundle over a minitwistor space $\mathbf{T}$, and such that the twistor lines of $Z$ map into twistor lines of $\mathbf{T}$. In fact, the existence of a $\mathbf{C}^*$ action is a global assertion, and it is sufficient for our purposes for $Z$ to fibre over $\mathbf{T}$ with the fibres orbits of a holomorphic vector field.

From the hypothesis of the theorem, we have $\wedge^3\alpha$ vanishing with multiplicity 2 on $D$, thus $2D$ is a divisor of $K^{-1}$ and (working locally or passing to a double covering) there is a holomorphic section $v$ of $K^{-1/2}$ vanishing on $D$. Since $D$ is $SU(2)$-invariant, so is $v$. But as in Theorem 4, the twisted 1-form $\theta$ on the twistor space of an Einstein manifold defines by composition with $\alpha$ a section $\beta$ of $K^{-1/2} \otimes \mathfrak{g}^c$, and hence a 3-dimensional subspace $\mathfrak{g}^c \subset H^0(Z, K^{-1/2})$. The section $v$ lies outside this subspace since it is invariant whereas the representation $\mathfrak{g}^c$ is irreducible. We thus have a 4-dimensional subspace $U$ of the space of sections.

We claim that there are no base points for this system, that is there are no points where all sections vanish. Suppose for a contradiction that $z \in Z$ is such a point. Since $s$ vanishes at $z$, this point lies in $D$. But the base locus is invariant by $SU(2)$, which has 3-dimensional orbits, hence a neighbourhood $D_0$ of $z$ in $D$ is contained in the locus. By reality, the same is true of the antipodal point $\tau(z)$. Thus all sections $u \in U$ vanish on $D_0 + \tau(D_0)$. Now let $P$ be a real twistor line passing through $z$. Since $K^{-1/2}$ is of degree 2 on $P$, $D$ meets it only in the points $z, \tau(z)$. Nearby twistor lines meet $D$ in $D_0$ and $\tau(D_0)$, thus in a neighbourhood of $P$, all sections $u \in U$ vanish only on $D_0 + \tau(D_0)$. Thus each $u$ can be written $u = fv$ for some holomorphic function $f$ in a neighbourhood of $P$. But on any twistor space all holomorphic functions are constant, thus $u$ is $SU(2)$-invariant, which we know not to be the case. Hence there are no base points.

Since there are no base points, we can use the system $U$ to define a holomorphic map $p : Z \rightarrow CP^3$ with the property that $p^*(\mathcal{O}(1)) \cong K^{-1/2}$. Since $K^{-1/2}$ has degree 2 on twistor lines, each twistor line maps to a conic in $CP^3$. Now $s = \text{tr}(\beta^2)$ is an $SU(2)$-invariant section of $K^{-1}$, and so its divisor is a component of the zero set of $\Lambda^3\alpha$. Hence, at least in a neighbourhood of a twistor line, $s = \lambda v^2$ for some constant $\lambda$. But the equation

$$\text{tr}(\beta^2) = \lambda v^2$$

defines a subvariety of degree 2 in $CP^3$, a nonsingular quadric if $\lambda \neq 0$ and a quadric cone if $\lambda = 0$. Note that from (39), which is equally valid in the present context, $\lambda = 0$ iff the scalar curvature $R = 0$. Thus if $R \neq 0$, $p$ maps $Z$ to a quadric and the twistor lines map to conics in the quadric, i.e., to plane sections. If $R = 0$, $p$ maps to the cone, but the complement of the vertex is isomorphic to $TCP^1$, and the sections are plane sections missing the vertex. In either case, then, the image is the minitwistor space for a 3-manifold of constant curvature, and the twistor lines correspond.

It remains to find the vector field along the fibres. For this, note (see [8], for example), that any real holomorphic section of $K^{-1/2}$ corresponds to a section $\omega$ of the bundle $\Lambda^2_+$ on $M$ satisfying a certain differential equation $\bar{D}_2\omega = 0$, and as a consequence of this and the Einstein condition, the vector field $X$ dual to the 1-form $d^*\omega$ is a Killing vector field. Thus the section $v$ generates an $SU(2)$-invariant vector field, which preserves the metric and hence induces a holomorphic vector field on the twistor space. Being invariant, it leaves fixed each section in $U$, and so acts along the fibres of the projection $p$.

The only thing left to check is that $X$ is not zero. However, if this were so, then $\omega$ would satisfy $\bar{D}_2\omega = 0$ and $d\omega = 0$ and would then be covariant constant by the definition of $\bar{D}_2$. But then the holonomy would reduce to $U(2)$ (i.e., the metric would be Kähler) or be trivial. On the other hand, as we have remarked in Section 2, an anti-self-dual Kähler metric has zero scalar curvature, and since the metric is Einstein, this makes it hyperkähler. Since the Kähler form $\omega$ is invariant, the action of $SU(2)$ on the full 3-dimensional space of covariant constant forms is trivial. In twistor terms, however, this means that the rank of $\alpha$ is 2, the case excluded here and dealt with in Theorem 2. The theorem is thus proved.

We can now put together Theorems 2, 6, and 11 to obtain a list of all invariant anti-self-dual Einstein metrics:

**Theorem 12.** Let $M$ be an $SU(2)$-invariant anti-self-dual Einstein metric with 3-dimensional generic orbits. Then $M$ is locally isometric to one of the following:

1. a 4-manifold of constant curvature,
2. the Eguchi-Hanson metric,
3. the Belinskii-Gibbons-Page-Pope metric,
4. an $SU(2)$-invariant $U(1)$-monopole over a 3-manifold of constant curvature,
5. a metric defined by the solution to Painlevé’s sixth equation in Theorem 6.
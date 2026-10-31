# Independent stress review of the intrinsic and joint gaps

Date: 2026-09-19. Reviewed `round3_rigidity.md` and `round3_joint_gap.md`,
the weighted-Hodge input in `round2_rigidity.md`, and the live manuscript's
derivation of `quantSW`. This review sought missing geometric hypotheses;
it did not modify either theorem file.

I found no remaining mathematical gap in the intrinsic argument or its
specified general-type blow-up specialization. The decisive point is that
the actual bounded spinor, with its determinant-connection curvature
budget, supplies more than the old bounded two-form model.

1. **The Hessian commutator does not omit a curvature derivative.** Put
   `T=integral <D_iD_j Phi,D_jD_i Phi>`. Integrating the first i derivative
   and commuting on the bundle-valued one-form D Phi gives

       T=||tr D^2 Phi||_2^2
           -integral Ric_ij <D_i Phi,D_j Phi>
           +sum_ij integral <F_ij D_j Phi,D_i Phi>.

   The antisymmetric Hessian identity gives
   `||D^2 Phi||_2^2-T=(1/2)sum_ij||F_ij Phi||_2^2`.
   This is the displayed integrated formula in the proof. It applies to
   nonabelian connections as well: skew-adjointness, not commutativity,
   supplies the needed sign in the cross term. No derivative of F occurs.

2. **The critical-looking curvature term can be absorbed at arbitrary
   total L2 size.** The divergence of
   `|D Phi|^2 <Phi,D Phi>^sharp` gives the intrinsic interpolation bound
   `||D Phi||_4^2<=4||Phi||_infinity||D^2 Phi||_2` in dimension four.
   Hence the cross term is bounded by
   `4||Phi||_infinity||F||_2||D^2 Phi||_2`. Young's inequality therefore
   absorbs a term linear in the Hessian norm. It neither requires a
   Sobolev constant nor assumes that the connection curvature is small.
   Squaring this estimate produces extensive integrals, with no extra
   factor of volume.

3. **W-minus is absent for the stated representation-theoretic reason.**
   In the spinor connection curvature, Clifford action projects the final
   two Riemann indices to Lambda-plus. This removes the W-minus block,
   but retains W-plus, scalar curvature, and the off-diagonal traceless
   Ricci blocks. The proof retains all of them. The separate determinant
   curvature still has an anti-self-dual component; it is controlled by
   `||F_A||_2^2=2||F_A^+||_2^2-4pi^2 a^2`. Thus an uncontrolled negative
   a-square is not silently discarded; it is exactly the B_a term.

4. **The test tensor is the same tensor whose strong norm is established.**
   The map Phi to A_psi is a parallel polynomial invariant under the U(1)
   phase, so its second covariant derivative is controlled by D_A^2 Phi
   and |D_A Phi|^2 without choosing a gauge. Contraction then bounds
   `nabla J_psi`, not merely a spinor derivative in a different bundle.
   Contracted Bianchi gives the weak estimate with one derivative on an
   arbitrary test tensor, so choosing the smooth `T=J_psi` is legitimate.
   Quantitatively the two factors are
   `C sqrt(epsilon V)` and `C sqrt((1+dcal/V+B_a)V)`; dividing their
   product by V gives exactly the normalized estimate in the proof.

5. **Neither spinor zeros nor hidden derivative concentration affect the
   lower bound.** Here rho is the smooth function |Phi|^2, and A_psi is
   polynomial even at zeros. The weighted Hodge identity supplies the
   derivative-energy value directly. Its cross-error integral is at most
   `C||d rho||_2||d psi||_2=O(Delta+eta)`, using bounded rho. It does not
   require uniform integrability of a derivative-energy density.

6. **The topological specialization supplies the sign needed above.**
   The selected genuine blow-up monopole class has a-square A-k for every
   choice of signs. If delta is small, the Chern--Weil integrand
   `s^2/24-|Ric^circ|^2/2+2|W-plus|^2` has strictly positive integral:
   its first two terms are bounded below by
   `(2/3)(1-delta)^2-2delta^2>0`. Thus A-k>0 follows from the hypothetical
   metric itself. No upper volume bound or bound on Euler/A is needed.
   The scalar lower bound on V is used in the correct direction when
   converting the topological error A d into an average.

The result is stronger than the older full-curvature conditional gap,
but the extra input is explicit: the actual rescaled monopole PDE and
determinant Chern--Weil identity. The older functional counterexample
lacked this input. This review supports the stated family theorem; it
does not establish publication priority or a general Yau26 theorem.

# Route Assessment — Step 81

Session `S0910A01`. Updated after the `L` orbit-exchange verification and radial scale-ledger repair.

## Positive mixed-row branch: current exact structural state

The product-orbifold construction remains a local positive-Einstein desingularization test around
\[
\mathcal O=(S^2\times S^2)/\langle(r_\pi,r_\pi)\rangle,
\]
not a solution of Yau Problem 26.  The useful current result is that the symmetry reduction is now sharper and less misleading.

Validated ingredients:

1. **`A` symmetry** exchanges nodes inside the two orbits `\{NN,SS\}` and `\{NS,SN\}` and removes the four scalar full-kernel projections because those modes are `A`-odd in the symmetric construction.
2. **`J` symmetry** fixes each node and the insertion direction `\omega_2`, acts as `diag(-1,+1,-1)` on both `\Lambda^\pm`, and kills all transverse `\omega_1,\omega_3` bubble projections at every actually constructed order.
3. **Rank-one determinant** gives the local second-order radial coefficient `\mu_1=0` for the bare product curvature block.
4. **`L` symmetry** with `L(x,y)=(-x,y)` descends to the quotient, exchanges the two `A`-orbits, reverses 4D orientation, and swaps plus/minus EH chiralities.  Executable checks show
   \[
   \omega_2^+\mapsto\omega_2^-,\quad L^*H^4_-(Lx)=H^4_+(x),\quad L^*O_{\rm rad}^-(Lx)=O_{\rm rad}^+(x)
   \]
   for the complete angular `rho_x` formula and the leading radial asymptotic tensor.

## Correct surviving radial equation

The reduced radial finite-dimensional response must retain the receiver scale:
\[
F_i(t_1,t_2)=t_i\sum_jB_{ij}t_j^2+R_i,
\]
not `\sum_jB_{ij}t_j^3`.  The current Ozuch estimate `O(t_max^{5/2})` is not sharp enough to identify this as the first true term at comparable scales.

In the `L`-transported radial normalization,
\[
F_2(t_1,t_2)=F_1(t_2,t_1),\qquad
B=\begin{pmatrix}a&b\\b&a\end{pmatrix}.
\]
For positive scales, the candidate leading system is
\[
\begin{pmatrix}a&b\\b&a\end{pmatrix}
\begin{pmatrix}t_1^2\\t_2^2\end{pmatrix}=0.
\]
Thus a positive kernel requires `a+b=0`; if `a=-b\ne0`, then the surviving branch is asymptotically equal-scale, while if `a=b=0` the entire candidate matrix vanishes and the next radial layer is decisive.  Symmetry alone does not imply any of these cancellations.

## Coefficient architecture

The combinatorics script shows that for the opposite-corner spin row:
\[
F_1=t_1\bigl((s+d)t_1^2+2c t_2^2\bigr)+\cdots,
\qquad
F_2=t_2\bigl(2c t_1^2+(s+d)t_2^2\bigr)+\cdots.
\]
Here:

- `s`: local self radial response after `\mu_1=0`;
- `d`: same-orbit diagonal same-chirality companion response; its leading kernel block is expected to vanish by chirality split but must be included until the full projected expansion proves this;
- `c`: one adjacent opposite-chirality cross response; each representative receiver sees two such sources, giving `b=2c`.

A corrected combinatorial point: in the opposite-corner spin row, cross-orbit mixed-chirality pairs are **adjacent**, not diagonal.  Diagonal geometry appears in the same-orbit same-chirality companion term.

## Next mathematical work

The next valuable execution/construction step is not another parity argument.  It is a source-pinned projected expansion for the even radial projection with enough precision to decide whether the first nonzero even layer is:

1. a pure `t_i t_j^2` matrix with coefficients `a=s+d`, `b=2c`;
2. a `t_i t_j^2 log t_j` or related logarithmic matrix, as suggested by Ozuch Remark 2.11 for higher asymptotic terms;
3. a higher-order term after additional cancellations.

The coefficient computation must use the full product `P` pseudo-inverse with additive spectral denominators, source singular subtraction only at the source/self node, and regular second-jet extraction at the receiver.  It must include the even shape mode `g_1-g_2`, Bianchi/DeTurck corrections, cutoff/matching terms, and exact radial projection normalization.

## Broader Yau--26 position

- The full sign-unrestricted all-dimensional proposition remains open.
- The restricted IL negative-gap theorem remains the most mature family-level result, but it does not settle the proposition.
- The graph-neck branch remains a negative laboratory with sharpened center constraints but no small-defect global construction.
- A02's Gursky/LeBrun positive-Einstein topology test is complementary: if it finds a positive-Einstein nonexistence result for the mixed rows, the local desingularization effort would change role; absent such an obstruction, the radial system remains a meaningful constructive test.

## Files

- `workspace/notes/step81_L_exchange_and_radial_ledger.md`
- `workspace/scripts/step81_L_symmetry_scale_ledger.py`
- `workspace/data/step81_L_symmetry_scale_ledger.json`
- `workspace/scripts/step81_L_H4_transport.py`
- `workspace/data/step81_L_H4_transport.json`
- `workspace/scripts/step81_L_radial_tensor_transport.py`
- `workspace/data/step81_L_radial_tensor_transport.json`
- `workspace/scripts/step81_radial_B_combinatorics.py`
- `workspace/data/step81_radial_B_combinatorics.json`
- `trace/ttcs/results/step81_ttcs01_verifier1_integration.md`

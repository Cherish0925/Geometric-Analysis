# Route assessment after Step 50

## 1. Product-quotient/Campedelli front

Step 49's categorical reversal has been corrected.  The valid state is:

* The complex-smoothing/Aubin--Yau chain is a real Einstein-existence mechanism to test.
* It is established for any nodal canonical model that is actually in a global Q-Gorenstein smoothing family with ample canonical class and whose simultaneous resolution identifies the smooth fiber with the minimal resolution.
* It is not established for every product-quotient candidate, and failure of this particular smoothing mechanism would not prove Einstein nonexistence.
* Mixed-chirality Eguchi--Hanson fillings and positive product quotients remain outside this negative Kähler--Einstein mechanism.

### 1.1 Explicit six-nodal classical Campedelli model

`workspace/scripts/step50_six_nodal_campedelli_arrangement.py` gives a concrete global-smoothing example inside the Alexeev--Pardini $(\mathbb Z_2)^3$ Campedelli component.  The arrangement
\[
 x,y,z,x-y,y-z,x-z,x-y+z=0
\]
has exactly six triple points and three double points, with no point of multiplicity at least four.  The script finds 1680 labellings by the nonzero elements of $\mathbb F_2^3$ for which every triple-point label set is a basis.  Alexeev--Pardini then gives a canonical model with six $A_1$ points and ample canonical class; moving the seven lines to general position smooths all six nodes.  Aubin--Yau on nearby smooth fibers plus simultaneous resolution/Ehresmann gives a negative Einstein metric on the minimal resolution.

This is existence evidence and a useful check that the smoothing mechanism is not empty.  It is not yet identified with the BCGP $G=\mathbb Z_4^2$ product-quotient row.

### 1.2 BCGP $G=\mathbb Z_4^2$ row

`workspace/scripts/step50_z4x4_character_smoothing_test.py` used the actual BCGP §6.7 branch triples
\[
((1,3),(1,0),(2,1)),\qquad ((3,2),(0,1),(1,1))
\]
and found
\[
\dim(H^0(2K_{C_1})\otimes H^0(K_{C_2}))^G=0,
\quad
\dim(H^0(K_{C_1})\otimes H^0(2K_{C_2}))^G=0.
\]
Under the quotient/reflexive-form/RDP comparison this gives the sufficient obstruction vanishing $H^0(\Omega^1_S\otimes K_S)=0$, hence $H^2(T_S)=0$, which would globalize local $A_1$ Q-Gorenstein smoothings.

What remains is source-level verification of that sheaf comparison for the six-nodal quotient and the exact Lee--Park/Burns--Wahl implication.  Also still unresolved: whether this BCGP row lies in the classical $(\mathbb Z_2)^3$ Campedelli component.  The shared fundamental group and numerical invariants are not enough.

## 2. Restricted negative Ishida--LeBrun route

A03 peer message #381 corrects the normalized-flow status.  A03 Step 51 should not be cited as proving the normalized Yang--Wang start.  A flat $T^4$ cutoff test shows curvature is created from zero by the Hessian of the cutoff, so the critical homothety cancellation does not eliminate the spatial Hessian forcing.  A metric-only Xu fixed-point repair gives a transported cutoff, not the fixed-cutoff geometric equation.  The correct remaining flow start is a coupled transported-coefficient system for $(\widehat g,\widehat a)$ with $\widehat a=a\circ\varphi^{-1}$ and the metric equation containing $-2\widehat a\widehat g$.

The positive-time shifted $T/U/C$ continuation remains a separate useful module, but the IL analytic platform should be treated as incomplete until the coupled transported-coefficient start is proved.

## 3. Current priorities

1. For the BCGP $\mathbb Z_4^2$ row, verify the quotient/RDP sheaf comparison and Lee--Park/Burns--Wahl smoothing implication, then decide whether the character-level vanishing gives a genuine global smoothing of all six nodes.
2. Determine whether the BCGP row is already known to lie in the Alexeev--Pardini classical Campedelli component; if a moduli-component identification exists, reuse it rather than presenting a new proof.
3. Continue independent scrutiny of the IL coupled transported-coefficient flow start after A03 #381.
4. Keep positive mixed-chirality rows separate: the negative Q-Gorenstein/Aubin--Yau chain does not decide them.

None of these settles the full all-dimensional Yau 26 proposition or the Lean formalization requirement.

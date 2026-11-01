"""Scaling exponents for the Calabi-orbifold desingularization route.

This is not a proof; it is a bookkeeping probe for Yau26 Explore.
It records how a (0,2)-tensor estimate measured in g_cal converts to
operator norm with respect to g_t ~ t*g_cal in the glued Calabi region.

Morteza--Viaclovsky Lemma 4.2 gives (k=0)
    | Ric_{g_t} - Lambda*g_t - t*lambda*chi*o |_{g_cal} <= C t^2 rho^2.
On the transition/damage zone rho ~ t^{-1/4}; in the core rho=O(1).
For a (0,2)-tensor T, |T|_{op,t*g_cal} = t^{-1}|T|_{op,g_cal}.
Thus remainder exponent in g_t-operator norm is:
    t^{-1} * t^2 * rho^2 = t^{1 + 2*rho_exponent}.
The obstruction term t*lambda*o has g_t-operator size t^{-1}*t*|lambda o| = O(1)
when lambda != 0 and o is nonzero.
"""
from fractions import Fraction

regions = {
    "core_rho_O_1": Fraction(0),      # rho ~ t^0
    "transition_rho_t_minus_quarter": Fraction(-1, 4),
}

print("region,remainder_exponent_gcal,remainder_exponent_gt_operator,obstruction_exponent_gt_operator")
for name, rho_exp in regions.items():
    rem_gcal = Fraction(2) + 2 * rho_exp
    rem_gt = rem_gcal - 1
    obstruction_gt = Fraction(0)  # t*o as (0,2), metric inverse contributes t^{-1}
    print(f"{name},{rem_gcal},{rem_gt},{obstruction_gt}")

assert regions["transition_rho_t_minus_quarter"] == Fraction(-1, 4)
assert Fraction(2) + 2 * Fraction(-1, 4) == Fraction(3, 2)
assert Fraction(3, 2) - 1 == Fraction(1, 2)
print("Conclusion: the MV remainder can be C0-small (worst t^1/2), but a nonzero first-obstruction term t*lambda*o is order one in g_t-operator norm.")

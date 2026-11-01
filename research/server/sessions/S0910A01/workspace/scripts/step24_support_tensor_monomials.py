#!/usr/bin/env python3
"""Monomial ledger for the Step 24 buffered selected-support estimates.

The goal is to prevent weight mistakes in the exact tensor proof.  We track only
powers of the physical cutoff a=chi^2, the curvature scale F, and the active
Sobolev test variable used for the critical L2 x L4 absorption.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Monomial:
    a: float
    F: float
    E: float = 0.0
    name: str = ""
    def __mul__(self, other):
        return Monomial(self.a + other.a, self.F + other.F, self.E + other.E,
                        f"({self.name}*{other.name})")
    def square(self):
        return Monomial(2*self.a, 2*self.F, 2*self.E, f"{self.name}^2")
    def same_exponents(self, other):
        return (self.a, self.F, self.E) == (other.a, other.F, other.E)
    def __str__(self):
        parts=[]
        if self.a: parts.append(f"a^{self.a:g}")
        if self.F: parts.append(f"F^{self.F:g}")
        if self.E: parts.append(f"E^{self.E:g}")
        return " ".join(parts) or "1"

F = Monomial(0,1,name="F")
E = Monomial(0,0,1,name="E")
chiF = Monomial(0.5,1,name="chiF")         # chi F = a^{1/2} F
aF32 = Monomial(1,1.5,name="aF32")        # a F^{3/2}
chiE = Monomial(0.5,0,1,name="chiE")

# q=2 curvature reaction: int a F^3 = int F*(chi F)^2
q2_reaction = Monomial(1,3,name="aF3")
q2_factor = F * chiF.square()
print("q=2 reaction:", q2_reaction, " factorization:", q2_factor)
assert q2_reaction.same_exponents(q2_factor)
print("  Sobolev variable: chi F; grad gives a|grad F|^2 + |dchi|^2 F^2")

# q=3 curvature reaction: I4=int a^2 F^4 = int F*(aF^{3/2})^2
q3_reaction = Monomial(2,4,name="a2F4")
q3_factor = F * aF32.square()
print("q=3 reaction:", q3_reaction, " factorization:", q3_factor)
assert q3_reaction.same_exponents(q3_factor)
print("  Sobolev variable: a F^(3/2); grad(a F^(3/2)) gives a^2 F |grad F|^2 + |da|^2 F^3")
print("  Since |da|^2 <= C r^-2 a, the cutoff term is <= C r^-2 a F^3 = C r^-2 Y")

# Defect potential: int a F |E|^2 = int F*(chi E)^2
defect_potential = Monomial(1,1,2,name="aF E2")
defect_factor = F * chiE.square()
print("defect potential:", defect_potential, " factorization:", defect_factor)
assert defect_potential.same_exponents(defect_factor)
print("  Sobolev variable: chi E; grad gives a|grad E|^2 + |dchi|^2 E^2")

# Show the wrong q=3 variable chi*F^(3/2) generates an uncontrolled cutoff term.
wrong_var = Monomial(0.5,1.5,name="chiF32")
wrong_square_times_F = F * wrong_var.square()
print("wrong q=3 variable chi F^(3/2) factors:", wrong_square_times_F)
assert wrong_square_times_F.same_exponents(Monomial(1,4,0))  # gives a F^4, not a^2 F^4
print("  It factors aF^4, not the actual a^2F^4 reaction, and its |dchi|^2 F^3 term lacks an a factor.")

print("PASS: Step 24 support-local q=2, q=3, and Q absorptions use consistent weights.")

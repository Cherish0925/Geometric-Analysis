"""Step 77: exact symbolic checks of the AK-Einstein first-tier identities and the
W+ Bochner integrand in AK variables.

Conventions (step-62 norms): W+ is a symmetric trace-free endomorphism of Lambda^+
written in an orthonormal frame (u, u2, u3), u = omega/sqrt2,
    W+ = [[r, eta^T], [eta, -r/2 I + V]],  tr V = 0,
Frobenius norms, q = |nabla omega|^2 = 4 r - 2 s/3 (AK Weitzenbock trace).
Outputs printed; no files written.
"""
import sympy as sp

r, s, q, e1, e2, v1, v2 = sp.symbols('r s q e1 e2 v1 v2', real=True)
V = sp.Matrix([[v1, v2], [v2, -v1]])
eta = sp.Matrix([e1, e2])
B = -r / 2 * sp.eye(2) + V
W = sp.zeros(3, 3)
W[0, 0] = r
W[0, 1:3] = eta.T
W[1:3, 0] = eta
W[1:3, 1:3] = B

trV2 = (V * V).trace()
eta2 = (eta.T * eta)[0]
etaVeta = (eta.T * V * eta)[0]

normW2 = sp.expand((W * W).trace())
trW3 = sp.expand((W ** 3).trace())
print('|W|^2 - (3/2 r^2 + 2|eta|^2 + trV^2) =',
      sp.simplify(normW2 - (sp.Rational(3, 2) * r**2 + 2 * eta2 + trV2)))
print('trW^3 - formula =',
      sp.simplify(trW3 - (sp.Rational(3, 4) * r**3 + sp.Rational(3, 2) * r * eta2
                          - sp.Rational(3, 2) * r * trV2 + 3 * etaVeta)))

# pointwise algebra |W+|^2 - s^2/24 with r = s/6 + q/4
sub = {r: s / 6 + q / 4}
lhs = sp.expand(normW2.subs(sub) - s**2 / 24)
rhs = sp.expand(2 * eta2 + trV2 + s * q / 8 + 3 * q**2 / 32)
print('|W+|^2 - s^2/24 - (2|eta|^2+trV^2+sq/8+3q^2/32) =', sp.simplify(lhs - rhs))

# LeBrun Prop.1 integrand: s W(om,om) - 8(|W|^2 - 1/2 |W(om)^perp|^2), W(om,om)=2r, |W(om)^perp|^2=2|eta|^2
leb = sp.expand((s * 2 * r - 8 * (normW2 - eta2)).subs(sub))
star = sp.expand(-(s * q / 2) - (8 * eta2 + 8 * trV2 + sp.Rational(3, 4) * q**2))
print('LeBrun integrand - [ -sq/2 - 8|eta|^2 - 8trV^2 - 3q^2/4 ] =', sp.simplify(leb - star))

# Chern-Weil c1^2 integrand with i F = W(om)^perp + (2s+q)/8 om - q/8 omhat, |om|^2=|omhat|^2=2
cw = 2 * eta2 + 2 * ((2 * s + q) / 8)**2 - 2 * (q / 8)**2      # |gamma+|^2 - |gamma-|^2
top = s**2 / 24 + 2 * normW2.subs(sub)                         # 4 pi^2 (2chi+3tau) density
print('CW density - topological density =', sp.factor(sp.expand(cw - top)),
      '  (integral of this vanishing is the Sekigawa/LeBrun identity x(-1/2))')

# Bochner right side 6 trW^3 - (s/2)|W|^2
boch = sp.expand((6 * trW3 - s / 2 * normW2).subs(sub))
boch_form = sp.expand(sp.Rational(9, 8) * (s / 6 + q / 4)**2 * q + (s / 2 + 9 * q / 4) * eta2
                      + (-2 * s - 9 * q / 4) * trV2 + 18 * etaVeta)
print('Bochner RHS - formula =', sp.simplify(boch - boch_form))

# Bianchi VIII control integrals (step-59 norms -> step-62: |eta|^2_62 = |eta|^2_59/2)
S, Qi, Q2, E59, W3 = -12, 64, sp.Rational(512, 3), 32, 16
print('Bianchi VIII: |s|Q/16 =', sp.Abs(S) * Qi / 16, ' sum =', E59 / 2 + W3 + sp.Rational(3, 32) * Q2)

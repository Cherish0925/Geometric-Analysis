"""Exact checks for the constants in round2_rigidity.md."""

import sympy as sp

R = sp.Rational
amin, amax, zmax = R(61, 384), R(67, 384), R(1, 512)
gap_lower = R(3, 2)*(amin-zmax)-sp.sqrt(6*amax*zmax)/2
assert sp.simplify(gap_lower-R(1, 8)).is_positive
qmax = 4+R(1, 16)+3*amax
assert qmax == R(587, 128) and qmax < 5
assert R(1+9**2, 64) == R(41, 32)

good_delta = R(1, 36) + 5/(216*R(1, 8))
assert good_delta == R(23, 108)
variance_delta = 2*R(1, 18)
variance_density = 2*R(41, 32)/72
assert variance_delta == R(1, 9)
assert variance_density == R(41, 1152)
bad_delta = 2*variance_delta
bad_density = 2*variance_density + 2*R(9, 32)*64
assert bad_density == 36+R(41, 576)
assert good_delta+bad_delta == R(47, 108) < 1
assert bad_density < 37
assert R(41, 32)/72 == R(41, 2304)

# Exact distance to the forbidden orbit and coupled spinor constants.
a, z = sp.symbols("a z", real=True)
assert sp.expand(R(3, 2)*a*a+R(1, 24)+(-a+z)/2
                 -(R(3, 2)*(a-R(1, 6))**2+z/2)) == 0
assert 2*R(4, 27) == R(8, 27)
assert 2*R(4, 9)*R(1, 12)*R(41, 32) == R(41, 432)
coupled_delta = R(9, 8)*R(16, 27)+R(20, 24)*R(8, 27)
coupled_density = R(1, 8)+R(9, 8)*576+R(20, 24)*R(41, 432)
assert coupled_delta == R(74, 81) < 1
assert coupled_density == R(1, 8)+648+R(205, 2592) < 649
assert (3+sp.sqrt(2))**2 < 20

v = sp.Matrix(sp.symbols("v0:3", real=True))
psi = sp.Matrix(sp.symbols("p0:3", real=True))
rho2, pv = psi.dot(psi), psi.dot(v)
derivative = pv*sp.eye(3)/12-(psi*v.T+v*psi.T)/8
assert sp.simplify(sp.trace(derivative.T*derivative)
                   -rho2*v.dot(v)/32-pv**2/96) == 0
assert R(9, 24) == R(3, 8)
assert 15+18*(R(1, 2)+R(25, 384)) < 26
assert 26*R(3, 8) < 10

# Covariant first-jet identity for the spinor model, including amplitude.
omega = []
for pairs in (((0, 1, 1), (2, 3, 1)),
              ((0, 2, 1), (3, 1, 1)),
              ((0, 3, 1), (1, 2, 1))):
    form = sp.zeros(4)
    for i, j, sign in pairs:
        form[i, j], form[j, i] = sign, -sign
    omega.append(form)
rho = sp.symbols("rho", positive=True)
cjet = sp.symbols("c0:4", real=True)
ajet = sp.symbols("a0:4", real=True)
bjet = sp.symbols("b0:4", real=True)
pjet = sp.Matrix([rho, 0, 0])
vjet = [sp.Matrix([cjet[i], ajet[i], bjet[i]]) for i in range(4)]
dmodel = [pjet.dot(vj)*sp.eye(3)/12-(pjet*vj.T+vj*pjet.T)/8 for vj in vjet]
grad_model2 = sum(sp.trace(dm.T*dm) for dm in dmodel)
div_model = sp.MutableDenseNDimArray.zeros(4, 4, 4)
for j in range(4):
    for k in range(4):
        for l in range(4):
            div_model[j, k, l] = sum(
                dmodel[i][a, b]*omega[a][i, j]*omega[b][k, l]/2
                for i in range(4) for a in range(3) for b in range(3)
            )
div_model2 = sum(div_model[j, k, l]**2 for j in range(4) for k in range(4) for l in range(4))
grad_form = [sum((vjet[i][a]*omega[a] for a in range(3)), sp.zeros(4))/sp.sqrt(2)
             for i in range(4)]
exterior = sp.MutableDenseNDimArray.zeros(4, 4, 4)
for i in range(4):
    for j in range(4):
        for k in range(4):
            exterior[i, j, k] = grad_form[i][j, k]+grad_form[j][k, i]+grad_form[k][i, j]
exterior2 = sum(exterior[i, j, k]**2 for i in range(4) for j in range(4) for k in range(4))/6
star_exterior = [sum(sp.LeviCivita(i, j, k, l)*exterior[i, j, k]
                    for i in range(4) for j in range(4) for k in range(4))/6 for l in range(4)]
contract_amp = [sum(cjet[i]*rho*omega[0][i, j]/sp.sqrt(2) for i in range(4)) for j in range(4)]
cross_amp = sum(contract_amp[j]*star_exterior[j] for j in range(4))
grad_form2 = sum(vj.dot(vj) for vj in vjet)
amp2 = sum(ci**2 for ci in cjet)
jet_identity_rhs = rho**2*(grad_form2-2*exterior2)/64+rho**2*amp2/32-rho*cross_amp/16
assert sp.expand(grad_model2-div_model2-jet_identity_rhs) == 0

# Model curvature potential is exactly rho^2/64 times the two-form term.
w0, w1, w2, w3, w4, scalar = sp.symbols("w0 w1 w2 w3 w4 scalar", real=True)
weyl = sp.Matrix([[w0, w1, w2], [w1, w3, w4], [w2, w4, -w0-w3]])
model = rho**2*sp.eye(3)/24-pjet*pjet.T/8
model_potential = scalar*sp.trace(model*model)/2-6*sp.trace(weyl*model*model)
form_potential = scalar*rho**2/3-2*(pjet.T*weyl*pjet)[0]
assert sp.expand(model_potential-rho**2*form_potential/64) == 0
assert sp.trace(model*model) == rho**4/96
assert -R(4, 3)*2+R(4, 6) == -2
assert -R(4, 3)*4+R(8, 6) == -4
assert R(4, 32) == R(1, 8)
assert R(4, 64) == R(1, 16)

# Four-dimensional bump powers in the endpoint example.
dimension = 4
frequency_power = R(3, 2)
R_l2_power = R(dimension, 2)-frequency_power
gradient_l2_power = R(dimension, 2)-frequency_power
product_l1_power = dimension-2*frequency_power
pairing_power = dimension-2*frequency_power-1
cutoff_pairing_power = dimension-frequency_power-1-1
assert (R_l2_power, gradient_l2_power, product_l1_power,
        pairing_power, cutoff_pairing_power) == (R(1, 2), R(1, 2), 1, 0, R(1, 2))

print("Exact round-two checks passed.")
print("Spectral gap lower bound:", gap_lower, "=", gap_lower.evalf())
print("Good-set q upper bound:", qmax)
print("Projection coefficients before rounding:", good_delta+bad_delta, bad_density)
print("Coupled approximation coefficients before rounding:", coupled_delta, coupled_density)
print("Endpoint scaling (R L2, grad a L2, product L1, pairing):",
      R_l2_power, gradient_l2_power, product_l1_power, pairing_power)
print("Full first-jet and intrinsic potential identities: passed")
print("Forced model derivative energies (gradient, divergence):", R(1, 8), R(1, 16))

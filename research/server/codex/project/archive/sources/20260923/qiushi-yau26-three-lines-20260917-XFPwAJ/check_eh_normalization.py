"""Exact checks for the Euler-angle convention added to the construction paper."""
import json
import sympy as s

r, theta, phi, psi = s.symbols('r theta phi psi', real=True)
coordinates = (r, theta, phi, psi)
x = s.Matrix([
    r*s.cos(theta/2)*s.cos((psi+phi)/2),
    r*s.cos(theta/2)*s.sin((psi+phi)/2),
    r*s.sin(theta/2)*s.cos((psi-phi)/2),
    r*s.sin(theta/2)*s.sin((psi-phi)/2),
])
frame = s.Matrix([
    [0, -s.sin(psi), s.cos(psi)*s.sin(theta), 0],
    [0, s.cos(psi), s.sin(psi)*s.sin(theta), 0],
    [0, 0, s.cos(theta), 1],
])
jacobian = x.jacobian(coordinates)
expected_metric = s.diag(1, 0, 0, 0) + r**2*frame.T*frame/4
assert all(s.trigsimp(s.expand_trig(v)) == 0
           for v in jacobian.T*jacobian-expected_metric)
jx = s.Matrix([-x[1], x[0], -x[3], x[2]])
assert all(s.trigsimp(s.expand_trig(v)) == 0
           for v in jx.T*jacobian-r**2*frame[2, :]/2)
for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
    for i in range(4):
        for j in range(i+1, 4):
            exterior = s.diff(frame[a, j], coordinates[i])-s.diff(frame[a, i], coordinates[j])
            wedge = frame[b, i]*frame[c, j]-frame[b, j]*frame[c, i]
            assert s.trigsimp(exterior-wedge) == 0
print(json.dumps({'euclidean_metric': 'passed', 'J_one_form': 'passed',
                  'three_structure_equations': 'passed'}))

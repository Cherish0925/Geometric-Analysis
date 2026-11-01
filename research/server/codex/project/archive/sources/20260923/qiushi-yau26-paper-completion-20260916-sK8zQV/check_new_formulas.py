"""Independent checks for newly expanded paper calculations; not global proofs."""
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm, expm_frechet
from scipy.integrate import quad_vec
import sympy as s


def require(condition, explanation):
    if not condition:
        raise RuntimeError(explanation)


t = s.symbols('t')
hermite = [1-10*t**3+15*t**4-6*t**5, t-6*t**3+8*t**4-3*t**5,
           (t**2-3*t**3+3*t**4-t**5)/2,
           10*t**3-15*t**4+6*t**5, -4*t**3+7*t**4-3*t**5,
           (t**3-2*t**4+t**5)/2]
jet_matrix = s.Matrix([[s.diff(poly, t, order).subs(t, end) for poly in hermite]
                      for end in (0, 1) for order in range(3)])
require(jet_matrix == s.eye(6), 'Hermite endpoint data do not match')
free = t**3 * (1-t)**3
require(all(s.diff(free, t, k).subs(t, end) == 0
            for end in (0, 1) for k in range(3)), 'Free correction changes endpoint jets')

# Noncommuting matrices test the integral formula, not a commuting shortcut.
X = np.array([[.2, .3, 0.], [.3, -.1, .15], [0., .15, .4]])
V = np.array([[1., -.2, .1], [-.2, 0., .25], [.1, .25, -.3]])
W = np.array([[0., .4, -.1], [.4, .7, 0.], [-.1, 0., .2]])
first, first_bound = quad_vec(lambda u: expm((1-u)*X) @ V @ expm(u*X), 0, 1)
first_error = float(np.max(np.abs(first - expm_frechet(X, V, compute_expm=False))))
def inner(u, v):
    return (expm((1-u)*X) @ V @ expm((u-v)*X) @ W @ expm(v*X)
            + expm((1-u)*X) @ W @ expm((u-v)*X) @ V @ expm(v*X))
second, second_bound = quad_vec(lambda u: quad_vec(lambda v: inner(u, v), 0, u)[0], 0, 1)
h = 1e-5
finite = (expm_frechet(X+h*W, V, compute_expm=False)
          - expm_frechet(X-h*W, V, compute_expm=False)) / (2*h)
second_error = float(np.max(np.abs(second - finite)))
require(first_error < 1e-12 and second_error < 1e-8, 'Matrix-exponential formula mismatch')
require(float(np.linalg.norm(X@V-V@X)) > .1, 'Fixture accidentally commutes')

# Centre jets cancel the full tangential Gaussian Einstein equation.
B = s.diag(1, 2, 3)
A = s.Matrix([[1, 1, 0], [1, -1, 2], [0, 2, 0]])
Rhat = s.Matrix([[-2, 1, 2], [1, -3, 1], [2, 1, -1-s.trace(A*A)]])
q = B*B
K = B*A*B
qrr = B*(2*(Rhat+3*s.eye(3))+4*A*A)*B
Kr = qrr/2
S = q.inv()*K
Ricq = B*Rhat*B
Err = 3-s.trace(q.inv()*Kr)+s.trace(S*S)
ET = Ricq+3*q-Kr-s.trace(S)*K+2*K*q.inv()*K
require(Err == 0 and ET == s.zeros(3), 'Centre Hamilton/tangential block mismatch')

report = {'status': 'passed', 'hermite_jet_matrix': str(jet_matrix),
          'matrix_exponential_numeric': {'first_max_error': first_error,
                                         'second_max_error': second_error,
                                         'scope': 'Numerical diagnostic, not interval certificate'},
          'gaussian_center_blocks': 'exact zero; mixed block requires momentum data',
          'scope': 'Endpoint and matrix formulas, not global existence or novelty'}
root = Path(__file__).resolve().parent
report['papers_sha256'] = {name: hashlib.sha256((root/'package/research'/name).read_bytes()).hexdigest()
                          for name in ['20260910.tex', '20260916_global.tex']}
with (root/'new-formula-checks.json').open('x') as handle:
    json.dump(report, handle, ensure_ascii=False, indent=2)
print(json.dumps(report, ensure_ascii=False))

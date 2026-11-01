import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = ['x', '2', '2', '4']
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'step57_general_form.py')).read()
exec(src.split('# ---------- quadrature')[0])
for a in range(11, 20):
    t = np.eye(20)[a]; R = riemann_from_operator(operator_from_params(t))
    Ric = np.einsum('abad->bd', R); s = np.trace(Ric)
    print(a, 'Ric0 |.|^2 =', round(float(np.sum((Ric - s / 4 * np.eye(4)) ** 2)), 6), 's', round(float(s), 8))
t = np.zeros(20); t[0] = 12; R = riemann_from_operator(operator_from_params(t)); print('s check', np.trace(np.einsum('abad->bd', R)))

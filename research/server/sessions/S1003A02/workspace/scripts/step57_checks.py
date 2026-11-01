import sys, os, json, time
import numpy as np
import jax, jax.numpy as jnp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step57_kernel_log_coefficient import *

t0 = time.time()
res = {}
# check 1: Burns scalar flat, not Ricci flat
Afun = tail_A()
x = jnp.array([0.3, -0.7, 0.5, 0.2])
for eps in [0.3, 1.0]:
    g = lambda y: jnp.eye(4) + eps * Afun(y)
    d, Ric, s = density_from_jet(*jet(g, x))
    print('Burns eps', eps, 'scalar', float(s), '|Ric0|^2', float(d))
# check 2: CH normalisation with J2
for name, J in [('J2', J2), ('J3', J3)]:
    gCH = ddbar_metric(lambda y: -jnp.log(1 - jnp.dot(y, y)), J)
    d, Ric, s = density_from_jet(*jet(gCH, jnp.zeros(4) + 1e-30))
    print(name, 'Ric at 0', np.round(np.array(Ric), 6).diagonal(), 'P-density', float(d))
    d, Ric, s = density_from_jet(*jet(gCH, jnp.array([0.2, 0.1, -0.3, 0.15])))
    print(name, ' Einstein check: |Ric0|^2 at generic point', float(d), 's', float(s))

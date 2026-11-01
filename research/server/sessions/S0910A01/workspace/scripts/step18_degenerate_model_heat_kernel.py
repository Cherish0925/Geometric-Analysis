#!/usr/bin/env python3
"""
Step 18 model for the degenerate transition operator.

Near a regular cutoff boundary take a(x)=x^2 on 0<x<=1.  The linear part of
K_t = a K_xx becomes, in y=log x,

    u_t = u_yy - u_y,       y in (-infty,0].

The target weighted curvature is f=aK=x^2K=e^{2y}u.  This script estimates the
operator norm from initial ||K_0||_{L^2(dx)} to sup_y e^{2y}|u(y,t)| for the
full-line heat-with-drift kernel.  It is only a model calculation.
"""
import math
import numpy as np
from scipy.integrate import quad


def kernel(y, z, t):
    # u_t = u_yy - u_y has transport velocity +1: a spike centered at z
    # moves to z+t.  Kernel center is y=z+t.
    return (4*math.pi*t)**(-0.5) * math.exp(-((y - z - t)**2)/(4*t))


def norm_bound_at_y(y, t):
    # Analytic Cauchy-Schwarz bound for z <= 0:
    # I = ∫ G(y,z,t)^2 e^{-z} dz, with G centered at z+t.
    # Completing the square gives
    # I=(4πt)^(-1) exp(-y+3t/2) ∫_{-∞}^0 exp(-(z-(y-2t))^2/(2t)) dz.
    # The finite upper limit is important for stable far-boundary spike tests.
    erf_arg = (2*t - y) / math.sqrt(2*t)
    gaussian_tail = math.sqrt(math.pi*t/2) * (1 + math.erf(erf_arg))
    I = (4*math.pi*t)**(-1) * math.exp(-y + 1.5*t) * gaussian_tail
    return math.exp(2*y) * math.sqrt(I)


print("Degenerate model heat-kernel bound for a=x^2")
print("Target: sup_y x^2 K(y,t) <= C(t) ||K0||_{L2(dx)}")

for t in [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1.0]:
    ys = np.linspace(-40, 0, 1201)
    vals = np.array([norm_bound_at_y(float(y), t) for y in ys])
    imax = int(np.argmax(vals))
    print(f"t={t:8.1e}: C(t)~{vals[imax]:10.4e}, max y={ys[imax]:7.3f}, C*t^(1/4)={vals[imax]*t**0.25:10.4e}")

print("\nSpike test: normalize narrow Gaussian spikes in L2(dx) and evaluate x^2K after t=0.01")
t = 1e-2
width = 0.05
for z0 in [-2, -5, -10, -20, -35]:
    # Exact full-line normalization for u0=A exp(-(z-z0)^2/(2w^2)) in L2(e^z dz):
    # int exp(-(z-z0)^2/w^2) e^z dz = sqrt(pi) w exp(z0+w^2/4).
    norm_int = math.sqrt(math.pi) * width * math.exp(z0 + width**2/4)
    A = 1.0 / math.sqrt(norm_int)
    ys = np.linspace(max(-50, z0-5), min(0, z0+5), 801)
    outs = []
    lo, hi = z0 - 8*width, z0 + 8*width
    for y in ys:
        conv, _ = quad(lambda z: kernel(y, z, t)*A*math.exp(-((z-z0)**2)/(2*width**2)),
                       lo, hi, epsabs=1e-12, epsrel=1e-10, limit=200)
        outs.append(math.exp(2*y)*abs(conv))
    outs = np.array(outs)
    imax = int(np.argmax(outs))
    bound = norm_bound_at_y(float(ys[imax]), t)
    print(f"  spike z0={z0:6.1f}, A={A:10.3e}: sup x^2K={outs[imax]:10.4e} at y={ys[imax]:7.3f}; CS bound there={bound:10.4e}")

print("\nInterpretation: in this one-dimensional normal model, degeneration alone does not create an unbounded aK from unit L2(dx) curvature.  This supports, but does not prove, the desired degenerate epsilon-regularity; the real geometric problem still includes tangential variables, nonlinear reaction, tensor cutoff terms, and coupled E estimates.")

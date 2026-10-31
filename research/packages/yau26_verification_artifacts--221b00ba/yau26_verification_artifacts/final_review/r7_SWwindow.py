# sanity check of prop:SW: rho(delta)=max over eigenvalue box of 12|E0|^2/s^2, and the "in particular" clause
import numpy as np, itertools
def rho(delta,N=41):
    g=np.linspace(-delta,delta,N); best=0
    for d in itertools.product(g,repeat=4):
        d=np.array(d); s=-4+d.sum(); E2=(d**2).sum()-d.sum()**2/4
        best=max(best,12*E2/s**2)
    return best
for delta in (0.1,0.2,0.25,0.268,0.3,0.4,0.49):
    r=rho(delta,N=21)
    print("delta=%.3f  rho_num=%.6f  3d^2=%.6f  9d^2/(2-d)^2=%.6f  => max r=2rho/3=%.5f  vs 2d^2=%.5f, 6d^2/(2-d)^2=%.5f"%(delta,r,3*delta**2,9*delta**2/(2-delta)**2,2*r/3,2*delta**2,6*delta**2/(2-delta)**2))

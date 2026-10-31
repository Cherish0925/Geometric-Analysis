# Check the report's Table (football) against the leading-order prediction  L*delta ~ sup_t |psi''(t)/L + 6 psi'(t)| / 36
import mpmath as mp
mp.mp.dps=40
f=lambda t: mp.e**(-1/t) if t>0 else mp.mpf(0)
psi=lambda t: f(t)/(f(t)+f(1-t))
for ex,Lrep,drep in ((8,2.526,0.135117),(16,7.131,0.046850),(32,16.341,0.020407),(64,34.762,0.0095899),(128,71.603,0.0046554)):
    a=mp.mpf(10)**(-ex); L=mp.log(a**mp.mpf('0.25')/(8*a**mp.mpf('0.5')))
    best=0
    for i in range(1,4000):
        t=mp.mpf(i)/4000
        v=abs(mp.diff(psi,t,2)/L**2+6*mp.diff(psi,t)/L)/36
        best=max(best,v)
    print("a=1e-%d  L=%.3f (report %.3f)  predicted delta=%.6f  report delta=%.6f  ratio=%.5f"%(ex,L,Lrep,best,drep,drep/float(best)))

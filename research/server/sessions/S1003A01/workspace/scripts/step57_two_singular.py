"""Step 57b: Singular elimination for the X-free two-direction invariance tower.
Usage: CHAR=0|32003 N=6 python step57_two_singular.py
Ideal I_N = <Phi_1..Phi_N> in Q[h1,h2,h3,W1,W2,W3] (lam=-Q eliminated), saturated by
mu1*mu2*(mu1-mu2) (rank-deficient and single-direction strata removed).  Prints the
Krull dimension of each I_N; for the final one, minimal associated primes.
Projective dimension = Krull - 1.  A lam != 0 strict invariant solution requires
Krull dim >= 2 on a component where Q != 0 and q != 0.
"""
import json, os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
N = int(os.environ.get('N', '6')); CH = os.environ.get('CHAR', '0')
d = os.path.join(here, '../data/step57')
T = json.load(open(os.path.join(d, f'two_tower_N{max(N,6)}.json')))
Phi = [p.replace('**', '^') for p in T['Phi'][:N]]
mu = [m.replace('**', '^') for m in T['mu']]
Q = T['Q'].replace('**', '^')
fn = os.path.join(d, f'two_sat_N{N}_p{CH}.sing')
with open(fn, 'w') as f:
    f.write('LIB "elim.lib"; LIB "primdec.lib";\noption(redSB);\n')
    f.write(f'ring r={CH},(h1,h2,h3,W1,W2,W3),dp;\n')
    f.write(f'poly m1={mu[0]}; poly m2={mu[1]}; poly m3={mu[2]}; poly QQ={Q};\n')
    f.write('poly sg=m1*m2*(m1-m2);\n')
    for n in range(N):
        f.write(f'poly P{n+1}={Phi[n]};\n')
    f.write('ideal I; ideal J;\n')
    for n in range(1, N+1):
        f.write(f'I=I,P{n}; J=sat(I,sg)[1]; J=std(J); print("N={n} dim="+string(dim(J))+" vdim/mult="+string(mult(J)));\n')
        f.write('I=J;\n')
    f.write('list L=minAssGTZ(J); print("components: "+string(size(L)));\n')
    f.write('int i; for(i=1;i<=size(L);i++){print("--- comp "+string(i)+" dim "+string(dim(std(L[i])))); print(L[i]);'
            ' print("Q in comp? "+string(reduce(QQ,std(L[i]))==0));}\n')
    f.write('quit;\n')
r = subprocess.run(['Singular', '-q', fn], capture_output=True, text=True,
                   timeout=int(os.environ.get('TMO', '3000')))
print(r.stdout[-20000:]); print(r.stderr[-3000:])
open(fn.replace('.sing', '.out'), 'w').write(r.stdout + '\n' + r.stderr)

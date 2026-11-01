"""Step 57c: rational reconstruction + exact verification of the surviving
two-direction component.
1. mod a large prime p: J_N = sat(<Phi_1..Phi_N>, mu1 mu2 (mu1-mu2)), minimal primes.
2. farey-lift each prime to Q, then verify over Q:
   Phi_1 in P, D(g) in P for every generator g (invariance of V(P) under the
   lam=-Q Einstein flow), mu1, mu2, mu1-mu2, Q not in P.
Outputs ../data/step57/two_lift.out (Singular text) and two_lift_P*.txt.
"""
import json, os, subprocess, sys
import sympy as sp
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import step57_classA_metric_only as M
d = os.path.join(here, '../data/step57')
T = json.load(open(os.path.join(d, 'two_tower_N6.json')))
N = int(os.environ.get('N', '5'))
Phi = [p.replace('**', '^') for p in T['Phi'][:N]]
mu = [m.replace('**', '^') for m in T['mu']]
Qs = T['Q'].replace('**', '^')
# vector field with lam=-Q, as Singular polys
Vs = [str(sp.expand(M.V[v].subs(M.lam, -M.Q))).replace('**', '^') for v in list(M.h) + list(M.W)]
p = int(os.environ.get('P', '32003'))
fn = os.path.join(d, 'two_lift.sing')
with open(fn, 'w') as f:
    f.write('LIB "primdec.lib"; LIB "modstd.lib";\noption(redSB);\n')
    f.write(f'ring rp={p},(h1,h2,h3,W1,W2,W3),dp;\n')
    f.write(f'poly sg=({mu[0]})*({mu[1]})*(({mu[0]})-({mu[1]}));\n')
    for n in range(N):
        f.write(f'poly P{n+1}={Phi[n]};\n')
    f.write('ideal I; ideal J;\n')
    for n in range(1, N+1):
        f.write(f'I=I,P{n}; J=std(sat(I,sg)[1]); print("N={n} modp dim "+string(dim(J))+" mult "+string(mult(J))); I=J;\n')
    f.write('list L=minAssGTZ(J); int nL=size(L); print("modp comps "+string(nL));\n')
    f.write('ring r0=0,(h1,h2,h3,W1,W2,W3),dp;\n')
    f.write('list L0; int i; int j; ideal Pz;\n')
    f.write(f'poly m1={mu[0]}; poly m2={mu[1]}; poly Qc={Qs}; poly F1={Phi[0]};\n')
    f.write('ideal VF=' + ','.join(Vs) + ';\n')
    f.write('proc Dv(poly g){ poly r=0; int k; for(k=1;k<=6;k++){ r=r+diff(g,var(k))*VF[k]; } return(r); }\n')
    f.write('for(i=1;i<=nL;i++){ setring rp; ideal Pi=L[i]; setring r0; ideal Pq=farey(fetch(rp,Pi),' + str(p) + '); Pq=std(Pq);\n')
    f.write('  print("=== component "+string(i)+" dim "+string(dim(Pq))+" deg "+string(mult(Pq)));\n')
    f.write('  print(Pq);\n')
    f.write('  print("Phi1 in P: "+string(reduce(F1,Pq)==0));\n')
    f.write('  int inv=1; for(j=1;j<=size(Pq);j++){ if(reduce(Dv(Pq[j]),Pq)!=0){inv=0;} } print("invariant: "+string(inv));\n')
    f.write('  print("m1 in P: "+string(reduce(m1,Pq)==0)+"  m2 in P: "+string(reduce(m2,Pq)==0)+"  m1-m2 in P: "+string(reduce(m1-m2,Pq)==0)+"  Q in P: "+string(reduce(Qc,Pq)==0));\n')
    f.write('  write(":w ' + os.path.join(d, 'two_lift_P') + '"+string(i)+".txt", Pq);\n')
    f.write('  kill Pq; setring rp; kill Pi; setring r0; }\n')
    f.write('quit;\n')
with open(os.path.join(d, 'two_lift.out'), 'w') as fo:
    r = subprocess.run(['Singular', '-q', fn], stdout=fo, stderr=subprocess.STDOUT,
                       timeout=int(os.environ.get('TMO', '1500')))
out = '\n'.join(l for l in open(os.path.join(d, 'two_lift.out')).read().splitlines() if 'redefining' not in l)
print(out[-20000:])

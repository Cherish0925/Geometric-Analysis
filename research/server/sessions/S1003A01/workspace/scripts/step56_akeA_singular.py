"""Step 56d: export the exact propagated constraint tower to Singular and test
strictness by saturation.  Usage: EPS=+-1 MODE=single|two python step56_ake_singular.py NK LAM
Writes ../data/step56/sing_<mode>_eps<e>_lam<L>.sing and runs Singular on it.
single: strict  <=> alpha2 != 0 or alpha3 != 0 (q = 2(a^2 mu1^2 + alpha2^2 + alpha3^2)/(abc)^2).
"""
import sympy as sp, os, sys, subprocess
sys.path.insert(0, os.path.dirname(__file__))
import step56_akeA_propagate as P
mode = os.environ.get('MODE', 'single'); NK = int(sys.argv[1])
LAM = P.lam if sys.argv[2] == 'sym' else sp.Rational(sys.argv[2])
sa, sb, sc, A_, B_, C_ = P.sa, P.sb, P.sc, P.A_, P.B_, P.C_; X = P.X; e = P.eps
num = lambda z: sp.numer(sp.together(z))
if mode == 'single':
    sub = {X[0]: 1, X[1]: 0, X[2]: 0}
    tower = [num(P.MU[0])]
    vs = [sa, sb, sc, A_, B_, C_]
    strict = [num(sp.together(P.q.subs(sub)))]
elif mode == 'two':
    sub = {X[2]: 0, X[1]: 1 - X[0]}
    tower = [num(sp.together(sum(X[i]*P.MU[i] for i in range(3)).subs(sub)))]
    vs = [sa, sb, sc, A_, B_, C_, X[0]]
    qn = num(sp.together(P.q.subs(sub)))
    strict = [qn]
else:
    sub = {X[2]: 1 - X[0] - X[1]}
    tower = [num(sp.together(sum(X[i]*P.MU[i] for i in range(3)).subs(sub)))]
    vs = [sa, sb, sc, A_, B_, C_, X[0], X[1]]
    qn = num(sp.together(P.q.subs(sub)))
    strict = [qn]
for n in range(1, NK):
    tower.append(sp.expand(num(sp.together(P.Dt(tower[-1]).subs(sub)))))
gens = [sp.expand(num(P.H).subs(P.lam, LAM))] + [sp.expand(k.subs(P.lam, LAM)) for k in tower]
names = ['a', 'b', 'c', 'A', 'B', 'C', 'X1', 'X2'][:len(vs)]
if LAM == P.lam:
    vs = vs + [P.lam]; names = names + ['l']
ren = dict(zip(vs, sp.symbols(names)))
def S(z): return str(sp.expand(z.subs(ren))).replace('**', '^')
L = str(LAM).replace('/', '_').replace('-', 'm')
fn = os.path.join(os.path.dirname(__file__), f'../data/step56/singA_{"".join(map(lambda v: str(v).replace("-","m"),P.B.NB))}_{mode}_eps{e}_lam{L}_K{NK}_p{os.environ.get("CHAR","0")}.sing')
extra = {'single': '', 'two': '*X1*(1-X1)', 'three': '*X1*X2*(1-X1-X2)'}[mode]
with open(fn, 'w') as f:
    f.write('LIB "elim.lib";\noption(redSB);\n')
    f.write(f'ring r={os.environ.get("CHAR","0")},({",".join(names)}),dp;\n')
    f.write('ideal I=' + ',\n'.join(S(g) for g in gens) + ';\n')
    f.write(f'ideal J=sat(I,a*b*c{extra})[1];\n')
    f.write('print("dim(J) (Krull, incl. complex):"); print(dim(std(J)));\n')
    for i, s in enumerate(strict):
        f.write(f'poly s{i}={S(s)};\n')
        f.write(f'ideal Js{i}=sat(J,s{i})[1];\n')
        f.write(f'print("strict saturation {i}:"); print(Js{i}); print(dim(std(Js{i})));\n')
    f.write('quit;\n')
print('wrote', fn, flush=True)
r = subprocess.run(['Singular', '-q', fn], capture_output=True, text=True, timeout=int(os.environ.get('TMO', '1500')))
print(r.stdout[-6000:]); print(r.stderr[-2000:])
open(fn.replace('.sing', '.out'), 'w').write(r.stdout + '\n' + r.stderr)

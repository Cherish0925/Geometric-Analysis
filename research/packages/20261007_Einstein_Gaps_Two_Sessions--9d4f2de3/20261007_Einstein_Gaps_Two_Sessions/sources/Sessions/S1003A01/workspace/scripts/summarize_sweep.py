"""Summarize a cell sweep directory: best j per (Rc, mu, mode)."""
import json, glob, sys, collections
d = sys.argv[1]
best = collections.defaultdict(lambda: None)
n = 0
for f in glob.glob(d + '/*.jsonl'):
    for line in open(f):
        x = json.loads(line); n += 1
        if x['pen'] > 1e-8:
            continue
        k = (x['Rc'], x['mu'], x['mode'])
        if best[k] is None or x['j'] < best[k]['j']:
            best[k] = x
print('records', n)
print(f"{'Rc':>5} {'mu':>7} {'mode':>8} {'j_best':>10} {'(2+mu)^2/(1-mu^2/R^4)':>22}")
for k in sorted(best):
    x = best[k]
    print(f"{k[0]:5.2f} {k[1]:7.4f} {k[2]:>8} {x['j']:10.5f} {x['kahler_bound']:22.5f}")

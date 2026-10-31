#!/bin/bash
# Step 15 batch: continuation of the ACH1 bolt branch to both ends, and complete sign-change
# enumeration of U_f(b,d) for the three possible ACH fibre slots.
S=Sessions/S1003A02/workspace/scripts/ach_projected.py
O=Sessions/S1003A02/workspace/data/ach_projected
python $S cont 0.29 0.000826293617 0.005 80 down > $O/cont_down.log 2>&1 &
python $S cont 8.0 7.17402860308 400 60 up > $O/cont_up.log 2>&1 &
python $S cont 0.75 0.238048384506 0.85 20 min > $O/cont_min.log 2>&1 &
for b in 0.03 0.1 0.2 0.3 0.5 0.8 1.5 3 8 20; do
  for f in 0 1 2; do
    python $S roots $b $f 1e-3 > $O/roots_b${b}_f${f}.log 2>&1 &
  done
done
wait
cat $O/roots_*.log | grep '^{' | python -c "
import sys, json
for l in sys.stdin:
    r = json.loads(l)
    print(r['b'], 'slot', r['slot'], 'hit', r['n_hit'], '/', r['n'], 'min_dev %.3g' % (r['min_dev'] or -1),
          [(round(x['d1'], 12), round(x['dev1'] or -1, 4), round(x['dev2'] or -1, 4)) for x in r['roots']])
"
tail -n 3 $O/cont_down.log $O/cont_up.log $O/cont_min.log

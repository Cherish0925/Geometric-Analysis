#!/bin/bash
# Run the projected ACH1 branch solver over b in four parallel groups; summarize.
D=Sessions/S1003A02/workspace/data/ach_projected
S=Sessions/S1003A02/workspace/scripts/ach_projected.py
timeout 1500 python $S branch 0.29,0.32,0.35,0.4,0.45,0.5 brA > Sessions/S1003A02/workspace/data/ach_projected/brA.log 2>&1 &
timeout 1500 python $S branch 0.55,0.6,0.65,0.7,0.75,0.8 brB > Sessions/S1003A02/workspace/data/ach_projected/brB.log 2>&1 &
timeout 1500 python $S branch 0.85,0.9,0.95,1.0,1.1,1.2,1.3 brC > Sessions/S1003A02/workspace/data/ach_projected/brC.log 2>&1 &
timeout 1500 python $S branch 1.5,2.0,3.0,4.0,6.0,8.0,12.0,16.0 brD > Sessions/S1003A02/workspace/data/ach_projected/brD.log 2>&1 &
wait
for f in $D/brA.log $D/brB.log $D/brC.log $D/brD.log; do
python - "$f" <<'EOF'
import json, sys
for l in open(sys.argv[1]):
    if l.startswith('{'):
        r = json.loads(l)
        print(r['b'], *[(k, round(v['d'], 12), round(v['rho'], 9), round(v['dev'], 5)) if v.get('found') else (k, 'NF')
                         for k, v in r.items() if k != 'b'])
    else:
        print(l.strip()[:200])
EOF
done

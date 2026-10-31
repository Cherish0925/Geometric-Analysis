"""Run step37 transport jobs with bounded concurrency.

Input: a text file; each line is 'NAME ARGS...' (ARGS passed to the given script).
Writes OUTDIR/NAME.json and OUTDIR/NAME.log.  Returns nonzero if any job failed.
Usage: python step37_run_jobs.py SCRIPT RECORD JOBFILE OUTDIR [-P n] [--extra "..."]
"""
import argparse, shlex, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ap = argparse.ArgumentParser(); ap.add_argument("script"); ap.add_argument("record")
ap.add_argument("jobfile"); ap.add_argument("outdir"); ap.add_argument("-P", type=int, default=6)
ap.add_argument("--extra", default="")
a = ap.parse_args(); out = Path(a.outdir); out.mkdir(parents=True, exist_ok=True)
jobs = [l.split(None, 1) for l in Path(a.jobfile).read_text().splitlines() if l.strip()]

def run(j):
    name, rest = j[0], (j[1] if len(j) > 1 else "")
    cmd = [sys.executable, a.script, a.record] + shlex.split(rest) + shlex.split(a.extra) + ["--out", str(out/f"{name}.json")]
    with open(out/f"{name}.log", "w") as fh:
        r = subprocess.run(cmd, stdout=fh, stderr=subprocess.STDOUT)
    return name, r.returncode

with ThreadPoolExecutor(a.P) as ex:
    res = list(ex.map(run, jobs))
bad = [n for n, c in res if c != 0]
print("failed:", bad)
sys.exit(1 if bad else 0)
